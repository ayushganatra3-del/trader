# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T00:28:05.000163+00:00 · 20743 ticks

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

Today: 330 decisions in 66 calls, $0.0047 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T00:28 | 0 / 1 / 4 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T00:28 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T00:28 | 1 / 4 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Z-score reversion | AAPL | 1.77 | +1.13% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.93 | 2.93 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.07 | 2.07 | 16 | 50.0 | -12.86 | -2.12 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Hold SPY | benchmark | 101.44 | 1.44 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -9.54 | -2.84 | -13.79 | 119 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.23 | 1.23 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.66 | 0.67 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.64 | 0.64 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.14 | 0.14 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.38 | -0.62 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 18 | Donchian 55/20 · 1h | breakout | 98.25 | -1.75 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 19 | Daily: Bullish score | daily | 98.15 | -1.85 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 20 | Max aggression: 1-day momentum | meta | 98.02 | -1.98 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 21 | Trend pullback · 1h | trend | 97.89 | -2.11 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 22 | Hold BTC | benchmark | 97.58 | -2.42 | 0 | — | 27.47 | 3.25 | -8.68 | 1 |
| 23 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.04 | -2.96 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 25 | Z-score reversion · 1h | reversion | 96.71 | -3.29 | 45 | 42.2 | 3.17 | 0.76 | -8.60 | 160 |
| 26 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 27 | ADX DI cross · 1h | trend | 96.49 | -3.51 | 62 | 19.4 | -6.05 | -0.96 | -13.79 | 253 |
| 28 | Stochastic reversion · 1h | reversion | 96.44 | -3.56 | 100 | 51.0 | -13.24 | -2.54 | -13.95 | 342 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.66 | -2.75 | -9.02 | 309 |
| 30 | MACD cross · 1h | trend | 95.86 | -4.14 | 125 | 24.0 | -10.99 | -1.71 | -17.79 | 459 |
| 31 | Parabolic SAR · 1h | trend | 95.37 | -4.63 | 86 | 22.1 | 2.00 | 0.44 | -21.52 | 289 |
| 32 | EMA 20/50 cross · 1h | trend | 95.36 | -4.64 | 45 | 15.6 | 4.90 | 0.75 | -23.71 | 136 |
| 33 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -8.00 | -3.86 | -8.72 | 231 |
| 34 | Supertrend · 1h | trend | 94.57 | -5.43 | 58 | 13.8 | 1.32 | 0.36 | -18.92 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.51 | -6.49 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.46 | -6.54 | 151 | 32.5 | -7.70 | -1.15 | -16.91 | 129 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.27 | -2.76 | -6.49 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.63 | -7.37 | 66 | 15.2 | -0.63 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.54 | -7.46 | 115 | 43.5 | -18.87 | -6.23 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.52 | -7.48 | 439 | 17.8 | 1.25 | 0.36 | -12.67 | 394 |
| 42 | Volume breakout · 1h | breakout | 91.74 | -8.27 | 70 | 20.0 | 9.16 | 1.39 | -12.60 | 116 |
| 43 | RSI(14) reversion · 1h | reversion | 91.62 | -8.38 | 34 | 26.5 | 0.50 | 0.23 | -9.24 | 129 |
| 44 | Ichimoku · 1h | trend | 91.03 | -8.97 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger breakout · 1h | breakout | 90.88 | -9.12 | 74 | 28.4 | 8.33 | 1.20 | -14.21 | 277 |
| 46 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 71 | 15.5 | -6.93 | -0.59 | -27.17 | 236 |
| 47 | Bollinger reversion · 1h | reversion | 90.36 | -9.64 | 88 | 35.2 | -24.07 | -5.84 | -24.28 | 315 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | CCI reversion · 1h | reversion | 89.02 | -10.98 | 113 | 45.1 | -10.90 | -1.46 | -14.35 | 409 |
| 50 | OBV trend · 1h | momentum | 88.73 | -11.27 | 150 | 18.7 | -12.84 | -1.22 | -34.15 | 319 |
| 51 | Williams %R · 1h | reversion | 88.49 | -11.51 | 136 | 44.9 | -26.82 | -4.41 | -28.66 | 507 |
| 52 | VWAP momentum · 1h | momentum | 88.26 | -11.74 | 311 | 23.2 | -32.82 | -4.87 | -40.20 | 1251 |
| 53 | Max aggression: 5-day momentum | meta | 88.12 | -11.88 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.98 | -12.02 | 130 | 30.8 | -28.75 | -5.49 | -28.75 | 496 |
| 55 | Donchian 20/10 · 1h | breakout | 87.73 | -12.27 | 63 | 17.5 | -0.60 | 0.13 | -19.51 | 214 |
| 56 | Heikin-Ashi · 1h | trend | 87.72 | -12.28 | 153 | 28.1 | -29.97 | -4.94 | -37.65 | 675 |
| 57 | MACD zero-line · 1h | trend | 87.61 | -12.39 | 67 | 17.9 | -21.01 | -3.89 | -21.53 | 232 |
| 58 | EMA 9/21 cross · 1h | trend | 87.12 | -12.88 | 108 | 13.0 | -8.23 | -0.86 | -23.06 | 332 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.29 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.66 | -13.34 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.46 | -13.54 | 153 | 17.0 | -48.29 | -23.12 | -48.29 | 587 |
| 62 | ROC + volume · 1h | momentum | 85.54 | -14.46 | 164 | 20.1 | -9.06 | -1.05 | -25.01 | 401 |
| 63 | ROC + volume | momentum | 72.29 | -27.71 | 421 | 22.3 | -72.90 | -16.38 | -74.61 | 1656 |
| 64 | Squeeze breakout | breakout | 69.52 | -30.48 | 354 | 15.5 | -62.32 | -17.98 | -62.32 | 1223 |
| 65 | Volume breakout | breakout | 69.45 | -30.55 | 279 | 14.7 | -61.65 | -17.41 | -61.65 | 893 |
| 66 | RSI(14) reversion | reversion | 68.73 | -31.27 | 423 | 26.2 | -73.98 | -17.29 | -74.01 | 1485 |
| 67 | EMA 20/50 cross | trend | 67.43 | -32.57 | 357 | 19.9 | -76.39 | -15.01 | -76.39 | 1430 |
| 68 | Donchian 55/20 | breakout | 66.63 | -33.37 | 360 | 17.5 | -68.13 | -14.21 | -69.10 | 1289 |
| 69 | VWAP reversion | reversion | 62.83 | -37.17 | 469 | 24.9 | -73.08 | -15.47 | -73.08 | 1415 |
| 70 | AI bee: Boozy | ai | 60.33 | -39.66 | 261 | 5.0 | — | — | — | — |
| 71 | Keltner breakout | breakout | 60.30 | -39.70 | 485 | 14.6 | -83.21 | -26.74 | -83.21 | 1834 |
| 72 | Supertrend | trend | 60.00 | -40.00 | 503 | 19.3 | -86.04 | -20.71 | -86.04 | 1891 |
| 73 | Ichimoku | trend | 57.09 | -42.91 | 436 | 9.9 | -82.15 | -22.70 | -82.15 | 1731 |
| 74 | AI bee: Bizzy | ai | 55.31 | -44.69 | 891 | 8.3 | — | — | — | — |
| 75 | MFI reversion | reversion | 54.69 | -45.31 | 623 | 19.4 | -88.12 | -27.55 | -88.12 | 2119 |
| 76 | Z-score reversion | reversion | 54.57 | -45.43 | 570 | 21.9 | -86.35 | -22.42 | -86.35 | 2082 |
| 77 | ADX DI cross | trend | 53.41 | -46.59 | 599 | 10.0 | -89.15 | -33.58 | -89.15 | 2103 |
| 78 | Donchian 20/10 | breakout | 51.89 | -48.11 | 684 | 17.5 | -90.87 | -25.55 | -90.87 | 2642 |
| 79 | MACD zero-line | trend | 50.91 | -49.09 | 635 | 14.5 | -91.48 | -29.36 | -91.48 | 2344 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.57 | -29.93 | -98.57 | 5310 |
| 81 | Trend pullback | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.12 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.15 | -29.35 | -93.15 | 2592 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.44 | -25.01 | -90.44 | 2356 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -32.37 | -97.36 | 3516 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.36 | -34.98 | -96.36 | 3578 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.27 | -25.14 | -94.27 | 2623 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -35.89 | -99.38 | 5641 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -30.70 | -96.29 | 3591 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.71 | -99.73 | 6144 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.28 | -36.87 | -97.28 | 3650 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.55 | -35.89 | -98.55 | 4670 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.36 | -32.07 | -93.36 | 2791 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -38.68 | -99.55 | 6114 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.06 | -32.23 | -96.06 | 3738 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.79 | -33.71 | -95.80 | 4053 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -44.68 | -99.89 | 8198 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T00:25 | Z-score reversion | buy | ETH-USD | 13.66 | — | entry signal |
| 2026-10-13T00:25 | Z-score reversion | buy | BTC-USD | 13.66 | — | entry signal |
| 2026-10-13T00:15 | MFI reversion | buy | ETH-USD | 13.69 | — | entry signal |
| 2026-10-13T00:10 | Stochastic reversion · 1h | sell | BTC-USD | 15.98 | -0.30 | stop-loss |
| 2026-10-13T00:10 | Bollinger reversion · 1h | sell | XRP-USD | 17.96 | -0.21 | stop-loss |
| 2026-10-13T00:10 | VWAP reversion | sell | XRP-USD | 12.60 | -0.12 | exit signal |
| 2026-10-13T00:10 | VWAP reversion | sell | SOL-USD | 12.48 | -0.24 | stop-loss |
| 2026-10-13T00:10 | VWAP reversion | sell | ETH-USD | 12.55 | -0.17 | stop-loss |
| 2026-10-13T00:10 | VWAP reversion | sell | DOGE-USD | 12.59 | -0.14 | exit signal |
| 2026-10-13T00:10 | VWAP reversion | sell | BTC-USD | 12.60 | -0.13 | stop-loss |
| 2026-10-13T00:10 | Z-score reversion | sell | SOL-USD | 10.85 | -0.21 | stop-loss |
| 2026-10-13T00:10 | Z-score reversion | sell | ETH-USD | 13.64 | -0.18 | stop-loss |
| 2026-10-13T00:10 | RSI(14) reversion | sell | SOL-USD | 16.99 | -0.33 | stop-loss |
| 2026-10-13T00:05 | Z-score reversion | buy | ETH-USD | 2.77 | — | rebalance up |
| 2026-10-13T00:05 | Z-score reversion | buy | DOGE-USD | 2.76 | — | rebalance up |
| 2026-10-13T00:05 | Z-score reversion | sell | BTC-USD | 10.98 | -0.08 | stop-loss |
| 2026-10-13T00:01 | VWAP reversion | buy | XRP-USD | 12.73 | — | entry |
| 2026-10-13T00:01 | VWAP reversion | buy | SOL-USD | 12.73 | — | entry |
| 2026-10-13T00:01 | VWAP reversion | buy | ETH-USD | 12.73 | — | entry |
| 2026-10-13T00:01 | VWAP reversion | buy | DOGE-USD | 12.73 | — | entry |
| 2026-10-13T00:01 | VWAP reversion | buy | BTC-USD | 12.73 | — | entry |
| 2026-10-13T00:01 | Z-score reversion | buy | XRP-USD | 11.06 | — | entry |
| 2026-10-13T00:01 | Z-score reversion | buy | SOL-USD | 11.06 | — | entry |
| 2026-10-13T00:01 | Z-score reversion | buy | ETH-USD | 11.06 | — | entry |
| 2026-10-13T00:01 | Z-score reversion | buy | DOGE-USD | 11.06 | — | entry |
| 2026-10-13T00:01 | Z-score reversion | buy | BTC-USD | 11.06 | — | entry |
| 2026-10-13T00:01 | RSI(14) reversion | buy | XRP-USD | 17.32 | — | entry |
| 2026-10-13T00:01 | RSI(14) reversion | buy | SOL-USD | 17.32 | — | entry |
| 2026-10-13T00:01 | RSI(14) reversion | buy | DOGE-USD | 17.32 | — | entry |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 00:28:05.000163+00:00 -> 2026-10-13 00:38:05.000163+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
