# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T19:21:05.000124+00:00 · 65988 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.19 (-14.81%)

Closed trades 227, win rate 36.6%, fees £6.24, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| META | 17.04 | -0.02 |
| SOXL | 16.58 | -0.55 |
| SQQQ | 17.57 | +0.50 |
| TSLA | 17.26 | +0.13 |

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

Today: 32547 decisions in 3030 calls, $0.4072 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T19:21 | 6 / 17 / 7 | cash |  |
| Breezy | 2026-11-19T19:21 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-19T19:21 | 6 / 21 / 3 | ETHU 60% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.09 | 21.09 | 25 | 64.0 | 29.87 | 4.66 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.14 | 14.14 | 0 | — | 12.37 | 4.16 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.27 | 3.27 | 0 | — | 3.70 | 1.15 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.23 | -3.79 | -4.99 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 39 | 41.0 | -2.78 | -0.51 | -9.74 | 36 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -2.27 | -0.67 | -9.06 | 205 |
| 10 | Agent (rotation) | meta | 95.93 | -4.07 | 210 | 28.6 | -0.82 | -0.22 | -7.49 | 152 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.47 | -5.53 | 0 | — | -6.38 | -2.17 | -8.00 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.19 | -6.81 | 0 | — | -6.89 | -1.81 | -8.68 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.74 | -8.26 | 8 | 50.0 | -8.08 | -0.61 | -18.69 | 6 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.19 | -9.80 | 0 | — | -10.46 | -2.95 | -12.78 | 1 |
| 18 | Copy: Insider buying | copy | 90.02 | -9.98 | 55 | 40.0 | -9.15 | -1.79 | -14.79 | 67 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.66 | -3.74 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 89.48 | -10.53 | 115 | 23.5 | -13.84 | -7.01 | -15.29 | 52 |
| 21 | Daily: Bullish score | daily | 87.30 | -12.70 | 17 | 17.6 | -11.14 | -2.33 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.28 | -9.17 | -16.28 | 71 |
| 24 | Opening range 30m | breakout | 86.28 | -13.72 | 448 | 33.5 | -11.62 | -3.88 | -14.66 | 561 |
| 25 | Agent | meta | 85.19 | -14.81 | 227 | 36.6 | -14.46 | -6.78 | -17.14 | 209 |
| 26 | Agent (aggressive) | meta | 82.70 | -17.30 | 105 | 34.3 | -16.58 | -4.29 | -19.99 | 99 |
| 27 | Parabolic SAR · 1h | trend | 81.07 | -18.93 | 194 | 27.8 | -27.53 | -8.45 | -29.17 | 199 |
| 28 | Connors RSI(2) · 1h | reversion | 80.52 | -19.48 | 216 | 40.3 | -14.77 | -6.58 | -15.33 | 78 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.45 | -5.37 | -21.50 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -24.70 | -6.53 | -27.86 | 149 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -26.20 | -6.92 | -30.86 | 84 |
| 32 | Opening range 15m | breakout | 77.22 | -22.78 | 546 | 31.7 | -20.58 | -6.16 | -23.55 | 667 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 75.20 | -24.80 | 2 | 0.0 | -23.31 | -3.34 | -26.96 | 1 |
| 34 | Hold BTC | benchmark | 73.76 | -26.24 | 2 | 0.0 | -22.96 | -3.68 | -28.91 | 1 |
| 35 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -49.36 | -3.22 | -57.68 | 22 |
| 36 | Ichimoku · 1h | trend | 73.37 | -26.63 | 107 | 14.0 | -31.74 | -9.69 | -32.81 | 112 |
| 37 | ADX DI cross · 1h | trend | 72.76 | -27.24 | 225 | 20.0 | -29.99 | -4.78 | -36.82 | 279 |
| 38 | Stochastic reversion · 1h | reversion | 71.72 | -28.28 | 356 | 42.1 | -36.43 | -5.62 | -36.56 | 427 |
| 39 | Supertrend · 1h | trend | 70.38 | -29.62 | 195 | 16.9 | -34.11 | -5.74 | -40.56 | 208 |
| 40 | Triple EMA stack · 1h | trend | 70.04 | -29.96 | 161 | 14.3 | -32.21 | -6.69 | -38.83 | 171 |
| 41 | Bollinger breakout · 1h | breakout | 70.01 | -29.99 | 195 | 21.5 | -33.89 | -8.87 | -36.62 | 218 |
| 42 | MFI reversion · 1h | reversion | 69.98 | -30.02 | 463 | 33.7 | -29.60 | -4.47 | -31.36 | 172 |
| 43 | EMA 20/50 cross · 1h | trend | 69.57 | -30.43 | 118 | 10.2 | -37.94 | -8.61 | -44.44 | 122 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.37 | -4.99 | -37.91 | 31 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -30.60 | -6.14 | -36.31 | 206 |
| 46 | Heikin-Ashi · 1h | trend | 67.68 | -32.32 | 483 | 23.0 | -46.95 | -10.40 | -48.19 | 626 |
| 47 | RSI momentum · 1h | momentum | 67.57 | -32.43 | 184 | 14.1 | -35.48 | -6.80 | -41.58 | 204 |
| 48 | OBV trend · 1h | momentum | 67.50 | -32.50 | 315 | 19.4 | -35.70 | -8.16 | -40.92 | 243 |
| 49 | CCI reversion · 1h | reversion | 67.14 | -32.86 | 397 | 42.1 | -42.52 | -7.17 | -44.29 | 481 |
| 50 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -42.09 | -2.65 | -57.50 | 39 |
| 51 | MACD cross · 1h | trend | 65.55 | -34.45 | 428 | 21.7 | -43.45 | -7.10 | -49.07 | 493 |
| 52 | ROC + volume · 1h ⏸ | momentum | 64.82 | -35.18 | 431 | 27.6 | -39.58 | -6.90 | -44.42 | 341 |
| 53 | Donchian 20/10 · 1h | breakout | 64.61 | -35.39 | 165 | 17.6 | -36.89 | -7.18 | -42.93 | 191 |
| 54 | Bollinger reversion · 1h | reversion | 62.49 | -37.51 | 357 | 38.1 | -39.88 | -6.13 | -40.37 | 418 |
| 55 | Williams %R · 1h | reversion | 62.00 | -38.01 | 446 | 40.6 | -48.18 | -8.56 | -48.41 | 579 |
| 56 | EMA 9/21 cross · 1h | trend | 61.88 | -38.12 | 291 | 11.3 | -40.94 | -8.07 | -47.13 | 324 |
| 57 | Agent (ML meta-label) | meta | 58.76 | -41.24 | 1988 | 24.7 | -25.80 | -4.36 | -26.70 | 282 |
| 58 | RSI(14) reversion · 1h | reversion | 58.55 | -41.45 | 219 | 33.8 | -40.49 | -5.92 | -43.35 | 265 |
| 59 | Z-score reversion · 1h | reversion | 55.89 | -44.11 | 233 | 34.3 | -38.75 | -5.43 | -41.10 | 257 |
| 60 | Candlestick reversal · 1h | reversion | 55.44 | -44.56 | 573 | 27.1 | -49.50 | -9.30 | -49.85 | 663 |
| 61 | VWAP momentum · 1h | momentum | 54.35 | -45.65 | 1000 | 21.7 | -59.65 | -12.06 | -62.40 | 1201 |
| 62 | Three white soldiers | momentum | 52.98 | -47.02 | 608 | 14.3 | -51.56 | -23.04 | -51.56 | 667 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -48.68 | -99.12 | 5300 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.22 | -30.21 | -83.42 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.43 | -47.06 | -94.46 | 2469 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.59 | -35.32 | -90.60 | 1946 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.08 | -45.34 | -92.09 | 2295 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.48 | -30.48 | -90.54 | 2046 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.13 | -52.27 | -98.13 | 3475 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.75 | -53.70 | -96.76 | 3378 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -36.16 | -93.74 | 2202 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.74 | -35.90 | -83.76 | 1588 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.63 | -56.71 | -99.63 | 6190 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.92 | -46.60 | -92.92 | 2533 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.73 | -38.70 | -94.78 | 3186 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -75.66 | -99.83 | 6234 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.18 | -48.59 | -93.18 | 2268 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.13 | -26.31 | -78.14 | 1621 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.84 | -97.82 | 3392 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -59.45 | -99.10 | 5007 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.59 | -29.93 | -70.59 | 1223 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.88 | -57.37 | -94.88 | 2718 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.01 | -40.25 | -86.02 | 1720 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -73.86 | -99.72 | 6452 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.93 | -31.63 | -90.97 | 2396 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.45 | -19.43 | -80.51 | 1868 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.69 | -37.75 | -91.69 | 2183 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.69 | -47.78 | -97.72 | 3954 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.06 | -57.43 | -90.06 | 2167 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.47 | -32.12 | -67.47 | 797 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.41 | -29.06 | -74.52 | 1207 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.15 | -18.87 | -82.15 | 1795 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.61 | -46.84 | -97.61 | 4365 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.74 | -99.94 | 8413 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T19:20 | Agent (ML meta-label) | buy | TECL | 7.35 | — | entry |
| 2026-11-19T19:15 | Agent | buy | META | 17.06 | — | following VWAP reversion |
| 2026-11-19T19:05 | MFI reversion · 1h | buy | MSTR | 10.01 | — | entry |
| 2026-11-19T19:05 | MFI reversion · 1h | sell | GOOGL | 11.46 | -0.14 | stop-loss |
| 2026-11-19T19:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 98.59 | — | entry |
| 2026-11-19T19:00 | MACD cross · 1h | buy | MSTR | 3.46 | — | rebalance up |
| 2026-11-19T19:00 | MACD cross · 1h | buy | GOOGL | 3.47 | — | rebalance up |
| 2026-11-19T19:00 | MACD cross · 1h | sell | AMZN | 5.13 | -0.09 | stop-loss |
| 2026-11-19T18:55 | Agent | sell | META | 16.94 | -0.20 | selected signal exited |
| 2026-11-19T18:50 | ADX DI cross · 1h | buy | LABU | 3.73 | — | rebalance up |
| 2026-11-19T18:50 | Three white soldiers | sell | XRP-USD | 13.21 | -0.12 | exit signal |
| 2026-11-19T18:50 | Three white soldiers | sell | SOL-USD | 13.21 | -0.13 | exit signal |
| 2026-11-19T18:45 | Three white soldiers | buy | XRP-USD | 5.68 | — | rebalance up |
| 2026-11-19T18:45 | Three white soldiers | buy | SOL-USD | 5.68 | — | rebalance up |
| 2026-11-19T18:45 | Three white soldiers | sell | UPRO | 7.54 | -0.05 | exit signal |
| 2026-11-19T18:45 | Three white soldiers | sell | TNA | 7.57 | -0.06 | exit signal |
| 2026-11-19T18:45 | Three white soldiers | sell | SPY | 7.60 | -0.02 | exit signal |
| 2026-11-19T18:45 | Three white soldiers | sell | IWM | 7.60 | -0.02 | exit signal |
| 2026-11-19T18:40 | ADX DI cross · 1h | buy | TSLA | 3.66 | — | rebalance up |
| 2026-11-19T18:40 | Three white soldiers | sell | NVDA | 7.61 | -0.02 | exit signal |
| 2026-11-19T18:35 | Three white soldiers | buy | UPRO | 7.59 | — | entry signal |
| 2026-11-19T18:35 | Three white soldiers | buy | TNA | 7.63 | — | entry signal |
| 2026-11-19T18:35 | Three white soldiers | buy | SPY | 7.63 | — | entry signal |
| 2026-11-19T18:35 | Three white soldiers | buy | IWM | 7.63 | — | entry signal |
| 2026-11-19T18:35 | Three white soldiers | sell | XRP-USD | 5.69 | -0.03 | rebalance down |
| 2026-11-19T18:35 | Three white soldiers | sell | SOL-USD | 5.68 | -0.04 | rebalance down |
| 2026-11-19T18:35 | Three white soldiers | sell | NVDA | 5.73 | -0.01 | rebalance down |
| 2026-11-19T18:30 | Agent (ML meta-label) | sell | PLTR | 7.29 | -0.13 | selected signal exited |
| 2026-11-19T18:30 | CCI reversion · 1h | buy | MSTR | 3.85 | — | rebalance up |
| 2026-11-19T18:30 | CCI reversion · 1h | buy | LABU | 3.95 | — | rebalance up |
| 2026-11-19T18:30 | CCI reversion · 1h | buy | ETHU | 4.00 | — | rebalance up |
| 2026-11-19T18:30 | CCI reversion · 1h | buy | COIN | 3.71 | — | rebalance up |
| 2026-11-19T18:30 | CCI reversion · 1h | sell | SQQQ | 8.94 | 0.44 | exit signal |
| 2026-11-19T18:30 | Connors RSI(2) · 1h | buy | AMZN | 20.18 | — | entry signal |
| 2026-11-19T18:30 | Candlestick reversal · 1h | buy | SOL-USD | 7.01 | — | entry |
| 2026-11-19T18:30 | Candlestick reversal · 1h | sell | LABU | 6.14 | 0.04 | exit signal |
| 2026-11-19T18:30 | Candlestick reversal · 1h | sell | AAPL | 6.22 | -0.01 | exit signal |
| 2026-11-19T18:30 | RSI momentum · 1h | buy | SQQQ | 16.83 | — | entry signal |
| 2026-11-19T18:30 | VWAP momentum · 1h | buy | ETHU | 13.61 | — | entry signal |
| 2026-11-19T18:30 | VWAP momentum · 1h | buy | BITX | 13.73 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 19:21:05.000124+00:00 -> 2026-11-19 19:31:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 19:21:05.000124+00:00 -> 2026-11-19 19:31:05.000124+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
