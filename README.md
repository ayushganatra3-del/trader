# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T23:25:05.000125+00:00 · 48989 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.46 (-11.54%)

Closed trades 148, win rate 37.2%, fees £4.17, max drawdown -11.95%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-05 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-05)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 37.21 · VIX 26.94 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, AMZN 5.2, AAPL 5.0, MSFT 4.9, TSLA 1.2, MSTR 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 42789 decisions in 3669 calls, $0.5323 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T23:25 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-05T23:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T23:25 | 2 / 3 / 0 | ETH-USD 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.66 | 11.66 | 0 | — | 13.22 | 4.56 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.82 | 7.82 | 29 | 27.6 | 16.51 | 2.75 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.06 | 0.62 | -9.63 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.27 | -0.73 | 0 | — | 2.97 | 0.93 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 97.88 | -2.12 | 107 | 45.8 | -13.90 | -3.39 | -14.27 | 148 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.77 | -2.23 | 117 | 35.0 | 4.93 | 2.53 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.45 | -6.50 | 21 |
| 12 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.06 | 0.10 | -9.18 | 218 |
| 13 | Agent (rotation) | meta | 95.12 | -4.88 | 175 | 28.0 | -6.67 | -3.79 | -10.36 | 173 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 15 | Hold SPY | benchmark | 93.86 | -6.14 | 0 | — | -4.45 | -1.66 | -6.18 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -13.15 | -1.40 | -18.73 | 8 |
| 17 | Trend pullback · 1h | trend | 92.11 | -7.88 | 105 | 22.9 | -15.25 | -5.52 | -17.86 | 81 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 90.69 | -9.31 | 0 | — | -8.33 | -2.54 | -9.25 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.03 | -9.97 | 0 | — | -7.33 | -2.19 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.95 | -5.14 | -17.56 | 579 |
| 22 | Daily: Bullish score | daily | 89.04 | -10.96 | 14 | 21.4 | -4.51 | -0.58 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.26 | -3.58 | -14.68 | 86 |
| 24 | Agent | meta | 88.46 | -11.54 | 148 | 37.2 | -14.20 | -7.64 | -14.60 | 211 |
| 25 | Hold BTC ⏸ | benchmark | 88.43 | -11.57 | 1 | 0.0 | -5.26 | -0.66 | -13.74 | 1 |
| 26 | Parabolic SAR · 1h | trend | 87.58 | -12.42 | 166 | 27.1 | -15.02 | -3.33 | -20.02 | 242 |
| 27 | Donchian 55/20 · 1h | breakout | 86.64 | -13.36 | 71 | 14.1 | -12.50 | -2.54 | -19.94 | 104 |
| 28 | Copy: Insider buying | copy | 86.46 | -13.54 | 40 | 37.5 | -25.08 | -4.99 | -26.04 | 65 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -30.71 | -1.90 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.58 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.67 | -16.33 | 446 | 30.7 | -19.82 | -5.89 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.75 | -17.25 | 144 | 27.8 | -16.20 | -3.67 | -21.39 | 103 |
| 33 | Keltner breakout · 1h | breakout | 82.00 | -18.00 | 106 | 23.6 | -22.02 | -4.57 | -24.41 | 176 |
| 34 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -28.72 | -4.50 | -29.24 | 385 |
| 35 | Connors RSI(2) · 1h | reversion | 80.66 | -19.34 | 203 | 39.9 | -20.81 | -6.95 | -21.32 | 130 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -14.78 | -2.05 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -24.20 | -4.04 | -26.36 | 263 |
| 38 | Bollinger breakout · 1h | breakout | 79.19 | -20.81 | 165 | 23.6 | -22.43 | -4.68 | -26.52 | 247 |
| 39 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -21.52 | -2.90 | -22.50 | 152 |
| 40 | Ichimoku · 1h | trend | 78.72 | -21.28 | 94 | 14.9 | -22.59 | -4.62 | -28.82 | 126 |
| 41 | CCI reversion · 1h | reversion | 77.28 | -22.72 | 284 | 45.8 | -29.45 | -4.79 | -30.63 | 448 |
| 42 | Heikin-Ashi · 1h | trend | 77.13 | -22.87 | 385 | 23.1 | -42.47 | -8.94 | -44.25 | 674 |
| 43 | EMA 20/50 cross · 1h | trend | 76.57 | -23.43 | 102 | 10.8 | -22.75 | -4.11 | -30.17 | 131 |
| 44 | Triple EMA stack · 1h | trend | 75.05 | -24.95 | 142 | 14.8 | -30.04 | -6.35 | -33.06 | 209 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.31 | -5.47 | -29.20 | 211 |
| 46 | RSI momentum · 1h | momentum | 73.99 | -26.01 | 158 | 12.7 | -27.86 | -5.31 | -32.33 | 220 |
| 47 | Supertrend · 1h | trend | 73.91 | -26.09 | 166 | 13.3 | -29.83 | -5.19 | -34.26 | 217 |
| 48 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -36.11 | -6.41 | -38.81 | 472 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -28.16 | -4.39 | -28.35 | 223 |
| 50 | Donchian 20/10 · 1h | breakout | 72.40 | -27.60 | 140 | 20.0 | -29.70 | -5.50 | -34.25 | 214 |
| 51 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -35.53 | -4.98 | -37.45 | 30 |
| 52 | Bollinger reversion · 1h ⏸ | reversion | 72.03 | -27.97 | 244 | 38.9 | -34.17 | -6.33 | -34.52 | 375 |
| 53 | Williams %R · 1h ⏸ | reversion | 71.97 | -28.03 | 310 | 44.8 | -39.24 | -6.59 | -39.45 | 524 |
| 54 | ROC + volume · 1h | momentum | 71.60 | -28.40 | 344 | 25.6 | -36.81 | -7.18 | -37.94 | 385 |
| 55 | OBV trend · 1h | momentum | 71.31 | -28.69 | 266 | 17.3 | -33.35 | -7.11 | -33.72 | 297 |
| 56 | VWAP momentum · 1h | momentum | 68.60 | -31.40 | 757 | 22.3 | -55.12 | -12.19 | -56.33 | 1214 |
| 57 | EMA 9/21 cross · 1h | trend | 68.01 | -31.99 | 241 | 10.0 | -39.21 | -8.08 | -39.91 | 335 |
| 58 | Three white soldiers | momentum | 66.53 | -33.47 | 451 | 16.2 | -47.96 | -22.47 | -47.96 | 637 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -28.35 | -4.44 | -30.66 | 204 |
| 60 | Agent (ML meta-label) ⏸ | meta | 65.08 | -34.92 | 1508 | 22.3 | -7.34 | -0.94 | -18.78 | 322 |
| 61 | Candlestick reversal · 1h ⏸ | reversion | 64.98 | -35.02 | 395 | 28.6 | -39.18 | -7.34 | -39.41 | 563 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -41.38 | -2.56 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -46.55 | -98.92 | 5132 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.73 | -25.20 | -80.21 | 1404 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -48.36 | -93.22 | 2490 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.91 | -31.32 | -89.06 | 1893 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.54 | -39.88 | -90.57 | 2282 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.48 | -33.08 | -90.56 | 2217 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -55.78 | -97.66 | 3435 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.07 | -61.49 | -96.07 | 3346 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -33.65 | -93.67 | 2426 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.62 | -37.19 | -81.68 | 1632 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -55.62 | -99.51 | 5941 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.53 | -44.41 | -92.56 | 2583 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.85 | -39.30 | -95.88 | 3426 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -75.76 | -99.79 | 6121 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.61 | -44.34 | -91.61 | 2247 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.77 | -27.01 | -74.82 | 1562 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -65.16 | -97.66 | 3486 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -63.10 | -98.77 | 4840 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.45 | -29.34 | -70.08 | 1204 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.51 | -56.91 | -94.51 | 2740 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.69 | -37.98 | -84.73 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -75.72 | -99.64 | 6315 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.97 | -31.12 | -89.04 | 2264 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.57 | -19.66 | -77.81 | 1732 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.24 | -36.40 | -91.26 | 2225 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.54 | -52.89 | -96.57 | 3834 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.34 | -57.16 | -89.34 | 2155 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.41 | -28.21 | -65.75 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.03 | -24.44 | -73.80 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.21 | -17.84 | -78.26 | 1651 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -50.16 | -97.25 | 4303 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -114.77 | -99.93 | 8196 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T23:15 | Agent | sell | DOGE-USD | 17.21 | -0.60 | selected signal exited |
| 2026-11-05T23:15 | CCI reversion · 1h | buy | BTC-USD | 18.86 | — | entry |
| 2026-11-05T23:15 | CCI reversion · 1h | sell | DOGE-USD | 18.85 | -0.66 | target is flat |
| 2026-11-05T23:15 | VWAP reversion · 1h | sell | XRP-USD | 9.56 | -0.29 | stop-loss |
| 2026-11-05T22:00 | CCI reversion · 1h | buy | SOL-USD | 19.48 | — | entry signal |
| 2026-11-05T21:00 | Agent | buy | DOGE-USD | 17.81 | — | following CCI reversion · 1h |
| 2026-11-05T21:00 | CCI reversion · 1h | buy | DOGE-USD | 19.51 | — | entry signal |
| 2026-11-05T20:56 | Agent (rotation) | sell | SQQQ | 33.49 | 2.40 | selected signal exited |
| 2026-11-05T20:56 | Day trade: Stocks in Play ORB | sell | SQQQ | 26.26 | 2.26 | target is flat |
| 2026-11-05T20:56 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 103.72 | 5.77 | target is flat |
| 2026-11-05T20:56 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 113.59 | 8.13 | target is flat |
| 2026-11-05T20:56 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 95.31 | -0.15 | target is flat |
| 2026-11-05T20:56 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 107.82 | 10.32 | target is flat |
| 2026-11-05T20:56 | Opening range 30m | sell | SQQQ | 23.26 | 1.05 | end-of-day flatten |
| 2026-11-05T20:56 | Opening range 15m | sell | SQQQ | 22.01 | 1.45 | end-of-day flatten |
| 2026-11-05T20:50 | OBV trend · 1h | buy | SQQQ | 17.78 | — | entry |
| 2026-11-05T20:40 | Agent (ML meta-label) | buy | LABU | 3.30 | — | following VWAP momentum · 1h |
| 2026-11-05T20:40 | Agent (ML meta-label) | sell | AAPL | 3.27 | 0.02 | rebalance down |
| 2026-11-05T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 95.46 | — | entry |
| 2026-11-05T20:30 | CCI reversion · 1h | buy | MSTR | 19.50 | — | entry signal |
| 2026-11-05T20:30 | CCI reversion · 1h | buy | BITX | 19.50 | — | entry signal |
| 2026-11-05T20:30 | VWAP reversion · 1h | buy | UPRO | 9.75 | — | entry signal |
| 2026-11-05T20:30 | VWAP reversion · 1h | buy | TNA | 9.89 | — | entry signal |
| 2026-11-05T20:30 | VWAP reversion · 1h | buy | PLTR | 9.89 | — | entry signal |
| 2026-11-05T20:30 | VWAP reversion · 1h | buy | NVDA | 9.89 | — | entry signal |
| 2026-11-05T20:30 | VWAP reversion · 1h | buy | IWM | 9.89 | — | entry signal |
| 2026-11-05T20:30 | VWAP reversion · 1h | sell | XRP-USD | 5.02 | 0.01 | rebalance down |
| 2026-11-05T20:30 | VWAP reversion · 1h | sell | SOL-USD | 14.74 | -0.14 | rebalance down |
| 2026-11-05T20:30 | VWAP reversion · 1h | sell | ETH-USD | 9.75 | -0.13 | rebalance down |
| 2026-11-05T20:30 | VWAP reversion · 1h | sell | DOGE-USD | 10.00 | 0.04 | rebalance down |
| 2026-11-05T20:30 | VWAP reversion · 1h | sell | BTC-USD | 9.80 | -0.09 | rebalance down |
| 2026-11-05T20:30 | Connors RSI(2) · 1h | sell | AAPL | 20.14 | -0.11 | exit signal |
| 2026-11-05T20:30 | OBV trend · 1h | buy | AAPL | 17.77 | — | entry signal |
| 2026-11-05T20:30 | OBV trend · 1h | sell | MSFT | 17.67 | -0.17 | target is flat |
| 2026-11-05T20:30 | ROC + volume · 1h | sell | MSFT | 17.64 | -0.23 | exit signal |
| 2026-11-05T20:30 | ROC + volume · 1h | sell | AMZN | 17.69 | -0.04 | exit signal |
| 2026-11-05T20:30 | ROC + volume · 1h | sell | AAPL | 17.63 | -0.08 | exit signal |
| 2026-11-05T20:30 | VWAP momentum · 1h | buy | AMZN | 17.07 | — | entry |
| 2026-11-05T20:30 | Trend pullback · 1h | buy | AAPL | 23.00 | — | entry signal |
| 2026-11-05T20:06 | Agent (ML meta-label) | buy | MSTR | 4.68 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 23:25:05.000125+00:00 -> 2026-11-05 23:35:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 23:25:05.000125+00:00 -> 2026-11-05 23:35:05.000125+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 23:25:05.000125+00:00 -> 2026-11-05 23:35:05.000125+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
