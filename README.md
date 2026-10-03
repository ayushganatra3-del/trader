# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T02:35:05.000143+00:00 · 9550 ticks

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

Today: 1995 decisions in 399 calls, $0.0279 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T02:35 | 2 / 1 / 2 | AMZN 16%, COIN 16%, MSTR 15% |  |
| Breezy | 2026-10-03T02:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T02:35 | 3 / 2 / 0 | BTC-USD 41% |  |

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
| 3 | Hold BTC | benchmark | 101.18 | 1.18 | 0 | — | 33.11 | 4.07 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.70 | -3.16 | -14.05 | 116 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.00 | -5.22 | -26.06 | 497 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 10 | 60.0 | 5.01 | 1.44 | -6.57 | 118 |
| 9 | Bollinger reversion · 1h | reversion | 100.18 | 0.18 | 38 | 44.7 | -14.67 | -3.90 | -17.68 | 307 |
| 10 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.91 | 1.94 | -1.46 | 86 |
| 14 | Z-score reversion · 1h | reversion | 99.75 | -0.25 | 18 | 55.6 | 5.64 | 1.30 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.70 | 1.05 | -16.96 | 115 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.08 | -0.92 | 40 | 60.0 | -8.64 | -1.79 | -9.86 | 334 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.77 | 0.45 | -12.41 | 419 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 45 | 20.0 | -21.96 | -5.63 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.90 | -2.10 | 50 | 20.0 | -3.24 | -1.21 | -8.90 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 14.00 | 1.75 | -14.40 | 132 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -12.45 | -4.20 | -14.21 | 226 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.64 | -3.05 | -19.41 | 501 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 1.64 | 0.44 | -11.23 | 384 |
| 37 | MFI reversion · 1h | reversion | 96.62 | -3.38 | 69 | 29.0 | -6.94 | -1.14 | -16.99 | 121 |
| 38 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -7.86 | -0.96 | -19.70 | 311 |
| 39 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.60 | 2.81 | -4.73 | 199 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 2.56 | 0.53 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.60 | -3.69 | -21.08 | 71 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -5.83 | -0.83 | -13.84 | 274 |
| 44 | MACD cross · 1h | trend | 95.50 | -4.50 | 71 | 15.5 | -14.70 | -2.37 | -17.27 | 483 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.31 | 0.92 | -16.19 | 127 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.88 | 0.45 | -16.65 | 227 |
| 49 | VWAP momentum · 1h | momentum | 93.45 | -6.55 | 171 | 22.8 | -40.96 | -6.46 | -42.62 | 1284 |
| 50 | Bollinger breakout · 1h | breakout | 93.18 | -6.82 | 36 | 16.7 | 5.73 | 0.93 | -12.06 | 292 |
| 51 | Triple EMA stack · 1h | trend | 93.11 | -6.89 | 50 | 8.0 | -7.32 | -0.69 | -23.88 | 240 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Three white soldiers | momentum | 92.52 | -7.48 | 66 | 16.7 | -49.26 | -26.26 | -49.26 | 591 |
| 54 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 2.74 | 0.57 | -12.60 | 128 |
| 55 | EMA 9/21 cross · 1h | trend | 91.74 | -8.26 | 68 | 11.8 | -5.12 | -0.51 | -18.47 | 343 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | Heikin-Ashi · 1h | trend | 91.08 | -8.92 | 86 | 25.6 | -32.94 | -5.85 | -33.56 | 690 |
| 58 | MACD zero-line · 1h | trend | 90.81 | -9.19 | 38 | 13.2 | -4.93 | -0.44 | -18.32 | 238 |
| 59 | Donchian 20/10 · 1h | breakout | 90.65 | -9.35 | 31 | 12.9 | 0.01 | 0.22 | -16.18 | 219 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -13.38 | -1.49 | -26.66 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.62 | -1.39 | -23.19 | 214 |
| 62 | RSI(14) reversion | reversion | 87.33 | -12.67 | 179 | 34.6 | -72.53 | -21.04 | -72.57 | 1462 |
| 63 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -12.81 | -1.65 | -23.45 | 424 |
| 64 | Squeeze breakout | breakout | 82.76 | -17.24 | 175 | 16.0 | -60.35 | -18.35 | -61.02 | 1207 |
| 65 | Donchian 55/20 | breakout | 82.27 | -17.73 | 170 | 18.8 | -68.18 | -15.30 | -68.22 | 1307 |
| 66 | EMA 20/50 cross | trend | 80.15 | -19.85 | 191 | 18.8 | -78.86 | -16.73 | -79.03 | 1483 |
| 67 | Volume breakout | breakout | 79.88 | -20.12 | 157 | 14.0 | -64.22 | -20.02 | -64.22 | 910 |
| 68 | VWAP reversion | reversion | 79.87 | -20.12 | 208 | 28.8 | -71.41 | -17.41 | -71.63 | 1394 |
| 69 | ROC + volume | momentum | 79.77 | -20.23 | 258 | 20.2 | -73.58 | -17.83 | -73.89 | 1668 |
| 70 | AI bee: Bizzy | ai | 77.93 | -22.07 | 403 | 10.2 | — | — | — | — |
| 71 | Z-score reversion | reversion | 77.69 | -22.31 | 274 | 31.0 | -85.84 | -26.93 | -85.86 | 2113 |
| 72 | MFI reversion | reversion | 76.14 | -23.86 | 267 | 22.5 | -88.31 | -33.49 | -88.33 | 2138 |
| 73 | Keltner breakout | breakout | 75.95 | -24.05 | 247 | 13.8 | -85.37 | -32.33 | -85.37 | 1900 |
| 74 | Ichimoku | trend | 75.70 | -24.30 | 209 | 10.0 | -81.56 | -25.49 | -81.56 | 1764 |
| 75 | AI bee: Boozy | ai | 75.63 | -24.37 | 150 | 5.3 | — | — | — | — |
| 76 | Supertrend | trend | 75.37 | -24.63 | 266 | 20.7 | -87.34 | -23.47 | -87.39 | 1952 |
| 77 | Donchian 20/10 | breakout | 72.27 | -27.73 | 343 | 19.5 | -90.89 | -28.12 | -90.90 | 2685 |
| 78 | MACD zero-line | trend | 71.60 | -28.40 | 334 | 17.1 | -91.75 | -32.58 | -91.75 | 2371 |
| 79 | ADX DI cross | trend | 71.28 | -28.72 | 305 | 10.2 | -89.83 | -41.48 | -89.83 | 2124 |
| 80 | Trend pullback | trend | 70.85 | -29.15 | 318 | 17.0 | -91.56 | -32.74 | -91.56 | 2350 |
| 81 | Triple EMA stack | trend | 70.68 | -29.32 | 353 | 16.7 | -93.23 | -33.80 | -93.24 | 2635 |
| 82 | RSI momentum | momentum | 70.17 | -29.83 | 324 | 15.7 | -90.68 | -27.71 | -90.73 | 2401 |
| 83 | Bollinger breakout | breakout | 69.16 | -30.84 | 350 | 16.0 | -93.93 | -38.18 | -93.94 | 2849 |
| 84 | Stochastic reversion | reversion | 67.62 | -32.38 | 519 | 25.8 | -95.84 | -41.08 | -95.84 | 4067 |
| 85 | Consensus | meta | 66.73 | -33.27 | 322 | 9.6 | -94.83 | -29.23 | -94.83 | 2678 |
| 86 | Connors RSI(2) | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.60 | -38.55 | -96.60 | 3649 |
| 87 | Bollinger reversion | reversion | 65.87 | -34.13 | 503 | 18.1 | -95.91 | -40.13 | -95.91 | 3727 |
| 88 | EMA 9/21 cross | trend | 65.56 | -34.44 | 457 | 17.7 | -97.42 | -37.58 | -97.43 | 3561 |
| 89 | OBV trend | momentum | 63.80 | -36.20 | 512 | 15.6 | -96.14 | -42.54 | -96.15 | 3623 |
| 90 | Candlestick reversal | reversion | 63.60 | -36.40 | 566 | 16.8 | -99.36 | -43.86 | -99.36 | 5673 |
| 91 | CCI reversion | reversion | 62.95 | -37.05 | 473 | 17.8 | -98.51 | -44.16 | -98.51 | 4726 |
| 92 | VWAP momentum | momentum | 62.14 | -37.86 | 528 | 9.5 | -98.66 | -34.22 | -98.66 | 5332 |
| 93 | Parabolic SAR | trend | 60.68 | -39.32 | 481 | 14.8 | -97.16 | -48.14 | -97.16 | 3662 |
| 94 | Williams %R | reversion | 59.11 | -40.89 | 584 | 22.9 | -99.52 | -49.09 | -99.52 | 6149 |
| 95 | MACD cross | trend | 58.74 | -41.26 | 554 | 14.6 | -99.72 | -53.49 | -99.72 | 6171 |
| 96 | Heikin-Ashi | trend | 57.34 | -42.66 | 513 | 9.7 | -99.90 | -62.01 | -99.90 | 8355 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T02:35 | Donchian 55/20 | buy | DOGE-USD | 4.10 | — | rebalance up |
| 2026-10-03T02:35 | Donchian 55/20 | sell | BTC-USD | 4.10 | -0.02 | rebalance down |
| 2026-10-03T02:35 | VWAP momentum | sell | DOGE-USD | 15.49 | -0.12 | exit signal |
| 2026-10-03T02:30 | Consensus | sell | DOGE-USD | 16.61 | -0.10 | target is flat |
| 2026-10-03T02:30 | VWAP momentum | buy | DOGE-USD | 6.33 | — | rebalance up |
| 2026-10-03T02:30 | VWAP momentum | sell | XRP-USD | 15.49 | -0.10 | exit signal |
| 2026-10-03T02:30 | Heikin-Ashi | sell | DOGE-USD | 14.28 | -0.09 | exit signal |
| 2026-10-03T02:26 | AI bee: Bizzy | sell | DOGE-USD | 10.73 | -0.07 | Jev: sell (sell p=0.86) after 10 min |
| 2026-10-03T02:25 | Consensus | buy | DOGE-USD | 16.71 | — | entry |
| 2026-10-03T02:25 | Heikin-Ashi | buy | ETH-USD | 14.37 | — | entry signal |
| 2026-10-03T02:25 | Heikin-Ashi | buy | DOGE-USD | 14.37 | — | entry signal |
| 2026-10-03T02:23 | AI bee: Boozy | buy | BTC-USD | 31.17 | — | Jev: buy (buy p=0.60) |
| 2026-10-03T02:20 | CCI reversion | buy | BTC-USD | 15.76 | — | entry signal |
| 2026-10-03T02:20 | VWAP momentum | buy | DOGE-USD | 9.27 | — | entry signal |
| 2026-10-03T02:20 | VWAP momentum | sell | SOL-USD | 3.14 | -0.02 | rebalance down |
| 2026-10-03T02:16 | AI bee: Boozy | sell | ETH-USD | 31.17 | -0.20 | Jev: sell |
| 2026-10-03T02:16 | AI bee: Bizzy | buy | DOGE-USD | 10.80 | — | Jev: buy (buy p=0.55) |
| 2026-10-03T02:15 | MFI reversion | buy | BTC-USD | 19.05 | — | entry signal |
| 2026-10-03T02:15 | CCI reversion | buy | DOGE-USD | 15.76 | — | entry signal |
| 2026-10-03T02:15 | Williams %R | buy | DOGE-USD | 14.79 | — | entry signal |
| 2026-10-03T02:15 | Donchian 55/20 | buy | DOGE-USD | 8.20 | — | entry |
| 2026-10-03T02:15 | Donchian 20/10 | buy | DOGE-USD | 18.08 | — | entry |
| 2026-10-03T02:15 | OBV trend | buy | ETH-USD | 15.96 | — | entry signal |
| 2026-10-03T02:15 | VWAP momentum | buy | XRP-USD | 15.59 | — | entry signal |
| 2026-10-03T02:15 | ADX DI cross | buy | DOGE-USD | 17.83 | — | entry signal |
| 2026-10-03T02:10 | Squeeze breakout | sell | ETH-USD | 20.68 | -0.12 | stop-loss |
| 2026-10-03T02:10 | Keltner breakout | sell | XRP-USD | 18.98 | -0.08 | exit signal |
| 2026-10-03T02:10 | Keltner breakout | sell | SOL-USD | 18.98 | -0.10 | exit signal |
| 2026-10-03T02:10 | Keltner breakout | sell | ETH-USD | 18.92 | -0.11 | stop-loss |
| 2026-10-03T02:10 | Bollinger breakout | sell | ETH-USD | 13.84 | -0.05 | stop-loss |
| 2026-10-03T02:10 | Donchian 55/20 | buy | BTC-USD | 8.19 | — | rebalance up |
| 2026-10-03T02:10 | Donchian 55/20 | sell | DOGE-USD | 16.39 | -0.02 | exit signal |
| 2026-10-03T02:10 | Donchian 20/10 | buy | BTC-USD | 3.75 | — | rebalance up |
| 2026-10-03T02:10 | Donchian 20/10 | sell | ETH-USD | 14.44 | -0.06 | exit signal |
| 2026-10-03T02:10 | Donchian 20/10 | sell | DOGE-USD | 14.53 | 0.11 | exit signal |
| 2026-10-03T02:10 | OBV trend | sell | XRP-USD | 15.93 | -0.04 | exit signal |
| 2026-10-03T02:10 | OBV trend | sell | ETH-USD | 15.89 | -0.09 | exit signal |
| 2026-10-03T02:10 | VWAP momentum | sell | XRP-USD | 15.55 | -0.08 | exit signal |
| 2026-10-03T02:00 | AI bee: Boozy | buy | ETH-USD | 31.37 | — | Jev: buy (buy p=0.60) |
| 2026-10-03T02:00 | VWAP momentum · 1h | buy | ETH-USD | 10.01 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
