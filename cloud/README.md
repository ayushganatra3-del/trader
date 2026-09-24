# Virtual cloud runner

This is a one-shot Python 3.11+ process with no third-party dependencies. It simulates trades only; its only network operation is a public, read-only Yahoo Finance chart request. There are no broker credentials or order interfaces.

From the repository root:

```sh
python3 cloud/run.py --action check --data-dir data
python3 cloud/run.py --action start --date 2026-09-25 --data-dir data
python3 cloud/run.py --action stop --data-dir data
python3 cloud/probe.py
python3 -m unittest discover -s cloud -p 'test_*.py' -v
```

Choose a current or future weekday when starting. A date may be no more than seven calendar days ahead, and today's start must be before 15:45 Europe/London. Omit `--date` to select today on `start`. If supplied on `check` or `stop`, it must match the active date. An existing session can never be reset or restarted. Only an explicit `start` creates a new session; scheduled `check` runs are idle otherwise.

`start` persists £100 of virtual cash and selects the date without making market requests. `check` observes once after London open, reconciles already recorded intentions, and evaluates the fixed strategy. `stop` cancels unfilled buy intentions, halts new buys and records exit intentions using the actual stop time. Holdings stay visible until later valid bars support those exits. A flat stopped session closes immediately. Missing final fills produce an incomplete result, never invented cash proceeds. No operation resets balances or fills missed historical decisions.

The date and all market boundaries use the IANA `Europe/London` zone, so summer and winter offsets differ correctly. Rules remain fixed: ISF.L, VUSA.L and EQQQ.L; £40 entries; at most two holdings including pending buys; six entries at most; positive contiguous 20-minute momentum and close above session VWAP; close-based 1% stop, 2% take-profit, or below-VWAP exits; 10 basis points adverse cost per fill; a £3 equity-loss trigger halts entries. Fractional units, zero flat commission and zero ETF transaction taxes are modelling assumptions. This is not an executable quote or a profit guarantee.

Market data must be for the exact session, in GBP or explicitly quoted pence, with complete five-minute bars. A fill requires an already saved intention and a bar starting at or after its decision time. New price decisions require data no more than 25 minutes beyond the latest completed bar's end. Older valid same-session data may reconcile existing intentions. No entries are permitted from 15:45 London, exits queue from 16:15 and final reconciliation occurs on the first check at or after 17:00. If the calendar day has passed, the session expires without any market fetch or replay. Weekends cannot be started; there is no built-in holiday calendar, so a weekday closure is handled as missing/current-day-invalid data and cannot produce trades.

## Persistence contract

`--data-dir` must be durable between runs. GitHub Actions stores it on the dedicated data branch; a machine-local folder without persistence would not provide cloud continuity.

```text
data/
  control.json          # version: 1, active_session: YYYY-MM-DD or null
  dashboard.json        # complete read-only UI summary
  checks.jsonl          # every operation and saved data/runtime gaps
  notes/YYYY-MM-DD/     # deduplicated memory notes for fills/final outcomes
  sessions/YYYY-MM-DD/
    state.json          # authoritative atomic portfolio and immutable events
    events.jsonl        # derived event view
    journal.md          # readable accounting, fills, timestamps and sources
    checks.jsonl        # check results specific to this date
    snapshots/*.json    # immutable raw provider replies, hashes and fetch times
```

`dashboard.json` has `version: 1`, UTC `generated_at`, `control`, `last_check` and `sessions` sorted newest first. Each session contains its state plus `totals` (`cash_gbp`, `reserved_gbp`, `available_gbp`, `holdings_gbp`, `equity_gbp`, `realised_gbp`, `unrealised_gbp`, `total_pl_gbp`) and a relative `journal_path`. New snapshot sources are relative to the data directory. Historical imported sessions remain visible and are never selected automatically.

Cloud memory notes are created once per actual fill or finalisation event, named by event ID. They include original decision/fill/recognition times and label imported history explicitly. Pending intentions never get a fill note. These portable notes live in the repository's data branch, rather than requiring access to Codex memory on a particular computer.

`probe.py` checks the current London-day data source without reading or mutating any portfolio. It uses a temporary evidence directory that is deleted afterward, reports data availability/freshness for each symbol, and exits nonzero if any symbol is unavailable. A successful diagnostic is not a trade or proof of uninterrupted scheduled availability. Valid same-day after-hours bars can be reported as available but stale for new decisions.

Each run takes an exclusive filesystem lock. The workflow must also serialize cloud jobs because filesystem locks on separate runners cannot coordinate. State writes use atomic replacement and refuse changes to the existing event prefix. `events.jsonl`, journal and dashboard are derived from the committed state. A crash between files can leave a derived view behind the authoritative state; the next check rebuilds views when it saves that session. Preserve the entire data folder even on a failed run, and never resolve a data conflict by resetting state.

The process emits one JSON result. Idle, waiting, successful checks and safely recorded provider gaps exit 0; invalid actions/dates, broken accounting or runtime failures exit 1. Results expose `alerts` for missing price data and never imply that a pending intention filled. GitHub scheduling can be delayed or skipped; this model records those limitations rather than backdating activity. Unit tests inject clocks and snapshots and perform no network requests.
