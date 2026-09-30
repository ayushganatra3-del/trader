# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T16:10:05.000136+00:00 · 7052 ticks

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

Today: 21837 decisions in 2448 calls, $0.2789 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T16:10 | 8 / 16 / 6 | COIN 15% |  |
| Breezy | 2026-09-30T16:10 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-09-30T16:10 | 6 / 20 / 4 | COIN 75% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 102.14 | 2.14 | 2 | 50.0 | 15.41 | 3.29 | -7.55 | 43 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.65 | 0.65 | 1 | 100.0 | 0.48 | 0.25 | -9.74 | 24 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 4 | Hold BTC | benchmark | 100.46 | 0.46 | 0 | — | 29.88 | 3.74 | -8.68 | 1 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.23 | 0.23 | 0 | — | 7.23 | 2.94 | -3.62 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 99.96 | -0.04 | 0 | — | -8.75 | -1.68 | -15.27 | 2 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 99.86 | -0.14 | 0 | — | -2.58 | -1.50 | -5.09 | 2 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.83 | -0.17 | 7 | 42.9 | 3.04 | 1.54 | -2.15 | 83 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.79 | -0.21 | 0 | — | 5.41 | 1.54 | -7.93 | 7 |
| 12 | Daily: Bullish score | daily | 99.76 | -0.24 | 3 | 0.0 | 0.62 | 0.29 | -12.76 | 14 |
| 13 | Agent | meta | 99.65 | -0.35 | 25 | 68.0 | -9.94 | -6.60 | -10.71 | 214 |
| 14 | Hold SPY | benchmark | 99.65 | -0.35 | 0 | — | 3.88 | 2.14 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -12.64 | -4.25 | -14.76 | 122 |
| 16 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -0.41 | -0.21 | -3.92 | 97 |
| 17 | RSI(14) reversion · 1h | reversion | 99.43 | -0.57 | 8 | 62.5 | 4.00 | 1.17 | -6.57 | 125 |
| 18 | Copy: Insider buying | copy | 99.19 | -0.81 | 2 | 100.0 | -13.64 | -2.66 | -17.74 | 73 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 20 | Gap and go | momentum | 99.12 | -0.88 | 10 | 10.0 | 16.20 | 3.98 | -4.73 | 184 |
| 21 | Stochastic reversion · 1h | reversion | 99.07 | -0.93 | 29 | 55.2 | -11.65 | -2.56 | -13.58 | 326 |
| 22 | Copy: Warren Buffett (BRK-B) | copy | 99.00 | -1.00 | 0 | — | -1.34 | -0.50 | -7.65 | 1 |
| 23 | Copy: Hedge-fund gurus (GURU) | copy | 98.98 | -1.02 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.89 | -1.11 | 2 | 0.0 | -0.28 | -0.04 | -4.88 | 18 |
| 25 | Williams %R · 1h | reversion | 98.81 | -1.19 | 50 | 50.0 | -16.96 | -3.16 | -19.41 | 489 |
| 26 | CCI reversion · 1h | reversion | 98.66 | -1.34 | 40 | 37.5 | 2.26 | 0.54 | -12.41 | 411 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.59 | -1.41 | 0 | — | 24.13 | 3.54 | -6.29 | 1 |
| 28 | Agent (rotation) | meta | 98.48 | -1.52 | 33 | 12.1 | -4.72 | -1.61 | -9.79 | 208 |
| 29 | Candlestick reversal · 1h | reversion | 98.44 | -1.56 | 33 | 24.2 | -25.15 | -6.07 | -26.42 | 499 |
| 30 | Daily: SMA 20/50 cross · AAPL | daily | 98.37 | -1.63 | 0 | — | -5.72 | -1.25 | -10.06 | 1 |
| 31 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.28 | 0.23 | -15.21 | 46 |
| 32 | Z-score reversion · 1h | reversion | 98.20 | -1.80 | 11 | 45.5 | 4.79 | 1.15 | -8.60 | 154 |
| 33 | Connors RSI(2) · 1h | reversion | 97.94 | -2.06 | 47 | 46.8 | -11.01 | -3.48 | -11.76 | 233 |
| 34 | EMA 20/50 cross · 1h | trend | 97.61 | -2.39 | 17 | 5.9 | 16.80 | 2.09 | -12.18 | 128 |
| 35 | Bollinger reversion · 1h | reversion | 97.47 | -2.53 | 31 | 32.3 | -15.47 | -4.27 | -17.07 | 308 |
| 36 | Opening range 30m | breakout | 97.22 | -2.78 | 38 | 13.2 | -9.64 | -2.79 | -14.28 | 561 |
| 37 | Max aggression: 5-day momentum | meta | 96.90 | -3.10 | 3 | 66.7 | -12.01 | -0.81 | -29.56 | 29 |
| 38 | Trend pullback · 1h | trend | 96.57 | -3.43 | 30 | 10.0 | -24.82 | -6.55 | -25.81 | 151 |
| 39 | Supertrend · 1h | trend | 96.55 | -3.45 | 18 | 5.6 | 1.52 | 0.41 | -16.43 | 203 |
| 40 | Agent (ML meta-label) | meta | 96.34 | -3.66 | 156 | 12.8 | 4.22 | 0.91 | -11.42 | 385 |
| 41 | Opening range 15m | breakout | 96.04 | -3.96 | 49 | 12.2 | -11.14 | -3.02 | -16.70 | 689 |
| 42 | Donchian 55/20 · 1h | breakout | 95.81 | -4.19 | 15 | 0.0 | 5.27 | 0.89 | -16.96 | 113 |
| 43 | Max aggression: 1-day momentum | meta | 95.52 | -4.48 | 3 | 33.3 | -20.29 | -0.94 | -41.28 | 42 |
| 44 | MACD cross · 1h | trend | 95.40 | -4.60 | 41 | 9.8 | -13.04 | -2.04 | -17.55 | 473 |
| 45 | Parabolic SAR · 1h | trend | 95.26 | -4.74 | 30 | 13.3 | -8.28 | -1.04 | -19.53 | 303 |
| 46 | MFI reversion · 1h | reversion | 95.25 | -4.75 | 50 | 18.0 | -8.87 | -1.59 | -17.08 | 130 |
| 47 | Squeeze breakout · 1h | breakout | 95.10 | -4.90 | 15 | 6.7 | 12.86 | 2.27 | -7.19 | 98 |
| 48 | Three white soldiers | momentum | 94.60 | -5.40 | 48 | 18.8 | -50.16 | -27.60 | -50.39 | 608 |
| 49 | ADX DI cross · 1h | trend | 94.41 | -5.59 | 32 | 6.2 | -15.31 | -2.82 | -17.86 | 258 |
| 50 | Volume breakout · 1h | breakout | 94.40 | -5.61 | 28 | 3.6 | 5.67 | 0.99 | -12.60 | 123 |
| 51 | Ichimoku · 1h | trend | 93.90 | -6.10 | 20 | 15.0 | 5.92 | 0.89 | -15.13 | 122 |
| 52 | RSI momentum · 1h | momentum | 93.67 | -6.33 | 28 | 3.6 | -1.19 | 0.04 | -15.29 | 220 |
| 53 | Bollinger breakout · 1h | breakout | 93.51 | -6.49 | 24 | 8.3 | 6.70 | 1.07 | -9.63 | 280 |
| 54 | VWAP momentum · 1h | momentum | 93.47 | -6.53 | 114 | 13.2 | -34.30 | -5.15 | -35.76 | 1248 |
| 55 | Triple EMA stack · 1h | trend | 92.86 | -7.14 | 33 | 6.1 | -7.58 | -0.74 | -22.30 | 231 |
| 56 | MACD zero-line · 1h | trend | 92.55 | -7.45 | 23 | 4.3 | -7.34 | -0.85 | -16.22 | 231 |
| 57 | EMA 9/21 cross · 1h | trend | 92.20 | -7.80 | 46 | 10.9 | -4.83 | -0.46 | -16.92 | 321 |
| 58 | Keltner breakout · 1h | breakout | 92.01 | -7.99 | 14 | 0.0 | -7.54 | -0.86 | -19.74 | 218 |
| 59 | Donchian 20/10 · 1h | breakout | 91.84 | -8.16 | 21 | 9.5 | 2.00 | 0.47 | -13.45 | 222 |
| 60 | Heikin-Ashi · 1h | trend | 91.61 | -8.39 | 51 | 9.8 | -27.14 | -4.33 | -31.31 | 684 |
| 61 | RSI(14) reversion | reversion | 91.00 | -9.00 | 125 | 36.0 | -71.12 | -21.24 | -71.28 | 1477 |
| 62 | OBV trend · 1h | momentum | 90.46 | -9.54 | 64 | 6.2 | -13.41 | -1.54 | -25.03 | 329 |
| 63 | ROC + volume · 1h | momentum | 87.82 | -12.18 | 59 | 5.1 | -13.19 | -1.75 | -21.75 | 412 |
| 64 | Squeeze breakout | breakout | 87.71 | -12.29 | 104 | 13.5 | -59.66 | -18.49 | -59.83 | 1188 |
| 65 | Donchian 55/20 | breakout | 86.28 | -13.72 | 106 | 16.0 | -67.40 | -15.34 | -67.63 | 1295 |
| 66 | ROC + volume | momentum | 85.27 | -14.73 | 173 | 19.7 | -72.57 | -17.65 | -72.83 | 1651 |
| 67 | Volume breakout | breakout | 85.21 | -14.79 | 113 | 15.0 | -62.31 | -19.89 | -62.65 | 901 |
| 68 | Keltner breakout | breakout | 83.80 | -16.20 | 166 | 13.3 | -84.73 | -34.66 | -84.79 | 1903 |
| 69 | Ichimoku | trend | 83.67 | -16.33 | 129 | 8.5 | -80.28 | -25.76 | -80.43 | 1744 |
| 70 | Z-score reversion | reversion | 83.53 | -16.47 | 195 | 30.8 | -84.62 | -27.56 | -84.71 | 2107 |
| 71 | EMA 20/50 cross | trend | 83.48 | -16.52 | 141 | 14.9 | -78.74 | -17.44 | -78.75 | 1473 |
| 72 | VWAP reversion | reversion | 83.45 | -16.55 | 151 | 23.2 | -71.84 | -17.82 | -72.06 | 1408 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 80.21 | -19.79 | 196 | 17.9 | -87.44 | -24.60 | -87.60 | 1962 |
| 76 | MFI reversion | reversion | 79.87 | -20.13 | 195 | 20.0 | -88.11 | -35.32 | -88.19 | 2148 |
| 77 | Donchian 20/10 | breakout | 79.85 | -20.15 | 222 | 18.0 | -90.56 | -28.90 | -90.67 | 2675 |
| 78 | MACD zero-line | trend | 79.67 | -20.33 | 223 | 15.7 | -91.78 | -35.76 | -91.84 | 2357 |
| 79 | Trend pullback | trend | 78.95 | -21.05 | 184 | 19.0 | -90.51 | -32.85 | -90.59 | 2255 |
| 80 | Triple EMA stack | trend | 78.72 | -21.28 | 231 | 16.5 | -92.71 | -34.18 | -92.81 | 2587 |
| 81 | RSI momentum | momentum | 78.02 | -21.98 | 218 | 14.7 | -90.27 | -28.72 | -90.38 | 2381 |
| 82 | Bollinger breakout | breakout | 77.91 | -22.09 | 235 | 16.2 | -93.81 | -42.17 | -93.82 | 2864 |
| 83 | ADX DI cross | trend | 76.94 | -23.06 | 217 | 7.4 | -89.45 | -45.51 | -89.46 | 2118 |
| 84 | Consensus | meta | 74.84 | -25.16 | 201 | 7.0 | -94.62 | -30.30 | -94.64 | 2648 |
| 85 | Stochastic reversion | reversion | 74.43 | -25.57 | 358 | 24.0 | -95.95 | -45.16 | -95.96 | 4057 |
| 86 | EMA 9/21 cross | trend | 74.28 | -25.72 | 306 | 17.0 | -97.40 | -41.00 | -97.44 | 3535 |
| 87 | Connors RSI(2) | reversion | 74.02 | -25.98 | 272 | 16.9 | -96.40 | -40.42 | -96.41 | 3604 |
| 88 | Candlestick reversal | reversion | 73.03 | -26.96 | 317 | 13.2 | -99.36 | -48.70 | -99.36 | 5599 |
| 89 | Bollinger reversion | reversion | 72.90 | -27.10 | 335 | 15.5 | -95.81 | -43.55 | -95.83 | 3685 |
| 90 | OBV trend | momentum | 71.39 | -28.61 | 306 | 15.0 | -95.87 | -46.84 | -95.90 | 3529 |
| 91 | CCI reversion | reversion | 70.65 | -29.35 | 278 | 12.2 | -98.47 | -49.54 | -98.47 | 4692 |
| 92 | Parabolic SAR | trend | 70.33 | -29.67 | 299 | 13.0 | -96.94 | -53.88 | -96.96 | 3620 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.54 | -36.18 | -98.55 | 5266 |
| 94 | MACD cross | trend | 68.39 | -31.61 | 321 | 13.7 | -99.71 | -63.61 | -99.72 | 6086 |
| 95 | Williams %R | reversion | 67.82 | -32.18 | 396 | 21.2 | -99.53 | -57.58 | -99.53 | 6102 |
| 96 | Heikin-Ashi | trend | 66.84 | -33.16 | 310 | 5.8 | -99.89 | -76.92 | -99.89 | 8290 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T16:10 | MFI reversion | sell | XRP-USD | 19.99 | 0.04 | exit signal |
| 2026-09-30T16:10 | MFI reversion | sell | DOGE-USD | 20.02 | 0.05 | exit signal |
| 2026-09-30T16:10 | CCI reversion | buy | TNA | 5.28 | — | rebalance up |
| 2026-09-30T16:10 | CCI reversion | buy | SQQQ | 8.72 | — | rebalance up |
| 2026-09-30T16:10 | CCI reversion | buy | SOXL | 6.28 | — | rebalance up |
| 2026-09-30T16:10 | CCI reversion | buy | NVDA | 7.73 | — | rebalance up |
| 2026-09-30T16:10 | CCI reversion | buy | IWM | 5.31 | — | rebalance up |
| 2026-09-30T16:10 | CCI reversion | sell | TSLA | 7.86 | 0.05 | exit signal |
| 2026-09-30T16:10 | CCI reversion | sell | ETH-USD | 5.41 | -0.02 | exit signal |
| 2026-09-30T16:10 | CCI reversion | sell | AMD | 7.83 | -0.02 | exit signal |
| 2026-09-30T16:10 | Williams %R | buy | SQQQ | 3.41 | — | rebalance up |
| 2026-09-30T16:10 | Williams %R | buy | IWM | 5.66 | — | rebalance up |
| 2026-09-30T16:10 | Williams %R | buy | AAPL | 3.42 | — | rebalance up |
| 2026-09-30T16:10 | Williams %R | sell | AMD | 13.60 | 0.01 | exit signal |
| 2026-09-30T16:10 | Stochastic reversion | sell | AMD | 18.67 | 0.01 | exit signal |
| 2026-09-30T16:10 | Z-score reversion | sell | TSLA | 11.93 | 0.08 | exit signal |
| 2026-09-30T16:10 | RSI(14) reversion | buy | SQQQ | 9.91 | — | rebalance up |
| 2026-09-30T16:10 | RSI(14) reversion | buy | SOL-USD | 9.76 | — | rebalance up |
| 2026-09-30T16:10 | RSI(14) reversion | buy | ETH-USD | 9.78 | — | rebalance up |
| 2026-09-30T16:10 | RSI(14) reversion | sell | XRP-USD | 13.04 | 0.06 | exit signal |
| 2026-09-30T16:10 | RSI(14) reversion | sell | DOGE-USD | 12.96 | -0.03 | exit signal |
| 2026-09-30T16:10 | RSI(14) reversion | sell | COIN | 13.10 | 0.11 | exit signal |
| 2026-09-30T16:10 | RSI(14) reversion | sell | BTC-USD | 13.03 | 0.03 | exit signal |
| 2026-09-30T16:10 | Volume breakout | buy | DOGE-USD | 21.32 | — | entry signal |
| 2026-09-30T16:10 | Squeeze breakout | buy | MSTR | 21.93 | — | entry signal |
| 2026-09-30T16:10 | Donchian 20/10 | buy | MSTR | 4.99 | — | entry signal |
| 2026-09-30T16:10 | Donchian 20/10 | buy | DOGE-USD | 4.99 | — | entry signal |
| 2026-09-30T16:10 | Donchian 20/10 | buy | COIN | 4.99 | — | entry signal |
| 2026-09-30T16:10 | Donchian 20/10 | buy | BTC-USD | 4.99 | — | entry signal |
| 2026-09-30T16:10 | Donchian 20/10 | buy | BITX | 4.99 | — | entry signal |
| 2026-09-30T16:10 | Donchian 20/10 | sell | UPRO | 6.40 | 0.03 | rebalance down |
| 2026-09-30T16:10 | Donchian 20/10 | sell | TECL | 6.46 | 0.03 | rebalance down |
| 2026-09-30T16:10 | Donchian 20/10 | sell | SPY | 6.38 | 0.01 | rebalance down |
| 2026-09-30T16:10 | Donchian 20/10 | sell | MSFT | 6.41 | 0.03 | rebalance down |
| 2026-09-30T16:10 | Ichimoku | buy | TECL | 4.23 | — | rebalance up |
| 2026-09-30T16:10 | Ichimoku | buy | LABU | 8.07 | — | rebalance up |
| 2026-09-30T16:10 | Ichimoku | buy | AMZN | 4.20 | — | rebalance up |
| 2026-09-30T16:10 | Ichimoku | sell | AAPL | 16.56 | -0.04 | exit signal |
| 2026-09-30T16:10 | MACD zero-line | buy | TSLA | 19.80 | — | entry signal |
| 2026-09-30T16:10 | MACD zero-line | buy | BTC-USD | 19.93 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
