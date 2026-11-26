# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T00:09:05.000137+00:00 · 73620 ticks

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

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 28.04 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 150 decisions in 30 calls, $0.0021 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T00:09 | 2 / 2 / 1 | DOGE-USD 17% |  |
| Breezy | 2026-11-26T00:09 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T00:09 | 5 / 0 / 0 | BTC-USD 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| EMA 20/50 cross | TECL | 1.74 | +5.81% | 3 |
| Bollinger reversion · 1h | MSFT | 1.74 | +7.75% | 3 |
| Z-score reversion | SQQQ | 1.74 | +8.59% | 5 |
| EMA 20/50 cross | TQQQ | 1.64 | +4.16% | 4 |
| OBV trend | COIN | 1.49 | +1.46% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.63 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.96 | 15.96 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.10 | 5.10 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.31 | 0.50 | -5.49 | 185 |
| 12 | Hold SPY | benchmark | 94.11 | -5.89 | 0 | — | -6.75 | -1.72 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.53 | -6.47 | 23 | 8.7 | -5.32 | -7.82 | -6.57 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.32 | -6.68 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.16 | -6.84 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.57 | -8.43 | 116 | 24.1 | -7.45 | -4.36 | -10.99 | 34 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.20 | -10.80 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.11 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.82 | -14.18 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.88 | -2.37 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.14 | -16.86 | 77 | 19.5 | -19.66 | -6.69 | -19.85 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.30 | -6.13 | -13.46 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.22 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.76 | -23.24 | 173 | 28.9 | -22.12 | -8.82 | -22.55 | 70 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.25 | -24.75 | 210 | 27.6 | -35.24 | -8.56 | -35.72 | 184 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.48 | -7.76 | -29.49 | 74 |
| 32 | Max aggression: 5-day momentum | meta | 74.02 | -25.98 | 27 | 37.0 | -56.74 | -3.00 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.59 | -26.41 | 141 | 24.8 | -26.46 | -6.45 | -26.74 | 143 |
| 34 | Ichimoku · 1h | trend | 73.31 | -26.69 | 114 | 15.8 | -29.88 | -7.58 | -30.60 | 99 |
| 35 | Daily: Momentum burst | daily | 71.07 | -28.93 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.79 | -30.21 | 264 | 18.9 | -37.61 | -7.06 | -38.44 | 288 |
| 37 | Hold BTC | benchmark | 69.75 | -30.25 | 3 | 0.0 | -29.00 | -5.12 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.06 | -31.94 | 209 | 22.5 | -31.46 | -8.11 | -31.80 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.86 | -32.15 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 66.79 | -33.21 | 221 | 17.6 | -40.64 | -8.07 | -42.30 | 211 |
| 41 | Stochastic reversion · 1h | reversion | 66.67 | -33.33 | 411 | 39.9 | -32.92 | -3.42 | -42.70 | 440 |
| 42 | OBV trend · 1h | momentum | 66.44 | -33.56 | 325 | 19.7 | -42.14 | -10.35 | -42.36 | 224 |
| 43 | EMA 20/50 cross · 1h | trend | 65.90 | -34.10 | 126 | 9.5 | -37.99 | -10.46 | -38.21 | 112 |
| 44 | Triple EMA stack · 1h | trend | 65.10 | -34.91 | 172 | 15.1 | -42.79 | -10.48 | -43.30 | 171 |
| 45 | MACD zero-line · 1h | trend | 63.14 | -36.86 | 202 | 16.3 | -37.09 | -10.31 | -37.58 | 202 |
| 46 | MFI reversion · 1h | reversion | 62.63 | -37.37 | 518 | 32.4 | -31.87 | -4.66 | -38.15 | 198 |
| 47 | RSI momentum · 1h | momentum | 62.43 | -37.57 | 203 | 14.8 | -43.81 | -9.73 | -44.14 | 195 |
| 48 | Donchian 20/10 · 1h | breakout | 61.20 | -38.80 | 183 | 17.5 | -41.60 | -9.26 | -43.16 | 200 |
| 49 | Heikin-Ashi · 1h | trend | 60.85 | -39.15 | 547 | 21.9 | -49.59 | -10.15 | -50.18 | 641 |
| 50 | ROC + volume · 1h | momentum | 60.76 | -39.24 | 465 | 26.7 | -40.47 | -7.86 | -41.37 | 337 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.63 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.04 | -41.96 | 314 | 12.1 | -45.36 | -10.41 | -46.47 | 334 |
| 53 | MACD cross · 1h | trend | 57.23 | -42.77 | 492 | 20.3 | -54.12 | -10.96 | -55.74 | 512 |
| 54 | Agent (ML meta-label) | meta | 56.25 | -43.75 | 2074 | 25.4 | -23.86 | -3.13 | -30.34 | 337 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.14 | -8.97 | -55.53 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -4.96 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 50.99 | -49.01 | 1086 | 21.5 | -61.42 | -13.37 | -62.15 | 1188 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.51 | -9.24 | -58.86 | 693 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.38 | -9.38 | -59.58 | 608 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -46.60 | -99.16 | 5367 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.57 | -31.40 | -84.47 | 1427 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.22 | -45.76 | -94.39 | 2394 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.38 | -30.13 | -91.09 | 1882 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.40 | -39.15 | -91.78 | 2214 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.61 | -26.76 | -88.64 | 1915 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -46.62 | -98.23 | 3412 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.83 | -49.87 | -96.91 | 3343 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.81 | -34.41 | -92.81 | 2061 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.14 | -34.85 | -82.32 | 1505 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -53.20 | -99.70 | 6282 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -36.96 | -93.18 | 2472 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.08 | -34.68 | -94.08 | 3126 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -62.33 | -99.82 | 6070 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.92 | -41.24 | -93.22 | 2252 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.88 | -19.35 | -52.24 | 662 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.55 | -22.73 | -78.57 | 1602 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -55.04 | -97.71 | 3233 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.20 | -58.37 | -99.22 | 5131 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.32 | -22.31 | -70.94 | 1198 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -45.21 | -94.71 | 2651 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.44 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.08 | -33.40 | -84.46 | 1640 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -67.97 | -99.77 | 6529 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.58 | -30.65 | -91.97 | 2498 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.89 | -20.00 | -83.42 | 1968 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.72 | -32.85 | -92.03 | 2169 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -47.45 | -98.22 | 4056 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.28 | -45.52 | -90.70 | 2191 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.98 | -22.62 | -67.70 | 779 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.66 | -27.49 | -73.38 | 1150 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.76 | -19.19 | -85.02 | 1825 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -48.14 | -98.12 | 4399 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -88.20 | -99.94 | 8281 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.10 | -6.77 | -52.53 | 291 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 00:09:05.000137+00:00 -> 2026-11-26 00:19:05.000137+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
