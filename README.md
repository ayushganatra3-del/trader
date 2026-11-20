# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T17:20:05.000135+00:00 · 67095 ticks

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

Today: 23298 decisions in 2646 calls, $0.2986 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T17:20 | 1 / 17 / 12 | cash |  |
| Breezy | 2026-11-20T17:20 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-20T17:20 | 4 / 22 / 4 | COIN 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| CCI reversion | SOXL | 1.96 | +18.20% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 122.69 | 22.69 | 26 | 65.4 | 25.76 | 4.19 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.82 | 14.82 | 0 | — | 12.69 | 4.25 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.57 | 4.57 | 40 | 42.5 | 2.67 | 0.68 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 102.26 | 2.26 | 0 | — | 3.22 | 0.96 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.14 | -0.86 | 203 | 31.5 | -0.00 | 0.09 | -9.06 | 202 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 96.06 | -3.94 | 212 | 28.8 | -0.85 | -0.22 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 92.14 | -7.86 | 0 | — | -8.92 | -2.96 | -10.30 | 1 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.97 | -4.39 | -10.76 | 44 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Bullish score | daily | 89.83 | -10.17 | 19 | 15.8 | -12.43 | -3.11 | -19.56 | 14 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.31 | -10.69 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | Copy: Insider buying | copy | 88.50 | -11.50 | 55 | 40.0 | -7.46 | -1.44 | -14.79 | 66 |
| 19 | VWAP reversion · 1h | reversion | 88.47 | -11.53 | 156 | 45.5 | -13.59 | -4.00 | -18.52 | 152 |
| 20 | Copy: Congress Democrats (NANC) | copy | 87.75 | -12.25 | 0 | — | -12.93 | -3.58 | -15.38 | 1 |
| 21 | Squeeze breakout · 1h | breakout | 87.39 | -12.61 | 70 | 20.0 | -17.91 | -8.69 | -18.95 | 72 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.36 | -13.64 | 451 | 33.5 | -11.62 | -3.87 | -14.87 | 552 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -16.41 | -1.46 | -22.90 | 6 |
| 25 | Parabolic SAR · 1h | trend | 83.79 | -16.21 | 194 | 27.8 | -24.91 | -7.09 | -28.86 | 196 |
| 26 | Donchian 55/20 · 1h | breakout | 80.84 | -19.16 | 79 | 12.7 | -25.15 | -7.41 | -28.01 | 81 |
| 27 | Volume breakout · 1h | breakout | 80.70 | -19.30 | 163 | 28.8 | -15.47 | -4.91 | -21.55 | 74 |
| 28 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -20.37 | -5.50 | -20.59 | 208 |
| 29 | Connors RSI(2) · 1h | reversion | 79.94 | -20.06 | 218 | 40.4 | -15.42 | -6.97 | -15.42 | 71 |
| 30 | Keltner breakout · 1h | breakout | 79.56 | -20.44 | 126 | 26.2 | -21.17 | -5.62 | -25.34 | 143 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -24.12 | -4.43 | -24.28 | 99 |
| 32 | Opening range 15m | breakout | 76.77 | -23.23 | 561 | 31.0 | -21.88 | -6.75 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 75.83 | -24.17 | 107 | 14.0 | -28.82 | -8.25 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 73.93 | -26.07 | 227 | 20.3 | -26.07 | -3.97 | -35.87 | 274 |
| 35 | Triple EMA stack · 1h | trend | 72.07 | -27.93 | 161 | 14.3 | -33.54 | -8.43 | -36.70 | 170 |
| 36 | Bollinger breakout · 1h | breakout | 72.05 | -27.95 | 195 | 21.5 | -29.72 | -6.60 | -36.32 | 214 |
| 37 | Supertrend · 1h | trend | 71.98 | -28.02 | 198 | 16.7 | -34.28 | -6.87 | -37.64 | 199 |
| 38 | EMA 20/50 cross · 1h | trend | 71.73 | -28.27 | 119 | 10.1 | -36.47 | -10.42 | -40.64 | 122 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 71.43 | -28.57 | 2 | 0.0 | -27.50 | -3.97 | -30.97 | 1 |
| 40 | Heikin-Ashi · 1h | trend | 70.11 | -29.89 | 483 | 23.0 | -44.52 | -9.46 | -47.85 | 616 |
| 41 | RSI momentum · 1h | momentum | 69.80 | -30.20 | 184 | 14.1 | -37.68 | -8.30 | -41.77 | 202 |
| 42 | Hold BTC | benchmark | 69.80 | -30.20 | 2 | 0.0 | -27.45 | -4.44 | -32.36 | 1 |
| 43 | OBV trend · 1h | momentum | 69.76 | -30.24 | 315 | 19.4 | -38.19 | -10.17 | -41.17 | 240 |
| 44 | Max aggression: 1-day momentum | meta | 69.76 | -30.24 | 33 | 27.3 | -51.16 | -3.62 | -58.27 | 39 |
| 45 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 46 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -51.51 | -3.52 | -60.06 | 22 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -40.80 | -5.97 | -42.06 | 437 |
| 49 | Donchian 20/10 · 1h | breakout | 66.49 | -33.51 | 165 | 17.6 | -35.25 | -6.52 | -43.26 | 191 |
| 50 | ROC + volume · 1h | momentum | 65.62 | -34.38 | 431 | 27.6 | -34.89 | -6.30 | -41.24 | 335 |
| 51 | MFI reversion · 1h | reversion | 65.26 | -34.74 | 475 | 33.1 | -34.97 | -5.25 | -36.49 | 171 |
| 52 | EMA 9/21 cross · 1h | trend | 63.95 | -36.05 | 291 | 11.3 | -39.33 | -7.39 | -47.32 | 323 |
| 53 | CCI reversion · 1h | reversion | 63.04 | -36.96 | 406 | 41.1 | -46.39 | -7.67 | -47.50 | 479 |
| 54 | MACD cross · 1h | trend | 62.39 | -37.61 | 444 | 20.9 | -50.17 | -9.96 | -51.00 | 496 |
| 55 | Bollinger reversion · 1h | reversion | 59.17 | -40.83 | 366 | 37.4 | -42.94 | -6.59 | -43.59 | 420 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -51.13 | -8.60 | -51.89 | 582 |
| 57 | Agent (ML meta-label) | meta | 56.59 | -43.41 | 2003 | 24.7 | -24.95 | -4.75 | -28.14 | 295 |
| 58 | RSI(14) reversion · 1h | reversion | 55.81 | -44.19 | 224 | 33.0 | -42.25 | -6.15 | -45.67 | 271 |
| 59 | VWAP momentum · 1h | momentum | 54.55 | -45.45 | 1013 | 21.4 | -56.16 | -11.25 | -60.51 | 1192 |
| 60 | Z-score reversion · 1h | reversion | 52.20 | -47.80 | 240 | 33.3 | -43.04 | -6.00 | -45.45 | 264 |
| 61 | Three white soldiers | momentum | 52.03 | -47.98 | 616 | 14.1 | -51.67 | -23.32 | -52.01 | 662 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -52.22 | -9.58 | -52.39 | 676 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -47.50 | -99.16 | 5334 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.51 | -30.60 | -84.01 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.97 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.28 | -34.20 | -91.37 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.14 | -45.00 | -92.27 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -28.77 | -90.21 | 2023 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.23 | -50.87 | -98.23 | 3489 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.83 | -52.25 | -96.84 | 3388 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.83 | -40.43 | -93.94 | 2205 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.61 | -35.82 | -83.61 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.52 | -99.67 | 6315 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.98 | -46.37 | -93.05 | 2529 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.49 | -94.64 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -74.36 | -99.84 | 6270 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.49 | -47.20 | -93.49 | 2286 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.98 | -26.75 | -78.98 | 1641 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.82 | -97.83 | 3379 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -59.82 | -99.15 | 5079 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.91 | -29.85 | -70.91 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.96 | -56.88 | -94.97 | 2717 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.70 | -39.33 | -85.94 | 1704 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -73.76 | -99.73 | 6531 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.61 | -32.22 | -91.62 | 2468 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.91 | -19.69 | -81.99 | 1931 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.35 | -36.09 | -92.36 | 2189 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.87 | -47.97 | -97.87 | 4024 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.41 | -54.48 | -90.41 | 2188 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.35 | -32.03 | -67.45 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.05 | -28.31 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.89 | -19.17 | -83.95 | 1839 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.76 | -47.50 | -97.76 | 4425 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -117.30 | -99.95 | 8422 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 17:20:05.000135+00:00 -> 2026-11-20 17:30:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
