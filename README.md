# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T20:40:05.000152+00:00 · 72229 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.44 (-21.56%)

Closed trades 244, win rate 36.1%, fees £6.57, max drawdown -22.02%.

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

Today: 40035 decisions in 3267 calls, $0.4948 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T20:40 | 6 / 18 / 6 | cash |  |
| Breezy | 2026-11-24T20:40 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-24T20:40 | 4 / 25 / 1 | COIN 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |
| Opening range 30m | SQQQ | 1.57 | +20.80% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.26 | 15.26 | 0 | — | 13.38 | 4.55 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.16 | 4.16 | 0 | — | 4.71 | 1.31 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.12 | 0.05 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.18 | -3.82 | 229 | 28.4 | -2.02 | -0.62 | -7.73 | 159 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.72 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.39 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.03 | -5.96 | 0 | — | -6.51 | -1.66 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.81 | -6.19 | 20 | 10.0 | -4.83 | -7.97 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.42 | -7.58 | 0 | — | -8.12 | -1.65 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 91.92 | -8.08 | 61 | 41.0 | -7.28 | -1.35 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.36 | -8.64 | 116 | 24.1 | -7.66 | -3.88 | -10.85 | 40 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.37 | -9.63 | 28 | 17.9 | -9.80 | -7.49 | -10.06 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.29 | -10.71 | 0 | — | -11.65 | -2.52 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.48 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.17 | -13.83 | 167 | 46.1 | -11.31 | -2.06 | -20.49 | 155 |
| 21 | Daily: Bullish score | daily | 85.62 | -14.38 | 20 | 20.0 | -12.86 | -2.83 | -19.56 | 14 |
| 22 | Opening range 30m | breakout | 85.03 | -14.97 | 469 | 32.8 | -13.11 | -4.40 | -13.73 | 543 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.17 | -7.39 | -21.55 | 75 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.53 | -6.46 | -14.68 | 65 |
| 26 | Parabolic SAR · 1h | trend | 78.62 | -21.38 | 206 | 28.2 | -32.35 | -8.50 | -32.72 | 184 |
| 27 | Agent | meta | 78.44 | -21.56 | 244 | 36.1 | -26.25 | -5.97 | -26.53 | 196 |
| 28 | Volume breakout · 1h | breakout | 78.20 | -21.80 | 169 | 27.8 | -22.47 | -6.84 | -24.10 | 73 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 76.65 | -23.35 | 138 | 24.6 | -24.96 | -6.50 | -27.01 | 150 |
| 31 | Opening range 15m | breakout | 76.34 | -23.66 | 585 | 30.4 | -22.24 | -6.87 | -22.57 | 670 |
| 32 | Donchian 55/20 · 1h | breakout | 76.19 | -23.80 | 87 | 13.8 | -29.38 | -7.88 | -29.68 | 82 |
| 33 | Ichimoku · 1h | trend | 74.62 | -25.38 | 113 | 15.9 | -29.65 | -7.62 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.39 | -29.61 | 260 | 19.2 | -37.44 | -7.12 | -38.61 | 292 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.80 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.08 | -30.92 | 208 | 22.1 | -31.48 | -8.26 | -33.57 | 209 |
| 37 | Hold BTC | benchmark | 68.76 | -31.24 | 3 | 0.0 | -29.80 | -5.28 | -36.10 | 1 |
| 38 | Supertrend · 1h | trend | 68.49 | -31.51 | 207 | 18.4 | -37.44 | -7.40 | -38.92 | 210 |
| 39 | Triple EMA stack · 1h | trend | 68.22 | -31.78 | 169 | 15.4 | -39.39 | -10.17 | -39.54 | 173 |
| 40 | EMA 20/50 cross · 1h | trend | 67.74 | -32.26 | 124 | 9.7 | -38.00 | -10.20 | -39.04 | 111 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 67.58 | -32.42 | 3 | 0.0 | -26.21 | -3.27 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 66.64 | -33.36 | 323 | 19.8 | -39.79 | -10.02 | -40.94 | 229 |
| 43 | RSI momentum · 1h | momentum | 65.29 | -34.71 | 200 | 15.0 | -40.93 | -9.49 | -42.36 | 197 |
| 44 | Heikin-Ashi · 1h | trend | 64.53 | -35.48 | 542 | 22.0 | -48.19 | -9.81 | -49.69 | 627 |
| 45 | MACD zero-line · 1h | trend | 64.35 | -35.65 | 199 | 16.6 | -34.25 | -9.31 | -34.73 | 198 |
| 46 | Max aggression: 1-day momentum | meta | 63.46 | -36.54 | 34 | 26.5 | -56.42 | -4.20 | -60.68 | 38 |
| 47 | Stochastic reversion · 1h | reversion | 63.15 | -36.85 | 400 | 40.5 | -35.43 | -3.85 | -42.69 | 432 |
| 48 | ROC + volume · 1h | momentum | 62.72 | -37.28 | 456 | 27.0 | -42.51 | -8.35 | -43.85 | 342 |
| 49 | Max aggression: 5-day momentum | meta | 62.63 | -37.37 | 26 | 34.6 | -62.81 | -4.14 | -67.33 | 23 |
| 50 | Donchian 20/10 · 1h | breakout | 62.06 | -37.94 | 181 | 17.7 | -39.95 | -8.58 | -42.49 | 194 |
| 51 | EMA 9/21 cross · 1h | trend | 59.99 | -40.01 | 310 | 12.3 | -44.21 | -10.47 | -45.66 | 330 |
| 52 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -34.05 | -5.14 | -35.70 | 186 |
| 53 | MACD cross · 1h | trend | 57.91 | -42.09 | 478 | 20.9 | -53.28 | -10.86 | -54.42 | 501 |
| 54 | Agent (ML meta-label) | meta | 56.68 | -43.32 | 2068 | 25.2 | -24.91 | -3.27 | -33.45 | 328 |
| 55 | CCI reversion · 1h | reversion | 55.79 | -44.21 | 444 | 39.4 | -51.98 | -8.89 | -52.62 | 493 |
| 56 | Bollinger reversion · 1h | reversion | 55.42 | -44.58 | 392 | 37.5 | -39.79 | -4.80 | -45.42 | 424 |
| 57 | VWAP momentum · 1h | momentum | 53.24 | -46.76 | 1075 | 21.5 | -58.50 | -13.16 | -59.87 | 1178 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.90 | -8.50 | -52.98 | 687 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.15 | -8.98 | -56.43 | 595 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -49.69 | -99.16 | 5353 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.77 | -33.60 | -83.79 | 1414 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.48 | -51.00 | -94.49 | 2436 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.75 | -32.43 | -90.76 | 1900 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.80 | -42.40 | -91.82 | 2236 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.68 | -28.93 | -89.82 | 1965 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -49.71 | -98.18 | 3438 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.91 | -55.94 | -96.91 | 3325 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.02 | -37.33 | -93.03 | 2073 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.18 | -36.37 | -83.18 | 1543 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -57.28 | -99.68 | 6275 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.20 | -39.59 | -93.21 | 2497 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.37 | -36.93 | -94.38 | 3174 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.86 | -99.82 | 6110 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.18 | -44.83 | -93.23 | 2260 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.52 | -22.25 | -51.57 | 640 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.27 | -23.80 | -78.35 | 1610 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -59.94 | -97.77 | 3283 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -61.68 | -99.18 | 5144 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.31 | -27.85 | -71.45 | 1208 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.88 | -49.10 | -94.89 | 2672 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -47.03 | -6.61 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.08 | -36.98 | -85.31 | 1661 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.09 | -99.77 | 6541 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -31.53 | -91.73 | 2471 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.85 | -20.33 | -83.21 | 1947 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.84 | -31.73 | -91.89 | 2170 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.17 | -49.96 | -98.17 | 4071 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.33 | -47.81 | -90.34 | 2202 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.54 | -29.98 | -68.54 | 794 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.30 | -28.57 | -73.30 | 1162 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.16 | -19.36 | -84.31 | 1815 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -50.59 | -98.06 | 4424 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -107.07 | -99.94 | 8258 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.92 | -7.39 | -50.46 | 306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T20:40 | Agent (ML meta-label) | buy | COIN | 14.17 | — | entry |
| 2026-11-24T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 90.60 | — | entry |
| 2026-11-24T20:30 | ROC + volume · 1h | buy | LABU | 5.08 | — | rebalance up |
| 2026-11-24T20:30 | ROC + volume · 1h | buy | IWM | 5.24 | — | rebalance up |
| 2026-11-24T20:30 | ROC + volume · 1h | buy | AAPL | 5.25 | — | rebalance up |
| 2026-11-24T20:30 | ROC + volume · 1h | sell | TSLA | 10.44 | -0.17 | exit signal |
| 2026-11-24T20:30 | ROC + volume · 1h | sell | SPY | 10.40 | -0.05 | exit signal |
| 2026-11-24T20:30 | ROC + volume · 1h | sell | NVDA | 10.38 | -0.09 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | buy | TSLA | 7.06 | — | rebalance up |
| 2026-11-24T20:30 | VWAP momentum · 1h | buy | TNA | 7.10 | — | rebalance up |
| 2026-11-24T20:30 | VWAP momentum · 1h | buy | LABU | 7.10 | — | rebalance up |
| 2026-11-24T20:30 | VWAP momentum · 1h | buy | IWM | 7.07 | — | rebalance up |
| 2026-11-24T20:30 | VWAP momentum · 1h | buy | AMD | 7.11 | — | rebalance up |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | UPRO | 3.54 | -0.05 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | TQQQ | 3.53 | -0.07 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | TECL | 3.52 | -0.08 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | SPY | 3.58 | -0.02 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | SOXL | 3.42 | -0.18 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | QQQ | 3.57 | -0.03 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | PLTR | 3.55 | -0.05 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | META | 3.56 | -0.04 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | GOOGL | 3.58 | -0.02 | exit signal |
| 2026-11-24T20:30 | VWAP momentum · 1h | sell | AAPL | 3.59 | 0.01 | exit signal |
| 2026-11-24T20:30 | Heikin-Ashi · 1h | buy | TNA | 5.43 | — | rebalance up |
| 2026-11-24T20:30 | Heikin-Ashi · 1h | buy | LABU | 5.41 | — | rebalance up |
| 2026-11-24T20:30 | Heikin-Ashi · 1h | buy | IWM | 5.34 | — | rebalance up |
| 2026-11-24T20:30 | Heikin-Ashi · 1h | sell | TSLA | 10.78 | -0.07 | exit signal |
| 2026-11-24T20:30 | Heikin-Ashi · 1h | sell | PLTR | 10.71 | -0.06 | exit signal |
| 2026-11-24T20:30 | Heikin-Ashi · 1h | sell | AAPL | 10.83 | -0.05 | exit signal |
| 2026-11-24T20:30 | Supertrend · 1h | sell | MSTR | 2.64 | -0.39 | exit signal |
| 2026-11-24T20:30 | Supertrend · 1h | sell | COIN | 2.79 | -0.24 | exit signal |
| 2026-11-24T20:30 | MACD zero-line · 1h | buy | IWM | 16.08 | — | entry signal |
| 2026-11-24T20:30 | MACD cross · 1h | buy | META | 3.29 | — | rebalance up |
| 2026-11-24T20:30 | MACD cross · 1h | buy | GOOGL | 3.22 | — | rebalance up |
| 2026-11-24T20:30 | MACD cross · 1h | sell | AMZN | 2.50 | -0.07 | exit signal |
| 2026-11-24T20:30 | Triple EMA stack · 1h | buy | TSLA | 17.06 | — | entry signal |
| 2026-11-24T20:20 | Agent (ML meta-label) | sell | TQQQ | 2.98 | -0.02 | selected signal exited |
| 2026-11-24T20:20 | Agent (ML meta-label) | sell | MSFT | 14.14 | -0.00 | selected signal exited |
| 2026-11-24T20:15 | Agent (ML meta-label) | buy | TQQQ | 3.01 | — | entry |
| 2026-11-24T20:15 | Agent (ML meta-label) | sell | SQQQ | 3.01 | -0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 20:40:05.000152+00:00 -> 2026-11-24 20:50:05.000152+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
