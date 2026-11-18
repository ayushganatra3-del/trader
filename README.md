# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T10:05:05.000164+00:00 · 64285 ticks

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

Today: 7833 decisions in 1569 calls, $0.1095 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T10:05 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-18T10:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T10:05 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.51% | 14 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |
| Squeeze breakout | SQQQ | 1.74 | +6.13% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.21 | 17.21 | 0 | — | 14.89 | 5.37 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 3.01 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 16.87 | 3.44 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.75 | 3.75 | 0 | — | 5.77 | 1.26 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.24 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -3.01 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.77 | -3.23 | 8 | 50.0 | -3.91 | -0.08 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.88 | -4.12 | 0 | — | -3.89 | -1.30 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.05 | -5.95 | 198 | 30.3 | -4.26 | -1.51 | -8.84 | 149 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.31 | -8.29 | -5.89 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.66 | -7.34 | 0 | — | -8.38 | -2.22 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.82 | -9.18 | 153 | 46.4 | -11.58 | -3.41 | -18.48 | 149 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.79 | -9.21 | 0 | — | -8.30 | -2.26 | -12.67 | 1 |
| 19 | Copy: Insider buying | copy | 90.43 | -9.57 | 50 | 42.0 | -9.31 | -1.86 | -14.79 | 62 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -13.17 | -7.16 | -13.30 | 57 |
| 21 | Daily: Bullish score | daily | 87.29 | -12.71 | 17 | 17.6 | -4.97 | -0.80 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 86.88 | -13.12 | 68 | 20.6 | -18.70 | -8.82 | -19.11 | 75 |
| 24 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.03 | -2.89 | -14.11 | 570 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.20 | -7.35 | -16.95 | 199 |
| 26 | Parabolic SAR · 1h | trend | 82.75 | -17.25 | 184 | 27.7 | -24.80 | -6.90 | -28.05 | 202 |
| 27 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 28 | Keltner breakout · 1h | breakout | 80.76 | -19.24 | 122 | 26.2 | -21.36 | -5.27 | -27.13 | 154 |
| 29 | Connors RSI(2) · 1h | reversion | 80.50 | -19.50 | 215 | 40.0 | -14.19 | -6.29 | -14.66 | 88 |
| 30 | Donchian 55/20 · 1h | breakout | 80.16 | -19.84 | 77 | 13.0 | -24.36 | -6.34 | -29.99 | 84 |
| 31 | Max aggression: 5-day momentum | meta | 80.04 | -19.96 | 21 | 42.9 | -48.12 | -3.22 | -55.24 | 22 |
| 32 | Volume breakout · 1h | breakout | 79.76 | -20.24 | 162 | 28.4 | -15.91 | -5.00 | -22.20 | 78 |
| 33 | Opening range 15m | breakout | 78.30 | -21.70 | 534 | 31.6 | -16.06 | -4.36 | -21.37 | 680 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.80 | -23.20 | 2 | 0.0 | -18.43 | -2.47 | -26.43 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 76.78 | -23.22 | 30 | 26.7 | -24.46 | -0.95 | -57.50 | 39 |
| 36 | Hold BTC | benchmark | 75.64 | -24.36 | 2 | 0.0 | -15.74 | -2.21 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 75.62 | -24.38 | 101 | 14.9 | -28.50 | -8.31 | -29.95 | 112 |
| 38 | ADX DI cross · 1h | trend | 74.77 | -25.23 | 209 | 19.1 | -27.58 | -4.47 | -35.42 | 263 |
| 39 | Bollinger breakout · 1h | breakout | 73.81 | -26.19 | 189 | 22.2 | -28.59 | -7.28 | -34.16 | 224 |
| 40 | Stochastic reversion · 1h | reversion | 73.55 | -26.45 | 345 | 42.6 | -34.28 | -5.22 | -36.02 | 424 |
| 41 | Supertrend · 1h | trend | 73.12 | -26.88 | 189 | 15.9 | -31.06 | -5.20 | -39.67 | 200 |
| 42 | Triple EMA stack · 1h | trend | 72.10 | -27.90 | 155 | 14.8 | -31.77 | -6.37 | -38.00 | 183 |
| 43 | RSI momentum · 1h | momentum | 71.82 | -28.18 | 176 | 14.2 | -30.05 | -5.42 | -37.63 | 197 |
| 44 | MFI reversion · 1h | reversion | 71.19 | -28.81 | 435 | 33.6 | -28.40 | -4.23 | -30.41 | 164 |
| 45 | MACD zero-line · 1h | trend | 70.53 | -29.47 | 181 | 17.7 | -27.35 | -5.49 | -33.53 | 204 |
| 46 | EMA 20/50 cross · 1h | trend | 70.37 | -29.63 | 115 | 10.4 | -35.95 | -10.04 | -39.23 | 116 |
| 47 | MACD cross · 1h | trend | 69.86 | -30.14 | 413 | 22.3 | -38.90 | -6.35 | -44.56 | 477 |
| 48 | Heikin-Ashi · 1h | trend | 69.59 | -30.41 | 471 | 22.9 | -43.44 | -9.29 | -45.25 | 640 |
| 49 | OBV trend · 1h | momentum | 69.43 | -30.57 | 306 | 19.0 | -35.19 | -7.52 | -40.19 | 257 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 51 | ROC + volume · 1h | momentum | 69.19 | -30.82 | 410 | 28.0 | -32.98 | -5.84 | -39.54 | 356 |
| 52 | Donchian 20/10 · 1h | breakout | 68.05 | -31.95 | 159 | 18.2 | -33.40 | -5.92 | -41.07 | 203 |
| 53 | CCI reversion · 1h | reversion | 67.41 | -32.59 | 382 | 41.6 | -41.26 | -6.83 | -44.29 | 469 |
| 54 | EMA 9/21 cross · 1h | trend | 64.33 | -35.67 | 280 | 11.1 | -40.92 | -7.89 | -47.20 | 325 |
| 55 | Bollinger reversion · 1h | reversion | 64.24 | -35.76 | 344 | 37.8 | -38.41 | -5.83 | -39.42 | 413 |
| 56 | Williams %R · 1h | reversion | 63.58 | -36.42 | 430 | 40.7 | -45.68 | -7.85 | -46.86 | 562 |
| 57 | Agent (ML meta-label) | meta | 60.22 | -39.78 | 1906 | 24.3 | -27.48 | -4.35 | -28.44 | 289 |
| 58 | RSI(14) reversion · 1h | reversion | 58.70 | -41.30 | 205 | 31.7 | -41.06 | -6.10 | -43.29 | 251 |
| 59 | Z-score reversion · 1h | reversion | 57.57 | -42.43 | 224 | 35.3 | -37.41 | -5.22 | -39.23 | 256 |
| 60 | VWAP momentum · 1h | momentum | 57.21 | -42.79 | 963 | 21.9 | -53.32 | -9.83 | -58.39 | 1197 |
| 61 | Candlestick reversal · 1h | reversion | 55.62 | -44.38 | 547 | 26.7 | -46.47 | -8.48 | -48.30 | 644 |
| 62 | Three white soldiers | momentum | 54.97 | -45.03 | 586 | 14.5 | -49.42 | -21.49 | -50.32 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -43.24 | -99.03 | 5283 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.19 | -25.19 | -82.12 | 1398 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.80 | -42.18 | -93.80 | 2463 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.03 | -31.40 | -90.20 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.26 | -39.80 | -91.28 | 2290 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.95 | -31.49 | -90.00 | 2123 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -47.82 | -97.90 | 3485 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.46 | -54.02 | -96.47 | 3401 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -39.93 | -93.61 | 2227 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.74 | -33.75 | -82.74 | 1598 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -52.79 | -99.60 | 6077 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.93 | -41.73 | -91.98 | 2557 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.91 | -39.47 | -94.91 | 3298 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.50 | -99.81 | 6190 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.48 | -42.99 | -92.50 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.43 | -25.86 | -76.44 | 1641 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -60.66 | -97.68 | 3433 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -55.66 | -99.02 | 4957 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.82 | -27.53 | -69.13 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -56.05 | -94.67 | 2746 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.47 | -37.31 | -84.51 | 1718 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -67.15 | -99.69 | 6371 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.71 | -30.36 | -90.86 | 2353 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.46 | -18.69 | -79.91 | 1834 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.18 | -35.43 | -91.25 | 2160 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.52 | -45.21 | -97.52 | 3905 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -56.67 | -89.34 | 2155 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -29.60 | -66.70 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.08 | -22.83 | -72.62 | 1220 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.71 | -18.01 | -80.75 | 1730 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -45.55 | -97.55 | 4334 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -107.57 | -99.94 | 8461 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-18T07:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 3.60 | 0.07 | rebalance down |
| 2026-11-18T07:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 3.71 | 0.11 | rebalance down |
| 2026-11-18T06:01 | VWAP momentum · 1h | buy | DOGE-USD | 4.98 | — | entry signal |
| 2026-11-18T06:01 | VWAP momentum · 1h | buy | BTC-USD | 7.13 | — | entry signal |
| 2026-11-18T06:01 | VWAP momentum · 1h | sell | XRP-USD | 7.13 | -0.01 | rebalance down |
| 2026-11-18T05:50 | MFI reversion · 1h | buy | BTC-USD | 3.88 | — | rebalance up |
| 2026-11-18T05:50 | Three white soldiers | sell | BTC-USD | 13.67 | -0.10 | exit signal |
| 2026-11-18T05:20 | Three white soldiers | buy | BTC-USD | 13.77 | — | entry signal |
| 2026-11-18T05:00 | VWAP momentum · 1h | buy | XRP-USD | 14.25 | — | entry signal |
| 2026-11-18T05:00 | Heikin-Ashi · 1h | buy | SOL-USD | 17.38 | — | entry signal |
| 2026-11-18T02:00 | ROC + volume · 1h | sell | XRP-USD | 17.28 | -0.03 | exit signal |
| 2026-11-18T02:00 | ROC + volume · 1h | sell | DOGE-USD | 17.18 | -0.15 | exit signal |
| 2026-11-18T02:00 | Heikin-Ashi · 1h | sell | XRP-USD | 13.89 | -0.02 | exit signal |
| 2026-11-18T02:00 | Heikin-Ashi · 1h | sell | SOL-USD | 13.84 | 0.07 | exit signal |
| 2026-11-18T02:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 17.28 | -0.12 | exit signal |
| 2026-11-18T02:00 | Heikin-Ashi · 1h | sell | BTC-USD | 7.54 | -0.08 | exit signal |
| 2026-11-18T02:00 | ADX DI cross · 1h | sell | ETH-USD | 18.44 | -0.32 | exit signal |
| 2026-11-18T01:50 | Heikin-Ashi · 1h | buy | BTC-USD | 3.49 | — | rebalance up |
| 2026-11-18T01:50 | Heikin-Ashi · 1h | sell | XRP-USD | 3.49 | 0.00 | rebalance down |
| 2026-11-18T01:00 | VWAP momentum · 1h | sell | XRP-USD | 6.38 | 0.05 | exit signal |
| 2026-11-18T01:00 | VWAP momentum · 1h | sell | SOL-USD | 6.47 | 0.15 | exit signal |
| 2026-11-18T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.37 | 0.05 | exit signal |
| 2026-11-18T01:00 | Heikin-Ashi · 1h | buy | BTC-USD | 4.13 | — | entry |
| 2026-11-18T01:00 | Heikin-Ashi · 1h | sell | SOL-USD | 3.68 | 0.05 | rebalance down |
| 2026-11-18T01:00 | Ichimoku · 1h | buy | XRP-USD | 18.79 | — | entry signal |
| 2026-11-18T01:00 | Ichimoku · 1h | buy | SOL-USD | 18.79 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 10:05:05.000164+00:00 -> 2026-11-18 10:15:05.000164+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 10:05:05.000164+00:00 -> 2026-11-18 10:15:05.000164+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
