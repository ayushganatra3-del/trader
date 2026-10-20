# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T15:55:05.000125+00:00 · 29686 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.02 (-8.98%)

Closed trades 87, win rate 40.2%, fees £2.92, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.59 | +0.31 |

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

Today: 22332 decisions in 2358 calls, $0.2832 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T15:55 | 11 / 16 / 2 | cash |  |
| Breezy | 2026-10-20T15:55 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-10-20T15:55 | 8 / 20 / 1 | MSTR 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | BITX | 1.97 | +4.12% | 6 |
| VWAP reversion | ETHU | 1.90 | +4.27% | 5 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.39 | 5.39 | 0 | — | 7.00 | 3.36 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -0.91 | -0.17 | -9.24 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 100.99 | 0.99 | 9 | 44.4 | -12.97 | -0.89 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.03 | -0.97 | 0 | — | -0.01 | 0.04 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 59 | 35.6 | 2.43 | 1.40 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.73 | -1.27 | 0 | — | -0.24 | -0.02 | -5.15 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.65 | -1.35 | 3 | 33.3 | 4.40 | 1.01 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 14 | Hold BTC | benchmark | 97.46 | -2.54 | 0 | — | 20.08 | 2.67 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.16 | -2.85 | 0 | — | -3.70 | -1.38 | -7.04 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.00 | -2.26 | -5.83 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.89 | -3.11 | 0 | — | -0.03 | 0.05 | -5.31 | 1 |
| 18 | Agent (rotation) | meta | 96.16 | -3.84 | 114 | 31.6 | -6.64 | -2.88 | -8.29 | 322 |
| 19 | Donchian 55/20 · 1h | breakout | 95.88 | -4.12 | 40 | 15.0 | -17.65 | -3.55 | -23.04 | 104 |
| 20 | Copy: Insider buying | copy | 95.68 | -4.32 | 23 | 43.5 | -11.10 | -1.88 | -20.62 | 72 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Trend pullback · 1h | trend | 95.44 | -4.56 | 90 | 23.3 | -20.52 | -6.13 | -20.78 | 135 |
| 23 | ADX DI cross · 1h | trend | 94.53 | -5.47 | 89 | 18.0 | -12.89 | -2.29 | -16.63 | 262 |
| 24 | Daily: Momentum burst | daily | 94.06 | -5.94 | 6 | 16.7 | -6.69 | -0.88 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.29 | 1.37 | -6.51 | 198 |
| 26 | Opening range 30m | breakout | 92.49 | -7.51 | 208 | 29.3 | -12.98 | -3.73 | -17.26 | 565 |
| 27 | Squeeze breakout · 1h | breakout | 91.55 | -8.45 | 46 | 21.7 | -3.75 | -0.85 | -11.32 | 99 |
| 28 | Daily: Bullish score | daily | 91.45 | -8.55 | 7 | 0.0 | -6.39 | -0.67 | -13.10 | 13 |
| 29 | Parabolic SAR · 1h | trend | 91.38 | -8.62 | 105 | 21.9 | -17.58 | -3.76 | -23.78 | 275 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.73 | -2.42 | -16.91 | 1 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 91.08 | -8.92 | 0 | — | 1.12 | 0.34 | -14.37 | 1 |
| 32 | Agent | meta | 91.02 | -8.98 | 87 | 40.2 | -16.58 | -5.18 | -18.23 | 279 |
| 33 | Bollinger breakout · 1h | breakout | 90.52 | -9.48 | 87 | 29.9 | -10.99 | -2.00 | -15.86 | 259 |
| 34 | Volume breakout · 1h | breakout | 90.48 | -9.52 | 84 | 22.6 | -12.58 | -2.26 | -15.57 | 107 |
| 35 | Connors RSI(2) · 1h | reversion | 89.46 | -10.54 | 150 | 41.3 | -22.73 | -6.75 | -24.22 | 202 |
| 36 | RSI momentum · 1h | momentum | 88.98 | -11.02 | 83 | 15.7 | -20.08 | -4.00 | -25.22 | 213 |
| 37 | EMA 20/50 cross · 1h | trend | 88.62 | -11.38 | 62 | 12.9 | -20.98 | -3.95 | -23.07 | 131 |
| 38 | Opening range 15m | breakout | 88.60 | -11.40 | 256 | 25.8 | -17.52 | -4.63 | -20.98 | 700 |
| 39 | Stochastic reversion · 1h | reversion | 88.18 | -11.82 | 163 | 46.6 | -14.01 | -2.32 | -22.24 | 362 |
| 40 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -15.07 | -3.91 | -19.13 | 133 |
| 41 | Supertrend · 1h | trend | 88.07 | -11.93 | 88 | 12.5 | -21.96 | -4.44 | -26.86 | 222 |
| 42 | Keltner breakout · 1h | breakout | 87.26 | -12.74 | 60 | 21.7 | -16.32 | -2.65 | -26.20 | 204 |
| 43 | Ichimoku · 1h | trend | 86.71 | -13.29 | 60 | 13.3 | -19.17 | -3.61 | -19.92 | 119 |
| 44 | MACD cross · 1h | trend | 86.40 | -13.60 | 192 | 20.3 | -26.96 | -5.16 | -33.11 | 472 |
| 45 | Triple EMA stack · 1h | trend | 85.17 | -14.83 | 91 | 14.3 | -31.06 | -5.69 | -35.47 | 231 |
| 46 | Z-score reversion · 1h | reversion | 84.87 | -15.13 | 95 | 30.5 | -14.50 | -2.39 | -21.32 | 197 |
| 47 | MFI reversion · 1h | reversion | 84.35 | -15.64 | 212 | 31.1 | -15.10 | -2.34 | -20.43 | 146 |
| 48 | Donchian 20/10 · 1h | breakout | 84.13 | -15.87 | 81 | 17.3 | -14.49 | -1.93 | -29.35 | 222 |
| 49 | Agent (ML meta-label) | meta | 83.88 | -16.12 | 702 | 19.2 | -2.73 | -0.36 | -14.58 | 382 |
| 50 | OBV trend · 1h | momentum | 83.58 | -16.42 | 186 | 17.2 | -30.91 | -5.41 | -37.46 | 319 |
| 51 | MACD zero-line · 1h | trend | 83.33 | -16.67 | 89 | 14.6 | -25.94 | -5.20 | -26.23 | 222 |
| 52 | Three white soldiers | momentum | 82.79 | -17.21 | 248 | 19.8 | -46.94 | -18.15 | -47.76 | 614 |
| 53 | Bollinger reversion · 1h | reversion | 82.30 | -17.70 | 162 | 35.8 | -28.13 | -5.39 | -33.53 | 352 |
| 54 | Williams %R · 1h | reversion | 81.59 | -18.41 | 193 | 43.5 | -32.25 | -5.08 | -36.49 | 526 |
| 55 | ROC + volume · 1h | momentum | 81.50 | -18.50 | 199 | 21.6 | -25.95 | -4.48 | -33.89 | 394 |
| 56 | CCI reversion · 1h | reversion | 80.92 | -19.08 | 177 | 41.8 | -16.89 | -2.07 | -27.44 | 445 |
| 57 | Heikin-Ashi · 1h | trend | 80.53 | -19.47 | 228 | 21.1 | -40.70 | -8.52 | -45.41 | 679 |
| 58 | RSI(14) reversion · 1h | reversion | 80.04 | -19.96 | 83 | 22.9 | -16.08 | -2.88 | -23.28 | 178 |
| 59 | EMA 9/21 cross · 1h | trend | 79.38 | -20.62 | 143 | 10.5 | -29.44 | -6.13 | -30.15 | 322 |
| 60 | VWAP momentum · 1h | momentum | 77.97 | -22.03 | 445 | 20.2 | -42.38 | -6.96 | -49.84 | 1258 |
| 61 | Candlestick reversal · 1h | reversion | 77.52 | -22.48 | 220 | 28.2 | -32.23 | -5.49 | -35.30 | 551 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.64 | -1.59 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 62.34 | -37.66 | 618 | 23.1 | -76.71 | -19.13 | -78.69 | 1724 |
| 64 | Volume breakout | breakout | 61.70 | -38.30 | 376 | 14.1 | -63.08 | -18.79 | -64.20 | 870 |
| 65 | Squeeze breakout | breakout | 58.95 | -41.05 | 485 | 14.2 | -64.33 | -19.69 | -66.58 | 1213 |
| 66 | Donchian 55/20 | breakout | 58.21 | -41.79 | 488 | 18.0 | -69.92 | -16.85 | -73.50 | 1284 |
| 67 | RSI(14) reversion | reversion | 57.43 | -42.57 | 737 | 26.2 | -74.56 | -16.48 | -75.06 | 1626 |
| 68 | EMA 20/50 cross | trend | 56.02 | -43.98 | 532 | 19.2 | -77.19 | -16.29 | -80.87 | 1442 |
| 69 | VWAP reversion | reversion | 53.69 | -46.31 | 752 | 25.3 | -71.58 | -14.59 | -72.28 | 1511 |
| 70 | Keltner breakout | breakout | 50.92 | -49.08 | 698 | 16.9 | -82.46 | -24.69 | -83.82 | 1809 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -30.04 | -98.76 | 5312 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.48 | -31.12 | -93.85 | 2581 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.68 | -20.65 | -88.38 | 1904 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.51 | -25.29 | -91.32 | 2356 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.92 | -25.43 | -91.18 | 2237 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.48 | -32.09 | -97.64 | 3516 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.67 | -35.61 | -96.84 | 3582 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -27.88 | -94.44 | 2520 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.69 | -26.83 | -82.72 | 1691 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.85 | -99.38 | 5751 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.31 | -25.65 | -92.18 | 2622 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.91 | -31.31 | -95.91 | 3442 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -39.62 | -99.76 | 6193 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.54 | -28.92 | -91.68 | 2350 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -37.94 | -97.71 | 3605 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.22 | -98.49 | 4716 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.87 | -32.84 | -94.17 | 2799 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -38.57 | -99.53 | 6184 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.26 | -87.09 | 2163 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.80 | -26.02 | -88.25 | 2155 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.18 | -95.98 | 3760 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.12 | -32.79 | -89.26 | 2125 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -33.03 | -95.83 | 4118 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -42.99 | -99.90 | 8246 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T15:55 | Agent (ML meta-label) | buy | AMZN | 8.39 | — | entry |
| 2026-10-20T15:55 | Agent (ML meta-label) | sell | QQQ | 7.63 | -0.01 | selected signal exited |
| 2026-10-20T15:55 | Agent (ML meta-label) | sell | COIN | 7.59 | -0.05 | selected signal exited |
| 2026-10-20T15:55 | EMA 20/50 cross | buy | NVDA | 5.09 | — | entry signal |
| 2026-10-20T15:40 | ROC + volume | sell | MSTR | 15.65 | 0.23 | exit signal |
| 2026-10-20T15:40 | EMA 20/50 cross | sell | TQQQ | 1.14 | -0.02 | stop-loss |
| 2026-10-20T15:40 | EMA 20/50 cross | sell | SOXL | 3.23 | -0.12 | stop-loss |
| 2026-10-20T15:40 | EMA 20/50 cross | sell | QQQ | 3.32 | -0.02 | stop-loss |
| 2026-10-20T15:40 | EMA 20/50 cross | sell | NVDA | 3.32 | -0.03 | stop-loss |
| 2026-10-20T15:40 | EMA 20/50 cross | sell | COIN | 2.84 | -0.07 | stop-loss |
| 2026-10-20T15:35 | Candlestick reversal · 1h | sell | GOOGL | 6.55 | -0.13 | stop-loss |
| 2026-10-20T15:35 | Squeeze breakout | sell | TSLA | 14.77 | 0.08 | stop-loss |
| 2026-10-20T15:35 | Keltner breakout | sell | TSLA | 12.72 | -0.05 | stop-loss |
| 2026-10-20T15:35 | Keltner breakout | sell | IWM | 12.77 | 0.02 | stop-loss |
| 2026-10-20T15:35 | ROC + volume | sell | TNA | 15.56 | 0.11 | stop-loss |
| 2026-10-20T15:35 | ROC + volume | sell | IWM | 15.62 | 0.00 | exit signal |
| 2026-10-20T15:35 | EMA 20/50 cross | sell | AMD | 3.46 | -0.05 | stop-loss |
| 2026-10-20T15:30 | Agent (rotation) | sell | TQQQ | 31.80 | -0.43 | selected signal exited |
| 2026-10-20T15:30 | Day trade: Stocks in Play ORB | sell | LABU | 24.89 | 0.20 | target is flat |
| 2026-10-20T15:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 105.38 | -1.44 | target is flat |
| 2026-10-20T15:30 | Agent (ML meta-label) | buy | TSLA | 4.19 | — | rebalance up |
| 2026-10-20T15:30 | Agent (ML meta-label) | sell | GOOGL | 4.75 | -0.00 | selected signal exited |
| 2026-10-20T15:30 | MFI reversion · 1h | buy | UPRO | 2.03 | — | rebalance up |
| 2026-10-20T15:30 | MFI reversion · 1h | buy | QQQ | 12.04 | — | entry signal |
| 2026-10-20T15:30 | MFI reversion · 1h | sell | SPY | 14.07 | -0.02 | target is flat |
| 2026-10-20T15:30 | CCI reversion · 1h | buy | META | 6.74 | — | entry signal |
| 2026-10-20T15:30 | CCI reversion · 1h | sell | TNA | 4.22 | 0.17 | exit signal |
| 2026-10-20T15:30 | CCI reversion · 1h | sell | IWM | 4.10 | 0.04 | exit signal |
| 2026-10-20T15:30 | Connors RSI(2) · 1h | buy | AAPL | 22.36 | — | entry signal |
| 2026-10-20T15:30 | Candlestick reversal · 1h | sell | MSTR | 5.60 | 0.12 | target is flat |
| 2026-10-20T15:30 | Volume breakout · 1h | buy | TSLA | 4.69 | — | rebalance up |
| 2026-10-20T15:30 | Volume breakout · 1h | buy | BTC-USD | 4.56 | — | rebalance up |
| 2026-10-20T15:30 | Volume breakout · 1h | sell | ETH-USD | 18.00 | -0.31 | stop-loss |
| 2026-10-20T15:30 | Volume breakout · 1h | sell | AMZN | 18.14 | -0.03 | target is flat |
| 2026-10-20T15:30 | Squeeze breakout · 1h | sell | ETH-USD | 22.79 | -0.41 | stop-loss |
| 2026-10-20T15:30 | Keltner breakout · 1h | buy | TSLA | 5.76 | — | rebalance up |
| 2026-10-20T15:30 | Keltner breakout · 1h | buy | TNA | 5.80 | — | rebalance up |
| 2026-10-20T15:30 | Keltner breakout · 1h | buy | LABU | 5.66 | — | rebalance up |
| 2026-10-20T15:30 | Keltner breakout · 1h | buy | IWM | 5.74 | — | rebalance up |
| 2026-10-20T15:30 | Keltner breakout · 1h | buy | BTC-USD | 5.82 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 15:55:05.000125+00:00 -> 2026-10-20 16:05:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
