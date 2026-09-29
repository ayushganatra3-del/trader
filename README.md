# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T21:10:05.000161+00:00 · 6104 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.68 (-0.32%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 20.02 | +0.03 |

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

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.96 · VIX 16.02 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 37878 decisions in 3074 calls, $0.4680 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T21:10 | 3 / 2 / 0 | SOL-USD 20%, XRP-USD 18%, DOGE-USD 15% |  |
| Breezy | 2026-09-29T21:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T21:10 | 5 / 0 / 0 | DOGE-USD 40%, SOL-USD 36% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.02 | 1.02 | 2 | 50.0 | 13.82 | 3.01 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | 0.64 | 0.29 | -9.74 | 24 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.05 | 0.05 | 0 | — | 7.21 | 2.96 | -3.62 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.68 | -7.93 | 7 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Hold BTC | benchmark | 99.93 | -0.07 | 0 | — | 30.24 | 3.80 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.71 | -0.29 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.63 | -1.84 | 83 |
| 11 | Agent | meta | 99.68 | -0.32 | 24 | 66.7 | -10.29 | -6.91 | -10.75 | 216 |
| 12 | Agent (aggressive) | meta | 99.56 | -0.44 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.48 | -0.52 | 0 | — | 3.46 | 1.94 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.40 | -0.60 | 0 | — | -2.73 | -1.32 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.39 | -0.61 | 0 | — | -3.44 | -2.11 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.13 | -0.87 | 20 | 25.0 | -12.95 | -4.42 | -14.73 | 123 |
| 18 | Daily: Bullish score | daily | 99.05 | -0.95 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.01 | -0.99 | 7 | 57.1 | 5.07 | 1.33 | -7.03 | 119 |
| 20 | Z-score reversion · 1h | reversion | 98.88 | -1.12 | 10 | 50.0 | 5.16 | 1.24 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.85 | -1.15 | 2 | 100.0 | -14.26 | -2.83 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Candlestick reversal · 1h | reversion | 98.65 | -1.35 | 20 | 25.0 | -26.72 | -6.71 | -27.54 | 488 |
| 24 | Williams %R · 1h | reversion | 98.62 | -1.38 | 40 | 45.0 | -18.00 | -3.35 | -19.52 | 488 |
| 25 | Stochastic reversion · 1h | reversion | 98.53 | -1.47 | 26 | 53.8 | -13.62 | -3.02 | -14.85 | 327 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.70 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.43 | -1.57 | 0 | — | 23.27 | 3.46 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.25 | -1.75 | 35 | 34.3 | 0.23 | 0.21 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.86 | -2.15 | 45 | 44.4 | -11.43 | -3.67 | -11.77 | 235 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.78 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.79 | -2.21 | 0 | — | -11.11 | -2.29 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.75 | -2.25 | 12 | 8.3 | 16.76 | 2.00 | -14.13 | 126 |
| 34 | Max aggression: 5-day momentum | meta | 97.69 | -2.31 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Bollinger reversion · 1h | reversion | 97.27 | -2.73 | 22 | 27.3 | -17.68 | -4.95 | -18.30 | 312 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.63 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.07 | -2.93 | 9 | 11.1 | 15.55 | 2.75 | -5.11 | 92 |
| 38 | Max aggression: 1-day momentum | meta | 96.66 | -3.34 | 2 | 0.0 | -37.96 | -2.25 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.62 | -3.38 | 0 | — | -9.73 | -2.36 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.58 | -3.42 | 18 | 5.6 | 2.00 | 0.48 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.49 | -3.51 | 139 | 12.9 | -0.57 | 0.07 | -12.39 | 394 |
| 42 | Trend pullback · 1h | trend | 96.39 | -3.61 | 27 | 11.1 | -28.34 | -6.94 | -29.45 | 148 |
| 43 | MACD cross · 1h | trend | 96.12 | -3.88 | 40 | 10.0 | -18.87 | -3.22 | -21.99 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.90 | -4.10 | 26 | 11.5 | -7.76 | -0.97 | -18.82 | 292 |
| 45 | Donchian 55/20 · 1h | breakout | 95.84 | -4.16 | 12 | 0.0 | 4.53 | 0.80 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.87 | -16.91 | 684 |
| 47 | MFI reversion · 1h | reversion | 95.46 | -4.54 | 44 | 13.6 | -10.03 | -1.85 | -17.20 | 131 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -50.24 | -28.40 | -50.38 | 607 |
| 49 | Ichimoku · 1h | trend | 95.18 | -4.83 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.91 | -5.09 | 17 | 5.9 | 7.92 | 1.23 | -10.10 | 283 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 1.00 | -12.60 | 125 |
| 52 | MACD zero-line · 1h | trend | 94.28 | -5.71 | 20 | 5.0 | -5.52 | -0.59 | -14.64 | 223 |
| 53 | RSI momentum · 1h | momentum | 94.28 | -5.72 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 54 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.51 | 1.03 | -12.78 | 214 |
| 55 | ADX DI cross · 1h | trend | 94.02 | -5.98 | 30 | 6.7 | -16.26 | -3.03 | -17.94 | 256 |
| 56 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.33 | 0.27 | -18.68 | 212 |
| 57 | Triple EMA stack · 1h | trend | 93.84 | -6.16 | 30 | 6.7 | -7.41 | -0.71 | -22.58 | 228 |
| 58 | VWAP momentum · 1h | momentum | 93.69 | -6.31 | 103 | 12.6 | -35.09 | -5.35 | -35.53 | 1234 |
| 59 | EMA 9/21 cross · 1h | trend | 93.05 | -6.95 | 44 | 11.4 | -3.90 | -0.34 | -16.92 | 307 |
| 60 | Heikin-Ashi · 1h | trend | 92.79 | -7.21 | 44 | 11.4 | -26.50 | -4.05 | -30.59 | 675 |
| 61 | OBV trend · 1h | momentum | 92.48 | -7.52 | 54 | 7.4 | -10.11 | -1.07 | -25.19 | 313 |
| 62 | RSI(14) reversion | reversion | 90.97 | -9.03 | 118 | 34.7 | -71.10 | -21.65 | -71.21 | 1471 |
| 63 | Squeeze breakout | breakout | 89.86 | -10.14 | 92 | 15.2 | -59.59 | -18.51 | -59.93 | 1190 |
| 64 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.85 | -0.41 | -19.29 | 405 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | ROC + volume | momentum | 87.31 | -12.69 | 148 | 18.9 | -72.20 | -17.97 | -72.26 | 1611 |
| 68 | Volume breakout | breakout | 87.29 | -12.71 | 102 | 15.7 | -62.06 | -20.51 | -62.20 | 892 |
| 69 | EMA 20/50 cross | trend | 87.23 | -12.77 | 121 | 16.5 | -78.53 | -17.53 | -78.59 | 1467 |
| 70 | Donchian 55/20 | breakout | 87.22 | -12.78 | 96 | 15.6 | -68.30 | -15.72 | -68.37 | 1305 |
| 71 | Ichimoku | trend | 86.01 | -13.99 | 110 | 9.1 | -80.49 | -26.23 | -80.51 | 1745 |
| 72 | Keltner breakout | breakout | 85.64 | -14.36 | 148 | 13.5 | -84.91 | -34.68 | -84.96 | 1901 |
| 73 | Z-score reversion | reversion | 85.08 | -14.92 | 180 | 32.8 | -84.37 | -27.64 | -84.41 | 2093 |
| 74 | VWAP reversion | reversion | 84.68 | -15.32 | 137 | 22.6 | -71.86 | -17.64 | -72.20 | 1399 |
| 75 | MACD zero-line | trend | 82.88 | -17.12 | 197 | 16.8 | -91.69 | -35.93 | -91.70 | 2352 |
| 76 | Supertrend | trend | 82.59 | -17.41 | 175 | 18.3 | -87.44 | -24.90 | -87.48 | 1960 |
| 77 | Donchian 20/10 | breakout | 81.48 | -18.52 | 203 | 17.7 | -90.96 | -29.67 | -90.98 | 2679 |
| 78 | MFI reversion | reversion | 81.35 | -18.65 | 181 | 19.9 | -87.88 | -36.64 | -87.90 | 2138 |
| 79 | Bollinger breakout | breakout | 81.26 | -18.75 | 202 | 16.8 | -93.90 | -42.16 | -93.92 | 2865 |
| 80 | Triple EMA stack | trend | 80.54 | -19.46 | 212 | 15.6 | -93.08 | -36.29 | -93.09 | 2623 |
| 81 | RSI momentum | momentum | 80.47 | -19.52 | 194 | 13.4 | -90.39 | -29.56 | -90.39 | 2379 |
| 82 | Trend pullback | trend | 79.54 | -20.46 | 168 | 17.3 | -90.93 | -35.30 | -90.93 | 2282 |
| 83 | ADX DI cross | trend | 79.37 | -20.63 | 196 | 8.2 | -89.44 | -47.47 | -89.44 | 2117 |
| 84 | EMA 9/21 cross | trend | 77.34 | -22.66 | 273 | 17.6 | -97.41 | -42.27 | -97.41 | 3534 |
| 85 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.45 | -42.98 | -96.45 | 3634 |
| 86 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.57 | -30.35 | -94.58 | 2642 |
| 87 | Stochastic reversion | reversion | 76.20 | -23.80 | 325 | 24.3 | -95.93 | -47.22 | -95.94 | 4060 |
| 88 | Candlestick reversal ⏸ | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.35 | -50.99 | -99.35 | 5571 |
| 89 | OBV trend | momentum | 75.58 | -24.42 | 270 | 15.6 | -95.93 | -49.15 | -95.95 | 3532 |
| 90 | Bollinger reversion | reversion | 75.07 | -24.93 | 303 | 15.8 | -95.77 | -45.47 | -95.77 | 3683 |
| 91 | CCI reversion | reversion | 73.79 | -26.21 | 232 | 11.6 | -98.44 | -51.72 | -98.45 | 4695 |
| 92 | VWAP momentum ⏸ | momentum | 73.33 | -26.67 | 369 | 10.3 | -98.44 | -36.47 | -98.44 | 5161 |
| 93 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -96.97 | -56.71 | -96.98 | 3630 |
| 94 | MACD cross | trend | 72.18 | -27.82 | 270 | 14.1 | -99.71 | -67.22 | -99.71 | 6070 |
| 95 | Williams %R ⏸ | reversion | 71.59 | -28.41 | 340 | 21.2 | -99.52 | -60.94 | -99.52 | 6106 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -87.24 | -99.89 | 8298 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T21:05 | OBV trend | sell | ETH-USD | 18.81 | -0.15 | exit signal |
| 2026-09-29T21:05 | OBV trend | sell | BTC-USD | 18.89 | -0.12 | exit signal |
| 2026-09-29T21:05 | VWAP momentum | sell | DOGE-USD | 18.28 | -0.15 | exit signal |
| 2026-09-29T21:05 | VWAP momentum | sell | BTC-USD | 18.30 | -0.13 | exit signal |
| 2026-09-29T21:05 | Ichimoku | sell | BTC-USD | 21.40 | -0.14 | exit signal |
| 2026-09-29T21:05 | ADX DI cross | sell | SOL-USD | 19.78 | -0.14 | exit signal |
| 2026-09-29T21:05 | ADX DI cross | sell | DOGE-USD | 19.73 | -0.17 | exit signal |
| 2026-09-29T21:05 | MACD zero-line | sell | XRP-USD | 20.59 | -0.18 | exit signal |
| 2026-09-29T21:05 | MACD cross | sell | XRP-USD | 17.97 | -0.16 | exit signal |
| 2026-09-29T21:05 | Triple EMA stack | sell | ETH-USD | 20.04 | -0.15 | exit signal |
| 2026-09-29T21:05 | EMA 9/21 cross | buy | DOGE-USD | 3.91 | — | rebalance up |
| 2026-09-29T21:05 | EMA 9/21 cross | sell | XRP-USD | 11.57 | -0.10 | exit signal |
| 2026-09-29T21:05 | EMA 9/21 cross | sell | ETH-USD | 19.28 | -0.16 | exit signal |
| 2026-09-29T21:00 | Heikin-Ashi · 1h | buy | BTC-USD | 23.22 | — | entry signal |
| 2026-09-29T21:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 18.68 | -0.13 | exit signal |
| 2026-09-29T21:00 | VWAP momentum | sell | SOL-USD | 18.28 | -0.12 | exit signal |
| 2026-09-29T21:00 | MACD cross | sell | SOL-USD | 17.97 | -0.12 | exit signal |
| 2026-09-29T20:55 | Stochastic reversion | sell | SOL-USD | 19.02 | -0.05 | exit signal |
| 2026-09-29T20:55 | MACD cross | buy | SOL-USD | 18.10 | — | entry signal |
| 2026-09-29T20:50 | VWAP momentum | buy | SOL-USD | 18.40 | — | entry signal |
| 2026-09-29T20:40 | VWAP momentum | buy | DOGE-USD | 18.43 | — | entry signal |
| 2026-09-29T20:40 | VWAP momentum | buy | BTC-USD | 18.43 | — | entry signal |
| 2026-09-29T20:35 | VWAP momentum | sell | DOGE-USD | 18.33 | -0.15 | exit signal |
| 2026-09-29T20:35 | VWAP momentum | sell | BTC-USD | 18.38 | -0.12 | exit signal |
| 2026-09-29T20:35 | Ichimoku | buy | BTC-USD | 21.54 | — | entry signal |
| 2026-09-29T20:30 | MFI reversion | buy | DOGE-USD | 20.36 | — | entry signal |
| 2026-09-29T20:30 | MACD zero-line | buy | XRP-USD | 20.77 | — | entry signal |
| 2026-09-29T20:30 | EMA 9/21 cross | buy | XRP-USD | 3.87 | — | rebalance up |
| 2026-09-29T20:30 | EMA 9/21 cross | sell | SOL-USD | 3.87 | -0.02 | rebalance down |
| 2026-09-29T20:26 | Stochastic reversion | sell | DOGE-USD | 19.07 | -0.00 | exit signal |
| 2026-09-29T20:26 | VWAP momentum | buy | DOGE-USD | 18.48 | — | entry |
| 2026-09-29T20:26 | ADX DI cross | buy | DOGE-USD | 19.91 | — | entry |
| 2026-09-29T20:26 | MACD zero-line | buy | DOGE-USD | 20.79 | — | entry signal |
| 2026-09-29T20:26 | MACD cross | buy | XRP-USD | 18.14 | — | entry signal |
| 2026-09-29T20:26 | MACD cross | buy | DOGE-USD | 18.14 | — | entry signal |
| 2026-09-29T20:26 | Triple EMA stack | buy | SOL-USD | 20.19 | — | entry signal |
| 2026-09-29T20:26 | Triple EMA stack | buy | ETH-USD | 20.19 | — | entry signal |
| 2026-09-29T20:26 | EMA 9/21 cross | buy | XRP-USD | 7.81 | — | entry signal |
| 2026-09-29T20:26 | EMA 9/21 cross | buy | DOGE-USD | 15.53 | — | entry signal |
| 2026-09-29T20:26 | EMA 9/21 cross | sell | BTC-USD | 3.97 | -0.02 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
