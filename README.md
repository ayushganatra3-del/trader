# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T16:40:05.000150+00:00 · 4711 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.95 (-0.05%)

Closed trades 14, win rate 71.4%, fees £0.44, max drawdown -1.39%.

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

### Market regime (QQQ, 2026-09-25)

**Uptrend** since 2026-09-21 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 20.87 · VIX 14.87 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, COIN 8.0, MSFT 7.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 11282 decisions in 536 calls, $0.1340 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T16:40 | 1 / 12 / 17 | LABU 13% |  |
| Breezy | 2026-09-28T16:40 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-09-28T16:40 | 4 / 21 / 5 | MSTR 38%, LABU 30% |  |

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
| 1 | Agent (aggressive) | meta | 100.59 | 0.59 | 6 | 66.7 | 1.65 | 1.07 | -3.92 | 90 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.46 | 0.46 | 0 | — | 11.66 | 2.60 | -7.55 | 43 |
| 3 | Copy: Hedge-fund gurus (GURU) | copy | 100.31 | 0.31 | 0 | — | -0.21 | -0.05 | -5.14 | 1 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.10 | 0.10 | 4 | 50.0 | 2.26 | 1.18 | -2.47 | 91 |
| 5 | Hold BTC | benchmark | 100.06 | 0.06 | 0 | — | 31.61 | 3.95 | -8.68 | 1 |
| 6 | Copy: Congress Democrats (NANC) | copy | 100.03 | 0.03 | 0 | — | 7.44 | 2.82 | -3.62 | 1 |
| 7 | RSI(14) reversion · 1h | reversion | 100.01 | 0.01 | 1 | 100.0 | 7.71 | 1.74 | -6.87 | 134 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 5.83 | 1.34 | -7.93 | 7 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | -0.41 | -0.62 | -1.49 | 18 |
| 12 | Daily: Bullish score | daily | 99.97 | -0.03 | 2 | 0.0 | -0.12 | 0.18 | -12.76 | 13 |
| 13 | Agent | meta | 99.95 | -0.05 | 14 | 71.4 | -9.51 | -6.42 | -10.68 | 203 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 99.86 | -0.14 | 0 | — | -1.02 | -0.62 | -7.65 | 1 |
| 15 | Daily: SMA 20/50 cross · AAPL | daily | 99.77 | -0.23 | 0 | — | -7.13 | -1.75 | -12.73 | 1 |
| 16 | Hold SPY | benchmark | 99.69 | -0.31 | 0 | — | 3.55 | 1.84 | -3.66 | 1 |
| 17 | Stochastic reversion · 1h | reversion | 99.43 | -0.57 | 21 | 52.4 | -9.99 | -2.17 | -12.43 | 324 |
| 18 | Opening range 30m | breakout | 99.41 | -0.59 | 15 | 13.3 | -7.55 | -2.19 | -13.54 | 554 |
| 19 | Connors RSI(2) · 1h | reversion | 99.41 | -0.59 | 33 | 54.5 | -11.72 | -3.75 | -13.49 | 243 |
| 20 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.35 | -0.65 | 0 | — | -5.62 | -1.68 | -12.40 | 25 |
| 21 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 22 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 23 | Timing: Nasdaq FTD · QQQ | daily | 99.23 | -0.77 | 0 | — | -3.40 | -2.14 | -5.09 | 2 |
| 24 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.44 | -5.16 | 27 |
| 25 | Copy: Insider buying | copy | 99.15 | -0.85 | 2 | 100.0 | -12.05 | -2.31 | -17.74 | 73 |
| 26 | Williams %R · 1h | reversion | 99.05 | -0.95 | 27 | 51.9 | -17.93 | -3.31 | -20.27 | 489 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 99.01 | -0.99 | 0 | — | 24.64 | 3.54 | -6.29 | 1 |
| 28 | Z-score reversion · 1h | reversion | 98.94 | -1.06 | 4 | 25.0 | 3.82 | 0.96 | -8.60 | 155 |
| 29 | CCI reversion · 1h | reversion | 98.94 | -1.06 | 21 | 28.6 | 0.67 | 0.28 | -12.41 | 414 |
| 30 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 31 | EMA 20/50 cross · 1h | trend | 98.61 | -1.39 | 8 | 12.5 | 17.19 | 2.04 | -14.36 | 124 |
| 32 | Candlestick reversal · 1h | reversion | 98.60 | -1.40 | 9 | 22.2 | -23.32 | -4.95 | -25.75 | 503 |
| 33 | Opening range 15m | breakout | 98.59 | -1.41 | 22 | 13.6 | -10.23 | -2.74 | -16.14 | 689 |
| 34 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.62 | -0.05 | -15.21 | 47 |
| 35 | Supertrend · 1h | trend | 98.33 | -1.67 | 11 | 9.1 | 10.06 | 1.49 | -16.43 | 196 |
| 36 | Squeeze breakout · 1h | breakout | 98.28 | -1.72 | 7 | 14.3 | 14.35 | 2.51 | -8.33 | 96 |
| 37 | Agent (rotation) | meta | 98.15 | -1.85 | 26 | 11.5 | -7.94 | -2.76 | -11.77 | 210 |
| 38 | Parabolic SAR · 1h | trend | 98.09 | -1.91 | 18 | 16.7 | -5.00 | -0.56 | -18.82 | 303 |
| 39 | MACD cross · 1h | trend | 98.02 | -1.98 | 26 | 11.5 | -15.06 | -2.55 | -21.04 | 456 |
| 40 | Trend pullback · 1h | trend | 97.83 | -2.17 | 21 | 14.3 | -25.44 | -6.93 | -26.81 | 152 |
| 41 | Bollinger reversion · 1h | reversion | 97.80 | -2.19 | 18 | 33.3 | -15.31 | -4.23 | -16.13 | 314 |
| 42 | Timing: Nasdaq FTD · TQQQ | daily | 97.79 | -2.21 | 0 | — | -10.93 | -2.31 | -15.27 | 2 |
| 43 | Donchian 55/20 · 1h | breakout | 97.73 | -2.27 | 8 | 0.0 | 5.29 | 0.90 | -16.96 | 113 |
| 44 | Agent (ML meta-label) | meta | 97.64 | -2.36 | 55 | 9.1 | 8.35 | 1.63 | -10.76 | 363 |
| 45 | MACD zero-line · 1h | trend | 97.23 | -2.77 | 13 | 7.7 | 0.32 | 0.24 | -14.64 | 223 |
| 46 | EMA 9/21 cross · 1h | trend | 97.18 | -2.82 | 30 | 13.3 | 4.70 | 0.84 | -16.92 | 306 |
| 47 | Bollinger breakout · 1h | breakout | 97.04 | -2.96 | 13 | 7.7 | 12.78 | 1.83 | -10.45 | 284 |
| 48 | Triple EMA stack · 1h | trend | 97.01 | -2.99 | 22 | 9.1 | -3.55 | -0.22 | -22.96 | 226 |
| 49 | RSI momentum · 1h | momentum | 96.80 | -3.20 | 20 | 5.0 | 4.07 | 0.77 | -15.29 | 213 |
| 50 | Three white soldiers | momentum | 96.62 | -3.38 | 29 | 13.8 | -51.93 | -28.42 | -51.94 | 622 |
| 51 | ADX DI cross · 1h | trend | 96.57 | -3.43 | 22 | 9.1 | -12.62 | -2.43 | -16.78 | 253 |
| 52 | Max aggression: 1-day momentum | meta | 96.56 | -3.44 | 1 | 0.0 | -31.28 | -1.75 | -49.41 | 42 |
| 53 | Ichimoku · 1h | trend | 96.55 | -3.45 | 10 | 10.0 | 9.20 | 1.26 | -15.13 | 119 |
| 54 | Max aggression: 5-day momentum | meta | 96.31 | -3.69 | 1 | 0.0 | -0.03 | 0.35 | -29.56 | 29 |
| 55 | VWAP momentum · 1h | momentum | 96.18 | -3.82 | 74 | 6.8 | -33.45 | -5.01 | -33.98 | 1256 |
| 56 | MFI reversion · 1h | reversion | 95.96 | -4.04 | 37 | 10.8 | -9.53 | -1.77 | -17.27 | 126 |
| 57 | Donchian 20/10 · 1h | breakout | 95.86 | -4.14 | 12 | 16.7 | 14.10 | 1.94 | -12.78 | 213 |
| 58 | Heikin-Ashi · 1h | trend | 95.79 | -4.21 | 27 | 14.8 | -23.66 | -3.61 | -28.06 | 682 |
| 59 | OBV trend · 1h | momentum | 95.73 | -4.27 | 46 | 6.5 | -8.16 | -0.81 | -25.24 | 328 |
| 60 | Volume breakout · 1h | breakout | 95.41 | -4.59 | 25 | 4.0 | 6.55 | 1.10 | -12.60 | 126 |
| 61 | Keltner breakout · 1h | breakout | 95.36 | -4.64 | 7 | 0.0 | -0.98 | 0.08 | -18.68 | 219 |
| 62 | AI bee: Bizzy | ai | 94.54 | -5.46 | 142 | 17.6 | — | — | — | — |
| 63 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 92.93 | -7.07 | 78 | 34.6 | -71.51 | -22.28 | -71.84 | 1485 |
| 65 | ROC + volume · 1h | momentum | 92.51 | -7.49 | 41 | 4.9 | -3.33 | -0.27 | -17.18 | 400 |
| 66 | Squeeze breakout | breakout | 91.08 | -8.93 | 59 | 6.8 | -59.67 | -18.47 | -59.90 | 1189 |
| 67 | ROC + volume | momentum | 90.58 | -9.42 | 85 | 12.9 | -72.15 | -17.99 | -72.66 | 1658 |
| 68 | EMA 20/50 cross | trend | 90.45 | -9.55 | 72 | 15.3 | -78.45 | -17.70 | -78.54 | 1482 |
| 69 | Donchian 55/20 | breakout | 90.29 | -9.71 | 67 | 11.9 | -68.45 | -15.87 | -68.51 | 1330 |
| 70 | Volume breakout | breakout | 90.28 | -9.72 | 64 | 9.4 | -62.35 | -20.91 | -62.35 | 909 |
| 71 | Keltner breakout | breakout | 88.99 | -11.01 | 87 | 9.2 | -85.03 | -35.72 | -85.09 | 1929 |
| 72 | Ichimoku | trend | 88.83 | -11.17 | 80 | 8.8 | -80.50 | -26.52 | -80.52 | 1764 |
| 73 | Z-score reversion | reversion | 87.19 | -12.81 | 130 | 28.5 | -84.70 | -29.04 | -84.90 | 2102 |
| 74 | Supertrend | trend | 86.37 | -13.63 | 110 | 15.5 | -87.23 | -25.26 | -87.44 | 1981 |
| 75 | MACD zero-line | trend | 86.25 | -13.75 | 123 | 13.8 | -91.64 | -37.09 | -91.68 | 2374 |
| 76 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -70.86 | -17.47 | -71.87 | 1424 |
| 77 | RSI momentum | momentum | 85.85 | -14.15 | 114 | 13.2 | -90.42 | -30.18 | -90.43 | 2400 |
| 78 | Bollinger breakout | breakout | 85.81 | -14.19 | 119 | 10.9 | -93.94 | -42.92 | -93.99 | 2883 |
| 79 | Donchian 20/10 | breakout | 85.58 | -14.41 | 129 | 14.7 | -90.84 | -30.14 | -90.97 | 2697 |
| 80 | Triple EMA stack | trend | 85.26 | -14.74 | 141 | 12.8 | -93.03 | -37.06 | -93.05 | 2621 |
| 81 | Trend pullback | trend | 85.05 | -14.95 | 124 | 16.1 | -90.67 | -35.77 | -90.68 | 2296 |
| 82 | ADX DI cross | trend | 84.09 | -15.91 | 127 | 7.1 | -89.28 | -49.89 | -89.35 | 2123 |
| 83 | Connors RSI(2) | reversion | 83.91 | -16.09 | 166 | 17.5 | -96.38 | -43.19 | -96.38 | 3650 |
| 84 | MFI reversion | reversion | 83.58 | -16.42 | 135 | 15.6 | -87.99 | -37.97 | -88.12 | 2182 |
| 85 | Stochastic reversion | reversion | 82.42 | -17.58 | 206 | 24.8 | -95.93 | -49.73 | -95.96 | 4069 |
| 86 | EMA 9/21 cross | trend | 81.43 | -18.57 | 184 | 12.5 | -97.43 | -43.67 | -97.45 | 3562 |
| 87 | Consensus | meta | 81.24 | -18.76 | 134 | 6.0 | -94.91 | -31.94 | -94.91 | 2689 |
| 88 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.33 | -56.11 | -99.34 | 5569 |
| 89 | OBV trend | momentum | 81.07 | -18.93 | 182 | 12.1 | -95.79 | -51.09 | -95.81 | 3550 |
| 90 | Bollinger reversion | reversion | 79.72 | -20.28 | 218 | 13.8 | -95.81 | -46.87 | -95.84 | 3692 |
| 91 | VWAP momentum | momentum | 79.72 | -20.28 | 233 | 9.4 | -98.47 | -37.22 | -98.48 | 5231 |
| 92 | Parabolic SAR | trend | 79.48 | -20.52 | 197 | 12.2 | -96.87 | -59.80 | -96.90 | 3643 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.45 | -56.59 | -98.47 | 4712 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -75.31 | -99.70 | 6094 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.53 | -68.04 | -99.53 | 6099 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.88 | -104.53 | -99.89 | 8325 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T16:40 | AI bee: Bizzy | buy | LABU | 12.29 | — | Jev: buy (buy p=0.52) |
| 2026-09-28T16:40 | Consensus | buy | NVDA | 6.00 | — | rebalance up |
| 2026-09-28T16:40 | Consensus | buy | MSTR | 6.11 | — | rebalance up |
| 2026-09-28T16:40 | Consensus | buy | LABU | 6.01 | — | rebalance up |
| 2026-09-28T16:40 | Consensus | buy | BTC-USD | 6.09 | — | rebalance up |
| 2026-09-28T16:40 | Consensus | buy | AAPL | 6.08 | — | rebalance up |
| 2026-09-28T16:40 | Consensus | sell | SOL-USD | 10.05 | -0.10 | target is flat |
| 2026-09-28T16:40 | Consensus | sell | ETH-USD | 10.11 | -0.09 | target is flat |
| 2026-09-28T16:40 | Consensus | sell | DOGE-USD | 10.13 | -0.10 | target is flat |
| 2026-09-28T16:40 | Bollinger reversion | buy | SQQQ | 19.93 | — | entry signal |
| 2026-09-28T16:40 | Volume breakout | buy | BITX | 12.90 | — | entry |
| 2026-09-28T16:40 | Volume breakout | sell | TNA | 11.23 | -0.11 | target is flat |
| 2026-09-28T16:40 | Squeeze breakout | sell | TSLA | 22.67 | -0.08 | stop-loss |
| 2026-09-28T16:40 | Bollinger breakout | buy | META | 4.09 | — | entry |
| 2026-09-28T16:40 | Bollinger breakout | sell | TSLA | 4.74 | -0.01 | stop-loss |
| 2026-09-28T16:40 | Opening range 30m | sell | SPY | 3.05 | -0.01 | exit signal |
| 2026-09-28T16:40 | VWAP momentum | buy | SOXL | 3.21 | — | entry |
| 2026-09-28T16:40 | VWAP momentum | sell | AMD | 3.21 | -0.01 | exit signal |
| 2026-09-28T16:40 | EMA 20/50 cross | buy | MSTR | 5.34 | — | entry signal |
| 2026-09-28T16:40 | EMA 20/50 cross | sell | LABU | 5.34 | 0.13 | rebalance down |
| 2026-09-28T16:39 | AI bee: Bizzy | sell | SOXL | 12.69 | -0.09 | Jev: sell (buy p=0.13) |
| 2026-09-28T16:39 | AI bee: Bizzy | sell | LABU | 15.16 | 0.02 | Jev: sell (buy p=0.17) |
| 2026-09-28T16:39 | AI bee: Bizzy | sell | AMD | 14.89 | -0.02 | Jev: sell (buy p=0.15) |
| 2026-09-28T16:37 | AI bee: Bizzy | buy | SOXL | 12.78 | — | Jev: buy (buy p=0.54) |
| 2026-09-28T16:37 | AI bee: Bizzy | buy | AMD | 14.91 | — | Jev: buy (buy p=0.63) |
| 2026-09-28T16:35 | Agent (ML meta-label) | buy | QQQ | 1.92 | — | entry |
| 2026-09-28T16:35 | MFI reversion | buy | SQQQ | 20.92 | — | entry signal |
| 2026-09-28T16:35 | Three white soldiers | sell | TSLA | 24.07 | -0.11 | stop-loss |
| 2026-09-28T16:35 | Volume breakout | sell | BITX | 11.30 | -0.01 | target is flat |
| 2026-09-28T16:35 | VWAP momentum | buy | AMD | 3.22 | — | entry |
| 2026-09-28T16:35 | VWAP momentum | sell | AAPL | 3.22 | -0.00 | exit signal |
| 2026-09-28T16:35 | Triple EMA stack | buy | XRP-USD | 12.17 | — | entry signal |
| 2026-09-28T16:35 | Triple EMA stack | buy | SOL-USD | 12.22 | — | entry signal |
| 2026-09-28T16:35 | Triple EMA stack | sell | LABU | 5.15 | 0.13 | rebalance down |
| 2026-09-28T16:35 | Triple EMA stack | sell | ETH-USD | 4.82 | -0.01 | rebalance down |
| 2026-09-28T16:35 | Triple EMA stack | sell | DOGE-USD | 4.74 | -0.04 | rebalance down |
| 2026-09-28T16:35 | Triple EMA stack | sell | BTC-USD | 4.83 | -0.00 | rebalance down |
| 2026-09-28T16:35 | Triple EMA stack | sell | AAPL | 4.84 | -0.01 | rebalance down |
| 2026-09-28T16:35 | EMA 20/50 cross | buy | XRP-USD | 11.90 | — | entry signal |
| 2026-09-28T16:35 | EMA 20/50 cross | buy | SOL-USD | 10.33 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
