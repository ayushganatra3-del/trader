# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T17:09:05.000173+00:00 · 62151 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.02 (-13.98%)

Closed trades 198, win rate 36.4%, fees £5.69, max drawdown -15.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.10 | -0.05 |

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

Today: 23547 decisions in 2751 calls, $0.3021 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T17:09 | 1 / 9 / 20 | cash |  |
| Breezy | 2026-11-16T17:09 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-16T17:09 | 4 / 19 / 7 | BITX 69% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.50 | 18.50 | 0 | — | 15.64 | 5.16 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 15.38 | 3.13 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.98 | 3.98 | 0 | — | 5.73 | 1.57 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.88 | 1.88 | 34 | 41.2 | 0.63 | 0.27 | -9.64 | 31 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -2.55 | -2.21 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 6.54 | 1.83 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 1.27 | 0.43 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.23 | -2.77 | 0 | — | -1.78 | -0.54 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.84 | -5.16 | 0 | — | -5.58 | -1.47 | -8.27 | 1 |
| 14 | Agent (rotation) | meta | 93.97 | -6.03 | 195 | 29.7 | -3.26 | -1.15 | -8.08 | 150 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 16 | Copy: Insider buying | copy | 92.56 | -7.44 | 47 | 42.6 | -9.15 | -1.84 | -14.95 | 62 |
| 17 | Copy: Congress Democrats (NANC) | copy | 92.31 | -7.69 | 0 | — | -6.35 | -1.69 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.40 | -9.61 | 112 | 23.2 | -15.56 | -7.03 | -17.50 | 66 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -8.05 | -2.45 | -15.48 | 74 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.36 | -13.64 | 16 | 18.8 | -6.39 | -1.06 | -19.56 | 15 |
| 24 | Agent | meta | 86.02 | -13.98 | 198 | 36.4 | -13.79 | -6.74 | -16.06 | 202 |
| 25 | Opening range 30m | breakout | 85.70 | -14.30 | 436 | 33.5 | -11.11 | -3.56 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.36 | -16.64 | 95 | 34.7 | -13.80 | -3.70 | -16.78 | 99 |
| 27 | Parabolic SAR · 1h | trend | 83.35 | -16.65 | 180 | 28.3 | -17.96 | -3.88 | -24.74 | 215 |
| 28 | Donchian 55/20 · 1h | breakout | 80.52 | -19.48 | 75 | 13.3 | -22.71 | -4.80 | -30.04 | 87 |
| 29 | Connors RSI(2) · 1h | reversion | 80.50 | -19.50 | 212 | 40.1 | -14.32 | -6.30 | -14.86 | 98 |
| 30 | Keltner breakout · 1h | breakout | 80.17 | -19.83 | 121 | 25.6 | -18.10 | -4.02 | -25.47 | 162 |
| 31 | Volume breakout · 1h | breakout | 79.72 | -20.28 | 161 | 28.6 | -16.24 | -5.14 | -21.95 | 85 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 78.03 | -21.97 | 2 | 0.0 | -13.96 | -1.71 | -24.26 | 1 |
| 33 | Opening range 15m | breakout | 77.77 | -22.23 | 530 | 31.5 | -18.17 | -4.90 | -21.37 | 702 |
| 34 | Max aggression: 5-day momentum | meta | 76.52 | -23.48 | 21 | 42.9 | -49.66 | -3.30 | -55.24 | 23 |
| 35 | Hold BTC | benchmark | 75.88 | -24.12 | 2 | 0.0 | -15.87 | -2.23 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.29 | -31.62 | 116 |
| 37 | Stochastic reversion · 1h | reversion | 75.32 | -24.68 | 322 | 45.3 | -30.86 | -4.63 | -32.18 | 405 |
| 38 | ADX DI cross · 1h | trend | 74.35 | -25.65 | 207 | 19.3 | -23.30 | -3.50 | -33.59 | 261 |
| 39 | Bollinger breakout · 1h | breakout | 74.14 | -25.86 | 184 | 22.3 | -23.98 | -4.99 | -31.79 | 234 |
| 40 | Max aggression: 1-day momentum | meta | 73.40 | -26.60 | 30 | 26.7 | -24.98 | -0.95 | -57.50 | 40 |
| 41 | MACD zero-line · 1h | trend | 72.34 | -27.66 | 173 | 18.5 | -23.19 | -4.44 | -30.90 | 191 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -24.34 | -3.45 | -28.68 | 162 |
| 43 | Supertrend · 1h | trend | 71.56 | -28.44 | 186 | 15.6 | -32.38 | -5.50 | -39.67 | 200 |
| 44 | Heikin-Ashi · 1h | trend | 71.42 | -28.59 | 459 | 23.3 | -36.59 | -6.11 | -43.26 | 639 |
| 45 | MACD cross · 1h | trend | 71.15 | -28.85 | 401 | 22.7 | -32.86 | -4.68 | -42.91 | 471 |
| 46 | RSI momentum · 1h | momentum | 70.93 | -29.07 | 174 | 13.8 | -27.85 | -4.44 | -37.87 | 206 |
| 47 | Triple EMA stack · 1h | trend | 70.90 | -29.10 | 153 | 14.4 | -26.42 | -4.27 | -37.61 | 193 |
| 48 | EMA 20/50 cross · 1h | trend | 70.74 | -29.26 | 111 | 9.9 | -33.76 | -7.87 | -40.27 | 115 |
| 49 | ROC + volume · 1h | momentum | 70.53 | -29.47 | 404 | 28.5 | -27.99 | -4.59 | -37.79 | 357 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.83 | -4.95 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.88 | -31.12 | 301 | 19.3 | -29.54 | -5.10 | -39.42 | 267 |
| 52 | CCI reversion · 1h | reversion | 68.77 | -31.23 | 372 | 41.7 | -38.76 | -6.28 | -41.88 | 460 |
| 53 | Donchian 20/10 · 1h | breakout | 67.44 | -32.56 | 157 | 18.5 | -29.13 | -4.52 | -39.23 | 206 |
| 54 | Bollinger reversion · 1h | reversion | 66.95 | -33.05 | 319 | 40.4 | -34.69 | -5.30 | -35.66 | 403 |
| 55 | Williams %R · 1h | reversion | 64.58 | -35.42 | 414 | 41.5 | -44.09 | -7.47 | -44.93 | 546 |
| 56 | EMA 9/21 cross · 1h | trend | 64.44 | -35.56 | 270 | 11.5 | -34.46 | -5.66 | -43.98 | 319 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -21.92 | -3.92 | -27.39 | 340 |
| 58 | RSI(14) reversion · 1h | reversion | 60.36 | -39.64 | 201 | 32.3 | -38.91 | -5.70 | -40.89 | 244 |
| 59 | Z-score reversion · 1h | reversion | 59.86 | -40.14 | 221 | 35.7 | -34.51 | -4.73 | -35.77 | 237 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.86 | -10.16 | -57.03 | 1215 |
| 61 | Candlestick reversal · 1h | reversion | 57.93 | -42.07 | 526 | 27.2 | -44.98 | -8.22 | -45.54 | 620 |
| 62 | Three white soldiers | momentum | 56.96 | -43.04 | 565 | 14.9 | -49.30 | -21.88 | -49.30 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -42.09 | -99.02 | 5330 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.25 | -25.89 | -81.26 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.87 | -43.60 | -93.90 | 2520 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.02 | -32.64 | -90.06 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.53 | -41.03 | -91.54 | 2336 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.90 | -30.29 | -89.93 | 2149 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -48.25 | -97.90 | 3460 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -54.78 | -96.35 | 3434 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.51 | -36.00 | -93.51 | 2274 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.86 | -33.36 | -82.87 | 1640 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.23 | -99.60 | 6020 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.04 | -42.18 | -92.06 | 2590 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.16 | -35.67 | -95.17 | 3369 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.63 | -99.81 | 6130 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.41 | -42.80 | -92.44 | 2272 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.17 | -25.92 | -76.24 | 1656 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.59 | -55.88 | -97.61 | 3473 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -55.72 | -98.99 | 4924 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.37 | -26.74 | -68.54 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -54.66 | -94.65 | 2758 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.69 | -36.72 | -84.70 | 1758 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -68.00 | -99.70 | 6358 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.30 | -29.38 | -90.37 | 2326 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.95 | -18.86 | -80.11 | 1811 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.94 | -35.57 | -91.02 | 2179 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.44 | -44.07 | -97.47 | 3900 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -58.25 | -89.12 | 2148 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.35 | -29.21 | -66.35 | 827 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.29 | -23.05 | -72.36 | 1252 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.03 | -17.19 | -80.76 | 1742 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.52 | -44.57 | -97.56 | 4326 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -96.19 | -99.94 | 8385 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T17:05 | Three white soldiers | buy | XRP-USD | 14.26 | — | entry signal |
| 2026-11-16T17:05 | Three white soldiers | buy | DOGE-USD | 14.26 | — | entry signal |
| 2026-11-16T17:00 | Williams %R · 1h | buy | PLTR | 3.93 | — | entry |
| 2026-11-16T17:00 | Williams %R · 1h | buy | META | 3.33 | — | rebalance up |
| 2026-11-16T17:00 | Williams %R · 1h | sell | DOGE-USD | 7.26 | 0.08 | exit signal |
| 2026-11-16T17:00 | ROC + volume · 1h | buy | DOGE-USD | 17.61 | — | entry signal |
| 2026-11-16T17:00 | MACD cross · 1h | buy | XRP-USD | 10.13 | — | entry signal |
| 2026-11-16T17:00 | MACD cross · 1h | buy | SOL-USD | 10.17 | — | entry signal |
| 2026-11-16T17:00 | MACD cross · 1h | sell | SQQQ | 3.96 | 0.11 | rebalance down |
| 2026-11-16T17:00 | MACD cross · 1h | sell | NVDA | 4.01 | -0.02 | rebalance down |
| 2026-11-16T17:00 | MACD cross · 1h | sell | ETH-USD | 4.04 | -0.04 | rebalance down |
| 2026-11-16T17:00 | MACD cross · 1h | sell | DOGE-USD | 4.20 | 0.01 | rebalance down |
| 2026-11-16T17:00 | MACD cross · 1h | sell | BTC-USD | 4.08 | -0.02 | rebalance down |
| 2026-11-16T17:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 16.10 | — | entry signal |
| 2026-11-16T16:50 | Three white soldiers | sell | MSFT | 14.35 | 0.06 | exit signal |
| 2026-11-16T16:40 | Candlestick reversal · 1h | buy | MSTR | 5.80 | — | entry |
| 2026-11-16T16:40 | Candlestick reversal · 1h | buy | BITX | 3.75 | — | rebalance up |
| 2026-11-16T16:40 | Candlestick reversal · 1h | sell | NVDA | 4.75 | -0.01 | rebalance down |
| 2026-11-16T16:40 | Candlestick reversal · 1h | sell | BTC-USD | 4.80 | -0.02 | rebalance down |
| 2026-11-16T16:30 | Williams %R · 1h | buy | META | 1.29 | — | entry signal |
| 2026-11-16T16:30 | Williams %R · 1h | buy | AMZN | 4.31 | — | entry signal |
| 2026-11-16T16:30 | Williams %R · 1h | buy | AAPL | 4.31 | — | entry signal |
| 2026-11-16T16:30 | Stochastic reversion · 1h | buy | TSLA | 6.87 | — | entry signal |
| 2026-11-16T16:30 | Stochastic reversion · 1h | buy | TQQQ | 6.89 | — | entry signal |
| 2026-11-16T16:30 | Stochastic reversion · 1h | buy | TECL | 6.89 | — | entry signal |
| 2026-11-16T16:30 | Stochastic reversion · 1h | buy | QQQ | 6.89 | — | entry signal |
| 2026-11-16T16:30 | Stochastic reversion · 1h | buy | GOOGL | 6.89 | — | entry signal |
| 2026-11-16T16:30 | Stochastic reversion · 1h | buy | AAPL | 6.89 | — | entry signal |
| 2026-11-16T16:30 | Stochastic reversion · 1h | sell | TNA | 8.25 | 0.02 | rebalance down |
| 2026-11-16T16:30 | Stochastic reversion · 1h | sell | MSFT | 5.83 | 0.06 | rebalance down |
| 2026-11-16T16:30 | Stochastic reversion · 1h | sell | LABU | 5.71 | -0.03 | rebalance down |
| 2026-11-16T16:30 | Stochastic reversion · 1h | sell | IWM | 5.71 | 0.01 | rebalance down |
| 2026-11-16T16:30 | Stochastic reversion · 1h | sell | AMD | 8.35 | -0.01 | rebalance down |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | UPRO | 4.79 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | TQQQ | 4.81 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | TECL | 4.81 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | SPY | 4.81 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | SOXL | 4.81 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | QQQ | 4.81 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | PLTR | 4.81 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 17:09:05.000173+00:00 -> 2026-11-16 17:19:05.000173+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 17:09:05.000173+00:00 -> 2026-11-16 17:19:05.000173+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
