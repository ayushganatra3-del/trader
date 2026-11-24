# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T15:40:05.000130+00:00 · 71972 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.64 (-21.36%)

Closed trades 241, win rate 35.7%, fees £6.53, max drawdown -21.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 15.68 | -0.06 |

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

Today: 16803 decisions in 2496 calls, $0.2232 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T15:40 | 3 / 9 / 18 | cash |  |
| Breezy | 2026-11-24T15:40 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-24T15:40 | 3 / 24 / 3 | COIN 63% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.80 | 15.80 | 0 | — | 13.53 | 4.73 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.94 | 3.94 | 0 | — | 4.50 | 1.20 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.65 | -1.35 | 218 | 31.7 | 0.01 | 0.09 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.16 | -3.84 | 228 | 28.5 | -0.15 | 0.04 | -7.48 | 156 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.98 | -4.02 | 169 | 33.1 | -3.96 | -3.58 | -5.31 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.72 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 93.99 | -6.01 | 0 | — | -6.81 | -1.73 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.95 | -8.05 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.31 | -8.69 | 116 | 24.1 | -8.69 | -4.63 | -11.83 | 40 |
| 16 | Copy: Insider buying | copy | 90.99 | -9.01 | 58 | 39.7 | -7.71 | -1.45 | -14.79 | 70 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.25 | -10.75 | 0 | — | -10.90 | -2.33 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.30 | -2.99 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.01 | -13.99 | 165 | 46.1 | -11.36 | -2.03 | -20.49 | 152 |
| 21 | Daily: Bullish score | daily | 85.58 | -14.43 | 20 | 20.0 | -13.12 | -3.03 | -19.56 | 14 |
| 22 | Opening range 30m | breakout | 85.00 | -15.00 | 467 | 33.0 | -14.33 | -4.79 | -14.39 | 549 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -18.28 | -6.47 | -18.61 | 76 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.80 | -6.59 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 78.65 | -21.35 | 205 | 28.3 | -32.27 | -8.48 | -32.47 | 184 |
| 27 | Agent | meta | 78.64 | -21.36 | 241 | 35.7 | -25.17 | -5.66 | -25.49 | 196 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 29 | Volume breakout · 1h | breakout | 76.88 | -23.12 | 169 | 27.8 | -23.44 | -7.22 | -23.97 | 72 |
| 30 | Opening range 15m | breakout | 76.44 | -23.56 | 581 | 30.6 | -22.69 | -7.07 | -22.95 | 671 |
| 31 | Donchian 55/20 · 1h | breakout | 75.98 | -24.02 | 87 | 13.8 | -30.31 | -8.07 | -30.31 | 84 |
| 32 | Keltner breakout · 1h | breakout | 75.62 | -24.38 | 137 | 24.8 | -27.04 | -6.99 | -27.98 | 150 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.66 | -8.08 | -31.53 | 101 |
| 34 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.76 | -4.86 | -36.38 | 24 |
| 35 | ADX DI cross · 1h | trend | 69.35 | -30.65 | 259 | 19.3 | -40.25 | -7.50 | -40.69 | 281 |
| 36 | Hold BTC | benchmark | 69.07 | -30.93 | 3 | 0.0 | -29.16 | -5.23 | -36.10 | 1 |
| 37 | Supertrend · 1h | trend | 68.50 | -31.50 | 205 | 18.5 | -35.43 | -6.81 | -35.76 | 212 |
| 38 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -38.58 | -10.09 | -39.09 | 175 |
| 39 | Bollinger breakout · 1h | breakout | 67.92 | -32.08 | 208 | 22.1 | -33.98 | -9.03 | -35.23 | 213 |
| 40 | EMA 20/50 cross · 1h | trend | 67.84 | -32.16 | 124 | 9.7 | -36.30 | -10.04 | -37.44 | 115 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 67.41 | -32.59 | 3 | 0.0 | -26.19 | -3.14 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 66.66 | -33.34 | 323 | 19.8 | -39.51 | -10.07 | -40.78 | 231 |
| 43 | MACD zero-line · 1h | trend | 64.24 | -35.76 | 199 | 16.6 | -34.13 | -9.09 | -34.30 | 205 |
| 44 | RSI momentum · 1h | momentum | 64.16 | -35.84 | 200 | 15.0 | -41.59 | -9.68 | -42.28 | 196 |
| 45 | Heikin-Ashi · 1h | trend | 64.12 | -35.88 | 538 | 22.1 | -48.47 | -9.90 | -49.44 | 629 |
| 46 | Stochastic reversion · 1h | reversion | 63.84 | -36.16 | 399 | 40.6 | -34.24 | -3.70 | -42.79 | 433 |
| 47 | Max aggression: 5-day momentum | meta | 62.48 | -37.52 | 26 | 34.6 | -62.90 | -4.15 | -67.33 | 23 |
| 48 | ROC + volume · 1h | momentum | 61.70 | -38.30 | 453 | 27.2 | -43.56 | -8.63 | -44.16 | 341 |
| 49 | Donchian 20/10 · 1h | breakout | 61.25 | -38.75 | 181 | 17.7 | -41.03 | -8.79 | -42.83 | 193 |
| 50 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.77 | -5.11 | -35.63 | 182 |
| 51 | Max aggression: 1-day momentum | meta | 59.43 | -40.57 | 34 | 26.5 | -59.19 | -4.36 | -60.68 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 59.24 | -40.76 | 309 | 12.3 | -44.77 | -10.64 | -46.36 | 331 |
| 53 | MACD cross · 1h | trend | 57.63 | -42.38 | 475 | 21.1 | -52.71 | -10.59 | -53.55 | 508 |
| 54 | Agent (ML meta-label) | meta | 56.82 | -43.18 | 2054 | 25.0 | -19.29 | -2.27 | -29.30 | 335 |
| 55 | CCI reversion · 1h | reversion | 56.21 | -43.79 | 439 | 39.4 | -50.71 | -8.53 | -51.96 | 505 |
| 56 | Bollinger reversion · 1h | reversion | 55.65 | -44.34 | 391 | 37.6 | -40.05 | -4.85 | -45.42 | 430 |
| 57 | VWAP momentum · 1h | momentum | 53.10 | -46.90 | 1063 | 21.6 | -57.62 | -13.15 | -58.46 | 1188 |
| 58 | Williams %R · 1h | reversion | 51.00 | -49.00 | 509 | 37.7 | -54.99 | -9.01 | -56.27 | 592 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.53 | -8.62 | -53.02 | 681 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.17 | -49.99 | -99.17 | 5410 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.87 | -33.79 | -84.10 | 1436 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.57 | -50.06 | -94.60 | 2447 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.68 | -32.53 | -90.71 | 1919 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.89 | -42.40 | -91.89 | 2251 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.82 | -28.97 | -89.89 | 1967 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -49.57 | -98.20 | 3435 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.05 | -55.29 | -97.05 | 3393 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.29 | -38.28 | -93.30 | 2101 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.49 | -35.20 | -83.54 | 1564 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -57.60 | -99.68 | 6264 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.35 | -39.49 | -93.35 | 2502 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.43 | -36.86 | -94.45 | 3166 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.66 | -99.82 | 6131 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.31 | -44.88 | -93.33 | 2264 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.78 | -22.33 | -51.80 | 641 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.15 | -23.91 | -79.18 | 1616 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.45 | -97.83 | 3291 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -62.25 | -99.18 | 5137 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.27 | -27.45 | -71.27 | 1203 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.02 | -48.81 | -95.03 | 2672 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.70 | -6.57 | -48.78 | 280 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.66 | -37.62 | -85.67 | 1679 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.92 | -99.76 | 6538 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.51 | -31.15 | -91.51 | 2492 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.00 | -20.39 | -83.01 | 1952 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.82 | -31.41 | -91.83 | 2198 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -50.00 | -98.14 | 4058 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.41 | -48.59 | -90.41 | 2194 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.93 | -29.84 | -68.93 | 798 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.79 | -28.67 | -73.83 | 1170 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.07 | -19.30 | -84.14 | 1833 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.02 | -50.43 | -98.03 | 4413 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -103.46 | -99.94 | 8264 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -48.08 | -7.27 | -51.09 | 302 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T15:40 | Agent (ML meta-label) | buy | SQQQ | 7.84 | — | rebalance up |
| 2026-11-24T15:40 | Agent (ML meta-label) | sell | BITX | 11.31 | -0.05 | selected signal exited |
| 2026-11-24T15:35 | Agent (ML meta-label) | buy | SQQQ | 6.35 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T15:35 | Agent (ML meta-label) | sell | BITX | 2.86 | 0.02 | rebalance down |
| 2026-11-24T15:35 | Opening range 30m | buy | MSFT | 21.24 | — | entry signal |
| 2026-11-24T15:30 | Agent (rotation) | buy | SQQQ | 8.02 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T15:30 | Agent (ML meta-label) | buy | BITX | 14.20 | — | entry |
| 2026-11-24T15:30 | Agent (ML meta-label) | sell | SQQQ | 14.26 | 0.08 | selected signal exited |
| 2026-11-24T15:30 | Agent | buy | SQQQ | 15.74 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | UPRO | 4.55 | -0.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | TSLA | 3.25 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | TQQQ | 3.12 | -0.33 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | SPY | 3.18 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | QQQ | 3.16 | -0.12 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | PLTR | 3.18 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | MSTR | 3.07 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | META | 3.18 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | GOOGL | 3.17 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | ETH-USD | 3.14 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | DOGE-USD | 3.14 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | BTC-USD | 3.15 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | CCI reversion · 1h | sell | LABU | 2.94 | 0.25 | exit signal |
| 2026-11-24T15:30 | Williams %R · 1h | buy | SQQQ | 10.21 | — | entry signal |
| 2026-11-24T15:30 | Williams %R · 1h | sell | AAPL | 8.51 | -0.03 | exit signal |
| 2026-11-24T15:30 | Stochastic reversion · 1h | buy | ETH-USD | 4.05 | — | rebalance up |
| 2026-11-24T15:30 | Stochastic reversion · 1h | buy | AMD | 3.43 | — | rebalance up |
| 2026-11-24T15:30 | Stochastic reversion · 1h | sell | AAPL | 5.18 | 0.03 | exit signal |
| 2026-11-24T15:30 | VWAP reversion · 1h | sell | MSFT | 21.88 | 0.03 | target is flat |
| 2026-11-24T15:30 | Volume breakout · 1h | buy | LABU | 19.13 | — | entry signal |
| 2026-11-24T15:30 | Keltner breakout · 1h | buy | LABU | 18.77 | — | entry signal |
| 2026-11-24T15:30 | Bollinger breakout · 1h | buy | LABU | 16.90 | — | entry signal |
| 2026-11-24T15:30 | Donchian 20/10 · 1h | buy | LABU | 15.24 | — | entry signal |
| 2026-11-24T15:30 | RSI momentum · 1h | buy | LABU | 15.93 | — | entry signal |
| 2026-11-24T15:30 | ROC + volume · 1h | buy | LABU | 15.31 | — | entry signal |
| 2026-11-24T15:30 | ROC + volume · 1h | buy | IWM | 15.31 | — | entry signal |
| 2026-11-24T15:30 | ROC + volume · 1h | buy | AAPL | 15.31 | — | entry signal |
| 2026-11-24T15:30 | VWAP momentum · 1h | buy | LABU | 4.49 | — | rebalance up |
| 2026-11-24T15:30 | VWAP momentum · 1h | buy | BTC-USD | 4.47 | — | rebalance up |
| 2026-11-24T15:30 | VWAP momentum · 1h | buy | AAPL | 4.28 | — | rebalance up |
| 2026-11-24T15:30 | VWAP momentum · 1h | sell | TNA | 8.80 | -0.06 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 15:40:05.000130+00:00 -> 2026-11-24 15:50:05.000130+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
