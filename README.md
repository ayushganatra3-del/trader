# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T22:25:05.000168+00:00 · 18383 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.94 (-4.06%)

Closed trades 53, win rate 54.7%, fees £2.10, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 16771 decisions in 3356 calls, $0.2343 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T22:25 | 1 / 3 / 1 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-10T22:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T22:25 | 2 / 2 / 1 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Z-score reversion | TNA | 1.94 | +3.40% | 7 |
| Keltner breakout | LABU | 1.94 | +8.17% | 7 |
| Bollinger reversion | TECL | 1.82 | +2.00% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.79 | -2.38 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -13.59 | -2.18 | -22.02 | 69 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.50 | -0.55 | -37.31 | 43 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.22 | 2.44 | -1.58 | 86 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 18 | Hold BTC | benchmark | 99.18 | -0.82 | 0 | — | 27.45 | 3.29 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -10.40 | -2.01 | -14.61 | 344 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.76 | -3.24 | 38 | 13.2 | 5.58 | 0.83 | -19.85 | 134 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -0.30 | 0.04 | -10.38 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.67 | -0.10 | -13.84 | 257 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.69 | -0.19 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.86 | -4.14 | 110 | 24.5 | -15.92 | -2.58 | -17.84 | 469 |
| 34 | Supertrend · 1h | trend | 95.31 | -4.70 | 52 | 13.5 | 0.41 | 0.25 | -18.22 | 209 |
| 35 | Squeeze breakout · 1h | breakout | 94.00 | -6.00 | 36 | 25.0 | 23.30 | 3.18 | -8.82 | 108 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.39 | -1.81 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.72 | -0.49 | -9.03 | 154 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Ichimoku · 1h | trend | 92.94 | -7.06 | 41 | 19.5 | -0.15 | 0.18 | -20.02 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -4.81 | -0.74 | -13.34 | 416 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.85 | -4.99 | -23.52 | 315 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.71 | 0.65 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 91.73 | -8.27 | 68 | 29.4 | 6.13 | 0.95 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.72 | -8.28 | 120 | 47.5 | -24.17 | -4.16 | -26.91 | 510 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.72 | -0.87 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.23 | -9.77 | 115 | 31.3 | -27.05 | -5.30 | -28.90 | 516 |
| 51 | CCI reversion · 1h | reversion | 89.78 | -10.22 | 100 | 45.0 | -8.29 | -1.07 | -14.35 | 414 |
| 52 | VWAP momentum · 1h | momentum | 89.71 | -10.29 | 278 | 22.3 | -34.08 | -5.14 | -39.30 | 1282 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 89.11 | -10.89 | 62 | 19.4 | -6.97 | -0.76 | -19.79 | 241 |
| 55 | Donchian 20/10 · 1h | breakout | 88.82 | -11.18 | 58 | 19.0 | -0.20 | 0.18 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.48 | -1.42 | -28.63 | 319 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.65 | -5.15 | -36.60 | 701 |
| 58 | Three white soldiers | momentum | 88.02 | -11.98 | 136 | 18.4 | -47.82 | -23.16 | -47.82 | 587 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.85 | -12.15 | 101 | 13.9 | -8.88 | -1.00 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.05 | -1.26 | -25.35 | 213 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.61 | -1.29 | -23.91 | 413 |
| 63 | RSI(14) reversion | reversion | 75.22 | -24.77 | 355 | 28.7 | -72.70 | -18.13 | -72.76 | 1493 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.77 | -16.62 | -73.79 | 1668 |
| 65 | Squeeze breakout | breakout | 71.32 | -28.68 | 323 | 14.9 | -62.61 | -18.42 | -62.61 | 1233 |
| 66 | Donchian 55/20 | breakout | 70.82 | -29.18 | 327 | 18.0 | -67.60 | -14.46 | -67.60 | 1292 |
| 67 | EMA 20/50 cross | trend | 70.74 | -29.26 | 324 | 20.1 | -77.35 | -15.46 | -77.35 | 1462 |
| 68 | Volume breakout | breakout | 70.39 | -29.61 | 259 | 13.1 | -62.76 | -18.14 | -62.76 | 902 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.84 | -16.20 | -71.98 | 1438 |
| 70 | Supertrend | trend | 65.12 | -34.88 | 449 | 20.3 | -86.22 | -21.17 | -86.23 | 1915 |
| 71 | Keltner breakout | breakout | 63.34 | -36.66 | 442 | 14.5 | -83.92 | -27.91 | -83.92 | 1850 |
| 72 | Z-score reversion | reversion | 61.19 | -38.81 | 486 | 23.5 | -85.53 | -23.23 | -85.53 | 2083 |
| 73 | Ichimoku | trend | 60.64 | -39.36 | 401 | 9.7 | -81.69 | -23.36 | -81.70 | 1747 |
| 74 | AI bee: Boozy | ai | 60.55 | -39.45 | 253 | 5.1 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.53 | -39.47 | 498 | 21.7 | -87.65 | -28.46 | -87.67 | 2123 |
| 76 | AI bee: Bizzy | ai | 58.99 | -41.01 | 812 | 9.0 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.54 | -42.46 | 531 | 10.4 | -89.59 | -34.24 | -89.59 | 2132 |
| 78 | Donchian 20/10 | breakout | 56.39 | -43.61 | 623 | 18.3 | -90.85 | -26.22 | -90.85 | 2666 |
| 79 | RSI momentum | momentum | 55.62 | -44.38 | 590 | 17.3 | -90.27 | -25.72 | -90.27 | 2379 |
| 80 | Trend pullback ⏸ | trend | 55.45 | -44.55 | 581 | 15.0 | -90.94 | -27.06 | -90.94 | 2335 |
| 81 | MACD zero-line | trend | 55.18 | -44.82 | 570 | 15.1 | -91.63 | -29.95 | -91.63 | 2368 |
| 82 | Triple EMA stack | trend | 54.02 | -45.98 | 618 | 15.5 | -93.21 | -30.46 | -93.21 | 2619 |
| 83 | Bollinger breakout | breakout | 51.86 | -48.14 | 654 | 14.4 | -93.57 | -33.30 | -93.57 | 2820 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.56 | -98.69 | 5402 |
| 85 | Consensus | meta | 50.59 | -49.41 | 616 | 9.9 | -94.27 | -26.14 | -94.27 | 2692 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -33.26 | -97.39 | 3551 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -36.61 | -96.49 | 3616 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.97 | -99.34 | 5693 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.33 | -31.85 | -96.34 | 3617 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.66 | -99.73 | 6206 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -38.71 | -97.37 | 3688 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.22 | -98.47 | 4715 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.35 | -99.51 | 6147 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -33.60 | -95.85 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.54 | -34.53 | -95.54 | 4084 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.84 | -99.90 | 8324 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T22:25 | RSI(14) reversion | buy | DOGE-USD | 18.82 | — | entry signal |
| 2026-10-10T22:25 | EMA 20/50 cross | sell | BTC-USD | 17.82 | -0.10 | exit signal |
| 2026-10-10T22:24 | AI bee: Bizzy | sell | SOL-USD | 8.24 | -0.06 | Jev: sell (sell p=0.69) after 11 min |
| 2026-10-10T22:20 | Donchian 20/10 | sell | XRP-USD | 14.11 | -0.11 | stop-loss |
| 2026-10-10T22:20 | Supertrend | sell | XRP-USD | 16.18 | -0.14 | exit signal |
| 2026-10-10T22:20 | EMA 20/50 cross | sell | XRP-USD | 17.62 | -0.14 | stop-loss |
| 2026-10-10T22:13 | AI bee: Bizzy | buy | SOL-USD | 8.30 | — | Jev: buy (buy p=0.56) |
| 2026-10-10T22:10 | Triple EMA stack | sell | BTC-USD | 13.45 | -0.09 | exit signal |
| 2026-10-10T22:05 | MACD zero-line | sell | BTC-USD | 13.75 | -0.09 | exit signal |
| 2026-10-10T22:05 | Triple EMA stack | sell | XRP-USD | 13.53 | -0.08 | exit signal |
| 2026-10-10T22:00 | Consensus | sell | BTC-USD | 12.60 | -0.08 | target is flat |
| 2026-10-10T22:00 | Donchian 55/20 | sell | XRP-USD | 17.61 | -0.14 | stop-loss |
| 2026-10-10T22:00 | RSI momentum | sell | XRP-USD | 13.93 | -0.09 | exit signal |
| 2026-10-10T21:45 | Consensus | sell | XRP-USD | 12.64 | -0.09 | target is flat |
| 2026-10-10T21:45 | Squeeze breakout | sell | XRP-USD | 17.74 | -0.12 | exit signal |
| 2026-10-10T21:45 | Keltner breakout | sell | XRP-USD | 15.75 | -0.11 | exit signal |
| 2026-10-10T21:45 | Bollinger breakout | sell | XRP-USD | 12.90 | -0.08 | exit signal |
| 2026-10-10T21:45 | MACD zero-line | sell | XRP-USD | 13.82 | -0.08 | exit signal |
| 2026-10-10T21:35 | Consensus | buy | BTC-USD | 12.68 | — | entry |
| 2026-10-10T21:35 | MACD zero-line | buy | BTC-USD | 13.83 | — | entry signal |
| 2026-10-10T21:35 | Triple EMA stack | buy | BTC-USD | 13.54 | — | entry signal |
| 2026-10-10T21:30 | RSI momentum | sell | SOL-USD | 13.92 | -0.09 | exit signal |
| 2026-10-10T21:30 | EMA 20/50 cross | sell | ETH-USD | 14.27 | -0.03 | exit signal |
| 2026-10-10T21:25 | Triple EMA stack | sell | SOL-USD | 13.47 | -0.09 | exit signal |
| 2026-10-10T21:20 | Triple EMA stack | buy | SOL-USD | 13.57 | — | entry signal |
| 2026-10-10T21:15 | Triple EMA stack | sell | SOL-USD | 13.59 | -0.08 | exit signal |
| 2026-10-10T21:10 | Consensus | sell | BTC-USD | 12.62 | -0.08 | target is flat |
| 2026-10-10T21:10 | Volume breakout | sell | XRP-USD | 17.52 | -0.10 | exit signal |
| 2026-10-10T21:10 | Donchian 55/20 | sell | BTC-USD | 14.28 | -0.08 | exit signal |
| 2026-10-10T21:10 | Triple EMA stack | sell | BTC-USD | 13.51 | -0.09 | exit signal |
| 2026-10-10T21:05 | Consensus | buy | BTC-USD | 12.70 | — | entry |
| 2026-10-10T21:03 | AI bee: Bizzy | sell | DOGE-USD | 8.61 | -0.06 | Jev: sell (sell p=0.74) after 10 min |
| 2026-10-10T21:00 | Consensus | sell | BTC-USD | 12.65 | -0.08 | target is flat |
| 2026-10-10T21:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 8.57 | — | entry signal |
| 2026-10-10T21:00 | MFI reversion | sell | XRP-USD | 15.11 | -0.04 | exit signal |
| 2026-10-10T21:00 | ADX DI cross | sell | ETH-USD | 14.30 | -0.11 | exit signal |
| 2026-10-10T20:55 | ADX DI cross | buy | ETH-USD | 14.41 | — | entry signal |
| 2026-10-10T20:53 | AI bee: Bizzy | buy | DOGE-USD | 8.67 | — | Jev: buy (buy p=0.59) |
| 2026-10-10T20:50 | AI bee: Bizzy | sell | XRP-USD | 8.15 | -0.03 | Jev: sell (sell p=0.57) after 20 min |
| 2026-10-10T20:50 | Donchian 55/20 | buy | XRP-USD | 17.75 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 22:25:05.000168+00:00 -> 2026-10-10 22:35:05.000168+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
