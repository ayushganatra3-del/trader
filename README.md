# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T23:10:05.000119+00:00 · 73570 ticks

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

Today: 42270 decisions in 3534 calls, $0.5227 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T23:10 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-25T23:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-25T23:10 | 1 / 2 / 2 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.95 | 15.95 | 0 | — | 14.88 | 5.04 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.12 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.09 | 5.09 | 0 | — | 6.08 | 1.63 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.09 | 0.06 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.11 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.33 | 0.51 | -5.49 | 177 |
| 12 | Hold SPY | benchmark | 94.10 | -5.90 | 0 | — | -6.75 | -1.74 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.46 | -6.54 | 23 | 8.7 | -5.37 | -7.88 | -6.57 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.32 | -6.68 | 0 | — | -7.99 | -1.62 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.15 | -6.85 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.57 | -8.43 | 116 | 24.1 | -7.45 | -4.39 | -10.99 | 34 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.65 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.19 | -10.81 | 0 | — | -12.17 | -2.66 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.19 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.14 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.82 | -14.18 | 20 | 20.0 | -13.31 | -2.96 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.79 | -2.38 | -20.49 | 155 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.01 | -16.99 | 77 | 19.5 | -19.78 | -6.80 | -19.85 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.30 | -6.18 | -13.46 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.80 | -5.26 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.69 | -23.31 | 173 | 28.9 | -22.08 | -9.36 | -22.45 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.15 | -6.11 | -27.61 | 195 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.72 | -4.61 | -18.54 | 92 |
| 30 | Parabolic SAR · 1h | trend | 75.19 | -24.82 | 210 | 27.6 | -35.68 | -8.73 | -36.09 | 185 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.48 | -7.83 | -29.49 | 74 |
| 32 | Max aggression: 5-day momentum | meta | 74.01 | -25.99 | 27 | 37.0 | -56.74 | -3.02 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.59 | -26.41 | 141 | 24.8 | -26.46 | -6.50 | -26.74 | 143 |
| 34 | Ichimoku · 1h | trend | 73.31 | -26.69 | 114 | 15.8 | -29.88 | -7.64 | -30.60 | 99 |
| 35 | Daily: Momentum burst | daily | 71.07 | -28.93 | 31 | 16.1 | -33.19 | -4.59 | -35.97 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.69 | -30.32 | 264 | 18.9 | -37.59 | -7.11 | -38.33 | 287 |
| 37 | Hold BTC | benchmark | 69.40 | -30.60 | 3 | 0.0 | -29.29 | -5.24 | -36.10 | 1 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 67.85 | -32.15 | 3 | 0.0 | -25.48 | -3.18 | -33.66 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 67.83 | -32.17 | 209 | 22.5 | -31.68 | -8.22 | -31.80 | 207 |
| 40 | Supertrend · 1h | trend | 66.75 | -33.26 | 221 | 17.6 | -40.91 | -8.19 | -42.48 | 212 |
| 41 | Stochastic reversion · 1h | reversion | 66.66 | -33.34 | 411 | 39.9 | -32.84 | -3.45 | -42.70 | 440 |
| 42 | OBV trend · 1h | momentum | 66.44 | -33.56 | 325 | 19.7 | -41.23 | -10.14 | -42.35 | 225 |
| 43 | EMA 20/50 cross · 1h | trend | 65.90 | -34.10 | 126 | 9.5 | -38.23 | -10.66 | -38.45 | 113 |
| 44 | Triple EMA stack · 1h | trend | 65.09 | -34.91 | 172 | 15.1 | -42.79 | -10.59 | -43.30 | 171 |
| 45 | MACD zero-line · 1h | trend | 63.08 | -36.92 | 202 | 16.3 | -37.38 | -10.49 | -37.57 | 203 |
| 46 | MFI reversion · 1h | reversion | 62.60 | -37.40 | 518 | 32.4 | -32.72 | -4.88 | -38.34 | 201 |
| 47 | RSI momentum · 1h | momentum | 62.31 | -37.69 | 203 | 14.8 | -43.98 | -9.82 | -44.18 | 195 |
| 48 | Donchian 20/10 · 1h | breakout | 61.17 | -38.83 | 183 | 17.5 | -41.65 | -9.36 | -43.16 | 200 |
| 49 | Heikin-Ashi · 1h ⏸ | trend | 60.88 | -39.12 | 547 | 21.9 | -49.73 | -10.27 | -50.29 | 642 |
| 50 | ROC + volume · 1h | momentum | 60.64 | -39.36 | 465 | 26.7 | -40.03 | -7.85 | -40.83 | 337 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.66 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 57.97 | -42.03 | 314 | 12.1 | -45.45 | -10.52 | -46.48 | 334 |
| 53 | MACD cross · 1h | trend | 57.17 | -42.83 | 492 | 20.3 | -54.14 | -11.08 | -55.73 | 512 |
| 54 | Agent (ML meta-label) | meta | 56.25 | -43.75 | 2074 | 25.4 | -21.98 | -2.72 | -30.68 | 331 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.12 | -9.05 | -55.51 | 502 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -5.01 | -45.50 | 430 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.09 | -9.16 | -58.75 | 685 |
| 58 | VWAP momentum · 1h | momentum | 50.92 | -49.09 | 1086 | 21.5 | -60.90 | -13.50 | -61.61 | 1187 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.62 | -9.55 | -59.58 | 609 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -49.63 | -99.17 | 5356 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.59 | -32.47 | -84.46 | 1427 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.21 | -48.32 | -94.39 | 2391 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.49 | -31.41 | -91.13 | 1884 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -40.43 | -91.75 | 2209 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.65 | -27.45 | -88.68 | 1915 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.16 | -49.37 | -98.23 | 3407 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -52.34 | -96.89 | 3321 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.84 | -35.40 | -92.84 | 2057 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.09 | -35.94 | -82.30 | 1502 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -57.80 | -99.70 | 6293 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.02 | -38.31 | -93.24 | 2474 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.09 | -35.94 | -94.09 | 3125 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.11 | -99.82 | 6071 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.94 | -43.21 | -93.22 | 2253 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.62 | -19.09 | -52.05 | 662 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.71 | -23.14 | -78.72 | 1595 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -59.43 | -97.70 | 3229 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.97 | -99.22 | 5134 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.28 | -22.66 | -70.92 | 1197 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -47.34 | -94.74 | 2650 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.50 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.29 | -34.81 | -84.63 | 1646 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -77.35 | -99.77 | 6531 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.59 | -31.63 | -91.97 | 2502 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.91 | -20.36 | -83.44 | 1970 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.08 | -34.83 | -92.31 | 2172 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.22 | -50.71 | -98.23 | 4059 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.36 | -47.92 | -90.77 | 2193 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.30 | -23.97 | -68.08 | 777 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.69 | -28.23 | -73.36 | 1150 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.90 | -19.56 | -85.16 | 1831 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -51.32 | -98.12 | 4399 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.42 | -99.94 | 8279 |
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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 23:10:05.000119+00:00 -> 2026-11-25 23:20:05.000119+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
