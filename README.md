# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T14:00:05.000105+00:00 · 64508 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.66 (-15.34%)

Closed trades 219, win rate 35.6%, fees £6.07, max drawdown -17.33%.

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

Today: 11172 decisions in 2238 calls, $0.1563 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T14:00 | 1 / 0 / 4 | cash |  |
| Breezy | 2026-11-18T14:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T14:00 | 1 / 3 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |
| Squeeze breakout | SQQQ | 1.74 | +6.13% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.14 | 17.14 | 0 | — | 14.89 | 5.37 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 3.01 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 16.87 | 3.44 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.68 | 3.68 | 0 | — | 5.76 | 1.26 | -6.60 | 1 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.24 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -3.01 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.72 | -3.28 | 8 | 50.0 | -3.91 | -0.08 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 95.82 | -4.18 | 0 | — | -3.89 | -1.30 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.05 | -5.95 | 198 | 30.3 | -4.26 | -1.51 | -8.84 | 149 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.61 | -5.91 | -6.03 | 22 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.61 | -7.39 | 0 | — | -8.38 | -2.22 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.81 | -9.19 | 153 | 46.4 | -11.59 | -3.41 | -18.48 | 149 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.74 | -9.26 | 0 | — | -8.30 | -2.26 | -12.67 | 1 |
| 19 | Copy: Insider buying | copy | 90.38 | -9.62 | 50 | 42.0 | -9.31 | -1.86 | -14.79 | 62 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -13.24 | -7.20 | -13.30 | 57 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.26 | -12.74 | 17 | 17.6 | -4.97 | -0.80 | -19.56 | 18 |
| 23 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.03 | -2.89 | -14.11 | 570 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -19.20 | -9.05 | -19.20 | 75 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.21 | -7.35 | -16.95 | 199 |
| 26 | Parabolic SAR · 1h | trend | 81.87 | -18.13 | 184 | 27.7 | -25.07 | -6.98 | -28.05 | 201 |
| 27 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 28 | Connors RSI(2) · 1h | reversion | 80.49 | -19.51 | 215 | 40.0 | -14.20 | -6.30 | -14.66 | 88 |
| 29 | Keltner breakout · 1h | breakout | 80.06 | -19.94 | 124 | 25.8 | -23.37 | -6.08 | -27.19 | 155 |
| 30 | Max aggression: 5-day momentum | meta | 80.00 | -20.00 | 21 | 42.9 | -47.39 | -3.14 | -55.24 | 21 |
| 31 | Volume breakout · 1h | breakout | 79.74 | -20.25 | 162 | 28.4 | -15.91 | -5.00 | -22.20 | 78 |
| 32 | Donchian 55/20 · 1h | breakout | 79.65 | -20.35 | 77 | 13.0 | -24.82 | -6.50 | -29.99 | 84 |
| 33 | Opening range 15m | breakout | 78.30 | -21.70 | 534 | 31.6 | -16.06 | -4.36 | -21.37 | 680 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.76 | -23.24 | 2 | 0.0 | -18.43 | -2.47 | -26.43 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 76.74 | -23.26 | 30 | 26.7 | -37.40 | -2.23 | -57.50 | 38 |
| 36 | Ichimoku · 1h | trend | 75.01 | -24.99 | 101 | 14.9 | -29.05 | -8.53 | -29.95 | 112 |
| 37 | Hold BTC | benchmark | 74.88 | -25.12 | 2 | 0.0 | -16.52 | -2.34 | -28.91 | 1 |
| 38 | ADX DI cross · 1h | trend | 74.76 | -25.24 | 209 | 19.1 | -27.58 | -4.47 | -35.42 | 263 |
| 39 | Stochastic reversion · 1h | reversion | 73.50 | -26.50 | 345 | 42.6 | -34.29 | -5.22 | -36.02 | 425 |
| 40 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.50 | -8.13 | -34.16 | 224 |
| 41 | Supertrend · 1h | trend | 72.51 | -27.49 | 189 | 15.9 | -31.59 | -5.32 | -39.67 | 200 |
| 42 | Triple EMA stack · 1h | trend | 71.62 | -28.38 | 155 | 14.8 | -32.05 | -6.49 | -38.00 | 183 |
| 43 | RSI momentum · 1h | momentum | 71.23 | -28.77 | 176 | 14.2 | -30.59 | -5.55 | -37.63 | 197 |
| 44 | MFI reversion · 1h | reversion | 71.16 | -28.84 | 435 | 33.6 | -28.27 | -4.24 | -30.36 | 165 |
| 45 | MACD zero-line · 1h | trend | 70.20 | -29.80 | 183 | 17.5 | -27.67 | -5.56 | -33.80 | 204 |
| 46 | EMA 20/50 cross · 1h | trend | 70.00 | -30.00 | 115 | 10.4 | -35.77 | -9.13 | -39.89 | 117 |
| 47 | MACD cross · 1h | trend | 69.77 | -30.23 | 416 | 22.1 | -39.23 | -6.42 | -44.56 | 477 |
| 48 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 49 | Heikin-Ashi · 1h | trend | 69.17 | -30.83 | 473 | 22.8 | -43.74 | -9.35 | -45.41 | 640 |
| 50 | OBV trend · 1h | momentum | 68.81 | -31.19 | 307 | 18.9 | -35.22 | -7.53 | -39.70 | 255 |
| 51 | ROC + volume · 1h | momentum | 68.79 | -31.21 | 411 | 28.0 | -32.97 | -5.80 | -39.81 | 356 |
| 52 | Donchian 20/10 · 1h | breakout | 67.50 | -32.50 | 159 | 18.2 | -34.56 | -6.31 | -41.07 | 203 |
| 53 | CCI reversion · 1h | reversion | 67.37 | -32.63 | 382 | 41.6 | -41.34 | -6.85 | -44.29 | 469 |
| 54 | Bollinger reversion · 1h | reversion | 64.21 | -35.79 | 344 | 37.8 | -38.41 | -5.83 | -39.42 | 413 |
| 55 | EMA 9/21 cross · 1h | trend | 63.74 | -36.26 | 282 | 11.0 | -41.46 | -8.04 | -47.20 | 325 |
| 56 | Williams %R · 1h | reversion | 63.54 | -36.46 | 430 | 40.7 | -45.72 | -7.86 | -46.86 | 563 |
| 57 | Agent (ML meta-label) | meta | 60.21 | -39.79 | 1906 | 24.3 | -27.02 | -4.45 | -27.02 | 288 |
| 58 | RSI(14) reversion · 1h | reversion | 58.67 | -41.33 | 205 | 31.7 | -41.01 | -6.09 | -43.29 | 252 |
| 59 | Z-score reversion · 1h | reversion | 57.54 | -42.46 | 224 | 35.3 | -37.41 | -5.22 | -39.23 | 256 |
| 60 | VWAP momentum · 1h | momentum | 56.87 | -43.13 | 966 | 21.8 | -55.70 | -11.23 | -58.95 | 1198 |
| 61 | Candlestick reversal · 1h | reversion | 55.56 | -44.44 | 547 | 26.7 | -46.63 | -8.49 | -48.43 | 642 |
| 62 | Three white soldiers | momentum | 54.97 | -45.03 | 586 | 14.5 | -49.55 | -21.43 | -50.46 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -43.38 | -99.03 | 5274 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.33 | -25.37 | -82.29 | 1397 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.65 | -42.36 | -93.83 | 2453 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.93 | -31.67 | -90.20 | 1926 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.06 | -40.02 | -91.32 | 2280 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.53 | -90.07 | 2123 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.85 | -48.13 | -97.88 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.41 | -54.27 | -96.47 | 3392 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -38.98 | -93.55 | 2225 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.23 | -33.83 | -82.47 | 1587 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -54.30 | -99.61 | 6089 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.82 | -42.04 | -91.97 | 2548 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.91 | -39.56 | -94.91 | 3295 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.02 | -99.81 | 6192 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.40 | -43.09 | -92.51 | 2255 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.81 | -25.87 | -76.10 | 1632 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -61.16 | -97.67 | 3426 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.04 | -57.74 | -99.05 | 4963 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.72 | -27.57 | -69.17 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -56.36 | -94.58 | 2738 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.13 | -37.31 | -84.49 | 1708 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -69.28 | -99.70 | 6371 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.88 | -31.09 | -90.88 | 2362 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.69 | -18.76 | -79.97 | 1839 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.29 | -36.20 | -91.32 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.56 | -45.97 | -97.56 | 3908 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.29 | -57.47 | -89.29 | 2153 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.95 | -29.60 | -66.70 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.04 | -22.87 | -72.63 | 1219 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.03 | -18.18 | -81.03 | 1738 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.58 | -46.25 | -97.59 | 4330 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -111.24 | -99.94 | 8459 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T14:00 | Squeeze breakout · 1h | sell | SOL-USD | 21.42 | -0.34 | exit signal |
| 2026-11-18T14:00 | Keltner breakout · 1h | sell | SOL-USD | 19.87 | -0.31 | exit signal |
| 2026-11-18T14:00 | Bollinger breakout · 1h | sell | SOL-USD | 18.12 | -0.29 | exit signal |
| 2026-11-18T14:00 | MACD cross · 1h | sell | XRP-USD | 2.96 | -0.01 | exit signal |
| 2026-11-18T13:00 | Squeeze breakout · 1h | sell | DOGE-USD | 21.38 | -0.37 | exit signal |
| 2026-11-18T13:00 | Bollinger breakout · 1h | sell | DOGE-USD | 18.09 | -0.32 | exit signal |
| 2026-11-18T13:00 | OBV trend · 1h | sell | DOGE-USD | 15.74 | -0.19 | exit signal |
| 2026-11-18T13:00 | MACD zero-line · 1h | sell | BTC-USD | 17.36 | -0.27 | exit signal |
| 2026-11-18T13:00 | MACD cross · 1h | buy | XRP-USD | 2.97 | — | entry |
| 2026-11-18T13:00 | MACD cross · 1h | sell | BTC-USD | 2.97 | -0.02 | exit signal |
| 2026-11-18T12:45 | ROC + volume · 1h | sell | XRP-USD | 16.86 | -0.43 | stop-loss |
| 2026-11-18T12:30 | Keltner breakout · 1h | sell | XRP-USD | 19.75 | -0.43 | stop-loss |
| 2026-11-18T12:05 | Bollinger breakout · 1h | sell | XRP-USD | 18.39 | -0.01 | stop-loss |
| 2026-11-18T12:05 | MACD zero-line · 1h | sell | DOGE-USD | 17.51 | -0.12 | target is flat |
| 2026-11-18T12:05 | MACD cross · 1h | buy | BTC-USD | 2.99 | — | entry |
| 2026-11-18T12:05 | MACD cross · 1h | sell | DOGE-USD | 2.99 | -0.01 | target is flat |
| 2026-11-18T12:00 | VWAP momentum · 1h | sell | XRP-USD | 14.05 | -0.09 | exit signal |
| 2026-11-18T12:00 | Heikin-Ashi · 1h | sell | XRP-USD | 17.31 | -0.04 | exit signal |
| 2026-11-18T12:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 3.21 | — | rebalance up |
| 2026-11-18T12:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 5.29 | — | rebalance up |
| 2026-11-18T12:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 5.12 | -0.07 | exit signal |
| 2026-11-18T12:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 8.27 | -0.09 | exit signal |
| 2026-11-18T11:00 | VWAP momentum · 1h | buy | XRP-USD | 7.03 | — | rebalance up |
| 2026-11-18T11:00 | VWAP momentum · 1h | sell | ETH-USD | 4.90 | -0.03 | exit signal |
| 2026-11-18T11:00 | VWAP momentum · 1h | sell | BTC-USD | 7.07 | -0.06 | exit signal |
| 2026-11-18T11:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 17.23 | -0.19 | exit signal |
| 2026-11-18T10:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 17.41 | — | entry signal |
| 2026-11-18T08:00 | MFI reversion · 1h | sell | BTC-USD | 11.83 | 0.00 | exit signal |
| 2026-11-18T08:00 | Keltner breakout · 1h | buy | XRP-USD | 20.18 | — | entry signal |
| 2026-11-18T08:00 | OBV trend · 1h | buy | DOGE-USD | 15.93 | — | entry signal |
| 2026-11-18T08:00 | ROC + volume · 1h | buy | XRP-USD | 17.29 | — | entry signal |
| 2026-11-18T08:00 | MACD zero-line · 1h | buy | BTC-USD | 17.64 | — | entry signal |
| 2026-11-18T08:00 | EMA 20/50 cross · 1h | buy | DOGE-USD | 17.58 | — | entry signal |
| 2026-11-18T08:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.19 | — | entry signal |
| 2026-11-18T08:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 5.19 | 0.01 | rebalance down |
| 2026-11-18T07:00 | VWAP momentum · 1h | buy | ETH-USD | 4.93 | — | entry |
| 2026-11-18T07:00 | VWAP momentum · 1h | sell | DOGE-USD | 4.93 | -0.05 | exit signal |
| 2026-11-18T07:00 | Heikin-Ashi · 1h | buy | XRP-USD | 17.35 | — | entry signal |
| 2026-11-18T07:00 | Heikin-Ashi · 1h | sell | SOL-USD | 17.22 | -0.16 | exit signal |
| 2026-11-18T07:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 8.36 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 14:00:05.000105+00:00 -> 2026-11-18 14:10:05.000105+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 14:00:05.000105+00:00 -> 2026-11-18 14:10:05.000105+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
