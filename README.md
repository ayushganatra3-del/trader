# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T15:40:05.000184+00:00 · 4669 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.68 (-0.32%)

Closed trades 12, win rate 66.7%, fees £0.41, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 39.88 | +0.30 |
| COIN | 19.82 | -0.12 |

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

Today: 7709 decisions in 416 calls, $0.0922 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T15:40 | 2 / 24 / 3 | ETHU 15% |  |
| Breezy | 2026-09-28T15:40 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-09-28T15:40 | 15 / 14 / 0 | ETHU 42%, COIN 42% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.56 | 1.56 | 0 | — | 12.82 | 2.82 | -7.55 | 43 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.44 | 0.44 | 0 | — | -4.64 | -1.37 | -12.40 | 25 |
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.37 | 0.37 | 4 | 50.0 | 2.44 | 1.27 | -2.47 | 92 |
| 4 | Copy: Hedge-fund gurus (GURU) | copy | 100.37 | 0.37 | 0 | — | -0.21 | -0.05 | -5.14 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.32 | 0.32 | 0 | — | 1.13 | 0.55 | -4.88 | 16 |
| 6 | Agent (aggressive) | meta | 100.21 | 0.21 | 4 | 50.0 | 1.31 | 0.85 | -3.92 | 89 |
| 7 | Copy: Warren Buffett (BRK-B) | copy | 100.16 | 0.16 | 0 | — | -0.70 | -0.52 | -7.65 | 1 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 6.03 | 1.34 | -7.93 | 7 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | -0.41 | -0.62 | -1.49 | 18 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.93 | -0.07 | 0 | — | -6.86 | -1.73 | -12.73 | 1 |
| 13 | Agent | meta | 99.68 | -0.32 | 12 | 66.7 | -9.82 | -6.58 | -10.68 | 204 |
| 14 | Hold SPY | benchmark | 99.52 | -0.48 | 0 | — | 3.15 | 1.71 | -3.66 | 1 |
| 15 | Hold BTC | benchmark | 99.49 | -0.51 | 0 | — | 30.06 | 3.85 | -8.68 | 1 |
| 16 | Daily: Bullish score | daily | 99.46 | -0.54 | 2 | 0.0 | -0.64 | 0.10 | -12.76 | 13 |
| 17 | RSI(14) reversion · 1h | reversion | 99.46 | -0.54 | 1 | 100.0 | 8.37 | 2.27 | -6.57 | 122 |
| 18 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 19 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 20 | Copy: Congress Democrats (NANC) | copy | 99.28 | -0.72 | 0 | — | 6.44 | 2.41 | -3.62 | 1 |
| 21 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.28 | -2.70 | -5.16 | 28 |
| 22 | Opening range 30m | breakout | 99.07 | -0.93 | 13 | 15.4 | -7.83 | -2.28 | -13.54 | 548 |
| 23 | Agent (rotation) | meta | 99.03 | -0.97 | 26 | 11.5 | -4.92 | -1.60 | -11.77 | 221 |
| 24 | Timing: Nasdaq FTD · QQQ | daily | 98.94 | -1.06 | 0 | — | -3.74 | -2.31 | -5.09 | 2 |
| 25 | Copy: Insider buying | copy | 98.54 | -1.46 | 2 | 100.0 | -12.73 | -2.47 | -17.74 | 73 |
| 26 | Stochastic reversion · 1h | reversion | 98.50 | -1.50 | 20 | 50.0 | -10.97 | -2.40 | -12.43 | 322 |
| 27 | Z-score reversion · 1h | reversion | 98.49 | -1.51 | 4 | 25.0 | 3.35 | 0.86 | -8.60 | 154 |
| 28 | Connors RSI(2) · 1h | reversion | 98.40 | -1.60 | 28 | 46.4 | -12.76 | -4.06 | -13.59 | 243 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.88 | -0.05 | -15.21 | 47 |
| 30 | Williams %R · 1h | reversion | 98.30 | -1.70 | 26 | 50.0 | -19.89 | -3.64 | -21.61 | 482 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 98.20 | -1.80 | 0 | — | 23.86 | 3.39 | -6.29 | 1 |
| 32 | Squeeze breakout · 1h | breakout | 98.18 | -1.82 | 7 | 14.3 | 15.33 | 2.65 | -8.16 | 97 |
| 33 | Parabolic SAR · 1h | trend | 98.14 | -1.86 | 18 | 16.7 | -4.79 | -0.53 | -18.82 | 300 |
| 34 | Opening range 15m | breakout | 98.13 | -1.87 | 22 | 13.6 | -10.57 | -2.84 | -16.14 | 683 |
| 35 | Supertrend · 1h | trend | 98.13 | -1.87 | 11 | 9.1 | 11.94 | 1.73 | -16.43 | 198 |
| 36 | Candlestick reversal · 1h | reversion | 98.07 | -1.93 | 8 | 12.5 | -27.39 | -6.76 | -27.94 | 489 |
| 37 | CCI reversion · 1h | reversion | 98.06 | -1.94 | 20 | 25.0 | -0.93 | 0.02 | -12.41 | 407 |
| 38 | Bollinger reversion · 1h | reversion | 97.74 | -2.26 | 18 | 33.3 | -15.50 | -4.28 | -16.13 | 307 |
| 39 | EMA 20/50 cross · 1h | trend | 97.69 | -2.31 | 7 | 14.3 | 15.56 | 1.88 | -14.36 | 125 |
| 40 | MACD cross · 1h | trend | 97.43 | -2.57 | 26 | 11.5 | -16.10 | -2.75 | -21.07 | 455 |
| 41 | Trend pullback · 1h | trend | 97.39 | -2.61 | 21 | 14.3 | -26.90 | -7.27 | -27.81 | 152 |
| 42 | MACD zero-line · 1h | trend | 97.27 | -2.73 | 13 | 7.7 | 0.38 | 0.25 | -14.64 | 223 |
| 43 | Agent (ML meta-label) | meta | 97.12 | -2.88 | 51 | 7.8 | 16.72 | 2.33 | -10.86 | 381 |
| 44 | Bollinger breakout · 1h | breakout | 97.07 | -2.93 | 13 | 7.7 | 12.83 | 1.84 | -10.41 | 283 |
| 45 | Donchian 55/20 · 1h | breakout | 96.89 | -3.10 | 8 | 0.0 | 3.45 | 0.66 | -16.96 | 114 |
| 46 | Timing: Nasdaq FTD · TQQQ | daily | 96.78 | -3.22 | 0 | — | -11.90 | -2.48 | -15.27 | 2 |
| 47 | RSI momentum · 1h | momentum | 96.74 | -3.26 | 20 | 5.0 | 2.35 | 0.53 | -15.29 | 213 |
| 48 | ADX DI cross · 1h | trend | 96.74 | -3.26 | 22 | 9.1 | -11.92 | -2.28 | -16.35 | 255 |
| 49 | Three white soldiers | momentum | 96.73 | -3.27 | 28 | 14.3 | -51.94 | -28.35 | -51.95 | 622 |
| 50 | Ichimoku · 1h | trend | 96.50 | -3.50 | 10 | 10.0 | 9.11 | 1.25 | -15.13 | 119 |
| 51 | EMA 9/21 cross · 1h | trend | 96.47 | -3.53 | 29 | 13.8 | 3.48 | 0.67 | -16.92 | 307 |
| 52 | Triple EMA stack · 1h | trend | 96.37 | -3.63 | 21 | 9.5 | -4.14 | -0.29 | -22.96 | 227 |
| 53 | Max aggression: 1-day momentum | meta | 96.19 | -3.81 | 1 | 0.0 | -31.59 | -1.77 | -49.41 | 42 |
| 54 | Donchian 20/10 · 1h | breakout | 96.03 | -3.97 | 12 | 16.7 | 14.71 | 2.01 | -12.78 | 213 |
| 55 | Heikin-Ashi · 1h | trend | 95.99 | -4.01 | 27 | 14.8 | -22.53 | -3.42 | -27.94 | 691 |
| 56 | VWAP momentum · 1h | momentum | 95.82 | -4.18 | 73 | 6.8 | -33.91 | -5.07 | -34.24 | 1253 |
| 57 | OBV trend · 1h | momentum | 95.80 | -4.20 | 46 | 6.5 | -7.74 | -0.76 | -25.24 | 328 |
| 58 | Max aggression: 5-day momentum | meta | 95.75 | -4.25 | 1 | 0.0 | -0.67 | 0.30 | -29.56 | 29 |
| 59 | Volume breakout · 1h | breakout | 95.32 | -4.68 | 25 | 4.0 | 6.44 | 1.08 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.27 | -4.73 | 7 | 0.0 | 0.04 | 0.21 | -18.68 | 219 |
| 61 | AI bee: Bizzy | ai | 95.15 | -4.85 | 89 | 9.0 | — | — | — | — |
| 62 | MFI reversion · 1h | reversion | 95.13 | -4.87 | 37 | 10.8 | -10.42 | -1.94 | -17.20 | 126 |
| 63 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 64 | ROC + volume · 1h | momentum | 92.54 | -7.46 | 41 | 4.9 | -0.36 | 0.15 | -17.18 | 401 |
| 65 | RSI(14) reversion | reversion | 92.39 | -7.61 | 65 | 23.1 | -71.86 | -22.34 | -71.95 | 1485 |
| 66 | Squeeze breakout | breakout | 91.15 | -8.85 | 58 | 6.9 | -59.65 | -18.45 | -59.85 | 1185 |
| 67 | Volume breakout | breakout | 90.61 | -9.39 | 62 | 8.1 | -62.19 | -20.87 | -62.19 | 902 |
| 68 | EMA 20/50 cross | trend | 90.25 | -9.74 | 72 | 15.3 | -78.74 | -17.74 | -78.74 | 1481 |
| 69 | Donchian 55/20 | breakout | 90.25 | -9.75 | 66 | 10.6 | -68.42 | -15.87 | -68.42 | 1328 |
| 70 | ROC + volume | momentum | 89.97 | -10.04 | 85 | 12.9 | -72.48 | -18.12 | -72.69 | 1640 |
| 71 | Keltner breakout | breakout | 88.79 | -11.21 | 87 | 9.2 | -85.17 | -35.81 | -85.17 | 1915 |
| 72 | Ichimoku | trend | 88.76 | -11.24 | 79 | 7.6 | -80.46 | -26.51 | -80.46 | 1766 |
| 73 | Z-score reversion | reversion | 86.58 | -13.42 | 115 | 19.1 | -85.07 | -28.86 | -85.15 | 2111 |
| 74 | RSI momentum | momentum | 85.98 | -14.02 | 113 | 13.3 | -90.45 | -30.12 | -90.45 | 2384 |
| 75 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -71.18 | -17.40 | -71.87 | 1425 |
| 76 | MACD zero-line | trend | 85.87 | -14.13 | 122 | 13.9 | -91.70 | -37.25 | -91.72 | 2367 |
| 77 | Supertrend | trend | 85.78 | -14.22 | 110 | 15.5 | -87.44 | -25.39 | -87.52 | 1966 |
| 78 | Bollinger breakout | breakout | 85.50 | -14.50 | 118 | 11.0 | -93.98 | -43.14 | -93.99 | 2864 |
| 79 | Triple EMA stack | trend | 85.41 | -14.59 | 139 | 12.9 | -93.01 | -37.12 | -93.01 | 2619 |
| 80 | Trend pullback | trend | 85.29 | -14.71 | 122 | 16.4 | -90.67 | -35.62 | -90.68 | 2295 |
| 81 | Donchian 20/10 | breakout | 84.88 | -15.12 | 129 | 14.7 | -90.99 | -30.43 | -91.00 | 2680 |
| 82 | Connors RSI(2) | reversion | 84.07 | -15.93 | 163 | 17.2 | -96.37 | -43.17 | -96.37 | 3650 |
| 83 | ADX DI cross | trend | 83.92 | -16.08 | 122 | 7.4 | -89.26 | -49.95 | -89.28 | 2110 |
| 84 | MFI reversion | reversion | 83.30 | -16.70 | 122 | 9.0 | -88.05 | -37.95 | -88.12 | 2181 |
| 85 | Stochastic reversion | reversion | 82.48 | -17.52 | 192 | 21.9 | -95.95 | -49.72 | -95.98 | 4074 |
| 86 | Consensus | meta | 81.38 | -18.62 | 129 | 6.2 | -94.88 | -32.05 | -94.88 | 2676 |
| 87 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.33 | -56.01 | -99.34 | 5571 |
| 88 | OBV trend | momentum | 81.09 | -18.91 | 179 | 12.3 | -95.86 | -50.76 | -95.87 | 3545 |
| 89 | EMA 9/21 cross | trend | 80.89 | -19.11 | 183 | 12.6 | -97.45 | -43.97 | -97.45 | 3542 |
| 90 | Bollinger reversion | reversion | 79.76 | -20.24 | 214 | 14.0 | -95.88 | -46.87 | -95.90 | 3706 |
| 91 | VWAP momentum | momentum | 79.50 | -20.50 | 226 | 9.7 | -98.48 | -37.25 | -98.49 | 5239 |
| 92 | Parabolic SAR | trend | 78.76 | -21.23 | 196 | 12.2 | -96.89 | -60.62 | -96.90 | 3642 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.46 | -56.49 | -98.47 | 4720 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -75.34 | -99.70 | 6111 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.53 | -68.03 | -99.53 | 6100 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.89 | -104.93 | -99.89 | 8323 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T15:40 | Agent (ML meta-label) | sell | AMZN | 4.85 | -0.00 | selected signal exited |
| 2026-09-28T15:40 | Agent | sell | ETHU | 20.00 | 0.05 | selected signal exited |
| 2026-09-28T15:40 | Stochastic reversion | buy | XRP-USD | 5.90 | — | entry |
| 2026-09-28T15:40 | Stochastic reversion | buy | UPRO | 5.90 | — | entry |
| 2026-09-28T15:40 | Stochastic reversion | buy | TNA | 5.90 | — | entry |
| 2026-09-28T15:40 | Stochastic reversion | buy | SOL-USD | 5.90 | — | entry |
| 2026-09-28T15:40 | Stochastic reversion | sell | TQQQ | 5.94 | 0.08 | exit signal |
| 2026-09-28T15:40 | Stochastic reversion | sell | TECL | 5.98 | 0.13 | exit signal |
| 2026-09-28T15:40 | Stochastic reversion | sell | QQQ | 5.89 | 0.03 | exit signal |
| 2026-09-28T15:40 | Stochastic reversion | sell | MSTR | 5.90 | 0.02 | exit signal |
| 2026-09-28T15:40 | Stochastic reversion | sell | DOGE-USD | 2.71 | 0.01 | exit signal |
| 2026-09-28T15:40 | Stochastic reversion | sell | AAPL | 4.13 | 0.02 | exit signal |
| 2026-09-28T15:40 | Bollinger reversion | buy | META | 14.51 | — | rebalance up |
| 2026-09-28T15:40 | Bollinger reversion | buy | IWM | 14.60 | — | rebalance up |
| 2026-09-28T15:40 | Bollinger reversion | buy | GOOGL | 14.62 | — | rebalance up |
| 2026-09-28T15:40 | Bollinger reversion | buy | COIN | 14.67 | — | rebalance up |
| 2026-09-28T15:40 | Bollinger reversion | sell | XRP-USD | 5.30 | -0.03 | exit signal |
| 2026-09-28T15:40 | Bollinger reversion | sell | TECL | 5.78 | 0.11 | take-profit |
| 2026-09-28T15:40 | Bollinger reversion | sell | SOL-USD | 5.30 | -0.02 | exit signal |
| 2026-09-28T15:40 | Bollinger reversion | sell | MSTR | 4.74 | -0.00 | exit signal |
| 2026-09-28T15:40 | Bollinger reversion | sell | ETHU | 5.34 | 0.01 | exit signal |
| 2026-09-28T15:40 | Bollinger reversion | sell | ETH-USD | 5.31 | -0.02 | exit signal |
| 2026-09-28T15:40 | Bollinger reversion | sell | DOGE-USD | 5.33 | -0.00 | exit signal |
| 2026-09-28T15:40 | Bollinger reversion | sell | BTC-USD | 4.96 | -0.01 | exit signal |
| 2026-09-28T15:40 | Bollinger reversion | sell | BITX | 6.16 | 0.05 | exit signal |
| 2026-09-28T15:40 | Donchian 20/10 | sell | SQQQ | 21.35 | 0.15 | exit signal |
| 2026-09-28T15:40 | ROC + volume | sell | SQQQ | 22.78 | 0.26 | stop-loss |
| 2026-09-28T15:40 | VWAP momentum | buy | ETH-USD | 2.40 | — | rebalance up |
| 2026-09-28T15:40 | VWAP momentum | buy | AAPL | 11.36 | — | entry signal |
| 2026-09-28T15:40 | VWAP momentum | sell | PLTR | 4.60 | 0.01 | rebalance down |
| 2026-09-28T15:40 | VWAP momentum | sell | LABU | 4.60 | 0.04 | rebalance down |
| 2026-09-28T15:40 | VWAP momentum | sell | AMZN | 4.56 | 0.01 | rebalance down |
| 2026-09-28T15:40 | ADX DI cross | buy | XRP-USD | 14.00 | — | entry signal |
| 2026-09-28T15:40 | ADX DI cross | buy | PLTR | 14.01 | — | entry signal |
| 2026-09-28T15:40 | ADX DI cross | buy | DOGE-USD | 14.01 | — | entry signal |
| 2026-09-28T15:40 | ADX DI cross | buy | BTC-USD | 14.01 | — | entry signal |
| 2026-09-28T15:40 | ADX DI cross | sell | NVDA | 7.01 | -0.00 | rebalance down |
| 2026-09-28T15:40 | ADX DI cross | sell | AAPL | 7.02 | 0.01 | rebalance down |
| 2026-09-28T15:40 | MACD zero-line | buy | AAPL | 21.47 | — | entry signal |
| 2026-09-28T15:40 | EMA 9/21 cross | buy | PLTR | 20.23 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
