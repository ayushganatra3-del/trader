# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T00:10:05.000150+00:00 · 5087 ticks

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

Today: 135 decisions in 27 calls, $0.0019 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T00:10 | 1 / 3 / 1 | DOGE-USD 20% |  |
| Breezy | 2026-09-29T00:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T00:10 | 2 / 3 / 0 | DOGE-USD 35%, XRP-USD 26% |  |

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
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.41 | 1.25 | -2.47 | 92 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 10 | RSI(14) reversion · 1h | reversion | 99.68 | -0.32 | 2 | 100.0 | 12.13 | 2.52 | -6.57 | 145 |
| 11 | Hold BTC | benchmark | 99.67 | -0.33 | 0 | — | 30.59 | 3.84 | -8.68 | 1 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.66 | -0.34 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.65 | -0.35 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.44 | -0.56 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 17 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.77 | -5.16 | 28 |
| 18 | Daily: Bullish score | daily | 99.15 | -0.85 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 19 | Connors RSI(2) · 1h | reversion | 99.04 | -0.96 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.00 | -1.00 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.99 | -1.01 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.89 | -1.11 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 98.80 | -1.20 | 23 | 56.5 | -12.40 | -2.75 | -14.07 | 324 |
| 24 | Z-score reversion · 1h | reversion | 98.79 | -1.21 | 4 | 25.0 | 3.57 | 0.89 | -8.60 | 155 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | Williams %R · 1h | reversion | 98.65 | -1.35 | 29 | 51.7 | -18.41 | -3.39 | -20.37 | 488 |
| 27 | CCI reversion · 1h | reversion | 98.56 | -1.44 | 23 | 34.8 | 1.63 | 0.44 | -12.41 | 409 |
| 28 | Copy: Insider buying | copy | 98.49 | -1.51 | 2 | 100.0 | -12.69 | -2.44 | -17.74 | 73 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.88 | -2.76 | -11.75 | 233 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Squeeze breakout · 1h | breakout | 98.00 | -2.00 | 7 | 14.3 | 16.09 | 2.83 | -6.26 | 94 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 98.00 | -2.00 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 34 | Candlestick reversal · 1h | reversion | 97.90 | -2.10 | 12 | 16.7 | -25.95 | -6.05 | -26.71 | 492 |
| 35 | EMA 20/50 cross · 1h | trend | 97.81 | -2.19 | 8 | 12.5 | 15.79 | 1.88 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.79 | -2.21 | 11 | 9.1 | 4.83 | 0.84 | -16.43 | 195 |
| 37 | MACD cross · 1h | trend | 97.66 | -2.34 | 27 | 11.1 | -15.41 | -2.59 | -20.52 | 454 |
| 38 | Bollinger reversion · 1h | reversion | 97.25 | -2.75 | 19 | 31.6 | -17.61 | -4.89 | -17.88 | 308 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 40 | Donchian 55/20 · 1h | breakout | 97.17 | -2.83 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.06 | -2.94 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 42 | Parabolic SAR · 1h | trend | 97.04 | -2.96 | 19 | 15.8 | -5.64 | -0.64 | -18.82 | 301 |
| 43 | Agent (ML meta-label) | meta | 97.00 | -3.00 | 79 | 10.1 | 2.96 | 0.69 | -11.25 | 397 |
| 44 | Trend pullback · 1h | trend | 96.99 | -3.01 | 22 | 13.6 | -26.02 | -6.92 | -26.61 | 149 |
| 45 | MACD zero-line · 1h | trend | 96.95 | -3.05 | 14 | 7.1 | -3.34 | -0.28 | -14.81 | 221 |
| 46 | Bollinger breakout · 1h | breakout | 96.80 | -3.20 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 47 | RSI momentum · 1h | momentum | 96.41 | -3.59 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Three white soldiers | momentum | 96.19 | -3.81 | 32 | 12.5 | -51.65 | -28.00 | -51.65 | 619 |
| 49 | EMA 9/21 cross · 1h | trend | 96.11 | -3.89 | 33 | 12.1 | 3.31 | 0.65 | -16.92 | 311 |
| 50 | Triple EMA stack · 1h | trend | 95.93 | -4.07 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 51 | Ichimoku · 1h | trend | 95.90 | -4.10 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 52 | ADX DI cross · 1h | trend | 95.83 | -4.17 | 25 | 8.0 | -12.26 | -2.31 | -16.02 | 250 |
| 53 | Max aggression: 5-day momentum | meta | 95.77 | -4.23 | 1 | 0.0 | -0.60 | 0.30 | -29.56 | 29 |
| 54 | Donchian 20/10 · 1h | breakout | 95.76 | -4.24 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 55 | MFI reversion · 1h | reversion | 95.60 | -4.40 | 38 | 13.2 | -9.78 | -1.80 | -17.20 | 126 |
| 56 | Max aggression: 1-day momentum | meta | 95.49 | -4.51 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 57 | OBV trend · 1h | momentum | 95.40 | -4.60 | 47 | 6.4 | -9.57 | -1.00 | -25.24 | 317 |
| 58 | VWAP momentum · 1h | momentum | 95.23 | -4.77 | 80 | 6.2 | -33.29 | -4.95 | -33.83 | 1250 |
| 59 | Volume breakout · 1h | breakout | 95.15 | -4.85 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.10 | -4.90 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 94.31 | -5.69 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | AI bee: Boozy | ai | 93.54 | -6.46 | 37 | 2.7 | — | — | — | — |
| 63 | AI bee: Bizzy | ai | 93.34 | -6.66 | 176 | 15.3 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 93.14 | -6.86 | 86 | 36.0 | -70.89 | -21.62 | -71.28 | 1472 |
| 65 | ROC + volume · 1h | momentum | 91.95 | -8.05 | 43 | 7.0 | -3.98 | -0.35 | -17.40 | 403 |
| 66 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.83 | -18.62 | -59.90 | 1179 |
| 67 | ROC + volume | momentum | 89.42 | -10.58 | 114 | 16.7 | -71.95 | -17.84 | -72.35 | 1656 |
| 68 | Volume breakout | breakout | 88.86 | -11.14 | 75 | 9.3 | -62.39 | -20.43 | -62.39 | 906 |
| 69 | Donchian 55/20 | breakout | 88.82 | -11.18 | 76 | 11.8 | -68.74 | -15.88 | -68.76 | 1331 |
| 70 | EMA 20/50 cross | trend | 88.50 | -11.50 | 89 | 14.6 | -78.85 | -17.64 | -78.94 | 1487 |
| 71 | Ichimoku | trend | 87.81 | -12.19 | 84 | 8.3 | -80.44 | -26.22 | -80.54 | 1757 |
| 72 | Keltner breakout | breakout | 87.81 | -12.19 | 117 | 10.3 | -84.90 | -34.84 | -84.91 | 1928 |
| 73 | Z-score reversion | reversion | 86.66 | -13.34 | 142 | 29.6 | -84.55 | -28.08 | -84.69 | 2083 |
| 74 | VWAP reversion | reversion | 85.79 | -14.21 | 101 | 13.9 | -70.42 | -16.66 | -71.75 | 1408 |
| 75 | MACD zero-line | trend | 85.05 | -14.95 | 151 | 15.9 | -91.50 | -35.60 | -91.64 | 2366 |
| 76 | Supertrend | trend | 84.70 | -15.30 | 137 | 16.1 | -87.42 | -24.87 | -87.46 | 1968 |
| 77 | Bollinger breakout | breakout | 84.67 | -15.33 | 153 | 15.0 | -93.92 | -41.56 | -93.93 | 2874 |
| 78 | RSI momentum | momentum | 84.60 | -15.40 | 140 | 11.4 | -90.27 | -29.58 | -90.35 | 2398 |
| 79 | Triple EMA stack | trend | 83.77 | -16.23 | 163 | 14.1 | -92.97 | -36.47 | -93.00 | 2627 |
| 80 | Trend pullback | trend | 83.47 | -16.53 | 138 | 15.9 | -90.52 | -33.77 | -90.53 | 2281 |
| 81 | Donchian 20/10 | breakout | 83.35 | -16.65 | 154 | 15.6 | -90.90 | -29.98 | -90.91 | 2687 |
| 82 | ADX DI cross | trend | 82.80 | -17.20 | 154 | 7.1 | -89.39 | -47.05 | -89.42 | 2130 |
| 83 | MFI reversion | reversion | 82.34 | -17.66 | 151 | 16.6 | -87.87 | -35.38 | -87.92 | 2175 |
| 84 | Connors RSI(2) | reversion | 81.72 | -18.28 | 196 | 17.3 | -96.40 | -41.56 | -96.40 | 3649 |
| 85 | Candlestick reversal | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.35 | -50.92 | -99.36 | 5561 |
| 86 | Stochastic reversion | reversion | 80.66 | -19.34 | 245 | 24.5 | -95.85 | -46.70 | -95.86 | 4054 |
| 87 | EMA 9/21 cross | trend | 79.78 | -20.22 | 215 | 14.0 | -97.41 | -42.28 | -97.41 | 3551 |
| 88 | OBV trend | momentum | 79.51 | -20.49 | 212 | 13.2 | -95.80 | -49.19 | -95.80 | 3562 |
| 89 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.87 | -31.02 | -94.87 | 2674 |
| 90 | Bollinger reversion | reversion | 79.09 | -20.91 | 233 | 13.3 | -95.73 | -44.87 | -95.73 | 3675 |
| 91 | VWAP momentum | momentum | 77.76 | -22.24 | 278 | 9.7 | -98.47 | -36.23 | -98.47 | 5208 |
| 92 | Parabolic SAR | trend | 77.42 | -22.58 | 224 | 12.5 | -96.92 | -56.40 | -96.93 | 3651 |
| 93 | CCI reversion | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.46 | -51.84 | -98.46 | 4700 |
| 94 | MACD cross | trend | 76.35 | -23.65 | 177 | 8.5 | -99.70 | -65.14 | -99.70 | 6088 |
| 95 | Williams %R | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.52 | -60.51 | -99.52 | 6089 |
| 96 | Heikin-Ashi | trend | 75.44 | -24.56 | 190 | 3.2 | -99.89 | -84.54 | -99.89 | 8319 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T00:10 | AI bee: Bizzy | sell | XRP-USD | 13.47 | -0.08 | Jev: sell (buy p=0.27) |
| 2026-09-29T00:10 | VWAP momentum | buy | XRP-USD | 3.91 | — | rebalance up |
| 2026-09-29T00:10 | VWAP momentum | buy | SOL-USD | 3.90 | — | rebalance up |
| 2026-09-29T00:10 | VWAP momentum | buy | DOGE-USD | 3.89 | — | rebalance up |
| 2026-09-29T00:10 | VWAP momentum | sell | ETH-USD | 15.52 | -0.09 | exit signal |
| 2026-09-29T00:10 | MACD zero-line | buy | XRP-USD | 4.26 | — | rebalance up |
| 2026-09-29T00:10 | MACD zero-line | buy | SOL-USD | 4.27 | — | rebalance up |
| 2026-09-29T00:10 | MACD zero-line | buy | DOGE-USD | 8.48 | — | rebalance up |
| 2026-09-29T00:10 | MACD zero-line | sell | ETH-USD | 16.99 | -0.08 | exit signal |
| 2026-09-29T00:10 | MACD zero-line | sell | BTC-USD | 16.97 | -0.12 | exit signal |
| 2026-09-29T00:10 | MACD cross | buy | SOL-USD | 3.84 | — | rebalance up |
| 2026-09-29T00:10 | MACD cross | sell | ETH-USD | 15.24 | -0.09 | exit signal |
| 2026-09-29T00:10 | MACD cross | sell | BTC-USD | 15.24 | -0.09 | exit signal |
| 2026-09-29T00:09 | AI bee: Boozy | buy | XRP-USD | 24.36 | — | Jev: buy (buy p=0.52) |
| 2026-09-29T00:09 | AI bee: Boozy | sell | ETH-USD | 32.18 | -0.21 | Jev: sell (buy p=0.28) |
| 2026-09-29T00:09 | AI bee: Bizzy | buy | XRP-USD | 13.55 | — | Jev: buy (buy p=0.58) |
| 2026-09-29T00:09 | AI bee: Bizzy | buy | DOGE-USD | 18.69 | — | Jev: buy (buy p=0.80) |
| 2026-09-29T00:08 | AI bee: Bizzy | sell | XRP-USD | 16.76 | -0.10 | Jev: sell (buy p=0.03) |
| 2026-09-29T00:07 | AI bee: Boozy | buy | ETH-USD | 32.39 | — | Jev: buy (buy p=0.69) |
| 2026-09-29T00:07 | AI bee: Boozy | sell | XRP-USD | 29.51 | -0.12 | Jev: buy (buy p=0.68) |
| 2026-09-29T00:07 | AI bee: Bizzy | sell | DOGE-USD | 20.03 | -0.11 | Jev: sell (buy p=0.41) |
| 2026-09-29T00:07 | VWAP momentum | buy | XRP-USD | 7.76 | — | rebalance up |
| 2026-09-29T00:07 | VWAP momentum | sell | ETH-USD | 3.89 | -0.02 | rebalance down |
| 2026-09-29T00:07 | VWAP momentum | sell | BTC-USD | 3.89 | -0.02 | rebalance down |
| 2026-09-29T00:07 | Triple EMA stack | buy | SOL-USD | 8.36 | — | rebalance up |
| 2026-09-29T00:07 | Triple EMA stack | sell | XRP-USD | 4.18 | -0.02 | rebalance down |
| 2026-09-29T00:07 | Triple EMA stack | sell | ETH-USD | 4.18 | -0.02 | rebalance down |
| 2026-09-29T00:05 | AI bee: Bizzy | buy | XRP-USD | 16.86 | — | Jev: buy (buy p=0.72) |
| 2026-09-29T00:05 | AI bee: Bizzy | buy | DOGE-USD | 20.14 | — | Jev: buy (buy p=0.86) |
| 2026-09-29T00:05 | VWAP reversion | sell | SOL-USD | 21.34 | -0.14 | exit signal |
| 2026-09-29T00:05 | Donchian 20/10 | buy | DOGE-USD | 4.17 | — | rebalance up |
| 2026-09-29T00:05 | Donchian 20/10 | sell | XRP-USD | 4.17 | -0.02 | rebalance down |
| 2026-09-29T00:05 | ROC + volume | sell | SOL-USD | 22.25 | -0.09 | exit signal |
| 2026-09-29T00:05 | ROC + volume | sell | ETH-USD | 22.25 | -0.15 | exit signal |
| 2026-09-29T00:05 | VWAP momentum | buy | XRP-USD | 7.85 | — | entry signal |
| 2026-09-29T00:05 | VWAP momentum | buy | SOL-USD | 15.60 | — | entry signal |
| 2026-09-29T00:05 | VWAP momentum | buy | DOGE-USD | 15.60 | — | entry signal |
| 2026-09-29T00:05 | Trend pullback | buy | ETH-USD | 20.89 | — | entry signal |
| 2026-09-29T00:05 | MACD zero-line | sell | XRP-USD | 4.26 | -0.02 | rebalance down |
| 2026-09-29T00:05 | Triple EMA stack | buy | SOL-USD | 4.26 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
