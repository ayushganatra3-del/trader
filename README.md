# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-22T02:50:05.000135+00:00 · 68832 ticks

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

Today: 2190 decisions in 438 calls, $0.0306 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-22T02:50 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-22T02:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-22T02:50 | 2 / 3 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.73 | +27.26% | 5 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.56 | +8.27% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.46 | 14.46 | 0 | — | 12.16 | 4.62 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.12 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.40 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.59 | 0.27 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -3.14 | -2.96 | -3.73 | 72 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 0.88 | 0.39 | -7.56 | 152 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.13 | -5.13 | 19 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.44 | -4.11 | -10.32 | 42 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.38 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.24 | -19.56 | 14 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.98 | -7.58 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -9.44 | -1.94 | -14.79 | 65 |
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
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.09 | -4.86 | -21.85 | 199 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -24.76 | -4.14 | -25.44 | 94 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.69 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -26.88 | -7.25 | -31.39 | 105 |
| 34 | ADX DI cross · 1h | trend | 74.10 | -25.90 | 228 | 20.2 | -31.67 | -5.95 | -35.87 | 276 |
| 35 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.95 | -3.41 | -58.27 | 39 |
| 36 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -32.47 | -7.77 | -36.09 | 169 |
| 37 | Supertrend · 1h | trend | 72.86 | -27.14 | 198 | 16.7 | -33.73 | -6.56 | -37.64 | 204 |
| 38 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.35 | -9.46 | -40.30 | 121 |
| 39 | Bollinger breakout · 1h | breakout | 71.91 | -28.09 | 195 | 21.5 | -33.25 | -8.77 | -35.61 | 211 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.14 | -32.18 | 1 |
| 41 | Heikin-Ashi · 1h | trend | 70.35 | -29.65 | 492 | 23.4 | -44.93 | -9.54 | -47.84 | 614 |
| 42 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -37.69 | -9.42 | -41.14 | 234 |
| 43 | RSI momentum · 1h | momentum | 69.94 | -30.06 | 184 | 14.1 | -36.74 | -8.04 | -39.81 | 200 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.41 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 46 | Hold BTC | benchmark | 68.84 | -31.16 | 3 | 0.0 | -27.23 | -5.82 | -36.23 | 1 |
| 47 | MACD zero-line · 1h | trend | 67.04 | -32.96 | 190 | 17.4 | -33.76 | -9.40 | -34.06 | 207 |
| 48 | Stochastic reversion · 1h | reversion | 66.71 | -33.30 | 383 | 39.9 | -43.42 | -6.19 | -44.07 | 447 |
| 49 | Donchian 20/10 · 1h | breakout | 66.37 | -33.63 | 165 | 17.6 | -40.79 | -9.15 | -42.61 | 194 |
| 50 | ROC + volume · 1h | momentum | 65.98 | -34.02 | 433 | 27.5 | -41.92 | -8.82 | -42.96 | 340 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -35.82 | -5.30 | -39.54 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 63.87 | -36.13 | 291 | 11.3 | -43.39 | -10.20 | -46.01 | 323 |
| 53 | MACD cross · 1h | trend | 62.74 | -37.27 | 446 | 20.9 | -49.44 | -9.83 | -50.90 | 502 |
| 54 | CCI reversion · 1h | reversion | 58.33 | -41.67 | 423 | 39.5 | -47.77 | -7.86 | -51.36 | 489 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.73 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.57 | -44.42 | 1024 | 21.7 | -58.93 | -13.77 | -60.44 | 1198 |
| 57 | Agent (ML meta-label) | meta | 55.14 | -44.86 | 2023 | 24.6 | -30.84 | -5.21 | -33.40 | 337 |
| 58 | Williams %R · 1h | reversion | 53.97 | -46.03 | 480 | 37.7 | -54.45 | -9.06 | -55.96 | 587 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.01 | -6.48 | -49.45 | 276 |
| 60 | Three white soldiers | momentum | 51.17 | -48.83 | 629 | 14.5 | -52.48 | -22.54 | -53.22 | 669 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.77 | -8.71 | -54.72 | 686 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.08 | -49.20 | -99.14 | 5334 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.23 | -35.95 | -84.50 | 1411 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.44 | -48.26 | -94.66 | 2458 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.70 | -32.74 | -91.46 | 1942 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.46 | -41.08 | -92.03 | 2277 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.63 | -27.83 | -89.71 | 1984 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.14 | -48.04 | -98.21 | 3481 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.86 | -52.22 | -96.96 | 3405 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.37 | -38.65 | -93.37 | 2159 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.52 | -34.87 | -83.85 | 1582 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -54.13 | -99.65 | 6336 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.71 | -39.79 | -92.95 | 2525 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.51 | -37.84 | -94.51 | 3142 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -63.97 | -99.84 | 6272 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.34 | -45.36 | -93.46 | 2273 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.17 | -23.40 | -79.83 | 1648 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -57.46 | -97.84 | 3375 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -57.84 | -99.15 | 5122 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.01 | -27.20 | -70.67 | 1222 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.78 | -47.61 | -94.89 | 2719 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.54 | -6.18 | -49.04 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.41 | -36.11 | -85.83 | 1703 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.75 | -70.16 | -99.75 | 6569 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.53 | -31.18 | -91.54 | 2486 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.58 | -19.71 | -82.79 | 1951 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.41 | -32.63 | -92.54 | 2194 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.04 | -47.20 | -98.04 | 4065 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.95 | -46.07 | -90.09 | 2207 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.86 | -29.95 | -67.72 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.09 | -27.71 | -74.90 | 1196 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.81 | -18.99 | -84.06 | 1858 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.84 | -47.08 | -97.84 | 4458 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -92.56 | -99.94 | 8416 |
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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-24 02:50:05.000135+00:00 -> 2026-11-22 03:00:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
