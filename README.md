# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T21:25:05.000141+00:00 · 64845 ticks

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

Today: 38322 decisions in 3249 calls, $0.4753 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T21:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-18T21:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T21:25 | 1 / 4 / 0 | ETH-USD 64% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.74 | 14.74 | 0 | — | 13.21 | 4.39 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.82 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.96 | 3.96 | 0 | — | 4.56 | 1.32 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 152 | 35.5 | -3.29 | -2.89 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.41 | 1.16 | -9.06 | 205 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.02 | -3.98 | 8 | 50.0 | -4.05 | -0.14 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.70 | -4.30 | 0 | — | -3.89 | -1.27 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.24 | -1.50 | -8.79 | 151 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.95 | -7.93 | -5.54 | 20 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.55 | -7.45 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.25 | -8.75 | 0 | — | -7.58 | -2.04 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.21 | -9.79 | 114 | 23.7 | -15.26 | -7.45 | -15.58 | 61 |
| 19 | Copy: Insider buying | copy | 90.12 | -9.88 | 52 | 40.4 | -10.49 | -2.12 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.88 | -3.79 | -18.48 | 150 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.08 | -12.92 | 17 | 17.6 | -7.35 | -1.38 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.08 | -9.17 | -18.13 | 72 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.17 | -6.58 | -16.41 | 204 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -11.98 | -4.05 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.69 | -18.31 | 188 | 28.2 | -24.13 | -6.66 | -27.22 | 197 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.36 | -6.39 | -14.68 | 86 |
| 29 | Keltner breakout · 1h | breakout | 79.91 | -20.09 | 124 | 25.8 | -23.48 | -6.45 | -25.90 | 148 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.12 | -5.22 | -21.21 | 73 |
| 31 | Max aggression: 5-day momentum | meta | 79.22 | -20.78 | 21 | 42.9 | -47.98 | -3.20 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.89 | -21.11 | 78 | 12.8 | -25.58 | -6.72 | -30.57 | 84 |
| 33 | Opening range 15m | breakout | 77.70 | -22.30 | 541 | 32.0 | -19.89 | -5.92 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.01 | -22.99 | 2 | 0.0 | -18.99 | -2.58 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.60 | -24.40 | 209 | 19.1 | -26.24 | -4.25 | -34.88 | 266 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 37 | Hold BTC | benchmark | 73.29 | -26.71 | 2 | 0.0 | -18.34 | -2.61 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.65 | -8.30 | -33.72 | 216 |
| 39 | Stochastic reversion · 1h | reversion | 72.89 | -27.11 | 351 | 42.5 | -34.64 | -5.27 | -35.78 | 424 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -38.66 | -2.34 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.72 | -28.28 | 191 | 16.2 | -32.52 | -5.40 | -39.71 | 200 |
| 42 | Triple EMA stack · 1h | trend | 70.75 | -29.25 | 157 | 14.6 | -30.75 | -6.24 | -37.72 | 172 |
| 43 | MFI reversion · 1h | reversion | 70.47 | -29.53 | 452 | 33.4 | -27.38 | -4.08 | -30.08 | 176 |
| 44 | RSI momentum · 1h | momentum | 70.38 | -29.62 | 179 | 14.5 | -31.46 | -5.71 | -38.37 | 198 |
| 45 | Heikin-Ashi · 1h | trend | 69.95 | -30.05 | 474 | 23.0 | -44.39 | -9.75 | -45.85 | 631 |
| 46 | MACD zero-line · 1h | trend | 69.85 | -30.15 | 184 | 17.9 | -28.09 | -5.60 | -34.29 | 203 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.32 | -30.68 | 116 | 10.3 | -36.87 | -9.39 | -40.84 | 118 |
| 49 | ROC + volume · 1h | momentum | 69.06 | -30.94 | 413 | 28.1 | -34.17 | -6.26 | -39.51 | 342 |
| 50 | OBV trend · 1h | momentum | 68.27 | -31.73 | 310 | 19.4 | -34.42 | -7.30 | -39.87 | 249 |
| 51 | MACD cross · 1h | trend | 67.73 | -32.27 | 417 | 22.3 | -41.22 | -6.75 | -46.93 | 490 |
| 52 | CCI reversion · 1h | reversion | 67.14 | -32.86 | 387 | 41.6 | -42.18 | -7.08 | -44.29 | 472 |
| 53 | Donchian 20/10 · 1h | breakout | 66.55 | -33.45 | 162 | 17.9 | -36.05 | -6.98 | -41.19 | 194 |
| 54 | Bollinger reversion · 1h | reversion | 63.74 | -36.26 | 348 | 37.9 | -38.98 | -5.95 | -39.61 | 417 |
| 55 | Williams %R · 1h | reversion | 63.63 | -36.37 | 437 | 40.7 | -46.64 | -8.14 | -47.31 | 566 |
| 56 | EMA 9/21 cross · 1h | trend | 62.84 | -37.16 | 285 | 11.6 | -39.64 | -7.78 | -45.71 | 321 |
| 57 | Agent (ML meta-label) | meta | 60.12 | -39.88 | 1949 | 24.6 | -24.71 | -4.66 | -25.96 | 294 |
| 58 | RSI(14) reversion · 1h | reversion | 58.84 | -41.16 | 206 | 32.0 | -40.93 | -6.06 | -43.22 | 256 |
| 59 | Z-score reversion · 1h | reversion | 57.46 | -42.54 | 227 | 35.2 | -36.94 | -5.11 | -39.53 | 257 |
| 60 | VWAP momentum · 1h | momentum | 55.30 | -44.70 | 987 | 21.5 | -56.35 | -11.05 | -60.32 | 1206 |
| 61 | Candlestick reversal · 1h | reversion | 55.21 | -44.79 | 552 | 26.4 | -47.61 | -8.75 | -48.90 | 638 |
| 62 | Three white soldiers | momentum | 54.64 | -45.36 | 589 | 14.4 | -49.74 | -22.01 | -50.82 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -42.53 | -99.05 | 5272 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.79 | -27.31 | -82.56 | 1405 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.75 | -42.57 | -94.02 | 2458 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.69 | -29.58 | -90.40 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -39.84 | -91.50 | 2302 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.95 | -30.66 | -90.11 | 2068 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -46.31 | -97.94 | 3469 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -52.53 | -96.43 | 3382 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.34 | -37.79 | -93.35 | 2191 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.74 | -35.41 | -82.82 | 1582 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -55.16 | -99.60 | 6104 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.90 | -43.12 | -92.17 | 2548 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.78 | -38.88 | -94.79 | 3223 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.60 | -99.81 | 6201 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.37 | -41.85 | -92.67 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.01 | -27.18 | -76.40 | 1638 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -61.65 | -97.73 | 3431 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.55 | -99.07 | 4970 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.26 | -28.67 | -70.13 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -55.84 | -94.69 | 2752 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.73 | -37.68 | -85.19 | 1731 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.73 | -99.70 | 6403 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.83 | -31.28 | -91.03 | 2363 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.93 | -19.08 | -80.35 | 1836 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.35 | -36.81 | -91.45 | 2152 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.60 | -46.75 | -97.60 | 3913 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -57.68 | -89.42 | 2164 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.26 | -31.03 | -67.02 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.82 | -24.85 | -73.12 | 1217 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.62 | -18.38 | -81.88 | 1760 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.54 | -46.49 | -97.56 | 4326 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -116.13 | -99.94 | 8454 |
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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 21:25:05.000141+00:00 -> 2026-11-18 21:35:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 21:25:05.000141+00:00 -> 2026-11-18 21:35:05.000141+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
