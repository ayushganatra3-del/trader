# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T15:30:05.000153+00:00 · 16873 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.05 (-3.95%)

Closed trades 52, win rate 55.8%, fees £2.09, max drawdown -5.22%.

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

Today: 16992 decisions in 2193 calls, $0.2211 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T15:30 | 1 / 21 / 7 | COIN 14%, PLTR 15%, AAPL 15% |  |
| Breezy | 2026-10-09T15:30 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-09T15:30 | 2 / 24 / 3 | COIN 75% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.33 | 3.33 | 37 | 43.2 | -7.73 | -2.34 | -13.79 | 119 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 102.51 | 2.51 | 0 | — | -3.39 | -1.36 | -7.31 | 1 |
| 3 | Timing: Nasdaq FTD · TQQQ | daily | 101.90 | 1.90 | 0 | — | -4.78 | -0.79 | -15.27 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.20 | 1.20 | 0 | — | 1.62 | 0.79 | -3.62 | 1 |
| 7 | Hold SPY | benchmark | 101.18 | 1.18 | 0 | — | 0.30 | 0.22 | -3.66 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 100.97 | 0.97 | 0 | — | -1.09 | -0.58 | -5.09 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.43 | 0.43 | 9 | 22.2 | 4.13 | 1.27 | -7.55 | 44 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Stochastic reversion · 1h | reversion | 99.59 | -0.41 | 88 | 55.7 | -10.60 | -2.02 | -15.02 | 341 |
| 14 | Copy: Insider buying | copy | 99.55 | -0.45 | 13 | 53.8 | -14.28 | -2.44 | -21.08 | 72 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.64 | -1.73 | -3.04 | 20 |
| 16 | Hold BTC | benchmark | 99.13 | -0.87 | 0 | — | 27.04 | 3.22 | -8.68 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.09 | -0.91 | 34 | 35.3 | 4.64 | 2.18 | -1.52 | 90 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 98.82 | -1.18 | 0 | — | -4.78 | -2.27 | -5.36 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 98.53 | -1.47 | 27 | 14.8 | 12.37 | 1.55 | -16.96 | 109 |
| 20 | Copy: Cathie Wood (ARKK) | copy | 98.50 | -1.50 | 0 | — | 11.32 | 1.84 | -8.33 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.18 | -1.82 | 0 | — | 1.11 | 0.49 | -5.18 | 1 |
| 22 | Daily: Bullish score | daily | 97.77 | -2.23 | 4 | 0.0 | 0.71 | 0.29 | -12.76 | 11 |
| 23 | Three white soldiers · 1h | momentum | 97.53 | -2.47 | 6 | 0.0 | -3.10 | -2.38 | -4.15 | 26 |
| 24 | Max aggression: 1-day momentum | meta | 97.26 | -2.74 | 10 | 30.0 | -17.71 | -0.72 | -37.31 | 43 |
| 25 | Agent (rotation) | meta | 96.96 | -3.04 | 79 | 29.1 | 2.89 | 0.79 | -8.65 | 262 |
| 26 | Z-score reversion · 1h | reversion | 96.93 | -3.08 | 37 | 40.5 | -0.05 | 0.12 | -8.60 | 165 |
| 27 | Trend pullback · 1h | trend | 96.89 | -3.10 | 78 | 23.1 | -22.89 | -6.41 | -25.39 | 169 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.46 | -17.67 | 40 |
| 29 | EMA 20/50 cross · 1h | trend | 96.56 | -3.44 | 37 | 10.8 | 4.05 | 0.66 | -19.85 | 135 |
| 30 | ADX DI cross · 1h | trend | 96.07 | -3.93 | 55 | 21.8 | -2.99 | -0.30 | -13.84 | 255 |
| 31 | Agent | meta | 96.05 | -3.95 | 52 | 55.8 | -9.64 | -5.28 | -10.28 | 243 |
| 32 | MACD cross · 1h | trend | 95.82 | -4.18 | 106 | 22.6 | -17.27 | -2.80 | -18.77 | 468 |
| 33 | Parabolic SAR · 1h | trend | 95.65 | -4.35 | 82 | 22.0 | -3.49 | -0.30 | -20.87 | 293 |
| 34 | Supertrend · 1h | trend | 94.56 | -5.44 | 52 | 13.5 | -1.14 | 0.04 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.24 | -5.76 | 35 | 25.7 | 23.61 | 3.20 | -8.61 | 107 |
| 36 | Agent (aggressive) | meta | 94.22 | -5.78 | 24 | 45.8 | -4.23 | -1.91 | -6.26 | 107 |
| 37 | Gap and go | momentum | 93.86 | -6.13 | 56 | 10.7 | 7.65 | 1.95 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.82 | -6.18 | 106 | 34.0 | -12.61 | -1.97 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.42 | -6.58 | 26 | 26.9 | -2.29 | -0.39 | -9.03 | 151 |
| 40 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.21 | 0.23 | -19.98 | 118 |
| 41 | Agent (ML meta-label) | meta | 92.93 | -7.07 | 387 | 18.1 | -6.05 | -1.02 | -12.63 | 419 |
| 42 | Connors RSI(2) · 1h | reversion | 92.93 | -7.07 | 110 | 43.6 | -18.43 | -6.08 | -20.97 | 253 |
| 43 | Bollinger reversion · 1h | reversion | 92.89 | -7.11 | 72 | 37.5 | -20.84 | -4.94 | -23.75 | 318 |
| 44 | RSI momentum · 1h | momentum | 92.39 | -7.61 | 63 | 15.9 | 3.39 | 0.61 | -17.07 | 219 |
| 45 | Volume breakout · 1h | breakout | 92.17 | -7.83 | 46 | 17.4 | 7.29 | 1.15 | -12.60 | 122 |
| 46 | Williams %R · 1h | reversion | 91.51 | -8.49 | 115 | 47.8 | -25.85 | -4.46 | -27.60 | 515 |
| 47 | Bollinger breakout · 1h | breakout | 91.43 | -8.57 | 67 | 29.9 | 5.09 | 0.82 | -12.86 | 288 |
| 48 | Candlestick reversal · 1h | reversion | 90.85 | -9.14 | 104 | 30.8 | -27.74 | -5.37 | -29.94 | 511 |
| 49 | Opening range 30m | breakout | 90.85 | -9.15 | 133 | 20.3 | -17.11 | -5.17 | -17.78 | 573 |
| 50 | Triple EMA stack · 1h | trend | 90.51 | -9.49 | 69 | 15.9 | -9.07 | -0.91 | -26.35 | 235 |
| 51 | CCI reversion · 1h | reversion | 89.85 | -10.15 | 93 | 41.9 | -9.41 | -1.23 | -14.35 | 415 |
| 52 | MACD zero-line · 1h | trend | 89.81 | -10.19 | 59 | 20.3 | -6.23 | -0.65 | -19.40 | 238 |
| 53 | VWAP momentum · 1h | momentum | 89.60 | -10.39 | 268 | 22.0 | -35.62 | -5.35 | -39.34 | 1274 |
| 54 | Three white soldiers | momentum | 89.15 | -10.85 | 124 | 18.5 | -47.87 | -22.87 | -48.05 | 583 |
| 55 | Opening range 15m | breakout | 88.97 | -11.03 | 155 | 18.7 | -18.67 | -5.30 | -19.78 | 696 |
| 56 | Donchian 20/10 · 1h | breakout | 88.55 | -11.45 | 57 | 19.3 | -1.35 | 0.04 | -17.72 | 221 |
| 57 | OBV trend · 1h | momentum | 88.46 | -11.54 | 141 | 17.7 | -13.34 | -1.53 | -28.86 | 318 |
| 58 | Heikin-Ashi · 1h | trend | 88.15 | -11.85 | 135 | 25.2 | -32.05 | -5.41 | -36.59 | 697 |
| 59 | EMA 9/21 cross · 1h | trend | 87.58 | -12.42 | 101 | 13.9 | -10.69 | -1.24 | -21.45 | 337 |
| 60 | Keltner breakout · 1h | breakout | 86.70 | -13.30 | 43 | 18.6 | -12.20 | -1.41 | -25.26 | 214 |
| 61 | Max aggression: 5-day momentum | meta | 86.30 | -13.70 | 7 | 28.6 | -16.00 | -1.23 | -34.64 | 28 |
| 62 | ROC + volume · 1h | momentum | 86.09 | -13.91 | 130 | 21.5 | -10.19 | -1.23 | -23.20 | 415 |
| 63 | RSI(14) reversion | reversion | 75.92 | -24.08 | 345 | 28.7 | -73.67 | -18.50 | -73.95 | 1510 |
| 64 | ROC + volume | momentum | 75.43 | -24.57 | 370 | 21.9 | -72.99 | -16.59 | -73.95 | 1663 |
| 65 | Squeeze breakout | breakout | 74.05 | -25.95 | 284 | 14.8 | -61.73 | -18.06 | -61.88 | 1208 |
| 66 | Donchian 55/20 | breakout | 72.38 | -27.61 | 291 | 17.2 | -68.07 | -14.39 | -68.48 | 1287 |
| 67 | EMA 20/50 cross | trend | 71.97 | -28.03 | 294 | 19.0 | -77.61 | -15.39 | -77.76 | 1459 |
| 68 | Volume breakout | breakout | 71.68 | -28.32 | 237 | 13.5 | -63.35 | -17.92 | -63.50 | 901 |
| 69 | VWAP reversion | reversion | 68.53 | -31.47 | 385 | 26.0 | -72.28 | -16.29 | -72.61 | 1445 |
| 70 | Supertrend | trend | 66.28 | -33.72 | 427 | 20.1 | -86.80 | -21.31 | -86.83 | 1931 |
| 71 | Keltner breakout | breakout | 65.39 | -34.61 | 405 | 14.1 | -84.27 | -27.47 | -84.53 | 1851 |
| 72 | AI bee: Bizzy | ai | 62.45 | -37.55 | 732 | 9.2 | — | — | — | — |
| 73 | Ichimoku | trend | 62.35 | -37.66 | 370 | 8.9 | -81.77 | -23.06 | -81.87 | 1737 |
| 74 | Z-score reversion | reversion | 61.87 | -38.13 | 471 | 23.8 | -85.98 | -23.38 | -86.04 | 2099 |
| 75 | MFI reversion | reversion | 61.83 | -38.16 | 456 | 21.5 | -88.17 | -28.29 | -88.17 | 2144 |
| 76 | AI bee: Boozy | ai | 61.49 | -38.51 | 246 | 5.3 | — | — | — | — |
| 77 | Donchian 20/10 | breakout | 59.22 | -40.78 | 568 | 18.1 | -90.89 | -25.85 | -90.99 | 2652 |
| 78 | ADX DI cross | trend | 58.96 | -41.04 | 510 | 10.2 | -89.85 | -34.41 | -89.85 | 2141 |
| 79 | Trend pullback | trend | 58.88 | -41.12 | 521 | 15.5 | -90.52 | -26.85 | -90.59 | 2290 |
| 80 | MACD zero-line | trend | 58.32 | -41.68 | 531 | 15.8 | -91.49 | -29.35 | -91.49 | 2354 |
| 81 | RSI momentum | momentum | 58.31 | -41.69 | 533 | 17.3 | -90.30 | -25.25 | -90.38 | 2364 |
| 82 | Triple EMA stack | trend | 57.08 | -42.92 | 559 | 15.2 | -93.12 | -29.71 | -93.14 | 2598 |
| 83 | Bollinger breakout | breakout | 55.04 | -44.96 | 592 | 14.9 | -93.56 | -32.59 | -93.58 | 2802 |
| 84 | Consensus | meta | 53.02 | -46.98 | 564 | 9.9 | -94.27 | -25.53 | -94.28 | 2673 |
| 85 | EMA 9/21 cross | trend | 51.02 | -48.98 | 721 | 16.0 | -97.36 | -32.70 | -97.37 | 3531 |
| 86 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -30.16 | -98.72 | 5386 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.40 | -35.58 | -96.43 | 3577 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.36 | -99.36 | 5686 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.27 | -31.43 | -96.28 | 3575 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.04 | -99.73 | 6150 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.32 | -37.39 | -97.33 | 3642 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.50 | -98.50 | 4707 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.84 | -99.53 | 6138 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -33.31 | -95.93 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -34.28 | -95.70 | 4079 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.25 | -99.90 | 8269 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T15:30 | Agent (ML meta-label) | buy | BTC-USD | 4.58 | — | entry |
| 2026-10-09T15:30 | Agent (ML meta-label) | sell | META | 4.58 | -0.01 | selected signal exited |
| 2026-10-09T15:30 | Consensus | buy | MSFT | 13.26 | — | entry |
| 2026-10-09T15:30 | Agent (aggressive) | sell | UPRO | 47.08 | -0.06 | selected signal exited |
| 2026-10-09T15:30 | Agent | sell | UPRO | 19.22 | 0.01 | selected signal exited |
| 2026-10-09T15:30 | CCI reversion · 1h | buy | QQQ | 1.26 | — | entry |
| 2026-10-09T15:30 | CCI reversion · 1h | buy | AAPL | 5.62 | — | entry signal |
| 2026-10-09T15:30 | CCI reversion · 1h | sell | MSFT | 2.18 | 0.01 | exit signal |
| 2026-10-09T15:30 | CCI reversion · 1h | sell | LABU | 4.69 | 0.27 | rebalance down |
| 2026-10-09T15:30 | Williams %R · 1h | buy | TQQQ | 6.10 | — | rebalance up |
| 2026-10-09T15:30 | Williams %R · 1h | buy | TECL | 6.09 | — | rebalance up |
| 2026-10-09T15:30 | Williams %R · 1h | buy | SPY | 6.09 | — | rebalance up |
| 2026-10-09T15:30 | Williams %R · 1h | buy | QQQ | 6.11 | — | rebalance up |
| 2026-10-09T15:30 | Williams %R · 1h | buy | META | 6.10 | — | rebalance up |
| 2026-10-09T15:30 | Williams %R · 1h | sell | UPRO | 7.02 | 0.09 | exit signal |
| 2026-10-09T15:30 | Williams %R · 1h | sell | AMZN | 11.50 | 0.04 | exit signal |
| 2026-10-09T15:30 | Bollinger reversion · 1h | buy | TQQQ | 6.31 | — | rebalance up |
| 2026-10-09T15:30 | Bollinger reversion · 1h | buy | SOXL | 6.69 | — | rebalance up |
| 2026-10-09T15:30 | Bollinger reversion · 1h | buy | QQQ | 6.33 | — | rebalance up |
| 2026-10-09T15:30 | Bollinger reversion · 1h | buy | META | 6.32 | — | rebalance up |
| 2026-10-09T15:30 | Bollinger reversion · 1h | buy | ETHU | 5.13 | — | rebalance up |
| 2026-10-09T15:30 | Bollinger reversion · 1h | buy | BITX | 6.00 | — | rebalance up |
| 2026-10-09T15:30 | Bollinger reversion · 1h | sell | UPRO | 13.34 | 0.12 | exit signal |
| 2026-10-09T15:30 | Candlestick reversal · 1h | sell | BITX | 12.94 | 0.05 | exit signal |
| 2026-10-09T15:30 | RSI momentum · 1h | buy | MSFT | 8.22 | — | entry signal |
| 2026-10-09T15:30 | RSI momentum · 1h | buy | AMZN | 15.40 | — | entry signal |
| 2026-10-09T15:30 | RSI momentum · 1h | sell | TSLA | 7.41 | -0.12 | rebalance down |
| 2026-10-09T15:30 | RSI momentum · 1h | sell | BTC-USD | 7.72 | -0.04 | rebalance down |
| 2026-10-09T15:30 | VWAP momentum · 1h | buy | UPRO | 6.40 | — | entry |
| 2026-10-09T15:30 | VWAP momentum · 1h | buy | TECL | 6.40 | — | entry signal |
| 2026-10-09T15:30 | VWAP momentum · 1h | buy | SOL-USD | 6.40 | — | entry |
| 2026-10-09T15:30 | VWAP momentum · 1h | sell | TSLA | 5.89 | 0.12 | exit signal |
| 2026-10-09T15:30 | VWAP momentum · 1h | sell | GOOGL | 5.96 | -0.03 | exit signal |
| 2026-10-09T15:30 | VWAP momentum · 1h | sell | BITX | 8.07 | 0.03 | exit signal |
| 2026-10-09T15:30 | Heikin-Ashi · 1h | buy | UPRO | 8.80 | — | entry signal |
| 2026-10-09T15:30 | Heikin-Ashi · 1h | buy | SPY | 8.82 | — | entry signal |
| 2026-10-09T15:30 | Heikin-Ashi · 1h | buy | PLTR | 8.82 | — | entry signal |
| 2026-10-09T15:30 | Heikin-Ashi · 1h | buy | MSFT | 8.82 | — | entry signal |
| 2026-10-09T15:30 | Heikin-Ashi · 1h | buy | GOOGL | 8.82 | — | entry signal |
| 2026-10-09T15:30 | Heikin-Ashi · 1h | buy | AMZN | 8.82 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 15:30:05.000153+00:00 -> 2026-10-09 15:40:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
