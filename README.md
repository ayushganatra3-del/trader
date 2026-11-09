# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T11:10:05.000131+00:00 · 53317 ticks

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

Today: 9075 decisions in 1815 calls, $0.1270 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T11:10 | 4 / 0 / 1 | cash |  |
| Breezy | 2026-11-09T11:10 | 0 / 4 / 1 | cash |  |
| Boozy | 2026-11-09T11:10 | 3 / 1 / 1 | ETH-USD 54% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.74 | 11.74 | 0 | — | 13.03 | 4.43 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.27 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.06 | 0.13 | -9.63 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 98.94 | -1.06 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.77 | -1.23 | 131 | 47.3 | -12.40 | -2.90 | -13.98 | 152 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.31 | 2.75 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -6.86 | -3.98 | -10.32 | 163 |
| 12 | Hold SPY | benchmark | 94.36 | -5.64 | 0 | — | -4.16 | -1.47 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.45 | -0.39 | -9.06 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Trend pullback · 1h | trend | 91.96 | -8.04 | 108 | 23.1 | -14.27 | -5.43 | -17.86 | 78 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.72 | -8.28 | 7 | 42.9 | -10.10 | -0.97 | -18.73 | 8 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 91.68 | -8.32 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.37 | -9.63 | 0 | — | -7.19 | -2.11 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.48 | -4.92 | -17.56 | 588 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.07 | -3.14 | -14.68 | 81 |
| 23 | Daily: Bullish score | daily | 88.65 | -11.35 | 15 | 20.0 | -5.00 | -1.02 | -16.58 | 14 |
| 24 | Copy: Insider buying | copy | 88.35 | -11.64 | 40 | 37.5 | -13.56 | -3.32 | -16.06 | 61 |
| 25 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -13.63 | -7.16 | -13.73 | 196 |
| 26 | Parabolic SAR · 1h | trend | 86.80 | -13.20 | 166 | 27.1 | -12.88 | -2.83 | -20.50 | 234 |
| 27 | Hold BTC | benchmark | 86.10 | -13.90 | 1 | 0.0 | -5.60 | -0.73 | -15.58 | 1 |
| 28 | Donchian 55/20 · 1h | breakout | 85.84 | -14.16 | 71 | 14.1 | -12.74 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 84.79 | -15.21 | 17 | 47.1 | -32.59 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -16.64 | -4.81 | -18.51 | 93 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -5.98 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 81.50 | -18.50 | 265 | 46.4 | -25.67 | -3.81 | -29.25 | 394 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.21 | -4.60 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.09 | -19.91 | 2 | 0.0 | -12.03 | -1.62 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 78.80 | -21.20 | 177 | 18.1 | -23.95 | -4.00 | -27.31 | 261 |
| 38 | Ichimoku · 1h | trend | 77.70 | -22.30 | 94 | 14.9 | -22.74 | -4.65 | -29.43 | 124 |
| 39 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.22 | -4.82 | -27.58 | 245 |
| 40 | MFI reversion · 1h | reversion | 76.34 | -23.66 | 343 | 33.5 | -20.44 | -2.96 | -21.93 | 160 |
| 41 | EMA 20/50 cross · 1h | trend | 76.01 | -23.99 | 102 | 10.8 | -21.86 | -3.93 | -30.58 | 127 |
| 42 | CCI reversion · 1h | reversion | 75.47 | -24.53 | 304 | 43.8 | -29.76 | -4.90 | -30.28 | 469 |
| 43 | Heikin-Ashi · 1h | trend | 75.24 | -24.76 | 393 | 22.9 | -41.95 | -8.78 | -41.95 | 670 |
| 44 | MACD zero-line · 1h | trend | 74.45 | -25.55 | 157 | 16.6 | -24.83 | -5.11 | -29.20 | 206 |
| 45 | Triple EMA stack · 1h | trend | 74.37 | -25.63 | 142 | 14.8 | -27.44 | -5.73 | -33.48 | 200 |
| 46 | Supertrend · 1h | trend | 73.37 | -26.63 | 166 | 13.3 | -29.10 | -5.03 | -34.80 | 213 |
| 47 | RSI momentum · 1h | momentum | 73.29 | -26.71 | 158 | 12.7 | -26.42 | -5.01 | -32.60 | 214 |
| 48 | MACD cross · 1h | trend | 72.29 | -27.71 | 348 | 22.7 | -34.15 | -6.02 | -39.27 | 478 |
| 49 | Daily: Momentum burst | daily | 72.23 | -27.77 | 26 | 11.5 | -35.90 | -5.13 | -38.31 | 31 |
| 50 | Williams %R · 1h | reversion | 72.11 | -27.89 | 315 | 44.8 | -36.20 | -5.84 | -37.41 | 537 |
| 51 | Bollinger reversion · 1h | reversion | 71.95 | -28.05 | 260 | 38.8 | -31.10 | -5.35 | -33.27 | 373 |
| 52 | Z-score reversion · 1h | reversion | 71.65 | -28.35 | 169 | 34.3 | -24.02 | -3.61 | -27.66 | 230 |
| 53 | Donchian 20/10 · 1h | breakout | 71.38 | -28.62 | 141 | 19.9 | -29.54 | -5.47 | -34.69 | 211 |
| 54 | OBV trend · 1h | momentum | 70.85 | -29.15 | 273 | 17.9 | -27.76 | -5.84 | -33.65 | 278 |
| 55 | ROC + volume · 1h | momentum | 69.69 | -30.31 | 348 | 25.3 | -37.53 | -7.23 | -39.24 | 378 |
| 56 | EMA 9/21 cross · 1h | trend | 66.54 | -33.46 | 246 | 9.8 | -37.58 | -7.68 | -39.16 | 328 |
| 57 | Agent (ML meta-label) | meta | 65.94 | -34.06 | 1542 | 23.0 | -13.60 | -2.01 | -21.87 | 355 |
| 58 | VWAP momentum · 1h | momentum | 65.92 | -34.08 | 798 | 21.6 | -53.60 | -11.78 | -53.60 | 1229 |
| 59 | RSI(14) reversion · 1h | reversion | 64.88 | -35.12 | 150 | 26.7 | -30.08 | -4.77 | -32.49 | 226 |
| 60 | Candlestick reversal · 1h | reversion | 64.38 | -35.62 | 424 | 27.8 | -38.93 | -7.24 | -38.94 | 587 |
| 61 | Three white soldiers | momentum | 62.64 | -37.36 | 487 | 15.0 | -49.36 | -22.50 | -49.36 | 650 |
| 62 | Max aggression: 1-day momentum | meta | 61.95 | -38.05 | 26 | 26.9 | -42.96 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -46.05 | -99.01 | 5258 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.29 | -25.95 | -80.29 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -45.98 | -93.44 | 2510 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.37 | -32.22 | -89.51 | 1910 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.98 | -39.58 | -91.00 | 2307 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.04 | -31.69 | -90.04 | 2190 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -54.04 | -97.73 | 3475 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -54.52 | -96.35 | 3398 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -32.41 | -93.59 | 2426 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.36 | -34.67 | -82.36 | 1650 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -55.64 | -99.53 | 6009 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.63 | -43.80 | -92.63 | 2595 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.62 | -37.62 | -95.62 | 3402 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.56 | -99.80 | 6188 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -43.36 | -91.91 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.72 | -24.83 | -75.82 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -60.79 | -97.76 | 3506 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.64 | -98.84 | 4899 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.51 | -28.98 | -69.54 | 1195 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.65 | -53.54 | -94.65 | 2740 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.81 | -36.57 | -84.86 | 1759 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.35 | -99.65 | 6395 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.67 | -32.41 | -89.77 | 2309 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.39 | -20.09 | -78.51 | 1764 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.68 | -36.82 | -90.74 | 2225 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.81 | -53.07 | -96.82 | 3907 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.46 | -57.62 | -89.56 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.85 | -28.26 | -65.87 | 801 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.20 | -23.62 | -72.23 | 1249 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.34 | -18.96 | -79.54 | 1686 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.32 | -50.79 | -97.33 | 4338 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -108.62 | -99.93 | 8288 |
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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 11:10:05.000131+00:00 -> 2026-11-09 11:20:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 11:10:05.000131+00:00 -> 2026-11-09 11:20:05.000131+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 11:10:05.000131+00:00 -> 2026-11-09 11:20:05.000131+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
