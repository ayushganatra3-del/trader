"""Daily-bar sleeves: market timing and multi-day swing setups.

These need years of daily history, which the 5-minute data (60 days) cannot
give. A signal on a completed daily bar takes effect at the next US open, so
each sleeve is a schedule of target weights (a ``CopyBook``) and is traded
and backtested exactly like the copy-trading sleeves.

* Nasdaq timing (O'Neil/IBD method, as in tradermonty/claude-trading-skills):
  count distribution days (index down >= 0.2% on higher volume) over the last
  25 sessions and cut exposure as they pile up (100/75/50/25%). After a
  correction, stay out until a follow-through day (day 4-10 of a rally
  attempt, +1.25% on higher volume) or a new 63-session closing high.
  No exposure while ^VXN >= 35.
* Momentum burst (Stockbee): a +4% day on rising volume that closes near its
  high; hold 4 sessions or until the trigger-day low breaks.
* Exhaustion hammer (Stockbee): a long-lower-wick reversal that undercuts
  recent lows during a pullback in an uptrend; hold 5 sessions.
* Bullish score (staskh/trading_skills): SMA/RSI/MACD/EMA/ADX/momentum
  checklist; hold the best-scoring names.
"""
from __future__ import annotations

import json
import logging
import urllib.parse
from pathlib import Path

import numpy as np
import pandas as pd

from .config import Config
from .copytrade import CopyBook, _next_open_utc
from .data import COLUMNS, _http_json
from .indicators import ema, wilder

log = logging.getLogger(__name__)

NEW_YORK = "America/New_York"
VXN, VIX = "^VXN", "^VIX"
TIMING = "Timing: Nasdaq FTD"
BURST = "Daily: Momentum burst"
HAMMER = "Daily: Exhaustion hammer"
SCORE = "Daily: Bullish score"
EXPOSURE = ((2, 1.0, "normal"), (4, 0.75, "caution"), (5, 0.5, "high"))  # (max distribution days, exposure, level)
SEVERE = (0.25, "severe")


# ------------------------------------------------------------------ data

def completed(frame: pd.DataFrame, now: pd.Timestamp) -> pd.DataFrame:
    """Drop today's bar until the US session has closed."""
    local = now.tz_convert(NEW_YORK)
    today = pd.Timestamp(local.date())
    closed = local.hour * 60 + local.minute >= 16 * 60 + 10
    return frame[frame.index <= today] if closed else frame[frame.index < today]


def _tidy(frame: pd.DataFrame, now: pd.Timestamp) -> pd.DataFrame:
    frame = frame.rename(columns=str.lower)[COLUMNS].astype(float)
    frame = frame.dropna(subset=["open", "high", "low", "close"])
    frame = frame[(frame[["open", "high", "low", "close"]] > 0).all(axis=1)]
    frame["volume"] = frame["volume"].fillna(0.0)
    index = pd.DatetimeIndex(frame.index)
    if index.tz is not None:
        index = index.tz_convert(NEW_YORK).tz_localize(None)
    frame.index = index.normalize().as_unit("ns")
    frame = frame[~frame.index.duplicated(keep="last")].sort_index()
    return completed(frame, now)


def fetch_daily_yfinance(symbols: list[str], period: str, now: pd.Timestamp) -> dict[str, pd.DataFrame]:
    """One batched yfinance download of split/dividend-adjusted daily bars."""
    import yfinance as yf

    raw = yf.download(symbols, period=period, interval="1d", auto_adjust=True, actions=False,
                      group_by="ticker", threads=True, progress=False, timeout=30)
    out = {}
    for symbol in symbols:
        try:
            frame = raw[symbol] if isinstance(raw.columns, pd.MultiIndex) else raw
        except KeyError:
            continue
        frame = _tidy(frame, now)
        if len(frame):
            out[symbol] = frame
    return out


def fetch_daily_yahoo(symbol: str, period: str, now: pd.Timestamp) -> pd.DataFrame:
    """Fallback: Yahoo's chart API, adjusted with its adjclose series."""
    params = urllib.parse.urlencode({"interval": "1d", "range": period})
    payload = _http_json(f"https://query2.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?{params}")
    result = payload["chart"]["result"][0]
    quote = result["indicators"]["quote"][0]
    frame = pd.DataFrame({key: pd.to_numeric(pd.Series(quote.get(key)), errors="coerce") for key in COLUMNS})
    frame.index = pd.to_datetime(np.asarray(result["timestamp"], dtype="int64"), unit="s", utc=True)
    adj = (result["indicators"].get("adjclose") or [{}])[0].get("adjclose")
    if adj:
        ratio = pd.to_numeric(pd.Series(adj, index=frame.index), errors="coerce") / frame["close"]
        frame[["open", "high", "low", "close"]] = frame[["open", "high", "low", "close"]].mul(ratio.fillna(1.0), axis=0)
    return _tidy(frame, now)


def _last_close(now: pd.Timestamp) -> pd.Timestamp:
    """The most recent weekday 16:10 New York time at or before ``now``."""
    local = now.tz_convert(NEW_YORK)
    close = local.normalize() + pd.Timedelta(hours=16, minutes=10)
    while close > local or close.dayofweek >= 5:
        close -= pd.Timedelta(days=1)
    return close.tz_convert("UTC")


class DailyData:
    """Daily bars for the stock universe plus ^VXN/^VIX, cached on disk.

    Refetched every ``refresh_hours`` and soon after each US close."""

    def __init__(self, symbols, cache_dir: str | Path | None = None, period: str = "2y",
                 refresh_hours: float = 3.0, fetcher=None):
        self.symbols = list(dict.fromkeys(list(symbols) + [VXN, VIX]))
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.period = period
        self.refresh_hours = refresh_hours
        self.fetcher = fetcher  # fetcher(symbols, period, now) -> {symbol: frame}; for tests
        self.bars: dict[str, pd.DataFrame] = {}
        self.fetched_at: pd.Timestamp | None = None
        self.error: str | None = None
        if self.cache_dir and self.cache_dir.exists():
            for symbol in self.symbols:
                path = self._path(symbol)
                if path.exists():
                    try:
                        frame = pd.read_csv(path, index_col=0)
                        frame.index = pd.to_datetime(frame.index).as_unit("ns")
                        self.bars[symbol] = frame[COLUMNS].astype(float)
                    except Exception as error:  # corrupt cache: refetch
                        log.warning("Ignoring daily cache for %s: %s", symbol, error)
            try:
                self.fetched_at = pd.Timestamp(json.loads((self.cache_dir / "fetched.json").read_text())["at"])
            except (OSError, ValueError, KeyError):
                self.fetched_at = None
            if set(self.symbols) - set(self.bars):
                self.fetched_at = None

    def _path(self, symbol: str) -> Path:
        return self.cache_dir / f"{symbol.replace('^', '_')}.csv.gz"

    def due(self, now: pd.Timestamp) -> bool:
        if self.fetched_at is None:
            return True
        return now - self.fetched_at >= pd.Timedelta(hours=self.refresh_hours) or self.fetched_at < _last_close(now)

    def refresh(self, now: pd.Timestamp | None = None) -> str | None:
        now = pd.Timestamp.now(tz="UTC") if now is None else now
        if not self.due(now):
            return self.error
        try:
            fresh = (self.fetcher or fetch_daily_yfinance)(self.symbols, self.period, now)
        except Exception as error:  # yfinance down or rate-limited: try the plain API
            log.warning("Daily bars via yfinance failed: %s", error)
            fresh = {}
        missing = [s for s in self.symbols if s not in fresh]
        if missing and self.fetcher is None:
            failures = 0
            for symbol in missing:
                if failures >= 2:  # the source is down: try again on the next refresh
                    break
                try:
                    fresh[symbol] = fetch_daily_yahoo(symbol, self.period, now)
                    failures = 0
                except (RuntimeError, ValueError, KeyError, IndexError, TypeError) as error:
                    log.warning("Daily bars for %s failed: %s", symbol, error)
                    failures += 1
        got = {s: f for s, f in fresh.items() if f is not None and len(f)}
        self.bars.update(got)
        missing = [s for s in self.symbols if s not in got]
        self.error = f"no daily bars for {', '.join(missing)}" if missing else None
        self.fetched_at = now
        if self.cache_dir and got:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            for symbol, frame in got.items():
                frame.to_csv(self._path(symbol))
            (self.cache_dir / "fetched.json").write_text(json.dumps({"at": now.isoformat()}))
        return self.error


# ------------------------------------------------------------------ market timing

def distribution_flags(bars: pd.DataFrame, drop: float = 0.002) -> pd.Series:
    close, volume = bars["close"], bars["volume"]
    return (close.pct_change() <= -drop) & (volume > volume.shift(1))


def market_regime(bars: pd.DataFrame, vxn: pd.Series | None = None, window: int = 25,
                  vxn_gate: float = 35.0) -> pd.DataFrame:
    """Per session: uptrend/correction state, distribution count, rally day
    and the exposure to hold into the next session."""
    close = bars["close"].to_numpy()
    low = bars["low"].to_numpy()
    volume = bars["volume"].to_numpy()
    n = len(close)
    dist = distribution_flags(bars).to_numpy()
    sma50 = bars["close"].rolling(50, min_periods=50).mean().to_numpy()
    high63 = bars["close"].rolling(63, min_periods=1).max().to_numpy()
    vol_index = vxn.reindex(bars.index).ffill().to_numpy() if vxn is not None else np.full(n, np.nan)

    rows = []
    state, since = "uptrend", 0  # distribution days only count after the last follow-through
    swing_low = rally_day = 0
    day1_low = np.nan
    for i in range(n):
        count = 0
        for j in range(max(since, i - window + 1), i + 1):
            if dist[j] and close[j:i + 1].max() < close[j] * 1.05:  # a 5% rally erases a distribution day
                count += 1
        ftd = False
        up = i > 0 and close[i] > close[i - 1]
        if state == "uptrend":
            broken = close[i] <= high63[i] * 0.90 or (count >= 5 and np.isfinite(sma50[i]) and close[i] < sma50[i])
            if broken:
                state, swing_low, rally_day = "correction", close[i], 0
        elif close[i] >= high63[i]:  # a new 63-session closing high ends a correction without a textbook FTD
            state, since, rally_day, count = "uptrend", i + 1, 0, 0
        elif close[i] < swing_low:
            swing_low, rally_day = close[i], 0
        elif rally_day == 0:
            if up:
                rally_day, day1_low = 1, low[i]
        else:
            rally_day += 1
            if rally_day <= 3 and close[i] < day1_low:
                rally_day = 0
            elif 4 <= rally_day <= 10 and close[i] / close[i - 1] - 1 >= 0.0125 and volume[i] > volume[i - 1]:
                state, since, rally_day, ftd, count = "uptrend", i + 1, 0, True, 0
            elif rally_day > 10:
                rally_day = 0
        if state == "correction":
            exposure, level = 0.0, "correction"
        else:
            exposure, level = next(((e, name) for limit, e, name in EXPOSURE if count <= limit), SEVERE)
        gated = np.isfinite(vol_index[i]) and vol_index[i] >= vxn_gate
        if gated:
            exposure = 0.0
        if i == 0 or state != rows[-1][0]:
            changed = bars.index[i]
        rows.append((state, level, count, rally_day, ftd, exposure, vol_index[i], gated, changed))
    return pd.DataFrame(rows, index=bars.index, columns=["state", "level", "distribution_days", "rally_day",
                                                         "follow_through", "exposure", "vxn", "vxn_gate", "since"])


# ------------------------------------------------------------------ swing setups

def _hold(trigger: pd.Series, stop: pd.Series, close: pd.Series, days: int) -> pd.Series:
    """True on each session after whose close we want to hold (from a trigger
    for ``days`` sessions, or until a close below the trigger-day stop)."""
    trig, stops, c = trigger.fillna(False).to_numpy(), stop.to_numpy(), close.to_numpy()
    out = np.zeros(len(c), bool)
    left, level = 0, np.nan
    for i in range(len(c)):
        if left and c[i] < level:
            left = 0
        if trig[i]:
            left, level = days, stops[i]
        if left:
            out[i] = True
            left -= 1
    return pd.Series(out, index=close.index)


def momentum_burst(bars: pd.DataFrame, days: int = 4) -> pd.Series:
    c, h, lo, v = bars["close"], bars["high"], bars["low"], bars["volume"]
    location = (c - lo) / (h - lo).replace(0, np.nan)
    trigger = ((c / c.shift(1) >= 1.04) & (v > v.shift(1)) & (location >= 0.7)
               & (c.shift(1) / c.shift(4) - 1 < 0.08))  # not already extended
    return _hold(trigger, lo, c, days)


def exhaustion_hammer(bars: pd.DataFrame, days: int = 5) -> pd.Series:
    o, c, h, lo, v = bars["open"], bars["close"], bars["high"], bars["low"], bars["volume"]
    span = (h - lo).replace(0, np.nan)
    body = (c - o).abs()
    lower = pd.concat([o, c], axis=1).min(axis=1) - lo
    upper = h - pd.concat([o, c], axis=1).max(axis=1)
    hammer = (lower >= 2 * body) & (lower >= 0.5 * span) & (upper <= 0.25 * span) & ((c - lo) / span >= 0.6)
    sma50 = c.rolling(50, min_periods=50).mean()
    pullback = 1 - c / c.rolling(20, min_periods=20).max()
    trigger = (hammer & (c > sma50) & (sma50 > sma50.shift(10)) & pullback.between(0.05, 0.25)
               & (lo < lo.rolling(5, min_periods=5).min().shift(1)) & (v >= v.rolling(20, min_periods=20).mean()))
    return _hold(trigger, lo, c, days)


def bullish_score(bars: pd.DataFrame) -> pd.Series:
    """staskh/trading_skills' bullish composite, computed causally for every day."""
    c, h, lo = bars["close"], bars["high"], bars["low"]
    score = (c > c.rolling(20, min_periods=20).mean()).astype(float)
    score += (c > c.rolling(50, min_periods=50).mean()).astype(float)
    delta = c.diff()
    gain, loss = wilder(delta.clip(lower=0), 14), wilder(-delta.clip(upper=0), 14)
    rsi = 100 - 100 / (1 + gain / loss.replace(0, np.nan))
    score += np.select([rsi.between(50, 70), rsi.between(30, 50, inclusive="left"), rsi < 30], [1.0, 0.5, 0.25], 0.0)
    line = ema(c, 12) - ema(c, 26)
    signal = ema(line, 9)
    hist = line - signal
    score += (line > signal).astype(float) + 0.5 * (hist > hist.shift(1))
    fast_up = ema(c, 9) > ema(c, 21)
    score += np.where(fast_up, 0.5, -0.25)
    score += np.select([fast_up & (line > signal), ~fast_up & (line < signal)], [0.5, -0.5], 0.0)
    up, down = h.diff(), -lo.diff()
    tr = pd.concat([h - lo, (h - c.shift(1)).abs(), (lo - c.shift(1)).abs()], axis=1).max(axis=1)
    atr = wilder(tr, 14).replace(0, np.nan)
    plus = 100 * wilder(up.where((up > down) & (up > 0), 0.0), 14) / atr
    minus = 100 * wilder(down.where((down > up) & (down > 0), 0.0), 14) / atr
    adx = wilder(100 * (plus - minus).abs() / (plus + minus).replace(0, np.nan), 14)
    score += np.select([(adx > 25) & (plus > minus), plus > minus], [1.5, 0.5], 0.0)
    score += ((c / c.shift(63) - 1) * 100 / 20).clip(-1, 2).fillna(0.0)
    return score.where(c.rolling(63, min_periods=63).count() >= 63)


def top_scores(scores: pd.DataFrame, top_n: int, minimum: float) -> pd.DataFrame:
    """Hold the ``top_n`` best names scoring >= ``minimum``; keep a holding
    until its score falls a point below that, so the sleeve does not churn."""
    held: list[str] = []
    rows = []
    for _, row in scores.iterrows():
        row = row.dropna()
        held = [s for s in held if row.get(s, -np.inf) >= minimum - 1]
        for symbol in row[row >= minimum].sort_values(ascending=False).index:
            if len(held) >= top_n:
                break
            if symbol not in held:
                held.append(symbol)
        rows.append({s: 1.0 for s in held})
    return pd.DataFrame(rows, index=scores.index, columns=scores.columns).fillna(0.0)


# ------------------------------------------------------------------ books

def schedule(weights: pd.DataFrame, sessions: int = 150) -> list:
    """Turn per-session target weights into [[effective UTC time, {ticker: w}]]
    entries, each effective from the next US open."""
    out, last = [], None
    for day, row in weights.tail(sessions).iterrows():
        targets = {s: round(float(w), 4) for s, w in row.items() if w > 1e-9}
        if targets != last:
            out.append([_next_open_utc(pd.Timestamp(day)).isoformat(), targets])
            last = targets
    return out


def _equal(active: pd.DataFrame, slots: int) -> pd.DataFrame:
    count = active.sum(axis=1)
    return active.astype(float).div(np.maximum(count, slots), axis=0)


def daily_symbols(config: Config) -> list[str]:
    stocks = [a.symbol for a in config.universe if a.kind == "us_equity" and a.trade_strategies]
    return list(dict.fromkeys([config.daily.index, *stocks]))


def daily_books(daily: dict[str, pd.DataFrame], config: Config, fetched_at: pd.Timestamp) -> tuple[list[CopyBook], dict]:
    """All daily sleeves as books, plus the latest market regime for the dashboard."""
    cfg = config.daily
    stamp = fetched_at.isoformat()
    stocks = [a.symbol for a in config.universe
              if a.kind == "us_equity" and a.trade_strategies and a.symbol in daily and len(daily[a.symbol]) >= 80]
    books, regime = [], {}
    index = daily.get(cfg.index)
    if index is not None and len(index) >= 80:
        frame = market_regime(index, daily.get(VXN, pd.DataFrame()).get("close"), vxn_gate=cfg.vxn_gate)
        last = frame.iloc[-1]
        vix = daily.get(VIX)
        regime = {"index": cfg.index, "session": frame.index[-1].strftime("%Y-%m-%d"), "state": last["state"],
                  "since": last["since"].strftime("%Y-%m-%d"),
                  "level": last["level"], "distribution_days": int(last["distribution_days"]),
                  "rally_day": int(last["rally_day"]), "exposure": float(last["exposure"]),
                  "vxn": None if pd.isna(last["vxn"]) else round(float(last["vxn"]), 2),
                  "vix": round(float(vix["close"].iloc[-1]), 2) if vix is not None and len(vix) else None,
                  "last_follow_through": (frame.index[frame["follow_through"]][-1].strftime("%Y-%m-%d")
                                          if frame["follow_through"].any() else None)}
        for ticker in cfg.timing_tickers:
            if ticker in config.symbols:
                books.append(CopyBook(
                    f"{TIMING} · {ticker}", kind="daily", cap=1.0, source=f"{cfg.index} daily bars, ^VXN",
                    description=(f"Market timing: holds {ticker} sized by {cfg.index} distribution days in the last 25 "
                                 "sessions (0-2: 100%, 3-4: 75%, 5: 50%, 6+: 25%); out in a correction until a "
                                 f"follow-through day; out while ^VXN >= {cfg.vxn_gate:.0f}"),
                    schedule=schedule(frame[["exposure"]].rename(columns={"exposure": ticker})),
                    as_of=regime["session"], updated_at=stamp))
    if stocks:
        slots = config.risk.slots
        setups = ((BURST, momentum_burst, cfg.burst_hold_days,
                   "Stockbee momentum burst: +4% day on rising volume closing near its high; holds up to "
                   f"{cfg.burst_hold_days} sessions, exits if the trigger-day low breaks"),
                  (HAMMER, exhaustion_hammer, cfg.hammer_hold_days,
                   "Stockbee exhaustion hammer: long-lower-wick reversal that undercuts recent lows in a 5-25% "
                   f"pullback within an uptrend; holds up to {cfg.hammer_hold_days} sessions"))
        for name, rule, days, text in setups:
            active = pd.DataFrame({s: rule(daily[s], days) for s in stocks}).fillna(False)
            books.append(CopyBook(name, text, "daily bars", schedule(_equal(active, slots)), kind="daily",
                                  as_of=active.index[-1].strftime("%Y-%m-%d"), updated_at=stamp))
        scores = pd.DataFrame({s: bullish_score(daily[s]) for s in stocks})
        held = top_scores(scores, cfg.score_top_n, cfg.score_min)
        books.append(CopyBook(
            SCORE, f"staskh bullish score (SMA, RSI, MACD, EMA, ADX, 3-month momentum; max about 9): holds the top "
                   f"{cfg.score_top_n} names scoring {cfg.score_min:g}+", "daily bars",
            schedule(_equal(held > 0, cfg.score_top_n)), kind="daily",
            as_of=held.index[-1].strftime("%Y-%m-%d"), updated_at=stamp))
        latest = scores.iloc[-1].dropna().sort_values(ascending=False)
        regime["top_scores"] = {s: round(float(v), 2) for s, v in latest.head(6).items()}
    return books, regime
