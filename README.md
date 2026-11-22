# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-22T02:20:05.000132+00:00 · 68803 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £80.18 (-19.82%)

Closed trades 238, win rate 36.1%, fees £6.46, max drawdown -20.19%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-21 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 1755 decisions in 351 calls, $0.0245 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-22T02:20 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-22T02:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-22T02:20 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.73 | +27.25% | 5 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.56 | +8.27% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.49 | 14.49 | 0 | — | 12.18 | 4.63 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.12 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.40 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -3.14 | -2.96 | -3.73 | 72 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 0.96 | 0.41 | -7.56 | 153 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.13 | -5.13 | 19 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.44 | -4.11 | -10.32 | 42 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.38 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.24 | -19.56 | 14 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.98 | -7.58 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -9.45 | -1.94 | -14.79 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.77 | -12.23 | 160 | 45.0 | -14.66 | -4.24 | -20.40 | 156 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -4.00 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -4.01 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.80 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.90 | -15.10 | 194 | 27.8 | -22.59 | -6.03 | -27.65 | 188 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.29 | -6.43 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -19.82 | -9.62 | -20.09 | 67 |
| 28 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 126 | 26.2 | -22.37 | -6.41 | -24.28 | 138 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -20.49 | -4.95 | -21.26 | 199 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.50 | -3.95 | -18.44 | 91 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.69 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -26.88 | -7.25 | -31.39 | 105 |
| 34 | ADX DI cross · 1h | trend | 74.53 | -25.47 | 228 | 20.2 | -31.22 | -5.84 | -35.87 | 276 |
| 35 | Supertrend · 1h | trend | 73.25 | -26.75 | 198 | 16.7 | -33.30 | -6.45 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.96 | -3.42 | -58.28 | 39 |
| 37 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -32.47 | -7.77 | -36.09 | 169 |
| 38 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.35 | -9.46 | -40.30 | 121 |
| 39 | Bollinger breakout · 1h | breakout | 72.29 | -27.71 | 195 | 21.5 | -32.86 | -8.64 | -35.61 | 211 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.14 | -32.18 | 1 |
| 41 | Heikin-Ashi · 1h | trend | 70.35 | -29.65 | 492 | 23.4 | -44.93 | -9.54 | -47.84 | 614 |
| 42 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -37.69 | -9.42 | -41.15 | 234 |
| 43 | RSI momentum · 1h | momentum | 70.15 | -29.85 | 184 | 14.1 | -36.55 | -7.98 | -39.81 | 200 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.41 | -37.91 | 31 |
| 45 | Hold BTC | benchmark | 69.24 | -30.76 | 3 | 0.0 | -26.86 | -5.73 | -36.23 | 1 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 47 | MACD zero-line · 1h | trend | 67.53 | -32.47 | 190 | 17.4 | -33.25 | -9.23 | -33.55 | 207 |
| 48 | Donchian 20/10 · 1h | breakout | 66.73 | -33.27 | 165 | 17.6 | -40.42 | -9.04 | -42.61 | 194 |
| 49 | Stochastic reversion · 1h | reversion | 66.71 | -33.30 | 383 | 39.9 | -43.42 | -6.19 | -44.08 | 447 |
| 50 | ROC + volume · 1h | momentum | 65.98 | -34.02 | 433 | 27.5 | -41.54 | -8.85 | -42.64 | 339 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -35.78 | -5.29 | -39.51 | 179 |
| 52 | EMA 9/21 cross · 1h | trend | 64.20 | -35.80 | 291 | 11.3 | -43.03 | -10.07 | -46.01 | 323 |
| 53 | MACD cross · 1h | trend | 63.11 | -36.89 | 446 | 20.9 | -49.12 | -9.73 | -50.90 | 502 |
| 54 | CCI reversion · 1h | reversion | 58.33 | -41.67 | 423 | 39.5 | -47.77 | -7.86 | -51.36 | 489 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.73 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.69 | -44.31 | 1024 | 21.7 | -58.78 | -13.71 | -60.39 | 1197 |
| 57 | Agent (ML meta-label) | meta | 55.14 | -44.86 | 2023 | 24.6 | -30.25 | -5.34 | -32.61 | 325 |
| 58 | Williams %R · 1h | reversion | 53.97 | -46.03 | 480 | 37.7 | -54.46 | -9.06 | -55.96 | 587 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.01 | -6.48 | -49.45 | 276 |
| 60 | Three white soldiers | momentum | 51.17 | -48.83 | 629 | 14.5 | -52.42 | -22.57 | -53.16 | 668 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.58 | -8.69 | -54.54 | 685 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.09 | -49.17 | -99.15 | 5338 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.23 | -35.95 | -84.49 | 1411 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.44 | -48.26 | -94.66 | 2458 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.70 | -32.75 | -91.46 | 1942 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.46 | -41.08 | -92.03 | 2277 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.57 | -27.84 | -89.67 | 1986 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -48.04 | -98.21 | 3482 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.86 | -53.61 | -96.91 | 3406 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.36 | -38.65 | -93.36 | 2157 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.51 | -34.92 | -83.84 | 1582 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -53.99 | -99.65 | 6332 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.71 | -39.79 | -92.95 | 2525 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.48 | -37.49 | -94.48 | 3143 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -64.03 | -99.84 | 6273 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.39 | -45.36 | -93.46 | 2278 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.13 | -23.49 | -79.79 | 1647 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -57.46 | -97.84 | 3375 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -57.75 | -99.15 | 5122 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.01 | -27.20 | -70.67 | 1222 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.78 | -47.61 | -94.89 | 2719 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.54 | -6.18 | -49.04 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.40 | -36.15 | -85.81 | 1703 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.75 | -68.85 | -99.75 | 6565 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.46 | -30.90 | -91.54 | 2484 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.58 | -19.71 | -82.79 | 1951 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.42 | -32.54 | -92.56 | 2197 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.04 | -46.92 | -98.04 | 4063 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.96 | -46.08 | -90.10 | 2207 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.86 | -29.95 | -67.72 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.09 | -27.71 | -74.90 | 1196 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.75 | -18.84 | -84.11 | 1852 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.82 | -46.17 | -97.82 | 4453 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -92.70 | -99.94 | 8418 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-22T02:00 | ROC + volume · 1h | sell | SOL-USD | 16.40 | -0.21 | exit signal |
| 2026-11-22T02:00 | ROC + volume · 1h | sell | BTC-USD | 16.38 | -0.23 | exit signal |
| 2026-11-22T02:00 | VWAP momentum · 1h | buy | XRP-USD | 13.95 | — | entry signal |
| 2026-11-22T01:00 | VWAP momentum · 1h | sell | XRP-USD | 4.26 | 0.13 | exit signal |
| 2026-11-22T01:00 | VWAP momentum · 1h | sell | SOL-USD | 9.42 | 0.34 | exit signal |
| 2026-11-22T01:00 | VWAP momentum · 1h | sell | ETH-USD | 9.35 | 0.19 | exit signal |
| 2026-11-22T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 9.42 | 0.34 | exit signal |
| 2026-11-22T01:00 | VWAP momentum · 1h | sell | BTC-USD | 9.37 | 0.29 | exit signal |
| 2026-11-21T23:01 | Heikin-Ashi · 1h | sell | DOGE-USD | 17.57 | -0.12 | exit signal |
| 2026-11-21T23:01 | Heikin-Ashi · 1h | sell | BTC-USD | 14.30 | 0.44 | exit signal |
| 2026-11-21T22:05 | Three white soldiers | sell | DOGE-USD | 12.70 | -0.12 | stop-loss |
| 2026-11-21T22:01 | Heikin-Ashi · 1h | sell | XRP-USD | 17.56 | 0.10 | exit signal |
| 2026-11-21T22:01 | Three white soldiers | buy | DOGE-USD | 12.82 | — | entry signal |
| 2026-11-21T21:00 | Heikin-Ashi · 1h | buy | XRP-USD | 9.93 | — | rebalance up |
| 2026-11-21T21:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 3.57 | — | rebalance up |
| 2026-11-21T21:00 | Heikin-Ashi · 1h | sell | SOL-USD | 14.15 | 0.25 | exit signal |
| 2026-11-21T20:00 | MACD zero-line · 1h | sell | XRP-USD | 3.39 | -0.01 | rebalance down |
| 2026-11-21T19:10 | MACD zero-line · 1h | buy | DOGE-USD | 3.39 | — | rebalance up |
| 2026-11-21T19:10 | MACD zero-line · 1h | sell | ETH-USD | 3.39 | -0.02 | rebalance down |
| 2026-11-21T19:02 | MACD zero-line · 1h | buy | DOGE-USD | 3.40 | — | rebalance up |
| 2026-11-21T19:02 | MACD zero-line · 1h | sell | SOL-USD | 3.40 | -0.02 | rebalance down |
| 2026-11-21T19:00 | MFI reversion · 1h | sell | XRP-USD | 16.60 | 1.02 | exit signal |
| 2026-11-21T19:00 | MFI reversion · 1h | sell | BTC-USD | 16.34 | 0.47 | exit signal |
| 2026-11-21T19:00 | MACD zero-line · 1h | buy | DOGE-USD | 3.46 | — | entry signal |
| 2026-11-21T19:00 | MACD zero-line · 1h | buy | BTC-USD | 13.60 | — | entry signal |
| 2026-11-21T18:00 | MFI reversion · 1h | sell | ETH-USD | 16.67 | 1.09 | exit signal |
| 2026-11-21T18:00 | MACD zero-line · 1h | buy | XRP-USD | 17.00 | — | entry signal |
| 2026-11-21T17:25 | Agent (ML meta-label) | sell | XRP-USD | 3.93 | -0.01 | selected signal exited |
| 2026-11-21T17:15 | Agent (ML meta-label) | buy | XRP-USD | 3.94 | — | entry |
| 2026-11-21T17:05 | Agent (ML meta-label) | sell | XRP-USD | 4.57 | -0.03 | selected signal exited |
| 2026-11-21T17:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 14.12 | — | entry |
| 2026-11-21T17:00 | Heikin-Ashi · 1h | sell | ETH-USD | 14.12 | 0.39 | exit signal |
| 2026-11-21T17:00 | MACD zero-line · 1h | buy | SOL-USD | 17.03 | — | entry signal |
| 2026-11-21T17:00 | MACD zero-line · 1h | buy | ETH-USD | 17.03 | — | entry signal |
| 2026-11-21T16:55 | Agent (ML meta-label) | buy | XRP-USD | 4.60 | — | entry |
| 2026-11-21T16:50 | Agent (ML meta-label) | sell | XRP-USD | 4.23 | -0.02 | selected signal exited |
| 2026-11-21T16:45 | Agent (ML meta-label) | buy | XRP-USD | 4.25 | — | entry |
| 2026-11-21T16:15 | Agent (ML meta-label) | sell | XRP-USD | 4.23 | -0.01 | selected signal exited |
| 2026-11-21T16:05 | Agent (ML meta-label) | buy | XRP-USD | 4.25 | — | entry |
| 2026-11-21T16:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 5.25 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-24 02:20:05.000132+00:00 -> 2026-11-22 02:30:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
