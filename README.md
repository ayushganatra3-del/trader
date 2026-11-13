# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T05:40:05.000144+00:00 · 57820 ticks

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

Today: 4575 decisions in 915 calls, $0.0642 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T05:40 | 4 / 1 / 0 | cash |  |
| Breezy | 2026-11-13T05:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-13T05:40 | 3 / 2 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Gap and go | UPRO | 1.59 | +2.90% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.04 | 17.04 | 0 | — | 14.68 | 4.92 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.62 | 12.62 | 22 | 68.2 | 16.23 | 3.32 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.73 | 11.73 | 34 | 29.4 | 20.04 | 2.99 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.99 | 4.00 | 0 | — | 6.13 | 1.70 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.73 | 0.73 | 140 | 35.0 | 7.31 | 2.89 | -3.96 | 88 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.58 | 1.87 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.53 | -1.47 | 0 | — | -0.22 | 0.00 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.89 | -2.12 | 1 | 0.0 | -2.09 | -1.42 | -5.83 | 2 |
| 13 | Agent (rotation) | meta | 97.84 | -2.16 | 191 | 30.4 | -0.60 | -0.16 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.07 | -3.93 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.93 | -3.36 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 95.01 | -4.99 | 43 | 39.5 | -4.17 | -0.75 | -14.81 | 66 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.08 | -5.92 | 0 | — | -4.23 | -1.12 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 93.21 | -6.79 | 1 | 0.0 | -7.08 | -1.56 | -16.91 | 2 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 21 | Trend pullback · 1h | trend | 91.76 | -8.24 | 110 | 22.7 | -13.08 | -4.55 | -17.58 | 73 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Parabolic SAR · 1h | trend | 86.00 | -14.00 | 171 | 27.5 | -14.92 | -3.21 | -21.80 | 217 |
| 24 | Opening range 30m | breakout | 85.89 | -14.11 | 433 | 33.3 | -10.12 | -3.20 | -14.11 | 601 |
| 25 | Agent | meta | 85.55 | -14.45 | 190 | 35.3 | -15.04 | -7.57 | -15.21 | 210 |
| 26 | Daily: Bullish score | daily | 84.74 | -15.26 | 16 | 18.8 | -11.13 | -1.80 | -19.56 | 15 |
| 27 | Donchian 55/20 · 1h | breakout | 83.96 | -16.04 | 73 | 13.7 | -22.89 | -4.82 | -29.68 | 94 |
| 28 | Agent (aggressive) | meta | 83.73 | -16.27 | 92 | 33.7 | -17.67 | -4.98 | -18.51 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 82.35 | -17.65 | 2 | 0.0 | -8.05 | -0.88 | -24.16 | 1 |
| 30 | Keltner breakout · 1h | breakout | 81.68 | -18.32 | 114 | 23.7 | -15.55 | -3.11 | -25.14 | 170 |
| 31 | Max aggression: 5-day momentum | meta | 81.45 | -18.55 | 20 | 45.0 | -32.68 | -1.99 | -45.81 | 22 |
| 32 | ADX DI cross · 1h | trend | 81.42 | -18.58 | 192 | 19.3 | -19.71 | -3.00 | -29.51 | 269 |
| 33 | Connors RSI(2) · 1h | reversion | 80.95 | -19.05 | 210 | 40.5 | -17.80 | -6.24 | -18.30 | 114 |
| 34 | Hold BTC | benchmark | 80.77 | -19.23 | 1 | 0.0 | -11.67 | -1.62 | -21.59 | 1 |
| 35 | Volume breakout · 1h | breakout | 80.16 | -19.84 | 159 | 28.3 | -13.17 | -3.05 | -22.12 | 90 |
| 36 | Stochastic reversion · 1h | reversion | 79.24 | -20.76 | 298 | 47.3 | -26.82 | -3.96 | -27.52 | 387 |
| 37 | MFI reversion · 1h | reversion | 78.85 | -21.15 | 390 | 35.4 | -20.03 | -2.61 | -23.43 | 161 |
| 38 | Opening range 15m | breakout | 78.23 | -21.77 | 524 | 31.3 | -17.52 | -4.71 | -21.36 | 715 |
| 39 | Heikin-Ashi · 1h | trend | 77.08 | -22.92 | 437 | 24.5 | -36.24 | -6.77 | -38.20 | 656 |
| 40 | MACD cross · 1h | trend | 76.86 | -23.14 | 377 | 23.1 | -28.31 | -4.22 | -38.65 | 473 |
| 41 | Bollinger breakout · 1h | breakout | 76.62 | -23.38 | 179 | 22.3 | -20.87 | -4.31 | -29.92 | 239 |
| 42 | Max aggression: 1-day momentum | meta | 76.00 | -24.00 | 29 | 27.6 | -15.60 | -0.34 | -57.50 | 40 |
| 43 | MACD zero-line · 1h | trend | 75.79 | -24.21 | 168 | 17.9 | -21.64 | -4.22 | -30.99 | 204 |
| 44 | Supertrend · 1h | trend | 75.56 | -24.44 | 172 | 14.0 | -27.73 | -4.75 | -36.51 | 212 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.16 | -8.87 | -31.80 | 116 |
| 46 | RSI momentum · 1h | momentum | 75.07 | -24.93 | 162 | 13.6 | -24.61 | -3.82 | -36.35 | 212 |
| 47 | EMA 20/50 cross · 1h | trend | 74.73 | -25.27 | 105 | 10.5 | -26.92 | -4.57 | -38.62 | 122 |
| 48 | Daily: Momentum burst | daily | 74.15 | -25.85 | 27 | 11.1 | -30.29 | -4.08 | -36.97 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.45 | -26.55 | 147 | 14.3 | -26.30 | -4.30 | -37.19 | 205 |
| 50 | ROC + volume · 1h | momentum | 72.93 | -27.07 | 390 | 28.7 | -29.63 | -5.42 | -38.37 | 374 |
| 51 | Donchian 20/10 · 1h | breakout | 72.18 | -27.82 | 145 | 19.3 | -27.07 | -4.89 | -35.90 | 209 |
| 52 | OBV trend · 1h | momentum | 71.65 | -28.35 | 290 | 19.3 | -27.38 | -4.75 | -36.64 | 275 |
| 53 | Bollinger reversion · 1h | reversion | 71.63 | -28.37 | 295 | 41.0 | -32.46 | -5.05 | -35.72 | 376 |
| 54 | CCI reversion · 1h | reversion | 71.13 | -28.87 | 345 | 43.5 | -37.59 | -5.94 | -37.82 | 456 |
| 55 | Williams %R · 1h | reversion | 67.36 | -32.64 | 377 | 43.2 | -42.52 | -6.94 | -42.80 | 529 |
| 56 | EMA 9/21 cross · 1h | trend | 67.28 | -32.72 | 259 | 10.0 | -35.39 | -7.27 | -41.97 | 331 |
| 57 | Z-score reversion · 1h | reversion | 66.28 | -33.72 | 203 | 37.4 | -29.64 | -4.20 | -29.71 | 231 |
| 58 | Agent (ML meta-label) | meta | 66.16 | -33.84 | 1820 | 24.8 | -14.94 | -1.95 | -24.47 | 337 |
| 59 | VWAP momentum · 1h | momentum | 65.96 | -34.04 | 899 | 22.2 | -50.94 | -10.37 | -51.42 | 1216 |
| 60 | RSI(14) reversion · 1h | reversion | 63.50 | -36.50 | 183 | 31.7 | -36.30 | -5.37 | -36.62 | 232 |
| 61 | Candlestick reversal · 1h | reversion | 62.03 | -37.97 | 476 | 28.2 | -44.40 | -8.17 | -44.60 | 589 |
| 62 | Three white soldiers | momentum | 58.39 | -41.61 | 539 | 14.5 | -49.71 | -22.24 | -49.71 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -43.42 | -98.98 | 5247 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.85 | -25.22 | -79.85 | 1407 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.80 | -44.66 | -93.80 | 2530 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.28 | -31.33 | -89.37 | 1912 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.32 | -40.49 | -91.32 | 2332 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.78 | -30.99 | -89.82 | 2195 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -50.67 | -97.89 | 3472 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -54.53 | -96.32 | 3444 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.58 | -32.85 | -93.58 | 2329 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.28 | -34.34 | -83.28 | 1659 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -55.00 | -99.59 | 6006 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.32 | -42.59 | -92.32 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.31 | -36.23 | -95.31 | 3460 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -70.95 | -99.82 | 6152 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -41.88 | -92.30 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.51 | -25.46 | -75.51 | 1625 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -58.18 | -97.65 | 3508 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.89 | -63.01 | -98.89 | 4923 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.90 | -26.76 | -68.92 | 1235 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.82 | -55.42 | -94.83 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.11 | -38.29 | -85.11 | 1782 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -74.69 | -99.67 | 6358 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.22 | -32.52 | -90.25 | 2311 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.65 | -20.16 | -78.69 | 1774 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.83 | -36.62 | -90.83 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.01 | -52.75 | -97.01 | 3870 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.26 | -53.87 | -89.26 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.09 | -29.72 | -66.11 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.54 | -22.79 | -71.55 | 1254 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.10 | -19.28 | -80.16 | 1723 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.38 | -50.00 | -97.39 | 4312 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.50 | -99.93 | 8360 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-13T03:15 | Candlestick reversal · 1h | sell | SOL-USD | 5.60 | -0.12 | stop-loss |
| 2026-11-13T03:15 | Candlestick reversal · 1h | sell | DOGE-USD | 5.59 | -0.13 | stop-loss |
| 2026-11-13T03:00 | VWAP momentum · 1h | sell | DOGE-USD | 8.11 | -0.16 | exit signal |
| 2026-11-13T02:45 | Candlestick reversal · 1h | sell | ETH-USD | 5.55 | -0.13 | stop-loss |
| 2026-11-13T02:45 | Heikin-Ashi · 1h | sell | DOGE-USD | 18.95 | -0.50 | stop-loss |
| 2026-11-13T02:15 | CCI reversion · 1h | sell | BTC-USD | 7.10 | -0.13 | stop-loss |
| 2026-11-13T02:15 | Williams %R · 1h | sell | BTC-USD | 4.77 | -0.09 | stop-loss |
| 2026-11-13T02:15 | Bollinger reversion · 1h | sell | BTC-USD | 8.88 | -0.16 | stop-loss |
| 2026-11-13T02:00 | Williams %R · 1h | sell | DOGE-USD | 4.82 | -0.04 | exit signal |
| 2026-11-13T02:00 | VWAP momentum · 1h | sell | SOL-USD | 3.98 | -0.04 | exit signal |
| 2026-11-13T02:00 | Heikin-Ashi · 1h | sell | XRP-USD | 19.26 | -0.18 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 05:40:05.000144+00:00 -> 2026-11-13 05:50:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
