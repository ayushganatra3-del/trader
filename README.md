# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T15:55:05.000290+00:00 · 28541 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.37%)

Closed trades 80, win rate 38.8%, fees £2.76, max drawdown -9.78%.

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

Today: 19965 decisions in 2352 calls, $0.2558 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T15:55 | 2 / 11 / 17 | cash |  |
| Breezy | 2026-10-19T15:55 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-19T15:55 | 0 / 27 / 3 | COIN 73% |  |

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
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.71 | 7.71 | 10 | 70.0 | 10.25 | 3.43 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.78 | 4.78 | 0 | — | 5.66 | 2.77 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.91 | -0.10 | 3 | 33.3 | 4.09 | 0.92 | -7.93 | 9 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.68 | -0.32 | 0 | — | 2.41 | 1.02 | -5.18 | 1 |
| 10 | Hold SPY | benchmark | 99.53 | -0.47 | 0 | — | 0.10 | 0.10 | -3.13 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.30 | -1.70 | 54 | 31.5 | 3.12 | 1.73 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.81 | -2.19 | 111 | 32.4 | -2.53 | -1.16 | -5.45 | 275 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.57 | -2.43 | 0 | — | -0.42 | -0.11 | -5.31 | 1 |
| 15 | Hold BTC | benchmark | 97.37 | -2.63 | 0 | — | 26.07 | 3.11 | -8.68 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.19 | -2.37 | -5.83 | 1 |
| 17 | Donchian 55/20 · 1h | breakout | 96.85 | -3.15 | 36 | 16.7 | -10.72 | -1.73 | -20.85 | 107 |
| 18 | Copy: Insider buying | copy | 96.78 | -3.22 | 23 | 43.5 | -14.61 | -2.64 | -20.62 | 73 |
| 19 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -19.83 | -5.87 | -20.58 | 135 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.18 | -3.83 | 0 | — | -7.03 | -2.78 | -7.55 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Gap and go | momentum | 94.06 | -5.94 | 70 | 12.9 | 10.53 | 2.62 | -6.51 | 202 |
| 23 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -0.78 | -0.10 | -9.46 | 94 |
| 24 | Daily: Momentum burst | daily | 93.29 | -6.71 | 6 | 16.7 | -5.58 | -0.69 | -20.58 | 40 |
| 25 | ADX DI cross · 1h | trend | 93.21 | -6.79 | 86 | 18.6 | -13.35 | -2.51 | -15.20 | 254 |
| 26 | Max aggression: 5-day momentum | meta | 93.15 | -6.85 | 8 | 37.5 | -21.92 | -1.86 | -34.64 | 26 |
| 27 | Daily: Bullish score | daily | 92.33 | -7.67 | 7 | 0.0 | -2.95 | -0.18 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.96 | -8.04 | 78 | 23.1 | -4.19 | -0.46 | -16.37 | 107 |
| 29 | Parabolic SAR · 1h | trend | 91.94 | -8.06 | 102 | 22.5 | -12.73 | -2.33 | -23.89 | 269 |
| 30 | Opening range 30m | breakout | 91.64 | -8.36 | 197 | 29.4 | -11.09 | -3.04 | -17.61 | 564 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -13.31 | -2.54 | -16.91 | 1 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.96 | -9.04 | 0 | — | 4.14 | 0.77 | -14.37 | 1 |
| 33 | Bollinger breakout · 1h | breakout | 90.85 | -9.15 | 84 | 28.6 | -3.66 | -0.41 | -17.80 | 261 |
| 34 | Agent | meta | 90.63 | -9.37 | 80 | 38.8 | -8.60 | -4.76 | -10.86 | 235 |
| 35 | EMA 20/50 cross · 1h | trend | 90.04 | -9.96 | 58 | 13.8 | -19.48 | -3.57 | -21.40 | 126 |
| 36 | RSI momentum · 1h | momentum | 89.42 | -10.59 | 78 | 16.7 | -16.57 | -2.92 | -26.86 | 215 |
| 37 | Stochastic reversion · 1h | reversion | 89.41 | -10.59 | 152 | 46.1 | -16.63 | -2.78 | -22.24 | 370 |
| 38 | Connors RSI(2) · 1h | reversion | 88.94 | -11.06 | 149 | 40.9 | -23.67 | -7.14 | -24.79 | 207 |
| 39 | Ichimoku · 1h | trend | 88.65 | -11.35 | 55 | 14.5 | -17.57 | -3.31 | -18.08 | 113 |
| 40 | Keltner breakout · 1h | breakout | 87.78 | -12.22 | 56 | 23.2 | -10.38 | -1.31 | -29.07 | 205 |
| 41 | Agent (aggressive) | meta | 87.73 | -12.27 | 40 | 32.5 | -2.14 | -0.60 | -9.23 | 110 |
| 42 | Supertrend · 1h | trend | 87.34 | -12.66 | 86 | 12.8 | -20.31 | -3.91 | -27.52 | 218 |
| 43 | Triple EMA stack · 1h | trend | 87.21 | -12.79 | 85 | 15.3 | -22.53 | -3.02 | -34.09 | 233 |
| 44 | Opening range 15m | breakout | 87.07 | -12.93 | 247 | 25.1 | -16.21 | -4.17 | -21.40 | 702 |
| 45 | Max aggression: 1-day momentum | meta | 86.99 | -13.01 | 15 | 33.3 | -11.28 | -0.29 | -37.31 | 42 |
| 46 | MACD cross · 1h | trend | 86.69 | -13.31 | 187 | 20.9 | -25.30 | -4.57 | -32.11 | 473 |
| 47 | Z-score reversion · 1h | reversion | 86.56 | -13.44 | 91 | 30.8 | -12.53 | -1.94 | -21.32 | 198 |
| 48 | OBV trend · 1h | momentum | 85.37 | -14.63 | 174 | 17.8 | -28.02 | -4.53 | -34.71 | 321 |
| 49 | Agent (ML meta-label) | meta | 84.73 | -15.27 | 664 | 18.8 | -18.55 | -3.15 | -24.52 | 390 |
| 50 | MFI reversion · 1h | reversion | 84.67 | -15.33 | 209 | 31.1 | -16.83 | -2.61 | -21.34 | 139 |
| 51 | MACD zero-line · 1h | trend | 84.40 | -15.60 | 86 | 15.1 | -24.83 | -4.96 | -25.14 | 218 |
| 52 | Donchian 20/10 · 1h | breakout | 83.29 | -16.71 | 81 | 17.3 | -0.62 | 0.15 | -25.09 | 215 |
| 53 | Williams %R · 1h | reversion | 83.10 | -16.90 | 182 | 42.9 | -32.87 | -5.13 | -36.50 | 535 |
| 54 | Three white soldiers | momentum | 82.88 | -17.12 | 225 | 18.2 | -47.13 | -18.90 | -47.41 | 606 |
| 55 | Bollinger reversion · 1h | reversion | 82.83 | -17.17 | 157 | 34.4 | -28.34 | -5.44 | -33.31 | 351 |
| 56 | RSI(14) reversion · 1h | reversion | 81.52 | -18.48 | 75 | 21.3 | -12.26 | -2.11 | -22.27 | 180 |
| 57 | ROC + volume · 1h | momentum | 81.51 | -18.49 | 197 | 20.8 | -17.46 | -2.21 | -33.03 | 391 |
| 58 | CCI reversion · 1h | reversion | 81.47 | -18.53 | 163 | 39.3 | -19.09 | -2.41 | -27.44 | 440 |
| 59 | EMA 9/21 cross · 1h | trend | 80.42 | -19.58 | 131 | 11.5 | -20.42 | -3.42 | -30.50 | 316 |
| 60 | Heikin-Ashi · 1h | trend | 79.78 | -20.22 | 212 | 22.6 | -35.74 | -5.93 | -44.06 | 681 |
| 61 | VWAP momentum · 1h | momentum | 78.95 | -21.05 | 418 | 20.3 | -35.23 | -4.64 | -47.95 | 1249 |
| 62 | Candlestick reversal · 1h | reversion | 78.46 | -21.54 | 210 | 26.7 | -34.08 | -5.90 | -37.86 | 534 |
| 63 | ROC + volume | momentum | 62.61 | -37.39 | 577 | 22.0 | -75.42 | -17.27 | -78.03 | 1733 |
| 64 | Volume breakout | breakout | 61.78 | -38.22 | 353 | 12.7 | -62.49 | -17.61 | -64.19 | 877 |
| 65 | Squeeze breakout | breakout | 60.93 | -39.07 | 455 | 14.1 | -64.01 | -20.76 | -65.58 | 1203 |
| 66 | Donchian 55/20 | breakout | 59.87 | -40.13 | 463 | 17.9 | -67.89 | -14.01 | -72.80 | 1276 |
| 67 | RSI(14) reversion | reversion | 57.86 | -42.14 | 700 | 24.9 | -74.68 | -16.57 | -74.70 | 1611 |
| 68 | EMA 20/50 cross | trend | 57.66 | -42.34 | 491 | 18.9 | -75.45 | -14.30 | -80.26 | 1433 |
| 69 | VWAP reversion | reversion | 53.87 | -46.13 | 737 | 25.0 | -72.20 | -14.88 | -72.88 | 1518 |
| 70 | Keltner breakout | breakout | 51.82 | -48.18 | 653 | 15.8 | -82.46 | -26.16 | -83.37 | 1814 |
| 71 | AI bee: Boozy | ai | 50.66 | -49.34 | 346 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.73 | -98.65 | 5317 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.12 | -28.93 | -93.67 | 2569 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.29 | -20.01 | -87.98 | 1898 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.93 | -23.83 | -90.92 | 2346 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.95 | -25.61 | -91.01 | 2268 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -32.24 | -97.48 | 3487 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -35.39 | -96.71 | 3581 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -26.20 | -94.78 | 2592 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.61 | -22.98 | -82.89 | 1707 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.20 | -99.38 | 5738 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.99 | -25.11 | -91.85 | 2620 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.10 | -31.62 | -96.11 | 3478 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.61 | -99.74 | 6181 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.41 | -28.78 | -91.47 | 2342 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.51 | -38.02 | -97.55 | 3628 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.40 | -98.47 | 4697 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.60 | -32.37 | -93.81 | 2797 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.13 | -99.53 | 6156 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.19 | -86.76 | 2149 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.87 | -26.70 | -87.87 | 2141 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.69 | -95.89 | 3761 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.94 | -32.49 | -89.01 | 2099 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.43 | -95.74 | 4097 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.10 | -99.90 | 8268 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T15:55 | Volume breakout | sell | LABU | 15.28 | -0.11 | target is flat |
| 2026-10-19T15:50 | ROC + volume | buy | LABU | 4.93 | — | entry |
| 2026-10-19T15:50 | ROC + volume | sell | SOL-USD | 4.93 | -0.06 | stop-loss |
| 2026-10-19T15:45 | VWAP reversion | buy | SQQQ | 13.46 | — | entry signal |
| 2026-10-19T15:45 | Volume breakout | buy | LABU | 15.39 | — | entry signal |
| 2026-10-19T15:41 | ROC + volume | buy | TQQQ | 2.60 | — | rebalance up |
| 2026-10-19T15:41 | ROC + volume | sell | ETHU | 2.60 | -0.04 | stop-loss |
| 2026-10-19T15:41 | EMA 20/50 cross | buy | IWM | 3.37 | — | entry |
| 2026-10-19T15:41 | EMA 20/50 cross | sell | DOGE-USD | 3.37 | -0.03 | exit signal |
| 2026-10-19T15:36 | Candlestick reversal · 1h | sell | QQQ | 6.48 | 0.11 | take-profit |
| 2026-10-19T15:36 | Three white soldiers | buy | MSFT | 12.45 | — | entry signal |
| 2026-10-19T15:36 | Three white soldiers | buy | AMZN | 16.58 | — | entry signal |
| 2026-10-19T15:36 | Three white soldiers | sell | TNA | 4.21 | 0.03 | rebalance down |
| 2026-10-19T15:36 | Three white soldiers | sell | NVDA | 4.16 | 0.01 | rebalance down |
| 2026-10-19T15:36 | Volume breakout | buy | SPY | 15.48 | — | entry |
| 2026-10-19T15:36 | EMA 20/50 cross | buy | GOOGL | 2.24 | — | entry |
| 2026-10-19T15:36 | EMA 20/50 cross | buy | DOGE-USD | 3.39 | — | entry |
| 2026-10-19T15:36 | EMA 20/50 cross | sell | AAPL | 5.63 | -0.01 | exit signal |
| 2026-10-19T15:30 | Agent (rotation) | buy | TQQQ | 32.61 | — | entry |
| 2026-10-19T15:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 107.79 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | UPRO | 5.28 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | TNA | 5.31 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | QQQ | 5.31 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | PLTR | 5.31 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | MSTR | 5.31 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | MSFT | 5.31 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | META | 5.31 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | LABU | 5.31 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | IWM | 5.31 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | GOOGL | 5.31 | — | entry |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | COIN | 5.31 | — | following EMA 20/50 cross |
| 2026-10-19T15:30 | Agent (ML meta-label) | buy | BITX | 5.31 | — | following VWAP reversion |
| 2026-10-19T15:30 | Agent (ML meta-label) | sell | SOXL | 11.83 | 0.43 | rebalance down |
| 2026-10-19T15:30 | Agent (ML meta-label) | sell | NVDA | 15.82 | 0.14 | rebalance down |
| 2026-10-19T15:30 | Agent (ML meta-label) | sell | ETHU | 15.84 | 0.03 | rebalance down |
| 2026-10-19T15:30 | Agent (ML meta-label) | sell | AMD | 15.94 | 0.12 | rebalance down |
| 2026-10-19T15:30 | CCI reversion · 1h | sell | TSLA | 4.08 | 0.02 | exit signal |
| 2026-10-19T15:30 | CCI reversion · 1h | sell | AMZN | 4.09 | 0.04 | exit signal |
| 2026-10-19T15:30 | Stochastic reversion · 1h | buy | UPRO | 5.07 | — | entry |
| 2026-10-19T15:30 | Stochastic reversion · 1h | sell | TSLA | 5.07 | 0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 15:55:05.000290+00:00 -> 2026-10-19 16:05:05.000290+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
