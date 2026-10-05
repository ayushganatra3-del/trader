# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T02:05:05.000146+00:00 · 11933 ticks

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

Today: 1620 decisions in 324 calls, $0.0228 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T02:05 | 2 / 3 / 0 | AMZN 18%, COIN 17%, MSTR 17% |  |
| Breezy | 2026-10-05T02:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T02:05 | 2 / 3 / 0 | MSTR 66% |  |

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
| 1 | Hold BTC | benchmark | 103.58 | 3.58 | 0 | — | 35.58 | 4.27 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.19 | 2.19 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.06 | 2.06 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.04 | 1.04 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.95 | 0.95 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.87 | 0.87 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.87 | 0.87 | 53 | 37.7 | -24.29 | -5.49 | -26.60 | 496 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 4.10 | 1.18 | -6.57 | 119 |
| 9 | Hold SPY | benchmark | 100.11 | 0.11 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.82 | -3.92 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.78 | -0.22 | 20 | 55.0 | 6.18 | 1.40 | -8.60 | 158 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.70 | -0.30 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.34 | 1.00 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.62 | -0.38 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.47 | -0.53 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.03 | -0.97 | 45 | 60.0 | -8.07 | -1.65 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.92 | 0.48 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 49 | 22.4 | -21.72 | -5.52 | -25.34 | 158 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -4.27 | -1.61 | -9.74 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.79 | -2.21 | 25 | 8.0 | 13.90 | 1.72 | -14.40 | 137 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.77 | -2.23 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.50 | -2.50 | 60 | 43.3 | -11.84 | -3.96 | -14.21 | 220 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.53 | 70 | 54.3 | -17.14 | -3.13 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.71 | -3.29 | 207 | 17.4 | -0.66 | 0.03 | -12.05 | 367 |
| 37 | Parabolic SAR · 1h | trend | 96.57 | -3.43 | 49 | 16.3 | -5.39 | -0.59 | -19.70 | 305 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.44 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.13 | -3.87 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 41 | MACD cross · 1h | trend | 96.05 | -3.95 | 72 | 16.7 | -11.97 | -1.86 | -17.27 | 476 |
| 42 | Supertrend · 1h | trend | 96.05 | -3.95 | 28 | 7.1 | 3.60 | 0.66 | -16.43 | 202 |
| 43 | Copy: Insider buying | copy | 95.83 | -4.17 | 6 | 50.0 | -18.81 | -3.69 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.68 | -4.32 | 41 | 12.2 | -4.65 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.50 | -4.50 | 24 | 16.7 | 20.71 | 2.95 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.25 | -5.75 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 93.99 | -6.01 | 40 | 2.5 | 2.06 | 0.47 | -16.65 | 231 |
| 49 | Bollinger breakout · 1h | breakout | 93.36 | -6.64 | 40 | 20.0 | 6.77 | 1.05 | -12.06 | 296 |
| 50 | VWAP momentum · 1h | momentum | 93.35 | -6.65 | 181 | 23.2 | -38.54 | -6.00 | -39.36 | 1276 |
| 51 | Triple EMA stack · 1h | trend | 93.15 | -6.85 | 50 | 8.0 | -7.95 | -0.76 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.49 | -7.51 | 30 | 6.7 | 3.20 | 0.63 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 91.85 | -8.15 | 69 | 11.6 | -3.03 | -0.22 | -18.47 | 339 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 91.11 | -8.89 | 31 | 12.9 | 0.13 | 0.23 | -16.18 | 224 |
| 57 | MACD zero-line · 1h | trend | 91.00 | -9.00 | 39 | 15.4 | -2.84 | -0.16 | -18.32 | 236 |
| 58 | Heikin-Ashi · 1h | trend | 90.87 | -9.13 | 96 | 25.0 | -31.74 | -5.52 | -33.92 | 686 |
| 59 | Three white soldiers | momentum | 90.65 | -9.35 | 78 | 14.1 | -49.69 | -26.13 | -50.01 | 594 |
| 60 | OBV trend · 1h | momentum | 89.46 | -10.54 | 97 | 11.3 | -12.42 | -1.35 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.35 | -11.65 | 23 | 4.3 | -10.99 | -1.28 | -23.19 | 217 |
| 62 | ROC + volume · 1h | momentum | 87.26 | -12.74 | 87 | 14.9 | -9.85 | -1.21 | -23.16 | 419 |
| 63 | RSI(14) reversion | reversion | 86.92 | -13.08 | 183 | 33.9 | -70.47 | -19.68 | -70.54 | 1425 |
| 64 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -70.04 | -17.00 | -70.04 | 1370 |
| 65 | Donchian 55/20 | breakout | 78.44 | -21.56 | 204 | 16.7 | -68.82 | -15.44 | -69.12 | 1316 |
| 66 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.04 | -18.66 | -63.10 | 1234 |
| 67 | ROC + volume | momentum | 77.90 | -22.10 | 270 | 19.3 | -73.43 | -17.50 | -74.19 | 1666 |
| 68 | EMA 20/50 cross | trend | 77.69 | -22.31 | 221 | 17.6 | -78.95 | -16.51 | -79.05 | 1488 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.67 | -19.90 | -64.67 | 918 |
| 70 | Z-score reversion | reversion | 75.89 | -24.11 | 294 | 28.9 | -84.78 | -25.52 | -84.81 | 2081 |
| 71 | MFI reversion | reversion | 73.57 | -26.43 | 294 | 20.7 | -87.56 | -31.61 | -87.61 | 2108 |
| 72 | Supertrend | trend | 72.44 | -27.56 | 300 | 19.7 | -87.49 | -23.19 | -87.53 | 1956 |
| 73 | AI bee: Bizzy | ai | 70.05 | -29.95 | 513 | 8.0 | — | — | — | — |
| 74 | Keltner breakout | breakout | 69.38 | -30.62 | 301 | 11.6 | -85.91 | -32.08 | -85.93 | 1916 |
| 75 | ADX DI cross | trend | 69.06 | -30.94 | 325 | 9.5 | -89.53 | -38.66 | -89.55 | 2107 |
| 76 | Ichimoku | trend | 67.98 | -32.02 | 275 | 8.0 | -82.68 | -25.45 | -82.87 | 1799 |
| 77 | AI bee: Boozy | ai | 67.45 | -32.55 | 200 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.14 | -33.86 | 381 | 15.0 | -92.04 | -32.49 | -92.05 | 2385 |
| 79 | Donchian 20/10 | breakout | 65.67 | -34.33 | 402 | 17.2 | -91.30 | -28.07 | -91.34 | 2702 |
| 80 | RSI momentum | momentum | 64.38 | -35.62 | 382 | 14.4 | -90.94 | -27.95 | -90.95 | 2414 |
| 81 | Triple EMA stack | trend | 63.08 | -36.92 | 433 | 14.5 | -93.67 | -34.32 | -93.68 | 2669 |
| 82 | Stochastic reversion | reversion | 62.84 | -37.16 | 583 | 23.0 | -95.62 | -38.90 | -95.65 | 4054 |
| 83 | Trend pullback | trend | 62.79 | -37.21 | 401 | 14.2 | -91.82 | -33.37 | -91.82 | 2384 |
| 84 | Bollinger reversion | reversion | 62.38 | -37.62 | 546 | 16.7 | -95.60 | -37.74 | -95.61 | 3687 |
| 85 | Bollinger breakout | breakout | 61.90 | -38.10 | 418 | 13.6 | -94.25 | -37.80 | -94.29 | 2874 |
| 86 | Consensus | meta | 60.49 | -39.51 | 384 | 8.6 | -94.36 | -27.50 | -94.36 | 2640 |
| 87 | EMA 9/21 cross | trend | 58.64 | -41.36 | 540 | 16.3 | -97.58 | -37.39 | -97.59 | 3593 |
| 88 | Connors RSI(2) | reversion | 58.47 | -41.53 | 510 | 15.9 | -96.63 | -37.36 | -96.63 | 3663 |
| 89 | Candlestick reversal | reversion | 57.24 | -42.76 | 645 | 14.9 | -99.30 | -41.74 | -99.30 | 5633 |
| 90 | CCI reversion | reversion | 57.08 | -42.92 | 550 | 15.3 | -98.44 | -42.28 | -98.45 | 4712 |
| 91 | VWAP momentum | momentum | 56.07 | -43.93 | 608 | 9.0 | -98.69 | -33.59 | -98.69 | 5347 |
| 92 | OBV trend | momentum | 55.66 | -44.34 | 605 | 14.0 | -96.46 | -43.16 | -96.47 | 3671 |
| 93 | Parabolic SAR | trend | 53.77 | -46.23 | 555 | 12.8 | -97.42 | -45.28 | -97.42 | 3716 |
| 94 | MACD cross | trend | 51.89 | -48.11 | 634 | 12.8 | -99.73 | -50.85 | -99.73 | 6202 |
| 95 | Williams %R | reversion | 51.74 | -48.26 | 687 | 19.5 | -99.50 | -46.79 | -99.50 | 6144 |
| 96 | Heikin-Ashi | trend | 50.53 | -49.47 | 595 | 8.4 | -99.90 | -57.96 | -99.90 | 8367 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T02:05 | Consensus | buy | ETH-USD | 15.13 | — | entry |
| 2026-10-05T02:05 | Williams %R | buy | XRP-USD | 12.96 | — | entry signal |
| 2026-10-05T02:05 | Williams %R | buy | DOGE-USD | 12.96 | — | entry signal |
| 2026-10-05T02:05 | Stochastic reversion | buy | XRP-USD | 15.72 | — | entry signal |
| 2026-10-05T02:05 | Connors RSI(2) | sell | DOGE-USD | 14.58 | -0.06 | exit signal |
| 2026-10-05T02:05 | OBV trend | buy | XRP-USD | 13.94 | — | entry signal |
| 2026-10-05T02:05 | OBV trend | buy | ETH-USD | 13.94 | — | entry signal |
| 2026-10-05T02:05 | VWAP momentum | buy | ETH-USD | 14.04 | — | entry signal |
| 2026-10-05T02:05 | VWAP momentum | buy | DOGE-USD | 14.04 | — | entry signal |
| 2026-10-05T02:05 | Trend pullback | buy | ETH-USD | 15.72 | — | entry signal |
| 2026-10-05T02:05 | Trend pullback | buy | DOGE-USD | 15.73 | — | entry signal |
| 2026-10-05T02:05 | Trend pullback | buy | BTC-USD | 15.73 | — | entry signal |
| 2026-10-05T02:05 | MACD cross | buy | SOL-USD | 12.98 | — | entry signal |
| 2026-10-05T02:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.52 | 0.01 | exit signal |
| 2026-10-05T02:00 | VWAP momentum · 1h | sell | BTC-USD | 15.68 | 0.18 | exit signal |
| 2026-10-05T02:00 | Williams %R | buy | SOL-USD | 12.97 | — | entry signal |
| 2026-10-05T02:00 | Williams %R | buy | ETH-USD | 12.97 | — | entry signal |
| 2026-10-05T02:00 | Stochastic reversion | buy | SOL-USD | 15.74 | — | entry signal |
| 2026-10-05T02:00 | Stochastic reversion | buy | ETH-USD | 15.74 | — | entry signal |
| 2026-10-05T01:55 | Consensus | sell | ETH-USD | 15.13 | -0.11 | target is flat |
| 2026-10-05T01:55 | Connors RSI(2) | buy | BTC-USD | 14.63 | — | entry signal |
| 2026-10-05T01:55 | Keltner breakout | sell | BTC-USD | 17.28 | -0.17 | stop-loss |
| 2026-10-05T01:55 | Bollinger breakout | sell | XRP-USD | 15.40 | -0.17 | stop-loss |
| 2026-10-05T01:55 | Bollinger breakout | sell | BTC-USD | 15.47 | -0.12 | stop-loss |
| 2026-10-05T01:55 | Donchian 55/20 | sell | XRP-USD | 19.50 | -0.22 | stop-loss |
| 2026-10-05T01:55 | Donchian 55/20 | sell | BTC-USD | 19.50 | -0.20 | stop-loss |
| 2026-10-05T01:55 | Donchian 20/10 | sell | XRP-USD | 16.33 | -0.18 | stop-loss |
| 2026-10-05T01:55 | OBV trend | sell | XRP-USD | 13.95 | -0.12 | exit signal |
| 2026-10-05T01:55 | OBV trend | sell | ETH-USD | 13.92 | -0.12 | exit signal |
| 2026-10-05T01:55 | ROC + volume | sell | BTC-USD | 19.40 | -0.20 | stop-loss |
| 2026-10-05T01:55 | VWAP momentum | sell | BTC-USD | 11.25 | -0.07 | exit signal |
| 2026-10-05T01:55 | Trend pullback | sell | ETH-USD | 15.66 | -0.12 | exit signal |
| 2026-10-05T01:55 | Ichimoku | sell | XRP-USD | 16.97 | -0.19 | stop-loss |
| 2026-10-05T01:55 | Ichimoku | sell | BTC-USD | 17.02 | -0.14 | exit signal |
| 2026-10-05T01:55 | MACD cross | sell | BTC-USD | 12.98 | -0.09 | exit signal |
| 2026-10-05T01:55 | Triple EMA stack | sell | ETH-USD | 15.70 | -0.13 | exit signal |
| 2026-10-05T01:55 | EMA 9/21 cross | sell | ETH-USD | 14.59 | -0.12 | exit signal |
| 2026-10-05T01:50 | Candlestick reversal | buy | SOL-USD | 14.31 | — | entry signal |
| 2026-10-05T01:50 | ROC + volume | sell | XRP-USD | 19.43 | -0.18 | exit signal |
| 2026-10-05T01:45 | MFI reversion | sell | SOL-USD | 18.28 | -0.15 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 02:05:05.000146+00:00 -> 2026-10-05 02:15:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
