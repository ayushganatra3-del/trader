# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T08:55:05.000179+00:00 · 21149 ticks

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
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 6420 decisions in 1284 calls, $0.0899 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T08:55 | 0 / 1 / 4 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T08:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T08:55 | 1 / 3 / 1 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.72 | 2.72 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.01 | 2.01 | 16 | 50.0 | -15.07 | -2.39 | -21.97 | 73 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -8.80 | -2.61 | -13.79 | 117 |
| 6 | Hold SPY | benchmark | 101.23 | 1.24 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.03 | 1.03 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.46 | 0.46 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.44 | 0.43 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.94 | -0.06 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 15 | Hold BTC | benchmark | 99.88 | -0.12 | 0 | — | 30.00 | 3.48 | -8.68 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.18 | -0.82 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.10 | -1.90 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 97.95 | -2.05 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.82 | -2.18 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.69 | -2.31 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.22 | -2.78 | 105 | 52.4 | -10.83 | -2.01 | -13.91 | 341 |
| 24 | Three white soldiers · 1h | momentum | 97.04 | -2.96 | 8 | 0.0 | -3.46 | -2.65 | -4.64 | 29 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.84 | -3.16 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 26 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 27 | Z-score reversion · 1h | reversion | 96.55 | -3.45 | 47 | 44.7 | 3.56 | 0.83 | -8.60 | 165 |
| 28 | ADX DI cross · 1h | trend | 96.28 | -3.72 | 62 | 19.4 | -5.59 | -0.88 | -13.79 | 252 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -8.05 | -3.38 | -9.43 | 322 |
| 30 | MACD cross · 1h | trend | 95.68 | -4.32 | 125 | 24.0 | -10.80 | -1.68 | -17.79 | 463 |
| 31 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.86 | -3.80 | -8.72 | 230 |
| 32 | Parabolic SAR · 1h | trend | 95.21 | -4.79 | 86 | 22.1 | 2.00 | 0.44 | -21.52 | 289 |
| 33 | EMA 20/50 cross · 1h | trend | 95.16 | -4.84 | 45 | 15.6 | 4.90 | 0.75 | -23.71 | 136 |
| 34 | Supertrend · 1h | trend | 94.38 | -5.62 | 58 | 13.8 | 0.67 | 0.28 | -18.92 | 218 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.42 | -6.58 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.27 | -6.73 | 151 | 32.5 | -7.13 | -1.05 | -16.91 | 131 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.27 | -2.76 | -6.49 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.44 | -7.56 | 66 | 15.2 | -0.69 | 0.12 | -23.02 | 230 |
| 40 | Connors RSI(2) · 1h | reversion | 92.35 | -7.65 | 115 | 43.5 | -18.94 | -6.26 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.33 | -7.67 | 439 | 17.8 | 0.20 | 0.17 | -12.62 | 399 |
| 42 | Volume breakout · 1h | breakout | 91.59 | -8.41 | 70 | 20.0 | 9.16 | 1.39 | -12.60 | 116 |
| 43 | RSI(14) reversion · 1h | reversion | 91.52 | -8.48 | 36 | 30.6 | 1.97 | 0.55 | -9.40 | 130 |
| 44 | Ichimoku · 1h | trend | 90.85 | -9.15 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger reversion · 1h | reversion | 90.74 | -9.26 | 93 | 37.6 | -23.67 | -5.71 | -24.41 | 319 |
| 46 | Bollinger breakout · 1h | breakout | 90.74 | -9.26 | 74 | 28.4 | 8.33 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.55 | -9.46 | 71 | 15.5 | -6.99 | -0.60 | -27.17 | 236 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 88.99 | -11.01 | 141 | 46.1 | -25.27 | -4.10 | -28.82 | 509 |
| 50 | CCI reversion · 1h | reversion | 88.84 | -11.16 | 114 | 45.6 | -9.75 | -1.28 | -14.35 | 410 |
| 51 | OBV trend · 1h | momentum | 88.55 | -11.45 | 150 | 18.7 | -12.55 | -1.19 | -34.15 | 318 |
| 52 | VWAP momentum · 1h | momentum | 88.08 | -11.92 | 311 | 23.2 | -32.54 | -4.81 | -40.18 | 1254 |
| 53 | Candlestick reversal · 1h | reversion | 87.98 | -12.02 | 130 | 30.8 | -26.89 | -5.11 | -27.05 | 485 |
| 54 | Max aggression: 5-day momentum | meta | 87.93 | -12.06 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 55 | Heikin-Ashi · 1h | trend | 87.65 | -12.35 | 153 | 28.1 | -29.93 | -4.93 | -37.81 | 680 |
| 56 | Donchian 20/10 · 1h | breakout | 87.55 | -12.45 | 63 | 17.5 | -0.66 | 0.13 | -19.51 | 215 |
| 57 | MACD zero-line · 1h | trend | 87.36 | -12.64 | 67 | 17.9 | -20.37 | -3.76 | -21.55 | 230 |
| 58 | EMA 9/21 cross · 1h | trend | 86.89 | -13.11 | 108 | 13.0 | -8.60 | -0.91 | -23.06 | 335 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.29 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.49 | -13.51 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.19 | -13.81 | 156 | 17.3 | -48.13 | -23.09 | -48.13 | 586 |
| 62 | ROC + volume · 1h | momentum | 85.37 | -14.63 | 164 | 20.1 | -8.89 | -1.02 | -25.13 | 396 |
| 63 | ROC + volume | momentum | 73.36 | -26.64 | 426 | 23.0 | -72.38 | -15.90 | -74.72 | 1659 |
| 64 | Squeeze breakout | breakout | 69.22 | -30.78 | 356 | 15.4 | -62.22 | -18.02 | -62.22 | 1221 |
| 65 | Volume breakout | breakout | 68.85 | -31.15 | 285 | 14.7 | -61.63 | -17.54 | -61.63 | 892 |
| 66 | RSI(14) reversion | reversion | 68.73 | -31.27 | 430 | 27.0 | -73.88 | -17.25 | -74.06 | 1485 |
| 67 | EMA 20/50 cross | trend | 67.97 | -32.03 | 357 | 19.9 | -75.91 | -14.70 | -76.20 | 1429 |
| 68 | Donchian 55/20 | breakout | 66.55 | -33.45 | 364 | 17.6 | -68.00 | -14.15 | -69.18 | 1290 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -73.10 | -15.51 | -73.13 | 1416 |
| 70 | Supertrend | trend | 60.66 | -39.34 | 509 | 19.8 | -85.69 | -20.19 | -85.95 | 1889 |
| 71 | Keltner breakout | breakout | 60.63 | -39.37 | 492 | 15.4 | -83.00 | -26.18 | -83.18 | 1835 |
| 72 | AI bee: Boozy | ai | 59.91 | -40.09 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.54 | -43.46 | 440 | 9.8 | -82.11 | -22.69 | -82.11 | 1728 |
| 74 | MFI reversion | reversion | 55.26 | -44.74 | 628 | 20.1 | -87.84 | -26.97 | -88.04 | 2111 |
| 75 | Z-score reversion | reversion | 54.68 | -45.32 | 576 | 22.2 | -86.19 | -22.35 | -86.38 | 2077 |
| 76 | AI bee: Bizzy | ai | 54.61 | -45.39 | 909 | 8.3 | — | — | — | — |
| 77 | ADX DI cross | trend | 53.59 | -46.41 | 610 | 10.7 | -88.99 | -33.13 | -89.06 | 2107 |
| 78 | Donchian 20/10 | breakout | 52.22 | -47.78 | 693 | 18.0 | -90.65 | -25.09 | -90.76 | 2640 |
| 79 | MACD zero-line | trend | 51.34 | -48.66 | 640 | 15.2 | -91.23 | -28.63 | -91.34 | 2339 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.49 | -28.92 | -98.54 | 5293 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.02 | -28.85 | -93.06 | 2588 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.20 | -24.35 | -90.34 | 2354 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.31 | -26.42 | -91.31 | 2329 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.25 | -31.38 | -97.30 | 3507 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -34.39 | -96.29 | 3574 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -25.31 | -94.30 | 2631 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.86 | -99.37 | 5632 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.35 | -31.15 | -96.35 | 3604 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.30 | -99.72 | 6134 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.25 | -36.65 | -97.25 | 3645 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.93 | -98.52 | 4663 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.27 | -31.93 | -93.27 | 2789 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.87 | -99.54 | 6106 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.05 | -32.55 | -96.06 | 3729 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.75 | -33.84 | -95.77 | 4044 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.75 | -99.89 | 8201 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T08:55 | Donchian 55/20 | sell | SOL-USD | 16.60 | -0.11 | exit signal |
| 2026-10-13T08:55 | Donchian 55/20 | sell | BTC-USD | 13.33 | 0.02 | exit signal |
| 2026-10-13T08:55 | Donchian 20/10 | sell | XRP-USD | 10.46 | -0.10 | exit signal |
| 2026-10-13T08:55 | Supertrend | sell | SOL-USD | 15.12 | -0.20 | exit signal |
| 2026-10-13T08:50 | Donchian 55/20 | buy | SOL-USD | 3.38 | — | rebalance up |
| 2026-10-13T08:50 | Donchian 55/20 | sell | ETH-USD | 13.35 | -0.00 | exit signal |
| 2026-10-13T08:50 | Donchian 55/20 | sell | DOGE-USD | 13.29 | -0.06 | exit signal |
| 2026-10-13T08:50 | ADX DI cross | sell | ETH-USD | 10.83 | 0.18 | exit signal |
| 2026-10-13T08:50 | Supertrend | buy | SOL-USD | 6.21 | — | rebalance up |
| 2026-10-13T08:50 | Supertrend | sell | ETH-USD | 12.24 | 0.26 | exit signal |
| 2026-10-13T08:50 | Supertrend | sell | DOGE-USD | 15.14 | -0.16 | exit signal |
| 2026-10-13T08:50 | Supertrend | sell | BTC-USD | 12.16 | 0.09 | exit signal |
| 2026-10-13T08:45 | ADX DI cross | sell | BTC-USD | 10.79 | 0.09 | exit signal |
| 2026-10-13T08:40 | Donchian 20/10 | sell | SOL-USD | 13.05 | -0.16 | stop-loss |
| 2026-10-13T08:40 | Donchian 20/10 | sell | ETH-USD | 13.06 | -0.13 | stop-loss |
| 2026-10-13T08:40 | Donchian 20/10 | sell | BTC-USD | 10.49 | 0.09 | exit signal |
| 2026-10-13T08:40 | Ichimoku | sell | ETH-USD | 14.10 | -0.15 | exit signal |
| 2026-10-13T08:40 | ADX DI cross | sell | XRP-USD | 13.40 | -0.09 | exit signal |
| 2026-10-13T08:40 | ADX DI cross | sell | SOL-USD | 13.39 | -0.12 | exit signal |
| 2026-10-13T08:35 | Ichimoku | sell | SOL-USD | 14.10 | -0.15 | exit signal |
| 2026-10-13T08:30 | Squeeze breakout | sell | BTC-USD | 17.20 | -0.14 | stop-loss |
| 2026-10-13T08:30 | Keltner breakout | sell | BTC-USD | 15.07 | -0.12 | stop-loss |
| 2026-10-13T08:30 | Donchian 20/10 | buy | SOL-USD | 2.65 | — | rebalance up |
| 2026-10-13T08:30 | Donchian 20/10 | buy | ETH-USD | 2.63 | — | rebalance up |
| 2026-10-13T08:30 | Donchian 20/10 | sell | DOGE-USD | 10.45 | -0.09 | exit signal |
| 2026-10-13T08:30 | Ichimoku | sell | DOGE-USD | 14.09 | -0.15 | stop-loss |
| 2026-10-13T08:30 | ADX DI cross | buy | XRP-USD | 2.84 | — | rebalance up |
| 2026-10-13T08:30 | ADX DI cross | buy | SOL-USD | 2.72 | — | rebalance up |
| 2026-10-13T08:30 | ADX DI cross | sell | DOGE-USD | 10.74 | -0.07 | exit signal |
| 2026-10-13T08:25 | Volume breakout | sell | BTC-USD | 17.10 | -0.15 | exit signal |
| 2026-10-13T08:23 | AI bee: Bizzy | sell | BTC-USD | 7.68 | -0.05 | Jev: sell (sell p=0.64) after 10 min |
| 2026-10-13T08:20 | Three white soldiers | sell | BTC-USD | 21.42 | -0.17 | stop-loss |
| 2026-10-13T08:16 | Three white soldiers | buy | BTC-USD | 21.59 | — | entry signal |
| 2026-10-13T08:16 | Volume breakout | buy | BTC-USD | 17.25 | — | entry signal |
| 2026-10-13T08:16 | Ichimoku | buy | SOL-USD | 14.25 | — | entry signal |
| 2026-10-13T08:16 | Ichimoku | buy | ETH-USD | 14.25 | — | entry signal |
| 2026-10-13T08:16 | Ichimoku | buy | DOGE-USD | 14.25 | — | entry signal |
| 2026-10-13T08:13 | AI bee: Bizzy | buy | BTC-USD | 7.74 | — | Jev: buy (buy p=0.57) |
| 2026-10-13T08:01 | ADX DI cross · 1h | buy | ETH-USD | 7.98 | — | entry signal |
| 2026-10-13T08:01 | EMA 9/21 cross · 1h | buy | ETH-USD | 2.92 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 08:55:05.000179+00:00 -> 2026-10-13 09:05:05.000179+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
