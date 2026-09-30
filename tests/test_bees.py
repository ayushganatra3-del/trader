import dataclasses
import io
import json
import urllib.error

import numpy as np
import pandas as pd
import pytest

from agent import bees
from agent.bees import BEES, Bee, Hive, Holding, JevClient, JevError, live_numbers, plan, question_key
from agent.config import Config, _crypto, _us
from agent.data import StaticData
from agent.engine import Engine

from conftest import END

BEE = Bee("Test", "a test trader", cap=0.25, max_positions=3, max_exposure=0.6, min_prob=0.5, sell_prob=0.5,
          hold_minutes=10, stop_loss=0.03, cooldown_minutes=15)
T0 = pd.Timestamp("2026-09-24 15:00", tz="UTC")


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
            answers[key] = {"type": "choice", "confidence": p, **ans(choice, p)}
        return answers, self.cost


def ans(choice, p):
    return {"choice": choice, "probabilities": {"buy": p if choice == "buy" else 0.1, "hold": 0.3,
                                                "sell": p if choice == "sell" else 0.1}}


def test_buys_need_a_confident_call_and_fit_the_limits():
    keys = {question_key(s): s for s in ("AAA", "BBB", "CCC", "BTC-USD")}
    answers = {"AAA": ans("buy", 0.8), "BBB": ans("buy", 0.4), "CCC": ans("hold", 0.2), "BTC_USD": ans("buy", 1.0)}
    book = {"CCC": Holding(0.2, 0.01, 30), "EEE": Holding(0.05, 0.0, 30)}  # EEE is closed, so it is not asked about
    memory = {}
    targets, decisions = plan(BEE, answers, keys, book, memory, T0 - pd.Timedelta(minutes=1))
    assert targets == {"CCC": 0.2, "EEE": 0.05} and decisions["AAA"][2] == "warming up"  # a first answer only seeds
    targets, decisions = plan(BEE, answers, keys, book, memory, T0)
    # the strongest three (BTC 0.25, AAA 0.2, CCC 0.2) trimmed together to the 60% limit; EEE makes way
    assert set(targets) == {"AAA", "BTC-USD", "CCC"} and sum(targets.values()) == pytest.approx(0.6, abs=1e-3)
    assert targets["BTC-USD"] / targets["AAA"] == pytest.approx(0.25 / 0.2, rel=1e-3)
    assert decisions["BBB"] == ["buy", 0.4, ""] and decisions["AAA"][2] == "buy (buy p=0.80)"
    assert "EEE" in memory["sold"]


def test_a_one_minute_blip_is_ignored_but_a_steady_call_gets_through():
    memory, keys = {}, {"AAA": "AAA"}
    for minute in range(3):
        plan(BEE, {"AAA": ans("hold", 0.1)}, keys, {}, memory, T0 + pd.Timedelta(minutes=minute))
    targets, _ = plan(BEE, {"AAA": ans("buy", 0.9)}, keys, {}, memory, T0 + pd.Timedelta(minutes=3))
    assert targets == {}  # running buy probability 0.34
    targets, decisions = plan(BEE, {"AAA": ans("buy", 0.9)}, keys, {}, memory, T0 + pd.Timedelta(minutes=4))
    assert "AAA" in targets and decisions["AAA"][1] == pytest.approx(0.508, abs=1e-3)


def test_positions_are_held_then_sold_only_on_a_confident_call():
    memory, keys = {}, {"AAA": "AAA"}
    targets, decisions = plan(BEE, {"AAA": ans("sell", 0.9)}, keys, {"AAA": Holding(0.25, 0.005, 3)}, memory, T0)
    assert targets == {"AAA": 0.25} and decisions["AAA"][2] == "holding (3 of 10 min)"
    later = T0 + pd.Timedelta(minutes=9)
    targets, _ = plan(BEE, {"AAA": ans("hold", 0.2)}, keys, {"AAA": Holding(0.25, 0.005, 12)}, memory, later)
    assert targets == {"AAA": 0.25}  # "hold" never sells
    targets, decisions = plan(BEE, {"AAA": ans("sell", 0.9)}, keys, {"AAA": Holding(0.25, 0.005, 13)}, memory,
                              later + pd.Timedelta(minutes=1))
    assert targets == {} and decisions["AAA"][2].startswith("sell")


def test_stop_loss_exits_inside_the_holding_time_and_blocks_a_quick_rebuy():
    memory, keys = {}, {"AAA": "AAA"}
    targets, decisions = plan(BEE, {"AAA": ans("buy", 0.9)}, keys, {"AAA": Holding(0.25, -0.035, 2)}, memory, T0)
    assert targets == {} and decisions["AAA"][2] == "stop-loss at -3.5%"
    targets, decisions = plan(BEE, {"AAA": ans("buy", 0.95)}, keys, {}, memory, T0 + pd.Timedelta(minutes=5))
    assert targets == {} and decisions["AAA"][2] == "cooling down after a sale"
    targets, decisions = plan(BEE, {"AAA": ans("buy", 0.95)}, keys, {}, memory, T0 + pd.Timedelta(minutes=16))
    assert targets == {} and decisions["AAA"][2] == "warming up"  # 11 minutes since its last answer
    targets, _ = plan(BEE, {"AAA": ans("buy", 0.95)}, keys, {}, memory, T0 + pd.Timedelta(minutes=17))
    assert "AAA" in targets


def test_positions_being_held_are_never_trimmed_for_new_buys():
    book = {"AAA": Holding(0.4, 0.0, 2)}
    answers = {k: ans("buy", 0.9) for k in ("BBB", "CCC", "DDD")}
    memory = {}
    plan(BEE, answers, {k: k for k in answers}, book, memory, T0 - pd.Timedelta(minutes=1))
    targets, _ = plan(BEE, answers, {k: k for k in answers}, book, memory, T0)
    assert targets["AAA"] == 0.4 and len(targets) == 3 and sum(targets.values()) == pytest.approx(0.6, abs=1e-3)


def test_flip_flopping_answers_no_longer_churn_the_sleeves():
    class ReplayFeed(StaticData):
        def __init__(self, config, bars):
            super().__init__(config, bars, gbpusd=1.3)
            self.full = bars

        def refresh(self, now=None):
            self.bars = {s: b[b.index + pd.Timedelta(minutes=1) <= now] for s, b in self.full.items()}
            return {}

    class FlipFlop(FakeJev):
        """Buy one minute, sell the next, for everything: the noise that churned the first bees."""

        def decide(self, state, questions):
            self.calls.append((state, questions))
            turn = sum(1 for s, _ in self.calls if s["trader"] == state["trader"])
            return {key: ans("buy" if turn % 2 else "sell", 0.9) for key in questions}, 0.0

    config = hive_config()
    start = END - pd.Timedelta(minutes=60)
    feed = ReplayFeed(dataclasses.replace(config, interval="1m"), minute_bars(config.symbols, END + pd.Timedelta(minutes=1), 200))
    hive = Hive(config, client=FlipFlop(), data=feed)
    state, trades = {"sleeves": {}}, []
    for minute in range(60):
        trades += hive.run(state, start + pd.Timedelta(minutes=minute, seconds=30), lambda c: 1 / 1.3, lambda n: config.risk)
    per_bee = {b.sleeve: sum(1 for t in trades if t["sleeve"] == b.sleeve) for b in BEES}
    assert per_bee["AI bee: Bizzy"] > 0  # it still trades...
    assert all(n <= 5 * 3 for n in per_bee.values())  # ...but a handful of times an hour per symbol, not every minute


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
    assert trades == [] and len(client.calls) == len(BEES)  # the first answers only warm up the averages
    trades = hive.run(state, END + pd.Timedelta(minutes=1, seconds=30), lambda c: 1 / 1.3, lambda n: config.risk)
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
    assert spend["calls"] == 6 and spend["decisions"] == 18 and spend["usd"] == pytest.approx(0.006)


def test_overnight_only_crypto_is_asked_about():
    config = hive_config()
    night = pd.Timestamp("2026-09-24 23:00", tz="UTC")
    client = FakeJev()
    make_hive(config, client, night).run({"sleeves": {}}, night + pd.Timedelta(seconds=30),
                                         lambda c: 1 / 1.3, lambda n: config.risk)
    assert all(set(q) == {"BTC_USD"} for _, q in client.calls)


def test_budget_and_failures_leave_the_bees_holding():
    config = hive_config(daily_budget_usd=0.0055)
    client = FakeJev({"SPY": ("buy", 0.9)})
    hive = make_hive(config, client, END)
    state = {"sleeves": {}}
    now = END + pd.Timedelta(seconds=30)
    for minute in range(2):
        hive.run(state, now + pd.Timedelta(minutes=minute), lambda c: 1 / 1.3, lambda n: config.risk)
    held = {b.sleeve: dict(state["sleeves"][b.sleeve]["positions"]) for b in BEES}
    assert all("SPY" in h for h in held.values())
    hive.run(state, now + pd.Timedelta(minutes=2), lambda c: 1 / 1.3, lambda n: config.risk)
    assert len(client.calls) == 6 and state["bees"]["budget_spent"]  # $0.006 spent of $0.0055: no more calls
    assert {b.sleeve: state["sleeves"][b.sleeve]["positions"] for b in BEES} == held
    # next UTC day the budget resets; an API failure is recorded and nothing is sold
    client.fail = "HTTP 402: Insufficient credits"
    hive.data = make_hive(config, client, END + pd.Timedelta(days=1)).data  # fresh prices for the next day
    trades = hive.run(state, now + pd.Timedelta(days=1), lambda c: 1 / 1.3, lambda n: config.risk)
    assert len(client.calls) == 9 and not state["bees"]["budget_spent"]
    assert "Insufficient credits" in state["bees"]["Bizzy"]["error"] and not [t for t in trades if t["side"] == "sell"]


def test_engine_trades_and_reports_the_bees(tmp_path, small_config, small_bars):
    client = FakeJev({"NVDA": ("buy", 0.9)})
    engine = Engine(small_config, tmp_path, market=StaticData(small_config, small_bars, gbpusd=1.3),
                    hive=make_hive(small_config, client, END))
    engine.tick(END + pd.Timedelta(seconds=30))
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
    state = engine2.store.load()
    assert state["bees"]["spend"]["calls"] == 6  # the averages carried over the restart, so the second minute trades
    assert all("NVDA" in state["sleeves"][b.sleeve]["positions"] for b in BEES)


def test_big_universes_are_split_into_calls_of_32_questions(monkeypatch):
    monkeypatch.setattr(bees, "QUESTIONS_PER_CALL", 2)
    config = hive_config()
    client = FakeJev({"BTC_USD": ("buy", 0.9)})
    state = {"sleeves": {}}
    hive = make_hive(config, client, END)
    for minute in range(2):
        hive.run(state, END + pd.Timedelta(minutes=minute, seconds=30), lambda c: 1 / 1.3, lambda n: config.risk)
    assert sorted(len(q) for _, q in client.calls) == [1] * 6 + [2] * 6  # 3 symbols in calls of 2, for each bee
    assert state["bees"]["spend"]["calls"] == 12 and state["bees"]["spend"]["decisions"] == 18
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


def test_stop_loss_still_works_without_fresh_jev_calls():
    from agent.portfolio import new_sleeve

    config = hive_config()
    hive = make_hive(config, FakeJev(fail="HTTP 402: Insufficient credits"), END)
    price_gbp = hive.data.bars["NVDA"]["close"].iloc[-1] / 1.3
    sleeve = new_sleeve("AI bee: Bizzy", 100.0, "2026-09-24T18:00:00Z")
    sleeve["positions"]["NVDA"] = {"units": 20 / price_gbp, "cost_gbp": 21.0, "opened_at": "2026-09-24T18:57:00Z",
                                   "entry_price": 0.0, "realised_gbp": 0.0}  # bought 3 minutes ago for £21, worth £20
    sleeve["cash_gbp"] = 79.0
    state = {"sleeves": {"AI bee: Bizzy": sleeve}}
    trades = hive.run(state, END + pd.Timedelta(seconds=30), lambda c: 1 / 1.3, lambda n: config.risk)
    assert [(t["sleeve"], t["side"], t["symbol"]) for t in trades] == [("AI bee: Bizzy", "sell", "NVDA")]
    assert trades[0]["reason"] == "stop-loss at -4.8% (no fresh Jev call)"
    assert "NVDA" in state["bees"]["memory"]["Bizzy"]["sold"]


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


def test_only_symbols_trading_now_are_fetched():
    from agent.data import MarketData

    config = hive_config()
    fetched, broken = [], set()

    def fetcher(symbol, interval, range_, now=None):
        if symbol == "GBPUSD=X":  # the feed's half-hourly FX refresh
            return minute_bars([symbol], now.floor("min"))[symbol]
        fetched.append(symbol)
        if symbol in broken:
            raise RuntimeError("rate limited")
        return minute_bars([symbol], now.floor("min"))[symbol]

    feed = MarketData(dataclasses.replace(config, interval="1m", history_range="1d"), None, fetcher=fetcher)
    hive = Hive(config, client=FakeJev(), data=feed)
    session = END + pd.Timedelta(seconds=30)
    hive.run({"sleeves": {}}, session, lambda c: 1 / 1.3, lambda n: config.risk)
    assert sorted(fetched) == ["BTC-USD", "NVDA", "SPY"]
    broken.add("NVDA")  # NVDA fails once while the market is open...
    hive.run({"sleeves": {}}, session + pd.Timedelta(minutes=2), lambda c: 1 / 1.3, lambda n: config.risk)
    fetched.clear()
    broken.clear()
    close = pd.Timestamp("2026-09-24 20:00:30", tz="UTC")  # the US close: one last fetch for the closing bar
    hive.run({"sleeves": {}}, close, lambda c: 1 / 1.3, lambda n: config.risk)
    assert {"SPY", "NVDA"} <= set(fetched)
    assert hive.data.bars["SPY"].index[-1] == pd.Timestamp("2026-09-24 19:59", tz="UTC")
    broken.add("NVDA")
    hive.run({"sleeves": {}}, close + pd.Timedelta(minutes=2), lambda c: 1 / 1.3, lambda n: config.risk)
    fetched.clear()
    night = pd.Timestamp("2026-09-24 23:00:30", tz="UTC")  # ...then the market is shut: its stale error is dropped
    state = {"sleeves": {}}
    hive.run(state, night, lambda c: 1 / 1.3, lambda n: config.risk)
    assert fetched == ["BTC-USD"] and "Bizzy" in state["bees"]  # stocks are not asked for all night
    fetched.clear()
    hive.run(state, END + pd.Timedelta(days=1, seconds=30), lambda c: 1 / 1.3, lambda n: config.risk)
    assert {"SPY", "NVDA"} <= set(fetched)  # and come back at the next session
