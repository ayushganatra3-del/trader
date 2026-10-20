# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T18:25:05.000152+00:00 · 29789 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.10 (-8.90%)

Closed trades 87, win rate 40.2%, fees £2.92, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.67 | +0.39 |

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

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 31509 decisions in 2667 calls, $0.3903 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T18:25 | 2 / 9 / 18 | cash |  |
| Breezy | 2026-10-20T18:25 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-20T18:25 | 4 / 25 / 0 | COIN 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | BITX | 1.90 | +3.32% | 6 |
| VWAP reversion | ETHU | 1.90 | +4.27% | 5 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.61 | 5.61 | 0 | — | 7.32 | 3.51 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 101.31 | 1.30 | 9 | 44.4 | -12.81 | -0.87 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.06 | -0.94 | 0 | — | -0.10 | -0.01 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.94 | -1.06 | 59 | 35.6 | 2.41 | 1.38 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.64 | -1.36 | 0 | — | -0.04 | 0.07 | -5.15 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.43 | -1.57 | 3 | 33.3 | 4.68 | 1.07 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 14 | Hold BTC | benchmark | 97.65 | -2.35 | 0 | — | 20.67 | 2.73 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.07 | -2.93 | 0 | — | -4.14 | -1.58 | -7.04 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.80 | -2.15 | -5.83 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.96 | -3.04 | 0 | — | 0.03 | 0.07 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.16 | -3.84 | 40 | 15.0 | -18.45 | -3.64 | -22.00 | 103 |
| 19 | Agent (rotation) | meta | 96.13 | -3.87 | 114 | 31.6 | -7.23 | -3.28 | -9.02 | 303 |
| 20 | Trend pullback · 1h | trend | 95.57 | -4.43 | 90 | 23.3 | -20.40 | -6.11 | -20.75 | 133 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Copy: Insider buying | copy | 95.28 | -4.72 | 24 | 41.7 | -12.71 | -2.19 | -20.62 | 72 |
| 23 | ADX DI cross · 1h | trend | 94.76 | -5.24 | 89 | 18.0 | -13.61 | -2.62 | -15.49 | 256 |
| 24 | Daily: Momentum burst | daily | 94.04 | -5.96 | 6 | 16.7 | -6.91 | -0.92 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.28 | 1.37 | -6.51 | 198 |
| 26 | Opening range 30m | breakout | 92.48 | -7.52 | 208 | 29.3 | -13.09 | -3.78 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.74 | -8.26 | 105 | 21.9 | -18.37 | -3.97 | -21.51 | 273 |
| 28 | Squeeze breakout · 1h | breakout | 91.57 | -8.43 | 46 | 21.7 | -3.93 | -0.89 | -11.34 | 97 |
| 29 | Daily: Bullish score | daily | 91.51 | -8.49 | 7 | 0.0 | -6.77 | -0.73 | -13.10 | 13 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 91.49 | -8.51 | 0 | — | 1.35 | 0.37 | -14.37 | 1 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.20 | -2.31 | -16.91 | 1 |
| 32 | Agent | meta | 91.10 | -8.90 | 87 | 40.2 | -7.53 | -3.30 | -14.50 | 257 |
| 33 | Volume breakout · 1h | breakout | 90.91 | -9.09 | 84 | 22.6 | -12.22 | -2.19 | -15.57 | 108 |
| 34 | Bollinger breakout · 1h | breakout | 90.74 | -9.26 | 87 | 29.9 | -11.08 | -2.02 | -16.14 | 260 |
| 35 | Connors RSI(2) · 1h | reversion | 89.55 | -10.45 | 151 | 41.7 | -22.71 | -6.74 | -24.22 | 201 |
| 36 | RSI momentum · 1h | momentum | 89.27 | -10.73 | 83 | 15.7 | -20.94 | -4.16 | -26.37 | 216 |
| 37 | EMA 20/50 cross · 1h | trend | 88.71 | -11.29 | 62 | 12.9 | -19.12 | -3.53 | -21.33 | 131 |
| 38 | Opening range 15m | breakout | 88.61 | -11.39 | 256 | 25.8 | -17.63 | -4.69 | -20.98 | 700 |
| 39 | Supertrend · 1h | trend | 88.38 | -11.62 | 88 | 12.5 | -21.33 | -4.16 | -26.62 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 88.16 | -11.84 | 164 | 47.0 | -14.17 | -2.35 | -22.24 | 362 |
| 41 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -9.41 | -2.34 | -21.34 | 145 |
| 42 | Keltner breakout · 1h | breakout | 87.48 | -12.52 | 60 | 21.7 | -16.37 | -2.66 | -26.27 | 207 |
| 43 | Ichimoku · 1h | trend | 87.02 | -12.98 | 60 | 13.3 | -18.94 | -3.57 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.51 | -13.49 | 193 | 20.2 | -26.84 | -5.13 | -33.08 | 470 |
| 45 | Triple EMA stack · 1h | trend | 85.26 | -14.74 | 91 | 14.3 | -30.99 | -5.74 | -34.98 | 230 |
| 46 | Z-score reversion · 1h | reversion | 84.81 | -15.19 | 95 | 30.5 | -14.69 | -2.43 | -21.32 | 197 |
| 47 | Donchian 20/10 · 1h | breakout | 84.60 | -15.40 | 81 | 17.3 | -13.69 | -1.82 | -28.38 | 219 |
| 48 | MFI reversion · 1h | reversion | 84.19 | -15.81 | 216 | 30.6 | -15.02 | -2.36 | -20.43 | 145 |
| 49 | Agent (ML meta-label) | meta | 83.99 | -16.01 | 708 | 19.2 | -5.00 | -0.77 | -16.16 | 369 |
| 50 | OBV trend · 1h | momentum | 83.85 | -16.14 | 186 | 17.2 | -29.83 | -5.16 | -37.05 | 321 |
| 51 | MACD zero-line · 1h | trend | 83.72 | -16.29 | 89 | 14.6 | -25.90 | -5.17 | -26.71 | 224 |
| 52 | Three white soldiers | momentum | 82.67 | -17.33 | 249 | 19.7 | -46.42 | -17.56 | -47.79 | 614 |
| 53 | Bollinger reversion · 1h | reversion | 82.26 | -17.74 | 162 | 35.8 | -29.20 | -5.67 | -32.82 | 348 |
| 54 | ROC + volume · 1h | momentum | 81.60 | -18.40 | 199 | 21.6 | -27.94 | -5.01 | -34.58 | 398 |
| 55 | Williams %R · 1h | reversion | 81.60 | -18.40 | 194 | 43.8 | -32.35 | -5.10 | -36.49 | 526 |
| 56 | CCI reversion · 1h | reversion | 80.87 | -19.13 | 177 | 41.8 | -18.23 | -2.27 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.62 | -19.38 | 229 | 21.0 | -41.94 | -8.69 | -46.61 | 680 |
| 58 | RSI(14) reversion · 1h | reversion | 79.91 | -20.09 | 83 | 22.9 | -14.85 | -2.71 | -23.28 | 168 |
| 59 | EMA 9/21 cross · 1h | trend | 79.68 | -20.32 | 143 | 10.5 | -29.37 | -6.11 | -29.99 | 325 |
| 60 | VWAP momentum · 1h | momentum | 77.92 | -22.08 | 449 | 20.5 | -44.19 | -7.70 | -50.50 | 1255 |
| 61 | Candlestick reversal · 1h | reversion | 77.42 | -22.58 | 222 | 28.8 | -36.94 | -6.66 | -38.98 | 536 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.32 | -1.57 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 61.84 | -38.16 | 626 | 23.2 | -77.11 | -19.97 | -78.68 | 1727 |
| 64 | Volume breakout | breakout | 61.62 | -38.38 | 376 | 14.1 | -63.48 | -18.82 | -64.54 | 880 |
| 65 | Squeeze breakout | breakout | 58.67 | -41.33 | 489 | 14.1 | -65.65 | -21.66 | -66.58 | 1204 |
| 66 | Donchian 55/20 | breakout | 58.33 | -41.66 | 494 | 18.6 | -70.32 | -17.38 | -73.50 | 1278 |
| 67 | RSI(14) reversion | reversion | 57.38 | -42.62 | 740 | 26.4 | -74.58 | -16.49 | -75.05 | 1615 |
| 68 | EMA 20/50 cross | trend | 55.94 | -44.06 | 536 | 19.0 | -76.85 | -15.70 | -80.87 | 1444 |
| 69 | VWAP reversion | reversion | 53.69 | -46.31 | 752 | 25.3 | -71.63 | -14.62 | -72.28 | 1499 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -29.94 | -98.78 | 5309 |
| 71 | Keltner breakout | breakout | 50.59 | -49.41 | 701 | 16.8 | -82.63 | -25.33 | -83.82 | 1807 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -32.23 | -93.86 | 2599 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.67 | -20.59 | -88.38 | 1900 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.33 | -24.85 | -91.32 | 2355 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.06 | -25.73 | -91.25 | 2255 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.55 | -33.07 | -97.64 | 3521 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.74 | -37.33 | -96.74 | 3588 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.26 | -27.48 | -94.43 | 2518 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.70 | -27.20 | -82.70 | 1708 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.81 | -99.38 | 5742 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.40 | -25.88 | -92.18 | 2623 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.94 | -31.47 | -95.94 | 3452 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -40.79 | -99.75 | 6197 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.58 | -28.99 | -91.65 | 2352 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -38.76 | -97.67 | 3616 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.24 | -98.49 | 4705 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.88 | -32.69 | -94.15 | 2800 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -38.51 | -99.52 | 6167 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.60 | -21.99 | -87.01 | 2137 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.67 | -25.90 | -88.06 | 2136 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.32 | -95.98 | 3762 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.05 | -32.46 | -89.31 | 2119 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -32.90 | -95.83 | 4104 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.04 | -99.90 | 8278 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T18:25 | Squeeze breakout | sell | PLTR | 14.67 | -0.05 | stop-loss |
| 2026-10-20T18:25 | Donchian 55/20 | sell | ETHU | 4.87 | 0.07 | exit signal |
| 2026-10-20T18:18 | Copy: Insider buying | buy | IAM | 1.02 | — | entry |
| 2026-10-20T18:18 | Copy: Insider buying | buy | CTY | 10.87 | — | rebalance up |
| 2026-10-20T18:18 | Copy: Insider buying | sell | FLSC | 11.89 | -0.37 | target is flat |
| 2026-10-20T18:16 | Agent (ML meta-label) | buy | QQQ | 7.38 | — | entry |
| 2026-10-20T18:16 | Agent (ML meta-label) | sell | IWM | 7.01 | -0.00 | selected signal exited |
| 2026-10-20T18:16 | Volume breakout | buy | LABU | 15.42 | — | entry signal |
| 2026-10-20T18:16 | Keltner breakout | buy | LABU | 12.66 | — | entry signal |
| 2026-10-20T18:16 | Donchian 55/20 | sell | MSTR | 3.92 | 0.02 | exit signal |
| 2026-10-20T18:16 | Donchian 55/20 | sell | COIN | 3.86 | -0.04 | exit signal |
| 2026-10-20T18:16 | ROC + volume | buy | LABU | 15.48 | — | entry signal |
| 2026-10-20T18:10 | Agent (ML meta-label) | buy | IWM | 7.01 | — | entry |
| 2026-10-20T18:10 | Agent (ML meta-label) | sell | AAPL | 7.01 | -0.00 | selected signal exited |
| 2026-10-20T18:10 | ROC + volume | sell | SOL-USD | 12.39 | -0.09 | exit signal |
| 2026-10-20T18:10 | ROC + volume | sell | LABU | 15.52 | 0.02 | target is flat |
| 2026-10-20T18:10 | EMA 20/50 cross | buy | TQQQ | 1.55 | — | entry |
| 2026-10-20T18:10 | EMA 20/50 cross | buy | SOXL | 3.51 | — | entry signal |
| 2026-10-20T18:10 | EMA 20/50 cross | sell | SQQQ | 5.06 | -0.02 | exit signal |
| 2026-10-20T18:05 | Squeeze breakout | sell | BTC-USD | 14.63 | -0.11 | exit signal |
| 2026-10-20T18:05 | Squeeze breakout | sell | BITX | 14.66 | -0.08 | exit signal |
| 2026-10-20T18:05 | ROC + volume | buy | LABU | 15.49 | — | entry |
| 2026-10-20T18:05 | ROC + volume | sell | DOGE-USD | 12.39 | -0.07 | exit signal |
| 2026-10-20T18:05 | ROC + volume | sell | BITX | 15.46 | -0.06 | exit signal |
| 2026-10-20T18:01 | EMA 20/50 cross | buy | QQQ | 2.45 | — | entry signal |
| 2026-10-20T17:55 | Agent (ML meta-label) | buy | AAPL | 7.01 | — | entry |
| 2026-10-20T17:55 | OBV trend · 1h | buy | AMZN | 8.59 | — | entry |
| 2026-10-20T17:55 | OBV trend · 1h | sell | SOL-USD | 4.35 | -0.00 | rebalance down |
| 2026-10-20T17:55 | OBV trend · 1h | sell | BTC-USD | 4.23 | -0.03 | rebalance down |
| 2026-10-20T17:55 | Squeeze breakout | sell | MSFT | 14.67 | -0.04 | stop-loss |
| 2026-10-20T17:55 | Keltner breakout | sell | MSFT | 12.62 | -0.05 | stop-loss |
| 2026-10-20T17:55 | EMA 20/50 cross | buy | TECL | 4.01 | — | entry signal |
| 2026-10-20T17:50 | Agent (ML meta-label) | sell | QQQ | 7.39 | -0.00 | selected signal exited |
| 2026-10-20T17:50 | Squeeze breakout | buy | PLTR | 14.73 | — | entry signal |
| 2026-10-20T17:50 | ROC + volume | buy | BITX | 3.14 | — | rebalance up |
| 2026-10-20T17:50 | ROC + volume | sell | XRP-USD | 12.40 | -0.07 | exit signal |
| 2026-10-20T17:50 | ROC + volume | sell | ETH-USD | 12.40 | -0.07 | exit signal |
| 2026-10-20T17:50 | EMA 20/50 cross | buy | NVDA | 4.32 | — | entry signal |
| 2026-10-20T17:45 | MFI reversion · 1h | buy | TECL | 5.32 | — | rebalance up |
| 2026-10-20T17:45 | MFI reversion · 1h | sell | GOOGL | 12.04 | -0.01 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 18:25:05.000152+00:00 -> 2026-10-20 18:35:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
