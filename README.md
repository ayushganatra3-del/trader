# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T06:39:05.000102+00:00 · 57877 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.55 (-14.45%)

Closed trades 190, win rate 35.3%, fees £5.54, max drawdown -14.98%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 5430 decisions in 1086 calls, $0.0761 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T06:39 | 2 / 2 / 1 | SOL-USD 14% |  |
| Breezy | 2026-11-13T06:39 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-13T06:39 | 3 / 2 / 0 | SOL-USD 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.77% | 6 |
| MFI reversion | TSLA | 1.75 | +2.55% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.09 | 17.09 | 0 | — | 14.68 | 4.92 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.62 | 12.62 | 22 | 68.2 | 16.23 | 3.32 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.73 | 11.73 | 34 | 29.4 | 20.04 | 2.99 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.04 | 4.04 | 0 | — | 6.13 | 1.70 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.73 | 0.73 | 140 | 35.0 | 7.14 | 2.82 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.44 | 1.84 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.56 | -1.44 | 0 | — | -0.22 | 0.00 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.92 | -2.08 | 1 | 0.0 | -2.09 | -1.43 | -5.83 | 2 |
| 13 | Agent (rotation) | meta | 97.84 | -2.16 | 191 | 30.4 | -0.44 | -0.09 | -8.69 | 158 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.11 | -3.89 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.93 | -3.36 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 95.05 | -4.95 | 43 | 39.5 | -4.17 | -0.75 | -14.81 | 66 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.12 | -5.88 | 0 | — | -4.23 | -1.12 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 93.24 | -6.76 | 1 | 0.0 | -7.08 | -1.56 | -16.91 | 2 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 21 | Trend pullback · 1h | trend | 91.78 | -8.22 | 110 | 22.7 | -13.08 | -4.55 | -17.58 | 73 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Parabolic SAR · 1h | trend | 86.03 | -13.97 | 171 | 27.5 | -14.92 | -3.21 | -21.80 | 217 |
| 24 | Opening range 30m | breakout | 85.89 | -14.11 | 433 | 33.3 | -10.11 | -3.19 | -14.11 | 601 |
| 25 | Agent | meta | 85.55 | -14.45 | 190 | 35.3 | -15.04 | -7.57 | -15.21 | 210 |
| 26 | Daily: Bullish score | daily | 84.76 | -15.23 | 16 | 18.8 | -11.13 | -1.80 | -19.56 | 15 |
| 27 | Donchian 55/20 · 1h | breakout | 83.99 | -16.01 | 73 | 13.7 | -22.89 | -4.82 | -29.68 | 94 |
| 28 | Agent (aggressive) | meta | 83.73 | -16.27 | 92 | 33.7 | -17.67 | -4.98 | -18.51 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 82.38 | -17.62 | 2 | 0.0 | -8.05 | -0.88 | -24.16 | 1 |
| 30 | Keltner breakout · 1h | breakout | 81.71 | -18.29 | 114 | 23.7 | -15.25 | -3.04 | -25.14 | 169 |
| 31 | ADX DI cross · 1h | trend | 81.45 | -18.55 | 192 | 19.3 | -19.94 | -3.05 | -29.51 | 270 |
| 32 | Max aggression: 5-day momentum | meta | 81.45 | -18.55 | 20 | 45.0 | -32.68 | -1.99 | -45.81 | 22 |
| 33 | Hold BTC | benchmark | 81.18 | -18.82 | 1 | 0.0 | -11.21 | -1.56 | -22.00 | 1 |
| 34 | Connors RSI(2) · 1h | reversion | 80.97 | -19.03 | 210 | 40.5 | -17.80 | -6.24 | -18.30 | 114 |
| 35 | Volume breakout · 1h | breakout | 80.16 | -19.84 | 159 | 28.3 | -13.17 | -3.05 | -22.12 | 90 |
| 36 | Stochastic reversion · 1h | reversion | 79.36 | -20.64 | 298 | 47.3 | -26.64 | -3.93 | -27.61 | 390 |
| 37 | MFI reversion · 1h | reversion | 78.87 | -21.13 | 390 | 35.4 | -19.21 | -2.46 | -23.02 | 161 |
| 38 | Opening range 15m | breakout | 78.23 | -21.77 | 524 | 31.3 | -17.52 | -4.71 | -21.36 | 715 |
| 39 | Heikin-Ashi · 1h | trend | 77.09 | -22.91 | 437 | 24.5 | -36.24 | -6.77 | -38.20 | 656 |
| 40 | MACD cross · 1h | trend | 76.88 | -23.12 | 377 | 23.1 | -28.23 | -4.20 | -38.65 | 472 |
| 41 | Bollinger breakout · 1h | breakout | 76.65 | -23.35 | 179 | 22.3 | -20.88 | -4.31 | -29.92 | 239 |
| 42 | Max aggression: 1-day momentum | meta | 76.00 | -24.00 | 29 | 27.6 | -15.60 | -0.34 | -57.50 | 40 |
| 43 | MACD zero-line · 1h | trend | 75.81 | -24.19 | 168 | 17.9 | -21.64 | -4.22 | -30.99 | 204 |
| 44 | Supertrend · 1h | trend | 75.59 | -24.41 | 172 | 14.0 | -27.77 | -4.76 | -36.51 | 212 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.16 | -8.87 | -31.80 | 116 |
| 46 | RSI momentum · 1h | momentum | 75.10 | -24.90 | 162 | 13.6 | -24.54 | -3.81 | -36.35 | 212 |
| 47 | EMA 20/50 cross · 1h | trend | 74.76 | -25.24 | 105 | 10.5 | -26.92 | -4.57 | -38.62 | 122 |
| 48 | Daily: Momentum burst | daily | 74.17 | -25.83 | 27 | 11.1 | -30.29 | -4.08 | -36.97 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.48 | -26.52 | 147 | 14.3 | -26.23 | -4.29 | -37.19 | 205 |
| 50 | ROC + volume · 1h | momentum | 72.95 | -27.05 | 390 | 28.7 | -29.37 | -5.36 | -38.32 | 374 |
| 51 | Donchian 20/10 · 1h | breakout | 72.21 | -27.79 | 145 | 19.3 | -27.07 | -4.89 | -35.90 | 209 |
| 52 | Bollinger reversion · 1h | reversion | 71.75 | -28.25 | 295 | 41.0 | -32.37 | -5.04 | -35.72 | 378 |
| 53 | OBV trend · 1h | momentum | 71.67 | -28.32 | 290 | 19.3 | -27.50 | -4.78 | -36.71 | 275 |
| 54 | CCI reversion · 1h | reversion | 71.13 | -28.87 | 345 | 43.5 | -37.59 | -5.94 | -37.82 | 456 |
| 55 | Williams %R · 1h | reversion | 67.40 | -32.60 | 377 | 43.2 | -42.33 | -6.94 | -42.58 | 529 |
| 56 | EMA 9/21 cross · 1h | trend | 67.31 | -32.69 | 259 | 10.0 | -35.12 | -7.20 | -41.97 | 329 |
| 57 | Z-score reversion · 1h | reversion | 66.28 | -33.72 | 203 | 37.4 | -29.64 | -4.20 | -29.71 | 231 |
| 58 | Agent (ML meta-label) | meta | 66.18 | -33.82 | 1820 | 24.8 | -12.18 | -1.69 | -22.32 | 345 |
| 59 | VWAP momentum · 1h | momentum | 65.99 | -34.02 | 899 | 22.2 | -50.88 | -10.35 | -51.23 | 1218 |
| 60 | RSI(14) reversion · 1h | reversion | 63.57 | -36.43 | 183 | 31.7 | -36.04 | -5.30 | -36.57 | 235 |
| 61 | Candlestick reversal · 1h | reversion | 62.20 | -37.80 | 476 | 28.2 | -43.96 | -8.09 | -44.25 | 590 |
| 62 | Three white soldiers | momentum | 58.41 | -41.59 | 539 | 14.5 | -49.63 | -22.23 | -49.68 | 665 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -43.56 | -99.00 | 5260 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.89 | -25.22 | -79.89 | 1408 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.78 | -44.66 | -93.78 | 2528 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.31 | -31.47 | -89.37 | 1917 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -40.60 | -91.32 | 2334 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.78 | -30.99 | -89.82 | 2195 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -50.55 | -97.90 | 3475 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -54.18 | -96.29 | 3439 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.58 | -32.76 | -93.58 | 2335 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.28 | -34.34 | -83.28 | 1659 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.58 | -54.95 | -99.58 | 5999 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.34 | -42.54 | -92.36 | 2613 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.31 | -36.24 | -95.31 | 3460 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -70.06 | -99.82 | 6147 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -42.02 | -92.29 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.53 | -25.55 | -75.53 | 1626 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -58.07 | -97.64 | 3506 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.90 | -63.16 | -98.90 | 4924 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.79 | -26.64 | -68.88 | 1236 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.78 | -54.94 | -94.80 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.11 | -38.52 | -85.11 | 1782 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -75.20 | -99.67 | 6355 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.23 | -32.54 | -90.26 | 2311 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.59 | -20.15 | -78.72 | 1775 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.74 | -36.36 | -90.77 | 2174 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.01 | -52.75 | -97.02 | 3872 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -54.96 | -89.27 | 2132 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.06 | -29.62 | -66.13 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.43 | -22.79 | -71.45 | 1252 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.12 | -19.29 | -80.31 | 1728 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.38 | -50.12 | -97.39 | 4312 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -96.80 | -99.93 | 8363 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T06:25 | Three white soldiers | buy | BTC-USD | 14.60 | — | entry signal |
| 2026-11-13T06:20 | Three white soldiers | buy | SOL-USD | 14.60 | — | entry signal |
| 2026-11-13T06:00 | Williams %R · 1h | buy | XRP-USD | 6.74 | — | entry signal |
| 2026-11-13T06:00 | Stochastic reversion · 1h | buy | DOGE-USD | 4.20 | — | entry signal |
| 2026-11-13T06:00 | Stochastic reversion · 1h | buy | BTC-USD | 8.80 | — | entry signal |
| 2026-11-13T06:00 | Bollinger reversion · 1h | buy | XRP-USD | 10.23 | — | entry signal |
| 2026-11-13T06:00 | Bollinger reversion · 1h | buy | DOGE-USD | 10.23 | — | entry signal |
| 2026-11-13T06:00 | RSI(14) reversion · 1h | buy | XRP-USD | 10.58 | — | entry signal |
| 2026-11-13T06:00 | Candlestick reversal · 1h | buy | XRP-USD | 6.89 | — | entry signal |
| 2026-11-13T06:00 | Candlestick reversal · 1h | buy | SOL-USD | 6.89 | — | entry signal |
| 2026-11-13T06:00 | Candlestick reversal · 1h | buy | DOGE-USD | 6.89 | — | entry signal |
| 2026-11-13T03:55 | MFI reversion · 1h | sell | XRP-USD | 11.13 | -0.30 | stop-loss |
| 2026-11-13T03:50 | MFI reversion · 1h | sell | DOGE-USD | 11.13 | -0.28 | stop-loss |
| 2026-11-13T03:50 | RSI(14) reversion · 1h | sell | DOGE-USD | 7.68 | -0.36 | stop-loss |
| 2026-11-13T03:45 | CCI reversion · 1h | sell | XRP-USD | 11.79 | -0.32 | stop-loss |
| 2026-11-13T03:45 | Z-score reversion · 1h | sell | XRP-USD | 16.52 | -0.38 | stop-loss |
| 2026-11-13T03:25 | CCI reversion · 1h | buy | XRP-USD | 4.88 | — | rebalance up |
| 2026-11-13T03:25 | CCI reversion · 1h | sell | DOGE-USD | 6.94 | -0.29 | stop-loss |
| 2026-11-13T03:25 | Williams %R · 1h | sell | XRP-USD | 4.68 | -0.17 | stop-loss |
| 2026-11-13T03:25 | Z-score reversion · 1h | sell | DOGE-USD | 16.49 | -0.50 | stop-loss |
| 2026-11-13T03:25 | Candlestick reversal · 1h | sell | XRP-USD | 6.41 | -0.14 | stop-loss |
| 2026-11-13T03:25 | MACD cross · 1h | sell | DOGE-USD | 9.35 | -0.29 | stop-loss |
| 2026-11-13T03:20 | MFI reversion · 1h | buy | XRP-USD | 4.15 | — | rebalance up |
| 2026-11-13T03:20 | MFI reversion · 1h | buy | DOGE-USD | 5.27 | — | rebalance up |
| 2026-11-13T03:20 | MFI reversion · 1h | sell | ETH-USD | 6.02 | -0.15 | stop-loss |
| 2026-11-13T03:20 | CCI reversion · 1h | sell | ETH-USD | 7.01 | -0.22 | stop-loss |
| 2026-11-13T03:20 | Williams %R · 1h | sell | ETH-USD | 4.71 | -0.15 | stop-loss |
| 2026-11-13T03:20 | Z-score reversion · 1h | sell | ETH-USD | 16.58 | -0.43 | stop-loss |
| 2026-11-13T03:20 | Bollinger reversion · 1h | sell | ETH-USD | 8.90 | -0.22 | stop-loss |
| 2026-11-13T03:20 | RSI(14) reversion · 1h | sell | ETH-USD | 7.80 | -0.24 | stop-loss |
| 2026-11-13T03:15 | MFI reversion · 1h | sell | SOL-USD | 6.02 | -0.18 | stop-loss |
| 2026-11-13T03:15 | CCI reversion · 1h | sell | SOL-USD | 7.02 | -0.21 | stop-loss |
| 2026-11-13T03:15 | Williams %R · 1h | sell | SOL-USD | 4.71 | -0.14 | stop-loss |
| 2026-11-13T03:15 | Stochastic reversion · 1h | sell | SOL-USD | 13.01 | -0.26 | stop-loss |
| 2026-11-13T03:15 | Z-score reversion · 1h | buy | XRP-USD | 6.63 | — | rebalance up |
| 2026-11-13T03:15 | Z-score reversion · 1h | buy | ETH-USD | 3.41 | — | rebalance up |
| 2026-11-13T03:15 | Z-score reversion · 1h | buy | DOGE-USD | 3.39 | — | rebalance up |
| 2026-11-13T03:15 | Z-score reversion · 1h | sell | SOL-USD | 16.49 | -0.49 | stop-loss |
| 2026-11-13T03:15 | Bollinger reversion · 1h | sell | SOL-USD | 8.89 | -0.27 | stop-loss |
| 2026-11-13T03:15 | RSI(14) reversion · 1h | sell | SOL-USD | 7.81 | -0.24 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 06:39:05.000102+00:00 -> 2026-11-13 06:49:05.000102+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
