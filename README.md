# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T10:55:05.000106+00:00 · 65563 ticks

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

Today: 8772 decisions in 1755 calls, $0.1225 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T10:55 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-19T10:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-19T10:55 | 1 / 4 / 0 | BTC-USD 51% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.70 | 14.70 | 0 | — | 13.21 | 4.22 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.02 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.82 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.93 | 3.93 | 0 | — | 4.56 | 1.41 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 152 | 35.5 | -3.30 | -2.89 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.41 | 1.16 | -9.06 | 205 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.00 | -4.00 | 8 | 50.0 | -4.05 | -0.13 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.67 | -4.33 | 0 | — | -3.89 | -1.35 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -2.86 | -1.00 | -7.69 | 146 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.94 | -7.06 | 0 | — | -6.94 | -1.82 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.34 | -8.66 | 0 | — | -7.46 | -2.08 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.21 | -9.79 | 114 | 23.7 | -14.95 | -7.24 | -15.61 | 59 |
| 19 | Copy: Insider buying | copy | 90.10 | -9.90 | 52 | 40.4 | -10.48 | -2.12 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.06 | -12.94 | 17 | 17.6 | -7.35 | -2.30 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.21 | -9.25 | -18.57 | 73 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.17 | -6.58 | -16.41 | 204 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -11.99 | -4.38 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.64 | -18.36 | 188 | 28.2 | -24.07 | -6.64 | -27.22 | 201 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.21 | -6.32 | -14.68 | 83 |
| 29 | Keltner breakout · 1h | breakout | 79.90 | -20.10 | 124 | 25.8 | -23.35 | -6.41 | -25.90 | 147 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.23 | -5.25 | -21.31 | 74 |
| 31 | Max aggression: 5-day momentum | meta | 79.19 | -20.81 | 21 | 42.9 | -47.98 | -3.20 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 33 | Opening range 15m | breakout | 77.70 | -22.30 | 541 | 32.0 | -19.89 | -5.86 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.99 | -23.01 | 2 | 0.0 | -18.99 | -2.67 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.58 | -24.42 | 209 | 19.1 | -26.42 | -4.29 | -34.88 | 269 |
| 36 | Hold BTC | benchmark | 74.90 | -25.10 | 2 | 0.0 | -18.43 | -3.38 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 73.83 | -26.17 | 104 | 14.4 | -29.54 | -8.64 | -30.67 | 112 |
| 38 | Stochastic reversion · 1h | reversion | 72.95 | -27.05 | 352 | 42.6 | -34.55 | -5.25 | -35.78 | 425 |
| 39 | Bollinger breakout · 1h | breakout | 72.80 | -27.20 | 192 | 21.9 | -30.82 | -8.37 | -33.86 | 217 |
| 40 | Max aggression: 1-day momentum | meta | 71.77 | -28.23 | 32 | 28.1 | -38.62 | -2.34 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.31 | -28.70 | 192 | 16.7 | -32.88 | -5.47 | -39.71 | 201 |
| 42 | MFI reversion · 1h | reversion | 70.78 | -29.22 | 452 | 33.4 | -28.47 | -4.25 | -30.85 | 170 |
| 43 | Triple EMA stack · 1h | trend | 70.60 | -29.40 | 157 | 14.6 | -30.83 | -6.31 | -37.69 | 173 |
| 44 | RSI momentum · 1h | momentum | 70.17 | -29.83 | 179 | 14.5 | -32.02 | -6.05 | -38.37 | 199 |
| 45 | Heikin-Ashi · 1h | trend | 69.98 | -30.02 | 474 | 23.0 | -44.01 | -9.61 | -45.85 | 628 |
| 46 | MACD zero-line · 1h | trend | 69.59 | -30.41 | 184 | 17.9 | -28.34 | -5.67 | -34.55 | 207 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.99 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.22 | -30.78 | 117 | 10.3 | -36.24 | -7.57 | -43.13 | 121 |
| 49 | ROC + volume · 1h | momentum | 69.04 | -30.96 | 413 | 28.1 | -33.53 | -6.11 | -39.51 | 336 |
| 50 | OBV trend · 1h | momentum | 68.10 | -31.90 | 310 | 19.4 | -34.29 | -7.26 | -39.96 | 249 |
| 51 | MACD cross · 1h | trend | 67.72 | -32.28 | 417 | 22.3 | -40.52 | -6.57 | -46.92 | 494 |
| 52 | CCI reversion · 1h | reversion | 67.14 | -32.86 | 387 | 41.6 | -42.09 | -7.05 | -44.29 | 476 |
| 53 | Donchian 20/10 · 1h | breakout | 66.54 | -33.46 | 162 | 17.9 | -35.10 | -6.74 | -41.19 | 189 |
| 54 | Bollinger reversion · 1h | reversion | 64.01 | -35.98 | 352 | 38.4 | -38.72 | -5.90 | -39.66 | 417 |
| 55 | Williams %R · 1h | reversion | 63.69 | -36.31 | 440 | 41.1 | -46.85 | -8.18 | -47.66 | 567 |
| 56 | EMA 9/21 cross · 1h | trend | 62.67 | -37.33 | 285 | 11.6 | -39.71 | -7.79 | -45.88 | 326 |
| 57 | Agent (ML meta-label) | meta | 60.14 | -39.86 | 1949 | 24.6 | -30.97 | -5.73 | -32.17 | 279 |
| 58 | RSI(14) reversion · 1h | reversion | 58.99 | -41.01 | 208 | 32.7 | -40.36 | -5.93 | -43.22 | 258 |
| 59 | Z-score reversion · 1h | reversion | 57.46 | -42.54 | 227 | 35.2 | -36.78 | -5.08 | -39.53 | 259 |
| 60 | VWAP momentum · 1h | momentum | 55.28 | -44.72 | 987 | 21.5 | -57.70 | -11.71 | -60.32 | 1213 |
| 61 | Candlestick reversal · 1h | reversion | 55.23 | -44.77 | 553 | 26.4 | -48.05 | -8.89 | -49.09 | 646 |
| 62 | Three white soldiers | momentum | 53.92 | -46.08 | 598 | 14.5 | -50.38 | -23.18 | -51.57 | 666 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.06 | -46.40 | -99.09 | 5333 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.44 | -29.49 | -82.78 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.13 | -46.73 | -94.13 | 2465 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.38 | -34.79 | -90.45 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.61 | -44.70 | -91.65 | 2311 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.96 | -31.24 | -89.97 | 2063 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.93 | -51.33 | -98.00 | 3477 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.68 | -57.79 | -96.68 | 3425 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -38.71 | -93.62 | 2215 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.10 | -35.94 | -83.10 | 1585 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -53.98 | -99.61 | 6115 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.07 | -47.20 | -92.33 | 2552 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.69 | -38.93 | -94.69 | 3207 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -73.64 | -99.82 | 6203 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.63 | -47.69 | -92.77 | 2267 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.79 | -27.84 | -77.29 | 1649 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -61.53 | -97.78 | 3429 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.07 | -56.86 | -99.07 | 4979 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.48 | -29.31 | -70.41 | 1232 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -56.36 | -94.87 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.14 | -41.07 | -85.57 | 1735 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -68.85 | -99.70 | 6415 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.86 | -31.10 | -91.03 | 2370 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.87 | -19.01 | -80.35 | 1841 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.57 | -37.02 | -91.66 | 2163 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.62 | -45.70 | -97.62 | 3923 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.37 | -59.96 | -89.62 | 2173 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.62 | -32.42 | -67.53 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.36 | -28.00 | -73.41 | 1223 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.60 | -18.40 | -81.80 | 1753 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.58 | -45.38 | -97.58 | 4335 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -105.58 | -99.94 | 8448 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-19T05:00 | Williams %R · 1h | sell | BTC-USD | 2.79 | 0.02 | exit signal |
| 2026-11-19T05:00 | Bollinger reversion · 1h | sell | BTC-USD | 10.70 | 0.02 | exit signal |
| 2026-11-19T05:00 | RSI(14) reversion · 1h | sell | ETH-USD | 4.00 | 0.05 | exit signal |
| 2026-11-19T05:00 | OBV trend · 1h | buy | SOL-USD | 17.08 | — | entry signal |
| 2026-11-19T05:00 | Parabolic SAR · 1h | buy | ETH-USD | 13.49 | — | entry signal |
| 2026-11-19T05:00 | Parabolic SAR · 1h | buy | DOGE-USD | 13.63 | — | entry signal |
| 2026-11-19T05:00 | Parabolic SAR · 1h | sell | SOL-USD | 6.82 | -0.01 | rebalance down |
| 2026-11-19T05:00 | MACD zero-line · 1h | buy | SOL-USD | 17.47 | — | entry signal |
| 2026-11-19T05:00 | Triple EMA stack · 1h | buy | SOL-USD | 17.70 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 10:55:05.000106+00:00 -> 2026-11-19 11:05:05.000106+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 10:55:05.000106+00:00 -> 2026-11-19 11:05:05.000106+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
