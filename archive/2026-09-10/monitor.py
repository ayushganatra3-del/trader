#!/usr/bin/env python3
"""One-day virtual ETF journal. No broker, credentials, or real order interface."""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import tempfile
import urllib.error
import urllib.request

UTC = dt.timezone.utc
SESSION_DAY = "2026-09-10"
SYMBOLS = ("ISF.L", "VUSA.L", "EQQQ.L")
START_CASH = 100.0
BUY_BUDGET = 40.0
COST_RATE = 0.001
MAX_POSITIONS = 2
MAX_BUYS = 6
MAX_AGE_SECONDS = 25 * 60
BAR_SECONDS = 300
BASE = Path(__file__).resolve().parent


def stamp(value):
    return value.astimezone(UTC).isoformat(timespec="microseconds").replace("+00:00", "Z")


def instant(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)


def boundary(hour, minute=0):
    return instant(f"{SESSION_DAY}T{hour:02}:{minute:02}:00Z")


def number(value, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Missing or nonnumeric market data")
    if not math.isfinite(value) or (value <= 0 if positive else value < 0):
        raise ValueError("Invalid market data value")
    return float(value)


def parse_snapshot(symbol, payload, observed_at, source="injected offline fixture", allow_stale_reconciliation=False):
    """Validate one read-only Yahoo chart observation; prices returned in GBP."""
    if observed_at.date().isoformat() != SESSION_DAY:
        raise ValueError("Observation is outside the fixed session day")
    chart = payload.get("chart", {})
    if chart.get("error") or not chart.get("result"):
        raise ValueError("Provider returned no valid chart")
    result = chart["result"][0]
    meta = result.get("meta", {})
    if meta.get("symbol") != symbol:
        raise ValueError("Provider symbol does not match request")
    if meta.get("dataGranularity", "5m") != "5m":
        raise ValueError("Provider data granularity is not five minutes")
    currency = meta.get("currency")
    if currency not in ("GBp", "GBX", "GBP"):
        raise ValueError(f"Unsupported or ambiguous price currency: {currency!r}")
    scale = 0.01 if currency in ("GBp", "GBX") else 1.0
    market_time = meta.get("regularMarketTime")
    if market_time is None:
        raise ValueError("Provider market time is required to verify delayed bar completion")
    if market_time is not None:
        market_time = number(market_time, positive=True)
        if market_time > observed_at.timestamp():
            raise ValueError("Provider market timestamp is in the future")
        if dt.datetime.fromtimestamp(market_time, UTC).date().isoformat() != SESSION_DAY:
            raise ValueError("Provider market timestamp is not today's session")
    timestamps = result.get("timestamp") or []
    indicators = result.get("indicators", {}).get("quote") or []
    if not indicators:
        raise ValueError("No OHLCV quotes")
    data = indicators[0]
    if any(len(data.get(key, [])) != len(timestamps) for key in ("open", "high", "low", "close", "volume")):
        raise ValueError("OHLCV arrays do not align")
    bars = []
    seen = set()
    for index, raw_time in enumerate(timestamps):
        start = number(raw_time, positive=True)
        if start > observed_at.timestamp():
            raise ValueError("Provider contains a future bar")
        bar_date = dt.datetime.fromtimestamp(start, UTC)
        if bar_date.date().isoformat() != SESSION_DAY:
            continue
        if not boundary(7).timestamp() <= start < boundary(15, 30).timestamp():
            continue
        if start % BAR_SECONDS != 0:
            continue  # Yahoo may append a current trade row at an irregular time.
        if start in seen:
            raise ValueError("Duplicate provider bar timestamp")
        seen.add(start)
        if start + BAR_SECONDS > min(observed_at.timestamp(), market_time):
            continue  # The current, unfinished bar can never signal or fill.
        try:
            values = {key: number(data[key][index], positive=True) * scale for key in ("open", "high", "low", "close")}
            values["volume"] = number(data["volume"][index])
        except ValueError as error:
            raise ValueError(f"Invalid completed bar at {bar_date.isoformat()}: {error}") from error
        if not values["low"] <= min(values["open"], values["close"]) <= max(values["open"], values["close"]) <= values["high"]:
            raise ValueError("Inconsistent OHLC range")
        bars.append(dict(start=start, end=start + BAR_SECONDS, **values))
    bars.sort(key=lambda bar: bar["start"])
    if not bars:
        raise ValueError("No complete bars from today's regular session")
    age = observed_at.timestamp() - bars[-1]["end"]
    if age < 0 or (age > MAX_AGE_SECONDS and not allow_stale_reconciliation):
        raise ValueError(f"Latest completed bar is stale ({age / 60:.1f} minutes after bar end)")
    total_volume = sum(bar["volume"] for bar in bars)
    if total_volume <= 0:
        raise ValueError("No positive session trading volume for VWAP")
    vwap = sum(((bar["high"] + bar["low"] + bar["close"]) / 3) * bar["volume"] for bar in bars) / total_volume
    # A 20-minute rule requires contiguous recent five-minute observations.
    contiguous = len(bars) >= 6 and all(bars[-offset]["start"] - bars[-offset - 1]["start"] == BAR_SECONDS for offset in range(1, 5))
    momentum = bars[-1]["close"] / bars[-5]["close"] - 1 if contiguous else None
    return {"symbol": symbol, "currency": currency, "scale_to_gbp": scale,
            "observed_at": stamp(observed_at), "source": source, "bars": bars,
            "age_seconds": age, "fresh": age <= MAX_AGE_SECONDS, "vwap": vwap, "momentum_20m": momentum,
            "latest_start": stamp(dt.datetime.fromtimestamp(bars[-1]["start"], UTC)),
            "latest_end": stamp(dt.datetime.fromtimestamp(bars[-1]["end"], UTC)),
            "close": bars[-1]["close"]}


def initial_state(now):
    return {"version": 1, "session_day": SESSION_DAY, "created_at": stamp(now),
            "status": "active", "starting_cash_gbp": START_CASH, "cash_gbp": START_CASH,
            "realised_gbp": 0.0, "positions": {}, "intents": [], "events": [],
            "next_id": 1, "buy_fills": 0, "halted": False, "halt_reason": None,
            "stopped_assets": [], "cooldowns": {}, "quotes": {}, "last_check_at": None,
            "rules": {"symbols": list(SYMBOLS), "buy_budget_gbp": BUY_BUDGET,
                      "max_positions": MAX_POSITIONS, "max_buy_fills": MAX_BUYS,
                      "per_fill_cost_bps": 10, "session_loss_halt_gbp": 3,
                      "no_entries_after_utc": "14:45", "exit_queue_utc": "15:15",
                      "regular_close_utc": "15:30", "final_reconciliation_utc": "16:00"}}


def add_event(state, kind, now, **fields):
    event = {"event_id": f"event-{len(state['events']) + 1:06d}", "type": kind,
             "recorded_at": stamp(now), **fields}
    state["events"].append(event)
    return event


def pending(state, side=None):
    return [intent for intent in state["intents"] if intent["status"] == "pending" and (side is None or intent["side"] == side)]


def reserved_cash(state):
    return sum(intent["budget_gbp"] for intent in pending(state, "buy"))


def totals(state):
    market_value = sum(position["quantity"] * position["mark_gbp"] for position in state["positions"].values())
    open_cost = sum(position["cost_basis_gbp"] for position in state["positions"].values())
    equity = state["cash_gbp"] + market_value
    return {"cash_gbp": state["cash_gbp"], "reserved_gbp": reserved_cash(state),
            "available_gbp": state["cash_gbp"] - reserved_cash(state),
            "holdings_gbp": market_value, "equity_gbp": equity,
            "realised_gbp": state["realised_gbp"], "unrealised_gbp": market_value - open_cost,
            "total_pl_gbp": equity - START_CASH}


def assert_accounting(state):
    summary = totals(state)
    if state["cash_gbp"] < -1e-8 or summary["available_gbp"] < -1e-8:
        raise ValueError("Cash or reservation reconciliation failed")
    if len(state["positions"]) + len(pending(state, "buy")) > MAX_POSITIONS:
        raise ValueError("Position limit failed")
    if abs(summary["realised_gbp"] + summary["unrealised_gbp"] - summary["total_pl_gbp"]) > 1e-7:
        raise ValueError("Profit reconciliation failed")
    ledger_cash = START_CASH
    for event in state["events"]:
        if event["type"] == "fill":
            ledger_cash += event["cash_change_gbp"]
    if abs(ledger_cash - state["cash_gbp"]) > 1e-7:
        raise ValueError("Fill ledger does not reconcile to cash")
    if state["buy_fills"] > MAX_BUYS:
        raise ValueError("Daily buy limit failed")


def decide(state, symbol, side, now, reason, quote=None):
    if any(intent["symbol"] == symbol and intent["side"] == side for intent in pending(state)):
        return
    intent = {"intent_id": f"{SESSION_DAY}-{state['next_id']:04d}", "symbol": symbol,
              "side": side, "status": "pending", "decision_at": stamp(now), "reason": reason}
    state["next_id"] += 1
    if side == "buy":
        intent["budget_gbp"] = BUY_BUDGET
    if quote:
        intent.update(signal_close_gbp=quote["close"], signal_vwap_gbp=quote["vwap"],
                      signal_bar_start=quote["latest_start"], observation_source=quote["source"])
    state["intents"].append(intent)
    add_event(state, "decision", now, **intent)


def cancel_buys(state, now, reason):
    for intent in pending(state, "buy"):
        intent.update(status="cancelled", cancelled_at=stamp(now), cancellation_reason=reason)
        add_event(state, "cancelled", now, intent_id=intent["intent_id"], symbol=intent["symbol"], reason=reason)


def recognise_fills(state, quotes, now):
    for intent in pending(state):
        quote = quotes.get(intent["symbol"])
        if not quote:
            continue
        decision_time = instant(intent["decision_at"]).timestamp()
        # A previously persisted intent is mandatory. The decision's observed wall
        # clock time excludes all price bars that had already started at decision.
        candidates = [bar for bar in quote["bars"] if bar["start"] >= decision_time and bar["start"] < boundary(15, 30).timestamp() and (intent["side"] == "sell" or bar["start"] < boundary(14, 45).timestamp())]
        if not candidates:
            continue
        bar = candidates[0]
        raw_price = bar["open"]
        execution_price = raw_price * (1 + COST_RATE if intent["side"] == "buy" else 1 - COST_RATE)
        fill_at = stamp(dt.datetime.fromtimestamp(bar["start"], UTC))
        if intent["side"] == "buy":
            if state["halted"] or intent["symbol"] in state["positions"]:
                raise ValueError("Invalid pending buy in halted or occupied state")
            budget = intent["budget_gbp"]
            if state["cash_gbp"] + 1e-8 < budget or len(state["positions"]) >= MAX_POSITIONS:
                raise ValueError("Pending buy exceeds cash or position limits")
            quantity = budget / execution_price
            change = -budget
            realised = 0.0
            state["cash_gbp"] -= budget
            state["buy_fills"] += 1
            state["positions"][intent["symbol"]] = {
                "symbol": intent["symbol"], "quantity": quantity, "cost_basis_gbp": budget,
                "entry_reference_gbp": raw_price, "entry_execution_gbp": execution_price,
                "entry_at": fill_at, "entry_recognised_at": stamp(now),
                "entry_intent_id": intent["intent_id"], "mark_gbp": quote["close"],
                "mark_bar_end": quote["latest_end"], "mark_observed_at": quote["observed_at"]}
        else:
            position = state["positions"].get(intent["symbol"])
            if position is None:
                raise ValueError("Pending sell has no virtual holding")
            quantity = position["quantity"]
            change = quantity * execution_price
            realised = change - position["cost_basis_gbp"]
            state["cash_gbp"] += change
            state["realised_gbp"] += realised
            del state["positions"][intent["symbol"]]
            state["cooldowns"][intent["symbol"]] = stamp(now + dt.timedelta(minutes=30))
        intent.update(status="filled", effective_fill_at=fill_at, recognised_at=stamp(now))
        add_event(state, "fill", now, intent_id=intent["intent_id"], symbol=intent["symbol"],
                  side=intent["side"], reason=intent["reason"], decision_at=intent["decision_at"],
                  effective_fill_at=fill_at, recognised_at=stamp(now), raw_open_gbp=raw_price,
                  execution_price_gbp=execution_price, quantity=quantity,
                  adverse_cost_gbp=quantity * raw_price * COST_RATE,
                  cash_change_gbp=change, realised_gbp=realised,
                  observed_at=quote["observed_at"], source=quote["source"],
                  fill_bar_end=stamp(dt.datetime.fromtimestamp(bar["end"], UTC)))


def step(state, quotes, errors, now):
    """Advance using validated observed snapshots. Inject snapshots/time in tests."""
    if state.get("session_day") != SESSION_DAY:
        raise ValueError("State belongs to a different session; it will not be reset")
    if state["status"] in ("complete", "incomplete") or now.date().isoformat() != SESSION_DAY:
        return {"status": state["status"], "new_fills": [], "alerts": ["Session is closed; no actions taken"], **totals(state)}
    if state.get("last_check_at") and now < instant(state["last_check_at"]):
        raise ValueError("Wall clock moved backwards; refusing to replay a check")
    # A caller cannot pass pre-parsed old observations as if they were current.
    for symbol, quote in quotes.items():
        if symbol not in SYMBOLS or quote["symbol"] != symbol:
            raise ValueError("Unapproved symbol")
        if instant(quote["observed_at"]) > now:
            raise ValueError("Quote observation is in the future")
    fresh_quotes = {symbol: quote for symbol, quote in quotes.items() if now.timestamp() - quote["bars"][-1]["end"] <= MAX_AGE_SECONDS}
    event_start = len(state["events"])
    state["last_check_at"] = stamp(now)
    for symbol in SYMBOLS:
        quote = quotes.get(symbol)
        if quote:
            state["quotes"][symbol] = {key: quote[key] for key in ("observed_at", "source", "currency", "scale_to_gbp", "age_seconds", "latest_start", "latest_end", "close", "vwap", "momentum_20m")}
            state["quotes"][symbol]["status"] = "valid" if symbol in fresh_quotes else "stale — existing-intent reconciliation only"
        else:
            previous = state["quotes"].get(symbol, {})
            state["quotes"][symbol] = {**previous, "status": "unavailable", "last_error_at": stamp(now), "error": errors.get(symbol, "No observation")}
    recognise_fills(state, quotes, now)
    for symbol, position in state["positions"].items():
        if symbol in fresh_quotes:
            quote = fresh_quotes[symbol]
            position.update(mark_gbp=quote["close"], mark_bar_end=quote["latest_end"], mark_observed_at=quote["observed_at"])
    summary = totals(state)
    if summary["total_pl_gbp"] <= -3 and not state["halted"]:
        state.update(halted=True, halt_reason="Session net equity loss reached £3")
        add_event(state, "halt", now, reason=state["halt_reason"], equity_gbp=summary["equity_gbp"])
    if state["halted"]:
        cancel_buys(state, now, state["halt_reason"])
    if now >= boundary(14, 45):
        cancel_buys(state, now, "No further entry fills at or after 15:45 BST")
    # End-of-day reconciliation may recognise existing legitimate orders; it
    # must never invent a close using a candle predating the exit decision.
    final = now >= boundary(16)
    if not final:
        for symbol, position in list(state["positions"].items()):
            quote = fresh_quotes.get(symbol)
            reason = None
            if state["halted"]:
                reason = state["halt_reason"]
            elif now >= boundary(15, 15):
                reason = "Scheduled 16:15 BST close"
            elif quote:
                if quote["close"] <= position["entry_reference_gbp"] * 0.99:
                    reason = "1% stop signal"
                    if symbol not in state["stopped_assets"]:
                        state["stopped_assets"].append(symbol)
                elif quote["close"] >= position["entry_reference_gbp"] * 1.02:
                    reason = "2% take-profit signal"
                elif quote["close"] < quote["vwap"]:
                    reason = "Close fell below session VWAP"
            if reason:
                decide(state, symbol, "sell", now, reason, quote)
        if now < boundary(14, 45) and not state["halted"]:
            candidates = sorted((quote for quote in fresh_quotes.values()
                                 if quote["momentum_20m"] is not None and quote["momentum_20m"] > 0 and quote["close"] > quote["vwap"]),
                                key=lambda quote: (-quote["momentum_20m"], quote["symbol"]))
            occupied = set(state["positions"]) | {intent["symbol"] for intent in pending(state, "buy")}
            for quote in candidates:
                symbol = quote["symbol"]
                if len(occupied) >= MAX_POSITIONS or state["buy_fills"] + len(pending(state, "buy")) >= MAX_BUYS:
                    break
                if symbol in occupied or symbol in state["stopped_assets"]:
                    continue
                if symbol in state["cooldowns"] and now < instant(state["cooldowns"][symbol]):
                    continue
                if state["cash_gbp"] - reserved_cash(state) + 1e-8 < BUY_BUDGET:
                    break
                decide(state, symbol, "buy", now, "Close above session VWAP and positive 20-minute return", quote)
                occupied.add(symbol)
    if final:
        cancel_buys(state, now, "Final reconciliation")
        for intent in pending(state, "sell"):
            intent.update(status="unresolved", unresolved_at=stamp(now))
            add_event(state, "unresolved", now, intent_id=intent["intent_id"], symbol=intent["symbol"], reason="No observed completed eligible session bar; no closing fill fabricated")
        state.update(status="incomplete" if state["positions"] else "complete", finalised_at=stamp(now))
        add_event(state, "finalised", now, status=state["status"], open_symbols=sorted(state["positions"]), **totals(state))
    assert_accounting(state)
    new_events = state["events"][event_start:]
    alerts = [event for event in new_events if event["type"] in ("halt", "unresolved", "finalised")]
    if errors:
        alerts.append({"type": "data_unavailable", "details": errors})
    return {"status": state["status"], "checked_at": stamp(now), "new_fills": [event for event in new_events if event["type"] == "fill"],
            "new_decisions": [event for event in new_events if event["type"] == "decision"],
            "alerts": alerts, "pending_intents": len(pending(state)), "halted": state["halted"], **totals(state)}


def atomic_text(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_journal(state, path):
    summary = totals(state)
    money = lambda value: f"£{value:,.4f}"
    lines = ["# £100 virtual stock-market session — 10 September 2026", "",
             f"**Status:** {state['status']}. **Last check (UTC):** {state.get('last_check_at') or 'Not yet checked'}.", "",
             "All amounts are virtual. No broker account, actual orders, deposits or real-money execution are involved.", "",
             "| Measure | GBP |", "|---|---:|", f"| Starting cash | {money(START_CASH)} |"]
    for label, key in (("Cash", "cash_gbp"), ("Reserved for pending buys", "reserved_gbp"), ("Available cash", "available_gbp"), ("Open holdings at last valid mark", "holdings_gbp"), ("Net equity", "equity_gbp"), ("Realised profit/loss", "realised_gbp"), ("Unrealised profit/loss", "unrealised_gbp"), ("Total profit/loss", "total_pl_gbp")):
        lines.append(f"| {label} | {money(summary[key])} |")
    lines += ["", f"Buy fills: {state['buy_fills']}/{MAX_BUYS}. New-entry halt: {'YES — ' + state['halt_reason'] if state['halted'] else 'No'}.", "",
              "## Open positions", "", "| ETF | Units | Cost basis | Last mark | Mark bar end UTC | Mark observed UTC |", "|---|---:|---:|---:|---|---|"]
    for symbol, position in sorted(state["positions"].items()):
        lines.append(f"| {symbol} | {position['quantity']:.8f} | {money(position['cost_basis_gbp'])} | {money(position['mark_gbp'])} | {position['mark_bar_end']} | {position['mark_observed_at']} |")
    if not state["positions"]:
        lines.append("| None | — | — | — | — | — |")
    lines += ["", "## Pending or unresolved intentions", "", "| ID | ETF | Action | Status | Decision UTC | Reason |", "|---|---|---|---|---|---|"]
    outstanding = [intent for intent in state["intents"] if intent["status"] in ("pending", "unresolved")]
    for intent in outstanding:
        lines.append(f"| {intent['intent_id']} | {intent['symbol']} | {intent['side']} | {intent['status']} | {intent['decision_at']} | {intent['reason']} |")
    if not outstanding:
        lines.append("| None | — | — | — | — | — |")
    lines += ["", "## Trade fills", "", "A decision and a fill are different events. Effective fill time is the open of a later eligible five-minute bar; recognition time is when the delayed observation made the fill knowable.", "",
              "| ETF / action | Units | Price incl. cost | Decision UTC | Effective fill UTC | Recognition UTC | Realised P/L | Reason |", "|---|---:|---:|---|---|---|---:|---|"]
    fills = [event for event in state["events"] if event["type"] == "fill"]
    for event in fills:
        lines.append(f"| {event['symbol']} {event['side']} | {event['quantity']:.8f} | {money(event['execution_price_gbp'])} | {event['decision_at']} | {event['effective_fill_at']} | {event['recognised_at']} | {money(event['realised_gbp'])} | {event['reason']} |")
    if not fills:
        lines.append("| No fills yet | — | — | — | — | — | — | — |")
    lines += ["", "## Quote freshness", "", "| ETF | Status | Currency → GBP | Latest complete bar end UTC | Observed UTC | Delay after bar end | Source / issue |", "|---|---|---|---|---|---|---|"]
    for symbol in SYMBOLS:
        quote = state["quotes"].get(symbol, {})
        issue = quote.get("error", "") if quote.get("status") == "unavailable" else quote.get("source", "")
        lines.append(f"| {symbol} | {quote.get('status', 'Not checked')} | {quote.get('currency', '—')} × {quote.get('scale_to_gbp', '—')} | {quote.get('latest_end', '—')} | {quote.get('observed_at', '—')} | {quote.get('age_seconds', '—')} seconds | {issue.replace('|', '/')} |")
    lines += ["", "## Fixed rules and accounting assumptions", "",
              "- Session: 10 September 2026 only. London regular hours 08:00–16:30 BST (07:00–15:30 UTC). Each run observes once; missed checks do not create historical decisions.",
              "- Read-only Yahoo Finance five-minute ETF charts: ISF.L, VUSA.L, EQQQ.L. These quotes may be delayed. Raw responses and real observation timestamps are preserved in snapshots/.",
              "- Only complete bars from today's regular session are used. Future data, nonpositive prices, invalid volume and ambiguous currency are rejected. A bar must have ended according to both observation time and the provider market time. Data older than 25 minutes after the latest complete bar's end are used only to reconcile existing intentions, never for new price signals.",
              "- Prices explicitly quoted in GBp or GBX are divided by 100; GBP prices are unchanged. No FX conversion is used.",
              "- Buy signal: at least six completed session bars, close above volume-weighted HLC typical-price session VWAP, and close above the close four contiguous five-minute bars earlier. Candidates are ranked by that 20-minute return.",
              "- Up to two cash-funded £40 fractional holdings including pending buys; no top-ups, leverage or short positions. Maximum six buy fills. Pending buys reserve cash.",
              "- Each fill applies 10 basis points (0.10%) adverse price cost. No flat fee. ETF transaction tax is assumed zero for this simulation. Fractional ETF fills and bar-open liquidity are modelling assumptions, not executable broker quotes.",
              "- A buy intent is saved before any fill. A fill requires a subsequently observed complete bar whose start is at or after the actual decision timestamp. Fill price is that first eligible bar's open, adjusted adversely for costs. No pre-decision price is used to fill.",
              "- Exit signals: close at least 1% below the raw entry-bar open, at least 2% above it, or below session VWAP. Stops are signals, not guaranteed execution prices. Assets with stop signals cannot re-enter; other sold assets wait 30 minutes after exit recognition.",
              "- A £3 net-equity loss halts new entries for the entire session and queues exits. Unrealised equity uses the latest valid observed close, without a hypothetical future sale cost; sale costs enter realised profit when a sale is recognised.",
              "- No new buy decisions at or after 15:45 BST (14:45 UTC). Scheduled exits are queued on the first check at or after 16:15 BST (15:15 UTC). No buy fill may have an effective time at or after that cutoff. Pending buys with no eligible earlier fill are cancelled at the cutoff after reconciliation.",
              "- Fills require a bar starting before the 16:30 BST regular close. At or after 17:00 BST (16:00 UTC), one final reconciliation finalises the session. Any unsold exposure stays visible as incomplete; no closing sale or final profit is invented.",
              "- state.json is the atomic authoritative record. Its events list only grows; events.jsonl and this journal are derived views. An exclusive local lock prevents overlapping runs.", "",
              "## Event sources", ""]
    for event in fills:
        lines.append(f"- {event['event_id']}, {event['symbol']} {event['side']}: {event['source']}")
    if not fills:
        lines.append("No trade-fill sources yet.")
    if state["status"] == "incomplete":
        lines += ["", "**Incomplete close:** holdings remain valued at their last valid observed marks. This is not a fully realised end-of-day result."]
    atomic_text(path, "\n".join(lines) + "\n")


def save_state(state, folder):
    folder = Path(folder)
    state_path = folder / "state.json"
    if state_path.exists():
        previous = json.loads(state_path.read_text())
        old_events = previous["events"]
        if state["events"][:len(old_events)] != old_events:
            raise ValueError("Immutable event history changed; refusing to save")
    assert_accounting(state)
    atomic_text(state_path, json.dumps(state, indent=2, allow_nan=False) + "\n")
    atomic_text(folder / "events.jsonl", "".join(json.dumps(event, allow_nan=False) + "\n" for event in state["events"]))
    write_journal(state, folder / "journal.md")


@contextlib.contextmanager
def exclusive_lock(folder):
    with (Path(folder) / ".monitor.lock").open("a+") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError("Another virtual monitor run is already active") from error
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def fetch_snapshot(symbol, folder):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=1d&interval=5m&includePrePost=false"
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (VirtualMarketJournal; read-only)", "Accept": "application/json"})
    # This is the only network operation: GET of a public market-data URL.
    with urllib.request.urlopen(request, timeout=15) as response:
        raw = response.read(5_000_001)
    observed_at = dt.datetime.now(UTC)
    if len(raw) > 5_000_000:
        raise ValueError("Market-data response exceeds size limit")
    digest = hashlib.sha256(raw).hexdigest()
    filename = f"{observed_at.strftime('%Y%m%dT%H%M%S.%fZ')}-{symbol}-{digest[:12]}.json"
    snapshot_path = Path(folder) / "snapshots" / filename
    envelope = {"observed_at": stamp(observed_at), "source_url": url, "sha256_raw": digest,
                "raw_response": raw.decode("utf-8")}
    # Unique immutable evidence path, never overwrite an existing snapshot.
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    with snapshot_path.open("x", encoding="utf-8") as handle:
        json.dump(envelope, handle, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    payload = json.loads(raw)
    return parse_snapshot(symbol, payload, observed_at, source=str(snapshot_path), allow_stale_reconciliation=True)


def expire_missed_session(state, now):
    """Administrative finalisation only; never fetch, fill or decide after today."""
    if now.date().isoformat() <= SESSION_DAY or state["status"] in ("complete", "incomplete"):
        return
    cancel_buys(state, now, "Session day expired; final scheduled check was missed")
    for intent in pending(state, "sell"):
        intent.update(status="unresolved", unresolved_at=stamp(now))
        add_event(state, "unresolved", now, intent_id=intent["intent_id"], symbol=intent["symbol"], reason="Session day expired with no final reconciliation; no fill fabricated")
    state.update(status="incomplete" if state["positions"] else "complete", finalised_at=stamp(now), missed_final_check=True)
    add_event(state, "finalised", now, status=state["status"], reason="Missed final check; administrative expiry only", open_symbols=sorted(state["positions"]), **totals(state))
    assert_accounting(state)


def run(folder=BASE):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    with exclusive_lock(folder):
        now = dt.datetime.now(UTC)
        state_path = folder / "state.json"
        state = json.loads(state_path.read_text()) if state_path.exists() else initial_state(now)
        if state_path.exists() and now.date().isoformat() > SESSION_DAY and state["status"] not in ("complete", "incomplete"):
            expire_missed_session(state, now)
            save_state(state, folder)
        if state["status"] in ("complete", "incomplete") or now.date().isoformat() != SESSION_DAY:
            return {"status": state["status"] if state_path.exists() else "outside_session_day", "alerts": ["No market fetch or actions: fixed session has ended"], **totals(state)}
        quotes, errors = {}, {}
        for symbol in SYMBOLS:
            try:
                quotes[symbol] = fetch_snapshot(symbol, folder)
            except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError, IndexError, OSError) as error:
                errors[symbol] = f"{type(error).__name__}: {error}"
        # Decisions use the wall-clock AFTER all responses, never request-start
        # time. This prevents a slower fetch from introducing look-ahead fills.
        now = dt.datetime.now(UTC)
        result = step(state, quotes, errors, now)
        save_state(state, folder)
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--folder", type=Path, default=BASE, help="Persistent virtual-session output directory")
    args = parser.parse_args()
    try:
        print(json.dumps(run(args.folder), indent=2, allow_nan=False))
    except (RuntimeError, ValueError, OSError) as error:
        print(json.dumps({"status": "error", "error": str(error)}))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
