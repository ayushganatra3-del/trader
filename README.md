# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T19:57:05.000169+00:00 · 17081 ticks

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
| Copy: Insider buying | 2026-10-09 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-08)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 21.98 · VIX 15.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.3, AMD 7.1, TECL 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 35583 decisions in 2817 calls, $0.4386 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T19:57 | 4 / 21 / 5 | COIN 14%, NANC 16% |  |
| Breezy | 2026-10-09T19:57 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-09T19:57 | 0 / 29 / 1 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.78 | +2.31% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.29 | 3.29 | 37 | 43.2 | -7.19 | -2.16 | -13.79 | 121 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.48 | 2.48 | 0 | — | -4.12 | -0.66 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.13 | 2.13 | 0 | — | -3.63 | -1.49 | -7.31 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 6 | Copy: Insider buying | copy | 101.52 | 1.52 | 14 | 57.1 | -12.53 | -2.03 | -21.08 | 72 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.44 | 1.44 | 0 | — | 1.98 | 0.95 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.23 | 1.23 | 0 | — | 0.47 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.07 | 1.07 | 0 | — | -0.88 | -0.46 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.31 | 2.48 | -1.52 | 90 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.54 | -0.46 | 0 | — | -3.97 | -1.85 | -5.36 | 1 |
| 16 | Max aggression: 1-day momentum | meta | 99.48 | -0.52 | 10 | 30.0 | -15.73 | -0.56 | -37.31 | 43 |
| 17 | Donchian 55/20 · 1h | breakout | 99.38 | -0.62 | 27 | 14.8 | 13.41 | 1.67 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.10 | -0.91 | 88 | 55.7 | -10.91 | -2.12 | -14.99 | 342 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Copy: Cathie Wood (ARKK) | copy | 98.82 | -1.18 | 0 | — | 11.82 | 1.92 | -8.33 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.67 | -1.33 | 0 | — | 1.73 | 0.74 | -5.18 | 1 |
| 22 | Hold BTC | benchmark | 98.36 | -1.64 | 0 | — | 26.15 | 3.16 | -8.68 | 1 |
| 23 | Daily: Bullish score | daily | 97.81 | -2.19 | 4 | 0.0 | 0.78 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.61 | -2.39 | 6 | 0.0 | -2.99 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.11 | -2.89 | 38 | 42.1 | 0.21 | 0.17 | -8.60 | 165 |
| 26 | Trend pullback · 1h | trend | 97.01 | -2.99 | 78 | 23.1 | -22.71 | -6.38 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.82 | -3.18 | 38 | 13.2 | 4.51 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.68 | -3.33 | 80 | 30.0 | 2.63 | 0.73 | -8.65 | 256 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.33 | -3.67 | 58 | 20.7 | -2.50 | -0.23 | -13.84 | 259 |
| 31 | Parabolic SAR · 1h | trend | 96.27 | -3.73 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.74 | -4.26 | 107 | 22.4 | -16.83 | -2.74 | -18.37 | 473 |
| 34 | Supertrend · 1h | trend | 94.71 | -5.29 | 52 | 13.5 | -0.50 | 0.13 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.22 | -5.78 | 35 | 25.7 | 24.20 | 3.29 | -8.62 | 105 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.55 | -2.07 | -6.59 | 109 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.61 | -6.39 | 119 | 34.5 | -12.66 | -2.10 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.30 | -6.70 | 26 | 26.9 | -2.43 | -0.42 | -9.03 | 151 |
| 40 | Ichimoku · 1h | trend | 93.06 | -6.94 | 41 | 19.5 | -0.31 | 0.16 | -19.98 | 120 |
| 41 | Connors RSI(2) · 1h | reversion | 92.99 | -7.01 | 113 | 43.4 | -18.29 | -6.07 | -20.97 | 253 |
| 42 | Agent (ML meta-label) | meta | 92.94 | -7.06 | 392 | 18.4 | -4.06 | -0.63 | -12.83 | 436 |
| 43 | Bollinger reversion · 1h | reversion | 92.72 | -7.28 | 73 | 37.0 | -20.94 | -5.01 | -23.75 | 318 |
| 44 | RSI momentum · 1h | momentum | 92.68 | -7.32 | 64 | 15.6 | 3.79 | 0.66 | -17.07 | 221 |
| 45 | Volume breakout · 1h | breakout | 92.64 | -7.36 | 56 | 19.6 | 8.03 | 1.25 | -12.60 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 92.00 | -8.00 | 67 | 29.9 | 6.39 | 0.98 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.45 | -8.55 | 116 | 48.3 | -25.31 | -4.38 | -27.32 | 512 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.79 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.71 | -9.29 | 69 | 15.9 | -8.61 | -0.85 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.00 | -10.00 | 114 | 30.7 | -28.81 | -5.68 | -30.44 | 522 |
| 51 | VWAP momentum · 1h | momentum | 89.71 | -10.29 | 277 | 22.0 | -35.48 | -5.38 | -39.46 | 1277 |
| 52 | CCI reversion · 1h | reversion | 89.62 | -10.38 | 96 | 43.8 | -9.37 | -1.23 | -14.35 | 418 |
| 53 | MACD zero-line · 1h | trend | 89.44 | -10.56 | 59 | 20.3 | -6.56 | -0.70 | -19.40 | 239 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.37 | -5.21 | -19.78 | 700 |
| 55 | Three white soldiers | momentum | 89.12 | -10.88 | 128 | 19.5 | -47.86 | -23.27 | -48.05 | 586 |
| 56 | Donchian 20/10 · 1h | breakout | 88.79 | -11.21 | 58 | 19.0 | -0.67 | 0.13 | -17.72 | 221 |
| 57 | OBV trend · 1h | momentum | 88.70 | -11.30 | 149 | 18.8 | -12.35 | -1.40 | -28.83 | 320 |
| 58 | Heikin-Ashi · 1h | trend | 88.58 | -11.42 | 138 | 25.4 | -31.75 | -5.37 | -36.59 | 703 |
| 59 | Max aggression: 5-day momentum | meta | 87.96 | -12.04 | 7 | 28.6 | -14.28 | -1.04 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.77 | -12.23 | 101 | 13.9 | -10.13 | -1.17 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.12 | -12.88 | 43 | 18.6 | -11.26 | -1.29 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.47 | -13.53 | 132 | 21.2 | -9.84 | -1.18 | -23.20 | 414 |
| 63 | RSI(14) reversion | reversion | 75.48 | -24.52 | 350 | 29.1 | -73.51 | -18.73 | -73.66 | 1509 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.32 | -17.05 | -74.19 | 1664 |
| 65 | Squeeze breakout | breakout | 73.91 | -26.09 | 299 | 15.7 | -61.63 | -18.22 | -61.72 | 1217 |
| 66 | Donchian 55/20 | breakout | 72.55 | -27.45 | 310 | 18.4 | -68.04 | -14.52 | -68.48 | 1297 |
| 67 | EMA 20/50 cross | trend | 72.03 | -27.97 | 307 | 20.5 | -77.55 | -15.51 | -77.72 | 1463 |
| 68 | Volume breakout | breakout | 71.54 | -28.46 | 248 | 13.7 | -63.38 | -18.26 | -63.65 | 902 |
| 69 | VWAP reversion | reversion | 68.26 | -31.74 | 392 | 26.3 | -72.14 | -16.44 | -72.52 | 1455 |
| 70 | Supertrend | trend | 66.04 | -33.96 | 434 | 20.5 | -86.71 | -21.49 | -86.71 | 1930 |
| 71 | Keltner breakout | breakout | 65.43 | -34.57 | 420 | 15.0 | -84.15 | -27.76 | -84.45 | 1858 |
| 72 | Ichimoku | trend | 62.41 | -37.59 | 383 | 10.2 | -81.75 | -23.47 | -81.87 | 1749 |
| 73 | AI bee: Bizzy | ai | 62.10 | -37.90 | 754 | 9.7 | — | — | — | — |
| 74 | Z-score reversion | reversion | 61.46 | -38.54 | 479 | 23.8 | -85.89 | -23.71 | -85.89 | 2102 |
| 75 | MFI reversion | reversion | 61.33 | -38.67 | 486 | 22.0 | -88.06 | -29.02 | -88.06 | 2110 |
| 76 | AI bee: Boozy | ai | 61.29 | -38.71 | 246 | 5.3 | — | — | — | — |
| 77 | Donchian 20/10 | breakout | 59.24 | -40.76 | 591 | 19.0 | -90.82 | -26.16 | -90.92 | 2662 |
| 78 | Trend pullback | trend | 59.09 | -40.91 | 537 | 16.0 | -90.44 | -27.24 | -90.54 | 2300 |
| 79 | ADX DI cross | trend | 58.74 | -41.26 | 517 | 10.4 | -89.83 | -35.22 | -89.84 | 2144 |
| 80 | RSI momentum | momentum | 58.21 | -41.79 | 558 | 17.9 | -90.27 | -25.67 | -90.35 | 2375 |
| 81 | MACD zero-line | trend | 57.70 | -42.30 | 541 | 15.7 | -91.53 | -29.90 | -91.53 | 2360 |
| 82 | Triple EMA stack | trend | 57.02 | -42.98 | 578 | 16.3 | -93.13 | -30.48 | -93.14 | 2610 |
| 83 | Bollinger breakout | breakout | 54.68 | -45.32 | 617 | 15.1 | -93.54 | -33.25 | -93.55 | 2817 |
| 84 | Consensus | meta | 52.91 | -47.09 | 586 | 10.4 | -94.25 | -25.89 | -94.26 | 2683 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -30.87 | -98.73 | 5400 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.27 | -97.36 | 3540 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -36.60 | -96.40 | 3589 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -37.63 | -99.37 | 5710 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.28 | -32.22 | -96.28 | 3604 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.82 | -99.73 | 6204 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.32 | -38.69 | -97.33 | 3674 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.59 | -98.50 | 4724 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -41.20 | -99.53 | 6164 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.96 | -34.44 | -95.96 | 3758 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -35.30 | -95.70 | 4098 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.14 | -99.90 | 8330 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T19:56 | AI bee: Bizzy | sell | AMZN | 9.55 | -0.01 | Jev: sell (sell p=0.60) after 18 min |
| 2026-10-09T19:55 | Agent (rotation) | sell | SQQQ | 32.26 | 0.03 | selected signal exited |
| 2026-10-09T19:55 | Day trade: Stocks in Play ORB | sell | UPRO | 24.76 | -0.08 | target is flat |
| 2026-10-09T19:55 | Day trade: Stocks in Play ORB | sell | PLTR | 25.28 | 0.53 | target is flat |
| 2026-10-09T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 99.05 | -0.21 | target is flat |
| 2026-10-09T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 99.58 | 0.11 | target is flat |
| 2026-10-09T19:55 | Consensus | sell | PLTR | 13.30 | 0.23 | target is flat |
| 2026-10-09T19:55 | Consensus | sell | MSFT | 13.20 | -0.02 | target is flat |
| 2026-10-09T19:55 | Consensus | sell | AMZN | 13.22 | 0.04 | target is flat |
| 2026-10-09T19:55 | MFI reversion · 1h | buy | TSLA | 18.73 | — | entry |
| 2026-10-09T19:55 | MFI reversion · 1h | sell | COIN | 19.02 | 0.57 | target is flat |
| 2026-10-09T19:55 | Candlestick reversal · 1h | buy | QQQ | 10.00 | — | entry |
| 2026-10-09T19:55 | VWAP momentum · 1h | buy | TSLA | 6.41 | — | entry |
| 2026-10-09T19:55 | MFI reversion | sell | META | 12.29 | -0.02 | end-of-day flatten |
| 2026-10-09T19:55 | MFI reversion | sell | LABU | 12.27 | -0.08 | end-of-day flatten |
| 2026-10-09T19:55 | MFI reversion | sell | GOOGL | 12.27 | -0.02 | end-of-day flatten |
| 2026-10-09T19:55 | VWAP reversion | sell | NVDA | 17.08 | -0.04 | end-of-day flatten |
| 2026-10-09T19:55 | Z-score reversion | buy | ETH-USD | 3.08 | — | rebalance up |
| 2026-10-09T19:55 | Z-score reversion | buy | DOGE-USD | 15.39 | — | entry signal |
| 2026-10-09T19:55 | Z-score reversion | buy | BTC-USD | 3.08 | — | rebalance up |
| 2026-10-09T19:55 | Z-score reversion | sell | MSTR | 12.32 | -0.01 | end-of-day flatten |
| 2026-10-09T19:55 | Z-score reversion | sell | META | 12.29 | -0.02 | end-of-day flatten |
| 2026-10-09T19:55 | Z-score reversion | sell | BITX | 12.32 | -0.03 | end-of-day flatten |
| 2026-10-09T19:55 | RSI(14) reversion | buy | SOL-USD | 18.89 | — | entry signal |
| 2026-10-09T19:55 | RSI(14) reversion | sell | MSTR | 18.90 | 0.01 | end-of-day flatten |
| 2026-10-09T19:55 | RSI(14) reversion | sell | META | 18.84 | -0.11 | end-of-day flatten |
| 2026-10-09T19:55 | RSI(14) reversion | sell | BITX | 18.88 | -0.06 | end-of-day flatten |
| 2026-10-09T19:55 | Three white soldiers | sell | AMZN | 22.37 | 0.09 | end-of-day flatten |
| 2026-10-09T19:55 | Volume breakout | sell | PLTR | 18.02 | 0.12 | end-of-day flatten |
| 2026-10-09T19:55 | Squeeze breakout | sell | PLTR | 18.59 | 0.15 | end-of-day flatten |
| 2026-10-09T19:55 | Keltner breakout | sell | PLTR | 13.20 | 0.26 | end-of-day flatten |
| 2026-10-09T19:55 | Keltner breakout | sell | AMZN | 16.35 | -0.02 | end-of-day flatten |
| 2026-10-09T19:55 | Bollinger breakout | sell | PLTR | 11.01 | 0.10 | end-of-day flatten |
| 2026-10-09T19:55 | Bollinger breakout | sell | AMZN | 13.66 | 0.01 | end-of-day flatten |
| 2026-10-09T19:55 | Opening range 30m | sell | UPRO | 11.37 | 0.03 | end-of-day flatten |
| 2026-10-09T19:55 | Opening range 30m | sell | TNA | 4.71 | -0.01 | end-of-day flatten |
| 2026-10-09T19:55 | Opening range 30m | sell | SPY | 10.09 | -0.01 | end-of-day flatten |
| 2026-10-09T19:55 | Opening range 30m | sell | PLTR | 3.96 | 0.08 | end-of-day flatten |
| 2026-10-09T19:55 | Opening range 30m | sell | MSTR | 10.00 | -0.08 | end-of-day flatten |
| 2026-10-09T19:55 | Opening range 30m | sell | MSFT | 7.57 | 0.03 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 19:57:05.000169+00:00 -> 2026-10-09 20:07:05.000169+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
