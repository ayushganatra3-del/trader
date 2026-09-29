# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T16:40:05.000157+00:00 · 5898 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.16 (+0.16%)

Closed trades 21, win rate 71.4%, fees £0.62, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 40.07 | -0.03 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-29 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 23967 decisions in 2456 calls, $0.3032 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T16:40 | 2 / 15 / 12 | AMZN 18%, COIN 14% |  |
| Breezy | 2026-09-29T16:40 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-09-29T16:40 | 3 / 23 / 3 | COIN 40%, MSTR 32% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |
| CCI reversion | AMD | 2.04 | +3.07% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.81 | 1.81 | 1 | 100.0 | 14.55 | 3.16 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 4 | Agent (aggressive) | meta | 100.17 | 0.17 | 8 | 62.5 | 1.18 | 0.77 | -3.92 | 93 |
| 5 | Agent | meta | 100.16 | 0.16 | 21 | 71.4 | -9.39 | -6.24 | -10.68 | 212 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 11.70 | 2.23 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Copy: Congress Democrats (NANC) | copy | 99.95 | -0.05 | 0 | — | 6.78 | 2.53 | -3.62 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.45 | 1.78 | -1.51 | 83 |
| 11 | Hold BTC | benchmark | 99.63 | -0.37 | 0 | — | 29.81 | 3.75 | -8.68 | 1 |
| 12 | Hold SPY | benchmark | 99.50 | -0.49 | 0 | — | 3.71 | 1.91 | -3.66 | 1 |
| 13 | Copy: Warren Buffett (BRK-B) | copy | 99.48 | -0.52 | 0 | — | -1.78 | -0.69 | -7.65 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.47 | -0.53 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.39 | -0.61 | 0 | — | -3.58 | -2.20 | -5.09 | 2 |
| 16 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 17 | RSI(14) reversion · 1h | reversion | 99.23 | -0.77 | 7 | 57.1 | 2.08 | 0.67 | -6.57 | 117 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | Daily: Bullish score | daily | 98.87 | -1.14 | 2 | 0.0 | -1.56 | -0.02 | -12.76 | 13 |
| 20 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 21 | Max aggression: 5-day momentum | meta | 98.71 | -1.28 | 2 | 50.0 | -7.74 | -0.36 | -29.56 | 29 |
| 22 | Williams %R · 1h | reversion | 98.67 | -1.33 | 39 | 46.2 | -18.21 | -3.36 | -19.58 | 482 |
| 23 | Z-score reversion · 1h | reversion | 98.64 | -1.36 | 9 | 44.4 | 4.22 | 1.04 | -8.60 | 153 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 98.47 | -1.53 | 0 | — | 25.25 | 3.64 | -6.29 | 1 |
| 25 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.64 | 3.88 | -4.73 | 195 |
| 26 | Candlestick reversal · 1h | reversion | 98.40 | -1.60 | 18 | 27.8 | -26.33 | -6.42 | -26.80 | 482 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.15 | 0.00 | -15.21 | 47 |
| 28 | Copy: Insider buying | copy | 98.35 | -1.65 | 2 | 100.0 | -14.84 | -2.96 | -17.74 | 72 |
| 29 | CCI reversion · 1h | reversion | 98.14 | -1.86 | 34 | 35.3 | 2.21 | 0.54 | -12.41 | 405 |
| 30 | Agent (rotation) | meta | 98.10 | -1.90 | 32 | 12.5 | -5.43 | -1.84 | -11.62 | 217 |
| 31 | EMA 20/50 cross · 1h | trend | 97.95 | -2.05 | 10 | 10.0 | 15.42 | 1.87 | -14.36 | 128 |
| 32 | Connors RSI(2) · 1h | reversion | 97.91 | -2.09 | 41 | 46.3 | -12.95 | -4.10 | -13.22 | 236 |
| 33 | Stochastic reversion · 1h | reversion | 97.83 | -2.17 | 26 | 53.8 | -14.49 | -3.21 | -15.03 | 321 |
| 34 | Opening range 30m | breakout | 97.69 | -2.31 | 31 | 12.9 | -8.51 | -2.45 | -13.54 | 559 |
| 35 | Timing: Nasdaq FTD · TQQQ | daily | 97.52 | -2.48 | 0 | — | -11.48 | -2.38 | -15.27 | 2 |
| 36 | Squeeze breakout · 1h | breakout | 97.43 | -2.58 | 9 | 11.1 | 13.87 | 2.42 | -7.66 | 99 |
| 37 | Supertrend · 1h | trend | 97.33 | -2.67 | 16 | 6.2 | 4.15 | 0.75 | -16.43 | 196 |
| 38 | Daily: SMA 20/50 cross · AAPL | daily | 97.24 | -2.76 | 0 | — | -9.93 | -2.44 | -12.73 | 1 |
| 39 | Bollinger reversion · 1h | reversion | 96.87 | -3.12 | 22 | 27.3 | -18.41 | -5.14 | -18.51 | 310 |
| 40 | Donchian 55/20 · 1h | breakout | 96.62 | -3.38 | 12 | 0.0 | 5.24 | 0.89 | -16.96 | 112 |
| 41 | Agent (ML meta-label) | meta | 96.56 | -3.44 | 112 | 10.7 | -0.00 | 0.15 | -12.04 | 371 |
| 42 | MACD cross · 1h | trend | 96.51 | -3.49 | 36 | 8.3 | -18.07 | -3.07 | -21.54 | 459 |
| 43 | Trend pullback · 1h | trend | 96.50 | -3.50 | 25 | 12.0 | -28.93 | -7.07 | -29.59 | 149 |
| 44 | Opening range 15m | breakout | 96.17 | -3.83 | 41 | 12.2 | -10.21 | -2.77 | -16.14 | 691 |
| 45 | Parabolic SAR · 1h | trend | 95.74 | -4.26 | 25 | 12.0 | -8.75 | -1.12 | -18.82 | 292 |
| 46 | Ichimoku · 1h | trend | 95.70 | -4.30 | 15 | 13.3 | 6.68 | 0.98 | -15.13 | 121 |
| 47 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -51.83 | -28.82 | -52.12 | 623 |
| 48 | Bollinger breakout · 1h | breakout | 95.32 | -4.67 | 17 | 5.9 | 7.26 | 1.14 | -10.83 | 284 |
| 49 | MACD zero-line · 1h | trend | 95.21 | -4.79 | 18 | 5.6 | -4.92 | -0.51 | -14.64 | 222 |
| 50 | RSI momentum · 1h | momentum | 94.84 | -5.16 | 24 | 4.2 | -1.24 | 0.03 | -15.29 | 212 |
| 51 | Volume breakout · 1h | breakout | 94.83 | -5.17 | 26 | 3.8 | 5.75 | 0.98 | -12.60 | 125 |
| 52 | ADX DI cross · 1h | trend | 94.79 | -5.21 | 29 | 6.9 | -12.59 | -2.37 | -15.39 | 254 |
| 53 | MFI reversion · 1h | reversion | 94.78 | -5.22 | 42 | 11.9 | -10.65 | -1.98 | -17.27 | 126 |
| 54 | Donchian 20/10 · 1h | breakout | 94.69 | -5.31 | 14 | 14.3 | 7.53 | 1.15 | -12.78 | 216 |
| 55 | Triple EMA stack · 1h | trend | 94.37 | -5.63 | 29 | 6.9 | -6.78 | -0.62 | -22.92 | 228 |
| 56 | VWAP momentum · 1h | momentum | 94.30 | -5.70 | 100 | 13.0 | -30.71 | -4.51 | -34.71 | 1236 |
| 57 | Keltner breakout · 1h | breakout | 94.28 | -5.72 | 9 | 0.0 | -4.60 | -0.40 | -18.68 | 216 |
| 58 | Max aggression: 1-day momentum | meta | 94.02 | -5.98 | 2 | 0.0 | -39.73 | -2.42 | -49.44 | 42 |
| 59 | EMA 9/21 cross · 1h | trend | 93.94 | -6.06 | 40 | 12.5 | -3.56 | -0.29 | -16.92 | 309 |
| 60 | OBV trend · 1h | momentum | 93.47 | -6.54 | 51 | 7.8 | -9.08 | -0.94 | -25.24 | 327 |
| 61 | Heikin-Ashi · 1h | trend | 92.94 | -7.06 | 41 | 12.2 | -23.42 | -3.51 | -30.37 | 677 |
| 62 | RSI(14) reversion | reversion | 91.18 | -8.82 | 99 | 33.3 | -70.91 | -21.46 | -71.14 | 1482 |
| 63 | Squeeze breakout | breakout | 89.77 | -10.23 | 79 | 10.1 | -59.90 | -18.71 | -60.26 | 1178 |
| 64 | ROC + volume · 1h | momentum | 89.59 | -10.41 | 51 | 5.9 | -4.37 | -0.35 | -18.96 | 406 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | Donchian 55/20 | breakout | 87.83 | -12.16 | 88 | 14.8 | -68.33 | -15.65 | -68.35 | 1303 |
| 68 | EMA 20/50 cross | trend | 87.57 | -12.43 | 105 | 15.2 | -78.70 | -17.62 | -78.85 | 1465 |
| 69 | ROC + volume | momentum | 87.44 | -12.56 | 133 | 17.3 | -72.70 | -18.31 | -73.12 | 1645 |
| 70 | Volume breakout | breakout | 87.37 | -12.63 | 89 | 12.4 | -62.26 | -20.64 | -62.37 | 891 |
| 71 | Ichimoku | trend | 86.08 | -13.92 | 105 | 8.6 | -80.36 | -26.22 | -80.37 | 1758 |
| 72 | Keltner breakout | breakout | 85.58 | -14.42 | 138 | 11.6 | -85.10 | -35.88 | -85.28 | 1925 |
| 73 | Z-score reversion | reversion | 85.15 | -14.86 | 160 | 30.0 | -84.31 | -27.50 | -84.43 | 2093 |
| 74 | VWAP reversion | reversion | 84.58 | -15.43 | 119 | 17.6 | -71.83 | -17.65 | -72.18 | 1395 |
| 75 | Supertrend | trend | 83.15 | -16.85 | 155 | 16.8 | -87.60 | -25.36 | -87.61 | 1959 |
| 76 | MACD zero-line | trend | 83.11 | -16.89 | 172 | 14.5 | -91.62 | -36.32 | -91.63 | 2354 |
| 77 | MFI reversion | reversion | 81.85 | -18.15 | 168 | 18.5 | -87.68 | -35.28 | -87.80 | 2161 |
| 78 | Donchian 20/10 | breakout | 81.34 | -18.66 | 178 | 16.9 | -91.03 | -30.74 | -91.11 | 2683 |
| 79 | Bollinger breakout | breakout | 81.09 | -18.91 | 183 | 14.8 | -94.03 | -42.85 | -94.13 | 2865 |
| 80 | Triple EMA stack | trend | 80.92 | -19.08 | 193 | 14.5 | -93.16 | -36.33 | -93.16 | 2618 |
| 81 | RSI momentum | momentum | 80.74 | -19.26 | 173 | 11.6 | -90.57 | -29.89 | -90.57 | 2385 |
| 82 | ADX DI cross | trend | 80.17 | -19.83 | 180 | 6.7 | -89.39 | -46.89 | -89.43 | 2099 |
| 83 | Trend pullback | trend | 80.13 | -19.87 | 163 | 17.8 | -90.78 | -34.76 | -90.79 | 2288 |
| 84 | EMA 9/21 cross | trend | 77.79 | -22.21 | 249 | 15.3 | -97.35 | -42.07 | -97.36 | 3534 |
| 85 | Connors RSI(2) | reversion | 77.50 | -22.50 | 234 | 16.2 | -96.46 | -43.12 | -96.47 | 3649 |
| 86 | Consensus | meta | 77.19 | -22.81 | 179 | 7.3 | -94.57 | -30.64 | -94.57 | 2643 |
| 87 | Stochastic reversion | reversion | 76.65 | -23.35 | 292 | 22.3 | -95.92 | -47.93 | -95.97 | 4064 |
| 88 | Candlestick reversal | reversion | 76.45 | -23.55 | 256 | 13.3 | -99.36 | -53.31 | -99.36 | 5579 |
| 89 | OBV trend | momentum | 76.06 | -23.94 | 250 | 14.0 | -95.92 | -49.74 | -95.92 | 3549 |
| 90 | Bollinger reversion | reversion | 75.54 | -24.46 | 275 | 13.8 | -95.75 | -46.00 | -95.79 | 3683 |
| 91 | VWAP momentum | momentum | 74.25 | -25.75 | 343 | 9.6 | -98.43 | -36.57 | -98.47 | 5210 |
| 92 | CCI reversion | reversion | 74.19 | -25.81 | 197 | 7.1 | -98.44 | -52.11 | -98.45 | 4692 |
| 93 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -96.99 | -57.08 | -97.00 | 3648 |
| 94 | MACD cross | trend | 72.62 | -27.38 | 230 | 11.3 | -99.70 | -67.12 | -99.70 | 6094 |
| 95 | Williams %R | reversion | 72.19 | -27.81 | 297 | 20.5 | -99.52 | -61.26 | -99.53 | 6095 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -91.61 | -99.89 | 8324 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T16:40 | Donchian 55/20 · 1h | buy | TECL | 8.01 | — | rebalance up |
| 2026-09-29T16:40 | Donchian 55/20 · 1h | buy | SOXL | 8.14 | — | rebalance up |
| 2026-09-29T16:40 | Donchian 55/20 · 1h | buy | QQQ | 7.89 | — | rebalance up |
| 2026-09-29T16:40 | Donchian 55/20 · 1h | buy | NVDA | 7.85 | — | rebalance up |
| 2026-09-29T16:40 | Donchian 55/20 · 1h | sell | XRP-USD | 19.21 | -0.46 | stop-loss |
| 2026-09-29T16:40 | Donchian 20/10 · 1h | sell | XRP-USD | 23.50 | -0.53 | stop-loss |
| 2026-09-29T16:40 | RSI momentum · 1h | sell | XRP-USD | 23.59 | -0.49 | stop-loss |
| 2026-09-29T16:40 | ROC + volume · 1h | sell | XRP-USD | 22.26 | -0.48 | stop-loss |
| 2026-09-29T16:40 | VWAP momentum · 1h | buy | MSFT | 23.49 | — | entry |
| 2026-09-29T16:40 | Ichimoku · 1h | sell | XRP-USD | 23.66 | -0.69 | stop-loss |
| 2026-09-29T16:40 | Triple EMA stack · 1h | buy | SOXL | 4.74 | — | rebalance up |
| 2026-09-29T16:40 | Triple EMA stack · 1h | buy | ETH-USD | 7.77 | — | rebalance up |
| 2026-09-29T16:40 | Triple EMA stack · 1h | sell | XRP-USD | 18.75 | -0.34 | stop-loss |
| 2026-09-29T16:40 | Triple EMA stack · 1h | sell | TECL | 14.45 | -0.21 | target is flat |
| 2026-09-29T16:40 | EMA 9/21 cross · 1h | buy | SOXL | 4.92 | — | rebalance up |
| 2026-09-29T16:40 | EMA 9/21 cross · 1h | buy | NVDA | 4.76 | — | rebalance up |
| 2026-09-29T16:40 | EMA 9/21 cross · 1h | buy | ETH-USD | 4.87 | — | rebalance up |
| 2026-09-29T16:40 | EMA 9/21 cross · 1h | sell | TECL | 9.39 | -0.07 | target is flat |
| 2026-09-29T16:40 | MFI reversion | buy | MSTR | 11.71 | — | entry |
| 2026-09-29T16:40 | MFI reversion | buy | ETH-USD | 11.71 | — | entry |
| 2026-09-29T16:40 | MFI reversion | buy | COIN | 11.71 | — | entry |
| 2026-09-29T16:40 | MFI reversion | buy | BTC-USD | 8.30 | — | rebalance up |
| 2026-09-29T16:40 | MFI reversion | sell | UPRO | 10.20 | -0.03 | exit signal |
| 2026-09-29T16:40 | MFI reversion | sell | SPY | 10.27 | -0.01 | exit signal |
| 2026-09-29T16:40 | MFI reversion | sell | SOL-USD | 10.21 | -0.07 | exit signal |
| 2026-09-29T16:40 | MFI reversion | sell | DOGE-USD | 10.25 | -0.04 | exit signal |
| 2026-09-29T16:40 | MFI reversion | sell | BITX | 6.85 | 0.02 | exit signal |
| 2026-09-29T16:40 | Candlestick reversal | buy | SPY | 6.37 | — | entry |
| 2026-09-29T16:40 | Candlestick reversal | sell | XRP-USD | 6.85 | -0.10 | stop-loss |
| 2026-09-29T16:40 | Candlestick reversal | sell | TSLA | 6.95 | -0.03 | stop-loss |
| 2026-09-29T16:40 | Volume breakout | buy | AMZN | 21.85 | — | entry signal |
| 2026-09-29T16:40 | Squeeze breakout | buy | AMZN | 22.45 | — | entry signal |
| 2026-09-29T16:40 | Bollinger breakout | buy | AMZN | 20.28 | — | entry signal |
| 2026-09-29T16:40 | Donchian 20/10 | buy | AMZN | 20.34 | — | entry signal |
| 2026-09-29T16:40 | Supertrend | buy | AMZN | 20.79 | — | entry signal |
| 2026-09-29T16:35 | Agent (ML meta-label) | buy | QQQ | 5.68 | — | entry |
| 2026-09-29T16:35 | Agent (ML meta-label) | sell | SOL-USD | 5.34 | -0.03 | selected signal exited |
| 2026-09-29T16:35 | Agent (ML meta-label) | sell | PLTR | 5.36 | -0.00 | selected signal exited |
| 2026-09-29T16:35 | Consensus | sell | XRP-USD | 19.16 | -0.18 | target is flat |
| 2026-09-29T16:35 | Agent | sell | TQQQ | 20.00 | -0.05 | selected signal exited |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
