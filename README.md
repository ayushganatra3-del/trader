# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T20:40:05.000170+00:00 · 7267 ticks

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
| Copy: Insider buying | 2026-09-30 | ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, ADRX 12%, BBD 12%, ENHA 12%, CX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-30)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.26 · VIX 16.42 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, META 7.4, MSFT 7.2, AMD 7.2, ETHU 7.0, BITX 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 38253 decisions in 3093 calls, $0.4723 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T20:40 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-09-30T20:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T20:40 | 2 / 3 / 0 | ETH-USD 57% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.70 | 0.70 | 3 | 33.3 | 13.60 | 2.94 | -7.55 | 43 |
| 2 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 3 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 4 | Copy: Congress Democrats (NANC) | copy | 99.89 | -0.11 | 0 | — | 5.20 | 2.20 | -3.62 | 1 |
| 5 | Hold BTC | benchmark | 99.88 | -0.12 | 0 | — | 28.94 | 3.64 | -8.68 | 1 |
| 6 | Agent | meta | 99.63 | -0.37 | 27 | 66.7 | -10.23 | -6.84 | -10.80 | 224 |
| 7 | Copy: Hedge-fund gurus (GURU) | copy | 99.58 | -0.42 | 0 | — | -2.19 | -1.03 | -5.14 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.65 | 1.35 | -2.11 | 83 |
| 9 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -1.50 | -0.81 | -4.46 | 99 |
| 10 | VWAP reversion · 1h | reversion | 99.43 | -0.57 | 22 | 27.3 | -12.58 | -4.24 | -14.72 | 124 |
| 11 | RSI(14) reversion · 1h | reversion | 99.42 | -0.58 | 8 | 62.5 | 2.03 | 0.63 | -7.26 | 137 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 99.41 | -0.59 | 0 | — | -3.22 | -1.95 | -5.09 | 2 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 14 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 2 | 50.0 | -1.10 | -0.29 | -9.74 | 24 |
| 15 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 16 | Hold SPY | benchmark | 99.02 | -0.98 | 0 | — | 2.91 | 1.63 | -3.66 | 1 |
| 17 | Stochastic reversion · 1h | reversion | 98.70 | -1.30 | 30 | 56.7 | -10.25 | -2.28 | -11.63 | 324 |
| 18 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 14.96 | 3.71 | -4.73 | 182 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 20 | Copy: Warren Buffett (BRK-B) | copy | 98.66 | -1.34 | 0 | — | -2.22 | -0.87 | -7.65 | 1 |
| 21 | Daily: Bullish score | daily | 98.52 | -1.49 | 3 | 0.0 | -1.05 | 0.05 | -12.76 | 14 |
| 22 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.54 | 0.27 | -15.21 | 46 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 98.29 | -1.71 | 0 | — | -10.46 | -2.12 | -15.27 | 2 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.29 | -1.71 | 0 | — | 2.47 | 0.77 | -7.93 | 7 |
| 25 | Williams %R · 1h | reversion | 98.22 | -1.78 | 51 | 51.0 | -17.52 | -3.30 | -19.41 | 491 |
| 26 | Copy: Insider buying | copy | 98.20 | -1.80 | 2 | 100.0 | -14.74 | -2.91 | -17.74 | 73 |
| 27 | CCI reversion · 1h | reversion | 98.17 | -1.83 | 42 | 40.5 | 1.52 | 0.42 | -12.41 | 414 |
| 28 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.58 | -3.34 | -11.47 | 232 |
| 29 | Candlestick reversal · 1h | reversion | 97.89 | -2.11 | 33 | 24.2 | -26.61 | -6.69 | -27.33 | 496 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 97.78 | -2.22 | 0 | — | 26.25 | 3.85 | -6.29 | 1 |
| 31 | Agent (rotation) | meta | 97.76 | -2.24 | 37 | 13.5 | -5.52 | -1.91 | -9.79 | 208 |
| 32 | Z-score reversion · 1h | reversion | 97.64 | -2.35 | 11 | 45.5 | 3.25 | 0.82 | -8.60 | 153 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.40 | -2.60 | 0 | — | -7.64 | -1.79 | -10.03 | 1 |
| 34 | Bollinger reversion · 1h | reversion | 96.98 | -3.02 | 32 | 34.4 | -16.89 | -4.73 | -17.77 | 306 |
| 35 | EMA 20/50 cross · 1h | trend | 96.31 | -3.69 | 19 | 5.3 | 15.01 | 1.90 | -12.18 | 130 |
| 36 | Opening range 30m | breakout | 96.12 | -3.88 | 49 | 12.2 | -11.24 | -3.27 | -15.06 | 559 |
| 37 | Supertrend · 1h | trend | 95.91 | -4.09 | 19 | 5.3 | 0.74 | 0.30 | -16.43 | 203 |
| 38 | Agent (ML meta-label) | meta | 95.50 | -4.50 | 170 | 12.9 | 4.70 | 0.92 | -12.45 | 429 |
| 39 | Trend pullback · 1h | trend | 95.44 | -4.56 | 33 | 12.1 | -26.13 | -6.99 | -26.13 | 156 |
| 40 | Max aggression: 5-day momentum | meta | 95.39 | -4.61 | 3 | 66.7 | -13.55 | -0.96 | -29.56 | 29 |
| 41 | Donchian 55/20 · 1h | breakout | 95.38 | -4.62 | 15 | 0.0 | 4.59 | 0.80 | -16.96 | 113 |
| 42 | Opening range 15m | breakout | 94.87 | -5.13 | 61 | 14.8 | -12.31 | -3.38 | -17.03 | 686 |
| 43 | MFI reversion · 1h | reversion | 94.62 | -5.38 | 51 | 19.6 | -9.16 | -1.65 | -17.05 | 131 |
| 44 | Squeeze breakout · 1h | breakout | 94.49 | -5.51 | 16 | 6.2 | 11.75 | 2.08 | -7.61 | 99 |
| 45 | Three white soldiers | momentum | 94.48 | -5.52 | 51 | 19.6 | -50.21 | -27.72 | -50.28 | 605 |
| 46 | Parabolic SAR · 1h | trend | 94.33 | -5.67 | 32 | 12.5 | -9.70 | -1.26 | -19.53 | 303 |
| 47 | MACD cross · 1h | trend | 94.12 | -5.88 | 46 | 8.7 | -14.32 | -2.27 | -17.47 | 477 |
| 48 | Max aggression: 1-day momentum | meta | 94.03 | -5.97 | 3 | 33.3 | -21.69 | -1.04 | -41.28 | 42 |
| 49 | Volume breakout · 1h | breakout | 93.79 | -6.21 | 29 | 3.4 | 5.32 | 0.94 | -12.60 | 122 |
| 50 | ADX DI cross · 1h | trend | 93.73 | -6.27 | 35 | 5.7 | -16.00 | -3.02 | -17.41 | 260 |
| 51 | Ichimoku · 1h | trend | 92.92 | -7.08 | 21 | 14.3 | 4.66 | 0.75 | -15.26 | 122 |
| 52 | RSI momentum · 1h | momentum | 92.48 | -7.52 | 30 | 3.3 | -3.59 | -0.29 | -16.07 | 221 |
| 53 | VWAP momentum · 1h | momentum | 92.24 | -7.76 | 127 | 15.7 | -39.20 | -6.30 | -39.27 | 1247 |
| 54 | Bollinger breakout · 1h | breakout | 92.09 | -7.91 | 25 | 8.0 | 5.06 | 0.86 | -10.56 | 280 |
| 55 | Triple EMA stack · 1h | trend | 91.25 | -8.75 | 40 | 5.0 | -8.76 | -0.88 | -22.27 | 233 |
| 56 | EMA 9/21 cross · 1h | trend | 91.16 | -8.84 | 50 | 10.0 | -8.58 | -0.99 | -17.41 | 320 |
| 57 | MACD zero-line · 1h | trend | 90.91 | -9.09 | 28 | 3.6 | -9.28 | -1.11 | -17.32 | 232 |
| 58 | RSI(14) reversion | reversion | 90.88 | -9.12 | 131 | 35.1 | -71.33 | -21.42 | -71.46 | 1473 |
| 59 | Keltner breakout · 1h | breakout | 90.83 | -9.17 | 15 | 0.0 | -8.80 | -1.03 | -20.71 | 218 |
| 60 | Heikin-Ashi · 1h | trend | 90.63 | -9.37 | 59 | 8.5 | -29.01 | -4.77 | -31.82 | 684 |
| 61 | Donchian 20/10 · 1h | breakout | 89.94 | -10.06 | 23 | 8.7 | -1.39 | 0.04 | -14.99 | 218 |
| 62 | OBV trend · 1h | momentum | 88.91 | -11.09 | 70 | 5.7 | -14.50 | -1.67 | -25.03 | 322 |
| 63 | Squeeze breakout | breakout | 87.41 | -12.59 | 110 | 13.6 | -59.32 | -18.24 | -59.40 | 1178 |
| 64 | ROC + volume · 1h | momentum | 86.45 | -13.55 | 60 | 5.0 | -15.08 | -2.02 | -22.40 | 413 |
| 65 | Donchian 55/20 | breakout | 86.05 | -13.95 | 120 | 20.0 | -67.23 | -15.22 | -67.31 | 1291 |
| 66 | Volume breakout | breakout | 85.14 | -14.86 | 115 | 15.7 | -62.64 | -20.19 | -62.73 | 894 |
| 67 | ROC + volume | momentum | 84.44 | -15.56 | 183 | 20.2 | -72.18 | -17.58 | -72.21 | 1625 |
| 68 | Keltner breakout | breakout | 83.44 | -16.56 | 174 | 14.9 | -84.65 | -34.54 | -84.66 | 1887 |
| 69 | VWAP reversion | reversion | 83.11 | -16.89 | 161 | 24.8 | -72.14 | -17.94 | -72.19 | 1404 |
| 70 | Ichimoku | trend | 83.10 | -16.90 | 138 | 10.1 | -80.29 | -25.51 | -80.29 | 1741 |
| 71 | EMA 20/50 cross | trend | 83.06 | -16.93 | 150 | 16.0 | -79.19 | -17.54 | -79.20 | 1469 |
| 72 | Z-score reversion | reversion | 83.04 | -16.96 | 207 | 31.4 | -85.03 | -28.07 | -85.07 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 79.89 | -20.11 | 204 | 19.1 | -87.56 | -24.42 | -87.61 | 1944 |
| 76 | Donchian 20/10 | breakout | 78.80 | -21.20 | 248 | 19.4 | -90.70 | -29.32 | -90.71 | 2667 |
| 77 | MFI reversion | reversion | 78.77 | -21.23 | 205 | 19.5 | -88.24 | -35.55 | -88.24 | 2129 |
| 78 | MACD zero-line | trend | 78.69 | -21.30 | 246 | 16.3 | -91.64 | -34.82 | -91.65 | 2350 |
| 79 | Trend pullback | trend | 77.79 | -22.21 | 213 | 16.9 | -90.88 | -33.24 | -90.88 | 2272 |
| 80 | RSI momentum | momentum | 77.30 | -22.70 | 239 | 15.5 | -90.27 | -28.53 | -90.27 | 2371 |
| 81 | Triple EMA stack | trend | 77.13 | -22.87 | 257 | 16.3 | -92.88 | -34.89 | -92.88 | 2589 |
| 82 | Bollinger breakout | breakout | 77.06 | -22.94 | 251 | 16.3 | -93.86 | -42.23 | -93.86 | 2847 |
| 83 | ADX DI cross | trend | 75.94 | -24.06 | 237 | 8.0 | -89.43 | -44.23 | -89.43 | 2107 |
| 84 | Stochastic reversion | reversion | 73.49 | -26.51 | 390 | 24.4 | -95.90 | -45.55 | -95.91 | 4047 |
| 85 | EMA 9/21 cross | trend | 73.01 | -26.99 | 337 | 16.9 | -97.34 | -40.35 | -97.34 | 3527 |
| 86 | Consensus | meta | 72.98 | -27.02 | 230 | 7.4 | -94.70 | -30.52 | -94.71 | 2667 |
| 87 | Connors RSI(2) ⏸ | reversion | 72.37 | -27.63 | 319 | 19.7 | -96.49 | -40.72 | -96.49 | 3639 |
| 88 | Bollinger reversion | reversion | 71.72 | -28.28 | 367 | 17.2 | -95.87 | -44.15 | -95.88 | 3690 |
| 89 | Candlestick reversal ⏸ | reversion | 71.29 | -28.71 | 376 | 14.4 | -99.37 | -48.65 | -99.37 | 5611 |
| 90 | OBV trend ⏸ | momentum | 70.20 | -29.80 | 361 | 16.1 | -95.94 | -45.95 | -95.94 | 3539 |
| 91 | CCI reversion | reversion | 69.90 | -30.10 | 318 | 13.2 | -98.50 | -49.16 | -98.50 | 4694 |
| 92 | Parabolic SAR | trend | 69.41 | -30.59 | 329 | 13.4 | -96.91 | -51.98 | -96.92 | 3609 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.55 | -35.84 | -98.55 | 5224 |
| 94 | MACD cross ⏸ | trend | 67.57 | -32.43 | 368 | 14.1 | -99.72 | -62.62 | -99.72 | 6071 |
| 95 | Williams %R ⏸ | reversion | 67.21 | -32.79 | 441 | 22.0 | -99.53 | -57.24 | -99.53 | 6116 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -75.92 | -99.89 | 8285 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T20:40 | Stochastic reversion | sell | SOL-USD | 18.41 | 0.03 | exit signal |
| 2026-09-30T20:40 | Z-score reversion | sell | ETH-USD | 20.73 | -0.09 | exit signal |
| 2026-09-30T20:40 | Bollinger reversion | sell | BTC-USD | 17.88 | -0.08 | exit signal |
| 2026-09-30T20:35 | EMA 9/21 cross | buy | ETH-USD | 18.26 | — | entry signal |
| 2026-09-30T20:30 | CCI reversion | sell | ETH-USD | 17.48 | -0.04 | exit signal |
| 2026-09-30T20:30 | MACD zero-line | buy | DOGE-USD | 19.69 | — | entry signal |
| 2026-09-30T20:25 | Stochastic reversion | sell | ETH-USD | 18.34 | -0.04 | exit signal |
| 2026-09-30T20:25 | Z-score reversion | buy | ETH-USD | 4.17 | — | rebalance up |
| 2026-09-30T20:25 | Z-score reversion | buy | BTC-USD | 4.23 | — | rebalance up |
| 2026-09-30T20:25 | Z-score reversion | sell | DOGE-USD | 16.64 | 0.03 | exit signal |
| 2026-09-30T20:25 | Bollinger reversion | sell | XRP-USD | 17.92 | -0.03 | exit signal |
| 2026-09-30T20:25 | Bollinger reversion | sell | SOL-USD | 17.96 | -0.10 | exit signal |
| 2026-09-30T20:25 | Bollinger breakout | buy | DOGE-USD | 19.28 | — | entry signal |
| 2026-09-30T20:25 | Supertrend | buy | DOGE-USD | 19.99 | — | entry signal |
| 2026-09-30T20:20 | Bollinger reversion | sell | ETH-USD | 17.89 | -0.06 | exit signal |
| 2026-09-30T20:20 | RSI(14) reversion | sell | DOGE-USD | 22.72 | -0.03 | exit signal |
| 2026-09-30T20:20 | Donchian 20/10 | buy | DOGE-USD | 19.71 | — | entry signal |
| 2026-09-30T20:20 | EMA 9/21 cross | buy | DOGE-USD | 18.27 | — | entry signal |
| 2026-09-30T20:15 | CCI reversion | buy | BTC-USD | 17.47 | — | entry signal |
| 2026-09-30T20:10 | CCI reversion | buy | SOL-USD | 17.45 | — | entry signal |
| 2026-09-30T20:10 | Z-score reversion | buy | BTC-USD | 4.13 | — | rebalance up |
| 2026-09-30T20:10 | Z-score reversion | sell | ETH-USD | 4.13 | -0.03 | rebalance down |
| 2026-09-30T20:05 | CCI reversion | buy | XRP-USD | 17.46 | — | entry signal |
| 2026-09-30T20:05 | Z-score reversion | buy | BTC-USD | 4.15 | — | rebalance up |
| 2026-09-30T20:05 | Z-score reversion | sell | SOL-USD | 4.15 | -0.03 | rebalance down |
| 2026-09-30T20:01 | Agent (ML meta-label) | sell | SOL-USD | 4.94 | -0.14 | selected signal exited |
| 2026-09-30T20:01 | Trend pullback · 1h | sell | BTC-USD | 11.92 | -0.13 | exit signal |
| 2026-09-30T20:01 | Supertrend · 1h | sell | SOL-USD | 1.76 | -0.08 | exit signal |
| 2026-09-30T20:01 | MACD zero-line · 1h | sell | BTC-USD | 18.23 | -0.15 | exit signal |
| 2026-09-30T20:01 | MACD cross · 1h | sell | BTC-USD | 5.27 | -0.13 | exit signal |
| 2026-09-30T20:01 | EMA 9/21 cross · 1h | sell | XRP-USD | 10.32 | -0.21 | exit signal |
| 2026-09-30T20:01 | EMA 9/21 cross · 1h | sell | ETH-USD | 10.13 | -0.25 | exit signal |
| 2026-09-30T20:01 | Stochastic reversion | buy | SOL-USD | 18.38 | — | entry signal |
| 2026-09-30T20:01 | Stochastic reversion | buy | ETH-USD | 18.38 | — | entry signal |
| 2026-09-30T20:01 | Stochastic reversion | buy | BTC-USD | 18.38 | — | entry signal |
| 2026-09-30T20:01 | Z-score reversion | buy | BTC-USD | 8.30 | — | entry signal |
| 2026-09-30T20:01 | Z-score reversion | sell | XRP-USD | 4.14 | -0.04 | rebalance down |
| 2026-09-30T20:01 | Z-score reversion | sell | DOGE-USD | 4.16 | -0.02 | rebalance down |
| 2026-09-30T20:01 | Bollinger reversion | buy | XRP-USD | 17.95 | — | entry signal |
| 2026-09-30T20:01 | Bollinger reversion | buy | ETH-USD | 17.95 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
