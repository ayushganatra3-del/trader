# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T15:20:05.000131+00:00 · 67010 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £81.93 (-18.07%)

Closed trades 235, win rate 36.6%, fees £6.36, max drawdown -18.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-20 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.48 · VIX 28.44 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 15564 decisions in 2391 calls, $0.2079 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T15:20 | 1 / 3 / 27 | cash |  |
| Breezy | 2026-11-20T15:20 | 0 / 19 / 12 | cash |  |
| Boozy | 2026-11-20T15:20 | 3 / 17 / 11 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| CCI reversion | SOXL | 1.96 | +18.20% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.75 | 21.75 | 26 | 65.4 | 24.79 | 4.05 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.08 | 15.08 | 0 | — | 13.09 | 4.37 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.20 | 3.20 | 0 | — | 4.31 | 1.24 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 40 | 42.5 | -2.13 | -0.35 | -9.74 | 35 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.22 | -0.78 | 159 | 34.6 | -4.44 | -3.92 | -5.02 | 75 |
| 9 | Gap and go | momentum | 97.84 | -2.16 | 203 | 31.5 | -1.27 | -0.34 | -9.06 | 202 |
| 10 | Agent (rotation) | meta | 95.39 | -4.61 | 212 | 28.8 | -1.53 | -0.46 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 93.35 | -6.64 | 0 | — | -7.59 | -2.58 | -8.98 | 1 |
| 14 | Trend pullback · 1h | trend | 91.16 | -8.84 | 115 | 23.5 | -8.63 | -4.88 | -11.21 | 43 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.12 | -8.88 | 0 | — | -9.14 | -2.40 | -10.09 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 17 | Copy: Insider buying | copy | 89.83 | -10.17 | 55 | 40.0 | -5.78 | -1.07 | -14.79 | 66 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.35 | -10.65 | 0 | — | -11.22 | -3.16 | -14.12 | 1 |
| 19 | VWAP reversion · 1h | reversion | 89.15 | -10.85 | 156 | 45.5 | -12.93 | -3.82 | -18.48 | 149 |
| 20 | Daily: Bullish score | daily | 88.64 | -11.36 | 19 | 15.8 | -13.54 | -3.52 | -19.56 | 14 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 88.62 | -11.38 | 8 | 50.0 | -12.62 | -1.07 | -19.29 | 6 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.61 | -18.94 | 71 |
| 24 | Opening range 30m | breakout | 85.23 | -14.78 | 451 | 33.5 | -12.75 | -4.23 | -14.87 | 552 |
| 25 | Parabolic SAR · 1h | trend | 82.60 | -17.40 | 194 | 27.8 | -25.87 | -7.71 | -28.86 | 196 |
| 26 | Agent | meta | 81.93 | -18.07 | 235 | 36.6 | -16.88 | -6.50 | -17.09 | 205 |
| 27 | Connors RSI(2) · 1h | reversion | 80.07 | -19.93 | 218 | 40.4 | -15.51 | -6.99 | -15.67 | 71 |
| 28 | Agent (aggressive) | meta | 79.74 | -20.26 | 108 | 33.3 | -18.85 | -4.55 | -19.15 | 96 |
| 29 | Donchian 55/20 · 1h | breakout | 79.74 | -20.26 | 79 | 12.7 | -26.43 | -8.22 | -27.74 | 82 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.48 | -5.37 | -21.55 | 73 |
| 31 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.50 | -6.24 | -25.33 | 143 |
| 32 | Opening range 15m | breakout | 76.19 | -23.80 | 558 | 31.2 | -22.38 | -6.88 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 74.76 | -25.24 | 107 | 14.0 | -29.72 | -8.90 | -32.08 | 109 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 73.98 | -26.02 | 2 | 0.0 | -24.81 | -3.60 | -28.95 | 1 |
| 35 | ADX DI cross · 1h | trend | 73.54 | -26.46 | 226 | 20.4 | -26.00 | -3.90 | -35.87 | 272 |
| 36 | Triple EMA stack · 1h | trend | 71.18 | -28.82 | 161 | 14.3 | -34.57 | -9.00 | -36.46 | 170 |
| 37 | Bollinger breakout · 1h | breakout | 71.07 | -28.93 | 195 | 21.5 | -32.90 | -8.82 | -36.32 | 217 |
| 38 | Supertrend · 1h | trend | 70.95 | -29.05 | 198 | 16.7 | -32.39 | -5.41 | -39.16 | 203 |
| 39 | Hold BTC | benchmark | 70.81 | -29.19 | 2 | 0.0 | -26.66 | -4.29 | -31.02 | 1 |
| 40 | EMA 20/50 cross · 1h | trend | 70.71 | -29.29 | 119 | 10.1 | -37.27 | -11.12 | -40.64 | 122 |
| 41 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 42 | Heikin-Ashi · 1h | trend | 69.13 | -30.87 | 483 | 23.0 | -45.22 | -9.86 | -47.85 | 616 |
| 43 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -53.90 | -3.82 | -60.06 | 22 |
| 44 | RSI momentum · 1h | momentum | 68.82 | -31.18 | 184 | 14.1 | -38.52 | -8.73 | -41.81 | 202 |
| 45 | Stochastic reversion · 1h | reversion | 68.80 | -31.20 | 364 | 41.2 | -38.50 | -5.82 | -39.73 | 424 |
| 46 | OBV trend · 1h | momentum | 68.77 | -31.23 | 315 | 19.4 | -37.99 | -10.28 | -41.22 | 240 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Max aggression: 1-day momentum | meta | 66.23 | -33.77 | 33 | 27.3 | -53.57 | -3.81 | -58.27 | 39 |
| 49 | Donchian 20/10 · 1h | breakout | 65.58 | -34.42 | 165 | 17.6 | -36.07 | -6.83 | -43.26 | 191 |
| 50 | MFI reversion · 1h | reversion | 65.50 | -34.50 | 474 | 33.1 | -34.52 | -5.18 | -36.25 | 173 |
| 51 | ROC + volume · 1h | momentum | 64.82 | -35.18 | 431 | 27.6 | -38.46 | -6.73 | -43.99 | 339 |
| 52 | CCI reversion · 1h | reversion | 64.25 | -35.75 | 403 | 41.4 | -45.11 | -7.62 | -46.25 | 478 |
| 53 | EMA 9/21 cross · 1h | trend | 63.04 | -36.96 | 291 | 11.3 | -40.02 | -7.69 | -47.32 | 323 |
| 54 | MACD cross · 1h | trend | 62.13 | -37.87 | 442 | 21.0 | -50.45 | -9.97 | -50.77 | 496 |
| 55 | Bollinger reversion · 1h | reversion | 59.73 | -40.27 | 365 | 37.5 | -42.30 | -6.53 | -42.95 | 419 |
| 56 | Williams %R · 1h | reversion | 58.62 | -41.38 | 463 | 39.1 | -49.88 | -8.61 | -50.66 | 578 |
| 57 | RSI(14) reversion · 1h | reversion | 56.28 | -43.73 | 223 | 33.2 | -42.08 | -6.18 | -44.96 | 266 |
| 58 | Agent (ML meta-label) | meta | 56.18 | -43.82 | 2000 | 24.6 | -28.39 | -5.72 | -29.98 | 292 |
| 59 | VWAP momentum · 1h | momentum | 53.74 | -46.26 | 1013 | 21.4 | -57.64 | -11.72 | -61.36 | 1197 |
| 60 | Z-score reversion · 1h | reversion | 52.83 | -47.17 | 240 | 33.3 | -42.23 | -5.94 | -44.68 | 263 |
| 61 | Three white soldiers | momentum | 52.03 | -47.98 | 616 | 14.1 | -51.80 | -23.32 | -52.01 | 663 |
| 62 | Candlestick reversal · 1h | reversion | 51.57 | -48.43 | 598 | 25.9 | -51.74 | -9.58 | -51.92 | 673 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.18 | -47.85 | -99.18 | 5349 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.53 | -30.66 | -84.00 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.39 | -46.99 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.19 | -34.68 | -91.27 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.21 | -45.00 | -92.27 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.04 | -28.98 | -90.21 | 2023 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.24 | -50.95 | -98.24 | 3491 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -54.21 | -96.78 | 3392 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.01 | -40.86 | -94.03 | 2215 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.64 | -35.82 | -83.65 | 1579 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -58.08 | -99.66 | 6265 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.12 | -46.06 | -93.12 | 2533 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.50 | -94.63 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -75.24 | -99.84 | 6247 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.51 | -47.19 | -93.51 | 2287 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.99 | -26.67 | -78.99 | 1640 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.84 | -60.95 | -97.84 | 3379 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -59.74 | -99.13 | 5048 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.00 | -29.85 | -71.00 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.97 | -56.70 | -94.97 | 2717 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.91 | -40.19 | -85.99 | 1705 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -74.01 | -99.73 | 6491 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.36 | -32.44 | -91.36 | 2436 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.87 | -19.68 | -80.87 | 1897 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.29 | -38.39 | -92.29 | 2187 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.80 | -48.16 | -97.80 | 4003 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.39 | -54.56 | -90.39 | 2187 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.34 | -32.14 | -67.34 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.37 | -29.02 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.17 | -19.05 | -83.17 | 1804 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.69 | -47.48 | -97.69 | 4387 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -116.94 | -99.95 | 8421 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T15:20 | Agent (rotation) | buy | SQQQ | 7.95 | — | following Connors RSI(2) |
| 2026-11-20T15:20 | Day trade: Stocks in Play ORB | sell | TNA | 24.21 | -0.48 | target is flat |
| 2026-11-20T15:20 | Day trade: Stocks in Play ORB | sell | IWM | 24.88 | -0.18 | target is flat |
| 2026-11-20T15:20 | Agent (aggressive) | sell | SOXL | 37.94 | -3.87 | selected signal exited |
| 2026-11-20T15:20 | Agent | sell | TSLA | 16.80 | -0.27 | selected signal exited |
| 2026-11-20T15:20 | Agent | sell | SOXL | 31.04 | -3.16 | selected signal exited |
| 2026-11-20T15:20 | MFI reversion · 1h | sell | ETHU | 15.51 | -1.51 | stop-loss |
| 2026-11-20T15:20 | MFI reversion · 1h | sell | BTC-USD | 13.35 | -0.45 | stop-loss |
| 2026-11-20T15:20 | Williams %R · 1h | buy | TNA | 7.91 | — | rebalance up |
| 2026-11-20T15:20 | Williams %R · 1h | buy | MSFT | 7.80 | — | rebalance up |
| 2026-11-20T15:20 | Williams %R · 1h | buy | LABU | 7.88 | — | rebalance up |
| 2026-11-20T15:20 | Williams %R · 1h | buy | IWM | 7.85 | — | rebalance up |
| 2026-11-20T15:20 | Williams %R · 1h | buy | AAPL | 8.19 | — | rebalance up |
| 2026-11-20T15:20 | Williams %R · 1h | sell | XRP-USD | 4.12 | -0.16 | stop-loss |
| 2026-11-20T15:20 | Williams %R · 1h | sell | SOL-USD | 4.11 | -0.17 | stop-loss |
| 2026-11-20T15:20 | Williams %R · 1h | sell | ETHU | 3.16 | -0.50 | stop-loss |
| 2026-11-20T15:20 | Williams %R · 1h | sell | ETH-USD | 4.09 | -0.18 | stop-loss |
| 2026-11-20T15:20 | Williams %R · 1h | sell | BTC-USD | 3.32 | -0.09 | stop-loss |
| 2026-11-20T15:20 | Z-score reversion · 1h | sell | XRP-USD | 13.04 | -0.49 | stop-loss |
| 2026-11-20T15:20 | Z-score reversion · 1h | sell | BTC-USD | 13.14 | -0.45 | stop-loss |
| 2026-11-20T15:20 | Bollinger reversion · 1h | sell | XRP-USD | 11.86 | -0.45 | stop-loss |
| 2026-11-20T15:20 | Bollinger reversion · 1h | sell | SOL-USD | 11.72 | -0.53 | stop-loss |
| 2026-11-20T15:20 | Bollinger reversion · 1h | sell | BTC-USD | 11.89 | -0.44 | stop-loss |
| 2026-11-20T15:20 | RSI(14) reversion · 1h | sell | BTC-USD | 13.90 | -0.41 | stop-loss |
| 2026-11-20T15:20 | VWAP momentum · 1h | sell | ETH-USD | 12.77 | -0.65 | stop-loss |
| 2026-11-20T15:20 | MACD cross · 1h | buy | LABU | 3.33 | — | rebalance up |
| 2026-11-20T15:20 | MACD cross · 1h | buy | COIN | 3.19 | — | rebalance up |
| 2026-11-20T15:20 | MACD cross · 1h | sell | ETH-USD | 12.25 | -0.49 | stop-loss |
| 2026-11-20T15:20 | MACD cross · 1h | sell | BTC-USD | 12.36 | -0.39 | stop-loss |
| 2026-11-20T15:20 | Three white soldiers | sell | COIN | 12.82 | -0.36 | stop-loss |
| 2026-11-20T15:20 | Opening range 30m | buy | SQQQ | 21.31 | — | entry signal |
| 2026-11-20T15:20 | Opening range 30m | sell | PLTR | 21.08 | -0.52 | stop-loss |
| 2026-11-20T15:20 | Opening range 30m | sell | LABU | 20.95 | -0.65 | stop-loss |
| 2026-11-20T15:20 | Opening range 15m | buy | SQQQ | 19.03 | — | entry signal |
| 2026-11-20T15:20 | Opening range 15m | buy | MSFT | 13.55 | — | rebalance up |
| 2026-11-20T15:20 | Opening range 15m | buy | GOOGL | 13.56 | — | rebalance up |
| 2026-11-20T15:20 | Opening range 15m | buy | AMZN | 13.60 | — | rebalance up |
| 2026-11-20T15:20 | Opening range 15m | sell | UPRO | 5.42 | -0.10 | stop-loss |
| 2026-11-20T15:20 | Opening range 15m | sell | TSLA | 5.42 | -0.11 | stop-loss |
| 2026-11-20T15:20 | Opening range 15m | sell | TQQQ | 5.31 | -0.20 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 15:20:05.000131+00:00 -> 2026-11-20 15:30:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
