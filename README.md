# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T04:35:05.000243+00:00 · 12064 ticks

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

Today: 3585 decisions in 717 calls, $0.0503 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T04:35 | 0 / 1 / 4 | SOL-USD 15%, AMZN 18%, COIN 18%, MSTR 17% |  |
| Breezy | 2026-10-05T04:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T04:35 | 1 / 4 / 0 | MSTR 66% |  |

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
| 1 | Hold BTC | benchmark | 102.62 | 2.62 | 0 | — | 33.78 | 4.08 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.52 | 2.52 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.40 | 2.40 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | Copy: Congress Democrats (NANC) | copy | 101.28 | 1.28 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 5 | VWAP reversion · 1h | reversion | 101.28 | 1.28 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 101.20 | 1.20 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 101.20 | 1.20 | 53 | 37.7 | -24.24 | -5.46 | -26.54 | 496 |
| 8 | RSI(14) reversion · 1h | reversion | 100.70 | 0.70 | 11 | 63.6 | 3.62 | 1.05 | -6.57 | 120 |
| 9 | Hold SPY | benchmark | 100.43 | 0.43 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Bollinger reversion · 1h | reversion | 100.07 | 0.07 | 41 | 43.9 | -14.80 | -3.91 | -17.52 | 304 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 100.03 | 0.03 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 12 | Z-score reversion · 1h | reversion | 100.02 | 0.02 | 20 | 55.0 | 5.72 | 1.30 | -8.60 | 159 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Donchian 55/20 · 1h | breakout | 99.99 | -0.01 | 17 | 0.0 | 6.03 | 0.96 | -16.96 | 116 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.95 | -0.06 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 18 | Daily: Bullish score | daily | 99.80 | -0.20 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Stochastic reversion · 1h | reversion | 99.25 | -0.75 | 45 | 60.0 | -8.07 | -1.65 | -9.82 | 327 |
| 20 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 21 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 22 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 23 | CCI reversion · 1h | reversion | 99.22 | -0.78 | 63 | 49.2 | 1.92 | 0.47 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 99.11 | -0.89 | 50 | 22.0 | -21.11 | -5.35 | -25.34 | 156 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 99.06 | -0.94 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | EMA 20/50 cross · 1h | trend | 98.11 | -1.89 | 25 | 8.0 | 13.38 | 1.67 | -14.40 | 137 |
| 30 | Daily: SMA 20/50 cross · AAPL | daily | 98.09 | -1.91 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 31 | Agent (rotation) | meta | 97.99 | -2.01 | 52 | 23.1 | -5.00 | -1.92 | -9.49 | 227 |
| 32 | Williams %R · 1h | reversion | 97.79 | -2.21 | 70 | 54.3 | -17.14 | -3.13 | -19.41 | 495 |
| 33 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 34 | Connors RSI(2) · 1h | reversion | 97.55 | -2.45 | 60 | 43.3 | -12.22 | -4.10 | -14.21 | 223 |
| 35 | Daily: Momentum burst | daily | 97.06 | -2.94 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.97 | -3.04 | 208 | 17.3 | -1.55 | -0.12 | -12.05 | 347 |
| 37 | Parabolic SAR · 1h | trend | 96.65 | -3.35 | 51 | 17.6 | -5.67 | -0.63 | -19.70 | 305 |
| 38 | Max aggression: 1-day momentum | meta | 96.44 | -3.56 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 39 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 40 | Supertrend · 1h | trend | 96.19 | -3.81 | 28 | 7.1 | 3.30 | 0.62 | -16.43 | 202 |
| 41 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.44 | -16.99 | 119 |
| 42 | Copy: Insider buying | copy | 96.14 | -3.86 | 6 | 50.0 | -18.81 | -3.69 | -21.08 | 73 |
| 43 | MACD cross · 1h | trend | 96.06 | -3.94 | 72 | 16.7 | -11.82 | -1.84 | -17.27 | 472 |
| 44 | ADX DI cross · 1h | trend | 95.99 | -4.01 | 41 | 12.2 | -4.78 | -0.64 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.52 | -4.49 | 26 | 19.2 | 20.30 | 2.90 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.54 | -5.46 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 94.26 | -5.74 | 41 | 2.4 | 1.50 | 0.39 | -16.65 | 231 |
| 49 | Bollinger breakout · 1h | breakout | 93.48 | -6.52 | 43 | 25.6 | 6.56 | 1.02 | -12.06 | 296 |
| 50 | Triple EMA stack · 1h | trend | 93.43 | -6.57 | 50 | 8.0 | -7.88 | -0.76 | -23.88 | 244 |
| 51 | VWAP momentum · 1h | momentum | 93.38 | -6.62 | 182 | 23.1 | -38.72 | -6.04 | -39.36 | 1277 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.79 | -7.21 | 30 | 6.7 | 2.82 | 0.58 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 92.03 | -7.97 | 69 | 11.6 | -3.11 | -0.23 | -18.47 | 340 |
| 55 | Max aggression: 5-day momentum | meta | 91.59 | -8.41 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | MACD zero-line · 1h | trend | 91.14 | -8.86 | 39 | 15.4 | -3.25 | -0.21 | -18.32 | 236 |
| 57 | Donchian 20/10 · 1h | breakout | 91.06 | -8.94 | 32 | 15.6 | -0.25 | 0.18 | -16.18 | 224 |
| 58 | Three white soldiers | momentum | 90.65 | -9.35 | 78 | 14.1 | -49.69 | -26.13 | -50.01 | 594 |
| 59 | Heikin-Ashi · 1h | trend | 90.64 | -9.36 | 98 | 25.5 | -32.08 | -5.60 | -33.92 | 686 |
| 60 | OBV trend · 1h | momentum | 89.75 | -10.25 | 97 | 11.3 | -12.93 | -1.42 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.41 | -11.59 | 27 | 7.4 | -11.28 | -1.33 | -23.22 | 217 |
| 62 | ROC + volume · 1h | momentum | 87.27 | -12.73 | 90 | 15.6 | -10.10 | -1.24 | -23.17 | 419 |
| 63 | RSI(14) reversion | reversion | 86.37 | -13.63 | 185 | 33.5 | -70.45 | -19.67 | -70.53 | 1419 |
| 64 | VWAP reversion | reversion | 78.75 | -21.25 | 217 | 28.1 | -70.19 | -17.13 | -70.19 | 1371 |
| 65 | Donchian 55/20 | breakout | 78.44 | -21.56 | 204 | 16.7 | -68.82 | -15.44 | -69.12 | 1316 |
| 66 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.04 | -18.66 | -63.10 | 1234 |
| 67 | ROC + volume | momentum | 77.90 | -22.10 | 270 | 19.3 | -73.43 | -17.50 | -74.19 | 1666 |
| 68 | EMA 20/50 cross | trend | 77.45 | -22.55 | 224 | 18.3 | -79.07 | -16.61 | -79.07 | 1488 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.38 | -19.76 | -64.38 | 914 |
| 70 | Z-score reversion | reversion | 75.30 | -24.70 | 296 | 28.7 | -84.75 | -25.49 | -84.83 | 2077 |
| 71 | MFI reversion | reversion | 72.92 | -27.08 | 296 | 20.6 | -87.68 | -32.06 | -87.72 | 2112 |
| 72 | Supertrend | trend | 72.22 | -27.78 | 304 | 20.1 | -87.44 | -23.22 | -87.46 | 1952 |
| 73 | AI bee: Bizzy | ai | 69.75 | -30.25 | 517 | 7.9 | — | — | — | — |
| 74 | Keltner breakout | breakout | 69.38 | -30.62 | 301 | 11.6 | -85.79 | -31.73 | -85.81 | 1912 |
| 75 | ADX DI cross | trend | 68.74 | -31.26 | 328 | 9.5 | -89.60 | -39.14 | -89.62 | 2110 |
| 76 | Ichimoku | trend | 67.98 | -32.02 | 275 | 8.0 | -82.69 | -25.46 | -82.87 | 1800 |
| 77 | AI bee: Boozy | ai | 67.26 | -32.74 | 201 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.01 | -33.99 | 382 | 14.9 | -92.04 | -32.59 | -92.05 | 2385 |
| 79 | Donchian 20/10 | breakout | 65.60 | -34.40 | 403 | 17.1 | -91.21 | -27.79 | -91.34 | 2697 |
| 80 | RSI momentum | momentum | 63.94 | -36.06 | 386 | 14.2 | -90.99 | -28.13 | -90.99 | 2415 |
| 81 | Triple EMA stack | trend | 62.79 | -37.21 | 437 | 14.4 | -93.71 | -34.55 | -93.71 | 2670 |
| 82 | Trend pullback | trend | 62.31 | -37.69 | 407 | 14.0 | -91.71 | -33.19 | -91.71 | 2375 |
| 83 | Bollinger breakout | breakout | 61.90 | -38.10 | 418 | 13.6 | -94.19 | -37.60 | -94.22 | 2869 |
| 84 | Stochastic reversion | reversion | 61.83 | -38.17 | 592 | 22.6 | -95.68 | -39.79 | -95.71 | 4056 |
| 85 | Bollinger reversion | reversion | 61.22 | -38.78 | 553 | 16.5 | -95.69 | -38.61 | -95.69 | 3694 |
| 86 | Consensus | meta | 59.96 | -40.04 | 390 | 8.5 | -94.42 | -27.75 | -94.42 | 2643 |
| 87 | EMA 9/21 cross | trend | 58.24 | -41.76 | 545 | 16.1 | -97.57 | -37.68 | -97.58 | 3589 |
| 88 | Connors RSI(2) | reversion | 57.52 | -42.48 | 521 | 15.5 | -96.66 | -37.82 | -96.66 | 3668 |
| 89 | CCI reversion | reversion | 56.33 | -43.67 | 555 | 15.1 | -98.46 | -42.84 | -98.46 | 4715 |
| 90 | Candlestick reversal | reversion | 55.81 | -44.19 | 659 | 14.6 | -99.30 | -42.44 | -99.30 | 5629 |
| 91 | VWAP momentum | momentum | 55.29 | -44.71 | 617 | 8.9 | -98.69 | -33.79 | -98.69 | 5347 |
| 92 | OBV trend | momentum | 54.94 | -45.06 | 613 | 13.9 | -96.49 | -43.75 | -96.51 | 3674 |
| 93 | Parabolic SAR | trend | 53.26 | -46.74 | 560 | 12.7 | -97.43 | -45.95 | -97.43 | 3718 |
| 94 | MACD cross | trend | 51.51 | -48.49 | 638 | 12.7 | -99.73 | -51.32 | -99.73 | 6203 |
| 95 | Williams %R | reversion | 50.77 | -49.23 | 698 | 19.2 | -99.51 | -47.70 | -99.51 | 6146 |
| 96 | Heikin-Ashi | trend | 50.07 | -49.93 | 600 | 8.3 | -99.90 | -58.31 | -99.90 | 8362 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T04:35 | Keltner breakout · 1h | sell | DOGE-USD | 5.79 | -0.10 | stop-loss |
| 2026-10-05T04:35 | MFI reversion | sell | DOGE-USD | 18.06 | -0.28 | stop-loss |
| 2026-10-05T04:35 | Williams %R | buy | SOL-USD | 5.03 | — | rebalance up |
| 2026-10-05T04:35 | Williams %R | sell | XRP-USD | 12.67 | -0.16 | stop-loss |
| 2026-10-05T04:35 | Williams %R | sell | ETH-USD | 10.15 | -0.10 | stop-loss |
| 2026-10-05T04:35 | Williams %R | sell | DOGE-USD | 10.10 | -0.15 | stop-loss |
| 2026-10-05T04:35 | Williams %R | sell | BTC-USD | 10.16 | -0.10 | stop-loss |
| 2026-10-05T04:35 | Stochastic reversion | sell | XRP-USD | 12.35 | -0.15 | stop-loss |
| 2026-10-05T04:35 | Stochastic reversion | sell | ETH-USD | 15.46 | -0.17 | stop-loss |
| 2026-10-05T04:35 | Stochastic reversion | sell | DOGE-USD | 15.36 | -0.24 | stop-loss |
| 2026-10-05T04:35 | Stochastic reversion | sell | BTC-USD | 6.21 | -0.06 | stop-loss |
| 2026-10-05T04:35 | VWAP reversion | sell | ETH-USD | 19.57 | -0.21 | stop-loss |
| 2026-10-05T04:35 | Z-score reversion | sell | XRP-USD | 18.74 | -0.23 | stop-loss |
| 2026-10-05T04:35 | Z-score reversion | sell | DOGE-USD | 18.67 | -0.28 | stop-loss |
| 2026-10-05T04:35 | Bollinger reversion | sell | ETH-USD | 15.31 | -0.16 | stop-loss |
| 2026-10-05T04:35 | Bollinger reversion | sell | DOGE-USD | 15.24 | -0.24 | stop-loss |
| 2026-10-05T04:35 | Bollinger reversion | sell | BTC-USD | 15.25 | -0.16 | stop-loss |
| 2026-10-05T04:35 | Connors RSI(2) | sell | BTC-USD | 14.31 | -0.15 | stop-loss |
| 2026-10-05T04:35 | RSI(14) reversion | sell | XRP-USD | 21.48 | -0.24 | stop-loss |
| 2026-10-05T04:35 | RSI(14) reversion | sell | ETH-USD | 21.51 | -0.22 | stop-loss |
| 2026-10-05T04:35 | Candlestick reversal | sell | BTC-USD | 13.87 | -0.13 | stop-loss |
| 2026-10-05T04:30 | MFI reversion | buy | ETH-USD | 18.30 | — | entry signal |
| 2026-10-05T04:30 | CCI reversion | buy | SOL-USD | 14.10 | — | entry signal |
| 2026-10-05T04:30 | Connors RSI(2) | sell | XRP-USD | 14.40 | -0.14 | stop-loss |
| 2026-10-05T04:30 | Candlestick reversal | sell | XRP-USD | 13.91 | -0.12 | exit signal |
| 2026-10-05T04:27 | AI bee: Bizzy | buy | SOL-USD | 10.45 | — | Jev: buy (buy p=0.60) |
| 2026-10-05T04:25 | Williams %R | buy | SOL-USD | 7.73 | — | entry signal |
| 2026-10-05T04:25 | Williams %R | buy | ETH-USD | 10.25 | — | entry signal |
| 2026-10-05T04:25 | Williams %R | buy | DOGE-USD | 10.25 | — | entry signal |
| 2026-10-05T04:25 | Williams %R | buy | BTC-USD | 10.25 | — | entry signal |
| 2026-10-05T04:25 | VWAP reversion | buy | SOL-USD | 19.74 | — | entry signal |
| 2026-10-05T04:25 | Z-score reversion | buy | SOL-USD | 18.95 | — | entry signal |
| 2026-10-05T04:25 | Z-score reversion | buy | DOGE-USD | 18.95 | — | entry signal |
| 2026-10-05T04:25 | Connors RSI(2) | sell | DOGE-USD | 14.39 | -0.10 | exit signal |
| 2026-10-05T04:25 | RSI(14) reversion | buy | XRP-USD | 21.73 | — | entry signal |
| 2026-10-05T04:25 | RSI(14) reversion | buy | SOL-USD | 21.73 | — | entry signal |
| 2026-10-05T04:25 | RSI(14) reversion | buy | ETH-USD | 21.73 | — | entry signal |
| 2026-10-05T04:25 | Candlestick reversal | buy | BTC-USD | 14.00 | — | entry signal |
| 2026-10-05T04:20 | ROC + volume · 1h | sell | XRP-USD | 6.22 | -0.00 | stop-loss |
| 2026-10-05T04:20 | ROC + volume · 1h | sell | ETH-USD | 6.17 | -0.07 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 04:35:05.000243+00:00 -> 2026-10-05 04:45:05.000243+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
