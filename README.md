# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T01:35:05.000178+00:00 · 11910 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.25 (-0.76%)

Closed trades 33, win rate 66.7%, fees £1.04, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, GME 12%, BPRE 12%, PAM 12%, CX 12%, GPUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 1275 decisions in 255 calls, $0.0179 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T01:35 | 0 / 3 / 2 | AMZN 18%, COIN 17%, MSTR 17% |  |
| Breezy | 2026-10-05T01:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T01:35 | 1 / 4 / 0 | MSTR 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.58 | +4.45% | 4 |
| VWAP reversion | AMZN | 1.94 | +0.87% | 3 |
| Z-score reversion | SQQQ | 1.74 | +3.40% | 6 |
| RSI(14) reversion | SQQQ | 1.71 | +3.09% | 4 |
| VWAP reversion | SQQQ | 1.63 | +1.18% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Hold BTC | benchmark | 103.63 | 3.63 | 0 | — | 35.49 | 4.26 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.19 | 2.19 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.06 | 2.06 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.04 | 1.04 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.95 | 0.95 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.87 | 0.87 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.87 | 0.87 | 53 | 37.7 | -23.42 | -5.32 | -25.75 | 492 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 4.95 | 1.41 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.11 | 0.11 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.83 | -3.92 | -17.55 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.78 | -0.22 | 20 | 55.0 | 6.18 | 1.40 | -8.60 | 158 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.70 | -0.30 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.33 | 1.00 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.62 | -0.38 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.47 | -0.53 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.03 | -0.97 | 45 | 60.0 | -8.07 | -1.65 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.88 | 0.47 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 98.81 | -1.19 | 49 | 22.4 | -21.75 | -5.53 | -25.34 | 158 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -4.27 | -1.61 | -9.74 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.79 | -2.21 | 25 | 8.0 | 13.86 | 1.72 | -14.40 | 137 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.77 | -2.23 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.50 | -2.50 | 60 | 43.3 | -11.84 | -3.96 | -14.21 | 220 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.53 | 70 | 54.3 | -17.15 | -3.13 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.71 | -3.29 | 207 | 17.4 | 1.95 | 0.49 | -11.92 | 356 |
| 37 | Parabolic SAR · 1h | trend | 96.56 | -3.44 | 49 | 16.3 | -5.41 | -0.59 | -19.70 | 305 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.44 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.13 | -3.87 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 41 | MACD cross · 1h | trend | 96.03 | -3.97 | 72 | 16.7 | -11.86 | -1.84 | -17.27 | 476 |
| 42 | Supertrend · 1h | trend | 96.03 | -3.97 | 28 | 7.1 | 3.58 | 0.66 | -16.43 | 202 |
| 43 | Copy: Insider buying | copy | 95.83 | -4.17 | 6 | 50.0 | -18.81 | -3.69 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.68 | -4.32 | 41 | 12.2 | -4.67 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.49 | -4.51 | 24 | 16.7 | 20.69 | 2.95 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.25 | -5.75 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.02 | 40 | 2.5 | 2.03 | 0.46 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.43 | -6.57 | 179 | 22.3 | -38.65 | -6.01 | -39.50 | 1278 |
| 50 | Bollinger breakout · 1h | breakout | 93.35 | -6.65 | 40 | 20.0 | 6.76 | 1.05 | -12.06 | 296 |
| 51 | Triple EMA stack · 1h | trend | 93.14 | -6.86 | 50 | 8.0 | -7.78 | -0.74 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.49 | -7.51 | 30 | 6.7 | 3.18 | 0.62 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 91.83 | -8.17 | 69 | 11.6 | -2.87 | -0.19 | -18.47 | 340 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 91.08 | -8.92 | 31 | 12.9 | 0.10 | 0.23 | -16.18 | 224 |
| 57 | MACD zero-line · 1h | trend | 91.00 | -9.00 | 39 | 15.4 | -2.86 | -0.16 | -18.32 | 236 |
| 58 | Heikin-Ashi · 1h | trend | 90.87 | -9.13 | 96 | 25.0 | -31.74 | -5.52 | -33.92 | 686 |
| 59 | Three white soldiers | momentum | 90.65 | -9.35 | 78 | 14.1 | -49.69 | -26.13 | -50.01 | 594 |
| 60 | OBV trend · 1h | momentum | 89.46 | -10.54 | 97 | 11.3 | -12.45 | -1.35 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.33 | -11.67 | 23 | 4.3 | -11.01 | -1.29 | -23.19 | 217 |
| 62 | ROC + volume · 1h | momentum | 87.26 | -12.74 | 87 | 14.9 | -9.86 | -1.21 | -23.16 | 419 |
| 63 | RSI(14) reversion | reversion | 86.92 | -13.08 | 183 | 33.9 | -70.50 | -19.70 | -70.57 | 1426 |
| 64 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.94 | -16.96 | -69.94 | 1369 |
| 65 | Donchian 55/20 | breakout | 78.60 | -21.40 | 202 | 16.8 | -68.76 | -15.40 | -69.05 | 1316 |
| 66 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.34 | -19.09 | -63.10 | 1238 |
| 67 | ROC + volume | momentum | 78.03 | -21.98 | 268 | 19.4 | -73.39 | -17.47 | -74.15 | 1666 |
| 68 | EMA 20/50 cross | trend | 77.62 | -22.38 | 221 | 17.6 | -78.92 | -16.50 | -79.01 | 1487 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.67 | -19.90 | -64.67 | 918 |
| 70 | Z-score reversion | reversion | 75.89 | -24.11 | 294 | 28.9 | -84.78 | -25.52 | -84.81 | 2081 |
| 71 | MFI reversion | reversion | 73.63 | -26.37 | 293 | 20.8 | -87.57 | -31.59 | -87.61 | 2109 |
| 72 | Supertrend | trend | 72.38 | -27.62 | 300 | 19.7 | -87.38 | -23.10 | -87.40 | 1952 |
| 73 | AI bee: Bizzy | ai | 70.05 | -29.95 | 513 | 8.0 | — | — | — | — |
| 74 | Keltner breakout | breakout | 69.45 | -30.55 | 300 | 11.7 | -85.80 | -31.75 | -85.82 | 1913 |
| 75 | ADX DI cross | trend | 69.06 | -30.94 | 325 | 9.5 | -89.56 | -38.85 | -89.58 | 2109 |
| 76 | Ichimoku | trend | 68.12 | -31.88 | 273 | 8.1 | -82.65 | -25.39 | -82.83 | 1799 |
| 77 | AI bee: Boozy | ai | 67.45 | -32.55 | 200 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.20 | -33.80 | 380 | 15.0 | -92.06 | -32.45 | -92.07 | 2387 |
| 79 | Donchian 20/10 | breakout | 65.75 | -34.25 | 401 | 17.2 | -91.29 | -28.06 | -91.33 | 2702 |
| 80 | RSI momentum | momentum | 64.38 | -35.62 | 382 | 14.4 | -90.94 | -27.95 | -90.94 | 2414 |
| 81 | Triple EMA stack | trend | 63.10 | -36.90 | 432 | 14.6 | -93.68 | -34.31 | -93.68 | 2670 |
| 82 | Trend pullback | trend | 62.98 | -37.02 | 400 | 14.2 | -91.79 | -33.22 | -91.79 | 2381 |
| 83 | Stochastic reversion | reversion | 62.95 | -37.05 | 583 | 23.0 | -95.61 | -38.80 | -95.65 | 4051 |
| 84 | Bollinger reversion | reversion | 62.38 | -37.62 | 546 | 16.7 | -95.62 | -37.84 | -95.62 | 3691 |
| 85 | Bollinger breakout | breakout | 62.03 | -37.97 | 416 | 13.7 | -94.24 | -37.68 | -94.27 | 2874 |
| 86 | Consensus | meta | 60.59 | -39.41 | 383 | 8.6 | -94.35 | -27.48 | -94.35 | 2640 |
| 87 | EMA 9/21 cross | trend | 58.66 | -41.34 | 539 | 16.3 | -97.58 | -37.37 | -97.59 | 3594 |
| 88 | Connors RSI(2) | reversion | 58.52 | -41.48 | 509 | 15.9 | -96.62 | -37.33 | -96.62 | 3662 |
| 89 | Candlestick reversal | reversion | 57.24 | -42.76 | 645 | 14.9 | -99.30 | -41.76 | -99.30 | 5637 |
| 90 | CCI reversion | reversion | 57.08 | -42.92 | 550 | 15.3 | -98.45 | -42.41 | -98.45 | 4716 |
| 91 | VWAP momentum | momentum | 56.20 | -43.80 | 607 | 9.1 | -98.68 | -33.53 | -98.69 | 5345 |
| 92 | OBV trend | momentum | 55.85 | -44.15 | 603 | 14.1 | -96.45 | -42.98 | -96.47 | 3670 |
| 93 | Parabolic SAR | trend | 53.83 | -46.17 | 553 | 12.8 | -97.42 | -45.22 | -97.43 | 3717 |
| 94 | MACD cross | trend | 52.10 | -47.90 | 630 | 12.9 | -99.73 | -50.60 | -99.73 | 6202 |
| 95 | Williams %R | reversion | 51.87 | -48.13 | 687 | 19.5 | -99.50 | -46.63 | -99.50 | 6139 |
| 96 | Heikin-Ashi | trend | 50.53 | -49.47 | 595 | 8.4 | -99.90 | -58.04 | -99.90 | 8371 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T01:35 | Consensus | sell | DOGE-USD | 14.99 | -0.17 | target is flat |
| 2026-10-05T01:35 | Connors RSI(2) | buy | DOGE-USD | 14.64 | — | entry signal |
| 2026-10-05T01:35 | Three white soldiers | sell | XRP-USD | 22.54 | -0.16 | exit signal |
| 2026-10-05T01:35 | Candlestick reversal | sell | SOL-USD | 14.27 | -0.07 | exit signal |
| 2026-10-05T01:35 | Keltner breakout | sell | XRP-USD | 17.30 | -0.17 | exit signal |
| 2026-10-05T01:35 | Keltner breakout | sell | DOGE-USD | 17.28 | -0.20 | stop-loss |
| 2026-10-05T01:35 | Bollinger breakout | sell | DOGE-USD | 15.41 | -0.18 | stop-loss |
| 2026-10-05T01:35 | Donchian 20/10 | sell | DOGE-USD | 16.34 | -0.19 | stop-loss |
| 2026-10-05T01:35 | OBV trend | sell | DOGE-USD | 13.88 | -0.16 | stop-loss |
| 2026-10-05T01:35 | RSI momentum | sell | DOGE-USD | 15.97 | -0.18 | stop-loss |
| 2026-10-05T01:35 | ROC + volume | sell | DOGE-USD | 19.38 | -0.25 | stop-loss |
| 2026-10-05T01:35 | VWAP momentum | sell | XRP-USD | 11.26 | -0.05 | exit signal |
| 2026-10-05T01:35 | VWAP momentum | sell | SOL-USD | 8.34 | -0.07 | exit signal |
| 2026-10-05T01:35 | VWAP momentum | sell | ETH-USD | 14.04 | -0.10 | exit signal |
| 2026-10-05T01:35 | VWAP momentum | sell | DOGE-USD | 11.26 | -0.06 | exit signal |
| 2026-10-05T01:35 | Heikin-Ashi | sell | XRP-USD | 12.62 | -0.13 | exit signal |
| 2026-10-05T01:35 | Heikin-Ashi | sell | SOL-USD | 12.63 | -0.12 | exit signal |
| 2026-10-05T01:35 | Heikin-Ashi | sell | DOGE-USD | 12.60 | -0.17 | stop-loss |
| 2026-10-05T01:35 | Heikin-Ashi | sell | BTC-USD | 12.65 | -0.10 | exit signal |
| 2026-10-05T01:35 | Ichimoku | sell | ETH-USD | 16.98 | -0.15 | exit signal |
| 2026-10-05T01:35 | Ichimoku | sell | DOGE-USD | 16.97 | -0.20 | stop-loss |
| 2026-10-05T01:35 | ADX DI cross | sell | ETH-USD | 17.22 | -0.12 | exit signal |
| 2026-10-05T01:35 | ADX DI cross | sell | DOGE-USD | 17.19 | -0.13 | exit signal |
| 2026-10-05T01:35 | Parabolic SAR | sell | ETH-USD | 13.42 | -0.10 | exit signal |
| 2026-10-05T01:35 | Parabolic SAR | sell | DOGE-USD | 13.44 | -0.08 | exit signal |
| 2026-10-05T01:35 | MACD cross | buy | DOGE-USD | 2.64 | — | rebalance up |
| 2026-10-05T01:35 | MACD cross | sell | ETH-USD | 5.24 | -0.04 | exit signal |
| 2026-10-05T01:33 | AI bee: Boozy | sell | BTC-USD | 22.88 | -0.15 | Jev: buy |
| 2026-10-05T01:30 | AI bee: Bizzy | sell | XRP-USD | 12.23 | -0.07 | Jev: sell (sell p=0.56) after 10 min |
| 2026-10-05T01:30 | CCI reversion | sell | SOL-USD | 14.28 | -0.06 | exit signal |
| 2026-10-05T01:30 | Keltner breakout | buy | BTC-USD | 17.46 | — | entry signal |
| 2026-10-05T01:30 | Donchian 55/20 | buy | BTC-USD | 19.70 | — | entry signal |
| 2026-10-05T01:30 | ROC + volume | buy | BTC-USD | 19.60 | — | entry signal |
| 2026-10-05T01:30 | Ichimoku | buy | ETH-USD | 17.13 | — | entry signal |
| 2026-10-05T01:25 | ROC + volume | buy | XRP-USD | 19.62 | — | entry signal |
| 2026-10-05T01:25 | Heikin-Ashi | buy | XRP-USD | 12.75 | — | entry signal |
| 2026-10-05T01:25 | Heikin-Ashi | buy | SOL-USD | 12.75 | — | entry signal |
| 2026-10-05T01:25 | Heikin-Ashi | buy | BTC-USD | 12.75 | — | entry signal |
| 2026-10-05T01:20 | AI bee: Bizzy | buy | XRP-USD | 12.30 | — | Jev: buy (buy p=0.70) |
| 2026-10-05T01:20 | CCI reversion | sell | ETH-USD | 11.43 | -0.04 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
