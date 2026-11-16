# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T16:10:05.000125+00:00 · 62102 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.61 (-14.39%)

Closed trades 197, win rate 36.0%, fees £5.68, max drawdown -15.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.04 | -0.11 |
| SOXL | 17.35 | +0.31 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-16 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 19161 decisions in 2604 calls, $0.2508 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T16:10 | 6 / 14 / 10 | cash |  |
| Breezy | 2026-11-16T16:10 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-16T16:10 | 5 / 22 / 3 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.82 | +5.11% | 10 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| CCI reversion | SOXL | 2.19 | +16.29% | 10 |
| Bollinger reversion | TSLA | 2.18 | +2.18% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.53 | 18.53 | 0 | — | 15.60 | 5.15 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 15.38 | 3.13 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.45 | 4.45 | 0 | — | 6.22 | 1.70 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.88 | 1.88 | 34 | 41.2 | 0.98 | 0.35 | -9.64 | 31 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -2.55 | -2.21 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 6.54 | 1.83 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 1.67 | 0.47 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.46 | -2.54 | 0 | — | -1.46 | -0.43 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.71 | -5.29 | 0 | — | -5.69 | -1.50 | -8.27 | 1 |
| 14 | Agent (rotation) | meta | 93.97 | -6.03 | 195 | 29.7 | -2.93 | -1.00 | -8.11 | 153 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 16 | Copy: Insider buying | copy | 92.67 | -7.33 | 47 | 42.6 | -9.10 | -1.84 | -14.95 | 62 |
| 17 | Copy: Congress Democrats (NANC) | copy | 92.15 | -7.85 | 0 | — | -6.33 | -1.68 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.50 | -9.50 | 112 | 23.2 | -15.46 | -7.02 | -17.47 | 66 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -7.37 | -2.07 | -15.48 | 74 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.51 | -13.49 | 16 | 18.8 | -6.16 | -1.01 | -19.56 | 15 |
| 24 | Agent | meta | 85.61 | -14.39 | 197 | 36.0 | -13.94 | -6.91 | -15.66 | 197 |
| 25 | Opening range 30m | breakout | 85.59 | -14.41 | 436 | 33.5 | -11.22 | -3.60 | -14.11 | 583 |
| 26 | Parabolic SAR · 1h | trend | 83.26 | -16.74 | 180 | 28.3 | -18.08 | -3.96 | -24.82 | 215 |
| 27 | Agent (aggressive) | meta | 83.23 | -16.77 | 95 | 34.7 | -14.68 | -4.02 | -16.59 | 95 |
| 28 | Connors RSI(2) · 1h | reversion | 80.76 | -19.24 | 212 | 40.1 | -14.04 | -6.15 | -14.84 | 98 |
| 29 | Donchian 55/20 · 1h | breakout | 80.62 | -19.38 | 75 | 13.3 | -22.62 | -4.78 | -30.02 | 87 |
| 30 | Keltner breakout · 1h | breakout | 80.07 | -19.93 | 121 | 25.6 | -17.48 | -3.70 | -25.49 | 163 |
| 31 | Volume breakout · 1h | breakout | 79.63 | -20.37 | 161 | 28.6 | -16.33 | -5.17 | -21.95 | 85 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 78.11 | -21.89 | 2 | 0.0 | -13.80 | -1.69 | -24.26 | 1 |
| 33 | Opening range 15m | breakout | 77.67 | -22.33 | 530 | 31.5 | -18.27 | -4.92 | -21.36 | 702 |
| 34 | Max aggression: 5-day momentum | meta | 76.13 | -23.87 | 21 | 42.9 | -49.91 | -3.31 | -55.24 | 23 |
| 35 | Stochastic reversion · 1h | reversion | 75.60 | -24.40 | 322 | 45.3 | -30.60 | -4.61 | -32.18 | 399 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.29 | -31.62 | 116 |
| 37 | Hold BTC | benchmark | 75.33 | -24.67 | 2 | 0.0 | -15.78 | -2.22 | -28.91 | 1 |
| 38 | ADX DI cross · 1h | trend | 74.26 | -25.74 | 207 | 19.3 | -23.82 | -3.64 | -33.61 | 265 |
| 39 | Bollinger breakout · 1h | breakout | 73.97 | -26.03 | 184 | 22.3 | -24.08 | -5.02 | -31.70 | 234 |
| 40 | Max aggression: 1-day momentum | meta | 73.03 | -26.97 | 30 | 26.7 | -25.36 | -0.97 | -57.50 | 40 |
| 41 | MACD zero-line · 1h | trend | 72.25 | -27.75 | 173 | 18.5 | -23.61 | -4.53 | -31.14 | 192 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -21.85 | -2.99 | -28.68 | 162 |
| 43 | Heikin-Ashi · 1h | trend | 71.25 | -28.75 | 459 | 23.3 | -38.60 | -7.07 | -43.26 | 653 |
| 44 | Supertrend · 1h | trend | 71.03 | -28.97 | 186 | 15.6 | -32.88 | -5.60 | -39.67 | 200 |
| 45 | RSI momentum · 1h | momentum | 70.92 | -29.08 | 174 | 13.8 | -28.84 | -4.68 | -38.47 | 204 |
| 46 | MACD cross · 1h | trend | 70.81 | -29.19 | 401 | 22.7 | -32.95 | -4.68 | -42.72 | 468 |
| 47 | Triple EMA stack · 1h | trend | 70.80 | -29.20 | 153 | 14.4 | -26.72 | -4.31 | -37.83 | 194 |
| 48 | EMA 20/50 cross · 1h | trend | 70.66 | -29.34 | 111 | 9.9 | -33.61 | -7.81 | -40.16 | 114 |
| 49 | ROC + volume · 1h | momentum | 70.45 | -29.55 | 404 | 28.5 | -27.02 | -4.21 | -37.69 | 356 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.92 | -4.96 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.75 | -31.25 | 301 | 19.3 | -30.54 | -5.28 | -39.92 | 265 |
| 52 | CCI reversion · 1h | reversion | 68.39 | -31.61 | 372 | 41.7 | -39.08 | -6.32 | -41.88 | 460 |
| 53 | Bollinger reversion · 1h | reversion | 67.34 | -32.66 | 319 | 40.4 | -34.31 | -5.26 | -35.59 | 392 |
| 54 | Donchian 20/10 · 1h | breakout | 67.28 | -32.72 | 157 | 18.5 | -29.12 | -4.48 | -39.22 | 206 |
| 55 | Williams %R · 1h | reversion | 64.47 | -35.53 | 413 | 41.4 | -44.41 | -7.56 | -44.93 | 540 |
| 56 | EMA 9/21 cross · 1h | trend | 64.43 | -35.57 | 269 | 11.5 | -34.59 | -5.67 | -44.04 | 318 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -21.68 | -4.05 | -27.32 | 343 |
| 58 | RSI(14) reversion · 1h | reversion | 60.48 | -39.52 | 201 | 32.3 | -39.41 | -5.82 | -40.82 | 238 |
| 59 | Z-score reversion · 1h | reversion | 59.86 | -40.14 | 221 | 35.7 | -34.51 | -4.73 | -35.77 | 237 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.85 | -10.20 | -56.97 | 1211 |
| 61 | Candlestick reversal · 1h | reversion | 57.86 | -42.14 | 526 | 27.2 | -43.07 | -7.57 | -45.27 | 610 |
| 62 | Three white soldiers | momentum | 57.13 | -42.88 | 563 | 14.7 | -49.61 | -22.15 | -49.70 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -42.27 | -99.02 | 5331 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.28 | -25.89 | -81.28 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.87 | -43.60 | -93.87 | 2515 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.04 | -32.81 | -90.05 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.51 | -41.13 | -91.51 | 2334 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.94 | -30.36 | -89.94 | 2152 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -48.47 | -97.89 | 3463 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -54.88 | -96.32 | 3434 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.39 | -35.09 | -93.39 | 2265 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.72 | -32.78 | -82.73 | 1643 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.81 | -99.61 | 6026 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.11 | -42.73 | -92.11 | 2590 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.20 | -35.67 | -95.20 | 3378 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -69.97 | -99.81 | 6131 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.42 | -42.79 | -92.42 | 2267 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.57 | -26.47 | -76.57 | 1662 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -56.15 | -97.60 | 3471 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.99 | -56.21 | -99.00 | 4928 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.37 | -26.76 | -68.56 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -56.24 | -94.70 | 2767 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.85 | -37.74 | -84.85 | 1764 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -67.97 | -99.70 | 6367 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.38 | -29.56 | -90.46 | 2332 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.89 | -18.82 | -80.19 | 1814 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.99 | -35.78 | -91.04 | 2175 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.45 | -44.22 | -97.47 | 3903 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.19 | -61.02 | -89.19 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.33 | -29.19 | -66.33 | 826 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.39 | -23.03 | -72.40 | 1254 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.96 | -17.11 | -80.77 | 1744 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.54 | -45.10 | -97.57 | 4330 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -96.06 | -99.93 | 8380 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T16:10 | Three white soldiers | sell | XRP-USD | 14.17 | -0.12 | exit signal |
| 2026-11-16T16:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 101.88 | -2.00 | target is flat |
| 2026-11-16T16:00 | Agent | sell | TSLA | 17.23 | 0.19 | selected signal exited |
| 2026-11-16T16:00 | Candlestick reversal · 1h | buy | BTC-USD | 2.87 | — | rebalance up |
| 2026-11-16T16:00 | ROC + volume · 1h | sell | ETH-USD | 17.36 | -0.34 | exit signal |
| 2026-11-16T16:00 | MACD cross · 1h | buy | SQQQ | 5.18 | — | rebalance up |
| 2026-11-16T16:00 | MACD cross · 1h | buy | NVDA | 5.27 | — | rebalance up |
| 2026-11-16T16:00 | MACD cross · 1h | buy | ETH-USD | 5.35 | — | rebalance up |
| 2026-11-16T16:00 | MACD cross · 1h | buy | DOGE-USD | 5.35 | — | rebalance up |
| 2026-11-16T16:00 | MACD cross · 1h | buy | BTC-USD | 5.32 | — | rebalance up |
| 2026-11-16T16:00 | MACD cross · 1h | sell | XRP-USD | 8.80 | -0.15 | exit signal |
| 2026-11-16T16:00 | MACD cross · 1h | sell | SOL-USD | 8.79 | -0.17 | exit signal |
| 2026-11-16T16:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 16.11 | — | entry signal |
| 2026-11-16T15:55 | Agent (rotation) | sell | SQQQ | 7.75 | -0.09 | selected signal exited |
| 2026-11-16T15:55 | Agent (aggressive) | buy | COIN | 41.75 | — | following MACD cross |
| 2026-11-16T15:55 | Agent | buy | COIN | 17.15 | — | following MACD cross |
| 2026-11-16T15:55 | Gap and go | sell | SQQQ | 24.82 | -0.29 | exit signal |
| 2026-11-16T15:50 | Supertrend · 1h | buy | SQQQ | 3.60 | — | rebalance up |
| 2026-11-16T15:50 | Three white soldiers | buy | XRP-USD | 14.29 | — | entry signal |
| 2026-11-16T15:50 | Three white soldiers | buy | META | 14.29 | — | entry signal |
| 2026-11-16T15:40 | Three white soldiers | buy | MSFT | 14.29 | — | entry signal |
| 2026-11-16T15:38 | Copy: Insider buying | buy | STWD | 3.05 | — | entry |
| 2026-11-16T15:38 | Copy: Insider buying | buy | PSEC | 11.58 | — | entry |
| 2026-11-16T15:38 | Copy: Insider buying | buy | MDGL | 8.04 | — | rebalance up |
| 2026-11-16T15:38 | Copy: Insider buying | buy | FUN | 11.58 | — | entry |
| 2026-11-16T15:38 | Copy: Insider buying | buy | BH | 11.58 | — | entry |
| 2026-11-16T15:38 | Copy: Insider buying | sell | MGM | 11.88 | 0.68 | target is flat |
| 2026-11-16T15:38 | Copy: Insider buying | sell | KNOP | 11.72 | 0.34 | target is flat |
| 2026-11-16T15:38 | Copy: Insider buying | sell | BBTX | 11.07 | -0.01 | target is flat |
| 2026-11-16T15:38 | Copy: Insider buying | sell | ASPE | 11.17 | 0.32 | target is flat |
| 2026-11-16T15:35 | CCI reversion · 1h | buy | XRP-USD | 4.58 | — | rebalance up |
| 2026-11-16T15:35 | CCI reversion · 1h | buy | DOGE-USD | 4.57 | — | rebalance up |
| 2026-11-16T15:35 | CCI reversion · 1h | buy | BTC-USD | 4.55 | — | rebalance up |
| 2026-11-16T15:35 | CCI reversion · 1h | sell | AMD | 6.78 | -0.22 | stop-loss |
| 2026-11-16T15:35 | Candlestick reversal · 1h | buy | NVDA | 4.78 | — | rebalance up |
| 2026-11-16T15:35 | Candlestick reversal · 1h | buy | MSFT | 4.72 | — | rebalance up |
| 2026-11-16T15:35 | Candlestick reversal · 1h | buy | AMD | 2.93 | — | rebalance up |
| 2026-11-16T15:35 | Candlestick reversal · 1h | sell | LABU | 11.47 | -0.07 | stop-loss |
| 2026-11-16T15:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 103.88 | — | entry |
| 2026-11-16T15:30 | Williams %R · 1h | buy | XRP-USD | 3.86 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 16:10:05.000125+00:00 -> 2026-11-16 16:20:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 16:10:05.000125+00:00 -> 2026-11-16 16:20:05.000125+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
