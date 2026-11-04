# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T15:55:05.000136+00:00 · 47341 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.73 (-10.27%)

Closed trades 144, win rate 38.2%, fees £4.01, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 14175 decisions in 1989 calls, $0.1864 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T15:55 | 1 / 12 / 17 | cash |  |
| Breezy | 2026-11-04T15:55 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-04T15:55 | 5 / 22 / 3 | MSTR 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 111.00 | 11.00 | 0 | — | 11.94 | 4.78 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.39 | 6.39 | 17 | 70.6 | 5.87 | 1.84 | -4.91 | 26 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.79 | 1.79 | 0 | — | 5.78 | 1.58 | -6.60 | 1 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.55 | 0.55 | 26 | 46.2 | -1.01 | -0.28 | -7.17 | 27 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.10 | -13.53 | 140 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.20 | -0.80 | 5 | 40.0 | 3.95 | 0.97 | -7.93 | 8 |
| 9 | Hold SPY | benchmark | 97.83 | -2.17 | 0 | — | -0.99 | -0.46 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.46 | -3.54 | 110 | 35.5 | 6.17 | 2.85 | -3.27 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.25 | -4.75 | 0 | — | -2.13 | -0.76 | -7.64 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.28 | -5.72 | 0 | — | -4.91 | -1.85 | -6.35 | 1 |
| 17 | Hold BTC | benchmark | 94.25 | -5.75 | 0 | — | -1.19 | -0.03 | -13.22 | 1 |
| 18 | Agent (rotation) | meta | 93.98 | -6.02 | 159 | 28.3 | -7.24 | -5.62 | -8.26 | 188 |
| 19 | Gap and go | momentum | 93.61 | -6.39 | 155 | 27.1 | -0.69 | -0.16 | -8.76 | 223 |
| 20 | Max aggression: 5-day momentum | meta | 91.37 | -8.62 | 16 | 43.8 | -23.67 | -1.36 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.94 | -9.06 | 103 | 22.3 | -16.46 | -6.09 | -17.40 | 78 |
| 23 | Parabolic SAR · 1h | trend | 90.24 | -9.76 | 154 | 26.6 | -13.79 | -3.08 | -18.16 | 244 |
| 24 | Agent | meta | 89.73 | -10.27 | 144 | 38.2 | -11.58 | -6.98 | -12.62 | 205 |
| 25 | Opening range 30m | breakout | 89.55 | -10.45 | 351 | 33.3 | -15.56 | -5.16 | -17.21 | 588 |
| 26 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.19 | -3.10 | -14.15 | 86 |
| 27 | Copy: Insider buying | copy | 88.27 | -11.73 | 37 | 37.8 | -22.54 | -4.61 | -23.56 | 63 |
| 28 | Donchian 55/20 · 1h | breakout | 86.98 | -13.02 | 62 | 12.9 | -14.35 | -3.09 | -19.86 | 107 |
| 29 | Daily: Bullish score | daily | 86.95 | -13.05 | 14 | 21.4 | -12.17 | -1.92 | -16.58 | 14 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -11.94 | -3.93 | -14.77 | 95 |
| 31 | Stochastic reversion · 1h | reversion | 85.71 | -14.29 | 248 | 47.6 | -22.01 | -4.30 | -25.61 | 385 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 85.49 | -14.52 | 1 | 0.0 | -8.17 | -1.23 | -16.59 | 1 |
| 33 | Volume breakout · 1h | breakout | 85.04 | -14.96 | 130 | 28.5 | -13.60 | -3.09 | -18.08 | 102 |
| 34 | ADX DI cross · 1h | trend | 84.64 | -15.36 | 155 | 18.1 | -18.21 | -3.37 | -22.27 | 271 |
| 35 | Keltner breakout · 1h | breakout | 84.12 | -15.88 | 91 | 23.1 | -22.19 | -4.62 | -24.44 | 184 |
| 36 | MFI reversion · 1h | reversion | 83.75 | -16.25 | 316 | 34.2 | -14.04 | -2.17 | -18.07 | 151 |
| 37 | Connors RSI(2) · 1h | reversion | 82.95 | -17.05 | 192 | 40.6 | -19.46 | -6.44 | -20.23 | 130 |
| 38 | Opening range 15m | breakout | 82.78 | -17.22 | 430 | 30.5 | -20.26 | -6.23 | -21.19 | 722 |
| 39 | Ichimoku · 1h | trend | 81.92 | -18.08 | 85 | 12.9 | -17.48 | -3.52 | -25.73 | 124 |
| 40 | Bollinger breakout · 1h | breakout | 81.55 | -18.45 | 145 | 24.1 | -17.46 | -3.51 | -23.94 | 247 |
| 41 | CCI reversion · 1h | reversion | 80.15 | -19.85 | 277 | 46.2 | -22.44 | -3.34 | -27.71 | 455 |
| 42 | EMA 20/50 cross · 1h | trend | 78.87 | -21.13 | 92 | 10.9 | -20.46 | -3.75 | -28.14 | 130 |
| 43 | Heikin-Ashi · 1h | trend | 78.82 | -21.18 | 372 | 22.6 | -39.90 | -8.24 | -43.61 | 665 |
| 44 | MACD zero-line · 1h | trend | 78.46 | -21.54 | 141 | 15.6 | -25.41 | -5.34 | -30.11 | 220 |
| 45 | Z-score reversion · 1h | reversion | 78.28 | -21.72 | 151 | 37.1 | -14.17 | -2.06 | -23.02 | 220 |
| 46 | MACD cross · 1h | trend | 78.17 | -21.83 | 309 | 23.0 | -31.64 | -6.08 | -33.72 | 479 |
| 47 | Bollinger reversion · 1h | reversion | 77.94 | -22.06 | 233 | 40.3 | -26.86 | -5.22 | -30.17 | 380 |
| 48 | Supertrend · 1h | trend | 77.85 | -22.15 | 147 | 12.9 | -27.39 | -5.18 | -30.19 | 237 |
| 49 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.34 | -4.46 | -33.57 | 33 |
| 50 | RSI momentum · 1h | momentum | 76.68 | -23.32 | 142 | 12.0 | -29.14 | -5.67 | -31.45 | 226 |
| 51 | Williams %R · 1h | reversion | 76.43 | -23.57 | 289 | 47.4 | -35.65 | -6.39 | -36.95 | 532 |
| 52 | Triple EMA stack · 1h | trend | 75.87 | -24.13 | 131 | 13.7 | -29.17 | -5.91 | -32.11 | 207 |
| 53 | OBV trend · 1h | momentum | 75.30 | -24.70 | 248 | 17.3 | -29.90 | -6.51 | -30.95 | 290 |
| 54 | Donchian 20/10 · 1h | breakout | 74.53 | -25.47 | 124 | 19.4 | -26.95 | -4.86 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.11 | -25.89 | 314 | 25.5 | -33.65 | -6.55 | -36.25 | 383 |
| 56 | RSI(14) reversion · 1h | reversion | 72.68 | -27.32 | 136 | 28.7 | -20.38 | -3.48 | -26.28 | 218 |
| 57 | Candlestick reversal · 1h | reversion | 70.59 | -29.41 | 373 | 30.3 | -34.68 | -6.54 | -38.50 | 564 |
| 58 | Agent (ML meta-label) | meta | 70.19 | -29.81 | 1389 | 22.0 | -6.35 | -1.21 | -16.80 | 263 |
| 59 | VWAP momentum · 1h | momentum | 70.03 | -29.97 | 720 | 22.1 | -55.38 | -11.34 | -56.81 | 1234 |
| 60 | EMA 9/21 cross · 1h | trend | 69.57 | -30.43 | 225 | 9.8 | -36.89 | -7.43 | -40.21 | 339 |
| 61 | Three white soldiers | momentum | 67.92 | -32.08 | 431 | 16.0 | -46.85 | -21.49 | -47.11 | 628 |
| 62 | Max aggression: 1-day momentum | meta | 65.56 | -34.44 | 24 | 29.2 | -36.91 | -2.22 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -44.72 | -98.99 | 5165 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.04 | -24.23 | -80.27 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -44.38 | -93.53 | 2508 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.82 | -29.90 | -89.11 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.10 | -36.37 | -91.27 | 2312 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.28 | -31.49 | -90.28 | 2186 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -50.06 | -97.77 | 3463 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -54.43 | -96.29 | 3357 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.54 | -32.90 | -93.66 | 2448 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.21 | -35.62 | -82.21 | 1643 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -54.00 | -99.49 | 5889 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.02 | -42.55 | -93.11 | 2621 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.47 | -36.88 | -95.47 | 3364 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -68.63 | -99.80 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -40.76 | -91.87 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.06 | -26.86 | -75.13 | 1570 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -56.32 | -97.76 | 3490 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -60.50 | -98.71 | 4821 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.94 | -28.75 | -70.85 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.79 | -52.39 | -94.89 | 2780 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.61 | -35.60 | -84.91 | 1790 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.52 | -99.63 | 6311 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.18 | -30.02 | -88.44 | 2257 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.78 | -19.15 | -76.97 | 1713 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.64 | -37.26 | -90.67 | 2237 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.48 | -50.19 | -96.53 | 3832 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.01 | -47.45 | -89.33 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.15 | -26.92 | -65.73 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.92 | -24.72 | -74.28 | 1275 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.88 | -18.73 | -77.46 | 1623 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.96 | -51.80 | -97.00 | 4244 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.05 | -99.92 | 8188 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T15:50 | Agent (rotation) | sell | UPRO | 3.13 | -0.03 | selected signal exited |
| 2026-11-04T15:50 | Williams %R · 1h | sell | SOXL | 10.34 | -1.16 | stop-loss |
| 2026-11-04T15:50 | Z-score reversion · 1h | sell | SOXL | 9.34 | -1.27 | stop-loss |
| 2026-11-04T15:50 | Bollinger reversion · 1h | sell | SOXL | 18.55 | -1.84 | stop-loss |
| 2026-11-04T15:50 | RSI(14) reversion · 1h | sell | SOXL | 11.33 | -1.49 | stop-loss |
| 2026-11-04T15:50 | Opening range 30m | buy | COIN | 8.15 | — | entry |
| 2026-11-04T15:50 | Opening range 30m | sell | UPRO | 8.89 | -0.09 | stop-loss |
| 2026-11-04T15:50 | Opening range 15m | buy | GOOGL | 5.00 | — | rebalance up |
| 2026-11-04T15:50 | Opening range 15m | sell | TQQQ | 5.80 | -0.12 | stop-loss |
| 2026-11-04T15:50 | Opening range 15m | sell | QQQ | 5.89 | -0.04 | stop-loss |
| 2026-11-04T15:50 | Gap and go | buy | MSFT | 11.84 | — | rebalance up |
| 2026-11-04T15:50 | Gap and go | buy | ETHU | 11.42 | — | rebalance up |
| 2026-11-04T15:50 | Gap and go | buy | BITX | 11.33 | — | rebalance up |
| 2026-11-04T15:50 | Gap and go | buy | AAPL | 11.72 | — | rebalance up |
| 2026-11-04T15:50 | Gap and go | sell | UPRO | 11.56 | -0.02 | stop-loss |
| 2026-11-04T15:50 | Gap and go | sell | SPY | 11.56 | -0.01 | exit signal |
| 2026-11-04T15:45 | Agent (rotation) | sell | QQQ | 2.42 | -0.02 | selected signal exited |
| 2026-11-04T15:45 | Agent | sell | AMD | 17.58 | -0.46 | selected signal exited |
| 2026-11-04T15:45 | MACD cross · 1h | buy | PLTR | 1.37 | — | entry |
| 2026-11-04T15:45 | MACD cross · 1h | buy | IWM | 3.56 | — | entry |
| 2026-11-04T15:45 | MACD cross · 1h | sell | SOXL | 4.06 | -0.50 | stop-loss |
| 2026-11-04T15:45 | Three white soldiers | sell | SOL-USD | 13.57 | 0.07 | exit signal |
| 2026-11-04T15:45 | Three white soldiers | sell | MSTR | 16.61 | -0.33 | stop-loss |
| 2026-11-04T15:45 | Three white soldiers | sell | BTC-USD | 13.57 | 0.07 | exit signal |
| 2026-11-04T15:45 | Three white soldiers | sell | BITX | 10.47 | -0.09 | exit signal |
| 2026-11-04T15:45 | Opening range 15m | sell | TECL | 1.66 | -0.05 | stop-loss |
| 2026-11-04T15:40 | Gap and go | sell | GOOGL | 11.49 | 0.11 | stop-loss |
| 2026-11-04T15:35 | Agent (ML meta-label) | buy | SPY | 1.36 | — | entry |
| 2026-11-04T15:35 | Agent (ML meta-label) | buy | IWM | 5.03 | — | entry |
| 2026-11-04T15:35 | Agent (ML meta-label) | sell | PLTR | 6.39 | -0.03 | selected signal exited |
| 2026-11-04T15:35 | Gap and go | sell | TQQQ | 11.71 | 0.13 | stop-loss |
| 2026-11-04T15:30 | Agent (ML meta-label) | buy | TQQQ | 6.41 | — | entry |
| 2026-11-04T15:30 | Agent (ML meta-label) | buy | PLTR | 6.42 | — | entry |
| 2026-11-04T15:30 | Agent (ML meta-label) | buy | MSTR | 6.42 | — | entry |
| 2026-11-04T15:30 | Agent (ML meta-label) | buy | MSFT | 6.42 | — | following MACD zero-line, Bollinger reversion · 1h |
| 2026-11-04T15:30 | Agent (ML meta-label) | buy | GOOGL | 6.42 | — | entry |
| 2026-11-04T15:30 | Agent (ML meta-label) | buy | COIN | 6.42 | — | entry |
| 2026-11-04T15:30 | Agent (ML meta-label) | buy | BITX | 6.42 | — | following Z-score reversion |
| 2026-11-04T15:30 | Agent (ML meta-label) | buy | AMZN | 6.42 | — | entry |
| 2026-11-04T15:30 | Agent (ML meta-label) | buy | AAPL | 6.42 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 15:55:05.000136+00:00 -> 2026-11-04 16:05:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 15:55:05.000136+00:00 -> 2026-11-04 16:05:05.000136+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 15:55:05.000136+00:00 -> 2026-11-04 16:05:05.000136+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
