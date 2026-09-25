import json

import numpy as np
import pandas as pd
import pytest

from agent.config import Config, _crypto
from agent.data import StaticData, synthetic_bars
from agent.engine import Engine
from agent.research import run_research
from agent.strategies import all_strategies

from conftest import END


class ReplayData(StaticData):
    """Serves bars only up to a movable clock, like a live feed would."""

    def __init__(self, config, bars, gbpusd):
        super().__init__(config, bars, gbpusd)
        self.full = bars

    def at(self, now):
        self.bars = {s: b[b.index + pd.Timedelta(minutes=5) <= now] for s, b in self.full.items()}


def crypto_config(**kwargs):
    base = Config(universe=(_crypto("BTC-USD"), _crypto("ETH-USD")),
                  disabled_strategies=tuple(s.name for s in all_strategies()
                                            if s.name not in ("EMA 9/21 cross", "Bollinger reversion", "Hold BTC")))
    return base


def test_tick_writes_state_and_reports(tmp_path, small_config, small_bars):
    market = StaticData(small_config, small_bars, gbpusd=1.3)
    engine = Engine(small_config, tmp_path, market=market)
    result = engine.tick(END + pd.Timedelta(seconds=30))
    assert result["errors"] == {}
    for name in ("state.json", "dashboard.json", "README.md", "history.jsonl"):
        assert (tmp_path / name).exists(), name
    state = json.loads((tmp_path / "state.json").read_text())
    assert "Agent" in state["sleeves"] and "Hold SPY" in state["sleeves"]
    dashboard = json.loads((tmp_path / "dashboard.json").read_text())
    assert dashboard["sleeves"] and dashboard["mode"] == "paper"
    # restart from disk and keep going
    engine2 = Engine(small_config, tmp_path, market=market)
    engine2.tick(END + pd.Timedelta(minutes=1))
    state2 = json.loads((tmp_path / "state.json").read_text())
    assert state2["ticks"] == 2 and state2["created_at"] == state["created_at"]


def test_equity_is_conserved_without_price_moves(tmp_path, small_config, small_bars):
    market = StaticData(small_config, small_bars, gbpusd=1.3)
    engine = Engine(small_config, tmp_path, market=market)
    engine.tick(END + pd.Timedelta(seconds=30))
    state = json.loads((tmp_path / "state.json").read_text())
    for name, sleeve in state["sleeves"].items():
        # only costs can have been lost so far
        assert 99.0 < sleeve["equity_gbp"] <= 100.0 + 1e-9, name


def test_stocks_do_not_trade_when_market_closed(tmp_path, small_config, small_bars):
    saturday = pd.Timestamp("2026-09-26 15:00", tz="UTC")
    bars = synthetic_bars(small_config, days=15, seed=3, end=saturday)
    engine = Engine(small_config, tmp_path, market=StaticData(small_config, bars, gbpusd=1.3))
    result = engine.tick(saturday)
    assert result["trades"]
    assert {t["symbol"] for t in result["trades"]} <= {"BTC-USD", "ETH-USD"}


def test_paper_trading_matches_backtest(tmp_path):
    """Replaying bars one at a time through the live engine should reproduce
    the vectorised backtest (up to rebalancing-band and entry-cost noise)."""
    config = crypto_config()
    bars = synthetic_bars(config, days=12, seed=11, end=END)
    replay = ReplayData(config, bars, gbpusd=1.25)
    engine = Engine(config, tmp_path, market=replay)
    times = bars["BTC-USD"].index[-60:] + pd.Timedelta(minutes=5, seconds=20)
    for now in times:
        replay.at(now)
        engine.tick(now)
    state = json.loads((tmp_path / "state.json").read_text())
    research = run_research(bars, config, all_strategies(disabled=config.disabled_strategies))
    for name in ("EMA 9/21 cross", "Bollinger reversion", "Hold BTC"):
        returns = research.sleeves[name].returns
        start = returns.index.get_loc(times[0] - pd.Timedelta(minutes=5, seconds=20))
        backtest = float(np.prod(1 + returns.iloc[start + 1:]))
        paper = state["sleeves"][name]["equity_gbp"] / 100.0
        assert paper == pytest.approx(backtest, abs=0.02), name


def test_broker_mirrors_the_paper_sleeve_with_extra_breakers(tmp_path, small_config, small_bars, monkeypatch):
    import dataclasses

    from agent import live

    config = dataclasses.replace(small_config, broker=dataclasses.replace(small_config.broker, mode="alpaca-paper"))
    seen = {}

    def fake_sync(broker, targets, cfg, now, prices_usd, gbpusd, stamp):
        seen["targets"] = targets
        return {"ok": True, "orders": []}

    monkeypatch.setattr(live, "sync_broker", fake_sync)
    engine = Engine(config, tmp_path, market=StaticData(config, small_bars, gbpusd=1.3), broker=object())
    engine.tick(END + pd.Timedelta(seconds=30))
    state = json.loads((tmp_path / "state.json").read_text())
    agent = state["sleeves"]["Agent"]
    held = {s for s, p in agent["positions"].items()}
    assert {s for s, w in seen["targets"].items() if w > 0} == held
    assert set(seen["targets"]) == set(config.symbols)  # explicit zeros for everything else
    assert engine._risk_for("Agent").weekly_loss_limit == 0.05
    assert engine._risk_for("EMA 9/21 cross").weekly_loss_limit is None
