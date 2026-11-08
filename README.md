# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-08T22:15:05.000164+00:00 · 52614 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.54 (-12.46%)

Closed trades 156, win rate 35.9%, fees £4.84, max drawdown -12.87%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 17301 decisions in 3465 calls, $0.2418 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-08T22:15 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-08T22:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-08T22:15 | 5 / 0 / 0 | BTC-USD 50% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.50 | +9.96% | 5 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| VWAP reversion | SQQQ | 1.91 | +6.52% | 4 |
| MFI reversion | SQQQ | 1.88 | +4.84% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.65 | -1.35 | 126 | 46.0 | -12.77 | -3.05 | -13.66 | 148 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.31 | 2.75 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.33 | -4.62 | -10.32 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.43 | -0.39 | -9.06 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -14.27 | -5.43 | -17.86 | 78 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.48 | -5.32 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -12.86 | -3.08 | -15.96 | 62 |
| 23 | Daily: Bullish score | daily | 88.75 | -11.25 | 15 | 20.0 | -5.01 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.82 | -3.41 | -14.68 | 84 |
| 25 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -13.73 | -7.22 | -13.74 | 198 |
| 26 | Hold BTC | benchmark | 86.96 | -13.04 | 1 | 0.0 | -6.19 | -0.78 | -15.15 | 1 |
| 27 | Parabolic SAR · 1h | trend | 86.90 | -13.10 | 166 | 27.1 | -12.89 | -2.83 | -20.50 | 234 |
| 28 | Donchian 55/20 · 1h | breakout | 85.94 | -14.06 | 71 | 14.1 | -12.75 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 85.15 | -14.85 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -16.81 | -4.87 | -18.51 | 94 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 81.95 | -18.05 | 264 | 46.6 | -25.39 | -3.76 | -29.25 | 392 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -21.90 | -4.53 | -24.50 | 171 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 78.98 | -21.02 | 177 | 18.1 | -24.68 | -4.14 | -27.31 | 264 |
| 38 | Ichimoku · 1h | trend | 77.87 | -22.12 | 94 | 14.9 | -22.75 | -4.65 | -29.43 | 124 |
| 39 | MFI reversion · 1h | reversion | 77.30 | -22.70 | 341 | 33.7 | -18.48 | -2.72 | -19.77 | 154 |
| 40 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.32 | -4.85 | -27.58 | 246 |
| 41 | CCI reversion · 1h | reversion | 76.25 | -23.75 | 300 | 44.3 | -29.15 | -4.77 | -29.68 | 460 |
| 42 | EMA 20/50 cross · 1h | trend | 76.07 | -23.93 | 102 | 10.8 | -21.87 | -3.93 | -30.58 | 127 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -42.78 | -9.03 | -42.80 | 675 |
| 44 | MACD zero-line · 1h | trend | 74.45 | -25.55 | 157 | 16.6 | -24.83 | -5.11 | -29.20 | 206 |
| 45 | Triple EMA stack · 1h | trend | 74.45 | -25.55 | 142 | 14.8 | -27.41 | -5.72 | -33.47 | 200 |
| 46 | Supertrend · 1h | trend | 73.62 | -26.38 | 166 | 13.3 | -29.11 | -5.03 | -34.80 | 213 |
| 47 | RSI momentum · 1h | momentum | 73.46 | -26.54 | 158 | 12.7 | -26.43 | -5.01 | -32.60 | 214 |
| 48 | Z-score reversion · 1h | reversion | 72.63 | -27.37 | 166 | 34.9 | -24.35 | -3.64 | -27.66 | 224 |
| 49 | Bollinger reversion · 1h | reversion | 72.59 | -27.41 | 258 | 39.1 | -30.13 | -5.16 | -32.89 | 367 |
| 50 | MACD cross · 1h | trend | 72.47 | -27.52 | 348 | 22.7 | -34.36 | -6.06 | -39.27 | 479 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -35.95 | -5.77 | -37.43 | 534 |
| 52 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.90 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.46 | -28.54 | 141 | 19.9 | -29.72 | -5.50 | -34.69 | 211 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -27.98 | -5.85 | -33.91 | 278 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -37.67 | -7.31 | -38.98 | 379 |
| 56 | EMA 9/21 cross · 1h | trend | 66.69 | -33.31 | 246 | 9.8 | -38.67 | -7.96 | -39.17 | 331 |
| 57 | VWAP momentum · 1h | momentum | 66.35 | -33.65 | 795 | 21.6 | -54.16 | -11.97 | -54.20 | 1232 |
| 58 | Agent (ML meta-label) | meta | 66.29 | -33.71 | 1542 | 23.0 | -8.92 | -1.53 | -17.09 | 338 |
| 59 | RSI(14) reversion · 1h | reversion | 65.62 | -34.38 | 148 | 27.0 | -29.58 | -4.67 | -31.98 | 219 |
| 60 | Candlestick reversal · 1h | reversion | 64.86 | -35.14 | 422 | 28.0 | -38.85 | -7.19 | -38.85 | 582 |
| 61 | Three white soldiers | momentum | 62.81 | -37.19 | 486 | 15.0 | -49.32 | -23.18 | -49.32 | 654 |
| 62 | Max aggression: 1-day momentum | meta | 62.21 | -37.79 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -46.43 | -98.97 | 5248 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.42 | -26.16 | -80.45 | 1427 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.43 | -47.31 | -93.43 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.11 | -32.24 | -89.11 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.90 | -40.15 | -90.90 | 2310 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.40 | -32.88 | -90.41 | 2207 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -55.57 | -97.72 | 3474 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -57.35 | -96.35 | 3413 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.57 | -32.56 | -93.61 | 2428 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.26 | -34.94 | -82.29 | 1650 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -56.09 | -99.53 | 5999 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.63 | -44.52 | -92.63 | 2600 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.80 | -39.03 | -95.80 | 3430 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.12 | -99.80 | 6189 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.73 | -43.84 | -91.74 | 2272 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.38 | -24.67 | -75.38 | 1566 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -64.56 | -97.77 | 3514 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -64.04 | -98.83 | 4894 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.54 | -29.25 | -69.54 | 1196 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -55.20 | -94.66 | 2744 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.77 | -37.37 | -84.77 | 1760 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.03 | -99.65 | 6390 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.54 | -32.35 | -89.54 | 2303 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.21 | -20.03 | -78.23 | 1755 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.85 | -37.65 | -90.85 | 2220 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.77 | -53.01 | -96.77 | 3905 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -57.69 | -89.36 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.90 | -28.78 | -65.90 | 802 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.60 | -24.41 | -72.60 | 1255 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.01 | -18.56 | -79.08 | 1680 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.32 | -50.94 | -97.33 | 4340 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -120.22 | -99.93 | 8295 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-08T22:00 | Agent (ML meta-label) | buy | ETH-USD | 3.90 | — | entry |
| 2026-11-08T22:00 | MFI reversion · 1h | sell | BTC-USD | 12.74 | -0.24 | stop-loss |
| 2026-11-08T22:00 | Stochastic reversion · 1h | buy | ETH-USD | 2.23 | — | entry signal |
| 2026-11-08T21:55 | MFI reversion · 1h | buy | BTC-USD | 5.85 | — | rebalance up |
| 2026-11-08T21:55 | MFI reversion · 1h | sell | SOL-USD | 6.89 | -0.22 | stop-loss |
| 2026-11-08T21:55 | MFI reversion · 1h | sell | ETH-USD | 6.93 | -0.20 | stop-loss |
| 2026-11-08T21:55 | MFI reversion · 1h | sell | DOGE-USD | 8.32 | -0.35 | stop-loss |
| 2026-11-08T21:55 | Z-score reversion · 1h | sell | SOL-USD | 4.98 | -0.14 | stop-loss |
| 2026-11-08T21:55 | Z-score reversion · 1h | sell | DOGE-USD | 4.08 | -0.17 | stop-loss |
| 2026-11-08T21:55 | RSI(14) reversion · 1h | sell | SOL-USD | 4.23 | -0.12 | stop-loss |
| 2026-11-08T21:55 | RSI(14) reversion · 1h | sell | ETH-USD | 4.31 | -0.16 | stop-loss |
| 2026-11-08T21:55 | RSI(14) reversion · 1h | sell | DOGE-USD | 4.21 | -0.18 | stop-loss |
| 2026-11-08T21:50 | CCI reversion · 1h | sell | ETH-USD | 2.24 | -0.04 | stop-loss |
| 2026-11-08T21:50 | CCI reversion · 1h | sell | DOGE-USD | 3.95 | -0.07 | stop-loss |
| 2026-11-08T21:50 | CCI reversion · 1h | sell | BTC-USD | 3.59 | -0.05 | stop-loss |
| 2026-11-08T21:50 | Stochastic reversion · 1h | sell | XRP-USD | 2.23 | -0.05 | stop-loss |
| 2026-11-08T21:50 | Bollinger reversion · 1h | sell | XRP-USD | 5.93 | -0.13 | stop-loss |
| 2026-11-08T21:50 | RSI(14) reversion · 1h | sell | XRP-USD | 4.03 | -0.10 | stop-loss |
| 2026-11-08T21:50 | Candlestick reversal · 1h | sell | ETH-USD | 5.34 | -0.07 | stop-loss |
| 2026-11-08T21:50 | Candlestick reversal · 1h | sell | DOGE-USD | 3.90 | -0.06 | stop-loss |
| 2026-11-08T21:50 | MACD cross · 1h | sell | SOL-USD | 4.76 | -0.10 | stop-loss |
| 2026-11-08T21:50 | MACD cross · 1h | sell | DOGE-USD | 4.77 | -0.09 | stop-loss |
| 2026-11-08T21:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.31 | -0.08 | exit signal |
| 2026-11-08T21:00 | MACD zero-line · 1h | sell | BTC-USD | 18.49 | -0.16 | exit signal |
| 2026-11-08T21:00 | MACD cross · 1h | sell | BTC-USD | 4.81 | -0.04 | exit signal |
| 2026-11-08T21:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 16.57 | -0.14 | exit signal |
| 2026-11-08T20:00 | MACD zero-line · 1h | buy | BTC-USD | 18.65 | — | entry signal |
| 2026-11-08T20:00 | MACD cross · 1h | sell | XRP-USD | 4.80 | -0.05 | exit signal |
| 2026-11-08T19:30 | Agent (ML meta-label) | sell | XRP-USD | 3.30 | -0.02 | selected signal exited |
| 2026-11-08T19:21 | Agent (ML meta-label) | buy | XRP-USD | 3.32 | — | entry |
| 2026-11-08T19:00 | CCI reversion · 1h | buy | ETH-USD | 2.27 | — | entry signal |
| 2026-11-08T19:00 | CCI reversion · 1h | buy | BTC-USD | 3.64 | — | entry signal |
| 2026-11-08T19:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.38 | — | entry signal |
| 2026-11-08T19:00 | MACD cross · 1h | buy | XRP-USD | 4.85 | — | entry signal |
| 2026-11-08T19:00 | MACD cross · 1h | buy | BTC-USD | 4.85 | — | entry signal |
| 2026-11-08T19:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 16.71 | — | entry signal |
| 2026-11-08T19:00 | Three white soldiers | sell | SOL-USD | 15.66 | -0.11 | exit signal |
| 2026-11-08T18:30 | Three white soldiers | sell | XRP-USD | 15.62 | -0.14 | stop-loss |
| 2026-11-08T18:20 | Three white soldiers | buy | XRP-USD | 15.77 | — | entry signal |
| 2026-11-08T18:20 | Three white soldiers | buy | SOL-USD | 15.77 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-10 22:15:05.000164+00:00 -> 2026-11-08 22:25:05.000164+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-10 22:15:05.000164+00:00 -> 2026-11-08 22:25:05.000164+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-10 22:15:05.000164+00:00 -> 2026-11-08 22:25:05.000164+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
