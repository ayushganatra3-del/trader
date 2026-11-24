# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T16:40:05.000160+00:00 · 72021 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.95 (-21.05%)

Closed trades 242, win rate 36.0%, fees £6.54, max drawdown -21.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 15.85 | +0.07 |

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

Today: 21243 decisions in 2643 calls, $0.2752 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T16:40 | 2 / 6 / 22 | cash |  |
| Breezy | 2026-11-24T16:40 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-24T16:40 | 2 / 22 / 6 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.78 | 15.78 | 0 | — | 13.25 | 4.73 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.95 | 3.95 | 0 | — | 4.35 | 1.20 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.06 | -0.94 | 218 | 31.7 | 0.44 | 0.23 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.30 | -3.70 | 228 | 28.5 | 0.00 | 0.09 | -7.48 | 156 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.06 | -3.51 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.62 | -2.88 | -7.38 | 1 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 13 | Hold SPY | benchmark | 93.69 | -6.30 | 0 | — | -7.18 | -1.81 | -11.71 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.95 | -8.05 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.69 | -8.31 | 116 | 24.1 | -8.45 | -4.52 | -11.87 | 41 |
| 16 | Copy: Insider buying | copy | 91.44 | -8.55 | 58 | 39.7 | -8.08 | -1.54 | -14.79 | 70 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.17 | -10.83 | 0 | — | -11.10 | -2.38 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.96 | -2.99 | -20.94 | 1 |
| 20 | Daily: Bullish score | daily | 85.93 | -14.07 | 20 | 20.0 | -12.60 | -2.91 | -19.56 | 14 |
| 21 | VWAP reversion · 1h | reversion | 85.45 | -14.55 | 165 | 46.1 | -11.97 | -2.11 | -20.49 | 152 |
| 22 | Opening range 30m | breakout | 85.25 | -14.75 | 468 | 32.9 | -14.07 | -4.72 | -14.39 | 549 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -18.87 | -6.73 | -19.15 | 75 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.62 | -6.51 | -14.78 | 66 |
| 26 | Agent | meta | 78.95 | -21.05 | 242 | 36.0 | -25.56 | -5.81 | -26.37 | 193 |
| 27 | Parabolic SAR · 1h | trend | 78.34 | -21.66 | 206 | 28.2 | -32.54 | -8.53 | -32.65 | 184 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 29 | Volume breakout · 1h | breakout | 77.21 | -22.79 | 169 | 27.8 | -23.12 | -7.12 | -23.97 | 72 |
| 30 | Opening range 15m | breakout | 76.42 | -23.58 | 584 | 30.5 | -22.69 | -7.07 | -22.95 | 671 |
| 31 | Donchian 55/20 · 1h | breakout | 75.98 | -24.02 | 87 | 13.8 | -29.74 | -7.87 | -29.75 | 83 |
| 32 | Keltner breakout · 1h | breakout | 75.77 | -24.23 | 138 | 24.6 | -27.24 | -7.20 | -27.96 | 151 |
| 33 | Ichimoku · 1h | trend | 73.69 | -26.31 | 113 | 15.9 | -30.52 | -8.02 | -31.53 | 102 |
| 34 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.52 | -4.86 | -36.38 | 24 |
| 35 | ADX DI cross · 1h | trend | 69.53 | -30.48 | 259 | 19.3 | -39.26 | -7.45 | -39.85 | 278 |
| 36 | Hold BTC | benchmark | 68.64 | -31.36 | 3 | 0.0 | -29.74 | -5.30 | -36.10 | 1 |
| 37 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -39.33 | -10.40 | -39.33 | 175 |
| 38 | Bollinger breakout · 1h | breakout | 68.20 | -31.80 | 208 | 22.1 | -33.19 | -8.84 | -34.74 | 212 |
| 39 | EMA 20/50 cross · 1h | trend | 68.13 | -31.87 | 124 | 9.7 | -35.93 | -9.95 | -37.34 | 113 |
| 40 | Supertrend · 1h | trend | 68.03 | -31.98 | 205 | 18.5 | -37.13 | -7.17 | -38.13 | 215 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 67.21 | -32.79 | 3 | 0.0 | -25.92 | -3.17 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 66.91 | -33.09 | 323 | 19.8 | -38.76 | -9.82 | -40.26 | 230 |
| 43 | Heikin-Ashi · 1h | trend | 64.47 | -35.53 | 538 | 22.1 | -48.19 | -9.87 | -49.45 | 630 |
| 44 | RSI momentum · 1h | momentum | 64.26 | -35.74 | 200 | 15.0 | -41.35 | -9.57 | -42.13 | 195 |
| 45 | MACD zero-line · 1h | trend | 64.05 | -35.95 | 199 | 16.6 | -35.55 | -9.59 | -35.69 | 201 |
| 46 | Max aggression: 5-day momentum | meta | 63.52 | -36.48 | 26 | 34.6 | -62.29 | -4.07 | -67.33 | 23 |
| 47 | Stochastic reversion · 1h | reversion | 63.33 | -36.67 | 400 | 40.5 | -36.01 | -3.96 | -43.45 | 431 |
| 48 | ROC + volume · 1h | momentum | 61.75 | -38.25 | 453 | 27.2 | -43.59 | -8.60 | -44.23 | 341 |
| 49 | Donchian 20/10 · 1h | breakout | 61.51 | -38.49 | 181 | 17.7 | -40.42 | -8.69 | -42.47 | 192 |
| 50 | Max aggression: 1-day momentum | meta | 60.42 | -39.58 | 34 | 26.5 | -58.51 | -4.32 | -60.68 | 38 |
| 51 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.72 | -5.09 | -35.63 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 59.20 | -40.80 | 309 | 12.3 | -44.47 | -10.49 | -46.23 | 330 |
| 53 | MACD cross · 1h | trend | 57.46 | -42.54 | 477 | 21.0 | -52.68 | -10.56 | -53.49 | 504 |
| 54 | Agent (ML meta-label) | meta | 56.28 | -43.72 | 2059 | 25.1 | -21.43 | -2.76 | -30.66 | 323 |
| 55 | CCI reversion · 1h | reversion | 55.97 | -44.03 | 442 | 39.1 | -50.94 | -8.59 | -51.86 | 505 |
| 56 | Bollinger reversion · 1h | reversion | 55.34 | -44.66 | 392 | 37.5 | -40.69 | -4.95 | -45.42 | 428 |
| 57 | VWAP momentum · 1h | momentum | 53.27 | -46.73 | 1064 | 21.6 | -58.40 | -13.54 | -59.09 | 1172 |
| 58 | Williams %R · 1h | reversion | 50.98 | -49.02 | 509 | 37.7 | -55.25 | -9.05 | -56.51 | 591 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.21 | -8.68 | -53.50 | 668 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -49.80 | -99.16 | 5388 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.84 | -33.68 | -84.15 | 1435 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.52 | -50.01 | -94.57 | 2445 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.71 | -32.57 | -90.76 | 1911 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.77 | -42.34 | -91.82 | 2248 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.82 | -29.15 | -89.92 | 1964 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -49.72 | -98.20 | 3423 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.99 | -55.45 | -97.01 | 3382 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.27 | -38.21 | -93.29 | 2081 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.43 | -34.67 | -83.57 | 1561 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -57.29 | -99.68 | 6289 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.32 | -39.42 | -93.34 | 2497 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.35 | -36.66 | -94.37 | 3156 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.85 | -99.82 | 6131 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.31 | -44.89 | -93.31 | 2262 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.72 | -22.33 | -51.75 | 640 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.20 | -23.85 | -79.26 | 1618 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.65 | -97.83 | 3292 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -62.10 | -99.19 | 5136 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.29 | -27.45 | -71.29 | 1201 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.02 | -48.78 | -95.03 | 2669 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.62 | -6.50 | -48.58 | 279 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.53 | -37.32 | -85.66 | 1678 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.03 | -99.77 | 6528 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.65 | -31.18 | -91.66 | 2486 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.21 | -20.46 | -83.28 | 1962 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.01 | -31.96 | -92.01 | 2182 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.16 | -50.05 | -98.16 | 4057 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.42 | -48.57 | -90.42 | 2193 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.99 | -29.78 | -68.99 | 800 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.68 | -28.62 | -73.77 | 1168 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.27 | -19.42 | -84.32 | 1823 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.05 | -50.35 | -98.06 | 4415 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -103.83 | -99.94 | 8257 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -49.26 | -7.53 | -51.32 | 288 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T16:30 | Agent (ML meta-label) | buy | SQQQ | 8.06 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T16:30 | Agent (ML meta-label) | buy | COIN | 8.07 | — | entry |
| 2026-11-24T16:30 | Agent (ML meta-label) | buy | AMD | 8.07 | — | entry |
| 2026-11-24T16:30 | Agent (ML meta-label) | sell | UPRO | 3.26 | 0.01 | rebalance down |
| 2026-11-24T16:30 | Agent (ML meta-label) | sell | MSTR | 6.03 | -0.18 | rebalance down |
| 2026-11-24T16:30 | Agent (ML meta-label) | sell | ETHU | 6.05 | -0.29 | rebalance down |
| 2026-11-24T16:30 | Agent (ML meta-label) | sell | BITX | 3.24 | -0.01 | rebalance down |
| 2026-11-24T16:30 | CCI reversion · 1h | sell | AAPL | 2.67 | -0.01 | exit signal |
| 2026-11-24T16:30 | Keltner breakout · 1h | sell | TSLA | 18.36 | -0.56 | exit signal |
| 2026-11-24T16:30 | Heikin-Ashi · 1h | buy | SQQQ | 16.06 | — | entry signal |
| 2026-11-24T16:30 | Ichimoku · 1h | buy | LABU | 18.38 | — | entry signal |
| 2026-11-24T16:30 | Supertrend · 1h | buy | AAPL | 3.41 | — | entry signal |
| 2026-11-24T16:30 | MACD zero-line · 1h | buy | AAPL | 16.02 | — | entry signal |
| 2026-11-24T16:25 | Agent (ML meta-label) | buy | MSTR | 4.73 | — | rebalance up |
| 2026-11-24T16:25 | Agent (ML meta-label) | buy | ETHU | 4.74 | — | rebalance up |
| 2026-11-24T16:25 | Agent (ML meta-label) | sell | SQQQ | 2.93 | -0.04 | selected signal exited |
| 2026-11-24T16:25 | Agent (ML meta-label) | sell | AMD | 12.17 | -1.61 | selected signal exited |
| 2026-11-24T16:20 | Agent (ML meta-label) | buy | SQQQ | 2.97 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T16:15 | Agent (ML meta-label) | buy | UPRO | 11.27 | — | entry |
| 2026-11-24T16:15 | Agent (ML meta-label) | buy | BITX | 4.56 | — | rebalance up |
| 2026-11-24T16:15 | Agent (ML meta-label) | sell | SQQQ | 10.03 | 0.06 | selected signal exited |
| 2026-11-24T16:15 | Agent (ML meta-label) | sell | COIN | 7.64 | -0.06 | selected signal exited |
| 2026-11-24T16:15 | Stochastic reversion · 1h | sell | AMD | 7.79 | -0.79 | stop-loss |
| 2026-11-24T16:15 | MACD cross · 1h | sell | QQQ | 4.08 | -0.07 | stop-loss |
| 2026-11-24T16:12 | Agent (ML meta-label) | buy | SQQQ | 3.42 | — | rebalance up |
| 2026-11-24T16:12 | Agent (ML meta-label) | sell | BITX | 4.56 | -0.01 | rebalance down |
| 2026-11-24T16:10 | Agent | buy | SQQQ | 15.78 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T16:05 | Day trade: Stocks in Play ORB | sell | TNA | 23.52 | -0.71 | target is flat |
| 2026-11-24T16:05 | Agent | sell | SQQQ | 15.92 | 0.19 | selected signal exited |
| 2026-11-24T16:05 | Bollinger reversion · 1h | sell | AMD | 12.56 | -2.00 | stop-loss |
| 2026-11-24T16:05 | Opening range 15m | buy | MSFT | 3.82 | — | rebalance up |
| 2026-11-24T16:05 | Opening range 15m | sell | AMZN | 18.97 | -0.22 | stop-loss |
| 2026-11-24T16:05 | Opening range 15m | sell | AAPL | 19.08 | -0.12 | stop-loss |
| 2026-11-24T16:00 | Agent (ML meta-label) | buy | COIN | 7.71 | — | entry |
| 2026-11-24T16:00 | Agent (ML meta-label) | sell | MSTR | 4.60 | -0.17 | rebalance down |
| 2026-11-24T16:00 | Agent (ML meta-label) | sell | ETHU | 3.11 | -0.20 | rebalance down |
| 2026-11-24T16:00 | Stochastic reversion · 1h | buy | SOL-USD | 7.08 | — | entry signal |
| 2026-11-24T16:00 | VWAP momentum · 1h | sell | BTC-USD | 13.13 | -0.21 | exit signal |
| 2026-11-24T16:00 | Opening range 15m | buy | AMZN | 3.85 | — | rebalance up |
| 2026-11-24T16:00 | Opening range 15m | buy | AAPL | 3.84 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 16:40:05.000160+00:00 -> 2026-11-24 16:50:05.000160+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
