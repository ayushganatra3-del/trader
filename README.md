# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T23:55:05.000151+00:00 · 18451 ticks

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

Today: 17791 decisions in 3560 calls, $0.2486 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T23:55 | 0 / 2 / 3 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-10T23:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T23:55 | 2 / 2 / 1 | COIN 76% |  |

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
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.95 | -1.92 | -14.61 | 342 |
| 19 | Hold BTC | benchmark | 99.15 | -0.85 | 0 | — | 27.33 | 3.27 | -8.68 | 1 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -23.05 | -6.52 | -25.39 | 174 |
| 27 | EMA 20/50 cross · 1h | trend | 96.75 | -3.25 | 38 | 13.2 | 4.48 | 0.71 | -19.85 | 137 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 2.19 | 0.62 | -7.98 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.60 | -0.08 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.72 | -0.19 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.85 | -4.15 | 110 | 24.5 | -15.96 | -2.58 | -17.84 | 469 |
| 34 | Supertrend · 1h | trend | 95.26 | -4.75 | 52 | 13.5 | -0.18 | 0.17 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 93.98 | -6.02 | 36 | 25.0 | 23.88 | 3.25 | -8.83 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.19 | -1.77 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -1.71 | -0.26 | -9.03 | 147 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Ichimoku · 1h | trend | 92.93 | -7.07 | 41 | 19.5 | -0.15 | 0.18 | -20.02 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -1.03 | -0.05 | -11.90 | 410 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.73 | -4.95 | -23.39 | 314 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.43 | 0.62 | -17.07 | 224 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 91.72 | -8.28 | 68 | 29.4 | 6.27 | 0.97 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.69 | -8.30 | 120 | 47.5 | -24.09 | -4.15 | -26.91 | 511 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.68 | -0.99 | -26.38 | 239 |
| 50 | Candlestick reversal · 1h | reversion | 90.22 | -9.79 | 116 | 31.9 | -27.10 | -5.32 | -28.91 | 514 |
| 51 | CCI reversion · 1h | reversion | 89.78 | -10.22 | 100 | 45.0 | -8.48 | -1.09 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.70 | -10.30 | 278 | 22.3 | -33.75 | -5.08 | -39.30 | 1280 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 89.05 | -10.95 | 62 | 19.4 | -7.04 | -0.77 | -19.79 | 241 |
| 55 | Donchian 20/10 · 1h | breakout | 88.82 | -11.19 | 58 | 19.0 | -0.23 | 0.18 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -13.31 | -1.53 | -28.63 | 322 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.65 | -5.15 | -36.60 | 701 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.84 | -12.16 | 101 | 13.9 | -9.16 | -1.04 | -21.49 | 336 |
| 60 | Three white soldiers | momentum | 87.72 | -12.28 | 138 | 18.1 | -48.00 | -23.19 | -48.00 | 589 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.62 | -1.29 | -23.91 | 413 |
| 63 | RSI(14) reversion | reversion | 75.13 | -24.87 | 355 | 28.7 | -72.66 | -18.15 | -72.69 | 1490 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.77 | -16.62 | -73.79 | 1668 |
| 65 | Squeeze breakout | breakout | 71.32 | -28.68 | 323 | 14.9 | -62.51 | -18.38 | -62.51 | 1232 |
| 66 | Donchian 55/20 | breakout | 70.82 | -29.18 | 327 | 18.0 | -67.60 | -14.46 | -67.60 | 1292 |
| 67 | EMA 20/50 cross | trend | 70.40 | -29.60 | 327 | 19.9 | -77.08 | -15.37 | -77.09 | 1456 |
| 68 | Volume breakout | breakout | 70.39 | -29.61 | 259 | 13.1 | -62.76 | -18.14 | -62.76 | 902 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.61 | -16.07 | -71.76 | 1433 |
| 70 | Supertrend | trend | 64.97 | -35.03 | 450 | 20.2 | -86.16 | -21.17 | -86.16 | 1913 |
| 71 | Keltner breakout | breakout | 63.34 | -36.66 | 442 | 14.5 | -83.95 | -27.93 | -83.95 | 1852 |
| 72 | Z-score reversion | reversion | 60.80 | -39.20 | 488 | 23.4 | -85.60 | -23.36 | -85.60 | 2087 |
| 73 | Ichimoku | trend | 60.64 | -39.36 | 401 | 9.7 | -81.71 | -23.38 | -81.72 | 1748 |
| 74 | AI bee: Boozy | ai | 60.55 | -39.45 | 253 | 5.1 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.35 | -39.65 | 499 | 21.6 | -87.64 | -28.43 | -87.64 | 2120 |
| 76 | AI bee: Bizzy | ai | 58.89 | -41.11 | 814 | 9.0 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.54 | -42.46 | 531 | 10.4 | -89.30 | -34.76 | -89.30 | 2118 |
| 78 | Donchian 20/10 | breakout | 56.28 | -43.72 | 624 | 18.3 | -90.87 | -26.23 | -90.87 | 2667 |
| 79 | RSI momentum | momentum | 55.51 | -44.49 | 591 | 17.3 | -90.24 | -25.66 | -90.24 | 2378 |
| 80 | Trend pullback ⏸ | trend | 55.45 | -44.55 | 581 | 15.0 | -91.02 | -27.16 | -91.02 | 2340 |
| 81 | MACD zero-line | trend | 54.99 | -45.01 | 572 | 15.0 | -91.44 | -30.03 | -91.44 | 2360 |
| 82 | Triple EMA stack | trend | 53.82 | -46.18 | 620 | 15.5 | -93.21 | -30.36 | -93.21 | 2620 |
| 83 | Bollinger breakout | breakout | 51.77 | -48.23 | 655 | 14.4 | -93.57 | -33.28 | -93.57 | 2820 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -30.63 | -98.68 | 5396 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -33.34 | -97.37 | 3547 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.51 | -36.61 | -96.51 | 3620 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -26.21 | -94.30 | 2695 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.06 | -99.35 | 5691 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.78 | -96.37 | 3623 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.69 | -99.73 | 6209 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.47 | -97.36 | 3688 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.34 | -98.48 | 4715 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.35 | -99.51 | 6147 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -33.67 | -95.87 | 3746 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.56 | -34.47 | -95.56 | 4082 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.94 | -99.90 | 8326 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T23:50 | EMA 20/50 cross | sell | BTC-USD | 17.54 | -0.12 | exit signal |
| 2026-10-10T23:47 | AI bee: Bizzy | sell | XRP-USD | 8.64 | -0.05 | Jev: sell (sell p=0.55) after 12 min |
| 2026-10-10T23:45 | MACD zero-line | sell | BTC-USD | 13.69 | -0.09 | exit signal |
| 2026-10-10T23:45 | Triple EMA stack | sell | BTC-USD | 13.40 | -0.09 | exit signal |
| 2026-10-10T23:35 | AI bee: Bizzy | buy | XRP-USD | 8.69 | — | Jev: buy (buy p=0.59) |
| 2026-10-10T23:35 | Consensus | sell | BTC-USD | 12.53 | -0.07 | target is flat |
| 2026-10-10T23:35 | Z-score reversion | buy | SOL-USD | 15.23 | — | entry signal |
| 2026-10-10T23:30 | EMA 20/50 cross | sell | SOL-USD | 17.67 | -0.13 | exit signal |
| 2026-10-10T23:25 | Consensus | buy | BTC-USD | 12.60 | — | entry |
| 2026-10-10T23:25 | Supertrend | sell | SOL-USD | 16.21 | -0.12 | exit signal |
| 2026-10-10T23:20 | Triple EMA stack | sell | SOL-USD | 13.40 | -0.10 | exit signal |
| 2026-10-10T23:15 | Consensus | sell | BTC-USD | 12.54 | -0.08 | target is flat |
| 2026-10-10T23:15 | Three white soldiers | sell | XRP-USD | 21.86 | -0.14 | exit signal |
| 2026-10-10T23:15 | Three white soldiers | sell | DOGE-USD | 21.85 | -0.16 | exit signal |
| 2026-10-10T23:15 | Donchian 20/10 | sell | SOL-USD | 13.99 | -0.11 | stop-loss |
| 2026-10-10T23:15 | MACD zero-line | sell | SOL-USD | 13.69 | -0.10 | exit signal |
| 2026-10-10T23:10 | Bollinger breakout | sell | SOL-USD | 12.87 | -0.09 | exit signal |
| 2026-10-10T23:10 | RSI momentum | sell | SOL-USD | 13.80 | -0.11 | exit signal |
| 2026-10-10T23:07 | AI bee: Bizzy | sell | SOL-USD | 8.06 | -0.05 | Jev: sell (sell p=0.75) after 12 min |
| 2026-10-10T23:05 | Consensus | buy | BTC-USD | 12.62 | — | entry |
| 2026-10-10T23:05 | Three white soldiers | buy | XRP-USD | 22.00 | — | entry signal |
| 2026-10-10T23:05 | Three white soldiers | buy | DOGE-USD | 22.00 | — | entry signal |
| 2026-10-10T23:05 | MACD zero-line | buy | BTC-USD | 13.79 | — | entry signal |
| 2026-10-10T23:00 | Candlestick reversal · 1h | sell | SOL-USD | 11.27 | 0.01 | time stop |
| 2026-10-10T23:00 | Z-score reversion | sell | BTC-USD | 15.18 | -0.09 | exit signal |
| 2026-10-10T23:00 | Supertrend | buy | BTC-USD | 16.29 | — | entry signal |
| 2026-10-10T23:00 | Triple EMA stack | buy | BTC-USD | 13.50 | — | entry signal |
| 2026-10-10T23:00 | EMA 20/50 cross | buy | BTC-USD | 17.66 | — | entry signal |
| 2026-10-10T22:55 | AI bee: Bizzy | buy | SOL-USD | 8.12 | — | Jev: buy (buy p=0.55) |
| 2026-10-10T22:55 | MFI reversion | buy | DOGE-USD | 15.10 | — | entry |
| 2026-10-10T22:55 | Z-score reversion | buy | XRP-USD | 15.27 | — | entry signal |
| 2026-10-10T22:55 | Z-score reversion | buy | DOGE-USD | 15.27 | — | entry |
| 2026-10-10T22:55 | Z-score reversion | buy | BTC-USD | 15.27 | — | entry signal |
| 2026-10-10T22:55 | RSI(14) reversion | buy | XRP-USD | 18.81 | — | entry signal |
| 2026-10-10T22:50 | Consensus | sell | BTC-USD | 12.56 | -0.09 | target is flat |
| 2026-10-10T22:50 | MFI reversion | sell | DOGE-USD | 15.01 | -0.12 | stop-loss |
| 2026-10-10T22:50 | Z-score reversion | sell | DOGE-USD | 15.18 | -0.12 | stop-loss |
| 2026-10-10T22:50 | EMA 20/50 cross | sell | BTC-USD | 17.56 | -0.13 | stop-loss |
| 2026-10-10T22:40 | Consensus | buy | BTC-USD | 12.65 | — | entry |
| 2026-10-10T22:40 | MFI reversion | buy | DOGE-USD | 15.13 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 23:55:05.000151+00:00 -> 2026-10-11 00:05:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
