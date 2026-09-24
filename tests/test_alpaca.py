import io
import json
import re
import urllib.error
import urllib.request
from urllib.parse import parse_qs, urlsplit

import pandas as pd
import pytest

from agent.brokers.alpaca import LIVE_URL, PAPER_URL, AlpacaBroker, AlpacaError, urllib_transport
from agent.config import DEFAULT_UNIVERSE, UK_ETFS, BrokerConfig, Config
from agent.live import (
    LIVE_CONFIRM_ENV,
    LIVE_CONFIRM_VALUE,
    client_order_id,
    make_broker,
    sync_broker,
)

NOW = pd.Timestamp("2026-09-24 15:05", tz="UTC")
STAMP = "2026-09-24T15:05:00+00:00"
GBPUSD = 1.34
BUDGET = 100 * GBPUSD


class FakeAlpaca:
    """In-memory transport: canned JSON per endpoint, records every request."""

    def __init__(self, account=None, positions=(), open_orders=(), is_open=True):
        self.account = {
            "equity": "10000", "cash": "10000", "buying_power": "20000",
            "non_marginable_buying_power": "10000", "last_equity": "9900.5",
            "daytrade_count": "0", "trading_blocked": False, "account_blocked": False,
            "status": "ACTIVE", **(account or {}),
        }
        self.positions = list(positions)
        self.open_orders = list(open_orders)
        self.is_open = is_open
        self.queued = {}  # (method, path) -> [(status, body), ...] served first
        self.reject = {}  # order symbol -> (status, message)
        self.calls = []

    def queue(self, method, path, *responses):
        self.queued.setdefault((method, path), []).extend(responses)

    def __call__(self, method, url, headers, body):
        parts = urlsplit(url)
        payload = json.loads(body) if body else None
        self.calls.append({"method": method, "url": url, "path": parts.path,
                           "query": parse_qs(parts.query), "headers": headers, "json": payload})
        queued = self.queued.get((method, parts.path))
        if queued:
            status, data = queued.pop(0)
            return status, json.dumps(data).encode()
        return self._route(method, parts.path, payload)

    def _route(self, method, path, payload):
        ok = lambda data: (200, json.dumps(data).encode())  # noqa: E731
        if method == "GET" and path == "/v2/account":
            return ok(self.account)
        if method == "GET" and path == "/v2/clock":
            return ok({"timestamp": "2026-09-24T11:05:00-04:00", "is_open": self.is_open})
        if method == "GET" and path == "/v2/positions":
            return ok(self.positions)
        if method == "GET" and path == "/v2/orders":
            return ok(self.open_orders)
        if method == "POST" and path == "/v2/orders":
            if payload["symbol"] in self.reject:
                status, message = self.reject[payload["symbol"]]
                return status, json.dumps({"code": 40310000, "message": message}).encode()
            return ok({"id": f"ord-{len(self.trades())}", "status": "accepted", **payload})
        if method == "DELETE" and path.startswith("/v2/positions/"):
            return ok({"id": f"close-{path.rsplit('/', 1)[-1]}", "status": "accepted"})
        return 404, b'{"message": "not found"}'

    def trades(self):
        return [c for c in self.calls if c["method"] in ("POST", "DELETE")]

    def order_bodies(self):
        return [c["json"] for c in self.calls if c["method"] == "POST"]


def position(symbol, qty, price, asset_class="us_equity"):
    return {"symbol": symbol, "qty": str(qty), "qty_available": str(qty), "side": "long",
            "market_value": str(qty * price), "avg_entry_price": str(price),
            "current_price": str(price), "unrealized_pl": "0", "asset_class": asset_class}


def make_config(**broker):
    options = {"mode": "alpaca-paper", "capital_gbp": 100.0, **broker}
    return Config(universe=DEFAULT_UNIVERSE + UK_ETFS, broker=BrokerConfig(**options))


def make_broker_for(fake, sleeps=None):
    return AlpacaBroker("key-id", "secret", paper=True, transport=fake,
                        sleep=(sleeps.append if sleeps is not None else lambda _s: None))


def run(fake, targets, config=None, prices=None, sleeps=None):
    return sync_broker(make_broker_for(fake, sleeps), targets, config or make_config(), NOW,
                       prices or {}, GBPUSD, STAMP)


def reasons(report):
    return {item["symbol"]: item["reason"] for item in report["skipped"]}


# --- client -----------------------------------------------------------------

def test_account_parsing_and_auth_headers():
    fake = FakeAlpaca(account={"daytrade_count": "2"})
    account = make_broker_for(fake).account()
    assert account["equity"] == 10000.0 and isinstance(account["equity"], float)
    assert account["cash"] == 10000.0
    assert account["buying_power"] == 20000.0
    assert account["non_marginable_buying_power"] == 10000.0
    assert account["last_equity"] == 9900.5
    assert account["daytrade_count"] == 2 and isinstance(account["daytrade_count"], int)
    call = fake.calls[0]
    assert call["url"] == PAPER_URL + "/v2/account"
    assert call["headers"]["APCA-API-KEY-ID"] == "key-id"
    assert call["headers"]["APCA-API-SECRET-KEY"] == "secret"


def test_live_broker_uses_live_url():
    fake = FakeAlpaca()
    AlpacaBroker("k", "s", paper=False, transport=fake).clock()
    assert fake.calls[0]["url"] == LIVE_URL + "/v2/clock"


def test_positions_normalise_crypto_symbols():
    fake = FakeAlpaca(positions=[position("BTCUSD", 0.001, 60000, "crypto"), position("AAPL", 2, 200)])
    positions = make_broker_for(fake).positions()
    assert set(positions) == {"BTC/USD", "AAPL"}
    btc = positions["BTC/USD"]
    assert btc["qty"] == 0.001 and btc["market_value"] == pytest.approx(60.0)
    assert btc["current_price"] == 60000.0 and btc["asset_class"] == "crypto"


def test_open_orders_query():
    fake = FakeAlpaca(open_orders=[{"symbol": "AAPL"}])
    assert make_broker_for(fake).open_orders() == [{"symbol": "AAPL"}]
    assert fake.calls[0]["query"] == {"status": ["open"], "limit": ["500"]}


def test_get_retries_on_429_and_5xx():
    fake = FakeAlpaca()
    fake.queue("GET", "/v2/account", (429, {"message": "slow down"}), (503, {"message": "busy"}))
    sleeps = []
    assert make_broker_for(fake, sleeps).account()["equity"] == 10000.0
    assert len(fake.calls) == 3 and len(sleeps) == 2


def test_get_gives_up_after_three_retries():
    fake = FakeAlpaca()
    fake.queue("GET", "/v2/clock", *[(500, {"message": "down"})] * 10)
    sleeps = []
    with pytest.raises(AlpacaError) as info:
        make_broker_for(fake, sleeps).clock()
    assert info.value.status == 500 and b"down" in info.value.body
    assert len(fake.calls) == 4 and len(sleeps) == 3


def test_post_and_delete_are_never_retried():
    fake = FakeAlpaca()
    fake.queue("POST", "/v2/orders", (503, {"message": "busy"}), (200, {"id": "x"}))
    fake.queue("DELETE", "/v2/positions/AAPL", (500, {"message": "oops"}))
    broker = make_broker_for(fake)
    with pytest.raises(AlpacaError):
        broker.submit_market_order("AAPL", "buy", notional=10)
    with pytest.raises(AlpacaError):
        broker.close_position("AAPL")
    assert len(fake.calls) == 2


def test_network_error_is_wrapped():
    def broken(method, url, headers, body):
        raise urllib.error.URLError("connection refused")

    broker = AlpacaBroker("k", "s", transport=broken, sleep=lambda _s: None)
    with pytest.raises(AlpacaError) as info:
        broker.submit_market_order("AAPL", "buy", notional=5)
    assert info.value.status == 0 and "secret" not in str(info.value)


def test_submit_market_order_payload():
    fake = FakeAlpaca()
    broker = make_broker_for(fake)
    broker.submit_market_order("BTC/USD", "buy", notional=12.349, time_in_force="gtc", client_order_id="abc")
    broker.submit_market_order("AAPL", "sell", qty=0.1234567891234)
    broker.submit_market_order("AAPL", "sell", qty=10.0)
    first, second, third = fake.order_bodies()
    assert first == {"symbol": "BTC/USD", "side": "buy", "type": "market", "time_in_force": "gtc",
                     "notional": "12.34", "client_order_id": "abc"}
    assert second["qty"] == "0.123456789" and "notional" not in second
    assert third["qty"] == "10"
    with pytest.raises(ValueError):
        broker.submit_market_order("AAPL", "buy")
    with pytest.raises(ValueError):
        broker.submit_market_order("AAPL", "buy", notional=5, qty=1)
    with pytest.raises(ValueError):
        broker.submit_market_order("AAPL", "buy", notional=0.001)


def test_close_position_crypto_path():
    fake = FakeAlpaca()
    make_broker_for(fake).close_position("BTC/USD")
    assert fake.calls[0]["method"] == "DELETE"
    assert fake.calls[0]["path"] == "/v2/positions/BTCUSD"


def test_from_env(monkeypatch):
    monkeypatch.delenv("APCA_API_KEY_ID", raising=False)
    monkeypatch.delenv("APCA_API_SECRET_KEY", raising=False)
    with pytest.raises(AlpacaError, match="APCA_API_KEY_ID"):
        AlpacaBroker.from_env(paper=True)
    monkeypatch.setenv("APCA_API_KEY_ID", "k")
    monkeypatch.setenv("APCA_API_SECRET_KEY", "s")
    assert AlpacaBroker.from_env(paper=True).base_url == PAPER_URL


def test_urllib_transport_returns_error_status(monkeypatch):
    def fake_urlopen(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 403, "Forbidden", {}, io.BytesIO(b'{"message":"no"}'))

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    status, body = urllib_transport(5)("GET", PAPER_URL + "/v2/account", {}, None)
    assert status == 403 and json.loads(body) == {"message": "no"}


# --- make_broker ----------------------------------------------------------------

def test_make_broker_modes(monkeypatch):
    monkeypatch.setenv("APCA_API_KEY_ID", "k")
    monkeypatch.setenv("APCA_API_SECRET_KEY", "s")
    monkeypatch.delenv(LIVE_CONFIRM_ENV, raising=False)
    assert make_broker(make_config(mode="paper")) is None
    assert make_broker(make_config(mode="alpaca-paper")).base_url == PAPER_URL
    with pytest.raises(RuntimeError, match=LIVE_CONFIRM_ENV):
        make_broker(make_config(mode="alpaca-live"))
    monkeypatch.setenv(LIVE_CONFIRM_ENV, "yes")
    with pytest.raises(RuntimeError):
        make_broker(make_config(mode="alpaca-live"))
    monkeypatch.setenv(LIVE_CONFIRM_ENV, LIVE_CONFIRM_VALUE)
    assert make_broker(make_config(mode="alpaca-live")).base_url == LIVE_URL


# --- sync_broker -----------------------------------------------------------------

def test_sells_before_buys():
    fake = FakeAlpaca(positions=[position("AAPL", 0.3, 200), position("NVDA", 0.5, 120)])
    targets = {"BTC-USD": 0.5, "ETH-USD": 0.3, "AAPL": 0.0, "NVDA": 0.1}
    report = run(fake, targets, prices={"NVDA": 120.0})
    assert report["ok"], report
    json.dumps(report)  # report is plain data, safe to log
    sides = [o["side"] for o in report["orders"]]
    assert sides == ["sell", "sell", "buy", "buy"]
    trades = fake.trades()
    assert trades[0]["method"] == "DELETE" and trades[0]["path"] == "/v2/positions/AAPL"
    nvda = trades[1]["json"]
    assert nvda["symbol"] == "NVDA" and nvda["side"] == "sell"
    assert float(nvda["qty"]) == pytest.approx((60 - 0.1 * BUDGET) / 120, abs=1e-8)
    buys = {t["json"]["symbol"]: float(t["json"]["notional"]) for t in trades[2:]}
    assert buys == {"BTC/USD": pytest.approx(0.5 * BUDGET, abs=0.01),
                    "ETH/USD": pytest.approx(0.3 * BUDGET, abs=0.01)}
    assert all(t["json"]["time_in_force"] == "gtc" for t in trades[2:])
    assert nvda["time_in_force"] == "day"


def test_rebalance_band_skips_small_adjustments():
    fake = FakeAlpaca(positions=[position("AAPL", 0.335, 200), position("NVDA", 0.67, 100)])
    report = run(fake, {"AAPL": 0.52, "NVDA": 0.3}, prices={"AAPL": 200.0, "NVDA": 100.0})
    assert reasons(report)["AAPL"] == "within rebalance band"
    assert [(o["symbol"], o["side"]) for o in report["orders"]] == [("NVDA", "sell")]


def test_budget_cap_limits_total_buys():
    fake = FakeAlpaca()  # $10,000 in the account, but capital_gbp=100
    report = run(fake, {"AAPL": 1.0, "NVDA": 1.0, "BTC-USD": 1.0, "ETH-USD": 0.4})
    assert report["budget_usd"] == pytest.approx(BUDGET)
    spent = sum(float(body["notional"]) for body in fake.order_bodies())
    assert 0 < spent <= BUDGET + 1e-9
    assert "budget exhausted" in reasons(report).values()


def test_budget_counts_existing_positions():
    fake = FakeAlpaca(positions=[position("TSLA", 0.5, 200)])  # $100 already deployed, not targeted
    run(fake, {"AAPL": 1.0})
    assert float(fake.order_bodies()[0]["notional"]) == pytest.approx(BUDGET - 100, abs=0.01)


def test_buys_limited_by_cash():
    fake = FakeAlpaca(account={"equity": "200", "cash": "30", "buying_power": "60",
                               "non_marginable_buying_power": "30"})
    run(fake, {"BTC-USD": 1.0})
    assert fake.order_bodies()[0]["notional"] == "30.00"


def test_market_closed_skips_stocks_but_trades_crypto():
    fake = FakeAlpaca(positions=[position("NVDA", 1, 50)], is_open=False)
    report = run(fake, {"AAPL": 0.5, "NVDA": 0.0, "BTC-USD": 0.4})
    assert reasons(report) == {"AAPL": "market closed", "NVDA": "market closed"}
    bodies = fake.order_bodies()
    assert [(b["symbol"], b["time_in_force"]) for b in bodies] == [("BTC/USD", "gtc")]
    assert not any(c["method"] == "DELETE" for c in fake.calls)


def test_trade_flags_respected():
    fake = FakeAlpaca()
    report = run(fake, {"AAPL": 0.3, "BTC-USD": 0.3}, config=make_config(trade_crypto=False))
    assert reasons(report) == {"BTC-USD": "crypto trading disabled"}
    report = run(FakeAlpaca(), {"AAPL": 0.3}, config=make_config(trade_stocks=False))
    assert reasons(report) == {"AAPL": "stock trading disabled"}


def test_open_orders_are_not_duplicated():
    fake = FakeAlpaca(open_orders=[{"symbol": "AAPL", "status": "new"},
                                   {"symbol": "BTCUSD", "status": "accepted", "asset_class": "crypto"}])
    report = run(fake, {"AAPL": 0.3, "BTC-USD": 0.3, "ETH-USD": 0.3})
    assert reasons(report) == {"AAPL": "open order pending", "BTC-USD": "open order pending"}
    assert [b["symbol"] for b in fake.order_bodies()] == ["ETH/USD"]


def test_pdt_guard_blocks_stock_buys_only():
    fake = FakeAlpaca(account={"equity": "20000", "daytrade_count": "3"},
                      positions=[position("TSLA", 0.5, 200)])
    report = run(fake, {"AAPL": 0.5, "TSLA": 0.0, "BTC-USD": 0.3})
    assert reasons(report) == {"AAPL": "PDT guard"}
    assert [(o["symbol"], o["side"]) for o in report["orders"]] == [("TSLA", "sell"), ("BTC-USD", "buy")]


def test_pdt_guard_off_above_threshold():
    fake = FakeAlpaca(account={"equity": "30000", "daytrade_count": "5"})
    report = run(fake, {"AAPL": 0.5})
    assert report["skipped"] == [] and len(report["orders"]) == 1


def test_order_errors_are_captured():
    fake = FakeAlpaca()
    fake.reject["BTC/USD"] = (403, "insufficient balance for USD")
    report = run(fake, {"BTC-USD": 0.5, "AAPL": 0.4})
    assert report["ok"] is False
    assert report["errors"][0]["symbol"] == "BTC-USD"
    assert "insufficient balance" in report["errors"][0]["error"]
    assert [o["symbol"] for o in report["orders"]] == ["AAPL"]


def test_duplicate_client_order_id_is_skipped_not_error():
    fake = FakeAlpaca()
    fake.reject["AAPL"] = (422, "client_order_id must be unique")
    report = run(fake, {"AAPL": 0.5})
    assert report["ok"] and reasons(report) == {"AAPL": "already submitted for this bar"}


def test_fetch_failure_returns_not_ok():
    fake = FakeAlpaca()
    fake.queue("GET", "/v2/account", *[(500, {"message": "down"})] * 4)
    report = run(fake, {"AAPL": 0.5}, sleeps=[])
    assert report["ok"] is False and "down" in report["error"]
    assert fake.trades() == []


def test_blocked_account_places_no_orders():
    fake = FakeAlpaca(account={"trading_blocked": True})
    report = run(fake, {"AAPL": 0.5, "BTC-USD": 0.5})
    assert report["ok"] is False and "blocked" in report["error"]
    assert fake.trades() == []


def test_unknown_and_uk_symbols_skipped():
    report = run(FakeAlpaca(), {"VUSA.L": 0.5, "FOO": 0.2})
    assert reasons(report) == {"VUSA.L": "not tradable on Alpaca", "FOO": "not in universe"}
    assert report["orders"] == []


def test_order_cap():
    fake = FakeAlpaca()
    report = run(fake, {"AAPL": 0.2, "NVDA": 0.2, "BTC-USD": 0.2, "ETH-USD": 0.2},
                 config=make_config(max_orders_per_tick=2))
    assert len(fake.trades()) == 2
    assert list(reasons(report).values()).count("order cap reached") == 2


def test_small_buys_below_minimum_skipped():
    report = run(FakeAlpaca(), {"AAPL": 0.005})  # $0.67 < max($1, £1)
    assert reasons(report) == {"AAPL": "below minimum trade"}


def test_client_order_id_sanitised():
    assert client_order_id("BTC-USD", "buy", STAMP) == "agent-BTC-USD-buy-2026-09-24T1505000000"
    assert client_order_id("VUSA.L", "sell", "2026/09/24 15:05") == "agent-VUSAL-sell-202609241505"
    long_a = client_order_id("DOGE-USD", "sell", "2026-09-24 15:05:00.123456789+00:00 extra-label")
    long_b = client_order_id("DOGE-USD", "sell", "2026-09-24 15:10:00.123456789+00:00 extra-label")
    for value in (long_a, long_b):
        assert len(value) <= 48 and re.fullmatch(r"[A-Za-z0-9_-]+", value)
    assert long_a != long_b


def test_submitted_orders_carry_client_order_id():
    fake = FakeAlpaca()
    run(fake, {"BTC-USD": 0.5, "AAPL": 0.3})
    ids = [body["client_order_id"] for body in fake.order_bodies()]
    assert ids == ["agent-BTC-USD-buy-2026-09-24T1505000000", "agent-AAPL-buy-2026-09-24T1505000000"]
    assert all(len(i) <= 48 and re.fullmatch(r"[A-Za-z0-9_-]+", i) for i in ids)
