# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T05:55:05.000190+00:00 · 17571 ticks

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

Today: 4605 decisions in 921 calls, $0.0644 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T05:55 | 0 / 3 / 2 | DOGE-USD 15%, NANC 17%, COIN 14% |  |
| Breezy | 2026-10-10T05:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T05:55 | 1 / 3 / 1 | COIN 75% |  |

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
| 18 | Stochastic reversion · 1h | reversion | 99.19 | -0.81 | 88 | 55.7 | -10.88 | -2.11 | -14.99 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.92 | -1.08 | 0 | — | 27.27 | 3.27 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.31 | -2.69 | 40 | 45.0 | 1.60 | 0.44 | -8.60 | 162 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.56 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 1.17 | 0.38 | -8.88 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.41 | -0.06 | -13.84 | 256 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.93 | -4.07 | 108 | 23.1 | -16.02 | -2.59 | -17.97 | 471 |
| 34 | Supertrend · 1h | trend | 95.26 | -4.74 | 52 | 13.5 | -0.10 | 0.18 | -18.22 | 211 |
| 35 | Squeeze breakout · 1h | breakout | 94.29 | -5.71 | 35 | 25.7 | 24.29 | 3.30 | -8.65 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.43 | -1.96 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.07 | -0.34 | -9.03 | 149 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -1.36 | -0.10 | -11.88 | 410 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.80 | -4.97 | -23.49 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.73 | 0.65 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 92.01 | -7.99 | 67 | 29.9 | 6.70 | 1.02 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.79 | -8.21 | 119 | 47.9 | -25.07 | -4.32 | -27.27 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.29 | -0.94 | -26.38 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.31 | -9.69 | 114 | 30.7 | -26.99 | -5.32 | -28.88 | 516 |
| 51 | CCI reversion · 1h | reversion | 89.79 | -10.21 | 98 | 44.9 | -9.22 | -1.21 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.77 | -10.23 | 277 | 22.0 | -35.57 | -5.39 | -39.28 | 1287 |
| 53 | MACD zero-line · 1h | trend | 89.58 | -10.42 | 60 | 20.0 | -6.06 | -0.63 | -19.50 | 240 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Three white soldiers | momentum | 88.94 | -11.06 | 130 | 19.2 | -47.74 | -23.25 | -47.82 | 586 |
| 56 | Donchian 20/10 · 1h | breakout | 88.88 | -11.12 | 58 | 19.0 | 0.07 | 0.22 | -17.72 | 221 |
| 57 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.30 | -1.40 | -28.47 | 318 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.18 | -5.24 | -36.60 | 702 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.88 | -12.12 | 101 | 13.9 | -9.16 | -1.04 | -21.49 | 336 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.44 | -1.27 | -23.88 | 413 |
| 63 | RSI(14) reversion | reversion | 75.51 | -24.49 | 352 | 29.0 | -72.80 | -18.21 | -72.96 | 1494 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.04 | -16.74 | -73.92 | 1666 |
| 65 | Squeeze breakout | breakout | 73.28 | -26.72 | 305 | 15.7 | -61.80 | -18.36 | -61.80 | 1222 |
| 66 | Donchian 55/20 | breakout | 72.33 | -27.67 | 314 | 18.5 | -67.67 | -14.50 | -68.00 | 1297 |
| 67 | EMA 20/50 cross | trend | 72.30 | -27.70 | 309 | 20.4 | -77.16 | -15.32 | -77.37 | 1460 |
| 68 | Volume breakout | breakout | 71.29 | -28.71 | 251 | 13.5 | -63.27 | -18.38 | -63.32 | 903 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.74 | -16.14 | -71.89 | 1436 |
| 70 | Supertrend | trend | 66.37 | -33.63 | 436 | 20.6 | -86.37 | -21.19 | -86.44 | 1925 |
| 71 | Keltner breakout | breakout | 64.73 | -35.27 | 427 | 15.0 | -84.20 | -28.31 | -84.31 | 1863 |
| 72 | Ichimoku | trend | 61.62 | -38.38 | 390 | 10.0 | -81.85 | -23.72 | -81.85 | 1754 |
| 73 | Z-score reversion | reversion | 61.41 | -38.59 | 483 | 23.6 | -85.72 | -23.52 | -85.73 | 2094 |
| 74 | MFI reversion | reversion | 61.17 | -38.83 | 490 | 22.0 | -87.72 | -28.63 | -87.72 | 2121 |
| 75 | AI bee: Boozy | ai | 61.06 | -38.94 | 248 | 5.2 | — | — | — | — |
| 76 | AI bee: Bizzy | ai | 60.56 | -39.44 | 781 | 9.3 | — | — | — | — |
| 77 | ADX DI cross | trend | 58.60 | -41.40 | 520 | 10.6 | -89.57 | -34.70 | -89.58 | 2132 |
| 78 | Trend pullback | trend | 58.51 | -41.49 | 545 | 16.0 | -90.37 | -27.08 | -90.38 | 2300 |
| 79 | Donchian 20/10 | breakout | 58.41 | -41.59 | 601 | 19.0 | -90.82 | -26.39 | -90.83 | 2667 |
| 80 | RSI momentum | momentum | 57.66 | -42.34 | 567 | 17.8 | -90.28 | -25.83 | -90.29 | 2382 |
| 81 | MACD zero-line | trend | 57.01 | -42.99 | 549 | 15.7 | -91.54 | -29.86 | -91.55 | 2362 |
| 82 | Triple EMA stack | trend | 56.50 | -43.50 | 587 | 16.4 | -93.15 | -30.86 | -93.16 | 2617 |
| 83 | Bollinger breakout | breakout | 53.80 | -46.20 | 629 | 14.9 | -93.56 | -33.76 | -93.56 | 2822 |
| 84 | Consensus | meta | 52.27 | -47.73 | 595 | 10.3 | -94.22 | -25.92 | -94.22 | 2690 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -30.73 | -98.68 | 5389 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -33.42 | -97.34 | 3542 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -37.13 | -96.43 | 3610 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.96 | -99.34 | 5685 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.18 | -31.85 | -96.18 | 3585 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.90 | -99.73 | 6207 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -39.23 | -97.34 | 3683 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.54 | -98.47 | 4716 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.56 | -99.51 | 6147 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -33.73 | -95.84 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.55 | -34.69 | -95.55 | 4082 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.31 | -99.90 | 8347 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-10T05:40 | Keltner breakout | buy | BTC-USD | 16.23 | — | entry signal |
| 2026-10-10T05:40 | Bollinger breakout | buy | ETH-USD | 13.48 | — | entry signal |
| 2026-10-10T05:40 | Bollinger breakout | buy | BTC-USD | 13.49 | — | entry signal |
| 2026-10-10T05:40 | Donchian 55/20 | buy | SOL-USD | 17.85 | — | entry signal |
| 2026-10-10T05:40 | Donchian 55/20 | buy | BTC-USD | 18.12 | — | entry signal |
| 2026-10-10T05:40 | Donchian 20/10 | buy | BTC-USD | 14.62 | — | entry signal |
| 2026-10-10T05:40 | Ichimoku | buy | DOGE-USD | 15.42 | — | entry signal |
| 2026-10-10T05:39 | AI bee: Bizzy | buy | XRP-USD | 9.08 | — | Jev: buy (buy p=0.60) |
| 2026-10-10T05:35 | MFI reversion | sell | BTC-USD | 15.28 | -0.07 | exit signal |
| 2026-10-10T05:35 | Donchian 55/20 | buy | XRP-USD | 18.12 | — | entry signal |
| 2026-10-10T05:35 | Trend pullback | buy | BTC-USD | 5.88 | — | entry signal |
| 2026-10-10T05:35 | Trend pullback | sell | XRP-USD | 2.92 | -0.01 | rebalance down |
| 2026-10-10T05:35 | Trend pullback | sell | DOGE-USD | 2.92 | -0.01 | rebalance down |
| 2026-10-10T05:33 | AI bee: Bizzy | buy | SOL-USD | 8.79 | — | Jev: buy (buy p=0.58) |
| 2026-10-10T05:30 | Consensus | buy | SOL-USD | 13.07 | — | entry |
| 2026-10-10T05:30 | Bollinger breakout | sell | BTC-USD | 13.48 | -0.08 | exit signal |
| 2026-10-10T05:24 | AI bee: Bizzy | sell | DOGE-USD | 8.71 | -0.07 | Jev: sell (sell p=0.82) after 10 min |
| 2026-10-10T05:15 | Volume breakout | buy | ETH-USD | 17.84 | — | entry signal |
| 2026-10-10T05:15 | Squeeze breakout | buy | SOL-USD | 18.36 | — | entry signal |
| 2026-10-10T05:15 | Bollinger breakout | buy | SOL-USD | 13.50 | — | entry signal |
| 2026-10-10T05:15 | Donchian 20/10 | buy | XRP-USD | 14.63 | — | entry signal |
| 2026-10-10T05:15 | Donchian 20/10 | buy | SOL-USD | 14.63 | — | entry signal |
| 2026-10-10T05:15 | RSI momentum | buy | SOL-USD | 11.30 | — | entry signal |
| 2026-10-10T05:15 | RSI momentum | sell | XRP-USD | 2.90 | -0.01 | rebalance down |
| 2026-10-10T05:14 | AI bee: Bizzy | buy | DOGE-USD | 8.79 | — | Jev: buy (buy p=0.58) |
| 2026-10-10T05:09 | AI bee: Bizzy | sell | SOL-USD | 8.63 | -0.06 | Jev: sell (sell p=0.79) after 11 min |
| 2026-10-10T05:00 | Williams %R · 1h | sell | SOL-USD | 12.58 | -0.07 | exit signal |
| 2026-10-10T05:00 | Williams %R · 1h | sell | ETH-USD | 3.92 | -0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 05:55:05.000190+00:00 -> 2026-10-10 06:05:05.000190+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
