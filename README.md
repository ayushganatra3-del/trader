# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T12:05:05.000176+00:00 · 74209 ticks

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

Today: 8745 decisions in 1749 calls, $0.1220 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T12:05 | 4 / 1 / 0 | SOL-USD 16%, DOGE-USD 15% |  |
| Breezy | 2026-11-26T12:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T12:05 | 5 / 0 / 0 | ETH-USD 72% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.99 | 15.99 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.13 | 5.13 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.31 | 0.50 | -5.49 | 185 |
| 12 | Hold SPY | benchmark | 94.13 | -5.87 | 0 | — | -6.75 | -1.72 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.61 | -6.39 | 24 | 12.5 | -5.29 | -7.77 | -6.57 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.35 | -6.65 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.18 | -6.82 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.58 | -8.42 | 116 | 24.1 | -7.10 | -4.52 | -10.42 | 29 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.22 | -10.78 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.11 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.83 | -14.17 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -12.87 | -2.37 | -20.49 | 156 |
| 23 | Squeeze breakout · 1h | breakout | 83.77 | -16.23 | 77 | 19.5 | -19.35 | -6.49 | -20.11 | 80 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.99 | -20.01 | 222 | 41.0 | -13.28 | -6.11 | -13.46 | 60 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.22 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.83 | -23.17 | 174 | 29.3 | -22.21 | -8.80 | -22.48 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.54 | -24.45 | 211 | 28.0 | -34.43 | -8.32 | -35.15 | 182 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 74.04 | -25.96 | 27 | 37.0 | -56.74 | -3.00 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.67 | -26.33 | 141 | 24.8 | -25.96 | -6.31 | -26.32 | 143 |
| 34 | Ichimoku · 1h | trend | 73.32 | -26.68 | 114 | 15.8 | -28.79 | -7.26 | -29.63 | 95 |
| 35 | Daily: Momentum burst | daily | 71.07 | -28.93 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.31 | -29.69 | 3 | 0.0 | -28.22 | -4.94 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 70.22 | -29.78 | 264 | 18.9 | -37.13 | -6.91 | -38.33 | 288 |
| 38 | Bollinger breakout · 1h | breakout | 68.95 | -31.05 | 209 | 22.5 | -30.59 | -7.74 | -31.81 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.87 | -32.12 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.05 | -32.95 | 221 | 17.6 | -40.18 | -7.93 | -42.06 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.68 | -33.32 | 411 | 39.9 | -33.08 | -3.45 | -42.70 | 438 |
| 42 | OBV trend · 1h | momentum | 66.46 | -33.54 | 325 | 19.7 | -40.60 | -10.07 | -40.93 | 224 |
| 43 | EMA 20/50 cross · 1h | trend | 65.93 | -34.07 | 126 | 9.5 | -37.83 | -10.30 | -38.32 | 117 |
| 44 | Triple EMA stack · 1h | trend | 65.04 | -34.96 | 172 | 15.1 | -40.80 | -10.10 | -41.22 | 168 |
| 45 | MACD zero-line · 1h | trend | 63.38 | -36.62 | 202 | 16.3 | -36.85 | -10.14 | -37.70 | 202 |
| 46 | RSI momentum · 1h | momentum | 62.93 | -37.07 | 203 | 14.8 | -42.86 | -9.38 | -43.62 | 193 |
| 47 | MFI reversion · 1h | reversion | 62.69 | -37.31 | 520 | 32.7 | -32.55 | -4.81 | -38.15 | 194 |
| 48 | Donchian 20/10 · 1h | breakout | 61.39 | -38.61 | 183 | 17.5 | -40.88 | -9.01 | -42.86 | 199 |
| 49 | ROC + volume · 1h | momentum | 61.19 | -38.81 | 465 | 26.7 | -39.94 | -7.68 | -41.19 | 335 |
| 50 | Heikin-Ashi · 1h | trend | 60.82 | -39.18 | 553 | 21.9 | -49.35 | -10.07 | -49.85 | 640 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.63 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.42 | -41.58 | 314 | 12.1 | -44.91 | -10.22 | -46.34 | 332 |
| 53 | MACD cross · 1h | trend | 57.44 | -42.56 | 493 | 20.5 | -54.01 | -10.89 | -55.77 | 514 |
| 54 | Agent (ML meta-label) | meta | 56.26 | -43.74 | 2074 | 25.4 | -19.10 | -2.29 | -26.98 | 330 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.26 | -9.00 | -55.64 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -4.96 | -45.50 | 430 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.43 | -9.25 | -58.79 | 692 |
| 58 | VWAP momentum · 1h | momentum | 50.82 | -49.18 | 1102 | 21.5 | -61.56 | -13.50 | -61.93 | 1196 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.34 | -9.37 | -59.57 | 606 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -48.30 | -99.15 | 5390 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.64 | -31.70 | -84.09 | 1426 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.25 | -46.79 | -94.26 | 2397 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.38 | -30.38 | -90.82 | 1885 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.51 | -40.21 | -91.54 | 2223 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.45 | -26.86 | -88.48 | 1914 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -47.82 | -98.19 | 3415 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -51.17 | -96.85 | 3344 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.31 | -35.92 | -93.32 | 2102 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.22 | -35.70 | -82.23 | 1514 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -53.19 | -99.69 | 6286 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.92 | -37.56 | -93.02 | 2471 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.26 | -35.22 | -94.26 | 3139 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -64.11 | -99.81 | 6073 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.02 | -42.52 | -93.18 | 2259 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.34 | -18.92 | -51.64 | 658 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.93 | -23.52 | -78.23 | 1604 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -55.46 | -97.69 | 3230 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -58.47 | -99.18 | 5120 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.99 | -22.82 | -70.32 | 1194 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -47.21 | -94.58 | 2652 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.44 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.33 | -34.42 | -84.34 | 1643 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -68.75 | -99.77 | 6521 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.46 | -30.18 | -91.80 | 2492 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.95 | -20.06 | -83.43 | 1972 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.56 | -32.21 | -91.87 | 2158 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -48.00 | -98.23 | 4055 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.32 | -46.71 | -90.51 | 2193 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.87 | -29.25 | -67.90 | 779 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.64 | -27.58 | -72.70 | 1150 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.75 | -19.15 | -85.04 | 1826 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.11 | -48.82 | -98.11 | 4401 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -99.31 | -99.94 | 8285 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.83 | -7.19 | -52.53 | 298 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-26T05:00 | MFI reversion · 1h | sell | SOL-USD | 4.81 | 0.18 | exit signal |
| 2026-11-26T05:00 | VWAP momentum · 1h | buy | SOL-USD | 1.96 | — | entry signal |
| 2026-11-26T05:00 | VWAP momentum · 1h | buy | BTC-USD | 1.96 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | buy | SOL-USD | 6.49 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | buy | BTC-USD | 13.04 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | sell | XRP-USD | 3.30 | 0.00 | rebalance down |
| 2026-11-26T04:00 | VWAP momentum · 1h | sell | SOL-USD | 1.95 | -0.01 | exit signal |
| 2026-11-26T04:00 | Heikin-Ashi · 1h | buy | XRP-USD | 2.44 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 12:05:05.000176+00:00 -> 2026-11-26 12:15:05.000176+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
