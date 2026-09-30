# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T14:10:05.000127+00:00 · 6960 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.65 (-0.35%)

Closed trades 25, win rate 68.0%, fees £0.72, max drawdown -1.39%.

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

Today: 13581 decisions in 2172 calls, $0.1824 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T14:10 | 3 / 21 / 6 | AAPL 14% |  |
| Breezy | 2026-09-30T14:10 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-09-30T14:10 | 4 / 23 / 3 | BITX 37%, MSTR 32% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.81 | 1.81 | 2 | 50.0 | 15.07 | 3.23 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 3 | Hold BTC | benchmark | 100.46 | 0.46 | 0 | — | 30.06 | 3.76 | -8.68 | 1 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.32 | 0.32 | 1 | 100.0 | 0.18 | 0.14 | -9.74 | 24 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.06 | 0.06 | 0 | — | 6.12 | 1.72 | -7.93 | 7 |
| 6 | Daily: Bullish score | daily | 100.05 | 0.05 | 3 | 0.0 | 0.81 | 0.31 | -12.76 | 14 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.05 | 0.05 | 0 | — | 7.26 | 2.96 | -3.62 | 1 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 99.73 | -0.27 | 0 | — | -2.68 | -1.57 | -5.09 | 2 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.72 | -0.28 | 7 | 42.9 | 3.35 | 1.70 | -1.76 | 83 |
| 12 | Agent | meta | 99.65 | -0.35 | 25 | 68.0 | -9.82 | -6.50 | -10.68 | 215 |
| 13 | Timing: Nasdaq FTD · TQQQ | daily | 99.64 | -0.36 | 0 | — | -9.02 | -1.75 | -15.27 | 2 |
| 14 | Hold SPY | benchmark | 99.59 | -0.41 | 0 | — | 4.53 | 2.44 | -3.66 | 1 |
| 15 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 8 | 62.5 | 7.91 | 1.91 | -6.57 | 128 |
| 16 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -0.41 | -0.21 | -3.92 | 97 |
| 17 | VWAP reversion · 1h | reversion | 99.47 | -0.53 | 21 | 23.8 | -12.65 | -4.27 | -14.72 | 122 |
| 18 | Stochastic reversion · 1h | reversion | 99.24 | -0.76 | 26 | 53.8 | -11.50 | -2.53 | -13.45 | 327 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 20 | Williams %R · 1h | reversion | 99.01 | -0.99 | 44 | 43.2 | -11.59 | -1.73 | -19.41 | 489 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.96 | -1.04 | 0 | — | -5.65 | -1.21 | -10.06 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.95 | -1.05 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.82 | -1.18 | 1 | 0.0 | -0.33 | -0.06 | -4.88 | 17 |
| 24 | Copy: Warren Buffett (BRK-B) | copy | 98.77 | -1.23 | 0 | — | -0.42 | -0.10 | -7.65 | 1 |
| 25 | CCI reversion · 1h | reversion | 98.72 | -1.28 | 36 | 33.3 | 2.36 | 0.56 | -12.41 | 409 |
| 26 | Copy: Insider buying | copy | 98.69 | -1.31 | 2 | 100.0 | -14.11 | -2.77 | -17.74 | 73 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.58 | -1.42 | 0 | — | 24.66 | 3.61 | -6.29 | 1 |
| 28 | Gap and go | momentum | 98.49 | -1.51 | 10 | 10.0 | 15.60 | 3.85 | -4.73 | 183 |
| 29 | Candlestick reversal · 1h | reversion | 98.48 | -1.52 | 30 | 26.7 | -25.42 | -6.11 | -26.71 | 498 |
| 30 | Z-score reversion · 1h | reversion | 98.39 | -1.61 | 11 | 45.5 | 4.99 | 1.19 | -8.60 | 153 |
| 31 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.09 | 0.20 | -15.21 | 46 |
| 32 | Agent (rotation) | meta | 98.13 | -1.87 | 33 | 12.1 | -5.66 | -2.04 | -10.62 | 213 |
| 33 | EMA 20/50 cross · 1h | trend | 98.02 | -1.99 | 14 | 7.1 | 16.96 | 2.10 | -12.18 | 129 |
| 34 | Connors RSI(2) · 1h | reversion | 97.78 | -2.22 | 46 | 45.7 | -11.15 | -3.53 | -11.76 | 232 |
| 35 | Bollinger reversion · 1h | reversion | 97.60 | -2.40 | 26 | 30.8 | -16.79 | -4.61 | -18.20 | 312 |
| 36 | Opening range 30m | breakout | 97.14 | -2.86 | 37 | 13.5 | -9.80 | -2.84 | -14.21 | 557 |
| 37 | Max aggression: 5-day momentum | meta | 97.02 | -2.98 | 3 | 66.7 | -11.87 | -0.79 | -29.56 | 29 |
| 38 | Supertrend · 1h | trend | 96.69 | -3.31 | 18 | 5.6 | 3.24 | 0.63 | -16.43 | 196 |
| 39 | Trend pullback · 1h | trend | 96.58 | -3.42 | 28 | 10.7 | -24.72 | -6.50 | -25.81 | 146 |
| 40 | Agent (ML meta-label) | meta | 96.39 | -3.61 | 149 | 12.8 | 0.14 | 0.18 | -14.51 | 403 |
| 41 | Donchian 55/20 · 1h | breakout | 96.17 | -3.83 | 13 | 0.0 | 4.58 | 0.80 | -16.96 | 115 |
| 42 | Opening range 15m | breakout | 96.10 | -3.90 | 48 | 12.5 | -11.34 | -3.08 | -16.70 | 687 |
| 43 | Squeeze breakout · 1h | breakout | 95.86 | -4.14 | 12 | 8.3 | 11.91 | 2.09 | -7.74 | 102 |
| 44 | MFI reversion · 1h | reversion | 95.80 | -4.20 | 47 | 14.9 | -8.85 | -1.58 | -17.20 | 129 |
| 45 | Max aggression: 1-day momentum | meta | 95.64 | -4.36 | 3 | 33.3 | -20.17 | -0.93 | -41.28 | 42 |
| 46 | MACD cross · 1h | trend | 95.63 | -4.38 | 40 | 10.0 | -13.18 | -2.06 | -17.52 | 463 |
| 47 | Parabolic SAR · 1h | trend | 95.62 | -4.38 | 26 | 11.5 | -7.94 | -0.99 | -19.53 | 293 |
| 48 | Ichimoku · 1h | trend | 94.57 | -5.42 | 18 | 16.7 | 6.40 | 0.94 | -15.13 | 122 |
| 49 | Three white soldiers | momentum | 94.51 | -5.49 | 46 | 17.4 | -50.23 | -27.73 | -50.27 | 608 |
| 50 | RSI momentum · 1h | momentum | 94.31 | -5.69 | 25 | 4.0 | -1.75 | -0.04 | -15.29 | 218 |
| 51 | ADX DI cross · 1h | trend | 94.28 | -5.71 | 31 | 6.5 | -15.18 | -2.83 | -17.52 | 252 |
| 52 | Volume breakout · 1h | breakout | 94.28 | -5.72 | 28 | 3.6 | 5.23 | 0.91 | -12.60 | 126 |
| 53 | Bollinger breakout · 1h | breakout | 94.09 | -5.91 | 21 | 9.5 | 7.41 | 1.15 | -10.16 | 287 |
| 54 | VWAP momentum · 1h | momentum | 93.92 | -6.08 | 105 | 13.3 | -33.52 | -5.00 | -35.31 | 1241 |
| 55 | Triple EMA stack · 1h | trend | 93.42 | -6.58 | 30 | 6.7 | -6.77 | -0.63 | -22.10 | 231 |
| 56 | MACD zero-line · 1h | trend | 93.26 | -6.74 | 22 | 4.5 | -6.26 | -0.69 | -14.79 | 228 |
| 57 | Donchian 20/10 · 1h | breakout | 92.69 | -7.31 | 18 | 11.1 | 4.25 | 0.75 | -12.78 | 218 |
| 58 | Keltner breakout · 1h | breakout | 92.52 | -7.48 | 12 | 0.0 | -7.00 | -0.76 | -19.20 | 221 |
| 59 | EMA 9/21 cross · 1h | trend | 92.36 | -7.64 | 45 | 11.1 | -6.14 | -0.65 | -16.92 | 318 |
| 60 | Heikin-Ashi · 1h | trend | 92.15 | -7.85 | 45 | 11.1 | -25.64 | -3.87 | -30.83 | 674 |
| 61 | OBV trend · 1h | momentum | 91.62 | -8.38 | 58 | 6.9 | -14.44 | -1.68 | -25.03 | 326 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -70.89 | -20.94 | -71.11 | 1475 |
| 63 | ROC + volume · 1h | momentum | 88.22 | -11.78 | 54 | 5.6 | -11.34 | -1.45 | -20.45 | 410 |
| 64 | Squeeze breakout | breakout | 87.79 | -12.21 | 102 | 13.7 | -59.92 | -18.68 | -59.94 | 1195 |
| 65 | Donchian 55/20 | breakout | 86.51 | -13.49 | 101 | 14.9 | -67.46 | -15.36 | -67.82 | 1308 |
| 66 | ROC + volume | momentum | 85.49 | -14.52 | 161 | 18.0 | -72.87 | -17.80 | -73.03 | 1657 |
| 67 | Volume breakout | breakout | 85.28 | -14.72 | 113 | 15.0 | -62.30 | -19.91 | -62.61 | 899 |
| 68 | EMA 20/50 cross | trend | 84.80 | -15.20 | 136 | 14.7 | -78.71 | -17.52 | -78.94 | 1481 |
| 69 | Keltner breakout | breakout | 84.07 | -15.93 | 160 | 13.8 | -84.60 | -34.48 | -84.62 | 1893 |
| 70 | VWAP reversion | reversion | 83.73 | -16.27 | 147 | 23.1 | -71.87 | -17.78 | -71.97 | 1399 |
| 71 | Z-score reversion | reversion | 83.53 | -16.47 | 193 | 30.6 | -84.61 | -27.53 | -84.62 | 2105 |
| 72 | Ichimoku | trend | 83.25 | -16.75 | 127 | 8.7 | -80.55 | -26.12 | -80.56 | 1745 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 80.11 | -19.89 | 196 | 17.9 | -87.42 | -24.56 | -87.56 | 1958 |
| 76 | MFI reversion | reversion | 80.06 | -19.94 | 190 | 18.9 | -88.08 | -35.18 | -88.09 | 2143 |
| 77 | Donchian 20/10 | breakout | 79.89 | -20.11 | 219 | 17.8 | -90.61 | -29.06 | -90.68 | 2678 |
| 78 | MACD zero-line | trend | 79.54 | -20.46 | 221 | 14.9 | -91.82 | -35.88 | -91.86 | 2360 |
| 79 | Trend pullback | trend | 78.69 | -21.31 | 181 | 18.8 | -90.59 | -33.17 | -90.64 | 2262 |
| 80 | Triple EMA stack | trend | 78.57 | -21.43 | 231 | 16.5 | -92.93 | -35.39 | -93.02 | 2608 |
| 81 | Bollinger breakout | breakout | 78.36 | -21.64 | 226 | 15.9 | -93.81 | -42.24 | -93.85 | 2868 |
| 82 | RSI momentum | momentum | 77.74 | -22.26 | 215 | 14.0 | -90.39 | -28.95 | -90.49 | 2391 |
| 83 | ADX DI cross | trend | 76.93 | -23.07 | 213 | 7.5 | -89.47 | -45.38 | -89.47 | 2099 |
| 84 | Connors RSI(2) | reversion | 75.72 | -24.28 | 252 | 16.3 | -96.32 | -39.60 | -96.32 | 3603 |
| 85 | Consensus | meta | 75.31 | -24.69 | 199 | 7.0 | -94.64 | -30.03 | -94.65 | 2645 |
| 86 | Stochastic reversion | reversion | 74.61 | -25.39 | 344 | 23.3 | -95.90 | -44.32 | -95.94 | 4049 |
| 87 | EMA 9/21 cross | trend | 74.28 | -25.72 | 305 | 16.7 | -97.40 | -40.99 | -97.44 | 3547 |
| 88 | Candlestick reversal | reversion | 73.65 | -26.35 | 298 | 12.4 | -99.35 | -48.73 | -99.35 | 5592 |
| 89 | Bollinger reversion | reversion | 73.14 | -26.86 | 323 | 14.9 | -95.79 | -43.37 | -95.80 | 3680 |
| 90 | OBV trend | momentum | 71.28 | -28.73 | 301 | 14.6 | -95.96 | -48.18 | -95.97 | 3555 |
| 91 | CCI reversion | reversion | 70.78 | -29.22 | 267 | 10.9 | -98.46 | -49.35 | -98.46 | 4683 |
| 92 | Parabolic SAR | trend | 70.04 | -29.96 | 295 | 12.5 | -96.99 | -55.21 | -97.00 | 3625 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.53 | -36.10 | -98.55 | 5270 |
| 94 | MACD cross | trend | 68.42 | -31.58 | 309 | 13.6 | -99.72 | -64.48 | -99.72 | 6090 |
| 95 | Williams %R | reversion | 68.25 | -31.75 | 376 | 19.9 | -99.52 | -56.40 | -99.52 | 6110 |
| 96 | Heikin-Ashi | trend | 67.52 | -32.48 | 275 | 3.6 | -99.89 | -76.68 | -99.89 | 8297 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T14:10 | Stochastic reversion | buy | SQQQ | 18.62 | — | entry signal |
| 2026-09-30T14:10 | VWAP reversion | buy | SQQQ | 20.94 | — | entry signal |
| 2026-09-30T14:10 | VWAP reversion | sell | TNA | 21.07 | 0.09 | exit signal |
| 2026-09-30T14:10 | VWAP reversion | sell | IWM | 20.99 | 0.02 | exit signal |
| 2026-09-30T14:10 | Three white soldiers | buy | AMZN | 23.63 | — | entry signal |
| 2026-09-30T14:10 | Three white soldiers | buy | AAPL | 23.63 | — | entry signal |
| 2026-09-30T14:10 | Candlestick reversal | buy | SQQQ | 7.51 | — | entry signal |
| 2026-09-30T14:10 | Candlestick reversal | sell | TSLA | 3.79 | 0.01 | rebalance down |
| 2026-09-30T14:10 | Candlestick reversal | sell | DOGE-USD | 3.69 | -0.02 | rebalance down |
| 2026-09-30T14:10 | RSI momentum | buy | LABU | 4.03 | — | entry signal |
| 2026-09-30T14:10 | RSI momentum | sell | AMZN | 4.03 | 0.03 | rebalance down |
| 2026-09-30T14:10 | Trend pullback | sell | SOXL | 19.53 | -0.22 | exit signal |
| 2026-09-30T14:10 | Heikin-Ashi | sell | NVDA | 5.58 | -0.02 | exit signal |
| 2026-09-30T14:10 | Triple EMA stack | sell | SOL-USD | 19.58 | 0.02 | exit signal |
| 2026-09-30T14:10 | EMA 9/21 cross | sell | BTC-USD | 18.42 | -0.08 | exit signal |
| 2026-09-30T14:05 | Agent (ML meta-label) | buy | TSLA | 2.48 | — | entry |
| 2026-09-30T14:05 | Agent (ML meta-label) | sell | BTC-USD | 2.48 | -0.02 | selected signal exited |
| 2026-09-30T14:05 | Bollinger reversion · 1h | sell | AAPL | 9.06 | 0.16 | take-profit |
| 2026-09-30T14:05 | RSI(14) reversion · 1h | sell | AAPL | 25.11 | 0.30 | take-profit |
| 2026-09-30T14:05 | CCI reversion | buy | TSLA | 17.70 | — | entry signal |
| 2026-09-30T14:05 | Williams %R | buy | TSLA | 2.43 | — | entry signal |
| 2026-09-30T14:05 | Williams %R | buy | SOXL | 7.26 | — | rebalance up |
| 2026-09-30T14:05 | Williams %R | sell | SQQQ | 9.70 | -0.10 | stop-loss |
| 2026-09-30T14:05 | Stochastic reversion | sell | SQQQ | 18.53 | -0.19 | stop-loss |
| 2026-09-30T14:05 | VWAP reversion | buy | MSTR | 20.97 | — | entry signal |
| 2026-09-30T14:05 | Z-score reversion | buy | TSLA | 20.89 | — | entry signal |
| 2026-09-30T14:05 | RSI(14) reversion | buy | TSLA | 22.70 | — | entry signal |
| 2026-09-30T14:05 | Candlestick reversal | buy | SOXL | 10.97 | — | rebalance up |
| 2026-09-30T14:05 | Candlestick reversal | buy | DOGE-USD | 3.70 | — | rebalance up |
| 2026-09-30T14:05 | Candlestick reversal | sell | META | 14.71 | -0.02 | exit signal |
| 2026-09-30T14:05 | Bollinger breakout | buy | GOOGL | 10.62 | — | entry signal |
| 2026-09-30T14:05 | Bollinger breakout | buy | AMZN | 11.19 | — | entry signal |
| 2026-09-30T14:05 | Bollinger breakout | sell | QQQ | 4.43 | -0.00 | rebalance down |
| 2026-09-30T14:05 | Bollinger breakout | sell | PLTR | 4.42 | 0.00 | rebalance down |
| 2026-09-30T14:05 | Bollinger breakout | sell | MSFT | 8.41 | 0.04 | rebalance down |
| 2026-09-30T14:05 | Bollinger breakout | sell | AAPL | 4.54 | 0.07 | rebalance down |
| 2026-09-30T14:05 | Opening range 30m | buy | UPRO | 10.80 | — | entry signal |
| 2026-09-30T14:05 | Opening range 30m | buy | TQQQ | 10.80 | — | entry signal |
| 2026-09-30T14:05 | Opening range 30m | buy | TECL | 10.80 | — | entry signal |
| 2026-09-30T14:05 | Opening range 30m | buy | SPY | 10.80 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
