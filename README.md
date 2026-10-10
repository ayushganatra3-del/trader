# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T22:55:05.000153+00:00 · 18406 ticks

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

Today: 17116 decisions in 3425 calls, $0.2391 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T22:55 | 1 / 4 / 0 | NANC 17%, COIN 15%, SOL-USD 14% |  |
| Breezy | 2026-10-10T22:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T22:55 | 2 / 3 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.14 | +1.01% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| MFI reversion | AAPL | 1.96 | +0.72% | 7 |
| Z-score reversion | TNA | 1.94 | +3.40% | 7 |
| Keltner breakout | LABU | 1.94 | +8.17% | 7 |

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
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.16 | 2.41 | -1.64 | 87 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 18 | Hold BTC | benchmark | 99.27 | -0.73 | 0 | — | 27.61 | 3.31 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.17 | -0.82 | 89 | 55.1 | -10.80 | -2.10 | -14.73 | 344 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.66 | -1.34 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.77 | -3.23 | 38 | 13.2 | 5.58 | 0.83 | -19.85 | 134 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -0.30 | 0.04 | -10.38 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.64 | -0.09 | -13.84 | 257 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.68 | -0.19 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.87 | -4.13 | 110 | 24.5 | -15.91 | -2.57 | -17.84 | 469 |
| 34 | Supertrend · 1h | trend | 95.32 | -4.68 | 52 | 13.5 | -0.13 | 0.17 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 93.99 | -6.01 | 36 | 25.0 | 23.89 | 3.26 | -8.83 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.95 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.37 | -1.80 | -17.79 | 128 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -3.07 | -0.57 | -9.03 | 155 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Ichimoku · 1h | trend | 92.96 | -7.04 | 41 | 19.5 | -0.12 | 0.19 | -20.02 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -0.25 | 0.10 | -12.02 | 406 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.80 | -4.97 | -23.48 | 315 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.71 | 0.65 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 91.74 | -8.26 | 68 | 29.4 | 6.30 | 0.97 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.71 | -8.29 | 120 | 47.5 | -24.22 | -4.17 | -26.91 | 511 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.65 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.25 | -9.75 | 115 | 31.3 | -27.58 | -5.41 | -29.43 | 518 |
| 51 | CCI reversion · 1h | reversion | 89.77 | -10.22 | 100 | 45.0 | -8.54 | -1.10 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.71 | -10.29 | 278 | 22.3 | -34.07 | -5.14 | -39.29 | 1284 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.22 | -19.78 | 700 |
| 54 | MACD zero-line · 1h | trend | 89.14 | -10.86 | 62 | 19.4 | -6.95 | -0.76 | -19.79 | 241 |
| 55 | Donchian 20/10 · 1h | breakout | 88.82 | -11.18 | 58 | 19.0 | -0.17 | 0.19 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.32 | -1.40 | -28.62 | 319 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.64 | -5.15 | -36.59 | 701 |
| 58 | Three white soldiers | momentum | 88.02 | -11.98 | 136 | 18.4 | -47.94 | -23.30 | -47.94 | 589 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.86 | -12.14 | 101 | 13.9 | -8.95 | -1.01 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.80 | -1.32 | -24.06 | 413 |
| 63 | RSI(14) reversion | reversion | 75.17 | -24.83 | 355 | 28.7 | -72.69 | -18.15 | -72.72 | 1492 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.78 | -16.63 | -73.80 | 1670 |
| 65 | Squeeze breakout | breakout | 71.32 | -28.68 | 323 | 14.9 | -62.61 | -18.42 | -62.61 | 1233 |
| 66 | Donchian 55/20 | breakout | 70.82 | -29.18 | 327 | 18.0 | -67.60 | -14.46 | -67.60 | 1292 |
| 67 | EMA 20/50 cross | trend | 70.64 | -29.36 | 325 | 20.0 | -77.14 | -15.40 | -77.15 | 1458 |
| 68 | Volume breakout | breakout | 70.39 | -29.61 | 259 | 13.1 | -62.72 | -18.09 | -62.72 | 901 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.66 | -16.06 | -71.81 | 1433 |
| 70 | Supertrend | trend | 65.14 | -34.86 | 449 | 20.3 | -86.20 | -21.16 | -86.21 | 1914 |
| 71 | Keltner breakout | breakout | 63.34 | -36.66 | 442 | 14.5 | -83.92 | -27.91 | -83.92 | 1850 |
| 72 | Z-score reversion | reversion | 60.93 | -39.07 | 487 | 23.4 | -85.57 | -23.30 | -85.57 | 2086 |
| 73 | Ichimoku | trend | 60.64 | -39.36 | 401 | 9.7 | -81.69 | -23.36 | -81.70 | 1747 |
| 74 | AI bee: Boozy | ai | 60.55 | -39.45 | 253 | 5.1 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.36 | -39.64 | 499 | 21.6 | -87.65 | -28.34 | -87.65 | 2123 |
| 76 | AI bee: Bizzy | ai | 58.97 | -41.03 | 812 | 9.0 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.54 | -42.46 | 531 | 10.4 | -89.50 | -34.52 | -89.50 | 2126 |
| 78 | Donchian 20/10 | breakout | 56.35 | -43.65 | 623 | 18.3 | -90.86 | -26.22 | -90.86 | 2667 |
| 79 | RSI momentum | momentum | 55.58 | -44.42 | 590 | 17.3 | -90.23 | -25.66 | -90.23 | 2378 |
| 80 | Trend pullback ⏸ | trend | 55.45 | -44.55 | 581 | 15.0 | -90.95 | -27.04 | -90.95 | 2336 |
| 81 | MACD zero-line | trend | 55.15 | -44.85 | 570 | 15.1 | -91.54 | -30.04 | -91.54 | 2365 |
| 82 | Triple EMA stack | trend | 53.98 | -46.02 | 618 | 15.5 | -93.25 | -30.54 | -93.25 | 2623 |
| 83 | Bollinger breakout | breakout | 51.83 | -48.17 | 654 | 14.4 | -93.54 | -33.24 | -93.55 | 2819 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.57 | -98.69 | 5409 |
| 85 | Consensus | meta | 50.50 | -49.50 | 617 | 9.9 | -94.25 | -26.12 | -94.25 | 2686 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -33.27 | -97.39 | 3552 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -36.62 | -96.50 | 3618 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.01 | -99.35 | 5694 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.35 | -31.83 | -96.35 | 3619 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.68 | -99.73 | 6209 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -38.70 | -97.37 | 3689 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.29 | -98.47 | 4714 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.32 | -99.51 | 6151 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -33.63 | -95.86 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.55 | -34.45 | -95.56 | 4081 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.84 | -99.90 | 8323 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-10T22:40 | Donchian 20/10 | buy | SOL-USD | 14.10 | — | entry signal |
| 2026-10-10T22:40 | RSI momentum | buy | SOL-USD | 13.90 | — | entry signal |
| 2026-10-10T22:35 | Z-score reversion | buy | DOGE-USD | 15.30 | — | entry signal |
| 2026-10-10T22:35 | Bollinger breakout | buy | SOL-USD | 12.96 | — | entry signal |
| 2026-10-10T22:35 | MACD zero-line | buy | SOL-USD | 13.80 | — | entry signal |
| 2026-10-10T22:35 | Triple EMA stack | buy | SOL-USD | 13.50 | — | entry signal |
| 2026-10-10T22:35 | EMA 20/50 cross | buy | BTC-USD | 17.69 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 22:55:05.000153+00:00 -> 2026-10-10 23:05:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
