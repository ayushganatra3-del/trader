# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T14:41:05.000143+00:00 · 5798 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.24 (+0.24%)

Closed trades 19, win rate 73.7%, fees £0.56, max drawdown -1.39%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-28 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 15063 decisions in 2156 calls, $0.1988 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T14:41 | 6 / 11 / 13 | XRP-USD 18%, TECL 16%, DOGE-USD 15%, SQQQ 15% |  |
| Breezy | 2026-09-29T14:41 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-09-29T14:41 | 10 / 17 / 3 | BITX 38%, ETHU 38% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| VWAP reversion | NVDA | 2.16 | +1.89% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.61 | 0.61 | 1 | 100.0 | 13.32 | 2.91 | -7.55 | 43 |
| 2 | Max aggression: 5-day momentum | meta | 100.60 | 0.60 | 2 | 50.0 | -5.87 | -0.18 | -29.56 | 29 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 4 | Hold BTC | benchmark | 100.37 | 0.37 | 0 | — | 30.90 | 3.87 | -8.68 | 1 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Agent | meta | 100.24 | 0.24 | 19 | 73.7 | -8.61 | -5.60 | -10.16 | 206 |
| 7 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 8 | Daily: Bullish score | daily | 100.12 | 0.12 | 2 | 0.0 | -0.25 | 0.17 | -12.76 | 13 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.06 | 0.07 | 0 | — | 7.84 | 2.98 | -3.62 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 11.23 | 2.14 | -7.93 | 7 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.45 | 1.78 | -1.51 | 83 |
| 14 | Hold SPY | benchmark | 99.65 | -0.35 | 0 | — | 4.22 | 2.19 | -3.66 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.63 | -0.37 | 0 | — | -3.24 | -1.97 | -5.09 | 2 |
| 16 | Copy: Warren Buffett (BRK-B) | copy | 99.62 | -0.38 | 0 | — | -1.73 | -0.67 | -7.65 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.58 | -0.42 | 0 | — | -2.58 | -1.24 | -5.14 | 1 |
| 18 | RSI(14) reversion · 1h | reversion | 99.45 | -0.55 | 5 | 80.0 | 4.53 | 1.31 | -6.57 | 126 |
| 19 | Williams %R · 1h | reversion | 99.37 | -0.63 | 34 | 52.9 | -16.81 | -3.06 | -19.41 | 484 |
| 20 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 21 | EMA 20/50 cross · 1h | trend | 99.21 | -0.79 | 8 | 12.5 | 18.04 | 2.12 | -14.36 | 127 |
| 22 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 23 | Gap and go | momentum | 99.02 | -0.98 | 8 | 12.5 | 16.09 | 3.99 | -4.73 | 194 |
| 24 | Candlestick reversal · 1h | reversion | 98.99 | -1.01 | 14 | 28.6 | -25.45 | -5.93 | -26.57 | 491 |
| 25 | Stochastic reversion · 1h | reversion | 98.97 | -1.02 | 26 | 53.8 | -14.09 | -3.10 | -15.70 | 321 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 98.96 | -1.04 | 0 | — | 26.49 | 3.80 | -6.29 | 1 |
| 27 | CCI reversion · 1h | reversion | 98.94 | -1.06 | 29 | 41.4 | 3.31 | 0.72 | -12.41 | 406 |
| 28 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 29 | Z-score reversion · 1h | reversion | 98.62 | -1.38 | 7 | 57.1 | 3.23 | 0.82 | -8.60 | 154 |
| 30 | Connors RSI(2) · 1h | reversion | 98.50 | -1.50 | 41 | 46.3 | -12.33 | -3.92 | -13.23 | 236 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 98.45 | -1.55 | 0 | — | -10.53 | -2.15 | -15.27 | 2 |
| 32 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.28 | -0.02 | -15.21 | 47 |
| 33 | Opening range 30m | breakout | 98.33 | -1.67 | 31 | 12.9 | -7.85 | -2.25 | -13.54 | 559 |
| 34 | Squeeze breakout · 1h | breakout | 98.26 | -1.74 | 7 | 14.3 | 17.98 | 3.06 | -6.80 | 99 |
| 35 | Copy: Insider buying | copy | 98.26 | -1.74 | 2 | 100.0 | -14.91 | -2.98 | -17.74 | 72 |
| 36 | Supertrend · 1h | trend | 98.21 | -1.79 | 12 | 8.3 | 5.49 | 0.93 | -16.43 | 196 |
| 37 | Donchian 55/20 · 1h | breakout | 97.99 | -2.01 | 10 | 0.0 | 5.42 | 0.91 | -16.96 | 114 |
| 38 | Agent (rotation) | meta | 97.90 | -2.10 | 30 | 13.3 | -5.89 | -2.02 | -11.94 | 218 |
| 39 | Trend pullback · 1h | trend | 97.80 | -2.21 | 24 | 12.5 | -27.91 | -6.73 | -29.59 | 148 |
| 40 | Bollinger reversion · 1h | reversion | 97.65 | -2.35 | 20 | 30.0 | -17.60 | -4.88 | -17.86 | 306 |
| 41 | Agent (ML meta-label) | meta | 97.43 | -2.57 | 89 | 12.4 | -0.52 | 0.05 | -12.21 | 393 |
| 42 | MACD cross · 1h | trend | 97.43 | -2.57 | 33 | 9.1 | -16.99 | -2.88 | -21.54 | 459 |
| 43 | Daily: SMA 20/50 cross · AAPL | daily | 97.37 | -2.63 | 0 | — | -9.90 | -2.44 | -12.73 | 1 |
| 44 | Parabolic SAR · 1h | trend | 97.25 | -2.75 | 21 | 14.3 | -6.26 | -0.74 | -18.82 | 292 |
| 45 | Ichimoku · 1h | trend | 97.18 | -2.83 | 12 | 16.7 | 8.43 | 1.17 | -15.13 | 121 |
| 46 | MACD zero-line · 1h | trend | 97.09 | -2.91 | 15 | 6.7 | -2.85 | -0.21 | -14.64 | 222 |
| 47 | Opening range 15m | breakout | 97.04 | -2.96 | 40 | 12.5 | -9.65 | -2.61 | -16.14 | 691 |
| 48 | RSI momentum · 1h | momentum | 96.56 | -3.44 | 20 | 5.0 | 2.01 | 0.48 | -15.29 | 210 |
| 49 | Bollinger breakout · 1h | breakout | 96.39 | -3.60 | 14 | 7.1 | 11.07 | 1.61 | -10.46 | 287 |
| 50 | Triple EMA stack · 1h | trend | 96.15 | -3.85 | 26 | 7.7 | -3.75 | -0.24 | -22.53 | 210 |
| 51 | VWAP momentum · 1h | momentum | 96.09 | -3.91 | 92 | 13.0 | -28.88 | -4.16 | -33.85 | 1239 |
| 52 | ADX DI cross · 1h | trend | 95.83 | -4.17 | 25 | 8.0 | -10.62 | -1.94 | -15.70 | 255 |
| 53 | Donchian 20/10 · 1h | breakout | 95.74 | -4.26 | 12 | 16.7 | 9.46 | 1.39 | -12.78 | 216 |
| 54 | Volume breakout · 1h | breakout | 95.41 | -4.59 | 25 | 4.0 | 6.93 | 1.14 | -12.60 | 127 |
| 55 | Three white soldiers | momentum | 95.36 | -4.64 | 42 | 19.0 | -51.91 | -28.83 | -52.20 | 627 |
| 56 | EMA 9/21 cross · 1h | trend | 95.23 | -4.77 | 36 | 13.9 | -1.81 | -0.05 | -16.92 | 310 |
| 57 | MFI reversion · 1h | reversion | 95.22 | -4.78 | 38 | 13.2 | -11.89 | -2.25 | -17.46 | 128 |
| 58 | Keltner breakout · 1h | breakout | 95.14 | -4.86 | 7 | 0.0 | -1.74 | -0.03 | -18.68 | 223 |
| 59 | OBV trend · 1h | momentum | 94.92 | -5.08 | 48 | 6.2 | -8.18 | -0.82 | -25.24 | 328 |
| 60 | Heikin-Ashi · 1h | trend | 94.34 | -5.66 | 36 | 11.1 | -21.44 | -3.16 | -29.64 | 678 |
| 61 | Max aggression: 1-day momentum | meta | 93.30 | -6.70 | 2 | 0.0 | -40.13 | -2.46 | -49.44 | 42 |
| 62 | RSI(14) reversion | reversion | 91.94 | -8.06 | 95 | 34.7 | -70.72 | -21.36 | -71.15 | 1479 |
| 63 | ROC + volume · 1h | momentum | 91.01 | -8.99 | 46 | 6.5 | -4.76 | -0.46 | -18.14 | 409 |
| 64 | Squeeze breakout | breakout | 90.20 | -9.80 | 77 | 9.1 | -59.54 | -18.40 | -60.51 | 1190 |
| 65 | Donchian 55/20 | breakout | 88.97 | -11.03 | 85 | 12.9 | -67.38 | -15.37 | -67.59 | 1309 |
| 66 | EMA 20/50 cross | trend | 88.70 | -11.30 | 98 | 14.3 | -78.32 | -17.39 | -78.78 | 1475 |
| 67 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 68 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 69 | ROC + volume | momentum | 87.79 | -12.21 | 131 | 17.6 | -72.29 | -18.10 | -72.91 | 1669 |
| 70 | Volume breakout | breakout | 87.38 | -12.62 | 89 | 12.4 | -62.48 | -20.77 | -62.86 | 916 |
| 71 | Ichimoku | trend | 86.89 | -13.11 | 97 | 8.2 | -80.49 | -26.46 | -80.58 | 1768 |
| 72 | Keltner breakout | breakout | 86.43 | -13.57 | 134 | 11.2 | -84.87 | -35.19 | -85.18 | 1938 |
| 73 | Z-score reversion | reversion | 85.72 | -14.29 | 152 | 30.9 | -84.31 | -27.66 | -84.48 | 2087 |
| 74 | VWAP reversion | reversion | 85.26 | -14.74 | 108 | 16.7 | -71.17 | -17.31 | -71.83 | 1396 |
| 75 | Supertrend | trend | 83.95 | -16.05 | 152 | 15.8 | -87.12 | -24.35 | -87.53 | 1964 |
| 76 | MACD zero-line | trend | 83.56 | -16.44 | 165 | 15.2 | -91.64 | -36.54 | -91.68 | 2355 |
| 77 | MFI reversion | reversion | 82.44 | -17.56 | 155 | 17.4 | -87.41 | -33.71 | -87.71 | 2164 |
| 78 | Donchian 20/10 | breakout | 82.11 | -17.89 | 174 | 16.7 | -90.81 | -30.11 | -91.07 | 2690 |
| 79 | Triple EMA stack | trend | 81.81 | -18.20 | 184 | 14.7 | -93.03 | -37.39 | -93.05 | 2641 |
| 80 | RSI momentum | momentum | 81.72 | -18.28 | 165 | 10.9 | -90.57 | -30.58 | -90.63 | 2391 |
| 81 | Bollinger breakout | breakout | 81.64 | -18.36 | 178 | 15.2 | -93.94 | -42.02 | -94.11 | 2885 |
| 82 | Trend pullback | trend | 81.14 | -18.86 | 157 | 17.8 | -90.60 | -34.40 | -90.60 | 2296 |
| 83 | ADX DI cross | trend | 80.56 | -19.44 | 174 | 6.3 | -89.33 | -46.79 | -89.62 | 2109 |
| 84 | Connors RSI(2) | reversion | 79.21 | -20.79 | 220 | 15.5 | -96.37 | -42.18 | -96.37 | 3652 |
| 85 | Consensus | meta | 78.48 | -21.52 | 171 | 7.0 | -94.63 | -30.39 | -94.64 | 2658 |
| 86 | EMA 9/21 cross | trend | 78.46 | -21.54 | 238 | 15.1 | -97.37 | -42.48 | -97.44 | 3559 |
| 87 | Candlestick reversal | reversion | 77.77 | -22.23 | 223 | 14.3 | -99.32 | -50.54 | -99.33 | 5546 |
| 88 | Stochastic reversion | reversion | 77.59 | -22.41 | 269 | 22.7 | -95.85 | -47.61 | -95.90 | 4055 |
| 89 | OBV trend | momentum | 77.13 | -22.86 | 240 | 13.8 | -95.89 | -51.21 | -95.92 | 3575 |
| 90 | Bollinger reversion | reversion | 76.48 | -23.52 | 257 | 13.6 | -95.69 | -45.79 | -95.72 | 3677 |
| 91 | VWAP momentum | momentum | 75.99 | -24.01 | 317 | 8.8 | -98.40 | -36.34 | -98.45 | 5228 |
| 92 | CCI reversion | reversion | 74.71 | -25.29 | 184 | 6.0 | -98.42 | -51.29 | -98.43 | 4689 |
| 93 | MACD cross | trend | 73.16 | -26.84 | 215 | 11.2 | -99.70 | -65.75 | -99.70 | 6086 |
| 94 | Williams %R | reversion | 73.10 | -26.90 | 274 | 19.3 | -99.51 | -61.04 | -99.52 | 6100 |
| 95 | Parabolic SAR | trend | 72.91 | -27.09 | 267 | 13.1 | -97.03 | -59.33 | -97.05 | 3663 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.29 | -99.89 | 8348 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T14:41 | Agent (ML meta-label) | buy | XRP-USD | 2.80 | — | entry |
| 2026-09-29T14:41 | Agent (ML meta-label) | buy | TSLA | 4.06 | — | entry |
| 2026-09-29T14:41 | Agent (ML meta-label) | sell | QQQ | 3.74 | -0.00 | selected signal exited |
| 2026-09-29T14:41 | Agent (ML meta-label) | sell | MSTR | 2.43 | -0.01 | selected signal exited |
| 2026-09-29T14:41 | Agent | sell | NVDA | 20.05 | 0.05 | selected signal exited |
| 2026-09-29T14:41 | Bollinger breakout · 1h | buy | ETHU | 4.81 | — | rebalance up |
| 2026-09-29T14:41 | Bollinger breakout · 1h | sell | XRP-USD | 4.81 | -0.01 | rebalance down |
| 2026-09-29T14:41 | CCI reversion | sell | MSFT | 6.82 | 0.11 | exit signal |
| 2026-09-29T14:41 | Williams %R | buy | SQQQ | 4.56 | — | entry signal |
| 2026-09-29T14:41 | VWAP reversion | buy | LABU | 9.47 | — | entry signal |
| 2026-09-29T14:41 | VWAP reversion | sell | NVDA | 9.48 | 0.02 | exit signal |
| 2026-09-29T14:41 | Candlestick reversal | buy | ETH-USD | 2.53 | — | entry signal |
| 2026-09-29T14:41 | Candlestick reversal | buy | BTC-USD | 12.97 | — | entry signal |
| 2026-09-29T14:41 | Candlestick reversal | sell | TSLA | 15.50 | 0.01 | exit signal |
| 2026-09-29T14:41 | Bollinger breakout | buy | MSFT | 8.30 | — | entry signal |
| 2026-09-29T14:41 | Bollinger breakout | sell | TECL | 4.12 | 0.01 | rebalance down |
| 2026-09-29T14:41 | Bollinger breakout | sell | META | 4.18 | -0.02 | rebalance down |
| 2026-09-29T14:41 | OBV trend | buy | TQQQ | 2.45 | — | entry |
| 2026-09-29T14:41 | OBV trend | buy | DOGE-USD | 8.57 | — | entry signal |
| 2026-09-29T14:41 | OBV trend | sell | BITX | 10.95 | -0.13 | exit signal |
| 2026-09-29T14:41 | Trend pullback | buy | ETHU | 8.23 | — | entry signal |
| 2026-09-29T14:41 | Trend pullback | sell | XRP-USD | 4.08 | -0.01 | rebalance down |
| 2026-09-29T14:41 | Trend pullback | sell | NVDA | 4.15 | 0.01 | rebalance down |
| 2026-09-29T14:41 | EMA 20/50 cross | buy | TQQQ | 9.82 | — | entry |
| 2026-09-29T14:41 | EMA 20/50 cross | sell | ETH-USD | 9.82 | 0.10 | exit signal |
| 2026-09-29T14:41 | EMA 9/21 cross | buy | MSFT | 1.13 | — | entry signal |
| 2026-09-29T14:41 | EMA 9/21 cross | buy | AMZN | 7.13 | — | entry signal |
| 2026-09-29T14:41 | EMA 9/21 cross | sell | NVDA | 4.15 | 0.01 | rebalance down |
| 2026-09-29T14:41 | EMA 9/21 cross | sell | META | 4.12 | -0.01 | rebalance down |
| 2026-09-29T14:35 | Agent (ML meta-label) | buy | QQQ | 3.75 | — | entry |
| 2026-09-29T14:35 | Agent (ML meta-label) | sell | COIN | 3.74 | -0.01 | selected signal exited |
| 2026-09-29T14:35 | Agent | sell | MSFT | 20.20 | 0.21 | selected signal exited |
| 2026-09-29T14:35 | CCI reversion | buy | SOL-USD | 6.78 | — | entry |
| 2026-09-29T14:35 | CCI reversion | buy | GOOGL | 6.80 | — | entry signal |
| 2026-09-29T14:35 | CCI reversion | buy | DOGE-USD | 6.80 | — | entry |
| 2026-09-29T14:35 | CCI reversion | buy | AMZN | 6.80 | — | entry |
| 2026-09-29T14:35 | CCI reversion | sell | UPRO | 3.90 | 0.00 | rebalance down |
| 2026-09-29T14:35 | CCI reversion | sell | TSLA | 3.89 | 0.02 | rebalance down |
| 2026-09-29T14:35 | CCI reversion | sell | SQQQ | 3.82 | -0.03 | rebalance down |
| 2026-09-29T14:35 | CCI reversion | sell | SPY | 3.89 | -0.00 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
