# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-02T14:37:05.000184+00:00 · 8975 ticks

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

### Market regime (QQQ, 2026-10-01)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.51 · VIX 16.39 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.6, PLTR 8.5, META 7.7, AMD 7.5, TECL 7.1, BITX 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 14322 decisions in 2073 calls, $0.1895 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-02T14:37 | 2 / 15 / 14 | cash |  |
| Breezy | 2026-10-02T14:37 | 0 / 26 / 5 | cash |  |
| Boozy | 2026-10-02T14:37 | 0 / 27 / 4 | MSTR 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| Bollinger reversion · 1h | UPRO | 2.12 | +4.42% | 3 |
| Connors RSI(2) · 1h | TQQQ | 2.12 | +4.58% | 4 |
| Z-score reversion | MSFT | 2.05 | +2.32% | 5 |
| Stochastic reversion · 1h | SPY | 2.03 | +1.53% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 103.80 | 3.80 | 0 | — | -5.53 | -0.91 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 103.50 | 3.50 | 0 | — | 4.31 | 1.18 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 102.52 | 2.52 | 0 | — | 35.78 | 4.33 | -8.68 | 1 |
| 4 | Daily: Bullish score | daily | 101.95 | 1.95 | 3 | 0.0 | 4.31 | 0.78 | -12.76 | 14 |
| 5 | Timing: Nasdaq FTD · QQQ | daily | 101.38 | 1.38 | 0 | — | -1.39 | -0.73 | -5.09 | 2 |
| 6 | Donchian 55/20 · 1h | breakout | 101.30 | 1.30 | 15 | 0.0 | 8.46 | 1.26 | -16.96 | 115 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.20 | 1.20 | 0 | — | 4.52 | 2.02 | -3.62 | 1 |
| 8 | Stochastic reversion · 1h | reversion | 100.98 | 0.98 | 39 | 61.5 | -6.76 | -1.37 | -9.86 | 328 |
| 9 | Z-score reversion · 1h | reversion | 100.60 | 0.60 | 17 | 58.8 | 6.42 | 1.44 | -8.60 | 156 |
| 10 | Candlestick reversal · 1h | reversion | 100.56 | 0.56 | 53 | 37.7 | -23.16 | -5.28 | -26.14 | 492 |
| 11 | Hold SPY | benchmark | 100.33 | 0.33 | 0 | — | 2.20 | 1.28 | -3.66 | 1 |
| 12 | RSI(14) reversion · 1h | reversion | 100.24 | 0.24 | 10 | 60.0 | 4.62 | 1.34 | -6.57 | 116 |
| 13 | EMA 20/50 cross · 1h | trend | 100.16 | 0.16 | 23 | 8.7 | 16.95 | 2.03 | -14.40 | 130 |
| 14 | Copy: Cathie Wood (ARKK) | copy | 100.15 | 0.15 | 0 | — | 24.90 | 3.63 | -6.29 | 1 |
| 15 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 16 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 17 | Trend pullback · 1h | trend | 99.93 | -0.07 | 43 | 20.9 | -22.56 | -5.53 | -26.06 | 164 |
| 18 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 24 | 33.3 | -11.06 | -3.75 | -14.05 | 111 |
| 19 | Day trade: Stocks in Play ORB | daytrade | 99.89 | -0.11 | 15 | 33.3 | 3.95 | 1.96 | -1.46 | 86 |
| 20 | Bollinger reversion · 1h | reversion | 99.86 | -0.14 | 38 | 44.7 | -14.99 | -4.01 | -17.68 | 302 |
| 21 | Williams %R · 1h | reversion | 99.67 | -0.33 | 69 | 55.1 | -15.08 | -2.71 | -19.41 | 494 |
| 22 | CCI reversion · 1h | reversion | 99.48 | -0.52 | 63 | 49.2 | 2.40 | 0.56 | -12.41 | 413 |
| 23 | Copy: Warren Buffett (BRK-B) | copy | 99.46 | -0.54 | 0 | — | -2.41 | -0.93 | -7.65 | 1 |
| 24 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 25 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.45 | -5.95 | -11.27 | 222 |
| 26 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 27 | Copy: Hedge-fund gurus (GURU) | copy | 99.05 | -0.95 | 0 | — | -2.59 | -1.22 | -5.14 | 1 |
| 28 | Max aggression: 1-day momentum | meta | 99.03 | -0.97 | 5 | 40.0 | -21.01 | -0.97 | -41.28 | 43 |
| 29 | Connors RSI(2) · 1h | reversion | 99.01 | -0.99 | 53 | 49.1 | -11.53 | -3.92 | -13.59 | 223 |
| 30 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 31 | Three white soldiers · 1h | momentum | 98.55 | -1.45 | 3 | 0.0 | -3.10 | -2.52 | -3.95 | 26 |
| 32 | Agent (ML meta-label) | meta | 98.42 | -1.58 | 199 | 17.6 | 3.97 | 0.86 | -10.88 | 366 |
| 33 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.97 | -0.47 | -4.23 | 104 |
| 34 | Agent (rotation) | meta | 98.11 | -1.89 | 48 | 18.8 | -3.35 | -1.25 | -8.90 | 227 |
| 35 | Daily: SMA 20/50 cross · AAPL | daily | 97.83 | -2.17 | 0 | — | 0.36 | 0.22 | -5.18 | 1 |
| 36 | Parabolic SAR · 1h | trend | 97.80 | -2.19 | 42 | 14.3 | -6.45 | -0.73 | -19.70 | 312 |
| 37 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 38 | Supertrend · 1h | trend | 97.56 | -2.44 | 23 | 4.3 | 3.73 | 0.68 | -16.43 | 203 |
| 39 | ADX DI cross · 1h | trend | 97.53 | -2.46 | 40 | 12.5 | -3.65 | -0.44 | -13.84 | 269 |
| 40 | Daily: Momentum burst | daily | 97.18 | -2.82 | 3 | 0.0 | -0.84 | 0.05 | -16.22 | 46 |
| 41 | MACD cross · 1h | trend | 97.12 | -2.88 | 63 | 11.1 | -14.05 | -2.18 | -17.97 | 485 |
| 42 | Gap and go | momentum | 97.12 | -2.88 | 25 | 8.0 | 12.99 | 3.16 | -4.73 | 199 |
| 43 | Squeeze breakout · 1h | breakout | 96.69 | -3.31 | 20 | 20.0 | 22.02 | 3.11 | -8.06 | 113 |
| 44 | MFI reversion · 1h | reversion | 96.64 | -3.36 | 68 | 29.4 | -6.00 | -0.97 | -16.99 | 121 |
| 45 | Opening range 30m | breakout | 96.34 | -3.66 | 58 | 20.7 | -12.75 | -3.82 | -15.29 | 562 |
| 46 | Ichimoku · 1h | trend | 96.21 | -3.79 | 23 | 13.0 | 8.04 | 1.09 | -16.19 | 128 |
| 47 | Copy: Insider buying | copy | 95.96 | -4.04 | 4 | 50.0 | -17.99 | -3.58 | -19.77 | 71 |
| 48 | RSI momentum · 1h | momentum | 95.66 | -4.34 | 34 | 2.9 | 2.99 | 0.59 | -16.65 | 228 |
| 49 | Opening range 15m | breakout | 95.27 | -4.72 | 72 | 19.4 | -14.04 | -4.00 | -17.48 | 688 |
| 50 | Triple EMA stack · 1h | trend | 95.00 | -5.00 | 46 | 6.5 | -6.69 | -0.60 | -23.88 | 241 |
| 51 | VWAP momentum · 1h | momentum | 94.69 | -5.31 | 151 | 18.5 | -39.85 | -6.15 | -42.55 | 1276 |
| 52 | Bollinger breakout · 1h | breakout | 94.27 | -5.73 | 32 | 18.8 | 6.92 | 1.07 | -12.06 | 293 |
| 53 | Max aggression: 5-day momentum | meta | 94.05 | -5.95 | 5 | 40.0 | -18.96 | -1.59 | -29.56 | 30 |
| 54 | Volume breakout · 1h | breakout | 93.63 | -6.37 | 29 | 3.4 | 4.11 | 0.76 | -12.60 | 128 |
| 55 | EMA 9/21 cross · 1h | trend | 93.41 | -6.59 | 62 | 11.3 | -3.58 | -0.28 | -18.47 | 343 |
| 56 | Three white soldiers | momentum | 92.82 | -7.18 | 64 | 17.2 | -49.52 | -26.65 | -49.52 | 598 |
| 57 | Heikin-Ashi · 1h | trend | 92.58 | -7.42 | 71 | 19.7 | -31.53 | -5.43 | -33.58 | 683 |
| 58 | MACD zero-line · 1h | trend | 92.50 | -7.50 | 32 | 6.2 | -3.56 | -0.25 | -18.32 | 233 |
| 59 | Donchian 20/10 · 1h | breakout | 91.84 | -8.16 | 25 | 8.0 | 0.35 | 0.26 | -16.18 | 222 |
| 60 | OBV trend · 1h | momentum | 91.09 | -8.91 | 85 | 10.6 | -13.29 | -1.47 | -26.61 | 338 |
| 61 | RSI(14) reversion | reversion | 89.58 | -10.42 | 163 | 36.2 | -72.60 | -21.06 | -72.82 | 1464 |
| 62 | Keltner breakout · 1h | breakout | 89.30 | -10.70 | 19 | 0.0 | -11.04 | -1.31 | -21.92 | 216 |
| 63 | ROC + volume · 1h | momentum | 88.45 | -11.54 | 76 | 14.5 | -12.19 | -1.55 | -23.53 | 422 |
| 64 | Squeeze breakout | breakout | 83.76 | -16.24 | 159 | 16.4 | -59.92 | -18.24 | -60.71 | 1204 |
| 65 | Donchian 55/20 | breakout | 83.59 | -16.41 | 157 | 19.7 | -67.63 | -15.05 | -67.96 | 1309 |
| 66 | VWAP reversion | reversion | 82.54 | -17.46 | 176 | 28.4 | -70.84 | -17.14 | -70.84 | 1376 |
| 67 | ROC + volume | momentum | 80.49 | -19.51 | 246 | 20.3 | -73.50 | -17.83 | -73.84 | 1676 |
| 68 | EMA 20/50 cross | trend | 80.48 | -19.52 | 186 | 18.8 | -78.77 | -16.63 | -79.22 | 1483 |
| 69 | Volume breakout | breakout | 80.20 | -19.80 | 154 | 13.6 | -64.03 | -20.04 | -64.10 | 917 |
| 70 | Z-score reversion | reversion | 79.69 | -20.31 | 257 | 32.3 | -85.47 | -26.42 | -85.47 | 2103 |
| 71 | AI bee: Boozy | ai | 79.65 | -20.35 | 131 | 3.8 | — | — | — | — |
| 72 | AI bee: Bizzy | ai | 79.57 | -20.43 | 367 | 11.2 | — | — | — | — |
| 73 | MFI reversion | reversion | 77.42 | -22.58 | 239 | 21.8 | -88.32 | -33.61 | -88.32 | 2140 |
| 74 | Ichimoku | trend | 77.05 | -22.95 | 185 | 9.7 | -81.20 | -25.52 | -81.31 | 1760 |
| 75 | Keltner breakout | breakout | 76.94 | -23.06 | 235 | 14.0 | -85.18 | -32.55 | -85.19 | 1900 |
| 76 | Supertrend | trend | 75.24 | -24.76 | 263 | 20.5 | -87.28 | -23.43 | -87.45 | 1951 |
| 77 | Donchian 20/10 | breakout | 73.61 | -26.39 | 318 | 19.5 | -90.64 | -27.58 | -90.73 | 2676 |
| 78 | ADX DI cross | trend | 72.17 | -27.83 | 289 | 9.3 | -89.71 | -41.57 | -89.71 | 2114 |
| 79 | MACD zero-line | trend | 72.07 | -27.93 | 320 | 16.9 | -91.69 | -32.43 | -91.69 | 2361 |
| 80 | Trend pullback | trend | 71.94 | -28.06 | 288 | 18.1 | -91.63 | -33.56 | -91.63 | 2326 |
| 81 | Triple EMA stack | trend | 71.85 | -28.14 | 329 | 17.6 | -93.11 | -33.50 | -93.16 | 2616 |
| 82 | RSI momentum | momentum | 71.75 | -28.25 | 309 | 16.2 | -90.41 | -27.47 | -90.51 | 2392 |
| 83 | Bollinger breakout | breakout | 70.37 | -29.63 | 334 | 16.5 | -93.92 | -38.34 | -93.92 | 2851 |
| 84 | Stochastic reversion | reversion | 69.89 | -30.11 | 461 | 24.9 | -95.82 | -42.19 | -95.82 | 4030 |
| 85 | Consensus | meta | 68.50 | -31.50 | 297 | 9.8 | -94.65 | -29.17 | -94.65 | 2653 |
| 86 | Bollinger reversion | reversion | 68.21 | -31.79 | 449 | 17.4 | -95.93 | -41.15 | -95.93 | 3696 |
| 87 | Connors RSI(2) | reversion | 66.55 | -33.45 | 399 | 19.3 | -96.68 | -39.49 | -96.68 | 3622 |
| 88 | EMA 9/21 cross | trend | 66.29 | -33.71 | 432 | 18.5 | -97.37 | -37.14 | -97.40 | 3541 |
| 89 | Candlestick reversal | reversion | 65.88 | -34.12 | 481 | 17.0 | -99.34 | -44.34 | -99.34 | 5591 |
| 90 | CCI reversion | reversion | 65.32 | -34.67 | 413 | 17.2 | -98.51 | -44.83 | -98.51 | 4687 |
| 91 | OBV trend | momentum | 64.87 | -35.13 | 463 | 16.2 | -96.11 | -42.98 | -96.12 | 3582 |
| 92 | VWAP momentum | momentum | 63.44 | -36.56 | 501 | 9.4 | -98.61 | -33.65 | -98.61 | 5313 |
| 93 | Parabolic SAR | trend | 61.88 | -38.12 | 446 | 14.3 | -97.16 | -48.46 | -97.16 | 3648 |
| 94 | Williams %R | reversion | 60.68 | -39.32 | 571 | 23.3 | -99.53 | -50.69 | -99.53 | 6100 |
| 95 | MACD cross | trend | 60.36 | -39.64 | 519 | 15.2 | -99.71 | -52.28 | -99.71 | 6109 |
| 96 | Heikin-Ashi ⏸ | trend | 58.33 | -41.67 | 502 | 10.0 | -99.90 | -63.56 | -99.90 | 8304 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-02T14:35 | Consensus | buy | TQQQ | 5.08 | — | rebalance up |
| 2026-10-02T14:35 | Consensus | buy | TECL | 5.13 | — | rebalance up |
| 2026-10-02T14:35 | Consensus | buy | SOXL | 5.12 | — | rebalance up |
| 2026-10-02T14:35 | Consensus | buy | NVDA | 5.12 | — | rebalance up |
| 2026-10-02T14:35 | Consensus | buy | AMD | 5.13 | — | rebalance up |
| 2026-10-02T14:35 | Consensus | sell | XRP-USD | 8.57 | -0.09 | target is flat |
| 2026-10-02T14:35 | Consensus | sell | TSLA | 8.42 | -0.06 | target is flat |
| 2026-10-02T14:35 | Consensus | sell | QQQ | 8.60 | -0.01 | target is flat |
| 2026-10-02T14:35 | Squeeze breakout · 1h | buy | NVDA | 15.74 | — | rebalance up |
| 2026-10-02T14:35 | Squeeze breakout · 1h | sell | BITX | 19.03 | 0.28 | stop-loss |
| 2026-10-02T14:35 | Keltner breakout · 1h | sell | BTC-USD | 5.94 | -0.07 | stop-loss |
| 2026-10-02T14:35 | Bollinger breakout · 1h | sell | BITX | 5.87 | 0.08 | stop-loss |
| 2026-10-02T14:35 | ROC + volume · 1h | sell | BTC-USD | 4.65 | 0.07 | stop-loss |
| 2026-10-02T14:35 | CCI reversion | buy | XRP-USD | 7.00 | — | rebalance up |
| 2026-10-02T14:35 | CCI reversion | buy | SQQQ | 6.91 | — | rebalance up |
| 2026-10-02T14:35 | CCI reversion | buy | SOL-USD | 7.03 | — | rebalance up |
| 2026-10-02T14:35 | CCI reversion | buy | LABU | 6.97 | — | rebalance up |
| 2026-10-02T14:35 | CCI reversion | sell | DOGE-USD | 9.27 | -0.15 | stop-loss |
| 2026-10-02T14:35 | CCI reversion | sell | BTC-USD | 9.28 | -0.13 | stop-loss |
| 2026-10-02T14:35 | Williams %R | sell | XRP-USD | 15.16 | -0.20 | stop-loss |
| 2026-10-02T14:35 | Williams %R | sell | SOL-USD | 12.13 | -0.19 | stop-loss |
| 2026-10-02T14:35 | Stochastic reversion | sell | ETH-USD | 17.38 | -0.21 | stop-loss |
| 2026-10-02T14:35 | VWAP reversion | sell | MSTR | 20.33 | -0.40 | stop-loss |
| 2026-10-02T14:35 | Z-score reversion | sell | ETH-USD | 19.76 | -0.24 | stop-loss |
| 2026-10-02T14:35 | Bollinger reversion | sell | ETH-USD | 10.32 | -0.13 | stop-loss |
| 2026-10-02T14:35 | Bollinger reversion | sell | DOGE-USD | 13.58 | -0.18 | stop-loss |
| 2026-10-02T14:35 | Bollinger reversion | sell | BTC-USD | 13.55 | -0.20 | stop-loss |
| 2026-10-02T14:35 | Connors RSI(2) | buy | SOL-USD | 7.36 | — | entry signal |
| 2026-10-02T14:35 | Connors RSI(2) | buy | ETHU | 7.41 | — | entry signal |
| 2026-10-02T14:35 | Connors RSI(2) | buy | DOGE-USD | 7.41 | — | entry signal |
| 2026-10-02T14:35 | Connors RSI(2) | buy | BITX | 7.41 | — | entry signal |
| 2026-10-02T14:35 | Connors RSI(2) | buy | AMZN | 7.41 | — | entry signal |
| 2026-10-02T14:35 | Connors RSI(2) | sell | MSTR | 9.15 | -0.18 | rebalance down |
| 2026-10-02T14:35 | Connors RSI(2) | sell | MSFT | 9.33 | -0.01 | rebalance down |
| 2026-10-02T14:35 | Connors RSI(2) | sell | COIN | 9.29 | -0.08 | rebalance down |
| 2026-10-02T14:35 | Connors RSI(2) | sell | BTC-USD | 9.22 | -0.09 | rebalance down |
| 2026-10-02T14:35 | Candlestick reversal | sell | ETH-USD | 16.38 | -0.20 | stop-loss |
| 2026-10-02T14:35 | Keltner breakout | sell | BITX | 19.13 | -0.28 | stop-loss |
| 2026-10-02T14:35 | OBV trend | buy | META | 12.98 | — | entry signal |
| 2026-10-02T14:35 | OBV trend | sell | SOL-USD | 10.72 | -0.18 | stop-loss |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
