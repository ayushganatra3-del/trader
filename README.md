# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T19:10:05.000118+00:00 · 72155 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.44 (-21.56%)

Closed trades 244, win rate 36.1%, fees £6.57, max drawdown -22.02%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-24 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, BH 12%, FUN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-23)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.62 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.4, AAPL 4.1, TSLA 3.2, AMZN 1.1, GOOGL 0.8, META 0.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 33360 decisions in 3045 calls, $0.4166 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T19:10 | 3 / 22 / 6 | cash |  |
| Breezy | 2026-11-24T19:10 | 0 / 25 / 6 | cash |  |
| Boozy | 2026-11-24T19:10 | 2 / 27 / 2 | COIN 54% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |
| Opening range 30m | SQQQ | 1.57 | +20.80% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 28.60 | 4.33 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.38 | 15.38 | 0 | — | 13.61 | 4.64 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.08 | 4.08 | 0 | — | 4.44 | 1.25 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.12 | 0.05 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.16 | -3.84 | 229 | 28.4 | -1.25 | -0.35 | -7.61 | 160 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.06 | -3.51 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.74 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.19 | -5.81 | 0 | — | -6.18 | -1.57 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 94.05 | -5.95 | 20 | 10.0 | -5.21 | -7.92 | -5.57 | 20 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.57 | -7.43 | 0 | — | -7.94 | -1.60 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 92.28 | -7.72 | 59 | 39.0 | -6.93 | -1.26 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.12 | -8.88 | 116 | 24.1 | -7.76 | -3.91 | -10.72 | 39 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.73 | -10.27 | 0 | — | -10.91 | -2.35 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.32 | -2.99 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.31 | -13.70 | 167 | 46.1 | -11.00 | -1.97 | -20.49 | 154 |
| 21 | Opening range 30m | breakout | 85.50 | -14.50 | 469 | 32.8 | -13.61 | -4.58 | -14.39 | 552 |
| 22 | Daily: Bullish score | daily | 85.40 | -14.61 | 20 | 20.0 | -13.43 | -3.08 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -18.62 | -6.92 | -18.90 | 73 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.62 | -6.51 | -14.78 | 66 |
| 26 | Parabolic SAR · 1h | trend | 78.89 | -21.11 | 206 | 28.2 | -32.03 | -8.42 | -32.65 | 184 |
| 27 | Agent | meta | 78.44 | -21.56 | 244 | 36.1 | -26.17 | -5.95 | -26.47 | 195 |
| 28 | Volume breakout · 1h | breakout | 78.42 | -21.58 | 169 | 27.8 | -21.96 | -6.63 | -23.97 | 72 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.40 | -4.28 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 77.10 | -22.90 | 138 | 24.6 | -26.11 | -6.75 | -28.09 | 152 |
| 31 | Opening range 15m | breakout | 76.69 | -23.31 | 585 | 30.4 | -22.55 | -7.03 | -22.98 | 679 |
| 32 | Donchian 55/20 · 1h | breakout | 76.39 | -23.61 | 87 | 13.8 | -29.37 | -7.77 | -29.86 | 84 |
| 33 | Ichimoku · 1h | trend | 74.82 | -25.18 | 113 | 15.9 | -29.47 | -7.53 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.68 | -29.32 | 259 | 19.3 | -38.55 | -7.35 | -40.00 | 282 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.51 | -4.86 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.27 | -30.73 | 208 | 22.1 | -31.53 | -8.26 | -34.11 | 211 |
| 37 | Hold BTC | benchmark | 69.14 | -30.86 | 3 | 0.0 | -29.27 | -5.21 | -36.10 | 1 |
| 38 | Supertrend · 1h | trend | 68.86 | -31.14 | 205 | 18.5 | -35.27 | -6.81 | -37.23 | 214 |
| 39 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -39.92 | -10.36 | -39.92 | 174 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 68.23 | -31.77 | 3 | 0.0 | -24.60 | -3.02 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.82 | -32.18 | 124 | 9.7 | -37.57 | -10.14 | -38.71 | 114 |
| 42 | OBV trend · 1h | momentum | 66.65 | -33.35 | 323 | 19.8 | -38.81 | -9.91 | -39.99 | 227 |
| 43 | RSI momentum · 1h | momentum | 65.70 | -34.30 | 200 | 15.0 | -40.57 | -9.37 | -42.37 | 195 |
| 44 | Heikin-Ashi · 1h | trend | 65.08 | -34.92 | 539 | 22.1 | -47.71 | -9.72 | -49.67 | 629 |
| 45 | MACD zero-line · 1h | trend | 64.38 | -35.62 | 199 | 16.6 | -33.82 | -9.23 | -34.34 | 201 |
| 46 | Max aggression: 1-day momentum | meta | 64.11 | -35.88 | 34 | 26.5 | -55.95 | -4.17 | -60.68 | 38 |
| 47 | Stochastic reversion · 1h | reversion | 63.45 | -36.55 | 400 | 40.5 | -36.34 | -4.02 | -43.59 | 435 |
| 48 | ROC + volume · 1h | momentum | 62.93 | -37.07 | 453 | 27.2 | -42.20 | -8.25 | -43.85 | 342 |
| 49 | Donchian 20/10 · 1h | breakout | 62.43 | -37.57 | 181 | 17.7 | -39.48 | -8.45 | -42.39 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 61.96 | -38.04 | 26 | 34.6 | -63.19 | -4.19 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.42 | -39.58 | 310 | 12.3 | -44.01 | -10.31 | -45.71 | 330 |
| 52 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.20 | -5.03 | -35.63 | 184 |
| 53 | MACD cross · 1h | trend | 58.12 | -41.88 | 477 | 21.0 | -52.49 | -10.63 | -53.95 | 502 |
| 54 | Agent (ML meta-label) | meta | 56.85 | -43.15 | 2064 | 25.2 | -18.65 | -2.32 | -29.13 | 348 |
| 55 | CCI reversion · 1h | reversion | 56.21 | -43.79 | 444 | 39.4 | -51.35 | -8.80 | -52.37 | 495 |
| 56 | Bollinger reversion · 1h | reversion | 55.72 | -44.28 | 392 | 37.5 | -39.20 | -4.72 | -45.42 | 424 |
| 57 | VWAP momentum · 1h | momentum | 53.93 | -46.07 | 1064 | 21.6 | -57.52 | -12.89 | -59.44 | 1172 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.60 | -8.91 | -53.92 | 687 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -54.76 | -8.92 | -56.25 | 595 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -49.75 | -99.15 | 5372 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.85 | -33.84 | -83.90 | 1425 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.52 | -50.54 | -94.52 | 2448 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.70 | -32.56 | -90.73 | 1917 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.76 | -42.34 | -91.79 | 2240 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.65 | -28.79 | -89.86 | 1963 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -49.65 | -98.19 | 3437 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -55.46 | -96.96 | 3354 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.24 | -37.90 | -93.31 | 2096 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.27 | -35.68 | -83.30 | 1546 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.46 | -99.68 | 6272 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.21 | -39.40 | -93.25 | 2502 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.35 | -36.76 | -94.35 | 3165 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.21 | -99.82 | 6112 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.18 | -44.89 | -93.20 | 2268 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.60 | -22.25 | -51.76 | 640 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.81 | -23.88 | -78.93 | 1615 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -58.84 | -97.79 | 3271 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -61.95 | -99.18 | 5120 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.39 | -27.62 | -71.39 | 1204 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.92 | -48.70 | -94.95 | 2678 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.62 | -6.56 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.33 | -36.84 | -85.59 | 1674 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.82 | -99.77 | 6534 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.58 | -31.53 | -91.73 | 2471 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.84 | -20.33 | -83.23 | 1950 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.83 | -31.91 | -91.95 | 2182 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -49.91 | -98.15 | 4051 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.33 | -48.15 | -90.37 | 2210 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.92 | -29.52 | -68.92 | 799 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.06 | -28.40 | -73.29 | 1162 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.06 | -19.31 | -84.32 | 1819 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.04 | -50.54 | -98.06 | 4419 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -105.61 | -99.94 | 8261 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.76 | -6.96 | -51.27 | 302 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T19:10 | Agent (ML meta-label) | buy | QQQ | 11.34 | — | entry |
| 2026-11-24T19:10 | Agent (ML meta-label) | sell | UPRO | 11.34 | 0.11 | selected signal exited |
| 2026-11-24T19:00 | CCI reversion · 1h | buy | XRP-USD | 3.74 | — | entry signal |
| 2026-11-24T19:00 | Williams %R · 1h | sell | SQQQ | 7.33 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T19:00 | Williams %R · 1h | sell | SOXL | 5.05 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T19:00 | Williams %R · 1h | sell | SOL-USD | 5.04 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T19:00 | Williams %R · 1h | sell | MSFT | 5.04 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T19:00 | Williams %R · 1h | sell | ETH-USD | 5.06 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T19:00 | Williams %R · 1h | sell | DOGE-USD | 5.05 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T19:00 | Williams %R · 1h | sell | COIN | 7.24 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T19:00 | Williams %R · 1h | sell | BTC-USD | 5.06 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T19:00 | Williams %R · 1h | sell | AMZN | 5.06 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T18:55 | Agent | sell | SQQQ | 15.70 | 0.01 | selected signal exited |
| 2026-11-24T18:30 | CCI reversion · 1h | buy | MSTR | 4.03 | — | entry signal |
| 2026-11-24T18:30 | CCI reversion · 1h | buy | COIN | 4.03 | — | entry signal |
| 2026-11-24T18:30 | CCI reversion · 1h | sell | TNA | 2.74 | 0.06 | exit signal |
| 2026-11-24T18:30 | CCI reversion · 1h | sell | IWM | 2.69 | 0.01 | exit signal |
| 2026-11-24T18:30 | VWAP reversion · 1h | sell | BITX | 20.88 | -2.40 | exit signal |
| 2026-11-24T18:30 | Three white soldiers · 1h | buy | LABU | 23.47 | — | entry signal |
| 2026-11-24T18:30 | Donchian 20/10 · 1h | buy | TNA | 15.59 | — | entry signal |
| 2026-11-24T18:30 | Donchian 20/10 · 1h | buy | IWM | 15.59 | — | entry signal |
| 2026-11-24T18:30 | OBV trend · 1h | buy | LABU | 16.62 | — | entry signal |
| 2026-11-24T18:30 | Heikin-Ashi · 1h | sell | SQQQ | 15.65 | -0.41 | exit signal |
| 2026-11-24T18:30 | ADX DI cross · 1h | buy | MSFT | 3.72 | — | entry |
| 2026-11-24T18:30 | ADX DI cross · 1h | sell | LABU | 3.72 | 0.28 | rebalance down |
| 2026-11-24T18:30 | EMA 20/50 cross · 1h | buy | LABU | 16.91 | — | entry signal |
| 2026-11-24T18:30 | EMA 9/21 cross · 1h | buy | TNA | 2.63 | — | entry signal |
| 2026-11-24T18:25 | Agent (ML meta-label) | buy | UPRO | 3.20 | — | rebalance up |
| 2026-11-24T18:25 | Agent (ML meta-label) | buy | SQQQ | 3.54 | — | rebalance up |
| 2026-11-24T18:25 | Agent (ML meta-label) | buy | MSTR | 3.31 | — | rebalance up |
| 2026-11-24T18:25 | Agent (ML meta-label) | buy | ETHU | 3.23 | — | rebalance up |
| 2026-11-24T18:25 | Agent (ML meta-label) | buy | COIN | 3.30 | — | rebalance up |
| 2026-11-24T18:25 | Agent (ML meta-label) | sell | BITX | 8.22 | 0.16 | selected signal exited |
| 2026-11-24T18:16 | Copy: Insider buying | buy | BH | 10.61 | — | entry |
| 2026-11-24T18:16 | Copy: Insider buying | sell | STWD | 10.61 | -0.23 | target is flat |
| 2026-11-24T18:00 | CCI reversion · 1h | buy | DOGE-USD | 4.03 | — | entry signal |
| 2026-11-24T18:00 | Williams %R · 1h | buy | SOXL | 2.83 | — | rebalance up |
| 2026-11-24T18:00 | Williams %R · 1h | buy | SOL-USD | 5.10 | — | entry signal |
| 2026-11-24T18:00 | Williams %R · 1h | buy | DOGE-USD | 5.10 | — | entry signal |
| 2026-11-24T18:00 | Williams %R · 1h | sell | MSFT | 3.50 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 19:10:05.000118+00:00 -> 2026-11-24 19:20:05.000118+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
