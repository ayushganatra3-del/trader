# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T02:15:05.000133+00:00 · 71261 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.69 (-21.31%)

Closed trades 241, win rate 35.7%, fees £6.52, max drawdown -21.99%.

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

Today: 1815 decisions in 363 calls, $0.0254 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T02:15 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-24T02:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-24T02:15 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.12 | +6.57% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| MFI reversion | SQQQ | 1.67 | +10.14% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.46 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.35 | 15.36 | 0 | — | 12.43 | 4.21 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.99 | 3.99 | 0 | — | 2.66 | 0.79 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.80 | -0.16 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.72 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.95 | -0.23 | -7.48 | 155 |
| 11 | Hold SPY | benchmark | 95.39 | -4.61 | 0 | — | -6.09 | -1.54 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -3.16 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.48 | -7.52 | 0 | — | -8.61 | -1.75 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -4.94 | -3.12 | -8.12 | 30 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.81 | -9.19 | 0 | — | -10.60 | -2.26 | -17.03 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.46 | -10.08 | 25 |
| 18 | Copy: Insider buying | copy | 90.01 | -9.99 | 58 | 39.7 | -17.15 | -3.23 | -22.56 | 68 |
| 19 | VWAP reversion · 1h | reversion | 89.89 | -10.11 | 163 | 46.0 | -7.54 | -1.33 | -20.49 | 157 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -3.27 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.53 | -13.47 | 9 | 44.4 | -10.93 | -0.59 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.35 | -14.39 | 542 |
| 23 | Daily: Bullish score | daily | 85.32 | -14.68 | 20 | 20.0 | -16.45 | -3.76 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -20.94 | -6.96 | -21.47 | 82 |
| 25 | Connors RSI(2) · 1h | reversion | 80.43 | -19.57 | 220 | 40.9 | -14.29 | -6.30 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.23 | -19.77 | 204 | 28.4 | -28.24 | -7.57 | -30.34 | 190 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -25.94 | -5.59 | -26.54 | 196 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -24.76 | -4.13 | -25.84 | 91 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -22.46 | -6.92 | -23.30 | 660 |
| 30 | Donchian 55/20 · 1h | breakout | 76.75 | -23.25 | 85 | 14.1 | -29.31 | -7.66 | -29.80 | 84 |
| 31 | Volume breakout · 1h | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.88 | -6.97 | -23.25 | 72 |
| 32 | Keltner breakout · 1h | breakout | 75.67 | -24.33 | 137 | 24.8 | -23.99 | -6.28 | -24.86 | 142 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.92 | -31.19 | 102 |
| 34 | Hold BTC | benchmark | 70.82 | -29.18 | 3 | 0.0 | -29.86 | -5.31 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 70.82 | -29.18 | 204 | 18.6 | -35.18 | -6.80 | -39.07 | 211 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.37 | -29.63 | 3 | 0.0 | -23.26 | -2.81 | -32.18 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.67 | -30.33 | 252 | 19.0 | -37.74 | -6.72 | -40.30 | 279 |
| 38 | Triple EMA stack · 1h | trend | 69.32 | -30.68 | 166 | 15.1 | -37.59 | -9.45 | -38.80 | 169 |
| 39 | Daily: Momentum burst | daily | 69.16 | -30.84 | 30 | 13.3 | -37.24 | -5.32 | -37.81 | 25 |
| 40 | EMA 20/50 cross · 1h | trend | 69.14 | -30.86 | 119 | 10.1 | -37.46 | -10.26 | -39.34 | 117 |
| 41 | Bollinger breakout · 1h | breakout | 68.64 | -31.36 | 207 | 22.2 | -32.73 | -8.52 | -33.88 | 211 |
| 42 | OBV trend · 1h | momentum | 66.80 | -33.20 | 321 | 19.9 | -39.43 | -9.99 | -40.76 | 233 |
| 43 | Stochastic reversion · 1h | reversion | 66.74 | -33.26 | 394 | 40.9 | -32.66 | -3.45 | -42.70 | 432 |
| 44 | MACD zero-line · 1h | trend | 65.86 | -34.14 | 198 | 16.7 | -35.07 | -9.50 | -35.51 | 206 |
| 45 | RSI momentum · 1h | momentum | 65.03 | -34.97 | 196 | 15.3 | -39.40 | -8.77 | -40.99 | 201 |
| 46 | Heikin-Ashi · 1h | trend | 64.61 | -35.39 | 526 | 22.2 | -46.88 | -9.47 | -47.76 | 630 |
| 47 | Max aggression: 5-day momentum | meta | 64.11 | -35.89 | 25 | 36.0 | -62.02 | -4.00 | -65.90 | 23 |
| 48 | MFI reversion · 1h | reversion | 63.64 | -36.36 | 486 | 32.9 | -32.13 | -4.63 | -37.87 | 185 |
| 49 | Donchian 20/10 · 1h | breakout | 61.87 | -38.13 | 178 | 18.0 | -39.62 | -8.40 | -41.33 | 193 |
| 50 | ROC + volume · 1h | momentum | 61.61 | -38.39 | 452 | 27.0 | -42.81 | -8.55 | -42.92 | 343 |
| 51 | EMA 9/21 cross · 1h | trend | 59.80 | -40.20 | 303 | 12.2 | -44.46 | -10.36 | -45.52 | 334 |
| 52 | Agent (ML meta-label) | meta | 59.60 | -40.40 | 2049 | 25.0 | -17.77 | -2.05 | -29.44 | 330 |
| 53 | Max aggression: 1-day momentum | meta | 59.16 | -40.84 | 34 | 26.5 | -52.64 | -3.83 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 58.89 | -41.11 | 467 | 21.4 | -49.27 | -9.39 | -51.01 | 516 |
| 55 | CCI reversion · 1h | reversion | 58.08 | -41.92 | 430 | 40.0 | -49.26 | -8.09 | -51.92 | 498 |
| 56 | Bollinger reversion · 1h | reversion | 57.95 | -42.05 | 391 | 37.6 | -37.41 | -4.42 | -45.42 | 430 |
| 57 | Williams %R · 1h | reversion | 53.99 | -46.01 | 500 | 38.4 | -53.61 | -8.64 | -55.78 | 584 |
| 58 | VWAP momentum · 1h | momentum | 53.51 | -46.49 | 1054 | 21.8 | -57.82 | -13.16 | -58.29 | 1183 |
| 59 | RSI(14) reversion · 1h | reversion | 51.00 | -49.00 | 241 | 32.0 | -49.66 | -7.83 | -52.23 | 285 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -50.81 | -8.33 | -54.24 | 661 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -46.76 | -99.12 | 5324 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.94 | -32.93 | -84.38 | 1434 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.47 | -47.31 | -94.47 | 2434 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.66 | -31.76 | -90.69 | 1910 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.79 | -41.02 | -91.79 | 2252 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.63 | -27.76 | -89.69 | 1963 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -47.25 | -98.18 | 3430 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.03 | -51.55 | -97.03 | 3376 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -37.56 | -93.56 | 2118 |
| 70 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.31 | -34.10 | -83.32 | 1554 |
| 71 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -54.06 | -99.68 | 6293 |
| 72 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.25 | -37.96 | -93.26 | 2493 |
| 73 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.47 | -35.53 | -94.47 | 3179 |
| 74 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -62.96 | -99.83 | 6145 |
| 75 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.26 | -43.43 | -93.30 | 2271 |
| 76 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.86 | -22.28 | -51.86 | 642 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.21 | -23.85 | -78.30 | 1608 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -53.92 | -97.77 | 3282 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -57.04 | -99.19 | 5123 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.13 | -27.31 | -71.16 | 1201 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.00 | -47.25 | -95.01 | 2671 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.79 | -6.17 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.41 | -36.56 | -85.45 | 1666 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -68.90 | -99.77 | 6546 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.60 | -30.31 | -91.69 | 2472 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.16 | -20.09 | -83.16 | 1954 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.06 | -30.88 | -92.07 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -47.35 | -98.14 | 4055 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.36 | -46.51 | -90.36 | 2195 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.07 | -29.40 | -68.14 | 791 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.41 | -27.83 | -73.43 | 1163 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.68 | -19.20 | -84.68 | 1837 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.98 | -47.15 | -97.99 | 4410 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.96 | -99.94 | 8292 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T02:00 | ROC + volume · 1h | sell | DOGE-USD | 10.26 | -0.01 | exit signal |
| 2026-11-24T02:00 | Supertrend · 1h | sell | BTC-USD | 2.91 | 0.10 | exit signal |
| 2026-11-24T02:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 7.48 | — | entry signal |
| 2026-11-24T02:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 6.52 | 0.12 | exit signal |
| 2026-11-24T01:50 | Three white soldiers | sell | DOGE-USD | 12.47 | -0.09 | exit signal |
| 2026-11-24T01:20 | Three white soldiers | buy | DOGE-USD | 12.56 | — | entry |
| 2026-11-24T01:00 | Stochastic reversion · 1h | buy | DOGE-USD | 1.96 | — | entry signal |
| 2026-11-24T01:00 | Triple EMA stack · 1h | sell | SOL-USD | 17.32 | 0.13 | exit signal |
| 2026-11-24T01:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 7.78 | -0.55 | exit signal |
| 2026-11-24T00:00 | Max aggression: 5-day momentum | buy | SOL-USD | 64.49 | — | entry |
| 2026-11-24T00:00 | Williams %R · 1h | buy | DOGE-USD | 5.44 | — | entry signal |
| 2026-11-24T00:00 | Donchian 55/20 · 1h | buy | XRP-USD | 19.20 | — | entry |
| 2026-11-24T00:00 | Donchian 55/20 · 1h | buy | SOL-USD | 19.20 | — | entry |
| 2026-11-24T00:00 | Donchian 20/10 · 1h | buy | XRP-USD | 15.51 | — | entry |
| 2026-11-24T00:00 | Donchian 20/10 · 1h | buy | SOL-USD | 15.51 | — | entry |
| 2026-11-24T00:00 | Donchian 20/10 · 1h | buy | BTC-USD | 15.51 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | XRP-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | SOL-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | DOGE-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | BTC-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | ROC + volume · 1h | buy | DOGE-USD | 10.27 | — | entry |
| 2026-11-24T00:00 | ADX DI cross · 1h | buy | BTC-USD | 5.36 | — | entry |
| 2026-11-24T00:00 | Triple EMA stack · 1h | sell | XRP-USD | 17.28 | -0.17 | exit signal |
| 2026-11-24T00:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 7.37 | 0.07 | exit signal |
| 2026-11-24T00:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 7.51 | 0.03 | exit signal |
| 2026-11-23T23:35 | Three white soldiers | sell | BTC-USD | 12.49 | -0.08 | exit signal |
| 2026-11-23T23:05 | Three white soldiers | buy | BTC-USD | 12.58 | — | entry signal |
| 2026-11-23T23:00 | Parabolic SAR · 1h | sell | DOGE-USD | 13.08 | -0.09 | exit signal |
| 2026-11-23T23:00 | Supertrend · 1h | sell | DOGE-USD | 2.87 | 0.04 | exit signal |
| 2026-11-23T23:00 | Triple EMA stack · 1h | buy | XRP-USD | 3.47 | — | rebalance up |
| 2026-11-23T23:00 | Triple EMA stack · 1h | buy | SOL-USD | 5.16 | — | rebalance up |
| 2026-11-23T23:00 | Triple EMA stack · 1h | buy | DOGE-USD | 5.01 | — | rebalance up |
| 2026-11-23T23:00 | Triple EMA stack · 1h | sell | ETH-USD | 12.12 | -0.07 | exit signal |
| 2026-11-23T23:00 | Triple EMA stack · 1h | sell | BTC-USD | 12.16 | -0.02 | exit signal |
| 2026-11-23T22:00 | Stochastic reversion · 1h | buy | XRP-USD | 7.42 | — | entry signal |
| 2026-11-23T21:00 | Stochastic reversion · 1h | buy | BTC-USD | 8.35 | — | entry signal |
| 2026-11-23T21:00 | OBV trend · 1h | sell | SOL-USD | 14.15 | 0.27 | exit signal |
| 2026-11-23T21:00 | Supertrend · 1h | sell | SOL-USD | 2.88 | 0.08 | exit signal |
| 2026-11-23T21:00 | Supertrend · 1h | sell | ETH-USD | 2.92 | 0.12 | exit signal |
| 2026-11-23T21:00 | MACD cross · 1h | sell | DOGE-USD | 4.47 | 0.07 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 02:15:05.000133+00:00 -> 2026-11-24 02:25:05.000133+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
