# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-14T21:40:05.000128+00:00 · 59870 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.50 (-14.50%)

Closed trades 195, win rate 35.9%, fees £5.63, max drawdown -15.42%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-14 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 16629 decisions in 3327 calls, $0.2328 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-14T21:40 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-14T21:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-14T21:40 | 3 / 2 / 0 | ETH-USD 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 3.17 | +3.60% | 9 |
| RSI momentum | TNA | 2.20 | +2.77% | 6 |
| Z-score reversion | TQQQ | 2.19 | +4.95% | 6 |
| Williams %R | TSLA | 2.15 | +8.36% | 18 |
| Gap and go | TQQQ | 1.80 | +5.84% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.89 | 17.89 | 0 | — | 15.31 | 5.11 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 3.29 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.99 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.63 | 4.63 | 0 | — | 6.58 | 1.81 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 1.00 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 2.98 | 1.86 | -4.12 | 86 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.72 | 1.89 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.33 | -1.67 | 0 | — | -0.61 | -0.13 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.89 | -3.12 | 1 | 0.0 | -3.27 | -2.15 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.69 | -3.31 | 191 | 30.4 | -3.13 | -1.09 | -8.46 | 150 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.35 | -3.65 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.25 | -5.75 | 43 | 39.5 | -6.38 | -1.27 | -14.79 | 60 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.13 | -3.91 | -5.99 | 24 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.28 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.07 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.84 | -8.15 | 110 | 22.7 | -15.16 | -5.61 | -17.77 | 70 |
| 20 | VWAP reversion · 1h | reversion | 91.38 | -8.62 | 148 | 45.9 | -16.84 | -4.15 | -16.84 | 155 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.30 | -0.70 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.28 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.26 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.69 | -14.31 | 16 | 18.8 | -10.26 | -1.63 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.78 | -7.43 | -15.23 | 202 |
| 26 | Parabolic SAR · 1h | trend | 85.27 | -14.73 | 176 | 29.0 | -15.13 | -3.25 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -16.39 | -4.61 | -17.28 | 97 |
| 28 | Donchian 55/20 · 1h | breakout | 81.99 | -18.01 | 73 | 13.7 | -23.08 | -4.82 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.85 | -19.15 | 2 | 0.0 | -9.89 | -1.14 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -17.82 | -6.24 | -18.32 | 115 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -15.43 | -3.60 | -23.29 | 91 |
| 32 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.59 | -3.56 | -25.39 | 167 |
| 33 | Stochastic reversion · 1h | reversion | 78.63 | -21.37 | 312 | 46.2 | -27.99 | -4.17 | -28.07 | 408 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.71 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 76.77 | -23.23 | 406 | 35.0 | -22.93 | -2.95 | -26.53 | 169 |
| 36 | ADX DI cross · 1h | trend | 76.53 | -23.47 | 200 | 20.0 | -23.46 | -3.48 | -32.66 | 265 |
| 37 | Hold BTC | benchmark | 76.52 | -23.48 | 1 | 0.0 | -15.80 | -2.23 | -26.39 | 1 |
| 38 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.59 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -23.36 | -4.88 | -30.71 | 238 |
| 41 | Max aggression: 1-day momentum | meta | 74.90 | -25.11 | 29 | 27.6 | -20.15 | -0.61 | -57.50 | 41 |
| 42 | Heikin-Ashi · 1h | trend | 74.62 | -25.38 | 445 | 24.0 | -37.14 | -6.82 | -39.47 | 661 |
| 43 | MACD zero-line · 1h | trend | 73.48 | -26.52 | 171 | 18.7 | -23.28 | -4.56 | -30.99 | 199 |
| 44 | RSI momentum · 1h | momentum | 72.60 | -27.40 | 171 | 14.0 | -26.78 | -4.11 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.54 | -27.46 | 109 | 10.1 | -28.28 | -4.78 | -40.51 | 120 |
| 46 | MACD cross · 1h | trend | 72.12 | -27.88 | 393 | 23.2 | -31.46 | -4.66 | -40.30 | 473 |
| 47 | Supertrend · 1h | trend | 71.93 | -28.07 | 182 | 14.8 | -29.23 | -4.95 | -36.83 | 206 |
| 48 | Triple EMA stack · 1h | trend | 71.63 | -28.37 | 151 | 14.6 | -27.19 | -4.46 | -38.65 | 201 |
| 49 | ROC + volume · 1h | momentum | 71.18 | -28.82 | 399 | 28.8 | -31.12 | -5.64 | -37.65 | 374 |
| 50 | Bollinger reversion · 1h | reversion | 70.75 | -29.25 | 310 | 40.6 | -36.09 | -5.69 | -36.13 | 393 |
| 51 | CCI reversion · 1h | reversion | 69.88 | -30.12 | 356 | 42.1 | -38.85 | -6.16 | -38.94 | 474 |
| 52 | OBV trend · 1h | momentum | 69.68 | -30.32 | 299 | 19.1 | -28.65 | -4.99 | -38.37 | 270 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.12 | -4.51 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.23 | -30.77 | 153 | 19.0 | -31.40 | -5.67 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 65.98 | -34.02 | 396 | 42.2 | -44.68 | -7.46 | -44.71 | 545 |
| 56 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1855 | 24.7 | -20.73 | -3.71 | -23.90 | 339 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -36.96 | -7.42 | -43.16 | 323 |
| 58 | VWAP momentum · 1h | momentum | 62.53 | -37.47 | 917 | 22.2 | -52.61 | -10.45 | -53.90 | 1234 |
| 59 | Candlestick reversal · 1h | reversion | 60.93 | -39.07 | 502 | 27.5 | -46.83 | -8.62 | -46.83 | 616 |
| 60 | RSI(14) reversion · 1h | reversion | 60.90 | -39.10 | 196 | 31.1 | -40.77 | -6.02 | -41.57 | 251 |
| 61 | Z-score reversion · 1h ⏸ | reversion | 60.56 | -39.45 | 215 | 35.3 | -33.25 | -4.58 | -34.52 | 237 |
| 62 | Three white soldiers | momentum | 58.18 | -41.82 | 544 | 14.5 | -49.19 | -21.96 | -49.51 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -44.96 | -99.04 | 5330 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.18 | -25.51 | -80.78 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -45.51 | -93.73 | 2536 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.79 | -32.05 | -89.96 | 1930 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.29 | -41.59 | -91.38 | 2346 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.24 | -29.58 | -89.30 | 2167 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -52.62 | -97.91 | 3502 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.20 | -56.61 | -96.22 | 3460 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.35 | -31.97 | -93.37 | 2308 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.97 | -34.12 | -82.97 | 1652 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -55.18 | -99.59 | 6058 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.15 | -43.07 | -92.15 | 2623 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.10 | -36.05 | -95.10 | 3433 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -75.12 | -99.82 | 6175 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.44 | -43.93 | -92.50 | 2289 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.21 | -26.42 | -76.30 | 1662 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.57 | -59.14 | -97.58 | 3512 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.97 | -60.17 | -98.97 | 4959 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.80 | -27.33 | -69.09 | 1253 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -57.70 | -94.72 | 2802 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.91 | -38.72 | -85.01 | 1778 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -70.59 | -99.69 | 6391 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.82 | -31.10 | -90.82 | 2347 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.27 | -19.25 | -80.63 | 1824 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.91 | -36.69 | -90.94 | 2199 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.31 | -46.36 | -97.33 | 3911 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.41 | -58.46 | -89.41 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.63 | -29.29 | -65.73 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.28 | -22.95 | -71.51 | 1256 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.35 | -18.35 | -81.48 | 1753 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.60 | -47.83 | -97.61 | 4367 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -116.35 | -99.93 | 8464 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-14T21:10 | Williams %R · 1h | sell | BTC-USD | 3.83 | -0.10 | stop-loss |
| 2026-11-14T21:10 | Stochastic reversion · 1h | sell | ETH-USD | 4.47 | -0.16 | stop-loss |
| 2026-11-14T21:10 | Stochastic reversion · 1h | sell | BTC-USD | 3.29 | -0.08 | stop-loss |
| 2026-11-14T21:10 | Bollinger reversion · 1h | sell | BTC-USD | 6.31 | -0.14 | stop-loss |
| 2026-11-14T21:10 | RSI(14) reversion · 1h | sell | BTC-USD | 15.14 | -0.37 | stop-loss |
| 2026-11-14T20:55 | MFI reversion · 1h | sell | XRP-USD | 8.49 | -0.38 | stop-loss |
| 2026-11-14T20:55 | Williams %R · 1h | sell | XRP-USD | 3.18 | -0.16 | stop-loss |
| 2026-11-14T20:55 | Williams %R · 1h | sell | SOL-USD | 3.21 | -0.13 | stop-loss |
| 2026-11-14T20:55 | Williams %R · 1h | sell | ETH-USD | 3.21 | -0.13 | stop-loss |
| 2026-11-14T20:55 | Williams %R · 1h | sell | DOGE-USD | 3.16 | -0.17 | stop-loss |
| 2026-11-14T20:55 | VWAP reversion · 1h | sell | XRP-USD | 22.54 | -1.10 | stop-loss |
| 2026-11-14T20:55 | VWAP reversion · 1h | sell | SOL-USD | 22.74 | -0.90 | stop-loss |
| 2026-11-14T20:55 | VWAP reversion · 1h | sell | DOGE-USD | 22.44 | -1.20 | stop-loss |
| 2026-11-14T20:55 | Z-score reversion · 1h | sell | ETH-USD | 14.79 | -0.59 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-14T20:55 | Z-score reversion · 1h | sell | BTC-USD | 15.02 | -0.35 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-14T20:55 | Bollinger reversion · 1h | sell | ETH-USD | 2.77 | -0.09 | stop-loss |
| 2026-11-14T20:55 | RSI(14) reversion · 1h | buy | BTC-USD | 3.16 | — | rebalance up |
| 2026-11-14T20:55 | RSI(14) reversion · 1h | sell | ETH-USD | 11.88 | -0.47 | stop-loss |
| 2026-11-14T20:55 | Candlestick reversal · 1h | sell | XRP-USD | 3.32 | -0.14 | stop-loss |
| 2026-11-14T20:55 | Candlestick reversal · 1h | sell | ETH-USD | 3.93 | -0.16 | stop-loss |
| 2026-11-14T20:55 | Candlestick reversal · 1h | sell | BTC-USD | 3.77 | -0.08 | stop-loss |
| 2026-11-14T20:15 | Stochastic reversion · 1h | buy | ETH-USD | 4.64 | — | entry |
| 2026-11-14T20:15 | Stochastic reversion · 1h | sell | DOGE-USD | 4.56 | -0.09 | stop-loss |
| 2026-11-14T20:15 | Bollinger reversion · 1h | buy | ETH-USD | 2.86 | — | entry |
| 2026-11-14T20:15 | Bollinger reversion · 1h | buy | BTC-USD | 6.45 | — | entry |
| 2026-11-14T20:15 | Bollinger reversion · 1h | sell | DOGE-USD | 8.68 | -0.22 | stop-loss |
| 2026-11-14T20:00 | Candlestick reversal · 1h | buy | XRP-USD | 3.46 | — | entry signal |
| 2026-11-14T18:00 | Williams %R · 1h | buy | XRP-USD | 3.33 | — | entry signal |
| 2026-11-14T18:00 | Williams %R · 1h | buy | SOL-USD | 3.33 | — | entry signal |
| 2026-11-14T18:00 | Williams %R · 1h | buy | ETH-USD | 3.33 | — | entry signal |
| 2026-11-14T18:00 | Williams %R · 1h | buy | DOGE-USD | 3.33 | — | entry signal |
| 2026-11-14T18:00 | VWAP reversion · 1h | buy | XRP-USD | 23.65 | — | entry signal |
| 2026-11-14T18:00 | VWAP reversion · 1h | buy | SOL-USD | 23.65 | — | entry signal |
| 2026-11-14T18:00 | VWAP reversion · 1h | buy | DOGE-USD | 23.65 | — | entry signal |
| 2026-11-14T18:00 | Z-score reversion · 1h | buy | ETH-USD | 15.37 | — | entry signal |
| 2026-11-14T18:00 | Z-score reversion · 1h | buy | BTC-USD | 15.37 | — | entry signal |
| 2026-11-14T18:00 | RSI(14) reversion · 1h | buy | ETH-USD | 12.35 | — | entry signal |
| 2026-11-14T18:00 | RSI(14) reversion · 1h | buy | BTC-USD | 12.35 | — | entry signal |
| 2026-11-14T18:00 | Candlestick reversal · 1h | buy | ETH-USD | 4.09 | — | entry signal |
| 2026-11-14T17:55 | Three white soldiers | sell | SOL-USD | 14.45 | -0.12 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-16 21:40:05.000128+00:00 -> 2026-11-14 21:50:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
