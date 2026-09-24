"""Mirror the Agent sleeve's target weights into an Alpaca account.

Real-money trading needs both ``broker.mode = "alpaca-live"`` and
``AGENT_LIVE_CONFIRM=I-ACCEPT-REAL-MONEY-RISK``. Whatever the account holds,
at most ``broker.capital_gbp`` (converted to USD) is ever deployed.
"""
from __future__ import annotations

import hashlib
import math
import os
import re

import pandas as pd

from .brokers.alpaca import AlpacaBroker, AlpacaError

LIVE_CONFIRM_ENV = "AGENT_LIVE_CONFIRM"
LIVE_CONFIRM_VALUE = "I-ACCEPT-REAL-MONEY-RISK"
PDT_EQUITY_USD = 25_000.0
PDT_MAX_DAY_TRADES = 3
_MAX_CLIENT_ID = 48


def make_broker(config) -> AlpacaBroker | None:
    mode = config.broker.mode
    if mode == "paper":
        return None
    if mode == "alpaca-paper":
        return AlpacaBroker.from_env(paper=True)
    if mode == "alpaca-live":
        if os.environ.get(LIVE_CONFIRM_ENV) != LIVE_CONFIRM_VALUE:
            raise RuntimeError(
                f"Refusing real-money trading: broker mode is 'alpaca-live' but "
                f"{LIVE_CONFIRM_ENV} is not set to {LIVE_CONFIRM_VALUE!r}"
            )
        return AlpacaBroker.from_env(paper=False)
    raise ValueError(f"Unknown broker mode {mode!r}")


def client_order_id(symbol: str, side: str, bar_stamp: str) -> str:
    """Deterministic per bar, so Alpaca rejects a resubmission of the same order."""
    raw = f"agent-{symbol}-{side}-{bar_stamp}"
    clean = re.sub(r"[^A-Za-z0-9_-]", "", raw)
    if len(clean) <= _MAX_CLIENT_ID:
        return clean
    # Truncating would drop the bar stamp and collide across bars; keep a digest instead.
    digest = hashlib.sha1(raw.encode()).hexdigest()[:10]
    return f"{clean[:_MAX_CLIENT_ID - 11]}-{digest}"


def _key(symbol: str) -> str:
    return symbol.replace("/", "").upper()


def _is_duplicate(exc: Exception) -> bool:
    return isinstance(exc, AlpacaError) and exc.status == 422 and "client_order_id" in str(exc)


def _available_cash(account: dict) -> float:
    fields = ("cash", "buying_power", "non_marginable_buying_power")
    values = [float(account[key]) for key in fields if account.get(key) is not None]
    return max(0.0, min(values)) if values else 0.0


def sync_broker(
    broker,
    targets: dict[str, float],
    config,
    now: pd.Timestamp,
    prices_usd: dict[str, float],
    gbpusd: float,
    bar_stamp: str,
) -> dict:
    settings = config.broker
    report = {
        "ok": False,
        "mode": settings.mode,
        "time": now.isoformat() if hasattr(now, "isoformat") else str(now),
        "equity_usd": None,
        "cash_usd": None,
        "budget_usd": 0.0,
        "market_open": None,
        "orders": [],
        "skipped": [],
        "errors": [],
        "positions": {},
        "error": None,
    }
    skipped, errors, orders = report["skipped"], report["errors"], report["orders"]

    try:
        account = broker.account()
        clock = broker.clock()
        positions = broker.positions()
        pending = {_key(str(order.get("symbol", ""))) for order in broker.open_orders()}
    except Exception as exc:  # noqa: BLE001 - a broker outage must not stop the engine
        report["error"] = f"{type(exc).__name__}: {exc}"
        return report

    if not isinstance(gbpusd, (int, float)) or not math.isfinite(gbpusd) or gbpusd <= 0:
        gbpusd = config.gbpusd_fallback
    equity = float(account.get("equity") or 0.0)
    cash = _available_cash(account)
    budget = max(0.0, min(equity, settings.capital_gbp * gbpusd))
    market_open = bool(clock.get("is_open"))
    report.update(equity_usd=equity, cash_usd=cash, budget_usd=budget, market_open=market_open, positions=positions)

    if account.get("trading_blocked") or account.get("account_blocked") or account.get("trade_suspended_by_user"):
        report["error"] = "Alpaca account is blocked from trading"
        return report

    min_trade = max(1.0, config.risk.min_trade_gbp * gbpusd)
    band = config.risk.rebalance_band * budget
    pdt_guard = equity < PDT_EQUITY_USD and int(account.get("daytrade_count") or 0) >= PDT_MAX_DAY_TRADES
    held = {_key(symbol): pos for symbol, pos in positions.items()}
    universe = {_key(asset.alpaca) for asset in config.universe if asset.kind != "uk_equity"}
    deployed = sum(max(0.0, pos["market_value"]) for key, pos in held.items() if key in universe)

    sells: list[dict] = []
    buys: list[dict] = []
    for symbol, weight in targets.items():
        try:
            asset = config.asset(symbol)
        except KeyError:
            skipped.append({"symbol": symbol, "reason": "not in universe"})
            continue
        try:
            weight = float(weight)
        except (TypeError, ValueError):
            weight = math.nan
        if not math.isfinite(weight):
            skipped.append({"symbol": symbol, "reason": "invalid target weight"})
            continue
        weight = min(max(weight, 0.0), 1.0)
        if asset.kind == "uk_equity":
            if weight > 0:
                skipped.append({"symbol": symbol, "reason": "not tradable on Alpaca"})
            continue

        pos = held.get(_key(asset.alpaca))
        qty = pos["qty"] if pos else 0.0
        if qty < 0:
            skipped.append({"symbol": symbol, "reason": "short position not managed"})
            continue
        current = max(0.0, pos["market_value"]) if pos and qty > 0 else 0.0
        target = weight * budget
        diff = target - current
        if qty > 0 and target <= 0:
            action = {"action": "close", "side": "sell", "value": current}
        elif qty > 0 and abs(diff) < band:
            skipped.append({"symbol": symbol, "reason": "within rebalance band"})
            continue
        elif diff < 0:
            action = {"action": "sell", "side": "sell", "value": -diff}
        elif diff > 0:
            action = {"action": "buy", "side": "buy", "value": diff}
        else:
            continue

        stock = asset.kind != "crypto"
        reason = None
        if stock and not settings.trade_stocks:
            reason = "stock trading disabled"
        elif stock and not market_open:
            reason = "market closed"
        elif not stock and not settings.trade_crypto:
            reason = "crypto trading disabled"
        elif _key(asset.alpaca) in pending:
            reason = "open order pending"
        elif action["side"] == "buy" and stock and pdt_guard:
            reason = "PDT guard"
        elif action["action"] != "close" and action["value"] < min_trade:
            reason = "below minimum trade"
        if reason:
            skipped.append({"symbol": symbol, "reason": reason})
            continue

        if action["action"] == "sell":
            price = _positive((prices_usd or {}).get(symbol)) or (pos["current_price"] if pos else 0.0)
            if price <= 0:
                skipped.append({"symbol": symbol, "reason": "no price"})
                continue
            sell_qty = action["value"] / price
            if sell_qty >= pos["qty_available"]:
                action.update(action="close", value=current)
            else:
                action["qty"] = sell_qty
        if action["action"] == "close":
            action["qty"] = qty
        action.update(symbol=symbol, asset=asset)
        (buys if action["side"] == "buy" else sells).append(action)

    count = 0

    def submit(action: dict, **size) -> dict | None:
        nonlocal count
        symbol, asset, side = action["symbol"], action["asset"], action["side"]
        if count >= settings.max_orders_per_tick:
            skipped.append({"symbol": symbol, "reason": "order cap reached"})
            return None
        count += 1
        order_id = client_order_id(symbol, side, bar_stamp)
        try:
            if action["action"] == "close":
                response = broker.close_position(asset.alpaca)
            else:
                response = broker.submit_market_order(
                    asset.alpaca,
                    side,
                    time_in_force="gtc" if asset.kind == "crypto" else "day",
                    client_order_id=order_id,
                    **size,
                )
        except Exception as exc:  # noqa: BLE001 - record and carry on with other symbols
            if _is_duplicate(exc):
                skipped.append({"symbol": symbol, "reason": "already submitted for this bar"})
            else:
                errors.append({"symbol": symbol, "error": f"{type(exc).__name__}: {exc}"})
            return None
        response = response if isinstance(response, dict) else {}
        orders.append({
            "symbol": symbol,
            "broker_symbol": asset.alpaca,
            "action": action["action"],
            "side": side,
            **size,
            "status": response.get("status"),
            "id": response.get("id"),
            "client_order_id": response.get("client_order_id") or (None if action["action"] == "close" else order_id),
        })
        return response

    headroom = budget - deployed
    for action in sorted(sells, key=lambda item: -item["value"]):
        if submit(action, qty=action["qty"]) is not None:
            headroom += action["value"]

    for action in sorted(buys, key=lambda item: -item["value"]):
        notional = min(action["value"], cash, headroom)
        if notional < min_trade:
            reason = "insufficient cash" if cash < min(action["value"], headroom) else "budget exhausted"
            skipped.append({"symbol": action["symbol"], "reason": reason})
            continue
        notional = math.floor(notional * 100) / 100
        if submit(action, notional=notional) is not None:
            cash -= notional
            headroom -= notional

    report["ok"] = not errors
    return report


def _positive(value) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return 0.0
    return result if math.isfinite(result) and result > 0 else 0.0
