# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T15:15:05.000102+00:00 · 70711 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £79.17 (-20.82%)

Closed trades 238, win rate 36.1%, fees £6.47, max drawdown -21.19%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 30.90 | -1.00 |

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

Today: 12968 decisions in 2299 calls, $0.1768 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T15:15 | 5 / 19 / 6 | cash |  |
| Breezy | 2026-11-23T15:15 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-23T15:15 | 4 / 25 / 1 | COIN 68% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.84 | 14.84 | 0 | — | 13.38 | 4.51 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.12 | 1.31 | -9.74 | 36 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.46 | 7.46 | 40 | 30.0 | 9.00 | 1.50 | -9.24 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.46 | 3.46 | 0 | — | 1.52 | 0.51 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.54 | 0.54 | 205 | 31.7 | 0.79 | 0.33 | -8.71 | 204 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.90 | -3.69 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 97.23 | -2.77 | 214 | 29.0 | 0.50 | 0.25 | -7.48 | 148 |
| 11 | Hold SPY | benchmark | 95.21 | -4.79 | 0 | — | -6.58 | -1.67 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.24 | -3.15 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | VWAP reversion · 1h | reversion | 91.92 | -8.09 | 161 | 45.3 | -5.22 | -0.70 | -20.49 | 156 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.77 | -8.23 | 0 | — | -9.12 | -1.92 | -13.87 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 17 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.56 | -3.47 | -8.72 | 31 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.03 | -9.97 | 0 | — | -11.36 | -2.51 | -17.03 | 1 |
| 19 | Copy: Insider buying | copy | 89.07 | -10.93 | 57 | 40.4 | -18.78 | -3.70 | -22.56 | 68 |
| 20 | Opening range 30m | breakout | 87.38 | -12.62 | 452 | 33.6 | -11.90 | -3.98 | -14.52 | 532 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.89 | -3.26 | -20.94 | 1 |
| 22 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.35 | -13.65 | 9 | 44.4 | -11.01 | -0.60 | -26.65 | 6 |
| 23 | Daily: Bullish score | daily | 85.82 | -14.18 | 19 | 15.8 | -17.34 | -3.91 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 84.40 | -15.60 | 75 | 20.0 | -15.08 | -6.28 | -15.96 | 72 |
| 25 | Parabolic SAR · 1h | trend | 82.32 | -17.68 | 198 | 27.3 | -25.40 | -7.01 | -29.63 | 186 |
| 26 | Connors RSI(2) · 1h | reversion | 80.18 | -19.82 | 218 | 40.4 | -13.97 | -6.15 | -14.37 | 67 |
| 27 | Donchian 55/20 · 1h | breakout | 79.42 | -20.58 | 80 | 12.5 | -26.80 | -7.38 | -29.11 | 85 |
| 28 | Agent | meta | 79.17 | -20.82 | 238 | 36.1 | -25.29 | -5.54 | -25.29 | 200 |
| 29 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -24.95 | -4.15 | -25.44 | 96 |
| 30 | Opening range 15m | breakout | 77.85 | -22.15 | 562 | 31.1 | -21.55 | -6.62 | -23.54 | 652 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -21.09 | -7.84 | -21.46 | 72 |
| 32 | Keltner breakout · 1h | breakout | 75.89 | -24.11 | 134 | 25.4 | -27.41 | -7.31 | -27.82 | 149 |
| 33 | Ichimoku · 1h | trend | 75.75 | -24.25 | 109 | 13.8 | -26.83 | -7.24 | -30.74 | 108 |
| 34 | Hold BTC | benchmark | 73.10 | -26.90 | 3 | 0.0 | -27.04 | -4.61 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 72.52 | -27.48 | 198 | 16.7 | -33.01 | -6.22 | -38.61 | 203 |
| 36 | Triple EMA stack · 1h | trend | 71.67 | -28.33 | 161 | 14.3 | -34.54 | -8.84 | -38.31 | 163 |
| 37 | EMA 20/50 cross · 1h | trend | 71.47 | -28.53 | 119 | 10.1 | -34.88 | -9.62 | -39.77 | 123 |
| 38 | ADX DI cross · 1h | trend | 71.13 | -28.87 | 234 | 20.1 | -33.64 | -6.22 | -36.16 | 271 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 70.86 | -29.14 | 3 | 0.0 | -23.30 | -2.74 | -32.18 | 1 |
| 40 | Bollinger breakout · 1h | breakout | 69.13 | -30.87 | 207 | 22.2 | -33.15 | -8.71 | -34.63 | 213 |
| 41 | Daily: Momentum burst | daily | 69.01 | -31.00 | 30 | 13.3 | -37.87 | -5.42 | -38.08 | 25 |
| 42 | OBV trend · 1h | momentum | 68.75 | -31.25 | 318 | 19.5 | -36.88 | -9.61 | -40.43 | 232 |
| 43 | Max aggression: 5-day momentum | meta | 67.62 | -32.38 | 24 | 37.5 | -59.83 | -3.93 | -63.78 | 23 |
| 44 | RSI momentum · 1h | momentum | 67.27 | -32.73 | 187 | 13.9 | -36.41 | -8.10 | -39.47 | 201 |
| 45 | Stochastic reversion · 1h | reversion | 67.12 | -32.88 | 388 | 40.2 | -34.39 | -3.54 | -43.44 | 436 |
| 46 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -35.20 | -9.52 | -35.53 | 209 |
| 47 | Heikin-Ashi · 1h | trend | 65.80 | -34.20 | 500 | 23.2 | -47.24 | -9.92 | -47.24 | 614 |
| 48 | MFI reversion · 1h | reversion | 64.70 | -35.30 | 484 | 33.1 | -30.66 | -4.30 | -37.45 | 176 |
| 49 | Donchian 20/10 · 1h | breakout | 64.59 | -35.41 | 172 | 16.9 | -37.93 | -8.25 | -40.58 | 194 |
| 50 | ROC + volume · 1h | momentum | 63.18 | -36.82 | 439 | 27.6 | -41.23 | -8.48 | -41.38 | 339 |
| 51 | EMA 9/21 cross · 1h | trend | 61.69 | -38.31 | 298 | 11.1 | -43.89 | -10.25 | -46.29 | 328 |
| 52 | MACD cross · 1h | trend | 60.48 | -39.52 | 462 | 21.0 | -48.56 | -9.34 | -49.70 | 500 |
| 53 | Agent (ML meta-label) | meta | 60.20 | -39.80 | 2026 | 24.7 | -26.13 | -3.14 | -37.15 | 316 |
| 54 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -52.61 | -3.83 | -54.71 | 38 |
| 55 | CCI reversion · 1h | reversion | 59.00 | -41.00 | 429 | 40.1 | -48.68 | -8.00 | -52.15 | 484 |
| 56 | Bollinger reversion · 1h | reversion | 57.93 | -42.07 | 384 | 36.7 | -38.39 | -4.56 | -45.42 | 436 |
| 57 | Williams %R · 1h | reversion | 54.96 | -45.04 | 487 | 38.4 | -52.99 | -8.54 | -55.62 | 587 |
| 58 | VWAP momentum · 1h | momentum | 54.50 | -45.50 | 1031 | 21.6 | -57.78 | -13.23 | -59.15 | 1184 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -45.19 | -6.66 | -50.46 | 296 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.62 | -8.46 | -55.00 | 689 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -47.30 | -99.14 | 5321 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.83 | -31.95 | -84.71 | 1436 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.63 | -50.33 | -94.68 | 2431 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.78 | -30.88 | -91.11 | 1928 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.74 | -40.80 | -91.83 | 2252 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.14 | -27.37 | -89.38 | 1940 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -48.28 | -98.16 | 3429 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.02 | -53.21 | -97.06 | 3373 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.49 | -39.02 | -93.51 | 2163 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.34 | -22.56 | -52.34 | 653 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.31 | -35.12 | -83.50 | 1550 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.55 | -99.66 | 6294 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.09 | -40.59 | -93.12 | 2498 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.22 | -35.38 | -94.26 | 3109 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -63.02 | -99.83 | 6158 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.28 | -43.29 | -93.46 | 2268 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.71 | -24.31 | -79.08 | 1624 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -56.65 | -97.80 | 3292 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -56.23 | -99.17 | 5088 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.84 | -28.22 | -70.99 | 1204 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.94 | -48.59 | -94.96 | 2689 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -43.42 | -5.84 | -48.72 | 267 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.60 | -37.15 | -85.77 | 1686 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.16 | -99.76 | 6521 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.58 | -30.24 | -91.68 | 2486 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.93 | -19.66 | -83.07 | 1966 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.78 | -29.16 | -92.08 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.12 | -47.04 | -98.12 | 4056 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.07 | -45.83 | -90.19 | 2197 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.43 | -30.40 | -68.49 | 801 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.33 | -27.91 | -74.45 | 1168 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.67 | -18.79 | -83.75 | 1848 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.94 | -47.60 | -97.95 | 4429 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -88.18 | -99.94 | 8293 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T15:15 | Agent (rotation) | buy | LABU | 8.10 | — | entry |
| 2026-11-23T15:15 | ADX DI cross · 1h | buy | SQQQ | 3.58 | — | rebalance up |
| 2026-11-23T15:15 | Opening range 30m | buy | TSLA | 21.85 | — | entry signal |
| 2026-11-23T15:15 | Opening range 15m | buy | TSLA | 19.47 | — | entry signal |
| 2026-11-23T15:15 | Gap and go | buy | LABU | 25.14 | — | entry signal |
| 2026-11-23T15:10 | Volume breakout · 1h | sell | XRP-USD | 15.23 | -0.24 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T15:10 | Volume breakout · 1h | sell | SOL-USD | 13.45 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T15:10 | Volume breakout · 1h | sell | ETH-USD | 13.29 | -0.32 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T15:10 | Volume breakout · 1h | sell | DOGE-USD | 13.61 | -0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T15:10 | Volume breakout · 1h | sell | BTC-USD | 13.35 | -0.26 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T15:10 | Squeeze breakout · 1h | sell | SOL-USD | 17.81 | 0.93 | stop-loss |
| 2026-11-23T15:10 | Squeeze breakout · 1h | sell | DOGE-USD | 17.97 | -0.01 | stop-loss |
| 2026-11-23T15:10 | Keltner breakout · 1h | sell | SOL-USD | 18.90 | 0.54 | stop-loss |
| 2026-11-23T15:10 | Keltner breakout · 1h | sell | DOGE-USD | 18.95 | -0.06 | stop-loss |
| 2026-11-23T15:10 | Bollinger breakout · 1h | sell | SOL-USD | 15.07 | 0.89 | stop-loss |
| 2026-11-23T15:10 | Bollinger breakout · 1h | sell | DOGE-USD | 14.93 | 0.70 | stop-loss |
| 2026-11-23T15:07 | Copy: Insider buying | buy | KNOP | 1.26 | — | entry |
| 2026-11-23T15:07 | Copy: Insider buying | buy | BORR | 11.14 | — | entry |
| 2026-11-23T15:07 | Copy: Insider buying | sell | PSEC | 12.19 | 1.20 | target is flat |
| 2026-11-23T15:05 | Agent (rotation) | sell | LABU | 8.14 | -0.07 | selected signal exited |
| 2026-11-23T15:05 | Gap and go | sell | LABU | 24.84 | -0.21 | exit signal |
| 2026-11-23T15:02 | ROC + volume · 1h | buy | XRP-USD | 3.17 | — | rebalance up |
| 2026-11-23T15:02 | ROC + volume · 1h | sell | BTC-USD | 3.17 | -0.05 | rebalance down |
| 2026-11-23T15:00 | Day trade: Stocks in Play ORB | sell | SQQQ | 23.96 | -0.71 | target is flat |
| 2026-11-23T15:00 | Agent (ML meta-label) | sell | SOXL | 5.95 | 0.07 | selected signal exited |
| 2026-11-23T15:00 | Bollinger reversion · 1h | sell | SOXL | 7.33 | 0.09 | take-profit |
| 2026-11-23T15:00 | Squeeze breakout · 1h | buy | ETH-USD | 21.19 | — | entry signal |
| 2026-11-23T15:00 | Squeeze breakout · 1h | sell | BTC-USD | 17.62 | -0.36 | stop-loss |
| 2026-11-23T15:00 | Keltner breakout · 1h | sell | BTC-USD | 19.01 | -0.32 | stop-loss |
| 2026-11-23T15:00 | Bollinger breakout · 1h | sell | BTC-USD | 14.47 | 0.24 | stop-loss |
| 2026-11-23T15:00 | Donchian 55/20 · 1h | buy | ETH-USD | 5.81 | — | rebalance up |
| 2026-11-23T15:00 | Donchian 55/20 · 1h | sell | SQQQ | 13.29 | -0.84 | stop-loss |
| 2026-11-23T15:00 | Donchian 20/10 · 1h | buy | ETH-USD | 4.69 | — | rebalance up |
| 2026-11-23T15:00 | Donchian 20/10 · 1h | sell | SQQQ | 10.80 | -0.68 | stop-loss |
| 2026-11-23T15:00 | ROC + volume · 1h | buy | XRP-USD | 9.48 | — | entry signal |
| 2026-11-23T15:00 | ROC + volume · 1h | buy | ETH-USD | 12.65 | — | entry signal |
| 2026-11-23T15:00 | ROC + volume · 1h | sell | SOL-USD | 3.17 | -0.04 | rebalance down |
| 2026-11-23T15:00 | ROC + volume · 1h | sell | DOGE-USD | 3.18 | 0.01 | rebalance down |
| 2026-11-23T15:00 | MACD cross · 1h | buy | ETH-USD | 7.84 | — | rebalance up |
| 2026-11-23T15:00 | MACD cross · 1h | sell | SQQQ | 11.48 | -0.89 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 15:15:05.000102+00:00 -> 2026-11-23 15:25:05.000102+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
