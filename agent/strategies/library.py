"""The strategy zoo: well-known intraday rule sets, each in a few lines.

All are long-only (a small cash account can't short; inverse ETFs such as
SQQQ in the universe give bearish exposure). Parameters are textbook defaults,
not fitted to recent data, so backtests are not tuned to the test period.
"""
from __future__ import annotations

import dataclasses

import pandas as pd

from ..indicators import Features, crossed_above, crossed_below
from .base import Strategy

EQUITIES = ("us_equity", "uk_equity")


def _false(f: Features) -> pd.Series:
    return pd.Series(False, index=f.index)


# ----------------------------------------------------------------- trend

def ema_cross(fast: int, slow: int):
    def fn(f: Features):
        a, b = f.ema(fast), f.ema(slow)
        return crossed_above(a, b), crossed_below(a, b)
    return fn


def triple_ema(f: Features):
    e1, e2, e3 = f.ema(8), f.ema(21), f.ema(55)
    aligned = (e1 > e2) & (e2 > e3)
    return aligned & ~aligned.shift(1, fill_value=False), e1 < e2


def macd_cross(f: Features):
    line, signal = f.macd()
    return crossed_above(line, signal), crossed_below(line, signal)


def macd_zero(f: Features):
    line, signal = f.macd()
    return crossed_above(line, 0.0) & (line > signal), crossed_below(line, signal)


def supertrend(f: Features):
    trend = f.supertrend(10, 3.0)
    return (trend > 0) & (trend.shift(1) < 0), trend < 0


def psar(f: Features):
    trend = f.psar()
    return (trend > 0) & (trend.shift(1) < 0) & (f.close > f.ema(50)), trend < 0


def adx_trend(f: Features):
    adx, plus_di, minus_di = f.adx(14)
    return crossed_above(plus_di, minus_di) & (adx > 20), crossed_below(plus_di, minus_di)


def ichimoku(f: Features):
    tenkan, kijun, top, _ = f.ichimoku()
    above = f.close > top
    return crossed_above(tenkan, kijun) & above, f.close < kijun


def heikin_ashi(f: Features):
    ho, hh, hl, hc = f.heikin_ashi()
    green = hc > ho
    strong = green & (hl >= ho)  # no lower wick
    streak = strong & strong.shift(1, fill_value=False)
    return streak & ~streak.shift(1, fill_value=False), ~green


def ma_pullback(f: Features):
    """Buy a dip to the 20 EMA inside an up-trend (EMA20 > EMA50 > EMA200)."""
    e20, e50, e200 = f.ema(20), f.ema(50), f.ema(200)
    trend = (e20 > e50) & (e50 > e200)
    touched = f.low <= e20
    return trend & touched & (f.close > e20) & (f.close > f.open), f.close < e50


# ----------------------------------------------------------------- momentum

def vwap_momentum(f: Features):
    """The original GPT rule: above session VWAP with positive 20-minute return."""
    vwap = f.vwap()
    up = (f.close > vwap) & (f.roc(4) > 0)
    return up & ~up.shift(1, fill_value=False), f.close < vwap


def roc_volume(f: Features):
    roc = f.roc(12)
    vol = f.volume_ratio(20)
    return (roc > 0.006) & (vol > 1.5) & (f.close > f.ema(20)), roc < 0


def rsi_momentum(f: Features):
    rsi = f.rsi(14)
    return crossed_above(rsi, 60) & (f.close > f.ema(50)), crossed_below(rsi, 45)


def obv_trend(f: Features):
    obv = f.obv()
    obv_ema = obv.ewm(span=20, adjust=False, min_periods=20).mean()
    cond = (obv > obv_ema) & (f.close > f.ema(20)) & (f.ema(20) > f.ema(50))
    return cond & ~cond.shift(1, fill_value=False), (obv < obv_ema) & (f.close < f.ema(20))


def gap_and_go(f: Features):
    """Stocks gapping up >1% that break the first 5-minute bar's high."""
    gap = f.session_open() / f.prev_session_close() - 1
    first_high = f.high.where(f.session["since_open"] < 5).groupby(f.session["session"]).transform("max")
    since = f.session["since_open"]
    entry = (gap > 0.01) & (since >= 5) & (since < 90) & crossed_above(f.close, first_high)
    return entry, f.close < f.vwap()


# ----------------------------------------------------------------- breakout

def donchian(entry_n: int, exit_n: int):
    def fn(f: Features):
        return f.close > f.highest(entry_n), f.close < f.lowest(exit_n)
    return fn


def opening_range_breakout(minutes: int):
    def fn(f: Features):
        high, low, complete = f.opening_range(minutes)
        entry = complete & crossed_above(f.close, high) & (f.session["since_open"] < 240)
        return entry, f.close < (high + low) / 2
    return fn


# ----------------------------------------------------------------- candlesticks

def _candles(f: Features):
    body = f.close - f.open
    span = (f.high - f.low).replace(0, float("nan"))
    lower = pd.concat([f.open, f.close], axis=1).min(axis=1) - f.low
    upper = f.high - pd.concat([f.open, f.close], axis=1).max(axis=1)
    return body, span, lower, upper


def bullish_candles(f: Features) -> pd.Series:
    """Bullish engulfing, hammer or morning star on the latest bar."""
    body, span, lower, upper = _candles(f)
    prev = body.shift(1)
    engulfing = (prev < 0) & (body > 0) & (f.open <= f.close.shift(1)) & (f.close >= f.open.shift(1)) & (body > -prev)
    hammer = (lower >= 2 * body.abs()) & (upper <= 0.3 * span) & ((f.close - f.low) / span >= 0.6)
    big = body.abs() > 0.5 * f.atr(14)
    star = ((body.shift(2) < 0) & big.shift(2, fill_value=False) & (body.shift(1).abs() < 0.3 * body.shift(2).abs())
            & (body > 0) & (f.close > f.open.shift(2) + body.shift(2) / 2))
    return engulfing | hammer | star


def candlestick_reversal(f: Features):
    """A bullish reversal candle after a pullback (below EMA20, RSI under 45)."""
    pullback = (f.close.shift(1) < f.ema(20).shift(1)) & (f.rsi(14).shift(1) < 45)
    body, _, _, _ = _candles(f)
    bearish_engulfing = (body.shift(1) > 0) & (body < 0) & (f.open >= f.close.shift(1)) & (f.close <= f.open.shift(1))
    return bullish_candles(f) & pullback, bearish_engulfing | (f.close > f.bollinger(20, 2.0)[2])


def three_white_soldiers(f: Features):
    body, span, _, upper = _candles(f)
    green = (body > 0) & (upper <= 0.3 * span) & (body > 0.3 * f.atr(14))
    rising = (f.close > f.close.shift(1)) & (f.open > f.open.shift(1)) & (f.open <= f.close.shift(1))
    soldiers = green & green.shift(1, fill_value=False) & green.shift(2, fill_value=False) & rising & rising.shift(1, fill_value=False)
    return soldiers, f.close < f.ema(9)


def bollinger_breakout(f: Features):
    lower, mid, upper = f.bollinger(20, 2.0)
    return crossed_above(f.close, upper), f.close < mid


def keltner_breakout(f: Features):
    lower, mid, upper = f.keltner(20, 2.0)
    return crossed_above(f.close, upper), f.close < mid


def squeeze_breakout(f: Features):
    """TTM-style squeeze: Bollinger bands inside Keltner, then release upward."""
    bl, bm, bu = f.bollinger(20, 2.0)
    kl, km, ku = f.keltner(20, 1.5)
    squeezed = (bu < ku) & (bl > kl)
    was_squeezed = squeezed.shift(1, fill_value=False).rolling(6, min_periods=1).max().astype(bool)
    return was_squeezed & ~squeezed & (f.close > bu) & (f.roc(3) > 0), f.close < bm


def volume_breakout(f: Features):
    entry = (f.volume_ratio(20) > 3.0) & (f.close > f.open) & (f.close > f.highest(20))
    return entry, f.close < f.ema(9)


# ----------------------------------------------------------------- mean reversion

def rsi_reversion(f: Features):
    rsi = f.rsi(14)
    return crossed_above(rsi, 30), rsi > 55


def connors_rsi2(f: Features):
    rsi2 = f.rsi(2)
    return (rsi2 < 10) & (f.close > f.sma(200)), f.close > f.sma(5)


def bollinger_reversion(f: Features):
    lower, mid, upper = f.bollinger(20, 2.0)
    return crossed_above(f.close, lower), f.close >= mid


def zscore_reversion(f: Features):
    z = f.zscore(50)
    return crossed_above(z, -2.0), z > 0


def vwap_reversion(f: Features):
    vwap, sd = f.vwap(), f.vwap_std()
    stretched = f.close < vwap - 2 * sd
    return stretched & (f.close > f.open), f.close >= vwap


def stochastic_reversion(f: Features):
    k, d = f.stochastic(14, 3)
    return crossed_above(k, d) & (k < 25), k > 80


def williams_reversion(f: Features):
    wr = f.williams_r(14)
    return crossed_above(wr, -80), wr > -20


def cci_reversion(f: Features):
    cci = f.cci(20)
    return crossed_above(cci, -100), cci > 100


def mfi_reversion(f: Features):
    mfi = f.mfi(14)
    return crossed_above(mfi, 20), mfi > 70


# ----------------------------------------------------------------- timeframes

def on_timeframe(fn, minutes: int):
    """Run a rule on ``minutes``-long bars; events land on the completing 5m bar."""
    def wrapped(f: Features):
        higher, anchor = f.resampled(minutes)
        if len(higher.index) < 2:
            return _false(f), _false(f)
        entry, exit_ = fn(higher)
        return f.on_base(entry, anchor), f.on_base(exit_, anchor)
    return wrapped


# ----------------------------------------------------------------- benchmarks

def always_long(f: Features):
    return pd.Series(True, index=f.index), _false(f)


def model_signal(key: str):
    """Signals supplied externally (e.g. Kronos forecasts) via Features.extra."""
    def fn(f: Features):
        forecast = f.extra.get(key)
        if forecast is None or forecast.empty:
            return _false(f), _false(f)
        aligned = forecast.reindex(f.index).ffill(limit=6)
        threshold = f.extra.get(f"{key}_threshold", 0.004)
        return aligned > threshold, aligned < 0
    return fn


S = Strategy
INTRADAY: tuple[Strategy, ...] = (
    # trend following
    S("EMA 9/21 cross", "ema_cross", "trend", "Fast EMA crosses the slow EMA", ema_cross(9, 21), params={"fast": 9, "slow": 21}),
    S("EMA 20/50 cross", "ema_cross", "trend", "Slower EMA crossover", ema_cross(20, 50), params={"fast": 20, "slow": 50}),
    S("Triple EMA stack", "triple_ema", "trend", "8>21>55 EMAs line up", triple_ema),
    S("MACD cross", "macd", "trend", "MACD crosses its signal line", macd_cross),
    S("MACD zero-line", "macd", "trend", "MACD crosses above zero", macd_zero),
    S("Supertrend", "supertrend", "trend", "Supertrend(10,3) flips up", supertrend, stop_atr=None),
    S("Parabolic SAR", "psar", "trend", "SAR flips below price above EMA50", psar),
    S("ADX DI cross", "adx", "trend", "+DI crosses -DI with ADX>20", adx_trend),
    S("Ichimoku", "ichimoku", "trend", "Tenkan/Kijun cross above the cloud", ichimoku),
    S("Heikin-Ashi", "heikin_ashi", "trend", "Two strong green HA candles", heikin_ashi),
    S("Trend pullback", "pullback", "trend", "Dip to EMA20 inside an EMA20>50>200 trend", ma_pullback, take_atr=4.0),
    # momentum
    S("VWAP momentum", "vwap_momentum", "momentum", "Above session VWAP with positive 20-min return (original GPT rule)", vwap_momentum),
    S("ROC + volume", "roc_volume", "momentum", "1-hour return >0.6% on 1.5x volume", roc_volume, trail_atr=2.5),
    S("RSI momentum", "rsi_momentum", "momentum", "RSI crosses 60 in an up-trend", rsi_momentum),
    S("OBV trend", "obv", "momentum", "On-balance volume confirms the trend", obv_trend),
    S("Gap and go", "gap_and_go", "momentum", "Gap up >1% breaks the first-bar high", gap_and_go, trail_atr=2.0, kinds=EQUITIES),
    # breakout
    S("Donchian 20/10", "donchian", "breakout", "Turtle breakout of a 20-bar high", donchian(20, 10), params={"entry": 20, "exit": 10}),
    S("Donchian 55/20", "donchian", "breakout", "Slow turtle breakout", donchian(55, 20), params={"entry": 55, "exit": 20}),
    S("Opening range 15m", "orb", "breakout", "Break of the first 15 minutes' high", opening_range_breakout(15), kinds=EQUITIES),
    S("Opening range 30m", "orb", "breakout", "Break of the first 30 minutes' high", opening_range_breakout(30), kinds=EQUITIES),
    S("Bollinger breakout", "bb_breakout", "breakout", "Close above the upper Bollinger band", bollinger_breakout, trail_atr=2.0),
    S("Keltner breakout", "keltner", "breakout", "Close above the upper Keltner channel", keltner_breakout, trail_atr=2.0),
    S("Squeeze breakout", "squeeze", "breakout", "Volatility squeeze releases upward", squeeze_breakout, trail_atr=2.0),
    S("Volume breakout", "volume_breakout", "breakout", "3x volume bar breaks a 20-bar high", volume_breakout, max_bars=24),
    # candlestick patterns
    S("Candlestick reversal", "candles", "reversion", "Bullish engulfing, hammer or morning star after a pullback", candlestick_reversal,
      stop_atr=1.5, take_atr=3.0, max_bars=24),
    S("Three white soldiers", "candles", "momentum", "Three strong rising green candles", three_white_soldiers, stop_atr=1.5),
    # mean reversion
    S("RSI(14) reversion", "rsi_reversion", "reversion", "RSI climbs back above 30", rsi_reversion, take_atr=3.0),
    S("Connors RSI(2)", "connors_rsi2", "reversion", "RSI(2)<10 above the 200 SMA", connors_rsi2, max_bars=36),
    S("Bollinger reversion", "bb_reversion", "reversion", "Close back inside the lower band", bollinger_reversion, take_atr=3.0),
    S("Z-score reversion", "zscore", "reversion", "50-bar z-score recovers from -2", zscore_reversion),
    S("VWAP reversion", "vwap_reversion", "reversion", "Bounce from 2 sigma below VWAP", vwap_reversion),
    S("Stochastic reversion", "stoch", "reversion", "%K crosses %D below 25", stochastic_reversion),
    S("Williams %R", "williams", "reversion", "%R climbs out of oversold", williams_reversion),
    S("CCI reversion", "cci", "reversion", "CCI climbs back above -100", cci_reversion),
    S("MFI reversion", "mfi", "reversion", "Money-flow index leaves oversold", mfi_reversion),
)

# Hourly "swing" versions: far fewer trades, so costs bite less, and stock
# positions may be held overnight (which also avoids US day-trade limits).
# Opening-range and gap rules only make sense intraday.
SWING: tuple[Strategy, ...] = tuple(
    dataclasses.replace(s, name=f"{s.name} · 1h", fn=on_timeframe(s.fn, 60), timeframe=60, intraday=False,
                        description=s.description + " (hourly bars, can hold overnight)")
    for s in INTRADAY if s.family not in ("orb", "gap_and_go"))

STRATEGIES: tuple[Strategy, ...] = INTRADAY + SWING

KRONOS_STRATEGY = S("Kronos forecast", "kronos", "model",
                    "Kronos foundation-model forecast of the next hour's return",
                    model_signal("kronos"), stop_atr=2.0, max_bars=24)

def _hold(name: str, symbol: str, description: str, style: str = "benchmark") -> Strategy:
    return S(name, "benchmark" if style == "benchmark" else "copy_fund", style, description, always_long,
             stop_atr=None, intraday=False, benchmark=True, params={"symbols": [symbol]})


BENCHMARKS: tuple[Strategy, ...] = (
    _hold("Hold SPY", "SPY", "Buy and hold the S&P 500 (not a day trade)"),
    _hold("Hold BTC", "BTC-USD", "Buy and hold Bitcoin"),
    # Copy-trading funds: professionals already copy these people's disclosed trades.
    _hold("Copy: Congress Democrats (NANC)", "NANC", "ETF copying stock trades disclosed by Democratic members of Congress (incl. Pelosi)", "copy"),
    _hold("Copy: Hedge-fund gurus (GURU)", "GURU", "ETF holding top picks from hedge funds' 13F filings", "copy"),
    _hold("Copy: Cathie Wood (ARKK)", "ARKK", "Cathie Wood's flagship ARK Innovation fund", "copy"),
    _hold("Copy: Warren Buffett (BRK-B)", "BRK-B", "Berkshire Hathaway, Warren Buffett's company", "copy"),
)


def all_strategies(kronos: bool = False, disabled: tuple[str, ...] = ()) -> list[Strategy]:
    chosen = list(STRATEGIES) + ([KRONOS_STRATEGY] if kronos else []) + list(BENCHMARKS)
    return [strategy for strategy in chosen if strategy.name not in disabled]
