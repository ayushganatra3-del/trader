# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T09:10:05.000146+00:00 · 5526 ticks

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

Today: 6715 decisions in 1343 calls, $0.0940 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T09:10 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-09-29T09:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T09:10 | 1 / 4 / 0 | ETH-USD 22% |  |

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
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 6 | Hold BTC | benchmark | 100.16 | 0.17 | 0 | — | 29.29 | 3.69 | -8.68 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 11 | RSI(14) reversion · 1h | reversion | 99.87 | -0.13 | 3 | 100.0 | 12.99 | 2.70 | -6.57 | 142 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.83 | -0.17 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.81 | -0.18 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.61 | -0.39 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 16 | Daily: Bullish score | daily | 99.32 | -0.68 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 17 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 99.17 | -0.83 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 99.15 | -0.85 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 21 | Connors RSI(2) · 1h | reversion | 99.13 | -0.87 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 22 | Stochastic reversion · 1h | reversion | 99.12 | -0.88 | 25 | 56.0 | -12.34 | -2.73 | -13.81 | 324 |
| 23 | Z-score reversion · 1h | reversion | 99.11 | -0.89 | 6 | 50.0 | 4.24 | 1.04 | -8.60 | 154 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.06 | -0.94 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | Williams %R · 1h | reversion | 98.68 | -1.32 | 33 | 51.5 | -17.91 | -3.29 | -19.50 | 485 |
| 27 | Copy: Insider buying | copy | 98.64 | -1.36 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 28 | CCI reversion · 1h | reversion | 98.64 | -1.36 | 26 | 38.5 | 1.52 | 0.42 | -12.41 | 405 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.15 | -2.52 | -11.75 | 234 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Candlestick reversal · 1h | reversion | 98.17 | -1.83 | 13 | 23.1 | -26.01 | -6.09 | -26.46 | 493 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 98.16 | -1.84 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 34 | Supertrend · 1h | trend | 98.04 | -1.96 | 11 | 9.1 | 5.52 | 0.93 | -16.43 | 194 |
| 35 | Squeeze breakout · 1h | breakout | 97.92 | -2.08 | 7 | 14.3 | 15.80 | 2.78 | -6.26 | 95 |
| 36 | EMA 20/50 cross · 1h | trend | 97.91 | -2.09 | 8 | 12.5 | 15.57 | 1.86 | -14.36 | 126 |
| 37 | Bollinger reversion · 1h | reversion | 97.40 | -2.60 | 19 | 31.6 | -17.70 | -4.92 | -17.79 | 306 |
| 38 | Donchian 55/20 · 1h | breakout | 97.29 | -2.71 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.22 | -2.78 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | MACD cross · 1h | trend | 97.19 | -2.81 | 31 | 9.7 | -16.10 | -2.72 | -20.52 | 459 |
| 42 | Agent (ML meta-label) | meta | 97.15 | -2.85 | 79 | 10.1 | 3.89 | 0.83 | -11.02 | 384 |
| 43 | Trend pullback · 1h | trend | 97.13 | -2.87 | 22 | 13.6 | -25.76 | -6.84 | -26.34 | 148 |
| 44 | Parabolic SAR · 1h | trend | 96.87 | -3.13 | 20 | 15.0 | -5.87 | -0.68 | -18.82 | 304 |
| 45 | Bollinger breakout · 1h | breakout | 96.83 | -3.17 | 13 | 7.7 | 13.17 | 1.87 | -9.85 | 285 |
| 46 | RSI momentum · 1h | momentum | 96.41 | -3.60 | 20 | 5.0 | 1.48 | 0.40 | -15.29 | 213 |
| 47 | MACD zero-line · 1h | trend | 96.37 | -3.63 | 15 | 6.7 | -3.41 | -0.29 | -14.64 | 219 |
| 48 | Max aggression: 5-day momentum | meta | 96.04 | -3.96 | 1 | 0.0 | -0.48 | 0.31 | -29.56 | 29 |
| 49 | Triple EMA stack · 1h | trend | 95.95 | -4.05 | 24 | 8.3 | -2.91 | -0.13 | -22.95 | 224 |
| 50 | EMA 9/21 cross · 1h | trend | 95.86 | -4.14 | 34 | 11.8 | 2.74 | 0.57 | -16.92 | 314 |
| 51 | Donchian 20/10 · 1h | breakout | 95.84 | -4.16 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 52 | MFI reversion · 1h | reversion | 95.78 | -4.22 | 38 | 13.2 | -9.26 | -1.69 | -17.20 | 125 |
| 53 | Ichimoku · 1h | trend | 95.77 | -4.23 | 11 | 9.1 | 7.93 | 1.11 | -15.13 | 121 |
| 54 | ADX DI cross · 1h | trend | 95.69 | -4.31 | 25 | 8.0 | -11.71 | -2.20 | -15.39 | 250 |
| 55 | Max aggression: 1-day momentum | meta | 95.65 | -4.35 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 56 | Three white soldiers | momentum | 95.57 | -4.43 | 41 | 19.5 | -51.86 | -28.66 | -52.21 | 626 |
| 57 | OBV trend · 1h | momentum | 95.38 | -4.62 | 47 | 6.4 | -9.69 | -1.01 | -25.24 | 318 |
| 58 | VWAP momentum · 1h | momentum | 95.29 | -4.71 | 82 | 7.3 | -31.99 | -4.72 | -34.09 | 1251 |
| 59 | Volume breakout · 1h | breakout | 95.19 | -4.82 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.14 | -4.86 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 93.89 | -6.11 | 35 | 11.4 | -23.06 | -3.45 | -29.64 | 683 |
| 62 | ROC + volume · 1h | momentum | 91.94 | -8.06 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.22 | -22.00 | -71.30 | 1473 |
| 64 | Squeeze breakout | breakout | 89.38 | -10.62 | 74 | 6.8 | -60.14 | -18.89 | -60.44 | 1185 |
| 65 | ROC + volume | momentum | 89.18 | -10.82 | 120 | 17.5 | -71.83 | -17.84 | -72.43 | 1656 |
| 66 | Donchian 55/20 | breakout | 88.73 | -11.27 | 79 | 11.4 | -68.40 | -15.87 | -68.56 | 1330 |
| 67 | Volume breakout | breakout | 88.47 | -11.53 | 81 | 12.3 | -62.25 | -20.44 | -62.47 | 908 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | EMA 20/50 cross | trend | 87.80 | -12.20 | 97 | 13.4 | -78.90 | -17.81 | -79.32 | 1487 |
| 71 | Ichimoku | trend | 87.53 | -12.46 | 90 | 8.9 | -80.32 | -26.13 | -80.34 | 1755 |
| 72 | Keltner breakout | breakout | 87.35 | -12.65 | 125 | 10.4 | -84.82 | -34.90 | -84.97 | 1927 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.55 | -28.29 | -84.62 | 2084 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -71.35 | -17.63 | -71.75 | 1422 |
| 75 | Supertrend | trend | 84.13 | -15.87 | 146 | 15.8 | -87.20 | -24.61 | -87.53 | 1961 |
| 76 | MACD zero-line | trend | 83.80 | -16.20 | 159 | 15.1 | -91.60 | -36.33 | -91.77 | 2365 |
| 77 | Donchian 20/10 | breakout | 82.75 | -17.25 | 165 | 16.4 | -90.87 | -30.20 | -91.02 | 2686 |
| 78 | Trend pullback | trend | 82.73 | -17.27 | 141 | 15.6 | -90.55 | -33.91 | -90.55 | 2283 |
| 79 | Bollinger breakout | breakout | 82.61 | -17.39 | 170 | 14.7 | -93.95 | -42.32 | -94.06 | 2876 |
| 80 | Triple EMA stack | trend | 82.44 | -17.56 | 175 | 14.3 | -92.93 | -37.07 | -93.07 | 2621 |
| 81 | RSI momentum | momentum | 82.40 | -17.60 | 157 | 10.8 | -90.45 | -30.37 | -90.63 | 2403 |
| 82 | MFI reversion | reversion | 82.06 | -17.94 | 153 | 17.0 | -87.80 | -34.91 | -87.92 | 2168 |
| 83 | ADX DI cross | trend | 81.43 | -18.57 | 167 | 6.6 | -89.39 | -48.28 | -89.49 | 2126 |
| 84 | Connors RSI(2) | reversion | 80.45 | -19.55 | 206 | 16.5 | -96.39 | -41.45 | -96.39 | 3655 |
| 85 | Consensus | meta | 79.04 | -20.96 | 162 | 7.4 | -94.77 | -30.60 | -94.77 | 2667 |
| 86 | EMA 9/21 cross | trend | 79.01 | -20.99 | 227 | 15.0 | -97.37 | -42.36 | -97.43 | 3543 |
| 87 | Candlestick reversal | reversion | 78.46 | -21.54 | 202 | 13.9 | -99.35 | -53.03 | -99.35 | 5561 |
| 88 | Stochastic reversion | reversion | 78.18 | -21.82 | 258 | 23.3 | -95.94 | -49.14 | -95.94 | 4055 |
| 89 | OBV trend | momentum | 77.90 | -22.10 | 228 | 13.6 | -95.76 | -50.19 | -95.85 | 3558 |
| 90 | Bollinger reversion | reversion | 76.88 | -23.12 | 246 | 12.6 | -95.79 | -47.01 | -95.79 | 3678 |
| 91 | VWAP momentum | momentum | 75.23 | -24.77 | 301 | 9.0 | -98.45 | -37.11 | -98.46 | 5208 |
| 92 | CCI reversion | reversion | 75.04 | -24.96 | 176 | 5.7 | -98.47 | -53.54 | -98.47 | 4701 |
| 93 | Parabolic SAR | trend | 74.66 | -25.34 | 249 | 13.3 | -96.96 | -59.07 | -96.98 | 3661 |
| 94 | MACD cross | trend | 73.93 | -26.07 | 202 | 10.9 | -99.70 | -68.10 | -99.70 | 6096 |
| 95 | Williams %R | reversion | 73.77 | -26.23 | 256 | 19.5 | -99.53 | -63.86 | -99.53 | 6095 |
| 96 | Heikin-Ashi | trend | 70.94 | -29.05 | 231 | 3.5 | -99.89 | -92.25 | -99.89 | 8329 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T09:10 | Consensus | sell | ETH-USD | 19.65 | -0.15 | target is flat |
| 2026-09-29T09:10 | RSI momentum | sell | ETH-USD | 16.52 | 0.08 | exit signal |
| 2026-09-29T09:10 | Triple EMA stack | sell | ETH-USD | 20.63 | 0.10 | exit signal |
| 2026-09-29T09:10 | EMA 9/21 cross | sell | ETH-USD | 15.81 | 0.12 | exit signal |
| 2026-09-29T09:05 | CCI reversion | buy | XRP-USD | 18.79 | — | entry signal |
| 2026-09-29T09:00 | Consensus | buy | ETH-USD | 19.80 | — | entry |
| 2026-09-29T09:00 | Candlestick reversal · 1h | buy | DOGE-USD | 6.94 | — | rebalance up |
| 2026-09-29T09:00 | Candlestick reversal · 1h | sell | XRP-USD | 8.26 | 0.10 | exit signal |
| 2026-09-29T09:00 | OBV trend · 1h | buy | ETH-USD | 23.87 | — | entry signal |
| 2026-09-29T09:00 | Parabolic SAR · 1h | buy | BTC-USD | 5.37 | — | entry signal |
| 2026-09-29T09:00 | Parabolic SAR · 1h | sell | DOGE-USD | 5.37 | -0.02 | rebalance down |
| 2026-09-29T09:00 | MACD zero-line · 1h | buy | BTC-USD | 24.13 | — | entry signal |
| 2026-09-29T09:00 | Triple EMA stack · 1h | buy | ETH-USD | 23.77 | — | entry signal |
| 2026-09-29T09:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 9.80 | — | entry signal |
| 2026-09-29T09:00 | MFI reversion | buy | XRP-USD | 20.54 | — | entry signal |
| 2026-09-29T09:00 | Stochastic reversion | buy | ETH-USD | 19.58 | — | entry signal |
| 2026-09-29T09:00 | Connors RSI(2) | sell | XRP-USD | 20.09 | -0.13 | exit signal |
| 2026-09-29T09:00 | Connors RSI(2) | sell | SOL-USD | 20.09 | -0.11 | exit signal |
| 2026-09-29T09:00 | Connors RSI(2) | sell | BTC-USD | 20.08 | -0.11 | exit signal |
| 2026-09-29T09:00 | Candlestick reversal | buy | BTC-USD | 19.63 | — | entry signal |
| 2026-09-29T08:55 | Connors RSI(2) | buy | ETH-USD | 20.16 | — | entry signal |
| 2026-09-29T08:55 | Candlestick reversal | sell | BTC-USD | 19.54 | -0.13 | exit signal |
| 2026-09-29T08:55 | Donchian 20/10 | sell | ETH-USD | 16.56 | 0.10 | exit signal |
| 2026-09-29T08:55 | RSI momentum | sell | SOL-USD | 20.58 | -0.04 | exit signal |
| 2026-09-29T08:55 | Supertrend | sell | ETH-USD | 16.84 | 0.10 | exit signal |
| 2026-09-29T08:55 | EMA 9/21 cross | sell | SOL-USD | 15.86 | 0.09 | exit signal |
| 2026-09-29T08:55 | EMA 9/21 cross | sell | BTC-USD | 15.80 | 0.04 | exit signal |
| 2026-09-29T08:50 | CCI reversion | buy | DOGE-USD | 18.81 | — | entry signal |
| 2026-09-29T08:50 | Stochastic reversion | buy | XRP-USD | 19.61 | — | entry signal |
| 2026-09-29T08:50 | Stochastic reversion | buy | BTC-USD | 19.61 | — | entry signal |
| 2026-09-29T08:50 | Bollinger reversion | buy | XRP-USD | 19.28 | — | entry signal |
| 2026-09-29T08:50 | Bollinger reversion | buy | SOL-USD | 19.28 | — | entry signal |
| 2026-09-29T08:50 | Bollinger reversion | buy | BTC-USD | 19.28 | — | entry signal |
| 2026-09-29T08:50 | Candlestick reversal | buy | BTC-USD | 19.67 | — | entry signal |
| 2026-09-29T08:45 | Connors RSI(2) | buy | SOL-USD | 20.20 | — | entry signal |
| 2026-09-29T08:45 | Connors RSI(2) | buy | BTC-USD | 20.20 | — | entry signal |
| 2026-09-29T08:45 | Donchian 55/20 | sell | BTC-USD | 22.15 | -0.03 | exit signal |
| 2026-09-29T08:45 | OBV trend | sell | BTC-USD | 19.38 | 0.02 | exit signal |
| 2026-09-29T08:45 | RSI momentum | buy | SOL-USD | 4.16 | — | rebalance up |
| 2026-09-29T08:45 | RSI momentum | sell | XRP-USD | 16.42 | -0.08 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
