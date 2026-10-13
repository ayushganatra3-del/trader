# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T12:55:05.000135+00:00 · 21351 ticks

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
| Copy: Insider buying | 2026-10-13 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 9450 decisions in 1890 calls, $0.1323 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T12:55 | 0 / 4 / 1 | XRP-USD 15%, PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T12:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T12:55 | 1 / 4 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MFI reversion | AAPL | 2.02 | +0.67% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.64 | 2.64 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 101.93 | 1.93 | 16 | 50.0 | -15.08 | -2.39 | -21.97 | 73 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -8.81 | -2.62 | -13.79 | 116 |
| 6 | Hold SPY | benchmark | 101.15 | 1.15 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.95 | 0.95 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.39 | 0.39 | 0 | — | -5.03 | -0.82 | -15.27 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.36 | 0.36 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 15 | Hold BTC | benchmark | 99.43 | -0.57 | 0 | — | 30.07 | 3.50 | -8.68 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.10 | -0.90 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.04 | -1.96 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 97.88 | -2.12 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.75 | -2.25 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.61 | -2.38 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.17 | -2.83 | 105 | 52.4 | -10.68 | -1.98 | -13.91 | 339 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 96.77 | -3.23 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 25 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 26 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 27 | Z-score reversion · 1h | reversion | 96.41 | -3.59 | 47 | 44.7 | 3.29 | 0.78 | -8.60 | 165 |
| 28 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -9.75 | -3.70 | -10.90 | 299 |
| 29 | ADX DI cross · 1h | trend | 96.13 | -3.87 | 63 | 19.0 | -6.03 | -0.96 | -13.79 | 254 |
| 30 | MACD cross · 1h | trend | 95.43 | -4.57 | 125 | 24.0 | -10.29 | -1.59 | -17.79 | 460 |
| 31 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.82 | -3.78 | -8.72 | 231 |
| 32 | Parabolic SAR · 1h | trend | 95.15 | -4.85 | 86 | 22.1 | 2.16 | 0.46 | -21.52 | 288 |
| 33 | EMA 20/50 cross · 1h | trend | 95.09 | -4.91 | 45 | 15.6 | 5.18 | 0.78 | -23.77 | 135 |
| 34 | Supertrend · 1h | trend | 94.31 | -5.69 | 58 | 13.8 | 1.04 | 0.33 | -19.12 | 217 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.38 | -6.62 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.22 | -6.79 | 151 | 32.5 | -7.54 | -1.13 | -16.91 | 130 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.23 | -2.74 | -6.45 | 113 |
| 39 | RSI momentum · 1h | momentum | 92.37 | -7.63 | 66 | 15.2 | -0.38 | 0.16 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.28 | -7.72 | 115 | 43.5 | -18.94 | -6.26 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.26 | -7.74 | 439 | 17.8 | -0.39 | 0.06 | -12.15 | 400 |
| 42 | Volume breakout · 1h | breakout | 91.54 | -8.46 | 70 | 20.0 | 9.08 | 1.38 | -12.60 | 117 |
| 43 | RSI(14) reversion · 1h | reversion | 91.35 | -8.65 | 36 | 30.6 | -2.00 | -0.32 | -9.40 | 143 |
| 44 | Ichimoku · 1h | trend | 90.79 | -9.21 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger reversion · 1h | reversion | 90.70 | -9.30 | 93 | 37.6 | -23.66 | -5.71 | -24.41 | 319 |
| 46 | Bollinger breakout · 1h | breakout | 90.69 | -9.31 | 74 | 28.4 | 8.34 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.47 | -9.53 | 71 | 15.5 | -7.13 | -0.62 | -27.18 | 237 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 88.96 | -11.04 | 141 | 46.1 | -25.28 | -4.11 | -28.82 | 506 |
| 50 | CCI reversion · 1h | reversion | 88.76 | -11.23 | 114 | 45.6 | -9.99 | -1.32 | -14.35 | 410 |
| 51 | OBV trend · 1h | momentum | 88.48 | -11.52 | 150 | 18.7 | -12.43 | -1.17 | -34.14 | 317 |
| 52 | VWAP momentum · 1h | momentum | 88.02 | -11.98 | 311 | 23.2 | -32.83 | -4.87 | -40.31 | 1255 |
| 53 | Max aggression: 5-day momentum | meta | 87.87 | -12.13 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.81 | -12.19 | 130 | 30.8 | -29.88 | -5.67 | -29.98 | 502 |
| 55 | Donchian 20/10 · 1h | breakout | 87.49 | -12.51 | 63 | 17.5 | -0.70 | 0.12 | -19.51 | 215 |
| 56 | MACD zero-line · 1h | trend | 87.22 | -12.78 | 67 | 17.9 | -20.45 | -3.78 | -21.66 | 230 |
| 57 | Heikin-Ashi · 1h | trend | 87.02 | -12.97 | 158 | 27.2 | -30.40 | -5.03 | -38.03 | 680 |
| 58 | EMA 9/21 cross · 1h | trend | 86.75 | -13.25 | 109 | 12.8 | -7.41 | -0.75 | -23.22 | 330 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.42 | -13.58 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.19 | -13.81 | 156 | 17.3 | -48.04 | -22.98 | -48.12 | 585 |
| 62 | ROC + volume · 1h | momentum | 85.30 | -14.70 | 164 | 20.1 | -8.89 | -1.02 | -25.13 | 396 |
| 63 | ROC + volume | momentum | 73.36 | -26.64 | 426 | 23.0 | -72.38 | -15.90 | -74.73 | 1660 |
| 64 | Squeeze breakout | breakout | 69.22 | -30.78 | 356 | 15.4 | -62.07 | -17.94 | -62.07 | 1219 |
| 65 | Volume breakout | breakout | 68.85 | -31.15 | 285 | 14.7 | -61.24 | -17.29 | -61.24 | 887 |
| 66 | EMA 20/50 cross | trend | 67.43 | -32.57 | 362 | 20.4 | -76.11 | -14.86 | -76.21 | 1429 |
| 67 | RSI(14) reversion | reversion | 66.94 | -33.06 | 442 | 26.5 | -74.43 | -17.54 | -74.46 | 1494 |
| 68 | Donchian 55/20 | breakout | 66.43 | -33.57 | 365 | 17.5 | -68.07 | -14.19 | -69.19 | 1290 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -72.79 | -15.45 | -72.82 | 1415 |
| 70 | Keltner breakout | breakout | 60.63 | -39.37 | 492 | 15.4 | -82.87 | -25.92 | -83.05 | 1831 |
| 71 | Supertrend | trend | 60.10 | -39.90 | 510 | 20.0 | -85.75 | -20.37 | -85.88 | 1893 |
| 72 | AI bee: Boozy | ai | 59.91 | -40.09 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.54 | -43.46 | 440 | 9.8 | -82.14 | -22.74 | -82.14 | 1729 |
| 74 | AI bee: Bizzy | ai | 54.26 | -45.74 | 913 | 8.2 | — | — | — | — |
| 75 | MFI reversion | reversion | 54.22 | -45.78 | 634 | 19.9 | -87.90 | -27.62 | -87.93 | 2114 |
| 76 | Z-score reversion | reversion | 53.04 | -46.96 | 590 | 21.9 | -86.30 | -22.49 | -86.32 | 2081 |
| 77 | ADX DI cross | trend | 52.82 | -47.18 | 616 | 10.6 | -89.13 | -33.94 | -89.18 | 2116 |
| 78 | Donchian 20/10 | breakout | 52.22 | -47.78 | 693 | 18.0 | -90.56 | -24.92 | -90.69 | 2636 |
| 79 | MACD zero-line | trend | 51.23 | -48.77 | 640 | 15.2 | -91.24 | -28.69 | -91.32 | 2340 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.49 | -29.03 | -98.52 | 5294 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.02 | -28.85 | -93.06 | 2588 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.21 | -24.39 | -90.34 | 2355 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.32 | -26.46 | -91.32 | 2328 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.25 | -31.49 | -97.29 | 3509 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -34.62 | -96.30 | 3574 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.32 | -25.35 | -94.32 | 2633 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.62 | -99.38 | 5648 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.39 | -31.48 | -96.39 | 3609 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.77 | -99.72 | 6137 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.29 | -37.10 | -97.29 | 3650 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -36.40 | -98.54 | 4669 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.22 | -31.73 | -93.22 | 2785 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.50 | -99.55 | 6113 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.05 | -32.93 | -96.05 | 3732 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -34.03 | -95.75 | 4046 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -45.78 | -99.89 | 8199 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T12:54 | AI bee: Bizzy | buy | XRP-USD | 8.03 | — | Jev: buy (buy p=0.59) |
| 2026-10-13T12:52 | Supertrend | buy | XRP-USD | 3.00 | — | rebalance up |
| 2026-10-13T12:52 | Supertrend | sell | ETH-USD | 3.00 | -0.03 | rebalance down |
| 2026-10-13T12:50 | Z-score reversion | sell | XRP-USD | 13.35 | 0.03 | exit signal |
| 2026-10-13T12:50 | Z-score reversion | sell | ETH-USD | 13.35 | -0.03 | exit signal |
| 2026-10-13T12:50 | RSI(14) reversion | sell | XRP-USD | 16.97 | 0.05 | take-profit |
| 2026-10-13T12:50 | Supertrend | buy | XRP-USD | 3.05 | — | entry signal |
| 2026-10-13T12:50 | Supertrend | sell | DOGE-USD | 3.05 | -0.02 | rebalance down |
| 2026-10-13T12:50 | MACD zero-line | buy | XRP-USD | 12.84 | — | entry signal |
| 2026-10-13T12:50 | MACD zero-line | buy | DOGE-USD | 12.84 | — | entry signal |
| 2026-10-13T12:40 | ADX DI cross | buy | SOL-USD | 13.21 | — | entry signal |
| 2026-10-13T12:30 | ADX DI cross | buy | ETH-USD | 13.22 | — | entry signal |
| 2026-10-13T12:30 | ADX DI cross | buy | DOGE-USD | 13.22 | — | entry signal |
| 2026-10-13T12:22 | AI bee: Bizzy | sell | XRP-USD | 7.55 | -0.07 | Jev: sell (sell p=0.90) after 12 min |
| 2026-10-13T12:15 | Z-score reversion | sell | DOGE-USD | 13.19 | -0.09 | stop-loss |
| 2026-10-13T12:15 | RSI(14) reversion | sell | DOGE-USD | 16.65 | -0.11 | stop-loss |
| 2026-10-13T12:15 | ADX DI cross | sell | ETH-USD | 13.15 | -0.09 | exit signal |
| 2026-10-13T12:10 | AI bee: Bizzy | buy | XRP-USD | 7.62 | — | Jev: buy (buy p=0.56) |
| 2026-10-13T12:10 | Z-score reversion | buy | DOGE-USD | 13.28 | — | entry |
| 2026-10-13T12:10 | RSI(14) reversion | buy | DOGE-USD | 16.76 | — | entry |
| 2026-10-13T12:10 | ADX DI cross | buy | ETH-USD | 13.24 | — | entry signal |
| 2026-10-13T12:05 | Z-score reversion | sell | DOGE-USD | 13.18 | -0.18 | stop-loss |
| 2026-10-13T12:05 | RSI(14) reversion | sell | DOGE-USD | 16.68 | -0.23 | stop-loss |
| 2026-10-13T12:05 | ADX DI cross | sell | ETH-USD | 10.59 | -0.12 | exit signal |
| 2026-10-13T12:00 | MFI reversion | sell | BTC-USD | 13.52 | -0.13 | stop-loss |
| 2026-10-13T11:55 | MFI reversion | sell | SOL-USD | 13.44 | -0.21 | stop-loss |
| 2026-10-13T11:55 | RSI(14) reversion | sell | SOL-USD | 16.66 | -0.26 | stop-loss |
| 2026-10-13T11:55 | ADX DI cross | sell | XRP-USD | 10.61 | -0.10 | exit signal |
| 2026-10-13T11:55 | ADX DI cross | sell | SOL-USD | 10.55 | -0.16 | stop-loss |
| 2026-10-13T11:55 | ADX DI cross | sell | DOGE-USD | 10.60 | -0.12 | exit signal |
| 2026-10-13T11:55 | ADX DI cross | sell | BTC-USD | 10.62 | -0.10 | exit signal |
| 2026-10-13T11:35 | AI bee: Bizzy | sell | DOGE-USD | 8.26 | -0.09 | Jev: sell (sell p=0.62) after 11 min |
| 2026-10-13T11:25 | MFI reversion | buy | XRP-USD | 13.65 | — | entry signal |
| 2026-10-13T11:25 | MFI reversion | buy | SOL-USD | 13.65 | — | entry signal |
| 2026-10-13T11:25 | MFI reversion | buy | BTC-USD | 13.65 | — | entry signal |
| 2026-10-13T11:25 | Z-score reversion | buy | DOGE-USD | 13.36 | — | entry signal |
| 2026-10-13T11:25 | Z-score reversion | sell | BTC-USD | 13.38 | -0.02 | exit signal |
| 2026-10-13T11:25 | RSI(14) reversion | buy | SOL-USD | 16.91 | — | entry signal |
| 2026-10-13T11:25 | RSI(14) reversion | buy | DOGE-USD | 16.91 | — | entry signal |
| 2026-10-13T11:25 | RSI(14) reversion | sell | ETH-USD | 13.58 | 0.00 | take-profit |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 12:55:05.000135+00:00 -> 2026-10-13 13:05:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
