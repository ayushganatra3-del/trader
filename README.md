# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T02:35:05.000148+00:00 · 11955 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.25 (-0.76%)

Closed trades 33, win rate 66.7%, fees £1.04, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, GME 12%, BPRE 12%, PAM 12%, CX 12%, GPUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 1950 decisions in 390 calls, $0.0274 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T02:35 | 0 / 3 / 2 | ETH-USD 14%, AMZN 18%, COIN 18%, MSTR 17% |  |
| Breezy | 2026-10-05T02:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T02:35 | 1 / 3 / 1 | MSTR 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.58 | +4.45% | 4 |
| VWAP reversion | AMZN | 1.94 | +0.87% | 3 |
| Z-score reversion | SQQQ | 1.74 | +3.40% | 6 |
| RSI(14) reversion | SQQQ | 1.71 | +3.09% | 4 |
| VWAP reversion | SQQQ | 1.63 | +1.18% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Hold BTC | benchmark | 103.33 | 3.33 | 0 | — | 35.12 | 4.22 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.20 | 2.20 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.07 | 2.08 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.05 | 1.05 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.97 | 0.97 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.89 | 0.89 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.89 | 0.89 | 53 | 37.7 | -24.28 | -5.48 | -26.58 | 496 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 4.10 | 1.18 | -6.57 | 119 |
| 9 | Hold SPY | benchmark | 100.12 | 0.12 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.91 | -0.09 | 41 | 43.9 | -14.82 | -3.92 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.79 | -0.21 | 20 | 55.0 | 6.18 | 1.40 | -8.60 | 158 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.71 | -0.28 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.68 | -0.32 | 17 | 0.0 | 6.31 | 0.99 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.63 | -0.37 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.48 | -0.52 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.04 | -0.96 | 45 | 60.0 | -8.07 | -1.65 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.91 | -1.09 | 63 | 49.2 | 1.94 | 0.48 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 98.83 | -1.17 | 49 | 22.4 | -21.73 | -5.52 | -25.34 | 158 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.75 | -1.25 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -4.27 | -1.61 | -9.74 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.80 | -2.20 | 25 | 8.0 | 13.87 | 1.72 | -14.40 | 137 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.78 | -2.21 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.51 | -2.49 | 60 | 43.3 | -11.84 | -3.96 | -14.21 | 220 |
| 34 | Williams %R · 1h | reversion | 97.49 | -2.51 | 70 | 54.3 | -17.14 | -3.13 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 207 | 17.4 | 2.71 | 0.63 | -11.03 | 360 |
| 37 | Parabolic SAR · 1h | trend | 96.56 | -3.44 | 49 | 16.3 | -5.41 | -0.59 | -19.70 | 305 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.44 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.14 | -3.86 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 96.05 | -3.96 | 28 | 7.1 | 3.58 | 0.66 | -16.43 | 202 |
| 42 | MACD cross · 1h | trend | 96.04 | -3.96 | 72 | 16.7 | -11.99 | -1.86 | -17.27 | 476 |
| 43 | Copy: Insider buying | copy | 95.84 | -4.16 | 6 | 50.0 | -18.81 | -3.69 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.69 | -4.31 | 41 | 12.2 | -4.65 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.48 | -4.52 | 24 | 16.7 | 20.65 | 2.94 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.26 | -5.74 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 94.00 | -6.00 | 40 | 2.5 | 2.04 | 0.46 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.36 | -6.64 | 181 | 23.2 | -38.54 | -6.00 | -39.36 | 1276 |
| 50 | Bollinger breakout · 1h | breakout | 93.35 | -6.65 | 40 | 20.0 | 6.75 | 1.05 | -12.06 | 296 |
| 51 | Triple EMA stack · 1h | trend | 93.16 | -6.84 | 50 | 8.0 | -7.97 | -0.77 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.50 | -7.50 | 30 | 6.7 | 3.17 | 0.62 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 91.86 | -8.14 | 69 | 11.6 | -3.05 | -0.22 | -18.47 | 339 |
| 55 | Max aggression: 5-day momentum | meta | 91.31 | -8.69 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 91.10 | -8.90 | 31 | 12.9 | 0.10 | 0.23 | -16.18 | 224 |
| 57 | MACD zero-line · 1h | trend | 91.00 | -9.00 | 39 | 15.4 | -2.86 | -0.16 | -18.32 | 236 |
| 58 | Heikin-Ashi · 1h | trend | 90.81 | -9.19 | 96 | 25.0 | -31.80 | -5.53 | -33.92 | 686 |
| 59 | Three white soldiers | momentum | 90.65 | -9.35 | 78 | 14.1 | -49.69 | -26.13 | -50.01 | 594 |
| 60 | OBV trend · 1h | momentum | 89.47 | -10.53 | 97 | 11.3 | -12.45 | -1.35 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.34 | -11.66 | 23 | 4.3 | -11.01 | -1.29 | -23.19 | 217 |
| 62 | ROC + volume · 1h | momentum | 87.25 | -12.75 | 87 | 14.9 | -9.88 | -1.21 | -23.16 | 419 |
| 63 | RSI(14) reversion | reversion | 86.92 | -13.08 | 183 | 33.9 | -70.41 | -19.62 | -70.48 | 1421 |
| 64 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.99 | -16.98 | -69.99 | 1368 |
| 65 | Donchian 55/20 | breakout | 78.44 | -21.56 | 204 | 16.7 | -68.82 | -15.44 | -69.12 | 1316 |
| 66 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.10 | -18.75 | -63.10 | 1235 |
| 67 | ROC + volume | momentum | 77.90 | -22.10 | 270 | 19.3 | -73.43 | -17.50 | -74.19 | 1666 |
| 68 | EMA 20/50 cross | trend | 77.68 | -22.32 | 221 | 17.6 | -78.96 | -16.51 | -79.05 | 1488 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.67 | -19.90 | -64.67 | 918 |
| 70 | Z-score reversion | reversion | 75.89 | -24.11 | 294 | 28.9 | -84.78 | -25.52 | -84.81 | 2081 |
| 71 | MFI reversion | reversion | 73.57 | -26.43 | 294 | 20.7 | -87.56 | -31.61 | -87.61 | 2108 |
| 72 | Supertrend | trend | 72.40 | -27.60 | 300 | 19.7 | -87.38 | -23.11 | -87.41 | 1952 |
| 73 | AI bee: Bizzy | ai | 69.84 | -30.16 | 515 | 8.0 | — | — | — | — |
| 74 | Keltner breakout | breakout | 69.38 | -30.62 | 301 | 11.6 | -85.85 | -31.91 | -85.87 | 1914 |
| 75 | ADX DI cross | trend | 68.84 | -31.16 | 327 | 9.5 | -89.56 | -38.89 | -89.58 | 2108 |
| 76 | Ichimoku | trend | 67.98 | -32.02 | 275 | 8.0 | -82.68 | -25.45 | -82.87 | 1799 |
| 77 | AI bee: Boozy | ai | 67.26 | -32.74 | 201 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.14 | -33.86 | 381 | 15.0 | -92.04 | -32.49 | -92.05 | 2385 |
| 79 | Donchian 20/10 | breakout | 65.60 | -34.40 | 403 | 17.1 | -91.31 | -28.12 | -91.35 | 2702 |
| 80 | RSI momentum | momentum | 64.11 | -35.89 | 383 | 14.4 | -90.98 | -28.07 | -90.98 | 2416 |
| 81 | Triple EMA stack | trend | 62.93 | -37.07 | 434 | 14.5 | -93.69 | -34.43 | -93.69 | 2670 |
| 82 | Stochastic reversion | reversion | 62.75 | -37.24 | 585 | 22.9 | -95.61 | -38.97 | -95.65 | 4051 |
| 83 | Trend pullback | trend | 62.70 | -37.30 | 402 | 14.2 | -91.83 | -33.45 | -91.83 | 2384 |
| 84 | Bollinger reversion | reversion | 62.38 | -37.62 | 546 | 16.7 | -95.60 | -37.75 | -95.60 | 3687 |
| 85 | Bollinger breakout | breakout | 61.90 | -38.10 | 418 | 13.6 | -94.25 | -37.80 | -94.29 | 2874 |
| 86 | Consensus | meta | 60.27 | -39.73 | 386 | 8.5 | -94.38 | -27.60 | -94.38 | 2641 |
| 87 | EMA 9/21 cross | trend | 58.42 | -41.58 | 541 | 16.3 | -97.58 | -37.57 | -97.59 | 3593 |
| 88 | Connors RSI(2) | reversion | 58.34 | -41.66 | 511 | 15.9 | -96.63 | -37.44 | -96.63 | 3664 |
| 89 | Candlestick reversal | reversion | 57.24 | -42.77 | 645 | 14.9 | -99.29 | -41.68 | -99.29 | 5628 |
| 90 | CCI reversion | reversion | 57.08 | -42.92 | 550 | 15.3 | -98.44 | -42.28 | -98.45 | 4712 |
| 91 | VWAP momentum | momentum | 55.73 | -44.27 | 612 | 9.0 | -98.70 | -33.76 | -98.70 | 5351 |
| 92 | OBV trend | momentum | 55.46 | -44.54 | 607 | 14.0 | -96.46 | -43.29 | -96.47 | 3670 |
| 93 | Parabolic SAR | trend | 53.49 | -46.51 | 555 | 12.8 | -97.42 | -45.60 | -97.43 | 3718 |
| 94 | Williams %R | reversion | 51.71 | -48.29 | 689 | 19.4 | -99.50 | -46.73 | -99.50 | 6139 |
| 95 | MACD cross | trend | 51.70 | -48.30 | 635 | 12.8 | -99.73 | -51.09 | -99.73 | 6204 |
| 96 | Heikin-Ashi | trend | 50.17 | -49.83 | 599 | 8.3 | -99.90 | -58.49 | -99.90 | 8371 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T02:35 | AI bee: Boozy | sell | ETH-USD | 22.69 | -0.19 | Jev: sell |
| 2026-10-05T02:35 | Consensus | sell | DOGE-USD | 14.84 | -0.15 | target is flat |
| 2026-10-05T02:35 | Stochastic reversion | buy | BTC-USD | 15.70 | — | entry signal |
| 2026-10-05T02:35 | Connors RSI(2) | buy | XRP-USD | 14.60 | — | entry signal |
| 2026-10-05T02:35 | OBV trend | sell | DOGE-USD | 13.75 | -0.14 | exit signal |
| 2026-10-05T02:35 | VWAP momentum | sell | ETH-USD | 11.16 | -0.06 | exit signal |
| 2026-10-05T02:35 | Trend pullback | sell | BTC-USD | 15.60 | -0.13 | exit signal |
| 2026-10-05T02:35 | Heikin-Ashi | sell | ETH-USD | 12.53 | -0.09 | exit signal |
| 2026-10-05T02:35 | ADX DI cross | sell | SOL-USD | 17.14 | -0.13 | exit signal |
| 2026-10-05T02:35 | MACD cross | sell | DOGE-USD | 12.85 | -0.13 | exit signal |
| 2026-10-05T02:30 | Consensus | sell | BTC-USD | 15.15 | -0.09 | target is flat |
| 2026-10-05T02:30 | Connors RSI(2) | buy | BTC-USD | 14.61 | — | entry signal |
| 2026-10-05T02:30 | OBV trend | sell | BTC-USD | 13.92 | -0.12 | exit signal |
| 2026-10-05T02:30 | RSI momentum | sell | BTC-USD | 16.05 | -0.11 | exit signal |
| 2026-10-05T02:30 | VWAP momentum | sell | XRP-USD | 13.92 | -0.11 | exit signal |
| 2026-10-05T02:30 | VWAP momentum | sell | SOL-USD | 13.94 | -0.10 | exit signal |
| 2026-10-05T02:30 | Triple EMA stack | sell | BTC-USD | 15.73 | -0.11 | exit signal |
| 2026-10-05T02:30 | EMA 9/21 cross | buy | XRP-USD | 2.91 | — | rebalance up |
| 2026-10-05T02:30 | EMA 9/21 cross | buy | SOL-USD | 5.83 | — | rebalance up |
| 2026-10-05T02:30 | EMA 9/21 cross | buy | DOGE-USD | 2.93 | — | rebalance up |
| 2026-10-05T02:30 | EMA 9/21 cross | sell | BTC-USD | 11.68 | -0.08 | exit signal |
| 2026-10-05T02:28 | AI bee: Bizzy | buy | ETH-USD | 10.13 | — | Jev: buy (buy p=0.58) |
| 2026-10-05T02:27 | AI bee: Bizzy | sell | DOGE-USD | 11.33 | -0.11 | Jev: sell (sell p=0.86) after 10 min |
| 2026-10-05T02:25 | Donchian 20/10 | sell | BTC-USD | 16.39 | -0.13 | exit signal |
| 2026-10-05T02:25 | Heikin-Ashi | sell | XRP-USD | 12.53 | -0.09 | exit signal |
| 2026-10-05T02:25 | Heikin-Ashi | sell | SOL-USD | 12.55 | -0.08 | exit signal |
| 2026-10-05T02:25 | Heikin-Ashi | sell | DOGE-USD | 12.53 | -0.10 | exit signal |
| 2026-10-05T02:25 | ADX DI cross | sell | BTC-USD | 17.23 | -0.11 | exit signal |
| 2026-10-05T02:20 | RSI momentum | buy | ETH-USD | 16.05 | — | entry signal |
| 2026-10-05T02:20 | VWAP momentum | buy | XRP-USD | 2.81 | — | rebalance up |
| 2026-10-05T02:20 | VWAP momentum | buy | SOL-USD | 2.81 | — | rebalance up |
| 2026-10-05T02:20 | VWAP momentum | sell | BTC-USD | 11.14 | -0.09 | exit signal |
| 2026-10-05T02:20 | Parabolic SAR | buy | XRP-USD | 13.42 | — | entry signal |
| 2026-10-05T02:20 | Parabolic SAR | buy | DOGE-USD | 13.42 | — | entry signal |
| 2026-10-05T02:19 | AI bee: Boozy | buy | ETH-USD | 22.88 | — | Jev: buy (buy p=0.67) |
| 2026-10-05T02:17 | AI bee: Bizzy | buy | DOGE-USD | 11.44 | — | Jev: buy (buy p=0.65) |
| 2026-10-05T02:17 | AI bee: Bizzy | sell | SOL-USD | 9.74 | -0.04 | Jev: sell (sell p=0.53) after 10 min |
| 2026-10-05T02:15 | Consensus | buy | DOGE-USD | 14.99 | — | entry |
| 2026-10-05T02:15 | Williams %R | sell | SOL-USD | 12.93 | -0.03 | exit signal |
| 2026-10-05T02:15 | Williams %R | sell | ETH-USD | 12.93 | -0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 02:35:05.000148+00:00 -> 2026-10-05 02:45:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
