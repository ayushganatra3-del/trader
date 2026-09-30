# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T17:40:05.000158+00:00 · 7125 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.76 (-0.24%)

Closed trades 25, win rate 68.0%, fees £0.74, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TQQQ | 39.97 | +0.11 |

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

Today: 28275 decisions in 2667 calls, $0.3543 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T17:40 | 8 / 8 / 13 | cash |  |
| Breezy | 2026-09-30T17:40 | 0 / 21 / 8 | cash |  |
| Boozy | 2026-09-30T17:40 | 5 / 19 / 5 | cash |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.73 | 1.73 | 2 | 50.0 | 14.77 | 3.18 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 3 | Copy: Congress Democrats (NANC) | copy | 100.45 | 0.45 | 0 | — | 7.25 | 2.95 | -3.62 | 1 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.25 | 0.25 | 1 | 100.0 | -0.08 | 0.06 | -9.74 | 24 |
| 5 | Hold BTC | benchmark | 100.18 | 0.18 | 0 | — | 29.43 | 3.69 | -8.68 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 99.83 | -0.17 | 0 | — | -2.76 | -1.63 | -5.09 | 2 |
| 9 | Agent | meta | 99.76 | -0.24 | 25 | 68.0 | -9.95 | -6.57 | -10.72 | 220 |
| 10 | Hold SPY | benchmark | 99.63 | -0.37 | 0 | — | 3.61 | 2.01 | -3.66 | 1 |
| 11 | Timing: Nasdaq FTD · TQQQ | daily | 99.57 | -0.43 | 0 | — | -9.26 | -1.81 | -15.27 | 2 |
| 12 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -12.32 | -4.18 | -14.45 | 121 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.61 | 1.33 | -2.15 | 83 |
| 14 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -0.41 | -0.21 | -3.92 | 97 |
| 15 | RSI(14) reversion · 1h | reversion | 99.49 | -0.51 | 8 | 62.5 | 1.72 | 0.56 | -6.57 | 125 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.47 | -0.53 | 0 | — | 4.66 | 1.35 | -7.93 | 7 |
| 17 | Copy: Insider buying | copy | 99.34 | -0.66 | 2 | 100.0 | -13.66 | -2.66 | -17.74 | 73 |
| 18 | Daily: Bullish score | daily | 99.31 | -0.69 | 3 | 0.0 | -0.08 | 0.19 | -12.76 | 14 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 99.14 | -0.86 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 21 | Copy: Warren Buffett (BRK-B) | copy | 99.07 | -0.93 | 0 | — | -1.63 | -0.62 | -7.65 | 1 |
| 22 | Stochastic reversion · 1h | reversion | 98.90 | -1.10 | 30 | 56.7 | -10.81 | -2.39 | -12.45 | 327 |
| 23 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 15.60 | 3.85 | -4.73 | 184 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 25 | Williams %R · 1h | reversion | 98.63 | -1.37 | 51 | 51.0 | -17.37 | -3.26 | -19.41 | 491 |
| 26 | CCI reversion · 1h | reversion | 98.48 | -1.52 | 42 | 40.5 | 2.01 | 0.50 | -12.41 | 414 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.46 | -1.54 | 0 | — | 23.84 | 3.51 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.27 | 0.23 | -15.21 | 46 |
| 29 | Candlestick reversal · 1h | reversion | 98.34 | -1.66 | 33 | 24.2 | -25.40 | -6.13 | -26.78 | 495 |
| 30 | Daily: SMA 20/50 cross · AAPL | daily | 98.22 | -1.78 | 0 | — | -6.34 | -1.42 | -10.06 | 1 |
| 31 | Z-score reversion · 1h | reversion | 98.14 | -1.85 | 11 | 45.5 | 4.64 | 1.12 | -8.60 | 156 |
| 32 | Agent (rotation) | meta | 98.10 | -1.90 | 36 | 13.9 | -5.19 | -1.79 | -9.79 | 208 |
| 33 | Connors RSI(2) · 1h | reversion | 97.98 | -2.02 | 48 | 45.8 | -11.04 | -3.49 | -11.76 | 233 |
| 34 | Bollinger reversion · 1h | reversion | 97.43 | -2.57 | 31 | 32.3 | -15.68 | -4.35 | -17.10 | 308 |
| 35 | EMA 20/50 cross · 1h | trend | 97.30 | -2.70 | 17 | 5.9 | 16.29 | 2.03 | -12.18 | 130 |
| 36 | Opening range 30m | breakout | 96.85 | -3.15 | 42 | 11.9 | -10.10 | -2.94 | -14.41 | 561 |
| 37 | Supertrend · 1h | trend | 96.37 | -3.63 | 18 | 5.6 | 1.10 | 0.35 | -16.43 | 203 |
| 38 | Max aggression: 5-day momentum | meta | 96.18 | -3.82 | 3 | 66.7 | -12.80 | -0.89 | -29.56 | 29 |
| 39 | Agent (ML meta-label) | meta | 96.11 | -3.89 | 159 | 13.2 | 3.50 | 0.79 | -11.96 | 396 |
| 40 | Trend pullback · 1h | trend | 96.06 | -3.94 | 30 | 10.0 | -25.39 | -6.81 | -25.72 | 155 |
| 41 | Opening range 15m | breakout | 95.85 | -4.15 | 50 | 12.0 | -11.55 | -3.15 | -16.70 | 689 |
| 42 | Donchian 55/20 · 1h | breakout | 95.64 | -4.36 | 15 | 0.0 | 4.92 | 0.84 | -16.96 | 113 |
| 43 | MFI reversion · 1h | reversion | 95.23 | -4.77 | 51 | 19.6 | -9.06 | -1.63 | -17.08 | 129 |
| 44 | Squeeze breakout · 1h | breakout | 95.05 | -4.95 | 15 | 6.7 | 12.32 | 2.18 | -7.19 | 99 |
| 45 | Parabolic SAR · 1h | trend | 95.05 | -4.95 | 30 | 13.3 | -8.69 | -1.10 | -19.53 | 303 |
| 46 | MACD cross · 1h | trend | 95.04 | -4.96 | 41 | 9.8 | -13.34 | -2.09 | -17.40 | 474 |
| 47 | Max aggression: 1-day momentum | meta | 94.81 | -5.19 | 3 | 33.3 | -21.01 | -0.99 | -41.28 | 42 |
| 48 | Three white soldiers | momentum | 94.58 | -5.42 | 49 | 20.4 | -50.14 | -27.50 | -50.37 | 607 |
| 49 | Volume breakout · 1h | breakout | 94.35 | -5.65 | 28 | 3.6 | 5.94 | 1.02 | -12.60 | 122 |
| 50 | ADX DI cross · 1h | trend | 94.20 | -5.80 | 33 | 6.1 | -15.50 | -2.90 | -17.60 | 259 |
| 51 | Ichimoku · 1h | trend | 93.66 | -6.34 | 20 | 15.0 | 5.54 | 0.85 | -15.13 | 122 |
| 52 | RSI momentum · 1h | momentum | 93.35 | -6.65 | 28 | 3.6 | -0.98 | 0.07 | -15.29 | 221 |
| 53 | Bollinger breakout · 1h | breakout | 93.32 | -6.68 | 24 | 8.3 | 6.36 | 1.03 | -9.63 | 280 |
| 54 | VWAP momentum · 1h | momentum | 93.00 | -7.00 | 123 | 15.4 | -36.45 | -5.74 | -36.53 | 1248 |
| 55 | Triple EMA stack · 1h | trend | 92.44 | -7.56 | 34 | 5.9 | -8.09 | -0.80 | -22.28 | 234 |
| 56 | MACD zero-line · 1h | trend | 92.14 | -7.86 | 23 | 4.3 | -7.87 | -0.92 | -16.22 | 232 |
| 57 | EMA 9/21 cross · 1h | trend | 91.92 | -8.08 | 46 | 10.9 | -7.67 | -0.86 | -16.92 | 321 |
| 58 | Keltner breakout · 1h | breakout | 91.84 | -8.16 | 14 | 0.0 | -7.16 | -0.80 | -19.94 | 216 |
| 59 | Donchian 20/10 · 1h | breakout | 91.37 | -8.63 | 21 | 9.5 | -0.53 | 0.15 | -13.70 | 222 |
| 60 | Heikin-Ashi · 1h | trend | 91.31 | -8.69 | 57 | 8.8 | -28.05 | -4.54 | -31.37 | 682 |
| 61 | RSI(14) reversion | reversion | 91.24 | -8.76 | 128 | 35.9 | -71.13 | -21.21 | -71.38 | 1476 |
| 62 | OBV trend · 1h | momentum | 89.92 | -10.09 | 64 | 6.2 | -13.76 | -1.59 | -25.03 | 332 |
| 63 | Squeeze breakout | breakout | 87.46 | -12.54 | 106 | 13.2 | -59.96 | -18.65 | -59.97 | 1184 |
| 64 | ROC + volume · 1h | momentum | 87.45 | -12.55 | 59 | 5.1 | -14.19 | -1.90 | -21.75 | 412 |
| 65 | Donchian 55/20 | breakout | 86.05 | -13.95 | 116 | 18.1 | -67.56 | -15.43 | -67.61 | 1294 |
| 66 | Volume breakout | breakout | 85.07 | -14.93 | 114 | 14.9 | -62.74 | -20.20 | -62.74 | 897 |
| 67 | ROC + volume | momentum | 84.73 | -15.27 | 178 | 20.2 | -73.17 | -18.00 | -73.17 | 1652 |
| 68 | Z-score reversion | reversion | 83.59 | -16.41 | 199 | 32.2 | -84.94 | -27.90 | -85.01 | 2098 |
| 69 | Keltner breakout | breakout | 83.47 | -16.54 | 171 | 14.6 | -84.68 | -34.61 | -84.69 | 1889 |
| 70 | VWAP reversion | reversion | 83.41 | -16.59 | 153 | 24.2 | -71.73 | -17.68 | -72.01 | 1413 |
| 71 | Ichimoku | trend | 83.30 | -16.70 | 134 | 9.7 | -80.36 | -25.77 | -80.37 | 1743 |
| 72 | EMA 20/50 cross | trend | 83.01 | -16.99 | 143 | 14.7 | -78.94 | -17.52 | -78.95 | 1478 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 79.93 | -20.07 | 197 | 17.8 | -87.41 | -24.50 | -87.51 | 1959 |
| 76 | MFI reversion | reversion | 79.76 | -20.24 | 197 | 19.8 | -88.12 | -35.33 | -88.18 | 2145 |
| 77 | Donchian 20/10 | breakout | 79.34 | -20.66 | 237 | 19.0 | -90.69 | -29.28 | -90.69 | 2665 |
| 78 | MACD zero-line | trend | 79.20 | -20.80 | 232 | 15.9 | -91.76 | -35.59 | -91.77 | 2353 |
| 79 | Trend pullback | trend | 78.59 | -21.41 | 194 | 18.0 | -90.67 | -33.03 | -90.68 | 2258 |
| 80 | Triple EMA stack | trend | 77.83 | -22.17 | 243 | 16.5 | -92.80 | -34.64 | -92.80 | 2582 |
| 81 | RSI momentum | momentum | 77.55 | -22.45 | 230 | 14.8 | -90.22 | -28.66 | -90.26 | 2381 |
| 82 | Bollinger breakout | breakout | 77.41 | -22.59 | 243 | 16.0 | -93.84 | -42.21 | -93.84 | 2846 |
| 83 | ADX DI cross | trend | 76.43 | -23.57 | 232 | 7.8 | -89.43 | -44.68 | -89.44 | 2119 |
| 84 | Consensus | meta | 74.35 | -25.65 | 209 | 7.2 | -94.69 | -30.50 | -94.71 | 2663 |
| 85 | Stochastic reversion | reversion | 74.24 | -25.76 | 362 | 24.0 | -95.96 | -45.28 | -95.96 | 4066 |
| 86 | EMA 9/21 cross | trend | 73.78 | -26.22 | 318 | 17.3 | -97.42 | -41.28 | -97.43 | 3531 |
| 87 | Connors RSI(2) | reversion | 73.47 | -26.53 | 296 | 19.3 | -96.43 | -40.60 | -96.43 | 3632 |
| 88 | Bollinger reversion | reversion | 72.69 | -27.31 | 339 | 15.9 | -95.83 | -43.80 | -95.83 | 3691 |
| 89 | Candlestick reversal | reversion | 72.67 | -27.33 | 327 | 14.4 | -99.36 | -48.30 | -99.36 | 5606 |
| 90 | OBV trend | momentum | 70.86 | -29.14 | 332 | 16.3 | -95.90 | -46.37 | -95.90 | 3529 |
| 91 | CCI reversion | reversion | 70.60 | -29.40 | 286 | 12.6 | -98.47 | -49.43 | -98.47 | 4688 |
| 92 | Parabolic SAR | trend | 70.08 | -29.92 | 311 | 13.2 | -96.92 | -53.27 | -96.93 | 3613 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.54 | -35.92 | -98.54 | 5242 |
| 94 | MACD cross | trend | 68.01 | -31.99 | 334 | 14.4 | -99.71 | -63.19 | -99.71 | 6067 |
| 95 | Williams %R | reversion | 67.59 | -32.41 | 405 | 21.5 | -99.53 | -57.17 | -99.53 | 6118 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -76.02 | -99.89 | 8285 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T17:40 | Agent (ML meta-label) | sell | TQQQ | 5.77 | 0.10 | selected signal exited |
| 2026-09-30T17:40 | Agent (ML meta-label) | sell | AAPL | 2.51 | -0.01 | selected signal exited |
| 2026-09-30T17:40 | Consensus | buy | TSLA | 18.59 | — | entry |
| 2026-09-30T17:40 | MFI reversion · 1h | buy | SOL-USD | 4.76 | — | rebalance up |
| 2026-09-30T17:40 | MFI reversion | buy | PLTR | 19.94 | — | entry signal |
| 2026-09-30T17:40 | CCI reversion | buy | UPRO | 6.40 | — | entry signal |
| 2026-09-30T17:40 | CCI reversion | buy | TQQQ | 6.42 | — | entry signal |
| 2026-09-30T17:40 | CCI reversion | buy | TECL | 6.42 | — | entry signal |
| 2026-09-30T17:40 | CCI reversion | buy | SPY | 6.42 | — | entry signal |
| 2026-09-30T17:40 | CCI reversion | buy | QQQ | 6.42 | — | entry signal |
| 2026-09-30T17:40 | CCI reversion | buy | AAPL | 6.42 | — | entry signal |
| 2026-09-30T17:40 | CCI reversion | sell | SOXL | 7.71 | 0.00 | rebalance down |
| 2026-09-30T17:40 | CCI reversion | sell | NVDA | 7.67 | -0.00 | rebalance down |
| 2026-09-30T17:40 | CCI reversion | sell | MSFT | 7.69 | 0.00 | rebalance down |
| 2026-09-30T17:40 | CCI reversion | sell | LABU | 7.75 | 0.03 | rebalance down |
| 2026-09-30T17:40 | CCI reversion | sell | AMZN | 7.69 | -0.00 | rebalance down |
| 2026-09-30T17:40 | Williams %R | buy | TQQQ | 3.14 | — | entry |
| 2026-09-30T17:40 | Williams %R | buy | PLTR | 3.56 | — | entry |
| 2026-09-30T17:40 | Williams %R | sell | DOGE-USD | 6.70 | -0.09 | stop-loss |
| 2026-09-30T17:40 | Z-score reversion | buy | PLTR | 4.42 | — | entry signal |
| 2026-09-30T17:40 | Z-score reversion | sell | TNA | 4.20 | 0.00 | rebalance down |
| 2026-09-30T17:40 | Bollinger reversion | buy | GOOGL | 6.06 | — | entry signal |
| 2026-09-30T17:40 | Bollinger reversion | sell | MSFT | 6.61 | 0.01 | exit signal |
| 2026-09-30T17:40 | Connors RSI(2) | buy | XRP-USD | 3.98 | — | rebalance up |
| 2026-09-30T17:40 | Connors RSI(2) | buy | SOL-USD | 3.97 | — | rebalance up |
| 2026-09-30T17:40 | Connors RSI(2) | buy | META | 3.94 | — | rebalance up |
| 2026-09-30T17:40 | Connors RSI(2) | buy | GOOGL | 3.94 | — | rebalance up |
| 2026-09-30T17:40 | Connors RSI(2) | buy | ETH-USD | 3.96 | — | rebalance up |
| 2026-09-30T17:40 | Connors RSI(2) | buy | BTC-USD | 3.95 | — | rebalance up |
| 2026-09-30T17:40 | Connors RSI(2) | buy | BITX | 3.95 | — | rebalance up |
| 2026-09-30T17:40 | Connors RSI(2) | sell | TQQQ | 5.28 | 0.01 | exit signal |
| 2026-09-30T17:40 | Connors RSI(2) | sell | TECL | 5.27 | 0.01 | exit signal |
| 2026-09-30T17:40 | Connors RSI(2) | sell | QQQ | 5.27 | 0.00 | exit signal |
| 2026-09-30T17:40 | Connors RSI(2) | sell | AMZN | 5.27 | 0.01 | exit signal |
| 2026-09-30T17:40 | Candlestick reversal | buy | DOGE-USD | 5.19 | — | entry signal |
| 2026-09-30T17:40 | Candlestick reversal | buy | BITX | 5.19 | — | entry signal |
| 2026-09-30T17:40 | Squeeze breakout | buy | TSLA | 21.87 | — | entry signal |
| 2026-09-30T17:40 | OBV trend | buy | MSFT | 17.61 | — | entry signal |
| 2026-09-30T17:40 | OBV trend | buy | LABU | 17.72 | — | entry |
| 2026-09-30T17:40 | OBV trend | buy | AMZN | 17.72 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
