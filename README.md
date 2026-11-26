# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T04:05:05.000142+00:00 · 73810 ticks

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
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 28.29 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 2760 decisions in 552 calls, $0.0385 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T04:05 | 2 / 2 / 1 | XRP-USD 14% |  |
| Breezy | 2026-11-26T04:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T04:05 | 3 / 2 / 0 | ETH-USD 60% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.63 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.02 | 16.02 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.15 | 5.15 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.31 | 0.50 | -5.49 | 185 |
| 12 | Hold SPY | benchmark | 94.15 | -5.84 | 0 | — | -6.75 | -1.72 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.87 | -6.13 | 23 | 8.7 | -5.07 | -7.30 | -6.57 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.37 | -6.63 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.21 | -6.79 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.58 | -8.42 | 116 | 24.1 | -7.45 | -4.36 | -10.99 | 34 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.24 | -10.76 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.11 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.83 | -14.16 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.89 | -2.37 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.80 | -16.20 | 77 | 19.5 | -19.03 | -6.39 | -19.85 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.30 | -6.13 | -13.46 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.22 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 77.08 | -22.92 | 173 | 28.9 | -21.95 | -8.64 | -22.48 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.67 | -24.33 | 210 | 27.6 | -35.30 | -8.51 | -36.14 | 185 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 74.05 | -25.95 | 27 | 37.0 | -56.74 | -3.00 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.73 | -26.27 | 141 | 24.8 | -26.37 | -6.42 | -26.74 | 145 |
| 34 | Ichimoku · 1h | trend | 73.32 | -26.68 | 114 | 15.8 | -29.58 | -7.51 | -30.21 | 97 |
| 35 | Daily: Momentum burst | daily | 71.08 | -28.92 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.37 | -29.63 | 3 | 0.0 | -27.98 | -4.88 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 70.24 | -29.76 | 264 | 18.9 | -37.03 | -6.90 | -38.23 | 288 |
| 38 | Bollinger breakout · 1h | breakout | 68.97 | -31.03 | 209 | 22.5 | -30.58 | -7.73 | -31.80 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.89 | -32.11 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.08 | -32.92 | 221 | 17.6 | -40.16 | -7.92 | -42.12 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.70 | -33.30 | 411 | 39.9 | -32.82 | -3.42 | -42.70 | 439 |
| 42 | OBV trend · 1h | momentum | 66.48 | -33.52 | 325 | 19.7 | -42.18 | -10.35 | -42.37 | 228 |
| 43 | EMA 20/50 cross · 1h | trend | 65.93 | -34.07 | 126 | 9.5 | -37.81 | -10.38 | -38.01 | 115 |
| 44 | Triple EMA stack · 1h | trend | 65.21 | -34.79 | 172 | 15.1 | -43.10 | -10.48 | -43.32 | 173 |
| 45 | MACD zero-line · 1h | trend | 63.44 | -36.56 | 202 | 16.3 | -36.82 | -10.15 | -37.55 | 204 |
| 46 | RSI momentum · 1h | momentum | 62.98 | -37.02 | 203 | 14.8 | -43.34 | -9.53 | -44.17 | 195 |
| 47 | MFI reversion · 1h | reversion | 62.72 | -37.28 | 519 | 32.6 | -32.77 | -4.85 | -38.15 | 195 |
| 48 | Donchian 20/10 · 1h | breakout | 61.44 | -38.56 | 183 | 17.5 | -40.86 | -9.00 | -42.86 | 199 |
| 49 | ROC + volume · 1h | momentum | 61.20 | -38.80 | 465 | 26.7 | -39.93 | -7.67 | -41.19 | 335 |
| 50 | Heikin-Ashi · 1h | trend | 60.93 | -39.07 | 548 | 21.9 | -49.51 | -10.13 | -50.17 | 642 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.63 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.43 | -41.57 | 314 | 12.1 | -44.94 | -10.25 | -46.37 | 334 |
| 53 | MACD cross · 1h | trend | 57.46 | -42.54 | 492 | 20.3 | -53.91 | -10.89 | -55.68 | 513 |
| 54 | Agent (ML meta-label) | meta | 56.27 | -43.73 | 2074 | 25.4 | -20.34 | -2.60 | -28.57 | 315 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.10 | -8.96 | -55.49 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -4.96 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 51.00 | -49.00 | 1093 | 21.7 | -61.51 | -13.43 | -62.13 | 1192 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.64 | -9.03 | -58.27 | 686 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.31 | -9.36 | -59.57 | 607 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -47.54 | -99.17 | 5387 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.38 | -30.46 | -84.38 | 1425 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.18 | -45.02 | -94.39 | 2397 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.11 | -29.26 | -90.95 | 1882 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.25 | -38.27 | -91.75 | 2213 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.50 | -26.70 | -88.53 | 1920 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.13 | -45.72 | -98.22 | 3409 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -49.73 | -96.92 | 3349 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.90 | -34.88 | -92.90 | 2072 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.17 | -35.25 | -82.41 | 1514 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -52.50 | -99.69 | 6275 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.81 | -36.43 | -93.11 | 2469 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.14 | -34.99 | -94.14 | 3126 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -63.66 | -99.82 | 6074 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.95 | -41.69 | -93.23 | 2255 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.86 | -18.99 | -52.24 | 663 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.91 | -23.45 | -78.37 | 1607 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -55.52 | -97.73 | 3240 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -57.92 | -99.20 | 5121 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.98 | -22.64 | -70.48 | 1194 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.52 | -45.82 | -94.66 | 2651 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.44 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.20 | -34.09 | -84.50 | 1646 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -67.13 | -99.77 | 6524 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.53 | -30.43 | -91.91 | 2491 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.94 | -20.03 | -83.46 | 1967 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.61 | -32.41 | -91.94 | 2155 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.22 | -47.38 | -98.23 | 4052 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.23 | -45.51 | -90.68 | 2190 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.15 | -29.39 | -68.15 | 780 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.80 | -27.64 | -73.36 | 1154 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.73 | -19.11 | -85.02 | 1819 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.08 | -47.84 | -98.10 | 4396 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -95.04 | -99.94 | 8288 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.10 | -6.77 | -52.53 | 291 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T04:00 | VWAP momentum · 1h | sell | SOL-USD | 1.95 | -0.01 | exit signal |
| 2026-11-26T04:00 | Heikin-Ashi · 1h | buy | XRP-USD | 2.44 | — | entry signal |
| 2026-11-26T04:00 | Heikin-Ashi · 1h | sell | ETH-USD | 2.43 | -0.01 | exit signal |
| 2026-11-26T04:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 3.75 | — | entry signal |
| 2026-11-26T04:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 3.75 | -0.01 | rebalance down |
| 2026-11-26T03:00 | MFI reversion · 1h | sell | BTC-USD | 5.16 | 0.15 | exit signal |
| 2026-11-26T03:00 | VWAP momentum · 1h | sell | BTC-USD | 1.95 | -0.02 | exit signal |
| 2026-11-26T02:20 | ROC + volume · 1h | buy | DOGE-USD | 3.34 | — | rebalance up |
| 2026-11-26T02:20 | ROC + volume · 1h | buy | BTC-USD | 3.37 | — | rebalance up |
| 2026-11-26T02:00 | Keltner breakout · 1h | buy | XRP-USD | 18.40 | — | entry signal |
| 2026-11-26T02:00 | Keltner breakout · 1h | buy | DOGE-USD | 18.40 | — | entry signal |
| 2026-11-26T02:00 | VWAP momentum · 1h | buy | XRP-USD | 1.96 | — | entry signal |
| 2026-11-26T02:00 | VWAP momentum · 1h | buy | SOL-USD | 1.96 | — | entry signal |
| 2026-11-26T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 1.96 | — | entry signal |
| 2026-11-26T02:00 | VWAP momentum · 1h | buy | BTC-USD | 1.96 | — | entry signal |
| 2026-11-26T02:00 | Triple EMA stack · 1h | buy | XRP-USD | 16.27 | — | entry signal |
| 2026-11-26T02:00 | Triple EMA stack · 1h | buy | DOGE-USD | 16.27 | — | entry signal |
| 2026-11-26T02:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 2.23 | — | entry signal |
| 2026-11-26T02:00 | EMA 20/50 cross · 1h | buy | DOGE-USD | 13.18 | — | entry signal |
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | XRP-USD | 4.27 | 0.04 | exit signal |
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | SOL-USD | 4.28 | 0.05 | exit signal |
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | ETH-USD | 4.24 | 0.02 | exit signal |
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | DOGE-USD | 4.31 | 0.08 | exit signal |
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | BTC-USD | 4.26 | 0.03 | exit signal |
| 2026-11-26T00:00 | Heikin-Ashi · 1h | buy | SOL-USD | 2.44 | — | entry |
| 2026-11-26T00:00 | Heikin-Ashi · 1h | buy | ETH-USD | 2.44 | — | entry |
| 2026-11-26T00:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.44 | — | entry |
| 2026-11-26T00:00 | Heikin-Ashi · 1h | buy | BTC-USD | 2.44 | — | entry |
| 2026-11-25T22:11 | Three white soldiers · 1h | buy | DOGE-USD | 5.33 | — | rebalance up |
| 2026-11-25T22:11 | ROC + volume · 1h | buy | DOGE-USD | 6.75 | — | entry |
| 2026-11-25T22:11 | ROC + volume · 1h | sell | XRP-USD | 3.41 | 0.03 | rebalance down |
| 2026-11-25T22:11 | ROC + volume · 1h | sell | SOL-USD | 3.42 | 0.03 | rebalance down |
| 2026-11-25T22:11 | ROC + volume · 1h | sell | ETH-USD | 3.29 | -0.01 | rebalance down |
| 2026-11-25T22:11 | ROC + volume · 1h | sell | BTC-USD | 3.36 | 0.01 | rebalance down |
| 2026-11-25T22:00 | MACD zero-line · 1h | buy | BTC-USD | 7.88 | — | entry signal |
| 2026-11-25T22:00 | MACD zero-line · 1h | sell | XRP-USD | 7.85 | -0.05 | rebalance down |
| 2026-11-25T21:05 | Bollinger breakout · 1h | buy | BTC-USD | 3.43 | — | rebalance up |
| 2026-11-25T21:05 | Bollinger breakout · 1h | sell | DOGE-USD | 3.43 | 0.01 | rebalance down |
| 2026-11-25T21:00 | Bollinger breakout · 1h | buy | BTC-USD | 10.21 | — | entry signal |
| 2026-11-25T21:00 | Bollinger breakout · 1h | sell | XRP-USD | 3.40 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 04:05:05.000142+00:00 -> 2026-11-26 04:15:05.000142+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
