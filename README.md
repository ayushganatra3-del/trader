# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-14T17:40:05.000161+00:00 · 59664 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.50 (-14.50%)

Closed trades 195, win rate 35.9%, fees £5.63, max drawdown -15.42%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-14 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 13539 decisions in 2709 calls, $0.1895 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-14T17:40 | 0 / 5 / 0 | cash |  |
| Breezy | 2026-11-14T17:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-14T17:40 | 4 / 1 / 0 | ETH-USD 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 3.17 | +3.60% | 9 |
| RSI momentum | TNA | 2.20 | +2.77% | 6 |
| Z-score reversion | TQQQ | 2.19 | +4.95% | 6 |
| Williams %R | TSLA | 2.15 | +8.36% | 18 |
| Gap and go | TQQQ | 1.80 | +5.84% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.89 | 17.89 | 0 | — | 15.31 | 5.11 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 3.29 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.99 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.63 | 4.63 | 0 | — | 6.58 | 1.81 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 1.00 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 2.98 | 1.86 | -4.12 | 86 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.72 | 1.89 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.33 | -1.67 | 0 | — | -0.61 | -0.13 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.89 | -3.12 | 1 | 0.0 | -3.27 | -2.15 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.69 | -3.31 | 191 | 30.4 | -3.13 | -1.09 | -8.46 | 150 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.35 | -3.65 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 94.58 | -5.42 | 145 | 46.9 | -13.91 | -3.63 | -13.91 | 152 |
| 16 | Copy: Insider buying | copy | 94.25 | -5.75 | 43 | 39.5 | -6.38 | -1.27 | -14.79 | 60 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.13 | -3.91 | -5.99 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.28 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.07 | -10.13 | 22 |
| 20 | Trend pullback · 1h | trend | 91.84 | -8.15 | 110 | 22.7 | -15.11 | -5.58 | -17.77 | 70 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.30 | -0.70 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.28 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.26 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.69 | -14.31 | 16 | 18.8 | -10.26 | -1.63 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.63 | -7.33 | -15.23 | 201 |
| 26 | Parabolic SAR · 1h | trend | 85.27 | -14.73 | 176 | 29.0 | -15.04 | -3.23 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -16.39 | -4.61 | -17.28 | 97 |
| 28 | Donchian 55/20 · 1h | breakout | 81.99 | -18.01 | 73 | 13.7 | -23.08 | -4.82 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.85 | -19.15 | 2 | 0.0 | -9.89 | -1.14 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -18.15 | -6.39 | -18.32 | 115 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -15.46 | -3.61 | -23.29 | 91 |
| 32 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.30 | -3.50 | -25.39 | 169 |
| 33 | Stochastic reversion · 1h | reversion | 79.01 | -20.99 | 309 | 46.6 | -27.45 | -4.08 | -28.07 | 408 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.71 | -21.36 | 720 |
| 35 | Hold BTC | benchmark | 77.97 | -22.02 | 1 | 0.0 | -14.93 | -2.03 | -25.41 | 1 |
| 36 | MFI reversion · 1h | reversion | 77.22 | -22.78 | 405 | 35.1 | -21.27 | -2.74 | -25.27 | 167 |
| 37 | ADX DI cross · 1h | trend | 76.53 | -23.47 | 200 | 20.0 | -23.46 | -3.48 | -32.66 | 265 |
| 38 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.59 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -23.19 | -4.84 | -30.71 | 238 |
| 41 | Max aggression: 1-day momentum | meta | 74.90 | -25.11 | 29 | 27.6 | -20.15 | -0.61 | -57.50 | 41 |
| 42 | Heikin-Ashi · 1h | trend | 74.62 | -25.38 | 445 | 24.0 | -37.14 | -6.82 | -39.47 | 661 |
| 43 | MACD zero-line · 1h | trend | 73.48 | -26.52 | 171 | 18.7 | -23.28 | -4.56 | -30.99 | 199 |
| 44 | RSI momentum · 1h | momentum | 72.60 | -27.40 | 171 | 14.0 | -26.62 | -4.07 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.54 | -27.46 | 109 | 10.1 | -28.28 | -4.78 | -40.51 | 120 |
| 46 | MACD cross · 1h | trend | 72.12 | -27.88 | 393 | 23.2 | -31.46 | -4.66 | -40.30 | 473 |
| 47 | Supertrend · 1h | trend | 71.93 | -28.07 | 182 | 14.8 | -29.23 | -4.95 | -36.83 | 206 |
| 48 | Triple EMA stack · 1h | trend | 71.63 | -28.37 | 151 | 14.6 | -27.20 | -4.46 | -38.66 | 201 |
| 49 | Bollinger reversion · 1h | reversion | 71.22 | -28.78 | 307 | 41.0 | -35.01 | -5.54 | -35.68 | 389 |
| 50 | ROC + volume · 1h | momentum | 71.18 | -28.82 | 399 | 28.8 | -30.16 | -5.43 | -37.65 | 373 |
| 51 | CCI reversion · 1h | reversion | 69.88 | -30.12 | 356 | 42.1 | -38.85 | -6.16 | -38.94 | 474 |
| 52 | OBV trend · 1h | momentum | 69.68 | -30.32 | 299 | 19.1 | -28.65 | -4.99 | -38.37 | 270 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.12 | -4.51 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.23 | -30.77 | 153 | 19.0 | -31.12 | -5.62 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 66.66 | -33.34 | 391 | 42.7 | -44.10 | -7.35 | -44.17 | 541 |
| 56 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1855 | 24.7 | -23.14 | -3.64 | -26.90 | 335 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -37.19 | -7.49 | -43.16 | 324 |
| 58 | VWAP momentum · 1h | momentum | 62.53 | -37.47 | 917 | 22.2 | -52.57 | -10.44 | -53.90 | 1234 |
| 59 | RSI(14) reversion · 1h | reversion | 61.74 | -38.26 | 194 | 31.4 | -39.32 | -5.88 | -39.61 | 241 |
| 60 | Z-score reversion · 1h | reversion | 61.50 | -38.51 | 213 | 35.7 | -32.36 | -4.53 | -33.42 | 236 |
| 61 | Candlestick reversal · 1h | reversion | 61.31 | -38.69 | 499 | 27.7 | -45.87 | -8.55 | -45.92 | 611 |
| 62 | Three white soldiers | momentum | 58.37 | -41.63 | 543 | 14.5 | -49.03 | -21.74 | -49.44 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.06 | -44.99 | -99.06 | 5345 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.20 | -25.56 | -80.78 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -45.50 | -93.73 | 2536 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.60 | -32.09 | -89.66 | 1939 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.24 | -41.42 | -91.33 | 2346 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.49 | -30.37 | -89.49 | 2176 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -52.49 | -97.91 | 3506 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -56.75 | -96.23 | 3463 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.48 | -32.45 | -93.49 | 2316 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.97 | -34.12 | -82.97 | 1652 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -55.65 | -99.60 | 6061 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.15 | -42.85 | -92.15 | 2626 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.21 | -36.23 | -95.21 | 3448 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -74.63 | -99.81 | 6172 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.39 | -43.78 | -92.42 | 2288 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.10 | -26.36 | -76.22 | 1662 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.57 | -58.77 | -97.58 | 3512 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.95 | -62.40 | -98.96 | 4959 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.70 | -27.22 | -69.01 | 1253 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -56.76 | -94.71 | 2806 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.01 | -38.72 | -85.01 | 1782 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -74.32 | -99.68 | 6384 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.61 | -32.29 | -90.74 | 2345 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.07 | -19.75 | -80.23 | 1823 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.92 | -37.37 | -91.02 | 2195 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.23 | -49.06 | -97.24 | 3906 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -57.63 | -89.35 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.62 | -29.29 | -65.73 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.28 | -22.95 | -71.51 | 1256 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.26 | -19.28 | -80.58 | 1749 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.53 | -50.41 | -97.55 | 4368 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -114.33 | -99.94 | 8471 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-14T17:25 | Three white soldiers | buy | SOL-USD | 14.58 | — | entry signal |
| 2026-11-14T17:00 | MFI reversion · 1h | buy | XRP-USD | 8.87 | — | entry signal |
| 2026-11-14T16:50 | Candlestick reversal · 1h | sell | SOL-USD | 3.74 | -0.10 | stop-loss |
| 2026-11-14T16:30 | Candlestick reversal · 1h | sell | DOGE-USD | 3.74 | -0.10 | stop-loss |
| 2026-11-14T16:25 | VWAP reversion · 1h | sell | XRP-USD | 23.11 | -0.71 | stop-loss |
| 2026-11-14T16:15 | CCI reversion · 1h | sell | XRP-USD | 3.24 | -0.11 | stop-loss |
| 2026-11-14T16:15 | Williams %R · 1h | sell | XRP-USD | 3.24 | -0.11 | stop-loss |
| 2026-11-14T16:15 | Stochastic reversion · 1h | buy | DOGE-USD | 4.64 | — | entry |
| 2026-11-14T16:15 | Stochastic reversion · 1h | sell | XRP-USD | 4.72 | -0.11 | stop-loss |
| 2026-11-14T16:15 | RSI(14) reversion · 1h | sell | XRP-USD | 15.19 | -0.37 | stop-loss |
| 2026-11-14T16:10 | CCI reversion · 1h | sell | SOL-USD | 3.79 | -0.13 | stop-loss |
| 2026-11-14T16:10 | Bollinger reversion · 1h | buy | DOGE-USD | 8.90 | — | entry |
| 2026-11-14T16:10 | Bollinger reversion · 1h | sell | SOL-USD | 8.84 | -0.08 | stop-loss |
| 2026-11-14T16:00 | Williams %R · 1h | buy | BTC-USD | 3.92 | — | entry signal |
| 2026-11-14T16:00 | Stochastic reversion · 1h | buy | BTC-USD | 3.38 | — | entry signal |
| 2026-11-14T16:00 | Candlestick reversal · 1h | buy | SOL-USD | 3.84 | — | entry signal |
| 2026-11-14T16:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.84 | — | entry signal |
| 2026-11-14T16:00 | Candlestick reversal · 1h | buy | BTC-USD | 3.84 | — | entry signal |
| 2026-11-14T15:35 | MFI reversion · 1h | sell | XRP-USD | 8.87 | -0.16 | stop-loss |
| 2026-11-14T15:35 | Z-score reversion · 1h | sell | XRP-USD | 15.25 | -0.51 | stop-loss |
| 2026-11-14T15:30 | MACD cross · 1h | sell | XRP-USD | 17.90 | -0.38 | stop-loss |
| 2026-11-14T15:25 | Bollinger reversion · 1h | buy | SOL-USD | 8.91 | — | entry |
| 2026-11-14T15:25 | Bollinger reversion · 1h | sell | XRP-USD | 8.64 | -0.31 | stop-loss |
| 2026-11-14T15:10 | MFI reversion · 1h | buy | XRP-USD | 9.03 | — | entry |
| 2026-11-14T15:10 | MFI reversion · 1h | sell | BTC-USD | 9.03 | -0.10 | stop-loss |
| 2026-11-14T15:10 | Stochastic reversion · 1h | sell | BTC-USD | 3.38 | -0.09 | stop-loss |
| 2026-11-14T15:00 | Candlestick reversal · 1h | sell | XRP-USD | 3.80 | -0.06 | exit signal |
| 2026-11-14T14:35 | MFI reversion · 1h | buy | BTC-USD | 9.13 | — | entry |
| 2026-11-14T14:35 | MFI reversion · 1h | sell | ETH-USD | 9.13 | -0.29 | stop-loss |
| 2026-11-14T14:35 | CCI reversion · 1h | sell | BTC-USD | 3.27 | -0.09 | stop-loss |
| 2026-11-14T14:35 | Williams %R · 1h | sell | SOL-USD | 2.49 | -0.09 | stop-loss |
| 2026-11-14T14:35 | Stochastic reversion · 1h | buy | XRP-USD | 4.84 | — | entry |
| 2026-11-14T14:35 | Stochastic reversion · 1h | sell | SOL-USD | 4.84 | -0.12 | stop-loss |
| 2026-11-14T14:35 | Z-score reversion · 1h | sell | SOL-USD | 15.19 | -0.53 | stop-loss |
| 2026-11-14T14:35 | Bollinger reversion · 1h | sell | DOGE-USD | 0.97 | -0.04 | stop-loss |
| 2026-11-14T14:35 | RSI(14) reversion · 1h | buy | XRP-USD | 15.55 | — | entry |
| 2026-11-14T14:35 | RSI(14) reversion · 1h | sell | SOL-USD | 4.84 | -0.16 | stop-loss |
| 2026-11-14T14:35 | RSI(14) reversion · 1h | sell | ETH-USD | 10.23 | -0.33 | stop-loss |
| 2026-11-14T14:35 | RSI(14) reversion · 1h | sell | DOGE-USD | 10.17 | -0.38 | stop-loss |
| 2026-11-14T14:35 | RSI(14) reversion · 1h | sell | BTC-USD | 8.80 | -0.20 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-16 17:40:05.000161+00:00 -> 2026-11-14 17:50:05.000161+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
