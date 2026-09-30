# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T18:10:05.000142+00:00 · 7146 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.84 (-0.16%)

Closed trades 25, win rate 68.0%, fees £0.75, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TQQQ | 19.95 | +0.09 |

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

Today: 30156 decisions in 2730 calls, $0.3762 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T18:10 | 10 / 10 / 10 | AMD 15% |  |
| Breezy | 2026-09-30T18:10 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-09-30T18:10 | 7 / 21 / 2 | BITX 58% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.90 | 1.90 | 2 | 50.0 | 14.96 | 3.21 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.41 | 0.41 | 1 | 100.0 | 0.09 | 0.11 | -9.74 | 24 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.40 | 0.40 | 0 | — | 5.73 | 2.40 | -3.62 | 1 |
| 5 | Hold BTC | benchmark | 100.26 | 0.26 | 0 | — | 29.35 | 3.68 | -8.68 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 99.88 | -0.12 | 0 | — | -2.71 | -1.60 | -5.09 | 2 |
| 9 | Agent | meta | 99.84 | -0.16 | 25 | 68.0 | -9.87 | -6.51 | -10.72 | 220 |
| 10 | Timing: Nasdaq FTD · TQQQ | daily | 99.73 | -0.27 | 0 | — | -9.11 | -1.77 | -15.27 | 2 |
| 11 | Hold SPY | benchmark | 99.59 | -0.41 | 0 | — | 3.33 | 1.86 | -3.66 | 1 |
| 12 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -12.23 | -4.16 | -14.37 | 121 |
| 13 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 8 | 62.5 | 4.12 | 1.21 | -6.57 | 121 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.61 | 1.33 | -2.15 | 83 |
| 15 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -0.41 | -0.21 | -3.92 | 97 |
| 16 | Daily: Bullish score | daily | 99.43 | -0.57 | 3 | 0.0 | -0.04 | 0.19 | -12.76 | 14 |
| 17 | Copy: Insider buying | copy | 99.41 | -0.59 | 2 | 100.0 | -13.60 | -2.65 | -17.74 | 73 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.37 | -0.63 | 0 | — | 4.18 | 1.22 | -7.93 | 7 |
| 19 | Copy: Warren Buffett (BRK-B) | copy | 99.20 | -0.80 | 0 | — | -1.67 | -0.64 | -7.65 | 1 |
| 20 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 99.14 | -0.86 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 22 | Stochastic reversion · 1h | reversion | 98.95 | -1.05 | 30 | 56.7 | -10.52 | -2.33 | -12.21 | 326 |
| 23 | Williams %R · 1h | reversion | 98.70 | -1.30 | 51 | 51.0 | -16.96 | -3.17 | -19.41 | 490 |
| 24 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 15.60 | 3.85 | -4.73 | 184 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 98.61 | -1.39 | 0 | — | 23.68 | 3.49 | -6.29 | 1 |
| 27 | CCI reversion · 1h | reversion | 98.54 | -1.46 | 42 | 40.5 | 1.84 | 0.47 | -12.41 | 414 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.41 | 0.25 | -15.21 | 46 |
| 29 | Candlestick reversal · 1h | reversion | 98.34 | -1.66 | 33 | 24.2 | -24.56 | -5.90 | -26.25 | 489 |
| 30 | Daily: SMA 20/50 cross · AAPL | daily | 98.32 | -1.68 | 0 | — | -6.54 | -1.47 | -10.06 | 1 |
| 31 | Agent (rotation) | meta | 98.15 | -1.85 | 36 | 13.9 | -5.14 | -1.77 | -9.79 | 208 |
| 32 | Connors RSI(2) · 1h | reversion | 98.13 | -1.87 | 48 | 45.8 | -10.91 | -3.44 | -11.76 | 233 |
| 33 | Z-score reversion · 1h | reversion | 98.12 | -1.88 | 11 | 45.5 | 4.21 | 1.03 | -8.60 | 155 |
| 34 | Bollinger reversion · 1h | reversion | 97.49 | -2.51 | 31 | 32.3 | -15.28 | -4.23 | -17.06 | 308 |
| 35 | EMA 20/50 cross · 1h | trend | 97.44 | -2.56 | 17 | 5.9 | 16.07 | 2.01 | -12.18 | 131 |
| 36 | Opening range 30m | breakout | 96.84 | -3.16 | 42 | 11.9 | -10.11 | -2.94 | -14.43 | 561 |
| 37 | Supertrend · 1h | trend | 96.39 | -3.61 | 18 | 5.6 | 1.48 | 0.40 | -16.43 | 203 |
| 38 | Max aggression: 5-day momentum | meta | 96.32 | -3.68 | 3 | 66.7 | -12.67 | -0.87 | -29.56 | 29 |
| 39 | Trend pullback · 1h | trend | 96.16 | -3.84 | 31 | 9.7 | -25.42 | -6.82 | -25.72 | 155 |
| 40 | Agent (ML meta-label) | meta | 96.14 | -3.86 | 159 | 13.2 | -0.26 | 0.10 | -10.92 | 408 |
| 41 | Donchian 55/20 · 1h | breakout | 95.88 | -4.12 | 15 | 0.0 | 5.18 | 0.88 | -16.96 | 113 |
| 42 | Opening range 15m | breakout | 95.80 | -4.20 | 50 | 12.0 | -11.54 | -3.15 | -16.70 | 689 |
| 43 | MFI reversion · 1h | reversion | 95.26 | -4.74 | 51 | 19.6 | -9.04 | -1.63 | -17.08 | 129 |
| 44 | Parabolic SAR · 1h | trend | 95.09 | -4.92 | 30 | 13.3 | -8.64 | -1.10 | -19.53 | 303 |
| 45 | MACD cross · 1h | trend | 95.02 | -4.99 | 42 | 9.5 | -13.36 | -2.10 | -17.40 | 474 |
| 46 | Squeeze breakout · 1h | breakout | 94.98 | -5.02 | 15 | 6.7 | 12.22 | 2.18 | -7.19 | 98 |
| 47 | Max aggression: 1-day momentum | meta | 94.95 | -5.05 | 3 | 33.3 | -20.89 | -0.98 | -41.28 | 42 |
| 48 | Three white soldiers | momentum | 94.55 | -5.45 | 49 | 20.4 | -50.21 | -27.66 | -50.32 | 606 |
| 49 | ADX DI cross · 1h | trend | 94.30 | -5.70 | 33 | 6.1 | -15.25 | -2.85 | -17.45 | 259 |
| 50 | Volume breakout · 1h | breakout | 94.28 | -5.72 | 28 | 3.6 | 5.87 | 1.01 | -12.60 | 122 |
| 51 | Ichimoku · 1h | trend | 93.78 | -6.22 | 20 | 15.0 | 5.68 | 0.86 | -15.13 | 122 |
| 52 | RSI momentum · 1h | momentum | 93.41 | -6.59 | 28 | 3.6 | -0.77 | 0.09 | -15.29 | 221 |
| 53 | Bollinger breakout · 1h | breakout | 93.19 | -6.81 | 24 | 8.3 | 6.21 | 1.01 | -9.63 | 280 |
| 54 | VWAP momentum · 1h | momentum | 92.91 | -7.09 | 124 | 15.3 | -37.25 | -5.87 | -37.32 | 1246 |
| 55 | Triple EMA stack · 1h | trend | 92.58 | -7.42 | 34 | 5.9 | -7.56 | -0.73 | -22.28 | 234 |
| 56 | MACD zero-line · 1h | trend | 92.07 | -7.93 | 24 | 4.2 | -7.99 | -0.94 | -16.22 | 232 |
| 57 | EMA 9/21 cross · 1h | trend | 91.96 | -8.04 | 46 | 10.9 | -7.62 | -0.85 | -16.92 | 321 |
| 58 | Keltner breakout · 1h | breakout | 91.77 | -8.23 | 14 | 0.0 | -8.13 | -0.94 | -19.97 | 217 |
| 59 | Heikin-Ashi · 1h | trend | 91.34 | -8.66 | 57 | 8.8 | -28.02 | -4.53 | -31.38 | 682 |
| 60 | Donchian 20/10 · 1h | breakout | 91.24 | -8.76 | 21 | 9.5 | -0.23 | 0.18 | -13.74 | 222 |
| 61 | RSI(14) reversion | reversion | 91.23 | -8.77 | 128 | 35.9 | -71.08 | -21.19 | -71.29 | 1475 |
| 62 | OBV trend · 1h | momentum | 89.89 | -10.11 | 66 | 6.1 | -13.81 | -1.59 | -25.03 | 331 |
| 63 | Squeeze breakout | breakout | 87.47 | -12.53 | 107 | 13.1 | -59.68 | -18.52 | -59.70 | 1182 |
| 64 | ROC + volume · 1h | momentum | 87.44 | -12.56 | 59 | 5.1 | -14.20 | -1.90 | -21.75 | 412 |
| 65 | Donchian 55/20 | breakout | 86.01 | -13.99 | 117 | 18.8 | -67.52 | -15.40 | -67.53 | 1293 |
| 66 | Volume breakout | breakout | 85.07 | -14.93 | 114 | 14.9 | -62.89 | -20.24 | -62.89 | 898 |
| 67 | ROC + volume | momentum | 84.66 | -15.34 | 179 | 20.1 | -73.06 | -17.88 | -73.06 | 1647 |
| 68 | Z-score reversion | reversion | 83.55 | -16.45 | 200 | 32.0 | -84.94 | -27.90 | -85.01 | 2097 |
| 69 | VWAP reversion | reversion | 83.51 | -16.49 | 153 | 24.2 | -71.83 | -17.80 | -72.00 | 1407 |
| 70 | Keltner breakout | breakout | 83.48 | -16.52 | 171 | 14.6 | -84.75 | -34.65 | -84.76 | 1889 |
| 71 | Ichimoku | trend | 83.30 | -16.70 | 134 | 9.7 | -80.36 | -25.77 | -80.37 | 1743 |
| 72 | EMA 20/50 cross | trend | 83.01 | -16.99 | 144 | 14.6 | -78.85 | -17.44 | -78.86 | 1478 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 79.98 | -20.02 | 197 | 17.8 | -87.37 | -24.43 | -87.48 | 1959 |
| 76 | MFI reversion | reversion | 79.62 | -20.38 | 197 | 19.8 | -88.14 | -35.41 | -88.15 | 2136 |
| 77 | Donchian 20/10 | breakout | 79.34 | -20.66 | 240 | 19.2 | -90.65 | -29.16 | -90.66 | 2662 |
| 78 | MACD zero-line | trend | 79.17 | -20.83 | 233 | 15.9 | -91.71 | -35.41 | -91.71 | 2354 |
| 79 | Trend pullback | trend | 78.47 | -21.53 | 198 | 17.7 | -90.70 | -33.07 | -90.70 | 2265 |
| 80 | Triple EMA stack | trend | 77.60 | -22.40 | 243 | 16.5 | -92.81 | -34.64 | -92.81 | 2585 |
| 81 | RSI momentum | momentum | 77.49 | -22.51 | 232 | 14.7 | -90.27 | -28.77 | -90.27 | 2384 |
| 82 | Bollinger breakout | breakout | 77.46 | -22.54 | 244 | 16.0 | -93.82 | -42.06 | -93.83 | 2845 |
| 83 | ADX DI cross | trend | 76.44 | -23.56 | 232 | 7.8 | -89.40 | -44.38 | -89.41 | 2123 |
| 84 | Stochastic reversion | reversion | 74.25 | -25.75 | 367 | 24.8 | -95.95 | -45.10 | -95.95 | 4065 |
| 85 | Consensus | meta | 74.02 | -25.98 | 212 | 7.1 | -94.56 | -30.19 | -94.57 | 2648 |
| 86 | EMA 9/21 cross | trend | 73.59 | -26.41 | 320 | 17.2 | -97.40 | -41.08 | -97.41 | 3532 |
| 87 | Connors RSI(2) | reversion | 73.23 | -26.77 | 304 | 18.8 | -96.44 | -40.64 | -96.44 | 3637 |
| 88 | Bollinger reversion | reversion | 72.65 | -27.35 | 344 | 16.9 | -95.83 | -43.91 | -95.83 | 3698 |
| 89 | Candlestick reversal | reversion | 72.59 | -27.41 | 332 | 14.5 | -99.37 | -49.50 | -99.37 | 5623 |
| 90 | OBV trend | momentum | 70.63 | -29.37 | 338 | 16.0 | -95.88 | -45.89 | -95.88 | 3533 |
| 91 | CCI reversion | reversion | 70.63 | -29.37 | 290 | 13.4 | -98.46 | -49.33 | -98.47 | 4695 |
| 92 | Parabolic SAR | trend | 69.94 | -30.06 | 312 | 13.1 | -96.92 | -53.07 | -96.92 | 3615 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.55 | -36.04 | -98.55 | 5220 |
| 94 | MACD cross | trend | 68.02 | -31.98 | 335 | 14.3 | -99.71 | -62.92 | -99.71 | 6072 |
| 95 | Williams %R | reversion | 67.63 | -32.37 | 411 | 22.1 | -99.53 | -57.28 | -99.53 | 6111 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -76.57 | -99.89 | 8281 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T18:10 | Consensus | sell | LABU | 12.29 | -0.07 | target is flat |
| 2026-09-30T18:10 | Williams %R | buy | COIN | 2.27 | — | entry signal |
| 2026-09-30T18:10 | Connors RSI(2) | buy | UPRO | 18.30 | — | entry signal |
| 2026-09-30T18:10 | Connors RSI(2) | buy | SPY | 18.33 | — | entry signal |
| 2026-09-30T18:10 | Connors RSI(2) | sell | DOGE-USD | 18.27 | -0.13 | exit signal |
| 2026-09-30T18:10 | OBV trend | buy | SOXL | 7.85 | — | entry signal |
| 2026-09-30T18:10 | OBV trend | buy | NVDA | 7.85 | — | entry signal |
| 2026-09-30T18:10 | OBV trend | sell | UPRO | 7.03 | -0.03 | exit signal |
| 2026-09-30T18:10 | Trend pullback | buy | TQQQ | 4.07 | — | rebalance up |
| 2026-09-30T18:10 | Trend pullback | buy | TECL | 4.08 | — | rebalance up |
| 2026-09-30T18:10 | Trend pullback | buy | QQQ | 4.07 | — | rebalance up |
| 2026-09-30T18:10 | Trend pullback | buy | NVDA | 4.06 | — | rebalance up |
| 2026-09-30T18:10 | Trend pullback | buy | MSFT | 4.07 | — | rebalance up |
| 2026-09-30T18:10 | Trend pullback | buy | LABU | 4.07 | — | rebalance up |
| 2026-09-30T18:10 | Trend pullback | buy | AAPL | 4.08 | — | rebalance up |
| 2026-09-30T18:10 | Trend pullback | sell | AMZN | 7.13 | -0.01 | exit signal |
| 2026-09-30T18:10 | Parabolic SAR | buy | NVDA | 8.73 | — | entry |
| 2026-09-30T18:10 | Parabolic SAR | sell | AMZN | 8.73 | -0.03 | exit signal |
| 2026-09-30T18:10 | MACD cross | buy | NVDA | 1.34 | — | entry signal |
| 2026-09-30T18:10 | MACD cross | buy | IWM | 6.18 | — | entry |
| 2026-09-30T18:10 | MACD cross | sell | LABU | 7.53 | -0.04 | exit signal |
| 2026-09-30T18:05 | Williams %R | buy | SQQQ | 3.98 | — | entry signal |
| 2026-09-30T18:05 | Bollinger reversion | buy | XRP-USD | 2.85 | — | entry |
| 2026-09-30T18:05 | Bollinger reversion | buy | SOL-USD | 5.19 | — | entry |
| 2026-09-30T18:05 | Bollinger reversion | buy | META | 5.19 | — | entry |
| 2026-09-30T18:05 | Bollinger reversion | sell | TNA | 6.62 | 0.02 | exit signal |
| 2026-09-30T18:05 | Bollinger reversion | sell | IWM | 6.61 | 0.00 | exit signal |
| 2026-09-30T18:05 | Connors RSI(2) | buy | AMZN | 18.34 | — | entry signal |
| 2026-09-30T18:05 | OBV trend | sell | NVDA | 7.06 | -0.01 | exit signal |
| 2026-09-30T18:05 | OBV trend | sell | AAPL | 7.06 | -0.02 | exit signal |
| 2026-09-30T18:05 | Trend pullback | sell | UPRO | 7.10 | -0.02 | exit signal |
| 2026-09-30T18:05 | Trend pullback | sell | SPY | 7.14 | -0.01 | exit signal |
| 2026-09-30T18:00 | Consensus | buy | TQQQ | 12.35 | — | entry |
| 2026-09-30T18:00 | Consensus | buy | QQQ | 12.36 | — | entry |
| 2026-09-30T18:00 | Consensus | buy | LABU | 12.36 | — | entry |
| 2026-09-30T18:00 | Consensus | sell | TSLA | 6.25 | 0.01 | rebalance down |
| 2026-09-30T18:00 | Consensus | sell | GOOGL | 6.18 | -0.02 | rebalance down |
| 2026-09-30T18:00 | Consensus | sell | AMZN | 6.23 | 0.00 | rebalance down |
| 2026-09-30T18:00 | OBV trend · 1h | buy | LABU | 8.01 | — | entry |
| 2026-09-30T18:00 | OBV trend · 1h | buy | GOOGL | 8.19 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
