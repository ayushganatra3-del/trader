# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T00:15:05.000139+00:00 · 52728 ticks

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

Today: 240 decisions in 48 calls, $0.0034 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T00:15 | 5 / 0 / 0 | SOL-USD 14% |  |
| Breezy | 2026-11-09T00:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-09T00:15 | 3 / 2 / 0 | ETH-USD 65% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.43 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.27 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.83 | -1.17 | 126 | 46.0 | -12.60 | -3.00 | -13.66 | 153 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.31 | 2.75 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.35 | -4.63 | -10.32 | 163 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.47 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.43 | -0.39 | -9.06 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -14.27 | -5.43 | -17.86 | 78 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.11 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.48 | -4.92 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -12.86 | -3.08 | -15.96 | 62 |
| 23 | Daily: Bullish score | daily | 88.75 | -11.25 | 15 | 20.0 | -5.01 | -1.02 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.82 | -3.41 | -14.68 | 84 |
| 25 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -13.63 | -7.16 | -13.73 | 196 |
| 26 | Hold BTC | benchmark | 87.40 | -12.60 | 1 | 0.0 | -5.97 | -0.57 | -15.15 | 1 |
| 27 | Parabolic SAR · 1h | trend | 86.90 | -13.10 | 166 | 27.1 | -12.89 | -2.83 | -20.50 | 234 |
| 28 | Donchian 55/20 · 1h | breakout | 85.94 | -14.06 | 71 | 14.1 | -12.75 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 85.15 | -14.85 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -16.64 | -4.81 | -18.51 | 93 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -5.98 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 81.96 | -18.04 | 264 | 46.6 | -25.37 | -3.75 | -29.25 | 393 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -21.90 | -4.53 | -24.50 | 171 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.62 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 78.98 | -21.02 | 177 | 18.1 | -25.10 | -4.21 | -27.31 | 265 |
| 38 | Ichimoku · 1h | trend | 77.87 | -22.12 | 94 | 14.9 | -22.75 | -4.65 | -29.43 | 124 |
| 39 | MFI reversion · 1h | reversion | 77.29 | -22.71 | 341 | 33.7 | -18.51 | -2.72 | -20.06 | 158 |
| 40 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.32 | -4.85 | -27.58 | 246 |
| 41 | CCI reversion · 1h | reversion | 76.25 | -23.75 | 300 | 44.3 | -29.15 | -4.77 | -29.68 | 460 |
| 42 | EMA 20/50 cross · 1h | trend | 76.07 | -23.93 | 102 | 10.8 | -21.87 | -3.93 | -30.58 | 127 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -42.78 | -8.79 | -42.80 | 675 |
| 44 | MACD zero-line · 1h | trend | 74.45 | -25.55 | 157 | 16.6 | -24.83 | -5.11 | -29.20 | 206 |
| 45 | Triple EMA stack · 1h | trend | 74.45 | -25.55 | 142 | 14.8 | -27.41 | -5.72 | -33.47 | 200 |
| 46 | Supertrend · 1h | trend | 73.62 | -26.38 | 166 | 13.3 | -29.11 | -5.03 | -34.80 | 213 |
| 47 | RSI momentum · 1h | momentum | 73.46 | -26.54 | 158 | 12.7 | -26.43 | -5.01 | -32.60 | 214 |
| 48 | Z-score reversion · 1h | reversion | 72.63 | -27.37 | 166 | 34.9 | -24.35 | -3.64 | -27.66 | 224 |
| 49 | Bollinger reversion · 1h | reversion | 72.58 | -27.43 | 258 | 39.1 | -30.73 | -5.25 | -33.45 | 369 |
| 50 | MACD cross · 1h | trend | 72.47 | -27.52 | 348 | 22.7 | -34.73 | -6.14 | -39.27 | 480 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -35.88 | -5.76 | -37.41 | 535 |
| 52 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.90 | -5.13 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.46 | -28.54 | 141 | 19.9 | -29.72 | -5.50 | -34.69 | 211 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -27.98 | -5.85 | -33.91 | 278 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -37.30 | -7.20 | -38.98 | 377 |
| 56 | EMA 9/21 cross · 1h | trend | 66.69 | -33.31 | 246 | 9.8 | -39.01 | -8.02 | -39.18 | 333 |
| 57 | VWAP momentum · 1h | momentum | 66.35 | -33.65 | 795 | 21.6 | -54.16 | -11.72 | -54.20 | 1232 |
| 58 | Agent (ML meta-label) | meta | 66.31 | -33.69 | 1542 | 23.0 | -10.37 | -1.50 | -20.03 | 348 |
| 59 | RSI(14) reversion · 1h | reversion | 65.60 | -34.40 | 148 | 27.0 | -30.00 | -4.75 | -32.01 | 221 |
| 60 | Candlestick reversal · 1h | reversion | 64.86 | -35.14 | 422 | 28.0 | -38.70 | -7.15 | -38.90 | 583 |
| 61 | Three white soldiers | momentum | 62.64 | -37.36 | 487 | 15.0 | -49.37 | -22.41 | -49.38 | 654 |
| 62 | Max aggression: 1-day momentum | meta | 62.21 | -37.79 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -43.70 | -98.98 | 5252 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.42 | -25.37 | -80.45 | 1427 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -44.69 | -93.42 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.27 | -31.22 | -89.27 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.83 | -38.01 | -90.83 | 2306 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.38 | -32.02 | -90.38 | 2205 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -51.15 | -97.73 | 3475 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -53.06 | -96.31 | 3408 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.60 | -32.79 | -93.61 | 2430 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.26 | -34.04 | -82.29 | 1650 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -51.38 | -99.54 | 6008 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.62 | -41.95 | -92.62 | 2599 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.78 | -37.71 | -95.78 | 3425 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -68.00 | -99.80 | 6193 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -41.83 | -91.77 | 2273 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.45 | -23.99 | -75.45 | 1566 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -58.34 | -97.74 | 3508 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -57.85 | -98.85 | 4900 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.41 | -28.62 | -69.41 | 1194 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -51.32 | -94.67 | 2743 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.80 | -35.70 | -84.80 | 1760 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -67.36 | -99.65 | 6391 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.45 | -31.32 | -89.54 | 2305 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.29 | -19.53 | -78.48 | 1758 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.83 | -35.88 | -90.92 | 2223 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.77 | -49.29 | -96.80 | 3905 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.42 | -53.38 | -89.42 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.86 | -27.88 | -65.86 | 801 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.60 | -23.62 | -72.60 | 1255 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.03 | -18.43 | -79.21 | 1682 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.31 | -47.65 | -97.33 | 4341 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -92.54 | -99.93 | 8292 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T00:00 | MFI reversion · 1h | buy | SOL-USD | 8.58 | — | entry signal |
| 2026-11-09T00:00 | MFI reversion · 1h | buy | ETH-USD | 8.58 | — | entry signal |
| 2026-11-09T00:00 | MFI reversion · 1h | buy | BTC-USD | 8.58 | — | entry signal |
| 2026-11-09T00:00 | MFI reversion · 1h | sell | DOGE-USD | 4.23 | -0.03 | rebalance down |
| 2026-11-09T00:00 | Bollinger reversion · 1h | buy | BTC-USD | 6.05 | — | entry signal |
| 2026-11-09T00:00 | RSI(14) reversion · 1h | buy | BTC-USD | 5.05 | — | entry signal |
| 2026-11-08T23:35 | Three white soldiers | sell | SOL-USD | 15.53 | -0.18 | exit signal |
| 2026-11-08T23:15 | Three white soldiers | buy | SOL-USD | 15.70 | — | entry signal |
| 2026-11-08T23:00 | MFI reversion · 1h | buy | DOGE-USD | 12.88 | — | entry signal |
| 2026-11-08T23:00 | VWAP reversion · 1h | buy | XRP-USD | 7.99 | — | entry signal |
| 2026-11-08T23:00 | VWAP reversion · 1h | buy | SOL-USD | 16.44 | — | entry signal |
| 2026-11-08T23:00 | VWAP reversion · 1h | buy | ETH-USD | 16.44 | — | entry signal |
| 2026-11-08T23:00 | VWAP reversion · 1h | buy | DOGE-USD | 16.44 | — | entry signal |
| 2026-11-08T23:00 | VWAP reversion · 1h | buy | BTC-USD | 16.44 | — | entry signal |
| 2026-11-08T22:00 | Agent (ML meta-label) | buy | ETH-USD | 3.90 | — | entry |
| 2026-11-08T22:00 | MFI reversion · 1h | sell | BTC-USD | 12.74 | -0.24 | stop-loss |
| 2026-11-08T22:00 | Stochastic reversion · 1h | buy | ETH-USD | 2.23 | — | entry signal |
| 2026-11-08T21:55 | MFI reversion · 1h | buy | BTC-USD | 5.85 | — | rebalance up |
| 2026-11-08T21:55 | MFI reversion · 1h | sell | SOL-USD | 6.89 | -0.22 | stop-loss |
| 2026-11-08T21:55 | MFI reversion · 1h | sell | ETH-USD | 6.93 | -0.20 | stop-loss |
| 2026-11-08T21:55 | MFI reversion · 1h | sell | DOGE-USD | 8.32 | -0.35 | stop-loss |
| 2026-11-08T21:55 | Z-score reversion · 1h | sell | SOL-USD | 4.98 | -0.14 | stop-loss |
| 2026-11-08T21:55 | Z-score reversion · 1h | sell | DOGE-USD | 4.08 | -0.17 | stop-loss |
| 2026-11-08T21:55 | RSI(14) reversion · 1h | sell | SOL-USD | 4.23 | -0.12 | stop-loss |
| 2026-11-08T21:55 | RSI(14) reversion · 1h | sell | ETH-USD | 4.31 | -0.16 | stop-loss |
| 2026-11-08T21:55 | RSI(14) reversion · 1h | sell | DOGE-USD | 4.21 | -0.18 | stop-loss |
| 2026-11-08T21:50 | CCI reversion · 1h | sell | ETH-USD | 2.24 | -0.04 | stop-loss |
| 2026-11-08T21:50 | CCI reversion · 1h | sell | DOGE-USD | 3.95 | -0.07 | stop-loss |
| 2026-11-08T21:50 | CCI reversion · 1h | sell | BTC-USD | 3.59 | -0.05 | stop-loss |
| 2026-11-08T21:50 | Stochastic reversion · 1h | sell | XRP-USD | 2.23 | -0.05 | stop-loss |
| 2026-11-08T21:50 | Bollinger reversion · 1h | sell | XRP-USD | 5.93 | -0.13 | stop-loss |
| 2026-11-08T21:50 | RSI(14) reversion · 1h | sell | XRP-USD | 4.03 | -0.10 | stop-loss |
| 2026-11-08T21:50 | Candlestick reversal · 1h | sell | ETH-USD | 5.34 | -0.07 | stop-loss |
| 2026-11-08T21:50 | Candlestick reversal · 1h | sell | DOGE-USD | 3.90 | -0.06 | stop-loss |
| 2026-11-08T21:50 | MACD cross · 1h | sell | SOL-USD | 4.76 | -0.10 | stop-loss |
| 2026-11-08T21:50 | MACD cross · 1h | sell | DOGE-USD | 4.77 | -0.09 | stop-loss |
| 2026-11-08T21:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.31 | -0.08 | exit signal |
| 2026-11-08T21:00 | MACD zero-line · 1h | sell | BTC-USD | 18.49 | -0.16 | exit signal |
| 2026-11-08T21:00 | MACD cross · 1h | sell | BTC-USD | 4.81 | -0.04 | exit signal |
| 2026-11-08T21:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 16.57 | -0.14 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 00:15:05.000139+00:00 -> 2026-11-09 00:25:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 00:15:05.000139+00:00 -> 2026-11-09 00:25:05.000139+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 00:15:05.000139+00:00 -> 2026-11-09 00:25:05.000139+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
