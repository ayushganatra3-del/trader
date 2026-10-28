# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T01:00:05.000130+00:00 · 38474 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.98 (-10.02%)

Closed trades 116, win rate 38.8%, fees £3.50, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-27 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.91 · VIX 17.52 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 780 decisions in 156 calls, $0.0109 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T01:00 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-10-28T01:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T01:00 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.31 | +6.31% | 11 |
| MACD zero-line | MSFT | 2.19 | +0.66% | 5 |
| VWAP momentum · 1h | LABU | 2.05 | +21.96% | 3 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.14 | 7.14 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.15 | 1.15 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.19 | -3.65 | -14.07 | 148 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.60 | -0.40 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 6.76 | 3.22 | -2.11 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.76 | -2.24 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.39 | -3.61 | 123 | 31.7 | -4.47 | -2.47 | -7.67 | 186 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.04 | -3.96 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 16 | Hold BTC | benchmark | 95.90 | -4.10 | 0 | — | 1.84 | 0.47 | -9.28 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.39 | -2.90 | -4.59 | 28 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.14 | 1.68 | -8.76 | 203 |
| 20 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 21 | Donchian 55/20 · 1h | breakout | 93.61 | -6.39 | 49 | 16.3 | -13.05 | -2.90 | -15.40 | 99 |
| 22 | Trend pullback · 1h | trend | 93.46 | -6.54 | 96 | 22.9 | -23.23 | -7.38 | -23.27 | 113 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.61 | -7.39 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 24 | Parabolic SAR · 1h | trend | 92.59 | -7.41 | 121 | 25.6 | -20.08 | -4.90 | -23.02 | 248 |
| 25 | Daily: Momentum burst | daily | 91.97 | -8.03 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 26 | ADX DI cross · 1h | trend | 91.97 | -8.03 | 120 | 18.3 | -14.09 | -3.04 | -15.88 | 271 |
| 27 | Copy: Insider buying | copy | 91.87 | -8.13 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.35 | -8.65 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.26 | -8.74 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 91.02 | -8.98 | 52 | 23.1 | -4.51 | -1.17 | -12.21 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.33 | -9.67 | 112 | 26.8 | -11.79 | -2.42 | -15.94 | 112 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.02 | -6.38 | -12.20 | 209 |
| 34 | Bollinger breakout · 1h | breakout | 88.99 | -11.01 | 109 | 26.6 | -11.30 | -2.19 | -18.15 | 246 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.62 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.88 | -12.12 | 205 | 47.3 | -20.83 | -3.84 | -22.35 | 389 |
| 37 | Keltner breakout · 1h | breakout | 87.35 | -12.65 | 74 | 23.0 | -18.84 | -3.60 | -23.13 | 186 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.01 | -12.98 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 85.88 | -14.12 | 114 | 14.0 | -23.68 | -4.78 | -26.59 | 230 |
| 41 | RSI momentum · 1h | momentum | 85.18 | -14.82 | 104 | 15.4 | -23.94 | -4.76 | -26.87 | 211 |
| 42 | Connors RSI(2) · 1h | reversion | 85.16 | -14.84 | 176 | 40.9 | -23.72 | -7.42 | -24.36 | 179 |
| 43 | EMA 20/50 cross · 1h | trend | 84.55 | -15.45 | 73 | 11.0 | -22.65 | -4.60 | -24.49 | 136 |
| 44 | MACD cross · 1h | trend | 84.40 | -15.60 | 244 | 22.1 | -27.69 | -5.37 | -29.94 | 476 |
| 45 | Ichimoku · 1h | trend | 84.14 | -15.86 | 68 | 11.8 | -19.83 | -4.02 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.74 | -16.26 | 101 | 14.9 | -28.19 | -5.34 | -31.19 | 204 |
| 47 | MFI reversion · 1h | reversion | 83.50 | -16.50 | 274 | 32.1 | -16.03 | -2.47 | -20.70 | 153 |
| 48 | CCI reversion · 1h | reversion | 82.61 | -17.39 | 230 | 45.2 | -24.12 | -3.44 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 82.18 | -17.82 | 99 | 20.2 | -22.93 | -4.33 | -26.02 | 219 |
| 50 | Williams %R · 1h | reversion | 82.16 | -17.84 | 232 | 47.0 | -34.98 | -5.89 | -36.03 | 537 |
| 51 | MACD zero-line · 1h | trend | 81.38 | -18.62 | 111 | 15.3 | -24.22 | -5.18 | -25.67 | 230 |
| 52 | Agent (ML meta-label) | meta | 80.86 | -19.14 | 982 | 20.6 | -9.66 | -1.74 | -17.42 | 338 |
| 53 | Bollinger reversion · 1h | reversion | 80.85 | -19.15 | 182 | 37.4 | -29.08 | -5.94 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.70 | -19.30 | 209 | 17.7 | -31.40 | -6.44 | -33.78 | 294 |
| 55 | RSI(14) reversion · 1h | reversion | 80.43 | -19.57 | 107 | 27.1 | -15.29 | -2.82 | -24.48 | 186 |
| 56 | ROC + volume · 1h | momentum | 79.38 | -20.62 | 259 | 25.9 | -29.81 | -5.65 | -32.05 | 379 |
| 57 | Heikin-Ashi · 1h | trend | 78.44 | -21.56 | 301 | 22.6 | -42.99 | -9.43 | -44.66 | 666 |
| 58 | Candlestick reversal · 1h | reversion | 77.44 | -22.56 | 285 | 29.5 | -36.35 | -7.40 | -37.17 | 544 |
| 59 | VWAP momentum · 1h | momentum | 77.11 | -22.89 | 578 | 22.7 | -49.49 | -10.76 | -51.28 | 1237 |
| 60 | Three white soldiers | momentum | 76.92 | -23.08 | 326 | 19.0 | -45.06 | -21.00 | -45.09 | 608 |
| 61 | EMA 9/21 cross · 1h | trend | 76.79 | -23.21 | 176 | 10.8 | -29.62 | -6.24 | -31.61 | 337 |
| 62 | Max aggression: 1-day momentum | meta | 72.60 | -27.40 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 53.17 | -46.83 | 816 | 22.2 | -74.86 | -26.66 | -75.09 | 1568 |
| 64 | Volume breakout | breakout | 51.79 | -48.21 | 491 | 12.6 | -63.74 | -25.75 | -64.24 | 809 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -43.18 | -98.85 | 5123 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.89 | -23.02 | -79.67 | 1415 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.58 | -44.30 | -93.72 | 2529 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.96 | -29.38 | -89.25 | 1918 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.46 | -37.17 | -91.61 | 2342 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.41 | -31.82 | -90.41 | 2195 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -52.32 | -97.89 | 3514 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.13 | -56.41 | -96.20 | 3379 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.01 | -35.84 | -94.01 | 2463 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.17 | -33.22 | -82.47 | 1689 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.27 | -99.42 | 5755 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -42.13 | -93.13 | 2635 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -38.81 | -95.43 | 3390 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.17 | -99.78 | 6174 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -43.58 | -92.42 | 2318 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -61.51 | -97.82 | 3592 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -57.01 | -98.65 | 4789 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.84 | -29.13 | -68.94 | 1183 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -54.44 | -94.72 | 2775 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.58 | -38.31 | -84.64 | 1810 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -63.40 | -99.61 | 6296 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.25 | -28.67 | -88.27 | 2225 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.38 | -18.71 | -76.79 | 1679 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.56 | -36.56 | -90.57 | 2269 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.25 | -46.71 | -96.26 | 3813 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.08 | -48.06 | -90.08 | 2130 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.07 | -24.61 | -73.53 | 1279 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.19 | -17.91 | -76.49 | 1572 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.53 | -47.92 | -96.53 | 4191 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -92.35 | -99.92 | 8286 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | XRP-USD | 6.47 | 0.09 | exit signal |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | ETH-USD | 5.45 | 0.02 | exit signal |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | BTC-USD | 2.95 | 0.01 | exit signal |
| 2026-10-28T01:00 | Heikin-Ashi · 1h | sell | BTC-USD | 3.90 | -0.02 | exit signal |
| 2026-10-28T00:20 | ROC + volume | sell | DOGE-USD | 13.22 | -0.14 | stop-loss |
| 2026-10-28T00:05 | ROC + volume | sell | XRP-USD | 13.22 | -0.14 | stop-loss |
| 2026-10-28T00:00 | Donchian 55/20 · 1h | buy | XRP-USD | 3.96 | — | entry signal |
| 2026-10-28T00:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 18.74 | — | entry signal |
| 2026-10-27T23:50 | ROC + volume | buy | XRP-USD | 13.36 | — | entry signal |
| 2026-10-27T23:50 | ROC + volume | buy | DOGE-USD | 13.36 | — | entry signal |
| 2026-10-27T22:25 | Volume breakout | sell | XRP-USD | 12.96 | -0.11 | exit signal |
| 2026-10-27T22:00 | Triple EMA stack · 1h | buy | BTC-USD | 4.60 | — | entry |
| 2026-10-27T22:00 | Triple EMA stack · 1h | sell | XRP-USD | 4.60 | 0.08 | rebalance down |
| 2026-10-27T22:00 | Volume breakout | sell | SOL-USD | 12.94 | -0.13 | stop-loss |
| 2026-10-27T22:00 | Volume breakout | sell | ETH-USD | 12.94 | -0.13 | stop-loss |
| 2026-10-27T22:00 | ROC + volume | sell | SOL-USD | 13.33 | -0.13 | stop-loss |
| 2026-10-27T22:00 | ROC + volume | sell | ETH-USD | 13.33 | -0.13 | stop-loss |
| 2026-10-27T21:45 | Volume breakout | sell | BTC-USD | 12.95 | -0.12 | stop-loss |
| 2026-10-27T21:45 | ROC + volume | sell | BTC-USD | 13.34 | -0.12 | stop-loss |
| 2026-10-27T21:35 | Volume breakout | buy | XRP-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | Volume breakout | buy | SOL-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | Volume breakout | buy | ETH-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | Volume breakout | buy | BTC-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | ROC + volume | buy | SOL-USD | 13.46 | — | entry signal |
| 2026-10-27T21:35 | ROC + volume | buy | ETH-USD | 13.46 | — | entry signal |
| 2026-10-27T21:35 | ROC + volume | buy | BTC-USD | 13.46 | — | entry signal |
| 2026-10-27T21:00 | Heikin-Ashi · 1h | sell | XRP-USD | 4.32 | -0.03 | exit signal |
| 2026-10-27T21:00 | Heikin-Ashi · 1h | sell | ETH-USD | 1.35 | -0.01 | exit signal |
| 2026-10-27T20:20 | Three white soldiers | sell | SOL-USD | 19.16 | -0.12 | exit signal |
| 2026-10-27T20:15 | Three white soldiers | sell | ETH-USD | 19.20 | -0.15 | exit signal |
| 2026-10-27T20:00 | OBV trend · 1h | buy | BTC-USD | 7.33 | — | entry signal |
| 2026-10-27T20:00 | OBV trend · 1h | sell | XRP-USD | 4.13 | 0.02 | rebalance down |
| 2026-10-27T20:00 | OBV trend · 1h | sell | DOGE-USD | 4.14 | -0.00 | rebalance down |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 2.04 | — | entry signal |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 10.56 | — | entry signal |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 6.30 | 0.09 | rebalance down |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 6.29 | 0.00 | rebalance down |
| 2026-10-27T20:00 | Three white soldiers | buy | SOL-USD | 19.28 | — | entry |
| 2026-10-27T19:55 | Agent (rotation) | sell | TQQQ | 32.22 | 0.12 | selected signal exited |
| 2026-10-27T19:55 | Day trade: Stocks in Play ORB | sell | TSLA | 24.98 | 0.40 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 01:00:05.000130+00:00 -> 2026-10-28 01:10:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
