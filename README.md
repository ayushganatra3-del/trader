# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T17:40:05.000134+00:00 · 4767 ticks

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

Today: 16238 decisions in 704 calls, $0.1921 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T17:40 | 1 / 14 / 14 | GOOGL 19% |  |
| Breezy | 2026-09-28T17:40 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-09-28T17:40 | 5 / 23 / 1 | MSTR 31%, BITX 27% |  |

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
| 1 | Agent (aggressive) | meta | 100.59 | 0.59 | 6 | 66.7 | 0.71 | 0.45 | -4.81 | 88 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.45 | 0.45 | 0 | — | 11.72 | 2.61 | -7.55 | 43 |
| 3 | Daily: Bullish score | daily | 100.13 | 0.13 | 2 | 0.0 | 0.17 | 0.22 | -12.76 | 13 |
| 4 | Hold BTC | benchmark | 100.11 | 0.11 | 0 | — | 31.36 | 3.97 | -8.68 | 1 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 4 | 50.0 | 2.27 | 1.19 | -2.47 | 91 |
| 6 | RSI(14) reversion · 1h | reversion | 100.04 | 0.04 | 2 | 100.0 | 6.70 | 1.87 | -6.57 | 123 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 6.13 | 1.34 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | -0.41 | -0.62 | -1.49 | 18 |
| 11 | Agent | meta | 99.95 | -0.05 | 14 | 71.4 | -8.98 | -5.97 | -10.16 | 201 |
| 12 | Copy: Congress Democrats (NANC) | copy | 99.69 | -0.31 | 0 | — | 7.28 | 2.76 | -3.62 | 1 |
| 13 | Copy: Warren Buffett (BRK-B) | copy | 99.64 | -0.36 | 0 | — | -1.84 | -0.69 | -7.65 | 1 |
| 14 | Stochastic reversion · 1h | reversion | 99.63 | -0.37 | 21 | 52.4 | -11.45 | -2.53 | -14.07 | 324 |
| 15 | Hold SPY | benchmark | 99.59 | -0.41 | 0 | — | 3.51 | 1.82 | -3.66 | 1 |
| 16 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | -7.22 | -1.83 | -12.73 | 1 |
| 17 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 18 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.34 | -0.66 | 0 | — | -5.56 | -1.66 | -12.40 | 25 |
| 19 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 20 | Williams %R · 1h | reversion | 99.19 | -0.81 | 27 | 51.9 | -18.57 | -3.43 | -20.98 | 490 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 99.17 | -0.83 | 0 | — | -1.63 | -0.76 | -5.14 | 1 |
| 22 | Connors RSI(2) · 1h | reversion | 99.16 | -0.84 | 34 | 55.9 | -11.87 | -3.80 | -13.49 | 243 |
| 23 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.79 | -5.16 | 28 |
| 24 | Timing: Nasdaq FTD · QQQ | daily | 99.15 | -0.85 | 0 | — | -3.42 | -2.15 | -5.09 | 2 |
| 25 | CCI reversion · 1h | reversion | 99.13 | -0.87 | 22 | 31.8 | 0.02 | 0.18 | -12.41 | 415 |
| 26 | Opening range 30m | breakout | 99.11 | -0.89 | 22 | 9.1 | -8.11 | -2.36 | -13.54 | 562 |
| 27 | Z-score reversion · 1h | reversion | 99.03 | -0.97 | 4 | 25.0 | 3.91 | 0.98 | -8.60 | 155 |
| 28 | Copy: Insider buying | copy | 98.78 | -1.22 | 2 | 100.0 | -12.36 | -2.39 | -17.74 | 73 |
| 29 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 30 | Candlestick reversal · 1h | reversion | 98.72 | -1.28 | 9 | 22.2 | -26.85 | -6.62 | -27.97 | 491 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 98.58 | -1.42 | 0 | — | 24.71 | 3.48 | -6.29 | 1 |
| 32 | EMA 20/50 cross · 1h | trend | 98.56 | -1.45 | 8 | 12.5 | 16.22 | 1.95 | -14.36 | 126 |
| 33 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.59 | -0.05 | -15.21 | 47 |
| 34 | Supertrend · 1h | trend | 98.23 | -1.77 | 11 | 9.1 | 4.60 | 0.82 | -16.43 | 196 |
| 35 | Agent (rotation) | meta | 98.15 | -1.85 | 26 | 11.5 | -8.59 | -3.03 | -11.91 | 221 |
| 36 | Opening range 15m | breakout | 98.13 | -1.86 | 29 | 10.3 | -10.69 | -2.88 | -16.14 | 696 |
| 37 | Squeeze breakout · 1h | breakout | 98.13 | -1.87 | 7 | 14.3 | 14.20 | 2.48 | -8.33 | 96 |
| 38 | Parabolic SAR · 1h | trend | 97.96 | -2.04 | 18 | 16.7 | -5.05 | -0.57 | -18.82 | 305 |
| 39 | MACD cross · 1h | trend | 97.91 | -2.09 | 26 | 11.5 | -15.44 | -2.62 | -21.20 | 459 |
| 40 | Trend pullback · 1h | trend | 97.91 | -2.09 | 22 | 13.6 | -25.33 | -6.91 | -26.81 | 152 |
| 41 | Bollinger reversion · 1h | reversion | 97.78 | -2.22 | 18 | 33.3 | -16.28 | -4.55 | -16.95 | 311 |
| 42 | Timing: Nasdaq FTD · TQQQ | daily | 97.66 | -2.34 | 0 | — | -10.99 | -2.32 | -15.27 | 2 |
| 43 | Agent (ML meta-label) | meta | 97.57 | -2.43 | 64 | 10.9 | 3.70 | 0.80 | -11.24 | 363 |
| 44 | Donchian 55/20 · 1h | breakout | 97.56 | -2.44 | 8 | 0.0 | 5.08 | 0.88 | -16.96 | 113 |
| 45 | MACD zero-line · 1h | trend | 97.16 | -2.84 | 13 | 7.7 | 0.37 | 0.25 | -14.64 | 224 |
| 46 | EMA 9/21 cross · 1h | trend | 96.91 | -3.09 | 31 | 12.9 | 3.82 | 0.72 | -16.92 | 310 |
| 47 | Bollinger breakout · 1h | breakout | 96.83 | -3.17 | 13 | 7.7 | 12.60 | 1.81 | -10.46 | 284 |
| 48 | RSI momentum · 1h | momentum | 96.65 | -3.35 | 20 | 5.0 | 2.04 | 0.48 | -15.29 | 213 |
| 49 | Triple EMA stack · 1h | trend | 96.63 | -3.38 | 23 | 8.7 | -3.58 | -0.22 | -22.96 | 227 |
| 50 | Three white soldiers | momentum | 96.49 | -3.51 | 30 | 13.3 | -52.13 | -28.58 | -52.13 | 623 |
| 51 | Max aggression: 5-day momentum | meta | 96.46 | -3.54 | 1 | 0.0 | 0.19 | 0.37 | -29.56 | 29 |
| 52 | ADX DI cross · 1h | trend | 96.44 | -3.56 | 22 | 9.1 | -10.89 | -2.07 | -15.39 | 251 |
| 53 | Ichimoku · 1h | trend | 96.32 | -3.68 | 10 | 10.0 | 8.98 | 1.24 | -15.13 | 119 |
| 54 | VWAP momentum · 1h | momentum | 96.15 | -3.85 | 76 | 6.6 | -32.94 | -4.94 | -33.25 | 1244 |
| 55 | MFI reversion · 1h | reversion | 96.00 | -4.00 | 37 | 10.8 | -9.41 | -1.74 | -17.27 | 126 |
| 56 | Max aggression: 1-day momentum | meta | 96.00 | -4.00 | 1 | 0.0 | -31.64 | -1.78 | -49.41 | 42 |
| 57 | Donchian 20/10 · 1h | breakout | 95.72 | -4.28 | 12 | 16.7 | 13.24 | 1.84 | -12.78 | 213 |
| 58 | OBV trend · 1h | momentum | 95.61 | -4.38 | 47 | 6.4 | -8.30 | -0.83 | -25.24 | 328 |
| 59 | Heikin-Ashi · 1h | trend | 95.58 | -4.42 | 29 | 13.8 | -23.69 | -3.61 | -28.17 | 682 |
| 60 | Volume breakout · 1h | breakout | 95.27 | -4.73 | 25 | 4.0 | 6.42 | 1.08 | -12.60 | 126 |
| 61 | Keltner breakout · 1h | breakout | 95.22 | -4.78 | 7 | 0.0 | -0.43 | 0.15 | -18.68 | 221 |
| 62 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 63 | AI bee: Bizzy ⏸ | ai | 93.85 | -6.15 | 171 | 15.8 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 93.02 | -6.98 | 79 | 35.4 | -71.18 | -22.23 | -71.75 | 1495 |
| 65 | ROC + volume · 1h | momentum | 92.39 | -7.61 | 41 | 4.9 | -3.39 | -0.27 | -17.18 | 401 |
| 66 | Squeeze breakout | breakout | 90.66 | -9.34 | 62 | 6.5 | -59.93 | -18.68 | -59.97 | 1186 |
| 67 | EMA 20/50 cross | trend | 90.04 | -9.96 | 75 | 14.7 | -78.53 | -17.74 | -78.63 | 1487 |
| 68 | ROC + volume | momentum | 89.97 | -10.03 | 106 | 17.0 | -72.40 | -18.08 | -72.70 | 1668 |
| 69 | Donchian 55/20 | breakout | 89.62 | -10.38 | 70 | 11.4 | -68.59 | -15.99 | -68.66 | 1333 |
| 70 | Volume breakout | breakout | 88.92 | -11.08 | 74 | 9.5 | -62.97 | -20.76 | -62.98 | 914 |
| 71 | Ichimoku | trend | 88.70 | -11.30 | 81 | 8.6 | -80.50 | -26.58 | -80.50 | 1762 |
| 72 | Keltner breakout | breakout | 88.51 | -11.49 | 103 | 8.7 | -85.10 | -35.97 | -85.17 | 1941 |
| 73 | Z-score reversion | reversion | 87.19 | -12.80 | 134 | 29.9 | -84.58 | -28.98 | -84.79 | 2088 |
| 74 | Supertrend | trend | 86.34 | -13.66 | 111 | 15.3 | -87.28 | -25.25 | -87.44 | 1981 |
| 75 | MACD zero-line | trend | 85.97 | -14.03 | 134 | 14.9 | -91.54 | -37.08 | -91.58 | 2369 |
| 76 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -70.89 | -17.47 | -71.87 | 1417 |
| 77 | RSI momentum | momentum | 85.78 | -14.22 | 116 | 12.9 | -90.31 | -30.20 | -90.35 | 2399 |
| 78 | Bollinger breakout | breakout | 85.67 | -14.33 | 137 | 13.9 | -93.97 | -43.05 | -94.00 | 2886 |
| 79 | Donchian 20/10 | breakout | 85.61 | -14.39 | 130 | 14.6 | -90.83 | -30.11 | -90.96 | 2696 |
| 80 | Triple EMA stack | trend | 85.25 | -14.75 | 144 | 12.5 | -93.03 | -37.14 | -93.07 | 2624 |
| 81 | Trend pullback | trend | 84.54 | -15.46 | 127 | 16.5 | -90.59 | -35.10 | -90.60 | 2293 |
| 82 | Connors RSI(2) | reversion | 84.05 | -15.95 | 175 | 18.9 | -96.33 | -42.60 | -96.36 | 3649 |
| 83 | ADX DI cross | trend | 83.87 | -16.13 | 135 | 6.7 | -89.36 | -49.98 | -89.42 | 2131 |
| 84 | MFI reversion | reversion | 83.72 | -16.29 | 135 | 15.6 | -87.94 | -37.97 | -88.11 | 2180 |
| 85 | Stochastic reversion | reversion | 82.50 | -17.50 | 208 | 25.5 | -95.90 | -49.71 | -95.94 | 4052 |
| 86 | EMA 9/21 cross | trend | 81.49 | -18.51 | 185 | 12.4 | -97.40 | -43.67 | -97.41 | 3546 |
| 87 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.33 | -55.90 | -99.33 | 5567 |
| 88 | OBV trend | momentum | 80.86 | -19.14 | 186 | 12.4 | -95.82 | -51.29 | -95.84 | 3558 |
| 89 | Consensus | meta | 80.37 | -19.63 | 142 | 7.0 | -94.96 | -32.09 | -94.96 | 2686 |
| 90 | Bollinger reversion | reversion | 79.71 | -20.29 | 218 | 13.8 | -95.82 | -46.87 | -95.84 | 3684 |
| 91 | VWAP momentum | momentum | 79.44 | -20.56 | 246 | 8.9 | -98.45 | -37.25 | -98.46 | 5228 |
| 92 | Parabolic SAR | trend | 78.38 | -21.62 | 204 | 12.7 | -96.90 | -61.04 | -96.91 | 3654 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.46 | -56.50 | -98.47 | 4695 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -75.13 | -99.70 | 6098 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.53 | -67.94 | -99.53 | 6087 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.89 | -105.28 | -99.89 | 8325 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T17:40 | Agent (ML meta-label) | buy | QQQ | 4.65 | — | entry |
| 2026-09-28T17:40 | Agent (ML meta-label) | sell | SPY | 4.64 | -0.00 | selected signal exited |
| 2026-09-28T17:40 | Stochastic reversion | buy | TSLA | 20.59 | — | entry signal |
| 2026-09-28T17:40 | Z-score reversion | sell | META | 21.80 | -0.04 | exit signal |
| 2026-09-28T17:40 | OBV trend | buy | SOL-USD | 1.15 | — | entry |
| 2026-09-28T17:40 | OBV trend | buy | PLTR | 7.35 | — | entry signal |
| 2026-09-28T17:40 | OBV trend | sell | MSTR | 4.26 | 0.02 | rebalance down |
| 2026-09-28T17:40 | OBV trend | sell | ETH-USD | 4.24 | 0.01 | rebalance down |
| 2026-09-28T17:35 | Agent (ML meta-label) | buy | SPY | 4.65 | — | entry |
| 2026-09-28T17:35 | Agent (ML meta-label) | buy | IWM | 4.65 | — | entry |
| 2026-09-28T17:35 | Consensus | sell | ETHU | 20.07 | -0.17 | target is flat |
| 2026-09-28T17:35 | OBV trend · 1h | sell | TECL | 23.82 | -0.15 | target is flat |
| 2026-09-28T17:35 | Stochastic reversion | buy | NVDA | 20.63 | — | entry signal |
| 2026-09-28T17:35 | Volume breakout | sell | LABU | 18.05 | 0.03 | exit signal |
| 2026-09-28T17:35 | Volume breakout | sell | ETHU | 22.22 | -0.24 | stop-loss |
| 2026-09-28T17:35 | Volume breakout | sell | BITX | 17.82 | -0.17 | exit signal |
| 2026-09-28T17:35 | Keltner breakout | sell | LABU | 5.18 | 0.03 | stop-loss |
| 2026-09-28T17:35 | Keltner breakout | sell | ETHU | 5.18 | -0.07 | stop-loss |
| 2026-09-28T17:35 | Bollinger breakout | sell | LABU | 5.68 | 0.04 | stop-loss |
| 2026-09-28T17:35 | Bollinger breakout | sell | ETHU | 5.68 | 0.05 | stop-loss |
| 2026-09-28T17:35 | Opening range 30m | sell | ETHU | 8.95 | -0.12 | stop-loss |
| 2026-09-28T17:35 | Opening range 15m | sell | ETHU | 8.86 | -0.11 | stop-loss |
| 2026-09-28T17:35 | Donchian 55/20 | sell | ETHU | 11.17 | -0.14 | stop-loss |
| 2026-09-28T17:35 | ROC + volume | sell | LABU | 22.44 | 0.09 | exit signal |
| 2026-09-28T17:35 | Parabolic SAR | buy | TECL | 6.53 | — | entry |
| 2026-09-28T17:35 | Parabolic SAR | sell | LABU | 5.57 | -0.08 | stop-loss |
| 2026-09-28T17:35 | Parabolic SAR | sell | ETHU | 5.57 | -0.07 | stop-loss |
| 2026-09-28T17:30 | Agent (ML meta-label) | sell | IWM | 4.62 | 0.02 | selected signal exited |
| 2026-09-28T17:30 | Consensus | buy | SOL-USD | 8.59 | — | rebalance up |
| 2026-09-28T17:30 | Consensus | buy | MSTR | 8.60 | — | rebalance up |
| 2026-09-28T17:30 | Consensus | buy | ETHU | 8.65 | — | rebalance up |
| 2026-09-28T17:30 | Consensus | buy | BITX | 8.62 | — | rebalance up |
| 2026-09-28T17:30 | Consensus | sell | ETH-USD | 11.44 | -0.16 | target is flat |
| 2026-09-28T17:30 | Consensus | sell | BTC-USD | 11.48 | -0.12 | target is flat |
| 2026-09-28T17:30 | CCI reversion · 1h | buy | PLTR | 5.22 | — | entry signal |
| 2026-09-28T17:30 | CCI reversion · 1h | sell | ETHU | 5.25 | 0.02 | exit signal |
| 2026-09-28T17:30 | Connors RSI(2) · 1h | sell | MSFT | 14.22 | 0.03 | exit signal |
| 2026-09-28T17:30 | VWAP momentum · 1h | buy | BTC-USD | 8.39 | — | rebalance up |
| 2026-09-28T17:30 | VWAP momentum · 1h | sell | NVDA | 11.93 | -0.11 | exit signal |
| 2026-09-28T17:30 | VWAP momentum · 1h | sell | AAPL | 14.56 | -0.09 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
