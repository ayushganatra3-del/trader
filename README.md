# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T04:30:05.000172+00:00 · 15184 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.65 (-3.35%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.45 | +0.07 |
| ETHU | 19.46 | +0.07 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-07 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, BORR 12%, PSUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 3480 decisions in 696 calls, $0.0488 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T04:30 | 0 / 4 / 1 | PLTR 15% |  |
| Breezy | 2026-10-08T04:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T04:30 | 2 / 3 / 0 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.71 | 5.71 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.18 | 2.19 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.59 | 1.59 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.29 | 1.29 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.11 | 1.11 | 18 | 5.6 | 11.49 | 1.57 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.65 | 0.65 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.62 | 0.62 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.52 | 0.52 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.86 | -0.14 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Hold BTC | benchmark | 99.20 | -0.80 | 0 | — | 28.75 | 3.44 | -8.68 | 1 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.80 | -1.20 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.49 | -1.51 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.49 | -1.51 | 68 | 23.5 | -20.89 | -5.98 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.42 | -1.58 | 34 | 5.9 | 7.47 | 1.02 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.45 | -2.55 | 62 | 58.1 | -10.83 | -2.15 | -11.24 | 339 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.35 | -2.65 | 0 | — | 12.72 | 2.06 | -7.19 | 1 |
| 25 | Connors RSI(2) · 1h | reversion | 97.06 | -2.94 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.77 | -3.23 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | Agent | meta | 96.65 | -3.35 | 42 | 57.1 | -11.03 | -6.01 | -11.37 | 253 |
| 28 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 1.49 | 0.50 | -10.39 | 277 |
| 29 | Copy: Insider buying | copy | 96.48 | -3.52 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 30 | RSI(14) reversion · 1h | reversion | 96.07 | -3.93 | 18 | 38.9 | 2.33 | 0.69 | -6.57 | 114 |
| 31 | Z-score reversion · 1h | reversion | 95.81 | -4.19 | 30 | 43.3 | -0.23 | 0.08 | -8.60 | 159 |
| 32 | Candlestick reversal · 1h | reversion | 95.78 | -4.22 | 85 | 32.9 | -26.67 | -6.02 | -26.77 | 480 |
| 33 | Supertrend · 1h | trend | 95.77 | -4.23 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 34 | Parabolic SAR · 1h | trend | 95.49 | -4.51 | 80 | 21.2 | -6.76 | -0.78 | -20.87 | 295 |
| 35 | ADX DI cross · 1h | trend | 95.18 | -4.82 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.14 | -4.86 | 55 | 41.8 | -17.17 | -4.29 | -18.92 | 308 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -6.21 | -2.32 | -6.70 | 114 |
| 38 | Max aggression: 1-day momentum | meta | 94.91 | -5.09 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 39 | Agent (ML meta-label) | meta | 94.88 | -5.12 | 290 | 15.5 | -1.56 | -0.14 | -13.24 | 365 |
| 40 | MACD cross · 1h | trend | 94.80 | -5.20 | 101 | 22.8 | -12.35 | -1.74 | -17.27 | 467 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.15 | 2.52 | -8.12 | 101 |
| 42 | RSI momentum · 1h | momentum | 94.17 | -5.83 | 51 | 3.9 | -3.92 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.89 | -6.11 | 104 | 21.2 | -17.38 | -5.28 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.55 | -6.45 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.53 | -6.47 | 63 | 30.2 | 7.56 | 1.12 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.21 | -6.79 | 61 | 11.5 | -8.70 | -0.88 | -24.26 | 242 |
| 48 | Volume breakout · 1h | breakout | 92.74 | -7.26 | 44 | 15.9 | 6.47 | 1.05 | -12.60 | 121 |
| 49 | MFI reversion · 1h | reversion | 92.72 | -7.28 | 86 | 27.9 | -11.95 | -2.05 | -16.99 | 122 |
| 50 | Williams %R · 1h | reversion | 92.61 | -7.39 | 95 | 48.4 | -22.90 | -4.15 | -23.19 | 499 |
| 51 | Opening range 15m | breakout | 92.21 | -7.79 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.16 | -8.84 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.16 | -8.84 | 90 | 11.1 | -4.61 | -0.42 | -18.86 | 340 |
| 54 | CCI reversion · 1h | reversion | 90.84 | -9.16 | 80 | 45.0 | -5.98 | -0.75 | -12.41 | 406 |
| 55 | MACD zero-line · 1h | trend | 90.55 | -9.45 | 57 | 19.3 | -4.96 | -0.47 | -19.00 | 237 |
| 56 | VWAP momentum · 1h | momentum | 90.39 | -9.62 | 243 | 22.6 | -36.84 | -5.63 | -37.98 | 1274 |
| 57 | Three white soldiers | momentum | 90.29 | -9.71 | 107 | 18.7 | -48.59 | -24.14 | -48.59 | 583 |
| 58 | OBV trend · 1h | momentum | 89.33 | -10.67 | 126 | 16.7 | -14.59 | -1.63 | -28.48 | 330 |
| 59 | Keltner breakout · 1h | breakout | 88.96 | -11.04 | 39 | 17.9 | -8.97 | -0.99 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.72 | -11.28 | 126 | 24.6 | -31.96 | -5.45 | -35.61 | 691 |
| 61 | ROC + volume · 1h | momentum | 87.01 | -12.99 | 123 | 19.5 | -9.12 | -1.08 | -23.22 | 406 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.74 | -19.26 | 270 | 31.1 | -72.08 | -18.86 | -72.11 | 1431 |
| 64 | ROC + volume | momentum | 76.18 | -23.82 | 327 | 20.2 | -73.40 | -17.09 | -73.60 | 1652 |
| 65 | Squeeze breakout | breakout | 75.78 | -24.22 | 264 | 14.8 | -62.05 | -18.31 | -62.11 | 1214 |
| 66 | Donchian 55/20 | breakout | 73.96 | -26.04 | 269 | 16.7 | -68.87 | -14.99 | -68.93 | 1293 |
| 67 | EMA 20/50 cross | trend | 72.88 | -27.12 | 275 | 17.8 | -77.83 | -15.70 | -77.83 | 1462 |
| 68 | Volume breakout | breakout | 72.78 | -27.22 | 216 | 12.0 | -64.75 | -18.90 | -64.75 | 914 |
| 69 | VWAP reversion | reversion | 72.73 | -27.27 | 323 | 27.2 | -70.17 | -15.87 | -70.42 | 1392 |
| 70 | Supertrend | trend | 68.62 | -31.38 | 374 | 19.3 | -86.73 | -21.39 | -86.79 | 1923 |
| 71 | MFI reversion | reversion | 66.31 | -33.69 | 406 | 21.7 | -87.44 | -29.18 | -87.46 | 2108 |
| 72 | Keltner breakout | breakout | 65.97 | -34.03 | 366 | 12.6 | -85.32 | -29.43 | -85.32 | 1879 |
| 73 | Ichimoku | trend | 65.78 | -34.22 | 330 | 9.1 | -81.71 | -23.57 | -81.72 | 1732 |
| 74 | Z-score reversion | reversion | 65.50 | -34.51 | 413 | 24.5 | -85.38 | -24.09 | -85.41 | 2068 |
| 75 | AI bee: Bizzy | ai | 65.02 | -34.98 | 653 | 8.4 | — | — | — | — |
| 76 | ADX DI cross | trend | 62.82 | -37.18 | 424 | 8.7 | -89.67 | -34.96 | -89.67 | 2110 |
| 77 | AI bee: Boozy | ai | 62.77 | -37.23 | 226 | 3.5 | — | — | — | — |
| 78 | MACD zero-line | trend | 61.61 | -38.39 | 478 | 14.9 | -91.35 | -29.43 | -91.35 | 2354 |
| 79 | Donchian 20/10 | breakout | 61.54 | -38.46 | 508 | 17.5 | -91.03 | -26.44 | -91.03 | 2663 |
| 80 | RSI momentum | momentum | 59.88 | -40.12 | 478 | 16.1 | -90.44 | -25.71 | -90.47 | 2369 |
| 81 | Trend pullback | trend | 59.85 | -40.15 | 495 | 15.4 | -91.09 | -28.48 | -91.10 | 2329 |
| 82 | Triple EMA stack | trend | 58.92 | -41.08 | 518 | 15.1 | -93.28 | -31.15 | -93.31 | 2618 |
| 83 | Bollinger breakout | breakout | 57.53 | -42.47 | 528 | 13.4 | -93.83 | -34.04 | -93.83 | 2830 |
| 84 | Consensus | meta | 55.97 | -44.03 | 507 | 9.9 | -94.49 | -25.93 | -94.49 | 2694 |
| 85 | EMA 9/21 cross | trend | 53.83 | -46.17 | 652 | 15.8 | -97.34 | -33.35 | -97.34 | 3523 |
| 86 | Stochastic reversion | reversion | 53.29 | -46.72 | 764 | 22.1 | -95.61 | -34.69 | -95.61 | 4035 |
| 87 | Connors RSI(2) | reversion | 52.95 | -47.05 | 697 | 19.9 | -96.39 | -32.57 | -96.39 | 3598 |
| 88 | Bollinger reversion | reversion | 52.51 | -47.49 | 713 | 16.7 | -95.77 | -34.05 | -95.77 | 3694 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.49 | -98.65 | 5332 |
| 90 | OBV trend | momentum | 50.49 | -49.51 | 755 | 14.4 | -96.40 | -37.38 | -96.40 | 3596 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -37.09 | -99.30 | 5585 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.31 | -99.73 | 6125 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -40.14 | -97.39 | 3662 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.80 | -98.47 | 4680 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.78 | -99.51 | 6096 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.57 | -99.90 | 8250 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T04:30 | Stochastic reversion | sell | BTC-USD | 13.37 | -0.05 | exit signal |
| 2026-10-08T04:30 | Z-score reversion | buy | SOL-USD | 16.39 | — | entry signal |
| 2026-10-08T04:30 | Bollinger reversion | buy | XRP-USD | 13.15 | — | entry signal |
| 2026-10-08T04:30 | Bollinger reversion | buy | DOGE-USD | 13.15 | — | entry signal |
| 2026-10-08T04:25 | Stochastic reversion | sell | XRP-USD | 13.22 | -0.19 | stop-loss |
| 2026-10-08T04:25 | VWAP reversion | buy | SOL-USD | 18.19 | — | entry signal |
| 2026-10-08T04:25 | VWAP reversion | sell | XRP-USD | 18.04 | -0.26 | stop-loss |
| 2026-10-08T04:25 | Bollinger reversion | buy | SOL-USD | 13.15 | — | entry signal |
| 2026-10-08T04:25 | Bollinger reversion | sell | XRP-USD | 13.03 | -0.19 | stop-loss |
| 2026-10-08T04:20 | MFI reversion · 1h | buy | DOGE-USD | 4.67 | — | rebalance up |
| 2026-10-08T04:20 | MFI reversion · 1h | sell | SOL-USD | 18.44 | -0.33 | stop-loss |
| 2026-10-08T04:20 | MFI reversion · 1h | sell | BTC-USD | 18.46 | -0.28 | stop-loss |
| 2026-10-08T04:20 | Williams %R · 1h | buy | XRP-USD | 5.39 | — | rebalance up |
| 2026-10-08T04:20 | Williams %R · 1h | sell | SOL-USD | 13.12 | -0.29 | stop-loss |
| 2026-10-08T04:20 | Williams %R · 1h | sell | BTC-USD | 13.20 | -0.21 | stop-loss |
| 2026-10-08T04:20 | Z-score reversion · 1h | buy | XRP-USD | 11.97 | — | rebalance up |
| 2026-10-08T04:20 | Z-score reversion · 1h | sell | SOL-USD | 15.83 | -0.30 | stop-loss |
| 2026-10-08T04:20 | Z-score reversion · 1h | sell | BTC-USD | 15.90 | -0.25 | stop-loss |
| 2026-10-08T04:20 | RSI(14) reversion · 1h | buy | XRP-USD | 14.34 | — | rebalance up |
| 2026-10-08T04:20 | RSI(14) reversion · 1h | buy | DOGE-USD | 4.86 | — | rebalance up |
| 2026-10-08T04:20 | RSI(14) reversion · 1h | sell | SOL-USD | 23.87 | -0.53 | stop-loss |
| 2026-10-08T04:20 | RSI(14) reversion · 1h | sell | BTC-USD | 24.02 | -0.39 | stop-loss |
| 2026-10-08T04:20 | MACD cross · 1h | buy | DOGE-USD | 9.16 | — | entry |
| 2026-10-08T04:20 | MACD cross · 1h | sell | BTC-USD | 9.16 | -0.16 | stop-loss |
| 2026-10-08T04:20 | Stochastic reversion | sell | SOL-USD | 13.26 | -0.15 | stop-loss |
| 2026-10-08T04:20 | VWAP reversion | sell | SOL-USD | 18.09 | -0.21 | stop-loss |
| 2026-10-08T04:20 | Z-score reversion | sell | DOGE-USD | 16.34 | -0.23 | stop-loss |
| 2026-10-08T04:20 | Bollinger reversion | sell | DOGE-USD | 10.52 | -0.15 | stop-loss |
| 2026-10-08T04:10 | Agent (ML meta-label) | sell | SOL-USD | 3.42 | -0.02 | selected signal exited |
| 2026-10-08T04:10 | MFI reversion | buy | ETH-USD | 16.58 | — | entry signal |
| 2026-10-08T04:10 | Stochastic reversion | buy | XRP-USD | 13.41 | — | entry signal |
| 2026-10-08T04:10 | Stochastic reversion | buy | SOL-USD | 13.41 | — | entry signal |
| 2026-10-08T04:10 | VWAP reversion | buy | XRP-USD | 18.30 | — | entry signal |
| 2026-10-08T04:10 | VWAP reversion | buy | SOL-USD | 18.30 | — | entry signal |
| 2026-10-08T04:10 | Z-score reversion | buy | ETH-USD | 16.43 | — | entry signal |
| 2026-10-08T04:10 | Z-score reversion | buy | BTC-USD | 16.43 | — | entry signal |
| 2026-10-08T04:10 | Bollinger reversion | buy | XRP-USD | 13.22 | — | entry signal |
| 2026-10-08T04:10 | RSI(14) reversion | buy | BTC-USD | 2.74 | — | entry signal |
| 2026-10-08T04:05 | Agent (ML meta-label) | buy | SOL-USD | 3.44 | — | entry |
| 2026-10-08T04:05 | Stochastic reversion | buy | BTC-USD | 13.42 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 04:30:05.000172+00:00 -> 2026-10-08 04:40:05.000172+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
