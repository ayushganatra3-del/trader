# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T02:41:05.000128+00:00 · 61383 ticks

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

Today: 2235 decisions in 447 calls, $0.0313 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T02:41 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-16T02:41 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-16T02:41 | 3 / 2 / 0 | ETH-USD 67% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.84 | 17.84 | 0 | — | 15.31 | 5.02 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 2.90 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.96 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.58 | 4.58 | 0 | — | 6.58 | 1.79 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 0.99 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 3.07 | 1.93 | -3.47 | 82 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.59 | 1.84 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.47 | 0.22 | -18.69 | 7 |
| 11 | Hold SPY | benchmark | 98.28 | -1.72 | 0 | — | -0.61 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.84 | -3.16 | 1 | 0.0 | -3.27 | -2.13 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.66 | -3.34 | 191 | 30.4 | -2.58 | -0.87 | -8.50 | 150 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.31 | -3.69 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.20 | -5.80 | 43 | 39.5 | -6.35 | -1.21 | -15.78 | 58 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.65 | -6.35 | 0 | — | -4.81 | -1.26 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.81 | -8.19 | 110 | 22.7 | -13.63 | -5.99 | -14.95 | 65 |
| 20 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -14.74 | -4.08 | -18.48 | 156 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -3.68 | -0.77 | -16.02 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.26 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.61 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.66 | -14.34 | 16 | 18.8 | -10.26 | -1.97 | -19.56 | 19 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.17 | -7.05 | -15.01 | 193 |
| 26 | Parabolic SAR · 1h | trend | 85.07 | -14.93 | 176 | 29.0 | -15.29 | -3.27 | -22.69 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -14.83 | -4.08 | -16.59 | 92 |
| 28 | Donchian 55/20 · 1h | breakout | 81.96 | -18.04 | 73 | 13.7 | -23.08 | -4.78 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.81 | -19.19 | 2 | 0.0 | -9.89 | -1.38 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.63 | -19.37 | 212 | 40.1 | -18.02 | -6.23 | -18.10 | 111 |
| 31 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -16.96 | -3.38 | -25.39 | 165 |
| 32 | Volume breakout · 1h | breakout | 79.96 | -20.04 | 161 | 28.6 | -14.06 | -3.20 | -22.55 | 90 |
| 33 | Stochastic reversion · 1h | reversion | 78.82 | -21.18 | 314 | 46.5 | -24.58 | -3.61 | -28.40 | 406 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.88 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 77.04 | -22.95 | 407 | 35.1 | -18.84 | -2.42 | -26.60 | 168 |
| 36 | Hold BTC | benchmark | 76.22 | -23.78 | 2 | 0.0 | -16.33 | -2.28 | -28.91 | 1 |
| 37 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.57 | -50.62 | 22 |
| 38 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.69 | -31.41 | 114 |
| 39 | Max aggression: 1-day momentum | meta | 74.86 | -25.14 | 29 | 27.6 | -21.85 | -0.73 | -57.50 | 40 |
| 40 | Bollinger breakout · 1h | breakout | 74.59 | -25.41 | 184 | 22.3 | -23.16 | -4.79 | -31.20 | 235 |
| 41 | ADX DI cross · 1h | trend | 74.53 | -25.47 | 206 | 19.4 | -25.09 | -3.74 | -34.43 | 271 |
| 42 | Heikin-Ashi · 1h | trend | 74.00 | -26.00 | 452 | 23.7 | -38.05 | -6.98 | -40.73 | 669 |
| 43 | MACD zero-line · 1h | trend | 73.32 | -26.68 | 171 | 18.7 | -23.45 | -4.56 | -31.10 | 200 |
| 44 | RSI momentum · 1h | momentum | 72.57 | -27.43 | 171 | 14.0 | -26.93 | -4.13 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.50 | -27.50 | 109 | 10.1 | -28.22 | -4.71 | -40.51 | 120 |
| 46 | MACD cross · 1h | trend | 72.38 | -27.62 | 393 | 23.2 | -31.21 | -4.57 | -41.23 | 473 |
| 47 | Supertrend · 1h | trend | 71.80 | -28.20 | 182 | 14.8 | -29.43 | -4.95 | -37.38 | 211 |
| 48 | Triple EMA stack · 1h | trend | 71.61 | -28.39 | 151 | 14.6 | -27.09 | -4.41 | -38.66 | 201 |
| 49 | Bollinger reversion · 1h | reversion | 70.82 | -29.18 | 313 | 40.9 | -32.84 | -5.17 | -34.21 | 393 |
| 50 | ROC + volume · 1h | momentum | 70.35 | -29.65 | 401 | 28.7 | -30.49 | -5.45 | -37.90 | 363 |
| 51 | CCI reversion · 1h | reversion | 70.16 | -29.84 | 359 | 42.6 | -35.50 | -5.61 | -39.14 | 471 |
| 52 | OBV trend · 1h | momentum | 69.66 | -30.34 | 299 | 19.1 | -28.53 | -4.91 | -38.36 | 271 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.10 | -4.60 | -37.81 | 35 |
| 54 | Donchian 20/10 · 1h | breakout | 69.03 | -30.97 | 153 | 19.0 | -30.10 | -5.34 | -37.82 | 205 |
| 55 | Williams %R · 1h | reversion | 66.12 | -33.88 | 404 | 42.3 | -41.98 | -7.08 | -42.64 | 546 |
| 56 | Agent (ML meta-label) | meta | 65.04 | -34.96 | 1855 | 24.7 | -22.29 | -5.09 | -26.56 | 334 |
| 57 | EMA 9/21 cross · 1h | trend | 64.67 | -35.33 | 267 | 11.6 | -37.34 | -7.47 | -43.48 | 328 |
| 58 | VWAP momentum · 1h | momentum | 62.48 | -37.52 | 918 | 22.2 | -52.05 | -10.17 | -53.34 | 1237 |
| 59 | RSI(14) reversion · 1h | reversion | 61.74 | -38.26 | 199 | 32.2 | -39.16 | -5.74 | -40.46 | 250 |
| 60 | Z-score reversion · 1h | reversion | 61.01 | -38.99 | 216 | 35.6 | -33.31 | -4.55 | -35.69 | 238 |
| 61 | Candlestick reversal · 1h | reversion | 60.88 | -39.12 | 511 | 27.8 | -43.47 | -8.13 | -43.84 | 614 |
| 62 | Three white soldiers | momentum | 57.82 | -42.18 | 557 | 14.9 | -49.31 | -21.49 | -49.47 | 669 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -40.68 | -98.99 | 5313 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.11 | -26.65 | -81.11 | 1432 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -43.84 | -93.77 | 2533 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.99 | -32.23 | -90.03 | 1945 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.55 | -41.32 | -91.58 | 2362 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.58 | -29.96 | -89.61 | 2176 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.85 | -48.79 | -97.88 | 3499 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -54.43 | -96.35 | 3468 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -31.71 | -93.55 | 2316 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.06 | -33.40 | -83.08 | 1656 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -52.78 | -99.60 | 6065 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.11 | -41.40 | -92.19 | 2629 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.20 | -35.35 | -95.20 | 3450 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -65.96 | -99.81 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.41 | -42.03 | -92.45 | 2296 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.25 | -25.96 | -76.52 | 1680 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.58 | -55.80 | -97.60 | 3500 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -55.03 | -98.99 | 4967 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.07 | -26.87 | -69.25 | 1246 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -53.41 | -94.71 | 2804 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.76 | -36.91 | -84.84 | 1777 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -64.84 | -99.70 | 6402 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.86 | -30.17 | -90.93 | 2355 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.17 | -18.62 | -80.86 | 1828 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.09 | -34.70 | -91.15 | 2197 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.43 | -44.17 | -97.43 | 3923 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -53.81 | -89.30 | 2173 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.49 | -29.39 | -66.67 | 834 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.29 | -23.18 | -72.31 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.35 | -17.60 | -81.88 | 1774 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.43 | -97.59 | 4364 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -89.39 | -99.93 | 8461 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-16T00:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 17.26 | — | entry signal |
| 2026-11-16T00:00 | ROC + volume · 1h | buy | SOL-USD | 17.80 | — | entry signal |
| 2026-11-16T00:00 | ROC + volume · 1h | buy | DOGE-USD | 17.80 | — | entry signal |
| 2026-11-16T00:00 | ADX DI cross · 1h | buy | SOL-USD | 15.10 | — | entry signal |
| 2026-11-16T00:00 | ADX DI cross · 1h | buy | DOGE-USD | 15.10 | — | entry signal |
| 2026-11-16T00:00 | ADX DI cross · 1h | buy | BTC-USD | 15.10 | — | entry signal |
| 2026-11-16T00:00 | Parabolic SAR · 1h | buy | XRP-USD | 21.08 | — | entry signal |
| 2026-11-16T00:00 | Supertrend · 1h | buy | DOGE-USD | 3.77 | — | entry signal |
| 2026-11-16T00:00 | Supertrend · 1h | sell | XRP-USD | 3.77 | 0.00 | rebalance down |
| 2026-11-16T00:00 | MACD zero-line · 1h | buy | XRP-USD | 18.37 | — | entry signal |
| 2026-11-15T23:15 | Three white soldiers | sell | XRP-USD | 14.30 | -0.18 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 02:41:05.000128+00:00 -> 2026-11-16 02:51:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
