# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T05:55:05.000135+00:00 · 44684 ticks

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

Today: 4680 decisions in 936 calls, $0.0654 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T05:55 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-02T05:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-02T05:55 | 1 / 4 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.48 | 6.48 | 0 | — | 7.73 | 3.79 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.63 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 2.05 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.87 | -0.13 | 96 | 44.8 | -12.42 | -3.45 | -12.61 | 144 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.84 | -0.16 | 0 | — | 3.11 | 1.35 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.75 | 3.18 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.16 | -2.84 | 0 | — | -1.35 | -0.73 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.55 | -5.83 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.96 | -5.04 | 129 | 31.0 | -4.44 | -3.15 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.37 | 1.45 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.62 | -5.38 | 0 | — | -7.15 | -2.74 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.03 | -5.97 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 92.49 | -7.51 | 0 | — | -0.86 | 0.03 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.57 | -5.07 | -12.21 | 209 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -16.99 | -6.24 | -17.93 | 83 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.69 | -16.91 | 2 |
| 23 | Parabolic SAR · 1h | trend | 91.16 | -8.84 | 141 | 28.4 | -16.56 | -3.77 | -20.27 | 251 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.08 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 89.67 | -10.34 | 60 | 23.3 | -6.62 | -1.82 | -13.27 | 91 |
| 26 | Copy: Insider buying | copy | 89.46 | -10.54 | 34 | 35.3 | -21.47 | -4.33 | -23.10 | 62 |
| 27 | Donchian 55/20 · 1h | breakout | 88.91 | -11.09 | 58 | 13.8 | -17.21 | -3.80 | -18.19 | 106 |
| 28 | Daily: Bullish score | daily | 88.57 | -11.43 | 14 | 21.4 | -6.72 | -1.08 | -14.73 | 18 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Volume breakout · 1h | breakout | 85.92 | -14.08 | 127 | 29.1 | -16.04 | -3.29 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.55 | -14.45 | 226 | 47.8 | -17.45 | -3.03 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 84.99 | -15.01 | 141 | 19.1 | -15.22 | -2.75 | -20.33 | 262 |
| 34 | Keltner breakout · 1h | breakout | 84.90 | -15.10 | 87 | 24.1 | -23.43 | -4.55 | -25.77 | 185 |
| 35 | Connors RSI(2) · 1h | reversion | 83.38 | -16.62 | 188 | 40.4 | -21.48 | -6.87 | -21.89 | 152 |
| 36 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.37 | -19.33 | 723 |
| 37 | Bollinger breakout · 1h | breakout | 82.87 | -17.13 | 135 | 25.9 | -15.54 | -2.85 | -21.76 | 244 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.60 | -3.61 | -30.48 | 38 |
| 39 | MFI reversion · 1h | reversion | 82.34 | -17.66 | 295 | 31.9 | -17.28 | -2.74 | -20.24 | 152 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.59 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.08 | -17.92 | 79 | 13.9 | -20.76 | -4.14 | -24.80 | 118 |
| 42 | Supertrend · 1h | trend | 80.06 | -19.94 | 137 | 13.1 | -26.22 | -4.78 | -29.58 | 219 |
| 43 | CCI reversion · 1h | reversion | 79.88 | -20.12 | 257 | 45.5 | -25.12 | -3.89 | -27.91 | 446 |
| 44 | EMA 20/50 cross · 1h | trend | 79.74 | -20.26 | 89 | 11.2 | -23.54 | -4.48 | -26.96 | 137 |
| 45 | RSI momentum · 1h | momentum | 79.31 | -20.69 | 130 | 13.1 | -26.57 | -4.79 | -30.28 | 217 |
| 46 | MACD cross · 1h | trend | 79.14 | -20.86 | 288 | 24.3 | -30.85 | -6.13 | -32.88 | 463 |
| 47 | Williams %R · 1h | reversion | 78.99 | -21.01 | 259 | 47.1 | -33.17 | -5.87 | -34.88 | 518 |
| 48 | Z-score reversion · 1h | reversion | 78.30 | -21.70 | 136 | 33.8 | -17.13 | -2.65 | -22.55 | 207 |
| 49 | MACD zero-line · 1h | trend | 78.12 | -21.88 | 134 | 15.7 | -23.41 | -4.66 | -27.97 | 215 |
| 50 | Bollinger reversion · 1h | reversion | 77.99 | -22.01 | 203 | 37.4 | -29.51 | -6.17 | -30.72 | 373 |
| 51 | Triple EMA stack · 1h | trend | 77.85 | -22.15 | 121 | 14.9 | -31.02 | -5.85 | -33.46 | 209 |
| 52 | Heikin-Ashi · 1h | trend | 77.63 | -22.36 | 340 | 23.5 | -41.18 | -8.88 | -42.69 | 665 |
| 53 | OBV trend · 1h | momentum | 77.51 | -22.49 | 234 | 17.5 | -33.24 | -6.75 | -36.15 | 302 |
| 54 | Donchian 20/10 · 1h | breakout | 76.03 | -23.97 | 117 | 20.5 | -26.08 | -4.52 | -29.81 | 217 |
| 55 | ROC + volume · 1h | momentum | 75.30 | -24.70 | 293 | 25.6 | -28.83 | -5.07 | -32.80 | 382 |
| 56 | Max aggression: 1-day momentum | meta | 73.36 | -26.64 | 21 | 33.3 | -33.79 | -1.99 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 73.04 | -26.96 | 123 | 26.0 | -21.35 | -3.76 | -26.17 | 196 |
| 58 | VWAP momentum · 1h | momentum | 71.80 | -28.20 | 667 | 22.2 | -51.43 | -10.86 | -51.55 | 1243 |
| 59 | Candlestick reversal · 1h | reversion | 71.44 | -28.56 | 331 | 28.1 | -33.49 | -6.53 | -35.71 | 544 |
| 60 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -23.61 | -4.02 | -25.84 | 333 |
| 61 | EMA 9/21 cross · 1h | trend | 70.89 | -29.11 | 210 | 10.0 | -34.01 | -6.36 | -37.32 | 336 |
| 62 | Three white soldiers | momentum | 70.75 | -29.25 | 400 | 16.2 | -45.05 | -20.83 | -45.48 | 624 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -43.45 | -98.90 | 5235 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.67 | -23.83 | -79.70 | 1425 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.60 | -45.07 | -93.62 | 2541 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.91 | -31.60 | -88.99 | 1944 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.27 | -38.36 | -91.31 | 2357 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.59 | -31.27 | -90.59 | 2259 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -52.68 | -97.78 | 3531 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -57.94 | -96.26 | 3415 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.82 | -34.74 | -93.82 | 2477 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.29 | -34.41 | -82.32 | 1700 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -54.65 | -99.48 | 5929 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.90 | -43.59 | -92.91 | 2635 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.61 | -37.12 | -95.61 | 3477 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -76.07 | -99.78 | 6254 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.97 | -45.42 | -91.97 | 2316 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.93 | -26.98 | -74.97 | 1567 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -59.94 | -97.73 | 3585 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -59.54 | -98.64 | 4869 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.66 | -28.00 | -68.74 | 1206 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -54.87 | -94.67 | 2793 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.58 | -37.98 | -84.62 | 1811 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.32 | -99.62 | 6383 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.09 | -30.27 | -88.17 | 2253 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.25 | -19.67 | -77.38 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.27 | -36.99 | -90.30 | 2248 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -51.75 | -96.44 | 3851 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.74 | -54.07 | -89.79 | 2158 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.03 | -25.12 | -64.34 | 816 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.72 | -25.25 | -73.87 | 1277 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.77 | -18.84 | -77.03 | 1607 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -50.59 | -96.79 | 4262 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -95.51 | -99.93 | 8375 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-02T04:00 | Williams %R · 1h | sell | DOGE-USD | 19.93 | 0.08 | exit signal |
| 2026-11-02T04:00 | Stochastic reversion · 1h | sell | SOL-USD | 4.80 | 0.05 | exit signal |
| 2026-11-02T04:00 | Stochastic reversion · 1h | sell | DOGE-USD | 4.79 | 0.04 | exit signal |
| 2026-11-02T04:00 | Z-score reversion · 1h | sell | SOL-USD | 13.11 | 0.07 | exit signal |
| 2026-11-02T04:00 | RSI(14) reversion · 1h | sell | SOL-USD | 12.14 | -0.12 | exit signal |
| 2026-11-02T04:00 | Candlestick reversal · 1h | sell | XRP-USD | 7.16 | 0.02 | exit signal |
| 2026-11-02T04:00 | Candlestick reversal · 1h | sell | DOGE-USD | 7.16 | 0.02 | exit signal |
| 2026-11-02T04:00 | Squeeze breakout · 1h | buy | BTC-USD | 22.52 | — | entry signal |
| 2026-11-02T04:00 | Bollinger breakout · 1h | buy | XRP-USD | 8.14 | — | entry signal |
| 2026-11-02T04:00 | Bollinger breakout · 1h | buy | DOGE-USD | 16.68 | — | entry signal |
| 2026-11-02T04:00 | Bollinger breakout · 1h | sell | ETH-USD | 4.23 | 0.01 | rebalance down |
| 2026-11-02T04:00 | RSI momentum · 1h | buy | DOGE-USD | 13.27 | — | entry signal |
| 2026-11-02T04:00 | RSI momentum · 1h | sell | ETH-USD | 6.85 | 0.10 | rebalance down |
| 2026-11-02T04:00 | RSI momentum · 1h | sell | BTC-USD | 6.62 | 0.03 | rebalance down |
| 2026-11-02T04:00 | ROC + volume · 1h | buy | XRP-USD | 18.45 | — | entry signal |
| 2026-11-02T04:00 | ROC + volume · 1h | buy | BTC-USD | 18.94 | — | entry signal |
| 2026-11-02T04:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.08 | — | entry signal |
| 2026-11-02T04:00 | Heikin-Ashi · 1h | buy | BTC-USD | 19.51 | — | entry signal |
| 2026-11-02T04:00 | ADX DI cross · 1h | buy | SOL-USD | 21.34 | — | entry signal |
| 2026-11-02T04:00 | Supertrend · 1h | buy | SOL-USD | 15.81 | — | entry signal |
| 2026-11-02T04:00 | Supertrend · 1h | buy | DOGE-USD | 16.11 | — | entry signal |
| 2026-11-02T04:00 | Supertrend · 1h | sell | ETH-USD | 4.08 | 0.01 | rebalance down |
| 2026-11-02T04:00 | Supertrend · 1h | sell | BTC-USD | 4.02 | -0.00 | rebalance down |
| 2026-11-02T04:00 | MACD zero-line · 1h | buy | XRP-USD | 19.61 | — | entry signal |
| 2026-11-02T04:00 | MACD zero-line · 1h | buy | DOGE-USD | 19.61 | — | entry signal |
| 2026-11-02T04:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 9.16 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 05:55:05.000135+00:00 -> 2026-11-02 06:05:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
