"""The holdings website (docs/index.html, served by GitHub Pages) reads the bot's dashboard.json:
keep the fields it uses and the fields the engine writes in step."""
import json
from pathlib import Path

import pandas as pd

from agent.data import StaticData
from agent.engine import Engine

from conftest import END

PAGE = Path(__file__).resolve().parents[1] / "docs" / "index.html"


def test_site_reads_fields_the_engine_writes(tmp_path, small_config, small_bars):
    Engine(small_config, tmp_path, market=StaticData(small_config, small_bars, gbpusd=1.3)).tick(END + pd.Timedelta(seconds=30))
    dashboard = json.loads((tmp_path / "dashboard.json").read_text())
    page = PAGE.read_text()
    assert "/agent-state/dashboard.json" in page

    top = ("generated_at", "mode", "starting_capital_gbp", "sleeves", "recent_trades", "bees")
    live = ("equity_gbp", "cash_gbp", "return_pct", "positions", "closed_trades", "halted", "disabled", "halt_reason")
    position = ("symbol", "units", "cost_gbp", "value_gbp", "pnl_gbp", "opened_at")
    trade = ("t", "sleeve", "side", "symbol", "value_gbp", "pnl_gbp", "reason")
    held = next(s for s in dashboard["sleeves"] if s["live"] and s["live"]["positions"])
    assert set(top) <= set(dashboard)
    assert set(live) <= set(held["live"]) and "live_curve" in held
    assert set(position) <= set(held["live"]["positions"][0])
    assert set(trade) <= set(dashboard["recent_trades"][0])
    for field in ("generated_at", "starting_capital_gbp", "live_curve", "recent_trades") + live + position + ("reason",):
        assert field in page, field
