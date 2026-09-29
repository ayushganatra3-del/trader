# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T17:40:05.000139+00:00 · 5940 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.13 (+0.13%)

Closed trades 22, win rate 72.7%, fees £0.64, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 40.00 | -0.10 |

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

Today: 27711 decisions in 2582 calls, $0.3471 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T17:40 | 4 / 10 / 15 | AMZN 20%, BRK-B 15%, UPRO 14%, AAPL 14% |  |
| Breezy | 2026-09-29T17:40 | 0 / 24 / 5 | cash |  |
| Boozy | 2026-09-29T17:40 | 6 / 21 / 2 | UPRO 31%, COIN 30% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |
| CCI reversion | AMD | 2.04 | +3.07% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.94 | 1.94 | 1 | 100.0 | 14.65 | 3.18 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 4 | Agent | meta | 100.13 | 0.13 | 22 | 72.7 | -9.53 | -6.37 | -10.68 | 212 |
| 5 | Agent (aggressive) | meta | 100.08 | 0.08 | 8 | 62.5 | 0.38 | 0.28 | -3.92 | 93 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 10.11 | 1.92 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Copy: Congress Democrats (NANC) | copy | 99.93 | -0.07 | 0 | — | 8.60 | 3.29 | -3.62 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.45 | 1.78 | -1.51 | 83 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 99.62 | -0.38 | 0 | — | -1.90 | -0.74 | -7.65 | 1 |
| 12 | Hold BTC | benchmark | 99.60 | -0.40 | 0 | — | 28.79 | 3.64 | -8.68 | 1 |
| 13 | Hold SPY | benchmark | 99.51 | -0.49 | 0 | — | 2.98 | 1.50 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.50 | -0.50 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.39 | -0.61 | 0 | — | -3.61 | -2.22 | -5.09 | 2 |
| 16 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.88 | -4.39 | -14.73 | 121 |
| 17 | RSI(14) reversion · 1h | reversion | 99.23 | -0.77 | 7 | 57.1 | 9.40 | 2.28 | -6.57 | 119 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 20 | Z-score reversion · 1h | reversion | 98.63 | -1.37 | 10 | 50.0 | 4.18 | 1.03 | -8.60 | 153 |
| 21 | Daily: Bullish score | daily | 98.63 | -1.37 | 2 | 0.0 | -2.01 | -0.09 | -12.76 | 13 |
| 22 | Williams %R · 1h | reversion | 98.58 | -1.42 | 39 | 46.2 | -18.10 | -3.37 | -19.41 | 479 |
| 23 | Max aggression: 5-day momentum | meta | 98.46 | -1.53 | 2 | 50.0 | -8.01 | -0.39 | -29.56 | 29 |
| 24 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.41 | 3.82 | -4.73 | 195 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.44 | -1.56 | 0 | — | 24.53 | 3.54 | -6.29 | 1 |
| 26 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.28 | -0.02 | -15.21 | 47 |
| 27 | Copy: Insider buying | copy | 98.34 | -1.66 | 2 | 100.0 | -14.88 | -2.97 | -17.74 | 72 |
| 28 | Candlestick reversal · 1h | reversion | 98.31 | -1.69 | 19 | 26.3 | -27.73 | -6.81 | -28.16 | 488 |
| 29 | Agent (rotation) | meta | 98.14 | -1.86 | 32 | 12.5 | -6.26 | -2.10 | -10.83 | 232 |
| 30 | CCI reversion · 1h | reversion | 98.08 | -1.92 | 34 | 35.3 | 2.03 | 0.51 | -12.41 | 405 |
| 31 | Stochastic reversion · 1h | reversion | 97.94 | -2.06 | 26 | 53.8 | -14.54 | -3.21 | -15.13 | 325 |
| 32 | Connors RSI(2) · 1h | reversion | 97.77 | -2.23 | 41 | 46.3 | -13.10 | -4.13 | -13.22 | 236 |
| 33 | EMA 20/50 cross · 1h | trend | 97.67 | -2.33 | 10 | 10.0 | 15.39 | 1.87 | -14.36 | 127 |
| 34 | Daily: SMA 20/50 cross · AAPL | daily | 97.52 | -2.48 | 0 | — | -10.35 | -2.55 | -12.73 | 1 |
| 35 | Timing: Nasdaq FTD · TQQQ | daily | 97.48 | -2.52 | 0 | — | -11.55 | -2.40 | -15.27 | 2 |
| 36 | Squeeze breakout · 1h | breakout | 97.29 | -2.71 | 9 | 11.1 | 12.42 | 2.17 | -8.70 | 99 |
| 37 | Opening range 30m | breakout | 96.91 | -3.09 | 35 | 11.4 | -9.25 | -2.65 | -14.21 | 563 |
| 38 | Bollinger reversion · 1h | reversion | 96.82 | -3.18 | 22 | 27.3 | -18.48 | -5.16 | -18.63 | 313 |
| 39 | Supertrend · 1h | trend | 96.81 | -3.19 | 17 | 5.9 | 2.88 | 0.59 | -16.43 | 194 |
| 40 | Agent (ML meta-label) | meta | 96.38 | -3.62 | 121 | 10.7 | -3.35 | -0.47 | -13.85 | 374 |
| 41 | Donchian 55/20 · 1h | breakout | 96.26 | -3.74 | 12 | 0.0 | 4.80 | 0.83 | -16.96 | 112 |
| 42 | MACD cross · 1h | trend | 96.15 | -3.85 | 37 | 10.8 | -15.87 | -2.54 | -19.06 | 460 |
| 43 | Trend pullback · 1h | trend | 96.09 | -3.91 | 26 | 11.5 | -26.04 | -6.91 | -26.44 | 146 |
| 44 | Ichimoku · 1h | trend | 95.49 | -4.51 | 15 | 13.3 | 7.17 | 1.03 | -15.13 | 122 |
| 45 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -52.07 | -28.94 | -52.20 | 622 |
| 46 | Parabolic SAR · 1h | trend | 95.32 | -4.68 | 26 | 11.5 | -9.22 | -1.19 | -18.82 | 293 |
| 47 | Opening range 15m | breakout | 95.32 | -4.68 | 46 | 10.9 | -11.24 | -3.02 | -16.91 | 696 |
| 48 | Bollinger breakout · 1h | breakout | 95.25 | -4.75 | 17 | 5.9 | 6.80 | 1.09 | -11.10 | 284 |
| 49 | Max aggression: 1-day momentum | meta | 94.92 | -5.08 | 2 | 0.0 | -39.18 | -2.37 | -49.44 | 42 |
| 50 | MFI reversion · 1h | reversion | 94.88 | -5.12 | 43 | 11.6 | -10.50 | -1.95 | -17.27 | 128 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 1.00 | -12.60 | 125 |
| 52 | ADX DI cross · 1h | trend | 94.57 | -5.43 | 29 | 6.9 | -15.88 | -3.01 | -17.77 | 254 |
| 53 | RSI momentum · 1h | momentum | 94.54 | -5.46 | 24 | 4.2 | -0.01 | 0.20 | -15.29 | 216 |
| 54 | MACD zero-line · 1h | trend | 94.53 | -5.47 | 19 | 5.3 | -5.61 | -0.61 | -14.64 | 223 |
| 55 | Donchian 20/10 · 1h | breakout | 94.30 | -5.70 | 15 | 13.3 | 7.11 | 1.10 | -12.78 | 216 |
| 56 | Triple EMA stack · 1h | trend | 94.18 | -5.82 | 29 | 6.9 | -6.36 | -0.56 | -22.88 | 226 |
| 57 | Keltner breakout · 1h | breakout | 94.15 | -5.85 | 9 | 0.0 | -7.09 | -0.79 | -18.68 | 215 |
| 58 | VWAP momentum · 1h | momentum | 93.73 | -6.27 | 102 | 12.7 | -32.44 | -4.82 | -35.28 | 1227 |
| 59 | EMA 9/21 cross · 1h | trend | 93.53 | -6.47 | 40 | 12.5 | -4.57 | -0.43 | -16.92 | 310 |
| 60 | OBV trend · 1h | momentum | 93.03 | -6.97 | 53 | 7.5 | -9.78 | -1.03 | -25.24 | 327 |
| 61 | Heikin-Ashi · 1h | trend | 92.88 | -7.12 | 43 | 11.6 | -23.46 | -3.52 | -30.54 | 678 |
| 62 | RSI(14) reversion | reversion | 90.86 | -9.14 | 104 | 33.7 | -70.83 | -21.21 | -71.04 | 1471 |
| 63 | Squeeze breakout | breakout | 89.70 | -10.30 | 80 | 10.0 | -59.76 | -18.58 | -60.01 | 1178 |
| 64 | ROC + volume · 1h | momentum | 89.51 | -10.49 | 51 | 5.9 | -4.34 | -0.35 | -19.08 | 406 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | ROC + volume | momentum | 87.39 | -12.61 | 134 | 17.2 | -72.50 | -18.17 | -72.50 | 1614 |
| 68 | EMA 20/50 cross | trend | 87.37 | -12.63 | 107 | 15.0 | -78.58 | -17.62 | -78.67 | 1466 |
| 69 | Volume breakout | breakout | 87.36 | -12.64 | 90 | 12.2 | -62.08 | -20.58 | -62.11 | 887 |
| 70 | Donchian 55/20 | breakout | 87.22 | -12.78 | 91 | 14.3 | -68.53 | -15.74 | -68.54 | 1306 |
| 71 | Ichimoku | trend | 86.08 | -13.92 | 106 | 8.5 | -80.36 | -26.22 | -80.37 | 1758 |
| 72 | Keltner breakout | breakout | 85.32 | -14.68 | 138 | 11.6 | -84.98 | -35.24 | -84.98 | 1901 |
| 73 | Z-score reversion | reversion | 85.09 | -14.91 | 164 | 30.5 | -84.38 | -27.65 | -84.39 | 2091 |
| 74 | VWAP reversion | reversion | 84.58 | -15.42 | 122 | 18.9 | -71.85 | -17.61 | -72.20 | 1400 |
| 75 | MACD zero-line | trend | 83.03 | -16.97 | 174 | 14.9 | -91.81 | -36.31 | -91.81 | 2348 |
| 76 | Supertrend | trend | 82.76 | -17.24 | 159 | 16.4 | -87.35 | -24.71 | -87.44 | 1955 |
| 77 | MFI reversion | reversion | 81.54 | -18.45 | 170 | 18.8 | -87.61 | -34.95 | -87.78 | 2155 |
| 78 | Donchian 20/10 | breakout | 81.34 | -18.66 | 179 | 16.8 | -90.80 | -29.94 | -90.82 | 2668 |
| 79 | Bollinger breakout | breakout | 80.97 | -19.03 | 186 | 14.5 | -93.99 | -42.21 | -93.99 | 2851 |
| 80 | Triple EMA stack | trend | 80.82 | -19.18 | 194 | 14.4 | -93.05 | -36.64 | -93.05 | 2613 |
| 81 | RSI momentum | momentum | 80.56 | -19.44 | 174 | 11.5 | -90.53 | -29.81 | -90.53 | 2384 |
| 82 | ADX DI cross | trend | 80.14 | -19.86 | 181 | 6.6 | -89.42 | -47.37 | -89.44 | 2100 |
| 83 | Trend pullback | trend | 79.93 | -20.07 | 164 | 17.7 | -90.90 | -35.25 | -90.90 | 2284 |
| 84 | EMA 9/21 cross | trend | 77.91 | -22.09 | 250 | 15.2 | -97.34 | -41.84 | -97.35 | 3539 |
| 85 | Connors RSI(2) | reversion | 77.15 | -22.85 | 237 | 16.0 | -96.48 | -43.15 | -96.48 | 3648 |
| 86 | Consensus | meta | 76.98 | -23.02 | 180 | 7.2 | -94.63 | -30.71 | -94.63 | 2643 |
| 87 | Stochastic reversion | reversion | 76.47 | -23.53 | 297 | 23.2 | -95.95 | -48.36 | -95.98 | 4067 |
| 88 | Candlestick reversal ⏸ | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.35 | -52.24 | -99.35 | 5580 |
| 89 | OBV trend | momentum | 75.74 | -24.26 | 252 | 14.3 | -95.95 | -49.95 | -95.95 | 3538 |
| 90 | Bollinger reversion | reversion | 75.27 | -24.73 | 287 | 15.0 | -95.81 | -46.63 | -95.81 | 3689 |
| 91 | VWAP momentum | momentum | 74.18 | -25.82 | 347 | 9.8 | -98.43 | -36.50 | -98.45 | 5177 |
| 92 | CCI reversion | reversion | 74.02 | -25.98 | 204 | 8.8 | -98.45 | -52.69 | -98.45 | 4695 |
| 93 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -97.00 | -57.03 | -97.00 | 3652 |
| 94 | MACD cross | trend | 72.53 | -27.47 | 234 | 12.0 | -99.71 | -68.72 | -99.71 | 6091 |
| 95 | Williams %R | reversion | 71.98 | -28.02 | 306 | 19.9 | -99.52 | -61.96 | -99.53 | 6098 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -91.72 | -99.89 | 8318 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T17:40 | Agent (ML meta-label) | buy | PLTR | 5.67 | — | entry |
| 2026-09-29T17:40 | Agent (ML meta-label) | buy | COIN | 5.67 | — | following Connors RSI(2) · 1h |
| 2026-09-29T17:40 | Agent | sell | TQQQ | 20.05 | 0.04 | selected signal exited |
| 2026-09-29T17:40 | Parabolic SAR · 1h | buy | META | 4.77 | — | rebalance up |
| 2026-09-29T17:40 | Parabolic SAR · 1h | sell | NVDA | 4.77 | 0.01 | rebalance down |
| 2026-09-29T17:40 | Z-score reversion | buy | XRP-USD | 6.08 | — | entry |
| 2026-09-29T17:40 | Z-score reversion | sell | AAPL | 9.53 | 0.00 | exit signal |
| 2026-09-29T17:40 | Bollinger reversion | buy | TECL | 4.05 | — | rebalance up |
| 2026-09-29T17:40 | Bollinger reversion | buy | NVDA | 4.05 | — | rebalance up |
| 2026-09-29T17:40 | Bollinger reversion | sell | TNA | 5.81 | 0.01 | exit signal |
| 2026-09-29T17:40 | RSI(14) reversion | buy | DOGE-USD | 6.50 | — | entry |
| 2026-09-29T17:40 | RSI(14) reversion | sell | AAPL | 6.07 | 0.01 | exit signal |
| 2026-09-29T17:40 | Donchian 20/10 | buy | AAPL | 20.26 | — | entry signal |
| 2026-09-29T17:40 | MACD cross | buy | SOXL | 3.18 | — | entry |
| 2026-09-29T17:40 | MACD cross | sell | COIN | 3.18 | -0.02 | exit signal |
| 2026-09-29T17:40 | EMA 9/21 cross | buy | AAPL | 7.84 | — | entry signal |
| 2026-09-29T17:40 | EMA 9/21 cross | sell | MSTR | 7.84 | -0.03 | exit signal |
| 2026-09-29T17:35 | Agent (ML meta-label) | buy | TNA | 6.43 | — | entry |
| 2026-09-29T17:35 | OBV trend · 1h | buy | NVDA | 4.66 | — | rebalance up |
| 2026-09-29T17:35 | Williams %R | buy | AMZN | 2.45 | — | entry |
| 2026-09-29T17:35 | Williams %R | sell | TQQQ | 2.04 | -0.01 | exit signal |
| 2026-09-29T17:35 | Stochastic reversion | sell | TQQQ | 3.65 | 0.01 | exit signal |
| 2026-09-29T17:35 | Squeeze breakout | buy | AAPL | 22.42 | — | entry signal |
| 2026-09-29T17:35 | Bollinger breakout | buy | AAPL | 20.24 | — | entry signal |
| 2026-09-29T17:35 | VWAP momentum | buy | LABU | 18.36 | — | entry signal |
| 2026-09-29T17:35 | ADX DI cross | buy | AAPL | 20.04 | — | entry signal |
| 2026-09-29T17:35 | Triple EMA stack | buy | AMZN | 20.20 | — | entry signal |
| 2026-09-29T17:35 | EMA 9/21 cross | buy | MSTR | 7.87 | — | entry signal |
| 2026-09-29T17:35 | EMA 9/21 cross | buy | META | 5.08 | — | rebalance up |
| 2026-09-29T17:35 | EMA 9/21 cross | sell | GOOGL | 6.47 | -0.01 | rebalance down |
| 2026-09-29T17:35 | EMA 9/21 cross | sell | AMZN | 6.49 | 0.01 | rebalance down |
| 2026-09-29T17:30 | Agent (ML meta-label) | sell | TNA | 1.43 | 0.00 | selected signal exited |
| 2026-09-29T17:30 | Agent (ML meta-label) | sell | SOL-USD | 6.00 | -0.03 | selected signal exited |
| 2026-09-29T17:30 | Consensus | buy | META | 19.26 | — | entry |
| 2026-09-29T17:30 | Stochastic reversion · 1h | buy | UPRO | 9.78 | — | entry signal |
| 2026-09-29T17:30 | Stochastic reversion · 1h | buy | TNA | 9.81 | — | entry signal |
| 2026-09-29T17:30 | Stochastic reversion · 1h | buy | SPY | 9.81 | — | entry signal |
| 2026-09-29T17:30 | Stochastic reversion · 1h | buy | IWM | 9.81 | — | entry signal |
| 2026-09-29T17:30 | Stochastic reversion · 1h | buy | AAPL | 9.81 | — | entry |
| 2026-09-29T17:30 | Stochastic reversion · 1h | sell | MSTR | 9.67 | -0.18 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
