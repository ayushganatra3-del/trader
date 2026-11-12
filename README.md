# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T21:10:05.000300+00:00 · 57367 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.55 (-14.45%)

Closed trades 190, win rate 35.3%, fees £5.54, max drawdown -14.98%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-12 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.39 · VIX 18.89 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 41420 decisions in 3323 calls, $0.5109 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T21:10 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-12T21:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-12T21:10 | 1 / 3 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.01 | 17.01 | 0 | — | 14.68 | 4.92 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.62 | 12.62 | 22 | 68.2 | 16.23 | 3.32 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.73 | 11.73 | 34 | 29.4 | 20.04 | 2.99 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.97 | 3.97 | 0 | — | 6.13 | 1.70 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.73 | 0.73 | 140 | 35.0 | 7.14 | 2.82 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.44 | 1.84 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.50 | -1.50 | 0 | — | -0.22 | 0.00 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.86 | -2.14 | 1 | 0.0 | -2.09 | -1.42 | -5.83 | 2 |
| 13 | Agent (rotation) | meta | 97.84 | -2.16 | 191 | 30.4 | -1.05 | -0.33 | -8.69 | 167 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.84 | -3.16 | 0 | — | -3.40 | -0.86 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.47 | -4.53 | 143 | 47.6 | -12.76 | -3.31 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 95.00 | -5.00 | 43 | 39.5 | -6.54 | -1.28 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.06 | -5.94 | 0 | — | -4.23 | -1.12 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 93.19 | -6.81 | 1 | 0.0 | -7.08 | -1.56 | -16.91 | 2 |
| 21 | Trend pullback · 1h | trend | 91.75 | -8.25 | 110 | 22.7 | -13.08 | -4.55 | -17.58 | 73 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Parabolic SAR · 1h | trend | 85.97 | -14.03 | 171 | 27.5 | -14.02 | -2.98 | -21.80 | 220 |
| 24 | Opening range 30m | breakout | 85.89 | -14.11 | 433 | 33.3 | -10.11 | -3.19 | -14.11 | 601 |
| 25 | Agent | meta | 85.55 | -14.45 | 190 | 35.3 | -14.79 | -7.38 | -15.37 | 215 |
| 26 | Daily: Bullish score | daily | 84.72 | -15.28 | 16 | 18.8 | -11.13 | -1.80 | -19.56 | 15 |
| 27 | Hold BTC | benchmark | 84.14 | -15.86 | 1 | 0.0 | -7.80 | -1.03 | -18.34 | 1 |
| 28 | Donchian 55/20 · 1h | breakout | 83.95 | -16.05 | 73 | 13.7 | -22.51 | -4.72 | -29.68 | 94 |
| 29 | Agent (aggressive) | meta | 83.73 | -16.27 | 92 | 33.7 | -17.62 | -4.95 | -19.13 | 104 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.29 | -17.71 | 2 | 0.0 | -8.10 | -0.89 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.66 | -18.34 | 114 | 23.7 | -15.25 | -3.04 | -25.14 | 169 |
| 32 | ADX DI cross · 1h | trend | 81.45 | -18.55 | 191 | 19.4 | -20.55 | -3.14 | -29.51 | 273 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -32.69 | -1.99 | -45.81 | 22 |
| 34 | Connors RSI(2) · 1h | reversion | 80.94 | -19.06 | 210 | 40.5 | -17.94 | -6.30 | -18.41 | 116 |
| 35 | Volume breakout · 1h | breakout | 80.15 | -19.85 | 159 | 28.3 | -12.63 | -2.93 | -21.22 | 91 |
| 36 | MFI reversion · 1h | reversion | 79.84 | -20.16 | 385 | 35.8 | -18.12 | -2.30 | -23.02 | 163 |
| 37 | Stochastic reversion · 1h | reversion | 79.50 | -20.50 | 297 | 47.5 | -26.90 | -3.98 | -27.43 | 389 |
| 38 | Opening range 15m | breakout | 78.23 | -21.77 | 524 | 31.3 | -17.52 | -4.71 | -21.36 | 715 |
| 39 | Heikin-Ashi · 1h | trend | 77.76 | -22.24 | 435 | 24.6 | -36.05 | -6.73 | -38.20 | 657 |
| 40 | MACD cross · 1h | trend | 77.09 | -22.91 | 376 | 23.1 | -27.55 | -4.07 | -38.65 | 471 |
| 41 | Bollinger breakout · 1h | breakout | 76.61 | -23.39 | 179 | 22.3 | -20.87 | -4.31 | -29.92 | 239 |
| 42 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -15.60 | -0.34 | -57.50 | 40 |
| 43 | MACD zero-line · 1h | trend | 75.76 | -24.24 | 168 | 17.9 | -21.65 | -4.22 | -30.99 | 204 |
| 44 | Supertrend · 1h | trend | 75.54 | -24.46 | 172 | 14.0 | -27.81 | -4.76 | -36.51 | 212 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 46 | RSI momentum · 1h | momentum | 75.05 | -24.95 | 162 | 13.6 | -23.82 | -3.66 | -36.35 | 212 |
| 47 | EMA 20/50 cross · 1h | trend | 74.71 | -25.29 | 105 | 10.5 | -27.60 | -4.65 | -38.62 | 124 |
| 48 | Daily: Momentum burst | daily | 74.15 | -25.85 | 27 | 11.1 | -30.27 | -4.08 | -36.97 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.43 | -26.57 | 147 | 14.3 | -26.11 | -4.26 | -37.19 | 205 |
| 50 | ROC + volume · 1h | momentum | 72.91 | -27.09 | 390 | 28.7 | -30.07 | -5.58 | -38.32 | 375 |
| 51 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -36.45 | -5.65 | -36.62 | 457 |
| 52 | Donchian 20/10 · 1h | breakout | 72.16 | -27.84 | 145 | 19.3 | -27.07 | -4.89 | -35.90 | 209 |
| 53 | Bollinger reversion · 1h | reversion | 72.13 | -27.88 | 290 | 41.0 | -31.90 | -4.93 | -35.72 | 378 |
| 54 | OBV trend · 1h | momentum | 71.63 | -28.37 | 290 | 19.3 | -26.51 | -4.56 | -36.52 | 275 |
| 55 | Williams %R · 1h ⏸ | reversion | 67.95 | -32.05 | 372 | 43.8 | -42.06 | -6.90 | -42.13 | 528 |
| 56 | Z-score reversion · 1h | reversion | 67.82 | -32.18 | 199 | 38.2 | -27.39 | -3.80 | -29.17 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 67.27 | -32.73 | 259 | 10.0 | -35.11 | -7.18 | -41.97 | 329 |
| 58 | VWAP momentum · 1h | momentum | 66.20 | -33.80 | 895 | 22.3 | -51.44 | -10.49 | -51.91 | 1216 |
| 59 | Agent (ML meta-label) | meta | 66.17 | -33.83 | 1819 | 24.8 | -18.87 | -2.64 | -22.93 | 350 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -35.37 | -5.14 | -35.94 | 235 |
| 61 | Candlestick reversal · 1h | reversion | 62.66 | -37.34 | 469 | 28.4 | -43.87 | -8.05 | -43.92 | 589 |
| 62 | Three white soldiers | momentum | 58.62 | -41.38 | 537 | 14.5 | -49.70 | -22.55 | -49.70 | 664 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.75 | -99.00 | 5255 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.89 | -25.54 | -79.89 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.79 | -46.43 | -93.79 | 2534 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.31 | -31.66 | -89.42 | 1916 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.18 | -41.17 | -91.18 | 2329 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.91 | -31.60 | -89.95 | 2203 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -53.75 | -97.91 | 3481 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -57.60 | -96.34 | 3418 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -32.52 | -93.50 | 2318 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.19 | -34.91 | -83.19 | 1660 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -55.73 | -99.57 | 5987 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.28 | -44.01 | -92.28 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.38 | -36.87 | -95.39 | 3472 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -78.57 | -99.82 | 6156 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.38 | -44.20 | -92.40 | 2268 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.40 | -25.48 | -75.40 | 1625 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -61.70 | -97.67 | 3517 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -63.82 | -98.87 | 4918 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.68 | -27.26 | -68.68 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.81 | -59.05 | -94.81 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.11 | -39.48 | -85.11 | 1782 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.21 | -99.65 | 6349 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.97 | -32.50 | -90.00 | 2301 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.84 | -19.85 | -78.14 | 1762 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.66 | -36.81 | -90.71 | 2176 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.83 | -52.43 | -96.83 | 3852 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.34 | -58.26 | -89.34 | 2136 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.44 | -30.65 | -66.44 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.44 | -23.12 | -71.53 | 1255 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.07 | -18.93 | -79.37 | 1706 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.31 | -50.04 | -97.32 | 4308 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.59 | -99.93 | 8370 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T21:00 | VWAP reversion · 1h | sell | XRP-USD | 23.96 | 0.07 | exit signal |
| 2026-11-12T21:00 | VWAP momentum · 1h | buy | XRP-USD | 8.28 | — | entry signal |
| 2026-11-12T21:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.63 | -0.06 | exit signal |
| 2026-11-12T21:00 | MACD cross · 1h | buy | DOGE-USD | 9.64 | — | entry signal |
| 2026-11-12T20:55 | Agent (rotation) | sell | TQQQ | 65.29 | -0.77 | selected signal exited |
| 2026-11-12T20:55 | Day trade: Stocks in Play ORB | sell | UPRO | 24.86 | 0.04 | target is flat |
| 2026-11-12T20:55 | Day trade: Stocks in Play ORB | sell | TECL | 25.49 | 0.66 | target is flat |
| 2026-11-12T20:55 | Day trade: Stocks in Play ORB | sell | NVDA | 25.88 | 0.95 | target is flat |
| 2026-11-12T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 112.62 | 0.36 | target is flat |
| 2026-11-12T20:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 111.73 | 2.14 | target is flat |
| 2026-11-12T20:55 | Agent (aggressive) | sell | LABU | 41.74 | -0.25 | selected signal exited |
| 2026-11-12T20:55 | Agent | sell | SQQQ | 17.20 | 0.03 | selected signal exited |
| 2026-11-12T20:55 | Agent | sell | LABU | 17.05 | -0.10 | selected signal exited |
| 2026-11-12T20:55 | MFI reversion · 1h | sell | TECL | 6.10 | 0.21 | target is flat |
| 2026-11-12T20:55 | Opening range 30m | sell | TQQQ | 6.10 | -0.05 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 30m | sell | TECL | 6.07 | 0.05 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 30m | sell | SOXL | 5.97 | -0.10 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 30m | sell | QQQ | 6.20 | -0.02 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 30m | sell | PLTR | 6.20 | -0.02 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 30m | sell | NVDA | 6.19 | 0.06 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 30m | sell | MSTR | 6.05 | 0.01 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 30m | sell | GOOGL | 6.23 | -0.01 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 30m | sell | ETHU | 6.13 | 0.02 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 30m | sell | AMD | 6.18 | -0.07 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | UPRO | 8.67 | -0.03 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | TQQQ | 8.67 | -0.07 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | TECL | 8.69 | 0.10 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | SPY | 8.73 | -0.00 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | SOXL | 8.61 | -0.14 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | QQQ | 8.73 | -0.03 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | NVDA | 8.78 | 0.13 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | MSTR | 8.67 | -0.08 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | ETHU | 2.68 | 0.01 | end-of-day flatten |
| 2026-11-12T20:55 | Opening range 15m | sell | AMD | 6.00 | -0.02 | end-of-day flatten |
| 2026-11-12T20:35 | MFI reversion · 1h | buy | LABU | 7.24 | — | entry |
| 2026-11-12T20:35 | MFI reversion · 1h | sell | SOXL | 6.16 | -0.09 | target is flat |
| 2026-11-12T20:35 | Opening range 30m | sell | SPY | 6.20 | -0.02 | stop-loss |
| 2026-11-12T20:35 | Opening range 30m | sell | COIN | 6.06 | -0.19 | stop-loss |
| 2026-11-12T20:35 | Opening range 15m | buy | ETHU | 2.67 | — | entry |
| 2026-11-12T20:35 | Opening range 15m | sell | COIN | 2.67 | -0.03 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 21:10:05.000300+00:00 -> 2026-11-12 21:20:05.000300+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
