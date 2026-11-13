# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T08:10:05.000149+00:00 · 57953 ticks

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

Today: 6570 decisions in 1314 calls, $0.0921 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T08:10 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-13T08:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-13T08:10 | 4 / 1 / 0 | ETH-USD 53% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.02 | 17.02 | 0 | — | 14.68 | 4.92 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.62 | 12.62 | 22 | 68.2 | 16.23 | 3.32 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.73 | 11.73 | 34 | 29.4 | 20.04 | 2.99 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.98 | 3.98 | 0 | — | 6.13 | 1.70 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.73 | 0.73 | 140 | 35.0 | 7.14 | 2.82 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.44 | 1.84 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.51 | -1.49 | 0 | — | -0.22 | 0.00 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.86 | -2.14 | 1 | 0.0 | -2.09 | -1.43 | -5.83 | 2 |
| 13 | Agent (rotation) | meta | 97.84 | -2.16 | 191 | 30.4 | -0.44 | -0.09 | -8.69 | 158 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.05 | -3.95 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 95.00 | -5.00 | 43 | 39.5 | -4.17 | -0.75 | -14.81 | 66 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.07 | -5.93 | 0 | — | -4.23 | -1.12 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 93.19 | -6.81 | 1 | 0.0 | -7.08 | -1.56 | -16.91 | 2 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 21 | Trend pullback · 1h | trend | 91.75 | -8.25 | 110 | 22.7 | -13.06 | -4.54 | -17.58 | 73 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Parabolic SAR · 1h | trend | 85.98 | -14.02 | 171 | 27.5 | -14.92 | -3.21 | -21.80 | 217 |
| 24 | Opening range 30m | breakout | 85.89 | -14.11 | 433 | 33.3 | -10.11 | -3.19 | -14.11 | 601 |
| 25 | Agent | meta | 85.55 | -14.45 | 190 | 35.3 | -15.04 | -7.57 | -15.21 | 210 |
| 26 | Daily: Bullish score | daily | 84.73 | -15.27 | 16 | 18.8 | -11.13 | -1.80 | -19.56 | 15 |
| 27 | Donchian 55/20 · 1h | breakout | 83.95 | -16.05 | 73 | 13.7 | -22.90 | -4.82 | -29.68 | 94 |
| 28 | Agent (aggressive) | meta | 83.73 | -16.27 | 92 | 33.7 | -17.67 | -4.98 | -18.51 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 82.34 | -17.66 | 2 | 0.0 | -8.05 | -0.88 | -24.16 | 1 |
| 30 | Keltner breakout · 1h | breakout | 81.66 | -18.34 | 114 | 23.7 | -15.25 | -3.04 | -25.14 | 169 |
| 31 | Max aggression: 5-day momentum | meta | 81.45 | -18.55 | 20 | 45.0 | -32.68 | -1.99 | -45.81 | 22 |
| 32 | ADX DI cross · 1h | trend | 81.41 | -18.59 | 192 | 19.3 | -19.96 | -3.05 | -29.51 | 270 |
| 33 | Hold BTC | benchmark | 81.03 | -18.97 | 1 | 0.0 | -11.41 | -1.58 | -22.00 | 1 |
| 34 | Connors RSI(2) · 1h | reversion | 80.94 | -19.06 | 210 | 40.5 | -17.80 | -6.24 | -18.30 | 114 |
| 35 | Volume breakout · 1h | breakout | 80.15 | -19.85 | 159 | 28.3 | -13.17 | -3.05 | -22.12 | 90 |
| 36 | Stochastic reversion · 1h | reversion | 79.33 | -20.67 | 298 | 47.3 | -26.56 | -3.92 | -27.61 | 390 |
| 37 | MFI reversion · 1h | reversion | 78.85 | -21.15 | 390 | 35.4 | -19.21 | -2.46 | -23.02 | 161 |
| 38 | Opening range 15m | breakout | 78.23 | -21.77 | 524 | 31.3 | -17.52 | -4.71 | -21.36 | 715 |
| 39 | Heikin-Ashi · 1h | trend | 77.08 | -22.92 | 437 | 24.5 | -36.24 | -6.77 | -38.20 | 656 |
| 40 | MACD cross · 1h | trend | 76.85 | -23.15 | 377 | 23.1 | -26.85 | -3.96 | -38.65 | 468 |
| 41 | Bollinger breakout · 1h | breakout | 76.61 | -23.39 | 179 | 22.3 | -20.88 | -4.31 | -29.92 | 239 |
| 42 | Max aggression: 1-day momentum | meta | 76.00 | -24.00 | 29 | 27.6 | -15.60 | -0.34 | -57.50 | 40 |
| 43 | MACD zero-line · 1h | trend | 75.78 | -24.22 | 168 | 17.9 | -21.66 | -4.23 | -30.99 | 204 |
| 44 | Supertrend · 1h | trend | 75.55 | -24.45 | 172 | 14.0 | -27.75 | -4.76 | -36.51 | 212 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 46 | RSI momentum · 1h | momentum | 75.06 | -24.94 | 162 | 13.6 | -24.33 | -3.77 | -36.35 | 211 |
| 47 | EMA 20/50 cross · 1h | trend | 74.72 | -25.28 | 105 | 10.5 | -26.89 | -4.56 | -38.62 | 122 |
| 48 | Daily: Momentum burst | daily | 74.14 | -25.86 | 27 | 11.1 | -30.29 | -4.08 | -36.97 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.44 | -26.56 | 147 | 14.3 | -26.57 | -4.36 | -37.19 | 205 |
| 50 | ROC + volume · 1h | momentum | 72.91 | -27.09 | 390 | 28.7 | -29.37 | -5.36 | -38.32 | 374 |
| 51 | Donchian 20/10 · 1h | breakout | 72.17 | -27.83 | 145 | 19.3 | -27.07 | -4.89 | -35.90 | 209 |
| 52 | Bollinger reversion · 1h | reversion | 71.79 | -28.21 | 295 | 41.0 | -32.37 | -5.03 | -35.72 | 381 |
| 53 | OBV trend · 1h | momentum | 71.63 | -28.36 | 290 | 19.3 | -27.78 | -4.84 | -36.71 | 275 |
| 54 | CCI reversion · 1h | reversion | 71.18 | -28.82 | 345 | 43.5 | -37.30 | -5.87 | -37.63 | 459 |
| 55 | Williams %R · 1h | reversion | 67.38 | -32.62 | 377 | 43.2 | -42.33 | -6.96 | -42.63 | 532 |
| 56 | EMA 9/21 cross · 1h | trend | 67.27 | -32.73 | 259 | 10.0 | -35.12 | -7.20 | -41.97 | 329 |
| 57 | Z-score reversion · 1h | reversion | 66.22 | -33.78 | 203 | 37.4 | -29.66 | -4.20 | -29.95 | 234 |
| 58 | Agent (ML meta-label) | meta | 66.15 | -33.85 | 1820 | 24.8 | -15.68 | -2.31 | -24.54 | 346 |
| 59 | VWAP momentum · 1h | momentum | 65.98 | -34.02 | 899 | 22.2 | -50.95 | -10.34 | -51.23 | 1222 |
| 60 | RSI(14) reversion · 1h | reversion | 63.62 | -36.38 | 183 | 31.7 | -36.21 | -5.34 | -36.57 | 236 |
| 61 | Candlestick reversal · 1h | reversion | 62.31 | -37.69 | 476 | 28.2 | -43.89 | -8.08 | -44.30 | 590 |
| 62 | Three white soldiers | momentum | 58.43 | -41.57 | 541 | 14.6 | -49.60 | -22.18 | -49.68 | 665 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.43 | -99.01 | 5270 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.86 | -25.28 | -79.92 | 1409 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.78 | -44.97 | -93.79 | 2528 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.27 | -31.29 | -89.37 | 1917 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.25 | -40.30 | -91.29 | 2333 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.71 | -30.83 | -89.75 | 2191 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -50.39 | -97.89 | 3476 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -54.56 | -96.24 | 3431 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.57 | -32.83 | -93.57 | 2334 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.17 | -34.34 | -83.17 | 1655 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -54.99 | -99.59 | 6011 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.33 | -42.77 | -92.33 | 2610 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.31 | -36.31 | -95.31 | 3461 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -69.82 | -99.82 | 6144 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.30 | -42.30 | -92.30 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.48 | -25.44 | -75.53 | 1626 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -57.93 | -97.63 | 3503 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.90 | -63.21 | -98.90 | 4924 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.76 | -26.65 | -68.84 | 1235 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -55.10 | -94.79 | 2783 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.07 | -38.59 | -85.09 | 1781 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -75.35 | -99.67 | 6356 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.23 | -32.54 | -90.26 | 2311 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.72 | -20.15 | -78.83 | 1779 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.72 | -36.26 | -90.77 | 2174 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.01 | -52.76 | -97.01 | 3872 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -56.56 | -89.37 | 2137 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.91 | -29.36 | -66.06 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.38 | -22.81 | -71.42 | 1252 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.20 | -19.29 | -80.38 | 1730 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.38 | -50.18 | -97.38 | 4312 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -98.25 | -99.93 | 8361 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T08:00 | CCI reversion · 1h | buy | SOL-USD | 8.89 | — | entry signal |
| 2026-11-13T08:00 | CCI reversion · 1h | buy | DOGE-USD | 8.89 | — | entry signal |
| 2026-11-13T08:00 | VWAP momentum · 1h | buy | DOGE-USD | 3.84 | — | entry signal |
| 2026-11-13T07:41 | Three white soldiers | sell | SOL-USD | 14.69 | 0.09 | exit signal |
| 2026-11-13T07:30 | Three white soldiers | sell | BTC-USD | 14.55 | -0.05 | exit signal |
| 2026-11-13T07:00 | CCI reversion · 1h | buy | XRP-USD | 11.85 | — | entry signal |
| 2026-11-13T07:00 | Williams %R · 1h | buy | SOL-USD | 4.82 | — | entry signal |
| 2026-11-13T07:00 | Williams %R · 1h | buy | ETH-USD | 4.82 | — | entry signal |
| 2026-11-13T07:00 | Williams %R · 1h | buy | DOGE-USD | 4.82 | — | entry signal |
| 2026-11-13T07:00 | Williams %R · 1h | buy | BTC-USD | 4.82 | — | entry signal |
| 2026-11-13T07:00 | Z-score reversion · 1h | buy | XRP-USD | 16.57 | — | entry signal |
| 2026-11-13T07:00 | Z-score reversion · 1h | buy | SOL-USD | 16.57 | — | entry signal |
| 2026-11-13T07:00 | Z-score reversion · 1h | buy | DOGE-USD | 16.57 | — | entry signal |
| 2026-11-13T07:00 | Bollinger reversion · 1h | buy | SOL-USD | 1.22 | — | entry signal |
| 2026-11-13T07:00 | Bollinger reversion · 1h | buy | ETH-USD | 7.18 | — | entry signal |
| 2026-11-13T07:00 | Bollinger reversion · 1h | buy | BTC-USD | 7.18 | — | entry signal |
| 2026-11-13T07:00 | RSI(14) reversion · 1h | buy | SOL-USD | 7.95 | — | entry signal |
| 2026-11-13T07:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 7.95 | — | entry signal |
| 2026-11-13T07:00 | VWAP momentum · 1h | buy | XRP-USD | 8.25 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 08:10:05.000149+00:00 -> 2026-11-13 08:20:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
