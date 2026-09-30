# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T19:10:05.000178+00:00 · 7188 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.88 (-0.12%)

Closed trades 26, win rate 69.2%, fees £0.79, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TQQQ | 19.98 | +0.07 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-30 | ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, ADRX 12%, BBD 12%, ENHA 12%, CX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.07 · VIX 16.04 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 33870 decisions in 2856 calls, $0.4197 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T19:10 | 4 / 10 / 16 | AMD 18%, TECL 17%, SOXL 15% |  |
| Breezy | 2026-09-30T19:10 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-09-30T19:10 | 4 / 21 / 5 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| RSI(14) reversion · 1h | SOL-USD | 2.42 | +2.64% | 3 |
| Z-score reversion | MSFT | 2.34 | +2.58% | 5 |
| Williams %R | TQQQ | 2.04 | +2.09% | 14 |
| Candlestick reversal | TQQQ | 2.01 | +4.48% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.99 | 1.99 | 2 | 50.0 | 15.08 | 3.23 | -7.55 | 43 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.50 | 0.50 | 1 | 100.0 | 0.19 | 0.15 | -9.74 | 24 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.13 | 0.13 | 0 | — | 6.54 | 2.71 | -3.62 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Hold BTC | benchmark | 99.95 | -0.05 | 0 | — | 29.05 | 3.65 | -8.68 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 99.90 | -0.10 | 0 | — | -2.68 | -1.58 | -5.09 | 2 |
| 9 | Agent | meta | 99.88 | -0.12 | 26 | 69.2 | -9.94 | -6.50 | -10.81 | 220 |
| 10 | Timing: Nasdaq FTD · TQQQ | daily | 99.82 | -0.18 | 0 | — | -9.01 | -1.75 | -15.27 | 2 |
| 11 | VWAP reversion · 1h | reversion | 99.64 | -0.36 | 22 | 27.3 | -12.30 | -4.16 | -14.52 | 123 |
| 12 | Hold SPY | benchmark | 99.53 | -0.47 | 0 | — | 3.14 | 1.77 | -3.66 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.52 | -0.47 | 8 | 62.5 | 1.78 | 0.58 | -6.57 | 125 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.61 | 1.33 | -2.15 | 83 |
| 15 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -2.02 | -1.06 | -5.02 | 99 |
| 16 | Copy: Insider buying | copy | 99.45 | -0.55 | 2 | 100.0 | -13.54 | -2.64 | -17.74 | 73 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.31 | -0.69 | 0 | — | 3.43 | 1.03 | -7.93 | 7 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 19 | Daily: Bullish score | daily | 99.13 | -0.87 | 3 | 0.0 | -0.36 | 0.15 | -12.76 | 14 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 99.12 | -0.88 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 21 | Stochastic reversion · 1h | reversion | 98.96 | -1.04 | 30 | 56.7 | -9.90 | -2.19 | -11.62 | 324 |
| 22 | Copy: Warren Buffett (BRK-B) | copy | 98.79 | -1.21 | 0 | — | -1.70 | -0.64 | -7.65 | 1 |
| 23 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 15.60 | 3.85 | -4.73 | 184 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 25 | Williams %R · 1h | reversion | 98.63 | -1.36 | 51 | 51.0 | -17.03 | -3.19 | -19.41 | 490 |
| 26 | CCI reversion · 1h | reversion | 98.58 | -1.42 | 42 | 40.5 | 2.03 | 0.50 | -12.41 | 414 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.60 | 0.28 | -15.21 | 46 |
| 28 | Daily: SMA 20/50 cross · AAPL | daily | 98.35 | -1.65 | 0 | — | -6.62 | -1.49 | -10.04 | 1 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 98.32 | -1.68 | 0 | — | 23.40 | 3.47 | -6.29 | 1 |
| 30 | Candlestick reversal · 1h | reversion | 98.31 | -1.69 | 33 | 24.2 | -24.73 | -5.99 | -26.01 | 499 |
| 31 | Agent (rotation) | meta | 98.18 | -1.82 | 36 | 13.9 | -5.11 | -1.76 | -9.79 | 208 |
| 32 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.65 | -3.36 | -11.53 | 233 |
| 33 | Z-score reversion · 1h | reversion | 98.16 | -1.84 | 11 | 45.5 | 4.26 | 1.04 | -8.60 | 155 |
| 34 | Bollinger reversion · 1h | reversion | 97.60 | -2.40 | 32 | 34.4 | -15.49 | -4.28 | -17.06 | 308 |
| 35 | EMA 20/50 cross · 1h | trend | 97.41 | -2.59 | 18 | 5.6 | 16.50 | 2.06 | -12.18 | 130 |
| 36 | Opening range 30m | breakout | 96.78 | -3.22 | 42 | 11.9 | -9.80 | -2.83 | -14.44 | 560 |
| 37 | Supertrend · 1h | trend | 96.35 | -3.65 | 18 | 5.6 | 1.00 | 0.34 | -16.43 | 203 |
| 38 | Donchian 55/20 · 1h | breakout | 96.23 | -3.77 | 15 | 0.0 | 5.59 | 0.93 | -16.96 | 113 |
| 39 | Trend pullback · 1h | trend | 96.15 | -3.85 | 31 | 9.7 | -25.42 | -6.82 | -25.72 | 155 |
| 40 | Agent (ML meta-label) | meta | 96.11 | -3.89 | 159 | 13.2 | 5.08 | 1.03 | -11.68 | 389 |
| 41 | Max aggression: 5-day momentum | meta | 95.77 | -4.23 | 3 | 66.7 | -13.15 | -0.92 | -29.56 | 29 |
| 42 | Opening range 15m | breakout | 95.77 | -4.23 | 52 | 11.5 | -11.56 | -3.16 | -16.70 | 689 |
| 43 | Parabolic SAR · 1h | trend | 95.07 | -4.93 | 31 | 12.9 | -8.64 | -1.10 | -19.53 | 303 |
| 44 | MFI reversion · 1h | reversion | 95.02 | -4.98 | 51 | 19.6 | -9.28 | -1.68 | -17.11 | 130 |
| 45 | Squeeze breakout · 1h | breakout | 94.99 | -5.01 | 15 | 6.7 | 12.65 | 2.23 | -7.19 | 98 |
| 46 | MACD cross · 1h | trend | 94.86 | -5.14 | 45 | 8.9 | -13.45 | -2.11 | -17.38 | 475 |
| 47 | Three white soldiers | momentum | 94.48 | -5.52 | 51 | 19.6 | -50.24 | -27.70 | -50.32 | 606 |
| 48 | Max aggression: 1-day momentum | meta | 94.41 | -5.59 | 3 | 33.3 | -21.33 | -1.02 | -41.28 | 42 |
| 49 | ADX DI cross · 1h | trend | 94.40 | -5.61 | 33 | 6.1 | -15.29 | -2.85 | -17.60 | 259 |
| 50 | Volume breakout · 1h | breakout | 94.29 | -5.71 | 28 | 3.6 | 5.89 | 1.02 | -12.60 | 122 |
| 51 | Ichimoku · 1h | trend | 93.98 | -6.02 | 20 | 15.0 | 5.92 | 0.89 | -15.13 | 122 |
| 52 | RSI momentum · 1h | momentum | 93.44 | -6.55 | 28 | 3.6 | -1.35 | 0.01 | -15.29 | 220 |
| 53 | Bollinger breakout · 1h | breakout | 93.04 | -6.96 | 24 | 8.3 | 6.09 | 0.99 | -9.71 | 280 |
| 54 | VWAP momentum · 1h | momentum | 92.87 | -7.13 | 127 | 15.7 | -38.67 | -6.21 | -39.01 | 1248 |
| 55 | Triple EMA stack · 1h | trend | 92.45 | -7.55 | 35 | 5.7 | -8.24 | -0.82 | -22.08 | 235 |
| 56 | MACD zero-line · 1h | trend | 91.87 | -8.13 | 26 | 3.8 | -8.17 | -0.96 | -16.46 | 232 |
| 57 | EMA 9/21 cross · 1h | trend | 91.85 | -8.15 | 46 | 10.9 | -7.74 | -0.88 | -16.92 | 320 |
| 58 | Keltner breakout · 1h | breakout | 91.65 | -8.35 | 14 | 0.0 | -8.79 | -1.04 | -20.04 | 217 |
| 59 | Heikin-Ashi · 1h | trend | 91.27 | -8.73 | 59 | 8.5 | -28.07 | -4.54 | -31.39 | 683 |
| 60 | Donchian 20/10 · 1h | breakout | 91.02 | -8.98 | 21 | 9.5 | -0.67 | 0.13 | -14.01 | 222 |
| 61 | RSI(14) reversion | reversion | 90.98 | -9.03 | 129 | 35.7 | -71.21 | -21.30 | -71.38 | 1475 |
| 62 | OBV trend · 1h | momentum | 89.81 | -10.19 | 68 | 5.9 | -15.35 | -1.79 | -25.03 | 331 |
| 63 | Squeeze breakout | breakout | 87.43 | -12.57 | 109 | 12.8 | -59.67 | -18.51 | -59.75 | 1181 |
| 64 | ROC + volume · 1h | momentum | 87.41 | -12.59 | 59 | 5.1 | -14.44 | -1.94 | -21.75 | 413 |
| 65 | Donchian 55/20 | breakout | 86.06 | -13.94 | 118 | 18.6 | -67.27 | -15.24 | -67.35 | 1292 |
| 66 | Volume breakout | breakout | 85.16 | -14.84 | 114 | 14.9 | -62.76 | -20.22 | -62.81 | 888 |
| 67 | ROC + volume | momentum | 84.45 | -15.55 | 181 | 19.9 | -72.26 | -17.64 | -72.26 | 1628 |
| 68 | Keltner breakout | breakout | 83.50 | -16.50 | 172 | 14.5 | -84.60 | -34.42 | -84.63 | 1886 |
| 69 | VWAP reversion | reversion | 83.40 | -16.60 | 154 | 24.7 | -71.85 | -17.81 | -72.00 | 1407 |
| 70 | Z-score reversion | reversion | 83.40 | -16.60 | 200 | 32.0 | -84.97 | -27.97 | -85.01 | 2101 |
| 71 | EMA 20/50 cross | trend | 83.19 | -16.81 | 145 | 14.5 | -78.92 | -17.44 | -78.98 | 1471 |
| 72 | Ichimoku | trend | 83.16 | -16.84 | 136 | 9.6 | -80.24 | -25.47 | -80.27 | 1739 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 80.17 | -19.83 | 199 | 18.1 | -87.30 | -24.29 | -87.44 | 1959 |
| 76 | MFI reversion | reversion | 79.43 | -20.57 | 199 | 19.6 | -88.19 | -35.53 | -88.21 | 2136 |
| 77 | Donchian 20/10 | breakout | 79.22 | -20.78 | 243 | 18.9 | -90.58 | -28.98 | -90.61 | 2663 |
| 78 | MACD zero-line | trend | 79.05 | -20.95 | 239 | 15.9 | -91.64 | -35.24 | -91.64 | 2357 |
| 79 | Trend pullback | trend | 78.37 | -21.63 | 203 | 17.2 | -90.75 | -32.98 | -90.77 | 2272 |
| 80 | Triple EMA stack | trend | 77.65 | -22.35 | 247 | 16.2 | -92.84 | -34.89 | -92.87 | 2591 |
| 81 | RSI momentum | momentum | 77.53 | -22.47 | 234 | 15.0 | -90.35 | -28.96 | -90.38 | 2388 |
| 82 | Bollinger breakout | breakout | 77.26 | -22.74 | 247 | 15.8 | -93.85 | -42.17 | -93.85 | 2847 |
| 83 | ADX DI cross | trend | 76.29 | -23.71 | 233 | 8.2 | -89.46 | -44.76 | -89.46 | 2113 |
| 84 | Stochastic reversion | reversion | 74.10 | -25.90 | 373 | 24.9 | -95.90 | -45.57 | -95.90 | 4066 |
| 85 | EMA 9/21 cross | trend | 73.58 | -26.43 | 325 | 16.9 | -97.37 | -40.86 | -97.38 | 3535 |
| 86 | Consensus | meta | 73.56 | -26.44 | 222 | 6.8 | -94.64 | -30.57 | -94.66 | 2660 |
| 87 | Connors RSI(2) | reversion | 72.98 | -27.02 | 314 | 19.7 | -96.46 | -40.68 | -96.46 | 3640 |
| 88 | Bollinger reversion | reversion | 72.44 | -27.56 | 352 | 17.3 | -95.82 | -44.01 | -95.82 | 3690 |
| 89 | Candlestick reversal | reversion | 72.15 | -27.85 | 357 | 15.1 | -99.36 | -49.53 | -99.36 | 5630 |
| 90 | OBV trend | momentum | 70.57 | -29.43 | 347 | 15.6 | -95.92 | -46.42 | -95.93 | 3546 |
| 91 | CCI reversion | reversion | 70.50 | -29.50 | 298 | 14.1 | -98.47 | -49.23 | -98.47 | 4701 |
| 92 | Parabolic SAR | trend | 69.81 | -30.19 | 319 | 13.5 | -96.95 | -53.78 | -96.95 | 3617 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.53 | -35.70 | -98.54 | 5228 |
| 94 | MACD cross | trend | 67.70 | -32.30 | 348 | 14.4 | -99.72 | -62.93 | -99.72 | 6075 |
| 95 | Williams %R | reversion | 67.40 | -32.60 | 424 | 22.4 | -99.53 | -57.35 | -99.53 | 6117 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -75.28 | -99.89 | 8281 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T19:10 | Consensus | buy | SOXL | 18.22 | — | entry |
| 2026-09-30T19:10 | Consensus | buy | AMD | 18.40 | — | entry |
| 2026-09-30T19:10 | Agent | sell | TQQQ | 20.05 | 0.06 | rebalance down |
| 2026-09-30T19:10 | Williams %R | buy | XRP-USD | 4.22 | — | entry |
| 2026-09-30T19:10 | Williams %R | sell | QQQ | 3.96 | -0.00 | exit signal |
| 2026-09-30T19:10 | Candlestick reversal | buy | UPRO | 6.56 | — | entry |
| 2026-09-30T19:10 | Candlestick reversal | buy | GOOGL | 6.56 | — | entry |
| 2026-09-30T19:10 | Candlestick reversal | sell | XRP-USD | 6.54 | -0.03 | exit signal |
| 2026-09-30T19:10 | Candlestick reversal | sell | ETHU | 7.23 | 0.00 | exit signal |
| 2026-09-30T19:10 | Candlestick reversal | sell | DOGE-USD | 4.80 | -0.03 | exit signal |
| 2026-09-30T19:10 | Bollinger breakout | buy | SOXL | 19.12 | — | entry signal |
| 2026-09-30T19:10 | ROC + volume | buy | SOXL | 21.12 | — | entry signal |
| 2026-09-30T19:10 | ROC + volume | buy | AMD | 21.12 | — | entry signal |
| 2026-09-30T19:10 | ADX DI cross | buy | DOGE-USD | 19.09 | — | entry signal |
| 2026-09-30T19:10 | Parabolic SAR | buy | TSLA | 3.82 | — | entry signal |
| 2026-09-30T19:10 | Parabolic SAR | buy | SOXL | 3.93 | — | rebalance up |
| 2026-09-30T19:10 | Parabolic SAR | sell | SQQQ | 7.75 | -0.05 | exit signal |
| 2026-09-30T19:10 | MACD zero-line | buy | COIN | 7.94 | — | rebalance up |
| 2026-09-30T19:10 | MACD zero-line | sell | SQQQ | 15.71 | -0.07 | exit signal |
| 2026-09-30T19:10 | MACD cross | buy | QQQ | 2.56 | — | entry signal |
| 2026-09-30T19:10 | MACD cross | buy | NVDA | 3.22 | — | entry signal |
| 2026-09-30T19:10 | MACD cross | buy | MSFT | 3.22 | — | entry signal |
| 2026-09-30T19:10 | MACD cross | sell | SQQQ | 4.52 | -0.02 | exit signal |
| 2026-09-30T19:10 | MACD cross | sell | BTC-USD | 4.49 | -0.03 | exit signal |
| 2026-09-30T19:06 | CCI reversion | sell | META | 2.48 | 0.00 | exit signal |
| 2026-09-30T19:06 | Williams %R | buy | QQQ | 3.97 | — | entry |
| 2026-09-30T19:06 | Williams %R | sell | META | 4.22 | -0.00 | exit signal |
| 2026-09-30T19:06 | Stochastic reversion | sell | META | 5.29 | -0.01 | exit signal |
| 2026-09-30T19:06 | Connors RSI(2) | sell | NVDA | 18.25 | 0.00 | exit signal |
| 2026-09-30T19:06 | Candlestick reversal | buy | AMZN | 5.56 | — | entry signal |
| 2026-09-30T19:06 | Candlestick reversal | sell | BTC-USD | 6.53 | -0.04 | exit signal |
| 2026-09-30T19:06 | Donchian 55/20 | buy | SOXL | 21.49 | — | entry signal |
| 2026-09-30T19:06 | Donchian 20/10 | buy | SOXL | 8.20 | — | entry signal |
| 2026-09-30T19:06 | Donchian 20/10 | sell | TECL | 4.00 | 0.01 | rebalance down |
| 2026-09-30T19:06 | Donchian 20/10 | sell | AMD | 4.20 | 0.04 | rebalance down |
| 2026-09-30T19:06 | OBV trend | buy | TQQQ | 6.40 | — | entry signal |
| 2026-09-30T19:06 | OBV trend | buy | NVDA | 6.42 | — | entry signal |
| 2026-09-30T19:06 | OBV trend | buy | MSFT | 6.42 | — | entry signal |
| 2026-09-30T19:06 | OBV trend | buy | META | 6.42 | — | entry signal |
| 2026-09-30T19:06 | OBV trend | buy | GOOGL | 6.42 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
