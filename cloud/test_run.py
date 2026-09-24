"""Offline cloud lifecycle, London clock and persistence regression tests."""
import copy
import datetime as dt
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock

import engine as e
import probe as p
import run as r
from test_engine import at, quote, seed_position


DAY = "2026-09-10"


class CloudTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        self.now = at("07:31:00")
        self.fetch = Mock(side_effect=AssertionError("Network forbidden in lifecycle test"))

    def run_action(self, action="check", day=None):
        return r.execute(action, self.folder, day, clock=lambda: self.now, fetcher=self.fetch)

    def state(self, day=DAY):
        return r.load_session(self.folder, day)

    def dashboard(self):
        return json.loads((self.folder / "dashboard.json").read_text())

    def seed(self):
        self.run_action("start")
        state = seed_position()
        # Preserve the session_started event as an immutable prefix.
        original = self.state()
        for event in state["events"]:
            event["event_id"] = f"event-{len(original['events']) + 1:06d}"
            original["events"].append(event)
        state["events"] = original["events"]
        e.save_state(state, self.folder / "sessions" / DAY)
        return state

    def test_idle_check_never_creates_session_or_fetches(self):
        result = self.run_action()
        self.assertEqual(result["status"], "idle")
        self.assertEqual(self.dashboard()["sessions"], [])
        self.assertIsNone(self.dashboard()["control"]["active_session"])
        self.fetch.assert_not_called()

    def test_start_is_explicit_one_day_no_market_fetch(self):
        result = self.run_action("start")
        self.assertEqual(result["status"], "started")
        self.assertEqual(result["equity_gbp"], 100)
        self.assertEqual(self.dashboard()["control"]["active_session"], DAY)
        self.assertEqual(self.dashboard()["sessions"][0]["journal_path"], f"sessions/{DAY}/journal.md")
        self.fetch.assert_not_called()

    def test_repeated_start_does_not_reset_state(self):
        state = self.seed()
        result = self.run_action("start")
        self.assertEqual(result["status"], "already_started")
        self.assertEqual(self.state(), state)

    def test_invalid_dates_cannot_create_paths_or_sessions(self):
        for day in ("2026-9-10", "../old", "2026-09-09", "2026-09-12", "2026-09-18"):
            self.assertEqual(self.run_action("start", day)["status"], "error")
        self.assertFalse((self.folder / "sessions").exists())

    def test_future_weekday_up_to_seven_days_is_allowed(self):
        self.assertEqual(self.run_action("start", "2026-09-17")["status"], "started")
        self.assertEqual(self.run_action()["status"], "waiting_for_open")
        self.fetch.assert_not_called()

    def test_today_cutoff_cannot_start(self):
        self.now = at("14:45:00")
        self.assertEqual(self.run_action("start")["status"], "error")
        self.assertFalse((self.folder / "sessions").exists())

    def test_before_london_open_does_not_fetch(self):
        self.now = at("06:59:59")
        self.run_action("start")
        self.assertEqual(self.run_action()["status"], "waiting_for_open")
        self.fetch.assert_not_called()

    def test_a_second_date_cannot_replace_active_session(self):
        self.run_action("start")
        self.assertEqual(self.run_action("start", "2026-09-11")["status"], "error")
        self.assertEqual(self.dashboard()["control"]["active_session"], DAY)

    def test_check_date_mismatch_keeps_original_portfolio(self):
        self.run_action("start")
        before = self.state()
        self.assertEqual(self.run_action("check", "2026-09-11")["status"], "error")
        self.assertEqual(before, self.state())
        self.fetch.assert_not_called()

    def test_data_failures_are_saved_and_do_not_change_cash(self):
        self.run_action("start")
        self.fetch.side_effect = OSError("offline provider")
        result = self.run_action()
        self.assertEqual(result["status"], "active")
        self.assertEqual(result["equity_gbp"], 100)
        self.assertEqual(result["alerts"][0]["type"], "data_unavailable")
        self.assertEqual(len(self.state()["last_errors"]), 3)
        self.assertIn("offline provider", (self.folder / "checks.jsonl").read_text())
        self.assertIn("offline provider", (self.folder / "sessions" / DAY / "checks.jsonl").read_text())

    def test_decision_uses_post_fetch_clock(self):
        self.run_action("start")
        self.fetch.side_effect = lambda symbol, folder, day: quote(symbol=symbol)
        times = iter([at("07:31:00"), at("07:33:00")])
        result = r.execute("check", self.folder, clock=lambda: next(times), fetcher=self.fetch)
        self.assertEqual(len(result["new_decisions"]), 2)
        self.assertEqual({i["decision_at"] for i in self.state()["intents"]}, {e.stamp(at("07:33:00"))})
        self.assertEqual(result["new_fills"], [])

    def test_stop_cancels_unfilled_buys_without_filling(self):
        self.run_action("start")
        self.fetch.side_effect = lambda symbol, folder, day: quote(symbol=symbol)
        self.run_action()
        self.assertEqual(len(e.pending(self.state(), "buy")), 2)
        self.now = at("07:32:00")
        before_calls = self.fetch.call_count
        result = self.run_action("stop")
        self.assertEqual(result["status"], "complete")
        self.assertEqual(result["equity_gbp"], 100)
        self.assertEqual(self.fetch.call_count, before_calls)
        self.assertIsNone(self.dashboard()["control"]["active_session"])
        self.assertFalse(e.pending(self.state()))

    def test_stop_holding_queues_later_exit_and_keeps_reconciling(self):
        self.seed()
        self.now = at("07:42:00")
        result = self.run_action("stop")
        self.assertEqual(result["status"], "active")
        self.assertEqual(result["new_fills"], [])
        self.assertEqual(e.pending(self.state(), "sell")[0]["decision_at"], e.stamp(self.now))
        self.assertEqual(self.dashboard()["control"]["active_session"], DAY)
        self.fetch.assert_not_called()
        self.now = at("07:51:00")
        self.fetch.side_effect = lambda symbol, folder, day: quote(symbol=symbol, last_start="07:45:00", observed="07:51:00")
        result = self.run_action()
        self.assertEqual(result["status"], "complete")
        self.assertEqual(len(result["new_fills"]), 1)
        self.assertEqual(result["new_fills"][0]["side"], "sell")
        self.assertEqual(result["new_fills"][0]["effective_fill_at"], e.stamp(at("07:45:00")))
        self.assertIsNone(self.dashboard()["control"]["active_session"])
        self.assertFalse(e.pending(self.state(), "buy"))

    def test_repeated_stop_does_not_duplicate_exit_or_events(self):
        self.seed()
        self.now = at("07:42:00")
        self.run_action("stop")
        before = self.state()
        self.now = at("07:43:00")
        self.run_action("stop")
        self.assertEqual(before, self.state())

    def test_repeated_stop_at_deadline_finalises_existing_stop(self):
        self.seed()
        self.now = at("07:42:00")
        self.run_action("stop")
        self.now = at("16:00:00")
        result = self.run_action("stop")
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(len([event for event in self.state()["events"] if event["type"] == "stop_requested"]), 1)
        self.assertIsNone(self.dashboard()["control"]["active_session"])

    def test_stop_never_erases_a_late_unclosed_position(self):
        self.seed()
        self.now = at("16:00:00")
        result = self.run_action("stop")
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["cash_gbp"], 60)
        self.assertTrue(self.state()["positions"])
        self.assertFalse(e.pending(self.state()))
        self.assertIsNone(self.dashboard()["control"]["active_session"])

    def test_later_day_expires_without_network_or_backfill(self):
        seeded = self.seed()
        self.now = e.instant("2026-09-11T07:31:00Z")
        result = self.run_action()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["new_fills"], [])
        self.assertEqual(self.state()["positions"], seeded["positions"])
        self.assertTrue(self.state()["missed_final_check"])
        self.assertIsNone(self.dashboard()["control"]["active_session"])
        self.fetch.assert_not_called()

    def test_final_missing_quotes_reports_incomplete_and_clears_active(self):
        self.seed()
        self.now = at("16:01:00")
        self.fetch.side_effect = ValueError("no valid closing bars")
        result = self.run_action()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["cash_gbp"], 60)
        self.assertIsNone(self.dashboard()["control"]["active_session"])
        self.assertEqual(len(self.state()["positions"]), 1)

    def test_existing_finished_date_never_resets(self):
        self.run_action("start")
        self.run_action("stop")
        before = self.state()
        self.assertEqual(self.run_action("start")["status"], "error")
        self.assertEqual(before, self.state())

    def test_new_date_requires_explicit_start_after_previous_finishes(self):
        self.run_action("start")
        self.run_action("stop")
        self.now = e.instant("2026-09-11T07:31:00Z")
        self.assertEqual(self.run_action()["status"], "idle")
        self.assertFalse((self.folder / "sessions" / "2026-09-11").exists())
        self.assertEqual(self.run_action("start")["status"], "started")
        self.assertEqual(len(self.dashboard()["sessions"]), 2)
        self.assertEqual(self.dashboard()["sessions"][0]["session_day"], "2026-09-11")

    def test_missing_active_state_does_not_invent_starting_cash(self):
        e.atomic_text(self.folder / "control.json", json.dumps({"version": 1, "active_session": DAY}))
        result = self.run_action()
        self.assertEqual(result["status"], "error")
        self.assertFalse((self.folder / "sessions" / DAY).exists())
        self.fetch.assert_not_called()

    def test_cloud_memory_only_records_fills_and_final_outcomes_once(self):
        self.seed()
        self.now = at("07:42:00")
        self.run_action("stop")
        notes = list((self.folder / "notes" / DAY).glob("*.md"))
        self.assertEqual(len(notes), 1)
        note_text = notes[0].read_text()
        self.assertIn("ISF.L buy", note_text)
        self.assertIn("recognition:", note_text)
        self.now = at("07:43:00")
        self.run_action("stop")
        self.assertEqual(notes[0].read_text(), note_text)
        self.now = at("16:00:00")
        self.run_action("stop")
        notes = list((self.folder / "notes" / DAY).glob("*.md"))
        self.assertEqual(len(notes), 2)
        self.assertTrue(any("Final status: incomplete" in path.read_text() for path in notes))

    def test_imported_ledger_note_preserves_original_recognition(self):
        self.seed()
        self.now = e.instant("2026-09-24T08:00:00Z")
        self.run_action()
        note = next(path for path in (self.folder / "notes" / DAY).glob("*.md") if "ISF.L buy" in path.read_text())
        self.assertIn("Imported historical event", note.read_text())
        self.assertIn("recognition: 2026-09-10T07:41:00", note.read_text())


class LondonTimeTests(unittest.TestCase):
    def test_boundaries_follow_summer_and_winter_offsets(self):
        self.assertEqual(e.boundary("2026-09-10", 8), e.instant("2026-09-10T07:00:00Z"))
        self.assertEqual(e.boundary("2026-12-10", 8), e.instant("2026-12-10T08:00:00Z"))
        self.assertEqual(e.boundary("2026-09-10", 17), e.instant("2026-09-10T16:00:00Z"))
        self.assertEqual(e.boundary("2026-12-10", 17), e.instant("2026-12-10T17:00:00Z"))

    def test_dates_are_london_dates_near_midnight(self):
        now = e.instant("2026-09-09T23:30:00Z")
        self.assertEqual(e.london_day(now), "2026-09-10")
        r.validate_start("2026-09-10", now)

    def test_winter_cutoff_is_1545_utc_not_summer_cutoff(self):
        r.validate_start("2026-12-10", e.instant("2026-12-10T14:46:00Z"))
        with self.assertRaisesRegex(ValueError, "cutoff"):
            r.validate_start("2026-12-10", e.instant("2026-12-10T15:45:00Z"))

    def test_winter_regular_bars_parse_and_fill_at_correct_hour(self):
        day = "2026-12-10"
        observed = e.instant(f"{day}T08:31:00Z")
        starts = [e.boundary(day, 8).timestamp() + i * 300 for i in range(6)]
        values = [10 + i * 0.01 for i in range(6)]
        payload = {"chart": {"result": [{"meta": {"symbol": "ISF.L", "currency": "GBP", "regularMarketTime": observed.timestamp()},
                                            "timestamp": starts, "indicators": {"quote": [{"open": values, "high": values,
                                                                                          "low": values, "close": values, "volume": [100] * 6}]}}]}}
        q = e.parse_snapshot("ISF.L", payload, observed, day)
        state = e.initial_state(observed, day)
        result = e.step(state, {"ISF.L": q}, {}, observed)
        self.assertEqual(len(result["new_decisions"]), 1)
        self.assertEqual(q["latest_end"], e.stamp(e.instant(f"{day}T08:30:00Z")))

    def test_naive_clock_and_timestamp_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "timezone"):
            e.stamp(dt.datetime(2026, 9, 10, 8))
        with self.assertRaisesRegex(ValueError, "timezone"):
            e.instant("2026-09-10T08:00:00")


class ProviderProbeTests(unittest.TestCase):
    def test_probe_checks_three_symbols_and_removes_temporary_evidence(self):
        folders = []

        def fetch(symbol, folder, day):
            folders.append(folder)
            self.assertEqual(day, DAY)
            return quote(symbol=symbol)

        result = p.probe(fetcher=fetch, now=at("07:31:00"))
        self.assertEqual(result["status"], "available")
        self.assertEqual(set(result["symbols"]), set(e.SYMBOLS))
        self.assertTrue(all(not folder.exists() for folder in folders))

    def test_probe_failure_is_visible_without_fabricating_quotes(self):
        result = p.probe(fetcher=Mock(side_effect=OSError("provider blocked")), now=at("07:31:00"))
        self.assertEqual(result["status"], "unavailable")
        self.assertTrue(all(item["status"] == "unavailable" for item in result["symbols"].values()))

    def test_probe_can_report_valid_after_hours_stale_data(self):
        result = p.probe(fetcher=lambda symbol, folder, day: quote(symbol=symbol, observed="16:00:01", market_time="15:30:00",
                                                                  last_start="15:25:00", allow_stale_reconciliation=True), now=at("16:00:01"))
        self.assertEqual(result["status"], "available")
        self.assertFalse(result["symbols"]["ISF.L"]["fresh_for_new_decisions"])


if __name__ == "__main__":
    unittest.main()
