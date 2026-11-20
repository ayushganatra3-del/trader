# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T18:20:05.000129+00:00 · 67152 ticks

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

Today: 28497 decisions in 2817 calls, $0.3595 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T18:20 | 9 / 20 / 1 | MSTR 16%, SOXL 14% |  |
| Breezy | 2026-11-20T18:20 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-20T18:20 | 9 / 21 / 0 | MSTR 78% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 122.12 | 22.12 | 26 | 65.4 | 25.19 | 4.11 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.59 | 14.59 | 0 | — | 12.47 | 4.18 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.08 | 4.08 | 40 | 42.5 | 2.20 | 0.59 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 102.25 | 2.25 | 0 | — | 3.22 | 0.96 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.02 | -0.98 | 203 | 31.5 | -0.11 | 0.05 | -9.06 | 202 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 95.87 | -4.13 | 212 | 28.8 | -1.03 | -0.29 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 92.17 | -7.83 | 0 | — | -8.87 | -2.95 | -10.45 | 1 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.97 | -4.39 | -10.76 | 44 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Bullish score | daily | 89.72 | -10.28 | 19 | 15.8 | -12.53 | -3.15 | -19.56 | 14 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.30 | -10.70 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | VWAP reversion · 1h | reversion | 88.79 | -11.21 | 156 | 45.5 | -13.27 | -3.91 | -18.57 | 152 |
| 19 | Copy: Insider buying | copy | 87.98 | -12.03 | 55 | 40.0 | -7.85 | -1.52 | -14.79 | 66 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 21 | Squeeze breakout · 1h | breakout | 87.28 | -12.72 | 70 | 20.0 | -18.00 | -8.79 | -18.95 | 72 |
| 22 | Copy: Congress Democrats (NANC) | copy | 87.10 | -12.90 | 0 | — | -13.56 | -3.69 | -15.78 | 1 |
| 23 | Opening range 30m | breakout | 86.25 | -13.74 | 451 | 33.5 | -11.72 | -3.91 | -14.87 | 552 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -16.35 | -1.45 | -23.32 | 6 |
| 25 | Parabolic SAR · 1h | trend | 83.68 | -16.32 | 194 | 27.8 | -25.00 | -7.14 | -28.86 | 196 |
| 26 | Donchian 55/20 · 1h | breakout | 80.74 | -19.26 | 79 | 12.7 | -25.24 | -7.47 | -28.01 | 81 |
| 27 | Volume breakout · 1h | breakout | 80.60 | -19.40 | 163 | 28.8 | -15.58 | -4.98 | -21.55 | 74 |
| 28 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -19.51 | -5.73 | -20.19 | 205 |
| 29 | Connors RSI(2) · 1h | reversion | 79.94 | -20.06 | 218 | 40.4 | -15.42 | -6.97 | -15.43 | 71 |
| 30 | Keltner breakout · 1h | breakout | 79.47 | -20.53 | 126 | 26.2 | -21.90 | -5.98 | -25.34 | 145 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -15.89 | -4.11 | -18.95 | 94 |
| 32 | Opening range 15m | breakout | 76.68 | -23.32 | 561 | 31.0 | -21.96 | -6.78 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 75.73 | -24.27 | 107 | 14.0 | -28.90 | -8.31 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 73.83 | -26.17 | 228 | 20.2 | -25.97 | -3.95 | -35.87 | 273 |
| 35 | Triple EMA stack · 1h | trend | 71.99 | -28.01 | 161 | 14.3 | -32.98 | -8.17 | -37.24 | 170 |
| 36 | Bollinger breakout · 1h | breakout | 71.96 | -28.04 | 195 | 21.5 | -31.18 | -7.65 | -36.32 | 216 |
| 37 | Supertrend · 1h | trend | 71.88 | -28.12 | 198 | 16.7 | -34.35 | -6.91 | -37.64 | 199 |
| 38 | EMA 20/50 cross · 1h | trend | 71.65 | -28.35 | 119 | 10.1 | -36.54 | -10.48 | -40.64 | 122 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 71.22 | -28.78 | 2 | 0.0 | -27.71 | -3.99 | -30.97 | 1 |
| 40 | Heikin-Ashi · 1h | trend | 70.02 | -29.98 | 483 | 23.0 | -44.65 | -9.53 | -47.85 | 616 |
| 41 | RSI momentum · 1h | momentum | 69.71 | -30.29 | 184 | 14.1 | -37.71 | -8.32 | -41.77 | 202 |
| 42 | OBV trend · 1h | momentum | 69.67 | -30.33 | 315 | 19.4 | -38.67 | -10.35 | -41.25 | 240 |
| 43 | Hold BTC | benchmark | 69.49 | -30.51 | 2 | 0.0 | -27.73 | -4.47 | -32.58 | 1 |
| 44 | Max aggression: 1-day momentum | meta | 69.44 | -30.57 | 33 | 27.3 | -51.40 | -3.64 | -58.28 | 39 |
| 45 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 46 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -51.73 | -3.55 | -60.06 | 22 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -40.93 | -6.06 | -42.08 | 437 |
| 49 | Donchian 20/10 · 1h | breakout | 66.41 | -33.59 | 165 | 17.6 | -35.44 | -6.63 | -43.26 | 192 |
| 50 | ROC + volume · 1h | momentum | 65.54 | -34.46 | 431 | 27.6 | -34.90 | -6.31 | -41.19 | 336 |
| 51 | MFI reversion · 1h | reversion | 65.26 | -34.74 | 475 | 33.1 | -34.97 | -5.25 | -36.49 | 171 |
| 52 | EMA 9/21 cross · 1h | trend | 63.87 | -36.13 | 291 | 11.3 | -39.40 | -7.42 | -47.32 | 323 |
| 53 | CCI reversion · 1h | reversion | 63.01 | -36.99 | 406 | 41.1 | -46.42 | -7.67 | -47.57 | 479 |
| 54 | MACD cross · 1h | trend | 62.32 | -37.68 | 444 | 20.9 | -50.24 | -9.96 | -51.01 | 496 |
| 55 | Bollinger reversion · 1h | reversion | 59.36 | -40.63 | 366 | 37.4 | -42.76 | -6.58 | -43.69 | 422 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -51.23 | -8.59 | -52.11 | 582 |
| 57 | Agent (ML meta-label) | meta | 56.71 | -43.29 | 2004 | 24.7 | -27.14 | -4.97 | -30.21 | 298 |
| 58 | RSI(14) reversion · 1h | reversion | 55.87 | -44.13 | 224 | 33.0 | -41.86 | -6.07 | -45.67 | 272 |
| 59 | VWAP momentum · 1h | momentum | 54.47 | -45.52 | 1013 | 21.4 | -56.20 | -11.27 | -60.51 | 1192 |
| 60 | Z-score reversion · 1h ⏸ | reversion | 52.10 | -47.90 | 242 | 33.1 | -43.20 | -6.01 | -45.65 | 264 |
| 61 | Three white soldiers | momentum | 52.03 | -47.98 | 616 | 14.1 | -51.64 | -23.32 | -51.98 | 661 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -52.17 | -9.57 | -52.53 | 678 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -47.44 | -99.16 | 5336 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.51 | -30.54 | -84.01 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.86 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.28 | -34.20 | -91.37 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.15 | -45.01 | -92.26 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -28.78 | -90.21 | 2023 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.23 | -50.87 | -98.23 | 3487 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.83 | -52.19 | -96.84 | 3389 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.82 | -40.87 | -93.91 | 2204 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.61 | -35.82 | -83.61 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -57.77 | -99.67 | 6324 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.99 | -46.32 | -93.05 | 2532 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.50 | -94.63 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -74.44 | -99.84 | 6276 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.48 | -47.20 | -93.48 | 2285 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.73 | -27.21 | -78.73 | 1637 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.83 | -60.95 | -97.83 | 3381 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -59.87 | -99.15 | 5091 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.92 | -29.85 | -70.92 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.95 | -56.67 | -94.96 | 2719 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.72 | -39.43 | -85.94 | 1704 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -73.84 | -99.73 | 6541 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.50 | -32.20 | -91.56 | 2464 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.58 | -19.73 | -81.75 | 1929 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.24 | -36.58 | -92.30 | 2197 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.86 | -48.06 | -97.88 | 4024 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.36 | -54.54 | -90.38 | 2189 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.33 | -32.05 | -67.43 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.07 | -28.38 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.70 | -19.17 | -83.82 | 1837 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.75 | -47.55 | -97.76 | 4429 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.36 | -99.95 | 8421 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-20T17:45 | Z-score reversion · 1h | sell | GOOGL | 12.89 | -0.30 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T17:30 | Agent (ML meta-label) | buy | MSTR | 13.27 | — | entry |
| 2026-11-20T17:30 | Agent (ML meta-label) | buy | BITX | 14.15 | — | entry |
| 2026-11-20T17:30 | Agent (ML meta-label) | buy | AMD | 14.15 | — | entry |
| 2026-11-20T17:30 | Bollinger reversion · 1h | buy | MSTR | 14.79 | — | entry signal |
| 2026-11-20T17:30 | ADX DI cross · 1h | sell | GOOGL | 18.01 | -0.36 | exit signal |
| 2026-11-20T17:15 | Daily: Connors RSI(2) · 3x ETFs | sell | UPRO | 85.09 | -13.73 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T17:02 | Candlestick reversal · 1h | sell | GOOGL | 12.77 | -0.12 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T17:02 | Candlestick reversal · 1h | sell | DOGE-USD | 12.79 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T17:02 | Candlestick reversal · 1h | sell | BTC-USD | 12.79 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T17:00 | Agent (ML meta-label) | sell | AAPL | 14.15 | 0.04 | selected signal exited |
| 2026-11-20T17:00 | VWAP reversion · 1h | buy | XRP-USD | 22.29 | — | entry signal |
| 2026-11-20T17:00 | VWAP reversion · 1h | buy | DOGE-USD | 22.29 | — | entry signal |
| 2026-11-20T17:00 | VWAP reversion · 1h | buy | BTC-USD | 22.29 | — | entry signal |
| 2026-11-20T17:00 | RSI(14) reversion · 1h | buy | SOL-USD | 13.99 | — | entry signal |
| 2026-11-20T17:00 | Candlestick reversal · 1h | buy | DOGE-USD | 12.86 | — | entry signal |
| 2026-11-20T17:00 | Candlestick reversal · 1h | buy | BTC-USD | 12.86 | — | entry signal |
| 2026-11-20T16:55 | Agent (ML meta-label) | buy | AAPL | 14.11 | — | entry |
| 2026-11-20T16:55 | CCI reversion · 1h | sell | LABU | 15.42 | -0.91 | stop-loss |
| 2026-11-20T16:55 | RSI(14) reversion · 1h | sell | LABU | 13.86 | -0.78 | stop-loss |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | UPRO | 4.72 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | TQQQ | 4.67 | -0.24 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | TNA | 4.76 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | SPY | 4.85 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | SOXL | 4.46 | -0.45 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | QQQ | 4.83 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | PLTR | 4.80 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | NVDA | 4.81 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 18:20:05.000129+00:00 -> 2026-11-20 18:30:05.000129+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
