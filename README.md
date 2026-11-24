# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T04:15:05.000139+00:00 · 71372 ticks

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

Today: 3480 decisions in 696 calls, $0.0487 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T04:15 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-24T04:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-24T04:15 | 5 / 0 / 0 | ETH-USD 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| MFI reversion | SQQQ | 1.67 | +10.14% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.35 | 15.35 | 0 | — | 12.43 | 4.42 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 0.77 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.97 | 3.97 | 0 | — | 2.64 | 1.06 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.10 | 0.06 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.75 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.07 | 0.06 | -7.48 | 149 |
| 11 | Hold SPY | benchmark | 95.39 | -4.61 | 0 | — | -6.09 | -1.50 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -2.88 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.48 | -7.52 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -4.94 | -3.15 | -8.12 | 30 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.81 | -9.19 | 0 | — | -10.60 | -2.27 | -17.03 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Insider buying | copy | 90.01 | -9.99 | 58 | 39.7 | -17.15 | -3.25 | -22.56 | 68 |
| 19 | VWAP reversion · 1h | reversion | 89.89 | -10.11 | 163 | 46.0 | -7.93 | -1.41 | -20.49 | 158 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -2.99 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.53 | -13.47 | 9 | 44.4 | -10.93 | -0.60 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.39 | -14.39 | 542 |
| 23 | Daily: Bullish score | daily | 85.32 | -14.68 | 20 | 20.0 | -16.45 | -3.46 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.09 | -7.04 | -21.84 | 82 |
| 25 | Parabolic SAR · 1h | trend | 80.22 | -19.77 | 204 | 28.4 | -28.25 | -7.64 | -30.34 | 190 |
| 26 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.80 | -6.59 | -14.96 | 66 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -25.58 | -5.78 | -25.97 | 195 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.11 | -4.19 | -18.44 | 88 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -22.04 | -6.77 | -23.30 | 660 |
| 30 | Volume breakout · 1h | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.88 | -7.04 | -23.25 | 72 |
| 31 | Donchian 55/20 · 1h | breakout | 76.51 | -23.49 | 86 | 14.0 | -29.50 | -7.80 | -30.05 | 84 |
| 32 | Keltner breakout · 1h | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.35 | -6.46 | -25.21 | 143 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.99 | -31.19 | 102 |
| 34 | Supertrend · 1h | trend | 70.82 | -29.18 | 204 | 18.6 | -35.13 | -6.85 | -39.07 | 211 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 70.37 | -29.63 | 3 | 0.0 | -23.26 | -2.75 | -32.18 | 1 |
| 36 | Hold BTC | benchmark | 70.15 | -29.85 | 3 | 0.0 | -30.76 | -5.11 | -36.14 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.58 | -30.42 | 253 | 19.0 | -38.00 | -6.87 | -40.45 | 280 |
| 38 | Daily: Momentum burst | daily | 69.16 | -30.84 | 30 | 13.3 | -37.24 | -5.04 | -37.81 | 25 |
| 39 | Triple EMA stack · 1h | trend | 69.05 | -30.95 | 167 | 15.6 | -38.01 | -9.67 | -38.74 | 169 |
| 40 | EMA 20/50 cross · 1h | trend | 68.72 | -31.28 | 120 | 10.0 | -37.70 | -10.49 | -39.47 | 118 |
| 41 | Bollinger breakout · 1h | breakout | 68.64 | -31.36 | 207 | 22.2 | -32.73 | -8.61 | -33.88 | 211 |
| 42 | OBV trend · 1h | momentum | 66.71 | -33.29 | 321 | 19.9 | -39.72 | -10.22 | -40.78 | 233 |
| 43 | Stochastic reversion · 1h | reversion | 66.64 | -33.36 | 395 | 40.8 | -33.02 | -3.53 | -42.70 | 432 |
| 44 | MACD zero-line · 1h | trend | 65.86 | -34.14 | 198 | 16.7 | -34.96 | -9.56 | -35.37 | 205 |
| 45 | RSI momentum · 1h | momentum | 64.69 | -35.31 | 198 | 15.2 | -40.30 | -9.34 | -41.18 | 201 |
| 46 | Heikin-Ashi · 1h | trend | 64.61 | -35.39 | 526 | 22.2 | -46.88 | -9.54 | -47.76 | 630 |
| 47 | Max aggression: 5-day momentum | meta | 63.89 | -36.11 | 25 | 36.0 | -62.15 | -4.05 | -66.45 | 23 |
| 48 | MFI reversion · 1h | reversion | 63.64 | -36.36 | 486 | 32.9 | -32.31 | -4.70 | -37.87 | 185 |
| 49 | ROC + volume · 1h | momentum | 61.61 | -38.39 | 452 | 27.0 | -42.98 | -8.62 | -43.12 | 342 |
| 50 | Donchian 20/10 · 1h | breakout | 61.40 | -38.60 | 180 | 17.8 | -40.07 | -8.62 | -41.86 | 193 |
| 51 | EMA 9/21 cross · 1h | trend | 59.66 | -40.34 | 304 | 12.2 | -44.69 | -10.56 | -45.71 | 334 |
| 52 | Agent (ML meta-label) | meta | 59.60 | -40.40 | 2049 | 25.0 | -20.90 | -2.71 | -30.61 | 319 |
| 53 | Max aggression: 1-day momentum | meta | 59.16 | -40.84 | 34 | 26.5 | -52.65 | -3.86 | -54.72 | 38 |
| 54 | MACD cross · 1h | trend | 58.89 | -41.11 | 467 | 21.4 | -49.62 | -9.62 | -50.69 | 510 |
| 55 | CCI reversion · 1h | reversion | 58.08 | -41.92 | 430 | 40.0 | -49.26 | -8.17 | -51.92 | 498 |
| 56 | Bollinger reversion · 1h | reversion | 57.95 | -42.05 | 391 | 37.6 | -37.42 | -4.46 | -45.42 | 430 |
| 57 | Williams %R · 1h | reversion | 53.94 | -46.06 | 500 | 38.4 | -53.58 | -8.70 | -55.78 | 584 |
| 58 | VWAP momentum · 1h | momentum | 53.51 | -46.49 | 1054 | 21.8 | -57.91 | -13.35 | -58.29 | 1183 |
| 59 | RSI(14) reversion · 1h | reversion | 51.00 | -49.00 | 241 | 32.0 | -49.91 | -7.98 | -52.23 | 291 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.05 | -8.80 | -54.76 | 669 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -48.07 | -99.11 | 5326 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.98 | -33.33 | -84.38 | 1435 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.45 | -48.60 | -94.46 | 2432 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.63 | -31.74 | -90.65 | 1913 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.76 | -41.07 | -91.77 | 2252 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.64 | -28.53 | -89.70 | 1963 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -47.55 | -98.18 | 3433 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.99 | -52.22 | -96.99 | 3382 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -38.79 | -93.70 | 2130 |
| 70 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.31 | -34.82 | -83.33 | 1555 |
| 71 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -54.90 | -99.68 | 6298 |
| 72 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.17 | -38.10 | -93.17 | 2492 |
| 73 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.47 | -36.88 | -94.47 | 3179 |
| 74 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -63.21 | -99.83 | 6147 |
| 75 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.24 | -43.64 | -93.28 | 2271 |
| 76 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.89 | -22.15 | -51.89 | 642 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.29 | -23.72 | -78.29 | 1600 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -56.87 | -97.77 | 3282 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -57.75 | -99.20 | 5126 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.34 | -27.24 | -71.34 | 1203 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.98 | -47.23 | -94.98 | 2669 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.79 | -6.22 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.30 | -36.31 | -85.30 | 1662 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -69.99 | -99.77 | 6552 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.53 | -30.14 | -91.59 | 2473 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.42 | -19.83 | -83.51 | 1963 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.99 | -30.53 | -92.02 | 2170 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.17 | -48.02 | -98.18 | 4061 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.26 | -46.36 | -90.26 | 2192 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.82 | -29.86 | -67.82 | 788 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.36 | -28.05 | -73.36 | 1163 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.90 | -18.75 | -85.05 | 1846 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.01 | -48.14 | -98.03 | 4417 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -92.09 | -99.94 | 8287 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-24T00:00 | RSI momentum · 1h | buy | XRP-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | SOL-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | DOGE-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | BTC-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | ROC + volume · 1h | buy | DOGE-USD | 10.27 | — | entry |
| 2026-11-24T00:00 | ADX DI cross · 1h | buy | BTC-USD | 5.36 | — | entry |
| 2026-11-24T00:00 | Triple EMA stack · 1h | sell | XRP-USD | 17.28 | -0.17 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 04:15:05.000139+00:00 -> 2026-11-24 04:25:05.000139+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
