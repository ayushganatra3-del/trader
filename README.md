# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-01T11:10:05.000153+00:00 · 7664 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.63 (-0.37%)

Closed trades 27, win rate 66.7%, fees £0.80, max drawdown -1.39%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-01 | KOD 12%, ADRX 12%, ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, BBD 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-30)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.46 · VIX 16.34 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, META 7.4, MSFT 7.2, AMD 7.2, ETHU 7.0, BITX 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 3770 decisions in 754 calls, $0.0530 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-01T11:10 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-10-01T11:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-01T11:10 | 0 / 5 / 0 | ETH-USD 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| Williams %R | TQQQ | 2.51 | +2.91% | 16 |
| Z-score reversion | MSFT | 2.34 | +2.58% | 5 |
| Stochastic reversion | MSFT | 1.97 | +2.78% | 13 |
| Connors RSI(2) · 1h | TECL | 1.95 | +5.24% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.70 | 0.70 | 3 | 33.3 | 13.60 | 2.92 | -7.55 | 43 |
| 2 | Hold BTC | benchmark | 100.53 | 0.53 | 0 | — | 31.32 | 3.90 | -8.68 | 1 |
| 3 | Copy: Congress Democrats (NANC) | copy | 100.33 | 0.33 | 0 | — | 5.20 | 2.18 | -3.62 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 99.84 | -0.16 | 0 | — | -3.22 | -1.93 | -5.09 | 2 |
| 7 | Copy: Hedge-fund gurus (GURU) | copy | 99.66 | -0.34 | 0 | — | -2.55 | -1.21 | -5.14 | 1 |
| 8 | RSI(14) reversion · 1h | reversion | 99.63 | -0.37 | 8 | 62.5 | 4.53 | 1.27 | -7.26 | 132 |
| 9 | Agent | meta | 99.63 | -0.37 | 27 | 66.7 | -10.23 | -6.78 | -10.80 | 224 |
| 10 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -10.76 | -3.66 | -14.05 | 114 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.65 | 1.34 | -2.11 | 83 |
| 12 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -1.50 | -0.81 | -4.46 | 99 |
| 13 | Hold SPY | benchmark | 99.46 | -0.54 | 0 | — | 2.91 | 1.62 | -3.66 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 15 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 2 | 50.0 | -1.10 | -0.29 | -9.74 | 24 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.38 | -5.16 | 27 |
| 17 | Stochastic reversion · 1h | reversion | 99.12 | -0.88 | 30 | 56.7 | -9.47 | -2.08 | -10.86 | 322 |
| 18 | Copy: Warren Buffett (BRK-B) | copy | 99.09 | -0.91 | 0 | — | -2.22 | -0.86 | -7.65 | 1 |
| 19 | Daily: Bullish score | daily | 98.95 | -1.05 | 3 | 0.0 | -1.05 | 0.05 | -12.76 | 14 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 98.72 | -1.28 | 0 | — | -10.46 | -2.10 | -15.27 | 2 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.72 | -1.28 | 0 | — | 2.47 | 0.76 | -7.93 | 7 |
| 22 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 15.10 | 3.71 | -4.73 | 182 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 24 | Copy: Insider buying | copy | 98.64 | -1.36 | 2 | 100.0 | -14.74 | -2.89 | -17.74 | 73 |
| 25 | CCI reversion · 1h | reversion | 98.56 | -1.44 | 42 | 40.5 | 1.95 | 0.49 | -12.41 | 413 |
| 26 | Williams %R · 1h | reversion | 98.56 | -1.44 | 52 | 50.0 | -16.69 | -3.09 | -19.41 | 490 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.54 | 0.27 | -15.21 | 46 |
| 28 | Candlestick reversal · 1h | reversion | 98.34 | -1.67 | 33 | 24.2 | -25.36 | -6.28 | -26.74 | 491 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 98.21 | -1.79 | 0 | — | 26.25 | 3.82 | -6.29 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.58 | -3.31 | -11.47 | 232 |
| 31 | Z-score reversion · 1h | reversion | 98.07 | -1.93 | 11 | 45.5 | 3.25 | 0.82 | -8.60 | 153 |
| 32 | Daily: SMA 20/50 cross · AAPL | daily | 97.83 | -2.17 | 0 | — | -7.64 | -1.77 | -10.03 | 1 |
| 33 | Agent (rotation) | meta | 97.76 | -2.24 | 37 | 13.5 | -5.20 | -1.78 | -9.79 | 211 |
| 34 | Bollinger reversion · 1h | reversion | 97.41 | -2.59 | 32 | 34.4 | -16.74 | -4.64 | -17.77 | 305 |
| 35 | EMA 20/50 cross · 1h | trend | 96.69 | -3.31 | 20 | 5.0 | 15.99 | 1.99 | -12.18 | 130 |
| 36 | Supertrend · 1h | trend | 96.41 | -3.59 | 19 | 5.3 | 0.82 | 0.31 | -16.43 | 203 |
| 37 | Opening range 30m | breakout | 96.12 | -3.88 | 49 | 12.2 | -11.24 | -3.24 | -15.06 | 559 |
| 38 | Agent (ML meta-label) | meta | 95.85 | -4.15 | 173 | 12.7 | 6.69 | 1.27 | -13.14 | 404 |
| 39 | Max aggression: 5-day momentum | meta | 95.81 | -4.19 | 3 | 66.7 | -13.55 | -0.95 | -29.56 | 29 |
| 40 | Donchian 55/20 · 1h | breakout | 95.79 | -4.21 | 15 | 0.0 | 4.59 | 0.79 | -16.96 | 113 |
| 41 | Trend pullback · 1h | trend | 95.68 | -4.32 | 35 | 11.4 | -26.42 | -7.04 | -26.63 | 160 |
| 42 | MFI reversion · 1h | reversion | 94.98 | -5.02 | 52 | 19.2 | -8.76 | -1.56 | -17.05 | 128 |
| 43 | Opening range 15m | breakout | 94.87 | -5.13 | 61 | 14.8 | -12.31 | -3.35 | -17.03 | 686 |
| 44 | Parabolic SAR · 1h | trend | 94.59 | -5.41 | 33 | 12.1 | -10.25 | -1.33 | -19.53 | 306 |
| 45 | Squeeze breakout · 1h | breakout | 94.49 | -5.51 | 16 | 6.2 | 12.09 | 2.12 | -7.61 | 98 |
| 46 | MACD cross · 1h | trend | 94.45 | -5.55 | 48 | 10.4 | -15.11 | -2.40 | -17.47 | 483 |
| 47 | Max aggression: 1-day momentum | meta | 94.45 | -5.55 | 3 | 33.3 | -21.69 | -1.04 | -41.28 | 42 |
| 48 | Three white soldiers | momentum | 94.16 | -5.84 | 52 | 19.2 | -50.18 | -27.47 | -50.18 | 605 |
| 49 | ADX DI cross · 1h | trend | 94.14 | -5.86 | 35 | 5.7 | -15.94 | -2.98 | -17.43 | 260 |
| 50 | Volume breakout · 1h | breakout | 93.79 | -6.21 | 29 | 3.4 | 5.32 | 0.93 | -12.60 | 122 |
| 51 | Ichimoku · 1h | trend | 93.22 | -6.78 | 21 | 14.3 | 4.48 | 0.73 | -15.66 | 121 |
| 52 | RSI momentum · 1h | momentum | 92.81 | -7.19 | 30 | 3.3 | -3.44 | -0.27 | -16.26 | 220 |
| 53 | VWAP momentum · 1h | momentum | 92.64 | -7.36 | 127 | 15.7 | -39.37 | -6.30 | -39.37 | 1257 |
| 54 | Bollinger breakout · 1h | breakout | 92.29 | -7.71 | 25 | 8.0 | 5.06 | 0.85 | -10.56 | 280 |
| 55 | Triple EMA stack · 1h | trend | 91.64 | -8.36 | 41 | 7.3 | -9.71 | -0.99 | -22.71 | 239 |
| 56 | EMA 9/21 cross · 1h | trend | 91.32 | -8.68 | 53 | 9.4 | -8.71 | -1.00 | -17.94 | 324 |
| 57 | MACD zero-line · 1h | trend | 91.20 | -8.80 | 29 | 6.9 | -9.01 | -1.06 | -17.53 | 232 |
| 58 | Heikin-Ashi · 1h | trend | 91.02 | -8.98 | 59 | 8.5 | -29.88 | -4.90 | -32.92 | 688 |
| 59 | Keltner breakout · 1h | breakout | 90.92 | -9.07 | 15 | 0.0 | -8.80 | -1.02 | -20.71 | 218 |
| 60 | Donchian 20/10 · 1h | breakout | 90.13 | -9.87 | 23 | 8.7 | -1.39 | 0.04 | -14.99 | 218 |
| 61 | RSI(14) reversion | reversion | 90.06 | -9.94 | 143 | 34.3 | -71.76 | -21.52 | -71.85 | 1476 |
| 62 | OBV trend · 1h | momentum | 89.31 | -10.69 | 70 | 5.7 | -15.10 | -1.73 | -25.58 | 329 |
| 63 | ROC + volume · 1h | momentum | 86.56 | -13.44 | 62 | 4.8 | -15.08 | -2.01 | -22.31 | 412 |
| 64 | Squeeze breakout | breakout | 86.37 | -13.63 | 115 | 13.0 | -59.40 | -17.96 | -59.50 | 1183 |
| 65 | Donchian 55/20 | breakout | 85.41 | -14.59 | 123 | 19.5 | -67.28 | -15.05 | -67.32 | 1295 |
| 66 | Volume breakout | breakout | 84.58 | -15.42 | 118 | 15.3 | -62.78 | -19.92 | -62.81 | 900 |
| 67 | ROC + volume | momentum | 83.43 | -16.57 | 186 | 19.9 | -72.29 | -17.43 | -72.57 | 1641 |
| 68 | VWAP reversion | reversion | 83.15 | -16.85 | 163 | 25.8 | -71.18 | -17.38 | -71.33 | 1385 |
| 69 | Keltner breakout | breakout | 82.67 | -17.33 | 176 | 14.8 | -84.32 | -32.47 | -84.32 | 1882 |
| 70 | Z-score reversion | reversion | 82.08 | -17.92 | 221 | 30.8 | -84.82 | -27.26 | -84.89 | 2092 |
| 71 | EMA 20/50 cross | trend | 81.92 | -18.08 | 155 | 15.5 | -79.26 | -17.43 | -79.26 | 1473 |
| 72 | AI bee: Bizzy | ai | 81.81 | -18.19 | 300 | 9.0 | — | — | — | — |
| 73 | AI bee: Boozy | ai | 81.67 | -18.33 | 109 | 0.9 | — | — | — | — |
| 74 | Ichimoku | trend | 81.26 | -18.74 | 145 | 9.7 | -80.53 | -25.30 | -80.59 | 1753 |
| 75 | MFI reversion | reversion | 78.60 | -21.40 | 210 | 19.5 | -88.03 | -33.82 | -88.10 | 2132 |
| 76 | Trend pullback | trend | 77.79 | -22.21 | 213 | 16.9 | -91.02 | -32.90 | -91.02 | 2281 |
| 77 | Supertrend | trend | 77.70 | -22.30 | 213 | 18.3 | -87.34 | -24.02 | -87.34 | 1942 |
| 78 | MACD zero-line | trend | 76.28 | -23.72 | 258 | 15.5 | -91.52 | -33.03 | -91.58 | 2351 |
| 79 | Triple EMA stack | trend | 76.03 | -23.97 | 263 | 16.0 | -92.90 | -33.88 | -92.90 | 2596 |
| 80 | Donchian 20/10 | breakout | 76.00 | -24.00 | 261 | 18.4 | -90.62 | -28.10 | -90.64 | 2667 |
| 81 | Bollinger breakout | breakout | 75.44 | -24.56 | 261 | 15.7 | -93.70 | -38.57 | -93.73 | 2841 |
| 82 | RSI momentum | momentum | 74.92 | -25.08 | 250 | 14.8 | -90.26 | -27.83 | -90.26 | 2376 |
| 83 | ADX DI cross | trend | 74.66 | -25.34 | 246 | 7.7 | -89.46 | -42.09 | -89.52 | 2108 |
| 84 | Stochastic reversion | reversion | 72.80 | -27.20 | 401 | 23.7 | -95.74 | -42.89 | -95.75 | 4024 |
| 85 | Consensus | meta | 72.67 | -27.33 | 231 | 7.4 | -94.71 | -29.56 | -94.71 | 2664 |
| 86 | Connors RSI(2) | reversion | 72.19 | -27.81 | 320 | 19.7 | -96.54 | -39.80 | -96.54 | 3645 |
| 87 | Bollinger reversion | reversion | 70.34 | -29.66 | 385 | 16.4 | -95.88 | -43.06 | -95.88 | 3687 |
| 88 | Candlestick reversal | reversion | 70.07 | -29.93 | 393 | 14.5 | -99.35 | -47.92 | -99.35 | 5595 |
| 89 | EMA 9/21 cross | trend | 69.86 | -30.14 | 358 | 15.9 | -97.35 | -39.10 | -97.35 | 3534 |
| 90 | OBV trend | momentum | 69.58 | -30.42 | 364 | 15.9 | -95.98 | -44.33 | -95.98 | 3562 |
| 91 | CCI reversion | reversion | 68.86 | -31.14 | 337 | 13.4 | -98.48 | -47.56 | -98.48 | 4688 |
| 92 | Parabolic SAR | trend | 68.26 | -31.74 | 337 | 13.1 | -96.97 | -50.18 | -96.98 | 3629 |
| 93 | VWAP momentum | momentum | 66.65 | -33.35 | 426 | 8.9 | -98.62 | -35.81 | -98.62 | 5278 |
| 94 | MACD cross | trend | 66.24 | -33.76 | 380 | 13.7 | -99.71 | -57.43 | -99.71 | 6066 |
| 95 | Williams %R | reversion | 65.60 | -34.40 | 462 | 21.2 | -99.52 | -53.92 | -99.53 | 6103 |
| 96 | Heikin-Ashi | trend | 65.28 | -34.72 | 342 | 6.1 | -99.89 | -68.41 | -99.89 | 8284 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-01T11:05 | Triple EMA stack · 1h | buy | BTC-USD | 1.50 | — | entry |
| 2026-10-01T11:05 | Triple EMA stack · 1h | sell | DOGE-USD | 1.50 | 0.00 | target is flat |
| 2026-10-01T11:05 | ROC + volume | buy | XRP-USD | 20.93 | — | entry signal |
| 2026-10-01T11:05 | ROC + volume | buy | SOL-USD | 20.93 | — | entry signal |
| 2026-10-01T11:05 | ROC + volume | buy | ETH-USD | 20.93 | — | entry signal |
| 2026-10-01T11:05 | ROC + volume | buy | DOGE-USD | 20.93 | — | entry signal |
| 2026-10-01T11:05 | VWAP momentum | sell | XRP-USD | 16.61 | -0.15 | exit signal |
| 2026-10-01T11:05 | VWAP momentum | sell | DOGE-USD | 16.60 | -0.16 | target is flat |
| 2026-10-01T11:05 | Heikin-Ashi | sell | XRP-USD | 13.07 | -0.04 | exit signal |
| 2026-10-01T11:05 | Heikin-Ashi | sell | SOL-USD | 13.00 | -0.08 | exit signal |
| 2026-10-01T11:05 | Heikin-Ashi | sell | ETH-USD | 13.07 | -0.05 | exit signal |
| 2026-10-01T11:05 | Heikin-Ashi | sell | DOGE-USD | 13.07 | -0.04 | exit signal |
| 2026-10-01T11:05 | Heikin-Ashi | sell | BTC-USD | 13.07 | -0.05 | exit signal |
| 2026-10-01T11:05 | ADX DI cross | sell | XRP-USD | 18.61 | -0.16 | exit signal |
| 2026-10-01T11:05 | ADX DI cross | sell | SOL-USD | 18.65 | -0.14 | exit signal |
| 2026-10-01T11:05 | ADX DI cross | sell | DOGE-USD | 18.66 | -0.13 | exit signal |
| 2026-10-01T11:05 | Triple EMA stack | buy | ETH-USD | 19.02 | — | entry signal |
| 2026-10-01T11:00 | Consensus | buy | ETH-USD | 18.19 | — | entry |
| 2026-10-01T11:00 | MACD cross · 1h | buy | ETH-USD | 6.75 | — | entry signal |
| 2026-10-01T11:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 9.14 | — | entry signal |
| 2026-10-01T11:00 | OBV trend | buy | ETH-USD | 17.42 | — | entry signal |
| 2026-10-01T11:00 | MACD zero-line | buy | XRP-USD | 19.14 | — | entry signal |
| 2026-10-01T11:00 | MACD zero-line | buy | SOL-USD | 19.14 | — | entry signal |
| 2026-10-01T11:00 | EMA 20/50 cross | buy | ETH-USD | 20.51 | — | entry signal |
| 2026-10-01T10:59 | AI bee: Bizzy | sell | DOGE-USD | 11.53 | -0.07 | Jev: sell (sell p=0.70) after 10 min |
| 2026-10-01T10:57 | Supertrend | buy | XRP-USD | 3.90 | — | rebalance up |
| 2026-10-01T10:57 | Supertrend | sell | ETH-USD | 3.90 | -0.01 | rebalance down |
| 2026-10-01T10:55 | CCI reversion | sell | SOL-USD | 17.17 | -0.03 | exit signal |
| 2026-10-01T10:55 | CCI reversion | sell | DOGE-USD | 17.27 | 0.07 | exit signal |
| 2026-10-01T10:55 | VWAP reversion | sell | DOGE-USD | 20.87 | 0.10 | exit signal |
| 2026-10-01T10:55 | Three white soldiers | buy | BTC-USD | 23.57 | — | entry signal |
| 2026-10-01T10:55 | Candlestick reversal | sell | XRP-USD | 17.52 | 0.04 | take-profit |
| 2026-10-01T10:55 | Candlestick reversal | sell | SOL-USD | 17.48 | 0.03 | take-profit |
| 2026-10-01T10:55 | Candlestick reversal | sell | DOGE-USD | 17.56 | 0.07 | take-profit |
| 2026-10-01T10:55 | Keltner breakout | buy | ETH-USD | 20.76 | — | entry signal |
| 2026-10-01T10:55 | Keltner breakout | buy | DOGE-USD | 20.76 | — | entry signal |
| 2026-10-01T10:55 | Keltner breakout | buy | BTC-USD | 20.76 | — | entry signal |
| 2026-10-01T10:55 | Bollinger breakout | buy | ETH-USD | 18.91 | — | entry signal |
| 2026-10-01T10:55 | Bollinger breakout | buy | BTC-USD | 18.91 | — | entry signal |
| 2026-10-01T10:55 | Donchian 20/10 | buy | XRP-USD | 19.10 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
