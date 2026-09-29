# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T13:39:05.000161+00:00 · 5748 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.98 (-0.02%)

Closed trades 17, win rate 70.6%, fees £0.52, max drawdown -1.39%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-28 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 10560 decisions in 2007 calls, $0.1462 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T13:39 | 5 / 19 / 6 | COIN 18%, BITX 16%, ARKK 14%, ETHU 14% |  |
| Breezy | 2026-09-29T13:39 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-09-29T13:39 | 7 / 23 / 0 | COIN 46%, BITX 45% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| VWAP reversion | NVDA | 2.16 | +1.89% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 1 | 100.0 | 12.64 | 2.76 | -7.55 | 44 |
| 2 | Hold BTC | benchmark | 100.64 | 0.64 | 0 | — | 30.87 | 3.87 | -8.68 | 1 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 4 | Daily: Bullish score | daily | 100.37 | 0.37 | 2 | 0.0 | 0.08 | 0.21 | -12.76 | 13 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.89 | 1.49 | -2.35 | 88 |
| 6 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.28 | 0.83 | -3.92 | 92 |
| 7 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 6.57 | 1.24 | -7.93 | 7 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.32 | -5.20 | -9.99 | 207 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.89 | -0.11 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.88 | -0.12 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | RSI(14) reversion · 1h | reversion | 99.78 | -0.22 | 5 | 80.0 | 5.32 | 1.44 | -6.57 | 129 |
| 15 | Stochastic reversion · 1h | reversion | 99.76 | -0.24 | 26 | 53.8 | -9.90 | -2.12 | -12.28 | 324 |
| 16 | Hold SPY | benchmark | 99.66 | -0.34 | 0 | — | 4.11 | 2.13 | -3.66 | 1 |
| 17 | Williams %R · 1h | reversion | 99.51 | -0.49 | 33 | 51.5 | -18.01 | -3.36 | -20.18 | 484 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 99.41 | -0.59 | 0 | — | -3.46 | -2.12 | -5.09 | 2 |
| 19 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.88 | -4.39 | -14.73 | 121 |
| 20 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.42 | 4.07 | -4.73 | 191 |
| 21 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 22 | EMA 20/50 cross · 1h | trend | 99.13 | -0.87 | 8 | 12.5 | 17.98 | 2.12 | -14.36 | 125 |
| 23 | Z-score reversion · 1h | reversion | 99.13 | -0.87 | 7 | 57.1 | 3.75 | 0.94 | -8.60 | 154 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.13 | -0.87 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Candlestick reversal · 1h | reversion | 99.04 | -0.96 | 13 | 23.1 | -25.37 | -5.94 | -26.48 | 493 |
| 26 | CCI reversion · 1h | reversion | 99.04 | -0.96 | 28 | 42.9 | 3.29 | 0.71 | -12.41 | 404 |
| 27 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 28 | Copy: Insider buying | copy | 98.70 | -1.30 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Connors RSI(2) · 1h | reversion | 98.51 | -1.49 | 40 | 47.5 | -12.22 | -3.88 | -13.13 | 234 |
| 30 | Agent (rotation) | meta | 98.43 | -1.57 | 27 | 14.8 | -5.94 | -1.94 | -12.24 | 217 |
| 31 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.99 | -0.13 | -15.21 | 47 |
| 32 | Squeeze breakout · 1h | breakout | 98.34 | -1.66 | 7 | 14.3 | 12.45 | 2.10 | -11.07 | 105 |
| 33 | Supertrend · 1h | trend | 98.23 | -1.77 | 11 | 9.1 | 4.29 | 0.77 | -16.43 | 194 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 98.23 | -1.77 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 35 | Parabolic SAR · 1h | trend | 98.22 | -1.77 | 20 | 15.0 | -4.59 | -0.48 | -18.82 | 306 |
| 36 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 37 | MACD cross · 1h | trend | 97.99 | -2.01 | 32 | 9.4 | -13.90 | -2.20 | -19.12 | 458 |
| 38 | Daily: SMA 20/50 cross · AAPL | daily | 97.87 | -2.13 | 0 | — | -9.11 | -2.25 | -12.73 | 1 |
| 39 | Timing: Nasdaq FTD · TQQQ | daily | 97.78 | -2.22 | 0 | — | -11.15 | -2.30 | -15.27 | 2 |
| 40 | Bollinger reversion · 1h | reversion | 97.76 | -2.24 | 20 | 30.0 | -17.51 | -4.85 | -17.88 | 306 |
| 41 | Trend pullback · 1h | trend | 97.76 | -2.24 | 23 | 13.0 | -28.51 | -6.94 | -29.93 | 147 |
| 42 | Agent (ML meta-label) | meta | 97.70 | -2.30 | 80 | 11.2 | 1.10 | 0.35 | -13.64 | 381 |
| 43 | Donchian 55/20 · 1h | breakout | 97.69 | -2.31 | 9 | 0.0 | 4.92 | 0.85 | -16.96 | 114 |
| 44 | Max aggression: 5-day momentum | meta | 97.36 | -2.64 | 2 | 50.0 | 0.81 | 0.41 | -29.56 | 30 |
| 45 | Ichimoku · 1h | trend | 97.31 | -2.69 | 12 | 16.7 | 8.43 | 1.17 | -15.13 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 97.28 | -2.72 | 13 | 7.7 | 11.17 | 1.62 | -11.15 | 286 |
| 47 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 48 | MACD zero-line · 1h | trend | 97.16 | -2.84 | 15 | 6.7 | -2.79 | -0.20 | -14.64 | 222 |
| 49 | RSI momentum · 1h | momentum | 96.70 | -3.30 | 20 | 5.0 | 2.90 | 0.60 | -15.29 | 214 |
| 50 | Max aggression: 1-day momentum | meta | 96.70 | -3.30 | 2 | 0.0 | -31.34 | -1.73 | -49.41 | 43 |
| 51 | Triple EMA stack · 1h | trend | 96.32 | -3.68 | 26 | 7.7 | -4.41 | -0.33 | -22.57 | 225 |
| 52 | ADX DI cross · 1h | trend | 96.21 | -3.79 | 25 | 8.0 | -11.12 | -2.03 | -15.68 | 251 |
| 53 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 38 | 13.2 | -7.47 | -1.30 | -16.99 | 126 |
| 54 | VWAP momentum · 1h | momentum | 96.13 | -3.87 | 88 | 11.4 | -28.77 | -4.13 | -33.87 | 1233 |
| 55 | EMA 9/21 cross · 1h | trend | 95.99 | -4.01 | 36 | 13.9 | 3.75 | 0.70 | -16.92 | 309 |
| 56 | Donchian 20/10 · 1h | breakout | 95.93 | -4.07 | 12 | 16.7 | 9.55 | 1.40 | -12.78 | 216 |
| 57 | Three white soldiers | momentum | 95.40 | -4.60 | 42 | 19.0 | -51.89 | -28.81 | -52.20 | 626 |
| 58 | Volume breakout · 1h | breakout | 95.38 | -4.62 | 25 | 4.0 | 6.63 | 1.10 | -12.60 | 126 |
| 59 | Keltner breakout · 1h | breakout | 95.21 | -4.79 | 7 | 0.0 | -5.57 | -0.57 | -18.68 | 219 |
| 60 | OBV trend · 1h | momentum | 95.20 | -4.80 | 47 | 6.4 | -8.88 | -0.91 | -25.24 | 323 |
| 61 | Heikin-Ashi · 1h | trend | 95.00 | -5.00 | 35 | 11.4 | -21.18 | -3.11 | -29.64 | 679 |
| 62 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -70.67 | -21.25 | -71.16 | 1469 |
| 63 | ROC + volume · 1h | momentum | 91.68 | -8.32 | 45 | 6.7 | -3.80 | -0.33 | -17.28 | 408 |
| 64 | Donchian 55/20 | breakout | 89.62 | -10.38 | 80 | 11.2 | -67.77 | -15.52 | -68.51 | 1324 |
| 65 | Squeeze breakout | breakout | 89.59 | -10.41 | 75 | 6.7 | -59.80 | -18.61 | -60.81 | 1194 |
| 66 | EMA 20/50 cross | trend | 88.92 | -11.08 | 97 | 13.4 | -78.54 | -17.53 | -79.39 | 1487 |
| 67 | ROC + volume | momentum | 88.71 | -11.29 | 125 | 16.8 | -72.13 | -18.01 | -72.90 | 1663 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Volume breakout | breakout | 87.38 | -12.62 | 89 | 12.4 | -62.60 | -20.71 | -62.98 | 914 |
| 71 | Ichimoku | trend | 87.14 | -12.86 | 95 | 8.4 | -80.44 | -26.37 | -80.58 | 1763 |
| 72 | Keltner breakout | breakout | 87.00 | -13.00 | 130 | 10.0 | -84.74 | -35.08 | -85.05 | 1930 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.39 | -27.90 | -84.48 | 2076 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -70.22 | -16.26 | -71.75 | 1391 |
| 75 | Supertrend | trend | 84.49 | -15.51 | 149 | 16.1 | -87.09 | -24.35 | -87.54 | 1956 |
| 76 | MACD zero-line | trend | 83.68 | -16.32 | 162 | 14.8 | -91.56 | -36.05 | -91.81 | 2368 |
| 77 | Trend pullback | trend | 82.95 | -17.05 | 149 | 18.8 | -90.47 | -33.93 | -90.50 | 2287 |
| 78 | Donchian 20/10 | breakout | 82.80 | -17.20 | 170 | 17.1 | -90.78 | -29.99 | -91.02 | 2687 |
| 79 | Triple EMA stack | trend | 82.43 | -17.57 | 179 | 14.5 | -92.97 | -37.25 | -93.08 | 2629 |
| 80 | Bollinger breakout | breakout | 82.26 | -17.74 | 175 | 14.3 | -93.95 | -42.17 | -94.11 | 2880 |
| 81 | RSI momentum | momentum | 82.23 | -17.77 | 163 | 11.0 | -90.45 | -30.34 | -90.67 | 2408 |
| 82 | MFI reversion | reversion | 82.14 | -17.86 | 155 | 17.4 | -87.73 | -34.43 | -87.90 | 2163 |
| 83 | ADX DI cross | trend | 81.35 | -18.65 | 168 | 6.5 | -89.29 | -47.15 | -89.52 | 2127 |
| 84 | Connors RSI(2) | reversion | 79.46 | -20.54 | 214 | 15.9 | -96.37 | -42.15 | -96.37 | 3653 |
| 85 | EMA 9/21 cross | trend | 79.01 | -20.99 | 231 | 15.2 | -97.34 | -41.88 | -97.43 | 3547 |
| 86 | Consensus | meta | 78.73 | -21.27 | 168 | 7.1 | -94.82 | -30.83 | -94.84 | 2689 |
| 87 | Candlestick reversal | reversion | 78.52 | -21.48 | 208 | 14.4 | -99.33 | -51.28 | -99.33 | 5547 |
| 88 | Stochastic reversion | reversion | 77.93 | -22.07 | 267 | 22.5 | -95.85 | -47.84 | -95.88 | 4042 |
| 89 | OBV trend | momentum | 77.55 | -22.45 | 237 | 13.5 | -95.80 | -50.50 | -95.88 | 3570 |
| 90 | Bollinger reversion | reversion | 76.89 | -23.11 | 249 | 12.4 | -95.69 | -45.99 | -95.69 | 3665 |
| 91 | VWAP momentum | momentum | 76.32 | -23.68 | 301 | 9.0 | -98.42 | -36.51 | -98.45 | 5210 |
| 92 | CCI reversion | reversion | 75.08 | -24.92 | 181 | 5.5 | -98.41 | -51.19 | -98.42 | 4683 |
| 93 | Parabolic SAR | trend | 73.77 | -26.23 | 261 | 13.0 | -96.98 | -58.78 | -97.02 | 3668 |
| 94 | Williams %R | reversion | 73.53 | -26.47 | 266 | 18.8 | -99.51 | -61.02 | -99.51 | 6076 |
| 95 | MACD cross | trend | 73.26 | -26.74 | 213 | 10.8 | -99.70 | -63.63 | -99.71 | 6087 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -93.86 | -99.89 | 8344 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T13:35 | Max aggression: 5-day momentum | buy | SOXL | 97.41 | — | entry |
| 2026-09-29T13:35 | Max aggression: 5-day momentum | sell | SOL-USD | 97.41 | 0.58 | target is flat |
| 2026-09-29T13:35 | Max aggression: 1-day momentum | buy | LABU | 96.75 | — | entry |
| 2026-09-29T13:35 | Max aggression: 1-day momentum | sell | NVDA | 96.75 | -0.08 | target is flat |
| 2026-09-29T13:35 | Agent (rotation) | buy | SQQQ | 32.82 | — | entry |
| 2026-09-29T13:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 101.36 | — | entry |
| 2026-09-29T13:35 | Agent (ML meta-label) | buy | BTC-USD | 1.01 | — | entry |
| 2026-09-29T13:35 | Agent (ML meta-label) | buy | AMZN | 3.62 | — | entry |
| 2026-09-29T13:35 | Agent (ML meta-label) | sell | QQQ | 4.63 | 0.02 | selected signal exited |
| 2026-09-29T13:35 | Consensus | sell | DOGE-USD | 19.64 | -0.06 | target is flat |
| 2026-09-29T13:35 | CCI reversion · 1h | buy | TQQQ | 5.20 | — | entry |
| 2026-09-29T13:35 | CCI reversion · 1h | buy | TECL | 6.60 | — | entry |
| 2026-09-29T13:35 | CCI reversion · 1h | buy | SPY | 6.60 | — | entry |
| 2026-09-29T13:35 | CCI reversion · 1h | buy | AMD | 6.60 | — | entry |
| 2026-09-29T13:35 | Williams %R · 1h | buy | UPRO | 7.11 | — | entry |
| 2026-09-29T13:35 | Stochastic reversion · 1h | buy | MSTR | 7.56 | — | rebalance up |
| 2026-09-29T13:35 | Stochastic reversion · 1h | buy | META | 8.87 | — | rebalance up |
| 2026-09-29T13:35 | Stochastic reversion · 1h | buy | GOOGL | 8.92 | — | rebalance up |
| 2026-09-29T13:35 | Stochastic reversion · 1h | buy | ETHU | 8.58 | — | rebalance up |
| 2026-09-29T13:35 | Stochastic reversion · 1h | buy | BITX | 8.83 | — | rebalance up |
| 2026-09-29T13:35 | Stochastic reversion · 1h | sell | TSLA | 14.03 | -0.29 | stop-loss |
| 2026-09-29T13:35 | Z-score reversion · 1h | buy | TNA | 8.26 | — | rebalance up |
| 2026-09-29T13:35 | Z-score reversion · 1h | buy | SQQQ | 8.18 | — | rebalance up |
| 2026-09-29T13:35 | Z-score reversion · 1h | buy | IWM | 8.28 | — | rebalance up |
| 2026-09-29T13:35 | Bollinger reversion · 1h | sell | TSLA | 9.55 | -0.24 | stop-loss |
| 2026-09-29T13:35 | Connors RSI(2) · 1h | sell | AAPL | 24.47 | -0.29 | stop-loss |
| 2026-09-29T13:35 | RSI(14) reversion · 1h | buy | TNA | 8.25 | — | rebalance up |
| 2026-09-29T13:35 | RSI(14) reversion · 1h | buy | IWM | 8.27 | — | rebalance up |
| 2026-09-29T13:35 | RSI(14) reversion · 1h | sell | TSLA | 16.34 | -0.41 | stop-loss |
| 2026-09-29T13:35 | Bollinger breakout · 1h | buy | XRP-USD | 9.81 | — | rebalance up |
| 2026-09-29T13:35 | Bollinger breakout · 1h | sell | NVDA | 4.93 | 0.01 | rebalance down |
| 2026-09-29T13:35 | Bollinger breakout · 1h | sell | LABU | 4.88 | 0.03 | rebalance down |
| 2026-09-29T13:35 | Donchian 55/20 · 1h | sell | AMD | 9.58 | -0.41 | target is flat |
| 2026-09-29T13:35 | Donchian 20/10 · 1h | buy | XRP-USD | 4.95 | — | rebalance up |
| 2026-09-29T13:35 | Donchian 20/10 · 1h | sell | NVDA | 4.95 | 0.01 | rebalance down |
| 2026-09-29T13:35 | RSI momentum · 1h | buy | XRP-USD | 5.01 | — | rebalance up |
| 2026-09-29T13:35 | RSI momentum · 1h | sell | NVDA | 5.01 | 0.01 | rebalance down |
| 2026-09-29T13:35 | ROC + volume · 1h | buy | XRP-USD | 10.94 | — | entry |
| 2026-09-29T13:35 | ROC + volume · 1h | buy | SOL-USD | 13.11 | — | entry |
| 2026-09-29T13:35 | ROC + volume · 1h | buy | BTC-USD | 4.99 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
