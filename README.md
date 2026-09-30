# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T22:10:05.000149+00:00 · 7334 ticks

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

Today: 39258 decisions in 3294 calls, $0.4863 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T22:10 | 1 / 0 / 4 | cash |  |
| Breezy | 2026-09-30T22:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T22:10 | 0 / 5 / 0 | cash |  |

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
| 4 | Copy: Congress Democrats (NANC) | copy | 99.85 | -0.15 | 0 | — | 5.20 | 2.20 | -3.62 | 1 |
| 5 | Hold BTC | benchmark | 99.71 | -0.29 | 0 | — | 28.42 | 3.58 | -8.68 | 1 |
| 6 | Agent | meta | 99.63 | -0.37 | 27 | 66.7 | -10.23 | -6.84 | -10.80 | 224 |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.65 | 1.35 | -2.11 | 83 |
| 8 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -1.50 | -0.81 | -4.46 | 99 |
| 9 | VWAP reversion · 1h | reversion | 99.42 | -0.58 | 22 | 27.3 | -11.77 | -4.04 | -14.05 | 121 |
| 10 | RSI(14) reversion · 1h | reversion | 99.39 | -0.61 | 8 | 62.5 | 2.38 | 0.71 | -7.26 | 136 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 99.36 | -0.64 | 0 | — | -3.22 | -1.95 | -5.09 | 2 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 13 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 2 | 50.0 | -1.10 | -0.29 | -9.74 | 24 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.17 | -0.83 | 0 | — | -2.55 | -1.22 | -5.14 | 1 |
| 15 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 16 | Hold SPY | benchmark | 98.98 | -1.02 | 0 | — | 2.91 | 1.63 | -3.66 | 1 |
| 17 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 14.96 | 3.71 | -4.73 | 182 |
| 18 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 19 | Stochastic reversion · 1h | reversion | 98.63 | -1.37 | 30 | 56.7 | -9.98 | -2.22 | -11.63 | 325 |
| 20 | Copy: Warren Buffett (BRK-B) | copy | 98.61 | -1.39 | 0 | — | -2.22 | -0.87 | -7.65 | 1 |
| 21 | Daily: Bullish score | daily | 98.47 | -1.53 | 3 | 0.0 | -1.05 | 0.05 | -12.76 | 14 |
| 22 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.54 | 0.27 | -15.21 | 46 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 98.24 | -1.76 | 0 | — | -10.46 | -2.12 | -15.27 | 2 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.24 | -1.76 | 0 | — | 2.47 | 0.77 | -7.93 | 7 |
| 25 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.58 | -3.34 | -11.47 | 232 |
| 26 | Copy: Insider buying | copy | 98.16 | -1.84 | 2 | 100.0 | -14.74 | -2.91 | -17.74 | 73 |
| 27 | CCI reversion · 1h | reversion | 98.12 | -1.88 | 42 | 40.5 | 1.95 | 0.49 | -12.41 | 411 |
| 28 | Williams %R · 1h | reversion | 98.11 | -1.89 | 51 | 51.0 | -17.36 | -3.27 | -19.41 | 491 |
| 29 | Candlestick reversal · 1h | reversion | 97.81 | -2.19 | 33 | 24.2 | -26.28 | -6.58 | -26.87 | 494 |
| 30 | Agent (rotation) | meta | 97.76 | -2.24 | 37 | 13.5 | -5.52 | -1.91 | -9.79 | 208 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 97.73 | -2.27 | 0 | — | 26.25 | 3.85 | -6.29 | 1 |
| 32 | Z-score reversion · 1h | reversion | 97.60 | -2.40 | 11 | 45.5 | 3.25 | 0.82 | -8.60 | 153 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.36 | -2.64 | 0 | — | -7.64 | -1.79 | -10.03 | 1 |
| 34 | Bollinger reversion · 1h | reversion | 96.94 | -3.06 | 32 | 34.4 | -16.85 | -4.71 | -17.75 | 305 |
| 35 | EMA 20/50 cross · 1h | trend | 96.27 | -3.73 | 19 | 5.3 | 14.99 | 1.89 | -12.18 | 130 |
| 36 | Opening range 30m | breakout | 96.12 | -3.88 | 49 | 12.2 | -11.24 | -3.27 | -15.06 | 559 |
| 37 | Supertrend · 1h | trend | 95.78 | -4.22 | 19 | 5.3 | 0.68 | 0.29 | -16.43 | 203 |
| 38 | Agent (ML meta-label) | meta | 95.42 | -4.58 | 170 | 12.9 | 5.85 | 1.09 | -12.72 | 406 |
| 39 | Trend pullback · 1h | trend | 95.40 | -4.60 | 33 | 12.1 | -26.12 | -6.99 | -26.13 | 156 |
| 40 | Max aggression: 5-day momentum | meta | 95.35 | -4.65 | 3 | 66.7 | -13.55 | -0.96 | -29.56 | 29 |
| 41 | Donchian 55/20 · 1h | breakout | 95.33 | -4.67 | 15 | 0.0 | 4.58 | 0.80 | -16.96 | 113 |
| 42 | Opening range 15m | breakout | 94.87 | -5.13 | 61 | 14.8 | -12.31 | -3.38 | -17.03 | 686 |
| 43 | MFI reversion · 1h | reversion | 94.51 | -5.49 | 51 | 19.6 | -9.23 | -1.67 | -17.05 | 131 |
| 44 | Squeeze breakout · 1h | breakout | 94.49 | -5.51 | 16 | 6.2 | 12.09 | 2.13 | -7.61 | 98 |
| 45 | Three white soldiers | momentum | 94.48 | -5.52 | 51 | 19.6 | -50.21 | -27.72 | -50.28 | 605 |
| 46 | Parabolic SAR · 1h | trend | 94.30 | -5.70 | 32 | 12.5 | -9.90 | -1.29 | -19.53 | 304 |
| 47 | MACD cross · 1h | trend | 94.08 | -5.92 | 46 | 8.7 | -14.32 | -2.27 | -17.47 | 477 |
| 48 | Max aggression: 1-day momentum | meta | 93.99 | -6.01 | 3 | 33.3 | -21.69 | -1.04 | -41.28 | 42 |
| 49 | Volume breakout · 1h | breakout | 93.79 | -6.21 | 29 | 3.4 | 5.32 | 0.94 | -12.60 | 122 |
| 50 | ADX DI cross · 1h | trend | 93.69 | -6.31 | 35 | 5.7 | -16.04 | -3.03 | -17.45 | 261 |
| 51 | Ichimoku · 1h | trend | 92.88 | -7.12 | 21 | 14.3 | 4.66 | 0.75 | -15.26 | 122 |
| 52 | RSI momentum · 1h | momentum | 92.44 | -7.56 | 30 | 3.3 | -4.01 | -0.35 | -16.07 | 222 |
| 53 | VWAP momentum · 1h | momentum | 92.19 | -7.81 | 127 | 15.7 | -39.20 | -6.30 | -39.27 | 1247 |
| 54 | Bollinger breakout · 1h | breakout | 92.07 | -7.93 | 25 | 8.0 | 4.98 | 0.85 | -10.56 | 280 |
| 55 | Triple EMA stack · 1h | trend | 91.21 | -8.79 | 40 | 5.0 | -9.12 | -0.92 | -22.27 | 233 |
| 56 | EMA 9/21 cross · 1h | trend | 91.06 | -8.94 | 51 | 9.8 | -8.72 | -1.01 | -17.43 | 320 |
| 57 | MACD zero-line · 1h | trend | 90.88 | -9.12 | 28 | 3.6 | -9.27 | -1.11 | -17.32 | 232 |
| 58 | Keltner breakout · 1h | breakout | 90.82 | -9.18 | 15 | 0.0 | -8.78 | -1.02 | -20.71 | 217 |
| 59 | RSI(14) reversion | reversion | 90.67 | -9.33 | 131 | 35.1 | -71.45 | -21.59 | -71.52 | 1474 |
| 60 | Heikin-Ashi · 1h | trend | 90.58 | -9.42 | 59 | 8.5 | -29.02 | -4.77 | -31.82 | 684 |
| 61 | Donchian 20/10 · 1h | breakout | 89.91 | -10.09 | 23 | 8.7 | -1.39 | 0.04 | -14.99 | 218 |
| 62 | OBV trend · 1h | momentum | 88.88 | -11.12 | 70 | 5.7 | -14.46 | -1.66 | -25.03 | 322 |
| 63 | Squeeze breakout | breakout | 87.41 | -12.59 | 110 | 13.6 | -59.23 | -18.16 | -59.30 | 1177 |
| 64 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 61 | 4.9 | -15.20 | -2.04 | -22.42 | 413 |
| 65 | Donchian 55/20 | breakout | 86.05 | -13.95 | 120 | 20.0 | -67.14 | -15.17 | -67.22 | 1290 |
| 66 | Volume breakout | breakout | 85.00 | -15.00 | 116 | 15.5 | -62.53 | -20.02 | -62.57 | 893 |
| 67 | ROC + volume | momentum | 84.44 | -15.56 | 183 | 20.2 | -72.18 | -17.58 | -72.21 | 1625 |
| 68 | Keltner breakout | breakout | 83.44 | -16.56 | 174 | 14.9 | -84.44 | -33.68 | -84.46 | 1881 |
| 69 | Ichimoku | trend | 83.10 | -16.90 | 138 | 10.1 | -80.20 | -25.31 | -80.22 | 1739 |
| 70 | VWAP reversion | reversion | 83.03 | -16.97 | 161 | 24.8 | -72.12 | -17.91 | -72.15 | 1402 |
| 71 | EMA 20/50 cross | trend | 82.89 | -17.11 | 151 | 15.9 | -78.94 | -17.42 | -78.94 | 1465 |
| 72 | Z-score reversion | reversion | 82.83 | -17.17 | 207 | 31.4 | -84.94 | -28.03 | -84.95 | 2099 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 79.60 | -20.40 | 205 | 19.0 | -87.58 | -24.40 | -87.58 | 1944 |
| 76 | MFI reversion | reversion | 78.77 | -21.23 | 205 | 19.5 | -88.24 | -35.51 | -88.24 | 2129 |
| 77 | Donchian 20/10 | breakout | 78.52 | -21.48 | 250 | 19.2 | -90.57 | -28.78 | -90.57 | 2660 |
| 78 | MACD zero-line | trend | 78.43 | -21.57 | 248 | 16.1 | -91.67 | -34.84 | -91.67 | 2351 |
| 79 | Trend pullback | trend | 77.79 | -22.21 | 213 | 16.9 | -90.86 | -33.12 | -90.86 | 2271 |
| 80 | RSI momentum | momentum | 77.14 | -22.86 | 240 | 15.4 | -90.17 | -28.32 | -90.17 | 2367 |
| 81 | Triple EMA stack | trend | 76.97 | -23.03 | 258 | 16.3 | -92.81 | -34.42 | -92.81 | 2585 |
| 82 | Bollinger breakout | breakout | 76.92 | -23.08 | 252 | 16.3 | -93.75 | -40.86 | -93.75 | 2838 |
| 83 | ADX DI cross | trend | 75.81 | -24.19 | 238 | 8.0 | -89.48 | -44.37 | -89.50 | 2109 |
| 84 | Stochastic reversion | reversion | 73.35 | -26.65 | 391 | 24.3 | -95.91 | -45.45 | -95.91 | 4046 |
| 85 | Consensus | meta | 72.98 | -27.02 | 230 | 7.4 | -94.68 | -30.15 | -94.68 | 2664 |
| 86 | Connors RSI(2) ⏸ | reversion | 72.37 | -27.63 | 319 | 19.7 | -96.49 | -40.72 | -96.49 | 3638 |
| 87 | EMA 9/21 cross | trend | 72.32 | -27.68 | 342 | 16.7 | -97.36 | -40.49 | -97.36 | 3531 |
| 88 | Bollinger reversion | reversion | 71.64 | -28.36 | 367 | 17.2 | -95.88 | -44.18 | -95.88 | 3691 |
| 89 | Candlestick reversal ⏸ | reversion | 71.29 | -28.71 | 376 | 14.4 | -99.37 | -48.70 | -99.37 | 5615 |
| 90 | OBV trend ⏸ | momentum | 70.20 | -29.80 | 361 | 16.1 | -95.92 | -45.49 | -95.92 | 3537 |
| 91 | CCI reversion | reversion | 69.70 | -30.30 | 319 | 13.2 | -98.50 | -49.22 | -98.50 | 4694 |
| 92 | Parabolic SAR | trend | 69.41 | -30.59 | 329 | 13.4 | -96.88 | -51.17 | -96.88 | 3605 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.55 | -35.67 | -98.55 | 5220 |
| 94 | MACD cross ⏸ | trend | 67.57 | -32.43 | 368 | 14.1 | -99.72 | -61.42 | -99.72 | 6066 |
| 95 | Williams %R ⏸ | reversion | 67.21 | -32.79 | 441 | 22.0 | -99.53 | -56.84 | -99.53 | 6113 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -74.48 | -99.89 | 8280 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T22:10 | RSI momentum | sell | ETH-USD | 19.17 | -0.16 | exit signal |
| 2026-09-30T22:10 | Supertrend | sell | ETH-USD | 19.81 | -0.16 | exit signal |
| 2026-09-30T22:10 | Triple EMA stack | sell | ETH-USD | 19.12 | -0.16 | stop-loss |
| 2026-09-30T22:10 | EMA 20/50 cross | sell | ETH-USD | 20.59 | -0.18 | stop-loss |
| 2026-09-30T22:05 | ROC + volume · 1h | sell | DOGE-USD | 12.22 | -0.15 | target is flat |
| 2026-09-30T22:05 | Donchian 20/10 | sell | ETH-USD | 19.56 | -0.14 | exit signal |
| 2026-09-30T22:05 | ADX DI cross | sell | BTC-USD | 18.85 | -0.13 | exit signal |
| 2026-09-30T22:05 | MACD zero-line | sell | ETH-USD | 19.55 | -0.12 | exit signal |
| 2026-09-30T22:05 | EMA 9/21 cross | sell | BTC-USD | 18.00 | -0.12 | exit signal |
| 2026-09-30T22:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 7.03 | -0.12 | exit signal |
| 2026-09-30T21:55 | Stochastic reversion | buy | DOGE-USD | 18.36 | — | entry signal |
| 2026-09-30T21:55 | Bollinger reversion | buy | XRP-USD | 17.93 | — | entry signal |
| 2026-09-30T21:55 | EMA 9/21 cross | buy | BTC-USD | 18.12 | — | entry signal |
| 2026-09-30T21:50 | EMA 9/21 cross | sell | SOL-USD | 18.04 | -0.14 | exit signal |
| 2026-09-30T21:50 | EMA 9/21 cross | sell | DOGE-USD | 18.12 | -0.15 | exit signal |
| 2026-09-30T21:50 | EMA 9/21 cross | sell | BTC-USD | 18.08 | -0.12 | exit signal |
| 2026-09-30T21:45 | Volume breakout | sell | ETH-USD | 21.14 | -0.14 | exit signal |
| 2026-09-30T21:40 | Triple EMA stack | buy | ETH-USD | 19.28 | — | entry signal |
| 2026-09-30T21:35 | EMA 20/50 cross | buy | ETH-USD | 20.77 | — | entry signal |
| 2026-09-30T21:35 | EMA 9/21 cross | buy | SOL-USD | 18.19 | — | entry signal |
| 2026-09-30T21:35 | EMA 9/21 cross | buy | BTC-USD | 18.21 | — | entry signal |
| 2026-09-30T21:25 | Bollinger breakout | sell | DOGE-USD | 19.08 | -0.21 | exit signal |
| 2026-09-30T21:25 | Donchian 20/10 | sell | DOGE-USD | 19.54 | -0.16 | exit signal |
| 2026-09-30T21:25 | MACD zero-line | sell | DOGE-USD | 19.48 | -0.21 | exit signal |
| 2026-09-30T21:25 | EMA 9/21 cross | sell | SOL-USD | 18.10 | -0.15 | exit signal |
| 2026-09-30T21:20 | CCI reversion | sell | BTC-USD | 17.38 | -0.08 | exit signal |
| 2026-09-30T21:20 | ADX DI cross | buy | BTC-USD | 18.98 | — | entry signal |
| 2026-09-30T21:10 | Volume breakout | buy | ETH-USD | 21.29 | — | entry signal |
| 2026-09-30T21:10 | EMA 9/21 cross | buy | SOL-USD | 18.25 | — | entry signal |
| 2026-09-30T21:05 | Stochastic reversion | sell | BTC-USD | 18.31 | -0.07 | exit signal |
| 2026-09-30T21:05 | Donchian 20/10 | buy | ETH-USD | 19.70 | — | entry signal |
| 2026-09-30T21:05 | RSI momentum | buy | ETH-USD | 19.32 | — | entry signal |
| 2026-09-30T21:05 | Supertrend | buy | ETH-USD | 19.97 | — | entry signal |
| 2026-09-30T21:00 | Stochastic reversion · 1h | buy | SOL-USD | 3.97 | — | entry signal |
| 2026-09-30T21:00 | Candlestick reversal · 1h | buy | ETH-USD | 6.23 | — | entry signal |
| 2026-09-30T20:55 | Z-score reversion | buy | XRP-USD | 4.15 | — | rebalance up |
| 2026-09-30T20:45 | MACD zero-line | buy | ETH-USD | 19.67 | — | entry signal |
| 2026-09-30T20:40 | Stochastic reversion | sell | SOL-USD | 18.41 | 0.03 | exit signal |
| 2026-09-30T20:40 | Z-score reversion | sell | ETH-USD | 20.73 | -0.09 | exit signal |
| 2026-09-30T20:40 | Bollinger reversion | sell | BTC-USD | 17.88 | -0.08 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
