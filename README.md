# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T10:05:05.000158+00:00 · 12325 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.25 (-0.76%)

Closed trades 33, win rate 66.7%, fees £1.04, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, GME 12%, BPRE 12%, PAM 12%, CX 12%, GPUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 7500 decisions in 1500 calls, $0.1052 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T10:05 | 2 / 2 / 1 | XRP-USD 16%, AMZN 18%, COIN 18%, MSTR 17% |  |
| Breezy | 2026-10-05T10:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T10:05 | 2 / 3 / 0 | MSTR 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.58 | +4.45% | 4 |
| VWAP reversion | AMZN | 1.94 | +0.87% | 3 |
| Z-score reversion | SQQQ | 1.74 | +3.40% | 6 |
| RSI(14) reversion | SQQQ | 1.71 | +3.09% | 4 |
| VWAP reversion | SQQQ | 1.63 | +1.18% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Hold BTC | benchmark | 102.90 | 2.90 | 0 | — | 34.66 | 4.17 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.25 | 2.25 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.12 | 2.12 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.08 | 1.08 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.01 | 1.01 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.93 | 0.93 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.93 | 0.93 | 53 | 37.7 | -21.96 | -4.97 | -24.32 | 486 |
| 8 | RSI(14) reversion · 1h | reversion | 100.63 | 0.64 | 11 | 63.6 | 4.95 | 1.41 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.17 | 0.17 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 13 | Z-score reversion · 1h | reversion | 99.82 | -0.18 | 20 | 55.0 | 6.66 | 1.50 | -8.60 | 157 |
| 14 | Bollinger reversion · 1h | reversion | 99.79 | -0.21 | 42 | 42.9 | -14.21 | -3.75 | -17.08 | 303 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.76 | -0.24 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.73 | -0.28 | 17 | 0.0 | 6.03 | 0.96 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.68 | -0.32 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.53 | -0.47 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.01 | -0.99 | 45 | 60.0 | -8.10 | -1.66 | -9.82 | 328 |
| 23 | CCI reversion · 1h | reversion | 98.95 | -1.05 | 63 | 49.2 | 2.54 | 0.58 | -12.41 | 410 |
| 24 | Trend pullback · 1h | trend | 98.87 | -1.13 | 50 | 22.0 | -21.31 | -5.41 | -25.34 | 161 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.79 | -1.21 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.86 | -2.14 | 52 | 23.1 | -5.06 | -1.95 | -9.49 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.85 | -2.15 | 25 | 8.0 | 13.75 | 1.71 | -14.40 | 137 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.83 | -2.17 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Williams %R · 1h | reversion | 97.53 | -2.47 | 70 | 54.3 | -16.95 | -3.09 | -19.41 | 499 |
| 34 | Connors RSI(2) · 1h | reversion | 97.42 | -2.58 | 63 | 44.4 | -11.89 | -3.98 | -14.40 | 223 |
| 35 | Daily: Momentum burst | daily | 97.00 | -3.00 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.56 | -3.44 | 211 | 17.1 | 0.92 | 0.31 | -10.84 | 365 |
| 37 | Parabolic SAR · 1h | trend | 96.30 | -3.70 | 53 | 17.0 | -5.57 | -0.61 | -19.70 | 307 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.50 | -1.44 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.19 | -3.81 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 96.01 | -3.99 | 29 | 10.3 | 3.35 | 0.63 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.89 | -4.11 | 6 | 50.0 | -19.54 | -3.87 | -21.08 | 70 |
| 43 | ADX DI cross · 1h | trend | 95.73 | -4.27 | 41 | 12.2 | -5.14 | -0.70 | -13.84 | 270 |
| 44 | MACD cross · 1h | trend | 95.60 | -4.40 | 79 | 19.0 | -11.42 | -1.77 | -17.27 | 473 |
| 45 | Squeeze breakout · 1h | breakout | 95.35 | -4.65 | 26 | 19.2 | 20.30 | 2.90 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.30 | -5.70 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 94.02 | -5.98 | 41 | 2.4 | 2.50 | 0.52 | -16.65 | 229 |
| 49 | Bollinger breakout · 1h | breakout | 93.31 | -6.69 | 43 | 25.6 | 6.56 | 1.02 | -12.06 | 296 |
| 50 | Triple EMA stack · 1h | trend | 93.18 | -6.82 | 51 | 9.8 | -7.70 | -0.73 | -23.88 | 244 |
| 51 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 52 | VWAP momentum · 1h | momentum | 92.71 | -7.29 | 184 | 22.8 | -38.71 | -6.04 | -38.71 | 1277 |
| 53 | Volume breakout · 1h | breakout | 92.55 | -7.45 | 30 | 6.7 | 2.82 | 0.57 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 91.84 | -8.16 | 70 | 12.9 | -3.05 | -0.22 | -18.47 | 341 |
| 55 | Max aggression: 5-day momentum | meta | 91.35 | -8.65 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 91.03 | -8.97 | 32 | 15.6 | -0.03 | 0.21 | -16.18 | 224 |
| 57 | MACD zero-line · 1h | trend | 90.89 | -9.11 | 42 | 16.7 | -3.33 | -0.22 | -18.32 | 236 |
| 58 | Three white soldiers | momentum | 90.65 | -9.35 | 78 | 14.1 | -49.69 | -26.13 | -50.01 | 594 |
| 59 | Heikin-Ashi · 1h | trend | 90.40 | -9.60 | 98 | 25.5 | -32.21 | -5.63 | -33.94 | 687 |
| 60 | OBV trend · 1h | momentum | 89.51 | -10.49 | 97 | 11.3 | -12.50 | -1.36 | -26.59 | 338 |
| 61 | Keltner breakout · 1h | breakout | 88.24 | -11.77 | 27 | 7.4 | -11.28 | -1.33 | -23.22 | 217 |
| 62 | ROC + volume · 1h | momentum | 87.05 | -12.95 | 91 | 15.4 | -10.04 | -1.23 | -23.26 | 419 |
| 63 | RSI(14) reversion | reversion | 86.16 | -13.84 | 190 | 32.6 | -70.54 | -19.75 | -70.66 | 1423 |
| 64 | VWAP reversion | reversion | 78.74 | -21.26 | 222 | 27.9 | -69.78 | -16.91 | -69.95 | 1365 |
| 65 | Squeeze breakout | breakout | 78.34 | -21.66 | 212 | 13.7 | -61.97 | -18.55 | -63.10 | 1232 |
| 66 | ROC + volume | momentum | 77.52 | -22.48 | 274 | 19.0 | -73.58 | -17.64 | -74.30 | 1670 |
| 67 | Donchian 55/20 | breakout | 77.49 | -22.52 | 209 | 16.3 | -69.00 | -15.40 | -69.53 | 1317 |
| 68 | EMA 20/50 cross | trend | 76.45 | -23.55 | 228 | 18.0 | -78.99 | -16.57 | -79.11 | 1487 |
| 69 | Volume breakout | breakout | 76.05 | -23.95 | 187 | 11.8 | -64.54 | -19.94 | -64.66 | 916 |
| 70 | Z-score reversion | reversion | 75.06 | -24.95 | 301 | 28.2 | -84.77 | -25.52 | -84.92 | 2079 |
| 71 | MFI reversion | reversion | 72.46 | -27.54 | 301 | 20.3 | -87.61 | -31.94 | -87.67 | 2112 |
| 72 | Supertrend | trend | 71.73 | -28.27 | 309 | 19.7 | -87.32 | -23.03 | -87.49 | 1947 |
| 73 | AI bee: Bizzy | ai | 68.95 | -31.05 | 528 | 7.8 | — | — | — | — |
| 74 | Keltner breakout | breakout | 68.47 | -31.53 | 308 | 11.4 | -85.97 | -32.16 | -85.99 | 1917 |
| 75 | ADX DI cross | trend | 68.38 | -31.62 | 333 | 9.3 | -89.50 | -38.32 | -89.54 | 2105 |
| 76 | Ichimoku | trend | 67.98 | -32.02 | 275 | 8.0 | -82.59 | -25.27 | -82.87 | 1796 |
| 77 | AI bee: Boozy | ai | 66.39 | -33.61 | 207 | 3.9 | — | — | — | — |
| 78 | MACD zero-line | trend | 65.83 | -34.17 | 387 | 14.7 | -91.95 | -32.61 | -91.99 | 2382 |
| 79 | Donchian 20/10 | breakout | 64.98 | -35.02 | 409 | 16.9 | -91.32 | -28.10 | -91.43 | 2702 |
| 80 | RSI momentum | momentum | 63.54 | -36.46 | 391 | 14.1 | -90.98 | -28.16 | -90.98 | 2415 |
| 81 | Triple EMA stack | trend | 62.05 | -37.95 | 442 | 14.3 | -93.70 | -34.79 | -93.70 | 2669 |
| 82 | Trend pullback | trend | 61.80 | -38.20 | 410 | 13.9 | -91.64 | -32.68 | -91.64 | 2369 |
| 83 | Bollinger breakout | breakout | 61.46 | -38.54 | 425 | 13.6 | -94.20 | -37.79 | -94.23 | 2871 |
| 84 | Stochastic reversion | reversion | 61.33 | -38.67 | 596 | 22.5 | -95.62 | -39.57 | -95.66 | 4047 |
| 85 | Bollinger reversion | reversion | 60.63 | -39.37 | 558 | 16.3 | -95.66 | -38.38 | -95.67 | 3690 |
| 86 | Consensus | meta | 58.83 | -41.17 | 400 | 8.2 | -94.49 | -27.90 | -94.50 | 2649 |
| 87 | EMA 9/21 cross | trend | 57.90 | -42.10 | 550 | 16.0 | -97.54 | -37.61 | -97.54 | 3584 |
| 88 | Connors RSI(2) | reversion | 56.82 | -43.18 | 527 | 15.4 | -96.66 | -37.53 | -96.66 | 3665 |
| 89 | CCI reversion | reversion | 55.75 | -44.25 | 561 | 15.0 | -98.44 | -42.46 | -98.45 | 4713 |
| 90 | Candlestick reversal | reversion | 55.19 | -44.81 | 667 | 14.4 | -99.29 | -42.39 | -99.29 | 5629 |
| 91 | VWAP momentum | momentum | 54.32 | -45.68 | 626 | 8.8 | -98.69 | -33.85 | -98.70 | 5349 |
| 92 | OBV trend | momentum | 54.13 | -45.87 | 620 | 13.7 | -96.47 | -43.45 | -96.49 | 3671 |
| 93 | Parabolic SAR | trend | 52.81 | -47.19 | 566 | 12.9 | -97.41 | -45.95 | -97.42 | 3716 |
| 94 | MACD cross | trend | 50.98 | -49.02 | 650 | 13.1 | -99.73 | -51.48 | -99.73 | 6197 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -47.34 | -99.50 | 6136 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -58.88 | -99.90 | 8365 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T10:05 | Agent (ML meta-label) | buy | DOGE-USD | 4.02 | — | following Stochastic reversion · 1h |
| 2026-10-05T10:05 | Agent (ML meta-label) | sell | SOL-USD | 4.33 | -0.07 | selected signal exited |
| 2026-10-05T10:05 | CCI reversion | buy | SOL-USD | 2.78 | — | rebalance up |
| 2026-10-05T10:05 | CCI reversion | sell | XRP-USD | 2.78 | -0.01 | rebalance down |
| 2026-10-05T10:05 | Bollinger reversion | sell | XRP-USD | 15.11 | -0.10 | exit signal |
| 2026-10-05T10:05 | VWAP momentum | buy | DOGE-USD | 13.59 | — | entry signal |
| 2026-10-05T10:05 | MACD cross | buy | XRP-USD | 12.76 | — | entry signal |
| 2026-10-05T10:03 | AI bee: Bizzy | buy | XRP-USD | 10.84 | — | Jev: buy (buy p=0.63) |
| 2026-10-05T10:00 | ROC + volume · 1h | sell | DOGE-USD | 7.83 | -0.09 | exit signal |
| 2026-10-05T10:00 | VWAP momentum · 1h | sell | DOGE-USD | 22.52 | -0.26 | exit signal |
| 2026-10-05T10:00 | MACD cross · 1h | sell | DOGE-USD | 7.28 | -0.09 | exit signal |
| 2026-10-05T09:55 | MFI reversion | buy | SOL-USD | 18.11 | — | entry signal |
| 2026-10-05T09:55 | Candlestick reversal | buy | BTC-USD | 13.81 | — | entry |
| 2026-10-05T09:55 | Candlestick reversal | sell | ETH-USD | 13.76 | -0.10 | exit signal |
| 2026-10-05T09:42 | CCI reversion | buy | SOL-USD | 2.79 | — | rebalance up |
| 2026-10-05T09:42 | CCI reversion | sell | ETH-USD | 2.79 | -0.02 | rebalance down |
| 2026-10-05T09:40 | CCI reversion | buy | SOL-USD | 2.85 | — | entry signal |
| 2026-10-05T09:40 | CCI reversion | buy | BTC-USD | 11.16 | — | entry signal |
| 2026-10-05T09:40 | Connors RSI(2) | sell | DOGE-USD | 14.13 | -0.12 | exit signal |
| 2026-10-05T09:40 | Candlestick reversal | buy | SOL-USD | 13.84 | — | entry signal |
| 2026-10-05T09:40 | Candlestick reversal | buy | DOGE-USD | 13.84 | — | entry signal |
| 2026-10-05T09:35 | CCI reversion | buy | XRP-USD | 13.95 | — | entry signal |
| 2026-10-05T09:35 | Stochastic reversion | buy | DOGE-USD | 15.32 | — | entry signal |
| 2026-10-05T09:35 | Supertrend | sell | ETH-USD | 17.95 | -0.10 | exit signal |
| 2026-10-05T09:30 | Consensus | sell | DOGE-USD | 14.62 | -0.21 | target is flat |
| 2026-10-05T09:30 | Donchian 55/20 | sell | DOGE-USD | 15.44 | -0.19 | stop-loss |
| 2026-10-05T09:30 | RSI momentum | sell | DOGE-USD | 12.73 | -0.05 | exit signal |
| 2026-10-05T09:30 | VWAP momentum | sell | ETH-USD | 13.53 | -0.10 | exit signal |
| 2026-10-05T09:30 | VWAP momentum | sell | DOGE-USD | 10.96 | -0.08 | exit signal |
| 2026-10-05T09:30 | Trend pullback | sell | DOGE-USD | 15.34 | -0.22 | exit signal |
| 2026-10-05T09:30 | Supertrend | sell | DOGE-USD | 14.37 | -0.05 | exit signal |
| 2026-10-05T09:30 | Triple EMA stack | sell | DOGE-USD | 12.41 | -0.14 | exit signal |
| 2026-10-05T09:30 | EMA 20/50 cross | sell | ETH-USD | 19.12 | -0.22 | stop-loss |
| 2026-10-05T09:30 | EMA 9/21 cross | sell | DOGE-USD | 11.60 | -0.04 | exit signal |
| 2026-10-05T09:25 | MFI reversion | buy | XRP-USD | 18.15 | — | entry signal |
| 2026-10-05T09:25 | MFI reversion | buy | BTC-USD | 18.15 | — | entry signal |
| 2026-10-05T09:25 | CCI reversion | buy | DOGE-USD | 13.97 | — | entry signal |
| 2026-10-05T09:25 | Stochastic reversion | buy | XRP-USD | 15.34 | — | entry signal |
| 2026-10-05T09:25 | Bollinger reversion | buy | BTC-USD | 15.17 | — | entry signal |
| 2026-10-05T09:25 | VWAP momentum | buy | ETH-USD | 13.63 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 10:05:05.000158+00:00 -> 2026-10-05 10:15:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
