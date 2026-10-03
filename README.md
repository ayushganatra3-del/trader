# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T23:05:05.000116+00:00 · 10572 ticks

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

Today: 17322 decisions in 3465 calls, $0.2422 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T23:05 | 0 / 1 / 4 | AMZN 17%, COIN 16%, MSTR 16% |  |
| Breezy | 2026-10-03T23:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T23:05 | 0 / 2 / 3 | MSTR 62% |  |

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
| 3 | Hold BTC | benchmark | 101.32 | 1.32 | 0 | — | 33.34 | 4.09 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.00 | -2.92 | -14.05 | 113 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -24.46 | -5.62 | -26.75 | 501 |
| 8 | RSI(14) reversion · 1h | reversion | 100.52 | 0.53 | 10 | 60.0 | 3.43 | 1.02 | -6.57 | 122 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.80 | -3.94 | -17.52 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.69 | -0.31 | 18 | 55.6 | 5.52 | 1.27 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 5.99 | 0.96 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 98.98 | -1.02 | 44 | 59.1 | -8.12 | -1.68 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.48 | 0.41 | -12.41 | 416 |
| 24 | Trend pullback · 1h | trend | 98.78 | -1.22 | 46 | 19.6 | -22.03 | -5.63 | -25.84 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.86 | -2.14 | 50 | 20.0 | -4.84 | -1.85 | -9.74 | 234 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.63 | 1.71 | -14.40 | 133 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.69 | -2.31 | 57 | 45.6 | -11.66 | -3.93 | -14.21 | 222 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.18 | -3.17 | -19.41 | 496 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 5.92 | 1.20 | -12.17 | 365 |
| 37 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -6.16 | -0.70 | -19.70 | 304 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.84 | 2.87 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.06 | -1.36 | -16.99 | 122 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 3.38 | 0.64 | -16.43 | 197 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.87 | -3.78 | -21.08 | 69 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -6.16 | -0.88 | -13.84 | 275 |
| 44 | MACD cross · 1h | trend | 95.45 | -4.55 | 71 | 15.5 | -14.03 | -2.25 | -17.27 | 484 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.61 | 0.41 | -16.65 | 227 |
| 49 | Triple EMA stack · 1h | trend | 93.10 | -6.90 | 50 | 8.0 | -7.74 | -0.74 | -23.88 | 241 |
| 50 | Bollinger breakout · 1h | breakout | 93.04 | -6.96 | 38 | 15.8 | 6.24 | 0.99 | -12.06 | 292 |
| 51 | VWAP momentum · 1h | momentum | 93.02 | -6.98 | 177 | 22.0 | -41.24 | -6.52 | -41.92 | 1287 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.24 | -4.58 | -18.91 | 695 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.04 | 0.61 | -12.60 | 127 |
| 54 | EMA 9/21 cross · 1h | trend | 91.65 | -8.35 | 69 | 11.6 | -4.03 | -0.36 | -18.47 | 340 |
| 55 | Three white soldiers | momentum | 91.29 | -8.71 | 74 | 14.9 | -49.54 | -26.28 | -49.65 | 594 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | MACD zero-line · 1h | trend | 90.77 | -9.23 | 38 | 13.2 | -3.98 | -0.31 | -18.32 | 234 |
| 58 | Donchian 20/10 · 1h | breakout | 90.52 | -9.48 | 31 | 12.9 | -0.30 | 0.18 | -16.18 | 223 |
| 59 | Heikin-Ashi · 1h | trend | 90.51 | -9.49 | 91 | 24.2 | -33.10 | -5.88 | -33.67 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.77 | -1.41 | -26.45 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.02 | -1.30 | -23.19 | 212 |
| 62 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -10.95 | -1.38 | -23.16 | 417 |
| 63 | RSI(14) reversion | reversion | 86.96 | -13.04 | 182 | 34.1 | -72.15 | -20.52 | -72.15 | 1455 |
| 64 | Squeeze breakout | breakout | 81.07 | -18.93 | 187 | 15.0 | -60.94 | -18.53 | -61.81 | 1215 |
| 65 | Donchian 55/20 | breakout | 80.42 | -19.58 | 184 | 17.4 | -68.62 | -15.50 | -68.68 | 1309 |
| 66 | ROC + volume | momentum | 79.60 | -20.40 | 259 | 20.1 | -73.37 | -17.66 | -73.91 | 1667 |
| 67 | VWAP reversion | reversion | 79.43 | -20.57 | 213 | 28.6 | -71.28 | -17.33 | -71.35 | 1386 |
| 68 | Volume breakout | breakout | 78.97 | -21.03 | 164 | 13.4 | -64.00 | -19.92 | -64.00 | 908 |
| 69 | EMA 20/50 cross | trend | 77.54 | -22.46 | 212 | 17.0 | -79.27 | -16.93 | -79.37 | 1490 |
| 70 | Z-score reversion | reversion | 76.27 | -23.73 | 288 | 29.5 | -85.54 | -27.02 | -85.54 | 2107 |
| 71 | AI bee: Bizzy | ai | 74.53 | -25.47 | 450 | 9.1 | — | — | — | — |
| 72 | MFI reversion | reversion | 74.25 | -25.75 | 282 | 21.3 | -88.04 | -33.41 | -88.04 | 2124 |
| 73 | Keltner breakout | breakout | 74.13 | -25.87 | 261 | 13.0 | -85.43 | -32.33 | -85.43 | 1899 |
| 74 | Supertrend | trend | 72.79 | -27.21 | 287 | 19.5 | -87.48 | -23.63 | -87.53 | 1953 |
| 75 | Ichimoku | trend | 72.71 | -27.29 | 232 | 9.1 | -82.11 | -25.93 | -82.11 | 1779 |
| 76 | AI bee: Boozy ⏸ | ai | 72.08 | -27.92 | 170 | 4.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 70.15 | -29.85 | 315 | 9.8 | -89.72 | -40.91 | -89.72 | 2114 |
| 78 | Donchian 20/10 | breakout | 68.87 | -31.13 | 370 | 18.1 | -91.14 | -28.40 | -91.14 | 2693 |
| 79 | MACD zero-line | trend | 68.57 | -31.43 | 359 | 15.9 | -91.89 | -32.72 | -91.89 | 2381 |
| 80 | Trend pullback | trend | 67.75 | -32.26 | 345 | 15.7 | -91.78 | -33.30 | -91.78 | 2363 |
| 81 | Bollinger breakout | breakout | 66.57 | -33.44 | 373 | 15.0 | -94.03 | -38.32 | -94.03 | 2853 |
| 82 | RSI momentum | momentum | 66.54 | -33.46 | 354 | 14.7 | -90.99 | -28.24 | -90.99 | 2412 |
| 83 | Triple EMA stack ⏸ | trend | 66.28 | -33.72 | 395 | 14.9 | -93.57 | -34.10 | -93.62 | 2657 |
| 84 | Stochastic reversion | reversion | 65.16 | -34.84 | 551 | 24.3 | -95.80 | -40.78 | -95.80 | 4067 |
| 85 | Consensus | meta | 65.02 | -34.98 | 337 | 9.2 | -94.20 | -28.10 | -94.20 | 2614 |
| 86 | Bollinger reversion | reversion | 63.75 | -36.24 | 527 | 17.3 | -95.84 | -40.10 | -95.84 | 3720 |
| 87 | Connors RSI(2) | reversion | 62.67 | -37.33 | 458 | 17.7 | -96.66 | -39.09 | -96.66 | 3665 |
| 88 | EMA 9/21 cross ⏸ | trend | 61.38 | -38.62 | 501 | 16.8 | -97.53 | -37.94 | -97.53 | 3580 |
| 89 | OBV trend ⏸ | momentum | 59.92 | -40.08 | 553 | 14.5 | -96.34 | -43.28 | -96.34 | 3649 |
| 90 | Candlestick reversal ⏸ | reversion | 59.72 | -40.28 | 611 | 15.5 | -99.35 | -43.87 | -99.35 | 5672 |
| 91 | CCI reversion | reversion | 59.67 | -40.33 | 515 | 16.3 | -98.52 | -44.47 | -98.52 | 4737 |
| 92 | VWAP momentum ⏸ | momentum | 58.87 | -41.13 | 563 | 8.9 | -98.66 | -33.92 | -98.66 | 5328 |
| 93 | Parabolic SAR ⏸ | trend | 57.56 | -42.44 | 513 | 13.8 | -97.27 | -47.34 | -97.27 | 3684 |
| 94 | MACD cross ⏸ | trend | 55.83 | -44.17 | 586 | 13.8 | -99.72 | -52.79 | -99.72 | 6180 |
| 95 | Williams %R ⏸ | reversion | 55.60 | -44.41 | 630 | 21.3 | -99.52 | -48.85 | -99.52 | 6155 |
| 96 | Heikin-Ashi ⏸ | trend | 54.73 | -45.27 | 544 | 9.2 | -99.90 | -60.45 | -99.90 | 8346 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T23:05 | Donchian 20/10 | sell | ETH-USD | 17.14 | -0.12 | exit signal |
| 2026-10-03T23:05 | RSI momentum | sell | ETH-USD | 16.55 | -0.12 | exit signal |
| 2026-10-03T23:05 | Trend pullback | sell | ETH-USD | 16.86 | -0.10 | exit signal |
| 2026-10-03T23:05 | Ichimoku | sell | ETH-USD | 18.08 | -0.13 | exit signal |
| 2026-10-03T23:05 | MACD zero-line | sell | SOL-USD | 17.06 | -0.13 | exit signal |
| 2026-10-03T23:05 | EMA 20/50 cross | sell | SOL-USD | 19.28 | -0.15 | exit signal |
| 2026-10-03T23:00 | Trend pullback · 1h | buy | SOL-USD | 3.25 | — | entry signal |
| 2026-10-03T23:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.39 | — | entry signal |
| 2026-10-03T23:00 | Connors RSI(2) | buy | SOL-USD | 15.68 | — | entry signal |
| 2026-10-03T23:00 | Squeeze breakout | sell | SOL-USD | 20.16 | -0.15 | exit signal |
| 2026-10-03T23:00 | Bollinger breakout | sell | SOL-USD | 16.56 | -0.12 | exit signal |
| 2026-10-03T23:00 | Bollinger breakout | sell | ETH-USD | 16.59 | -0.12 | exit signal |
| 2026-10-03T22:50 | Z-score reversion | sell | BTC-USD | 19.06 | -0.09 | exit signal |
| 2026-10-03T22:50 | Donchian 20/10 | buy | BTC-USD | 17.25 | — | entry signal |
| 2026-10-03T22:50 | MACD zero-line | buy | BTC-USD | 17.18 | — | entry signal |
| 2026-10-03T22:45 | EMA 20/50 cross | buy | SOL-USD | 19.43 | — | entry signal |
| 2026-10-03T22:44 | AI bee: Bizzy | sell | DOGE-USD | 11.21 | -0.07 | Jev: sell (sell p=0.82) after 11 min |
| 2026-10-03T22:40 | CCI reversion | sell | DOGE-USD | 14.91 | -0.07 | exit signal |
| 2026-10-03T22:40 | RSI(14) reversion | sell | BTC-USD | 21.66 | -0.10 | exit signal |
| 2026-10-03T22:40 | Squeeze breakout | buy | SOL-USD | 20.31 | — | entry signal |
| 2026-10-03T22:40 | Bollinger breakout | buy | SOL-USD | 16.69 | — | entry signal |
| 2026-10-03T22:35 | MACD zero-line | buy | SOL-USD | 17.19 | — | entry signal |
| 2026-10-03T22:33 | AI bee: Bizzy | buy | DOGE-USD | 11.28 | — | Jev: buy (buy p=0.60) |
| 2026-10-03T22:30 | CCI reversion | sell | SOL-USD | 11.96 | -0.06 | exit signal |
| 2026-10-03T22:25 | CCI reversion | sell | BTC-USD | 11.95 | -0.06 | exit signal |
| 2026-10-03T22:21 | AI bee: Bizzy | sell | SOL-USD | 10.31 | -0.06 | Jev: sell (sell p=0.64) after 11 min |
| 2026-10-03T22:20 | MFI reversion | sell | BTC-USD | 18.56 | -0.09 | exit signal |
| 2026-10-03T22:15 | CCI reversion | buy | DOGE-USD | 3.01 | — | rebalance up |
| 2026-10-03T22:15 | CCI reversion | sell | ETH-USD | 11.90 | -0.06 | exit signal |
| 2026-10-03T22:15 | Stochastic reversion | sell | SOL-USD | 16.25 | -0.07 | exit signal |
| 2026-10-03T22:15 | Stochastic reversion | sell | DOGE-USD | 16.25 | -0.09 | exit signal |
| 2026-10-03T22:15 | Z-score reversion | sell | SOL-USD | 19.07 | -0.09 | exit signal |
| 2026-10-03T22:15 | Bollinger reversion | sell | XRP-USD | 15.91 | -0.10 | exit signal |
| 2026-10-03T22:15 | Bollinger reversion | sell | DOGE-USD | 15.92 | -0.09 | exit signal |
| 2026-10-03T22:15 | Bollinger breakout | buy | ETH-USD | 16.70 | — | entry signal |
| 2026-10-03T22:15 | Donchian 20/10 | buy | ETH-USD | 17.26 | — | entry signal |
| 2026-10-03T22:15 | RSI momentum | buy | ETH-USD | 16.66 | — | entry signal |
| 2026-10-03T22:15 | Ichimoku | buy | ETH-USD | 18.21 | — | entry signal |
| 2026-10-03T22:10 | AI bee: Bizzy | buy | SOL-USD | 10.37 | — | Jev: buy (buy p=0.56) |
| 2026-10-03T22:10 | Bollinger reversion | sell | BTC-USD | 15.92 | -0.08 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
