# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T07:25:05.000121+00:00 · 21076 ticks

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

Today: 5325 decisions in 1065 calls, $0.0746 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T07:25 | 0 / 2 / 3 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T07:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T07:25 | 2 / 2 / 1 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.77 | 2.77 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.06 | 2.06 | 16 | 50.0 | -15.08 | -2.39 | -21.97 | 73 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | Hold SPY | benchmark | 101.28 | 1.28 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -8.80 | -2.61 | -13.79 | 117 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.07 | 1.07 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.51 | 0.51 | 0 | — | -5.03 | -0.82 | -15.27 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.48 | 0.48 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Hold BTC | benchmark | 100.04 | 0.04 | 0 | — | 30.75 | 3.55 | -8.68 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Daily: SMA 20/50 cross · AAPL | daily | 99.98 | -0.02 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.22 | -0.78 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.14 | -1.86 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.00 | -2.00 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.87 | -2.13 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.74 | -2.26 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.25 | -2.75 | 105 | 52.4 | -10.69 | -1.98 | -13.91 | 343 |
| 24 | Three white soldiers · 1h | momentum | 97.19 | -2.81 | 8 | 0.0 | -3.33 | -2.55 | -4.64 | 29 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.89 | -3.11 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 26 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 27 | Z-score reversion · 1h | reversion | 96.64 | -3.37 | 47 | 44.7 | 3.61 | 0.84 | -8.60 | 165 |
| 28 | ADX DI cross · 1h | trend | 96.39 | -3.61 | 62 | 19.4 | -5.76 | -0.91 | -13.79 | 253 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -8.60 | -3.20 | -9.97 | 315 |
| 30 | MACD cross · 1h | trend | 95.76 | -4.24 | 125 | 24.0 | -10.78 | -1.67 | -17.79 | 463 |
| 31 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.82 | -3.78 | -8.72 | 231 |
| 32 | Parabolic SAR · 1h | trend | 95.25 | -4.75 | 86 | 22.1 | 2.01 | 0.45 | -21.52 | 289 |
| 33 | EMA 20/50 cross · 1h | trend | 95.21 | -4.79 | 45 | 15.6 | 4.90 | 0.75 | -23.71 | 136 |
| 34 | Supertrend · 1h | trend | 94.43 | -5.57 | 58 | 13.8 | 0.72 | 0.29 | -18.92 | 218 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.33 | -6.67 | 151 | 32.5 | -7.02 | -1.04 | -16.91 | 130 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.23 | -2.74 | -6.45 | 113 |
| 39 | RSI momentum · 1h | momentum | 92.49 | -7.51 | 66 | 15.2 | -0.62 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.39 | -7.61 | 115 | 43.5 | -18.94 | -6.26 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.38 | -7.62 | 439 | 17.8 | 0.61 | 0.25 | -13.09 | 389 |
| 42 | Volume breakout · 1h | breakout | 91.62 | -8.38 | 70 | 20.0 | 9.08 | 1.38 | -12.60 | 117 |
| 43 | RSI(14) reversion · 1h | reversion | 91.61 | -8.39 | 36 | 30.6 | 1.08 | 0.35 | -9.40 | 134 |
| 44 | Ichimoku · 1h | trend | 90.89 | -9.11 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger breakout · 1h | breakout | 90.77 | -9.23 | 74 | 28.4 | 8.34 | 1.21 | -14.21 | 277 |
| 46 | Bollinger reversion · 1h | reversion | 90.77 | -9.23 | 93 | 37.6 | -23.66 | -5.71 | -24.41 | 319 |
| 47 | Triple EMA stack · 1h | trend | 90.59 | -9.41 | 71 | 15.5 | -7.02 | -0.60 | -27.17 | 236 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 89.01 | -10.99 | 141 | 46.1 | -25.27 | -4.10 | -28.82 | 509 |
| 50 | CCI reversion · 1h | reversion | 88.91 | -11.09 | 114 | 45.6 | -9.72 | -1.27 | -14.35 | 410 |
| 51 | OBV trend · 1h | momentum | 88.59 | -11.41 | 150 | 18.7 | -12.47 | -1.18 | -34.14 | 317 |
| 52 | VWAP momentum · 1h | momentum | 88.13 | -11.88 | 311 | 23.2 | -32.50 | -4.80 | -40.20 | 1255 |
| 53 | Candlestick reversal · 1h | reversion | 88.01 | -11.99 | 130 | 30.8 | -29.01 | -5.51 | -29.16 | 496 |
| 54 | Max aggression: 5-day momentum | meta | 87.98 | -12.02 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 55 | Heikin-Ashi · 1h | trend | 87.84 | -12.16 | 153 | 28.1 | -29.81 | -4.90 | -37.84 | 680 |
| 56 | Donchian 20/10 · 1h | breakout | 87.60 | -12.40 | 63 | 17.5 | -0.64 | 0.13 | -19.51 | 215 |
| 57 | MACD zero-line · 1h | trend | 87.43 | -12.57 | 67 | 17.9 | -20.34 | -3.75 | -21.54 | 230 |
| 58 | EMA 9/21 cross · 1h | trend | 86.97 | -13.03 | 108 | 13.0 | -8.49 | -0.89 | -23.06 | 334 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.53 | -13.47 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.36 | -13.64 | 155 | 17.4 | -48.06 | -22.97 | -48.10 | 586 |
| 62 | ROC + volume · 1h | momentum | 85.41 | -14.59 | 164 | 20.1 | -9.22 | -1.07 | -25.13 | 397 |
| 63 | ROC + volume | momentum | 73.36 | -26.64 | 426 | 23.0 | -72.50 | -15.99 | -74.73 | 1663 |
| 64 | Squeeze breakout | breakout | 69.36 | -30.64 | 355 | 15.5 | -62.14 | -17.96 | -62.14 | 1220 |
| 65 | Volume breakout | breakout | 69.14 | -30.86 | 283 | 14.8 | -61.57 | -17.45 | -61.57 | 893 |
| 66 | RSI(14) reversion | reversion | 68.73 | -31.27 | 430 | 27.0 | -73.89 | -17.25 | -74.07 | 1487 |
| 67 | EMA 20/50 cross | trend | 68.09 | -31.91 | 357 | 19.9 | -75.92 | -14.70 | -76.26 | 1430 |
| 68 | Donchian 55/20 | breakout | 66.83 | -33.17 | 360 | 17.5 | -68.09 | -14.17 | -69.18 | 1293 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -72.96 | -15.49 | -72.99 | 1415 |
| 70 | Supertrend | trend | 61.17 | -38.83 | 504 | 19.4 | -85.68 | -20.07 | -86.02 | 1892 |
| 71 | Keltner breakout | breakout | 60.75 | -39.25 | 491 | 15.5 | -82.93 | -26.01 | -83.15 | 1836 |
| 72 | AI bee: Boozy | ai | 59.91 | -40.09 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.99 | -43.01 | 437 | 9.8 | -82.05 | -22.59 | -82.05 | 1727 |
| 74 | MFI reversion | reversion | 55.26 | -44.74 | 628 | 20.1 | -87.81 | -27.01 | -88.01 | 2111 |
| 75 | AI bee: Bizzy | ai | 54.70 | -45.30 | 907 | 8.3 | — | — | — | — |
| 76 | Z-score reversion | reversion | 54.68 | -45.32 | 576 | 22.2 | -86.23 | -22.36 | -86.42 | 2078 |
| 77 | ADX DI cross | trend | 53.95 | -46.05 | 604 | 10.4 | -88.90 | -32.62 | -89.06 | 2105 |
| 78 | Donchian 20/10 | breakout | 52.78 | -47.22 | 687 | 17.9 | -90.57 | -24.75 | -90.78 | 2639 |
| 79 | MACD zero-line | trend | 51.34 | -48.66 | 640 | 15.2 | -91.24 | -28.64 | -91.34 | 2339 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -28.75 | -98.53 | 5293 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.06 | -28.91 | -93.14 | 2592 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.20 | -24.27 | -90.40 | 2356 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.25 | -26.22 | -91.25 | 2327 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.25 | -31.24 | -97.31 | 3508 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -34.49 | -96.33 | 3577 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -25.36 | -94.33 | 2635 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.83 | -99.37 | 5640 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.31 | -30.91 | -96.31 | 3598 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.90 | -99.72 | 6130 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.24 | -36.60 | -97.24 | 3646 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.82 | -98.53 | 4661 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.26 | -31.75 | -93.28 | 2790 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.84 | -99.54 | 6106 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.04 | -32.55 | -96.05 | 3729 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.75 | -33.85 | -95.78 | 4045 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -45.50 | -99.88 | 8200 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T07:25 | Donchian 20/10 | sell | ETH-USD | 10.57 | 0.21 | exit signal |
| 2026-10-13T07:25 | ADX DI cross | buy | DOGE-USD | 2.71 | — | rebalance up |
| 2026-10-13T07:25 | ADX DI cross | sell | SOL-USD | 8.01 | -0.06 | exit signal |
| 2026-10-13T07:20 | ADX DI cross | buy | SOL-USD | 8.07 | — | entry signal |
| 2026-10-13T07:20 | ADX DI cross | buy | DOGE-USD | 10.82 | — | entry signal |
| 2026-10-13T07:20 | ADX DI cross | sell | BTC-USD | 2.74 | 0.02 | rebalance down |
| 2026-10-13T07:15 | ADX DI cross | buy | XRP-USD | 13.54 | — | entry signal |
| 2026-10-13T07:12 | Trend pullback | sell | ETH-USD | 12.56 | -0.08 | Kill switch: down 50% from peak |
| 2026-10-13T07:12 | Trend pullback | sell | BTC-USD | 12.56 | -0.08 | Kill switch: down 50% from peak |
| 2026-10-13T07:10 | Trend pullback | buy | ETH-USD | 12.64 | — | entry signal |
| 2026-10-13T07:10 | Trend pullback | buy | BTC-USD | 12.64 | — | entry signal |
| 2026-10-13T07:10 | ADX DI cross | sell | SOL-USD | 13.52 | 0.09 | exit signal |
| 2026-10-13T07:10 | ADX DI cross | sell | DOGE-USD | 10.84 | 0.18 | exit signal |
| 2026-10-13T07:05 | Three white soldiers | sell | ETH-USD | 21.49 | -0.13 | exit signal |
| 2026-10-13T07:05 | Squeeze breakout | sell | XRP-USD | 17.22 | -0.16 | stop-loss |
| 2026-10-13T07:05 | Keltner breakout | sell | XRP-USD | 12.16 | 0.04 | stop-loss |
| 2026-10-13T07:05 | Keltner breakout | sell | SOL-USD | 12.14 | 0.03 | stop-loss |
| 2026-10-13T07:05 | Keltner breakout | sell | ETH-USD | 12.20 | 0.16 | stop-loss |
| 2026-10-13T07:05 | Keltner breakout | sell | DOGE-USD | 12.08 | -0.06 | exit signal |
| 2026-10-13T07:05 | Keltner breakout | sell | BTC-USD | 12.16 | 0.09 | exit signal |
| 2026-10-13T07:05 | Donchian 20/10 | buy | BTC-USD | 2.70 | — | rebalance up |
| 2026-10-13T07:05 | Donchian 20/10 | sell | XRP-USD | 10.48 | 0.12 | exit signal |
| 2026-10-13T07:05 | Donchian 20/10 | sell | SOL-USD | 7.97 | 0.14 | exit signal |
| 2026-10-13T07:05 | ADX DI cross | buy | SOL-USD | 5.36 | — | rebalance up |
| 2026-10-13T07:05 | ADX DI cross | buy | BTC-USD | 2.76 | — | rebalance up |
| 2026-10-13T07:05 | ADX DI cross | sell | XRP-USD | 10.75 | 0.12 | exit signal |
| 2026-10-13T07:05 | Supertrend | buy | XRP-USD | 3.13 | — | rebalance up |
| 2026-10-13T07:05 | Supertrend | buy | BTC-USD | 3.13 | — | rebalance up |
| 2026-10-13T07:05 | Supertrend | sell | SOL-USD | 12.25 | 0.27 | exit signal |
| 2026-10-13T07:00 | MACD zero-line · 1h | buy | BTC-USD | 21.39 | — | entry signal |
| 2026-10-13T06:58 | AI bee: Bizzy | sell | XRP-USD | 7.62 | -0.05 | Jev: sell (sell p=0.75) after 10 min |
| 2026-10-13T06:53 | AI bee: Boozy | sell | ETH-USD | 13.78 | -0.08 | Jev: add (buy p=0.53) |
| 2026-10-13T06:48 | AI bee: Bizzy | buy | XRP-USD | 7.67 | — | Jev: buy (buy p=0.56) |
| 2026-10-13T06:42 | AI bee: Bizzy | sell | DOGE-USD | 8.18 | -0.05 | Jev: sell (sell p=0.74) after 11 min |
| 2026-10-13T06:38 | AI bee: Boozy | buy | ETH-USD | 13.86 | — | Jev: buy (buy p=0.78) |
| 2026-10-13T06:35 | AI bee: Bizzy | sell | SOL-USD | 7.98 | -0.05 | Jev: sell (sell p=0.70) after 11 min |
| 2026-10-13T06:31 | AI bee: Bizzy | buy | DOGE-USD | 8.23 | — | Jev: buy (buy p=0.60) |
| 2026-10-13T06:25 | ROC + volume | sell | ETH-USD | 14.79 | 0.37 | exit signal |
| 2026-10-13T06:24 | AI bee: Bizzy | buy | SOL-USD | 8.02 | — | Jev: buy (buy p=0.59) |
| 2026-10-13T06:15 | ROC + volume | sell | BTC-USD | 18.28 | 0.21 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 07:25:05.000121+00:00 -> 2026-10-13 07:35:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
