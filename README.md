# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T19:20:05.000124+00:00 · 67207 ticks

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
| Copy: Insider buying | 2026-11-20 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.48 · VIX 28.44 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 33468 decisions in 2982 calls, $0.4177 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T19:20 | 1 / 8 / 21 | cash |  |
| Breezy | 2026-11-20T19:20 | 0 / 21 / 9 | cash |  |
| Boozy | 2026-11-20T19:20 | 1 / 20 / 9 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| MFI reversion | META | 2.04 | +2.40% | 6 |
| CCI reversion | SOXL | 1.96 | +18.20% | 16 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 124.57 | 24.57 | 26 | 65.4 | 27.68 | 4.42 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.16 | 14.15 | 0 | — | 12.02 | 4.03 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.17 | 6.17 | 40 | 42.5 | 4.23 | 0.94 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.94 | 1.94 | 0 | — | 2.89 | 0.87 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.54 | -0.46 | 203 | 31.5 | 0.39 | 0.21 | -9.06 | 202 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 96.67 | -3.33 | 212 | 28.8 | -0.21 | 0.01 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 91.68 | -8.32 | 0 | — | -9.37 | -3.06 | -10.74 | 1 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.05 | -4.45 | -10.84 | 44 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Bullish score | daily | 90.19 | -9.81 | 19 | 15.8 | -12.10 | -2.98 | -19.56 | 14 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.32 | -10.68 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | Copy: Insider buying | copy | 88.11 | -11.88 | 56 | 39.3 | -7.08 | -1.36 | -14.79 | 66 |
| 19 | Squeeze breakout · 1h | breakout | 87.73 | -12.27 | 70 | 20.0 | -17.59 | -8.33 | -18.95 | 72 |
| 20 | Copy: Congress Democrats (NANC) | copy | 87.62 | -12.38 | 0 | — | -13.06 | -3.61 | -15.78 | 1 |
| 21 | VWAP reversion · 1h | reversion | 87.59 | -12.41 | 157 | 45.2 | -14.46 | -4.18 | -19.25 | 152 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.70 | -13.30 | 451 | 33.5 | -11.28 | -3.74 | -14.87 | 552 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -17.71 | -1.58 | -24.00 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.15 | -15.85 | 194 | 27.8 | -24.62 | -6.88 | -28.86 | 196 |
| 26 | Donchian 55/20 · 1h | breakout | 81.18 | -18.82 | 79 | 12.7 | -24.54 | -7.10 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.02 | -18.98 | 163 | 28.8 | -15.76 | -5.31 | -21.55 | 75 |
| 28 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -20.25 | -5.61 | -20.81 | 209 |
| 29 | Connors RSI(2) · 1h | reversion | 79.88 | -20.12 | 218 | 40.4 | -15.49 | -7.00 | -15.51 | 71 |
| 30 | Keltner breakout · 1h | breakout | 79.88 | -20.12 | 126 | 26.2 | -21.79 | -5.97 | -25.34 | 146 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -16.10 | -4.16 | -19.15 | 98 |
| 32 | Opening range 15m | breakout | 77.08 | -22.92 | 561 | 31.0 | -21.57 | -6.65 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.16 | -23.84 | 107 | 14.0 | -28.54 | -8.03 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.18 | -25.82 | 228 | 20.2 | -25.61 | -3.87 | -35.87 | 273 |
| 35 | Bollinger breakout · 1h | breakout | 72.35 | -27.65 | 195 | 21.5 | -31.78 | -8.09 | -36.32 | 217 |
| 36 | Triple EMA stack · 1h | trend | 72.34 | -27.66 | 161 | 14.3 | -32.46 | -7.88 | -37.24 | 170 |
| 37 | Supertrend · 1h | trend | 72.29 | -27.71 | 198 | 16.7 | -34.03 | -6.76 | -37.64 | 199 |
| 38 | EMA 20/50 cross · 1h | trend | 72.01 | -27.99 | 119 | 10.1 | -36.22 | -10.19 | -40.64 | 122 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 70.92 | -29.08 | 2 | 0.0 | -28.03 | -4.02 | -31.13 | 1 |
| 40 | Max aggression: 1-day momentum | meta | 70.83 | -29.17 | 33 | 27.3 | -50.42 | -3.56 | -58.27 | 39 |
| 41 | Heikin-Ashi · 1h | trend | 70.41 | -29.59 | 483 | 23.0 | -44.37 | -9.36 | -47.85 | 616 |
| 42 | RSI momentum · 1h | momentum | 70.09 | -29.91 | 184 | 14.1 | -37.44 | -8.16 | -41.77 | 202 |
| 43 | OBV trend · 1h | momentum | 70.06 | -29.94 | 315 | 19.4 | -38.90 | -10.35 | -41.24 | 240 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -50.77 | -3.41 | -60.06 | 22 |
| 46 | Hold BTC ⏸ | benchmark | 68.38 | -31.62 | 3 | 0.0 | -29.02 | -4.58 | -33.67 | 1 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -42.06 | -6.07 | -42.77 | 442 |
| 49 | Donchian 20/10 · 1h | breakout | 66.77 | -33.23 | 165 | 17.6 | -35.12 | -6.50 | -43.26 | 192 |
| 50 | ROC + volume · 1h | momentum | 65.88 | -34.12 | 431 | 27.6 | -34.43 | -6.12 | -41.19 | 336 |
| 51 | MFI reversion · 1h | reversion | 65.03 | -34.97 | 475 | 33.1 | -35.21 | -5.27 | -36.72 | 172 |
| 52 | EMA 9/21 cross · 1h | trend | 64.23 | -35.77 | 291 | 11.3 | -39.10 | -7.29 | -47.32 | 323 |
| 53 | CCI reversion · 1h | reversion | 62.89 | -37.11 | 407 | 41.0 | -46.53 | -7.67 | -47.64 | 479 |
| 54 | MACD cross · 1h | trend | 62.60 | -37.41 | 444 | 20.9 | -49.99 | -9.95 | -51.01 | 496 |
| 55 | Bollinger reversion · 1h | reversion | 58.69 | -41.31 | 367 | 37.3 | -43.45 | -6.63 | -44.09 | 429 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -51.95 | -8.53 | -52.69 | 582 |
| 57 | Agent (ML meta-label) | meta | 55.73 | -44.27 | 2004 | 24.7 | -25.94 | -4.59 | -28.19 | 298 |
| 58 | RSI(14) reversion · 1h | reversion | 55.57 | -44.43 | 224 | 33.0 | -42.39 | -6.16 | -45.87 | 271 |
| 59 | VWAP momentum · 1h | momentum | 54.79 | -45.20 | 1013 | 21.4 | -55.99 | -11.18 | -60.51 | 1192 |
| 60 | Z-score reversion · 1h ⏸ | reversion | 52.10 | -47.90 | 242 | 33.1 | -43.39 | -6.02 | -45.79 | 265 |
| 61 | Three white soldiers | momentum | 51.81 | -48.19 | 617 | 14.1 | -51.87 | -23.32 | -52.21 | 663 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -52.90 | -9.52 | -53.08 | 679 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -47.61 | -99.15 | 5331 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.55 | -30.58 | -84.01 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.41 | -46.94 | -94.42 | 2453 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.28 | -34.20 | -91.37 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.11 | -44.94 | -92.27 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.96 | -28.60 | -90.21 | 2024 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.26 | -49.97 | -98.26 | 3492 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -52.09 | -96.86 | 3391 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.82 | -40.33 | -93.94 | 2204 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.61 | -35.82 | -83.61 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -56.71 | -99.67 | 6342 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.23 | -44.39 | -93.23 | 2536 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.50 | -94.63 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -73.62 | -99.84 | 6276 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.53 | -46.76 | -93.53 | 2287 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.29 | -26.20 | -79.29 | 1642 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.83 | -60.96 | -97.84 | 3382 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -59.54 | -99.15 | 5096 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.05 | -29.85 | -71.05 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.10 | -54.68 | -95.10 | 2730 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.76 | -39.53 | -85.98 | 1705 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.74 | -73.00 | -99.74 | 6545 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.64 | -31.86 | -91.64 | 2463 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.88 | -19.50 | -81.88 | 1930 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.46 | -34.77 | -92.46 | 2197 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.89 | -47.48 | -97.89 | 4034 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.58 | -52.68 | -90.59 | 2206 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.22 | -32.14 | -67.31 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.95 | -28.03 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.96 | -19.10 | -83.96 | 1841 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.77 | -47.24 | -97.77 | 4436 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -117.43 | -99.95 | 8424 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T19:20 | VWAP reversion · 1h | sell | BTC-USD | 21.57 | -0.72 | stop-loss |
| 2026-11-20T19:00 | MFI reversion · 1h | buy | DOGE-USD | 16.32 | — | entry signal |
| 2026-11-20T18:50 | Hold BTC | sell | BTC-USD | 68.38 | -6.75 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T18:47 | Three white soldiers | sell | MSTR | 12.79 | -0.22 | stop-loss |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | TNA | 4.69 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | TECL | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | PLTR | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | LABU | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | ETHU | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | COIN | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | XRP-USD | 2.91 | -0.01 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | SQQQ | 6.57 | 0.60 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | SOL-USD | 4.70 | -0.02 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | MSTR | 4.78 | 0.07 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | BITX | 4.67 | -0.04 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | AMD | 4.71 | 0.02 | rebalance down |
| 2026-11-20T18:30 | Copy: Insider buying | buy | PSEC | 10.99 | — | entry |
| 2026-11-20T18:30 | Copy: Insider buying | sell | LRN | 11.19 | -0.41 | target is flat |
| 2026-11-20T18:30 | CCI reversion · 1h | sell | AAPL | 12.70 | -0.17 | stop-loss |
| 2026-11-20T18:30 | Bollinger reversion · 1h | buy | TNA | 6.55 | — | entry signal |
| 2026-11-20T18:30 | Bollinger reversion · 1h | buy | PLTR | 6.59 | — | entry signal |
| 2026-11-20T18:30 | Bollinger reversion · 1h | buy | MSFT | 6.59 | — | entry signal |
| 2026-11-20T18:30 | Bollinger reversion · 1h | buy | IWM | 6.59 | — | entry signal |
| 2026-11-20T18:30 | Bollinger reversion · 1h | buy | COIN | 6.59 | — | entry signal |
| 2026-11-20T18:30 | Bollinger reversion · 1h | buy | AMD | 6.59 | — | entry signal |
| 2026-11-20T18:30 | Bollinger reversion · 1h | sell | SOL-USD | 8.20 | -0.04 | rebalance down |
| 2026-11-20T18:30 | Bollinger reversion · 1h | sell | MSTR | 8.43 | 0.12 | rebalance down |
| 2026-11-20T18:30 | Bollinger reversion · 1h | sell | GOOGL | 8.02 | -0.18 | rebalance down |
| 2026-11-20T18:30 | Bollinger reversion · 1h | sell | AAPL | 12.05 | -0.17 | stop-loss |
| 2026-11-20T18:25 | Three white soldiers | buy | MSTR | 13.01 | — | entry signal |
| 2026-11-20T18:00 | Agent (ML meta-label) | buy | XRP-USD | 7.65 | — | entry |
| 2026-11-20T18:00 | Agent (ML meta-label) | buy | SOL-USD | 9.45 | — | entry |
| 2026-11-20T18:00 | Agent (ML meta-label) | sell | MSTR | 3.94 | 0.03 | rebalance down |
| 2026-11-20T18:00 | Agent (ML meta-label) | sell | BITX | 4.65 | -0.02 | rebalance down |
| 2026-11-20T18:00 | Agent (ML meta-label) | sell | AMD | 4.73 | 0.03 | rebalance down |
| 2026-11-20T18:00 | Bollinger reversion · 1h | buy | SOL-USD | 14.84 | — | entry signal |
| 2026-11-20T17:50 | Agent (ML meta-label) | buy | AMD | 2.83 | — | rebalance up |
| 2026-11-20T17:50 | Agent (ML meta-label) | sell | AAPL | 6.62 | -0.01 | selected signal exited |
| 2026-11-20T17:45 | Agent (ML meta-label) | buy | AAPL | 6.63 | — | entry |
| 2026-11-20T17:45 | Agent (ML meta-label) | sell | SQQQ | 3.74 | 0.34 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 19:20:05.000124+00:00 -> 2026-11-20 19:30:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
