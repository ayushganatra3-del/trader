# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T03:24:05.000153+00:00 · 18622 ticks

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

Today: 2535 decisions in 507 calls, $0.0355 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T03:24 | 0 / 0 / 5 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T03:24 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T03:24 | 3 / 2 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.63 | +3.96% | 6 |
| RSI momentum | IWM | 2.39 | +1.07% | 4 |
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

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
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.52 | -1.83 | -14.61 | 342 |
| 19 | Hold BTC | benchmark | 99.10 | -0.90 | 0 | — | 27.10 | 3.25 | -8.68 | 1 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -23.05 | -6.53 | -25.39 | 175 |
| 27 | EMA 20/50 cross · 1h | trend | 96.68 | -3.32 | 39 | 12.8 | 4.49 | 0.71 | -19.85 | 137 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -5.72 | -2.14 | -8.60 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -2.45 | -0.22 | -13.84 | 261 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.73 | -0.19 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.82 | -4.18 | 112 | 24.1 | -15.67 | -2.53 | -17.84 | 468 |
| 34 | Supertrend · 1h | trend | 95.15 | -4.85 | 52 | 13.5 | -0.29 | 0.15 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 93.98 | -6.02 | 36 | 25.0 | 23.88 | 3.25 | -8.85 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.90 | -2.25 | -6.77 | 103 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.32 | -1.79 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -3.62 | -0.69 | -9.03 | 151 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Ichimoku · 1h | trend | 92.92 | -7.08 | 41 | 19.5 | 0.02 | 0.20 | -20.02 | 120 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -6.78 | -1.05 | -13.62 | 415 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.75 | 0.66 | -17.07 | 223 |
| 44 | Bollinger reversion · 1h | reversion | 92.70 | -7.30 | 74 | 37.8 | -20.43 | -4.87 | -23.13 | 314 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 91.71 | -8.29 | 68 | 29.4 | 6.19 | 0.96 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.49 | -8.51 | 120 | 47.5 | -23.96 | -4.12 | -26.91 | 511 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.96 | -0.90 | -26.38 | 237 |
| 50 | Candlestick reversal · 1h | reversion | 90.22 | -9.79 | 116 | 31.9 | -27.19 | -5.32 | -29.00 | 515 |
| 51 | CCI reversion · 1h | reversion | 89.70 | -10.30 | 100 | 45.0 | -8.41 | -1.08 | -14.35 | 414 |
| 52 | VWAP momentum · 1h | momentum | 89.61 | -10.39 | 280 | 22.1 | -33.92 | -5.11 | -39.30 | 1282 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 88.97 | -11.03 | 63 | 19.0 | -7.12 | -0.78 | -19.84 | 241 |
| 55 | Donchian 20/10 · 1h | breakout | 88.79 | -11.21 | 58 | 19.0 | -0.39 | 0.16 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -13.18 | -1.52 | -28.63 | 321 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.65 | -5.15 | -36.60 | 701 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.80 | -12.20 | 102 | 13.7 | -9.15 | -1.03 | -21.49 | 338 |
| 60 | Three white soldiers | momentum | 87.47 | -12.53 | 140 | 17.9 | -48.07 | -23.33 | -48.07 | 590 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.62 | -1.29 | -23.91 | 413 |
| 63 | RSI(14) reversion | reversion | 74.75 | -25.25 | 360 | 28.3 | -72.80 | -18.28 | -72.80 | 1493 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.68 | -16.55 | -73.79 | 1667 |
| 65 | Squeeze breakout | breakout | 71.21 | -28.79 | 324 | 14.8 | -62.51 | -18.41 | -62.51 | 1232 |
| 66 | Donchian 55/20 | breakout | 70.42 | -29.58 | 330 | 17.9 | -67.45 | -14.40 | -67.45 | 1290 |
| 67 | Volume breakout | breakout | 70.28 | -29.72 | 260 | 13.1 | -62.65 | -18.06 | -62.65 | 901 |
| 68 | EMA 20/50 cross | trend | 69.99 | -30.01 | 330 | 19.7 | -77.14 | -15.43 | -77.14 | 1457 |
| 69 | VWAP reversion | reversion | 68.15 | -31.85 | 396 | 26.0 | -71.63 | -16.11 | -71.71 | 1437 |
| 70 | Supertrend | trend | 64.40 | -35.60 | 455 | 20.0 | -86.15 | -21.28 | -86.15 | 1912 |
| 71 | Keltner breakout | breakout | 63.10 | -36.90 | 444 | 14.4 | -83.75 | -27.82 | -83.75 | 1847 |
| 72 | Ichimoku | trend | 60.51 | -39.49 | 402 | 9.7 | -81.71 | -23.41 | -81.71 | 1746 |
| 73 | AI bee: Boozy | ai | 60.46 | -39.54 | 254 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 60.27 | -39.73 | 496 | 23.0 | -85.74 | -23.62 | -85.74 | 2092 |
| 75 | MFI reversion | reversion | 59.99 | -40.01 | 503 | 21.5 | -87.70 | -28.67 | -87.70 | 2122 |
| 76 | AI bee: Bizzy | ai | 58.62 | -41.38 | 819 | 8.9 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.25 | -42.75 | 534 | 10.3 | -89.37 | -35.10 | -89.37 | 2122 |
| 78 | Donchian 20/10 | breakout | 55.98 | -44.02 | 627 | 18.2 | -90.86 | -26.35 | -90.86 | 2668 |
| 79 | Trend pullback | trend | 55.35 | -44.66 | 582 | 14.9 | -90.99 | -27.04 | -90.99 | 2338 |
| 80 | RSI momentum | momentum | 55.10 | -44.90 | 595 | 17.1 | -90.32 | -25.90 | -90.32 | 2381 |
| 81 | MACD zero-line | trend | 54.39 | -45.61 | 578 | 14.9 | -91.49 | -30.40 | -91.49 | 2361 |
| 82 | Triple EMA stack | trend | 53.51 | -46.49 | 623 | 15.4 | -93.25 | -30.60 | -93.25 | 2622 |
| 83 | Bollinger breakout | breakout | 51.40 | -48.60 | 659 | 14.3 | -93.52 | -33.38 | -93.52 | 2818 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -31.37 | -98.66 | 5394 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.77 | -97.36 | 3546 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -36.66 | -96.48 | 3615 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -26.34 | -94.33 | 2699 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.54 | -99.35 | 5689 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.39 | -32.02 | -96.39 | 3626 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.04 | -99.73 | 6204 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -38.63 | -97.37 | 3687 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.71 | -98.49 | 4717 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.80 | -99.52 | 6149 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -33.91 | -95.89 | 3749 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.57 | -34.78 | -95.57 | 4082 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.71 | -99.90 | 8318 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T03:20 | MFI reversion | sell | XRP-USD | 14.95 | -0.13 | stop-loss |
| 2026-10-11T03:20 | EMA 20/50 cross | sell | ETH-USD | 17.47 | -0.13 | stop-loss |
| 2026-10-11T03:15 | MFI reversion | sell | DOGE-USD | 14.91 | -0.15 | stop-loss |
| 2026-10-11T03:15 | Donchian 55/20 | sell | ETH-USD | 17.53 | -0.14 | stop-loss |
| 2026-10-11T03:15 | Donchian 20/10 | sell | ETH-USD | 13.96 | -0.10 | exit signal |
| 2026-10-11T03:15 | Donchian 20/10 | sell | BTC-USD | 13.97 | -0.10 | stop-loss |
| 2026-10-11T03:15 | RSI momentum | sell | ETH-USD | 13.78 | -0.10 | exit signal |
| 2026-10-11T03:15 | RSI momentum | sell | BTC-USD | 13.77 | -0.10 | stop-loss |
| 2026-10-11T03:15 | Trend pullback | sell | ETH-USD | 13.76 | -0.10 | exit signal |
| 2026-10-11T03:15 | Supertrend | sell | XRP-USD | 16.05 | -0.15 | exit signal |
| 2026-10-11T03:15 | Supertrend | sell | ETH-USD | 16.10 | -0.12 | exit signal |
| 2026-10-11T03:15 | Supertrend | sell | BTC-USD | 16.11 | -0.11 | exit signal |
| 2026-10-11T03:15 | Triple EMA stack | sell | ETH-USD | 13.36 | -0.10 | exit signal |
| 2026-10-11T03:15 | Triple EMA stack | sell | BTC-USD | 13.34 | -0.10 | stop-loss |
| 2026-10-11T03:15 | EMA 20/50 cross | sell | BTC-USD | 17.45 | -0.13 | stop-loss |
| 2026-10-11T03:10 | Donchian 55/20 | sell | BTC-USD | 17.54 | -0.12 | stop-loss |
| 2026-10-11T03:10 | MACD zero-line | sell | BTC-USD | 13.65 | -0.09 | exit signal |
| 2026-10-11T03:05 | Squeeze breakout | sell | ETH-USD | 17.72 | -0.11 | exit signal |
| 2026-10-11T03:05 | Keltner breakout | sell | BTC-USD | 15.69 | -0.11 | exit signal |
| 2026-10-11T03:05 | Bollinger breakout | sell | ETH-USD | 12.86 | -0.08 | exit signal |
| 2026-10-11T03:05 | Bollinger breakout | sell | BTC-USD | 12.85 | -0.08 | exit signal |
| 2026-10-11T03:05 | RSI momentum | sell | DOGE-USD | 13.77 | -0.11 | stop-loss |
| 2026-10-11T03:05 | Supertrend | sell | DOGE-USD | 16.10 | -0.13 | exit signal |
| 2026-10-11T03:05 | MACD zero-line | sell | XRP-USD | 13.50 | -0.11 | stop-loss |
| 2026-10-11T03:05 | MACD zero-line | sell | ETH-USD | 13.67 | -0.08 | exit signal |
| 2026-10-11T03:05 | Triple EMA stack | sell | DOGE-USD | 13.33 | -0.12 | stop-loss |
| 2026-10-11T03:05 | EMA 20/50 cross | sell | DOGE-USD | 17.43 | -0.16 | stop-loss |
| 2026-10-11T03:00 | MACD zero-line · 1h | sell | SOL-USD | 21.89 | -0.22 | exit signal |
| 2026-10-11T03:00 | MACD cross · 1h | sell | SOL-USD | 5.34 | -0.03 | exit signal |
| 2026-10-11T03:00 | Donchian 20/10 | sell | DOGE-USD | 13.97 | -0.10 | exit signal |
| 2026-10-11T03:00 | MACD zero-line | sell | SOL-USD | 13.58 | -0.10 | exit signal |
| 2026-10-11T02:55 | MFI reversion | buy | DOGE-USD | 15.06 | — | entry signal |
| 2026-10-11T02:55 | ADX DI cross | sell | DOGE-USD | 14.29 | -0.09 | exit signal |
| 2026-10-11T02:45 | Keltner breakout | buy | BTC-USD | 15.80 | — | entry signal |
| 2026-10-11T02:45 | Donchian 55/20 | buy | BTC-USD | 17.66 | — | entry signal |
| 2026-10-11T02:40 | MACD zero-line | buy | XRP-USD | 13.61 | — | entry signal |
| 2026-10-11T02:40 | MACD zero-line | buy | SOL-USD | 13.68 | — | entry signal |
| 2026-10-11T02:35 | Z-score reversion | sell | XRP-USD | 15.05 | -0.06 | exit signal |
| 2026-10-11T02:35 | RSI(14) reversion | sell | XRP-USD | 18.66 | -0.07 | exit signal |
| 2026-10-11T02:35 | Donchian 55/20 | buy | ETH-USD | 17.67 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 03:24:05.000153+00:00 -> 2026-10-11 03:34:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
