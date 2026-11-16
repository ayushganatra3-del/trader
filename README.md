# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T06:10:05.000112+00:00 · 61570 ticks

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
| Copy: Insider buying | 2026-11-14 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 5040 decisions in 1008 calls, $0.0706 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T06:10 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-16T06:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-16T06:10 | 1 / 4 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.91 | 17.91 | 0 | — | 15.31 | 5.02 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 2.90 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.96 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.64 | 4.64 | 0 | — | 6.58 | 1.79 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 0.99 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 3.16 | 1.99 | -3.39 | 82 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.72 | 1.87 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.47 | 0.22 | -18.69 | 7 |
| 11 | Hold SPY | benchmark | 98.34 | -1.67 | 0 | — | -0.61 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.89 | -3.11 | 1 | 0.0 | -3.27 | -2.13 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.70 | -3.30 | 191 | 30.4 | -2.50 | -0.84 | -8.33 | 153 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.36 | -3.64 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.26 | -5.74 | 43 | 39.5 | -7.13 | -1.42 | -14.95 | 58 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.26 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.85 | -8.15 | 110 | 22.7 | -12.74 | -5.62 | -14.95 | 64 |
| 20 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.88 | -3.47 | -18.48 | 151 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -4.02 | -0.87 | -16.02 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.26 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.61 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.70 | -14.30 | 16 | 18.8 | -10.26 | -1.97 | -19.56 | 19 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.17 | -7.05 | -15.01 | 193 |
| 26 | Parabolic SAR · 1h | trend | 84.72 | -15.28 | 176 | 29.0 | -15.70 | -3.36 | -22.81 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -14.83 | -4.08 | -16.59 | 92 |
| 28 | Donchian 55/20 · 1h | breakout | 82.00 | -18.00 | 73 | 13.7 | -23.08 | -4.78 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.86 | -19.14 | 2 | 0.0 | -9.89 | -1.38 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -16.83 | -6.41 | -16.91 | 109 |
| 31 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.02 | -3.40 | -25.39 | 165 |
| 32 | Volume breakout · 1h | breakout | 79.96 | -20.04 | 161 | 28.6 | -14.06 | -3.20 | -22.55 | 90 |
| 33 | Stochastic reversion · 1h | reversion | 78.86 | -21.14 | 314 | 46.5 | -24.51 | -3.60 | -28.40 | 406 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.88 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 76.96 | -23.04 | 407 | 35.1 | -18.70 | -2.41 | -26.89 | 163 |
| 36 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.57 | -50.62 | 22 |
| 37 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -29.98 | -8.25 | -31.49 | 115 |
| 38 | Hold BTC | benchmark | 75.15 | -24.85 | 2 | 0.0 | -16.92 | -2.39 | -28.91 | 1 |
| 39 | Max aggression: 1-day momentum | meta | 74.90 | -25.10 | 29 | 27.6 | -21.85 | -0.73 | -57.50 | 40 |
| 40 | Bollinger breakout · 1h | breakout | 74.59 | -25.41 | 184 | 22.3 | -23.16 | -4.79 | -31.20 | 235 |
| 41 | ADX DI cross · 1h | trend | 74.53 | -25.47 | 206 | 19.4 | -25.44 | -3.80 | -34.43 | 272 |
| 42 | Heikin-Ashi · 1h | trend | 74.04 | -25.96 | 452 | 23.7 | -38.05 | -6.98 | -40.73 | 669 |
| 43 | MACD zero-line · 1h | trend | 72.96 | -27.04 | 172 | 18.6 | -23.66 | -4.60 | -31.23 | 200 |
| 44 | RSI momentum · 1h | momentum | 72.61 | -27.39 | 171 | 14.0 | -26.86 | -4.12 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.55 | -27.45 | 109 | 10.1 | -29.14 | -5.09 | -40.75 | 119 |
| 46 | Triple EMA stack · 1h | trend | 71.63 | -28.36 | 151 | 14.6 | -27.40 | -4.46 | -38.66 | 201 |
| 47 | MACD cross · 1h | trend | 71.63 | -28.37 | 394 | 23.1 | -31.98 | -4.73 | -41.23 | 476 |
| 48 | Supertrend · 1h | trend | 71.52 | -28.48 | 182 | 14.8 | -30.92 | -5.44 | -37.43 | 208 |
| 49 | Bollinger reversion · 1h | reversion | 70.86 | -29.14 | 313 | 40.9 | -31.90 | -4.96 | -33.59 | 391 |
| 50 | CCI reversion · 1h | reversion | 70.11 | -29.89 | 359 | 42.6 | -35.20 | -5.54 | -39.14 | 468 |
| 51 | ROC + volume · 1h | momentum | 70.05 | -29.95 | 402 | 28.6 | -31.02 | -5.57 | -37.90 | 364 |
| 52 | OBV trend · 1h | momentum | 69.69 | -30.31 | 299 | 19.1 | -28.36 | -4.89 | -38.28 | 270 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.10 | -4.60 | -37.81 | 35 |
| 54 | Donchian 20/10 · 1h | breakout | 68.81 | -31.19 | 153 | 19.0 | -30.37 | -5.40 | -37.82 | 205 |
| 55 | Williams %R · 1h | reversion | 66.09 | -33.91 | 404 | 42.3 | -41.05 | -6.87 | -42.52 | 545 |
| 56 | Agent (ML meta-label) | meta | 65.08 | -34.92 | 1855 | 24.7 | -21.66 | -4.24 | -25.58 | 326 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -37.93 | -7.62 | -43.65 | 329 |
| 58 | VWAP momentum · 1h | momentum | 62.52 | -37.48 | 918 | 22.2 | -51.90 | -10.10 | -53.45 | 1234 |
| 59 | RSI(14) reversion · 1h | reversion | 61.45 | -38.55 | 199 | 32.2 | -37.86 | -5.51 | -40.40 | 247 |
| 60 | Candlestick reversal · 1h | reversion | 60.76 | -39.24 | 511 | 27.8 | -43.52 | -8.15 | -43.70 | 616 |
| 61 | Z-score reversion · 1h | reversion | 60.41 | -39.59 | 216 | 35.6 | -34.13 | -4.69 | -35.69 | 238 |
| 62 | Three white soldiers | momentum | 57.58 | -42.42 | 559 | 14.8 | -49.41 | -21.77 | -49.42 | 668 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -42.14 | -99.02 | 5330 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.31 | -26.86 | -81.35 | 1433 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.92 | -45.42 | -93.92 | 2541 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.04 | -33.11 | -90.04 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.63 | -42.18 | -91.63 | 2360 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.89 | -30.64 | -89.91 | 2189 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -49.81 | -97.89 | 3498 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -57.57 | -96.49 | 3486 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -33.25 | -93.68 | 2321 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.18 | -33.65 | -83.18 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.27 | -99.60 | 6069 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.17 | -42.34 | -92.23 | 2628 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.20 | -35.34 | -95.20 | 3450 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.55 | -99.81 | 6173 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.49 | -42.92 | -92.50 | 2296 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.48 | -26.29 | -76.68 | 1682 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -57.14 | -97.62 | 3504 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.97 | -56.47 | -98.98 | 4963 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.14 | -27.02 | -69.29 | 1246 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -54.83 | -94.75 | 2804 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.76 | -37.11 | -84.83 | 1777 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -68.35 | -99.69 | 6399 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.75 | -30.51 | -90.75 | 2347 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.67 | -18.65 | -80.37 | 1816 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.11 | -35.53 | -91.14 | 2194 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.43 | -44.52 | -97.43 | 3922 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.34 | -55.83 | -89.34 | 2174 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.61 | -29.68 | -66.73 | 833 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.29 | -23.18 | -72.31 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.92 | -17.67 | -81.42 | 1757 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.53 | -45.25 | -97.55 | 4359 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -93.25 | -99.94 | 8463 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T06:00 | ROC + volume · 1h | sell | DOGE-USD | 17.27 | -0.32 | exit signal |
| 2026-11-16T06:00 | MACD zero-line · 1h | sell | XRP-USD | 17.85 | -0.52 | exit signal |
| 2026-11-16T06:00 | MACD cross · 1h | buy | DOGE-USD | 5.68 | — | rebalance up |
| 2026-11-16T06:00 | MACD cross · 1h | sell | XRP-USD | 10.09 | -0.22 | exit signal |
| 2026-11-16T03:10 | Three white soldiers | sell | DOGE-USD | 14.37 | -0.06 | exit signal |
| 2026-11-16T03:00 | Williams %R · 1h | buy | BTC-USD | 4.13 | — | entry signal |
| 2026-11-16T03:00 | Candlestick reversal · 1h | buy | ETH-USD | 3.39 | — | entry signal |
| 2026-11-16T03:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.81 | — | entry signal |
| 2026-11-16T03:00 | Candlestick reversal · 1h | buy | BTC-USD | 3.81 | — | entry signal |
| 2026-11-16T03:00 | ROC + volume · 1h | buy | DOGE-USD | 17.59 | — | entry signal |
| 2026-11-16T02:55 | Three white soldiers | sell | SOL-USD | 14.35 | -0.08 | exit signal |
| 2026-11-16T02:15 | Three white soldiers | buy | SOL-USD | 14.43 | — | entry signal |
| 2026-11-16T02:15 | Three white soldiers | buy | DOGE-USD | 14.43 | — | entry signal |
| 2026-11-16T02:00 | Volume breakout · 1h | sell | DOGE-USD | 19.57 | -0.57 | exit signal |
| 2026-11-16T02:00 | Squeeze breakout · 1h | sell | DOGE-USD | 21.38 | -0.62 | exit signal |
| 2026-11-16T02:00 | Bollinger breakout · 1h | sell | DOGE-USD | 18.25 | -0.53 | exit signal |
| 2026-11-16T02:00 | ROC + volume · 1h | sell | DOGE-USD | 17.29 | -0.50 | exit signal |
| 2026-11-16T02:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 8.59 | -0.16 | exit signal |
| 2026-11-16T02:00 | ADX DI cross · 1h | sell | DOGE-USD | 18.42 | -0.50 | exit signal |
| 2026-11-16T01:00 | Candlestick reversal · 1h | sell | XRP-USD | 3.75 | -0.06 | exit signal |
| 2026-11-16T01:00 | Candlestick reversal · 1h | sell | SOL-USD | 2.82 | 0.02 | exit signal |
| 2026-11-16T01:00 | Candlestick reversal · 1h | sell | BTC-USD | 4.35 | 0.00 | exit signal |
| 2026-11-16T01:00 | ROC + volume · 1h | sell | SOL-USD | 17.48 | -0.32 | exit signal |
| 2026-11-16T01:00 | VWAP momentum · 1h | sell | BTC-USD | 3.11 | -0.02 | exit signal |
| 2026-11-16T01:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 8.75 | — | entry |
| 2026-11-16T01:00 | Heikin-Ashi · 1h | sell | SOL-USD | 8.15 | -0.11 | exit signal |
| 2026-11-16T01:00 | ADX DI cross · 1h | buy | DOGE-USD | 3.82 | — | rebalance up |
| 2026-11-16T01:00 | ADX DI cross · 1h | sell | SOL-USD | 14.83 | -0.27 | exit signal |
| 2026-11-16T01:00 | ADX DI cross · 1h | sell | BTC-USD | 14.91 | -0.19 | exit signal |
| 2026-11-16T00:00 | CCI reversion · 1h | sell | XRP-USD | 4.32 | 0.20 | exit signal |
| 2026-11-16T00:00 | Williams %R · 1h | sell | XRP-USD | 4.20 | 0.07 | exit signal |
| 2026-11-16T00:00 | RSI(14) reversion · 1h | buy | ETH-USD | 4.64 | — | rebalance up |
| 2026-11-16T00:00 | RSI(14) reversion · 1h | buy | BTC-USD | 4.67 | — | rebalance up |
| 2026-11-16T00:00 | RSI(14) reversion · 1h | sell | SOL-USD | 8.90 | 0.11 | exit signal |
| 2026-11-16T00:00 | RSI(14) reversion · 1h | sell | DOGE-USD | 7.79 | 0.12 | exit signal |
| 2026-11-16T00:00 | Candlestick reversal · 1h | buy | XRP-USD | 3.82 | — | entry |
| 2026-11-16T00:00 | Candlestick reversal · 1h | sell | DOGE-USD | 3.88 | 0.08 | exit signal |
| 2026-11-16T00:00 | Volume breakout · 1h | buy | DOGE-USD | 20.13 | — | entry signal |
| 2026-11-16T00:00 | Squeeze breakout · 1h | buy | DOGE-USD | 22.00 | — | entry signal |
| 2026-11-16T00:00 | Bollinger breakout · 1h | buy | DOGE-USD | 18.78 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 06:10:05.000112+00:00 -> 2026-11-16 06:20:05.000112+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 06:10:05.000112+00:00 -> 2026-11-16 06:20:05.000112+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
