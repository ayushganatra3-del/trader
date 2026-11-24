# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T17:40:05.000130+00:00 · 72078 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.42 (-21.57%)

Closed trades 243, win rate 35.8%, fees £6.55, max drawdown -21.99%.

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

Today: 26403 decisions in 2814 calls, $0.3353 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T17:40 | 1 / 23 / 6 | cash |  |
| Breezy | 2026-11-24T17:40 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-24T17:40 | 4 / 26 / 0 | ETHU 66% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.87 | 15.87 | 0 | — | 13.63 | 4.75 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.37 | 4.37 | 0 | — | 4.65 | 1.30 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.12 | 0.05 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.25 | -3.75 | 229 | 28.4 | -0.06 | 0.07 | -7.48 | 156 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.06 | -3.51 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.50 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.43 | -5.57 | 0 | — | -6.40 | -1.62 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.28 | -5.49 | 19 |
| 14 | Copy: Insider buying | copy | 92.18 | -7.82 | 58 | 39.7 | -6.83 | -1.24 | -14.79 | 70 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.97 | -8.03 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 16 | Trend pullback · 1h | trend | 91.00 | -9.00 | 116 | 24.1 | -9.14 | -4.92 | -11.87 | 41 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.62 | -10.38 | 0 | — | -11.24 | -2.43 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.68 | -2.99 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.45 | -13.55 | 166 | 46.4 | -10.91 | -1.96 | -20.49 | 154 |
| 21 | Opening range 30m | breakout | 85.34 | -14.66 | 469 | 32.8 | -13.93 | -4.68 | -14.39 | 552 |
| 22 | Daily: Bullish score | daily | 85.29 | -14.71 | 20 | 20.0 | -13.23 | -3.12 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -18.54 | -6.57 | -18.71 | 73 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.62 | -6.51 | -14.78 | 66 |
| 26 | Parabolic SAR · 1h | trend | 79.00 | -21.00 | 206 | 28.2 | -31.98 | -8.41 | -32.65 | 184 |
| 27 | Agent | meta | 78.42 | -21.57 | 243 | 35.8 | -26.29 | -5.98 | -26.47 | 196 |
| 28 | Volume breakout · 1h | breakout | 77.94 | -22.06 | 169 | 27.8 | -22.42 | -6.85 | -23.97 | 72 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 30 | Opening range 15m | breakout | 76.68 | -23.32 | 585 | 30.4 | -22.54 | -7.03 | -22.98 | 679 |
| 31 | Keltner breakout · 1h | breakout | 76.66 | -23.34 | 138 | 24.6 | -26.48 | -6.94 | -28.07 | 151 |
| 32 | Donchian 55/20 · 1h | breakout | 75.95 | -24.05 | 87 | 13.8 | -29.82 | -7.89 | -29.83 | 84 |
| 33 | Ichimoku · 1h | trend | 74.38 | -25.62 | 113 | 15.9 | -29.88 | -7.74 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.43 | -29.57 | 259 | 19.3 | -38.55 | -7.33 | -39.85 | 279 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.29 | -4.86 | -36.38 | 24 |
| 36 | Hold BTC | benchmark | 69.32 | -30.68 | 3 | 0.0 | -29.03 | -5.19 | -36.10 | 1 |
| 37 | Supertrend · 1h | trend | 69.03 | -30.97 | 205 | 18.5 | -35.30 | -6.84 | -37.41 | 215 |
| 38 | Bollinger breakout · 1h | breakout | 68.85 | -31.15 | 208 | 22.1 | -32.15 | -8.52 | -34.33 | 211 |
| 39 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -39.90 | -10.41 | -39.90 | 175 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 68.22 | -31.78 | 3 | 0.0 | -24.71 | -3.03 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.61 | -32.38 | 124 | 9.7 | -36.48 | -10.11 | -37.41 | 114 |
| 42 | OBV trend · 1h | momentum | 66.46 | -33.54 | 323 | 19.8 | -39.48 | -10.15 | -40.35 | 230 |
| 43 | RSI momentum · 1h | momentum | 65.35 | -34.65 | 200 | 15.0 | -40.46 | -9.35 | -42.12 | 197 |
| 44 | Heikin-Ashi · 1h | trend | 64.75 | -35.25 | 538 | 22.1 | -48.09 | -9.88 | -49.45 | 631 |
| 45 | MACD zero-line · 1h | trend | 64.45 | -35.55 | 199 | 16.6 | -35.27 | -9.76 | -35.83 | 200 |
| 46 | Stochastic reversion · 1h | reversion | 63.70 | -36.30 | 400 | 40.5 | -35.59 | -3.91 | -43.46 | 435 |
| 47 | ROC + volume · 1h | momentum | 62.80 | -37.20 | 453 | 27.2 | -42.65 | -8.32 | -44.23 | 343 |
| 48 | Max aggression: 1-day momentum | meta | 62.66 | -37.34 | 34 | 26.5 | -56.98 | -4.24 | -60.68 | 38 |
| 49 | Donchian 20/10 · 1h | breakout | 62.09 | -37.91 | 181 | 17.7 | -39.88 | -8.56 | -42.47 | 192 |
| 50 | Max aggression: 5-day momentum | meta | 61.65 | -38.35 | 26 | 34.6 | -63.40 | -4.21 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.18 | -39.82 | 310 | 12.3 | -43.59 | -10.13 | -46.17 | 330 |
| 52 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.12 | -5.02 | -35.63 | 184 |
| 53 | MACD cross · 1h | trend | 58.10 | -41.90 | 477 | 21.0 | -52.43 | -10.61 | -53.91 | 501 |
| 54 | Agent (ML meta-label) | meta | 57.11 | -42.89 | 2061 | 25.1 | -19.71 | -2.37 | -30.30 | 330 |
| 55 | CCI reversion · 1h | reversion | 56.41 | -43.59 | 442 | 39.1 | -51.12 | -8.74 | -52.66 | 496 |
| 56 | Bollinger reversion · 1h | reversion | 55.87 | -44.13 | 392 | 37.5 | -39.05 | -4.70 | -45.42 | 423 |
| 57 | VWAP momentum · 1h | momentum | 53.85 | -46.15 | 1064 | 21.6 | -58.29 | -13.26 | -59.52 | 1177 |
| 58 | Williams %R · 1h | reversion | 51.00 | -49.00 | 509 | 37.7 | -54.89 | -8.97 | -56.27 | 592 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.50 | -8.93 | -54.09 | 676 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -49.77 | -99.16 | 5406 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.81 | -33.80 | -83.99 | 1427 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.52 | -50.04 | -94.56 | 2443 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.69 | -32.56 | -90.74 | 1919 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.80 | -42.30 | -91.85 | 2256 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.70 | -28.83 | -89.91 | 1964 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -49.49 | -98.20 | 3439 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.97 | -55.50 | -97.00 | 3373 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.17 | -37.38 | -93.24 | 2079 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.26 | -35.59 | -83.32 | 1561 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.61 | -99.68 | 6269 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.28 | -39.31 | -93.33 | 2509 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.34 | -36.63 | -94.35 | 3154 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.29 | -99.82 | 6141 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.21 | -44.62 | -93.27 | 2268 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.72 | -22.33 | -51.75 | 640 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.07 | -23.85 | -79.20 | 1622 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -59.41 | -97.80 | 3285 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -62.46 | -99.19 | 5135 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.24 | -27.44 | -71.28 | 1210 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.96 | -48.13 | -95.02 | 2687 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -45.90 | -6.41 | -48.58 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.47 | -37.02 | -85.68 | 1680 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.97 | -99.77 | 6525 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.48 | -31.19 | -91.65 | 2478 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.75 | -20.25 | -83.16 | 1942 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.81 | -31.84 | -91.94 | 2194 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -50.06 | -98.16 | 4056 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.35 | -48.58 | -90.40 | 2209 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -69.00 | -29.69 | -69.00 | 803 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.13 | -28.47 | -73.29 | 1166 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.00 | -19.26 | -84.33 | 1821 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.03 | -50.43 | -98.06 | 4409 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -103.59 | -99.94 | 8269 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -45.38 | -6.65 | -50.49 | 291 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T17:35 | Agent | sell | SQQQ | 15.32 | -0.45 | selected signal exited |
| 2026-11-24T17:35 | Opening range 30m | buy | TNA | 8.28 | — | rebalance up |
| 2026-11-24T17:35 | Opening range 30m | buy | MSFT | 4.29 | — | rebalance up |
| 2026-11-24T17:35 | Opening range 30m | buy | IWM | 4.28 | — | rebalance up |
| 2026-11-24T17:35 | Opening range 30m | sell | SQQQ | 20.83 | -0.44 | exit signal |
| 2026-11-24T17:30 | CCI reversion · 1h | buy | SOXL | 4.33 | — | entry signal |
| 2026-11-24T17:30 | Williams %R · 1h | buy | SOXL | 2.24 | — | entry signal |
| 2026-11-24T17:30 | Williams %R · 1h | buy | COIN | 7.29 | — | entry signal |
| 2026-11-24T17:30 | Williams %R · 1h | sell | SQQQ | 2.76 | -0.04 | rebalance down |
| 2026-11-24T17:30 | Stochastic reversion · 1h | buy | COIN | 4.12 | — | entry signal |
| 2026-11-24T17:30 | Stochastic reversion · 1h | buy | AMD | 5.78 | — | entry signal |
| 2026-11-24T17:30 | VWAP reversion · 1h | sell | ETHU | 20.06 | 0.39 | exit signal |
| 2026-11-24T17:30 | Bollinger reversion · 1h | buy | AMD | 13.56 | — | entry signal |
| 2026-11-24T17:30 | Donchian 55/20 · 1h | buy | LABU | 19.00 | — | entry signal |
| 2026-11-24T17:30 | ROC + volume · 1h | buy | SPY | 10.46 | — | entry signal |
| 2026-11-24T17:30 | ROC + volume · 1h | buy | NVDA | 10.47 | — | entry signal |
| 2026-11-24T17:30 | ROC + volume · 1h | sell | TSLA | 4.72 | -0.07 | rebalance down |
| 2026-11-24T17:30 | ROC + volume · 1h | sell | LABU | 5.99 | 0.42 | rebalance down |
| 2026-11-24T17:30 | ROC + volume · 1h | sell | IWM | 4.97 | 0.04 | rebalance down |
| 2026-11-24T17:30 | ROC + volume · 1h | sell | AAPL | 4.90 | 0.02 | rebalance down |
| 2026-11-24T17:30 | VWAP momentum · 1h | buy | TNA | 8.97 | — | entry signal |
| 2026-11-24T17:30 | VWAP momentum · 1h | buy | PLTR | 8.97 | — | entry signal |
| 2026-11-24T17:30 | VWAP momentum · 1h | buy | MSFT | 8.97 | — | entry signal |
| 2026-11-24T17:30 | VWAP momentum · 1h | buy | IWM | 8.97 | — | entry signal |
| 2026-11-24T17:30 | VWAP momentum · 1h | sell | LABU | 5.24 | 0.54 | rebalance down |
| 2026-11-24T17:30 | VWAP momentum · 1h | sell | AAPL | 4.30 | 0.03 | rebalance down |
| 2026-11-24T17:30 | Heikin-Ashi · 1h | buy | AAPL | 15.84 | — | entry signal |
| 2026-11-24T17:30 | EMA 9/21 cross · 1h | buy | IWM | 15.03 | — | entry signal |
| 2026-11-24T17:30 | EMA 9/21 cross · 1h | sell | GOOGL | 14.72 | -0.06 | exit signal |
| 2026-11-24T17:30 | Opening range 15m | buy | AAPL | 10.89 | — | entry |
| 2026-11-24T17:30 | Opening range 15m | sell | SQQQ | 10.89 | -0.17 | exit signal |
| 2026-11-24T17:15 | Opening range 15m | buy | UPRO | 10.20 | — | entry signal |
| 2026-11-24T17:15 | Opening range 15m | buy | SPY | 10.94 | — | entry signal |
| 2026-11-24T17:15 | Opening range 15m | sell | SQQQ | 7.94 | -0.09 | rebalance down |
| 2026-11-24T17:15 | Opening range 15m | sell | MSFT | 4.39 | 0.05 | rebalance down |
| 2026-11-24T17:15 | Opening range 15m | sell | LABU | 4.46 | 0.09 | rebalance down |
| 2026-11-24T17:15 | Opening range 15m | sell | IWM | 4.35 | -0.00 | rebalance down |
| 2026-11-24T17:10 | Agent (rotation) | sell | SQQQ | 7.94 | -0.08 | selected signal exited |
| 2026-11-24T17:10 | Opening range 30m | buy | TNA | 13.00 | — | entry signal |
| 2026-11-24T17:10 | Opening range 30m | buy | IWM | 17.04 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 17:40:05.000130+00:00 -> 2026-11-24 17:50:05.000130+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
