# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T09:40:05.000142+00:00 · 61759 ticks

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

Today: 7875 decisions in 1575 calls, $0.1103 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T09:40 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-16T09:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-16T09:40 | 1 / 4 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.81 | 17.81 | 0 | — | 15.31 | 5.02 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 2.90 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.96 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.56 | 4.56 | 0 | — | 6.58 | 1.79 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 0.99 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 3.16 | 1.99 | -3.39 | 82 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.72 | 1.87 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.47 | 0.22 | -18.69 | 7 |
| 11 | Hold SPY | benchmark | 98.25 | -1.75 | 0 | — | -0.61 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.81 | -3.19 | 1 | 0.0 | -3.27 | -2.13 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.65 | -3.35 | 191 | 30.4 | -2.50 | -0.84 | -8.33 | 153 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.28 | -3.72 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.18 | -5.82 | 43 | 39.5 | -7.13 | -1.42 | -14.95 | 58 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.63 | -6.37 | 0 | — | -4.81 | -1.26 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.79 | -8.21 | 110 | 22.7 | -12.74 | -5.62 | -14.95 | 64 |
| 20 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.70 | -3.42 | -18.48 | 149 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -3.68 | -0.77 | -16.02 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.26 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.61 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.64 | -14.36 | 16 | 18.8 | -10.26 | -1.97 | -19.56 | 19 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.17 | -7.05 | -15.01 | 193 |
| 26 | Parabolic SAR · 1h | trend | 84.68 | -15.32 | 177 | 28.8 | -15.59 | -3.34 | -22.83 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -14.83 | -4.08 | -16.59 | 92 |
| 28 | Donchian 55/20 · 1h | breakout | 81.95 | -18.05 | 73 | 13.7 | -23.08 | -4.78 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.79 | -19.21 | 2 | 0.0 | -9.89 | -1.38 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.62 | -19.38 | 212 | 40.1 | -14.26 | -6.02 | -14.56 | 105 |
| 31 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -16.96 | -3.38 | -25.39 | 165 |
| 32 | Volume breakout · 1h | breakout | 79.96 | -20.04 | 161 | 28.6 | -14.06 | -3.20 | -22.55 | 90 |
| 33 | Stochastic reversion · 1h | reversion | 78.80 | -21.20 | 314 | 46.5 | -24.57 | -3.61 | -28.40 | 405 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.88 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 76.88 | -23.12 | 407 | 35.1 | -18.76 | -2.42 | -26.89 | 163 |
| 36 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.57 | -50.62 | 22 |
| 37 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -29.98 | -8.25 | -31.49 | 115 |
| 38 | Hold BTC | benchmark | 74.96 | -25.04 | 2 | 0.0 | -16.88 | -2.39 | -28.91 | 1 |
| 39 | Max aggression: 1-day momentum | meta | 74.84 | -25.16 | 29 | 27.6 | -21.85 | -0.73 | -57.50 | 40 |
| 40 | Bollinger breakout · 1h | breakout | 74.59 | -25.41 | 184 | 22.3 | -23.16 | -4.79 | -31.20 | 235 |
| 41 | ADX DI cross · 1h | trend | 74.53 | -25.47 | 206 | 19.4 | -25.51 | -3.81 | -34.43 | 272 |
| 42 | Heikin-Ashi · 1h | trend | 73.98 | -26.02 | 452 | 23.7 | -38.05 | -6.98 | -40.73 | 669 |
| 43 | MACD zero-line · 1h | trend | 72.95 | -27.05 | 172 | 18.6 | -23.66 | -4.60 | -31.23 | 200 |
| 44 | RSI momentum · 1h | momentum | 72.55 | -27.45 | 171 | 14.0 | -27.88 | -4.44 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.49 | -27.51 | 109 | 10.1 | -28.97 | -5.05 | -40.75 | 119 |
| 46 | Triple EMA stack · 1h | trend | 71.59 | -28.41 | 151 | 14.6 | -27.51 | -4.47 | -38.66 | 201 |
| 47 | MACD cross · 1h | trend | 71.41 | -28.59 | 397 | 22.9 | -32.33 | -4.79 | -41.23 | 474 |
| 48 | Supertrend · 1h | trend | 71.35 | -28.65 | 182 | 14.8 | -31.70 | -5.68 | -37.62 | 207 |
| 49 | Bollinger reversion · 1h | reversion | 70.81 | -29.19 | 313 | 40.9 | -31.90 | -4.96 | -33.59 | 391 |
| 50 | ROC + volume · 1h | momentum | 70.02 | -29.98 | 402 | 28.6 | -31.02 | -5.57 | -37.90 | 364 |
| 51 | CCI reversion · 1h | reversion | 69.98 | -30.02 | 359 | 42.6 | -35.50 | -5.61 | -39.14 | 470 |
| 52 | OBV trend · 1h | momentum | 69.64 | -30.36 | 299 | 19.1 | -28.15 | -4.84 | -38.28 | 270 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.10 | -4.60 | -37.81 | 35 |
| 54 | Donchian 20/10 · 1h | breakout | 68.63 | -31.37 | 154 | 18.8 | -30.52 | -5.43 | -37.95 | 205 |
| 55 | Williams %R · 1h | reversion | 65.98 | -34.02 | 404 | 42.3 | -41.46 | -6.95 | -42.52 | 547 |
| 56 | Agent (ML meta-label) | meta | 65.03 | -34.98 | 1855 | 24.7 | -17.04 | -3.28 | -21.53 | 329 |
| 57 | EMA 9/21 cross · 1h | trend | 64.65 | -35.35 | 267 | 11.6 | -37.87 | -7.60 | -43.65 | 329 |
| 58 | VWAP momentum · 1h | momentum | 62.47 | -37.53 | 918 | 22.2 | -51.90 | -10.10 | -53.45 | 1234 |
| 59 | RSI(14) reversion · 1h | reversion | 61.28 | -38.72 | 199 | 32.2 | -37.96 | -5.53 | -40.40 | 243 |
| 60 | Candlestick reversal · 1h | reversion | 60.66 | -39.34 | 514 | 27.6 | -43.69 | -8.19 | -43.69 | 614 |
| 61 | Z-score reversion · 1h | reversion | 60.15 | -39.85 | 216 | 35.6 | -34.42 | -4.74 | -35.69 | 238 |
| 62 | Three white soldiers | momentum | 57.15 | -42.85 | 562 | 14.8 | -49.73 | -22.13 | -49.80 | 670 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -42.33 | -99.02 | 5334 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.07 | -26.59 | -81.22 | 1428 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.84 | -44.64 | -93.84 | 2536 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.13 | -33.63 | -90.13 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.56 | -42.82 | -91.56 | 2355 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.88 | -30.63 | -89.91 | 2189 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -50.74 | -97.92 | 3500 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.45 | -56.55 | -96.45 | 3480 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.64 | -34.15 | -93.64 | 2319 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.07 | -33.52 | -83.07 | 1653 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.96 | -99.60 | 6067 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.19 | -43.28 | -92.24 | 2627 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.20 | -35.34 | -95.20 | 3450 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.43 | -99.82 | 6176 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.52 | -43.81 | -92.53 | 2295 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.42 | -26.26 | -76.61 | 1681 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -57.33 | -97.63 | 3502 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -56.93 | -98.99 | 4971 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.09 | -27.22 | -69.25 | 1245 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -55.83 | -94.72 | 2801 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.66 | -36.86 | -84.73 | 1774 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -69.10 | -99.69 | 6400 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.80 | -30.69 | -90.80 | 2354 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.64 | -18.70 | -80.29 | 1814 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.03 | -35.61 | -91.05 | 2192 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.42 | -44.46 | -97.43 | 3925 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.20 | -59.10 | -89.20 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.61 | -29.68 | -66.73 | 833 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.02 | -22.87 | -72.04 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.56 | -17.61 | -80.97 | 1755 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -45.71 | -97.57 | 4362 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.11 | -99.94 | 8466 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 09:40:05.000142+00:00 -> 2026-11-16 09:50:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 09:40:05.000142+00:00 -> 2026-11-16 09:50:05.000142+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
