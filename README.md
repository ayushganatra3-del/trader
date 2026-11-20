# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T15:50:05.000122+00:00 · 67028 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £82.00 (-18.00%)

Closed trades 235, win rate 36.6%, fees £6.38, max drawdown -18.46%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 16.39 | -0.01 |
| TSLA | 32.85 | +0.08 |

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

Today: 17199 decisions in 2445 calls, $0.2271 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T15:50 | 14 / 8 / 8 | cash |  |
| Breezy | 2026-11-20T15:50 | 0 / 21 / 9 | cash |  |
| Boozy | 2026-11-20T15:50 | 5 / 20 / 5 | COIN 52% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.31 | 15.31 | 0 | — | 13.22 | 4.41 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.32 | 3.32 | 0 | — | 4.34 | 1.25 | -6.60 | 0 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.32 | 0.32 | 40 | 42.5 | -1.45 | -0.20 | -9.74 | 36 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.07 | -0.93 | 160 | 34.4 | -4.62 | -4.06 | -5.34 | 75 |
| 9 | Gap and go | momentum | 98.10 | -1.90 | 203 | 31.5 | -1.03 | -0.26 | -9.06 | 202 |
| 10 | Agent (rotation) | meta | 95.47 | -4.53 | 212 | 28.8 | -1.45 | -0.43 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 93.22 | -6.78 | 0 | — | -7.80 | -2.65 | -9.38 | 1 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.43 | -4.67 | -11.21 | 43 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.19 | -8.81 | 0 | — | -9.14 | -2.40 | -10.09 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 17 | Copy: Insider buying | copy | 89.31 | -10.69 | 55 | 40.0 | -6.98 | -1.34 | -14.79 | 66 |
| 18 | VWAP reversion · 1h | reversion | 89.15 | -10.85 | 156 | 45.5 | -12.93 | -3.82 | -18.48 | 149 |
| 19 | Daily: Bullish score | daily | 88.88 | -11.12 | 19 | 15.8 | -13.33 | -3.45 | -19.56 | 14 |
| 20 | Copy: Congress Democrats (NANC) | copy | 88.58 | -11.41 | 0 | — | -12.05 | -3.39 | -14.48 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 88.04 | -11.96 | 8 | 50.0 | -13.26 | -1.14 | -20.39 | 6 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 86.47 | -13.53 | 70 | 20.0 | -18.75 | -9.50 | -18.95 | 72 |
| 24 | Opening range 30m | breakout | 85.45 | -14.55 | 451 | 33.5 | -12.53 | -4.17 | -14.87 | 552 |
| 25 | Parabolic SAR · 1h | trend | 82.84 | -17.16 | 194 | 27.8 | -25.69 | -7.60 | -28.86 | 196 |
| 26 | Agent | meta | 82.00 | -18.00 | 235 | 36.6 | -16.81 | -6.52 | -17.11 | 207 |
| 27 | Connors RSI(2) · 1h | reversion | 80.07 | -19.93 | 218 | 40.4 | -15.51 | -6.99 | -15.67 | 71 |
| 28 | Donchian 55/20 · 1h | breakout | 79.95 | -20.05 | 79 | 12.7 | -26.25 | -8.10 | -27.74 | 82 |
| 29 | Volume breakout · 1h | breakout | 79.85 | -20.15 | 163 | 28.8 | -16.33 | -5.31 | -21.55 | 74 |
| 30 | Agent (aggressive) | meta | 79.82 | -20.18 | 108 | 33.3 | -18.77 | -4.54 | -19.15 | 98 |
| 31 | Keltner breakout · 1h | breakout | 78.72 | -21.27 | 126 | 26.2 | -21.93 | -5.91 | -25.34 | 144 |
| 32 | Opening range 15m | breakout | 76.33 | -23.67 | 559 | 31.1 | -22.30 | -6.87 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 74.97 | -25.03 | 107 | 14.0 | -29.55 | -8.79 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 73.60 | -26.40 | 227 | 20.3 | -25.98 | -3.89 | -35.87 | 273 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 72.28 | -27.72 | 2 | 0.0 | -26.60 | -3.86 | -29.76 | 1 |
| 36 | Triple EMA stack · 1h | trend | 71.36 | -28.64 | 161 | 14.3 | -34.41 | -8.91 | -36.46 | 170 |
| 37 | Bollinger breakout · 1h | breakout | 71.26 | -28.74 | 195 | 21.5 | -32.74 | -8.72 | -36.32 | 217 |
| 38 | Supertrend · 1h | trend | 71.15 | -28.85 | 198 | 16.7 | -32.26 | -5.32 | -39.93 | 204 |
| 39 | EMA 20/50 cross · 1h | trend | 70.93 | -29.07 | 119 | 10.1 | -37.12 | -11.00 | -40.64 | 122 |
| 40 | Hold BTC | benchmark | 70.29 | -29.71 | 2 | 0.0 | -27.24 | -4.38 | -31.58 | 1 |
| 41 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 42 | Heikin-Ashi · 1h | trend | 69.33 | -30.67 | 483 | 23.0 | -45.09 | -9.78 | -47.85 | 616 |
| 43 | RSI momentum · 1h | momentum | 69.01 | -30.99 | 184 | 14.1 | -38.37 | -8.65 | -41.81 | 202 |
| 44 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -53.46 | -3.77 | -60.06 | 22 |
| 45 | OBV trend · 1h | momentum | 68.96 | -31.04 | 315 | 19.4 | -37.84 | -10.18 | -41.22 | 240 |
| 46 | Stochastic reversion · 1h | reversion | 68.19 | -31.81 | 365 | 41.1 | -39.07 | -5.87 | -40.50 | 435 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Max aggression: 1-day momentum | meta | 66.93 | -33.07 | 33 | 27.3 | -53.12 | -3.78 | -58.27 | 39 |
| 49 | Donchian 20/10 · 1h | breakout | 65.76 | -34.24 | 165 | 17.6 | -35.92 | -6.78 | -43.26 | 191 |
| 50 | MFI reversion · 1h | reversion | 65.26 | -34.74 | 475 | 33.1 | -34.76 | -5.21 | -36.49 | 173 |
| 51 | ROC + volume · 1h | momentum | 64.93 | -35.07 | 431 | 27.6 | -36.33 | -6.60 | -41.95 | 338 |
| 52 | CCI reversion · 1h | reversion | 63.77 | -36.23 | 405 | 41.2 | -45.56 | -7.65 | -46.71 | 479 |
| 53 | EMA 9/21 cross · 1h | trend | 63.22 | -36.78 | 291 | 11.3 | -39.88 | -7.63 | -47.32 | 323 |
| 54 | MACD cross · 1h | trend | 61.83 | -38.17 | 444 | 20.9 | -50.68 | -9.97 | -51.00 | 496 |
| 55 | Bollinger reversion · 1h | reversion | 59.70 | -40.30 | 365 | 37.5 | -42.36 | -6.53 | -43.14 | 420 |
| 56 | Williams %R · 1h | reversion | 58.40 | -41.60 | 465 | 38.9 | -50.13 | -8.62 | -50.98 | 580 |
| 57 | RSI(14) reversion · 1h | reversion | 56.20 | -43.80 | 223 | 33.2 | -42.21 | -6.20 | -45.13 | 266 |
| 58 | Agent (ML meta-label) | meta | 55.94 | -44.06 | 2002 | 24.6 | -30.31 | -6.08 | -30.90 | 293 |
| 59 | VWAP momentum · 1h | momentum | 53.90 | -46.10 | 1013 | 21.4 | -57.07 | -11.57 | -60.93 | 1195 |
| 60 | Z-score reversion · 1h | reversion | 52.76 | -47.24 | 240 | 33.3 | -42.34 | -5.95 | -44.86 | 264 |
| 61 | Three white soldiers | momentum | 52.03 | -47.98 | 616 | 14.1 | -51.80 | -23.32 | -52.01 | 663 |
| 62 | Candlestick reversal · 1h | reversion | 51.59 | -48.41 | 598 | 25.9 | -51.72 | -9.58 | -51.95 | 674 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -47.42 | -99.16 | 5343 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.54 | -30.66 | -84.01 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.99 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.23 | -34.47 | -91.34 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.20 | -45.02 | -92.27 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -28.77 | -90.21 | 2023 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.23 | -50.93 | -98.24 | 3490 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -53.81 | -96.79 | 3392 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.01 | -40.27 | -94.05 | 2217 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.64 | -35.82 | -83.65 | 1579 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -58.10 | -99.66 | 6287 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.03 | -46.15 | -93.05 | 2529 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.49 | -94.64 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -75.24 | -99.84 | 6247 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.49 | -47.20 | -93.49 | 2286 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.49 | -25.45 | -79.49 | 1653 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.84 | -60.95 | -97.84 | 3379 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -59.87 | -99.13 | 5050 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.91 | -29.85 | -70.91 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.96 | -56.89 | -94.96 | 2716 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.85 | -40.06 | -85.94 | 1704 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -74.20 | -99.73 | 6505 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.43 | -32.49 | -91.44 | 2448 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.07 | -19.73 | -81.13 | 1903 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.18 | -37.39 | -92.19 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.83 | -48.33 | -97.83 | 4018 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.39 | -54.56 | -90.40 | 2187 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.43 | -31.94 | -67.53 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.31 | -28.91 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.57 | -19.14 | -83.57 | 1820 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.73 | -47.72 | -97.73 | 4409 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -116.76 | -99.95 | 8419 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T15:50 | Day trade: Stocks in Play ORB | sell | MSFT | 24.93 | -0.02 | target is flat |
| 2026-11-20T15:50 | Agent (aggressive) | buy | SOXL | 39.87 | — | following Z-score reversion, CCI reversion |
| 2026-11-20T15:50 | Agent | buy | SOXL | 16.40 | — | following Z-score reversion, CCI reversion |
| 2026-11-20T15:45 | Agent (ML meta-label) | sell | COIN | 13.85 | -0.46 | selected signal exited |
| 2026-11-20T15:45 | MFI reversion · 1h | sell | COIN | 16.44 | -0.63 | stop-loss |
| 2026-11-20T15:45 | CCI reversion · 1h | sell | COIN | 15.75 | -0.59 | stop-loss |
| 2026-11-20T15:45 | Stochastic reversion · 1h | sell | COIN | 4.81 | -0.16 | stop-loss |
| 2026-11-20T15:45 | MACD cross · 1h | sell | COIN | 15.33 | -0.51 | stop-loss |
| 2026-11-20T15:45 | Opening range 15m | sell | MSFT | 18.90 | -0.18 | stop-loss |
| 2026-11-20T15:41 | Williams %R · 1h | buy | GOOGL | 3.00 | — | rebalance up |
| 2026-11-20T15:41 | Williams %R · 1h | sell | LABU | 3.01 | -0.01 | rebalance down |
| 2026-11-20T15:35 | Agent (ML meta-label) | sell | LABU | 13.82 | -0.49 | selected signal exited |
| 2026-11-20T15:35 | CCI reversion · 1h | buy | GOOGL | 6.01 | — | rebalance up |
| 2026-11-20T15:35 | CCI reversion · 1h | buy | COIN | 3.21 | — | rebalance up |
| 2026-11-20T15:35 | CCI reversion · 1h | sell | AMD | 12.69 | -0.41 | stop-loss |
| 2026-11-20T15:35 | RSI(14) reversion · 1h | buy | LABU | 2.81 | — | rebalance up |
| 2026-11-20T15:35 | Trend pullback · 1h | sell | SQQQ | 24.90 | 2.74 | take-profit |
| 2026-11-20T15:35 | MACD cross · 1h | sell | LABU | 15.33 | -0.59 | stop-loss |
| 2026-11-20T15:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 99.63 | — | entry |
| 2026-11-20T15:30 | Agent (aggressive) | buy | TSLA | 39.87 | — | following Stochastic reversion, Bollinger reversion |
| 2026-11-20T15:30 | Agent | buy | TSLA | 32.77 | — | following Stochastic reversion, Bollinger reversion |
| 2026-11-20T15:30 | CCI reversion · 1h | buy | GOOGL | 9.97 | — | entry signal |
| 2026-11-20T15:30 | CCI reversion · 1h | sell | COIN | 3.27 | -0.08 | rebalance down |
| 2026-11-20T15:30 | CCI reversion · 1h | sell | AMD | 3.25 | -0.07 | rebalance down |
| 2026-11-20T15:30 | CCI reversion · 1h | sell | AAPL | 3.46 | -0.01 | rebalance down |
| 2026-11-20T15:30 | Williams %R · 1h | buy | GOOGL | 8.68 | — | entry signal |
| 2026-11-20T15:30 | Williams %R · 1h | buy | AMZN | 11.69 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | UPRO | 4.89 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | TQQQ | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | TNA | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | SPY | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | SOXL | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | QQQ | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | PLTR | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | NVDA | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | MSTR | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | META | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | buy | AMZN | 4.91 | — | entry signal |
| 2026-11-20T15:30 | Stochastic reversion · 1h | sell | MSFT | 12.58 | 0.05 | rebalance down |
| 2026-11-20T15:30 | Stochastic reversion · 1h | sell | LABU | 12.37 | -0.19 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 15:50:05.000122+00:00 -> 2026-11-20 16:00:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
