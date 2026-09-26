import json
from types import SimpleNamespace

import numpy as np
import pandas as pd

from agent.analyst import BOOK, Analyst, clean_positions, snapshot
from agent.config import Config
from agent.research import run_research
from agent.data import synthetic_bars
from agent.strategies import all_strategies

DAYS = pd.bdate_range("2025-01-01", periods=300)


def walk(seed):
    rng = np.random.default_rng(seed)
    close = 100 * np.exp(np.cumsum(rng.normal(0.0005, 0.02, len(DAYS))))
    return pd.DataFrame({"open": close, "high": close * 1.01, "low": close * 0.99, "close": close,
                         "volume": rng.lognormal(15, 0.4, len(DAYS))}, index=DAYS)


def block(**kwargs):
    return SimpleNamespace(**kwargs)


class FakeClient:
    """Mimics the two Anthropic SDK calls the analyst makes."""

    def __init__(self, decision, pause_first=False):
        self.calls = []
        self.decision = decision
        self.pause_first = pause_first
        self.beta = SimpleNamespace(messages=SimpleNamespace(create=self._research))
        self.messages = SimpleNamespace(create=self._decide)

    def _research(self, **kwargs):
        self.calls.append(("research", kwargs))
        if self.pause_first and len(self.calls) == 1:
            return block(stop_reason="pause_turn", content=[block(type="server_tool_use")])
        return block(stop_reason="end_turn", content=[block(type="text", text="Bull case wins on NVDA.")])

    def _decide(self, **kwargs):
        self.calls.append(("decide", kwargs))
        return block(stop_reason="end_turn", content=[block(type="text", text=json.dumps(self.decision))])


def test_clean_positions_caps_and_normalises():
    raw = [{"symbol": "NVDA", "weight": 60}, {"symbol": "AAPL", "weight": 0.5}, {"symbol": "XXX", "weight": 0.3},
           {"symbol": "MSFT", "weight": 0.35}, {"symbol": "AMD", "weight": 0.1}, {"symbol": "TSLA", "weight": 0.05}]
    weights = clean_positions(raw, ["NVDA", "AAPL", "MSFT", "AMD", "TSLA"], max_positions=4, cap=0.35)
    assert set(weights) == {"NVDA", "AAPL", "MSFT", "AMD"}  # unknown symbol and the smallest dropped
    assert max(weights.values()) <= 0.35 + 1e-9 and sum(weights.values()) <= 1 + 1e-9


def test_snapshot_uses_only_completed_bars():
    rows = snapshot({"NVDA": walk(1)}, ["NVDA", "MISSING"])
    assert [r["symbol"] for r in rows] == ["NVDA"]
    assert rows[0]["close"] == round(walk(1)["close"].iloc[-1], 2)


def test_analyst_runs_once_per_session_and_trades_from_the_next_open():
    config = Config()
    daily = {s: walk(i) for i, s in enumerate(["QQQ", "NVDA", "AAPL", "TQQQ"])}
    decision = {"market_view": "Risk-on.", "positions": [{"symbol": "NVDA", "weight": 0.35, "reason": "Earnings beat"}]}
    client = FakeClient(decision, pause_first=True)
    analyst = Analyst(config, client)
    store = {}
    now = pd.Timestamp(DAYS[-1].strftime("%Y-%m-%d") + "T21:00Z")  # after that session's close
    book = analyst.run(store, daily, {"state": "uptrend"}, now)
    assert [c[0] for c in client.calls] == ["research", "research", "decide"]  # resumed the paused turn
    research = client.calls[0][1]
    assert research["fallbacks"] == "default" and research["tools"][0]["type"] == "web_search_20260209"
    assert "NVDA" in research["messages"][0]["content"]
    assert book.name == BOOK and book.kind == "ai" and book.current() == {"NVDA": 0.35}
    effective = pd.Timestamp(book.schedule[-1][0])
    assert effective > now and effective.tz_convert("America/New_York").strftime("%H:%M") == "09:30"
    assert store["latest"]["positions"][0]["reason"] == "Earnings beat"
    # same session again: no new API call
    analyst.run(store, daily, {"state": "uptrend"}, now + pd.Timedelta(hours=3))
    assert len(client.calls) == 3

    # the book becomes a forward-only sleeve: flat before the decision, 35% NVDA after it
    intraday = synthetic_bars(config, days=5, end=effective + pd.Timedelta(hours=2))
    research_result = run_research(intraday, config, all_strategies(), copy_books=[book])
    sleeve = research_result.sleeves[BOOK]
    assert (sleeve.weights[sleeve.weights.index < effective].to_numpy() == 0).all()
    assert abs(sleeve.weights["NVDA"].iloc[-1] - 0.35) < 1e-9


def test_analyst_failure_keeps_the_last_book_and_retries_later():
    config = Config()
    daily = {s: walk(i) for i, s in enumerate(["QQQ", "NVDA"])}

    class Broken(FakeClient):
        def _research(self, **kwargs):
            self.calls.append(("research", kwargs))
            raise RuntimeError("overloaded")

    client = Broken({})
    analyst = Analyst(config, client)
    store = {}
    now = pd.Timestamp(DAYS[-1].strftime("%Y-%m-%d") + "T21:00Z")
    book = analyst.run(store, daily, {"state": "uptrend"}, now)
    assert "overloaded" in book.error and book.schedule == []
    analyst.run(store, daily, {}, now + pd.Timedelta(minutes=30))
    assert len(client.calls) == 1  # waits before retrying
    analyst.run(store, daily, {}, now + pd.Timedelta(hours=2, minutes=5))
    assert len(client.calls) == 2


def test_engine_reports_the_analyst(tmp_path):
    from agent.daily import DailyData
    from agent.data import StaticData
    from agent.engine import Engine

    config = Config()
    end = pd.Timestamp(DAYS[-1].strftime("%Y-%m-%d") + "T20:30Z")
    fetcher = lambda symbols, period, now: {s: walk(i) for i, s in enumerate(symbols)}  # noqa: E731
    decision = {"market_view": "Choppy tape.", "positions": [{"symbol": "AAPL", "weight": 0.2, "reason": "Holding support"}]}
    engine = Engine(config, tmp_path, market=StaticData(config, synthetic_bars(config, days=5, end=end), gbpusd=1.3),
                    daily=DailyData(["QQQ", "AAPL"], fetcher=fetcher), analyst=Analyst(config, FakeClient(decision)))
    engine.tick(end)
    assert BOOK in engine.store.load()["sleeves"]
    readme = (tmp_path / "README.md").read_text()
    assert "AI analyst" in readme and "Holding support" in readme
    assert "Choppy tape." in (tmp_path / "dashboard.html").read_text()


def test_bees_trade_as_separate_personas():
    from agent.analyst import BEES

    config = Config()
    daily = {s: walk(i) for i, s in enumerate(["QQQ", "NVDA", "TQQQ"])}
    now = pd.Timestamp(DAYS[-1].strftime("%Y-%m-%d") + "T21:00Z")
    books = []
    for persona in BEES:
        client = FakeClient({"market_view": "x", "positions": [{"symbol": "TQQQ", "weight": 0.3, "reason": "r"}]})
        analyst = Analyst(config, client, persona=persona)
        books.append(analyst.run({}, daily, {"state": "uptrend"}, now))
        assert persona[1] in client.calls[0][1]["system"]  # its personality reaches the model
        assert analyst.store_key == f"analyst:{persona[0]}"
    assert [b.name for b in books] == ["AI bee: Bizzy", "AI bee: Breezy", "AI bee: Boozy"]
    assert all(b.current() == {"TQQQ": 0.3} for b in books)


def test_engine_runs_the_bees_alongside_the_analyst(tmp_path):
    from agent.analyst import BEES
    from agent.daily import DailyData
    from agent.data import StaticData
    from agent.engine import Engine

    config = Config()
    end = pd.Timestamp(DAYS[-1].strftime("%Y-%m-%d") + "T20:30Z")
    fetcher = lambda symbols, period, now: {s: walk(i) for i, s in enumerate(symbols)}  # noqa: E731
    decision = {"market_view": "ok", "positions": [{"symbol": "AAPL", "weight": 0.2, "reason": "r"}]}
    engine = Engine(config, tmp_path, market=StaticData(config, synthetic_bars(config, days=5, end=end), gbpusd=1.3),
                    daily=DailyData(["QQQ", "AAPL"], fetcher=fetcher), analyst=Analyst(config, FakeClient(decision)),
                    bees=[Analyst(config, FakeClient(decision), persona=bee) for bee in BEES])
    engine.tick(end)
    sleeves = engine.store.load()["sleeves"]
    assert BOOK in sleeves and all(f"AI bee: {name}" in sleeves for name, _ in BEES)
