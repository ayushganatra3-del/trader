# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T23:55:05.000130+00:00 · 64975 ticks

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

Today: 40272 decisions in 3639 calls, $0.5025 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T23:55 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-18T23:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T23:55 | 2 / 3 / 0 | ETH-USD 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.51% | 14 |
| OBV trend | SQQQ | 1.88 | +3.85% | 12 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.63 | 14.63 | 0 | — | 13.21 | 4.39 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.82 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.87 | 3.87 | 0 | — | 4.56 | 1.32 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 152 | 35.5 | -3.30 | -2.89 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.34 | 1.14 | -9.06 | 207 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.94 | -4.06 | 8 | 50.0 | -4.05 | -0.14 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.61 | -4.39 | 0 | — | -3.89 | -1.27 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.26 | -1.50 | -8.79 | 153 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.95 | -7.93 | -5.54 | 20 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.88 | -7.12 | 0 | — | -6.94 | -1.82 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.28 | -8.72 | 0 | — | -7.46 | -2.00 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.19 | -9.81 | 114 | 23.7 | -15.26 | -7.45 | -15.58 | 61 |
| 19 | Copy: Insider buying | copy | 90.04 | -9.96 | 52 | 40.4 | -10.48 | -2.12 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.03 | -12.97 | 17 | 17.6 | -7.35 | -1.38 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.08 | -9.17 | -18.13 | 72 |
| 24 | Agent | meta | 85.17 | -14.83 | 225 | 36.4 | -14.17 | -6.57 | -16.41 | 204 |
| 25 | Opening range 30m | breakout | 85.06 | -14.94 | 447 | 33.6 | -11.99 | -4.05 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.65 | -18.35 | 188 | 28.2 | -24.13 | -6.66 | -27.22 | 197 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.32 | -6.37 | -14.68 | 85 |
| 29 | Keltner breakout · 1h | breakout | 79.88 | -20.12 | 124 | 25.8 | -23.48 | -6.45 | -25.90 | 148 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.23 | -5.25 | -21.31 | 74 |
| 31 | Max aggression: 5-day momentum | meta | 79.14 | -20.86 | 21 | 42.9 | -47.98 | -3.20 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 33 | Opening range 15m | breakout | 77.70 | -22.30 | 541 | 32.0 | -19.89 | -5.93 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.94 | -23.06 | 2 | 0.0 | -18.99 | -2.58 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.53 | -24.47 | 209 | 19.1 | -26.24 | -4.25 | -34.88 | 266 |
| 36 | Hold BTC | benchmark | 74.11 | -25.89 | 2 | 0.0 | -17.70 | -2.59 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.65 | -8.30 | -33.72 | 216 |
| 39 | Stochastic reversion · 1h | reversion | 72.85 | -27.15 | 351 | 42.5 | -34.63 | -5.27 | -35.78 | 424 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -38.62 | -2.34 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.49 | -28.51 | 192 | 16.7 | -32.69 | -5.43 | -39.71 | 200 |
| 42 | Triple EMA stack · 1h | trend | 70.71 | -29.29 | 157 | 14.6 | -30.75 | -6.24 | -37.72 | 172 |
| 43 | MFI reversion · 1h | reversion | 70.57 | -29.43 | 452 | 33.4 | -29.27 | -4.41 | -31.00 | 171 |
| 44 | RSI momentum · 1h | momentum | 70.35 | -29.65 | 179 | 14.5 | -31.47 | -5.71 | -38.37 | 198 |
| 45 | Heikin-Ashi · 1h | trend | 69.90 | -30.10 | 474 | 23.0 | -44.09 | -9.64 | -45.85 | 629 |
| 46 | MACD zero-line · 1h | trend | 69.84 | -30.16 | 184 | 17.9 | -28.09 | -5.60 | -34.29 | 203 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.30 | -30.70 | 116 | 10.3 | -36.84 | -9.38 | -40.97 | 118 |
| 49 | ROC + volume · 1h | momentum | 69.00 | -31.00 | 413 | 28.1 | -34.46 | -6.33 | -39.51 | 341 |
| 50 | OBV trend · 1h | momentum | 68.23 | -31.77 | 310 | 19.4 | -34.08 | -7.19 | -39.87 | 248 |
| 51 | MACD cross · 1h | trend | 67.68 | -32.32 | 417 | 22.3 | -41.09 | -6.72 | -46.93 | 490 |
| 52 | CCI reversion · 1h | reversion | 67.10 | -32.90 | 387 | 41.6 | -42.21 | -7.09 | -44.29 | 473 |
| 53 | Donchian 20/10 · 1h | breakout | 66.53 | -33.47 | 162 | 17.9 | -36.43 | -7.06 | -41.19 | 194 |
| 54 | Bollinger reversion · 1h | reversion | 63.93 | -36.07 | 348 | 37.9 | -38.73 | -5.90 | -39.66 | 417 |
| 55 | Williams %R · 1h | reversion | 63.63 | -36.37 | 437 | 40.7 | -46.55 | -8.11 | -47.31 | 566 |
| 56 | EMA 9/21 cross · 1h | trend | 62.81 | -37.19 | 285 | 11.6 | -39.64 | -7.78 | -45.71 | 321 |
| 57 | Agent (ML meta-label) | meta | 60.11 | -39.89 | 1949 | 24.6 | -27.65 | -5.09 | -28.56 | 306 |
| 58 | RSI(14) reversion · 1h | reversion | 58.89 | -41.11 | 206 | 32.0 | -40.82 | -6.04 | -43.22 | 256 |
| 59 | Z-score reversion · 1h | reversion | 57.43 | -42.57 | 227 | 35.2 | -36.86 | -5.09 | -39.53 | 257 |
| 60 | VWAP momentum · 1h | momentum | 55.25 | -44.75 | 987 | 21.5 | -56.13 | -11.04 | -60.15 | 1203 |
| 61 | Candlestick reversal · 1h | reversion | 55.19 | -44.81 | 552 | 26.4 | -47.74 | -8.83 | -48.84 | 641 |
| 62 | Three white soldiers | momentum | 54.75 | -45.25 | 589 | 14.4 | -49.60 | -21.92 | -50.81 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -42.02 | -99.07 | 5325 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.92 | -27.58 | -82.56 | 1408 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.85 | -44.13 | -94.03 | 2461 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.97 | -32.13 | -90.40 | 1930 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.26 | -41.61 | -91.52 | 2309 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.01 | -30.90 | -90.11 | 2068 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -47.85 | -97.96 | 3466 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.41 | -55.94 | -96.46 | 3394 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.36 | -37.98 | -93.36 | 2187 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.74 | -35.41 | -82.82 | 1585 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -55.14 | -99.61 | 6107 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.93 | -43.31 | -92.19 | 2553 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.76 | -38.77 | -94.77 | 3218 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -71.90 | -99.82 | 6202 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.47 | -43.55 | -92.70 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.37 | -27.27 | -76.76 | 1649 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -61.79 | -97.72 | 3430 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.06 | -99.07 | 4972 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.39 | -28.79 | -70.16 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -55.53 | -94.71 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -37.84 | -85.22 | 1734 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.96 | -99.70 | 6403 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.85 | -31.34 | -91.03 | 2368 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.90 | -19.07 | -80.35 | 1838 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.57 | -37.07 | -91.65 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.61 | -46.42 | -97.62 | 3916 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.43 | -60.17 | -89.48 | 2169 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.33 | -30.81 | -67.05 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.43 | -26.82 | -73.12 | 1220 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.39 | -18.26 | -81.73 | 1749 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -46.52 | -97.56 | 4327 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -115.55 | -99.94 | 8451 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T23:45 | Three white soldiers | buy | SOL-USD | 13.69 | — | entry signal |
| 2026-11-18T23:05 | Three white soldiers | buy | DOGE-USD | 13.66 | — | entry signal |
| 2026-11-18T23:00 | Supertrend · 1h | sell | SOL-USD | 17.81 | 0.09 | exit signal |
| 2026-11-18T22:50 | Donchian 55/20 · 1h | sell | XRP-USD | 19.37 | -0.58 | stop-loss |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 23:55:05.000130+00:00 -> 2026-11-19 00:05:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 23:55:05.000130+00:00 -> 2026-11-19 00:05:05.000130+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
