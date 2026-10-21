# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T19:20:05.000141+00:00 · 31022 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.68 (-9.32%)

Closed trades 91, win rate 40.7%, fees £3.01, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.20 | +0.09 |
| TSLA | 18.07 | -0.06 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-20)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.22 · VIX 17.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 35211 decisions in 2829 calls, $0.4337 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T19:20 | 11 / 15 / 4 | AMD 15% |  |
| Breezy | 2026-10-21T19:20 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-21T19:20 | 8 / 20 / 2 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.31 | 6.31 | 0 | — | 8.63 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.99 | 2.00 | 10 | 50.0 | -6.82 | -0.29 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.01 | 0.01 | 4 | 50.0 | 9.24 | 1.95 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold BTC | benchmark | 99.56 | -0.44 | 0 | — | 15.45 | 2.21 | -8.68 | 1 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.53 | -0.47 | 0 | — | 1.41 | 0.67 | -5.02 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.24 | -0.76 | 63 | 34.9 | 2.69 | 1.57 | -2.29 | 65 |
| 13 | Hold SPY | benchmark | 99.23 | -0.78 | 0 | — | 0.97 | 0.60 | -3.13 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.44 | -2.56 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.11 | -2.89 | 0 | — | -3.90 | -1.48 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.02 | -1.71 | -5.83 | 1 |
| 18 | Copy: Insider buying | copy | 96.50 | -3.50 | 25 | 40.0 | -11.47 | -1.95 | -20.62 | 72 |
| 19 | Donchian 55/20 · 1h | breakout | 96.09 | -3.91 | 41 | 17.1 | -14.34 | -2.91 | -16.00 | 103 |
| 20 | Agent (rotation) | meta | 95.75 | -4.25 | 117 | 30.8 | -6.79 | -3.61 | -7.99 | 269 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 22 | ADX DI cross · 1h | trend | 95.47 | -4.54 | 91 | 19.8 | -12.34 | -2.25 | -16.51 | 261 |
| 23 | Daily: Momentum burst | daily | 95.02 | -4.98 | 6 | 16.7 | -9.21 | -1.35 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.78 | -5.22 | 92 | 23.9 | -20.14 | -6.17 | -20.28 | 131 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.91 | 2.14 | -7.13 | 202 |
| 26 | Opening range 30m | breakout | 93.42 | -6.58 | 225 | 32.4 | -11.01 | -3.12 | -17.26 | 571 |
| 27 | Parabolic SAR · 1h | trend | 93.36 | -6.64 | 108 | 23.1 | -15.07 | -3.30 | -19.14 | 273 |
| 28 | Squeeze breakout · 1h | breakout | 93.15 | -6.85 | 46 | 21.7 | -1.72 | -0.33 | -11.48 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 92.73 | -7.27 | 0 | — | 0.79 | 0.28 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.30 | -7.70 | 87 | 29.9 | -9.24 | -1.63 | -15.28 | 262 |
| 31 | Daily: Bullish score | daily | 91.95 | -8.04 | 8 | 0.0 | -2.99 | -0.23 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.01 | -1.87 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.76 | -9.24 | 92 | 23.9 | -12.62 | -2.25 | -14.13 | 113 |
| 34 | Agent | meta | 90.68 | -9.32 | 91 | 40.7 | -14.82 | -7.22 | -19.71 | 253 |
| 35 | Supertrend · 1h | trend | 90.15 | -9.85 | 88 | 12.5 | -21.21 | -4.20 | -27.05 | 219 |
| 36 | Connors RSI(2) · 1h | reversion | 89.96 | -10.04 | 158 | 42.4 | -21.90 | -6.51 | -23.75 | 194 |
| 37 | RSI momentum · 1h | momentum | 89.72 | -10.28 | 84 | 16.7 | -20.51 | -4.11 | -22.06 | 222 |
| 38 | Stochastic reversion · 1h | reversion | 89.44 | -10.56 | 169 | 47.3 | -13.71 | -2.24 | -22.24 | 362 |
| 39 | EMA 20/50 cross · 1h | trend | 88.94 | -11.06 | 62 | 12.9 | -20.89 | -3.60 | -23.67 | 138 |
| 40 | Opening range 15m | breakout | 88.10 | -11.90 | 277 | 28.5 | -15.44 | -4.18 | -19.20 | 707 |
| 41 | Keltner breakout · 1h | breakout | 88.03 | -11.97 | 61 | 23.0 | -18.34 | -3.42 | -25.68 | 206 |
| 42 | MACD cross · 1h | trend | 87.48 | -12.52 | 199 | 21.1 | -23.67 | -4.47 | -26.94 | 467 |
| 43 | Agent (aggressive) | meta | 87.44 | -12.56 | 45 | 35.6 | -13.34 | -3.92 | -18.70 | 129 |
| 44 | Ichimoku · 1h | trend | 86.87 | -13.13 | 60 | 13.3 | -17.78 | -3.33 | -20.25 | 118 |
| 45 | Z-score reversion · 1h | reversion | 86.68 | -13.32 | 102 | 34.3 | -11.56 | -1.79 | -21.32 | 196 |
| 46 | Donchian 20/10 · 1h | breakout | 86.02 | -13.98 | 83 | 19.3 | -20.98 | -3.87 | -30.05 | 230 |
| 47 | Triple EMA stack · 1h | trend | 85.62 | -14.38 | 92 | 15.2 | -29.08 | -5.37 | -29.63 | 223 |
| 48 | MFI reversion · 1h | reversion | 85.14 | -14.86 | 228 | 32.9 | -14.52 | -2.20 | -21.11 | 140 |
| 49 | Agent (ML meta-label) | meta | 84.53 | -15.47 | 732 | 20.1 | -7.39 | -1.16 | -16.02 | 375 |
| 50 | MACD zero-line · 1h | trend | 84.42 | -15.58 | 92 | 15.2 | -23.40 | -4.55 | -26.06 | 227 |
| 51 | OBV trend · 1h | momentum | 84.04 | -15.96 | 188 | 17.6 | -32.71 | -6.16 | -33.39 | 316 |
| 52 | ROC + volume · 1h | momentum | 83.00 | -17.00 | 212 | 23.6 | -26.49 | -4.75 | -33.30 | 391 |
| 53 | Three white soldiers | momentum | 82.63 | -17.38 | 257 | 20.6 | -45.62 | -18.00 | -46.54 | 605 |
| 54 | Williams %R · 1h | reversion | 82.57 | -17.43 | 199 | 44.7 | -31.51 | -4.88 | -36.62 | 517 |
| 55 | Bollinger reversion · 1h | reversion | 82.54 | -17.46 | 163 | 36.2 | -29.13 | -5.62 | -32.84 | 348 |
| 56 | CCI reversion · 1h | reversion | 82.09 | -17.91 | 188 | 43.6 | -20.29 | -2.63 | -27.44 | 436 |
| 57 | Heikin-Ashi · 1h | trend | 81.39 | -18.61 | 237 | 21.1 | -43.44 | -9.29 | -46.38 | 679 |
| 58 | EMA 9/21 cross · 1h | trend | 80.87 | -19.13 | 143 | 10.5 | -27.01 | -5.25 | -29.95 | 331 |
| 59 | RSI(14) reversion · 1h | reversion | 80.82 | -19.18 | 85 | 24.7 | -14.89 | -2.70 | -23.28 | 171 |
| 60 | VWAP momentum · 1h | momentum | 79.10 | -20.90 | 475 | 21.3 | -45.28 | -8.30 | -51.87 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 78.93 | -21.07 | 230 | 30.0 | -35.61 | -6.26 | -39.07 | 540 |
| 62 | Max aggression: 1-day momentum | meta | 76.96 | -23.04 | 17 | 29.4 | -34.32 | -2.15 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.86 | -40.14 | 677 | 23.3 | -77.80 | -22.03 | -78.91 | 1710 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 400 | 13.5 | -64.78 | -20.33 | -65.03 | 869 |
| 65 | RSI(14) reversion | reversion | 57.19 | -42.81 | 751 | 26.6 | -74.08 | -16.17 | -74.89 | 1607 |
| 66 | Donchian 55/20 | breakout | 56.47 | -43.53 | 532 | 19.5 | -71.98 | -19.14 | -74.04 | 1287 |
| 67 | Squeeze breakout | breakout | 56.26 | -43.74 | 521 | 14.0 | -66.93 | -22.39 | -67.86 | 1214 |
| 68 | EMA 20/50 cross | trend | 55.47 | -44.53 | 565 | 19.5 | -78.75 | -19.02 | -80.88 | 1441 |
| 69 | VWAP reversion | reversion | 54.22 | -45.78 | 762 | 25.7 | -70.96 | -14.20 | -72.15 | 1470 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.76 | -30.99 | -98.80 | 5284 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.96 | -33.64 | -94.28 | 2612 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.57 | -22.21 | -88.67 | 1902 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.96 | -26.74 | -91.71 | 2368 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.41 | -26.16 | -91.49 | 2276 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -33.84 | -97.77 | 3508 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.90 | -37.75 | -96.98 | 3579 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.59 | -27.83 | -94.77 | 2571 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.97 | -27.79 | -83.44 | 1736 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.00 | -99.38 | 5716 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.98 | -28.42 | -92.66 | 2631 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.90 | -31.53 | -95.90 | 3485 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.42 | -99.76 | 6166 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -29.66 | -91.90 | 2343 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -39.45 | -97.82 | 3638 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.39 | -98.49 | 4695 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.21 | -34.97 | -94.44 | 2813 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.47 | -28.01 | -84.44 | 1814 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.32 | -99.54 | 6186 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.86 | -22.48 | -87.01 | 2143 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.79 | -26.17 | -88.05 | 2121 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -32.82 | -95.96 | 3766 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -33.36 | -89.49 | 2100 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.77 | -33.39 | -95.78 | 4087 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.04 | -99.91 | 8293 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T19:20 | Agent (ML meta-label) | buy | ETHU | 9.39 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T19:20 | EMA 20/50 cross | sell | AMZN | 5.05 | -0.02 | exit signal |
| 2026-10-21T19:15 | Agent (ML meta-label) | sell | ETHU | 9.28 | -0.15 | selected signal exited |
| 2026-10-21T19:15 | Agent | buy | ETHU | 18.11 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T19:15 | VWAP reversion | buy | TNA | 13.54 | — | entry signal |
| 2026-10-21T19:15 | VWAP reversion | buy | IWM | 13.54 | — | entry signal |
| 2026-10-21T19:15 | RSI(14) reversion | buy | UPRO | 8.16 | — | entry signal |
| 2026-10-21T19:15 | RSI(14) reversion | buy | TQQQ | 8.16 | — | entry signal |
| 2026-10-21T19:15 | RSI(14) reversion | buy | SPY | 8.16 | — | entry signal |
| 2026-10-21T19:15 | RSI(14) reversion | buy | QQQ | 8.16 | — | entry signal |
| 2026-10-21T19:15 | RSI(14) reversion | buy | IWM | 8.16 | — | entry signal |
| 2026-10-21T19:15 | RSI(14) reversion | buy | ETH-USD | 8.16 | — | entry signal |
| 2026-10-21T19:15 | RSI(14) reversion | buy | AMZN | 8.16 | — | entry signal |
| 2026-10-21T19:15 | EMA 20/50 cross | sell | META | 5.01 | -0.02 | exit signal |
| 2026-10-21T19:10 | Opening range 15m | sell | META | 6.24 | -0.05 | stop-loss |
| 2026-10-21T19:05 | VWAP reversion | buy | LABU | 13.54 | — | entry signal |
| 2026-10-21T19:05 | VWAP reversion | sell | SQQQ | 13.60 | 0.12 | exit signal |
| 2026-10-21T19:05 | Opening range 15m | buy | TECL | 4.48 | — | rebalance up |
| 2026-10-21T19:05 | Opening range 15m | sell | SOXL | 5.10 | -0.13 | stop-loss |
| 2026-10-21T19:05 | Donchian 55/20 | buy | XRP-USD | 2.87 | — | rebalance up |
| 2026-10-21T19:05 | Donchian 55/20 | sell | DOGE-USD | 11.26 | -0.08 | exit signal |
| 2026-10-21T19:05 | Donchian 55/20 | sell | BTC-USD | 11.25 | -0.07 | exit signal |
| 2026-10-21T19:00 | Agent (rotation) | sell | TQQQ | 31.69 | -0.39 | selected signal exited |
| 2026-10-21T19:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 103.17 | -1.27 | target is flat |
| 2026-10-21T19:00 | Squeeze breakout | sell | XRP-USD | 14.02 | -0.13 | stop-loss |
| 2026-10-21T19:00 | Squeeze breakout | sell | AMD | 14.16 | 0.06 | exit signal |
| 2026-10-21T19:00 | Opening range 15m | buy | AMD | 5.20 | — | entry |
| 2026-10-21T19:00 | Opening range 15m | sell | AMZN | 5.20 | -0.03 | stop-loss |
| 2026-10-21T19:00 | Donchian 55/20 | buy | XRP-USD | 5.61 | — | rebalance up |
| 2026-10-21T19:00 | Donchian 55/20 | buy | PLTR | 5.62 | — | rebalance up |
| 2026-10-21T19:00 | Donchian 55/20 | buy | DOGE-USD | 5.70 | — | rebalance up |
| 2026-10-21T19:00 | Donchian 55/20 | buy | BTC-USD | 6.19 | — | rebalance up |
| 2026-10-21T19:00 | Donchian 55/20 | buy | AMD | 6.60 | — | rebalance up |
| 2026-10-21T19:00 | Donchian 55/20 | sell | MSTR | 3.29 | 0.08 | exit signal |
| 2026-10-21T19:00 | Donchian 55/20 | sell | ETHU | 5.68 | 0.03 | exit signal |
| 2026-10-21T19:00 | Donchian 55/20 | sell | ETH-USD | 5.65 | 0.03 | exit signal |
| 2026-10-21T19:00 | Donchian 55/20 | sell | COIN | 5.66 | 0.01 | exit signal |
| 2026-10-21T19:00 | Donchian 55/20 | sell | BITX | 5.65 | 0.08 | exit signal |
| 2026-10-21T19:00 | Donchian 55/20 | sell | AAPL | 2.92 | 0.01 | exit signal |
| 2026-10-21T19:00 | ROC + volume | buy | SQQQ | 14.99 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 19:20:05.000141+00:00 -> 2026-10-21 19:30:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
