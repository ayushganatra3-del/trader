# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T19:40:05.000161+00:00 · 6026 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.54 (-0.46%)

Closed trades 23, win rate 69.6%, fees £0.70, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 19.88 | -0.15 |
| COIN | 19.85 | -0.13 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-29 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 35427 decisions in 2840 calls, $0.4372 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T19:40 | 3 / 17 / 10 | PLTR 17%, TECL 15%, SQQQ 12% |  |
| Breezy | 2026-09-29T19:40 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-09-29T19:40 | 8 / 19 / 3 | BITX 30%, PLTR 29% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.17 | 1.17 | 1 | 100.0 | 13.99 | 3.05 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -0.28 | 0.00 | -9.74 | 24 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 11.87 | 2.26 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.00 | 0.00 | 0 | — | 7.31 | 2.99 | -3.62 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Hold BTC | benchmark | 99.91 | -0.09 | 0 | — | 31.10 | 3.89 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.73 | -0.27 | 0 | — | -0.21 | -0.02 | -7.65 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.13 | 1.60 | -1.88 | 83 |
| 11 | Agent | meta | 99.54 | -0.46 | 23 | 69.6 | -9.85 | -6.53 | -10.20 | 213 |
| 12 | Hold SPY | benchmark | 99.51 | -0.49 | 0 | — | 3.54 | 1.99 | -3.66 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.42 | -0.58 | 0 | — | -3.42 | -2.10 | -5.09 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.33 | -0.67 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 15 | Daily: Bullish score | daily | 99.26 | -0.74 | 2 | 0.0 | -0.95 | 0.06 | -12.76 | 13 |
| 16 | Agent (aggressive) | meta | 99.21 | -0.79 | 9 | 55.6 | -0.95 | -0.46 | -4.81 | 96 |
| 17 | VWAP reversion · 1h | reversion | 99.17 | -0.83 | 20 | 25.0 | -12.91 | -4.41 | -14.72 | 123 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | RSI(14) reversion · 1h | reversion | 99.01 | -0.99 | 7 | 57.1 | 3.77 | 1.01 | -7.31 | 122 |
| 20 | Z-score reversion · 1h | reversion | 98.81 | -1.19 | 10 | 50.0 | 4.51 | 1.10 | -8.60 | 154 |
| 21 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 22 | Williams %R · 1h | reversion | 98.64 | -1.36 | 40 | 45.0 | -17.92 | -3.33 | -19.46 | 488 |
| 23 | Candlestick reversal · 1h | reversion | 98.56 | -1.44 | 20 | 25.0 | -27.75 | -6.87 | -28.45 | 492 |
| 24 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.95 | 3.72 | -4.73 | 183 |
| 25 | Stochastic reversion · 1h | reversion | 98.41 | -1.59 | 26 | 53.8 | -14.15 | -3.12 | -15.20 | 328 |
| 26 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -0.43 | 0.12 | -15.21 | 47 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.34 | -1.66 | 0 | — | 23.34 | 3.47 | -6.29 | 1 |
| 28 | CCI reversion · 1h | reversion | 98.22 | -1.78 | 35 | 34.3 | 0.39 | 0.23 | -12.41 | 410 |
| 29 | Copy: Insider buying | copy | 98.17 | -1.83 | 2 | 100.0 | -14.91 | -2.98 | -17.74 | 72 |
| 30 | Agent (rotation) | meta | 97.89 | -2.10 | 32 | 12.5 | -5.25 | -1.87 | -11.49 | 207 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 97.86 | -2.14 | 0 | — | -11.05 | -2.27 | -15.27 | 2 |
| 32 | EMA 20/50 cross · 1h | trend | 97.85 | -2.15 | 12 | 8.3 | 16.43 | 1.97 | -14.13 | 127 |
| 33 | Connors RSI(2) · 1h | reversion | 97.69 | -2.31 | 45 | 44.4 | -11.63 | -3.72 | -11.84 | 235 |
| 34 | Max aggression: 5-day momentum | meta | 97.68 | -2.33 | 2 | 50.0 | -8.59 | -0.45 | -29.56 | 29 |
| 35 | Squeeze breakout · 1h | breakout | 97.15 | -2.85 | 9 | 11.1 | 13.91 | 2.44 | -6.98 | 98 |
| 36 | Opening range 30m | breakout | 97.08 | -2.92 | 36 | 11.1 | -8.91 | -2.55 | -14.21 | 562 |
| 37 | Bollinger reversion · 1h | reversion | 97.00 | -3.00 | 22 | 27.3 | -18.20 | -5.08 | -18.63 | 313 |
| 38 | Supertrend · 1h | trend | 96.77 | -3.23 | 18 | 5.6 | 3.56 | 0.68 | -16.43 | 191 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.62 | -3.38 | 0 | — | -10.14 | -2.47 | -11.68 | 1 |
| 40 | Trend pullback · 1h | trend | 96.61 | -3.39 | 26 | 11.5 | -28.49 | -6.99 | -29.64 | 149 |
| 41 | Max aggression: 1-day momentum | meta | 96.53 | -3.47 | 2 | 0.0 | -38.04 | -2.26 | -49.44 | 42 |
| 42 | Agent (ML meta-label) | meta | 96.42 | -3.58 | 137 | 13.1 | -0.50 | 0.07 | -12.66 | 386 |
| 43 | MACD cross · 1h | trend | 96.09 | -3.90 | 40 | 10.0 | -19.14 | -3.27 | -22.24 | 461 |
| 44 | Donchian 55/20 · 1h | breakout | 96.01 | -3.99 | 12 | 0.0 | 4.72 | 0.82 | -16.96 | 112 |
| 45 | Parabolic SAR · 1h | trend | 95.89 | -4.11 | 26 | 11.5 | -7.77 | -0.97 | -18.82 | 292 |
| 46 | MFI reversion · 1h | reversion | 95.50 | -4.50 | 44 | 13.6 | -9.86 | -1.82 | -17.28 | 131 |
| 47 | Opening range 15m | breakout | 95.48 | -4.52 | 47 | 10.6 | -10.94 | -2.96 | -16.70 | 684 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -51.31 | -28.11 | -51.45 | 611 |
| 49 | Ichimoku · 1h | trend | 95.25 | -4.75 | 16 | 18.8 | 7.00 | 1.01 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.95 | -5.05 | 17 | 5.9 | 7.18 | 1.13 | -10.78 | 283 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 1.00 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.46 | -5.54 | 24 | 4.2 | 1.79 | 0.45 | -15.29 | 207 |
| 53 | MACD zero-line · 1h | trend | 94.27 | -5.73 | 20 | 5.0 | -5.52 | -0.59 | -14.64 | 223 |
| 54 | Donchian 20/10 · 1h | breakout | 94.05 | -5.95 | 16 | 12.5 | 6.12 | 0.98 | -12.78 | 214 |
| 55 | ADX DI cross · 1h | trend | 94.05 | -5.95 | 30 | 6.7 | -16.30 | -3.05 | -18.12 | 255 |
| 56 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | -7.61 | -0.85 | -18.68 | 216 |
| 57 | Triple EMA stack · 1h | trend | 94.02 | -5.98 | 29 | 6.9 | -7.38 | -0.71 | -22.58 | 229 |
| 58 | VWAP momentum · 1h | momentum | 93.66 | -6.34 | 103 | 12.6 | -34.62 | -5.26 | -35.35 | 1232 |
| 59 | EMA 9/21 cross · 1h | trend | 93.33 | -6.67 | 42 | 11.9 | -3.60 | -0.30 | -16.92 | 307 |
| 60 | Heikin-Ashi · 1h | trend | 92.68 | -7.32 | 44 | 11.4 | -26.60 | -4.07 | -30.64 | 674 |
| 61 | OBV trend · 1h | momentum | 92.49 | -7.51 | 54 | 7.4 | -11.41 | -1.24 | -25.19 | 315 |
| 62 | RSI(14) reversion | reversion | 90.85 | -9.15 | 116 | 35.3 | -71.03 | -21.51 | -71.12 | 1472 |
| 63 | Squeeze breakout | breakout | 89.88 | -10.12 | 82 | 9.8 | -59.63 | -18.51 | -59.97 | 1191 |
| 64 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.71 | -0.39 | -19.29 | 406 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | EMA 20/50 cross | trend | 87.64 | -12.37 | 108 | 14.8 | -78.52 | -17.49 | -78.68 | 1472 |
| 68 | ROC + volume | momentum | 87.63 | -12.37 | 140 | 17.9 | -72.38 | -18.15 | -72.55 | 1613 |
| 69 | Volume breakout | breakout | 87.49 | -12.51 | 99 | 15.2 | -62.06 | -20.64 | -62.28 | 894 |
| 70 | Donchian 55/20 | breakout | 87.14 | -12.86 | 92 | 14.1 | -68.50 | -15.74 | -68.55 | 1307 |
| 71 | Ichimoku | trend | 86.14 | -13.86 | 107 | 8.4 | -80.57 | -26.17 | -80.61 | 1749 |
| 72 | Keltner breakout | breakout | 85.72 | -14.28 | 138 | 11.6 | -85.01 | -34.79 | -85.08 | 1906 |
| 73 | Z-score reversion | reversion | 85.12 | -14.88 | 178 | 33.1 | -84.36 | -27.63 | -84.42 | 2093 |
| 74 | VWAP reversion | reversion | 84.70 | -15.30 | 130 | 20.8 | -71.91 | -17.67 | -72.25 | 1400 |
| 75 | MACD zero-line | trend | 83.36 | -16.64 | 185 | 16.2 | -91.63 | -35.74 | -91.68 | 2351 |
| 76 | Supertrend | trend | 82.75 | -17.25 | 162 | 16.0 | -87.43 | -24.89 | -87.45 | 1961 |
| 77 | Donchian 20/10 | breakout | 81.61 | -18.39 | 184 | 16.3 | -90.94 | -29.72 | -90.99 | 2682 |
| 78 | MFI reversion | reversion | 81.52 | -18.48 | 177 | 19.8 | -87.74 | -35.94 | -87.83 | 2139 |
| 79 | Bollinger breakout | breakout | 81.36 | -18.64 | 189 | 14.3 | -93.93 | -42.53 | -93.96 | 2870 |
| 80 | Triple EMA stack | trend | 80.99 | -19.01 | 197 | 15.2 | -93.06 | -36.13 | -93.09 | 2626 |
| 81 | RSI momentum | momentum | 80.86 | -19.14 | 178 | 11.2 | -90.54 | -29.77 | -90.58 | 2397 |
| 82 | ADX DI cross | trend | 80.19 | -19.81 | 185 | 7.6 | -89.12 | -46.15 | -89.17 | 2104 |
| 83 | Trend pullback | trend | 79.54 | -20.46 | 168 | 17.3 | -90.99 | -35.27 | -90.99 | 2286 |
| 84 | EMA 9/21 cross | trend | 78.19 | -21.81 | 255 | 15.3 | -97.39 | -41.63 | -97.41 | 3538 |
| 85 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.47 | -43.08 | -96.47 | 3641 |
| 86 | Consensus | meta | 76.92 | -23.08 | 185 | 7.0 | -94.56 | -30.41 | -94.57 | 2642 |
| 87 | Stochastic reversion | reversion | 76.27 | -23.73 | 318 | 24.8 | -95.91 | -47.00 | -95.91 | 4058 |
| 88 | Candlestick reversal ⏸ | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.33 | -50.49 | -99.34 | 5580 |
| 89 | OBV trend | momentum | 76.02 | -23.98 | 256 | 14.8 | -95.93 | -49.15 | -95.95 | 3532 |
| 90 | Bollinger reversion | reversion | 75.04 | -24.96 | 301 | 15.9 | -95.77 | -45.48 | -95.77 | 3683 |
| 91 | VWAP momentum | momentum | 74.13 | -25.87 | 353 | 9.6 | -98.41 | -35.91 | -98.42 | 5166 |
| 92 | CCI reversion | reversion | 73.80 | -26.20 | 229 | 11.8 | -98.44 | -51.72 | -98.45 | 4691 |
| 93 | MACD cross | trend | 72.68 | -27.32 | 257 | 13.2 | -99.71 | -67.28 | -99.71 | 6077 |
| 94 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -96.98 | -56.87 | -96.99 | 3639 |
| 95 | Williams %R ⏸ | reversion | 71.59 | -28.41 | 340 | 21.2 | -99.52 | -60.74 | -99.52 | 6105 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -89.38 | -99.89 | 8303 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T19:40 | Agent (ML meta-label) | sell | QQQ | 5.07 | -0.01 | selected signal exited |
| 2026-09-29T19:40 | Agent (ML meta-label) | sell | PLTR | 5.09 | 0.01 | selected signal exited |
| 2026-09-29T19:40 | Bollinger reversion | sell | AAPL | 18.72 | -0.08 | stop-loss |
| 2026-09-29T19:40 | Squeeze breakout | buy | PLTR | 2.45 | — | entry |
| 2026-09-29T19:40 | Squeeze breakout | buy | GOOGL | 7.49 | — | entry |
| 2026-09-29T19:40 | Squeeze breakout | sell | BTC-USD | 9.95 | -0.06 | exit signal |
| 2026-09-29T19:40 | Bollinger breakout | buy | PLTR | 2.82 | — | entry |
| 2026-09-29T19:40 | Bollinger breakout | buy | MSFT | 4.52 | — | entry |
| 2026-09-29T19:40 | Bollinger breakout | sell | BTC-USD | 7.34 | -0.05 | exit signal |
| 2026-09-29T19:40 | RSI momentum | sell | MSTR | 4.47 | -0.03 | exit signal |
| 2026-09-29T19:40 | ROC + volume | sell | TQQQ | 7.80 | -0.03 | exit signal |
| 2026-09-29T19:40 | MACD zero-line | sell | UPRO | 6.38 | -0.00 | target is flat |
| 2026-09-29T19:40 | MACD cross | sell | UPRO | 3.45 | 0.01 | target is flat |
| 2026-09-29T19:40 | Triple EMA stack | buy | TNA | 2.72 | — | entry |
| 2026-09-29T19:40 | Triple EMA stack | buy | SPY | 5.40 | — | entry |
| 2026-09-29T19:40 | Triple EMA stack | sell | AMZN | 8.07 | -0.01 | exit signal |
| 2026-09-29T19:40 | EMA 9/21 cross | buy | MSFT | 2.58 | — | entry |
| 2026-09-29T19:40 | EMA 9/21 cross | buy | GOOGL | 3.91 | — | entry |
| 2026-09-29T19:40 | EMA 9/21 cross | sell | AMZN | 6.49 | 0.01 | exit signal |
| 2026-09-29T19:36 | Agent (ML meta-label) | buy | TQQQ | 5.08 | — | following Candlestick reversal |
| 2026-09-29T19:36 | Agent (ML meta-label) | buy | QQQ | 5.08 | — | entry |
| 2026-09-29T19:36 | Agent (ML meta-label) | buy | PLTR | 5.08 | — | entry |
| 2026-09-29T19:36 | VWAP reversion | buy | TECL | 4.40 | — | rebalance up |
| 2026-09-29T19:36 | VWAP reversion | buy | MSTR | 4.40 | — | rebalance up |
| 2026-09-29T19:36 | VWAP reversion | buy | ETHU | 4.35 | — | rebalance up |
| 2026-09-29T19:36 | VWAP reversion | buy | COIN | 5.10 | — | rebalance up |
| 2026-09-29T19:36 | VWAP reversion | buy | BITX | 4.35 | — | rebalance up |
| 2026-09-29T19:36 | VWAP reversion | buy | AMD | 4.48 | — | rebalance up |
| 2026-09-29T19:36 | VWAP reversion | sell | TNA | 7.72 | 0.05 | exit signal |
| 2026-09-29T19:36 | VWAP reversion | sell | AAPL | 7.63 | -0.05 | stop-loss |
| 2026-09-29T19:36 | Connors RSI(2) | sell | SOXL | 19.28 | 0.00 | exit signal |
| 2026-09-29T19:36 | Supertrend | sell | TSLA | 8.23 | -0.06 | exit signal |
| 2026-09-29T19:36 | MACD zero-line | buy | SOL-USD | 5.20 | — | rebalance up |
| 2026-09-29T19:36 | MACD zero-line | buy | ETH-USD | 4.96 | — | rebalance up |
| 2026-09-29T19:36 | MACD zero-line | sell | SPY | 6.41 | -0.01 | exit signal |
| 2026-09-29T19:36 | MACD zero-line | sell | QQQ | 6.41 | -0.01 | exit signal |
| 2026-09-29T19:36 | MACD zero-line | sell | BTC-USD | 6.40 | -0.04 | exit signal |
| 2026-09-29T19:36 | MACD zero-line | sell | BITX | 6.42 | 0.01 | exit signal |
| 2026-09-29T19:36 | MACD cross | buy | NVDA | 3.66 | — | rebalance up |
| 2026-09-29T19:36 | MACD cross | sell | SPY | 3.45 | -0.00 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
