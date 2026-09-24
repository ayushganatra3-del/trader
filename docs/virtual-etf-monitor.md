# Legacy: Sterling Trading Lab virtual ETF monitor (GPT-built)

A private research website and a cloud-run **virtual-money** stock-market experiment. The monitor records hypothetical ETF buys, sells, costs, cash and profit/loss using delayed public market data. It does not send orders to a broker, handle money or promise returns.

- [Open the private website](https://sterling-trading-lab.ayushganny.chatgpt.site)
- [Open cloud controls and run history](https://github.com/ayushganatra3-del/trader/actions/workflows/virtual-trading.yml)
- [Read the durable virtual ledger](https://github.com/ayushganatra3-del/trader/tree/trading-state/data)

**This GitHub repository is public.** Source code, workflow logs and virtual portfolio records on every branch are public. The website retains its private access settings; that does not make these GitHub records private. Never commit broker credentials, private account information, environment files or personal notes.

## What runs in the cloud

| Component | Location | Purpose |
| --- | --- | --- |
| Research website | Sites, source in `trading-lab/` | Strategy research, backtests and the virtual-session dashboard |
| Virtual monitor | GitHub-hosted Actions, code in `cloud/` | One bounded observation and accounting update per run |
| Durable ledger | `trading-state` branch, `data/` | Controls, sessions, events, market snapshots and dashboard data |
| Research records | Site-backed database | Website records stored separately from the trading ledger |

The website reads the public `data/dashboard.json` from `trading-state`; no GitHub secret is needed for this read-only view. It does not execute trades when someone opens the page. Actions uses its short-lived repository token to save state. There is no dependency on an open laptop, a browser tab or the Codex desktop app.

The original **10 September 2026** experiment remains historical and incomplete: missing quotes prevented the final EQQQ sale. Importing it does not fabricate that sale, reset its balance or resume its trading.

## Start, check or stop a session

Open **Actions → Virtual trading → Run workflow**, leave the branch set to **main**, and choose:

| Action | Date field | Effect |
| --- | --- | --- |
| `check` | Leave blank | Observe an existing active session; otherwise refresh the idle dashboard. Never creates a session. |
| `start` | Explicit `YYYY-MM-DD` | Request one dated virtual session. The runner validates the date and rejects resets or conflicting sessions. |
| `stop` | Leave blank | Stop new entries and request exits under the simulation's valid-price rules. It cannot invent an immediate closing price. |

No new session starts merely because code was deployed or a scheduled check ran. Starting a session authorizes only its selected day; the runner does not roll over to tomorrow. Review the completed workflow and dashboard for confirmation rather than assuming a button click succeeded.

Choose today or a weekday within the next seven days. Today's start must be before 15:45 London time. Market holidays are handled by rejecting missing or wrong-day quotes; the runner does not include a separate holiday calendar. A manual `check` also runs an independent price-access diagnostic using temporary files; a failed diagnostic is shown in the workflow without changing the portfolio.

Checks are scheduled at minutes **07, 22, 37 and 52**, between **08:00 and 17:59 London time**, Monday–Friday. Session rules determine whether a check may make a decision, reconcile a pending fill, or only finish the journal. The extra checks after the close allow delayed-data reconciliation. An idle monitor stays idle.

GitHub scheduling is approximate: runs can be delayed or dropped during high load. Scheduled workflows run from the default branch; public repositories can have schedules disabled after 60 days without repository activity. A missed check is a gap, never permission to replay an earlier decision. [GitHub schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## Simulation rules and limitations

- A new session starts with **£100 virtual cash**, with at most two positions, £40 per entry and six buys per session. Fractional units are assumed; no borrowing or short sales.
- Instruments: `ISF.L`, `VUSA.L`, `EQQQ.L`. Prices are normalized to GBP, including sources quoted in pence.
- Signals use the fixed VWAP/momentum rules in `cloud/engine.py`. Entry and exit costs are modelled as a 0.10% adverse price adjustment per fill; actual brokerage fees and execution may differ.
- A decision is recorded at the actual observation time. A later check can fill it only from a complete five-minute bar starting after the recorded decision. Decision, effective fill and recognition times remain distinct.
- No new entries after **15:45 London time**; liquidation requests begin at **16:15**; final reconciliation is at the first check at or after **17:00**. Missing valid closing data leaves the result explicitly incomplete.
- Delayed quotes, source errors and missing observations preserve existing holdings and are logged. Last known values must not be interpreted as executable live prices.
- The per-session loss halt requests exits; it cannot guarantee a maximum loss. Backtests and a short virtual experiment are not evidence of reliable future profits.

## Persistence and recovery

The `trading-state` branch is authoritative. `data/control.json` controls the active session; `data/sessions/<date>/` contains the session ledger and source evidence; `data/dashboard.json` is a derived website view. Event IDs distinguish completed fills from pending intentions. Event notes remain in this cloud archive; an offline Mac's local memory folder is not automatically synchronized.

All monitor triggers share one concurrency group and do not cancel an executing check. Up to 100 pending runs can queue, so a later scheduled check does not replace a pending manual control. Each run checks out code and state into separate folders, then saves changed state even when the monitor reports an error. A missing state branch or control file is a failure, not a reason to create a fresh balance. [GitHub concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).

State commits use a normal push. A rejected push fails the workflow; it never force-pushes or silently recomputes decisions. A failed run attempts to upload a **14-day recovery artifact** containing its resulting state and execution output. If saving fails, pause the workflow and compare that artifact with the branch before another trading check. Preserve recorded events; do not replay missed trades, replace the branch blindly or reset balances. If the runner is terminated before artifact upload, only the last successfully pushed state is durable.

Provider-data gaps can be a successfully saved check with alerts. A green workflow means the run and save completed; it does not mean prices were fresh, a sale filled or the strategy made money. The dashboard and journal carry those distinctions.

## Development and deployment

Requirements: Node.js 22.13 or later and Python 3.11 or later. The cloud monitor uses the Python standard library. Website dependencies are locked in `trading-lab/package-lock.json`.

From the repository root:

```sh
python3 -m unittest discover -s cloud -p 'test_*.py' -v
cd trading-lab
npm ci --no-audit --no-fund
npm test
npm run typecheck
npm run build
```

The **Checks** workflow runs the same offline Python checks and website tests, type checks and build. Official GitHub Actions are pinned to immutable release commits. The virtual workflow grants only the repository `contents: write` permission it needs; the test workflow has read-only repository permission. [GitHub token permissions](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token).

Website publication remains managed through Sites using `trading-lab/.openai/hosting.json`. A GitHub push runs checks; it does **not** by itself publish a new website version. Keep the Site's private audience and configure any runtime values through Sites. The cloud virtual workflow has no broker secrets and does not invoke the separate broker-paper scripts shipped with the research app.
