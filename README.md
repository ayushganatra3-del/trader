# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T00:35:05.000169+00:00 · 11858 ticks

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

Today: 495 decisions in 99 calls, $0.0070 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T00:35 | 0 / 3 / 2 | AMZN 18%, COIN 17%, MSTR 17% |  |
| Breezy | 2026-10-05T00:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T00:35 | 1 / 3 / 1 | MSTR 66% |  |

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
| 1 | Hold BTC | benchmark | 103.06 | 3.06 | 0 | — | 35.07 | 4.22 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.16 | 2.17 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.04 | 2.04 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.02 | 1.02 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.93 | 0.93 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.85 | 0.85 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.85 | 0.85 | 53 | 37.7 | -21.67 | -4.91 | -24.07 | 484 |
| 8 | RSI(14) reversion · 1h | reversion | 100.61 | 0.61 | 11 | 63.6 | 4.95 | 1.41 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.08 | 0.08 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.89 | -0.11 | 41 | 43.9 | -14.80 | -3.91 | -17.52 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.76 | -0.24 | 20 | 55.0 | 6.18 | 1.40 | -8.60 | 158 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.68 | -0.32 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.64 | -0.36 | 17 | 0.0 | 6.24 | 0.99 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.59 | -0.41 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.45 | -0.56 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.01 | -0.99 | 45 | 60.0 | -8.07 | -1.65 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.87 | -1.13 | 63 | 49.2 | 1.92 | 0.48 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 98.79 | -1.21 | 49 | 22.4 | -21.98 | -5.60 | -25.34 | 159 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.71 | -1.29 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -4.27 | -1.61 | -9.74 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.77 | -2.23 | 25 | 8.0 | 14.01 | 1.73 | -14.40 | 136 |
| 31 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 32 | Daily: SMA 20/50 cross · AAPL | daily | 97.75 | -2.25 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 33 | Connors RSI(2) · 1h | reversion | 97.48 | -2.52 | 60 | 43.3 | -11.84 | -3.96 | -14.21 | 220 |
| 34 | Williams %R · 1h | reversion | 97.45 | -2.55 | 70 | 54.3 | -17.12 | -3.13 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.98 | -3.02 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.70 | -3.30 | 206 | 17.5 | 0.29 | 0.20 | -12.52 | 362 |
| 37 | Parabolic SAR · 1h | trend | 96.46 | -3.54 | 49 | 16.3 | -5.48 | -0.60 | -19.70 | 305 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.44 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.10 | -3.90 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 95.97 | -4.03 | 28 | 7.1 | 3.49 | 0.65 | -16.43 | 202 |
| 42 | MACD cross · 1h | trend | 95.91 | -4.09 | 72 | 16.7 | -11.47 | -1.78 | -17.27 | 474 |
| 43 | Copy: Insider buying | copy | 95.81 | -4.19 | 6 | 50.0 | -18.81 | -3.69 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.65 | -4.35 | 41 | 12.2 | -4.68 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.36 | -4.64 | 24 | 16.7 | 20.53 | 2.93 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.23 | -5.77 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 93.96 | -6.04 | 40 | 2.5 | 1.87 | 0.44 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.30 | -6.70 | 179 | 22.3 | -38.74 | -6.04 | -39.45 | 1278 |
| 50 | Bollinger breakout · 1h | breakout | 93.26 | -6.74 | 40 | 20.0 | 6.67 | 1.04 | -12.06 | 296 |
| 51 | Triple EMA stack · 1h | trend | 93.12 | -6.88 | 50 | 8.0 | -8.10 | -0.78 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.47 | -7.53 | 30 | 6.7 | 3.05 | 0.61 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 91.79 | -8.21 | 69 | 11.6 | -3.14 | -0.23 | -18.47 | 339 |
| 55 | Max aggression: 5-day momentum | meta | 91.27 | -8.73 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 90.97 | -9.03 | 31 | 12.9 | -0.00 | 0.21 | -16.18 | 224 |
| 57 | MACD zero-line · 1h | trend | 90.92 | -9.08 | 39 | 15.4 | -2.96 | -0.17 | -18.32 | 236 |
| 58 | Three white soldiers | momentum | 90.81 | -9.19 | 77 | 14.3 | -49.60 | -25.94 | -49.92 | 593 |
| 59 | Heikin-Ashi · 1h | trend | 90.63 | -9.37 | 96 | 25.0 | -31.91 | -5.56 | -33.92 | 686 |
| 60 | OBV trend · 1h | momentum | 89.44 | -10.56 | 97 | 11.3 | -12.53 | -1.36 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.28 | -11.72 | 23 | 4.3 | -11.04 | -1.29 | -23.19 | 216 |
| 62 | ROC + volume · 1h | momentum | 87.17 | -12.83 | 87 | 14.9 | -10.23 | -1.26 | -23.16 | 420 |
| 63 | RSI(14) reversion | reversion | 86.92 | -13.08 | 183 | 33.9 | -70.42 | -19.63 | -70.48 | 1422 |
| 64 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.63 | -16.79 | -69.63 | 1358 |
| 65 | Donchian 55/20 | breakout | 78.85 | -21.15 | 202 | 16.8 | -68.66 | -15.34 | -68.96 | 1314 |
| 66 | ROC + volume | momentum | 78.54 | -21.46 | 267 | 19.5 | -73.28 | -17.40 | -73.98 | 1664 |
| 67 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.02 | -18.66 | -63.09 | 1234 |
| 68 | EMA 20/50 cross | trend | 77.59 | -22.41 | 221 | 17.6 | -78.96 | -16.52 | -79.03 | 1487 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.67 | -19.90 | -64.67 | 918 |
| 70 | Z-score reversion | reversion | 75.89 | -24.11 | 294 | 28.9 | -84.78 | -25.52 | -84.81 | 2081 |
| 71 | MFI reversion | reversion | 73.72 | -26.28 | 293 | 20.8 | -87.55 | -31.51 | -87.61 | 2108 |
| 72 | Supertrend | trend | 72.50 | -27.50 | 300 | 19.7 | -87.40 | -23.10 | -87.43 | 1951 |
| 73 | AI bee: Bizzy | ai | 70.26 | -29.75 | 510 | 8.0 | — | — | — | — |
| 74 | Keltner breakout | breakout | 69.93 | -30.07 | 298 | 11.7 | -85.84 | -31.76 | -85.86 | 1914 |
| 75 | ADX DI cross | trend | 69.37 | -30.62 | 323 | 9.6 | -89.56 | -38.70 | -89.58 | 2108 |
| 76 | Ichimoku | trend | 68.65 | -31.35 | 271 | 8.1 | -82.59 | -25.24 | -82.70 | 1797 |
| 77 | AI bee: Boozy | ai | 67.68 | -32.32 | 198 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.26 | -33.73 | 380 | 15.0 | -92.01 | -32.41 | -92.02 | 2383 |
| 79 | Donchian 20/10 | breakout | 66.11 | -33.89 | 400 | 17.2 | -91.28 | -27.99 | -91.32 | 2701 |
| 80 | RSI momentum | momentum | 64.66 | -35.34 | 381 | 14.4 | -90.98 | -27.89 | -90.98 | 2415 |
| 81 | Triple EMA stack | trend | 63.35 | -36.65 | 432 | 14.6 | -93.73 | -34.11 | -93.73 | 2673 |
| 82 | Trend pullback | trend | 63.02 | -36.98 | 399 | 14.3 | -91.81 | -33.21 | -91.81 | 2381 |
| 83 | Stochastic reversion | reversion | 62.94 | -37.06 | 578 | 23.2 | -95.62 | -38.83 | -95.65 | 4051 |
| 84 | Bollinger reversion | reversion | 62.48 | -37.52 | 541 | 16.8 | -95.61 | -37.74 | -95.61 | 3689 |
| 85 | Bollinger breakout | breakout | 62.37 | -37.63 | 415 | 13.7 | -94.21 | -37.34 | -94.24 | 2871 |
| 86 | Consensus | meta | 60.64 | -39.36 | 382 | 8.6 | -94.35 | -27.20 | -94.35 | 2637 |
| 87 | EMA 9/21 cross | trend | 58.89 | -41.11 | 539 | 16.3 | -97.56 | -37.18 | -97.57 | 3588 |
| 88 | Connors RSI(2) | reversion | 58.57 | -41.43 | 509 | 15.9 | -96.64 | -37.42 | -96.64 | 3664 |
| 89 | Candlestick reversal | reversion | 57.32 | -42.68 | 642 | 14.8 | -99.29 | -41.64 | -99.29 | 5627 |
| 90 | CCI reversion | reversion | 57.09 | -42.91 | 545 | 15.4 | -98.45 | -42.35 | -98.45 | 4714 |
| 91 | VWAP momentum | momentum | 56.60 | -43.40 | 602 | 9.1 | -98.68 | -33.35 | -98.68 | 5338 |
| 92 | OBV trend | momentum | 56.29 | -43.71 | 601 | 14.1 | -96.48 | -42.51 | -96.50 | 3673 |
| 93 | Parabolic SAR | trend | 54.05 | -45.95 | 551 | 12.9 | -97.41 | -44.88 | -97.41 | 3713 |
| 94 | MACD cross | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -50.18 | -99.73 | 6202 |
| 95 | Williams %R | reversion | 51.87 | -48.13 | 682 | 19.6 | -99.50 | -46.58 | -99.50 | 6138 |
| 96 | Heikin-Ashi | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -56.64 | -99.90 | 8368 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T00:35 | Stochastic reversion | buy | SOL-USD | 3.25 | — | entry signal |
| 2026-10-05T00:35 | Stochastic reversion | buy | BTC-USD | 12.60 | — | entry signal |
| 2026-10-05T00:35 | Bollinger reversion | buy | XRP-USD | 15.64 | — | entry signal |
| 2026-10-05T00:35 | Bollinger reversion | buy | ETH-USD | 15.64 | — | entry signal |
| 2026-10-05T00:35 | Candlestick reversal | buy | SOL-USD | 14.34 | — | entry signal |
| 2026-10-05T00:35 | EMA 9/21 cross | sell | BTC-USD | 11.81 | 0.05 | exit signal |
| 2026-10-05T00:30 | Consensus | sell | XRP-USD | 15.09 | -0.16 | target is flat |
| 2026-10-05T00:30 | CCI reversion | sell | SOL-USD | 14.20 | -0.16 | stop-loss |
| 2026-10-05T00:30 | Williams %R | buy | BTC-USD | 7.76 | — | rebalance up |
| 2026-10-05T00:30 | Williams %R | sell | SOL-USD | 10.35 | -0.12 | stop-loss |
| 2026-10-05T00:30 | Bollinger reversion | sell | SOL-USD | 15.53 | -0.18 | stop-loss |
| 2026-10-05T00:30 | Donchian 55/20 | sell | XRP-USD | 19.02 | -0.07 | exit signal |
| 2026-10-05T00:30 | Donchian 55/20 | sell | ETH-USD | 15.82 | -0.08 | exit signal |
| 2026-10-05T00:30 | Donchian 55/20 | sell | BTC-USD | 15.85 | 0.03 | exit signal |
| 2026-10-05T00:30 | Donchian 20/10 | sell | ETH-USD | 13.26 | -0.06 | exit signal |
| 2026-10-05T00:30 | Donchian 20/10 | sell | BTC-USD | 13.29 | 0.02 | exit signal |
| 2026-10-05T00:30 | RSI momentum | sell | XRP-USD | 12.95 | -0.04 | exit signal |
| 2026-10-05T00:30 | RSI momentum | sell | ETH-USD | 12.97 | -0.06 | exit signal |
| 2026-10-05T00:30 | RSI momentum | sell | BTC-USD | 13.02 | 0.04 | exit signal |
| 2026-10-05T00:30 | VWAP momentum | sell | DOGE-USD | 14.07 | -0.14 | exit signal |
| 2026-10-05T00:30 | Trend pullback | sell | XRP-USD | 15.69 | -0.16 | stop-loss |
| 2026-10-05T00:30 | Trend pullback | sell | ETH-USD | 15.71 | -0.14 | exit signal |
| 2026-10-05T00:30 | Supertrend | sell | XRP-USD | 18.11 | -0.04 | exit signal |
| 2026-10-05T00:30 | Triple EMA stack | sell | XRP-USD | 12.67 | -0.01 | exit signal |
| 2026-10-05T00:30 | Triple EMA stack | sell | ETH-USD | 12.68 | -0.00 | exit signal |
| 2026-10-05T00:30 | Triple EMA stack | sell | BTC-USD | 12.71 | 0.06 | exit signal |
| 2026-10-05T00:30 | EMA 9/21 cross | sell | XRP-USD | 11.78 | -0.01 | exit signal |
| 2026-10-05T00:30 | EMA 9/21 cross | sell | ETH-USD | 11.78 | -0.00 | exit signal |
| 2026-10-05T00:25 | Candlestick reversal | sell | SOL-USD | 14.27 | -0.12 | exit signal |
| 2026-10-05T00:25 | Candlestick reversal | sell | DOGE-USD | 14.29 | -0.10 | exit signal |
| 2026-10-05T00:25 | OBV trend | sell | ETH-USD | 13.99 | -0.12 | exit signal |
| 2026-10-05T00:25 | VWAP momentum | sell | ETH-USD | 14.10 | -0.12 | exit signal |
| 2026-10-05T00:25 | ADX DI cross | sell | XRP-USD | 17.25 | -0.12 | exit signal |
| 2026-10-05T00:25 | EMA 20/50 cross | sell | DOGE-USD | 19.83 | 0.44 | exit signal |
| 2026-10-05T00:20 | Williams %R | buy | BTC-USD | 5.25 | — | entry signal |
| 2026-10-05T00:20 | Williams %R | sell | SOL-USD | 2.60 | -0.02 | rebalance down |
| 2026-10-05T00:20 | Williams %R | sell | ETH-USD | 2.61 | -0.01 | rebalance down |
| 2026-10-05T00:20 | Connors RSI(2) | sell | XRP-USD | 14.62 | -0.06 | exit signal |
| 2026-10-05T00:20 | Connors RSI(2) | sell | ETH-USD | 14.63 | -0.05 | exit signal |
| 2026-10-05T00:20 | Connors RSI(2) | sell | BTC-USD | 14.60 | -0.07 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
