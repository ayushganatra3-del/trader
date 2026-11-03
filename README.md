# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T17:20:05.000133+00:00 · 46385 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.54 (-9.46%)

Closed trades 141, win rate 39.0%, fees £3.96, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-03 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 22251 decisions in 2547 calls, $0.2843 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T17:20 | 5 / 13 / 12 | cash |  |
| Breezy | 2026-11-03T17:20 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-03T17:20 | 5 / 22 / 3 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| VWAP reversion | COIN | 1.90 | +3.73% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.02 | 9.02 | 0 | — | 9.67 | 4.16 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.50 | 0.26 | -5.37 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.85 | 0.85 | 26 | 26.9 | 8.55 | 2.17 | -6.54 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -12.85 | -3.55 | -13.12 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.92 | -3.08 | 0 | — | -1.40 | -0.70 | -3.94 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.35 | -3.65 | 5 | 40.0 | 3.14 | 0.82 | -7.93 | 8 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.34 | -3.66 | 107 | 34.6 | 4.32 | 2.07 | -3.79 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 95.80 | -4.20 | 0 | — | -0.89 | -0.26 | -6.60 | 1 |
| 14 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.36 | -5.64 | 0 | — | -2.61 | -0.97 | -7.64 | 1 |
| 16 | Agent (rotation) | meta | 94.19 | -5.81 | 156 | 28.8 | -5.15 | -3.05 | -8.68 | 185 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.13 | -5.87 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 18 | Gap and go | momentum | 92.60 | -7.40 | 148 | 27.0 | 1.50 | 0.54 | -9.15 | 226 |
| 19 | Hold BTC | benchmark | 91.52 | -8.48 | 0 | — | -0.11 | 0.16 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.73 | -9.27 | 102 | 21.6 | -16.46 | -6.10 | -17.40 | 78 |
| 22 | Agent | meta | 90.54 | -9.46 | 141 | 39.0 | -10.30 | -6.21 | -12.22 | 208 |
| 23 | Opening range 30m | breakout | 90.20 | -9.79 | 337 | 32.9 | -12.60 | -3.83 | -17.21 | 589 |
| 24 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -8.39 | -2.80 | -13.79 | 88 |
| 25 | Parabolic SAR · 1h | trend | 88.61 | -11.39 | 150 | 26.7 | -13.89 | -3.22 | -17.40 | 241 |
| 26 | Copy: Insider buying | copy | 88.36 | -11.64 | 35 | 37.1 | -22.39 | -4.57 | -23.13 | 61 |
| 27 | Donchian 55/20 · 1h | breakout | 88.36 | -11.64 | 60 | 13.3 | -14.67 | -3.30 | -18.06 | 100 |
| 28 | Daily: Bullish score | daily | 88.26 | -11.74 | 14 | 21.4 | -4.45 | -0.48 | -14.78 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.05 | -12.96 | 1 | 0.0 | -2.70 | -0.24 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.59 | -3.83 | -14.77 | 96 |
| 31 | Stochastic reversion · 1h | reversion | 84.91 | -15.09 | 239 | 46.9 | -23.78 | -4.76 | -26.20 | 390 |
| 32 | Max aggression: 5-day momentum | meta | 84.79 | -15.21 | 15 | 40.0 | -29.57 | -1.96 | -36.71 | 25 |
| 33 | Volume breakout · 1h | breakout | 84.71 | -15.29 | 129 | 28.7 | -15.70 | -3.62 | -18.08 | 96 |
| 34 | MFI reversion · 1h | reversion | 84.33 | -15.68 | 303 | 33.0 | -14.96 | -2.33 | -18.14 | 149 |
| 35 | Keltner breakout · 1h | breakout | 84.11 | -15.89 | 89 | 23.6 | -23.30 | -4.88 | -24.12 | 174 |
| 36 | Connors RSI(2) · 1h | reversion | 83.86 | -16.14 | 191 | 40.8 | -20.54 | -6.68 | -20.99 | 136 |
| 37 | ADX DI cross · 1h | trend | 83.41 | -16.59 | 148 | 18.2 | -17.46 | -3.27 | -21.64 | 250 |
| 38 | Opening range 15m | breakout | 82.98 | -17.02 | 411 | 30.2 | -17.91 | -5.20 | -20.73 | 720 |
| 39 | Bollinger breakout · 1h | breakout | 81.62 | -18.38 | 140 | 25.0 | -17.78 | -3.61 | -23.31 | 233 |
| 40 | Ichimoku · 1h | trend | 81.14 | -18.86 | 84 | 13.1 | -18.92 | -3.84 | -25.58 | 120 |
| 41 | EMA 20/50 cross · 1h | trend | 80.04 | -19.96 | 90 | 11.1 | -18.60 | -3.61 | -26.91 | 124 |
| 42 | CCI reversion · 1h | reversion | 79.36 | -20.64 | 268 | 44.8 | -26.18 | -4.12 | -27.91 | 451 |
| 43 | Bollinger reversion · 1h | reversion | 78.51 | -21.49 | 224 | 38.4 | -27.45 | -5.36 | -30.14 | 375 |
| 44 | MACD zero-line · 1h | trend | 77.93 | -22.07 | 136 | 15.4 | -25.37 | -5.52 | -27.61 | 212 |
| 45 | Z-score reversion · 1h | reversion | 77.82 | -22.18 | 142 | 34.5 | -14.10 | -2.02 | -23.02 | 217 |
| 46 | Supertrend · 1h | trend | 77.80 | -22.20 | 141 | 12.8 | -27.82 | -5.31 | -29.54 | 223 |
| 47 | MACD cross · 1h | trend | 77.47 | -22.52 | 300 | 23.3 | -33.68 | -6.51 | -36.40 | 478 |
| 48 | Williams %R · 1h | reversion | 77.04 | -22.96 | 276 | 46.4 | -36.32 | -6.45 | -37.64 | 529 |
| 49 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -26.80 | -3.47 | -33.57 | 33 |
| 50 | Heikin-Ashi · 1h | trend | 76.45 | -23.55 | 357 | 22.4 | -41.67 | -8.66 | -44.63 | 664 |
| 51 | RSI momentum · 1h | momentum | 76.38 | -23.62 | 136 | 12.5 | -30.02 | -5.73 | -31.98 | 215 |
| 52 | Triple EMA stack · 1h | trend | 76.32 | -23.68 | 126 | 14.3 | -28.58 | -5.70 | -31.13 | 205 |
| 53 | OBV trend · 1h | momentum | 75.92 | -24.08 | 240 | 17.5 | -30.76 | -6.51 | -32.98 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 75.26 | -24.74 | 120 | 20.0 | -27.49 | -4.91 | -30.44 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.31 | -25.69 | 302 | 25.5 | -34.48 | -6.71 | -36.14 | 376 |
| 56 | RSI(14) reversion · 1h | reversion | 73.23 | -26.77 | 130 | 26.2 | -19.74 | -3.46 | -26.28 | 199 |
| 57 | Candlestick reversal · 1h | reversion | 71.49 | -28.51 | 355 | 28.7 | -33.66 | -6.14 | -37.45 | 547 |
| 58 | Agent (ML meta-label) | meta | 70.19 | -29.81 | 1343 | 21.4 | -13.81 | -2.76 | -18.29 | 303 |
| 59 | Three white soldiers | momentum | 69.21 | -30.79 | 414 | 16.2 | -46.19 | -21.64 | -46.21 | 616 |
| 60 | EMA 9/21 cross · 1h | trend | 69.05 | -30.95 | 219 | 9.6 | -37.29 | -7.57 | -38.97 | 327 |
| 61 | VWAP momentum · 1h | momentum | 68.75 | -31.25 | 700 | 21.6 | -53.44 | -10.49 | -56.39 | 1233 |
| 62 | Max aggression: 1-day momentum | meta | 68.31 | -31.69 | 23 | 30.4 | -32.76 | -1.86 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.44 | -98.97 | 5194 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.19 | -23.17 | -80.26 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.38 | -45.35 | -93.42 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -31.07 | -89.04 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.03 | -36.92 | -91.07 | 2329 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.56 | -31.88 | -90.67 | 2219 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -51.66 | -97.72 | 3454 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -59.95 | -96.23 | 3378 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.49 | -34.63 | -93.51 | 2396 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.64 | -34.36 | -81.99 | 1661 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -51.54 | -99.47 | 5846 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -43.72 | -93.00 | 2620 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.35 | -36.81 | -95.36 | 3346 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.09 | -99.80 | 6163 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -43.89 | -91.88 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.49 | -26.33 | -74.87 | 1556 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -59.76 | -97.76 | 3535 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -59.24 | -98.66 | 4808 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.03 | -26.88 | -70.22 | 1194 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -54.15 | -94.76 | 2772 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.95 | -37.80 | -84.99 | 1813 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.72 | -99.61 | 6290 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.13 | -29.87 | -88.25 | 2228 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.56 | -19.10 | -76.72 | 1689 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.05 | -36.03 | -90.13 | 2228 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.45 | -49.85 | -96.46 | 3803 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -54.42 | -89.42 | 2137 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.84 | -25.47 | -65.79 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.40 | -24.74 | -74.08 | 1272 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.83 | -18.88 | -77.02 | 1578 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -48.66 | -96.81 | 4221 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.02 | -99.92 | 8220 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T17:15 | Agent (ML meta-label) | buy | TSLA | 10.53 | — | rebalance up |
| 2026-11-03T17:15 | Agent (ML meta-label) | buy | SQQQ | 10.59 | — | rebalance up |
| 2026-11-03T17:15 | Agent (ML meta-label) | buy | MSTR | 10.56 | — | rebalance up |
| 2026-11-03T17:15 | Agent (ML meta-label) | buy | ETHU | 10.53 | — | rebalance up |
| 2026-11-03T17:15 | Agent (ML meta-label) | sell | UPRO | 7.02 | 0.01 | selected signal exited |
| 2026-11-03T17:15 | Agent (ML meta-label) | sell | TQQQ | 7.04 | 0.02 | selected signal exited |
| 2026-11-03T17:15 | Agent (ML meta-label) | sell | TNA | 7.02 | 0.00 | selected signal exited |
| 2026-11-03T17:15 | Agent (ML meta-label) | sell | SOXL | 7.07 | 0.05 | selected signal exited |
| 2026-11-03T17:15 | Agent (ML meta-label) | sell | GOOGL | 7.03 | 0.01 | selected signal exited |
| 2026-11-03T17:15 | Agent (ML meta-label) | sell | BITX | 7.03 | 0.01 | selected signal exited |
| 2026-11-03T17:10 | Opening range 30m | buy | QQQ | 1.97 | — | entry signal |
| 2026-11-03T17:05 | Agent (ML meta-label) | buy | UPRO | 7.01 | — | entry |
| 2026-11-03T17:05 | Agent (ML meta-label) | buy | TQQQ | 7.02 | — | entry |
| 2026-11-03T17:05 | Agent (ML meta-label) | buy | TNA | 7.02 | — | entry |
| 2026-11-03T17:05 | Agent (ML meta-label) | buy | SOXL | 7.02 | — | following Connors RSI(2) |
| 2026-11-03T17:05 | Agent (ML meta-label) | buy | MSTR | 7.02 | — | entry |
| 2026-11-03T17:05 | Agent (ML meta-label) | buy | GOOGL | 7.02 | — | entry |
| 2026-11-03T17:05 | Agent (ML meta-label) | buy | BITX | 7.02 | — | following Z-score reversion |
| 2026-11-03T17:05 | Agent (ML meta-label) | sell | TSLA | 10.51 | -0.05 | rebalance down |
| 2026-11-03T17:05 | Agent (ML meta-label) | sell | SQQQ | 10.54 | -0.00 | rebalance down |
| 2026-11-03T17:05 | Agent (ML meta-label) | sell | ETHU | 7.07 | 0.03 | rebalance down |
| 2026-11-03T17:05 | Three white soldiers | buy | DOGE-USD | 17.31 | — | entry |
| 2026-11-03T17:00 | MACD zero-line · 1h | buy | SOL-USD | 11.73 | — | entry signal |
| 2026-11-03T17:00 | MACD zero-line · 1h | buy | BTC-USD | 15.60 | — | entry signal |
| 2026-11-03T17:00 | MACD zero-line · 1h | sell | XRP-USD | 4.14 | 0.06 | rebalance down |
| 2026-11-03T17:00 | MACD zero-line · 1h | sell | ETH-USD | 3.95 | -0.00 | rebalance down |
| 2026-11-03T16:55 | Agent (rotation) | sell | BITX | 7.90 | 0.02 | selected signal exited |
| 2026-11-03T16:55 | Agent (ML meta-label) | buy | TSLA | 3.52 | — | rebalance up |
| 2026-11-03T16:55 | Agent (ML meta-label) | buy | SQQQ | 3.59 | — | rebalance up |
| 2026-11-03T16:55 | Agent (ML meta-label) | sell | MSTR | 10.53 | 0.03 | selected signal exited |
| 2026-11-03T16:55 | Agent (ML meta-label) | sell | BITX | 17.59 | 0.06 | selected signal exited |
| 2026-11-03T16:55 | Agent | sell | MSFT | 18.09 | -0.02 | selected signal exited |
| 2026-11-03T16:55 | Candlestick reversal · 1h | buy | ETHU | 1.59 | — | entry |
| 2026-11-03T16:55 | Gap and go | sell | BITX | 23.33 | 0.07 | target is flat |
| 2026-11-03T16:51 | Agent (ML meta-label) | buy | MSTR | 10.50 | — | entry |
| 2026-11-03T16:51 | Agent (ML meta-label) | sell | TSLA | 3.51 | -0.02 | rebalance down |
| 2026-11-03T16:51 | Agent (ML meta-label) | sell | SQQQ | 3.52 | 0.01 | rebalance down |
| 2026-11-03T16:51 | Candlestick reversal · 1h | buy | AAPL | 8.45 | — | rebalance up |
| 2026-11-03T16:51 | Candlestick reversal · 1h | sell | ETHU | 10.03 | 0.03 | target is flat |
| 2026-11-03T16:50 | Agent (ML meta-label) | buy | BITX | 17.53 | — | following Z-score reversion |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 17:20:05.000133+00:00 -> 2026-11-03 17:30:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 17:20:05.000133+00:00 -> 2026-11-03 17:30:05.000133+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 17:20:05.000133+00:00 -> 2026-11-03 17:30:05.000133+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
