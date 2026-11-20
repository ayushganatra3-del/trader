# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T17:51:05.000109+00:00 · 67123 ticks

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

Today: 25869 decisions in 2730 calls, $0.3287 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T17:51 | 11 / 15 / 4 | cash |  |
| Breezy | 2026-11-20T17:51 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-20T17:51 | 8 / 20 / 2 | COIN 60% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 122.98 | 22.98 | 26 | 65.4 | 26.08 | 4.23 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.33 | 14.33 | 0 | — | 12.21 | 4.09 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 40 | 42.5 | 2.93 | 0.72 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 102.24 | 2.24 | 0 | — | 3.22 | 0.96 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.21 | -0.79 | 203 | 31.5 | 0.06 | 0.11 | -9.06 | 202 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 96.15 | -3.85 | 212 | 28.8 | -0.74 | -0.18 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 91.97 | -8.03 | 0 | — | -9.07 | -3.00 | -10.43 | 1 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.97 | -4.39 | -10.76 | 44 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Bullish score | daily | 89.89 | -10.11 | 19 | 15.8 | -12.38 | -3.09 | -19.56 | 14 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.30 | -10.70 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | VWAP reversion · 1h | reversion | 88.40 | -11.60 | 156 | 45.5 | -13.66 | -4.01 | -18.57 | 152 |
| 19 | Copy: Insider buying | copy | 88.23 | -11.77 | 55 | 40.0 | -7.66 | -1.48 | -14.79 | 66 |
| 20 | Squeeze breakout · 1h | breakout | 87.44 | -12.56 | 70 | 20.0 | -17.86 | -8.63 | -18.95 | 72 |
| 21 | Copy: Congress Democrats (NANC) | copy | 87.38 | -12.62 | 0 | — | -13.28 | -3.64 | -15.50 | 1 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.41 | -13.59 | 451 | 33.5 | -11.56 | -3.85 | -14.87 | 552 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -16.89 | -1.50 | -23.24 | 6 |
| 25 | Parabolic SAR · 1h | trend | 83.85 | -16.15 | 194 | 27.8 | -24.87 | -7.05 | -28.86 | 196 |
| 26 | Donchian 55/20 · 1h | breakout | 80.90 | -19.10 | 79 | 12.7 | -24.79 | -7.28 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 80.75 | -19.25 | 163 | 28.8 | -16.03 | -5.46 | -21.55 | 75 |
| 28 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -19.82 | -5.64 | -20.05 | 209 |
| 29 | Connors RSI(2) · 1h | reversion | 79.94 | -20.06 | 218 | 40.4 | -15.43 | -6.97 | -15.43 | 71 |
| 30 | Keltner breakout · 1h | breakout | 79.61 | -20.39 | 126 | 26.2 | -21.59 | -5.82 | -25.34 | 146 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -15.94 | -4.13 | -19.15 | 97 |
| 32 | Opening range 15m | breakout | 76.82 | -23.18 | 561 | 31.0 | -21.83 | -6.74 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 75.88 | -24.12 | 107 | 14.0 | -28.77 | -8.21 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 73.95 | -26.05 | 228 | 20.2 | -26.04 | -3.96 | -35.87 | 274 |
| 35 | Triple EMA stack · 1h | trend | 72.12 | -27.88 | 161 | 14.3 | -33.50 | -8.40 | -36.70 | 170 |
| 36 | Bollinger breakout · 1h | breakout | 72.10 | -27.90 | 195 | 21.5 | -31.92 | -8.18 | -36.32 | 217 |
| 37 | Supertrend · 1h | trend | 72.03 | -27.97 | 198 | 16.7 | -34.24 | -6.86 | -37.64 | 199 |
| 38 | EMA 20/50 cross · 1h | trend | 71.78 | -28.22 | 119 | 10.1 | -36.43 | -10.38 | -40.64 | 122 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 71.16 | -28.84 | 2 | 0.0 | -27.77 | -4.00 | -30.97 | 1 |
| 40 | Heikin-Ashi · 1h | trend | 70.16 | -29.84 | 483 | 23.0 | -44.55 | -9.47 | -47.85 | 616 |
| 41 | Max aggression: 1-day momentum | meta | 69.93 | -30.07 | 33 | 27.3 | -51.05 | -3.61 | -58.28 | 39 |
| 42 | RSI momentum · 1h | momentum | 69.84 | -30.16 | 184 | 14.1 | -37.64 | -8.28 | -41.77 | 202 |
| 43 | OBV trend · 1h | momentum | 69.81 | -30.19 | 315 | 19.4 | -38.15 | -10.13 | -41.17 | 240 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Hold BTC | benchmark | 69.36 | -30.64 | 2 | 0.0 | -27.87 | -4.49 | -32.51 | 1 |
| 46 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -51.39 | -3.50 | -60.06 | 22 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -40.93 | -5.97 | -42.06 | 439 |
| 49 | Donchian 20/10 · 1h | breakout | 66.54 | -33.46 | 165 | 17.6 | -35.33 | -6.58 | -43.26 | 192 |
| 50 | ROC + volume · 1h | momentum | 65.66 | -34.34 | 431 | 27.6 | -34.64 | -6.19 | -41.19 | 336 |
| 51 | MFI reversion · 1h | reversion | 65.26 | -34.74 | 475 | 33.1 | -34.97 | -5.25 | -36.49 | 171 |
| 52 | EMA 9/21 cross · 1h | trend | 64.00 | -36.00 | 291 | 11.3 | -39.30 | -7.38 | -47.32 | 323 |
| 53 | CCI reversion · 1h | reversion | 63.01 | -36.99 | 406 | 41.1 | -46.42 | -7.67 | -47.55 | 479 |
| 54 | MACD cross · 1h | trend | 62.42 | -37.58 | 444 | 20.9 | -50.14 | -9.95 | -51.00 | 496 |
| 55 | Bollinger reversion · 1h | reversion | 59.13 | -40.87 | 366 | 37.4 | -42.98 | -6.60 | -43.69 | 421 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -51.26 | -8.59 | -52.02 | 582 |
| 57 | Agent (ML meta-label) | meta | 56.47 | -43.52 | 2004 | 24.7 | -25.22 | -4.92 | -27.70 | 291 |
| 58 | RSI(14) reversion · 1h | reversion | 55.78 | -44.22 | 224 | 33.0 | -42.30 | -6.16 | -45.67 | 271 |
| 59 | VWAP momentum · 1h | momentum | 54.59 | -45.41 | 1013 | 21.4 | -56.13 | -11.24 | -60.51 | 1192 |
| 60 | Z-score reversion · 1h ⏸ | reversion | 52.10 | -47.90 | 242 | 33.1 | -43.12 | -6.01 | -45.54 | 264 |
| 61 | Three white soldiers | momentum | 52.03 | -47.98 | 616 | 14.1 | -51.64 | -23.32 | -51.98 | 661 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -52.22 | -9.57 | -52.42 | 676 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -47.50 | -99.16 | 5335 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.55 | -30.64 | -84.01 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.99 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.28 | -34.20 | -91.37 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.13 | -44.99 | -92.27 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -28.78 | -90.21 | 2023 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.22 | -50.87 | -98.22 | 3486 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -52.31 | -96.83 | 3388 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.79 | -40.53 | -93.91 | 2203 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.61 | -35.82 | -83.61 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.64 | -99.67 | 6325 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -46.38 | -93.05 | 2529 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.49 | -94.64 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -74.16 | -99.84 | 6278 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.48 | -47.20 | -93.48 | 2285 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.67 | -27.30 | -78.67 | 1637 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.83 | -60.80 | -97.83 | 3380 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -59.76 | -99.15 | 5086 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.91 | -29.85 | -70.91 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.94 | -56.70 | -94.96 | 2716 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.72 | -39.34 | -85.98 | 1705 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.74 | -73.68 | -99.74 | 6535 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -32.19 | -91.59 | 2466 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.99 | -19.68 | -82.02 | 1934 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.34 | -36.44 | -92.34 | 2211 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.88 | -47.93 | -97.88 | 4026 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.39 | -54.48 | -90.39 | 2186 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.33 | -32.05 | -67.43 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.03 | -28.26 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.03 | -19.16 | -84.03 | 1843 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.77 | -47.44 | -97.77 | 4430 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.26 | -99.94 | 8418 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | MSTR | 4.82 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | META | 4.87 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | LABU | 4.82 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:50 | Stochastic reversion · 1h | sell | AMZN | 4.83 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:45 | Agent (rotation) | buy | SQQQ | 31.59 | — | rebalance up |
| 2026-11-20T16:45 | Day trade: Stocks in Play ORB | sell | GOOGL | 24.70 | -0.24 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 17:51:05.000109+00:00 -> 2026-11-20 18:01:05.000109+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
