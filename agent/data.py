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


def _http_json(url: str, timeout: float = 20.0, retries: int = 3):
    last_error = None
    for attempt in range(retries):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read(20_000_000))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ConnectionError) as error:
            last_error = error
            if isinstance(error, urllib.error.HTTPError) and error.code in (400, 404):
                break
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET {url.split('?')[0]} failed: {last_error}")


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
    params = urllib.parse.urlencode({"interval": interval, "range": range_, "includePrePost": "false"})
    last_error = None
    for host in ("query1", "query2"):
        url = f"https://{host}.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?{params}"
        try:
            frame, _ = parse_yahoo(_http_json(url), interval, now)
            return frame
        except (RuntimeError, ValueError) as error:
            last_error = error
    raise RuntimeError(f"Yahoo {symbol}: {last_error}")


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
        self.fetcher = fetcher or fetch_yahoo
        self.bars: dict[str, pd.DataFrame] = {}
        self.errors: dict[str, str] = {}
        self.gbpusd: pd.Series = pd.Series(dtype=float)
        self.last_fetch: dict[str, pd.Timestamp] = {}
        self.last_fx: pd.Timestamp | None = None
        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            for asset in config.universe:
                path = self._path(asset.symbol)
                if path.exists():
                    try:
                        frame = pd.read_csv(path, index_col=0)
                        frame.index = pd.to_datetime(frame.index, utc=True).as_unit("ns")
                        self.bars[asset.symbol] = frame[COLUMNS].astype(float)
                    except Exception as error:  # corrupt cache: refetch
                        log.warning("Ignoring cache for %s: %s", asset.symbol, error)

    def _path(self, symbol: str) -> Path:
        return self.cache_dir / f"{symbol.replace('/', '_')}.csv.gz"

    def _fetch(self, asset: Asset, range_: str, now) -> pd.DataFrame:
        try:
            return self.fetcher(asset.symbol, self.config.interval, range_, now=now)
        except Exception as error:
            if asset.kind != "crypto" or self.fetcher is not fetch_yahoo:
                raise
            log.warning("Yahoo failed for %s (%s); trying Coinbase", asset.symbol, error)
            days = 60.0 if range_.endswith("d") and int(range_[:-1]) > 5 else 2.0
            return fetch_coinbase(asset.symbol, self.config.interval, days=days, now=now)

    def _due(self, asset: Asset, old: pd.DataFrame, now: pd.Timestamp) -> bool:
        """Only hit the provider when a new completed bar could exist."""
        from .sessions import is_open

        last_fetch = self.last_fetch.get(asset.symbol)
        if old.empty or last_fetch is None:
            return True
        bar = pd.Timedelta(seconds=INTERVAL_SECONDS[self.config.interval])
        if not is_open(asset.kind, now) and not is_open(asset.kind, now - 2 * bar):
            return now - last_fetch >= pd.Timedelta(minutes=30)
        next_bar_done = old.index[-1] + 2 * bar
        return now >= next_bar_done or now - last_fetch >= bar

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
            frame = self.fetcher("GBPUSD=X", "1h" if self.fetcher is fetch_yahoo else self.config.interval, "60d", now=now)
            if not frame.empty:
                self.gbpusd = frame["close"]
        except Exception as error:
            log.warning("FX fetch failed, using fallback GBPUSD: %s", error)

    def save(self):
        if not self.cache_dir:
            return
        for symbol, frame in self.bars.items():
            frame.to_csv(self._path(symbol), compression="gzip", float_format="%.8g")

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
