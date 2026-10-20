# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T15:25:05.000164+00:00 · 29657 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.05 (-8.95%)

Closed trades 87, win rate 40.2%, fees £2.92, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.62 | +0.34 |

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

Today: 19728 decisions in 2271 calls, $0.2528 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T15:25 | 2 / 18 / 10 | cash |  |
| Breezy | 2026-10-20T15:25 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-20T15:25 | 2 / 26 / 2 | MSTR 70% |  |

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
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.53 | 5.53 | 11 | 63.6 | 7.92 | 2.61 | -3.27 | 20 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 105.31 | 5.30 | 0 | — | 6.96 | 3.35 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -0.91 | -0.17 | -9.24 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 100.32 | 0.32 | 9 | 44.4 | -13.53 | -0.96 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.93 | -1.07 | 0 | — | -0.22 | -0.08 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.80 | -1.20 | 58 | 34.5 | 4.27 | 2.23 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.50 | -1.50 | 0 | — | -1.11 | -0.38 | -5.15 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.41 | -1.59 | 3 | 33.3 | 3.85 | 0.90 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 14 | Hold BTC | benchmark | 97.37 | -2.63 | 0 | — | 19.27 | 2.58 | -8.68 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.17 | -2.83 | 0 | — | 0.29 | 0.18 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.14 | -2.86 | 0 | — | -3.70 | -1.38 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.10 | -2.32 | -5.83 | 1 |
| 18 | Agent (rotation) | meta | 96.13 | -3.87 | 113 | 31.9 | -5.83 | -2.92 | -7.75 | 312 |
| 19 | Donchian 55/20 · 1h | breakout | 95.94 | -4.06 | 39 | 15.4 | -17.78 | -3.57 | -23.10 | 104 |
| 20 | Copy: Insider buying | copy | 95.66 | -4.34 | 23 | 43.5 | -11.20 | -1.90 | -20.62 | 72 |
| 21 | Trend pullback · 1h | trend | 95.49 | -4.51 | 89 | 23.6 | -20.46 | -6.11 | -20.77 | 135 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.47 | -5.53 | 89 | 18.0 | -13.18 | -2.36 | -16.42 | 266 |
| 24 | Daily: Momentum burst | daily | 94.29 | -5.71 | 6 | 16.7 | -5.71 | -0.72 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.30 | 1.38 | -6.51 | 198 |
| 26 | Opening range 30m | breakout | 92.37 | -7.63 | 208 | 29.3 | -13.08 | -3.77 | -17.26 | 565 |
| 27 | Squeeze breakout · 1h | breakout | 91.55 | -8.46 | 45 | 22.2 | -3.62 | -0.81 | -11.20 | 100 |
| 28 | Daily: Bullish score | daily | 91.29 | -8.71 | 7 | 0.0 | -7.30 | -0.80 | -13.10 | 13 |
| 29 | Parabolic SAR · 1h | trend | 91.26 | -8.74 | 105 | 21.9 | -17.48 | -3.73 | -23.03 | 274 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -13.00 | -2.48 | -16.91 | 1 |
| 31 | Agent | meta | 91.05 | -8.95 | 87 | 40.2 | -12.18 | -4.31 | -14.41 | 296 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.96 | -9.04 | 0 | — | 0.62 | 0.26 | -14.37 | 1 |
| 33 | Bollinger breakout · 1h | breakout | 90.63 | -9.37 | 86 | 30.2 | -12.56 | -2.34 | -16.89 | 260 |
| 34 | Volume breakout · 1h | breakout | 90.60 | -9.40 | 82 | 23.2 | -15.05 | -2.69 | -18.32 | 111 |
| 35 | Connors RSI(2) · 1h | reversion | 89.39 | -10.61 | 150 | 41.3 | -22.58 | -6.68 | -24.01 | 203 |
| 36 | RSI momentum · 1h | momentum | 89.00 | -11.00 | 82 | 15.9 | -23.33 | -4.46 | -28.30 | 219 |
| 37 | EMA 20/50 cross · 1h | trend | 88.66 | -11.35 | 62 | 12.9 | -20.40 | -3.72 | -22.54 | 130 |
| 38 | Opening range 15m | breakout | 88.50 | -11.51 | 256 | 25.8 | -17.62 | -4.68 | -20.98 | 700 |
| 39 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -8.84 | -2.15 | -12.24 | 139 |
| 40 | Stochastic reversion · 1h | reversion | 88.01 | -11.99 | 163 | 46.6 | -14.29 | -2.38 | -22.24 | 363 |
| 41 | Supertrend · 1h | trend | 87.96 | -12.04 | 88 | 12.5 | -21.66 | -4.33 | -26.49 | 222 |
| 42 | Keltner breakout · 1h | breakout | 87.38 | -12.62 | 59 | 22.0 | -18.34 | -3.32 | -25.20 | 207 |
| 43 | Ichimoku · 1h | trend | 86.97 | -13.03 | 59 | 13.6 | -19.21 | -3.63 | -19.67 | 119 |
| 44 | MACD cross · 1h | trend | 86.34 | -13.66 | 192 | 20.3 | -27.46 | -5.28 | -33.45 | 472 |
| 45 | Triple EMA stack · 1h | trend | 85.20 | -14.80 | 91 | 14.3 | -31.54 | -5.70 | -35.94 | 221 |
| 46 | Z-score reversion · 1h | reversion | 84.83 | -15.17 | 95 | 30.5 | -14.13 | -2.32 | -21.32 | 198 |
| 47 | MFI reversion · 1h | reversion | 84.40 | -15.60 | 211 | 31.3 | -14.58 | -2.24 | -20.43 | 145 |
| 48 | Donchian 20/10 · 1h | breakout | 84.14 | -15.86 | 81 | 17.3 | -12.64 | -1.59 | -27.86 | 220 |
| 49 | Agent (ML meta-label) | meta | 83.85 | -16.15 | 699 | 19.3 | -7.49 | -1.25 | -15.72 | 378 |
| 50 | OBV trend · 1h | momentum | 83.54 | -16.46 | 185 | 17.3 | -31.22 | -5.41 | -37.71 | 328 |
| 51 | MACD zero-line · 1h | trend | 83.52 | -16.48 | 88 | 14.8 | -25.68 | -5.15 | -25.95 | 221 |
| 52 | Three white soldiers | momentum | 82.79 | -17.21 | 248 | 19.8 | -46.94 | -18.16 | -47.76 | 614 |
| 53 | Bollinger reversion · 1h | reversion | 82.30 | -17.70 | 162 | 35.8 | -28.13 | -5.39 | -33.53 | 352 |
| 54 | Williams %R · 1h | reversion | 81.57 | -18.43 | 193 | 43.5 | -33.05 | -5.22 | -36.50 | 529 |
| 55 | ROC + volume · 1h | momentum | 81.44 | -18.56 | 199 | 21.6 | -25.24 | -4.25 | -33.68 | 396 |
| 56 | CCI reversion · 1h | reversion | 80.89 | -19.11 | 175 | 41.1 | -16.93 | -2.08 | -27.44 | 444 |
| 57 | Heikin-Ashi · 1h | trend | 80.62 | -19.38 | 228 | 21.1 | -40.07 | -8.40 | -44.90 | 680 |
| 58 | RSI(14) reversion · 1h | reversion | 80.00 | -20.00 | 83 | 22.9 | -16.81 | -3.09 | -23.28 | 178 |
| 59 | EMA 9/21 cross · 1h | trend | 79.41 | -20.59 | 142 | 10.6 | -29.68 | -6.21 | -30.17 | 321 |
| 60 | VWAP momentum · 1h | momentum | 77.92 | -22.08 | 438 | 20.5 | -41.82 | -6.90 | -49.06 | 1263 |
| 61 | Candlestick reversal · 1h | reversion | 77.41 | -22.59 | 218 | 28.0 | -33.75 | -6.00 | -37.16 | 546 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.45 | -1.58 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 62.65 | -37.35 | 610 | 22.8 | -76.77 | -18.94 | -78.84 | 1735 |
| 64 | Volume breakout | breakout | 61.70 | -38.30 | 376 | 14.1 | -63.34 | -18.80 | -64.45 | 878 |
| 65 | Squeeze breakout | breakout | 59.01 | -40.99 | 484 | 14.0 | -64.34 | -20.00 | -66.58 | 1213 |
| 66 | Donchian 55/20 | breakout | 58.17 | -41.83 | 488 | 18.0 | -69.94 | -16.79 | -73.50 | 1285 |
| 67 | RSI(14) reversion | reversion | 57.35 | -42.65 | 737 | 26.2 | -74.63 | -16.54 | -75.14 | 1626 |
| 68 | EMA 20/50 cross | trend | 56.06 | -43.94 | 526 | 19.4 | -77.01 | -16.03 | -80.87 | 1438 |
| 69 | VWAP reversion | reversion | 53.69 | -46.31 | 752 | 25.3 | -71.57 | -14.58 | -72.28 | 1506 |
| 70 | Keltner breakout | breakout | 51.03 | -48.97 | 696 | 16.8 | -82.41 | -24.82 | -83.82 | 1810 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -29.98 | -98.76 | 5295 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -30.69 | -93.86 | 2571 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.81 | -20.86 | -88.38 | 1903 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.43 | -25.08 | -91.32 | 2356 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.94 | -25.39 | -91.20 | 2240 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.49 | -32.37 | -97.64 | 3508 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.64 | -35.34 | -96.83 | 3578 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.38 | -27.91 | -94.45 | 2518 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.64 | -26.73 | -82.72 | 1691 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.75 | -99.38 | 5754 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.24 | -25.39 | -92.18 | 2622 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.90 | -31.28 | -95.90 | 3442 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -39.19 | -99.76 | 6205 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.48 | -28.62 | -91.65 | 2350 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -37.92 | -97.71 | 3605 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.27 | -98.49 | 4716 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.84 | -32.66 | -94.15 | 2798 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.73 | -99.53 | 6176 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.80 | -22.29 | -87.09 | 2163 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.89 | -26.01 | -88.38 | 2152 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.34 | -95.99 | 3770 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.99 | -32.29 | -89.26 | 2121 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -33.12 | -95.83 | 4113 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -42.99 | -99.90 | 8248 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T15:25 | Agent (ML meta-label) | buy | GOOGL | 4.76 | — | entry |
| 2026-10-20T15:25 | Agent (ML meta-label) | sell | ETHU | 4.76 | -0.05 | rebalance down |
| 2026-10-20T15:25 | ROC + volume | buy | AMD | 3.81 | — | rebalance up |
| 2026-10-20T15:25 | ROC + volume | sell | QQQ | 5.69 | -0.00 | exit signal |
| 2026-10-20T15:20 | Agent (ML meta-label) | buy | TSLA | 3.44 | — | following Opening range 15m, Opening range 30m |
| 2026-10-20T15:20 | Agent (ML meta-label) | buy | QQQ | 7.64 | — | entry |
| 2026-10-20T15:20 | Agent (ML meta-label) | buy | LABU | 7.64 | — | entry |
| 2026-10-20T15:20 | Agent (ML meta-label) | buy | COIN | 7.64 | — | entry |
| 2026-10-20T15:20 | Agent (ML meta-label) | sell | UPRO | 4.39 | 0.01 | rebalance down |
| 2026-10-20T15:20 | Agent (ML meta-label) | sell | TNA | 4.34 | 0.06 | rebalance down |
| 2026-10-20T15:20 | Agent (ML meta-label) | sell | SQQQ | 4.48 | 0.00 | rebalance down |
| 2026-10-20T15:20 | Agent (ML meta-label) | sell | PLTR | 4.41 | -0.02 | rebalance down |
| 2026-10-20T15:20 | Agent (ML meta-label) | sell | NVDA | 4.37 | -0.01 | rebalance down |
| 2026-10-20T15:20 | Agent (ML meta-label) | sell | AMD | 4.36 | -0.04 | rebalance down |
| 2026-10-20T15:20 | MFI reversion · 1h | buy | UPRO | 4.86 | — | entry |
| 2026-10-20T15:20 | MFI reversion · 1h | sell | ETH-USD | 4.86 | 0.03 | rebalance down |
| 2026-10-20T15:20 | RSI(14) reversion | buy | AAPL | 14.27 | — | entry signal |
| 2026-10-20T15:20 | Keltner breakout | buy | TNA | 12.73 | — | entry signal |
| 2026-10-20T15:20 | Keltner breakout | buy | LABU | 12.78 | — | entry signal |
| 2026-10-20T15:20 | ROC + volume | sell | NVDA | 5.70 | 0.01 | exit signal |
| 2026-10-20T15:15 | Agent (ML meta-label) | buy | UPRO | 11.99 | — | entry |
| 2026-10-20T15:15 | Agent (ML meta-label) | sell | QQQ | 12.00 | -0.07 | selected signal exited |
| 2026-10-20T15:15 | MFI reversion · 1h | buy | TNA | 11.20 | — | entry |
| 2026-10-20T15:15 | MFI reversion · 1h | buy | SPY | 9.41 | — | rebalance up |
| 2026-10-20T15:15 | MFI reversion · 1h | sell | MSTR | 6.98 | -0.10 | rebalance down |
| 2026-10-20T15:15 | MFI reversion · 1h | sell | COIN | 6.61 | -0.04 | rebalance down |
| 2026-10-20T15:15 | MFI reversion · 1h | sell | AMD | 7.01 | -0.07 | rebalance down |
| 2026-10-20T15:15 | RSI(14) reversion · 1h | buy | AMD | 4.02 | — | rebalance up |
| 2026-10-20T15:15 | Volume breakout · 1h | buy | TSLA | 6.59 | — | rebalance up |
| 2026-10-20T15:15 | Volume breakout · 1h | buy | LABU | 6.72 | — | rebalance up |
| 2026-10-20T15:15 | Volume breakout · 1h | buy | ETH-USD | 6.82 | — | rebalance up |
| 2026-10-20T15:15 | Volume breakout · 1h | buy | BTC-USD | 6.78 | — | rebalance up |
| 2026-10-20T15:15 | Volume breakout · 1h | buy | AMZN | 6.67 | — | rebalance up |
| 2026-10-20T15:15 | Volume breakout · 1h | sell | XRP-USD | 11.17 | -0.30 | stop-loss |
| 2026-10-20T15:15 | Volume breakout · 1h | sell | SOL-USD | 11.20 | -0.29 | stop-loss |
| 2026-10-20T15:15 | Volume breakout · 1h | sell | DOGE-USD | 11.21 | -0.28 | stop-loss |
| 2026-10-20T15:15 | Squeeze breakout · 1h | buy | ETH-USD | 7.60 | — | rebalance up |
| 2026-10-20T15:15 | Squeeze breakout · 1h | buy | BTC-USD | 7.54 | — | rebalance up |
| 2026-10-20T15:15 | Squeeze breakout · 1h | buy | BITX | 7.67 | — | rebalance up |
| 2026-10-20T15:15 | Squeeze breakout · 1h | sell | XRP-USD | 15.19 | -0.41 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 15:25:05.000164+00:00 -> 2026-10-20 15:35:05.000164+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
