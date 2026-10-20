# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T19:55:05.000167+00:00 · 29876 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.86 (-9.14%)

Closed trades 90, win rate 41.1%, fees £2.98, max drawdown -9.99%.

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

Today: 39249 decisions in 2928 calls, $0.4808 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T19:55 | 4 / 17 / 9 | META 14% |  |
| Breezy | 2026-10-20T19:55 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-20T19:55 | 4 / 23 / 3 | ETHU 73% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.74 | 5.74 | 0 | — | 8.11 | 3.86 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.66 | -2.08 | -13.79 | 134 |
| 6 | Max aggression: 5-day momentum | meta | 100.99 | 0.99 | 9 | 44.4 | -13.01 | -0.90 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.90 | -1.10 | 0 | — | 0.26 | 0.20 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.70 | -1.30 | 62 | 35.5 | 4.26 | 2.23 | -1.45 | 61 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 98.37 | -1.63 | 0 | — | -0.66 | -0.19 | -5.15 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 97.96 | -2.04 | 3 | 33.3 | 4.29 | 0.99 | -7.93 | 8 |
| 14 | Hold BTC | benchmark | 97.62 | -2.38 | 0 | — | 19.20 | 2.57 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.79 | -2.14 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.99 | -3.01 | 0 | — | -4.14 | -1.58 | -7.04 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.80 | -3.20 | 0 | — | 0.05 | 0.08 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.21 | -3.79 | 40 | 15.0 | -17.69 | -3.48 | -21.38 | 102 |
| 19 | Agent (rotation) | meta | 96.04 | -3.96 | 114 | 31.6 | -6.39 | -3.12 | -8.16 | 304 |
| 20 | Copy: Insider buying | copy | 95.99 | -4.01 | 25 | 40.0 | -12.09 | -2.08 | -20.62 | 72 |
| 21 | Trend pullback · 1h | trend | 95.69 | -4.31 | 90 | 23.3 | -20.92 | -6.26 | -21.38 | 133 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.57 | -5.42 | 89 | 18.0 | -13.84 | -2.61 | -16.12 | 252 |
| 24 | Daily: Momentum burst | daily | 94.01 | -5.99 | 6 | 16.7 | -7.10 | -0.95 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.71 | 1.50 | -6.51 | 196 |
| 26 | Opening range 30m | breakout | 92.11 | -7.89 | 225 | 32.4 | -13.39 | -3.90 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.71 | -8.29 | 105 | 21.9 | -18.41 | -3.95 | -22.26 | 274 |
| 28 | Squeeze breakout · 1h | breakout | 91.64 | -8.36 | 46 | 21.7 | -3.37 | -0.74 | -11.48 | 98 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.17 | -2.30 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 91.13 | -8.87 | 7 | 0.0 | -7.83 | -0.88 | -13.10 | 13 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 90.88 | -9.12 | 0 | — | 0.90 | 0.30 | -14.37 | 1 |
| 32 | Agent | meta | 90.86 | -9.14 | 90 | 41.1 | -9.79 | -5.52 | -13.58 | 239 |
| 33 | Volume breakout · 1h | breakout | 90.57 | -9.43 | 84 | 22.6 | -12.40 | -2.22 | -13.91 | 107 |
| 34 | Bollinger breakout · 1h | breakout | 90.53 | -9.47 | 87 | 29.9 | -11.86 | -2.19 | -16.44 | 258 |
| 35 | Connors RSI(2) · 1h | reversion | 89.47 | -10.53 | 151 | 41.7 | -22.61 | -6.74 | -24.07 | 201 |
| 36 | RSI momentum · 1h | momentum | 89.21 | -10.79 | 83 | 15.7 | -23.65 | -4.59 | -26.04 | 217 |
| 37 | EMA 20/50 cross · 1h | trend | 88.52 | -11.48 | 62 | 12.9 | -19.23 | -3.53 | -21.37 | 132 |
| 38 | Opening range 15m | breakout | 88.26 | -11.74 | 270 | 29.3 | -17.72 | -4.78 | -20.79 | 699 |
| 39 | Supertrend · 1h | trend | 88.16 | -11.85 | 88 | 12.5 | -21.43 | -4.19 | -26.62 | 222 |
| 40 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -9.03 | -2.63 | -12.89 | 122 |
| 41 | Stochastic reversion · 1h | reversion | 87.89 | -12.12 | 164 | 47.0 | -14.56 | -2.43 | -22.24 | 362 |
| 42 | Keltner breakout · 1h | breakout | 87.25 | -12.75 | 60 | 21.7 | -16.68 | -2.75 | -26.39 | 206 |
| 43 | Ichimoku · 1h | trend | 86.79 | -13.21 | 60 | 13.3 | -19.12 | -3.60 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.29 | -13.71 | 193 | 20.2 | -27.39 | -5.28 | -33.68 | 470 |
| 45 | Triple EMA stack · 1h | trend | 85.22 | -14.78 | 91 | 14.3 | -31.15 | -5.78 | -35.14 | 229 |
| 46 | Donchian 20/10 · 1h | breakout | 84.55 | -15.45 | 81 | 17.3 | -14.96 | -2.03 | -28.55 | 219 |
| 47 | Z-score reversion · 1h | reversion | 84.55 | -15.45 | 96 | 30.2 | -14.24 | -2.34 | -21.32 | 195 |
| 48 | MFI reversion · 1h | reversion | 83.92 | -16.08 | 220 | 30.5 | -14.64 | -2.29 | -20.43 | 146 |
| 49 | OBV trend · 1h | momentum | 83.76 | -16.25 | 186 | 17.2 | -30.49 | -5.41 | -36.72 | 314 |
| 50 | Agent (ML meta-label) | meta | 83.72 | -16.28 | 711 | 19.1 | -2.28 | -0.21 | -15.61 | 376 |
| 51 | MACD zero-line · 1h | trend | 83.57 | -16.43 | 89 | 14.6 | -25.47 | -5.01 | -26.48 | 226 |
| 52 | Three white soldiers | momentum | 82.66 | -17.34 | 249 | 19.7 | -46.81 | -18.03 | -47.63 | 614 |
| 53 | Bollinger reversion · 1h | reversion | 82.20 | -17.80 | 162 | 35.8 | -29.44 | -5.71 | -32.84 | 347 |
| 54 | Williams %R · 1h | reversion | 81.47 | -18.53 | 195 | 43.6 | -30.59 | -4.72 | -36.49 | 524 |
| 55 | ROC + volume · 1h | momentum | 81.36 | -18.64 | 203 | 21.2 | -28.98 | -5.30 | -34.59 | 398 |
| 56 | CCI reversion · 1h | reversion | 80.74 | -19.26 | 178 | 41.6 | -18.20 | -2.27 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.18 | -19.82 | 232 | 20.7 | -42.47 | -8.89 | -47.30 | 673 |
| 58 | RSI(14) reversion · 1h | reversion | 79.72 | -20.28 | 83 | 22.9 | -15.21 | -2.67 | -23.28 | 184 |
| 59 | EMA 9/21 cross · 1h | trend | 79.56 | -20.44 | 143 | 10.5 | -29.39 | -6.13 | -30.19 | 326 |
| 60 | VWAP momentum · 1h | momentum | 77.61 | -22.39 | 463 | 19.9 | -44.99 | -8.05 | -50.53 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 77.33 | -22.67 | 226 | 28.8 | -36.47 | -6.67 | -38.74 | 540 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -27.93 | -1.54 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 61.59 | -38.41 | 628 | 23.1 | -78.00 | -22.03 | -78.44 | 1717 |
| 64 | Volume breakout | breakout | 61.59 | -38.41 | 377 | 14.1 | -63.33 | -19.13 | -64.07 | 871 |
| 65 | Squeeze breakout | breakout | 58.55 | -41.45 | 490 | 14.1 | -66.06 | -22.13 | -66.58 | 1204 |
| 66 | Donchian 55/20 | breakout | 57.80 | -42.20 | 503 | 19.3 | -70.51 | -17.46 | -73.50 | 1276 |
| 67 | RSI(14) reversion | reversion | 57.39 | -42.61 | 744 | 26.5 | -74.07 | -16.18 | -74.89 | 1610 |
| 68 | EMA 20/50 cross | trend | 55.66 | -44.34 | 551 | 19.4 | -76.87 | -15.62 | -80.87 | 1445 |
| 69 | VWAP reversion | reversion | 53.63 | -46.37 | 754 | 25.2 | -71.42 | -14.48 | -72.29 | 1500 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.78 | -31.03 | -98.78 | 5302 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -32.09 | -93.90 | 2596 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.66 | -20.41 | -88.38 | 1895 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.32 | -24.68 | -91.32 | 2351 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.99 | -25.64 | -91.20 | 2250 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.54 | -32.93 | -97.64 | 3520 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.68 | -36.97 | -96.70 | 3565 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -28.12 | -94.47 | 2532 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.70 | -27.38 | -82.70 | 1707 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.77 | -99.37 | 5741 |
| 80 | Keltner breakout | breakout | 50.28 | -49.73 | 703 | 16.8 | -83.30 | -27.51 | -83.82 | 1803 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.74 | -27.42 | -92.26 | 2622 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.95 | -31.54 | -95.96 | 3461 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -40.92 | -99.75 | 6192 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.56 | -28.99 | -91.63 | 2351 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -38.24 | -97.67 | 3606 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.07 | -98.47 | 4708 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.04 | -34.68 | -94.05 | 2797 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.55 | -99.52 | 6187 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.61 | -21.99 | -87.01 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.80 | -26.23 | -88.00 | 2134 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -32.40 | -95.97 | 3767 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.09 | -32.48 | -89.35 | 2113 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.63 | -32.63 | -95.77 | 4110 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.45 | -99.90 | 8287 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T19:55 | Day trade: Stocks in Play ORB | sell | LABU | 24.57 | -0.15 | target is flat |
| 2026-10-20T19:55 | Day trade: Stocks in Play ORB | sell | IWM | 24.80 | 0.24 | target is flat |
| 2026-10-20T19:55 | Agent | sell | TSLA | 36.52 | 0.24 | selected signal exited |
| 2026-10-20T19:55 | MFI reversion · 1h | buy | IWM | 5.57 | — | entry |
| 2026-10-20T19:55 | VWAP reversion | sell | AAPL | 13.40 | -0.01 | end-of-day flatten |
| 2026-10-20T19:55 | RSI(14) reversion | sell | META | 14.43 | 0.03 | end-of-day flatten |
| 2026-10-20T19:55 | RSI(14) reversion | sell | COIN | 14.36 | 0.02 | end-of-day flatten |
| 2026-10-20T19:55 | RSI(14) reversion | sell | AAPL | 14.31 | -0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Squeeze breakout | sell | SQQQ | 14.63 | -0.04 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | UPRO | 4.90 | -0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TSLA | 5.14 | 0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TQQQ | 5.09 | 0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TNA | 5.20 | 0.06 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TECL | 5.09 | 0.05 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | SPY | 5.12 | -0.02 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | SOXL | 5.12 | 0.10 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | QQQ | 5.12 | -0.00 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | PLTR | 5.08 | -0.05 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | NVDA | 5.11 | -0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | MSTR | 5.14 | 0.13 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | LABU | 5.28 | 0.14 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | IWM | 5.15 | 0.02 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | ETHU | 5.63 | 0.06 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | COIN | 4.66 | -0.04 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | BITX | 5.07 | 0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | AMD | 5.10 | 0.02 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | UPRO | 6.23 | 0.05 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | TSLA | 6.25 | 0.04 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | TQQQ | 6.25 | 0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | TNA | 6.31 | 0.16 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | TECL | 6.29 | 0.07 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | SPY | 6.22 | -0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | SOXL | 6.39 | 0.17 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | QQQ | 6.22 | 0.00 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | MSTR | 6.44 | 0.27 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | LABU | 6.52 | 0.42 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | IWM | 6.25 | 0.05 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | ETHU | 6.36 | 0.16 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | COIN | 6.24 | 0.04 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | BITX | 6.29 | 0.10 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 19:55:05.000167+00:00 -> 2026-10-20 20:05:05.000167+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
