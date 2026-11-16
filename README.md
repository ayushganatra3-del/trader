# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T17:39:05.000154+00:00 · 62180 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.02 (-13.98%)

Closed trades 198, win rate 36.4%, fees £5.70, max drawdown -15.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.11 | -0.04 |
| TSLA | 17.20 | -0.01 |

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

Today: 26172 decisions in 2838 calls, $0.3328 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T17:39 | 1 / 9 / 20 | cash |  |
| Breezy | 2026-11-16T17:39 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-16T17:39 | 4 / 18 / 8 | COIN 68% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.13 | 18.13 | 0 | — | 15.26 | 5.05 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 15.38 | 3.13 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.84 | 3.84 | 0 | — | 5.58 | 1.53 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.88 | 1.88 | 34 | 41.2 | 0.45 | 0.23 | -9.64 | 31 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -2.55 | -2.21 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 6.54 | 1.83 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 1.20 | 0.42 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.06 | -2.94 | 0 | — | -1.91 | -0.58 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.84 | -5.16 | 0 | — | -5.58 | -1.47 | -8.27 | 1 |
| 14 | Agent (rotation) | meta | 93.97 | -6.03 | 195 | 29.7 | -4.07 | -1.45 | -8.86 | 153 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 16 | Copy: Insider buying | copy | 92.58 | -7.42 | 47 | 42.6 | -9.16 | -1.85 | -14.95 | 62 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.12 | -7.88 | 0 | — | -6.35 | -1.68 | -10.64 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.36 | -9.64 | 112 | 23.2 | -15.26 | -6.92 | -17.21 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -7.91 | -2.39 | -15.48 | 74 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.42 | -13.58 | 16 | 18.8 | -7.26 | -1.22 | -19.56 | 15 |
| 24 | Agent | meta | 86.02 | -13.98 | 198 | 36.4 | -13.78 | -6.73 | -16.06 | 203 |
| 25 | Opening range 30m | breakout | 85.87 | -14.13 | 436 | 33.5 | -11.01 | -3.52 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.39 | -16.61 | 95 | 34.7 | -14.65 | -4.01 | -16.78 | 97 |
| 27 | Parabolic SAR · 1h | trend | 83.32 | -16.68 | 180 | 28.3 | -18.20 | -3.95 | -24.93 | 215 |
| 28 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -21.47 | -4.53 | -28.90 | 86 |
| 29 | Connors RSI(2) · 1h | reversion | 80.37 | -19.63 | 212 | 40.1 | -14.46 | -6.36 | -14.99 | 98 |
| 30 | Keltner breakout · 1h | breakout | 80.33 | -19.67 | 121 | 25.6 | -17.50 | -3.71 | -25.69 | 164 |
| 31 | Volume breakout · 1h | breakout | 79.69 | -20.31 | 161 | 28.6 | -16.27 | -5.15 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 77.93 | -22.07 | 530 | 31.5 | -18.05 | -4.86 | -21.37 | 702 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 77.87 | -22.14 | 2 | 0.0 | -14.19 | -1.74 | -24.26 | 1 |
| 34 | Max aggression: 5-day momentum | meta | 77.13 | -22.87 | 21 | 42.9 | -49.26 | -3.28 | -55.24 | 23 |
| 35 | Hold BTC | benchmark | 75.86 | -24.14 | 2 | 0.0 | -15.33 | -2.15 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.29 | -31.62 | 116 |
| 37 | Stochastic reversion · 1h | reversion | 74.99 | -25.01 | 322 | 45.3 | -30.90 | -4.60 | -31.91 | 409 |
| 38 | ADX DI cross · 1h | trend | 74.50 | -25.50 | 207 | 19.3 | -23.18 | -3.48 | -33.59 | 261 |
| 39 | Bollinger breakout · 1h | breakout | 74.26 | -25.74 | 184 | 22.3 | -23.87 | -4.97 | -31.79 | 234 |
| 40 | Max aggression: 1-day momentum | meta | 73.98 | -26.02 | 30 | 26.7 | -24.39 | -0.91 | -57.50 | 40 |
| 41 | MACD zero-line · 1h | trend | 72.49 | -27.51 | 173 | 18.5 | -23.04 | -4.41 | -30.90 | 191 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -24.66 | -3.49 | -28.68 | 163 |
| 43 | Heikin-Ashi · 1h | trend | 71.56 | -28.44 | 459 | 23.3 | -36.26 | -6.05 | -43.26 | 638 |
| 44 | Supertrend · 1h | trend | 71.48 | -28.52 | 186 | 15.6 | -32.46 | -5.51 | -39.67 | 200 |
| 45 | RSI momentum · 1h | momentum | 71.03 | -28.97 | 175 | 14.3 | -27.65 | -4.43 | -37.79 | 205 |
| 46 | Triple EMA stack · 1h | trend | 71.02 | -28.98 | 153 | 14.4 | -26.34 | -4.26 | -37.64 | 193 |
| 47 | MACD cross · 1h | trend | 70.99 | -29.01 | 401 | 22.7 | -32.93 | -4.68 | -42.84 | 471 |
| 48 | EMA 20/50 cross · 1h | trend | 70.78 | -29.22 | 111 | 9.9 | -33.57 | -7.82 | -40.12 | 114 |
| 49 | ROC + volume · 1h | momentum | 70.56 | -29.44 | 404 | 28.5 | -28.14 | -4.62 | -37.85 | 357 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.90 | -4.96 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.97 | -31.03 | 302 | 19.2 | -29.45 | -5.08 | -39.42 | 267 |
| 52 | CCI reversion · 1h | reversion | 68.58 | -31.43 | 372 | 41.7 | -38.72 | -6.24 | -41.88 | 459 |
| 53 | Donchian 20/10 · 1h | breakout | 67.54 | -32.46 | 157 | 18.5 | -29.16 | -4.54 | -39.23 | 206 |
| 54 | Bollinger reversion · 1h ⏸ | reversion | 66.56 | -33.45 | 333 | 39.0 | -35.06 | -5.32 | -35.97 | 405 |
| 55 | Williams %R · 1h | reversion | 64.43 | -35.57 | 415 | 41.4 | -44.07 | -7.44 | -44.75 | 545 |
| 56 | EMA 9/21 cross · 1h | trend | 64.39 | -35.61 | 270 | 11.5 | -34.58 | -5.66 | -44.10 | 319 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -19.14 | -3.65 | -24.63 | 338 |
| 58 | RSI(14) reversion · 1h | reversion | 60.29 | -39.71 | 201 | 32.3 | -36.36 | -5.07 | -41.16 | 246 |
| 59 | Z-score reversion · 1h | reversion | 59.86 | -40.14 | 221 | 35.7 | -34.51 | -4.73 | -35.77 | 237 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.58 | -9.74 | -57.07 | 1210 |
| 61 | Candlestick reversal · 1h | reversion | 57.72 | -42.28 | 526 | 27.2 | -43.55 | -7.69 | -45.03 | 627 |
| 62 | Three white soldiers | momentum | 56.79 | -43.21 | 567 | 14.8 | -49.45 | -21.93 | -49.45 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -41.93 | -99.02 | 5322 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.33 | -25.83 | -81.33 | 1421 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.92 | -43.46 | -93.92 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.10 | -32.56 | -90.11 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.57 | -40.84 | -91.57 | 2335 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.85 | -30.18 | -89.89 | 2147 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -48.08 | -97.89 | 3456 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -54.53 | -96.37 | 3435 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -35.96 | -93.53 | 2272 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.89 | -33.46 | -82.89 | 1641 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.30 | -99.60 | 6021 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.08 | -42.22 | -92.08 | 2592 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.15 | -35.69 | -95.16 | 3364 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -67.79 | -99.81 | 6128 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.46 | -42.85 | -92.47 | 2270 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.27 | -25.92 | -76.27 | 1657 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.59 | -55.69 | -97.60 | 3471 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -55.39 | -98.99 | 4915 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.29 | -26.71 | -68.47 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -54.75 | -94.68 | 2761 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.79 | -36.81 | -84.79 | 1760 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -66.73 | -99.69 | 6359 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.35 | -29.51 | -90.37 | 2325 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.89 | -18.80 | -79.97 | 1813 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.00 | -35.77 | -91.05 | 2179 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.43 | -43.65 | -97.45 | 3896 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.14 | -58.76 | -89.14 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.41 | -29.23 | -66.41 | 827 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.19 | -23.07 | -72.31 | 1249 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.10 | -17.26 | -80.76 | 1743 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -45.17 | -97.57 | 4337 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -95.91 | -99.94 | 8379 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T17:35 | Agent | buy | TSLA | 17.21 | — | following Bollinger reversion |
| 2026-11-16T17:35 | Three white soldiers | sell | XRP-USD | 14.14 | -0.13 | exit signal |
| 2026-11-16T17:30 | Williams %R · 1h | buy | QQQ | 4.34 | — | entry |
| 2026-11-16T17:30 | Williams %R · 1h | sell | SPY | 4.34 | -0.02 | stop-loss |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | UPRO | 4.73 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | TQQQ | 4.72 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | TNA | 4.76 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | TECL | 4.69 | -0.12 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | SPY | 4.79 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | SOXL | 4.68 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | QQQ | 4.78 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | PLTR | 4.75 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | MSTR | 4.75 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | LABU | 4.76 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | IWM | 4.79 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | GOOGL | 4.78 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | BITX | 4.84 | 0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | Bollinger reversion · 1h | sell | AMZN | 4.74 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T17:30 | OBV trend · 1h | sell | META | 17.22 | -0.17 | exit signal |
| 2026-11-16T17:30 | RSI momentum · 1h | sell | AAPL | 17.91 | -0.04 | exit signal |
| 2026-11-16T17:30 | Three white soldiers | sell | DOGE-USD | 14.13 | -0.13 | exit signal |
| 2026-11-16T17:10 | Donchian 55/20 · 1h | sell | AAPL | 20.59 | -0.20 | stop-loss |
| 2026-11-16T17:05 | Three white soldiers | buy | XRP-USD | 14.26 | — | entry signal |
| 2026-11-16T17:05 | Three white soldiers | buy | DOGE-USD | 14.26 | — | entry signal |
| 2026-11-16T17:00 | Williams %R · 1h | buy | PLTR | 3.93 | — | entry |
| 2026-11-16T17:00 | Williams %R · 1h | buy | META | 3.33 | — | rebalance up |
| 2026-11-16T17:00 | Williams %R · 1h | sell | DOGE-USD | 7.26 | 0.08 | exit signal |
| 2026-11-16T17:00 | ROC + volume · 1h | buy | DOGE-USD | 17.61 | — | entry signal |
| 2026-11-16T17:00 | MACD cross · 1h | buy | XRP-USD | 10.13 | — | entry signal |
| 2026-11-16T17:00 | MACD cross · 1h | buy | SOL-USD | 10.17 | — | entry signal |
| 2026-11-16T17:00 | MACD cross · 1h | sell | SQQQ | 3.96 | 0.11 | rebalance down |
| 2026-11-16T17:00 | MACD cross · 1h | sell | NVDA | 4.01 | -0.02 | rebalance down |
| 2026-11-16T17:00 | MACD cross · 1h | sell | ETH-USD | 4.04 | -0.04 | rebalance down |
| 2026-11-16T17:00 | MACD cross · 1h | sell | DOGE-USD | 4.20 | 0.01 | rebalance down |
| 2026-11-16T17:00 | MACD cross · 1h | sell | BTC-USD | 4.08 | -0.02 | rebalance down |
| 2026-11-16T17:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 16.10 | — | entry signal |
| 2026-11-16T16:50 | Three white soldiers | sell | MSFT | 14.35 | 0.06 | exit signal |
| 2026-11-16T16:40 | Candlestick reversal · 1h | buy | MSTR | 5.80 | — | entry |
| 2026-11-16T16:40 | Candlestick reversal · 1h | buy | BITX | 3.75 | — | rebalance up |
| 2026-11-16T16:40 | Candlestick reversal · 1h | sell | NVDA | 4.75 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 17:39:05.000154+00:00 -> 2026-11-16 17:49:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 17:39:05.000154+00:00 -> 2026-11-16 17:49:05.000154+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
