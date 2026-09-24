"""Kronos price forecasts for the "model" strategy.

Kronos (https://github.com/shiyu-coder/Kronos, MIT) is a foundation model for
OHLCV candlesticks. ``KronosForecaster`` turns the last ``lookback`` completed
bars of a symbol into one number: the expected return from the last close to
the predicted close ``pred_len`` bars ahead.

``update_forecasts`` keeps a JSON-serialisable store of those numbers, keyed by
the start time of the last bar each forecast used, and only re-forecasts a
symbol once ``every_minutes`` of new bars have arrived. Inference is slow on a
CPU, so each call works through the stalest symbols first and stops once its
time budget is spent.

Nothing here imports torch until a model is actually needed, so the engine can
import this module on machines without the optional Kronos dependencies
(``requirements-kronos.txt``).
"""
from __future__ import annotations

import importlib
import logging
import math
import os
import time

import numpy as np
import pandas as pd

from ..config import KronosConfig

log = logging.getLogger(__name__)

MIN_BARS = 64
KEEP_DAYS = 10
PRICE_COLUMNS = ["open", "high", "low", "close", "volume"]
LOAD_RETRY_SECONDS = 600.0

# Monotonic clock used for the time budget (tests replace it).
_clock = time.monotonic


class KronosUnavailable(RuntimeError):
    """The Kronos model could not be loaded (missing deps or weights)."""


def kronos_available() -> bool:
    """True if the optional Kronos dependencies can be imported."""
    for name in ("torch", "einops", "huggingface_hub", "safetensors"):
        try:
            importlib.import_module(name)
        except Exception:  # ImportError, or a broken install raising something else
            return False
    return True


def _max_context(model_name: str) -> int:
    # Kronos-mini was trained with a 2048-bar context; small/base with 512.
    return 2048 if "mini" in model_name.lower() else 512


class KronosForecaster:
    """Expected-return forecasts from a Kronos model.

    The tokenizer and model are downloaded/loaded with ``from_pretrained`` on
    first use, unless a ready ``predictor`` (anything with Kronos's
    ``KronosPredictor.predict`` signature) is injected.
    """

    def __init__(self, cfg: KronosConfig, device: str | None = None, predictor=None):
        self.cfg = cfg
        self.device = device
        self._predictor = predictor
        self._load_failed_at: float | None = None
        self._load_error: Exception | None = None

    @property
    def predictor(self):
        if self._predictor is None:
            self._predictor = self._load()
        return self._predictor

    def _load(self):
        if self._load_failed_at is not None and _clock() - self._load_failed_at < LOAD_RETRY_SECONDS:
            raise KronosUnavailable(f"Kronos model unavailable: {self._load_error}")
        started = time.perf_counter()
        try:
            import torch

            from .model import Kronos, KronosPredictor, KronosTokenizer

            device = self.device or ("cuda:0" if torch.cuda.is_available() else "cpu")
            if device == "cpu":
                # Use the cores we have, but don't oversubscribe big hosts.
                torch.set_num_threads(max(1, min(os.cpu_count() or 1, 8)))
            tokenizer = KronosTokenizer.from_pretrained(self.cfg.tokenizer)
            model = Kronos.from_pretrained(self.cfg.model)
            tokenizer.eval()
            model.eval()
            predictor = KronosPredictor(model, tokenizer, device=device,
                                        max_context=_max_context(self.cfg.model))
        except Exception as error:
            self._load_failed_at = _clock()
            self._load_error = error
            raise KronosUnavailable(f"Could not load Kronos ({self.cfg.model}): {error}") from error
        self.device = device
        self._load_failed_at = self._load_error = None
        log.info("Loaded Kronos %s on %s in %.1fs", self.cfg.model, device, time.perf_counter() - started)
        return predictor

    def expected_return(self, bars: pd.DataFrame, bar_minutes: int = 5) -> float:
        """Predicted close ``pred_len`` bars ahead / last actual close - 1.

        ``bars`` holds completed bars indexed by UTC start time with
        open/high/low/close/volume columns.
        """
        cfg = self.cfg
        missing = [column for column in PRICE_COLUMNS if column not in bars.columns]
        if missing:
            raise ValueError(f"bars missing columns {missing}")
        has_amount = "amount" in bars.columns
        df = bars[PRICE_COLUMNS + (["amount"] if has_amount else [])].astype(float)
        df["volume"] = df["volume"].fillna(0.0)
        df = df.dropna(subset=["open", "high", "low", "close"])
        df = df[~df.index.duplicated(keep="last")].sort_index().tail(cfg.lookback)
        if len(df) < MIN_BARS:
            raise ValueError(f"Kronos needs at least {MIN_BARS} bars, got {len(df)}")
        if not has_amount or df["amount"].isna().any():
            df["amount"] = df["close"] * df["volume"]

        index = pd.DatetimeIndex(df.index)
        if index.tz is not None:
            index = index.tz_convert("UTC").tz_localize(None)
        step = pd.Timedelta(minutes=bar_minutes)
        x_timestamp = pd.Series(index)
        y_timestamp = pd.Series(pd.date_range(index[-1] + step, periods=cfg.pred_len, freq=step))

        prediction = self.predictor.predict(
            df=df.reset_index(drop=True),
            x_timestamp=x_timestamp,
            y_timestamp=y_timestamp,
            pred_len=cfg.pred_len,
            T=1.0,
            top_k=0,
            top_p=0.9,
            sample_count=cfg.sample_count,
            verbose=False,
        )
        last_close = float(df["close"].iloc[-1])
        predicted_close = float(prediction["close"].iloc[-1])
        result = predicted_close / last_close - 1.0
        if not math.isfinite(result):
            raise ValueError(f"non-finite forecast (last close {last_close}, predicted {predicted_close})")
        return result


# One lazily-loaded forecaster per (model, tokenizer), reused across calls when
# the engine doesn't pass its own.
_default_forecasters: dict[tuple[str, str], KronosForecaster] = {}


def _default_forecaster(cfg: KronosConfig) -> KronosForecaster:
    key = (cfg.model, cfg.tokenizer)
    forecaster = _default_forecasters.get(key)
    if forecaster is None:
        forecaster = _default_forecasters[key] = KronosForecaster(cfg)
    forecaster.cfg = cfg
    return forecaster


def _utc(value) -> pd.Timestamp:
    stamp = pd.Timestamp(value)
    return stamp.tz_localize("UTC") if stamp.tzinfo is None else stamp.tz_convert("UTC")


def _latest_key(entries: dict) -> pd.Timestamp | None:
    stamps = []
    for key in entries or {}:
        try:
            stamps.append(_utc(key))
        except (ValueError, TypeError):
            continue
    return max(stamps) if stamps else None


def _bar_minutes(index: pd.DatetimeIndex, default: int = 5) -> int:
    if len(index) < 3:
        return default
    step = pd.Series(index[-50:]).diff().dropna().median()
    minutes = int(round(step.total_seconds() / 60)) if pd.notna(step) else 0
    return minutes if minutes > 0 else default


def _trim(store: dict, cutoff: pd.Timestamp) -> None:
    for symbol in list(store):
        entries = store[symbol]
        if not isinstance(entries, dict):
            del store[symbol]
            continue
        for key in list(entries):
            try:
                stale = _utc(key) < cutoff
            except (ValueError, TypeError):
                stale = True
            if stale:
                del entries[key]
        if not entries:
            del store[symbol]


def update_forecasts(store: dict, bars_by_symbol: dict[str, pd.DataFrame], cfg, now: pd.Timestamp,
                     forecaster=None, open_symbols: set[str] | None = None,
                     time_budget_s: float = 240) -> dict:
    """Refresh stale Kronos forecasts in ``store`` and return it.

    ``store`` is ``{symbol: {"<ISO UTC start of last input bar>": expected_return}}``.
    Symbols are taken in ``bars_by_symbol`` order, filtered to ``open_symbols``
    when given, and capped at ``cfg.max_symbols``. A symbol is re-forecast when
    its latest bar (at or before ``now``) is at least ``cfg.every_minutes``
    newer than its latest stored forecast. Stalest symbols go first; work stops
    once ``time_budget_s`` has elapsed. Per-symbol errors are logged and
    skipped; if the model itself can't be loaded the call stops early.
    Entries older than ``KEEP_DAYS`` days before ``now`` are dropped.
    """
    cfg = getattr(cfg, "kronos", cfg)  # accept the full Config too
    now = _utc(now)
    started = _clock()

    symbols = [symbol for symbol in bars_by_symbol if open_symbols is None or symbol in open_symbols]
    symbols = symbols[: max(0, int(cfg.max_symbols))]

    due = []
    for position, symbol in enumerate(symbols):
        bars = bars_by_symbol[symbol]
        if bars is None or len(bars) == 0:
            continue
        index = pd.DatetimeIndex(bars.index)
        index = index.tz_localize("UTC") if index.tz is None else index.tz_convert("UTC")
        bars = bars.set_axis(index)
        if not index.is_monotonic_increasing:
            bars = bars.sort_index()
        bars = bars.loc[:now]  # never look past "now" (matters when replaying history)
        if len(bars) == 0:
            continue
        last_bar = bars.index[-1]
        latest = _latest_key(store.get(symbol))
        if latest is not None and last_bar - latest < pd.Timedelta(minutes=cfg.every_minutes):
            continue
        # Never-forecast symbols first, then oldest forecast; ties keep universe order.
        rank = (0, pd.Timestamp.min.tz_localize("UTC")) if latest is None else (1, latest)
        due.append((rank, position, symbol, bars, last_bar))
    due.sort(key=lambda item: (item[0], item[1]))

    done = 0
    for _, _, symbol, bars, last_bar in due:
        if _clock() - started >= time_budget_s:
            log.info("Kronos time budget (%.0fs) spent; %d/%d symbols left for next time",
                     time_budget_s, len(due) - done, len(due))
            break
        if forecaster is None:
            forecaster = _default_forecaster(cfg)
        try:
            value = float(forecaster.expected_return(bars, bar_minutes=_bar_minutes(bars.index)))
            if not math.isfinite(value):
                raise ValueError(f"non-finite forecast {value}")
        except KronosUnavailable as error:
            log.warning("Kronos unavailable, skipping forecasts: %s", error)
            break
        except Exception as error:
            log.warning("Kronos forecast failed for %s: %s", symbol, error)
        else:
            store.setdefault(symbol, {})[last_bar.isoformat()] = value
        done += 1

    _trim(store, now - pd.Timedelta(days=KEEP_DAYS))
    return store


def forecasts_as_series(store: dict) -> dict[str, pd.Series]:
    """``{symbol: float Series of expected returns indexed by UTC bar start}``."""
    result = {}
    for symbol, entries in store.items():
        if not isinstance(entries, dict):
            continue
        stamps, values = [], []
        for key, value in entries.items():
            try:
                stamp = _utc(key)
                number = float(value)
            except (ValueError, TypeError):
                continue
            stamps.append(stamp)
            values.append(number)
        series = pd.Series(values, index=pd.DatetimeIndex(stamps, tz="UTC") if stamps
                           else pd.DatetimeIndex([], tz="UTC"), dtype=float, name=symbol)
        series = series[~series.index.duplicated(keep="last")].sort_index()
        result[symbol] = series
    return result
