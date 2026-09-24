"""Exchange session calendars (regular hours only, weekends closed).

Holidays are not modelled: on a holiday the data source simply returns no
bars, so nothing trades.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .config import SESSIONS


def _minutes(hhmm: str) -> int:
    hours, minutes = hhmm.split(":")
    return int(hours) * 60 + int(minutes)


def session_mask(index: pd.DatetimeIndex, kind: str) -> np.ndarray:
    """True for bars that start inside the regular session."""
    spec = SESSIONS[kind]
    if spec is None:
        return np.ones(len(index), dtype=bool)
    tz, open_, close = spec
    local = index.tz_convert(tz)
    minute = local.hour * 60 + local.minute
    return np.asarray((local.dayofweek < 5) & (minute >= _minutes(open_)) & (minute < _minutes(close)))


def session_frame(index: pd.DatetimeIndex, kind: str, bar_minutes: int = 5) -> pd.DataFrame:
    """Per-bar session info: session id, minutes since open, minutes to close.

    ``minutes_to_close`` is measured from the *end* of the bar. For crypto the
    session is the UTC day and the close is never reached (inf).
    """
    spec = SESSIONS[kind]
    if spec is None:
        day = index.tz_convert("UTC").normalize()
        since = (index - day).total_seconds() / 60.0
        return pd.DataFrame({"session": day.as_unit("ns").asi8, "since_open": np.asarray(since),
                             "to_close": np.full(len(index), np.inf)}, index=index)
    tz, open_, close = spec
    local = index.tz_convert(tz)
    minute = local.hour * 60 + local.minute
    since = minute - _minutes(open_)
    to_close = _minutes(close) - (minute + bar_minutes)
    return pd.DataFrame({"session": local.normalize().as_unit("ns").asi8, "since_open": np.asarray(since, dtype=float),
                         "to_close": np.asarray(to_close, dtype=float)}, index=index)


def is_open(kind: str, now: pd.Timestamp) -> bool:
    return bool(session_mask(pd.DatetimeIndex([now]), kind)[0])
