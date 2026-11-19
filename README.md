# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T15:25:05.000127+00:00 · 65802 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.17 (-14.83%)

Closed trades 225, win rate 36.4%, fees £6.17, max drawdown -17.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-19 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, LRN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-18)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 33.12 · VIX 24.56 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 6.2, AMZN 6.2, TSLA 4.1, AMD 3.9, META 1.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 15855 decisions in 2472 calls, $0.2117 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T15:25 | 1 / 8 / 21 | cash |  |
| Breezy | 2026-11-19T15:25 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-19T15:25 | 5 / 21 / 4 | BITX 56% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.97% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| Connors RSI(2) | SQQQ | 1.81 | +3.66% | 10 |
| Squeeze breakout | SQQQ | 1.74 | +6.13% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.70 | 13.70 | 0 | — | 12.07 | 3.91 | -4.55 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.90 | 11.90 | 25 | 64.0 | 19.27 | 3.92 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.82 | 2.82 | 0 | — | 3.92 | 1.14 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -3.87 | -3.43 | -4.83 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | 1.17 | 0.45 | -9.06 | 212 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.52 | -3.48 | 8 | 50.0 | -2.19 | -0.06 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.77 | -4.23 | 0 | — | -3.61 | -1.29 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.78 | -5.44 | 20 |
| 14 | Agent (rotation) | meta | 93.36 | -6.64 | 210 | 28.6 | -3.45 | -1.23 | -7.63 | 152 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.85 | -7.15 | 0 | — | -7.17 | -1.88 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 92.61 | -7.39 | 0 | — | -6.42 | -1.65 | -12.67 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 18 | Copy: Insider buying | copy | 90.71 | -9.29 | 52 | 40.4 | -8.66 | -1.67 | -14.79 | 67 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 88.66 | -11.35 | 115 | 23.5 | -15.40 | -7.49 | -15.91 | 55 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -15.95 | -9.05 | -16.16 | 70 |
| 23 | Daily: Bullish score | daily | 85.92 | -14.08 | 17 | 17.6 | -11.16 | -2.54 | -19.56 | 14 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.84 | -7.12 | -17.06 | 203 |
| 25 | Opening range 30m | breakout | 84.98 | -15.02 | 447 | 33.6 | -12.78 | -4.39 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.22 | -18.78 | 189 | 28.0 | -27.45 | -8.46 | -28.30 | 198 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -13.98 | -6.20 | -14.70 | 78 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.18 | -5.24 | -21.26 | 74 |
| 30 | Keltner breakout · 1h | breakout | 78.58 | -21.42 | 125 | 25.6 | -24.61 | -6.59 | -27.35 | 149 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.88 | -6.79 | -30.73 | 84 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 78.29 | -21.71 | 2 | 0.0 | -17.53 | -2.42 | -26.43 | 1 |
| 33 | Opening range 15m | breakout | 76.05 | -23.95 | 545 | 31.7 | -21.54 | -6.34 | -23.19 | 674 |
| 34 | ADX DI cross · 1h | trend | 74.90 | -25.10 | 209 | 19.1 | -26.98 | -4.37 | -34.78 | 265 |
| 35 | Hold BTC | benchmark | 74.28 | -25.72 | 2 | 0.0 | -22.05 | -3.51 | -28.91 | 1 |
| 36 | Stochastic reversion · 1h | reversion | 74.22 | -25.78 | 352 | 42.6 | -33.14 | -4.90 | -35.86 | 426 |
| 37 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -48.63 | -3.16 | -56.74 | 22 |
| 38 | Ichimoku · 1h | trend | 73.59 | -26.41 | 104 | 14.4 | -29.74 | -8.71 | -30.92 | 113 |
| 39 | Bollinger breakout · 1h | breakout | 72.83 | -27.17 | 192 | 21.9 | -31.10 | -8.52 | -34.08 | 217 |
| 40 | MFI reversion · 1h | reversion | 71.87 | -28.13 | 456 | 34.0 | -27.72 | -4.10 | -31.02 | 170 |
| 41 | Supertrend · 1h | trend | 70.68 | -29.32 | 192 | 16.7 | -33.23 | -5.65 | -39.86 | 205 |
| 42 | Heikin-Ashi · 1h | trend | 70.19 | -29.81 | 478 | 23.0 | -44.19 | -9.66 | -45.86 | 628 |
| 43 | Triple EMA stack · 1h | trend | 70.02 | -29.98 | 157 | 14.6 | -33.25 | -6.95 | -39.65 | 173 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.35 | -4.99 | -37.91 | 31 |
| 45 | MACD zero-line · 1h | trend | 69.40 | -30.60 | 184 | 17.9 | -28.65 | -5.76 | -34.68 | 209 |
| 46 | MACD cross · 1h | trend | 68.96 | -31.04 | 417 | 22.3 | -39.54 | -6.31 | -46.90 | 497 |
| 47 | Max aggression: 1-day momentum | meta | 68.92 | -31.08 | 32 | 28.1 | -34.09 | -1.87 | -57.50 | 39 |
| 48 | ROC + volume · 1h | momentum | 68.73 | -31.27 | 417 | 28.5 | -34.60 | -6.36 | -39.70 | 336 |
| 49 | EMA 20/50 cross · 1h | trend | 68.55 | -31.45 | 117 | 10.3 | -37.26 | -8.31 | -43.54 | 121 |
| 50 | RSI momentum · 1h | momentum | 68.51 | -31.49 | 180 | 14.4 | -33.79 | -6.24 | -40.29 | 201 |
| 51 | CCI reversion · 1h | reversion | 68.40 | -31.60 | 388 | 41.5 | -41.35 | -6.80 | -44.29 | 478 |
| 52 | OBV trend · 1h | momentum | 67.42 | -32.58 | 311 | 19.3 | -34.79 | -7.67 | -40.21 | 246 |
| 53 | Donchian 20/10 · 1h | breakout | 65.36 | -34.64 | 163 | 17.8 | -35.84 | -6.95 | -41.73 | 189 |
| 54 | Williams %R · 1h | reversion | 64.45 | -35.55 | 440 | 41.1 | -46.03 | -7.92 | -47.80 | 573 |
| 55 | Bollinger reversion · 1h | reversion | 63.45 | -36.55 | 353 | 38.5 | -38.73 | -5.90 | -39.63 | 417 |
| 56 | EMA 9/21 cross · 1h | trend | 61.93 | -38.07 | 285 | 11.6 | -40.80 | -8.02 | -46.84 | 325 |
| 57 | Agent (ML meta-label) | meta | 61.19 | -38.81 | 1960 | 24.7 | -15.70 | -2.17 | -21.03 | 283 |
| 58 | RSI(14) reversion · 1h | reversion | 59.83 | -40.17 | 214 | 34.6 | -39.25 | -5.66 | -43.22 | 261 |
| 59 | Z-score reversion · 1h | reversion | 58.05 | -41.95 | 227 | 35.2 | -36.16 | -4.95 | -39.63 | 260 |
| 60 | Candlestick reversal · 1h | reversion | 56.43 | -43.57 | 563 | 27.2 | -46.19 | -8.32 | -48.43 | 652 |
| 61 | VWAP momentum · 1h | momentum | 56.10 | -43.90 | 989 | 21.5 | -57.13 | -11.54 | -60.43 | 1208 |
| 62 | Three white soldiers | momentum | 53.92 | -46.08 | 598 | 14.5 | -51.03 | -23.18 | -51.09 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.08 | -47.64 | -99.08 | 5342 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.89 | -30.27 | -83.05 | 1409 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.34 | -47.62 | -94.34 | 2459 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.61 | -35.55 | -90.64 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.94 | -46.62 | -91.94 | 2300 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.28 | -31.55 | -90.29 | 2060 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.05 | -53.02 | -98.06 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.79 | -57.75 | -96.79 | 3422 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.86 | -37.07 | -93.87 | 2224 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.51 | -35.94 | -83.52 | 1597 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -54.53 | -99.61 | 6119 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -47.59 | -92.71 | 2561 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.71 | -39.16 | -94.71 | 3206 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -75.38 | -99.83 | 6191 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.93 | -49.43 | -92.94 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.50 | -27.86 | -77.52 | 1660 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -61.99 | -97.80 | 3409 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.08 | -57.91 | -99.08 | 4982 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.83 | -29.89 | -70.83 | 1245 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.89 | -57.39 | -94.89 | 2751 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.87 | -41.08 | -85.89 | 1739 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -70.94 | -99.71 | 6411 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.84 | -31.15 | -91.01 | 2372 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.87 | -18.85 | -80.43 | 1836 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.52 | -36.62 | -91.61 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.62 | -46.42 | -97.62 | 3924 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.79 | -61.55 | -89.81 | 2168 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.43 | -31.84 | -67.48 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.06 | -28.48 | -74.14 | 1218 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.58 | -18.41 | -81.71 | 1749 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -45.40 | -97.58 | 4326 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.58 | -99.94 | 8431 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T15:25 | Day trade: Stocks in Play ORB | sell | LABU | 24.54 | -0.53 | target is flat |
| 2026-11-19T15:25 | Agent (ML meta-label) | buy | TNA | 5.08 | — | rebalance up |
| 2026-11-19T15:25 | Agent (ML meta-label) | buy | SOXL | 5.20 | — | rebalance up |
| 2026-11-19T15:25 | Agent (ML meta-label) | buy | LABU | 3.08 | — | rebalance up |
| 2026-11-19T15:25 | Agent (ML meta-label) | buy | AMD | 5.10 | — | rebalance up |
| 2026-11-19T15:25 | Agent (ML meta-label) | sell | SQQQ | 8.24 | 0.13 | selected signal exited |
| 2026-11-19T15:25 | Agent (ML meta-label) | sell | NVDA | 10.22 | -0.09 | selected signal exited |
| 2026-11-19T15:20 | Agent (rotation) | buy | SQQQ | 31.07 | — | following Connors RSI(2), Squeeze breakout |
| 2026-11-19T15:20 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 111.39 | — | entry |
| 2026-11-19T15:15 | Agent (rotation) | sell | SOXL | 5.05 | -0.17 | selected signal exited |
| 2026-11-19T15:15 | Agent (rotation) | sell | PLTR | 7.66 | -0.14 | selected signal exited |
| 2026-11-19T15:15 | Agent (rotation) | sell | MSFT | 5.18 | -0.04 | selected signal exited |
| 2026-11-19T15:15 | Agent (ML meta-label) | buy | SQQQ | 8.11 | — | following Connors RSI(2), Squeeze breakout |
| 2026-11-19T15:15 | Agent (ML meta-label) | buy | NVDA | 6.61 | — | rebalance up |
| 2026-11-19T15:15 | Agent (ML meta-label) | sell | TNA | 5.14 | -0.03 | rebalance down |
| 2026-11-19T15:15 | Agent (ML meta-label) | sell | SOXL | 4.66 | 0.14 | rebalance down |
| 2026-11-19T15:15 | Agent (ML meta-label) | sell | AMD | 4.93 | 0.02 | rebalance down |
| 2026-11-19T15:15 | Opening range 30m | buy | SQQQ | 21.27 | — | entry signal |
| 2026-11-19T15:15 | Opening range 15m | buy | SQQQ | 19.04 | — | entry signal |
| 2026-11-19T15:15 | Opening range 15m | sell | SOXL | 18.65 | -0.78 | stop-loss |
| 2026-11-19T15:15 | Opening range 15m | sell | MSFT | 19.25 | -0.17 | exit signal |
| 2026-11-19T15:15 | Gap and go | sell | SOXL | 24.29 | -0.71 | stop-loss |
| 2026-11-19T15:15 | Gap and go | sell | PLTR | 24.39 | -0.44 | stop-loss |
| 2026-11-19T15:15 | Gap and go | sell | MSFT | 24.65 | -0.18 | exit signal |
| 2026-11-19T15:10 | Day trade: Stocks in Play ORB | buy | LABU | 25.08 | — | entry |
| 2026-11-19T15:10 | Agent (ML meta-label) | buy | NVDA | 3.70 | — | entry |
| 2026-11-19T15:10 | Agent (ML meta-label) | sell | LABU | 3.70 | 0.12 | rebalance down |
| 2026-11-19T15:10 | Opening range 30m | buy | LABU | 21.27 | — | entry signal |
| 2026-11-19T15:10 | Opening range 15m | buy | LABU | 19.17 | — | entry signal |
| 2026-11-19T15:10 | Opening range 15m | sell | TECL | 19.19 | -0.23 | target is flat |
| 2026-11-19T15:05 | Agent (rotation) | buy | PLTR | 7.80 | — | entry |
| 2026-11-19T15:05 | Agent (ML meta-label) | buy | TNA | 6.71 | — | rebalance up |
| 2026-11-19T15:05 | Agent (ML meta-label) | buy | SOXL | 7.21 | — | rebalance up |
| 2026-11-19T15:05 | Agent (ML meta-label) | buy | LABU | 5.54 | — | rebalance up |
| 2026-11-19T15:05 | Agent (ML meta-label) | buy | AMD | 8.68 | — | rebalance up |
| 2026-11-19T15:05 | Agent (ML meta-label) | sell | TECL | 3.66 | 0.03 | selected signal exited |
| 2026-11-19T15:05 | Agent (ML meta-label) | sell | SQQQ | 8.69 | -0.09 | selected signal exited |
| 2026-11-19T15:05 | Agent (ML meta-label) | sell | SPY | 8.90 | -0.02 | selected signal exited |
| 2026-11-19T15:05 | Agent (ML meta-label) | sell | NVDA | 6.89 | 0.22 | selected signal exited |
| 2026-11-19T15:05 | Gap and go | buy | PLTR | 24.83 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 15:25:05.000127+00:00 -> 2026-11-19 15:35:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 15:25:05.000127+00:00 -> 2026-11-19 15:35:05.000127+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
