# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T08:10:05.000124+00:00 · 53161 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.54 (-12.46%)

Closed trades 156, win rate 35.9%, fees £4.84, max drawdown -12.87%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 6735 decisions in 1347 calls, $0.0942 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T08:10 | 2 / 0 / 3 | cash |  |
| Breezy | 2026-11-09T08:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-09T08:10 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| VWAP reversion | SQQQ | 1.91 | +6.52% | 4 |
| MFI reversion | SQQQ | 1.88 | +4.84% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.01 | 12.01 | 0 | — | 13.03 | 4.43 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.27 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.18 | -0.82 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.83 | -1.17 | 131 | 47.3 | -12.57 | -3.00 | -13.66 | 153 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.31 | 2.75 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.35 | -4.63 | -10.32 | 163 |
| 12 | Hold SPY | benchmark | 94.59 | -5.41 | 0 | — | -4.16 | -1.47 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.43 | -0.39 | -9.06 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Trend pullback · 1h | trend | 92.01 | -7.99 | 108 | 23.1 | -14.27 | -5.43 | -17.86 | 78 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.94 | -8.06 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 91.90 | -8.10 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.59 | -9.40 | 0 | — | -7.19 | -2.11 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.48 | -4.92 | -17.56 | 588 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.80 | -3.40 | -14.68 | 84 |
| 23 | Daily: Bullish score | daily | 88.70 | -11.30 | 15 | 20.0 | -5.01 | -1.02 | -16.58 | 14 |
| 24 | Copy: Insider buying | copy | 88.57 | -11.43 | 40 | 37.5 | -13.56 | -3.32 | -16.06 | 61 |
| 25 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -13.63 | -7.16 | -13.73 | 196 |
| 26 | Parabolic SAR · 1h | trend | 86.85 | -13.15 | 166 | 27.1 | -12.89 | -2.83 | -20.50 | 234 |
| 27 | Hold BTC | benchmark | 85.99 | -14.01 | 1 | 0.0 | -6.28 | -0.79 | -15.58 | 1 |
| 28 | Donchian 55/20 · 1h | breakout | 85.89 | -14.11 | 71 | 14.1 | -12.75 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 84.96 | -15.04 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -16.64 | -4.81 | -18.51 | 93 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -5.98 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 81.71 | -18.29 | 265 | 46.4 | -25.65 | -3.80 | -29.25 | 394 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -21.90 | -4.53 | -24.50 | 171 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.28 | -19.72 | 2 | 0.0 | -12.03 | -1.62 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 78.89 | -21.11 | 177 | 18.1 | -23.96 | -4.00 | -27.31 | 261 |
| 38 | Ichimoku · 1h | trend | 77.79 | -22.21 | 94 | 14.9 | -22.75 | -4.65 | -29.43 | 124 |
| 39 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.31 | -4.84 | -27.58 | 246 |
| 40 | MFI reversion · 1h | reversion | 76.32 | -23.68 | 343 | 33.5 | -19.33 | -2.86 | -20.66 | 159 |
| 41 | EMA 20/50 cross · 1h | trend | 76.04 | -23.96 | 102 | 10.8 | -21.87 | -3.93 | -30.58 | 127 |
| 42 | CCI reversion · 1h | reversion | 75.77 | -24.23 | 304 | 43.8 | -29.55 | -4.85 | -30.06 | 464 |
| 43 | Heikin-Ashi · 1h | trend | 75.43 | -24.57 | 393 | 22.9 | -41.98 | -8.79 | -41.98 | 670 |
| 44 | MACD zero-line · 1h | trend | 74.45 | -25.55 | 157 | 16.6 | -24.83 | -5.11 | -29.20 | 206 |
| 45 | Triple EMA stack · 1h | trend | 74.41 | -25.59 | 142 | 14.8 | -27.44 | -5.73 | -33.47 | 200 |
| 46 | Supertrend · 1h | trend | 73.50 | -26.50 | 166 | 13.3 | -29.11 | -5.03 | -34.80 | 213 |
| 47 | RSI momentum · 1h | momentum | 73.38 | -26.62 | 158 | 12.7 | -26.43 | -5.01 | -32.60 | 214 |
| 48 | MACD cross · 1h | trend | 72.38 | -27.61 | 348 | 22.7 | -34.15 | -6.02 | -39.27 | 478 |
| 49 | Williams %R · 1h | reversion | 72.28 | -27.72 | 315 | 44.8 | -36.15 | -5.82 | -37.42 | 535 |
| 50 | Daily: Momentum burst | daily | 72.26 | -27.74 | 26 | 11.5 | -35.90 | -5.13 | -38.31 | 31 |
| 51 | Z-score reversion · 1h | reversion | 72.09 | -27.91 | 169 | 34.3 | -23.72 | -3.56 | -27.66 | 225 |
| 52 | Bollinger reversion · 1h | reversion | 72.07 | -27.93 | 260 | 38.8 | -30.75 | -5.29 | -32.89 | 372 |
| 53 | Donchian 20/10 · 1h | breakout | 71.42 | -28.58 | 141 | 19.9 | -29.62 | -5.48 | -34.69 | 211 |
| 54 | OBV trend · 1h | momentum | 70.90 | -29.10 | 273 | 17.9 | -27.98 | -5.85 | -33.91 | 278 |
| 55 | ROC + volume · 1h | momentum | 69.73 | -30.27 | 348 | 25.3 | -37.30 | -7.20 | -38.98 | 377 |
| 56 | EMA 9/21 cross · 1h | trend | 66.62 | -33.38 | 246 | 9.8 | -37.58 | -7.68 | -39.17 | 328 |
| 57 | Agent (ML meta-label) | meta | 66.08 | -33.92 | 1542 | 23.0 | -14.31 | -2.18 | -22.39 | 365 |
| 58 | VWAP momentum · 1h | momentum | 66.05 | -33.95 | 798 | 21.6 | -53.80 | -11.79 | -53.87 | 1232 |
| 59 | RSI(14) reversion · 1h | reversion | 65.15 | -34.85 | 150 | 26.7 | -29.34 | -4.65 | -32.33 | 221 |
| 60 | Candlestick reversal · 1h | reversion | 64.64 | -35.36 | 424 | 27.8 | -38.58 | -7.18 | -38.58 | 583 |
| 61 | Three white soldiers | momentum | 62.64 | -37.36 | 487 | 15.0 | -49.37 | -22.41 | -49.38 | 654 |
| 62 | Max aggression: 1-day momentum | meta | 62.07 | -37.93 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -45.86 | -99.01 | 5266 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.30 | -25.75 | -80.41 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.39 | -45.70 | -93.42 | 2510 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.83 | -89.36 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.82 | -38.86 | -90.87 | 2303 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.23 | -32.03 | -90.23 | 2199 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -53.23 | -97.71 | 3472 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -54.21 | -96.34 | 3407 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.57 | -32.58 | -93.61 | 2428 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.38 | -34.67 | -82.48 | 1654 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -55.61 | -99.54 | 6006 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.57 | -42.79 | -92.57 | 2594 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.68 | -37.71 | -95.68 | 3411 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.93 | -99.80 | 6191 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -42.64 | -91.83 | 2272 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.62 | -24.47 | -75.62 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.45 | -97.76 | 3507 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -63.37 | -98.86 | 4904 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.42 | -28.76 | -69.45 | 1194 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -52.39 | -94.61 | 2736 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -35.70 | -84.71 | 1756 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -74.53 | -99.66 | 6393 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.74 | -32.68 | -89.77 | 2314 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.29 | -20.15 | -78.44 | 1759 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.83 | -37.11 | -90.84 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.83 | -52.87 | -96.83 | 3910 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -55.74 | -89.41 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.79 | -28.05 | -65.79 | 800 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.20 | -23.62 | -72.31 | 1250 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.41 | -18.89 | -79.57 | 1686 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.33 | -50.32 | -97.33 | 4339 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -105.70 | -99.93 | 8289 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T07:30 | CCI reversion · 1h | sell | DOGE-USD | 3.69 | -0.12 | stop-loss |
| 2026-11-09T07:30 | Z-score reversion · 1h | sell | DOGE-USD | 4.69 | -0.15 | stop-loss |
| 2026-11-09T07:15 | MFI reversion · 1h | sell | BTC-USD | 8.41 | -0.17 | stop-loss |
| 2026-11-09T07:15 | CCI reversion · 1h | sell | ETH-USD | 3.66 | -0.08 | stop-loss |
| 2026-11-09T07:15 | Stochastic reversion · 1h | buy | XRP-USD | 2.17 | — | entry |
| 2026-11-09T07:15 | Stochastic reversion · 1h | sell | ETH-USD | 2.17 | -0.06 | stop-loss |
| 2026-11-09T07:15 | Z-score reversion · 1h | sell | SOL-USD | 5.02 | -0.17 | stop-loss |
| 2026-11-09T07:15 | Bollinger reversion · 1h | sell | ETH-USD | 4.38 | -0.16 | stop-loss |
| 2026-11-09T07:15 | Bollinger reversion · 1h | sell | BTC-USD | 5.93 | -0.12 | stop-loss |
| 2026-11-09T07:15 | RSI(14) reversion · 1h | sell | SOL-USD | 4.23 | -0.14 | stop-loss |
| 2026-11-09T07:15 | RSI(14) reversion · 1h | sell | BTC-USD | 4.95 | -0.10 | stop-loss |
| 2026-11-09T07:05 | MFI reversion · 1h | sell | XRP-USD | 7.51 | -0.23 | stop-loss |
| 2026-11-09T07:05 | CCI reversion · 1h | sell | SOL-USD | 2.09 | -0.06 | stop-loss |
| 2026-11-09T06:40 | CCI reversion · 1h | buy | ETH-USD | 3.73 | — | entry |
| 2026-11-09T06:40 | CCI reversion · 1h | sell | BTC-USD | 3.73 | -0.08 | stop-loss |
| 2026-11-09T06:30 | Z-score reversion · 1h | sell | BTC-USD | 5.08 | -0.11 | stop-loss |
| 2026-11-09T06:00 | VWAP momentum · 1h | sell | DOGE-USD | 5.43 | -0.10 | exit signal |
| 2026-11-09T04:00 | Candlestick reversal · 1h | sell | SOL-USD | 3.20 | -0.03 | exit signal |
| 2026-11-09T04:00 | Candlestick reversal · 1h | sell | ETH-USD | 6.43 | -0.06 | exit signal |
| 2026-11-09T04:00 | VWAP momentum · 1h | sell | ETH-USD | 2.97 | -0.02 | exit signal |
| 2026-11-09T04:00 | VWAP momentum · 1h | sell | BTC-USD | 5.47 | -0.06 | exit signal |
| 2026-11-09T02:00 | MFI reversion · 1h | buy | XRP-USD | 7.74 | — | entry signal |
| 2026-11-09T02:00 | CCI reversion · 1h | buy | SOL-USD | 2.15 | — | entry signal |
| 2026-11-09T02:00 | CCI reversion · 1h | buy | DOGE-USD | 3.81 | — | entry signal |
| 2026-11-09T02:00 | CCI reversion · 1h | buy | BTC-USD | 3.81 | — | entry signal |
| 2026-11-09T02:00 | Z-score reversion · 1h | buy | DOGE-USD | 4.84 | — | entry signal |
| 2026-11-09T02:00 | Candlestick reversal · 1h | buy | SOL-USD | 3.23 | — | entry signal |
| 2026-11-09T02:00 | VWAP momentum · 1h | buy | ETH-USD | 3.00 | — | entry signal |
| 2026-11-09T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.53 | — | entry signal |
| 2026-11-09T02:00 | VWAP momentum · 1h | buy | BTC-USD | 5.53 | — | entry signal |
| 2026-11-09T01:00 | VWAP reversion · 1h | sell | XRP-USD | 7.99 | -0.00 | exit signal |
| 2026-11-09T01:00 | VWAP reversion · 1h | sell | SOL-USD | 16.57 | 0.13 | exit signal |
| 2026-11-09T01:00 | VWAP reversion · 1h | sell | ETH-USD | 16.46 | 0.02 | exit signal |
| 2026-11-09T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 16.46 | 0.02 | exit signal |
| 2026-11-09T01:00 | VWAP reversion · 1h | sell | BTC-USD | 16.51 | 0.07 | exit signal |
| 2026-11-09T01:00 | Z-score reversion · 1h | buy | SOL-USD | 5.19 | — | entry signal |
| 2026-11-09T01:00 | Z-score reversion · 1h | buy | BTC-USD | 5.19 | — | entry signal |
| 2026-11-09T01:00 | Bollinger reversion · 1h | buy | ETH-USD | 4.54 | — | entry signal |
| 2026-11-09T01:00 | Bollinger reversion · 1h | buy | DOGE-USD | 4.54 | — | entry signal |
| 2026-11-09T01:00 | RSI(14) reversion · 1h | buy | SOL-USD | 4.38 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 08:10:05.000124+00:00 -> 2026-11-09 08:20:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 08:10:05.000124+00:00 -> 2026-11-09 08:20:05.000124+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 08:10:05.000124+00:00 -> 2026-11-09 08:20:05.000124+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
