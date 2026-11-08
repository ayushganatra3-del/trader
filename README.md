# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-08T11:50:05.000132+00:00 · 52068 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.54 (-12.46%)

Closed trades 156, win rate 35.9%, fees £4.84, max drawdown -12.87%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 9117 decisions in 1827 calls, $0.1274 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-08T11:50 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-08T11:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-08T11:50 | 1 / 3 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 1.95 | +8.75% | 6 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| VWAP reversion | SQQQ | 1.93 | +6.85% | 4 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.06 | 0.13 | -9.63 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.65 | -1.35 | 126 | 46.0 | -12.38 | -2.91 | -13.75 | 147 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.46 | 2.83 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -6.88 | -3.99 | -10.35 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.54 | -0.42 | -9.14 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.97 | -18.73 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -14.27 | -5.43 | -17.86 | 78 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.49 | -5.33 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -12.86 | -3.08 | -15.96 | 62 |
| 23 | Daily: Bullish score | daily | 88.76 | -11.23 | 15 | 20.0 | -5.00 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.72 | -3.38 | -14.68 | 83 |
| 25 | Hold BTC | benchmark | 88.65 | -11.35 | 1 | 0.0 | -4.97 | -0.48 | -14.09 | 1 |
| 26 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -14.32 | -7.67 | -14.33 | 197 |
| 27 | Parabolic SAR · 1h | trend | 86.91 | -13.09 | 166 | 27.1 | -13.11 | -2.89 | -20.50 | 235 |
| 28 | Donchian 55/20 · 1h | breakout | 85.95 | -14.05 | 71 | 14.1 | -12.74 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 85.19 | -14.81 | 17 | 47.1 | -32.59 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.23 | -5.45 | -18.65 | 93 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.01 | -17.99 | 263 | 46.8 | -25.32 | -3.74 | -29.25 | 392 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.05 | -4.57 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.37 | -20.63 | 175 | 18.3 | -23.79 | -3.96 | -27.04 | 260 |
| 38 | MFI reversion · 1h | reversion | 78.35 | -21.65 | 337 | 34.1 | -18.81 | -2.69 | -20.14 | 156 |
| 39 | Ichimoku · 1h | trend | 77.88 | -22.12 | 94 | 14.9 | -22.74 | -4.65 | -29.43 | 124 |
| 40 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.46 | -4.88 | -27.58 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.42 | -23.58 | 294 | 45.2 | -29.81 | -4.90 | -30.24 | 465 |
| 42 | EMA 20/50 cross · 1h | trend | 76.08 | -23.92 | 102 | 10.8 | -21.86 | -3.93 | -30.58 | 127 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -42.90 | -9.05 | -42.90 | 676 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.47 | -5.26 | -29.20 | 208 |
| 45 | Triple EMA stack · 1h | trend | 74.46 | -25.54 | 142 | 14.8 | -28.08 | -5.90 | -33.48 | 202 |
| 46 | Supertrend · 1h | trend | 73.63 | -26.37 | 166 | 13.3 | -29.81 | -5.18 | -34.80 | 215 |
| 47 | RSI momentum · 1h | momentum | 73.47 | -26.53 | 158 | 12.7 | -27.74 | -5.29 | -32.60 | 217 |
| 48 | Z-score reversion · 1h | reversion | 72.93 | -27.07 | 164 | 35.4 | -25.17 | -3.75 | -27.66 | 227 |
| 49 | MACD cross · 1h | trend | 72.83 | -27.17 | 342 | 23.1 | -34.40 | -6.06 | -38.98 | 478 |
| 50 | Bollinger reversion · 1h | reversion | 72.73 | -27.27 | 256 | 39.5 | -30.87 | -5.28 | -33.80 | 371 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -36.75 | -5.95 | -38.55 | 534 |
| 52 | Daily: Momentum burst | daily | 72.31 | -27.69 | 26 | 11.5 | -35.92 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.47 | -28.53 | 141 | 19.9 | -29.91 | -5.54 | -34.69 | 212 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -29.94 | -6.17 | -34.11 | 285 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -38.35 | -7.44 | -39.25 | 382 |
| 56 | EMA 9/21 cross · 1h | trend | 67.11 | -32.89 | 243 | 9.9 | -38.77 | -7.97 | -39.15 | 333 |
| 57 | VWAP momentum · 1h | momentum | 66.56 | -33.44 | 790 | 21.8 | -54.95 | -12.12 | -54.97 | 1239 |
| 58 | Agent (ML meta-label) | meta | 66.32 | -33.68 | 1541 | 23.0 | -9.95 | -1.68 | -18.70 | 338 |
| 59 | RSI(14) reversion · 1h | reversion | 66.17 | -33.83 | 143 | 27.3 | -28.97 | -4.55 | -31.54 | 219 |
| 60 | Candlestick reversal · 1h | reversion | 65.05 | -34.95 | 418 | 28.2 | -38.26 | -7.07 | -38.30 | 579 |
| 61 | Three white soldiers | momentum | 63.69 | -36.31 | 478 | 15.3 | -49.20 | -22.83 | -49.20 | 650 |
| 62 | Max aggression: 1-day momentum | meta | 62.24 | -37.76 | 26 | 26.9 | -42.96 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -46.09 | -98.98 | 5246 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.74 | -26.19 | -80.74 | 1437 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -47.04 | -93.45 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.95 | -32.27 | -88.95 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.74 | -39.97 | -90.74 | 2306 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.13 | -32.19 | -90.18 | 2194 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -54.94 | -97.72 | 3481 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -56.85 | -96.31 | 3401 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.64 | -33.35 | -93.65 | 2435 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.20 | -34.38 | -82.20 | 1650 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -54.39 | -99.53 | 6001 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.58 | -43.75 | -92.58 | 2600 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.73 | -38.43 | -95.73 | 3419 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -74.23 | -99.80 | 6190 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.73 | -43.73 | -91.73 | 2277 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.19 | -24.63 | -75.19 | 1567 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -63.05 | -97.77 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -63.09 | -98.83 | 4895 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.64 | -28.96 | -69.64 | 1198 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -54.30 | -94.63 | 2744 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.63 | -37.03 | -84.63 | 1757 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -73.82 | -99.64 | 6381 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.48 | -31.94 | -89.51 | 2304 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.06 | -19.73 | -78.06 | 1753 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.09 | -37.52 | -91.10 | 2226 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.75 | -52.06 | -96.75 | 3904 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.43 | -55.43 | -89.43 | 2163 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.49 | -28.51 | -65.49 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.74 | -24.07 | -72.74 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.71 | -18.49 | -78.73 | 1673 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.30 | -49.96 | -97.30 | 4339 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -113.03 | -99.93 | 8304 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-08T11:20 | Three white soldiers | buy | BTC-USD | 15.93 | — | entry signal |
| 2026-11-08T11:05 | VWAP reversion · 1h | sell | DOGE-USD | 24.54 | -0.16 | target is flat |
| 2026-11-08T11:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.70 | — | entry signal |
| 2026-11-08T11:00 | VWAP momentum · 1h | buy | SOL-USD | 1.55 | — | entry |
| 2026-11-08T11:00 | VWAP momentum · 1h | buy | ETH-USD | 6.05 | — | entry |
| 2026-11-08T11:00 | VWAP momentum · 1h | sell | XRP-USD | 6.60 | -0.06 | exit signal |
| 2026-11-08T10:00 | MACD cross · 1h | sell | DOGE-USD | 4.80 | -0.06 | exit signal |
| 2026-11-08T10:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 16.79 | — | entry signal |
| 2026-11-08T09:20 | CCI reversion · 1h | sell | DOGE-USD | 3.41 | -0.06 | stop-loss |
| 2026-11-08T09:20 | Candlestick reversal · 1h | buy | ETH-USD | 3.99 | — | entry |
| 2026-11-08T09:20 | Candlestick reversal · 1h | sell | DOGE-USD | 3.99 | -0.05 | stop-loss |
| 2026-11-08T09:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.03 | — | entry |
| 2026-11-08T09:00 | Candlestick reversal · 1h | sell | XRP-USD | 4.03 | 0.00 | exit signal |
| 2026-11-08T08:45 | Agent (ML meta-label) | sell | XRP-USD | 3.67 | -0.02 | selected signal exited |
| 2026-11-08T08:30 | Agent (ML meta-label) | buy | XRP-USD | 3.69 | — | entry |
| 2026-11-08T08:00 | CCI reversion · 1h | buy | SOL-USD | 1.71 | — | entry |
| 2026-11-08T08:00 | CCI reversion · 1h | sell | BTC-USD | 1.31 | -0.00 | exit signal |
| 2026-11-08T08:00 | Bollinger reversion · 1h | sell | ETH-USD | 4.84 | -0.01 | exit signal |
| 2026-11-08T08:00 | MACD cross · 1h | buy | SOL-USD | 4.86 | — | entry signal |
| 2026-11-08T08:00 | MACD cross · 1h | buy | DOGE-USD | 4.86 | — | entry signal |
| 2026-11-08T06:00 | Stochastic reversion · 1h | sell | XRP-USD | 2.28 | 0.00 | exit signal |
| 2026-11-08T06:00 | Bollinger reversion · 1h | sell | XRP-USD | 5.59 | -0.02 | exit signal |
| 2026-11-08T06:00 | VWAP momentum · 1h | buy | XRP-USD | 6.66 | — | entry signal |
| 2026-11-08T05:35 | Three white soldiers | sell | SOL-USD | 15.85 | -0.11 | exit signal |
| 2026-11-08T05:15 | Three white soldiers | buy | SOL-USD | 15.96 | — | entry signal |
| 2026-11-08T05:00 | VWAP momentum · 1h | sell | ETH-USD | 6.62 | -0.04 | exit signal |
| 2026-11-08T04:00 | VWAP reversion · 1h | sell | SOL-USD | 24.65 | -0.13 | exit signal |
| 2026-11-08T04:00 | VWAP reversion · 1h | sell | DOGE-USD | 24.60 | -0.18 | exit signal |
| 2026-11-08T04:00 | Z-score reversion · 1h | sell | BTC-USD | 5.22 | -0.01 | exit signal |
| 2026-11-08T04:00 | Bollinger reversion · 1h | buy | SOL-USD | 5.01 | — | entry |
| 2026-11-08T04:00 | Bollinger reversion · 1h | sell | BTC-USD | 4.36 | -0.01 | exit signal |
| 2026-11-08T03:55 | Three white soldiers | sell | SOL-USD | 15.87 | -0.12 | exit signal |
| 2026-11-08T03:50 | Three white soldiers | buy | SOL-USD | 15.99 | — | entry signal |
| 2026-11-08T03:00 | VWAP momentum · 1h | buy | ETH-USD | 6.67 | — | entry signal |
| 2026-11-08T03:00 | VWAP momentum · 1h | buy | BTC-USD | 6.67 | — | entry signal |
| 2026-11-08T02:50 | Stochastic reversion · 1h | buy | XRP-USD | 2.28 | — | entry |
| 2026-11-08T02:50 | Stochastic reversion · 1h | sell | DOGE-USD | 2.28 | -0.05 | target is flat |
| 2026-11-08T02:50 | Bollinger reversion · 1h | buy | ETH-USD | 4.85 | — | entry |
| 2026-11-08T02:50 | Bollinger reversion · 1h | sell | DOGE-USD | 5.49 | -0.12 | target is flat |
| 2026-11-08T02:50 | Candlestick reversal · 1h | buy | XRP-USD | 4.03 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-10 11:50:05.000132+00:00 -> 2026-11-08 12:00:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-10 11:50:05.000132+00:00 -> 2026-11-08 12:00:05.000132+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-10 11:50:05.000132+00:00 -> 2026-11-08 12:00:05.000132+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
