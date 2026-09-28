# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T21:40:05.000176+00:00 · 4967 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.98 (-0.02%)

Closed trades 17, win rate 70.6%, fees £0.52, max drawdown -1.39%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-28 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.08 · VIX 16.19 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 28254 decisions in 1303 calls, $0.3354 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T21:40 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-09-28T21:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-28T21:40 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.63 | +2.51% | 11 |
| Stochastic reversion | COIN | 2.50 | +5.60% | 9 |
| Williams %R | ETHU | 2.33 | +8.38% | 17 |
| CCI reversion | AMD | 2.17 | +3.10% | 10 |
| Bollinger reversion | PLTR | 2.11 | +1.89% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.36 | 1.36 | 1 | 100.0 | 12.70 | 2.79 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.11 | -1.49 | 19 |
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.41 | 1.26 | -2.47 | 92 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.63 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.40 | -12.40 | 25 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.34 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -5.02 | -9.84 | 203 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.65 | -0.35 | 0 | — | -1.17 | -0.44 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.64 | -0.36 | 0 | — | 8.06 | 3.10 | -3.62 | 1 |
| 12 | Hold BTC | benchmark | 99.55 | -0.45 | 0 | — | 30.31 | 3.87 | -8.68 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.46 | -0.54 | 2 | 100.0 | 12.62 | 2.67 | -6.57 | 142 |
| 14 | Hold SPY | benchmark | 99.43 | -0.57 | 0 | — | 4.05 | 2.11 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 17 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.79 | -5.16 | 28 |
| 18 | Daily: Bullish score | daily | 99.14 | -0.85 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 19 | Connors RSI(2) · 1h | reversion | 99.04 | -0.96 | 39 | 48.7 | -11.80 | -3.76 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 98.99 | -1.01 | 0 | — | -3.63 | -2.25 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.98 | -1.02 | 0 | — | -7.89 | -1.95 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.88 | -1.12 | 0 | — | -1.97 | -0.92 | -5.14 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 24 | Stochastic reversion · 1h | reversion | 98.73 | -1.27 | 23 | 56.5 | -12.48 | -2.79 | -14.07 | 324 |
| 25 | Williams %R · 1h | reversion | 98.58 | -1.42 | 29 | 51.7 | -18.40 | -3.42 | -20.33 | 488 |
| 26 | Z-score reversion · 1h | reversion | 98.55 | -1.45 | 4 | 25.0 | 3.36 | 0.86 | -8.60 | 155 |
| 27 | Copy: Insider buying | copy | 98.49 | -1.51 | 2 | 100.0 | -12.69 | -2.46 | -17.74 | 73 |
| 28 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -8.05 | -2.85 | -11.75 | 232 |
| 29 | CCI reversion · 1h | reversion | 98.43 | -1.57 | 23 | 34.8 | -0.09 | 0.16 | -12.41 | 412 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.61 | -13.54 | 562 |
| 32 | Squeeze breakout · 1h | breakout | 98.00 | -2.00 | 7 | 14.3 | 16.09 | 2.85 | -6.26 | 94 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 97.99 | -2.01 | 0 | — | 25.09 | 3.65 | -6.29 | 1 |
| 34 | Candlestick reversal · 1h | reversion | 97.89 | -2.11 | 12 | 16.7 | -26.11 | -6.17 | -26.61 | 492 |
| 35 | EMA 20/50 cross · 1h | trend | 97.81 | -2.19 | 8 | 12.5 | 15.68 | 1.89 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.73 | -2.27 | 11 | 9.1 | 3.40 | 0.66 | -16.43 | 197 |
| 37 | MACD cross · 1h | trend | 97.45 | -2.55 | 27 | 11.1 | -15.67 | -2.66 | -20.78 | 455 |
| 38 | Bollinger reversion · 1h | reversion | 97.24 | -2.76 | 19 | 31.6 | -17.59 | -4.92 | -17.85 | 308 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.76 | -16.14 | 692 |
| 40 | Donchian 55/20 · 1h | breakout | 97.16 | -2.84 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.05 | -2.95 | 0 | — | -11.60 | -2.43 | -15.27 | 2 |
| 42 | Parabolic SAR · 1h | trend | 96.99 | -3.01 | 19 | 15.8 | -6.03 | -0.71 | -18.82 | 303 |
| 43 | Agent (ML meta-label) | meta | 96.99 | -3.01 | 79 | 10.1 | 3.58 | 0.80 | -12.69 | 400 |
| 44 | Trend pullback · 1h | trend | 96.99 | -3.01 | 22 | 13.6 | -26.48 | -7.10 | -27.11 | 151 |
| 45 | MACD zero-line · 1h | trend | 96.86 | -3.14 | 14 | 7.1 | -3.35 | -0.29 | -14.93 | 222 |
| 46 | Bollinger breakout · 1h | breakout | 96.79 | -3.21 | 13 | 7.7 | 13.27 | 1.90 | -9.85 | 284 |
| 47 | Three white soldiers | momentum | 96.49 | -3.51 | 30 | 13.3 | -51.64 | -28.63 | -51.77 | 620 |
| 48 | RSI momentum · 1h | momentum | 96.41 | -3.59 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 49 | EMA 9/21 cross · 1h | trend | 96.03 | -3.97 | 33 | 12.1 | 2.61 | 0.56 | -16.92 | 313 |
| 50 | Triple EMA stack · 1h | trend | 95.92 | -4.08 | 24 | 8.3 | -3.38 | -0.19 | -22.95 | 226 |
| 51 | Ichimoku · 1h | trend | 95.89 | -4.11 | 11 | 9.1 | 8.17 | 1.15 | -15.13 | 119 |
| 52 | ADX DI cross · 1h | trend | 95.83 | -4.17 | 24 | 8.3 | -12.03 | -2.28 | -15.77 | 251 |
| 53 | Donchian 20/10 · 1h | breakout | 95.75 | -4.25 | 12 | 16.7 | 12.05 | 1.71 | -12.78 | 213 |
| 54 | MFI reversion · 1h | reversion | 95.48 | -4.52 | 38 | 13.2 | -9.89 | -1.84 | -17.20 | 126 |
| 55 | Max aggression: 1-day momentum | meta | 95.48 | -4.52 | 1 | 0.0 | -32.05 | -1.81 | -49.41 | 42 |
| 56 | OBV trend · 1h | momentum | 95.40 | -4.60 | 47 | 6.4 | -10.88 | -1.18 | -25.24 | 321 |
| 57 | Max aggression: 5-day momentum | meta | 95.20 | -4.80 | 1 | 0.0 | -1.18 | 0.26 | -29.56 | 29 |
| 58 | VWAP momentum · 1h | momentum | 95.18 | -4.82 | 80 | 6.2 | -33.25 | -4.98 | -33.82 | 1249 |
| 59 | Volume breakout · 1h | breakout | 95.14 | -4.86 | 25 | 4.0 | 6.26 | 1.06 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.09 | -4.91 | 7 | 0.0 | -0.48 | 0.15 | -18.68 | 221 |
| 61 | Heikin-Ashi · 1h | trend | 94.30 | -5.70 | 35 | 11.4 | -22.62 | -3.40 | -29.24 | 678 |
| 62 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 63 | AI bee: Bizzy ⏸ | ai | 93.85 | -6.15 | 171 | 15.8 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 93.11 | -6.89 | 83 | 36.1 | -70.78 | -21.90 | -71.16 | 1468 |
| 65 | ROC + volume · 1h | momentum | 91.92 | -8.08 | 43 | 7.0 | -4.01 | -0.36 | -17.38 | 403 |
| 66 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.84 | -18.92 | -59.92 | 1179 |
| 67 | ROC + volume | momentum | 89.60 | -10.40 | 112 | 17.0 | -72.16 | -18.14 | -72.30 | 1658 |
| 68 | Volume breakout | breakout | 88.86 | -11.14 | 75 | 9.3 | -62.55 | -20.79 | -62.55 | 908 |
| 69 | Donchian 55/20 | breakout | 88.82 | -11.18 | 76 | 11.8 | -68.73 | -16.09 | -68.75 | 1331 |
| 70 | EMA 20/50 cross | trend | 88.82 | -11.18 | 89 | 14.6 | -78.85 | -17.91 | -78.86 | 1483 |
| 71 | Keltner breakout | breakout | 87.98 | -12.02 | 117 | 10.3 | -85.07 | -36.18 | -85.07 | 1933 |
| 72 | Ichimoku | trend | 87.87 | -12.13 | 84 | 8.3 | -80.53 | -26.87 | -80.53 | 1758 |
| 73 | Z-score reversion | reversion | 86.77 | -13.23 | 138 | 29.0 | -84.62 | -28.93 | -84.76 | 2085 |
| 74 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -70.98 | -17.14 | -71.87 | 1413 |
| 75 | MACD zero-line | trend | 85.50 | -14.51 | 149 | 16.1 | -91.50 | -36.98 | -91.59 | 2363 |
| 76 | Supertrend | trend | 84.97 | -15.04 | 135 | 16.3 | -87.46 | -25.50 | -87.48 | 1968 |
| 77 | Bollinger breakout | breakout | 84.90 | -15.10 | 153 | 15.0 | -93.92 | -43.64 | -93.92 | 2873 |
| 78 | RSI momentum | momentum | 84.81 | -15.19 | 140 | 11.4 | -90.33 | -30.47 | -90.33 | 2396 |
| 79 | Triple EMA stack | trend | 84.05 | -15.95 | 163 | 14.1 | -92.99 | -37.76 | -92.99 | 2624 |
| 80 | Donchian 20/10 | breakout | 83.84 | -16.16 | 152 | 15.8 | -90.92 | -30.78 | -90.92 | 2686 |
| 81 | Trend pullback | trend | 83.54 | -16.46 | 138 | 15.9 | -90.51 | -34.67 | -90.53 | 2280 |
| 82 | ADX DI cross | trend | 82.84 | -17.16 | 154 | 7.1 | -89.49 | -50.23 | -89.49 | 2131 |
| 83 | MFI reversion | reversion | 82.61 | -17.39 | 145 | 15.9 | -87.82 | -36.60 | -87.84 | 2174 |
| 84 | Connors RSI(2) | reversion | 82.27 | -17.73 | 192 | 17.7 | -96.38 | -43.46 | -96.38 | 3649 |
| 85 | Stochastic reversion | reversion | 81.19 | -18.81 | 241 | 24.9 | -95.86 | -49.88 | -95.86 | 4055 |
| 86 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.35 | -54.94 | -99.35 | 5555 |
| 87 | EMA 9/21 cross | trend | 79.88 | -20.12 | 215 | 14.0 | -97.43 | -44.53 | -97.43 | 3551 |
| 88 | OBV trend | momentum | 79.80 | -20.20 | 212 | 13.2 | -95.78 | -52.41 | -95.78 | 3556 |
| 89 | Consensus | meta | 79.58 | -20.42 | 155 | 7.1 | -95.00 | -32.40 | -95.00 | 2687 |
| 90 | Bollinger reversion ⏸ | reversion | 79.09 | -20.91 | 233 | 13.3 | -95.71 | -47.73 | -95.71 | 3671 |
| 91 | VWAP momentum ⏸ | momentum | 78.10 | -21.90 | 277 | 9.7 | -98.48 | -37.41 | -98.48 | 5208 |
| 92 | Parabolic SAR | trend | 77.42 | -22.58 | 224 | 12.5 | -96.93 | -61.53 | -96.93 | 3652 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.46 | -55.82 | -98.47 | 4702 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -74.09 | -99.70 | 6088 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.52 | -67.14 | -99.52 | 6087 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.89 | -105.32 | -99.89 | 8317 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T21:40 | MFI reversion | buy | BTC-USD | 20.67 | — | entry signal |
| 2026-09-28T21:40 | MACD zero-line | sell | ETH-USD | 21.24 | -0.18 | exit signal |
| 2026-09-28T21:35 | Stochastic reversion | buy | SOL-USD | 20.35 | — | entry signal |
| 2026-09-28T21:35 | Stochastic reversion | buy | DOGE-USD | 20.35 | — | entry signal |
| 2026-09-28T21:35 | EMA 9/21 cross | sell | ETH-USD | 19.93 | -0.19 | exit signal |
| 2026-09-28T21:30 | Connors RSI(2) | buy | ETH-USD | 20.59 | — | entry signal |
| 2026-09-28T21:25 | Connors RSI(2) | buy | DOGE-USD | 20.63 | — | entry signal |
| 2026-09-28T21:25 | Connors RSI(2) | buy | BTC-USD | 20.63 | — | entry signal |
| 2026-09-28T21:25 | Bollinger breakout | sell | XRP-USD | 21.03 | -0.26 | exit signal |
| 2026-09-28T21:25 | Donchian 20/10 | sell | DOGE-USD | 20.86 | -0.25 | stop-loss |
| 2026-09-28T21:20 | ADX DI cross | sell | XRP-USD | 20.55 | -0.22 | exit signal |
| 2026-09-28T21:20 | EMA 9/21 cross | sell | XRP-USD | 19.90 | -0.18 | exit signal |
| 2026-09-28T21:20 | EMA 9/21 cross | sell | DOGE-USD | 19.90 | -0.21 | exit signal |
| 2026-09-28T21:15 | MACD zero-line | buy | ETH-USD | 21.42 | — | entry signal |
| 2026-09-28T21:10 | EMA 9/21 cross | buy | XRP-USD | 20.07 | — | entry signal |
| 2026-09-28T21:05 | Stochastic reversion | sell | BTC-USD | 20.35 | -0.03 | exit signal |
| 2026-09-28T21:05 | RSI(14) reversion | sell | XRP-USD | 23.36 | 0.09 | exit signal |
| 2026-09-28T21:05 | RSI(14) reversion | sell | DOGE-USD | 23.36 | 0.10 | exit signal |
| 2026-09-28T21:05 | Bollinger breakout | buy | XRP-USD | 21.29 | — | entry signal |
| 2026-09-28T21:05 | Donchian 20/10 | buy | XRP-USD | 21.11 | — | entry signal |
| 2026-09-28T21:05 | Donchian 20/10 | buy | ETH-USD | 21.11 | — | entry signal |
| 2026-09-28T21:05 | Donchian 20/10 | buy | DOGE-USD | 21.11 | — | entry signal |
| 2026-09-28T21:05 | ADX DI cross | buy | XRP-USD | 20.77 | — | entry signal |
| 2026-09-28T21:05 | Supertrend | buy | ETH-USD | 21.34 | — | entry signal |
| 2026-09-28T21:05 | Supertrend | buy | DOGE-USD | 21.34 | — | entry signal |
| 2026-09-28T21:05 | EMA 9/21 cross | buy | ETH-USD | 20.11 | — | entry signal |
| 2026-09-28T21:05 | EMA 9/21 cross | buy | DOGE-USD | 20.11 | — | entry signal |
| 2026-09-28T21:00 | Connors RSI(2) | sell | DOGE-USD | 20.56 | -0.10 | exit signal |
| 2026-09-28T20:55 | Connors RSI(2) | buy | DOGE-USD | 20.65 | — | entry signal |
| 2026-09-28T20:45 | MFI reversion | buy | XRP-USD | 20.70 | — | entry signal |
| 2026-09-28T20:40 | MFI reversion | sell | ETH-USD | 20.60 | -0.04 | exit signal |
| 2026-09-28T20:40 | ADX DI cross | sell | DOGE-USD | 20.67 | -0.12 | exit signal |
| 2026-09-28T20:30 | ADX DI cross | buy | DOGE-USD | 20.80 | — | entry signal |
| 2026-09-28T20:25 | Stochastic reversion | sell | XRP-USD | 20.32 | -0.04 | exit signal |
| 2026-09-28T20:25 | Stochastic reversion | sell | DOGE-USD | 20.41 | 0.04 | exit signal |
| 2026-09-28T20:00 | Candlestick reversal · 1h | sell | XRP-USD | 10.80 | -0.26 | exit signal |
| 2026-09-28T20:00 | Candlestick reversal · 1h | sell | SOL-USD | 7.49 | -0.14 | exit signal |
| 2026-09-28T20:00 | VWAP momentum · 1h | buy | ETH-USD | 12.69 | — | rebalance up |
| 2026-09-28T20:00 | VWAP momentum · 1h | sell | XRP-USD | 3.12 | -0.08 | exit signal |
| 2026-09-28T20:00 | VWAP momentum · 1h | sell | SOL-USD | 6.29 | -0.12 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
