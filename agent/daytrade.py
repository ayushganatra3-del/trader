"""Day-trading sleeves from published research.

Each builder returns target weights on the research index (a weight set on a
bar's close earns the next bar's return), so backtests and paper trading use
the same rules. Stops are checked on each completed 5-minute bar and exit at
that bar's close, which is a little worse than a resting stop order.

* ORB 5m (Zarattini & Aziz 2023, "Can Day Trading Really Be Profitable?"):
  trade the direction of the first 5-minute candle of QQQ from the second
  candle, stop at the other end of that candle, target 10R, flat at the close.
  Long = TQQQ, short = SQQQ (this account cannot short).
* Stocks in Play ORB (Zarattini, Barbon & Aziz 2024, "A Profitable Day Trading
  Strategy for the U.S. Equity Market"): each morning take the stocks with the
  highest relative volume in the first 5 minutes and a green first candle; buy
  a break of the opening-range high, stop 10% of the daily ATR below it, flat
  at the close. Long side only.
* Noise-area momentum (Zarattini, Aziz & Barbon 2024, "Beat the Market: An
  Effective Intraday Momentum Strategy for S&P500 ETF"): the "noise area" is
  the day's open +/- the average move from the open at that time of day over
  the last 14 days. Every half hour, go long above it or short below it; exit
  when price crosses back through the band or VWAP; flat at the close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

NEW_YORK = "America/New_York"
LAST_MINUTE = 380  # bars starting 15:50 or later: be flat (exit at the 15:50 bar's close)


def _open_end(last_loc: int, index: pd.DatetimeIndex, final_day: bool) -> int:
    """Where a position with no exit yet stops: the end of the research index
    on the day still trading (so the latest target holds it), else just after
    the day's last bar (e.g. an early-close half day)."""
    return len(index) if final_day else last_loc + 1


def _session(bars: pd.DataFrame) -> pd.DataFrame:
    """Regular-session bars with their New York day and minutes since 09:30."""
    local = bars.index.tz_convert(NEW_YORK)
    minute = local.hour * 60 + local.minute - (9 * 60 + 30)
    frame = bars.assign(day=local.normalize().tz_localize(None), minute=np.asarray(minute))
    return frame[(frame["minute"] >= 0) & (frame["minute"] < 390)]


def _daily_atr(session: pd.DataFrame, n: int = 14) -> pd.Series:
    """ATR of completed days, known before each day starts (index = day)."""
    daily = session.groupby("day").agg(high=("high", "max"), low=("low", "min"), close=("close", "last"))
    prev = daily["close"].shift(1)
    tr = pd.concat([daily["high"] - daily["low"], (daily["high"] - prev).abs(), (daily["low"] - prev).abs()], axis=1).max(axis=1)
    return tr.rolling(n, min_periods=5).mean().shift(1)


def orb_5m(bars: dict[str, pd.DataFrame], index: pd.DatetimeIndex, symbols: list[str], signal: str,
           long: str | None, short: str | None, target_r: float = 10.0) -> np.ndarray | None:
    if signal not in bars or not any(s in symbols for s in (long, short) if s):
        return None
    column = {s: j for j, s in enumerate(symbols)}
    weights = np.zeros((len(index), len(symbols)))
    session = _session(bars[signal])
    loc = pd.Series(index.get_indexer(session.index), index=session.index)
    final = session["day"].iloc[-1] if len(session) else None
    for day_key, day in session.groupby("day"):
        first = day[day["minute"] == 0]
        if first.empty:
            continue
        o, h, lo, c = (float(first[k].iloc[0]) for k in ("open", "high", "low", "close"))
        if c > o and long in column:
            side, stop, risk = column[long], lo, c - lo
            target = c + target_r * risk
        elif c < o and short in column:
            side, stop, risk = column[short], h, h - c
            target = c - target_r * risk
        else:
            continue
        if risk <= 0:
            continue
        start = loc[first.index[0]]
        end = None
        for ts, bar in day[day["minute"] > 0].iterrows():
            if bar["minute"] >= LAST_MINUTE:
                end = loc[ts]
                break
            if (c > o and (bar["low"] <= stop or bar["high"] >= target)) or \
               (c < o and (bar["high"] >= stop or bar["low"] <= target)):
                end = loc[ts]
                break
        if end is None:
            end = _open_end(loc[day.index[-1]], index, day_key == final)
        if start >= 0 and end > start:
            weights[start:end, side] = 1.0
    return weights


def stocks_in_play(bars: dict[str, pd.DataFrame], index: pd.DatetimeIndex, symbols: list[str],
                   candidates: list[str], top_n: int = 4, min_relvol: float = 1.0, stop_atr: float = 0.10,
                   lookback: int = 14) -> np.ndarray | None:
    column = {s: j for j, s in enumerate(symbols)}
    names = [s for s in candidates if s in bars and s in column]
    if not names or top_n <= 0:
        return None
    weights = np.zeros((len(index), len(symbols)))
    firsts, sessions, atrs = {}, {}, {}
    for s in names:
        session = _session(bars[s])
        if session.empty:
            continue
        sessions[s] = session
        first = session[session["minute"] == 0].set_index("day")
        first = first.assign(relvol=first["volume"] / first["volume"].rolling(lookback, min_periods=5).mean().shift(1))
        firsts[s] = first
        atrs[s] = _daily_atr(session)
    days = sorted({d for f in firsts.values() for d in f.index})
    final = days[-1] if days else None
    for day in days:
        ranked = []
        for s, first in firsts.items():
            if day not in first.index:
                continue
            row = first.loc[day]
            atr = atrs[s].get(day, np.nan)
            if row["close"] > row["open"] and row["relvol"] >= min_relvol and np.isfinite(atr) and atr > 0:
                ranked.append((row["relvol"], s, row["high"], atr))
        for _, s, or_high, atr in sorted(ranked, reverse=True)[:top_n]:
            day_bars = sessions[s][sessions[s]["day"] == day]
            loc = index.get_indexer(day_bars.index)
            stop = or_high - stop_atr * atr
            start = end = None
            for k, (_, bar) in enumerate(day_bars.iterrows()):
                if bar["minute"] == 0:
                    continue
                if bar["minute"] >= LAST_MINUTE:
                    end = loc[k]
                    break
                if start is None:
                    if bar["high"] > or_high:  # the buy-stop at the opening-range high fills in this bar
                        start = loc[k]
                        if bar["close"] <= stop:
                            end = loc[k] + 1
                            break
                elif bar["low"] <= stop:
                    end = loc[k]
                    break
            if start is None:
                continue
            if end is None:
                end = _open_end(loc[-1], index, day == final)
            if end > start:
                weights[start:end, column[s]] += 1.0 / top_n
    return weights


def noise_area(bars: dict[str, pd.DataFrame], index: pd.DatetimeIndex, symbols: list[str], signal: str,
               long: str | None, short: str | None, lookback: int = 14, every: int = 30) -> np.ndarray | None:
    if signal not in bars or not any(s in symbols for s in (long, short) if s):
        return None
    column = {s: j for j, s in enumerate(symbols)}
    session = _session(bars[signal])
    if session.empty:
        return None
    day_open = session.groupby("day")["open"].transform("first")
    move = (session["close"] / day_open - 1).abs()
    table = pd.DataFrame({"day": session["day"], "minute": session["minute"], "move": move.to_numpy()})
    grid = table.pivot_table(index="day", columns="minute", values="move")
    sigma = grid.rolling(lookback, min_periods=lookback).mean().shift(1)  # previous days only
    prev_close = session.groupby("day")["close"].last().shift(1)
    typical = (session["high"] + session["low"] + session["close"]) / 3
    pv = (typical * session["volume"]).groupby(session["day"]).cumsum()
    vol = session["volume"].groupby(session["day"]).cumsum()
    vwap = (pv / vol.replace(0, np.nan)).fillna(session["close"])
    weights = np.zeros((len(index), len(symbols)))
    loc = index.get_indexer(session.index)
    position = 0
    last_day = None
    for k, (ts, bar) in enumerate(session.iterrows()):
        day, minute = bar["day"], int(bar["minute"])
        if day != last_day:
            position, last_day = 0, day
        if minute >= LAST_MINUTE:
            position = 0
        elif (minute + 5) % every == 0 and day in sigma.index and minute in sigma.columns:
            band = sigma.at[day, minute]
            base_open, prior = day_open.iloc[k], prev_close.get(day, np.nan)
            if np.isfinite(band):
                upper = max(base_open, prior if np.isfinite(prior) else base_open) * (1 + band)
                lower = min(base_open, prior if np.isfinite(prior) else base_open) * (1 - band)
                close, level = bar["close"], vwap.iloc[k]
                if position == 1 and close < max(upper, level):
                    position = 0
                elif position == -1 and close > min(lower, level):
                    position = 0
                if position == 0:
                    position = 1 if close > upper else -1 if close < lower else 0
        side = long if position == 1 else short if position == -1 else None
        if side in column and loc[k] >= 0:
            weights[loc[k], column[side]] = 1.0
    # hold between signal bars (crypto bars interleave the union index)
    frame = pd.DataFrame(weights, index=index)
    frame[~index.isin(session.index)] = np.nan
    return frame.ffill().fillna(0.0).to_numpy()


def last_half_hour(bars: dict[str, pd.DataFrame], index: pd.DatetimeIndex, symbols: list[str], signal: str,
                   long: str | None, short: str | None, k: float = 0.5, lookback: int = 20) -> np.ndarray | None:
    """Market intraday momentum (Gao, Han, Li & Zhou 2018; Baltussen et al. 2021): the move from the
    previous close to 15:30 predicts the last half hour. Trade it only when the move is larger than
    ``k`` times its recent standard deviation; hold 15:30 to 15:55."""
    if signal not in bars or not any(s in symbols for s in (long, short) if s):
        return None
    column = {s: j for j, s in enumerate(symbols)}
    session = _session(bars[signal])
    if session.empty:
        return None
    prev_close = session.groupby("day")["close"].last().shift(1)
    marks = session[session["minute"] == 355]  # the 15:25 bar, complete at 15:30
    move = pd.Series(marks["close"].to_numpy(), index=marks["day"].to_numpy()) / prev_close.reindex(marks["day"]).to_numpy() - 1
    threshold = k * move.rolling(lookback, min_periods=10).std().shift(1)
    weights = np.zeros((len(index), len(symbols)))
    final = session["day"].iloc[-1]
    for ts, bar in marks.iterrows():
        day = bar["day"]
        r, theta = move.get(day, np.nan), threshold.get(day, np.nan)
        if not (np.isfinite(r) and np.isfinite(theta)) or abs(r) <= theta:
            continue
        side = long if r > 0 else short
        if side not in column:
            continue
        start = index.get_loc(ts)
        later = session[(session["day"] == day) & (session["minute"] >= LAST_MINUTE)]
        end = index.get_loc(later.index[0]) if len(later) else (len(index) if day == final else start + 1)
        weights[start:end, column[side]] = 1.0
    return weights


def open_breakout(bars: dict[str, pd.DataFrame], index: pd.DatetimeIndex, symbols: list[str], signal: str,
                  long: str | None, short: str | None, k: float = 0.5) -> np.ndarray | None:
    """Volatility breakout from the open (Larry Williams; Crabel; Concretum 2026): go with a 5-minute
    close beyond open +/- k x the previous day's range that is also a new session extreme. Stop at
    the open, flat before the close, one trade per day."""
    if signal not in bars or not any(s in symbols for s in (long, short) if s):
        return None
    column = {s: j for j, s in enumerate(symbols)}
    session = _session(bars[signal])
    if session.empty:
        return None
    daily = session.groupby("day").agg(high=("high", "max"), low=("low", "min"))
    prior_range = (daily["high"] - daily["low"]).shift(1)
    weights = np.zeros((len(index), len(symbols)))
    loc = pd.Series(index.get_indexer(session.index), index=session.index)
    final = session["day"].iloc[-1]
    for day_key, day in session.groupby("day"):
        span = prior_range.get(day_key, np.nan)
        first = day[day["minute"] == 0]
        if first.empty or not np.isfinite(span) or span <= 0:
            continue
        day_open = float(first["open"].iloc[0])
        upper, lower = day_open + k * span, day_open - k * span
        high_so_far, low_so_far = day["high"].cummax().shift(1), day["low"].cummin().shift(1)
        side = start = end = None
        for ts, bar in day.iterrows():
            minute = bar["minute"]
            if side is None:
                if minute >= LAST_MINUTE - 30:  # no new trades in the last 40 minutes
                    break
                if bar["close"] > upper and bar["close"] >= high_so_far.get(ts, -np.inf) and long in column:
                    side, start = 1, loc[ts]
                elif bar["close"] < lower and bar["close"] <= low_so_far.get(ts, np.inf) and short in column:
                    side, start = -1, loc[ts]
                continue
            if minute >= LAST_MINUTE or (side == 1 and bar["close"] < day_open) or (side == -1 and bar["close"] > day_open):
                end = loc[ts]
                break
        if side is None:
            continue
        if end is None:
            end = _open_end(loc[day.index[-1]], index, day_key == final)
        weights[start:end, column[long if side == 1 else short]] = 1.0
    return weights
