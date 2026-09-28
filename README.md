# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T23:10:05.000159+00:00 · 5041 ticks

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

Today: 29364 decisions in 1525 calls, $0.3509 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T23:10 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-09-28T23:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-28T23:10 | 4 / 1 / 0 | ETH-USD 29%, DOGE-USD 25% |  |

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
| 11 | Hold BTC | benchmark | 99.64 | -0.36 | 0 | — | 30.16 | 3.82 | -8.68 | 1 |
| 12 | Copy: Congress Democrats (NANC) | copy | 99.64 | -0.36 | 0 | — | 8.06 | 3.10 | -3.62 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.56 | -0.44 | 2 | 100.0 | 15.16 | 3.20 | -6.57 | 138 |
| 14 | Hold SPY | benchmark | 99.43 | -0.57 | 0 | — | 4.05 | 2.11 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 17 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.44 | -5.16 | 27 |
| 18 | Daily: Bullish score | daily | 99.15 | -0.85 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 19 | Connors RSI(2) · 1h | reversion | 99.04 | -0.96 | 39 | 48.7 | -11.80 | -3.76 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 98.99 | -1.01 | 0 | — | -3.63 | -2.25 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.98 | -1.02 | 0 | — | -7.89 | -1.95 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.89 | -1.11 | 0 | — | -1.97 | -0.92 | -5.14 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 98.79 | -1.22 | 23 | 56.5 | -12.42 | -2.77 | -14.06 | 324 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 25 | Z-score reversion · 1h | reversion | 98.67 | -1.33 | 4 | 25.0 | 3.47 | 0.88 | -8.60 | 155 |
| 26 | Williams %R · 1h | reversion | 98.63 | -1.37 | 29 | 51.7 | -18.14 | -3.36 | -20.10 | 487 |
| 27 | CCI reversion · 1h | reversion | 98.49 | -1.51 | 23 | 34.8 | 1.58 | 0.44 | -12.41 | 409 |
| 28 | Copy: Insider buying | copy | 98.49 | -1.51 | 2 | 100.0 | -12.69 | -2.46 | -17.74 | 73 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -8.05 | -2.85 | -11.75 | 232 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.61 | -13.54 | 562 |
| 32 | Squeeze breakout · 1h | breakout | 98.00 | -2.00 | 7 | 14.3 | 15.85 | 2.81 | -6.26 | 95 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 97.99 | -2.01 | 0 | — | 25.09 | 3.65 | -6.29 | 1 |
| 34 | Candlestick reversal · 1h | reversion | 97.89 | -2.11 | 12 | 16.7 | -25.61 | -6.02 | -26.58 | 489 |
| 35 | EMA 20/50 cross · 1h | trend | 97.81 | -2.19 | 8 | 12.5 | 15.68 | 1.89 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.78 | -2.22 | 11 | 9.1 | 4.83 | 0.85 | -16.43 | 195 |
| 37 | MACD cross · 1h | trend | 97.57 | -2.42 | 27 | 11.1 | -15.50 | -2.63 | -20.54 | 454 |
| 38 | Bollinger reversion · 1h | reversion | 97.24 | -2.76 | 19 | 31.6 | -17.59 | -4.92 | -17.85 | 308 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.76 | -16.14 | 692 |
| 40 | Donchian 55/20 · 1h | breakout | 97.16 | -2.84 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.05 | -2.95 | 0 | — | -11.60 | -2.43 | -15.27 | 2 |
| 42 | Parabolic SAR · 1h | trend | 97.04 | -2.96 | 19 | 15.8 | -5.63 | -0.65 | -18.82 | 301 |
| 43 | Agent (ML meta-label) | meta | 96.99 | -3.01 | 79 | 10.1 | 2.40 | 0.60 | -10.59 | 384 |
| 44 | Trend pullback · 1h | trend | 96.99 | -3.01 | 22 | 13.6 | -26.02 | -6.98 | -26.61 | 149 |
| 45 | MACD zero-line · 1h | trend | 96.95 | -3.05 | 14 | 7.1 | -3.24 | -0.27 | -14.90 | 222 |
| 46 | Bollinger breakout · 1h | breakout | 96.80 | -3.20 | 13 | 7.7 | 13.27 | 1.90 | -9.85 | 284 |
| 47 | Three white soldiers | momentum | 96.41 | -3.59 | 30 | 13.3 | -51.53 | -28.70 | -51.56 | 618 |
| 48 | RSI momentum · 1h | momentum | 96.41 | -3.59 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 49 | EMA 9/21 cross · 1h | trend | 96.11 | -3.89 | 33 | 12.1 | 3.34 | 0.66 | -16.92 | 311 |
| 50 | Triple EMA stack · 1h | trend | 95.92 | -4.08 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 51 | Ichimoku · 1h | trend | 95.90 | -4.11 | 11 | 9.1 | 8.17 | 1.15 | -15.13 | 119 |
| 52 | ADX DI cross · 1h | trend | 95.82 | -4.17 | 25 | 8.0 | -11.92 | -2.26 | -15.42 | 250 |
| 53 | Donchian 20/10 · 1h | breakout | 95.75 | -4.25 | 12 | 16.7 | 12.05 | 1.71 | -12.78 | 213 |
| 54 | Max aggression: 5-day momentum | meta | 95.64 | -4.36 | 1 | 0.0 | -0.72 | 0.29 | -29.56 | 29 |
| 55 | MFI reversion · 1h | reversion | 95.57 | -4.43 | 38 | 13.2 | -9.80 | -1.82 | -17.20 | 126 |
| 56 | Max aggression: 1-day momentum | meta | 95.48 | -4.52 | 1 | 0.0 | -32.05 | -1.81 | -49.41 | 42 |
| 57 | OBV trend · 1h | momentum | 95.40 | -4.60 | 47 | 6.4 | -10.10 | -1.08 | -25.24 | 319 |
| 58 | VWAP momentum · 1h | momentum | 95.26 | -4.74 | 80 | 6.2 | -33.17 | -4.97 | -33.83 | 1249 |
| 59 | Volume breakout · 1h | breakout | 95.14 | -4.86 | 25 | 4.0 | 6.26 | 1.06 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.09 | -4.91 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 94.30 | -5.70 | 35 | 11.4 | -22.62 | -3.40 | -29.24 | 678 |
| 62 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 63 | AI bee: Bizzy ⏸ | ai | 93.85 | -6.15 | 171 | 15.8 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 93.14 | -6.86 | 86 | 36.0 | -70.73 | -21.87 | -71.12 | 1466 |
| 65 | ROC + volume · 1h | momentum | 91.94 | -8.06 | 43 | 7.0 | -3.98 | -0.36 | -17.40 | 403 |
| 66 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.84 | -18.92 | -59.92 | 1179 |
| 67 | ROC + volume | momentum | 89.45 | -10.55 | 112 | 17.0 | -71.94 | -18.10 | -72.31 | 1655 |
| 68 | Volume breakout | breakout | 88.86 | -11.14 | 75 | 9.3 | -62.46 | -20.74 | -62.46 | 907 |
| 69 | Donchian 55/20 | breakout | 88.82 | -11.18 | 76 | 11.8 | -68.73 | -16.09 | -68.75 | 1331 |
| 70 | EMA 20/50 cross | trend | 88.76 | -11.24 | 89 | 14.6 | -78.76 | -17.90 | -78.84 | 1482 |
| 71 | Keltner breakout | breakout | 87.79 | -12.21 | 117 | 10.3 | -84.99 | -36.21 | -84.99 | 1930 |
| 72 | Ichimoku | trend | 87.75 | -12.25 | 84 | 8.3 | -80.48 | -26.84 | -80.55 | 1757 |
| 73 | Z-score reversion | reversion | 86.66 | -13.34 | 142 | 29.6 | -84.63 | -28.90 | -84.75 | 2086 |
| 74 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -70.70 | -17.15 | -71.87 | 1408 |
| 75 | MACD zero-line | trend | 85.15 | -14.85 | 149 | 16.1 | -91.53 | -37.08 | -91.63 | 2367 |
| 76 | Bollinger breakout | breakout | 84.59 | -15.41 | 153 | 15.0 | -93.94 | -43.77 | -93.94 | 2875 |
| 77 | Supertrend | trend | 84.55 | -15.45 | 137 | 16.1 | -87.40 | -25.47 | -87.41 | 1968 |
| 78 | RSI momentum | momentum | 84.47 | -15.53 | 140 | 11.4 | -90.29 | -30.46 | -90.35 | 2398 |
| 79 | Triple EMA stack | trend | 83.99 | -16.01 | 163 | 14.1 | -92.96 | -37.78 | -92.98 | 2623 |
| 80 | Trend pullback | trend | 83.54 | -16.46 | 138 | 15.9 | -90.59 | -35.06 | -90.60 | 2284 |
| 81 | Donchian 20/10 | breakout | 83.31 | -16.68 | 154 | 15.6 | -90.92 | -30.89 | -90.92 | 2687 |
| 82 | ADX DI cross | trend | 82.67 | -17.34 | 154 | 7.1 | -89.47 | -50.20 | -89.48 | 2133 |
| 83 | MFI reversion | reversion | 82.55 | -17.45 | 147 | 15.6 | -87.83 | -36.72 | -87.91 | 2175 |
| 84 | Connors RSI(2) | reversion | 81.72 | -18.28 | 196 | 17.3 | -96.41 | -43.60 | -96.41 | 3650 |
| 85 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.35 | -54.62 | -99.35 | 5558 |
| 86 | Stochastic reversion ⏸ | reversion | 80.66 | -19.34 | 245 | 24.5 | -95.88 | -49.60 | -95.89 | 4055 |
| 87 | OBV trend | momentum | 79.74 | -20.26 | 212 | 13.2 | -95.78 | -52.45 | -95.78 | 3557 |
| 88 | EMA 9/21 cross | trend | 79.66 | -20.34 | 215 | 14.0 | -97.42 | -44.57 | -97.42 | 3552 |
| 89 | Consensus | meta | 79.52 | -20.48 | 155 | 7.1 | -94.86 | -31.81 | -94.86 | 2674 |
| 90 | Bollinger reversion ⏸ | reversion | 79.09 | -20.91 | 233 | 13.3 | -95.74 | -47.40 | -95.75 | 3676 |
| 91 | VWAP momentum ⏸ | momentum | 78.10 | -21.90 | 277 | 9.7 | -98.48 | -37.43 | -98.48 | 5207 |
| 92 | Parabolic SAR | trend | 77.42 | -22.58 | 224 | 12.5 | -96.92 | -61.41 | -96.93 | 3651 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.47 | -55.79 | -98.47 | 4702 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -73.83 | -99.70 | 6093 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.52 | -66.70 | -99.52 | 6088 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.88 | -104.87 | -99.89 | 8317 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-09-28T23:05 | MACD zero-line | buy | XRP-USD | 21.37 | — | entry signal |
| 2026-09-28T23:05 | MACD zero-line | buy | SOL-USD | 21.37 | — | entry signal |
| 2026-09-28T23:05 | MACD zero-line | buy | BTC-USD | 21.37 | — | entry signal |
| 2026-09-28T23:05 | EMA 9/21 cross | buy | DOGE-USD | 8.04 | — | entry signal |
| 2026-09-28T23:05 | EMA 9/21 cross | sell | XRP-USD | 3.99 | -0.01 | rebalance down |
| 2026-09-28T23:05 | EMA 9/21 cross | sell | ETH-USD | 3.98 | -0.01 | rebalance down |
| 2026-09-28T23:00 | ADX DI cross · 1h | sell | ETH-USD | 24.02 | -0.12 | exit signal |
| 2026-09-28T23:00 | Z-score reversion | sell | SOL-USD | 21.65 | 0.03 | exit signal |
| 2026-09-28T23:00 | Donchian 20/10 | buy | ETH-USD | 20.92 | — | entry signal |
| 2026-09-28T23:00 | RSI momentum | buy | BTC-USD | 21.19 | — | entry signal |
| 2026-09-28T23:00 | EMA 9/21 cross | buy | SOL-USD | 19.93 | — | entry signal |
| 2026-09-28T22:56 | Supertrend | buy | XRP-USD | 8.44 | — | rebalance up |
| 2026-09-28T22:56 | Supertrend | sell | ETH-USD | 4.22 | -0.02 | rebalance down |
| 2026-09-28T22:56 | Supertrend | sell | BTC-USD | 4.22 | -0.02 | rebalance down |
| 2026-09-28T22:55 | Z-score reversion | sell | XRP-USD | 21.68 | -0.05 | exit signal |
| 2026-09-28T22:55 | Supertrend | buy | XRP-USD | 4.29 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
