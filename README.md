# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T11:40:05.000183+00:00 · 53346 ticks

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

Today: 9510 decisions in 1902 calls, $0.1330 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T11:40 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-09T11:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-09T11:40 | 2 / 3 / 0 | ETH-USD 70% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.73 | 11.73 | 0 | — | 13.03 | 4.43 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.27 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 98.94 | -1.06 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.77 | -1.23 | 131 | 47.3 | -12.79 | -3.05 | -13.88 | 153 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.31 | 2.75 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.35 | -4.63 | -10.32 | 163 |
| 12 | Hold SPY | benchmark | 94.36 | -5.64 | 0 | — | -4.16 | -1.47 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.43 | -0.39 | -9.06 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Trend pullback · 1h | trend | 91.96 | -8.04 | 108 | 23.1 | -14.27 | -5.43 | -17.86 | 78 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.72 | -8.28 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 91.67 | -8.33 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.37 | -9.63 | 0 | — | -7.19 | -2.11 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.48 | -4.92 | -17.56 | 588 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.54 | -3.31 | -14.68 | 82 |
| 23 | Daily: Bullish score | daily | 88.64 | -11.36 | 15 | 20.0 | -5.01 | -1.02 | -16.58 | 14 |
| 24 | Copy: Insider buying | copy | 88.35 | -11.65 | 40 | 37.5 | -13.56 | -3.32 | -16.06 | 61 |
| 25 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -13.63 | -7.16 | -13.73 | 196 |
| 26 | Parabolic SAR · 1h | trend | 86.79 | -13.21 | 166 | 27.1 | -12.89 | -2.83 | -20.50 | 234 |
| 27 | Hold BTC | benchmark | 86.68 | -13.32 | 1 | 0.0 | -5.10 | -0.63 | -15.58 | 1 |
| 28 | Donchian 55/20 · 1h | breakout | 85.83 | -14.17 | 71 | 14.1 | -12.75 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 84.75 | -15.25 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -16.64 | -4.81 | -18.51 | 93 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -5.98 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 81.51 | -18.49 | 265 | 46.4 | -25.62 | -3.80 | -29.25 | 394 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.21 | -4.60 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.09 | -19.91 | 2 | 0.0 | -12.03 | -1.62 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 78.79 | -21.21 | 177 | 18.1 | -23.96 | -4.00 | -27.31 | 261 |
| 38 | Ichimoku · 1h | trend | 77.69 | -22.31 | 94 | 14.9 | -22.75 | -4.65 | -29.43 | 124 |
| 39 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.21 | -4.82 | -27.58 | 245 |
| 40 | MFI reversion · 1h | reversion | 76.50 | -23.50 | 343 | 33.5 | -18.95 | -2.80 | -20.66 | 159 |
| 41 | EMA 20/50 cross · 1h | trend | 76.00 | -24.00 | 102 | 10.8 | -21.87 | -3.93 | -30.58 | 127 |
| 42 | CCI reversion · 1h | reversion | 75.53 | -24.47 | 304 | 43.8 | -29.65 | -4.87 | -30.29 | 469 |
| 43 | Heikin-Ashi · 1h | trend | 75.24 | -24.76 | 393 | 22.9 | -41.93 | -8.78 | -41.94 | 670 |
| 44 | MACD zero-line · 1h | trend | 74.45 | -25.55 | 157 | 16.6 | -24.83 | -5.11 | -29.20 | 206 |
| 45 | Triple EMA stack · 1h | trend | 74.36 | -25.64 | 142 | 14.8 | -27.45 | -5.73 | -33.47 | 200 |
| 46 | Supertrend · 1h | trend | 73.36 | -26.64 | 166 | 13.3 | -29.11 | -5.03 | -34.80 | 213 |
| 47 | RSI momentum · 1h | momentum | 73.28 | -26.72 | 158 | 12.7 | -26.43 | -5.01 | -32.60 | 214 |
| 48 | MACD cross · 1h | trend | 72.29 | -27.71 | 348 | 22.7 | -34.15 | -6.02 | -39.27 | 478 |
| 49 | Daily: Momentum burst | daily | 72.22 | -27.78 | 26 | 11.5 | -35.90 | -5.13 | -38.31 | 31 |
| 50 | Williams %R · 1h | reversion | 72.10 | -27.89 | 315 | 44.8 | -36.06 | -5.82 | -37.36 | 537 |
| 51 | Bollinger reversion · 1h | reversion | 71.98 | -28.02 | 260 | 38.8 | -31.06 | -5.34 | -33.27 | 373 |
| 52 | Z-score reversion · 1h | reversion | 71.80 | -28.20 | 169 | 34.3 | -23.86 | -3.59 | -27.66 | 230 |
| 53 | Donchian 20/10 · 1h | breakout | 71.37 | -28.63 | 141 | 19.9 | -29.46 | -5.45 | -34.69 | 211 |
| 54 | OBV trend · 1h | momentum | 70.85 | -29.15 | 273 | 17.9 | -27.98 | -5.85 | -33.91 | 278 |
| 55 | ROC + volume · 1h | momentum | 69.69 | -30.31 | 348 | 25.3 | -37.26 | -7.19 | -38.98 | 377 |
| 56 | EMA 9/21 cross · 1h | trend | 66.53 | -33.47 | 246 | 9.8 | -37.58 | -7.68 | -39.17 | 328 |
| 57 | Agent (ML meta-label) | meta | 65.97 | -34.03 | 1542 | 23.0 | -14.46 | -2.19 | -23.07 | 357 |
| 58 | VWAP momentum · 1h | momentum | 65.92 | -34.08 | 798 | 21.6 | -53.60 | -11.78 | -53.60 | 1228 |
| 59 | RSI(14) reversion · 1h | reversion | 64.99 | -35.01 | 150 | 26.7 | -29.93 | -4.74 | -32.51 | 226 |
| 60 | Candlestick reversal · 1h | reversion | 64.44 | -35.56 | 424 | 27.8 | -38.92 | -7.23 | -39.01 | 586 |
| 61 | Three white soldiers | momentum | 62.64 | -37.36 | 487 | 15.0 | -48.94 | -22.41 | -48.94 | 648 |
| 62 | Max aggression: 1-day momentum | meta | 61.92 | -38.08 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -46.23 | -99.01 | 5262 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.32 | -25.99 | -80.32 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -46.11 | -93.45 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.42 | -32.30 | -89.58 | 1915 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.07 | -39.80 | -91.08 | 2311 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -31.57 | -90.03 | 2188 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -54.34 | -97.74 | 3478 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -55.08 | -96.37 | 3411 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -32.47 | -93.62 | 2427 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.39 | -34.76 | -82.40 | 1651 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -55.80 | -99.53 | 6008 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.61 | -43.94 | -92.63 | 2596 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.63 | -37.61 | -95.63 | 3402 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.01 | -99.80 | 6187 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.89 | -43.60 | -91.94 | 2280 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.87 | -24.80 | -76.00 | 1574 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -61.11 | -97.77 | 3508 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -63.14 | -98.85 | 4900 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.58 | -29.14 | -69.65 | 1197 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -54.02 | -94.68 | 2743 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.87 | -36.85 | -84.94 | 1762 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.36 | -99.65 | 6392 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.68 | -32.44 | -89.77 | 2310 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.24 | -20.10 | -78.44 | 1759 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.62 | -36.65 | -90.75 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.81 | -53.01 | -96.82 | 3908 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.47 | -57.69 | -89.58 | 2162 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.82 | -28.39 | -65.95 | 801 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.10 | -23.68 | -72.11 | 1248 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.31 | -18.79 | -79.57 | 1686 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.31 | -50.62 | -97.34 | 4338 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -108.82 | -99.93 | 8284 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T09:00 | CCI reversion · 1h | buy | SOL-USD | 2.23 | — | entry signal |
| 2026-11-09T09:00 | CCI reversion · 1h | buy | ETH-USD | 3.61 | — | entry signal |
| 2026-11-09T09:00 | CCI reversion · 1h | buy | DOGE-USD | 3.61 | — | entry signal |
| 2026-11-09T09:00 | Z-score reversion · 1h | buy | XRP-USD | 4.24 | — | entry signal |
| 2026-11-09T09:00 | Z-score reversion · 1h | buy | SOL-USD | 4.24 | — | entry signal |
| 2026-11-09T09:00 | Z-score reversion · 1h | buy | ETH-USD | 4.24 | — | entry signal |
| 2026-11-09T09:00 | Z-score reversion · 1h | buy | DOGE-USD | 4.24 | — | entry signal |
| 2026-11-09T09:00 | Z-score reversion · 1h | buy | BTC-USD | 4.24 | — | entry signal |
| 2026-11-09T09:00 | RSI(14) reversion · 1h | buy | XRP-USD | 1.21 | — | entry signal |
| 2026-11-09T09:00 | RSI(14) reversion · 1h | buy | SOL-USD | 3.84 | — | entry signal |
| 2026-11-09T09:00 | RSI(14) reversion · 1h | buy | ETH-USD | 3.84 | — | entry signal |
| 2026-11-09T09:00 | RSI(14) reversion · 1h | buy | BTC-USD | 3.84 | — | entry signal |
| 2026-11-09T09:00 | Candlestick reversal · 1h | buy | ETH-USD | 3.75 | — | entry signal |
| 2026-11-09T09:00 | Candlestick reversal · 1h | buy | DOGE-USD | 5.87 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 11:40:05.000183+00:00 -> 2026-11-09 11:50:05.000183+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 11:40:05.000183+00:00 -> 2026-11-09 11:50:05.000183+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 11:40:05.000183+00:00 -> 2026-11-09 11:50:05.000183+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
