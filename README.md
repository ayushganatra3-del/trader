# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-01T09:42:05.000125+00:00 · 7598 ticks

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

Today: 2780 decisions in 556 calls, $0.0391 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-01T09:42 | 1 / 3 / 1 | ETH-USD 18%, BTC-USD 14% |  |
| Breezy | 2026-10-01T09:42 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-01T09:42 | 2 / 3 / 0 | ETH-USD 65% |  |

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
| 2 | Hold BTC | benchmark | 100.40 | 0.40 | 0 | — | 30.91 | 3.85 | -8.68 | 1 |
| 3 | Copy: Congress Democrats (NANC) | copy | 100.25 | 0.25 | 0 | — | 5.20 | 2.18 | -3.62 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 99.76 | -0.24 | 0 | — | -3.22 | -1.93 | -5.09 | 2 |
| 7 | Agent | meta | 99.63 | -0.37 | 27 | 66.7 | -10.23 | -6.78 | -10.80 | 224 |
| 8 | RSI(14) reversion · 1h | reversion | 99.59 | -0.41 | 8 | 62.5 | 4.94 | 1.37 | -7.26 | 129 |
| 9 | Copy: Hedge-fund gurus (GURU) | copy | 99.57 | -0.43 | 0 | — | -2.55 | -1.21 | -5.14 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.52 | -0.48 | 22 | 27.3 | -10.84 | -3.69 | -14.05 | 115 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.65 | 1.34 | -2.11 | 83 |
| 12 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -1.50 | -0.81 | -4.46 | 99 |
| 13 | Hold SPY | benchmark | 99.38 | -0.62 | 0 | — | 2.91 | 1.62 | -3.66 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 15 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 2 | 50.0 | -1.10 | -0.29 | -9.74 | 24 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.38 | -5.16 | 27 |
| 17 | Stochastic reversion · 1h | reversion | 99.04 | -0.96 | 30 | 56.7 | -9.46 | -2.07 | -10.86 | 322 |
| 18 | Copy: Warren Buffett (BRK-B) | copy | 99.01 | -0.99 | 0 | — | -2.22 | -0.86 | -7.65 | 1 |
| 19 | Daily: Bullish score | daily | 98.86 | -1.14 | 3 | 0.0 | -1.05 | 0.05 | -12.76 | 14 |
| 20 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 14.85 | 3.65 | -4.73 | 182 |
| 21 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 98.64 | -1.36 | 0 | — | -10.46 | -2.10 | -15.27 | 2 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.64 | -1.36 | 0 | — | 2.47 | 0.76 | -7.93 | 7 |
| 24 | Copy: Insider buying | copy | 98.55 | -1.45 | 2 | 100.0 | -14.74 | -2.89 | -17.74 | 73 |
| 25 | CCI reversion · 1h | reversion | 98.49 | -1.51 | 42 | 40.5 | 2.01 | 0.50 | -12.41 | 412 |
| 26 | Williams %R · 1h | reversion | 98.49 | -1.51 | 52 | 50.0 | -16.68 | -3.09 | -19.41 | 490 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.54 | 0.27 | -15.21 | 46 |
| 28 | Candlestick reversal · 1h | reversion | 98.25 | -1.75 | 33 | 24.2 | -25.17 | -6.22 | -26.74 | 488 |
| 29 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.58 | -3.31 | -11.47 | 232 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 98.13 | -1.87 | 0 | — | 26.25 | 3.82 | -6.29 | 1 |
| 31 | Z-score reversion · 1h | reversion | 97.99 | -2.01 | 11 | 45.5 | 3.25 | 0.82 | -8.60 | 153 |
| 32 | Agent (rotation) | meta | 97.76 | -2.24 | 37 | 13.5 | -5.27 | -1.80 | -9.79 | 211 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.75 | -2.25 | 0 | — | -7.64 | -1.77 | -10.03 | 1 |
| 34 | Bollinger reversion · 1h | reversion | 97.33 | -2.67 | 32 | 34.4 | -16.70 | -4.63 | -17.69 | 305 |
| 35 | EMA 20/50 cross · 1h | trend | 96.60 | -3.40 | 20 | 5.0 | 15.98 | 1.99 | -12.18 | 130 |
| 36 | Supertrend · 1h | trend | 96.33 | -3.67 | 19 | 5.3 | 0.81 | 0.31 | -16.43 | 203 |
| 37 | Opening range 30m | breakout | 96.12 | -3.88 | 49 | 12.2 | -11.24 | -3.24 | -15.06 | 559 |
| 38 | Agent (ML meta-label) | meta | 95.78 | -4.22 | 173 | 12.7 | 6.77 | 1.31 | -12.11 | 410 |
| 39 | Max aggression: 5-day momentum | meta | 95.73 | -4.27 | 3 | 66.7 | -13.55 | -0.95 | -29.56 | 29 |
| 40 | Donchian 55/20 · 1h | breakout | 95.71 | -4.29 | 15 | 0.0 | 4.59 | 0.79 | -16.96 | 113 |
| 41 | Trend pullback · 1h | trend | 95.63 | -4.38 | 35 | 11.4 | -26.05 | -6.95 | -26.25 | 158 |
| 42 | MFI reversion · 1h | reversion | 95.06 | -4.94 | 51 | 19.6 | -8.65 | -1.54 | -17.05 | 128 |
| 43 | Opening range 15m | breakout | 94.87 | -5.13 | 61 | 14.8 | -12.54 | -3.41 | -17.25 | 687 |
| 44 | Parabolic SAR · 1h | trend | 94.54 | -5.46 | 33 | 12.1 | -9.95 | -1.28 | -19.53 | 305 |
| 45 | Squeeze breakout · 1h | breakout | 94.49 | -5.51 | 16 | 6.2 | 12.09 | 2.12 | -7.61 | 98 |
| 46 | MACD cross · 1h | trend | 94.43 | -5.57 | 47 | 8.5 | -15.22 | -2.42 | -17.62 | 483 |
| 47 | Max aggression: 1-day momentum | meta | 94.37 | -5.63 | 3 | 33.3 | -21.69 | -1.04 | -41.28 | 42 |
| 48 | Three white soldiers | momentum | 94.29 | -5.71 | 52 | 19.2 | -50.12 | -27.33 | -50.12 | 604 |
| 49 | ADX DI cross · 1h | trend | 94.06 | -5.94 | 35 | 5.7 | -16.37 | -3.06 | -17.79 | 262 |
| 50 | Volume breakout · 1h | breakout | 93.79 | -6.21 | 29 | 3.4 | 5.32 | 0.93 | -12.60 | 122 |
| 51 | Ichimoku · 1h | trend | 93.17 | -6.83 | 21 | 14.3 | 4.48 | 0.73 | -15.66 | 121 |
| 52 | RSI momentum · 1h | momentum | 92.75 | -7.25 | 30 | 3.3 | -3.42 | -0.27 | -16.26 | 220 |
| 53 | VWAP momentum · 1h | momentum | 92.56 | -7.44 | 127 | 15.7 | -39.37 | -6.30 | -39.37 | 1257 |
| 54 | Bollinger breakout · 1h | breakout | 92.26 | -7.74 | 25 | 8.0 | 5.06 | 0.85 | -10.56 | 280 |
| 55 | Triple EMA stack · 1h | trend | 91.58 | -8.42 | 40 | 5.0 | -9.46 | -0.96 | -22.69 | 238 |
| 56 | EMA 9/21 cross · 1h | trend | 91.30 | -8.71 | 53 | 9.4 | -8.66 | -1.00 | -17.92 | 323 |
| 57 | MACD zero-line · 1h | trend | 91.27 | -8.73 | 28 | 3.6 | -8.90 | -1.05 | -17.53 | 232 |
| 58 | Heikin-Ashi · 1h | trend | 90.95 | -9.05 | 59 | 8.5 | -29.86 | -4.90 | -32.90 | 688 |
| 59 | Keltner breakout · 1h | breakout | 90.91 | -9.09 | 15 | 0.0 | -8.80 | -1.02 | -20.71 | 218 |
| 60 | RSI(14) reversion | reversion | 90.20 | -9.80 | 140 | 33.6 | -71.40 | -21.15 | -71.53 | 1471 |
| 61 | Donchian 20/10 · 1h | breakout | 90.10 | -9.90 | 23 | 8.7 | -1.38 | 0.04 | -14.99 | 218 |
| 62 | OBV trend · 1h | momentum | 89.24 | -10.76 | 70 | 5.7 | -15.22 | -1.75 | -25.54 | 328 |
| 63 | ROC + volume · 1h | momentum | 86.50 | -13.50 | 62 | 4.8 | -15.26 | -2.03 | -22.31 | 413 |
| 64 | Squeeze breakout | breakout | 86.37 | -13.63 | 115 | 13.0 | -59.40 | -17.96 | -59.50 | 1183 |
| 65 | Donchian 55/20 | breakout | 85.41 | -14.59 | 123 | 19.5 | -67.25 | -15.04 | -67.29 | 1295 |
| 66 | Volume breakout | breakout | 84.58 | -15.42 | 118 | 15.3 | -62.78 | -19.92 | -62.81 | 900 |
| 67 | ROC + volume | momentum | 84.06 | -15.94 | 184 | 20.1 | -72.08 | -17.29 | -72.38 | 1637 |
| 68 | VWAP reversion | reversion | 83.12 | -16.88 | 162 | 25.3 | -71.06 | -17.30 | -71.28 | 1385 |
| 69 | Keltner breakout | breakout | 83.04 | -16.96 | 176 | 14.8 | -84.28 | -32.37 | -84.28 | 1880 |
| 70 | Z-score reversion | reversion | 82.27 | -17.73 | 217 | 30.4 | -84.88 | -27.45 | -84.93 | 2098 |
| 71 | EMA 20/50 cross | trend | 82.09 | -17.91 | 155 | 15.5 | -79.26 | -17.43 | -79.27 | 1472 |
| 72 | AI bee: Bizzy | ai | 81.96 | -18.04 | 297 | 9.1 | — | — | — | — |
| 73 | Ichimoku | trend | 81.76 | -18.24 | 145 | 9.7 | -80.38 | -25.03 | -80.51 | 1748 |
| 74 | AI bee: Boozy | ai | 81.57 | -18.43 | 109 | 0.9 | — | — | — | — |
| 75 | MFI reversion | reversion | 78.61 | -21.39 | 210 | 19.5 | -88.05 | -33.89 | -88.10 | 2134 |
| 76 | Supertrend | trend | 78.42 | -21.58 | 211 | 18.5 | -87.19 | -23.76 | -87.19 | 1936 |
| 77 | Trend pullback | trend | 77.79 | -22.21 | 213 | 16.9 | -91.03 | -32.98 | -91.03 | 2282 |
| 78 | MACD zero-line | trend | 76.97 | -23.03 | 256 | 15.6 | -91.50 | -33.00 | -91.54 | 2350 |
| 79 | Donchian 20/10 | breakout | 76.87 | -23.13 | 258 | 18.6 | -90.54 | -27.91 | -90.55 | 2664 |
| 80 | Triple EMA stack | trend | 76.19 | -23.81 | 263 | 16.0 | -92.88 | -33.77 | -92.89 | 2593 |
| 81 | Bollinger breakout | breakout | 75.64 | -24.36 | 261 | 15.7 | -93.72 | -38.63 | -93.73 | 2841 |
| 82 | RSI momentum | momentum | 75.63 | -24.37 | 248 | 14.9 | -90.17 | -27.57 | -90.17 | 2372 |
| 83 | ADX DI cross | trend | 75.49 | -24.51 | 240 | 7.9 | -89.36 | -41.46 | -89.41 | 2107 |
| 84 | Stochastic reversion | reversion | 72.80 | -27.20 | 401 | 23.7 | -95.76 | -43.18 | -95.76 | 4026 |
| 85 | Consensus | meta | 72.75 | -27.25 | 231 | 7.4 | -94.72 | -29.45 | -94.72 | 2664 |
| 86 | Connors RSI(2) | reversion | 72.37 | -27.63 | 319 | 19.7 | -96.53 | -39.73 | -96.53 | 3645 |
| 87 | EMA 9/21 cross | trend | 70.78 | -29.22 | 353 | 16.1 | -97.32 | -38.81 | -97.32 | 3532 |
| 88 | Bollinger reversion | reversion | 70.39 | -29.61 | 382 | 16.5 | -95.89 | -43.20 | -95.89 | 3688 |
| 89 | Candlestick reversal | reversion | 70.36 | -29.64 | 388 | 13.9 | -99.35 | -47.84 | -99.35 | 5595 |
| 90 | OBV trend | momentum | 69.72 | -30.28 | 364 | 15.9 | -95.97 | -44.22 | -95.97 | 3560 |
| 91 | CCI reversion | reversion | 68.81 | -31.19 | 335 | 13.1 | -98.49 | -47.92 | -98.50 | 4690 |
| 92 | Parabolic SAR | trend | 68.35 | -31.65 | 337 | 13.1 | -96.98 | -50.43 | -96.98 | 3627 |
| 93 | VWAP momentum | momentum | 67.33 | -32.67 | 421 | 9.0 | -98.61 | -35.68 | -98.61 | 5273 |
| 94 | MACD cross | trend | 66.98 | -33.02 | 375 | 13.9 | -99.71 | -57.27 | -99.71 | 6067 |
| 95 | Williams %R | reversion | 65.85 | -34.15 | 456 | 21.3 | -99.53 | -53.96 | -99.53 | 6100 |
| 96 | Heikin-Ashi | trend | 65.82 | -34.18 | 333 | 6.3 | -99.89 | -67.91 | -99.89 | 8282 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-01T09:41 | AI bee: Bizzy | buy | BTC-USD | 11.88 | — | Jev: buy (buy p=0.58) |
| 2026-10-01T09:41 | EMA 9/21 cross | buy | SOL-USD | 3.53 | — | rebalance up |
| 2026-10-01T09:41 | EMA 9/21 cross | sell | ETH-USD | 3.53 | -0.02 | rebalance down |
| 2026-10-01T09:40 | Z-score reversion | buy | XRP-USD | 4.13 | — | rebalance up |
| 2026-10-01T09:40 | Z-score reversion | buy | SOL-USD | 4.15 | — | rebalance up |
| 2026-10-01T09:40 | Z-score reversion | sell | BTC-USD | 16.41 | 0.00 | exit signal |
| 2026-10-01T09:40 | RSI momentum | buy | ETH-USD | 18.93 | — | entry signal |
| 2026-10-01T09:40 | RSI momentum | buy | BTC-USD | 18.93 | — | entry signal |
| 2026-10-01T09:40 | MACD zero-line | buy | ETH-USD | 19.26 | — | entry signal |
| 2026-10-01T09:40 | EMA 9/21 cross | buy | SOL-USD | 7.14 | — | entry signal |
| 2026-10-01T09:40 | EMA 9/21 cross | buy | DOGE-USD | 14.18 | — | entry signal |
| 2026-10-01T09:40 | EMA 9/21 cross | sell | BTC-USD | 3.54 | -0.02 | rebalance down |
| 2026-10-01T09:35 | AI bee: Boozy | buy | ETH-USD | 53.08 | — | Jev: buy (buy p=0.65) |
| 2026-10-01T09:35 | AI bee: Boozy | sell | BTC-USD | 44.86 | -0.22 | Jev: add (buy p=0.55) |
| 2026-10-01T09:35 | MFI reversion | sell | BTC-USD | 19.66 | 0.04 | exit signal |
| 2026-10-01T09:35 | Donchian 20/10 | buy | SOL-USD | 19.23 | — | entry signal |
| 2026-10-01T09:35 | ROC + volume | buy | ETH-USD | 21.04 | — | entry signal |
| 2026-10-01T09:35 | ROC + volume | buy | BTC-USD | 21.04 | — | entry signal |
| 2026-10-01T09:35 | VWAP momentum | buy | ETH-USD | 16.84 | — | entry signal |
| 2026-10-01T09:35 | Heikin-Ashi | buy | SOL-USD | 16.42 | — | entry signal |
| 2026-10-01T09:35 | ADX DI cross | buy | SOL-USD | 18.89 | — | entry signal |
| 2026-10-01T09:35 | Supertrend | buy | ETH-USD | 19.62 | — | entry signal |
| 2026-10-01T09:35 | MACD zero-line | buy | BTC-USD | 19.27 | — | entry signal |
| 2026-10-01T09:35 | EMA 9/21 cross | buy | XRP-USD | 17.73 | — | entry signal |
| 2026-10-01T09:33 | AI bee: Bizzy | buy | ETH-USD | 14.74 | — | Jev: buy (buy p=0.72) |
| 2026-10-01T09:30 | RSI(14) reversion | sell | ETH-USD | 18.12 | 0.06 | exit signal |
| 2026-10-01T09:30 | Donchian 20/10 | buy | ETH-USD | 19.24 | — | entry signal |
| 2026-10-01T09:30 | Supertrend | buy | BTC-USD | 19.63 | — | entry signal |
| 2026-10-01T09:30 | EMA 9/21 cross | buy | ETH-USD | 17.74 | — | entry signal |
| 2026-10-01T09:25 | Heikin-Ashi | sell | XRP-USD | 16.38 | -0.05 | exit signal |
| 2026-10-01T09:25 | ADX DI cross | buy | ETH-USD | 18.89 | — | entry signal |
| 2026-10-01T09:25 | EMA 9/21 cross | buy | BTC-USD | 17.75 | — | entry signal |
| 2026-10-01T09:20 | RSI(14) reversion | buy | XRP-USD | 4.62 | — | rebalance up |
| 2026-10-01T09:20 | RSI(14) reversion | buy | SOL-USD | 4.53 | — | rebalance up |
| 2026-10-01T09:20 | RSI(14) reversion | sell | BTC-USD | 17.97 | -0.03 | exit signal |
| 2026-10-01T09:20 | Candlestick reversal | sell | ETH-USD | 17.54 | -0.03 | exit signal |
| 2026-10-01T09:20 | VWAP momentum | buy | BTC-USD | 16.85 | — | entry signal |
| 2026-10-01T09:19 | AI bee: Boozy | buy | BTC-USD | 45.08 | — | Jev: buy (buy p=0.55) |
| 2026-10-01T09:19 | AI bee: Boozy | sell | ETH-USD | 44.33 | -0.02 | Jev: buy |
| 2026-10-01T09:16 | AI bee: Bizzy | sell | XRP-USD | 12.04 | -0.04 | Jev: sell (sell p=0.79) after 10 min |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
