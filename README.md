# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T13:52:05.000127+00:00 · 45070 ticks

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
| Copy: Insider buying | 2026-11-02 | MSM 12%, LRN 12%, SRRK 12%, BPRE 12%, RENT 12%, ACN 12%, SCQCU 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 10446 decisions in 2094 calls, $0.1461 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T13:52 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-02T13:52 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-02T13:52 | 2 / 3 / 0 | ETH-USD 59% |  |

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
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.67 | -0.33 | 0 | — | 3.11 | 1.35 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.47 | 3.04 | -2.10 | 95 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.55 | -5.83 | 2 |
| 11 | Hold SPY | benchmark | 97.00 | -3.00 | 0 | — | -1.35 | -0.73 | -3.94 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.90 | -5.10 | 129 | 31.0 | -4.44 | -3.15 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.37 | 1.45 | -8.76 | 203 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.46 | -5.54 | 0 | — | -7.15 | -2.74 | -8.12 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.87 | -6.13 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 91.89 | -8.11 | 0 | — | -0.77 | 0.05 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.57 | -5.07 | -12.21 | 209 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -16.99 | -6.24 | -17.93 | 83 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.69 | -16.91 | 2 |
| 23 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.08 | -17.21 | 591 |
| 24 | Parabolic SAR · 1h | trend | 90.49 | -9.51 | 144 | 27.8 | -17.98 | -4.23 | -19.78 | 249 |
| 25 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.78 | -1.87 | -13.40 | 91 |
| 26 | Copy: Insider buying | copy | 89.31 | -10.70 | 34 | 35.3 | -21.47 | -4.33 | -23.10 | 62 |
| 27 | Donchian 55/20 · 1h | breakout | 88.54 | -11.46 | 59 | 13.6 | -14.83 | -3.30 | -17.79 | 101 |
| 28 | Daily: Bullish score | daily | 88.53 | -11.47 | 14 | 21.4 | -6.72 | -1.08 | -14.73 | 18 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Volume breakout · 1h | breakout | 85.88 | -14.12 | 127 | 29.1 | -14.67 | -3.13 | -18.27 | 105 |
| 32 | Stochastic reversion · 1h | reversion | 85.43 | -14.57 | 226 | 47.8 | -17.45 | -3.03 | -24.77 | 391 |
| 33 | Keltner breakout · 1h | breakout | 84.86 | -15.14 | 87 | 24.1 | -23.43 | -4.55 | -25.77 | 185 |
| 34 | ADX DI cross · 1h | trend | 84.83 | -15.17 | 142 | 19.0 | -15.39 | -2.77 | -20.33 | 262 |
| 35 | Connors RSI(2) · 1h | reversion | 83.31 | -16.69 | 188 | 40.4 | -20.64 | -6.56 | -21.02 | 150 |
| 36 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.37 | -19.33 | 723 |
| 37 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.60 | -3.61 | -30.48 | 38 |
| 38 | Bollinger breakout · 1h | breakout | 82.37 | -17.63 | 138 | 25.4 | -16.00 | -2.94 | -22.06 | 244 |
| 39 | MFI reversion · 1h | reversion | 82.20 | -17.80 | 295 | 31.9 | -15.41 | -2.41 | -20.24 | 148 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.59 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 81.78 | -18.22 | 81 | 13.6 | -21.00 | -4.20 | -24.98 | 121 |
| 42 | CCI reversion · 1h | reversion | 79.83 | -20.17 | 257 | 45.5 | -23.63 | -3.62 | -27.91 | 442 |
| 43 | Supertrend · 1h | trend | 79.68 | -20.32 | 137 | 13.1 | -27.28 | -5.33 | -28.28 | 215 |
| 44 | EMA 20/50 cross · 1h | trend | 79.46 | -20.55 | 90 | 11.1 | -23.45 | -4.69 | -26.11 | 132 |
| 45 | Williams %R · 1h | reversion | 78.91 | -21.09 | 259 | 47.1 | -32.18 | -5.64 | -34.88 | 515 |
| 46 | RSI momentum · 1h | momentum | 78.69 | -21.31 | 133 | 12.8 | -28.88 | -5.58 | -29.28 | 215 |
| 47 | MACD cross · 1h | trend | 78.36 | -21.64 | 293 | 23.9 | -31.47 | -6.28 | -33.36 | 463 |
| 48 | Z-score reversion · 1h | reversion | 78.30 | -21.70 | 136 | 33.8 | -17.13 | -2.65 | -22.55 | 207 |
| 49 | Bollinger reversion · 1h | reversion | 77.87 | -22.12 | 203 | 37.4 | -29.13 | -6.07 | -30.63 | 371 |
| 50 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -23.93 | -4.81 | -28.23 | 215 |
| 51 | Triple EMA stack · 1h | trend | 77.56 | -22.44 | 122 | 14.8 | -33.28 | -6.54 | -33.38 | 209 |
| 52 | Heikin-Ashi · 1h | trend | 77.39 | -22.61 | 343 | 23.3 | -41.39 | -8.94 | -42.77 | 665 |
| 53 | OBV trend · 1h | momentum | 77.26 | -22.73 | 235 | 17.4 | -35.41 | -7.59 | -36.23 | 302 |
| 54 | Donchian 20/10 · 1h | breakout | 75.76 | -24.24 | 118 | 20.3 | -26.26 | -4.56 | -29.87 | 217 |
| 55 | ROC + volume · 1h | momentum | 74.81 | -25.19 | 296 | 25.3 | -29.31 | -5.16 | -33.26 | 384 |
| 56 | Max aggression: 1-day momentum | meta | 73.23 | -26.77 | 21 | 33.3 | -31.10 | -1.74 | -50.32 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 73.04 | -26.96 | 123 | 26.0 | -20.71 | -3.64 | -26.17 | 189 |
| 58 | Candlestick reversal · 1h | reversion | 71.41 | -28.59 | 331 | 28.1 | -33.04 | -6.40 | -35.71 | 540 |
| 59 | VWAP momentum · 1h | momentum | 71.26 | -28.74 | 670 | 22.1 | -51.71 | -10.95 | -51.77 | 1244 |
| 60 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -20.27 | -3.88 | -22.33 | 352 |
| 61 | Three white soldiers | momentum | 70.47 | -29.53 | 402 | 16.2 | -45.26 | -21.01 | -45.69 | 626 |
| 62 | EMA 9/21 cross · 1h | trend | 70.42 | -29.58 | 213 | 9.9 | -34.32 | -6.40 | -37.72 | 335 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -43.89 | -98.92 | 5250 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.56 | -23.67 | -79.56 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.54 | -44.14 | -93.59 | 2540 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.99 | -32.21 | -89.12 | 1949 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.27 | -38.27 | -91.40 | 2359 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.68 | -31.53 | -90.68 | 2264 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -53.71 | -97.77 | 3535 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -56.75 | -96.27 | 3415 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -34.83 | -93.71 | 2468 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.10 | -33.80 | -82.13 | 1696 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -56.76 | -99.48 | 5931 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -43.55 | -92.99 | 2639 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.67 | -37.46 | -95.67 | 3485 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -79.21 | -99.78 | 6261 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.94 | -45.86 | -91.94 | 2315 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.81 | -27.01 | -74.85 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -58.23 | -97.72 | 3582 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -62.01 | -98.66 | 4872 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.93 | -27.94 | -69.10 | 1211 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -54.33 | -94.69 | 2795 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.77 | -37.79 | -84.86 | 1819 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -70.64 | -99.62 | 6380 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.11 | -30.50 | -88.29 | 2254 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.96 | -19.67 | -77.23 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.17 | -37.28 | -90.27 | 2243 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.34 | -51.77 | -96.40 | 3845 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.65 | -55.46 | -89.73 | 2154 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.11 | -25.15 | -64.48 | 818 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.72 | -25.16 | -73.96 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.69 | -18.72 | -76.00 | 1591 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.74 | -50.12 | -96.80 | 4259 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.02 | -99.93 | 8372 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T13:20 | RSI momentum · 1h | sell | XRP-USD | 19.55 | -0.19 | stop-loss |
| 2026-11-02T13:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 14.11 | -0.08 | exit signal |
| 2026-11-02T12:35 | Three white soldiers | sell | SOL-USD | 17.49 | -0.17 | stop-loss |
| 2026-11-02T12:15 | Three white soldiers | buy | SOL-USD | 17.66 | — | entry signal |
| 2026-11-02T12:00 | Donchian 20/10 · 1h | sell | BTC-USD | 18.90 | -0.13 | exit signal |
| 2026-11-02T12:00 | RSI momentum · 1h | buy | XRP-USD | 6.48 | — | rebalance up |
| 2026-11-02T12:00 | RSI momentum · 1h | buy | ETH-USD | 6.61 | — | rebalance up |
| 2026-11-02T12:00 | RSI momentum · 1h | sell | BTC-USD | 13.09 | -0.09 | exit signal |
| 2026-11-02T12:00 | ROC + volume · 1h | sell | XRP-USD | 18.16 | -0.30 | exit signal |
| 2026-11-02T12:00 | Parabolic SAR · 1h | sell | ETH-USD | 18.14 | -0.04 | exit signal |
| 2026-11-02T12:00 | MACD cross · 1h | sell | SOL-USD | 19.54 | -0.30 | exit signal |
| 2026-11-02T12:00 | MACD cross · 1h | sell | ETH-USD | 15.72 | -0.14 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 13:52:05.000127+00:00 -> 2026-11-02 14:02:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
