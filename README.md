# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T17:55:05.000149+00:00 · 29770 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.07 (-8.93%)

Closed trades 87, win rate 40.2%, fees £2.92, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.64 | +0.36 |

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

Today: 29826 decisions in 2610 calls, $0.3706 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T17:55 | 8 / 11 / 11 | LABU 16%, SOXL 15%, AMD 14% |  |
| Breezy | 2026-10-20T17:55 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-20T17:55 | 7 / 22 / 1 | MSTR 75% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.65 | 5.65 | 0 | — | 7.23 | 3.45 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 102.23 | 2.23 | 9 | 44.4 | -12.02 | -0.78 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.15 | -0.85 | 0 | — | 0.01 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.95 | -1.05 | 59 | 35.6 | 2.42 | 1.39 | -1.45 | 61 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.77 | -1.23 | 3 | 33.3 | 4.62 | 1.06 | -7.93 | 8 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 98.62 | -1.38 | 0 | — | -0.12 | 0.03 | -5.15 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 14 | Hold BTC | benchmark | 97.95 | -2.05 | 0 | — | 20.65 | 2.73 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.07 | -2.93 | 0 | — | -4.14 | -1.58 | -7.04 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.93 | -2.22 | -5.83 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.96 | -3.04 | 0 | — | 0.03 | 0.07 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.26 | -3.74 | 40 | 15.0 | -18.35 | -3.62 | -22.00 | 103 |
| 19 | Agent (rotation) | meta | 96.13 | -3.87 | 114 | 31.6 | -7.14 | -3.22 | -9.02 | 302 |
| 20 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.18 | -3.18 | -6.31 | 33 |
| 21 | Trend pullback · 1h | trend | 95.47 | -4.53 | 90 | 23.3 | -20.49 | -6.14 | -20.75 | 133 |
| 22 | Copy: Insider buying | copy | 95.16 | -4.84 | 23 | 43.5 | -12.80 | -2.21 | -20.62 | 72 |
| 23 | ADX DI cross · 1h | trend | 94.89 | -5.11 | 89 | 18.0 | -11.55 | -2.09 | -15.39 | 255 |
| 24 | Daily: Momentum burst | daily | 94.40 | -5.60 | 6 | 16.7 | -6.45 | -0.84 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.28 | 1.37 | -6.51 | 198 |
| 26 | Opening range 30m | breakout | 92.80 | -7.20 | 208 | 29.3 | -12.78 | -3.64 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.96 | -8.04 | 105 | 21.9 | -18.38 | -3.94 | -22.26 | 274 |
| 28 | Squeeze breakout · 1h | breakout | 91.82 | -8.18 | 46 | 21.7 | -2.77 | -0.59 | -11.34 | 98 |
| 29 | Daily: Bullish score | daily | 91.59 | -8.41 | 7 | 0.0 | -6.78 | -0.73 | -13.10 | 13 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 91.39 | -8.61 | 0 | — | 1.48 | 0.39 | -14.37 | 1 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.54 | -2.38 | -16.91 | 1 |
| 32 | Agent | meta | 91.07 | -8.93 | 87 | 40.2 | -10.42 | -4.24 | -16.93 | 266 |
| 33 | Volume breakout · 1h | breakout | 90.93 | -9.07 | 84 | 22.6 | -12.21 | -2.19 | -15.57 | 108 |
| 34 | Bollinger breakout · 1h | breakout | 90.85 | -9.15 | 87 | 29.9 | -10.94 | -1.99 | -16.24 | 260 |
| 35 | Connors RSI(2) · 1h | reversion | 89.54 | -10.46 | 151 | 41.7 | -22.71 | -6.74 | -24.22 | 201 |
| 36 | RSI momentum · 1h | momentum | 89.33 | -10.66 | 83 | 15.7 | -20.41 | -4.01 | -26.37 | 216 |
| 37 | Opening range 15m | breakout | 88.95 | -11.05 | 256 | 25.8 | -17.34 | -4.54 | -20.98 | 700 |
| 38 | EMA 20/50 cross · 1h | trend | 88.79 | -11.21 | 62 | 12.9 | -19.07 | -3.52 | -21.33 | 131 |
| 39 | Supertrend · 1h | trend | 88.57 | -11.43 | 88 | 12.5 | -21.10 | -4.10 | -26.62 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 88.52 | -11.48 | 164 | 47.0 | -13.73 | -2.26 | -22.24 | 362 |
| 41 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -2.92 | -0.78 | -11.07 | 138 |
| 42 | Keltner breakout · 1h | breakout | 87.52 | -12.48 | 60 | 21.7 | -16.30 | -2.66 | -26.29 | 207 |
| 43 | Ichimoku · 1h | trend | 87.04 | -12.96 | 60 | 13.3 | -18.91 | -3.57 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.67 | -13.33 | 193 | 20.2 | -27.81 | -5.30 | -33.08 | 471 |
| 45 | Triple EMA stack · 1h | trend | 85.32 | -14.68 | 91 | 14.3 | -30.77 | -5.72 | -34.89 | 230 |
| 46 | Z-score reversion · 1h | reversion | 85.07 | -14.93 | 95 | 30.5 | -14.36 | -2.36 | -21.32 | 197 |
| 47 | Donchian 20/10 · 1h | breakout | 84.66 | -15.34 | 81 | 17.3 | -13.52 | -1.79 | -28.41 | 219 |
| 48 | MFI reversion · 1h | reversion | 84.50 | -15.50 | 216 | 30.6 | -14.69 | -2.29 | -20.43 | 145 |
| 49 | Agent (ML meta-label) | meta | 84.11 | -15.89 | 706 | 19.3 | -4.78 | -0.74 | -15.38 | 373 |
| 50 | OBV trend · 1h | momentum | 83.99 | -16.01 | 186 | 17.2 | -29.76 | -5.17 | -37.05 | 321 |
| 51 | MACD zero-line · 1h | trend | 83.83 | -16.17 | 89 | 14.6 | -25.89 | -5.16 | -26.79 | 224 |
| 52 | Three white soldiers | momentum | 82.67 | -17.33 | 249 | 19.7 | -46.42 | -17.56 | -47.79 | 614 |
| 53 | Bollinger reversion · 1h | reversion | 82.26 | -17.75 | 162 | 35.8 | -29.21 | -5.67 | -32.82 | 348 |
| 54 | Williams %R · 1h | reversion | 81.86 | -18.14 | 194 | 43.8 | -32.13 | -5.05 | -36.49 | 526 |
| 55 | ROC + volume · 1h | momentum | 81.85 | -18.15 | 199 | 21.6 | -26.57 | -4.61 | -34.62 | 398 |
| 56 | CCI reversion · 1h | reversion | 81.06 | -18.94 | 177 | 41.8 | -17.95 | -2.22 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.81 | -19.19 | 229 | 21.0 | -41.82 | -8.62 | -46.62 | 680 |
| 58 | RSI(14) reversion · 1h | reversion | 80.08 | -19.92 | 83 | 22.9 | -14.69 | -2.67 | -23.28 | 168 |
| 59 | EMA 9/21 cross · 1h | trend | 79.77 | -20.23 | 143 | 10.5 | -29.37 | -6.11 | -30.07 | 325 |
| 60 | VWAP momentum · 1h | momentum | 78.15 | -21.85 | 449 | 20.5 | -42.11 | -6.78 | -50.53 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 77.59 | -22.41 | 222 | 28.8 | -36.65 | -6.56 | -38.89 | 536 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.63 | -1.59 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 62.07 | -37.92 | 622 | 23.2 | -77.05 | -19.87 | -78.69 | 1723 |
| 64 | Volume breakout | breakout | 61.70 | -38.30 | 376 | 14.1 | -63.34 | -18.78 | -64.46 | 874 |
| 65 | Squeeze breakout | breakout | 58.84 | -41.16 | 486 | 14.2 | -65.74 | -21.65 | -66.58 | 1205 |
| 66 | Donchian 55/20 | breakout | 58.55 | -41.45 | 491 | 18.3 | -70.17 | -17.25 | -73.50 | 1278 |
| 67 | RSI(14) reversion | reversion | 57.41 | -42.59 | 740 | 26.4 | -74.61 | -16.51 | -75.08 | 1620 |
| 68 | EMA 20/50 cross | trend | 56.14 | -43.86 | 535 | 19.1 | -76.91 | -15.91 | -80.87 | 1445 |
| 69 | VWAP reversion | reversion | 53.69 | -46.31 | 752 | 25.3 | -71.57 | -14.58 | -72.28 | 1501 |
| 70 | Keltner breakout | breakout | 50.65 | -49.35 | 701 | 16.8 | -82.59 | -25.21 | -83.82 | 1806 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -29.96 | -98.78 | 5325 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.70 | -32.79 | -93.85 | 2599 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.69 | -20.67 | -88.38 | 1901 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.38 | -25.03 | -91.32 | 2357 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.06 | -25.60 | -91.30 | 2252 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.55 | -33.05 | -97.64 | 3521 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -38.18 | -96.82 | 3596 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -27.86 | -94.47 | 2534 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.62 | -27.07 | -82.64 | 1707 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.70 | -99.38 | 5747 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.36 | -25.74 | -92.18 | 2620 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.93 | -31.39 | -95.93 | 3446 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -40.71 | -99.75 | 6207 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.52 | -28.82 | -91.63 | 2351 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -38.62 | -97.67 | 3614 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.17 | -98.49 | 4700 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.84 | -32.48 | -94.15 | 2800 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -38.40 | -99.52 | 6165 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.53 | -21.85 | -87.01 | 2142 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.69 | -25.85 | -88.12 | 2134 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.32 | -95.98 | 3761 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.96 | -32.09 | -89.30 | 2114 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.66 | -32.85 | -95.83 | 4098 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -42.94 | -99.90 | 8282 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-20T17:40 | Keltner breakout | buy | MSFT | 12.68 | — | entry signal |
| 2026-10-20T17:35 | MFI reversion · 1h | buy | TECL | 8.77 | — | entry |
| 2026-10-20T17:30 | Williams %R · 1h | buy | SQQQ | 13.64 | — | entry |
| 2026-10-20T17:30 | Williams %R · 1h | sell | MSTR | 13.84 | 0.26 | exit signal |
| 2026-10-20T17:30 | Stochastic reversion · 1h | sell | MSFT | 14.91 | 0.11 | exit signal |
| 2026-10-20T17:30 | Connors RSI(2) · 1h | sell | MSFT | 22.46 | 0.10 | exit signal |
| 2026-10-20T17:30 | RSI(14) reversion · 1h | buy | META | 20.01 | — | entry signal |
| 2026-10-20T17:30 | Candlestick reversal · 1h | sell | SOXL | 5.45 | 0.00 | exit signal |
| 2026-10-20T17:30 | Candlestick reversal · 1h | sell | AMD | 5.52 | -0.02 | exit signal |
| 2026-10-20T17:30 | VWAP momentum · 1h | buy | SPY | 3.40 | — | entry signal |
| 2026-10-20T17:30 | VWAP momentum · 1h | buy | QQQ | 3.55 | — | entry signal |
| 2026-10-20T17:30 | VWAP momentum · 1h | buy | NVDA | 3.55 | — | entry signal |
| 2026-10-20T17:30 | VWAP momentum · 1h | buy | ETHU | 3.55 | — | entry signal |
| 2026-10-20T17:30 | VWAP momentum · 1h | buy | COIN | 3.55 | — | entry signal |
| 2026-10-20T17:30 | VWAP momentum · 1h | buy | BITX | 3.55 | — | entry signal |
| 2026-10-20T17:30 | VWAP momentum · 1h | buy | AMZN | 3.55 | — | entry signal |
| 2026-10-20T17:30 | VWAP momentum · 1h | sell | SOXL | 3.49 | -0.08 | exit signal |
| 2026-10-20T17:30 | VWAP momentum · 1h | sell | AMD | 3.53 | -0.04 | exit signal |
| 2026-10-20T17:30 | MACD cross · 1h | buy | MSTR | 1.35 | — | entry |
| 2026-10-20T17:30 | MACD cross · 1h | buy | ETH-USD | 5.09 | — | entry |
| 2026-10-20T17:30 | MACD cross · 1h | sell | GOOGL | 5.66 | -0.10 | exit signal |
| 2026-10-20T17:30 | ROC + volume | buy | BITX | 12.37 | — | entry |
| 2026-10-20T17:25 | RSI(14) reversion | sell | AAPL | 14.29 | 0.02 | exit signal |
| 2026-10-20T17:25 | Squeeze breakout | buy | MSFT | 14.70 | — | entry signal |
| 2026-10-20T17:25 | ROC + volume | sell | BITX | 12.37 | -0.04 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 17:55:05.000149+00:00 -> 2026-10-20 18:05:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
