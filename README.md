# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T15:50:05.000147+00:00 · 45148 ticks

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
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BPRE 12%, ACN 12%, SCQCU 12%, NPB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 13413 decisions in 2328 calls, $0.1824 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T15:50 | 1 / 9 / 20 | cash |  |
| Breezy | 2026-11-02T15:50 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-02T15:50 | 3 / 21 / 6 | MSTR 67% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.69 | 7.69 | 0 | — | 9.19 | 4.32 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 6.19 | 2.00 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.97 | 2.97 | 23 | 47.8 | 3.30 | 1.26 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.42 | -0.58 | 98 | 45.9 | -12.63 | -3.51 | -12.64 | 138 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.78 | -1.22 | 0 | — | 2.25 | 0.99 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 97.80 | -2.20 | 0 | — | 0.02 | 0.07 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.69 | -2.31 | 101 | 35.6 | 4.47 | 2.25 | -2.46 | 94 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.32 | -2.28 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.24 | 0.60 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.09 | -4.91 | 0 | — | -1.01 | -0.31 | -7.64 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.97 | -5.03 | 0 | — | -5.31 | -2.03 | -6.49 | 1 |
| 16 | Gap and go | momentum | 94.81 | -5.18 | 130 | 27.7 | 4.04 | 1.34 | -8.76 | 215 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 18 | Agent (rotation) | meta | 94.44 | -5.56 | 136 | 29.4 | -6.46 | -4.59 | -9.14 | 143 |
| 19 | Hold BTC | benchmark | 91.63 | -8.37 | 0 | — | -0.16 | 0.14 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -9.17 | -5.60 | -12.48 | 205 |
| 21 | Trend pullback · 1h | trend | 91.50 | -8.50 | 101 | 21.8 | -17.15 | -6.31 | -18.32 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.52 | -2.43 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 89.87 | -10.13 | 319 | 34.5 | -12.46 | -3.81 | -17.21 | 584 |
| 24 | Parabolic SAR · 1h | trend | 89.53 | -10.47 | 145 | 27.6 | -15.20 | -3.60 | -16.86 | 241 |
| 25 | Copy: Insider buying | copy | 89.51 | -10.49 | 34 | 35.3 | -21.25 | -4.27 | -23.10 | 62 |
| 26 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -5.00 | -1.49 | -13.40 | 89 |
| 27 | Daily: Bullish score | daily | 89.25 | -10.76 | 14 | 21.4 | -6.25 | -0.77 | -14.73 | 14 |
| 28 | Donchian 55/20 · 1h | breakout | 88.65 | -11.35 | 59 | 13.6 | -13.91 | -3.13 | -18.06 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 88.05 | -11.95 | 1 | 0.0 | -2.07 | -0.15 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -10.06 | -3.24 | -14.77 | 99 |
| 31 | Stochastic reversion · 1h | reversion | 86.16 | -13.84 | 226 | 47.8 | -21.53 | -4.45 | -24.74 | 387 |
| 32 | Volume breakout · 1h | breakout | 85.20 | -14.80 | 128 | 28.9 | -16.94 | -3.80 | -18.61 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.48 | -15.52 | 88 | 23.9 | -20.32 | -3.93 | -23.96 | 174 |
| 34 | ADX DI cross · 1h | trend | 84.19 | -15.81 | 142 | 19.0 | -18.24 | -3.32 | -21.64 | 259 |
| 35 | Connors RSI(2) · 1h | reversion | 83.75 | -16.25 | 190 | 40.5 | -20.70 | -6.61 | -21.05 | 147 |
| 36 | MFI reversion · 1h | reversion | 83.38 | -16.61 | 299 | 32.8 | -16.10 | -2.57 | -18.25 | 144 |
| 37 | Opening range 15m | breakout | 82.67 | -17.33 | 394 | 31.2 | -17.74 | -5.18 | -19.65 | 716 |
| 38 | Bollinger breakout · 1h | breakout | 82.11 | -17.89 | 139 | 25.2 | -15.07 | -2.78 | -22.52 | 233 |
| 39 | Max aggression: 5-day momentum | meta | 81.35 | -18.65 | 15 | 40.0 | -35.31 | -2.59 | -37.35 | 26 |
| 40 | Ichimoku · 1h | trend | 81.15 | -18.84 | 81 | 13.6 | -21.49 | -4.34 | -25.58 | 120 |
| 41 | Daily: Momentum burst | daily | 80.84 | -19.16 | 19 | 15.8 | -24.85 | -3.54 | -30.47 | 33 |
| 42 | CCI reversion · 1h | reversion | 80.75 | -19.25 | 258 | 45.7 | -25.06 | -3.92 | -28.00 | 446 |
| 43 | Bollinger reversion · 1h | reversion | 79.01 | -20.99 | 209 | 39.2 | -28.17 | -5.70 | -30.78 | 371 |
| 44 | Supertrend · 1h | trend | 78.74 | -21.25 | 137 | 13.1 | -26.85 | -5.17 | -28.39 | 222 |
| 45 | Williams %R · 1h | reversion | 78.72 | -21.28 | 260 | 47.3 | -34.20 | -6.23 | -35.20 | 517 |
| 46 | Z-score reversion · 1h | reversion | 78.52 | -21.48 | 137 | 34.3 | -13.40 | -1.92 | -22.55 | 206 |
| 47 | EMA 20/50 cross · 1h | trend | 78.03 | -21.97 | 90 | 11.1 | -25.26 | -5.10 | -27.74 | 132 |
| 48 | MACD cross · 1h | trend | 77.83 | -22.18 | 293 | 23.9 | -32.85 | -6.57 | -34.83 | 465 |
| 49 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -23.35 | -4.64 | -27.72 | 214 |
| 50 | RSI momentum · 1h | momentum | 77.31 | -22.69 | 133 | 12.8 | -30.87 | -6.00 | -31.06 | 214 |
| 51 | Triple EMA stack · 1h | trend | 77.08 | -22.92 | 122 | 14.8 | -31.28 | -6.37 | -31.57 | 206 |
| 52 | Heikin-Ashi · 1h | trend | 77.04 | -22.96 | 344 | 23.3 | -41.44 | -8.95 | -43.08 | 662 |
| 53 | OBV trend · 1h | momentum | 76.26 | -23.74 | 236 | 17.8 | -35.49 | -7.72 | -36.17 | 308 |
| 54 | Donchian 20/10 · 1h | breakout | 75.32 | -24.68 | 118 | 20.3 | -26.42 | -4.45 | -30.79 | 206 |
| 55 | ROC + volume · 1h | momentum | 74.71 | -25.29 | 298 | 25.5 | -29.20 | -4.96 | -34.18 | 372 |
| 56 | RSI(14) reversion · 1h | reversion | 72.89 | -27.11 | 124 | 26.6 | -19.70 | -3.41 | -26.17 | 199 |
| 57 | Candlestick reversal · 1h | reversion | 71.28 | -28.73 | 332 | 28.3 | -35.60 | -7.21 | -36.74 | 542 |
| 58 | Max aggression: 1-day momentum | meta | 71.18 | -28.82 | 22 | 31.8 | -32.98 | -1.90 | -50.32 | 42 |
| 59 | Agent (ML meta-label) | meta | 70.52 | -29.48 | 1208 | 20.9 | -14.06 | -2.40 | -20.46 | 318 |
| 60 | Three white soldiers | momentum | 70.09 | -29.91 | 404 | 16.1 | -45.63 | -21.21 | -45.86 | 617 |
| 61 | VWAP momentum · 1h | momentum | 69.99 | -30.01 | 673 | 22.1 | -51.83 | -10.78 | -52.16 | 1231 |
| 62 | EMA 9/21 cross · 1h | trend | 69.52 | -30.48 | 214 | 9.8 | -36.20 | -6.63 | -40.21 | 326 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.95 | -98.96 | 5207 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.63 | -24.04 | -79.66 | 1428 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.60 | -44.05 | -93.61 | 2534 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.02 | -31.97 | -89.03 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.35 | -37.94 | -91.35 | 2337 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.88 | -31.74 | -90.88 | 2237 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -53.32 | -97.78 | 3485 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -56.99 | -96.28 | 3399 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -35.37 | -93.68 | 2443 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.26 | -33.74 | -82.26 | 1691 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -56.08 | -99.47 | 5843 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.99 | -43.88 | -92.99 | 2619 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.62 | -37.37 | -95.63 | 3408 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -76.95 | -99.79 | 6171 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.00 | -45.32 | -92.01 | 2289 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.94 | -26.59 | -75.03 | 1572 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -59.59 | -97.74 | 3552 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -61.72 | -98.66 | 4813 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.19 | -28.16 | -69.19 | 1199 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -54.06 | -94.69 | 2772 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.87 | -37.60 | -84.90 | 1811 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -72.02 | -99.62 | 6300 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.04 | -30.05 | -88.06 | 2210 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.07 | -19.70 | -77.13 | 1710 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.25 | -37.61 | -90.25 | 2227 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.38 | -52.22 | -96.38 | 3805 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.69 | -54.55 | -89.69 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.17 | -25.25 | -64.67 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.95 | -25.40 | -73.95 | 1282 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.74 | -18.62 | -75.82 | 1599 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.75 | -50.34 | -96.76 | 4213 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -95.90 | -99.92 | 8245 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T15:50 | Agent (rotation) | sell | TECL | 3.47 | -0.05 | selected signal exited |
| 2026-11-02T15:50 | Agent (rotation) | sell | SOXL | 3.43 | -0.09 | selected signal exited |
| 2026-11-02T15:50 | Agent (rotation) | sell | PLTR | 3.49 | -0.03 | selected signal exited |
| 2026-11-02T15:50 | Agent (ML meta-label) | buy | UPRO | 4.25 | — | entry |
| 2026-11-02T15:50 | Agent (ML meta-label) | buy | NVDA | 5.88 | — | entry |
| 2026-11-02T15:50 | Agent (ML meta-label) | sell | GOOGL | 6.42 | -0.02 | selected signal exited |
| 2026-11-02T15:50 | Agent (ML meta-label) | sell | ETHU | 3.71 | -0.01 | rebalance down |
| 2026-11-02T15:50 | Three white soldiers | sell | TECL | 17.29 | -0.33 | stop-loss |
| 2026-11-02T15:50 | Opening range 30m | buy | TSLA | 6.42 | — | entry |
| 2026-11-02T15:50 | Opening range 30m | sell | NVDA | 6.88 | -0.08 | stop-loss |
| 2026-11-02T15:50 | Opening range 15m | buy | MSFT | 5.51 | — | entry |
| 2026-11-02T15:50 | Opening range 15m | sell | NVDA | 5.85 | -0.07 | stop-loss |
| 2026-11-02T15:50 | Gap and go | buy | UPRO | 5.22 | — | rebalance up |
| 2026-11-02T15:50 | Gap and go | buy | TSLA | 5.24 | — | rebalance up |
| 2026-11-02T15:50 | Gap and go | buy | TQQQ | 5.28 | — | rebalance up |
| 2026-11-02T15:50 | Gap and go | buy | TNA | 5.23 | — | rebalance up |
| 2026-11-02T15:50 | Gap and go | buy | MSTR | 5.20 | — | rebalance up |
| 2026-11-02T15:50 | Gap and go | buy | AMZN | 5.15 | — | rebalance up |
| 2026-11-02T15:50 | Gap and go | sell | TECL | 10.44 | -0.15 | stop-loss |
| 2026-11-02T15:50 | Gap and go | sell | SOXL | 10.35 | -0.26 | stop-loss |
| 2026-11-02T15:50 | Gap and go | sell | PLTR | 10.52 | -0.10 | exit signal |
| 2026-11-02T15:45 | Agent (rotation) | sell | NVDA | 4.51 | -0.01 | selected signal exited |
| 2026-11-02T15:45 | Agent (ML meta-label) | buy | TQQQ | 6.13 | — | entry |
| 2026-11-02T15:45 | Agent (ML meta-label) | buy | TECL | 6.44 | — | entry |
| 2026-11-02T15:45 | Agent (ML meta-label) | buy | MSTR | 6.44 | — | following Williams %R |
| 2026-11-02T15:45 | Agent (ML meta-label) | buy | GOOGL | 6.44 | — | entry |
| 2026-11-02T15:45 | Agent (ML meta-label) | sell | TSLA | 5.70 | 0.12 | rebalance down |
| 2026-11-02T15:45 | Agent (ML meta-label) | sell | SQQQ | 5.15 | -0.07 | rebalance down |
| 2026-11-02T15:45 | Agent (ML meta-label) | sell | LABU | 3.72 | -0.04 | rebalance down |
| 2026-11-02T15:45 | Agent (ML meta-label) | sell | COIN | 5.48 | 0.02 | rebalance down |
| 2026-11-02T15:45 | Agent (ML meta-label) | sell | BITX | 5.39 | 0.01 | rebalance down |
| 2026-11-02T15:45 | Gap and go | buy | TSLA | 10.55 | — | entry |
| 2026-11-02T15:45 | Gap and go | sell | NVDA | 10.55 | -0.07 | exit signal |
| 2026-11-02T15:40 | Agent (rotation) | sell | MSTR | 4.77 | 0.01 | rebalance down |
| 2026-11-02T15:40 | Agent (ML meta-label) | buy | SOXL | 3.54 | — | entry |
| 2026-11-02T15:40 | Agent (ML meta-label) | buy | LABU | 6.10 | — | rebalance up |
| 2026-11-02T15:40 | Agent (ML meta-label) | sell | MSTR | 9.63 | 0.01 | selected signal exited |
| 2026-11-02T15:35 | Agent (ML meta-label) | buy | LABU | 4.17 | — | entry |
| 2026-11-02T15:35 | Agent (ML meta-label) | sell | TECL | 3.28 | -0.02 | selected signal exited |
| 2026-11-02T15:35 | RSI momentum · 1h | buy | TSLA | 4.00 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 15:50:05.000147+00:00 -> 2026-11-02 16:00:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
