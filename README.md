# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T12:38:05.000150+00:00 · 5702 ticks

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

Today: 9345 decisions in 1869 calls, $0.1306 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T12:38 | 3 / 2 / 0 | DOGE-USD 15%, SOL-USD 13% |  |
| Breezy | 2026-09-29T12:38 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T12:38 | 5 / 0 / 0 | SOL-USD 42%, DOGE-USD 40% |  |

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
| 2 | Hold BTC | benchmark | 100.68 | 0.68 | 0 | — | 30.74 | 3.85 | -8.68 | 1 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 11 | RSI(14) reversion · 1h | reversion | 99.94 | -0.06 | 4 | 100.0 | 15.46 | 3.23 | -6.57 | 135 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.73 | -0.27 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.72 | -0.28 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.51 | -0.48 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 17 | Daily: Bullish score | daily | 99.23 | -0.77 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Z-score reversion · 1h | reversion | 99.17 | -0.83 | 7 | 57.1 | 4.37 | 1.07 | -8.60 | 154 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Connors RSI(2) · 1h | reversion | 99.08 | -0.92 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 21 | Timing: Nasdaq FTD · QQQ | daily | 99.08 | -0.93 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 22 | Daily: SMA 20/50 cross · AAPL | daily | 99.06 | -0.94 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 99.06 | -0.94 | 25 | 56.0 | -12.27 | -2.72 | -13.74 | 324 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 98.97 | -1.03 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | CCI reversion · 1h | reversion | 98.61 | -1.39 | 28 | 42.9 | 1.57 | 0.43 | -12.41 | 405 |
| 27 | Williams %R · 1h | reversion | 98.60 | -1.40 | 33 | 51.5 | -17.89 | -3.29 | -19.48 | 485 |
| 28 | Copy: Insider buying | copy | 98.56 | -1.44 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.15 | -2.52 | -11.75 | 234 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.25 | -1.75 | 13 | 23.1 | -25.46 | -5.96 | -26.04 | 490 |
| 32 | Squeeze breakout · 1h | breakout | 98.20 | -1.80 | 7 | 14.3 | 16.59 | 2.91 | -6.26 | 94 |
| 33 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 34 | Supertrend · 1h | trend | 98.16 | -1.84 | 11 | 9.1 | 5.73 | 0.96 | -16.43 | 194 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 98.07 | -1.93 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 36 | EMA 20/50 cross · 1h | trend | 97.95 | -2.05 | 8 | 12.5 | 15.78 | 1.88 | -14.36 | 126 |
| 37 | MACD cross · 1h | trend | 97.73 | -2.27 | 31 | 9.7 | -15.50 | -2.61 | -20.56 | 459 |
| 38 | Bollinger reversion · 1h | reversion | 97.31 | -2.69 | 19 | 31.6 | -17.66 | -4.91 | -17.74 | 306 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 40 | Donchian 55/20 · 1h | breakout | 97.22 | -2.78 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 41 | MACD zero-line · 1h | trend | 97.19 | -2.81 | 15 | 6.7 | -2.51 | -0.16 | -14.64 | 221 |
| 42 | Timing: Nasdaq FTD · TQQQ | daily | 97.13 | -2.87 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 43 | Parabolic SAR · 1h | trend | 97.12 | -2.88 | 20 | 15.0 | -5.25 | -0.58 | -18.82 | 304 |
| 44 | Agent (ML meta-label) | meta | 97.09 | -2.91 | 79 | 10.1 | 4.20 | 0.88 | -10.62 | 394 |
| 45 | Bollinger breakout · 1h | breakout | 97.07 | -2.94 | 13 | 7.7 | 13.54 | 1.91 | -9.85 | 285 |
| 46 | Trend pullback · 1h | trend | 97.06 | -2.94 | 22 | 13.6 | -25.55 | -6.77 | -26.30 | 147 |
| 47 | Max aggression: 5-day momentum | meta | 97.03 | -2.97 | 1 | 0.0 | 0.63 | 0.40 | -29.56 | 29 |
| 48 | RSI momentum · 1h | momentum | 96.58 | -3.42 | 20 | 5.0 | 1.75 | 0.44 | -15.29 | 214 |
| 49 | Triple EMA stack · 1h | trend | 96.17 | -3.83 | 24 | 8.3 | -2.59 | -0.09 | -22.95 | 224 |
| 50 | Ichimoku · 1h | trend | 96.15 | -3.85 | 11 | 9.1 | 8.45 | 1.17 | -15.13 | 121 |
| 51 | ADX DI cross · 1h | trend | 96.10 | -3.90 | 25 | 8.0 | -11.26 | -2.10 | -15.39 | 250 |
| 52 | EMA 9/21 cross · 1h | trend | 95.98 | -4.02 | 34 | 11.8 | 3.94 | 0.73 | -16.92 | 312 |
| 53 | MFI reversion · 1h | reversion | 95.91 | -4.09 | 38 | 13.2 | -9.06 | -1.65 | -17.20 | 125 |
| 54 | Donchian 20/10 · 1h | breakout | 95.85 | -4.15 | 12 | 16.7 | 12.13 | 1.70 | -12.78 | 214 |
| 55 | OBV trend · 1h | momentum | 95.63 | -4.38 | 47 | 6.4 | -9.25 | -0.95 | -25.24 | 318 |
| 56 | Three white soldiers | momentum | 95.57 | -4.43 | 41 | 19.5 | -51.78 | -28.65 | -52.20 | 625 |
| 57 | Max aggression: 1-day momentum | meta | 95.56 | -4.44 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 58 | VWAP momentum · 1h | momentum | 95.54 | -4.46 | 82 | 7.3 | -30.94 | -4.52 | -34.09 | 1248 |
| 59 | Volume breakout · 1h | breakout | 95.16 | -4.84 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.11 | -4.89 | 7 | 0.0 | -0.48 | 0.14 | -18.68 | 221 |
| 61 | Heikin-Ashi · 1h | trend | 94.82 | -5.18 | 35 | 11.4 | -21.66 | -3.20 | -29.64 | 680 |
| 62 | ROC + volume · 1h | momentum | 91.86 | -8.13 | 44 | 6.8 | -4.14 | -0.38 | -17.54 | 404 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.12 | -21.90 | -71.22 | 1472 |
| 64 | Squeeze breakout | breakout | 89.45 | -10.54 | 75 | 6.7 | -60.13 | -18.88 | -60.51 | 1187 |
| 65 | Donchian 55/20 | breakout | 89.43 | -10.57 | 80 | 11.2 | -68.09 | -15.62 | -68.56 | 1332 |
| 66 | EMA 20/50 cross | trend | 88.91 | -11.09 | 97 | 13.4 | -78.61 | -17.53 | -79.35 | 1486 |
| 67 | ROC + volume | momentum | 88.61 | -11.39 | 123 | 17.1 | -72.02 | -17.98 | -72.78 | 1663 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Volume breakout | breakout | 87.45 | -12.55 | 86 | 11.6 | -62.52 | -20.68 | -62.90 | 913 |
| 71 | Keltner breakout | breakout | 86.97 | -13.03 | 128 | 10.2 | -84.84 | -35.07 | -85.12 | 1933 |
| 72 | Ichimoku | trend | 86.91 | -13.09 | 95 | 8.4 | -80.46 | -26.41 | -80.64 | 1765 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.39 | -27.89 | -84.48 | 2077 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -70.37 | -16.48 | -71.75 | 1404 |
| 75 | Supertrend | trend | 84.43 | -15.57 | 148 | 16.2 | -87.08 | -24.32 | -87.53 | 1964 |
| 76 | MACD zero-line | trend | 83.66 | -16.34 | 161 | 14.9 | -91.57 | -36.17 | -91.81 | 2367 |
| 77 | Trend pullback | trend | 83.02 | -16.98 | 147 | 17.7 | -90.47 | -33.85 | -90.52 | 2287 |
| 78 | Donchian 20/10 | breakout | 82.77 | -17.23 | 168 | 17.3 | -90.78 | -29.98 | -91.02 | 2688 |
| 79 | Triple EMA stack | trend | 82.35 | -17.65 | 179 | 14.5 | -92.96 | -37.18 | -93.09 | 2629 |
| 80 | Bollinger breakout | breakout | 82.27 | -17.73 | 173 | 14.5 | -93.94 | -42.12 | -94.11 | 2881 |
| 81 | RSI momentum | momentum | 82.23 | -17.77 | 161 | 11.2 | -90.43 | -30.31 | -90.67 | 2410 |
| 82 | MFI reversion | reversion | 82.14 | -17.86 | 155 | 17.4 | -87.70 | -34.21 | -87.92 | 2165 |
| 83 | ADX DI cross | trend | 81.35 | -18.65 | 168 | 6.5 | -89.26 | -46.76 | -89.50 | 2120 |
| 84 | Connors RSI(2) | reversion | 79.64 | -20.36 | 214 | 15.9 | -96.37 | -42.04 | -96.37 | 3651 |
| 85 | EMA 9/21 cross | trend | 78.93 | -21.07 | 231 | 15.2 | -97.34 | -41.92 | -97.43 | 3547 |
| 86 | Consensus | meta | 78.80 | -21.20 | 167 | 7.2 | -94.74 | -30.48 | -94.77 | 2669 |
| 87 | Candlestick reversal | reversion | 78.52 | -21.48 | 208 | 14.4 | -99.33 | -51.86 | -99.34 | 5552 |
| 88 | Stochastic reversion | reversion | 77.93 | -22.07 | 267 | 22.5 | -95.87 | -48.24 | -95.88 | 4051 |
| 89 | OBV trend | momentum | 77.50 | -22.50 | 236 | 13.6 | -95.78 | -50.60 | -95.87 | 3567 |
| 90 | Bollinger reversion | reversion | 76.89 | -23.11 | 249 | 12.4 | -95.72 | -46.36 | -95.72 | 3668 |
| 91 | VWAP momentum | momentum | 76.21 | -23.79 | 301 | 9.0 | -98.43 | -36.82 | -98.47 | 5213 |
| 92 | CCI reversion | reversion | 75.08 | -24.92 | 181 | 5.5 | -98.43 | -52.01 | -98.43 | 4691 |
| 93 | Parabolic SAR | trend | 74.13 | -25.88 | 256 | 12.9 | -96.95 | -58.04 | -97.01 | 3669 |
| 94 | MACD cross | trend | 73.62 | -26.38 | 208 | 10.6 | -99.70 | -65.22 | -99.71 | 6096 |
| 95 | Williams %R | reversion | 73.53 | -26.47 | 266 | 18.8 | -99.52 | -61.70 | -99.52 | 6086 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -93.05 | -99.89 | 8339 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T12:35 | Connors RSI(2) | sell | BTC-USD | 19.86 | -0.09 | exit signal |
| 2026-09-29T12:35 | Volume breakout | buy | XRP-USD | 21.88 | — | entry signal |
| 2026-09-29T12:35 | Keltner breakout | buy | ETH-USD | 4.23 | — | rebalance up |
| 2026-09-29T12:35 | Donchian 55/20 | buy | SOL-USD | 4.49 | — | rebalance up |
| 2026-09-29T12:35 | Donchian 20/10 | buy | ETH-USD | 4.03 | — | rebalance up |
| 2026-09-29T12:35 | OBV trend | buy | SOL-USD | 3.90 | — | rebalance up |
| 2026-09-29T12:35 | Trend pullback | sell | XRP-USD | 20.87 | 0.16 | take-profit |
| 2026-09-29T12:35 | Parabolic SAR | buy | XRP-USD | 18.55 | — | entry signal |
| 2026-09-29T12:35 | MACD cross | buy | SOL-USD | 3.55 | — | rebalance up |
| 2026-09-29T12:35 | MACD cross | buy | ETH-USD | 3.70 | — | rebalance up |
| 2026-09-29T12:30 | Connors RSI(2) | sell | XRP-USD | 19.87 | -0.08 | exit signal |
| 2026-09-29T12:30 | Trend pullback | buy | XRP-USD | 20.71 | — | entry signal |
| 2026-09-29T12:30 | Parabolic SAR | sell | XRP-USD | 14.81 | -0.03 | exit signal |
| 2026-09-29T12:25 | Consensus | buy | XRP-USD | 3.98 | — | rebalance up |
| 2026-09-29T12:25 | Consensus | sell | SOL-USD | 15.64 | -0.13 | target is flat |
| 2026-09-29T12:25 | Consensus | sell | BTC-USD | 15.62 | -0.15 | target is flat |
| 2026-09-29T12:25 | Connors RSI(2) | buy | XRP-USD | 19.95 | — | entry signal |
| 2026-09-29T12:25 | Connors RSI(2) | buy | BTC-USD | 19.95 | — | entry signal |
| 2026-09-29T12:25 | Volume breakout | sell | XRP-USD | 21.84 | -0.20 | exit signal |
| 2026-09-29T12:25 | Volume breakout | sell | SOL-USD | 21.86 | -0.18 | exit signal |
| 2026-09-29T12:25 | Volume breakout | sell | DOGE-USD | 21.85 | -0.21 | exit signal |
| 2026-09-29T12:25 | Keltner breakout | buy | XRP-USD | 8.66 | — | rebalance up |
| 2026-09-29T12:25 | Keltner breakout | buy | SOL-USD | 4.33 | — | rebalance up |
| 2026-09-29T12:25 | Keltner breakout | buy | DOGE-USD | 4.35 | — | rebalance up |
| 2026-09-29T12:25 | Keltner breakout | sell | BTC-USD | 17.22 | -0.17 | stop-loss |
| 2026-09-29T12:25 | Bollinger breakout | buy | SOL-USD | 4.10 | — | rebalance up |
| 2026-09-29T12:25 | Bollinger breakout | buy | DOGE-USD | 4.12 | — | rebalance up |
| 2026-09-29T12:25 | Bollinger breakout | sell | BTC-USD | 16.30 | -0.16 | stop-loss |
| 2026-09-29T12:25 | Donchian 55/20 | buy | XRP-USD | 4.82 | — | rebalance up |
| 2026-09-29T12:25 | Donchian 55/20 | sell | BTC-USD | 17.70 | -0.17 | stop-loss |
| 2026-09-29T12:25 | Donchian 20/10 | buy | XRP-USD | 8.24 | — | rebalance up |
| 2026-09-29T12:25 | Donchian 20/10 | buy | SOL-USD | 4.12 | — | rebalance up |
| 2026-09-29T12:25 | Donchian 20/10 | buy | DOGE-USD | 4.14 | — | rebalance up |
| 2026-09-29T12:25 | Donchian 20/10 | sell | BTC-USD | 16.39 | -0.16 | stop-loss |
| 2026-09-29T12:25 | OBV trend | buy | DOGE-USD | 3.90 | — | rebalance up |
| 2026-09-29T12:25 | OBV trend | sell | BTC-USD | 15.35 | -0.15 | stop-loss |
| 2026-09-29T12:25 | Ichimoku | sell | BTC-USD | 21.53 | -0.17 | exit signal |
| 2026-09-29T12:25 | Parabolic SAR | buy | SOL-USD | 7.38 | — | rebalance up |
| 2026-09-29T12:25 | Parabolic SAR | buy | DOGE-USD | 3.72 | — | rebalance up |
| 2026-09-29T12:25 | Parabolic SAR | sell | BTC-USD | 18.42 | -0.10 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: Yahoo CRAFX: GET https://query2.finance.yahoo.com/v8/finance/chart/CRAFX: HTTP 429 Too Many Requests
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: Yahoo CYBN: GET https://query2.finance.yahoo.com/v8/finance/chart/CYBN: HTTP 429 Too Many Requests
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: Yahoo GREE: GET https://query2.finance.yahoo.com/v8/finance/chart/GREE: HTTP 429 Too Many Requests

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
