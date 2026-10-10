# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T06:25:05.000150+00:00 · 17593 ticks

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

Today: 4935 decisions in 987 calls, $0.0690 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T06:25 | 2 / 2 / 1 | NANC 17%, COIN 14% |  |
| Breezy | 2026-10-10T06:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T06:25 | 3 / 2 / 0 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.14 | +1.01% | 5 |
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
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -13.60 | -2.18 | -22.02 | 69 |
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
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.31 | 2.48 | -1.52 | 90 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.30 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.19 | -0.81 | 88 | 55.7 | -10.91 | -2.12 | -15.02 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.94 | -1.06 | 0 | — | 27.32 | 3.28 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.24 | -2.76 | 41 | 43.9 | 1.53 | 0.43 | -8.60 | 162 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.59 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 0.51 | 0.23 | -8.66 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.84 | -0.12 | -13.84 | 257 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.88 | -4.12 | 108 | 23.1 | -16.27 | -2.64 | -17.97 | 473 |
| 34 | Supertrend · 1h | trend | 95.23 | -4.77 | 52 | 13.5 | -0.15 | 0.17 | -18.22 | 211 |
| 35 | Squeeze breakout · 1h | breakout | 94.21 | -5.79 | 35 | 25.7 | 24.17 | 3.29 | -8.65 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.72 | -2.03 | -17.79 | 128 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -3.28 | -0.61 | -9.03 | 153 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | 0.11 | 0.17 | -12.68 | 409 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.87 | -4.99 | -23.56 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.08 | 0.70 | -17.07 | 222 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.93 | -8.07 | 67 | 29.9 | 6.60 | 1.01 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.80 | -8.21 | 119 | 47.9 | -25.11 | -4.33 | -27.32 | 513 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.64 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.29 | -9.71 | 114 | 30.7 | -28.56 | -5.62 | -30.37 | 522 |
| 51 | CCI reversion · 1h | reversion | 89.78 | -10.22 | 98 | 44.9 | -9.17 | -1.20 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.74 | -10.26 | 277 | 22.0 | -35.64 | -5.40 | -39.27 | 1286 |
| 53 | MACD zero-line · 1h | trend | 89.47 | -10.54 | 60 | 20.0 | -6.25 | -0.66 | -19.50 | 240 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Three white soldiers | momentum | 88.94 | -11.06 | 130 | 19.2 | -47.69 | -23.18 | -47.77 | 587 |
| 56 | Donchian 20/10 · 1h | breakout | 88.86 | -11.14 | 58 | 19.0 | 0.01 | 0.21 | -17.72 | 221 |
| 57 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -11.98 | -1.35 | -28.47 | 318 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.20 | -5.25 | -36.59 | 702 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.86 | -12.14 | 101 | 13.9 | -9.44 | -1.07 | -21.49 | 338 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.74 | -1.31 | -24.14 | 412 |
| 63 | RSI(14) reversion | reversion | 75.51 | -24.49 | 352 | 29.0 | -72.80 | -18.21 | -72.96 | 1494 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.06 | -16.75 | -73.94 | 1668 |
| 65 | Squeeze breakout | breakout | 73.14 | -26.86 | 307 | 15.6 | -61.86 | -18.41 | -61.86 | 1222 |
| 66 | EMA 20/50 cross | trend | 72.20 | -27.80 | 309 | 20.4 | -77.15 | -15.32 | -77.35 | 1459 |
| 67 | Donchian 55/20 | breakout | 72.16 | -27.84 | 315 | 18.4 | -67.74 | -14.55 | -68.00 | 1297 |
| 68 | Volume breakout | breakout | 71.23 | -28.77 | 252 | 13.5 | -63.28 | -18.40 | -63.30 | 902 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.84 | -16.16 | -71.98 | 1437 |
| 70 | Supertrend | trend | 66.29 | -33.71 | 436 | 20.6 | -86.33 | -21.16 | -86.38 | 1923 |
| 71 | Keltner breakout | breakout | 64.58 | -35.42 | 429 | 14.9 | -84.25 | -28.39 | -84.32 | 1863 |
| 72 | Ichimoku | trend | 61.46 | -38.54 | 392 | 9.9 | -81.80 | -23.68 | -81.80 | 1751 |
| 73 | Z-score reversion | reversion | 61.41 | -38.59 | 483 | 23.6 | -85.72 | -23.52 | -85.73 | 2094 |
| 74 | MFI reversion | reversion | 61.17 | -38.83 | 490 | 22.0 | -87.70 | -28.57 | -87.70 | 2120 |
| 75 | AI bee: Boozy | ai | 61.06 | -38.94 | 248 | 5.2 | — | — | — | — |
| 76 | AI bee: Bizzy | ai | 60.53 | -39.47 | 782 | 9.3 | — | — | — | — |
| 77 | ADX DI cross | trend | 58.58 | -41.42 | 520 | 10.6 | -89.55 | -34.67 | -89.56 | 2131 |
| 78 | Trend pullback | trend | 58.36 | -41.64 | 546 | 15.9 | -90.37 | -27.08 | -90.38 | 2299 |
| 79 | Donchian 20/10 | breakout | 58.26 | -41.74 | 603 | 18.9 | -90.85 | -26.46 | -90.85 | 2667 |
| 80 | RSI momentum | momentum | 57.54 | -42.46 | 568 | 18.0 | -90.26 | -25.84 | -90.27 | 2380 |
| 81 | MACD zero-line | trend | 56.97 | -43.03 | 550 | 15.6 | -91.55 | -29.89 | -91.55 | 2362 |
| 82 | Triple EMA stack | trend | 56.40 | -43.60 | 588 | 16.3 | -93.13 | -30.88 | -93.14 | 2615 |
| 83 | Bollinger breakout | breakout | 53.66 | -46.34 | 632 | 14.9 | -93.58 | -33.88 | -93.58 | 2822 |
| 84 | Consensus | meta | 52.07 | -47.93 | 598 | 10.2 | -94.24 | -26.01 | -94.24 | 2686 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -30.78 | -98.69 | 5394 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -33.47 | -97.34 | 3541 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -37.22 | -96.42 | 3610 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.96 | -99.34 | 5691 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.14 | -31.53 | -96.14 | 3582 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.06 | -99.73 | 6206 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -39.31 | -97.34 | 3681 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.51 | -98.47 | 4715 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.66 | -99.51 | 6150 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -33.73 | -95.84 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.56 | -34.76 | -95.56 | 4084 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.40 | -99.90 | 8346 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T06:15 | Squeeze breakout | sell | ETH-USD | 18.23 | -0.13 | exit signal |
| 2026-10-10T06:15 | Bollinger breakout | sell | ETH-USD | 13.39 | -0.09 | exit signal |
| 2026-10-10T06:15 | Donchian 20/10 | sell | XRP-USD | 14.52 | -0.10 | exit signal |
| 2026-10-10T06:15 | Donchian 20/10 | sell | SOL-USD | 14.52 | -0.11 | exit signal |
| 2026-10-10T06:15 | RSI momentum | buy | SOL-USD | 3.14 | — | rebalance up |
| 2026-10-10T06:15 | RSI momentum | sell | DOGE-USD | 11.67 | 0.10 | exit signal |
| 2026-10-10T06:15 | Trend pullback | buy | BTC-USD | 5.83 | — | rebalance up |
| 2026-10-10T06:15 | Trend pullback | sell | DOGE-USD | 11.64 | -0.08 | exit signal |
| 2026-10-10T06:15 | MACD zero-line | sell | ETH-USD | 14.22 | -0.08 | exit signal |
| 2026-10-10T06:15 | Triple EMA stack | sell | DOGE-USD | 8.47 | -0.06 | exit signal |
| 2026-10-10T06:10 | Consensus | sell | XRP-USD | 13.03 | -0.05 | target is flat |
| 2026-10-10T06:05 | Consensus | sell | SOL-USD | 12.98 | -0.08 | target is flat |
| 2026-10-10T06:05 | Consensus | sell | DOGE-USD | 12.99 | -0.08 | target is flat |
| 2026-10-10T06:05 | Volume breakout | sell | ETH-USD | 17.73 | -0.11 | exit signal |
| 2026-10-10T06:05 | Squeeze breakout | sell | SOL-USD | 18.24 | -0.12 | stop-loss |
| 2026-10-10T06:05 | Keltner breakout | sell | XRP-USD | 16.09 | -0.14 | stop-loss |
| 2026-10-10T06:05 | Keltner breakout | sell | SOL-USD | 16.08 | -0.15 | stop-loss |
| 2026-10-10T06:05 | Bollinger breakout | sell | XRP-USD | 10.72 | -0.06 | stop-loss |
| 2026-10-10T06:05 | Bollinger breakout | sell | SOL-USD | 10.72 | -0.07 | stop-loss |
| 2026-10-10T06:05 | Donchian 55/20 | sell | SOL-USD | 17.68 | -0.16 | stop-loss |
| 2026-10-10T06:05 | Trend pullback | buy | BTC-USD | 2.91 | — | rebalance up |
| 2026-10-10T06:05 | Trend pullback | sell | ETH-USD | 2.91 | -0.02 | rebalance down |
| 2026-10-10T06:05 | Ichimoku | sell | SOL-USD | 15.33 | -0.08 | exit signal |
| 2026-10-10T06:05 | Ichimoku | sell | DOGE-USD | 15.29 | -0.13 | exit signal |
| 2026-10-10T06:00 | Z-score reversion · 1h | buy | SOL-USD | 5.11 | — | rebalance up |
| 2026-10-10T06:00 | Z-score reversion · 1h | sell | ETH-USD | 8.68 | -0.03 | exit signal |
| 2026-10-10T06:00 | MACD cross · 1h | buy | BTC-USD | 2.53 | — | entry signal |
| 2026-10-10T05:57 | AI bee: Bizzy | sell | DOGE-USD | 9.00 | -0.06 | Jev: sell (sell p=0.77) after 10 min |
| 2026-10-10T05:50 | Bollinger breakout | sell | DOGE-USD | 5.38 | -0.03 | target is flat |
| 2026-10-10T05:49 | AI bee: Bizzy | sell | XRP-USD | 9.02 | -0.06 | Jev: sell (sell p=0.77) after 10 min |
| 2026-10-10T05:47 | AI bee: Bizzy | buy | DOGE-USD | 9.06 | — | Jev: buy (buy p=0.60) |
| 2026-10-10T05:45 | Consensus | buy | BTC-USD | 13.08 | — | entry |
| 2026-10-10T05:45 | Squeeze breakout | buy | ETH-USD | 18.36 | — | entry signal |
| 2026-10-10T05:45 | Squeeze breakout | buy | BTC-USD | 18.36 | — | entry signal |
| 2026-10-10T05:45 | Bollinger breakout | buy | DOGE-USD | 5.41 | — | entry signal |
| 2026-10-10T05:45 | Bollinger breakout | sell | XRP-USD | 2.72 | -0.01 | rebalance down |
| 2026-10-10T05:45 | Bollinger breakout | sell | SOL-USD | 2.70 | -0.01 | rebalance down |
| 2026-10-10T05:44 | AI bee: Bizzy | sell | SOL-USD | 8.75 | -0.04 | Jev: sell (sell p=0.51) after 11 min |
| 2026-10-10T05:40 | Keltner breakout | buy | XRP-USD | 16.23 | — | entry signal |
| 2026-10-10T05:40 | Keltner breakout | buy | SOL-USD | 16.23 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 06:25:05.000150+00:00 -> 2026-10-10 06:35:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
