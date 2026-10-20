# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T16:25:05.000158+00:00 · 29707 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.87 (-9.13%)

Closed trades 87, win rate 40.2%, fees £2.92, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.44 | +0.16 |

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

Today: 24216 decisions in 2421 calls, $0.3052 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T16:25 | 8 / 16 / 6 | cash |  |
| Breezy | 2026-10-20T16:25 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-20T16:25 | 6 / 23 / 1 | MSTR 69% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.51 | 5.51 | 0 | — | 7.12 | 3.39 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -0.91 | -0.17 | -9.24 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 100.52 | 0.52 | 9 | 44.4 | -13.38 | -0.94 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.87 | -1.13 | 0 | — | -0.16 | -0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.85 | -1.15 | 59 | 35.6 | 2.36 | 1.35 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.59 | -1.41 | 0 | — | -0.57 | -0.16 | -5.15 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.08 | -1.92 | 3 | 33.3 | 3.11 | 0.76 | -7.93 | 8 |
| 14 | Hold BTC | benchmark | 97.29 | -2.71 | 0 | — | 20.70 | 2.73 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.16 | -2.85 | 0 | — | -3.70 | -1.38 | -7.04 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.21 | -2.38 | -5.83 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.93 | -3.06 | 0 | — | -0.00 | 0.06 | -5.31 | 1 |
| 18 | Agent (rotation) | meta | 96.12 | -3.88 | 114 | 31.6 | -7.49 | -3.43 | -9.06 | 331 |
| 19 | Donchian 55/20 · 1h | breakout | 95.93 | -4.07 | 40 | 15.0 | -17.24 | -3.44 | -21.99 | 103 |
| 20 | Trend pullback · 1h | trend | 95.60 | -4.40 | 90 | 23.3 | -20.39 | -6.09 | -20.78 | 135 |
| 21 | Copy: Insider buying | copy | 95.60 | -4.40 | 23 | 43.5 | -11.75 | -2.01 | -20.62 | 72 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.21 | -5.79 | 89 | 18.0 | -11.72 | -2.19 | -15.24 | 261 |
| 24 | Daily: Momentum burst | daily | 94.10 | -5.90 | 6 | 16.7 | -6.87 | -0.91 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.29 | 1.37 | -6.51 | 198 |
| 26 | Opening range 30m | breakout | 92.13 | -7.87 | 208 | 29.3 | -13.33 | -3.88 | -17.26 | 565 |
| 27 | Squeeze breakout · 1h | breakout | 91.42 | -8.58 | 46 | 21.7 | -3.60 | -0.80 | -11.34 | 97 |
| 28 | Daily: Bullish score | daily | 91.30 | -8.70 | 7 | 0.0 | -6.98 | -0.76 | -13.10 | 13 |
| 29 | Parabolic SAR · 1h | trend | 91.24 | -8.76 | 105 | 21.9 | -17.72 | -3.80 | -23.78 | 275 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -13.30 | -2.54 | -16.91 | 1 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 90.96 | -9.04 | 0 | — | 1.34 | 0.37 | -14.37 | 1 |
| 32 | Agent | meta | 90.87 | -9.13 | 87 | 40.2 | -7.07 | -3.79 | -13.25 | 274 |
| 33 | Volume breakout · 1h | breakout | 90.25 | -9.75 | 84 | 22.6 | -12.85 | -2.31 | -15.57 | 107 |
| 34 | Bollinger breakout · 1h | breakout | 90.11 | -9.89 | 87 | 29.9 | -11.28 | -2.06 | -15.98 | 259 |
| 35 | Connors RSI(2) · 1h | reversion | 89.41 | -10.59 | 150 | 41.3 | -22.78 | -6.77 | -24.22 | 202 |
| 36 | RSI momentum · 1h | momentum | 88.79 | -11.21 | 83 | 15.7 | -20.26 | -4.03 | -25.43 | 213 |
| 37 | EMA 20/50 cross · 1h | trend | 88.53 | -11.47 | 62 | 12.9 | -21.05 | -3.96 | -23.14 | 132 |
| 38 | Opening range 15m | breakout | 88.20 | -11.79 | 256 | 25.8 | -17.86 | -4.79 | -20.98 | 700 |
| 39 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -5.97 | -1.96 | -9.68 | 106 |
| 40 | Stochastic reversion · 1h | reversion | 87.94 | -12.06 | 163 | 46.6 | -14.23 | -2.36 | -22.24 | 362 |
| 41 | Supertrend · 1h | trend | 87.87 | -12.13 | 88 | 12.5 | -21.80 | -4.36 | -26.49 | 222 |
| 42 | Keltner breakout · 1h | breakout | 86.85 | -13.15 | 60 | 21.7 | -17.05 | -2.76 | -26.49 | 207 |
| 43 | Ichimoku · 1h | trend | 86.49 | -13.51 | 60 | 13.3 | -19.39 | -3.64 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.13 | -13.87 | 192 | 20.3 | -26.97 | -5.17 | -33.11 | 471 |
| 45 | Triple EMA stack · 1h | trend | 85.08 | -14.92 | 91 | 14.3 | -31.63 | -5.83 | -35.20 | 232 |
| 46 | Z-score reversion · 1h | reversion | 84.71 | -15.29 | 95 | 30.5 | -14.73 | -2.44 | -21.32 | 197 |
| 47 | MFI reversion · 1h | reversion | 84.08 | -15.92 | 213 | 31.0 | -15.42 | -2.44 | -20.43 | 147 |
| 48 | Donchian 20/10 · 1h | breakout | 84.02 | -15.98 | 81 | 17.3 | -14.96 | -2.01 | -29.18 | 222 |
| 49 | Agent (ML meta-label) | meta | 83.62 | -16.38 | 703 | 19.3 | -6.60 | -1.10 | -15.60 | 386 |
| 50 | OBV trend · 1h | momentum | 83.54 | -16.46 | 186 | 17.2 | -30.89 | -5.40 | -37.47 | 320 |
| 51 | MACD zero-line · 1h | trend | 83.12 | -16.88 | 89 | 14.6 | -26.10 | -5.24 | -26.47 | 222 |
| 52 | Three white soldiers | momentum | 82.67 | -17.33 | 249 | 19.7 | -46.56 | -17.74 | -47.79 | 615 |
| 53 | Bollinger reversion · 1h | reversion | 82.30 | -17.70 | 162 | 35.8 | -28.13 | -5.39 | -33.53 | 352 |
| 54 | Williams %R · 1h | reversion | 81.42 | -18.58 | 193 | 43.5 | -32.31 | -5.09 | -36.49 | 526 |
| 55 | ROC + volume · 1h | momentum | 81.17 | -18.83 | 199 | 21.6 | -26.50 | -4.60 | -34.19 | 398 |
| 56 | CCI reversion · 1h | reversion | 80.79 | -19.20 | 177 | 41.8 | -17.05 | -2.09 | -27.44 | 445 |
| 57 | Heikin-Ashi · 1h | trend | 80.16 | -19.84 | 228 | 21.1 | -41.01 | -8.67 | -45.43 | 681 |
| 58 | RSI(14) reversion · 1h | reversion | 79.97 | -20.03 | 83 | 22.9 | -15.74 | -2.81 | -23.28 | 179 |
| 59 | EMA 9/21 cross · 1h | trend | 79.07 | -20.93 | 143 | 10.5 | -29.70 | -6.19 | -30.14 | 322 |
| 60 | VWAP momentum · 1h | momentum | 77.76 | -22.24 | 446 | 20.4 | -42.38 | -6.95 | -49.74 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 77.28 | -22.72 | 220 | 28.2 | -32.55 | -5.57 | -35.42 | 551 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.16 | -1.56 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 62.37 | -37.63 | 619 | 23.3 | -76.81 | -19.20 | -78.76 | 1722 |
| 64 | Volume breakout | breakout | 61.70 | -38.30 | 376 | 14.1 | -63.22 | -18.79 | -64.33 | 872 |
| 65 | Squeeze breakout | breakout | 58.95 | -41.05 | 485 | 14.2 | -65.30 | -21.12 | -66.58 | 1208 |
| 66 | Donchian 55/20 | breakout | 58.04 | -41.96 | 491 | 18.3 | -70.96 | -18.05 | -73.50 | 1284 |
| 67 | RSI(14) reversion | reversion | 57.29 | -42.71 | 738 | 26.2 | -74.72 | -16.59 | -75.19 | 1635 |
| 68 | EMA 20/50 cross | trend | 55.89 | -44.11 | 533 | 19.1 | -77.19 | -16.24 | -80.87 | 1440 |
| 69 | VWAP reversion | reversion | 53.69 | -46.31 | 752 | 25.3 | -71.67 | -14.65 | -72.28 | 1519 |
| 70 | Keltner breakout | breakout | 50.70 | -49.30 | 700 | 16.9 | -82.57 | -25.12 | -83.82 | 1810 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -29.97 | -98.77 | 5342 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.59 | -32.16 | -93.85 | 2584 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.84 | -20.92 | -88.38 | 1901 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.47 | -25.29 | -91.32 | 2351 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.91 | -25.47 | -91.11 | 2242 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.49 | -32.13 | -97.64 | 3519 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -36.14 | -96.83 | 3587 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.34 | -27.82 | -94.42 | 2515 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.72 | -26.92 | -82.72 | 1690 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.78 | -99.38 | 5757 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.39 | -26.01 | -92.18 | 2623 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -31.40 | -95.93 | 3451 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -39.64 | -99.76 | 6184 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.60 | -28.99 | -91.73 | 2348 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -38.95 | -97.70 | 3602 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.32 | -98.49 | 4706 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.84 | -32.70 | -94.15 | 2797 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.65 | -99.53 | 6188 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.19 | -87.02 | 2158 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.84 | -26.18 | -88.24 | 2154 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.17 | -95.99 | 3763 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.03 | -32.40 | -89.28 | 2130 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -33.08 | -95.83 | 4107 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.22 | -99.90 | 8260 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T16:25 | EMA 20/50 cross | buy | SQQQ | 5.08 | — | entry signal |
| 2026-10-20T16:25 | EMA 20/50 cross | sell | NVDA | 5.07 | -0.02 | exit signal |
| 2026-10-20T16:20 | Donchian 55/20 | buy | ETHU | 2.94 | — | rebalance up |
| 2026-10-20T16:20 | Donchian 55/20 | sell | TSLA | 3.89 | -0.01 | exit signal |
| 2026-10-20T16:15 | MFI reversion · 1h | buy | PLTR | 6.82 | — | entry |
| 2026-10-20T16:15 | Volume breakout · 1h | buy | LABU | 4.55 | — | rebalance up |
| 2026-10-20T16:15 | Three white soldiers | sell | TECL | 20.58 | -0.12 | target is flat |
| 2026-10-20T16:15 | Donchian 55/20 | sell | TNA | 3.93 | 0.08 | exit signal |
| 2026-10-20T16:15 | Donchian 55/20 | sell | IWM | 3.90 | 0.02 | exit signal |
| 2026-10-20T16:10 | Agent (ML meta-label) | buy | QQQ | 5.41 | — | entry |
| 2026-10-20T16:10 | Agent (ML meta-label) | buy | COIN | 1.99 | — | entry |
| 2026-10-20T16:10 | MFI reversion · 1h | buy | UPRO | 7.16 | — | rebalance up |
| 2026-10-20T16:10 | MFI reversion · 1h | sell | COIN | 13.98 | -0.18 | target is flat |
| 2026-10-20T16:10 | RSI(14) reversion | sell | GOOGL | 14.29 | -0.12 | stop-loss |
| 2026-10-20T16:10 | Keltner breakout | sell | LABU | 12.58 | -0.19 | exit signal |
| 2026-10-20T16:05 | Agent (ML meta-label) | sell | COIN | 7.00 | 0.01 | selected signal exited |
| 2026-10-20T16:05 | Keltner breakout | sell | TNA | 12.63 | -0.11 | exit signal |
| 2026-10-20T16:00 | OBV trend · 1h | buy | ETH-USD | 20.88 | — | entry signal |
| 2026-10-20T16:00 | VWAP momentum · 1h | sell | SOL-USD | 3.50 | -0.00 | exit signal |
| 2026-10-20T16:00 | Heikin-Ashi · 1h | buy | ETH-USD | 8.79 | — | entry signal |
| 2026-10-20T16:00 | Heikin-Ashi · 1h | buy | BTC-USD | 16.12 | — | entry signal |
| 2026-10-20T16:00 | Heikin-Ashi · 1h | sell | LABU | 5.51 | 0.49 | rebalance down |
| 2026-10-20T16:00 | Triple EMA stack · 1h | buy | ETH-USD | 21.21 | — | entry signal |
| 2026-10-20T16:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 22.16 | — | entry signal |
| 2026-10-20T16:00 | Three white soldiers | buy | TECL | 20.70 | — | entry signal |
| 2026-10-20T16:00 | ROC + volume | sell | LABU | 15.54 | 0.38 | exit signal |
| 2026-10-20T15:57 | Agent (ML meta-label) | buy | COIN | 6.99 | — | entry |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 16:25:05.000158+00:00 -> 2026-10-20 16:35:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
