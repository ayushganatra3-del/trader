# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T18:10:05.000200+00:00 · 5962 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.98 (-0.02%)

Closed trades 23, win rate 69.6%, fees £0.68, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 39.99 | +0.04 |

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

Today: 29691 decisions in 2648 calls, $0.3703 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T18:10 | 2 / 13 / 14 | ETHU 16% |  |
| Breezy | 2026-09-29T18:10 | 0 / 24 / 5 | cash |  |
| Boozy | 2026-09-29T18:10 | 5 / 22 / 2 | ETHU 36%, BITX 34% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 102.00 | 2.00 | 1 | 100.0 | 14.72 | 3.19 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.76 | 1.46 | -7.93 | 7 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Agent | meta | 99.98 | -0.02 | 23 | 69.6 | -9.67 | -6.47 | -10.68 | 213 |
| 8 | Agent (aggressive) | meta | 99.97 | -0.03 | 9 | 55.6 | 0.27 | 0.21 | -3.92 | 94 |
| 9 | Copy: Congress Democrats (NANC) | copy | 99.91 | -0.09 | 0 | — | 6.59 | 2.72 | -3.62 | 1 |
| 10 | Hold BTC | benchmark | 99.78 | -0.22 | 0 | — | 29.27 | 3.69 | -8.68 | 1 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 99.76 | -0.24 | 0 | — | -1.37 | -0.52 | -7.65 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.54 | 1.82 | -1.51 | 83 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 99.50 | -0.50 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 14 | Hold SPY | benchmark | 99.49 | -0.51 | 0 | — | 3.21 | 1.63 | -3.66 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.37 | -0.63 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 16 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -13.00 | -4.42 | -14.85 | 121 |
| 17 | RSI(14) reversion · 1h | reversion | 99.23 | -0.77 | 7 | 57.1 | 5.48 | 1.36 | -6.57 | 126 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | Daily: Bullish score | daily | 98.82 | -1.18 | 2 | 0.0 | -1.86 | -0.07 | -12.76 | 13 |
| 20 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 21 | Z-score reversion · 1h | reversion | 98.72 | -1.28 | 10 | 50.0 | 4.28 | 1.05 | -8.60 | 153 |
| 22 | Williams %R · 1h | reversion | 98.69 | -1.31 | 40 | 45.0 | -19.03 | -3.56 | -20.46 | 480 |
| 23 | Candlestick reversal · 1h | reversion | 98.51 | -1.49 | 19 | 26.3 | -28.75 | -6.97 | -29.30 | 492 |
| 24 | Copy: Insider buying | copy | 98.50 | -1.50 | 2 | 100.0 | -14.72 | -2.94 | -17.74 | 72 |
| 25 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.39 | 3.81 | -4.73 | 195 |
| 26 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -2.17 | -0.16 | -15.21 | 47 |
| 27 | Max aggression: 5-day momentum | meta | 98.33 | -1.67 | 2 | 50.0 | -8.13 | -0.40 | -29.56 | 29 |
| 28 | CCI reversion · 1h | reversion | 98.20 | -1.80 | 35 | 34.3 | 2.10 | 0.52 | -12.41 | 405 |
| 29 | Agent (rotation) | meta | 98.16 | -1.84 | 32 | 12.5 | -4.99 | -1.68 | -11.62 | 213 |
| 30 | Stochastic reversion · 1h | reversion | 98.16 | -1.84 | 26 | 53.8 | -13.67 | -3.06 | -14.47 | 323 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 98.09 | -1.91 | 0 | — | 22.56 | 3.26 | -6.29 | 1 |
| 32 | EMA 20/50 cross · 1h | trend | 97.70 | -2.30 | 10 | 10.0 | 15.44 | 1.87 | -14.36 | 127 |
| 33 | Connors RSI(2) · 1h | reversion | 97.69 | -2.31 | 41 | 46.3 | -13.07 | -4.12 | -13.13 | 235 |
| 34 | Timing: Nasdaq FTD · TQQQ | daily | 97.41 | -2.59 | 0 | — | -11.61 | -2.41 | -15.27 | 2 |
| 35 | Daily: SMA 20/50 cross · AAPL | daily | 97.22 | -2.78 | 0 | — | -10.81 | -2.65 | -12.65 | 1 |
| 36 | Opening range 30m | breakout | 97.21 | -2.79 | 35 | 11.4 | -8.97 | -2.58 | -14.21 | 563 |
| 37 | Squeeze breakout · 1h | breakout | 97.19 | -2.81 | 9 | 11.1 | 14.03 | 2.48 | -6.88 | 97 |
| 38 | Bollinger reversion · 1h | reversion | 96.96 | -3.04 | 22 | 27.3 | -18.21 | -5.10 | -18.45 | 312 |
| 39 | Supertrend · 1h | trend | 96.69 | -3.31 | 18 | 5.6 | 3.11 | 0.62 | -16.43 | 198 |
| 40 | Agent (ML meta-label) | meta | 96.37 | -3.63 | 130 | 10.8 | -6.08 | -1.06 | -13.31 | 401 |
| 41 | Trend pullback · 1h | trend | 96.23 | -3.77 | 26 | 11.5 | -25.93 | -6.88 | -26.54 | 146 |
| 42 | MACD cross · 1h | trend | 96.15 | -3.85 | 39 | 10.3 | -15.89 | -2.54 | -19.05 | 460 |
| 43 | Donchian 55/20 · 1h | breakout | 96.12 | -3.88 | 12 | 0.0 | 4.67 | 0.82 | -16.96 | 112 |
| 44 | Max aggression: 1-day momentum | meta | 95.75 | -4.25 | 2 | 0.0 | -38.64 | -2.32 | -49.44 | 42 |
| 45 | Parabolic SAR · 1h | trend | 95.72 | -4.28 | 26 | 11.5 | -8.83 | -1.13 | -18.82 | 293 |
| 46 | Opening range 15m | breakout | 95.61 | -4.39 | 46 | 10.9 | -10.97 | -2.96 | -16.91 | 696 |
| 47 | Ichimoku · 1h | trend | 95.35 | -4.65 | 15 | 13.3 | 7.02 | 1.01 | -15.13 | 122 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -51.31 | -28.11 | -51.45 | 611 |
| 49 | Bollinger breakout · 1h | breakout | 95.18 | -4.82 | 17 | 5.9 | 7.81 | 1.21 | -10.18 | 284 |
| 50 | MFI reversion · 1h | reversion | 95.16 | -4.84 | 43 | 11.6 | -10.27 | -1.90 | -17.27 | 128 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 1.00 | -12.60 | 125 |
| 52 | ADX DI cross · 1h | trend | 94.54 | -5.46 | 29 | 6.9 | -16.18 | -3.08 | -18.17 | 256 |
| 53 | MACD zero-line · 1h | trend | 94.46 | -5.54 | 20 | 5.0 | -5.71 | -0.62 | -14.64 | 223 |
| 54 | RSI momentum · 1h | momentum | 94.44 | -5.56 | 24 | 4.2 | -0.26 | 0.16 | -15.29 | 216 |
| 55 | Donchian 20/10 · 1h | breakout | 94.23 | -5.77 | 15 | 13.3 | 7.69 | 1.17 | -12.78 | 214 |
| 56 | Triple EMA stack · 1h | trend | 94.11 | -5.89 | 29 | 6.9 | -6.43 | -0.57 | -22.88 | 226 |
| 57 | Keltner breakout · 1h | breakout | 94.05 | -5.95 | 9 | 0.0 | -6.04 | -0.63 | -18.68 | 215 |
| 58 | VWAP momentum · 1h | momentum | 93.99 | -6.01 | 102 | 12.7 | -32.71 | -4.88 | -35.44 | 1228 |
| 59 | EMA 9/21 cross · 1h | trend | 93.42 | -6.58 | 42 | 11.9 | -4.72 | -0.45 | -16.92 | 310 |
| 60 | Heikin-Ashi · 1h | trend | 92.89 | -7.11 | 43 | 11.6 | -23.46 | -3.52 | -30.54 | 678 |
| 61 | OBV trend · 1h | momentum | 92.88 | -7.12 | 53 | 7.5 | -9.38 | -0.98 | -25.24 | 326 |
| 62 | RSI(14) reversion | reversion | 90.95 | -9.05 | 108 | 35.2 | -71.13 | -21.65 | -71.21 | 1477 |
| 63 | Squeeze breakout | breakout | 89.76 | -10.24 | 81 | 9.9 | -59.76 | -18.55 | -60.03 | 1182 |
| 64 | ROC + volume · 1h | momentum | 89.45 | -10.55 | 51 | 5.9 | -4.94 | -0.43 | -19.17 | 406 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | EMA 20/50 cross | trend | 87.80 | -12.20 | 107 | 15.0 | -78.59 | -17.54 | -78.76 | 1470 |
| 68 | Volume breakout | breakout | 87.51 | -12.49 | 91 | 12.1 | -61.99 | -20.56 | -62.08 | 891 |
| 69 | ROC + volume | momentum | 87.50 | -12.50 | 135 | 17.0 | -72.48 | -18.16 | -72.52 | 1609 |
| 70 | Donchian 55/20 | breakout | 87.49 | -12.51 | 91 | 14.3 | -68.41 | -15.70 | -68.52 | 1305 |
| 71 | Ichimoku | trend | 86.14 | -13.86 | 106 | 8.5 | -80.39 | -26.22 | -80.41 | 1761 |
| 72 | Keltner breakout | breakout | 85.76 | -14.24 | 138 | 11.6 | -84.85 | -35.21 | -84.93 | 1901 |
| 73 | Z-score reversion | reversion | 85.06 | -14.94 | 170 | 31.8 | -84.37 | -27.65 | -84.41 | 2091 |
| 74 | VWAP reversion | reversion | 84.65 | -15.35 | 124 | 18.5 | -71.97 | -17.73 | -72.21 | 1404 |
| 75 | MACD zero-line | trend | 83.42 | -16.59 | 175 | 14.9 | -91.69 | -36.30 | -91.73 | 2343 |
| 76 | Supertrend | trend | 82.84 | -17.16 | 159 | 16.4 | -87.41 | -24.93 | -87.42 | 1959 |
| 77 | MFI reversion | reversion | 81.65 | -18.35 | 171 | 19.3 | -87.72 | -35.98 | -87.78 | 2165 |
| 78 | Donchian 20/10 | breakout | 81.60 | -18.41 | 180 | 16.7 | -90.77 | -29.87 | -90.82 | 2673 |
| 79 | Bollinger breakout | breakout | 81.22 | -18.78 | 187 | 14.4 | -93.97 | -42.12 | -93.99 | 2856 |
| 80 | Triple EMA stack | trend | 81.18 | -18.82 | 194 | 14.4 | -93.05 | -36.52 | -93.08 | 2612 |
| 81 | RSI momentum | momentum | 80.94 | -19.06 | 174 | 11.5 | -90.48 | -29.79 | -90.53 | 2383 |
| 82 | ADX DI cross | trend | 79.98 | -20.02 | 182 | 6.6 | -89.40 | -47.62 | -89.40 | 2101 |
| 83 | Trend pullback | trend | 79.79 | -20.21 | 166 | 17.5 | -90.93 | -35.26 | -90.93 | 2285 |
| 84 | EMA 9/21 cross | trend | 78.09 | -21.91 | 252 | 15.1 | -97.34 | -41.76 | -97.35 | 3541 |
| 85 | Connors RSI(2) | reversion | 77.10 | -22.89 | 238 | 16.0 | -96.49 | -43.13 | -96.49 | 3647 |
| 86 | Consensus | meta | 77.10 | -22.90 | 182 | 7.1 | -94.69 | -30.81 | -94.70 | 2648 |
| 87 | Stochastic reversion | reversion | 76.52 | -23.48 | 312 | 23.7 | -95.98 | -48.80 | -95.99 | 4070 |
| 88 | Candlestick reversal ⏸ | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.34 | -51.72 | -99.35 | 5592 |
| 89 | OBV trend | momentum | 76.01 | -23.99 | 253 | 14.2 | -95.93 | -49.49 | -95.94 | 3532 |
| 90 | Bollinger reversion | reversion | 75.18 | -24.82 | 294 | 15.0 | -95.76 | -45.73 | -95.77 | 3689 |
| 91 | VWAP momentum | momentum | 74.33 | -25.67 | 349 | 9.7 | -98.42 | -36.33 | -98.44 | 5174 |
| 92 | CCI reversion | reversion | 73.94 | -26.06 | 217 | 9.7 | -98.46 | -52.73 | -98.46 | 4702 |
| 93 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -97.00 | -57.02 | -97.00 | 3652 |
| 94 | MACD cross | trend | 72.55 | -27.45 | 241 | 12.0 | -99.71 | -67.69 | -99.71 | 6083 |
| 95 | Williams %R | reversion | 71.89 | -28.11 | 325 | 20.0 | -99.53 | -62.61 | -99.53 | 6106 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -88.16 | -99.89 | 8303 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T18:10 | Agent (ML meta-label) | buy | TQQQ | 6.42 | — | following Candlestick reversal |
| 2026-09-29T18:10 | CCI reversion | sell | UPRO | 4.62 | -0.01 | exit signal |
| 2026-09-29T18:10 | CCI reversion | sell | ETHU | 3.72 | 0.02 | exit signal |
| 2026-09-29T18:10 | CCI reversion | sell | ETH-USD | 3.69 | -0.01 | exit signal |
| 2026-09-29T18:10 | Williams %R | buy | SQQQ | 6.54 | — | entry signal |
| 2026-09-29T18:10 | Volume breakout | sell | SPY | 14.58 | -0.03 | exit signal |
| 2026-09-29T18:10 | Donchian 20/10 | sell | AAPL | 9.06 | -0.04 | stop-loss |
| 2026-09-29T18:10 | VWAP momentum | buy | META | 3.73 | — | rebalance up |
| 2026-09-29T18:10 | VWAP momentum | buy | AMZN | 3.74 | — | rebalance up |
| 2026-09-29T18:10 | VWAP momentum | sell | TSLA | 14.84 | -0.03 | exit signal |
| 2026-09-29T18:10 | Ichimoku | buy | AMZN | 21.54 | — | entry signal |
| 2026-09-29T18:10 | ADX DI cross | buy | SOL-USD | 13.34 | — | entry signal |
| 2026-09-29T18:10 | ADX DI cross | buy | ETHU | 13.35 | — | entry signal |
| 2026-09-29T18:10 | ADX DI cross | buy | BTC-USD | 13.35 | — | entry signal |
| 2026-09-29T18:10 | ADX DI cross | sell | UPRO | 6.65 | -0.02 | rebalance down |
| 2026-09-29T18:10 | ADX DI cross | sell | TSLA | 6.71 | 0.01 | rebalance down |
| 2026-09-29T18:10 | ADX DI cross | sell | BITX | 6.68 | -0.01 | rebalance down |
| 2026-09-29T18:10 | MACD cross | sell | AMZN | 3.81 | -0.01 | exit signal |
| 2026-09-29T18:10 | EMA 9/21 cross | buy | TSLA | 3.16 | — | entry signal |
| 2026-09-29T18:10 | EMA 9/21 cross | buy | TNA | 9.77 | — | entry signal |
| 2026-09-29T18:10 | EMA 9/21 cross | buy | IWM | 9.77 | — | entry signal |
| 2026-09-29T18:10 | EMA 9/21 cross | buy | BITX | 9.77 | — | entry signal |
| 2026-09-29T18:10 | EMA 9/21 cross | sell | SQQQ | 5.79 | 0.00 | rebalance down |
| 2026-09-29T18:10 | EMA 9/21 cross | sell | LABU | 5.92 | 0.09 | rebalance down |
| 2026-09-29T18:10 | EMA 9/21 cross | sell | AAPL | 15.53 | -0.07 | stop-loss |
| 2026-09-29T18:05 | Agent (ML meta-label) | buy | TNA | 6.89 | — | entry |
| 2026-09-29T18:05 | Agent (ML meta-label) | sell | TQQQ | 6.67 | 0.03 | selected signal exited |
| 2026-09-29T18:05 | Agent (ML meta-label) | sell | PLTR | 3.26 | -0.00 | selected signal exited |
| 2026-09-29T18:05 | Consensus | sell | SQQQ | 19.18 | -0.10 | target is flat |
| 2026-09-29T18:05 | Agent | buy | AMD | 19.96 | — | rebalance up |
| 2026-09-29T18:05 | MACD cross · 1h | buy | SQQQ | 4.61 | — | rebalance up |
| 2026-09-29T18:05 | MFI reversion | buy | NVDA | 10.21 | — | entry signal |
| 2026-09-29T18:05 | MFI reversion | sell | TNA | 10.31 | 0.02 | exit signal |
| 2026-09-29T18:05 | CCI reversion | buy | UPRO | 4.63 | — | entry signal |
| 2026-09-29T18:05 | CCI reversion | buy | SOL-USD | 4.63 | — | entry signal |
| 2026-09-29T18:05 | CCI reversion | buy | MSTR | 4.63 | — | entry signal |
| 2026-09-29T18:05 | CCI reversion | buy | GOOGL | 4.63 | — | entry signal |
| 2026-09-29T18:05 | CCI reversion | buy | COIN | 4.63 | — | entry signal |
| 2026-09-29T18:05 | CCI reversion | buy | AMD | 4.63 | — | entry signal |
| 2026-09-29T18:05 | CCI reversion | sell | TSLA | 5.72 | 0.01 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
