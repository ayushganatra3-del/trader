# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T14:35:05.000147+00:00 · 74345 ticks

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
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 28.29 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 10782 decisions in 2157 calls, $0.1504 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T14:35 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-26T14:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T14:35 | 3 / 2 / 0 | ETH-USD 55% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.92 | 15.92 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.07 | 5.07 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.30 | 0.49 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.08 | -5.92 | 0 | — | -6.75 | -1.72 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.57 | -6.43 | 24 | 12.5 | -5.29 | -7.77 | -6.57 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.29 | -6.71 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.13 | -6.87 | 63 | 41.3 | -4.98 | -0.83 | -14.79 | 73 |
| 16 | Trend pullback · 1h | trend | 91.56 | -8.44 | 116 | 24.1 | -7.30 | -4.43 | -10.74 | 31 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.17 | -10.83 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.11 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.82 | -14.18 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -12.87 | -2.37 | -20.49 | 156 |
| 23 | Squeeze breakout · 1h | breakout | 83.66 | -16.34 | 77 | 19.5 | -19.13 | -6.44 | -19.85 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.99 | -20.01 | 222 | 41.0 | -13.28 | -6.11 | -13.46 | 60 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.22 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.82 | -23.18 | 174 | 29.3 | -22.18 | -8.79 | -22.46 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.24 | -6.09 | -27.61 | 195 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.54 | -24.46 | 211 | 28.0 | -34.40 | -8.31 | -35.15 | 182 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 73.99 | -26.01 | 27 | 37.0 | -54.97 | -2.83 | -67.33 | 22 |
| 33 | Keltner breakout · 1h | breakout | 73.65 | -26.35 | 141 | 24.8 | -26.40 | -6.43 | -26.75 | 145 |
| 34 | Ichimoku · 1h | trend | 73.31 | -26.70 | 114 | 15.8 | -28.79 | -7.26 | -29.63 | 95 |
| 35 | Daily: Momentum burst | daily | 71.06 | -28.94 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.28 | -29.72 | 3 | 0.0 | -27.38 | -4.75 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 70.19 | -29.81 | 264 | 18.9 | -36.76 | -6.82 | -38.08 | 286 |
| 38 | Bollinger breakout · 1h | breakout | 68.94 | -31.06 | 209 | 22.5 | -30.39 | -7.66 | -31.80 | 206 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.83 | -32.17 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.05 | -32.95 | 221 | 17.6 | -40.15 | -7.92 | -42.12 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.65 | -33.35 | 411 | 39.9 | -32.92 | -3.43 | -42.70 | 438 |
| 42 | OBV trend · 1h | momentum | 66.42 | -33.58 | 325 | 19.7 | -40.50 | -9.99 | -40.85 | 223 |
| 43 | EMA 20/50 cross · 1h | trend | 65.91 | -34.09 | 126 | 9.5 | -37.97 | -10.29 | -38.47 | 117 |
| 44 | Triple EMA stack · 1h | trend | 65.01 | -34.99 | 172 | 15.1 | -41.02 | -10.10 | -41.47 | 169 |
| 45 | MACD zero-line · 1h | trend | 63.31 | -36.69 | 203 | 16.3 | -37.06 | -10.21 | -37.75 | 202 |
| 46 | RSI momentum · 1h | momentum | 62.93 | -37.07 | 203 | 14.8 | -42.65 | -9.30 | -43.57 | 192 |
| 47 | MFI reversion · 1h | reversion | 62.66 | -37.34 | 520 | 32.7 | -32.25 | -4.75 | -38.15 | 193 |
| 48 | Donchian 20/10 · 1h | breakout | 61.34 | -38.66 | 183 | 17.5 | -40.83 | -8.99 | -42.84 | 199 |
| 49 | ROC + volume · 1h | momentum | 61.12 | -38.88 | 466 | 26.8 | -39.95 | -7.69 | -41.16 | 335 |
| 50 | Heikin-Ashi · 1h | trend | 60.81 | -39.19 | 553 | 21.9 | -49.36 | -10.07 | -49.85 | 641 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.63 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.40 | -41.60 | 314 | 12.1 | -45.02 | -10.23 | -46.46 | 331 |
| 53 | MACD cross · 1h | trend | 57.39 | -42.61 | 494 | 20.6 | -53.88 | -10.86 | -55.65 | 511 |
| 54 | Agent (ML meta-label) | meta | 56.24 | -43.76 | 2074 | 25.4 | -22.18 | -2.91 | -29.86 | 332 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.09 | -8.96 | -55.56 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -4.96 | -45.50 | 430 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.21 | -9.19 | -58.58 | 691 |
| 58 | VWAP momentum · 1h | momentum | 50.80 | -49.20 | 1102 | 21.5 | -61.20 | -13.41 | -61.58 | 1193 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.22 | -9.34 | -59.57 | 606 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -48.45 | -99.16 | 5400 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.53 | -31.38 | -83.98 | 1425 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.26 | -46.96 | -94.27 | 2400 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.31 | -30.06 | -90.72 | 1882 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.56 | -40.21 | -91.56 | 2224 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.58 | -27.09 | -88.58 | 1923 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -47.80 | -98.17 | 3413 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -51.23 | -96.84 | 3348 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.25 | -35.51 | -93.25 | 2098 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.13 | -35.60 | -82.15 | 1509 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -51.80 | -99.68 | 6277 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.94 | -37.65 | -93.02 | 2472 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.29 | -35.24 | -94.29 | 3143 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -63.84 | -99.81 | 6072 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.06 | -43.00 | -93.14 | 2260 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.34 | -18.92 | -51.64 | 658 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.14 | -23.64 | -78.25 | 1606 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -56.04 | -97.70 | 3232 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -56.50 | -99.17 | 5114 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.99 | -22.83 | -70.32 | 1196 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -47.62 | -94.64 | 2657 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.44 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.43 | -34.54 | -84.44 | 1645 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -66.81 | -99.77 | 6519 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.47 | -30.25 | -91.80 | 2491 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.82 | -19.87 | -83.36 | 1970 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.46 | -31.61 | -91.86 | 2155 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -47.05 | -98.22 | 4048 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.27 | -46.16 | -90.49 | 2191 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.00 | -29.24 | -68.04 | 780 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.79 | -27.85 | -72.79 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.63 | -18.97 | -85.02 | 1824 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -48.64 | -98.12 | 4401 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -100.17 | -99.94 | 8288 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.20 | -7.05 | -52.53 | 297 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T14:00 | ROC + volume · 1h | buy | SOL-USD | 1.44 | — | rebalance up |
| 2026-11-26T14:00 | ROC + volume · 1h | buy | ETH-USD | 5.40 | — | rebalance up |
| 2026-11-26T14:00 | ROC + volume · 1h | sell | XRP-USD | 6.83 | 0.15 | exit signal |
| 2026-11-26T14:00 | VWAP momentum · 1h | buy | SOL-USD | 2.03 | — | entry signal |
| 2026-11-26T14:00 | Heikin-Ashi · 1h | buy | ETH-USD | 2.76 | — | entry signal |
| 2026-11-26T13:00 | MACD zero-line · 1h | buy | DOGE-USD | 7.97 | — | entry |
| 2026-11-26T13:00 | MACD zero-line · 1h | sell | XRP-USD | 7.97 | 0.04 | exit signal |
| 2026-11-26T13:00 | MACD cross · 1h | sell | XRP-USD | 2.52 | 0.06 | exit signal |
| 2026-11-26T12:00 | VWAP momentum · 1h | buy | ETH-USD | 2.12 | — | entry signal |
| 2026-11-26T12:00 | VWAP momentum · 1h | buy | DOGE-USD | 2.12 | — | entry signal |
| 2026-11-26T12:00 | MACD cross · 1h | sell | SOL-USD | 2.49 | 0.07 | exit signal |
| 2026-11-26T11:00 | VWAP momentum · 1h | sell | SOL-USD | 1.93 | -0.03 | exit signal |
| 2026-11-26T11:00 | VWAP momentum · 1h | sell | ETH-USD | 1.94 | -0.02 | exit signal |
| 2026-11-26T11:00 | VWAP momentum · 1h | sell | BTC-USD | 1.93 | -0.03 | exit signal |
| 2026-11-26T11:00 | Parabolic SAR · 1h | sell | XRP-USD | 9.59 | 0.20 | exit signal |
| 2026-11-26T10:05 | VWAP momentum · 1h | sell | DOGE-USD | 1.95 | -0.01 | target is flat |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | SOL-USD | 1.96 | — | entry signal |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | ETH-USD | 1.96 | — | entry signal |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | DOGE-USD | 1.96 | — | entry signal |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | BTC-USD | 1.96 | — | entry signal |
| 2026-11-26T09:00 | VWAP reversion · 1h | sell | ETH-USD | 21.18 | 0.01 | exit signal |
| 2026-11-26T09:00 | Connors RSI(2) · 1h | sell | DOGE-USD | 20.01 | 0.02 | exit signal |
| 2026-11-26T08:00 | VWAP reversion · 1h | buy | ETH-USD | 21.17 | — | entry signal |
| 2026-11-26T07:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 19.99 | — | entry signal |
| 2026-11-26T07:00 | Three white soldiers · 1h | sell | DOGE-USD | 18.80 | 0.21 | exit signal |
| 2026-11-26T07:00 | Volume breakout · 1h | sell | DOGE-USD | 19.21 | 0.08 | exit signal |
| 2026-11-26T07:00 | VWAP momentum · 1h | sell | XRP-USD | 1.95 | -0.01 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | XRP-USD | 2.40 | -0.03 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | SOL-USD | 2.43 | -0.00 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | BTC-USD | 2.43 | -0.01 | exit signal |
| 2026-11-26T07:00 | Triple EMA stack · 1h | buy | ETH-USD | 5.33 | — | entry signal |
| 2026-11-26T07:00 | Triple EMA stack · 1h | sell | DOGE-USD | 5.33 | -0.06 | rebalance down |
| 2026-11-26T06:25 | VWAP momentum · 1h | sell | DOGE-USD | 2.11 | -0.01 | target is flat |
| 2026-11-26T06:25 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.42 | -0.01 | target is flat |
| 2026-11-26T06:20 | VWAP momentum · 1h | buy | DOGE-USD | 2.12 | — | entry |
| 2026-11-26T06:20 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.43 | — | entry |
| 2026-11-26T06:05 | VWAP momentum · 1h | sell | DOGE-USD | 1.95 | -0.02 | target is flat |
| 2026-11-26T06:05 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.44 | 0.01 | target is flat |
| 2026-11-26T06:00 | VWAP momentum · 1h | sell | SOL-USD | 1.94 | -0.02 | exit signal |
| 2026-11-26T06:00 | VWAP momentum · 1h | sell | BTC-USD | 1.95 | -0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 14:35:05.000147+00:00 -> 2026-11-26 14:45:05.000147+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
