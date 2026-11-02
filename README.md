# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T11:55:05.000162+00:00 · 44969 ticks

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

Today: 8931 decisions in 1791 calls, $0.1249 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T11:55 | 1 / 3 / 1 | SOL-USD 15% |  |
| Breezy | 2026-11-02T11:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-02T11:55 | 2 / 3 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.39 | 6.39 | 0 | — | 7.73 | 3.79 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.63 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 2.05 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.80 | -0.20 | 96 | 44.8 | -11.70 | -3.22 | -12.13 | 140 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.75 | -0.25 | 0 | — | 3.11 | 1.35 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.75 | 3.18 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.08 | -2.92 | 0 | — | -1.35 | -0.73 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.55 | -5.83 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.93 | -5.07 | 129 | 31.0 | -4.44 | -3.15 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.37 | 1.45 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.54 | -5.46 | 0 | — | -7.15 | -2.74 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.95 | -6.05 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 91.80 | -8.20 | 0 | — | -0.58 | 0.08 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.57 | -5.07 | -12.21 | 209 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -16.99 | -6.24 | -17.93 | 83 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.69 | -16.91 | 2 |
| 23 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.08 | -17.21 | 591 |
| 24 | Parabolic SAR · 1h | trend | 90.54 | -9.46 | 143 | 28.0 | -17.01 | -3.88 | -20.27 | 251 |
| 25 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.78 | -1.87 | -13.40 | 91 |
| 26 | Copy: Insider buying | copy | 89.38 | -10.62 | 34 | 35.3 | -21.47 | -4.33 | -23.10 | 62 |
| 27 | Daily: Bullish score | daily | 88.55 | -11.45 | 14 | 21.4 | -6.72 | -1.08 | -14.73 | 18 |
| 28 | Donchian 55/20 · 1h | breakout | 88.54 | -11.46 | 59 | 13.6 | -16.16 | -3.64 | -17.73 | 103 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Volume breakout · 1h | breakout | 85.90 | -14.10 | 127 | 29.1 | -16.04 | -3.29 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.49 | -14.51 | 226 | 47.8 | -17.45 | -3.03 | -24.77 | 391 |
| 33 | Keltner breakout · 1h | breakout | 84.88 | -15.12 | 87 | 24.1 | -23.43 | -4.55 | -25.77 | 185 |
| 34 | ADX DI cross · 1h | trend | 84.81 | -15.19 | 142 | 19.0 | -15.26 | -2.74 | -20.33 | 261 |
| 35 | Connors RSI(2) · 1h | reversion | 83.34 | -16.66 | 188 | 40.4 | -21.48 | -6.87 | -21.86 | 152 |
| 36 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.37 | -19.33 | 723 |
| 37 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.60 | -3.61 | -30.48 | 38 |
| 38 | Bollinger breakout · 1h | breakout | 82.38 | -17.62 | 138 | 25.4 | -16.00 | -2.94 | -22.06 | 244 |
| 39 | MFI reversion · 1h | reversion | 82.27 | -17.73 | 295 | 31.9 | -15.00 | -2.32 | -20.24 | 149 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.59 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 81.77 | -18.23 | 81 | 13.6 | -21.04 | -4.21 | -24.93 | 121 |
| 42 | CCI reversion · 1h | reversion | 79.85 | -20.14 | 257 | 45.5 | -23.63 | -3.62 | -27.91 | 442 |
| 43 | Supertrend · 1h | trend | 79.57 | -20.43 | 137 | 13.1 | -27.45 | -5.36 | -28.09 | 215 |
| 44 | EMA 20/50 cross · 1h | trend | 79.49 | -20.51 | 90 | 11.1 | -24.08 | -4.84 | -26.11 | 134 |
| 45 | Williams %R · 1h | reversion | 78.95 | -21.05 | 259 | 47.1 | -33.20 | -5.87 | -34.88 | 518 |
| 46 | RSI momentum · 1h | momentum | 78.91 | -21.09 | 131 | 13.0 | -26.97 | -4.92 | -30.22 | 217 |
| 47 | MACD cross · 1h | trend | 78.47 | -21.53 | 291 | 24.1 | -31.37 | -6.26 | -33.31 | 463 |
| 48 | Z-score reversion · 1h | reversion | 78.30 | -21.70 | 136 | 33.8 | -17.13 | -2.65 | -22.55 | 207 |
| 49 | Bollinger reversion · 1h | reversion | 77.93 | -22.07 | 203 | 37.4 | -29.13 | -6.07 | -30.63 | 371 |
| 50 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -23.93 | -4.81 | -28.23 | 215 |
| 51 | Triple EMA stack · 1h | trend | 77.55 | -22.45 | 122 | 14.8 | -33.36 | -6.53 | -33.60 | 209 |
| 52 | Heikin-Ashi · 1h | trend | 77.41 | -22.59 | 343 | 23.3 | -41.39 | -8.94 | -42.77 | 665 |
| 53 | OBV trend · 1h | momentum | 77.27 | -22.73 | 235 | 17.4 | -33.08 | -6.63 | -36.20 | 302 |
| 54 | Donchian 20/10 · 1h | breakout | 75.80 | -24.20 | 117 | 20.5 | -26.26 | -4.56 | -29.81 | 217 |
| 55 | ROC + volume · 1h | momentum | 74.85 | -25.15 | 295 | 25.4 | -29.25 | -5.16 | -33.14 | 383 |
| 56 | Max aggression: 1-day momentum | meta | 73.29 | -26.71 | 21 | 33.3 | -33.79 | -1.99 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 73.04 | -26.96 | 123 | 26.0 | -20.85 | -3.66 | -26.17 | 195 |
| 58 | Candlestick reversal · 1h | reversion | 71.37 | -28.63 | 331 | 28.1 | -32.81 | -6.33 | -35.71 | 541 |
| 59 | VWAP momentum · 1h | momentum | 71.29 | -28.71 | 670 | 22.1 | -51.72 | -10.96 | -51.77 | 1244 |
| 60 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -17.07 | -2.87 | -21.79 | 341 |
| 61 | Three white soldiers | momentum | 70.65 | -29.35 | 401 | 16.2 | -45.13 | -20.91 | -45.56 | 625 |
| 62 | EMA 9/21 cross · 1h | trend | 70.49 | -29.51 | 212 | 9.9 | -34.29 | -6.39 | -37.62 | 335 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -43.64 | -98.90 | 5239 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.45 | -23.54 | -79.45 | 1421 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -43.80 | -93.55 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -31.95 | -88.97 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.14 | -37.84 | -91.28 | 2350 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.66 | -31.52 | -90.66 | 2263 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -53.43 | -97.77 | 3531 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.21 | -56.20 | -96.25 | 3412 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.63 | -34.65 | -93.66 | 2465 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.07 | -33.74 | -82.09 | 1695 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -56.53 | -99.48 | 5929 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.88 | -43.51 | -92.91 | 2634 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.67 | -37.51 | -95.67 | 3486 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -78.21 | -99.78 | 6259 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.86 | -45.46 | -91.86 | 2310 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.99 | -27.02 | -75.02 | 1568 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -57.22 | -97.70 | 3575 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.63 | -98.65 | 4870 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.84 | -28.20 | -68.95 | 1209 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -54.96 | -94.68 | 2793 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.63 | -37.91 | -84.69 | 1812 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -70.45 | -99.61 | 6376 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.16 | -30.60 | -88.28 | 2253 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.07 | -19.75 | -77.17 | 1737 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.23 | -37.51 | -90.31 | 2244 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.36 | -52.13 | -96.39 | 3844 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.79 | -55.80 | -89.84 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -63.97 | -25.02 | -64.34 | 815 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.63 | -25.07 | -73.87 | 1276 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.74 | -18.74 | -76.09 | 1589 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.73 | -50.01 | -96.77 | 4253 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.57 | -99.92 | 8372 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T11:50 | Donchian 55/20 · 1h | sell | BTC-USD | 21.95 | -0.31 | stop-loss |
| 2026-11-02T11:50 | Triple EMA stack · 1h | sell | BTC-USD | 19.19 | -0.28 | stop-loss |
| 2026-11-02T11:50 | EMA 20/50 cross · 1h | sell | BTC-USD | 19.68 | -0.27 | stop-loss |
| 2026-11-02T11:00 | Ichimoku · 1h | sell | XRP-USD | 20.32 | -0.14 | exit signal |
| 2026-11-02T11:00 | Parabolic SAR · 1h | sell | XRP-USD | 22.51 | -0.24 | exit signal |
| 2026-11-02T11:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.91 | — | rebalance up |
| 2026-11-02T11:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 8.90 | -0.07 | exit signal |
| 2026-11-02T10:05 | MACD zero-line · 1h | sell | XRP-USD | 19.22 | -0.39 | target is flat |
| 2026-11-02T10:05 | MACD cross · 1h | sell | XRP-USD | 19.55 | -0.27 | target is flat |
| 2026-11-02T10:00 | ROC + volume · 1h | buy | ETH-USD | 18.70 | — | entry signal |
| 2026-11-02T10:00 | VWAP momentum · 1h | sell | ETH-USD | 17.67 | -0.19 | exit signal |
| 2026-11-02T10:00 | Ichimoku · 1h | buy | XRP-USD | 20.46 | — | entry signal |
| 2026-11-02T09:00 | Candlestick reversal · 1h | buy | SOL-USD | 7.94 | — | entry signal |
| 2026-11-02T09:00 | VWAP momentum · 1h | buy | ETH-USD | 17.86 | — | entry signal |
| 2026-11-02T09:00 | Ichimoku · 1h | sell | BTC-USD | 20.41 | -0.11 | exit signal |
| 2026-11-02T09:00 | MACD cross · 1h | buy | XRP-USD | 4.21 | — | rebalance up |
| 2026-11-02T09:00 | MACD cross · 1h | buy | SOL-USD | 3.98 | — | rebalance up |
| 2026-11-02T09:00 | MACD cross · 1h | sell | DOGE-USD | 15.67 | -0.06 | exit signal |
| 2026-11-02T09:00 | Three white soldiers | sell | XRP-USD | 17.58 | -0.11 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 11:55:05.000162+00:00 -> 2026-11-02 12:05:05.000162+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
