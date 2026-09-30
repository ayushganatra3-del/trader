# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T15:10:05.000150+00:00 · 7001 ticks

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

Today: 17265 decisions in 2295 calls, $0.2255 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T15:10 | 2 / 24 / 3 | LABU 15% |  |
| Breezy | 2026-09-30T15:10 | 0 / 24 / 5 | cash |  |
| Boozy | 2026-09-30T15:10 | 4 / 25 / 0 | COIN 65% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.83 | 1.83 | 2 | 50.0 | 15.04 | 3.23 | -7.55 | 43 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.54 | 0.54 | 0 | — | 6.54 | 1.82 | -7.93 | 7 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 1 | 100.0 | 0.16 | 0.14 | -9.74 | 24 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.28 | 0.28 | 0 | — | 7.37 | 3.00 | -3.62 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Hold BTC | benchmark | 99.95 | -0.05 | 0 | — | 28.93 | 3.64 | -8.68 | 1 |
| 9 | Copy: Insider buying | copy | 99.77 | -0.23 | 2 | 100.0 | -13.15 | -2.54 | -17.74 | 73 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 99.76 | -0.24 | 0 | — | -2.69 | -1.58 | -5.09 | 2 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 7 | 42.9 | 3.34 | 1.70 | -1.76 | 83 |
| 12 | Timing: Nasdaq FTD · TQQQ | daily | 99.66 | -0.34 | 0 | — | -9.04 | -1.76 | -15.27 | 2 |
| 13 | Agent | meta | 99.65 | -0.35 | 25 | 68.0 | -10.41 | -6.70 | -11.08 | 215 |
| 14 | Hold SPY | benchmark | 99.63 | -0.37 | 0 | — | 3.96 | 2.18 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -12.58 | -4.24 | -14.70 | 122 |
| 16 | RSI(14) reversion · 1h | reversion | 99.50 | -0.50 | 8 | 62.5 | 0.02 | 0.11 | -7.97 | 124 |
| 17 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -2.05 | -1.11 | -4.99 | 98 |
| 18 | Daily: Bullish score | daily | 99.39 | -0.61 | 3 | 0.0 | 0.09 | 0.21 | -12.76 | 14 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 99.00 | -1.00 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 21 | Gap and go | momentum | 98.93 | -1.07 | 10 | 10.0 | 15.97 | 3.93 | -4.73 | 184 |
| 22 | Copy: Warren Buffett (BRK-B) | copy | 98.91 | -1.09 | 0 | — | -0.99 | -0.35 | -7.65 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 98.78 | -1.22 | 26 | 53.8 | -12.00 | -2.65 | -13.58 | 326 |
| 24 | Daily: SMA 20/50 cross · AAPL | daily | 98.67 | -1.33 | 0 | — | -5.97 | -1.31 | -10.06 | 1 |
| 25 | CCI reversion · 1h | reversion | 98.61 | -1.39 | 38 | 34.2 | 2.18 | 0.53 | -12.41 | 411 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 2 | 0.0 | -0.60 | -0.18 | -4.88 | 18 |
| 27 | Williams %R · 1h | reversion | 98.57 | -1.43 | 47 | 46.8 | -17.60 | -3.30 | -19.52 | 488 |
| 28 | Z-score reversion · 1h | reversion | 98.53 | -1.47 | 11 | 45.5 | 5.11 | 1.22 | -8.60 | 154 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.24 | 0.22 | -15.21 | 46 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 98.33 | -1.67 | 0 | — | 24.01 | 3.53 | -6.29 | 1 |
| 31 | Candlestick reversal · 1h | reversion | 98.29 | -1.71 | 33 | 24.2 | -26.29 | -6.37 | -27.43 | 494 |
| 32 | Agent (rotation) | meta | 98.29 | -1.71 | 33 | 12.1 | -5.20 | -1.86 | -10.27 | 210 |
| 33 | Connors RSI(2) · 1h | reversion | 97.93 | -2.07 | 47 | 46.8 | -11.03 | -3.49 | -11.76 | 233 |
| 34 | Bollinger reversion · 1h | reversion | 97.49 | -2.51 | 31 | 32.3 | -15.54 | -4.30 | -17.14 | 307 |
| 35 | EMA 20/50 cross · 1h | trend | 97.35 | -2.65 | 16 | 6.2 | 15.48 | 1.96 | -12.19 | 129 |
| 36 | Opening range 30m | breakout | 97.12 | -2.88 | 38 | 13.2 | -9.75 | -2.83 | -14.28 | 558 |
| 37 | Supertrend · 1h | trend | 96.38 | -3.62 | 18 | 5.6 | 1.69 | 0.43 | -16.43 | 199 |
| 38 | Trend pullback · 1h | trend | 96.35 | -3.65 | 29 | 10.3 | -24.98 | -6.61 | -25.81 | 147 |
| 39 | Agent (ML meta-label) | meta | 96.10 | -3.90 | 153 | 13.1 | 4.76 | 0.98 | -12.37 | 398 |
| 40 | Opening range 15m | breakout | 95.98 | -4.02 | 49 | 12.2 | -11.34 | -3.09 | -16.70 | 689 |
| 41 | Max aggression: 5-day momentum | meta | 95.92 | -4.08 | 3 | 66.7 | -12.91 | -0.90 | -29.56 | 29 |
| 42 | Donchian 55/20 · 1h | breakout | 95.80 | -4.20 | 15 | 0.0 | 4.03 | 0.73 | -16.96 | 115 |
| 43 | MACD cross · 1h | trend | 95.31 | -4.69 | 40 | 10.0 | -12.98 | -2.03 | -17.31 | 469 |
| 44 | Parabolic SAR · 1h | trend | 95.06 | -4.94 | 28 | 10.7 | -7.71 | -0.95 | -18.82 | 304 |
| 45 | MFI reversion · 1h | reversion | 94.96 | -5.04 | 50 | 18.0 | -9.34 | -1.69 | -17.14 | 129 |
| 46 | Squeeze breakout · 1h | breakout | 94.91 | -5.09 | 15 | 6.7 | 10.86 | 1.91 | -7.74 | 102 |
| 47 | Max aggression: 1-day momentum | meta | 94.56 | -5.44 | 3 | 33.3 | -21.11 | -1.00 | -41.28 | 42 |
| 48 | Three white soldiers | momentum | 94.45 | -5.55 | 47 | 17.0 | -50.28 | -27.78 | -50.39 | 609 |
| 49 | ADX DI cross · 1h | trend | 94.27 | -5.73 | 32 | 6.2 | -15.68 | -2.90 | -17.95 | 259 |
| 50 | Volume breakout · 1h | breakout | 94.21 | -5.79 | 28 | 3.6 | 5.85 | 0.99 | -12.60 | 129 |
| 51 | Ichimoku · 1h | trend | 93.81 | -6.19 | 20 | 15.0 | 5.80 | 0.88 | -15.13 | 122 |
| 52 | RSI momentum · 1h | momentum | 93.61 | -6.39 | 28 | 3.6 | -1.28 | 0.02 | -15.29 | 218 |
| 53 | VWAP momentum · 1h | momentum | 93.46 | -6.54 | 113 | 13.3 | -34.33 | -5.16 | -35.60 | 1246 |
| 54 | Bollinger breakout · 1h | breakout | 93.40 | -6.60 | 24 | 8.3 | 6.65 | 1.06 | -10.11 | 288 |
| 55 | Triple EMA stack · 1h | trend | 92.76 | -7.24 | 32 | 6.2 | -6.28 | -0.56 | -22.22 | 216 |
| 56 | MACD zero-line · 1h | trend | 92.33 | -7.67 | 23 | 4.3 | -7.48 | -0.87 | -16.21 | 229 |
| 57 | EMA 9/21 cross · 1h | trend | 91.94 | -8.06 | 46 | 10.9 | -4.79 | -0.46 | -16.92 | 318 |
| 58 | Keltner breakout · 1h | breakout | 91.92 | -8.08 | 14 | 0.0 | -7.32 | -0.79 | -19.70 | 220 |
| 59 | Heikin-Ashi · 1h | trend | 91.60 | -8.40 | 51 | 9.8 | -26.08 | -3.95 | -31.31 | 676 |
| 60 | Donchian 20/10 · 1h | breakout | 91.58 | -8.42 | 21 | 9.5 | 3.32 | 0.63 | -13.45 | 219 |
| 61 | RSI(14) reversion | reversion | 90.85 | -9.15 | 120 | 34.2 | -71.31 | -21.48 | -71.37 | 1499 |
| 62 | OBV trend · 1h | momentum | 90.29 | -9.71 | 64 | 6.2 | -13.74 | -1.60 | -24.90 | 328 |
| 63 | Squeeze breakout | breakout | 87.72 | -12.28 | 104 | 13.5 | -60.05 | -18.73 | -60.06 | 1191 |
| 64 | ROC + volume · 1h | momentum | 87.51 | -12.49 | 59 | 5.1 | -11.99 | -1.55 | -21.75 | 418 |
| 65 | Donchian 55/20 | breakout | 86.16 | -13.84 | 106 | 16.0 | -67.53 | -15.41 | -67.71 | 1296 |
| 66 | Volume breakout | breakout | 85.28 | -14.72 | 113 | 15.0 | -62.30 | -19.91 | -62.61 | 899 |
| 67 | ROC + volume | momentum | 85.20 | -14.79 | 172 | 19.8 | -72.67 | -17.69 | -72.88 | 1651 |
| 68 | Keltner breakout | breakout | 83.81 | -16.19 | 163 | 13.5 | -84.67 | -34.56 | -84.75 | 1899 |
| 69 | Ichimoku | trend | 83.60 | -16.40 | 127 | 8.7 | -80.40 | -25.95 | -80.51 | 1745 |
| 70 | EMA 20/50 cross | trend | 83.56 | -16.44 | 141 | 14.9 | -78.93 | -17.59 | -78.93 | 1476 |
| 71 | Z-score reversion | reversion | 83.33 | -16.67 | 194 | 30.4 | -84.64 | -27.58 | -84.68 | 2108 |
| 72 | VWAP reversion | reversion | 83.18 | -16.82 | 151 | 23.2 | -71.88 | -17.82 | -72.05 | 1404 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 80.09 | -19.91 | 196 | 17.9 | -87.44 | -24.60 | -87.58 | 1960 |
| 76 | Donchian 20/10 | breakout | 79.85 | -20.15 | 220 | 17.7 | -90.59 | -28.98 | -90.67 | 2673 |
| 77 | MFI reversion | reversion | 79.79 | -20.20 | 190 | 18.9 | -88.08 | -35.22 | -88.11 | 2155 |
| 78 | MACD zero-line | trend | 79.55 | -20.45 | 222 | 15.3 | -91.80 | -35.82 | -91.85 | 2355 |
| 79 | Trend pullback | trend | 79.00 | -21.00 | 183 | 19.1 | -90.54 | -32.85 | -90.64 | 2261 |
| 80 | Triple EMA stack | trend | 78.62 | -21.38 | 231 | 16.5 | -92.88 | -35.16 | -92.96 | 2581 |
| 81 | Bollinger breakout | breakout | 78.13 | -21.87 | 230 | 15.7 | -93.81 | -42.23 | -93.84 | 2862 |
| 82 | RSI momentum | momentum | 78.07 | -21.93 | 216 | 13.9 | -90.39 | -28.98 | -90.50 | 2382 |
| 83 | ADX DI cross | trend | 76.96 | -23.04 | 214 | 7.5 | -89.46 | -45.59 | -89.48 | 2108 |
| 84 | Consensus | meta | 74.97 | -25.03 | 201 | 7.0 | -94.70 | -30.35 | -94.72 | 2654 |
| 85 | Stochastic reversion | reversion | 74.45 | -25.55 | 345 | 23.2 | -95.95 | -45.23 | -95.97 | 4053 |
| 86 | EMA 9/21 cross | trend | 74.21 | -25.79 | 306 | 17.0 | -97.40 | -41.01 | -97.45 | 3540 |
| 87 | Connors RSI(2) | reversion | 74.20 | -25.80 | 265 | 17.0 | -96.40 | -40.35 | -96.40 | 3604 |
| 88 | Candlestick reversal | reversion | 73.09 | -26.91 | 308 | 12.7 | -99.36 | -49.40 | -99.36 | 5615 |
| 89 | Bollinger reversion | reversion | 73.02 | -26.98 | 327 | 15.3 | -95.81 | -43.55 | -95.82 | 3687 |
| 90 | OBV trend | momentum | 71.36 | -28.64 | 304 | 14.8 | -95.91 | -47.51 | -95.93 | 3538 |
| 91 | CCI reversion | reversion | 70.58 | -29.42 | 268 | 10.8 | -98.47 | -49.55 | -98.47 | 4693 |
| 92 | Parabolic SAR | trend | 70.43 | -29.57 | 295 | 12.5 | -96.96 | -54.53 | -96.99 | 3618 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.53 | -36.09 | -98.54 | 5263 |
| 94 | MACD cross | trend | 68.38 | -31.62 | 312 | 13.5 | -99.71 | -64.06 | -99.72 | 6083 |
| 95 | Williams %R | reversion | 67.83 | -32.17 | 383 | 20.1 | -99.52 | -56.91 | -99.53 | 6107 |
| 96 | Heikin-Ashi | trend | 67.17 | -32.83 | 294 | 5.4 | -99.89 | -77.67 | -99.89 | 8306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T15:10 | Connors RSI(2) | buy | AAPL | 18.55 | — | entry signal |
| 2026-09-30T15:10 | Candlestick reversal | buy | XRP-USD | 2.04 | — | rebalance up |
| 2026-09-30T15:10 | Candlestick reversal | buy | TSLA | 8.13 | — | entry signal |
| 2026-09-30T15:10 | Candlestick reversal | buy | SOL-USD | 8.13 | — | entry signal |
| 2026-09-30T15:10 | Candlestick reversal | sell | SQQQ | 9.15 | -0.02 | exit signal |
| 2026-09-30T15:10 | Candlestick reversal | sell | ETHU | 9.15 | -0.01 | target is flat |
| 2026-09-30T15:10 | Squeeze breakout | sell | NVDA | 21.97 | -0.01 | exit signal |
| 2026-09-30T15:10 | ROC + volume | sell | UPRO | 21.27 | 0.02 | exit signal |
| 2026-09-30T15:10 | ROC + volume | sell | AAPL | 21.27 | -0.03 | exit signal |
| 2026-09-30T15:10 | Trend pullback | buy | BITX | 19.75 | — | entry signal |
| 2026-09-30T15:10 | MACD zero-line | sell | AAPL | 20.13 | 0.32 | exit signal |
| 2026-09-30T15:10 | Triple EMA stack | buy | META | 19.58 | — | entry signal |
| 2026-09-30T15:05 | Agent (ML meta-label) | sell | COIN | 4.58 | 0.01 | selected signal exited |
| 2026-09-30T15:05 | Candlestick reversal | buy | XRP-USD | 1.01 | — | entry signal |
| 2026-09-30T15:05 | Candlestick reversal | buy | BTC-USD | 8.13 | — | entry signal |
| 2026-09-30T15:05 | Candlestick reversal | sell | SOXL | 9.13 | 0.03 | exit signal |
| 2026-09-30T15:05 | ROC + volume | buy | UPRO | 9.10 | — | rebalance up |
| 2026-09-30T15:05 | ROC + volume | buy | LABU | 9.11 | — | rebalance up |
| 2026-09-30T15:05 | ROC + volume | buy | AMZN | 12.74 | — | rebalance up |
| 2026-09-30T15:05 | ROC + volume | buy | AAPL | 9.16 | — | rebalance up |
| 2026-09-30T15:05 | ROC + volume | sell | TQQQ | 12.18 | 0.02 | exit signal |
| 2026-09-30T15:05 | ROC + volume | sell | TECL | 10.74 | 0.03 | exit signal |
| 2026-09-30T15:05 | ROC + volume | sell | MSFT | 10.73 | 0.03 | exit signal |
| 2026-09-30T15:05 | Heikin-Ashi | buy | TNA | 3.58 | — | rebalance up |
| 2026-09-30T15:05 | Heikin-Ashi | buy | META | 3.59 | — | rebalance up |
| 2026-09-30T15:05 | Heikin-Ashi | buy | LABU | 3.59 | — | rebalance up |
| 2026-09-30T15:05 | Heikin-Ashi | buy | IWM | 3.59 | — | rebalance up |
| 2026-09-30T15:05 | Heikin-Ashi | buy | DOGE-USD | 3.60 | — | rebalance up |
| 2026-09-30T15:05 | Heikin-Ashi | buy | BTC-USD | 3.60 | — | rebalance up |
| 2026-09-30T15:05 | Heikin-Ashi | buy | BITX | 3.59 | — | rebalance up |
| 2026-09-30T15:05 | Heikin-Ashi | buy | AMZN | 3.59 | — | rebalance up |
| 2026-09-30T15:05 | Heikin-Ashi | sell | UPRO | 4.80 | -0.02 | exit signal |
| 2026-09-30T15:05 | Heikin-Ashi | sell | TQQQ | 4.78 | -0.01 | exit signal |
| 2026-09-30T15:05 | Heikin-Ashi | sell | TECL | 4.78 | -0.03 | exit signal |
| 2026-09-30T15:05 | Heikin-Ashi | sell | SPY | 4.80 | -0.00 | exit signal |
| 2026-09-30T15:05 | Heikin-Ashi | sell | SOXL | 4.78 | -0.02 | exit signal |
| 2026-09-30T15:05 | Heikin-Ashi | sell | QQQ | 4.80 | -0.01 | exit signal |
| 2026-09-30T15:05 | MACD cross | buy | COIN | 1.41 | — | entry signal |
| 2026-09-30T15:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 98.59 | — | entry |
| 2026-09-30T15:00 | Agent (ML meta-label) | buy | XRP-USD | 2.54 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
