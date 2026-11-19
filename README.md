# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T20:20:05.000168+00:00 · 66036 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.41 (-14.59%)

Closed trades 229, win rate 36.7%, fees £6.28, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| META | 17.01 | -0.05 |
| SOXL | 17.07 | -0.01 |
| SQQQ | 17.17 | +0.07 |
| TSLA | 17.22 | +0.10 |

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

Today: 36864 decisions in 3174 calls, $0.4579 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T20:20 | 4 / 21 / 5 | TNA 15% |  |
| Breezy | 2026-11-19T20:20 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-19T20:20 | 8 / 21 / 1 | BITX 68% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.72 | 21.72 | 25 | 64.0 | 24.83 | 4.05 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.33 | 14.33 | 0 | — | 12.25 | 4.10 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.32 | 3.32 | 0 | — | 4.34 | 1.25 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.10 | -3.64 | -4.86 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.61 | -0.39 | 39 | 41.0 | -2.10 | -0.35 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.76 | -0.50 | -9.06 | 201 |
| 10 | Agent (rotation) | meta | 96.10 | -3.90 | 210 | 28.6 | -1.11 | -0.31 | -7.73 | 153 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.34 | -5.66 | 0 | — | -6.69 | -2.29 | -8.32 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.16 | -6.84 | 0 | — | -6.89 | -1.81 | -8.68 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.56 | -8.05 | -9.88 | 23 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.35 | -8.65 | 8 | 50.0 | -10.00 | -0.78 | -18.69 | 6 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.07 | -9.93 | 0 | — | -10.58 | -2.98 | -12.87 | 1 |
| 18 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.67 | -3.74 | -18.48 | 149 |
| 19 | Copy: Insider buying | copy | 89.64 | -10.36 | 55 | 40.0 | -9.40 | -1.86 | -14.79 | 67 |
| 20 | Trend pullback · 1h | trend | 89.59 | -10.40 | 115 | 23.5 | -11.15 | -6.52 | -12.77 | 49 |
| 21 | Daily: Bullish score | daily | 87.35 | -12.65 | 17 | 17.6 | -14.60 | -3.87 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.40 | -13.60 | 448 | 33.5 | -11.54 | -3.84 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.61 | -18.94 | 71 |
| 25 | Agent | meta | 85.41 | -14.59 | 229 | 36.7 | -13.62 | -6.15 | -16.51 | 213 |
| 26 | Agent (aggressive) | meta | 83.73 | -16.27 | 106 | 34.0 | -15.36 | -3.98 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 81.18 | -18.82 | 194 | 27.8 | -27.11 | -8.33 | -28.86 | 196 |
| 28 | Connors RSI(2) · 1h | reversion | 80.47 | -19.53 | 217 | 40.6 | -14.80 | -6.60 | -15.33 | 78 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.50 | -5.38 | -21.55 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.50 | -6.24 | -25.33 | 143 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -26.22 | -6.92 | -30.88 | 84 |
| 32 | Opening range 15m | breakout | 77.33 | -22.68 | 546 | 31.7 | -21.22 | -6.52 | -23.60 | 658 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 74.79 | -25.21 | 2 | 0.0 | -24.05 | -3.46 | -27.33 | 1 |
| 34 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -52.79 | -3.69 | -57.68 | 21 |
| 35 | Ichimoku · 1h | trend | 73.47 | -26.53 | 107 | 14.0 | -30.90 | -9.55 | -32.08 | 109 |
| 36 | Hold BTC | benchmark | 73.35 | -26.65 | 2 | 0.0 | -23.49 | -3.76 | -28.91 | 1 |
| 37 | ADX DI cross · 1h | trend | 72.79 | -27.21 | 225 | 20.0 | -28.70 | -4.55 | -35.87 | 279 |
| 38 | Stochastic reversion · 1h | reversion | 71.58 | -28.42 | 356 | 42.1 | -36.16 | -5.55 | -36.67 | 426 |
| 39 | Supertrend · 1h | trend | 70.12 | -29.88 | 196 | 16.8 | -33.17 | -5.57 | -39.70 | 204 |
| 40 | Triple EMA stack · 1h | trend | 70.12 | -29.88 | 161 | 14.3 | -30.41 | -6.26 | -37.24 | 170 |
| 41 | Bollinger breakout · 1h | breakout | 70.01 | -29.99 | 195 | 21.5 | -33.45 | -8.72 | -36.22 | 217 |
| 42 | MFI reversion · 1h | reversion | 69.64 | -30.36 | 464 | 33.6 | -29.25 | -4.41 | -31.07 | 173 |
| 43 | EMA 20/50 cross · 1h | trend | 69.63 | -30.37 | 118 | 10.2 | -36.64 | -7.93 | -43.94 | 127 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -28.11 | -5.62 | -34.12 | 207 |
| 46 | Heikin-Ashi · 1h | trend | 67.97 | -32.03 | 483 | 23.0 | -46.38 | -10.35 | -47.85 | 619 |
| 47 | RSI momentum · 1h | momentum | 67.66 | -32.34 | 184 | 14.1 | -35.36 | -6.78 | -41.55 | 203 |
| 48 | OBV trend · 1h | momentum | 67.59 | -32.41 | 315 | 19.4 | -35.70 | -7.91 | -41.18 | 240 |
| 49 | CCI reversion · 1h | reversion | 66.83 | -33.17 | 398 | 42.0 | -42.47 | -7.16 | -44.29 | 479 |
| 50 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -46.45 | -3.17 | -57.50 | 38 |
| 51 | MACD cross · 1h | trend | 65.30 | -34.70 | 430 | 21.6 | -42.92 | -6.99 | -48.92 | 495 |
| 52 | ROC + volume · 1h ⏸ | momentum | 64.82 | -35.18 | 431 | 27.6 | -40.04 | -6.97 | -44.84 | 342 |
| 53 | Donchian 20/10 · 1h | breakout | 64.61 | -35.39 | 165 | 17.6 | -37.16 | -7.22 | -43.17 | 191 |
| 54 | Bollinger reversion · 1h | reversion | 62.38 | -37.62 | 357 | 38.1 | -39.17 | -5.97 | -40.36 | 416 |
| 55 | EMA 9/21 cross · 1h | trend | 61.96 | -38.04 | 291 | 11.3 | -41.07 | -8.04 | -47.32 | 323 |
| 56 | Williams %R · 1h | reversion | 61.79 | -38.21 | 447 | 40.5 | -48.05 | -8.50 | -48.33 | 574 |
| 57 | Agent (ML meta-label) | meta | 58.48 | -41.52 | 1991 | 24.7 | -29.24 | -5.37 | -29.67 | 320 |
| 58 | RSI(14) reversion · 1h | reversion | 58.29 | -41.71 | 219 | 33.8 | -39.97 | -5.78 | -43.48 | 271 |
| 59 | Z-score reversion · 1h | reversion | 55.84 | -44.16 | 233 | 34.3 | -38.54 | -5.39 | -41.55 | 256 |
| 60 | Candlestick reversal · 1h | reversion | 55.14 | -44.86 | 576 | 26.9 | -49.25 | -9.22 | -49.56 | 671 |
| 61 | VWAP momentum · 1h | momentum | 54.48 | -45.52 | 1003 | 21.6 | -57.62 | -11.74 | -60.81 | 1191 |
| 62 | Three white soldiers | momentum | 52.98 | -47.02 | 608 | 14.3 | -51.66 | -23.34 | -51.66 | 665 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -47.83 | -99.10 | 5283 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.24 | -30.46 | -83.44 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.43 | -47.00 | -94.46 | 2463 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.65 | -35.38 | -90.65 | 1943 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.06 | -45.64 | -92.10 | 2289 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.47 | -30.46 | -90.55 | 2040 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -51.65 | -98.15 | 3482 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -52.77 | -96.73 | 3371 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.78 | -36.81 | -93.80 | 2220 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.72 | -35.79 | -83.72 | 1586 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.63 | -57.21 | -99.63 | 6219 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.92 | -46.60 | -92.92 | 2531 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.71 | -38.63 | -94.77 | 3181 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -75.88 | -99.83 | 6236 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.20 | -48.77 | -93.21 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.33 | -25.49 | -78.35 | 1625 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.92 | -97.83 | 3385 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -59.30 | -99.10 | 5025 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.74 | -29.71 | -70.74 | 1232 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.91 | -57.03 | -94.91 | 2719 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.11 | -40.58 | -86.12 | 1711 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -73.82 | -99.72 | 6473 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.95 | -31.74 | -90.98 | 2396 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.52 | -19.31 | -80.59 | 1878 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.63 | -37.50 | -91.67 | 2170 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.69 | -47.73 | -97.71 | 3971 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.05 | -56.38 | -90.05 | 2175 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.54 | -32.03 | -67.54 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.46 | -29.14 | -74.57 | 1207 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.39 | -18.94 | -82.47 | 1807 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.62 | -47.08 | -97.63 | 4373 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.51 | -99.94 | 8412 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T20:20 | Agent (aggressive) | buy | SOXL | 41.87 | — | following CCI reversion, Z-score reversion |
| 2026-11-19T20:20 | Agent | buy | SOXL | 17.08 | — | following CCI reversion, Z-score reversion |
| 2026-11-19T20:05 | Agent (ML meta-label) | buy | TSLA | 2.05 | — | following Stochastic reversion |
| 2026-11-19T20:05 | Agent (ML meta-label) | buy | TQQQ | 6.46 | — | entry |
| 2026-11-19T20:05 | Agent (ML meta-label) | sell | TECL | 7.21 | -0.09 | selected signal exited |
| 2026-11-19T20:05 | MFI reversion · 1h | buy | TSLA | 7.98 | — | rebalance up |
| 2026-11-19T20:05 | MFI reversion · 1h | sell | QQQ | 9.90 | -0.22 | stop-loss |
| 2026-11-19T20:00 | Agent (ML meta-label) | buy | TECL | 7.31 | — | entry |
| 2026-11-19T20:00 | CCI reversion · 1h | buy | AAPL | 7.66 | — | rebalance up |
| 2026-11-19T20:00 | CCI reversion · 1h | sell | NVDA | 9.34 | -0.41 | stop-loss |
| 2026-11-19T20:00 | Candlestick reversal · 1h | buy | TQQQ | 2.99 | — | entry |
| 2026-11-19T20:00 | Candlestick reversal · 1h | buy | TECL | 5.02 | — | entry |
| 2026-11-19T20:00 | Candlestick reversal · 1h | buy | SOXL | 5.02 | — | entry |
| 2026-11-19T20:00 | Candlestick reversal · 1h | sell | SOL-USD | 6.87 | -0.14 | exit signal |
| 2026-11-19T20:00 | Candlestick reversal · 1h | sell | BTC-USD | 6.15 | -0.10 | exit signal |
| 2026-11-19T20:00 | Supertrend · 1h | sell | BTC-USD | 17.34 | -0.42 | exit signal |
| 2026-11-19T20:00 | MACD cross · 1h | sell | GOOGL | 5.92 | -0.15 | stop-loss |
| 2026-11-19T19:55 | Agent | buy | SQQQ | 17.10 | — | following OBV trend |
| 2026-11-19T19:50 | Agent (ML meta-label) | sell | TECL | 7.30 | -0.06 | selected signal exited |
| 2026-11-19T19:50 | MACD cross · 1h | buy | MSFT | 3.59 | — | rebalance up |
| 2026-11-19T19:50 | MACD cross · 1h | buy | COIN | 3.49 | — | rebalance up |
| 2026-11-19T19:50 | MACD cross · 1h | sell | NVDA | 5.10 | -0.19 | stop-loss |
| 2026-11-19T19:46 | Agent (ML meta-label) | buy | TECL | 7.36 | — | entry |
| 2026-11-19T19:40 | Williams %R · 1h | buy | DOGE-USD | 3.45 | — | entry |
| 2026-11-19T19:40 | Williams %R · 1h | sell | NVDA | 3.81 | -0.15 | stop-loss |
| 2026-11-19T19:36 | Agent (aggressive) | sell | SOXL | 41.73 | -0.30 | selected signal exited |
| 2026-11-19T19:36 | Agent | sell | SOXL | 17.01 | -0.12 | selected signal exited |
| 2026-11-19T19:31 | Agent | sell | SQQQ | 17.35 | 0.28 | selected signal exited |
| 2026-11-19T19:31 | CCI reversion · 1h | buy | AAPL | 3.47 | — | entry signal |
| 2026-11-19T19:31 | Bollinger reversion · 1h | buy | TNA | 15.63 | — | entry signal |
| 2026-11-19T19:31 | Connors RSI(2) · 1h | sell | AAPL | 20.26 | 0.11 | exit signal |
| 2026-11-19T19:31 | Candlestick reversal · 1h | buy | QQQ | 2.87 | — | entry signal |
| 2026-11-19T19:31 | Candlestick reversal · 1h | buy | PLTR | 4.28 | — | entry signal |
| 2026-11-19T19:31 | Candlestick reversal · 1h | buy | MSFT | 4.28 | — | entry signal |
| 2026-11-19T19:31 | VWAP momentum · 1h | buy | AAPL | 13.57 | — | entry signal |
| 2026-11-19T19:31 | VWAP momentum · 1h | sell | ETHU | 13.47 | -0.14 | exit signal |
| 2026-11-19T19:31 | Heikin-Ashi · 1h | buy | SQQQ | 16.92 | — | entry signal |
| 2026-11-19T19:25 | MFI reversion · 1h | buy | TSLA | 1.96 | — | entry |
| 2026-11-19T19:25 | RSI(14) reversion · 1h | buy | COIN | 2.79 | — | rebalance up |
| 2026-11-19T19:25 | Candlestick reversal · 1h | sell | MSTR | 6.08 | -0.13 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 20:20:05.000168+00:00 -> 2026-11-19 20:30:05.000168+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 20:20:05.000168+00:00 -> 2026-11-19 20:30:05.000168+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
