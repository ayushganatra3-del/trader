# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T06:15:05.000130+00:00 · 71468 ticks

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

Today: 4920 decisions in 984 calls, $0.0688 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T06:15 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-24T06:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-24T06:15 | 0 / 5 / 0 | cash |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.36 | 15.36 | 0 | — | 12.43 | 4.42 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 0.77 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.00 | 4.00 | 0 | — | 2.66 | 1.07 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.51 | -0.07 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.75 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.20 | 0.02 | -7.48 | 149 |
| 11 | Hold SPY | benchmark | 95.40 | -4.60 | 0 | — | -6.09 | -1.50 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -2.88 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.48 | -7.52 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -4.94 | -3.15 | -8.12 | 30 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.81 | -9.19 | 0 | — | -10.60 | -2.27 | -17.03 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Insider buying | copy | 90.02 | -9.98 | 58 | 39.7 | -8.96 | -1.74 | -14.79 | 68 |
| 19 | VWAP reversion · 1h | reversion | 89.89 | -10.11 | 163 | 46.0 | -7.59 | -1.38 | -20.49 | 154 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -2.99 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.53 | -13.46 | 9 | 44.4 | -10.93 | -0.60 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.39 | -14.39 | 542 |
| 23 | Daily: Bullish score | daily | 85.32 | -14.68 | 20 | 20.0 | -16.45 | -3.46 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.68 | -7.30 | -21.86 | 81 |
| 25 | Parabolic SAR · 1h | trend | 80.23 | -19.77 | 204 | 28.4 | -28.24 | -7.64 | -30.34 | 190 |
| 26 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.80 | -6.59 | -14.96 | 66 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -26.13 | -5.69 | -26.52 | 195 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -25.30 | -4.28 | -25.84 | 91 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -22.46 | -6.90 | -23.30 | 660 |
| 30 | Donchian 55/20 · 1h | breakout | 76.57 | -23.43 | 86 | 14.0 | -29.65 | -7.86 | -29.99 | 84 |
| 31 | Volume breakout · 1h | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.88 | -7.04 | -23.25 | 72 |
| 32 | Keltner breakout · 1h | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.04 | -6.35 | -24.91 | 143 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.99 | -31.19 | 102 |
| 34 | Supertrend · 1h | trend | 70.82 | -29.18 | 204 | 18.6 | -34.62 | -6.86 | -37.07 | 206 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 70.38 | -29.62 | 3 | 0.0 | -23.26 | -2.75 | -32.18 | 1 |
| 36 | Hold BTC | benchmark | 70.25 | -29.75 | 3 | 0.0 | -30.26 | -5.09 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.58 | -30.42 | 253 | 19.0 | -37.81 | -6.80 | -40.30 | 279 |
| 38 | Daily: Momentum burst | daily | 69.16 | -30.84 | 30 | 13.3 | -37.24 | -5.04 | -37.81 | 25 |
| 39 | Triple EMA stack · 1h | trend | 68.94 | -31.06 | 167 | 15.6 | -38.21 | -9.81 | -38.57 | 171 |
| 40 | EMA 20/50 cross · 1h | trend | 68.90 | -31.10 | 120 | 10.0 | -37.60 | -10.41 | -39.66 | 118 |
| 41 | Bollinger breakout · 1h | breakout | 68.64 | -31.36 | 207 | 22.2 | -32.55 | -8.54 | -33.70 | 211 |
| 42 | OBV trend · 1h | momentum | 66.88 | -33.12 | 321 | 19.9 | -39.40 | -10.07 | -40.75 | 233 |
| 43 | Stochastic reversion · 1h | reversion | 66.72 | -33.28 | 395 | 40.8 | -33.41 | -3.59 | -42.70 | 432 |
| 44 | MACD zero-line · 1h | trend | 65.87 | -34.13 | 198 | 16.7 | -35.25 | -9.66 | -35.53 | 206 |
| 45 | RSI momentum · 1h | momentum | 64.83 | -35.17 | 198 | 15.2 | -39.89 | -9.15 | -41.28 | 201 |
| 46 | Heikin-Ashi · 1h | trend | 64.58 | -35.42 | 526 | 22.2 | -46.91 | -9.55 | -47.76 | 631 |
| 47 | Max aggression: 5-day momentum | meta | 63.97 | -36.03 | 25 | 36.0 | -62.11 | -4.04 | -66.45 | 23 |
| 48 | MFI reversion · 1h | reversion | 63.64 | -36.36 | 486 | 32.9 | -32.31 | -4.70 | -37.87 | 186 |
| 49 | ROC + volume · 1h | momentum | 61.61 | -38.39 | 452 | 27.0 | -42.98 | -8.62 | -43.13 | 342 |
| 50 | Donchian 20/10 · 1h | breakout | 61.44 | -38.56 | 180 | 17.8 | -40.03 | -8.61 | -41.86 | 193 |
| 51 | EMA 9/21 cross · 1h | trend | 59.61 | -40.39 | 305 | 12.5 | -44.77 | -10.59 | -45.71 | 336 |
| 52 | Agent (ML meta-label) | meta | 59.60 | -40.40 | 2049 | 25.0 | -16.67 | -1.90 | -28.61 | 326 |
| 53 | Max aggression: 1-day momentum | meta | 59.16 | -40.84 | 34 | 26.5 | -52.64 | -3.86 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 58.89 | -41.11 | 467 | 21.4 | -49.99 | -9.78 | -51.09 | 512 |
| 55 | CCI reversion · 1h | reversion | 58.08 | -41.92 | 430 | 40.0 | -49.28 | -8.18 | -51.92 | 501 |
| 56 | Bollinger reversion · 1h | reversion | 57.95 | -42.05 | 391 | 37.6 | -37.41 | -4.46 | -45.42 | 430 |
| 57 | Williams %R · 1h | reversion | 53.98 | -46.02 | 500 | 38.4 | -53.70 | -8.75 | -55.78 | 589 |
| 58 | VWAP momentum · 1h | momentum | 53.51 | -46.49 | 1054 | 21.8 | -57.99 | -13.38 | -58.29 | 1187 |
| 59 | RSI(14) reversion · 1h | reversion | 51.01 | -48.99 | 241 | 32.0 | -49.89 | -7.97 | -52.23 | 292 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.80 | -8.71 | -54.59 | 668 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -48.41 | -99.12 | 5328 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.02 | -33.45 | -84.38 | 1438 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.47 | -48.97 | -94.48 | 2436 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.61 | -31.66 | -90.65 | 1914 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.81 | -41.45 | -91.82 | 2256 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.65 | -28.56 | -89.72 | 1964 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -47.49 | -98.18 | 3433 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.02 | -52.39 | -97.02 | 3386 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -39.15 | -93.61 | 2120 |
| 70 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.32 | -34.84 | -83.33 | 1555 |
| 71 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -54.70 | -99.68 | 6293 |
| 72 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.23 | -38.09 | -93.23 | 2495 |
| 73 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.47 | -36.89 | -94.47 | 3179 |
| 74 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -64.18 | -99.83 | 6146 |
| 75 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.29 | -44.14 | -93.29 | 2275 |
| 76 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.71 | -22.17 | -51.71 | 641 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.31 | -23.85 | -78.32 | 1602 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -57.85 | -97.78 | 3286 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -57.99 | -99.19 | 5123 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.13 | -27.24 | -71.16 | 1201 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.98 | -47.52 | -94.98 | 2669 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.79 | -6.22 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.45 | -37.04 | -85.45 | 1666 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -70.03 | -99.77 | 6547 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.42 | -30.11 | -91.49 | 2468 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.25 | -19.84 | -83.33 | 1958 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.92 | -31.05 | -91.94 | 2161 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -48.09 | -98.16 | 4058 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.32 | -47.27 | -90.32 | 2196 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.97 | -30.24 | -67.97 | 790 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.50 | -28.01 | -73.51 | 1164 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.63 | -18.76 | -84.79 | 1841 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.99 | -48.19 | -98.00 | 4411 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -95.03 | -99.94 | 8289 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T06:00 | Heikin-Ashi · 1h | buy | XRP-USD | 4.61 | — | entry signal |
| 2026-11-24T06:00 | Triple EMA stack · 1h | buy | DOGE-USD | 17.28 | — | entry signal |
| 2026-11-24T06:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 7.46 | — | entry signal |
| 2026-11-24T05:00 | CCI reversion · 1h | buy | ETH-USD | 2.53 | — | entry signal |
| 2026-11-24T05:00 | Triple EMA stack · 1h | buy | XRP-USD | 17.26 | — | entry signal |
| 2026-11-24T05:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 8.53 | — | entry signal |
| 2026-11-24T05:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 7.39 | 0.12 | exit signal |
| 2026-11-24T04:00 | Triple EMA stack · 1h | sell | DOGE-USD | 17.22 | 0.05 | exit signal |
| 2026-11-24T03:10 | Stochastic reversion · 1h | buy | ETH-USD | 3.96 | — | entry |
| 2026-11-24T03:10 | Stochastic reversion · 1h | buy | DOGE-USD | 4.12 | — | rebalance up |
| 2026-11-24T03:10 | Stochastic reversion · 1h | sell | BTC-USD | 8.08 | -0.27 | stop-loss |
| 2026-11-24T03:10 | Connors RSI(2) · 1h | sell | SOL-USD | 19.37 | -0.94 | stop-loss |
| 2026-11-24T03:10 | EMA 20/50 cross · 1h | buy | XRP-USD | 6.31 | — | rebalance up |
| 2026-11-24T03:10 | EMA 20/50 cross · 1h | buy | DOGE-USD | 4.88 | — | rebalance up |
| 2026-11-24T03:10 | EMA 20/50 cross · 1h | sell | ETH-USD | 14.13 | -0.38 | stop-loss |
| 2026-11-24T03:00 | Donchian 55/20 · 1h | sell | SOL-USD | 18.77 | -0.43 | exit signal |
| 2026-11-24T03:00 | Donchian 20/10 · 1h | sell | SOL-USD | 15.16 | -0.34 | exit signal |
| 2026-11-24T03:00 | Donchian 20/10 · 1h | sell | BTC-USD | 15.10 | -0.41 | exit signal |
| 2026-11-24T03:00 | RSI momentum · 1h | buy | XRP-USD | 3.64 | — | rebalance up |
| 2026-11-24T03:00 | RSI momentum · 1h | buy | DOGE-USD | 3.71 | — | rebalance up |
| 2026-11-24T03:00 | RSI momentum · 1h | sell | SOL-USD | 9.09 | -0.21 | exit signal |
| 2026-11-24T03:00 | RSI momentum · 1h | sell | BTC-USD | 9.06 | -0.24 | exit signal |
| 2026-11-24T03:00 | ADX DI cross · 1h | sell | BTC-USD | 5.22 | -0.14 | exit signal |
| 2026-11-24T03:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 7.39 | -0.09 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 06:15:05.000130+00:00 -> 2026-11-24 06:25:05.000130+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
