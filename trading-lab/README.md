# Sterling Trading Lab

A private strategy-research app with five transparent backtests, a 16-family method catalogue, CSV import, chronological evaluation, a private cloud experiment journal, a cloud virtual-portfolio dashboard and optional Alpaca paper account monitoring.

It does not promise returns. £100 to £1,000,000 in 30 days is 10,000× capital, requiring 35.9356% compounded growth every calendar day. No live trading is implemented or connected. No broker order has been submitted as part of development. Synthetic examples are demonstrations, not historical performance.


## Cloud virtual portfolio

The default Cloud portfolio tab reads the committed virtual ledger from the public [trader repository](https://github.com/ayushganatra3-del/trader). GitHub Actions performs date-bound checks with no laptop dependency. Use the linked cloud controls to start one explicit date, check status or stop entries. The historical 10 September session stays incomplete. See the [repository operations guide](https://github.com/ayushganatra3-del/trader#readme) for cloud scheduling, state durability and recovery.

Research saves use the Site's DB binding and per-user ownership checks. Generated Drizzle migrations live in `drizzle/`. Reads and writes reject missing authenticated identity; writes also require the same origin. The hosted Site stays private. GitHub source and virtual-session records remain public, matching the supplied repository's existing visibility. The cloud virtual runner never calls the optional broker code below.

## Use the workspace

1. Start with a synthetic regime to understand the controls, or import consistently adjusted daily prices in `date,open,high,low,close` format.
2. Choose the imported price currency before import. The software does not perform FX conversion.
3. Set capital, allocation, one-way costs (10 bps = 0.10%), per-order fees and the closing-equity drawdown stop, then run the comparison.
4. Inspect the rule and every simulated order. The first 101 observations warm up the indicators.
5. Evaluate the final 30% only after choosing the rule. Viewing and then repeatedly tuning against it compromises the holdout.
6. Save the full experiment to your private cloud journal, including source prices and settings. Reopen it on another device, or export the JSON. An import button preserves summaries from the old browser journal.

The five rules are buy and hold, SMA(100) trend, 63-session absolute momentum, 20/10-session Donchian breakout and Wilder RSI(14) 30/50 mean reversion. All signals use a completed close and fill at the next available open. Open final positions are marked at the final close. A drawdown breach exits at the next open; a breach on the final bar stays pending. Gaps can exceed the stop. Buy and hold uses the same allocation and stop as the other rules, so it is a matched-control benchmark, not an unrestricted fully invested index return.

Real-world taxes, FX charges, market impact, liquidity, intraday execution, borrow, financing and instrument-specific constraints are not fully modelled. Fractional quantities are assumed. Imported corporate actions and source provenance are the user's responsibility. Adjusted IEX history is an approximation, not a consolidated executable tape. No claim of statistical significance or live profitability is made.

## Connect the hosted paper account view

Create an Alpaca paper account at https://app.alpaca.markets/signup. Configure `APCA_API_KEY_ID` and `APCA_API_SECRET_KEY` as private runtime secrets in this Site. Never enter secrets in source code, browser storage or chat. This Site is deployed owner-private and the broker route requires the platform's authenticated-user header. Keep account access owner-private.

The hosted account route is GET-only and returns a reduced balance, position and order view. It cannot submit an order. It exposes no generic broker proxy. Trading and data endpoints are fixed to Alpaca paper and market-data hosts, redirects are rejected and responses are not cached. Market history explicitly uses IEX, daily bars and `adjustment=all` and excludes today's incomplete bar.

The credentials themselves may permit trading, despite the hosted interface using only read operations. A valid paper connection does not imply live broker approval or UK eligibility. No credentials are supplied in this checkout.

## Legacy optional paper-broker CLI (not the cloud virtual runner)

Requires Node.js 22.13+ and a dedicated Alpaca paper account, preferably reset to $100 simulated cash. USD is separate from the app's £100 synthetic example; no GBP conversion is implied. A paper balance over $125 is deliberately rejected so a $100,000 default account cannot obscure the experiment's scale.

```sh
npm install
cp .env.example .env.local
```

Enter your paper credentials in the ignored `.env.local` file. Then:

```sh
npm run paper:check
```

This runs one decision without submitting orders. Start paper execution only when ready:

```sh
npm run paper:run
```

Stop with Ctrl+C. The process must stay running and the computer awake; the webpage does not run, supervise or schedule it. No automation was started during development.

Default: SPY, 100-session trend, at most $5 per entry, $25 maximum proposed position exposure, no leverage, one ordinary strategy action per New York day. Symbols are allowlisted (SPY, AAPL, MSFT). A separate emergency exit can follow a same-day entry when the $2 loss trigger trips. This is not a guaranteed loss ceiling. The baseline is equity at the first observation of that session, persisted across restarts; do not deposit, withdraw or trade manually during a session.

The runner uses a prior completed daily signal but may execute later in the regular session, so it does not replicate the backtest's next-open fill. It buys one bounded entry on an entry signal rather than matching a backtest's configurable portfolio percentage. The backtest's drawdown stop and the runner's $2 session loss trigger differ. Treat the runner as an execution experiment, not as a reproduction of a backtest return.

The fixed paper URL has no live override. Orders require active account and asset status, USD cash balances, regular market hours, a fresh IEX minute bar and no outstanding orders. Non-bot positions and short holdings are rejected. Daily signal data must be ordered and recent; the age guard is deliberately conservative but does not prove that a vendor omitted no session.

`.paper-state` stores the account-bound journal, persistent loss stops, pending intent and process lock. Do not delete it to get around a halt. An exclusive lock prevents two local runners using the same directory. Do not run multiple directories against the same account. Intent is atomically written and flushed before submission. A timeout or unknown outcome never triggers automatic resubmission; restart reconciles by the same client order ID. Broker acceptance is not a fill. Reconcile unknown orders using the broker dashboard before any manual recovery. For a stale lock after a crash, first verify the earlier process is stopped and review the journal; only then remove `runner.lock`, preserving `journal.json`.

## Development and checks

```sh
npm run dev
npm test
npm run typecheck
npm run build
```

Automated tests cover chronology, cash/cost accounting, RSI edge cases, impossible CSV prices/dates, final-bar stops, overnight gaps, cash-only paper checks, immutable paper host, credential absence, pending orders, intent persistence, duplicate prevention, timeout reconciliation, session loss halts, configuration/account mismatches and unavailable journals. These are deterministic and mocked tests, not provider end-to-end validation.

No browser UI testing was requested or performed. A feature-detected WebMCP backtest tool is included; no supported live WebMCP validation context was available. It exposes no broker actions.

## Sources

The app links each strategy family to primary material. Key limitations and references:

- FCA risk and returns: https://www.fca.org.uk/investsmart/risk-returns
- CFTC hypothetical trading systems: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/fraudadv_tradingsystem.html
- Backtest overfitting research: https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf
- Alpaca paper-trading limitations: https://docs.alpaca.markets/us/docs/paper-trading
- Alpaca fractional orders: https://docs.alpaca.markets/us/docs/fractional-trading

Paper trading does not model every live cost or execution effect and cannot establish future profit.

## Validation record

34 automated tests and the TypeScript check passed after the cloud migration. The production build passed after upgrading React/RSC to 19.2.8 and the framework to vinext beta.9. Local HTTP checks returned 200 for the workspace, 401 for an unauthenticated account read and 405 for POST to the account route.

Dependency audit: no high/critical production-dependency findings remain. One low-severity finding concerns esbuild's Windows development server; this is not used by the hosted Worker. The scaffold's Cloudflare development tooling still reports five high-severity inherited findings (sharp/ws and their dependants) and should be updated before exposing a development server or deploying it in another environment. The private hosted Worker does not use those local development servers or image parsers. No live browser interaction or actual broker credentials were tested.
