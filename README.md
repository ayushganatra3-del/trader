# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-01T10:10:05.000149+00:00 · 7619 ticks

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

Today: 3095 decisions in 619 calls, $0.0435 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-01T10:10 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-01T10:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-01T10:10 | 1 / 3 / 1 | ETH-USD 65% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.70 | 0.70 | 3 | 33.3 | 13.60 | 2.92 | -7.55 | 43 |
| 2 | Copy: Congress Democrats (NANC) | copy | 100.25 | 0.25 | 0 | — | 5.20 | 2.18 | -3.62 | 1 |
| 3 | Hold BTC | benchmark | 100.18 | 0.18 | 0 | — | 30.59 | 3.82 | -8.68 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 99.76 | -0.24 | 0 | — | -3.22 | -1.93 | -5.09 | 2 |
| 7 | Agent | meta | 99.63 | -0.37 | 27 | 66.7 | -10.23 | -6.78 | -10.80 | 224 |
| 8 | RSI(14) reversion · 1h | reversion | 99.59 | -0.41 | 8 | 62.5 | 4.03 | 1.14 | -7.26 | 133 |
| 9 | Copy: Hedge-fund gurus (GURU) | copy | 99.57 | -0.43 | 0 | — | -2.55 | -1.21 | -5.14 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.52 | -0.48 | 22 | 27.3 | -10.76 | -3.66 | -14.05 | 114 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.65 | 1.34 | -2.11 | 83 |
| 12 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -1.50 | -0.81 | -4.46 | 99 |
| 13 | Hold SPY | benchmark | 99.38 | -0.62 | 0 | — | 2.91 | 1.62 | -3.66 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 15 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 2 | 50.0 | -1.10 | -0.29 | -9.74 | 24 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.38 | -5.16 | 27 |
| 17 | Stochastic reversion · 1h | reversion | 99.02 | -0.98 | 30 | 56.7 | -9.50 | -2.08 | -10.86 | 322 |
| 18 | Copy: Warren Buffett (BRK-B) | copy | 99.01 | -0.99 | 0 | — | -2.22 | -0.86 | -7.65 | 1 |
| 19 | Daily: Bullish score | daily | 98.86 | -1.14 | 3 | 0.0 | -1.05 | 0.05 | -12.76 | 14 |
| 20 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 14.85 | 3.65 | -4.73 | 182 |
| 21 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 98.64 | -1.36 | 0 | — | -10.46 | -2.10 | -15.27 | 2 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.64 | -1.36 | 0 | — | 2.47 | 0.76 | -7.93 | 7 |
| 24 | Copy: Insider buying | copy | 98.55 | -1.45 | 2 | 100.0 | -14.74 | -2.89 | -17.74 | 73 |
| 25 | CCI reversion · 1h | reversion | 98.46 | -1.54 | 42 | 40.5 | 1.89 | 0.48 | -12.41 | 413 |
| 26 | Williams %R · 1h | reversion | 98.42 | -1.58 | 52 | 50.0 | -16.75 | -3.11 | -19.41 | 490 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.54 | 0.27 | -15.21 | 46 |
| 28 | Candlestick reversal · 1h | reversion | 98.23 | -1.77 | 33 | 24.2 | -25.59 | -6.35 | -26.77 | 491 |
| 29 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.58 | -3.31 | -11.47 | 232 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 98.13 | -1.87 | 0 | — | 26.25 | 3.82 | -6.29 | 1 |
| 31 | Z-score reversion · 1h | reversion | 97.99 | -2.01 | 11 | 45.5 | 3.25 | 0.82 | -8.60 | 153 |
| 32 | Agent (rotation) | meta | 97.76 | -2.24 | 37 | 13.5 | -5.27 | -1.80 | -9.79 | 211 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.75 | -2.25 | 0 | — | -7.64 | -1.77 | -10.03 | 1 |
| 34 | Bollinger reversion · 1h | reversion | 97.33 | -2.67 | 32 | 34.4 | -16.74 | -4.64 | -17.77 | 305 |
| 35 | EMA 20/50 cross · 1h | trend | 96.56 | -3.44 | 20 | 5.0 | 15.92 | 1.98 | -12.18 | 130 |
| 36 | Supertrend · 1h | trend | 96.19 | -3.81 | 19 | 5.3 | 0.70 | 0.29 | -16.43 | 203 |
| 37 | Opening range 30m | breakout | 96.12 | -3.88 | 49 | 12.2 | -11.24 | -3.24 | -15.06 | 559 |
| 38 | Max aggression: 5-day momentum | meta | 95.73 | -4.27 | 3 | 66.7 | -13.55 | -0.95 | -29.56 | 29 |
| 39 | Agent (ML meta-label) | meta | 95.72 | -4.28 | 173 | 12.7 | 4.28 | 0.87 | -12.19 | 409 |
| 40 | Donchian 55/20 · 1h | breakout | 95.71 | -4.29 | 15 | 0.0 | 4.58 | 0.79 | -16.96 | 113 |
| 41 | Trend pullback · 1h | trend | 95.56 | -4.43 | 35 | 11.4 | -25.91 | -6.89 | -26.13 | 158 |
| 42 | Opening range 15m | breakout | 94.87 | -5.13 | 61 | 14.8 | -12.54 | -3.41 | -17.25 | 687 |
| 43 | MFI reversion · 1h | reversion | 94.80 | -5.20 | 52 | 19.2 | -8.92 | -1.59 | -17.05 | 128 |
| 44 | Parabolic SAR · 1h | trend | 94.54 | -5.46 | 33 | 12.1 | -9.95 | -1.28 | -19.53 | 305 |
| 45 | Squeeze breakout · 1h | breakout | 94.49 | -5.51 | 16 | 6.2 | 12.09 | 2.12 | -7.61 | 98 |
| 46 | MACD cross · 1h | trend | 94.41 | -5.59 | 48 | 10.4 | -15.07 | -2.39 | -17.47 | 482 |
| 47 | Max aggression: 1-day momentum | meta | 94.37 | -5.63 | 3 | 33.3 | -21.69 | -1.04 | -41.28 | 42 |
| 48 | Three white soldiers | momentum | 94.29 | -5.71 | 52 | 19.2 | -50.12 | -27.33 | -50.12 | 604 |
| 49 | ADX DI cross · 1h | trend | 94.06 | -5.94 | 35 | 5.7 | -16.37 | -3.06 | -17.79 | 262 |
| 50 | Volume breakout · 1h | breakout | 93.79 | -6.21 | 29 | 3.4 | 5.32 | 0.93 | -12.60 | 122 |
| 51 | Ichimoku · 1h | trend | 93.17 | -6.83 | 21 | 14.3 | 4.48 | 0.73 | -15.66 | 121 |
| 52 | RSI momentum · 1h | momentum | 92.75 | -7.25 | 30 | 3.3 | -3.48 | -0.27 | -16.26 | 220 |
| 53 | VWAP momentum · 1h | momentum | 92.56 | -7.44 | 127 | 15.7 | -39.37 | -6.30 | -39.37 | 1257 |
| 54 | Bollinger breakout · 1h | breakout | 92.26 | -7.74 | 25 | 8.0 | 4.98 | 0.84 | -10.56 | 280 |
| 55 | Triple EMA stack · 1h | trend | 91.56 | -8.44 | 40 | 5.0 | -9.65 | -0.99 | -22.71 | 238 |
| 56 | EMA 9/21 cross · 1h | trend | 91.20 | -8.80 | 53 | 9.4 | -8.63 | -0.99 | -17.94 | 322 |
| 57 | MACD zero-line · 1h | trend | 91.15 | -8.85 | 29 | 6.9 | -9.04 | -1.07 | -17.53 | 232 |
| 58 | Heikin-Ashi · 1h | trend | 90.95 | -9.05 | 59 | 8.5 | -29.87 | -4.90 | -32.90 | 688 |
| 59 | Keltner breakout · 1h | breakout | 90.91 | -9.09 | 15 | 0.0 | -8.78 | -1.01 | -20.71 | 217 |
| 60 | Donchian 20/10 · 1h | breakout | 90.10 | -9.90 | 23 | 8.7 | -1.39 | 0.04 | -14.99 | 218 |
| 61 | RSI(14) reversion | reversion | 89.90 | -10.10 | 141 | 34.0 | -71.43 | -21.13 | -71.60 | 1469 |
| 62 | OBV trend · 1h | momentum | 89.15 | -10.85 | 70 | 5.7 | -15.17 | -1.74 | -25.58 | 328 |
| 63 | ROC + volume · 1h | momentum | 86.50 | -13.50 | 62 | 4.8 | -15.08 | -2.01 | -22.31 | 412 |
| 64 | Squeeze breakout | breakout | 86.37 | -13.63 | 115 | 13.0 | -59.41 | -17.97 | -59.51 | 1183 |
| 65 | Donchian 55/20 | breakout | 85.41 | -14.59 | 123 | 19.5 | -67.25 | -15.04 | -67.29 | 1295 |
| 66 | Volume breakout | breakout | 84.58 | -15.42 | 118 | 15.3 | -62.78 | -19.92 | -62.81 | 900 |
| 67 | ROC + volume | momentum | 83.71 | -16.29 | 186 | 19.9 | -72.21 | -17.38 | -72.49 | 1637 |
| 68 | Keltner breakout | breakout | 83.04 | -16.96 | 176 | 14.8 | -84.25 | -32.26 | -84.25 | 1879 |
| 69 | VWAP reversion | reversion | 82.96 | -17.04 | 162 | 25.3 | -71.07 | -17.31 | -71.29 | 1385 |
| 70 | EMA 20/50 cross | trend | 82.09 | -17.91 | 155 | 15.5 | -79.23 | -17.41 | -79.23 | 1471 |
| 71 | AI bee: Bizzy | ai | 81.88 | -18.12 | 299 | 9.0 | — | — | — | — |
| 72 | Z-score reversion | reversion | 81.87 | -18.13 | 217 | 30.4 | -84.93 | -27.53 | -84.98 | 2096 |
| 73 | Ichimoku | trend | 81.76 | -18.24 | 145 | 9.7 | -80.38 | -25.03 | -80.51 | 1748 |
| 74 | AI bee: Boozy | ai | 81.40 | -18.59 | 109 | 0.9 | — | — | — | — |
| 75 | MFI reversion | reversion | 78.37 | -21.63 | 210 | 19.5 | -88.07 | -34.01 | -88.11 | 2133 |
| 76 | Supertrend | trend | 78.10 | -21.90 | 213 | 18.3 | -87.24 | -23.86 | -87.24 | 1936 |
| 77 | Trend pullback | trend | 77.79 | -22.21 | 213 | 16.9 | -91.03 | -32.98 | -91.03 | 2282 |
| 78 | MACD zero-line | trend | 76.65 | -23.35 | 258 | 15.5 | -91.54 | -33.20 | -91.54 | 2350 |
| 79 | Donchian 20/10 | breakout | 76.44 | -23.56 | 261 | 18.4 | -90.60 | -28.07 | -90.60 | 2664 |
| 80 | Triple EMA stack | trend | 76.19 | -23.81 | 263 | 16.0 | -92.88 | -33.78 | -92.89 | 2593 |
| 81 | Bollinger breakout | breakout | 75.64 | -24.36 | 261 | 15.7 | -93.72 | -38.64 | -93.73 | 2841 |
| 82 | RSI momentum | momentum | 75.31 | -24.69 | 250 | 14.8 | -90.21 | -27.69 | -90.21 | 2372 |
| 83 | ADX DI cross | trend | 75.15 | -24.85 | 243 | 7.8 | -89.45 | -42.17 | -89.46 | 2109 |
| 84 | Stochastic reversion | reversion | 72.80 | -27.20 | 401 | 23.7 | -95.76 | -43.19 | -95.76 | 4026 |
| 85 | Consensus | meta | 72.75 | -27.25 | 231 | 7.4 | -94.61 | -29.55 | -94.61 | 2654 |
| 86 | Connors RSI(2) | reversion | 72.19 | -27.81 | 320 | 19.7 | -96.54 | -39.84 | -96.54 | 3646 |
| 87 | Bollinger reversion | reversion | 70.23 | -29.77 | 382 | 16.5 | -95.89 | -43.19 | -95.89 | 3690 |
| 88 | EMA 9/21 cross | trend | 70.17 | -29.83 | 358 | 15.9 | -97.35 | -39.18 | -97.35 | 3532 |
| 89 | Candlestick reversal | reversion | 69.93 | -30.07 | 390 | 13.8 | -99.35 | -48.00 | -99.35 | 5592 |
| 90 | OBV trend | momentum | 69.72 | -30.28 | 364 | 15.9 | -95.97 | -44.22 | -95.97 | 3560 |
| 91 | CCI reversion | reversion | 68.81 | -31.19 | 335 | 13.1 | -98.49 | -47.92 | -98.50 | 4690 |
| 92 | Parabolic SAR | trend | 68.35 | -31.65 | 337 | 13.1 | -96.98 | -50.43 | -96.98 | 3627 |
| 93 | VWAP momentum | momentum | 67.02 | -32.98 | 424 | 9.0 | -98.62 | -35.73 | -98.62 | 5272 |
| 94 | MACD cross | trend | 66.37 | -33.63 | 379 | 13.7 | -99.71 | -57.37 | -99.71 | 6062 |
| 95 | Heikin-Ashi | trend | 65.60 | -34.40 | 337 | 6.2 | -99.89 | -68.04 | -99.89 | 8280 |
| 96 | Williams %R | reversion | 65.47 | -34.53 | 457 | 21.2 | -99.53 | -54.23 | -99.53 | 6106 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-01T10:10 | Williams %R | buy | XRP-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Williams %R | buy | SOL-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Williams %R | buy | ETH-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Williams %R | buy | DOGE-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Williams %R | buy | BTC-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Bollinger reversion | buy | XRP-USD | 17.60 | — | entry signal |
| 2026-10-01T10:10 | Bollinger reversion | buy | SOL-USD | 17.60 | — | entry signal |
| 2026-10-01T10:10 | Bollinger reversion | buy | DOGE-USD | 17.60 | — | entry signal |
| 2026-10-01T10:10 | MACD cross | sell | ETH-USD | 13.33 | -0.04 | exit signal |
| 2026-10-01T10:05 | Williams %R | sell | SOL-USD | 16.28 | -0.18 | stop-loss |
| 2026-10-01T10:05 | Z-score reversion | buy | DOGE-USD | 4.10 | — | rebalance up |
| 2026-10-01T10:05 | Connors RSI(2) | sell | ETH-USD | 17.91 | -0.19 | stop-loss |
| 2026-10-01T10:05 | RSI(14) reversion | buy | DOGE-USD | 4.54 | — | rebalance up |
| 2026-10-01T10:05 | Candlestick reversal | sell | SOL-USD | 17.49 | -0.13 | exit signal |
| 2026-10-01T10:05 | Candlestick reversal | sell | DOGE-USD | 17.40 | -0.20 | stop-loss |
| 2026-10-01T10:05 | Donchian 20/10 | sell | ETH-USD | 19.03 | -0.21 | stop-loss |
| 2026-10-01T10:05 | Donchian 20/10 | sell | BTC-USD | 19.09 | -0.16 | exit signal |
| 2026-10-01T10:05 | RSI momentum | sell | ETH-USD | 18.71 | -0.23 | stop-loss |
| 2026-10-01T10:05 | RSI momentum | sell | BTC-USD | 18.74 | -0.20 | stop-loss |
| 2026-10-01T10:05 | ROC + volume | sell | ETH-USD | 20.80 | -0.25 | stop-loss |
| 2026-10-01T10:05 | ROC + volume | sell | BTC-USD | 20.83 | -0.21 | stop-loss |
| 2026-10-01T10:05 | VWAP momentum | sell | BTC-USD | 16.70 | -0.15 | exit signal |
| 2026-10-01T10:05 | ADX DI cross | sell | BTC-USD | 18.74 | -0.16 | exit signal |
| 2026-10-01T10:05 | Supertrend | sell | ETH-USD | 19.39 | -0.23 | exit signal |
| 2026-10-01T10:05 | Supertrend | sell | BTC-USD | 19.44 | -0.19 | exit signal |
| 2026-10-01T10:05 | MACD zero-line | sell | ETH-USD | 19.03 | -0.23 | stop-loss |
| 2026-10-01T10:05 | MACD zero-line | sell | BTC-USD | 19.08 | -0.19 | stop-loss |
| 2026-10-01T10:05 | MACD cross | sell | XRP-USD | 9.94 | -0.12 | exit signal |
| 2026-10-01T10:05 | MACD cross | sell | SOL-USD | 16.54 | -0.18 | stop-loss |
| 2026-10-01T10:05 | MACD cross | sell | DOGE-USD | 13.20 | -0.14 | stop-loss |
| 2026-10-01T10:05 | EMA 9/21 cross | sell | XRP-USD | 17.46 | -0.27 | stop-loss |
| 2026-10-01T10:05 | EMA 9/21 cross | sell | ETH-USD | 14.03 | -0.16 | stop-loss |
| 2026-10-01T10:05 | EMA 9/21 cross | sell | BTC-USD | 14.07 | -0.13 | stop-loss |
| 2026-10-01T10:00 | MFI reversion · 1h | buy | BTC-USD | 19.00 | — | entry |
| 2026-10-01T10:00 | MFI reversion · 1h | sell | ETH-USD | 19.07 | -0.10 | exit signal |
| 2026-10-01T10:00 | Trend pullback · 1h | buy | BTC-USD | 13.66 | — | entry signal |
| 2026-10-01T10:00 | MACD zero-line · 1h | sell | ETH-USD | 22.75 | 0.03 | exit signal |
| 2026-10-01T10:00 | MACD cross · 1h | sell | ETH-USD | 4.07 | 0.01 | exit signal |
| 2026-10-01T10:00 | Williams %R | buy | SOL-USD | 16.46 | — | entry signal |
| 2026-10-01T10:00 | ADX DI cross | sell | ETH-USD | 18.77 | -0.11 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
