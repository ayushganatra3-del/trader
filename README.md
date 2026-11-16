# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T19:11:05.000107+00:00 · 62257 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.06 (-13.94%)

Closed trades 199, win rate 36.2%, fees £5.72, max drawdown -15.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.19 | +0.04 |
| SOXL | 17.18 | -0.02 |

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

Today: 33114 decisions in 3069 calls, $0.4141 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T19:11 | 1 / 2 / 27 | cash |  |
| Breezy | 2026-11-16T19:11 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-16T19:11 | 3 / 19 / 8 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.88 | 17.88 | 0 | — | 14.48 | 4.81 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.01 | 10.01 | 23 | 65.2 | 14.12 | 2.88 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.66 | 3.66 | 0 | — | 5.45 | 1.50 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 35 | 40.0 | -1.00 | -0.10 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -2.55 | -2.21 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 6.94 | 1.94 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 1.17 | 0.42 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.74 | -3.26 | 0 | — | -2.39 | -0.73 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.02 | -5.98 | 0 | — | -6.44 | -1.68 | -8.27 | 1 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 15 | Agent (rotation) | meta | 93.63 | -6.37 | 195 | 29.7 | -2.96 | -1.03 | -7.92 | 150 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 17 | Copy: Insider buying | copy | 91.80 | -8.20 | 47 | 42.6 | -9.89 | -1.98 | -14.95 | 62 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.51 | -8.49 | 0 | — | -6.21 | -1.62 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.32 | -9.68 | 112 | 23.2 | -15.61 | -7.04 | -17.58 | 66 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -7.45 | -2.12 | -15.48 | 74 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.46 | -13.54 | 16 | 18.8 | -5.42 | -0.87 | -19.56 | 15 |
| 24 | Agent | meta | 86.06 | -13.94 | 199 | 36.2 | -13.65 | -6.65 | -15.98 | 200 |
| 25 | Opening range 30m | breakout | 85.95 | -14.05 | 436 | 33.5 | -10.97 | -3.50 | -14.11 | 584 |
| 26 | Agent (aggressive) | meta | 83.60 | -16.40 | 95 | 34.7 | -14.42 | -3.94 | -16.78 | 97 |
| 27 | Parabolic SAR · 1h | trend | 83.21 | -16.79 | 180 | 28.3 | -18.02 | -3.92 | -24.74 | 215 |
| 28 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -21.87 | -4.74 | -28.90 | 86 |
| 29 | Keltner breakout · 1h | breakout | 80.40 | -19.60 | 121 | 25.6 | -18.19 | -4.15 | -25.47 | 161 |
| 30 | Connors RSI(2) · 1h | reversion | 80.29 | -19.71 | 213 | 39.9 | -14.09 | -6.17 | -14.68 | 98 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 161 | 28.6 | -16.37 | -5.18 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 78.00 | -22.00 | 530 | 31.5 | -17.88 | -4.82 | -21.37 | 702 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 77.78 | -22.22 | 2 | 0.0 | -14.21 | -1.74 | -24.50 | 1 |
| 34 | Max aggression: 5-day momentum | meta | 77.41 | -22.59 | 21 | 42.9 | -49.04 | -3.27 | -55.24 | 23 |
| 35 | Hold BTC | benchmark | 75.87 | -24.13 | 2 | 0.0 | -14.90 | -2.08 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.29 | -31.62 | 116 |
| 37 | ADX DI cross · 1h | trend | 74.57 | -25.43 | 207 | 19.3 | -23.21 | -3.52 | -33.78 | 256 |
| 38 | Max aggression: 1-day momentum | meta | 74.26 | -25.74 | 30 | 26.7 | -24.07 | -0.88 | -57.50 | 40 |
| 39 | Bollinger breakout · 1h | breakout | 74.24 | -25.76 | 184 | 22.3 | -23.80 | -4.95 | -31.74 | 234 |
| 40 | Stochastic reversion · 1h ⏸ | reversion | 74.07 | -25.93 | 333 | 44.1 | -31.53 | -4.67 | -32.96 | 409 |
| 41 | MACD zero-line · 1h | trend | 72.35 | -27.65 | 173 | 18.5 | -24.74 | -4.86 | -31.30 | 191 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -25.69 | -3.64 | -29.27 | 161 |
| 43 | Heikin-Ashi · 1h | trend | 71.63 | -28.38 | 459 | 23.3 | -36.19 | -6.05 | -43.26 | 638 |
| 44 | Supertrend · 1h | trend | 71.36 | -28.64 | 187 | 16.0 | -32.61 | -5.56 | -39.35 | 201 |
| 45 | RSI momentum · 1h | momentum | 71.10 | -28.90 | 175 | 14.3 | -28.03 | -4.56 | -37.87 | 206 |
| 46 | Triple EMA stack · 1h | trend | 71.06 | -28.94 | 154 | 14.9 | -27.42 | -4.63 | -38.18 | 192 |
| 47 | EMA 20/50 cross · 1h | trend | 70.90 | -29.10 | 111 | 9.9 | -35.35 | -9.52 | -38.77 | 113 |
| 48 | MACD cross · 1h | trend | 70.76 | -29.24 | 402 | 22.6 | -33.28 | -4.76 | -42.93 | 470 |
| 49 | ROC + volume · 1h | momentum | 70.60 | -29.40 | 404 | 28.5 | -27.93 | -4.58 | -37.72 | 357 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.46 | -4.88 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.00 | -31.00 | 302 | 19.2 | -29.69 | -5.15 | -39.48 | 267 |
| 52 | CCI reversion · 1h | reversion | 67.92 | -32.08 | 375 | 41.6 | -39.55 | -6.36 | -41.93 | 460 |
| 53 | Donchian 20/10 · 1h | breakout | 67.52 | -32.48 | 157 | 18.5 | -29.32 | -4.59 | -39.29 | 206 |
| 54 | Bollinger reversion · 1h ⏸ | reversion | 66.56 | -33.45 | 333 | 39.0 | -35.43 | -5.34 | -36.72 | 407 |
| 55 | EMA 9/21 cross · 1h | trend | 64.31 | -35.69 | 270 | 11.5 | -34.65 | -5.69 | -44.12 | 319 |
| 56 | Williams %R · 1h | reversion | 64.11 | -35.89 | 418 | 41.1 | -44.79 | -7.57 | -45.22 | 546 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -23.51 | -4.29 | -28.68 | 344 |
| 58 | Z-score reversion · 1h | reversion | 59.86 | -40.14 | 221 | 35.7 | -34.51 | -4.73 | -35.77 | 237 |
| 59 | RSI(14) reversion · 1h | reversion | 59.58 | -40.42 | 202 | 32.2 | -41.47 | -6.16 | -41.60 | 245 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.71 | -9.73 | -57.23 | 1210 |
| 61 | Candlestick reversal · 1h | reversion | 57.66 | -42.34 | 527 | 27.1 | -45.35 | -8.30 | -45.92 | 613 |
| 62 | Three white soldiers | momentum | 56.74 | -43.26 | 568 | 14.8 | -49.50 | -21.93 | -49.50 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -41.82 | -99.03 | 5322 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.48 | -25.87 | -81.49 | 1428 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.01 | -43.12 | -94.01 | 2515 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.04 | -32.16 | -90.07 | 1939 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.49 | -40.85 | -91.50 | 2328 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.92 | -30.19 | -89.92 | 2146 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.93 | -47.73 | -97.93 | 3463 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.46 | -53.84 | -96.46 | 3440 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.32 | -35.86 | -93.33 | 2249 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.72 | -32.88 | -82.72 | 1635 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -52.72 | -99.59 | 6033 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.10 | -42.06 | -92.11 | 2587 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.17 | -35.81 | -95.17 | 3351 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -66.50 | -99.81 | 6142 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.48 | -42.58 | -92.48 | 2271 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.36 | -25.94 | -76.36 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -56.24 | -97.62 | 3469 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -54.49 | -98.98 | 4936 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.33 | -26.69 | -68.53 | 1222 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -54.74 | -94.71 | 2757 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.79 | -37.03 | -84.79 | 1758 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -65.26 | -99.69 | 6369 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.37 | -29.55 | -90.45 | 2332 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.70 | -18.66 | -79.85 | 1809 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.99 | -35.40 | -91.06 | 2185 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.43 | -43.75 | -97.44 | 3897 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.18 | -58.15 | -89.20 | 2154 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -29.24 | -66.40 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.05 | -23.09 | -72.20 | 1246 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.28 | -17.45 | -80.74 | 1758 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.54 | -44.57 | -97.57 | 4355 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -94.54 | -99.94 | 8389 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T19:05 | Three white soldiers | sell | AMZN | 14.15 | -0.05 | exit signal |
| 2026-11-16T19:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 100.98 | -0.90 | target is flat |
| 2026-11-16T19:00 | MACD zero-line · 1h | buy | ETH-USD | 18.13 | — | entry signal |
| 2026-11-16T19:00 | MACD zero-line · 1h | buy | DOGE-USD | 18.13 | — | entry signal |
| 2026-11-16T18:55 | Agent | sell | TSLA | 17.18 | -0.03 | selected signal exited |
| 2026-11-16T18:50 | Three white soldiers | buy | AMZN | 14.20 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 19:11:05.000107+00:00 -> 2026-11-16 19:21:05.000107+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 19:11:05.000107+00:00 -> 2026-11-16 19:21:05.000107+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
