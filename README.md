# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-02T18:36:05.000169+00:00 · 9162 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.24 (-0.76%)

Closed trades 32, win rate 65.6%, fees £0.92, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, ETRA 12%, BBD 12%, BPRE 12%, GME 12%, NYAX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-01)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.51 · VIX 16.39 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.6, PLTR 8.5, META 7.7, AMD 7.5, TECL 7.1, BITX 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 31047 decisions in 2634 calls, $0.3856 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-02T18:36 | 0 / 13 / 17 | PLTR 14% |  |
| Breezy | 2026-10-02T18:36 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-02T18:36 | 0 / 26 / 4 | COIN 50% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| Bollinger reversion · 1h | UPRO | 2.12 | +4.42% | 3 |
| Connors RSI(2) · 1h | TQQQ | 2.12 | +4.58% | 4 |
| Z-score reversion | MSFT | 2.05 | +2.32% | 5 |
| Stochastic reversion · 1h | SPY | 2.03 | +1.53% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.08 | 2.08 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 101.91 | 1.91 | 0 | — | -7.32 | -1.34 | -15.27 | 2 |
| 3 | Hold BTC | benchmark | 101.04 | 1.04 | 0 | — | 34.98 | 4.26 | -8.68 | 1 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.84 | 0.84 | 0 | — | 4.08 | 1.86 | -3.62 | 1 |
| 5 | Timing: Nasdaq FTD · QQQ | daily | 100.78 | 0.78 | 0 | — | -2.04 | -1.15 | -5.09 | 2 |
| 6 | Candlestick reversal · 1h | reversion | 100.61 | 0.60 | 53 | 37.7 | -23.22 | -5.30 | -26.16 | 490 |
| 7 | RSI(14) reversion · 1h | reversion | 100.32 | 0.32 | 10 | 60.0 | 4.68 | 1.35 | -6.57 | 117 |
| 8 | Hold SPY | benchmark | 100.04 | 0.04 | 0 | — | 1.83 | 1.09 | -3.66 | 1 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Bollinger reversion · 1h | reversion | 99.94 | -0.06 | 38 | 44.7 | -14.92 | -3.98 | -17.66 | 303 |
| 12 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 24 | 33.3 | -10.50 | -3.54 | -14.05 | 111 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 15 | 33.3 | 3.90 | 1.94 | -1.46 | 86 |
| 14 | Daily: Bullish score | daily | 99.78 | -0.22 | 3 | 0.0 | 2.02 | 0.47 | -12.76 | 14 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.68 | -0.32 | 0 | — | -2.26 | -0.87 | -7.65 | 1 |
| 16 | Z-score reversion · 1h | reversion | 99.59 | -0.41 | 17 | 58.8 | 5.32 | 1.23 | -8.60 | 157 |
| 17 | Donchian 55/20 · 1h | breakout | 99.56 | -0.44 | 17 | 0.0 | 6.56 | 1.03 | -16.96 | 115 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.45 | -5.95 | -11.27 | 222 |
| 20 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 99.12 | -0.88 | 0 | — | -2.59 | -1.22 | -5.14 | 1 |
| 22 | Stochastic reversion · 1h | reversion | 98.85 | -1.15 | 40 | 60.0 | -8.55 | -1.77 | -9.82 | 329 |
| 23 | Trend pullback · 1h | trend | 98.78 | -1.22 | 45 | 20.0 | -23.69 | -6.08 | -25.92 | 166 |
| 24 | CCI reversion · 1h | reversion | 98.71 | -1.29 | 63 | 49.2 | 2.13 | 0.51 | -12.41 | 412 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 98.59 | -1.41 | 0 | — | 22.87 | 3.42 | -6.29 | 1 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.97 | -0.47 | -4.23 | 104 |
| 29 | Connors RSI(2) · 1h | reversion | 98.00 | -2.00 | 53 | 49.1 | -12.22 | -4.14 | -13.59 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.80 | -2.20 | 24 | 8.3 | 13.53 | 1.70 | -14.40 | 129 |
| 31 | Agent (rotation) | meta | 97.78 | -2.22 | 48 | 18.8 | -3.70 | -1.39 | -8.90 | 228 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.70 | -2.30 | 0 | — | 0.16 | 0.15 | -5.18 | 1 |
| 34 | Williams %R · 1h | reversion | 97.43 | -2.57 | 69 | 55.1 | -16.88 | -3.09 | -19.41 | 495 |
| 35 | Agent (ML meta-label) | meta | 96.76 | -3.24 | 202 | 17.8 | 0.97 | 0.32 | -13.23 | 369 |
| 36 | MFI reversion · 1h | reversion | 96.64 | -3.36 | 68 | 29.4 | -6.03 | -0.97 | -16.99 | 121 |
| 37 | Daily: Momentum burst | daily | 96.49 | -3.51 | 3 | 0.0 | -1.60 | -0.07 | -16.85 | 46 |
| 38 | Parabolic SAR · 1h | trend | 96.37 | -3.63 | 46 | 15.2 | -8.06 | -0.99 | -19.70 | 312 |
| 39 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.84 | 2.87 | -4.73 | 199 |
| 40 | Supertrend · 1h | trend | 96.01 | -3.99 | 25 | 8.0 | 2.57 | 0.53 | -16.43 | 202 |
| 41 | Max aggression: 1-day momentum | meta | 96.00 | -4.00 | 5 | 40.0 | -23.48 | -1.18 | -41.28 | 43 |
| 42 | ADX DI cross · 1h | trend | 95.88 | -4.12 | 41 | 12.2 | -5.65 | -0.79 | -13.84 | 271 |
| 43 | MACD cross · 1h | trend | 95.43 | -4.57 | 69 | 14.5 | -16.00 | -2.56 | -18.30 | 487 |
| 44 | Squeeze breakout · 1h | breakout | 95.22 | -4.78 | 22 | 18.2 | 19.93 | 2.87 | -8.06 | 113 |
| 45 | Copy: Insider buying | copy | 95.20 | -4.80 | 4 | 50.0 | -19.45 | -3.82 | -21.24 | 71 |
| 46 | Opening range 30m | breakout | 95.20 | -4.80 | 68 | 17.6 | -13.90 | -4.14 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.18 | -5.82 | 30 | 16.7 | 5.83 | 0.87 | -16.19 | 129 |
| 48 | RSI momentum · 1h | momentum | 93.90 | -6.10 | 39 | 2.6 | 1.31 | 0.37 | -16.65 | 228 |
| 49 | VWAP momentum · 1h | momentum | 93.69 | -6.31 | 170 | 22.9 | -40.43 | -6.32 | -42.55 | 1277 |
| 50 | Bollinger breakout · 1h | breakout | 93.14 | -6.86 | 36 | 16.7 | 5.20 | 0.86 | -12.06 | 293 |
| 51 | Opening range 15m | breakout | 93.08 | -6.92 | 85 | 16.5 | -16.16 | -4.57 | -18.84 | 695 |
| 52 | Triple EMA stack · 1h | trend | 93.01 | -6.99 | 49 | 6.1 | -8.27 | -0.81 | -23.88 | 244 |
| 53 | Three white soldiers | momentum | 92.82 | -7.18 | 64 | 17.2 | -49.14 | -26.00 | -49.34 | 593 |
| 54 | Volume breakout · 1h | breakout | 92.43 | -7.57 | 30 | 6.7 | 2.74 | 0.57 | -12.60 | 129 |
| 55 | EMA 9/21 cross · 1h | trend | 91.71 | -8.29 | 65 | 10.8 | -4.93 | -0.48 | -18.47 | 342 |
| 56 | Heikin-Ashi · 1h | trend | 91.32 | -8.68 | 85 | 25.9 | -32.78 | -5.81 | -33.58 | 687 |
| 57 | Max aggression: 5-day momentum | meta | 91.17 | -8.83 | 5 | 40.0 | -21.49 | -1.93 | -29.56 | 30 |
| 58 | MACD zero-line · 1h | trend | 90.69 | -9.31 | 36 | 8.3 | -5.62 | -0.53 | -18.32 | 237 |
| 59 | Donchian 20/10 · 1h | breakout | 90.65 | -9.36 | 31 | 12.9 | -1.36 | 0.05 | -16.18 | 222 |
| 60 | OBV trend · 1h | momentum | 89.46 | -10.54 | 96 | 10.4 | -15.71 | -1.81 | -26.61 | 341 |
| 61 | Keltner breakout · 1h | breakout | 88.25 | -11.75 | 22 | 0.0 | -11.42 | -1.36 | -23.19 | 213 |
| 62 | RSI(14) reversion | reversion | 88.08 | -11.92 | 168 | 35.7 | -72.22 | -20.90 | -72.22 | 1455 |
| 63 | ROC + volume · 1h | momentum | 87.14 | -12.86 | 83 | 14.5 | -13.98 | -1.82 | -24.41 | 421 |
| 64 | Squeeze breakout | breakout | 83.11 | -16.89 | 169 | 16.0 | -60.16 | -18.15 | -60.88 | 1210 |
| 65 | Donchian 55/20 | breakout | 82.38 | -17.61 | 168 | 18.5 | -68.11 | -15.26 | -68.40 | 1308 |
| 66 | Volume breakout | breakout | 80.20 | -19.80 | 155 | 14.2 | -64.19 | -20.08 | -64.23 | 914 |
| 67 | EMA 20/50 cross | trend | 80.16 | -19.84 | 191 | 18.8 | -78.85 | -16.71 | -79.03 | 1478 |
| 68 | VWAP reversion | reversion | 79.95 | -20.05 | 188 | 27.1 | -71.07 | -17.09 | -71.10 | 1384 |
| 69 | ROC + volume | momentum | 79.82 | -20.18 | 257 | 20.2 | -73.89 | -17.92 | -74.15 | 1661 |
| 70 | AI bee: Bizzy | ai | 79.09 | -20.91 | 380 | 10.8 | — | — | — | — |
| 71 | Z-score reversion | reversion | 78.06 | -21.94 | 266 | 31.6 | -85.78 | -26.89 | -85.78 | 2106 |
| 72 | AI bee: Boozy | ai | 77.74 | -22.26 | 134 | 3.7 | — | — | — | — |
| 73 | MFI reversion | reversion | 76.50 | -23.50 | 252 | 22.2 | -88.25 | -33.37 | -88.26 | 2141 |
| 74 | Keltner breakout | breakout | 76.22 | -23.78 | 243 | 13.6 | -85.25 | -32.02 | -85.34 | 1901 |
| 75 | Ichimoku | trend | 75.86 | -24.14 | 206 | 10.2 | -81.51 | -25.46 | -81.62 | 1768 |
| 76 | Supertrend | trend | 75.24 | -24.76 | 263 | 20.5 | -87.35 | -23.50 | -87.38 | 1948 |
| 77 | Donchian 20/10 | breakout | 72.50 | -27.50 | 335 | 19.1 | -90.79 | -27.87 | -90.85 | 2682 |
| 78 | MACD zero-line | trend | 71.87 | -28.12 | 324 | 16.7 | -91.69 | -32.31 | -91.69 | 2360 |
| 79 | ADX DI cross | trend | 71.77 | -28.23 | 297 | 9.4 | -89.68 | -40.80 | -89.78 | 2117 |
| 80 | Trend pullback | trend | 70.99 | -29.01 | 309 | 16.8 | -91.65 | -33.13 | -91.66 | 2346 |
| 81 | Triple EMA stack | trend | 70.92 | -29.08 | 346 | 16.8 | -93.21 | -33.93 | -93.24 | 2631 |
| 82 | Bollinger breakout | breakout | 70.10 | -29.90 | 337 | 16.3 | -93.95 | -38.32 | -93.95 | 2854 |
| 83 | RSI momentum | momentum | 70.05 | -29.95 | 321 | 15.6 | -90.64 | -27.70 | -90.73 | 2401 |
| 84 | Stochastic reversion | reversion | 68.10 | -31.90 | 497 | 25.4 | -95.83 | -41.17 | -95.83 | 4062 |
| 85 | Consensus ⏸ | meta | 67.00 | -33.00 | 319 | 9.7 | -94.79 | -29.16 | -94.79 | 2665 |
| 86 | Bollinger reversion | reversion | 66.46 | -33.54 | 484 | 18.6 | -95.88 | -40.23 | -95.88 | 3721 |
| 87 | Connors RSI(2) ⏸ | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.66 | -39.10 | -96.66 | 3658 |
| 88 | EMA 9/21 cross | trend | 65.53 | -34.47 | 448 | 17.9 | -97.40 | -37.53 | -97.42 | 3556 |
| 89 | OBV trend | momentum | 64.10 | -35.90 | 494 | 16.0 | -96.13 | -43.08 | -96.14 | 3590 |
| 90 | CCI reversion | reversion | 63.73 | -36.27 | 441 | 17.5 | -98.50 | -44.11 | -98.50 | 4715 |
| 91 | Candlestick reversal ⏸ | reversion | 63.68 | -36.32 | 565 | 16.8 | -99.34 | -43.56 | -99.34 | 5650 |
| 92 | VWAP momentum | momentum | 62.76 | -37.24 | 520 | 9.4 | -98.61 | -33.52 | -98.61 | 5317 |
| 93 | Parabolic SAR | trend | 61.43 | -38.57 | 461 | 14.8 | -97.17 | -48.24 | -97.18 | 3669 |
| 94 | MACD cross ⏸ | trend | 59.48 | -40.52 | 545 | 14.9 | -99.72 | -52.79 | -99.72 | 6155 |
| 95 | Williams %R ⏸ | reversion | 59.36 | -40.64 | 582 | 23.0 | -99.52 | -49.18 | -99.52 | 6139 |
| 96 | Heikin-Ashi ⏸ | trend | 58.33 | -41.67 | 502 | 10.0 | -99.90 | -62.63 | -99.90 | 8336 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-02T18:35 | CCI reversion | buy | TNA | 3.54 | — | entry signal |
| 2026-10-02T18:35 | CCI reversion | buy | IWM | 3.54 | — | entry signal |
| 2026-10-02T18:35 | CCI reversion | buy | AAPL | 3.54 | — | entry signal |
| 2026-10-02T18:35 | CCI reversion | sell | XRP-USD | 3.50 | -0.05 | stop-loss |
| 2026-10-02T18:35 | CCI reversion | sell | SOL-USD | 3.53 | -0.06 | stop-loss |
| 2026-10-02T18:35 | CCI reversion | sell | COIN | 3.53 | -0.05 | stop-loss |
| 2026-10-02T18:35 | Stochastic reversion | buy | SOL-USD | 2.60 | — | entry |
| 2026-10-02T18:35 | Stochastic reversion | buy | DOGE-USD | 4.87 | — | entry |
| 2026-10-02T18:35 | Stochastic reversion | sell | XRP-USD | 7.47 | -0.13 | stop-loss |
| 2026-10-02T18:35 | Z-score reversion | sell | SOL-USD | 19.41 | -0.29 | stop-loss |
| 2026-10-02T18:35 | Z-score reversion | sell | ETH-USD | 15.65 | -0.17 | stop-loss |
| 2026-10-02T18:35 | Bollinger reversion | buy | GOOGL | 2.12 | — | rebalance up |
| 2026-10-02T18:35 | Bollinger reversion | buy | COIN | 5.28 | — | rebalance up |
| 2026-10-02T18:35 | Bollinger reversion | sell | AAPL | 7.40 | 0.00 | exit signal |
| 2026-10-02T18:35 | Candlestick reversal | sell | TNA | 4.56 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | SOXL | 7.11 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | SOL-USD | 4.11 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | PLTR | 4.01 | -0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | NVDA | 5.35 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | MSTR | 3.98 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | META | 4.56 | -0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | ETHU | 4.55 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | ETH-USD | 7.06 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | COIN | 3.98 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | BTC-USD | 4.53 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | BITX | 5.32 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | Candlestick reversal | sell | AMZN | 4.55 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-02T18:35 | ADX DI cross | sell | XRP-USD | 17.71 | -0.32 | stop-loss |
| 2026-10-02T18:33 | AI bee: Bizzy | buy | PLTR | 11.21 | — | Jev: buy (buy p=0.57) |
| 2026-10-02T18:33 | AI bee: Bizzy | sell | AMD | 12.72 | -0.03 | Jev: sell (sell p=0.82) after 11 min |
| 2026-10-02T18:30 | Connors RSI(2) · 1h | buy | MSTR | 24.55 | — | entry signal |
| 2026-10-02T18:30 | OBV trend · 1h | buy | MSFT | 11.19 | — | entry signal |
| 2026-10-02T18:30 | OBV trend · 1h | sell | META | 9.97 | -0.05 | exit signal |
| 2026-10-02T18:30 | VWAP momentum · 1h | buy | SQQQ | 23.43 | — | entry signal |
| 2026-10-02T18:30 | VWAP momentum · 1h | sell | GOOGL | 23.40 | -0.05 | exit signal |
| 2026-10-02T18:30 | Heikin-Ashi · 1h | sell | UPRO | 22.86 | 0.09 | exit signal |
| 2026-10-02T18:30 | Heikin-Ashi · 1h | sell | SPY | 22.85 | -0.00 | exit signal |
| 2026-10-02T18:30 | Triple EMA stack · 1h | buy | SPY | 8.46 | — | entry signal |
| 2026-10-02T18:30 | Triple EMA stack · 1h | sell | ETHU | 8.21 | -0.23 | exit signal |
| 2026-10-02T18:30 | EMA 20/50 cross · 1h | buy | SPY | 10.88 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
