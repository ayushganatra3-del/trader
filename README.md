# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T19:11:05.000145+00:00 · 73378 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.46 (-23.54%)

Closed trades 249, win rate 36.1%, fees £6.85, max drawdown -23.90%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 15.12 | -0.28 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 26.36 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 32811 decisions in 2958 calls, $0.4088 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T19:11 | 2 / 21 / 7 | cash |  |
| Breezy | 2026-11-25T19:11 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-25T19:11 | 8 / 21 / 1 | COIN 80% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| Bollinger reversion · 1h | ETH-USD | 1.78 | +4.64% | 7 |
| MFI reversion | SQQQ | 1.78 | +11.82% | 4 |
| RSI(14) reversion · 1h | ETH-USD | 1.77 | +5.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 23.61 | 3.54 | -5.42 | 29 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.14 | 16.14 | 0 | — | 14.91 | 5.04 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.73 | 1.11 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.03 | 5.03 | 0 | — | 5.27 | 1.55 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.49 | -0.06 | -8.01 | 210 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.65 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | -0.45 | -0.06 | -6.21 | 167 |
| 12 | Hold SPY | benchmark | 94.22 | -5.78 | 0 | — | -6.78 | -1.75 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.26 | -6.74 | 21 | 9.5 | -5.69 | -7.79 | -6.66 | 22 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.06 | -6.94 | 0 | — | -8.24 | -1.68 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 91.98 | -8.02 | 62 | 40.3 | -5.80 | -1.02 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.56 | -8.44 | 116 | 24.1 | -6.38 | -3.29 | -9.95 | 36 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 88.64 | -11.37 | 0 | — | -12.33 | -2.68 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.05 | -2.97 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 87.13 | -12.87 | 478 | 32.4 | -10.02 | -3.03 | -15.55 | 552 |
| 21 | Daily: Bullish score | daily | 85.81 | -14.19 | 20 | 20.0 | -13.14 | -2.92 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.79 | -2.38 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -17.12 | -6.35 | -17.15 | 68 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.87 | -5.92 | -13.04 | 60 |
| 26 | Opening range 15m | breakout | 79.42 | -20.58 | 601 | 30.3 | -19.55 | -5.40 | -24.90 | 685 |
| 27 | Volume breakout · 1h | breakout | 76.70 | -23.30 | 170 | 28.2 | -22.08 | -9.36 | -22.30 | 69 |
| 28 | Agent | meta | 76.46 | -23.54 | 249 | 36.1 | -27.79 | -6.29 | -27.98 | 199 |
| 29 | Agent (aggressive) | meta | 75.68 | -24.32 | 114 | 33.3 | -17.92 | -4.65 | -18.51 | 92 |
| 30 | Parabolic SAR · 1h | trend | 75.23 | -24.77 | 210 | 27.6 | -35.47 | -8.66 | -35.98 | 185 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.44 | -7.82 | -29.45 | 74 |
| 32 | Max aggression: 5-day momentum | meta | 74.40 | -25.60 | 27 | 37.0 | -56.51 | -2.98 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.69 | -26.31 | 141 | 24.8 | -27.76 | -6.87 | -28.21 | 151 |
| 34 | Ichimoku · 1h | trend | 73.41 | -26.59 | 114 | 15.8 | -30.89 | -7.91 | -31.69 | 102 |
| 35 | Daily: Momentum burst | daily | 71.17 | -28.84 | 31 | 16.1 | -33.49 | -4.64 | -36.38 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.90 | -30.10 | 264 | 18.9 | -38.19 | -7.38 | -39.05 | 275 |
| 37 | Hold BTC | benchmark | 69.28 | -30.72 | 3 | 0.0 | -29.07 | -5.18 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -31.85 | -8.35 | -32.27 | 204 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 68.11 | -31.89 | 3 | 0.0 | -25.73 | -3.22 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 66.81 | -33.19 | 221 | 17.6 | -40.22 | -7.98 | -41.89 | 210 |
| 41 | OBV trend · 1h | momentum | 66.69 | -33.31 | 324 | 19.8 | -39.20 | -9.50 | -40.78 | 226 |
| 42 | Stochastic reversion · 1h | reversion | 66.40 | -33.60 | 411 | 39.9 | -34.21 | -3.67 | -43.52 | 443 |
| 43 | EMA 20/50 cross · 1h | trend | 65.87 | -34.13 | 126 | 9.5 | -38.26 | -10.65 | -38.50 | 113 |
| 44 | Triple EMA stack · 1h | trend | 65.08 | -34.92 | 172 | 15.1 | -42.68 | -10.46 | -42.95 | 170 |
| 45 | MACD zero-line · 1h | trend | 63.27 | -36.73 | 202 | 16.3 | -34.82 | -9.55 | -35.24 | 196 |
| 46 | RSI momentum · 1h | momentum | 62.66 | -37.34 | 203 | 14.8 | -43.58 | -9.85 | -44.00 | 189 |
| 47 | MFI reversion · 1h | reversion | 62.53 | -37.47 | 513 | 32.2 | -32.12 | -4.76 | -37.72 | 198 |
| 48 | Donchian 20/10 · 1h | breakout | 61.42 | -38.58 | 183 | 17.5 | -41.13 | -9.22 | -42.84 | 197 |
| 49 | Heikin-Ashi · 1h ⏸ | trend | 60.88 | -39.12 | 547 | 21.9 | -50.47 | -10.42 | -51.35 | 628 |
| 50 | ROC + volume · 1h | momentum | 60.70 | -39.30 | 462 | 26.8 | -40.58 | -7.99 | -41.43 | 337 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -61.89 | -4.66 | -63.57 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.33 | -41.66 | 314 | 12.1 | -45.15 | -10.53 | -46.62 | 327 |
| 53 | MACD cross · 1h | trend | 57.13 | -42.87 | 492 | 20.3 | -54.07 | -11.02 | -55.58 | 506 |
| 54 | Agent (ML meta-label) | meta | 56.26 | -43.74 | 2073 | 25.4 | -20.21 | -2.56 | -27.40 | 326 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.21 | -9.10 | -55.42 | 511 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.82 | -5.01 | -45.50 | 431 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -57.03 | -9.46 | -59.29 | 705 |
| 58 | VWAP momentum · 1h | momentum | 50.89 | -49.11 | 1086 | 21.5 | -60.59 | -13.40 | -61.82 | 1180 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.37 | -9.46 | -59.60 | 609 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -49.28 | -99.19 | 5382 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.62 | -32.37 | -84.43 | 1428 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.25 | -46.42 | -94.44 | 2406 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.55 | -31.36 | -91.19 | 1905 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.44 | -40.04 | -91.82 | 2221 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.99 | -27.79 | -89.03 | 1916 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -48.33 | -98.24 | 3422 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.80 | -50.32 | -96.92 | 3334 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.53 | -34.26 | -92.68 | 2029 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.11 | -34.72 | -82.43 | 1504 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -57.68 | -99.70 | 6308 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -37.37 | -93.27 | 2475 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.04 | -35.50 | -94.06 | 3122 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -67.79 | -99.83 | 6086 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.94 | -42.52 | -93.26 | 2263 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.32 | -17.18 | -52.43 | 664 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.72 | -22.21 | -78.95 | 1596 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -57.50 | -97.75 | 3224 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.80 | -99.22 | 5141 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.22 | -21.70 | -71.18 | 1196 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.45 | -44.29 | -94.76 | 2650 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.95 | -6.62 | -51.26 | 292 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.10 | -32.31 | -84.78 | 1657 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -77.03 | -99.78 | 6536 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.58 | -31.61 | -91.95 | 2501 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.91 | -20.33 | -83.42 | 1967 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.07 | -34.71 | -92.28 | 2167 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -50.61 | -98.24 | 4065 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.23 | -46.33 | -90.79 | 2217 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.69 | -25.00 | -68.12 | 778 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.88 | -27.89 | -73.36 | 1156 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -85.05 | -19.61 | -85.19 | 1839 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -51.16 | -98.12 | 4411 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -106.14 | -99.94 | 8277 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -45.54 | -6.67 | -52.62 | 298 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T19:00 | Agent | sell | SQQQ | 15.45 | -0.06 | rebalance down |
| 2026-11-25T19:00 | MFI reversion · 1h | buy | AMD | 4.77 | — | entry |
| 2026-11-25T19:00 | MFI reversion · 1h | sell | XRP-USD | 5.09 | 0.08 | exit signal |
| 2026-11-25T19:00 | Three white soldiers · 1h | buy | DOGE-USD | 23.20 | — | entry signal |
| 2026-11-25T19:00 | Supertrend · 1h | buy | XRP-USD | 3.68 | — | entry signal |
| 2026-11-25T19:00 | Supertrend · 1h | sell | SQQQ | 3.68 | -0.36 | rebalance down |
| 2026-11-25T18:55 | Agent | buy | SQQQ | 15.26 | — | rebalance up |
| 2026-11-25T18:50 | Agent | sell | SQQQ | 14.88 | -0.35 | rebalance down |
| 2026-11-25T18:45 | RSI momentum · 1h | sell | SQQQ | 14.22 | -1.38 | stop-loss |
| 2026-11-25T18:45 | ROC + volume · 1h | buy | META | 1.13 | — | entry |
| 2026-11-25T18:45 | ROC + volume · 1h | buy | IWM | 8.62 | — | entry |
| 2026-11-25T18:45 | ROC + volume · 1h | sell | SQQQ | 9.75 | -0.94 | stop-loss |
| 2026-11-25T18:45 | Parabolic SAR · 1h | sell | SQQQ | 9.30 | -0.90 | stop-loss |
| 2026-11-25T18:45 | MACD cross · 1h | sell | SQQQ | 4.98 | -0.46 | stop-loss |
| 2026-11-25T18:45 | Triple EMA stack · 1h | sell | SQQQ | 15.17 | -1.47 | stop-loss |
| 2026-11-25T18:45 | EMA 9/21 cross · 1h | buy | TNA | 5.61 | — | rebalance up |
| 2026-11-25T18:45 | EMA 9/21 cross · 1h | buy | IWM | 2.92 | — | rebalance up |
| 2026-11-25T18:45 | EMA 9/21 cross · 1h | sell | SQQQ | 13.05 | -1.26 | stop-loss |
| 2026-11-25T18:40 | Volume breakout · 1h | buy | IWM | 19.16 | — | entry |
| 2026-11-25T18:35 | Agent | buy | SQQQ | 15.37 | — | rebalance up |
| 2026-11-25T18:35 | Copy: Insider buying | buy | PLTR | 10.34 | — | rebalance up |
| 2026-11-25T18:35 | Copy: Insider buying | sell | FUN | 10.97 | -0.61 | target is flat |
| 2026-11-25T18:30 | Agent | sell | SQQQ | 15.30 | -0.09 | rebalance down |
| 2026-11-25T18:30 | Three white soldiers · 1h | buy | MSTR | 23.14 | — | entry signal |
| 2026-11-25T18:30 | Volume breakout · 1h | buy | META | 19.16 | — | entry signal |
| 2026-11-25T18:30 | Keltner breakout · 1h | buy | LABU | 18.35 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | buy | TNA | 12.21 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | buy | META | 12.21 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | buy | IWM | 12.21 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | buy | AAPL | 12.21 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | sell | LABU | 4.28 | 0.32 | rebalance down |
| 2026-11-25T18:30 | OBV trend · 1h | buy | AAPL | 16.68 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | TNA | 4.15 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | PLTR | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | IWM | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | ETHU | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | COIN | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | AAPL | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | sell | XRP-USD | 4.19 | -0.03 | rebalance down |
| 2026-11-25T18:30 | VWAP momentum · 1h | sell | SOL-USD | 4.20 | -0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 19:11:05.000145+00:00 -> 2026-11-25 19:21:05.000145+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
