# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T11:10:05.000128+00:00 · 61840 ticks

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

Today: 9090 decisions in 1818 calls, $0.1273 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T11:10 | 0 / 5 / 0 | cash |  |
| Breezy | 2026-11-16T11:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-16T11:10 | 3 / 2 / 0 | ETH-USD 66% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.06 | 18.06 | 0 | — | 15.31 | 5.02 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 2.90 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.96 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.78 | 4.78 | 0 | — | 6.58 | 1.79 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 0.99 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 3.16 | 1.99 | -3.39 | 82 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.72 | 1.87 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.47 | 0.22 | -18.69 | 7 |
| 11 | Hold SPY | benchmark | 98.47 | -1.53 | 0 | — | -0.61 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.02 | -2.98 | 1 | 0.0 | -3.27 | -2.13 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.78 | -3.22 | 191 | 30.4 | -2.59 | -0.87 | -8.42 | 160 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.49 | -3.51 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.38 | -5.62 | 43 | 39.5 | -7.13 | -1.42 | -14.95 | 58 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.83 | -6.17 | 0 | — | -4.81 | -1.26 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.95 | -8.05 | 110 | 22.7 | -12.74 | -5.62 | -14.95 | 64 |
| 20 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -3.98 | -0.86 | -16.02 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.26 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.61 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.78 | -14.22 | 16 | 18.8 | -10.26 | -1.97 | -19.56 | 19 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.17 | -7.05 | -15.01 | 193 |
| 26 | Parabolic SAR · 1h | trend | 84.82 | -15.18 | 177 | 28.8 | -15.59 | -3.34 | -22.83 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -14.83 | -4.08 | -16.59 | 92 |
| 28 | Donchian 55/20 · 1h | breakout | 82.08 | -17.92 | 73 | 13.7 | -23.08 | -4.78 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.97 | -19.03 | 2 | 0.0 | -9.89 | -1.38 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.67 | -19.34 | 212 | 40.1 | -14.02 | -5.90 | -14.56 | 104 |
| 31 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -16.96 | -3.38 | -25.39 | 165 |
| 32 | Volume breakout · 1h | breakout | 79.96 | -20.04 | 161 | 28.6 | -14.06 | -3.20 | -22.55 | 90 |
| 33 | Stochastic reversion · 1h | reversion | 78.96 | -21.04 | 314 | 46.5 | -24.23 | -3.55 | -28.40 | 405 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.88 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 77.10 | -22.90 | 407 | 35.1 | -18.59 | -2.39 | -26.89 | 163 |
| 36 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.57 | -50.62 | 22 |
| 37 | Hold BTC | benchmark | 75.56 | -24.44 | 2 | 0.0 | -16.26 | -2.29 | -28.91 | 1 |
| 38 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -29.98 | -8.25 | -31.49 | 115 |
| 39 | Max aggression: 1-day momentum | meta | 75.00 | -25.00 | 29 | 27.6 | -21.85 | -0.73 | -57.50 | 40 |
| 40 | Bollinger breakout · 1h | breakout | 74.59 | -25.41 | 184 | 22.3 | -23.16 | -4.79 | -31.20 | 235 |
| 41 | ADX DI cross · 1h | trend | 74.53 | -25.47 | 206 | 19.4 | -25.44 | -3.80 | -34.43 | 272 |
| 42 | Heikin-Ashi · 1h | trend | 74.12 | -25.88 | 452 | 23.7 | -38.05 | -6.98 | -40.73 | 669 |
| 43 | MACD zero-line · 1h | trend | 72.99 | -27.01 | 172 | 18.6 | -23.66 | -4.60 | -31.23 | 200 |
| 44 | RSI momentum · 1h | momentum | 72.71 | -27.29 | 171 | 14.0 | -28.03 | -4.50 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.64 | -27.36 | 109 | 10.1 | -31.87 | -7.24 | -39.46 | 117 |
| 46 | Supertrend · 1h | trend | 71.71 | -28.29 | 182 | 14.8 | -31.83 | -5.78 | -37.62 | 206 |
| 47 | Triple EMA stack · 1h | trend | 71.70 | -28.30 | 151 | 14.6 | -27.48 | -4.48 | -38.66 | 201 |
| 48 | MACD cross · 1h | trend | 71.41 | -28.59 | 398 | 22.9 | -32.38 | -4.80 | -41.23 | 474 |
| 49 | Bollinger reversion · 1h | reversion | 70.93 | -29.07 | 313 | 40.9 | -31.92 | -4.97 | -33.59 | 393 |
| 50 | CCI reversion · 1h | reversion | 70.22 | -29.78 | 359 | 42.6 | -35.06 | -5.51 | -39.14 | 471 |
| 51 | ROC + volume · 1h | momentum | 70.10 | -29.90 | 402 | 28.6 | -31.02 | -5.57 | -37.90 | 364 |
| 52 | OBV trend · 1h | momentum | 69.76 | -30.24 | 299 | 19.1 | -28.46 | -4.91 | -38.28 | 270 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.10 | -4.60 | -37.81 | 35 |
| 54 | Donchian 20/10 · 1h | breakout | 68.74 | -31.26 | 154 | 18.8 | -30.52 | -5.43 | -37.95 | 205 |
| 55 | Williams %R · 1h | reversion | 66.16 | -33.84 | 404 | 42.3 | -41.27 | -6.91 | -42.52 | 550 |
| 56 | Agent (ML meta-label) | meta | 65.17 | -34.83 | 1855 | 24.7 | -20.31 | -3.33 | -24.82 | 323 |
| 57 | EMA 9/21 cross · 1h | trend | 64.79 | -35.21 | 267 | 11.6 | -37.87 | -7.60 | -43.65 | 329 |
| 58 | VWAP momentum · 1h | momentum | 62.59 | -37.41 | 918 | 22.2 | -51.90 | -10.10 | -53.45 | 1235 |
| 59 | RSI(14) reversion · 1h | reversion | 61.57 | -38.43 | 199 | 32.2 | -37.39 | -5.42 | -40.40 | 241 |
| 60 | Candlestick reversal · 1h | reversion | 60.75 | -39.25 | 514 | 27.6 | -42.84 | -7.97 | -43.25 | 616 |
| 61 | Z-score reversion · 1h | reversion | 60.68 | -39.32 | 216 | 35.6 | -33.86 | -4.65 | -35.69 | 238 |
| 62 | Three white soldiers | momentum | 57.15 | -42.85 | 562 | 14.8 | -49.78 | -22.15 | -49.78 | 668 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -42.06 | -99.01 | 5330 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.92 | -26.33 | -81.09 | 1428 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.84 | -44.68 | -93.85 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.03 | -33.59 | -90.06 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.55 | -42.81 | -91.56 | 2359 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.89 | -30.64 | -89.91 | 2189 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -50.38 | -97.90 | 3502 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.45 | -56.45 | -96.45 | 3481 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.51 | -34.68 | -93.51 | 2304 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.07 | -33.52 | -83.07 | 1653 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -55.09 | -99.60 | 6074 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.18 | -43.19 | -92.25 | 2630 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.20 | -35.34 | -95.20 | 3450 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.74 | -99.82 | 6179 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.46 | -43.63 | -92.50 | 2296 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.40 | -26.22 | -76.65 | 1683 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -57.33 | -97.63 | 3502 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -56.83 | -98.99 | 4968 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.06 | -27.16 | -69.27 | 1246 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -55.72 | -94.74 | 2806 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.68 | -36.97 | -84.75 | 1777 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -68.73 | -99.69 | 6395 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.72 | -30.51 | -90.75 | 2346 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.83 | -18.67 | -80.52 | 1819 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.04 | -35.58 | -91.07 | 2194 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.42 | -44.32 | -97.42 | 3922 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.16 | -59.05 | -89.19 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.61 | -29.68 | -66.73 | 833 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.03 | -22.88 | -72.06 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.37 | -17.43 | -80.96 | 1754 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.54 | -45.52 | -97.56 | 4358 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.75 | -99.94 | 8465 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-16T02:55 | Three white soldiers | sell | SOL-USD | 14.35 | -0.08 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 11:10:05.000128+00:00 -> 2026-11-16 11:20:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 11:10:05.000128+00:00 -> 2026-11-16 11:20:05.000128+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
