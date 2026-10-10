# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T02:25:05.000130+00:00 · 17387 ticks

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

Today: 1845 decisions in 369 calls, $0.0258 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T02:25 | 0 / 3 / 2 | DOGE-USD 15%, NANC 16%, COIN 14% |  |
| Breezy | 2026-10-10T02:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T02:25 | 1 / 2 / 2 | COIN 75% |  |

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
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -12.05 | -1.91 | -21.08 | 72 |
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
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 88 | 55.7 | -10.87 | -2.11 | -15.02 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.72 | -1.27 | 0 | — | 27.14 | 3.26 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.26 | -2.73 | 40 | 45.0 | 1.54 | 0.43 | -8.60 | 162 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.56 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 1.17 | 0.38 | -8.88 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.88 | -0.13 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.87 | -4.13 | 108 | 23.1 | -16.07 | -2.60 | -17.97 | 471 |
| 34 | Supertrend · 1h | trend | 95.17 | -4.83 | 52 | 13.5 | -0.20 | 0.17 | -18.22 | 211 |
| 35 | Squeeze breakout · 1h | breakout | 94.20 | -5.80 | 35 | 25.7 | 24.16 | 3.29 | -8.65 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.45 | -1.97 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.33 | -0.40 | -9.03 | 151 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -5.81 | -0.97 | -12.86 | 420 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.89 | -5.00 | -23.75 | 319 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.68 | 0.65 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.92 | -8.08 | 67 | 29.9 | 6.59 | 1.01 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.81 | -8.19 | 117 | 48.7 | -25.10 | -4.32 | -27.34 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.22 | -0.93 | -26.38 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.27 | -9.73 | 114 | 30.7 | -27.90 | -5.52 | -29.72 | 521 |
| 51 | CCI reversion · 1h | reversion | 89.76 | -10.23 | 98 | 44.9 | -9.26 | -1.21 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.74 | -10.26 | 277 | 22.0 | -35.57 | -5.39 | -39.28 | 1285 |
| 53 | MACD zero-line · 1h | trend | 89.44 | -10.56 | 60 | 20.0 | -6.21 | -0.65 | -19.47 | 240 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Three white soldiers | momentum | 88.94 | -11.06 | 130 | 19.2 | -47.90 | -23.37 | -47.98 | 588 |
| 56 | Donchian 20/10 · 1h | breakout | 88.85 | -11.15 | 58 | 19.0 | -0.01 | 0.21 | -17.72 | 221 |
| 57 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.20 | -1.38 | -28.47 | 318 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.44 | -5.30 | -36.60 | 702 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.84 | -12.16 | 101 | 13.9 | -9.49 | -1.08 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.44 | -1.27 | -23.88 | 413 |
| 63 | RSI(14) reversion | reversion | 75.51 | -24.49 | 352 | 29.0 | -72.80 | -18.21 | -72.96 | 1494 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.04 | -16.74 | -73.92 | 1666 |
| 65 | Squeeze breakout | breakout | 73.66 | -26.34 | 301 | 15.6 | -61.62 | -18.22 | -61.62 | 1220 |
| 66 | Donchian 55/20 | breakout | 72.71 | -27.29 | 311 | 18.3 | -67.87 | -14.47 | -68.37 | 1300 |
| 67 | EMA 20/50 cross | trend | 72.24 | -27.76 | 308 | 20.5 | -77.32 | -15.41 | -77.52 | 1464 |
| 68 | Volume breakout | breakout | 71.36 | -28.64 | 250 | 13.6 | -63.50 | -18.34 | -63.59 | 907 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.77 | -16.16 | -71.91 | 1436 |
| 70 | Supertrend | trend | 66.47 | -33.53 | 434 | 20.5 | -86.41 | -21.19 | -86.50 | 1926 |
| 71 | Keltner breakout | breakout | 65.25 | -34.75 | 422 | 14.9 | -84.19 | -27.86 | -84.44 | 1864 |
| 72 | Ichimoku | trend | 62.14 | -37.85 | 385 | 10.1 | -81.74 | -23.52 | -81.78 | 1750 |
| 73 | Z-score reversion | reversion | 61.41 | -38.59 | 483 | 23.6 | -85.73 | -23.53 | -85.74 | 2095 |
| 74 | MFI reversion | reversion | 61.38 | -38.62 | 487 | 22.2 | -87.73 | -28.60 | -87.75 | 2122 |
| 75 | AI bee: Bizzy | ai | 61.21 | -38.79 | 770 | 9.5 | — | — | — | — |
| 76 | AI bee: Boozy | ai | 61.06 | -38.94 | 248 | 5.2 | — | — | — | — |
| 77 | Trend pullback | trend | 58.95 | -41.05 | 541 | 16.1 | -90.36 | -27.06 | -90.43 | 2297 |
| 78 | Donchian 20/10 | breakout | 58.89 | -41.11 | 596 | 18.8 | -90.85 | -26.19 | -90.90 | 2669 |
| 79 | ADX DI cross | trend | 58.76 | -41.24 | 518 | 10.4 | -89.62 | -34.68 | -89.65 | 2135 |
| 80 | RSI momentum | momentum | 58.00 | -42.00 | 562 | 17.8 | -90.31 | -25.74 | -90.34 | 2383 |
| 81 | MACD zero-line | trend | 57.17 | -42.83 | 548 | 15.7 | -91.57 | -29.89 | -91.57 | 2364 |
| 82 | Triple EMA stack | trend | 57.07 | -42.93 | 580 | 16.2 | -93.12 | -30.49 | -93.14 | 2615 |
| 83 | Bollinger breakout | breakout | 54.43 | -45.57 | 621 | 15.0 | -93.52 | -33.30 | -93.53 | 2820 |
| 84 | Consensus | meta | 52.67 | -47.33 | 589 | 10.4 | -94.21 | -25.85 | -94.22 | 2687 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.76 | -98.69 | 5394 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.33 | -33.14 | -97.34 | 3541 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.43 | -36.73 | -96.44 | 3610 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.94 | -99.34 | 5688 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.21 | -31.95 | -96.21 | 3591 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.79 | -99.73 | 6208 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -39.08 | -97.35 | 3683 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.48 | -98.48 | 4717 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.49 | -99.51 | 6147 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -33.69 | -95.85 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.56 | -34.50 | -95.56 | 4081 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.66 | -99.90 | 8350 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T02:25 | Three white soldiers | sell | SOL-USD | 22.25 | -0.04 | exit signal |
| 2026-10-10T02:25 | Volume breakout | sell | ETH-USD | 17.77 | -0.10 | exit signal |
| 2026-10-10T02:25 | Squeeze breakout | buy | ETH-USD | 11.00 | — | rebalance up |
| 2026-10-10T02:25 | Squeeze breakout | sell | BTC-USD | 18.32 | -0.13 | exit signal |
| 2026-10-10T02:25 | Bollinger breakout | buy | SOL-USD | 2.74 | — | rebalance up |
| 2026-10-10T02:25 | Bollinger breakout | sell | BTC-USD | 8.17 | -0.06 | exit signal |
| 2026-10-10T02:25 | Trend pullback | sell | BTC-USD | 14.67 | -0.09 | exit signal |
| 2026-10-10T02:25 | MACD zero-line | sell | BTC-USD | 14.22 | -0.10 | exit signal |
| 2026-10-10T02:20 | AI bee: Bizzy | buy | DOGE-USD | 9.37 | — | Jev: buy (buy p=0.61) |
| 2026-10-10T02:07 | AI bee: Boozy | sell | ETH-USD | 15.31 | -0.10 | Jev: sell |
| 2026-10-10T02:07 | AI bee: Bizzy | sell | XRP-USD | 9.28 | -0.06 | Jev: sell (sell p=0.70) after 12 min |
| 2026-10-10T02:05 | Bollinger breakout | buy | BTC-USD | 2.72 | — | rebalance up |
| 2026-10-10T02:05 | Bollinger breakout | sell | SOL-USD | 2.72 | -0.00 | rebalance down |
| 2026-10-10T02:00 | CCI reversion · 1h | sell | XRP-USD | 4.63 | 0.04 | exit signal |
| 2026-10-10T02:00 | Williams %R · 1h | buy | ETH-USD | 3.95 | — | entry |
| 2026-10-10T02:00 | Williams %R · 1h | buy | BTC-USD | 6.32 | — | rebalance up |
| 2026-10-10T02:00 | Williams %R · 1h | sell | XRP-USD | 10.27 | 0.12 | exit signal |
| 2026-10-10T02:00 | Bollinger reversion · 1h | sell | SOL-USD | 15.51 | 0.05 | exit signal |
| 2026-10-10T02:00 | Squeeze breakout · 1h | buy | DOGE-USD | 23.57 | — | entry signal |
| 2026-10-10T02:00 | Bollinger breakout · 1h | buy | DOGE-USD | 22.92 | — | entry signal |
| 2026-10-10T02:00 | MACD zero-line · 1h | buy | DOGE-USD | 22.34 | — | entry signal |
| 2026-10-10T01:55 | AI bee: Bizzy | buy | XRP-USD | 9.34 | — | Jev: buy (buy p=0.61) |
| 2026-10-10T01:55 | AI bee: Bizzy | sell | DOGE-USD | 9.43 | -0.03 | Jev: sell (sell p=0.53) after 10 min |
| 2026-10-10T01:55 | MFI reversion | sell | DOGE-USD | 15.38 | 0.05 | exit signal |
| 2026-10-10T01:55 | Squeeze breakout | buy | ETH-USD | 7.47 | — | entry signal |
| 2026-10-10T01:55 | Squeeze breakout | sell | XRP-USD | 3.72 | -0.00 | rebalance down |
| 2026-10-10T01:55 | Squeeze breakout | sell | DOGE-USD | 3.75 | 0.01 | rebalance down |
| 2026-10-10T01:55 | Keltner breakout | buy | ETH-USD | 16.32 | — | entry signal |
| 2026-10-10T01:51 | AI bee: Boozy | buy | ETH-USD | 15.41 | — | Jev: buy (buy p=0.75) |
| 2026-10-10T01:50 | AI bee: Bizzy | sell | SOL-USD | 9.76 | -0.04 | Jev: sell (sell p=0.53) after 10 min |
| 2026-10-10T01:50 | Squeeze breakout | buy | BTC-USD | 18.45 | — | entry signal |
| 2026-10-10T01:50 | Bollinger breakout | buy | BTC-USD | 5.50 | — | entry signal |
| 2026-10-10T01:50 | Bollinger breakout | sell | XRP-USD | 2.74 | 0.00 | rebalance down |
| 2026-10-10T01:50 | Bollinger breakout | sell | DOGE-USD | 2.75 | 0.00 | rebalance down |
| 2026-10-10T01:45 | AI bee: Bizzy | buy | DOGE-USD | 9.47 | — | Jev: buy (buy p=0.62) |
| 2026-10-10T01:45 | Consensus | buy | DOGE-USD | 13.12 | — | entry |
| 2026-10-10T01:45 | Volume breakout | buy | DOGE-USD | 17.85 | — | entry signal |
| 2026-10-10T01:40 | AI bee: Bizzy | buy | SOL-USD | 9.80 | — | Jev: buy (buy p=0.64) |
| 2026-10-10T01:35 | Trend pullback | buy | DOGE-USD | 14.74 | — | entry signal |
| 2026-10-10T01:35 | Ichimoku | sell | BTC-USD | 15.45 | -0.10 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 02:25:05.000130+00:00 -> 2026-10-10 02:35:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
