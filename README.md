# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T15:41:05.000132+00:00 · 7031 ticks

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

Today: 19962 decisions in 2385 calls, $0.2570 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T15:41 | 3 / 16 / 11 | cash |  |
| Breezy | 2026-09-30T15:41 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-09-30T15:41 | 5 / 22 / 3 | BITX 73% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.98 | 1.98 | 2 | 50.0 | 15.23 | 3.26 | -7.55 | 43 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.49 | 0.49 | 1 | 100.0 | 0.32 | 0.19 | -9.74 | 24 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 4 | Hold BTC | benchmark | 100.28 | 0.28 | 0 | — | 29.69 | 3.72 | -8.68 | 1 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.23 | 0.23 | 0 | — | 7.23 | 2.94 | -3.62 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.86 | -0.14 | 0 | — | 6.38 | 1.77 | -7.93 | 7 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 99.81 | -0.19 | 0 | — | -8.89 | -1.72 | -15.27 | 2 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 99.80 | -0.20 | 0 | — | -2.63 | -1.54 | -5.09 | 2 |
| 11 | Copy: Insider buying | copy | 99.80 | -0.20 | 2 | 100.0 | -13.09 | -2.52 | -17.74 | 73 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.78 | -0.22 | 7 | 42.9 | 3.39 | 1.73 | -1.76 | 83 |
| 13 | Daily: Bullish score | daily | 99.75 | -0.25 | 3 | 0.0 | 0.55 | 0.28 | -12.76 | 14 |
| 14 | Agent | meta | 99.65 | -0.35 | 25 | 68.0 | -10.04 | -6.67 | -10.71 | 216 |
| 15 | Hold SPY | benchmark | 99.63 | -0.37 | 0 | — | 4.10 | 2.25 | -3.66 | 1 |
| 16 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -12.78 | -4.28 | -14.90 | 123 |
| 17 | RSI(14) reversion · 1h | reversion | 99.50 | -0.51 | 8 | 62.5 | 4.07 | 1.19 | -6.57 | 125 |
| 18 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -2.05 | -1.11 | -4.99 | 98 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 20 | Gap and go | momentum | 99.01 | -0.99 | 10 | 10.0 | 16.07 | 3.95 | -4.73 | 184 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 98.98 | -1.02 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 22 | Stochastic reversion · 1h | reversion | 98.92 | -1.08 | 29 | 55.2 | -11.82 | -2.60 | -13.59 | 326 |
| 23 | Copy: Warren Buffett (BRK-B) | copy | 98.84 | -1.16 | 0 | — | -1.22 | -0.45 | -7.65 | 1 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 2 | 0.0 | -0.44 | -0.11 | -4.88 | 18 |
| 25 | Williams %R · 1h | reversion | 98.65 | -1.34 | 50 | 50.0 | -17.35 | -3.25 | -19.41 | 488 |
| 26 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | -5.66 | -1.23 | -10.06 | 1 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.60 | -1.40 | 0 | — | 24.29 | 3.56 | -6.29 | 1 |
| 28 | CCI reversion · 1h | reversion | 98.58 | -1.42 | 40 | 37.5 | 2.32 | 0.55 | -12.41 | 411 |
| 29 | Agent (rotation) | meta | 98.37 | -1.63 | 33 | 12.1 | -4.82 | -1.65 | -9.79 | 208 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.05 | 0.19 | -15.21 | 46 |
| 31 | Candlestick reversal · 1h | reversion | 98.29 | -1.71 | 33 | 24.2 | -25.77 | -6.21 | -26.91 | 501 |
| 32 | Z-score reversion · 1h | reversion | 98.29 | -1.71 | 11 | 45.5 | 4.87 | 1.17 | -8.60 | 154 |
| 33 | Connors RSI(2) · 1h | reversion | 97.87 | -2.13 | 47 | 46.8 | -11.07 | -3.51 | -11.76 | 233 |
| 34 | EMA 20/50 cross · 1h | trend | 97.48 | -2.52 | 17 | 5.9 | 16.65 | 2.07 | -12.18 | 128 |
| 35 | Bollinger reversion · 1h | reversion | 97.31 | -2.69 | 31 | 32.3 | -15.68 | -4.35 | -17.14 | 308 |
| 36 | Opening range 30m | breakout | 97.16 | -2.84 | 38 | 13.2 | -9.71 | -2.81 | -14.28 | 561 |
| 37 | Trend pullback · 1h | trend | 96.62 | -3.38 | 30 | 10.0 | -24.77 | -6.53 | -25.81 | 149 |
| 38 | Supertrend · 1h | trend | 96.54 | -3.46 | 18 | 5.6 | 1.47 | 0.40 | -16.43 | 203 |
| 39 | Max aggression: 5-day momentum | meta | 96.54 | -3.46 | 3 | 66.7 | -12.34 | -0.84 | -29.56 | 29 |
| 40 | Agent (ML meta-label) | meta | 96.16 | -3.84 | 156 | 12.8 | 4.84 | 0.99 | -10.41 | 390 |
| 41 | Opening range 15m | breakout | 96.09 | -3.91 | 49 | 12.2 | -11.21 | -3.04 | -16.70 | 689 |
| 42 | Donchian 55/20 · 1h | breakout | 95.84 | -4.16 | 15 | 0.0 | 5.31 | 0.89 | -16.96 | 113 |
| 43 | MACD cross · 1h | trend | 95.25 | -4.75 | 41 | 9.8 | -13.17 | -2.06 | -17.55 | 473 |
| 44 | Max aggression: 1-day momentum | meta | 95.16 | -4.84 | 3 | 33.3 | -20.59 | -0.96 | -41.28 | 42 |
| 45 | Parabolic SAR · 1h | trend | 95.15 | -4.85 | 29 | 13.8 | -8.41 | -1.06 | -19.53 | 303 |
| 46 | Squeeze breakout · 1h | breakout | 95.10 | -4.90 | 15 | 6.7 | 12.33 | 2.18 | -7.19 | 102 |
| 47 | MFI reversion · 1h | reversion | 94.99 | -5.01 | 50 | 18.0 | -9.22 | -1.66 | -17.20 | 130 |
| 48 | Three white soldiers | momentum | 94.45 | -5.55 | 48 | 18.8 | -50.27 | -27.78 | -50.39 | 609 |
| 49 | Volume breakout · 1h | breakout | 94.40 | -5.60 | 28 | 3.6 | 5.68 | 0.99 | -12.60 | 123 |
| 50 | ADX DI cross · 1h | trend | 94.39 | -5.61 | 32 | 6.2 | -15.46 | -2.85 | -17.86 | 259 |
| 51 | Ichimoku · 1h | trend | 93.83 | -6.17 | 20 | 15.0 | 5.84 | 0.88 | -15.13 | 122 |
| 52 | RSI momentum · 1h | momentum | 93.59 | -6.41 | 28 | 3.6 | -1.27 | 0.03 | -15.29 | 220 |
| 53 | VWAP momentum · 1h | momentum | 93.43 | -6.57 | 114 | 13.2 | -34.08 | -5.12 | -35.53 | 1248 |
| 54 | Bollinger breakout · 1h | breakout | 93.31 | -6.69 | 24 | 8.3 | 6.57 | 1.05 | -9.63 | 280 |
| 55 | Triple EMA stack · 1h | trend | 92.72 | -7.28 | 33 | 6.1 | -7.56 | -0.73 | -22.30 | 231 |
| 56 | MACD zero-line · 1h | trend | 92.30 | -7.70 | 23 | 4.3 | -7.59 | -0.88 | -16.22 | 231 |
| 57 | EMA 9/21 cross · 1h | trend | 91.99 | -8.01 | 46 | 10.9 | -5.01 | -0.49 | -16.92 | 321 |
| 58 | Keltner breakout · 1h | breakout | 91.86 | -8.14 | 14 | 0.0 | -6.98 | -0.77 | -19.71 | 215 |
| 59 | Heikin-Ashi · 1h | trend | 91.59 | -8.41 | 51 | 9.8 | -27.19 | -4.34 | -31.31 | 684 |
| 60 | Donchian 20/10 · 1h | breakout | 91.54 | -8.46 | 21 | 9.5 | 2.00 | 0.47 | -13.45 | 221 |
| 61 | RSI(14) reversion | reversion | 90.93 | -9.07 | 120 | 34.2 | -71.25 | -21.38 | -71.39 | 1476 |
| 62 | OBV trend · 1h | momentum | 90.47 | -9.53 | 64 | 6.2 | -13.52 | -1.56 | -25.03 | 328 |
| 63 | Squeeze breakout | breakout | 87.72 | -12.28 | 104 | 13.5 | -59.86 | -18.64 | -59.87 | 1186 |
| 64 | ROC + volume · 1h | momentum | 87.68 | -12.32 | 59 | 5.1 | -13.33 | -1.77 | -21.75 | 411 |
| 65 | Donchian 55/20 | breakout | 86.26 | -13.74 | 106 | 16.0 | -67.49 | -15.38 | -67.71 | 1296 |
| 66 | Volume breakout | breakout | 85.28 | -14.72 | 113 | 15.0 | -62.39 | -19.93 | -62.73 | 900 |
| 67 | ROC + volume | momentum | 85.13 | -14.87 | 172 | 19.8 | -72.66 | -17.70 | -72.84 | 1651 |
| 68 | Keltner breakout | breakout | 83.79 | -16.21 | 163 | 13.5 | -84.73 | -34.65 | -84.78 | 1903 |
| 69 | Ichimoku | trend | 83.57 | -16.43 | 127 | 8.7 | -80.36 | -25.88 | -80.47 | 1745 |
| 70 | EMA 20/50 cross | trend | 83.55 | -16.45 | 141 | 14.9 | -78.73 | -17.44 | -78.76 | 1471 |
| 71 | Z-score reversion | reversion | 83.31 | -16.68 | 194 | 30.4 | -84.66 | -27.62 | -84.71 | 2107 |
| 72 | VWAP reversion | reversion | 83.30 | -16.70 | 151 | 23.2 | -71.89 | -17.85 | -72.05 | 1404 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 80.02 | -19.98 | 196 | 17.9 | -87.47 | -24.65 | -87.60 | 1961 |
| 76 | Donchian 20/10 | breakout | 79.89 | -20.11 | 221 | 18.1 | -90.59 | -29.00 | -90.67 | 2672 |
| 77 | MFI reversion | reversion | 79.88 | -20.12 | 191 | 19.4 | -88.14 | -35.43 | -88.21 | 2139 |
| 78 | MACD zero-line | trend | 79.53 | -20.47 | 223 | 15.7 | -91.79 | -35.76 | -91.83 | 2354 |
| 79 | Trend pullback | trend | 78.95 | -21.05 | 184 | 19.0 | -90.57 | -33.04 | -90.65 | 2262 |
| 80 | Triple EMA stack | trend | 78.60 | -21.40 | 231 | 16.5 | -92.92 | -35.35 | -93.00 | 2597 |
| 81 | RSI momentum | momentum | 78.01 | -21.99 | 216 | 13.9 | -90.39 | -28.99 | -90.49 | 2382 |
| 82 | Bollinger breakout | breakout | 77.96 | -22.04 | 233 | 15.9 | -93.82 | -42.24 | -93.83 | 2861 |
| 83 | ADX DI cross | trend | 77.02 | -22.98 | 214 | 7.5 | -89.44 | -45.47 | -89.47 | 2102 |
| 84 | Consensus | meta | 74.76 | -25.24 | 201 | 7.0 | -94.60 | -30.36 | -94.61 | 2647 |
| 85 | Stochastic reversion | reversion | 74.42 | -25.58 | 355 | 23.7 | -95.95 | -45.18 | -95.96 | 4056 |
| 86 | EMA 9/21 cross | trend | 74.20 | -25.80 | 306 | 17.0 | -97.41 | -41.19 | -97.45 | 3532 |
| 87 | Connors RSI(2) | reversion | 74.01 | -25.99 | 269 | 17.1 | -96.40 | -40.42 | -96.40 | 3607 |
| 88 | Candlestick reversal | reversion | 73.05 | -26.95 | 311 | 12.5 | -99.36 | -49.08 | -99.36 | 5598 |
| 89 | Bollinger reversion | reversion | 72.95 | -27.05 | 333 | 15.6 | -95.81 | -43.52 | -95.83 | 3686 |
| 90 | OBV trend | momentum | 71.31 | -28.69 | 305 | 14.8 | -95.91 | -47.61 | -95.94 | 3521 |
| 91 | CCI reversion | reversion | 70.66 | -29.34 | 269 | 10.8 | -98.47 | -49.70 | -98.48 | 4693 |
| 92 | Parabolic SAR | trend | 70.32 | -29.68 | 298 | 12.8 | -96.95 | -54.25 | -96.98 | 3616 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.52 | -35.87 | -98.53 | 5260 |
| 94 | MACD cross | trend | 68.17 | -31.83 | 319 | 13.5 | -99.72 | -64.07 | -99.72 | 6093 |
| 95 | Williams %R | reversion | 67.80 | -32.20 | 393 | 21.1 | -99.53 | -57.04 | -99.53 | 6108 |
| 96 | Heikin-Ashi | trend | 66.83 | -33.17 | 302 | 5.6 | -99.89 | -77.19 | -99.89 | 8303 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T15:40 | MFI reversion | sell | COIN | 13.33 | 0.02 | exit signal |
| 2026-09-30T15:40 | Williams %R | buy | TSLA | 7.89 | — | rebalance up |
| 2026-09-30T15:40 | Williams %R | buy | SQQQ | 7.93 | — | rebalance up |
| 2026-09-30T15:40 | Williams %R | buy | NVDA | 6.79 | — | rebalance up |
| 2026-09-30T15:40 | Williams %R | buy | AMD | 7.94 | — | rebalance up |
| 2026-09-30T15:40 | Williams %R | buy | AAPL | 6.78 | — | rebalance up |
| 2026-09-30T15:40 | Williams %R | sell | SOXL | 5.64 | 0.01 | exit signal |
| 2026-09-30T15:40 | Williams %R | sell | SOL-USD | 6.75 | -0.03 | exit signal |
| 2026-09-30T15:40 | Williams %R | sell | ETHU | 5.67 | 0.02 | exit signal |
| 2026-09-30T15:40 | Williams %R | sell | ETH-USD | 5.63 | -0.02 | exit signal |
| 2026-09-30T15:40 | Williams %R | sell | DOGE-USD | 4.84 | -0.01 | exit signal |
| 2026-09-30T15:40 | Stochastic reversion | buy | TSLA | 9.15 | — | rebalance up |
| 2026-09-30T15:40 | Stochastic reversion | buy | SQQQ | 9.22 | — | rebalance up |
| 2026-09-30T15:40 | Stochastic reversion | buy | NVDA | 7.45 | — | rebalance up |
| 2026-09-30T15:40 | Stochastic reversion | buy | AMD | 9.18 | — | rebalance up |
| 2026-09-30T15:40 | Stochastic reversion | buy | AAPL | 7.45 | — | rebalance up |
| 2026-09-30T15:40 | Stochastic reversion | sell | SOXL | 5.77 | -0.01 | exit signal |
| 2026-09-30T15:40 | Stochastic reversion | sell | SOL-USD | 5.65 | -0.03 | exit signal |
| 2026-09-30T15:40 | Stochastic reversion | sell | ETHU | 5.76 | 0.04 | exit signal |
| 2026-09-30T15:40 | Stochastic reversion | sell | ETH-USD | 5.71 | -0.01 | exit signal |
| 2026-09-30T15:40 | Stochastic reversion | sell | DOGE-USD | 5.74 | -0.02 | exit signal |
| 2026-09-30T15:40 | Bollinger reversion | sell | ETHU | 18.30 | 0.08 | exit signal |
| 2026-09-30T15:40 | Bollinger reversion | sell | ETH-USD | 18.20 | -0.08 | exit signal |
| 2026-09-30T15:40 | Connors RSI(2) | buy | AMZN | 18.51 | — | entry signal |
| 2026-09-30T15:40 | ROC + volume | buy | BITX | 21.29 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | buy | XRP-USD | 5.55 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | buy | TECL | 5.58 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | buy | SOL-USD | 5.58 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | buy | MSTR | 5.58 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | buy | ETHU | 5.58 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | buy | ETH-USD | 5.58 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | buy | DOGE-USD | 5.58 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | buy | BTC-USD | 5.58 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | buy | BITX | 5.58 | — | entry signal |
| 2026-09-30T15:40 | Heikin-Ashi | sell | PLTR | 13.39 | -0.02 | exit signal |
| 2026-09-30T15:40 | Heikin-Ashi | sell | MSFT | 7.81 | -0.00 | rebalance down |
| 2026-09-30T15:40 | Heikin-Ashi | sell | META | 7.84 | 0.01 | rebalance down |
| 2026-09-30T15:40 | Heikin-Ashi | sell | LABU | 13.32 | 0.05 | exit signal |
| 2026-09-30T15:40 | Heikin-Ashi | sell | GOOGL | 7.83 | 0.01 | rebalance down |
| 2026-09-30T15:40 | Parabolic SAR | buy | TECL | 10.50 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
