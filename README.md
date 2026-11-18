# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T10:35:05.000128+00:00 · 64314 ticks

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

Today: 8268 decisions in 1656 calls, $0.1156 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T10:35 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-18T10:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T10:35 | 1 / 4 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.05 | 17.05 | 0 | — | 14.89 | 5.37 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 3.01 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 16.87 | 3.44 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.60 | 3.60 | 0 | — | 5.76 | 1.26 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.24 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -3.01 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.64 | -3.36 | 8 | 50.0 | -3.91 | -0.08 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.75 | -4.25 | 0 | — | -3.89 | -1.30 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.05 | -5.95 | 198 | 30.3 | -4.26 | -1.51 | -8.84 | 149 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.61 | -5.91 | -6.03 | 22 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.54 | -7.46 | 0 | — | -8.38 | -2.22 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.79 | -9.21 | 153 | 46.4 | -11.59 | -3.41 | -18.48 | 149 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.67 | -9.33 | 0 | — | -8.30 | -2.26 | -12.67 | 1 |
| 19 | Copy: Insider buying | copy | 90.31 | -9.69 | 50 | 42.0 | -9.31 | -1.86 | -14.79 | 62 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -13.17 | -7.16 | -13.30 | 57 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.23 | -12.77 | 17 | 17.6 | -4.97 | -0.80 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.52 | -13.48 | 68 | 20.6 | -18.98 | -8.96 | -19.11 | 75 |
| 24 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.03 | -2.89 | -14.11 | 570 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.21 | -7.35 | -16.95 | 199 |
| 26 | Parabolic SAR · 1h | trend | 82.15 | -17.85 | 184 | 27.7 | -25.25 | -7.05 | -28.05 | 202 |
| 27 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 28 | Connors RSI(2) · 1h | reversion | 80.47 | -19.53 | 215 | 40.0 | -14.20 | -6.30 | -14.66 | 88 |
| 29 | Keltner breakout · 1h | breakout | 80.42 | -19.58 | 122 | 26.2 | -22.47 | -5.80 | -27.13 | 154 |
| 30 | Max aggression: 5-day momentum | meta | 79.93 | -20.07 | 21 | 42.9 | -48.12 | -3.22 | -55.24 | 22 |
| 31 | Donchian 55/20 · 1h | breakout | 79.85 | -20.15 | 77 | 13.0 | -24.60 | -6.43 | -29.99 | 84 |
| 32 | Volume breakout · 1h | breakout | 79.73 | -20.27 | 162 | 28.4 | -15.91 | -5.00 | -22.20 | 78 |
| 33 | Opening range 15m | breakout | 78.30 | -21.70 | 534 | 31.6 | -16.06 | -4.36 | -21.37 | 680 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.70 | -23.30 | 2 | 0.0 | -18.43 | -2.47 | -26.43 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 76.68 | -23.32 | 30 | 26.7 | -24.46 | -0.95 | -57.50 | 39 |
| 36 | Ichimoku · 1h | trend | 75.19 | -24.81 | 101 | 14.9 | -28.83 | -8.45 | -29.95 | 112 |
| 37 | Hold BTC | benchmark | 75.16 | -24.84 | 2 | 0.0 | -15.99 | -2.28 | -28.91 | 1 |
| 38 | ADX DI cross · 1h | trend | 74.75 | -25.25 | 209 | 19.1 | -27.58 | -4.47 | -35.42 | 263 |
| 39 | Stochastic reversion · 1h | reversion | 73.45 | -26.55 | 345 | 42.6 | -34.28 | -5.22 | -36.02 | 424 |
| 40 | Bollinger breakout · 1h | breakout | 73.40 | -26.60 | 189 | 22.2 | -29.50 | -7.73 | -34.16 | 225 |
| 41 | Supertrend · 1h | trend | 72.68 | -27.32 | 189 | 15.9 | -31.38 | -5.27 | -39.67 | 200 |
| 42 | Triple EMA stack · 1h | trend | 71.79 | -28.21 | 155 | 14.8 | -31.99 | -6.43 | -38.00 | 183 |
| 43 | RSI momentum · 1h | momentum | 71.39 | -28.61 | 176 | 14.2 | -30.38 | -5.50 | -37.63 | 197 |
| 44 | MFI reversion · 1h | reversion | 71.11 | -28.89 | 435 | 33.6 | -28.27 | -4.24 | -30.36 | 165 |
| 45 | MACD zero-line · 1h | trend | 70.27 | -29.73 | 181 | 17.7 | -27.54 | -5.53 | -33.68 | 204 |
| 46 | EMA 20/50 cross · 1h | trend | 70.11 | -29.89 | 115 | 10.4 | -36.12 | -10.12 | -39.23 | 116 |
| 47 | MACD cross · 1h | trend | 69.75 | -30.25 | 413 | 22.3 | -39.10 | -6.40 | -44.56 | 477 |
| 48 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 49 | Heikin-Ashi · 1h | trend | 69.34 | -30.66 | 471 | 22.9 | -43.58 | -9.32 | -45.25 | 640 |
| 50 | ROC + volume · 1h | momentum | 69.06 | -30.94 | 410 | 28.0 | -33.03 | -5.85 | -39.54 | 356 |
| 51 | OBV trend · 1h | momentum | 69.02 | -30.98 | 306 | 19.0 | -34.96 | -7.47 | -39.70 | 256 |
| 52 | Donchian 20/10 · 1h | breakout | 67.65 | -32.35 | 159 | 18.2 | -33.71 | -6.00 | -41.07 | 203 |
| 53 | CCI reversion · 1h | reversion | 67.32 | -32.68 | 382 | 41.6 | -41.30 | -6.84 | -44.29 | 469 |
| 54 | Bollinger reversion · 1h | reversion | 64.16 | -35.84 | 344 | 37.8 | -38.41 | -5.83 | -39.42 | 413 |
| 55 | EMA 9/21 cross · 1h | trend | 63.94 | -36.06 | 280 | 11.1 | -41.21 | -7.97 | -47.20 | 325 |
| 56 | Williams %R · 1h | reversion | 63.49 | -36.51 | 430 | 40.7 | -45.69 | -7.85 | -46.86 | 562 |
| 57 | Agent (ML meta-label) | meta | 60.19 | -39.81 | 1906 | 24.3 | -32.45 | -5.05 | -32.64 | 291 |
| 58 | RSI(14) reversion · 1h | reversion | 58.63 | -41.38 | 205 | 31.7 | -41.06 | -6.10 | -43.29 | 251 |
| 59 | Z-score reversion · 1h | reversion | 57.49 | -42.51 | 224 | 35.3 | -37.41 | -5.22 | -39.23 | 256 |
| 60 | VWAP momentum · 1h | momentum | 57.03 | -42.97 | 963 | 21.9 | -53.77 | -9.85 | -58.80 | 1198 |
| 61 | Candlestick reversal · 1h | reversion | 55.53 | -44.47 | 547 | 26.7 | -46.62 | -8.49 | -48.43 | 642 |
| 62 | Three white soldiers | momentum | 54.97 | -45.03 | 586 | 14.5 | -49.55 | -21.43 | -50.46 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -43.36 | -99.04 | 5282 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.32 | -25.33 | -82.24 | 1398 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -42.38 | -93.83 | 2462 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.11 | -31.62 | -90.22 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.18 | -40.02 | -91.32 | 2285 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.98 | -31.50 | -90.03 | 2123 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -48.04 | -97.88 | 3481 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -54.27 | -96.48 | 3401 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -39.79 | -93.58 | 2224 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.47 | -33.83 | -82.47 | 1593 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.94 | -99.60 | 6074 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.00 | -42.04 | -92.02 | 2557 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.93 | -39.55 | -94.93 | 3300 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.83 | -99.81 | 6191 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.47 | -43.09 | -92.51 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.44 | -25.87 | -76.45 | 1642 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -61.03 | -97.70 | 3434 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -55.97 | -99.02 | 4953 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.71 | -27.57 | -69.17 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.65 | -56.36 | -94.65 | 2742 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.39 | -37.31 | -84.49 | 1714 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -67.64 | -99.69 | 6371 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.71 | -30.36 | -90.86 | 2353 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.50 | -18.69 | -79.91 | 1832 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.16 | -35.49 | -91.23 | 2161 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.52 | -45.34 | -97.53 | 3903 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -56.66 | -89.33 | 2154 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.44 | -29.60 | -66.70 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.13 | -22.87 | -72.63 | 1220 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.75 | -18.04 | -80.79 | 1729 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -45.80 | -97.56 | 4331 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -107.98 | -99.94 | 8461 |
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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 10:35:05.000128+00:00 -> 2026-11-18 10:45:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 10:35:05.000128+00:00 -> 2026-11-18 10:45:05.000128+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
