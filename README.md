# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T13:25:05.000150+00:00 · 19088 ticks

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

Today: 9525 decisions in 1905 calls, $0.1332 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T13:25 | 0 / 3 / 2 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T13:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T13:25 | 0 / 5 / 0 | COIN 76% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.44 | -2.26 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -15.27 | -2.51 | -23.22 | 71 |
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
| 18 | Hold BTC | benchmark | 99.29 | -0.71 | 0 | — | 27.87 | 3.33 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.41 | -1.80 | -14.61 | 340 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -23.00 | -6.51 | -25.39 | 173 |
| 27 | EMA 20/50 cross · 1h | trend | 96.71 | -3.29 | 39 | 12.8 | 5.24 | 0.79 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.98 | -2.38 | -9.70 | 258 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.65 | -0.09 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.82 | -0.21 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.79 | -4.21 | 113 | 23.9 | -15.03 | -2.41 | -17.27 | 464 |
| 34 | Supertrend · 1h | trend | 95.07 | -4.93 | 53 | 13.2 | 0.14 | 0.21 | -18.22 | 209 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.90 | -2.25 | -6.77 | 103 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.85 | -6.15 | 37 | 24.3 | 23.00 | 3.15 | -8.95 | 108 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.00 | -1.56 | -17.79 | 128 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -1.95 | -0.32 | -9.03 | 148 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -2.56 | -0.30 | -13.31 | 411 |
| 42 | Ichimoku · 1h | trend | 92.81 | -7.19 | 42 | 19.0 | -0.09 | 0.19 | -20.11 | 120 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 5.03 | 0.81 | -17.07 | 220 |
| 44 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 45 | Bollinger reversion · 1h | reversion | 92.50 | -7.50 | 76 | 36.8 | -20.81 | -4.97 | -23.18 | 317 |
| 46 | Bollinger breakout · 1h | breakout | 91.61 | -8.39 | 70 | 28.6 | 5.73 | 0.91 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.13 | -8.87 | 123 | 46.3 | -24.03 | -4.14 | -26.91 | 511 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.08 | -0.91 | -26.38 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.13 | -9.87 | 116 | 31.9 | -26.39 | -5.15 | -28.18 | 512 |
| 51 | CCI reversion · 1h | reversion | 89.56 | -10.44 | 101 | 44.6 | -7.75 | -0.98 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.46 | -10.54 | 283 | 21.9 | -33.38 | -5.01 | -39.30 | 1280 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 88.84 | -11.15 | 64 | 18.8 | -6.63 | -0.72 | -19.96 | 239 |
| 55 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.74 | -1.46 | -28.63 | 320 |
| 56 | Donchian 20/10 · 1h | breakout | 88.74 | -11.26 | 59 | 18.6 | -0.68 | 0.12 | -17.72 | 224 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.43 | -5.10 | -36.60 | 700 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.78 | -12.22 | 103 | 13.6 | -9.95 | -1.15 | -21.61 | 340 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.05 | -23.30 | -48.07 | 590 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.34 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.93 | -1.34 | -23.91 | 413 |
| 63 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.68 | -16.55 | -73.79 | 1667 |
| 64 | RSI(14) reversion | reversion | 73.91 | -26.09 | 369 | 27.6 | -72.64 | -18.30 | -72.65 | 1493 |
| 65 | Squeeze breakout | breakout | 70.69 | -29.31 | 328 | 14.6 | -62.50 | -18.47 | -62.50 | 1231 |
| 66 | Donchian 55/20 | breakout | 70.16 | -29.84 | 332 | 17.8 | -67.57 | -14.46 | -67.57 | 1292 |
| 67 | Volume breakout | breakout | 70.06 | -29.94 | 262 | 13.0 | -62.70 | -18.11 | -62.72 | 902 |
| 68 | EMA 20/50 cross | trend | 69.30 | -30.70 | 334 | 19.5 | -77.23 | -15.52 | -77.23 | 1461 |
| 69 | VWAP reversion | reversion | 67.81 | -32.19 | 402 | 25.9 | -71.48 | -16.12 | -71.53 | 1434 |
| 70 | Supertrend | trend | 63.40 | -36.60 | 462 | 19.7 | -86.16 | -21.30 | -86.19 | 1916 |
| 71 | Keltner breakout | breakout | 62.33 | -37.67 | 451 | 14.2 | -83.80 | -27.94 | -83.80 | 1849 |
| 72 | AI bee: Boozy | ai | 60.38 | -39.62 | 255 | 5.1 | — | — | — | — |
| 73 | Ichimoku | trend | 60.07 | -39.93 | 406 | 9.6 | -81.79 | -23.54 | -81.79 | 1749 |
| 74 | Z-score reversion | reversion | 59.36 | -40.64 | 508 | 22.4 | -85.36 | -23.32 | -85.36 | 2082 |
| 75 | MFI reversion | reversion | 59.15 | -40.84 | 514 | 21.2 | -87.59 | -28.79 | -87.59 | 2121 |
| 76 | AI bee: Bizzy | ai | 57.85 | -42.15 | 833 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.23 | -43.77 | 544 | 10.1 | -89.34 | -35.61 | -89.34 | 2121 |
| 78 | Trend pullback | trend | 55.12 | -44.88 | 584 | 14.9 | -90.99 | -27.12 | -90.99 | 2339 |
| 79 | Donchian 20/10 | breakout | 54.81 | -45.19 | 638 | 17.9 | -90.87 | -26.48 | -90.87 | 2668 |
| 80 | RSI momentum | momentum | 53.70 | -46.30 | 608 | 16.8 | -90.39 | -26.02 | -90.39 | 2386 |
| 81 | MACD zero-line | trend | 52.90 | -47.10 | 594 | 14.5 | -91.59 | -30.65 | -91.59 | 2369 |
| 82 | Triple EMA stack | trend | 52.86 | -47.13 | 629 | 15.3 | -93.21 | -30.51 | -93.21 | 2620 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -31.70 | -98.68 | 5404 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -34.28 | -97.39 | 3552 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.46 | -36.53 | -96.46 | 3613 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.23 | -26.00 | -94.23 | 2687 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -38.12 | -99.35 | 5699 |
| 88 | Bollinger breakout | breakout | 50.26 | -49.74 | 672 | 14.0 | -93.56 | -33.63 | -93.56 | 2820 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -32.03 | -96.38 | 3625 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.43 | -99.73 | 6210 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -38.45 | -97.35 | 3686 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -38.11 | -98.46 | 4715 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.34 | -99.52 | 6155 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -34.48 | -95.88 | 3749 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.61 | -35.14 | -95.61 | 4089 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.62 | -99.90 | 8319 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T13:25 | EMA 20/50 cross | buy | DOGE-USD | 17.34 | — | entry signal |
| 2026-10-11T13:20 | Trend pullback | buy | BTC-USD | 13.79 | — | entry signal |
| 2026-10-11T13:15 | ADX DI cross | buy | ETH-USD | 14.07 | — | entry signal |
| 2026-10-11T13:15 | Triple EMA stack | buy | ETH-USD | 13.23 | — | entry signal |
| 2026-10-11T13:10 | Donchian 20/10 | sell | DOGE-USD | 13.68 | -0.11 | target is flat |
| 2026-10-11T13:10 | Triple EMA stack | sell | BTC-USD | 10.59 | -0.07 | exit signal |
| 2026-10-11T13:05 | Bollinger breakout | sell | XRP-USD | 10.06 | -0.07 | exit signal |
| 2026-10-11T13:05 | Donchian 55/20 | sell | ETH-USD | 17.44 | -0.14 | stop-loss |
| 2026-10-11T13:05 | Donchian 20/10 | sell | ETH-USD | 10.96 | -0.08 | exit signal |
| 2026-10-11T13:05 | Donchian 20/10 | sell | BTC-USD | 10.96 | -0.08 | exit signal |
| 2026-10-11T13:05 | RSI momentum | sell | DOGE-USD | 13.40 | -0.11 | exit signal |
| 2026-10-11T13:05 | RSI momentum | sell | BTC-USD | 10.74 | -0.06 | exit signal |
| 2026-10-11T13:05 | Trend pullback | sell | BTC-USD | 13.72 | -0.09 | exit signal |
| 2026-10-11T13:05 | Supertrend | buy | XRP-USD | 6.28 | — | rebalance up |
| 2026-10-11T13:05 | Supertrend | buy | SOL-USD | 3.19 | — | rebalance up |
| 2026-10-11T13:05 | Supertrend | buy | ETH-USD | 3.17 | — | rebalance up |
| 2026-10-11T13:05 | Supertrend | buy | DOGE-USD | 3.19 | — | rebalance up |
| 2026-10-11T13:05 | Supertrend | sell | BTC-USD | 12.66 | -0.07 | exit signal |
| 2026-10-11T13:05 | Triple EMA stack | sell | ETH-USD | 13.22 | -0.10 | stop-loss |
| 2026-10-11T13:05 | Triple EMA stack | sell | DOGE-USD | 13.20 | -0.11 | stop-loss |
| 2026-10-11T13:05 | EMA 20/50 cross | sell | ETH-USD | 13.86 | -0.11 | stop-loss |
| 2026-10-11T13:05 | EMA 20/50 cross | sell | DOGE-USD | 17.29 | -0.15 | stop-loss |
| 2026-10-11T13:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.69 | — | entry signal |
| 2026-10-11T12:55 | Keltner breakout | sell | XRP-USD | 12.48 | -0.08 | exit signal |
| 2026-10-11T12:55 | Donchian 20/10 | buy | DOGE-USD | 2.75 | — | rebalance up |
| 2026-10-11T12:55 | Donchian 20/10 | sell | SOL-USD | 10.95 | -0.09 | stop-loss |
| 2026-10-11T12:55 | Triple EMA stack | buy | XRP-USD | 10.58 | — | rebalance up |
| 2026-10-11T12:55 | Triple EMA stack | sell | SOL-USD | 13.21 | -0.10 | exit signal |
| 2026-10-11T12:50 | Squeeze breakout | sell | ETH-USD | 17.59 | -0.11 | exit signal |
| 2026-10-11T12:50 | Keltner breakout | sell | ETH-USD | 15.58 | -0.11 | exit signal |
| 2026-10-11T12:50 | Keltner breakout | sell | BTC-USD | 12.49 | -0.08 | stop-loss |
| 2026-10-11T12:50 | Bollinger breakout | sell | ETH-USD | 10.06 | -0.06 | exit signal |
| 2026-10-11T12:50 | Bollinger breakout | sell | BTC-USD | 10.06 | -0.06 | stop-loss |
| 2026-10-11T12:50 | RSI momentum | buy | XRP-USD | 5.37 | — | rebalance up |
| 2026-10-11T12:50 | RSI momentum | buy | ETH-USD | 2.69 | — | rebalance up |
| 2026-10-11T12:50 | RSI momentum | buy | DOGE-USD | 2.71 | — | rebalance up |
| 2026-10-11T12:50 | RSI momentum | sell | SOL-USD | 10.72 | -0.08 | exit signal |
| 2026-10-11T12:50 | Ichimoku | sell | SOL-USD | 14.95 | -0.12 | exit signal |
| 2026-10-11T12:50 | MACD zero-line | sell | XRP-USD | 13.21 | -0.09 | exit signal |
| 2026-10-11T12:50 | EMA 20/50 cross | buy | XRP-USD | 6.94 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 13:25:05.000150+00:00 -> 2026-10-11 13:35:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
