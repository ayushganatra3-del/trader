# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T22:25:05.000172+00:00 · 47685 ticks

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

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.32 · VIX 16.88 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 39368 decisions in 3020 calls, $0.4832 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T22:25 | 1 / 2 / 2 | ETH-USD 17% |  |
| Breezy | 2026-11-04T22:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-04T22:25 | 2 / 3 / 0 | ETH-USD 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.96 | 12.96 | 0 | — | 14.28 | 4.98 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.90 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.63 | 0.63 | 0 | — | 4.55 | 1.39 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.12 | -13.53 | 140 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.11 | -0.89 | 5 | 40.0 | 4.51 | 1.09 | -7.24 | 8 |
| 8 | Hold SPY | benchmark | 98.00 | -2.00 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.03 | -9.61 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.13 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.86 | 2.74 | -3.27 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.22 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.32 | -4.68 | 0 | — | -3.89 | -1.45 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.88 | -5.12 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Hold BTC | benchmark | 94.55 | -5.45 | 0 | — | -1.28 | 0.01 | -13.22 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.95 | -5.33 | 26 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -0.89 | -0.23 | -8.76 | 218 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -7.87 | -6.63 | -8.32 | 182 |
| 20 | Max aggression: 5-day momentum | meta | 91.25 | -8.75 | 16 | 43.8 | -23.80 | -1.39 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.80 | -9.20 | 103 | 22.3 | -16.27 | -6.06 | -17.67 | 78 |
| 23 | Parabolic SAR · 1h | trend | 89.98 | -10.02 | 155 | 27.1 | -15.23 | -3.40 | -19.35 | 246 |
| 24 | Copy: Insider buying | copy | 89.55 | -10.45 | 38 | 39.5 | -21.61 | -4.39 | -23.32 | 63 |
| 25 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.98 | -7.23 | -12.78 | 212 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.73 | -5.20 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.66 | -3.36 | -14.15 | 89 |
| 28 | Daily: Bullish score | daily | 87.01 | -12.99 | 14 | 21.4 | -8.59 | -1.32 | -16.58 | 14 |
| 29 | Donchian 55/20 · 1h | breakout | 86.84 | -13.16 | 62 | 12.9 | -12.93 | -2.77 | -19.91 | 105 |
| 30 | Stochastic reversion · 1h | reversion | 86.82 | -13.18 | 249 | 47.8 | -20.42 | -3.88 | -24.97 | 383 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.11 | -13.89 | 1 | 0.0 | -6.88 | -1.01 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.52 | -4.17 | -14.77 | 97 |
| 33 | ADX DI cross · 1h | trend | 85.15 | -14.85 | 155 | 18.1 | -17.73 | -3.18 | -22.68 | 276 |
| 34 | Volume breakout · 1h | breakout | 84.56 | -15.44 | 132 | 28.8 | -14.01 | -3.23 | -18.08 | 105 |
| 35 | MFI reversion · 1h | reversion | 84.40 | -15.60 | 324 | 34.3 | -12.74 | -1.87 | -18.47 | 153 |
| 36 | Keltner breakout · 1h | breakout | 83.70 | -16.30 | 94 | 24.5 | -20.10 | -4.15 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.43 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.14 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 82.14 | -17.86 | 85 | 12.9 | -20.26 | -4.31 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.41 | -18.59 | 148 | 25.0 | -18.06 | -3.70 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.94 | -19.07 | 278 | 46.4 | -22.03 | -3.19 | -27.71 | 450 |
| 42 | EMA 20/50 cross · 1h | trend | 79.47 | -20.53 | 92 | 10.9 | -18.81 | -3.34 | -27.87 | 132 |
| 43 | Heikin-Ashi · 1h | trend | 78.80 | -21.20 | 375 | 22.7 | -40.45 | -8.50 | -43.89 | 676 |
| 44 | MACD zero-line · 1h | trend | 78.42 | -21.58 | 141 | 15.6 | -24.99 | -5.20 | -29.59 | 222 |
| 45 | MACD cross · 1h | trend | 78.12 | -21.88 | 310 | 22.9 | -30.47 | -5.98 | -33.62 | 474 |
| 46 | Z-score reversion · 1h | reversion | 77.99 | -22.01 | 152 | 37.5 | -15.60 | -2.31 | -23.02 | 219 |
| 47 | Supertrend · 1h | trend | 77.90 | -22.10 | 147 | 12.9 | -29.49 | -5.37 | -32.06 | 232 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.29 | -33.57 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.90 | -23.10 | 233 | 40.3 | -28.20 | -5.57 | -30.69 | 367 |
| 50 | Williams %R · 1h | reversion | 76.64 | -23.36 | 290 | 47.6 | -33.22 | -6.03 | -34.64 | 525 |
| 51 | RSI momentum · 1h | momentum | 76.51 | -23.49 | 142 | 12.0 | -28.31 | -5.47 | -30.45 | 227 |
| 52 | Triple EMA stack · 1h | trend | 76.06 | -23.94 | 131 | 13.7 | -27.21 | -5.40 | -31.75 | 212 |
| 53 | OBV trend · 1h | momentum | 75.42 | -24.58 | 248 | 17.3 | -29.09 | -6.34 | -30.85 | 292 |
| 54 | Donchian 20/10 · 1h | breakout | 74.38 | -25.62 | 124 | 19.4 | -27.69 | -5.08 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.19 | -25.81 | 321 | 25.5 | -33.52 | -6.58 | -36.19 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 72.18 | -27.82 | 136 | 28.7 | -20.25 | -3.37 | -26.28 | 217 |
| 57 | EMA 9/21 cross · 1h | trend | 69.60 | -30.39 | 225 | 9.8 | -36.60 | -7.41 | -40.09 | 341 |
| 58 | VWAP momentum · 1h | momentum | 69.52 | -30.48 | 729 | 22.2 | -53.22 | -11.00 | -55.70 | 1214 |
| 59 | Agent (ML meta-label) | meta | 69.31 | -30.69 | 1442 | 22.3 | -11.95 | -2.20 | -20.69 | 295 |
| 60 | Candlestick reversal · 1h | reversion | 69.21 | -30.79 | 376 | 30.1 | -35.17 | -6.57 | -37.70 | 552 |
| 61 | Three white soldiers | momentum | 68.23 | -31.77 | 436 | 16.5 | -46.88 | -22.04 | -47.18 | 633 |
| 62 | Max aggression: 1-day momentum | meta | 66.59 | -33.41 | 24 | 29.2 | -35.94 | -2.16 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -46.19 | -98.96 | 5154 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.23 | -25.42 | -80.32 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.46 | -47.58 | -93.48 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.91 | -31.47 | -89.07 | 1903 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.95 | -38.85 | -91.04 | 2313 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.24 | -32.33 | -90.27 | 2211 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -53.85 | -97.72 | 3460 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.17 | -59.54 | -96.18 | 3361 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -34.57 | -93.63 | 2459 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.16 | -37.57 | -82.16 | 1652 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -57.09 | -99.49 | 5881 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.95 | -43.72 | -92.99 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.61 | -38.06 | -95.61 | 3412 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -77.04 | -99.80 | 6165 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.72 | -43.76 | -91.80 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.56 | -26.89 | -74.56 | 1549 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -64.74 | -97.75 | 3526 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -65.02 | -98.69 | 4830 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.57 | -28.69 | -70.46 | 1200 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -55.09 | -94.79 | 2762 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.59 | -37.39 | -84.66 | 1786 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -76.10 | -99.62 | 6306 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.27 | -31.17 | -88.44 | 2239 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.83 | -19.44 | -77.27 | 1706 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.33 | -36.78 | -90.35 | 2213 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.45 | -52.84 | -96.49 | 3834 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.20 | -55.11 | -89.20 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.30 | -28.03 | -65.56 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.70 | -25.59 | -73.79 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.63 | -18.69 | -77.43 | 1603 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.93 | -53.94 | -96.94 | 4250 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.40 | -99.93 | 8226 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T22:20 | EMA 20/50 cross · 1h | sell | XRP-USD | 3.96 | 0.12 | rebalance down |
| 2026-11-04T22:20 | Three white soldiers | buy | SOL-USD | 17.09 | — | entry signal |
| 2026-11-04T22:20 | Three white soldiers | buy | ETH-USD | 17.09 | — | entry signal |
| 2026-11-04T21:15 | Agent (ML meta-label) | sell | ETH-USD | 5.31 | -0.02 | selected signal exited |
| 2026-11-04T21:05 | Agent (ML meta-label) | buy | ETH-USD | 5.33 | — | entry |
| 2026-11-04T21:00 | Parabolic SAR · 1h | sell | XRP-USD | 8.92 | 0.10 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 22:25:05.000172+00:00 -> 2026-11-04 22:35:05.000172+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 22:25:05.000172+00:00 -> 2026-11-04 22:35:05.000172+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 22:25:05.000172+00:00 -> 2026-11-04 22:35:05.000172+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
