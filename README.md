# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T19:25:05.000126+00:00 · 47518 ticks

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

Today: 30213 decisions in 2520 calls, $0.3736 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T19:25 | 1 / 13 / 16 | cash |  |
| Breezy | 2026-11-04T19:25 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-04T19:25 | 4 / 22 / 4 | COIN 70% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.06 | 12.06 | 0 | — | 13.41 | 5.00 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 6.07 | 1.90 | -4.91 | 26 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.63 | 1.63 | 0 | — | 5.59 | 1.55 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.10 | -13.53 | 140 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.73 | -0.27 | 5 | 40.0 | 4.71 | 1.11 | -7.85 | 8 |
| 8 | Hold SPY | benchmark | 98.16 | -1.84 | 0 | — | -0.61 | -0.25 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.59 | -1.02 | -9.60 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 96.25 | -3.75 | 112 | 34.8 | 5.93 | 2.74 | -3.32 | 90 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.08 | -4.92 | 0 | — | -2.08 | -0.74 | -7.64 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.31 | -5.70 | 0 | — | -4.91 | -1.85 | -6.35 | 1 |
| 17 | Hold BTC | benchmark | 94.10 | -5.90 | 0 | — | -2.06 | -0.18 | -13.22 | 1 |
| 18 | Agent (rotation) | meta | 94.01 | -5.99 | 163 | 27.6 | -7.23 | -5.72 | -9.38 | 191 |
| 19 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -0.87 | -0.23 | -8.76 | 220 |
| 20 | Max aggression: 5-day momentum | meta | 91.25 | -8.75 | 16 | 43.8 | -23.80 | -1.37 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.62 | -9.38 | 103 | 22.3 | -16.75 | -6.22 | -17.97 | 79 |
| 23 | Parabolic SAR · 1h | trend | 90.32 | -9.68 | 154 | 26.6 | -14.89 | -3.34 | -19.39 | 239 |
| 24 | Agent | meta | 89.73 | -10.27 | 144 | 38.2 | -12.20 | -7.33 | -13.23 | 206 |
| 25 | Copy: Insider buying | copy | 89.64 | -10.36 | 38 | 39.5 | -21.48 | -4.32 | -23.32 | 63 |
| 26 | Opening range 30m | breakout | 89.52 | -10.48 | 355 | 33.0 | -15.44 | -5.11 | -17.21 | 591 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.29 | -3.23 | -14.15 | 84 |
| 28 | Daily: Bullish score | daily | 87.12 | -12.88 | 14 | 21.4 | -11.72 | -1.84 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.75 | -13.25 | 249 | 47.8 | -20.60 | -3.90 | -25.10 | 387 |
| 30 | Donchian 55/20 · 1h | breakout | 86.74 | -13.26 | 62 | 12.9 | -14.59 | -3.14 | -19.85 | 107 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.48 | -13.52 | 1 | 0.0 | -6.12 | -0.86 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.62 | -4.16 | -14.77 | 97 |
| 33 | ADX DI cross · 1h | trend | 85.06 | -14.94 | 155 | 18.1 | -19.84 | -3.56 | -23.74 | 271 |
| 34 | Volume breakout · 1h | breakout | 84.94 | -15.06 | 130 | 28.5 | -13.71 | -3.12 | -18.08 | 104 |
| 35 | MFI reversion · 1h | reversion | 84.39 | -15.61 | 321 | 34.3 | -14.17 | -2.16 | -18.78 | 154 |
| 36 | Keltner breakout · 1h | breakout | 83.93 | -16.07 | 94 | 24.5 | -20.65 | -4.28 | -22.73 | 184 |
| 37 | Connors RSI(2) · 1h | reversion | 83.13 | -16.87 | 192 | 40.6 | -19.27 | -6.35 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.70 | -17.30 | 434 | 30.2 | -19.82 | -6.06 | -21.19 | 721 |
| 39 | Ichimoku · 1h | trend | 82.03 | -17.97 | 85 | 12.9 | -19.94 | -4.23 | -26.10 | 127 |
| 40 | Bollinger breakout · 1h | breakout | 81.49 | -18.51 | 148 | 25.0 | -17.84 | -3.60 | -23.94 | 251 |
| 41 | CCI reversion · 1h | reversion | 80.63 | -19.37 | 278 | 46.4 | -21.95 | -3.26 | -27.71 | 454 |
| 42 | EMA 20/50 cross · 1h | trend | 79.16 | -20.84 | 92 | 10.9 | -18.65 | -3.51 | -26.55 | 134 |
| 43 | Heikin-Ashi · 1h | trend | 79.09 | -20.91 | 372 | 22.6 | -40.02 | -8.25 | -43.70 | 673 |
| 44 | MACD zero-line · 1h | trend | 78.48 | -21.52 | 141 | 15.6 | -25.17 | -5.36 | -29.93 | 223 |
| 45 | Z-score reversion · 1h | reversion | 78.22 | -21.78 | 152 | 37.5 | -15.36 | -2.24 | -23.02 | 218 |
| 46 | MACD cross · 1h | trend | 78.14 | -21.86 | 310 | 22.9 | -32.22 | -6.31 | -34.36 | 472 |
| 47 | Supertrend · 1h | trend | 78.07 | -21.93 | 147 | 12.9 | -27.08 | -5.08 | -30.19 | 237 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.26 | -4.45 | -33.57 | 33 |
| 49 | Williams %R · 1h | reversion | 76.78 | -23.22 | 290 | 47.6 | -33.28 | -5.94 | -34.80 | 529 |
| 50 | RSI momentum · 1h | momentum | 76.61 | -23.39 | 142 | 12.0 | -28.81 | -5.62 | -30.92 | 228 |
| 51 | Bollinger reversion · 1h | reversion | 76.60 | -23.40 | 233 | 40.3 | -29.08 | -5.73 | -31.14 | 375 |
| 52 | Triple EMA stack · 1h | trend | 75.92 | -24.08 | 131 | 13.7 | -29.31 | -5.95 | -32.00 | 210 |
| 53 | OBV trend · 1h | momentum | 75.36 | -24.64 | 248 | 17.3 | -29.72 | -6.41 | -31.02 | 290 |
| 54 | Donchian 20/10 · 1h | breakout | 74.51 | -25.48 | 124 | 19.4 | -27.16 | -4.92 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.24 | -25.76 | 320 | 25.6 | -34.17 | -6.68 | -36.82 | 389 |
| 56 | RSI(14) reversion · 1h | reversion | 71.96 | -28.04 | 136 | 28.7 | -21.06 | -3.70 | -26.28 | 224 |
| 57 | Agent (ML meta-label) | meta | 69.99 | -30.01 | 1430 | 22.4 | -0.68 | 0.03 | -17.35 | 279 |
| 58 | VWAP momentum · 1h | momentum | 69.66 | -30.34 | 723 | 22.1 | -54.62 | -11.27 | -55.91 | 1222 |
| 59 | EMA 9/21 cross · 1h | trend | 69.61 | -30.39 | 225 | 9.8 | -36.83 | -7.40 | -40.23 | 343 |
| 60 | Candlestick reversal · 1h | reversion | 69.47 | -30.53 | 376 | 30.1 | -34.86 | -6.56 | -37.68 | 562 |
| 61 | Three white soldiers | momentum | 68.34 | -31.66 | 436 | 16.5 | -46.97 | -21.71 | -47.38 | 629 |
| 62 | Max aggression: 1-day momentum | meta | 66.54 | -33.46 | 24 | 29.2 | -35.98 | -2.15 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -44.91 | -98.99 | 5169 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.01 | -24.70 | -80.10 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.36 | -44.07 | -93.37 | 2505 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.91 | -30.15 | -89.13 | 1904 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.91 | -36.27 | -91.09 | 2308 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.17 | -31.38 | -90.18 | 2198 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -49.89 | -97.75 | 3457 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.17 | -52.52 | -96.20 | 3351 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -32.97 | -93.57 | 2451 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.11 | -36.03 | -82.15 | 1653 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -53.74 | -99.49 | 5883 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.92 | -41.37 | -93.03 | 2600 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.58 | -36.90 | -95.59 | 3391 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -67.10 | -99.80 | 6145 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.61 | -40.76 | -91.76 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.66 | -26.43 | -74.68 | 1551 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -56.93 | -97.72 | 3510 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -59.88 | -98.70 | 4833 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.63 | -28.18 | -70.54 | 1193 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -51.94 | -94.81 | 2757 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -36.12 | -84.81 | 1789 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.00 | -99.62 | 6310 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.16 | -29.89 | -88.44 | 2235 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.60 | -19.07 | -77.04 | 1706 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.56 | -36.63 | -90.57 | 2239 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -49.24 | -96.51 | 3828 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.25 | -51.31 | -89.39 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.43 | -27.24 | -65.80 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -24.64 | -73.79 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.82 | -18.56 | -77.62 | 1616 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.95 | -51.53 | -96.96 | 4253 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.35 | -99.93 | 8211 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T19:25 | Agent (ML meta-label) | buy | SQQQ | 3.95 | — | rebalance up |
| 2026-11-04T19:25 | Agent (ML meta-label) | buy | MSTR | 4.03 | — | rebalance up |
| 2026-11-04T19:25 | Agent (ML meta-label) | buy | MSFT | 3.96 | — | rebalance up |
| 2026-11-04T19:25 | Agent (ML meta-label) | buy | ETHU | 12.76 | — | rebalance up |
| 2026-11-04T19:25 | Agent (ML meta-label) | buy | AAPL | 3.96 | — | rebalance up |
| 2026-11-04T19:25 | Agent (ML meta-label) | sell | SOL-USD | 9.96 | -0.07 | selected signal exited |
| 2026-11-04T19:25 | Agent (ML meta-label) | sell | BITX | 9.96 | -0.11 | selected signal exited |
| 2026-11-04T19:25 | Agent (ML meta-label) | sell | AMZN | 8.75 | -0.01 | selected signal exited |
| 2026-11-04T19:20 | Agent (ML meta-label) | buy | ETHU | 1.25 | — | entry |
| 2026-11-04T19:20 | Agent (ML meta-label) | buy | AMZN | 8.77 | — | entry |
| 2026-11-04T19:20 | Agent (ML meta-label) | sell | XRP-USD | 9.96 | -0.06 | selected signal exited |
| 2026-11-04T19:15 | Agent (ML meta-label) | buy | XRP-USD | 10.02 | — | entry |
| 2026-11-04T19:15 | Agent (ML meta-label) | sell | ETHU | 10.03 | -0.05 | selected signal exited |
| 2026-11-04T19:10 | Agent (ML meta-label) | buy | SOL-USD | 10.03 | — | entry |
| 2026-11-04T19:10 | Agent (ML meta-label) | sell | AMZN | 10.07 | -0.01 | selected signal exited |
| 2026-11-04T19:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 97.94 | -1.48 | target is flat |
| 2026-11-04T19:00 | MFI reversion · 1h | sell | SPY | 11.26 | -0.03 | target is flat |
| 2026-11-04T18:55 | ROC + volume · 1h | buy | TQQQ | 3.83 | — | entry |
| 2026-11-04T18:55 | ROC + volume · 1h | buy | IWM | 3.91 | — | entry |
| 2026-11-04T18:55 | ROC + volume · 1h | sell | XRP-USD | 3.87 | 0.02 | stop-loss |
| 2026-11-04T18:55 | ROC + volume · 1h | sell | SOL-USD | 3.87 | -0.02 | stop-loss |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | SQQQ | 4.97 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | MSTR | 4.97 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | MSFT | 5.03 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | ETHU | 5.07 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | BITX | 5.05 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | AMZN | 5.04 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | AAPL | 5.02 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | UPRO | 5.01 | 0.00 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | TQQQ | 4.22 | -0.03 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | TNA | 6.36 | -0.04 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | SPY | 5.02 | -0.00 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | IWM | 5.02 | -0.02 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | COIN | 5.04 | 0.02 | selected signal exited |
| 2026-11-04T18:45 | Agent (ML meta-label) | sell | GOOGL | 4.48 | -0.01 | selected signal exited |
| 2026-11-04T18:45 | ADX DI cross · 1h | buy | TQQQ | 4.26 | — | entry |
| 2026-11-04T18:45 | ADX DI cross · 1h | sell | LABU | 4.26 | 0.15 | rebalance down |
| 2026-11-04T18:45 | Opening range 15m | sell | AMZN | 6.85 | -0.07 | stop-loss |
| 2026-11-04T18:40 | Agent (ML meta-label) | buy | GOOGL | 4.49 | — | entry |
| 2026-11-04T18:40 | Agent (ML meta-label) | sell | AMD | 4.49 | -0.01 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 19:25:05.000126+00:00 -> 2026-11-04 19:35:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 19:25:05.000126+00:00 -> 2026-11-04 19:35:05.000126+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 19:25:05.000126+00:00 -> 2026-11-04 19:35:05.000126+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
