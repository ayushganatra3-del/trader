# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T08:55:05.000141+00:00 · 44821 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.52 (-8.48%)

Closed trades 130, win rate 40.8%, fees £3.76, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-30 | MSM 12%, LRN 12%, SRRK 12%, BPRE 12%, RENT 12%, ACN 12%, SCQCU 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 6717 decisions in 1347 calls, $0.0939 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T08:55 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-02T08:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-02T08:55 | 1 / 4 / 0 | ETH-USD 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.34 | +0.86% | 5 |
| Bollinger reversion | AMZN | 2.17 | +2.35% | 10 |
| Stochastic reversion | ETHU | 2.10 | +5.34% | 11 |
| Z-score reversion | BITX | 2.10 | +6.37% | 7 |
| Williams %R | MSTR | 2.00 | +3.35% | 15 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.30 | 6.30 | 0 | — | 7.73 | 3.79 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.63 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 2.05 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.74 | -0.26 | 96 | 44.8 | -11.70 | -3.22 | -12.13 | 140 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.66 | -0.34 | 0 | — | 3.11 | 1.35 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.75 | 3.18 | -1.98 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.55 | -5.83 | 2 |
| 11 | Hold SPY | benchmark | 96.99 | -3.01 | 0 | — | -1.35 | -0.73 | -3.94 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.90 | -5.10 | 129 | 31.0 | -4.44 | -3.15 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.37 | 1.45 | -8.76 | 203 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.45 | -5.55 | 0 | — | -7.15 | -2.74 | -8.12 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.87 | -6.13 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 92.20 | -7.80 | 0 | — | 0.04 | 0.18 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.57 | -5.07 | -12.21 | 209 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -16.99 | -6.24 | -17.93 | 83 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.69 | -16.91 | 2 |
| 23 | Parabolic SAR · 1h | trend | 90.78 | -9.22 | 142 | 28.2 | -16.73 | -3.81 | -20.27 | 251 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.08 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.78 | -1.87 | -13.40 | 91 |
| 26 | Copy: Insider buying | copy | 89.30 | -10.70 | 34 | 35.3 | -21.47 | -4.33 | -23.10 | 62 |
| 27 | Donchian 55/20 · 1h | breakout | 88.78 | -11.22 | 58 | 13.8 | -17.82 | -3.96 | -18.17 | 106 |
| 28 | Daily: Bullish score | daily | 88.53 | -11.47 | 14 | 21.4 | -6.72 | -1.08 | -14.73 | 18 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Volume breakout · 1h | breakout | 85.88 | -14.12 | 127 | 29.1 | -16.04 | -3.29 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.42 | -14.58 | 226 | 47.8 | -17.45 | -3.03 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 84.90 | -15.10 | 142 | 19.0 | -15.37 | -2.76 | -20.33 | 262 |
| 34 | Keltner breakout · 1h | breakout | 84.86 | -15.14 | 87 | 24.1 | -23.43 | -4.55 | -25.77 | 185 |
| 35 | Connors RSI(2) · 1h | reversion | 83.30 | -16.70 | 188 | 40.4 | -21.48 | -6.87 | -21.89 | 152 |
| 36 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.37 | -19.33 | 723 |
| 37 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.60 | -3.61 | -30.48 | 38 |
| 38 | Bollinger breakout · 1h | breakout | 82.37 | -17.64 | 138 | 25.4 | -16.00 | -2.94 | -22.06 | 244 |
| 39 | MFI reversion · 1h | reversion | 82.20 | -17.80 | 295 | 31.9 | -15.43 | -2.40 | -20.24 | 150 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.59 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.06 | -17.95 | 79 | 13.9 | -20.71 | -4.13 | -24.80 | 120 |
| 42 | CCI reversion · 1h | reversion | 79.83 | -20.17 | 257 | 45.5 | -23.63 | -3.62 | -27.91 | 442 |
| 43 | Supertrend · 1h | trend | 79.79 | -20.21 | 137 | 13.1 | -26.77 | -5.02 | -29.58 | 217 |
| 44 | EMA 20/50 cross · 1h | trend | 79.61 | -20.39 | 89 | 11.2 | -23.77 | -4.75 | -26.11 | 134 |
| 45 | RSI momentum · 1h | momentum | 79.02 | -20.98 | 131 | 13.0 | -26.43 | -4.75 | -30.20 | 217 |
| 46 | Williams %R · 1h | reversion | 78.91 | -21.09 | 259 | 47.1 | -33.17 | -5.87 | -34.88 | 518 |
| 47 | MACD cross · 1h | trend | 78.89 | -21.11 | 289 | 24.2 | -31.00 | -6.17 | -33.14 | 463 |
| 48 | Z-score reversion · 1h | reversion | 78.30 | -21.70 | 136 | 33.8 | -17.13 | -2.65 | -22.55 | 207 |
| 49 | Bollinger reversion · 1h | reversion | 77.87 | -22.13 | 203 | 37.4 | -29.13 | -6.07 | -30.63 | 371 |
| 50 | MACD zero-line · 1h | trend | 77.79 | -22.21 | 135 | 15.6 | -23.64 | -4.71 | -28.21 | 215 |
| 51 | Triple EMA stack · 1h | trend | 77.78 | -22.22 | 121 | 14.9 | -32.71 | -6.37 | -33.55 | 209 |
| 52 | Heikin-Ashi · 1h | trend | 77.39 | -22.61 | 343 | 23.3 | -41.39 | -8.94 | -42.77 | 665 |
| 53 | OBV trend · 1h | momentum | 77.33 | -22.67 | 235 | 17.4 | -32.32 | -6.28 | -36.20 | 302 |
| 54 | Donchian 20/10 · 1h | breakout | 75.95 | -24.05 | 117 | 20.5 | -26.06 | -4.52 | -29.81 | 217 |
| 55 | ROC + volume · 1h | momentum | 74.91 | -25.09 | 295 | 25.4 | -29.11 | -5.13 | -33.05 | 382 |
| 56 | Max aggression: 1-day momentum | meta | 73.23 | -26.77 | 21 | 33.3 | -33.79 | -1.99 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 73.04 | -26.96 | 123 | 26.0 | -21.17 | -3.74 | -26.17 | 190 |
| 58 | VWAP momentum · 1h | momentum | 71.45 | -28.55 | 669 | 22.1 | -51.61 | -10.92 | -51.67 | 1243 |
| 59 | Candlestick reversal · 1h | reversion | 71.44 | -28.56 | 331 | 28.1 | -33.14 | -6.43 | -35.71 | 540 |
| 60 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -20.50 | -3.45 | -24.08 | 355 |
| 61 | Three white soldiers | momentum | 70.72 | -29.28 | 400 | 16.2 | -45.08 | -20.86 | -45.52 | 625 |
| 62 | EMA 9/21 cross · 1h | trend | 70.66 | -29.34 | 211 | 10.0 | -34.17 | -6.36 | -37.54 | 336 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -43.78 | -98.91 | 5245 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.63 | -23.83 | -79.63 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.59 | -44.93 | -93.61 | 2541 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.80 | -31.73 | -88.91 | 1944 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.18 | -38.12 | -91.26 | 2355 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.65 | -31.45 | -90.65 | 2263 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -52.56 | -97.75 | 3529 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -57.91 | -96.26 | 3416 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.60 | -34.40 | -93.62 | 2463 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.29 | -34.41 | -82.32 | 1700 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -55.83 | -99.47 | 5924 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -43.79 | -92.94 | 2639 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.65 | -37.40 | -95.65 | 3482 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -76.94 | -99.78 | 6257 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.93 | -45.60 | -91.93 | 2315 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.95 | -26.99 | -74.99 | 1568 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -59.30 | -97.73 | 3581 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.24 | -98.65 | 4869 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.81 | -28.23 | -68.90 | 1211 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -55.14 | -94.69 | 2796 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.70 | -38.44 | -84.75 | 1816 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -70.57 | -99.61 | 6375 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.17 | -30.60 | -88.27 | 2258 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.98 | -19.69 | -77.14 | 1735 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.28 | -37.64 | -90.31 | 2246 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.38 | -52.35 | -96.40 | 3845 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.65 | -54.64 | -89.72 | 2154 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -63.97 | -25.02 | -64.34 | 815 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.72 | -25.25 | -73.87 | 1277 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.77 | -18.74 | -76.12 | 1590 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.72 | -49.71 | -96.75 | 4250 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.59 | -99.93 | 8380 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T08:35 | Three white soldiers | buy | XRP-USD | 17.69 | — | entry signal |
| 2026-11-02T08:00 | OBV trend · 1h | sell | BTC-USD | 18.32 | -0.21 | exit signal |
| 2026-11-02T08:00 | Ichimoku · 1h | buy | ETH-USD | 20.51 | — | entry signal |
| 2026-11-02T08:00 | Ichimoku · 1h | buy | BTC-USD | 20.51 | — | entry signal |
| 2026-11-02T08:00 | Parabolic SAR · 1h | buy | XRP-USD | 13.89 | — | rebalance up |
| 2026-11-02T08:00 | Parabolic SAR · 1h | buy | DOGE-USD | 4.64 | — | rebalance up |
| 2026-11-02T08:00 | Parabolic SAR · 1h | sell | BTC-USD | 22.56 | -0.23 | exit signal |
| 2026-11-02T08:00 | MACD cross · 1h | buy | DOGE-USD | 15.73 | — | entry |
| 2026-11-02T08:00 | MACD cross · 1h | sell | BTC-USD | 15.73 | -0.12 | exit signal |
| 2026-11-02T07:50 | ROC + volume · 1h | sell | BTC-USD | 18.65 | -0.29 | stop-loss |
| 2026-11-02T07:35 | Squeeze breakout · 1h | sell | BTC-USD | 22.20 | -0.32 | stop-loss |
| 2026-11-02T07:35 | RSI momentum · 1h | buy | XRP-USD | 13.26 | — | entry |
| 2026-11-02T07:35 | RSI momentum · 1h | sell | DOGE-USD | 12.99 | -0.28 | stop-loss |
| 2026-11-02T07:35 | MACD zero-line · 1h | sell | DOGE-USD | 19.19 | -0.41 | stop-loss |
| 2026-11-02T07:35 | EMA 9/21 cross · 1h | buy | XRP-USD | 8.97 | — | entry |
| 2026-11-02T07:35 | EMA 9/21 cross · 1h | sell | DOGE-USD | 8.97 | -0.19 | stop-loss |
| 2026-11-02T07:00 | Bollinger breakout · 1h | sell | XRP-USD | 20.59 | -0.26 | exit signal |
| 2026-11-02T07:00 | Bollinger breakout · 1h | sell | DOGE-USD | 20.54 | -0.32 | exit signal |
| 2026-11-02T07:00 | VWAP momentum · 1h | sell | SOL-USD | 14.22 | -0.18 | exit signal |
| 2026-11-02T07:00 | VWAP momentum · 1h | sell | DOGE-USD | 14.22 | -0.17 | exit signal |
| 2026-11-02T06:45 | Bollinger breakout · 1h | sell | BTC-USD | 16.49 | -0.15 | stop-loss |
| 2026-11-02T06:45 | ROC + volume · 1h | sell | ETH-USD | 18.73 | -0.18 | stop-loss |
| 2026-11-02T06:00 | Heikin-Ashi · 1h | sell | ETH-USD | 19.38 | -0.10 | exit signal |
| 2026-11-02T06:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 18.87 | -0.20 | exit signal |
| 2026-11-02T06:00 | Heikin-Ashi · 1h | sell | BTC-USD | 19.32 | -0.19 | exit signal |
| 2026-11-02T06:00 | ADX DI cross · 1h | sell | SOL-USD | 21.06 | -0.29 | exit signal |
| 2026-11-02T05:20 | Squeeze breakout · 1h | sell | ETH-USD | 22.31 | -0.20 | stop-loss |
| 2026-11-02T05:20 | Keltner breakout · 1h | sell | ETH-USD | 21.09 | -0.19 | stop-loss |
| 2026-11-02T05:20 | Bollinger breakout · 1h | buy | XRP-USD | 8.55 | — | rebalance up |
| 2026-11-02T05:20 | Bollinger breakout · 1h | buy | DOGE-USD | 4.19 | — | rebalance up |
| 2026-11-02T05:20 | Bollinger breakout · 1h | sell | ETH-USD | 16.48 | -0.10 | stop-loss |
| 2026-11-02T05:00 | Candlestick reversal · 1h | sell | SOL-USD | 7.13 | -0.01 | exit signal |
| 2026-11-02T05:00 | VWAP momentum · 1h | buy | SOL-USD | 9.90 | — | rebalance up |
| 2026-11-02T05:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.39 | — | rebalance up |
| 2026-11-02T05:00 | VWAP momentum · 1h | sell | ETH-USD | 8.96 | -0.04 | exit signal |
| 2026-11-02T05:00 | VWAP momentum · 1h | sell | BTC-USD | 8.94 | -0.05 | exit signal |
| 2026-11-02T04:01 | Bollinger breakout · 1h | buy | XRP-USD | 4.16 | — | rebalance up |
| 2026-11-02T04:01 | Bollinger breakout · 1h | sell | BTC-USD | 4.16 | -0.01 | rebalance down |
| 2026-11-02T04:00 | CCI reversion · 1h | sell | SOL-USD | 20.02 | -0.20 | exit signal |
| 2026-11-02T04:00 | CCI reversion · 1h | sell | DOGE-USD | 20.01 | -0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 08:55:05.000141+00:00 -> 2026-11-02 09:05:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
