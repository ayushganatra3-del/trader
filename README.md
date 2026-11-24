# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T19:40:05.000161+00:00 · 72172 ticks

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

Today: 34890 decisions in 3096 calls, $0.4345 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T19:40 | 2 / 7 / 21 | cash |  |
| Breezy | 2026-11-24T19:40 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-24T19:40 | 4 / 21 / 5 | COIN 53% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.52 | 15.52 | 0 | — | 13.58 | 4.60 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.29 | 4.29 | 0 | — | 4.75 | 1.28 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.12 | 0.05 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.22 | -3.78 | 229 | 28.4 | -1.19 | -0.33 | -7.61 | 160 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.06 | -3.51 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.71 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.19 | -5.80 | 0 | — | -6.39 | -1.63 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.94 | -6.07 | 20 | 10.0 | -5.34 | -8.21 | -5.57 | 20 |
| 14 | Copy: Insider buying | copy | 92.73 | -7.27 | 61 | 41.0 | -6.52 | -1.17 | -14.79 | 70 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.62 | -7.38 | 0 | — | -7.94 | -1.60 | -13.87 | 1 |
| 16 | Trend pullback · 1h | trend | 91.21 | -8.79 | 116 | 24.1 | -7.68 | -3.87 | -10.72 | 39 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.66 | -10.35 | 0 | — | -11.04 | -2.38 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.26 | -2.99 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.27 | -13.73 | 167 | 46.1 | -11.06 | -1.98 | -20.49 | 154 |
| 21 | Daily: Bullish score | daily | 85.48 | -14.52 | 20 | 20.0 | -13.50 | -3.06 | -19.56 | 14 |
| 22 | Opening range 30m | breakout | 85.30 | -14.70 | 469 | 32.8 | -14.12 | -4.73 | -14.70 | 550 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -18.35 | -6.77 | -18.74 | 71 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.50 | -6.44 | -14.66 | 66 |
| 26 | Parabolic SAR · 1h | trend | 78.83 | -21.17 | 206 | 28.2 | -32.11 | -8.44 | -32.65 | 184 |
| 27 | Agent | meta | 78.44 | -21.56 | 244 | 36.1 | -26.46 | -6.03 | -26.75 | 195 |
| 28 | Volume breakout · 1h | breakout | 78.31 | -21.69 | 169 | 27.8 | -22.06 | -6.68 | -23.97 | 72 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 76.90 | -23.10 | 138 | 24.6 | -26.64 | -6.91 | -28.45 | 153 |
| 31 | Opening range 15m | breakout | 76.58 | -23.42 | 585 | 30.4 | -22.96 | -7.15 | -23.41 | 676 |
| 32 | Donchian 55/20 · 1h | breakout | 76.30 | -23.70 | 87 | 13.8 | -29.53 | -7.84 | -29.93 | 84 |
| 33 | Ichimoku · 1h | trend | 74.73 | -25.27 | 113 | 15.9 | -29.56 | -7.58 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.58 | -29.42 | 260 | 19.2 | -38.43 | -7.31 | -39.72 | 279 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.65 | -4.86 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.18 | -30.82 | 208 | 22.1 | -31.64 | -8.32 | -34.14 | 211 |
| 37 | Hold BTC | benchmark | 69.00 | -31.00 | 3 | 0.0 | -29.50 | -5.24 | -36.10 | 1 |
| 38 | Supertrend · 1h | trend | 68.76 | -31.24 | 205 | 18.5 | -35.60 | -6.90 | -37.41 | 214 |
| 39 | Triple EMA stack · 1h | trend | 68.30 | -31.70 | 169 | 15.4 | -40.20 | -10.43 | -40.20 | 174 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 68.26 | -31.74 | 3 | 0.0 | -24.56 | -3.02 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.75 | -32.25 | 124 | 9.7 | -37.59 | -10.19 | -38.65 | 116 |
| 42 | OBV trend · 1h | momentum | 66.63 | -33.37 | 323 | 19.8 | -41.16 | -10.34 | -42.26 | 225 |
| 43 | RSI momentum · 1h | momentum | 65.53 | -34.47 | 200 | 15.0 | -40.88 | -9.45 | -42.51 | 199 |
| 44 | Heikin-Ashi · 1h | trend | 64.88 | -35.12 | 539 | 22.1 | -47.92 | -9.76 | -49.69 | 627 |
| 45 | MACD zero-line · 1h | trend | 64.41 | -35.59 | 199 | 16.6 | -33.57 | -9.18 | -34.11 | 200 |
| 46 | Max aggression: 1-day momentum | meta | 63.80 | -36.20 | 34 | 26.5 | -56.19 | -4.18 | -60.68 | 38 |
| 47 | Stochastic reversion · 1h | reversion | 63.41 | -36.59 | 400 | 40.5 | -36.46 | -4.04 | -43.64 | 435 |
| 48 | ROC + volume · 1h | momentum | 62.87 | -37.13 | 453 | 27.2 | -42.29 | -8.28 | -43.78 | 343 |
| 49 | Donchian 20/10 · 1h | breakout | 62.29 | -37.71 | 181 | 17.7 | -39.63 | -8.49 | -42.39 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 62.20 | -37.80 | 26 | 34.6 | -63.07 | -4.17 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.26 | -39.74 | 310 | 12.3 | -44.13 | -10.40 | -45.65 | 330 |
| 52 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.22 | -5.03 | -35.63 | 185 |
| 53 | MACD cross · 1h | trend | 58.06 | -41.94 | 477 | 21.0 | -52.60 | -10.66 | -53.97 | 503 |
| 54 | Agent (ML meta-label) | meta | 56.87 | -43.13 | 2066 | 25.3 | -22.04 | -2.78 | -31.58 | 336 |
| 55 | CCI reversion · 1h | reversion | 56.15 | -43.85 | 444 | 39.4 | -51.38 | -8.79 | -52.31 | 496 |
| 56 | Bollinger reversion · 1h | reversion | 55.70 | -44.30 | 392 | 37.5 | -39.26 | -4.72 | -45.42 | 424 |
| 57 | VWAP momentum · 1h | momentum | 53.70 | -46.30 | 1065 | 21.6 | -58.00 | -12.97 | -59.70 | 1177 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.94 | -8.92 | -54.20 | 680 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -54.84 | -8.94 | -56.25 | 596 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -49.67 | -99.14 | 5369 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.77 | -33.63 | -83.80 | 1417 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.51 | -50.78 | -94.51 | 2446 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.64 | -32.50 | -90.66 | 1902 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.75 | -42.38 | -91.76 | 2237 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.62 | -28.81 | -89.80 | 1962 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -49.71 | -98.18 | 3440 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.99 | -56.04 | -96.99 | 3356 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.09 | -37.23 | -93.14 | 2081 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.27 | -35.89 | -83.28 | 1543 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.41 | -99.68 | 6271 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.21 | -39.47 | -93.22 | 2501 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.34 | -36.73 | -94.34 | 3171 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.66 | -99.82 | 6111 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.18 | -44.92 | -93.20 | 2267 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.74 | -22.41 | -51.83 | 643 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.72 | -23.88 | -78.86 | 1616 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -59.73 | -97.79 | 3282 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -61.88 | -99.18 | 5134 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.36 | -27.69 | -71.39 | 1205 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.95 | -49.12 | -94.95 | 2679 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.69 | -6.57 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.29 | -36.93 | -85.53 | 1671 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.29 | -99.77 | 6531 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.56 | -31.52 | -91.72 | 2471 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.82 | -20.37 | -83.27 | 1957 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.83 | -31.70 | -91.94 | 2180 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -49.94 | -98.15 | 4052 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.30 | -48.03 | -90.32 | 2208 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.82 | -29.71 | -68.82 | 800 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.15 | -28.49 | -73.29 | 1162 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.03 | -19.29 | -84.32 | 1820 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.05 | -50.79 | -98.06 | 4413 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -106.07 | -99.94 | 8265 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.60 | -7.27 | -50.32 | 305 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T19:35 | Agent (ML meta-label) | buy | MSTR | 2.87 | — | rebalance up |
| 2026-11-24T19:35 | Agent (ML meta-label) | sell | COIN | 11.40 | 0.03 | selected signal exited |
| 2026-11-24T19:30 | Copy: Insider buying | buy | WWB | 10.29 | — | rebalance up |
| 2026-11-24T19:30 | Copy: Insider buying | sell | SCQCU | 11.37 | 0.26 | target is flat |
| 2026-11-24T19:30 | CCI reversion · 1h | buy | AMD | 3.52 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | UPRO | 3.58 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | TSLA | 3.60 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | TQQQ | 3.60 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | TECL | 3.60 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | SPY | 3.60 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | SOXL | 3.60 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | QQQ | 3.60 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | META | 3.60 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | GOOGL | 3.60 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | buy | AMD | 3.60 | — | entry signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | sell | TNA | 5.43 | 0.04 | rebalance down |
| 2026-11-24T19:30 | VWAP momentum · 1h | sell | PLTR | 5.37 | -0.00 | rebalance down |
| 2026-11-24T19:30 | VWAP momentum · 1h | sell | MSFT | 8.85 | -0.12 | exit signal |
| 2026-11-24T19:30 | VWAP momentum · 1h | sell | LABU | 5.60 | 0.70 | rebalance down |
| 2026-11-24T19:30 | VWAP momentum · 1h | sell | IWM | 5.39 | 0.01 | rebalance down |
| 2026-11-24T19:30 | VWAP momentum · 1h | sell | AAPL | 5.36 | 0.03 | rebalance down |
| 2026-11-24T19:30 | Heikin-Ashi · 1h | buy | TSLA | 10.85 | — | entry signal |
| 2026-11-24T19:30 | Heikin-Ashi · 1h | buy | TNA | 10.86 | — | entry signal |
| 2026-11-24T19:30 | Heikin-Ashi · 1h | buy | IWM | 10.86 | — | entry signal |
| 2026-11-24T19:30 | Heikin-Ashi · 1h | sell | PLTR | 5.24 | 0.04 | rebalance down |
| 2026-11-24T19:30 | Heikin-Ashi · 1h | sell | LABU | 6.73 | 0.60 | rebalance down |
| 2026-11-24T19:30 | Heikin-Ashi · 1h | sell | AAPL | 4.96 | -0.01 | rebalance down |
| 2026-11-24T19:30 | ADX DI cross · 1h | sell | MSFT | 3.70 | -0.02 | exit signal |
| 2026-11-24T19:30 | Triple EMA stack · 1h | buy | LABU | 17.11 | — | entry signal |
| 2026-11-24T19:30 | EMA 20/50 cross · 1h | buy | TSLA | 16.95 | — | entry signal |
| 2026-11-24T19:21 | Agent (ML meta-label) | buy | SQQQ | 2.85 | — | rebalance up |
| 2026-11-24T19:15 | Agent (ML meta-label) | buy | ETHU | 2.88 | — | rebalance up |
| 2026-11-24T19:15 | Agent (ML meta-label) | sell | QQQ | 11.34 | 0.00 | selected signal exited |
| 2026-11-24T19:15 | Copy: Insider buying | buy | PAM | 10.99 | — | entry |
| 2026-11-24T19:15 | Copy: Insider buying | sell | TEAM | 10.99 | 0.49 | target is flat |
| 2026-11-24T19:10 | Agent (ML meta-label) | buy | QQQ | 11.34 | — | entry |
| 2026-11-24T19:10 | Agent (ML meta-label) | sell | UPRO | 11.34 | 0.11 | selected signal exited |
| 2026-11-24T19:00 | CCI reversion · 1h | buy | XRP-USD | 3.74 | — | entry signal |
| 2026-11-24T19:00 | Williams %R · 1h | sell | SQQQ | 7.33 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T19:00 | Williams %R · 1h | sell | SOXL | 5.05 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 19:40:05.000161+00:00 -> 2026-11-24 19:50:05.000161+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
