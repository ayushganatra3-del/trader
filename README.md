# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-01T19:35:05.000146+00:00 · 8072 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.24 (-0.76%)

Closed trades 31, win rate 64.5%, fees £0.90, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-01 | KOD 12%, ADRX 12%, ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, BBD 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-30)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.46 · VIX 16.34 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, META 7.4, MSFT 7.2, AMD 7.2, ETHU 7.0, BITX 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 32024 decisions in 1978 calls, $0.3875 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-01T19:35 | 3 / 11 / 16 | NANC 17% |  |
| Breezy | 2026-10-01T19:35 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-01T19:35 | 2 / 26 / 2 | COIN 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| Williams %R | TQQQ | 2.51 | +2.91% | 16 |
| Z-score reversion | MSFT | 2.34 | +2.58% | 5 |
| Stochastic reversion | MSFT | 1.97 | +2.78% | 13 |
| Connors RSI(2) · 1h | TECL | 1.95 | +5.24% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Hold BTC | benchmark | 101.63 | 1.64 | 0 | — | 34.27 | 4.22 | -8.68 | 1 |
| 2 | Daily: Bullish score | daily | 100.93 | 0.93 | 3 | 0.0 | 3.02 | 0.61 | -12.76 | 14 |
| 3 | Copy: Congress Democrats (NANC) | copy | 100.64 | 0.64 | 0 | — | 3.81 | 1.76 | -3.62 | 1 |
| 4 | Stochastic reversion · 1h | reversion | 100.44 | 0.44 | 34 | 58.8 | -8.47 | -1.79 | -10.86 | 327 |
| 5 | Timing: Nasdaq FTD · QQQ | daily | 100.32 | 0.32 | 0 | — | -2.83 | -1.68 | -5.09 | 2 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.09 | 0.09 | 0 | — | 0.46 | 0.24 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 99.90 | -0.10 | 0 | — | -9.46 | -1.86 | -15.27 | 2 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.85 | -0.14 | 11 | 27.3 | 4.08 | 2.05 | -1.46 | 83 |
| 11 | Hold SPY | benchmark | 99.79 | -0.21 | 0 | — | 1.39 | 0.85 | -3.66 | 1 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.65 | -0.35 | 4 | 25.0 | 15.75 | 3.45 | -7.55 | 43 |
| 13 | RSI(14) reversion · 1h | reversion | 99.64 | -0.36 | 9 | 55.6 | 1.66 | 0.54 | -6.74 | 121 |
| 14 | VWAP reversion · 1h | reversion | 99.59 | -0.41 | 23 | 30.4 | -10.47 | -3.54 | -14.05 | 116 |
| 15 | CCI reversion · 1h | reversion | 99.39 | -0.61 | 55 | 45.5 | 2.67 | 0.60 | -12.41 | 417 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.39 | -0.61 | 0 | — | -2.31 | -1.09 | -5.14 | 1 |
| 17 | Bollinger reversion · 1h | reversion | 99.38 | -0.62 | 37 | 43.2 | -15.16 | -4.04 | -17.75 | 307 |
| 18 | Copy: Warren Buffett (BRK-B) | copy | 99.36 | -0.64 | 0 | — | -3.59 | -1.43 | -7.65 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 20 | Agent | meta | 99.24 | -0.76 | 31 | 64.5 | -11.04 | -6.72 | -12.27 | 225 |
| 21 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.58 | -2.13 | -3.95 | 24 |
| 22 | Williams %R · 1h | reversion | 99.15 | -0.85 | 61 | 52.5 | -16.13 | -2.96 | -19.41 | 499 |
| 23 | Connors RSI(2) · 1h | reversion | 99.01 | -0.99 | 53 | 49.1 | -11.97 | -4.09 | -13.59 | 227 |
| 24 | Z-score reversion · 1h | reversion | 98.94 | -1.06 | 12 | 41.7 | 4.32 | 1.04 | -8.60 | 156 |
| 25 | Candlestick reversal · 1h | reversion | 98.68 | -1.32 | 44 | 29.5 | -25.08 | -5.93 | -26.60 | 485 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.36 | -1.64 | 0 | — | 23.00 | 3.46 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 1.55 | 0.42 | -15.21 | 45 |
| 29 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -2.27 | -1.23 | -4.29 | 105 |
| 30 | Donchian 55/20 · 1h | breakout | 98.02 | -1.98 | 15 | 0.0 | 6.21 | 1.00 | -16.96 | 110 |
| 31 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | 0.34 | 0.19 | -9.74 | 24 |
| 32 | EMA 20/50 cross · 1h | trend | 97.72 | -2.28 | 22 | 9.1 | 13.83 | 1.74 | -14.32 | 130 |
| 33 | Gap and go | momentum | 97.64 | -2.36 | 17 | 11.8 | 13.04 | 3.20 | -4.73 | 182 |
| 34 | Agent (rotation) | meta | 97.47 | -2.53 | 43 | 11.6 | -4.17 | -1.50 | -9.81 | 234 |
| 35 | Trend pullback · 1h | trend | 97.39 | -2.61 | 39 | 12.8 | -24.83 | -6.57 | -26.34 | 166 |
| 36 | Copy: Insider buying | copy | 97.24 | -2.76 | 4 | 50.0 | -15.71 | -3.10 | -18.45 | 75 |
| 37 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 198 | 17.7 | -0.46 | 0.07 | -11.23 | 389 |
| 38 | Daily: SMA 20/50 cross · AAPL | daily | 96.71 | -3.29 | 0 | — | -0.41 | -0.05 | -5.18 | 1 |
| 39 | Supertrend · 1h | trend | 96.48 | -3.52 | 22 | 4.5 | 1.33 | 0.38 | -16.43 | 202 |
| 40 | Opening range 30m | breakout | 96.47 | -3.54 | 52 | 11.5 | -11.07 | -3.21 | -15.29 | 563 |
| 41 | Parabolic SAR · 1h | trend | 95.62 | -4.38 | 41 | 14.6 | -9.12 | -1.15 | -19.70 | 309 |
| 42 | ADX DI cross · 1h | trend | 95.17 | -4.83 | 38 | 7.9 | -6.00 | -0.84 | -13.84 | 267 |
| 43 | MACD cross · 1h | trend | 94.95 | -5.05 | 63 | 11.1 | -17.66 | -2.90 | -19.81 | 488 |
| 44 | Opening range 15m | breakout | 94.85 | -5.15 | 66 | 13.6 | -12.40 | -3.32 | -17.48 | 680 |
| 45 | Max aggression: 1-day momentum | meta | 94.82 | -5.18 | 4 | 25.0 | -21.44 | -1.02 | -41.28 | 43 |
| 46 | MFI reversion · 1h | reversion | 94.30 | -5.70 | 62 | 24.2 | -9.03 | -1.62 | -17.08 | 127 |
| 47 | Squeeze breakout · 1h | breakout | 94.12 | -5.88 | 16 | 6.2 | 10.90 | 1.93 | -8.06 | 101 |
| 48 | RSI momentum · 1h | momentum | 93.82 | -6.18 | 34 | 2.9 | -0.57 | 0.12 | -16.65 | 217 |
| 49 | Ichimoku · 1h | trend | 93.77 | -6.23 | 23 | 13.0 | 5.05 | 0.79 | -16.19 | 125 |
| 50 | Volume breakout · 1h | breakout | 93.67 | -6.33 | 29 | 3.4 | 4.08 | 0.76 | -12.60 | 120 |
| 51 | Three white soldiers | momentum | 93.14 | -6.86 | 62 | 17.7 | -49.85 | -27.01 | -49.85 | 603 |
| 52 | VWAP momentum · 1h | momentum | 92.92 | -7.08 | 142 | 14.8 | -42.08 | -6.73 | -43.07 | 1278 |
| 53 | Triple EMA stack · 1h | trend | 92.57 | -7.42 | 46 | 6.5 | -9.28 | -0.96 | -23.51 | 243 |
| 54 | Max aggression: 5-day momentum | meta | 92.15 | -7.85 | 4 | 50.0 | -11.02 | -0.70 | -29.56 | 30 |
| 55 | Bollinger breakout · 1h | breakout | 91.28 | -8.72 | 27 | 7.4 | 3.20 | 0.62 | -12.06 | 281 |
| 56 | EMA 9/21 cross · 1h | trend | 91.20 | -8.80 | 61 | 9.8 | -8.96 | -1.04 | -18.47 | 334 |
| 57 | MACD zero-line · 1h | trend | 91.00 | -9.00 | 32 | 6.2 | -6.30 | -0.62 | -18.32 | 233 |
| 58 | Heikin-Ashi · 1h | trend | 90.59 | -9.41 | 66 | 15.2 | -33.22 | -5.97 | -33.88 | 685 |
| 59 | Keltner breakout · 1h | breakout | 90.53 | -9.46 | 16 | 0.0 | -10.23 | -1.23 | -21.04 | 217 |
| 60 | RSI(14) reversion | reversion | 89.84 | -10.16 | 157 | 36.3 | -72.76 | -21.42 | -73.07 | 1467 |
| 61 | OBV trend · 1h | momentum | 89.74 | -10.26 | 81 | 7.4 | -15.35 | -1.75 | -26.83 | 334 |
| 62 | Donchian 20/10 · 1h | breakout | 89.30 | -10.70 | 25 | 8.0 | -2.95 | -0.15 | -16.18 | 211 |
| 63 | ROC + volume · 1h | momentum | 86.42 | -13.58 | 71 | 8.5 | -12.44 | -1.60 | -23.27 | 410 |
| 64 | Squeeze breakout | breakout | 85.93 | -14.07 | 142 | 17.6 | -59.80 | -18.19 | -59.89 | 1186 |
| 65 | Donchian 55/20 | breakout | 84.37 | -15.63 | 137 | 19.0 | -68.01 | -15.40 | -68.06 | 1294 |
| 66 | VWAP reversion | reversion | 83.46 | -16.54 | 170 | 28.2 | -70.78 | -17.24 | -71.02 | 1380 |
| 67 | Volume breakout | breakout | 83.29 | -16.71 | 133 | 13.5 | -63.70 | -20.21 | -63.70 | 905 |
| 68 | ROC + volume | momentum | 82.61 | -17.39 | 218 | 20.6 | -72.72 | -17.61 | -73.06 | 1631 |
| 69 | AI bee: Bizzy | ai | 81.77 | -18.23 | 325 | 11.4 | — | — | — | — |
| 70 | AI bee: Boozy | ai | 81.19 | -18.81 | 117 | 3.4 | — | — | — | — |
| 71 | EMA 20/50 cross | trend | 80.83 | -19.17 | 167 | 15.0 | -79.25 | -17.28 | -79.37 | 1489 |
| 72 | Z-score reversion | reversion | 80.67 | -19.33 | 246 | 33.3 | -85.84 | -27.61 | -85.90 | 2113 |
| 73 | Keltner breakout | breakout | 80.45 | -19.55 | 208 | 14.4 | -84.71 | -32.95 | -84.71 | 1892 |
| 74 | Ichimoku | trend | 79.92 | -20.08 | 162 | 10.5 | -81.15 | -26.02 | -81.15 | 1747 |
| 75 | MFI reversion | reversion | 78.21 | -21.79 | 227 | 21.1 | -88.44 | -34.90 | -88.51 | 2121 |
| 76 | Supertrend | trend | 76.98 | -23.02 | 228 | 18.4 | -87.42 | -24.11 | -87.54 | 1952 |
| 77 | Trend pullback | trend | 76.40 | -23.60 | 238 | 16.8 | -91.15 | -33.78 | -91.24 | 2296 |
| 78 | Donchian 20/10 | breakout | 75.29 | -24.71 | 288 | 18.8 | -90.78 | -28.49 | -90.85 | 2666 |
| 79 | Bollinger breakout | breakout | 74.55 | -25.45 | 300 | 17.0 | -93.83 | -39.46 | -93.83 | 2842 |
| 80 | Triple EMA stack | trend | 74.36 | -25.64 | 291 | 15.8 | -93.12 | -34.68 | -93.17 | 2612 |
| 81 | MACD zero-line | trend | 74.15 | -25.85 | 299 | 17.1 | -91.75 | -33.74 | -91.75 | 2363 |
| 82 | ADX DI cross | trend | 73.96 | -26.04 | 269 | 8.6 | -89.65 | -42.84 | -89.69 | 2108 |
| 83 | RSI momentum | momentum | 73.88 | -26.12 | 270 | 14.1 | -90.46 | -28.16 | -90.51 | 2391 |
| 84 | Stochastic reversion | reversion | 72.90 | -27.10 | 428 | 25.9 | -95.82 | -42.44 | -95.83 | 4036 |
| 85 | Consensus | meta | 71.53 | -28.47 | 260 | 8.5 | -94.63 | -29.74 | -94.63 | 2657 |
| 86 | Connors RSI(2) | reversion | 71.29 | -28.71 | 353 | 21.5 | -96.52 | -39.62 | -96.53 | 3598 |
| 87 | Bollinger reversion | reversion | 69.78 | -30.22 | 427 | 18.3 | -95.97 | -41.94 | -96.01 | 3702 |
| 88 | Candlestick reversal | reversion | 69.06 | -30.94 | 447 | 17.7 | -99.35 | -46.19 | -99.36 | 5606 |
| 89 | EMA 9/21 cross | trend | 68.68 | -31.32 | 386 | 16.1 | -97.43 | -39.97 | -97.45 | 3549 |
| 90 | OBV trend | momentum | 68.34 | -31.66 | 416 | 16.3 | -96.03 | -44.63 | -96.05 | 3539 |
| 91 | CCI reversion | reversion | 67.97 | -32.03 | 382 | 18.1 | -98.53 | -46.59 | -98.53 | 4696 |
| 92 | Parabolic SAR | trend | 65.80 | -34.20 | 393 | 13.7 | -97.10 | -50.61 | -97.10 | 3643 |
| 93 | VWAP momentum ⏸ | momentum | 64.52 | -35.48 | 475 | 9.1 | -98.64 | -35.76 | -98.65 | 5287 |
| 94 | Williams %R | reversion | 64.44 | -35.56 | 525 | 24.8 | -99.53 | -52.39 | -99.53 | 6109 |
| 95 | MACD cross | trend | 64.19 | -35.81 | 471 | 15.5 | -99.72 | -57.13 | -99.72 | 6118 |
| 96 | Heikin-Ashi | trend | 62.57 | -37.43 | 455 | 10.5 | -99.90 | -68.57 | -99.90 | 8281 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-01T19:35 | Consensus | sell | NVDA | 10.22 | -0.04 | target is flat |
| 2026-10-01T19:35 | CCI reversion | buy | LABU | 6.83 | — | entry |
| 2026-10-01T19:35 | CCI reversion | sell | BTC-USD | 3.39 | -0.02 | rebalance down |
| 2026-10-01T19:35 | CCI reversion | sell | BITX | 3.44 | -0.00 | rebalance down |
| 2026-10-01T19:35 | Williams %R | buy | LABU | 7.95 | — | entry |
| 2026-10-01T19:35 | Stochastic reversion | buy | SOL-USD | 3.36 | — | entry signal |
| 2026-10-01T19:35 | Stochastic reversion | buy | ETH-USD | 6.63 | — | entry signal |
| 2026-10-01T19:35 | Stochastic reversion | buy | DOGE-USD | 4.88 | — | rebalance up |
| 2026-10-01T19:35 | Stochastic reversion | sell | TNA | 5.54 | 0.01 | rebalance down |
| 2026-10-01T19:35 | Stochastic reversion | sell | SQQQ | 5.57 | 0.02 | rebalance down |
| 2026-10-01T19:35 | Stochastic reversion | sell | BTC-USD | 3.76 | -0.03 | rebalance down |
| 2026-10-01T19:35 | Z-score reversion | buy | LABU | 20.17 | — | entry |
| 2026-10-01T19:35 | Bollinger reversion | buy | XRP-USD | 17.48 | — | entry signal |
| 2026-10-01T19:35 | Bollinger reversion | buy | SOL-USD | 17.48 | — | entry signal |
| 2026-10-01T19:35 | Bollinger reversion | buy | DOGE-USD | 17.48 | — | entry signal |
| 2026-10-01T19:35 | Connors RSI(2) | buy | XRP-USD | 10.19 | — | entry |
| 2026-10-01T19:35 | Connors RSI(2) | buy | ETHU | 7.91 | — | rebalance up |
| 2026-10-01T19:35 | Connors RSI(2) | sell | BTC-USD | 10.16 | -0.05 | exit signal |
| 2026-10-01T19:35 | Connors RSI(2) | sell | BITX | 10.23 | 0.03 | exit signal |
| 2026-10-01T19:35 | Three white soldiers | sell | GOOGL | 23.25 | -0.05 | exit signal |
| 2026-10-01T19:35 | Candlestick reversal | sell | GOOGL | 17.21 | -0.00 | exit signal |
| 2026-10-01T19:35 | Squeeze breakout | sell | NVDA | 21.46 | -0.10 | stop-loss |
| 2026-10-01T19:35 | Keltner breakout | sell | MSTR | 20.05 | -0.16 | stop-loss |
| 2026-10-01T19:35 | Bollinger breakout | sell | NVDA | 18.64 | -0.09 | stop-loss |
| 2026-10-01T19:35 | Bollinger breakout | sell | MSTR | 18.58 | -0.15 | stop-loss |
| 2026-10-01T19:35 | Donchian 55/20 | buy | SOXL | 4.62 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 55/20 | buy | NVDA | 4.68 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 55/20 | buy | MSTR | 4.64 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 55/20 | buy | IWM | 4.63 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 55/20 | buy | ETH-USD | 4.74 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 55/20 | sell | COIN | 9.37 | -0.04 | stop-loss |
| 2026-10-01T19:35 | Donchian 20/10 | buy | TQQQ | 5.20 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 20/10 | buy | TECL | 6.27 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 20/10 | buy | SPY | 6.29 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 20/10 | buy | SOXL | 6.27 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 20/10 | buy | QQQ | 5.91 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 20/10 | buy | PLTR | 5.79 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 20/10 | buy | MSFT | 5.82 | — | rebalance up |
| 2026-10-01T19:35 | Donchian 20/10 | sell | NVDA | 3.97 | -0.02 | exit signal |
| 2026-10-01T19:35 | Donchian 20/10 | sell | COIN | 5.78 | -0.02 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
