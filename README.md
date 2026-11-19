# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T12:55:05.000175+00:00 · 65672 ticks

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

Today: 10407 decisions in 2082 calls, $0.1453 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T12:55 | 1 / 4 / 0 | XRP-USD 16% |  |
| Breezy | 2026-11-19T12:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-19T12:55 | 2 / 3 / 0 | ETH-USD 63% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.61 | 14.61 | 0 | — | 13.21 | 4.22 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.02 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.82 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.85 | 3.85 | 0 | — | 4.56 | 1.41 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 152 | 35.5 | -3.30 | -2.89 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.65 | 1.24 | -9.06 | 206 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.92 | -4.08 | 8 | 50.0 | -4.05 | -0.13 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.59 | -4.41 | 0 | — | -3.89 | -1.35 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -2.78 | -0.97 | -7.69 | 147 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.86 | -7.14 | 0 | — | -6.94 | -1.82 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.26 | -8.74 | 0 | — | -7.46 | -2.08 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.19 | -9.81 | 114 | 23.7 | -14.95 | -7.24 | -15.61 | 59 |
| 19 | Copy: Insider buying | copy | 90.03 | -9.97 | 52 | 40.4 | -10.48 | -2.12 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.03 | -12.97 | 17 | 17.6 | -7.35 | -2.30 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.08 | -9.17 | -18.13 | 72 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.17 | -6.57 | -16.41 | 203 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -11.99 | -4.38 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.69 | -18.31 | 188 | 28.2 | -23.90 | -6.57 | -27.22 | 201 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -13.89 | -6.16 | -14.68 | 83 |
| 29 | Keltner breakout · 1h | breakout | 79.87 | -20.13 | 124 | 25.8 | -23.19 | -6.21 | -25.90 | 148 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.23 | -5.25 | -21.31 | 74 |
| 31 | Max aggression: 5-day momentum | meta | 79.13 | -20.87 | 21 | 42.9 | -47.98 | -3.20 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 33 | Opening range 15m | breakout | 77.70 | -22.30 | 541 | 32.0 | -19.89 | -5.86 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.93 | -23.07 | 2 | 0.0 | -18.99 | -2.67 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.52 | -24.48 | 209 | 19.1 | -26.41 | -4.29 | -34.88 | 269 |
| 36 | Hold BTC | benchmark | 74.90 | -25.11 | 2 | 0.0 | -20.45 | -3.37 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 73.96 | -26.04 | 104 | 14.4 | -29.39 | -8.58 | -30.70 | 112 |
| 38 | Stochastic reversion · 1h | reversion | 72.91 | -27.09 | 352 | 42.6 | -34.54 | -5.25 | -35.78 | 425 |
| 39 | Bollinger breakout · 1h | breakout | 72.86 | -27.14 | 192 | 21.9 | -30.74 | -8.34 | -33.86 | 217 |
| 40 | Max aggression: 1-day momentum | meta | 71.77 | -28.23 | 32 | 28.1 | -38.62 | -2.34 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.30 | -28.70 | 192 | 16.7 | -32.86 | -5.47 | -39.71 | 202 |
| 42 | MFI reversion · 1h | reversion | 70.76 | -29.24 | 452 | 33.4 | -28.88 | -4.32 | -31.00 | 170 |
| 43 | Triple EMA stack · 1h | trend | 70.71 | -29.29 | 157 | 14.6 | -30.68 | -6.29 | -37.87 | 174 |
| 44 | RSI momentum · 1h | momentum | 70.20 | -29.80 | 179 | 14.5 | -31.24 | -5.66 | -38.41 | 199 |
| 45 | Heikin-Ashi · 1h | trend | 69.89 | -30.11 | 475 | 22.9 | -43.99 | -9.60 | -45.85 | 628 |
| 46 | MACD zero-line · 1h | trend | 69.67 | -30.33 | 184 | 17.9 | -28.21 | -5.64 | -34.66 | 208 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.99 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.26 | -30.74 | 117 | 10.3 | -37.27 | -9.75 | -41.02 | 120 |
| 49 | ROC + volume · 1h | momentum | 68.98 | -31.02 | 413 | 28.1 | -33.53 | -6.11 | -39.51 | 336 |
| 50 | OBV trend · 1h | momentum | 68.20 | -31.80 | 310 | 19.4 | -33.92 | -7.14 | -39.98 | 249 |
| 51 | MACD cross · 1h | trend | 67.67 | -32.33 | 417 | 22.3 | -40.48 | -6.56 | -46.92 | 494 |
| 52 | CCI reversion · 1h | reversion | 67.09 | -32.91 | 387 | 41.6 | -42.09 | -7.05 | -44.29 | 476 |
| 53 | Donchian 20/10 · 1h | breakout | 66.53 | -33.47 | 162 | 17.9 | -35.07 | -6.73 | -41.19 | 189 |
| 54 | Bollinger reversion · 1h | reversion | 63.99 | -36.01 | 352 | 38.4 | -38.72 | -5.90 | -39.66 | 417 |
| 55 | Williams %R · 1h | reversion | 63.65 | -36.35 | 440 | 41.1 | -46.85 | -8.18 | -47.66 | 567 |
| 56 | EMA 9/21 cross · 1h | trend | 62.71 | -37.29 | 285 | 11.6 | -39.58 | -7.76 | -45.93 | 326 |
| 57 | Agent (ML meta-label) | meta | 60.10 | -39.90 | 1949 | 24.6 | -34.64 | -7.29 | -35.76 | 301 |
| 58 | RSI(14) reversion · 1h | reversion | 58.95 | -41.05 | 208 | 32.7 | -40.93 | -6.06 | -43.22 | 254 |
| 59 | Z-score reversion · 1h | reversion | 57.42 | -42.58 | 227 | 35.2 | -36.79 | -5.08 | -39.53 | 259 |
| 60 | VWAP momentum · 1h | momentum | 55.24 | -44.76 | 987 | 21.5 | -57.35 | -11.62 | -60.32 | 1209 |
| 61 | Candlestick reversal · 1h | reversion | 55.19 | -44.81 | 553 | 26.4 | -47.87 | -8.87 | -48.97 | 639 |
| 62 | Three white soldiers | momentum | 53.92 | -46.08 | 598 | 14.5 | -50.99 | -23.26 | -51.07 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.07 | -46.21 | -99.09 | 5324 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.48 | -29.63 | -82.78 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.20 | -47.78 | -94.21 | 2471 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.48 | -35.21 | -90.51 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.66 | -45.75 | -91.70 | 2311 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.55 | -90.04 | 2066 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.01 | -52.35 | -98.02 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.65 | -58.11 | -96.67 | 3420 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -38.74 | -93.62 | 2212 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.17 | -36.20 | -83.22 | 1588 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -53.88 | -99.61 | 6117 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.40 | -48.00 | -92.43 | 2555 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.67 | -39.16 | -94.68 | 3208 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -74.65 | -99.82 | 6212 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.78 | -48.39 | -92.79 | 2270 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.25 | -27.88 | -77.36 | 1650 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -62.12 | -97.77 | 3431 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.07 | -57.05 | -99.08 | 4984 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.25 | -29.64 | -70.27 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.87 | -57.02 | -94.87 | 2754 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.58 | -41.46 | -85.66 | 1737 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -69.09 | -99.70 | 6419 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.86 | -31.13 | -91.03 | 2371 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.90 | -19.01 | -80.35 | 1837 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.66 | -37.20 | -91.68 | 2162 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.62 | -45.87 | -97.62 | 3924 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.64 | -60.68 | -89.64 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.33 | -32.56 | -67.37 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.33 | -28.05 | -73.45 | 1222 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.56 | -18.37 | -81.79 | 1748 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.58 | -45.53 | -97.58 | 4336 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.22 | -99.94 | 8449 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T12:00 | Supertrend · 1h | buy | BTC-USD | 17.82 | — | entry signal |
| 2026-11-19T12:00 | EMA 20/50 cross · 1h | buy | DOGE-USD | 17.31 | — | entry signal |
| 2026-11-19T11:45 | MACD zero-line · 1h | buy | XRP-USD | 3.48 | — | rebalance up |
| 2026-11-19T11:45 | MACD zero-line · 1h | sell | DOGE-USD | 3.48 | -0.02 | rebalance down |
| 2026-11-19T11:35 | MACD zero-line · 1h | buy | XRP-USD | 3.49 | — | rebalance up |
| 2026-11-19T11:35 | MACD zero-line · 1h | sell | SOL-USD | 3.49 | -0.02 | rebalance down |
| 2026-11-19T11:00 | Heikin-Ashi · 1h | buy | ETH-USD | 3.08 | — | entry |
| 2026-11-19T11:00 | Heikin-Ashi · 1h | buy | BTC-USD | 3.97 | — | rebalance up |
| 2026-11-19T11:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 7.05 | -0.02 | exit signal |
| 2026-11-19T10:55 | Three white soldiers | sell | DOGE-USD | 13.41 | -0.10 | exit signal |
| 2026-11-19T10:50 | Three white soldiers | buy | DOGE-USD | 13.50 | — | entry signal |
| 2026-11-19T10:10 | MACD zero-line · 1h | buy | XRP-USD | 3.48 | — | entry |
| 2026-11-19T10:10 | MACD zero-line · 1h | sell | ETH-USD | 3.48 | -0.01 | rebalance down |
| 2026-11-19T10:00 | RSI(14) reversion · 1h | sell | BTC-USD | 3.96 | 0.02 | exit signal |
| 2026-11-19T09:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 3.51 | — | entry signal |
| 2026-11-19T09:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 3.51 | -0.03 | rebalance down |
| 2026-11-19T08:05 | Three white soldiers | sell | XRP-USD | 13.43 | -0.10 | exit signal |
| 2026-11-19T08:00 | Ichimoku · 1h | buy | SOL-USD | 18.53 | — | entry signal |
| 2026-11-19T08:00 | Ichimoku · 1h | buy | DOGE-USD | 18.53 | — | entry signal |
| 2026-11-19T08:00 | MACD zero-line · 1h | buy | ETH-USD | 17.44 | — | entry signal |
| 2026-11-19T08:00 | MACD zero-line · 1h | buy | DOGE-USD | 17.46 | — | entry signal |
| 2026-11-19T08:00 | Triple EMA stack · 1h | buy | XRP-USD | 16.77 | — | entry signal |
| 2026-11-19T08:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 5.20 | — | rebalance up |
| 2026-11-19T08:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 5.20 | -0.02 | rebalance down |
| 2026-11-19T07:55 | Three white soldiers | buy | XRP-USD | 13.53 | — | entry signal |
| 2026-11-19T07:00 | Williams %R · 1h | sell | XRP-USD | 3.36 | 0.00 | exit signal |
| 2026-11-19T07:00 | Stochastic reversion · 1h | sell | XRP-USD | 5.27 | 0.07 | exit signal |
| 2026-11-19T07:00 | Bollinger breakout · 1h | buy | SOL-USD | 18.25 | — | entry signal |
| 2026-11-19T07:00 | OBV trend · 1h | buy | XRP-USD | 16.14 | — | entry signal |
| 2026-11-19T07:00 | RSI momentum · 1h | buy | SOL-USD | 17.60 | — | entry signal |
| 2026-11-19T07:00 | Supertrend · 1h | buy | SOL-USD | 17.89 | — | entry signal |
| 2026-11-19T07:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 4.73 | — | entry signal |
| 2026-11-19T07:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 3.18 | 0.00 | rebalance down |
| 2026-11-19T06:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 7.07 | — | entry signal |
| 2026-11-19T06:00 | Heikin-Ashi · 1h | buy | BTC-USD | 10.00 | — | entry signal |
| 2026-11-19T06:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 17.28 | — | entry signal |
| 2026-11-19T06:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 15.70 | — | entry signal |
| 2026-11-19T05:05 | Three white soldiers | sell | BTC-USD | 13.54 | 0.02 | exit signal |
| 2026-11-19T05:00 | Williams %R · 1h | buy | XRP-USD | 3.36 | — | entry |
| 2026-11-19T05:00 | Williams %R · 1h | sell | DOGE-USD | 4.00 | 0.05 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 12:55:05.000175+00:00 -> 2026-11-19 13:05:05.000175+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 12:55:05.000175+00:00 -> 2026-11-19 13:05:05.000175+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
