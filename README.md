# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T18:10:05.000124+00:00 · 72106 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.42 (-21.58%)

Closed trades 243, win rate 35.8%, fees £6.56, max drawdown -22.02%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 15.68 | -0.00 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-24 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, BH 12%, FUN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-23)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.62 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.4, AAPL 4.1, TSLA 3.2, AMZN 1.1, GOOGL 0.8, META 0.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 28926 decisions in 2898 calls, $0.3648 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T18:10 | 0 / 21 / 9 | cash |  |
| Breezy | 2026-11-24T18:10 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-24T18:10 | 4 / 24 / 2 | BITX 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |
| Opening range 30m | SQQQ | 1.57 | +20.80% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 28.60 | 4.33 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.71 | 15.71 | 0 | — | 13.78 | 4.71 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.48 | 4.48 | 0 | — | 4.63 | 1.32 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.12 | 0.05 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.28 | -3.72 | 229 | 28.4 | -0.02 | 0.08 | -7.48 | 156 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.06 | -3.51 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.64 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.33 | -5.67 | 0 | — | -6.50 | -1.65 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.28 | -5.49 | 19 |
| 14 | Copy: Insider buying | copy | 91.98 | -8.02 | 58 | 39.7 | -7.03 | -1.29 | -14.79 | 70 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.97 | -8.03 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 16 | Trend pullback · 1h | trend | 91.07 | -8.93 | 116 | 24.1 | -9.07 | -4.89 | -11.87 | 41 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.80 | -10.20 | 0 | — | -10.97 | -2.36 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.09 | -2.99 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.56 | -13.44 | 166 | 46.4 | -10.78 | -1.94 | -20.49 | 154 |
| 21 | Opening range 30m | breakout | 85.41 | -14.59 | 469 | 32.8 | -13.83 | -4.65 | -14.39 | 552 |
| 22 | Daily: Bullish score | daily | 85.35 | -14.65 | 20 | 20.0 | -13.42 | -3.10 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -18.21 | -6.74 | -18.47 | 71 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.62 | -6.51 | -14.78 | 66 |
| 26 | Parabolic SAR · 1h | trend | 79.07 | -20.93 | 206 | 28.2 | -31.91 | -8.39 | -32.65 | 184 |
| 27 | Agent | meta | 78.42 | -21.58 | 243 | 35.8 | -26.29 | -5.98 | -26.55 | 197 |
| 28 | Volume breakout · 1h | breakout | 78.06 | -21.93 | 169 | 27.8 | -22.30 | -6.80 | -23.97 | 72 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 76.82 | -23.18 | 138 | 24.6 | -26.67 | -6.92 | -28.41 | 153 |
| 31 | Opening range 15m | breakout | 76.71 | -23.29 | 585 | 30.4 | -22.50 | -7.02 | -22.97 | 679 |
| 32 | Donchian 55/20 · 1h | breakout | 76.07 | -23.93 | 87 | 13.8 | -29.70 | -7.86 | -29.88 | 84 |
| 33 | Ichimoku · 1h | trend | 74.49 | -25.51 | 113 | 15.9 | -29.78 | -7.69 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.57 | -29.43 | 259 | 19.3 | -38.77 | -7.40 | -40.40 | 281 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.37 | -4.86 | -36.38 | 24 |
| 36 | Hold BTC | benchmark | 69.46 | -30.54 | 3 | 0.0 | -29.02 | -5.17 | -36.10 | 1 |
| 37 | Supertrend · 1h | trend | 69.00 | -31.00 | 205 | 18.5 | -35.41 | -6.86 | -37.48 | 217 |
| 38 | Bollinger breakout · 1h | breakout | 68.96 | -31.04 | 208 | 22.1 | -31.82 | -8.40 | -34.11 | 211 |
| 39 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -39.11 | -10.31 | -39.29 | 173 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 68.19 | -31.81 | 3 | 0.0 | -24.78 | -3.03 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.67 | -32.33 | 124 | 9.7 | -36.43 | -10.10 | -37.41 | 114 |
| 42 | OBV trend · 1h | momentum | 66.50 | -33.50 | 323 | 19.8 | -39.47 | -10.14 | -40.35 | 230 |
| 43 | RSI momentum · 1h | momentum | 65.49 | -34.51 | 200 | 15.0 | -39.81 | -9.15 | -41.43 | 196 |
| 44 | Heikin-Ashi · 1h | trend | 64.95 | -35.05 | 538 | 22.1 | -47.64 | -9.71 | -49.48 | 630 |
| 45 | MACD zero-line · 1h | trend | 64.47 | -35.53 | 199 | 16.6 | -35.18 | -9.73 | -35.76 | 200 |
| 46 | Stochastic reversion · 1h | reversion | 63.64 | -36.36 | 400 | 40.5 | -35.97 | -3.97 | -43.59 | 437 |
| 47 | Max aggression: 1-day momentum | meta | 63.04 | -36.96 | 34 | 26.5 | -56.72 | -4.22 | -60.68 | 38 |
| 48 | ROC + volume · 1h | momentum | 62.84 | -37.16 | 453 | 27.2 | -42.69 | -8.34 | -44.24 | 343 |
| 49 | Donchian 20/10 · 1h | breakout | 62.19 | -37.81 | 181 | 17.7 | -39.70 | -8.51 | -42.39 | 192 |
| 50 | Max aggression: 5-day momentum | meta | 61.83 | -38.17 | 26 | 34.6 | -63.29 | -4.20 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.30 | -39.70 | 310 | 12.3 | -43.28 | -9.99 | -46.15 | 330 |
| 52 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.11 | -5.01 | -35.63 | 184 |
| 53 | MACD cross · 1h | trend | 58.13 | -41.87 | 477 | 21.0 | -52.42 | -10.61 | -53.91 | 501 |
| 54 | Agent (ML meta-label) | meta | 57.09 | -42.91 | 2062 | 25.1 | -20.66 | -2.63 | -30.03 | 347 |
| 55 | CCI reversion · 1h | reversion | 56.35 | -43.65 | 442 | 39.1 | -51.40 | -8.82 | -52.54 | 493 |
| 56 | Bollinger reversion · 1h | reversion | 55.77 | -44.23 | 392 | 37.5 | -39.15 | -4.71 | -45.42 | 424 |
| 57 | VWAP momentum · 1h | momentum | 53.93 | -46.08 | 1064 | 21.6 | -58.28 | -13.27 | -59.45 | 1177 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.40 | -8.87 | -53.78 | 679 |
| 59 | Williams %R · 1h | reversion | 50.86 | -49.14 | 509 | 37.7 | -55.12 | -9.00 | -56.39 | 596 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -49.79 | -99.16 | 5386 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.77 | -33.76 | -83.92 | 1429 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.49 | -50.03 | -94.54 | 2443 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.70 | -32.56 | -90.74 | 1921 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.74 | -42.27 | -91.80 | 2256 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.56 | -28.61 | -89.78 | 1963 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -49.53 | -98.19 | 3438 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.01 | -55.57 | -97.02 | 3374 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.09 | -36.89 | -93.17 | 2072 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.21 | -35.58 | -83.27 | 1559 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -57.67 | -99.68 | 6286 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.27 | -39.35 | -93.31 | 2508 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.33 | -36.57 | -94.34 | 3151 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -68.95 | -99.82 | 6130 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.22 | -44.71 | -93.26 | 2274 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.66 | -22.33 | -51.75 | 639 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.98 | -23.79 | -79.17 | 1625 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -59.28 | -97.81 | 3283 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -62.46 | -99.19 | 5134 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.13 | -27.44 | -71.18 | 1207 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.95 | -48.17 | -95.01 | 2683 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.02 | -6.42 | -48.58 | 282 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.42 | -36.96 | -85.65 | 1679 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.99 | -99.77 | 6518 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.53 | -31.27 | -91.65 | 2472 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.82 | -20.23 | -83.20 | 1961 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.79 | -31.79 | -91.95 | 2170 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -50.02 | -98.16 | 4056 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.38 | -48.55 | -90.41 | 2214 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -69.12 | -29.38 | -69.13 | 808 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.09 | -28.44 | -73.29 | 1166 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.94 | -19.23 | -84.31 | 1820 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.03 | -50.43 | -98.06 | 4408 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -104.70 | -99.94 | 8260 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -45.69 | -6.72 | -50.49 | 290 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T18:00 | CCI reversion · 1h | buy | DOGE-USD | 4.03 | — | entry signal |
| 2026-11-24T18:00 | Williams %R · 1h | buy | SOXL | 2.83 | — | rebalance up |
| 2026-11-24T18:00 | Williams %R · 1h | buy | SOL-USD | 5.10 | — | entry signal |
| 2026-11-24T18:00 | Williams %R · 1h | buy | DOGE-USD | 5.10 | — | entry signal |
| 2026-11-24T18:00 | Williams %R · 1h | sell | MSFT | 3.50 | -0.01 | rebalance down |
| 2026-11-24T18:00 | Williams %R · 1h | sell | ETH-USD | 3.45 | -0.03 | rebalance down |
| 2026-11-24T18:00 | Williams %R · 1h | sell | BTC-USD | 3.45 | -0.03 | rebalance down |
| 2026-11-24T18:00 | Williams %R · 1h | sell | AMZN | 3.36 | -0.07 | rebalance down |
| 2026-11-24T18:00 | Bollinger reversion · 1h | buy | ETH-USD | 8.77 | — | entry signal |
| 2026-11-24T18:00 | Bollinger reversion · 1h | sell | XRP-USD | 2.96 | -0.02 | rebalance down |
| 2026-11-24T18:00 | Bollinger reversion · 1h | sell | SOL-USD | 2.87 | -0.04 | rebalance down |
| 2026-11-24T18:00 | Bollinger reversion · 1h | sell | DOGE-USD | 2.94 | -0.02 | rebalance down |
| 2026-11-24T17:55 | Agent | buy | SQQQ | 15.68 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T17:51 | Agent (ML meta-label) | sell | AMD | 8.36 | 0.29 | selected signal exited |
| 2026-11-24T17:35 | Agent | sell | SQQQ | 15.32 | -0.45 | selected signal exited |
| 2026-11-24T17:35 | Opening range 30m | buy | TNA | 8.28 | — | rebalance up |
| 2026-11-24T17:35 | Opening range 30m | buy | MSFT | 4.29 | — | rebalance up |
| 2026-11-24T17:35 | Opening range 30m | buy | IWM | 4.28 | — | rebalance up |
| 2026-11-24T17:35 | Opening range 30m | sell | SQQQ | 20.83 | -0.44 | exit signal |
| 2026-11-24T17:30 | CCI reversion · 1h | buy | SOXL | 4.33 | — | entry signal |
| 2026-11-24T17:30 | Williams %R · 1h | buy | SOXL | 2.24 | — | entry signal |
| 2026-11-24T17:30 | Williams %R · 1h | buy | COIN | 7.29 | — | entry signal |
| 2026-11-24T17:30 | Williams %R · 1h | sell | SQQQ | 2.76 | -0.04 | rebalance down |
| 2026-11-24T17:30 | Stochastic reversion · 1h | buy | COIN | 4.12 | — | entry signal |
| 2026-11-24T17:30 | Stochastic reversion · 1h | buy | AMD | 5.78 | — | entry signal |
| 2026-11-24T17:30 | VWAP reversion · 1h | sell | ETHU | 20.06 | 0.39 | exit signal |
| 2026-11-24T17:30 | Bollinger reversion · 1h | buy | AMD | 13.56 | — | entry signal |
| 2026-11-24T17:30 | Donchian 55/20 · 1h | buy | LABU | 19.00 | — | entry signal |
| 2026-11-24T17:30 | ROC + volume · 1h | buy | SPY | 10.46 | — | entry signal |
| 2026-11-24T17:30 | ROC + volume · 1h | buy | NVDA | 10.47 | — | entry signal |
| 2026-11-24T17:30 | ROC + volume · 1h | sell | TSLA | 4.72 | -0.07 | rebalance down |
| 2026-11-24T17:30 | ROC + volume · 1h | sell | LABU | 5.99 | 0.42 | rebalance down |
| 2026-11-24T17:30 | ROC + volume · 1h | sell | IWM | 4.97 | 0.04 | rebalance down |
| 2026-11-24T17:30 | ROC + volume · 1h | sell | AAPL | 4.90 | 0.02 | rebalance down |
| 2026-11-24T17:30 | VWAP momentum · 1h | buy | TNA | 8.97 | — | entry signal |
| 2026-11-24T17:30 | VWAP momentum · 1h | buy | PLTR | 8.97 | — | entry signal |
| 2026-11-24T17:30 | VWAP momentum · 1h | buy | MSFT | 8.97 | — | entry signal |
| 2026-11-24T17:30 | VWAP momentum · 1h | buy | IWM | 8.97 | — | entry signal |
| 2026-11-24T17:30 | VWAP momentum · 1h | sell | LABU | 5.24 | 0.54 | rebalance down |
| 2026-11-24T17:30 | VWAP momentum · 1h | sell | AAPL | 4.30 | 0.03 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 18:10:05.000124+00:00 -> 2026-11-24 18:20:05.000124+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
