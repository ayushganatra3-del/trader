# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T23:55:05.000127+00:00 · 28897 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.38%)

Closed trades 86, win rate 39.5%, fees £2.89, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, APLD 12%, FLSC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 37689 decisions in 3420 calls, $0.4697 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T23:55 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-10-19T23:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T23:55 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |
| VWAP reversion | BITX | 1.52 | +2.60% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.86 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.09 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.16 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 105.06 | 5.06 | 0 | — | 5.36 | 2.60 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.07 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.96 | -0.04 | 0 | — | 2.38 | 1.01 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.20 | -0.80 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.05 | -3.91 | 21 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.34 | -1.66 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.06 | 1.70 | -2.17 | 63 |
| 13 | Donchian 55/20 · 1h | breakout | 97.69 | -2.31 | 36 | 16.7 | -12.62 | -2.43 | -18.86 | 101 |
| 14 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -2.15 | -0.80 | -5.10 | 288 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.40 | -2.60 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 16 | Hold BTC | benchmark | 97.39 | -2.61 | 0 | — | 26.67 | 3.19 | -8.68 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.29 | -5.83 | 1 |
| 18 | Trend pullback · 1h | trend | 96.52 | -3.48 | 88 | 23.9 | -19.69 | -5.83 | -20.58 | 137 |
| 19 | Copy: Insider buying | copy | 96.49 | -3.51 | 23 | 43.5 | -14.93 | -2.72 | -20.62 | 73 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.43 | -3.57 | 0 | — | -5.86 | -2.34 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.91 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.47 | -4.53 | 8 | 37.5 | -20.05 | -1.70 | -34.64 | 26 |
| 23 | ADX DI cross · 1h | trend | 93.68 | -6.32 | 88 | 18.2 | -14.55 | -2.67 | -16.51 | 259 |
| 24 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.54 | 2.18 | -6.51 | 199 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 92.96 | -7.04 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.04 | -7.96 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.91 | -8.10 | 78 | 23.1 | -12.73 | -2.29 | -16.76 | 107 |
| 29 | Parabolic SAR · 1h | trend | 91.77 | -8.23 | 102 | 22.5 | -14.36 | -2.74 | -24.65 | 269 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.46 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.79 | -17.26 | 557 |
| 32 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 84 | 28.6 | -8.66 | -1.46 | -16.89 | 256 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -8.04 | -4.27 | -15.29 | 255 |
| 34 | EMA 20/50 cross · 1h | trend | 90.47 | -9.53 | 58 | 13.8 | -18.96 | -3.41 | -21.31 | 126 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 90.13 | -9.87 | 0 | — | 0.78 | 0.29 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.99 | -10.02 | 79 | 16.5 | -19.92 | -3.39 | -30.20 | 212 |
| 37 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.62 | -23.86 | 205 |
| 38 | Ichimoku · 1h | trend | 88.76 | -11.24 | 55 | 14.5 | -17.48 | -3.32 | -18.08 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.33 | -11.67 | 152 | 46.1 | -17.09 | -2.98 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -4.44 | -1.11 | -15.22 | 120 |
| 41 | Keltner breakout · 1h | breakout | 87.73 | -12.27 | 56 | 23.2 | -11.96 | -1.69 | -26.96 | 201 |
| 42 | Triple EMA stack · 1h | trend | 87.66 | -12.34 | 85 | 15.3 | -23.36 | -3.63 | -32.98 | 232 |
| 43 | Supertrend · 1h | trend | 87.56 | -12.44 | 86 | 12.8 | -22.75 | -4.69 | -26.48 | 214 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.72 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 86.05 | -13.96 | 189 | 20.6 | -27.87 | -5.45 | -32.78 | 469 |
| 46 | OBV trend · 1h | momentum | 85.47 | -14.53 | 180 | 17.8 | -25.49 | -3.66 | -35.99 | 313 |
| 47 | Z-score reversion · 1h | reversion | 85.24 | -14.76 | 91 | 30.8 | -14.19 | -2.35 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.79 | -15.21 | 209 | 31.1 | -17.02 | -2.67 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.24 | -15.76 | 87 | 14.9 | -24.79 | -4.93 | -25.19 | 217 |
| 50 | Donchian 20/10 · 1h | breakout | 84.03 | -15.97 | 81 | 17.3 | -8.00 | -0.83 | -27.92 | 214 |
| 51 | Agent (ML meta-label) | meta | 83.89 | -16.11 | 681 | 18.8 | -5.14 | -0.78 | -15.56 | 363 |
| 52 | Bollinger reversion · 1h | reversion | 82.86 | -17.14 | 158 | 34.8 | -27.80 | -5.35 | -33.53 | 349 |
| 53 | Max aggression: 1-day momentum | meta | 82.60 | -17.40 | 15 | 33.3 | -15.83 | -0.60 | -37.31 | 42 |
| 54 | Three white soldiers | momentum | 82.29 | -17.71 | 232 | 19.0 | -47.32 | -18.81 | -47.71 | 604 |
| 55 | Williams %R · 1h | reversion | 82.04 | -17.96 | 182 | 42.9 | -33.23 | -5.32 | -36.50 | 531 |
| 56 | ROC + volume · 1h | momentum | 81.48 | -18.52 | 197 | 20.8 | -21.87 | -3.30 | -33.90 | 387 |
| 57 | CCI reversion · 1h | reversion | 80.73 | -19.27 | 163 | 39.3 | -17.86 | -2.25 | -27.44 | 442 |
| 58 | EMA 9/21 cross · 1h | trend | 80.28 | -19.71 | 135 | 11.1 | -29.22 | -6.09 | -29.53 | 315 |
| 59 | RSI(14) reversion · 1h | reversion | 80.18 | -19.82 | 75 | 21.3 | -20.45 | -3.67 | -25.21 | 170 |
| 60 | Heikin-Ashi · 1h | trend | 78.94 | -21.05 | 224 | 21.4 | -36.53 | -6.03 | -44.82 | 683 |
| 61 | VWAP momentum · 1h | momentum | 77.97 | -22.03 | 433 | 20.8 | -43.18 | -7.64 | -48.28 | 1245 |
| 62 | Candlestick reversal · 1h | reversion | 77.15 | -22.85 | 214 | 27.6 | -36.67 | -6.61 | -37.63 | 529 |
| 63 | ROC + volume | momentum | 61.62 | -38.38 | 596 | 22.3 | -76.02 | -18.06 | -78.18 | 1732 |
| 64 | Volume breakout | breakout | 61.28 | -38.72 | 361 | 13.0 | -62.78 | -18.03 | -64.34 | 878 |
| 65 | Squeeze breakout | breakout | 59.82 | -40.18 | 473 | 14.0 | -64.18 | -20.40 | -65.94 | 1207 |
| 66 | Donchian 55/20 | breakout | 58.88 | -41.12 | 476 | 18.5 | -68.08 | -13.77 | -72.93 | 1267 |
| 67 | RSI(14) reversion | reversion | 58.17 | -41.84 | 707 | 25.2 | -74.77 | -16.80 | -75.00 | 1601 |
| 68 | EMA 20/50 cross | trend | 56.70 | -43.30 | 513 | 19.9 | -74.98 | -13.44 | -80.32 | 1422 |
| 69 | VWAP reversion | reversion | 53.65 | -46.35 | 749 | 25.2 | -71.92 | -14.92 | -72.51 | 1498 |
| 70 | Keltner breakout | breakout | 50.62 | -49.38 | 677 | 16.1 | -82.54 | -25.21 | -83.66 | 1810 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -29.29 | -98.68 | 5267 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.06 | -28.20 | -93.71 | 2563 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -85.87 | -18.71 | -88.15 | 1891 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.79 | -22.61 | -91.12 | 2346 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.03 | -26.17 | -91.10 | 2262 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -30.99 | -97.55 | 3493 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -34.08 | -96.74 | 3571 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -28.24 | -94.53 | 2515 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.97 | -24.94 | -82.94 | 1695 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.73 | -99.36 | 5731 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.91 | -23.69 | -92.03 | 2622 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.12 | -32.32 | -96.12 | 3471 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.20 | -99.74 | 6187 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.71 | -30.05 | -91.71 | 2334 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -36.42 | -97.63 | 3627 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -37.12 | -98.45 | 4687 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.72 | -32.52 | -93.99 | 2801 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.72 | -99.52 | 6155 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.71 | -22.50 | -86.78 | 2129 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.80 | -26.95 | -87.81 | 2130 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.80 | -32.73 | -95.81 | 3732 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.93 | -32.86 | -89.09 | 2095 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.68 | -33.90 | -95.68 | 4097 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.92 | -99.90 | 8281 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T23:46 | Three white soldiers | buy | DOGE-USD | 20.59 | — | entry signal |
| 2026-10-19T23:20 | Donchian 55/20 | buy | XRP-USD | 5.87 | — | rebalance up |
| 2026-10-19T23:20 | Donchian 55/20 | buy | ETH-USD | 2.96 | — | rebalance up |
| 2026-10-19T23:20 | Donchian 55/20 | buy | DOGE-USD | 2.96 | — | rebalance up |
| 2026-10-19T23:20 | Donchian 55/20 | sell | BTC-USD | 14.67 | -0.13 | stop-loss |
| 2026-10-19T23:20 | EMA 20/50 cross | buy | XRP-USD | 8.47 | — | rebalance up |
| 2026-10-19T23:20 | EMA 20/50 cross | sell | BTC-USD | 14.10 | -0.12 | stop-loss |
| 2026-10-19T23:10 | Squeeze breakout | sell | SOL-USD | 14.96 | -0.13 | stop-loss |
| 2026-10-19T23:10 | Keltner breakout | sell | SOL-USD | 10.12 | -0.09 | stop-loss |
| 2026-10-19T23:10 | ROC + volume | sell | SOL-USD | 15.34 | -0.14 | exit signal |
| 2026-10-19T23:00 | Heikin-Ashi · 1h | buy | BTC-USD | 3.85 | — | entry signal |
| 2026-10-19T23:00 | Parabolic SAR · 1h | buy | SOL-USD | 22.80 | — | entry signal |
| 2026-10-19T23:00 | Parabolic SAR · 1h | buy | DOGE-USD | 22.97 | — | entry signal |
| 2026-10-19T23:00 | Squeeze breakout | sell | DOGE-USD | 11.98 | -0.07 | stop-loss |
| 2026-10-19T23:00 | Keltner breakout | sell | DOGE-USD | 10.13 | -0.09 | stop-loss |
| 2026-10-19T23:00 | ROC + volume | sell | DOGE-USD | 15.32 | -0.16 | stop-loss |
| 2026-10-19T22:36 | Three white soldiers | sell | SOL-USD | 20.47 | -0.17 | exit signal |
| 2026-10-19T22:36 | Volume breakout | sell | SOL-USD | 15.29 | -0.09 | exit signal |
| 2026-10-19T22:36 | Volume breakout | sell | ETH-USD | 15.25 | -0.12 | exit signal |
| 2026-10-19T22:36 | Squeeze breakout | sell | ETH-USD | 14.95 | -0.11 | stop-loss |
| 2026-10-19T22:36 | Squeeze breakout | sell | BTC-USD | 14.95 | -0.10 | stop-loss |
| 2026-10-19T22:36 | Keltner breakout | sell | ETH-USD | 12.65 | -0.12 | stop-loss |
| 2026-10-19T22:36 | Keltner breakout | sell | BTC-USD | 10.14 | -0.08 | stop-loss |
| 2026-10-19T22:30 | Squeeze breakout | buy | BTC-USD | 12.00 | — | rebalance up |
| 2026-10-19T22:30 | Squeeze breakout | sell | XRP-USD | 14.97 | -0.11 | stop-loss |
| 2026-10-19T22:30 | Keltner breakout | buy | ETH-USD | 2.55 | — | rebalance up |
| 2026-10-19T22:30 | Keltner breakout | sell | XRP-USD | 10.12 | -0.10 | stop-loss |
| 2026-10-19T22:22 | Keltner breakout | buy | XRP-USD | 5.10 | — | rebalance up |
| 2026-10-19T22:22 | Keltner breakout | sell | SOL-USD | 2.56 | -0.01 | rebalance down |
| 2026-10-19T22:22 | Keltner breakout | sell | DOGE-USD | 2.55 | -0.01 | rebalance down |
| 2026-10-19T22:20 | Squeeze breakout | buy | BTC-USD | 3.05 | — | entry signal |
| 2026-10-19T22:20 | Squeeze breakout | sell | DOGE-USD | 3.03 | -0.00 | rebalance down |
| 2026-10-19T22:20 | Keltner breakout | buy | XRP-USD | 5.12 | — | entry signal |
| 2026-10-19T22:20 | Keltner breakout | buy | ETH-USD | 10.22 | — | entry signal |
| 2026-10-19T22:20 | Keltner breakout | buy | BTC-USD | 10.22 | — | entry signal |
| 2026-10-19T22:20 | ROC + volume | buy | DOGE-USD | 15.48 | — | entry signal |
| 2026-10-19T22:15 | Squeeze breakout | buy | ETH-USD | 15.07 | — | entry signal |
| 2026-10-19T22:12 | Donchian 55/20 | buy | XRP-USD | 2.95 | — | rebalance up |
| 2026-10-19T22:12 | Donchian 55/20 | sell | DOGE-USD | 2.95 | -0.01 | rebalance down |
| 2026-10-19T22:10 | VWAP reversion | sell | ETH-USD | 10.77 | 0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 23:55:05.000127+00:00 -> 2026-10-20 00:05:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
