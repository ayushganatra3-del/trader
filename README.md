# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-15T02:10:05.000135+00:00 · 60106 ticks

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

Today: 1800 decisions in 360 calls, $0.0253 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-15T02:10 | 4 / 1 / 0 | DOGE-USD 20%, SOL-USD 17%, XRP-USD 15%, ETH-USD 14% |  |
| Breezy | 2026-11-15T02:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-15T02:10 | 5 / 0 / 0 | ETH-USD 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 3.27 | +5.62% | 11 |
| Bollinger reversion | TSLA | 2.67 | +2.69% | 7 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| Z-score reversion | TQQQ | 2.19 | +4.95% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.89 | 17.89 | 0 | — | 15.31 | 5.07 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 2.92 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.99 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.63 | 4.63 | 0 | — | 6.58 | 1.81 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 1.00 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 2.98 | 1.86 | -4.12 | 86 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.72 | 1.89 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.22 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.33 | -1.67 | 0 | — | -0.61 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.89 | -3.12 | 1 | 0.0 | -3.27 | -2.15 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.69 | -3.31 | 191 | 30.4 | -3.13 | -1.09 | -8.46 | 150 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.35 | -3.65 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.25 | -5.75 | 43 | 39.5 | -6.38 | -1.27 | -14.79 | 60 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.86 | -3.41 | -5.99 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.27 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.07 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.84 | -8.15 | 110 | 22.7 | -16.08 | -6.12 | -17.77 | 69 |
| 20 | VWAP reversion · 1h | reversion | 89.88 | -10.12 | 150 | 45.3 | -18.32 | -4.47 | -19.60 | 159 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.28 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.64 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.69 | -14.31 | 16 | 18.8 | -10.26 | -1.98 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.23 | -7.14 | -15.23 | 195 |
| 26 | Parabolic SAR · 1h | trend | 85.27 | -14.73 | 176 | 29.0 | -15.13 | -3.25 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -15.54 | -4.36 | -16.69 | 93 |
| 28 | Donchian 55/20 · 1h | breakout | 81.99 | -18.01 | 73 | 13.7 | -23.08 | -4.82 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.85 | -19.15 | 2 | 0.0 | -9.89 | -1.39 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -17.99 | -6.32 | -18.11 | 112 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -14.40 | -3.35 | -23.29 | 89 |
| 32 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.02 | -3.43 | -25.39 | 165 |
| 33 | Stochastic reversion · 1h | reversion | 78.65 | -21.35 | 312 | 46.2 | -27.80 | -4.15 | -28.40 | 412 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.92 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 76.82 | -23.18 | 406 | 35.0 | -23.02 | -2.96 | -26.93 | 170 |
| 36 | ADX DI cross · 1h | trend | 76.53 | -23.47 | 200 | 20.0 | -23.76 | -3.54 | -32.66 | 266 |
| 37 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.59 | -50.62 | 22 |
| 38 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -26.69 | -6.13 | -31.58 | 117 |
| 39 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.62 | -4.70 | -30.71 | 234 |
| 40 | Max aggression: 1-day momentum | meta | 74.90 | -25.11 | 29 | 27.6 | -20.15 | -0.61 | -57.50 | 41 |
| 41 | Heikin-Ashi · 1h | trend | 74.62 | -25.38 | 445 | 24.0 | -37.14 | -6.72 | -39.47 | 661 |
| 42 | Hold BTC | benchmark | 74.48 | -25.52 | 2 | 0.0 | -18.26 | -2.68 | -28.91 | 1 |
| 43 | MACD zero-line · 1h | trend | 73.48 | -26.52 | 171 | 18.7 | -23.28 | -4.56 | -30.99 | 199 |
| 44 | RSI momentum · 1h | momentum | 72.60 | -27.40 | 171 | 14.0 | -26.62 | -4.07 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.54 | -27.46 | 109 | 10.1 | -28.26 | -4.77 | -40.51 | 120 |
| 46 | MACD cross · 1h | trend | 72.12 | -27.88 | 393 | 23.2 | -31.46 | -4.66 | -40.30 | 473 |
| 47 | Supertrend · 1h | trend | 71.93 | -28.07 | 182 | 14.8 | -29.23 | -4.95 | -36.83 | 206 |
| 48 | Triple EMA stack · 1h | trend | 71.63 | -28.37 | 151 | 14.6 | -27.22 | -4.49 | -38.65 | 201 |
| 49 | ROC + volume · 1h | momentum | 71.18 | -28.82 | 399 | 28.8 | -29.74 | -5.33 | -37.65 | 367 |
| 50 | Bollinger reversion · 1h | reversion | 70.67 | -29.33 | 311 | 40.5 | -36.47 | -5.76 | -37.12 | 398 |
| 51 | CCI reversion · 1h | reversion | 69.91 | -30.09 | 356 | 42.1 | -38.64 | -6.14 | -39.04 | 474 |
| 52 | OBV trend · 1h | momentum | 69.68 | -30.32 | 299 | 19.1 | -28.63 | -4.99 | -38.37 | 270 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.12 | -4.64 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.23 | -30.77 | 153 | 19.0 | -29.93 | -5.35 | -37.58 | 204 |
| 55 | Williams %R · 1h | reversion | 65.76 | -34.24 | 398 | 42.0 | -44.70 | -7.50 | -45.18 | 549 |
| 56 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1855 | 24.7 | -26.85 | -5.15 | -29.68 | 329 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -36.96 | -7.42 | -43.16 | 323 |
| 58 | VWAP momentum · 1h | momentum | 62.53 | -37.47 | 917 | 22.2 | -52.68 | -10.39 | -53.42 | 1232 |
| 59 | RSI(14) reversion · 1h | reversion | 61.00 | -39.00 | 196 | 31.1 | -40.83 | -6.04 | -41.33 | 247 |
| 60 | Candlestick reversal · 1h | reversion | 60.85 | -39.15 | 503 | 27.4 | -46.19 | -8.65 | -46.32 | 614 |
| 61 | Z-score reversion · 1h | reversion | 60.56 | -39.45 | 215 | 35.3 | -33.82 | -4.70 | -34.52 | 233 |
| 62 | Three white soldiers | momentum | 58.11 | -41.89 | 546 | 14.7 | -49.41 | -21.59 | -49.43 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.08 | -43.69 | -99.08 | 5346 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.39 | -25.83 | -80.69 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -43.10 | -93.71 | 2533 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.01 | -32.93 | -90.16 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.53 | -41.38 | -91.53 | 2352 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.27 | -29.48 | -89.32 | 2161 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.94 | -50.82 | -97.94 | 3499 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -52.52 | -96.23 | 3459 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.38 | -31.17 | -93.41 | 2306 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.91 | -32.80 | -82.91 | 1650 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -50.55 | -99.60 | 6064 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.24 | -42.02 | -92.24 | 2621 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.09 | -34.59 | -95.09 | 3430 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -67.04 | -99.82 | 6188 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.55 | -43.18 | -92.55 | 2288 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.53 | -26.18 | -76.53 | 1664 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.54 | -54.13 | -97.54 | 3501 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -52.76 | -99.01 | 4967 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.06 | -26.92 | -69.06 | 1251 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -54.62 | -94.74 | 2799 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.05 | -37.81 | -85.05 | 1777 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -62.67 | -99.70 | 6396 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.03 | -29.78 | -91.15 | 2354 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.50 | -18.78 | -81.20 | 1829 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.20 | -35.86 | -91.27 | 2202 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.34 | -43.34 | -97.38 | 3911 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -56.94 | -89.51 | 2165 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.74 | -28.82 | -65.74 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.40 | -22.46 | -71.51 | 1254 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.38 | -17.80 | -81.91 | 1760 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.59 | -43.75 | -97.65 | 4370 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -93.37 | -99.93 | 8455 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-15T01:45 | Williams %R · 1h | sell | SOL-USD | 3.15 | -0.15 | stop-loss |
| 2026-11-15T01:45 | VWAP reversion · 1h | sell | SOL-USD | 21.83 | -1.02 | stop-loss |
| 2026-11-15T01:35 | Candlestick reversal · 1h | sell | SOL-USD | 3.92 | -0.14 | stop-loss |
| 2026-11-15T01:30 | Williams %R · 1h | sell | BTC-USD | 3.20 | -0.10 | stop-loss |
| 2026-11-15T01:30 | VWAP reversion · 1h | sell | BTC-USD | 22.14 | -0.70 | stop-loss |
| 2026-11-15T01:30 | Bollinger reversion · 1h | buy | ETH-USD | 5.71 | — | entry |
| 2026-11-15T01:30 | Bollinger reversion · 1h | sell | BTC-USD | 5.71 | -0.18 | stop-loss |
| 2026-11-15T01:00 | MFI reversion · 1h | buy | XRP-USD | 8.49 | — | entry signal |
| 2026-11-15T01:00 | CCI reversion · 1h | buy | XRP-USD | 4.11 | — | entry signal |
| 2026-11-15T01:00 | RSI(14) reversion · 1h | buy | XRP-USD | 15.22 | — | entry signal |
| 2026-11-15T00:55 | Three white soldiers | sell | XRP-USD | 14.59 | 0.04 | exit signal |
| 2026-11-15T00:25 | Three white soldiers | sell | BTC-USD | 14.43 | -0.11 | exit signal |
| 2026-11-15T00:00 | Hold BTC | buy | BTC-USD | 75.13 | — | entry |
| 2026-11-15T00:00 | Williams %R · 1h | buy | XRP-USD | 3.30 | — | entry signal |
| 2026-11-15T00:00 | Williams %R · 1h | buy | SOL-USD | 3.30 | — | entry signal |
| 2026-11-15T00:00 | Williams %R · 1h | buy | ETH-USD | 3.30 | — | entry signal |
| 2026-11-15T00:00 | Williams %R · 1h | buy | DOGE-USD | 3.30 | — | entry signal |
| 2026-11-15T00:00 | Williams %R · 1h | buy | BTC-USD | 3.30 | — | entry signal |
| 2026-11-15T00:00 | VWAP reversion · 1h | buy | XRP-USD | 22.84 | — | entry signal |
| 2026-11-15T00:00 | VWAP reversion · 1h | buy | SOL-USD | 22.84 | — | entry signal |
| 2026-11-15T00:00 | VWAP reversion · 1h | buy | ETH-USD | 22.84 | — | entry signal |
| 2026-11-15T00:00 | VWAP reversion · 1h | buy | BTC-USD | 22.84 | — | entry signal |
| 2026-11-15T00:00 | Bollinger reversion · 1h | buy | DOGE-USD | 3.19 | — | entry signal |
| 2026-11-15T00:00 | Bollinger reversion · 1h | buy | BTC-USD | 5.90 | — | entry signal |
| 2026-11-15T00:00 | Candlestick reversal · 1h | buy | XRP-USD | 4.06 | — | entry signal |
| 2026-11-15T00:00 | Candlestick reversal · 1h | buy | SOL-USD | 4.06 | — | entry signal |
| 2026-11-14T23:55 | Three white soldiers | buy | XRP-USD | 14.55 | — | entry signal |
| 2026-11-14T23:55 | Three white soldiers | buy | BTC-USD | 14.55 | — | entry signal |
| 2026-11-14T22:10 | Hold BTC | sell | BTC-USD | 75.13 | -13.30 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-14T22:00 | Stochastic reversion · 1h | buy | SOL-USD | 2.86 | — | entry signal |
| 2026-11-14T22:00 | Stochastic reversion · 1h | buy | DOGE-USD | 4.91 | — | entry signal |
| 2026-11-14T21:10 | Williams %R · 1h | sell | BTC-USD | 3.83 | -0.10 | stop-loss |
| 2026-11-14T21:10 | Stochastic reversion · 1h | sell | ETH-USD | 4.47 | -0.16 | stop-loss |
| 2026-11-14T21:10 | Stochastic reversion · 1h | sell | BTC-USD | 3.29 | -0.08 | stop-loss |
| 2026-11-14T21:10 | Bollinger reversion · 1h | sell | BTC-USD | 6.31 | -0.14 | stop-loss |
| 2026-11-14T21:10 | RSI(14) reversion · 1h | sell | BTC-USD | 15.14 | -0.37 | stop-loss |
| 2026-11-14T20:55 | MFI reversion · 1h | sell | XRP-USD | 8.49 | -0.38 | stop-loss |
| 2026-11-14T20:55 | Williams %R · 1h | sell | XRP-USD | 3.18 | -0.16 | stop-loss |
| 2026-11-14T20:55 | Williams %R · 1h | sell | SOL-USD | 3.21 | -0.13 | stop-loss |
| 2026-11-14T20:55 | Williams %R · 1h | sell | ETH-USD | 3.21 | -0.13 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-17 02:10:05.000135+00:00 -> 2026-11-15 02:20:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
