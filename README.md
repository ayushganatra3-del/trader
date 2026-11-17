# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T17:37:05.000127+00:00 · 63429 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.89 (-15.11%)

Closed trades 209, win rate 36.4%, fees £5.93, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 16.78 | +0.06 |
| IWM | 16.98 | -0.08 |
| TNA | 16.84 | -0.22 |

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

Today: 26040 decisions in 2796 calls, $0.3311 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T17:37 | 2 / 12 / 16 | cash |  |
| Breezy | 2026-11-17T17:37 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-17T17:37 | 1 / 23 / 6 | COIN 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.33 | 17.33 | 0 | — | 12.85 | 4.27 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.70 | 10.70 | 24 | 62.5 | 16.17 | 3.29 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.07 | 3.07 | 0 | — | 5.32 | 1.47 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.63 | 2.12 | -9.06 | 224 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -2.71 | -2.27 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.74 | -0.26 | 37 | 40.5 | -1.52 | -0.22 | -9.64 | 33 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.42 | -3.58 | 8 | 50.0 | -2.66 | 0.02 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.44 | -4.56 | 0 | — | -3.39 | -1.07 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 14 | Agent (rotation) | meta | 93.86 | -6.14 | 197 | 29.9 | -1.80 | -0.57 | -8.15 | 159 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 91.87 | -8.13 | 0 | — | -8.67 | -2.26 | -8.69 | 1 |
| 17 | Copy: Insider buying | copy | 91.21 | -8.79 | 47 | 42.6 | -8.93 | -1.77 | -14.79 | 62 |
| 18 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 19 | Copy: Congress Democrats (NANC) | copy | 90.29 | -9.71 | 0 | — | -8.26 | -2.23 | -12.67 | 1 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.24 | -12.76 | 17 | 17.6 | -3.51 | -0.49 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -10.31 | -3.39 | -16.01 | 73 |
| 24 | Opening range 30m | breakout | 86.25 | -13.75 | 438 | 33.6 | -9.82 | -3.11 | -14.11 | 575 |
| 25 | Agent | meta | 84.89 | -15.11 | 209 | 36.4 | -15.18 | -7.34 | -17.12 | 205 |
| 26 | Agent (aggressive) | meta | 82.27 | -17.73 | 100 | 34.0 | -16.83 | -4.64 | -19.92 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -25.25 | -7.05 | -27.22 | 203 |
| 28 | Keltner breakout · 1h | breakout | 80.98 | -19.02 | 122 | 26.2 | -18.56 | -4.17 | -26.30 | 154 |
| 29 | Max aggression: 5-day momentum | meta | 80.33 | -19.67 | 21 | 42.9 | -47.69 | -3.14 | -55.24 | 22 |
| 30 | Connors RSI(2) · 1h | reversion | 80.33 | -19.68 | 215 | 40.0 | -14.47 | -6.39 | -14.87 | 94 |
| 31 | Volume breakout · 1h | breakout | 79.83 | -20.17 | 162 | 28.4 | -15.56 | -4.82 | -22.16 | 79 |
| 32 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.40 | -6.63 | -29.47 | 84 |
| 33 | Opening range 15m | breakout | 78.17 | -21.83 | 533 | 31.5 | -16.61 | -4.45 | -21.37 | 686 |
| 34 | Max aggression: 1-day momentum | meta | 77.06 | -22.94 | 30 | 26.7 | -23.83 | -0.89 | -57.50 | 39 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 76.38 | -23.62 | 2 | 0.0 | -15.09 | -1.85 | -26.43 | 1 |
| 36 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.28 | -8.50 | -29.80 | 111 |
| 37 | ADX DI cross · 1h | trend | 75.16 | -24.84 | 208 | 19.2 | -26.00 | -4.10 | -34.44 | 259 |
| 38 | Hold BTC | benchmark | 74.22 | -25.78 | 2 | 0.0 | -16.27 | -2.30 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 73.62 | -26.38 | 189 | 22.2 | -26.15 | -5.66 | -33.25 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 72.82 | -27.18 | 345 | 42.6 | -34.94 | -5.28 | -36.33 | 424 |
| 41 | Triple EMA stack · 1h | trend | 71.08 | -28.92 | 155 | 14.8 | -31.52 | -6.33 | -37.61 | 185 |
| 42 | Supertrend · 1h | trend | 71.00 | -29.00 | 189 | 15.9 | -33.93 | -5.74 | -40.74 | 201 |
| 43 | RSI momentum · 1h | momentum | 70.92 | -29.09 | 176 | 14.2 | -32.19 | -5.86 | -38.85 | 195 |
| 44 | MACD zero-line · 1h | trend | 70.68 | -29.32 | 181 | 17.7 | -26.78 | -5.30 | -33.13 | 199 |
| 45 | MFI reversion · 1h | reversion | 70.49 | -29.51 | 424 | 34.0 | -26.09 | -3.75 | -30.42 | 169 |
| 46 | EMA 20/50 cross · 1h | trend | 69.91 | -30.09 | 115 | 10.4 | -36.21 | -9.97 | -39.18 | 114 |
| 47 | Heikin-Ashi · 1h | trend | 69.73 | -30.27 | 466 | 23.0 | -41.43 | -8.30 | -44.68 | 633 |
| 48 | ROC + volume · 1h | momentum | 69.48 | -30.52 | 408 | 28.2 | -29.92 | -4.79 | -39.15 | 354 |
| 49 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 50 | MACD cross · 1h | trend | 69.13 | -30.87 | 413 | 22.3 | -37.84 | -5.96 | -44.75 | 475 |
| 51 | OBV trend · 1h | momentum | 68.42 | -31.58 | 306 | 19.0 | -35.27 | -7.48 | -39.97 | 261 |
| 52 | Donchian 20/10 · 1h | breakout | 67.19 | -32.81 | 159 | 18.2 | -31.05 | -5.25 | -39.11 | 204 |
| 53 | CCI reversion · 1h | reversion | 66.58 | -33.42 | 382 | 41.6 | -41.42 | -6.78 | -44.29 | 460 |
| 54 | Bollinger reversion · 1h | reversion | 64.12 | -35.88 | 344 | 37.8 | -39.06 | -5.92 | -40.01 | 411 |
| 55 | Williams %R · 1h | reversion | 62.99 | -37.01 | 430 | 40.7 | -45.75 | -7.78 | -46.91 | 559 |
| 56 | EMA 9/21 cross · 1h | trend | 62.89 | -37.11 | 280 | 11.1 | -39.86 | -7.72 | -45.87 | 318 |
| 57 | Agent (ML meta-label) | meta | 60.21 | -39.79 | 1888 | 24.5 | -26.36 | -4.38 | -30.71 | 327 |
| 58 | RSI(14) reversion · 1h | reversion | 58.32 | -41.68 | 205 | 31.7 | -42.23 | -6.21 | -43.58 | 272 |
| 59 | Z-score reversion · 1h | reversion | 57.15 | -42.85 | 224 | 35.3 | -37.50 | -5.18 | -39.23 | 250 |
| 60 | VWAP momentum · 1h | momentum | 56.83 | -43.17 | 958 | 21.6 | -53.45 | -9.52 | -58.15 | 1198 |
| 61 | Three white soldiers | momentum | 55.37 | -44.63 | 581 | 14.6 | -49.47 | -21.84 | -49.87 | 659 |
| 62 | Candlestick reversal · 1h | reversion | 55.05 | -44.95 | 546 | 26.6 | -46.01 | -8.24 | -47.63 | 636 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -42.93 | -99.03 | 5257 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.67 | -25.59 | -82.03 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.02 | -41.76 | -94.03 | 2491 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.15 | -31.22 | -90.37 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.41 | -38.45 | -91.43 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.82 | -30.52 | -89.83 | 2121 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -46.28 | -97.90 | 3451 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -52.95 | -96.55 | 3423 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.59 | -37.20 | -93.65 | 2234 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.98 | -32.11 | -83.06 | 1619 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.26 | -99.60 | 6071 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.05 | -41.29 | -92.06 | 2565 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.06 | -37.82 | -95.07 | 3321 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -64.51 | -99.81 | 6161 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -41.94 | -92.30 | 2238 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.75 | -25.99 | -75.81 | 1640 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -57.00 | -97.64 | 3455 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.02 | -54.48 | -99.03 | 4940 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.23 | -26.58 | -68.44 | 1223 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.52 | -52.32 | -94.54 | 2736 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.36 | -36.84 | -84.36 | 1735 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -64.74 | -99.70 | 6366 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.79 | -30.20 | -90.90 | 2359 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.69 | -18.58 | -79.89 | 1828 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.17 | -35.48 | -91.26 | 2162 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.52 | -44.09 | -97.57 | 3916 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.26 | -55.45 | -89.35 | 2164 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.04 | -29.65 | -66.04 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.06 | -22.94 | -72.51 | 1232 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.54 | -17.68 | -80.76 | 1736 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -45.12 | -97.61 | 4360 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -94.73 | -99.94 | 8419 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-17T17:30 | Z-score reversion · 1h | buy | UPRO | 7.15 | — | entry signal |
| 2026-11-17T17:30 | Z-score reversion · 1h | buy | TNA | 7.16 | — | entry signal |
| 2026-11-17T17:30 | Z-score reversion · 1h | buy | TECL | 7.16 | — | entry signal |
| 2026-11-17T17:30 | Z-score reversion · 1h | buy | SPY | 7.16 | — | entry signal |
| 2026-11-17T17:30 | Z-score reversion · 1h | buy | LABU | 7.16 | — | entry signal |
| 2026-11-17T17:30 | Z-score reversion · 1h | buy | IWM | 7.16 | — | entry signal |
| 2026-11-17T17:30 | Z-score reversion · 1h | sell | ETHU | 7.45 | -0.20 | rebalance down |
| 2026-11-17T17:30 | Z-score reversion · 1h | sell | AMZN | 4.75 | -0.03 | rebalance down |
| 2026-11-17T17:30 | Bollinger reversion · 1h | buy | UPRO | 8.02 | — | entry signal |
| 2026-11-17T17:30 | Bollinger reversion · 1h | buy | TNA | 8.04 | — | entry signal |
| 2026-11-17T17:30 | Bollinger reversion · 1h | buy | SPY | 8.04 | — | entry signal |
| 2026-11-17T17:30 | Bollinger reversion · 1h | buy | IWM | 8.04 | — | entry signal |
| 2026-11-17T17:30 | Bollinger reversion · 1h | sell | TSLA | 8.09 | 0.05 | rebalance down |
| 2026-11-17T17:30 | Bollinger reversion · 1h | sell | COIN | 8.12 | -0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 17:37:05.000127+00:00 -> 2026-11-17 17:47:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 17:37:05.000127+00:00 -> 2026-11-17 17:47:05.000127+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
