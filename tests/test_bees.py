import dataclasses
import io
import json
import urllib.error

import numpy as np
import pandas as pd
import pytest

from agent import bees
from agent.bees import BEES, Bee, Hive, JevClient, JevError, live_numbers, question_key, to_weights
from agent.config import Config, _crypto, _us
from agent.data import StaticData
from agent.engine import Engine

from conftest import END

BEE = Bee("Test", "a test trader", cap=0.25, max_positions=3, max_exposure=0.6, min_prob=0.5)


def minute_bars(symbols, end, minutes=120, seed=1):
    """1-minute bars whose last completed bar ends at ``end``."""
    rng = np.random.default_rng(seed)
    index = pd.date_range(end=end - pd.Timedelta(minutes=1), periods=minutes, freq="1min", tz="UTC")
    out = {}
    for i, symbol in enumerate(symbols):
        close = 100 * (i + 1) * np.exp(np.cumsum(rng.normal(0, 0.001, minutes)))
        out[symbol] = pd.DataFrame({"open": close, "high": close * 1.001, "low": close * 0.999, "close": close,
                                    "volume": rng.lognormal(10, 0.3, minutes)}, index=index)
    return out


class FakeJev:
    """Answers every question with hold unless told otherwise; records each call."""

    def __init__(self, picks=None, cost=0.001, fail=None):
        self.picks, self.cost, self.fail, self.calls = picks or {}, cost, fail, []

    def decide(self, state, questions):
        self.calls.append((state, questions))
        if self.fail:
            raise JevError(self.fail)
        answers = {}
        for key in questions:
            choice, p = self.picks.get(key, ("hold", 0.1))
            answers[key] = {"type": "choice", "choice": choice, "confidence": p,
                            "probabilities": {"buy": p if choice == "buy" else 0.1, "hold": 0.5, "sell": 0.1}}
        return answers, self.cost


def test_answers_become_capped_weights():
    keys = {question_key(s): s for s in ("AAA", "BBB", "CCC", "DDD", "BTC-USD")}
    answers = {"AAA": {"choice": "buy", "probabilities": {"buy": 0.8}},
               "BBB": {"choice": "buy", "probabilities": {"buy": 0.4}},  # below min_prob: no buy
               "CCC": {"choice": "sell", "probabilities": {"buy": 0.0}},
               "DDD": {"choice": "hold", "probabilities": {"buy": 0.2}},
               "BTC_USD": {"choice": "buy", "probabilities": {"buy": 1.0}}}
    held = {"CCC": 0.2, "DDD": 0.1, "EEE": 0.05}  # EEE is not open, so it is not asked about
    targets, decisions = to_weights(BEE, answers, keys, held)
    assert "CCC" not in targets and "BBB" not in targets
    assert decisions["AAA"] == ["buy", 0.8] and decisions["CCC"][0] == "sell"
    # AAA 0.2, BTC 0.25, DDD 0.1 kept, EEE 0.05 dropped by the 3-position limit; total 0.55 <= 0.6
    assert set(targets) == {"AAA", "BTC-USD", "DDD"}
    assert targets["AAA"] == pytest.approx(0.2) and targets["BTC-USD"] == pytest.approx(0.25)
    assert sum(targets.values()) <= BEE.max_exposure + 1e-9
    # a buy never shrinks a bigger position, and exposure is scaled down to the limit
    targets, _ = to_weights(BEE, {"AAA": {"choice": "buy", "probabilities": {"buy": 0.6}}}, {"AAA": "AAA"},
                            {"AAA": 0.3, "DDD": 0.5})
    assert targets["AAA"] / targets["DDD"] == pytest.approx(0.3 / 0.5) and sum(targets.values()) == pytest.approx(0.6)


def test_live_numbers_read_only_the_bars_given():
    bars = minute_bars(["AAA"], END)["AAA"]
    numbers = live_numbers(bars)
    close = bars["close"]
    assert numbers["price"] == pytest.approx(close.iloc[-1], rel=1e-6)
    assert numbers["chg_5m_pct"] == pytest.approx(100 * (close.iloc[-1] / close.iloc[-6] - 1), abs=1e-3)
    assert live_numbers(bars.iloc[:10]) is None
    assert live_numbers(bars.iloc[:-30]) != numbers  # the snapshot moves with every new bar


def test_client_posts_to_openrouter_decisions(monkeypatch):
    seen = {}

    class Reply(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

    def urlopen(request, timeout):
        seen["request"], seen["timeout"] = request, timeout
        return Reply(json.dumps({"answers": {"AAA": {"type": "choice", "choice": "buy"}},
                                 "usage": {"cost": 0.00042}}).encode())

    monkeypatch.setattr(bees.urllib.request, "urlopen", urlopen)
    answers, cost = JevClient("sk-test", "typesafe/jev-1.13").decide({"x": 1}, {"AAA": {"type": "choice"}})
    request = seen["request"]
    assert request.full_url == "https://openrouter.ai/api/alpha/decisions" and request.get_method() == "POST"
    assert request.get_header("Authorization") == "Bearer sk-test"
    body = json.loads(request.data)
    assert body == {"model": "typesafe/jev-1.13", "state": {"x": 1}, "questions": {"AAA": {"type": "choice"}}}
    assert answers["AAA"]["choice"] == "buy" and cost == pytest.approx(0.00042)

    def refuse(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 402, "Payment Required", {},
                                     io.BytesIO(b'{"error": {"message": "Insufficient credits"}}'))

    monkeypatch.setattr(bees.urllib.request, "urlopen", refuse)
    with pytest.raises(JevError, match="402: Insufficient credits"):
        JevClient("sk-test", "m").decide({}, {})


def hive_config(**bees_changes):
    config = Config(universe=(_us("SPY"), _us("NVDA"), _crypto("BTC-USD")))
    return dataclasses.replace(config, bees=dataclasses.replace(config.bees, **bees_changes))


def make_hive(config, client, end):
    data = StaticData(dataclasses.replace(config, interval="1m"), minute_bars(config.symbols, end), gbpusd=1.3)
    return Hive(config, client=client, data=data)


def test_each_bee_asks_about_every_open_symbol_and_trades():
    config = hive_config()
    client = FakeJev({"NVDA": ("buy", 0.9)})
    hive = make_hive(config, client, END)
    state = {"sleeves": {}}
    trades = hive.run(state, END + pd.Timedelta(seconds=30), lambda currency: 1 / 1.3, lambda name: config.risk)
    assert len(client.calls) == len(BEES)
    for state_sent, questions in client.calls:
        assert set(questions) == {"SPY", "NVDA", "BTC_USD"}  # US market open: stocks and crypto
        assert set(state_sent["market"]) == set(questions) and "NVDA" in questions["NVDA"]["instructions"]
        assert questions["NVDA"]["criteria"] == bees.MENU
    assert {c[0]["trader"] for c in client.calls} == {b.strategy for b in BEES}  # each bee's own personality
    for bee in BEES:
        sleeve = state["sleeves"][bee.sleeve]
        assert "NVDA" in sleeve["positions"] and set(sleeve["positions"]) == {"NVDA"}
        assert state["bees"][bee.name]["counts"] == {"buy": 1, "hold": 2, "sell": 0}
    assert {t["sleeve"] for t in trades} == {b.sleeve for b in BEES} and all(t["side"] == "buy" for t in trades)
    assert "Jev: buy" in trades[0]["reason"]
    spend = state["bees"]["spend"]
    assert spend["calls"] == 3 and spend["decisions"] == 9 and spend["usd"] == pytest.approx(0.003)


def test_overnight_only_crypto_is_asked_about():
    config = hive_config()
    night = pd.Timestamp("2026-09-24 23:00", tz="UTC")
    client = FakeJev()
    make_hive(config, client, night).run({"sleeves": {}}, night + pd.Timedelta(seconds=30),
                                         lambda c: 1 / 1.3, lambda n: config.risk)
    assert all(set(q) == {"BTC_USD"} for _, q in client.calls)


def test_budget_and_failures_leave_the_bees_holding():
    config = hive_config(daily_budget_usd=0.0025)
    client = FakeJev({"SPY": ("buy", 0.9)})
    hive = make_hive(config, client, END)
    state = {"sleeves": {}}
    now = END + pd.Timedelta(seconds=30)
    hive.run(state, now, lambda c: 1 / 1.3, lambda n: config.risk)
    held = {b.sleeve: dict(state["sleeves"][b.sleeve]["positions"]) for b in BEES}
    hive.run(state, now + pd.Timedelta(minutes=1), lambda c: 1 / 1.3, lambda n: config.risk)
    assert len(client.calls) == 3 and state["bees"]["budget_spent"]  # $0.003 spent of $0.0025: no more calls
    assert {b.sleeve: state["sleeves"][b.sleeve]["positions"] for b in BEES} == held
    # next UTC day the budget resets; an API failure is recorded and nothing is sold
    client.fail = "HTTP 402: Insufficient credits"
    hive.data = make_hive(config, client, END + pd.Timedelta(days=1)).data  # fresh prices for the next day
    trades = hive.run(state, now + pd.Timedelta(days=1), lambda c: 1 / 1.3, lambda n: config.risk)
    assert len(client.calls) == 6 and not state["bees"]["budget_spent"]
    assert "Insufficient credits" in state["bees"]["Bizzy"]["error"] and not [t for t in trades if t["side"] == "sell"]


def test_engine_trades_and_reports_the_bees(tmp_path, small_config, small_bars):
    client = FakeJev({"NVDA": ("buy", 0.9)})
    engine = Engine(small_config, tmp_path, market=StaticData(small_config, small_bars, gbpusd=1.3),
                    hive=make_hive(small_config, client, END))
    engine.tick(END + pd.Timedelta(seconds=30))
    state = engine.store.load()
    assert all("NVDA" in state["sleeves"][b.sleeve]["positions"] for b in BEES)
    dashboard = json.loads((tmp_path / "dashboard.json").read_text())
    rows = {s["name"]: s for s in dashboard["sleeves"]}
    assert all(rows[b.sleeve]["live"] and rows[b.sleeve]["backtest"] is None for b in BEES)
    assert dashboard["bees"]["spend"]["decisions"] == 12  # 3 bees x 4 open symbols
    assert "AI bees (Jev: typesafe/jev-1.13)" in (tmp_path / "README.md").read_text()
    assert "AI bees" in (tmp_path / "dashboard.html").read_text()
    # a restart keeps trading the same sleeves
    engine2 = Engine(small_config, tmp_path, market=StaticData(small_config, small_bars, gbpusd=1.3),
                     hive=make_hive(small_config, client, END + pd.Timedelta(minutes=1)))
    engine2.tick(END + pd.Timedelta(minutes=1, seconds=30))
    assert engine2.store.load()["bees"]["spend"]["calls"] == 6


def test_big_universes_are_split_into_calls_of_32_questions(monkeypatch):
    monkeypatch.setattr(bees, "QUESTIONS_PER_CALL", 2)
    config = hive_config()
    client = FakeJev({"BTC_USD": ("buy", 0.9)})
    state = {"sleeves": {}}
    make_hive(config, client, END).run(state, END + pd.Timedelta(seconds=30), lambda c: 1 / 1.3, lambda n: config.risk)
    assert sorted(len(q) for _, q in client.calls) == [1, 1, 1, 2, 2, 2]  # 3 symbols in calls of 2, for each bee
    assert state["bees"]["spend"]["calls"] == 6 and state["bees"]["spend"]["decisions"] == 9
    assert all("BTC-USD" in state["sleeves"][b.sleeve]["positions"] for b in BEES)


def test_paid_batches_count_when_a_later_batch_fails(monkeypatch):
    monkeypatch.setattr(bees, "QUESTIONS_PER_CALL", 2)
    config = hive_config()

    class SecondBatchFails(FakeJev):
        def decide(self, state, questions):
            if len(questions) == 1:
                self.calls.append((state, questions))
                raise JevError("HTTP 500: upstream error")
            return super().decide(state, questions)

    client = SecondBatchFails({"SPY": ("buy", 0.9)})
    state = {"sleeves": {}}
    make_hive(config, client, END).run(state, END + pd.Timedelta(seconds=30), lambda c: 1 / 1.3, lambda n: config.risk)
    spend = state["bees"]["spend"]
    assert spend["calls"] == 3 and spend["usd"] == pytest.approx(0.003) and spend["decisions"] == 0
    assert all("upstream error" in state["bees"][b.name]["error"] for b in BEES)
    assert all(not state["sleeves"][b.sleeve]["positions"] for b in BEES)  # no half-made decisions acted on


def test_bees_need_an_openrouter_key(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    assert not Hive.available()
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    hive = Hive(Config())
    assert Hive.available() and hive.client.api_key == "sk-test"
    assert len(hive.assets) * len(BEES) == 96  # ~100 decisions a minute while US markets are open
    assert all(a.trade_strategies for a in hive.data.config.universe)  # every symbol refreshed each minute


def test_doctor_fails_when_there_is_nothing_to_ask_jev(monkeypatch, capsys):
    from agent import __main__ as cli

    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    monkeypatch.setattr(Hive, "refresh", lambda self, now, fx: ({}, {}, {"BTC-USD": "timed out"}))
    assert cli._check_bees(Config()) is False  # crypto always trades, so no data means broken feeds
    assert "jev FAIL" in capsys.readouterr().out
