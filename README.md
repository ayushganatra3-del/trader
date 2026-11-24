# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T20:10:05.000143+00:00 · 72200 ticks

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

Today: 37428 decisions in 3180 calls, $0.4643 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T20:10 | 3 / 18 / 8 | cash |  |
| Breezy | 2026-11-24T20:10 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-11-24T20:10 | 5 / 20 / 4 | BITX 56% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.35 | 15.35 | 0 | — | 13.46 | 4.58 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.05 | 4.05 | 0 | — | 4.57 | 1.27 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.12 | 0.05 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.15 | -3.85 | 229 | 28.4 | -2.06 | -0.63 | -7.73 | 159 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.72 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.39 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 93.98 | -6.02 | 0 | — | -6.59 | -1.68 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.70 | -6.30 | 20 | 10.0 | -4.95 | -8.14 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.62 | -7.38 | 0 | — | -7.94 | -1.60 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 92.34 | -7.66 | 61 | 41.0 | -6.90 | -1.26 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.42 | -8.58 | 116 | 24.1 | -7.61 | -3.85 | -10.85 | 40 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.57 | -7.30 | -10.06 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.54 | -10.46 | 0 | — | -11.43 | -2.47 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.48 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.25 | -13.75 | 167 | 46.1 | -11.24 | -2.05 | -20.49 | 155 |
| 21 | Daily: Bullish score | daily | 85.68 | -14.32 | 20 | 20.0 | -12.81 | -2.82 | -19.56 | 14 |
| 22 | Opening range 30m | breakout | 84.93 | -15.07 | 469 | 32.8 | -13.25 | -4.44 | -13.73 | 543 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.17 | -7.39 | -21.55 | 75 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.53 | -6.46 | -14.68 | 65 |
| 26 | Parabolic SAR · 1h | trend | 78.56 | -21.44 | 206 | 28.2 | -32.35 | -8.49 | -32.65 | 184 |
| 27 | Agent | meta | 78.44 | -21.56 | 244 | 36.1 | -26.25 | -5.97 | -26.53 | 196 |
| 28 | Volume breakout · 1h | breakout | 78.11 | -21.89 | 169 | 27.8 | -22.56 | -6.88 | -24.10 | 73 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 76.60 | -23.40 | 138 | 24.6 | -25.70 | -6.70 | -27.25 | 150 |
| 31 | Opening range 15m | breakout | 76.26 | -23.73 | 585 | 30.4 | -22.32 | -6.89 | -22.58 | 670 |
| 32 | Donchian 55/20 · 1h | breakout | 76.11 | -23.89 | 87 | 13.8 | -29.46 | -7.91 | -29.68 | 82 |
| 33 | Ichimoku · 1h | trend | 74.53 | -25.47 | 113 | 15.9 | -29.74 | -7.67 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.36 | -29.64 | 260 | 19.2 | -37.49 | -7.13 | -38.61 | 292 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.80 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.00 | -31.00 | 208 | 22.1 | -31.56 | -8.30 | -33.57 | 209 |
| 37 | Hold BTC | benchmark | 68.89 | -31.11 | 3 | 0.0 | -29.57 | -5.26 | -36.10 | 1 |
| 38 | Supertrend · 1h | trend | 68.50 | -31.50 | 205 | 18.5 | -37.43 | -7.40 | -38.92 | 210 |
| 39 | Triple EMA stack · 1h | trend | 68.13 | -31.87 | 169 | 15.4 | -39.47 | -10.19 | -39.54 | 172 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 67.79 | -32.20 | 3 | 0.0 | -25.98 | -3.25 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.65 | -32.35 | 124 | 9.7 | -38.11 | -10.23 | -39.04 | 111 |
| 42 | OBV trend · 1h | momentum | 66.60 | -33.40 | 323 | 19.8 | -39.83 | -10.04 | -40.94 | 229 |
| 43 | RSI momentum · 1h | momentum | 65.18 | -34.82 | 200 | 15.0 | -41.04 | -9.53 | -42.36 | 197 |
| 44 | Heikin-Ashi · 1h | trend | 64.52 | -35.48 | 539 | 22.1 | -48.21 | -9.81 | -49.69 | 627 |
| 45 | MACD zero-line · 1h | trend | 64.28 | -35.72 | 199 | 16.6 | -34.33 | -9.33 | -34.73 | 197 |
| 46 | Stochastic reversion · 1h | reversion | 63.31 | -36.69 | 400 | 40.5 | -35.28 | -3.83 | -42.69 | 432 |
| 47 | Max aggression: 1-day momentum | meta | 63.17 | -36.83 | 34 | 26.5 | -56.62 | -4.21 | -60.68 | 38 |
| 48 | Max aggression: 5-day momentum | meta | 62.78 | -37.22 | 26 | 34.6 | -62.72 | -4.13 | -67.33 | 23 |
| 49 | ROC + volume · 1h | momentum | 62.60 | -37.40 | 453 | 27.2 | -42.62 | -8.38 | -43.85 | 343 |
| 50 | Donchian 20/10 · 1h | breakout | 61.98 | -38.02 | 181 | 17.7 | -40.03 | -8.60 | -42.49 | 194 |
| 51 | EMA 9/21 cross · 1h | trend | 59.91 | -40.09 | 310 | 12.3 | -44.29 | -10.51 | -45.66 | 330 |
| 52 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -34.01 | -5.14 | -35.64 | 185 |
| 53 | MACD cross · 1h | trend | 57.87 | -42.13 | 477 | 21.0 | -53.32 | -10.87 | -54.42 | 501 |
| 54 | Agent (ML meta-label) | meta | 56.92 | -43.08 | 2066 | 25.3 | -24.69 | -3.31 | -34.52 | 328 |
| 55 | CCI reversion · 1h | reversion | 55.89 | -44.11 | 444 | 39.4 | -51.92 | -8.88 | -52.62 | 493 |
| 56 | Bollinger reversion · 1h | reversion | 55.50 | -44.50 | 392 | 37.5 | -39.71 | -4.79 | -45.42 | 424 |
| 57 | VWAP momentum · 1h | momentum | 53.29 | -46.71 | 1065 | 21.6 | -58.50 | -13.16 | -59.87 | 1176 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.85 | -8.50 | -52.93 | 686 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.07 | -8.98 | -56.34 | 595 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -49.67 | -99.15 | 5358 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.75 | -33.59 | -83.79 | 1415 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.51 | -50.87 | -94.52 | 2438 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.72 | -32.46 | -90.73 | 1900 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.82 | -42.43 | -91.82 | 2237 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.67 | -28.89 | -89.82 | 1963 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -49.71 | -98.17 | 3438 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -56.27 | -96.95 | 3335 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.07 | -37.44 | -93.08 | 2081 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.30 | -36.00 | -83.30 | 1546 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -57.41 | -99.68 | 6268 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.25 | -39.57 | -93.26 | 2501 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.37 | -36.99 | -94.37 | 3174 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.83 | -99.82 | 6108 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.18 | -44.81 | -93.23 | 2260 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.62 | -22.25 | -51.71 | 642 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.62 | -23.88 | -78.75 | 1616 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -59.79 | -97.77 | 3282 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -61.70 | -99.18 | 5133 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.41 | -27.85 | -71.43 | 1210 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.94 | -49.07 | -94.95 | 2677 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -47.03 | -6.61 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.26 | -36.98 | -85.49 | 1665 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.10 | -99.77 | 6530 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.56 | -31.52 | -91.72 | 2471 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.81 | -20.31 | -83.21 | 1952 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.93 | -31.63 | -91.98 | 2168 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.16 | -50.01 | -98.16 | 4063 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.29 | -47.93 | -90.29 | 2199 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.85 | -29.65 | -68.85 | 804 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.30 | -28.57 | -73.30 | 1162 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.04 | -19.30 | -84.31 | 1815 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -50.60 | -98.06 | 4424 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -106.13 | -99.94 | 8258 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.93 | -7.39 | -50.46 | 306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T20:05 | Agent (ML meta-label) | buy | MSFT | 14.15 | — | entry |
| 2026-11-24T20:05 | EMA 9/21 cross · 1h | buy | TNA | 3.00 | — | rebalance up |
| 2026-11-24T20:05 | EMA 9/21 cross · 1h | sell | IWM | 3.00 | -0.01 | rebalance down |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 20:10:05.000143+00:00 -> 2026-11-24 20:20:05.000143+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
