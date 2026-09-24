"""Minimal stdlib client for the Alpaca Trading API v2.

Only what the agent needs: account, clock, positions, open orders, market
orders and position closes. Credentials come from the environment and are
never included in error messages.
"""
from __future__ import annotations

import http.client
import json
import math
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from decimal import ROUND_DOWN, Decimal
from typing import Callable

PAPER_URL = "https://paper-api.alpaca.markets"
LIVE_URL = "https://api.alpaca.markets"
KEY_ENV = "APCA_API_KEY_ID"
SECRET_ENV = "APCA_API_SECRET_KEY"

_CRYPTO_QUOTES = ("USDT", "USDC", "USD")
_ACCOUNT_FLOATS = ("equity", "cash", "buying_power", "non_marginable_buying_power", "last_equity")
_POSITION_FLOATS = ("market_value", "avg_entry_price", "current_price", "unrealized_pl")

Transport = Callable[[str, str, dict, "bytes | None"], "tuple[int, bytes]"]


class AlpacaError(RuntimeError):
    def __init__(self, message: str, status: int | None = None, body: bytes | None = None):
        super().__init__(message)
        self.status = status
        self.body = body


def urllib_transport(timeout: float = 20) -> Transport:
    """HTTP transport that returns error statuses instead of raising."""

    def transport(method: str, url: str, headers: dict, body: bytes | None) -> tuple[int, bytes]:
        request = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.status, response.read()
        except urllib.error.HTTPError as exc:
            return exc.code, exc.read() or b""

    return transport


def normalise_symbol(symbol: str, asset_class: str = "") -> str:
    """Positions report crypto as "BTCUSD"; orders use "BTC/USD"."""
    if asset_class == "crypto" and "/" not in symbol:
        for quote in _CRYPTO_QUOTES:
            if symbol.endswith(quote) and len(symbol) > len(quote):
                return f"{symbol[:-len(quote)]}/{quote}"
    return symbol


def _float(value, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _decimal(value: float, places: int) -> str:
    # Round down so an order never exceeds the cash or quantity it was sized from.
    if value is None or not math.isfinite(value) or value <= 0:
        raise ValueError(f"order size must be a positive number, got {value!r}")
    amount = Decimal(repr(float(value))).quantize(Decimal(1).scaleb(-places), rounding=ROUND_DOWN)
    if amount <= 0:
        raise ValueError(f"order size {value!r} rounds to zero")
    return format(amount, "f")


def _error_message(raw: bytes) -> str:
    try:
        data = json.loads(raw)
        if isinstance(data, dict) and data.get("message"):
            return str(data["message"])
    except (ValueError, TypeError):
        pass
    return raw.decode("utf-8", "replace").strip()[:300] or "no response body"


class AlpacaBroker:
    def __init__(
        self,
        key_id: str,
        secret_key: str,
        paper: bool = True,
        transport: Transport | None = None,
        timeout: float = 20,
        sleep: Callable[[float], None] = time.sleep,
        retries: int = 3,
        backoff: float = 0.5,
    ):
        self.paper = paper
        self.base_url = PAPER_URL if paper else LIVE_URL
        self._headers = {
            "APCA-API-KEY-ID": key_id,
            "APCA-API-SECRET-KEY": secret_key,
            "Accept": "application/json",
            "User-Agent": "trader-agent",
        }
        self._transport = transport or urllib_transport(timeout)
        self._sleep = sleep
        self.retries = retries
        self.backoff = backoff

    def __repr__(self) -> str:
        return f"AlpacaBroker(paper={self.paper})"

    @classmethod
    def from_env(cls, paper: bool, **kwargs) -> "AlpacaBroker":
        key = os.environ.get(KEY_ENV, "").strip()
        secret = os.environ.get(SECRET_ENV, "").strip()
        missing = [name for name, value in ((KEY_ENV, key), (SECRET_ENV, secret)) if not value]
        if missing:
            account = "paper" if paper else "LIVE"
            raise AlpacaError(f"Alpaca {account} credentials missing: set {' and '.join(missing)}")
        return cls(key, secret, paper=paper, **kwargs)

    def _request(self, method: str, path: str, params: dict | None = None, payload: dict | None = None):
        url = self.base_url + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        headers = dict(self._headers)
        body = None
        if payload is not None:
            body = json.dumps(payload).encode()
            headers["Content-Type"] = "application/json"
        # Orders are never retried automatically: a lost response may still have placed one.
        attempts = 1 + (max(0, self.retries) if method == "GET" else 0)
        for attempt in range(attempts):
            try:
                status, raw = self._transport(method, url, headers, body)
            except (OSError, http.client.HTTPException) as exc:
                status, raw = 0, f"{type(exc).__name__}: {exc}".encode()
            retryable = status == 0 or status == 429 or status >= 500
            if not retryable or attempt == attempts - 1:
                break
            self._sleep(self.backoff * 2**attempt)
        if not 200 <= status < 300:
            raise AlpacaError(f"Alpaca {method} {path} failed ({status}): {_error_message(raw)}", status, raw)
        if not raw or not raw.strip():
            return {}
        try:
            return json.loads(raw)
        except ValueError as exc:
            raise AlpacaError(f"Alpaca {method} {path} returned invalid JSON", status, raw) from exc

    def account(self) -> dict:
        data = self._request("GET", "/v2/account")
        for key in _ACCOUNT_FLOATS:
            if key in data:
                data[key] = _float(data[key])
        data["daytrade_count"] = int(_float(data.get("daytrade_count")))
        return data

    def clock(self) -> dict:
        return self._request("GET", "/v2/clock")

    def positions(self) -> dict[str, dict]:
        out: dict[str, dict] = {}
        for item in self._request("GET", "/v2/positions") or []:
            asset_class = str(item.get("asset_class", ""))
            symbol = normalise_symbol(str(item.get("symbol", "")), asset_class)
            qty = _float(item.get("qty"))
            out[symbol] = {
                "symbol": symbol,
                "qty": qty,
                "qty_available": _float(item.get("qty_available"), qty),
                **{key: _float(item.get(key)) for key in _POSITION_FLOATS},
                "asset_class": asset_class,
            }
        return out

    def open_orders(self) -> list[dict]:
        return list(self._request("GET", "/v2/orders", {"status": "open", "limit": 500}) or [])

    def submit_market_order(
        self,
        symbol: str,
        side: str,
        notional: float | None = None,
        qty: float | None = None,
        time_in_force: str = "day",
        client_order_id: str | None = None,
    ) -> dict:
        if side not in ("buy", "sell"):
            raise ValueError(f"side must be 'buy' or 'sell', got {side!r}")
        if (notional is None) == (qty is None):
            raise ValueError("pass exactly one of notional or qty")
        payload = {"symbol": symbol, "side": side, "type": "market", "time_in_force": time_in_force}
        if notional is not None:
            payload["notional"] = _decimal(notional, 2)
        else:
            payload["qty"] = _decimal(qty, 9).rstrip("0").rstrip(".")
        if client_order_id:
            payload["client_order_id"] = client_order_id
        return self._request("POST", "/v2/orders", payload=payload)

    def close_position(self, symbol: str) -> dict:
        path = "/v2/positions/" + urllib.parse.quote(symbol.replace("/", ""), safe="")
        return self._request("DELETE", path)
