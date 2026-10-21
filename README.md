# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T16:20:05.000156+00:00 · 30857 ticks

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

Today: 20493 decisions in 2334 calls, $0.2619 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T16:20 | 10 / 8 / 11 | cash |  |
| Breezy | 2026-10-21T16:20 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-21T16:20 | 8 / 19 / 2 | MSTR 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.48 | 6.48 | 0 | — | 8.76 | 4.07 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.07 | 5.07 | 12 | 58.3 | 7.42 | 2.44 | -3.27 | 21 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 102.46 | 2.46 | 10 | 50.0 | -6.49 | -0.27 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.45 | 0.45 | 4 | 50.0 | 9.01 | 1.89 | -7.93 | 8 |
| 8 | Hold BTC | benchmark | 100.03 | 0.03 | 0 | — | 16.01 | 2.28 | -8.68 | 1 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.52 | -0.48 | 0 | — | 0.55 | 0.31 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.38 | -0.62 | 0 | — | 0.94 | 0.58 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.02 | -0.98 | 63 | 34.9 | 2.42 | 1.42 | -2.29 | 64 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.40 | -2.60 | 0 | — | 0.99 | 0.47 | -5.31 | 1 |
| 16 | Copy: Insider buying | copy | 97.36 | -2.65 | 25 | 40.0 | -10.81 | -1.82 | -20.62 | 72 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.20 | -1.82 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.89 | -3.11 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 96.54 | -3.46 | 40 | 15.0 | -14.05 | -2.80 | -16.01 | 103 |
| 20 | Agent (rotation) | meta | 96.32 | -3.67 | 114 | 31.6 | -6.43 | -3.28 | -8.30 | 296 |
| 21 | ADX DI cross · 1h | trend | 95.91 | -4.09 | 90 | 18.9 | -10.42 | -1.74 | -17.51 | 257 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 95.35 | -4.65 | 6 | 16.7 | -8.86 | -1.29 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 95.05 | -4.95 | 91 | 24.2 | -20.40 | -6.21 | -20.51 | 132 |
| 25 | Gap and go | momentum | 94.62 | -5.38 | 84 | 16.7 | 6.10 | 1.88 | -7.13 | 207 |
| 26 | Parabolic SAR · 1h | trend | 93.79 | -6.21 | 108 | 23.1 | -15.45 | -3.29 | -19.76 | 274 |
| 27 | Squeeze breakout · 1h | breakout | 93.78 | -6.22 | 46 | 21.7 | -1.19 | -0.19 | -11.48 | 100 |
| 28 | Opening range 30m | breakout | 93.70 | -6.30 | 225 | 32.4 | -10.73 | -3.01 | -17.26 | 568 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 93.24 | -6.76 | 0 | — | 3.38 | 0.68 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.76 | -7.24 | 87 | 29.9 | -7.08 | -1.22 | -15.79 | 258 |
| 31 | Daily: Bullish score | daily | 91.87 | -8.13 | 8 | 0.0 | -3.40 | -0.29 | -13.10 | 13 |
| 32 | Volume breakout · 1h | breakout | 91.33 | -8.67 | 89 | 23.6 | -12.13 | -2.14 | -14.02 | 109 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.50 | -1.98 | -16.91 | 1 |
| 34 | Agent | meta | 90.63 | -9.37 | 91 | 40.7 | -9.69 | -5.72 | -9.94 | 230 |
| 35 | Supertrend · 1h | trend | 90.46 | -9.54 | 88 | 12.5 | -20.31 | -3.87 | -26.58 | 226 |
| 36 | RSI momentum · 1h | momentum | 90.11 | -9.89 | 84 | 16.7 | -20.22 | -3.99 | -22.04 | 217 |
| 37 | Connors RSI(2) · 1h | reversion | 89.90 | -10.10 | 158 | 42.4 | -21.64 | -6.40 | -23.42 | 197 |
| 38 | Stochastic reversion · 1h | reversion | 89.43 | -10.57 | 168 | 47.6 | -12.84 | -2.06 | -22.24 | 363 |
| 39 | EMA 20/50 cross · 1h | trend | 89.25 | -10.75 | 62 | 12.9 | -20.86 | -3.80 | -23.82 | 138 |
| 40 | Opening range 15m | breakout | 88.51 | -11.49 | 273 | 28.9 | -16.20 | -4.34 | -19.69 | 705 |
| 41 | Keltner breakout · 1h | breakout | 88.41 | -11.59 | 61 | 23.0 | -21.51 | -4.17 | -27.08 | 206 |
| 42 | MACD cross · 1h | trend | 87.74 | -12.26 | 199 | 21.1 | -25.40 | -4.78 | -28.86 | 473 |
| 43 | Agent (aggressive) | meta | 87.53 | -12.47 | 45 | 35.6 | -10.65 | -3.25 | -10.83 | 115 |
| 44 | Ichimoku · 1h | trend | 87.25 | -12.75 | 60 | 13.3 | -18.21 | -3.41 | -20.25 | 117 |
| 45 | Z-score reversion · 1h | reversion | 86.61 | -13.38 | 101 | 33.7 | -11.68 | -1.82 | -21.32 | 195 |
| 46 | Donchian 20/10 · 1h | breakout | 86.36 | -13.64 | 83 | 19.3 | -20.46 | -3.78 | -29.78 | 225 |
| 47 | Triple EMA stack · 1h | trend | 86.06 | -13.94 | 91 | 14.3 | -29.52 | -5.44 | -31.00 | 224 |
| 48 | MFI reversion · 1h | reversion | 85.14 | -14.86 | 227 | 32.6 | -14.49 | -2.20 | -21.11 | 139 |
| 49 | Agent (ML meta-label) | meta | 84.98 | -15.02 | 720 | 19.7 | -4.37 | -0.60 | -16.20 | 363 |
| 50 | MACD zero-line · 1h | trend | 84.68 | -15.32 | 92 | 15.2 | -24.93 | -4.75 | -27.44 | 223 |
| 51 | OBV trend · 1h | momentum | 84.45 | -15.55 | 188 | 17.6 | -30.48 | -5.72 | -31.73 | 314 |
| 52 | ROC + volume · 1h | momentum | 83.33 | -16.67 | 211 | 23.7 | -26.32 | -4.72 | -33.07 | 387 |
| 53 | Three white soldiers | momentum | 82.64 | -17.36 | 256 | 20.7 | -46.08 | -17.88 | -46.93 | 609 |
| 54 | Williams %R · 1h | reversion | 82.60 | -17.40 | 198 | 44.4 | -30.33 | -4.63 | -36.50 | 518 |
| 55 | Bollinger reversion · 1h | reversion | 82.50 | -17.50 | 163 | 36.2 | -29.18 | -5.64 | -32.84 | 347 |
| 56 | CCI reversion · 1h | reversion | 82.16 | -17.84 | 185 | 43.2 | -20.02 | -2.58 | -27.44 | 436 |
| 57 | Heikin-Ashi · 1h | trend | 81.73 | -18.27 | 235 | 20.9 | -43.89 | -9.40 | -47.25 | 684 |
| 58 | EMA 9/21 cross · 1h | trend | 81.25 | -18.75 | 143 | 10.5 | -26.63 | -5.18 | -29.62 | 325 |
| 59 | RSI(14) reversion · 1h | reversion | 81.12 | -18.88 | 84 | 23.8 | -13.93 | -2.45 | -23.28 | 174 |
| 60 | VWAP momentum · 1h | momentum | 79.32 | -20.68 | 472 | 21.2 | -44.82 | -8.21 | -51.40 | 1255 |
| 61 | Candlestick reversal · 1h | reversion | 78.92 | -21.08 | 228 | 29.4 | -34.87 | -6.00 | -38.64 | 547 |
| 62 | Max aggression: 1-day momentum | meta | 77.06 | -22.94 | 17 | 29.4 | -34.31 | -2.15 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 60.31 | -39.69 | 659 | 22.9 | -77.76 | -21.79 | -79.03 | 1729 |
| 64 | Volume breakout | breakout | 59.55 | -40.45 | 394 | 13.7 | -64.76 | -20.25 | -65.02 | 864 |
| 65 | RSI(14) reversion | reversion | 57.15 | -42.85 | 749 | 26.6 | -74.06 | -16.16 | -74.89 | 1608 |
| 66 | Donchian 55/20 | breakout | 56.90 | -43.10 | 521 | 18.6 | -71.93 | -19.19 | -74.04 | 1293 |
| 67 | Squeeze breakout | breakout | 56.72 | -43.28 | 512 | 13.7 | -66.72 | -22.57 | -67.80 | 1214 |
| 68 | EMA 20/50 cross | trend | 55.63 | -44.38 | 563 | 19.5 | -78.05 | -17.41 | -80.89 | 1449 |
| 69 | VWAP reversion | reversion | 53.94 | -46.05 | 760 | 25.5 | -71.09 | -14.31 | -72.15 | 1470 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.78 | -31.24 | -98.80 | 5317 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.79 | -32.45 | -94.23 | 2612 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.49 | -21.99 | -88.67 | 1912 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.80 | -25.76 | -91.71 | 2375 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.49 | -26.37 | -91.63 | 2272 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.63 | -33.79 | -97.77 | 3521 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.88 | -37.74 | -96.97 | 3617 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -27.83 | -94.61 | 2545 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.69 | -27.48 | -83.35 | 1734 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.04 | -99.38 | 5724 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.85 | -27.67 | -92.66 | 2634 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.96 | -31.63 | -95.97 | 3452 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.75 | -99.76 | 6181 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.66 | -29.39 | -91.89 | 2354 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -39.74 | -97.79 | 3626 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.37 | -98.48 | 4702 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.19 | -35.36 | -94.43 | 2806 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.35 | -27.87 | -84.44 | 1812 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.32 | -99.53 | 6168 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.74 | -22.21 | -87.01 | 2141 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.53 | -25.43 | -88.05 | 2133 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -32.82 | -95.95 | 3759 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -33.28 | -89.41 | 2109 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.79 | -33.73 | -95.79 | 4094 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.42 | -99.91 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T16:20 | Agent (ML meta-label) | buy | ETHU | 2.42 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T16:15 | Volume breakout | sell | ETH-USD | 14.85 | -0.08 | exit signal |
| 2026-10-21T16:15 | ROC + volume | sell | AAPL | 5.48 | -0.02 | exit signal |
| 2026-10-21T16:10 | Agent (ML meta-label) | sell | ETHU | 2.42 | 0.01 | selected signal exited |
| 2026-10-21T16:10 | Three white soldiers | sell | AAPL | 20.71 | 0.11 | exit signal |
| 2026-10-21T16:10 | Volume breakout | sell | TECL | 14.88 | -0.03 | exit signal |
| 2026-10-21T16:10 | ROC + volume | sell | DOGE-USD | 5.46 | 0.00 | exit signal |
| 2026-10-21T16:05 | Three white soldiers | sell | COIN | 20.68 | 0.07 | exit signal |
| 2026-10-21T16:05 | ROC + volume | buy | AMD | 4.38 | — | entry signal |
| 2026-10-21T16:00 | Agent (rotation) | buy | TQQQ | 32.17 | — | entry |
| 2026-10-21T16:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 105.38 | — | entry |
| 2026-10-21T16:00 | Agent (ML meta-label) | buy | ETHU | 2.41 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T16:00 | Squeeze breakout · 1h | buy | ETH-USD | 22.65 | — | entry signal |
| 2026-10-21T16:00 | Three white soldiers | sell | SOXL | 20.58 | 0.05 | target is flat |
| 2026-10-21T16:00 | EMA 20/50 cross | buy | MSFT | 4.07 | — | entry signal |
| 2026-10-21T16:00 | EMA 20/50 cross | buy | AMZN | 5.06 | — | entry signal |
| 2026-10-21T15:55 | VWAP reversion | buy | SQQQ | 13.48 | — | entry signal |
| 2026-10-21T15:55 | RSI(14) reversion | buy | SQQQ | 14.28 | — | entry signal |
| 2026-10-21T15:55 | Three white soldiers | buy | SOXL | 20.53 | — | entry |
| 2026-10-21T15:55 | ROC + volume | buy | UPRO | 6.04 | — | entry signal |
| 2026-10-21T15:55 | ROC + volume | buy | QQQ | 6.04 | — | entry |
| 2026-10-21T15:55 | ROC + volume | sell | XRP-USD | 5.50 | -0.01 | exit signal |
| 2026-10-21T15:55 | ROC + volume | sell | BTC-USD | 5.48 | -0.03 | exit signal |
| 2026-10-21T15:55 | ROC + volume | sell | BITX | 5.49 | 0.07 | exit signal |
| 2026-10-21T15:52 | Agent (ML meta-label) | sell | ETHU | 2.41 | -0.01 | selected signal exited |
| 2026-10-21T15:45 | Squeeze breakout | buy | SOXL | 13.92 | — | entry signal |
| 2026-10-21T15:45 | Squeeze breakout | buy | AMD | 14.20 | — | entry signal |
| 2026-10-21T15:40 | Agent (ML meta-label) | buy | ETHU | 2.42 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T15:40 | Three white soldiers | buy | TQQQ | 20.71 | — | entry signal |
| 2026-10-21T15:40 | Volume breakout | buy | TECL | 14.92 | — | entry signal |
| 2026-10-21T15:40 | Opening range 15m | buy | TECL | 1.39 | — | entry |
| 2026-10-21T15:40 | Opening range 15m | buy | SPY | 6.33 | — | entry |
| 2026-10-21T15:40 | Opening range 15m | buy | MSFT | 6.33 | — | entry signal |
| 2026-10-21T15:40 | Opening range 15m | sell | QQQ | 4.66 | 0.01 | rebalance down |
| 2026-10-21T15:40 | Opening range 15m | sell | META | 4.66 | 0.02 | rebalance down |
| 2026-10-21T15:40 | Opening range 15m | sell | BITX | 4.72 | 0.09 | rebalance down |
| 2026-10-21T15:35 | Agent (ML meta-label) | buy | IWM | 4.84 | — | rebalance up |
| 2026-10-21T15:35 | Agent (ML meta-label) | sell | ETHU | 7.26 | 0.21 | selected signal exited |
| 2026-10-21T15:35 | Volume breakout | buy | QQQ | 14.91 | — | entry signal |
| 2026-10-21T15:35 | Opening range 30m | buy | UPRO | 8.50 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 16:20:05.000156+00:00 -> 2026-10-21 16:30:05.000156+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
