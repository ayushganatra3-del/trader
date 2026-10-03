# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T01:05:05.000163+00:00 · 9471 ticks

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

Today: 810 decisions in 162 calls, $0.0114 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T01:05 | 1 / 3 / 1 | AMZN 16%, COIN 16%, MSTR 15% |  |
| Breezy | 2026-10-03T01:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T01:05 | 2 / 3 / 0 | MSTR 58% |  |

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
| 3 | Hold BTC | benchmark | 101.17 | 1.17 | 0 | — | 33.27 | 4.09 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.74 | -3.18 | -14.05 | 116 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.06 | -5.24 | -25.94 | 490 |
| 8 | RSI(14) reversion · 1h | reversion | 100.64 | 0.64 | 10 | 60.0 | 4.96 | 1.42 | -6.57 | 117 |
| 9 | Bollinger reversion · 1h | reversion | 100.16 | 0.16 | 38 | 44.7 | -14.68 | -3.91 | -17.68 | 307 |
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
| 22 | Stochastic reversion · 1h | reversion | 99.05 | -0.95 | 40 | 60.0 | -8.18 | -1.69 | -9.82 | 334 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.74 | 0.45 | -12.41 | 419 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 45 | 20.0 | -22.96 | -5.91 | -25.84 | 160 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.90 | -2.10 | 50 | 20.0 | -3.17 | -1.18 | -8.90 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 14.10 | 1.76 | -14.40 | 132 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -12.45 | -4.20 | -14.21 | 226 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.64 | -3.05 | -19.41 | 500 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 3.51 | 0.77 | -9.81 | 380 |
| 37 | MFI reversion · 1h | reversion | 96.62 | -3.38 | 69 | 29.0 | -6.95 | -1.14 | -16.99 | 121 |
| 38 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -7.86 | -0.96 | -19.70 | 312 |
| 39 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.84 | 2.87 | -4.73 | 199 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 2.56 | 0.53 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.60 | -3.69 | -21.08 | 71 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -5.65 | -0.80 | -13.84 | 271 |
| 44 | MACD cross · 1h | trend | 95.50 | -4.50 | 71 | 15.5 | -14.79 | -2.38 | -17.27 | 483 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.31 | 0.92 | -16.19 | 127 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 2.35 | 0.51 | -16.65 | 227 |
| 49 | VWAP momentum · 1h | momentum | 93.52 | -6.48 | 170 | 22.9 | -40.88 | -6.44 | -42.55 | 1284 |
| 50 | Bollinger breakout · 1h | breakout | 93.18 | -6.82 | 36 | 16.7 | 5.30 | 0.88 | -12.06 | 293 |
| 51 | Triple EMA stack · 1h | trend | 93.11 | -6.89 | 50 | 8.0 | -8.01 | -0.78 | -23.88 | 243 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.24 | -4.58 | -18.91 | 695 |
| 53 | Three white soldiers | momentum | 92.52 | -7.48 | 66 | 16.7 | -49.37 | -26.36 | -49.37 | 593 |
| 54 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 2.74 | 0.57 | -12.60 | 128 |
| 55 | EMA 9/21 cross · 1h | trend | 91.74 | -8.26 | 68 | 11.8 | -4.92 | -0.48 | -18.47 | 342 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | Heikin-Ashi · 1h | trend | 91.04 | -8.96 | 86 | 25.6 | -32.98 | -5.86 | -33.58 | 690 |
| 58 | MACD zero-line · 1h | trend | 90.81 | -9.19 | 38 | 13.2 | -5.05 | -0.45 | -18.32 | 238 |
| 59 | Donchian 20/10 · 1h | breakout | 90.65 | -9.35 | 31 | 12.9 | -0.87 | 0.11 | -16.18 | 221 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -14.31 | -1.62 | -26.66 | 340 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.33 | -1.34 | -23.19 | 213 |
| 62 | RSI(14) reversion | reversion | 87.33 | -12.67 | 179 | 34.6 | -72.47 | -21.01 | -72.52 | 1462 |
| 63 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -12.79 | -1.64 | -23.45 | 424 |
| 64 | Squeeze breakout | breakout | 83.00 | -17.00 | 171 | 15.8 | -60.27 | -18.28 | -60.93 | 1207 |
| 65 | Donchian 55/20 | breakout | 82.36 | -17.64 | 169 | 18.9 | -68.30 | -15.36 | -68.33 | 1308 |
| 66 | EMA 20/50 cross | trend | 80.10 | -19.90 | 191 | 18.8 | -78.87 | -16.73 | -79.03 | 1483 |
| 67 | Volume breakout | breakout | 79.88 | -20.12 | 157 | 14.0 | -64.22 | -20.02 | -64.22 | 910 |
| 68 | VWAP reversion | reversion | 79.87 | -20.12 | 208 | 28.8 | -71.17 | -17.23 | -71.40 | 1387 |
| 69 | ROC + volume | momentum | 79.81 | -20.19 | 257 | 20.2 | -73.59 | -17.84 | -73.88 | 1669 |
| 70 | AI bee: Bizzy | ai | 78.19 | -21.81 | 400 | 10.2 | — | — | — | — |
| 71 | Z-score reversion | reversion | 77.69 | -22.31 | 274 | 31.0 | -85.85 | -26.94 | -85.87 | 2113 |
| 72 | AI bee: Boozy | ai | 76.31 | -23.68 | 147 | 5.4 | — | — | — | — |
| 73 | MFI reversion | reversion | 76.18 | -23.82 | 267 | 22.5 | -88.29 | -33.42 | -88.32 | 2136 |
| 74 | Keltner breakout | breakout | 76.16 | -23.84 | 243 | 13.6 | -85.34 | -32.17 | -85.35 | 1901 |
| 75 | Ichimoku | trend | 75.70 | -24.30 | 209 | 10.0 | -81.56 | -25.49 | -81.56 | 1764 |
| 76 | Supertrend | trend | 75.33 | -24.67 | 266 | 20.7 | -87.35 | -23.49 | -87.39 | 1952 |
| 77 | Donchian 20/10 | breakout | 72.42 | -27.59 | 341 | 19.4 | -90.86 | -28.04 | -90.88 | 2685 |
| 78 | MACD zero-line | trend | 71.60 | -28.40 | 334 | 17.1 | -91.72 | -32.49 | -91.72 | 2369 |
| 79 | ADX DI cross | trend | 71.34 | -28.66 | 305 | 10.2 | -89.81 | -41.34 | -89.81 | 2120 |
| 80 | Trend pullback | trend | 70.85 | -29.15 | 318 | 17.0 | -91.58 | -32.82 | -91.58 | 2352 |
| 81 | Triple EMA stack | trend | 70.64 | -29.36 | 353 | 16.7 | -93.30 | -34.07 | -93.31 | 2640 |
| 82 | RSI momentum | momentum | 70.14 | -29.86 | 324 | 15.7 | -90.69 | -27.77 | -90.74 | 2402 |
| 83 | Bollinger breakout | breakout | 69.40 | -30.60 | 345 | 16.2 | -93.93 | -38.03 | -93.95 | 2851 |
| 84 | Stochastic reversion | reversion | 67.67 | -32.33 | 519 | 25.8 | -95.84 | -41.02 | -95.84 | 4066 |
| 85 | Consensus | meta | 66.89 | -33.11 | 320 | 9.7 | -94.84 | -28.89 | -94.84 | 2679 |
| 86 | Connors RSI(2) | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.60 | -38.55 | -96.60 | 3649 |
| 87 | Bollinger reversion | reversion | 65.87 | -34.13 | 503 | 18.1 | -95.91 | -40.13 | -95.91 | 3727 |
| 88 | EMA 9/21 cross | trend | 65.53 | -34.48 | 457 | 17.7 | -97.42 | -37.61 | -97.43 | 3561 |
| 89 | OBV trend | momentum | 63.90 | -36.09 | 510 | 15.7 | -96.18 | -42.87 | -96.19 | 3628 |
| 90 | Candlestick reversal | reversion | 63.60 | -36.40 | 566 | 16.8 | -99.35 | -43.71 | -99.35 | 5668 |
| 91 | CCI reversion | reversion | 63.04 | -36.96 | 473 | 17.8 | -98.51 | -44.05 | -98.51 | 4724 |
| 92 | VWAP momentum | momentum | 62.53 | -37.47 | 524 | 9.5 | -98.61 | -33.63 | -98.62 | 5317 |
| 93 | Parabolic SAR | trend | 61.12 | -38.88 | 476 | 14.9 | -97.16 | -47.83 | -97.16 | 3664 |
| 94 | Williams %R | reversion | 59.20 | -40.80 | 584 | 22.9 | -99.52 | -48.97 | -99.52 | 6147 |
| 95 | MACD cross | trend | 58.96 | -41.04 | 550 | 14.7 | -99.72 | -53.27 | -99.72 | 6173 |
| 96 | Heikin-Ashi | trend | 57.88 | -42.12 | 507 | 9.9 | -99.90 | -61.16 | -99.90 | 8358 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T01:05 | AI bee: Boozy | sell | ETH-USD | 31.75 | -0.16 | Jev: buy |
| 2026-10-03T01:05 | Consensus | sell | XRP-USD | 16.64 | -0.11 | target is flat |
| 2026-10-03T01:05 | Three white soldiers | sell | XRP-USD | 23.00 | -0.17 | exit signal |
| 2026-10-03T01:05 | Volume breakout | sell | SOL-USD | 19.85 | -0.16 | exit signal |
| 2026-10-03T01:05 | Donchian 20/10 | buy | BTC-USD | 3.62 | — | rebalance up |
| 2026-10-03T01:05 | Donchian 20/10 | sell | ETH-USD | 3.62 | -0.01 | rebalance down |
| 2026-10-03T01:05 | VWAP momentum | buy | XRP-USD | 6.20 | — | rebalance up |
| 2026-10-03T01:05 | VWAP momentum | buy | ETH-USD | 3.13 | — | rebalance up |
| 2026-10-03T01:05 | VWAP momentum | buy | DOGE-USD | 3.14 | — | rebalance up |
| 2026-10-03T01:05 | VWAP momentum | buy | BTC-USD | 3.15 | — | rebalance up |
| 2026-10-03T01:05 | VWAP momentum | sell | SOL-USD | 12.49 | -0.05 | exit signal |
| 2026-10-03T01:05 | Heikin-Ashi | sell | BTC-USD | 11.59 | -0.05 | exit signal |
| 2026-10-03T01:05 | Parabolic SAR | sell | XRP-USD | 15.24 | -0.07 | exit signal |
| 2026-10-03T01:05 | Parabolic SAR | sell | DOGE-USD | 15.26 | -0.06 | exit signal |
| 2026-10-03T01:05 | MACD cross | sell | XRP-USD | 14.64 | -0.09 | exit signal |
| 2026-10-03T01:05 | Triple EMA stack | buy | BTC-USD | 3.52 | — | rebalance up |
| 2026-10-03T01:05 | Triple EMA stack | sell | ETH-USD | 3.52 | -0.02 | rebalance down |
| 2026-10-03T01:00 | AI bee: Bizzy | sell | ETH-USD | 10.73 | -0.07 | Jev: sell (sell p=0.60) after 10 min |
| 2026-10-03T01:00 | Consensus | buy | XRP-USD | 16.75 | — | entry |
| 2026-10-03T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 25.32 | 0.34 | exit signal |
| 2026-10-03T01:00 | VWAP momentum · 1h | buy | DOGE-USD | 10.09 | — | entry signal |
| 2026-10-03T01:00 | VWAP momentum · 1h | buy | BTC-USD | 13.37 | — | entry signal |
| 2026-10-03T01:00 | Heikin-Ashi · 1h | buy | XRP-USD | 22.82 | — | entry signal |
| 2026-10-03T01:00 | Heikin-Ashi · 1h | buy | SOL-USD | 22.82 | — | entry signal |
| 2026-10-03T01:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 22.82 | — | entry signal |
| 2026-10-03T01:00 | Heikin-Ashi | sell | XRP-USD | 14.46 | -0.09 | exit signal |
| 2026-10-03T01:00 | Parabolic SAR | buy | DOGE-USD | 3.07 | — | rebalance up |
| 2026-10-03T01:00 | Parabolic SAR | buy | BTC-USD | 9.16 | — | rebalance up |
| 2026-10-03T01:00 | Parabolic SAR | sell | SOL-USD | 12.23 | -0.02 | exit signal |
| 2026-10-03T01:00 | MACD zero-line | sell | DOGE-USD | 18.05 | 0.12 | target is flat |
| 2026-10-03T01:00 | MACD cross | buy | SOL-USD | 2.96 | — | rebalance up |
| 2026-10-03T01:00 | MACD cross | buy | ETH-USD | 2.96 | — | rebalance up |
| 2026-10-03T01:00 | MACD cross | buy | BTC-USD | 5.82 | — | rebalance up |
| 2026-10-03T01:00 | MACD cross | sell | DOGE-USD | 11.78 | -0.02 | target is flat |
| 2026-10-03T00:55 | Bollinger breakout | buy | BTC-USD | 3.47 | — | rebalance up |
| 2026-10-03T00:55 | Bollinger breakout | sell | ETH-USD | 3.47 | -0.01 | rebalance down |
| 2026-10-03T00:55 | Heikin-Ashi | sell | SOL-USD | 14.45 | -0.11 | exit signal |
| 2026-10-03T00:55 | Ichimoku | buy | BTC-USD | 18.94 | — | entry signal |
| 2026-10-03T00:55 | MACD cross | buy | BTC-USD | 2.95 | — | rebalance up |
| 2026-10-03T00:55 | MACD cross | sell | ETH-USD | 2.95 | -0.01 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
