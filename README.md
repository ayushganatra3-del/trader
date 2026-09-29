# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T09:40:05.000170+00:00 · 5554 ticks

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

Today: 7135 decisions in 1427 calls, $0.0998 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T09:40 | 3 / 2 / 0 | SOL-USD 16%, DOGE-USD 16%, XRP-USD 14% |  |
| Breezy | 2026-09-29T09:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T09:40 | 5 / 0 / 0 | SOL-USD 40%, DOGE-USD 38% |  |

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
| 3 | Hold BTC | benchmark | 100.40 | 0.40 | 0 | — | 29.58 | 3.72 | -8.68 | 1 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | RSI(14) reversion · 1h | reversion | 99.99 | -0.01 | 3 | 100.0 | 13.15 | 2.73 | -6.57 | 142 |
| 11 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.80 | -0.20 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.79 | -0.21 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.58 | -0.41 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 17 | Daily: Bullish score | daily | 99.30 | -0.70 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Z-score reversion · 1h | reversion | 99.19 | -0.81 | 6 | 50.0 | 4.35 | 1.06 | -8.60 | 154 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.14 | -0.85 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.13 | -0.87 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Connors RSI(2) · 1h | reversion | 99.11 | -0.89 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 23 | Stochastic reversion · 1h | reversion | 99.10 | -0.90 | 25 | 56.0 | -12.25 | -2.72 | -13.73 | 324 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.04 | -0.96 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | CCI reversion · 1h | reversion | 98.66 | -1.34 | 26 | 38.5 | 1.59 | 0.43 | -12.41 | 405 |
| 27 | Williams %R · 1h | reversion | 98.66 | -1.34 | 33 | 51.5 | -17.89 | -3.29 | -19.48 | 485 |
| 28 | Copy: Insider buying | copy | 98.62 | -1.38 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.15 | -2.52 | -11.75 | 234 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.22 | -1.78 | 13 | 23.1 | -25.95 | -6.07 | -26.45 | 493 |
| 32 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 98.14 | -1.86 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 34 | Supertrend · 1h | trend | 98.07 | -1.93 | 11 | 9.1 | 5.57 | 0.94 | -16.43 | 194 |
| 35 | Squeeze breakout · 1h | breakout | 97.96 | -2.04 | 7 | 14.3 | 16.27 | 2.86 | -6.26 | 94 |
| 36 | EMA 20/50 cross · 1h | trend | 97.91 | -2.09 | 8 | 12.5 | 15.59 | 1.87 | -14.36 | 126 |
| 37 | MACD cross · 1h | trend | 97.40 | -2.60 | 31 | 9.7 | -15.89 | -2.68 | -20.52 | 459 |
| 38 | Bollinger reversion · 1h | reversion | 97.38 | -2.62 | 19 | 31.6 | -17.68 | -4.91 | -17.77 | 306 |
| 39 | Donchian 55/20 · 1h | breakout | 97.27 | -2.73 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 40 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.20 | -2.80 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 42 | Agent (ML meta-label) | meta | 97.14 | -2.86 | 79 | 10.1 | 5.00 | 1.00 | -11.79 | 382 |
| 43 | Trend pullback · 1h | trend | 97.12 | -2.88 | 22 | 13.6 | -25.76 | -6.84 | -26.34 | 148 |
| 44 | Parabolic SAR · 1h | trend | 96.96 | -3.04 | 20 | 15.0 | -5.69 | -0.65 | -18.82 | 304 |
| 45 | Bollinger breakout · 1h | breakout | 96.87 | -3.13 | 13 | 7.7 | 13.23 | 1.88 | -9.85 | 285 |
| 46 | Max aggression: 5-day momentum | meta | 96.56 | -3.44 | 1 | 0.0 | 0.08 | 0.36 | -29.56 | 29 |
| 47 | MACD zero-line · 1h | trend | 96.47 | -3.53 | 15 | 6.7 | -3.29 | -0.28 | -14.64 | 219 |
| 48 | RSI momentum · 1h | momentum | 96.44 | -3.56 | 20 | 5.0 | 1.54 | 0.41 | -15.29 | 213 |
| 49 | Triple EMA stack · 1h | trend | 95.98 | -4.02 | 24 | 8.3 | -2.85 | -0.13 | -22.95 | 224 |
| 50 | EMA 9/21 cross · 1h | trend | 95.88 | -4.12 | 34 | 11.8 | 2.96 | 0.60 | -16.92 | 314 |
| 51 | ADX DI cross · 1h | trend | 95.88 | -4.12 | 25 | 8.0 | -11.52 | -2.16 | -15.39 | 250 |
| 52 | MFI reversion · 1h | reversion | 95.87 | -4.13 | 38 | 13.2 | -9.16 | -1.67 | -17.20 | 125 |
| 53 | Ichimoku · 1h | trend | 95.87 | -4.13 | 11 | 9.1 | 8.06 | 1.13 | -15.13 | 121 |
| 54 | Donchian 20/10 · 1h | breakout | 95.83 | -4.17 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 55 | Max aggression: 1-day momentum | meta | 95.63 | -4.38 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 56 | Three white soldiers | momentum | 95.57 | -4.43 | 41 | 19.5 | -51.86 | -28.66 | -52.21 | 626 |
| 57 | OBV trend · 1h | momentum | 95.41 | -4.59 | 47 | 6.4 | -9.64 | -1.01 | -25.24 | 318 |
| 58 | VWAP momentum · 1h | momentum | 95.38 | -4.62 | 82 | 7.3 | -31.82 | -4.69 | -34.09 | 1251 |
| 59 | Volume breakout · 1h | breakout | 95.18 | -4.82 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.13 | -4.87 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 94.21 | -5.79 | 35 | 11.4 | -22.76 | -3.40 | -29.64 | 683 |
| 62 | ROC + volume · 1h | momentum | 91.92 | -8.08 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.34 | -22.11 | -71.42 | 1476 |
| 64 | Squeeze breakout | breakout | 89.38 | -10.62 | 74 | 6.8 | -60.15 | -18.90 | -60.45 | 1185 |
| 65 | ROC + volume | momentum | 89.18 | -10.82 | 120 | 17.5 | -71.83 | -17.84 | -72.43 | 1656 |
| 66 | Donchian 55/20 | breakout | 89.00 | -11.00 | 79 | 11.4 | -68.28 | -15.78 | -68.56 | 1330 |
| 67 | Volume breakout | breakout | 88.47 | -11.53 | 81 | 12.3 | -62.25 | -20.44 | -62.47 | 908 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | EMA 20/50 cross | trend | 88.11 | -11.89 | 97 | 13.4 | -78.84 | -17.74 | -79.37 | 1487 |
| 70 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 71 | Ichimoku | trend | 87.49 | -12.51 | 90 | 8.9 | -80.33 | -26.15 | -80.34 | 1756 |
| 72 | Keltner breakout | breakout | 87.35 | -12.65 | 125 | 10.4 | -84.82 | -34.90 | -84.97 | 1927 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.50 | -28.17 | -84.57 | 2081 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -71.44 | -17.71 | -71.75 | 1424 |
| 75 | Supertrend | trend | 84.33 | -15.67 | 146 | 15.8 | -87.16 | -24.52 | -87.53 | 1961 |
| 76 | MACD zero-line | trend | 83.74 | -16.27 | 159 | 15.1 | -91.61 | -36.37 | -91.78 | 2366 |
| 77 | Donchian 20/10 | breakout | 82.94 | -17.06 | 165 | 16.4 | -90.84 | -30.08 | -91.02 | 2686 |
| 78 | Trend pullback | trend | 82.87 | -17.13 | 141 | 15.6 | -90.54 | -33.83 | -90.55 | 2286 |
| 79 | Bollinger breakout | breakout | 82.57 | -17.43 | 170 | 14.7 | -93.96 | -42.35 | -94.06 | 2877 |
| 80 | Triple EMA stack | trend | 82.46 | -17.54 | 175 | 14.3 | -92.93 | -37.06 | -93.07 | 2623 |
| 81 | RSI momentum | momentum | 82.45 | -17.55 | 157 | 10.8 | -90.45 | -30.36 | -90.63 | 2404 |
| 82 | MFI reversion | reversion | 82.12 | -17.88 | 153 | 17.0 | -87.79 | -34.85 | -87.92 | 2169 |
| 83 | ADX DI cross | trend | 81.41 | -18.59 | 167 | 6.6 | -89.35 | -47.93 | -89.50 | 2125 |
| 84 | Connors RSI(2) | reversion | 80.42 | -19.58 | 207 | 16.4 | -96.39 | -41.47 | -96.39 | 3655 |
| 85 | Consensus | meta | 79.03 | -20.97 | 162 | 7.4 | -94.77 | -30.60 | -94.78 | 2668 |
| 86 | EMA 9/21 cross | trend | 79.00 | -21.00 | 227 | 15.0 | -97.37 | -42.35 | -97.43 | 3545 |
| 87 | Candlestick reversal | reversion | 78.54 | -21.46 | 202 | 13.9 | -99.36 | -53.12 | -99.36 | 5566 |
| 88 | Stochastic reversion | reversion | 78.23 | -21.77 | 260 | 23.1 | -95.92 | -48.92 | -95.93 | 4054 |
| 89 | OBV trend | momentum | 77.99 | -22.02 | 228 | 13.6 | -95.75 | -50.02 | -95.86 | 3560 |
| 90 | Bollinger reversion | reversion | 76.89 | -23.11 | 249 | 12.4 | -95.77 | -46.86 | -95.77 | 3675 |
| 91 | VWAP momentum | momentum | 75.55 | -24.45 | 301 | 9.0 | -98.45 | -37.04 | -98.46 | 5210 |
| 92 | CCI reversion | reversion | 75.15 | -24.86 | 177 | 5.6 | -98.45 | -53.16 | -98.46 | 4701 |
| 93 | Parabolic SAR | trend | 74.54 | -25.46 | 249 | 13.3 | -96.96 | -58.98 | -96.99 | 3664 |
| 94 | Williams %R | reversion | 73.81 | -26.19 | 259 | 19.3 | -99.52 | -63.19 | -99.53 | 6092 |
| 95 | MACD cross | trend | 73.78 | -26.22 | 202 | 10.9 | -99.70 | -68.18 | -99.70 | 6099 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.32 | -99.89 | 8332 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T09:40 | MFI reversion | buy | ETH-USD | 20.54 | — | entry signal |
| 2026-09-29T09:40 | Williams %R | sell | XRP-USD | 18.47 | -0.04 | exit signal |
| 2026-09-29T09:40 | Williams %R | sell | SOL-USD | 18.44 | -0.06 | exit signal |
| 2026-09-29T09:40 | Stochastic reversion | sell | XRP-USD | 19.58 | -0.03 | exit signal |
| 2026-09-29T09:40 | MACD zero-line | buy | XRP-USD | 20.95 | — | entry signal |
| 2026-09-29T09:40 | MACD cross | buy | SOL-USD | 18.47 | — | entry signal |
| 2026-09-29T09:40 | MACD cross | buy | DOGE-USD | 18.47 | — | entry signal |
| 2026-09-29T09:40 | Triple EMA stack | buy | XRP-USD | 20.63 | — | entry signal |
| 2026-09-29T09:40 | EMA 9/21 cross | buy | XRP-USD | 19.77 | — | entry signal |
| 2026-09-29T09:35 | CCI reversion | buy | ETH-USD | 14.99 | — | rebalance up |
| 2026-09-29T09:35 | CCI reversion | sell | DOGE-USD | 15.01 | -0.04 | exit signal |
| 2026-09-29T09:35 | Williams %R | buy | ETH-USD | 18.48 | — | entry signal |
| 2026-09-29T09:35 | Williams %R | buy | BTC-USD | 18.51 | — | entry signal |
| 2026-09-29T09:35 | Williams %R | sell | DOGE-USD | 18.49 | -0.01 | exit signal |
| 2026-09-29T09:35 | Bollinger reversion | sell | XRP-USD | 19.24 | -0.04 | exit signal |
| 2026-09-29T09:35 | Bollinger reversion | sell | BTC-USD | 19.19 | -0.09 | exit signal |
| 2026-09-29T09:35 | Connors RSI(2) | sell | ETH-USD | 20.05 | -0.11 | exit signal |
| 2026-09-29T09:35 | Bollinger breakout | buy | DOGE-USD | 20.65 | — | entry signal |
| 2026-09-29T09:35 | OBV trend | buy | BTC-USD | 19.50 | — | entry signal |
| 2026-09-29T09:35 | RSI momentum | buy | SOL-USD | 20.62 | — | entry signal |
| 2026-09-29T09:35 | Trend pullback | buy | ETH-USD | 12.45 | — | entry signal |
| 2026-09-29T09:35 | Trend pullback | buy | BTC-USD | 16.59 | — | entry signal |
| 2026-09-29T09:35 | Trend pullback | sell | SOL-USD | 4.16 | -0.02 | rebalance down |
| 2026-09-29T09:35 | Trend pullback | sell | DOGE-USD | 4.22 | -0.01 | rebalance down |
| 2026-09-29T09:35 | Ichimoku | buy | DOGE-USD | 21.88 | — | entry signal |
| 2026-09-29T09:35 | Parabolic SAR | buy | XRP-USD | 18.66 | — | entry signal |
| 2026-09-29T09:35 | Parabolic SAR | buy | SOL-USD | 18.66 | — | entry signal |
| 2026-09-29T09:35 | Parabolic SAR | buy | BTC-USD | 18.66 | — | entry signal |
| 2026-09-29T09:35 | MACD cross | buy | XRP-USD | 18.48 | — | entry signal |
| 2026-09-29T09:35 | Triple EMA stack | buy | SOL-USD | 20.64 | — | entry signal |
| 2026-09-29T09:35 | EMA 9/21 cross | buy | SOL-USD | 19.77 | — | entry signal |
| 2026-09-29T09:31 | Heikin-Ashi | sell | XRP-USD | 17.63 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-29T09:31 | Heikin-Ashi | sell | SOL-USD | 17.63 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-29T09:30 | Consensus | buy | ETH-USD | 19.76 | — | entry |
| 2026-09-29T09:30 | CCI reversion | buy | ETH-USD | 3.82 | — | entry signal |
| 2026-09-29T09:30 | CCI reversion | sell | DOGE-USD | 3.74 | -0.02 | rebalance down |
| 2026-09-29T09:30 | Bollinger reversion | sell | SOL-USD | 19.18 | -0.10 | exit signal |
| 2026-09-29T09:30 | Heikin-Ashi | buy | XRP-USD | 17.74 | — | entry signal |
| 2026-09-29T09:30 | Heikin-Ashi | buy | SOL-USD | 17.74 | — | entry signal |
| 2026-09-29T09:25 | CCI reversion | buy | BTC-USD | 18.77 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
