# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T09:30:05.000139+00:00 · 15440 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.70 (-3.31%)

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
| Copy: Insider buying | 2026-10-07 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, BORR 12%, PSUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 7310 decisions in 1462 calls, $0.1025 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T09:30 | 2 / 2 / 1 | PLTR 15% |  |
| Breezy | 2026-10-08T09:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T09:30 | 2 / 3 / 0 | MSTR 70% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.84 | 5.84 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.31 | 2.31 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.72 | 1.72 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Hold SPY | benchmark | 101.41 | 1.41 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 8 | Donchian 55/20 · 1h | breakout | 101.24 | 1.24 | 18 | 5.6 | 11.91 | 1.62 | -16.96 | 108 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.78 | 0.78 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.74 | 0.74 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.55 | 0.55 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.98 | -0.02 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Hold BTC | benchmark | 99.52 | -0.48 | 0 | — | 27.59 | 3.33 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.93 | -1.07 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.61 | -1.39 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.60 | -1.40 | 68 | 23.5 | -20.84 | -5.96 | -23.40 | 173 |
| 21 | EMA 20/50 cross · 1h | trend | 98.51 | -1.49 | 34 | 5.9 | 7.06 | 0.98 | -19.45 | 135 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.51 | -2.49 | 62 | 58.1 | -10.92 | -2.17 | -11.26 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.47 | -2.53 | 0 | — | 12.72 | 2.06 | -7.19 | 1 |
| 25 | Connors RSI(2) · 1h | reversion | 97.17 | -2.83 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.83 | -3.17 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | Agent | meta | 96.70 | -3.31 | 42 | 57.1 | -9.68 | -5.52 | -10.27 | 249 |
| 28 | Copy: Insider buying | copy | 96.60 | -3.40 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 29 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 0.35 | 0.19 | -10.39 | 279 |
| 30 | Supertrend · 1h | trend | 95.86 | -4.14 | 42 | 9.5 | -3.06 | -0.26 | -17.19 | 209 |
| 31 | RSI(14) reversion · 1h | reversion | 95.61 | -4.39 | 20 | 35.0 | 1.97 | 0.60 | -6.57 | 118 |
| 32 | Parabolic SAR · 1h | trend | 95.55 | -4.46 | 80 | 21.2 | -6.92 | -0.81 | -20.87 | 294 |
| 33 | Candlestick reversal · 1h | reversion | 95.53 | -4.47 | 86 | 32.6 | -26.88 | -6.07 | -27.08 | 484 |
| 34 | Z-score reversion · 1h | reversion | 95.37 | -4.63 | 32 | 40.6 | -0.79 | -0.04 | -8.60 | 159 |
| 35 | ADX DI cross · 1h | trend | 95.27 | -4.73 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.25 | -4.75 | 55 | 41.8 | -17.20 | -4.30 | -18.92 | 311 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -1.36 | -0.57 | -6.03 | 109 |
| 38 | Max aggression: 1-day momentum | meta | 95.02 | -4.98 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 39 | Agent (ML meta-label) | meta | 94.98 | -5.02 | 290 | 15.5 | -0.55 | 0.05 | -12.79 | 350 |
| 40 | MACD cross · 1h | trend | 94.94 | -5.06 | 101 | 22.8 | -12.29 | -1.73 | -17.27 | 466 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 14.79 | 2.46 | -8.12 | 102 |
| 42 | RSI momentum · 1h | momentum | 94.27 | -5.73 | 51 | 3.9 | -3.94 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 94.01 | -5.99 | 104 | 21.2 | -17.38 | -5.28 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.60 | -6.40 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.58 | -6.42 | 63 | 30.2 | 7.34 | 1.09 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.30 | -6.70 | 61 | 11.5 | -8.86 | -0.90 | -24.26 | 242 |
| 48 | Volume breakout · 1h | breakout | 92.77 | -7.23 | 44 | 15.9 | 6.49 | 1.05 | -12.60 | 121 |
| 49 | Williams %R · 1h | reversion | 92.51 | -7.49 | 96 | 47.9 | -23.21 | -4.22 | -23.35 | 499 |
| 50 | MFI reversion · 1h | reversion | 92.41 | -7.58 | 87 | 27.6 | -12.28 | -2.11 | -16.99 | 122 |
| 51 | Opening range 15m | breakout | 92.33 | -7.67 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.26 | -8.74 | 50 | 20.0 | 2.07 | 0.46 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.24 | -8.76 | 90 | 11.1 | -4.49 | -0.40 | -18.86 | 339 |
| 54 | CCI reversion · 1h | reversion | 90.75 | -9.25 | 82 | 43.9 | -6.35 | -0.81 | -12.41 | 408 |
| 55 | MACD zero-line · 1h | trend | 90.61 | -9.39 | 57 | 19.3 | -5.63 | -0.56 | -19.00 | 240 |
| 56 | VWAP momentum · 1h | momentum | 90.46 | -9.54 | 243 | 22.6 | -36.24 | -5.50 | -37.98 | 1270 |
| 57 | Three white soldiers | momentum | 90.14 | -9.86 | 108 | 18.5 | -48.61 | -24.23 | -48.61 | 583 |
| 58 | OBV trend · 1h | momentum | 89.36 | -10.64 | 126 | 16.7 | -13.98 | -1.55 | -28.48 | 327 |
| 59 | Keltner breakout · 1h | breakout | 88.99 | -11.01 | 39 | 17.9 | -9.42 | -1.06 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.75 | -11.25 | 126 | 24.6 | -31.84 | -5.42 | -35.61 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.09 | -12.91 | 123 | 19.5 | -9.12 | -1.08 | -23.22 | 406 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.82 | -19.18 | 272 | 30.9 | -72.26 | -19.00 | -72.36 | 1433 |
| 64 | ROC + volume | momentum | 75.87 | -24.13 | 329 | 20.1 | -73.26 | -17.03 | -73.60 | 1648 |
| 65 | Squeeze breakout | breakout | 75.60 | -24.41 | 265 | 14.7 | -62.17 | -18.39 | -62.20 | 1214 |
| 66 | Donchian 55/20 | breakout | 74.01 | -25.99 | 269 | 16.7 | -68.59 | -14.81 | -68.69 | 1287 |
| 67 | VWAP reversion | reversion | 72.83 | -27.17 | 326 | 27.9 | -70.39 | -16.05 | -70.54 | 1399 |
| 68 | Volume breakout | breakout | 72.80 | -27.20 | 216 | 12.0 | -64.32 | -18.85 | -64.32 | 906 |
| 69 | EMA 20/50 cross | trend | 72.75 | -27.25 | 276 | 17.8 | -78.00 | -15.80 | -78.00 | 1467 |
| 70 | Supertrend | trend | 68.55 | -31.45 | 376 | 19.1 | -86.92 | -21.65 | -86.95 | 1929 |
| 71 | MFI reversion | reversion | 66.14 | -33.86 | 410 | 21.5 | -87.52 | -29.43 | -87.53 | 2110 |
| 72 | Keltner breakout | breakout | 65.86 | -34.14 | 367 | 12.5 | -85.25 | -29.41 | -85.25 | 1872 |
| 73 | Ichimoku | trend | 65.20 | -34.80 | 334 | 9.0 | -81.72 | -23.63 | -81.76 | 1732 |
| 74 | Z-score reversion | reversion | 65.19 | -34.81 | 419 | 24.1 | -85.47 | -24.21 | -85.53 | 2071 |
| 75 | AI bee: Bizzy | ai | 64.43 | -35.57 | 662 | 8.3 | — | — | — | — |
| 76 | ADX DI cross | trend | 62.35 | -37.65 | 430 | 8.6 | -89.74 | -35.65 | -89.74 | 2112 |
| 77 | AI bee: Boozy | ai | 62.26 | -37.74 | 230 | 3.5 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 61.42 | -38.58 | 510 | 17.5 | -91.09 | -26.65 | -91.11 | 2663 |
| 79 | MACD zero-line | trend | 60.94 | -39.06 | 485 | 14.6 | -91.52 | -29.96 | -91.52 | 2363 |
| 80 | Trend pullback | trend | 59.87 | -40.13 | 495 | 15.4 | -90.99 | -28.07 | -90.99 | 2322 |
| 81 | RSI momentum | momentum | 59.82 | -40.18 | 479 | 16.1 | -90.48 | -25.82 | -90.50 | 2368 |
| 82 | Triple EMA stack | trend | 59.00 | -41.00 | 518 | 15.1 | -93.36 | -31.38 | -93.36 | 2621 |
| 83 | Bollinger breakout | breakout | 57.13 | -42.87 | 533 | 13.3 | -93.85 | -34.34 | -93.86 | 2827 |
| 84 | Consensus | meta | 56.01 | -43.99 | 507 | 9.9 | -94.37 | -25.44 | -94.37 | 2681 |
| 85 | EMA 9/21 cross | trend | 53.57 | -46.43 | 656 | 15.7 | -97.40 | -33.88 | -97.40 | 3535 |
| 86 | Stochastic reversion | reversion | 53.08 | -46.92 | 772 | 22.0 | -95.63 | -34.84 | -95.63 | 4043 |
| 87 | Connors RSI(2) | reversion | 52.97 | -47.03 | 697 | 19.9 | -96.35 | -32.15 | -96.35 | 3590 |
| 88 | Bollinger reversion | reversion | 52.28 | -47.72 | 718 | 16.7 | -95.79 | -34.19 | -95.80 | 3696 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -31.07 | -98.70 | 5356 |
| 90 | OBV trend ⛔ | momentum | 50.34 | -49.66 | 757 | 14.4 | -96.40 | -37.51 | -96.40 | 3593 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.32 | -37.62 | -99.32 | 5594 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.72 | -99.73 | 6127 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.38 | -40.18 | -97.38 | 3659 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -38.00 | -98.48 | 4685 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.89 | -99.51 | 6098 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.81 | -99.90 | 8253 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T09:25 | Ichimoku | buy | DOGE-USD | 16.31 | — | entry |
| 2026-10-08T09:20 | Ichimoku | sell | DOGE-USD | 16.30 | -0.13 | exit signal |
| 2026-10-08T09:05 | Stochastic reversion | sell | SOL-USD | 13.26 | -0.05 | exit signal |
| 2026-10-08T09:05 | Stochastic reversion | sell | DOGE-USD | 13.25 | -0.03 | exit signal |
| 2026-10-08T09:05 | Stochastic reversion | sell | BTC-USD | 13.23 | -0.07 | exit signal |
| 2026-10-08T09:05 | Bollinger breakout | buy | XRP-USD | 14.29 | — | entry signal |
| 2026-10-08T09:00 | AI bee: Bizzy | sell | XRP-USD | 9.70 | -0.06 | Jev: sell (sell p=0.51) after 10 min |
| 2026-10-08T09:00 | Candlestick reversal · 1h | buy | SOL-USD | 4.86 | — | rebalance up |
| 2026-10-08T09:00 | Candlestick reversal · 1h | buy | ETH-USD | 4.83 | — | rebalance up |
| 2026-10-08T09:00 | Candlestick reversal · 1h | sell | BTC-USD | 19.10 | -0.05 | exit signal |
| 2026-10-08T08:52 | OBV trend | sell | XRP-USD | 11.93 | -0.07 | Kill switch: down 50% from peak |
| 2026-10-08T08:50 | AI bee: Bizzy | buy | XRP-USD | 9.76 | — | Jev: buy (buy p=0.61) |
| 2026-10-08T08:50 | OBV trend | buy | XRP-USD | 12.00 | — | entry signal |
| 2026-10-08T08:50 | EMA 20/50 cross | buy | XRP-USD | 17.63 | — | entry signal |
| 2026-10-08T08:45 | MFI reversion | buy | ETH-USD | 16.54 | — | entry signal |
| 2026-10-08T08:45 | Stochastic reversion | buy | DOGE-USD | 13.28 | — | entry signal |
| 2026-10-08T08:40 | Stochastic reversion | buy | ETH-USD | 13.28 | — | entry signal |
| 2026-10-08T08:40 | Bollinger reversion | buy | ETH-USD | 13.08 | — | entry signal |
| 2026-10-08T08:40 | MACD zero-line | sell | XRP-USD | 15.17 | -0.11 | exit signal |
| 2026-10-08T08:35 | Bollinger breakout | sell | XRP-USD | 2.02 | -0.01 | exit signal |
| 2026-10-08T08:35 | Bollinger breakout | sell | DOGE-USD | 14.23 | -0.11 | exit signal |
| 2026-10-08T08:35 | Donchian 20/10 | buy | DOGE-USD | 11.09 | — | entry |
| 2026-10-08T08:35 | Donchian 20/10 | sell | BTC-USD | 11.09 | -0.10 | exit signal |
| 2026-10-08T08:35 | OBV trend | sell | BTC-USD | 12.00 | -0.13 | stop-loss |
| 2026-10-08T08:35 | RSI momentum | buy | DOGE-USD | 14.79 | — | entry |
| 2026-10-08T08:35 | RSI momentum | sell | BTC-USD | 14.79 | -0.15 | stop-loss |
| 2026-10-08T08:35 | Ichimoku | sell | BTC-USD | 13.02 | -0.13 | stop-loss |
| 2026-10-08T08:35 | Supertrend | buy | BTC-USD | 6.44 | — | entry |
| 2026-10-08T08:35 | Supertrend | sell | SOL-USD | 6.44 | -0.08 | exit signal |
| 2026-10-08T08:35 | EMA 20/50 cross | sell | BTC-USD | 17.63 | -0.18 | stop-loss |
| 2026-10-08T08:35 | EMA 9/21 cross | buy | DOGE-USD | 10.04 | — | entry |
| 2026-10-08T08:35 | EMA 9/21 cross | sell | BTC-USD | 10.04 | -0.08 | exit signal |
| 2026-10-08T08:30 | Stochastic reversion | buy | BTC-USD | 13.30 | — | entry signal |
| 2026-10-08T08:30 | MACD zero-line | buy | XRP-USD | 8.72 | — | rebalance up |
| 2026-10-08T08:30 | MACD zero-line | sell | DOGE-USD | 15.20 | -0.10 | exit signal |
| 2026-10-08T08:28 | AI bee: Bizzy | sell | XRP-USD | 9.70 | -0.07 | Jev: sell (sell p=0.67) after 10 min |
| 2026-10-08T08:25 | Ichimoku | sell | ETH-USD | 13.03 | -0.12 | exit signal |
| 2026-10-08T08:23 | AI bee: Bizzy | sell | DOGE-USD | 9.90 | -0.06 | Jev: sell (sell p=0.54) after 15 min |
| 2026-10-08T08:18 | AI bee: Bizzy | buy | XRP-USD | 9.77 | — | Jev: buy (buy p=0.60) |
| 2026-10-08T08:15 | Keltner breakout | sell | BTC-USD | 16.36 | -0.14 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 09:30:05.000139+00:00 -> 2026-10-08 09:40:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
