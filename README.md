# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T23:35:05.000115+00:00 · 63740 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.66 (-15.34%)

Closed trades 219, win rate 35.6%, fees £6.07, max drawdown -17.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-17)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 35.58 · VIX 26.05 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 6.1, AMZN 4.3, TSLA 2.4, META 1.9, AMD 1.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 43236 decisions in 3729 calls, $0.5371 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T23:35 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-17T23:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T23:35 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.55% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.72 | 16.72 | 0 | — | 14.89 | 5.20 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.86 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 16.87 | 3.44 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.31 | 3.31 | 0 | — | 5.76 | 1.61 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.24 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -3.01 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.37 | -3.63 | 8 | 50.0 | -3.91 | -0.12 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.48 | -4.52 | 0 | — | -3.89 | -1.28 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.05 | -5.95 | 198 | 30.3 | -4.51 | -1.60 | -9.44 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.31 | -8.29 | -5.89 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.28 | -7.72 | 0 | — | -8.38 | -2.22 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.73 | -9.27 | 153 | 46.4 | -11.66 | -3.43 | -18.48 | 148 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.41 | -9.59 | 0 | — | -8.30 | -2.26 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -11.40 | -5.52 | -13.38 | 60 |
| 20 | Copy: Insider buying | copy | 90.06 | -9.94 | 50 | 42.0 | -9.31 | -1.86 | -14.79 | 62 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.10 | -12.90 | 17 | 17.6 | -4.97 | -0.78 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -15.66 | -6.21 | -19.02 | 76 |
| 24 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.03 | -2.86 | -14.11 | 570 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.21 | -7.35 | -16.95 | 199 |
| 26 | Parabolic SAR · 1h | trend | 82.41 | -17.59 | 184 | 27.7 | -25.29 | -7.04 | -28.05 | 205 |
| 27 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 28 | Keltner breakout · 1h | breakout | 80.73 | -19.27 | 122 | 26.2 | -18.74 | -3.97 | -27.13 | 153 |
| 29 | Connors RSI(2) · 1h | reversion | 80.41 | -19.59 | 215 | 40.0 | -14.35 | -6.38 | -14.85 | 93 |
| 30 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.03 | -6.57 | -29.47 | 83 |
| 31 | Max aggression: 5-day momentum | meta | 79.71 | -20.29 | 21 | 42.9 | -48.12 | -3.22 | -55.24 | 22 |
| 32 | Volume breakout · 1h | breakout | 79.67 | -20.33 | 162 | 28.4 | -15.91 | -5.00 | -22.20 | 78 |
| 33 | Opening range 15m | breakout | 78.30 | -21.70 | 534 | 31.6 | -16.06 | -4.31 | -21.37 | 680 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.49 | -23.52 | 2 | 0.0 | -18.43 | -2.48 | -26.43 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 76.46 | -23.54 | 30 | 26.7 | -24.46 | -0.95 | -57.50 | 39 |
| 36 | Hold BTC | benchmark | 75.74 | -24.26 | 2 | 0.0 | -15.40 | -2.19 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -28.72 | -8.40 | -29.33 | 109 |
| 38 | ADX DI cross · 1h | trend | 75.01 | -24.99 | 208 | 19.2 | -26.51 | -4.23 | -35.42 | 263 |
| 39 | Bollinger breakout · 1h | breakout | 73.62 | -26.38 | 189 | 22.2 | -26.06 | -5.73 | -33.32 | 221 |
| 40 | Stochastic reversion · 1h | reversion | 73.24 | -26.76 | 345 | 42.6 | -34.28 | -5.22 | -36.02 | 424 |
| 41 | Supertrend · 1h | trend | 72.66 | -27.34 | 189 | 15.9 | -31.21 | -5.23 | -39.67 | 200 |
| 42 | Triple EMA stack · 1h | trend | 71.59 | -28.41 | 155 | 14.8 | -31.71 | -6.40 | -38.02 | 183 |
| 43 | RSI momentum · 1h | momentum | 71.48 | -28.52 | 176 | 14.2 | -30.78 | -5.59 | -37.58 | 197 |
| 44 | MFI reversion · 1h | reversion | 70.97 | -29.03 | 434 | 33.6 | -28.05 | -4.20 | -30.36 | 166 |
| 45 | MACD zero-line · 1h | trend | 70.59 | -29.41 | 181 | 17.7 | -27.08 | -5.41 | -33.36 | 203 |
| 46 | Heikin-Ashi · 1h | trend | 70.31 | -29.69 | 466 | 23.0 | -42.49 | -9.01 | -44.96 | 636 |
| 47 | EMA 20/50 cross · 1h | trend | 70.00 | -30.00 | 115 | 10.4 | -36.10 | -10.12 | -39.23 | 115 |
| 48 | ROC + volume · 1h | momentum | 69.69 | -30.31 | 408 | 28.2 | -30.32 | -4.96 | -39.54 | 355 |
| 49 | MACD cross · 1h | trend | 69.59 | -30.41 | 413 | 22.3 | -38.88 | -6.34 | -44.56 | 477 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.98 | -31.02 | 306 | 19.0 | -35.06 | -7.51 | -39.70 | 255 |
| 52 | Donchian 20/10 · 1h | breakout | 67.73 | -32.27 | 159 | 18.2 | -32.26 | -5.43 | -40.92 | 201 |
| 53 | CCI reversion · 1h | reversion | 67.13 | -32.87 | 382 | 41.6 | -40.97 | -6.75 | -44.29 | 471 |
| 54 | EMA 9/21 cross · 1h | trend | 64.08 | -35.92 | 280 | 11.1 | -39.86 | -7.53 | -47.20 | 324 |
| 55 | Bollinger reversion · 1h | reversion | 63.98 | -36.02 | 344 | 37.8 | -38.45 | -5.84 | -39.42 | 414 |
| 56 | Williams %R · 1h | reversion | 63.32 | -36.69 | 430 | 40.7 | -45.46 | -7.78 | -46.86 | 563 |
| 57 | Agent (ML meta-label) | meta | 60.11 | -39.89 | 1906 | 24.3 | -26.88 | -5.03 | -27.89 | 289 |
| 58 | RSI(14) reversion · 1h | reversion | 58.46 | -41.54 | 205 | 31.7 | -40.72 | -6.02 | -43.29 | 252 |
| 59 | Z-score reversion · 1h | reversion | 57.33 | -42.67 | 224 | 35.3 | -37.40 | -5.21 | -39.23 | 256 |
| 60 | VWAP momentum · 1h | momentum | 57.11 | -42.89 | 959 | 21.7 | -53.31 | -9.51 | -58.63 | 1195 |
| 61 | Candlestick reversal · 1h | reversion | 55.43 | -44.58 | 546 | 26.6 | -46.95 | -8.59 | -48.43 | 643 |
| 62 | Three white soldiers | momentum | 55.07 | -44.93 | 585 | 14.5 | -49.78 | -21.82 | -50.37 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.57 | -99.03 | 5270 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.45 | -25.47 | -82.11 | 1404 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.92 | -41.69 | -94.02 | 2473 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.08 | -32.07 | -90.33 | 1939 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -40.32 | -91.49 | 2296 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.69 | -31.05 | -89.79 | 2111 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -48.27 | -97.94 | 3487 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -54.24 | -96.50 | 3397 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.42 | -38.38 | -93.53 | 2232 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.99 | -33.62 | -83.08 | 1606 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.67 | -99.60 | 6078 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.09 | -42.42 | -92.17 | 2565 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.86 | -39.07 | -94.87 | 3289 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.43 | -99.81 | 6191 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.47 | -43.88 | -92.48 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.55 | -26.08 | -76.68 | 1643 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -61.41 | -97.67 | 3434 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -56.52 | -99.01 | 4952 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.61 | -27.69 | -68.90 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -57.04 | -94.66 | 2747 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.62 | -38.05 | -84.65 | 1724 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -69.43 | -99.69 | 6376 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.75 | -31.09 | -90.90 | 2359 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.42 | -18.61 | -79.91 | 1832 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.28 | -36.59 | -91.36 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.50 | -45.77 | -97.53 | 3903 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -59.68 | -89.42 | 2163 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.44 | -30.15 | -66.44 | 815 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.62 | -23.08 | -72.62 | 1227 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.39 | -17.82 | -80.65 | 1717 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.53 | -46.40 | -97.58 | 4339 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -115.57 | -99.94 | 8464 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T23:00 | MACD zero-line · 1h | buy | DOGE-USD | 17.63 | — | entry signal |
| 2026-11-17T23:00 | Triple EMA stack · 1h | buy | XRP-USD | 17.80 | — | entry signal |
| 2026-11-17T22:00 | OBV trend · 1h | buy | XRP-USD | 17.10 | — | entry signal |
| 2026-11-17T22:00 | ROC + volume · 1h | buy | XRP-USD | 17.31 | — | entry signal |
| 2026-11-17T22:00 | Heikin-Ashi · 1h | buy | XRP-USD | 17.40 | — | entry signal |
| 2026-11-17T22:00 | Heikin-Ashi · 1h | buy | SOL-USD | 17.40 | — | entry signal |
| 2026-11-17T22:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 17.40 | — | entry signal |
| 2026-11-17T22:00 | Parabolic SAR · 1h | buy | XRP-USD | 20.39 | — | entry signal |
| 2026-11-17T22:00 | Parabolic SAR · 1h | buy | SOL-USD | 20.39 | — | entry signal |
| 2026-11-17T22:00 | Parabolic SAR · 1h | buy | DOGE-USD | 20.39 | — | entry signal |
| 2026-11-17T22:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 17.44 | — | entry signal |
| 2026-11-17T22:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 15.83 | — | entry signal |
| 2026-11-17T21:06 | MFI reversion · 1h | sell | BTC-USD | 3.92 | -0.05 | rebalance down |
| 2026-11-17T21:00 | ROC + volume · 1h | buy | DOGE-USD | 17.33 | — | entry signal |
| 2026-11-17T21:00 | MACD cross · 1h | buy | DOGE-USD | 3.00 | — | entry signal |
| 2026-11-17T20:55 | Agent (rotation) | sell | SQQQ | 31.47 | 0.17 | selected signal exited |
| 2026-11-17T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 98.59 | 0.15 | target is flat |
| 2026-11-17T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 111.39 | 0.61 | target is flat |
| 2026-11-17T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 91.65 | -0.23 | target is flat |
| 2026-11-17T20:55 | Agent (ML meta-label) | buy | TQQQ | 14.96 | — | entry |
| 2026-11-17T20:55 | Agent (ML meta-label) | sell | MSTR | 14.92 | -0.06 | selected signal exited |
| 2026-11-17T20:55 | Agent (ML meta-label) | sell | AMD | 14.94 | -0.04 | selected signal exited |
| 2026-11-17T20:55 | Agent | sell | SOXL | 17.04 | 0.10 | selected signal exited |
| 2026-11-17T20:55 | MFI reversion · 1h | buy | UPRO | 5.04 | — | entry |
| 2026-11-17T20:55 | MFI reversion · 1h | buy | TSLA | 10.08 | — | entry |
| 2026-11-17T20:55 | MFI reversion · 1h | sell | MSFT | 11.78 | -0.01 | target is flat |
| 2026-11-17T20:55 | Opening range 30m | sell | SQQQ | 21.97 | 0.45 | end-of-day flatten |
| 2026-11-17T20:55 | Opening range 15m | sell | SQQQ | 19.93 | 0.41 | end-of-day flatten |
| 2026-11-17T20:50 | Agent (ML meta-label) | buy | MSTR | 14.99 | — | entry |
| 2026-11-17T20:50 | Agent (ML meta-label) | buy | AMD | 14.99 | — | entry |
| 2026-11-17T20:50 | MFI reversion · 1h | buy | MSFT | 4.77 | — | rebalance up |
| 2026-11-17T20:50 | MFI reversion · 1h | sell | LABU | 8.11 | 0.08 | target is flat |
| 2026-11-17T20:50 | Three white soldiers | sell | NVDA | 13.75 | -0.02 | exit signal |
| 2026-11-17T20:45 | Agent (ML meta-label) | sell | TQQQ | 14.93 | -0.02 | selected signal exited |
| 2026-11-17T20:45 | Agent (ML meta-label) | sell | SQQQ | 11.99 | -0.00 | selected signal exited |
| 2026-11-17T20:45 | Agent (ML meta-label) | sell | MSTR | 14.98 | -0.03 | selected signal exited |
| 2026-11-17T20:45 | Agent (ML meta-label) | sell | AMD | 6.06 | -0.00 | selected signal exited |
| 2026-11-17T20:45 | Agent (aggressive) | sell | COIN | 40.80 | -0.18 | selected signal exited |
| 2026-11-17T20:45 | Agent | sell | COIN | 16.85 | -0.07 | selected signal exited |
| 2026-11-17T20:45 | VWAP momentum · 1h | buy | BITX | 6.31 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 23:35:05.000115+00:00 -> 2026-11-17 23:45:05.000115+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 23:35:05.000115+00:00 -> 2026-11-17 23:45:05.000115+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
