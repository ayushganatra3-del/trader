# £100 virtual stock-market session — 10 September 2026

**Status:** incomplete. **Last check (UTC):** 2026-09-10T16:02:35.302212Z.

All amounts are virtual. No broker account, actual orders, deposits or real-money execution are involved.

| Measure | GBP |
|---|---:|
| Starting cash | £100.0000 |
| Cash | £59.7899 |
| Reserved for pending buys | £0.0000 |
| Available cash | £59.7899 |
| Open holdings at last valid mark | £39.9721 |
| Net equity | £99.7620 |
| Realised profit/loss | £-0.2101 |
| Unrealised profit/loss | £-0.0279 |
| Total profit/loss | £-0.2380 |

Buy fills: 3/6. New-entry halt: No.

## Open positions

| ETF | Units | Cost basis | Last mark | Mark bar end UTC | Mark observed UTC |
|---|---:|---:|---:|---|---|
| EQQQ.L | 0.07547177 | £40.0000 | £529.6300 | 2026-09-10T11:30:00.000000Z | 2026-09-10T11:45:45.980315Z |

## Pending or unresolved intentions

| ID | ETF | Action | Status | Decision UTC | Reason |
|---|---|---|---|---|---|
| 2026-09-10-0005 | EQQQ.L | sell | unresolved | 2026-09-10T11:32:10.366745Z | Close fell below session VWAP |

## Trade fills

A decision and a fill are different events. Effective fill time is the open of a later eligible five-minute bar; recognition time is when the delayed observation made the fill knowable.

| ETF / action | Units | Price incl. cost | Decision UTC | Effective fill UTC | Recognition UTC | Realised P/L | Reason |
|---|---:|---:|---|---|---|---:|---|
| VUSA.L buy | 0.37303126 | £107.2296 | 2026-09-10T08:46:43.828442Z | 2026-09-10T08:50:00.000000Z | 2026-09-10T09:16:34.019848Z | £0.0000 | Close above session VWAP and positive 20-minute return |
| VUSA.L sell | 0.37303126 | £106.9729 | 2026-09-10T09:16:34.019848Z | 2026-09-10T09:20:00.000000Z | 2026-09-10T09:47:05.943960Z | £-0.0958 | Close fell below session VWAP |
| VUSA.L buy | 0.37278766 | £107.2997 | 2026-09-10T10:35:16.778330Z | 2026-09-10T10:40:00.000000Z | 2026-09-10T11:02:36.999005Z | £0.0000 | Close above session VWAP and positive 20-minute return |
| EQQQ.L buy | 0.07547177 | £529.9995 | 2026-09-10T11:02:36.999005Z | 2026-09-10T11:05:00.000000Z | 2026-09-10T11:32:10.366745Z | £0.0000 | Close above session VWAP and positive 20-minute return |
| VUSA.L sell | 0.37278766 | £106.9929 | 2026-09-10T11:45:45.981259Z | 2026-09-10T11:50:00.000000Z | 2026-09-10T12:17:17.721803Z | £-0.1144 | Close fell below session VWAP |

## Quote freshness

| ETF | Status | Currency → GBP | Latest complete bar end UTC | Observed UTC | Delay after bar end | Source / issue |
|---|---|---|---|---|---|---|
| ISF.L | stale — existing-intent reconciliation only | GBp × 0.01 | 2026-09-10T15:30:00.000000Z | 2026-09-10T16:02:33.732546Z | 1953.7325460910797 seconds | sessions/2026-09-10/snapshots/20260910T160233.732546Z-ISF.L-60e7ffee50ea.json |
| VUSA.L | stale — existing-intent reconciliation only | GBP × 1.0 | 2026-09-10T15:30:00.000000Z | 2026-09-10T16:02:35.005790Z | 1955.0057899951935 seconds | sessions/2026-09-10/snapshots/20260910T160235.005790Z-VUSA.L-9f824ca14be1.json |
| EQQQ.L | unavailable | GBp × 0.01 | 2026-09-10T11:30:00.000000Z | 2026-09-10T11:45:45.980315Z | 945.9803149700165 seconds | ValueError: Invalid completed bar at 2026-09-10T11:35:00+00:00: Missing or nonnumeric market data |

## Fixed rules and accounting assumptions

- Session: 10 September 2026 only. London regular hours 08:00–16:30 BST (07:00–15:30 UTC). Each run observes once; missed checks do not create historical decisions.
- Read-only Yahoo Finance five-minute ETF charts: ISF.L, VUSA.L, EQQQ.L. These quotes may be delayed. Raw responses and real observation timestamps are preserved in snapshots/.
- Only complete bars from today's regular session are used. Future data, nonpositive prices, invalid volume and ambiguous currency are rejected. A bar must have ended according to both observation time and the provider market time. Data older than 25 minutes after the latest complete bar's end are used only to reconcile existing intentions, never for new price signals.
- Prices explicitly quoted in GBp or GBX are divided by 100; GBP prices are unchanged. No FX conversion is used.
- Buy signal: at least six completed session bars, close above volume-weighted HLC typical-price session VWAP, and close above the close four contiguous five-minute bars earlier. Candidates are ranked by that 20-minute return.
- Up to two cash-funded £40 fractional holdings including pending buys; no top-ups, leverage or short positions. Maximum six buy fills. Pending buys reserve cash.
- Each fill applies 10 basis points (0.10%) adverse price cost. No flat fee. ETF transaction tax is assumed zero for this simulation. Fractional ETF fills and bar-open liquidity are modelling assumptions, not executable broker quotes.
- A buy intent is saved before any fill. A fill requires a subsequently observed complete bar whose start is at or after the actual decision timestamp. Fill price is that first eligible bar's open, adjusted adversely for costs. No pre-decision price is used to fill.
- Exit signals: close at least 1% below the raw entry-bar open, at least 2% above it, or below session VWAP. Stops are signals, not guaranteed execution prices. Assets with stop signals cannot re-enter; other sold assets wait 30 minutes after exit recognition.
- A £3 net-equity loss halts new entries for the entire session and queues exits. Unrealised equity uses the latest valid observed close, without a hypothetical future sale cost; sale costs enter realised profit when a sale is recognised.
- No new buy decisions at or after 15:45 BST (14:45 UTC). Scheduled exits are queued on the first check at or after 16:15 BST (15:15 UTC). No buy fill may have an effective time at or after that cutoff. Pending buys with no eligible earlier fill are cancelled at the cutoff after reconciliation.
- Fills require a bar starting before the 16:30 BST regular close. At or after 17:00 BST (16:00 UTC), one final reconciliation finalises the session. Any unsold exposure stays visible as incomplete; no closing sale or final profit is invented.
- state.json is the atomic authoritative record. Its events list only grows; events.jsonl and this journal are derived views. An exclusive local lock prevents overlapping runs.

## Event sources

- event-000002, VUSA.L buy: sessions/2026-09-10/snapshots/20260910T091633.925621Z-VUSA.L-ddf14b2e9de0.json
- event-000004, VUSA.L sell: sessions/2026-09-10/snapshots/20260910T094705.841830Z-VUSA.L-7dc250145c1d.json
- event-000006, VUSA.L buy: sessions/2026-09-10/snapshots/20260910T110236.909471Z-VUSA.L-ef68e237804d.json
- event-000008, EQQQ.L buy: sessions/2026-09-10/snapshots/20260910T113210.364763Z-EQQQ.L-5dd0c5ca6580.json
- event-000011, VUSA.L sell: sessions/2026-09-10/snapshots/20260910T121717.571424Z-VUSA.L-54a1672fa2a3.json

**Incomplete close:** holdings remain valued at their last valid observed marks. This is not a fully realised end-of-day result.
