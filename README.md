# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T17:10:05.000161+00:00 · 5919 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.04 (+0.04%)

Closed trades 21, win rate 71.4%, fees £0.63, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 39.97 | -0.13 |
| TQQQ | 19.99 | -0.02 |

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

Today: 25845 decisions in 2519 calls, $0.3252 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T17:10 | 5 / 13 / 11 | ARKK 17%, DOGE-USD 17%, BITX 16%, META 15% |  |
| Breezy | 2026-09-29T17:10 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-09-29T17:10 | 9 / 19 / 1 | BITX 46%, COIN 42% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 102.21 | 2.21 | 1 | 100.0 | 15.00 | 3.24 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 4 | Agent (aggressive) | meta | 100.04 | 0.04 | 8 | 62.5 | -0.13 | -0.02 | -4.81 | 93 |
| 5 | Agent | meta | 100.04 | 0.04 | 21 | 71.4 | -9.44 | -6.03 | -10.53 | 208 |
| 6 | Copy: Congress Democrats (NANC) | copy | 100.02 | 0.02 | 0 | — | 8.74 | 3.35 | -3.62 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 10.17 | 1.94 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.45 | 1.78 | -1.51 | 83 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 99.64 | -0.36 | 0 | — | -1.57 | -0.60 | -7.65 | 1 |
| 12 | Hold BTC | benchmark | 99.59 | -0.41 | 0 | — | 28.98 | 3.66 | -8.68 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 99.47 | -0.53 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 14 | Hold SPY | benchmark | 99.39 | -0.61 | 0 | — | 3.36 | 1.72 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.88 | -4.39 | -14.73 | 121 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 99.26 | -0.74 | 0 | — | -3.70 | -2.28 | -5.09 | 2 |
| 17 | RSI(14) reversion · 1h | reversion | 99.23 | -0.77 | 7 | 57.1 | 1.32 | 0.46 | -6.57 | 119 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 20 | Daily: Bullish score | daily | 98.72 | -1.28 | 2 | 0.0 | -1.77 | -0.05 | -12.76 | 13 |
| 21 | Z-score reversion · 1h | reversion | 98.61 | -1.39 | 9 | 44.4 | 4.19 | 1.03 | -8.60 | 153 |
| 22 | Williams %R · 1h | reversion | 98.58 | -1.42 | 39 | 46.2 | -18.34 | -3.39 | -19.64 | 482 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.64 | 3.88 | -4.73 | 195 |
| 24 | Copy: Insider buying | copy | 98.39 | -1.61 | 2 | 100.0 | -14.79 | -2.95 | -17.74 | 72 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.38 | -1.62 | 0 | — | 24.54 | 3.54 | -6.29 | 1 |
| 26 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.35 | -0.03 | -15.21 | 47 |
| 27 | Candlestick reversal · 1h | reversion | 98.24 | -1.76 | 18 | 27.8 | -27.01 | -6.56 | -27.32 | 484 |
| 28 | Agent (rotation) | meta | 98.23 | -1.77 | 32 | 12.5 | -5.30 | -1.80 | -11.62 | 217 |
| 29 | CCI reversion · 1h | reversion | 97.98 | -2.02 | 34 | 35.3 | 1.95 | 0.49 | -12.41 | 405 |
| 30 | Max aggression: 5-day momentum | meta | 97.86 | -2.14 | 2 | 50.0 | -8.54 | -0.44 | -29.56 | 29 |
| 31 | Connors RSI(2) · 1h | reversion | 97.85 | -2.15 | 41 | 46.3 | -12.99 | -4.11 | -13.22 | 236 |
| 32 | Stochastic reversion · 1h | reversion | 97.85 | -2.15 | 26 | 53.8 | -13.81 | -3.10 | -14.36 | 319 |
| 33 | EMA 20/50 cross · 1h | trend | 97.69 | -2.31 | 10 | 10.0 | 15.06 | 1.83 | -14.36 | 128 |
| 34 | Squeeze breakout · 1h | breakout | 97.31 | -2.69 | 9 | 11.1 | 15.16 | 2.67 | -6.18 | 97 |
| 35 | Daily: SMA 20/50 cross · AAPL | daily | 97.22 | -2.78 | 0 | — | -10.22 | -2.51 | -12.73 | 1 |
| 36 | Timing: Nasdaq FTD · TQQQ | daily | 97.15 | -2.85 | 0 | — | -11.82 | -2.46 | -15.27 | 2 |
| 37 | Opening range 30m | breakout | 97.12 | -2.88 | 35 | 11.4 | -9.05 | -2.60 | -14.00 | 562 |
| 38 | Supertrend · 1h | trend | 96.93 | -3.07 | 17 | 5.9 | 3.76 | 0.70 | -16.43 | 197 |
| 39 | Bollinger reversion · 1h | reversion | 96.77 | -3.23 | 22 | 27.3 | -18.22 | -5.10 | -18.33 | 309 |
| 40 | Agent (ML meta-label) | meta | 96.42 | -3.58 | 118 | 11.0 | -2.30 | -0.27 | -12.57 | 380 |
| 41 | MACD cross · 1h | trend | 96.34 | -3.66 | 37 | 10.8 | -18.19 | -3.09 | -21.49 | 459 |
| 42 | Trend pullback · 1h | trend | 96.21 | -3.79 | 25 | 12.0 | -29.47 | -7.26 | -29.92 | 148 |
| 43 | Donchian 55/20 · 1h | breakout | 96.10 | -3.90 | 12 | 0.0 | 4.68 | 0.82 | -16.96 | 112 |
| 44 | Ichimoku · 1h | trend | 95.59 | -4.41 | 15 | 13.3 | 6.55 | 0.97 | -15.13 | 121 |
| 45 | Opening range 15m | breakout | 95.52 | -4.48 | 46 | 10.9 | -10.81 | -2.92 | -16.49 | 694 |
| 46 | Parabolic SAR · 1h | trend | 95.36 | -4.64 | 26 | 11.5 | -8.55 | -1.09 | -18.82 | 291 |
| 47 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -51.91 | -28.90 | -52.12 | 624 |
| 48 | Bollinger breakout · 1h | breakout | 95.33 | -4.67 | 17 | 5.9 | 8.08 | 1.25 | -10.12 | 284 |
| 49 | Max aggression: 1-day momentum | meta | 95.16 | -4.84 | 2 | 0.0 | -39.00 | -2.35 | -49.44 | 42 |
| 50 | MFI reversion · 1h | reversion | 95.00 | -5.00 | 43 | 11.6 | -10.39 | -1.93 | -17.20 | 126 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 26 | 3.8 | 5.90 | 1.00 | -12.60 | 125 |
| 52 | MACD zero-line · 1h | trend | 94.62 | -5.38 | 19 | 5.3 | -5.49 | -0.59 | -14.64 | 222 |
| 53 | ADX DI cross · 1h | trend | 94.52 | -5.48 | 29 | 6.9 | -12.62 | -2.37 | -15.39 | 253 |
| 54 | RSI momentum · 1h | momentum | 94.48 | -5.52 | 24 | 4.2 | -1.65 | -0.03 | -15.29 | 212 |
| 55 | Donchian 20/10 · 1h | breakout | 94.36 | -5.64 | 15 | 13.3 | 7.15 | 1.10 | -12.78 | 216 |
| 56 | Keltner breakout · 1h | breakout | 94.16 | -5.84 | 9 | 0.0 | -3.60 | -0.26 | -18.68 | 215 |
| 57 | Triple EMA stack · 1h | trend | 94.07 | -5.93 | 29 | 6.9 | -6.55 | -0.59 | -22.92 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.88 | -6.12 | 101 | 12.9 | -31.03 | -4.56 | -35.02 | 1235 |
| 59 | EMA 9/21 cross · 1h | trend | 93.60 | -6.40 | 40 | 12.5 | -4.17 | -0.38 | -16.92 | 310 |
| 60 | OBV trend · 1h | momentum | 92.87 | -7.13 | 52 | 7.7 | -9.94 | -1.05 | -25.24 | 327 |
| 61 | Heikin-Ashi · 1h | trend | 92.68 | -7.32 | 41 | 12.2 | -23.64 | -3.54 | -30.58 | 677 |
| 62 | RSI(14) reversion | reversion | 90.92 | -9.08 | 103 | 33.0 | -71.20 | -21.71 | -71.44 | 1473 |
| 63 | Squeeze breakout | breakout | 89.71 | -10.29 | 80 | 10.0 | -59.76 | -18.57 | -60.01 | 1176 |
| 64 | ROC + volume · 1h | momentum | 89.57 | -10.43 | 51 | 5.9 | -4.73 | -0.40 | -18.97 | 407 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | EMA 20/50 cross | trend | 87.46 | -12.54 | 106 | 15.1 | -78.55 | -17.60 | -78.67 | 1465 |
| 68 | ROC + volume | momentum | 87.43 | -12.57 | 133 | 17.3 | -73.25 | -18.51 | -73.30 | 1634 |
| 69 | Donchian 55/20 | breakout | 87.40 | -12.60 | 91 | 14.3 | -68.49 | -15.72 | -68.49 | 1305 |
| 70 | Volume breakout | breakout | 87.31 | -12.69 | 90 | 12.2 | -62.02 | -20.61 | -62.02 | 885 |
| 71 | Ichimoku | trend | 86.16 | -13.84 | 105 | 8.6 | -80.34 | -26.20 | -80.37 | 1758 |
| 72 | Keltner breakout | breakout | 85.50 | -14.50 | 138 | 11.6 | -85.11 | -35.86 | -85.11 | 1903 |
| 73 | Z-score reversion | reversion | 85.16 | -14.84 | 162 | 30.2 | -84.36 | -27.63 | -84.39 | 2091 |
| 74 | VWAP reversion | reversion | 84.58 | -15.42 | 121 | 18.2 | -71.75 | -17.49 | -72.24 | 1398 |
| 75 | MACD zero-line | trend | 83.16 | -16.84 | 172 | 14.5 | -91.64 | -36.33 | -91.66 | 2355 |
| 76 | Supertrend | trend | 82.89 | -17.11 | 158 | 16.5 | -87.63 | -25.38 | -87.63 | 1961 |
| 77 | MFI reversion | reversion | 81.63 | -18.37 | 170 | 18.8 | -87.64 | -35.42 | -87.75 | 2159 |
| 78 | Donchian 20/10 | breakout | 81.42 | -18.58 | 178 | 16.9 | -90.99 | -30.65 | -91.02 | 2685 |
| 79 | Bollinger breakout | breakout | 81.04 | -18.96 | 185 | 14.6 | -94.05 | -43.04 | -94.05 | 2855 |
| 80 | Triple EMA stack | trend | 80.95 | -19.05 | 193 | 14.5 | -93.07 | -36.62 | -93.07 | 2614 |
| 81 | RSI momentum | momentum | 80.70 | -19.30 | 173 | 11.6 | -90.55 | -29.85 | -90.55 | 2383 |
| 82 | ADX DI cross | trend | 80.15 | -19.85 | 181 | 6.6 | -89.37 | -46.59 | -89.43 | 2100 |
| 83 | Trend pullback | trend | 80.02 | -19.98 | 164 | 17.7 | -90.90 | -35.22 | -90.90 | 2284 |
| 84 | EMA 9/21 cross | trend | 77.98 | -22.02 | 249 | 15.3 | -97.35 | -41.84 | -97.36 | 3535 |
| 85 | Consensus | meta | 77.16 | -22.84 | 179 | 7.3 | -94.57 | -30.52 | -94.58 | 2637 |
| 86 | Connors RSI(2) | reversion | 77.15 | -22.85 | 236 | 16.1 | -96.49 | -43.15 | -96.49 | 3651 |
| 87 | Stochastic reversion | reversion | 76.44 | -23.56 | 294 | 22.4 | -95.93 | -47.93 | -95.98 | 4066 |
| 88 | Candlestick reversal ⏸ | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.35 | -51.90 | -99.35 | 5576 |
| 89 | OBV trend | momentum | 75.90 | -24.10 | 251 | 13.9 | -95.98 | -49.77 | -95.98 | 3540 |
| 90 | Bollinger reversion | reversion | 75.26 | -24.74 | 280 | 13.9 | -95.78 | -46.17 | -95.81 | 3688 |
| 91 | VWAP momentum | momentum | 74.23 | -25.77 | 345 | 9.9 | -98.44 | -36.70 | -98.46 | 5196 |
| 92 | CCI reversion | reversion | 73.98 | -26.02 | 203 | 8.4 | -98.45 | -52.25 | -98.45 | 4692 |
| 93 | MACD cross | trend | 72.69 | -27.31 | 230 | 11.3 | -99.71 | -67.72 | -99.71 | 6098 |
| 94 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -97.00 | -57.04 | -97.00 | 3651 |
| 95 | Williams %R | reversion | 71.99 | -28.02 | 302 | 20.2 | -99.52 | -60.71 | -99.53 | 6100 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.70 | -99.89 | 8308 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T17:10 | Agent (ML meta-label) | sell | SPY | 3.88 | -0.01 | selected signal exited |
| 2026-09-29T17:10 | MFI reversion · 1h | sell | SPY | 19.14 | -0.13 | stop-loss |
| 2026-09-29T17:10 | MFI reversion | sell | MSTR | 11.73 | 0.01 | exit signal |
| 2026-09-29T17:10 | Bollinger reversion | buy | XRP-USD | 5.79 | — | entry |
| 2026-09-29T17:10 | Bollinger reversion | buy | TNA | 4.32 | — | rebalance up |
| 2026-09-29T17:10 | Bollinger reversion | sell | ETHU | 5.81 | -0.02 | exit signal |
| 2026-09-29T17:10 | Bollinger reversion | sell | ETH-USD | 5.79 | -0.04 | exit signal |
| 2026-09-29T17:10 | Connors RSI(2) | sell | SOXL | 19.31 | -0.01 | exit signal |
| 2026-09-29T17:10 | Volume breakout | sell | AMZN | 21.77 | -0.07 | exit signal |
| 2026-09-29T17:10 | Squeeze breakout | sell | AMZN | 22.37 | -0.08 | stop-loss |
| 2026-09-29T17:10 | Bollinger breakout | sell | AMZN | 20.21 | -0.07 | stop-loss |
| 2026-09-29T17:10 | Opening range 30m | sell | MSFT | 24.20 | -0.14 | stop-loss |
| 2026-09-29T17:10 | Opening range 30m | sell | AMZN | 24.22 | -0.11 | stop-loss |
| 2026-09-29T17:10 | Opening range 15m | sell | MSFT | 23.80 | -0.13 | stop-loss |
| 2026-09-29T17:10 | Opening range 15m | sell | AMZN | 23.82 | -0.11 | stop-loss |
| 2026-09-29T17:10 | Donchian 55/20 | sell | AMZN | 21.77 | -0.10 | stop-loss |
| 2026-09-29T17:10 | ROC + volume | buy | LABU | 21.86 | — | entry |
| 2026-09-29T17:10 | Supertrend | sell | MSFT | 16.64 | -0.11 | exit signal |
| 2026-09-29T17:10 | MACD zero-line | buy | GOOGL | 20.76 | — | entry signal |
| 2026-09-29T17:05 | Agent (ML meta-label) | sell | TNA | 5.67 | -0.01 | selected signal exited |
| 2026-09-29T17:05 | Agent (ML meta-label) | sell | COIN | 5.67 | 0.00 | selected signal exited |
| 2026-09-29T17:05 | CCI reversion | buy | TECL | 4.12 | — | entry |
| 2026-09-29T17:05 | CCI reversion | sell | MSTR | 4.12 | 0.01 | exit signal |
| 2026-09-29T17:05 | Keltner breakout | buy | LABU | 21.39 | — | entry signal |
| 2026-09-29T17:05 | Bollinger breakout | sell | META | 20.20 | -0.10 | exit signal |
| 2026-09-29T17:05 | RSI momentum | buy | LABU | 20.21 | — | entry signal |
| 2026-09-29T17:05 | VWAP momentum | sell | MSFT | 18.52 | -0.06 | exit signal |
| 2026-09-29T17:00 | Agent (ML meta-label) | buy | TNA | 5.67 | — | entry |
| 2026-09-29T17:00 | Agent (ML meta-label) | sell | XRP-USD | 2.67 | -0.13 | selected signal exited |
| 2026-09-29T17:00 | Agent | buy | TQQQ | 20.01 | — | following Candlestick reversal |
| 2026-09-29T17:00 | VWAP momentum · 1h | sell | XRP-USD | 23.13 | -0.75 | exit signal |
| 2026-09-29T17:00 | Parabolic SAR · 1h | buy | SOXL | 4.95 | — | rebalance up |
| 2026-09-29T17:00 | Parabolic SAR · 1h | sell | XRP-USD | 18.64 | -0.47 | exit signal |
| 2026-09-29T17:00 | Supertrend · 1h | buy | TECL | 5.17 | — | rebalance up |
| 2026-09-29T17:00 | Supertrend · 1h | buy | NVDA | 5.32 | — | rebalance up |
| 2026-09-29T17:00 | Supertrend · 1h | buy | BTC-USD | 6.48 | — | rebalance up |
| 2026-09-29T17:00 | Supertrend · 1h | sell | XRP-USD | 11.90 | -0.37 | exit signal |
| 2026-09-29T17:00 | MACD cross · 1h | buy | SQQQ | 5.05 | — | rebalance up |
| 2026-09-29T17:00 | MACD cross · 1h | buy | SOL-USD | 7.17 | — | rebalance up |
| 2026-09-29T17:00 | MACD cross · 1h | buy | NVDA | 5.35 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
