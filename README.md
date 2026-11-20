# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T16:21:05.000133+00:00 · 67058 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £80.92 (-19.08%)

Closed trades 236, win rate 36.4%, fees £6.43, max drawdown -19.70%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 32.11 | -0.64 |
| TSLA | 32.10 | -0.24 |

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

Today: 19929 decisions in 2535 calls, $0.2591 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T16:21 | 0 / 17 / 13 | cash |  |
| Breezy | 2026-11-20T16:21 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-20T16:21 | 4 / 24 / 2 | COIN 53% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.97 | 14.97 | 0 | — | 12.89 | 4.31 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.87 | 2.87 | 0 | — | 3.89 | 1.13 | -6.60 | 0 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.61 | 1.61 | 40 | 42.5 | -0.18 | 0.09 | -9.74 | 36 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 98.97 | -1.03 | 160 | 34.4 | -4.71 | -4.13 | -5.45 | 75 |
| 9 | Gap and go | momentum | 98.42 | -1.58 | 203 | 31.5 | -0.71 | -0.15 | -9.06 | 202 |
| 10 | Agent (rotation) | meta | 95.57 | -4.43 | 212 | 28.8 | -1.34 | -0.40 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 92.82 | -7.18 | 0 | — | -8.19 | -2.77 | -9.70 | 1 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.43 | -4.67 | -11.21 | 43 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.19 | -8.81 | 0 | — | -9.14 | -2.40 | -10.09 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 17 | Daily: Bullish score | daily | 89.17 | -10.83 | 19 | 15.8 | -13.05 | -3.34 | -19.56 | 14 |
| 18 | VWAP reversion · 1h | reversion | 89.15 | -10.85 | 156 | 45.5 | -12.93 | -3.82 | -18.48 | 149 |
| 19 | Copy: Insider buying | copy | 88.78 | -11.22 | 55 | 40.0 | -6.83 | -1.30 | -14.79 | 66 |
| 20 | Copy: Congress Democrats (NANC) | copy | 88.12 | -11.88 | 0 | — | -12.51 | -3.49 | -14.75 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.86 | -13.14 | 8 | 50.0 | -14.42 | -1.26 | -21.25 | 6 |
| 23 | Squeeze breakout · 1h | breakout | 86.75 | -13.25 | 70 | 20.0 | -18.49 | -9.28 | -18.95 | 72 |
| 24 | Opening range 30m | breakout | 85.72 | -14.28 | 451 | 33.5 | -12.25 | -4.08 | -14.87 | 552 |
| 25 | Parabolic SAR · 1h | trend | 83.13 | -16.87 | 194 | 27.8 | -25.45 | -7.44 | -28.86 | 196 |
| 26 | Agent | meta | 80.92 | -19.08 | 236 | 36.4 | -17.67 | -6.21 | -18.16 | 203 |
| 27 | Donchian 55/20 · 1h | breakout | 80.22 | -19.77 | 79 | 12.7 | -25.37 | -7.70 | -27.71 | 81 |
| 28 | Volume breakout · 1h | breakout | 80.10 | -19.89 | 163 | 28.8 | -16.08 | -5.21 | -21.55 | 74 |
| 29 | Connors RSI(2) · 1h | reversion | 80.07 | -19.93 | 218 | 40.4 | -15.29 | -6.92 | -15.29 | 70 |
| 30 | Keltner breakout · 1h | breakout | 78.98 | -21.02 | 126 | 26.2 | -21.68 | -5.82 | -25.34 | 144 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -19.95 | -4.59 | -20.42 | 98 |
| 32 | Opening range 15m | breakout | 76.20 | -23.80 | 561 | 31.0 | -22.43 | -6.90 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 75.23 | -24.77 | 107 | 14.0 | -29.32 | -8.63 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 73.74 | -26.26 | 227 | 20.3 | -26.94 | -4.36 | -35.87 | 273 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 71.94 | -28.06 | 2 | 0.0 | -26.94 | -3.91 | -30.10 | 1 |
| 36 | Triple EMA stack · 1h | trend | 71.58 | -28.42 | 161 | 14.3 | -34.41 | -8.84 | -36.37 | 170 |
| 37 | Bollinger breakout · 1h | breakout | 71.50 | -28.50 | 195 | 21.5 | -32.52 | -8.58 | -36.32 | 217 |
| 38 | Supertrend · 1h | trend | 71.40 | -28.60 | 198 | 16.7 | -33.32 | -6.26 | -37.74 | 202 |
| 39 | EMA 20/50 cross · 1h | trend | 71.22 | -28.78 | 119 | 10.1 | -36.92 | -10.82 | -40.64 | 122 |
| 40 | Hold BTC | benchmark | 69.77 | -30.23 | 2 | 0.0 | -27.51 | -4.44 | -32.36 | 1 |
| 41 | Heikin-Ashi · 1h | trend | 69.56 | -30.43 | 483 | 23.0 | -44.98 | -9.72 | -47.85 | 616 |
| 42 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 43 | RSI momentum · 1h | momentum | 69.25 | -30.75 | 184 | 14.1 | -38.08 | -8.52 | -41.77 | 202 |
| 44 | OBV trend · 1h | momentum | 69.21 | -30.79 | 315 | 19.4 | -37.70 | -10.07 | -41.22 | 240 |
| 45 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -52.86 | -3.69 | -60.06 | 22 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 47 | Stochastic reversion · 1h | reversion | 67.80 | -32.20 | 366 | 41.3 | -39.46 | -5.90 | -40.97 | 435 |
| 48 | Max aggression: 1-day momentum | meta | 67.79 | -32.21 | 33 | 27.3 | -52.52 | -3.73 | -58.27 | 39 |
| 49 | Donchian 20/10 · 1h | breakout | 65.98 | -34.02 | 165 | 17.6 | -35.83 | -6.78 | -43.26 | 192 |
| 50 | MFI reversion · 1h | reversion | 65.26 | -34.74 | 475 | 33.1 | -34.80 | -5.21 | -36.49 | 172 |
| 51 | ROC + volume · 1h | momentum | 65.14 | -34.86 | 431 | 27.6 | -36.12 | -6.54 | -41.94 | 338 |
| 52 | CCI reversion · 1h | reversion | 63.69 | -36.31 | 405 | 41.2 | -45.64 | -7.65 | -47.05 | 479 |
| 53 | EMA 9/21 cross · 1h | trend | 63.44 | -36.55 | 291 | 11.3 | -39.68 | -7.55 | -47.32 | 323 |
| 54 | MACD cross · 1h | trend | 62.00 | -38.00 | 444 | 20.9 | -50.52 | -9.97 | -51.00 | 496 |
| 55 | Bollinger reversion · 1h | reversion | 59.48 | -40.52 | 366 | 37.4 | -42.62 | -6.56 | -43.37 | 420 |
| 56 | Williams %R · 1h | reversion | 58.17 | -41.83 | 466 | 38.8 | -50.32 | -8.62 | -51.28 | 580 |
| 57 | RSI(14) reversion · 1h | reversion | 56.23 | -43.77 | 223 | 33.2 | -41.28 | -5.98 | -45.23 | 271 |
| 58 | Agent (ML meta-label) | meta | 56.12 | -43.88 | 2002 | 24.6 | -24.94 | -4.67 | -26.69 | 292 |
| 59 | VWAP momentum · 1h | momentum | 54.10 | -45.90 | 1013 | 21.4 | -56.94 | -11.53 | -60.93 | 1195 |
| 60 | Z-score reversion · 1h | reversion | 52.74 | -47.26 | 240 | 33.3 | -42.36 | -5.95 | -45.08 | 264 |
| 61 | Three white soldiers | momentum | 52.03 | -47.98 | 616 | 14.1 | -51.67 | -23.32 | -52.01 | 662 |
| 62 | Candlestick reversal · 1h | reversion | 51.53 | -48.47 | 598 | 25.9 | -51.60 | -9.51 | -52.05 | 676 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -47.46 | -99.16 | 5340 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.54 | -30.66 | -84.01 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.99 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.28 | -34.20 | -91.37 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.19 | -45.02 | -92.27 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -28.77 | -90.21 | 2023 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.23 | -50.87 | -98.23 | 3488 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -53.96 | -96.79 | 3389 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.90 | -40.80 | -93.98 | 2209 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.61 | -35.82 | -83.61 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -58.00 | -99.66 | 6294 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.03 | -46.16 | -93.05 | 2529 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.50 | -94.63 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -75.12 | -99.84 | 6254 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.53 | -47.20 | -93.53 | 2288 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.46 | -25.53 | -79.46 | 1652 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.84 | -60.95 | -97.84 | 3379 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -59.95 | -99.14 | 5076 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.91 | -29.85 | -70.91 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.94 | -56.70 | -94.94 | 2715 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.80 | -39.87 | -85.94 | 1704 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -74.21 | -99.73 | 6518 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.47 | -32.48 | -91.49 | 2460 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.20 | -19.76 | -81.20 | 1914 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.42 | -37.75 | -92.46 | 2199 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.83 | -48.33 | -97.84 | 4018 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.41 | -54.50 | -90.41 | 2188 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.52 | -31.80 | -67.61 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.23 | -28.75 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.67 | -19.18 | -83.68 | 1826 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.74 | -47.72 | -97.75 | 4418 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -116.90 | -99.94 | 8419 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T16:10 | Williams %R · 1h | buy | LABU | 2.93 | — | rebalance up |
| 2026-11-20T16:10 | Williams %R · 1h | buy | GOOGL | 2.94 | — | rebalance up |
| 2026-11-20T16:10 | Williams %R · 1h | buy | AMZN | 2.92 | — | rebalance up |
| 2026-11-20T16:10 | Williams %R · 1h | sell | MSFT | 11.59 | -0.16 | stop-loss |
| 2026-11-20T16:10 | Stochastic reversion · 1h | sell | MSFT | 4.86 | -0.03 | stop-loss |
| 2026-11-20T16:05 | Agent (aggressive) | sell | TSLA | 39.68 | -0.19 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:05 | Agent (aggressive) | sell | SOXL | 38.62 | -1.25 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T16:05 | Agent | buy | TSLA | 15.99 | — | rebalance up |
| 2026-11-20T16:05 | Agent | sell | META | 16.24 | -0.10 | selected signal exited |
| 2026-11-20T16:05 | EMA 20/50 cross · 1h | sell | SQQQ | 3.72 | 0.66 | rebalance down |
| 2026-11-20T16:05 | Opening range 15m | sell | GOOGL | 18.84 | -0.25 | stop-loss |
| 2026-11-20T16:05 | Opening range 15m | sell | AMZN | 19.00 | -0.13 | stop-loss |
| 2026-11-20T16:00 | Agent | buy | META | 16.35 | — | following MFI reversion |
| 2026-11-20T16:00 | Agent | sell | TSLA | 16.40 | -0.02 | rebalance down |
| 2026-11-20T16:00 | Bollinger reversion · 1h | sell | TNA | 11.90 | -0.60 | stop-loss |
| 2026-11-20T15:55 | Agent | buy | SOXL | 16.35 | — | rebalance up |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 16:21:05.000133+00:00 -> 2026-11-20 16:31:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
