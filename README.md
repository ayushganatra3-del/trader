# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T20:40:05.000137+00:00 · 57338 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.68 (-14.31%)

Closed trades 188, win rate 35.1%, fees £5.53, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 17.14 | -0.01 |
| SQQQ | 17.24 | +0.07 |

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

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 39626 decisions in 3236 calls, $0.4896 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T20:40 | 7 / 17 / 6 | cash |  |
| Breezy | 2026-11-12T20:40 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-12T20:40 | 7 / 21 / 2 | COIN 58% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.96 | 16.96 | 0 | — | 14.63 | 4.90 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.47 | 12.47 | 21 | 66.7 | 16.08 | 3.29 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.58 | 11.58 | 33 | 27.3 | 19.88 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.10 | 4.10 | 0 | — | 6.26 | 1.73 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.43 | 0.43 | 137 | 33.6 | 6.83 | 2.71 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.44 | 1.84 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.50 | -1.50 | 0 | — | -0.23 | 0.00 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 97.75 | -2.25 | 190 | 30.5 | -1.14 | -0.36 | -8.69 | 167 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.74 | -2.26 | 1 | 0.0 | -2.21 | -1.52 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.68 | -3.32 | 0 | — | -3.56 | -0.90 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.55 | -4.45 | 142 | 47.2 | -12.69 | -3.28 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 94.92 | -5.08 | 43 | 39.5 | -6.56 | -1.28 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.15 | -5.85 | 0 | — | -4.14 | -1.09 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 92.88 | -7.12 | 1 | 0.0 | -7.38 | -1.65 | -16.91 | 2 |
| 21 | Trend pullback · 1h | trend | 91.82 | -8.18 | 110 | 22.7 | -13.01 | -4.52 | -17.58 | 73 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Parabolic SAR · 1h | trend | 86.11 | -13.89 | 171 | 27.5 | -13.82 | -2.93 | -21.80 | 220 |
| 24 | Opening range 30m | breakout | 85.78 | -14.21 | 423 | 32.4 | -10.28 | -3.26 | -14.11 | 601 |
| 25 | Agent | meta | 85.68 | -14.31 | 188 | 35.1 | -14.69 | -7.34 | -15.40 | 215 |
| 26 | Daily: Bullish score | daily | 84.86 | -15.14 | 16 | 18.8 | -10.98 | -1.77 | -19.56 | 15 |
| 27 | Hold BTC | benchmark | 84.17 | -15.83 | 1 | 0.0 | -7.96 | -1.03 | -18.34 | 1 |
| 28 | Agent (aggressive) | meta | 83.95 | -16.05 | 91 | 34.1 | -17.49 | -4.92 | -19.21 | 104 |
| 29 | Donchian 55/20 · 1h | breakout | 83.91 | -16.09 | 73 | 13.7 | -22.54 | -4.73 | -29.68 | 94 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.36 | -17.64 | 2 | 0.0 | -8.02 | -0.88 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.67 | -18.33 | 114 | 23.7 | -15.23 | -3.03 | -25.14 | 169 |
| 32 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -33.31 | -2.05 | -45.81 | 22 |
| 33 | ADX DI cross · 1h | trend | 81.21 | -18.79 | 191 | 19.4 | -20.12 | -3.07 | -29.51 | 269 |
| 34 | Connors RSI(2) · 1h | reversion | 80.99 | -19.01 | 210 | 40.5 | -17.89 | -6.28 | -18.41 | 116 |
| 35 | Volume breakout · 1h | breakout | 80.22 | -19.78 | 159 | 28.3 | -12.56 | -2.91 | -21.17 | 91 |
| 36 | MFI reversion · 1h | reversion | 79.81 | -20.18 | 384 | 35.7 | -18.13 | -2.30 | -23.02 | 163 |
| 37 | Stochastic reversion · 1h | reversion | 79.56 | -20.44 | 297 | 47.5 | -26.83 | -3.97 | -27.43 | 389 |
| 38 | Opening range 15m | breakout | 78.08 | -21.92 | 514 | 31.1 | -17.62 | -4.75 | -21.36 | 715 |
| 39 | Heikin-Ashi · 1h | trend | 77.64 | -22.36 | 435 | 24.6 | -36.15 | -6.74 | -38.20 | 657 |
| 40 | MACD cross · 1h | trend | 77.00 | -23.00 | 376 | 23.1 | -27.63 | -4.08 | -38.65 | 469 |
| 41 | Bollinger breakout · 1h | breakout | 76.62 | -23.38 | 179 | 22.3 | -20.86 | -4.30 | -29.92 | 239 |
| 42 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -16.12 | -0.37 | -57.50 | 40 |
| 43 | MACD zero-line · 1h | trend | 75.47 | -24.53 | 168 | 17.9 | -21.94 | -4.28 | -30.99 | 204 |
| 44 | Supertrend · 1h | trend | 75.41 | -24.59 | 172 | 14.0 | -27.93 | -4.79 | -36.51 | 212 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 46 | RSI momentum · 1h | momentum | 74.95 | -25.05 | 162 | 13.6 | -24.15 | -3.73 | -36.35 | 212 |
| 47 | EMA 20/50 cross · 1h | trend | 74.69 | -25.31 | 105 | 10.5 | -27.61 | -4.66 | -38.62 | 124 |
| 48 | Daily: Momentum burst | daily | 74.04 | -25.96 | 27 | 11.1 | -30.34 | -4.09 | -36.97 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.44 | -26.56 | 147 | 14.3 | -26.19 | -4.28 | -37.19 | 205 |
| 50 | ROC + volume · 1h | momentum | 72.98 | -27.02 | 390 | 28.7 | -30.00 | -5.56 | -38.32 | 375 |
| 51 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -36.47 | -5.65 | -36.61 | 457 |
| 52 | Bollinger reversion · 1h | reversion | 72.28 | -27.72 | 290 | 41.0 | -31.77 | -4.92 | -35.72 | 378 |
| 53 | Donchian 20/10 · 1h | breakout | 72.02 | -27.98 | 145 | 19.3 | -27.22 | -4.92 | -35.90 | 209 |
| 54 | OBV trend · 1h | momentum | 71.65 | -28.35 | 290 | 19.3 | -26.52 | -4.56 | -36.52 | 276 |
| 55 | Williams %R · 1h ⏸ | reversion | 67.95 | -32.05 | 372 | 43.8 | -41.91 | -6.88 | -42.09 | 528 |
| 56 | Z-score reversion · 1h | reversion | 67.93 | -32.07 | 199 | 38.2 | -27.28 | -3.79 | -29.17 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 67.15 | -32.84 | 259 | 10.0 | -35.43 | -7.26 | -41.97 | 330 |
| 58 | VWAP momentum · 1h | momentum | 66.17 | -33.83 | 894 | 22.4 | -51.48 | -10.50 | -51.91 | 1215 |
| 59 | Agent (ML meta-label) | meta | 66.10 | -33.90 | 1819 | 24.8 | -20.30 | -2.72 | -23.52 | 349 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -36.59 | -5.34 | -36.76 | 241 |
| 61 | Candlestick reversal · 1h | reversion | 62.78 | -37.22 | 469 | 28.4 | -43.88 | -8.08 | -44.02 | 590 |
| 62 | Three white soldiers | momentum | 58.62 | -41.38 | 537 | 14.5 | -49.70 | -22.55 | -49.70 | 664 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.68 | -99.00 | 5253 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.87 | -25.57 | -79.92 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -46.39 | -93.78 | 2533 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.28 | -31.67 | -89.44 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.17 | -41.18 | -91.20 | 2330 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.90 | -31.58 | -89.94 | 2202 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -53.81 | -97.90 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -56.79 | -96.32 | 3416 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.54 | -32.59 | -93.57 | 2323 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.17 | -34.86 | -83.19 | 1660 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.81 | -99.57 | 5993 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.27 | -43.95 | -92.27 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.37 | -36.88 | -95.39 | 3472 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -78.93 | -99.82 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.36 | -44.30 | -92.40 | 2268 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.29 | -25.47 | -75.37 | 1622 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -61.03 | -97.67 | 3520 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -63.87 | -98.88 | 4920 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.66 | -27.25 | -68.68 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.79 | -58.89 | -94.80 | 2784 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.06 | -39.31 | -85.11 | 1781 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.34 | -99.65 | 6351 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.97 | -32.50 | -90.00 | 2301 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.99 | -19.90 | -78.33 | 1765 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.76 | -36.80 | -90.77 | 2174 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.84 | -52.43 | -96.84 | 3856 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -58.34 | -89.28 | 2133 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.44 | -30.65 | -66.44 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.38 | -23.06 | -71.53 | 1255 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.12 | -18.96 | -79.44 | 1709 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.31 | -50.00 | -97.32 | 4306 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.91 | -99.93 | 8368 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T20:35 | MFI reversion · 1h | buy | LABU | 7.24 | — | entry |
| 2026-11-12T20:35 | MFI reversion · 1h | sell | SOXL | 6.16 | -0.09 | target is flat |
| 2026-11-12T20:35 | Opening range 30m | sell | SPY | 6.20 | -0.02 | stop-loss |
| 2026-11-12T20:35 | Opening range 30m | sell | COIN | 6.06 | -0.19 | stop-loss |
| 2026-11-12T20:35 | Opening range 15m | buy | ETHU | 2.67 | — | entry |
| 2026-11-12T20:35 | Opening range 15m | sell | COIN | 2.67 | -0.03 | stop-loss |
| 2026-11-12T20:30 | Agent (ML meta-label) | sell | QQQ | 4.41 | -0.01 | selected signal exited |
| 2026-11-12T20:30 | Connors RSI(2) · 1h | buy | AMZN | 20.26 | — | entry signal |
| 2026-11-12T20:30 | Volume breakout · 1h | sell | AAPL | 20.04 | -0.03 | exit signal |
| 2026-11-12T20:30 | ROC + volume · 1h | buy | UPRO | 3.88 | — | rebalance up |
| 2026-11-12T20:30 | ROC + volume · 1h | buy | TSLA | 3.72 | — | rebalance up |
| 2026-11-12T20:30 | ROC + volume · 1h | buy | SPY | 3.86 | — | rebalance up |
| 2026-11-12T20:30 | ROC + volume · 1h | buy | GOOGL | 3.78 | — | rebalance up |
| 2026-11-12T20:30 | ROC + volume · 1h | buy | AMZN | 10.43 | — | entry signal |
| 2026-11-12T20:30 | ROC + volume · 1h | buy | AAPL | 3.90 | — | rebalance up |
| 2026-11-12T20:30 | ROC + volume · 1h | sell | TQQQ | 6.59 | 0.03 | exit signal |
| 2026-11-12T20:30 | ROC + volume · 1h | sell | TECL | 6.59 | 0.03 | exit signal |
| 2026-11-12T20:30 | ROC + volume · 1h | sell | SOXL | 6.77 | 0.38 | exit signal |
| 2026-11-12T20:30 | ROC + volume · 1h | sell | QQQ | 6.57 | 0.01 | exit signal |
| 2026-11-12T20:30 | ROC + volume · 1h | sell | PLTR | 6.62 | 0.05 | exit signal |
| 2026-11-12T20:30 | VWAP momentum · 1h | buy | TSLA | 7.35 | — | entry signal |
| 2026-11-12T20:30 | VWAP momentum · 1h | buy | SQQQ | 7.35 | — | entry signal |
| 2026-11-12T20:30 | VWAP momentum · 1h | sell | UPRO | 6.60 | 0.03 | exit signal |
| 2026-11-12T20:30 | VWAP momentum · 1h | sell | TQQQ | 6.56 | -0.16 | exit signal |
| 2026-11-12T20:30 | VWAP momentum · 1h | sell | COIN | 5.99 | -0.06 | exit signal |
| 2026-11-12T20:30 | Heikin-Ashi · 1h | sell | GOOGL | 19.34 | -0.18 | exit signal |
| 2026-11-12T20:30 | Parabolic SAR · 1h | buy | TSLA | 8.25 | — | entry signal |
| 2026-11-12T20:30 | MACD zero-line · 1h | buy | UPRO | 8.19 | — | rebalance up |
| 2026-11-12T20:30 | MACD zero-line · 1h | buy | SOXL | 10.52 | — | rebalance up |
| 2026-11-12T20:30 | MACD zero-line · 1h | buy | AMD | 9.88 | — | rebalance up |
| 2026-11-12T20:30 | MACD zero-line · 1h | sell | TQQQ | 8.36 | -0.01 | exit signal |
| 2026-11-12T20:30 | MACD zero-line · 1h | sell | SPY | 8.39 | 0.02 | exit signal |
| 2026-11-12T20:30 | MACD zero-line · 1h | sell | QQQ | 7.60 | 0.23 | exit signal |
| 2026-11-12T20:30 | MACD zero-line · 1h | sell | PLTR | 8.35 | -0.02 | exit signal |
| 2026-11-12T20:30 | MACD cross · 1h | buy | UPRO | 5.11 | — | rebalance up |
| 2026-11-12T20:30 | MACD cross · 1h | buy | TSLA | 9.63 | — | entry signal |
| 2026-11-12T20:30 | MACD cross · 1h | buy | TECL | 6.07 | — | rebalance up |
| 2026-11-12T20:30 | MACD cross · 1h | buy | SQQQ | 9.63 | — | entry signal |
| 2026-11-12T20:30 | MACD cross · 1h | buy | AMD | 5.20 | — | rebalance up |
| 2026-11-12T20:30 | MACD cross · 1h | sell | TQQQ | 6.71 | 0.51 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 20:40:05.000137+00:00 -> 2026-11-12 20:50:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
