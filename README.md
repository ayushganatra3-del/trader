# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T03:35:05.000124+00:00 · 12007 ticks

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

Today: 2730 decisions in 546 calls, $0.0383 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T03:35 | 0 / 3 / 2 | DOGE-USD 15%, AMZN 18%, COIN 18%, MSTR 17% |  |
| Breezy | 2026-10-05T03:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T03:35 | 1 / 3 / 1 | MSTR 66% |  |

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
| 1 | Hold BTC | benchmark | 103.54 | 3.54 | 0 | — | 34.55 | 4.17 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.52 | 2.52 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.39 | 2.39 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.28 | 1.28 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.28 | 1.28 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 101.20 | 1.20 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 101.20 | 1.20 | 53 | 37.7 | -23.20 | -5.27 | -25.54 | 491 |
| 8 | RSI(14) reversion · 1h | reversion | 100.70 | 0.70 | 11 | 63.6 | 4.98 | 1.42 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.43 | 0.43 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Bollinger reversion · 1h | reversion | 100.07 | 0.07 | 41 | 43.9 | -14.71 | -3.89 | -17.43 | 304 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 100.02 | 0.02 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 12 | Z-score reversion · 1h | reversion | 100.02 | 0.02 | 20 | 55.0 | 6.18 | 1.40 | -8.60 | 158 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Donchian 55/20 · 1h | breakout | 99.99 | -0.01 | 17 | 0.0 | 6.28 | 0.99 | -16.96 | 116 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.94 | -0.06 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 18 | Daily: Bullish score | daily | 99.79 | -0.21 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Stochastic reversion · 1h | reversion | 99.24 | -0.76 | 45 | 60.0 | -8.06 | -1.65 | -9.82 | 327 |
| 21 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 22 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 23 | CCI reversion · 1h | reversion | 99.21 | -0.79 | 63 | 49.2 | 1.95 | 0.48 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 99.13 | -0.87 | 49 | 22.4 | -21.26 | -5.40 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 99.05 | -0.95 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | EMA 20/50 cross · 1h | trend | 98.11 | -1.89 | 25 | 8.0 | 13.90 | 1.72 | -14.40 | 137 |
| 30 | Daily: SMA 20/50 cross · AAPL | daily | 98.09 | -1.91 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 31 | Agent (rotation) | meta | 97.99 | -2.01 | 52 | 23.1 | -4.27 | -1.61 | -9.74 | 228 |
| 32 | Williams %R · 1h | reversion | 97.79 | -2.21 | 70 | 54.3 | -17.11 | -3.12 | -19.41 | 495 |
| 33 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 34 | Connors RSI(2) · 1h | reversion | 97.73 | -2.27 | 60 | 43.3 | -11.84 | -3.96 | -14.21 | 220 |
| 35 | Daily: Momentum burst | daily | 97.06 | -2.94 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.99 | -3.01 | 207 | 17.4 | 1.16 | 0.35 | -12.31 | 368 |
| 37 | Parabolic SAR · 1h | trend | 96.82 | -3.18 | 49 | 16.3 | -5.46 | -0.60 | -19.70 | 305 |
| 38 | Max aggression: 1-day momentum | meta | 96.44 | -3.56 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 39 | Supertrend · 1h | trend | 96.32 | -3.69 | 28 | 7.1 | 3.55 | 0.66 | -16.43 | 202 |
| 40 | MACD cross · 1h | trend | 96.31 | -3.69 | 72 | 16.7 | -11.95 | -1.86 | -17.27 | 475 |
| 41 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 42 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.44 | -16.99 | 119 |
| 43 | Copy: Insider buying | copy | 96.13 | -3.87 | 6 | 50.0 | -18.81 | -3.69 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.99 | -4.01 | 41 | 12.2 | -4.68 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.67 | -4.33 | 25 | 20.0 | 20.53 | 2.93 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.54 | -5.46 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 94.29 | -5.71 | 40 | 2.5 | 1.92 | 0.45 | -16.65 | 231 |
| 49 | Bollinger breakout · 1h | breakout | 93.56 | -6.44 | 41 | 22.0 | 6.68 | 1.04 | -12.06 | 296 |
| 50 | VWAP momentum · 1h | momentum | 93.54 | -6.46 | 181 | 23.2 | -38.62 | -6.02 | -39.36 | 1277 |
| 51 | Triple EMA stack · 1h | trend | 93.44 | -6.56 | 50 | 8.0 | -7.77 | -0.74 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.79 | -7.21 | 30 | 6.7 | 3.14 | 0.62 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 92.12 | -7.88 | 69 | 11.6 | -3.09 | -0.22 | -18.47 | 339 |
| 55 | Max aggression: 5-day momentum | meta | 91.59 | -8.41 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 91.34 | -8.66 | 31 | 12.9 | 0.06 | 0.22 | -16.18 | 224 |
| 57 | MACD zero-line · 1h | trend | 91.27 | -8.73 | 39 | 15.4 | -2.90 | -0.17 | -18.32 | 236 |
| 58 | Heikin-Ashi · 1h | trend | 90.92 | -9.07 | 96 | 25.0 | -31.87 | -5.55 | -33.92 | 686 |
| 59 | Three white soldiers | momentum | 90.65 | -9.35 | 78 | 14.1 | -49.69 | -26.13 | -50.01 | 594 |
| 60 | OBV trend · 1h | momentum | 89.75 | -10.25 | 97 | 11.3 | -12.49 | -1.36 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.57 | -11.43 | 24 | 8.3 | -10.82 | -1.26 | -23.19 | 217 |
| 62 | ROC + volume · 1h | momentum | 87.42 | -12.58 | 87 | 14.9 | -9.91 | -1.21 | -23.16 | 419 |
| 63 | RSI(14) reversion | reversion | 86.92 | -13.08 | 183 | 33.9 | -70.38 | -19.59 | -70.45 | 1420 |
| 64 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.90 | -16.94 | -69.90 | 1367 |
| 65 | Donchian 55/20 | breakout | 78.44 | -21.56 | 204 | 16.7 | -68.82 | -15.44 | -69.12 | 1316 |
| 66 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.02 | -18.66 | -63.09 | 1234 |
| 67 | ROC + volume | momentum | 77.90 | -22.10 | 270 | 19.3 | -73.43 | -17.50 | -74.19 | 1666 |
| 68 | EMA 20/50 cross | trend | 77.74 | -22.26 | 222 | 18.0 | -78.94 | -16.52 | -79.01 | 1487 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.38 | -19.76 | -64.38 | 914 |
| 70 | Z-score reversion | reversion | 75.89 | -24.11 | 294 | 28.9 | -84.63 | -25.21 | -84.72 | 2074 |
| 71 | MFI reversion | reversion | 73.50 | -26.50 | 294 | 20.7 | -87.58 | -31.66 | -87.62 | 2109 |
| 72 | Supertrend | trend | 72.30 | -27.70 | 303 | 19.8 | -87.43 | -23.19 | -87.45 | 1952 |
| 73 | AI bee: Bizzy | ai | 69.83 | -30.17 | 516 | 7.9 | — | — | — | — |
| 74 | Keltner breakout | breakout | 69.38 | -30.62 | 301 | 11.6 | -85.79 | -31.73 | -85.81 | 1912 |
| 75 | ADX DI cross | trend | 68.74 | -31.26 | 328 | 9.5 | -89.64 | -39.35 | -89.66 | 2112 |
| 76 | Ichimoku | trend | 67.98 | -32.02 | 275 | 8.0 | -82.68 | -25.45 | -82.87 | 1799 |
| 77 | AI bee: Boozy | ai | 67.26 | -32.74 | 201 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.01 | -33.99 | 382 | 14.9 | -92.04 | -32.59 | -92.05 | 2385 |
| 79 | Donchian 20/10 | breakout | 65.60 | -34.40 | 403 | 17.1 | -91.21 | -27.79 | -91.34 | 2697 |
| 80 | RSI momentum | momentum | 63.94 | -36.06 | 386 | 14.2 | -91.03 | -28.19 | -91.03 | 2417 |
| 81 | Triple EMA stack | trend | 62.79 | -37.21 | 437 | 14.4 | -93.70 | -34.55 | -93.70 | 2670 |
| 82 | Stochastic reversion | reversion | 62.70 | -37.30 | 586 | 22.9 | -95.62 | -39.10 | -95.66 | 4051 |
| 83 | Trend pullback | trend | 62.38 | -37.62 | 406 | 14.0 | -91.82 | -33.56 | -91.82 | 2382 |
| 84 | Bollinger reversion | reversion | 62.34 | -37.66 | 546 | 16.7 | -95.61 | -37.78 | -95.61 | 3688 |
| 85 | Bollinger breakout | breakout | 61.90 | -38.10 | 418 | 13.6 | -94.19 | -37.60 | -94.22 | 2869 |
| 86 | Consensus | meta | 60.06 | -39.94 | 389 | 8.5 | -94.42 | -27.50 | -94.42 | 2645 |
| 87 | EMA 9/21 cross | trend | 58.24 | -41.76 | 545 | 16.1 | -97.57 | -37.69 | -97.58 | 3590 |
| 88 | Connors RSI(2) | reversion | 58.18 | -41.82 | 516 | 15.7 | -96.63 | -37.44 | -96.63 | 3665 |
| 89 | CCI reversion | reversion | 56.79 | -43.21 | 551 | 15.2 | -98.45 | -42.57 | -98.45 | 4716 |
| 90 | Candlestick reversal | reversion | 56.56 | -43.44 | 652 | 14.7 | -99.30 | -42.16 | -99.30 | 5633 |
| 91 | VWAP momentum | momentum | 55.34 | -44.66 | 616 | 8.9 | -98.68 | -33.76 | -98.69 | 5346 |
| 92 | OBV trend | momentum | 55.07 | -44.93 | 611 | 13.9 | -96.48 | -43.65 | -96.50 | 3674 |
| 93 | Parabolic SAR | trend | 53.26 | -46.74 | 560 | 12.7 | -97.43 | -45.95 | -97.43 | 3718 |
| 94 | MACD cross | trend | 51.62 | -48.38 | 637 | 12.7 | -99.73 | -51.17 | -99.73 | 6202 |
| 95 | Williams %R | reversion | 51.52 | -48.48 | 691 | 19.4 | -99.50 | -47.03 | -99.50 | 6141 |
| 96 | Heikin-Ashi | trend | 50.13 | -49.87 | 599 | 8.3 | -99.90 | -58.40 | -99.90 | 8366 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T03:35 | Squeeze breakout · 1h | buy | ETH-USD | 6.83 | — | rebalance up |
| 2026-10-05T03:35 | Squeeze breakout · 1h | sell | BTC-USD | 16.01 | 0.14 | stop-loss |
| 2026-10-05T03:35 | Keltner breakout · 1h | sell | BTC-USD | 6.82 | 0.02 | stop-loss |
| 2026-10-05T03:35 | Bollinger breakout · 1h | sell | BTC-USD | 6.28 | 0.08 | stop-loss |
| 2026-10-05T03:35 | CCI reversion | buy | XRP-USD | 14.22 | — | entry signal |
| 2026-10-05T03:35 | CCI reversion | sell | BTC-USD | 14.18 | -0.09 | stop-loss |
| 2026-10-05T03:35 | Williams %R | sell | BTC-USD | 12.85 | -0.08 | stop-loss |
| 2026-10-05T03:35 | Candlestick reversal | buy | ETH-USD | 2.84 | — | rebalance up |
| 2026-10-05T03:35 | Candlestick reversal | sell | SOL-USD | 11.26 | -0.07 | exit signal |
| 2026-10-05T03:35 | Candlestick reversal | sell | BTC-USD | 11.27 | -0.08 | exit signal |
| 2026-10-05T03:35 | OBV trend | buy | DOGE-USD | 13.78 | — | entry |
| 2026-10-05T03:35 | Trend pullback | buy | DOGE-USD | 15.61 | — | entry |
| 2026-10-05T03:35 | Heikin-Ashi | buy | DOGE-USD | 12.54 | — | entry signal |
| 2026-10-05T03:35 | EMA 20/50 cross | sell | XRP-USD | 19.49 | 0.10 | exit signal |
| 2026-10-05T03:30 | MFI reversion | buy | SOL-USD | 18.39 | — | entry signal |
| 2026-10-05T03:30 | CCI reversion | buy | ETH-USD | 14.24 | — | entry signal |
| 2026-10-05T03:30 | Connors RSI(2) | sell | ETH-USD | 14.49 | -0.09 | exit signal |
| 2026-10-05T03:30 | VWAP momentum | buy | DOGE-USD | 13.84 | — | entry signal |
| 2026-10-05T03:28 | AI bee: Bizzy | buy | DOGE-USD | 10.34 | — | Jev: buy (buy p=0.59) |
| 2026-10-05T03:25 | Consensus | buy | ETH-USD | 15.02 | — | entry |
| 2026-10-05T03:25 | Williams %R | buy | ETH-USD | 12.87 | — | entry signal |
| 2026-10-05T03:25 | Williams %R | sell | XRP-USD | 12.86 | -0.09 | stop-loss |
| 2026-10-05T03:25 | Stochastic reversion | sell | XRP-USD | 15.61 | -0.11 | stop-loss |
| 2026-10-05T03:25 | Candlestick reversal | buy | SOL-USD | 11.33 | — | entry signal |
| 2026-10-05T03:25 | Candlestick reversal | buy | ETH-USD | 11.35 | — | entry signal |
| 2026-10-05T03:25 | Candlestick reversal | buy | BTC-USD | 11.35 | — | entry signal |
| 2026-10-05T03:25 | Candlestick reversal | sell | XRP-USD | 2.84 | -0.02 | rebalance down |
| 2026-10-05T03:25 | Candlestick reversal | sell | DOGE-USD | 2.86 | -0.02 | rebalance down |
| 2026-10-05T03:20 | Consensus | sell | ETH-USD | 15.08 | -0.06 | target is flat |
| 2026-10-05T03:20 | Candlestick reversal | sell | SOL-USD | 14.15 | -0.12 | exit signal |
| 2026-10-05T03:20 | Candlestick reversal | sell | BTC-USD | 14.17 | -0.10 | exit signal |
| 2026-10-05T03:20 | RSI momentum | sell | ETH-USD | 15.95 | -0.10 | exit signal |
| 2026-10-05T03:20 | Trend pullback | sell | ETH-USD | 15.66 | -0.06 | exit signal |
| 2026-10-05T03:20 | Supertrend | sell | DOGE-USD | 17.98 | -0.18 | exit signal |
| 2026-10-05T03:20 | Triple EMA stack | sell | ETH-USD | 15.68 | -0.08 | exit signal |
| 2026-10-05T03:20 | EMA 9/21 cross | sell | ETH-USD | 14.57 | -0.07 | exit signal |
| 2026-10-05T03:15 | CCI reversion | buy | SOL-USD | 14.26 | — | entry signal |
| 2026-10-05T03:15 | CCI reversion | buy | DOGE-USD | 14.26 | — | entry signal |
| 2026-10-05T03:15 | Williams %R | buy | SOL-USD | 12.94 | — | entry signal |
| 2026-10-05T03:15 | Stochastic reversion | buy | DOGE-USD | 15.71 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 03:35:05.000124+00:00 -> 2026-10-05 03:45:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
