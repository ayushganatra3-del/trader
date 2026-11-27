# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T03:06:05.000132+00:00 · 74996 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.44 (-23.56%)

Closed trades 250, win rate 36.0%, fees £6.87, max drawdown -24.09%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 26.80 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 2490 decisions in 498 calls, $0.0347 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T03:06 | 2 / 3 / 0 | DOGE-USD 15% |  |
| Breezy | 2026-11-27T03:06 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T03:06 | 5 / 0 / 0 | ETH-USD 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| EMA 20/50 cross | TECL | 1.74 | +5.81% | 3 |
| Bollinger reversion · 1h | MSFT | 1.74 | +7.75% | 3 |
| Z-score reversion | SQQQ | 1.74 | +8.59% | 5 |
| EMA 20/50 cross | TQQQ | 1.64 | +4.16% | 4 |
| OBV trend | COIN | 1.45 | +1.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.60 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.96 | 15.96 | 0 | — | 14.88 | 4.95 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.10 | 5.10 | 0 | — | 6.08 | 1.60 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.06 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.23 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.30 | 0.49 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.11 | -5.89 | 0 | — | -6.75 | -1.71 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.59 | -6.41 | 24 | 12.5 | -5.31 | -7.71 | -6.56 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.33 | -6.67 | 0 | — | -7.99 | -1.59 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.16 | -6.84 | 63 | 41.3 | -4.98 | -0.83 | -14.79 | 73 |
| 16 | Trend pullback · 1h | trend | 91.57 | -8.43 | 116 | 24.1 | -6.87 | -4.38 | -10.25 | 29 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.52 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.20 | -10.80 | 0 | — | -12.17 | -2.61 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.14 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.09 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.82 | -14.18 | 20 | 20.0 | -13.31 | -2.92 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.25 | -2.43 | -20.49 | 154 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.08 | -16.92 | 79 | 20.3 | -19.61 | -6.63 | -19.85 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 79.96 | -20.04 | 224 | 41.1 | -13.25 | -6.05 | -13.46 | 62 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.18 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.86 | -23.14 | 174 | 29.3 | -22.14 | -8.69 | -22.45 | 72 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.18 | -6.02 | -27.63 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.54 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.33 | -24.67 | 216 | 27.8 | -33.89 | -8.08 | -35.01 | 186 |
| 31 | Donchian 55/20 · 1h | breakout | 74.65 | -25.35 | 88 | 13.6 | -29.14 | -7.52 | -29.32 | 75 |
| 32 | Ichimoku · 1h | trend | 74.03 | -25.97 | 114 | 15.8 | -28.05 | -6.91 | -29.63 | 100 |
| 33 | Max aggression: 5-day momentum | meta | 74.02 | -25.98 | 27 | 37.0 | -54.97 | -2.81 | -67.33 | 22 |
| 34 | Keltner breakout · 1h | breakout | 72.96 | -27.04 | 143 | 24.5 | -27.07 | -6.57 | -27.07 | 145 |
| 35 | Daily: Momentum burst | daily | 71.07 | -28.93 | 31 | 16.1 | -33.19 | -4.51 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 71.02 | -28.98 | 3 | 0.0 | -27.09 | -4.63 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.95 | -30.05 | 272 | 19.9 | -37.38 | -6.92 | -38.27 | 290 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 67.86 | -32.14 | 3 | 0.0 | -25.48 | -3.13 | -33.66 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 67.78 | -32.22 | 215 | 22.8 | -31.75 | -8.13 | -32.18 | 212 |
| 40 | Supertrend · 1h | trend | 67.29 | -32.70 | 221 | 17.6 | -39.86 | -7.75 | -42.12 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.67 | -33.33 | 411 | 39.9 | -32.82 | -3.39 | -42.70 | 437 |
| 42 | OBV trend · 1h | momentum | 66.45 | -33.55 | 325 | 19.7 | -40.14 | -9.68 | -41.11 | 225 |
| 43 | EMA 20/50 cross · 1h | trend | 66.09 | -33.91 | 126 | 9.5 | -36.55 | -9.73 | -37.86 | 116 |
| 44 | Triple EMA stack · 1h | trend | 65.61 | -34.39 | 172 | 15.1 | -40.82 | -9.66 | -42.40 | 169 |
| 45 | RSI momentum · 1h | momentum | 63.38 | -36.62 | 203 | 14.8 | -42.13 | -8.99 | -43.57 | 192 |
| 46 | MACD zero-line · 1h | trend | 63.07 | -36.93 | 206 | 16.5 | -36.59 | -10.03 | -36.92 | 199 |
| 47 | MFI reversion · 1h | reversion | 62.68 | -37.32 | 520 | 32.7 | -32.20 | -4.70 | -38.15 | 193 |
| 48 | Donchian 20/10 · 1h | breakout | 61.42 | -38.58 | 183 | 17.5 | -40.70 | -8.82 | -42.94 | 201 |
| 49 | Heikin-Ashi · 1h | trend | 60.69 | -39.31 | 559 | 21.6 | -49.49 | -10.02 | -49.87 | 649 |
| 50 | ROC + volume · 1h | momentum | 60.55 | -39.45 | 472 | 26.9 | -40.01 | -7.67 | -40.93 | 339 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.59 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.77 | -41.23 | 314 | 12.1 | -44.05 | -9.80 | -46.18 | 328 |
| 53 | MACD cross · 1h | trend | 57.31 | -42.69 | 497 | 21.1 | -53.31 | -10.63 | -55.07 | 511 |
| 54 | Agent (ML meta-label) | meta | 56.25 | -43.75 | 2074 | 25.4 | -19.18 | -2.36 | -26.11 | 316 |
| 55 | CCI reversion · 1h | reversion | 52.58 | -47.42 | 467 | 38.3 | -52.26 | -8.65 | -55.31 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.20 | -47.80 | 406 | 36.5 | -40.74 | -4.92 | -45.50 | 429 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.64 | -8.93 | -58.35 | 686 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.88 | -9.14 | -59.57 | 603 |
| 59 | VWAP momentum · 1h | momentum | 50.63 | -49.37 | 1112 | 21.3 | -60.65 | -13.03 | -60.91 | 1196 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.18 | -44.47 | -99.20 | 5408 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.41 | -30.06 | -83.67 | 1426 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.13 | -42.33 | -94.22 | 2397 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.16 | -28.80 | -90.49 | 1883 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -36.81 | -91.49 | 2224 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.67 | -26.04 | -88.75 | 1931 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -44.00 | -98.18 | 3411 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.79 | -45.85 | -96.84 | 3347 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.45 | -33.30 | -93.51 | 2120 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.92 | -33.57 | -81.92 | 1503 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -49.15 | -99.69 | 6279 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.71 | -34.87 | -92.85 | 2468 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.28 | -33.31 | -94.28 | 3141 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -55.83 | -99.81 | 6058 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.96 | -39.88 | -93.05 | 2258 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.21 | -18.64 | -51.40 | 656 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.93 | -22.61 | -78.20 | 1608 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -50.58 | -97.69 | 3230 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -53.31 | -99.16 | 5110 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.19 | -22.66 | -70.10 | 1200 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -42.68 | -94.64 | 2657 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.40 | -6.38 | -51.25 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.22 | -32.07 | -84.35 | 1645 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -59.99 | -99.77 | 6511 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.51 | -29.64 | -91.74 | 2498 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.74 | -19.52 | -83.22 | 1973 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.49 | -31.11 | -91.82 | 2156 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.19 | -44.85 | -98.21 | 4040 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.22 | -43.23 | -90.43 | 2197 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.14 | -28.39 | -68.20 | 784 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.79 | -26.89 | -72.99 | 1157 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.49 | -18.55 | -84.88 | 1828 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.07 | -45.25 | -98.08 | 4392 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -84.58 | -99.94 | 8300 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.28 | -6.76 | -52.52 | 291 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T03:00 | CCI reversion · 1h | sell | XRP-USD | 3.51 | 0.01 | exit signal |
| 2026-11-27T03:00 | CCI reversion · 1h | sell | ETH-USD | 3.77 | 0.02 | exit signal |
| 2026-11-27T03:00 | CCI reversion · 1h | sell | DOGE-USD | 3.79 | 0.04 | exit signal |
| 2026-11-27T03:00 | Bollinger reversion · 1h | sell | XRP-USD | 10.49 | 0.06 | exit signal |
| 2026-11-27T03:00 | Volume breakout · 1h | buy | ETH-USD | 19.13 | — | entry signal |
| 2026-11-27T03:00 | Volume breakout · 1h | buy | DOGE-USD | 19.21 | — | entry signal |
| 2026-11-27T03:00 | Volume breakout · 1h | buy | BTC-USD | 19.21 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | XRP-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | SOL-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | ETH-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | DOGE-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | BTC-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Donchian 55/20 · 1h | buy | SOL-USD | 18.65 | — | entry signal |
| 2026-11-27T03:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 18.65 | — | entry signal |
| 2026-11-27T03:00 | Donchian 20/10 · 1h | buy | BTC-USD | 3.28 | — | entry signal |
| 2026-11-27T03:00 | Donchian 20/10 · 1h | sell | XRP-USD | 3.28 | 0.03 | rebalance down |
| 2026-11-27T03:00 | ROC + volume · 1h | buy | SOL-USD | 10.01 | — | entry signal |
| 2026-11-27T03:00 | ROC + volume · 1h | buy | ETH-USD | 10.09 | — | entry signal |
| 2026-11-27T03:00 | ROC + volume · 1h | buy | DOGE-USD | 10.09 | — | entry signal |
| 2026-11-27T03:00 | ROC + volume · 1h | buy | BTC-USD | 10.09 | — | entry signal |
| 2026-11-27T03:00 | VWAP momentum · 1h | buy | XRP-USD | 1.87 | — | entry signal |
| 2026-11-27T03:00 | VWAP momentum · 1h | buy | SOL-USD | 1.87 | — | entry signal |
| 2026-11-27T03:00 | VWAP momentum · 1h | buy | ETH-USD | 1.87 | — | entry signal |
| 2026-11-27T03:00 | VWAP momentum · 1h | buy | DOGE-USD | 1.87 | — | entry signal |
| 2026-11-27T03:00 | VWAP momentum · 1h | buy | BTC-USD | 1.87 | — | entry signal |
| 2026-11-27T03:00 | Heikin-Ashi · 1h | buy | SOL-USD | 2.53 | — | entry signal |
| 2026-11-27T03:00 | Heikin-Ashi · 1h | buy | ETH-USD | 2.53 | — | entry signal |
| 2026-11-27T03:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.53 | — | entry signal |
| 2026-11-27T03:00 | Ichimoku · 1h | buy | ETH-USD | 5.00 | — | entry signal |
| 2026-11-27T03:00 | Ichimoku · 1h | buy | BTC-USD | 12.32 | — | entry signal |
| 2026-11-27T03:00 | Ichimoku · 1h | sell | XRP-USD | 4.88 | 0.03 | rebalance down |
| 2026-11-27T03:00 | Ichimoku · 1h | sell | SOL-USD | 6.21 | 0.05 | rebalance down |
| 2026-11-27T03:00 | Ichimoku · 1h | sell | DOGE-USD | 6.22 | 0.06 | rebalance down |
| 2026-11-27T03:00 | Parabolic SAR · 1h | buy | ETH-USD | 5.76 | — | entry signal |
| 2026-11-27T03:00 | Parabolic SAR · 1h | buy | DOGE-USD | 7.53 | — | entry signal |
| 2026-11-27T03:00 | Parabolic SAR · 1h | buy | BTC-USD | 7.53 | — | entry signal |
| 2026-11-27T03:00 | Parabolic SAR · 1h | sell | SOL-USD | 5.18 | 0.04 | rebalance down |
| 2026-11-27T03:00 | MACD cross · 1h | buy | SOL-USD | 2.73 | — | entry signal |
| 2026-11-27T03:00 | MACD cross · 1h | buy | ETH-USD | 2.73 | — | entry signal |
| 2026-11-27T03:00 | MACD cross · 1h | buy | BTC-USD | 2.73 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 03:06:05.000132+00:00 -> 2026-11-27 03:16:05.000132+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
