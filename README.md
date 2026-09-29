# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T13:10:05.000167+00:00 · 5726 ticks

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

Today: 9705 decisions in 1941 calls, $0.1356 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T13:10 | 2 / 2 / 1 | SOL-USD 16% |  |
| Breezy | 2026-09-29T13:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T13:10 | 5 / 0 / 0 | SOL-USD 41%, ETH-USD 40% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |
| CCI reversion | AMD | 2.04 | +3.07% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.36 | 1.36 | 1 | 100.0 | 12.70 | 2.77 | -7.55 | 43 |
| 2 | Hold BTC | benchmark | 100.88 | 0.88 | 0 | — | 31.17 | 3.89 | -8.68 | 1 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 11 | RSI(14) reversion · 1h | reversion | 99.94 | -0.06 | 4 | 100.0 | 12.45 | 2.57 | -6.57 | 142 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.73 | -0.27 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.72 | -0.28 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.51 | -0.48 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.88 | -4.39 | -14.73 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 17 | Daily: Bullish score | daily | 99.23 | -0.77 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Z-score reversion · 1h | reversion | 99.17 | -0.83 | 7 | 57.1 | 4.25 | 1.04 | -8.60 | 154 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Connors RSI(2) · 1h | reversion | 99.08 | -0.92 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 21 | Timing: Nasdaq FTD · QQQ | daily | 99.08 | -0.93 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 22 | Daily: SMA 20/50 cross · AAPL | daily | 99.06 | -0.94 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 99.06 | -0.94 | 25 | 56.0 | -12.37 | -2.74 | -13.84 | 324 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 98.97 | -1.03 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | CCI reversion · 1h | reversion | 98.61 | -1.39 | 28 | 42.9 | 1.57 | 0.43 | -12.41 | 405 |
| 27 | Williams %R · 1h | reversion | 98.60 | -1.40 | 33 | 51.5 | -17.95 | -3.30 | -19.54 | 485 |
| 28 | Copy: Insider buying | copy | 98.56 | -1.44 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.15 | -2.52 | -11.75 | 234 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.28 | -1.72 | 13 | 23.1 | -25.76 | -5.99 | -26.36 | 491 |
| 32 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 33 | Supertrend · 1h | trend | 98.17 | -1.82 | 11 | 9.1 | 5.72 | 0.96 | -16.43 | 195 |
| 34 | Squeeze breakout · 1h | breakout | 98.17 | -1.83 | 7 | 14.3 | 15.62 | 2.75 | -6.26 | 98 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 98.07 | -1.93 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 36 | MACD cross · 1h | trend | 97.96 | -2.04 | 31 | 9.7 | -15.31 | -2.57 | -20.56 | 459 |
| 37 | EMA 20/50 cross · 1h | trend | 97.95 | -2.05 | 8 | 12.5 | 15.83 | 1.89 | -14.36 | 126 |
| 38 | Max aggression: 5-day momentum | meta | 97.84 | -2.16 | 1 | 0.0 | 1.48 | 0.47 | -29.56 | 29 |
| 39 | MACD zero-line · 1h | trend | 97.44 | -2.56 | 15 | 6.7 | -2.31 | -0.13 | -14.64 | 222 |
| 40 | Bollinger reversion · 1h | reversion | 97.31 | -2.69 | 19 | 31.6 | -17.70 | -4.92 | -17.79 | 306 |
| 41 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 42 | Donchian 55/20 · 1h | breakout | 97.21 | -2.79 | 8 | 0.0 | 4.40 | 0.78 | -16.96 | 114 |
| 43 | Parabolic SAR · 1h | trend | 97.14 | -2.85 | 20 | 15.0 | -5.12 | -0.56 | -18.82 | 304 |
| 44 | Timing: Nasdaq FTD · TQQQ | daily | 97.13 | -2.87 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 45 | Agent (ML meta-label) | meta | 97.09 | -2.91 | 79 | 10.1 | 5.05 | 1.01 | -10.96 | 386 |
| 46 | Trend pullback · 1h | trend | 97.06 | -2.94 | 22 | 13.6 | -25.31 | -6.69 | -26.30 | 146 |
| 47 | Bollinger breakout · 1h | breakout | 97.04 | -2.96 | 13 | 7.7 | 13.49 | 1.91 | -9.85 | 286 |
| 48 | RSI momentum · 1h | momentum | 96.60 | -3.40 | 20 | 5.0 | 1.73 | 0.44 | -15.29 | 215 |
| 49 | Ichimoku · 1h | trend | 96.20 | -3.80 | 11 | 9.1 | 8.47 | 1.17 | -15.13 | 122 |
| 50 | ADX DI cross · 1h | trend | 96.17 | -3.83 | 25 | 8.0 | -11.19 | -2.08 | -15.39 | 250 |
| 51 | Triple EMA stack · 1h | trend | 96.17 | -3.83 | 24 | 8.3 | -2.59 | -0.09 | -22.95 | 224 |
| 52 | MFI reversion · 1h | reversion | 96.07 | -3.93 | 38 | 13.2 | -8.91 | -1.62 | -17.20 | 125 |
| 53 | EMA 9/21 cross · 1h | trend | 95.99 | -4.00 | 34 | 11.8 | 4.42 | 0.79 | -16.92 | 311 |
| 54 | Donchian 20/10 · 1h | breakout | 95.84 | -4.16 | 12 | 16.7 | 12.11 | 1.70 | -12.78 | 216 |
| 55 | OBV trend · 1h | momentum | 95.63 | -4.37 | 47 | 6.4 | -9.39 | -0.97 | -25.24 | 318 |
| 56 | VWAP momentum · 1h | momentum | 95.57 | -4.43 | 82 | 7.3 | -29.98 | -4.34 | -34.09 | 1243 |
| 57 | Max aggression: 1-day momentum | meta | 95.56 | -4.44 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 58 | Three white soldiers | momentum | 95.50 | -4.50 | 41 | 19.5 | -51.82 | -28.71 | -52.20 | 626 |
| 59 | Volume breakout · 1h | breakout | 95.14 | -4.86 | 25 | 4.0 | 6.23 | 1.04 | -12.60 | 127 |
| 60 | Heikin-Ashi · 1h | trend | 95.11 | -4.89 | 35 | 11.4 | -21.39 | -3.14 | -29.64 | 680 |
| 61 | Keltner breakout · 1h | breakout | 95.05 | -4.95 | 7 | 0.0 | -0.29 | 0.17 | -18.68 | 222 |
| 62 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.08 | -21.85 | -71.21 | 1471 |
| 63 | ROC + volume · 1h | momentum | 91.82 | -8.18 | 44 | 6.8 | -4.33 | -0.40 | -17.64 | 407 |
| 64 | Donchian 55/20 | breakout | 89.84 | -10.16 | 80 | 11.2 | -67.95 | -15.49 | -68.56 | 1332 |
| 65 | Squeeze breakout | breakout | 89.65 | -10.35 | 75 | 6.7 | -60.08 | -18.85 | -60.52 | 1188 |
| 66 | EMA 20/50 cross | trend | 89.13 | -10.87 | 97 | 13.4 | -78.56 | -17.47 | -79.35 | 1486 |
| 67 | ROC + volume | momentum | 89.02 | -10.98 | 123 | 17.1 | -71.89 | -17.89 | -72.78 | 1663 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Volume breakout | breakout | 87.59 | -12.41 | 87 | 11.5 | -62.47 | -20.65 | -62.91 | 914 |
| 71 | Keltner breakout | breakout | 87.37 | -12.63 | 128 | 10.2 | -84.77 | -34.76 | -85.12 | 1933 |
| 72 | Ichimoku | trend | 87.31 | -12.69 | 95 | 8.4 | -80.40 | -26.28 | -80.63 | 1764 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.39 | -27.90 | -84.48 | 2076 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -70.36 | -16.47 | -71.75 | 1404 |
| 75 | Supertrend | trend | 84.77 | -15.23 | 148 | 16.2 | -87.02 | -24.20 | -87.53 | 1964 |
| 76 | MACD zero-line | trend | 83.71 | -16.29 | 162 | 14.8 | -91.57 | -36.14 | -91.81 | 2367 |
| 77 | Donchian 20/10 | breakout | 83.15 | -16.85 | 168 | 17.3 | -90.74 | -29.80 | -91.02 | 2688 |
| 78 | Trend pullback | trend | 83.10 | -16.90 | 148 | 18.2 | -90.46 | -33.80 | -90.52 | 2287 |
| 79 | Triple EMA stack | trend | 82.66 | -17.34 | 179 | 14.5 | -92.93 | -37.00 | -93.08 | 2630 |
| 80 | Bollinger breakout | breakout | 82.60 | -17.40 | 173 | 14.5 | -93.92 | -41.91 | -94.11 | 2881 |
| 81 | RSI momentum | momentum | 82.56 | -17.44 | 161 | 11.2 | -90.39 | -30.23 | -90.67 | 2409 |
| 82 | MFI reversion | reversion | 82.14 | -17.86 | 155 | 17.4 | -87.71 | -34.29 | -87.92 | 2166 |
| 83 | ADX DI cross | trend | 81.35 | -18.65 | 168 | 6.5 | -89.26 | -46.77 | -89.51 | 2120 |
| 84 | Connors RSI(2) | reversion | 79.64 | -20.36 | 214 | 15.9 | -96.37 | -42.03 | -96.37 | 3652 |
| 85 | EMA 9/21 cross | trend | 79.23 | -20.77 | 231 | 15.2 | -97.33 | -41.69 | -97.43 | 3547 |
| 86 | Consensus | meta | 79.01 | -20.99 | 167 | 7.2 | -94.76 | -30.56 | -94.80 | 2674 |
| 87 | Candlestick reversal | reversion | 78.52 | -21.48 | 208 | 14.4 | -99.33 | -51.64 | -99.33 | 5550 |
| 88 | Stochastic reversion | reversion | 77.93 | -22.07 | 267 | 22.5 | -95.86 | -48.06 | -95.88 | 4049 |
| 89 | OBV trend | momentum | 77.81 | -22.19 | 236 | 13.6 | -95.76 | -50.25 | -95.87 | 3567 |
| 90 | Bollinger reversion | reversion | 76.89 | -23.11 | 249 | 12.4 | -95.69 | -46.08 | -95.69 | 3665 |
| 91 | VWAP momentum | momentum | 76.52 | -23.48 | 301 | 9.0 | -98.41 | -36.44 | -98.45 | 5207 |
| 92 | CCI reversion | reversion | 75.08 | -24.92 | 181 | 5.5 | -98.43 | -52.10 | -98.43 | 4691 |
| 93 | Parabolic SAR | trend | 74.20 | -25.80 | 258 | 12.8 | -96.95 | -58.25 | -97.01 | 3668 |
| 94 | MACD cross | trend | 73.69 | -26.31 | 210 | 10.5 | -99.69 | -63.81 | -99.71 | 6093 |
| 95 | Williams %R | reversion | 73.53 | -26.47 | 266 | 18.8 | -99.52 | -61.73 | -99.52 | 6087 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -93.73 | -99.89 | 8344 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T13:10 | Three white soldiers | buy | SOL-USD | 23.89 | — | entry signal |
| 2026-09-29T13:10 | MACD cross | buy | DOGE-USD | 18.44 | — | entry signal |
| 2026-09-29T13:05 | Parabolic SAR | sell | DOGE-USD | 14.79 | -0.05 | exit signal |
| 2026-09-29T13:05 | MACD zero-line | sell | DOGE-USD | 20.84 | -0.06 | exit signal |
| 2026-09-29T13:05 | MACD cross | sell | DOGE-USD | 18.29 | -0.06 | exit signal |
| 2026-09-29T13:02 | MACD zero-line · 1h | buy | SOL-USD | 4.85 | — | rebalance up |
| 2026-09-29T13:02 | MACD zero-line · 1h | sell | ETH-USD | 4.85 | 0.02 | rebalance down |
| 2026-09-29T13:00 | Volume breakout · 1h | buy | XRP-USD | 23.79 | — | entry signal |
| 2026-09-29T13:00 | Squeeze breakout · 1h | buy | XRP-USD | 24.54 | — | entry signal |
| 2026-09-29T13:00 | Keltner breakout · 1h | buy | XRP-USD | 23.78 | — | entry signal |
| 2026-09-29T13:00 | Keltner breakout · 1h | buy | ETH-USD | 23.78 | — | entry signal |
| 2026-09-29T13:00 | Bollinger breakout · 1h | buy | XRP-USD | 5.19 | — | entry signal |
| 2026-09-29T13:00 | Bollinger breakout · 1h | sell | ETH-USD | 4.99 | 0.02 | rebalance down |
| 2026-09-29T13:00 | Donchian 55/20 · 1h | buy | XRP-USD | 13.89 | — | entry signal |
| 2026-09-29T13:00 | Donchian 20/10 · 1h | buy | XRP-USD | 9.78 | — | entry signal |
| 2026-09-29T13:00 | Donchian 20/10 · 1h | buy | SOL-USD | 19.16 | — | entry signal |
| 2026-09-29T13:00 | Donchian 20/10 · 1h | sell | DOGE-USD | 4.78 | -0.01 | rebalance down |
| 2026-09-29T13:00 | RSI momentum · 1h | buy | XRP-USD | 5.04 | — | entry signal |
| 2026-09-29T13:00 | RSI momentum · 1h | sell | ETH-USD | 4.97 | 0.02 | rebalance down |
| 2026-09-29T13:00 | ROC + volume · 1h | buy | BTC-USD | 8.16 | — | entry signal |
| 2026-09-29T13:00 | ROC + volume · 1h | sell | ETH-USD | 8.16 | -0.04 | rebalance down |
| 2026-09-29T13:00 | Supertrend · 1h | buy | XRP-USD | 3.97 | — | entry signal |
| 2026-09-29T13:00 | MACD zero-line · 1h | buy | SOL-USD | 5.18 | — | entry signal |
| 2026-09-29T13:00 | MACD zero-line · 1h | sell | XRP-USD | 5.13 | 0.09 | rebalance down |
| 2026-09-29T13:00 | Trend pullback | sell | SOL-USD | 20.78 | 0.01 | take-profit |
| 2026-09-29T13:00 | MACD cross | sell | ETH-USD | 18.32 | -0.04 | exit signal |
| 2026-09-29T12:55 | Consensus | buy | ETH-USD | 3.60 | — | rebalance up |
| 2026-09-29T12:55 | Consensus | buy | DOGE-USD | 3.95 | — | rebalance up |
| 2026-09-29T12:50 | Volume breakout | sell | ETH-USD | 17.58 | -0.06 | exit signal |
| 2026-09-29T12:50 | Parabolic SAR | buy | SOL-USD | 3.71 | — | rebalance up |
| 2026-09-29T12:50 | Parabolic SAR | buy | BTC-USD | 3.82 | — | rebalance up |
| 2026-09-29T12:50 | Parabolic SAR | sell | ETH-USD | 14.82 | -0.02 | exit signal |
| 2026-09-29T12:45 | OBV trend | buy | ETH-USD | 3.91 | — | rebalance up |
| 2026-09-29T12:41 | Consensus | buy | SOL-USD | 19.73 | — | entry |
| 2026-09-29T12:41 | Volume breakout | buy | SOL-USD | 21.90 | — | entry signal |
| 2026-09-29T12:41 | Bollinger breakout | buy | ETH-USD | 4.13 | — | rebalance up |
| 2026-09-29T12:41 | Parabolic SAR | buy | BTC-USD | 14.79 | — | entry signal |
| 2026-09-29T12:41 | Parabolic SAR | sell | XRP-USD | 3.72 | -0.00 | rebalance down |
| 2026-09-29T12:41 | Parabolic SAR | sell | SOL-USD | 3.75 | 0.00 | rebalance down |
| 2026-09-29T12:41 | Parabolic SAR | sell | DOGE-USD | 3.73 | -0.00 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
