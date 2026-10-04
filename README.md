# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T21:35:05.000158+00:00 · 11703 ticks

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

Today: 16244 decisions in 3250 calls, $0.2270 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T21:35 | 0 / 4 / 1 | AMZN 17%, COIN 17%, MSTR 17% |  |
| Breezy | 2026-10-04T21:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T21:35 | 2 / 3 / 0 | MSTR 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.66 | +5.70% | 4 |
| Bollinger reversion · 1h | UPRO | 2.43 | +6.89% | 3 |
| RSI(14) reversion | SQQQ | 2.18 | +4.27% | 5 |
| Bollinger reversion · 1h | SPY | 2.00 | +1.40% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.94 | +3.45% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Hold BTC | benchmark | 102.65 | 2.65 | 0 | — | 34.97 | 4.25 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.27 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -24.59 | -5.61 | -26.88 | 498 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 3.28 | 0.97 | -6.57 | 121 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.82 | -3.95 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.77 | -0.23 | 20 | 55.0 | 6.18 | 1.41 | -8.60 | 158 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.41 | 1.01 | -16.96 | 114 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.36 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.02 | -0.98 | 45 | 60.0 | -8.07 | -1.66 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.92 | 0.48 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 48 | 20.8 | -21.97 | -5.65 | -25.34 | 159 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -3.94 | -1.48 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.94 | 1.74 | -14.40 | 136 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.51 | -2.49 | 59 | 44.1 | -11.73 | -3.95 | -14.21 | 222 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.50 | -3.23 | -19.41 | 496 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | -0.61 | 0.04 | -12.54 | 371 |
| 37 | Parabolic SAR · 1h | trend | 96.41 | -3.59 | 49 | 16.3 | -5.49 | -0.60 | -19.70 | 303 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.82 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.45 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -25.95 | -1.41 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 3.51 | 0.66 | -16.43 | 202 |
| 42 | MACD cross · 1h | trend | 95.94 | -4.07 | 72 | 16.7 | -11.84 | -1.86 | -17.27 | 475 |
| 43 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.63 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 23 | 17.4 | 20.66 | 2.97 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 7.50 | 1.04 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.02 | 40 | 2.5 | 1.97 | 0.46 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.33 | -6.67 | 179 | 22.3 | -39.14 | -6.16 | -39.94 | 1281 |
| 50 | Bollinger breakout · 1h | breakout | 93.23 | -6.77 | 39 | 17.9 | 6.46 | 1.02 | -12.06 | 297 |
| 51 | Triple EMA stack · 1h | trend | 93.14 | -6.86 | 50 | 8.0 | -7.55 | -0.72 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.31 | 0.65 | -12.60 | 128 |
| 54 | EMA 9/21 cross · 1h | trend | 91.80 | -8.20 | 69 | 11.6 | -3.58 | -0.29 | -18.47 | 341 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 91.00 | -9.00 | 31 | 12.9 | 0.21 | 0.24 | -16.18 | 224 |
| 57 | Heikin-Ashi · 1h | trend | 90.97 | -9.03 | 95 | 24.2 | -32.19 | -5.66 | -33.92 | 689 |
| 58 | MACD zero-line · 1h | trend | 90.92 | -9.09 | 39 | 15.4 | -2.99 | -0.18 | -18.32 | 236 |
| 59 | Three white soldiers | momentum | 90.81 | -9.19 | 77 | 14.3 | -49.60 | -26.51 | -49.92 | 593 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.48 | -1.37 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.43 | -11.57 | 22 | 0.0 | -10.89 | -1.28 | -23.19 | 214 |
| 62 | ROC + volume · 1h | momentum | 87.28 | -12.72 | 86 | 14.0 | -10.08 | -1.25 | -23.16 | 419 |
| 63 | RSI(14) reversion | reversion | 86.92 | -13.08 | 183 | 33.9 | -70.45 | -19.96 | -70.51 | 1425 |
| 64 | Donchian 55/20 | breakout | 79.37 | -20.63 | 196 | 16.3 | -68.71 | -15.61 | -68.81 | 1316 |
| 65 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.73 | -17.09 | -69.73 | 1361 |
| 66 | ROC + volume | momentum | 79.14 | -20.86 | 263 | 19.8 | -73.15 | -17.60 | -73.79 | 1664 |
| 67 | Squeeze breakout | breakout | 78.56 | -21.44 | 208 | 13.9 | -61.92 | -18.89 | -63.03 | 1234 |
| 68 | EMA 20/50 cross | trend | 77.92 | -22.08 | 219 | 17.4 | -79.08 | -16.75 | -79.24 | 1490 |
| 69 | Volume breakout | breakout | 77.21 | -22.79 | 177 | 12.4 | -64.54 | -20.21 | -64.55 | 916 |
| 70 | Z-score reversion | reversion | 75.89 | -24.11 | 294 | 28.9 | -84.78 | -26.07 | -84.81 | 2081 |
| 71 | MFI reversion | reversion | 73.80 | -26.20 | 292 | 20.9 | -87.64 | -32.63 | -87.70 | 2115 |
| 72 | Supertrend | trend | 72.71 | -27.29 | 297 | 19.5 | -87.44 | -23.53 | -87.51 | 1956 |
| 73 | AI bee: Bizzy | ai | 70.87 | -29.13 | 503 | 8.2 | — | — | — | — |
| 74 | Keltner breakout | breakout | 70.64 | -29.36 | 291 | 12.0 | -85.79 | -32.85 | -85.82 | 1913 |
| 75 | ADX DI cross | trend | 69.58 | -30.42 | 321 | 9.7 | -89.59 | -40.31 | -89.61 | 2111 |
| 76 | Ichimoku | trend | 68.70 | -31.30 | 269 | 8.2 | -82.69 | -25.80 | -82.78 | 1800 |
| 77 | AI bee: Boozy ⏸ | ai | 67.68 | -32.32 | 198 | 4.0 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 66.51 | -33.49 | 394 | 17.3 | -91.28 | -28.63 | -91.33 | 2703 |
| 79 | MACD zero-line | trend | 66.41 | -33.59 | 378 | 15.1 | -92.05 | -33.33 | -92.07 | 2388 |
| 80 | RSI momentum | momentum | 65.12 | -34.88 | 374 | 14.2 | -91.00 | -28.34 | -91.02 | 2419 |
| 81 | Trend pullback | trend | 63.95 | -36.05 | 391 | 14.3 | -91.80 | -34.19 | -91.82 | 2381 |
| 82 | Triple EMA stack | trend | 63.58 | -36.42 | 427 | 14.1 | -93.76 | -34.86 | -93.79 | 2676 |
| 83 | Stochastic reversion | reversion | 63.47 | -36.53 | 576 | 23.3 | -95.62 | -40.29 | -95.65 | 4054 |
| 84 | Bollinger reversion | reversion | 62.82 | -37.18 | 540 | 16.9 | -95.61 | -39.04 | -95.61 | 3691 |
| 85 | Bollinger breakout ⏸ | breakout | 62.49 | -37.51 | 414 | 13.8 | -94.23 | -38.85 | -94.27 | 2874 |
| 86 | Consensus ⏸ | meta | 60.98 | -39.02 | 381 | 8.7 | -94.33 | -27.93 | -94.36 | 2637 |
| 87 | EMA 9/21 cross | trend | 59.06 | -40.94 | 534 | 15.9 | -97.58 | -38.34 | -97.59 | 3594 |
| 88 | Connors RSI(2) ⏸ | reversion | 58.75 | -41.25 | 506 | 16.0 | -96.62 | -38.95 | -96.63 | 3661 |
| 89 | CCI reversion | reversion | 57.64 | -42.36 | 543 | 15.5 | -98.45 | -44.20 | -98.45 | 4719 |
| 90 | Candlestick reversal | reversion | 57.58 | -42.42 | 640 | 14.8 | -99.30 | -43.63 | -99.30 | 5633 |
| 91 | VWAP momentum | momentum | 57.02 | -42.98 | 595 | 8.6 | -98.69 | -34.36 | -98.70 | 5347 |
| 92 | OBV trend | momentum | 56.95 | -43.05 | 592 | 13.9 | -96.45 | -44.04 | -96.48 | 3671 |
| 93 | Parabolic SAR ⏸ | trend | 54.05 | -45.95 | 551 | 12.9 | -97.41 | -47.58 | -97.42 | 3714 |
| 94 | Williams %R | reversion | 52.59 | -47.41 | 678 | 19.8 | -99.50 | -49.16 | -99.50 | 6142 |
| 95 | MACD cross ⏸ | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -53.57 | -99.73 | 6201 |
| 96 | Heikin-Ashi ⏸ | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -62.42 | -99.90 | 8369 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T21:35 | Ichimoku | buy | XRP-USD | 17.19 | — | entry signal |
| 2026-10-04T21:30 | Volume breakout | sell | BTC-USD | 19.29 | -0.07 | exit signal |
| 2026-10-04T21:30 | Keltner breakout | sell | BTC-USD | 17.61 | -0.05 | stop-loss |
| 2026-10-04T21:30 | ROC + volume | sell | BTC-USD | 19.65 | -0.16 | stop-loss |
| 2026-10-04T21:25 | Volume breakout | sell | ETH-USD | 19.23 | -0.14 | exit signal |
| 2026-10-04T21:25 | Ichimoku | sell | ETH-USD | 17.10 | -0.11 | exit signal |
| 2026-10-04T21:22 | AI bee: Bizzy | sell | DOGE-USD | 14.03 | -0.05 | Jev: sell (sell p=0.54) after 13 min |
| 2026-10-04T21:20 | MFI reversion | sell | SOL-USD | 18.41 | -0.01 | exit signal |
| 2026-10-04T21:20 | Volume breakout | buy | DOGE-USD | 19.35 | — | entry signal |
| 2026-10-04T21:20 | MACD zero-line | buy | SOL-USD | 16.62 | — | entry signal |
| 2026-10-04T21:15 | CCI reversion | sell | SOL-USD | 14.41 | -0.03 | exit signal |
| 2026-10-04T21:15 | Z-score reversion | sell | SOL-USD | 18.94 | -0.04 | exit signal |
| 2026-10-04T21:15 | Candlestick reversal | sell | SOL-USD | 14.39 | -0.01 | take-profit |
| 2026-10-04T21:15 | Volume breakout | buy | ETH-USD | 19.37 | — | entry signal |
| 2026-10-04T21:15 | Keltner breakout | buy | XRP-USD | 17.68 | — | entry signal |
| 2026-10-04T21:15 | Donchian 55/20 | buy | XRP-USD | 19.09 | — | entry signal |
| 2026-10-04T21:15 | Donchian 55/20 | buy | ETH-USD | 19.86 | — | entry signal |
| 2026-10-04T21:15 | Donchian 20/10 | buy | XRP-USD | 16.59 | — | entry signal |
| 2026-10-04T21:15 | RSI momentum | buy | SOL-USD | 6.16 | — | entry signal |
| 2026-10-04T21:15 | RSI momentum | sell | BTC-USD | 3.31 | 0.00 | rebalance down |
| 2026-10-04T21:15 | ROC + volume | buy | BTC-USD | 19.81 | — | entry signal |
| 2026-10-04T21:15 | EMA 9/21 cross | buy | SOL-USD | 5.57 | — | entry signal |
| 2026-10-04T21:15 | EMA 9/21 cross | sell | BTC-USD | 3.04 | 0.01 | rebalance down |
| 2026-10-04T21:10 | CCI reversion | sell | XRP-USD | 14.37 | -0.06 | exit signal |
| 2026-10-04T21:10 | Williams %R | sell | XRP-USD | 13.12 | -0.05 | exit signal |
| 2026-10-04T21:10 | Stochastic reversion | sell | XRP-USD | 15.83 | -0.06 | exit signal |
| 2026-10-04T21:10 | RSI(14) reversion | sell | SOL-USD | 21.69 | -0.05 | exit signal |
| 2026-10-04T21:10 | Candlestick reversal | sell | XRP-USD | 14.37 | -0.04 | exit signal |
| 2026-10-04T21:10 | Squeeze breakout | buy | XRP-USD | 19.63 | — | entry signal |
| 2026-10-04T21:10 | Donchian 20/10 | buy | ETH-USD | 16.63 | — | entry signal |
| 2026-10-04T21:10 | RSI momentum | buy | XRP-USD | 16.28 | — | entry signal |
| 2026-10-04T21:10 | Trend pullback | sell | DOGE-USD | 16.15 | 0.09 | take-profit |
| 2026-10-04T21:09 | AI bee: Bizzy | buy | DOGE-USD | 14.08 | — | Jev: buy (buy p=0.79) |
| 2026-10-04T21:05 | Bollinger reversion | sell | XRP-USD | 15.67 | -0.06 | exit signal |
| 2026-10-04T21:05 | Squeeze breakout | buy | DOGE-USD | 19.62 | — | entry signal |
| 2026-10-04T21:05 | Keltner breakout | buy | DOGE-USD | 17.66 | — | entry signal |
| 2026-10-04T21:05 | ROC + volume | buy | DOGE-USD | 19.80 | — | entry signal |
| 2026-10-04T21:05 | Triple EMA stack | buy | XRP-USD | 15.86 | — | entry signal |
| 2026-10-04T21:05 | EMA 9/21 cross | buy | XRP-USD | 14.74 | — | entry signal |
| 2026-10-04T21:00 | Keltner breakout · 1h | buy | BTC-USD | 6.80 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
