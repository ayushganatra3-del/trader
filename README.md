# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T00:05:05.000136+00:00 · 9422 ticks

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

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 75 decisions in 15 calls, $0.0011 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T00:05 | 0 / 1 / 4 | AMZN 16%, COIN 16%, MSTR 15% |  |
| Breezy | 2026-10-03T00:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T00:05 | 0 / 4 / 1 | MSTR 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion · 1h | UPRO | 2.43 | +6.89% | 3 |
| Stochastic reversion · 1h | SPY | 2.28 | +2.53% | 3 |
| Connors RSI(2) · 1h | COIN | 2.23 | +6.43% | 5 |
| Stochastic reversion | MSFT | 2.20 | +2.95% | 13 |
| RSI(14) reversion | SQQQ | 2.18 | +4.27% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.27 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 3 | VWAP reversion · 1h | reversion | 100.99 | 0.99 | 24 | 33.3 | -9.73 | -3.17 | -14.05 | 116 |
| 4 | Hold BTC | benchmark | 100.96 | 0.96 | 0 | — | 33.97 | 4.16 | -8.68 | 1 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.55 | -5.38 | -26.13 | 492 |
| 8 | RSI(14) reversion · 1h | reversion | 100.54 | 0.54 | 10 | 60.0 | 4.85 | 1.40 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.97 | -0.03 | 38 | 44.7 | -14.87 | -3.96 | -17.68 | 307 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.91 | 1.94 | -1.46 | 86 |
| 14 | Z-score reversion · 1h | reversion | 99.70 | -0.30 | 18 | 55.6 | 5.51 | 1.27 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.70 | 1.05 | -16.96 | 115 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 98.95 | -1.05 | 40 | 60.0 | -8.80 | -1.83 | -9.86 | 334 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.59 | 0.42 | -12.41 | 419 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 45 | 20.0 | -22.64 | -5.84 | -25.34 | 160 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.85 | -2.15 | 50 | 20.0 | -3.28 | -1.22 | -8.90 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.79 | 1.72 | -14.40 | 131 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -12.45 | -4.20 | -14.21 | 226 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.72 | -3.06 | -19.41 | 499 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | -1.15 | -0.06 | -12.60 | 386 |
| 37 | MFI reversion · 1h | reversion | 96.62 | -3.38 | 69 | 29.0 | -6.94 | -1.14 | -16.99 | 121 |
| 38 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -7.86 | -0.96 | -19.70 | 312 |
| 39 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.60 | 2.81 | -4.73 | 199 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 2.56 | 0.53 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.60 | -3.69 | -21.08 | 71 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -5.88 | -0.83 | -13.84 | 271 |
| 44 | MACD cross · 1h | trend | 95.50 | -4.50 | 71 | 15.5 | -15.34 | -2.46 | -17.78 | 485 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.31 | 0.92 | -16.19 | 127 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 2.10 | 0.48 | -16.65 | 227 |
| 49 | VWAP momentum · 1h | momentum | 93.60 | -6.40 | 170 | 22.9 | -40.74 | -6.40 | -42.55 | 1279 |
| 50 | Bollinger breakout · 1h | breakout | 93.18 | -6.82 | 36 | 16.7 | 5.39 | 0.89 | -12.06 | 293 |
| 51 | Triple EMA stack · 1h | trend | 93.11 | -6.89 | 50 | 8.0 | -7.93 | -0.77 | -23.88 | 243 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Three white soldiers | momentum | 92.69 | -7.31 | 65 | 16.9 | -49.30 | -26.19 | -49.37 | 593 |
| 54 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 2.74 | 0.57 | -12.60 | 128 |
| 55 | EMA 9/21 cross · 1h | trend | 91.74 | -8.26 | 68 | 11.8 | -4.93 | -0.48 | -18.47 | 342 |
| 56 | Heikin-Ashi · 1h | trend | 91.29 | -8.71 | 86 | 25.6 | -32.78 | -5.81 | -33.56 | 687 |
| 57 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 58 | MACD zero-line · 1h | trend | 90.81 | -9.19 | 38 | 13.2 | -5.20 | -0.47 | -18.32 | 238 |
| 59 | Donchian 20/10 · 1h | breakout | 90.65 | -9.35 | 31 | 12.9 | -0.78 | 0.12 | -16.18 | 221 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -14.33 | -1.62 | -26.66 | 340 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.92 | -1.43 | -23.19 | 215 |
| 62 | RSI(14) reversion | reversion | 87.33 | -12.67 | 179 | 34.6 | -72.46 | -21.01 | -72.51 | 1461 |
| 63 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -12.74 | -1.64 | -23.45 | 424 |
| 64 | Squeeze breakout | breakout | 83.17 | -16.83 | 170 | 15.9 | -60.23 | -18.24 | -60.92 | 1205 |
| 65 | Donchian 55/20 | breakout | 82.34 | -17.66 | 169 | 18.9 | -68.43 | -15.42 | -68.46 | 1308 |
| 66 | Volume breakout | breakout | 80.12 | -19.88 | 155 | 14.2 | -64.26 | -19.96 | -64.29 | 912 |
| 67 | VWAP reversion | reversion | 80.10 | -19.91 | 203 | 28.6 | -71.06 | -17.13 | -71.34 | 1387 |
| 68 | EMA 20/50 cross | trend | 80.02 | -19.98 | 191 | 18.8 | -78.92 | -16.78 | -79.07 | 1482 |
| 69 | ROC + volume | momentum | 79.74 | -20.26 | 257 | 20.2 | -73.74 | -17.94 | -73.88 | 1673 |
| 70 | AI bee: Bizzy | ai | 78.37 | -21.63 | 397 | 10.3 | — | — | — | — |
| 71 | Z-score reversion | reversion | 77.69 | -22.31 | 274 | 31.0 | -85.84 | -26.93 | -85.86 | 2113 |
| 72 | AI bee: Boozy | ai | 76.79 | -23.21 | 144 | 5.6 | — | — | — | — |
| 73 | MFI reversion | reversion | 76.18 | -23.82 | 267 | 22.5 | -88.29 | -33.44 | -88.33 | 2138 |
| 74 | Keltner breakout | breakout | 76.15 | -23.86 | 243 | 13.6 | -85.35 | -32.19 | -85.36 | 1902 |
| 75 | Ichimoku | trend | 75.76 | -24.24 | 209 | 10.0 | -81.55 | -25.45 | -81.55 | 1763 |
| 76 | Supertrend | trend | 75.19 | -24.81 | 266 | 20.7 | -87.36 | -23.52 | -87.39 | 1950 |
| 77 | Donchian 20/10 | breakout | 72.43 | -27.57 | 339 | 19.5 | -90.86 | -28.02 | -90.89 | 2684 |
| 78 | MACD zero-line | trend | 71.70 | -28.30 | 331 | 16.9 | -91.71 | -32.41 | -91.72 | 2369 |
| 79 | ADX DI cross | trend | 71.34 | -28.66 | 305 | 10.2 | -89.81 | -41.33 | -89.81 | 2122 |
| 80 | Trend pullback | trend | 70.85 | -29.15 | 318 | 17.0 | -91.58 | -32.81 | -91.59 | 2353 |
| 81 | Triple EMA stack | trend | 70.58 | -29.42 | 353 | 16.7 | -93.29 | -34.10 | -93.29 | 2638 |
| 82 | RSI momentum | momentum | 69.92 | -30.07 | 324 | 15.7 | -90.75 | -27.94 | -90.77 | 2403 |
| 83 | Bollinger breakout | breakout | 69.44 | -30.56 | 344 | 16.3 | -93.95 | -38.10 | -93.98 | 2852 |
| 84 | Stochastic reversion | reversion | 67.67 | -32.33 | 519 | 25.8 | -95.84 | -41.02 | -95.84 | 4066 |
| 85 | Consensus | meta | 66.94 | -33.06 | 319 | 9.7 | -94.79 | -29.00 | -94.79 | 2671 |
| 86 | Connors RSI(2) | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.61 | -38.60 | -96.61 | 3651 |
| 87 | Bollinger reversion | reversion | 65.96 | -34.03 | 502 | 18.1 | -95.90 | -40.05 | -95.90 | 3726 |
| 88 | EMA 9/21 cross | trend | 65.44 | -34.56 | 456 | 17.8 | -97.42 | -37.66 | -97.43 | 3560 |
| 89 | OBV trend | momentum | 63.79 | -36.21 | 510 | 15.7 | -96.19 | -43.07 | -96.19 | 3628 |
| 90 | Candlestick reversal | reversion | 63.68 | -36.32 | 565 | 16.8 | -99.35 | -43.69 | -99.35 | 5668 |
| 91 | CCI reversion | reversion | 63.12 | -36.88 | 472 | 17.8 | -98.51 | -43.97 | -98.51 | 4723 |
| 92 | VWAP momentum | momentum | 62.70 | -37.30 | 523 | 9.6 | -98.60 | -33.36 | -98.61 | 5309 |
| 93 | Parabolic SAR | trend | 61.28 | -38.72 | 473 | 15.0 | -97.15 | -47.57 | -97.15 | 3662 |
| 94 | Williams %R | reversion | 59.36 | -40.64 | 582 | 23.0 | -99.52 | -48.78 | -99.52 | 6145 |
| 95 | MACD cross | trend | 59.23 | -40.77 | 546 | 14.8 | -99.72 | -52.91 | -99.72 | 6171 |
| 96 | Heikin-Ashi | trend | 58.24 | -41.76 | 503 | 9.9 | -99.90 | -60.43 | -99.90 | 8358 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T00:05 | VWAP reversion | buy | ETH-USD | 4.10 | — | rebalance up |
| 2026-10-03T00:05 | VWAP reversion | buy | BTC-USD | 4.08 | — | rebalance up |
| 2026-10-03T00:05 | VWAP reversion | sell | DOGE-USD | 16.13 | 0.17 | exit signal |
| 2026-10-03T00:05 | Heikin-Ashi | sell | DOGE-USD | 14.49 | -0.09 | exit signal |
| 2026-10-03T00:05 | ADX DI cross | sell | ETH-USD | 17.75 | -0.12 | exit signal |
| 2026-10-03T00:05 | Parabolic SAR | sell | BTC-USD | 15.25 | -0.11 | exit signal |
| 2026-10-03T00:05 | MACD zero-line | sell | ETH-USD | 17.80 | -0.12 | exit signal |
| 2026-10-03T00:05 | MACD cross | sell | ETH-USD | 14.77 | -0.10 | exit signal |
| 2026-10-03T00:00 | Consensus | buy | DOGE-USD | 16.75 | — | entry |
| 2026-10-03T00:00 | Bollinger breakout | buy | XRP-USD | 17.40 | — | entry |
| 2026-10-03T00:00 | Bollinger breakout | buy | SOL-USD | 17.40 | — | entry |
| 2026-10-03T00:00 | Bollinger breakout | buy | DOGE-USD | 17.40 | — | entry |
| 2026-10-03T00:00 | Heikin-Ashi | buy | DOGE-USD | 14.58 | — | entry |
| 2026-10-03T00:00 | MACD cross | buy | XRP-USD | 14.87 | — | entry |
| 2026-10-03T00:00 | MACD cross | buy | SOL-USD | 14.87 | — | entry |
| 2026-10-03T00:00 | MACD cross | buy | ETH-USD | 14.87 | — | entry |
| 2026-10-03T00:00 | MACD cross | buy | DOGE-USD | 14.87 | — | entry |
| 2026-10-03T00:00 | Triple EMA stack | buy | SOL-USD | 17.66 | — | entry signal |
| 2026-10-02T23:57 | AI bee: Boozy | sell | ETH-USD | 32.23 | -0.20 | Jev: sell |
| 2026-10-02T23:52 | AI bee: Bizzy | sell | DOGE-USD | 11.01 | -0.05 | Jev: sell (sell p=0.57) after 10 min |
| 2026-10-02T23:50 | Volume breakout | buy | DOGE-USD | 20.05 | — | entry signal |
| 2026-10-02T23:50 | ROC + volume | buy | DOGE-USD | 19.95 | — | entry signal |
| 2026-10-02T23:45 | CCI reversion | sell | BTC-USD | 15.72 | -0.08 | exit signal |
| 2026-10-02T23:45 | Keltner breakout | buy | XRP-USD | 19.06 | — | entry signal |
| 2026-10-02T23:45 | OBV trend | buy | SOL-USD | 15.97 | — | entry signal |
| 2026-10-02T23:45 | RSI momentum | buy | ETH-USD | 17.49 | — | entry signal |
| 2026-10-02T23:45 | EMA 20/50 cross | buy | SOL-USD | 20.03 | — | entry signal |
| 2026-10-02T23:42 | AI bee: Boozy | buy | ETH-USD | 32.43 | — | Jev: buy (buy p=0.59) |
| 2026-10-02T23:42 | AI bee: Bizzy | buy | DOGE-USD | 11.06 | — | Jev: buy (buy p=0.56) |
| 2026-10-02T23:40 | Triple EMA stack | buy | XRP-USD | 17.69 | — | entry signal |
| 2026-10-02T23:40 | Triple EMA stack | buy | DOGE-USD | 17.69 | — | entry signal |
| 2026-10-02T23:38 | AI bee: Bizzy | sell | XRP-USD | 10.95 | -0.06 | Jev: sell (sell p=0.63) after 11 min |
| 2026-10-02T23:35 | AI bee: Boozy | sell | DOGE-USD | 32.43 | -0.15 | Jev: buy |
| 2026-10-02T23:30 | OBV trend | buy | XRP-USD | 15.98 | — | entry signal |
| 2026-10-02T23:30 | OBV trend | buy | DOGE-USD | 15.98 | — | entry signal |
| 2026-10-02T23:30 | Parabolic SAR | buy | SOL-USD | 15.36 | — | entry signal |
| 2026-10-02T23:30 | Parabolic SAR | buy | BTC-USD | 15.36 | — | entry signal |
| 2026-10-02T23:30 | EMA 20/50 cross | buy | XRP-USD | 20.04 | — | entry signal |
| 2026-10-02T23:30 | EMA 20/50 cross | buy | DOGE-USD | 20.04 | — | entry signal |
| 2026-10-02T23:27 | AI bee: Bizzy | buy | XRP-USD | 11.01 | — | Jev: buy (buy p=0.56) |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
