# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-02T16:06:05.000167+00:00 · 9033 ticks

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

Today: 19545 decisions in 2247 calls, $0.2508 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-02T16:06 | 2 / 19 / 10 | TECL 14%, SOXL 14% |  |
| Breezy | 2026-10-02T16:06 | 0 / 30 / 1 | cash |  |
| Boozy | 2026-10-02T16:06 | 0 / 29 / 2 | MSTR 70% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.51 | 2.51 | 0 | — | -6.67 | -1.18 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.12 | 2.12 | 0 | — | 2.95 | 0.89 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 102.09 | 2.09 | 0 | — | 35.43 | 4.30 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 100.92 | 0.92 | 0 | — | -1.81 | -1.00 | -5.09 | 2 |
| 5 | Daily: Bullish score | daily | 100.81 | 0.81 | 3 | 0.0 | 3.17 | 0.63 | -12.76 | 14 |
| 6 | Copy: Congress Democrats (NANC) | copy | 100.45 | 0.46 | 0 | — | 3.79 | 1.73 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 100.33 | 0.33 | 17 | 0.0 | 7.48 | 1.14 | -16.96 | 115 |
| 8 | Candlestick reversal · 1h | reversion | 100.30 | 0.30 | 53 | 37.7 | -23.37 | -5.37 | -26.09 | 491 |
| 9 | RSI(14) reversion · 1h | reversion | 100.11 | 0.12 | 10 | 60.0 | 3.88 | 1.13 | -6.57 | 123 |
| 10 | Hold SPY | benchmark | 100.01 | 0.01 | 0 | — | 1.90 | 1.13 | -3.66 | 1 |
| 11 | Stochastic reversion · 1h | reversion | 100.00 | 0.00 | 40 | 60.0 | -7.83 | -1.62 | -9.86 | 328 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Day trade: Stocks in Play ORB | daytrade | 99.95 | -0.05 | 15 | 33.3 | 4.02 | 2.00 | -1.46 | 86 |
| 15 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 24 | 33.3 | -11.06 | -3.75 | -14.05 | 111 |
| 16 | Bollinger reversion · 1h | reversion | 99.73 | -0.27 | 38 | 44.7 | -15.10 | -4.05 | -17.68 | 303 |
| 17 | Z-score reversion · 1h | reversion | 99.61 | -0.39 | 17 | 58.8 | 5.38 | 1.25 | -8.60 | 156 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 19 | Copy: Warren Buffett (BRK-B) | copy | 99.31 | -0.69 | 0 | — | -2.52 | -0.98 | -7.65 | 1 |
| 20 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.45 | -5.95 | -11.27 | 222 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | EMA 20/50 cross · 1h | trend | 99.19 | -0.81 | 23 | 8.7 | 15.82 | 1.93 | -14.40 | 128 |
| 23 | Trend pullback · 1h | trend | 99.10 | -0.90 | 44 | 20.5 | -22.87 | -5.77 | -25.84 | 162 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.02 | -0.98 | 0 | — | -2.59 | -1.22 | -5.14 | 1 |
| 25 | CCI reversion · 1h | reversion | 98.98 | -1.02 | 63 | 49.2 | 1.99 | 0.49 | -12.41 | 413 |
| 26 | Connors RSI(2) · 1h | reversion | 98.82 | -1.18 | 53 | 49.1 | -11.36 | -3.87 | -13.59 | 225 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.67 | -1.33 | 0 | — | 23.10 | 3.45 | -6.29 | 1 |
| 28 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 29 | Williams %R · 1h | reversion | 98.37 | -1.63 | 69 | 55.1 | -16.20 | -2.96 | -19.41 | 495 |
| 30 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 31 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.97 | -0.47 | -4.23 | 104 |
| 32 | Max aggression: 1-day momentum | meta | 98.16 | -1.84 | 5 | 40.0 | -21.68 | -1.03 | -41.28 | 43 |
| 33 | Agent (rotation) | meta | 97.83 | -2.17 | 48 | 18.8 | -3.64 | -1.37 | -8.90 | 227 |
| 34 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 35 | Agent (ML meta-label) | meta | 97.48 | -2.52 | 202 | 17.8 | 3.06 | 0.69 | -11.25 | 384 |
| 36 | Daily: SMA 20/50 cross · AAPL | daily | 97.31 | -2.69 | 0 | — | -0.14 | 0.04 | -5.18 | 1 |
| 37 | Daily: Momentum burst | daily | 96.95 | -3.05 | 3 | 0.0 | -1.08 | 0.01 | -16.46 | 46 |
| 38 | Parabolic SAR · 1h | trend | 96.94 | -3.06 | 45 | 15.6 | -7.27 | -0.86 | -19.70 | 312 |
| 39 | Supertrend · 1h | trend | 96.76 | -3.24 | 23 | 4.3 | 3.48 | 0.65 | -16.43 | 202 |
| 40 | MFI reversion · 1h | reversion | 96.64 | -3.36 | 68 | 29.4 | -6.00 | -0.97 | -16.99 | 121 |
| 41 | ADX DI cross · 1h | trend | 96.63 | -3.37 | 41 | 12.2 | -4.26 | -0.55 | -13.84 | 269 |
| 42 | Gap and go | momentum | 96.29 | -3.71 | 33 | 6.1 | 11.96 | 2.91 | -4.73 | 199 |
| 43 | MACD cross · 1h | trend | 96.03 | -3.98 | 68 | 13.2 | -14.95 | -2.37 | -17.97 | 485 |
| 44 | Squeeze breakout · 1h | breakout | 95.83 | -4.17 | 22 | 18.2 | 20.94 | 2.99 | -8.06 | 113 |
| 45 | Ichimoku · 1h | trend | 95.24 | -4.76 | 27 | 11.1 | 7.16 | 1.00 | -16.19 | 128 |
| 46 | Opening range 30m | breakout | 95.12 | -4.88 | 68 | 17.6 | -13.94 | -4.15 | -16.19 | 565 |
| 47 | Copy: Insider buying | copy | 95.04 | -4.96 | 4 | 50.0 | -19.47 | -3.83 | -20.96 | 71 |
| 48 | RSI momentum · 1h | momentum | 94.89 | -5.12 | 36 | 2.8 | 2.53 | 0.53 | -16.65 | 227 |
| 49 | Triple EMA stack · 1h | trend | 94.08 | -5.92 | 46 | 6.5 | -7.09 | -0.65 | -23.88 | 241 |
| 50 | VWAP momentum · 1h | momentum | 93.85 | -6.15 | 169 | 23.1 | -40.44 | -6.33 | -42.55 | 1275 |
| 51 | Opening range 15m | breakout | 93.75 | -6.25 | 82 | 17.1 | -15.49 | -4.43 | -18.19 | 692 |
| 52 | Bollinger breakout · 1h | breakout | 93.48 | -6.52 | 35 | 17.1 | 5.87 | 0.94 | -12.06 | 293 |
| 53 | Max aggression: 5-day momentum | meta | 93.22 | -6.78 | 5 | 40.0 | -19.64 | -1.68 | -29.56 | 30 |
| 54 | Volume breakout · 1h | breakout | 92.89 | -7.11 | 30 | 6.7 | 3.36 | 0.65 | -12.60 | 129 |
| 55 | Three white soldiers | momentum | 92.82 | -7.18 | 64 | 17.2 | -49.52 | -26.65 | -49.52 | 598 |
| 56 | EMA 9/21 cross · 1h | trend | 92.56 | -7.44 | 63 | 11.1 | -4.37 | -0.40 | -18.47 | 343 |
| 57 | Heikin-Ashi · 1h | trend | 91.90 | -8.10 | 75 | 20.0 | -32.18 | -5.64 | -33.58 | 687 |
| 58 | MACD zero-line · 1h | trend | 91.34 | -8.66 | 35 | 5.7 | -4.77 | -0.41 | -18.32 | 237 |
| 59 | Donchian 20/10 · 1h | breakout | 91.04 | -8.96 | 29 | 13.8 | -0.55 | 0.15 | -16.18 | 222 |
| 60 | OBV trend · 1h | momentum | 90.21 | -9.79 | 91 | 11.0 | -14.04 | -1.58 | -26.61 | 337 |
| 61 | RSI(14) reversion | reversion | 89.18 | -10.82 | 164 | 36.6 | -72.09 | -20.86 | -72.20 | 1458 |
| 62 | Keltner breakout · 1h | breakout | 88.67 | -11.33 | 21 | 0.0 | -11.13 | -1.32 | -23.03 | 214 |
| 63 | ROC + volume · 1h | momentum | 87.67 | -12.33 | 80 | 13.8 | -13.35 | -1.73 | -24.25 | 423 |
| 64 | Squeeze breakout | breakout | 83.18 | -16.82 | 169 | 16.0 | -60.24 | -18.25 | -60.82 | 1204 |
| 65 | Donchian 55/20 | breakout | 82.46 | -17.55 | 168 | 18.5 | -68.09 | -15.27 | -68.36 | 1309 |
| 66 | VWAP reversion | reversion | 81.13 | -18.87 | 182 | 28.0 | -70.97 | -17.21 | -71.02 | 1387 |
| 67 | EMA 20/50 cross | trend | 80.25 | -19.75 | 189 | 19.0 | -78.81 | -16.69 | -79.22 | 1483 |
| 68 | Volume breakout | breakout | 80.20 | -19.80 | 155 | 14.2 | -63.91 | -19.97 | -63.98 | 928 |
| 69 | ROC + volume | momentum | 79.98 | -20.02 | 256 | 20.3 | -73.49 | -17.84 | -73.76 | 1674 |
| 70 | AI bee: Bizzy | ai | 79.37 | -20.63 | 369 | 11.1 | — | — | — | — |
| 71 | Z-score reversion | reversion | 79.06 | -20.94 | 260 | 31.9 | -85.56 | -26.60 | -85.59 | 2106 |
| 72 | AI bee: Boozy | ai | 78.84 | -21.16 | 131 | 3.8 | — | — | — | — |
| 73 | MFI reversion | reversion | 77.12 | -22.88 | 243 | 21.8 | -88.26 | -33.53 | -88.28 | 2140 |
| 74 | Ichimoku | trend | 76.27 | -23.73 | 199 | 9.5 | -81.40 | -25.51 | -81.54 | 1762 |
| 75 | Keltner breakout | breakout | 76.22 | -23.78 | 243 | 13.6 | -85.32 | -32.35 | -85.34 | 1905 |
| 76 | Supertrend | trend | 75.20 | -24.80 | 263 | 20.5 | -87.29 | -23.45 | -87.45 | 1952 |
| 77 | Donchian 20/10 | breakout | 72.89 | -27.11 | 331 | 19.0 | -90.73 | -27.79 | -90.79 | 2677 |
| 78 | MACD zero-line | trend | 72.07 | -27.93 | 320 | 16.9 | -91.69 | -32.43 | -91.69 | 2361 |
| 79 | ADX DI cross | trend | 72.05 | -27.95 | 293 | 9.2 | -89.73 | -41.62 | -89.73 | 2122 |
| 80 | Trend pullback | trend | 71.70 | -28.30 | 291 | 17.9 | -91.57 | -33.37 | -91.58 | 2331 |
| 81 | Triple EMA stack | trend | 71.62 | -28.38 | 331 | 17.5 | -93.13 | -33.61 | -93.18 | 2617 |
| 82 | RSI momentum | momentum | 70.84 | -29.16 | 314 | 15.9 | -90.53 | -27.64 | -90.62 | 2397 |
| 83 | Bollinger breakout | breakout | 70.16 | -29.84 | 337 | 16.3 | -93.94 | -38.33 | -93.94 | 2852 |
| 84 | Stochastic reversion | reversion | 68.73 | -31.27 | 471 | 24.4 | -95.85 | -42.32 | -95.86 | 4054 |
| 85 | Consensus | meta | 67.61 | -32.39 | 308 | 9.4 | -94.61 | -29.04 | -94.62 | 2651 |
| 86 | Bollinger reversion | reversion | 67.25 | -32.74 | 458 | 17.7 | -95.93 | -41.31 | -95.94 | 3710 |
| 87 | Connors RSI(2) ⏸ | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.68 | -39.42 | -96.69 | 3647 |
| 88 | EMA 9/21 cross | trend | 66.09 | -33.91 | 433 | 18.5 | -97.37 | -37.24 | -97.41 | 3543 |
| 89 | Candlestick reversal | reversion | 65.10 | -34.90 | 502 | 16.9 | -99.34 | -44.21 | -99.34 | 5616 |
| 90 | OBV trend | momentum | 64.75 | -35.25 | 468 | 16.2 | -96.10 | -42.96 | -96.12 | 3581 |
| 91 | CCI reversion | reversion | 64.47 | -35.53 | 418 | 17.2 | -98.51 | -44.83 | -98.51 | 4709 |
| 92 | VWAP momentum | momentum | 62.87 | -37.13 | 515 | 9.3 | -98.62 | -33.64 | -98.62 | 5320 |
| 93 | Parabolic SAR | trend | 61.87 | -38.13 | 446 | 14.3 | -97.16 | -48.46 | -97.17 | 3658 |
| 94 | MACD cross | trend | 60.17 | -39.83 | 521 | 15.2 | -99.71 | -52.35 | -99.71 | 6116 |
| 95 | Williams %R ⏸ | reversion | 59.36 | -40.64 | 582 | 23.0 | -99.53 | -50.91 | -99.53 | 6124 |
| 96 | Heikin-Ashi ⏸ | trend | 58.33 | -41.67 | 502 | 10.0 | -99.90 | -63.18 | -99.90 | 8312 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-02T16:06 | Agent (ML meta-label) | buy | SPY | 1.25 | — | following Stochastic reversion · 1h |
| 2026-10-02T16:06 | Agent (ML meta-label) | buy | SOL-USD | 3.90 | — | entry |
| 2026-10-02T16:06 | Agent (ML meta-label) | sell | COIN | 4.70 | -0.10 | selected signal exited |
| 2026-10-02T16:06 | Consensus | buy | TECL | 16.88 | — | entry |
| 2026-10-02T16:06 | MFI reversion | buy | UPRO | 2.28 | — | rebalance up |
| 2026-10-02T16:06 | MFI reversion | buy | AMZN | 11.02 | — | entry signal |
| 2026-10-02T16:06 | MFI reversion | sell | QQQ | 4.43 | -0.00 | rebalance down |
| 2026-10-02T16:06 | MFI reversion | sell | MSFT | 4.43 | -0.00 | rebalance down |
| 2026-10-02T16:06 | MFI reversion | sell | AAPL | 4.44 | -0.00 | rebalance down |
| 2026-10-02T16:06 | Bollinger reversion | sell | TECL | 3.98 | 0.04 | exit signal |
| 2026-10-02T16:06 | Bollinger reversion | sell | NVDA | 3.97 | 0.01 | exit signal |
| 2026-10-02T16:06 | Bollinger breakout | sell | SQQQ | 17.50 | -0.05 | stop-loss |
| 2026-10-02T16:06 | Donchian 20/10 | sell | SQQQ | 18.04 | -0.22 | stop-loss |
| 2026-10-02T16:06 | OBV trend | buy | NVDA | 16.04 | — | entry signal |
| 2026-10-02T16:06 | RSI momentum | sell | SQQQ | 17.57 | -0.21 | stop-loss |
| 2026-10-02T16:06 | Parabolic SAR | buy | UPRO | 6.17 | — | entry signal |
| 2026-10-02T16:06 | Parabolic SAR | buy | TECL | 6.19 | — | entry signal |
| 2026-10-02T16:06 | Parabolic SAR | buy | NVDA | 6.19 | — | entry signal |
| 2026-10-02T16:06 | Parabolic SAR | buy | GOOGL | 6.19 | — | entry signal |
| 2026-10-02T16:06 | Parabolic SAR | buy | AAPL | 6.19 | — | entry |
| 2026-10-02T16:06 | Parabolic SAR | sell | TSLA | 6.17 | -0.01 | rebalance down |
| 2026-10-02T16:06 | Parabolic SAR | sell | TQQQ | 6.21 | 0.01 | rebalance down |
| 2026-10-02T16:06 | Parabolic SAR | sell | SPY | 6.19 | -0.00 | rebalance down |
| 2026-10-02T16:06 | Parabolic SAR | sell | SOXL | 6.18 | -0.00 | rebalance down |
| 2026-10-02T16:06 | Parabolic SAR | sell | QQQ | 6.19 | -0.00 | rebalance down |
| 2026-10-02T16:06 | MACD cross | buy | XRP-USD | 8.57 | — | entry signal |
| 2026-10-02T16:06 | MACD cross | buy | ETH-USD | 8.61 | — | entry signal |
| 2026-10-02T16:06 | MACD cross | buy | BTC-USD | 8.61 | — | entry signal |
| 2026-10-02T16:06 | MACD cross | sell | SQQQ | 6.63 | 0.07 | rebalance down |
| 2026-10-02T16:06 | MACD cross | sell | SOL-USD | 6.26 | -0.02 | rebalance down |
| 2026-10-02T16:06 | MACD cross | sell | LABU | 6.45 | -0.02 | rebalance down |
| 2026-10-02T16:06 | MACD cross | sell | DOGE-USD | 6.45 | -0.03 | rebalance down |
| 2026-10-02T16:06 | Triple EMA stack | buy | TECL | 17.91 | — | entry signal |
| 2026-10-02T16:06 | EMA 9/21 cross | buy | TECL | 16.53 | — | entry signal |
| 2026-10-02T16:06 | EMA 9/21 cross | sell | SQQQ | 16.38 | -0.20 | stop-loss |
| 2026-10-02T16:04 | AI bee: Bizzy | buy | TECL | 11.50 | — | Jev: buy (buy p=0.58) |
| 2026-10-02T16:00 | Connors RSI(2) · 1h | buy | SOL-USD | 24.70 | — | entry signal |
| 2026-10-02T16:00 | Connors RSI(2) · 1h | buy | BTC-USD | 24.70 | — | entry signal |
| 2026-10-02T16:00 | Donchian 20/10 · 1h | sell | BTC-USD | 5.06 | -0.03 | exit signal |
| 2026-10-02T16:00 | OBV trend · 1h | sell | XRP-USD | 6.92 | -0.12 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
