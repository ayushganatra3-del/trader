# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T19:50:05.000160+00:00 · 67233 ticks

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

Today: 35826 decisions in 3060 calls, $0.4453 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T19:50 | 3 / 23 / 4 | cash |  |
| Breezy | 2026-11-20T19:50 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-20T19:50 | 7 / 23 / 0 | COIN 60% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 125.22 | 25.22 | 26 | 65.4 | 28.29 | 4.48 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.07 | 14.07 | 0 | — | 11.89 | 3.98 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.73 | 6.73 | 40 | 42.5 | 4.74 | 1.02 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 102.07 | 2.07 | 0 | — | 2.98 | 0.89 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.68 | -0.32 | 203 | 31.5 | 0.51 | 0.25 | -9.06 | 202 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 96.89 | -3.11 | 212 | 28.8 | -0.01 | 0.08 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 91.47 | -8.53 | 0 | — | -9.62 | -3.11 | -11.25 | 1 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.05 | -4.45 | -10.84 | 44 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Bullish score | daily | 90.32 | -9.68 | 19 | 15.8 | -11.99 | -2.94 | -19.56 | 14 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.35 | -10.65 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | Copy: Insider buying | copy | 87.92 | -12.08 | 56 | 39.3 | -7.64 | -1.48 | -14.79 | 66 |
| 19 | Squeeze breakout · 1h | breakout | 87.85 | -12.14 | 70 | 20.0 | -17.49 | -8.21 | -18.95 | 72 |
| 20 | VWAP reversion · 1h | reversion | 87.65 | -12.35 | 157 | 45.2 | -14.42 | -4.17 | -19.34 | 152 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Copy: Congress Democrats (NANC) | copy | 86.94 | -13.06 | 0 | — | -13.77 | -3.72 | -16.19 | 1 |
| 23 | Opening range 30m | breakout | 86.82 | -13.18 | 451 | 33.5 | -11.17 | -3.69 | -14.87 | 552 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -18.51 | -1.65 | -25.53 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.28 | -15.72 | 194 | 27.8 | -24.53 | -6.82 | -28.86 | 196 |
| 26 | Donchian 55/20 · 1h | breakout | 81.30 | -18.70 | 79 | 12.7 | -24.45 | -7.03 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.13 | -18.87 | 163 | 28.8 | -15.65 | -5.25 | -21.55 | 75 |
| 28 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -20.32 | -5.60 | -20.81 | 210 |
| 29 | Keltner breakout · 1h | breakout | 79.99 | -20.01 | 126 | 26.2 | -21.26 | -5.67 | -25.34 | 146 |
| 30 | Connors RSI(2) · 1h | reversion | 79.91 | -20.09 | 218 | 40.4 | -15.47 | -6.99 | -15.58 | 71 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -16.10 | -4.16 | -19.15 | 98 |
| 32 | Opening range 15m | breakout | 77.18 | -22.82 | 561 | 31.0 | -21.48 | -6.62 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.27 | -23.73 | 107 | 14.0 | -28.46 | -7.96 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.27 | -25.73 | 228 | 20.2 | -25.51 | -3.85 | -35.87 | 273 |
| 35 | Bollinger breakout · 1h | breakout | 72.46 | -27.54 | 195 | 21.5 | -31.69 | -8.03 | -36.32 | 217 |
| 36 | Triple EMA stack · 1h | trend | 72.44 | -27.56 | 161 | 14.3 | -32.37 | -7.82 | -37.24 | 170 |
| 37 | Supertrend · 1h | trend | 72.40 | -27.61 | 198 | 16.7 | -33.95 | -6.72 | -37.64 | 199 |
| 38 | EMA 20/50 cross · 1h | trend | 72.11 | -27.89 | 119 | 10.1 | -36.14 | -10.11 | -40.64 | 122 |
| 39 | Max aggression: 1-day momentum | meta | 71.20 | -28.80 | 33 | 27.3 | -50.18 | -3.54 | -58.27 | 39 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 70.89 | -29.11 | 2 | 0.0 | -28.08 | -4.03 | -31.59 | 1 |
| 41 | Heikin-Ashi · 1h | trend | 70.51 | -29.49 | 483 | 23.0 | -44.36 | -9.33 | -47.85 | 616 |
| 42 | RSI momentum · 1h | momentum | 70.20 | -29.80 | 184 | 14.1 | -37.37 | -8.12 | -41.77 | 202 |
| 43 | OBV trend · 1h | momentum | 70.11 | -29.89 | 316 | 19.6 | -40.82 | -11.78 | -41.14 | 239 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -50.54 | -3.38 | -60.06 | 22 |
| 46 | Hold BTC ⏸ | benchmark | 68.38 | -31.62 | 3 | 0.0 | -28.06 | -4.53 | -33.67 | 1 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -42.00 | -6.07 | -43.32 | 442 |
| 49 | Donchian 20/10 · 1h | breakout | 66.87 | -33.13 | 165 | 17.6 | -35.04 | -6.47 | -43.26 | 192 |
| 50 | ROC + volume · 1h | momentum | 65.97 | -34.03 | 431 | 27.6 | -34.34 | -6.08 | -41.19 | 337 |
| 51 | MFI reversion · 1h ⏸ | reversion | 64.95 | -35.05 | 476 | 33.0 | -35.20 | -5.27 | -36.76 | 172 |
| 52 | EMA 9/21 cross · 1h | trend | 64.33 | -35.67 | 291 | 11.3 | -39.03 | -7.26 | -47.32 | 323 |
| 53 | CCI reversion · 1h | reversion | 62.82 | -37.18 | 408 | 40.9 | -46.60 | -7.67 | -47.70 | 479 |
| 54 | MACD cross · 1h | trend | 62.67 | -37.33 | 444 | 20.9 | -49.93 | -9.94 | -51.01 | 496 |
| 55 | Bollinger reversion · 1h ⏸ | reversion | 58.24 | -41.76 | 377 | 36.6 | -43.46 | -6.63 | -44.54 | 430 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -51.93 | -8.54 | -52.74 | 582 |
| 57 | Agent (ML meta-label) | meta | 55.93 | -44.07 | 2004 | 24.7 | -25.83 | -4.70 | -28.83 | 308 |
| 58 | RSI(14) reversion · 1h | reversion | 55.67 | -44.33 | 224 | 33.0 | -42.29 | -6.14 | -45.87 | 271 |
| 59 | VWAP momentum · 1h | momentum | 54.91 | -45.09 | 1013 | 21.4 | -55.93 | -11.16 | -60.51 | 1192 |
| 60 | Z-score reversion · 1h ⏸ | reversion | 52.10 | -47.90 | 242 | 33.1 | -43.55 | -6.03 | -45.98 | 265 |
| 61 | Three white soldiers | momentum | 51.81 | -48.19 | 617 | 14.1 | -51.87 | -23.32 | -52.21 | 663 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -52.90 | -9.52 | -53.22 | 679 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -47.63 | -99.14 | 5327 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.52 | -30.59 | -84.01 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.39 | -46.97 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.28 | -34.20 | -91.37 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.04 | -44.88 | -92.21 | 2291 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.95 | -28.53 | -90.21 | 2024 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.26 | -49.97 | -98.26 | 3491 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -51.85 | -96.87 | 3390 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.80 | -40.27 | -93.93 | 2204 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.60 | -35.81 | -83.61 | 1579 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -56.85 | -99.67 | 6357 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.22 | -44.41 | -93.23 | 2536 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.50 | -94.63 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -73.24 | -99.84 | 6284 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.53 | -46.76 | -93.53 | 2287 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.05 | -26.59 | -79.07 | 1639 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.86 | -97.83 | 3381 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -59.50 | -99.15 | 5120 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.09 | -29.84 | -71.12 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.10 | -54.81 | -95.10 | 2730 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.78 | -39.64 | -85.98 | 1706 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.74 | -72.97 | -99.74 | 6567 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.60 | -31.99 | -91.67 | 2482 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.09 | -19.48 | -82.23 | 1950 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.42 | -34.38 | -92.47 | 2206 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.88 | -47.52 | -97.89 | 4055 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.57 | -52.83 | -90.59 | 2206 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.28 | -32.10 | -67.38 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.91 | -27.93 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.91 | -19.12 | -84.01 | 1858 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.75 | -47.29 | -97.77 | 4452 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -117.43 | -99.95 | 8430 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | TNA | 6.39 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | SOL-USD | 6.44 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | PLTR | 6.48 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | MSTR | 6.46 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | MSFT | 6.55 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | IWM | 6.54 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | DOGE-USD | 5.81 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | COIN | 6.48 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | AMD | 6.41 | -0.18 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | VWAP momentum · 1h | sell | SQQQ | 2.76 | 0.48 | rebalance down |
| 2026-11-20T19:30 | CCI reversion · 1h | sell | GOOGL | 15.49 | -0.49 | stop-loss |
| 2026-11-20T19:30 | Bollinger reversion · 1h | buy | DOGE-USD | 5.85 | — | entry |
| 2026-11-20T19:30 | Bollinger reversion · 1h | sell | GOOGL | 6.53 | -0.21 | stop-loss |
| 2026-11-20T19:25 | MFI reversion · 1h | sell | DOGE-USD | 16.01 | -0.31 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:25 | OBV trend · 1h | sell | SQQQ | 19.95 | 3.23 | target is flat |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 19:50:05.000160+00:00 -> 2026-11-20 20:00:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
