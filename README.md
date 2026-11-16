# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T18:40:05.000128+00:00 · 62228 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.40 (-14.60%)

Closed trades 198, win rate 36.4%, fees £5.71, max drawdown -15.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.08 | -0.07 |
| SOXL | 16.70 | -0.50 |
| TSLA | 17.10 | -0.11 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-16 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 30504 decisions in 2982 calls, $0.3836 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T18:40 | 1 / 11 / 18 | cash |  |
| Breezy | 2026-11-16T18:40 | 0 / 21 / 9 | cash |  |
| Boozy | 2026-11-16T18:40 | 6 / 15 / 9 | COIN 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.82 | +5.11% | 10 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| CCI reversion | SOXL | 2.19 | +16.29% | 10 |
| Bollinger reversion | TSLA | 2.18 | +2.18% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.86 | 17.86 | 0 | — | 14.91 | 4.93 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.18 | 11.18 | 23 | 65.2 | 15.34 | 3.12 | -4.91 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.51 | 3.51 | 0 | — | 5.30 | 1.46 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.38 | 2.38 | 34 | 41.2 | 0.69 | 0.28 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -2.55 | -2.21 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 6.54 | 1.83 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 1.13 | 0.41 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.52 | -3.48 | 0 | — | -2.34 | -0.71 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.80 | -5.20 | 0 | — | -5.58 | -1.47 | -8.27 | 1 |
| 14 | Agent (rotation) | meta | 93.97 | -6.04 | 195 | 29.7 | -2.62 | -0.90 | -7.92 | 150 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 17 | Copy: Insider buying | copy | 92.06 | -7.94 | 47 | 42.6 | -9.62 | -1.93 | -14.95 | 62 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.74 | -8.26 | 0 | — | -5.97 | -1.56 | -10.70 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.29 | -9.71 | 112 | 23.2 | -15.64 | -7.04 | -17.57 | 66 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -9.09 | -3.07 | -15.48 | 73 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.63 | -13.37 | 16 | 18.8 | -5.62 | -0.90 | -19.56 | 15 |
| 24 | Opening range 30m | breakout | 86.18 | -13.82 | 436 | 33.5 | -10.60 | -3.37 | -14.11 | 583 |
| 25 | Agent | meta | 85.40 | -14.60 | 198 | 36.4 | -14.51 | -7.20 | -16.17 | 203 |
| 26 | Agent (aggressive) | meta | 83.33 | -16.67 | 95 | 34.7 | -13.82 | -3.70 | -16.78 | 99 |
| 27 | Parabolic SAR · 1h | trend | 83.22 | -16.78 | 180 | 28.3 | -18.09 | -3.91 | -24.74 | 215 |
| 28 | Keltner breakout · 1h | breakout | 80.62 | -19.38 | 121 | 25.6 | -17.66 | -4.00 | -24.90 | 162 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -21.47 | -4.53 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.23 | -19.77 | 213 | 39.9 | -14.15 | -6.19 | -14.68 | 98 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 161 | 28.6 | -16.37 | -5.18 | -21.95 | 85 |
| 32 | Max aggression: 5-day momentum | meta | 78.24 | -21.76 | 21 | 42.9 | -48.50 | -3.24 | -55.24 | 23 |
| 33 | Opening range 15m | breakout | 78.21 | -21.79 | 530 | 31.5 | -17.68 | -4.75 | -21.37 | 702 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.47 | -22.53 | 2 | 0.0 | -14.22 | -1.73 | -24.26 | 1 |
| 35 | Hold BTC | benchmark | 75.81 | -24.18 | 2 | 0.0 | -14.81 | -2.07 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.29 | -31.62 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 75.05 | -24.95 | 30 | 26.7 | -23.26 | -0.83 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.77 | -25.23 | 207 | 19.3 | -24.70 | -3.88 | -33.78 | 256 |
| 39 | Bollinger breakout · 1h | breakout | 74.44 | -25.56 | 184 | 22.3 | -23.71 | -4.93 | -31.79 | 234 |
| 40 | Stochastic reversion · 1h ⏸ | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.00 | -4.70 | -32.99 | 409 |
| 41 | MACD zero-line · 1h | trend | 72.75 | -27.25 | 173 | 18.5 | -24.32 | -4.77 | -31.30 | 189 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -25.98 | -3.68 | -29.27 | 161 |
| 43 | Heikin-Ashi · 1h | trend | 71.82 | -28.18 | 459 | 23.3 | -36.02 | -6.03 | -43.26 | 638 |
| 44 | Supertrend · 1h | trend | 71.50 | -28.50 | 187 | 16.0 | -32.42 | -5.51 | -39.67 | 200 |
| 45 | RSI momentum · 1h | momentum | 71.29 | -28.71 | 175 | 14.3 | -27.72 | -4.47 | -37.88 | 206 |
| 46 | Triple EMA stack · 1h | trend | 71.26 | -28.74 | 154 | 14.9 | -26.90 | -4.45 | -38.18 | 192 |
| 47 | MACD cross · 1h | trend | 70.90 | -29.10 | 402 | 22.6 | -33.12 | -4.73 | -42.93 | 470 |
| 48 | EMA 20/50 cross · 1h | trend | 70.85 | -29.15 | 111 | 9.9 | -33.42 | -7.77 | -40.18 | 114 |
| 49 | ROC + volume · 1h | momentum | 70.84 | -29.16 | 404 | 28.5 | -27.50 | -4.45 | -37.80 | 356 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.37 | -4.86 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.11 | -30.89 | 302 | 19.2 | -29.46 | -5.10 | -39.48 | 267 |
| 52 | CCI reversion · 1h | reversion | 67.93 | -32.07 | 375 | 41.6 | -39.40 | -6.32 | -41.93 | 459 |
| 53 | Donchian 20/10 · 1h | breakout | 67.70 | -32.30 | 157 | 18.5 | -29.06 | -4.55 | -39.23 | 206 |
| 54 | Bollinger reversion · 1h ⏸ | reversion | 66.56 | -33.45 | 333 | 39.0 | -35.83 | -5.36 | -36.73 | 407 |
| 55 | EMA 9/21 cross · 1h | trend | 64.48 | -35.52 | 270 | 11.5 | -34.55 | -5.67 | -44.12 | 319 |
| 56 | Williams %R · 1h | reversion | 63.99 | -36.01 | 418 | 41.1 | -44.50 | -7.46 | -45.02 | 544 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -22.94 | -4.47 | -28.35 | 357 |
| 58 | Z-score reversion · 1h | reversion | 59.86 | -40.14 | 221 | 35.7 | -34.51 | -4.73 | -35.77 | 237 |
| 59 | RSI(14) reversion · 1h | reversion | 59.57 | -40.43 | 202 | 32.2 | -40.28 | -5.92 | -41.59 | 241 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.53 | -9.74 | -57.19 | 1210 |
| 61 | Candlestick reversal · 1h | reversion | 57.48 | -42.52 | 527 | 27.1 | -45.41 | -8.26 | -45.64 | 609 |
| 62 | Three white soldiers | momentum | 56.79 | -43.21 | 567 | 14.8 | -49.45 | -21.93 | -49.45 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -42.33 | -99.04 | 5322 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.44 | -25.90 | -81.46 | 1428 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.00 | -43.13 | -94.00 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.01 | -31.90 | -90.02 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.43 | -40.05 | -91.47 | 2325 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.86 | -30.16 | -89.88 | 2147 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.92 | -47.95 | -97.92 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -54.48 | -96.42 | 3436 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.29 | -34.72 | -93.32 | 2246 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.85 | -33.46 | -82.89 | 1639 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -53.00 | -99.60 | 6031 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.05 | -42.15 | -92.08 | 2588 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.18 | -35.78 | -95.18 | 3355 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -66.31 | -99.81 | 6130 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.49 | -42.63 | -92.49 | 2271 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.28 | -25.96 | -76.31 | 1655 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.58 | -56.20 | -97.59 | 3465 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -54.00 | -98.98 | 4919 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.44 | -26.67 | -68.73 | 1224 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -54.75 | -94.69 | 2759 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -36.79 | -84.73 | 1758 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -65.64 | -99.69 | 6355 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.44 | -29.69 | -90.45 | 2326 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.95 | -18.83 | -79.95 | 1809 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.98 | -35.30 | -91.02 | 2176 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.45 | -43.66 | -97.45 | 3894 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.17 | -57.79 | -89.20 | 2154 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.43 | -29.21 | -66.43 | 826 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.98 | -23.07 | -72.20 | 1246 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.37 | -17.52 | -80.72 | 1748 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -44.66 | -97.56 | 4354 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -94.37 | -99.94 | 8375 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T18:35 | Agent (rotation) | buy | SQQQ | 31.32 | — | entry |
| 2026-11-16T18:35 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 111.21 | — | entry |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | TSLA | 6.79 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | TQQQ | 6.63 | -0.26 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | TNA | 6.67 | -0.20 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | TECL | 6.59 | -0.31 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | QQQ | 6.80 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | MSFT | 6.81 | 0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | LABU | 6.57 | -0.35 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | IWM | 6.82 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | GOOGL | 6.79 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | AMD | 6.76 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | AAPL | 6.83 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Connors RSI(2) · 1h | sell | AAPL | 19.92 | -0.24 | stop-loss |
| 2026-11-16T18:31 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 101.88 | — | entry |
| 2026-11-16T18:31 | RSI(14) reversion · 1h | sell | NVDA | 12.33 | -0.70 | stop-loss |
| 2026-11-16T18:31 | Supertrend · 1h | buy | BTC-USD | 4.03 | — | rebalance up |
| 2026-11-16T18:31 | Supertrend · 1h | sell | AAPL | 8.28 | 0.21 | exit signal |
| 2026-11-16T18:31 | MACD cross · 1h | sell | NVDA | 9.90 | -0.31 | exit signal |
| 2026-11-16T18:31 | Triple EMA stack · 1h | sell | AAPL | 14.86 | 0.32 | exit signal |
| 2026-11-16T18:20 | Williams %R · 1h | sell | TNA | 6.52 | -0.24 | stop-loss |
| 2026-11-16T18:20 | Williams %R · 1h | sell | IWM | 6.69 | -0.07 | stop-loss |
| 2026-11-16T18:15 | CCI reversion · 1h | sell | LABU | 16.80 | -0.60 | stop-loss |
| 2026-11-16T18:15 | Williams %R · 1h | buy | TQQQ | 3.95 | — | entry |
| 2026-11-16T18:15 | Williams %R · 1h | sell | LABU | 3.95 | -0.28 | stop-loss |
| 2026-11-16T18:00 | CCI reversion · 1h | buy | XRP-USD | 5.60 | — | rebalance up |
| 2026-11-16T18:00 | CCI reversion · 1h | buy | LABU | 3.47 | — | rebalance up |
| 2026-11-16T18:00 | CCI reversion · 1h | buy | BTC-USD | 5.63 | — | rebalance up |
| 2026-11-16T18:00 | CCI reversion · 1h | sell | DOGE-USD | 11.47 | 0.05 | exit signal |
| 2026-11-16T17:41 | Agent | buy | SOXL | 17.21 | — | following CCI reversion |
| 2026-11-16T17:41 | CCI reversion · 1h | buy | SOL-USD | 3.82 | — | rebalance up |
| 2026-11-16T17:41 | CCI reversion · 1h | buy | LABU | 4.00 | — | rebalance up |
| 2026-11-16T17:41 | CCI reversion · 1h | sell | NVDA | 9.54 | -0.35 | stop-loss |
| 2026-11-16T17:41 | Candlestick reversal · 1h | sell | MSTR | 5.74 | -0.05 | target is flat |
| 2026-11-16T17:41 | OBV trend · 1h | buy | META | 17.24 | — | entry |
| 2026-11-16T17:35 | Agent | buy | TSLA | 17.21 | — | following Bollinger reversion |
| 2026-11-16T17:35 | Three white soldiers | sell | XRP-USD | 14.14 | -0.13 | exit signal |
| 2026-11-16T17:30 | Williams %R · 1h | buy | QQQ | 4.34 | — | entry |
| 2026-11-16T17:30 | Williams %R · 1h | sell | SPY | 4.34 | -0.02 | stop-loss |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | UPRO | 4.73 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 18:40:05.000128+00:00 -> 2026-11-16 18:50:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 18:40:05.000128+00:00 -> 2026-11-16 18:50:05.000128+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
