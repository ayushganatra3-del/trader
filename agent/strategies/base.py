from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import pandas as pd

from ..indicators import Features

SignalFn = Callable[[Features], "tuple[pd.Series, pd.Series]"]


@dataclass(frozen=True)
class Strategy:
    """A long-only rule set: ``fn`` returns (entry, exit) boolean series.

    Signals are evaluated on a bar's close and executed on the next bar.
    Rules with ``timeframe`` > 5 see resampled bars; their signals land on the
    5-minute bar that completes each higher bar. Protective exits (ATR stop,
    take-profit, trailing stop, time stop and the end-of-day flatten for
    stocks) are applied on top by the position engine.
    """

    name: str
    family: str
    style: str  # "trend" | "reversion" | "breakout" | "momentum" | "model" | "benchmark"
    description: str
    fn: SignalFn
    stop_atr: float | None = 2.0
    take_atr: float | None = None
    trail_atr: float | None = None
    max_bars: int | None = None  # in bars of this strategy's own timeframe
    intraday: bool = True  # flatten stocks before the close (day-trading)
    timeframe: int = 5  # minutes per bar the rules (and ATR stops) run on
    kinds: tuple[str, ...] = ("us_equity", "uk_equity", "crypto")
    benchmark: bool = False  # excluded from meta selection
    params: dict = field(default_factory=dict)
