import numpy as np
import pandas as pd
import pytest

from agent.config import Config
from agent.daily import (BURST, HAMMER, SCORE, TIMING, DailyData, completed, daily_books, market_regime,
                         momentum_burst, schedule, top_scores)
from agent.data import synthetic_bars
from agent.research import run_research
from agent.strategies import all_strategies

DAYS = pd.bdate_range("2025-01-01", periods=300)


def frame(close, volume=None, days=DAYS):
    close = np.asarray(close, float)
    volume = np.full(len(close), 1e6) if volume is None else np.asarray(volume, float)
    return pd.DataFrame({"open": close, "high": close * 1.005, "low": close * 0.995, "close": close,
                         "volume": volume}, index=days[:len(close)])


def walk(seed, n=300):
    rng = np.random.default_rng(seed)
    close = 100 * np.exp(np.cumsum(rng.normal(0.0005, 0.02, n)))
    open_ = close * np.exp(rng.normal(0, 0.007, n))
    return pd.DataFrame({"open": open_, "high": np.maximum(open_, close) * 1.01, "low": np.minimum(open_, close) * 0.99,
                         "close": close, "volume": rng.lognormal(15, 0.4, n)}, index=DAYS[:n])


def test_todays_bar_is_dropped_until_the_close():
    bars = frame([100, 101, 102], days=pd.DatetimeIndex(["2026-09-23", "2026-09-24", "2026-09-25"]))
    assert len(completed(bars, pd.Timestamp("2026-09-25T15:00Z"))) == 2  # 11:00 New York
    assert len(completed(bars, pd.Timestamp("2026-09-25T20:15Z"))) == 3  # 16:15 New York


def test_distribution_days_cut_exposure_and_follow_through_restores_it():
    close = list(np.linspace(100, 120, 80))
    volume = [1e6] * 80
    for _ in range(3):  # three distribution days: down 0.5% on higher volume
        close += [close[-1] * 0.995, close[-1] * 0.995 * 1.001]
        volume += [2e6, 1e6]
    regime = market_regime(frame(close, volume))
    assert regime["distribution_days"].iloc[-1] == 3 and regime["exposure"].iloc[-1] == 0.75
    # a 15% fall is a correction: out of the market
    close += list(close[-1] * np.linspace(0.98, 0.85, 8))
    volume += [1e6] * 8
    regime = market_regime(frame(close, volume))
    assert regime["state"].iloc[-1] == "correction" and regime["exposure"].iloc[-1] == 0.0
    # rally attempt: day 1-4 small gains, then +2% on higher volume on day 5 = follow-through
    close += [close[-1] * 1.003 ** k for k in range(1, 5)]
    volume += [1e6] * 4
    close.append(close[-1] * 1.02)
    volume.append(3e6)
    regime = market_regime(frame(close, volume))
    assert regime["follow_through"].iloc[-1] and regime["state"].iloc[-1] == "uptrend"
    assert regime["exposure"].iloc[-1] == 1.0
    gated = market_regime(frame(close, volume), vxn=pd.Series(40.0, index=DAYS[:len(close)]))
    assert gated["exposure"].iloc[-1] == 0.0 and gated["vxn_gate"].iloc[-1]


def test_momentum_burst_holds_then_exits_on_trigger_low():
    close = [100.0] * 30 + [105.0, 106, 107, 108, 109, 110]
    volume = [1e6] * 30 + [3e6] + [1e6] * 5
    bars = frame(close, volume)
    bars.loc[bars.index[30], "low"] = 100.5  # closes near the high of the burst day
    held = momentum_burst(bars, days=4)
    assert not held.iloc[29] and held.iloc[30:34].all() and not held.iloc[34]
    close[32] = 99.0  # breaks the trigger-day low: out early
    held = momentum_burst(frame(close, volume).assign(low=bars["low"]), days=4)
    assert held.iloc[30:32].all() and not held.iloc[32]


def test_top_scores_keeps_holdings_until_they_fade():
    scores = pd.DataFrame({"A": [7, 6.5, 5.5, 4.5], "B": [6.5, 7, 7, 7], "C": [5, 8, 8, 8]})
    held = top_scores(scores, top_n=2, minimum=6)
    assert held.iloc[0].to_dict() == {"A": 1, "B": 1, "C": 0}
    assert held.iloc[2].to_dict() == {"A": 1, "B": 1, "C": 0}  # A still within a point of the minimum
    assert held.iloc[3].to_dict() == {"A": 0, "B": 1, "C": 1}


def test_schedule_takes_effect_at_the_next_open():
    weights = pd.DataFrame({"QQQ": [0.0, 1.0, 1.0, 0.5]}, index=pd.DatetimeIndex(
        ["2026-09-23", "2026-09-24", "2026-09-25", "2026-09-28"]))
    entries = schedule(weights)
    assert [e[0] for e in entries] == ["2026-09-24T13:30:00+00:00", "2026-09-25T13:30:00+00:00",
                                       "2026-09-29T13:30:00+00:00"]  # Friday's signal waits for Monday
    assert entries[1][1] == {"QQQ": 1.0} and entries[2][1] == {"QQQ": 0.5}


def test_daily_books_build_and_trade_without_look_ahead():
    config = Config()
    daily = {a.symbol: walk(i) for i, a in enumerate(config.universe) if a.kind == "us_equity"}
    daily["^VXN"] = frame(np.full(300, 20.0))
    books, regime = daily_books(daily, config, pd.Timestamp("2026-02-24T22:00Z"))
    names = {b.name for b in books}
    assert {f"{TIMING} · TQQQ", f"{TIMING} · QQQ", BURST, HAMMER, SCORE} <= names
    assert regime["index"] == "QQQ" and regime["vxn"] == 20.0 and regime["top_scores"]
    for book in books:
        assert book.kind == "daily"
        opens = [pd.Timestamp(t) for t, _ in book.schedule]
        assert all(t.tz_convert("America/New_York").strftime("%H:%M") == "09:30" for t in opens)
    timing = next(b for b in books if b.name == f"{TIMING} · TQQQ")
    assert timing.cap == 1.0

    # the timing book can hold 100% of TQQQ; the research engine turns it into a sleeve
    intraday = synthetic_bars(config, days=10, end=pd.Timestamp("2026-02-24T21:00Z"))
    timing.schedule = [["2026-02-18T14:30:00+00:00", {"TQQQ": 1.0}]]
    research = run_research(intraday, config, all_strategies(), copy_books=[timing])
    sleeve = research.sleeves[timing.name]
    assert sleeve.kind == "daily"
    before = sleeve.weights.index < pd.Timestamp("2026-02-18T14:30Z")
    assert (sleeve.weights[before].to_numpy() == 0).all()
    assert sleeve.weights["TQQQ"].iloc[-1] == pytest.approx(1.0)


def test_daily_data_refreshes_after_each_close_and_uses_its_cache(tmp_path):
    calls = []

    def fetcher(symbols, period, now):
        calls.append(now)
        return {s: frame(np.linspace(100, 110, 50)) for s in symbols}

    data = DailyData(["QQQ"], tmp_path, fetcher=fetcher, refresh_hours=3)
    friday_noon = pd.Timestamp("2026-09-25T16:00Z")
    assert data.refresh(friday_noon) is None and len(calls) == 1
    data.refresh(friday_noon + pd.Timedelta(hours=1))
    assert len(calls) == 1  # fresh enough
    data.refresh(pd.Timestamp("2026-09-25T20:20Z"))  # just after Friday's close
    assert len(calls) == 2
    again = DailyData(["QQQ"], tmp_path, fetcher=fetcher, refresh_hours=3)
    assert set(again.bars) == {"QQQ", "^VXN", "^VIX"} and not again.due(pd.Timestamp("2026-09-25T20:30Z"))


def test_engine_trades_daily_sleeves_and_reports_the_regime(tmp_path):
    from agent.data import StaticData
    from agent.engine import Engine

    config = Config()
    end = pd.Timestamp("2026-02-24T20:00Z")
    intraday = synthetic_bars(config, days=10, end=end)
    fetcher = lambda symbols, period, now: {s: walk(i) for i, s in enumerate(symbols)}  # noqa: E731
    daily = DailyData(["QQQ", "TQQQ", "NVDA"], fetcher=fetcher)
    engine = Engine(config, tmp_path, market=StaticData(config, intraday, gbpusd=1.3), daily=daily)
    engine.tick(end)
    state = engine.store.load()
    assert state["regime"]["index"] == "QQQ" and state["regime"]["error"] is None
    assert f"{TIMING} · TQQQ" in state["sleeves"]
    readme = (tmp_path / "README.md").read_text()
    assert "Market regime" in readme and "Market regime" in (tmp_path / "dashboard.html").read_text()
