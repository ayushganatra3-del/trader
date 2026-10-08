# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T11:30:05.000175+00:00 · 15533 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.67 (-3.33%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.46 | +0.08 |
| ETHU | 19.47 | +0.09 |

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

Today: 8705 decisions in 1741 calls, $0.1221 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T11:30 | 1 / 4 / 0 | PLTR 15% |  |
| Breezy | 2026-10-08T11:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T11:30 | 0 / 5 / 0 | MSTR 70% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.78 | 5.78 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.25 | 2.25 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.66 | 1.66 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Hold SPY | benchmark | 101.35 | 1.35 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 8 | Donchian 55/20 · 1h | breakout | 101.17 | 1.17 | 18 | 5.6 | 11.91 | 1.62 | -16.96 | 108 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.72 | 0.71 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.68 | 0.68 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.53 | 0.53 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.92 | -0.08 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Hold BTC | benchmark | 98.87 | -1.13 | 0 | — | 26.58 | 3.22 | -8.68 | 1 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.87 | -1.13 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.55 | -1.45 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.55 | -1.46 | 68 | 23.5 | -20.84 | -5.96 | -23.40 | 173 |
| 21 | EMA 20/50 cross · 1h | trend | 98.46 | -1.54 | 34 | 5.9 | 7.05 | 0.98 | -19.45 | 135 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 97.41 | -2.59 | 0 | — | 12.72 | 2.06 | -7.19 | 1 |
| 24 | Stochastic reversion · 1h | reversion | 97.39 | -2.61 | 63 | 57.1 | -11.02 | -2.20 | -11.31 | 340 |
| 25 | Connors RSI(2) · 1h | reversion | 97.11 | -2.89 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.80 | -3.20 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | Agent | meta | 96.67 | -3.33 | 42 | 57.1 | -9.68 | -5.52 | -10.27 | 249 |
| 28 | Copy: Insider buying | copy | 96.54 | -3.46 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 29 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 0.53 | 0.24 | -10.39 | 277 |
| 30 | Supertrend · 1h | trend | 95.82 | -4.18 | 42 | 9.5 | -3.06 | -0.26 | -17.19 | 209 |
| 31 | Parabolic SAR · 1h | trend | 95.52 | -4.49 | 80 | 21.2 | -6.92 | -0.81 | -20.87 | 294 |
| 32 | ADX DI cross · 1h | trend | 95.22 | -4.78 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 33 | Candlestick reversal · 1h | reversion | 95.17 | -4.83 | 88 | 31.8 | -27.17 | -6.13 | -27.17 | 480 |
| 34 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -1.36 | -0.57 | -6.03 | 109 |
| 35 | Z-score reversion · 1h | reversion | 94.97 | -5.03 | 33 | 39.4 | -1.18 | -0.11 | -8.60 | 159 |
| 36 | Bollinger reversion · 1h | reversion | 94.97 | -5.03 | 56 | 41.1 | -17.41 | -4.36 | -18.92 | 311 |
| 37 | Max aggression: 1-day momentum | meta | 94.96 | -5.04 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 38 | Agent (ML meta-label) | meta | 94.93 | -5.07 | 290 | 15.5 | 2.97 | 0.67 | -11.40 | 356 |
| 39 | MACD cross · 1h | trend | 94.82 | -5.18 | 101 | 22.8 | -12.54 | -1.77 | -17.27 | 466 |
| 40 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.15 | 2.52 | -8.12 | 101 |
| 41 | RSI(14) reversion · 1h | reversion | 94.70 | -5.30 | 21 | 33.3 | 0.81 | 0.30 | -6.57 | 117 |
| 42 | RSI momentum · 1h | momentum | 94.22 | -5.78 | 51 | 3.9 | -3.60 | -0.35 | -18.16 | 221 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.95 | -6.05 | 104 | 21.2 | -17.38 | -5.28 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.57 | -6.43 | 39 | 17.9 | -3.18 | -0.24 | -19.68 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 93.56 | -6.44 | 63 | 30.2 | 6.95 | 1.05 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.25 | -6.75 | 61 | 11.5 | -8.98 | -0.91 | -24.26 | 242 |
| 48 | Volume breakout · 1h | breakout | 92.76 | -7.24 | 44 | 15.9 | 6.49 | 1.05 | -12.60 | 121 |
| 49 | Williams %R · 1h | reversion | 92.36 | -7.64 | 96 | 47.9 | -23.30 | -4.24 | -23.37 | 499 |
| 50 | Opening range 15m | breakout | 92.27 | -7.73 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 51 | MFI reversion · 1h | reversion | 92.23 | -7.77 | 87 | 27.6 | -12.49 | -2.15 | -16.99 | 122 |
| 52 | Donchian 20/10 · 1h | breakout | 91.21 | -8.79 | 50 | 20.0 | 2.07 | 0.46 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.20 | -8.80 | 90 | 11.1 | -4.49 | -0.40 | -18.86 | 339 |
| 54 | MACD zero-line · 1h | trend | 90.58 | -9.42 | 57 | 19.3 | -5.62 | -0.56 | -19.00 | 240 |
| 55 | CCI reversion · 1h | reversion | 90.22 | -9.78 | 83 | 43.4 | -6.92 | -0.90 | -12.41 | 408 |
| 56 | VWAP momentum · 1h | momentum | 90.21 | -9.79 | 246 | 22.4 | -36.39 | -5.53 | -38.12 | 1272 |
| 57 | Three white soldiers | momentum | 90.14 | -9.86 | 108 | 18.5 | -48.61 | -24.23 | -48.61 | 583 |
| 58 | OBV trend · 1h | momentum | 89.34 | -10.65 | 126 | 16.7 | -13.99 | -1.55 | -28.48 | 327 |
| 59 | Keltner breakout · 1h | breakout | 88.98 | -11.02 | 39 | 17.9 | -9.66 | -1.09 | -23.68 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 88.74 | -11.26 | 126 | 24.6 | -31.84 | -5.42 | -35.61 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.05 | -12.95 | 123 | 19.5 | -9.12 | -1.08 | -23.22 | 406 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.71 | -19.29 | 274 | 30.7 | -72.56 | -19.20 | -72.57 | 1440 |
| 64 | ROC + volume | momentum | 75.67 | -24.33 | 330 | 20.0 | -73.18 | -16.99 | -73.67 | 1646 |
| 65 | Squeeze breakout | breakout | 75.27 | -24.73 | 267 | 14.6 | -62.17 | -18.33 | -62.27 | 1213 |
| 66 | Donchian 55/20 | breakout | 73.62 | -26.38 | 271 | 16.6 | -68.76 | -14.89 | -68.86 | 1289 |
| 67 | Volume breakout | breakout | 72.79 | -27.21 | 216 | 12.0 | -64.03 | -18.71 | -64.03 | 902 |
| 68 | EMA 20/50 cross | trend | 72.37 | -27.63 | 278 | 17.6 | -78.24 | -15.93 | -78.24 | 1469 |
| 69 | VWAP reversion | reversion | 72.20 | -27.80 | 328 | 27.7 | -70.76 | -16.26 | -70.90 | 1406 |
| 70 | Supertrend | trend | 68.43 | -31.57 | 378 | 19.0 | -86.98 | -21.71 | -86.98 | 1929 |
| 71 | Keltner breakout | breakout | 65.84 | -34.16 | 367 | 12.5 | -85.05 | -29.04 | -85.05 | 1865 |
| 72 | MFI reversion | reversion | 65.79 | -34.21 | 412 | 21.4 | -87.57 | -29.53 | -87.57 | 2111 |
| 73 | Ichimoku | trend | 64.81 | -35.19 | 338 | 8.9 | -81.83 | -23.76 | -81.83 | 1734 |
| 74 | Z-score reversion | reversion | 64.45 | -35.55 | 422 | 23.9 | -85.59 | -24.28 | -85.59 | 2076 |
| 75 | AI bee: Bizzy | ai | 64.32 | -35.68 | 664 | 8.3 | — | — | — | — |
| 76 | ADX DI cross | trend | 62.33 | -37.67 | 430 | 8.6 | -89.74 | -35.66 | -89.74 | 2112 |
| 77 | AI bee: Boozy | ai | 62.26 | -37.74 | 230 | 3.5 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 61.35 | -38.65 | 511 | 17.4 | -91.11 | -26.73 | -91.11 | 2661 |
| 79 | MACD zero-line | trend | 60.75 | -39.25 | 487 | 14.6 | -91.54 | -29.98 | -91.54 | 2364 |
| 80 | Trend pullback | trend | 59.86 | -40.14 | 495 | 15.4 | -90.96 | -28.07 | -90.97 | 2319 |
| 81 | RSI momentum | momentum | 59.71 | -40.29 | 480 | 16.0 | -90.46 | -25.76 | -90.46 | 2366 |
| 82 | Triple EMA stack | trend | 58.96 | -41.04 | 518 | 15.1 | -93.31 | -31.28 | -93.31 | 2616 |
| 83 | Bollinger breakout | breakout | 56.93 | -43.07 | 535 | 13.3 | -93.83 | -34.28 | -93.83 | 2823 |
| 84 | Consensus | meta | 55.99 | -44.01 | 507 | 9.9 | -94.29 | -25.35 | -94.29 | 2672 |
| 85 | EMA 9/21 cross | trend | 53.48 | -46.52 | 657 | 15.7 | -97.41 | -33.95 | -97.41 | 3534 |
| 86 | Connors RSI(2) | reversion | 52.96 | -47.04 | 697 | 19.9 | -96.33 | -32.19 | -96.33 | 3588 |
| 87 | Stochastic reversion | reversion | 52.30 | -47.70 | 778 | 21.9 | -95.68 | -35.20 | -95.69 | 4048 |
| 88 | Bollinger reversion | reversion | 51.42 | -48.58 | 724 | 16.6 | -95.84 | -34.45 | -95.84 | 3702 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.93 | -98.69 | 5346 |
| 90 | OBV trend ⛔ | momentum | 50.31 | -49.69 | 757 | 14.4 | -96.37 | -37.25 | -96.37 | 3588 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.33 | -37.99 | -99.33 | 5607 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.71 | -99.73 | 6126 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.38 | -40.00 | -97.38 | 3658 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -38.05 | -98.48 | 4687 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -41.03 | -99.51 | 6102 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.71 | -99.90 | 8248 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-08T11:10 | Stochastic reversion | sell | XRP-USD | 10.47 | -0.13 | stop-loss |
| 2026-10-08T11:10 | Stochastic reversion | sell | SOL-USD | 10.47 | -0.15 | stop-loss |
| 2026-10-08T11:10 | Stochastic reversion | sell | ETH-USD | 10.47 | -0.14 | stop-loss |
| 2026-10-08T11:10 | Stochastic reversion | sell | BTC-USD | 10.51 | -0.11 | stop-loss |
| 2026-10-08T11:10 | VWAP reversion | sell | SOL-USD | 17.94 | -0.27 | stop-loss |
| 2026-10-08T11:10 | VWAP reversion | sell | ETH-USD | 17.95 | -0.24 | stop-loss |
| 2026-10-08T11:10 | Z-score reversion | sell | SOL-USD | 16.06 | -0.24 | stop-loss |
| 2026-10-08T11:10 | Z-score reversion | sell | BTC-USD | 16.11 | -0.17 | stop-loss |
| 2026-10-08T11:10 | Bollinger reversion | buy | DOGE-USD | 5.12 | — | rebalance up |
| 2026-10-08T11:10 | Bollinger reversion | sell | XRP-USD | 10.30 | -0.13 | stop-loss |
| 2026-10-08T11:10 | Bollinger reversion | sell | SOL-USD | 10.29 | -0.15 | stop-loss |
| 2026-10-08T11:10 | Bollinger reversion | sell | ETH-USD | 10.29 | -0.14 | stop-loss |
| 2026-10-08T11:10 | RSI(14) reversion | buy | XRP-USD | 2.68 | — | entry |
| 2026-10-08T11:10 | RSI(14) reversion | sell | SOL-USD | 2.68 | -0.04 | stop-loss |
| 2026-10-08T11:05 | Bollinger reversion | buy | DOGE-USD | 7.82 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 11:30:05.000175+00:00 -> 2026-10-08 11:40:05.000175+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
