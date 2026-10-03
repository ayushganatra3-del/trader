# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T21:05:05.000142+00:00 · 10454 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.24 (-0.76%)

Closed trades 32, win rate 65.6%, fees £0.92, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, ETRA 12%, BBD 12%, BPRE 12%, GME 12%, NYAX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 15552 decisions in 3111 calls, $0.2175 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T21:05 | 0 / 2 / 3 | AMZN 16%, COIN 16%, MSTR 16% |  |
| Breezy | 2026-10-03T21:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T21:05 | 1 / 4 / 0 | MSTR 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion · 1h | UPRO | 2.43 | +6.89% | 3 |
| Stochastic reversion · 1h | SPY | 2.28 | +2.53% | 3 |
| Connors RSI(2) · 1h | COIN | 2.23 | +6.43% | 5 |
| Stochastic reversion | MSFT | 2.20 | +2.95% | 13 |
| RSI(14) reversion | SQQQ | 2.18 | +4.27% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.27 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 101.24 | 1.24 | 0 | — | 32.70 | 4.02 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.00 | -2.92 | -14.05 | 113 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.91 | -5.48 | -26.27 | 496 |
| 8 | RSI(14) reversion · 1h | reversion | 100.58 | 0.58 | 10 | 60.0 | 5.01 | 1.44 | -6.57 | 122 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.82 | -3.95 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.75 | -0.25 | 18 | 55.6 | 5.61 | 1.29 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 5.99 | 0.96 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.01 | -0.99 | 44 | 59.1 | -8.09 | -1.67 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.49 | 0.41 | -12.41 | 416 |
| 24 | Trend pullback · 1h | trend | 98.79 | -1.21 | 46 | 19.6 | -21.45 | -5.48 | -25.34 | 155 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.89 | -2.11 | 50 | 20.0 | -4.88 | -1.87 | -9.74 | 234 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.91 | 1.74 | -14.40 | 134 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -11.64 | -3.92 | -14.21 | 221 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.72 | -3.06 | -19.41 | 499 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | -0.86 | -0.01 | -13.20 | 348 |
| 37 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -6.16 | -0.70 | -19.70 | 304 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.60 | 2.81 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -7.69 | -1.29 | -16.99 | 124 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 3.38 | 0.64 | -16.43 | 197 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.87 | -3.78 | -21.08 | 69 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -6.18 | -0.88 | -13.84 | 275 |
| 44 | MACD cross · 1h | trend | 95.48 | -4.52 | 71 | 15.5 | -14.28 | -2.29 | -17.27 | 485 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.61 | 0.41 | -16.65 | 227 |
| 49 | Triple EMA stack · 1h | trend | 93.10 | -6.90 | 50 | 8.0 | -7.52 | -0.71 | -23.88 | 241 |
| 50 | Bollinger breakout · 1h | breakout | 93.10 | -6.90 | 36 | 16.7 | 6.30 | 1.00 | -12.06 | 292 |
| 51 | VWAP momentum · 1h | momentum | 93.08 | -6.92 | 176 | 22.2 | -41.11 | -6.49 | -41.92 | 1287 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.04 | 0.61 | -12.60 | 127 |
| 54 | EMA 9/21 cross · 1h | trend | 91.69 | -8.31 | 68 | 11.8 | -4.24 | -0.39 | -18.47 | 340 |
| 55 | Three white soldiers | momentum | 91.29 | -8.71 | 74 | 14.9 | -49.54 | -26.28 | -49.65 | 594 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | MACD zero-line · 1h | trend | 90.78 | -9.22 | 38 | 13.2 | -4.00 | -0.31 | -18.32 | 234 |
| 58 | Donchian 20/10 · 1h | breakout | 90.53 | -9.47 | 31 | 12.9 | -0.28 | 0.18 | -16.18 | 223 |
| 59 | Heikin-Ashi · 1h | trend | 90.51 | -9.49 | 91 | 24.2 | -33.09 | -5.88 | -33.65 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -13.00 | -1.44 | -26.45 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.02 | -1.30 | -23.19 | 212 |
| 62 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -10.86 | -1.37 | -23.16 | 417 |
| 63 | RSI(14) reversion | reversion | 87.07 | -12.93 | 181 | 34.3 | -72.54 | -20.41 | -72.54 | 1458 |
| 64 | Squeeze breakout | breakout | 81.22 | -18.77 | 186 | 15.1 | -60.87 | -18.52 | -61.74 | 1214 |
| 65 | Donchian 55/20 | breakout | 80.51 | -19.49 | 183 | 17.5 | -68.56 | -15.47 | -68.62 | 1309 |
| 66 | ROC + volume | momentum | 79.60 | -20.40 | 259 | 20.1 | -73.37 | -17.66 | -73.92 | 1667 |
| 67 | VWAP reversion | reversion | 79.43 | -20.57 | 213 | 28.6 | -71.22 | -17.31 | -71.29 | 1387 |
| 68 | Volume breakout | breakout | 78.97 | -21.03 | 164 | 13.4 | -64.00 | -19.92 | -64.00 | 908 |
| 69 | EMA 20/50 cross | trend | 77.93 | -22.07 | 208 | 17.3 | -79.17 | -16.89 | -79.26 | 1489 |
| 70 | Z-score reversion | reversion | 76.66 | -23.34 | 285 | 29.8 | -85.59 | -26.87 | -85.59 | 2107 |
| 71 | MFI reversion | reversion | 74.79 | -25.21 | 278 | 21.6 | -88.05 | -33.32 | -88.05 | 2124 |
| 72 | AI bee: Bizzy | ai | 74.72 | -25.28 | 447 | 9.2 | — | — | — | — |
| 73 | Keltner breakout | breakout | 74.13 | -25.87 | 261 | 13.0 | -85.43 | -32.33 | -85.43 | 1899 |
| 74 | Ichimoku | trend | 72.91 | -27.09 | 230 | 9.1 | -82.06 | -25.93 | -82.06 | 1778 |
| 75 | Supertrend | trend | 72.86 | -27.14 | 286 | 19.6 | -87.47 | -23.62 | -87.51 | 1953 |
| 76 | AI bee: Boozy ⏸ | ai | 72.08 | -27.92 | 170 | 4.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 70.15 | -29.85 | 315 | 9.8 | -89.78 | -41.23 | -89.78 | 2119 |
| 78 | Donchian 20/10 | breakout | 69.05 | -30.95 | 369 | 18.2 | -91.13 | -28.42 | -91.13 | 2691 |
| 79 | MACD zero-line | trend | 68.83 | -31.17 | 357 | 16.0 | -91.86 | -32.70 | -91.86 | 2379 |
| 80 | Trend pullback | trend | 68.03 | -31.97 | 342 | 15.8 | -91.75 | -33.26 | -91.75 | 2361 |
| 81 | Bollinger breakout | breakout | 66.87 | -33.13 | 370 | 15.1 | -94.01 | -38.26 | -94.01 | 2851 |
| 82 | RSI momentum | momentum | 66.72 | -33.28 | 352 | 14.8 | -90.97 | -28.23 | -90.97 | 2411 |
| 83 | Triple EMA stack ⏸ | trend | 66.28 | -33.72 | 395 | 14.9 | -93.54 | -34.18 | -93.59 | 2655 |
| 84 | Stochastic reversion | reversion | 65.39 | -34.61 | 548 | 24.5 | -95.80 | -41.10 | -95.80 | 4068 |
| 85 | Consensus | meta | 65.02 | -34.98 | 337 | 9.2 | -94.23 | -28.20 | -94.23 | 2616 |
| 86 | Bollinger reversion | reversion | 64.09 | -35.91 | 523 | 17.4 | -95.87 | -39.88 | -95.87 | 3722 |
| 87 | Connors RSI(2) | reversion | 63.04 | -36.96 | 453 | 17.9 | -96.65 | -39.07 | -96.65 | 3667 |
| 88 | EMA 9/21 cross ⏸ | trend | 61.38 | -38.62 | 501 | 16.8 | -97.52 | -38.05 | -97.52 | 3578 |
| 89 | Candlestick reversal | reversion | 60.29 | -39.71 | 605 | 15.7 | -99.36 | -44.01 | -99.36 | 5676 |
| 90 | CCI reversion | reversion | 60.14 | -39.86 | 510 | 16.5 | -98.53 | -44.41 | -98.53 | 4737 |
| 91 | OBV trend ⏸ | momentum | 59.92 | -40.08 | 553 | 14.5 | -96.33 | -43.32 | -96.33 | 3648 |
| 92 | VWAP momentum | momentum | 59.09 | -40.91 | 559 | 8.9 | -98.65 | -34.02 | -98.65 | 5323 |
| 93 | Parabolic SAR ⏸ | trend | 57.56 | -42.44 | 513 | 13.8 | -97.27 | -47.38 | -97.27 | 3683 |
| 94 | MACD cross ⏸ | trend | 55.83 | -44.17 | 586 | 13.8 | -99.72 | -53.01 | -99.72 | 6177 |
| 95 | Williams %R ⏸ | reversion | 55.60 | -44.41 | 630 | 21.3 | -99.53 | -49.56 | -99.53 | 6156 |
| 96 | Heikin-Ashi ⏸ | trend | 54.73 | -45.27 | 544 | 9.2 | -99.90 | -61.46 | -99.90 | 8349 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T21:05 | Candlestick reversal | sell | BTC-USD | 15.01 | -0.10 | exit signal |
| 2026-10-03T21:05 | Donchian 20/10 | sell | ETH-USD | 17.23 | -0.11 | exit signal |
| 2026-10-03T21:05 | Donchian 20/10 | sell | DOGE-USD | 17.18 | -0.15 | stop-loss |
| 2026-10-03T21:05 | RSI momentum | sell | DOGE-USD | 16.61 | -0.15 | stop-loss |
| 2026-10-03T21:05 | Trend pullback | sell | XRP-USD | 16.93 | -0.12 | exit signal |
| 2026-10-03T21:05 | Supertrend | sell | DOGE-USD | 18.25 | -0.13 | exit signal |
| 2026-10-03T21:05 | MACD zero-line | sell | ETH-USD | 17.21 | -0.11 | exit signal |
| 2026-10-03T21:05 | Triple EMA stack | sell | XRP-USD | 16.55 | -0.12 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-03T21:05 | Triple EMA stack | sell | ETH-USD | 13.27 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-03T21:05 | Triple EMA stack | sell | DOGE-USD | 13.25 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-03T21:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.41 | — | entry |
| 2026-10-03T21:00 | VWAP momentum · 1h | sell | BTC-USD | 7.41 | -0.06 | exit signal |
| 2026-10-03T21:00 | Trend pullback · 1h | sell | BTC-USD | 3.25 | -0.02 | exit signal |
| 2026-10-03T21:00 | Connors RSI(2) | buy | ETH-USD | 15.79 | — | entry signal |
| 2026-10-03T21:00 | Connors RSI(2) | buy | DOGE-USD | 15.79 | — | entry signal |
| 2026-10-03T21:00 | Candlestick reversal | sell | XRP-USD | 15.11 | -0.09 | time stop |
| 2026-10-03T21:00 | Trend pullback | buy | XRP-USD | 17.05 | — | entry signal |
| 2026-10-03T21:00 | Trend pullback | sell | DOGE-USD | 17.02 | -0.11 | exit signal |
| 2026-10-03T21:00 | Ichimoku | sell | DOGE-USD | 18.18 | -0.13 | exit signal |
| 2026-10-03T21:00 | Triple EMA stack | sell | SOL-USD | 16.55 | -0.12 | exit signal |
| 2026-10-03T20:55 | Consensus | sell | SOL-USD | 16.19 | -0.13 | target is flat |
| 2026-10-03T20:55 | Bollinger reversion | buy | BTC-USD | 16.04 | — | entry signal |
| 2026-10-03T20:55 | Connors RSI(2) | buy | SOL-USD | 15.81 | — | entry signal |
| 2026-10-03T20:55 | Connors RSI(2) | buy | BTC-USD | 15.81 | — | entry signal |
| 2026-10-03T20:55 | Candlestick reversal | buy | BTC-USD | 15.11 | — | entry signal |
| 2026-10-03T20:55 | Donchian 20/10 | sell | SOL-USD | 13.89 | -0.09 | exit signal |
| 2026-10-03T20:55 | RSI momentum | sell | SOL-USD | 16.61 | -0.14 | stop-loss |
| 2026-10-03T20:55 | VWAP momentum | buy | XRP-USD | 3.20 | — | rebalance up |
| 2026-10-03T20:55 | VWAP momentum | sell | BTC-USD | 11.88 | -0.05 | exit signal |
| 2026-10-03T20:55 | Trend pullback | sell | XRP-USD | 16.99 | -0.11 | exit signal |
| 2026-10-03T20:55 | Trend pullback | sell | SOL-USD | 17.01 | -0.12 | exit signal |
| 2026-10-03T20:55 | MACD zero-line | sell | SOL-USD | 17.16 | -0.14 | exit signal |
| 2026-10-03T20:55 | MACD zero-line | sell | DOGE-USD | 17.19 | -0.11 | exit signal |
| 2026-10-03T20:50 | Consensus | sell | DOGE-USD | 16.18 | -0.12 | target is flat |
| 2026-10-03T20:50 | MFI reversion | sell | BTC-USD | 18.62 | -0.14 | stop-loss |
| 2026-10-03T20:50 | CCI reversion | sell | BTC-USD | 15.00 | -0.11 | stop-loss |
| 2026-10-03T20:50 | Connors RSI(2) | sell | BTC-USD | 15.73 | -0.11 | stop-loss |
| 2026-10-03T20:50 | Candlestick reversal | sell | SOL-USD | 15.04 | -0.10 | exit signal |
| 2026-10-03T20:50 | Bollinger breakout | sell | DOGE-USD | 16.63 | -0.13 | exit signal |
| 2026-10-03T20:50 | Ichimoku | sell | SOL-USD | 18.16 | -0.14 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
