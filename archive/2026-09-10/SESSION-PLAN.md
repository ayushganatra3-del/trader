# £100 virtual portfolio — 10 September 2026

User authorization: The user confirmed UK residence and explicitly requested a one-day, virtual-money trading experiment starting with £100, observation of stock markets, and memory of buys, sells and profit. This session makes no real or broker-paper orders and needs no account credentials.

## Rules fixed before the first trade

- Virtual starting cash: £100.00. GBP-denominated UK-listed stock-market ETFs only: iShares Core FTSE 100 (ISF.L), Vanguard S&P 500 (VUSA.L), Invesco EQQQ Nasdaq-100 (EQQQ.L).
- At most two positions, £40 cash per entry, fractional units assumed. No margin, shorting, derivatives, cash top-ups or changing the rules after seeing the result. At most six entries today.
- Observe public Yahoo Finance five-minute OHLCV bars, saving raw responses and fetch times. Prices can be delayed by roughly 15 minutes. Currency GBp/GBX is divided by 100; GBP is not.
- At least six completed bars are required. Buy candidates must close above their volume-weighted session typical price and above the close four five-minute bars earlier. Rank simultaneous candidates by that 20-minute change.
- Exit on an observed close 1% below entry reference, 2% above entry reference or below session VWAP. A stopped instrument cannot be rebought today; other exits require 30-minute cooldown.
- A £3 fall from the starting £100 of net marked equity halts new entries and requests exits. This is a trigger, not a guaranteed maximum loss.
- Every simulated fill includes an assumed adverse 0.10% price adjustment. No fixed commission. ETF taxes assumed zero for this toy experiment; actual broker charges, fractional eligibility and executable spreads are not modelled.

## Forward-only execution

A signal creates an intention at the time we actually observe it. A later check may fill it only at the open of the first subsequently observed complete five-minute bar whose start is at or after that intention time. An old price cannot be used to invent a past buy. The journal records the decision time, effective market fill time and later recognition time separately. These are hypothetical fills, not executable quotes.

Duplicate checks cannot duplicate a trade. Pending buys reserve cash. Stale, invalid or missing data block new activity. No assumption is made that unobserved stop crossings were filled. Quotes more than 25 minutes behind the check are rejected for current decisions. Previously recorded intentions may still be reconciled from verified completed bars later in the same session, even after the feed becomes too old for new decisions; this is delayed recognition of an existing decision, not permission to invent one.

## Today's schedule

Checks approximately every 15 minutes, only on 10 September 2026. London regular market hours are 08:00–16:30 BST. No entries after 15:45 BST; request liquidation at/after 16:15 BST, leaving time for delayed quotes. Reconcile through 17:00 BST. If no legitimate final fill is available, report unresolved exposure and an incomplete result rather than inventing an exit.

Local scheduled checks require the computer to be on and the desktop app running. Missed checks are not recreated as if they occurred. The schedule should stop after today's final report; no trade may be initiated on a later date.

## Records

- `state.json`: authoritative atomic accounting, pending intentions and immutable events.
- `snapshots/`: public market response evidence.
- `journal.md`: readable current portfolio and buy/sell log.
- `monitor.py`: one-check, virtual-only monitoring tool.
- Codex memory notes: starting authorization and summaries of actual simulated fills/final result. The journal is authoritative; a memory note must not invent activity.

Sources: https://query1.finance.yahoo.com/v8/finance/chart/ISF.L?range=1d&interval=5m ; https://www.lseg.com/en/media-centre/press-releases/2026/london-stock-exchange-to-launch-lse-24 ; https://learn.chatgpt.com/docs/automations?surface=app
