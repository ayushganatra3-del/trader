# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T19:28:05.000149+00:00 · 17052 ticks

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

Today: 32970 decisions in 2730 calls, $0.4079 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T19:28 | 1 / 15 / 14 | TECL 14% |  |
| Breezy | 2026-10-09T19:28 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-09T19:28 | 0 / 26 / 4 | COIN 75% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.33 | 3.33 | 37 | 43.2 | -7.16 | -2.15 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.72 | 2.72 | 0 | — | -3.89 | -0.61 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.12 | 2.12 | 0 | — | -3.64 | -1.49 | -7.31 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 6 | Copy: Insider buying | copy | 101.53 | 1.53 | 14 | 57.1 | -12.48 | -2.02 | -21.08 | 72 |
| 7 | Hold SPY | benchmark | 101.33 | 1.33 | 0 | — | 0.57 | 0.38 | -3.66 | 1 |
| 8 | Copy: Congress Democrats (NANC) | copy | 101.28 | 1.28 | 0 | — | 1.83 | 0.89 | -3.62 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.79 | -0.41 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.85 | -0.15 | 10 | 30.0 | -15.42 | -0.54 | -37.31 | 43 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.54 | -0.46 | 0 | — | -3.97 | -1.85 | -5.36 | 1 |
| 15 | Stochastic reversion · 1h | reversion | 99.50 | -0.50 | 88 | 55.7 | -10.54 | -2.02 | -15.02 | 342 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.47 | -0.53 | 35 | 37.1 | 5.23 | 2.45 | -1.52 | 90 |
| 17 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.36 | -0.64 | 9 | 22.2 | 3.15 | 1.01 | -7.55 | 44 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.64 | -1.74 | -3.04 | 20 |
| 19 | Donchian 55/20 · 1h | breakout | 99.10 | -0.90 | 27 | 14.8 | 13.11 | 1.64 | -16.96 | 109 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 98.82 | -1.18 | 0 | — | 1.90 | 0.80 | -5.18 | 1 |
| 21 | Copy: Cathie Wood (ARKK) | copy | 98.77 | -1.23 | 0 | — | 11.76 | 1.91 | -8.33 | 1 |
| 22 | Hold BTC | benchmark | 98.53 | -1.47 | 0 | — | 26.40 | 3.18 | -8.68 | 1 |
| 23 | Daily: Bullish score | daily | 97.83 | -2.17 | 4 | 0.0 | 0.85 | 0.31 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.54 | -2.46 | 6 | 0.0 | -3.06 | -2.37 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.30 | -2.70 | 38 | 42.1 | 0.44 | 0.22 | -8.60 | 165 |
| 26 | Trend pullback · 1h | trend | 97.18 | -2.82 | 78 | 23.1 | -22.57 | -6.33 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.91 | -3.09 | 38 | 13.2 | 4.63 | 0.73 | -19.85 | 135 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 29 | Agent (rotation) | meta | 96.62 | -3.38 | 79 | 29.1 | 2.57 | 0.72 | -8.65 | 255 |
| 30 | ADX DI cross · 1h | trend | 96.29 | -3.71 | 57 | 21.1 | -2.50 | -0.23 | -13.84 | 257 |
| 31 | Parabolic SAR · 1h | trend | 96.22 | -3.78 | 82 | 22.0 | -2.83 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.80 | -4.20 | 107 | 22.4 | -16.74 | -2.72 | -18.37 | 473 |
| 34 | Supertrend · 1h | trend | 94.80 | -5.20 | 52 | 13.5 | -0.44 | 0.13 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.23 | -5.77 | 35 | 25.7 | 24.20 | 3.29 | -8.62 | 105 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.55 | -2.07 | -6.59 | 109 |
| 37 | Gap and go | momentum | 93.93 | -6.07 | 56 | 10.7 | 7.69 | 1.98 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.72 | -6.28 | 115 | 34.8 | -12.50 | -2.06 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.44 | -6.56 | 26 | 26.9 | -2.19 | -0.37 | -9.03 | 151 |
| 40 | Connors RSI(2) · 1h | reversion | 93.12 | -6.88 | 112 | 43.8 | -18.18 | -6.02 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | -0.29 | 0.17 | -19.98 | 119 |
| 42 | Bollinger reversion · 1h | reversion | 93.04 | -6.96 | 73 | 37.0 | -20.62 | -4.89 | -23.75 | 318 |
| 43 | Agent (ML meta-label) | meta | 92.96 | -7.04 | 392 | 18.4 | -4.13 | -0.64 | -13.32 | 424 |
| 44 | RSI momentum · 1h | momentum | 92.66 | -7.33 | 63 | 15.9 | 3.80 | 0.66 | -17.07 | 220 |
| 45 | Volume breakout · 1h | breakout | 92.46 | -7.54 | 53 | 18.9 | 7.96 | 1.24 | -12.60 | 124 |
| 46 | Bollinger breakout · 1h | breakout | 91.82 | -8.18 | 67 | 29.9 | 6.19 | 0.96 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.79 | -8.21 | 116 | 48.3 | -25.05 | -4.30 | -27.34 | 512 |
| 48 | Opening range 30m | breakout | 91.03 | -8.97 | 136 | 19.9 | -16.77 | -5.08 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.80 | -9.20 | 69 | 15.9 | -8.50 | -0.84 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.31 | -9.69 | 113 | 31.0 | -28.30 | -5.56 | -30.17 | 520 |
| 51 | CCI reversion · 1h | reversion | 89.85 | -10.15 | 94 | 42.6 | -9.12 | -1.19 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.74 | -10.26 | 276 | 22.1 | -35.46 | -5.38 | -39.46 | 1276 |
| 53 | MACD zero-line · 1h | trend | 89.43 | -10.57 | 59 | 20.3 | -6.57 | -0.70 | -19.40 | 238 |
| 54 | Opening range 15m | breakout | 89.17 | -10.83 | 159 | 18.2 | -18.36 | -5.21 | -19.78 | 700 |
| 55 | Three white soldiers | momentum | 89.07 | -10.93 | 127 | 18.9 | -47.90 | -23.33 | -48.05 | 586 |
| 56 | Donchian 20/10 · 1h | breakout | 88.79 | -11.21 | 57 | 19.3 | -0.69 | 0.12 | -17.72 | 221 |
| 57 | OBV trend · 1h | momentum | 88.69 | -11.31 | 148 | 18.9 | -12.35 | -1.40 | -28.83 | 319 |
| 58 | Heikin-Ashi · 1h | trend | 88.65 | -11.35 | 137 | 24.8 | -31.69 | -5.35 | -36.59 | 702 |
| 59 | EMA 9/21 cross · 1h | trend | 87.82 | -12.18 | 101 | 13.9 | -10.01 | -1.16 | -21.49 | 337 |
| 60 | Max aggression: 5-day momentum | meta | 87.29 | -12.71 | 7 | 28.6 | -14.93 | -1.12 | -34.64 | 28 |
| 61 | Keltner breakout · 1h | breakout | 86.88 | -13.12 | 43 | 18.6 | -11.49 | -1.32 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.40 | -13.60 | 130 | 21.5 | -9.96 | -1.20 | -23.20 | 414 |
| 63 | RSI(14) reversion | reversion | 75.67 | -24.33 | 346 | 28.9 | -73.32 | -18.59 | -73.54 | 1506 |
| 64 | ROC + volume | momentum | 74.83 | -25.17 | 386 | 22.5 | -73.35 | -17.06 | -74.19 | 1665 |
| 65 | Squeeze breakout | breakout | 73.98 | -26.02 | 293 | 15.4 | -61.59 | -18.19 | -61.73 | 1217 |
| 66 | Donchian 55/20 | breakout | 72.67 | -27.33 | 298 | 17.1 | -67.98 | -14.48 | -68.48 | 1297 |
| 67 | EMA 20/50 cross | trend | 72.13 | -27.87 | 297 | 19.2 | -77.48 | -15.47 | -77.69 | 1462 |
| 68 | Volume breakout | breakout | 71.45 | -28.55 | 246 | 13.4 | -63.52 | -18.33 | -63.65 | 901 |
| 69 | VWAP reversion | reversion | 68.72 | -31.28 | 388 | 26.3 | -72.07 | -16.40 | -72.40 | 1452 |
| 70 | Supertrend | trend | 66.25 | -33.75 | 430 | 20.2 | -86.66 | -21.44 | -86.70 | 1930 |
| 71 | Keltner breakout | breakout | 65.50 | -34.50 | 414 | 14.7 | -84.17 | -27.83 | -84.47 | 1858 |
| 72 | Ichimoku | trend | 62.48 | -37.52 | 375 | 9.3 | -81.73 | -23.45 | -81.87 | 1748 |
| 73 | AI bee: Bizzy | ai | 62.25 | -37.75 | 751 | 9.7 | — | — | — | — |
| 74 | Z-score reversion | reversion | 61.76 | -38.23 | 473 | 23.9 | -85.94 | -23.72 | -85.98 | 2106 |
| 75 | AI bee: Boozy | ai | 61.70 | -38.30 | 246 | 5.3 | — | — | — | — |
| 76 | MFI reversion | reversion | 61.63 | -38.37 | 478 | 22.4 | -87.94 | -28.74 | -87.95 | 2111 |
| 77 | Donchian 20/10 | breakout | 59.40 | -40.60 | 578 | 18.7 | -90.82 | -26.18 | -90.94 | 2663 |
| 78 | Trend pullback | trend | 59.14 | -40.87 | 528 | 15.9 | -90.45 | -27.26 | -90.56 | 2302 |
| 79 | ADX DI cross | trend | 58.80 | -41.20 | 513 | 10.1 | -89.83 | -35.23 | -89.84 | 2144 |
| 80 | RSI momentum | momentum | 58.39 | -41.61 | 543 | 17.3 | -90.24 | -25.61 | -90.35 | 2375 |
| 81 | MACD zero-line | trend | 57.76 | -42.24 | 539 | 15.6 | -91.52 | -29.90 | -91.52 | 2360 |
| 82 | Triple EMA stack | trend | 57.11 | -42.89 | 567 | 15.7 | -93.12 | -30.46 | -93.14 | 2610 |
| 83 | Bollinger breakout | breakout | 54.72 | -45.28 | 608 | 15.0 | -93.55 | -33.32 | -93.55 | 2818 |
| 84 | Consensus | meta | 52.93 | -47.07 | 578 | 10.0 | -94.26 | -25.89 | -94.27 | 2680 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -30.89 | -98.73 | 5397 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.31 | -97.36 | 3541 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.39 | -36.59 | -96.41 | 3592 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.52 | -99.36 | 5706 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.28 | -32.24 | -96.29 | 3603 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.73 | -99.73 | 6205 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.32 | -38.65 | -97.32 | 3674 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.60 | -98.50 | 4725 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -41.12 | -99.53 | 6162 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -34.34 | -95.94 | 3754 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -35.18 | -95.68 | 4095 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.19 | -99.90 | 8330 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T19:25 | Consensus | buy | COIN | 7.54 | — | entry |
| 2026-10-09T19:25 | Consensus | sell | AAPL | 7.54 | -0.02 | target is flat |
| 2026-10-09T19:25 | MFI reversion · 1h | buy | ETHU | 4.78 | — | rebalance up |
| 2026-10-09T19:25 | MFI reversion · 1h | sell | TSLA | 7.80 | -0.01 | target is flat |
| 2026-10-09T19:25 | Candlestick reversal · 1h | sell | QQQ | 10.02 | -0.01 | target is flat |
| 2026-10-09T19:25 | Volume breakout · 1h | buy | AMZN | 23.11 | — | entry |
| 2026-10-09T19:25 | OBV trend · 1h | buy | TQQQ | 1.51 | — | entry |
| 2026-10-09T19:25 | OBV trend · 1h | buy | AAPL | 11.09 | — | entry |
| 2026-10-09T19:25 | OBV trend · 1h | sell | TSLA | 12.60 | -0.02 | target is flat |
| 2026-10-09T19:25 | MFI reversion | buy | AMZN | 8.17 | — | entry |
| 2026-10-09T19:25 | Squeeze breakout | buy | PLTR | 4.09 | — | rebalance up |
| 2026-10-09T19:25 | Squeeze breakout | sell | AAPL | 10.61 | 0.03 | stop-loss |
| 2026-10-09T19:25 | Keltner breakout | buy | UPRO | 3.72 | — | rebalance up |
| 2026-10-09T19:25 | Keltner breakout | buy | TECL | 3.73 | — | rebalance up |
| 2026-10-09T19:25 | Keltner breakout | buy | SPY | 3.75 | — | rebalance up |
| 2026-10-09T19:25 | Keltner breakout | buy | PLTR | 3.72 | — | rebalance up |
| 2026-10-09T19:25 | Keltner breakout | buy | MSFT | 3.77 | — | rebalance up |
| 2026-10-09T19:25 | Keltner breakout | sell | TNA | 9.33 | -0.02 | stop-loss |
| 2026-10-09T19:25 | Keltner breakout | sell | AAPL | 9.35 | 0.00 | stop-loss |
| 2026-10-09T19:25 | Bollinger breakout | buy | QQQ | 2.89 | — | rebalance up |
| 2026-10-09T19:25 | Bollinger breakout | sell | AAPL | 2.79 | 0.01 | stop-loss |
| 2026-10-09T19:25 | ROC + volume | sell | AAPL | 18.65 | -0.06 | stop-loss |
| 2026-10-09T19:25 | MACD zero-line | sell | TSLA | 14.45 | -0.00 | exit signal |
| 2026-10-09T19:24 | AI bee: Bizzy | sell | AAPL | 8.82 | -0.02 | Jev: sell (sell p=0.72) after 11 min |
| 2026-10-09T19:20 | AI bee: Bizzy | buy | TECL | 8.91 | — | Jev: buy (buy p=0.57) |
| 2026-10-09T19:20 | Candlestick reversal · 1h | buy | QQQ | 10.03 | — | entry |
| 2026-10-09T19:20 | Volume breakout · 1h | sell | AMZN | 23.11 | 0.00 | target is flat |
| 2026-10-09T19:20 | MFI reversion | buy | DOGE-USD | 3.53 | — | rebalance up |
| 2026-10-09T19:20 | MFI reversion | sell | TSLA | 8.19 | -0.01 | exit signal |
| 2026-10-09T19:20 | MFI reversion | sell | AMZN | 3.51 | 0.00 | target is flat |
| 2026-10-09T19:20 | Volume breakout | sell | MSFT | 17.84 | -0.03 | exit signal |
| 2026-10-09T19:20 | Squeeze breakout | buy | TSLA | 10.57 | — | entry |
| 2026-10-09T19:20 | Squeeze breakout | buy | TQQQ | 8.78 | — | rebalance up |
| 2026-10-09T19:20 | Squeeze breakout | sell | TNA | 10.57 | -0.02 | exit signal |
| 2026-10-09T19:20 | Squeeze breakout | sell | IWM | 11.06 | -0.02 | exit signal |
| 2026-10-09T19:20 | Bollinger breakout | buy | AMZN | 5.47 | — | entry signal |
| 2026-10-09T19:20 | Bollinger breakout | sell | TNA | 4.56 | -0.01 | exit signal |
| 2026-10-09T19:20 | Bollinger breakout | sell | IWM | 4.97 | -0.01 | exit signal |
| 2026-10-09T19:20 | MACD zero-line | buy | NVDA | 14.45 | — | entry signal |
| 2026-10-09T19:15 | Volume breakout · 1h | buy | MSFT | 22.55 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 19:28:05.000149+00:00 -> 2026-10-09 19:38:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
