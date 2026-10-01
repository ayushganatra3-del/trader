# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-01T13:39:05.000184+00:00 · 7782 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.63 (-0.37%)

Closed trades 27, win rate 66.7%, fees £0.80, max drawdown -1.39%.

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

Today: 6071 decisions in 1108 calls, $0.0838 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-01T13:39 | 6 / 18 / 6 | ETHU 14% |  |
| Breezy | 2026-10-01T13:39 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-01T13:39 | 4 / 25 / 1 | COIN 69% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.65 | 0.65 | 3 | 33.3 | 13.54 | 2.91 | -7.55 | 44 |
| 2 | Copy: Congress Democrats (NANC) | copy | 100.53 | 0.53 | 0 | — | 5.59 | 2.33 | -3.62 | 1 |
| 3 | Hold BTC | benchmark | 100.09 | 0.09 | 0 | — | 33.24 | 4.12 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 100.04 | 0.04 | 0 | — | -2.81 | -1.66 | -5.09 | 2 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Timing: Nasdaq FTD · TQQQ | daily | 99.67 | -0.33 | 0 | — | -9.40 | -1.85 | -15.27 | 2 |
| 8 | Agent | meta | 99.63 | -0.37 | 27 | 66.7 | -10.35 | -6.81 | -10.92 | 224 |
| 9 | VWAP reversion · 1h | reversion | 99.62 | -0.38 | 23 | 30.4 | -10.76 | -3.66 | -14.05 | 114 |
| 10 | Hold SPY | benchmark | 99.54 | -0.46 | 0 | — | 3.13 | 1.73 | -3.66 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.61 | 1.32 | -2.15 | 83 |
| 12 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -1.50 | -0.81 | -4.46 | 99 |
| 13 | RSI(14) reversion · 1h | reversion | 99.49 | -0.51 | 9 | 55.6 | 5.73 | 1.60 | -6.57 | 124 |
| 14 | Daily: Bullish score | daily | 99.44 | -0.56 | 3 | 0.0 | 2.09 | 0.49 | -12.76 | 14 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.43 | -0.56 | 0 | — | -2.55 | -1.21 | -5.14 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 17 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 2 | 50.0 | -0.05 | 0.06 | -9.74 | 23 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.75 | -2.27 | -4.15 | 26 |
| 19 | Stochastic reversion · 1h | reversion | 98.95 | -1.05 | 30 | 56.7 | -8.50 | -1.83 | -9.96 | 322 |
| 20 | Copy: Warren Buffett (BRK-B) | copy | 98.81 | -1.19 | 0 | — | -2.31 | -0.90 | -7.65 | 1 |
| 21 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 15.10 | 3.71 | -4.73 | 182 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.65 | -1.35 | 0 | — | -0.69 | -0.08 | -7.93 | 7 |
| 24 | CCI reversion · 1h | reversion | 98.60 | -1.40 | 43 | 39.5 | 2.33 | 0.55 | -12.41 | 413 |
| 25 | Williams %R · 1h | reversion | 98.51 | -1.49 | 53 | 49.1 | -16.60 | -3.08 | -19.41 | 489 |
| 26 | Copy: Insider buying | copy | 98.40 | -1.60 | 2 | 100.0 | -14.82 | -2.91 | -17.74 | 75 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 1.76 | 0.46 | -15.21 | 46 |
| 28 | Candlestick reversal · 1h | reversion | 98.33 | -1.67 | 35 | 25.7 | -23.58 | -5.67 | -25.07 | 487 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 98.29 | -1.71 | 0 | — | 26.55 | 3.86 | -6.29 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -12.51 | -4.28 | -13.38 | 227 |
| 31 | Z-score reversion · 1h | reversion | 97.91 | -2.09 | 12 | 41.7 | 3.56 | 0.88 | -8.60 | 153 |
| 32 | Agent (rotation) | meta | 97.73 | -2.27 | 37 | 13.5 | -2.51 | -0.95 | -8.12 | 223 |
| 33 | Bollinger reversion · 1h | reversion | 97.51 | -2.49 | 32 | 34.4 | -16.72 | -4.67 | -18.03 | 305 |
| 34 | EMA 20/50 cross · 1h | trend | 97.23 | -2.77 | 20 | 5.0 | 13.19 | 1.76 | -12.17 | 131 |
| 35 | Daily: SMA 20/50 cross · AAPL | daily | 97.01 | -2.99 | 0 | — | 1.44 | 0.59 | -4.80 | 1 |
| 36 | Donchian 55/20 · 1h | breakout | 96.68 | -3.32 | 15 | 0.0 | 6.13 | 0.99 | -16.96 | 112 |
| 37 | Supertrend · 1h | trend | 96.47 | -3.52 | 19 | 5.3 | 1.62 | 0.42 | -16.43 | 195 |
| 38 | Opening range 30m | breakout | 96.12 | -3.88 | 49 | 12.2 | -11.23 | -3.24 | -15.06 | 559 |
| 39 | Agent (ML meta-label) | meta | 96.00 | -4.00 | 175 | 13.1 | 4.82 | 1.03 | -10.53 | 362 |
| 40 | Trend pullback · 1h | trend | 95.94 | -4.06 | 37 | 10.8 | -26.54 | -7.09 | -27.24 | 163 |
| 41 | Max aggression: 5-day momentum | meta | 95.62 | -4.38 | 4 | 50.0 | -13.53 | -0.95 | -29.56 | 30 |
| 42 | Parabolic SAR · 1h | trend | 94.89 | -5.11 | 36 | 11.1 | -9.58 | -1.22 | -19.53 | 306 |
| 43 | Opening range 15m | breakout | 94.87 | -5.13 | 61 | 14.8 | -12.31 | -3.35 | -17.03 | 686 |
| 44 | MFI reversion · 1h | reversion | 94.83 | -5.17 | 54 | 20.4 | -7.08 | -1.20 | -16.99 | 127 |
| 45 | MACD cross · 1h | trend | 94.67 | -5.33 | 53 | 9.4 | -17.17 | -2.89 | -19.76 | 487 |
| 46 | ADX DI cross · 1h | trend | 94.59 | -5.41 | 35 | 5.7 | -6.70 | -0.97 | -13.84 | 263 |
| 47 | Squeeze breakout · 1h | breakout | 94.49 | -5.51 | 16 | 6.2 | 19.43 | 2.79 | -7.61 | 105 |
| 48 | Max aggression: 1-day momentum | meta | 94.26 | -5.74 | 4 | 25.0 | -21.67 | -1.03 | -41.28 | 43 |
| 49 | Three white soldiers | momentum | 94.04 | -5.96 | 53 | 18.9 | -50.09 | -27.50 | -50.14 | 603 |
| 50 | Ichimoku · 1h | trend | 93.83 | -6.17 | 21 | 14.3 | 5.31 | 0.82 | -15.66 | 121 |
| 51 | Volume breakout · 1h | breakout | 93.79 | -6.21 | 29 | 3.4 | 5.32 | 0.93 | -12.60 | 122 |
| 52 | RSI momentum · 1h | momentum | 93.31 | -6.69 | 31 | 3.2 | -0.68 | 0.11 | -16.12 | 217 |
| 53 | VWAP momentum · 1h | momentum | 93.00 | -7.00 | 132 | 15.9 | -39.22 | -6.27 | -39.53 | 1256 |
| 54 | Bollinger breakout · 1h | breakout | 92.41 | -7.59 | 25 | 8.0 | 4.15 | 0.74 | -10.56 | 280 |
| 55 | Triple EMA stack · 1h | trend | 92.20 | -7.80 | 42 | 7.1 | -10.33 | -1.09 | -23.02 | 241 |
| 56 | MACD zero-line · 1h | trend | 91.53 | -8.47 | 29 | 6.9 | -5.61 | -0.53 | -17.53 | 230 |
| 57 | EMA 9/21 cross · 1h | trend | 91.53 | -8.47 | 55 | 10.9 | -8.61 | -0.99 | -17.94 | 324 |
| 58 | Heikin-Ashi · 1h | trend | 91.35 | -8.65 | 64 | 15.6 | -32.26 | -5.69 | -33.03 | 685 |
| 59 | Keltner breakout · 1h | breakout | 90.95 | -9.05 | 15 | 0.0 | -11.08 | -1.33 | -20.72 | 205 |
| 60 | Donchian 20/10 · 1h | breakout | 90.25 | -9.75 | 23 | 8.7 | 0.16 | 0.24 | -14.99 | 213 |
| 61 | RSI(14) reversion | reversion | 90.02 | -9.98 | 143 | 34.3 | -71.58 | -21.33 | -71.78 | 1483 |
| 62 | OBV trend · 1h | momentum | 89.48 | -10.52 | 74 | 6.8 | -16.99 | -2.07 | -26.38 | 342 |
| 63 | ROC + volume · 1h | momentum | 87.03 | -12.97 | 62 | 4.8 | -13.01 | -1.68 | -22.31 | 412 |
| 64 | Squeeze breakout | breakout | 86.37 | -13.63 | 115 | 13.0 | -59.12 | -17.72 | -59.44 | 1184 |
| 65 | Donchian 55/20 | breakout | 85.41 | -14.59 | 123 | 19.5 | -67.18 | -14.99 | -67.21 | 1294 |
| 66 | Volume breakout | breakout | 84.58 | -15.42 | 118 | 15.3 | -62.70 | -19.82 | -62.81 | 899 |
| 67 | ROC + volume | momentum | 83.15 | -16.85 | 190 | 19.5 | -72.24 | -17.37 | -72.62 | 1640 |
| 68 | VWAP reversion | reversion | 83.15 | -16.85 | 163 | 25.8 | -70.65 | -16.89 | -71.33 | 1378 |
| 69 | Keltner breakout | breakout | 82.30 | -17.70 | 179 | 14.5 | -84.36 | -32.59 | -84.36 | 1877 |
| 70 | Z-score reversion | reversion | 82.02 | -17.98 | 221 | 30.8 | -84.82 | -27.24 | -84.88 | 2094 |
| 71 | AI bee: Bizzy | ai | 81.73 | -18.27 | 302 | 8.9 | — | — | — | — |
| 72 | AI bee: Boozy | ai | 81.17 | -18.83 | 111 | 0.9 | — | — | — | — |
| 73 | EMA 20/50 cross | trend | 80.99 | -19.01 | 159 | 15.1 | -79.09 | -17.24 | -79.10 | 1477 |
| 74 | Ichimoku | trend | 80.81 | -19.19 | 149 | 9.4 | -80.57 | -25.33 | -80.60 | 1752 |
| 75 | MFI reversion | reversion | 78.26 | -21.74 | 212 | 19.8 | -87.99 | -33.64 | -88.10 | 2131 |
| 76 | Trend pullback | trend | 77.45 | -22.55 | 215 | 16.7 | -91.05 | -33.08 | -91.05 | 2292 |
| 77 | Supertrend | trend | 76.79 | -23.21 | 218 | 17.9 | -87.26 | -23.77 | -87.26 | 1933 |
| 78 | MACD zero-line | trend | 75.95 | -24.05 | 262 | 15.3 | -91.53 | -33.10 | -91.59 | 2352 |
| 79 | Donchian 20/10 | breakout | 75.53 | -24.47 | 265 | 18.1 | -90.60 | -27.95 | -90.67 | 2665 |
| 80 | Triple EMA stack | trend | 75.33 | -24.67 | 267 | 15.7 | -92.93 | -33.98 | -92.93 | 2598 |
| 81 | Bollinger breakout | breakout | 75.22 | -24.78 | 263 | 15.6 | -93.67 | -38.12 | -93.74 | 2838 |
| 82 | RSI momentum | momentum | 74.42 | -25.58 | 254 | 14.6 | -90.29 | -27.85 | -90.29 | 2377 |
| 83 | ADX DI cross | trend | 74.39 | -25.61 | 247 | 7.7 | -89.48 | -42.08 | -89.57 | 2121 |
| 84 | Stochastic reversion | reversion | 72.62 | -27.38 | 402 | 23.6 | -95.74 | -42.84 | -95.77 | 4023 |
| 85 | Consensus | meta | 72.57 | -27.43 | 232 | 7.3 | -94.58 | -29.47 | -94.58 | 2644 |
| 86 | Connors RSI(2) | reversion | 71.35 | -28.65 | 326 | 19.3 | -96.56 | -39.97 | -96.56 | 3646 |
| 87 | Bollinger reversion | reversion | 70.29 | -29.71 | 385 | 16.4 | -95.82 | -42.47 | -95.84 | 3685 |
| 88 | Candlestick reversal | reversion | 69.29 | -30.71 | 397 | 14.4 | -99.34 | -47.25 | -99.34 | 5609 |
| 89 | EMA 9/21 cross | trend | 69.22 | -30.78 | 363 | 15.7 | -97.34 | -38.78 | -97.37 | 3533 |
| 90 | OBV trend | momentum | 68.90 | -31.10 | 369 | 15.7 | -95.98 | -44.32 | -95.98 | 3565 |
| 91 | CCI reversion | reversion | 68.64 | -31.36 | 338 | 13.3 | -98.46 | -46.99 | -98.47 | 4687 |
| 92 | Parabolic SAR | trend | 67.71 | -32.29 | 343 | 12.8 | -96.98 | -50.26 | -96.99 | 3630 |
| 93 | VWAP momentum | momentum | 66.10 | -33.90 | 430 | 8.8 | -98.61 | -35.60 | -98.61 | 5269 |
| 94 | MACD cross | trend | 65.65 | -34.34 | 387 | 13.4 | -99.71 | -57.15 | -99.71 | 6068 |
| 95 | Williams %R | reversion | 64.96 | -35.04 | 465 | 21.1 | -99.52 | -53.27 | -99.52 | 6097 |
| 96 | Heikin-Ashi | trend | 64.81 | -35.19 | 347 | 6.1 | -99.89 | -68.14 | -99.89 | 8276 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-01T13:38 | AI bee: Boozy | buy | COIN | 56.26 | — | Jev: buy (buy p=0.69) |
| 2026-10-01T13:38 | AI bee: Boozy | sell | ETH-USD | 41.85 | -0.13 | Jev: sell |
| 2026-10-01T13:37 | CCI reversion | buy | XRP-USD | 3.44 | — | rebalance up |
| 2026-10-01T13:37 | CCI reversion | sell | SOL-USD | 3.46 | -0.01 | rebalance down |
| 2026-10-01T13:35 | Max aggression: 5-day momentum | buy | LABU | 95.67 | — | entry |
| 2026-10-01T13:35 | Max aggression: 5-day momentum | sell | BITX | 95.67 | -3.46 | target is flat |
| 2026-10-01T13:35 | Max aggression: 1-day momentum | buy | TSLA | 94.31 | — | entry |
| 2026-10-01T13:35 | Max aggression: 1-day momentum | sell | BITX | 94.31 | -3.42 | target is flat |
| 2026-10-01T13:35 | Agent (rotation) | buy | TSLA | 8.15 | — | entry |
| 2026-10-01T13:35 | Agent (rotation) | buy | TQQQ | 32.59 | — | following Williams %R |
| 2026-10-01T13:35 | Agent (rotation) | buy | TNA | 8.15 | — | entry |
| 2026-10-01T13:35 | Agent (rotation) | buy | IWM | 8.15 | — | entry |
| 2026-10-01T13:35 | Agent (rotation) | buy | COIN | 8.15 | — | following Connors RSI(2) · 1h |
| 2026-10-01T13:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | TQQQ | 100.70 | — | entry |
| 2026-10-01T13:35 | Agent (ML meta-label) | buy | TQQQ | 5.05 | — | following Williams %R |
| 2026-10-01T13:35 | Agent (ML meta-label) | buy | QQQ | 5.05 | — | entry |
| 2026-10-01T13:35 | Agent (ML meta-label) | sell | PLTR | 4.36 | 0.00 | selected signal exited |
| 2026-10-01T13:35 | Agent (ML meta-label) | sell | AAPL | 3.79 | -0.06 | selected signal exited |
| 2026-10-01T13:35 | MFI reversion · 1h | buy | LABU | 18.97 | — | entry |
| 2026-10-01T13:35 | MFI reversion · 1h | sell | SQQQ | 9.16 | -0.06 | target is flat |
| 2026-10-01T13:35 | MFI reversion · 1h | sell | SPY | 15.78 | 0.01 | target is flat |
| 2026-10-01T13:35 | CCI reversion · 1h | buy | BTC-USD | 6.16 | — | entry |
| 2026-10-01T13:35 | CCI reversion · 1h | sell | AAPL | 6.43 | -0.12 | target is flat |
| 2026-10-01T13:35 | Williams %R · 1h | buy | MSTR | 2.20 | — | entry |
| 2026-10-01T13:35 | Williams %R · 1h | buy | ETH-USD | 5.85 | — | rebalance up |
| 2026-10-01T13:35 | Williams %R · 1h | sell | AAPL | 8.06 | -0.15 | target is flat |
| 2026-10-01T13:35 | VWAP reversion · 1h | sell | MSTR | 24.97 | 0.09 | target is flat |
| 2026-10-01T13:35 | Z-score reversion · 1h | buy | TSLA | 9.32 | — | rebalance up |
| 2026-10-01T13:35 | Z-score reversion · 1h | buy | TNA | 5.09 | — | rebalance up |
| 2026-10-01T13:35 | Z-score reversion · 1h | sell | AAPL | 24.09 | -0.45 | target is flat |
| 2026-10-01T13:35 | RSI(14) reversion · 1h | sell | AAPL | 24.42 | -0.46 | target is flat |
| 2026-10-01T13:35 | Candlestick reversal · 1h | buy | XRP-USD | 7.54 | — | entry |
| 2026-10-01T13:35 | Candlestick reversal · 1h | sell | META | 7.54 | 0.05 | target is flat |
| 2026-10-01T13:35 | OBV trend · 1h | buy | META | 11.19 | — | entry |
| 2026-10-01T13:35 | OBV trend · 1h | buy | ETH-USD | 11.19 | — | entry |
| 2026-10-01T13:35 | OBV trend · 1h | sell | QQQ | 8.22 | 0.02 | target is flat |
| 2026-10-01T13:35 | OBV trend · 1h | sell | PLTR | 8.15 | -0.07 | target is flat |
| 2026-10-01T13:35 | OBV trend · 1h | sell | NVDA | 8.22 | -0.01 | target is flat |
| 2026-10-01T13:35 | OBV trend · 1h | sell | AMD | 9.90 | -0.01 | target is flat |
| 2026-10-01T13:35 | RSI momentum · 1h | sell | PLTR | 8.37 | -0.14 | target is flat |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
