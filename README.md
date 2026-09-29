# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T10:40:05.000129+00:00 · 5600 ticks

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

Today: 7815 decisions in 1563 calls, $0.1093 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T10:40 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-09-29T10:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T10:40 | 4 / 0 / 1 | ETH-USD 24%, BTC-USD 24% |  |

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
| 2 | Hold BTC | benchmark | 100.54 | 0.54 | 0 | — | 30.15 | 3.78 | -8.68 | 1 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | RSI(14) reversion · 1h | reversion | 100.03 | 0.03 | 4 | 100.0 | 15.52 | 3.24 | -6.57 | 138 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.90 | -0.10 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.89 | -0.11 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.68 | -0.32 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | Daily: Bullish score | daily | 99.40 | -0.60 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 16 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 17 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 99.24 | -0.76 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 19 | Daily: SMA 20/50 cross · AAPL | daily | 99.23 | -0.77 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 20 | Z-score reversion · 1h | reversion | 99.20 | -0.80 | 6 | 50.0 | 4.29 | 1.05 | -8.60 | 154 |
| 21 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 25 | 56.0 | -12.35 | -2.73 | -13.82 | 324 |
| 22 | Connors RSI(2) · 1h | reversion | 99.16 | -0.84 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 23 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.14 | -0.86 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Williams %R · 1h | reversion | 98.75 | -1.25 | 33 | 51.5 | -17.91 | -3.29 | -19.50 | 485 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 27 | CCI reversion · 1h | reversion | 98.73 | -1.27 | 28 | 42.9 | 1.57 | 0.43 | -12.41 | 405 |
| 28 | Copy: Insider buying | copy | 98.71 | -1.29 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.15 | -2.52 | -11.75 | 234 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.29 | -1.72 | 13 | 23.1 | -25.93 | -6.05 | -26.44 | 493 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.24 | -1.76 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 34 | Supertrend · 1h | trend | 98.17 | -1.83 | 11 | 9.1 | 5.58 | 0.94 | -16.43 | 194 |
| 35 | Squeeze breakout · 1h | breakout | 98.02 | -1.98 | 7 | 14.3 | 15.87 | 2.79 | -6.26 | 95 |
| 36 | EMA 20/50 cross · 1h | trend | 98.01 | -1.99 | 8 | 12.5 | 15.56 | 1.86 | -14.36 | 126 |
| 37 | Bollinger reversion · 1h | reversion | 97.46 | -2.54 | 19 | 31.6 | -17.67 | -4.91 | -17.76 | 306 |
| 38 | MACD cross · 1h | trend | 97.38 | -2.62 | 31 | 9.7 | -16.19 | -2.74 | -20.74 | 460 |
| 39 | Donchian 55/20 · 1h | breakout | 97.34 | -2.66 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.30 | -2.70 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 42 | Agent (ML meta-label) | meta | 97.23 | -2.77 | 79 | 10.1 | 4.29 | 0.89 | -11.62 | 390 |
| 43 | Trend pullback · 1h | trend | 97.20 | -2.80 | 22 | 13.6 | -25.55 | -6.77 | -26.30 | 147 |
| 44 | Parabolic SAR · 1h | trend | 97.01 | -2.99 | 20 | 15.0 | -5.76 | -0.66 | -18.82 | 304 |
| 45 | Bollinger breakout · 1h | breakout | 96.97 | -3.03 | 13 | 7.7 | 13.24 | 1.88 | -9.85 | 285 |
| 46 | RSI momentum · 1h | momentum | 96.41 | -3.58 | 20 | 5.0 | 1.40 | 0.39 | -15.29 | 214 |
| 47 | Max aggression: 5-day momentum | meta | 96.37 | -3.63 | 1 | 0.0 | -0.22 | 0.33 | -29.56 | 29 |
| 48 | MACD zero-line · 1h | trend | 96.32 | -3.67 | 15 | 6.7 | -3.51 | -0.31 | -14.64 | 220 |
| 49 | Triple EMA stack · 1h | trend | 96.08 | -3.92 | 24 | 8.3 | -2.91 | -0.13 | -22.95 | 224 |
| 50 | EMA 9/21 cross · 1h | trend | 95.99 | -4.01 | 34 | 11.8 | 2.75 | 0.57 | -16.92 | 315 |
| 51 | Ichimoku · 1h | trend | 95.98 | -4.02 | 11 | 9.1 | 8.08 | 1.13 | -15.13 | 121 |
| 52 | MFI reversion · 1h | reversion | 95.91 | -4.09 | 38 | 13.2 | -9.21 | -1.68 | -17.20 | 125 |
| 53 | ADX DI cross · 1h | trend | 95.86 | -4.14 | 25 | 8.0 | -11.62 | -2.18 | -15.39 | 250 |
| 54 | Max aggression: 1-day momentum | meta | 95.72 | -4.28 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | Donchian 20/10 · 1h | breakout | 95.66 | -4.34 | 12 | 16.7 | 11.77 | 1.66 | -12.78 | 214 |
| 56 | Three white soldiers | momentum | 95.57 | -4.43 | 41 | 19.5 | -51.86 | -28.66 | -52.21 | 626 |
| 57 | OBV trend · 1h | momentum | 95.49 | -4.51 | 47 | 6.4 | -9.57 | -1.00 | -25.24 | 318 |
| 58 | VWAP momentum · 1h | momentum | 95.43 | -4.57 | 82 | 7.3 | -31.90 | -4.70 | -34.09 | 1251 |
| 59 | Volume breakout · 1h | breakout | 95.20 | -4.80 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.15 | -4.85 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 94.16 | -5.84 | 35 | 11.4 | -22.89 | -3.42 | -29.64 | 683 |
| 62 | ROC + volume · 1h | momentum | 91.99 | -8.01 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.06 | -21.83 | -71.21 | 1470 |
| 64 | Squeeze breakout | breakout | 89.18 | -10.82 | 75 | 6.7 | -60.25 | -18.95 | -60.49 | 1186 |
| 65 | Donchian 55/20 | breakout | 88.91 | -11.09 | 79 | 11.4 | -68.34 | -15.83 | -68.56 | 1330 |
| 66 | ROC + volume | momentum | 88.53 | -11.47 | 123 | 17.1 | -72.06 | -18.01 | -72.65 | 1659 |
| 67 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 68 | Volume breakout | breakout | 88.26 | -11.74 | 82 | 12.2 | -62.36 | -20.54 | -62.56 | 909 |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | EMA 20/50 cross | trend | 88.01 | -11.98 | 97 | 13.4 | -78.85 | -17.77 | -79.29 | 1487 |
| 71 | Keltner breakout | breakout | 87.00 | -13.00 | 127 | 10.2 | -84.89 | -35.21 | -85.03 | 1929 |
| 72 | Ichimoku | trend | 86.81 | -13.19 | 94 | 8.5 | -80.51 | -26.48 | -80.51 | 1759 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.49 | -28.16 | -84.56 | 2081 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -70.93 | -17.21 | -71.75 | 1417 |
| 75 | Supertrend | trend | 83.86 | -16.14 | 147 | 16.3 | -87.25 | -24.72 | -87.53 | 1964 |
| 76 | MACD zero-line | trend | 83.60 | -16.40 | 161 | 14.9 | -91.62 | -36.46 | -91.79 | 2367 |
| 77 | Donchian 20/10 | breakout | 82.79 | -17.21 | 167 | 17.4 | -90.86 | -30.19 | -91.02 | 2686 |
| 78 | Trend pullback | trend | 82.69 | -17.31 | 142 | 15.5 | -90.54 | -34.03 | -90.54 | 2285 |
| 79 | Bollinger breakout | breakout | 82.30 | -17.70 | 172 | 14.5 | -93.98 | -42.52 | -94.08 | 2878 |
| 80 | Triple EMA stack | trend | 82.15 | -17.85 | 176 | 14.8 | -92.97 | -37.28 | -93.07 | 2625 |
| 81 | MFI reversion | reversion | 82.13 | -17.87 | 154 | 17.5 | -87.78 | -34.78 | -87.92 | 2168 |
| 82 | RSI momentum | momentum | 81.95 | -18.05 | 160 | 11.2 | -90.47 | -30.37 | -90.65 | 2406 |
| 83 | ADX DI cross | trend | 81.44 | -18.56 | 167 | 6.6 | -89.37 | -48.14 | -89.50 | 2126 |
| 84 | Connors RSI(2) | reversion | 80.10 | -19.90 | 207 | 16.4 | -96.38 | -41.77 | -96.38 | 3652 |
| 85 | EMA 9/21 cross | trend | 78.78 | -21.22 | 227 | 15.0 | -97.38 | -42.58 | -97.43 | 3547 |
| 86 | Consensus | meta | 78.69 | -21.31 | 165 | 7.3 | -94.76 | -30.62 | -94.76 | 2667 |
| 87 | Candlestick reversal | reversion | 78.53 | -21.47 | 205 | 14.1 | -99.34 | -52.11 | -99.34 | 5551 |
| 88 | Stochastic reversion | reversion | 78.17 | -21.83 | 262 | 22.9 | -95.90 | -48.68 | -95.90 | 4051 |
| 89 | OBV trend | momentum | 77.55 | -22.45 | 233 | 13.3 | -95.78 | -50.64 | -95.85 | 3561 |
| 90 | Bollinger reversion | reversion | 76.89 | -23.11 | 249 | 12.4 | -95.75 | -46.75 | -95.76 | 3673 |
| 91 | VWAP momentum | momentum | 75.48 | -24.52 | 301 | 9.0 | -98.47 | -37.31 | -98.49 | 5218 |
| 92 | CCI reversion | reversion | 75.08 | -24.92 | 181 | 5.5 | -98.44 | -52.68 | -98.44 | 4697 |
| 93 | Parabolic SAR | trend | 74.30 | -25.70 | 253 | 13.0 | -96.95 | -58.18 | -97.00 | 3662 |
| 94 | Williams %R | reversion | 73.75 | -26.25 | 261 | 19.2 | -99.52 | -63.11 | -99.52 | 6092 |
| 95 | MACD cross | trend | 73.43 | -26.57 | 207 | 10.6 | -99.70 | -68.34 | -99.70 | 6099 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.81 | -99.89 | 8334 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T10:40 | OBV trend | sell | SOL-USD | 19.37 | -0.11 | exit signal |
| 2026-09-29T10:40 | RSI momentum | sell | XRP-USD | 16.15 | -0.16 | stop-loss |
| 2026-09-29T10:40 | RSI momentum | sell | SOL-USD | 16.36 | -0.12 | exit signal |
| 2026-09-29T10:40 | RSI momentum | sell | DOGE-USD | 16.57 | 0.11 | exit signal |
| 2026-09-29T10:40 | Trend pullback | buy | ETH-USD | 8.26 | — | rebalance up |
| 2026-09-29T10:40 | Trend pullback | buy | DOGE-USD | 4.16 | — | rebalance up |
| 2026-09-29T10:40 | Trend pullback | sell | SOL-USD | 16.51 | -0.10 | exit signal |
| 2026-09-29T10:40 | Ichimoku | sell | BTC-USD | 21.68 | -0.15 | exit signal |
| 2026-09-29T10:40 | Supertrend | buy | ETH-USD | 8.70 | — | rebalance up |
| 2026-09-29T10:40 | Supertrend | sell | DOGE-USD | 16.92 | 0.20 | exit signal |
| 2026-09-29T10:40 | Triple EMA stack | buy | SOL-USD | 4.12 | — | rebalance up |
| 2026-09-29T10:40 | Triple EMA stack | buy | ETH-USD | 11.91 | — | rebalance up |
| 2026-09-29T10:40 | Triple EMA stack | sell | DOGE-USD | 16.37 | 0.19 | exit signal |
| 2026-09-29T10:35 | Consensus | sell | DOGE-USD | 19.60 | -0.16 | target is flat |
| 2026-09-29T10:35 | Consensus | sell | BTC-USD | 19.67 | -0.08 | target is flat |
| 2026-09-29T10:35 | Connors RSI(2) | buy | SOL-USD | 20.06 | — | entry signal |
| 2026-09-29T10:35 | Keltner breakout | sell | BTC-USD | 21.70 | -0.14 | exit signal |
| 2026-09-29T10:35 | Bollinger breakout | sell | SOL-USD | 20.47 | -0.18 | stop-loss |
| 2026-09-29T10:35 | Donchian 20/10 | sell | SOL-USD | 16.70 | 0.16 | exit signal |
| 2026-09-29T10:35 | Donchian 20/10 | sell | DOGE-USD | 16.65 | 0.29 | exit signal |
| 2026-09-29T10:35 | OBV trend | sell | ETH-USD | 19.35 | -0.13 | exit signal |
| 2026-09-29T10:35 | OBV trend | sell | BTC-USD | 19.43 | -0.07 | exit signal |
| 2026-09-29T10:35 | ROC + volume | sell | XRP-USD | 22.10 | -0.20 | exit signal |
| 2026-09-29T10:35 | ROC + volume | sell | SOL-USD | 22.08 | -0.21 | exit signal |
| 2026-09-29T10:35 | ROC + volume | sell | DOGE-USD | 22.03 | -0.25 | stop-loss |
| 2026-09-29T10:35 | Ichimoku | sell | XRP-USD | 21.67 | -0.21 | exit signal |
| 2026-09-29T10:35 | Ichimoku | sell | SOL-USD | 21.69 | -0.20 | exit signal |
| 2026-09-29T10:35 | Ichimoku | sell | DOGE-USD | 21.72 | -0.16 | exit signal |
| 2026-09-29T10:35 | MACD zero-line | sell | BTC-USD | 20.84 | -0.09 | exit signal |
| 2026-09-29T10:35 | MACD cross | sell | BTC-USD | 18.37 | -0.08 | exit signal |
| 2026-09-29T10:30 | OBV trend | buy | ETH-USD | 19.48 | — | entry signal |
| 2026-09-29T10:30 | MACD zero-line | sell | XRP-USD | 20.84 | -0.11 | exit signal |
| 2026-09-29T10:30 | MACD cross | sell | XRP-USD | 14.71 | -0.07 | exit signal |
| 2026-09-29T10:30 | MACD cross | sell | SOL-USD | 18.38 | -0.09 | exit signal |
| 2026-09-29T10:30 | MACD cross | sell | ETH-USD | 18.35 | -0.11 | exit signal |
| 2026-09-29T10:30 | EMA 9/21 cross | buy | ETH-USD | 3.94 | — | rebalance up |
| 2026-09-29T10:30 | EMA 9/21 cross | sell | BTC-USD | 3.94 | -0.01 | rebalance down |
| 2026-09-29T10:25 | Squeeze breakout | sell | DOGE-USD | 22.15 | -0.20 | exit signal |
| 2026-09-29T10:25 | Bollinger breakout | sell | DOGE-USD | 20.52 | -0.13 | exit signal |
| 2026-09-29T10:25 | OBV trend | buy | SOL-USD | 3.90 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
