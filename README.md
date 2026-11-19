# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T04:26:05.000168+00:00 · 65207 ticks

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
| Copy: Insider buying | 2026-11-19 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, LRN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-18)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 33.12 · VIX 24.56 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 6.2, AMZN 6.2, TSLA 4.1, AMD 3.9, META 1.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 3435 decisions in 687 calls, $0.0481 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T04:26 | 2 / 3 / 0 | SOL-USD 16% |  |
| Breezy | 2026-11-19T04:26 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-19T04:26 | 5 / 0 / 0 | ETH-USD 64% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.82 | 14.82 | 0 | — | 13.21 | 4.22 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.02 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.82 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.04 | 4.04 | 0 | — | 4.56 | 1.41 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 152 | 35.5 | -3.30 | -2.89 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.41 | 1.16 | -9.06 | 205 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.10 | -3.90 | 8 | 50.0 | -4.05 | -0.13 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.77 | -4.23 | 0 | — | -3.89 | -1.35 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -2.86 | -1.00 | -7.69 | 146 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.03 | -6.97 | 0 | — | -6.94 | -1.82 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.43 | -8.57 | 0 | — | -7.46 | -2.08 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.23 | -9.77 | 114 | 23.7 | -15.34 | -7.48 | -15.58 | 61 |
| 19 | Copy: Insider buying | copy | 90.19 | -9.81 | 52 | 40.4 | -10.48 | -2.12 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.11 | -12.89 | 17 | 17.6 | -7.35 | -2.30 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.41 | -9.37 | -18.61 | 73 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.17 | -6.58 | -16.41 | 204 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -11.99 | -4.38 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.73 | -18.27 | 188 | 28.2 | -24.12 | -6.65 | -27.22 | 198 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.21 | -6.32 | -14.68 | 83 |
| 29 | Keltner breakout · 1h | breakout | 79.94 | -20.06 | 124 | 25.8 | -23.68 | -6.51 | -25.90 | 149 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.23 | -5.25 | -21.31 | 74 |
| 31 | Max aggression: 5-day momentum | meta | 79.27 | -20.73 | 21 | 42.9 | -47.98 | -3.20 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 33 | Opening range 15m | breakout | 77.70 | -22.30 | 541 | 32.0 | -19.89 | -5.86 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.07 | -22.93 | 2 | 0.0 | -18.99 | -2.67 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.66 | -24.34 | 209 | 19.1 | -26.38 | -4.28 | -34.88 | 267 |
| 36 | Hold BTC | benchmark | 74.43 | -25.57 | 2 | 0.0 | -18.56 | -3.51 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.73 | -8.35 | -33.72 | 216 |
| 39 | Stochastic reversion · 1h | reversion | 72.97 | -27.03 | 351 | 42.5 | -34.66 | -5.27 | -35.81 | 425 |
| 40 | Max aggression: 1-day momentum | meta | 71.77 | -28.23 | 32 | 28.1 | -38.62 | -2.34 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.55 | -28.45 | 192 | 16.7 | -32.69 | -5.43 | -39.71 | 200 |
| 42 | Triple EMA stack · 1h | trend | 70.77 | -29.23 | 157 | 14.6 | -30.82 | -6.25 | -37.72 | 172 |
| 43 | MFI reversion · 1h | reversion | 70.77 | -29.23 | 452 | 33.4 | -28.75 | -4.31 | -30.85 | 170 |
| 44 | RSI momentum · 1h | momentum | 70.41 | -29.59 | 179 | 14.5 | -31.68 | -5.90 | -38.37 | 198 |
| 45 | Heikin-Ashi · 1h | trend | 69.98 | -30.02 | 474 | 23.0 | -44.45 | -9.62 | -45.85 | 625 |
| 46 | MACD zero-line · 1h | trend | 69.87 | -30.14 | 184 | 17.9 | -28.05 | -5.59 | -34.29 | 203 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.99 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.13 | -30.87 | 117 | 10.3 | -37.42 | -9.81 | -40.97 | 118 |
| 49 | ROC + volume · 1h | momentum | 69.11 | -30.89 | 413 | 28.1 | -33.71 | -6.15 | -39.51 | 336 |
| 50 | OBV trend · 1h | momentum | 68.29 | -31.71 | 310 | 19.4 | -33.94 | -7.15 | -39.87 | 247 |
| 51 | MACD cross · 1h | trend | 67.79 | -32.21 | 417 | 22.3 | -40.54 | -6.58 | -46.92 | 492 |
| 52 | CCI reversion · 1h | reversion | 67.21 | -32.79 | 387 | 41.6 | -42.13 | -7.06 | -44.29 | 476 |
| 53 | Donchian 20/10 · 1h | breakout | 66.56 | -33.44 | 162 | 17.9 | -35.30 | -6.79 | -41.19 | 190 |
| 54 | Bollinger reversion · 1h | reversion | 64.05 | -35.95 | 351 | 38.2 | -38.71 | -5.89 | -39.66 | 417 |
| 55 | Williams %R · 1h | reversion | 63.76 | -36.24 | 437 | 40.7 | -46.53 | -8.10 | -47.34 | 566 |
| 56 | EMA 9/21 cross · 1h | trend | 62.86 | -37.14 | 285 | 11.6 | -39.64 | -7.77 | -45.71 | 321 |
| 57 | Agent (ML meta-label) | meta | 60.21 | -39.80 | 1949 | 24.6 | -25.54 | -4.58 | -28.06 | 298 |
| 58 | RSI(14) reversion · 1h | reversion | 59.04 | -40.96 | 206 | 32.0 | -40.43 | -5.94 | -43.22 | 257 |
| 59 | Z-score reversion · 1h | reversion | 57.52 | -42.48 | 227 | 35.2 | -36.79 | -5.08 | -39.53 | 259 |
| 60 | VWAP momentum · 1h | momentum | 55.34 | -44.66 | 987 | 21.5 | -57.80 | -11.70 | -60.32 | 1213 |
| 61 | Candlestick reversal · 1h | reversion | 55.28 | -44.72 | 553 | 26.4 | -47.96 | -8.86 | -48.96 | 645 |
| 62 | Three white soldiers | momentum | 54.13 | -45.87 | 595 | 14.5 | -50.29 | -23.06 | -51.45 | 665 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.09 | -46.73 | -99.09 | 5348 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.15 | -29.61 | -82.78 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.94 | -45.84 | -94.11 | 2465 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.10 | -34.61 | -90.52 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.34 | -44.37 | -91.63 | 2312 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.04 | -30.41 | -90.11 | 2063 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -50.44 | -97.99 | 3474 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -55.60 | -96.58 | 3416 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.23 | -37.34 | -93.24 | 2183 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.74 | -35.39 | -83.03 | 1585 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -53.78 | -99.61 | 6116 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.07 | -45.74 | -92.26 | 2553 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.72 | -37.53 | -94.73 | 3208 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.24 | -99.82 | 6206 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.54 | -46.93 | -92.79 | 2269 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.67 | -27.32 | -77.07 | 1649 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -59.26 | -97.77 | 3425 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.07 | -55.96 | -99.07 | 4978 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.26 | -28.36 | -70.25 | 1232 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.65 | -53.47 | -94.78 | 2754 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.99 | -40.00 | -85.43 | 1734 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -66.67 | -99.70 | 6411 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.85 | -31.09 | -91.03 | 2370 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.92 | -19.01 | -80.36 | 1840 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.55 | -36.87 | -91.66 | 2162 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.61 | -45.49 | -97.62 | 3922 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.59 | -59.06 | -89.59 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.19 | -31.26 | -67.05 | 804 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.76 | -27.97 | -73.38 | 1224 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.58 | -18.40 | -81.80 | 1751 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -44.87 | -97.57 | 4332 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -93.99 | -99.94 | 8440 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T04:00 | Bollinger reversion · 1h | buy | BTC-USD | 3.56 | — | rebalance up |
| 2026-11-19T04:00 | Bollinger reversion · 1h | sell | SOL-USD | 7.14 | 0.03 | exit signal |
| 2026-11-19T04:00 | Bollinger reversion · 1h | sell | DOGE-USD | 7.11 | -0.01 | exit signal |
| 2026-11-19T04:00 | Parabolic SAR · 1h | buy | SOL-USD | 20.43 | — | entry signal |
| 2026-11-19T03:35 | Three white soldiers | buy | BTC-USD | 13.52 | — | entry signal |
| 2026-11-19T03:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 17.27 | -0.17 | exit signal |
| 2026-11-19T02:00 | Candlestick reversal · 1h | buy | ETH-USD | 1.97 | — | entry |
| 2026-11-19T02:00 | Candlestick reversal · 1h | sell | SOL-USD | 1.97 | -0.01 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 04:26:05.000168+00:00 -> 2026-11-19 04:36:05.000168+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 04:26:05.000168+00:00 -> 2026-11-19 04:36:05.000168+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
