# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T14:55:05.000145+00:00 · 65781 ticks

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

Today: 13956 decisions in 2409 calls, $0.1895 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T14:55 | 2 / 7 / 21 | cash |  |
| Breezy | 2026-11-19T14:55 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-19T14:55 | 3 / 24 / 3 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.63 | 13.63 | 0 | — | 12.04 | 3.89 | -4.55 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.82 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.75 | 2.75 | 0 | — | 4.36 | 1.12 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.34 | 0.34 | 153 | 35.9 | -3.38 | -2.98 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.14 | -0.86 | 199 | 32.2 | 2.53 | 0.88 | -9.06 | 212 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.35 | -1.65 | 8 | 50.0 | -0.57 | 0.14 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 96.36 | -3.64 | 0 | — | -3.04 | -1.07 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.46 | -8.82 | -5.52 | 20 |
| 14 | Agent (rotation) | meta | 93.53 | -6.46 | 206 | 29.1 | -3.18 | -1.12 | -7.63 | 151 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.85 | -7.15 | 0 | — | -7.17 | -1.88 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 92.40 | -7.60 | 0 | — | -6.29 | -1.71 | -12.67 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 18 | Copy: Insider buying | copy | 90.47 | -9.53 | 52 | 40.4 | -8.64 | -1.67 | -14.79 | 67 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 88.66 | -11.35 | 115 | 23.5 | -15.21 | -7.44 | -15.74 | 54 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.43 | -9.25 | -16.70 | 72 |
| 23 | Daily: Bullish score | daily | 85.49 | -14.51 | 17 | 17.6 | -11.05 | -2.62 | -19.56 | 14 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.84 | -7.12 | -17.06 | 203 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -12.75 | -4.38 | -14.66 | 559 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.65 | -18.35 | 189 | 28.0 | -26.71 | -8.09 | -28.30 | 199 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -13.98 | -6.20 | -14.70 | 78 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.19 | -5.25 | -21.26 | 74 |
| 30 | Keltner breakout · 1h | breakout | 78.84 | -21.16 | 125 | 25.6 | -24.75 | -6.49 | -27.96 | 150 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 78.82 | -21.18 | 2 | 0.0 | -16.76 | -2.31 | -26.43 | 1 |
| 32 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 33 | Opening range 15m | breakout | 76.66 | -23.34 | 541 | 32.0 | -20.81 | -6.20 | -22.47 | 672 |
| 34 | ADX DI cross · 1h | trend | 75.31 | -24.69 | 209 | 19.1 | -27.10 | -4.40 | -35.03 | 267 |
| 35 | Stochastic reversion · 1h | reversion | 75.06 | -24.94 | 352 | 42.6 | -32.16 | -4.64 | -35.91 | 425 |
| 36 | Hold BTC | benchmark | 74.59 | -25.41 | 2 | 0.0 | -21.43 | -3.44 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 73.83 | -26.17 | 104 | 14.4 | -29.51 | -8.62 | -30.70 | 113 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -48.48 | -3.15 | -56.47 | 22 |
| 39 | Bollinger breakout · 1h | breakout | 72.88 | -27.12 | 192 | 21.9 | -30.70 | -8.32 | -33.86 | 217 |
| 40 | MFI reversion · 1h | reversion | 72.36 | -27.64 | 456 | 34.0 | -26.96 | -3.93 | -30.85 | 170 |
| 41 | Max aggression: 1-day momentum | meta | 71.70 | -28.30 | 32 | 28.1 | -31.44 | -1.59 | -57.50 | 39 |
| 42 | Heikin-Ashi · 1h | trend | 71.18 | -28.82 | 477 | 23.1 | -43.51 | -9.38 | -45.88 | 628 |
| 43 | Supertrend · 1h | trend | 70.54 | -29.46 | 192 | 16.7 | -33.28 | -5.66 | -39.81 | 205 |
| 44 | Triple EMA stack · 1h | trend | 69.97 | -30.03 | 157 | 14.6 | -32.99 | -6.85 | -39.69 | 173 |
| 45 | MACD cross · 1h | trend | 69.96 | -30.04 | 417 | 22.3 | -38.92 | -6.11 | -46.98 | 497 |
| 46 | MACD zero-line · 1h | trend | 69.82 | -30.18 | 184 | 17.9 | -28.14 | -5.63 | -34.63 | 209 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.36 | -4.99 | -37.91 | 31 |
| 48 | ROC + volume · 1h | momentum | 69.07 | -30.93 | 417 | 28.5 | -34.16 | -6.25 | -39.50 | 334 |
| 49 | CCI reversion · 1h | reversion | 69.04 | -30.96 | 388 | 41.5 | -40.39 | -6.49 | -44.29 | 479 |
| 50 | RSI momentum · 1h | momentum | 68.95 | -31.05 | 180 | 14.4 | -33.59 | -6.34 | -39.89 | 201 |
| 51 | EMA 20/50 cross · 1h | trend | 68.21 | -31.79 | 117 | 10.3 | -37.52 | -8.18 | -43.96 | 121 |
| 52 | OBV trend · 1h | momentum | 67.14 | -32.86 | 311 | 19.3 | -35.08 | -7.81 | -40.15 | 246 |
| 53 | Donchian 20/10 · 1h | breakout | 65.36 | -34.64 | 163 | 17.8 | -36.17 | -7.07 | -41.92 | 190 |
| 54 | Williams %R · 1h | reversion | 65.32 | -34.68 | 440 | 41.1 | -45.48 | -7.66 | -47.95 | 573 |
| 55 | Bollinger reversion · 1h | reversion | 64.07 | -35.93 | 353 | 38.5 | -37.99 | -5.72 | -39.51 | 417 |
| 56 | Agent (ML meta-label) | meta | 62.00 | -38.00 | 1954 | 24.6 | -15.97 | -2.55 | -18.23 | 291 |
| 57 | EMA 9/21 cross · 1h | trend | 61.99 | -38.01 | 285 | 11.6 | -41.10 | -8.11 | -46.71 | 326 |
| 58 | RSI(14) reversion · 1h | reversion | 60.23 | -39.77 | 214 | 34.6 | -39.02 | -5.59 | -43.22 | 265 |
| 59 | Z-score reversion · 1h | reversion | 58.64 | -41.36 | 227 | 35.2 | -35.42 | -4.78 | -39.63 | 260 |
| 60 | Candlestick reversal · 1h | reversion | 56.82 | -43.18 | 561 | 27.3 | -46.11 | -8.22 | -48.43 | 655 |
| 61 | VWAP momentum · 1h | momentum | 56.66 | -43.34 | 988 | 21.6 | -56.71 | -11.31 | -60.43 | 1208 |
| 62 | Three white soldiers | momentum | 53.92 | -46.08 | 598 | 14.5 | -51.03 | -23.18 | -51.09 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.08 | -46.81 | -99.09 | 5353 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.70 | -29.69 | -82.84 | 1408 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.28 | -47.99 | -94.29 | 2474 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.54 | -35.47 | -90.58 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.80 | -46.12 | -91.80 | 2304 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.17 | -31.50 | -90.17 | 2057 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.03 | -52.80 | -98.04 | 3481 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.75 | -58.30 | -96.76 | 3423 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -38.55 | -93.71 | 2216 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.16 | -36.23 | -83.26 | 1595 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -54.12 | -99.61 | 6111 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.58 | -48.32 | -92.58 | 2565 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.67 | -39.09 | -94.67 | 3198 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -75.40 | -99.83 | 6200 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.93 | -49.28 | -92.93 | 2266 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.37 | -27.99 | -77.37 | 1660 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -62.12 | -97.79 | 3414 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.08 | -57.74 | -99.08 | 4984 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.41 | -29.90 | -70.43 | 1242 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.92 | -57.38 | -94.92 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.79 | -41.57 | -85.79 | 1740 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -70.07 | -99.71 | 6417 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.85 | -31.13 | -91.02 | 2370 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.87 | -19.04 | -80.33 | 1842 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.62 | -37.26 | -91.66 | 2162 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.61 | -45.94 | -97.61 | 3918 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.62 | -61.09 | -89.62 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.38 | -32.20 | -67.43 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.67 | -28.36 | -73.67 | 1219 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.45 | -18.40 | -81.67 | 1750 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -45.65 | -97.58 | 4327 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -113.46 | -99.94 | 8438 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T14:55 | Agent (rotation) | sell | TECL | 5.14 | -0.08 | selected signal exited |
| 2026-11-19T14:55 | Agent (rotation) | sell | PLTR | 7.75 | -0.05 | selected signal exited |
| 2026-11-19T14:55 | Agent (rotation) | sell | NVDA | 5.15 | -0.07 | selected signal exited |
| 2026-11-19T14:55 | Agent (rotation) | sell | BITX | 4.43 | -0.05 | selected signal exited |
| 2026-11-19T14:55 | Day trade: Stocks in Play ORB | buy | AMZN | 25.09 | — | entry |
| 2026-11-19T14:55 | Agent (ML meta-label) | buy | TNA | 3.80 | — | rebalance up |
| 2026-11-19T14:55 | Agent (ML meta-label) | buy | SQQQ | 8.79 | — | following Connors RSI(2), Squeeze breakout |
| 2026-11-19T14:55 | Agent (ML meta-label) | sell | TECL | 8.76 | -0.14 | selected signal exited |
| 2026-11-19T14:55 | Agent (ML meta-label) | sell | AAPL | 6.91 | -0.04 | selected signal exited |
| 2026-11-19T14:55 | Candlestick reversal · 1h | sell | AAPL | 3.06 | -0.02 | stop-loss |
| 2026-11-19T14:55 | ROC + volume · 1h | sell | AMZN | 17.57 | 0.47 | target is flat |
| 2026-11-19T14:55 | ROC + volume · 1h | sell | AMD | 18.28 | 1.18 | target is flat |
| 2026-11-19T14:55 | Parabolic SAR · 1h | sell | AAPL | 13.55 | -0.19 | stop-loss |
| 2026-11-19T14:55 | Triple EMA stack · 1h | buy | DOGE-USD | 3.51 | — | rebalance up |
| 2026-11-19T14:55 | Triple EMA stack · 1h | sell | SQQQ | 3.51 | -0.04 | rebalance down |
| 2026-11-19T14:55 | Gap and go | buy | SOXL | 8.31 | — | rebalance up |
| 2026-11-19T14:55 | Gap and go | buy | MSFT | 8.13 | — | rebalance up |
| 2026-11-19T14:55 | Gap and go | buy | AMD | 8.15 | — | rebalance up |
| 2026-11-19T14:55 | Gap and go | sell | TECL | 16.43 | -0.27 | exit signal |
| 2026-11-19T14:55 | Gap and go | sell | PLTR | 16.47 | -0.10 | exit signal |
| 2026-11-19T14:55 | Gap and go | sell | NVDA | 16.46 | -0.24 | stop-loss |
| 2026-11-19T14:50 | Agent (rotation) | buy | BITX | 4.48 | — | entry |
| 2026-11-19T14:50 | Agent (ML meta-label) | buy | AAPL | 6.95 | — | entry |
| 2026-11-19T14:50 | Agent (ML meta-label) | sell | NVDA | 3.46 | 0.14 | rebalance down |
| 2026-11-19T14:50 | Agent (ML meta-label) | sell | AMD | 3.64 | 0.25 | rebalance down |
| 2026-11-19T14:50 | Opening range 15m | buy | TECL | 19.43 | — | entry signal |
| 2026-11-19T14:50 | Opening range 15m | buy | SOXL | 19.43 | — | entry signal |
| 2026-11-19T14:50 | Opening range 15m | buy | MSFT | 19.43 | — | entry signal |
| 2026-11-19T14:50 | Opening range 15m | buy | AMD | 19.43 | — | entry signal |
| 2026-11-19T14:45 | Agent (rotation) | buy | TECL | 5.22 | — | entry |
| 2026-11-19T14:45 | Agent (rotation) | buy | SOXL | 5.22 | — | following CCI reversion, Z-score reversion |
| 2026-11-19T14:45 | Agent (rotation) | buy | NVDA | 5.22 | — | entry |
| 2026-11-19T14:45 | Agent (rotation) | buy | MSFT | 5.22 | — | entry |
| 2026-11-19T14:45 | Agent (rotation) | buy | AMD | 5.22 | — | entry |
| 2026-11-19T14:45 | Agent (rotation) | sell | TQQQ | 31.23 | -0.10 | selected signal exited |
| 2026-11-19T14:45 | Day trade: Stocks in Play ORB | sell | TQQQ | 25.26 | 0.23 | target is flat |
| 2026-11-19T14:45 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 112.50 | -0.36 | target is flat |
| 2026-11-19T14:45 | Agent (ML meta-label) | buy | TECL | 8.91 | — | entry |
| 2026-11-19T14:45 | Agent (ML meta-label) | sell | SQQQ | 9.29 | -0.65 | selected signal exited |
| 2026-11-19T14:45 | Bollinger reversion · 1h | buy | IWM | 3.21 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 14:55:05.000145+00:00 -> 2026-11-19 15:05:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 14:55:05.000145+00:00 -> 2026-11-19 15:05:05.000145+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
