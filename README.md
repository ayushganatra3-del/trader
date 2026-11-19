# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T00:25:05.000118+00:00 · 65003 ticks

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

Today: 375 decisions in 75 calls, $0.0053 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T00:25 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-19T00:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-19T00:25 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.97% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| Connors RSI(2) | SQQQ | 1.81 | +3.66% | 10 |
| Squeeze breakout | SQQQ | 1.74 | +6.13% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.63 | 14.63 | 0 | — | 13.21 | 4.35 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 2.97 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.79 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.87 | 3.87 | 0 | — | 4.56 | 1.31 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 152 | 35.5 | -3.30 | -2.87 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.41 | 1.15 | -9.06 | 205 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.47 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.94 | -4.06 | 8 | 50.0 | -4.05 | -0.14 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.61 | -4.39 | 0 | — | -3.89 | -1.26 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.24 | -1.48 | -8.79 | 151 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.95 | -7.86 | -5.54 | 20 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.88 | -7.12 | 0 | — | -6.94 | -1.81 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.83 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.28 | -8.72 | 0 | — | -7.46 | -1.99 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.19 | -9.81 | 114 | 23.7 | -15.26 | -7.38 | -15.58 | 61 |
| 19 | Copy: Insider buying | copy | 90.04 | -9.96 | 52 | 40.4 | -10.48 | -2.10 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.64 | -18.48 | 149 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.03 | -12.97 | 17 | 17.6 | -7.35 | -1.37 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.08 | -9.08 | -18.13 | 72 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.18 | -6.52 | -16.41 | 203 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -11.99 | -4.02 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.84 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.65 | -18.35 | 188 | 28.2 | -24.13 | -6.60 | -27.22 | 197 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.20 | -6.26 | -14.68 | 84 |
| 29 | Keltner breakout · 1h | breakout | 79.88 | -20.12 | 124 | 25.8 | -23.21 | -6.32 | -25.90 | 148 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.23 | -5.21 | -21.31 | 74 |
| 31 | Max aggression: 5-day momentum | meta | 79.14 | -20.86 | 21 | 42.9 | -47.98 | -3.18 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.73 | -30.74 | 84 |
| 33 | Opening range 15m | breakout | 77.70 | -22.30 | 541 | 32.0 | -19.89 | -5.87 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.94 | -23.06 | 2 | 0.0 | -18.99 | -2.56 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.53 | -24.47 | 209 | 19.1 | -26.24 | -4.22 | -34.88 | 266 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.46 | -30.36 | 110 |
| 37 | Hold BTC | benchmark | 73.44 | -26.56 | 2 | 0.0 | -18.44 | -2.69 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.69 | -8.26 | -33.72 | 216 |
| 39 | Stochastic reversion · 1h | reversion | 72.81 | -27.19 | 351 | 42.5 | -34.67 | -5.23 | -35.78 | 425 |
| 40 | Max aggression: 1-day momentum | meta | 71.77 | -28.23 | 32 | 28.1 | -38.62 | -2.32 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.49 | -28.51 | 192 | 16.7 | -32.69 | -5.38 | -39.71 | 200 |
| 42 | Triple EMA stack · 1h | trend | 70.71 | -29.29 | 157 | 14.6 | -30.75 | -6.18 | -37.72 | 172 |
| 43 | MFI reversion · 1h | reversion | 70.45 | -29.55 | 452 | 33.4 | -29.03 | -4.33 | -30.73 | 171 |
| 44 | RSI momentum · 1h | momentum | 70.35 | -29.65 | 179 | 14.5 | -31.46 | -5.66 | -38.37 | 198 |
| 45 | Heikin-Ashi · 1h | trend | 69.90 | -30.10 | 474 | 23.0 | -44.09 | -9.55 | -45.85 | 629 |
| 46 | MACD zero-line · 1h | trend | 69.84 | -30.16 | 184 | 17.9 | -28.09 | -5.56 | -34.29 | 203 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.89 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.15 | -30.85 | 116 | 10.3 | -36.98 | -9.34 | -40.97 | 118 |
| 49 | ROC + volume · 1h | momentum | 69.00 | -31.00 | 413 | 28.1 | -34.03 | -6.18 | -39.51 | 339 |
| 50 | OBV trend · 1h | momentum | 68.23 | -31.77 | 310 | 19.4 | -33.82 | -7.04 | -39.87 | 247 |
| 51 | MACD cross · 1h | trend | 67.68 | -32.32 | 417 | 22.3 | -41.10 | -6.67 | -46.93 | 490 |
| 52 | CCI reversion · 1h | reversion | 67.10 | -32.90 | 387 | 41.6 | -42.35 | -7.05 | -44.29 | 476 |
| 53 | Donchian 20/10 · 1h | breakout | 66.53 | -33.47 | 162 | 17.9 | -35.72 | -6.83 | -41.19 | 191 |
| 54 | Bollinger reversion · 1h | reversion | 63.73 | -36.27 | 348 | 37.9 | -38.93 | -5.89 | -39.66 | 417 |
| 55 | Williams %R · 1h | reversion | 63.58 | -36.42 | 437 | 40.7 | -46.64 | -8.06 | -47.31 | 566 |
| 56 | EMA 9/21 cross · 1h | trend | 62.81 | -37.19 | 285 | 11.6 | -39.64 | -7.70 | -45.71 | 321 |
| 57 | Agent (ML meta-label) | meta | 60.11 | -39.89 | 1949 | 24.6 | -32.01 | -6.43 | -33.70 | 306 |
| 58 | RSI(14) reversion · 1h | reversion | 58.83 | -41.17 | 206 | 32.0 | -41.05 | -6.03 | -43.22 | 254 |
| 59 | Z-score reversion · 1h | reversion | 57.43 | -42.57 | 227 | 35.2 | -36.96 | -5.07 | -39.53 | 259 |
| 60 | VWAP momentum · 1h | momentum | 55.25 | -44.75 | 987 | 21.5 | -56.21 | -10.95 | -60.15 | 1205 |
| 61 | Candlestick reversal · 1h | reversion | 55.17 | -44.83 | 552 | 26.4 | -47.67 | -8.68 | -48.90 | 642 |
| 62 | Three white soldiers | momentum | 54.53 | -45.47 | 591 | 14.6 | -49.94 | -21.70 | -51.01 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -40.18 | -99.08 | 5318 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.07 | -27.15 | -82.66 | 1409 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.92 | -42.86 | -94.07 | 2463 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.06 | -31.53 | -90.41 | 1930 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.34 | -40.26 | -91.58 | 2309 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -29.98 | -90.11 | 2068 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -45.68 | -97.97 | 3466 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.40 | -52.63 | -96.46 | 3395 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.33 | -36.28 | -93.33 | 2183 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.85 | -34.58 | -82.90 | 1585 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -51.31 | -99.61 | 6105 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.05 | -42.56 | -92.23 | 2553 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.76 | -37.25 | -94.77 | 3218 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -65.25 | -99.82 | 6203 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.54 | -42.07 | -92.75 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.54 | -26.93 | -76.92 | 1650 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -57.51 | -97.72 | 3430 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -53.74 | -99.07 | 4972 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.39 | -28.05 | -70.16 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -53.37 | -94.78 | 2757 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.98 | -37.44 | -85.35 | 1734 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -63.67 | -99.70 | 6403 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.85 | -30.44 | -91.03 | 2368 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.90 | -18.77 | -80.35 | 1838 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.51 | -35.60 | -91.62 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.60 | -43.99 | -97.61 | 3916 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.52 | -56.93 | -89.52 | 2169 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.29 | -29.91 | -67.05 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.62 | -26.48 | -73.24 | 1220 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.55 | -18.10 | -81.78 | 1749 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.10 | -97.56 | 4326 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.36 | -99.94 | 8453 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | GOOGL | 3.14 | — | rebalance up |
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | AMZN | 11.01 | — | entry |
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | AMD | 3.13 | — | rebalance up |
| 2026-11-18T20:30 | VWAP momentum · 1h | sell | TQQQ | 7.83 | -0.08 | exit signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | sell | TECL | 7.86 | -0.09 | exit signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | sell | SPY | 7.87 | -0.02 | exit signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | sell | QQQ | 7.87 | -0.03 | exit signal |
| 2026-11-18T20:30 | Trend pullback · 1h | sell | AAPL | 22.50 | -0.07 | exit signal |
| 2026-11-18T20:30 | Heikin-Ashi · 1h | buy | GOOGL | 17.41 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 00:25:05.000118+00:00 -> 2026-11-19 00:35:05.000118+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 00:25:05.000118+00:00 -> 2026-11-19 00:35:05.000118+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
