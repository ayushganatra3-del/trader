# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T18:40:05.000136+00:00 · 72127 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.35 (-21.65%)

Closed trades 243, win rate 35.8%, fees £6.56, max drawdown -22.02%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 15.61 | -0.08 |

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

Today: 30828 decisions in 2961 calls, $0.3870 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T18:40 | 8 / 20 / 2 | cash |  |
| Breezy | 2026-11-24T18:40 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-24T18:40 | 6 / 24 / 0 | COIN 63% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.51 | 15.51 | 0 | — | 13.51 | 4.68 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.33 | 4.33 | 0 | — | 4.75 | 1.31 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.12 | 0.05 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.24 | -3.76 | 229 | 28.4 | -1.16 | -0.32 | -7.61 | 160 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.06 | -3.51 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.62 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.34 | -5.66 | 0 | — | -6.38 | -1.63 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.91 | -6.09 | 20 | 10.0 | -4.73 | -7.78 | -4.88 | 19 |
| 14 | Copy: Insider buying | copy | 92.30 | -7.70 | 59 | 39.0 | -7.05 | -1.29 | -14.79 | 70 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.90 | -8.10 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 16 | Trend pullback · 1h | trend | 90.96 | -9.04 | 116 | 24.1 | -8.10 | -4.08 | -10.84 | 40 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.62 | -10.38 | 0 | — | -11.02 | -2.37 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.00 | -2.99 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.53 | -13.47 | 167 | 46.1 | -10.77 | -1.94 | -20.49 | 154 |
| 21 | Opening range 30m | breakout | 85.56 | -14.44 | 469 | 32.8 | -13.57 | -4.57 | -14.39 | 552 |
| 22 | Daily: Bullish score | daily | 85.25 | -14.75 | 20 | 20.0 | -13.33 | -3.12 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -19.21 | -6.87 | -19.48 | 72 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.62 | -6.51 | -14.78 | 66 |
| 26 | Parabolic SAR · 1h | trend | 78.99 | -21.02 | 206 | 28.2 | -31.95 | -8.40 | -32.65 | 184 |
| 27 | Agent | meta | 78.35 | -21.65 | 243 | 35.8 | -26.27 | -5.97 | -26.47 | 195 |
| 28 | Volume breakout · 1h | breakout | 78.29 | -21.71 | 169 | 27.8 | -22.08 | -6.69 | -23.97 | 72 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 77.03 | -22.97 | 138 | 24.6 | -26.59 | -6.88 | -28.54 | 153 |
| 31 | Opening range 15m | breakout | 76.82 | -23.18 | 585 | 30.4 | -22.39 | -6.98 | -22.97 | 679 |
| 32 | Donchian 55/20 · 1h | breakout | 76.27 | -23.73 | 87 | 13.8 | -29.49 | -7.81 | -29.87 | 84 |
| 33 | Ichimoku · 1h | trend | 74.70 | -25.30 | 113 | 15.9 | -29.58 | -7.59 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.64 | -29.36 | 259 | 19.3 | -38.86 | -7.44 | -40.53 | 283 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.25 | -4.86 | -36.38 | 24 |
| 36 | Hold BTC | benchmark | 69.39 | -30.61 | 3 | 0.0 | -29.11 | -5.17 | -36.10 | 1 |
| 37 | Bollinger breakout · 1h | breakout | 69.16 | -30.84 | 208 | 22.1 | -31.75 | -8.35 | -34.23 | 211 |
| 38 | Supertrend · 1h | trend | 69.07 | -30.93 | 205 | 18.5 | -35.09 | -6.78 | -37.30 | 214 |
| 39 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -39.14 | -10.31 | -39.33 | 173 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 68.31 | -31.69 | 3 | 0.0 | -24.49 | -3.01 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.60 | -32.40 | 124 | 9.7 | -37.77 | -10.22 | -38.68 | 114 |
| 42 | OBV trend · 1h | momentum | 66.45 | -33.55 | 323 | 19.8 | -39.58 | -10.19 | -40.42 | 229 |
| 43 | RSI momentum · 1h | momentum | 65.63 | -34.37 | 200 | 15.0 | -40.11 | -9.22 | -41.87 | 194 |
| 44 | Heikin-Ashi · 1h | trend | 65.06 | -34.94 | 539 | 22.1 | -47.72 | -9.72 | -49.67 | 629 |
| 45 | MACD zero-line · 1h | trend | 64.41 | -35.59 | 199 | 16.6 | -33.79 | -9.23 | -34.34 | 201 |
| 46 | Max aggression: 1-day momentum | meta | 63.72 | -36.28 | 34 | 26.5 | -56.22 | -4.19 | -60.68 | 38 |
| 47 | Stochastic reversion · 1h | reversion | 63.66 | -36.34 | 400 | 40.5 | -34.67 | -3.77 | -42.73 | 436 |
| 48 | ROC + volume · 1h | momentum | 62.99 | -37.01 | 453 | 27.2 | -42.12 | -8.22 | -43.84 | 342 |
| 49 | Donchian 20/10 · 1h | breakout | 62.39 | -37.61 | 181 | 17.7 | -39.59 | -8.48 | -42.47 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 61.54 | -38.46 | 26 | 34.6 | -63.44 | -4.22 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.39 | -39.61 | 310 | 12.3 | -43.22 | -9.92 | -46.24 | 331 |
| 52 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.04 | -5.00 | -35.63 | 186 |
| 53 | MACD cross · 1h | trend | 58.16 | -41.84 | 477 | 21.0 | -52.40 | -10.61 | -53.93 | 502 |
| 54 | Agent (ML meta-label) | meta | 57.09 | -42.91 | 2063 | 25.2 | -22.40 | -2.98 | -31.60 | 340 |
| 55 | CCI reversion · 1h | reversion | 56.42 | -43.58 | 444 | 39.4 | -51.15 | -8.71 | -52.37 | 493 |
| 56 | Bollinger reversion · 1h | reversion | 55.90 | -44.10 | 392 | 37.5 | -38.99 | -4.69 | -45.42 | 424 |
| 57 | VWAP momentum · 1h | momentum | 53.99 | -46.01 | 1064 | 21.6 | -58.21 | -13.22 | -59.46 | 1176 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.95 | -8.78 | -53.51 | 682 |
| 59 | Williams %R · 1h | reversion | 50.96 | -49.04 | 509 | 37.7 | -54.59 | -8.90 | -56.11 | 595 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -49.75 | -99.16 | 5383 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.81 | -33.82 | -83.92 | 1429 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.48 | -50.23 | -94.51 | 2446 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.69 | -32.55 | -90.75 | 1922 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.72 | -42.23 | -91.78 | 2255 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.67 | -28.77 | -89.89 | 1964 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -49.44 | -98.19 | 3438 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.98 | -55.64 | -96.98 | 3371 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.05 | -36.89 | -93.16 | 2087 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.25 | -35.30 | -83.32 | 1550 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.39 | -99.68 | 6270 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.17 | -39.29 | -93.23 | 2503 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.33 | -36.60 | -94.35 | 3155 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.00 | -99.82 | 6118 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.15 | -44.52 | -93.22 | 2270 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.61 | -22.27 | -51.76 | 640 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.78 | -23.85 | -79.02 | 1622 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -59.16 | -97.80 | 3280 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -62.16 | -99.19 | 5131 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.21 | -27.62 | -71.30 | 1202 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.89 | -48.02 | -94.96 | 2679 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.45 | -6.53 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.34 | -36.71 | -85.62 | 1678 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.98 | -99.77 | 6518 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -31.52 | -91.72 | 2471 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.76 | -20.26 | -83.18 | 1950 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.80 | -31.94 | -91.98 | 2173 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -50.03 | -98.16 | 4052 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.31 | -48.56 | -90.38 | 2211 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.80 | -29.73 | -68.80 | 799 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.02 | -28.36 | -73.27 | 1164 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.92 | -19.21 | -84.31 | 1819 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.03 | -50.43 | -98.06 | 4407 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -104.53 | -99.94 | 8262 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.04 | -7.06 | -51.27 | 298 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-24T18:00 | Williams %R · 1h | sell | ETH-USD | 3.45 | -0.03 | rebalance down |
| 2026-11-24T18:00 | Williams %R · 1h | sell | BTC-USD | 3.45 | -0.03 | rebalance down |
| 2026-11-24T18:00 | Williams %R · 1h | sell | AMZN | 3.36 | -0.07 | rebalance down |
| 2026-11-24T18:00 | Bollinger reversion · 1h | buy | ETH-USD | 8.77 | — | entry signal |
| 2026-11-24T18:00 | Bollinger reversion · 1h | sell | XRP-USD | 2.96 | -0.02 | rebalance down |
| 2026-11-24T18:00 | Bollinger reversion · 1h | sell | SOL-USD | 2.87 | -0.04 | rebalance down |
| 2026-11-24T18:00 | Bollinger reversion · 1h | sell | DOGE-USD | 2.94 | -0.02 | rebalance down |
| 2026-11-24T17:55 | Agent | buy | SQQQ | 15.68 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T17:51 | Agent (ML meta-label) | sell | AMD | 8.36 | 0.29 | selected signal exited |
| 2026-11-24T17:35 | Agent | sell | SQQQ | 15.32 | -0.45 | selected signal exited |
| 2026-11-24T17:35 | Opening range 30m | buy | TNA | 8.28 | — | rebalance up |
| 2026-11-24T17:35 | Opening range 30m | buy | MSFT | 4.29 | — | rebalance up |
| 2026-11-24T17:35 | Opening range 30m | buy | IWM | 4.28 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 18:40:05.000136+00:00 -> 2026-11-24 18:50:05.000136+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
