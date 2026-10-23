# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T21:10:05.000152+00:00 · 33475 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | — | — | No insider purchases returned |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.39 · VIX 19.80 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 38901 decisions in 3192 calls, $0.4803 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T21:10 | 3 / 2 / 0 | ETH-USD 14% |  |
| Breezy | 2026-10-23T21:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T21:10 | 5 / 0 / 0 | ETH-USD 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| Stochastic reversion | BITX | 1.69 | +8.43% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.50 | 6.50 | 0 | — | 7.97 | 4.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.17 | 2.05 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.41 | -3.16 | -13.74 | 155 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.84 | 0.83 | 0 | — | 3.44 | 1.62 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 5.24 | 2.57 | -2.26 | 102 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.85 | -2.15 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.33 | -3.67 | 0 | — | 1.31 | 0.39 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.35 | -6.22 | 195 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.70 | -4.30 | 0 | — | -0.88 | -0.32 | -5.99 | 1 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.56 | -5.44 | 0 | — | -6.51 | -2.76 | -7.76 | 1 |
| 19 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 20 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.55 | -7.08 | -21.85 | 115 |
| 21 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -16.09 | -3.65 | -17.44 | 98 |
| 22 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.48 | -17.21 | 562 |
| 23 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.38 | -27.80 | 24 |
| 24 | Parabolic SAR · 1h | trend | 92.05 | -7.95 | 118 | 25.4 | -20.96 | -4.98 | -24.17 | 254 |
| 25 | Daily: Momentum burst | daily | 91.74 | -8.26 | 10 | 10.0 | -17.52 | -3.41 | -20.97 | 40 |
| 26 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 27 | ADX DI cross · 1h | trend | 91.23 | -8.77 | 108 | 18.5 | -11.62 | -2.39 | -14.53 | 255 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | Daily: Bullish score | daily | 89.56 | -10.44 | 9 | 0.0 | -8.04 | -1.05 | -14.40 | 14 |
| 30 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 31 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.09 | -7.62 | -11.81 | 206 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 89.17 | -10.83 | 0 | — | -5.31 | -0.77 | -14.52 | 1 |
| 33 | Bollinger breakout · 1h | breakout | 89.04 | -10.96 | 105 | 27.6 | -12.22 | -2.43 | -16.56 | 241 |
| 34 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.78 | -4.42 | -15.12 | 95 |
| 35 | Stochastic reversion · 1h | reversion | 87.19 | -12.81 | 186 | 45.2 | -20.30 | -3.85 | -22.47 | 385 |
| 36 | Keltner breakout · 1h | breakout | 86.32 | -13.68 | 73 | 23.3 | -22.69 | -4.82 | -24.32 | 190 |
| 37 | EMA 20/50 cross · 1h | trend | 86.15 | -13.85 | 71 | 11.3 | -22.80 | -4.56 | -25.11 | 138 |
| 38 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.07 | -4.71 | -17.87 | 703 |
| 39 | Supertrend · 1h | trend | 86.09 | -13.91 | 108 | 14.8 | -23.71 | -5.01 | -26.47 | 212 |
| 40 | RSI momentum · 1h | momentum | 85.63 | -14.37 | 101 | 15.8 | -21.46 | -4.61 | -23.39 | 216 |
| 41 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.30 | -8.05 | -27.06 | 196 |
| 42 | MACD cross · 1h | trend | 84.72 | -15.28 | 220 | 23.2 | -23.11 | -4.65 | -26.30 | 454 |
| 43 | Ichimoku · 1h | trend | 83.92 | -16.08 | 65 | 12.3 | -23.71 | -4.95 | -25.68 | 110 |
| 44 | Z-score reversion · 1h | reversion | 83.71 | -16.29 | 106 | 34.0 | -15.01 | -2.55 | -21.48 | 197 |
| 45 | Triple EMA stack · 1h | trend | 83.48 | -16.52 | 98 | 15.3 | -26.25 | -5.26 | -28.44 | 211 |
| 46 | MFI reversion · 1h | reversion | 82.03 | -17.96 | 258 | 31.8 | -17.76 | -2.92 | -20.54 | 144 |
| 47 | MACD zero-line · 1h | trend | 81.57 | -18.43 | 105 | 15.2 | -21.73 | -4.57 | -25.17 | 218 |
| 48 | Donchian 20/10 · 1h | breakout | 81.27 | -18.73 | 97 | 19.6 | -24.50 | -4.78 | -27.45 | 217 |
| 49 | Three white soldiers | momentum | 81.27 | -18.73 | 275 | 20.0 | -43.55 | -21.16 | -43.66 | 589 |
| 50 | OBV trend · 1h | momentum | 81.11 | -18.89 | 203 | 17.2 | -31.99 | -7.07 | -33.48 | 303 |
| 51 | Williams %R · 1h | reversion | 80.95 | -19.05 | 213 | 44.1 | -35.51 | -6.38 | -36.69 | 525 |
| 52 | Bollinger reversion · 1h | reversion | 80.20 | -19.80 | 171 | 34.5 | -31.16 | -6.53 | -32.19 | 362 |
| 53 | CCI reversion · 1h | reversion | 80.07 | -19.93 | 198 | 42.9 | -26.59 | -4.02 | -28.17 | 451 |
| 54 | Agent (ML meta-label) | meta | 79.51 | -20.49 | 858 | 18.6 | -12.27 | -2.17 | -15.07 | 378 |
| 55 | Heikin-Ashi · 1h | trend | 78.64 | -21.36 | 271 | 22.9 | -43.24 | -10.17 | -43.93 | 653 |
| 56 | ROC + volume · 1h | momentum | 78.20 | -21.80 | 240 | 23.8 | -31.09 | -6.24 | -32.25 | 380 |
| 57 | RSI(14) reversion · 1h | reversion | 77.88 | -22.12 | 91 | 23.1 | -15.19 | -2.82 | -23.51 | 186 |
| 58 | Candlestick reversal · 1h | reversion | 77.24 | -22.76 | 254 | 28.7 | -34.89 | -6.63 | -36.06 | 539 |
| 59 | EMA 9/21 cross · 1h | trend | 77.03 | -22.97 | 161 | 11.8 | -30.24 | -6.22 | -33.53 | 318 |
| 60 | VWAP momentum · 1h | momentum | 75.52 | -24.48 | 527 | 21.1 | -50.61 | -11.76 | -50.81 | 1218 |
| 61 | Max aggression: 1-day momentum | meta | 67.42 | -32.59 | 18 | 27.8 | -42.46 | -2.98 | -50.32 | 42 |
| 62 | ROC + volume | momentum | 57.60 | -42.40 | 706 | 22.7 | -74.49 | -26.97 | -74.70 | 1547 |
| 63 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -61.07 | -25.77 | -61.07 | 764 |
| 64 | Squeeze breakout | breakout | 53.87 | -46.13 | 547 | 14.3 | -66.06 | -28.85 | -66.19 | 1140 |
| 65 | Donchian 55/20 | breakout | 53.11 | -46.89 | 565 | 19.1 | -71.55 | -23.69 | -71.69 | 1251 |
| 66 | RSI(14) reversion | reversion | 53.08 | -46.92 | 826 | 26.4 | -76.52 | -19.77 | -76.81 | 1668 |
| 67 | EMA 20/50 cross | trend | 51.90 | -48.09 | 622 | 20.1 | -78.82 | -23.90 | -79.12 | 1408 |
| 68 | VWAP reversion | reversion | 50.74 | -49.26 | 816 | 25.1 | -74.50 | -17.55 | -74.75 | 1549 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -45.02 | -98.66 | 5014 |
| 70 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.78 | -47.48 | -93.82 | 2510 |
| 71 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.39 | -30.48 | -88.50 | 1876 |
| 72 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.11 | -38.68 | -91.17 | 2303 |
| 73 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.36 | -31.57 | -90.40 | 2149 |
| 74 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -54.94 | -97.67 | 3458 |
| 75 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.96 | -62.08 | -95.98 | 3318 |
| 76 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.69 | -35.44 | -93.73 | 2424 |
| 77 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.65 | -36.40 | -82.71 | 1679 |
| 78 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.31 | -55.75 | -99.32 | 5679 |
| 79 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.17 | -42.45 | -92.22 | 2575 |
| 80 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -40.60 | -95.29 | 3349 |
| 81 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.64 | -99.75 | 6088 |
| 82 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.95 | -46.36 | -91.96 | 2310 |
| 83 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.51 | -65.79 | -97.52 | 3517 |
| 84 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -60.29 | -98.48 | 4716 |
| 85 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 86 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.16 | -60.08 | -94.19 | 2729 |
| 87 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.58 | -39.90 | -83.65 | 1767 |
| 88 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -67.48 | -99.53 | 6165 |
| 89 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.58 | -29.01 | -87.65 | 2186 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.10 | -38.67 | -90.17 | 2235 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -48.29 | -95.92 | 3747 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.31 | -51.03 | -89.41 | 2083 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.05 | -48.83 | -96.09 | 4116 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -111.65 | -99.90 | 8127 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T21:10 | RSI(14) reversion | sell | DOGE-USD | 13.24 | -0.06 | exit signal |
| 2026-10-23T21:00 | MACD cross · 1h | sell | BTC-USD | 12.10 | -0.05 | exit signal |
| 2026-10-23T20:55 | RSI(14) reversion | sell | SOL-USD | 13.25 | -0.06 | exit signal |
| 2026-10-23T20:45 | RSI(14) reversion | sell | XRP-USD | 13.28 | -0.03 | exit signal |
| 2026-10-23T20:45 | Squeeze breakout | buy | ETH-USD | 13.47 | — | entry signal |
| 2026-10-23T20:00 | Donchian 20/10 · 1h | sell | SOL-USD | 19.86 | -0.38 | stop-loss |
| 2026-10-23T20:00 | MACD zero-line · 1h | sell | SOL-USD | 20.20 | -0.33 | exit signal |
| 2026-10-23T20:00 | MACD zero-line · 1h | sell | DOGE-USD | 20.24 | -0.32 | exit signal |
| 2026-10-23T20:00 | MACD cross · 1h | sell | SOL-USD | 9.35 | -0.10 | exit signal |
| 2026-10-23T20:00 | MACD cross · 1h | sell | DOGE-USD | 12.10 | 0.03 | exit signal |
| 2026-10-23T20:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 9.51 | -0.18 | stop-loss |
| 2026-10-23T20:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 9.57 | -0.11 | exit signal |
| 2026-10-23T20:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 10.89 | -0.19 | exit signal |
| 2026-10-23T19:55 | VWAP reversion | buy | XRP-USD | 2.54 | — | rebalance up |
| 2026-10-23T19:55 | VWAP reversion | buy | SOL-USD | 2.56 | — | rebalance up |
| 2026-10-23T19:55 | VWAP reversion | buy | DOGE-USD | 2.55 | — | rebalance up |
| 2026-10-23T19:55 | VWAP reversion | sell | BITX | 10.13 | -0.01 | end-of-day flatten |
| 2026-10-23T19:55 | VWAP reversion | sell | AAPL | 10.15 | 0.03 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | UPRO | 2.82 | -0.01 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | TQQQ | 9.25 | -0.11 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | TNA | 8.51 | 0.03 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | TECL | 9.30 | 0.01 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | SOXL | 9.10 | -0.29 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | QQQ | 9.34 | -0.04 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | PLTR | 9.42 | 0.05 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | MSFT | 9.39 | 0.01 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | META | 9.34 | -0.06 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | IWM | 7.20 | 0.00 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 30m | sell | AMD | 9.27 | -0.06 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | TQQQ | 9.57 | -0.01 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | TECL | 5.35 | 0.02 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | SPY | 3.38 | -0.01 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | SOXL | 2.67 | 0.00 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | QQQ | 9.60 | -0.00 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | PLTR | 8.71 | 0.10 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | NVDA | 9.54 | -0.08 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | MSTR | 6.14 | -0.03 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | MSFT | 8.63 | 0.02 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | META | 9.59 | -0.02 | end-of-day flatten |
| 2026-10-23T19:55 | Opening range 15m | sell | IWM | 4.34 | 0.00 | end-of-day flatten |

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
