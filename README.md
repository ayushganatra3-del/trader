# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T17:45:05.000138+00:00 · 70823 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £79.17 (-20.83%)

Closed trades 239, win rate 36.0%, fees £6.49, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 23126 decisions in 2635 calls, $0.2954 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T17:45 | 1 / 8 / 21 | cash |  |
| Breezy | 2026-11-23T17:45 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-23T17:45 | 2 / 23 / 5 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.81% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 32.17 | 4.75 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.54 | 15.54 | 0 | — | 13.52 | 4.55 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.52 | 1.37 | -9.74 | 35 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.71 | 3.71 | 0 | — | 1.96 | 0.62 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.41 | -0.59 | 215 | 32.1 | -0.22 | 0.02 | -8.71 | 210 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.78 | -3.55 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.10 | -3.90 | 225 | 28.9 | -0.75 | -0.16 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.34 | -4.66 | 0 | — | -6.91 | -1.78 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.26 | -3.17 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.10 | -7.90 | 0 | — | -9.10 | -1.91 | -13.87 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 16 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.56 | -3.47 | -8.72 | 31 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.81 | -9.19 | 0 | — | -10.61 | -2.28 | -17.03 | 1 |
| 18 | VWAP reversion · 1h | reversion | 90.57 | -9.43 | 163 | 46.0 | -6.90 | -1.13 | -20.49 | 156 |
| 19 | Copy: Insider buying | copy | 89.29 | -10.71 | 57 | 40.4 | -18.60 | -3.65 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.95 | -3.28 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.26 | -13.74 | 9 | 44.4 | -11.42 | -0.64 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.24 | -13.76 | 456 | 33.3 | -13.29 | -4.41 | -14.52 | 542 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -17.16 | -3.93 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.29 | -16.71 | 76 | 19.7 | -18.41 | -6.64 | -18.58 | 75 |
| 25 | Connors RSI(2) · 1h | reversion | 81.16 | -18.84 | 219 | 40.6 | -12.93 | -5.39 | -14.31 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.47 | -19.53 | 200 | 27.0 | -27.83 | -7.49 | -30.07 | 190 |
| 27 | Agent | meta | 79.17 | -20.83 | 239 | 36.0 | -27.05 | -5.96 | -27.77 | 202 |
| 28 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -25.70 | -4.32 | -26.03 | 95 |
| 29 | Donchian 55/20 · 1h | breakout | 77.39 | -22.61 | 82 | 12.2 | -28.58 | -7.75 | -28.84 | 84 |
| 30 | Opening range 15m | breakout | 77.25 | -22.75 | 567 | 30.9 | -22.40 | -6.92 | -23.54 | 661 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.93 | -6.95 | -23.10 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -26.76 | -6.83 | -27.18 | 149 |
| 33 | Ichimoku · 1h | trend | 73.69 | -26.31 | 110 | 13.6 | -30.44 | -8.02 | -31.46 | 105 |
| 34 | Hold BTC | benchmark | 71.44 | -28.56 | 3 | 0.0 | -29.29 | -5.22 | -36.21 | 1 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 71.02 | -28.98 | 3 | 0.0 | -23.78 | -2.83 | -32.18 | 1 |
| 36 | Supertrend · 1h | trend | 70.97 | -29.03 | 199 | 16.6 | -34.32 | -6.59 | -38.37 | 218 |
| 37 | Triple EMA stack · 1h | trend | 70.47 | -29.52 | 161 | 14.3 | -36.16 | -9.23 | -38.53 | 167 |
| 38 | EMA 20/50 cross · 1h | trend | 70.13 | -29.86 | 119 | 10.1 | -36.03 | -9.83 | -39.46 | 125 |
| 39 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -36.81 | -6.63 | -39.21 | 282 |
| 40 | Daily: Momentum burst | daily | 69.33 | -30.67 | 30 | 13.3 | -37.68 | -5.38 | -38.52 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.58 | -31.42 | 207 | 22.2 | -33.30 | -8.67 | -34.28 | 212 |
| 42 | OBV trend · 1h | momentum | 67.53 | -32.47 | 319 | 19.4 | -38.14 | -9.83 | -40.22 | 233 |
| 43 | Stochastic reversion · 1h | reversion | 67.06 | -32.94 | 392 | 40.6 | -35.09 | -3.75 | -43.45 | 436 |
| 44 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -33.96 | -9.11 | -34.22 | 209 |
| 45 | Max aggression: 5-day momentum | meta | 65.62 | -34.38 | 24 | 37.5 | -61.15 | -3.97 | -64.97 | 23 |
| 46 | RSI momentum · 1h | momentum | 65.36 | -34.64 | 188 | 13.8 | -39.11 | -8.72 | -40.59 | 203 |
| 47 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -47.09 | -9.45 | -47.47 | 632 |
| 48 | MFI reversion · 1h | reversion | 63.51 | -36.49 | 486 | 32.9 | -32.05 | -4.65 | -37.45 | 185 |
| 49 | Donchian 20/10 · 1h | breakout | 62.88 | -37.12 | 173 | 16.8 | -38.96 | -8.35 | -40.54 | 193 |
| 50 | ROC + volume · 1h ⏸ | momentum | 61.62 | -38.38 | 451 | 27.1 | -42.49 | -8.60 | -42.49 | 342 |
| 51 | EMA 9/21 cross · 1h | trend | 60.49 | -39.51 | 298 | 11.1 | -44.91 | -10.59 | -46.01 | 327 |
| 52 | Agent (ML meta-label) | meta | 59.94 | -40.05 | 2037 | 24.9 | -23.34 | -2.80 | -34.79 | 309 |
| 53 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -53.46 | -3.86 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 59.13 | -40.87 | 464 | 20.9 | -48.99 | -9.36 | -50.47 | 517 |
| 55 | Bollinger reversion · 1h | reversion | 58.06 | -41.94 | 391 | 37.6 | -37.81 | -4.47 | -45.42 | 435 |
| 56 | CCI reversion · 1h | reversion | 58.06 | -41.94 | 430 | 40.0 | -49.63 | -8.24 | -52.15 | 506 |
| 57 | Williams %R · 1h | reversion | 54.19 | -45.81 | 495 | 38.2 | -54.63 | -8.99 | -55.89 | 595 |
| 58 | VWAP momentum · 1h | momentum | 53.63 | -46.37 | 1044 | 21.6 | -58.34 | -13.44 | -58.83 | 1191 |
| 59 | RSI(14) reversion · 1h | reversion | 51.01 | -48.99 | 240 | 31.7 | -47.12 | -7.17 | -50.30 | 298 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.15 | -8.65 | -54.80 | 687 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -48.13 | -99.14 | 5339 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.97 | -33.00 | -84.55 | 1436 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.52 | -48.32 | -94.55 | 2423 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.88 | -31.47 | -91.06 | 1927 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.85 | -41.05 | -91.86 | 2256 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.47 | -27.61 | -89.54 | 1947 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.16 | -48.17 | -98.16 | 3413 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.00 | -51.73 | -97.00 | 3354 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -38.22 | -93.71 | 2151 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.26 | -22.44 | -52.27 | 648 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.32 | -34.76 | -83.40 | 1549 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.56 | -99.66 | 6290 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.22 | -40.64 | -93.22 | 2491 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.41 | -35.52 | -94.41 | 3150 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -61.58 | -99.82 | 6129 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.22 | -42.70 | -93.42 | 2264 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.48 | -24.08 | -78.93 | 1615 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -55.76 | -97.79 | 3285 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -57.53 | -99.18 | 5104 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.56 | -27.86 | -70.67 | 1194 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.98 | -49.08 | -94.98 | 2676 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.96 | -6.21 | -48.78 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.59 | -36.92 | -85.62 | 1678 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.51 | -99.76 | 6522 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.51 | -29.84 | -91.69 | 2463 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.86 | -19.50 | -82.99 | 1957 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.79 | -29.30 | -92.06 | 2173 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -47.40 | -98.15 | 4058 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.17 | -46.34 | -90.19 | 2189 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.60 | -29.88 | -68.61 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.21 | -28.34 | -74.22 | 1170 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.17 | -19.13 | -84.17 | 1846 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.00 | -48.30 | -98.00 | 4437 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.66 | -99.94 | 8280 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T17:45 | Squeeze breakout · 1h | sell | ETH-USD | 20.64 | -0.55 | stop-loss |
| 2026-11-23T17:45 | ROC + volume · 1h | sell | TSLA | 7.80 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T17:45 | ROC + volume · 1h | sell | SOL-USD | 7.57 | -0.26 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T17:45 | ROC + volume · 1h | sell | PLTR | 7.82 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T17:45 | ROC + volume · 1h | sell | NVDA | 7.70 | -0.26 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T17:45 | ROC + volume · 1h | sell | GOOGL | 7.83 | 0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T17:45 | ROC + volume · 1h | sell | ETH-USD | 7.72 | -0.21 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T17:45 | ROC + volume · 1h | sell | DOGE-USD | 7.63 | -0.23 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T17:45 | ROC + volume · 1h | sell | BTC-USD | 7.56 | -0.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T17:45 | Opening range 30m | sell | COIN | 9.50 | -0.10 | stop-loss |
| 2026-11-23T17:45 | Opening range 15m | buy | UPRO | 4.30 | — | rebalance up |
| 2026-11-23T17:45 | Opening range 15m | buy | TSLA | 4.24 | — | rebalance up |
| 2026-11-23T17:45 | Opening range 15m | buy | SPY | 4.19 | — | rebalance up |
| 2026-11-23T17:45 | Opening range 15m | buy | NVDA | 4.44 | — | rebalance up |
| 2026-11-23T17:45 | Opening range 15m | buy | LABU | 4.19 | — | rebalance up |
| 2026-11-23T17:45 | Opening range 15m | sell | COIN | 8.41 | -0.18 | stop-loss |
| 2026-11-23T17:36 | Agent (ML meta-label) | sell | BITX | 4.08 | -0.02 | selected signal exited |
| 2026-11-23T17:30 | Williams %R · 1h | sell | UPRO | 2.47 | -0.03 | exit signal |
| 2026-11-23T17:30 | Williams %R · 1h | sell | QQQ | 2.48 | -0.01 | exit signal |
| 2026-11-23T17:30 | Williams %R · 1h | sell | GOOGL | 2.51 | 0.01 | exit signal |
| 2026-11-23T17:30 | Stochastic reversion · 1h | buy | SQQQ | 6.73 | — | entry signal |
| 2026-11-23T17:30 | RSI(14) reversion · 1h | sell | GOOGL | 2.36 | 0.01 | exit signal |
| 2026-11-23T17:30 | VWAP momentum · 1h | buy | NVDA | 4.14 | — | entry signal |
| 2026-11-23T17:30 | VWAP momentum · 1h | sell | UPRO | 2.99 | -0.02 | exit signal |
| 2026-11-23T17:30 | VWAP momentum · 1h | sell | TQQQ | 2.34 | -0.04 | exit signal |
| 2026-11-23T17:30 | VWAP momentum · 1h | sell | SOXL | 2.30 | -0.07 | exit signal |
| 2026-11-23T17:30 | VWAP momentum · 1h | sell | PLTR | 2.35 | -0.03 | exit signal |
| 2026-11-23T17:30 | EMA 9/21 cross · 1h | buy | TSLA | 2.10 | — | entry signal |
| 2026-11-23T17:30 | EMA 9/21 cross · 1h | buy | NVDA | 7.60 | — | entry signal |
| 2026-11-23T17:30 | EMA 9/21 cross · 1h | sell | ETH-USD | 3.17 | 0.11 | rebalance down |
| 2026-11-23T17:30 | EMA 9/21 cross · 1h | sell | DOGE-USD | 3.43 | 0.14 | rebalance down |
| 2026-11-23T17:30 | EMA 9/21 cross · 1h | sell | BTC-USD | 3.10 | 0.04 | rebalance down |
| 2026-11-23T17:25 | Agent (ML meta-label) | buy | BITX | 4.10 | — | entry |
| 2026-11-23T17:20 | Agent (rotation) | buy | TQQQ | 8.02 | — | entry |
| 2026-11-23T17:20 | Agent (ML meta-label) | sell | BITX | 4.10 | -0.03 | selected signal exited |
| 2026-11-23T17:20 | VWAP momentum · 1h | sell | SPY | 2.83 | 0.00 | target is flat |
| 2026-11-23T17:20 | Gap and go | buy | TQQQ | 24.93 | — | entry |
| 2026-11-23T17:05 | ROC + volume · 1h | buy | BTC-USD | 7.68 | — | entry |
| 2026-11-23T17:05 | ROC + volume · 1h | sell | XRP-USD | 7.68 | -0.18 | stop-loss |
| 2026-11-23T17:00 | Agent (rotation) | buy | LABU | 8.02 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 17:45:05.000138+00:00 -> 2026-11-23 17:55:05.000138+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
