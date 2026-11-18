# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T22:25:05.000124+00:00 · 64895 ticks

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
| Copy: Insider buying | 2026-11-18 | PEPG 12%, FUN 12%, STWD 12%, LRN 12%, PSEC 12%, TEAM 12%, BH 12%, LILA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-18)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 33.34 · VIX 24.41 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 6.2, AMZN 6.2, TSLA 4.1, AMD 3.9, META 1.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 39072 decisions in 3399 calls, $0.4858 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T22:25 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-18T22:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T22:25 | 2 / 2 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| OBV trend | SQQQ | 1.77 | +6.24% | 9 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.66 | 14.66 | 0 | — | 13.21 | 4.39 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.82 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.89 | 3.89 | 0 | — | 4.56 | 1.32 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 152 | 35.5 | -3.30 | -2.89 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.41 | 1.16 | -9.06 | 205 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.96 | -4.04 | 8 | 50.0 | -4.05 | -0.14 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.63 | -4.37 | 0 | — | -3.89 | -1.27 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.24 | -1.50 | -8.79 | 151 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.95 | -7.93 | -5.54 | 20 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.90 | -7.10 | 0 | — | -6.94 | -1.82 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.30 | -8.70 | 0 | — | -7.46 | -2.00 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.20 | -9.80 | 114 | 23.7 | -15.26 | -7.45 | -15.58 | 61 |
| 19 | Copy: Insider buying | copy | 90.06 | -9.94 | 52 | 40.4 | -10.48 | -2.12 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.88 | -3.79 | -18.48 | 150 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.04 | -12.96 | 17 | 17.6 | -7.35 | -1.38 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.08 | -9.17 | -18.13 | 72 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.17 | -6.58 | -16.41 | 204 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -11.99 | -4.05 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.66 | -18.34 | 188 | 28.2 | -24.13 | -6.66 | -27.22 | 197 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.36 | -6.39 | -14.68 | 86 |
| 29 | Keltner breakout · 1h | breakout | 79.88 | -20.12 | 124 | 25.8 | -23.19 | -6.37 | -25.90 | 148 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.12 | -5.22 | -21.21 | 73 |
| 31 | Max aggression: 5-day momentum | meta | 79.16 | -20.84 | 21 | 42.9 | -47.98 | -3.20 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.73 | -21.27 | 78 | 12.8 | -25.72 | -6.75 | -30.58 | 84 |
| 33 | Opening range 15m | breakout | 77.70 | -22.30 | 541 | 32.0 | -19.89 | -5.93 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.96 | -23.04 | 2 | 0.0 | -18.99 | -2.58 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.55 | -24.45 | 209 | 19.1 | -26.24 | -4.25 | -34.88 | 266 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 37 | Hold BTC | benchmark | 73.24 | -26.75 | 2 | 0.0 | -18.56 | -2.61 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.65 | -8.30 | -33.72 | 216 |
| 39 | Stochastic reversion · 1h | reversion | 72.87 | -27.13 | 351 | 42.5 | -34.63 | -5.27 | -35.78 | 424 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -38.62 | -2.34 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.63 | -28.37 | 191 | 16.2 | -32.57 | -5.41 | -39.71 | 200 |
| 42 | Triple EMA stack · 1h | trend | 70.72 | -29.28 | 157 | 14.6 | -30.75 | -6.24 | -37.72 | 172 |
| 43 | MFI reversion · 1h | reversion | 70.40 | -29.60 | 452 | 33.4 | -27.40 | -4.08 | -30.08 | 176 |
| 44 | RSI momentum · 1h | momentum | 70.36 | -29.64 | 179 | 14.5 | -31.46 | -5.71 | -38.37 | 198 |
| 45 | Heikin-Ashi · 1h | trend | 69.91 | -30.09 | 474 | 23.0 | -44.09 | -9.64 | -45.85 | 629 |
| 46 | MACD zero-line · 1h | trend | 69.84 | -30.16 | 184 | 17.9 | -28.09 | -5.60 | -34.29 | 203 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.17 | -30.83 | 116 | 10.3 | -36.97 | -9.42 | -40.88 | 118 |
| 49 | ROC + volume · 1h | momentum | 69.01 | -30.99 | 413 | 28.1 | -34.13 | -6.25 | -39.51 | 342 |
| 50 | OBV trend · 1h | momentum | 68.24 | -31.76 | 310 | 19.4 | -34.43 | -7.30 | -39.87 | 249 |
| 51 | MACD cross · 1h | trend | 67.70 | -32.30 | 417 | 22.3 | -41.09 | -6.72 | -46.93 | 490 |
| 52 | CCI reversion · 1h | reversion | 67.11 | -32.89 | 387 | 41.6 | -42.24 | -7.09 | -44.29 | 473 |
| 53 | Donchian 20/10 · 1h | breakout | 66.54 | -33.46 | 162 | 17.9 | -36.28 | -7.03 | -41.19 | 194 |
| 54 | Bollinger reversion · 1h | reversion | 63.63 | -36.37 | 348 | 37.9 | -39.03 | -5.96 | -39.61 | 417 |
| 55 | Williams %R · 1h | reversion | 63.57 | -36.43 | 437 | 40.7 | -46.68 | -8.14 | -47.31 | 566 |
| 56 | EMA 9/21 cross · 1h | trend | 62.82 | -37.18 | 285 | 11.6 | -39.64 | -7.78 | -45.71 | 321 |
| 57 | Agent (ML meta-label) | meta | 60.12 | -39.88 | 1949 | 24.6 | -23.79 | -4.16 | -25.70 | 310 |
| 58 | RSI(14) reversion · 1h | reversion | 58.82 | -41.18 | 206 | 32.0 | -40.97 | -6.07 | -43.22 | 255 |
| 59 | Z-score reversion · 1h | reversion | 57.44 | -42.56 | 227 | 35.2 | -36.91 | -5.10 | -39.53 | 257 |
| 60 | VWAP momentum · 1h | momentum | 55.26 | -44.74 | 987 | 21.5 | -56.35 | -11.05 | -60.32 | 1206 |
| 61 | Candlestick reversal · 1h | reversion | 55.17 | -44.83 | 552 | 26.4 | -47.64 | -8.76 | -48.90 | 639 |
| 62 | Three white soldiers | momentum | 54.64 | -45.36 | 589 | 14.4 | -49.74 | -22.01 | -50.82 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -42.57 | -99.05 | 5271 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.86 | -27.59 | -82.56 | 1405 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -42.97 | -94.02 | 2458 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.74 | -30.05 | -90.40 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.17 | -40.53 | -91.50 | 2303 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.96 | -30.66 | -90.11 | 2068 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.85 | -45.75 | -97.95 | 3467 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -53.44 | -96.43 | 3383 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.36 | -37.94 | -93.36 | 2192 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.74 | -35.41 | -82.82 | 1582 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -55.30 | -99.61 | 6107 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.90 | -42.94 | -92.17 | 2548 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.77 | -38.89 | -94.79 | 3223 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.26 | -99.81 | 6197 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.46 | -43.54 | -92.67 | 2258 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.01 | -27.18 | -76.40 | 1638 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -61.60 | -97.73 | 3429 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.55 | -99.07 | 4971 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.25 | -28.68 | -70.13 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -55.45 | -94.69 | 2751 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.69 | -37.50 | -85.19 | 1730 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -71.05 | -99.70 | 6403 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.84 | -31.30 | -91.03 | 2364 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.95 | -19.11 | -80.36 | 1837 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.35 | -36.80 | -91.45 | 2151 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.60 | -46.77 | -97.60 | 3916 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.18 | -56.50 | -89.46 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.26 | -31.03 | -67.02 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.90 | -25.13 | -73.12 | 1217 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.68 | -18.38 | -81.88 | 1760 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -46.52 | -97.56 | 4329 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -116.11 | -99.94 | 8447 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T20:56 | Agent (ML meta-label) | buy | TQQQ | 1.41 | — | entry |
| 2026-11-18T20:56 | Agent (ML meta-label) | buy | TECL | 8.54 | — | entry |
| 2026-11-18T20:56 | Agent (ML meta-label) | sell | TNA | 9.95 | 0.01 | selected signal exited |
| 2026-11-18T20:55 | Day trade: Stocks in Play ORB | sell | TNA | 25.21 | 0.27 | target is flat |
| 2026-11-18T20:55 | Day trade: Stocks in Play ORB | sell | IWM | 25.04 | 0.10 | target is flat |
| 2026-11-18T20:55 | Opening range 30m | sell | TNA | 20.85 | -0.16 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 30m | sell | IWM | 21.16 | -0.06 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 30m | sell | AMZN | 22.01 | 0.41 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 30m | sell | AMD | 21.05 | 0.25 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 15m | sell | TNA | 19.28 | 0.06 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 15m | sell | IWM | 15.52 | 0.04 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 15m | sell | AMZN | 15.72 | 0.30 | end-of-day flatten |
| 2026-11-18T20:55 | Opening range 15m | sell | AMD | 18.63 | 0.22 | end-of-day flatten |
| 2026-11-18T20:45 | Agent (ML meta-label) | buy | TNA | 8.56 | — | rebalance up |
| 2026-11-18T20:45 | Agent (ML meta-label) | sell | SPY | 8.56 | -0.00 | selected signal exited |
| 2026-11-18T20:40 | Agent (aggressive) | sell | SOXL | 42.38 | 0.71 | selected signal exited |
| 2026-11-18T20:40 | Agent | sell | SOXL | 17.26 | 0.29 | selected signal exited |
| 2026-11-18T20:35 | Agent (ML meta-label) | buy | TNA | 1.38 | — | entry |
| 2026-11-18T20:35 | Agent (ML meta-label) | buy | SPY | 8.56 | — | following Squeeze breakout |
| 2026-11-18T20:30 | Agent (ML meta-label) | sell | TQQQ | 9.94 | -0.13 | selected signal exited |
| 2026-11-18T20:30 | MFI reversion · 1h | buy | SPY | 4.44 | — | entry |
| 2026-11-18T20:30 | MFI reversion · 1h | sell | TQQQ | 4.44 | -0.01 | exit signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | PLTR | 11.00 | — | entry signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | MSFT | 3.15 | — | rebalance up |
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | GOOGL | 3.14 | — | rebalance up |
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | AMZN | 11.01 | — | entry |
| 2026-11-18T20:30 | VWAP momentum · 1h | buy | AMD | 3.13 | — | rebalance up |
| 2026-11-18T20:30 | VWAP momentum · 1h | sell | TQQQ | 7.83 | -0.08 | exit signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | sell | TECL | 7.86 | -0.09 | exit signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | sell | SPY | 7.87 | -0.02 | exit signal |
| 2026-11-18T20:30 | VWAP momentum · 1h | sell | QQQ | 7.87 | -0.03 | exit signal |
| 2026-11-18T20:30 | Trend pullback · 1h | sell | AAPL | 22.50 | -0.07 | exit signal |
| 2026-11-18T20:30 | Heikin-Ashi · 1h | buy | GOOGL | 17.41 | — | entry signal |
| 2026-11-18T20:30 | Triple EMA stack · 1h | buy | AMZN | 17.70 | — | entry signal |
| 2026-11-18T20:25 | MFI reversion · 1h | buy | TQQQ | 3.26 | — | rebalance up |
| 2026-11-18T20:25 | MFI reversion · 1h | buy | TECL | 5.86 | — | entry |
| 2026-11-18T20:25 | MFI reversion · 1h | buy | MSTR | 5.86 | — | entry |
| 2026-11-18T20:25 | MFI reversion · 1h | sell | SPY | 7.06 | -0.03 | target is flat |
| 2026-11-18T20:25 | MFI reversion · 1h | sell | AMD | 7.15 | 0.12 | target is flat |
| 2026-11-18T20:15 | Agent | sell | TSLA | 17.05 | 0.04 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 22:25:05.000124+00:00 -> 2026-11-18 22:35:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 22:25:05.000124+00:00 -> 2026-11-18 22:35:05.000124+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
