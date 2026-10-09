# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T17:01:05.000143+00:00 · 16950 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.89 (-4.11%)

Closed trades 52, win rate 55.8%, fees £2.10, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 19.05 | -0.16 |

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

Today: 23904 decisions in 2424 calls, $0.3019 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T17:01 | 5 / 17 / 7 | COIN 14% |  |
| Breezy | 2026-10-09T17:01 | 0 / 28 / 1 | cash |  |
| Boozy | 2026-10-09T17:01 | 2 / 26 / 1 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| MFI reversion | AAPL | 1.85 | +0.72% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.33 | 3.33 | 37 | 43.2 | -8.02 | -2.46 | -13.79 | 118 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.40 | 2.40 | 0 | — | -4.28 | -0.70 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.18 | 2.18 | 0 | — | -3.67 | -1.51 | -7.31 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 6 | Hold SPY | benchmark | 101.30 | 1.30 | 0 | — | 0.45 | 0.31 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.27 | 1.27 | 0 | — | 1.71 | 0.84 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 101.10 | 1.10 | 0 | — | -0.94 | -0.49 | -5.09 | 1 |
| 9 | Copy: Insider buying | copy | 100.53 | 0.53 | 14 | 57.1 | -13.51 | -2.27 | -21.08 | 72 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Max aggression: 1-day momentum | meta | 100.36 | 0.36 | 10 | 30.0 | -15.07 | -0.51 | -37.31 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.90 | -0.10 | 9 | 22.2 | 3.61 | 1.14 | -7.55 | 44 |
| 15 | Stochastic reversion · 1h | reversion | 99.75 | -0.25 | 88 | 55.7 | -10.41 | -1.99 | -14.99 | 341 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.63 | -0.37 | 0 | — | -3.97 | -1.85 | -5.36 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.64 | -1.74 | -3.04 | 20 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 99.21 | -0.79 | 34 | 35.3 | 4.85 | 2.29 | -1.52 | 90 |
| 19 | Hold BTC | benchmark | 98.91 | -1.09 | 0 | — | 26.67 | 3.21 | -8.68 | 1 |
| 20 | Copy: Cathie Wood (ARKK) | copy | 98.87 | -1.13 | 0 | — | 11.77 | 1.91 | -8.33 | 1 |
| 21 | Donchian 55/20 · 1h | breakout | 98.78 | -1.22 | 27 | 14.8 | 12.67 | 1.59 | -16.96 | 109 |
| 22 | Daily: SMA 20/50 cross · AAPL | daily | 98.23 | -1.77 | 0 | — | 1.18 | 0.52 | -5.18 | 1 |
| 23 | Daily: Bullish score | daily | 97.71 | -2.29 | 4 | 0.0 | 0.65 | 0.28 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.49 | -2.51 | 6 | 0.0 | -3.14 | -2.43 | -4.19 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.44 | -2.56 | 38 | 42.1 | 0.51 | 0.23 | -8.60 | 165 |
| 26 | Trend pullback · 1h | trend | 97.24 | -2.76 | 78 | 23.1 | -22.60 | -6.34 | -25.39 | 169 |
| 27 | EMA 20/50 cross · 1h | trend | 96.82 | -3.18 | 38 | 13.2 | 4.37 | 0.70 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.79 | -3.21 | 79 | 29.1 | 2.41 | 0.68 | -8.65 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.54 | -3.46 | 55 | 21.8 | -2.34 | -0.20 | -13.84 | 255 |
| 31 | Parabolic SAR · 1h | trend | 96.40 | -3.60 | 82 | 22.0 | -2.81 | -0.21 | -20.87 | 293 |
| 32 | MACD cross · 1h | trend | 96.17 | -3.83 | 107 | 22.4 | -16.96 | -2.76 | -18.77 | 472 |
| 33 | Agent | meta | 95.89 | -4.11 | 52 | 55.8 | -9.75 | -5.39 | -10.28 | 245 |
| 34 | Supertrend · 1h | trend | 95.00 | -5.00 | 52 | 13.5 | -0.37 | 0.14 | -18.22 | 209 |
| 35 | Squeeze breakout · 1h | breakout | 94.43 | -5.57 | 35 | 25.7 | 24.44 | 3.32 | -8.61 | 105 |
| 36 | MFI reversion · 1h | reversion | 94.24 | -5.76 | 111 | 35.1 | -10.73 | -1.61 | -17.79 | 129 |
| 37 | Gap and go | momentum | 93.91 | -6.09 | 56 | 10.7 | 7.64 | 1.97 | -6.64 | 200 |
| 38 | Agent (aggressive) | meta | 93.83 | -6.17 | 24 | 45.8 | -4.62 | -2.12 | -6.26 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.57 | -6.43 | 26 | 26.9 | -2.79 | -0.50 | -9.03 | 154 |
| 40 | Agent (ML meta-label) | meta | 93.08 | -6.92 | 388 | 18.0 | -6.47 | -1.06 | -13.37 | 428 |
| 41 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.21 | 0.23 | -19.98 | 118 |
| 42 | Bollinger reversion · 1h | reversion | 93.02 | -6.97 | 72 | 37.5 | -20.65 | -4.91 | -23.70 | 318 |
| 43 | Connors RSI(2) · 1h | reversion | 92.78 | -7.22 | 110 | 43.6 | -18.54 | -6.17 | -20.97 | 253 |
| 44 | RSI momentum · 1h | momentum | 92.69 | -7.31 | 63 | 15.9 | 3.73 | 0.65 | -17.07 | 219 |
| 45 | Volume breakout · 1h | breakout | 92.21 | -7.79 | 51 | 15.7 | 7.49 | 1.18 | -12.60 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 91.78 | -8.22 | 67 | 29.9 | 5.45 | 0.87 | -12.90 | 288 |
| 47 | Williams %R · 1h | reversion | 91.65 | -8.35 | 116 | 48.3 | -25.71 | -4.46 | -27.59 | 516 |
| 48 | Opening range 30m | breakout | 91.13 | -8.87 | 134 | 20.1 | -16.77 | -5.08 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.89 | -9.11 | 69 | 15.9 | -8.68 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.71 | -9.29 | 107 | 30.8 | -28.02 | -5.47 | -30.24 | 517 |
| 51 | CCI reversion · 1h | reversion | 90.27 | -9.73 | 94 | 42.6 | -8.98 | -1.16 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.90 | -10.10 | 270 | 22.2 | -35.38 | -5.34 | -39.25 | 1280 |
| 53 | MACD zero-line · 1h | trend | 89.64 | -10.36 | 59 | 20.3 | -6.40 | -0.68 | -19.40 | 238 |
| 54 | Opening range 15m | breakout | 89.32 | -10.68 | 156 | 18.6 | -18.34 | -5.20 | -19.78 | 700 |
| 55 | Three white soldiers | momentum | 89.13 | -10.87 | 126 | 19.0 | -47.87 | -23.28 | -48.05 | 584 |
| 56 | Donchian 20/10 · 1h | breakout | 88.84 | -11.16 | 57 | 19.3 | -0.95 | 0.09 | -17.72 | 222 |
| 57 | Heikin-Ashi · 1h | trend | 88.64 | -11.36 | 135 | 25.2 | -31.61 | -5.33 | -36.59 | 699 |
| 58 | OBV trend · 1h | momentum | 88.63 | -11.37 | 143 | 18.2 | -13.02 | -1.49 | -28.86 | 318 |
| 59 | EMA 9/21 cross · 1h | trend | 87.72 | -12.28 | 101 | 13.9 | -10.49 | -1.22 | -21.49 | 338 |
| 60 | Keltner breakout · 1h | breakout | 86.79 | -13.21 | 43 | 18.6 | -11.98 | -1.39 | -25.31 | 216 |
| 61 | ROC + volume · 1h | momentum | 86.61 | -13.39 | 130 | 21.5 | -10.34 | -1.26 | -23.72 | 415 |
| 62 | Max aggression: 5-day momentum | meta | 86.45 | -13.55 | 7 | 28.6 | -15.84 | -1.22 | -34.64 | 28 |
| 63 | RSI(14) reversion | reversion | 75.83 | -24.18 | 346 | 28.9 | -73.38 | -18.63 | -73.63 | 1505 |
| 64 | ROC + volume | momentum | 75.38 | -24.62 | 375 | 22.1 | -73.14 | -16.95 | -74.12 | 1666 |
| 65 | Squeeze breakout | breakout | 74.21 | -25.79 | 285 | 15.1 | -61.48 | -18.09 | -61.73 | 1207 |
| 66 | Donchian 55/20 | breakout | 72.88 | -27.12 | 292 | 17.1 | -67.89 | -14.41 | -68.48 | 1289 |
| 67 | EMA 20/50 cross | trend | 72.09 | -27.91 | 295 | 19.3 | -77.62 | -15.56 | -77.82 | 1463 |
| 68 | Volume breakout | breakout | 71.60 | -28.39 | 240 | 13.8 | -63.34 | -18.17 | -63.49 | 899 |
| 69 | VWAP reversion | reversion | 68.49 | -31.51 | 386 | 26.2 | -72.24 | -16.67 | -72.59 | 1450 |
| 70 | Supertrend | trend | 66.48 | -33.52 | 428 | 20.1 | -86.72 | -21.56 | -86.80 | 1930 |
| 71 | Keltner breakout | breakout | 65.68 | -34.32 | 405 | 14.1 | -84.12 | -27.69 | -84.45 | 1852 |
| 72 | AI bee: Bizzy | ai | 62.58 | -37.42 | 739 | 9.6 | — | — | — | — |
| 73 | Ichimoku | trend | 62.56 | -37.44 | 370 | 8.9 | -81.74 | -23.46 | -81.87 | 1744 |
| 74 | AI bee: Boozy | ai | 62.09 | -37.91 | 246 | 5.3 | — | — | — | — |
| 75 | Z-score reversion | reversion | 61.81 | -38.19 | 472 | 23.9 | -85.99 | -23.83 | -86.04 | 2100 |
| 76 | MFI reversion | reversion | 61.73 | -38.27 | 468 | 21.8 | -88.06 | -28.51 | -88.11 | 2130 |
| 77 | Donchian 20/10 | breakout | 59.45 | -40.55 | 571 | 18.6 | -90.83 | -26.21 | -90.96 | 2655 |
| 78 | Trend pullback | trend | 59.29 | -40.71 | 524 | 15.6 | -90.44 | -27.22 | -90.57 | 2295 |
| 79 | ADX DI cross | trend | 58.90 | -41.10 | 511 | 10.2 | -89.85 | -35.39 | -89.85 | 2142 |
| 80 | RSI momentum | momentum | 58.58 | -41.42 | 533 | 17.3 | -90.25 | -25.66 | -90.38 | 2369 |
| 81 | MACD zero-line | trend | 58.09 | -41.91 | 532 | 15.8 | -91.53 | -30.12 | -91.53 | 2358 |
| 82 | Triple EMA stack | trend | 57.35 | -42.66 | 559 | 15.2 | -93.11 | -30.47 | -93.15 | 2603 |
| 83 | Bollinger breakout | breakout | 55.04 | -44.96 | 596 | 14.9 | -93.52 | -33.23 | -93.54 | 2803 |
| 84 | Consensus | meta | 53.02 | -46.98 | 567 | 10.1 | -94.26 | -26.05 | -94.28 | 2674 |
| 85 | EMA 9/21 cross | trend | 50.87 | -49.13 | 725 | 15.9 | -97.36 | -33.54 | -97.36 | 3536 |
| 86 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -30.83 | -98.73 | 5404 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -36.89 | -96.43 | 3583 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.62 | -99.36 | 5694 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.27 | -32.29 | -96.27 | 3584 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.71 | -99.73 | 6170 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.30 | -38.51 | -97.32 | 3654 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -37.90 | -98.51 | 4714 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -41.45 | -99.53 | 6145 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -34.18 | -95.92 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.68 | -35.26 | -95.68 | 4084 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.48 | -99.90 | 8294 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T17:00 | Williams %R · 1h | buy | SOL-USD | 12.65 | — | entry signal |
| 2026-10-09T17:00 | Candlestick reversal · 1h | buy | XRP-USD | 10.06 | — | entry signal |
| 2026-10-09T17:00 | Candlestick reversal · 1h | sell | QQQ | 10.06 | -0.01 | target is flat |
| 2026-10-09T17:00 | OBV trend · 1h | sell | TSLA | 12.63 | -0.03 | target is flat |
| 2026-10-09T17:00 | MFI reversion | buy | PLTR | 15.45 | — | entry |
| 2026-10-09T17:00 | MFI reversion | sell | XRP-USD | 15.44 | -0.09 | exit signal |
| 2026-10-09T17:00 | MFI reversion | sell | TSLA | 15.38 | -0.04 | target is flat |
| 2026-10-09T17:00 | Z-score reversion | sell | AAPL | 15.49 | 0.07 | exit signal |
| 2026-10-09T17:00 | Three white soldiers | sell | AMZN | 22.26 | -0.04 | exit signal |
| 2026-10-09T17:00 | Squeeze breakout | buy | META | 7.51 | — | rebalance up |
| 2026-10-09T17:00 | Squeeze breakout | sell | AMZN | 14.87 | 0.09 | exit signal |
| 2026-10-09T17:00 | Bollinger breakout | buy | COIN | 11.01 | — | entry signal |
| 2026-10-09T17:00 | Bollinger breakout | sell | PLTR | 11.00 | 0.09 | exit signal |
| 2026-10-09T17:00 | Donchian 20/10 | buy | TNA | 2.02 | — | entry |
| 2026-10-09T17:00 | Donchian 20/10 | buy | IWM | 5.41 | — | entry |
| 2026-10-09T17:00 | Donchian 20/10 | sell | AMZN | 6.59 | 0.03 | exit signal |
| 2026-10-09T16:59 | AI bee: Bizzy | sell | META | 8.80 | -0.01 | Jev: sell (sell p=0.50) after 14 min |
| 2026-10-09T16:55 | Candlestick reversal · 1h | buy | QQQ | 10.08 | — | entry |
| 2026-10-09T16:55 | Volume breakout · 1h | sell | AMZN | 23.04 | -0.03 | target is flat |
| 2026-10-09T16:55 | MFI reversion | sell | PLTR | 15.44 | -0.01 | target is flat |
| 2026-10-09T16:55 | RSI(14) reversion | sell | AAPL | 18.93 | 0.07 | exit signal |
| 2026-10-09T16:55 | Keltner breakout | buy | GOOGL | 3.62 | — | entry |
| 2026-10-09T16:55 | Keltner breakout | sell | UPRO | 3.62 | 0.02 | rebalance down |
| 2026-10-09T16:55 | ROC + volume | buy | COIN | 11.41 | — | entry signal |
| 2026-10-09T16:55 | ROC + volume | sell | MSFT | 3.77 | 0.02 | rebalance down |
| 2026-10-09T16:55 | ROC + volume | sell | META | 3.86 | 0.01 | rebalance down |
| 2026-10-09T16:55 | ROC + volume | sell | GOOGL | 3.78 | -0.01 | rebalance down |
| 2026-10-09T16:55 | MACD zero-line | buy | AAPL | 14.53 | — | entry signal |
| 2026-10-09T16:50 | MFI reversion · 1h | buy | LABU | 14.14 | — | entry |
| 2026-10-09T16:50 | MFI reversion · 1h | sell | ETHU | 4.74 | 0.00 | rebalance down |
| 2026-10-09T16:50 | Candlestick reversal · 1h | sell | QQQ | 10.08 | -0.01 | target is flat |
| 2026-10-09T16:50 | Volume breakout · 1h | buy | AMZN | 23.07 | — | entry |
| 2026-10-09T16:50 | OBV trend · 1h | buy | TSLA | 12.66 | — | entry |
| 2026-10-09T16:50 | MFI reversion | buy | TSLA | 15.41 | — | entry |
| 2026-10-09T16:50 | ROC + volume | buy | LABU | 18.73 | — | entry |
| 2026-10-09T16:50 | MACD zero-line | buy | ETH-USD | 14.54 | — | entry signal |
| 2026-10-09T16:50 | EMA 20/50 cross | buy | DOGE-USD | 5.19 | — | entry signal |
| 2026-10-09T16:50 | EMA 9/21 cross | buy | ETH-USD | 10.14 | — | entry signal |
| 2026-10-09T16:50 | EMA 9/21 cross | sell | META | 2.56 | 0.01 | rebalance down |
| 2026-10-09T16:50 | EMA 9/21 cross | sell | DOGE-USD | 2.55 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 17:01:05.000143+00:00 -> 2026-10-09 17:11:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
