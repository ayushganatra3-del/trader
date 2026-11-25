# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T23:40:05.000128+00:00 · 73592 ticks

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
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 28.04 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 42600 decisions in 3600 calls, $0.5273 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T23:40 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-25T23:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-25T23:40 | 2 / 3 / 0 | ETH-USD 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| Bollinger reversion · 1h | ETH-USD | 1.78 | +4.64% | 7 |
| RSI(14) reversion · 1h | ETH-USD | 1.77 | +5.50% | 3 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.66 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.96 | 15.96 | 0 | — | 14.88 | 5.04 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.12 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.10 | 5.10 | 0 | — | 6.08 | 1.63 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | 0.39 | 0.21 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.11 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.50 | 0.56 | -5.49 | 177 |
| 12 | Hold SPY | benchmark | 94.10 | -5.90 | 0 | — | -6.75 | -1.74 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.49 | -6.51 | 23 | 8.7 | -5.39 | -7.87 | -6.57 | 25 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.32 | -6.68 | 0 | — | -7.99 | -1.62 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.16 | -6.84 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.57 | -8.43 | 116 | 24.1 | -7.45 | -4.39 | -10.99 | 34 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.65 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.20 | -10.80 | 0 | — | -12.17 | -2.66 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.19 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.29 | -3.16 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.82 | -14.18 | 20 | 20.0 | -13.31 | -2.96 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.88 | -2.39 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.16 | -16.84 | 77 | 19.5 | -19.64 | -6.74 | -19.85 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.30 | -6.18 | -13.46 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.41 | -5.18 | -23.63 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.72 | -23.28 | 173 | 28.9 | -22.12 | -8.91 | -22.57 | 71 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.15 | -6.11 | -27.61 | 195 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.72 | -4.61 | -18.54 | 92 |
| 30 | Parabolic SAR · 1h | trend | 75.23 | -24.77 | 210 | 27.6 | -35.64 | -8.74 | -36.09 | 185 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.48 | -7.83 | -29.49 | 74 |
| 32 | Max aggression: 5-day momentum | meta | 74.02 | -25.98 | 27 | 37.0 | -56.74 | -3.02 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.59 | -26.41 | 141 | 24.8 | -26.43 | -6.50 | -26.70 | 143 |
| 34 | Ichimoku · 1h | trend | 73.31 | -26.69 | 114 | 15.8 | -29.88 | -7.64 | -30.60 | 99 |
| 35 | Daily: Momentum burst | daily | 71.07 | -28.93 | 31 | 16.1 | -33.19 | -4.59 | -35.97 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.78 | -30.22 | 264 | 18.9 | -37.51 | -7.09 | -38.33 | 287 |
| 37 | Hold BTC | benchmark | 69.69 | -30.31 | 3 | 0.0 | -28.95 | -5.15 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.02 | -31.98 | 209 | 22.5 | -31.50 | -8.19 | -31.80 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.86 | -32.15 | 3 | 0.0 | -25.48 | -3.18 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 66.78 | -33.23 | 221 | 17.6 | -40.85 | -8.19 | -42.48 | 212 |
| 41 | Stochastic reversion · 1h | reversion | 66.66 | -33.34 | 411 | 39.9 | -32.85 | -3.45 | -42.70 | 440 |
| 42 | OBV trend · 1h | momentum | 66.44 | -33.56 | 325 | 19.7 | -42.15 | -10.46 | -42.35 | 224 |
| 43 | EMA 20/50 cross · 1h | trend | 65.90 | -34.10 | 126 | 9.5 | -38.23 | -10.66 | -38.45 | 113 |
| 44 | Triple EMA stack · 1h | trend | 65.10 | -34.91 | 172 | 15.1 | -42.79 | -10.59 | -43.30 | 171 |
| 45 | MACD zero-line · 1h | trend | 63.14 | -36.87 | 202 | 16.3 | -37.27 | -10.49 | -37.57 | 203 |
| 46 | MFI reversion · 1h | reversion | 62.63 | -37.37 | 518 | 32.4 | -32.48 | -4.83 | -38.04 | 197 |
| 47 | RSI momentum · 1h | momentum | 62.39 | -37.60 | 203 | 14.8 | -43.87 | -9.83 | -44.18 | 195 |
| 48 | Donchian 20/10 · 1h | breakout | 61.20 | -38.80 | 183 | 17.5 | -41.65 | -9.37 | -43.19 | 200 |
| 49 | Heikin-Ashi · 1h ⏸ | trend | 60.88 | -39.12 | 547 | 21.9 | -49.70 | -10.27 | -50.29 | 642 |
| 50 | ROC + volume · 1h | momentum | 60.74 | -39.26 | 465 | 26.7 | -40.76 | -7.99 | -41.45 | 340 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.66 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.03 | -41.97 | 314 | 12.1 | -45.39 | -10.52 | -46.48 | 334 |
| 53 | MACD cross · 1h | trend | 57.22 | -42.78 | 492 | 20.3 | -54.11 | -11.07 | -55.73 | 512 |
| 54 | Agent (ML meta-label) | meta | 56.25 | -43.75 | 2074 | 25.4 | -18.94 | -2.37 | -27.50 | 326 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.12 | -9.05 | -55.51 | 502 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -5.01 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 50.98 | -49.02 | 1086 | 21.5 | -61.65 | -13.44 | -62.36 | 1187 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.93 | -9.14 | -58.67 | 683 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.62 | -9.55 | -59.58 | 609 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -49.32 | -99.17 | 5374 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.56 | -32.28 | -84.47 | 1428 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.21 | -48.39 | -94.39 | 2392 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.46 | -31.27 | -91.13 | 1884 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.32 | -40.52 | -91.75 | 2211 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.62 | -27.37 | -88.66 | 1915 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.16 | -49.39 | -98.22 | 3409 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.80 | -52.51 | -96.91 | 3338 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.90 | -35.43 | -92.90 | 2067 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.10 | -35.92 | -82.31 | 1502 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -57.74 | -99.70 | 6290 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -38.66 | -93.15 | 2472 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.10 | -35.96 | -94.10 | 3125 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.94 | -99.82 | 6068 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.93 | -43.19 | -93.21 | 2253 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.43 | -18.58 | -52.05 | 661 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.44 | -23.09 | -78.42 | 1599 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -59.60 | -97.71 | 3233 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.96 | -99.22 | 5134 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.28 | -22.66 | -70.92 | 1197 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.54 | -47.62 | -94.70 | 2649 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.50 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.16 | -34.72 | -84.51 | 1643 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -77.28 | -99.77 | 6530 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -31.57 | -91.96 | 2499 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.97 | -20.42 | -83.50 | 1971 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.82 | -34.20 | -91.99 | 2165 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.22 | -50.71 | -98.23 | 4059 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.35 | -48.12 | -90.73 | 2194 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.82 | -26.13 | -67.97 | 777 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.54 | -28.28 | -73.25 | 1150 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.86 | -19.54 | -85.07 | 1827 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -51.33 | -98.12 | 4399 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.59 | -99.94 | 8280 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.00 | -6.80 | -52.53 | 290 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-25T21:00 | Bollinger breakout · 1h | sell | SOL-USD | 3.41 | -0.01 | rebalance down |
| 2026-11-25T21:00 | Bollinger breakout · 1h | sell | ETH-USD | 3.40 | -0.01 | rebalance down |
| 2026-11-25T21:00 | RSI momentum · 1h | buy | BTC-USD | 7.08 | — | entry signal |
| 2026-11-25T21:00 | RSI momentum · 1h | sell | SOL-USD | 3.55 | -0.01 | rebalance down |
| 2026-11-25T21:00 | RSI momentum · 1h | sell | DOGE-USD | 3.53 | -0.01 | rebalance down |
| 2026-11-25T21:00 | MACD zero-line · 1h | buy | XRP-USD | 15.84 | — | entry signal |
| 2026-11-25T20:55 | Agent (ML meta-label) | buy | SQQQ | 14.06 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |
| 2026-11-25T20:55 | Agent (aggressive) | sell | SQQQ | 37.46 | -0.91 | selected signal exited |
| 2026-11-25T20:55 | Agent | sell | SQQQ | 30.49 | -0.30 | selected signal exited |
| 2026-11-25T20:55 | Opening range 30m | sell | UPRO | 7.99 | 0.30 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | TQQQ | 8.18 | 0.49 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | TNA | 7.90 | 0.42 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | SPY | 7.76 | 0.07 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | QQQ | 7.82 | 0.12 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | PLTR | 7.90 | 0.30 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | META | 7.01 | 0.15 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | IWM | 7.73 | 0.11 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | ETHU | 7.92 | 0.30 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | COIN | 7.98 | 0.29 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | BITX | 7.91 | 0.44 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 15m | sell | UPRO | 5.26 | 0.20 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 15m | sell | TQQQ | 5.41 | 0.33 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 15m | sell | TNA | 5.22 | 0.27 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 15m | sell | TECL | 5.51 | 0.42 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 15m | sell | SPY | 5.13 | 0.04 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 15m | sell | SOXL | 5.79 | 0.71 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 15m | sell | QQQ | 5.16 | 0.08 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 15m | sell | PLTR | 5.22 | 0.23 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 23:40:05.000128+00:00 -> 2026-11-25 23:50:05.000128+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
