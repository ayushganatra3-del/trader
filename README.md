# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T19:05:05.000174+00:00 · 10356 ticks

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

Today: 14082 decisions in 2817 calls, $0.1969 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T19:05 | 0 / 1 / 4 | AMZN 16%, COIN 16%, MSTR 16% |  |
| Breezy | 2026-10-03T19:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T19:05 | 1 / 4 / 0 | MSTR 62% |  |

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
| 3 | Hold BTC | benchmark | 101.43 | 1.43 | 0 | — | 33.48 | 4.11 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -8.78 | -2.84 | -14.05 | 114 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -24.06 | -5.52 | -26.32 | 495 |
| 8 | RSI(14) reversion · 1h | reversion | 100.59 | 0.59 | 10 | 60.0 | 4.47 | 1.29 | -6.57 | 120 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.80 | -3.94 | -17.52 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.73 | -0.27 | 18 | 55.6 | 5.60 | 1.29 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 5.99 | 0.96 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.01 | -0.99 | 44 | 59.1 | -8.08 | -1.67 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.53 | 0.42 | -12.41 | 416 |
| 24 | Trend pullback · 1h | trend | 98.81 | -1.19 | 45 | 20.0 | -21.91 | -5.60 | -25.84 | 156 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.89 | -2.11 | 50 | 20.0 | -4.82 | -1.84 | -9.74 | 234 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.42 | 1.69 | -14.40 | 134 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -11.64 | -3.92 | -14.21 | 221 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.73 | -3.07 | -19.41 | 500 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 2.29 | 0.56 | -13.01 | 371 |
| 37 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -6.16 | -0.70 | -19.70 | 304 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.84 | 2.87 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -7.45 | -1.24 | -16.99 | 124 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 3.38 | 0.64 | -16.43 | 197 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.87 | -3.78 | -21.08 | 69 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -6.13 | -0.88 | -13.84 | 275 |
| 44 | MACD cross · 1h | trend | 95.47 | -4.53 | 71 | 15.5 | -13.72 | -2.20 | -17.27 | 483 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.28 | 0.37 | -16.65 | 228 |
| 49 | VWAP momentum · 1h | momentum | 93.14 | -6.86 | 175 | 22.3 | -41.18 | -6.51 | -41.92 | 1288 |
| 50 | Bollinger breakout · 1h | breakout | 93.11 | -6.89 | 36 | 16.7 | 6.31 | 1.00 | -12.06 | 292 |
| 51 | Triple EMA stack · 1h | trend | 93.10 | -6.90 | 50 | 8.0 | -7.69 | -0.74 | -23.88 | 241 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.24 | -4.58 | -18.91 | 695 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.04 | 0.61 | -12.60 | 127 |
| 54 | EMA 9/21 cross · 1h | trend | 91.70 | -8.30 | 68 | 11.8 | -4.95 | -0.48 | -18.47 | 343 |
| 55 | Three white soldiers | momentum | 91.29 | -8.71 | 74 | 14.9 | -49.54 | -26.28 | -49.65 | 594 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | MACD zero-line · 1h | trend | 90.78 | -9.22 | 38 | 13.2 | -3.94 | -0.31 | -18.32 | 234 |
| 58 | Heikin-Ashi · 1h | trend | 90.58 | -9.42 | 90 | 24.4 | -33.05 | -5.87 | -33.64 | 688 |
| 59 | Donchian 20/10 · 1h | breakout | 90.53 | -9.47 | 31 | 12.9 | -0.28 | 0.18 | -16.18 | 223 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -13.09 | -1.45 | -26.45 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.27 | -1.34 | -23.19 | 213 |
| 62 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -11.29 | -1.43 | -23.16 | 419 |
| 63 | RSI(14) reversion | reversion | 87.07 | -12.93 | 181 | 34.3 | -71.95 | -20.58 | -71.95 | 1451 |
| 64 | Squeeze breakout | breakout | 81.22 | -18.77 | 186 | 15.1 | -60.99 | -18.63 | -61.74 | 1216 |
| 65 | Donchian 55/20 | breakout | 80.57 | -19.43 | 182 | 17.6 | -68.56 | -15.47 | -68.62 | 1309 |
| 66 | ROC + volume | momentum | 79.60 | -20.40 | 259 | 20.1 | -73.50 | -17.78 | -73.91 | 1667 |
| 67 | VWAP reversion | reversion | 79.43 | -20.57 | 213 | 28.6 | -71.29 | -17.33 | -71.35 | 1386 |
| 68 | Volume breakout | breakout | 78.97 | -21.03 | 164 | 13.4 | -64.15 | -20.14 | -64.15 | 911 |
| 69 | EMA 20/50 cross | trend | 78.05 | -21.95 | 207 | 17.4 | -79.13 | -16.87 | -79.23 | 1488 |
| 70 | Z-score reversion | reversion | 76.66 | -23.34 | 285 | 29.8 | -85.74 | -26.74 | -85.74 | 2111 |
| 71 | MFI reversion | reversion | 75.08 | -24.92 | 276 | 21.7 | -88.03 | -33.35 | -88.03 | 2122 |
| 72 | AI bee: Bizzy | ai | 74.98 | -25.02 | 443 | 9.3 | — | — | — | — |
| 73 | Keltner breakout | breakout | 74.13 | -25.87 | 261 | 13.0 | -85.57 | -32.90 | -85.57 | 1905 |
| 74 | Ichimoku | trend | 73.23 | -26.77 | 228 | 9.2 | -81.98 | -25.91 | -81.98 | 1775 |
| 75 | Supertrend | trend | 73.12 | -26.88 | 284 | 19.7 | -87.44 | -23.63 | -87.47 | 1952 |
| 76 | AI bee: Boozy ⏸ | ai | 72.08 | -27.92 | 170 | 4.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 70.15 | -29.85 | 315 | 9.8 | -89.85 | -41.97 | -89.85 | 2121 |
| 78 | Donchian 20/10 | breakout | 69.36 | -30.64 | 366 | 18.3 | -91.15 | -28.68 | -91.15 | 2694 |
| 79 | MACD zero-line | trend | 69.27 | -30.73 | 354 | 16.1 | -91.83 | -32.71 | -91.83 | 2376 |
| 80 | Trend pullback | trend | 68.74 | -31.26 | 336 | 16.1 | -91.67 | -33.10 | -91.67 | 2355 |
| 81 | RSI momentum | momentum | 67.07 | -32.93 | 350 | 14.9 | -90.92 | -28.20 | -90.92 | 2408 |
| 82 | Bollinger breakout | breakout | 67.05 | -32.95 | 369 | 15.2 | -94.04 | -38.74 | -94.04 | 2854 |
| 83 | Triple EMA stack | trend | 66.80 | -33.20 | 390 | 15.1 | -93.49 | -34.33 | -93.54 | 2651 |
| 84 | Stochastic reversion | reversion | 65.70 | -34.30 | 544 | 24.6 | -95.80 | -41.01 | -95.80 | 4067 |
| 85 | Consensus | meta | 65.27 | -34.73 | 335 | 9.3 | -94.21 | -28.13 | -94.21 | 2616 |
| 86 | Bollinger reversion | reversion | 64.28 | -35.72 | 521 | 17.5 | -95.86 | -39.78 | -95.86 | 3720 |
| 87 | Connors RSI(2) | reversion | 63.72 | -36.27 | 447 | 18.1 | -96.62 | -38.87 | -96.62 | 3659 |
| 88 | EMA 9/21 cross | trend | 61.60 | -38.40 | 498 | 16.9 | -97.51 | -38.29 | -97.51 | 3576 |
| 89 | Candlestick reversal | reversion | 60.65 | -39.35 | 599 | 15.9 | -99.35 | -43.87 | -99.35 | 5670 |
| 90 | CCI reversion | reversion | 60.48 | -39.52 | 505 | 16.6 | -98.52 | -44.33 | -98.52 | 4734 |
| 91 | OBV trend ⏸ | momentum | 59.92 | -40.08 | 553 | 14.5 | -96.31 | -43.43 | -96.31 | 3645 |
| 92 | VWAP momentum | momentum | 59.32 | -40.68 | 556 | 9.0 | -98.65 | -34.25 | -98.65 | 5329 |
| 93 | Parabolic SAR ⏸ | trend | 57.56 | -42.44 | 513 | 13.8 | -97.27 | -47.87 | -97.27 | 3682 |
| 94 | Williams %R | reversion | 55.99 | -44.01 | 624 | 21.5 | -99.52 | -49.41 | -99.52 | 6152 |
| 95 | MACD cross ⏸ | trend | 55.83 | -44.17 | 586 | 13.8 | -99.72 | -53.05 | -99.72 | 6175 |
| 96 | Heikin-Ashi ⏸ | trend | 54.73 | -45.27 | 544 | 9.2 | -99.90 | -62.11 | -99.90 | 8351 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T19:05 | Connors RSI(2) | buy | BTC-USD | 15.94 | — | entry signal |
| 2026-10-03T19:05 | Donchian 55/20 | sell | BTC-USD | 20.07 | -0.15 | stop-loss |
| 2026-10-03T19:05 | OBV trend | sell | BTC-USD | 15.00 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-03T19:05 | RSI momentum | sell | SOL-USD | 13.45 | -0.08 | exit signal |
| 2026-10-03T19:05 | RSI momentum | sell | BTC-USD | 16.75 | -0.11 | exit signal |
| 2026-10-03T19:05 | Trend pullback | sell | SOL-USD | 17.33 | -0.10 | exit signal |
| 2026-10-03T19:05 | Trend pullback | sell | DOGE-USD | 17.14 | -0.12 | exit signal |
| 2026-10-03T19:05 | Trend pullback | sell | BTC-USD | 17.15 | -0.12 | stop-loss |
| 2026-10-03T19:05 | Supertrend | sell | XRP-USD | 18.22 | -0.15 | exit signal |
| 2026-10-03T19:05 | Supertrend | sell | BTC-USD | 14.62 | -0.08 | exit signal |
| 2026-10-03T19:05 | Triple EMA stack | sell | SOL-USD | 13.39 | -0.05 | exit signal |
| 2026-10-03T19:05 | Triple EMA stack | sell | ETH-USD | 16.68 | -0.11 | exit signal |
| 2026-10-03T19:05 | Triple EMA stack | sell | BTC-USD | 13.39 | -0.08 | exit signal |
| 2026-10-03T19:05 | EMA 9/21 cross | sell | ETH-USD | 12.33 | -0.07 | exit signal |
| 2026-10-03T19:05 | EMA 9/21 cross | sell | BTC-USD | 12.32 | -0.07 | exit signal |
| 2026-10-03T19:00 | MFI reversion | buy | SOL-USD | 18.79 | — | entry signal |
| 2026-10-03T19:00 | Williams %R | buy | ETH-USD | 14.03 | — | entry signal |
| 2026-10-03T19:00 | Williams %R | buy | DOGE-USD | 14.03 | — | entry signal |
| 2026-10-03T19:00 | Stochastic reversion | buy | ETH-USD | 16.44 | — | entry signal |
| 2026-10-03T19:00 | Bollinger reversion | buy | XRP-USD | 16.09 | — | entry signal |
| 2026-10-03T19:00 | Connors RSI(2) | sell | ETH-USD | 15.91 | -0.10 | exit signal |
| 2026-10-03T19:00 | Candlestick reversal | buy | XRP-USD | 15.19 | — | entry signal |
| 2026-10-03T19:00 | Candlestick reversal | buy | DOGE-USD | 15.19 | — | entry signal |
| 2026-10-03T19:00 | Trend pullback | buy | DOGE-USD | 17.27 | — | entry signal |
| 2026-10-03T19:00 | Trend pullback | buy | BTC-USD | 17.27 | — | entry signal |
| 2026-10-03T18:55 | Donchian 55/20 | sell | XRP-USD | 20.15 | -0.14 | exit signal |
| 2026-10-03T18:55 | Donchian 20/10 | sell | ETH-USD | 13.89 | -0.08 | exit signal |
| 2026-10-03T18:55 | OBV trend | sell | ETH-USD | 12.01 | -0.08 | exit signal |
| 2026-10-03T18:55 | OBV trend | sell | DOGE-USD | 12.02 | -0.07 | exit signal |
| 2026-10-03T18:55 | RSI momentum | sell | ETH-USD | 13.45 | -0.08 | exit signal |
| 2026-10-03T18:55 | Trend pullback | sell | ETH-USD | 17.14 | -0.12 | exit signal |
| 2026-10-03T18:55 | Supertrend | buy | DOGE-USD | 7.40 | — | rebalance up |
| 2026-10-03T18:55 | Supertrend | sell | ETH-USD | 14.66 | -0.09 | exit signal |
| 2026-10-03T18:50 | Connors RSI(2) | buy | XRP-USD | 15.97 | — | entry signal |
| 2026-10-03T18:50 | Candlestick reversal | sell | DOGE-USD | 15.12 | -0.10 | exit signal |
| 2026-10-03T18:50 | Donchian 20/10 | sell | XRP-USD | 17.25 | -0.15 | exit signal |
| 2026-10-03T18:50 | OBV trend | sell | XRP-USD | 14.93 | -0.12 | exit signal |
| 2026-10-03T18:50 | RSI momentum | sell | XRP-USD | 16.69 | -0.14 | exit signal |
| 2026-10-03T18:50 | Trend pullback | sell | XRP-USD | 17.29 | -0.11 | exit signal |
| 2026-10-03T18:50 | Trend pullback | sell | DOGE-USD | 17.23 | -0.12 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
