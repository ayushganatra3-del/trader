# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T18:20:05.000146+00:00 · 30965 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.37%)

Closed trades 91, win rate 40.7%, fees £3.01, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 18.11 | -0.02 |

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

Today: 30117 decisions in 2658 calls, $0.3741 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T18:20 | 4 / 14 / 12 | cash |  |
| Breezy | 2026-10-21T18:20 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-10-21T18:20 | 4 / 20 / 6 | MSTR 74% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.15 | 6.15 | 0 | — | 8.73 | 4.09 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.44 | 4.44 | 14 | 50.0 | 6.88 | 2.26 | -3.69 | 22 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 5 | Max aggression: 5-day momentum | meta | 103.51 | 3.51 | 10 | 50.0 | -5.45 | -0.17 | -34.64 | 26 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.96 | 0.96 | 4 | 50.0 | 10.67 | 2.17 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold BTC | benchmark | 99.96 | -0.04 | 0 | — | 16.18 | 2.30 | -8.68 | 1 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.77 | -0.23 | 0 | — | 1.13 | 0.54 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.51 | -0.49 | 0 | — | 1.34 | 0.81 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.14 | -0.86 | 63 | 34.9 | 2.58 | 1.51 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.64 | -2.36 | 0 | — | 1.16 | 0.54 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.13 | -2.87 | 0 | — | -3.90 | -1.48 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.91 | -1.64 | -5.83 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.80 | -3.20 | 41 | 17.1 | -13.71 | -2.76 | -16.00 | 103 |
| 19 | Copy: Insider buying | copy | 96.48 | -3.52 | 25 | 40.0 | -11.52 | -1.97 | -20.62 | 72 |
| 20 | ADX DI cross · 1h | trend | 96.23 | -3.77 | 91 | 19.8 | -12.38 | -2.19 | -16.86 | 260 |
| 21 | Agent (rotation) | meta | 96.21 | -3.79 | 116 | 31.0 | -5.40 | -3.00 | -7.24 | 264 |
| 22 | Daily: Momentum burst | daily | 95.75 | -4.25 | 6 | 16.7 | -8.43 | -1.21 | -20.58 | 38 |
| 23 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 24 | Trend pullback · 1h | trend | 95.06 | -4.94 | 92 | 23.9 | -20.23 | -6.19 | -20.44 | 131 |
| 25 | Gap and go | momentum | 94.61 | -5.39 | 87 | 19.5 | 6.14 | 1.89 | -7.13 | 207 |
| 26 | Parabolic SAR · 1h | trend | 94.06 | -5.94 | 108 | 23.1 | -15.55 | -3.35 | -19.79 | 272 |
| 27 | Opening range 30m | breakout | 94.04 | -5.96 | 225 | 32.4 | -10.41 | -2.88 | -17.26 | 571 |
| 28 | Squeeze breakout · 1h | breakout | 93.79 | -6.21 | 46 | 21.7 | -0.56 | -0.03 | -11.48 | 99 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 93.27 | -6.73 | 0 | — | 3.33 | 0.67 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 93.10 | -6.90 | 87 | 29.9 | -6.52 | -1.09 | -15.59 | 261 |
| 31 | Daily: Bullish score | daily | 92.08 | -7.92 | 8 | 0.0 | -2.49 | -0.16 | -13.10 | 13 |
| 32 | Volume breakout · 1h | breakout | 91.54 | -8.46 | 89 | 23.6 | -12.03 | -2.12 | -14.06 | 113 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.68 | -1.80 | -16.91 | 1 |
| 34 | Supertrend · 1h | trend | 90.74 | -9.26 | 88 | 12.5 | -21.09 | -4.00 | -27.01 | 227 |
| 35 | Agent | meta | 90.63 | -9.37 | 91 | 40.7 | -15.70 | -7.33 | -17.72 | 259 |
| 36 | RSI momentum · 1h | momentum | 90.39 | -9.61 | 84 | 16.7 | -21.16 | -4.15 | -23.49 | 224 |
| 37 | Connors RSI(2) · 1h | reversion | 89.74 | -10.26 | 158 | 42.4 | -21.77 | -6.45 | -23.42 | 197 |
| 38 | Stochastic reversion · 1h | reversion | 89.51 | -10.49 | 169 | 47.3 | -13.65 | -2.23 | -22.24 | 362 |
| 39 | EMA 20/50 cross · 1h | trend | 89.38 | -10.62 | 62 | 12.9 | -20.58 | -3.61 | -23.73 | 136 |
| 40 | Opening range 15m | breakout | 88.72 | -11.28 | 274 | 28.8 | -15.92 | -4.24 | -19.69 | 709 |
| 41 | Keltner breakout · 1h | breakout | 88.69 | -11.31 | 61 | 23.0 | -20.44 | -3.87 | -27.27 | 206 |
| 42 | MACD cross · 1h | trend | 88.04 | -11.96 | 199 | 21.1 | -23.22 | -4.33 | -26.95 | 467 |
| 43 | Ichimoku · 1h | trend | 87.69 | -12.31 | 60 | 13.3 | -17.02 | -3.15 | -20.25 | 117 |
| 44 | Agent (aggressive) | meta | 87.53 | -12.47 | 45 | 35.6 | -11.55 | -3.35 | -13.58 | 125 |
| 45 | Z-score reversion · 1h | reversion | 86.90 | -13.10 | 102 | 34.3 | -11.35 | -1.75 | -21.32 | 196 |
| 46 | Donchian 20/10 · 1h | breakout | 86.63 | -13.37 | 83 | 19.3 | -20.39 | -3.71 | -29.99 | 230 |
| 47 | Triple EMA stack · 1h | trend | 86.15 | -13.85 | 92 | 15.2 | -29.38 | -5.42 | -30.29 | 223 |
| 48 | MFI reversion · 1h | reversion | 85.20 | -14.80 | 228 | 32.9 | -14.47 | -2.19 | -21.11 | 140 |
| 49 | Agent (ML meta-label) | meta | 85.11 | -14.89 | 729 | 20.2 | -10.06 | -1.73 | -15.45 | 362 |
| 50 | MACD zero-line · 1h | trend | 84.93 | -15.07 | 92 | 15.2 | -22.90 | -4.40 | -26.06 | 225 |
| 51 | OBV trend · 1h | momentum | 84.61 | -15.39 | 188 | 17.6 | -31.01 | -5.83 | -32.35 | 314 |
| 52 | ROC + volume · 1h | momentum | 83.64 | -16.36 | 212 | 23.6 | -26.50 | -4.72 | -33.30 | 392 |
| 53 | Three white soldiers | momentum | 82.63 | -17.38 | 257 | 20.6 | -46.02 | -17.82 | -46.93 | 607 |
| 54 | Bollinger reversion · 1h | reversion | 82.60 | -17.40 | 163 | 36.2 | -29.08 | -5.61 | -32.84 | 348 |
| 55 | Williams %R · 1h | reversion | 82.43 | -17.57 | 199 | 44.7 | -31.58 | -4.91 | -36.57 | 517 |
| 56 | CCI reversion · 1h | reversion | 82.12 | -17.88 | 188 | 43.6 | -20.27 | -2.63 | -27.44 | 436 |
| 57 | Heikin-Ashi · 1h | trend | 82.01 | -17.99 | 236 | 21.2 | -42.99 | -9.12 | -46.27 | 680 |
| 58 | EMA 9/21 cross · 1h | trend | 81.48 | -18.52 | 143 | 10.5 | -26.91 | -5.08 | -30.32 | 333 |
| 59 | RSI(14) reversion · 1h | reversion | 81.16 | -18.84 | 85 | 24.7 | -14.80 | -2.70 | -23.28 | 166 |
| 60 | VWAP momentum · 1h | momentum | 79.62 | -20.38 | 475 | 21.3 | -44.94 | -8.15 | -51.86 | 1255 |
| 61 | Candlestick reversal · 1h | reversion | 78.74 | -21.26 | 230 | 30.0 | -36.57 | -6.50 | -39.76 | 537 |
| 62 | Max aggression: 1-day momentum | meta | 77.87 | -22.13 | 17 | 29.4 | -33.56 | -2.08 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 60.10 | -39.90 | 675 | 23.4 | -77.56 | -21.53 | -78.99 | 1718 |
| 64 | Volume breakout | breakout | 59.22 | -40.78 | 399 | 13.5 | -64.97 | -20.29 | -65.27 | 873 |
| 65 | RSI(14) reversion | reversion | 57.07 | -42.93 | 750 | 26.7 | -74.06 | -16.15 | -74.89 | 1602 |
| 66 | Donchian 55/20 | breakout | 57.03 | -42.97 | 522 | 18.8 | -71.73 | -18.93 | -74.04 | 1288 |
| 67 | Squeeze breakout | breakout | 56.64 | -43.36 | 517 | 13.9 | -66.83 | -22.88 | -67.80 | 1217 |
| 68 | EMA 20/50 cross | trend | 55.79 | -44.21 | 563 | 19.5 | -78.55 | -18.71 | -80.89 | 1438 |
| 69 | VWAP reversion | reversion | 53.97 | -46.03 | 761 | 25.6 | -71.02 | -14.26 | -72.15 | 1465 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.75 | -30.94 | -98.80 | 5292 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.84 | -33.08 | -94.26 | 2612 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.48 | -22.22 | -88.67 | 1901 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.86 | -26.54 | -91.71 | 2372 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.48 | -26.33 | -91.52 | 2287 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.61 | -33.69 | -97.77 | 3509 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.88 | -37.79 | -96.98 | 3596 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.55 | -28.03 | -94.73 | 2554 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.89 | -27.87 | -83.44 | 1741 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.55 | -99.37 | 5701 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.83 | -27.61 | -92.66 | 2635 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.90 | -31.47 | -95.94 | 3455 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.43 | -99.76 | 6178 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.64 | -29.43 | -91.89 | 2345 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -39.42 | -97.80 | 3637 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.27 | -98.48 | 4690 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.20 | -35.24 | -94.43 | 2813 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.36 | -27.89 | -84.44 | 1814 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.23 | -99.54 | 6152 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.83 | -22.42 | -87.01 | 2134 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.78 | -26.16 | -88.05 | 2134 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -32.53 | -95.91 | 3743 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -33.28 | -89.42 | 2106 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -33.29 | -95.75 | 4065 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.01 | -99.91 | 8293 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T18:15 | Squeeze breakout | sell | NVDA | 13.61 | -0.01 | exit signal |
| 2026-10-21T18:10 | ROC + volume | sell | LABU | 14.94 | -0.07 | exit signal |
| 2026-10-21T18:06 | MFI reversion · 1h | buy | GOOGL | 21.29 | — | entry |
| 2026-10-21T18:06 | Volume breakout | buy | XRP-USD | 14.81 | — | entry signal |
| 2026-10-21T18:06 | Volume breakout | sell | AMZN | 14.77 | -0.04 | exit signal |
| 2026-10-21T18:06 | Squeeze breakout | buy | XRP-USD | 14.15 | — | entry signal |
| 2026-10-21T18:06 | ROC + volume | buy | XRP-USD | 15.03 | — | entry signal |
| 2026-10-21T18:00 | Agent (rotation) | sell | TQQQ | 31.98 | -0.12 | selected signal exited |
| 2026-10-21T18:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 104.44 | -0.39 | target is flat |
| 2026-10-21T18:00 | ROC + volume | buy | UPRO | 15.04 | — | entry |
| 2026-10-21T17:55 | ROC + volume | sell | UPRO | 15.06 | 0.04 | target is flat |
| 2026-10-21T17:50 | Volume breakout | buy | AMZN | 14.81 | — | entry signal |
| 2026-10-21T17:50 | Squeeze breakout | buy | GOOGL | 5.10 | — | rebalance up |
| 2026-10-21T17:50 | Squeeze breakout | buy | AMD | 2.84 | — | rebalance up |
| 2026-10-21T17:50 | Squeeze breakout | sell | TQQQ | 11.29 | 0.22 | exit signal |
| 2026-10-21T17:50 | Squeeze breakout | sell | QQQ | 11.32 | 0.07 | exit signal |
| 2026-10-21T17:45 | VWAP reversion | sell | LABU | 13.59 | 0.12 | exit signal |
| 2026-10-21T17:40 | ROC + volume | buy | UPRO | 8.33 | — | rebalance up |
| 2026-10-21T17:40 | ROC + volume | buy | LABU | 6.41 | — | rebalance up |
| 2026-10-21T17:40 | ROC + volume | sell | TQQQ | 6.67 | -0.04 | exit signal |
| 2026-10-21T17:40 | ROC + volume | sell | QQQ | 6.71 | -0.00 | exit signal |
| 2026-10-21T17:40 | ROC + volume | sell | PLTR | 6.71 | 0.05 | exit signal |
| 2026-10-21T17:40 | ROC + volume | sell | COIN | 6.69 | -0.04 | exit signal |
| 2026-10-21T17:40 | ROC + volume | sell | AMD | 6.71 | 0.03 | exit signal |
| 2026-10-21T17:35 | Agent (ML meta-label) | buy | QQQ | 4.57 | — | rebalance up |
| 2026-10-21T17:35 | Agent (ML meta-label) | sell | ETHU | 9.46 | 0.01 | selected signal exited |
| 2026-10-21T17:35 | Volume breakout | sell | UPRO | 14.85 | -0.03 | exit signal |
| 2026-10-21T17:35 | ROC + volume | buy | LABU | 8.59 | — | entry |
| 2026-10-21T17:35 | ROC + volume | sell | TECL | 7.49 | -0.04 | target is flat |
| 2026-10-21T17:30 | Agent (ML meta-label) | buy | ETHU | 9.45 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T17:30 | Agent (ML meta-label) | sell | SQQQ | 7.39 | -0.24 | selected signal exited |
| 2026-10-21T17:30 | Agent (ML meta-label) | sell | NVDA | 7.78 | 0.12 | selected signal exited |
| 2026-10-21T17:30 | Williams %R · 1h | buy | GOOGL | 20.60 | — | entry signal |
| 2026-10-21T17:30 | Z-score reversion · 1h | buy | GOOGL | 21.72 | — | entry signal |
| 2026-10-21T17:30 | Z-score reversion · 1h | sell | NVDA | 21.72 | 0.27 | exit signal |
| 2026-10-21T17:30 | RSI(14) reversion · 1h | buy | GOOGL | 20.29 | — | entry signal |
| 2026-10-21T17:30 | RSI(14) reversion · 1h | sell | AMD | 20.48 | 0.53 | exit signal |
| 2026-10-21T17:30 | Candlestick reversal · 1h | buy | SQQQ | 6.66 | — | rebalance up |
| 2026-10-21T17:30 | Candlestick reversal · 1h | buy | QQQ | 6.67 | — | rebalance up |
| 2026-10-21T17:30 | Candlestick reversal · 1h | buy | PLTR | 6.50 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 18:20:05.000146+00:00 -> 2026-10-21 18:30:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
