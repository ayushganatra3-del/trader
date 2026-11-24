# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T14:40:05.000129+00:00 · 71925 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.69 (-21.31%)

Closed trades 241, win rate 35.7%, fees £6.52, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-24 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, BH 12%, FUN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-23)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.62 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.4, AAPL 4.1, TSLA 3.2, AMZN 1.1, GOOGL 0.8, META 0.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 12531 decisions in 2355 calls, $0.1732 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T14:40 | 2 / 14 / 14 | LABU 14% |  |
| Breezy | 2026-11-24T14:40 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-24T14:40 | 3 / 21 / 6 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| MFI reversion | SQQQ | 1.62 | +10.95% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 28.17 | 4.27 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.84 | 14.84 | 0 | — | 12.43 | 4.42 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.80 | 5.80 | 41 | 29.3 | 5.11 | 0.93 | -11.78 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.81 | 3.81 | 0 | — | 3.93 | 1.14 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.13 | -0.87 | 217 | 31.8 | 0.25 | 0.17 | -8.58 | 210 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.56 | -2.44 | 164 | 33.5 | -2.69 | -2.75 | -3.91 | 61 |
| 10 | Agent (rotation) | meta | 96.28 | -3.72 | 227 | 28.6 | -0.15 | 0.04 | -7.48 | 156 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 93.94 | -6.07 | 0 | — | -7.15 | -1.78 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.07 | -7.93 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.46 | -4.54 | -11.69 | 38 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.40 | -9.60 | 0 | — | -10.60 | -2.27 | -17.03 | 1 |
| 18 | Copy: Insider buying | copy | 90.00 | -10.00 | 58 | 39.7 | -8.98 | -1.74 | -14.79 | 70 |
| 19 | VWAP reversion · 1h | reversion | 87.29 | -12.71 | 163 | 46.0 | -10.27 | -1.89 | -20.49 | 153 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.70 | -2.99 | -20.94 | 1 |
| 21 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.39 | -14.39 | 542 |
| 22 | Daily: Bullish score | daily | 85.54 | -14.46 | 20 | 20.0 | -13.30 | -3.05 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -20.25 | -7.24 | -20.78 | 76 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.80 | -6.59 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 79.04 | -20.96 | 205 | 28.3 | -31.48 | -8.35 | -31.69 | 183 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -25.18 | -5.66 | -25.57 | 196 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -14.67 | -4.12 | -17.05 | 85 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -21.81 | -6.77 | -22.95 | 659 |
| 30 | Volume breakout · 1h | breakout | 76.53 | -23.47 | 169 | 27.8 | -23.98 | -7.39 | -24.15 | 72 |
| 31 | Donchian 55/20 · 1h | breakout | 75.98 | -24.02 | 87 | 13.8 | -30.15 | -8.03 | -30.15 | 84 |
| 32 | Keltner breakout · 1h | breakout | 75.62 | -24.38 | 137 | 24.8 | -26.09 | -6.91 | -26.51 | 146 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.99 | -31.19 | 102 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 70.06 | -29.94 | 3 | 0.0 | -23.26 | -2.75 | -32.18 | 1 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.86 | -4.86 | -36.53 | 24 |
| 36 | Hold BTC | benchmark | 69.73 | -30.27 | 3 | 0.0 | -28.75 | -5.13 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.53 | -30.47 | 253 | 19.0 | -39.76 | -7.37 | -39.77 | 277 |
| 38 | Supertrend · 1h | trend | 68.96 | -31.04 | 204 | 18.6 | -36.93 | -7.30 | -37.53 | 211 |
| 39 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -40.01 | -10.52 | -40.22 | 166 |
| 40 | EMA 20/50 cross · 1h | trend | 68.11 | -31.89 | 123 | 9.8 | -37.57 | -10.22 | -38.98 | 116 |
| 41 | Bollinger breakout · 1h | breakout | 67.60 | -32.40 | 208 | 22.1 | -33.73 | -8.91 | -34.68 | 211 |
| 42 | OBV trend · 1h | momentum | 66.64 | -33.36 | 323 | 19.8 | -39.60 | -10.14 | -40.68 | 231 |
| 43 | MACD zero-line · 1h | trend | 64.68 | -35.32 | 198 | 16.7 | -33.54 | -9.01 | -33.71 | 204 |
| 44 | Stochastic reversion · 1h | reversion | 64.33 | -35.67 | 397 | 40.6 | -34.35 | -3.72 | -42.64 | 432 |
| 45 | Heikin-Ashi · 1h | trend | 64.27 | -35.73 | 528 | 22.2 | -48.34 | -9.89 | -49.06 | 629 |
| 46 | RSI momentum · 1h | momentum | 64.17 | -35.83 | 200 | 15.0 | -41.70 | -9.71 | -41.70 | 195 |
| 47 | Max aggression: 5-day momentum | meta | 62.39 | -37.61 | 26 | 34.6 | -63.00 | -4.16 | -66.90 | 23 |
| 48 | ROC + volume · 1h | momentum | 61.57 | -38.43 | 452 | 27.0 | -43.28 | -8.71 | -43.45 | 341 |
| 49 | Donchian 20/10 · 1h | breakout | 60.97 | -39.03 | 181 | 17.7 | -41.41 | -8.88 | -42.92 | 193 |
| 50 | Max aggression: 1-day momentum | meta | 60.42 | -39.58 | 34 | 26.5 | -58.57 | -4.33 | -60.19 | 38 |
| 51 | MFI reversion · 1h | reversion | 60.04 | -39.96 | 489 | 32.7 | -33.01 | -4.94 | -35.63 | 185 |
| 52 | EMA 9/21 cross · 1h | trend | 59.51 | -40.49 | 307 | 12.4 | -44.37 | -10.47 | -45.92 | 334 |
| 53 | MACD cross · 1h | trend | 57.83 | -42.17 | 473 | 21.1 | -51.93 | -10.31 | -52.70 | 511 |
| 54 | Agent (ML meta-label) | meta | 57.79 | -42.21 | 2049 | 25.0 | -18.65 | -2.33 | -29.02 | 341 |
| 55 | CCI reversion · 1h | reversion | 56.43 | -43.57 | 436 | 39.4 | -50.50 | -8.49 | -51.93 | 505 |
| 56 | Bollinger reversion · 1h | reversion | 56.39 | -43.62 | 391 | 37.6 | -39.06 | -4.71 | -45.42 | 430 |
| 57 | VWAP momentum · 1h | momentum | 53.38 | -46.62 | 1059 | 21.7 | -57.79 | -13.21 | -58.56 | 1187 |
| 58 | Williams %R · 1h | reversion | 51.34 | -48.66 | 505 | 38.0 | -54.82 | -8.98 | -56.10 | 591 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.03 | -8.50 | -53.05 | 686 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.17 | -49.89 | -99.17 | 5400 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.09 | -33.96 | -84.23 | 1442 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.59 | -50.38 | -94.59 | 2451 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.69 | -32.43 | -90.70 | 1923 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.91 | -42.29 | -91.91 | 2259 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.73 | -28.64 | -89.79 | 1975 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -49.20 | -98.19 | 3434 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.99 | -55.16 | -96.99 | 3391 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -38.85 | -93.54 | 2109 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.53 | -35.43 | -83.53 | 1559 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.44 | -99.67 | 6264 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.27 | -39.14 | -93.27 | 2501 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.42 | -36.81 | -94.42 | 3167 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.39 | -99.82 | 6142 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.35 | -44.88 | -93.35 | 2281 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.72 | -22.33 | -51.75 | 640 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.75 | -23.76 | -78.75 | 1614 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -59.86 | -97.82 | 3297 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -61.85 | -99.17 | 5120 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.13 | -27.35 | -71.15 | 1198 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.02 | -48.65 | -95.03 | 2674 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.85 | -6.58 | -48.78 | 280 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.54 | -37.35 | -85.54 | 1669 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.19 | -99.76 | 6529 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.37 | -31.00 | -91.39 | 2469 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.81 | -20.15 | -82.85 | 1940 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.78 | -31.31 | -91.78 | 2171 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.10 | -49.48 | -98.11 | 4048 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.41 | -48.61 | -90.41 | 2202 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.65 | -29.49 | -68.65 | 798 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.56 | -28.41 | -73.56 | 1169 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.97 | -18.96 | -84.00 | 1816 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.99 | -49.87 | -97.99 | 4408 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -101.77 | -99.94 | 8267 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.01 | -6.99 | -51.00 | 307 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T14:40 | Agent (rotation) | buy | LABU | 8.02 | — | entry |
| 2026-11-24T14:40 | Day trade: Stocks in Play ORB | buy | TSLA | 24.40 | — | entry |
| 2026-11-24T14:40 | Day trade: Stocks in Play ORB | buy | TNA | 24.40 | — | entry |
| 2026-11-24T14:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 24.40 | — | entry |
| 2026-11-24T14:40 | Day trade: Stocks in Play ORB | buy | LABU | 24.40 | — | entry |
| 2026-11-24T14:40 | MFI reversion · 1h | buy | TSLA | 3.34 | — | entry |
| 2026-11-24T14:40 | MFI reversion · 1h | sell | SOXL | 5.56 | -1.65 | stop-loss |
| 2026-11-24T14:40 | CCI reversion · 1h | sell | MSTR | 2.47 | -0.21 | stop-loss |
| 2026-11-24T14:40 | Williams %R · 1h | sell | MSTR | 5.20 | -0.33 | stop-loss |
| 2026-11-24T14:40 | Heikin-Ashi · 1h | sell | SOXL | 4.73 | -0.23 | stop-loss |
| 2026-11-24T14:40 | MACD cross · 1h | sell | SOXL | 3.07 | -0.15 | stop-loss |
| 2026-11-24T14:40 | MACD cross · 1h | sell | MSTR | 4.31 | -0.37 | stop-loss |
| 2026-11-24T14:40 | Gap and go | buy | LABU | 24.79 | — | entry signal |
| 2026-11-24T14:35 | Max aggression: 5-day momentum | buy | SQQQ | 61.73 | — | entry |
| 2026-11-24T14:35 | Max aggression: 5-day momentum | sell | SOL-USD | 61.73 | -2.76 | target is flat |
| 2026-11-24T14:35 | Max aggression: 1-day momentum | buy | LABU | 59.16 | — | entry |
| 2026-11-24T14:35 | Agent (rotation) | buy | AAPL | 32.00 | — | entry |
| 2026-11-24T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 104.69 | — | entry |
| 2026-11-24T14:35 | Agent (ML meta-label) | buy | MSTR | 6.62 | — | entry |
| 2026-11-24T14:35 | Agent (ML meta-label) | sell | SQQQ | 4.24 | 0.25 | rebalance down |
| 2026-11-24T14:35 | Daily: Bullish score | buy | SQQQ | 21.33 | — | entry |
| 2026-11-24T14:35 | Daily: Connors RSI(2) · 3x ETFs | sell | UPRO | 83.13 | -1.95 | target is flat |
| 2026-11-24T14:35 | Daily: Momentum burst | sell | SQQQ | 17.95 | 0.60 | target is flat |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | TNA | 2.98 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | SOL-USD | 3.19 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | MSTR | 3.19 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | MSFT | 3.19 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | META | 3.19 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | IWM | 3.19 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | GOOGL | 3.19 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | ETH-USD | 3.19 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | DOGE-USD | 3.19 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | buy | BTC-USD | 3.19 | — | entry |
| 2026-11-24T14:35 | MFI reversion · 1h | sell | TQQQ | 3.47 | -0.29 | rebalance down |
| 2026-11-24T14:35 | MFI reversion · 1h | sell | SPY | 3.12 | -0.07 | rebalance down |
| 2026-11-24T14:35 | MFI reversion · 1h | sell | QQQ | 3.81 | -0.12 | rebalance down |
| 2026-11-24T14:35 | MFI reversion · 1h | sell | PLTR | 3.99 | -0.02 | rebalance down |
| 2026-11-24T14:35 | MFI reversion · 1h | sell | COIN | 3.72 | -0.16 | rebalance down |
| 2026-11-24T14:35 | MFI reversion · 1h | sell | BITX | 6.50 | -0.70 | stop-loss |
| 2026-11-24T14:35 | MFI reversion · 1h | sell | AMZN | 7.05 | -0.16 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 14:40:05.000129+00:00 -> 2026-11-24 14:50:05.000129+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
