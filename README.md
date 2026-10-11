# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T10:55:05.000150+00:00 · 18974 ticks

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

Today: 7815 decisions in 1563 calls, $0.1093 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T10:55 | 0 / 4 / 1 | ETH-USD 14%, NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T10:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T10:55 | 2 / 3 / 0 | COIN 76% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.56 | -2.30 | -13.79 | 118 |
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
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.86 | -1.90 | -14.61 | 340 |
| 19 | Hold BTC | benchmark | 99.16 | -0.84 | 0 | — | 27.04 | 3.24 | -8.68 | 1 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.84 | -6.44 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.69 | -3.31 | 39 | 12.8 | 6.49 | 0.93 | -19.85 | 132 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -5.83 | -1.89 | -9.31 | 252 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.72 | -0.10 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.83 | -0.21 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.79 | -4.21 | 113 | 23.9 | -15.31 | -2.46 | -17.64 | 466 |
| 34 | Supertrend · 1h | trend | 95.03 | -4.97 | 53 | 13.2 | 0.14 | 0.21 | -18.22 | 209 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.90 | -2.25 | -6.77 | 103 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.85 | -6.15 | 37 | 24.3 | 23.83 | 3.25 | -8.95 | 106 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.38 | -1.63 | -17.79 | 129 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.00 | -0.33 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -3.45 | -0.45 | -13.65 | 410 |
| 42 | Ichimoku · 1h | trend | 92.81 | -7.19 | 42 | 19.0 | -0.09 | 0.19 | -20.11 | 120 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.24 | 0.72 | -17.07 | 222 |
| 44 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 45 | Bollinger reversion · 1h | reversion | 92.47 | -7.53 | 76 | 36.8 | -21.08 | -5.04 | -23.37 | 317 |
| 46 | Bollinger breakout · 1h | breakout | 91.61 | -8.39 | 70 | 28.6 | 6.05 | 0.94 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.08 | -8.92 | 123 | 46.3 | -24.47 | -4.22 | -26.91 | 516 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -7.68 | -0.74 | -26.38 | 234 |
| 50 | Candlestick reversal · 1h | reversion | 90.10 | -9.90 | 116 | 31.9 | -26.71 | -5.23 | -28.43 | 513 |
| 51 | CCI reversion · 1h | reversion | 89.54 | -10.46 | 101 | 44.6 | -8.13 | -1.04 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.50 | -10.50 | 282 | 22.0 | -33.64 | -5.05 | -39.30 | 1281 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 88.84 | -11.15 | 64 | 18.8 | -7.15 | -0.79 | -19.96 | 241 |
| 55 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.76 | -1.46 | -28.63 | 320 |
| 56 | Donchian 20/10 · 1h | breakout | 88.74 | -11.26 | 59 | 18.6 | -0.52 | 0.14 | -17.72 | 224 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.43 | -5.10 | -36.60 | 700 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.78 | -12.22 | 103 | 13.6 | -9.47 | -1.08 | -21.58 | 337 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.15 | -23.43 | -48.15 | 591 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.21 | -1.29 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.76 | -1.31 | -23.91 | 413 |
| 63 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.68 | -16.55 | -73.79 | 1667 |
| 64 | RSI(14) reversion | reversion | 74.01 | -25.99 | 367 | 27.8 | -73.11 | -18.49 | -73.11 | 1500 |
| 65 | Squeeze breakout | breakout | 70.80 | -29.20 | 327 | 14.7 | -62.44 | -18.43 | -62.44 | 1230 |
| 66 | Donchian 55/20 | breakout | 70.30 | -29.70 | 331 | 17.8 | -67.51 | -14.43 | -67.51 | 1291 |
| 67 | Volume breakout | breakout | 70.17 | -29.83 | 261 | 13.0 | -62.64 | -18.06 | -62.66 | 901 |
| 68 | EMA 20/50 cross | trend | 69.88 | -30.12 | 331 | 19.6 | -77.02 | -15.37 | -77.02 | 1455 |
| 69 | VWAP reversion | reversion | 67.74 | -32.26 | 401 | 25.9 | -71.88 | -16.25 | -71.88 | 1445 |
| 70 | Supertrend | trend | 63.71 | -36.29 | 461 | 19.7 | -86.18 | -21.35 | -86.18 | 1913 |
| 71 | Keltner breakout | breakout | 62.86 | -37.14 | 446 | 14.3 | -83.65 | -27.63 | -83.65 | 1844 |
| 72 | AI bee: Boozy | ai | 60.46 | -39.54 | 254 | 5.1 | — | — | — | — |
| 73 | Ichimoku | trend | 60.28 | -39.72 | 404 | 9.7 | -81.71 | -23.41 | -81.71 | 1746 |
| 74 | Z-score reversion | reversion | 59.39 | -40.61 | 505 | 22.6 | -85.60 | -23.70 | -85.60 | 2090 |
| 75 | MFI reversion | reversion | 59.19 | -40.81 | 513 | 21.2 | -87.68 | -28.94 | -87.68 | 2124 |
| 76 | AI bee: Bizzy | ai | 58.03 | -41.97 | 829 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.36 | -43.64 | 543 | 10.1 | -89.39 | -35.73 | -89.39 | 2123 |
| 78 | Trend pullback | trend | 55.26 | -44.74 | 583 | 14.9 | -91.01 | -27.10 | -91.01 | 2339 |
| 79 | Donchian 20/10 | breakout | 55.19 | -44.80 | 634 | 18.0 | -90.82 | -26.40 | -90.82 | 2664 |
| 80 | RSI momentum | momentum | 54.04 | -45.96 | 605 | 16.9 | -90.32 | -25.93 | -90.32 | 2381 |
| 81 | Triple EMA stack | trend | 53.34 | -46.66 | 625 | 15.4 | -93.15 | -30.22 | -93.15 | 2614 |
| 82 | MACD zero-line | trend | 53.28 | -46.72 | 589 | 14.6 | -91.57 | -30.70 | -91.57 | 2366 |
| 83 | Bollinger breakout | breakout | 50.63 | -49.38 | 667 | 14.1 | -93.51 | -33.44 | -93.51 | 2815 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -31.57 | -98.66 | 5396 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -34.27 | -97.38 | 3549 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -36.17 | -96.43 | 3607 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.12 | -25.72 | -94.12 | 2679 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -38.32 | -99.36 | 5710 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.39 | -32.04 | -96.39 | 3626 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -43.79 | -99.74 | 6212 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -38.18 | -97.34 | 3681 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -38.37 | -98.49 | 4721 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.71 | -99.52 | 6164 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.96 | -34.66 | -95.96 | 3762 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.65 | -35.42 | -95.65 | 4092 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.58 | -99.90 | 8319 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T10:55 | Z-score reversion | buy | XRP-USD | 14.86 | — | entry signal |
| 2026-10-11T10:52 | AI bee: Bizzy | buy | ETH-USD | 8.27 | — | Jev: buy (buy p=0.57) |
| 2026-10-11T10:50 | Z-score reversion | buy | DOGE-USD | 14.87 | — | entry |
| 2026-10-11T10:50 | RSI(14) reversion | buy | DOGE-USD | 18.52 | — | entry |
| 2026-10-11T10:45 | VWAP reversion | buy | XRP-USD | 16.96 | — | entry signal |
| 2026-10-11T10:45 | VWAP reversion | buy | DOGE-USD | 16.96 | — | entry signal |
| 2026-10-11T10:45 | Z-score reversion | buy | ETH-USD | 14.88 | — | entry signal |
| 2026-10-11T10:40 | MACD zero-line | sell | SOL-USD | 13.25 | -0.11 | stop-loss |
| 2026-10-11T10:35 | Donchian 20/10 | sell | ETH-USD | 13.77 | -0.11 | stop-loss |
| 2026-10-11T10:35 | ADX DI cross | sell | ETH-USD | 14.01 | -0.11 | stop-loss |
| 2026-10-11T10:35 | MACD zero-line | sell | ETH-USD | 13.27 | -0.10 | exit signal |
| 2026-10-11T10:31 | AI bee: Bizzy | sell | SOL-USD | 7.96 | -0.05 | Jev: sell (sell p=0.59) after 11 min |
| 2026-10-11T10:20 | AI bee: Bizzy | buy | SOL-USD | 8.01 | — | Jev: buy (buy p=0.55) |
| 2026-10-11T10:15 | Supertrend | sell | DOGE-USD | 15.83 | -0.13 | exit signal |
| 2026-10-11T10:15 | MACD zero-line | buy | SOL-USD | 13.36 | — | entry signal |
| 2026-10-11T10:10 | MACD zero-line | buy | ETH-USD | 13.37 | — | entry signal |
| 2026-10-11T10:07 | AI bee: Bizzy | sell | DOGE-USD | 8.40 | -0.05 | Jev: sell (sell p=0.89) after 12 min |
| 2026-10-11T10:00 | CCI reversion · 1h | buy | XRP-USD | 5.97 | — | entry signal |
| 2026-10-11T10:00 | CCI reversion · 1h | buy | DOGE-USD | 5.97 | — | entry signal |
| 2026-10-11T10:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 5.69 | -0.04 | exit signal |
| 2026-10-11T10:00 | Z-score reversion | sell | ETH-USD | 14.82 | -0.08 | exit signal |
| 2026-10-11T09:55 | AI bee: Bizzy | buy | DOGE-USD | 8.45 | — | Jev: buy (buy p=0.58) |
| 2026-10-11T09:45 | Donchian 20/10 | sell | SOL-USD | 13.77 | -0.11 | stop-loss |
| 2026-10-11T09:35 | MACD zero-line | sell | XRP-USD | 13.35 | -0.09 | exit signal |
| 2026-10-11T09:35 | MACD zero-line | sell | SOL-USD | 13.32 | -0.10 | exit signal |
| 2026-10-11T09:35 | MACD zero-line | sell | DOGE-USD | 13.35 | -0.09 | exit signal |
| 2026-10-11T09:30 | Squeeze breakout | sell | DOGE-USD | 17.60 | -0.13 | stop-loss |
| 2026-10-11T09:30 | Bollinger breakout | sell | XRP-USD | 12.63 | -0.09 | exit signal |
| 2026-10-11T09:30 | Bollinger breakout | sell | DOGE-USD | 12.66 | -0.09 | stop-loss |
| 2026-10-11T09:30 | Donchian 20/10 | sell | DOGE-USD | 13.75 | -0.10 | stop-loss |
| 2026-10-11T09:30 | RSI momentum | sell | XRP-USD | 13.46 | -0.10 | exit signal |
| 2026-10-11T09:30 | RSI momentum | sell | DOGE-USD | 13.45 | -0.10 | stop-loss |
| 2026-10-11T09:25 | EMA 20/50 cross | sell | BTC-USD | 17.39 | -0.11 | exit signal |
| 2026-10-11T09:23 | AI bee: Bizzy | sell | SOL-USD | 8.72 | -0.08 | Jev: sell (sell p=0.91) after 10 min |
| 2026-10-11T09:20 | Bollinger breakout | sell | SOL-USD | 12.65 | -0.09 | exit signal |
| 2026-10-11T09:20 | Bollinger breakout | sell | ETH-USD | 12.64 | -0.09 | exit signal |
| 2026-10-11T09:19 | AI bee: Bizzy | sell | ETH-USD | 8.22 | -0.06 | Jev: sell (sell p=0.78) after 10 min |
| 2026-10-11T09:15 | MFI reversion | sell | SOL-USD | 14.77 | -0.07 | exit signal |
| 2026-10-11T09:15 | Donchian 20/10 | buy | DOGE-USD | 13.86 | — | entry |
| 2026-10-11T09:15 | RSI momentum | buy | DOGE-USD | 13.55 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 10:55:05.000150+00:00 -> 2026-10-11 11:05:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
