# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T19:55:05.000153+00:00 · 28706 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.38%)

Closed trades 86, win rate 39.5%, fees £2.89, max drawdown -9.99%.

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

Today: 34668 decisions in 2847 calls, $0.4280 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T19:55 | 5 / 7 / 18 | cash |  |
| Breezy | 2026-10-19T19:55 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-19T19:55 | 2 / 23 / 5 | cash |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.74 | 4.74 | 0 | — | 4.65 | 2.20 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.96 | -0.04 | 0 | — | 2.29 | 0.97 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.27 | -0.72 | 0 | — | -0.43 | -0.20 | -3.13 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.53 | -1.47 | 3 | 33.3 | 2.56 | 0.65 | -7.93 | 9 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.14 | 1.74 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -2.16 | -0.79 | -5.09 | 267 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.53 | -2.47 | 0 | — | -0.69 | -0.22 | -5.31 | 1 |
| 15 | Donchian 55/20 · 1h | breakout | 97.30 | -2.70 | 36 | 16.7 | -11.49 | -2.12 | -18.86 | 100 |
| 16 | Hold BTC | benchmark | 97.19 | -2.81 | 0 | — | 26.22 | 3.12 | -8.68 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.97 | -2.24 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.59 | -3.40 | 0 | — | -5.71 | -2.25 | -7.04 | 1 |
| 19 | Copy: Insider buying | copy | 96.50 | -3.50 | 23 | 43.5 | -14.93 | -2.70 | -20.62 | 73 |
| 20 | Trend pullback · 1h | trend | 96.47 | -3.54 | 88 | 23.9 | -19.71 | -5.79 | -20.57 | 137 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.26 | -4.74 | 8 | 37.5 | -20.23 | -1.70 | -34.64 | 26 |
| 23 | ADX DI cross · 1h | trend | 93.61 | -6.39 | 88 | 18.2 | -14.59 | -2.66 | -16.51 | 259 |
| 24 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.50 | 2.16 | -6.54 | 200 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 92.90 | -7.10 | 6 | 16.7 | -5.94 | -0.75 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.05 | -7.95 | 7 | 0.0 | -3.00 | -0.18 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.93 | -8.07 | 78 | 23.1 | -7.34 | -1.14 | -16.37 | 107 |
| 29 | Parabolic SAR · 1h | trend | 91.88 | -8.12 | 102 | 22.5 | -14.24 | -2.70 | -24.65 | 267 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.68 | -2.41 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -12.93 | -3.70 | -17.26 | 558 |
| 32 | Bollinger breakout · 1h | breakout | 90.82 | -9.18 | 84 | 28.6 | -8.63 | -1.45 | -16.89 | 256 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -3.87 | -1.01 | -16.59 | 250 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 90.50 | -9.50 | 0 | — | 1.78 | 0.44 | -14.37 | 1 |
| 35 | EMA 20/50 cross · 1h | trend | 90.42 | -9.58 | 58 | 13.8 | -19.02 | -3.39 | -21.31 | 126 |
| 36 | RSI momentum · 1h | momentum | 89.67 | -10.33 | 78 | 16.7 | -19.35 | -3.12 | -30.20 | 212 |
| 37 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.57 | -23.86 | 205 |
| 38 | Ichimoku · 1h | trend | 88.66 | -11.34 | 55 | 14.5 | -17.57 | -3.31 | -18.08 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.42 | -11.58 | 152 | 46.1 | -17.33 | -2.99 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | 7.15 | 1.29 | -19.49 | 121 |
| 41 | Keltner breakout · 1h | breakout | 87.76 | -12.24 | 56 | 23.2 | -13.02 | -1.90 | -27.85 | 199 |
| 42 | Triple EMA stack · 1h | trend | 87.70 | -12.30 | 85 | 15.3 | -22.77 | -3.41 | -32.98 | 230 |
| 43 | Supertrend · 1h | trend | 87.19 | -12.81 | 86 | 12.8 | -23.02 | -4.71 | -26.48 | 214 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -18.01 | -4.87 | -20.98 | 695 |
| 45 | MACD cross · 1h | trend | 86.07 | -13.93 | 189 | 20.6 | -26.35 | -4.93 | -32.78 | 470 |
| 46 | OBV trend · 1h | momentum | 85.44 | -14.56 | 179 | 17.9 | -24.61 | -3.35 | -36.04 | 312 |
| 47 | Z-score reversion · 1h | reversion | 85.36 | -14.64 | 91 | 30.8 | -14.13 | -2.31 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.49 | -15.52 | 209 | 31.1 | -17.32 | -2.70 | -21.34 | 137 |
| 49 | MACD zero-line · 1h | trend | 84.27 | -15.73 | 87 | 14.9 | -24.78 | -4.89 | -25.20 | 217 |
| 50 | Agent (ML meta-label) | meta | 83.88 | -16.12 | 681 | 18.8 | -9.55 | -1.70 | -16.28 | 372 |
| 51 | Donchian 20/10 · 1h | breakout | 83.74 | -16.26 | 81 | 17.3 | -5.90 | -0.53 | -27.92 | 214 |
| 52 | Max aggression: 1-day momentum | meta | 83.04 | -16.96 | 15 | 33.3 | -15.39 | -0.56 | -37.31 | 42 |
| 53 | Bollinger reversion · 1h | reversion | 82.90 | -17.10 | 158 | 34.8 | -27.76 | -5.29 | -33.52 | 349 |
| 54 | Three white soldiers | momentum | 82.52 | -17.48 | 231 | 19.0 | -47.27 | -18.69 | -47.56 | 603 |
| 55 | Williams %R · 1h | reversion | 82.13 | -17.87 | 182 | 42.9 | -33.35 | -5.30 | -36.50 | 530 |
| 56 | ROC + volume · 1h | momentum | 81.46 | -18.54 | 197 | 20.8 | -20.42 | -2.97 | -33.74 | 386 |
| 57 | CCI reversion · 1h | reversion | 80.74 | -19.25 | 163 | 39.3 | -18.06 | -2.27 | -27.44 | 439 |
| 58 | RSI(14) reversion · 1h | reversion | 80.27 | -19.73 | 75 | 21.3 | -20.11 | -3.57 | -25.21 | 173 |
| 59 | EMA 9/21 cross · 1h | trend | 80.11 | -19.89 | 135 | 11.1 | -29.40 | -6.08 | -29.54 | 314 |
| 60 | Heikin-Ashi · 1h | trend | 78.91 | -21.09 | 224 | 21.4 | -36.61 | -6.09 | -44.77 | 681 |
| 61 | VWAP momentum · 1h | momentum | 77.96 | -22.04 | 433 | 20.8 | -40.06 | -6.35 | -48.32 | 1246 |
| 62 | Candlestick reversal · 1h | reversion | 77.24 | -22.76 | 214 | 27.6 | -36.52 | -6.51 | -37.62 | 528 |
| 63 | ROC + volume | momentum | 61.91 | -38.09 | 594 | 22.4 | -76.04 | -17.95 | -78.19 | 1729 |
| 64 | Volume breakout | breakout | 61.60 | -38.40 | 358 | 13.1 | -62.58 | -17.75 | -64.19 | 875 |
| 65 | Squeeze breakout | breakout | 60.47 | -39.53 | 467 | 14.1 | -64.06 | -20.53 | -65.58 | 1205 |
| 66 | Donchian 55/20 | breakout | 59.19 | -40.81 | 475 | 18.5 | -67.91 | -13.55 | -72.80 | 1262 |
| 67 | RSI(14) reversion | reversion | 58.17 | -41.84 | 707 | 25.2 | -74.48 | -16.44 | -74.72 | 1593 |
| 68 | EMA 20/50 cross | trend | 56.90 | -43.10 | 512 | 19.9 | -75.15 | -13.51 | -80.26 | 1420 |
| 69 | VWAP reversion | reversion | 53.57 | -46.43 | 747 | 25.0 | -72.14 | -14.89 | -72.62 | 1504 |
| 70 | Keltner breakout | breakout | 51.12 | -48.88 | 672 | 16.2 | -82.35 | -24.73 | -83.49 | 1805 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.46 | -98.66 | 5279 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.04 | -27.51 | -93.68 | 2559 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -85.93 | -18.62 | -88.15 | 1890 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.77 | -22.37 | -91.08 | 2344 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.97 | -25.51 | -91.07 | 2263 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -30.79 | -97.54 | 3495 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.51 | -33.46 | -96.73 | 3568 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.42 | -27.85 | -94.51 | 2519 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.99 | -24.59 | -82.93 | 1695 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.03 | -99.38 | 5747 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.95 | -23.83 | -91.98 | 2622 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.12 | -31.52 | -96.13 | 3473 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.65 | -99.74 | 6187 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.70 | -29.39 | -91.70 | 2332 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -36.09 | -97.61 | 3625 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.31 | -98.47 | 4694 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.71 | -32.45 | -93.93 | 2799 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.54 | -99.52 | 6155 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.83 | -22.35 | -86.94 | 2134 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.92 | -26.67 | -87.92 | 2135 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -32.17 | -95.85 | 3738 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.04 | -32.52 | -89.08 | 2101 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.21 | -95.73 | 4103 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.91 | -99.90 | 8282 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T19:55 | Day trade: Stocks in Play ORB | sell | AMZN | 24.89 | 0.44 | target is flat |
| 2026-10-19T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 98.40 | -0.69 | target is flat |
| 2026-10-19T19:55 | Agent (ML meta-label) | buy | QQQ | 5.24 | — | entry |
| 2026-10-19T19:55 | Agent (aggressive) | sell | SQQQ | 88.03 | 0.49 | selected signal exited |
| 2026-10-19T19:55 | Agent | sell | SQQQ | 36.41 | 0.20 | selected signal exited |
| 2026-10-19T19:55 | Agent | sell | BITX | 18.01 | -0.09 | selected signal exited |
| 2026-10-19T19:55 | VWAP reversion | sell | MSTR | 8.93 | -0.02 | end-of-day flatten |
| 2026-10-19T19:55 | VWAP reversion | sell | BITX | 10.71 | -0.05 | end-of-day flatten |
| 2026-10-19T19:55 | VWAP reversion | sell | AMD | 8.08 | 0.00 | end-of-day flatten |
| 2026-10-19T19:55 | RSI(14) reversion | sell | MSTR | 14.40 | -0.12 | end-of-day flatten |
| 2026-10-19T19:55 | Three white soldiers | sell | NVDA | 20.55 | -0.11 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | UPRO | 6.72 | -0.03 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | TSLA | 6.72 | -0.04 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | TQQQ | 6.67 | -0.07 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | TNA | 6.73 | -0.03 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | SPY | 6.74 | -0.02 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | QQQ | 6.73 | -0.03 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | NVDA | 6.72 | -0.04 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | GOOGL | 6.73 | -0.02 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | AMZN | 6.73 | -0.02 | end-of-day flatten |
| 2026-10-19T19:55 | Keltner breakout | sell | TECL | 10.20 | -0.12 | end-of-day flatten |
| 2026-10-19T19:55 | Keltner breakout | sell | SOXL | 10.08 | -0.23 | end-of-day flatten |
| 2026-10-19T19:55 | Keltner breakout | sell | META | 10.29 | -0.01 | end-of-day flatten |
| 2026-10-19T19:55 | Keltner breakout | sell | GOOGL | 10.26 | -0.04 | end-of-day flatten |
| 2026-10-19T19:55 | Keltner breakout | sell | AMZN | 10.28 | -0.03 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 30m | sell | TSLA | 15.14 | 0.08 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 30m | sell | PLTR | 15.08 | 0.08 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 30m | sell | NVDA | 15.19 | -0.02 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 30m | sell | MSFT | 15.17 | -0.01 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 30m | sell | GOOGL | 15.18 | -0.01 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 30m | sell | AMZN | 15.19 | 0.18 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 15m | sell | TSLA | 14.39 | 0.07 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 15m | sell | PLTR | 14.33 | 0.07 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 15m | sell | NVDA | 14.43 | 0.00 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 15m | sell | MSFT | 14.41 | -0.01 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 15m | sell | GOOGL | 14.43 | -0.01 | end-of-day flatten |
| 2026-10-19T19:55 | Opening range 15m | sell | AMZN | 14.43 | 0.17 | end-of-day flatten |
| 2026-10-19T19:55 | Donchian 55/20 | sell | META | 14.79 | -0.01 | end-of-day flatten |
| 2026-10-19T19:55 | ROC + volume | sell | TQQQ | 15.47 | -0.15 | end-of-day flatten |
| 2026-10-19T19:55 | ROC + volume | sell | TECL | 15.44 | -0.19 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 19:55:05.000153+00:00 -> 2026-10-19 20:05:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
