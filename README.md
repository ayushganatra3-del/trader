# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T18:45:05.000107+00:00 · 70870 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.86 (-21.14%)

Closed trades 240, win rate 35.8%, fees £6.50, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 27347 decisions in 2776 calls, $0.3448 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T18:45 | 1 / 14 / 15 | cash |  |
| Breezy | 2026-11-23T18:45 | 0 / 22 / 8 | cash |  |
| Boozy | 2026-11-23T18:45 | 1 / 21 / 8 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.81% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 32.17 | 4.75 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.47 | 15.47 | 0 | — | 13.40 | 4.51 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.25 | 1.33 | -9.74 | 35 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.87 | 3.88 | 0 | — | 2.14 | 0.67 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.89 | -0.18 | -8.71 | 210 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.78 | -3.55 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.97 | -0.23 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.50 | -4.50 | 0 | — | -6.87 | -1.76 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.40 | -3.26 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.20 | -5.49 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.16 | -7.84 | 0 | — | -9.10 | -1.91 | -13.87 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 16 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -4.94 | -3.08 | -8.11 | 30 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.87 | -9.13 | 0 | — | -10.71 | -2.30 | -17.03 | 1 |
| 18 | VWAP reversion · 1h | reversion | 90.55 | -9.45 | 163 | 46.0 | -6.94 | -1.15 | -20.49 | 156 |
| 19 | Copy: Insider buying | copy | 89.28 | -10.72 | 57 | 40.4 | -18.49 | -3.62 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -16.31 | -3.37 | -20.94 | 1 |
| 21 | Opening range 30m | breakout | 86.48 | -13.52 | 457 | 33.3 | -13.15 | -4.38 | -14.52 | 544 |
| 22 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.40 | -13.60 | 9 | 44.4 | -11.32 | -0.63 | -26.65 | 6 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -17.14 | -3.92 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -18.74 | -6.91 | -18.91 | 73 |
| 25 | Connors RSI(2) · 1h | reversion | 81.16 | -18.84 | 219 | 40.6 | -13.60 | -5.78 | -14.96 | 65 |
| 26 | Parabolic SAR · 1h | trend | 80.40 | -19.60 | 203 | 28.1 | -28.05 | -7.51 | -30.19 | 190 |
| 27 | Agent | meta | 78.86 | -21.14 | 240 | 35.8 | -26.00 | -5.64 | -26.43 | 200 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -26.39 | -4.46 | -26.39 | 96 |
| 29 | Opening range 15m | breakout | 77.36 | -22.64 | 567 | 30.9 | -22.72 | -7.01 | -23.54 | 663 |
| 30 | Donchian 55/20 · 1h | breakout | 77.10 | -22.90 | 83 | 12.0 | -28.87 | -7.73 | -29.13 | 84 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.97 | -6.94 | -23.25 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -26.78 | -6.83 | -27.36 | 149 |
| 33 | Ichimoku · 1h | trend | 73.58 | -26.41 | 112 | 15.2 | -30.55 | -8.02 | -31.46 | 105 |
| 34 | Hold BTC | benchmark | 71.36 | -28.64 | 3 | 0.0 | -29.29 | -5.22 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 70.96 | -29.04 | 199 | 16.6 | -34.69 | -6.64 | -38.68 | 218 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.47 | -29.53 | 3 | 0.0 | -24.49 | -2.99 | -32.18 | 1 |
| 37 | Triple EMA stack · 1h | trend | 70.14 | -29.86 | 162 | 14.8 | -36.22 | -9.21 | -38.25 | 166 |
| 38 | EMA 20/50 cross · 1h | trend | 70.04 | -29.96 | 119 | 10.1 | -36.06 | -9.87 | -39.34 | 124 |
| 39 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -36.56 | -6.57 | -39.14 | 282 |
| 40 | Daily: Momentum burst | daily | 69.32 | -30.68 | 30 | 13.3 | -37.71 | -5.38 | -38.52 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.59 | -31.41 | 207 | 22.2 | -33.41 | -8.73 | -34.46 | 213 |
| 42 | OBV trend · 1h | momentum | 67.31 | -32.69 | 320 | 19.7 | -38.34 | -9.81 | -40.20 | 232 |
| 43 | Stochastic reversion · 1h | reversion | 67.01 | -32.99 | 394 | 40.9 | -36.07 | -3.92 | -44.25 | 436 |
| 44 | MACD zero-line · 1h | trend | 65.92 | -34.08 | 198 | 16.7 | -33.88 | -9.06 | -34.07 | 209 |
| 45 | Max aggression: 5-day momentum | meta | 65.56 | -34.44 | 24 | 37.5 | -61.21 | -3.97 | -65.03 | 23 |
| 46 | RSI momentum · 1h | momentum | 65.28 | -34.72 | 188 | 13.8 | -39.36 | -8.86 | -40.74 | 204 |
| 47 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -47.13 | -9.45 | -47.64 | 632 |
| 48 | MFI reversion · 1h | reversion | 63.49 | -36.51 | 486 | 32.9 | -31.84 | -4.60 | -37.45 | 185 |
| 49 | Donchian 20/10 · 1h | breakout | 62.66 | -37.34 | 174 | 16.7 | -39.30 | -8.37 | -40.86 | 193 |
| 50 | ROC + volume · 1h ⏸ | momentum | 61.62 | -38.38 | 451 | 27.1 | -42.33 | -8.51 | -42.33 | 345 |
| 51 | EMA 9/21 cross · 1h | trend | 60.15 | -39.85 | 299 | 11.4 | -45.07 | -10.54 | -46.07 | 328 |
| 52 | Agent (ML meta-label) | meta | 59.84 | -40.16 | 2040 | 25.0 | -21.09 | -2.56 | -32.60 | 317 |
| 53 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -53.64 | -3.87 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 59.06 | -40.94 | 464 | 20.9 | -49.07 | -9.38 | -50.63 | 518 |
| 55 | CCI reversion · 1h | reversion | 58.05 | -41.95 | 430 | 40.0 | -49.52 | -8.25 | -52.02 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 391 | 37.6 | -37.73 | -4.49 | -45.42 | 434 |
| 57 | Williams %R · 1h | reversion | 54.05 | -45.95 | 499 | 38.3 | -54.95 | -9.04 | -56.16 | 594 |
| 58 | VWAP momentum · 1h | momentum | 53.57 | -46.43 | 1051 | 21.8 | -57.92 | -13.23 | -58.43 | 1191 |
| 59 | RSI(14) reversion · 1h | reversion | 51.00 | -49.00 | 240 | 31.7 | -45.30 | -6.65 | -50.33 | 314 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.27 | -8.41 | -53.91 | 687 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -48.12 | -99.14 | 5326 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.90 | -32.77 | -84.52 | 1434 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.51 | -48.37 | -94.52 | 2421 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.91 | -31.47 | -91.09 | 1927 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.87 | -41.37 | -91.90 | 2257 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.49 | -27.61 | -89.56 | 1947 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.14 | -48.01 | -98.14 | 3413 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.99 | -51.18 | -97.00 | 3359 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.74 | -38.22 | -93.74 | 2154 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.26 | -22.44 | -52.27 | 647 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.40 | -34.49 | -83.46 | 1561 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.09 | -99.66 | 6291 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.23 | -39.51 | -93.23 | 2489 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.42 | -35.47 | -94.42 | 3161 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -61.60 | -99.82 | 6119 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.19 | -42.48 | -93.41 | 2262 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.51 | -24.03 | -78.89 | 1613 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -55.14 | -97.79 | 3285 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -57.51 | -99.18 | 5110 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.62 | -27.54 | -70.62 | 1191 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.97 | -48.03 | -94.97 | 2671 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.95 | -6.21 | -48.78 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.65 | -37.07 | -85.65 | 1678 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -69.85 | -99.77 | 6528 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.51 | -29.83 | -91.69 | 2460 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.65 | -19.68 | -82.67 | 1952 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.85 | -29.76 | -92.06 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -47.38 | -98.15 | 4067 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.23 | -46.05 | -90.27 | 2194 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.43 | -29.99 | -68.44 | 796 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.06 | -27.78 | -74.18 | 1168 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.21 | -19.12 | -84.23 | 1846 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.00 | -48.26 | -98.00 | 4436 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -89.77 | -99.94 | 8277 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T18:40 | Donchian 55/20 · 1h | sell | DOGE-USD | 19.24 | -0.48 | stop-loss |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | buy | XRP-USD | 4.74 | — | rebalance up |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | buy | SOL-USD | 4.70 | — | rebalance up |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | buy | BTC-USD | 4.67 | — | rebalance up |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | sell | DOGE-USD | 11.15 | -0.27 | stop-loss |
| 2026-11-23T18:30 | Agent (ML meta-label) | buy | BITX | 10.96 | — | rebalance up |
| 2026-11-23T18:30 | Agent (ML meta-label) | sell | TECL | 14.08 | 0.79 | selected signal exited |
| 2026-11-23T18:30 | Williams %R · 1h | buy | TNA | 2.92 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | SOXL | 3.02 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | MSTR | 3.03 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | MSFT | 2.96 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | ETHU | 3.04 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | COIN | 2.97 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | BITX | 3.06 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | AMZN | 2.92 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | AMD | 2.96 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | AAPL | 2.95 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | sell | TQQQ | 2.46 | -0.04 | exit signal |
| 2026-11-23T18:30 | Williams %R · 1h | sell | TECL | 2.43 | -0.07 | exit signal |
| 2026-11-23T18:30 | Williams %R · 1h | sell | META | 2.53 | 0.03 | exit signal |
| 2026-11-23T18:30 | Williams %R · 1h | sell | IWM | 2.50 | 0.00 | exit signal |
| 2026-11-23T18:30 | Stochastic reversion · 1h | buy | MSTR | 3.48 | — | rebalance up |
| 2026-11-23T18:30 | Stochastic reversion · 1h | buy | ETHU | 3.57 | — | rebalance up |
| 2026-11-23T18:30 | Stochastic reversion · 1h | sell | TECL | 5.23 | 0.08 | exit signal |
| 2026-11-23T18:30 | Stochastic reversion · 1h | sell | IWM | 5.19 | 0.04 | exit signal |
| 2026-11-23T18:30 | VWAP momentum · 1h | buy | UPRO | 3.34 | — | entry signal |
| 2026-11-23T18:30 | VWAP momentum · 1h | buy | QQQ | 4.89 | — | entry signal |
| 2026-11-23T18:30 | VWAP momentum · 1h | buy | AAPL | 4.89 | — | entry signal |
| 2026-11-23T18:30 | VWAP momentum · 1h | sell | TSLA | 5.37 | -0.02 | exit signal |
| 2026-11-23T18:30 | VWAP momentum · 1h | sell | AMD | 5.34 | -0.04 | exit signal |
| 2026-11-23T18:30 | MACD zero-line · 1h | buy | NVDA | 16.50 | — | entry signal |
| 2026-11-23T18:30 | Triple EMA stack · 1h | buy | XRP-USD | 8.11 | — | rebalance up |
| 2026-11-23T18:30 | Triple EMA stack · 1h | sell | SQQQ | 14.70 | 0.56 | exit signal |
| 2026-11-23T18:30 | EMA 9/21 cross · 1h | buy | PLTR | 6.72 | — | entry signal |
| 2026-11-23T18:30 | EMA 9/21 cross · 1h | buy | LABU | 6.72 | — | entry signal |
| 2026-11-23T18:30 | EMA 9/21 cross · 1h | sell | SQQQ | 10.26 | 0.35 | exit signal |
| 2026-11-23T18:30 | EMA 9/21 cross · 1h | sell | SOL-USD | 3.24 | 0.14 | rebalance down |
| 2026-11-23T18:26 | Agent (ML meta-label) | buy | BITX | 4.05 | — | entry |
| 2026-11-23T18:20 | Agent (ML meta-label) | sell | BITX | 4.05 | -0.00 | selected signal exited |
| 2026-11-23T18:20 | Opening range 15m | buy | AAPL | 3.19 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 18:45:05.000107+00:00 -> 2026-11-23 18:55:05.000107+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
