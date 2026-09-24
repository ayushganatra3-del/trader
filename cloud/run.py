#!/usr/bin/env python3
"""One-shot, virtual-only cloud sessions. Python 3.11+, standard library only."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import urllib.error

import engine as e

TERMINAL = ("complete", "incomplete")


def utc_now():
    return dt.datetime.now(e.UTC)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def append_check(path, result):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(result, allow_nan=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def load_control(folder):
    path = folder / "control.json"
    control = read_json(path) if path.exists() else {"version": 1, "active_session": None}
    if control.get("version") != 1 or "active_session" not in control:
        raise ValueError("Unsupported control record; refusing to reset it")
    if control["active_session"] is not None:
        e.session_date(control["active_session"])
    return control


def load_session(folder, day):
    e.session_date(day)
    path = folder / "sessions" / day / "state.json"
    if not path.exists():
        raise ValueError(f"Active session {day} is missing; refusing to invent its balance")
    state = read_json(path)
    if state.get("session_day") != day or state.get("version") != 1:
        raise ValueError("Session record does not match its directory or supported version")
    e.assert_accounting(state)
    return state


def write_dashboard(folder, control, now, last_check):
    sessions = []
    for path in sorted((folder / "sessions").glob("*/state.json"), reverse=True):
        day = path.parent.name
        state = load_session(folder, day)
        write_event_notes(folder, state, now)
        sessions.append({**state, "totals": e.totals(state),
                         "journal_path": f"sessions/{day}/journal.md"})
    dashboard = {"version": 1, "generated_at": e.stamp(now), "control": control,
                 "sessions": sessions, "last_check": last_check}
    e.atomic_text(folder / "dashboard.json", json.dumps(dashboard, indent=2, allow_nan=False) + "\n")


def write_event_notes(folder, state, now):
    """Cloud memory of actual fills/final outcomes, deduplicated by event ID."""
    day = state["session_day"]
    summary = e.totals(state)
    for event in state["events"]:
        if event["type"] not in ("fill", "finalised"):
            continue
        event_id = event["event_id"]
        if not event_id.startswith("event-") or not event_id[6:].isdigit():
            raise ValueError("Invalid event ID for portable memory note")
        path = folder / "notes" / day / f"{event_id}.md"
        if path.exists():
            continue
        imported = day < e.london_day(now)
        lines = [f"# {day} · {event_id} · virtual {event['type']}", "",
                 f"Note generated at: {e.stamp(now)}.",
                 "Imported historical event. Original event times are preserved; this is not a new trade."
                 if imported else "Generated from the saved virtual ledger. No real-money or broker execution.", "",
                 f"Authoritative journal: ../../sessions/{day}/journal.md",
                 f"Authoritative event: ../../sessions/{day}/events.jsonl · {event_id}", ""]
        if event["type"] == "fill":
            lines += [f"- Instrument/action: {event['symbol']} {event['side']}.",
                      f"- Units: {event['quantity']:.12g}; effective price including modelled cost: £{event['execution_price_gbp']:.12g}.",
                      f"- Cash change: £{event['cash_change_gbp']:.8f}; realised trade profit/loss: £{event['realised_gbp']:.8f}.",
                      f"- Intention: {event['intent_id']}; decision: {event['decision_at']}.",
                      f"- Effective fill: {event['effective_fill_at']}; recognition: {event['recognised_at']}.",
                      f"- Evidence path relative to the data root: {event['source']}."]
        else:
            lines += [f"- Final status: {event['status']}.", f"- Finalisation time: {event['recorded_at']}.",
                      f"- Final cash: £{event['cash_gbp']:.8f}; open holdings: £{event['holdings_gbp']:.8f}.",
                      f"- Final net virtual profit/loss: £{event['total_pl_gbp']:.8f}.",
                      "- Unresolved holdings stay open at last valid marks; no closing sale is invented."]
        lines += ["", f"Portfolio snapshot from stored state, last checked {state.get('last_check_at') or 'not yet checked'}:",
                  f"cash £{summary['cash_gbp']:.8f}; holdings £{summary['holdings_gbp']:.8f}; "
                  f"equity £{summary['equity_gbp']:.8f}; realised £{summary['realised_gbp']:.8f}; "
                  f"unrealised £{summary['unrealised_gbp']:.8f}; net total £{summary['total_pl_gbp']:.8f}.",
                  "This snapshot can be later than the event above. Pending intentions are not fills."]
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with path.open("x", encoding="utf-8") as handle:
                handle.write("\n".join(lines) + "\n")
                handle.flush()
                os.fsync(handle.fileno())
        except FileExistsError:
            pass


def record_result(folder, control, result, now, session_day=None):
    result = {"checked_at": e.stamp(now), **result}
    append_check(folder / "checks.jsonl", result)
    if session_day and (folder / "sessions" / session_day / "state.json").exists():
        append_check(folder / "sessions" / session_day / "checks.jsonl", result)
    control = {**control, "updated_at": e.stamp(now)}
    e.atomic_text(folder / "control.json", json.dumps(control, indent=2, allow_nan=False) + "\n")
    write_dashboard(folder, control, now, result)
    return result


def validate_start(day, now):
    date = e.session_date(day)
    today = now.astimezone(e.LONDON).date()
    if date.weekday() >= 5:
        raise ValueError("Choose a weekday for the London stock-market simulation")
    if not today <= date <= today + dt.timedelta(days=7):
        raise ValueError("Session must be today or within the next seven calendar days")
    if date == today and now >= e.boundary(day, 15, 45):
        raise ValueError("Today's 15:45 London entry cutoff has passed; choose a future weekday")


def perform(action, folder, control, day, clock, fetcher):
    now = clock()
    e.london_day(now)  # Reject naive injectable clocks before any state mutation.
    active = control["active_session"]
    if day is not None:
        e.session_date(day)
    if action == "start":
        day = day or e.london_day(now)
        # An exact repeated start is idempotent, even if cutoff has since passed.
        if active == day:
            state = load_session(folder, day)
            if state["status"] not in TERMINAL:
                return {"status": "already_started", "session_day": day, "new_fills": [],
                        "alerts": [], **e.totals(state)}, now, day
        if active is not None:
            raise ValueError(f"Session {active} is still selected; check or stop it before starting another")
        if (folder / "sessions" / day).exists():
            raise ValueError("This session date already exists and can never be reset or restarted")
        validate_start(day, now)
        state = e.initial_state(now, day)
        e.add_event(state, "session_started", now, reason="Explicit one-day virtual session start")
        e.save_state(state, folder / "sessions" / day)
        control["active_session"] = day
        return {"status": "started", "session_day": day, "new_fills": [], "alerts": [],
                **e.totals(state)}, now, day
    if action not in ("check", "stop"):
        raise ValueError("Action must be check, start or stop")
    if day is not None and day != active:
        raise ValueError("Requested date does not match the active session; no session was changed")
    if active is None:
        return {"status": "idle", "new_fills": [], "alerts": [],
                "message": "No active session. Start a date explicitly to simulate trading."}, now, None
    state = load_session(folder, active)
    session_folder = folder / "sessions" / active
    if state["status"] in TERMINAL:
        control["active_session"] = None
        return {"status": state["status"], "session_day": active, "new_fills": [],
                "alerts": [], **e.totals(state)}, now, active
    if e.london_day(now) > active:
        e.expire_missed_session(state, now)
        result = {"status": state["status"], "new_fills": [], "alerts": [
            {"type": "missed_final_check", "message": "Expired without fetching or replaying missed decisions."}],
                  **e.totals(state)}
    elif action == "stop":
        before = len(state["events"])
        e.request_stop(state, now)
        result = {"status": state["status"], "new_fills": [], "alerts": [],
                  "new_decisions": [event for event in state["events"][before:] if event["type"] == "decision"],
                  "stop_requested": True, "pending_intents": len(e.pending(state)), **e.totals(state)}
    elif e.london_day(now) < active or now < e.boundary(active, 8):
        return {"status": "waiting_for_open", "session_day": active, "new_fills": [],
                "alerts": [], "opens_at": e.stamp(e.boundary(active, 8)), **e.totals(state)}, now, active
    else:
        quotes, errors = {}, {}
        for symbol in e.SYMBOLS:
            try:
                quotes[symbol] = fetcher(symbol, session_folder, active)
            except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError, IndexError, OSError) as error:
                errors[symbol] = f"{type(error).__name__}: {error}"
        # Fetches may be slow. Only the actual time after observations can be a
        # decision time. If midnight passed, expire without replay or fills.
        now = clock()
        if e.london_day(now) > active:
            e.expire_missed_session(state, now)
            result = {"status": state["status"], "new_fills": [],
                      "alerts": [{"type": "missed_final_check"}], **e.totals(state)}
        else:
            result = e.step(state, quotes, errors, now)
    e.save_state(state, session_folder)
    if state["status"] in TERMINAL:
        control["active_session"] = None
    return {"session_day": active, **result}, now, active


def execute(action, data_dir, day=None, *, clock=utc_now, fetcher=None):
    """Locked one-shot operation. No work is scheduled by this module itself."""
    folder = Path(data_dir)
    folder.mkdir(parents=True, exist_ok=True)
    with e.exclusive_lock(folder):
        control = load_control(folder)
        try:
            result, now, session_day = perform(action, folder, control, day, clock, fetcher or e.fetch_snapshot)
        except (RuntimeError, ValueError, OSError, KeyError, TypeError, IndexError) as error:
            # The last committed state stays authoritative; do not save any
            # partially mutated in-memory portfolio on failure.
            control = load_control(folder)
            now = clock()
            result = {"status": "error", "action": action, "new_fills": [],
                      "error": f"{type(error).__name__}: {error}"}
            session_day = control["active_session"]
        return record_result(folder, control, {"action": action, **result}, now, session_day)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--action", choices=("check", "start", "stop"), default="check")
    parser.add_argument("--date", dest="day", help="London session date, YYYY-MM-DD (default: today when starting)")
    parser.add_argument("--data-dir", type=Path, default=Path("data"), help="Persistent cloud data directory")
    args = parser.parse_args()
    try:
        result = execute(args.action, args.data_dir, args.day)
    except (RuntimeError, ValueError, OSError, KeyError, TypeError) as error:
        # A corrupt record/lock failure must not overwrite valid earlier data.
        result = {"status": "error", "error": f"{type(error).__name__}: {error}"}
    print(json.dumps(result, indent=2, allow_nan=False))
    raise SystemExit(1 if result["status"] == "error" else 0)


if __name__ == "__main__":
    main()
