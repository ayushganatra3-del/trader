# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T17:10:05.000146+00:00 · 7103 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.65 (-0.35%)

Closed trades 25, win rate 68.0%, fees £0.72, max drawdown -1.39%.

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

Today: 26355 decisions in 2601 calls, $0.3317 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T17:10 | 3 / 13 / 13 | AMD 15% |  |
| Breezy | 2026-09-30T17:10 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-09-30T17:10 | 4 / 24 / 1 | ETHU 58% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 102.10 | 2.10 | 2 | 50.0 | 15.19 | 3.25 | -7.55 | 43 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.61 | 0.60 | 1 | 100.0 | 0.29 | 0.18 | -9.74 | 24 |
| 3 | Hold BTC | benchmark | 100.55 | 0.55 | 0 | — | 29.75 | 3.72 | -8.68 | 1 |
| 4 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.41 | 0.41 | 0 | — | 7.01 | 2.85 | -3.62 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 99.94 | -0.06 | 0 | — | -2.64 | -1.55 | -5.09 | 2 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 99.92 | -0.08 | 0 | — | -8.92 | -1.72 | -15.27 | 2 |
| 10 | Daily: Bullish score | daily | 99.88 | -0.12 | 3 | 0.0 | 0.50 | 0.27 | -12.76 | 14 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.83 | -0.17 | 0 | — | 4.83 | 1.40 | -7.93 | 7 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.81 | -0.19 | 7 | 42.9 | 2.94 | 1.49 | -2.15 | 83 |
| 13 | Hold SPY | benchmark | 99.73 | -0.27 | 0 | — | 3.74 | 2.07 | -3.66 | 1 |
| 14 | Agent | meta | 99.65 | -0.35 | 25 | 68.0 | -10.04 | -6.65 | -10.72 | 219 |
| 15 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -12.32 | -4.18 | -14.45 | 121 |
| 16 | Copy: Insider buying | copy | 99.52 | -0.48 | 2 | 100.0 | -13.48 | -2.62 | -17.74 | 73 |
| 17 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -0.41 | -0.21 | -3.92 | 97 |
| 18 | RSI(14) reversion · 1h | reversion | 99.40 | -0.60 | 8 | 62.5 | 3.05 | 0.91 | -6.57 | 124 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 99.13 | -0.87 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 21 | Copy: Warren Buffett (BRK-B) | copy | 99.10 | -0.90 | 0 | — | -1.36 | -0.51 | -7.65 | 1 |
| 22 | Stochastic reversion · 1h | reversion | 99.09 | -0.91 | 30 | 56.7 | -10.54 | -2.32 | -12.41 | 326 |
| 23 | Williams %R · 1h | reversion | 98.99 | -1.01 | 51 | 51.0 | -16.97 | -3.17 | -19.41 | 491 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 24.09 | 3.54 | -6.29 | 1 |
| 25 | CCI reversion · 1h | reversion | 98.69 | -1.31 | 42 | 40.5 | 2.18 | 0.53 | -12.41 | 413 |
| 26 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 15.64 | 3.86 | -4.73 | 184 |
| 27 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 28 | Candlestick reversal · 1h | reversion | 98.43 | -1.57 | 33 | 24.2 | -25.04 | -6.07 | -26.51 | 498 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.34 | 0.24 | -15.21 | 46 |
| 30 | Agent (rotation) | meta | 98.32 | -1.68 | 35 | 14.3 | -4.96 | -1.71 | -9.79 | 208 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 98.28 | -1.72 | 0 | — | -6.31 | -1.41 | -10.06 | 1 |
| 32 | Z-score reversion · 1h | reversion | 98.18 | -1.82 | 11 | 45.5 | 4.66 | 1.12 | -8.60 | 156 |
| 33 | Connors RSI(2) · 1h | reversion | 98.10 | -1.90 | 47 | 46.8 | -10.93 | -3.45 | -11.76 | 233 |
| 34 | EMA 20/50 cross · 1h | trend | 97.69 | -2.31 | 17 | 5.9 | 16.77 | 2.08 | -12.18 | 128 |
| 35 | Bollinger reversion · 1h | reversion | 97.58 | -2.42 | 31 | 32.3 | -15.51 | -4.28 | -17.06 | 308 |
| 36 | Opening range 30m | breakout | 97.12 | -2.88 | 38 | 13.2 | -9.85 | -2.86 | -14.28 | 561 |
| 37 | Max aggression: 5-day momentum | meta | 96.97 | -3.03 | 3 | 66.7 | -12.07 | -0.81 | -29.56 | 29 |
| 38 | Supertrend · 1h | trend | 96.63 | -3.37 | 18 | 5.6 | 1.38 | 0.39 | -16.43 | 203 |
| 39 | Trend pullback · 1h | trend | 96.57 | -3.43 | 30 | 10.0 | -24.95 | -6.65 | -25.72 | 155 |
| 40 | Agent (ML meta-label) | meta | 96.41 | -3.59 | 157 | 12.7 | 4.06 | 0.86 | -10.40 | 396 |
| 41 | Opening range 15m | breakout | 96.04 | -3.96 | 49 | 12.2 | -11.35 | -3.09 | -16.70 | 689 |
| 42 | Donchian 55/20 · 1h | breakout | 95.88 | -4.12 | 15 | 0.0 | 5.19 | 0.88 | -16.96 | 113 |
| 43 | Max aggression: 1-day momentum | meta | 95.59 | -4.41 | 3 | 33.3 | -20.35 | -0.94 | -41.28 | 42 |
| 44 | MFI reversion · 1h | reversion | 95.51 | -4.49 | 51 | 19.6 | -8.75 | -1.56 | -17.08 | 129 |
| 45 | MACD cross · 1h | trend | 95.39 | -4.62 | 41 | 9.8 | -13.03 | -2.04 | -17.40 | 474 |
| 46 | Parabolic SAR · 1h | trend | 95.24 | -4.76 | 30 | 13.3 | -8.44 | -1.07 | -19.53 | 303 |
| 47 | Squeeze breakout · 1h | breakout | 95.14 | -4.86 | 15 | 6.7 | 12.43 | 2.20 | -7.19 | 99 |
| 48 | Three white soldiers | momentum | 94.58 | -5.42 | 49 | 20.4 | -50.19 | -27.63 | -50.39 | 608 |
| 49 | ADX DI cross · 1h | trend | 94.50 | -5.50 | 32 | 6.2 | -15.38 | -2.84 | -17.75 | 259 |
| 50 | Volume breakout · 1h | breakout | 94.43 | -5.57 | 28 | 3.6 | 6.04 | 1.04 | -12.60 | 122 |
| 51 | Ichimoku · 1h | trend | 93.90 | -6.10 | 20 | 15.0 | 5.81 | 0.88 | -15.13 | 123 |
| 52 | RSI momentum · 1h | momentum | 93.58 | -6.42 | 28 | 3.6 | -0.79 | 0.09 | -15.29 | 221 |
| 53 | VWAP momentum · 1h | momentum | 93.41 | -6.59 | 116 | 13.8 | -34.62 | -5.20 | -36.02 | 1250 |
| 54 | Bollinger breakout · 1h | breakout | 93.34 | -6.66 | 24 | 8.3 | 6.43 | 1.04 | -9.63 | 280 |
| 55 | Triple EMA stack · 1h | trend | 92.84 | -7.17 | 33 | 6.1 | -8.12 | -0.81 | -22.30 | 233 |
| 56 | MACD zero-line · 1h | trend | 92.62 | -7.38 | 23 | 4.3 | -7.44 | -0.86 | -16.22 | 232 |
| 57 | EMA 9/21 cross · 1h | trend | 92.27 | -7.73 | 46 | 10.9 | -7.24 | -0.80 | -16.92 | 320 |
| 58 | Keltner breakout · 1h | breakout | 91.85 | -8.15 | 14 | 0.0 | -8.25 | -0.96 | -19.84 | 216 |
| 59 | Donchian 20/10 · 1h | breakout | 91.58 | -8.42 | 21 | 9.5 | 0.30 | 0.25 | -13.48 | 222 |
| 60 | Heikin-Ashi · 1h | trend | 91.55 | -8.45 | 51 | 9.8 | -27.55 | -4.41 | -31.31 | 685 |
| 61 | RSI(14) reversion | reversion | 91.07 | -8.93 | 127 | 35.4 | -71.06 | -21.17 | -71.24 | 1486 |
| 62 | OBV trend · 1h | momentum | 90.36 | -9.64 | 64 | 6.2 | -13.44 | -1.54 | -25.03 | 330 |
| 63 | ROC + volume · 1h | momentum | 87.67 | -12.33 | 59 | 5.1 | -13.71 | -1.83 | -21.75 | 412 |
| 64 | Squeeze breakout | breakout | 87.59 | -12.41 | 106 | 13.2 | -59.69 | -18.55 | -59.73 | 1185 |
| 65 | Donchian 55/20 | breakout | 86.17 | -13.83 | 109 | 16.5 | -67.48 | -15.39 | -67.61 | 1294 |
| 66 | Volume breakout | breakout | 85.07 | -14.93 | 114 | 14.9 | -62.66 | -20.12 | -62.85 | 901 |
| 67 | ROC + volume | momentum | 84.99 | -15.01 | 177 | 20.3 | -72.75 | -17.75 | -72.86 | 1652 |
| 68 | Z-score reversion | reversion | 83.67 | -16.33 | 198 | 31.8 | -84.91 | -27.86 | -85.00 | 2096 |
| 69 | VWAP reversion | reversion | 83.61 | -16.39 | 152 | 23.7 | -71.73 | -17.71 | -72.04 | 1410 |
| 70 | Keltner breakout | breakout | 83.47 | -16.54 | 170 | 14.1 | -84.81 | -34.84 | -84.84 | 1901 |
| 71 | Ichimoku | trend | 83.40 | -16.60 | 133 | 9.8 | -80.35 | -25.80 | -80.40 | 1744 |
| 72 | EMA 20/50 cross | trend | 83.30 | -16.70 | 141 | 14.9 | -78.83 | -17.46 | -78.83 | 1477 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 80.21 | -19.79 | 196 | 17.9 | -87.41 | -24.54 | -87.55 | 1963 |
| 76 | MFI reversion | reversion | 79.85 | -20.15 | 196 | 19.9 | -88.15 | -35.44 | -88.24 | 2151 |
| 77 | Donchian 20/10 | breakout | 79.73 | -20.27 | 225 | 18.7 | -90.59 | -28.98 | -90.67 | 2677 |
| 78 | MACD zero-line | trend | 79.59 | -20.41 | 226 | 16.4 | -91.79 | -35.68 | -91.81 | 2355 |
| 79 | Trend pullback | trend | 78.94 | -21.06 | 184 | 19.0 | -90.56 | -32.94 | -90.61 | 2258 |
| 80 | Triple EMA stack | trend | 78.46 | -21.54 | 235 | 16.2 | -92.82 | -34.78 | -92.88 | 2587 |
| 81 | RSI momentum | momentum | 77.92 | -22.08 | 220 | 14.5 | -90.31 | -28.80 | -90.38 | 2383 |
| 82 | Bollinger breakout | breakout | 77.62 | -22.38 | 241 | 16.2 | -93.83 | -42.26 | -93.84 | 2860 |
| 83 | ADX DI cross | trend | 76.60 | -23.40 | 225 | 7.1 | -89.44 | -45.05 | -89.45 | 2115 |
| 84 | Stochastic reversion | reversion | 74.51 | -25.49 | 360 | 24.2 | -95.94 | -44.98 | -95.95 | 4060 |
| 85 | Consensus | meta | 74.48 | -25.52 | 206 | 6.8 | -94.68 | -30.43 | -94.69 | 2655 |
| 86 | EMA 9/21 cross | trend | 74.26 | -25.74 | 308 | 17.2 | -97.39 | -40.96 | -97.43 | 3542 |
| 87 | Connors RSI(2) | reversion | 73.86 | -26.14 | 288 | 18.1 | -96.41 | -40.48 | -96.41 | 3618 |
| 88 | Candlestick reversal | reversion | 73.06 | -26.94 | 321 | 14.3 | -99.36 | -49.23 | -99.36 | 5608 |
| 89 | Bollinger reversion | reversion | 72.99 | -27.01 | 337 | 16.0 | -95.80 | -43.41 | -95.83 | 3685 |
| 90 | OBV trend | momentum | 71.20 | -28.80 | 317 | 15.8 | -95.92 | -46.96 | -95.93 | 3533 |
| 91 | CCI reversion | reversion | 70.70 | -29.30 | 279 | 12.5 | -98.46 | -49.39 | -98.47 | 4698 |
| 92 | Parabolic SAR | trend | 70.15 | -29.85 | 309 | 13.3 | -96.95 | -54.11 | -96.96 | 3622 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.54 | -36.01 | -98.54 | 5249 |
| 94 | MACD cross | trend | 68.38 | -31.62 | 326 | 14.4 | -99.71 | -63.17 | -99.71 | 6069 |
| 95 | Williams %R | reversion | 67.95 | -32.05 | 399 | 21.8 | -99.53 | -57.19 | -99.53 | 6108 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -75.54 | -99.89 | 8289 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T17:10 | Consensus | buy | TQQQ | 18.62 | — | entry |
| 2026-09-30T17:10 | Williams %R | buy | DOGE-USD | 6.80 | — | entry signal |
| 2026-09-30T17:10 | Z-score reversion | sell | SOXL | 16.78 | 0.06 | exit signal |
| 2026-09-30T17:10 | Connors RSI(2) | sell | LABU | 18.48 | 0.01 | exit signal |
| 2026-09-30T17:10 | Connors RSI(2) | sell | DOGE-USD | 18.40 | -0.08 | exit signal |
| 2026-09-30T17:10 | Candlestick reversal | buy | TNA | 9.72 | — | entry signal |
| 2026-09-30T17:10 | Candlestick reversal | buy | PLTR | 12.19 | — | entry signal |
| 2026-09-30T17:10 | Candlestick reversal | buy | DOGE-USD | 12.19 | — | entry signal |
| 2026-09-30T17:10 | Candlestick reversal | sell | TECL | 6.11 | 0.01 | rebalance down |
| 2026-09-30T17:10 | Candlestick reversal | sell | SQQQ | 6.08 | -0.01 | rebalance down |
| 2026-09-30T17:10 | Squeeze breakout | sell | MSTR | 21.88 | -0.05 | exit signal |
| 2026-09-30T17:10 | Bollinger breakout | sell | MSTR | 15.51 | -0.04 | exit signal |
| 2026-09-30T17:10 | OBV trend | buy | TECL | 2.03 | — | entry signal |
| 2026-09-30T17:10 | OBV trend | buy | NVDA | 5.09 | — | entry signal |
| 2026-09-30T17:10 | OBV trend | sell | MSTR | 7.11 | -0.03 | exit signal |
| 2026-09-30T17:10 | ROC + volume | sell | BITX | 21.27 | 0.06 | exit signal |
| 2026-09-30T17:10 | Parabolic SAR | buy | META | 17.53 | — | entry signal |
| 2026-09-30T17:10 | MACD zero-line | sell | MSTR | 8.83 | -0.03 | exit signal |
| 2026-09-30T17:10 | MACD cross | buy | DOGE-USD | 6.84 | — | entry signal |
| 2026-09-30T17:10 | MACD cross | sell | MSTR | 4.55 | 0.01 | exit signal |
| 2026-09-30T17:10 | EMA 9/21 cross | buy | NVDA | 1.16 | — | entry signal |
| 2026-09-30T17:05 | MFI reversion | buy | PLTR | 19.96 | — | entry signal |
| 2026-09-30T17:05 | Williams %R | sell | SOXL | 6.19 | 0.02 | exit signal |
| 2026-09-30T17:05 | Stochastic reversion | buy | LABU | 8.55 | — | entry |
| 2026-09-30T17:05 | Stochastic reversion | sell | SPY | 4.27 | -0.00 | rebalance down |
| 2026-09-30T17:05 | Stochastic reversion | sell | MSFT | 4.28 | 0.00 | rebalance down |
| 2026-09-30T17:05 | Connors RSI(2) | buy | DOGE-USD | 18.48 | — | entry signal |
| 2026-09-30T17:05 | Squeeze breakout | sell | COIN | 21.86 | -0.08 | exit signal |
| 2026-09-30T17:05 | Bollinger breakout | buy | XRP-USD | 3.89 | — | rebalance up |
| 2026-09-30T17:05 | Bollinger breakout | buy | AMD | 3.89 | — | rebalance up |
| 2026-09-30T17:05 | Bollinger breakout | sell | COIN | 15.51 | -0.05 | exit signal |
| 2026-09-30T17:05 | Donchian 20/10 | buy | TSLA | 4.68 | — | entry signal |
| 2026-09-30T17:05 | OBV trend | buy | UPRO | 1.52 | — | entry signal |
| 2026-09-30T17:05 | OBV trend | buy | SOL-USD | 5.48 | — | entry signal |
| 2026-09-30T17:05 | OBV trend | buy | MSFT | 5.48 | — | entry |
| 2026-09-30T17:05 | OBV trend | buy | ETHU | 5.48 | — | entry |
| 2026-09-30T17:05 | OBV trend | sell | TNA | 8.64 | -0.00 | exit signal |
| 2026-09-30T17:05 | OBV trend | sell | IWM | 8.87 | 0.00 | exit signal |
| 2026-09-30T17:05 | Parabolic SAR | buy | TSLA | 17.54 | — | entry signal |
| 2026-09-30T17:05 | MACD zero-line | buy | AMD | 8.84 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
