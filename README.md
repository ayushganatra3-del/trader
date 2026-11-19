# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T17:24:05.000131+00:00 · 65883 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.72 (-14.28%)

Closed trades 226, win rate 36.7%, fees £6.22, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| META | 17.10 | -0.05 |
| SQQQ | 17.48 | +0.41 |
| TSLA | 17.15 | +0.03 |

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

Today: 23073 decisions in 2715 calls, $0.2963 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T17:24 | 14 / 15 / 2 | cash |  |
| Breezy | 2026-11-19T17:24 | 0 / 28 / 3 | cash |  |
| Boozy | 2026-11-19T17:24 | 9 / 21 / 1 | COIN 72% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 120.50 | 20.50 | 25 | 64.0 | 28.89 | 4.64 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.34 | 13.34 | 0 | — | 10.74 | 3.65 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.88 | 2.88 | 0 | — | 3.89 | 1.08 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -3.86 | -3.43 | -4.83 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -4.11 | -0.81 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | 1.17 | 0.45 | -9.06 | 212 |
| 10 | Agent (rotation) | meta | 95.76 | -4.24 | 210 | 28.6 | 0.45 | 0.24 | -6.64 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.43 | -5.57 | 0 | — | -5.42 | -1.83 | -7.93 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.78 | -5.44 | 20 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.09 | -6.92 | 0 | — | -6.89 | -1.81 | -8.68 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.88 | -8.12 | 8 | 50.0 | -7.40 | -0.59 | -18.69 | 6 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Insider buying | copy | 90.45 | -9.55 | 52 | 40.4 | -10.23 | -2.06 | -14.79 | 67 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.23 | -9.77 | 0 | — | -10.14 | -2.85 | -12.67 | 1 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.67 | -3.74 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 88.66 | -11.35 | 115 | 23.5 | -16.31 | -8.42 | -16.81 | 55 |
| 21 | Daily: Bullish score | daily | 87.31 | -12.69 | 17 | 17.6 | -9.99 | -2.31 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -15.91 | -9.02 | -16.11 | 70 |
| 24 | Opening range 30m | breakout | 86.17 | -13.83 | 448 | 33.5 | -11.73 | -3.93 | -14.66 | 561 |
| 25 | Agent | meta | 85.72 | -14.28 | 226 | 36.7 | -13.92 | -6.45 | -17.12 | 210 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.53 | -4.03 | -20.14 | 103 |
| 27 | Connors RSI(2) · 1h | reversion | 80.59 | -19.41 | 216 | 40.3 | -14.66 | -6.53 | -15.33 | 77 |
| 28 | Parabolic SAR · 1h | trend | 80.07 | -19.93 | 193 | 27.5 | -28.71 | -8.79 | -29.47 | 198 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.43 | -5.35 | -21.50 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -24.70 | -6.53 | -27.86 | 149 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.88 | -6.79 | -30.73 | 84 |
| 32 | Opening range 15m | breakout | 77.11 | -22.89 | 546 | 31.7 | -20.59 | -6.14 | -23.54 | 674 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 75.61 | -24.39 | 2 | 0.0 | -20.59 | -2.93 | -26.47 | 1 |
| 34 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -49.90 | -3.26 | -57.68 | 22 |
| 35 | Hold BTC | benchmark | 73.21 | -26.80 | 2 | 0.0 | -23.21 | -3.78 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 72.70 | -27.30 | 107 | 14.0 | -32.80 | -9.94 | -33.17 | 110 |
| 37 | ADX DI cross · 1h | trend | 72.13 | -27.87 | 222 | 19.4 | -30.30 | -4.78 | -36.70 | 278 |
| 38 | Stochastic reversion · 1h | reversion | 71.60 | -28.40 | 356 | 42.1 | -36.55 | -5.64 | -36.56 | 427 |
| 39 | Supertrend · 1h | trend | 70.30 | -29.70 | 192 | 16.7 | -33.01 | -5.54 | -39.57 | 209 |
| 40 | Bollinger breakout · 1h | breakout | 70.01 | -29.99 | 195 | 21.5 | -33.81 | -8.85 | -36.52 | 218 |
| 41 | Triple EMA stack · 1h | trend | 69.95 | -30.05 | 159 | 14.5 | -31.70 | -6.53 | -38.26 | 176 |
| 42 | MFI reversion · 1h | reversion | 69.78 | -30.22 | 462 | 33.8 | -29.66 | -4.48 | -31.04 | 171 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.41 | -4.99 | -37.91 | 31 |
| 44 | EMA 20/50 cross · 1h | trend | 69.37 | -30.63 | 118 | 10.2 | -37.87 | -8.30 | -44.47 | 126 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -30.05 | -6.02 | -35.94 | 208 |
| 46 | RSI momentum · 1h | momentum | 67.45 | -32.55 | 183 | 14.2 | -35.47 | -6.73 | -41.44 | 202 |
| 47 | Heikin-Ashi · 1h | trend | 67.17 | -32.83 | 480 | 22.9 | -47.58 | -10.32 | -48.49 | 629 |
| 48 | CCI reversion · 1h | reversion | 67.14 | -32.86 | 396 | 41.9 | -42.61 | -7.19 | -44.29 | 481 |
| 49 | OBV trend · 1h | momentum | 66.88 | -33.12 | 315 | 19.4 | -35.46 | -7.91 | -40.34 | 245 |
| 50 | ROC + volume · 1h | momentum | 65.65 | -34.35 | 428 | 27.8 | -38.88 | -6.92 | -43.69 | 340 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -43.19 | -2.74 | -57.50 | 39 |
| 52 | MACD cross · 1h | trend | 65.40 | -34.60 | 427 | 21.8 | -42.33 | -6.92 | -47.91 | 500 |
| 53 | Donchian 20/10 · 1h | breakout | 64.61 | -35.39 | 165 | 17.6 | -36.77 | -7.09 | -42.93 | 190 |
| 54 | Bollinger reversion · 1h | reversion | 62.43 | -37.57 | 357 | 38.1 | -39.92 | -6.14 | -40.38 | 418 |
| 55 | Williams %R · 1h | reversion | 61.97 | -38.03 | 446 | 40.6 | -48.23 | -8.56 | -48.35 | 574 |
| 56 | EMA 9/21 cross · 1h | trend | 61.69 | -38.31 | 288 | 11.5 | -40.86 | -8.04 | -46.82 | 324 |
| 57 | Agent (ML meta-label) | meta | 58.28 | -41.72 | 1985 | 24.7 | -26.28 | -4.38 | -26.28 | 269 |
| 58 | RSI(14) reversion · 1h | reversion | 58.05 | -41.95 | 219 | 33.8 | -40.80 | -5.99 | -43.36 | 265 |
| 59 | Z-score reversion · 1h | reversion | 56.20 | -43.80 | 232 | 34.5 | -38.65 | -5.44 | -40.70 | 258 |
| 60 | Candlestick reversal · 1h | reversion | 54.98 | -45.02 | 571 | 27.0 | -50.11 | -9.47 | -50.15 | 651 |
| 61 | VWAP momentum · 1h | momentum | 54.67 | -45.33 | 1000 | 21.7 | -58.89 | -12.00 | -61.69 | 1203 |
| 62 | Three white soldiers | momentum | 53.92 | -46.08 | 598 | 14.5 | -51.03 | -23.18 | -51.09 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.09 | -47.47 | -99.10 | 5311 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.07 | -29.97 | -83.33 | 1409 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.58 | -94.44 | 2481 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.45 | -35.10 | -90.62 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.99 | -46.13 | -92.04 | 2298 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.67 | -30.52 | -90.67 | 2058 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.09 | -53.07 | -98.10 | 3466 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.76 | -53.73 | -96.78 | 3409 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.75 | -37.31 | -93.76 | 2212 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.75 | -35.84 | -83.77 | 1589 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.62 | -56.44 | -99.62 | 6148 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -47.25 | -92.76 | 2546 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.78 | -38.52 | -94.78 | 3193 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -76.13 | -99.83 | 6197 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.03 | -49.63 | -93.03 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.00 | -26.94 | -78.06 | 1667 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.81 | -61.32 | -97.82 | 3409 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -59.33 | -99.10 | 4982 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.59 | -29.88 | -70.71 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.90 | -57.59 | -94.94 | 2738 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.99 | -41.11 | -86.08 | 1736 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -73.34 | -99.71 | 6433 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.96 | -31.65 | -90.99 | 2387 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.29 | -19.43 | -80.36 | 1847 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.62 | -37.46 | -91.62 | 2158 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.71 | -48.13 | -97.71 | 3947 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.97 | -59.81 | -89.97 | 2168 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.89 | -32.53 | -67.90 | 815 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.19 | -29.17 | -74.32 | 1211 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.25 | -18.86 | -82.25 | 1784 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.62 | -46.86 | -97.62 | 4361 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -113.33 | -99.94 | 8404 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | SOXL | 3.47 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | PLTR | 3.08 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | MSTR | 3.10 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | LABU | 3.11 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | ETHU | 3.13 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | COIN | 2.99 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | BITX | 3.11 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | sell | GOOGL | 6.47 | -0.02 | selected signal exited |
| 2026-11-19T17:20 | Bollinger breakout · 1h | sell | SOXL | 16.01 | -2.19 | stop-loss |
| 2026-11-19T17:20 | Donchian 20/10 · 1h | sell | GOOGL | 15.97 | -0.36 | stop-loss |
| 2026-11-19T17:20 | Donchian 20/10 · 1h | sell | AMZN | 15.95 | -0.39 | stop-loss |
| 2026-11-19T17:20 | ROC + volume · 1h | sell | SOXL | 13.08 | -0.77 | stop-loss |
| 2026-11-19T17:20 | ROC + volume · 1h | sell | GOOGL | 13.17 | -0.15 | stop-loss |
| 2026-11-19T17:20 | VWAP momentum · 1h | sell | META | 13.50 | -0.32 | stop-loss |
| 2026-11-19T17:20 | ADX DI cross · 1h | buy | TSLA | 5.34 | — | rebalance up |
| 2026-11-19T17:20 | ADX DI cross · 1h | buy | PLTR | 5.42 | — | rebalance up |
| 2026-11-19T17:20 | ADX DI cross · 1h | buy | NVDA | 5.39 | — | rebalance up |
| 2026-11-19T17:20 | ADX DI cross · 1h | buy | LABU | 5.44 | — | rebalance up |
| 2026-11-19T17:20 | ADX DI cross · 1h | buy | AMZN | 5.45 | — | rebalance up |
| 2026-11-19T17:20 | ADX DI cross · 1h | sell | SOXL | 8.97 | -0.58 | stop-loss |
| 2026-11-19T17:20 | ADX DI cross · 1h | sell | GOOGL | 9.04 | -0.11 | stop-loss |
| 2026-11-19T17:20 | MACD zero-line · 1h | sell | AMZN | 16.84 | -0.34 | stop-loss |
| 2026-11-19T17:20 | MACD cross · 1h | sell | TQQQ | 4.97 | -0.29 | stop-loss |
| 2026-11-19T17:20 | MACD cross · 1h | sell | QQQ | 5.17 | -0.09 | stop-loss |
| 2026-11-19T17:20 | MACD cross · 1h | sell | META | 3.66 | -0.04 | stop-loss |
| 2026-11-19T17:15 | Agent (ML meta-label) | sell | TECL | 4.01 | -0.33 | selected signal exited |
| 2026-11-19T17:15 | Agent | buy | META | 17.15 | — | following VWAP reversion |
| 2026-11-19T17:15 | RSI(14) reversion · 1h | buy | LABU | 2.97 | — | rebalance up |
| 2026-11-19T17:15 | ROC + volume · 1h | buy | PLTR | 3.31 | — | rebalance up |
| 2026-11-19T17:15 | ROC + volume · 1h | sell | TECL | 13.15 | -0.46 | stop-loss |
| 2026-11-19T17:15 | ROC + volume · 1h | sell | AMZN | 13.13 | -0.16 | stop-loss |
| 2026-11-19T17:15 | ADX DI cross · 1h | sell | TECL | 9.03 | -0.35 | stop-loss |
| 2026-11-19T17:10 | Agent (ML meta-label) | buy | SQQQ | 5.85 | — | following OBV trend |
| 2026-11-19T17:10 | Agent | buy | TSLA | 17.13 | — | following Stochastic reversion |
| 2026-11-19T17:10 | Williams %R · 1h | sell | META | 3.88 | -0.07 | stop-loss |
| 2026-11-19T17:05 | Agent (ML meta-label) | buy | GOOGL | 6.49 | — | entry |
| 2026-11-19T17:05 | Agent (ML meta-label) | sell | TQQQ | 4.08 | -0.26 | selected signal exited |
| 2026-11-19T17:05 | Agent (ML meta-label) | sell | SQQQ | 6.01 | 0.12 | selected signal exited |
| 2026-11-19T17:05 | MFI reversion · 1h | buy | GOOGL | 4.50 | — | rebalance up |
| 2026-11-19T17:05 | MFI reversion · 1h | sell | SPY | 8.84 | -0.12 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 17:24:05.000131+00:00 -> 2026-11-19 17:34:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 17:24:05.000131+00:00 -> 2026-11-19 17:34:05.000131+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
