"""Market data: Yahoo Finance 5-minute bars (stocks + crypto), Coinbase
fallback for crypto, an on-disk cache, FX, and a synthetic generator for
offline tests and demos.

Bars are indexed by their UTC start time and contain only *completed* bars.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

from .config import Asset, Config

log = logging.getLogger(__name__)

COLUMNS = ["open", "high", "low", "close", "volume"]
INTERVAL_SECONDS = {"1m": 60, "2m": 120, "5m": 300, "15m": 900, "30m": 1800, "60m": 3600, "1h": 3600}
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


class RateLimited(RuntimeError):
    """The provider refused us for making too many requests (HTTP 429)."""


def _http_json(url: str, timeout: float = 20.0, retries: int = 3):
    last_error = None
    for attempt in range(retries):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read(20_000_000))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ConnectionError) as error:
            last_error = error
            if isinstance(error, urllib.error.HTTPError):
                if error.code in (400, 401, 403, 404):
                    break
                if error.code == 429:
                    if attempt >= 1:
                        raise RateLimited(f"GET {url.split('?')[0]}: HTTP 429 Too Many Requests") from error
                    time.sleep(1.0)
                    continue
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET {url.split('?')[0]} failed: {last_error}")


def _range_days(range_: str) -> float:
    if not range_.endswith("d"):
        raise ValueError(f"Unsupported range {range_!r}")
    return float(range_[:-1])


def empty_bars() -> pd.DataFrame:
    return pd.DataFrame(columns=COLUMNS, index=pd.DatetimeIndex([], tz="UTC"), dtype=float)


def clean_bars(frame: pd.DataFrame, interval: str, now: pd.Timestamp | None = None) -> pd.DataFrame:
    """Drop invalid rows, irregular timestamps and the still-forming bar."""
    if frame.empty:
        return empty_bars()
    seconds = INTERVAL_SECONDS[interval]
    frame = frame[COLUMNS].astype(float)
    frame = frame[~frame.index.duplicated(keep="last")].sort_index()
    frame.index = frame.index.as_unit("ns")  # one resolution everywhere (pandas 3 may infer seconds)
    epoch = frame.index.asi8 // 10**9
    frame = frame[epoch % seconds == 0]
    frame = frame.dropna(subset=["open", "high", "low", "close"])
    frame = frame[(frame[["open", "high", "low", "close"]] > 0).all(axis=1)]
    frame["volume"] = frame["volume"].fillna(0.0).clip(lower=0)
    # Repair slightly inconsistent OHLC instead of discarding the symbol.
    frame["high"] = frame[["open", "high", "low", "close"]].max(axis=1)
    frame["low"] = frame[["open", "high", "low", "close"]].min(axis=1)
    now = now or pd.Timestamp.now(tz="UTC")
    frame = frame[frame.index + pd.Timedelta(seconds=seconds) <= now]
    return frame


def parse_yahoo(payload: dict, interval: str = "5m", now: pd.Timestamp | None = None) -> tuple[pd.DataFrame, str]:
    chart = payload.get("chart") or {}
    if chart.get("error") or not chart.get("result"):
        raise ValueError(f"Yahoo returned no chart: {chart.get('error')}")
    result = chart["result"][0]
    meta = result.get("meta", {})
    currency = meta.get("currency") or "USD"
    timestamps = result.get("timestamp") or []
    quote = (result.get("indicators", {}).get("quote") or [{}])[0]
    if not timestamps:
        return empty_bars(), currency
    frame = pd.DataFrame({key: pd.to_numeric(pd.Series(quote.get(key, [None] * len(timestamps))), errors="coerce")
                          for key in COLUMNS})
    frame.index = pd.to_datetime(np.asarray(timestamps, dtype="int64"), unit="s", utc=True)
    scale = 0.01 if currency in ("GBp", "GBX") else 1.0
    frame[["open", "high", "low", "close"]] *= scale
    return clean_bars(frame, interval, now), ("GBP" if scale != 1.0 else currency)


def fetch_yahoo(symbol: str, interval: str = "5m", range_: str = "60d", now=None) -> pd.DataFrame:
    """Plain HTTP to Yahoo's chart API (often rate-limited from cloud servers)."""
    params = urllib.parse.urlencode({"interval": interval, "range": range_, "includePrePost": "false"})
    last_error = None
    for host in ("query1", "query2"):
        url = f"https://{host}.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?{params}"
        try:
            frame, _ = parse_yahoo(_http_json(url), interval, now)
            return frame
        except (RuntimeError, ValueError) as error:
            last_error = error
    if isinstance(last_error, RateLimited):
        raise RateLimited(f"Yahoo {symbol}: {last_error}")
    raise RuntimeError(f"Yahoo {symbol}: {last_error}")


def fetch_yfinance(symbol: str, interval: str = "5m", range_: str = "60d", now=None) -> pd.DataFrame:
    """Yahoo via the yfinance library, which copes with Yahoo's bot blocking."""
    import yfinance as yf
    from yfinance.exceptions import YFRateLimitError

    now = pd.Timestamp.now(tz="UTC") if now is None else now
    days = min(_range_days(range_), 59.0)  # Yahoo keeps 60 days of intraday bars
    ticker = yf.Ticker(symbol)
    try:
        frame = ticker.history(start=now - pd.Timedelta(days=days), end=now + pd.Timedelta(minutes=10),
                               interval=interval, prepost=False, actions=False, auto_adjust=False,
                               raise_errors=True, timeout=20)
    except YFRateLimitError as error:
        raise RateLimited(f"yfinance {symbol}: {error}") from error
    if frame is None or frame.empty:
        return empty_bars()
    frame = frame.rename(columns=str.lower)
    frame.index = pd.DatetimeIndex(frame.index).tz_convert("UTC")
    currency = (ticker.history_metadata or {}).get("currency") or "USD"
    if currency in ("GBp", "GBX"):
        frame[["open", "high", "low", "close"]] *= 0.01
    return clean_bars(frame, interval, now)


def fetch_coinbase_range(symbol: str, interval: str = "5m", range_: str = "2d", now=None) -> pd.DataFrame:
    return fetch_coinbase(symbol, interval, days=min(_range_days(range_), 60.0), now=now)


def fetch_coinbase(symbol: str, interval: str = "5m", days: float = 2.0, now=None) -> pd.DataFrame:
    """Coinbase Exchange public candles (crypto only). 300 candles per call."""
    seconds = INTERVAL_SECONDS[interval]
    if seconds not in (60, 300, 900, 3600):
        raise ValueError("Unsupported Coinbase granularity")
    end = pd.Timestamp.now(tz="UTC") if now is None else now
    start = end - pd.Timedelta(days=days)
    rows = []
    cursor = start
    while cursor < end:
        chunk_end = min(cursor + pd.Timedelta(seconds=seconds * 300), end)
        params = urllib.parse.urlencode({"granularity": seconds, "start": cursor.isoformat(), "end": chunk_end.isoformat()})
        data = _http_json(f"https://api.exchange.coinbase.com/products/{symbol}/candles?{params}")
        rows.extend(data)
        cursor = chunk_end
        time.sleep(0.15)
    if not rows:
        return empty_bars()
    frame = pd.DataFrame(rows, columns=["time", "low", "high", "open", "close", "volume"])
    frame.index = pd.to_datetime(frame.pop("time").astype("int64"), unit="s", utc=True)
    return clean_bars(frame, interval, now)


def merge_bars(old: pd.DataFrame, new: pd.DataFrame, keep_days: int = 62) -> pd.DataFrame:
    if old.empty:
        combined = new
    elif new.empty:
        combined = old
    else:
        combined = pd.concat([old[~old.index.isin(new.index)], new]).sort_index()
    if not combined.empty:
        combined.index = combined.index.as_unit("ns")
        combined = combined[combined.index >= combined.index[-1] - pd.Timedelta(days=keep_days)]
    return combined


class MarketData:
    """Keeps a rolling window of bars per symbol, cached on disk."""

    def __init__(self, config: Config, cache_dir: str | Path | None = None, fetcher=None):
        self.config = config
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.fetcher = fetcher  # a custom fetcher replaces the provider chain (tests)
        self.cooldown: dict[str, float] = {}
        self.bars: dict[str, pd.DataFrame] = {}
        self.errors: dict[str, str] = {}
        self.gbpusd: pd.Series = pd.Series(dtype=float)
        self.last_fetch: dict[str, pd.Timestamp] = {}
        self.last_fx: pd.Timestamp | None = None
        self.live: set[str] | None = None  # symbols needing timely prices (None = all)
        self._dirty: set[str] = set()
        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            log_path = self.cache_dir / "fetch_log.json"
            if log_path.exists():
                try:
                    self.last_fetch = {s: pd.Timestamp(t) for s, t in json.loads(log_path.read_text()).items()}
                except (ValueError, OSError) as error:
                    log.warning("Ignoring fetch log: %s", error)
            for asset in config.universe:
                self._load(asset.symbol)

    def _path(self, symbol: str) -> Path:
        return self.cache_dir / f"{symbol.replace('/', '_')}.csv.gz"

    def _load(self, symbol: str) -> None:
        if not self.cache_dir or symbol in self.bars:
            return
        path = self._path(symbol)
        if path.exists():
            try:
                frame = pd.read_csv(path, index_col=0)
                frame.index = pd.to_datetime(frame.index, utc=True).as_unit("ns")
                self.bars[symbol] = frame[COLUMNS].astype(float)
            except Exception as error:  # corrupt cache: refetch
                log.warning("Ignoring cache for %s: %s", symbol, error)
                self.last_fetch.pop(symbol, None)
        else:
            self.last_fetch.pop(symbol, None)

    def set_universe(self, config: Config, live: set[str] | None = None) -> None:
        """Switch to a (larger) universe, e.g. with copy-trading tickers added.

        Symbols outside ``live`` only feed backtests and are refreshed rarely."""
        self.config = config
        self.live = live
        for asset in config.universe:
            self._load(asset.symbol)

    def _providers(self, kind: str) -> list[tuple[str, object]]:
        if self.fetcher is not None:
            return [("custom", self.fetcher)]
        chain = [("yfinance", fetch_yfinance), ("yahoo", fetch_yahoo)]
        if kind == "crypto":
            chain.insert(0, ("coinbase", fetch_coinbase_range))
        return chain

    def _fetch_symbol(self, symbol: str, kind: str, interval: str, range_: str, now) -> pd.DataFrame:
        """Try each provider in turn; a rate-limited provider is skipped for 10 minutes."""
        errors = []
        for name, provider in self._providers(kind):
            if self.cooldown.get(name, 0.0) > time.monotonic():
                errors.append(f"{name}: cooling down after a rate limit")
                continue
            try:
                return provider(symbol, interval, range_, now=now)
            except ImportError as error:
                errors.append(f"{name}: not installed ({error})")
            except RateLimited as error:
                self.cooldown[name] = time.monotonic() + 600
                errors.append(f"{name}: {error}")
            except Exception as error:
                errors.append(f"{name}: {error}")
        raise RuntimeError("; ".join(errors)[:600] or "no data provider")

    def _fetch(self, asset: Asset, range_: str, now) -> pd.DataFrame:
        return self._fetch_symbol(asset.symbol, asset.kind, self.config.interval, range_, now)

    def _due(self, asset: Asset, old: pd.DataFrame, now: pd.Timestamp) -> bool:
        """Only hit the provider when a new completed bar could exist."""
        from .sessions import is_open

        last_fetch = self.last_fetch.get(asset.symbol)
        if old.empty or last_fetch is None:
            return True
        waited = now - last_fetch
        if self.live is not None and asset.symbol not in self.live:
            return waited >= pd.Timedelta(hours=6)
        bar = pd.Timedelta(seconds=INTERVAL_SECONDS[self.config.interval])
        if not is_open(asset.kind, now) and not is_open(asset.kind, now - 2 * bar):
            return waited >= pd.Timedelta(minutes=30)
        if not asset.trade_strategies and waited < pd.Timedelta(minutes=15):
            return False  # held for weeks: fresher prices add nothing
        next_bar_done = old.index[-1] + 2 * bar
        return now >= next_bar_done or waited >= bar

    def refresh(self, now: pd.Timestamp | None = None) -> dict[str, str]:
        """Fetch new bars where due. Returns {symbol: error} for failures."""
        now = now or pd.Timestamp.now(tz="UTC")
        errors = {s: e for s, e in self.errors.items() if s in self.bars and not self._due(self.config.asset(s), self.bars[s], now)}
        jobs = []
        for asset in self.config.universe:
            old = self.bars.get(asset.symbol, empty_bars())
            if not self._due(asset, old, now):
                continue
            gap = now - old.index[-1] if not old.empty else pd.Timedelta(days=999)
            if asset.symbol not in self.last_fetch or gap > pd.Timedelta(days=4):
                range_ = self.config.history_range
            elif gap < pd.Timedelta(hours=2) and now.hour >= 1:
                range_ = "1d"
            else:
                range_ = "5d"
            jobs.append((asset, range_))

        def fetch(job):
            asset, range_ = job
            try:
                return asset, self._fetch(asset, range_, now), None
            except Exception as error:
                return asset, None, error

        changed = False
        started = time.monotonic()
        with ThreadPoolExecutor(max_workers=6) as pool:
            for asset, new, error in pool.map(fetch, jobs):
                if error is not None:
                    errors[asset.symbol] = str(error)[:300]
                    log.warning("Data error for %s: %s", asset.symbol, error)
                    continue
                self.bars[asset.symbol] = merge_bars(self.bars.get(asset.symbol, empty_bars()), new)
                self.last_fetch[asset.symbol] = now
                self._dirty.add(asset.symbol)
                changed = True
        if jobs:
            log.info("Fetched %d/%d symbols in %.1fs", len(jobs) - len([j for j in jobs if j[0].symbol in errors]),
                     len(jobs), time.monotonic() - started)
        self.errors = errors
        if self.last_fx is None or now - self.last_fx >= pd.Timedelta(minutes=30):
            self._refresh_fx(now)
            self.last_fx = now
        if changed:
            self.save()
        return self.errors

    def _refresh_fx(self, now):
        if not any(asset.currency == "USD" for asset in self.config.universe):
            return
        try:
            interval = self.config.interval if self.fetcher is not None else "1h"
            frame = self._fetch_symbol("GBPUSD=X", "fx", interval, "30d", now)
            if not frame.empty:
                self.gbpusd = frame["close"]
        except Exception as error:
            log.warning("FX fetch failed, using fallback GBPUSD: %s", error)

    def save(self):
        if not self.cache_dir:
            return
        for symbol in sorted(self._dirty):
            if symbol in self.bars:
                self.bars[symbol].to_csv(self._path(symbol), compression="gzip", float_format="%.8g")
        self._dirty.clear()
        log_path = self.cache_dir / "fetch_log.json"
        log_path.write_text(json.dumps({s: t.isoformat() for s, t in self.last_fetch.items()}))

    def fx_to_gbp(self, currency: str, at: pd.Timestamp | None = None) -> float:
        """Multiply a price in ``currency`` by this to get GBP."""
        if currency == "GBP":
            return 1.0
        if currency != "USD":
            raise ValueError(f"No FX for {currency}")
        rate = self.config.gbpusd_fallback
        if not self.gbpusd.empty:
            series = self.gbpusd if at is None else self.gbpusd[self.gbpusd.index <= at]
            if not series.empty and np.isfinite(series.iloc[-1]) and series.iloc[-1] > 0:
                rate = float(series.iloc[-1])
        return 1.0 / rate


# ---------------------------------------------------------------- synthetic

def synthetic_bars(config: Config, days: int = 30, seed: int = 7, end: pd.Timestamp | None = None,
                   random_walk: bool = False) -> dict[str, pd.DataFrame]:
    """Regime-switching random walks on each asset's real trading calendar.

    Used for offline tests/demos only. Contains trends and mean-reverting
    stretches so every strategy family gets exercised. ``random_walk=True``
    gives a pure random walk with no exploitable structure (used to check that
    nothing "profits" from look-ahead bias).
    """
    from .sessions import session_mask

    rng = np.random.default_rng(seed)
    seconds = INTERVAL_SECONDS[config.interval]
    end = (end or pd.Timestamp.now(tz="UTC")).floor(f"{seconds}s")
    index = pd.date_range(end - pd.Timedelta(days=days), end, freq=f"{seconds}s", tz="UTC", inclusive="left")
    out = {}
    for number, asset in enumerate(config.universe):
        mask = session_mask(index, asset.kind)
        idx = index[mask]
        n = len(idx)
        vol = (0.004 if asset.kind == "crypto" else 0.0025) * rng.uniform(0.6, 1.6)
        regime = np.zeros(n)
        state, drift = 0, 0.0
        for i in range(n):
            if rng.random() < 0.01:
                state = rng.integers(0, 3)
                drift = rng.normal(0, vol * 0.25)
            regime[i] = drift if state == 1 else 0.0
        shocks = rng.standard_t(4, n) * vol / np.sqrt(2)
        # Trend regimes plus an Ornstein-Uhlenbeck wobble around a slow anchor.
        log_price = np.zeros(n)
        anchor = 0.0
        for i in range(1, n):
            if random_walk:
                log_price[i] = log_price[i - 1] + shocks[i]
                continue
            anchor += regime[i]
            pull = 0.03 * (anchor - log_price[i - 1])
            log_price[i] = log_price[i - 1] + regime[i] + pull + shocks[i]
        base = 100.0 * (1 + number)
        close = base * np.exp(log_price)
        open_ = np.r_[close[0], close[:-1]] * np.exp(rng.normal(0, vol * 0.1, n))
        spread = np.abs(rng.normal(0, vol * 0.6, n))
        high = np.maximum(open_, close) * np.exp(spread)
        low = np.minimum(open_, close) * np.exp(-spread)
        volume = rng.lognormal(10, 0.6, n) * (1 + 3 * np.abs(shocks) / vol / 5)
        out[asset.symbol] = pd.DataFrame({"open": open_, "high": high, "low": low, "close": close, "volume": volume}, index=idx)
    return out


class StaticData(MarketData):
    """MarketData over a fixed dict of bars (tests / backtests)."""

    def __init__(self, config: Config, bars: dict[str, pd.DataFrame], gbpusd: float | None = None):
        super().__init__(config, cache_dir=None, fetcher=lambda *a, **k: empty_bars())
        self.bars = dict(bars)
        if gbpusd:
            self.gbpusd = pd.Series([gbpusd], index=[pd.Timestamp("2000-01-01", tz="UTC")])

    def refresh(self, now=None):
        return {}
