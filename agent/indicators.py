"""Causal technical indicators for one symbol's bars.

Every value at bar t uses only bars <= t. ``Features`` memoises indicators so
many strategies can share them cheaply.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .sessions import session_frame


def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False, min_periods=span).mean()


def wilder(series: pd.Series, period: int) -> pd.Series:
    return series.ewm(alpha=1.0 / period, adjust=False, min_periods=period).mean()


def crossed_above(a: pd.Series, b) -> pd.Series:
    b_prev = b.shift(1) if isinstance(b, pd.Series) else b
    return (a > b) & (a.shift(1) <= b_prev)


def crossed_below(a: pd.Series, b) -> pd.Series:
    b_prev = b.shift(1) if isinstance(b, pd.Series) else b
    return (a < b) & (a.shift(1) >= b_prev)


class Features:
    def __init__(self, bars: pd.DataFrame, kind: str, bar_minutes: int = 5, extra: dict | None = None):
        self.bars = bars
        self.kind = kind
        self.open = bars["open"]
        self.high = bars["high"]
        self.low = bars["low"]
        self.close = bars["close"]
        self.volume = bars["volume"]
        self.index = bars.index
        self.bar_minutes = bar_minutes
        self.session = session_frame(bars.index, kind, bar_minutes)
        self.extra = extra or {}

    def _memo(self, key, compute):
        cache = self.__dict__.setdefault("_store", {})
        if key not in cache:
            cache[key] = compute()
        return cache[key]

    # ------------------------------------------------------------ basics
    def sma(self, n: int) -> pd.Series:
        return self._memo(("sma", n), lambda: self.close.rolling(n, min_periods=n).mean())

    def ema(self, n: int) -> pd.Series:
        return self._memo(("ema", n), lambda: ema(self.close, n))

    def std(self, n: int) -> pd.Series:
        return self._memo(("std", n), lambda: self.close.rolling(n, min_periods=n).std(ddof=0))

    def roc(self, n: int) -> pd.Series:
        return self._memo(("roc", n), lambda: self.close / self.close.shift(n) - 1.0)

    def true_range(self) -> pd.Series:
        def compute():
            prev = self.close.shift(1)
            return pd.concat([self.high - self.low, (self.high - prev).abs(), (self.low - prev).abs()], axis=1).max(axis=1)
        return self._memo("tr", compute)

    def atr(self, n: int = 14) -> pd.Series:
        return self._memo(("atr", n), lambda: wilder(self.true_range(), n))

    def highest(self, n: int, shift: int = 1) -> pd.Series:
        """Highest high of the ``n`` bars before the current one."""
        return self._memo(("hh", n, shift), lambda: self.high.rolling(n, min_periods=n).max().shift(shift))

    def lowest(self, n: int, shift: int = 1) -> pd.Series:
        return self._memo(("ll", n, shift), lambda: self.low.rolling(n, min_periods=n).min().shift(shift))

    def zscore(self, n: int) -> pd.Series:
        return self._memo(("z", n), lambda: (self.close - self.sma(n)) / self.std(n).replace(0, np.nan))

    def volume_ratio(self, n: int = 20) -> pd.Series:
        return self._memo(("vr", n), lambda: self.volume / self.volume.rolling(n, min_periods=n).mean().shift(1).replace(0, np.nan))

    # ------------------------------------------------------------ oscillators
    def rsi(self, n: int = 14) -> pd.Series:
        def compute():
            delta = self.close.diff()
            gain = wilder(delta.clip(lower=0), n)
            loss = wilder(-delta.clip(upper=0), n)
            rs = gain / loss.replace(0, np.nan)
            return (100 - 100 / (1 + rs)).fillna(100.0).where(gain.notna())
        return self._memo(("rsi", n), compute)

    def macd(self, fast=12, slow=26, signal=9) -> tuple[pd.Series, pd.Series]:
        def compute():
            line = ema(self.close, fast) - ema(self.close, slow)
            return line, ema(line, signal)
        return self._memo(("macd", fast, slow, signal), compute)

    def bollinger(self, n=20, k=2.0) -> tuple[pd.Series, pd.Series, pd.Series]:
        def compute():
            mid, sd = self.sma(n), self.std(n)
            return mid - k * sd, mid, mid + k * sd
        return self._memo(("bb", n, k), compute)

    def keltner(self, n=20, k=2.0) -> tuple[pd.Series, pd.Series, pd.Series]:
        def compute():
            mid, band = self.ema(n), self.atr(n) * k
            return mid - band, mid, mid + band
        return self._memo(("kc", n, k), compute)

    def stochastic(self, n=14, smooth=3) -> tuple[pd.Series, pd.Series]:
        def compute():
            low = self.low.rolling(n, min_periods=n).min()
            high = self.high.rolling(n, min_periods=n).max()
            k = 100 * (self.close - low) / (high - low).replace(0, np.nan)
            return k, k.rolling(smooth, min_periods=smooth).mean()
        return self._memo(("stoch", n, smooth), compute)

    def williams_r(self, n=14) -> pd.Series:
        def compute():
            high = self.high.rolling(n, min_periods=n).max()
            low = self.low.rolling(n, min_periods=n).min()
            return -100 * (high - self.close) / (high - low).replace(0, np.nan)
        return self._memo(("wr", n), compute)

    def cci(self, n=20) -> pd.Series:
        def compute():
            tp = (self.high + self.low + self.close) / 3
            mean = tp.rolling(n, min_periods=n).mean()
            values = tp.to_numpy()
            mad = np.full(len(values), np.nan)
            if len(values) >= n:
                windows = np.lib.stride_tricks.sliding_window_view(values, n)
                mad[n - 1:] = np.abs(windows - windows.mean(axis=1, keepdims=True)).mean(axis=1)
            mad = pd.Series(mad, index=self.index)
            return (tp - mean) / (0.015 * mad.replace(0, np.nan))
        return self._memo(("cci", n), compute)

    def mfi(self, n=14) -> pd.Series:
        def compute():
            tp = (self.high + self.low + self.close) / 3
            flow = tp * self.volume
            up = flow.where(tp > tp.shift(1), 0.0).rolling(n, min_periods=n).sum()
            down = flow.where(tp < tp.shift(1), 0.0).rolling(n, min_periods=n).sum()
            return 100 - 100 / (1 + up / down.replace(0, np.nan))
        return self._memo(("mfi", n), compute)

    def adx(self, n=14) -> tuple[pd.Series, pd.Series, pd.Series]:
        def compute():
            up = self.high.diff()
            down = -self.low.diff()
            plus_dm = up.where((up > down) & (up > 0), 0.0)
            minus_dm = down.where((down > up) & (down > 0), 0.0)
            atr = wilder(self.true_range(), n)
            plus_di = 100 * wilder(plus_dm, n) / atr.replace(0, np.nan)
            minus_di = 100 * wilder(minus_dm, n) / atr.replace(0, np.nan)
            dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
            return wilder(dx, n), plus_di, minus_di
        return self._memo(("adx", n), compute)

    def obv(self) -> pd.Series:
        return self._memo("obv", lambda: (np.sign(self.close.diff()).fillna(0) * self.volume).cumsum())

    # ------------------------------------------------------------ session-aware
    def vwap(self) -> pd.Series:
        """Session VWAP (UTC day for crypto)."""
        def compute():
            tp = (self.high + self.low + self.close) / 3
            groups = self.session["session"]
            pv = (tp * self.volume).groupby(groups).cumsum()
            vol = self.volume.groupby(groups).cumsum()
            vwap = pv / vol.replace(0, np.nan)
            return vwap.fillna(tp.groupby(groups).transform(lambda s: s.expanding().mean()))
        return self._memo("vwap", compute)

    def vwap_std(self) -> pd.Series:
        def compute():
            groups = self.session["session"]
            diff = self.close - self.vwap()
            return diff.groupby(groups).transform(lambda s: s.expanding(min_periods=6).std(ddof=0))
        return self._memo("vwap_std", compute)

    def opening_range(self, minutes=30) -> tuple[pd.Series, pd.Series, pd.Series]:
        """(high, low, complete) of the first ``minutes`` of each session."""
        def compute():
            groups = self.session["session"]
            since = self.session["since_open"]
            in_range = since < minutes
            high = self.high.where(in_range).groupby(groups).cummax()
            low = self.low.where(in_range).groupby(groups).cummin()
            high = high.groupby(groups).ffill()
            low = low.groupby(groups).ffill()
            # the range must be fully formed and have started at the open
            first_since = since.groupby(groups).transform("min")
            complete = (since >= minutes) & (first_since <= 0)
            return high, low, complete
        return self._memo(("orb", minutes), compute)

    def session_open(self) -> pd.Series:
        return self._memo("sess_open", lambda: self.open.groupby(self.session["session"]).transform("first"))

    def prev_session_close(self) -> pd.Series:
        def compute():
            groups = self.session["session"]
            last = self.close.groupby(groups).last()
            prev = last.shift(1)
            return pd.Series(groups.map(prev).to_numpy(), index=self.index)
        return self._memo("prev_close", compute)

    # ------------------------------------------------------------ path-dependent
    def supertrend(self, n=10, mult=3.0) -> pd.Series:
        """+1 in an up-trend, -1 in a down-trend."""
        def compute():
            atr_arr = self.atr(n).to_numpy()
            hl2 = ((self.high + self.low) / 2).to_numpy()
            upper_basic = (hl2 + mult * atr_arr).tolist()
            lower_basic = (hl2 - mult * atr_arr).tolist()
            close = self.close.to_numpy().tolist()
            atr = atr_arr.tolist()
            size = len(close)
            nan = float("nan")
            upper, lower = [nan] * size, [nan] * size
            direction = [0.0] * size
            for i in range(size):
                if atr[i] != atr[i]:
                    continue
                if i == 0 or upper[i - 1] != upper[i - 1]:
                    upper[i], lower[i], direction[i] = upper_basic[i], lower_basic[i], 1
                    continue
                upper[i] = upper_basic[i] if (upper_basic[i] < upper[i - 1] or close[i - 1] > upper[i - 1]) else upper[i - 1]
                lower[i] = lower_basic[i] if (lower_basic[i] > lower[i - 1] or close[i - 1] < lower[i - 1]) else lower[i - 1]
                if direction[i - 1] <= 0:
                    direction[i] = 1 if close[i] > upper[i] else -1
                else:
                    direction[i] = -1 if close[i] < lower[i] else 1
            return pd.Series(direction, index=self.index)
        return self._memo(("st", n, mult), compute)

    def psar(self, step=0.02, max_step=0.2) -> pd.Series:
        """+1 when parabolic SAR is below price (up-trend), else -1."""
        def compute():
            high, low = self.high.to_numpy().tolist(), self.low.to_numpy().tolist()
            size = len(high)
            direction = [0.0] * size
            if size < 3:
                return pd.Series(direction, index=self.index)
            up, af, ep, sar = True, step, high[0], low[0]
            for i in range(1, size):
                sar = sar + af * (ep - sar)
                if up:
                    sar = min(sar, low[i - 1], low[i - 2] if i > 1 else low[i - 1])
                    if low[i] < sar:
                        up, sar, ep, af = False, ep, low[i], step
                    elif high[i] > ep:
                        ep, af = high[i], min(af + step, max_step)
                else:
                    sar = max(sar, high[i - 1], high[i - 2] if i > 1 else high[i - 1])
                    if high[i] > sar:
                        up, sar, ep, af = True, ep, high[i], step
                    elif low[i] < ep:
                        ep, af = low[i], min(af + step, max_step)
                direction[i] = 1 if up else -1
            return pd.Series(direction, index=self.index)
        return self._memo(("psar", step, max_step), compute)

    def heikin_ashi(self) -> tuple[pd.Series, pd.Series, pd.Series, pd.Series]:
        def compute():
            ha_close = ((self.open + self.high + self.low + self.close) / 4).to_numpy().tolist()
            size = len(ha_close)
            ha_open = [0.0] * size
            if size:
                ha_open[0] = (float(self.open.iloc[0]) + float(self.close.iloc[0])) / 2
            for i in range(1, size):
                ha_open[i] = (ha_open[i - 1] + ha_close[i - 1]) / 2
            ho = pd.Series(ha_open, index=self.index)
            hc = pd.Series(ha_close, index=self.index)
            hh = pd.concat([self.high, ho, hc], axis=1).max(axis=1)
            hl = pd.concat([self.low, ho, hc], axis=1).min(axis=1)
            return ho, hh, hl, hc
        return self._memo("ha", compute)

    def ichimoku(self, conv=9, base=26, span_b=52) -> tuple[pd.Series, pd.Series, pd.Series, pd.Series]:
        """(tenkan, kijun, cloud_top, cloud_bottom) with the cloud shifted forward (causal)."""
        def compute():
            def mid(n):
                return (self.high.rolling(n, min_periods=n).max() + self.low.rolling(n, min_periods=n).min()) / 2
            tenkan, kijun = mid(conv), mid(base)
            span_a = ((tenkan + kijun) / 2).shift(base)
            span_b_line = mid(span_b).shift(base)
            return tenkan, kijun, pd.concat([span_a, span_b_line], axis=1).max(axis=1), pd.concat([span_a, span_b_line], axis=1).min(axis=1)
        return self._memo(("ichi", conv, base, span_b), compute)
