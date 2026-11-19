# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T05:25:05.000130+00:00 · 65264 ticks

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

Today: 4287 decisions in 858 calls, $0.0599 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T05:25 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-11-19T05:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-19T05:25 | 2 / 3 / 0 | ETH-USD 58% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.86 | 14.86 | 0 | — | 13.21 | 4.22 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.02 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.82 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.07 | 4.07 | 0 | — | 4.56 | 1.41 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 152 | 35.5 | -3.30 | -2.89 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.65 | 1.24 | -9.06 | 206 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.13 | -3.87 | 8 | 50.0 | -4.05 | -0.13 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.80 | -4.20 | 0 | — | -3.89 | -1.35 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -2.78 | -0.97 | -7.69 | 147 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.07 | -6.93 | 0 | — | -6.94 | -1.82 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.46 | -8.54 | 0 | — | -7.46 | -2.08 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.24 | -9.76 | 114 | 23.7 | -15.28 | -7.46 | -15.58 | 61 |
| 19 | Copy: Insider buying | copy | 90.22 | -9.78 | 52 | 40.4 | -10.48 | -2.12 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.13 | -12.87 | 17 | 17.6 | -7.35 | -2.30 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.08 | -9.17 | -18.13 | 72 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.17 | -6.57 | -16.41 | 204 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -11.99 | -4.38 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.64 | -18.36 | 188 | 28.2 | -24.30 | -6.71 | -27.22 | 201 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.20 | -6.31 | -14.68 | 83 |
| 29 | Keltner breakout · 1h | breakout | 79.96 | -20.05 | 124 | 25.8 | -23.44 | -6.44 | -25.90 | 148 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.23 | -5.25 | -21.31 | 74 |
| 31 | Max aggression: 5-day momentum | meta | 79.30 | -20.70 | 21 | 42.9 | -47.98 | -3.20 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 33 | Opening range 15m | breakout | 77.70 | -22.30 | 541 | 32.0 | -19.89 | -5.86 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.09 | -22.91 | 2 | 0.0 | -18.99 | -2.67 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.68 | -24.32 | 209 | 19.1 | -26.44 | -4.30 | -34.88 | 268 |
| 36 | Hold BTC | benchmark | 74.54 | -25.46 | 2 | 0.0 | -18.39 | -3.49 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.65 | -8.30 | -33.72 | 216 |
| 39 | Stochastic reversion · 1h | reversion | 73.00 | -27.00 | 351 | 42.5 | -34.61 | -5.26 | -35.78 | 425 |
| 40 | Max aggression: 1-day momentum | meta | 71.77 | -28.23 | 32 | 28.1 | -38.62 | -2.34 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.56 | -28.44 | 192 | 16.7 | -32.69 | -5.43 | -39.71 | 200 |
| 42 | MFI reversion · 1h | reversion | 70.80 | -29.20 | 452 | 33.4 | -29.20 | -4.39 | -31.00 | 170 |
| 43 | Triple EMA stack · 1h | trend | 70.73 | -29.27 | 157 | 14.6 | -30.89 | -6.27 | -37.74 | 173 |
| 44 | RSI momentum · 1h | momentum | 70.42 | -29.58 | 179 | 14.5 | -31.46 | -5.71 | -38.37 | 198 |
| 45 | Heikin-Ashi · 1h | trend | 70.00 | -30.00 | 474 | 23.0 | -44.45 | -9.62 | -45.85 | 625 |
| 46 | MACD zero-line · 1h | trend | 69.82 | -30.18 | 184 | 17.9 | -28.10 | -5.61 | -34.29 | 204 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.99 | -37.91 | 32 |
| 48 | ROC + volume · 1h | momentum | 69.14 | -30.86 | 413 | 28.1 | -33.54 | -6.12 | -39.51 | 336 |
| 49 | EMA 20/50 cross · 1h | trend | 69.14 | -30.86 | 117 | 10.3 | -37.14 | -9.50 | -40.97 | 118 |
| 50 | OBV trend · 1h | momentum | 68.25 | -31.75 | 310 | 19.4 | -34.01 | -7.17 | -39.88 | 248 |
| 51 | MACD cross · 1h | trend | 67.82 | -32.18 | 417 | 22.3 | -40.55 | -6.58 | -46.92 | 493 |
| 52 | CCI reversion · 1h | reversion | 67.24 | -32.76 | 387 | 41.6 | -42.12 | -7.06 | -44.29 | 476 |
| 53 | Donchian 20/10 · 1h | breakout | 66.57 | -33.43 | 162 | 17.9 | -35.10 | -6.74 | -41.19 | 189 |
| 54 | Bollinger reversion · 1h | reversion | 64.06 | -35.94 | 352 | 38.4 | -38.72 | -5.90 | -39.66 | 417 |
| 55 | Williams %R · 1h | reversion | 63.75 | -36.25 | 439 | 41.0 | -46.51 | -8.10 | -47.31 | 566 |
| 56 | EMA 9/21 cross · 1h | trend | 62.83 | -37.17 | 285 | 11.6 | -39.69 | -7.79 | -45.73 | 322 |
| 57 | Agent (ML meta-label) | meta | 60.23 | -39.77 | 1949 | 24.6 | -24.44 | -4.56 | -27.61 | 298 |
| 58 | RSI(14) reversion · 1h | reversion | 59.06 | -40.94 | 207 | 32.4 | -40.49 | -5.96 | -43.22 | 256 |
| 59 | Z-score reversion · 1h | reversion | 57.54 | -42.46 | 227 | 35.2 | -36.81 | -5.08 | -39.53 | 259 |
| 60 | VWAP momentum · 1h | momentum | 55.36 | -44.64 | 987 | 21.5 | -57.78 | -11.70 | -60.32 | 1212 |
| 61 | Candlestick reversal · 1h | reversion | 55.30 | -44.70 | 553 | 26.4 | -47.78 | -8.84 | -48.84 | 646 |
| 62 | Three white soldiers | momentum | 54.11 | -45.89 | 596 | 14.6 | -50.17 | -23.15 | -51.32 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.07 | -46.70 | -99.09 | 5337 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.14 | -29.58 | -82.78 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.96 | -45.79 | -94.11 | 2465 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.09 | -34.59 | -90.52 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.32 | -44.32 | -91.63 | 2310 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -30.44 | -90.09 | 2063 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -50.39 | -97.99 | 3473 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -55.58 | -96.57 | 3409 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.30 | -37.89 | -93.31 | 2186 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.75 | -35.36 | -83.03 | 1584 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -53.84 | -99.61 | 6116 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.08 | -45.82 | -92.26 | 2553 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.73 | -37.77 | -94.73 | 3210 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.83 | -99.82 | 6204 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.56 | -47.40 | -92.79 | 2268 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.73 | -27.40 | -77.08 | 1649 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -59.73 | -97.77 | 3424 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.07 | -55.96 | -99.07 | 4976 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.29 | -28.47 | -70.25 | 1232 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -53.92 | -94.78 | 2754 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.98 | -40.13 | -85.41 | 1734 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -66.89 | -99.70 | 6411 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.85 | -31.09 | -91.03 | 2370 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.90 | -19.01 | -80.35 | 1838 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.57 | -36.88 | -91.67 | 2162 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.61 | -45.49 | -97.62 | 3922 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.60 | -59.05 | -89.60 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.34 | -31.71 | -67.17 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.61 | -27.94 | -73.38 | 1222 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.56 | -18.37 | -81.79 | 1748 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.87 | -97.57 | 4331 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -96.07 | -99.94 | 8441 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T05:05 | Three white soldiers | sell | BTC-USD | 13.54 | 0.02 | exit signal |
| 2026-11-19T05:00 | Williams %R · 1h | buy | XRP-USD | 3.36 | — | entry |
| 2026-11-19T05:00 | Williams %R · 1h | sell | DOGE-USD | 4.00 | 0.05 | exit signal |
| 2026-11-19T05:00 | Williams %R · 1h | sell | BTC-USD | 2.79 | 0.02 | exit signal |
| 2026-11-19T05:00 | Bollinger reversion · 1h | sell | BTC-USD | 10.70 | 0.02 | exit signal |
| 2026-11-19T05:00 | RSI(14) reversion · 1h | sell | ETH-USD | 4.00 | 0.05 | exit signal |
| 2026-11-19T05:00 | OBV trend · 1h | buy | SOL-USD | 17.08 | — | entry signal |
| 2026-11-19T05:00 | Parabolic SAR · 1h | buy | ETH-USD | 13.49 | — | entry signal |
| 2026-11-19T05:00 | Parabolic SAR · 1h | buy | DOGE-USD | 13.63 | — | entry signal |
| 2026-11-19T05:00 | Parabolic SAR · 1h | sell | SOL-USD | 6.82 | -0.01 | rebalance down |
| 2026-11-19T05:00 | MACD zero-line · 1h | buy | SOL-USD | 17.47 | — | entry signal |
| 2026-11-19T05:00 | Triple EMA stack · 1h | buy | SOL-USD | 17.70 | — | entry signal |
| 2026-11-19T05:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 15.72 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 05:25:05.000130+00:00 -> 2026-11-19 05:35:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 05:25:05.000130+00:00 -> 2026-11-19 05:35:05.000130+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
