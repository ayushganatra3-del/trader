# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T02:35:05.000132+00:00 · 73731 ticks

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

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 28.29 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 1575 decisions in 315 calls, $0.0220 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T02:35 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-11-26T02:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T02:35 | 4 / 1 / 0 | ETH-USD 55% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.01 | 16.01 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.14 | 5.14 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.31 | 0.50 | -5.49 | 185 |
| 12 | Hold SPY | benchmark | 94.15 | -5.85 | 0 | — | -6.75 | -1.72 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.81 | -6.19 | 23 | 8.7 | -5.12 | -7.40 | -6.57 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.36 | -6.64 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.20 | -6.80 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.58 | -8.42 | 116 | 24.1 | -7.45 | -4.36 | -10.99 | 34 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.24 | -10.76 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.11 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.83 | -14.17 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.89 | -2.37 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.74 | -16.26 | 77 | 19.5 | -19.17 | -6.45 | -19.90 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.30 | -6.13 | -13.46 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.22 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 77.02 | -22.98 | 173 | 28.9 | -22.01 | -8.67 | -22.48 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.60 | -24.40 | 210 | 27.6 | -35.36 | -8.54 | -36.14 | 185 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 74.05 | -25.95 | 27 | 37.0 | -56.74 | -3.00 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.60 | -26.40 | 141 | 24.8 | -26.49 | -6.46 | -26.74 | 145 |
| 34 | Ichimoku · 1h | trend | 73.32 | -26.68 | 114 | 15.8 | -29.90 | -7.58 | -30.62 | 99 |
| 35 | Daily: Momentum burst | daily | 71.08 | -28.92 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.41 | -29.59 | 3 | 0.0 | -28.03 | -4.89 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 70.21 | -29.79 | 264 | 18.9 | -37.37 | -6.98 | -38.54 | 289 |
| 38 | Bollinger breakout · 1h | breakout | 68.92 | -31.08 | 209 | 22.5 | -30.62 | -7.75 | -31.80 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.88 | -32.12 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.05 | -32.95 | 221 | 17.6 | -40.18 | -7.93 | -42.12 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.69 | -33.31 | 411 | 39.9 | -32.92 | -3.43 | -42.70 | 438 |
| 42 | OBV trend · 1h | momentum | 66.47 | -33.53 | 325 | 19.7 | -42.43 | -10.41 | -42.60 | 227 |
| 43 | EMA 20/50 cross · 1h | trend | 65.90 | -34.10 | 126 | 9.5 | -37.84 | -10.42 | -38.01 | 113 |
| 44 | Triple EMA stack · 1h | trend | 65.10 | -34.90 | 172 | 15.1 | -43.23 | -10.53 | -43.32 | 173 |
| 45 | MACD zero-line · 1h | trend | 63.41 | -36.59 | 202 | 16.3 | -36.72 | -10.11 | -37.55 | 203 |
| 46 | RSI momentum · 1h | momentum | 62.93 | -37.07 | 203 | 14.8 | -43.36 | -9.54 | -44.17 | 195 |
| 47 | MFI reversion · 1h | reversion | 62.76 | -37.24 | 518 | 32.4 | -32.43 | -4.78 | -38.15 | 197 |
| 48 | Donchian 20/10 · 1h | breakout | 61.41 | -38.59 | 183 | 17.5 | -41.30 | -9.15 | -43.15 | 200 |
| 49 | ROC + volume · 1h | momentum | 61.17 | -38.83 | 465 | 26.7 | -39.96 | -7.69 | -41.19 | 335 |
| 50 | Heikin-Ashi · 1h | trend | 60.95 | -39.05 | 547 | 21.9 | -49.50 | -10.12 | -50.17 | 641 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.63 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.40 | -41.60 | 314 | 12.1 | -45.08 | -10.29 | -46.49 | 335 |
| 53 | MACD cross · 1h | trend | 57.44 | -42.56 | 492 | 20.3 | -53.92 | -10.89 | -55.68 | 513 |
| 54 | Agent (ML meta-label) | meta | 56.26 | -43.74 | 2074 | 25.4 | -19.06 | -2.38 | -28.04 | 332 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.11 | -8.96 | -55.49 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -4.96 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 51.01 | -48.99 | 1091 | 21.7 | -61.50 | -13.40 | -62.22 | 1193 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.75 | -9.06 | -58.29 | 688 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.31 | -9.36 | -59.57 | 607 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -47.02 | -99.19 | 5393 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.36 | -30.47 | -84.49 | 1427 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.15 | -44.45 | -94.39 | 2396 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.11 | -29.26 | -90.95 | 1881 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.23 | -38.01 | -91.75 | 2213 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.38 | -26.31 | -88.55 | 1914 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.13 | -45.50 | -98.22 | 3410 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.79 | -48.33 | -96.92 | 3345 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.94 | -34.77 | -92.95 | 2075 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.14 | -34.89 | -82.40 | 1514 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -52.91 | -99.70 | 6283 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.86 | -36.31 | -93.14 | 2473 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.11 | -34.80 | -94.11 | 3123 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -63.27 | -99.82 | 6076 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.97 | -41.70 | -93.23 | 2255 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.88 | -19.13 | -52.24 | 663 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.76 | -23.22 | -78.38 | 1607 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -54.53 | -97.72 | 3239 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -58.00 | -99.21 | 5123 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.42 | -23.08 | -70.83 | 1200 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -45.62 | -94.69 | 2654 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.44 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.21 | -34.13 | -84.50 | 1646 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -66.97 | -99.77 | 6525 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -30.62 | -91.96 | 2497 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.17 | -20.27 | -83.69 | 1973 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.70 | -32.78 | -92.01 | 2162 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.22 | -47.34 | -98.23 | 4051 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.22 | -44.79 | -90.70 | 2191 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.91 | -28.94 | -67.91 | 783 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.61 | -27.35 | -73.38 | 1153 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.79 | -19.23 | -85.02 | 1824 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.09 | -47.84 | -98.11 | 4396 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -92.27 | -99.94 | 8286 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.00 | -6.74 | -52.53 | 290 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-25T21:00 | Bollinger breakout · 1h | sell | SOL-USD | 3.41 | -0.01 | rebalance down |
| 2026-11-25T21:00 | Bollinger breakout · 1h | sell | ETH-USD | 3.40 | -0.01 | rebalance down |
| 2026-11-25T21:00 | RSI momentum · 1h | buy | BTC-USD | 7.08 | — | entry signal |
| 2026-11-25T21:00 | RSI momentum · 1h | sell | SOL-USD | 3.55 | -0.01 | rebalance down |
| 2026-11-25T21:00 | RSI momentum · 1h | sell | DOGE-USD | 3.53 | -0.01 | rebalance down |
| 2026-11-25T21:00 | MACD zero-line · 1h | buy | XRP-USD | 15.84 | — | entry signal |
| 2026-11-25T20:55 | Agent (ML meta-label) | buy | SQQQ | 14.06 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 02:35:05.000132+00:00 -> 2026-11-26 02:45:05.000132+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
