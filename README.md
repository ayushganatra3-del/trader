# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T04:05:05.000147+00:00 · 12035 ticks

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

Today: 3150 decisions in 630 calls, $0.0442 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T04:05 | 0 / 0 / 5 | AMZN 18%, COIN 18%, MSTR 17% |  |
| Breezy | 2026-10-05T04:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T04:05 | 0 / 4 / 1 | MSTR 66% |  |

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
| 1 | Hold BTC | benchmark | 103.20 | 3.20 | 0 | — | 34.33 | 4.14 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.52 | 2.52 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.39 | 2.39 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.28 | 1.28 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.28 | 1.28 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 101.20 | 1.20 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 101.20 | 1.20 | 53 | 37.7 | -24.20 | -5.45 | -26.51 | 496 |
| 8 | RSI(14) reversion · 1h | reversion | 100.70 | 0.70 | 11 | 63.6 | 3.62 | 1.05 | -6.57 | 120 |
| 9 | Hold SPY | benchmark | 100.43 | 0.43 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Bollinger reversion · 1h | reversion | 100.07 | 0.07 | 41 | 43.9 | -14.80 | -3.91 | -17.52 | 304 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 100.02 | 0.02 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 12 | Z-score reversion · 1h | reversion | 100.02 | 0.02 | 20 | 55.0 | 5.72 | 1.30 | -8.60 | 159 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Donchian 55/20 · 1h | breakout | 99.99 | -0.01 | 17 | 0.0 | 6.18 | 0.98 | -16.96 | 116 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.94 | -0.06 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 18 | Daily: Bullish score | daily | 99.79 | -0.21 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Stochastic reversion · 1h | reversion | 99.24 | -0.76 | 45 | 60.0 | -8.07 | -1.65 | -9.82 | 327 |
| 21 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 22 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 23 | CCI reversion · 1h | reversion | 99.21 | -0.79 | 63 | 49.2 | 1.88 | 0.47 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 99.11 | -0.90 | 50 | 22.0 | -21.11 | -5.35 | -25.34 | 156 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 99.05 | -0.95 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | EMA 20/50 cross · 1h | trend | 98.11 | -1.89 | 25 | 8.0 | 13.56 | 1.69 | -14.40 | 137 |
| 30 | Daily: SMA 20/50 cross · AAPL | daily | 98.09 | -1.91 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 31 | Agent (rotation) | meta | 97.99 | -2.01 | 52 | 23.1 | -5.00 | -1.92 | -9.49 | 227 |
| 32 | Williams %R · 1h | reversion | 97.79 | -2.21 | 70 | 54.3 | -17.14 | -3.13 | -19.41 | 495 |
| 33 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 34 | Connors RSI(2) · 1h | reversion | 97.66 | -2.34 | 60 | 43.3 | -12.02 | -4.03 | -14.21 | 223 |
| 35 | Daily: Momentum burst | daily | 97.06 | -2.94 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.96 | -3.04 | 208 | 17.3 | -0.12 | 0.14 | -12.12 | 354 |
| 37 | Parabolic SAR · 1h | trend | 96.71 | -3.29 | 51 | 17.6 | -5.60 | -0.62 | -19.70 | 305 |
| 38 | Max aggression: 1-day momentum | meta | 96.44 | -3.56 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 39 | Supertrend · 1h | trend | 96.25 | -3.75 | 28 | 7.1 | 3.43 | 0.64 | -16.43 | 202 |
| 40 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 41 | MACD cross · 1h | trend | 96.20 | -3.80 | 72 | 16.7 | -11.69 | -1.82 | -17.27 | 472 |
| 42 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.44 | -16.99 | 119 |
| 43 | Copy: Insider buying | copy | 96.13 | -3.87 | 6 | 50.0 | -18.81 | -3.69 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.99 | -4.01 | 41 | 12.2 | -4.78 | -0.64 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.51 | -4.49 | 26 | 19.2 | 20.30 | 2.90 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.54 | -5.46 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 94.27 | -5.73 | 41 | 2.4 | 1.63 | 0.41 | -16.65 | 231 |
| 49 | Bollinger breakout · 1h | breakout | 93.48 | -6.52 | 43 | 25.6 | 6.56 | 1.02 | -12.06 | 296 |
| 50 | Triple EMA stack · 1h | trend | 93.43 | -6.57 | 50 | 8.0 | -7.74 | -0.74 | -23.88 | 244 |
| 51 | VWAP momentum · 1h | momentum | 93.38 | -6.62 | 182 | 23.1 | -38.72 | -6.04 | -39.35 | 1277 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.79 | -7.21 | 30 | 6.7 | 2.91 | 0.59 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 92.07 | -7.93 | 69 | 11.6 | -2.99 | -0.21 | -18.47 | 340 |
| 55 | Max aggression: 5-day momentum | meta | 91.59 | -8.41 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | MACD zero-line · 1h | trend | 91.21 | -8.79 | 39 | 15.4 | -3.05 | -0.19 | -18.32 | 236 |
| 57 | Donchian 20/10 · 1h | breakout | 91.19 | -8.81 | 32 | 15.6 | -0.10 | 0.20 | -16.18 | 224 |
| 58 | Three white soldiers | momentum | 90.65 | -9.35 | 78 | 14.1 | -49.69 | -26.13 | -50.01 | 594 |
| 59 | Heikin-Ashi · 1h | trend | 90.64 | -9.36 | 98 | 25.5 | -32.08 | -5.60 | -33.92 | 686 |
| 60 | OBV trend · 1h | momentum | 89.75 | -10.25 | 97 | 11.3 | -12.78 | -1.40 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.48 | -11.52 | 26 | 7.7 | -11.19 | -1.31 | -23.19 | 217 |
| 62 | ROC + volume · 1h | momentum | 87.33 | -12.67 | 88 | 15.9 | -10.02 | -1.23 | -23.16 | 419 |
| 63 | RSI(14) reversion | reversion | 86.92 | -13.08 | 183 | 33.9 | -70.48 | -19.68 | -70.55 | 1423 |
| 64 | VWAP reversion | reversion | 79.12 | -20.88 | 215 | 28.4 | -69.86 | -16.94 | -69.86 | 1366 |
| 65 | Donchian 55/20 | breakout | 78.44 | -21.56 | 204 | 16.7 | -68.82 | -15.44 | -69.12 | 1316 |
| 66 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.00 | -18.60 | -63.10 | 1233 |
| 67 | ROC + volume | momentum | 77.90 | -22.10 | 270 | 19.3 | -73.43 | -17.50 | -74.19 | 1666 |
| 68 | EMA 20/50 cross | trend | 77.45 | -22.55 | 224 | 18.3 | -79.02 | -16.58 | -79.03 | 1487 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.38 | -19.76 | -64.38 | 914 |
| 70 | Z-score reversion | reversion | 75.89 | -24.11 | 294 | 28.9 | -84.63 | -25.21 | -84.72 | 2074 |
| 71 | MFI reversion | reversion | 73.37 | -26.63 | 295 | 20.7 | -87.60 | -31.76 | -87.64 | 2109 |
| 72 | Supertrend | trend | 72.22 | -27.78 | 304 | 20.1 | -87.44 | -23.22 | -87.46 | 1952 |
| 73 | AI bee: Bizzy | ai | 69.80 | -30.20 | 517 | 7.9 | — | — | — | — |
| 74 | Keltner breakout | breakout | 69.38 | -30.62 | 301 | 11.6 | -85.79 | -31.73 | -85.81 | 1912 |
| 75 | ADX DI cross | trend | 68.74 | -31.26 | 328 | 9.5 | -89.58 | -39.00 | -89.60 | 2108 |
| 76 | Ichimoku | trend | 67.98 | -32.02 | 275 | 8.0 | -82.68 | -25.45 | -82.87 | 1799 |
| 77 | AI bee: Boozy | ai | 67.26 | -32.74 | 201 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.01 | -33.99 | 382 | 14.9 | -92.04 | -32.59 | -92.05 | 2385 |
| 79 | Donchian 20/10 | breakout | 65.60 | -34.40 | 403 | 17.1 | -91.21 | -27.79 | -91.34 | 2697 |
| 80 | RSI momentum | momentum | 63.94 | -36.06 | 386 | 14.2 | -90.99 | -28.13 | -90.99 | 2415 |
| 81 | Triple EMA stack | trend | 62.79 | -37.21 | 437 | 14.4 | -93.70 | -34.55 | -93.70 | 2670 |
| 82 | Stochastic reversion | reversion | 62.48 | -37.52 | 588 | 22.8 | -95.63 | -39.26 | -95.67 | 4052 |
| 83 | Trend pullback | trend | 62.31 | -37.69 | 407 | 14.0 | -91.78 | -33.48 | -91.78 | 2380 |
| 84 | Bollinger breakout | breakout | 61.90 | -38.10 | 418 | 13.6 | -94.19 | -37.60 | -94.23 | 2869 |
| 85 | Bollinger reversion | reversion | 61.89 | -38.11 | 548 | 16.6 | -95.63 | -38.16 | -95.64 | 3691 |
| 86 | Consensus | meta | 59.96 | -40.04 | 390 | 8.5 | -94.42 | -27.75 | -94.42 | 2643 |
| 87 | EMA 9/21 cross | trend | 58.24 | -41.76 | 545 | 16.1 | -97.58 | -37.70 | -97.59 | 3591 |
| 88 | Connors RSI(2) | reversion | 57.87 | -42.13 | 516 | 15.7 | -96.65 | -37.57 | -96.65 | 3668 |
| 89 | CCI reversion | reversion | 56.40 | -43.60 | 555 | 15.1 | -98.46 | -42.86 | -98.46 | 4715 |
| 90 | Candlestick reversal | reversion | 56.11 | -43.89 | 657 | 14.6 | -99.31 | -42.64 | -99.31 | 5642 |
| 91 | VWAP momentum | momentum | 55.29 | -44.71 | 617 | 8.9 | -98.69 | -33.80 | -98.69 | 5346 |
| 92 | OBV trend | momentum | 54.94 | -45.06 | 613 | 13.9 | -96.49 | -43.75 | -96.51 | 3674 |
| 93 | Parabolic SAR | trend | 53.26 | -46.74 | 560 | 12.7 | -97.43 | -45.95 | -97.43 | 3718 |
| 94 | MACD cross | trend | 51.51 | -48.49 | 638 | 12.7 | -99.73 | -51.32 | -99.73 | 6203 |
| 95 | Williams %R | reversion | 51.32 | -48.68 | 694 | 19.3 | -99.50 | -47.20 | -99.50 | 6141 |
| 96 | Heikin-Ashi | trend | 50.07 | -49.93 | 600 | 8.3 | -99.90 | -58.31 | -99.90 | 8362 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T04:05 | Agent (ML meta-label) | sell | DOGE-USD | 4.38 | -0.03 | selected signal exited |
| 2026-10-05T04:05 | CCI reversion | sell | XRP-USD | 14.07 | -0.15 | stop-loss |
| 2026-10-05T04:05 | CCI reversion | sell | DOGE-USD | 14.11 | -0.15 | stop-loss |
| 2026-10-05T04:05 | Bollinger reversion | sell | XRP-USD | 15.43 | -0.16 | stop-loss |
| 2026-10-05T04:05 | Bollinger reversion | sell | ETH-USD | 15.43 | -0.15 | stop-loss |
| 2026-10-05T04:00 | Agent (ML meta-label) | buy | DOGE-USD | 4.41 | — | following Stochastic reversion · 1h |
| 2026-10-05T04:00 | Consensus | sell | ETH-USD | 14.89 | -0.14 | target is flat |
| 2026-10-05T04:00 | Connors RSI(2) · 1h | buy | SOL-USD | 4.43 | — | entry signal |
| 2026-10-05T04:00 | Connors RSI(2) · 1h | buy | BTC-USD | 19.55 | — | entry signal |
| 2026-10-05T04:00 | Squeeze breakout · 1h | sell | ETH-USD | 23.75 | -0.06 | stop-loss |
| 2026-10-05T04:00 | Keltner breakout · 1h | sell | ETH-USD | 5.85 | -0.05 | stop-loss |
| 2026-10-05T04:00 | Bollinger breakout · 1h | sell | ETH-USD | 7.20 | 0.04 | stop-loss |
| 2026-10-05T04:00 | Donchian 20/10 · 1h | sell | SOL-USD | 5.67 | 0.00 | exit signal |
| 2026-10-05T04:00 | RSI momentum · 1h | buy | BTC-USD | 1.79 | — | entry |
| 2026-10-05T04:00 | RSI momentum · 1h | sell | SOL-USD | 1.79 | -0.00 | exit signal |
| 2026-10-05T04:00 | ROC + volume · 1h | sell | BTC-USD | 6.71 | 0.00 | stop-loss |
| 2026-10-05T04:00 | VWAP momentum · 1h | sell | ETH-USD | 23.01 | -0.20 | exit signal |
| 2026-10-05T04:00 | Trend pullback · 1h | sell | SOL-USD | 3.24 | -0.06 | exit signal |
| 2026-10-05T04:00 | Heikin-Ashi · 1h | sell | XRP-USD | 21.98 | -0.17 | exit signal |
| 2026-10-05T04:00 | Heikin-Ashi · 1h | sell | BTC-USD | 22.70 | 0.00 | exit signal |
| 2026-10-05T04:00 | Parabolic SAR · 1h | sell | SOL-USD | 1.41 | -0.02 | stop-loss |
| 2026-10-05T04:00 | Parabolic SAR · 1h | sell | BTC-USD | 7.49 | 0.07 | exit signal |
| 2026-10-05T04:00 | MFI reversion | sell | SOL-USD | 18.19 | -0.21 | stop-loss |
| 2026-10-05T04:00 | CCI reversion | sell | ETH-USD | 14.09 | -0.15 | stop-loss |
| 2026-10-05T04:00 | Williams %R | sell | ETH-USD | 12.75 | -0.12 | stop-loss |
| 2026-10-05T04:00 | Stochastic reversion | buy | XRP-USD | 15.65 | — | entry signal |
| 2026-10-05T04:00 | Stochastic reversion | sell | BTC-USD | 15.59 | -0.11 | stop-loss |
| 2026-10-05T04:00 | Connors RSI(2) | buy | DOGE-USD | 14.49 | — | entry signal |
| 2026-10-05T04:00 | Candlestick reversal | sell | SOL-USD | 14.01 | -0.14 | stop-loss |
| 2026-10-05T04:00 | Candlestick reversal | sell | DOGE-USD | 11.28 | -0.11 | stop-loss |
| 2026-10-05T04:00 | EMA 20/50 cross | sell | ETH-USD | 19.45 | 0.05 | exit signal |
| 2026-10-05T04:00 | EMA 20/50 cross | sell | DOGE-USD | 19.29 | -0.15 | stop-loss |
| 2026-10-05T03:55 | Keltner breakout · 1h | sell | XRP-USD | 3.46 | -0.02 | stop-loss |
| 2026-10-05T03:55 | Bollinger breakout · 1h | sell | XRP-USD | 6.25 | 0.05 | stop-loss |
| 2026-10-05T03:55 | Candlestick reversal | sell | ETH-USD | 11.25 | -0.09 | exit signal |
| 2026-10-05T03:55 | Candlestick reversal | sell | BTC-USD | 14.05 | -0.10 | exit signal |
| 2026-10-05T03:55 | OBV trend | sell | DOGE-USD | 13.65 | -0.13 | exit signal |
| 2026-10-05T03:50 | VWAP reversion | buy | SOL-USD | 19.81 | — | entry signal |
| 2026-10-05T03:50 | Bollinger reversion | buy | SOL-USD | 15.58 | — | entry signal |
| 2026-10-05T03:50 | Bollinger reversion | buy | ETH-USD | 15.58 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 04:05:05.000147+00:00 -> 2026-10-05 04:15:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
