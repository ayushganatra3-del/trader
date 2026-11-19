# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T01:25:05.000129+00:00 · 65054 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.17 (-14.83%)

Closed trades 225, win rate 36.4%, fees £6.17, max drawdown -17.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-18 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, LRN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-18)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 33.12 · VIX 24.56 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 6.2, AMZN 6.2, TSLA 4.1, AMD 3.9, META 1.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 1140 decisions in 228 calls, $0.0160 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T01:25 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-11-19T01:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-19T01:25 | 1 / 4 / 0 | ETH-USD 53% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.99% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| Connors RSI(2) | SQQQ | 1.81 | +3.66% | 10 |
| Squeeze breakout | SQQQ | 1.74 | +6.13% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.67 | 14.67 | 0 | — | 13.21 | 4.35 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 2.97 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.79 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.90 | 3.90 | 0 | — | 4.56 | 1.31 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 152 | 35.5 | -3.30 | -2.87 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.34 | 1.13 | -9.06 | 207 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.47 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.97 | -4.03 | 8 | 50.0 | -4.05 | -0.14 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.64 | -4.36 | 0 | — | -3.89 | -1.26 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.26 | -1.49 | -8.79 | 153 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.28 | -5.13 | 19 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.91 | -7.09 | 0 | — | -6.94 | -1.81 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.83 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.31 | -8.69 | 0 | — | -7.46 | -1.99 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.20 | -9.80 | 114 | 23.7 | -15.28 | -7.39 | -15.58 | 61 |
| 19 | Copy: Insider buying | copy | 90.07 | -9.93 | 52 | 40.4 | -10.48 | -2.10 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.64 | -18.48 | 149 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.05 | -12.95 | 17 | 17.6 | -7.35 | -1.37 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.08 | -9.08 | -18.13 | 72 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.17 | -6.52 | -16.41 | 204 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -11.99 | -4.02 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.84 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.66 | -18.34 | 188 | 28.2 | -24.13 | -6.60 | -27.22 | 197 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.19 | -6.25 | -14.68 | 84 |
| 29 | Keltner breakout · 1h | breakout | 79.89 | -20.11 | 124 | 25.8 | -23.21 | -6.32 | -25.90 | 148 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.23 | -5.21 | -21.31 | 74 |
| 31 | Max aggression: 5-day momentum | meta | 79.17 | -20.83 | 21 | 42.9 | -47.98 | -3.18 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.73 | -30.74 | 84 |
| 33 | Opening range 15m | breakout | 77.70 | -22.30 | 541 | 32.0 | -19.89 | -5.87 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.97 | -23.03 | 2 | 0.0 | -18.99 | -2.56 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.56 | -24.44 | 209 | 19.1 | -26.24 | -4.22 | -34.88 | 266 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.46 | -30.36 | 110 |
| 37 | Hold BTC | benchmark | 73.66 | -26.34 | 2 | 0.0 | -18.58 | -2.74 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.69 | -8.26 | -33.72 | 216 |
| 39 | Stochastic reversion · 1h | reversion | 72.84 | -27.16 | 351 | 42.5 | -34.66 | -5.23 | -35.78 | 425 |
| 40 | Max aggression: 1-day momentum | meta | 71.77 | -28.23 | 32 | 28.1 | -38.62 | -2.32 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.50 | -28.50 | 192 | 16.7 | -32.69 | -5.38 | -39.71 | 200 |
| 42 | Triple EMA stack · 1h | trend | 70.72 | -29.27 | 157 | 14.6 | -30.75 | -6.18 | -37.72 | 172 |
| 43 | MFI reversion · 1h | reversion | 70.52 | -29.48 | 452 | 33.4 | -29.35 | -4.39 | -31.00 | 171 |
| 44 | RSI momentum · 1h | momentum | 70.36 | -29.64 | 179 | 14.5 | -31.46 | -5.66 | -38.37 | 198 |
| 45 | Heikin-Ashi · 1h | trend | 69.92 | -30.09 | 474 | 23.0 | -44.09 | -9.55 | -45.85 | 629 |
| 46 | MACD zero-line · 1h | trend | 69.84 | -30.16 | 184 | 17.9 | -28.09 | -5.56 | -34.29 | 203 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.89 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.18 | -30.82 | 116 | 10.3 | -36.91 | -9.31 | -40.97 | 118 |
| 49 | ROC + volume · 1h | momentum | 69.02 | -30.98 | 413 | 28.1 | -33.79 | -6.12 | -39.51 | 337 |
| 50 | OBV trend · 1h | momentum | 68.24 | -31.76 | 310 | 19.4 | -33.95 | -7.08 | -39.87 | 247 |
| 51 | MACD cross · 1h | trend | 67.71 | -32.30 | 417 | 22.3 | -41.13 | -6.67 | -46.93 | 491 |
| 52 | CCI reversion · 1h | reversion | 67.12 | -32.88 | 387 | 41.6 | -42.31 | -7.05 | -44.29 | 476 |
| 53 | Donchian 20/10 · 1h | breakout | 66.54 | -33.46 | 162 | 17.9 | -35.30 | -6.73 | -41.19 | 190 |
| 54 | Bollinger reversion · 1h | reversion | 63.82 | -36.18 | 349 | 38.1 | -38.88 | -5.88 | -39.66 | 417 |
| 55 | Williams %R · 1h | reversion | 63.61 | -36.39 | 437 | 40.7 | -46.64 | -8.06 | -47.34 | 566 |
| 56 | EMA 9/21 cross · 1h | trend | 62.82 | -37.17 | 285 | 11.6 | -39.64 | -7.70 | -45.71 | 321 |
| 57 | Agent (ML meta-label) | meta | 60.13 | -39.87 | 1949 | 24.6 | -30.83 | -5.95 | -31.85 | 302 |
| 58 | RSI(14) reversion · 1h | reversion | 58.88 | -41.12 | 206 | 32.0 | -40.91 | -6.00 | -43.22 | 255 |
| 59 | Z-score reversion · 1h | reversion | 57.45 | -42.55 | 227 | 35.2 | -36.92 | -5.06 | -39.53 | 259 |
| 60 | VWAP momentum · 1h | momentum | 55.27 | -44.73 | 987 | 21.5 | -57.65 | -11.62 | -60.15 | 1207 |
| 61 | Candlestick reversal · 1h | reversion | 55.19 | -44.81 | 552 | 26.4 | -47.45 | -8.65 | -48.77 | 643 |
| 62 | Three white soldiers | momentum | 54.09 | -45.91 | 595 | 14.5 | -50.20 | -22.15 | -51.27 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -41.15 | -99.08 | 5332 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.04 | -27.10 | -82.66 | 1409 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.89 | -42.36 | -94.07 | 2461 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.07 | -31.55 | -90.41 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -39.92 | -91.58 | 2308 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.06 | -30.21 | -90.15 | 2068 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -45.58 | -97.97 | 3468 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.47 | -53.91 | -96.52 | 3398 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.31 | -36.19 | -93.31 | 2180 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.80 | -34.39 | -82.90 | 1584 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -51.44 | -99.61 | 6108 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.06 | -42.78 | -92.23 | 2553 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.75 | -37.13 | -94.76 | 3214 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -66.42 | -99.82 | 6206 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.55 | -42.24 | -92.77 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.68 | -27.18 | -76.95 | 1650 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -58.77 | -97.74 | 3430 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -53.74 | -99.07 | 4972 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.39 | -28.05 | -70.16 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -53.59 | -94.76 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.06 | -38.19 | -85.38 | 1735 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -63.78 | -99.70 | 6405 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.85 | -30.44 | -91.03 | 2368 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.90 | -18.77 | -80.35 | 1838 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.58 | -35.73 | -91.65 | 2170 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.61 | -43.99 | -97.61 | 3916 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.57 | -57.56 | -89.57 | 2171 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.29 | -29.82 | -67.05 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.66 | -26.62 | -73.24 | 1220 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.51 | -18.07 | -81.73 | 1749 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.10 | -97.56 | 4327 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -92.71 | -99.94 | 8449 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T01:20 | Three white soldiers | sell | XRP-USD | 13.51 | -0.12 | exit signal |
| 2026-11-19T01:20 | Three white soldiers | sell | ETH-USD | 13.53 | -0.10 | exit signal |
| 2026-11-19T01:20 | Three white soldiers | sell | BTC-USD | 13.51 | -0.12 | exit signal |
| 2026-11-19T01:10 | Three white soldiers | sell | SOL-USD | 13.54 | -0.09 | exit signal |
| 2026-11-19T01:00 | Bollinger reversion · 1h | sell | ETH-USD | 7.14 | 0.02 | exit signal |
| 2026-11-19T00:40 | Three white soldiers | buy | XRP-USD | 13.63 | — | entry signal |
| 2026-11-19T00:40 | Three white soldiers | buy | SOL-USD | 13.63 | — | entry signal |
| 2026-11-19T00:40 | Three white soldiers | buy | ETH-USD | 13.63 | — | entry signal |
| 2026-11-19T00:40 | Three white soldiers | buy | BTC-USD | 13.63 | — | entry signal |
| 2026-11-19T00:05 | Three white soldiers | sell | SOL-USD | 13.54 | -0.15 | stop-loss |
| 2026-11-19T00:05 | Three white soldiers | sell | DOGE-USD | 13.70 | 0.04 | exit signal |
| 2026-11-19T00:00 | Stochastic reversion · 1h | buy | XRP-USD | 5.20 | — | entry signal |
| 2026-11-18T23:45 | Three white soldiers | buy | SOL-USD | 13.69 | — | entry signal |
| 2026-11-18T23:05 | Three white soldiers | buy | DOGE-USD | 13.66 | — | entry signal |
| 2026-11-18T23:00 | Supertrend · 1h | sell | SOL-USD | 17.81 | 0.09 | exit signal |
| 2026-11-18T22:50 | Donchian 55/20 · 1h | sell | XRP-USD | 19.37 | -0.58 | stop-loss |
| 2026-11-18T20:56 | Agent (ML meta-label) | buy | TQQQ | 1.41 | — | entry |
| 2026-11-18T20:56 | Agent (ML meta-label) | buy | TECL | 8.54 | — | entry |
| 2026-11-18T20:56 | Agent (ML meta-label) | sell | TNA | 9.95 | 0.01 | selected signal exited |
| 2026-11-18T20:55 | Day trade: Stocks in Play ORB | sell | TNA | 25.21 | 0.27 | target is flat |
| 2026-11-18T20:55 | Day trade: Stocks in Play ORB | sell | IWM | 25.04 | 0.10 | target is flat |
| 2026-11-18T20:55 | Opening range 30m | sell | TNA | 20.85 | -0.16 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 30m | sell | IWM | 21.16 | -0.06 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 30m | sell | AMZN | 22.01 | 0.41 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 30m | sell | AMD | 21.05 | 0.25 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 15m | sell | TNA | 19.28 | 0.06 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 15m | sell | IWM | 15.52 | 0.04 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 15m | sell | AMZN | 15.72 | 0.30 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 15m | sell | AMD | 18.63 | 0.22 | end-of-day flatten |
| 2026-11-18T20:45 | Agent (ML meta-label) | buy | TNA | 8.56 | — | rebalance up |
| 2026-11-18T20:45 | Agent (ML meta-label) | sell | SPY | 8.56 | -0.00 | selected signal exited |
| 2026-11-18T20:40 | Agent (aggressive) | sell | SOXL | 42.38 | 0.71 | selected signal exited |
| 2026-11-18T20:40 | Agent | sell | SOXL | 17.26 | 0.29 | selected signal exited |
| 2026-11-18T20:35 | Agent (ML meta-label) | buy | TNA | 1.38 | — | entry |
| 2026-11-18T20:35 | Agent (ML meta-label) | buy | SPY | 8.56 | — | following Squeeze breakout |
| 2026-11-18T20:30 | Agent (ML meta-label) | sell | TQQQ | 9.94 | -0.13 | selected signal exited |
| 2026-11-18T20:30 | MFI reversion · 1h | buy | SPY | 4.44 | — | entry |
| 2026-11-18T20:30 | MFI reversion · 1h | sell | TQQQ | 4.44 | -0.01 | exit signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | PLTR | 11.00 | — | entry signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | MSFT | 3.15 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 01:25:05.000129+00:00 -> 2026-11-19 01:35:05.000129+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 01:25:05.000129+00:00 -> 2026-11-19 01:35:05.000129+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
