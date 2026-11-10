# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T19:55:05.000189+00:00 · 54934 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.53 (-12.47%)

Closed trades 169, win rate 35.5%, fees £5.11, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 17.52 | +0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-10 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 33332 decisions in 2950 calls, $0.4151 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T19:55 | 3 / 6 / 20 | cash |  |
| Breezy | 2026-11-10T19:55 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-11-10T19:55 | 5 / 21 / 3 | BITX 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.53 | +5.83% | 4 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| OBV trend | MSTR | 1.43 | +3.47% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.49 | 3.94 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.27 | 15.27 | 0 | — | 15.47 | 5.08 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.89 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.01 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.28 | 1.27 | 0 | — | 4.20 | 1.23 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.07 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.52 | 1.07 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -5.06 | -2.08 | -10.56 | 155 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.66 | -3.34 | 0 | — | -1.33 | -0.40 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.84 | -4.16 | 138 | 46.4 | -12.79 | -3.31 | -13.48 | 154 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.37 | -5.63 | 0 | — | -4.95 | -1.31 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.78 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.88 | -7.12 | 108 | 23.1 | -12.47 | -4.65 | -16.78 | 77 |
| 19 | Copy: Insider buying | copy | 92.53 | -7.47 | 43 | 39.5 | -8.34 | -1.74 | -15.11 | 67 |
| 20 | Copy: Congress Democrats (NANC) | copy | 92.19 | -7.81 | 0 | — | -4.63 | -1.23 | -10.64 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.15 | -2.85 | -14.15 | 75 |
| 23 | Opening range 30m | breakout | 88.37 | -11.63 | 403 | 33.3 | -14.70 | -4.57 | -14.82 | 605 |
| 24 | Agent | meta | 87.53 | -12.47 | 169 | 35.5 | -13.25 | -6.73 | -14.25 | 200 |
| 25 | Daily: Bullish score | daily | 86.67 | -13.33 | 15 | 20.0 | -7.14 | -1.02 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 85.86 | -14.14 | 1 | 0.0 | -6.54 | -0.82 | -16.64 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.46 | -14.54 | 168 | 26.8 | -13.66 | -2.80 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.98 | -15.02 | 79 | 32.9 | -15.89 | -4.49 | -18.49 | 93 |
| 29 | Donchian 55/20 · 1h | breakout | 84.27 | -15.73 | 71 | 14.1 | -21.54 | -4.50 | -26.93 | 102 |
| 30 | Keltner breakout · 1h | breakout | 81.67 | -18.33 | 110 | 23.6 | -20.95 | -4.37 | -25.32 | 175 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 81.50 | -18.50 | 2 | 0.0 | -8.81 | -1.00 | -24.16 | 1 |
| 32 | Connors RSI(2) · 1h | reversion | 80.97 | -19.03 | 207 | 40.1 | -19.38 | -6.48 | -19.98 | 125 |
| 33 | Opening range 15m | breakout | 80.79 | -19.21 | 500 | 31.4 | -20.56 | -5.59 | -20.62 | 735 |
| 34 | Stochastic reversion · 1h | reversion | 80.79 | -19.21 | 284 | 47.5 | -26.32 | -3.90 | -27.94 | 398 |
| 35 | Max aggression: 5-day momentum | meta | 80.34 | -19.66 | 18 | 44.4 | -36.24 | -2.31 | -45.81 | 25 |
| 36 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -15.42 | -3.62 | -22.08 | 93 |
| 37 | ADX DI cross · 1h | trend | 78.96 | -21.04 | 185 | 18.9 | -24.45 | -4.19 | -29.95 | 265 |
| 38 | Heikin-Ashi · 1h | trend | 78.90 | -21.10 | 416 | 24.5 | -40.21 | -7.54 | -42.52 | 664 |
| 39 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.22 | -4.42 | -27.99 | 236 |
| 40 | MFI reversion · 1h | reversion | 76.84 | -23.16 | 361 | 34.1 | -19.17 | -2.43 | -22.46 | 160 |
| 41 | CCI reversion · 1h | reversion | 76.81 | -23.18 | 326 | 45.1 | -26.34 | -3.98 | -30.69 | 453 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.26 | -8.88 | -31.64 | 119 |
| 43 | EMA 20/50 cross · 1h | trend | 75.10 | -24.90 | 102 | 10.8 | -26.50 | -4.71 | -36.18 | 120 |
| 44 | MACD cross · 1h | trend | 74.57 | -25.43 | 360 | 21.9 | -32.09 | -5.25 | -39.64 | 468 |
| 45 | MACD zero-line · 1h | trend | 73.81 | -26.19 | 159 | 16.4 | -25.25 | -5.20 | -30.85 | 215 |
| 46 | Bollinger reversion · 1h | reversion | 73.80 | -26.20 | 278 | 40.3 | -26.90 | -4.16 | -32.54 | 371 |
| 47 | RSI momentum · 1h | momentum | 73.38 | -26.62 | 159 | 12.6 | -25.54 | -4.25 | -34.84 | 212 |
| 48 | Supertrend · 1h | trend | 73.36 | -26.64 | 168 | 13.1 | -32.57 | -5.98 | -36.07 | 232 |
| 49 | Triple EMA stack · 1h | trend | 72.26 | -27.74 | 144 | 14.6 | -26.91 | -4.70 | -35.63 | 205 |
| 50 | OBV trend · 1h | momentum | 71.88 | -28.12 | 275 | 18.2 | -29.09 | -5.21 | -36.54 | 273 |
| 51 | Williams %R · 1h | reversion | 71.65 | -28.35 | 346 | 45.7 | -35.72 | -5.59 | -36.06 | 536 |
| 52 | ROC + volume · 1h | momentum | 71.09 | -28.91 | 362 | 26.5 | -35.64 | -6.83 | -38.38 | 381 |
| 53 | Donchian 20/10 · 1h | breakout | 70.91 | -29.09 | 142 | 19.7 | -30.40 | -5.68 | -35.64 | 205 |
| 54 | Daily: Momentum burst | daily | 70.62 | -29.38 | 27 | 11.1 | -38.07 | -5.45 | -38.86 | 34 |
| 55 | Z-score reversion · 1h ⏸ | reversion | 70.59 | -29.41 | 190 | 36.3 | -26.34 | -3.82 | -28.98 | 232 |
| 56 | Max aggression: 1-day momentum | meta | 67.33 | -32.67 | 27 | 25.9 | -30.56 | -1.51 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 66.37 | -33.63 | 170 | 30.6 | -27.95 | -3.74 | -32.54 | 244 |
| 58 | VWAP momentum · 1h | momentum | 66.04 | -33.96 | 838 | 22.0 | -53.95 | -11.60 | -55.01 | 1217 |
| 59 | Agent (ML meta-label) | meta | 65.54 | -34.46 | 1696 | 24.5 | -11.25 | -1.74 | -17.15 | 328 |
| 60 | EMA 9/21 cross · 1h | trend | 65.34 | -34.66 | 252 | 9.9 | -37.24 | -7.42 | -41.69 | 334 |
| 61 | Candlestick reversal · 1h | reversion | 63.58 | -36.42 | 446 | 28.0 | -37.77 | -6.82 | -38.92 | 591 |
| 62 | Three white soldiers | momentum | 60.63 | -39.37 | 510 | 14.7 | -49.17 | -23.00 | -49.17 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -46.09 | -98.97 | 5258 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.80 | -26.54 | -79.82 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.30 | -47.52 | -93.31 | 2509 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.27 | -32.41 | -89.31 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.77 | -40.25 | -90.79 | 2327 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.24 | -32.51 | -90.30 | 2196 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -55.22 | -97.77 | 3461 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -58.52 | -96.19 | 3401 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.54 | -33.30 | -93.67 | 2358 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.44 | -35.10 | -82.47 | 1668 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -55.67 | -99.55 | 5997 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.18 | -43.72 | -92.21 | 2611 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -37.76 | -95.56 | 3428 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.28 | -99.80 | 6165 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.98 | -44.10 | -92.01 | 2269 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.47 | -24.83 | -75.62 | 1597 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -63.92 | -97.74 | 3522 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.85 | -63.74 | -98.87 | 4893 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.63 | -27.62 | -68.99 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -55.38 | -94.57 | 2773 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.43 | -37.45 | -84.52 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -74.86 | -99.65 | 6339 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.68 | -32.64 | -89.83 | 2292 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.94 | -20.05 | -78.25 | 1749 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.64 | -37.25 | -90.81 | 2207 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.82 | -52.64 | -96.83 | 3856 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -59.00 | -89.35 | 2144 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.74 | -27.87 | -66.41 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.18 | -23.06 | -71.18 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.80 | -19.36 | -80.01 | 1691 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.22 | -49.62 | -97.24 | 4283 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -117.60 | -99.93 | 8314 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T19:50 | Agent (ML meta-label) | buy | TECL | 3.31 | — | rebalance up |
| 2026-11-10T19:50 | Agent (ML meta-label) | sell | META | 13.06 | -0.02 | selected signal exited |
| 2026-11-10T19:50 | Opening range 15m | sell | SQQQ | 19.95 | -0.35 | exit signal |
| 2026-11-10T19:45 | Agent (ML meta-label) | buy | TECL | 13.05 | — | entry |
| 2026-11-10T19:45 | Agent (ML meta-label) | buy | COIN | 13.07 | — | following Donchian 20/10 |
| 2026-11-10T19:45 | Agent (ML meta-label) | sell | SPY | 16.33 | 0.00 | selected signal exited |
| 2026-11-10T19:45 | Agent (ML meta-label) | sell | AMD | 3.29 | -0.00 | rebalance down |
| 2026-11-10T19:40 | Agent (ML meta-label) | buy | SPY | 5.45 | — | rebalance up |
| 2026-11-10T19:40 | Agent (ML meta-label) | buy | AMD | 3.30 | — | rebalance up |
| 2026-11-10T19:40 | Agent (ML meta-label) | sell | COIN | 13.06 | -0.02 | selected signal exited |
| 2026-11-10T19:40 | MFI reversion · 1h | buy | BITX | 12.72 | — | entry |
| 2026-11-10T19:40 | MFI reversion · 1h | sell | ETHU | 12.72 | 0.03 | target is flat |
| 2026-11-10T19:35 | Agent (ML meta-label) | buy | META | 13.08 | — | entry |
| 2026-11-10T19:35 | Agent (ML meta-label) | sell | TECL | 11.05 | 0.17 | selected signal exited |
| 2026-11-10T19:35 | OBV trend · 1h | buy | IWM | 7.49 | — | entry |
| 2026-11-10T19:35 | OBV trend · 1h | sell | META | 3.69 | 0.02 | rebalance down |
| 2026-11-10T19:35 | OBV trend · 1h | sell | AMZN | 3.80 | 0.04 | rebalance down |
| 2026-11-10T19:30 | Connors RSI(2) · 1h | sell | AAPL | 20.33 | 0.11 | exit signal |
| 2026-11-10T19:30 | Candlestick reversal · 1h | buy | TQQQ | 1.91 | — | entry signal |
| 2026-11-10T19:30 | Candlestick reversal · 1h | buy | MSFT | 7.05 | — | entry signal |
| 2026-11-10T19:30 | Candlestick reversal · 1h | sell | SQQQ | 8.96 | 0.17 | exit signal |
| 2026-11-10T19:30 | OBV trend · 1h | buy | AMD | 17.79 | — | entry signal |
| 2026-11-10T19:30 | ROC + volume · 1h | buy | SPY | 3.34 | — | entry signal |
| 2026-11-10T19:30 | ROC + volume · 1h | buy | AMD | 5.46 | — | entry signal |
| 2026-11-10T19:30 | VWAP momentum · 1h | buy | TNA | 9.98 | — | entry signal |
| 2026-11-10T19:30 | VWAP momentum · 1h | buy | IWM | 13.22 | — | entry signal |
| 2026-11-10T19:30 | VWAP momentum · 1h | sell | TSLA | 3.41 | 0.01 | rebalance down |
| 2026-11-10T19:30 | VWAP momentum · 1h | sell | SQQQ | 3.47 | 0.02 | rebalance down |
| 2026-11-10T19:30 | Triple EMA stack · 1h | buy | AMD | 18.04 | — | entry signal |
| 2026-11-10T19:30 | EMA 9/21 cross · 1h | buy | SOXL | 2.06 | — | entry signal |
| 2026-11-10T19:25 | Agent (ML meta-label) | buy | COIN | 4.89 | — | rebalance up |
| 2026-11-10T19:25 | Agent (ML meta-label) | buy | AMZN | 4.88 | — | rebalance up |
| 2026-11-10T19:25 | Agent (ML meta-label) | buy | AMD | 4.85 | — | rebalance up |
| 2026-11-10T19:25 | Agent (ML meta-label) | sell | AAPL | 10.89 | -0.00 | selected signal exited |
| 2026-11-10T19:15 | Three white soldiers | sell | SOL-USD | 15.13 | -0.17 | exit signal |
| 2026-11-10T19:15 | Three white soldiers | sell | ETH-USD | 15.17 | -0.12 | exit signal |
| 2026-11-10T19:15 | Three white soldiers | sell | DOGE-USD | 15.16 | -0.09 | exit signal |
| 2026-11-10T19:05 | Agent (ML meta-label) | buy | AAPL | 10.89 | — | entry |
| 2026-11-10T19:05 | Agent (ML meta-label) | sell | SOXL | 10.88 | -0.01 | selected signal exited |
| 2026-11-10T19:05 | Three white soldiers | sell | BTC-USD | 12.16 | -0.05 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 19:55:05.000189+00:00 -> 2026-11-10 20:05:05.000189+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
