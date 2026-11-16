# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T19:40:05.000184+00:00 · 62278 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.79 (-14.21%)

Closed trades 199, win rate 36.2%, fees £5.72, max drawdown -15.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.13 | -0.02 |
| SOXL | 16.98 | -0.23 |

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

Today: 35022 decisions in 3132 calls, $0.4365 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T19:40 | 2 / 5 / 23 | cash |  |
| Breezy | 2026-11-16T19:40 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-16T19:40 | 2 / 18 / 10 | COIN 62% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.62 | 17.62 | 0 | — | 13.70 | 4.56 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.92 | 10.92 | 23 | 65.2 | 15.02 | 3.06 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.49 | 3.49 | 0 | — | 5.22 | 1.44 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.53 | 1.52 | 35 | 40.0 | 0.06 | 0.14 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -2.55 | -2.21 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.26 | 2.02 | -9.06 | 225 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 1.60 | 0.46 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.54 | -3.46 | 0 | — | -2.73 | -0.84 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.07 | -5.93 | 0 | — | -6.44 | -1.68 | -8.27 | 1 |
| 14 | Agent (rotation) | meta | 93.89 | -6.11 | 195 | 29.7 | -2.86 | -0.99 | -8.06 | 150 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.83 | -8.17 | 0 | — | -6.89 | -1.85 | -10.92 | 1 |
| 18 | Copy: Insider buying | copy | 91.74 | -8.26 | 47 | 42.6 | -10.11 | -2.02 | -14.95 | 62 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.66 | -7.04 | -17.60 | 66 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -7.37 | -2.07 | -15.48 | 74 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.58 | -13.42 | 16 | 18.8 | -5.38 | -0.86 | -19.56 | 15 |
| 24 | Opening range 30m | breakout | 86.12 | -13.88 | 436 | 33.5 | -10.89 | -3.46 | -14.11 | 584 |
| 25 | Agent | meta | 85.79 | -14.21 | 199 | 36.2 | -13.89 | -6.84 | -15.94 | 199 |
| 26 | Agent (aggressive) | meta | 83.44 | -16.56 | 95 | 34.7 | -13.72 | -3.67 | -16.78 | 99 |
| 27 | Parabolic SAR · 1h | trend | 83.19 | -16.81 | 180 | 28.3 | -18.05 | -3.93 | -24.74 | 215 |
| 28 | Keltner breakout · 1h | breakout | 80.57 | -19.43 | 121 | 25.6 | -16.45 | -3.35 | -25.47 | 161 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -21.87 | -4.74 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.23 | -19.77 | 213 | 39.9 | -14.29 | -6.27 | -14.83 | 98 |
| 31 | Volume breakout · 1h | breakout | 79.57 | -20.43 | 161 | 28.6 | -16.40 | -5.18 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 78.16 | -21.84 | 530 | 31.5 | -17.47 | -4.70 | -21.37 | 693 |
| 33 | Max aggression: 5-day momentum | meta | 78.06 | -21.94 | 21 | 42.9 | -48.65 | -3.25 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.76 | -22.24 | 2 | 0.0 | -14.39 | -1.76 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 75.78 | -24.22 | 2 | 0.0 | -14.85 | -2.07 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.03 | -8.26 | -31.55 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 74.88 | -25.12 | 30 | 26.7 | -23.48 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.73 | -25.27 | 207 | 19.3 | -23.06 | -3.50 | -33.78 | 256 |
| 39 | Bollinger breakout · 1h | breakout | 74.37 | -25.63 | 184 | 22.3 | -23.67 | -4.93 | -31.71 | 234 |
| 40 | Stochastic reversion · 1h ⏸ | reversion | 74.07 | -25.93 | 333 | 44.1 | -31.85 | -4.68 | -32.96 | 416 |
| 41 | MACD zero-line · 1h | trend | 72.48 | -27.52 | 173 | 18.5 | -24.63 | -4.83 | -31.30 | 191 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -25.91 | -3.67 | -29.17 | 163 |
| 43 | Heikin-Ashi · 1h | trend | 71.78 | -28.22 | 459 | 23.3 | -39.08 | -7.45 | -43.26 | 637 |
| 44 | Supertrend · 1h | trend | 71.39 | -28.61 | 187 | 16.0 | -32.61 | -5.56 | -39.35 | 201 |
| 45 | RSI momentum · 1h | momentum | 71.25 | -28.75 | 175 | 14.3 | -28.08 | -4.58 | -38.03 | 205 |
| 46 | Triple EMA stack · 1h | trend | 71.21 | -28.79 | 154 | 14.9 | -26.61 | -4.46 | -37.61 | 192 |
| 47 | EMA 20/50 cross · 1h | trend | 70.92 | -29.08 | 111 | 9.9 | -35.34 | -9.54 | -38.74 | 113 |
| 48 | MACD cross · 1h | trend | 70.79 | -29.21 | 402 | 22.6 | -33.28 | -4.76 | -42.93 | 470 |
| 49 | ROC + volume · 1h | momentum | 70.75 | -29.25 | 404 | 28.5 | -27.66 | -4.53 | -37.60 | 357 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.40 | -4.87 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.14 | -30.86 | 303 | 19.1 | -29.15 | -5.07 | -39.14 | 256 |
| 52 | CCI reversion · 1h | reversion | 67.75 | -32.25 | 375 | 41.6 | -40.34 | -6.52 | -42.06 | 459 |
| 53 | Donchian 20/10 · 1h | breakout | 67.64 | -32.36 | 157 | 18.5 | -29.18 | -4.57 | -39.23 | 206 |
| 54 | Bollinger reversion · 1h ⏸ | reversion | 66.56 | -33.45 | 333 | 39.0 | -35.73 | -5.36 | -36.72 | 407 |
| 55 | EMA 9/21 cross · 1h | trend | 64.37 | -35.63 | 271 | 11.4 | -34.68 | -5.69 | -44.20 | 320 |
| 56 | Williams %R · 1h | reversion | 63.97 | -36.03 | 418 | 41.1 | -44.99 | -7.58 | -45.24 | 546 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -23.48 | -3.52 | -29.33 | 353 |
| 58 | Z-score reversion · 1h | reversion | 59.78 | -40.22 | 221 | 35.7 | -34.60 | -4.74 | -35.86 | 238 |
| 59 | RSI(14) reversion · 1h | reversion | 59.62 | -40.38 | 202 | 32.2 | -40.17 | -5.88 | -41.65 | 248 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.60 | -9.46 | -57.37 | 1214 |
| 61 | Candlestick reversal · 1h | reversion | 57.46 | -42.54 | 527 | 27.1 | -45.13 | -8.18 | -45.51 | 620 |
| 62 | Three white soldiers | momentum | 56.70 | -43.30 | 569 | 14.8 | -49.49 | -21.93 | -49.49 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -41.63 | -99.04 | 5308 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.39 | -25.78 | -81.40 | 1426 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.04 | -42.95 | -94.04 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.04 | -31.81 | -90.04 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.48 | -39.91 | -91.49 | 2323 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.91 | -30.15 | -89.92 | 2145 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.94 | -47.22 | -97.94 | 3465 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -53.60 | -96.44 | 3433 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.36 | -36.09 | -93.39 | 2251 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.75 | -32.91 | -82.75 | 1635 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -52.47 | -99.59 | 6032 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.10 | -42.14 | -92.10 | 2586 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.18 | -35.76 | -95.18 | 3348 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -66.47 | -99.81 | 6138 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.50 | -42.48 | -92.50 | 2271 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.37 | -25.92 | -76.37 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -56.52 | -97.62 | 3469 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.99 | -54.43 | -98.99 | 4937 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.32 | -26.68 | -68.53 | 1222 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -54.74 | -94.71 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.87 | -37.23 | -84.87 | 1759 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -65.13 | -99.69 | 6371 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.42 | -29.66 | -90.45 | 2332 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.82 | -18.72 | -79.85 | 1815 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.87 | -34.96 | -90.90 | 2183 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.43 | -43.84 | -97.43 | 3899 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.15 | -57.71 | -89.18 | 2155 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -29.24 | -66.40 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.00 | -23.08 | -72.20 | 1246 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.39 | -17.56 | -80.66 | 1755 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.61 | -97.56 | 4354 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -94.54 | -99.94 | 8384 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T19:31 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 100.98 | — | entry |
| 2026-11-16T19:31 | CCI reversion · 1h | buy | AMD | 16.99 | — | entry signal |
| 2026-11-16T19:31 | Z-score reversion · 1h | buy | ETHU | 14.96 | — | entry signal |
| 2026-11-16T19:31 | Connors RSI(2) · 1h | buy | AAPL | 20.07 | — | entry signal |
| 2026-11-16T19:31 | RSI(14) reversion · 1h | buy | NVDA | 14.90 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | TNA | 5.75 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | SOXL | 5.77 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | LABU | 5.77 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | IWM | 5.77 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | NVDA | 3.70 | -0.08 | rebalance down |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | MSFT | 5.71 | -0.01 | rebalance down |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | BTC-USD | 3.93 | 0.00 | rebalance down |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | BITX | 3.98 | 0.03 | rebalance down |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | AMD | 5.74 | -0.00 | rebalance down |
| 2026-11-16T19:31 | Trend pullback · 1h | sell | AAPL | 23.67 | 0.46 | exit signal |
| 2026-11-16T19:31 | EMA 9/21 cross · 1h | sell | AAPL | 16.03 | -0.02 | exit signal |
| 2026-11-16T19:25 | Three white soldiers | sell | AMZN | 14.14 | -0.04 | exit signal |
| 2026-11-16T19:21 | Three white soldiers | buy | AMZN | 14.19 | — | entry signal |
| 2026-11-16T19:15 | Candlestick reversal · 1h | buy | MSTR | 5.74 | — | entry |
| 2026-11-16T19:15 | OBV trend · 1h | sell | META | 17.20 | -0.05 | target is flat |
| 2026-11-16T19:05 | Three white soldiers | sell | AMZN | 14.15 | -0.05 | exit signal |
| 2026-11-16T19:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 100.98 | -0.90 | target is flat |
| 2026-11-16T19:00 | MACD zero-line · 1h | buy | ETH-USD | 18.13 | — | entry signal |
| 2026-11-16T19:00 | MACD zero-line · 1h | buy | DOGE-USD | 18.13 | — | entry signal |
| 2026-11-16T18:55 | Agent | sell | TSLA | 17.18 | -0.03 | selected signal exited |
| 2026-11-16T18:50 | Three white soldiers | buy | AMZN | 14.20 | — | entry signal |
| 2026-11-16T18:35 | Agent (rotation) | buy | SQQQ | 31.32 | — | entry |
| 2026-11-16T18:35 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 111.21 | — | entry |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | TSLA | 6.79 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | TQQQ | 6.63 | -0.26 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | TNA | 6.67 | -0.20 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | TECL | 6.59 | -0.31 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | QQQ | 6.80 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | MSFT | 6.81 | 0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | LABU | 6.57 | -0.35 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | IWM | 6.82 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | GOOGL | 6.79 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | AMD | 6.76 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Stochastic reversion · 1h | sell | AAPL | 6.83 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T18:35 | Connors RSI(2) · 1h | sell | AAPL | 19.92 | -0.24 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 19:40:05.000184+00:00 -> 2026-11-16 19:50:05.000184+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 19:40:05.000184+00:00 -> 2026-11-16 19:50:05.000184+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
