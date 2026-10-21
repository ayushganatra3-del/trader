# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T18:50:05.000131+00:00 · 30994 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.62 (-9.38%)

Closed trades 91, win rate 40.7%, fees £3.01, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 18.10 | -0.03 |

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

Today: 32694 decisions in 2745 calls, $0.4042 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T18:50 | 1 / 6 / 24 | cash |  |
| Breezy | 2026-10-21T18:50 | 0 / 24 / 7 | cash |  |
| Boozy | 2026-10-21T18:50 | 4 / 23 / 4 | MSTR 70% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.17 | 6.17 | 0 | — | 8.97 | 4.20 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.78 | 3.78 | 14 | 50.0 | 6.20 | 2.02 | -4.29 | 23 |
| 5 | Max aggression: 5-day momentum | meta | 103.09 | 3.09 | 10 | 50.0 | -5.82 | -0.20 | -34.64 | 26 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.39 | 0.39 | 4 | 50.0 | 9.88 | 2.05 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold BTC | benchmark | 99.79 | -0.21 | 0 | — | 15.92 | 2.27 | -8.68 | 1 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.60 | -0.40 | 0 | — | 1.12 | 0.54 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.35 | -0.65 | 0 | — | 1.29 | 0.79 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.06 | -0.94 | 63 | 34.9 | 2.52 | 1.48 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.44 | -2.56 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.11 | -2.89 | 0 | — | -3.90 | -1.48 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.96 | -1.68 | -5.83 | 1 |
| 18 | Copy: Insider buying | copy | 96.93 | -3.07 | 25 | 40.0 | -11.08 | -1.87 | -20.62 | 72 |
| 19 | Donchian 55/20 · 1h | breakout | 96.46 | -3.54 | 41 | 17.1 | -14.00 | -2.83 | -16.00 | 103 |
| 20 | Agent (rotation) | meta | 95.96 | -4.04 | 116 | 31.0 | -5.91 | -3.20 | -7.45 | 284 |
| 21 | ADX DI cross · 1h | trend | 95.90 | -4.10 | 91 | 19.8 | -11.84 | -2.13 | -16.49 | 260 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 95.40 | -4.61 | 6 | 16.7 | -8.61 | -1.24 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.89 | -5.11 | 92 | 23.9 | -20.05 | -6.14 | -20.15 | 131 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 5.78 | 1.80 | -7.13 | 207 |
| 26 | Parabolic SAR · 1h | trend | 93.75 | -6.25 | 108 | 23.1 | -15.80 | -3.43 | -19.79 | 272 |
| 27 | Opening range 30m | breakout | 93.64 | -6.37 | 225 | 32.4 | -10.78 | -3.03 | -17.26 | 571 |
| 28 | Squeeze breakout · 1h | breakout | 93.50 | -6.50 | 46 | 21.7 | -0.88 | -0.11 | -11.48 | 98 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 93.25 | -6.75 | 0 | — | 2.99 | 0.62 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.74 | -7.26 | 87 | 29.9 | -9.05 | -1.59 | -15.41 | 262 |
| 31 | Daily: Bullish score | daily | 91.84 | -8.16 | 8 | 0.0 | -2.73 | -0.19 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.83 | -1.83 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 91.22 | -8.78 | 91 | 24.2 | -12.34 | -2.19 | -13.90 | 111 |
| 34 | Agent | meta | 90.62 | -9.38 | 91 | 40.7 | -16.09 | -7.34 | -20.35 | 253 |
| 35 | Supertrend · 1h | trend | 90.44 | -9.56 | 88 | 12.5 | -20.93 | -4.11 | -27.05 | 219 |
| 36 | RSI momentum · 1h | momentum | 90.06 | -9.94 | 84 | 16.7 | -21.21 | -4.22 | -23.28 | 223 |
| 37 | Connors RSI(2) · 1h | reversion | 89.86 | -10.14 | 158 | 42.4 | -21.98 | -6.54 | -23.75 | 194 |
| 38 | Stochastic reversion · 1h | reversion | 89.46 | -10.54 | 169 | 47.3 | -13.69 | -2.24 | -22.24 | 362 |
| 39 | EMA 20/50 cross · 1h | trend | 89.22 | -10.78 | 62 | 12.9 | -20.65 | -3.54 | -23.67 | 138 |
| 40 | Keltner breakout · 1h | breakout | 88.41 | -11.59 | 61 | 23.0 | -18.25 | -3.50 | -25.97 | 203 |
| 41 | Opening range 15m | breakout | 88.34 | -11.65 | 274 | 28.8 | -16.30 | -4.37 | -19.75 | 710 |
| 42 | MACD cross · 1h | trend | 87.77 | -12.23 | 199 | 21.1 | -23.43 | -4.40 | -26.94 | 467 |
| 43 | Agent (aggressive) | meta | 87.52 | -12.48 | 45 | 35.6 | -12.51 | -3.57 | -17.99 | 129 |
| 44 | Ichimoku · 1h | trend | 87.31 | -12.69 | 60 | 13.3 | -17.39 | -3.24 | -20.25 | 118 |
| 45 | Z-score reversion · 1h | reversion | 86.70 | -13.30 | 102 | 34.3 | -11.54 | -1.79 | -21.32 | 196 |
| 46 | Donchian 20/10 · 1h | breakout | 86.33 | -13.67 | 83 | 19.3 | -19.56 | -3.58 | -29.02 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.88 | -14.12 | 92 | 15.2 | -29.27 | -5.38 | -30.01 | 223 |
| 48 | MFI reversion · 1h | reversion | 85.16 | -14.85 | 228 | 32.9 | -14.41 | -2.18 | -21.11 | 140 |
| 49 | Agent (ML meta-label) | meta | 84.87 | -15.13 | 731 | 20.1 | -10.28 | -1.70 | -16.42 | 360 |
| 50 | MACD zero-line · 1h | trend | 84.65 | -15.35 | 92 | 15.2 | -23.16 | -4.48 | -26.06 | 227 |
| 51 | OBV trend · 1h | momentum | 84.39 | -15.61 | 188 | 17.6 | -32.33 | -6.05 | -33.47 | 316 |
| 52 | ROC + volume · 1h | momentum | 83.29 | -16.71 | 212 | 23.6 | -26.74 | -4.79 | -33.33 | 393 |
| 53 | Three white soldiers | momentum | 82.63 | -17.38 | 257 | 20.6 | -46.05 | -17.86 | -46.93 | 608 |
| 54 | Bollinger reversion · 1h | reversion | 82.56 | -17.44 | 163 | 36.2 | -29.11 | -5.62 | -32.84 | 348 |
| 55 | Williams %R · 1h | reversion | 82.50 | -17.50 | 199 | 44.7 | -31.59 | -4.90 | -36.64 | 517 |
| 56 | CCI reversion · 1h | reversion | 82.07 | -17.93 | 188 | 43.6 | -20.32 | -2.64 | -27.44 | 436 |
| 57 | Heikin-Ashi · 1h | trend | 81.65 | -18.35 | 237 | 21.1 | -43.30 | -9.23 | -46.38 | 679 |
| 58 | EMA 9/21 cross · 1h | trend | 81.17 | -18.83 | 143 | 10.5 | -26.81 | -5.17 | -29.95 | 331 |
| 59 | RSI(14) reversion · 1h | reversion | 81.06 | -18.94 | 85 | 24.7 | -14.87 | -2.69 | -23.28 | 171 |
| 60 | VWAP momentum · 1h | momentum | 79.29 | -20.71 | 475 | 21.3 | -45.11 | -8.23 | -51.84 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 78.72 | -21.28 | 230 | 30.0 | -35.81 | -6.32 | -39.03 | 540 |
| 62 | Max aggression: 1-day momentum | meta | 77.22 | -22.78 | 17 | 29.4 | -34.10 | -2.13 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.97 | -40.03 | 676 | 23.4 | -77.74 | -21.82 | -78.93 | 1715 |
| 64 | Volume breakout | breakout | 59.10 | -40.90 | 400 | 13.5 | -65.00 | -20.36 | -65.21 | 871 |
| 65 | RSI(14) reversion | reversion | 57.14 | -42.86 | 751 | 26.6 | -73.82 | -15.93 | -74.89 | 1605 |
| 66 | Donchian 55/20 | breakout | 56.78 | -43.22 | 524 | 18.7 | -71.88 | -19.07 | -74.04 | 1289 |
| 67 | Squeeze breakout | breakout | 56.36 | -43.63 | 519 | 13.9 | -67.23 | -23.24 | -67.81 | 1215 |
| 68 | EMA 20/50 cross | trend | 55.59 | -44.41 | 563 | 19.5 | -78.64 | -18.83 | -80.89 | 1441 |
| 69 | VWAP reversion | reversion | 54.04 | -45.96 | 761 | 25.6 | -71.17 | -14.36 | -72.15 | 1464 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.76 | -30.97 | -98.80 | 5280 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.90 | -33.45 | -94.27 | 2611 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.43 | -21.88 | -88.67 | 1902 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.90 | -26.53 | -91.71 | 2368 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.45 | -26.30 | -91.46 | 2280 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.62 | -33.76 | -97.78 | 3509 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.87 | -37.53 | -96.96 | 3584 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.58 | -27.98 | -94.75 | 2554 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.95 | -27.78 | -83.44 | 1740 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.77 | -99.37 | 5703 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.96 | -28.38 | -92.66 | 2634 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.86 | -31.40 | -95.89 | 3471 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.44 | -99.76 | 6172 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.66 | -29.61 | -91.90 | 2343 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -39.42 | -97.81 | 3639 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.33 | -98.48 | 4687 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.21 | -35.08 | -94.44 | 2814 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.28 | -27.45 | -84.44 | 1812 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.20 | -99.54 | 6151 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.84 | -22.46 | -87.01 | 2132 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.71 | -25.95 | -88.05 | 2123 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -32.63 | -95.93 | 3739 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -33.31 | -89.40 | 2107 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -33.26 | -95.75 | 4064 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.05 | -99.91 | 8302 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T18:50 | Agent (ML meta-label) | buy | ETHU | 9.43 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T18:50 | Agent (ML meta-label) | sell | SPY | 9.43 | -0.02 | selected signal exited |
| 2026-10-21T18:50 | RSI(14) reversion | sell | SQQQ | 14.28 | -0.01 | exit signal |
| 2026-10-21T18:50 | Volume breakout | buy | SQQQ | 14.79 | — | entry signal |
| 2026-10-21T18:50 | Volume breakout | sell | XRP-USD | 14.70 | -0.10 | exit signal |
| 2026-10-21T18:50 | Squeeze breakout | sell | GOOGL | 14.11 | -0.04 | exit signal |
| 2026-10-21T18:50 | Squeeze breakout | sell | DOGE-USD | 13.98 | -0.16 | stop-loss |
| 2026-10-21T18:50 | Donchian 55/20 | buy | AMD | 4.73 | — | entry |
| 2026-10-21T18:50 | Donchian 55/20 | sell | MSFT | 2.28 | -0.01 | exit signal |
| 2026-10-21T18:50 | Donchian 55/20 | sell | AMZN | 3.33 | -0.01 | exit signal |
| 2026-10-21T18:50 | Gap and go | sell | TQQQ | 18.92 | 0.16 | stop-loss |
| 2026-10-21T18:50 | Gap and go | sell | COIN | 23.61 | 0.25 | stop-loss |
| 2026-10-21T18:50 | ROC + volume | sell | UPRO | 14.99 | -0.05 | stop-loss |
| 2026-10-21T18:45 | Agent (ML meta-label) | buy | SPY | 9.45 | — | entry |
| 2026-10-21T18:45 | Agent (ML meta-label) | sell | ETHU | 9.43 | -0.02 | selected signal exited |
| 2026-10-21T18:40 | Agent (ML meta-label) | buy | ETHU | 9.45 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T18:40 | Ichimoku · 1h | buy | COIN | 4.38 | — | rebalance up |
| 2026-10-21T18:40 | Ichimoku · 1h | sell | MSTR | 4.38 | 0.01 | rebalance down |
| 2026-10-21T18:30 | Agent (rotation) | buy | TQQQ | 32.08 | — | entry |
| 2026-10-21T18:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 104.44 | — | entry |
| 2026-10-21T18:30 | ROC + volume · 1h | buy | IWM | 3.98 | — | entry |
| 2026-10-21T18:30 | ROC + volume · 1h | buy | AMZN | 3.98 | — | entry signal |
| 2026-10-21T18:30 | ROC + volume · 1h | sell | ETH-USD | 4.36 | 0.05 | rebalance down |
| 2026-10-21T18:30 | ROC + volume · 1h | sell | BTC-USD | 4.30 | 0.02 | rebalance down |
| 2026-10-21T18:30 | Heikin-Ashi · 1h | buy | MSFT | 1.10 | — | entry |
| 2026-10-21T18:30 | Heikin-Ashi · 1h | buy | DOGE-USD | 3.42 | — | entry |
| 2026-10-21T18:30 | Heikin-Ashi · 1h | sell | META | 4.52 | -0.02 | exit signal |
| 2026-10-21T18:30 | Ichimoku · 1h | buy | COIN | 8.40 | — | entry signal |
| 2026-10-21T18:30 | Ichimoku · 1h | sell | AMZN | 4.53 | -0.00 | rebalance down |
| 2026-10-21T18:30 | MACD zero-line · 1h | buy | NVDA | 6.07 | — | entry |
| 2026-10-21T18:30 | MACD zero-line · 1h | buy | COIN | 6.07 | — | entry |
| 2026-10-21T18:30 | MACD zero-line · 1h | buy | AAPL | 6.07 | — | entry signal |
| 2026-10-21T18:30 | MACD zero-line · 1h | sell | MSTR | 4.49 | 0.04 | rebalance down |
| 2026-10-21T18:30 | MACD zero-line · 1h | sell | LABU | 4.37 | -0.01 | rebalance down |
| 2026-10-21T18:30 | MACD zero-line · 1h | sell | ETHU | 4.65 | 0.05 | rebalance down |
| 2026-10-21T18:30 | MACD zero-line · 1h | sell | BITX | 4.61 | 0.19 | rebalance down |
| 2026-10-21T18:25 | Volume breakout · 1h | buy | TECL | 11.44 | — | entry |
| 2026-10-21T18:25 | Volume breakout · 1h | sell | TQQQ | 5.09 | -0.01 | target is flat |
| 2026-10-21T18:25 | Volume breakout · 1h | sell | MSTR | 10.16 | 0.00 | target is flat |
| 2026-10-21T18:25 | OBV trend · 1h | buy | AMZN | 5.02 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 18:50:05.000131+00:00 -> 2026-10-21 19:00:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
