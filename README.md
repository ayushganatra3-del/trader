# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T18:50:05.000137+00:00 · 67178 ticks

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

Today: 30849 decisions in 2895 calls, $0.3870 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T18:50 | 3 / 19 / 8 | cash |  |
| Breezy | 2026-11-20T18:50 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-20T18:50 | 5 / 24 / 1 | COIN 51% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 1.96 | +18.20% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 122.92 | 22.92 | 26 | 65.4 | 25.99 | 4.22 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.51 | 14.51 | 0 | — | 12.37 | 4.15 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.76 | 4.76 | 40 | 42.5 | 2.85 | 0.71 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 102.07 | 2.07 | 0 | — | 3.02 | 0.90 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.19 | -0.81 | 203 | 31.5 | 0.05 | 0.10 | -9.06 | 202 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 96.13 | -3.87 | 212 | 28.8 | -0.77 | -0.19 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 92.05 | -7.95 | 0 | — | -9.00 | -2.98 | -10.45 | 1 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.97 | -4.39 | -10.76 | 44 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Bullish score | daily | 89.88 | -10.12 | 19 | 15.8 | -12.39 | -3.09 | -19.56 | 14 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.32 | -10.68 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | VWAP reversion · 1h | reversion | 88.23 | -11.77 | 156 | 45.5 | -13.83 | -4.05 | -18.66 | 152 |
| 19 | Copy: Insider buying | copy | 87.86 | -12.14 | 56 | 39.3 | -7.38 | -1.42 | -14.79 | 66 |
| 20 | Copy: Congress Democrats (NANC) | copy | 87.50 | -12.50 | 0 | — | -13.18 | -3.63 | -15.78 | 1 |
| 21 | Squeeze breakout · 1h | breakout | 87.43 | -12.57 | 70 | 20.0 | -17.87 | -8.64 | -18.95 | 72 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.40 | -13.60 | 451 | 33.5 | -11.58 | -3.85 | -14.87 | 552 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -16.71 | -1.49 | -23.32 | 6 |
| 25 | Parabolic SAR · 1h | trend | 83.84 | -16.16 | 194 | 27.8 | -24.11 | -6.82 | -28.66 | 195 |
| 26 | Donchian 55/20 · 1h | breakout | 80.89 | -19.11 | 79 | 12.7 | -24.80 | -7.29 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 80.74 | -19.27 | 163 | 28.8 | -16.04 | -5.47 | -21.55 | 75 |
| 28 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -20.05 | -5.59 | -20.74 | 205 |
| 29 | Connors RSI(2) · 1h | reversion | 79.91 | -20.09 | 218 | 40.4 | -15.47 | -6.99 | -15.48 | 71 |
| 30 | Keltner breakout · 1h | breakout | 79.60 | -20.40 | 126 | 26.2 | -21.62 | -5.83 | -25.34 | 146 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -16.08 | -4.16 | -19.15 | 97 |
| 32 | Opening range 15m | breakout | 76.81 | -23.19 | 561 | 31.0 | -21.84 | -6.74 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 75.87 | -24.13 | 107 | 14.0 | -28.78 | -8.22 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 73.95 | -26.05 | 228 | 20.2 | -25.57 | -3.80 | -35.87 | 273 |
| 35 | Triple EMA stack · 1h | trend | 72.11 | -27.89 | 161 | 14.3 | -32.87 | -8.11 | -37.24 | 170 |
| 36 | Bollinger breakout · 1h | breakout | 72.09 | -27.91 | 195 | 21.5 | -32.00 | -8.24 | -36.32 | 217 |
| 37 | Supertrend · 1h | trend | 72.02 | -27.98 | 198 | 16.7 | -34.25 | -6.86 | -37.64 | 199 |
| 38 | EMA 20/50 cross · 1h | trend | 71.77 | -28.23 | 119 | 10.1 | -36.44 | -10.39 | -40.64 | 122 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 71.22 | -28.78 | 2 | 0.0 | -27.72 | -3.99 | -30.97 | 1 |
| 40 | Heikin-Ashi · 1h | trend | 70.15 | -29.85 | 483 | 23.0 | -44.56 | -9.47 | -47.85 | 616 |
| 41 | Max aggression: 1-day momentum | meta | 69.89 | -30.11 | 33 | 27.3 | -51.07 | -3.62 | -58.27 | 39 |
| 42 | RSI momentum · 1h | momentum | 69.83 | -30.17 | 184 | 14.1 | -37.61 | -8.26 | -41.77 | 202 |
| 43 | OBV trend · 1h | momentum | 69.80 | -30.20 | 315 | 19.4 | -38.57 | -10.26 | -41.25 | 240 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -51.42 | -3.51 | -60.06 | 22 |
| 46 | Hold BTC ⏸ | benchmark | 68.38 | -31.62 | 3 | 0.0 | -28.62 | -4.56 | -33.27 | 1 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -41.40 | -6.07 | -42.11 | 442 |
| 49 | Donchian 20/10 · 1h | breakout | 66.53 | -33.47 | 165 | 17.6 | -35.34 | -6.59 | -43.26 | 192 |
| 50 | ROC + volume · 1h | momentum | 65.65 | -34.35 | 431 | 27.6 | -34.65 | -6.19 | -41.19 | 336 |
| 51 | MFI reversion · 1h | reversion | 65.26 | -34.74 | 475 | 33.1 | -34.97 | -5.25 | -36.49 | 171 |
| 52 | EMA 9/21 cross · 1h | trend | 63.99 | -36.01 | 291 | 11.3 | -39.30 | -7.38 | -47.32 | 323 |
| 53 | CCI reversion · 1h | reversion | 62.96 | -37.04 | 407 | 41.0 | -46.48 | -7.67 | -47.60 | 479 |
| 54 | MACD cross · 1h | trend | 62.41 | -37.59 | 444 | 20.9 | -50.16 | -9.96 | -51.01 | 496 |
| 55 | Bollinger reversion · 1h | reversion | 59.02 | -40.98 | 367 | 37.3 | -43.10 | -6.61 | -43.74 | 428 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -51.54 | -8.57 | -52.29 | 582 |
| 57 | Agent (ML meta-label) | meta | 56.22 | -43.78 | 2004 | 24.7 | -23.68 | -4.36 | -26.34 | 296 |
| 58 | RSI(14) reversion · 1h | reversion | 55.77 | -44.23 | 224 | 33.0 | -42.09 | -6.11 | -45.67 | 272 |
| 59 | VWAP momentum · 1h | momentum | 54.58 | -45.42 | 1013 | 21.4 | -56.13 | -11.24 | -60.51 | 1192 |
| 60 | Z-score reversion · 1h ⏸ | reversion | 52.10 | -47.90 | 242 | 33.1 | -43.27 | -6.02 | -45.67 | 265 |
| 61 | Three white soldiers | momentum | 51.81 | -48.19 | 617 | 14.1 | -51.82 | -23.36 | -52.17 | 662 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -52.44 | -9.56 | -52.62 | 679 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -47.56 | -99.15 | 5333 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.55 | -30.58 | -84.01 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.92 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.28 | -34.20 | -91.37 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.13 | -45.00 | -92.27 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -28.78 | -90.21 | 2024 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.25 | -50.34 | -98.25 | 3491 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -52.04 | -96.85 | 3391 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.82 | -40.75 | -93.92 | 2205 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.61 | -35.82 | -83.61 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.18 | -99.67 | 6335 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.05 | -46.06 | -93.05 | 2532 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.50 | -94.63 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -74.05 | -99.84 | 6276 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.52 | -46.80 | -93.52 | 2287 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.98 | -26.80 | -78.98 | 1641 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.83 | -60.95 | -97.83 | 3381 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -59.69 | -99.15 | 5092 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.05 | -29.85 | -71.05 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.01 | -56.29 | -95.01 | 2721 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.72 | -39.47 | -85.94 | 1704 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -73.47 | -99.73 | 6542 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -32.08 | -91.57 | 2463 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.59 | -19.67 | -81.62 | 1930 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.40 | -35.93 | -92.41 | 2201 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.86 | -48.06 | -97.88 | 4025 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.47 | -53.92 | -90.47 | 2191 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.28 | -32.10 | -67.38 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.03 | -28.27 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.77 | -19.17 | -83.77 | 1834 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.77 | -47.32 | -97.77 | 4429 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -117.43 | -99.95 | 8424 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-20T17:45 | Agent (ML meta-label) | sell | AMD | 2.89 | 0.01 | rebalance down |
| 2026-11-20T17:45 | Z-score reversion · 1h | sell | LABU | 10.54 | -0.71 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 18:50:05.000137+00:00 -> 2026-11-20 19:00:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
