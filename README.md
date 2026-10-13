# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T09:25:05.000125+00:00 · 21172 ticks

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

Today: 6765 decisions in 1353 calls, $0.0947 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T09:25 | 0 / 3 / 2 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T09:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T09:25 | 3 / 2 / 0 | COIN 77% |  |

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
| 5 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -9.06 | -2.70 | -13.79 | 120 |
| 6 | Hold SPY | benchmark | 101.23 | 1.24 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.03 | 1.03 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.46 | 0.46 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.44 | 0.43 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.94 | -0.06 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 15 | Hold BTC | benchmark | 99.76 | -0.24 | 0 | — | 29.93 | 3.47 | -8.68 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.18 | -0.82 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.10 | -1.90 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 97.95 | -2.05 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.82 | -2.18 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.69 | -2.31 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.22 | -2.78 | 105 | 52.4 | -10.69 | -1.98 | -13.91 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 96.84 | -3.16 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 25 | Three white soldiers · 1h | momentum | 96.83 | -3.17 | 9 | 0.0 | -3.67 | -2.81 | -4.81 | 29 |
| 26 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 27 | Z-score reversion · 1h | reversion | 96.50 | -3.50 | 47 | 44.7 | 3.41 | 0.80 | -8.60 | 165 |
| 28 | ADX DI cross · 1h | trend | 96.23 | -3.77 | 63 | 19.0 | -6.61 | -1.07 | -13.79 | 256 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -8.79 | -3.28 | -9.95 | 315 |
| 30 | MACD cross · 1h | trend | 95.56 | -4.44 | 125 | 24.0 | -10.91 | -1.70 | -17.79 | 462 |
| 31 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.86 | -3.80 | -8.72 | 230 |
| 32 | Parabolic SAR · 1h | trend | 95.21 | -4.79 | 86 | 22.1 | 2.15 | 0.46 | -21.52 | 288 |
| 33 | EMA 20/50 cross · 1h | trend | 95.16 | -4.84 | 45 | 15.6 | 5.03 | 0.76 | -23.71 | 135 |
| 34 | Supertrend · 1h | trend | 94.38 | -5.62 | 58 | 13.8 | 1.12 | 0.34 | -18.92 | 217 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.42 | -6.58 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.27 | -6.73 | 151 | 32.5 | -7.32 | -1.09 | -16.91 | 131 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.27 | -2.76 | -6.49 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.44 | -7.56 | 66 | 15.2 | -0.70 | 0.12 | -23.02 | 230 |
| 40 | Connors RSI(2) · 1h | reversion | 92.35 | -7.65 | 115 | 43.5 | -18.94 | -6.26 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.33 | -7.67 | 439 | 17.8 | 1.39 | 0.39 | -13.28 | 390 |
| 42 | Volume breakout · 1h | breakout | 91.59 | -8.41 | 70 | 20.0 | 9.16 | 1.39 | -12.60 | 116 |
| 43 | RSI(14) reversion · 1h | reversion | 91.46 | -8.54 | 36 | 30.6 | 0.80 | 0.29 | -9.40 | 134 |
| 44 | Ichimoku · 1h | trend | 90.85 | -9.15 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger reversion · 1h | reversion | 90.74 | -9.26 | 93 | 37.6 | -23.67 | -5.71 | -24.41 | 319 |
| 46 | Bollinger breakout · 1h | breakout | 90.74 | -9.26 | 74 | 28.4 | 8.33 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.55 | -9.46 | 71 | 15.5 | -6.78 | -0.57 | -27.17 | 235 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 88.99 | -11.01 | 141 | 46.1 | -25.14 | -4.08 | -28.82 | 507 |
| 50 | CCI reversion · 1h | reversion | 88.82 | -11.18 | 114 | 45.6 | -9.94 | -1.31 | -14.35 | 410 |
| 51 | OBV trend · 1h | momentum | 88.55 | -11.45 | 150 | 18.7 | -12.43 | -1.17 | -34.15 | 317 |
| 52 | VWAP momentum · 1h | momentum | 88.08 | -11.92 | 311 | 23.2 | -32.69 | -4.84 | -40.18 | 1254 |
| 53 | Max aggression: 5-day momentum | meta | 87.93 | -12.06 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.89 | -12.11 | 130 | 30.8 | -28.66 | -5.45 | -28.75 | 495 |
| 55 | Donchian 20/10 · 1h | breakout | 87.55 | -12.45 | 63 | 17.5 | -0.67 | 0.12 | -19.51 | 215 |
| 56 | MACD zero-line · 1h | trend | 87.34 | -12.66 | 67 | 17.9 | -20.18 | -3.72 | -21.59 | 229 |
| 57 | Heikin-Ashi · 1h | trend | 87.21 | -12.79 | 156 | 27.6 | -30.25 | -5.00 | -37.90 | 680 |
| 58 | EMA 9/21 cross · 1h | trend | 86.87 | -13.13 | 108 | 13.0 | -8.15 | -0.85 | -23.11 | 333 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.29 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.49 | -13.51 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.19 | -13.81 | 156 | 17.3 | -48.13 | -23.09 | -48.13 | 586 |
| 62 | ROC + volume · 1h | momentum | 85.37 | -14.63 | 164 | 20.1 | -8.89 | -1.02 | -25.13 | 396 |
| 63 | ROC + volume | momentum | 73.36 | -26.64 | 426 | 23.0 | -72.38 | -15.90 | -74.72 | 1659 |
| 64 | Squeeze breakout | breakout | 69.22 | -30.78 | 356 | 15.4 | -62.35 | -18.07 | -62.35 | 1223 |
| 65 | Volume breakout | breakout | 68.85 | -31.15 | 285 | 14.7 | -61.63 | -17.54 | -61.63 | 892 |
| 66 | RSI(14) reversion | reversion | 68.37 | -31.63 | 431 | 26.9 | -73.89 | -17.29 | -73.93 | 1486 |
| 67 | EMA 20/50 cross | trend | 67.62 | -32.38 | 359 | 20.3 | -75.95 | -14.75 | -76.17 | 1427 |
| 68 | Donchian 55/20 | breakout | 66.43 | -33.57 | 365 | 17.5 | -68.07 | -14.19 | -69.19 | 1290 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -73.10 | -15.51 | -73.13 | 1416 |
| 70 | Keltner breakout | breakout | 60.63 | -39.37 | 492 | 15.4 | -82.97 | -26.13 | -83.16 | 1834 |
| 71 | Supertrend | trend | 60.55 | -39.45 | 510 | 20.0 | -85.67 | -20.21 | -85.91 | 1888 |
| 72 | AI bee: Boozy | ai | 59.91 | -40.09 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.54 | -43.46 | 440 | 9.8 | -82.11 | -22.69 | -82.11 | 1728 |
| 74 | MFI reversion | reversion | 54.94 | -45.06 | 629 | 20.0 | -87.91 | -27.24 | -88.04 | 2114 |
| 75 | AI bee: Bizzy | ai | 54.61 | -45.39 | 909 | 8.3 | — | — | — | — |
| 76 | Z-score reversion | reversion | 54.39 | -45.61 | 577 | 22.2 | -86.22 | -22.44 | -86.34 | 2079 |
| 77 | ADX DI cross | trend | 53.59 | -46.41 | 610 | 10.7 | -89.01 | -33.18 | -89.08 | 2108 |
| 78 | Donchian 20/10 | breakout | 52.22 | -47.78 | 693 | 18.0 | -90.65 | -25.09 | -90.76 | 2640 |
| 79 | MACD zero-line | trend | 51.34 | -48.66 | 640 | 15.2 | -91.23 | -28.63 | -91.34 | 2339 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.51 | -29.11 | -98.55 | 5296 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.02 | -28.85 | -93.06 | 2588 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.20 | -24.35 | -90.34 | 2354 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.33 | -26.46 | -91.33 | 2329 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.26 | -31.48 | -97.30 | 3508 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -34.47 | -96.29 | 3573 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -25.41 | -94.33 | 2634 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.88 | -99.37 | 5630 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -31.34 | -96.38 | 3607 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.71 | -40.12 | -99.72 | 6130 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.25 | -36.65 | -97.25 | 3645 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.93 | -98.52 | 4663 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.27 | -31.93 | -93.27 | 2789 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.08 | -99.54 | 6111 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.06 | -32.74 | -96.06 | 3733 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.76 | -33.94 | -95.77 | 4049 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -45.66 | -99.88 | 8198 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T09:25 | MFI reversion | sell | DOGE-USD | 13.67 | -0.15 | stop-loss |
| 2026-10-13T09:25 | Z-score reversion | sell | DOGE-USD | 13.53 | -0.14 | stop-loss |
| 2026-10-13T09:25 | RSI(14) reversion | sell | DOGE-USD | 17.00 | -0.18 | stop-loss |
| 2026-10-13T09:20 | EMA 20/50 cross | buy | XRP-USD | 3.42 | — | rebalance up |
| 2026-10-13T09:20 | EMA 20/50 cross | buy | BTC-USD | 3.39 | — | rebalance up |
| 2026-10-13T09:20 | EMA 20/50 cross | sell | SOL-USD | 10.15 | 0.02 | exit signal |
| 2026-10-13T09:20 | EMA 20/50 cross | sell | DOGE-USD | 13.50 | 0.04 | exit signal |
| 2026-10-13T09:10 | MFI reversion | buy | XRP-USD | 13.81 | — | entry signal |
| 2026-10-13T09:10 | MFI reversion | buy | SOL-USD | 13.81 | — | entry signal |
| 2026-10-13T09:10 | MFI reversion | buy | DOGE-USD | 13.81 | — | entry signal |
| 2026-10-13T09:10 | Z-score reversion | buy | XRP-USD | 13.67 | — | entry signal |
| 2026-10-13T09:10 | Z-score reversion | buy | DOGE-USD | 13.67 | — | entry signal |
| 2026-10-13T09:10 | Z-score reversion | buy | BTC-USD | 13.67 | — | entry signal |
| 2026-10-13T09:10 | RSI(14) reversion | buy | SOL-USD | 17.18 | — | entry signal |
| 2026-10-13T09:10 | RSI(14) reversion | buy | ETH-USD | 17.18 | — | entry signal |
| 2026-10-13T09:10 | RSI(14) reversion | buy | DOGE-USD | 17.18 | — | entry signal |
| 2026-10-13T09:05 | Donchian 55/20 | sell | XRP-USD | 13.24 | -0.06 | exit signal |
| 2026-10-13T09:05 | Supertrend | sell | XRP-USD | 12.11 | 0.04 | exit signal |
| 2026-10-13T09:01 | Three white soldiers · 1h | sell | DOGE-USD | 24.11 | -0.18 | exit signal |
| 2026-10-13T09:01 | Heikin-Ashi · 1h | buy | XRP-USD | 21.89 | — | entry |
| 2026-10-13T09:01 | Heikin-Ashi · 1h | sell | SOL-USD | 17.38 | -0.09 | exit signal |
| 2026-10-13T09:01 | Heikin-Ashi · 1h | sell | ETH-USD | 17.49 | -0.05 | exit signal |
| 2026-10-13T09:01 | Heikin-Ashi · 1h | sell | DOGE-USD | 17.41 | -0.13 | exit signal |
| 2026-10-13T09:01 | ADX DI cross · 1h | sell | ETH-USD | 7.90 | -0.09 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 09:25:05.000125+00:00 -> 2026-10-13 09:35:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
