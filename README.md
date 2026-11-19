# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T18:23:05.000124+00:00 · 65931 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.19 (-14.81%)

Closed trades 226, win rate 36.7%, fees £6.22, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| META | 17.00 | -0.15 |
| SOXL | 16.54 | -0.59 |
| SQQQ | 17.52 | +0.45 |
| TSLA | 17.28 | +0.15 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-19 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, LRN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-18)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 33.12 · VIX 24.56 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 6.2, AMZN 6.2, TSLA 4.1, AMD 3.9, META 1.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 27429 decisions in 2859 calls, $0.3473 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T18:23 | 6 / 15 / 8 | cash |  |
| Breezy | 2026-11-19T18:23 | 0 / 22 / 7 | cash |  |
| Boozy | 2026-11-19T18:23 | 6 / 21 / 2 | ETHU 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.97% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| VWAP reversion | META | 1.90 | +2.79% | 4 |
| OBV trend | SQQQ | 1.88 | +3.85% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 120.74 | 20.74 | 25 | 64.0 | 29.09 | 4.63 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.71 | 13.71 | 0 | — | 11.21 | 3.77 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.95 | 2.95 | 0 | — | 3.79 | 1.08 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -3.88 | -3.45 | -4.83 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.69 | -0.48 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | 1.17 | 0.45 | -9.06 | 212 |
| 10 | Agent (rotation) | meta | 95.83 | -4.17 | 210 | 28.6 | -1.05 | -0.30 | -7.63 | 152 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.46 | -5.54 | 0 | — | -5.53 | -1.83 | -7.97 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.78 | -5.44 | 20 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.13 | -6.87 | 0 | — | -6.89 | -1.81 | -8.68 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.85 | -8.15 | 8 | 50.0 | -7.81 | -0.59 | -18.69 | 6 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.43 | -9.57 | 0 | — | -10.16 | -2.87 | -12.67 | 1 |
| 18 | Copy: Insider buying | copy | 89.96 | -10.04 | 55 | 40.0 | -9.20 | -1.81 | -14.79 | 67 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.66 | -3.74 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 89.41 | -10.59 | 115 | 23.5 | -14.75 | -7.36 | -16.08 | 56 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.21 | -12.79 | 17 | 17.6 | -10.48 | -2.34 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -15.90 | -9.02 | -15.90 | 70 |
| 24 | Opening range 30m | breakout | 86.21 | -13.79 | 448 | 33.5 | -11.68 | -3.91 | -14.66 | 561 |
| 25 | Agent | meta | 85.19 | -14.81 | 226 | 36.7 | -14.42 | -6.76 | -17.14 | 207 |
| 26 | Agent (aggressive) | meta | 82.59 | -17.41 | 105 | 34.3 | -16.68 | -4.31 | -19.98 | 100 |
| 27 | Parabolic SAR · 1h | trend | 81.02 | -18.98 | 194 | 27.8 | -27.88 | -8.61 | -29.47 | 199 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.66 | -6.52 | -15.33 | 77 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.45 | -5.37 | -21.50 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -25.19 | -6.65 | -28.32 | 150 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -26.20 | -6.92 | -30.86 | 84 |
| 32 | Opening range 15m | breakout | 77.16 | -22.84 | 546 | 31.7 | -20.54 | -6.13 | -23.54 | 674 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 75.44 | -24.56 | 2 | 0.0 | -21.07 | -2.96 | -26.67 | 1 |
| 34 | Hold BTC | benchmark | 73.98 | -26.02 | 2 | 0.0 | -22.73 | -3.63 | -28.91 | 1 |
| 35 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -49.17 | -3.20 | -57.68 | 22 |
| 36 | Ichimoku · 1h | trend | 73.32 | -26.68 | 107 | 14.0 | -32.23 | -9.81 | -33.26 | 111 |
| 37 | ADX DI cross · 1h | trend | 72.76 | -27.23 | 223 | 19.7 | -29.97 | -4.78 | -36.70 | 281 |
| 38 | Stochastic reversion · 1h | reversion | 71.85 | -28.15 | 356 | 42.1 | -36.18 | -5.58 | -36.56 | 427 |
| 39 | Supertrend · 1h | trend | 70.49 | -29.51 | 192 | 16.7 | -33.43 | -5.60 | -40.05 | 206 |
| 40 | MFI reversion · 1h | reversion | 70.26 | -29.75 | 462 | 33.8 | -29.10 | -4.38 | -31.36 | 172 |
| 41 | Bollinger breakout · 1h | breakout | 70.01 | -29.99 | 195 | 21.5 | -33.79 | -8.85 | -36.52 | 218 |
| 42 | Triple EMA stack · 1h | trend | 70.00 | -30.00 | 161 | 14.3 | -32.08 | -6.84 | -38.64 | 175 |
| 43 | EMA 20/50 cross · 1h | trend | 69.55 | -30.45 | 118 | 10.2 | -37.60 | -8.29 | -44.64 | 123 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.37 | -4.99 | -37.91 | 31 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -30.47 | -6.11 | -36.32 | 208 |
| 46 | CCI reversion · 1h | reversion | 67.80 | -32.20 | 396 | 41.9 | -41.97 | -7.01 | -44.29 | 481 |
| 47 | Heikin-Ashi · 1h | trend | 67.68 | -32.32 | 483 | 23.0 | -47.08 | -10.41 | -48.31 | 626 |
| 48 | OBV trend · 1h | momentum | 67.45 | -32.55 | 315 | 19.4 | -35.30 | -8.03 | -40.61 | 246 |
| 49 | RSI momentum · 1h | momentum | 67.33 | -32.67 | 184 | 14.1 | -35.61 | -6.77 | -41.52 | 203 |
| 50 | MACD cross · 1h | trend | 65.73 | -34.27 | 427 | 21.8 | -43.32 | -7.11 | -49.07 | 492 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -42.22 | -2.66 | -57.50 | 39 |
| 52 | ROC + volume · 1h ⏸ | momentum | 64.82 | -35.18 | 431 | 27.6 | -39.99 | -6.99 | -44.41 | 342 |
| 53 | Donchian 20/10 · 1h | breakout | 64.61 | -35.39 | 165 | 17.6 | -36.82 | -7.17 | -42.86 | 191 |
| 54 | Bollinger reversion · 1h | reversion | 62.44 | -37.56 | 357 | 38.1 | -39.95 | -6.14 | -40.41 | 418 |
| 55 | Williams %R · 1h | reversion | 62.14 | -37.86 | 446 | 40.6 | -48.46 | -8.63 | -48.96 | 582 |
| 56 | EMA 9/21 cross · 1h | trend | 61.83 | -38.17 | 291 | 11.3 | -41.09 | -8.09 | -47.13 | 325 |
| 57 | RSI(14) reversion · 1h | reversion | 58.97 | -41.03 | 219 | 33.8 | -41.53 | -6.21 | -43.36 | 257 |
| 58 | Agent (ML meta-label) | meta | 58.94 | -41.06 | 1987 | 24.7 | -30.84 | -6.42 | -31.56 | 282 |
| 59 | Z-score reversion · 1h | reversion | 56.12 | -43.88 | 233 | 34.3 | -38.42 | -5.39 | -40.80 | 257 |
| 60 | Candlestick reversal · 1h | reversion | 55.65 | -44.35 | 571 | 27.0 | -48.60 | -9.05 | -49.21 | 647 |
| 61 | VWAP momentum · 1h | momentum | 54.97 | -45.03 | 1000 | 21.7 | -59.49 | -12.06 | -62.46 | 1205 |
| 62 | Three white soldiers | momentum | 53.49 | -46.51 | 601 | 14.5 | -51.16 | -23.23 | -51.16 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -48.05 | -99.12 | 5299 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.09 | -30.12 | -83.43 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.39 | -46.82 | -94.44 | 2475 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.58 | -35.48 | -90.62 | 1948 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.96 | -45.64 | -92.01 | 2296 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.61 | -30.70 | -90.67 | 2057 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.11 | -52.87 | -98.11 | 3468 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.72 | -53.80 | -96.75 | 3387 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -37.86 | -93.71 | 2201 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.74 | -35.90 | -83.76 | 1588 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.62 | -56.63 | -99.62 | 6168 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.84 | -46.15 | -92.85 | 2538 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.76 | -38.70 | -94.80 | 3187 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -76.17 | -99.83 | 6216 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.06 | -49.42 | -93.07 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.05 | -26.31 | -78.06 | 1642 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -61.41 | -97.84 | 3401 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -59.49 | -99.10 | 5005 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.57 | -29.86 | -70.57 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.89 | -57.22 | -94.89 | 2724 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.10 | -40.59 | -86.10 | 1727 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -73.59 | -99.72 | 6447 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.93 | -31.53 | -90.99 | 2395 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.26 | -19.41 | -80.36 | 1857 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.63 | -37.52 | -91.65 | 2174 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.72 | -48.24 | -97.72 | 3955 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.09 | -57.30 | -90.10 | 2174 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.51 | -32.19 | -67.51 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.40 | -29.02 | -74.52 | 1210 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.00 | -18.82 | -82.02 | 1787 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.61 | -46.87 | -97.61 | 4360 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -116.62 | -99.94 | 8402 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T18:20 | ROC + volume · 1h | sell | PLTR | 16.34 | -0.31 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-19T18:20 | ROC + volume · 1h | sell | GOOGL | 16.11 | -0.37 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-19T18:20 | ROC + volume · 1h | sell | AMZN | 16.11 | -0.37 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-19T18:15 | RSI momentum · 1h | sell | AMZN | 17.16 | -0.37 | stop-loss |
| 2026-11-19T18:15 | EMA 9/21 cross · 1h | sell | AMZN | 15.10 | -0.34 | stop-loss |
| 2026-11-19T18:10 | Z-score reversion · 1h | buy | TECL | 4.11 | — | rebalance up |
| 2026-11-19T18:10 | Z-score reversion · 1h | buy | LABU | 4.08 | — | rebalance up |
| 2026-11-19T18:10 | Z-score reversion · 1h | sell | META | 9.36 | -0.15 | stop-loss |
| 2026-11-19T18:10 | Triple EMA stack · 1h | sell | AMZN | 17.11 | -0.33 | stop-loss |
| 2026-11-19T18:09 | Copy: Insider buying | buy | TEAM | 10.50 | — | entry |
| 2026-11-19T18:09 | Copy: Insider buying | buy | PAM | 11.29 | — | entry |
| 2026-11-19T18:09 | Copy: Insider buying | buy | ANAB | 11.29 | — | entry |
| 2026-11-19T18:09 | Copy: Insider buying | sell | PSEC | 10.28 | -1.30 | target is flat |
| 2026-11-19T18:09 | Copy: Insider buying | sell | LILA | 10.90 | -0.44 | target is flat |
| 2026-11-19T18:09 | Copy: Insider buying | sell | BH | 11.89 | 0.30 | target is flat |
| 2026-11-19T18:00 | Triple EMA stack · 1h | sell | XRP-USD | 16.46 | -0.30 | exit signal |
| 2026-11-19T18:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 15.34 | -0.20 | exit signal |
| 2026-11-19T18:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 15.52 | -0.12 | exit signal |
| 2026-11-19T18:00 | Three white soldiers | sell | DOGE-USD | 13.29 | -0.19 | stop-loss |
| 2026-11-19T18:00 | Three white soldiers | sell | AAPL | 13.36 | -0.05 | exit signal |
| 2026-11-19T17:56 | Three white soldiers | buy | AAPL | 13.41 | — | entry |
| 2026-11-19T17:45 | Three white soldiers | sell | BITX | 13.29 | -0.19 | stop-loss |
| 2026-11-19T17:41 | Agent (ML meta-label) | sell | TECL | 1.38 | -0.02 | selected signal exited |
| 2026-11-19T17:35 | Agent (ML meta-label) | buy | TECL | 1.40 | — | entry |
| 2026-11-19T17:35 | Agent (ML meta-label) | sell | AMZN | 1.40 | 0.00 | selected signal exited |
| 2026-11-19T17:35 | Three white soldiers | buy | DOGE-USD | 13.48 | — | entry signal |
| 2026-11-19T17:35 | Three white soldiers | buy | BITX | 13.48 | — | entry signal |
| 2026-11-19T17:30 | Agent (ML meta-label) | buy | AMZN | 1.40 | — | entry |
| 2026-11-19T17:30 | Williams %R · 1h | buy | TNA | 3.95 | — | entry signal |
| 2026-11-19T17:30 | Williams %R · 1h | buy | MSTR | 3.95 | — | entry signal |
| 2026-11-19T17:30 | Williams %R · 1h | buy | IWM | 3.95 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | buy | MSTR | 6.20 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | buy | IWM | 6.23 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | buy | BITX | 6.23 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | buy | AAPL | 6.23 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | LABU | 5.03 | 0.10 | rebalance down |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | ETHU | 5.03 | 0.04 | rebalance down |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | ETH-USD | 3.09 | -0.02 | rebalance down |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | COIN | 5.09 | 0.08 | rebalance down |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | BTC-USD | 4.87 | -0.03 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 18:23:05.000124+00:00 -> 2026-11-19 18:33:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 18:23:05.000124+00:00 -> 2026-11-19 18:33:05.000124+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
