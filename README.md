# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T16:39:05.000128+00:00 · 62131 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.99 (-14.01%)

Closed trades 198, win rate 36.4%, fees £5.69, max drawdown -15.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.06 | -0.09 |

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

Today: 21759 decisions in 2691 calls, $0.2811 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T16:39 | 1 / 16 / 13 | cash |  |
| Breezy | 2026-11-16T16:39 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-16T16:39 | 4 / 25 / 1 | COIN 64% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.31 | 18.31 | 0 | — | 15.39 | 5.09 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 15.38 | 3.13 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.27 | 4.27 | 0 | — | 6.02 | 1.65 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.88 | 1.88 | 34 | 41.2 | 0.89 | 0.33 | -9.64 | 31 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -2.55 | -2.21 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 6.54 | 1.83 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 1.16 | 0.42 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.51 | -2.49 | 0 | — | -1.42 | -0.42 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.84 | -5.16 | 0 | — | -5.58 | -1.47 | -8.27 | 1 |
| 14 | Agent (rotation) | meta | 93.97 | -6.03 | 195 | 29.7 | -2.05 | -0.68 | -7.38 | 152 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 16 | Copy: Insider buying | copy | 92.42 | -7.58 | 47 | 42.6 | -9.31 | -1.88 | -14.95 | 62 |
| 17 | Copy: Congress Democrats (NANC) | copy | 92.33 | -7.67 | 0 | — | -6.19 | -1.65 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.46 | -9.54 | 112 | 23.2 | -15.50 | -7.02 | -17.47 | 66 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -7.37 | -2.07 | -15.48 | 74 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.36 | -13.64 | 16 | 18.8 | -6.51 | -1.08 | -19.56 | 15 |
| 24 | Agent | meta | 85.99 | -14.01 | 198 | 36.4 | -13.61 | -6.67 | -15.68 | 195 |
| 25 | Opening range 30m | breakout | 85.48 | -14.52 | 436 | 33.5 | -11.33 | -3.63 | -14.11 | 583 |
| 26 | Parabolic SAR · 1h | trend | 83.31 | -16.69 | 180 | 28.3 | -17.82 | -3.89 | -24.64 | 215 |
| 27 | Agent (aggressive) | meta | 83.28 | -16.72 | 95 | 34.7 | -14.64 | -4.01 | -16.59 | 95 |
| 28 | Connors RSI(2) · 1h | reversion | 80.72 | -19.28 | 212 | 40.1 | -14.08 | -6.17 | -14.84 | 98 |
| 29 | Donchian 55/20 · 1h | breakout | 80.58 | -19.42 | 75 | 13.3 | -22.65 | -4.79 | -30.02 | 87 |
| 30 | Keltner breakout · 1h | breakout | 79.97 | -20.02 | 121 | 25.6 | -17.82 | -3.83 | -25.47 | 161 |
| 31 | Volume breakout · 1h | breakout | 79.69 | -20.31 | 161 | 28.6 | -16.28 | -5.15 | -21.95 | 85 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 78.37 | -21.63 | 2 | 0.0 | -13.54 | -1.65 | -24.26 | 1 |
| 33 | Opening range 15m | breakout | 77.58 | -22.42 | 530 | 31.5 | -18.35 | -4.95 | -21.37 | 702 |
| 34 | Stochastic reversion · 1h | reversion | 75.78 | -24.23 | 322 | 45.3 | -30.16 | -4.55 | -31.90 | 405 |
| 35 | Max aggression: 5-day momentum | meta | 75.76 | -24.24 | 21 | 42.9 | -50.15 | -3.33 | -55.24 | 23 |
| 36 | Hold BTC | benchmark | 75.59 | -24.41 | 2 | 0.0 | -16.29 | -2.30 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.29 | -31.62 | 116 |
| 38 | ADX DI cross · 1h | trend | 74.17 | -25.83 | 207 | 19.3 | -23.66 | -3.56 | -33.59 | 263 |
| 39 | Bollinger breakout · 1h | breakout | 73.93 | -26.07 | 184 | 22.3 | -24.20 | -5.04 | -31.79 | 234 |
| 40 | Max aggression: 1-day momentum | meta | 72.67 | -27.32 | 30 | 26.7 | -25.72 | -1.00 | -57.50 | 40 |
| 41 | MACD zero-line · 1h | trend | 72.17 | -27.83 | 173 | 18.5 | -23.37 | -4.47 | -30.90 | 191 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -24.00 | -3.41 | -28.68 | 161 |
| 43 | Heikin-Ashi · 1h | trend | 71.24 | -28.76 | 459 | 23.3 | -36.75 | -6.13 | -43.26 | 639 |
| 44 | Supertrend · 1h | trend | 71.18 | -28.82 | 186 | 15.6 | -32.73 | -5.57 | -39.67 | 200 |
| 45 | MACD cross · 1h | trend | 70.99 | -29.01 | 401 | 22.7 | -33.01 | -4.70 | -42.91 | 469 |
| 46 | EMA 20/50 cross · 1h | trend | 70.82 | -29.18 | 111 | 9.9 | -33.59 | -7.81 | -40.27 | 115 |
| 47 | RSI momentum · 1h | momentum | 70.81 | -29.19 | 174 | 13.8 | -28.38 | -4.54 | -38.05 | 205 |
| 48 | Triple EMA stack · 1h | trend | 70.76 | -29.24 | 153 | 14.4 | -26.56 | -4.30 | -37.66 | 193 |
| 49 | ROC + volume · 1h | momentum | 70.36 | -29.64 | 404 | 28.5 | -28.35 | -4.66 | -37.87 | 356 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.89 | -4.96 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.78 | -31.22 | 301 | 19.3 | -29.92 | -5.18 | -39.42 | 267 |
| 52 | CCI reversion · 1h | reversion | 68.67 | -31.33 | 372 | 41.7 | -38.83 | -6.29 | -41.88 | 460 |
| 53 | Bollinger reversion · 1h | reversion | 67.34 | -32.66 | 319 | 40.4 | -34.31 | -5.26 | -35.59 | 403 |
| 54 | Donchian 20/10 · 1h | breakout | 67.24 | -32.76 | 157 | 18.5 | -29.34 | -4.55 | -39.23 | 206 |
| 55 | Williams %R · 1h | reversion | 64.62 | -35.38 | 413 | 41.4 | -44.27 | -7.55 | -44.93 | 546 |
| 56 | EMA 9/21 cross · 1h | trend | 64.33 | -35.66 | 270 | 11.5 | -34.56 | -5.67 | -43.98 | 318 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -20.34 | -3.86 | -25.78 | 344 |
| 58 | RSI(14) reversion · 1h | reversion | 60.60 | -39.40 | 201 | 32.3 | -40.01 | -5.96 | -40.89 | 239 |
| 59 | Z-score reversion · 1h | reversion | 59.86 | -40.14 | 221 | 35.7 | -34.51 | -4.73 | -35.77 | 237 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.79 | -10.17 | -56.97 | 1211 |
| 61 | Candlestick reversal · 1h | reversion | 58.09 | -41.91 | 526 | 27.2 | -44.11 | -7.99 | -45.22 | 607 |
| 62 | Three white soldiers | momentum | 57.10 | -42.90 | 564 | 14.7 | -49.23 | -21.88 | -49.32 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -42.25 | -99.02 | 5336 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.27 | -25.88 | -81.27 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.88 | -43.63 | -93.88 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.98 | -32.73 | -90.06 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.55 | -40.94 | -91.55 | 2334 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.96 | -30.38 | -89.96 | 2152 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -48.13 | -97.89 | 3461 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -54.75 | -96.34 | 3435 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.42 | -35.15 | -93.42 | 2265 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.72 | -32.84 | -82.72 | 1635 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.94 | -99.61 | 6022 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.05 | -42.26 | -92.06 | 2588 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.20 | -35.61 | -95.21 | 3377 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.88 | -99.81 | 6135 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.43 | -42.78 | -92.43 | 2272 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.42 | -26.25 | -76.42 | 1662 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -56.13 | -97.61 | 3473 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.99 | -56.14 | -99.00 | 4926 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.35 | -26.74 | -68.53 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -54.53 | -94.62 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -36.68 | -84.68 | 1756 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -68.02 | -99.70 | 6361 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.32 | -29.40 | -90.44 | 2331 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.78 | -18.74 | -80.05 | 1815 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.94 | -35.58 | -91.02 | 2177 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.45 | -44.27 | -97.47 | 3901 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -59.32 | -89.13 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.33 | -29.19 | -66.33 | 826 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.38 | -23.04 | -72.38 | 1253 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.00 | -17.17 | -80.76 | 1740 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.53 | -45.06 | -97.57 | 4325 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.55 | -99.94 | 8393 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | MSTR | 4.81 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | GOOGL | 4.81 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | BITX | 4.81 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | buy | AMZN | 4.81 | — | entry signal |
| 2026-11-16T16:30 | Bollinger reversion · 1h | sell | TNA | 12.00 | -0.13 | rebalance down |
| 2026-11-16T16:30 | Bollinger reversion · 1h | sell | LABU | 12.04 | -0.07 | rebalance down |
| 2026-11-16T16:30 | Bollinger reversion · 1h | sell | IWM | 12.09 | -0.03 | rebalance down |
| 2026-11-16T16:30 | Candlestick reversal · 1h | buy | BITX | 5.93 | — | entry signal |
| 2026-11-16T16:30 | Candlestick reversal · 1h | sell | MSFT | 2.92 | 0.03 | rebalance down |
| 2026-11-16T16:30 | Candlestick reversal · 1h | sell | AMD | 3.02 | 0.03 | rebalance down |
| 2026-11-16T16:30 | OBV trend · 1h | buy | SQQQ | 17.20 | — | entry signal |
| 2026-11-16T16:30 | Heikin-Ashi · 1h | buy | SQQQ | 17.81 | — | entry signal |
| 2026-11-16T16:30 | Triple EMA stack · 1h | buy | SQQQ | 17.70 | — | entry signal |
| 2026-11-16T16:30 | EMA 20/50 cross · 1h | buy | SQQQ | 17.71 | — | entry signal |
| 2026-11-16T16:30 | EMA 9/21 cross · 1h | sell | TSLA | 16.26 | -0.02 | exit signal |
| 2026-11-16T16:25 | Agent | sell | SOXL | 17.71 | 0.67 | selected signal exited |
| 2026-11-16T16:15 | Three white soldiers | sell | META | 14.24 | -0.05 | exit signal |
| 2026-11-16T16:10 | Three white soldiers | sell | XRP-USD | 14.17 | -0.12 | exit signal |
| 2026-11-16T16:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 101.88 | -2.00 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 16:39:05.000128+00:00 -> 2026-11-16 16:49:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 16:39:05.000128+00:00 -> 2026-11-16 16:49:05.000128+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
