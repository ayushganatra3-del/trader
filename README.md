# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T05:05:05.000150+00:00 · 12087 ticks

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

Today: 3930 decisions in 786 calls, $0.0552 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T05:05 | 1 / 2 / 2 | AMZN 18%, COIN 18%, MSTR 17% |  |
| Breezy | 2026-10-05T05:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T05:05 | 0 / 4 / 1 | MSTR 66% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.52 | 2.52 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 2 | Hold BTC | benchmark | 102.52 | 2.52 | 0 | — | 33.64 | 4.06 | -8.68 | 1 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.40 | 2.40 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | Copy: Congress Democrats (NANC) | copy | 101.28 | 1.28 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 5 | VWAP reversion · 1h | reversion | 101.28 | 1.28 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 101.20 | 1.20 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 101.20 | 1.20 | 53 | 37.7 | -24.38 | -5.48 | -26.68 | 497 |
| 8 | RSI(14) reversion · 1h | reversion | 100.70 | 0.70 | 11 | 63.6 | 3.74 | 1.09 | -6.57 | 122 |
| 9 | Hold SPY | benchmark | 100.43 | 0.43 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Bollinger reversion · 1h | reversion | 100.07 | 0.07 | 41 | 43.9 | -14.79 | -3.91 | -17.51 | 304 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 100.03 | 0.03 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 12 | Z-score reversion · 1h | reversion | 100.02 | 0.02 | 20 | 55.0 | 5.72 | 1.30 | -8.60 | 159 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Donchian 55/20 · 1h | breakout | 99.99 | -0.01 | 17 | 0.0 | 6.03 | 0.96 | -16.96 | 116 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.95 | -0.06 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 18 | Daily: Bullish score | daily | 99.80 | -0.20 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 22 | CCI reversion · 1h | reversion | 99.22 | -0.78 | 63 | 49.2 | 1.92 | 0.48 | -12.41 | 411 |
| 23 | Stochastic reversion · 1h | reversion | 99.20 | -0.80 | 45 | 60.0 | -8.12 | -1.66 | -9.82 | 328 |
| 24 | Trend pullback · 1h | trend | 99.11 | -0.89 | 50 | 22.0 | -21.37 | -5.43 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 99.06 | -0.94 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | EMA 20/50 cross · 1h | trend | 98.11 | -1.89 | 25 | 8.0 | 13.58 | 1.69 | -14.40 | 137 |
| 30 | Daily: SMA 20/50 cross · AAPL | daily | 98.09 | -1.91 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 31 | Agent (rotation) | meta | 97.99 | -2.01 | 52 | 23.1 | -4.27 | -1.61 | -9.74 | 228 |
| 32 | Williams %R · 1h | reversion | 97.79 | -2.21 | 70 | 54.3 | -17.20 | -3.14 | -19.41 | 496 |
| 33 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 34 | Connors RSI(2) · 1h | reversion | 97.51 | -2.49 | 60 | 43.3 | -12.34 | -4.14 | -14.31 | 225 |
| 35 | Daily: Momentum burst | daily | 97.06 | -2.94 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.97 | -3.04 | 208 | 17.3 | 1.51 | 0.42 | -11.18 | 357 |
| 37 | Parabolic SAR · 1h | trend | 96.62 | -3.38 | 53 | 17.0 | -5.45 | -0.60 | -19.70 | 304 |
| 38 | Max aggression: 1-day momentum | meta | 96.44 | -3.56 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 39 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 40 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.44 | -16.99 | 119 |
| 41 | Supertrend · 1h | trend | 96.16 | -3.84 | 29 | 10.3 | 3.29 | 0.62 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 96.14 | -3.86 | 6 | 50.0 | -19.54 | -3.87 | -21.08 | 70 |
| 43 | MACD cross · 1h | trend | 96.01 | -3.99 | 76 | 19.7 | -11.65 | -1.81 | -17.27 | 472 |
| 44 | ADX DI cross · 1h | trend | 95.99 | -4.01 | 41 | 12.2 | -4.78 | -0.64 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.52 | -4.49 | 26 | 19.2 | 20.30 | 2.90 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.54 | -5.46 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 94.26 | -5.74 | 41 | 2.4 | 1.52 | 0.40 | -16.65 | 231 |
| 49 | Bollinger breakout · 1h | breakout | 93.48 | -6.52 | 43 | 25.6 | 6.56 | 1.02 | -12.06 | 296 |
| 50 | Triple EMA stack · 1h | trend | 93.42 | -6.58 | 51 | 9.8 | -7.92 | -0.76 | -23.88 | 244 |
| 51 | VWAP momentum · 1h | momentum | 93.38 | -6.62 | 182 | 23.1 | -38.49 | -6.00 | -39.03 | 1275 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.79 | -7.21 | 30 | 6.7 | 2.82 | 0.57 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 92.00 | -8.00 | 70 | 12.9 | -3.32 | -0.26 | -18.47 | 339 |
| 55 | Max aggression: 5-day momentum | meta | 91.59 | -8.41 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | MACD zero-line · 1h | trend | 91.10 | -8.90 | 42 | 16.7 | -3.33 | -0.22 | -18.32 | 236 |
| 57 | Donchian 20/10 · 1h | breakout | 91.07 | -8.93 | 32 | 15.6 | -0.23 | 0.18 | -16.18 | 224 |
| 58 | Three white soldiers | momentum | 90.65 | -9.35 | 78 | 14.1 | -49.69 | -26.13 | -50.01 | 594 |
| 59 | Heikin-Ashi · 1h | trend | 90.64 | -9.36 | 98 | 25.5 | -32.08 | -5.60 | -33.92 | 686 |
| 60 | OBV trend · 1h | momentum | 89.75 | -10.25 | 97 | 11.3 | -12.93 | -1.42 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.41 | -11.59 | 27 | 7.4 | -11.04 | -1.29 | -23.22 | 217 |
| 62 | ROC + volume · 1h | momentum | 87.27 | -12.73 | 90 | 15.6 | -10.10 | -1.24 | -23.17 | 419 |
| 63 | RSI(14) reversion | reversion | 86.15 | -13.85 | 185 | 33.5 | -70.85 | -20.03 | -70.91 | 1430 |
| 64 | VWAP reversion | reversion | 78.53 | -21.47 | 217 | 28.1 | -70.25 | -17.18 | -70.25 | 1374 |
| 65 | Donchian 55/20 | breakout | 78.44 | -21.56 | 204 | 16.7 | -68.82 | -15.44 | -69.12 | 1316 |
| 66 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.04 | -18.66 | -63.10 | 1234 |
| 67 | ROC + volume | momentum | 77.90 | -22.10 | 270 | 19.3 | -73.43 | -17.50 | -74.19 | 1666 |
| 68 | EMA 20/50 cross | trend | 77.45 | -22.55 | 224 | 18.3 | -79.07 | -16.61 | -79.07 | 1488 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.38 | -19.76 | -64.38 | 914 |
| 70 | Z-score reversion | reversion | 75.03 | -24.97 | 296 | 28.7 | -84.80 | -25.59 | -84.88 | 2080 |
| 71 | MFI reversion | reversion | 72.74 | -27.26 | 296 | 20.6 | -87.70 | -32.15 | -87.75 | 2114 |
| 72 | Supertrend | trend | 72.22 | -27.78 | 304 | 20.1 | -87.44 | -23.22 | -87.46 | 1952 |
| 73 | AI bee: Bizzy | ai | 69.71 | -30.29 | 518 | 7.9 | — | — | — | — |
| 74 | Keltner breakout | breakout | 69.38 | -30.62 | 301 | 11.6 | -85.79 | -31.73 | -85.81 | 1912 |
| 75 | ADX DI cross | trend | 68.74 | -31.26 | 328 | 9.5 | -89.64 | -39.32 | -89.65 | 2112 |
| 76 | Ichimoku | trend | 67.98 | -32.02 | 275 | 8.0 | -82.71 | -25.50 | -82.87 | 1801 |
| 77 | AI bee: Boozy | ai | 67.26 | -32.74 | 201 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.01 | -33.99 | 382 | 14.9 | -92.04 | -32.59 | -92.05 | 2385 |
| 79 | Donchian 20/10 | breakout | 65.60 | -34.40 | 403 | 17.1 | -91.21 | -27.79 | -91.34 | 2697 |
| 80 | RSI momentum | momentum | 63.94 | -36.06 | 386 | 14.2 | -90.99 | -28.13 | -90.99 | 2415 |
| 81 | Triple EMA stack | trend | 62.79 | -37.21 | 437 | 14.4 | -93.71 | -34.55 | -93.71 | 2670 |
| 82 | Trend pullback | trend | 62.31 | -37.69 | 407 | 14.0 | -91.67 | -32.99 | -91.67 | 2372 |
| 83 | Bollinger breakout | breakout | 61.90 | -38.10 | 418 | 13.6 | -94.19 | -37.60 | -94.22 | 2869 |
| 84 | Stochastic reversion | reversion | 61.70 | -38.30 | 592 | 22.6 | -95.65 | -39.73 | -95.68 | 4052 |
| 85 | Bollinger reversion | reversion | 61.00 | -39.00 | 553 | 16.5 | -95.70 | -38.73 | -95.70 | 3698 |
| 86 | Consensus | meta | 59.96 | -40.04 | 390 | 8.5 | -94.40 | -27.41 | -94.40 | 2642 |
| 87 | EMA 9/21 cross | trend | 58.24 | -41.76 | 545 | 16.1 | -97.57 | -37.68 | -97.58 | 3589 |
| 88 | Connors RSI(2) | reversion | 57.52 | -42.48 | 521 | 15.5 | -96.65 | -37.57 | -96.65 | 3665 |
| 89 | CCI reversion | reversion | 56.13 | -43.87 | 555 | 15.1 | -98.46 | -42.93 | -98.46 | 4717 |
| 90 | Candlestick reversal | reversion | 55.68 | -44.33 | 660 | 14.5 | -99.31 | -42.77 | -99.31 | 5640 |
| 91 | VWAP momentum | momentum | 55.29 | -44.71 | 617 | 8.9 | -98.69 | -33.78 | -98.69 | 5344 |
| 92 | OBV trend | momentum | 54.94 | -45.06 | 613 | 13.9 | -96.49 | -43.75 | -96.51 | 3674 |
| 93 | Parabolic SAR | trend | 53.26 | -46.74 | 560 | 12.7 | -97.43 | -45.95 | -97.43 | 3718 |
| 94 | MACD cross | trend | 51.45 | -48.55 | 638 | 12.7 | -99.73 | -51.30 | -99.73 | 6198 |
| 95 | Williams %R | reversion | 50.62 | -49.38 | 698 | 19.2 | -99.51 | -47.70 | -99.51 | 6145 |
| 96 | Heikin-Ashi | trend | 50.07 | -49.93 | 600 | 8.3 | -99.90 | -58.31 | -99.90 | 8362 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T05:05 | Candlestick reversal | sell | SOL-USD | 13.93 | -0.09 | exit signal |
| 2026-10-05T05:00 | Stochastic reversion · 1h | buy | SOL-USD | 14.18 | — | entry signal |
| 2026-10-05T05:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 5.41 | — | entry signal |
| 2026-10-05T05:00 | Connors RSI(2) · 1h | sell | BTC-USD | 5.41 | -0.07 | rebalance down |
| 2026-10-05T05:00 | Parabolic SAR · 1h | sell | XRP-USD | 6.39 | -0.04 | exit signal |
| 2026-10-05T05:00 | Parabolic SAR · 1h | sell | ETH-USD | 6.41 | -0.02 | exit signal |
| 2026-10-05T05:00 | Supertrend · 1h | buy | DOGE-USD | 5.06 | — | entry |
| 2026-10-05T05:00 | Supertrend · 1h | sell | BTC-USD | 5.33 | 0.00 | exit signal |
| 2026-10-05T05:00 | MACD zero-line · 1h | sell | ETH-USD | 3.11 | 0.00 | exit signal |
| 2026-10-05T05:00 | MACD zero-line · 1h | sell | DOGE-USD | 2.56 | -0.01 | exit signal |
| 2026-10-05T05:00 | MACD zero-line · 1h | sell | BTC-USD | 7.56 | -0.01 | exit signal |
| 2026-10-05T05:00 | MACD cross · 1h | sell | XRP-USD | 5.23 | 0.06 | exit signal |
| 2026-10-05T05:00 | MACD cross · 1h | sell | ETH-USD | 6.40 | 0.04 | exit signal |
| 2026-10-05T05:00 | MACD cross · 1h | sell | DOGE-USD | 6.50 | 0.14 | exit signal |
| 2026-10-05T05:00 | MACD cross · 1h | sell | BTC-USD | 5.98 | -0.01 | exit signal |
| 2026-10-05T05:00 | Triple EMA stack · 1h | buy | BTC-USD | 2.78 | — | entry |
| 2026-10-05T05:00 | Triple EMA stack · 1h | sell | SOL-USD | 2.78 | 0.01 | exit signal |
| 2026-10-05T05:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 4.84 | — | entry |
| 2026-10-05T05:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 5.75 | 0.02 | exit signal |
| 2026-10-05T04:50 | MFI reversion | buy | XRP-USD | 18.20 | — | entry signal |
| 2026-10-05T04:50 | MFI reversion | buy | DOGE-USD | 18.25 | — | entry signal |
| 2026-10-05T04:50 | CCI reversion | buy | XRP-USD | 14.09 | — | entry signal |
| 2026-10-05T04:50 | CCI reversion | buy | ETH-USD | 14.09 | — | entry signal |
| 2026-10-05T04:50 | CCI reversion | buy | DOGE-USD | 14.09 | — | entry signal |
| 2026-10-05T04:50 | Williams %R | buy | ETH-USD | 12.67 | — | entry signal |
| 2026-10-05T04:50 | Z-score reversion | buy | XRP-USD | 18.75 | — | entry signal |
| 2026-10-05T04:50 | Z-score reversion | buy | ETH-USD | 18.84 | — | entry signal |
| 2026-10-05T04:50 | Z-score reversion | buy | DOGE-USD | 18.84 | — | entry signal |
| 2026-10-05T04:50 | MACD cross | buy | SOL-USD | 12.88 | — | entry signal |
| 2026-10-05T04:47 | VWAP reversion | sell | SOL-USD | 3.94 | -0.03 | rebalance down |
| 2026-10-05T04:45 | Williams %R | buy | XRP-USD | 12.69 | — | entry signal |
| 2026-10-05T04:45 | Williams %R | buy | DOGE-USD | 12.69 | — | entry signal |
| 2026-10-05T04:45 | Stochastic reversion | buy | ETH-USD | 15.46 | — | entry signal |
| 2026-10-05T04:45 | Stochastic reversion | buy | BTC-USD | 15.46 | — | entry signal |
| 2026-10-05T04:45 | VWAP reversion | buy | XRP-USD | 11.83 | — | entry signal |
| 2026-10-05T04:45 | VWAP reversion | buy | ETH-USD | 15.75 | — | entry signal |
| 2026-10-05T04:45 | VWAP reversion | buy | DOGE-USD | 15.75 | — | entry signal |
| 2026-10-05T04:45 | VWAP reversion | buy | BTC-USD | 15.75 | — | entry signal |
| 2026-10-05T04:45 | Bollinger reversion | buy | XRP-USD | 15.30 | — | entry signal |
| 2026-10-05T04:45 | Bollinger reversion | buy | DOGE-USD | 15.30 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 05:05:05.000150+00:00 -> 2026-10-05 05:15:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
