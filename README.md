# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T23:55:05.000142+00:00 · 20720 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.28 (-4.72%)

Closed trades 59, win rate 49.2%, fees £2.28, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.55 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 35427 decisions in 3387 calls, $0.4450 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T23:55 | 0 / 3 / 2 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-12T23:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T23:55 | 1 / 4 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | AAPL | 2.49 | +0.83% | 6 |
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.95 | 2.96 | 0 | — | 1.61 | 0.84 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.09 | 2.09 | 16 | 50.0 | -12.87 | -2.14 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 4 | Hold SPY | benchmark | 101.46 | 1.46 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.11 | -3.27 | 17 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.25 | 1.25 | 0 | — | 1.71 | 0.84 | -3.62 | 1 |
| 7 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -9.45 | -2.83 | -13.79 | 118 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.69 | 0.69 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.66 | 0.66 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.31 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.44 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.16 | 0.16 | 0 | — | 3.58 | 1.41 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.40 | -0.60 | 0 | — | -4.89 | -2.27 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.66 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.80 | -3.51 | 21 |
| 18 | Donchian 55/20 · 1h | breakout | 98.27 | -1.73 | 31 | 12.9 | 12.04 | 1.46 | -18.79 | 113 |
| 19 | Daily: Bullish score | daily | 98.17 | -1.83 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 20 | Max aggression: 1-day momentum | meta | 98.04 | -1.96 | 11 | 36.4 | -16.71 | -0.63 | -37.31 | 42 |
| 21 | Hold BTC | benchmark | 97.97 | -2.03 | 0 | — | 27.97 | 3.32 | -8.68 | 1 |
| 22 | Trend pullback · 1h | trend | 97.91 | -2.09 | 78 | 23.1 | -23.01 | -6.47 | -25.60 | 168 |
| 23 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.63 | -4.53 | 27 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.06 | -2.94 | 0 | — | 9.02 | 1.51 | -8.33 | 1 |
| 25 | Z-score reversion · 1h | reversion | 96.73 | -3.27 | 45 | 42.2 | 3.18 | 0.76 | -8.60 | 160 |
| 26 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 27 | Stochastic reversion · 1h | reversion | 96.56 | -3.44 | 99 | 51.5 | -13.23 | -2.55 | -14.07 | 343 |
| 28 | ADX DI cross · 1h | trend | 96.51 | -3.49 | 62 | 19.4 | -6.75 | -1.10 | -13.79 | 256 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.52 | -2.72 | -8.88 | 305 |
| 30 | MACD cross · 1h | trend | 95.87 | -4.12 | 125 | 24.0 | -11.09 | -1.74 | -17.79 | 460 |
| 31 | Parabolic SAR · 1h | trend | 95.39 | -4.61 | 86 | 22.1 | 2.01 | 0.45 | -21.52 | 289 |
| 32 | EMA 20/50 cross · 1h | trend | 95.38 | -4.62 | 45 | 15.6 | 4.74 | 0.74 | -23.71 | 137 |
| 33 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.95 | -3.86 | -8.72 | 232 |
| 34 | Supertrend · 1h | trend | 94.60 | -5.40 | 58 | 13.8 | 1.33 | 0.36 | -18.92 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.67 | 2.22 | -6.20 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.52 | -6.48 | 39 | 23.1 | 15.62 | 2.48 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.50 | -6.50 | 151 | 32.5 | -7.81 | -1.19 | -16.91 | 129 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.24 | -2.76 | -6.45 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.65 | -7.35 | 66 | 15.2 | -0.62 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.56 | -7.44 | 115 | 43.5 | -18.87 | -6.28 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.54 | -7.46 | 439 | 17.8 | 0.22 | 0.18 | -12.66 | 402 |
| 42 | Volume breakout · 1h | breakout | 91.75 | -8.25 | 70 | 20.0 | 9.17 | 1.40 | -12.60 | 118 |
| 43 | RSI(14) reversion · 1h | reversion | 91.64 | -8.36 | 34 | 26.5 | 0.78 | 0.29 | -9.24 | 129 |
| 44 | Ichimoku · 1h | trend | 91.05 | -8.95 | 48 | 16.7 | 0.99 | 0.33 | -22.34 | 126 |
| 45 | Bollinger breakout · 1h | breakout | 90.89 | -9.11 | 74 | 28.4 | 8.34 | 1.21 | -14.21 | 277 |
| 46 | Triple EMA stack · 1h | trend | 90.75 | -9.25 | 71 | 15.5 | -6.93 | -0.59 | -27.17 | 236 |
| 47 | Bollinger reversion · 1h | reversion | 90.47 | -9.53 | 87 | 35.6 | -23.98 | -5.85 | -24.21 | 315 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.74 | -16.08 | 569 |
| 49 | CCI reversion · 1h | reversion | 89.05 | -10.95 | 113 | 45.1 | -10.86 | -1.47 | -14.35 | 409 |
| 50 | OBV trend · 1h | momentum | 88.75 | -11.25 | 150 | 18.7 | -12.75 | -1.22 | -34.14 | 318 |
| 51 | Williams %R · 1h | reversion | 88.50 | -11.50 | 136 | 44.9 | -26.82 | -4.44 | -28.65 | 507 |
| 52 | VWAP momentum · 1h | momentum | 88.28 | -11.72 | 311 | 23.2 | -33.17 | -4.96 | -40.46 | 1254 |
| 53 | Max aggression: 5-day momentum | meta | 88.13 | -11.87 | 7 | 28.6 | -14.35 | -1.05 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.99 | -12.01 | 130 | 30.8 | -27.94 | -5.37 | -28.20 | 494 |
| 55 | Donchian 20/10 · 1h | breakout | 87.75 | -12.25 | 63 | 17.5 | -0.59 | 0.13 | -19.51 | 214 |
| 56 | Heikin-Ashi · 1h | trend | 87.73 | -12.27 | 153 | 28.1 | -29.98 | -4.98 | -37.65 | 675 |
| 57 | MACD zero-line · 1h | trend | 87.62 | -12.38 | 67 | 17.9 | -20.79 | -3.88 | -21.53 | 231 |
| 58 | EMA 9/21 cross · 1h | trend | 87.14 | -12.86 | 108 | 13.0 | -8.22 | -0.86 | -23.06 | 332 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.07 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.69 | -13.31 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.46 | -13.54 | 153 | 17.0 | -48.29 | -23.54 | -48.29 | 587 |
| 62 | ROC + volume · 1h | momentum | 85.56 | -14.44 | 164 | 20.1 | -9.06 | -1.05 | -25.01 | 401 |
| 63 | ROC + volume | momentum | 72.29 | -27.71 | 421 | 22.3 | -72.90 | -16.58 | -74.60 | 1660 |
| 64 | Squeeze breakout | breakout | 69.52 | -30.48 | 354 | 15.5 | -62.19 | -18.18 | -62.19 | 1221 |
| 65 | Volume breakout | breakout | 69.45 | -30.55 | 279 | 14.7 | -61.61 | -17.60 | -61.61 | 891 |
| 66 | RSI(14) reversion ⏸ | reversion | 69.29 | -30.71 | 422 | 26.3 | -73.71 | -17.31 | -73.71 | 1481 |
| 67 | EMA 20/50 cross | trend | 67.43 | -32.57 | 357 | 19.9 | -76.43 | -15.20 | -76.43 | 1431 |
| 68 | Donchian 55/20 | breakout | 66.63 | -33.37 | 360 | 17.5 | -68.13 | -14.36 | -69.10 | 1289 |
| 69 | VWAP reversion ⏸ | reversion | 63.63 | -36.37 | 464 | 25.2 | -72.75 | -15.45 | -72.75 | 1415 |
| 70 | AI bee: Boozy | ai | 60.33 | -39.66 | 261 | 5.0 | — | — | — | — |
| 71 | Keltner breakout | breakout | 60.30 | -39.70 | 485 | 14.6 | -83.24 | -27.36 | -83.24 | 1835 |
| 72 | Supertrend | trend | 60.00 | -40.00 | 503 | 19.3 | -86.05 | -21.03 | -86.05 | 1892 |
| 73 | Ichimoku | trend | 57.09 | -42.91 | 436 | 9.9 | -82.24 | -23.18 | -82.24 | 1734 |
| 74 | AI bee: Bizzy | ai | 55.31 | -44.69 | 891 | 8.3 | — | — | — | — |
| 75 | Z-score reversion ⏸ | reversion | 55.28 | -44.72 | 567 | 22.0 | -86.20 | -22.51 | -86.20 | 2080 |
| 76 | MFI reversion ⏸ | reversion | 54.75 | -45.25 | 623 | 19.4 | -88.12 | -28.07 | -88.12 | 2122 |
| 77 | ADX DI cross | trend | 53.41 | -46.59 | 599 | 10.0 | -89.14 | -34.59 | -89.14 | 2103 |
| 78 | Donchian 20/10 | breakout | 51.89 | -48.11 | 684 | 17.5 | -90.89 | -26.08 | -90.89 | 2643 |
| 79 | MACD zero-line | trend | 50.91 | -49.09 | 635 | 14.5 | -91.47 | -30.08 | -91.47 | 2344 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.58 | -30.71 | -98.58 | 5308 |
| 81 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.67 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -30.23 | -93.21 | 2596 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.47 | -25.56 | -90.47 | 2358 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.30 | -97.36 | 3516 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -36.26 | -96.38 | 3578 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -25.74 | -94.30 | 2629 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.93 | -99.38 | 5645 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -31.51 | -96.30 | 3592 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.41 | -99.73 | 6144 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.29 | -38.27 | -97.29 | 3652 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.53 | -36.76 | -98.53 | 4667 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.37 | -32.99 | -93.37 | 2792 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.89 | -99.54 | 6110 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -32.81 | -96.03 | 3736 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.76 | -34.32 | -95.76 | 4053 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.89 | -99.89 | 8200 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T23:40 | Stochastic reversion · 1h | sell | XRP-USD | 15.38 | -0.16 | stop-loss |
| 2026-10-12T23:35 | Stochastic reversion · 1h | buy | XRP-USD | 5.03 | — | rebalance up |
| 2026-10-12T23:35 | Stochastic reversion · 1h | buy | BTC-USD | 5.52 | — | rebalance up |
| 2026-10-12T23:35 | Stochastic reversion · 1h | sell | SOL-USD | 10.55 | -0.27 | stop-loss |
| 2026-10-12T23:35 | Bollinger reversion · 1h | buy | XRP-USD | 5.20 | — | rebalance up |
| 2026-10-12T23:35 | Bollinger reversion · 1h | sell | SOL-USD | 11.23 | -0.14 | stop-loss |
| 2026-10-12T23:35 | Bollinger reversion · 1h | sell | BTC-USD | 12.93 | -0.19 | stop-loss |
| 2026-10-12T23:05 | CCI reversion · 1h | sell | BTC-USD | 3.61 | -0.05 | stop-loss |
| 2026-10-12T23:05 | Stochastic reversion · 1h | buy | XRP-USD | 10.51 | — | entry |
| 2026-10-12T23:05 | Stochastic reversion · 1h | sell | DOGE-USD | 10.51 | -0.32 | stop-loss |
| 2026-10-12T23:05 | Z-score reversion · 1h | sell | DOGE-USD | 10.42 | -0.34 | stop-loss |
| 2026-10-12T23:05 | Bollinger reversion · 1h | buy | XRP-USD | 12.96 | — | entry |
| 2026-10-12T23:05 | Bollinger reversion · 1h | sell | DOGE-USD | 12.67 | -0.39 | stop-loss |
| 2026-10-12T23:05 | RSI(14) reversion · 1h | sell | DOGE-USD | 12.72 | -0.39 | stop-loss |
| 2026-10-12T23:05 | Candlestick reversal · 1h | sell | SOL-USD | 8.48 | -0.18 | stop-loss |
| 2026-10-12T23:05 | VWAP reversion | sell | XRP-USD | 12.76 | -0.17 | stop-loss |
| 2026-10-12T23:05 | VWAP reversion | sell | SOL-USD | 15.90 | -0.20 | stop-loss |
| 2026-10-12T23:05 | VWAP reversion | sell | DOGE-USD | 12.68 | -0.26 | stop-loss |
| 2026-10-12T23:05 | RSI(14) reversion | sell | XRP-USD | 17.45 | -0.24 | stop-loss |
| 2026-10-12T23:05 | RSI(14) reversion | sell | SOL-USD | 17.23 | -0.22 | stop-loss |
| 2026-10-12T23:05 | RSI(14) reversion | sell | DOGE-USD | 17.31 | -0.34 | stop-loss |
| 2026-10-12T23:02 | AI bee: Bizzy | sell | SOL-USD | 7.53 | -0.09 | Jev: sell (sell p=0.90) after 11 min |
| 2026-10-12T23:02 | MFI reversion | sell | XRP-USD | 13.71 | -0.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-12T23:02 | MFI reversion | sell | DOGE-USD | 13.65 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-12T23:00 | Williams %R · 1h | sell | SOL-USD | 22.00 | -0.26 | stop-loss |
| 2026-10-12T23:00 | Williams %R · 1h | sell | BTC-USD | 17.85 | -0.21 | stop-loss |
| 2026-10-12T23:00 | Bollinger reversion · 1h | buy | SOL-USD | 11.37 | — | entry |
| 2026-10-12T23:00 | Bollinger reversion · 1h | sell | ETH-USD | 11.94 | -0.29 | stop-loss |
| 2026-10-12T23:00 | RSI(14) reversion · 1h | sell | SOL-USD | 2.20 | -0.04 | stop-loss |
| 2026-10-12T23:00 | MFI reversion | sell | SOL-USD | 13.62 | -0.20 | stop-loss |
| 2026-10-12T23:00 | VWAP reversion | sell | BTC-USD | 12.94 | -0.17 | stop-loss |
| 2026-10-12T23:00 | RSI(14) reversion | sell | ETH-USD | 17.30 | -0.25 | stop-loss |
| 2026-10-12T22:57 | MFI reversion | buy | DOGE-USD | 13.77 | — | entry signal |
| 2026-10-12T22:57 | MFI reversion | sell | ETH-USD | 13.68 | -0.15 | stop-loss |
| 2026-10-12T22:51 | AI bee: Bizzy | buy | SOL-USD | 7.62 | — | Jev: buy (buy p=0.55) |
| 2026-10-12T22:50 | VWAP reversion | buy | SOL-USD | 3.45 | — | rebalance up |
| 2026-10-12T22:50 | VWAP reversion | sell | ETH-USD | 12.80 | -0.11 | stop-loss |
| 2026-10-12T22:46 | VWAP reversion | buy | SOL-USD | 3.21 | — | rebalance up |
| 2026-10-12T22:46 | VWAP reversion | sell | ETH-USD | 3.21 | -0.02 | rebalance down |
| 2026-10-12T22:45 | VWAP reversion | buy | SOL-USD | 9.44 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 23:55:05.000142+00:00 -> 2026-10-13 00:05:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
