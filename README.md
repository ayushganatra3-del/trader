# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T18:40:05.000144+00:00 · 7168 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.75 (-0.25%)

Closed trades 26, win rate 69.2%, fees £0.76, max drawdown -1.39%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-30 | ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, ADRX 12%, BBD 12%, ENHA 12%, CX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.07 · VIX 16.04 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 32109 decisions in 2796 calls, $0.3991 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T18:40 | 7 / 12 / 10 | cash |  |
| Breezy | 2026-09-30T18:40 | 0 / 24 / 5 | cash |  |
| Boozy | 2026-09-30T18:40 | 4 / 20 / 5 | COIN 52% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| RSI(14) reversion · 1h | SOL-USD | 2.42 | +2.64% | 3 |
| Z-score reversion | MSFT | 2.34 | +2.58% | 5 |
| Williams %R | TQQQ | 2.04 | +2.09% | 14 |
| Candlestick reversal | TQQQ | 2.01 | +4.48% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.76 | 1.76 | 2 | 50.0 | 14.82 | 3.19 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.28 | 0.28 | 1 | 100.0 | -0.03 | 0.07 | -9.74 | 24 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.10 | 0.10 | 0 | — | 5.76 | 2.42 | -3.62 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Hold BTC | benchmark | 99.95 | -0.05 | 0 | — | 28.95 | 3.64 | -8.68 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 99.82 | -0.18 | 0 | — | -2.75 | -1.63 | -5.09 | 2 |
| 9 | Agent | meta | 99.75 | -0.25 | 26 | 69.2 | -9.98 | -6.58 | -10.75 | 220 |
| 10 | Timing: Nasdaq FTD · TQQQ | daily | 99.60 | -0.40 | 0 | — | -9.22 | -1.80 | -15.27 | 2 |
| 11 | VWAP reversion · 1h | reversion | 99.56 | -0.44 | 22 | 27.3 | -12.69 | -4.26 | -14.84 | 123 |
| 12 | Hold SPY | benchmark | 99.53 | -0.47 | 0 | — | 3.32 | 1.85 | -3.66 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.50 | -0.50 | 0 | — | 4.46 | 1.30 | -7.93 | 7 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.61 | 1.33 | -2.15 | 83 |
| 15 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -0.41 | -0.21 | -3.92 | 97 |
| 16 | RSI(14) reversion · 1h | reversion | 99.46 | -0.54 | 8 | 62.5 | 4.25 | 1.26 | -6.57 | 121 |
| 17 | Copy: Insider buying | copy | 99.34 | -0.66 | 2 | 100.0 | -13.62 | -2.66 | -17.74 | 73 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 99.12 | -0.88 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 20 | Copy: Warren Buffett (BRK-B) | copy | 99.09 | -0.91 | 0 | — | -1.62 | -0.62 | -7.65 | 1 |
| 21 | Daily: Bullish score | daily | 99.06 | -0.94 | 3 | 0.0 | -0.42 | 0.14 | -12.76 | 14 |
| 22 | Stochastic reversion · 1h | reversion | 98.85 | -1.15 | 30 | 56.7 | -10.78 | -2.38 | -12.37 | 326 |
| 23 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 15.60 | 3.85 | -4.73 | 184 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 25 | Williams %R · 1h | reversion | 98.50 | -1.50 | 51 | 51.0 | -17.37 | -3.26 | -19.41 | 491 |
| 26 | CCI reversion · 1h | reversion | 98.47 | -1.53 | 42 | 40.5 | 1.91 | 0.49 | -12.41 | 414 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.40 | -1.60 | 0 | — | 23.19 | 3.43 | -6.29 | 1 |
| 28 | Daily: SMA 20/50 cross · AAPL | daily | 98.37 | -1.63 | 0 | — | -6.58 | -1.48 | -10.06 | 1 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.31 | 0.23 | -15.21 | 46 |
| 30 | Candlestick reversal · 1h | reversion | 98.26 | -1.74 | 33 | 24.2 | -23.83 | -5.75 | -25.49 | 493 |
| 31 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.65 | -3.36 | -11.53 | 233 |
| 32 | Agent (rotation) | meta | 98.10 | -1.90 | 36 | 13.9 | -5.18 | -1.79 | -9.79 | 208 |
| 33 | Z-score reversion · 1h | reversion | 98.08 | -1.92 | 11 | 45.5 | 4.16 | 1.02 | -8.60 | 155 |
| 34 | Bollinger reversion · 1h | reversion | 97.49 | -2.51 | 32 | 34.4 | -15.67 | -4.34 | -17.12 | 308 |
| 35 | EMA 20/50 cross · 1h | trend | 97.33 | -2.67 | 18 | 5.6 | 15.98 | 2.00 | -12.18 | 131 |
| 36 | Opening range 30m | breakout | 96.82 | -3.18 | 42 | 11.9 | -10.12 | -2.94 | -14.43 | 561 |
| 37 | Supertrend · 1h | trend | 96.27 | -3.73 | 18 | 5.6 | 2.22 | 0.50 | -16.43 | 201 |
| 38 | Agent (ML meta-label) | meta | 96.03 | -3.97 | 159 | 13.2 | 1.97 | 0.50 | -12.09 | 406 |
| 39 | Trend pullback · 1h | trend | 96.01 | -3.99 | 31 | 9.7 | -25.54 | -6.86 | -25.72 | 155 |
| 40 | Donchian 55/20 · 1h | breakout | 95.99 | -4.01 | 15 | 0.0 | 5.33 | 0.89 | -16.96 | 113 |
| 41 | Opening range 15m | breakout | 95.76 | -4.24 | 52 | 11.5 | -11.56 | -3.16 | -16.70 | 689 |
| 42 | Max aggression: 5-day momentum | meta | 95.72 | -4.28 | 3 | 66.7 | -13.20 | -0.92 | -29.56 | 29 |
| 43 | Parabolic SAR · 1h | trend | 95.04 | -4.96 | 30 | 13.3 | -8.68 | -1.10 | -19.53 | 303 |
| 44 | Squeeze breakout · 1h | breakout | 94.96 | -5.04 | 15 | 6.7 | 12.31 | 2.18 | -7.19 | 100 |
| 45 | MFI reversion · 1h | reversion | 94.93 | -5.07 | 51 | 19.6 | -9.46 | -1.72 | -17.20 | 130 |
| 46 | MACD cross · 1h | trend | 94.90 | -5.10 | 42 | 9.5 | -13.44 | -2.11 | -17.38 | 475 |
| 47 | Three white soldiers | momentum | 94.57 | -5.43 | 50 | 20.0 | -50.19 | -27.65 | -50.32 | 606 |
| 48 | Max aggression: 1-day momentum | meta | 94.36 | -5.64 | 3 | 33.3 | -21.37 | -1.02 | -41.28 | 42 |
| 49 | ADX DI cross · 1h | trend | 94.27 | -5.73 | 33 | 6.1 | -15.56 | -2.91 | -17.60 | 260 |
| 50 | Volume breakout · 1h | breakout | 94.26 | -5.74 | 28 | 3.6 | 5.85 | 1.01 | -12.60 | 122 |
| 51 | Ichimoku · 1h | trend | 93.79 | -6.21 | 20 | 15.0 | 5.70 | 0.86 | -15.13 | 122 |
| 52 | RSI momentum · 1h | momentum | 93.40 | -6.60 | 28 | 3.6 | -0.86 | 0.08 | -15.29 | 219 |
| 53 | Bollinger breakout · 1h | breakout | 93.26 | -6.74 | 24 | 8.3 | 6.40 | 1.03 | -9.63 | 280 |
| 54 | VWAP momentum · 1h | momentum | 92.85 | -7.15 | 127 | 15.7 | -38.72 | -6.22 | -38.89 | 1248 |
| 55 | Triple EMA stack · 1h | trend | 92.43 | -7.57 | 34 | 5.9 | -7.88 | -0.77 | -22.08 | 235 |
| 56 | Keltner breakout · 1h | breakout | 91.87 | -8.13 | 14 | 0.0 | -7.61 | -0.86 | -19.97 | 219 |
| 57 | MACD zero-line · 1h | trend | 91.82 | -8.18 | 24 | 4.2 | -8.24 | -0.97 | -16.46 | 232 |
| 58 | EMA 9/21 cross · 1h | trend | 91.79 | -8.21 | 46 | 10.9 | -7.81 | -0.89 | -16.92 | 320 |
| 59 | Heikin-Ashi · 1h | trend | 91.31 | -8.69 | 59 | 8.5 | -28.04 | -4.54 | -31.39 | 683 |
| 60 | RSI(14) reversion | reversion | 91.22 | -8.78 | 128 | 35.9 | -70.92 | -20.99 | -71.13 | 1473 |
| 61 | Donchian 20/10 · 1h | breakout | 91.18 | -8.82 | 21 | 9.5 | -1.08 | 0.08 | -13.81 | 222 |
| 62 | OBV trend · 1h | momentum | 89.81 | -10.19 | 66 | 6.1 | -14.58 | -1.70 | -25.03 | 332 |
| 63 | Squeeze breakout | breakout | 87.48 | -12.52 | 108 | 13.0 | -59.56 | -18.45 | -59.62 | 1180 |
| 64 | ROC + volume · 1h | momentum | 87.40 | -12.60 | 59 | 5.1 | -14.23 | -1.91 | -21.75 | 412 |
| 65 | Donchian 55/20 | breakout | 85.91 | -14.09 | 118 | 18.6 | -67.50 | -15.38 | -67.52 | 1293 |
| 66 | Volume breakout | breakout | 85.07 | -14.93 | 114 | 14.9 | -62.96 | -20.25 | -62.96 | 889 |
| 67 | ROC + volume | momentum | 84.47 | -15.53 | 181 | 19.9 | -72.89 | -17.88 | -72.89 | 1641 |
| 68 | Keltner breakout | breakout | 83.40 | -16.60 | 172 | 14.5 | -84.76 | -34.67 | -84.77 | 1890 |
| 69 | Z-score reversion | reversion | 83.38 | -16.62 | 200 | 32.0 | -84.97 | -27.96 | -85.01 | 2100 |
| 70 | VWAP reversion | reversion | 83.32 | -16.68 | 154 | 24.7 | -71.86 | -17.81 | -71.98 | 1406 |
| 71 | Ichimoku | trend | 83.25 | -16.75 | 135 | 9.6 | -80.24 | -25.48 | -80.25 | 1742 |
| 72 | EMA 20/50 cross | trend | 82.99 | -17.01 | 145 | 14.5 | -78.89 | -17.46 | -78.93 | 1475 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 79.95 | -20.05 | 199 | 18.1 | -87.37 | -24.43 | -87.48 | 1960 |
| 76 | MFI reversion | reversion | 79.32 | -20.68 | 199 | 19.6 | -88.18 | -35.54 | -88.18 | 2146 |
| 77 | Donchian 20/10 | breakout | 79.26 | -20.74 | 242 | 19.0 | -90.64 | -29.11 | -90.66 | 2662 |
| 78 | MACD zero-line | trend | 79.19 | -20.81 | 236 | 16.1 | -91.67 | -35.30 | -91.68 | 2354 |
| 79 | Trend pullback | trend | 78.44 | -21.56 | 201 | 17.4 | -90.73 | -33.03 | -90.73 | 2267 |
| 80 | RSI momentum | momentum | 77.59 | -22.41 | 233 | 14.6 | -90.30 | -28.82 | -90.31 | 2385 |
| 81 | Triple EMA stack | trend | 77.59 | -22.41 | 246 | 16.3 | -92.88 | -35.13 | -92.89 | 2590 |
| 82 | Bollinger breakout | breakout | 77.44 | -22.56 | 245 | 15.9 | -93.84 | -42.17 | -93.85 | 2847 |
| 83 | ADX DI cross | trend | 76.33 | -23.66 | 233 | 8.2 | -89.41 | -44.64 | -89.42 | 2118 |
| 84 | Stochastic reversion | reversion | 74.04 | -25.96 | 370 | 24.6 | -95.96 | -45.25 | -95.96 | 4066 |
| 85 | Consensus | meta | 73.70 | -26.30 | 220 | 6.8 | -94.49 | -30.12 | -94.50 | 2641 |
| 86 | EMA 9/21 cross | trend | 73.63 | -26.37 | 323 | 17.0 | -97.39 | -40.79 | -97.40 | 3530 |
| 87 | Connors RSI(2) | reversion | 72.98 | -27.02 | 310 | 19.0 | -96.45 | -40.68 | -96.45 | 3640 |
| 88 | Bollinger reversion | reversion | 72.41 | -27.59 | 349 | 16.9 | -95.84 | -44.05 | -95.84 | 3697 |
| 89 | Candlestick reversal | reversion | 72.21 | -27.79 | 348 | 14.7 | -99.36 | -49.29 | -99.36 | 5624 |
| 90 | OBV trend | momentum | 70.66 | -29.34 | 340 | 15.9 | -95.90 | -46.29 | -95.91 | 3539 |
| 91 | CCI reversion | reversion | 70.45 | -29.55 | 294 | 13.3 | -98.47 | -49.46 | -98.47 | 4700 |
| 92 | Parabolic SAR | trend | 69.99 | -30.01 | 314 | 13.4 | -96.92 | -53.24 | -96.93 | 3615 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.54 | -35.80 | -98.54 | 5219 |
| 94 | MACD cross | trend | 67.96 | -32.04 | 340 | 14.4 | -99.71 | -62.89 | -99.71 | 6063 |
| 95 | Williams %R | reversion | 67.44 | -32.56 | 419 | 22.0 | -99.53 | -57.31 | -99.53 | 6108 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -75.24 | -99.89 | 8274 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T18:40 | Consensus | buy | SOXL | 18.43 | — | entry |
| 2026-09-30T18:40 | Donchian 55/20 · 1h | buy | QQQ | 4.57 | — | rebalance up |
| 2026-09-30T18:40 | Williams %R | buy | TNA | 3.48 | — | rebalance up |
| 2026-09-30T18:40 | Williams %R | buy | COIN | 4.48 | — | rebalance up |
| 2026-09-30T18:40 | Williams %R | sell | ETHU | 3.53 | -0.04 | stop-loss |
| 2026-09-30T18:40 | Williams %R | sell | ETH-USD | 3.53 | -0.04 | stop-loss |
| 2026-09-30T18:40 | Williams %R | sell | DOGE-USD | 4.45 | -0.06 | stop-loss |
| 2026-09-30T18:40 | Stochastic reversion | buy | GOOGL | 4.94 | — | entry signal |
| 2026-09-30T18:40 | Bollinger reversion | buy | ETHU | 3.98 | — | rebalance up |
| 2026-09-30T18:40 | Bollinger reversion | sell | XRP-USD | 2.81 | -0.03 | stop-loss |
| 2026-09-30T18:40 | Bollinger reversion | sell | SOL-USD | 5.13 | -0.06 | stop-loss |
| 2026-09-30T18:40 | Connors RSI(2) | buy | MSFT | 15.83 | — | rebalance up |
| 2026-09-30T18:40 | Connors RSI(2) | buy | BTC-USD | 3.66 | — | rebalance up |
| 2026-09-30T18:40 | Connors RSI(2) | buy | BITX | 3.66 | — | rebalance up |
| 2026-09-30T18:40 | Connors RSI(2) | sell | UPRO | 14.61 | -0.03 | exit signal |
| 2026-09-30T18:40 | Connors RSI(2) | sell | SPY | 14.62 | -0.02 | exit signal |
| 2026-09-30T18:40 | Connors RSI(2) | sell | META | 12.17 | 0.00 | exit signal |
| 2026-09-30T18:40 | Candlestick reversal | buy | MSTR | 8.03 | — | entry signal |
| 2026-09-30T18:40 | Candlestick reversal | sell | XRP-USD | 5.52 | -0.06 | stop-loss |
| 2026-09-30T18:40 | OBV trend | buy | AAPL | 7.85 | — | entry signal |
| 2026-09-30T18:40 | Trend pullback | buy | AAPL | 7.86 | — | entry signal |
| 2026-09-30T18:40 | Trend pullback | sell | TECL | 3.93 | 0.00 | rebalance down |
| 2026-09-30T18:40 | Trend pullback | sell | MSFT | 3.93 | -0.00 | rebalance down |
| 2026-09-30T18:40 | Triple EMA stack | buy | TSLA | 4.33 | — | rebalance up |
| 2026-09-30T18:40 | Triple EMA stack | buy | TECL | 4.28 | — | rebalance up |
| 2026-09-30T18:40 | Triple EMA stack | buy | SOXL | 4.32 | — | rebalance up |
| 2026-09-30T18:40 | Triple EMA stack | buy | NVDA | 4.32 | — | rebalance up |
| 2026-09-30T18:40 | Triple EMA stack | buy | LABU | 4.29 | — | rebalance up |
| 2026-09-30T18:40 | Triple EMA stack | buy | AMD | 4.29 | — | rebalance up |
| 2026-09-30T18:40 | Triple EMA stack | sell | MSFT | 8.61 | -0.03 | exit signal |
| 2026-09-30T18:40 | EMA 9/21 cross | sell | MSFT | 9.20 | -0.03 | exit signal |
| 2026-09-30T18:35 | Consensus | buy | TECL | 14.70 | — | rebalance up |
| 2026-09-30T18:35 | Consensus | sell | TSLA | 18.33 | -0.07 | target is flat |
| 2026-09-30T18:35 | Consensus | sell | SOXL | 18.38 | -0.06 | target is flat |
| 2026-09-30T18:35 | Consensus | sell | GOOGL | 14.72 | -0.06 | target is flat |
| 2026-09-30T18:35 | Agent | sell | TQQQ | 19.86 | -0.00 | selected signal exited |
| 2026-09-30T18:35 | MFI reversion | buy | XRP-USD | 5.19 | — | rebalance up |
| 2026-09-30T18:35 | MFI reversion | buy | TNA | 4.52 | — | rebalance up |
| 2026-09-30T18:35 | MFI reversion | buy | PLTR | 4.51 | — | rebalance up |
| 2026-09-30T18:35 | MFI reversion | buy | DOGE-USD | 4.53 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
