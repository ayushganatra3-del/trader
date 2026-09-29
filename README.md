# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T16:10:05.000175+00:00 · 5870 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.22 (+0.22%)

Closed trades 20, win rate 75.0%, fees £0.60, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 20.05 | -0.02 |
| TQQQ | 20.04 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-29 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 21510 decisions in 2372 calls, $0.2744 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T16:10 | 11 / 14 / 5 | XRP-USD 16%, PLTR 16%, SOXL 16%, DOGE-USD 16% |  |
| Breezy | 2026-09-29T16:10 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-09-29T16:10 | 15 / 15 / 0 | MSTR 34%, TECL 34% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |
| VWAP reversion | NVDA | 2.05 | +2.06% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.56 | 1.56 | 1 | 100.0 | 14.31 | 3.11 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 4 | Agent | meta | 100.22 | 0.22 | 20 | 75.0 | -9.19 | -5.84 | -10.53 | 208 |
| 5 | Agent (aggressive) | meta | 100.20 | 0.20 | 8 | 62.5 | 1.02 | 0.60 | -4.81 | 92 |
| 6 | Copy: Congress Democrats (NANC) | copy | 100.10 | 0.10 | 0 | — | 7.02 | 2.61 | -3.62 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 12.54 | 2.39 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.45 | 1.78 | -1.51 | 83 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 99.45 | -0.55 | 0 | — | -1.79 | -0.70 | -7.65 | 1 |
| 12 | Hold SPY | benchmark | 99.45 | -0.55 | 0 | — | 3.57 | 1.84 | -3.66 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 99.43 | -0.57 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 99.41 | -0.59 | 0 | — | -3.53 | -2.17 | -5.09 | 2 |
| 15 | Hold BTC | benchmark | 99.38 | -0.62 | 0 | — | 29.73 | 3.74 | -8.68 | 1 |
| 16 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.79 | 121 |
| 17 | Max aggression: 5-day momentum | meta | 99.29 | -0.71 | 2 | 50.0 | -7.17 | -0.31 | -29.56 | 29 |
| 18 | RSI(14) reversion · 1h | reversion | 99.23 | -0.77 | 7 | 57.1 | 2.78 | 0.86 | -6.57 | 118 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 21 | Z-score reversion · 1h | reversion | 98.64 | -1.36 | 9 | 44.4 | 4.22 | 1.04 | -8.60 | 151 |
| 22 | Daily: Bullish score | daily | 98.56 | -1.44 | 2 | 0.0 | -1.86 | -0.07 | -12.76 | 13 |
| 23 | Williams %R · 1h | reversion | 98.51 | -1.49 | 39 | 46.2 | -17.74 | -3.26 | -19.41 | 484 |
| 24 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.38 | 3.81 | -4.73 | 195 |
| 25 | Copy: Insider buying | copy | 98.39 | -1.61 | 2 | 100.0 | -14.77 | -2.95 | -17.74 | 72 |
| 26 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -0.92 | 0.04 | -15.21 | 47 |
| 27 | Candlestick reversal · 1h | reversion | 98.33 | -1.67 | 17 | 29.4 | -25.93 | -6.32 | -26.38 | 482 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.26 | -1.74 | 0 | — | 24.93 | 3.60 | -6.29 | 1 |
| 29 | CCI reversion · 1h | reversion | 98.08 | -1.92 | 34 | 35.3 | 2.15 | 0.52 | -12.41 | 406 |
| 30 | Agent (rotation) | meta | 98.02 | -1.98 | 32 | 12.5 | -5.74 | -1.96 | -11.79 | 218 |
| 31 | EMA 20/50 cross · 1h | trend | 97.89 | -2.11 | 9 | 11.1 | 16.17 | 1.94 | -14.36 | 127 |
| 32 | Opening range 30m | breakout | 97.83 | -2.17 | 31 | 12.9 | -8.36 | -2.41 | -13.54 | 559 |
| 33 | Connors RSI(2) · 1h | reversion | 97.82 | -2.18 | 41 | 46.3 | -13.00 | -4.11 | -13.22 | 236 |
| 34 | Timing: Nasdaq FTD · TQQQ | daily | 97.63 | -2.37 | 0 | — | -11.34 | -2.35 | -15.27 | 2 |
| 35 | Stochastic reversion · 1h | reversion | 97.53 | -2.47 | 26 | 53.8 | -14.84 | -3.28 | -15.14 | 320 |
| 36 | Squeeze breakout · 1h | breakout | 97.42 | -2.58 | 9 | 11.1 | 15.31 | 2.70 | -6.18 | 97 |
| 37 | Supertrend · 1h | trend | 97.39 | -2.61 | 16 | 6.2 | 4.28 | 0.77 | -16.43 | 197 |
| 38 | Daily: SMA 20/50 cross · AAPL | daily | 97.11 | -2.89 | 0 | — | -10.13 | -2.49 | -12.73 | 1 |
| 39 | Donchian 55/20 · 1h | breakout | 97.00 | -3.00 | 11 | 0.0 | 4.59 | 0.81 | -16.96 | 113 |
| 40 | Bollinger reversion · 1h | reversion | 96.81 | -3.19 | 22 | 27.3 | -18.38 | -5.13 | -18.44 | 306 |
| 41 | Agent (ML meta-label) | meta | 96.57 | -3.43 | 107 | 11.2 | 2.20 | 0.55 | -10.67 | 390 |
| 42 | MACD cross · 1h | trend | 96.51 | -3.49 | 36 | 8.3 | -18.10 | -3.08 | -21.59 | 459 |
| 43 | Trend pullback · 1h | trend | 96.44 | -3.56 | 25 | 12.0 | -28.87 | -7.06 | -29.59 | 148 |
| 44 | Opening range 15m | breakout | 96.31 | -3.69 | 41 | 12.2 | -10.37 | -2.81 | -16.16 | 692 |
| 45 | Ichimoku · 1h | trend | 95.98 | -4.01 | 14 | 14.3 | 7.02 | 1.02 | -15.13 | 121 |
| 46 | Parabolic SAR · 1h | trend | 95.83 | -4.17 | 25 | 12.0 | -8.05 | -1.01 | -18.82 | 291 |
| 47 | MACD zero-line · 1h | trend | 95.40 | -4.60 | 18 | 5.6 | -4.71 | -0.48 | -14.64 | 222 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -51.83 | -28.82 | -52.12 | 623 |
| 49 | Bollinger breakout · 1h | breakout | 95.26 | -4.74 | 17 | 5.9 | 8.06 | 1.25 | -10.11 | 284 |
| 50 | RSI momentum · 1h | momentum | 95.26 | -4.74 | 23 | 4.3 | -0.64 | 0.11 | -15.29 | 212 |
| 51 | Donchian 20/10 · 1h | breakout | 94.91 | -5.09 | 13 | 15.4 | 8.29 | 1.24 | -12.78 | 215 |
| 52 | ADX DI cross · 1h | trend | 94.86 | -5.14 | 29 | 6.9 | -15.74 | -2.99 | -18.02 | 254 |
| 53 | Volume breakout · 1h | breakout | 94.83 | -5.17 | 26 | 3.8 | 6.03 | 1.02 | -12.60 | 125 |
| 54 | Triple EMA stack · 1h | trend | 94.75 | -5.25 | 27 | 7.4 | -7.45 | -0.72 | -22.53 | 230 |
| 55 | MFI reversion · 1h | reversion | 94.66 | -5.34 | 41 | 12.2 | -10.76 | -2.00 | -17.27 | 127 |
| 56 | VWAP momentum · 1h | momentum | 94.44 | -5.56 | 100 | 13.0 | -31.12 | -4.58 | -34.74 | 1237 |
| 57 | Keltner breakout · 1h | breakout | 94.27 | -5.73 | 9 | 0.0 | -6.03 | -0.62 | -18.68 | 215 |
| 58 | EMA 9/21 cross · 1h | trend | 94.06 | -5.94 | 39 | 12.8 | -3.45 | -0.28 | -16.92 | 309 |
| 59 | OBV trend · 1h | momentum | 93.66 | -6.34 | 50 | 8.0 | -8.56 | -0.87 | -25.24 | 327 |
| 60 | Max aggression: 1-day momentum | meta | 93.57 | -6.43 | 2 | 0.0 | -39.99 | -2.45 | -49.44 | 42 |
| 61 | Heikin-Ashi · 1h | trend | 93.10 | -6.90 | 41 | 12.2 | -22.54 | -3.35 | -30.30 | 679 |
| 62 | RSI(14) reversion | reversion | 91.15 | -8.85 | 99 | 33.3 | -70.92 | -21.46 | -71.15 | 1473 |
| 63 | ROC + volume · 1h | momentum | 89.81 | -10.19 | 50 | 6.0 | -4.83 | -0.41 | -19.12 | 408 |
| 64 | Squeeze breakout | breakout | 89.78 | -10.21 | 79 | 10.1 | -60.13 | -18.89 | -60.42 | 1181 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | Donchian 55/20 | breakout | 87.96 | -12.04 | 88 | 14.8 | -68.28 | -15.62 | -68.32 | 1309 |
| 68 | EMA 20/50 cross | trend | 87.63 | -12.37 | 104 | 15.4 | -78.68 | -17.59 | -78.85 | 1465 |
| 69 | ROC + volume | momentum | 87.44 | -12.56 | 133 | 17.3 | -72.58 | -18.25 | -73.09 | 1668 |
| 70 | Volume breakout | breakout | 87.38 | -12.62 | 89 | 12.4 | -62.42 | -20.80 | -62.80 | 928 |
| 71 | Ichimoku | trend | 86.02 | -13.97 | 105 | 8.6 | -80.46 | -26.25 | -80.46 | 1766 |
| 72 | Keltner breakout | breakout | 85.58 | -14.42 | 138 | 11.6 | -85.02 | -35.57 | -85.28 | 1939 |
| 73 | Z-score reversion | reversion | 85.02 | -14.98 | 160 | 30.0 | -84.48 | -27.96 | -84.49 | 2095 |
| 74 | VWAP reversion | reversion | 84.38 | -15.62 | 119 | 17.6 | -71.91 | -17.73 | -72.14 | 1397 |
| 75 | Supertrend | trend | 83.19 | -16.81 | 155 | 16.8 | -87.57 | -25.31 | -87.59 | 1957 |
| 76 | MACD zero-line | trend | 83.00 | -17.00 | 172 | 14.5 | -91.63 | -36.35 | -91.63 | 2354 |
| 77 | MFI reversion | reversion | 82.02 | -17.98 | 163 | 18.4 | -87.60 | -35.43 | -87.68 | 2147 |
| 78 | Donchian 20/10 | breakout | 81.35 | -18.65 | 178 | 16.9 | -90.94 | -30.49 | -91.09 | 2694 |
| 79 | Bollinger breakout | breakout | 81.05 | -18.95 | 183 | 14.8 | -94.04 | -42.85 | -94.13 | 2880 |
| 80 | Triple EMA stack | trend | 80.89 | -19.11 | 192 | 14.6 | -93.08 | -36.61 | -93.08 | 2619 |
| 81 | RSI momentum | momentum | 80.72 | -19.28 | 172 | 11.6 | -90.45 | -29.85 | -90.45 | 2383 |
| 82 | ADX DI cross | trend | 80.20 | -19.80 | 180 | 6.7 | -89.43 | -47.40 | -89.53 | 2102 |
| 83 | Trend pullback | trend | 80.20 | -19.80 | 163 | 17.8 | -90.79 | -34.73 | -90.79 | 2289 |
| 84 | EMA 9/21 cross | trend | 77.70 | -22.30 | 248 | 14.9 | -97.35 | -42.11 | -97.36 | 3534 |
| 85 | Connors RSI(2) | reversion | 77.66 | -22.34 | 234 | 16.2 | -96.46 | -43.10 | -96.47 | 3648 |
| 86 | Consensus | meta | 77.48 | -22.52 | 177 | 7.3 | -94.55 | -30.38 | -94.56 | 2640 |
| 87 | Stochastic reversion | reversion | 76.62 | -23.38 | 287 | 22.0 | -95.92 | -47.97 | -95.97 | 4064 |
| 88 | Candlestick reversal | reversion | 76.58 | -23.42 | 250 | 13.2 | -99.35 | -52.78 | -99.35 | 5565 |
| 89 | OBV trend | momentum | 76.14 | -23.86 | 249 | 14.1 | -95.84 | -49.57 | -95.84 | 3548 |
| 90 | Bollinger reversion | reversion | 75.49 | -24.51 | 273 | 13.6 | -95.77 | -46.37 | -95.79 | 3683 |
| 91 | VWAP momentum | momentum | 74.41 | -25.59 | 341 | 9.7 | -98.45 | -36.85 | -98.47 | 5212 |
| 92 | CCI reversion | reversion | 74.21 | -25.80 | 195 | 6.2 | -98.44 | -52.11 | -98.45 | 4689 |
| 93 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -97.00 | -57.02 | -97.00 | 3649 |
| 94 | MACD cross | trend | 72.54 | -27.46 | 229 | 11.4 | -99.70 | -65.13 | -99.70 | 6087 |
| 95 | Williams %R | reversion | 72.23 | -27.77 | 292 | 19.5 | -99.52 | -61.68 | -99.52 | 6092 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.25 | -99.89 | 8321 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T16:10 | Agent (ML meta-label) | buy | PLTR | 6.04 | — | entry |
| 2026-09-29T16:10 | Agent (ML meta-label) | buy | MSTR | 6.04 | — | entry |
| 2026-09-29T16:10 | Consensus | buy | XRP-USD | 19.38 | — | entry |
| 2026-09-29T16:10 | Agent | buy | TQQQ | 20.05 | — | following Candlestick reversal |
| 2026-09-29T16:10 | Candlestick reversal | buy | XRP-USD | 6.95 | — | entry signal |
| 2026-09-29T16:10 | Candlestick reversal | buy | TQQQ | 6.97 | — | entry signal |
| 2026-09-29T16:10 | Candlestick reversal | buy | SOL-USD | 6.97 | — | entry signal |
| 2026-09-29T16:10 | Candlestick reversal | buy | META | 6.97 | — | entry |
| 2026-09-29T16:10 | Candlestick reversal | buy | GOOGL | 6.97 | — | entry |
| 2026-09-29T16:10 | Candlestick reversal | sell | TSLA | 5.74 | -0.01 | rebalance down |
| 2026-09-29T16:10 | Candlestick reversal | sell | TECL | 5.82 | -0.01 | rebalance down |
| 2026-09-29T16:10 | Candlestick reversal | sell | PLTR | 5.82 | -0.01 | rebalance down |
| 2026-09-29T16:10 | Candlestick reversal | sell | LABU | 5.85 | 0.03 | rebalance down |
| 2026-09-29T16:10 | Candlestick reversal | sell | IWM | 5.81 | -0.01 | rebalance down |
| 2026-09-29T16:10 | Candlestick reversal | sell | COIN | 5.78 | -0.02 | rebalance down |
| 2026-09-29T16:10 | VWAP momentum | buy | AMZN | 18.61 | — | entry signal |
| 2026-09-29T16:05 | Consensus | sell | NVDA | 19.36 | -0.07 | target is flat |
| 2026-09-29T16:05 | MFI reversion · 1h | buy | PLTR | 23.65 | — | entry |
| 2026-09-29T16:05 | MFI reversion | buy | BTC-USD | 3.42 | — | entry |
| 2026-09-29T16:05 | MFI reversion | buy | BITX | 6.83 | — | entry |
| 2026-09-29T16:05 | MFI reversion | sell | AAPL | 10.22 | -0.05 | stop-loss |
| 2026-09-29T16:05 | Williams %R | buy | ETH-USD | 2.77 | — | entry |
| 2026-09-29T16:05 | Williams %R | buy | AMZN | 3.28 | — | entry |
| 2026-09-29T16:05 | Williams %R | buy | AMD | 3.28 | — | entry |
| 2026-09-29T16:05 | Williams %R | sell | UPRO | 3.79 | -0.01 | stop-loss |
| 2026-09-29T16:05 | Williams %R | sell | AAPL | 5.54 | -0.03 | stop-loss |
| 2026-09-29T16:05 | VWAP reversion | buy | COIN | 7.65 | — | entry |
| 2026-09-29T16:05 | VWAP reversion | sell | UPRO | 7.65 | -0.04 | stop-loss |
| 2026-09-29T16:05 | Bollinger reversion | buy | AAPL | 5.80 | — | entry |
| 2026-09-29T16:05 | Bollinger reversion | sell | UPRO | 5.80 | -0.03 | stop-loss |
| 2026-09-29T16:05 | RSI(14) reversion | buy | DOGE-USD | 2.08 | — | entry |
| 2026-09-29T16:05 | RSI(14) reversion | buy | BTC-USD | 7.01 | — | entry |
| 2026-09-29T16:05 | RSI(14) reversion | sell | AAPL | 9.09 | -0.06 | stop-loss |
| 2026-09-29T16:05 | Opening range 15m | sell | AMD | 24.02 | -0.22 | stop-loss |
| 2026-09-29T16:05 | RSI momentum | sell | AMD | 20.15 | -0.13 | exit signal |
| 2026-09-29T16:05 | VWAP momentum | buy | XRP-USD | 18.63 | — | entry signal |
| 2026-09-29T16:05 | VWAP momentum | buy | SQQQ | 6.15 | — | rebalance up |
| 2026-09-29T16:05 | VWAP momentum | buy | MSFT | 3.74 | — | rebalance up |
| 2026-09-29T16:05 | VWAP momentum | sell | TSLA | 11.22 | -0.02 | exit signal |
| 2026-09-29T16:05 | VWAP momentum | sell | SOXL | 14.89 | -0.08 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
