# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-08T21:15:05.000155+00:00 · 52562 ticks

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

Today: 16521 decisions in 3309 calls, $0.2309 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-08T21:15 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-08T21:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-08T21:15 | 1 / 3 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.50 | +9.96% | 5 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| VWAP reversion | SQQQ | 1.91 | +6.52% | 4 |
| MFI reversion | SQQQ | 1.88 | +4.84% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.65 | -1.35 | 126 | 46.0 | -12.77 | -3.05 | -13.66 | 148 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.31 | 2.75 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.33 | -4.62 | -10.32 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.43 | -0.39 | -9.06 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -14.27 | -5.43 | -17.86 | 78 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.48 | -5.32 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -12.86 | -3.08 | -15.96 | 62 |
| 23 | Daily: Bullish score | daily | 88.75 | -11.25 | 15 | 20.0 | -5.01 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.54 | -3.31 | -14.68 | 82 |
| 25 | Hold BTC | benchmark | 88.39 | -11.61 | 1 | 0.0 | -4.59 | -0.53 | -14.09 | 1 |
| 26 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -13.73 | -7.22 | -13.74 | 198 |
| 27 | Parabolic SAR · 1h | trend | 86.90 | -13.10 | 166 | 27.1 | -12.89 | -2.83 | -20.50 | 234 |
| 28 | Donchian 55/20 · 1h | breakout | 85.94 | -14.06 | 71 | 14.1 | -12.75 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 85.15 | -14.85 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -16.81 | -4.87 | -18.51 | 94 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 81.99 | -18.01 | 263 | 46.8 | -25.30 | -3.74 | -29.25 | 391 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -21.90 | -4.53 | -24.50 | 171 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 78.98 | -21.02 | 177 | 18.1 | -24.06 | -4.02 | -27.31 | 261 |
| 38 | MFI reversion · 1h | reversion | 78.24 | -21.76 | 337 | 34.1 | -17.34 | -2.53 | -18.87 | 154 |
| 39 | Ichimoku · 1h | trend | 77.87 | -22.12 | 94 | 14.9 | -22.75 | -4.65 | -29.43 | 124 |
| 40 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.31 | -4.84 | -27.58 | 246 |
| 41 | CCI reversion · 1h | reversion | 76.35 | -23.65 | 297 | 44.8 | -29.00 | -4.74 | -29.68 | 460 |
| 42 | EMA 20/50 cross · 1h | trend | 76.07 | -23.93 | 102 | 10.8 | -21.87 | -3.93 | -30.58 | 127 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -42.90 | -9.05 | -42.90 | 676 |
| 44 | MACD zero-line · 1h | trend | 74.45 | -25.55 | 157 | 16.6 | -24.83 | -5.11 | -29.20 | 206 |
| 45 | Triple EMA stack · 1h | trend | 74.45 | -25.55 | 142 | 14.8 | -27.41 | -5.72 | -33.47 | 200 |
| 46 | Supertrend · 1h | trend | 73.62 | -26.38 | 166 | 13.3 | -29.11 | -5.03 | -34.80 | 213 |
| 47 | RSI momentum · 1h | momentum | 73.46 | -26.54 | 158 | 12.7 | -26.43 | -5.01 | -32.60 | 214 |
| 48 | Z-score reversion · 1h | reversion | 72.90 | -27.10 | 164 | 35.4 | -24.81 | -3.68 | -27.66 | 226 |
| 49 | Bollinger reversion · 1h | reversion | 72.67 | -27.33 | 257 | 39.3 | -30.63 | -5.23 | -33.45 | 368 |
| 50 | MACD cross · 1h | trend | 72.61 | -27.39 | 346 | 22.8 | -34.20 | -6.03 | -39.14 | 479 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -35.79 | -5.75 | -37.41 | 532 |
| 52 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.90 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.46 | -28.54 | 141 | 19.9 | -29.62 | -5.48 | -34.69 | 211 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -27.98 | -5.85 | -33.91 | 278 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -37.63 | -7.30 | -38.98 | 379 |
| 56 | EMA 9/21 cross · 1h | trend | 66.69 | -33.31 | 246 | 9.8 | -38.64 | -7.96 | -39.17 | 331 |
| 57 | VWAP momentum · 1h | momentum | 66.35 | -33.65 | 795 | 21.6 | -54.16 | -11.97 | -54.20 | 1232 |
| 58 | Agent (ML meta-label) | meta | 66.30 | -33.70 | 1542 | 23.0 | -7.84 | -1.25 | -17.69 | 345 |
| 59 | RSI(14) reversion · 1h | reversion | 66.06 | -33.94 | 144 | 27.1 | -29.08 | -4.55 | -31.54 | 225 |
| 60 | Candlestick reversal · 1h | reversion | 64.95 | -35.05 | 420 | 28.1 | -39.15 | -7.29 | -39.17 | 588 |
| 61 | Three white soldiers | momentum | 62.81 | -37.19 | 486 | 15.0 | -49.46 | -23.18 | -49.46 | 655 |
| 62 | Max aggression: 1-day momentum | meta | 62.21 | -37.79 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -46.42 | -98.99 | 5256 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.42 | -26.16 | -80.45 | 1427 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.49 | -47.63 | -93.49 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.18 | -32.33 | -89.21 | 1910 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.91 | -40.15 | -90.91 | 2310 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.36 | -32.68 | -90.39 | 2206 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -55.55 | -97.74 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.36 | -57.49 | -96.36 | 3414 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -33.22 | -93.67 | 2436 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.32 | -35.10 | -82.32 | 1651 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -55.68 | -99.53 | 5994 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.63 | -44.53 | -92.63 | 2601 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.80 | -39.03 | -95.80 | 3430 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.03 | -99.80 | 6190 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -44.00 | -91.77 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.45 | -24.67 | -75.45 | 1567 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -64.55 | -97.76 | 3514 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -63.99 | -98.83 | 4897 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.41 | -29.00 | -69.41 | 1194 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -55.26 | -94.66 | 2745 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.81 | -37.42 | -84.81 | 1761 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.23 | -99.65 | 6390 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.49 | -32.22 | -89.49 | 2303 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.03 | -19.89 | -78.04 | 1752 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.79 | -37.38 | -90.79 | 2222 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.72 | -53.11 | -96.72 | 3898 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.52 | -56.97 | -89.52 | 2168 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.90 | -28.78 | -65.90 | 802 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.87 | -24.43 | -72.87 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.84 | -18.45 | -78.84 | 1678 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -50.89 | -97.29 | 4340 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -120.22 | -99.93 | 8300 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-08T21:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.31 | -0.08 | exit signal |
| 2026-11-08T21:00 | MACD zero-line · 1h | sell | BTC-USD | 18.49 | -0.16 | exit signal |
| 2026-11-08T21:00 | MACD cross · 1h | sell | BTC-USD | 4.81 | -0.04 | exit signal |
| 2026-11-08T21:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 16.57 | -0.14 | exit signal |
| 2026-11-08T20:00 | MACD zero-line · 1h | buy | BTC-USD | 18.65 | — | entry signal |
| 2026-11-08T20:00 | MACD cross · 1h | sell | XRP-USD | 4.80 | -0.05 | exit signal |
| 2026-11-08T19:30 | Agent (ML meta-label) | sell | XRP-USD | 3.30 | -0.02 | selected signal exited |
| 2026-11-08T19:21 | Agent (ML meta-label) | buy | XRP-USD | 3.32 | — | entry |
| 2026-11-08T19:00 | CCI reversion · 1h | buy | ETH-USD | 2.27 | — | entry signal |
| 2026-11-08T19:00 | CCI reversion · 1h | buy | BTC-USD | 3.64 | — | entry signal |
| 2026-11-08T19:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.38 | — | entry signal |
| 2026-11-08T19:00 | MACD cross · 1h | buy | XRP-USD | 4.85 | — | entry signal |
| 2026-11-08T19:00 | MACD cross · 1h | buy | BTC-USD | 4.85 | — | entry signal |
| 2026-11-08T19:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 16.71 | — | entry signal |
| 2026-11-08T19:00 | Three white soldiers | sell | SOL-USD | 15.66 | -0.11 | exit signal |
| 2026-11-08T18:30 | Three white soldiers | sell | XRP-USD | 15.62 | -0.14 | stop-loss |
| 2026-11-08T18:20 | Three white soldiers | buy | XRP-USD | 15.77 | — | entry signal |
| 2026-11-08T18:20 | Three white soldiers | buy | SOL-USD | 15.77 | — | entry signal |
| 2026-11-08T18:00 | Stochastic reversion · 1h | buy | XRP-USD | 2.28 | — | entry signal |
| 2026-11-08T18:00 | Bollinger reversion · 1h | buy | XRP-USD | 6.06 | — | entry signal |
| 2026-11-08T18:00 | Candlestick reversal · 1h | buy | ETH-USD | 5.42 | — | entry signal |
| 2026-11-08T18:00 | MACD zero-line · 1h | sell | BTC-USD | 18.54 | -0.15 | exit signal |
| 2026-11-08T18:00 | MACD cross · 1h | sell | ETH-USD | 5.55 | -0.06 | exit signal |
| 2026-11-08T18:00 | MACD cross · 1h | sell | BTC-USD | 6.04 | -0.04 | exit signal |
| 2026-11-08T18:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 16.65 | -0.14 | exit signal |
| 2026-11-08T17:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.89 | -0.03 | exit signal |
| 2026-11-08T17:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.60 | -0.06 | exit signal |
| 2026-11-08T17:00 | VWAP momentum · 1h | sell | BTC-USD | 6.63 | -0.04 | exit signal |
| 2026-11-08T17:00 | ADX DI cross · 1h | sell | ETH-USD | 19.64 | -0.16 | exit signal |
| 2026-11-08T17:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 15.83 | -0.16 | exit signal |
| 2026-11-08T16:55 | Candlestick reversal · 1h | buy | DOGE-USD | 3.95 | — | entry |
| 2026-11-08T16:55 | Candlestick reversal · 1h | sell | ETH-USD | 3.95 | -0.03 | stop-loss |
| 2026-11-08T16:00 | CCI reversion · 1h | sell | SOL-USD | 1.71 | -0.00 | exit signal |
| 2026-11-08T15:00 | RSI(14) reversion · 1h | buy | XRP-USD | 4.14 | — | entry |
| 2026-11-08T15:00 | RSI(14) reversion · 1h | sell | BTC-USD | 4.45 | 0.00 | exit signal |
| 2026-11-08T15:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 15.99 | — | entry signal |
| 2026-11-08T15:00 | Three white soldiers | sell | XRP-USD | 15.67 | -0.13 | stop-loss |
| 2026-11-08T14:45 | Three white soldiers | buy | XRP-USD | 15.80 | — | entry signal |
| 2026-11-08T14:25 | Three white soldiers | sell | ETH-USD | 15.71 | -0.11 | exit signal |
| 2026-11-08T14:15 | Three white soldiers | buy | ETH-USD | 15.83 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-10 21:15:05.000155+00:00 -> 2026-11-08 21:25:05.000155+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-10 21:15:05.000155+00:00 -> 2026-11-08 21:25:05.000155+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-10 21:15:05.000155+00:00 -> 2026-11-08 21:25:05.000155+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
