# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T23:10:05.000139+00:00 · 62454 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.11 (-13.89%)

Closed trades 203, win rate 36.5%, fees £5.77, max drawdown -15.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-16 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 33.33 · VIX 23.58 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 41856 decisions in 3660 calls, $0.5205 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T23:10 | 3 / 1 / 1 | cash |  |
| Breezy | 2026-11-16T23:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-16T23:10 | 1 / 4 / 0 | ETH-USD 53% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.82 | +5.11% | 10 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| CCI reversion | SOXL | 2.19 | +16.29% | 10 |
| Bollinger reversion | TSLA | 2.18 | +2.18% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.06 | 18.07 | 0 | — | 13.96 | 4.69 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.81 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.29 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.76 | 3.76 | 0 | — | 5.51 | 1.53 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.52 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.08 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.31 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.64 | -3.36 | 0 | — | -2.59 | -0.81 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.02 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.23 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -1.94 | -0.63 | -8.15 | 157 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.85 | -6.15 | 0 | — | -6.65 | -1.74 | -8.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.78 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.69 | -8.31 | 47 | 42.6 | -10.04 | -2.02 | -14.95 | 62 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.58 | -8.42 | 0 | — | -7.13 | -1.93 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.36 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.99 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -8.38 | -2.36 | -16.01 | 79 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.69 | -13.31 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.10 | -7.03 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.46 | -14.11 | 583 |
| 26 | Parabolic SAR · 1h | trend | 83.37 | -16.63 | 180 | 28.3 | -17.78 | -3.91 | -24.65 | 216 |
| 27 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.21 | -16.78 | 96 |
| 28 | Keltner breakout · 1h | breakout | 80.59 | -19.41 | 121 | 25.6 | -18.84 | -4.24 | -25.84 | 157 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -22.85 | -5.30 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.32 | -19.68 | 213 | 39.9 | -14.21 | -6.29 | -14.88 | 98 |
| 31 | Volume breakout · 1h | breakout | 79.74 | -20.26 | 161 | 28.6 | -16.22 | -5.18 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.71 | -21.37 | 692 |
| 33 | Max aggression: 5-day momentum | meta | 78.12 | -21.88 | 21 | 42.9 | -48.60 | -3.28 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.32 | -22.68 | 2 | 0.0 | -14.56 | -1.79 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 76.35 | -23.65 | 2 | 0.0 | -14.00 | -1.95 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.37 | -31.62 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 74.94 | -25.06 | 30 | 26.7 | -23.41 | -0.85 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.74 | -25.26 | 207 | 19.3 | -26.70 | -4.38 | -34.65 | 256 |
| 39 | Bollinger breakout · 1h | breakout | 74.54 | -25.46 | 184 | 22.3 | -23.57 | -4.96 | -31.78 | 234 |
| 40 | Stochastic reversion · 1h ⏸ | reversion | 74.07 | -25.93 | 333 | 44.1 | -31.66 | -4.69 | -32.87 | 416 |
| 41 | MACD zero-line · 1h | trend | 72.57 | -27.43 | 173 | 18.5 | -24.88 | -4.94 | -31.62 | 195 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -25.69 | -3.67 | -29.26 | 165 |
| 43 | Heikin-Ashi · 1h | trend | 71.79 | -28.21 | 459 | 23.3 | -39.07 | -7.52 | -43.26 | 637 |
| 44 | Supertrend · 1h | trend | 71.69 | -28.31 | 187 | 16.0 | -32.24 | -5.52 | -39.67 | 200 |
| 45 | RSI momentum · 1h | momentum | 71.26 | -28.74 | 175 | 14.3 | -28.00 | -4.59 | -38.07 | 204 |
| 46 | Triple EMA stack · 1h | trend | 71.23 | -28.77 | 154 | 14.9 | -27.92 | -4.99 | -37.77 | 192 |
| 47 | MACD cross · 1h | trend | 71.08 | -28.92 | 402 | 22.6 | -33.63 | -4.87 | -43.17 | 476 |
| 48 | EMA 20/50 cross · 1h | trend | 70.94 | -29.06 | 112 | 9.8 | -35.46 | -9.74 | -38.88 | 113 |
| 49 | ROC + volume · 1h | momentum | 70.75 | -29.25 | 404 | 28.5 | -28.07 | -4.63 | -37.95 | 357 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.94 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.22 | -30.78 | 303 | 19.1 | -29.74 | -5.21 | -39.75 | 261 |
| 52 | CCI reversion · 1h | reversion | 67.93 | -32.07 | 377 | 41.9 | -40.19 | -6.57 | -42.07 | 454 |
| 53 | Donchian 20/10 · 1h | breakout | 67.80 | -32.20 | 157 | 18.5 | -29.96 | -4.94 | -39.25 | 206 |
| 54 | Bollinger reversion · 1h ⏸ | reversion | 66.56 | -33.45 | 333 | 39.0 | -36.36 | -5.53 | -36.96 | 405 |
| 55 | EMA 9/21 cross · 1h | trend | 64.34 | -35.66 | 272 | 11.4 | -36.70 | -6.69 | -44.54 | 321 |
| 56 | Williams %R · 1h | reversion | 64.16 | -35.84 | 418 | 41.1 | -44.23 | -7.48 | -45.12 | 546 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -26.09 | -4.00 | -30.53 | 331 |
| 58 | Z-score reversion · 1h | reversion | 59.61 | -40.39 | 221 | 35.7 | -34.78 | -4.80 | -36.18 | 242 |
| 59 | RSI(14) reversion · 1h | reversion | 59.30 | -40.70 | 204 | 31.9 | -40.74 | -6.04 | -42.17 | 240 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -52.84 | -9.45 | -57.29 | 1209 |
| 61 | Candlestick reversal · 1h ⏸ | reversion | 57.30 | -42.70 | 537 | 27.0 | -45.45 | -8.30 | -45.61 | 616 |
| 62 | Three white soldiers | momentum | 56.57 | -43.43 | 570 | 14.7 | -49.29 | -22.03 | -49.29 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -42.57 | -99.02 | 5302 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.40 | -26.11 | -81.43 | 1433 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.03 | -44.68 | -94.04 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.00 | -32.25 | -90.03 | 1935 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.49 | -41.08 | -91.49 | 2325 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.07 | -30.96 | -90.09 | 2151 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.94 | -48.55 | -97.94 | 3466 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -55.26 | -96.49 | 3440 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.41 | -37.84 | -93.41 | 2258 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.87 | -34.14 | -82.87 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -54.80 | -99.59 | 6044 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.18 | -42.68 | -92.18 | 2584 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.21 | -37.05 | -95.21 | 3356 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.76 | -99.81 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.41 | -43.75 | -92.42 | 2265 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.42 | -26.19 | -76.42 | 1649 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -62.05 | -97.63 | 3470 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -57.34 | -98.98 | 4940 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.55 | -27.50 | -68.55 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -56.81 | -94.72 | 2754 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -38.15 | -84.75 | 1747 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -70.05 | -99.69 | 6379 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.44 | -30.53 | -90.49 | 2336 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.51 | -18.73 | -79.59 | 1813 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.96 | -36.34 | -90.99 | 2180 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.42 | -45.82 | -97.43 | 3904 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -60.63 | -89.22 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -30.06 | -66.40 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.13 | -23.56 | -72.14 | 1248 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.33 | -17.77 | -80.58 | 1754 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -46.70 | -97.56 | 4359 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.32 | -99.94 | 8394 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T23:00 | CCI reversion · 1h | sell | SOL-USD | 13.71 | 0.09 | exit signal |
| 2026-11-16T22:00 | CCI reversion · 1h | sell | BTC-USD | 17.12 | 0.08 | exit signal |
| 2026-11-16T22:00 | RSI(14) reversion · 1h | sell | BTC-USD | 12.34 | -0.01 | exit signal |
| 2026-11-16T22:00 | MACD zero-line · 1h | buy | BTC-USD | 18.17 | — | entry signal |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 7.61 | — | entry signal |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 10.76 | — | entry signal |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 5.38 | -0.00 | rebalance down |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 5.22 | -0.05 | rebalance down |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 5.39 | -0.01 | rebalance down |
| 2026-11-16T21:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 3.26 | — | rebalance up |
| 2026-11-16T21:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 5.64 | -0.06 | exit signal |
| 2026-11-16T20:55 | Agent (rotation) | sell | SQQQ | 31.20 | -0.12 | selected signal exited |
| 2026-11-16T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 101.39 | 0.42 | target is flat |
| 2026-11-16T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 110.78 | -0.43 | target is flat |
| 2026-11-16T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 91.88 | -0.24 | target is flat |
| 2026-11-16T20:55 | Opening range 30m | sell | SQQQ | 21.74 | 0.28 | end-of-day flatten |
| 2026-11-16T20:55 | Opening range 15m | sell | SQQQ | 19.76 | 0.26 | end-of-day flatten |
| 2026-11-16T20:45 | RSI(14) reversion · 1h | sell | LABU | 13.70 | -1.22 | stop-loss |
| 2026-11-16T20:40 | Agent (aggressive) | sell | COIN | 41.62 | -0.09 | selected signal exited |
| 2026-11-16T20:40 | Agent | sell | COIN | 17.12 | -0.04 | selected signal exited |
| 2026-11-16T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 92.12 | — | entry |
| 2026-11-16T20:30 | Williams %R · 1h | buy | COIN | 5.83 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | MSTR | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | LABU | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | BITX | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | AMZN | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | sell | ETHU | 3.05 | 0.01 | rebalance down |
| 2026-11-16T20:30 | RSI(14) reversion · 1h | buy | COIN | 14.89 | — | entry signal |
| 2026-11-16T20:30 | EMA 20/50 cross · 1h | sell | META | 17.70 | -0.19 | exit signal |
| 2026-11-16T20:25 | Three white soldiers | sell | XRP-USD | 14.05 | -0.13 | exit signal |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | TNA | 5.73 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | SOXL | 5.61 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | NVDA | 5.74 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | MSFT | 5.75 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | LABU | 5.73 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | BTC-USD | 5.76 | 0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | BITX | 5.79 | 0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | AMD | 5.71 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:10 | Agent | sell | TSLA | 17.20 | 0.04 | selected signal exited |
| 2026-11-16T20:00 | Agent | sell | SOXL | 17.29 | 0.08 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 23:10:05.000139+00:00 -> 2026-11-16 23:20:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 23:10:05.000139+00:00 -> 2026-11-16 23:20:05.000139+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
