import json
import os
import re
from pathlib import Path

import pytest

from agent.report_html import MAX_POINTS, render

ROOT = Path(__file__).resolve().parents[1]
EVIL = "<script>alert(1)</script>"


def curve(n=5, start=100.0, step=0.5, day=1):
    return [[f"2026-09-{day:02d}T{9 + i // 12:02d}:{(i % 12) * 5:02d}:00+00:00", start + i * step] for i in range(n)]


def live(equity=101.0, positions=(), **extra):
    return {"equity_gbp": equity, "return_pct": equity - 100, "cash_gbp": 80.0, "fees_gbp": 0.12, "closed_trades": 3,
            "win_rate_pct": 66.7, "max_drawdown_pct": -1.5, "halted": False, "halt_reason": None, "disabled": False,
            "positions": list(positions), **extra}


def sleeve(name, kind="strategy", live_summary=None, live_points=5, bt_return=2.0, description="does things"):
    return {"name": name, "kind": kind, "style": "trend" if kind == "strategy" else kind, "description": description,
            "live": live_summary, "targets": {"AAPL": 0.2},
            "backtest": {"return_pct": bt_return, "final_gbp": 100 + bt_return, "sharpe": 1.2, "max_drawdown_pct": -3.0,
                         "trades": 12, "win_rate_pct": 55.0, "profit_factor": 1.4, "per_day_pct": 0.1,
                         "exposure_pct": 20.0, "days": 30.0},
            "live_curve": curve(live_points) if live_summary else [],
            "backtest_curve": curve(40, step=bt_return / 40)}


def dashboard(mode="paper", **overrides):
    position = {"symbol": "AAPL", "units": 0.02, "cost_gbp": 20.0, "value_gbp": 20.5, "pnl_gbp": 0.5,
                "opened_at": "2026-09-01T09:05:00Z", "entry_price": 1000.0}
    sleeves = [sleeve("Agent", "meta", live(positions=[position])), sleeve("Agent (aggressive)", "meta", live(99.0)),
               sleeve("Consensus", "meta", live()), sleeve("Hold SPY", "benchmark", live()),
               sleeve("Hold BTC", "benchmark", live()),
               sleeve("Halted one", live_summary=live(98.0, halted=True, halt_reason="daily loss limit")),
               sleeve("Disabled one", live_summary=live(90.0, disabled=True))]
    sleeves += [sleeve(f"Strategy {i}", live_summary=live(100 + i), bt_return=i) for i in range(6)]
    base = {
        "generated_at": "2026-09-01T10:00:00+00:00", "started_at": "2026-09-01T09:00:00Z", "mode": mode,
        "starting_capital_gbp": 100.0, "ticks": 12,
        "last_tick": {"at": "2026-09-01T10:00:00Z", "data_errors": {}},
        "backtest_window": {"from": "2026-08-01T00:00:00+00:00", "to": "2026-09-01T00:00:00+00:00", "bars": 100},
        "selection": [{"strategy": "MACD cross", "symbol": "AAPL", "score": 2.3, "lookback_return_pct": 10.1,
                       "lookback_trades": 20, "holding": True}],
        "sleeves": sleeves,
        "recent_trades": [{"t": "2026-09-01T09:05:00Z", "sleeve": "Agent", "symbol": "AAPL", "side": "buy",
                           "units": 0.02, "price": 1000.0, "value_gbp": 20.0, "fee_gbp": 0.01, "pnl_gbp": None,
                           "reason": "entry"}],
        "broker": None,
        "disclaimer": "Paper money. Past results do not predict future returns.",
    }
    return {**base, **overrides}


def assert_page(page: str):
    assert page.startswith("<!doctype html>")
    assert page.rstrip().endswith("</html>")
    assert page.count("<script>") == 1 and page.count("<style>") == 1
    # self-contained: no external scripts, styles, fonts or images
    assert not re.search(r"""(src|href)\s*=\s*["']?(https?:)?//""", page)
    assert "@import" not in page and "url(" not in page


def test_full_dashboard_renders_every_section():
    page = render(dashboard())
    assert_page(page)
    for text in ("Trading agent", "Paper money", "Leaderboard", "Today&#x27;s picks", "Agent holdings",
                 "Recent trades", "MACD cross", "Past results do not predict", "Halted", "Disabled"):
        assert text in page, text
    assert page.count('class="plot"') == 2  # live and backtest charts
    assert "Collecting data" not in page
    assert "Broker account" not in page and "Data problems" not in page
    assert "£101.00" in page  # Agent balance


def test_escapes_untrusted_strings():
    evil_attr = '"><img src=x onerror=alert(1)>'
    data = dashboard(broker={"ok": False, "error": EVIL, "orders": [{"symbol": EVIL}], "positions": {EVIL: {"symbol": EVIL}}},
                     last_tick={"data_errors": {EVIL: EVIL}}, mode=EVIL)
    data["sleeves"].append(sleeve(EVIL, live_summary=live(150.0), bt_return=50.0, description=evil_attr))
    data["selection"][0]["strategy"] = EVIL
    data["recent_trades"][0]["reason"] = EVIL
    page = render(data)
    assert_page(page)
    assert EVIL not in page
    assert "<img" not in page
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in page


def test_empty_and_missing_fields_do_not_crash():
    for data in ({}, {"sleeves": []}, {"sleeves": None, "recent_trades": None, "selection": None, "last_tick": None},
                 {"sleeves": [{"name": "Agent"}, {"name": "X", "live": None, "backtest": None, "live_curve": None}]},
                 {"sleeves": [{"name": "Agent", "live": {"equity_gbp": None, "positions": None},
                               "backtest_curve": [["bad time", 1], [None, None], ["2026-09-01T00:00:00Z", "nan"]]}],
                  "broker": {}, "last_tick": {"data_errors": ["one", "two"]}, "starting_capital_gbp": None}):
        page = render(data)
        assert_page(page)
        assert "Trading agent" in page


def test_backtest_only_falls_back_to_backtest_numbers():
    data = dashboard(mode="backtest", started_at=None, ticks=0, recent_trades=[])
    for s in data["sleeves"]:
        s["live"], s["live_curve"] = None, []
    page = render(data)
    assert_page(page)
    assert "Backtest only" in page
    assert '<span class="badge">Backtest</span>' in page
    assert "£102.00" in page  # Agent's backtest final balance
    assert "No live trading yet" in page
    assert page.count('class="plot"') == 1


def test_single_live_point_shows_collecting_note():
    data = dashboard()
    for s in data["sleeves"]:
        s["live_curve"] = s["live_curve"][:1]
    page = render(data)
    assert "Collecting data" in page
    assert page.count('class="plot"') == 1  # only the backtest chart


def test_alpaca_live_shows_real_money_warning():
    page = render(dashboard(mode="alpaca-live"))
    assert 'class="banner"' in page and "real money" in page
    assert 'class="badge mode live"' in page
    for mode in ("paper", "alpaca-paper"):
        other = render(dashboard(mode=mode))
        assert 'class="banner"' not in other and "real money" not in other


def test_broker_and_data_problem_sections():
    broker = {"ok": True, "mode": "alpaca-paper", "equity_usd": 134.5, "cash_usd": 80.0, "budget_usd": 134.0,
              "market_open": True, "orders": [{"symbol": "AAPL", "side": "buy", "action": "buy", "notional": 26.8}],
              "positions": {"AAPL": {"symbol": "AAPL", "qty": 0.1, "market_value": 26.9, "unrealized_pl": -0.1}},
              "skipped": [{"symbol": "VOD.L", "reason": "not tradable on Alpaca"}], "errors": [], "error": None}
    page = render(dashboard(mode="alpaca-paper", broker=broker, last_tick={"data_errors": {"TSLA": "HTTP 429"}}))
    assert "Broker account" in page and "$134.50" in page and "not tradable on Alpaca" in page
    assert "Data problems" in page and "HTTP 429" in page


def test_long_curves_are_downsampled():
    data = dashboard()
    data["sleeves"][0]["backtest_curve"] = curve(1000, step=0.01)
    page = render(data)
    longest = max(len(d.split(" ")) for d in re.findall(r' d="M([^"]*)"', page))
    assert longest <= MAX_POINTS + 1


def paths():
    configured = [Path(p) for p in os.environ.get("DASHBOARD_EXAMPLES", "").split(os.pathsep) if p]
    return configured + [ROOT / "state" / "dashboard.json"]


@pytest.mark.parametrize("path", paths(), ids=str)
def test_real_dashboard_files(path):
    if not path.exists():
        pytest.skip(f"{path} not present")
    page = render(json.loads(path.read_text()))
    assert_page(page)
    assert len(page) < 1_500_000
