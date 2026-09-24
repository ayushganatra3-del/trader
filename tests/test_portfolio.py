import pytest

from agent.config import RiskConfig
from agent.portfolio import Quote, Sleeve, new_sleeve

NOW, DAY = "2026-09-24T15:00:00Z", "2026-09-24"


def quote(symbol="AAPL", price=100.0, fx=0.75, cost=0.001, tradable=True):
    return Quote(symbol, price, fx, cost, tradable)


def sleeve():
    return Sleeve(new_sleeve("test", 100.0, NOW))


def test_buy_then_sell_accounts_for_costs():
    s = sleeve()
    risk = RiskConfig()
    trades = s.rebalance({"AAPL": 0.5}, {"AAPL": quote()}, risk, NOW, DAY)
    assert len(trades) == 1 and trades[0]["side"] == "buy"
    assert s.data["cash_gbp"] == pytest.approx(50.0)
    trades = s.rebalance({}, {"AAPL": quote(price=110)}, risk, NOW, DAY)
    assert trades[0]["side"] == "sell" and trades[0]["closed"]
    # +10% move minus 0.1% on each side
    expected = 50 * 1.1 * (1 - 0.001) / (1 + 0.001)
    assert s.data["cash_gbp"] == pytest.approx(50 + expected)
    assert s.data["wins"] == 1 and s.data["closed_trades"] == 1
    assert s.data["positions"] == {}


def test_cash_never_goes_negative():
    s = sleeve()
    targets = {"A": 0.6, "B": 0.6}
    s.rebalance(targets, {"A": quote("A"), "B": quote("B")}, RiskConfig(), NOW, DAY)
    assert s.data["cash_gbp"] >= -1e-9


def test_rebalance_band_avoids_churn():
    s = sleeve()
    risk = RiskConfig(rebalance_band=0.05)
    s.rebalance({"AAPL": 0.25}, {"AAPL": quote()}, risk, NOW, DAY)
    assert s.rebalance({"AAPL": 0.25}, {"AAPL": quote(price=103)}, risk, NOW, DAY) == []


def test_untradable_quotes_are_left_alone():
    s = sleeve()
    s.rebalance({"AAPL": 0.25}, {"AAPL": quote()}, RiskConfig(), NOW, DAY)
    assert s.rebalance({}, {"AAPL": quote(tradable=False)}, RiskConfig(), NOW, DAY) == []
    assert "AAPL" in s.data["positions"]


def test_daily_loss_limit_flattens_and_pauses():
    s = sleeve()
    risk = RiskConfig(daily_loss_limit=0.05)
    s.rebalance({"AAPL": 1.0 / 3}, {"AAPL": quote()}, risk, NOW, DAY)
    trades = s.rebalance({"AAPL": 1.0 / 3}, {"AAPL": quote(price=80)}, risk, NOW, DAY)
    assert trades and trades[0]["side"] == "sell"
    assert s.data["halted_day"] == DAY
    assert s.rebalance({"AAPL": 1.0 / 3}, {"AAPL": quote(price=80)}, risk, NOW, DAY) == []
    # next day it trades again
    assert s.rebalance({"AAPL": 1.0 / 3}, {"AAPL": quote(price=80)}, risk, NOW, "2026-09-25")


def test_kill_switch_disables_sleeve():
    s = sleeve()
    risk = RiskConfig(kill_drawdown=0.3, daily_loss_limit=0.99, max_symbol_weight=1.0)
    s.rebalance({"AAPL": 1.0}, {"AAPL": quote()}, risk, NOW, DAY)
    s.rebalance({"AAPL": 1.0}, {"AAPL": quote(price=60)}, risk, NOW, DAY)
    assert s.data["disabled"]
    assert s.rebalance({"AAPL": 1.0}, {"AAPL": quote(price=100)}, risk, NOW, "2026-09-30") == []


def test_summary_is_json_friendly():
    s = sleeve()
    s.rebalance({"AAPL": 0.3}, {"AAPL": quote()}, RiskConfig(), NOW, DAY)
    summary = s.summary()
    assert summary["positions"][0]["symbol"] == "AAPL"
    assert summary["return_pct"] < 0  # paid costs
