# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T03:55:05.000147+00:00 · 17469 ticks

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

Today: 3075 decisions in 615 calls, $0.0430 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T03:55 | 0 / 4 / 1 | NANC 17%, COIN 14% |  |
| Breezy | 2026-10-10T03:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T03:55 | 0 / 5 / 0 | COIN 75% |  |

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
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.33 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 88 | 55.7 | -10.86 | -2.11 | -14.99 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.67 | -1.33 | 0 | — | 27.06 | 3.25 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.25 | -2.75 | 40 | 45.0 | 1.52 | 0.43 | -8.60 | 162 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.38 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.56 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 1.17 | 0.38 | -8.88 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.83 | -0.12 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.85 | -4.15 | 108 | 23.1 | -16.09 | -2.61 | -17.97 | 471 |
| 34 | Supertrend · 1h | trend | 95.11 | -4.89 | 52 | 13.5 | -0.79 | 0.09 | -18.22 | 212 |
| 35 | Squeeze breakout · 1h | breakout | 94.21 | -5.79 | 35 | 25.7 | 24.17 | 3.29 | -8.65 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.43 | -1.96 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.36 | -0.41 | -9.03 | 151 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -5.32 | -0.90 | -12.16 | 410 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.87 | -4.99 | -23.73 | 319 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.59 | 0.64 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.93 | -8.07 | 67 | 29.9 | 6.60 | 1.01 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.79 | -8.21 | 117 | 48.7 | -25.06 | -4.32 | -27.28 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.27 | -0.94 | -26.38 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.24 | -9.76 | 114 | 30.7 | -28.35 | -5.60 | -30.13 | 522 |
| 51 | CCI reversion · 1h | reversion | 89.75 | -10.25 | 98 | 44.9 | -9.27 | -1.22 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.74 | -10.26 | 277 | 22.0 | -35.60 | -5.40 | -39.28 | 1285 |
| 53 | MACD zero-line · 1h | trend | 89.38 | -10.62 | 60 | 20.0 | -6.30 | -0.67 | -19.50 | 240 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Three white soldiers | momentum | 88.94 | -11.06 | 130 | 19.2 | -47.90 | -23.37 | -47.98 | 588 |
| 56 | Donchian 20/10 · 1h | breakout | 88.86 | -11.14 | 58 | 19.0 | -0.04 | 0.20 | -17.72 | 221 |
| 57 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.30 | -1.40 | -28.47 | 318 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.23 | -5.26 | -36.60 | 702 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.84 | -12.16 | 101 | 13.9 | -9.52 | -1.09 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.44 | -1.27 | -23.88 | 413 |
| 63 | RSI(14) reversion | reversion | 75.51 | -24.49 | 352 | 29.0 | -72.90 | -18.28 | -73.06 | 1497 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.04 | -16.74 | -73.92 | 1666 |
| 65 | Squeeze breakout | breakout | 73.45 | -26.55 | 305 | 15.7 | -61.75 | -18.33 | -61.76 | 1220 |
| 66 | Donchian 55/20 | breakout | 72.45 | -27.55 | 314 | 18.5 | -67.68 | -14.49 | -68.07 | 1295 |
| 67 | EMA 20/50 cross | trend | 72.10 | -27.91 | 309 | 20.4 | -77.30 | -15.41 | -77.46 | 1462 |
| 68 | Volume breakout | breakout | 71.34 | -28.66 | 251 | 13.5 | -63.45 | -18.35 | -63.53 | 906 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.77 | -16.16 | -71.91 | 1437 |
| 70 | Supertrend | trend | 66.27 | -33.73 | 436 | 20.6 | -86.43 | -21.26 | -86.48 | 1925 |
| 71 | Keltner breakout | breakout | 65.04 | -34.96 | 426 | 15.0 | -84.23 | -28.02 | -84.43 | 1864 |
| 72 | Ichimoku | trend | 62.04 | -37.96 | 387 | 10.1 | -81.77 | -23.57 | -81.78 | 1750 |
| 73 | Z-score reversion | reversion | 61.41 | -38.59 | 483 | 23.6 | -85.73 | -23.53 | -85.74 | 2095 |
| 74 | MFI reversion | reversion | 61.25 | -38.75 | 487 | 22.2 | -87.74 | -28.65 | -87.74 | 2124 |
| 75 | AI bee: Bizzy | ai | 61.08 | -38.92 | 773 | 9.4 | — | — | — | — |
| 76 | AI bee: Boozy | ai | 61.06 | -38.94 | 248 | 5.2 | — | — | — | — |
| 77 | Donchian 20/10 | breakout | 58.66 | -41.34 | 600 | 19.0 | -90.82 | -26.28 | -90.83 | 2665 |
| 78 | ADX DI cross | trend | 58.57 | -41.43 | 519 | 10.6 | -89.62 | -34.85 | -89.62 | 2135 |
| 79 | Trend pullback | trend | 58.53 | -41.48 | 545 | 16.0 | -90.39 | -27.18 | -90.40 | 2299 |
| 80 | RSI momentum | momentum | 57.80 | -42.20 | 566 | 17.8 | -90.34 | -25.87 | -90.34 | 2382 |
| 81 | MACD zero-line | trend | 57.17 | -42.83 | 548 | 15.7 | -91.52 | -29.75 | -91.52 | 2359 |
| 82 | Triple EMA stack | trend | 56.85 | -43.15 | 584 | 16.3 | -93.13 | -30.67 | -93.13 | 2613 |
| 83 | Bollinger breakout | breakout | 54.27 | -45.73 | 625 | 15.0 | -93.55 | -33.49 | -93.55 | 2820 |
| 84 | Consensus | meta | 52.45 | -47.55 | 593 | 10.3 | -94.22 | -25.94 | -94.22 | 2687 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.85 | -98.69 | 5391 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -33.28 | -97.34 | 3539 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -36.86 | -96.42 | 3607 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.97 | -99.34 | 5689 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.18 | -31.87 | -96.18 | 3586 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.80 | -99.73 | 6204 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -39.32 | -97.36 | 3686 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.49 | -98.47 | 4717 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.66 | -99.51 | 6152 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -33.75 | -95.85 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.57 | -34.70 | -95.58 | 4085 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.87 | -99.90 | 8344 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T03:50 | ADX DI cross | buy | XRP-USD | 14.65 | — | entry signal |
| 2026-10-10T03:45 | Consensus | buy | DOGE-USD | 13.12 | — | entry |
| 2026-10-10T03:45 | MFI reversion | buy | ETH-USD | 15.32 | — | entry signal |
| 2026-10-10T03:45 | Trend pullback | buy | DOGE-USD | 14.64 | — | entry signal |
| 2026-10-10T03:45 | ADX DI cross | buy | SOL-USD | 14.67 | — | entry signal |
| 2026-10-10T03:40 | MFI reversion | buy | XRP-USD | 15.33 | — | entry signal |
| 2026-10-10T03:40 | Supertrend | sell | BTC-USD | 16.53 | -0.11 | exit signal |
| 2026-10-10T03:35 | MFI reversion | buy | BTC-USD | 15.34 | — | entry signal |
| 2026-10-10T03:35 | Donchian 20/10 | sell | DOGE-USD | 11.88 | 0.09 | exit signal |
| 2026-10-10T03:35 | Triple EMA stack | sell | SOL-USD | 14.20 | -0.06 | exit signal |
| 2026-10-10T03:35 | EMA 20/50 cross | buy | SOL-USD | 10.82 | — | rebalance up |
| 2026-10-10T03:35 | EMA 20/50 cross | sell | BTC-USD | 17.88 | -0.12 | exit signal |
| 2026-10-10T03:30 | Consensus | sell | DOGE-USD | 13.09 | -0.03 | target is flat |
| 2026-10-10T03:30 | Squeeze breakout | sell | DOGE-USD | 14.73 | 0.03 | exit signal |
| 2026-10-10T03:30 | Keltner breakout | sell | DOGE-USD | 16.34 | 0.03 | exit signal |
| 2026-10-10T03:30 | Bollinger breakout | sell | DOGE-USD | 10.88 | 0.02 | exit signal |
| 2026-10-10T03:30 | Donchian 55/20 | sell | SOL-USD | 18.06 | -0.09 | exit signal |
| 2026-10-10T03:30 | Donchian 55/20 | sell | ETH-USD | 17.88 | -0.12 | exit signal |
| 2026-10-10T03:30 | Donchian 20/10 | sell | SOL-USD | 14.64 | -0.07 | exit signal |
| 2026-10-10T03:30 | Donchian 20/10 | sell | ETH-USD | 14.61 | -0.10 | exit signal |
| 2026-10-10T03:30 | RSI momentum | sell | SOL-USD | 14.41 | -0.07 | exit signal |
| 2026-10-10T03:30 | RSI momentum | sell | ETH-USD | 14.31 | -0.08 | exit signal |
| 2026-10-10T03:30 | Trend pullback | sell | ETH-USD | 14.62 | -0.11 | exit signal |
| 2026-10-10T03:30 | Supertrend | buy | SOL-USD | 6.65 | — | rebalance up |
| 2026-10-10T03:30 | Supertrend | buy | BTC-USD | 3.39 | — | rebalance up |
| 2026-10-10T03:30 | Supertrend | sell | XRP-USD | 13.27 | 0.05 | exit signal |
| 2026-10-10T03:30 | Triple EMA stack | sell | ETH-USD | 14.19 | -0.08 | exit signal |
| 2026-10-10T03:25 | Donchian 55/20 | sell | XRP-USD | 18.14 | 0.01 | exit signal |
| 2026-10-10T03:25 | Trend pullback | sell | XRP-USD | 14.57 | -0.13 | stop-loss |
| 2026-10-10T03:25 | Ichimoku | sell | SOL-USD | 15.51 | -0.05 | exit signal |
| 2026-10-10T03:25 | ADX DI cross | sell | XRP-USD | 14.68 | 0.02 | exit signal |
| 2026-10-10T03:25 | Triple EMA stack | sell | XRP-USD | 11.41 | 0.04 | exit signal |
| 2026-10-10T03:20 | RSI momentum | sell | XRP-USD | 11.63 | 0.05 | exit signal |
| 2026-10-10T03:15 | Donchian 20/10 | sell | XRP-USD | 11.81 | 0.01 | exit signal |
| 2026-10-10T03:10 | Volume breakout | sell | DOGE-USD | 17.83 | -0.02 | exit signal |
| 2026-10-10T03:05 | Consensus | sell | XRP-USD | 13.15 | -0.04 | target is flat |
| 2026-10-10T03:05 | Squeeze breakout | sell | XRP-USD | 14.71 | -0.02 | exit signal |
| 2026-10-10T03:05 | Keltner breakout | sell | XRP-USD | 16.29 | -0.02 | exit signal |
| 2026-10-10T03:05 | Keltner breakout | sell | SOL-USD | 16.22 | -0.09 | exit signal |
| 2026-10-10T03:05 | Bollinger breakout | sell | XRP-USD | 10.87 | -0.00 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 03:55:05.000147+00:00 -> 2026-10-10 04:05:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
