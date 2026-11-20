# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T16:50:05.000125+00:00 · 67076 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £80.18 (-19.82%)

Closed trades 238, win rate 36.1%, fees £6.46, max drawdown -20.19%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-20 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.48 · VIX 28.44 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 21564 decisions in 2589 calls, $0.2782 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T16:50 | 3 / 13 / 14 | cash |  |
| Breezy | 2026-11-20T16:50 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-20T16:50 | 7 / 18 / 5 | BITX 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.03 | +18.56% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.86 | 21.86 | 26 | 65.4 | 24.92 | 4.07 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.89 | 14.89 | 0 | — | 12.75 | 4.27 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.87 | 3.87 | 40 | 42.5 | 1.98 | 0.55 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 102.44 | 2.44 | 0 | — | 3.40 | 1.01 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.97 | -1.03 | 203 | 31.5 | -0.17 | 0.03 | -9.06 | 202 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 95.79 | -4.21 | 212 | 28.8 | -1.13 | -0.32 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 92.31 | -7.69 | 0 | — | -8.74 | -2.92 | -10.11 | 1 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.43 | -4.67 | -11.21 | 43 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Bullish score | daily | 89.68 | -10.32 | 19 | 15.8 | -12.59 | -3.17 | -19.56 | 14 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.31 | -10.69 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | VWAP reversion · 1h | reversion | 89.15 | -10.85 | 156 | 45.5 | -12.93 | -3.82 | -18.48 | 149 |
| 19 | Copy: Insider buying | copy | 88.64 | -11.36 | 55 | 40.0 | -7.06 | -1.35 | -14.79 | 66 |
| 20 | Copy: Congress Democrats (NANC) | copy | 87.85 | -12.15 | 0 | — | -12.83 | -3.56 | -15.07 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Squeeze breakout · 1h | breakout | 87.23 | -12.77 | 70 | 20.0 | -18.05 | -8.84 | -18.95 | 72 |
| 23 | Opening range 30m | breakout | 86.21 | -13.79 | 451 | 33.5 | -11.77 | -3.93 | -14.87 | 552 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.36 | -14.64 | 8 | 50.0 | -15.94 | -1.41 | -22.36 | 6 |
| 25 | Parabolic SAR · 1h | trend | 83.63 | -16.37 | 194 | 27.8 | -25.04 | -7.18 | -28.86 | 196 |
| 26 | Donchian 55/20 · 1h | breakout | 80.70 | -19.30 | 79 | 12.7 | -24.96 | -7.41 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 80.56 | -19.44 | 163 | 28.8 | -16.23 | -5.57 | -21.55 | 75 |
| 28 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -19.59 | -5.66 | -19.82 | 204 |
| 29 | Connors RSI(2) · 1h | reversion | 79.98 | -20.02 | 218 | 40.4 | -15.39 | -6.96 | -15.39 | 71 |
| 30 | Keltner breakout · 1h | breakout | 79.42 | -20.58 | 126 | 26.2 | -21.80 | -5.91 | -25.34 | 146 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -15.40 | -3.99 | -19.15 | 97 |
| 32 | Opening range 15m | breakout | 76.64 | -23.36 | 561 | 31.0 | -22.01 | -6.79 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 75.69 | -24.31 | 107 | 14.0 | -28.94 | -8.34 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 73.92 | -26.08 | 227 | 20.3 | -26.75 | -4.31 | -35.87 | 273 |
| 35 | Triple EMA stack · 1h | trend | 71.96 | -28.04 | 161 | 14.3 | -34.06 | -8.61 | -36.37 | 170 |
| 36 | Bollinger breakout · 1h | breakout | 71.92 | -28.08 | 195 | 21.5 | -32.16 | -8.35 | -36.32 | 217 |
| 37 | Supertrend · 1h | trend | 71.84 | -28.16 | 198 | 16.7 | -31.64 | -5.19 | -39.16 | 203 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 71.62 | -28.38 | 2 | 0.0 | -27.31 | -3.95 | -30.44 | 1 |
| 39 | EMA 20/50 cross · 1h | trend | 71.61 | -28.39 | 119 | 10.1 | -36.58 | -10.52 | -40.64 | 122 |
| 40 | Hold BTC | benchmark | 70.02 | -29.98 | 2 | 0.0 | -27.21 | -4.41 | -32.36 | 1 |
| 41 | Heikin-Ashi · 1h | trend | 69.98 | -30.02 | 483 | 23.0 | -44.73 | -9.56 | -47.85 | 616 |
| 42 | RSI momentum · 1h | momentum | 69.67 | -30.33 | 184 | 14.1 | -37.75 | -8.34 | -41.77 | 202 |
| 43 | OBV trend · 1h | momentum | 69.63 | -30.37 | 315 | 19.4 | -37.36 | -9.82 | -41.22 | 240 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 1-day momentum | meta | 69.29 | -30.71 | 33 | 27.3 | -51.50 | -3.65 | -58.28 | 39 |
| 46 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -51.84 | -3.56 | -60.06 | 22 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -40.39 | -5.94 | -41.57 | 435 |
| 49 | Donchian 20/10 · 1h | breakout | 66.37 | -33.63 | 165 | 17.6 | -35.48 | -6.64 | -43.26 | 192 |
| 50 | ROC + volume · 1h | momentum | 65.50 | -34.49 | 431 | 27.6 | -34.78 | -6.22 | -41.19 | 337 |
| 51 | MFI reversion · 1h | reversion | 65.26 | -34.74 | 475 | 33.1 | -34.80 | -5.21 | -36.49 | 172 |
| 52 | EMA 9/21 cross · 1h | trend | 63.83 | -36.17 | 291 | 11.3 | -39.36 | -7.42 | -47.32 | 323 |
| 53 | CCI reversion · 1h | reversion | 63.17 | -36.83 | 405 | 41.2 | -46.11 | -7.67 | -47.23 | 479 |
| 54 | MACD cross · 1h | trend | 62.30 | -37.70 | 444 | 20.9 | -50.26 | -9.96 | -51.00 | 496 |
| 55 | Bollinger reversion · 1h | reversion | 59.28 | -40.72 | 366 | 37.4 | -42.84 | -6.58 | -43.48 | 420 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -50.85 | -8.61 | -51.61 | 580 |
| 57 | Agent (ML meta-label) | meta | 56.45 | -43.55 | 2002 | 24.6 | -23.53 | -4.36 | -26.42 | 291 |
| 58 | RSI(14) reversion · 1h | reversion | 55.96 | -44.04 | 223 | 33.2 | -41.57 | -6.02 | -45.31 | 271 |
| 59 | VWAP momentum · 1h | momentum | 54.44 | -45.56 | 1013 | 21.4 | -56.70 | -11.44 | -60.93 | 1195 |
| 60 | Z-score reversion · 1h | reversion | 52.39 | -47.61 | 240 | 33.3 | -42.80 | -5.98 | -45.22 | 264 |
| 61 | Three white soldiers | momentum | 52.03 | -47.98 | 616 | 14.1 | -51.70 | -23.26 | -52.04 | 662 |
| 62 | Candlestick reversal · 1h | reversion | 51.40 | -48.60 | 598 | 25.9 | -51.72 | -9.53 | -52.04 | 676 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -47.72 | -99.16 | 5337 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.51 | -30.60 | -84.01 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.99 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.28 | -34.20 | -91.37 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.15 | -45.02 | -92.27 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -28.78 | -90.21 | 2023 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.23 | -50.87 | -98.23 | 3488 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -52.56 | -96.83 | 3389 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.96 | -40.03 | -94.07 | 2217 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.61 | -35.82 | -83.61 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -57.95 | -99.66 | 6304 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.99 | -46.33 | -93.05 | 2529 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.49 | -94.64 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -74.88 | -99.84 | 6260 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.49 | -47.20 | -93.49 | 2286 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.96 | -26.77 | -78.96 | 1638 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.83 | -60.89 | -97.83 | 3379 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -59.92 | -99.14 | 5074 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.91 | -29.85 | -70.91 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.96 | -56.89 | -94.96 | 2716 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.76 | -39.54 | -85.98 | 1705 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -74.06 | -99.73 | 6516 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.55 | -32.37 | -91.55 | 2464 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.63 | -19.76 | -81.63 | 1919 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.30 | -37.17 | -92.30 | 2207 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.85 | -48.24 | -97.85 | 4017 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.37 | -54.48 | -90.37 | 2186 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.52 | -31.80 | -67.61 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.09 | -28.42 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.80 | -19.19 | -83.80 | 1831 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.75 | -47.62 | -97.75 | 4427 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -116.93 | -99.94 | 8421 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | UPRO | 4.72 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | TQQQ | 4.67 | -0.24 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | TNA | 4.76 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | SPY | 4.85 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | SOXL | 4.46 | -0.45 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | QQQ | 4.83 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | PLTR | 4.80 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | NVDA | 4.81 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | MSTR | 4.82 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | META | 4.87 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | LABU | 4.82 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | AMZN | 4.83 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:45 | Agent (rotation) | buy | SQQQ | 31.59 | — | rebalance up |
| 2026-11-20T16:45 | Day trade: Stocks in Play ORB | sell | GOOGL | 24.70 | -0.24 | target is flat |
| 2026-11-20T16:45 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 121.75 | — | entry |
| 2026-11-20T16:45 | Williams %R · 1h | sell | LABU | 14.33 | -0.35 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:45 | Williams %R · 1h | sell | GOOGL | 14.44 | -0.18 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:45 | Williams %R · 1h | sell | AMZN | 14.39 | -0.22 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:45 | Williams %R · 1h | sell | AAPL | 11.65 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:30 | Agent | sell | TSLA | 31.91 | -0.43 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:30 | Agent | sell | SOXL | 31.55 | -1.20 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:30 | Connors RSI(2) · 1h | buy | AAPL | 20.02 | — | entry signal |
| 2026-11-20T16:10 | Williams %R · 1h | buy | LABU | 2.93 | — | rebalance up |
| 2026-11-20T16:10 | Williams %R · 1h | buy | GOOGL | 2.94 | — | rebalance up |
| 2026-11-20T16:10 | Williams %R · 1h | buy | AMZN | 2.92 | — | rebalance up |
| 2026-11-20T16:10 | Williams %R · 1h | sell | MSFT | 11.59 | -0.16 | stop-loss |
| 2026-11-20T16:10 | Stochastic reversion · 1h | sell | MSFT | 4.86 | -0.03 | stop-loss |
| 2026-11-20T16:05 | Agent (aggressive) | sell | TSLA | 39.68 | -0.19 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:05 | Agent (aggressive) | sell | SOXL | 38.62 | -1.25 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:05 | Agent | buy | TSLA | 15.99 | — | rebalance up |
| 2026-11-20T16:05 | Agent | sell | META | 16.24 | -0.10 | selected signal exited |
| 2026-11-20T16:05 | EMA 20/50 cross · 1h | sell | SQQQ | 3.72 | 0.66 | rebalance down |
| 2026-11-20T16:05 | Opening range 15m | sell | GOOGL | 18.84 | -0.25 | stop-loss |
| 2026-11-20T16:05 | Opening range 15m | sell | AMZN | 19.00 | -0.13 | stop-loss |
| 2026-11-20T16:00 | Agent | buy | META | 16.35 | — | following MFI reversion |
| 2026-11-20T16:00 | Agent | sell | TSLA | 16.40 | -0.02 | rebalance down |
| 2026-11-20T16:00 | Bollinger reversion · 1h | sell | TNA | 11.90 | -0.60 | stop-loss |
| 2026-11-20T15:55 | Agent | buy | SOXL | 16.35 | — | rebalance up |
| 2026-11-20T15:50 | Day trade: Stocks in Play ORB | sell | MSFT | 24.93 | -0.02 | target is flat |
| 2026-11-20T15:50 | Agent (aggressive) | buy | SOXL | 39.87 | — | following Z-score reversion, CCI reversion |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 16:50:05.000125+00:00 -> 2026-11-20 17:00:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
