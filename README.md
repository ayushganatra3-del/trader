# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T14:50:05.000130+00:00 · 45113 ticks

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

Today: 11388 decisions in 2223 calls, $0.1584 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T14:50 | 2 / 12 / 16 | cash |  |
| Breezy | 2026-11-02T14:50 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-02T14:50 | 4 / 22 / 4 | MSTR 70% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.24 | 7.24 | 0 | — | 8.73 | 4.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 6.19 | 2.00 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 4.50 | 1.71 | -4.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.96 | -0.04 | 97 | 45.4 | -12.19 | -3.38 | -12.41 | 138 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.42 | -1.58 | 0 | — | 1.79 | 0.79 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 97.62 | -2.38 | 0 | — | -0.59 | -0.26 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 100 | 36.0 | 3.93 | 2.00 | -2.46 | 93 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -2.18 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.22 | 0.60 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Gap and go | momentum | 94.99 | -5.01 | 124 | 29.0 | 4.53 | 1.49 | -8.76 | 206 |
| 15 | Agent (rotation) | meta | 94.78 | -5.22 | 130 | 30.8 | -5.96 | -4.25 | -8.89 | 134 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.77 | -5.23 | 0 | — | -1.24 | -0.41 | -7.64 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.48 | -5.52 | 0 | — | -7.15 | -2.74 | -8.12 | 1 |
| 19 | Hold BTC | benchmark | 91.70 | -8.30 | 0 | — | -0.64 | 0.07 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -9.28 | -5.68 | -12.59 | 204 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -17.68 | -6.53 | -18.61 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.07 | -2.33 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.14 | -3.70 | -17.21 | 568 |
| 24 | Parabolic SAR · 1h | trend | 89.80 | -10.20 | 145 | 27.6 | -14.99 | -3.55 | -16.86 | 236 |
| 25 | Copy: Insider buying | copy | 89.74 | -10.27 | 34 | 35.3 | -21.12 | -4.24 | -23.10 | 62 |
| 26 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -4.86 | -1.33 | -13.40 | 90 |
| 27 | Daily: Bullish score | daily | 88.55 | -11.45 | 14 | 21.4 | -7.49 | -0.97 | -14.73 | 14 |
| 28 | Donchian 55/20 · 1h | breakout | 88.08 | -11.92 | 59 | 13.6 | -14.49 | -3.27 | -18.04 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.68 | -12.32 | 1 | 0.0 | -3.21 | -0.34 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Stochastic reversion · 1h | reversion | 86.24 | -13.76 | 226 | 47.8 | -21.53 | -4.44 | -24.77 | 387 |
| 32 | Volume breakout · 1h | breakout | 85.43 | -14.57 | 127 | 29.1 | -13.57 | -2.88 | -18.27 | 99 |
| 33 | Keltner breakout · 1h | breakout | 84.45 | -15.55 | 88 | 23.9 | -20.26 | -3.76 | -25.33 | 175 |
| 34 | ADX DI cross · 1h | trend | 84.40 | -15.60 | 142 | 19.0 | -17.64 | -3.24 | -20.89 | 252 |
| 35 | Connors RSI(2) · 1h | reversion | 83.52 | -16.48 | 190 | 40.5 | -20.93 | -6.69 | -21.06 | 146 |
| 36 | MFI reversion · 1h | reversion | 83.17 | -16.83 | 299 | 32.8 | -16.32 | -2.62 | -18.25 | 144 |
| 37 | Opening range 15m | breakout | 82.99 | -17.01 | 390 | 31.5 | -17.45 | -5.08 | -19.36 | 702 |
| 38 | Bollinger breakout · 1h | breakout | 81.96 | -18.04 | 139 | 25.2 | -13.80 | -2.43 | -22.43 | 234 |
| 39 | Max aggression: 5-day momentum | meta | 81.85 | -18.15 | 15 | 40.0 | -34.97 | -2.55 | -37.35 | 26 |
| 40 | Daily: Momentum burst | daily | 81.59 | -18.41 | 19 | 15.8 | -24.53 | -3.48 | -30.47 | 33 |
| 41 | Ichimoku · 1h | trend | 81.33 | -18.67 | 81 | 13.6 | -21.18 | -4.25 | -25.28 | 119 |
| 42 | CCI reversion · 1h | reversion | 80.51 | -19.49 | 257 | 45.5 | -25.34 | -3.98 | -28.00 | 440 |
| 43 | Williams %R · 1h | reversion | 79.43 | -20.57 | 259 | 47.1 | -33.65 | -6.08 | -35.24 | 513 |
| 44 | Supertrend · 1h | trend | 79.19 | -20.81 | 137 | 13.1 | -26.49 | -5.13 | -28.00 | 214 |
| 45 | Bollinger reversion · 1h | reversion | 78.80 | -21.20 | 205 | 38.0 | -28.44 | -5.78 | -30.89 | 371 |
| 46 | EMA 20/50 cross · 1h | trend | 78.75 | -21.25 | 90 | 11.1 | -24.94 | -5.07 | -27.42 | 133 |
| 47 | Z-score reversion · 1h | reversion | 78.32 | -21.68 | 136 | 33.8 | -13.68 | -1.98 | -22.55 | 204 |
| 48 | MACD cross · 1h | trend | 78.02 | -21.98 | 293 | 23.9 | -32.46 | -6.44 | -34.32 | 461 |
| 49 | RSI momentum · 1h | momentum | 77.99 | -22.02 | 133 | 12.8 | -30.14 | -5.85 | -30.50 | 212 |
| 50 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -23.08 | -4.58 | -27.49 | 213 |
| 51 | Triple EMA stack · 1h | trend | 77.12 | -22.88 | 122 | 14.8 | -31.32 | -5.90 | -31.51 | 200 |
| 52 | Heikin-Ashi · 1h | trend | 77.02 | -22.98 | 344 | 23.3 | -41.13 | -8.92 | -42.76 | 661 |
| 53 | OBV trend · 1h | momentum | 76.56 | -23.44 | 235 | 17.4 | -36.39 | -7.95 | -36.55 | 305 |
| 54 | Donchian 20/10 · 1h | breakout | 75.35 | -24.65 | 118 | 20.3 | -24.52 | -4.03 | -30.15 | 209 |
| 55 | ROC + volume · 1h | momentum | 74.34 | -25.66 | 298 | 25.5 | -28.70 | -4.85 | -33.57 | 374 |
| 56 | RSI(14) reversion · 1h | reversion | 72.92 | -27.08 | 124 | 26.6 | -20.11 | -3.50 | -26.17 | 192 |
| 57 | Candlestick reversal · 1h | reversion | 71.43 | -28.57 | 332 | 28.3 | -34.99 | -6.94 | -36.48 | 546 |
| 58 | Max aggression: 1-day momentum | meta | 71.42 | -28.58 | 22 | 31.8 | -32.82 | -1.89 | -50.32 | 42 |
| 59 | VWAP momentum · 1h | momentum | 70.70 | -29.30 | 670 | 22.1 | -52.37 | -11.13 | -52.40 | 1222 |
| 60 | Agent (ML meta-label) | meta | 70.63 | -29.37 | 1198 | 20.9 | -14.96 | -2.68 | -17.95 | 305 |
| 61 | Three white soldiers | momentum | 70.47 | -29.53 | 402 | 16.2 | -45.30 | -21.00 | -45.61 | 617 |
| 62 | EMA 9/21 cross · 1h | trend | 69.72 | -30.29 | 213 | 9.9 | -35.88 | -6.56 | -39.79 | 324 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.60 | -98.94 | 5174 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.80 | -24.14 | -79.81 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -44.41 | -93.62 | 2526 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.08 | -32.11 | -89.08 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.37 | -38.13 | -91.38 | 2333 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.77 | -31.58 | -90.77 | 2244 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -53.30 | -97.76 | 3477 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -57.74 | -96.29 | 3391 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -34.93 | -93.62 | 2435 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.11 | -33.56 | -82.11 | 1688 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -57.06 | -99.48 | 5864 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.95 | -43.65 | -92.96 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.66 | -37.53 | -95.66 | 3427 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -78.20 | -99.78 | 6176 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.95 | -45.46 | -91.96 | 2286 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.96 | -26.56 | -74.96 | 1564 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -59.15 | -97.72 | 3548 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -61.88 | -98.66 | 4825 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.08 | -28.18 | -69.09 | 1198 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -53.87 | -94.66 | 2765 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.85 | -37.45 | -84.89 | 1805 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -70.91 | -99.61 | 6307 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.93 | -29.75 | -87.98 | 2207 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.28 | -19.81 | -77.29 | 1724 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.25 | -37.57 | -90.25 | 2227 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.37 | -52.01 | -96.39 | 3815 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.73 | -55.59 | -89.73 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.17 | -25.25 | -64.67 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.81 | -25.32 | -73.85 | 1272 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.88 | -18.74 | -75.93 | 1592 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.76 | -50.66 | -96.77 | 4219 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.60 | -99.92 | 8234 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T14:50 | Day trade: Stocks in Play ORB | buy | UPRO | 24.34 | — | entry |
| 2026-11-02T14:50 | Day trade: Stocks in Play ORB | sell | GOOGL | 24.32 | 0.00 | target is flat |
| 2026-11-02T14:50 | Agent (ML meta-label) | buy | TSLA | 8.74 | — | rebalance up |
| 2026-11-02T14:50 | Agent (ML meta-label) | buy | SQQQ | 8.68 | — | rebalance up |
| 2026-11-02T14:50 | Agent (ML meta-label) | buy | COIN | 8.66 | — | rebalance up |
| 2026-11-02T14:50 | Agent (ML meta-label) | buy | BITX | 8.67 | — | rebalance up |
| 2026-11-02T14:50 | Agent (ML meta-label) | sell | TQQQ | 9.00 | 0.01 | selected signal exited |
| 2026-11-02T14:50 | Agent (ML meta-label) | sell | MSTR | 9.04 | 0.04 | selected signal exited |
| 2026-11-02T14:50 | Agent (ML meta-label) | sell | MSFT | 7.71 | 0.01 | selected signal exited |
| 2026-11-02T14:50 | Agent (ML meta-label) | sell | ETHU | 9.00 | -0.00 | selected signal exited |
| 2026-11-02T14:50 | CCI reversion · 1h | buy | TSLA | 4.11 | — | rebalance up |
| 2026-11-02T14:50 | Bollinger reversion · 1h | buy | PLTR | 4.22 | — | rebalance up |
| 2026-11-02T14:50 | Bollinger reversion · 1h | sell | NVDA | 4.18 | 0.11 | take-profit |
| 2026-11-02T14:50 | Opening range 15m | buy | UPRO | 20.75 | — | entry signal |
| 2026-11-02T14:50 | Opening range 15m | buy | SPY | 20.75 | — | entry signal |
| 2026-11-02T14:50 | Opening range 15m | buy | AMZN | 20.75 | — | entry signal |
| 2026-11-02T14:45 | Agent (rotation) | buy | UPRO | 7.89 | — | entry |
| 2026-11-02T14:45 | Agent (rotation) | buy | NVDA | 7.89 | — | entry |
| 2026-11-02T14:45 | Day trade: Stocks in Play ORB | buy | GOOGL | 24.32 | — | entry |
| 2026-11-02T14:45 | Day trade: Stocks in Play ORB | sell | TSLA | 24.31 | -0.10 | target is flat |
| 2026-11-02T14:45 | Day trade: Stocks in Play ORB | sell | COIN | 24.11 | -0.30 | target is flat |
| 2026-11-02T14:45 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 100.19 | -0.15 | target is flat |
| 2026-11-02T14:45 | Agent (ML meta-label) | buy | TQQQ | 8.99 | — | entry |
| 2026-11-02T14:45 | Agent (ML meta-label) | buy | MSTR | 9.00 | — | following Williams %R |
| 2026-11-02T14:45 | Agent (ML meta-label) | buy | MSFT | 7.70 | — | following MACD zero-line |
| 2026-11-02T14:45 | Agent (ML meta-label) | buy | ETHU | 9.00 | — | following Stochastic reversion |
| 2026-11-02T14:45 | Agent (ML meta-label) | buy | BITX | 9.00 | — | following Z-score reversion |
| 2026-11-02T14:45 | Agent (ML meta-label) | sell | TSLA | 8.69 | -0.08 | rebalance down |
| 2026-11-02T14:45 | Agent (ML meta-label) | sell | SQQQ | 8.73 | -0.01 | rebalance down |
| 2026-11-02T14:45 | Agent (ML meta-label) | sell | COIN | 8.54 | -0.08 | rebalance down |
| 2026-11-02T14:45 | Bollinger reversion · 1h | sell | AMZN | 4.24 | 0.16 | take-profit |
| 2026-11-02T14:45 | Gap and go | buy | UPRO | 23.72 | — | entry signal |
| 2026-11-02T14:45 | Gap and go | buy | NVDA | 23.72 | — | entry signal |
| 2026-11-02T14:43 | Copy: Cathie Wood (ARKK) | buy | ARKK | 87.72 | — | entry |
| 2026-11-02T14:40 | Agent (rotation) | buy | AMZN | 7.89 | — | following Bollinger reversion |
| 2026-11-02T14:40 | Day trade: Stocks in Play ORB | buy | TSLA | 24.41 | — | entry |
| 2026-11-02T14:40 | Day trade: Stocks in Play ORB | buy | COIN | 24.41 | — | entry |
| 2026-11-02T14:40 | Day trade: Stocks in Play ORB | buy | AMZN | 24.41 | — | entry |
| 2026-11-02T14:40 | Agent (ML meta-label) | buy | TSLA | 5.64 | — | rebalance up |
| 2026-11-02T14:40 | Agent (ML meta-label) | buy | SQQQ | 5.55 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 14:50:05.000130+00:00 -> 2026-11-02 15:00:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
