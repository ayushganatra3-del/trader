"""Offline behavioural checks; no network and no broker."""
import copy
import datetime as dt
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import engine as m

SESSION_DAY = "2026-09-10"


def at(clock):
    return m.instant(f"2026-09-10T{clock}Z")


def fixture(symbol="ISF.L", last_start="07:25:00", observed="07:31:00", currency="GBP", base=10.0, slope=0.01, closes=None, market_time=None):
    final = at(last_start)
    starts = list(range(int(at("07:00:00").timestamp()), int(final.timestamp()) + 1, 300))
    prices = [base + i * slope for i in range(len(starts))]
    if closes:
        for index, value in closes.items():
            prices[index] = value
    data = {"open": prices[:], "close": prices[:], "high": [p + .001 for p in prices], "low": [p - .001 for p in prices], "volume": [100] * len(prices)}
    return {"chart": {"error": None, "result": [{"meta": {"symbol": symbol, "currency": currency, "regularMarketTime": at(market_time or observed).timestamp()}, "timestamp": starts, "indicators": {"quote": [data]}}]}}


def quote(symbol="ISF.L", last_start="07:25:00", observed="07:31:00", **kwargs):
    allow_stale = kwargs.pop("allow_stale_reconciliation", False)
    return m.parse_snapshot(symbol, fixture(symbol, last_start, observed, **kwargs), at(observed), SESSION_DAY, source="offline fixture", allow_stale_reconciliation=allow_stale)


def seed_position():
    state = m.initial_state(at("07:31:00"), SESSION_DAY)
    m.step(state, {"ISF.L": quote()}, {}, at("07:31:00"))
    m.step(state, {"ISF.L": quote(last_start="07:35:00", observed="07:41:00")}, {}, at("07:41:00"))
    return state


class DataValidationTests(unittest.TestCase):
    def test_explicit_pence_and_pounds_conversion(self):
        gbp = quote(currency="GBP", base=10, slope=.01)
        gbpence = quote(currency="GBp", base=1000, slope=1)
        gbx = quote(currency="GBX", base=1000, slope=1)
        self.assertAlmostEqual(gbp["close"], gbpence["close"])
        self.assertAlmostEqual(gbp["close"], gbx["close"])
        with self.assertRaisesRegex(ValueError, "currency"):
            quote(currency="USD")

    def test_delayed_partial_regular_bar_not_used(self):
        q = quote(last_start="07:35:00", observed="07:51:00", market_time="07:37:30")
        self.assertEqual(q["latest_start"], m.stamp(at("07:30:00")))
        self.assertEqual(q["latest_end"], m.stamp(at("07:35:00")))

    def test_irregular_yahoo_latest_trade_row_ignored(self):
        payload = fixture(last_start="07:30:00", observed="07:51:00", market_time="07:32:45")
        result = payload["chart"]["result"][0]
        result["timestamp"].append(at("07:32:45").timestamp())
        for key, value in result["indicators"]["quote"][0].items():
            value.append(100 if key == "volume" else 10)
        q = m.parse_snapshot("ISF.L", payload, at("07:51:00"), SESSION_DAY)
        self.assertEqual(q["latest_start"], m.stamp(at("07:25:00")))

    def test_stale_snapshot_rejected_for_normal_use(self):
        with self.assertRaisesRegex(ValueError, "stale"):
            quote(observed="08:01:00")

    def test_provider_time_future_or_wrong_day_rejected(self):
        with self.assertRaisesRegex(ValueError, "future"):
            quote(market_time="07:32:00")
        payload = fixture()
        payload["chart"]["result"][0]["meta"]["regularMarketTime"] = m.instant("2026-09-09T07:31:00Z").timestamp()
        with self.assertRaisesRegex(ValueError, "today"):
            m.parse_snapshot("ISF.L", payload, at("07:31:00"), SESSION_DAY)

    def test_missing_provider_time_rejected(self):
        payload = fixture()
        del payload["chart"]["result"][0]["meta"]["regularMarketTime"]
        with self.assertRaisesRegex(ValueError, "market time"):
            m.parse_snapshot("ISF.L", payload, at("07:31:00"), SESSION_DAY)

    def test_nonpositive_price_and_absent_volume_rejected(self):
        for field, value in (("close", 0), ("volume", -1), ("volume", None), ("open", float("nan"))):
            payload = fixture()
            payload["chart"]["result"][0]["indicators"]["quote"][0][field][1] = value
            with self.assertRaises(ValueError):
                m.parse_snapshot("ISF.L", payload, at("07:31:00"), SESSION_DAY)

    def test_wrong_bar_granularity_rejected(self):
        payload = fixture()
        payload["chart"]["result"][0]["meta"]["dataGranularity"] = "1m"
        with self.assertRaisesRegex(ValueError, "granularity"):
            m.parse_snapshot("ISF.L", payload, at("07:31:00"), SESSION_DAY)

    def test_zero_total_volume_cannot_signal(self):
        payload = fixture()
        data = payload["chart"]["result"][0]["indicators"]["quote"][0]
        data["volume"] = [0] * len(data["volume"])
        with self.assertRaisesRegex(ValueError, "volume"):
            m.parse_snapshot("ISF.L", payload, at("07:31:00"), SESSION_DAY)

    def test_missing_bars_cannot_masquerade_as_20_minutes(self):
        payload = fixture(last_start="07:35:00", observed="07:41:00")
        result = payload["chart"]["result"][0]
        del result["timestamp"][-3]
        for values in result["indicators"]["quote"][0].values():
            del values[-3]
        self.assertIsNone(m.parse_snapshot("ISF.L", payload, at("07:41:00"), SESSION_DAY)["momentum_20m"])


class ExecutionTests(unittest.TestCase):
    def test_signal_is_pending_not_a_retroactive_fill(self):
        state = m.initial_state(at("07:31:00"), SESSION_DAY)
        result = m.step(state, {"ISF.L": quote()}, {}, at("07:31:00"))
        self.assertEqual(result["new_fills"], [])
        self.assertEqual(state["cash_gbp"], 100)
        self.assertEqual(m.reserved_cash(state), 40)
        self.assertEqual(m.pending(state)[0]["decision_at"], m.stamp(at("07:31:00")))

    def test_no_fill_on_bar_already_underway_when_decision_observed(self):
        state = m.initial_state(at("07:31:00"), SESSION_DAY)
        m.step(state, {"ISF.L": quote()}, {}, at("07:31:00"))
        result = m.step(state, {"ISF.L": quote(last_start="07:30:00", observed="07:36:00")}, {}, at("07:36:00"))
        self.assertEqual(result["new_fills"], [])
        result = m.step(state, {"ISF.L": quote(last_start="07:35:00", observed="07:41:00")}, {}, at("07:41:00"))
        fill = result["new_fills"][0]
        self.assertEqual(fill["effective_fill_at"], m.stamp(at("07:35:00")))
        self.assertGreater(m.instant(fill["effective_fill_at"]), m.instant(fill["decision_at"]))
        self.assertGreater(m.instant(fill["recognised_at"]), m.instant(fill["effective_fill_at"]))

    def test_repeated_checks_do_not_duplicate_intents_or_fills(self):
        state = seed_position()
        previous = copy.deepcopy(state["events"])
        m.step(state, {"ISF.L": quote(last_start="07:35:00", observed="07:41:00")}, {}, at("07:41:00"))
        self.assertEqual(state["events"], previous)
        self.assertEqual(state["buy_fills"], 1)
        self.assertEqual(state["cash_gbp"], 60)

    def test_cash_fractional_cost_and_round_trip_reconcile(self):
        state = seed_position()
        position = state["positions"]["ISF.L"]
        raw_buy = 10.07
        expected_quantity = 40 / (raw_buy * 1.001)
        self.assertAlmostEqual(position["quantity"], expected_quantity)
        self.assertAlmostEqual(m.totals(state)["total_pl_gbp"], -40 * .001 / 1.001)
        m.decide(state, "ISF.L", "sell", at("07:41:00"), "test exit")
        m.step(state, {"ISF.L": quote(last_start="07:45:00", observed="07:51:00", base=10.1, slope=0)}, {}, at("07:51:00"))
        expected_profit = expected_quantity * 10.1 * .999 - 40
        self.assertAlmostEqual(state["cash_gbp"], 100 + expected_profit)
        self.assertAlmostEqual(state["realised_gbp"], expected_profit)
        self.assertEqual(len(state["positions"]), 0)
        m.assert_accounting(state)

    def test_three_candidates_ranked_two_only_and_cash_reserved(self):
        state = m.initial_state(at("07:31:00"), SESSION_DAY)
        quotes = {symbol: quote(symbol, slope=slope) for symbol, slope in zip(m.SYMBOLS, (.01, .03, .02))}
        m.step(state, quotes, {}, at("07:31:00"))
        self.assertEqual([intent["symbol"] for intent in m.pending(state)], ["VUSA.L", "EQQQ.L"])
        self.assertEqual(m.reserved_cash(state), 80)
        self.assertEqual(m.totals(state)["available_gbp"], 20)
        later = {symbol: quote(symbol, last_start="07:35:00", observed="07:41:00", slope=slope) for symbol, slope in zip(m.SYMBOLS, (.01, .03, .02))}
        m.step(state, later, {}, at("07:41:00"))
        self.assertEqual(len(state["positions"]), 2)
        self.assertEqual(state["cash_gbp"], 20)
        self.assertFalse(m.pending(state, "buy"))
        m.assert_accounting(state)

    def test_empty_data_cannot_generate_trades_or_equity_changes(self):
        state = m.initial_state(at("07:31:00"), SESSION_DAY)
        result = m.step(state, {}, {symbol: "unavailable" for symbol in m.SYMBOLS}, at("07:31:00"))
        self.assertEqual(result["equity_gbp"], 100)
        self.assertEqual(state["events"], [])

    def test_stale_data_can_reconcile_but_cannot_create_price_decisions(self):
        state = m.initial_state(at("07:31:00"), SESSION_DAY)
        stale = quote(last_start="07:25:00", observed="08:01:00", allow_stale_reconciliation=True)
        m.step(state, {"ISF.L": stale}, {}, at("08:01:00"))
        self.assertEqual(state["events"], [])

    def test_stop_queues_forward_exit_and_blocks_reentry(self):
        state = seed_position()
        falling = quote(last_start="07:45:00", observed="07:51:00", closes={-1: 9.9})
        result = m.step(state, {"ISF.L": falling}, {}, at("07:51:00"))
        self.assertEqual(result["new_fills"], [])
        self.assertEqual(m.pending(state, "sell")[0]["reason"], "1% stop signal")
        self.assertIn("ISF.L", state["stopped_assets"])
        m.step(state, {"ISF.L": quote(last_start="07:55:00", observed="08:01:00")}, {}, at("08:01:00"))
        m.step(state, {"ISF.L": quote(last_start="08:35:00", observed="08:41:00")}, {}, at("08:41:00"))
        self.assertFalse(m.pending(state, "buy"))

    def test_halt_persists_when_prices_recover(self):
        state = seed_position()
        result = m.step(state, {"ISF.L": quote(last_start="07:45:00", observed="07:51:00", closes={-1: 9.0})}, {}, at("07:51:00"))
        self.assertTrue(state["halted"])
        self.assertLess(result["total_pl_gbp"], -3)
        self.assertEqual(len(m.pending(state, "sell")), 1)
        m.step(state, {"ISF.L": quote(last_start="07:55:00", observed="08:01:00")}, {}, at("08:01:00"))
        m.step(state, {"ISF.L": quote(last_start="08:35:00", observed="08:41:00")}, {}, at("08:41:00"))
        self.assertTrue(state["halted"])
        self.assertFalse(m.pending(state, "buy"))

    def test_stale_marks_do_not_trigger_exit(self):
        state = seed_position()
        original_mark = state["positions"]["ISF.L"]["mark_gbp"]
        stale = quote(last_start="07:45:00", observed="08:31:00", closes={-1: 9}, allow_stale_reconciliation=True)
        m.step(state, {"ISF.L": stale}, {}, at("08:31:00"))
        self.assertFalse(m.pending(state, "sell"))
        self.assertEqual(state["positions"]["ISF.L"]["mark_gbp"], original_mark)

    def test_no_buy_effective_at_or_after_entry_cutoff(self):
        state = m.initial_state(at("14:40:01"), SESSION_DAY)
        m.step(state, {"ISF.L": quote(last_start="14:35:00", observed="14:40:01", slope=.0001)}, {}, at("14:40:01"))
        self.assertEqual(len(m.pending(state, "buy")), 1)
        result = m.step(state, {"ISF.L": quote(last_start="14:45:00", observed="14:51:00", slope=.0001)}, {}, at("14:51:00"))
        self.assertEqual(result["new_fills"], [])
        self.assertFalse(m.pending(state, "buy"))
        self.assertEqual(state["cash_gbp"], 100)

    def test_final_reconciliation_can_recognise_existing_sell_on_stale_data(self):
        state = seed_position()
        m.step(state, {}, {}, at("15:15:01"))
        self.assertEqual(len(m.pending(state, "sell")), 1)
        closing_quote = quote(last_start="15:25:00", observed="16:00:01", slope=.0001, market_time="15:30:00", allow_stale_reconciliation=True)
        result = m.step(state, {"ISF.L": closing_quote}, {}, at("16:00:01"))
        self.assertEqual(result["status"], "complete")
        self.assertEqual(result["new_fills"][0]["effective_fill_at"], m.stamp(at("15:20:00")))
        self.assertEqual(state["positions"], {})

    def test_missing_final_fill_reports_unresolved_without_fabricated_profit(self):
        state = seed_position()
        m.step(state, {}, {}, at("15:15:01"))
        result = m.step(state, {}, {}, at("16:00:01"))
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(state["cash_gbp"], 60)
        self.assertEqual(state["realised_gbp"], 0)
        self.assertEqual(len(state["positions"]), 1)
        self.assertEqual(state["intents"][-1]["status"], "unresolved")
        self.assertEqual(result["new_fills"], [])

    def test_final_status_and_other_day_cannot_trade_or_reset(self):
        state = seed_position()
        m.step(state, {}, {}, at("16:00:01"))
        final_state = copy.deepcopy(state)
        m.step(state, {}, {}, at("16:01:00"))
        m.step(state, {}, {}, m.instant("2026-09-11T08:00:00Z"))
        self.assertEqual(state, final_state)

    def test_missed_final_check_expires_without_filling_or_losing_exposure(self):
        state = seed_position()
        m.step(state, {}, {}, at("15:15:01"))
        before_fills = [event for event in state["events"] if event["type"] == "fill"]
        m.expire_missed_session(state, m.instant("2026-09-11T08:00:00Z"))
        self.assertEqual(state["status"], "incomplete")
        self.assertTrue(state["missed_final_check"])
        self.assertEqual(state["cash_gbp"], 60)
        self.assertEqual([event for event in state["events"] if event["type"] == "fill"], before_fills)

    def test_clock_cannot_move_backwards(self):
        state = seed_position()
        with self.assertRaisesRegex(ValueError, "backwards"):
            m.step(state, {}, {}, at("07:30:00"))


class PersistenceTests(unittest.TestCase):
    def test_persisted_intents_survive_restart_and_fill_once(self):
        with tempfile.TemporaryDirectory() as folder:
            state = m.initial_state(at("07:31:00"), SESSION_DAY)
            m.step(state, {"ISF.L": quote()}, {}, at("07:31:00"))
            m.save_state(state, folder)
            loaded = json.loads((Path(folder) / "state.json").read_text())
            m.step(loaded, {"ISF.L": quote(last_start="07:35:00", observed="07:41:00")}, {}, at("07:41:00"))
            m.save_state(loaded, folder)
            self.assertEqual(loaded["buy_fills"], 1)
            self.assertEqual(len((Path(folder) / "events.jsonl").read_text().splitlines()), len(loaded["events"]))
            journal = (Path(folder) / "journal.md").read_text()
            self.assertIn("Recognition UTC", journal)
            self.assertIn("£100.0000", journal)

    def test_immutable_history_cannot_be_rewritten(self):
        with tempfile.TemporaryDirectory() as folder:
            state = seed_position()
            m.save_state(state, folder)
            state["events"][0]["reason"] = "a different historical reason"
            with self.assertRaisesRegex(ValueError, "Immutable"):
                m.save_state(state, folder)

    def test_exclusive_lock_blocks_overlapping_run(self):
        with tempfile.TemporaryDirectory() as folder:
            with m.exclusive_lock(folder):
                with self.assertRaisesRegex(RuntimeError, "already active"):
                    with m.exclusive_lock(folder):
                        pass

    def test_corrupt_accounting_not_saved(self):
        state = seed_position()
        state["cash_gbp"] += 1
        with self.assertRaisesRegex(ValueError, "reconciliation|reconcile"):
            m.assert_accounting(state)



if __name__ == "__main__":
    unittest.main()
