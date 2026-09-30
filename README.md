# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T16:40:05.000133+00:00 · 7081 ticks

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

Today: 24423 decisions in 2535 calls, $0.3091 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T16:40 | 3 / 13 / 14 | cash |  |
| Breezy | 2026-09-30T16:40 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-09-30T16:40 | 3 / 26 / 1 | cash |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.84 | 1.84 | 2 | 50.0 | 14.91 | 3.20 | -7.55 | 43 |
| 2 | Copy: Congress Democrats (NANC) | copy | 100.58 | 0.58 | 0 | — | 7.38 | 2.99 | -3.62 | 1 |
| 3 | Hold BTC | benchmark | 100.51 | 0.51 | 0 | — | 29.44 | 3.69 | -8.68 | 1 |
| 4 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.36 | 0.36 | 1 | 100.0 | 0.04 | 0.10 | -9.74 | 24 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.99 | -0.01 | 0 | — | 5.51 | 1.57 | -7.93 | 7 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 99.86 | -0.14 | 0 | — | -2.72 | -1.60 | -5.09 | 2 |
| 10 | Daily: Bullish score | daily | 99.73 | -0.27 | 3 | 0.0 | 0.37 | 0.25 | -12.76 | 14 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.72 | -0.28 | 7 | 42.9 | 2.84 | 1.44 | -2.15 | 83 |
| 12 | Hold SPY | benchmark | 99.68 | -0.32 | 0 | — | 3.73 | 2.07 | -3.66 | 1 |
| 13 | Timing: Nasdaq FTD · TQQQ | daily | 99.68 | -0.32 | 0 | — | -9.15 | -1.78 | -15.27 | 2 |
| 14 | Agent | meta | 99.65 | -0.35 | 25 | 68.0 | -9.82 | -6.50 | -10.68 | 215 |
| 15 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -13.09 | -4.33 | -15.20 | 123 |
| 16 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -0.41 | -0.21 | -3.92 | 97 |
| 17 | Copy: Insider buying | copy | 99.48 | -0.52 | 2 | 100.0 | -13.52 | -2.63 | -17.74 | 73 |
| 18 | RSI(14) reversion · 1h | reversion | 99.43 | -0.57 | 8 | 62.5 | 3.48 | 1.03 | -6.57 | 124 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 99.13 | -0.87 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 21 | Stochastic reversion · 1h | reversion | 99.12 | -0.88 | 30 | 56.7 | -10.80 | -2.37 | -12.66 | 326 |
| 22 | Copy: Warren Buffett (BRK-B) | copy | 99.07 | -0.93 | 0 | — | -1.46 | -0.55 | -7.65 | 1 |
| 23 | Gap and go | momentum | 98.85 | -1.15 | 11 | 9.1 | 15.80 | 3.90 | -4.73 | 184 |
| 24 | Williams %R · 1h | reversion | 98.81 | -1.19 | 51 | 51.0 | -17.40 | -3.26 | -19.42 | 492 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.75 | -1.25 | 0 | — | 24.26 | 3.56 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | CCI reversion · 1h | reversion | 98.59 | -1.41 | 42 | 40.5 | 2.16 | 0.53 | -12.41 | 413 |
| 28 | Candlestick reversal · 1h | reversion | 98.42 | -1.58 | 33 | 24.2 | -25.38 | -6.16 | -26.53 | 499 |
| 29 | Daily: SMA 20/50 cross · AAPL | daily | 98.39 | -1.61 | 0 | — | -6.14 | -1.36 | -10.06 | 1 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.19 | 0.21 | -15.21 | 46 |
| 31 | Agent (rotation) | meta | 98.26 | -1.74 | 34 | 11.8 | -5.03 | -1.73 | -9.79 | 208 |
| 32 | Z-score reversion · 1h | reversion | 98.25 | -1.75 | 11 | 45.5 | 4.72 | 1.13 | -8.60 | 156 |
| 33 | Connors RSI(2) · 1h | reversion | 97.75 | -2.25 | 47 | 46.8 | -11.25 | -3.57 | -11.76 | 233 |
| 34 | EMA 20/50 cross · 1h | trend | 97.49 | -2.51 | 17 | 5.9 | 16.47 | 2.05 | -12.18 | 128 |
| 35 | Bollinger reversion · 1h | reversion | 97.46 | -2.54 | 31 | 32.3 | -15.65 | -4.34 | -17.14 | 308 |
| 36 | Opening range 30m | breakout | 97.10 | -2.90 | 38 | 13.2 | -9.86 | -2.86 | -14.28 | 561 |
| 37 | Max aggression: 5-day momentum | meta | 96.83 | -3.17 | 3 | 66.7 | -12.20 | -0.83 | -29.56 | 29 |
| 38 | Supertrend · 1h | trend | 96.57 | -3.43 | 18 | 5.6 | 1.37 | 0.39 | -16.43 | 202 |
| 39 | Trend pullback · 1h | trend | 96.43 | -3.57 | 30 | 10.0 | -24.99 | -6.66 | -25.72 | 152 |
| 40 | Agent (ML meta-label) | meta | 96.30 | -3.70 | 156 | 12.8 | 10.36 | 1.81 | -10.76 | 396 |
| 41 | Opening range 15m | breakout | 96.03 | -3.97 | 49 | 12.2 | -11.35 | -3.09 | -16.70 | 689 |
| 42 | Donchian 55/20 · 1h | breakout | 95.61 | -4.39 | 15 | 0.0 | 4.90 | 0.84 | -16.96 | 113 |
| 43 | Max aggression: 1-day momentum | meta | 95.45 | -4.55 | 3 | 33.3 | -20.47 | -0.95 | -41.28 | 42 |
| 44 | MACD cross · 1h | trend | 95.34 | -4.66 | 41 | 9.8 | -13.06 | -2.04 | -17.40 | 474 |
| 45 | MFI reversion · 1h | reversion | 95.29 | -4.71 | 51 | 19.6 | -9.11 | -1.64 | -17.20 | 129 |
| 46 | Parabolic SAR · 1h | trend | 95.18 | -4.82 | 30 | 13.3 | -8.52 | -1.08 | -19.53 | 303 |
| 47 | Squeeze breakout · 1h | breakout | 95.14 | -4.86 | 15 | 6.7 | 12.37 | 2.19 | -7.19 | 100 |
| 48 | Three white soldiers | momentum | 94.58 | -5.42 | 49 | 20.4 | -50.19 | -27.63 | -50.39 | 608 |
| 49 | Volume breakout · 1h | breakout | 94.44 | -5.56 | 28 | 3.6 | 6.05 | 1.04 | -12.60 | 122 |
| 50 | ADX DI cross · 1h | trend | 94.33 | -5.67 | 32 | 6.2 | -15.50 | -2.86 | -17.86 | 258 |
| 51 | Ichimoku · 1h | trend | 93.68 | -6.32 | 20 | 15.0 | 5.56 | 0.85 | -15.13 | 123 |
| 52 | RSI momentum · 1h | momentum | 93.51 | -6.50 | 28 | 3.6 | -0.74 | 0.10 | -15.29 | 221 |
| 53 | Bollinger breakout · 1h | breakout | 93.46 | -6.54 | 24 | 8.3 | 6.52 | 1.05 | -9.63 | 280 |
| 54 | VWAP momentum · 1h | momentum | 93.41 | -6.59 | 115 | 13.9 | -34.09 | -5.11 | -35.50 | 1250 |
| 55 | Triple EMA stack · 1h | trend | 92.64 | -7.36 | 33 | 6.1 | -7.77 | -0.76 | -22.30 | 232 |
| 56 | MACD zero-line · 1h | trend | 92.51 | -7.49 | 23 | 4.3 | -7.56 | -0.88 | -16.22 | 232 |
| 57 | EMA 9/21 cross · 1h | trend | 92.14 | -7.86 | 46 | 10.9 | -7.38 | -0.82 | -16.92 | 320 |
| 58 | Keltner breakout · 1h | breakout | 91.96 | -8.04 | 14 | 0.0 | -7.44 | -0.84 | -19.73 | 218 |
| 59 | Donchian 20/10 · 1h | breakout | 91.67 | -8.33 | 21 | 9.5 | 0.41 | 0.27 | -13.45 | 222 |
| 60 | Heikin-Ashi · 1h | trend | 91.53 | -8.47 | 51 | 9.8 | -27.55 | -4.41 | -31.31 | 685 |
| 61 | RSI(14) reversion | reversion | 91.13 | -8.87 | 127 | 35.4 | -71.12 | -21.23 | -71.33 | 1492 |
| 62 | OBV trend · 1h | momentum | 90.36 | -9.64 | 64 | 6.2 | -13.38 | -1.54 | -25.03 | 328 |
| 63 | Squeeze breakout | breakout | 87.66 | -12.34 | 104 | 13.5 | -59.83 | -18.60 | -59.87 | 1186 |
| 64 | ROC + volume · 1h | momentum | 87.65 | -12.35 | 59 | 5.1 | -13.67 | -1.82 | -21.75 | 412 |
| 65 | Donchian 55/20 | breakout | 86.18 | -13.82 | 108 | 16.7 | -67.36 | -15.32 | -67.49 | 1294 |
| 66 | Volume breakout | breakout | 85.07 | -14.93 | 114 | 14.9 | -62.55 | -20.08 | -62.75 | 900 |
| 67 | ROC + volume | momentum | 84.92 | -15.08 | 175 | 20.0 | -72.73 | -17.71 | -72.87 | 1652 |
| 68 | Keltner breakout | breakout | 83.64 | -16.36 | 168 | 13.7 | -84.72 | -34.58 | -84.78 | 1902 |
| 69 | Ichimoku | trend | 83.53 | -16.47 | 131 | 9.2 | -80.32 | -25.77 | -80.40 | 1744 |
| 70 | Z-score reversion | reversion | 83.50 | -16.50 | 196 | 31.1 | -84.76 | -27.77 | -84.82 | 2105 |
| 71 | VWAP reversion | reversion | 83.43 | -16.57 | 151 | 23.2 | -71.87 | -17.83 | -72.04 | 1405 |
| 72 | EMA 20/50 cross | trend | 83.34 | -16.66 | 141 | 14.9 | -78.90 | -17.53 | -78.90 | 1474 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 80.21 | -19.79 | 196 | 17.9 | -87.45 | -24.62 | -87.59 | 1963 |
| 76 | MFI reversion | reversion | 79.86 | -20.14 | 196 | 19.9 | -88.13 | -35.35 | -88.22 | 2145 |
| 77 | Donchian 20/10 | breakout | 79.69 | -20.31 | 224 | 18.8 | -90.57 | -28.92 | -90.67 | 2675 |
| 78 | MACD zero-line | trend | 79.54 | -20.46 | 223 | 15.7 | -91.77 | -35.67 | -91.80 | 2353 |
| 79 | Trend pullback | trend | 78.89 | -21.11 | 184 | 19.0 | -90.53 | -32.99 | -90.59 | 2257 |
| 80 | Triple EMA stack | trend | 78.60 | -21.40 | 233 | 16.3 | -92.81 | -34.75 | -92.88 | 2584 |
| 81 | RSI momentum | momentum | 77.91 | -22.09 | 219 | 14.6 | -90.30 | -28.80 | -90.38 | 2381 |
| 82 | Bollinger breakout | breakout | 77.67 | -22.33 | 239 | 16.3 | -93.82 | -42.19 | -93.83 | 2863 |
| 83 | ADX DI cross | trend | 76.72 | -23.28 | 223 | 7.2 | -89.46 | -45.25 | -89.46 | 2116 |
| 84 | Consensus | meta | 74.61 | -25.39 | 205 | 6.8 | -94.55 | -30.34 | -94.56 | 2640 |
| 85 | Stochastic reversion | reversion | 74.55 | -25.45 | 360 | 24.2 | -95.94 | -45.06 | -95.96 | 4060 |
| 86 | EMA 9/21 cross | trend | 74.19 | -25.81 | 308 | 17.2 | -97.40 | -40.99 | -97.43 | 3535 |
| 87 | Connors RSI(2) | reversion | 73.94 | -26.06 | 275 | 17.5 | -96.41 | -40.45 | -96.41 | 3618 |
| 88 | Bollinger reversion | reversion | 72.97 | -27.03 | 336 | 15.8 | -95.81 | -43.52 | -95.83 | 3687 |
| 89 | Candlestick reversal | reversion | 72.96 | -27.04 | 319 | 13.8 | -99.36 | -49.26 | -99.36 | 5607 |
| 90 | OBV trend | momentum | 71.31 | -28.69 | 312 | 15.4 | -95.86 | -45.98 | -95.87 | 3525 |
| 91 | CCI reversion | reversion | 70.72 | -29.28 | 278 | 12.2 | -98.47 | -49.58 | -98.47 | 4693 |
| 92 | Parabolic SAR | trend | 70.22 | -29.78 | 306 | 12.7 | -96.95 | -54.03 | -96.96 | 3620 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.53 | -35.97 | -98.53 | 5252 |
| 94 | MACD cross | trend | 68.33 | -31.67 | 322 | 13.7 | -99.71 | -63.39 | -99.71 | 6068 |
| 95 | Williams %R | reversion | 67.94 | -32.06 | 397 | 21.4 | -99.53 | -57.13 | -99.53 | 6101 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -76.55 | -99.89 | 8286 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T16:40 | Williams %R | buy | TECL | 9.03 | — | entry signal |
| 2026-09-30T16:40 | Williams %R | buy | SOXL | 11.33 | — | entry signal |
| 2026-09-30T16:40 | Williams %R | buy | LABU | 4.53 | — | rebalance up |
| 2026-09-30T16:40 | Williams %R | sell | SQQQ | 13.60 | 0.03 | exit signal |
| 2026-09-30T16:40 | Williams %R | sell | IWM | 5.65 | 0.00 | rebalance down |
| 2026-09-30T16:40 | Williams %R | sell | AAPL | 5.63 | -0.01 | rebalance down |
| 2026-09-30T16:40 | Stochastic reversion | buy | UPRO | 7.59 | — | entry signal |
| 2026-09-30T16:40 | Stochastic reversion | buy | SPY | 14.91 | — | entry signal |
| 2026-09-30T16:40 | Stochastic reversion | buy | MSFT | 14.91 | — | entry signal |
| 2026-09-30T16:40 | Stochastic reversion | sell | SQQQ | 18.75 | 0.07 | exit signal |
| 2026-09-30T16:40 | Bollinger reversion | buy | TECL | 18.25 | — | entry signal |
| 2026-09-30T16:40 | Bollinger reversion | buy | SOXL | 18.25 | — | entry signal |
| 2026-09-30T16:40 | Connors RSI(2) | buy | AMZN | 7.40 | — | entry signal |
| 2026-09-30T16:40 | Connors RSI(2) | sell | SOXL | 8.24 | -0.01 | exit signal |
| 2026-09-30T16:40 | ADX DI cross | buy | TSLA | 5.66 | — | rebalance up |
| 2026-09-30T16:40 | ADX DI cross | buy | SQQQ | 5.89 | — | rebalance up |
| 2026-09-30T16:40 | ADX DI cross | buy | META | 5.74 | — | rebalance up |
| 2026-09-30T16:40 | ADX DI cross | buy | COIN | 5.72 | — | rebalance up |
| 2026-09-30T16:40 | ADX DI cross | buy | BTC-USD | 5.75 | — | rebalance up |
| 2026-09-30T16:40 | ADX DI cross | sell | XRP-USD | 9.56 | -0.04 | exit signal |
| 2026-09-30T16:40 | ADX DI cross | sell | SOL-USD | 9.57 | -0.05 | exit signal |
| 2026-09-30T16:40 | ADX DI cross | sell | IWM | 9.63 | 0.00 | exit signal |
| 2026-09-30T16:40 | MACD zero-line | buy | SOL-USD | 6.44 | — | entry signal |
| 2026-09-30T16:40 | MACD zero-line | buy | ETHU | 6.83 | — | rebalance up |
| 2026-09-30T16:40 | MACD zero-line | sell | TSLA | 4.44 | -0.00 | rebalance down |
| 2026-09-30T16:40 | MACD zero-line | sell | MSTR | 4.41 | -0.01 | rebalance down |
| 2026-09-30T16:40 | MACD zero-line | sell | BTC-USD | 4.42 | -0.02 | rebalance down |
| 2026-09-30T16:40 | Triple EMA stack | buy | MSTR | 7.77 | — | entry signal |
| 2026-09-30T16:40 | EMA 9/21 cross | sell | DOGE-USD | 7.35 | -0.08 | exit signal |
| 2026-09-30T16:36 | Heikin-Ashi | sell | SQQQ | 16.67 | 0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-30T16:36 | Heikin-Ashi | sell | LABU | 16.63 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-30T16:35 | Agent (rotation) | sell | TECL | 8.16 | -0.01 | selected signal exited |
| 2026-09-30T16:35 | Consensus | buy | LABU | 18.67 | — | entry |
| 2026-09-30T16:35 | Consensus | sell | META | 18.68 | -0.01 | target is flat |
| 2026-09-30T16:35 | Stochastic reversion | sell | IWM | 18.62 | -0.01 | target is flat |
| 2026-09-30T16:35 | Three white soldiers | sell | META | 23.77 | 0.16 | exit signal |
| 2026-09-30T16:35 | Keltner breakout | buy | LABU | 20.93 | — | entry |
| 2026-09-30T16:35 | Donchian 55/20 | sell | TECL | 7.21 | -0.01 | exit signal |
| 2026-09-30T16:35 | Gap and go | sell | TECL | 24.59 | -0.03 | stop-loss |
| 2026-09-30T16:35 | RSI momentum | buy | MSFT | 1.05 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
