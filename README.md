# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T00:35:05.000167+00:00 · 63796 ticks

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
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-17)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 34.44 · VIX 25.46 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 6.1, AMZN 4.3, TSLA 2.4, META 1.9, AMD 1.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 510 decisions in 102 calls, $0.0072 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T00:35 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-18T00:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T00:35 | 2 / 3 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.73 | 16.73 | 0 | — | 14.89 | 5.15 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 16.87 | 3.41 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.32 | 3.32 | 0 | — | 5.76 | 1.59 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.22 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -2.98 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.47 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.38 | -3.62 | 8 | 50.0 | -3.91 | -0.12 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.49 | -4.51 | 0 | — | -3.89 | -1.27 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.05 | -5.95 | 198 | 30.3 | -4.51 | -1.59 | -9.44 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.31 | -8.21 | -5.89 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.29 | -7.71 | 0 | — | -8.38 | -2.20 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.09 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.73 | -9.27 | 153 | 46.4 | -11.66 | -3.41 | -18.48 | 148 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.42 | -9.58 | 0 | — | -8.30 | -2.24 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -11.47 | -5.54 | -13.38 | 60 |
| 20 | Copy: Insider buying | copy | 90.07 | -9.93 | 50 | 42.0 | -9.31 | -1.85 | -14.79 | 62 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.10 | -12.90 | 17 | 17.6 | -4.97 | -0.78 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.85 | -13.15 | 68 | 20.6 | -15.84 | -6.24 | -19.27 | 78 |
| 24 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.03 | -2.84 | -14.11 | 570 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.21 | -7.29 | -16.95 | 199 |
| 26 | Parabolic SAR · 1h | trend | 82.30 | -17.70 | 184 | 27.7 | -25.59 | -7.05 | -28.05 | 207 |
| 27 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.74 | -19.74 | 96 |
| 28 | Keltner breakout · 1h | breakout | 80.69 | -19.31 | 122 | 26.2 | -18.79 | -3.95 | -27.13 | 154 |
| 29 | Connors RSI(2) · 1h | reversion | 80.42 | -19.59 | 215 | 40.0 | -14.40 | -6.35 | -14.78 | 92 |
| 30 | Max aggression: 5-day momentum | meta | 79.72 | -20.28 | 21 | 42.9 | -48.12 | -3.19 | -55.24 | 22 |
| 31 | Donchian 55/20 · 1h | breakout | 79.71 | -20.29 | 77 | 13.0 | -25.13 | -6.54 | -29.68 | 85 |
| 32 | Volume breakout · 1h | breakout | 79.68 | -20.32 | 162 | 28.4 | -15.91 | -4.96 | -22.20 | 78 |
| 33 | Opening range 15m | breakout | 78.30 | -21.70 | 534 | 31.6 | -16.06 | -4.27 | -21.37 | 680 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.49 | -23.51 | 2 | 0.0 | -18.43 | -2.46 | -26.43 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 76.47 | -23.53 | 30 | 26.7 | -24.46 | -0.94 | -57.50 | 39 |
| 36 | Hold BTC | benchmark | 75.64 | -24.36 | 2 | 0.0 | -15.67 | -2.21 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -28.72 | -8.32 | -29.33 | 109 |
| 38 | ADX DI cross · 1h | trend | 74.91 | -25.09 | 208 | 19.2 | -27.35 | -4.38 | -35.42 | 263 |
| 39 | Bollinger breakout · 1h | breakout | 73.41 | -26.59 | 189 | 22.2 | -26.28 | -5.73 | -33.62 | 224 |
| 40 | Stochastic reversion · 1h | reversion | 73.25 | -26.75 | 345 | 42.6 | -34.28 | -5.18 | -36.02 | 424 |
| 41 | Supertrend · 1h | trend | 72.65 | -27.35 | 189 | 15.9 | -31.23 | -5.19 | -39.67 | 200 |
| 42 | Triple EMA stack · 1h | trend | 71.62 | -28.38 | 155 | 14.8 | -31.56 | -6.30 | -38.02 | 183 |
| 43 | RSI momentum · 1h | momentum | 71.38 | -28.62 | 176 | 14.2 | -30.52 | -5.49 | -37.58 | 198 |
| 44 | MFI reversion · 1h | reversion | 70.96 | -29.04 | 434 | 33.6 | -28.06 | -4.17 | -30.36 | 166 |
| 45 | MACD zero-line · 1h | trend | 70.57 | -29.43 | 181 | 17.7 | -27.11 | -5.38 | -33.36 | 203 |
| 46 | Heikin-Ashi · 1h | trend | 70.30 | -29.70 | 466 | 23.0 | -42.53 | -8.94 | -44.96 | 636 |
| 47 | EMA 20/50 cross · 1h | trend | 69.97 | -30.04 | 115 | 10.4 | -36.14 | -10.03 | -39.23 | 115 |
| 48 | ROC + volume · 1h | momentum | 69.63 | -30.37 | 408 | 28.2 | -30.39 | -4.93 | -39.54 | 355 |
| 49 | MACD cross · 1h | trend | 69.59 | -30.41 | 413 | 22.3 | -38.91 | -6.29 | -44.56 | 477 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.00 | -31.00 | 306 | 19.0 | -34.90 | -7.41 | -39.70 | 255 |
| 52 | Donchian 20/10 · 1h | breakout | 67.63 | -32.37 | 159 | 18.2 | -32.37 | -5.41 | -40.92 | 203 |
| 53 | CCI reversion · 1h | reversion | 67.14 | -32.86 | 382 | 41.6 | -40.98 | -6.69 | -44.29 | 471 |
| 54 | EMA 9/21 cross · 1h | trend | 64.08 | -35.92 | 280 | 11.1 | -39.86 | -7.46 | -47.20 | 324 |
| 55 | Bollinger reversion · 1h | reversion | 63.98 | -36.02 | 344 | 37.8 | -38.45 | -5.79 | -39.42 | 414 |
| 56 | Williams %R · 1h | reversion | 63.32 | -36.68 | 430 | 40.7 | -45.46 | -7.71 | -46.86 | 563 |
| 57 | Agent (ML meta-label) | meta | 60.11 | -39.89 | 1906 | 24.3 | -28.27 | -4.71 | -29.27 | 291 |
| 58 | RSI(14) reversion · 1h | reversion | 58.47 | -41.53 | 205 | 31.7 | -41.06 | -6.05 | -43.29 | 251 |
| 59 | Z-score reversion · 1h | reversion | 57.34 | -42.66 | 224 | 35.3 | -37.41 | -5.17 | -39.23 | 256 |
| 60 | VWAP momentum · 1h | momentum | 57.11 | -42.89 | 959 | 21.7 | -53.09 | -9.35 | -58.63 | 1193 |
| 61 | Candlestick reversal · 1h | reversion | 55.41 | -44.59 | 547 | 26.7 | -46.59 | -8.40 | -48.43 | 642 |
| 62 | Three white soldiers | momentum | 55.07 | -44.93 | 585 | 14.5 | -49.78 | -21.42 | -50.37 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -42.15 | -99.02 | 5273 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.61 | -24.95 | -82.11 | 1408 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.86 | -40.33 | -93.96 | 2468 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.09 | -31.18 | -90.33 | 1939 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.34 | -38.79 | -91.47 | 2295 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.69 | -30.22 | -89.75 | 2113 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -45.81 | -97.92 | 3484 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -51.31 | -96.48 | 3395 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.43 | -37.26 | -93.49 | 2232 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.03 | -32.76 | -83.08 | 1606 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -50.99 | -99.60 | 6077 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.02 | -41.28 | -92.07 | 2560 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.84 | -37.50 | -94.84 | 3287 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -65.48 | -99.81 | 6188 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.46 | -41.78 | -92.47 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.65 | -25.74 | -76.68 | 1643 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -56.43 | -97.67 | 3433 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -52.57 | -99.01 | 4951 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.60 | -27.01 | -68.90 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -53.75 | -94.60 | 2741 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.49 | -37.10 | -84.50 | 1719 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -62.81 | -99.69 | 6375 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.75 | -30.21 | -90.90 | 2359 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.45 | -18.35 | -79.91 | 1834 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.28 | -35.27 | -91.36 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.50 | -43.42 | -97.53 | 3902 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.41 | -55.21 | -89.41 | 2163 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -29.65 | -66.55 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.64 | -22.68 | -72.62 | 1227 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.39 | -17.57 | -80.64 | 1717 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.54 | -44.18 | -97.58 | 4339 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -90.85 | -99.94 | 8460 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-17T22:00 | Parabolic SAR · 1h | buy | XRP-USD | 20.39 | — | entry signal |
| 2026-11-17T22:00 | Parabolic SAR · 1h | buy | SOL-USD | 20.39 | — | entry signal |
| 2026-11-17T22:00 | Parabolic SAR · 1h | buy | DOGE-USD | 20.39 | — | entry signal |
| 2026-11-17T22:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 17.44 | — | entry signal |
| 2026-11-17T22:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 15.83 | — | entry signal |
| 2026-11-17T21:06 | MFI reversion · 1h | sell | BTC-USD | 3.92 | -0.05 | rebalance down |
| 2026-11-17T21:00 | ROC + volume · 1h | buy | DOGE-USD | 17.33 | — | entry signal |
| 2026-11-17T21:00 | MACD cross · 1h | buy | DOGE-USD | 3.00 | — | entry signal |
| 2026-11-17T20:55 | Agent (rotation) | sell | SQQQ | 31.47 | 0.17 | selected signal exited |
| 2026-11-17T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 98.59 | 0.15 | target is flat |
| 2026-11-17T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 111.39 | 0.61 | target is flat |
| 2026-11-17T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 91.65 | -0.23 | target is flat |
| 2026-11-17T20:55 | Agent (ML meta-label) | buy | TQQQ | 14.96 | — | entry |
| 2026-11-17T20:55 | Agent (ML meta-label) | sell | MSTR | 14.92 | -0.06 | selected signal exited |
| 2026-11-17T20:55 | Agent (ML meta-label) | sell | AMD | 14.94 | -0.04 | selected signal exited |
| 2026-11-17T20:55 | Agent | sell | SOXL | 17.04 | 0.10 | selected signal exited |
| 2026-11-17T20:55 | MFI reversion · 1h | buy | UPRO | 5.04 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 00:35:05.000167+00:00 -> 2026-11-18 00:45:05.000167+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 00:35:05.000167+00:00 -> 2026-11-18 00:45:05.000167+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
