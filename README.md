# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T17:25:05.000145+00:00 · 21553 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.07 (-4.93%)

Closed trades 61, win rate 47.5%, fees £2.31, max drawdown -5.37%.

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

Today: 25692 decisions in 2496 calls, $0.3232 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T17:25 | 2 / 15 / 12 | cash |  |
| Breezy | 2026-10-13T17:25 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-13T17:25 | 0 / 27 / 2 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.18 | +2.49% | 5 |
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.58 | 3.58 | 0 | — | 2.41 | 1.20 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -8.89 | -2.64 | -13.79 | 115 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | Hold SPY | benchmark | 101.00 | 1.00 | 0 | — | 0.48 | 0.33 | -3.66 | 1 |
| 6 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.89 | 0.89 | 11 | 36.4 | 5.09 | 1.58 | -7.55 | 43 |
| 7 | Copy: Insider buying | copy | 100.60 | 0.60 | 16 | 50.0 | -16.37 | -2.62 | -21.97 | 75 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 100.52 | 0.52 | 0 | — | 5.16 | 1.98 | -5.18 | 1 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.44 | 0.44 | 0 | — | 0.24 | 0.17 | -3.55 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.02 | 0.02 | 7 | 57.1 | -4.04 | -1.34 | -9.74 | 25 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.68 | -0.32 | 0 | — | -2.72 | -1.50 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.30 | -0.70 | 0 | — | 30.82 | 3.57 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.06 | -0.94 | 0 | — | -5.00 | -2.30 | -5.41 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 17 | Timing: Nasdaq FTD · TQQQ | daily | 98.42 | -1.58 | 0 | — | -9.33 | -1.70 | -15.27 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.71 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.91 | -2.09 | 82 | 25.6 | -22.87 | -6.44 | -25.58 | 172 |
| 20 | Donchian 55/20 · 1h | breakout | 97.73 | -2.27 | 31 | 12.9 | 7.21 | 1.01 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.37 | -2.63 | 5 | 0.0 | 0.43 | 0.25 | -12.76 | 12 |
| 22 | ADX DI cross · 1h | trend | 96.74 | -3.26 | 63 | 19.0 | -5.70 | -0.86 | -14.11 | 250 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.72 | -0.41 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 25 | Agent (rotation) | meta | 96.54 | -3.46 | 87 | 31.0 | -10.43 | -3.75 | -11.99 | 269 |
| 26 | Max aggression: 1-day momentum | meta | 96.09 | -3.91 | 12 | 33.3 | -10.61 | -0.23 | -37.31 | 42 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.92 | -4.08 | 0 | — | 7.31 | 1.25 | -8.36 | 1 |
| 28 | Stochastic reversion · 1h | reversion | 95.59 | -4.41 | 107 | 51.4 | -15.22 | -2.97 | -16.78 | 346 |
| 29 | EMA 20/50 cross · 1h | trend | 95.57 | -4.43 | 45 | 15.6 | 10.19 | 1.30 | -20.50 | 139 |
| 30 | MACD cross · 1h | trend | 95.55 | -4.46 | 128 | 24.2 | -12.60 | -2.00 | -19.81 | 462 |
| 31 | Agent | meta | 95.07 | -4.93 | 61 | 47.5 | -9.65 | -4.94 | -10.13 | 237 |
| 32 | Z-score reversion · 1h | reversion | 95.06 | -4.94 | 50 | 44.0 | 1.75 | 0.48 | -8.60 | 161 |
| 33 | Supertrend · 1h | trend | 94.12 | -5.88 | 60 | 13.3 | 0.10 | 0.21 | -19.12 | 219 |
| 34 | Parabolic SAR · 1h | trend | 94.10 | -5.90 | 90 | 22.2 | 1.63 | 0.40 | -22.37 | 289 |
| 35 | Squeeze breakout · 1h | breakout | 93.96 | -6.04 | 40 | 22.5 | 5.68 | 1.23 | -9.46 | 101 |
| 36 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 7.62 | 1.95 | -6.93 | 203 |
| 37 | Agent (aggressive) | meta | 92.86 | -7.14 | 31 | 35.5 | -9.12 | -3.98 | -9.12 | 120 |
| 38 | RSI momentum · 1h | momentum | 92.73 | -7.27 | 66 | 15.2 | 3.51 | 0.61 | -22.33 | 226 |
| 39 | Connors RSI(2) · 1h | reversion | 91.96 | -8.04 | 125 | 43.2 | -18.41 | -6.02 | -21.32 | 259 |
| 40 | MFI reversion · 1h | reversion | 91.72 | -8.28 | 160 | 31.9 | -8.05 | -1.25 | -17.02 | 131 |
| 41 | Ichimoku · 1h | trend | 91.41 | -8.59 | 48 | 16.7 | 1.73 | 0.41 | -22.34 | 126 |
| 42 | Agent (ML meta-label) | meta | 91.22 | -8.78 | 472 | 17.6 | -6.06 | -1.03 | -12.62 | 394 |
| 43 | Bollinger breakout · 1h | breakout | 91.05 | -8.95 | 75 | 28.0 | 7.62 | 1.12 | -14.21 | 278 |
| 44 | Volume breakout · 1h | breakout | 90.98 | -9.02 | 72 | 22.2 | 8.11 | 1.25 | -12.60 | 120 |
| 45 | RSI(14) reversion · 1h | reversion | 90.94 | -9.06 | 37 | 32.4 | -5.15 | -0.94 | -9.40 | 150 |
| 46 | Triple EMA stack · 1h | trend | 90.83 | -9.17 | 71 | 15.5 | -8.62 | -0.73 | -33.26 | 240 |
| 47 | Bollinger reversion · 1h | reversion | 89.18 | -10.82 | 96 | 36.5 | -25.02 | -5.99 | -25.41 | 324 |
| 48 | CCI reversion · 1h | reversion | 88.76 | -11.24 | 117 | 45.3 | -10.20 | -1.35 | -14.42 | 412 |
| 49 | Williams %R · 1h | reversion | 88.63 | -11.37 | 143 | 45.5 | -27.46 | -4.65 | -29.39 | 509 |
| 50 | OBV trend · 1h | momentum | 88.36 | -11.64 | 155 | 18.1 | -7.29 | -0.63 | -27.69 | 325 |
| 51 | Opening range 30m | breakout | 87.84 | -12.16 | 161 | 21.1 | -16.41 | -4.89 | -17.51 | 578 |
| 52 | MACD zero-line · 1h | trend | 87.82 | -12.18 | 68 | 17.6 | -22.15 | -4.33 | -23.02 | 228 |
| 53 | VWAP momentum · 1h | momentum | 87.58 | -12.42 | 323 | 23.2 | -32.60 | -4.82 | -40.38 | 1245 |
| 54 | Max aggression: 5-day momentum | meta | 87.43 | -12.57 | 8 | 37.5 | -10.68 | -0.68 | -34.64 | 28 |
| 55 | Donchian 20/10 · 1h | breakout | 87.29 | -12.71 | 64 | 17.2 | 1.40 | 0.37 | -19.51 | 217 |
| 56 | Keltner breakout · 1h | breakout | 87.11 | -12.89 | 46 | 19.6 | -7.72 | -0.82 | -26.76 | 214 |
| 57 | EMA 9/21 cross · 1h | trend | 86.79 | -13.21 | 110 | 12.7 | -9.34 | -1.12 | -24.20 | 327 |
| 58 | Three white soldiers | momentum | 86.76 | -13.24 | 161 | 18.6 | -47.80 | -22.55 | -48.12 | 588 |
| 59 | Heikin-Ashi · 1h | trend | 86.74 | -13.26 | 159 | 27.7 | -30.35 | -5.03 | -38.18 | 678 |
| 60 | Candlestick reversal · 1h | reversion | 86.14 | -13.86 | 136 | 29.4 | -30.47 | -5.98 | -30.82 | 502 |
| 61 | ROC + volume · 1h | momentum | 85.64 | -14.36 | 170 | 20.6 | -8.69 | -0.99 | -25.34 | 394 |
| 62 | Opening range 15m | breakout | 85.30 | -14.70 | 197 | 18.8 | -19.07 | -5.22 | -20.72 | 710 |
| 63 | ROC + volume | momentum | 72.16 | -27.84 | 446 | 22.9 | -72.58 | -16.27 | -74.52 | 1674 |
| 64 | Squeeze breakout | breakout | 68.53 | -31.47 | 368 | 15.8 | -62.40 | -18.06 | -62.46 | 1218 |
| 65 | Volume breakout | breakout | 68.22 | -31.79 | 289 | 14.5 | -61.48 | -17.38 | -61.48 | 890 |
| 66 | EMA 20/50 cross | trend | 67.15 | -32.85 | 369 | 20.1 | -76.12 | -14.86 | -76.25 | 1429 |
| 67 | RSI(14) reversion | reversion | 67.13 | -32.87 | 455 | 27.0 | -74.07 | -17.33 | -74.32 | 1496 |
| 68 | Donchian 55/20 | breakout | 65.01 | -34.99 | 376 | 17.0 | -68.60 | -14.38 | -69.86 | 1278 |
| 69 | VWAP reversion | reversion | 62.70 | -37.30 | 476 | 25.2 | -72.14 | -15.49 | -72.14 | 1393 |
| 70 | Supertrend | trend | 60.37 | -39.63 | 515 | 19.8 | -85.61 | -20.20 | -85.73 | 1902 |
| 71 | AI bee: Boozy | ai | 59.86 | -40.14 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.54 | -40.46 | 514 | 15.0 | -83.19 | -26.67 | -83.20 | 1856 |
| 73 | Ichimoku | trend | 55.50 | -44.50 | 455 | 9.5 | -82.17 | -22.83 | -82.17 | 1724 |
| 74 | AI bee: Bizzy | ai | 54.16 | -45.84 | 929 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.61 | -46.39 | 648 | 19.9 | -87.90 | -27.85 | -87.90 | 2113 |
| 76 | Z-score reversion | reversion | 52.67 | -47.33 | 606 | 22.9 | -86.21 | -22.28 | -86.29 | 2088 |
| 77 | ADX DI cross | trend | 52.14 | -47.86 | 639 | 10.5 | -89.19 | -34.12 | -89.19 | 2118 |
| 78 | Donchian 20/10 | breakout | 51.33 | -48.67 | 716 | 17.6 | -90.68 | -25.35 | -90.68 | 2642 |
| 79 | MACD zero-line | trend | 50.67 | -49.33 | 661 | 15.0 | -91.25 | -28.90 | -91.25 | 2347 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.49 | -29.32 | -98.51 | 5308 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.17 | -29.42 | -93.17 | 2601 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.24 | -24.57 | -90.24 | 2365 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.53 | -26.87 | -91.53 | 2348 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.28 | -31.96 | -97.29 | 3512 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -34.81 | -96.33 | 3566 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -25.45 | -94.39 | 2637 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.34 | -99.36 | 5655 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.31 | -31.08 | -96.31 | 3594 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.41 | -99.72 | 6128 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -37.31 | -97.35 | 3665 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.53 | -36.19 | -98.53 | 4666 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.31 | -32.13 | -93.32 | 2793 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.30 | -99.54 | 6121 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.05 | -32.79 | -96.05 | 3744 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -33.89 | -95.72 | 4049 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.70 | -99.89 | 8210 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T17:25 | Heikin-Ashi · 1h | buy | COIN | 4.35 | — | rebalance up |
| 2026-10-13T17:25 | Heikin-Ashi · 1h | sell | SQQQ | 4.35 | -0.01 | rebalance down |
| 2026-10-13T17:25 | MFI reversion | buy | MSFT | 6.34 | — | entry signal |
| 2026-10-13T17:25 | MFI reversion | buy | ETH-USD | 7.66 | — | entry signal |
| 2026-10-13T17:25 | MFI reversion | sell | TNA | 3.06 | -0.00 | rebalance down |
| 2026-10-13T17:25 | MFI reversion | sell | SQQQ | 3.14 | 0.01 | rebalance down |
| 2026-10-13T17:25 | MFI reversion | sell | MSTR | 3.05 | -0.00 | rebalance down |
| 2026-10-13T17:25 | MFI reversion | sell | META | 3.13 | 0.01 | rebalance down |
| 2026-10-13T17:25 | Donchian 55/20 | sell | COIN | 16.24 | -0.07 | stop-loss |
| 2026-10-13T17:25 | Donchian 20/10 | buy | TNA | 5.48 | — | rebalance up |
| 2026-10-13T17:25 | Donchian 20/10 | buy | TECL | 5.49 | — | rebalance up |
| 2026-10-13T17:25 | Donchian 20/10 | buy | NVDA | 5.51 | — | rebalance up |
| 2026-10-13T17:25 | Donchian 20/10 | buy | IWM | 5.49 | — | rebalance up |
| 2026-10-13T17:25 | Donchian 20/10 | sell | SOXL | 7.31 | -0.06 | exit signal |
| 2026-10-13T17:25 | Donchian 20/10 | sell | QQQ | 7.34 | -0.02 | stop-loss |
| 2026-10-13T17:25 | Donchian 20/10 | sell | AMD | 7.33 | 0.02 | exit signal |
| 2026-10-13T17:25 | ROC + volume | sell | AMD | 17.97 | -0.13 | exit signal |
| 2026-10-13T17:25 | Ichimoku | buy | DOGE-USD | 2.79 | — | rebalance up |
| 2026-10-13T17:25 | Ichimoku | sell | TECL | 2.79 | -0.01 | rebalance down |
| 2026-10-13T17:25 | ADX DI cross | sell | SOXL | 12.98 | -0.04 | exit signal |
| 2026-10-13T17:25 | ADX DI cross | sell | COIN | 13.02 | -0.04 | exit signal |
| 2026-10-13T17:23 | AI bee: Bizzy | sell | NVDA | 7.60 | -0.02 | Jev: sell (sell p=0.52) after 14 min |
| 2026-10-13T17:21 | AI bee: Bizzy | sell | META | 8.13 | -0.04 | Jev: sell (sell p=0.61) after 13 min |
| 2026-10-13T17:21 | MFI reversion · 1h | buy | AMD | 13.53 | — | entry |
| 2026-10-13T17:21 | MFI reversion · 1h | sell | TSLA | 4.59 | -0.01 | rebalance down |
| 2026-10-13T17:21 | MFI reversion · 1h | sell | QQQ | 4.67 | -0.01 | rebalance down |
| 2026-10-13T17:21 | MFI reversion | buy | MSTR | 10.72 | — | entry signal |
| 2026-10-13T17:21 | MFI reversion | sell | LABU | 10.57 | -0.17 | stop-loss |
| 2026-10-13T17:21 | Z-score reversion | buy | BTC-USD | 13.17 | — | entry signal |
| 2026-10-13T17:21 | Donchian 20/10 | buy | TNA | 2.66 | — | rebalance up |
| 2026-10-13T17:21 | Donchian 20/10 | buy | TECL | 2.69 | — | rebalance up |
| 2026-10-13T17:21 | Donchian 20/10 | buy | SOXL | 2.70 | — | rebalance up |
| 2026-10-13T17:21 | Donchian 20/10 | buy | QQQ | 2.66 | — | rebalance up |
| 2026-10-13T17:21 | Donchian 20/10 | buy | NVDA | 2.64 | — | rebalance up |
| 2026-10-13T17:21 | Donchian 20/10 | buy | IWM | 2.66 | — | rebalance up |
| 2026-10-13T17:21 | Donchian 20/10 | buy | AMD | 2.68 | — | rebalance up |
| 2026-10-13T17:21 | Donchian 20/10 | sell | UPRO | 4.67 | -0.02 | exit signal |
| 2026-10-13T17:21 | Donchian 20/10 | sell | TQQQ | 4.67 | -0.03 | exit signal |
| 2026-10-13T17:21 | Donchian 20/10 | sell | SPY | 4.69 | -0.01 | exit signal |
| 2026-10-13T17:21 | Ichimoku | buy | DOGE-USD | 8.31 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 17:25:05.000145+00:00 -> 2026-10-13 17:35:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
