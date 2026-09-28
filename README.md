# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T23:40:05.000136+00:00 · 5064 ticks

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

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 29709 decisions in 1594 calls, $0.3557 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T23:40 | 2 / 1 / 2 | DOGE-USD 20%, ETH-USD 14% |  |
| Breezy | 2026-09-28T23:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-28T23:40 | 4 / 1 / 0 | DOGE-USD 40%, ETH-USD 40% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.63 | +2.51% | 11 |
| Stochastic reversion | COIN | 2.50 | +5.60% | 9 |
| Williams %R | ETHU | 2.33 | +8.38% | 17 |
| CCI reversion | AMD | 2.13 | +3.17% | 10 |
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
| 10 | Hold BTC | benchmark | 99.77 | -0.23 | 0 | — | 30.17 | 3.83 | -8.68 | 1 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 99.66 | -0.34 | 0 | — | -1.17 | -0.44 | -7.65 | 1 |
| 12 | Copy: Congress Democrats (NANC) | copy | 99.65 | -0.35 | 0 | — | 8.06 | 3.10 | -3.62 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.62 | -0.38 | 2 | 100.0 | 15.23 | 3.21 | -6.57 | 138 |
| 14 | Hold SPY | benchmark | 99.44 | -0.56 | 0 | — | 4.05 | 2.11 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.23 | -4.73 | 191 |
| 17 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.79 | -5.16 | 28 |
| 18 | Daily: Bullish score | daily | 99.15 | -0.85 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 19 | Connors RSI(2) · 1h | reversion | 99.04 | -0.96 | 39 | 48.7 | -11.80 | -3.76 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.00 | -1.00 | 0 | — | -3.63 | -2.25 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.99 | -1.01 | 0 | — | -7.89 | -1.95 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.89 | -1.11 | 0 | — | -1.97 | -0.92 | -5.14 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 98.80 | -1.20 | 23 | 56.5 | -12.41 | -2.77 | -14.07 | 324 |
| 24 | Z-score reversion · 1h | reversion | 98.74 | -1.26 | 4 | 25.0 | 3.53 | 0.89 | -8.60 | 155 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | Williams %R · 1h | reversion | 98.65 | -1.35 | 29 | 51.7 | -18.37 | -3.41 | -20.33 | 488 |
| 27 | CCI reversion · 1h | reversion | 98.53 | -1.47 | 23 | 34.8 | 1.60 | 0.44 | -12.41 | 409 |
| 28 | Copy: Insider buying | copy | 98.49 | -1.51 | 2 | 100.0 | -12.69 | -2.46 | -17.74 | 73 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.88 | -2.78 | -11.75 | 233 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.61 | -13.54 | 562 |
| 32 | Squeeze breakout · 1h | breakout | 98.00 | -2.00 | 7 | 14.3 | 16.09 | 2.85 | -6.26 | 94 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 98.00 | -2.00 | 0 | — | 25.09 | 3.65 | -6.29 | 1 |
| 34 | Candlestick reversal · 1h | reversion | 97.90 | -2.10 | 12 | 16.7 | -25.61 | -6.02 | -26.58 | 489 |
| 35 | EMA 20/50 cross · 1h | trend | 97.81 | -2.19 | 8 | 12.5 | 15.68 | 1.89 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.81 | -2.19 | 11 | 9.1 | 4.11 | 0.76 | -16.43 | 196 |
| 37 | MACD cross · 1h | trend | 97.64 | -2.36 | 27 | 11.1 | -15.45 | -2.62 | -20.54 | 454 |
| 38 | Bollinger reversion · 1h | reversion | 97.25 | -2.75 | 19 | 31.6 | -17.59 | -4.92 | -17.85 | 308 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.77 | -16.14 | 692 |
| 40 | Donchian 55/20 · 1h | breakout | 97.17 | -2.83 | 8 | 0.0 | 4.42 | 0.79 | -16.96 | 113 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.06 | -2.94 | 0 | — | -11.60 | -2.43 | -15.27 | 2 |
| 42 | Parabolic SAR · 1h | trend | 97.06 | -2.94 | 19 | 15.8 | -5.62 | -0.65 | -18.82 | 301 |
| 43 | Agent (ML meta-label) | meta | 97.00 | -3.00 | 79 | 10.1 | 1.50 | 0.44 | -11.05 | 379 |
| 44 | Trend pullback · 1h | trend | 96.99 | -3.01 | 22 | 13.6 | -26.02 | -6.98 | -26.61 | 149 |
| 45 | MACD zero-line · 1h | trend | 96.97 | -3.03 | 14 | 7.1 | -3.22 | -0.27 | -14.90 | 222 |
| 46 | Bollinger breakout · 1h | breakout | 96.80 | -3.20 | 13 | 7.7 | 13.27 | 1.90 | -9.85 | 284 |
| 47 | RSI momentum · 1h | momentum | 96.41 | -3.59 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Three white soldiers | momentum | 96.28 | -3.71 | 31 | 12.9 | -51.60 | -28.72 | -51.60 | 619 |
| 49 | EMA 9/21 cross · 1h | trend | 96.13 | -3.87 | 33 | 12.1 | 3.36 | 0.66 | -16.92 | 311 |
| 50 | Triple EMA stack · 1h | trend | 95.93 | -4.07 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 51 | Ichimoku · 1h | trend | 95.90 | -4.10 | 11 | 9.1 | 8.17 | 1.15 | -15.13 | 119 |
| 52 | ADX DI cross · 1h | trend | 95.83 | -4.17 | 25 | 8.0 | -11.80 | -2.23 | -15.42 | 249 |
| 53 | Donchian 20/10 · 1h | breakout | 95.76 | -4.24 | 12 | 16.7 | 12.05 | 1.71 | -12.78 | 213 |
| 54 | Max aggression: 5-day momentum | meta | 95.74 | -4.26 | 1 | 0.0 | -0.63 | 0.30 | -29.56 | 29 |
| 55 | MFI reversion · 1h | reversion | 95.59 | -4.41 | 38 | 13.2 | -9.79 | -1.82 | -17.20 | 126 |
| 56 | Max aggression: 1-day momentum | meta | 95.49 | -4.51 | 1 | 0.0 | -32.05 | -1.81 | -49.41 | 42 |
| 57 | OBV trend · 1h | momentum | 95.40 | -4.60 | 47 | 6.4 | -10.10 | -1.08 | -25.24 | 319 |
| 58 | VWAP momentum · 1h | momentum | 95.28 | -4.72 | 80 | 6.2 | -33.19 | -4.97 | -33.83 | 1249 |
| 59 | Volume breakout · 1h | breakout | 95.15 | -4.85 | 25 | 4.0 | 6.26 | 1.06 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.10 | -4.90 | 7 | 0.0 | -0.52 | 0.14 | -18.68 | 221 |
| 61 | Heikin-Ashi · 1h | trend | 94.31 | -5.69 | 35 | 11.4 | -22.62 | -3.40 | -29.24 | 678 |
| 62 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 63 | AI bee: Bizzy ⏸ | ai | 93.85 | -6.15 | 171 | 15.8 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 93.14 | -6.86 | 86 | 36.0 | -70.74 | -21.87 | -71.14 | 1467 |
| 65 | ROC + volume · 1h | momentum | 91.96 | -8.04 | 43 | 7.0 | -3.95 | -0.35 | -17.40 | 403 |
| 66 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.83 | -18.91 | -59.90 | 1179 |
| 67 | ROC + volume | momentum | 89.49 | -10.51 | 112 | 17.0 | -71.93 | -18.09 | -72.35 | 1656 |
| 68 | Volume breakout | breakout | 88.86 | -11.14 | 75 | 9.3 | -62.39 | -20.78 | -62.39 | 906 |
| 69 | Donchian 55/20 | breakout | 88.82 | -11.18 | 76 | 11.8 | -68.74 | -16.10 | -68.76 | 1331 |
| 70 | EMA 20/50 cross | trend | 88.77 | -11.23 | 89 | 14.6 | -78.78 | -17.90 | -78.87 | 1483 |
| 71 | Keltner breakout | breakout | 87.83 | -12.17 | 117 | 10.3 | -84.94 | -36.17 | -84.95 | 1929 |
| 72 | Ichimoku | trend | 87.76 | -12.24 | 84 | 8.3 | -80.46 | -26.87 | -80.54 | 1757 |
| 73 | Z-score reversion | reversion | 86.66 | -13.34 | 142 | 29.6 | -84.58 | -28.85 | -84.70 | 2085 |
| 74 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -70.56 | -17.08 | -71.75 | 1410 |
| 75 | MACD zero-line | trend | 85.15 | -14.85 | 149 | 16.1 | -91.53 | -37.08 | -91.64 | 2368 |
| 76 | Supertrend | trend | 84.64 | -15.36 | 137 | 16.1 | -87.44 | -25.47 | -87.47 | 1969 |
| 77 | Bollinger breakout | breakout | 84.64 | -15.36 | 153 | 15.0 | -93.92 | -43.66 | -93.93 | 2874 |
| 78 | RSI momentum | momentum | 84.53 | -15.47 | 140 | 11.4 | -90.28 | -30.45 | -90.35 | 2398 |
| 79 | Triple EMA stack | trend | 84.00 | -16.00 | 163 | 14.1 | -92.95 | -37.78 | -92.98 | 2623 |
| 80 | Trend pullback | trend | 83.54 | -16.46 | 138 | 15.9 | -90.58 | -35.08 | -90.59 | 2283 |
| 81 | Donchian 20/10 | breakout | 83.39 | -16.61 | 154 | 15.6 | -90.89 | -30.85 | -90.91 | 2686 |
| 82 | ADX DI cross | trend | 82.75 | -17.25 | 154 | 7.1 | -89.41 | -50.17 | -89.44 | 2130 |
| 83 | MFI reversion | reversion | 82.34 | -17.66 | 151 | 16.6 | -87.86 | -36.66 | -87.91 | 2175 |
| 84 | Connors RSI(2) | reversion | 81.72 | -18.28 | 196 | 17.3 | -96.40 | -43.62 | -96.40 | 3649 |
| 85 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.35 | -54.61 | -99.36 | 5560 |
| 86 | Stochastic reversion ⏸ | reversion | 80.66 | -19.34 | 245 | 24.5 | -95.88 | -49.60 | -95.89 | 4055 |
| 87 | OBV trend | momentum | 79.75 | -20.25 | 212 | 13.2 | -95.79 | -52.40 | -95.79 | 3558 |
| 88 | EMA 9/21 cross | trend | 79.74 | -20.26 | 215 | 14.0 | -97.41 | -44.51 | -97.41 | 3551 |
| 89 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.87 | -31.86 | -94.87 | 2674 |
| 90 | Bollinger reversion ⏸ | reversion | 79.09 | -20.91 | 233 | 13.3 | -95.74 | -47.40 | -95.75 | 3676 |
| 91 | VWAP momentum ⏸ | momentum | 78.10 | -21.90 | 277 | 9.7 | -98.47 | -37.50 | -98.47 | 5207 |
| 92 | Parabolic SAR | trend | 77.42 | -22.58 | 224 | 12.5 | -96.92 | -61.41 | -96.93 | 3651 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.47 | -55.81 | -98.47 | 4703 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -74.11 | -99.70 | 6093 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.52 | -66.71 | -99.52 | 6089 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.89 | -104.26 | -99.89 | 8321 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T23:40 | RSI momentum | buy | XRP-USD | 4.22 | — | rebalance up |
| 2026-09-28T23:35 | MACD zero-line | buy | DOGE-USD | 4.26 | — | rebalance up |
| 2026-09-28T23:35 | MACD zero-line | sell | BTC-USD | 4.26 | -0.03 | rebalance down |
| 2026-09-28T23:30 | Three white soldiers | buy | BTC-USD | 24.10 | — | entry signal |
| 2026-09-28T23:30 | MACD zero-line | buy | DOGE-USD | 4.26 | — | rebalance up |
| 2026-09-28T23:30 | MACD zero-line | sell | SOL-USD | 4.26 | -0.02 | rebalance down |
| 2026-09-28T23:20 | MFI reversion | sell | SOL-USD | 20.65 | 0.07 | exit signal |
| 2026-09-28T23:20 | MFI reversion | sell | ETH-USD | 20.55 | -0.01 | exit signal |
| 2026-09-28T23:20 | MFI reversion | sell | DOGE-USD | 20.62 | 0.06 | exit signal |
| 2026-09-28T23:20 | MACD zero-line | buy | DOGE-USD | 4.30 | — | entry signal |
| 2026-09-28T23:20 | MACD zero-line | sell | ETH-USD | 4.29 | -0.02 | rebalance down |
| 2026-09-28T23:15 | Consensus | sell | ETH-USD | 19.75 | -0.14 | target is flat |
| 2026-09-28T23:15 | MFI reversion | sell | BTC-USD | 20.47 | -0.09 | exit signal |
| 2026-09-28T23:15 | Three white soldiers | sell | BTC-USD | 23.98 | -0.14 | exit signal |
| 2026-09-28T23:15 | RSI momentum | sell | BTC-USD | 4.22 | -0.03 | rebalance down |
| 2026-09-28T23:15 | ROC + volume | buy | SOL-USD | 22.34 | — | entry signal |
| 2026-09-28T23:10 | Consensus | buy | ETH-USD | 19.90 | — | entry |
| 2026-09-28T23:10 | OBV trend | buy | ETH-USD | 19.95 | — | entry signal |
| 2026-09-28T23:10 | ROC + volume | buy | DOGE-USD | 22.38 | — | entry signal |
| 2026-09-28T23:10 | Triple EMA stack | buy | ETH-USD | 21.01 | — | entry signal |
| 2026-09-28T23:10 | EMA 20/50 cross | buy | ETH-USD | 22.21 | — | entry signal |
| 2026-09-28T23:05 | Z-score reversion | sell | DOGE-USD | 21.70 | 0.08 | exit signal |
| 2026-09-28T23:05 | RSI(14) reversion | sell | DOGE-USD | 23.35 | 0.09 | take-profit |
| 2026-09-28T23:05 | Keltner breakout | buy | SOL-USD | 22.00 | — | entry signal |
| 2026-09-28T23:05 | Keltner breakout | buy | ETH-USD | 22.00 | — | entry signal |
| 2026-09-28T23:05 | Bollinger breakout | buy | XRP-USD | 21.22 | — | entry signal |
| 2026-09-28T23:05 | Bollinger breakout | buy | SOL-USD | 21.22 | — | entry signal |
| 2026-09-28T23:05 | Bollinger breakout | buy | ETH-USD | 21.22 | — | entry signal |
| 2026-09-28T23:05 | Donchian 20/10 | buy | XRP-USD | 20.91 | — | entry signal |
| 2026-09-28T23:05 | Donchian 20/10 | buy | SOL-USD | 20.91 | — | entry signal |
| 2026-09-28T23:05 | Donchian 20/10 | buy | BTC-USD | 20.91 | — | entry signal |
| 2026-09-28T23:05 | RSI momentum | buy | XRP-USD | 12.75 | — | entry signal |
| 2026-09-28T23:05 | RSI momentum | buy | SOL-USD | 16.95 | — | entry signal |
| 2026-09-28T23:05 | RSI momentum | buy | DOGE-USD | 16.95 | — | entry signal |
| 2026-09-28T23:05 | RSI momentum | sell | ETH-USD | 4.23 | -0.01 | rebalance down |
| 2026-09-28T23:05 | ROC + volume | buy | ETH-USD | 22.40 | — | entry signal |
| 2026-09-28T23:05 | Ichimoku | buy | XRP-USD | 21.97 | — | entry signal |
| 2026-09-28T23:05 | ADX DI cross | buy | DOGE-USD | 4.13 | — | rebalance up |
| 2026-09-28T23:05 | ADX DI cross | sell | SOL-USD | 4.13 | -0.01 | rebalance down |
| 2026-09-28T23:05 | Supertrend | sell | SOL-USD | 4.23 | -0.01 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
