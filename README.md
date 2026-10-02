# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-02T17:06:05.000169+00:00 · 9090 ticks

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

Today: 24603 decisions in 2418 calls, $0.3100 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-02T17:06 | 1 / 20 / 9 | TNA 14% |  |
| Breezy | 2026-10-02T17:06 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-02T17:06 | 2 / 26 / 2 | MSTR 70% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.48 | 2.48 | 0 | — | -6.85 | -1.23 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.46 | 2.46 | 0 | — | 3.14 | 0.93 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 101.89 | 1.89 | 0 | — | 35.48 | 4.31 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.01 | 1.01 | 0 | — | -1.87 | -1.04 | -5.09 | 2 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.85 | 0.85 | 0 | — | 4.03 | 1.84 | -3.62 | 1 |
| 6 | Candlestick reversal · 1h | reversion | 100.52 | 0.52 | 53 | 37.7 | -23.58 | -5.41 | -26.35 | 493 |
| 7 | Daily: Bullish score | daily | 100.51 | 0.51 | 3 | 0.0 | 2.70 | 0.57 | -12.76 | 14 |
| 8 | RSI(14) reversion · 1h | reversion | 100.21 | 0.21 | 10 | 60.0 | 3.18 | 0.95 | -6.57 | 124 |
| 9 | Hold SPY | benchmark | 100.19 | 0.19 | 0 | — | 1.93 | 1.14 | -3.66 | 1 |
| 10 | Donchian 55/20 · 1h | breakout | 100.09 | 0.09 | 17 | 0.0 | 7.06 | 1.09 | -16.96 | 115 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.98 | -0.02 | 15 | 33.3 | 4.01 | 1.99 | -1.46 | 86 |
| 14 | Z-score reversion · 1h | reversion | 99.91 | -0.09 | 17 | 58.8 | 5.62 | 1.29 | -8.60 | 156 |
| 15 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 24 | 33.3 | -10.73 | -3.62 | -14.05 | 112 |
| 16 | Bollinger reversion · 1h | reversion | 99.82 | -0.18 | 38 | 44.7 | -15.03 | -4.02 | -17.66 | 303 |
| 17 | Stochastic reversion · 1h | reversion | 99.69 | -0.31 | 40 | 60.0 | -7.79 | -1.61 | -9.82 | 328 |
| 18 | Copy: Warren Buffett (BRK-B) | copy | 99.55 | -0.45 | 0 | — | -2.44 | -0.95 | -7.65 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 20 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.45 | -5.95 | -11.27 | 222 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 99.17 | -0.83 | 0 | — | -2.59 | -1.22 | -5.14 | 1 |
| 23 | Trend pullback · 1h | trend | 99.03 | -0.97 | 44 | 20.5 | -23.54 | -6.01 | -25.99 | 164 |
| 24 | CCI reversion · 1h | reversion | 98.87 | -1.13 | 63 | 49.2 | 2.25 | 0.53 | -12.41 | 412 |
| 25 | EMA 20/50 cross · 1h | trend | 98.81 | -1.19 | 23 | 8.7 | 14.68 | 1.81 | -14.40 | 130 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 98.69 | -1.31 | 0 | — | 22.93 | 3.43 | -6.29 | 1 |
| 27 | Connors RSI(2) · 1h | reversion | 98.68 | -1.32 | 53 | 49.1 | -11.65 | -3.96 | -13.59 | 222 |
| 28 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 29 | Williams %R · 1h | reversion | 98.35 | -1.65 | 69 | 55.1 | -16.29 | -2.98 | -19.41 | 495 |
| 30 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 31 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.97 | -0.47 | -4.23 | 104 |
| 32 | Agent (rotation) | meta | 97.92 | -2.08 | 48 | 18.8 | -3.57 | -1.34 | -8.90 | 227 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.83 | -2.17 | 0 | — | 0.24 | 0.18 | -5.18 | 1 |
| 34 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 35 | Agent (ML meta-label) | meta | 97.40 | -2.60 | 202 | 17.8 | 7.90 | 1.46 | -10.90 | 359 |
| 36 | Max aggression: 1-day momentum | meta | 97.37 | -2.63 | 5 | 40.0 | -22.43 | -1.09 | -41.28 | 43 |
| 37 | Daily: Momentum burst | daily | 96.88 | -3.12 | 3 | 0.0 | -1.19 | -0.00 | -16.52 | 46 |
| 38 | Parabolic SAR · 1h | trend | 96.84 | -3.16 | 45 | 15.6 | -7.55 | -0.91 | -19.70 | 312 |
| 39 | Supertrend · 1h | trend | 96.66 | -3.34 | 25 | 8.0 | 3.22 | 0.62 | -16.43 | 202 |
| 40 | MFI reversion · 1h | reversion | 96.64 | -3.36 | 68 | 29.4 | -6.00 | -0.97 | -16.99 | 121 |
| 41 | ADX DI cross · 1h | trend | 96.54 | -3.46 | 41 | 12.2 | -4.71 | -0.63 | -13.84 | 270 |
| 42 | Gap and go | momentum | 96.31 | -3.69 | 33 | 6.1 | 11.95 | 2.90 | -4.73 | 199 |
| 43 | MACD cross · 1h | trend | 95.96 | -4.04 | 68 | 13.2 | -14.97 | -2.39 | -17.79 | 484 |
| 44 | Squeeze breakout · 1h | breakout | 95.57 | -4.43 | 22 | 18.2 | 20.43 | 2.94 | -8.06 | 113 |
| 45 | Opening range 30m | breakout | 95.23 | -4.77 | 68 | 17.6 | -13.91 | -4.14 | -16.25 | 566 |
| 46 | Copy: Insider buying | copy | 95.02 | -4.98 | 4 | 50.0 | -19.69 | -3.86 | -21.24 | 71 |
| 47 | Ichimoku · 1h | trend | 94.87 | -5.13 | 28 | 10.7 | 6.55 | 0.94 | -16.19 | 128 |
| 48 | RSI momentum · 1h | momentum | 94.63 | -5.37 | 37 | 2.7 | 2.25 | 0.49 | -16.65 | 227 |
| 49 | VWAP momentum · 1h | momentum | 93.87 | -6.13 | 169 | 23.1 | -40.34 | -6.30 | -42.55 | 1275 |
| 50 | Triple EMA stack · 1h | trend | 93.76 | -6.24 | 47 | 6.4 | -7.68 | -0.73 | -23.88 | 242 |
| 51 | Opening range 15m | breakout | 93.59 | -6.41 | 83 | 16.9 | -15.74 | -4.48 | -18.57 | 693 |
| 52 | Bollinger breakout · 1h | breakout | 93.41 | -6.59 | 36 | 16.7 | 5.59 | 0.91 | -12.06 | 293 |
| 53 | Volume breakout · 1h | breakout | 92.84 | -7.16 | 30 | 6.7 | 3.14 | 0.62 | -12.60 | 129 |
| 54 | Three white soldiers | momentum | 92.82 | -7.18 | 64 | 17.2 | -49.52 | -26.65 | -49.52 | 598 |
| 55 | Max aggression: 5-day momentum | meta | 92.47 | -7.53 | 5 | 40.0 | -20.41 | -1.79 | -29.56 | 30 |
| 56 | EMA 9/21 cross · 1h | trend | 92.35 | -7.65 | 64 | 10.9 | -4.65 | -0.44 | -18.47 | 343 |
| 57 | Heikin-Ashi · 1h | trend | 91.85 | -8.15 | 77 | 22.1 | -32.32 | -5.68 | -33.58 | 687 |
| 58 | MACD zero-line · 1h | trend | 91.23 | -8.77 | 35 | 5.7 | -5.08 | -0.46 | -18.32 | 238 |
| 59 | Donchian 20/10 · 1h | breakout | 90.97 | -9.03 | 30 | 13.3 | -0.89 | 0.11 | -16.18 | 222 |
| 60 | OBV trend · 1h | momentum | 90.06 | -9.94 | 93 | 10.8 | -14.50 | -1.64 | -26.61 | 337 |
| 61 | RSI(14) reversion | reversion | 88.97 | -11.03 | 166 | 36.1 | -72.10 | -20.87 | -72.11 | 1457 |
| 62 | Keltner breakout · 1h | breakout | 88.62 | -11.38 | 21 | 0.0 | -11.00 | -1.30 | -23.03 | 213 |
| 63 | ROC + volume · 1h | momentum | 87.57 | -12.43 | 80 | 13.8 | -12.13 | -1.54 | -23.53 | 424 |
| 64 | Squeeze breakout | breakout | 83.18 | -16.82 | 169 | 16.0 | -60.24 | -18.25 | -60.82 | 1204 |
| 65 | Donchian 55/20 | breakout | 82.48 | -17.52 | 168 | 18.5 | -68.09 | -15.27 | -68.36 | 1309 |
| 66 | VWAP reversion | reversion | 80.75 | -19.25 | 184 | 27.7 | -71.03 | -17.23 | -71.03 | 1385 |
| 67 | EMA 20/50 cross | trend | 80.20 | -19.80 | 190 | 18.9 | -78.84 | -16.71 | -79.22 | 1484 |
| 68 | Volume breakout | breakout | 80.20 | -19.80 | 155 | 14.2 | -64.01 | -20.02 | -64.08 | 928 |
| 69 | ROC + volume | momentum | 79.82 | -20.18 | 257 | 20.2 | -73.67 | -17.88 | -73.94 | 1670 |
| 70 | AI bee: Bizzy | ai | 79.28 | -20.71 | 373 | 11.0 | — | — | — | — |
| 71 | Z-score reversion | reversion | 78.87 | -21.13 | 261 | 32.2 | -85.63 | -26.70 | -85.63 | 2106 |
| 72 | AI bee: Boozy | ai | 78.79 | -21.21 | 131 | 3.8 | — | — | — | — |
| 73 | MFI reversion | reversion | 77.17 | -22.83 | 248 | 22.2 | -88.23 | -33.46 | -88.23 | 2129 |
| 74 | Keltner breakout | breakout | 76.22 | -23.78 | 243 | 13.6 | -85.32 | -32.35 | -85.34 | 1905 |
| 75 | Ichimoku | trend | 76.05 | -23.95 | 203 | 10.3 | -81.47 | -25.48 | -81.59 | 1767 |
| 76 | Supertrend | trend | 75.25 | -24.75 | 263 | 20.5 | -87.28 | -23.44 | -87.46 | 1954 |
| 77 | Donchian 20/10 | breakout | 72.82 | -27.18 | 332 | 19.3 | -90.75 | -27.81 | -90.81 | 2678 |
| 78 | ADX DI cross | trend | 72.10 | -27.90 | 294 | 9.2 | -89.72 | -41.51 | -89.74 | 2121 |
| 79 | MACD zero-line | trend | 72.00 | -28.00 | 320 | 16.9 | -91.70 | -32.45 | -91.70 | 2363 |
| 80 | Trend pullback | trend | 71.57 | -28.43 | 293 | 17.7 | -91.58 | -33.32 | -91.59 | 2334 |
| 81 | Triple EMA stack | trend | 71.35 | -28.65 | 338 | 17.2 | -93.16 | -33.70 | -93.21 | 2628 |
| 82 | RSI momentum | momentum | 70.49 | -29.51 | 317 | 15.8 | -90.60 | -27.75 | -90.68 | 2400 |
| 83 | Bollinger breakout | breakout | 70.16 | -29.84 | 337 | 16.3 | -93.94 | -38.33 | -93.94 | 2852 |
| 84 | Stochastic reversion | reversion | 68.65 | -31.35 | 484 | 25.4 | -95.83 | -41.85 | -95.83 | 4055 |
| 85 | Consensus | meta | 67.44 | -32.56 | 314 | 9.6 | -94.82 | -28.92 | -94.82 | 2675 |
| 86 | Bollinger reversion | reversion | 67.10 | -32.90 | 470 | 18.5 | -95.86 | -40.27 | -95.86 | 3703 |
| 87 | Connors RSI(2) ⏸ | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.65 | -39.29 | -96.66 | 3650 |
| 88 | EMA 9/21 cross | trend | 65.83 | -34.17 | 440 | 18.2 | -97.39 | -37.37 | -97.42 | 3555 |
| 89 | Candlestick reversal | reversion | 64.90 | -35.09 | 516 | 17.4 | -99.34 | -43.71 | -99.34 | 5623 |
| 90 | OBV trend | momentum | 64.53 | -35.47 | 475 | 16.2 | -96.10 | -43.02 | -96.12 | 3582 |
| 91 | CCI reversion | reversion | 64.37 | -35.63 | 424 | 17.7 | -98.49 | -44.24 | -98.49 | 4706 |
| 92 | VWAP momentum | momentum | 62.85 | -37.15 | 518 | 9.5 | -98.63 | -33.81 | -98.63 | 5322 |
| 93 | Parabolic SAR | trend | 61.84 | -38.16 | 452 | 14.4 | -97.17 | -48.51 | -97.17 | 3662 |
| 94 | MACD cross | trend | 59.98 | -40.02 | 524 | 15.1 | -99.71 | -52.46 | -99.71 | 6128 |
| 95 | Williams %R ⏸ | reversion | 59.36 | -40.64 | 582 | 23.0 | -99.53 | -50.26 | -99.53 | 6129 |
| 96 | Heikin-Ashi ⏸ | trend | 58.33 | -41.67 | 502 | 10.0 | -99.90 | -63.27 | -99.90 | 8330 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-02T17:05 | MFI reversion | buy | XRP-USD | 6.48 | — | rebalance up |
| 2026-10-02T17:05 | MFI reversion | buy | UPRO | 6.42 | — | rebalance up |
| 2026-10-02T17:05 | MFI reversion | sell | PLTR | 15.42 | -0.00 | exit signal |
| 2026-10-02T17:05 | CCI reversion | buy | QQQ | 1.28 | — | entry |
| 2026-10-02T17:05 | CCI reversion | buy | PLTR | 2.93 | — | entry |
| 2026-10-02T17:05 | CCI reversion | buy | NVDA | 2.93 | — | entry |
| 2026-10-02T17:05 | CCI reversion | sell | UPRO | 3.54 | 0.01 | exit signal |
| 2026-10-02T17:05 | CCI reversion | sell | SPY | 3.59 | 0.00 | exit signal |
| 2026-10-02T17:05 | Stochastic reversion | sell | META | 3.44 | -0.00 | exit signal |
| 2026-10-02T17:05 | Candlestick reversal | buy | SOL-USD | 1.58 | — | entry |
| 2026-10-02T17:05 | Candlestick reversal | buy | ETHU | 4.64 | — | entry |
| 2026-10-02T17:05 | Candlestick reversal | buy | ETH-USD | 4.64 | — | entry |
| 2026-10-02T17:05 | Candlestick reversal | sell | SOXL | 5.00 | -0.00 | target is flat |
| 2026-10-02T17:05 | Candlestick reversal | sell | LABU | 5.86 | -0.05 | exit signal |
| 2026-10-02T17:05 | OBV trend | buy | TQQQ | 10.75 | — | entry signal |
| 2026-10-02T17:05 | OBV trend | buy | IWM | 10.76 | — | entry signal |
| 2026-10-02T17:05 | OBV trend | sell | TSLA | 5.38 | 0.02 | rebalance down |
| 2026-10-02T17:05 | OBV trend | sell | TECL | 5.39 | 0.00 | rebalance down |
| 2026-10-02T17:05 | OBV trend | sell | GOOGL | 5.37 | 0.00 | rebalance down |
| 2026-10-02T17:05 | OBV trend | sell | AAPL | 5.37 | 0.00 | rebalance down |
| 2026-10-02T17:05 | RSI momentum | buy | SOXL | 17.62 | — | entry |
| 2026-10-02T17:05 | Ichimoku | sell | SOXL | 19.01 | 0.01 | exit signal |
| 2026-10-02T17:05 | Parabolic SAR | buy | META | 1.44 | — | entry signal |
| 2026-10-02T17:05 | Supertrend | buy | GOOGL | 18.82 | — | entry signal |
| 2026-10-02T17:05 | Supertrend | buy | AAPL | 18.82 | — | entry signal |
| 2026-10-02T17:05 | MACD zero-line | buy | AMZN | 18.00 | — | entry signal |
| 2026-10-02T17:05 | MACD cross | buy | BITX | 3.00 | — | entry |
| 2026-10-02T17:05 | MACD cross | sell | AAPL | 3.69 | 0.00 | rebalance down |
| 2026-10-02T17:05 | Triple EMA stack | buy | UPRO | 10.61 | — | entry signal |
| 2026-10-02T17:05 | Triple EMA stack | buy | SPY | 14.27 | — | entry signal |
| 2026-10-02T17:05 | EMA 9/21 cross | buy | UPRO | 6.46 | — | entry signal |
| 2026-10-02T17:05 | EMA 9/21 cross | buy | SPY | 10.97 | — | entry signal |
| 2026-10-02T17:05 | EMA 9/21 cross | sell | SQQQ | 5.44 | -0.02 | rebalance down |
| 2026-10-02T17:05 | EMA 9/21 cross | sell | AMZN | 5.49 | -0.00 | rebalance down |
| 2026-10-02T17:03 | AI bee: Bizzy | buy | TNA | 10.93 | — | Jev: buy (buy p=0.55) |
| 2026-10-02T17:01 | AI bee: Bizzy | sell | XRP-USD | 11.51 | -0.08 | Jev: sell (sell p=0.57) after 13 min |
| 2026-10-02T17:00 | RSI momentum · 1h | buy | SPY | 2.81 | — | entry |
| 2026-10-02T17:00 | RSI momentum · 1h | buy | PLTR | 4.98 | — | entry |
| 2026-10-02T17:00 | RSI momentum · 1h | sell | XRP-USD | 7.79 | -0.26 | exit signal |
| 2026-10-02T17:00 | Supertrend · 1h | buy | UPRO | 4.10 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
