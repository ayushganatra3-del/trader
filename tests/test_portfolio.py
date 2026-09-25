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


def test_weekly_limit_and_loss_streak_cooldown():
    risk = RiskConfig(weekly_loss_limit=0.05, loss_streak_cooldown=2, cooldown_hours=24,
                      daily_loss_limit=0.99, max_symbol_weight=1.0)
    s = sleeve()
    monday, tuesday = "2026-09-21", "2026-09-22"
    s.rebalance({"A": 0.5}, {"A": quote("A")}, risk, "2026-09-21T14:00:00+00:00", monday)
    s.rebalance({}, {"A": quote("A", price=97)}, risk, "2026-09-21T15:00:00+00:00", monday)  # loss 1
    s.rebalance({"B": 0.5}, {"B": quote("B")}, risk, "2026-09-21T16:00:00+00:00", monday)
    s.rebalance({}, {"B": quote("B", price=97)}, risk, "2026-09-21T17:00:00+00:00", monday)  # loss 2
    assert s.data["cooldown_until"].startswith("2026-09-22T17:00")
    assert s.rebalance({"C": 0.5}, {"C": quote("C")}, risk, "2026-09-22T10:00:00+00:00", tuesday) == []
    assert "losing trades" in s.data["halt_reason"]
    # after the cooldown it buys again; a >5% weekly loss then halts until next week
    trades = s.rebalance({"C": 1.0}, {"C": quote("C")}, risk, "2026-09-22T18:00:00+00:00", tuesday)
    assert trades and trades[0]["side"] == "buy"
    s.rebalance({"C": 1.0}, {"C": quote("C", price=90)}, risk, "2026-09-22T19:00:00+00:00", tuesday)
    assert "Weekly loss limit" in s.data["halt_reason"] and s.data["positions"] == {}
    assert s.rebalance({"C": 1.0}, {"C": quote("C", price=90)}, risk, "2026-09-24T19:00:00+00:00", "2026-09-24") == []
    assert s.rebalance({"C": 1.0}, {"C": quote("C", price=90)}, risk, "2026-09-28T14:00:00+00:00", "2026-09-28")


def test_weights_reflect_holdings():
    s = sleeve()
    s.rebalance({"A": 0.3}, {"A": quote("A")}, RiskConfig(), NOW, DAY)
    assert s.weights()["A"] == pytest.approx(0.3, abs=0.01)
