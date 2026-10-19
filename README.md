# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T13:55:05.000131+00:00 · 28441 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.44 (-8.56%)

Closed trades 78, win rate 38.5%, fees £2.71, max drawdown -9.08%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 36.62 | +0.15 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, APLD 12%, FLSC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 11010 decisions in 2052 calls, $0.1516 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T13:55 | 2 / 11 / 17 | cash |  |
| Breezy | 2026-10-19T13:55 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-19T13:55 | 0 / 29 / 1 | COIN 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |
| VWAP reversion | BITX | 1.52 | +2.60% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 10.33 | 3.45 | -3.27 | 18 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.27 | 6.27 | 15 | 40.0 | 9.62 | 2.34 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.68 | 4.68 | 0 | — | 5.55 | 2.71 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 101.09 | 1.09 | 64 | 39.1 | -8.89 | -2.55 | -13.79 | 136 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.13 | 0.13 | 0 | — | 3.95 | 1.57 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 10 | Hold SPY | benchmark | 99.05 | -0.95 | 0 | — | -0.23 | -0.09 | -3.13 | 1 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.21 | -1.79 | 3 | 33.3 | 2.38 | 0.61 | -7.93 | 9 |
| 12 | Agent (rotation) | meta | 98.09 | -1.91 | 110 | 32.7 | -5.07 | -2.51 | -6.83 | 306 |
| 13 | Copy: Insider buying | copy | 97.82 | -2.18 | 20 | 45.0 | -14.12 | -2.54 | -20.62 | 73 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 97.82 | -2.18 | 54 | 31.5 | 2.36 | 1.31 | -2.17 | 61 |
| 15 | Hold BTC | benchmark | 97.48 | -2.52 | 0 | — | 26.53 | 3.16 | -8.68 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 97.46 | -2.54 | 36 | 16.7 | -10.01 | -1.61 | -20.74 | 107 |
| 17 | Copy: Congress Democrats (NANC) | copy | 97.10 | -2.90 | 0 | — | -0.85 | -0.29 | -5.31 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.20 | -2.38 | -5.83 | 1 |
| 19 | Trend pullback · 1h | trend | 96.26 | -3.74 | 87 | 24.1 | -19.80 | -5.85 | -20.64 | 134 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 95.98 | -4.02 | 0 | — | -7.17 | -2.85 | -7.55 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.23 | -4.77 | 8 | 37.5 | -20.13 | -1.69 | -34.64 | 26 |
| 23 | Daily: Momentum burst | daily | 94.05 | -5.95 | 6 | 16.7 | -4.50 | -0.52 | -20.58 | 40 |
| 24 | ADX DI cross · 1h | trend | 93.67 | -6.33 | 83 | 19.3 | -11.42 | -2.24 | -12.42 | 255 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 2.66 | 0.67 | -9.46 | 98 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.49 | 2.39 | -6.51 | 196 |
| 27 | Parabolic SAR · 1h | trend | 91.88 | -8.12 | 100 | 23.0 | -13.43 | -2.21 | -24.34 | 273 |
| 28 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.89 | -0.12 | -14.31 | 110 |
| 29 | Daily: Bullish score | daily | 91.51 | -8.49 | 7 | 0.0 | -3.92 | -0.31 | -13.10 | 12 |
| 30 | Agent | meta | 91.44 | -8.56 | 78 | 38.5 | -8.15 | -5.06 | -9.56 | 244 |
| 31 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -11.35 | -3.12 | -17.60 | 548 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -13.32 | -2.55 | -16.91 | 1 |
| 33 | EMA 20/50 cross · 1h | trend | 90.94 | -9.06 | 55 | 14.5 | -18.07 | -3.14 | -19.78 | 130 |
| 34 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | -2.80 | -0.29 | -15.29 | 263 |
| 35 | Agent (aggressive) | meta | 90.35 | -9.65 | 39 | 33.3 | -8.14 | -2.73 | -11.20 | 113 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 90.06 | -9.94 | 0 | — | 3.47 | 0.68 | -14.37 | 1 |
| 37 | RSI momentum · 1h | momentum | 89.73 | -10.27 | 77 | 16.9 | -16.00 | -2.80 | -26.34 | 216 |
| 38 | Ichimoku · 1h | trend | 89.18 | -10.82 | 52 | 15.4 | -17.46 | -3.30 | -17.53 | 114 |
| 39 | Connors RSI(2) · 1h | reversion | 88.74 | -11.26 | 147 | 40.1 | -23.84 | -7.23 | -24.79 | 206 |
| 40 | Triple EMA stack · 1h | trend | 88.08 | -11.92 | 82 | 15.9 | -19.57 | -2.63 | -31.91 | 234 |
| 41 | Stochastic reversion · 1h | reversion | 88.06 | -11.94 | 150 | 45.3 | -17.19 | -2.94 | -22.24 | 371 |
| 42 | Supertrend · 1h | trend | 87.75 | -12.25 | 85 | 11.8 | -23.20 | -4.80 | -26.63 | 213 |
| 43 | Keltner breakout · 1h | breakout | 87.49 | -12.51 | 56 | 23.2 | -11.13 | -1.45 | -28.50 | 202 |
| 44 | MACD cross · 1h | trend | 86.77 | -13.23 | 181 | 21.5 | -25.42 | -4.66 | -31.84 | 463 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -16.53 | -4.27 | -21.40 | 685 |
| 46 | OBV trend · 1h | momentum | 86.34 | -13.66 | 171 | 18.1 | -20.78 | -2.75 | -33.75 | 315 |
| 47 | Z-score reversion · 1h | reversion | 85.62 | -14.38 | 91 | 30.8 | -13.47 | -2.17 | -21.32 | 190 |
| 48 | Max aggression: 1-day momentum | meta | 84.94 | -15.06 | 15 | 33.3 | -13.33 | -0.43 | -37.31 | 42 |
| 49 | MFI reversion · 1h | reversion | 84.82 | -15.18 | 209 | 31.1 | -17.18 | -2.67 | -21.34 | 138 |
| 50 | MACD zero-line · 1h | trend | 84.63 | -15.37 | 82 | 15.9 | -24.46 | -4.87 | -24.76 | 218 |
| 51 | Agent (ML meta-label) | meta | 83.92 | -16.08 | 660 | 18.5 | -14.98 | -2.60 | -17.86 | 379 |
| 52 | Donchian 20/10 · 1h | breakout | 83.56 | -16.43 | 79 | 17.7 | -0.48 | 0.15 | -22.76 | 216 |
| 53 | Three white soldiers | momentum | 82.61 | -17.39 | 225 | 18.2 | -47.28 | -19.03 | -47.28 | 601 |
| 54 | Williams %R · 1h | reversion | 82.23 | -17.77 | 180 | 42.2 | -33.53 | -5.30 | -36.50 | 521 |
| 55 | Bollinger reversion · 1h | reversion | 81.72 | -18.28 | 151 | 32.5 | -29.64 | -5.94 | -33.12 | 352 |
| 56 | ROC + volume · 1h | momentum | 81.27 | -18.73 | 195 | 21.0 | -15.72 | -2.15 | -28.75 | 390 |
| 57 | CCI reversion · 1h | reversion | 80.99 | -19.01 | 161 | 38.5 | -19.13 | -2.43 | -27.44 | 429 |
| 58 | RSI(14) reversion · 1h | reversion | 80.60 | -19.40 | 75 | 21.3 | -14.66 | -2.54 | -22.27 | 174 |
| 59 | EMA 9/21 cross · 1h | trend | 80.57 | -19.43 | 131 | 11.5 | -24.03 | -4.72 | -27.77 | 314 |
| 60 | Heikin-Ashi · 1h | trend | 80.15 | -19.85 | 211 | 22.7 | -35.00 | -5.82 | -43.48 | 667 |
| 61 | VWAP momentum · 1h | momentum | 78.82 | -21.18 | 415 | 20.5 | -35.83 | -4.79 | -47.57 | 1231 |
| 62 | Candlestick reversal · 1h | reversion | 77.93 | -22.07 | 207 | 26.1 | -34.43 | -5.97 | -36.48 | 540 |
| 63 | Volume breakout | breakout | 61.84 | -38.16 | 350 | 12.9 | -62.61 | -17.72 | -64.12 | 874 |
| 64 | ROC + volume | momentum | 61.61 | -38.39 | 571 | 21.9 | -75.69 | -17.44 | -78.03 | 1721 |
| 65 | Squeeze breakout | breakout | 60.37 | -39.63 | 455 | 14.1 | -62.34 | -15.88 | -65.55 | 1210 |
| 66 | Donchian 55/20 | breakout | 59.27 | -40.73 | 463 | 17.9 | -68.33 | -14.22 | -72.80 | 1269 |
| 67 | RSI(14) reversion | reversion | 58.23 | -41.77 | 693 | 24.8 | -74.29 | -16.30 | -74.48 | 1594 |
| 68 | EMA 20/50 cross | trend | 56.67 | -43.33 | 488 | 18.9 | -75.80 | -14.63 | -80.16 | 1422 |
| 69 | VWAP reversion | reversion | 53.38 | -46.62 | 723 | 24.1 | -72.01 | -14.74 | -72.83 | 1495 |
| 70 | Keltner breakout | breakout | 51.39 | -48.61 | 653 | 15.8 | -82.60 | -26.11 | -83.37 | 1803 |
| 71 | AI bee: Boozy | ai | 50.92 | -49.08 | 346 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.67 | -29.94 | -98.67 | 5321 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.36 | -30.14 | -93.65 | 2571 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.08 | -19.85 | -87.84 | 1890 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.05 | -24.06 | -90.91 | 2342 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.04 | -25.77 | -91.07 | 2281 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -32.30 | -97.45 | 3498 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.66 | -36.36 | -96.70 | 3586 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.43 | -26.62 | -94.74 | 2596 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.61 | -22.87 | -82.82 | 1709 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.00 | -99.37 | 5731 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.18 | -25.25 | -91.89 | 2615 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.11 | -31.69 | -96.11 | 3488 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.89 | -99.74 | 6184 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.41 | -28.79 | -91.41 | 2340 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.53 | -38.52 | -97.54 | 3644 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.44 | -98.46 | 4691 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.59 | -32.57 | -93.77 | 2788 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.91 | -99.52 | 6166 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.72 | -22.21 | -86.75 | 2152 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.93 | -26.82 | -87.93 | 2142 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -32.37 | -95.84 | 3756 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.86 | -32.26 | -89.03 | 2088 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -33.30 | -95.73 | 4104 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.53 | -99.90 | 8261 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T13:55 | ROC + volume · 1h | sell | ETH-USD | 20.39 | -0.29 | stop-loss |
| 2026-10-19T13:55 | Triple EMA stack · 1h | buy | XRP-USD | 4.77 | — | rebalance up |
| 2026-10-19T13:55 | Triple EMA stack · 1h | buy | SOL-USD | 4.44 | — | rebalance up |
| 2026-10-19T13:55 | Triple EMA stack · 1h | sell | ETH-USD | 17.63 | -0.35 | stop-loss |
| 2026-10-19T13:55 | Squeeze breakout | sell | TNA | 14.95 | -0.19 | stop-loss |
| 2026-10-19T13:55 | Squeeze breakout | sell | IWM | 15.07 | -0.07 | stop-loss |
| 2026-10-19T13:55 | ROC + volume | buy | TSLA | 15.37 | — | entry signal |
| 2026-10-19T13:55 | EMA 20/50 cross | buy | SOXL | 5.71 | — | entry signal |
| 2026-10-19T13:55 | EMA 20/50 cross | sell | AMZN | 2.84 | -0.00 | rebalance down |
| 2026-10-19T13:55 | EMA 20/50 cross | sell | AAPL | 2.86 | 0.00 | rebalance down |
| 2026-10-19T13:50 | Agent (aggressive) | buy | SQQQ | 45.14 | — | following Williams %R, Bollinger reversion, Heikin-Ashi · 1h |
| 2026-10-19T13:50 | Agent | buy | SQQQ | 18.09 | — | rebalance up |
| 2026-10-19T13:50 | ROC + volume | buy | QQQ | 15.37 | — | entry signal |
| 2026-10-19T13:50 | ROC + volume | buy | LABU | 15.37 | — | entry signal |
| 2026-10-19T13:50 | ROC + volume | sell | TNA | 15.43 | -0.14 | target is flat |
| 2026-10-19T13:50 | EMA 20/50 cross | buy | TSLA | 14.18 | — | entry signal |
| 2026-10-19T13:50 | EMA 20/50 cross | buy | AMD | 14.18 | — | entry signal |
| 2026-10-19T13:50 | EMA 20/50 cross | buy | AAPL | 14.18 | — | entry signal |
| 2026-10-19T13:45 | Day trade: Stocks in Play ORB | sell | SQQQ | 24.69 | -0.04 | target is flat |
| 2026-10-19T13:45 | Day trade: Stocks in Play ORB | sell | LABU | 23.69 | -1.03 | target is flat |
| 2026-10-19T13:45 | Agent (ML meta-label) | buy | SQQQ | 14.02 | — | following Williams %R, Bollinger reversion, Heikin-Ashi · 1h |
| 2026-10-19T13:45 | Keltner breakout | buy | GOOGL | 12.85 | — | entry signal |
| 2026-10-19T13:45 | ROC + volume | buy | PLTR | 15.37 | — | entry signal |
| 2026-10-19T13:45 | ROC + volume | sell | LABU | 14.91 | -0.65 | stop-loss |
| 2026-10-19T13:45 | EMA 20/50 cross | buy | AMZN | 14.18 | — | entry signal |
| 2026-10-19T13:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 24.72 | — | entry |
| 2026-10-19T13:40 | Day trade: Stocks in Play ORB | buy | LABU | 24.72 | — | entry |
| 2026-10-19T13:40 | Agent (ML meta-label) | sell | SQQQ | 14.05 | 0.02 | selected signal exited |
| 2026-10-19T13:40 | Squeeze breakout | buy | TNA | 15.14 | — | entry signal |
| 2026-10-19T13:40 | Squeeze breakout | buy | PLTR | 15.14 | — | entry signal |
| 2026-10-19T13:40 | Squeeze breakout | buy | MSFT | 15.14 | — | entry signal |
| 2026-10-19T13:40 | Squeeze breakout | buy | IWM | 15.14 | — | entry signal |
| 2026-10-19T13:40 | ROC + volume | buy | TNA | 15.57 | — | entry signal |
| 2026-10-19T13:40 | ROC + volume | buy | LABU | 15.57 | — | entry signal |
| 2026-10-19T13:40 | EMA 20/50 cross | sell | DOGE-USD | 14.15 | -0.14 | stop-loss |
| 2026-10-19T13:37 | Copy: Insider buying | buy | FLSC | 12.26 | — | entry |
| 2026-10-19T13:35 | Max aggression: 1-day momentum | buy | SOXL | 86.16 | — | entry |
| 2026-10-19T13:35 | Max aggression: 1-day momentum | sell | ETHU | 86.16 | -2.96 | target is flat |
| 2026-10-19T13:35 | Agent (rotation) | buy | SQQQ | 32.66 | — | following Williams %R, Bollinger reversion, Heikin-Ashi · 1h |
| 2026-10-19T13:35 | Agent (rotation) | sell | UPRO | 15.70 | -0.32 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 13:55:05.000131+00:00 -> 2026-10-19 14:05:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
