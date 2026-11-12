# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T17:40:05.000132+00:00 · 57190 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.04 (-13.96%)

Closed trades 185, win rate 35.7%, fees £5.46, max drawdown -14.98%.

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

Today: 26348 decisions in 2792 calls, $0.3343 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T17:40 | 4 / 22 / 4 | TECL 14%, SOXL 14% |  |
| Breezy | 2026-11-12T17:40 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-12T17:40 | 6 / 21 / 3 | COIN 63% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.59 | 17.59 | 0 | — | 16.38 | 5.35 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 114.48 | 14.48 | 21 | 66.7 | 21.01 | 4.08 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 113.58 | 13.58 | 33 | 27.3 | 22.05 | 3.20 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.19 | 4.19 | 0 | — | 6.38 | 1.76 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.49 | 1.49 | 137 | 33.6 | 8.03 | 3.06 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.44 | 1.83 | -9.06 | 233 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold SPY | benchmark | 99.02 | -0.98 | 0 | — | -0.55 | -0.05 | -6.18 | 1 |
| 11 | Agent (rotation) | meta | 98.92 | -1.08 | 190 | 30.5 | -1.66 | -0.53 | -9.59 | 172 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -2.95 | 0.06 | -18.69 | 5 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 98.32 | -1.68 | 1 | 0.0 | -1.61 | -1.05 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.32 | -3.68 | 0 | — | -3.90 | -0.99 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.42 | -4.58 | 142 | 47.2 | -12.80 | -3.32 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 94.85 | -5.15 | 43 | 39.5 | -6.63 | -1.29 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.65 | -5.35 | 0 | — | -2.79 | -0.69 | -10.64 | 1 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 94.55 | -5.45 | 1 | 0.0 | -5.71 | -1.17 | -16.91 | 2 |
| 19 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 21 | Trend pullback · 1h | trend | 92.10 | -7.90 | 109 | 22.9 | -13.62 | -4.74 | -18.42 | 75 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -8.27 | -2.89 | -14.89 | 75 |
| 23 | Opening range 30m | breakout | 86.66 | -13.34 | 418 | 32.8 | -9.74 | -3.05 | -14.11 | 603 |
| 24 | Parabolic SAR · 1h | trend | 86.63 | -13.37 | 171 | 27.5 | -13.24 | -2.79 | -21.98 | 220 |
| 25 | Agent | meta | 86.04 | -13.96 | 185 | 35.7 | -14.78 | -7.36 | -15.61 | 210 |
| 26 | Daily: Bullish score | daily | 84.62 | -15.38 | 16 | 18.8 | -11.55 | -1.67 | -19.56 | 15 |
| 27 | Hold BTC | benchmark | 84.56 | -15.44 | 1 | 0.0 | -7.22 | -0.96 | -18.34 | 1 |
| 28 | Agent (aggressive) | meta | 84.50 | -15.50 | 90 | 34.4 | -15.83 | -4.36 | -18.51 | 100 |
| 29 | Donchian 55/20 · 1h | breakout | 83.98 | -16.02 | 73 | 13.7 | -22.37 | -4.68 | -29.68 | 94 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.99 | -17.01 | 2 | 0.0 | -7.88 | -0.84 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.88 | -18.12 | 114 | 23.7 | -17.71 | -3.65 | -25.87 | 176 |
| 32 | ADX DI cross · 1h | trend | 81.54 | -18.46 | 191 | 19.4 | -20.21 | -3.20 | -29.90 | 266 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -25.44 | -1.29 | -45.81 | 24 |
| 34 | Connors RSI(2) · 1h | reversion | 81.17 | -18.83 | 210 | 40.5 | -19.69 | -6.63 | -20.32 | 120 |
| 35 | Volume breakout · 1h | breakout | 80.31 | -19.68 | 157 | 28.0 | -13.59 | -3.17 | -21.12 | 91 |
| 36 | MFI reversion · 1h | reversion | 80.31 | -19.69 | 378 | 36.0 | -17.53 | -2.22 | -23.02 | 164 |
| 37 | Stochastic reversion · 1h | reversion | 79.62 | -20.38 | 297 | 47.5 | -26.66 | -3.94 | -27.36 | 390 |
| 38 | Opening range 15m | breakout | 79.11 | -20.89 | 512 | 31.2 | -17.31 | -4.63 | -21.36 | 725 |
| 39 | Heikin-Ashi · 1h | trend | 77.99 | -22.01 | 431 | 24.6 | -36.06 | -6.78 | -38.20 | 658 |
| 40 | MACD cross · 1h | trend | 77.63 | -22.37 | 370 | 21.9 | -27.23 | -4.00 | -38.92 | 464 |
| 41 | Bollinger breakout · 1h | breakout | 76.46 | -23.54 | 179 | 22.3 | -22.13 | -4.60 | -29.88 | 242 |
| 42 | MACD zero-line · 1h | trend | 76.09 | -23.91 | 164 | 17.1 | -22.20 | -4.56 | -31.10 | 205 |
| 43 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -19.78 | -0.58 | -57.50 | 41 |
| 44 | Supertrend · 1h | trend | 75.95 | -24.05 | 172 | 14.0 | -28.65 | -5.03 | -36.25 | 222 |
| 45 | RSI momentum · 1h | momentum | 75.38 | -24.62 | 162 | 13.6 | -23.74 | -3.65 | -36.52 | 212 |
| 46 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 47 | EMA 20/50 cross · 1h | trend | 74.95 | -25.05 | 105 | 10.5 | -26.34 | -4.42 | -37.91 | 119 |
| 48 | Daily: Momentum burst | daily | 74.72 | -25.28 | 27 | 11.1 | -34.12 | -4.60 | -38.17 | 33 |
| 49 | ROC + volume · 1h | momentum | 73.52 | -26.48 | 385 | 27.8 | -30.60 | -5.70 | -38.37 | 377 |
| 50 | Triple EMA stack · 1h | trend | 73.43 | -26.57 | 147 | 14.3 | -25.50 | -4.22 | -36.72 | 206 |
| 51 | Bollinger reversion · 1h | reversion | 72.65 | -27.35 | 290 | 41.0 | -31.37 | -4.87 | -35.71 | 378 |
| 52 | Donchian 20/10 · 1h | breakout | 72.52 | -27.48 | 145 | 19.3 | -27.51 | -4.97 | -35.87 | 211 |
| 53 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -36.26 | -5.66 | -36.47 | 453 |
| 54 | OBV trend · 1h | momentum | 71.92 | -28.08 | 286 | 19.6 | -26.91 | -4.59 | -36.91 | 284 |
| 55 | Williams %R · 1h | reversion | 68.22 | -31.78 | 358 | 45.5 | -41.91 | -6.87 | -42.08 | 533 |
| 56 | Z-score reversion · 1h | reversion | 67.85 | -32.15 | 199 | 38.2 | -27.36 | -3.79 | -29.17 | 233 |
| 57 | EMA 9/21 cross · 1h | trend | 67.56 | -32.44 | 257 | 9.7 | -33.15 | -6.14 | -41.74 | 335 |
| 58 | VWAP momentum · 1h | momentum | 66.83 | -33.17 | 885 | 22.4 | -51.50 | -10.67 | -52.65 | 1219 |
| 59 | Agent (ML meta-label) | meta | 66.69 | -33.31 | 1788 | 25.0 | -17.52 | -2.24 | -25.29 | 344 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -33.85 | -4.66 | -35.17 | 246 |
| 61 | Candlestick reversal · 1h | reversion | 62.92 | -37.08 | 467 | 28.5 | -41.59 | -7.34 | -41.81 | 595 |
| 62 | Three white soldiers | momentum | 58.67 | -41.33 | 536 | 14.6 | -49.58 | -22.58 | -49.58 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.13 | -99.01 | 5276 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.10 | -26.13 | -80.14 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.64 | -45.87 | -93.66 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.32 | -32.19 | -89.58 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.08 | -40.68 | -91.10 | 2333 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.44 | -90.17 | 2201 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -54.30 | -97.89 | 3468 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -55.48 | -96.33 | 3435 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.52 | -32.38 | -93.53 | 2333 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.95 | -33.98 | -83.04 | 1655 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.77 | -99.58 | 5989 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.25 | -43.62 | -92.27 | 2603 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -37.13 | -95.46 | 3462 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -78.78 | -99.82 | 6148 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.30 | -44.42 | -92.30 | 2273 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.18 | -25.35 | -75.27 | 1628 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -58.36 | -97.62 | 3507 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -64.03 | -98.89 | 4905 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.46 | -27.05 | -68.54 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -58.32 | -94.78 | 2784 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.13 | -39.42 | -85.15 | 1795 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.87 | -99.66 | 6344 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.85 | -32.56 | -90.01 | 2300 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.08 | -20.15 | -78.50 | 1770 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.66 | -36.69 | -90.89 | 2188 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.87 | -53.30 | -96.90 | 3849 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -58.07 | -89.27 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.31 | -30.45 | -66.31 | 816 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.41 | -23.08 | -71.57 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.22 | -18.88 | -79.48 | 1721 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.29 | -49.71 | -97.33 | 4301 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.17 | -99.93 | 8348 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T17:40 | Agent (ML meta-label) | sell | QQQ | 4.17 | 0.00 | selected signal exited |
| 2026-11-12T17:40 | Three white soldiers | sell | BTC-USD | 14.59 | -0.14 | exit signal |
| 2026-11-12T17:40 | Three white soldiers | sell | BITX | 14.62 | -0.11 | exit signal |
| 2026-11-12T17:31 | Agent (ML meta-label) | buy | QQQ | 4.16 | — | entry |
| 2026-11-12T17:31 | Agent (ML meta-label) | sell | TNA | 3.91 | -0.00 | selected signal exited |
| 2026-11-12T17:31 | Agent (ML meta-label) | sell | PLTR | 3.33 | -0.00 | selected signal exited |
| 2026-11-12T17:31 | Agent (ML meta-label) | sell | IWM | 3.50 | -0.00 | selected signal exited |
| 2026-11-12T17:31 | Stochastic reversion · 1h | buy | BITX | 9.43 | — | entry signal |
| 2026-11-12T17:31 | Stochastic reversion · 1h | sell | MSFT | 4.64 | 0.07 | rebalance down |
| 2026-11-12T17:31 | Stochastic reversion · 1h | sell | ETHU | 4.79 | -0.07 | rebalance down |
| 2026-11-12T17:31 | VWAP momentum · 1h | sell | QQQ | 6.69 | -0.03 | exit signal |
| 2026-11-12T17:31 | VWAP momentum · 1h | sell | AAPL | 6.69 | 0.01 | exit signal |
| 2026-11-12T17:31 | Heikin-Ashi · 1h | buy | MSFT | 19.39 | — | entry signal |
| 2026-11-12T17:31 | Heikin-Ashi · 1h | buy | GOOGL | 19.52 | — | entry signal |
| 2026-11-12T17:31 | MACD cross · 1h | buy | MSFT | 6.45 | — | entry signal |
| 2026-11-12T17:31 | Triple EMA stack · 1h | buy | UPRO | 6.16 | — | entry signal |
| 2026-11-12T17:31 | Triple EMA stack · 1h | buy | GOOGL | 12.23 | — | entry signal |
| 2026-11-12T17:31 | Triple EMA stack · 1h | sell | TSLA | 6.12 | -0.01 | rebalance down |
| 2026-11-12T17:31 | Triple EMA stack · 1h | sell | QQQ | 6.17 | -0.03 | rebalance down |
| 2026-11-12T17:31 | Three white soldiers | buy | BTC-USD | 14.73 | — | entry signal |
| 2026-11-12T17:31 | Three white soldiers | buy | BITX | 14.73 | — | entry signal |
| 2026-11-12T17:25 | Agent (ML meta-label) | buy | IWM | 3.50 | — | entry |
| 2026-11-12T17:20 | Agent (rotation) | sell | AMD | 8.27 | 0.13 | selected signal exited |
| 2026-11-12T17:20 | Agent (ML meta-label) | buy | TNA | 3.92 | — | entry |
| 2026-11-12T17:20 | Agent (ML meta-label) | sell | QQQ | 4.16 | -0.01 | selected signal exited |
| 2026-11-12T17:20 | Agent (ML meta-label) | sell | IWM | 3.33 | -0.00 | selected signal exited |
| 2026-11-12T17:20 | ADX DI cross · 1h | sell | TSLA | 4.06 | 0.09 | rebalance down |
| 2026-11-12T17:20 | Gap and go | sell | AMD | 25.41 | 0.40 | stop-loss |
| 2026-11-12T17:15 | Agent (ML meta-label) | buy | PLTR | 3.34 | — | entry |
| 2026-11-12T17:15 | Agent (ML meta-label) | buy | IWM | 3.34 | — | entry |
| 2026-11-12T17:15 | Agent (ML meta-label) | sell | GOOGL | 3.41 | 0.01 | rebalance down |
| 2026-11-12T17:11 | Agent (ML meta-label) | buy | QQQ | 4.17 | — | entry |
| 2026-11-12T17:11 | Agent (ML meta-label) | sell | IWM | 3.71 | -0.00 | selected signal exited |
| 2026-11-12T17:11 | Agent | sell | AMD | 17.27 | 0.13 | selected signal exited |
| 2026-11-12T17:11 | Volume breakout · 1h | sell | AAPL | 20.02 | -0.02 | target is flat |
| 2026-11-12T17:11 | OBV trend · 1h | sell | SPY | 3.79 | -0.00 | target is flat |
| 2026-11-12T17:05 | Agent (ML meta-label) | sell | QQQ | 3.71 | 0.00 | selected signal exited |
| 2026-11-12T17:02 | Williams %R · 1h | buy | MSTR | 3.41 | — | rebalance up |
| 2026-11-12T17:02 | Williams %R · 1h | sell | SQQQ | 3.41 | -0.08 | rebalance down |
| 2026-11-12T17:00 | MFI reversion · 1h | buy | XRP-USD | 1.45 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 17:40:05.000132+00:00 -> 2026-11-12 17:50:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
