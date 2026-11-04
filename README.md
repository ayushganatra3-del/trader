# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T20:55:05.000132+00:00 · 47604 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.49 (-10.52%)

Closed trades 146, win rate 37.7%, fees £4.05, max drawdown -11.45%.

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

Today: 37922 decisions in 2777 calls, $0.4637 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T20:55 | 0 / 18 / 12 | cash |  |
| Breezy | 2026-11-04T20:55 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-04T20:55 | 4 / 25 / 1 | COIN 67% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.09 | 13.09 | 0 | — | 14.36 | 4.98 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.90 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.74 | 0.74 | 0 | — | 4.63 | 1.40 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.12 | -13.53 | 140 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.94 | -1.06 | 5 | 40.0 | 4.29 | 1.05 | -7.24 | 8 |
| 8 | Hold SPY | benchmark | 97.99 | -2.01 | 0 | — | -0.67 | -0.29 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.03 | -9.61 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.13 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.86 | 2.74 | -3.27 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.22 | -6.27 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.23 | -4.77 | 0 | — | -2.09 | -0.75 | -7.64 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.95 | -5.33 | 26 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.34 | -5.66 | 0 | — | -4.91 | -1.87 | -6.35 | 1 |
| 17 | Hold BTC | benchmark | 94.02 | -5.98 | 0 | — | -2.25 | -0.10 | -13.22 | 1 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -0.89 | -0.23 | -8.76 | 218 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -7.87 | -6.63 | -8.32 | 182 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.88 | -9.12 | 103 | 22.3 | -16.21 | -6.04 | -17.67 | 78 |
| 22 | Max aggression: 5-day momentum | meta | 90.78 | -9.21 | 16 | 43.8 | -24.21 | -1.43 | -36.71 | 25 |
| 23 | Parabolic SAR · 1h | trend | 89.88 | -10.12 | 154 | 26.6 | -15.29 | -3.45 | -19.35 | 245 |
| 24 | Copy: Insider buying | copy | 89.59 | -10.41 | 38 | 39.5 | -21.61 | -4.39 | -23.32 | 63 |
| 25 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.98 | -7.23 | -12.78 | 212 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.72 | -5.20 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.00 | -3.50 | -14.15 | 88 |
| 28 | Daily: Bullish score | daily | 87.09 | -12.90 | 14 | 21.4 | -8.52 | -1.30 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.59 | -13.41 | 249 | 47.8 | -20.66 | -3.96 | -24.97 | 383 |
| 30 | Donchian 55/20 · 1h | breakout | 86.57 | -13.44 | 62 | 12.9 | -13.73 | -2.94 | -19.91 | 106 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.87 | -14.13 | 1 | 0.0 | -7.17 | -1.06 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.51 | -4.16 | -14.77 | 97 |
| 33 | ADX DI cross · 1h | trend | 84.83 | -15.17 | 155 | 18.1 | -18.12 | -3.28 | -22.68 | 276 |
| 34 | Volume breakout · 1h | breakout | 84.41 | -15.59 | 132 | 28.8 | -14.15 | -3.26 | -18.08 | 105 |
| 35 | MFI reversion · 1h | reversion | 84.01 | -15.99 | 324 | 34.3 | -13.16 | -1.96 | -18.47 | 153 |
| 36 | Keltner breakout · 1h | breakout | 83.62 | -16.38 | 94 | 24.5 | -20.07 | -4.14 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.43 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.13 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 81.70 | -18.30 | 85 | 12.9 | -20.48 | -4.40 | -26.10 | 129 |
| 40 | Bollinger breakout · 1h | breakout | 81.23 | -18.77 | 148 | 25.0 | -18.27 | -3.75 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.46 | -19.54 | 278 | 46.4 | -22.42 | -3.27 | -27.71 | 450 |
| 42 | EMA 20/50 cross · 1h | trend | 79.06 | -20.94 | 92 | 10.9 | -19.28 | -3.44 | -27.87 | 133 |
| 43 | Heikin-Ashi · 1h | trend | 78.66 | -21.34 | 375 | 22.7 | -40.56 | -8.57 | -43.89 | 676 |
| 44 | MACD zero-line · 1h | trend | 78.22 | -21.78 | 141 | 15.6 | -25.09 | -5.25 | -29.62 | 222 |
| 45 | MACD cross · 1h | trend | 77.85 | -22.15 | 310 | 22.9 | -30.77 | -6.09 | -33.62 | 474 |
| 46 | Supertrend · 1h | trend | 77.75 | -22.25 | 147 | 12.9 | -29.57 | -5.40 | -32.06 | 232 |
| 47 | Z-score reversion · 1h | reversion | 77.71 | -22.29 | 152 | 37.5 | -15.98 | -2.38 | -23.02 | 219 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.29 | -33.57 | 33 |
| 49 | Williams %R · 1h | reversion | 76.41 | -23.59 | 290 | 47.6 | -33.45 | -6.09 | -34.64 | 525 |
| 50 | Bollinger reversion · 1h | reversion | 76.35 | -23.65 | 233 | 40.3 | -28.77 | -5.70 | -30.69 | 369 |
| 51 | RSI momentum · 1h | momentum | 76.32 | -23.68 | 142 | 12.0 | -28.50 | -5.53 | -30.53 | 227 |
| 52 | Triple EMA stack · 1h | trend | 75.84 | -24.16 | 131 | 13.7 | -27.67 | -5.52 | -31.75 | 212 |
| 53 | OBV trend · 1h | momentum | 75.08 | -24.92 | 248 | 17.3 | -29.43 | -6.46 | -30.85 | 292 |
| 54 | Donchian 20/10 · 1h | breakout | 74.20 | -25.80 | 124 | 19.4 | -27.90 | -5.12 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.00 | -26.00 | 321 | 25.5 | -33.63 | -6.60 | -36.10 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 71.57 | -28.43 | 136 | 28.7 | -20.60 | -3.44 | -26.28 | 218 |
| 57 | EMA 9/21 cross · 1h | trend | 69.45 | -30.55 | 225 | 9.8 | -36.85 | -7.50 | -40.09 | 341 |
| 58 | VWAP momentum · 1h | momentum | 69.34 | -30.66 | 729 | 22.2 | -53.38 | -11.11 | -55.70 | 1214 |
| 59 | Agent (ML meta-label) | meta | 69.33 | -30.67 | 1441 | 22.3 | -6.32 | -1.11 | -17.74 | 302 |
| 60 | Candlestick reversal · 1h | reversion | 69.09 | -30.91 | 376 | 30.1 | -35.46 | -6.64 | -37.87 | 554 |
| 61 | Three white soldiers | momentum | 68.34 | -31.66 | 436 | 16.5 | -46.79 | -21.97 | -47.18 | 631 |
| 62 | Max aggression: 1-day momentum | meta | 66.47 | -33.53 | 24 | 29.2 | -36.07 | -2.17 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -46.39 | -98.96 | 5152 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.16 | -25.52 | -80.24 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -47.54 | -93.42 | 2508 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.94 | -31.48 | -89.10 | 1900 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.91 | -38.79 | -91.01 | 2307 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.20 | -32.24 | -90.21 | 2206 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -53.81 | -97.71 | 3451 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.16 | -59.92 | -96.16 | 3354 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -34.26 | -93.59 | 2450 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.16 | -37.57 | -82.16 | 1652 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -57.05 | -99.49 | 5880 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -43.54 | -92.99 | 2602 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.60 | -38.11 | -95.61 | 3409 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.33 | -99.80 | 6163 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.72 | -43.28 | -91.82 | 2256 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.50 | -26.85 | -74.50 | 1547 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -64.53 | -97.74 | 3522 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -65.09 | -98.70 | 4832 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.49 | -28.30 | -70.46 | 1195 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -54.94 | -94.80 | 2758 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.53 | -37.09 | -84.66 | 1781 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -76.03 | -99.62 | 6311 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.28 | -31.22 | -88.44 | 2242 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.52 | -19.23 | -76.98 | 1701 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.40 | -36.86 | -90.40 | 2216 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.46 | -52.79 | -96.50 | 3837 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.24 | -55.15 | -89.25 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.30 | -28.03 | -65.56 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.68 | -25.55 | -73.79 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.70 | -18.71 | -77.51 | 1606 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.95 | -53.95 | -96.95 | 4254 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.33 | -99.93 | 8220 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T20:55 | Agent (rotation) | sell | UPRO | 3.12 | -0.03 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | TSLA | 3.15 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | TQQQ | 31.06 | -0.34 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | SPY | 3.14 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | MSTR | 3.18 | 0.02 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | MSFT | 3.17 | 0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | GOOGL | 3.11 | -0.04 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | COIN | 2.44 | 0.00 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | BITX | 3.15 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | AAPL | 3.13 | -0.03 | selected signal exited |
| 2026-11-04T20:55 | Day trade: Stocks in Play ORB | sell | MSFT | 24.25 | 0.19 | target is flat |
| 2026-11-04T20:55 | Day trade: Stocks in Play ORB | sell | GOOGL | 23.88 | -0.21 | target is flat |
| 2026-11-04T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 105.47 | -1.14 | target is flat |
| 2026-11-04T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 95.46 | -0.80 | target is flat |
| 2026-11-04T20:55 | Agent (aggressive) | sell | BITX | 42.49 | -0.26 | selected signal exited |
| 2026-11-04T20:55 | Agent | sell | BITX | 17.81 | -0.11 | selected signal exited |
| 2026-11-04T20:55 | Opening range 30m | sell | UPRO | 9.86 | -0.07 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | TSLA | 8.96 | -0.03 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | SPY | 8.95 | -0.03 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | MSTR | 9.03 | 0.05 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | MSFT | 9.01 | 0.02 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | GOOGL | 8.87 | -0.11 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | COIN | 12.79 | 0.09 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | BITX | 8.96 | -0.02 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | AAPL | 8.89 | -0.09 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | UPRO | 7.48 | -0.07 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | TSLA | 5.92 | -0.02 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | SPY | 7.52 | -0.03 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | PLTR | 5.80 | -0.08 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | MSTR | 5.97 | 0.08 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | MSFT | 5.95 | 0.02 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | GOOGL | 6.82 | -0.07 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | ETHU | 5.83 | 0.14 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | COIN | 6.04 | 0.09 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | BITX | 5.93 | 0.07 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | AAPL | 8.16 | -0.02 | end-of-day flatten |
| 2026-11-04T20:50 | Agent (ML meta-label) | sell | IWM | 5.33 | -0.00 | selected signal exited |
| 2026-11-04T20:50 | Volume breakout · 1h | buy | COIN | 6.25 | — | entry |
| 2026-11-04T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | TQQQ | 96.26 | — | entry |
| 2026-11-04T20:30 | Agent (ML meta-label) | buy | IWM | 5.33 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 20:55:05.000132+00:00 -> 2026-11-04 21:05:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 20:55:05.000132+00:00 -> 2026-11-04 21:05:05.000132+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 20:55:05.000132+00:00 -> 2026-11-04 21:05:05.000132+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
