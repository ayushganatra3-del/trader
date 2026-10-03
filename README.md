# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T02:05:05.000209+00:00 · 9522 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.24 (-0.76%)

Closed trades 32, win rate 65.6%, fees £0.92, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, ETRA 12%, BBD 12%, BPRE 12%, GME 12%, NYAX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 1575 decisions in 315 calls, $0.0221 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T02:05 | 1 / 3 / 1 | AMZN 16%, COIN 16%, MSTR 15% |  |
| Breezy | 2026-10-03T02:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T02:05 | 0 / 3 / 2 | ETH-USD 41% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion · 1h | UPRO | 2.43 | +6.89% | 3 |
| Stochastic reversion · 1h | SPY | 2.28 | +2.53% | 3 |
| Connors RSI(2) · 1h | COIN | 2.23 | +6.43% | 5 |
| Stochastic reversion | MSFT | 2.20 | +2.95% | 13 |
| RSI(14) reversion | SQQQ | 2.18 | +4.27% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.27 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 101.16 | 1.16 | 0 | — | 33.23 | 4.08 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.74 | -3.18 | -14.05 | 116 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.22 | -5.28 | -26.34 | 497 |
| 8 | RSI(14) reversion · 1h | reversion | 100.61 | 0.61 | 10 | 60.0 | 4.99 | 1.43 | -6.57 | 118 |
| 9 | Bollinger reversion · 1h | reversion | 100.19 | 0.19 | 38 | 44.7 | -14.32 | -3.79 | -17.62 | 307 |
| 10 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.91 | 1.94 | -1.46 | 86 |
| 14 | Z-score reversion · 1h | reversion | 99.77 | -0.23 | 18 | 55.6 | 5.65 | 1.30 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.70 | 1.05 | -16.96 | 115 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.07 | -0.93 | 40 | 60.0 | -8.12 | -1.68 | -9.82 | 334 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 2.26 | 0.53 | -12.41 | 418 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 45 | 20.0 | -22.48 | -5.77 | -25.84 | 158 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.90 | -2.10 | 50 | 20.0 | -3.16 | -1.18 | -8.90 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 14.00 | 1.75 | -14.40 | 132 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -12.45 | -4.20 | -14.21 | 226 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.63 | -3.04 | -19.41 | 500 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 1.85 | 0.48 | -11.14 | 379 |
| 37 | MFI reversion · 1h | reversion | 96.62 | -3.38 | 69 | 29.0 | -6.97 | -1.15 | -16.99 | 121 |
| 38 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -7.86 | -0.96 | -19.70 | 311 |
| 39 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.84 | 2.87 | -4.73 | 199 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 2.56 | 0.53 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.60 | -3.69 | -21.08 | 71 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -5.66 | -0.80 | -13.84 | 273 |
| 44 | MACD cross · 1h | trend | 95.50 | -4.50 | 71 | 15.5 | -14.70 | -2.37 | -17.27 | 483 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.32 | 2.92 | -8.06 | 112 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.31 | 0.92 | -16.19 | 127 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.88 | 0.45 | -16.65 | 227 |
| 49 | VWAP momentum · 1h | momentum | 93.45 | -6.55 | 171 | 22.8 | -40.98 | -6.46 | -42.62 | 1284 |
| 50 | Bollinger breakout · 1h | breakout | 93.18 | -6.82 | 36 | 16.7 | 5.71 | 0.93 | -12.06 | 292 |
| 51 | Triple EMA stack · 1h | trend | 93.11 | -6.89 | 50 | 8.0 | -7.32 | -0.69 | -23.88 | 240 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.24 | -4.58 | -18.91 | 695 |
| 53 | Three white soldiers | momentum | 92.52 | -7.48 | 66 | 16.7 | -49.26 | -26.26 | -49.26 | 591 |
| 54 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 2.74 | 0.57 | -12.60 | 128 |
| 55 | EMA 9/21 cross · 1h | trend | 91.74 | -8.26 | 68 | 11.8 | -5.13 | -0.51 | -18.47 | 343 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | Heikin-Ashi · 1h | trend | 91.08 | -8.92 | 86 | 25.6 | -32.95 | -5.85 | -33.58 | 690 |
| 58 | MACD zero-line · 1h | trend | 90.81 | -9.19 | 38 | 13.2 | -4.93 | -0.44 | -18.32 | 238 |
| 59 | Donchian 20/10 · 1h | breakout | 90.65 | -9.35 | 31 | 12.9 | 0.01 | 0.22 | -16.18 | 219 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -13.38 | -1.49 | -26.66 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.35 | -1.35 | -23.19 | 213 |
| 62 | RSI(14) reversion | reversion | 87.33 | -12.67 | 179 | 34.6 | -72.40 | -20.98 | -72.45 | 1461 |
| 63 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -12.86 | -1.65 | -23.45 | 424 |
| 64 | Squeeze breakout | breakout | 82.84 | -17.16 | 174 | 16.1 | -60.32 | -18.33 | -60.98 | 1207 |
| 65 | Donchian 55/20 | breakout | 82.40 | -17.60 | 169 | 18.9 | -68.21 | -15.31 | -68.25 | 1307 |
| 66 | EMA 20/50 cross | trend | 80.14 | -19.86 | 191 | 18.8 | -78.86 | -16.73 | -79.03 | 1483 |
| 67 | Volume breakout | breakout | 79.88 | -20.12 | 157 | 14.0 | -64.22 | -20.02 | -64.22 | 910 |
| 68 | VWAP reversion | reversion | 79.87 | -20.12 | 208 | 28.8 | -71.44 | -17.44 | -71.67 | 1393 |
| 69 | ROC + volume | momentum | 79.77 | -20.23 | 258 | 20.2 | -73.57 | -17.83 | -73.88 | 1668 |
| 70 | AI bee: Bizzy | ai | 78.00 | -22.00 | 402 | 10.2 | — | — | — | — |
| 71 | Z-score reversion | reversion | 77.69 | -22.31 | 274 | 31.0 | -85.85 | -26.94 | -85.87 | 2113 |
| 72 | MFI reversion | reversion | 76.18 | -23.82 | 267 | 22.5 | -88.29 | -33.42 | -88.32 | 2136 |
| 73 | Keltner breakout | breakout | 76.16 | -23.84 | 244 | 13.9 | -85.33 | -32.16 | -85.34 | 1900 |
| 74 | AI bee: Boozy | ai | 75.84 | -24.16 | 149 | 5.4 | — | — | — | — |
| 75 | Ichimoku | trend | 75.70 | -24.30 | 209 | 10.0 | -81.56 | -25.49 | -81.56 | 1764 |
| 76 | Supertrend | trend | 75.37 | -24.63 | 266 | 20.7 | -87.34 | -23.47 | -87.39 | 1952 |
| 77 | Donchian 20/10 | breakout | 72.45 | -27.55 | 341 | 19.4 | -90.87 | -28.05 | -90.89 | 2685 |
| 78 | MACD zero-line | trend | 71.60 | -28.40 | 334 | 17.1 | -91.72 | -32.49 | -91.72 | 2369 |
| 79 | ADX DI cross | trend | 71.34 | -28.66 | 305 | 10.2 | -89.83 | -41.47 | -89.83 | 2122 |
| 80 | Trend pullback | trend | 70.85 | -29.15 | 318 | 17.0 | -91.58 | -32.81 | -91.58 | 2351 |
| 81 | Triple EMA stack | trend | 70.68 | -29.32 | 353 | 16.7 | -93.25 | -33.91 | -93.27 | 2637 |
| 82 | RSI momentum | momentum | 70.16 | -29.84 | 324 | 15.7 | -90.69 | -27.75 | -90.74 | 2402 |
| 83 | Bollinger breakout | breakout | 69.22 | -30.78 | 349 | 16.0 | -93.95 | -38.25 | -93.95 | 2851 |
| 84 | Stochastic reversion | reversion | 67.62 | -32.38 | 519 | 25.8 | -95.84 | -41.08 | -95.84 | 4067 |
| 85 | Consensus | meta | 66.83 | -33.17 | 321 | 9.7 | -94.79 | -29.02 | -94.79 | 2674 |
| 86 | Connors RSI(2) | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.60 | -38.55 | -96.61 | 3650 |
| 87 | Bollinger reversion | reversion | 65.87 | -34.13 | 503 | 18.1 | -95.91 | -40.15 | -95.91 | 3727 |
| 88 | EMA 9/21 cross | trend | 65.55 | -34.45 | 457 | 17.7 | -97.42 | -37.59 | -97.43 | 3561 |
| 89 | OBV trend | momentum | 63.94 | -36.06 | 510 | 15.7 | -96.16 | -42.66 | -96.17 | 3626 |
| 90 | Candlestick reversal | reversion | 63.60 | -36.40 | 566 | 16.8 | -99.35 | -43.71 | -99.35 | 5668 |
| 91 | CCI reversion | reversion | 63.04 | -36.96 | 473 | 17.8 | -98.51 | -44.05 | -98.51 | 4724 |
| 92 | VWAP momentum | momentum | 62.41 | -37.59 | 525 | 9.5 | -98.65 | -34.09 | -98.66 | 5333 |
| 93 | Parabolic SAR | trend | 60.68 | -39.32 | 481 | 14.8 | -97.17 | -48.39 | -97.17 | 3665 |
| 94 | Williams %R | reversion | 59.15 | -40.85 | 584 | 22.9 | -99.52 | -49.03 | -99.52 | 6148 |
| 95 | MACD cross | trend | 58.74 | -41.26 | 554 | 14.6 | -99.72 | -53.49 | -99.72 | 6171 |
| 96 | Heikin-Ashi | trend | 57.47 | -42.53 | 512 | 9.8 | -99.90 | -61.81 | -99.90 | 8354 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T02:00 | AI bee: Boozy | buy | ETH-USD | 31.37 | — | Jev: buy (buy p=0.60) |
| 2026-10-03T02:00 | VWAP momentum · 1h | buy | ETH-USD | 10.01 | — | entry |
| 2026-10-03T02:00 | VWAP momentum · 1h | sell | DOGE-USD | 10.01 | -0.08 | exit signal |
| 2026-10-03T02:00 | Williams %R | buy | BTC-USD | 14.80 | — | entry signal |
| 2026-10-03T02:00 | Stochastic reversion | buy | DOGE-USD | 16.92 | — | entry signal |
| 2026-10-03T02:00 | Parabolic SAR | sell | SOL-USD | 15.10 | -0.12 | exit signal |
| 2026-10-03T01:55 | Squeeze breakout | sell | SOL-USD | 20.70 | -0.10 | exit signal |
| 2026-10-03T01:55 | Squeeze breakout | sell | BTC-USD | 20.47 | -0.13 | exit signal |
| 2026-10-03T01:55 | Bollinger breakout | sell | XRP-USD | 13.86 | -0.04 | exit signal |
| 2026-10-03T01:55 | Bollinger breakout | sell | SOL-USD | 17.25 | -0.07 | exit signal |
| 2026-10-03T01:55 | Bollinger breakout | sell | BTC-USD | 17.29 | -0.11 | exit signal |
| 2026-10-03T01:55 | Parabolic SAR | sell | XRP-USD | 15.18 | -0.10 | exit signal |
| 2026-10-03T01:55 | Parabolic SAR | sell | ETH-USD | 12.16 | -0.03 | exit signal |
| 2026-10-03T01:55 | Parabolic SAR | sell | DOGE-USD | 15.14 | -0.12 | exit signal |
| 2026-10-03T01:55 | MACD cross | sell | ETH-USD | 14.73 | -0.05 | exit signal |
| 2026-10-03T01:50 | Consensus | sell | DOGE-USD | 16.70 | -0.05 | target is flat |
| 2026-10-03T01:50 | Squeeze breakout | sell | DOGE-USD | 20.90 | 0.13 | target is flat |
| 2026-10-03T01:50 | Keltner breakout | sell | DOGE-USD | 19.07 | 0.01 | exit signal |
| 2026-10-03T01:50 | Bollinger breakout | buy | BTC-USD | 6.90 | — | rebalance up |
| 2026-10-03T01:50 | Bollinger breakout | sell | DOGE-USD | 13.83 | -0.04 | target is flat |
| 2026-10-03T01:50 | VWAP momentum | buy | XRP-USD | 3.13 | — | rebalance up |
| 2026-10-03T01:50 | VWAP momentum | buy | SOL-USD | 3.16 | — | rebalance up |
| 2026-10-03T01:50 | VWAP momentum | sell | DOGE-USD | 12.46 | -0.06 | exit signal |
| 2026-10-03T01:50 | Heikin-Ashi | sell | XRP-USD | 14.32 | -0.09 | exit signal |
| 2026-10-03T01:50 | Heikin-Ashi | sell | ETH-USD | 14.31 | -0.10 | exit signal |
| 2026-10-03T01:50 | MACD cross | sell | SOL-USD | 14.64 | -0.10 | exit signal |
| 2026-10-03T01:48 | AI bee: Bizzy | sell | ETH-USD | 10.87 | -0.07 | Jev: sell (sell p=0.60) after 11 min |
| 2026-10-03T01:44 | AI bee: Boozy | sell | ETH-USD | 31.37 | -0.16 | Jev: buy |
| 2026-10-03T01:40 | Z-score reversion · 1h | buy | DOGE-USD | 4.98 | — | entry |
| 2026-10-03T01:40 | Z-score reversion · 1h | sell | XRP-USD | 4.98 | 0.05 | rebalance down |
| 2026-10-03T01:40 | Heikin-Ashi | buy | ETH-USD | 14.41 | — | entry signal |
| 2026-10-03T01:40 | Supertrend | buy | BTC-USD | 3.77 | — | rebalance up |
| 2026-10-03T01:40 | Supertrend | sell | SOL-USD | 3.77 | 0.01 | rebalance down |
| 2026-10-03T01:36 | AI bee: Bizzy | buy | ETH-USD | 10.94 | — | Jev: buy (buy p=0.56) |
| 2026-10-03T01:35 | Heikin-Ashi | buy | XRP-USD | 14.42 | — | entry signal |
| 2026-10-03T01:30 | ROC + volume | sell | DOGE-USD | 19.91 | -0.04 | exit signal |
| 2026-10-03T01:30 | MACD cross | sell | BTC-USD | 14.70 | -0.09 | exit signal |
| 2026-10-03T01:28 | AI bee: Boozy | buy | ETH-USD | 31.54 | — | Jev: buy (buy p=0.59) |
| 2026-10-03T01:27 | AI bee: Bizzy | sell | SOL-USD | 12.48 | -0.13 | Jev: sell (sell p=0.71) after 10 min |
| 2026-10-03T01:25 | AI bee: Boozy | sell | BTC-USD | 31.54 | -0.22 | Jev: buy |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
