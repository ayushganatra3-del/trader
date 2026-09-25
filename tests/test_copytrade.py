import json

import numpy as np
import pandas as pd
import pytest

from agent import copytrade as ct
from agent.config import Config, _us
from agent.data import StaticData, synthetic_bars
from agent.engine import Engine

from conftest import END

TABLE = b"""<?xml version="1.0" encoding="UTF-8"?>
<informationTable xmlns="http://www.sec.gov/edgar/document/thirteenf/informationtable">
  <infoTable><nameOfIssuer>APPLE INC</nameOfIssuer><titleOfClass>COM</titleOfClass><cusip>037833100</cusip>
    <value>600</value><shrsOrPrnAmt><sshPrnamt>10</sshPrnamt><sshPrnamtType>SH</sshPrnamtType></shrsOrPrnAmt></infoTable>
  <infoTable><nameOfIssuer>APPLE INC</nameOfIssuer><titleOfClass>COM</titleOfClass><cusip>037833100</cusip>
    <value>100</value><shrsOrPrnAmt><sshPrnamt>2</sshPrnamt><sshPrnamtType>SH</sshPrnamtType></shrsOrPrnAmt></infoTable>
  <infoTable><nameOfIssuer>BERKSHIRE B</nameOfIssuer><titleOfClass>CL B</titleOfClass><cusip>084670702</cusip>
    <value>200</value><shrsOrPrnAmt><sshPrnamt>5</sshPrnamt><sshPrnamtType>SH</sshPrnamtType></shrsOrPrnAmt></infoTable>
  <infoTable><nameOfIssuer>BANK OF AMERICA</nameOfIssuer><titleOfClass>COM</titleOfClass><cusip>060505104</cusip>
    <value>100</value><shrsOrPrnAmt><sshPrnamt>5</sshPrnamt><sshPrnamtType>SH</sshPrnamtType></shrsOrPrnAmt></infoTable>
  <infoTable><nameOfIssuer>SOME PUT</nameOfIssuer><titleOfClass>PUT</titleOfClass><cusip>111111111</cusip>
    <value>999</value><shrsOrPrnAmt><sshPrnamt>5</sshPrnamt><sshPrnamtType>SH</sshPrnamtType></shrsOrPrnAmt><putCall>Put</putCall></infoTable>
  <infoTable><nameOfIssuer>A BOND</nameOfIssuer><titleOfClass>NOTE</titleOfClass><cusip>222222222</cusip>
    <value>999</value><shrsOrPrnAmt><sshPrnamt>5</sshPrnamt><sshPrnamtType>PRN</sshPrnamtType></shrsOrPrnAmt></infoTable>
</informationTable>"""

FIGI = {"037833100": "AAPL", "084670702": "BRK/B", "060505104": "BAC"}

INSIDER_HTML = """<html><body><table class="tinytable">
<thead><tr><th>X</th><th>Filing&nbsp;Date</th><th>Trade&nbsp;Date</th><th>Ticker</th><th>Company Name</th>
<th>Insider Name</th><th>Title</th><th>Trade&nbsp;Type</th><th>Price</th><th>Qty</th><th>Owned</th><th>ΔOwn</th><th>Value</th></tr></thead>
<tbody>
<tr><td>M</td><td>2026-09-22 16:05:12</td><td>2026-09-18</td><td><a href="/AAA">AAA</a></td><td>Aaa Inc</td><td>Jo</td><td>CEO</td><td>P - Purchase</td><td>$10.00</td><td>+100,000</td><td>1</td><td>+5%</td><td>+$1,000,000</td></tr>
<tr><td></td><td>2026-09-23 09:00:00</td><td>2026-09-21</td><td><a href="/BBB">BBB</a></td><td>Bbb Inc</td><td>Al</td><td>Dir</td><td>P - Purchase</td><td>$5.00</td><td>+60,000</td><td>1</td><td>+2%</td><td>+$300,000</td></tr>
<tr><td></td><td>2026-09-23 10:00:00</td><td>2026-09-21</td><td><a href="/CCC">CCC</a></td><td>Ccc Inc</td><td>Al</td><td>Dir</td><td>S - Sale</td><td>$5.00</td><td>-60,000</td><td>1</td><td>-2%</td><td>-$900,000</td></tr>
</tbody></table></body></html>"""


class FakeHttp:
    def __init__(self, filing_dates=("2026-05-15", "2026-08-14")):
        self.filing_dates = filing_dates
        self.posts = 0

    def get(self, url, headers=None):
        if "submissions" in url:
            n = len(self.filing_dates)
            return json.dumps({"name": "BERKSHIRE HATHAWAY INC", "filings": {"recent": {
                "form": ["13F-HR"] * n + ["4"],
                "accessionNumber": [f"0000950123-26-00000{i}" for i in range(n)] + ["x"],
                "filingDate": list(self.filing_dates) + ["2026-09-01"]}}}).encode()
        if url.endswith("index.json"):
            return json.dumps({"directory": {"item": [
                {"name": "primary_doc.xml", "size": "9999999"}, {"name": "infotable.xml", "size": "5000"},
                {"name": "0000950123-26-000001-index.htm", "size": "1"}]}}).encode()
        if url.endswith("infotable.xml"):
            return TABLE
        if "openinsider" in url:
            return INSIDER_HTML.encode()
        raise AssertionError(url)

    def post_json(self, url, body):
        self.posts += 1
        return json.dumps([{"data": [{"ticker": FIGI[j["idValue"]], "securityType": "Common Stock"}]}
                           if j["idValue"] in FIGI else {"warning": "No identifier found."} for j in body]).encode()


def test_parse_13f_skips_options_and_bonds_and_aggregates():
    holdings = ct.parse_13f_table(TABLE)
    assert set(holdings) == {"037833100", "084670702", "060505104"}
    assert holdings["037833100"]["value"] == 700


def test_map_cusips_uses_cache_and_yahoo_format():
    http, cache = FakeHttp(), {}
    tickers = ct.map_cusips(["037833100", "084670702", "999999999"], http, cache)
    assert tickers == {"037833100": "AAPL", "084670702": "BRK-B", "999999999": None}
    ct.map_cusips(["037833100"], http, cache)
    assert http.posts == 1  # second lookup served from cache


def test_13f_book_is_effective_only_after_filing(monkeypatch):
    monkeypatch.setattr(ct.time, "sleep", lambda s: None)
    config = Config()
    book = ct.fetch_13f_book("Buffett", "1067983", config, FakeHttp(), {}, now=pd.Timestamp("2026-09-24", tz="UTC"))
    assert book.error is None and not book.stale
    first, latest = book.schedule[0], book.schedule[-1]
    # filed Friday 2026-08-14 -> first usable at Monday's 09:30 New York open
    assert pd.Timestamp(latest[0]) == pd.Timestamp("2026-08-17 13:30", tz="UTC")
    assert pd.Timestamp(first[0]) < pd.Timestamp(latest[0])
    weights = latest[1]
    assert set(weights) == {"AAPL", "BRK-B", "BAC"}
    assert max(weights.values()) <= config.risk.max_symbol_weight + 1e-9
    assert sum(weights.values()) == pytest.approx(1.0, abs=1e-4)
    assert "BERKSHIRE" in book.description


def test_old_13f_is_marked_stale(monkeypatch):
    monkeypatch.setattr(ct.time, "sleep", lambda s: None)
    book = ct.fetch_13f_book("Burry", "1649339", Config(), FakeHttp(("2025-02-14",)), {},
                             now=pd.Timestamp("2026-09-24", tz="UTC"))
    assert book.stale and "too old" in book.error


def test_parse_openinsider_keeps_purchases_only():
    trades = ct.parse_openinsider(INSIDER_HTML)
    assert [t["ticker"] for t in trades] == ["AAA", "BBB"]
    assert trades[0]["value"] == 1_000_000
    # 16:05 New York filing -> 20:05 UTC
    assert trades[0]["filed"] == pd.Timestamp("2026-09-22 20:05:12", tz="UTC")


def test_insider_schedule_never_uses_future_filings():
    trades = ct.parse_openinsider(INSIDER_HTML)
    now = pd.Timestamp("2026-09-25 12:00", tz="UTC")
    schedule = ct.insider_schedule(trades, now, days=10, window=10, top_n=8)
    for when, weights in schedule:
        for ticker in weights:
            filed = min(t["filed"] for t in trades if t["ticker"] == ticker)
            assert filed < pd.Timestamp(when)
    by_time = {pd.Timestamp(w): h for w, h in schedule}
    # AAA was filed after the close on the 22nd, so it can't be held at that day's open
    assert by_time[pd.Timestamp("2026-09-22 13:30", tz="UTC")] == {}
    # BBB was filed at 09:00 New York on the 23rd, before that day's 09:30 open
    assert by_time[pd.Timestamp("2026-09-23 13:30", tz="UTC")] == {"AAA": 0.125, "BBB": 0.125}


def test_book_weights_follow_schedule_and_skip_missing_prices():
    index = pd.date_range("2026-09-21", periods=6, freq="1D", tz="UTC")
    book = ct.CopyBook("Copy: X", "", "test", schedule=[
        ["2026-09-22T00:00:00+00:00", {"AAA": 0.5, "BBB": 0.5}],
        ["2026-09-24T00:00:00+00:00", {"AAA": 0.25, "ZZZ": 0.75}]])
    weights = ct.book_weights(book, index, ["AAA", "BBB"], cap=1.0)
    assert weights[0].sum() == 0  # nothing before the first disclosure
    assert weights[1].tolist() == [0.5, 0.5]
    assert weights[3].tolist() == [1.0, 0.0]  # ZZZ has no prices: AAA takes the book
    stale = ct.CopyBook("Copy: Y", "", "test", schedule=book.schedule, stale=True)
    assert ct.book_weights(stale, index, ["AAA", "BBB"], cap=1.0).sum() == 0


class FakeCopier:
    def __init__(self, config, book):
        self.manager = ct.CopyManager(config, http=None)
        self.book = book

    def refresh(self, state, now):
        state.setdefault("copy", {"books": {}, "cusips": {}})["books"][self.book.name] = self.book.to_dict()
        return [self.book]

    def assets(self, books):
        return self.manager.assets(books)


def test_engine_trades_a_copy_book(tmp_path):
    config = Config(universe=(_us("SPY"), _us("NVDA")))
    bars = synthetic_bars(Config(universe=(_us("SPY"), _us("NVDA"), _us("AAPL"))), days=15, seed=4, end=END)
    book = ct.CopyBook("Copy: Test 13F", "test book", "test", schedule=[
        ["2026-09-15T13:30:00+00:00", {"AAPL": 0.35, "NVDA": 0.35}]], as_of="2026-09-14")
    engine = Engine(config, tmp_path, market=StaticData(config, bars, gbpusd=1.3), copier=FakeCopier(config, book))
    engine.tick(END + pd.Timedelta(seconds=30))
    assert "AAPL" in engine.run_config.symbols and not engine.run_config.asset("AAPL").trade_strategies
    state = json.loads((tmp_path / "state.json").read_text())
    positions = state["sleeves"]["Copy: Test 13F"]["positions"]
    assert set(positions) == {"AAPL", "NVDA"}
    dashboard = json.loads((tmp_path / "dashboard.json").read_text())
    assert dashboard["copy_books"][0]["holdings"] == {"AAPL": 0.35, "NVDA": 0.35}
    assert "Copy trading" in (tmp_path / "README.md").read_text()
    # strategies never trade copy-only tickers
    research = engine.research
    assert not any(symbol == "AAPL" for _, symbol in research.pair_columns)
    assert np.isclose(research.sleeves["Copy: Test 13F"].weights["AAPL"].iloc[-1], 0.35)
