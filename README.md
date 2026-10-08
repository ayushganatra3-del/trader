# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T12:30:05.000182+00:00 · 15577 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.70 (-3.30%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.47 | +0.09 |
| ETHU | 19.48 | +0.10 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-08 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 9365 decisions in 1873 calls, $0.1314 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T12:30 | 0 / 3 / 2 | PLTR 15% |  |
| Breezy | 2026-10-08T12:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T12:30 | 2 / 2 / 1 | MSTR 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |
| RSI(14) reversion | SOXL | 1.90 | +5.73% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.85 | 5.85 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.32 | 2.32 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.72 | 1.73 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Hold SPY | benchmark | 101.42 | 1.42 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 8 | Donchian 55/20 · 1h | breakout | 101.24 | 1.24 | 18 | 5.6 | 11.91 | 1.62 | -16.96 | 108 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.78 | 0.78 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.75 | 0.75 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.55 | 0.55 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.99 | -0.01 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Daily: SMA 20/50 cross · AAPL | daily | 98.93 | -1.07 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 18 | Hold BTC | benchmark | 98.86 | -1.14 | 0 | — | 25.92 | 3.15 | -8.68 | 1 |
| 19 | Daily: Bullish score | daily | 98.62 | -1.38 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.61 | -1.39 | 68 | 23.5 | -20.41 | -5.80 | -23.40 | 171 |
| 21 | EMA 20/50 cross · 1h | trend | 98.51 | -1.49 | 34 | 5.9 | 6.13 | 0.88 | -19.45 | 138 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 97.48 | -2.52 | 0 | — | 12.72 | 2.06 | -7.19 | 1 |
| 24 | Stochastic reversion · 1h | reversion | 97.39 | -2.61 | 64 | 56.2 | -10.99 | -2.19 | -11.34 | 339 |
| 25 | Connors RSI(2) · 1h | reversion | 97.18 | -2.82 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.84 | -3.16 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | Agent | meta | 96.70 | -3.30 | 42 | 57.1 | -9.52 | -5.41 | -10.39 | 247 |
| 28 | Copy: Insider buying | copy | 96.60 | -3.40 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 29 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 0.45 | 0.22 | -9.65 | 275 |
| 30 | Supertrend · 1h | trend | 95.86 | -4.13 | 42 | 9.5 | -2.80 | -0.22 | -17.19 | 208 |
| 31 | Parabolic SAR · 1h | trend | 95.55 | -4.45 | 80 | 21.2 | -6.92 | -0.81 | -20.87 | 294 |
| 32 | ADX DI cross · 1h | trend | 95.27 | -4.73 | 47 | 14.9 | -6.04 | -0.83 | -13.84 | 249 |
| 33 | Candlestick reversal · 1h | reversion | 95.17 | -4.83 | 88 | 31.8 | -27.59 | -6.23 | -27.60 | 487 |
| 34 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -0.97 | -0.38 | -6.03 | 109 |
| 35 | Max aggression: 1-day momentum | meta | 95.03 | -4.97 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 36 | Z-score reversion · 1h | reversion | 94.99 | -5.01 | 33 | 39.4 | -1.18 | -0.11 | -8.60 | 159 |
| 37 | Agent (ML meta-label) | meta | 94.98 | -5.01 | 290 | 15.5 | -0.56 | 0.04 | -11.66 | 356 |
| 38 | Bollinger reversion · 1h | reversion | 94.98 | -5.01 | 56 | 41.1 | -17.43 | -4.36 | -18.92 | 311 |
| 39 | MACD cross · 1h | trend | 94.77 | -5.23 | 102 | 22.5 | -12.76 | -1.81 | -17.27 | 466 |
| 40 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 14.96 | 2.49 | -8.12 | 102 |
| 41 | RSI(14) reversion · 1h | reversion | 94.53 | -5.47 | 21 | 33.3 | 0.16 | 0.14 | -6.57 | 120 |
| 42 | RSI momentum · 1h | momentum | 94.27 | -5.72 | 51 | 3.9 | -3.41 | -0.32 | -18.16 | 220 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 94.01 | -5.99 | 104 | 21.2 | -17.38 | -5.28 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.60 | -6.40 | 39 | 17.9 | -2.97 | -0.21 | -19.68 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 93.59 | -6.42 | 63 | 30.2 | 6.84 | 1.03 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.30 | -6.70 | 61 | 11.5 | -8.63 | -0.87 | -24.26 | 240 |
| 48 | Volume breakout · 1h | breakout | 92.77 | -7.23 | 44 | 15.9 | 6.46 | 1.05 | -12.60 | 121 |
| 49 | Williams %R · 1h | reversion | 92.39 | -7.62 | 96 | 47.9 | -23.31 | -4.24 | -23.38 | 499 |
| 50 | Opening range 15m | breakout | 92.33 | -7.67 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 51 | MFI reversion · 1h | reversion | 92.22 | -7.78 | 87 | 27.6 | -12.52 | -2.16 | -16.99 | 122 |
| 52 | Donchian 20/10 · 1h | breakout | 91.27 | -8.73 | 50 | 20.0 | 2.07 | 0.45 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.24 | -8.76 | 90 | 11.1 | -5.15 | -0.49 | -18.86 | 342 |
| 54 | MACD zero-line · 1h | trend | 90.61 | -9.39 | 57 | 19.3 | -5.83 | -0.58 | -19.00 | 240 |
| 55 | VWAP momentum · 1h | momentum | 90.26 | -9.74 | 246 | 22.4 | -36.39 | -5.53 | -38.12 | 1272 |
| 56 | Three white soldiers | momentum | 90.14 | -9.86 | 108 | 18.5 | -48.61 | -24.23 | -48.61 | 583 |
| 57 | CCI reversion · 1h | reversion | 90.03 | -9.97 | 84 | 42.9 | -7.23 | -0.95 | -12.41 | 408 |
| 58 | OBV trend · 1h | momentum | 89.36 | -10.64 | 126 | 16.7 | -13.88 | -1.54 | -28.48 | 326 |
| 59 | Keltner breakout · 1h | breakout | 88.99 | -11.01 | 39 | 17.9 | -9.47 | -1.06 | -23.68 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 88.75 | -11.25 | 126 | 24.6 | -31.84 | -5.42 | -35.61 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.09 | -12.91 | 123 | 19.5 | -9.15 | -1.08 | -23.22 | 406 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.76 | -19.24 | 274 | 30.7 | -73.10 | -19.50 | -73.10 | 1447 |
| 64 | ROC + volume | momentum | 75.70 | -24.30 | 330 | 20.0 | -73.11 | -16.93 | -73.67 | 1645 |
| 65 | Squeeze breakout | breakout | 75.27 | -24.73 | 267 | 14.6 | -62.17 | -18.33 | -62.27 | 1213 |
| 66 | Donchian 55/20 | breakout | 73.64 | -26.36 | 271 | 16.6 | -68.76 | -14.89 | -68.86 | 1289 |
| 67 | Volume breakout | breakout | 72.80 | -27.20 | 216 | 12.0 | -64.03 | -18.71 | -64.03 | 902 |
| 68 | EMA 20/50 cross | trend | 72.41 | -27.59 | 278 | 17.6 | -78.17 | -15.89 | -78.17 | 1468 |
| 69 | VWAP reversion | reversion | 72.19 | -27.81 | 328 | 27.7 | -70.95 | -16.35 | -71.00 | 1411 |
| 70 | Supertrend | trend | 68.47 | -31.53 | 378 | 19.0 | -86.98 | -21.71 | -86.98 | 1929 |
| 71 | Keltner breakout | breakout | 65.86 | -34.14 | 367 | 12.5 | -85.01 | -28.93 | -85.04 | 1864 |
| 72 | MFI reversion | reversion | 65.81 | -34.19 | 412 | 21.4 | -87.65 | -29.68 | -87.65 | 2116 |
| 73 | Ichimoku | trend | 64.81 | -35.19 | 338 | 8.9 | -81.75 | -23.64 | -81.75 | 1732 |
| 74 | AI bee: Bizzy | ai | 64.32 | -35.68 | 664 | 8.3 | — | — | — | — |
| 75 | Z-score reversion | reversion | 64.06 | -35.94 | 424 | 23.8 | -85.68 | -24.33 | -85.68 | 2078 |
| 76 | ADX DI cross | trend | 62.36 | -37.64 | 430 | 8.6 | -89.69 | -35.53 | -89.69 | 2110 |
| 77 | AI bee: Boozy | ai | 62.26 | -37.74 | 230 | 3.5 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 61.38 | -38.62 | 511 | 17.4 | -91.08 | -26.68 | -91.08 | 2660 |
| 79 | MACD zero-line | trend | 60.77 | -39.23 | 487 | 14.6 | -91.55 | -30.00 | -91.55 | 2364 |
| 80 | Trend pullback | trend | 59.87 | -40.13 | 495 | 15.4 | -90.91 | -28.03 | -90.92 | 2316 |
| 81 | RSI momentum | momentum | 59.74 | -40.26 | 480 | 16.0 | -90.43 | -25.70 | -90.45 | 2365 |
| 82 | Triple EMA stack | trend | 59.00 | -41.00 | 518 | 15.1 | -93.27 | -31.12 | -93.27 | 2613 |
| 83 | Bollinger breakout | breakout | 56.96 | -43.04 | 535 | 13.3 | -93.81 | -34.20 | -93.81 | 2822 |
| 84 | Consensus | meta | 56.01 | -43.99 | 507 | 9.9 | -94.34 | -25.41 | -94.35 | 2678 |
| 85 | EMA 9/21 cross | trend | 53.51 | -46.49 | 657 | 15.7 | -97.42 | -33.99 | -97.42 | 3535 |
| 86 | Connors RSI(2) | reversion | 52.97 | -47.03 | 697 | 19.9 | -96.33 | -32.20 | -96.33 | 3587 |
| 87 | Stochastic reversion | reversion | 52.01 | -47.99 | 780 | 21.8 | -95.70 | -35.31 | -95.71 | 4049 |
| 88 | Bollinger reversion | reversion | 51.26 | -48.74 | 725 | 16.6 | -95.86 | -34.50 | -95.86 | 3702 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -30.86 | -98.68 | 5343 |
| 90 | OBV trend ⛔ | momentum | 50.34 | -49.66 | 757 | 14.4 | -96.33 | -36.85 | -96.34 | 3583 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -38.19 | -99.34 | 5612 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.84 | -99.73 | 6133 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -39.50 | -97.35 | 3653 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -38.22 | -98.50 | 4691 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.09 | -99.52 | 6101 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.59 | -99.90 | 8243 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T12:20 | MACD cross · 1h | buy | DOGE-USD | 9.00 | — | entry |
| 2026-10-08T12:20 | Z-score reversion | buy | SOL-USD | 16.03 | — | entry signal |
| 2026-10-08T12:15 | CCI reversion · 1h | buy | DOGE-USD | 13.40 | — | rebalance up |
| 2026-10-08T12:15 | CCI reversion · 1h | buy | BTC-USD | 4.51 | — | rebalance up |
| 2026-10-08T12:15 | CCI reversion · 1h | sell | XRP-USD | 17.90 | -0.15 | stop-loss |
| 2026-10-08T12:15 | MACD cross · 1h | sell | DOGE-USD | 9.00 | -0.16 | stop-loss |
| 2026-10-08T12:15 | Stochastic reversion | sell | DOGE-USD | 13.05 | -0.13 | stop-loss |
| 2026-10-08T12:15 | Z-score reversion | sell | XRP-USD | 15.98 | -0.17 | stop-loss |
| 2026-10-08T12:15 | Z-score reversion | sell | DOGE-USD | 15.97 | -0.18 | stop-loss |
| 2026-10-08T12:10 | Stochastic reversion | buy | SOL-USD | 12.94 | — | entry signal |
| 2026-10-08T12:05 | Stochastic reversion · 1h | sell | BTC-USD | 6.41 | -0.10 | stop-loss |
| 2026-10-08T12:05 | Stochastic reversion | sell | SOL-USD | 12.94 | -0.14 | stop-loss |
| 2026-10-08T12:05 | Bollinger reversion | sell | SOL-USD | 12.73 | -0.14 | stop-loss |
| 2026-10-08T11:40 | MFI reversion | buy | ETH-USD | 1.68 | — | entry signal |
| 2026-10-08T11:40 | Z-score reversion | buy | ETH-USD | 16.10 | — | entry signal |
| 2026-10-08T11:30 | Z-score reversion | buy | BTC-USD | 16.12 | — | entry signal |
| 2026-10-08T11:25 | MFI reversion | buy | BTC-USD | 16.46 | — | entry signal |
| 2026-10-08T11:25 | Z-score reversion | buy | XRP-USD | 16.15 | — | entry signal |
| 2026-10-08T11:25 | Z-score reversion | buy | DOGE-USD | 16.15 | — | entry signal |
| 2026-10-08T11:25 | Bollinger reversion | buy | SOL-USD | 12.87 | — | entry signal |
| 2026-10-08T11:25 | Bollinger reversion | buy | ETH-USD | 12.87 | — | entry signal |
| 2026-10-08T11:20 | MFI reversion · 1h | buy | ETH-USD | 4.64 | — | rebalance up |
| 2026-10-08T11:20 | Z-score reversion · 1h | sell | ETH-USD | 23.51 | -0.51 | stop-loss |
| 2026-10-08T11:20 | Bollinger reversion · 1h | sell | SOL-USD | 5.60 | -0.13 | stop-loss |
| 2026-10-08T11:20 | RSI(14) reversion · 1h | sell | ETH-USD | 19.03 | -0.46 | stop-loss |
| 2026-10-08T11:20 | Z-score reversion | sell | XRP-USD | 16.08 | -0.20 | stop-loss |
| 2026-10-08T11:20 | Bollinger reversion | sell | BTC-USD | 12.79 | -0.14 | stop-loss |
| 2026-10-08T11:20 | RSI(14) reversion | buy | DOGE-USD | 2.66 | — | entry |
| 2026-10-08T11:20 | RSI(14) reversion | sell | XRP-USD | 2.66 | -0.02 | stop-loss |
| 2026-10-08T11:15 | Stochastic reversion | buy | XRP-USD | 13.05 | — | entry signal |
| 2026-10-08T11:15 | Stochastic reversion | buy | SOL-USD | 13.09 | — | entry signal |
| 2026-10-08T11:15 | Stochastic reversion | buy | BTC-USD | 13.09 | — | entry signal |
| 2026-10-08T11:15 | VWAP reversion | buy | XRP-USD | 9.83 | — | entry signal |
| 2026-10-08T11:15 | VWAP reversion | buy | ETH-USD | 18.08 | — | entry signal |
| 2026-10-08T11:15 | VWAP reversion | buy | BTC-USD | 18.08 | — | entry signal |
| 2026-10-08T11:10 | CCI reversion · 1h | buy | DOGE-USD | 9.01 | — | entry |
| 2026-10-08T11:10 | CCI reversion · 1h | buy | BTC-USD | 8.86 | — | rebalance up |
| 2026-10-08T11:10 | CCI reversion · 1h | sell | ETH-USD | 17.87 | -0.29 | stop-loss |
| 2026-10-08T11:10 | MFI reversion | sell | BTC-USD | 16.35 | -0.17 | stop-loss |
| 2026-10-08T11:10 | Stochastic reversion | buy | DOGE-USD | 2.70 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 12:30:05.000182+00:00 -> 2026-10-08 12:40:05.000182+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
