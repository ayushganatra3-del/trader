# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T01:35:05.000150+00:00 · 74915 ticks

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

Today: 1275 decisions in 255 calls, $0.0178 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T01:35 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-27T01:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T01:35 | 1 / 4 / 0 | ETH-USD 59% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.12 | 16.12 | 0 | — | 14.88 | 4.95 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.24 | 5.24 | 0 | — | 6.08 | 1.60 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.06 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.23 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.30 | 0.49 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.23 | -5.76 | 0 | — | -6.75 | -1.71 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.68 | -6.32 | 24 | 12.5 | -5.31 | -7.71 | -6.56 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.45 | -6.55 | 0 | — | -7.99 | -1.59 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.28 | -6.71 | 63 | 41.3 | -4.98 | -0.83 | -14.79 | 73 |
| 16 | Trend pullback · 1h | trend | 91.60 | -8.40 | 116 | 24.1 | -7.04 | -4.44 | -10.42 | 29 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.32 | -10.68 | 0 | — | -12.17 | -2.61 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.52 | -11.13 | 23 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.14 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.09 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.85 | -14.15 | 20 | 20.0 | -13.31 | -2.92 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.07 | -2.39 | -20.49 | 155 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.08 | -16.92 | 79 | 20.3 | -19.52 | -6.60 | -19.77 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 80.02 | -19.98 | 222 | 41.0 | -13.20 | -6.01 | -13.46 | 62 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.18 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.85 | -23.15 | 174 | 29.3 | -22.18 | -8.72 | -22.44 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.12 | -6.00 | -27.66 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -16.84 | -4.27 | -18.13 | 87 |
| 30 | Parabolic SAR · 1h | trend | 75.20 | -24.80 | 216 | 27.8 | -34.08 | -8.15 | -35.01 | 182 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.18 | -7.54 | -29.22 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 74.12 | -25.88 | 27 | 37.0 | -54.97 | -2.81 | -67.33 | 22 |
| 33 | Ichimoku · 1h | trend | 73.28 | -26.72 | 114 | 15.8 | -28.89 | -7.23 | -29.63 | 98 |
| 34 | Keltner breakout · 1h | breakout | 72.99 | -27.01 | 143 | 24.5 | -26.99 | -6.55 | -26.99 | 145 |
| 35 | Daily: Momentum burst | daily | 71.09 | -28.91 | 31 | 16.1 | -33.19 | -4.51 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.19 | -29.81 | 3 | 0.0 | -28.06 | -4.87 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.82 | -30.18 | 272 | 19.9 | -37.41 | -6.94 | -38.13 | 290 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 67.95 | -32.05 | 3 | 0.0 | -25.48 | -3.13 | -33.66 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 67.70 | -32.30 | 215 | 22.8 | -31.71 | -8.13 | -31.90 | 207 |
| 40 | Supertrend · 1h | trend | 67.08 | -32.92 | 221 | 17.6 | -40.23 | -7.88 | -42.10 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.75 | -33.25 | 411 | 39.9 | -32.42 | -3.33 | -42.70 | 437 |
| 42 | OBV trend · 1h | momentum | 66.53 | -33.47 | 325 | 19.7 | -40.86 | -9.99 | -41.30 | 223 |
| 43 | EMA 20/50 cross · 1h | trend | 65.92 | -34.09 | 126 | 9.5 | -38.04 | -10.25 | -38.68 | 117 |
| 44 | Triple EMA stack · 1h | trend | 64.89 | -35.11 | 172 | 15.1 | -40.73 | -9.94 | -41.50 | 168 |
| 45 | MACD zero-line · 1h | trend | 63.13 | -36.87 | 206 | 16.5 | -36.76 | -10.09 | -36.99 | 199 |
| 46 | RSI momentum · 1h | momentum | 62.87 | -37.13 | 203 | 14.8 | -42.82 | -9.30 | -43.57 | 192 |
| 47 | MFI reversion · 1h | reversion | 62.75 | -37.25 | 520 | 32.7 | -32.59 | -4.78 | -38.15 | 194 |
| 48 | Donchian 20/10 · 1h | breakout | 61.38 | -38.62 | 183 | 17.5 | -41.03 | -8.95 | -42.94 | 199 |
| 49 | Heikin-Ashi · 1h | trend | 60.68 | -39.32 | 559 | 21.6 | -49.50 | -10.02 | -49.87 | 646 |
| 50 | ROC + volume · 1h | momentum | 60.54 | -39.46 | 472 | 26.9 | -40.06 | -7.68 | -40.93 | 334 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.59 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.38 | -41.62 | 314 | 12.1 | -44.50 | -9.98 | -45.97 | 328 |
| 53 | MACD cross · 1h | trend | 57.36 | -42.64 | 497 | 21.1 | -52.77 | -10.44 | -54.55 | 506 |
| 54 | Agent (ML meta-label) | meta | 56.29 | -43.71 | 2074 | 25.4 | -17.63 | -2.06 | -25.35 | 311 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 464 | 37.9 | -52.41 | -8.69 | -55.31 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.11 | -47.89 | 405 | 36.3 | -40.89 | -4.94 | -45.50 | 432 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.13 | -9.05 | -58.51 | 691 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.88 | -9.14 | -59.57 | 603 |
| 59 | VWAP momentum · 1h | momentum | 50.66 | -49.34 | 1112 | 21.3 | -60.99 | -13.19 | -61.28 | 1194 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.17 | -44.86 | -99.18 | 5395 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.64 | -31.07 | -83.64 | 1424 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.20 | -43.75 | -94.20 | 2394 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.32 | -29.60 | -90.49 | 1883 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.51 | -38.13 | -91.51 | 2224 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.70 | -26.16 | -88.70 | 1927 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -45.24 | -98.17 | 3407 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -47.41 | -96.84 | 3345 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.46 | -33.47 | -93.46 | 2114 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.97 | -33.70 | -81.97 | 1505 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -48.95 | -99.68 | 6275 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.81 | -35.78 | -92.85 | 2466 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.28 | -33.33 | -94.28 | 3140 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -57.50 | -99.81 | 6064 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.04 | -40.90 | -93.04 | 2258 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.33 | -18.73 | -51.52 | 657 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.93 | -22.61 | -78.05 | 1603 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -52.01 | -97.68 | 3227 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -53.39 | -99.17 | 5114 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.17 | -22.64 | -70.10 | 1198 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -44.17 | -94.64 | 2656 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.40 | -6.38 | -51.25 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.29 | -32.38 | -84.30 | 1641 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -60.50 | -99.77 | 6516 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.51 | -29.64 | -91.74 | 2498 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.69 | -19.48 | -83.18 | 1972 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.55 | -31.13 | -91.89 | 2159 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -45.15 | -98.24 | 4049 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.39 | -45.18 | -90.43 | 2197 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.06 | -28.20 | -68.09 | 780 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.81 | -26.92 | -72.81 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.87 | -18.81 | -85.25 | 1835 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.09 | -45.60 | -98.11 | 4398 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -83.45 | -99.94 | 8296 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.52 | -6.82 | -52.52 | 295 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T01:00 | CCI reversion · 1h | buy | ETH-USD | 3.75 | — | entry signal |
| 2026-11-27T01:00 | CCI reversion · 1h | buy | DOGE-USD | 3.75 | — | entry signal |
| 2026-11-27T01:00 | Bollinger reversion · 1h | buy | XRP-USD | 10.43 | — | entry signal |
| 2026-11-27T01:00 | Ichimoku · 1h | buy | XRP-USD | 17.06 | — | entry signal |
| 2026-11-27T01:00 | Ichimoku · 1h | buy | SOL-USD | 18.33 | — | entry signal |
| 2026-11-27T01:00 | Ichimoku · 1h | buy | DOGE-USD | 18.33 | — | entry signal |
| 2026-11-27T00:40 | Parabolic SAR · 1h | sell | ETH-USD | 10.68 | -0.06 | target is flat |
| 2026-11-27T00:35 | Parabolic SAR · 1h | buy | ETH-USD | 10.74 | — | entry |
| 2026-11-27T00:20 | Parabolic SAR · 1h | sell | ETH-USD | 10.70 | -0.05 | target is flat |
| 2026-11-27T00:15 | Parabolic SAR · 1h | buy | ETH-USD | 10.74 | — | entry |
| 2026-11-27T00:00 | Connors RSI(2) · 1h | buy | XRP-USD | 19.97 | — | entry signal |
| 2026-11-27T00:00 | VWAP momentum · 1h | sell | SOL-USD | 2.19 | -0.01 | exit signal |
| 2026-11-26T23:15 | Parabolic SAR · 1h | sell | ETH-USD | 10.68 | -0.07 | target is flat |
| 2026-11-26T23:10 | Parabolic SAR · 1h | buy | ETH-USD | 10.75 | — | entry |
| 2026-11-26T23:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 20.00 | — | entry signal |
| 2026-11-26T23:00 | Bollinger breakout · 1h | sell | SOL-USD | 17.11 | 0.06 | exit signal |
| 2026-11-26T23:00 | Bollinger breakout · 1h | sell | DOGE-USD | 16.75 | -0.27 | exit signal |
| 2026-11-26T23:00 | VWAP momentum · 1h | sell | XRP-USD | 2.09 | -0.02 | exit signal |
| 2026-11-26T23:00 | VWAP momentum · 1h | sell | ETH-USD | 1.93 | -0.02 | exit signal |
| 2026-11-26T23:00 | VWAP momentum · 1h | sell | DOGE-USD | 1.92 | -0.03 | exit signal |
| 2026-11-26T23:00 | VWAP momentum · 1h | sell | BTC-USD | 1.86 | -0.02 | exit signal |
| 2026-11-26T23:00 | Heikin-Ashi · 1h | sell | SOL-USD | 2.51 | -0.02 | exit signal |
| 2026-11-26T23:00 | Heikin-Ashi · 1h | sell | ETH-USD | 2.50 | -0.03 | exit signal |
| 2026-11-26T23:00 | Heikin-Ashi · 1h | sell | BTC-USD | 2.51 | -0.03 | exit signal |
| 2026-11-26T23:00 | ADX DI cross · 1h | buy | SOL-USD | 3.89 | — | rebalance up |
| 2026-11-26T23:00 | ADX DI cross · 1h | sell | XRP-USD | 8.67 | -0.08 | exit signal |
| 2026-11-26T23:00 | ADX DI cross · 1h | sell | ETH-USD | 3.66 | -0.05 | exit signal |
| 2026-11-26T23:00 | ADX DI cross · 1h | sell | DOGE-USD | 6.29 | 0.02 | exit signal |
| 2026-11-26T23:00 | ADX DI cross · 1h | sell | BTC-USD | 6.97 | -0.03 | exit signal |
| 2026-11-26T22:10 | Parabolic SAR · 1h | sell | ETH-USD | 10.68 | -0.10 | target is flat |
| 2026-11-26T22:00 | CCI reversion · 1h | sell | ETH-USD | 4.05 | 0.01 | exit signal |
| 2026-11-26T22:00 | Heikin-Ashi · 1h | buy | BTC-USD | 2.53 | — | entry signal |
| 2026-11-26T22:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.51 | -0.02 | exit signal |
| 2026-11-26T22:00 | Parabolic SAR · 1h | buy | ETH-USD | 10.78 | — | entry signal |
| 2026-11-26T21:00 | Heikin-Ashi · 1h | buy | ETH-USD | 2.53 | — | entry signal |
| 2026-11-26T21:00 | Heikin-Ashi · 1h | sell | XRP-USD | 2.52 | -0.02 | exit signal |
| 2026-11-26T20:00 | Bollinger breakout · 1h | buy | DOGE-USD | 17.02 | — | entry signal |
| 2026-11-26T20:00 | VWAP momentum · 1h | buy | BTC-USD | 1.88 | — | entry signal |
| 2026-11-26T20:00 | Heikin-Ashi · 1h | buy | XRP-USD | 2.53 | — | entry signal |
| 2026-11-26T20:00 | Heikin-Ashi · 1h | buy | SOL-USD | 2.53 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 01:35:05.000150+00:00 -> 2026-11-27 01:45:05.000150+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
