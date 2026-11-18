# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T02:35:05.000136+00:00 · 63905 ticks

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

Today: 2145 decisions in 429 calls, $0.0301 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T02:35 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-18T02:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T02:35 | 0 / 5 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.75 | 16.75 | 0 | — | 14.89 | 5.37 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 3.01 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 16.87 | 3.44 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.35 | 3.35 | 0 | — | 5.77 | 1.26 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.24 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -3.01 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.39 | -3.60 | 8 | 50.0 | -3.91 | -0.08 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.50 | -4.50 | 0 | — | -3.89 | -1.30 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.05 | -5.95 | 198 | 30.3 | -4.26 | -1.51 | -8.84 | 149 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.31 | -8.29 | -5.89 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.30 | -7.70 | 0 | — | -8.38 | -2.22 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.73 | -9.27 | 153 | 46.4 | -11.58 | -3.41 | -18.48 | 149 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.44 | -9.56 | 0 | — | -8.30 | -2.26 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -13.38 | -7.28 | -13.38 | 58 |
| 20 | Copy: Insider buying | copy | 90.08 | -9.92 | 50 | 42.0 | -9.31 | -1.86 | -14.79 | 62 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.11 | -12.89 | 17 | 17.6 | -4.97 | -0.80 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.46 | -13.54 | 68 | 20.6 | -15.22 | -5.46 | -19.87 | 79 |
| 24 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.03 | -2.89 | -14.11 | 570 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.20 | -7.35 | -16.95 | 199 |
| 26 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 27 | Parabolic SAR · 1h | trend | 81.65 | -18.35 | 184 | 27.7 | -25.61 | -7.16 | -28.05 | 203 |
| 28 | Keltner breakout · 1h | breakout | 80.52 | -19.48 | 122 | 26.2 | -19.78 | -4.45 | -27.13 | 154 |
| 29 | Connors RSI(2) · 1h | reversion | 80.42 | -19.58 | 215 | 40.0 | -14.38 | -6.40 | -14.66 | 90 |
| 30 | Max aggression: 5-day momentum | meta | 79.73 | -20.27 | 21 | 42.9 | -48.12 | -3.22 | -55.24 | 22 |
| 31 | Volume breakout · 1h | breakout | 79.68 | -20.32 | 162 | 28.4 | -15.91 | -5.00 | -22.20 | 78 |
| 32 | Donchian 55/20 · 1h | breakout | 79.39 | -20.61 | 77 | 13.0 | -25.44 | -6.70 | -29.98 | 85 |
| 33 | Opening range 15m | breakout | 78.30 | -21.70 | 534 | 31.6 | -16.06 | -4.36 | -21.37 | 680 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.51 | -23.50 | 2 | 0.0 | -18.43 | -2.47 | -26.43 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 76.48 | -23.52 | 30 | 26.7 | -24.46 | -0.95 | -57.50 | 39 |
| 36 | Hold BTC | benchmark | 75.24 | -24.76 | 2 | 0.0 | -16.01 | -2.23 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 74.72 | -25.28 | 101 | 14.9 | -29.15 | -8.57 | -29.88 | 112 |
| 38 | ADX DI cross · 1h | trend | 74.70 | -25.30 | 209 | 19.1 | -27.58 | -4.47 | -35.42 | 263 |
| 39 | Stochastic reversion · 1h | reversion | 73.26 | -26.74 | 345 | 42.6 | -34.28 | -5.22 | -36.02 | 424 |
| 40 | Bollinger breakout · 1h | breakout | 72.94 | -27.06 | 189 | 22.2 | -26.77 | -5.91 | -34.10 | 224 |
| 41 | Supertrend · 1h | trend | 72.17 | -27.83 | 189 | 15.9 | -31.68 | -5.34 | -39.67 | 200 |
| 42 | Triple EMA stack · 1h | trend | 71.32 | -28.68 | 155 | 14.8 | -31.88 | -6.45 | -38.02 | 183 |
| 43 | MFI reversion · 1h | reversion | 70.93 | -29.07 | 434 | 33.6 | -28.22 | -4.21 | -30.41 | 165 |
| 44 | RSI momentum · 1h | momentum | 70.92 | -29.08 | 176 | 14.2 | -30.98 | -5.64 | -37.58 | 198 |
| 45 | MACD zero-line · 1h | trend | 70.40 | -29.60 | 181 | 17.7 | -27.29 | -5.47 | -33.47 | 203 |
| 46 | EMA 20/50 cross · 1h | trend | 69.83 | -30.17 | 115 | 10.4 | -36.27 | -10.19 | -39.23 | 115 |
| 47 | MACD cross · 1h | trend | 69.57 | -30.43 | 413 | 22.3 | -39.18 | -6.41 | -44.56 | 477 |
| 48 | Heikin-Ashi · 1h | trend | 69.50 | -30.50 | 470 | 23.0 | -43.40 | -9.28 | -45.08 | 637 |
| 49 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 50 | ROC + volume · 1h | momentum | 69.15 | -30.85 | 410 | 28.0 | -30.87 | -5.07 | -39.54 | 355 |
| 51 | OBV trend · 1h | momentum | 68.71 | -31.29 | 306 | 19.0 | -35.74 | -7.71 | -40.19 | 256 |
| 52 | Donchian 20/10 · 1h | breakout | 67.20 | -32.80 | 159 | 18.2 | -32.82 | -5.56 | -41.01 | 203 |
| 53 | CCI reversion · 1h | reversion | 67.15 | -32.85 | 382 | 41.6 | -41.00 | -6.73 | -44.29 | 471 |
| 54 | Bollinger reversion · 1h | reversion | 63.99 | -36.01 | 344 | 37.8 | -38.45 | -5.83 | -39.42 | 414 |
| 55 | EMA 9/21 cross · 1h | trend | 63.65 | -36.34 | 280 | 11.1 | -39.64 | -7.35 | -47.20 | 325 |
| 56 | Williams %R · 1h | reversion | 63.33 | -36.67 | 430 | 40.7 | -45.48 | -7.77 | -46.86 | 563 |
| 57 | Agent (ML meta-label) | meta | 60.12 | -39.88 | 1906 | 24.3 | -22.44 | -3.95 | -23.69 | 299 |
| 58 | RSI(14) reversion · 1h | reversion | 58.48 | -41.52 | 205 | 31.7 | -41.06 | -6.10 | -43.29 | 251 |
| 59 | Z-score reversion · 1h | reversion | 57.35 | -42.65 | 224 | 35.3 | -37.41 | -5.22 | -39.23 | 256 |
| 60 | VWAP momentum · 1h | momentum | 56.98 | -43.02 | 962 | 21.9 | -52.94 | -9.44 | -58.38 | 1191 |
| 61 | Candlestick reversal · 1h | reversion | 55.40 | -44.60 | 547 | 26.7 | -46.45 | -8.47 | -48.30 | 644 |
| 62 | Three white soldiers | momentum | 55.07 | -44.93 | 585 | 14.5 | -49.41 | -21.37 | -50.24 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -41.92 | -99.02 | 5272 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.66 | -25.07 | -82.11 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.86 | -41.07 | -93.90 | 2464 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.17 | -31.36 | -90.29 | 1938 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.37 | -39.18 | -91.43 | 2293 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.67 | -30.78 | -89.67 | 2109 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -46.05 | -97.90 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -51.43 | -96.46 | 3393 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -39.27 | -93.53 | 2233 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.00 | -33.11 | -83.02 | 1603 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.07 | -99.60 | 6078 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.00 | -41.11 | -92.02 | 2558 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.86 | -38.84 | -94.86 | 3287 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -65.70 | -99.80 | 6184 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.42 | -41.39 | -92.43 | 2258 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.58 | -25.64 | -76.61 | 1642 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -56.51 | -97.64 | 3427 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.02 | -54.49 | -99.02 | 4957 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.63 | -26.80 | -68.90 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -53.63 | -94.61 | 2742 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.55 | -36.88 | -84.55 | 1720 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -66.11 | -99.70 | 6377 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.75 | -30.36 | -90.90 | 2359 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.45 | -18.63 | -79.91 | 1834 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.27 | -35.45 | -91.33 | 2169 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.54 | -44.73 | -97.54 | 3909 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.49 | -55.42 | -89.49 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -29.32 | -66.55 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.87 | -22.68 | -72.62 | 1227 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.64 | -17.94 | -80.65 | 1727 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.58 | -45.20 | -97.58 | 4343 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -92.50 | -99.94 | 8453 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-18T01:00 | Ichimoku · 1h | buy | DOGE-USD | 18.79 | — | entry signal |
| 2026-11-18T00:00 | Candlestick reversal · 1h | buy | BTC-USD | 2.92 | — | entry |
| 2026-11-18T00:00 | Candlestick reversal · 1h | sell | DOGE-USD | 3.12 | 0.05 | exit signal |
| 2026-11-18T00:00 | Squeeze breakout · 1h | buy | SOL-USD | 21.76 | — | entry signal |
| 2026-11-18T00:00 | Squeeze breakout · 1h | buy | DOGE-USD | 21.76 | — | entry signal |
| 2026-11-18T00:00 | Keltner breakout · 1h | buy | SOL-USD | 20.18 | — | entry signal |
| 2026-11-18T00:00 | Bollinger breakout · 1h | buy | XRP-USD | 18.41 | — | entry signal |
| 2026-11-18T00:00 | Bollinger breakout · 1h | buy | SOL-USD | 18.41 | — | entry signal |
| 2026-11-18T00:00 | Bollinger breakout · 1h | buy | DOGE-USD | 18.41 | — | entry signal |
| 2026-11-18T00:00 | Donchian 55/20 · 1h | buy | XRP-USD | 19.95 | — | entry signal |
| 2026-11-18T00:00 | Donchian 55/20 · 1h | buy | SOL-USD | 19.95 | — | entry signal |
| 2026-11-18T00:00 | Donchian 20/10 · 1h | buy | XRP-USD | 16.08 | — | entry signal |
| 2026-11-18T00:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 16.94 | — | entry signal |
| 2026-11-18T00:00 | RSI momentum · 1h | buy | XRP-USD | 17.03 | — | entry signal |
| 2026-11-18T00:00 | RSI momentum · 1h | buy | DOGE-USD | 17.88 | — | entry signal |
| 2026-11-18T00:00 | ADX DI cross · 1h | buy | ETH-USD | 18.75 | — | entry signal |
| 2026-11-18T00:00 | Parabolic SAR · 1h | buy | BTC-USD | 20.39 | — | entry signal |
| 2026-11-17T23:00 | MACD zero-line · 1h | buy | DOGE-USD | 17.63 | — | entry signal |
| 2026-11-17T23:00 | Triple EMA stack · 1h | buy | XRP-USD | 17.80 | — | entry signal |
| 2026-11-17T22:00 | OBV trend · 1h | buy | XRP-USD | 17.10 | — | entry signal |
| 2026-11-17T22:00 | ROC + volume · 1h | buy | XRP-USD | 17.31 | — | entry signal |
| 2026-11-17T22:00 | Heikin-Ashi · 1h | buy | XRP-USD | 17.40 | — | entry signal |
| 2026-11-17T22:00 | Heikin-Ashi · 1h | buy | SOL-USD | 17.40 | — | entry signal |
| 2026-11-17T22:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 17.40 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 02:35:05.000136+00:00 -> 2026-11-18 02:45:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 02:35:05.000136+00:00 -> 2026-11-18 02:45:05.000136+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
