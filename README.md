# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T14:10:05.000168+00:00 · 4609 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.20 (+0.20%)

Closed trades 8, win rate 87.5%, fees £0.31, max drawdown -0.52%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 20.00 | -0.06 |
| ETHU | 20.03 | -0.01 |
| PLTR | 19.95 | -0.13 |

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

Today: 2574 decisions in 243 calls, $0.0322 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T14:10 | 1 / 8 / 20 | TNA 19% |  |
| Breezy | 2026-09-28T14:10 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-09-28T14:10 | 4 / 23 / 2 | TNA 36%, COIN 30% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.07 | 1.07 | 0 | — | 12.35 | 2.73 | -7.55 | 43 |
| 2 | Agent (aggressive) | meta | 100.37 | 0.37 | 3 | 66.7 | 4.63 | 2.33 | -3.92 | 86 |
| 3 | Copy: Hedge-fund gurus (GURU) | copy | 100.30 | 0.30 | 0 | — | -0.21 | -0.05 | -5.14 | 1 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.25 | 0.25 | 4 | 50.0 | 2.65 | 1.39 | -2.17 | 92 |
| 5 | Agent | meta | 100.20 | 0.20 | 8 | 87.5 | -8.21 | -5.24 | -9.99 | 202 |
| 6 | Copy: Warren Buffett (BRK-B) | copy | 100.15 | 0.15 | 0 | — | -0.68 | -0.49 | -7.65 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 9.97 | 1.34 | -7.93 | 7 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | 0.93 | 0.46 | -4.88 | 15 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | -0.41 | -0.62 | -1.49 | 18 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.99 | -0.01 | 0 | — | -5.97 | -1.70 | -12.73 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.97 | -0.03 | 0 | — | 3.65 | 1.10 | -6.57 | 119 |
| 14 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 0 | — | -6.08 | -1.74 | -12.40 | 25 |
| 15 | Copy: Congress Democrats (NANC) | copy | 99.78 | -0.22 | 0 | — | 6.85 | 2.69 | -3.62 | 1 |
| 16 | Hold SPY | benchmark | 99.72 | -0.28 | 0 | — | 3.79 | 1.86 | -3.66 | 1 |
| 17 | Hold BTC | benchmark | 99.62 | -0.38 | 0 | — | 31.27 | 3.88 | -8.68 | 1 |
| 18 | Daily: Bullish score | daily | 99.51 | -0.49 | 2 | 0.0 | -0.32 | 0.12 | -12.76 | 13 |
| 19 | Three white soldiers · 1h | momentum | 99.40 | -0.60 | 1 | 0.0 | -3.06 | -2.52 | -5.16 | 28 |
| 20 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 21 | Opening range 30m | breakout | 99.25 | -0.75 | 11 | 18.2 | -7.57 | -2.20 | -13.54 | 545 |
| 22 | Gap and go | momentum | 99.15 | -0.85 | 5 | 0.0 | 16.16 | 4.04 | -4.73 | 190 |
| 23 | Timing: Nasdaq FTD · QQQ | daily | 99.00 | -0.99 | 0 | — | -3.61 | -2.24 | -4.71 | 2 |
| 24 | Z-score reversion · 1h | reversion | 98.92 | -1.08 | 4 | 25.0 | 3.87 | 0.97 | -8.60 | 154 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.88 | -1.12 | 0 | — | 26.83 | 3.52 | -6.29 | 1 |
| 26 | Bollinger reversion · 1h | reversion | 98.79 | -1.21 | 17 | 35.3 | -14.55 | -4.06 | -15.93 | 306 |
| 27 | Parabolic SAR · 1h | trend | 98.77 | -1.23 | 8 | 37.5 | -2.28 | -0.15 | -18.82 | 302 |
| 28 | Williams %R · 1h | reversion | 98.75 | -1.25 | 22 | 54.5 | -18.84 | -3.47 | -21.04 | 492 |
| 29 | Copy: Insider buying | copy | 98.73 | -1.27 | 0 | — | -12.12 | -2.33 | -17.74 | 73 |
| 30 | Agent (rotation) | meta | 98.71 | -1.29 | 26 | 11.5 | -7.70 | -2.68 | -11.56 | 215 |
| 31 | Connors RSI(2) · 1h | reversion | 98.69 | -1.31 | 27 | 48.1 | -13.23 | -4.23 | -13.68 | 236 |
| 32 | Stochastic reversion · 1h | reversion | 98.57 | -1.43 | 18 | 44.4 | -10.13 | -2.21 | -11.99 | 324 |
| 33 | Candlestick reversal · 1h | reversion | 98.48 | -1.52 | 6 | 16.7 | -26.19 | -6.46 | -26.21 | 471 |
| 34 | Supertrend · 1h | trend | 98.45 | -1.55 | 7 | 14.3 | 5.37 | 0.92 | -16.43 | 194 |
| 35 | CCI reversion · 1h | reversion | 98.44 | -1.56 | 17 | 23.5 | -0.26 | 0.13 | -12.41 | 405 |
| 36 | EMA 20/50 cross · 1h | trend | 98.36 | -1.64 | 7 | 14.3 | 16.35 | 1.98 | -14.36 | 126 |
| 37 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.33 | -0.05 | -15.21 | 47 |
| 38 | Squeeze breakout · 1h | breakout | 98.25 | -1.75 | 7 | 14.3 | 16.08 | 2.72 | -8.48 | 99 |
| 39 | Opening range 15m | breakout | 98.24 | -1.76 | 20 | 15.0 | -10.44 | -2.80 | -16.14 | 681 |
| 40 | Trend pullback · 1h | trend | 98.04 | -1.96 | 14 | 21.4 | -26.04 | -7.13 | -26.42 | 152 |
| 41 | MACD cross · 1h | trend | 97.78 | -2.22 | 22 | 13.6 | -14.33 | -2.42 | -19.81 | 459 |
| 42 | Donchian 55/20 · 1h | breakout | 97.74 | -2.25 | 3 | 0.0 | 5.46 | 0.93 | -16.96 | 112 |
| 43 | Agent (ML meta-label) | meta | 97.56 | -2.44 | 35 | 0.0 | 9.53 | 1.83 | -12.28 | 367 |
| 44 | ADX DI cross · 1h | trend | 97.55 | -2.45 | 13 | 15.4 | -9.58 | -1.82 | -14.96 | 249 |
| 45 | MACD zero-line · 1h | trend | 97.47 | -2.53 | 11 | 9.1 | 1.54 | 0.42 | -14.64 | 223 |
| 46 | RSI momentum · 1h | momentum | 97.39 | -2.60 | 10 | 10.0 | 1.60 | 0.42 | -15.29 | 213 |
| 47 | Bollinger breakout · 1h | breakout | 97.23 | -2.77 | 13 | 7.7 | 15.11 | 2.09 | -10.99 | 282 |
| 48 | Heikin-Ashi · 1h | trend | 97.16 | -2.84 | 21 | 19.0 | -21.64 | -3.27 | -27.53 | 689 |
| 49 | Timing: Nasdaq FTD · TQQQ | daily | 97.13 | -2.87 | 0 | — | -11.52 | -2.41 | -14.11 | 2 |
| 50 | EMA 9/21 cross · 1h | trend | 96.98 | -3.02 | 24 | 16.7 | 5.88 | 0.99 | -16.92 | 314 |
| 51 | Triple EMA stack · 1h | trend | 96.95 | -3.05 | 16 | 12.5 | -1.96 | -0.01 | -22.96 | 228 |
| 52 | Three white soldiers | momentum | 96.73 | -3.27 | 28 | 14.3 | -51.84 | -28.14 | -51.85 | 621 |
| 53 | Ichimoku · 1h | trend | 96.63 | -3.37 | 9 | 11.1 | 9.31 | 1.27 | -15.13 | 117 |
| 54 | Donchian 20/10 · 1h | breakout | 96.52 | -3.48 | 9 | 22.2 | 13.46 | 1.89 | -12.78 | 212 |
| 55 | VWAP momentum · 1h | momentum | 96.48 | -3.52 | 62 | 6.5 | -34.02 | -5.10 | -34.29 | 1264 |
| 56 | OBV trend · 1h | momentum | 96.48 | -3.52 | 38 | 7.9 | -7.84 | -0.78 | -25.24 | 331 |
| 57 | Max aggression: 1-day momentum | meta | 96.45 | -3.54 | 1 | 0.0 | -31.35 | -1.75 | -49.41 | 42 |
| 58 | Max aggression: 5-day momentum | meta | 96.34 | -3.66 | 1 | 0.0 | 0.01 | 0.35 | -29.56 | 29 |
| 59 | AI bee: Bizzy | ai | 96.08 | -3.92 | 51 | 3.9 | — | — | — | — |
| 60 | MFI reversion · 1h | reversion | 95.65 | -4.36 | 36 | 11.1 | -10.00 | -1.86 | -17.27 | 126 |
| 61 | Volume breakout · 1h | breakout | 95.39 | -4.61 | 25 | 4.0 | 9.59 | 1.48 | -12.60 | 126 |
| 62 | Keltner breakout · 1h | breakout | 95.34 | -4.66 | 7 | 0.0 | -0.21 | 0.18 | -18.68 | 220 |
| 63 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 92.85 | -7.15 | 54 | 25.9 | -71.54 | -22.32 | -71.70 | 1465 |
| 65 | ROC + volume · 1h | momentum | 92.72 | -7.28 | 40 | 5.0 | 1.00 | 0.34 | -17.18 | 400 |
| 66 | EMA 20/50 cross | trend | 91.61 | -8.39 | 67 | 16.4 | -78.25 | -17.46 | -78.46 | 1481 |
| 67 | Squeeze breakout | breakout | 91.09 | -8.91 | 56 | 5.4 | -60.09 | -18.65 | -60.23 | 1185 |
| 68 | Donchian 55/20 | breakout | 90.81 | -9.19 | 60 | 10.0 | -68.30 | -15.74 | -68.45 | 1329 |
| 69 | Volume breakout | breakout | 90.61 | -9.39 | 62 | 8.1 | -62.19 | -20.87 | -62.19 | 902 |
| 70 | ROC + volume | momentum | 89.86 | -10.14 | 83 | 12.0 | -72.76 | -18.14 | -72.78 | 1647 |
| 71 | Ichimoku | trend | 88.90 | -11.10 | 77 | 6.5 | -80.41 | -26.45 | -80.51 | 1778 |
| 72 | Keltner breakout | breakout | 88.83 | -11.17 | 86 | 9.3 | -85.28 | -35.81 | -85.28 | 1924 |
| 73 | VWAP reversion | reversion | 87.06 | -12.94 | 92 | 15.2 | -71.02 | -17.46 | -71.74 | 1392 |
| 74 | RSI momentum | momentum | 86.80 | -13.20 | 108 | 13.0 | -90.39 | -29.81 | -90.47 | 2391 |
| 75 | Supertrend | trend | 86.73 | -13.27 | 105 | 15.2 | -87.35 | -25.17 | -87.44 | 1966 |
| 76 | Z-score reversion | reversion | 86.67 | -13.33 | 106 | 19.8 | -85.03 | -28.91 | -85.03 | 2086 |
| 77 | MACD zero-line | trend | 86.03 | -13.97 | 121 | 14.0 | -91.65 | -37.11 | -91.66 | 2364 |
| 78 | Triple EMA stack | trend | 86.02 | -13.98 | 134 | 12.7 | -92.97 | -36.79 | -93.00 | 2632 |
| 79 | Trend pullback | trend | 85.81 | -14.19 | 119 | 16.8 | -90.74 | -35.43 | -90.74 | 2313 |
| 80 | Bollinger breakout | breakout | 85.50 | -14.50 | 118 | 11.0 | -94.06 | -43.14 | -94.06 | 2873 |
| 81 | Donchian 20/10 | breakout | 85.44 | -14.56 | 123 | 13.8 | -91.07 | -30.17 | -91.14 | 2699 |
| 82 | Connors RSI(2) | reversion | 84.42 | -15.58 | 156 | 17.3 | -96.36 | -42.90 | -96.36 | 3658 |
| 83 | ADX DI cross | trend | 84.30 | -15.70 | 120 | 7.5 | -89.40 | -49.75 | -89.44 | 2115 |
| 84 | MFI reversion | reversion | 84.11 | -15.89 | 114 | 7.9 | -87.83 | -37.81 | -87.85 | 2162 |
| 85 | Stochastic reversion | reversion | 82.99 | -17.02 | 171 | 20.5 | -95.89 | -49.54 | -95.90 | 4049 |
| 86 | EMA 9/21 cross | trend | 81.44 | -18.55 | 178 | 11.2 | -97.45 | -43.58 | -97.47 | 3543 |
| 87 | Consensus | meta | 81.34 | -18.66 | 129 | 6.2 | -94.86 | -32.01 | -94.86 | 2671 |
| 88 | OBV trend | momentum | 81.31 | -18.69 | 176 | 11.9 | -95.86 | -50.49 | -95.88 | 3573 |
| 89 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.32 | -56.31 | -99.33 | 5537 |
| 90 | Bollinger reversion | reversion | 80.47 | -19.53 | 185 | 12.4 | -95.83 | -46.86 | -95.83 | 3691 |
| 91 | VWAP momentum | momentum | 80.27 | -19.73 | 213 | 9.4 | -98.43 | -37.05 | -98.45 | 5203 |
| 92 | Parabolic SAR | trend | 78.76 | -21.24 | 194 | 12.4 | -96.89 | -60.42 | -96.90 | 3660 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.44 | -56.78 | -98.45 | 4688 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -75.06 | -99.70 | 6088 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.52 | -68.21 | -99.52 | 6080 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.89 | -104.40 | -99.89 | 8332 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T14:10 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 100.00 | — | entry |
| 2026-09-28T14:10 | Agent (ML meta-label) | buy | SOL-USD | 3.04 | — | entry |
| 2026-09-28T14:10 | Agent (ML meta-label) | buy | AMZN | 4.24 | — | entry |
| 2026-09-28T14:10 | Agent | buy | ETHU | 20.04 | — | following Williams %R |
| 2026-09-28T14:10 | Stochastic reversion · 1h | buy | SOL-USD | 7.75 | — | rebalance up |
| 2026-09-28T14:10 | Stochastic reversion · 1h | sell | TSLA | 10.71 | -0.32 | stop-loss |
| 2026-09-28T14:10 | Keltner breakout · 1h | sell | TECL | 23.67 | -0.22 | stop-loss |
| 2026-09-28T14:10 | VWAP momentum · 1h | buy | XRP-USD | 5.17 | — | rebalance up |
| 2026-09-28T14:10 | VWAP momentum · 1h | sell | SOXL | 7.20 | -0.43 | stop-loss |
| 2026-09-28T14:10 | Ichimoku · 1h | sell | TECL | 24.15 | -0.70 | stop-loss |
| 2026-09-28T14:10 | MFI reversion | buy | MSTR | 4.16 | — | rebalance up |
| 2026-09-28T14:10 | MFI reversion | buy | LABU | 21.03 | — | entry |
| 2026-09-28T14:10 | Z-score reversion | buy | TNA | 14.44 | — | entry signal |
| 2026-09-28T14:10 | Z-score reversion | buy | IWM | 14.45 | — | entry signal |
| 2026-09-28T14:10 | Z-score reversion | buy | ETHU | 14.45 | — | entry signal |
| 2026-09-28T14:10 | Z-score reversion | sell | PLTR | 7.19 | -0.05 | rebalance down |
| 2026-09-28T14:10 | Z-score reversion | sell | MSFT | 7.26 | -0.03 | rebalance down |
| 2026-09-28T14:10 | Z-score reversion | sell | LABU | 7.22 | -0.02 | rebalance down |
| 2026-09-28T14:10 | Bollinger reversion | buy | DOGE-USD | 1.42 | — | entry signal |
| 2026-09-28T14:10 | Bollinger reversion | buy | BITX | 4.24 | — | entry signal |
| 2026-09-28T14:10 | Bollinger reversion | sell | GOOGL | 5.36 | -0.04 | stop-loss |
| 2026-09-28T14:10 | Opening range 30m | buy | TNA | 24.82 | — | entry signal |
| 2026-09-28T14:10 | Opening range 30m | buy | SQQQ | 24.82 | — | entry signal |
| 2026-09-28T14:10 | Opening range 30m | buy | IWM | 24.82 | — | entry signal |
| 2026-09-28T14:10 | Opening range 15m | buy | TNA | 24.55 | — | entry signal |
| 2026-09-28T14:10 | Opening range 15m | buy | IWM | 24.57 | — | entry signal |
| 2026-09-28T14:10 | VWAP momentum | buy | LABU | 4.22 | — | entry signal |
| 2026-09-28T14:10 | VWAP momentum | buy | AMZN | 7.30 | — | entry signal |
| 2026-09-28T14:10 | VWAP momentum | sell | MSTR | 7.27 | -0.03 | exit signal |
| 2026-09-28T14:10 | Ichimoku | buy | SQQQ | 22.23 | — | entry signal |
| 2026-09-28T14:10 | EMA 9/21 cross | buy | COIN | 9.59 | — | rebalance up |
| 2026-09-28T14:10 | EMA 9/21 cross | sell | DOGE-USD | 16.17 | 0.03 | exit signal |
| 2026-09-28T14:07 | AI bee: Boozy | sell | SQQQ | 22.11 | 0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-28T14:07 | AI bee: Boozy | sell | PLTR | 31.06 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-28T14:07 | AI bee: Bizzy | buy | TNA | 18.25 | — | Jev: buy (buy p=0.76) |
| 2026-09-28T14:07 | AI bee: Bizzy | sell | SQQQ | 15.61 | 0.00 | Jev: sell (buy p=0.17) |
| 2026-09-28T14:05 | AI bee: Boozy | buy | SQQQ | 22.10 | — | Jev: buy (buy p=0.47) |
| 2026-09-28T14:05 | AI bee: Boozy | sell | COIN | 33.28 | -0.18 | Jev: sell (buy p=0.35) |
| 2026-09-28T14:05 | AI bee: Bizzy | buy | SQQQ | 15.61 | — | Jev: buy (buy p=0.65) |
| 2026-09-28T14:05 | AI bee: Bizzy | sell | TNA | 16.32 | -0.04 | Jev: sell (buy p=0.02) |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
