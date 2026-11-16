# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T13:41:05.000131+00:00 · 61964 ticks

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
| Copy: Insider buying | 2026-11-16 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 10950 decisions in 2190 calls, $0.1534 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T13:41 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-16T13:41 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-16T13:41 | 2 / 3 / 0 | ETH-USD 58% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.97 | 17.97 | 0 | — | 15.31 | 5.02 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 2.90 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.96 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.70 | 4.70 | 0 | — | 6.58 | 1.79 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 0.99 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 3.07 | 1.93 | -3.47 | 82 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.59 | 1.84 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.47 | 0.22 | -18.69 | 7 |
| 11 | Hold SPY | benchmark | 98.39 | -1.61 | 0 | — | -0.61 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.95 | -3.05 | 1 | 0.0 | -3.27 | -2.13 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.74 | -3.27 | 191 | 30.4 | -2.63 | -0.89 | -8.42 | 160 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.42 | -3.58 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.31 | -5.69 | 43 | 39.5 | -7.13 | -1.42 | -14.95 | 58 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.76 | -6.24 | 0 | — | -4.81 | -1.26 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.89 | -8.11 | 110 | 22.7 | -12.74 | -5.62 | -14.95 | 64 |
| 20 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -4.14 | -0.91 | -16.02 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.26 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.61 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.73 | -14.27 | 16 | 18.8 | -10.26 | -1.97 | -19.56 | 19 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.17 | -7.05 | -15.01 | 193 |
| 26 | Parabolic SAR · 1h | trend | 84.77 | -15.23 | 177 | 28.8 | -16.02 | -3.51 | -22.83 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -14.83 | -4.08 | -16.59 | 92 |
| 28 | Donchian 55/20 · 1h | breakout | 82.03 | -17.97 | 73 | 13.7 | -23.08 | -4.78 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.91 | -19.09 | 2 | 0.0 | -9.89 | -1.38 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.65 | -19.35 | 212 | 40.1 | -13.84 | -5.82 | -14.56 | 103 |
| 31 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.02 | -3.40 | -25.39 | 165 |
| 32 | Volume breakout · 1h | breakout | 79.96 | -20.04 | 161 | 28.6 | -14.06 | -3.20 | -22.55 | 90 |
| 33 | Stochastic reversion · 1h | reversion | 78.90 | -21.10 | 314 | 46.5 | -24.23 | -3.55 | -28.40 | 405 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.88 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 77.00 | -23.00 | 407 | 35.1 | -17.71 | -2.27 | -26.60 | 164 |
| 36 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.57 | -50.62 | 22 |
| 37 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -29.98 | -8.25 | -31.49 | 115 |
| 38 | Hold BTC | benchmark | 75.13 | -24.87 | 2 | 0.0 | -15.52 | -2.18 | -28.91 | 1 |
| 39 | Max aggression: 1-day momentum | meta | 74.95 | -25.05 | 29 | 27.6 | -23.32 | -0.83 | -57.50 | 39 |
| 40 | Bollinger breakout · 1h | breakout | 74.59 | -25.41 | 184 | 22.3 | -23.16 | -4.79 | -31.20 | 235 |
| 41 | ADX DI cross · 1h | trend | 74.53 | -25.47 | 206 | 19.4 | -25.49 | -3.81 | -34.43 | 273 |
| 42 | Heikin-Ashi · 1h | trend | 74.07 | -25.93 | 452 | 23.7 | -38.05 | -6.98 | -40.73 | 669 |
| 43 | MACD zero-line · 1h | trend | 72.97 | -27.02 | 172 | 18.6 | -23.75 | -4.62 | -31.23 | 200 |
| 44 | RSI momentum · 1h | momentum | 72.65 | -27.35 | 171 | 14.0 | -27.43 | -4.27 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 109 | 10.1 | -32.43 | -7.63 | -39.46 | 116 |
| 46 | Triple EMA stack · 1h | trend | 71.66 | -28.34 | 151 | 14.6 | -27.17 | -4.40 | -38.66 | 201 |
| 47 | Supertrend · 1h | trend | 71.52 | -28.48 | 182 | 14.8 | -32.06 | -5.83 | -37.68 | 206 |
| 48 | MACD cross · 1h | trend | 71.39 | -28.61 | 398 | 22.9 | -32.25 | -4.76 | -41.23 | 473 |
| 49 | Bollinger reversion · 1h | reversion | 70.83 | -29.17 | 313 | 40.9 | -32.01 | -4.98 | -33.59 | 393 |
| 50 | ROC + volume · 1h | momentum | 70.07 | -29.93 | 402 | 28.6 | -30.83 | -5.52 | -37.90 | 364 |
| 51 | CCI reversion · 1h | reversion | 70.04 | -29.96 | 359 | 42.6 | -35.17 | -5.54 | -39.14 | 471 |
| 52 | OBV trend · 1h | momentum | 69.72 | -30.28 | 299 | 19.1 | -28.57 | -4.91 | -38.36 | 271 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.10 | -4.60 | -37.81 | 35 |
| 54 | Donchian 20/10 · 1h | breakout | 68.70 | -31.30 | 154 | 18.8 | -30.52 | -5.43 | -37.95 | 205 |
| 55 | Williams %R · 1h | reversion | 65.98 | -34.02 | 404 | 42.3 | -41.22 | -6.91 | -42.52 | 548 |
| 56 | Agent (ML meta-label) | meta | 65.12 | -34.88 | 1855 | 24.7 | -17.65 | -2.65 | -23.39 | 325 |
| 57 | EMA 9/21 cross · 1h | trend | 64.74 | -35.26 | 267 | 11.6 | -37.81 | -7.58 | -43.65 | 329 |
| 58 | VWAP momentum · 1h | momentum | 62.52 | -37.48 | 919 | 22.2 | -51.83 | -10.09 | -53.34 | 1237 |
| 59 | RSI(14) reversion · 1h | reversion | 61.42 | -38.58 | 199 | 32.2 | -37.14 | -5.34 | -40.40 | 246 |
| 60 | Candlestick reversal · 1h | reversion | 60.63 | -39.37 | 514 | 27.6 | -43.28 | -8.09 | -43.46 | 619 |
| 61 | Z-score reversion · 1h | reversion | 60.34 | -39.66 | 216 | 35.6 | -34.26 | -4.72 | -35.69 | 238 |
| 62 | Three white soldiers | momentum | 57.15 | -42.85 | 562 | 14.8 | -49.78 | -22.15 | -49.78 | 668 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -42.10 | -99.01 | 5330 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.25 | -26.62 | -81.39 | 1432 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.91 | -45.08 | -93.91 | 2541 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.13 | -33.60 | -90.14 | 1938 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.65 | -42.85 | -91.65 | 2356 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.91 | -30.69 | -89.91 | 2190 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -50.38 | -97.92 | 3501 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -57.44 | -96.49 | 3478 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -34.63 | -93.55 | 2309 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.11 | -33.58 | -83.11 | 1654 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.84 | -99.60 | 6061 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.17 | -43.42 | -92.22 | 2628 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.20 | -35.35 | -95.20 | 3450 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.72 | -99.82 | 6181 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.51 | -43.83 | -92.52 | 2294 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.44 | -26.36 | -76.63 | 1681 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -56.77 | -97.62 | 3499 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -56.83 | -99.00 | 4969 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.09 | -27.28 | -69.25 | 1246 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -56.36 | -94.75 | 2803 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.73 | -37.17 | -84.80 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -68.37 | -99.69 | 6398 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.72 | -30.54 | -90.75 | 2349 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.42 | -18.59 | -80.12 | 1810 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.88 | -35.29 | -90.92 | 2190 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.41 | -44.06 | -97.41 | 3918 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.38 | -61.83 | -89.41 | 2177 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.50 | -29.58 | -66.62 | 833 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.11 | -22.97 | -72.14 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.33 | -17.44 | -80.78 | 1752 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.54 | -45.51 | -97.57 | 4361 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.92 | -99.94 | 8470 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T12:00 | VWAP momentum · 1h | sell | SOL-USD | 3.57 | -0.04 | exit signal |
| 2026-11-16T11:00 | CCI reversion · 1h | buy | XRP-USD | 3.34 | — | entry signal |
| 2026-11-16T11:00 | CCI reversion · 1h | buy | DOGE-USD | 3.34 | — | entry signal |
| 2026-11-16T11:00 | Williams %R · 1h | buy | XRP-USD | 3.31 | — | entry signal |
| 2026-11-16T11:00 | Williams %R · 1h | buy | SOL-USD | 3.31 | — | entry signal |
| 2026-11-16T11:00 | Williams %R · 1h | buy | ETH-USD | 3.31 | — | entry signal |
| 2026-11-16T11:00 | Bollinger reversion · 1h | buy | XRP-USD | 1.31 | — | entry signal |
| 2026-11-16T11:00 | Bollinger reversion · 1h | buy | ETH-USD | 7.88 | — | entry signal |
| 2026-11-16T11:00 | Candlestick reversal · 1h | buy | SOL-USD | 3.57 | — | entry signal |
| 2026-11-16T11:00 | Candlestick reversal · 1h | buy | ETH-USD | 3.57 | — | entry signal |
| 2026-11-16T11:00 | Candlestick reversal · 1h | buy | BTC-USD | 3.57 | — | entry signal |
| 2026-11-16T11:00 | VWAP momentum · 1h | buy | SOL-USD | 3.61 | — | entry signal |
| 2026-11-16T10:00 | MACD cross · 1h | sell | DOGE-USD | 17.71 | -0.23 | exit signal |
| 2026-11-16T09:40 | Candlestick reversal · 1h | sell | DOGE-USD | 3.71 | -0.10 | stop-loss |
| 2026-11-16T09:15 | Donchian 20/10 · 1h | sell | DOGE-USD | 16.69 | -0.57 | stop-loss |
| 2026-11-16T09:00 | Candlestick reversal · 1h | sell | ETH-USD | 3.33 | -0.05 | exit signal |
| 2026-11-16T09:00 | Candlestick reversal · 1h | sell | BTC-USD | 3.74 | -0.06 | exit signal |
| 2026-11-16T09:00 | MACD cross · 1h | buy | DOGE-USD | 7.70 | — | rebalance up |
| 2026-11-16T09:00 | MACD cross · 1h | sell | ETH-USD | 10.17 | -0.13 | exit signal |
| 2026-11-16T09:00 | MACD cross · 1h | sell | BTC-USD | 10.19 | -0.12 | exit signal |
| 2026-11-16T08:05 | Three white soldiers | sell | DOGE-USD | 14.25 | -0.15 | stop-loss |
| 2026-11-16T08:05 | Three white soldiers | sell | BTC-USD | 14.27 | -0.12 | exit signal |
| 2026-11-16T08:00 | CCI reversion · 1h | buy | SOL-USD | 3.69 | — | entry signal |
| 2026-11-16T08:00 | MACD cross · 1h | sell | SOL-USD | 10.25 | -0.05 | exit signal |
| 2026-11-16T07:45 | Three white soldiers | sell | SOL-USD | 14.24 | -0.16 | exit signal |
| 2026-11-16T07:35 | Three white soldiers | buy | SOL-USD | 14.39 | — | entry signal |
| 2026-11-16T07:35 | Three white soldiers | buy | DOGE-USD | 14.39 | — | entry signal |
| 2026-11-16T07:35 | Three white soldiers | buy | BTC-USD | 14.39 | — | entry signal |
| 2026-11-16T07:00 | Williams %R · 1h | buy | DOGE-USD | 3.89 | — | entry signal |
| 2026-11-16T07:00 | Parabolic SAR · 1h | sell | XRP-USD | 20.54 | -0.54 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 13:41:05.000131+00:00 -> 2026-11-16 13:51:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 13:41:05.000131+00:00 -> 2026-11-16 13:51:05.000131+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
