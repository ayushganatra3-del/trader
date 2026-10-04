# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T10:35:05.000155+00:00 · 11145 ticks

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
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, ETRA 12%, BBD 12%, BPRE 12%, GME 12%, NYAX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 7874 decisions in 1576 calls, $0.1100 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T10:35 | 0 / 1 / 4 | BTC-USD 15%, AMZN 17%, COIN 17%, MSTR 16% |  |
| Breezy | 2026-10-04T10:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T10:35 | 2 / 2 / 1 | BTC-USD 35% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.27 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 101.99 | 1.99 | 0 | — | 35.77 | 4.34 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -24.43 | -5.61 | -26.72 | 501 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 4.55 | 1.32 | -6.57 | 119 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.82 | -3.95 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.83 | -0.17 | 19 | 57.9 | 5.74 | 1.32 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 5.70 | 0.93 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.36 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.02 | -0.98 | 45 | 60.0 | -8.07 | -1.66 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.55 | 0.42 | -12.41 | 416 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 46 | 19.6 | -22.54 | -5.79 | -25.84 | 161 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.93 | -2.07 | 51 | 21.6 | -3.86 | -1.45 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.47 | 1.69 | -14.40 | 135 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.62 | -2.38 | 58 | 44.8 | -11.63 | -3.91 | -14.21 | 220 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.14 | -3.16 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 0.58 | 0.25 | -12.16 | 375 |
| 37 | Parabolic SAR · 1h | trend | 96.46 | -3.54 | 47 | 17.0 | -6.15 | -0.70 | -19.70 | 305 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.84 | 2.87 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.16 | -1.38 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.91 | -4.09 | 28 | 7.1 | 3.34 | 0.63 | -16.43 | 199 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.60 | -0.62 | -13.84 | 267 |
| 44 | MACD cross · 1h | trend | 95.66 | -4.34 | 71 | 15.5 | -11.46 | -1.80 | -17.27 | 473 |
| 45 | Squeeze breakout · 1h | breakout | 95.24 | -4.76 | 22 | 18.2 | 19.93 | 2.87 | -8.06 | 115 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.02 | 40 | 2.5 | 1.59 | 0.41 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.24 | -6.76 | 178 | 21.9 | -40.55 | -6.41 | -40.97 | 1287 |
| 50 | Triple EMA stack · 1h | trend | 93.14 | -6.86 | 50 | 8.0 | -8.39 | -0.83 | -23.88 | 244 |
| 51 | Bollinger breakout · 1h | breakout | 93.08 | -6.92 | 38 | 15.8 | 6.22 | 0.99 | -12.06 | 297 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.24 | -4.58 | -18.91 | 695 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.04 | 0.61 | -12.60 | 127 |
| 54 | EMA 9/21 cross · 1h | trend | 91.77 | -8.23 | 69 | 11.6 | -4.26 | -0.39 | -18.47 | 342 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | Three white soldiers | momentum | 91.14 | -8.86 | 75 | 14.7 | -49.48 | -26.29 | -49.74 | 592 |
| 57 | MACD zero-line · 1h | trend | 90.91 | -9.10 | 38 | 13.2 | -3.28 | -0.22 | -18.32 | 235 |
| 58 | Donchian 20/10 · 1h | breakout | 90.71 | -9.29 | 31 | 12.9 | -0.11 | 0.20 | -16.18 | 224 |
| 59 | Heikin-Ashi · 1h | trend | 90.50 | -9.51 | 91 | 24.2 | -32.54 | -5.75 | -33.88 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.35 | -1.35 | -26.45 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.02 | -1.30 | -23.19 | 212 |
| 62 | ROC + volume · 1h | momentum | 87.13 | -12.87 | 84 | 14.3 | -10.42 | -1.30 | -23.16 | 417 |
| 63 | RSI(14) reversion | reversion | 86.96 | -13.04 | 182 | 34.1 | -70.74 | -20.26 | -70.78 | 1431 |
| 64 | Donchian 55/20 | breakout | 79.73 | -20.27 | 189 | 16.9 | -68.89 | -15.66 | -68.91 | 1312 |
| 65 | ROC + volume | momentum | 79.45 | -20.55 | 260 | 20.0 | -73.36 | -17.66 | -73.97 | 1667 |
| 66 | Squeeze breakout | breakout | 79.39 | -20.61 | 199 | 14.1 | -61.69 | -19.02 | -62.58 | 1226 |
| 67 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.76 | -17.10 | -69.76 | 1360 |
| 68 | Volume breakout | breakout | 77.88 | -22.12 | 172 | 12.8 | -64.40 | -20.29 | -64.40 | 914 |
| 69 | EMA 20/50 cross | trend | 77.78 | -22.22 | 213 | 16.9 | -79.11 | -16.79 | -79.24 | 1486 |
| 70 | Z-score reversion | reversion | 76.11 | -23.89 | 291 | 29.2 | -85.07 | -26.68 | -85.09 | 2090 |
| 71 | MFI reversion | reversion | 74.08 | -25.91 | 286 | 21.0 | -87.71 | -32.89 | -87.76 | 2110 |
| 72 | Supertrend | trend | 72.63 | -27.37 | 291 | 19.2 | -87.41 | -23.45 | -87.57 | 1953 |
| 73 | AI bee: Bizzy | ai | 72.53 | -27.47 | 478 | 8.6 | — | — | — | — |
| 74 | Keltner breakout | breakout | 71.87 | -28.13 | 277 | 12.3 | -85.70 | -33.28 | -85.70 | 1911 |
| 75 | Ichimoku | trend | 70.76 | -29.24 | 249 | 8.4 | -82.53 | -26.60 | -82.53 | 1794 |
| 76 | ADX DI cross | trend | 69.88 | -30.12 | 318 | 9.7 | -89.57 | -40.32 | -89.57 | 2109 |
| 77 | AI bee: Boozy | ai | 68.89 | -31.11 | 190 | 4.2 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 67.80 | -32.20 | 381 | 17.6 | -91.24 | -28.81 | -91.24 | 2702 |
| 79 | MACD zero-line | trend | 67.53 | -32.47 | 369 | 15.4 | -91.99 | -33.26 | -91.99 | 2383 |
| 80 | Trend pullback | trend | 66.33 | -33.67 | 361 | 15.0 | -91.75 | -33.15 | -91.76 | 2371 |
| 81 | RSI momentum | momentum | 65.93 | -34.07 | 361 | 14.7 | -91.07 | -28.60 | -91.08 | 2416 |
| 82 | Triple EMA stack | trend | 65.38 | -34.62 | 405 | 14.8 | -93.74 | -35.07 | -93.74 | 2671 |
| 83 | Stochastic reversion | reversion | 64.48 | -35.52 | 561 | 23.9 | -95.63 | -40.57 | -95.65 | 4052 |
| 84 | Bollinger breakout | breakout | 64.20 | -35.80 | 395 | 14.2 | -94.20 | -39.78 | -94.20 | 2874 |
| 85 | Consensus | meta | 63.76 | -36.24 | 349 | 8.9 | -94.15 | -27.74 | -94.16 | 2614 |
| 86 | Bollinger reversion | reversion | 63.31 | -36.69 | 533 | 17.1 | -95.67 | -39.76 | -95.67 | 3696 |
| 87 | Connors RSI(2) | reversion | 61.09 | -38.91 | 476 | 17.0 | -96.57 | -38.72 | -96.57 | 3649 |
| 88 | EMA 9/21 cross | trend | 60.72 | -39.28 | 511 | 16.6 | -97.53 | -38.07 | -97.55 | 3586 |
| 89 | Candlestick reversal | reversion | 58.89 | -41.11 | 623 | 15.2 | -99.29 | -43.53 | -99.29 | 5630 |
| 90 | CCI reversion | reversion | 58.78 | -41.22 | 528 | 15.9 | -98.46 | -44.79 | -98.46 | 4724 |
| 91 | OBV trend | momentum | 58.78 | -41.22 | 567 | 14.1 | -96.42 | -44.80 | -96.42 | 3663 |
| 92 | VWAP momentum | momentum | 56.79 | -43.21 | 590 | 8.5 | -98.72 | -34.92 | -98.72 | 5361 |
| 93 | Parabolic SAR | trend | 54.90 | -45.10 | 541 | 13.1 | -97.37 | -49.74 | -97.37 | 3703 |
| 94 | Williams %R | reversion | 54.08 | -45.92 | 653 | 20.5 | -99.50 | -49.53 | -99.50 | 6138 |
| 95 | MACD cross | trend | 52.83 | -47.17 | 622 | 13.0 | -99.73 | -54.46 | -99.73 | 6186 |
| 96 | Heikin-Ashi | trend | 51.61 | -48.39 | 583 | 8.6 | -99.90 | -64.63 | -99.90 | 8369 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T10:35 | Volume breakout | sell | ETH-USD | 19.36 | -0.14 | exit signal |
| 2026-10-04T10:35 | Heikin-Ashi | sell | ETH-USD | 12.86 | -0.09 | exit signal |
| 2026-10-04T10:35 | Parabolic SAR | sell | SOL-USD | 10.97 | -0.06 | exit signal |
| 2026-10-04T10:35 | MACD zero-line | sell | SOL-USD | 16.81 | -0.10 | exit signal |
| 2026-10-04T10:35 | MACD cross | sell | SOL-USD | 10.61 | -0.06 | exit signal |
| 2026-10-04T10:33 | AI bee: Boozy | buy | BTC-USD | 24.40 | — | Jev: buy (buy p=0.71) |
| 2026-10-04T10:33 | AI bee: Boozy | sell | ETH-USD | 24.40 | -0.15 | Jev: sell |
| 2026-10-04T10:32 | AI bee: Bizzy | buy | BTC-USD | 11.16 | — | Jev: buy (buy p=0.62) |
| 2026-10-04T10:31 | Connors RSI(2) | buy | XRP-USD | 15.30 | — | entry signal |
| 2026-10-04T10:31 | Connors RSI(2) | buy | SOL-USD | 15.30 | — | entry signal |
| 2026-10-04T10:31 | Keltner breakout | buy | ETH-USD | 14.32 | — | rebalance up |
| 2026-10-04T10:31 | Keltner breakout | sell | SOL-USD | 17.89 | -0.14 | exit signal |
| 2026-10-04T10:31 | Keltner breakout | sell | DOGE-USD | 17.95 | -0.13 | exit signal |
| 2026-10-04T10:31 | OBV trend | buy | XRP-USD | 5.86 | — | rebalance up |
| 2026-10-04T10:31 | OBV trend | sell | SOL-USD | 11.71 | -0.07 | exit signal |
| 2026-10-04T10:31 | Heikin-Ashi | sell | SOL-USD | 12.89 | -0.09 | exit signal |
| 2026-10-04T10:31 | Parabolic SAR | buy | ETH-USD | 2.78 | — | rebalance up |
| 2026-10-04T10:31 | Parabolic SAR | sell | DOGE-USD | 10.96 | -0.08 | exit signal |
| 2026-10-04T10:31 | MACD cross | sell | XRP-USD | 10.60 | -0.06 | exit signal |
| 2026-10-04T10:25 | Heikin-Ashi | buy | ETH-USD | 12.95 | — | entry signal |
| 2026-10-04T10:25 | Heikin-Ashi | buy | BTC-USD | 12.95 | — | entry signal |
| 2026-10-04T10:25 | MACD cross | buy | ETH-USD | 2.76 | — | rebalance up |
| 2026-10-04T10:25 | MACD cross | buy | BTC-USD | 2.66 | — | rebalance up |
| 2026-10-04T10:25 | MACD cross | sell | DOGE-USD | 10.59 | -0.08 | exit signal |
| 2026-10-04T10:20 | Volume breakout | buy | ETH-USD | 19.50 | — | entry signal |
| 2026-10-04T10:20 | Keltner breakout | buy | ETH-USD | 3.70 | — | entry signal |
| 2026-10-04T10:20 | Keltner breakout | sell | BTC-USD | 3.63 | -0.01 | rebalance down |
| 2026-10-04T10:20 | Donchian 20/10 | buy | ETH-USD | 16.97 | — | entry signal |
| 2026-10-04T10:20 | MACD cross | buy | ETH-USD | 10.52 | — | entry |
| 2026-10-04T10:20 | MACD cross | buy | BTC-USD | 10.61 | — | entry signal |
| 2026-10-04T10:17 | AI bee: Boozy | buy | ETH-USD | 24.56 | — | Jev: buy (buy p=0.66) |
| 2026-10-04T10:15 | MACD cross | sell | BTC-USD | 10.61 | -0.06 | exit signal |
| 2026-10-04T10:13 | AI bee: Bizzy | sell | DOGE-USD | 10.78 | -0.09 | Jev: sell (sell p=0.88) after 10 min |
| 2026-10-04T10:05 | MACD cross | sell | ETH-USD | 10.52 | -0.07 | exit signal |
| 2026-10-04T10:03 | AI bee: Bizzy | buy | DOGE-USD | 10.88 | — | Jev: buy (buy p=0.60) |
| 2026-10-04T10:00 | Ichimoku | sell | ETH-USD | 17.69 | -0.11 | exit signal |
| 2026-10-04T10:00 | Parabolic SAR | buy | ETH-USD | 2.74 | — | rebalance up |
| 2026-10-04T10:00 | Parabolic SAR | sell | DOGE-USD | 2.74 | -0.02 | rebalance down |
| 2026-10-04T09:59 | AI bee: Bizzy | sell | SOL-USD | 10.55 | -0.06 | Jev: sell (sell p=0.51) after 12 min |
| 2026-10-04T09:57 | AI bee: Boozy | sell | BTC-USD | 24.56 | -0.16 | Jev: buy |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
