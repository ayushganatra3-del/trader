# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T00:30:05.000143+00:00 · 38446 ticks

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
| Copy: Insider buying | 2026-10-27 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, PLUR 12%, RAPP 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.91 · VIX 17.52 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 360 decisions in 72 calls, $0.0051 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T00:30 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-28T00:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T00:30 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.31 | +6.31% | 11 |
| MACD zero-line | MSFT | 2.19 | +0.66% | 5 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP momentum · 1h | TSLA | 1.89 | +11.08% | 3 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.07 | 7.07 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.76 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.09 | 1.09 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.15 | -3.64 | -14.07 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.54 | -0.46 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 8.16 | 3.76 | -2.29 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.70 | -2.30 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.37 | -3.63 | 123 | 31.7 | -4.47 | -2.47 | -7.67 | 186 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 95.98 | -4.02 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 16 | Hold BTC | benchmark | 95.89 | -4.11 | 0 | — | 1.97 | 0.49 | -9.28 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 4.40 | 1.46 | -8.76 | 203 |
| 20 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 21 | Donchian 55/20 · 1h | breakout | 93.52 | -6.47 | 49 | 16.3 | -13.09 | -2.91 | -15.40 | 99 |
| 22 | Trend pullback · 1h | trend | 93.43 | -6.57 | 96 | 22.9 | -23.23 | -7.38 | -23.27 | 113 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.55 | -7.45 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 24 | Parabolic SAR · 1h | trend | 92.52 | -7.48 | 121 | 25.6 | -20.10 | -4.90 | -23.02 | 248 |
| 25 | Daily: Momentum burst | daily | 91.93 | -8.07 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 26 | ADX DI cross · 1h | trend | 91.91 | -8.09 | 120 | 18.3 | -14.11 | -3.04 | -15.89 | 271 |
| 27 | Copy: Insider buying | copy | 91.81 | -8.19 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.29 | -8.71 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 30 | Max aggression: 5-day momentum | meta | 91.21 | -8.79 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 31 | Squeeze breakout · 1h | breakout | 90.96 | -9.04 | 52 | 23.1 | -4.53 | -1.18 | -12.21 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.29 | -9.71 | 112 | 26.8 | -11.02 | -2.21 | -16.10 | 115 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.47 | -6.69 | -12.20 | 212 |
| 34 | Bollinger breakout · 1h | breakout | 88.94 | -11.06 | 109 | 26.6 | -11.31 | -2.19 | -18.15 | 246 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.18 | -3.67 | -14.77 | 97 |
| 36 | Stochastic reversion · 1h | reversion | 87.84 | -12.16 | 205 | 47.3 | -20.55 | -3.80 | -22.35 | 388 |
| 37 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 38 | Keltner breakout · 1h | breakout | 87.30 | -12.70 | 74 | 23.0 | -18.84 | -3.60 | -23.13 | 186 |
| 39 | Z-score reversion · 1h | reversion | 86.98 | -13.02 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 85.82 | -14.18 | 114 | 14.0 | -23.68 | -4.79 | -26.59 | 230 |
| 41 | Connors RSI(2) · 1h | reversion | 85.14 | -14.86 | 176 | 40.9 | -23.72 | -7.42 | -24.36 | 179 |
| 42 | RSI momentum · 1h | momentum | 85.12 | -14.88 | 104 | 15.4 | -23.95 | -4.76 | -26.87 | 211 |
| 43 | EMA 20/50 cross · 1h | trend | 84.48 | -15.52 | 73 | 11.0 | -22.67 | -4.60 | -24.49 | 136 |
| 44 | MACD cross · 1h | trend | 84.35 | -15.65 | 244 | 22.1 | -27.70 | -5.37 | -29.94 | 476 |
| 45 | Ichimoku · 1h | trend | 84.09 | -15.91 | 68 | 11.8 | -19.84 | -4.02 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.68 | -16.32 | 101 | 14.9 | -28.21 | -5.35 | -31.19 | 204 |
| 47 | MFI reversion · 1h | reversion | 83.48 | -16.52 | 274 | 32.1 | -16.32 | -2.52 | -20.70 | 154 |
| 48 | CCI reversion · 1h | reversion | 82.56 | -17.43 | 230 | 45.2 | -24.25 | -3.45 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 82.11 | -17.89 | 99 | 20.2 | -22.94 | -4.33 | -26.02 | 219 |
| 50 | Williams %R · 1h | reversion | 82.11 | -17.89 | 232 | 47.0 | -34.88 | -5.88 | -35.94 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.33 | -18.67 | 111 | 15.3 | -24.21 | -5.18 | -25.67 | 230 |
| 52 | Agent (ML meta-label) | meta | 80.81 | -19.18 | 982 | 20.6 | -8.33 | -1.49 | -17.71 | 342 |
| 53 | Bollinger reversion · 1h | reversion | 80.81 | -19.19 | 182 | 37.4 | -29.08 | -5.94 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.64 | -19.36 | 209 | 17.7 | -31.45 | -6.45 | -33.82 | 294 |
| 55 | RSI(14) reversion · 1h | reversion | 80.39 | -19.61 | 107 | 27.1 | -15.29 | -2.82 | -24.48 | 186 |
| 56 | ROC + volume · 1h | momentum | 79.33 | -20.66 | 259 | 25.9 | -29.98 | -5.72 | -31.96 | 382 |
| 57 | Heikin-Ashi · 1h | trend | 78.41 | -21.59 | 300 | 22.7 | -42.98 | -9.42 | -44.66 | 666 |
| 58 | Candlestick reversal · 1h | reversion | 77.39 | -22.61 | 285 | 29.5 | -36.23 | -7.36 | -37.11 | 543 |
| 59 | VWAP momentum · 1h | momentum | 77.10 | -22.90 | 575 | 22.3 | -49.34 | -10.69 | -51.17 | 1239 |
| 60 | Three white soldiers | momentum | 76.92 | -23.08 | 326 | 19.0 | -44.98 | -20.95 | -45.01 | 608 |
| 61 | EMA 9/21 cross · 1h | trend | 76.74 | -23.26 | 176 | 10.8 | -29.63 | -6.24 | -31.61 | 337 |
| 62 | Max aggression: 1-day momentum | meta | 72.56 | -27.44 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 53.17 | -46.83 | 816 | 22.2 | -74.73 | -26.61 | -74.91 | 1572 |
| 64 | Volume breakout | breakout | 51.79 | -48.21 | 491 | 12.6 | -63.73 | -25.79 | -64.24 | 809 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.86 | -42.97 | -98.86 | 5119 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.02 | -23.20 | -79.67 | 1417 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.58 | -44.22 | -93.71 | 2528 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.97 | -29.40 | -89.25 | 1918 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.43 | -36.98 | -91.61 | 2340 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.51 | -32.14 | -90.51 | 2198 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -52.06 | -97.88 | 3511 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -56.48 | -96.19 | 3384 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.00 | -35.67 | -94.00 | 2465 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.20 | -33.34 | -82.42 | 1688 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.44 | -99.42 | 5762 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -42.13 | -93.13 | 2635 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -38.69 | -95.43 | 3390 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.38 | -99.78 | 6181 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -43.60 | -92.42 | 2318 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -61.51 | -97.82 | 3592 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -56.77 | -98.65 | 4787 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.84 | -29.15 | -68.96 | 1184 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -54.44 | -94.72 | 2775 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.58 | -38.30 | -84.64 | 1810 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -63.07 | -99.61 | 6294 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.26 | -28.68 | -88.27 | 2225 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.49 | -18.86 | -76.79 | 1681 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.54 | -36.51 | -90.59 | 2273 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.25 | -46.68 | -96.25 | 3813 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.08 | -48.08 | -90.08 | 2130 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.06 | -24.61 | -73.53 | 1279 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.20 | -17.90 | -76.47 | 1572 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.53 | -47.79 | -96.53 | 4189 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -92.13 | -99.92 | 8287 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-27T19:55 | Day trade: Stocks in Play ORB | sell | AMD | 24.86 | 0.28 | target is flat |
| 2026-10-27T19:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 104.82 | -0.11 | target is flat |
| 2026-10-27T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 106.48 | 0.40 | target is flat |
| 2026-10-27T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 97.54 | -0.24 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 00:30:05.000143+00:00 -> 2026-10-28 00:40:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
