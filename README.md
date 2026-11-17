# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T18:05:05.000162+00:00 · 63448 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.78 (-15.22%)

Closed trades 212, win rate 35.8%, fees £5.98, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 16.95 | -0.01 |
| COIN | 16.77 | +0.05 |
| TNA | 16.79 | -0.27 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 27738 decisions in 2853 calls, $0.3510 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T18:05 | 9 / 15 / 6 | cash |  |
| Breezy | 2026-11-17T18:05 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-17T18:05 | 7 / 21 / 2 | COIN 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| MFI reversion | BITX | 2.15 | +2.19% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.47 | 17.47 | 0 | — | 13.57 | 4.53 | -4.69 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.17 | 11.17 | 24 | 62.5 | 16.66 | 3.37 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.92 | 2.92 | 0 | — | 4.99 | 1.38 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.79 | 2.16 | -9.06 | 224 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -2.71 | -2.27 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.65 | -0.35 | 37 | 40.5 | -1.60 | -0.24 | -9.64 | 34 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.94 | -4.06 | 8 | 50.0 | -3.15 | -0.03 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.33 | -4.67 | 0 | — | -2.90 | -0.90 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.99 | -6.01 | 197 | 29.9 | -1.66 | -0.52 | -8.15 | 159 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 91.87 | -8.13 | 0 | — | -8.67 | -2.26 | -8.69 | 1 |
| 17 | Copy: Insider buying | copy | 91.19 | -8.81 | 47 | 42.6 | -9.15 | -1.81 | -14.79 | 62 |
| 18 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.17 | -9.83 | 0 | — | -8.39 | -2.26 | -12.67 | 1 |
| 21 | Daily: Bullish score | daily | 87.32 | -12.68 | 17 | 17.6 | -3.74 | -0.54 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -10.88 | -3.86 | -16.07 | 73 |
| 24 | Opening range 30m | breakout | 86.34 | -13.66 | 438 | 33.6 | -9.72 | -3.07 | -14.11 | 575 |
| 25 | Agent | meta | 84.78 | -15.22 | 212 | 35.8 | -15.95 | -7.17 | -18.19 | 204 |
| 26 | Agent (aggressive) | meta | 82.25 | -17.75 | 100 | 34.0 | -16.85 | -4.64 | -19.92 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -25.44 | -7.09 | -27.22 | 204 |
| 28 | Keltner breakout · 1h | breakout | 80.98 | -19.02 | 122 | 26.2 | -20.24 | -4.93 | -26.30 | 155 |
| 29 | Max aggression: 5-day momentum | meta | 80.67 | -19.33 | 21 | 42.9 | -47.47 | -3.11 | -55.24 | 22 |
| 30 | Connors RSI(2) · 1h | reversion | 80.33 | -19.68 | 215 | 40.0 | -14.47 | -6.39 | -14.87 | 94 |
| 31 | Volume breakout · 1h | breakout | 79.91 | -20.09 | 162 | 28.4 | -15.47 | -4.79 | -22.16 | 79 |
| 32 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.03 | -6.51 | -29.47 | 83 |
| 33 | Opening range 15m | breakout | 78.26 | -21.74 | 533 | 31.5 | -16.52 | -4.42 | -21.37 | 686 |
| 34 | Max aggression: 1-day momentum | meta | 77.38 | -22.62 | 30 | 26.7 | -23.50 | -0.87 | -57.50 | 39 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 76.12 | -23.88 | 2 | 0.0 | -14.56 | -1.77 | -26.43 | 1 |
| 36 | ADX DI cross · 1h | trend | 75.24 | -24.76 | 208 | 19.2 | -26.07 | -4.10 | -34.57 | 259 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.28 | -8.50 | -29.80 | 111 |
| 38 | Hold BTC | benchmark | 74.41 | -25.59 | 2 | 0.0 | -16.23 | -2.30 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 73.62 | -26.38 | 189 | 22.2 | -26.20 | -5.67 | -33.25 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 72.67 | -27.33 | 345 | 42.6 | -35.08 | -5.30 | -36.33 | 424 |
| 41 | Supertrend · 1h | trend | 71.24 | -28.76 | 189 | 15.9 | -33.71 | -5.69 | -40.74 | 201 |
| 42 | Triple EMA stack · 1h | trend | 71.16 | -28.84 | 155 | 14.8 | -32.03 | -6.45 | -37.61 | 185 |
| 43 | RSI momentum · 1h | momentum | 71.05 | -28.95 | 176 | 14.2 | -32.49 | -5.93 | -38.85 | 196 |
| 44 | MACD zero-line · 1h | trend | 70.76 | -29.24 | 181 | 17.7 | -26.71 | -5.28 | -33.13 | 199 |
| 45 | MFI reversion · 1h | reversion | 70.49 | -29.51 | 427 | 33.7 | -26.06 | -3.75 | -30.46 | 165 |
| 46 | EMA 20/50 cross · 1h | trend | 69.99 | -30.01 | 115 | 10.4 | -36.14 | -9.95 | -39.18 | 114 |
| 47 | Heikin-Ashi · 1h | trend | 69.80 | -30.20 | 466 | 23.0 | -41.37 | -8.29 | -44.68 | 633 |
| 48 | ROC + volume · 1h | momentum | 69.56 | -30.44 | 408 | 28.2 | -29.72 | -4.72 | -39.15 | 353 |
| 49 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 50 | MACD cross · 1h | trend | 69.14 | -30.86 | 413 | 22.3 | -39.56 | -6.43 | -44.75 | 473 |
| 51 | OBV trend · 1h | momentum | 68.49 | -31.50 | 306 | 19.0 | -35.89 | -7.65 | -39.97 | 261 |
| 52 | Donchian 20/10 · 1h | breakout | 67.32 | -32.68 | 159 | 18.2 | -30.92 | -5.22 | -39.11 | 204 |
| 53 | CCI reversion · 1h | reversion | 66.40 | -33.60 | 382 | 41.6 | -41.57 | -6.81 | -44.29 | 460 |
| 54 | Bollinger reversion · 1h | reversion | 64.06 | -35.94 | 344 | 37.8 | -39.16 | -5.93 | -40.01 | 414 |
| 55 | EMA 9/21 cross · 1h | trend | 63.05 | -36.95 | 280 | 11.1 | -38.65 | -7.32 | -45.87 | 319 |
| 56 | Williams %R · 1h | reversion | 62.77 | -37.23 | 430 | 40.7 | -45.96 | -7.81 | -46.91 | 560 |
| 57 | Agent (ML meta-label) | meta | 60.19 | -39.81 | 1889 | 24.5 | -30.94 | -5.44 | -31.39 | 330 |
| 58 | RSI(14) reversion · 1h | reversion | 58.17 | -41.83 | 205 | 31.7 | -42.37 | -6.24 | -43.58 | 272 |
| 59 | Z-score reversion · 1h | reversion | 57.05 | -42.95 | 224 | 35.3 | -37.61 | -5.19 | -39.23 | 250 |
| 60 | VWAP momentum · 1h | momentum | 56.83 | -43.17 | 958 | 21.6 | -53.41 | -9.51 | -58.15 | 1197 |
| 61 | Three white soldiers | momentum | 55.43 | -44.58 | 581 | 14.6 | -49.31 | -21.62 | -49.92 | 659 |
| 62 | Candlestick reversal · 1h | reversion | 54.84 | -45.16 | 546 | 26.6 | -46.37 | -8.27 | -47.75 | 635 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -42.64 | -99.02 | 5250 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.73 | -25.60 | -82.03 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.06 | -41.49 | -94.07 | 2490 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.18 | -31.23 | -90.38 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.37 | -38.52 | -91.41 | 2306 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.82 | -30.52 | -89.83 | 2122 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -46.26 | -97.89 | 3453 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.53 | -51.96 | -96.54 | 3421 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.60 | -37.50 | -93.64 | 2235 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.00 | -32.04 | -83.09 | 1614 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -51.25 | -99.60 | 6049 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.07 | -41.18 | -92.07 | 2564 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.02 | -37.85 | -95.04 | 3315 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -64.64 | -99.81 | 6161 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.34 | -42.06 | -92.34 | 2243 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.80 | -25.93 | -75.80 | 1640 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -56.71 | -97.65 | 3451 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.02 | -54.16 | -99.03 | 4938 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.27 | -26.58 | -68.44 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.52 | -52.55 | -94.53 | 2736 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.30 | -36.32 | -84.30 | 1727 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -63.51 | -99.70 | 6359 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.79 | -30.21 | -90.90 | 2358 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.61 | -18.50 | -79.85 | 1821 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.19 | -35.18 | -91.32 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.53 | -44.37 | -97.56 | 3898 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -54.99 | -89.34 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.05 | -29.65 | -66.05 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.02 | -22.96 | -72.51 | 1231 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.25 | -17.37 | -80.68 | 1730 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.53 | -44.12 | -97.60 | 4339 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -92.29 | -99.94 | 8419 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T18:05 | Agent (ML meta-label) | sell | SQQQ | 15.03 | -0.02 | selected signal exited |
| 2026-11-17T18:05 | Agent | buy | BITX | 16.96 | — | following MFI reversion |
| 2026-11-17T18:05 | Agent | sell | IWM | 16.96 | -0.02 | selected signal exited |
| 2026-11-17T18:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 99.74 | — | entry |
| 2026-11-17T18:00 | Agent (ML meta-label) | buy | SQQQ | 15.05 | — | entry |
| 2026-11-17T18:00 | MFI reversion · 1h | sell | COIN | 10.09 | -0.14 | target is flat |
| 2026-11-17T17:55 | Agent | buy | IWM | 16.98 | — | following RSI momentum |
| 2026-11-17T17:55 | Agent | sell | BITX | 16.97 | -0.01 | selected signal exited |
| 2026-11-17T17:51 | Agent | buy | BITX | 16.98 | — | following MFI reversion |
| 2026-11-17T17:51 | Agent | sell | IWM | 16.97 | -0.09 | selected signal exited |
| 2026-11-17T17:51 | MFI reversion · 1h | buy | BITX | 8.81 | — | entry |
| 2026-11-17T17:51 | MFI reversion · 1h | sell | TQQQ | 8.78 | -0.07 | target is flat |
| 2026-11-17T17:40 | MFI reversion · 1h | buy | TQQQ | 3.76 | — | rebalance up |
| 2026-11-17T17:40 | MFI reversion · 1h | sell | GOOGL | 7.04 | -0.02 | target is flat |
| 2026-11-17T17:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 99.74 | -1.66 | target is flat |
| 2026-11-17T17:30 | Agent (ML meta-label) | sell | SPY | 15.04 | -0.02 | selected signal exited |
| 2026-11-17T17:30 | MFI reversion · 1h | buy | TQQQ | 5.09 | — | entry signal |
| 2026-11-17T17:30 | MFI reversion · 1h | buy | QQQ | 7.07 | — | entry signal |
| 2026-11-17T17:30 | MFI reversion · 1h | buy | GOOGL | 7.07 | — | entry signal |
| 2026-11-17T17:30 | MFI reversion · 1h | sell | LABU | 4.98 | 0.14 | rebalance down |
| 2026-11-17T17:30 | MFI reversion · 1h | sell | ETHU | 4.74 | -0.09 | rebalance down |
| 2026-11-17T17:30 | MFI reversion · 1h | sell | BTC-USD | 4.70 | -0.12 | rebalance down |
| 2026-11-17T17:30 | CCI reversion · 1h | buy | ETHU | 16.30 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | UPRO | 3.93 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | TQQQ | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | TNA | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | TECL | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | SPY | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | MSFT | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | META | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | LABU | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | IWM | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | GOOGL | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | buy | AMZN | 3.95 | — | entry signal |
| 2026-11-17T17:30 | Williams %R · 1h | sell | TSLA | 8.76 | 0.00 | rebalance down |
| 2026-11-17T17:30 | Williams %R · 1h | sell | SOXL | 9.04 | 0.26 | rebalance down |
| 2026-11-17T17:30 | Williams %R · 1h | sell | QQQ | 6.55 | 0.01 | rebalance down |
| 2026-11-17T17:30 | Williams %R · 1h | sell | NVDA | 6.50 | -0.02 | rebalance down |
| 2026-11-17T17:30 | Williams %R · 1h | sell | AMD | 6.50 | -0.02 | rebalance down |
| 2026-11-17T17:30 | Stochastic reversion · 1h | buy | MSFT | 4.25 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 18:05:05.000162+00:00 -> 2026-11-17 18:15:05.000162+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 18:05:05.000162+00:00 -> 2026-11-17 18:15:05.000162+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
