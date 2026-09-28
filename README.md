# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T22:40:05.000158+00:00 · 5012 ticks

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

Today: 28929 decisions in 1438 calls, $0.3449 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T22:40 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-09-28T22:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-28T22:40 | 5 / 0 / 0 | ETH-USD 36%, SOL-USD 30% |  |

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
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.30 | -2.47 | 91 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.63 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.40 | -12.40 | 25 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.34 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -5.02 | -9.84 | 203 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.65 | -0.35 | 0 | — | -1.17 | -0.44 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.64 | -0.36 | 0 | — | 8.06 | 3.10 | -3.62 | 1 |
| 12 | Hold BTC | benchmark | 99.57 | -0.43 | 0 | — | 30.41 | 3.88 | -8.68 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.43 | -0.57 | 2 | 100.0 | 14.72 | 3.12 | -6.57 | 136 |
| 14 | Hold SPY | benchmark | 99.43 | -0.57 | 0 | — | 4.05 | 2.11 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 17 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.79 | -5.16 | 28 |
| 18 | Daily: Bullish score | daily | 99.15 | -0.85 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 19 | Connors RSI(2) · 1h | reversion | 99.04 | -0.96 | 39 | 48.7 | -11.80 | -3.76 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 98.99 | -1.01 | 0 | — | -3.63 | -2.25 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.98 | -1.02 | 0 | — | -7.89 | -1.95 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.89 | -1.11 | 0 | — | -1.97 | -0.92 | -5.14 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 24 | Stochastic reversion · 1h | reversion | 98.74 | -1.26 | 23 | 56.5 | -12.48 | -2.78 | -14.07 | 324 |
| 25 | Williams %R · 1h | reversion | 98.59 | -1.41 | 29 | 51.7 | -18.36 | -3.41 | -20.30 | 488 |
| 26 | Z-score reversion · 1h | reversion | 98.53 | -1.47 | 4 | 25.0 | 3.34 | 0.85 | -8.60 | 155 |
| 27 | Copy: Insider buying | copy | 98.49 | -1.51 | 2 | 100.0 | -12.69 | -2.46 | -17.74 | 73 |
| 28 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -8.05 | -2.85 | -11.75 | 232 |
| 29 | CCI reversion · 1h | reversion | 98.42 | -1.58 | 23 | 34.8 | 1.52 | 0.43 | -12.41 | 409 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.61 | -13.54 | 562 |
| 32 | Squeeze breakout · 1h | breakout | 98.00 | -2.00 | 7 | 14.3 | 16.09 | 2.85 | -6.26 | 94 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 97.99 | -2.01 | 0 | — | 25.09 | 3.65 | -6.29 | 1 |
| 34 | Candlestick reversal · 1h | reversion | 97.89 | -2.11 | 12 | 16.7 | -25.69 | -6.10 | -25.98 | 484 |
| 35 | EMA 20/50 cross · 1h | trend | 97.81 | -2.19 | 8 | 12.5 | 15.65 | 1.88 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.75 | -2.25 | 11 | 9.1 | 4.05 | 0.75 | -16.43 | 196 |
| 37 | MACD cross · 1h | trend | 97.45 | -2.55 | 27 | 11.1 | -15.71 | -2.67 | -20.78 | 455 |
| 38 | Bollinger reversion · 1h | reversion | 97.24 | -2.76 | 19 | 31.6 | -17.61 | -4.93 | -17.88 | 308 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.76 | -16.14 | 692 |
| 40 | Donchian 55/20 · 1h | breakout | 97.16 | -2.84 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.05 | -2.95 | 0 | — | -11.60 | -2.43 | -15.27 | 2 |
| 42 | Parabolic SAR · 1h | trend | 97.01 | -2.99 | 19 | 15.8 | -6.01 | -0.70 | -18.82 | 303 |
| 43 | Agent (ML meta-label) | meta | 96.99 | -3.01 | 79 | 10.1 | 4.32 | 0.91 | -10.69 | 385 |
| 44 | Trend pullback · 1h | trend | 96.99 | -3.01 | 22 | 13.6 | -26.22 | -7.03 | -26.80 | 150 |
| 45 | MACD zero-line · 1h | trend | 96.89 | -3.11 | 14 | 7.1 | -3.21 | -0.27 | -14.64 | 220 |
| 46 | Bollinger breakout · 1h | breakout | 96.80 | -3.20 | 13 | 7.7 | 13.27 | 1.90 | -9.85 | 284 |
| 47 | Three white soldiers | momentum | 96.41 | -3.59 | 30 | 13.3 | -51.53 | -28.70 | -51.53 | 617 |
| 48 | RSI momentum · 1h | momentum | 96.41 | -3.59 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 49 | EMA 9/21 cross · 1h | trend | 96.06 | -3.94 | 33 | 12.1 | 2.98 | 0.61 | -16.92 | 312 |
| 50 | Triple EMA stack · 1h | trend | 95.92 | -4.08 | 24 | 8.3 | -2.85 | -0.13 | -22.95 | 223 |
| 51 | Ichimoku · 1h | trend | 95.90 | -4.11 | 11 | 9.1 | 8.17 | 1.15 | -15.13 | 119 |
| 52 | ADX DI cross · 1h | trend | 95.86 | -4.14 | 24 | 8.3 | -11.89 | -2.26 | -15.42 | 250 |
| 53 | Donchian 20/10 · 1h | breakout | 95.75 | -4.25 | 12 | 16.7 | 12.05 | 1.71 | -12.78 | 213 |
| 54 | MFI reversion · 1h | reversion | 95.49 | -4.51 | 38 | 13.2 | -9.88 | -1.84 | -17.20 | 126 |
| 55 | Max aggression: 1-day momentum | meta | 95.48 | -4.52 | 1 | 0.0 | -32.05 | -1.81 | -49.41 | 42 |
| 56 | OBV trend · 1h | momentum | 95.40 | -4.60 | 47 | 6.4 | -10.57 | -1.14 | -25.24 | 321 |
| 57 | Max aggression: 5-day momentum | meta | 95.24 | -4.76 | 1 | 0.0 | -1.14 | 0.26 | -29.56 | 29 |
| 58 | VWAP momentum · 1h | momentum | 95.21 | -4.79 | 80 | 6.2 | -33.23 | -4.98 | -33.83 | 1249 |
| 59 | Volume breakout · 1h | breakout | 95.14 | -4.86 | 25 | 4.0 | 6.26 | 1.06 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.09 | -4.91 | 7 | 0.0 | -0.48 | 0.15 | -18.68 | 221 |
| 61 | Heikin-Ashi · 1h | trend | 94.30 | -5.70 | 35 | 11.4 | -22.62 | -3.40 | -29.24 | 678 |
| 62 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 63 | AI bee: Bizzy ⏸ | ai | 93.85 | -6.15 | 171 | 15.8 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 93.17 | -6.83 | 83 | 36.1 | -70.75 | -21.89 | -71.14 | 1469 |
| 65 | ROC + volume · 1h | momentum | 91.92 | -8.08 | 43 | 7.0 | -4.00 | -0.36 | -17.40 | 403 |
| 66 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.84 | -18.92 | -59.92 | 1179 |
| 67 | ROC + volume | momentum | 89.60 | -10.40 | 112 | 17.0 | -71.99 | -18.10 | -72.30 | 1655 |
| 68 | Volume breakout | breakout | 88.86 | -11.14 | 75 | 9.3 | -62.46 | -20.74 | -62.46 | 907 |
| 69 | Donchian 55/20 | breakout | 88.82 | -11.18 | 76 | 11.8 | -68.73 | -16.09 | -68.75 | 1331 |
| 70 | EMA 20/50 cross | trend | 88.82 | -11.18 | 89 | 14.6 | -78.75 | -17.90 | -78.83 | 1481 |
| 71 | Keltner breakout | breakout | 87.98 | -12.02 | 117 | 10.3 | -85.05 | -36.18 | -85.05 | 1931 |
| 72 | Ichimoku | trend | 87.87 | -12.13 | 84 | 8.3 | -80.49 | -26.83 | -80.52 | 1757 |
| 73 | Z-score reversion | reversion | 86.64 | -13.36 | 139 | 28.8 | -84.63 | -28.90 | -84.75 | 2086 |
| 74 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -70.73 | -17.15 | -71.87 | 1408 |
| 75 | MACD zero-line | trend | 85.50 | -14.51 | 149 | 16.1 | -91.50 | -36.97 | -91.59 | 2363 |
| 76 | Bollinger breakout | breakout | 84.90 | -15.10 | 153 | 15.0 | -93.91 | -43.59 | -93.91 | 2872 |
| 77 | RSI momentum | momentum | 84.81 | -15.19 | 140 | 11.4 | -90.28 | -30.43 | -90.31 | 2394 |
| 78 | Supertrend | trend | 84.58 | -15.41 | 137 | 16.1 | -87.39 | -25.46 | -87.39 | 1965 |
| 79 | Triple EMA stack | trend | 84.05 | -15.95 | 163 | 14.1 | -93.01 | -37.74 | -93.01 | 2625 |
| 80 | Donchian 20/10 | breakout | 83.67 | -16.33 | 154 | 15.6 | -90.87 | -30.79 | -90.88 | 2683 |
| 81 | Trend pullback | trend | 83.54 | -16.46 | 138 | 15.9 | -90.54 | -34.83 | -90.55 | 2281 |
| 82 | ADX DI cross | trend | 82.72 | -17.28 | 154 | 7.1 | -89.36 | -50.04 | -89.36 | 2126 |
| 83 | MFI reversion | reversion | 82.32 | -17.68 | 147 | 15.6 | -87.86 | -36.66 | -87.91 | 2175 |
| 84 | Connors RSI(2) | reversion | 81.72 | -18.28 | 196 | 17.3 | -96.40 | -43.62 | -96.40 | 3649 |
| 85 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.35 | -54.62 | -99.36 | 5559 |
| 86 | Stochastic reversion ⏸ | reversion | 80.66 | -19.34 | 245 | 24.5 | -95.87 | -49.63 | -95.89 | 4055 |
| 87 | EMA 9/21 cross | trend | 79.88 | -20.12 | 215 | 14.0 | -97.40 | -44.43 | -97.40 | 3546 |
| 88 | OBV trend | momentum | 79.80 | -20.20 | 212 | 13.2 | -95.78 | -52.41 | -95.78 | 3556 |
| 89 | Consensus | meta | 79.58 | -20.42 | 155 | 7.1 | -94.78 | -31.53 | -94.78 | 2665 |
| 90 | Bollinger reversion ⏸ | reversion | 79.09 | -20.91 | 233 | 13.3 | -95.73 | -47.43 | -95.74 | 3676 |
| 91 | VWAP momentum ⏸ | momentum | 78.10 | -21.90 | 277 | 9.7 | -98.47 | -37.44 | -98.47 | 5205 |
| 92 | Parabolic SAR | trend | 77.42 | -22.58 | 224 | 12.5 | -96.92 | -61.41 | -96.93 | 3651 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.47 | -55.84 | -98.47 | 4703 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -73.99 | -99.70 | 6092 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.52 | -66.77 | -99.52 | 6088 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.89 | -104.83 | -99.89 | 8317 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T22:40 | Three white soldiers | buy | BTC-USD | 24.12 | — | entry signal |
| 2026-09-28T22:40 | ADX DI cross | buy | XRP-USD | 20.71 | — | entry signal |
| 2026-09-28T22:40 | ADX DI cross | buy | ETH-USD | 20.71 | — | entry signal |
| 2026-09-28T22:40 | Supertrend | buy | ETH-USD | 21.18 | — | entry signal |
| 2026-09-28T22:40 | Supertrend | buy | BTC-USD | 21.18 | — | entry signal |
| 2026-09-28T22:35 | MFI reversion | buy | DOGE-USD | 20.56 | — | entry signal |
| 2026-09-28T22:35 | MFI reversion | buy | BTC-USD | 20.56 | — | entry signal |
| 2026-09-28T22:30 | MFI reversion | buy | ETH-USD | 20.56 | — | entry signal |
| 2026-09-28T22:25 | MFI reversion | buy | SOL-USD | 20.58 | — | entry signal |
| 2026-09-28T22:20 | Z-score reversion | buy | SOL-USD | 21.62 | — | entry signal |
| 2026-09-28T22:20 | Z-score reversion | buy | DOGE-USD | 21.62 | — | entry signal |
| 2026-09-28T22:20 | Connors RSI(2) | sell | ETH-USD | 20.35 | -0.10 | exit signal |
| 2026-09-28T22:20 | RSI(14) reversion | buy | SOL-USD | 23.26 | — | entry signal |
| 2026-09-28T22:20 | RSI(14) reversion | buy | DOGE-USD | 23.26 | — | entry signal |
| 2026-09-28T22:10 | MFI reversion | sell | XRP-USD | 20.39 | -0.31 | stop-loss |
| 2026-09-28T22:10 | Z-score reversion | sell | SOL-USD | 21.46 | -0.30 | stop-loss |
| 2026-09-28T22:10 | Connors RSI(2) | buy | ETH-USD | 20.46 | — | entry signal |
| 2026-09-28T22:05 | Connors RSI(2) | sell | ETH-USD | 20.40 | -0.19 | stop-loss |
| 2026-09-28T22:05 | Connors RSI(2) | sell | DOGE-USD | 20.31 | -0.32 | stop-loss |
| 2026-09-28T22:05 | Supertrend | sell | ETH-USD | 21.07 | -0.27 | exit signal |
| 2026-09-28T22:02 | Stochastic reversion | sell | XRP-USD | 20.12 | -0.12 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-28T22:02 | Stochastic reversion | sell | DOGE-USD | 20.12 | -0.23 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-28T22:00 | MFI reversion | sell | BTC-USD | 20.49 | -0.17 | stop-loss |
| 2026-09-28T22:00 | Stochastic reversion | buy | XRP-USD | 20.24 | — | entry signal |
| 2026-09-28T22:00 | Stochastic reversion | sell | SOL-USD | 20.12 | -0.23 | stop-loss |
| 2026-09-28T22:00 | Stochastic reversion | sell | BTC-USD | 20.12 | -0.17 | stop-loss |
| 2026-09-28T22:00 | Connors RSI(2) | sell | BTC-USD | 20.45 | -0.18 | stop-loss |
| 2026-09-28T21:55 | Supertrend | sell | DOGE-USD | 20.97 | -0.37 | exit signal |
| 2026-09-28T21:50 | Stochastic reversion | buy | BTC-USD | 20.29 | — | entry signal |
| 2026-09-28T21:50 | Donchian 20/10 | sell | XRP-USD | 20.80 | -0.32 | stop-loss |
| 2026-09-28T21:50 | Donchian 20/10 | sell | ETH-USD | 20.90 | -0.22 | stop-loss |
| 2026-09-28T21:40 | MFI reversion | buy | BTC-USD | 20.67 | — | entry signal |
| 2026-09-28T21:40 | MACD zero-line | sell | ETH-USD | 21.24 | -0.18 | exit signal |
| 2026-09-28T21:35 | Stochastic reversion | buy | SOL-USD | 20.35 | — | entry signal |
| 2026-09-28T21:35 | Stochastic reversion | buy | DOGE-USD | 20.35 | — | entry signal |
| 2026-09-28T21:35 | EMA 9/21 cross | sell | ETH-USD | 19.93 | -0.19 | exit signal |
| 2026-09-28T21:30 | Connors RSI(2) | buy | ETH-USD | 20.59 | — | entry signal |
| 2026-09-28T21:25 | Connors RSI(2) | buy | DOGE-USD | 20.63 | — | entry signal |
| 2026-09-28T21:25 | Connors RSI(2) | buy | BTC-USD | 20.63 | — | entry signal |
| 2026-09-28T21:25 | Bollinger breakout | sell | XRP-USD | 21.03 | -0.26 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
