# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-01T10:40:05.000152+00:00 · 7642 ticks

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

Today: 3440 decisions in 688 calls, $0.0484 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-01T10:40 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-01T10:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-01T10:40 | 0 / 5 / 0 | ETH-USD 65% |  |

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
| 2 | Hold BTC | benchmark | 100.35 | 0.35 | 0 | — | 30.83 | 3.84 | -8.68 | 1 |
| 3 | Copy: Congress Democrats (NANC) | copy | 100.33 | 0.33 | 0 | — | 5.20 | 2.18 | -3.62 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 99.84 | -0.16 | 0 | — | -3.22 | -1.93 | -5.09 | 2 |
| 7 | Copy: Hedge-fund gurus (GURU) | copy | 99.66 | -0.34 | 0 | — | -2.55 | -1.21 | -5.14 | 1 |
| 8 | RSI(14) reversion · 1h | reversion | 99.63 | -0.37 | 8 | 62.5 | 4.28 | 1.20 | -7.26 | 133 |
| 9 | Agent | meta | 99.63 | -0.37 | 27 | 66.7 | -10.23 | -6.78 | -10.80 | 224 |
| 10 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -10.76 | -3.66 | -14.05 | 114 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.65 | 1.34 | -2.11 | 83 |
| 12 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -1.50 | -0.81 | -4.46 | 99 |
| 13 | Hold SPY | benchmark | 99.46 | -0.54 | 0 | — | 2.91 | 1.62 | -3.66 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 15 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 2 | 50.0 | -1.10 | -0.29 | -9.74 | 24 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.38 | -5.16 | 27 |
| 17 | Stochastic reversion · 1h | reversion | 99.11 | -0.89 | 30 | 56.7 | -9.49 | -2.08 | -10.86 | 322 |
| 18 | Copy: Warren Buffett (BRK-B) | copy | 99.09 | -0.91 | 0 | — | -2.22 | -0.86 | -7.65 | 1 |
| 19 | Daily: Bullish score | daily | 98.95 | -1.05 | 3 | 0.0 | -1.05 | 0.05 | -12.76 | 14 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 98.72 | -1.28 | 0 | — | -10.46 | -2.10 | -15.27 | 2 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.72 | -1.28 | 0 | — | 2.47 | 0.76 | -7.93 | 7 |
| 22 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 15.10 | 3.71 | -4.73 | 182 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 24 | Copy: Insider buying | copy | 98.64 | -1.36 | 2 | 100.0 | -14.74 | -2.89 | -17.74 | 73 |
| 25 | CCI reversion · 1h | reversion | 98.55 | -1.45 | 42 | 40.5 | 1.92 | 0.48 | -12.41 | 413 |
| 26 | Williams %R · 1h | reversion | 98.52 | -1.48 | 52 | 50.0 | -16.72 | -3.10 | -19.41 | 490 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.54 | 0.27 | -15.21 | 46 |
| 28 | Candlestick reversal · 1h | reversion | 98.32 | -1.68 | 33 | 24.2 | -25.70 | -6.39 | -26.74 | 491 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 98.21 | -1.79 | 0 | — | 26.25 | 3.82 | -6.29 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.58 | -3.31 | -11.47 | 232 |
| 31 | Z-score reversion · 1h | reversion | 98.07 | -1.93 | 11 | 45.5 | 3.25 | 0.82 | -8.60 | 153 |
| 32 | Daily: SMA 20/50 cross · AAPL | daily | 97.83 | -2.17 | 0 | — | -7.64 | -1.77 | -10.03 | 1 |
| 33 | Agent (rotation) | meta | 97.76 | -2.24 | 37 | 13.5 | -5.20 | -1.78 | -9.79 | 211 |
| 34 | Bollinger reversion · 1h | reversion | 97.41 | -2.59 | 32 | 34.4 | -16.72 | -4.64 | -17.72 | 305 |
| 35 | EMA 20/50 cross · 1h | trend | 96.66 | -3.34 | 20 | 5.0 | 15.95 | 1.99 | -12.18 | 130 |
| 36 | Supertrend · 1h | trend | 96.34 | -3.66 | 19 | 5.3 | 0.76 | 0.30 | -16.43 | 203 |
| 37 | Opening range 30m | breakout | 96.12 | -3.88 | 49 | 12.2 | -11.24 | -3.24 | -15.06 | 559 |
| 38 | Agent (ML meta-label) | meta | 95.83 | -4.17 | 173 | 12.7 | 6.79 | 1.23 | -11.99 | 416 |
| 39 | Max aggression: 5-day momentum | meta | 95.81 | -4.19 | 3 | 66.7 | -13.55 | -0.95 | -29.56 | 29 |
| 40 | Donchian 55/20 · 1h | breakout | 95.79 | -4.21 | 15 | 0.0 | 4.59 | 0.79 | -16.96 | 113 |
| 41 | Trend pullback · 1h | trend | 95.66 | -4.34 | 35 | 11.4 | -26.40 | -7.03 | -26.63 | 159 |
| 42 | MFI reversion · 1h | reversion | 94.92 | -5.08 | 52 | 19.2 | -8.81 | -1.57 | -17.05 | 128 |
| 43 | Opening range 15m | breakout | 94.87 | -5.13 | 61 | 14.8 | -12.31 | -3.35 | -17.03 | 686 |
| 44 | Parabolic SAR · 1h | trend | 94.59 | -5.41 | 33 | 12.1 | -10.25 | -1.33 | -19.53 | 306 |
| 45 | Squeeze breakout · 1h | breakout | 94.49 | -5.51 | 16 | 6.2 | 12.09 | 2.12 | -7.61 | 98 |
| 46 | MACD cross · 1h | trend | 94.48 | -5.52 | 48 | 10.4 | -15.07 | -2.39 | -17.47 | 482 |
| 47 | Max aggression: 1-day momentum | meta | 94.45 | -5.55 | 3 | 33.3 | -21.69 | -1.04 | -41.28 | 42 |
| 48 | Three white soldiers | momentum | 94.29 | -5.71 | 52 | 19.2 | -50.12 | -27.33 | -50.12 | 604 |
| 49 | ADX DI cross · 1h | trend | 94.14 | -5.86 | 35 | 5.7 | -16.23 | -3.03 | -17.79 | 261 |
| 50 | Volume breakout · 1h | breakout | 93.79 | -6.21 | 29 | 3.4 | 5.32 | 0.93 | -12.60 | 122 |
| 51 | Ichimoku · 1h | trend | 93.22 | -6.78 | 21 | 14.3 | 4.48 | 0.73 | -15.66 | 121 |
| 52 | RSI momentum · 1h | momentum | 92.81 | -7.19 | 30 | 3.3 | -3.48 | -0.27 | -16.26 | 220 |
| 53 | VWAP momentum · 1h | momentum | 92.64 | -7.36 | 127 | 15.7 | -39.37 | -6.30 | -39.37 | 1257 |
| 54 | Bollinger breakout · 1h | breakout | 92.29 | -7.71 | 25 | 8.0 | 5.06 | 0.85 | -10.56 | 280 |
| 55 | Triple EMA stack · 1h | trend | 91.65 | -8.35 | 40 | 5.0 | -9.59 | -0.98 | -22.71 | 238 |
| 56 | EMA 9/21 cross · 1h | trend | 91.31 | -8.69 | 53 | 9.4 | -8.56 | -0.98 | -17.94 | 322 |
| 57 | MACD zero-line · 1h | trend | 91.20 | -8.80 | 29 | 6.9 | -9.03 | -1.06 | -17.53 | 232 |
| 58 | Heikin-Ashi · 1h | trend | 91.02 | -8.98 | 59 | 8.5 | -29.87 | -4.90 | -32.92 | 688 |
| 59 | Keltner breakout · 1h | breakout | 90.92 | -9.07 | 15 | 0.0 | -8.68 | -1.00 | -20.71 | 218 |
| 60 | Donchian 20/10 · 1h | breakout | 90.13 | -9.87 | 23 | 8.7 | -1.38 | 0.04 | -14.99 | 218 |
| 61 | RSI(14) reversion | reversion | 90.07 | -9.93 | 141 | 34.0 | -71.58 | -21.34 | -71.67 | 1472 |
| 62 | OBV trend · 1h | momentum | 89.28 | -10.72 | 70 | 5.7 | -15.12 | -1.73 | -25.58 | 328 |
| 63 | ROC + volume · 1h | momentum | 86.56 | -13.44 | 62 | 4.8 | -15.26 | -2.03 | -22.31 | 413 |
| 64 | Squeeze breakout | breakout | 86.37 | -13.63 | 115 | 13.0 | -59.38 | -17.96 | -59.49 | 1183 |
| 65 | Donchian 55/20 | breakout | 85.41 | -14.59 | 123 | 19.5 | -67.28 | -15.05 | -67.32 | 1295 |
| 66 | Volume breakout | breakout | 84.58 | -15.42 | 118 | 15.3 | -62.78 | -19.92 | -62.81 | 900 |
| 67 | ROC + volume | momentum | 83.71 | -16.29 | 186 | 19.9 | -72.19 | -17.36 | -72.49 | 1637 |
| 68 | VWAP reversion | reversion | 83.07 | -16.93 | 162 | 25.3 | -71.18 | -17.39 | -71.33 | 1385 |
| 69 | Keltner breakout | breakout | 83.04 | -16.96 | 176 | 14.8 | -84.25 | -32.25 | -84.25 | 1879 |
| 70 | Z-score reversion | reversion | 82.10 | -17.90 | 218 | 30.7 | -84.86 | -27.38 | -84.94 | 2095 |
| 71 | EMA 20/50 cross | trend | 82.09 | -17.91 | 155 | 15.5 | -79.23 | -17.41 | -79.23 | 1471 |
| 72 | AI bee: Bizzy | ai | 81.88 | -18.12 | 299 | 9.0 | — | — | — | — |
| 73 | Ichimoku | trend | 81.76 | -18.24 | 145 | 9.7 | -80.38 | -25.03 | -80.51 | 1748 |
| 74 | AI bee: Boozy | ai | 81.55 | -18.45 | 109 | 0.9 | — | — | — | — |
| 75 | MFI reversion | reversion | 78.51 | -21.49 | 210 | 19.5 | -88.04 | -33.89 | -88.10 | 2132 |
| 76 | Supertrend | trend | 78.10 | -21.90 | 213 | 18.3 | -87.27 | -23.91 | -87.27 | 1937 |
| 77 | Trend pullback | trend | 77.79 | -22.21 | 213 | 16.9 | -91.02 | -32.90 | -91.02 | 2281 |
| 78 | MACD zero-line | trend | 76.65 | -23.35 | 258 | 15.5 | -91.48 | -32.83 | -91.54 | 2347 |
| 79 | Donchian 20/10 | breakout | 76.44 | -23.56 | 261 | 18.4 | -90.56 | -27.96 | -90.59 | 2663 |
| 80 | Triple EMA stack | trend | 76.19 | -23.81 | 263 | 16.0 | -92.88 | -33.77 | -92.88 | 2593 |
| 81 | Bollinger breakout | breakout | 75.64 | -24.36 | 261 | 15.7 | -93.68 | -38.42 | -93.71 | 2839 |
| 82 | RSI momentum | momentum | 75.31 | -24.69 | 250 | 14.8 | -90.21 | -27.69 | -90.21 | 2372 |
| 83 | ADX DI cross | trend | 75.15 | -24.85 | 243 | 7.8 | -89.41 | -41.97 | -89.45 | 2106 |
| 84 | Stochastic reversion | reversion | 72.80 | -27.20 | 401 | 23.7 | -95.75 | -43.04 | -95.75 | 4026 |
| 85 | Consensus | meta | 72.75 | -27.25 | 231 | 7.4 | -94.67 | -29.56 | -94.67 | 2660 |
| 86 | Connors RSI(2) | reversion | 72.19 | -27.81 | 320 | 19.7 | -96.54 | -39.80 | -96.54 | 3645 |
| 87 | Bollinger reversion | reversion | 70.38 | -29.62 | 383 | 16.4 | -95.89 | -43.17 | -95.90 | 3690 |
| 88 | EMA 9/21 cross | trend | 70.12 | -29.88 | 358 | 15.9 | -97.33 | -38.97 | -97.34 | 3531 |
| 89 | Candlestick reversal | reversion | 69.93 | -30.07 | 390 | 13.8 | -99.35 | -47.95 | -99.35 | 5594 |
| 90 | OBV trend | momentum | 69.72 | -30.28 | 364 | 15.9 | -95.97 | -44.22 | -95.97 | 3560 |
| 91 | CCI reversion | reversion | 68.75 | -31.25 | 335 | 13.1 | -98.49 | -47.92 | -98.49 | 4693 |
| 92 | Parabolic SAR | trend | 68.24 | -31.77 | 337 | 13.1 | -96.98 | -50.21 | -96.98 | 3628 |
| 93 | VWAP momentum | momentum | 66.96 | -33.04 | 424 | 9.0 | -98.61 | -35.72 | -98.61 | 5274 |
| 94 | MACD cross | trend | 66.13 | -33.87 | 380 | 13.7 | -99.71 | -57.55 | -99.71 | 6066 |
| 95 | Williams %R | reversion | 65.68 | -34.32 | 457 | 21.2 | -99.53 | -54.17 | -99.53 | 6107 |
| 96 | Heikin-Ashi | trend | 65.41 | -34.59 | 337 | 6.2 | -99.89 | -68.33 | -99.89 | 8284 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-01T10:40 | Z-score reversion | sell | ETH-USD | 16.43 | 0.05 | exit signal |
| 2026-10-01T10:40 | Bollinger reversion | sell | DOGE-USD | 17.58 | -0.01 | exit signal |
| 2026-10-01T10:40 | Heikin-Ashi | buy | XRP-USD | 16.40 | — | entry signal |
| 2026-10-01T10:40 | Heikin-Ashi | buy | ETH-USD | 16.40 | — | entry signal |
| 2026-10-01T10:40 | Heikin-Ashi | buy | DOGE-USD | 16.40 | — | entry signal |
| 2026-10-01T10:40 | Heikin-Ashi | buy | BTC-USD | 16.40 | — | entry signal |
| 2026-10-01T10:40 | MACD cross | buy | XRP-USD | 6.68 | — | entry signal |
| 2026-10-01T10:40 | MACD cross | buy | SOL-USD | 13.25 | — | entry signal |
| 2026-10-01T10:40 | MACD cross | buy | DOGE-USD | 13.25 | — | entry signal |
| 2026-10-01T10:40 | EMA 9/21 cross | buy | ETH-USD | 17.54 | — | entry signal |
| 2026-10-01T10:35 | CCI reversion | buy | SOL-USD | 17.20 | — | entry signal |
| 2026-10-01T10:35 | VWAP momentum | buy | BTC-USD | 16.75 | — | entry signal |
| 2026-10-01T10:35 | Parabolic SAR | buy | ETH-USD | 17.09 | — | entry signal |
| 2026-10-01T10:35 | Parabolic SAR | buy | BTC-USD | 17.09 | — | entry signal |
| 2026-10-01T10:35 | MACD cross | buy | ETH-USD | 16.58 | — | entry signal |
| 2026-10-01T10:35 | MACD cross | buy | BTC-USD | 16.58 | — | entry signal |
| 2026-10-01T10:30 | Candlestick reversal | buy | SOL-USD | 17.46 | — | entry signal |
| 2026-10-01T10:25 | CCI reversion | buy | XRP-USD | 17.20 | — | entry signal |
| 2026-10-01T10:25 | CCI reversion | buy | DOGE-USD | 17.20 | — | entry signal |
| 2026-10-01T10:20 | MACD cross | sell | BTC-USD | 13.32 | -0.02 | exit signal |
| 2026-10-01T10:15 | Candlestick reversal | buy | XRP-USD | 17.48 | — | entry signal |
| 2026-10-01T10:15 | Candlestick reversal | buy | DOGE-USD | 17.48 | — | entry signal |
| 2026-10-01T10:10 | Williams %R | buy | XRP-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Williams %R | buy | SOL-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Williams %R | buy | ETH-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Williams %R | buy | DOGE-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Williams %R | buy | BTC-USD | 13.13 | — | entry signal |
| 2026-10-01T10:10 | Bollinger reversion | buy | XRP-USD | 17.60 | — | entry signal |
| 2026-10-01T10:10 | Bollinger reversion | buy | SOL-USD | 17.60 | — | entry signal |
| 2026-10-01T10:10 | Bollinger reversion | buy | DOGE-USD | 17.60 | — | entry signal |
| 2026-10-01T10:10 | MACD cross | sell | ETH-USD | 13.33 | -0.04 | exit signal |
| 2026-10-01T10:05 | Williams %R | sell | SOL-USD | 16.28 | -0.18 | stop-loss |
| 2026-10-01T10:05 | Z-score reversion | buy | DOGE-USD | 4.10 | — | rebalance up |
| 2026-10-01T10:05 | Connors RSI(2) | sell | ETH-USD | 17.91 | -0.19 | stop-loss |
| 2026-10-01T10:05 | RSI(14) reversion | buy | DOGE-USD | 4.54 | — | rebalance up |
| 2026-10-01T10:05 | Candlestick reversal | sell | SOL-USD | 17.49 | -0.13 | exit signal |
| 2026-10-01T10:05 | Candlestick reversal | sell | DOGE-USD | 17.40 | -0.20 | stop-loss |
| 2026-10-01T10:05 | Donchian 20/10 | sell | ETH-USD | 19.03 | -0.21 | stop-loss |
| 2026-10-01T10:05 | Donchian 20/10 | sell | BTC-USD | 19.09 | -0.16 | exit signal |
| 2026-10-01T10:05 | RSI momentum | sell | ETH-USD | 18.71 | -0.23 | stop-loss |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
