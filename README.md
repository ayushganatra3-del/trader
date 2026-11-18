# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T16:00:05.000141+00:00 · 64608 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.67 (-15.33%)

Closed trades 219, win rate 35.6%, fees £6.08, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 16.95 | +0.02 |

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

### Market regime (QQQ, 2026-11-17)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 34.44 · VIX 25.46 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 6.1, AMZN 4.3, TSLA 2.4, META 1.9, AMD 1.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 18609 decisions in 2538 calls, $0.2440 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T16:00 | 6 / 15 / 9 | TNA 15%, SOXL 14% |  |
| Breezy | 2026-11-18T16:00 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-18T16:00 | 8 / 21 / 1 | COIN 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| OBV trend | SQQQ | 1.88 | +3.85% | 12 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 115.50 | 15.50 | 0 | — | 13.52 | 4.72 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 17.51 | 3.58 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.97 | 3.97 | 0 | — | 5.34 | 1.34 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.05 | 0.05 | 150 | 34.7 | -3.64 | -3.22 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 195 | 32.8 | 8.00 | 2.23 | -9.06 | 214 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.98 | -4.02 | 8 | 50.0 | -5.09 | -0.16 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.56 | -4.44 | 0 | — | -4.25 | -1.39 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 200 | 30.0 | -4.25 | -1.50 | -8.80 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.00 | -6.34 | -6.42 | 23 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.59 | -7.41 | 0 | — | -7.15 | -1.88 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | Copy: Insider buying | copy | 91.17 | -8.83 | 50 | 42.0 | -9.24 | -1.84 | -14.79 | 64 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.87 | -9.13 | 0 | — | -7.97 | -2.16 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.25 | -9.75 | 113 | 23.9 | -13.26 | -7.22 | -13.36 | 58 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -11.35 | -3.33 | -18.48 | 148 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.17 | -12.83 | 17 | 17.6 | -5.61 | -0.82 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.03 | -8.99 | -16.08 | 70 |
| 24 | Opening range 30m | breakout | 85.11 | -14.89 | 442 | 33.5 | -10.38 | -3.29 | -14.16 | 562 |
| 25 | Agent | meta | 84.67 | -15.33 | 219 | 35.6 | -15.35 | -7.47 | -17.11 | 199 |
| 26 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 27 | Parabolic SAR · 1h | trend | 81.35 | -18.65 | 188 | 28.2 | -24.80 | -7.03 | -27.46 | 204 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.31 | -6.36 | -14.63 | 87 |
| 29 | Keltner breakout · 1h | breakout | 79.94 | -20.06 | 124 | 25.8 | -23.72 | -6.24 | -26.69 | 157 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -14.79 | -4.64 | -21.17 | 77 |
| 31 | Max aggression: 5-day momentum | meta | 79.51 | -20.48 | 21 | 42.9 | -47.69 | -3.17 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 79.23 | -20.77 | 77 | 13.0 | -25.21 | -6.62 | -30.18 | 84 |
| 33 | Opening range 15m | breakout | 77.80 | -22.20 | 535 | 31.6 | -16.79 | -4.53 | -21.44 | 673 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.69 | -23.31 | 2 | 0.0 | -18.47 | -2.48 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 74.48 | -25.52 | 209 | 19.1 | -28.14 | -4.65 | -35.70 | 269 |
| 36 | Ichimoku · 1h | trend | 74.33 | -25.68 | 103 | 14.6 | -29.20 | -8.54 | -30.27 | 111 |
| 37 | Hold BTC | benchmark | 73.90 | -26.10 | 2 | 0.0 | -18.18 | -2.50 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.30 | -8.03 | -34.18 | 221 |
| 39 | Stochastic reversion · 1h | reversion | 72.98 | -27.02 | 349 | 42.4 | -34.32 | -5.22 | -35.61 | 426 |
| 40 | Supertrend · 1h | trend | 71.83 | -28.17 | 189 | 15.9 | -32.05 | -5.41 | -39.50 | 202 |
| 41 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -38.81 | -2.36 | -57.50 | 39 |
| 42 | Triple EMA stack · 1h | trend | 71.13 | -28.87 | 155 | 14.8 | -31.68 | -6.35 | -37.84 | 178 |
| 43 | RSI momentum · 1h | momentum | 70.49 | -29.51 | 178 | 14.6 | -30.75 | -5.58 | -37.50 | 198 |
| 44 | MFI reversion · 1h | reversion | 70.37 | -29.63 | 442 | 33.7 | -27.35 | -4.07 | -30.08 | 164 |
| 45 | MACD zero-line · 1h | trend | 70.09 | -29.91 | 183 | 17.5 | -27.50 | -5.49 | -33.83 | 202 |
| 46 | EMA 20/50 cross · 1h | trend | 69.48 | -30.52 | 116 | 10.3 | -36.01 | -9.27 | -39.97 | 117 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | Heikin-Ashi · 1h | trend | 68.95 | -31.05 | 474 | 23.0 | -45.55 | -10.08 | -45.70 | 637 |
| 49 | OBV trend · 1h | momentum | 68.38 | -31.62 | 310 | 19.4 | -36.25 | -7.76 | -40.15 | 256 |
| 50 | ROC + volume · 1h | momentum | 68.24 | -31.76 | 413 | 28.1 | -33.23 | -5.97 | -39.42 | 344 |
| 51 | MACD cross · 1h | trend | 67.93 | -32.07 | 416 | 22.1 | -40.64 | -6.66 | -46.12 | 480 |
| 52 | CCI reversion · 1h | reversion | 67.18 | -32.82 | 383 | 41.5 | -41.79 | -6.96 | -44.29 | 473 |
| 53 | Donchian 20/10 · 1h | breakout | 66.79 | -33.21 | 161 | 18.0 | -35.43 | -6.62 | -41.14 | 199 |
| 54 | Bollinger reversion · 1h | reversion | 63.94 | -36.06 | 345 | 37.7 | -38.71 | -5.89 | -39.49 | 413 |
| 55 | Williams %R · 1h | reversion | 63.67 | -36.33 | 432 | 41.0 | -46.47 | -8.10 | -47.52 | 564 |
| 56 | EMA 9/21 cross · 1h | trend | 63.16 | -36.84 | 283 | 11.0 | -40.36 | -7.94 | -46.31 | 323 |
| 57 | Agent (ML meta-label) | meta | 59.92 | -40.08 | 1912 | 24.5 | -24.91 | -4.59 | -25.65 | 282 |
| 58 | RSI(14) reversion · 1h | reversion | 58.89 | -41.11 | 206 | 32.0 | -41.48 | -6.18 | -43.22 | 253 |
| 59 | Z-score reversion · 1h | reversion | 57.54 | -42.46 | 225 | 35.1 | -37.01 | -5.13 | -39.46 | 253 |
| 60 | VWAP momentum · 1h | momentum | 55.83 | -44.17 | 972 | 21.7 | -55.79 | -11.20 | -59.43 | 1194 |
| 61 | Candlestick reversal · 1h | reversion | 55.31 | -44.69 | 550 | 26.5 | -47.10 | -8.64 | -48.32 | 639 |
| 62 | Three white soldiers | momentum | 54.75 | -45.25 | 588 | 14.5 | -49.82 | -21.86 | -50.71 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -43.67 | -99.04 | 5311 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.48 | -26.04 | -82.43 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.65 | -42.62 | -93.91 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.02 | -31.87 | -90.26 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.11 | -40.54 | -91.42 | 2287 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.60 | -90.05 | 2098 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -48.32 | -97.90 | 3464 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -54.07 | -96.45 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.49 | -38.84 | -93.55 | 2208 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.38 | -34.18 | -82.64 | 1584 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -54.90 | -99.61 | 6112 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.97 | -42.72 | -92.15 | 2542 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.91 | -39.45 | -94.92 | 3275 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.74 | -99.81 | 6185 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.50 | -44.07 | -92.61 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.20 | -25.79 | -76.72 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -61.70 | -97.72 | 3420 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.08 | -58.41 | -99.08 | 4978 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.72 | -27.52 | -69.39 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -57.11 | -94.66 | 2746 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.55 | -38.25 | -84.83 | 1722 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.27 | -99.70 | 6383 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.93 | -31.44 | -90.96 | 2373 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.96 | -18.91 | -80.01 | 1854 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.49 | -36.75 | -91.54 | 2155 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.56 | -46.19 | -97.57 | 3923 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.26 | -57.63 | -89.26 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.16 | -30.11 | -67.04 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.58 | -23.85 | -73.04 | 1218 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.41 | -18.34 | -81.48 | 1754 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.58 | -46.33 | -97.59 | 4332 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -113.83 | -99.94 | 8446 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T16:00 | Agent (rotation) | buy | AMZN | 7.83 | — | entry |
| 2026-11-18T16:00 | Agent (ML meta-label) | buy | GOOGL | 3.45 | — | entry |
| 2026-11-18T16:00 | Donchian 20/10 · 1h | sell | XRP-USD | 15.92 | -0.16 | exit signal |
| 2026-11-18T16:00 | OBV trend · 1h | sell | XRP-USD | 17.17 | 0.07 | exit signal |
| 2026-11-18T16:00 | RSI momentum · 1h | sell | SOL-USD | 17.89 | 0.08 | exit signal |
| 2026-11-18T16:00 | ROC + volume · 1h | sell | XRP-USD | 16.86 | -0.27 | exit signal |
| 2026-11-18T16:00 | Ichimoku · 1h | sell | XRP-USD | 18.70 | -0.09 | exit signal |
| 2026-11-18T16:00 | Ichimoku · 1h | sell | DOGE-USD | 18.41 | -0.38 | exit signal |
| 2026-11-18T16:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 17.22 | -0.37 | exit signal |
| 2026-11-18T16:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 15.73 | -0.22 | exit signal |
| 2026-11-18T16:00 | Gap and go | buy | AMZN | 25.00 | — | entry signal |
| 2026-11-18T15:55 | Agent (ML meta-label) | sell | SPY | 3.45 | -0.02 | rebalance down |
| 2026-11-18T15:55 | Agent | buy | TSLA | 16.93 | — | following Stochastic reversion |
| 2026-11-18T15:50 | Stochastic reversion · 1h | sell | BITX | 4.15 | -0.17 | stop-loss |
| 2026-11-18T15:50 | Candlestick reversal · 1h | buy | LABU | 3.23 | — | entry |
| 2026-11-18T15:50 | Candlestick reversal · 1h | sell | META | 3.03 | -0.04 | stop-loss |
| 2026-11-18T15:50 | Candlestick reversal · 1h | sell | BTC-USD | 2.82 | -0.09 | stop-loss |
| 2026-11-18T15:50 | EMA 9/21 cross · 1h | buy | XRP-USD | 3.17 | — | rebalance up |
| 2026-11-18T15:50 | Opening range 30m | sell | IWM | 21.35 | -0.15 | stop-loss |
| 2026-11-18T15:45 | Agent (rotation) | sell | AMZN | 7.79 | -0.04 | selected signal exited |
| 2026-11-18T15:45 | Donchian 20/10 · 1h | sell | DOGE-USD | 16.51 | -0.44 | stop-loss |
| 2026-11-18T15:45 | RSI momentum · 1h | sell | DOGE-USD | 17.42 | -0.46 | stop-loss |
| 2026-11-18T15:45 | Gap and go | sell | AMZN | 24.90 | -0.13 | exit signal |
| 2026-11-18T15:40 | VWAP momentum · 1h | sell | LABU | 13.65 | -0.46 | target is flat |
| 2026-11-18T15:40 | Opening range 30m | sell | TNA | 21.15 | -0.35 | stop-loss |
| 2026-11-18T15:40 | Opening range 30m | sell | LABU | 20.81 | -0.79 | stop-loss |
| 2026-11-18T15:40 | Opening range 15m | sell | LABU | 18.89 | -0.62 | stop-loss |
| 2026-11-18T15:35 | Agent (rotation) | buy | AMZN | 7.84 | — | entry |
| 2026-11-18T15:35 | MFI reversion · 1h | buy | ETHU | 11.77 | — | entry |
| 2026-11-18T15:35 | MFI reversion · 1h | sell | QQQ | 11.77 | -0.02 | target is flat |
| 2026-11-18T15:35 | OBV trend · 1h | sell | AAPL | 17.11 | -0.00 | target is flat |
| 2026-11-18T15:35 | Three white soldiers | sell | SOXL | 13.62 | -0.11 | exit signal |
| 2026-11-18T15:35 | Gap and go | buy | AMZN | 25.03 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | TSLA | 6.68 | — | following Stochastic reversion |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | TNA | 6.69 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | SOXL | 6.69 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | LABU | 6.69 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | IWM | 6.69 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | AMD | 6.69 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | AAPL | 6.69 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 16:00:05.000141+00:00 -> 2026-11-18 16:10:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 16:00:05.000141+00:00 -> 2026-11-18 16:10:05.000141+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
