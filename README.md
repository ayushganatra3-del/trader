# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T15:59:05.000108+00:00 · 54744 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.23 (-12.77%)

Closed trades 164, win rate 35.4%, fees £5.01, max drawdown -13.61%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-10 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 16211 decisions in 2380 calls, $0.2150 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T15:59 | 1 / 24 / 5 | cash |  |
| Breezy | 2026-11-10T15:59 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-10T15:59 | 8 / 20 / 2 | COIN 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| MFI reversion | LABU | 1.70 | +6.34% | 4 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.49 | 3.91 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.65 | 13.65 | 0 | — | 14.05 | 4.73 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.56 | 11.56 | 31 | 29.0 | 20.68 | 3.09 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.99 | 1.16 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.52 | 1.06 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 98.15 | -1.85 | 178 | 28.7 | -2.68 | -1.05 | -9.75 | 152 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.16 | -3.84 | 0 | — | -2.10 | -0.66 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.48 | -4.52 | 136 | 46.3 | -13.63 | -3.47 | -13.66 | 150 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.24 | -5.76 | 0 | — | -4.85 | -1.27 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.86 | -7.14 | 108 | 23.1 | -13.51 | -5.03 | -17.82 | 78 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.26 | -7.74 | 0 | — | -4.83 | -1.28 | -10.64 | 1 |
| 20 | Copy: Insider buying | copy | 91.64 | -8.36 | 42 | 38.1 | -9.03 | -1.88 | -15.11 | 67 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.92 | -11.08 | 401 | 33.4 | -14.44 | -4.51 | -14.62 | 603 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.16 | -2.83 | -14.15 | 76 |
| 24 | Agent | meta | 87.23 | -12.77 | 164 | 35.4 | -13.57 | -6.97 | -14.22 | 203 |
| 25 | Daily: Bullish score | daily | 86.90 | -13.10 | 15 | 20.0 | -7.94 | -1.17 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 85.32 | -14.68 | 1 | 0.0 | -7.46 | -1.01 | -16.43 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.29 | -14.71 | 167 | 26.9 | -13.31 | -2.70 | -21.27 | 224 |
| 28 | Agent (aggressive) | meta | 84.92 | -15.08 | 77 | 32.5 | -15.80 | -4.42 | -18.51 | 96 |
| 29 | Donchian 55/20 · 1h | breakout | 84.18 | -15.82 | 71 | 14.1 | -16.53 | -3.49 | -22.11 | 102 |
| 30 | Opening range 15m | breakout | 82.77 | -17.23 | 495 | 31.7 | -17.92 | -5.10 | -19.09 | 737 |
| 31 | Keltner breakout · 1h | breakout | 81.99 | -18.01 | 109 | 22.9 | -20.19 | -4.19 | -25.10 | 176 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 81.81 | -18.19 | 2 | 0.0 | -9.58 | -1.11 | -24.16 | 1 |
| 33 | Max aggression: 5-day momentum | meta | 80.94 | -19.06 | 18 | 44.4 | -35.61 | -2.22 | -45.81 | 25 |
| 34 | Connors RSI(2) · 1h | reversion | 80.90 | -19.09 | 206 | 39.8 | -19.43 | -6.45 | -19.99 | 125 |
| 35 | Volume breakout · 1h | breakout | 80.84 | -19.16 | 146 | 27.4 | -14.64 | -3.41 | -21.36 | 93 |
| 36 | Stochastic reversion · 1h | reversion | 80.30 | -19.70 | 284 | 47.5 | -25.64 | -3.77 | -27.05 | 389 |
| 37 | Heikin-Ashi · 1h | trend | 79.26 | -20.74 | 415 | 24.3 | -40.48 | -7.54 | -43.10 | 675 |
| 38 | ADX DI cross · 1h | trend | 79.08 | -20.92 | 181 | 19.3 | -24.32 | -4.14 | -29.26 | 269 |
| 39 | Bollinger breakout · 1h | breakout | 76.89 | -23.11 | 170 | 22.9 | -21.41 | -4.41 | -27.92 | 238 |
| 40 | CCI reversion · 1h | reversion | 76.84 | -23.16 | 326 | 45.1 | -25.05 | -3.75 | -30.63 | 457 |
| 41 | MFI reversion · 1h | reversion | 76.80 | -23.20 | 359 | 33.7 | -19.23 | -2.46 | -21.69 | 158 |
| 42 | Ichimoku · 1h | trend | 75.67 | -24.33 | 99 | 15.2 | -31.24 | -8.87 | -31.35 | 120 |
| 43 | EMA 20/50 cross · 1h | trend | 74.83 | -25.17 | 102 | 10.8 | -23.94 | -4.20 | -33.53 | 122 |
| 44 | MACD cross · 1h | trend | 74.38 | -25.62 | 355 | 22.3 | -33.14 | -5.38 | -39.51 | 481 |
| 45 | MACD zero-line · 1h | trend | 73.90 | -26.10 | 157 | 16.6 | -25.76 | -5.17 | -30.21 | 216 |
| 46 | Bollinger reversion · 1h | reversion | 73.50 | -26.50 | 278 | 40.3 | -26.38 | -4.03 | -32.06 | 372 |
| 47 | RSI momentum · 1h | momentum | 73.04 | -26.96 | 159 | 12.6 | -24.32 | -4.02 | -33.30 | 210 |
| 48 | Supertrend · 1h | trend | 73.03 | -26.97 | 167 | 13.2 | -32.33 | -5.89 | -35.46 | 232 |
| 49 | Triple EMA stack · 1h | trend | 72.49 | -27.51 | 143 | 14.7 | -26.21 | -4.57 | -34.51 | 205 |
| 50 | Z-score reversion · 1h | reversion | 72.10 | -27.90 | 186 | 36.0 | -25.53 | -3.65 | -27.66 | 228 |
| 51 | OBV trend · 1h | momentum | 72.08 | -27.92 | 274 | 18.2 | -27.11 | -4.77 | -35.55 | 277 |
| 52 | Williams %R · 1h | reversion | 71.62 | -28.38 | 346 | 45.7 | -35.50 | -5.49 | -36.01 | 529 |
| 53 | Donchian 20/10 · 1h | breakout | 71.01 | -28.99 | 142 | 19.7 | -30.89 | -5.65 | -35.64 | 209 |
| 54 | ROC + volume · 1h | momentum | 70.97 | -29.03 | 358 | 26.8 | -36.16 | -6.86 | -38.16 | 380 |
| 55 | Daily: Momentum burst | daily | 70.93 | -29.07 | 27 | 11.1 | -38.48 | -5.47 | -39.18 | 34 |
| 56 | RSI(14) reversion · 1h | reversion | 66.43 | -33.57 | 170 | 30.6 | -28.34 | -4.20 | -32.51 | 222 |
| 57 | Max aggression: 1-day momentum | meta | 66.23 | -33.77 | 27 | 25.9 | -31.53 | -1.58 | -57.50 | 41 |
| 58 | VWAP momentum · 1h | momentum | 66.10 | -33.90 | 829 | 22.0 | -53.46 | -11.40 | -54.31 | 1227 |
| 59 | Agent (ML meta-label) | meta | 65.76 | -34.24 | 1658 | 24.2 | -11.82 | -1.88 | -17.52 | 336 |
| 60 | EMA 9/21 cross · 1h | trend | 65.24 | -34.76 | 249 | 9.6 | -38.21 | -7.50 | -41.09 | 335 |
| 61 | Candlestick reversal · 1h | reversion | 63.16 | -36.84 | 444 | 27.9 | -37.62 | -6.84 | -38.86 | 582 |
| 62 | Three white soldiers | momentum | 61.14 | -38.86 | 502 | 14.9 | -49.01 | -22.96 | -49.01 | 647 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.96 | -98.95 | 5291 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.86 | -25.90 | -79.88 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.23 | -44.69 | -93.23 | 2503 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.40 | -31.73 | -89.41 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.71 | -38.59 | -90.71 | 2313 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.16 | -31.34 | -90.22 | 2200 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -53.18 | -97.78 | 3452 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.20 | -54.01 | -96.20 | 3423 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.63 | -32.65 | -93.73 | 2399 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.45 | -33.94 | -82.45 | 1674 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -55.23 | -99.56 | 6022 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.27 | -42.69 | -92.27 | 2597 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.51 | -36.67 | -95.51 | 3417 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.55 | -99.81 | 6161 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.01 | -42.33 | -92.02 | 2250 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.49 | -24.35 | -75.53 | 1595 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -58.34 | -97.73 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -62.97 | -98.88 | 4893 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.57 | -26.88 | -68.99 | 1217 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -52.22 | -94.57 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.47 | -36.19 | -84.49 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -72.31 | -99.65 | 6361 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.93 | -32.39 | -89.93 | 2293 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.93 | -20.38 | -78.93 | 1783 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.91 | -36.83 | -90.91 | 2224 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.85 | -52.79 | -96.85 | 3896 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.31 | -55.73 | -89.37 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.28 | -27.05 | -66.01 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.09 | -22.61 | -71.15 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.52 | -19.58 | -80.54 | 1701 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -49.01 | -97.27 | 4308 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -104.59 | -99.93 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T15:55 | Williams %R · 1h | sell | COIN | 17.92 | -0.73 | stop-loss |
| 2026-11-10T15:55 | Opening range 30m | sell | AMZN | 22.14 | -0.17 | stop-loss |
| 2026-11-10T15:55 | Opening range 15m | buy | META | 8.77 | — | rebalance up |
| 2026-11-10T15:55 | Opening range 15m | buy | AMD | 8.87 | — | rebalance up |
| 2026-11-10T15:55 | Opening range 15m | sell | TQQQ | 11.82 | -0.13 | exit signal |
| 2026-11-10T15:55 | Opening range 15m | sell | SOXL | 11.65 | -0.40 | stop-loss |
| 2026-11-10T15:55 | Opening range 15m | sell | QQQ | 11.89 | -0.05 | exit signal |
| 2026-11-10T15:55 | Opening range 15m | sell | AMZN | 11.88 | -0.07 | stop-loss |
| 2026-11-10T15:50 | Agent (ML meta-label) | buy | SPY | 13.10 | — | entry |
| 2026-11-10T15:50 | Agent (aggressive) | sell | SQQQ | 42.98 | 1.04 | selected signal exited |
| 2026-11-10T15:50 | Agent | sell | SQQQ | 17.79 | 0.43 | selected signal exited |
| 2026-11-10T15:50 | Williams %R · 1h | sell | NVDA | 17.79 | -0.35 | stop-loss |
| 2026-11-10T15:50 | Z-score reversion · 1h | buy | TECL | 3.66 | — | rebalance up |
| 2026-11-10T15:50 | Z-score reversion · 1h | buy | SOXL | 3.72 | — | rebalance up |
| 2026-11-10T15:50 | Z-score reversion · 1h | sell | NVDA | 14.46 | -0.47 | stop-loss |
| 2026-11-10T15:50 | RSI(14) reversion · 1h | sell | NVDA | 16.52 | -0.58 | stop-loss |
| 2026-11-10T15:50 | Opening range 15m | sell | TECL | 11.78 | -0.19 | stop-loss |
| 2026-11-10T15:45 | Agent (ML meta-label) | sell | DOGE-USD | 13.10 | -0.45 | selected signal exited |
| 2026-11-10T15:45 | MFI reversion · 1h | buy | TECL | 6.03 | — | rebalance up |
| 2026-11-10T15:45 | MFI reversion · 1h | buy | SPY | 6.29 | — | rebalance up |
| 2026-11-10T15:45 | MFI reversion · 1h | buy | AMZN | 7.83 | — | rebalance up |
| 2026-11-10T15:45 | MFI reversion · 1h | buy | AAPL | 6.38 | — | rebalance up |
| 2026-11-10T15:45 | MFI reversion · 1h | sell | SOL-USD | 12.75 | -0.24 | stop-loss |
| 2026-11-10T15:45 | MFI reversion · 1h | sell | DOGE-USD | 12.66 | -0.53 | stop-loss |
| 2026-11-10T15:45 | CCI reversion · 1h | sell | NVDA | 19.07 | -0.57 | stop-loss |
| 2026-11-10T15:45 | Stochastic reversion · 1h | sell | XRP-USD | 19.90 | -0.46 | stop-loss |
| 2026-11-10T15:45 | Ichimoku · 1h | sell | LABU | 18.31 | -1.12 | stop-loss |
| 2026-11-10T15:45 | Opening range 15m | buy | TQQQ | 6.37 | — | rebalance up |
| 2026-11-10T15:45 | Opening range 15m | buy | TECL | 6.39 | — | rebalance up |
| 2026-11-10T15:45 | Opening range 15m | buy | SOXL | 6.58 | — | rebalance up |
| 2026-11-10T15:45 | Opening range 15m | buy | QQQ | 6.30 | — | rebalance up |
| 2026-11-10T15:45 | Opening range 15m | buy | META | 6.27 | — | rebalance up |
| 2026-11-10T15:45 | Opening range 15m | buy | AMZN | 5.48 | — | rebalance up |
| 2026-11-10T15:45 | Opening range 15m | buy | AMD | 6.36 | — | rebalance up |
| 2026-11-10T15:45 | Opening range 15m | sell | UPRO | 5.57 | -0.06 | stop-loss |
| 2026-11-10T15:45 | Opening range 15m | sell | SPY | 5.64 | -0.02 | stop-loss |
| 2026-11-10T15:45 | Opening range 15m | sell | GOOGL | 5.62 | -0.04 | stop-loss |
| 2026-11-10T15:40 | Agent (ML meta-label) | buy | TECL | 5.86 | — | rebalance up |
| 2026-11-10T15:40 | Agent (ML meta-label) | buy | DOGE-USD | 5.99 | — | rebalance up |
| 2026-11-10T15:40 | Agent (ML meta-label) | buy | COIN | 5.05 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 15:59:05.000108+00:00 -> 2026-11-10 16:09:05.000108+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
