# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T04:25:05.000182+00:00 · 17497 ticks

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

Today: 3495 decisions in 699 calls, $0.0489 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T04:25 | 0 / 4 / 1 | NANC 17%, COIN 14% |  |
| Breezy | 2026-10-10T04:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T04:25 | 1 / 4 / 0 | COIN 75% |  |

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
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.31 | 2.48 | -1.52 | 90 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.33 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 88 | 55.7 | -10.84 | -2.10 | -14.99 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.78 | -1.22 | 0 | — | 27.21 | 3.27 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.26 | -2.74 | 40 | 45.0 | 1.54 | 0.43 | -8.60 | 162 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.38 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.56 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 1.17 | 0.38 | -8.88 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.87 | -0.13 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.86 | -4.14 | 108 | 23.1 | -16.07 | -2.60 | -17.97 | 471 |
| 34 | Supertrend · 1h | trend | 95.15 | -4.85 | 52 | 13.5 | -0.21 | 0.17 | -18.22 | 211 |
| 35 | Squeeze breakout · 1h | breakout | 94.22 | -5.78 | 35 | 25.7 | 24.20 | 3.29 | -8.65 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.45 | -1.97 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -3.22 | -0.60 | -9.03 | 153 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -4.82 | -0.79 | -13.04 | 404 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.84 | -4.98 | -23.70 | 319 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.66 | 0.65 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.94 | -8.06 | 67 | 29.9 | 6.62 | 1.01 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.81 | -8.19 | 117 | 48.7 | -25.06 | -4.32 | -27.31 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.27 | -0.94 | -26.38 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.25 | -9.75 | 114 | 30.7 | -28.18 | -5.57 | -29.98 | 522 |
| 51 | CCI reversion · 1h | reversion | 89.76 | -10.24 | 98 | 44.9 | -9.26 | -1.21 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.75 | -10.25 | 277 | 22.0 | -35.61 | -5.40 | -39.28 | 1285 |
| 53 | MACD zero-line · 1h | trend | 89.41 | -10.59 | 60 | 20.0 | -6.27 | -0.66 | -19.50 | 240 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Three white soldiers | momentum | 88.94 | -11.06 | 130 | 19.2 | -47.82 | -23.32 | -47.91 | 587 |
| 56 | Donchian 20/10 · 1h | breakout | 88.86 | -11.14 | 58 | 19.0 | -0.02 | 0.20 | -17.72 | 221 |
| 57 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.30 | -1.40 | -28.47 | 318 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.24 | -5.26 | -36.60 | 702 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.85 | -12.15 | 101 | 13.9 | -9.50 | -1.08 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.44 | -1.27 | -23.88 | 413 |
| 63 | RSI(14) reversion | reversion | 75.51 | -24.49 | 352 | 29.0 | -72.83 | -18.23 | -72.99 | 1495 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.04 | -16.74 | -73.92 | 1666 |
| 65 | Squeeze breakout | breakout | 73.45 | -26.55 | 305 | 15.7 | -61.73 | -18.32 | -61.75 | 1220 |
| 66 | Donchian 55/20 | breakout | 72.46 | -27.54 | 314 | 18.5 | -67.67 | -14.49 | -68.07 | 1295 |
| 67 | EMA 20/50 cross | trend | 72.10 | -27.90 | 309 | 20.4 | -77.29 | -15.41 | -77.44 | 1463 |
| 68 | Volume breakout | breakout | 71.34 | -28.66 | 251 | 13.5 | -63.45 | -18.35 | -63.53 | 906 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.77 | -16.16 | -71.91 | 1437 |
| 70 | Supertrend | trend | 66.19 | -33.81 | 436 | 20.6 | -86.45 | -21.29 | -86.48 | 1927 |
| 71 | Keltner breakout | breakout | 64.92 | -35.08 | 427 | 15.0 | -84.28 | -28.13 | -84.43 | 1865 |
| 72 | Ichimoku | trend | 61.77 | -38.23 | 388 | 10.1 | -81.86 | -23.71 | -81.86 | 1754 |
| 73 | Z-score reversion | reversion | 61.41 | -38.59 | 483 | 23.6 | -85.73 | -23.53 | -85.74 | 2095 |
| 74 | MFI reversion | reversion | 61.30 | -38.70 | 487 | 22.2 | -87.71 | -28.58 | -87.72 | 2123 |
| 75 | AI bee: Boozy | ai | 61.06 | -38.94 | 248 | 5.2 | — | — | — | — |
| 76 | AI bee: Bizzy | ai | 60.83 | -39.17 | 777 | 9.4 | — | — | — | — |
| 77 | ADX DI cross | trend | 58.59 | -41.41 | 519 | 10.6 | -89.61 | -34.81 | -89.61 | 2134 |
| 78 | Donchian 20/10 | breakout | 58.55 | -41.45 | 601 | 19.0 | -90.84 | -26.36 | -90.84 | 2666 |
| 79 | Trend pullback | trend | 58.41 | -41.59 | 545 | 16.0 | -90.40 | -27.19 | -90.40 | 2300 |
| 80 | RSI momentum | momentum | 57.61 | -42.39 | 566 | 17.8 | -90.31 | -25.89 | -90.31 | 2383 |
| 81 | MACD zero-line | trend | 57.02 | -42.98 | 548 | 15.7 | -91.54 | -29.86 | -91.54 | 2362 |
| 82 | Triple EMA stack | trend | 56.67 | -43.33 | 584 | 16.3 | -93.09 | -30.67 | -93.09 | 2612 |
| 83 | Bollinger breakout | breakout | 54.02 | -45.98 | 627 | 15.0 | -93.57 | -33.68 | -93.57 | 2822 |
| 84 | Consensus | meta | 52.37 | -47.63 | 594 | 10.3 | -94.23 | -25.93 | -94.23 | 2688 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.87 | -98.69 | 5393 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -33.40 | -97.35 | 3543 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -37.14 | -96.44 | 3610 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.97 | -99.34 | 5687 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.18 | -31.88 | -96.18 | 3585 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.98 | -99.73 | 6208 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -39.26 | -97.34 | 3682 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.51 | -98.47 | 4715 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.62 | -99.51 | 6150 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -33.73 | -95.84 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.56 | -34.68 | -95.56 | 4082 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.08 | -99.90 | 8346 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T04:25 | AI bee: Bizzy | sell | BTC-USD | 8.85 | -0.06 | Jev: sell (sell p=0.84) after 11 min |
| 2026-10-10T04:25 | Ichimoku | buy | SOL-USD | 15.48 | — | entry signal |
| 2026-10-10T04:25 | Ichimoku | buy | ETH-USD | 15.48 | — | entry signal |
| 2026-10-10T04:25 | Ichimoku | buy | DOGE-USD | 15.48 | — | entry signal |
| 2026-10-10T04:22 | AI bee: Bizzy | sell | ETH-USD | 8.74 | -0.05 | Jev: sell (sell p=0.58) after 20 min |
| 2026-10-10T04:20 | Consensus | sell | DOGE-USD | 13.05 | -0.08 | target is flat |
| 2026-10-10T04:20 | Keltner breakout | sell | DOGE-USD | 16.14 | -0.12 | stop-loss |
| 2026-10-10T04:20 | Bollinger breakout | sell | SOL-USD | 13.46 | -0.11 | exit signal |
| 2026-10-10T04:20 | Donchian 20/10 | sell | DOGE-USD | 14.55 | -0.11 | stop-loss |
| 2026-10-10T04:20 | Supertrend | buy | XRP-USD | 3.31 | — | rebalance up |
| 2026-10-10T04:20 | Supertrend | sell | ETH-USD | 3.31 | -0.01 | rebalance down |
| 2026-10-10T04:18 | AI bee: Bizzy | sell | DOGE-USD | 8.94 | -0.08 | Jev: sell (sell p=0.88) after 11 min |
| 2026-10-10T04:15 | Bollinger breakout | sell | DOGE-USD | 13.45 | -0.09 | exit signal |
| 2026-10-10T04:15 | Ichimoku | sell | DOGE-USD | 15.38 | -0.13 | exit signal |
| 2026-10-10T04:15 | EMA 20/50 cross | buy | BTC-USD | 3.60 | — | rebalance up |
| 2026-10-10T04:15 | EMA 20/50 cross | sell | SOL-USD | 3.60 | -0.01 | rebalance down |
| 2026-10-10T04:14 | AI bee: Bizzy | buy | BTC-USD | 8.90 | — | Jev: buy (buy p=0.58) |
| 2026-10-10T04:13 | AI bee: Bizzy | sell | XRP-USD | 8.37 | -0.06 | Jev: sell (sell p=0.77) after 10 min |
| 2026-10-10T04:10 | Consensus | buy | XRP-USD | 13.12 | — | entry |
| 2026-10-10T04:10 | Keltner breakout | buy | DOGE-USD | 16.26 | — | entry |
| 2026-10-10T04:10 | Bollinger breakout | buy | DOGE-USD | 13.54 | — | entry |
| 2026-10-10T04:10 | Donchian 20/10 | buy | DOGE-USD | 14.67 | — | entry |
| 2026-10-10T04:10 | MACD zero-line | buy | XRP-USD | 14.29 | — | entry signal |
| 2026-10-10T04:10 | MACD zero-line | buy | ETH-USD | 14.29 | — | entry signal |
| 2026-10-10T04:10 | MACD zero-line | buy | BTC-USD | 14.29 | — | entry signal |
| 2026-10-10T04:10 | Triple EMA stack | buy | XRP-USD | 8.43 | — | entry signal |
| 2026-10-10T04:10 | Triple EMA stack | buy | ETH-USD | 11.36 | — | entry signal |
| 2026-10-10T04:10 | Triple EMA stack | buy | BTC-USD | 11.36 | — | entry signal |
| 2026-10-10T04:10 | EMA 20/50 cross | buy | BTC-USD | 7.06 | — | entry signal |
| 2026-10-10T04:07 | AI bee: Bizzy | buy | DOGE-USD | 9.03 | — | Jev: buy (buy p=0.59) |
| 2026-10-10T04:05 | Bollinger breakout | buy | SOL-USD | 13.57 | — | entry signal |
| 2026-10-10T04:05 | Bollinger breakout | buy | BTC-USD | 13.57 | — | entry signal |
| 2026-10-10T04:05 | RSI momentum | buy | XRP-USD | 11.39 | — | entry signal |
| 2026-10-10T04:05 | RSI momentum | buy | SOL-USD | 11.57 | — | entry signal |
| 2026-10-10T04:05 | RSI momentum | buy | ETH-USD | 11.57 | — | entry signal |
| 2026-10-10T04:05 | RSI momentum | buy | BTC-USD | 11.57 | — | entry signal |
| 2026-10-10T04:05 | Trend pullback | buy | XRP-USD | 14.64 | — | entry signal |
| 2026-10-10T04:05 | Trend pullback | buy | ETH-USD | 14.64 | — | entry signal |
| 2026-10-10T04:05 | Ichimoku | buy | DOGE-USD | 15.51 | — | entry signal |
| 2026-10-10T04:05 | Supertrend | buy | XRP-USD | 9.82 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 04:25:05.000182+00:00 -> 2026-10-10 04:35:05.000182+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
