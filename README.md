# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T13:40:05.000149+00:00 · 6932 ticks

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

Today: 11040 decisions in 2088 calls, $0.1528 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T13:40 | 1 / 17 / 12 | TECL 18% |  |
| Breezy | 2026-09-30T13:40 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-09-30T13:40 | 6 / 24 / 0 | TECL 34%, MSTR 31% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.97 | 0.97 | 2 | 50.0 | 14.12 | 3.05 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 3 | Hold BTC | benchmark | 100.28 | 0.28 | 0 | — | 29.66 | 3.71 | -8.68 | 1 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -1.82 | -0.50 | -9.74 | 23 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.02 | 0.02 | 0 | — | 7.68 | 2.04 | -7.93 | 7 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: Bullish score | daily | 99.70 | -0.30 | 3 | 0.0 | 0.56 | 0.28 | -12.76 | 14 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.67 | -0.34 | 6 | 50.0 | 3.29 | 1.68 | -1.76 | 81 |
| 10 | Agent | meta | 99.65 | -0.35 | 25 | 68.0 | -9.91 | -6.59 | -10.68 | 215 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.61 | -0.39 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 12 | VWAP reversion · 1h | reversion | 99.51 | -0.49 | 21 | 23.8 | -12.54 | -4.24 | -14.65 | 121 |
| 13 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -0.41 | -0.21 | -3.92 | 97 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 99.45 | -0.55 | 0 | — | -2.95 | -1.77 | -5.09 | 2 |
| 15 | Hold SPY | benchmark | 99.37 | -0.63 | 0 | — | 3.88 | 2.14 | -3.66 | 1 |
| 16 | Copy: Warren Buffett (BRK-B) | copy | 99.27 | -0.73 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 17 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 18 | RSI(14) reversion · 1h | reversion | 99.13 | -0.88 | 7 | 57.1 | 7.22 | 1.73 | -6.57 | 129 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 98.95 | -1.05 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 98.82 | -1.18 | 0 | — | -9.77 | -1.94 | -15.27 | 2 |
| 21 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 22 | Stochastic reversion · 1h | reversion | 98.74 | -1.26 | 26 | 53.8 | -12.21 | -2.70 | -13.80 | 327 |
| 23 | Williams %R · 1h | reversion | 98.59 | -1.42 | 43 | 44.2 | -17.61 | -3.22 | -19.58 | 487 |
| 24 | Copy: Insider buying | copy | 98.46 | -1.54 | 2 | 100.0 | -14.29 | -2.81 | -17.74 | 73 |
| 25 | Gap and go | momentum | 98.44 | -1.56 | 10 | 10.0 | 15.61 | 3.86 | -4.73 | 183 |
| 26 | Z-score reversion · 1h | reversion | 98.37 | -1.63 | 11 | 45.5 | 4.96 | 1.19 | -8.60 | 153 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -0.49 | 0.11 | -15.21 | 46 |
| 28 | CCI reversion · 1h | reversion | 98.32 | -1.68 | 36 | 33.3 | 2.05 | 0.51 | -12.41 | 409 |
| 29 | Candlestick reversal · 1h | reversion | 98.21 | -1.79 | 30 | 26.7 | -25.61 | -6.19 | -26.66 | 497 |
| 30 | Connors RSI(2) · 1h | reversion | 98.07 | -1.94 | 46 | 45.7 | -10.88 | -3.43 | -11.76 | 232 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 97.99 | -2.01 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 32 | EMA 20/50 cross · 1h | trend | 97.97 | -2.03 | 14 | 7.1 | 17.14 | 2.12 | -12.18 | 128 |
| 33 | Agent (rotation) | meta | 97.82 | -2.18 | 33 | 12.1 | -4.70 | -1.69 | -10.23 | 213 |
| 34 | Bollinger reversion · 1h | reversion | 97.39 | -2.61 | 24 | 29.2 | -17.06 | -4.69 | -18.31 | 312 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.77 | -2.83 | -14.21 | 548 |
| 36 | Daily: SMA 20/50 cross · AAPL | daily | 97.06 | -2.94 | 0 | — | -7.04 | -1.63 | -10.06 | 1 |
| 37 | Max aggression: 5-day momentum | meta | 96.71 | -3.29 | 3 | 66.7 | -12.15 | -0.82 | -29.56 | 29 |
| 38 | Supertrend · 1h | trend | 96.66 | -3.34 | 18 | 5.6 | 3.26 | 0.63 | -16.43 | 194 |
| 39 | Trend pullback · 1h | trend | 96.54 | -3.46 | 28 | 10.7 | -24.76 | -6.52 | -25.81 | 146 |
| 40 | Agent (ML meta-label) | meta | 96.31 | -3.69 | 147 | 12.2 | 7.45 | 1.37 | -13.66 | 396 |
| 41 | Donchian 55/20 · 1h | breakout | 96.26 | -3.74 | 13 | 0.0 | 4.70 | 0.81 | -16.96 | 115 |
| 42 | Squeeze breakout · 1h | breakout | 95.71 | -4.29 | 12 | 8.3 | 7.71 | 1.38 | -11.41 | 105 |
| 43 | Parabolic SAR · 1h | trend | 95.62 | -4.38 | 26 | 11.5 | -7.94 | -0.99 | -19.53 | 293 |
| 44 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -11.73 | -3.21 | -16.70 | 676 |
| 45 | Max aggression: 1-day momentum | meta | 95.33 | -4.67 | 3 | 33.3 | -20.43 | -0.95 | -41.28 | 42 |
| 46 | MFI reversion · 1h | reversion | 95.25 | -4.75 | 47 | 14.9 | -7.08 | -1.21 | -16.99 | 128 |
| 47 | MACD cross · 1h | trend | 95.23 | -4.77 | 40 | 10.0 | -14.10 | -2.23 | -17.54 | 464 |
| 48 | Ichimoku · 1h | trend | 94.82 | -5.18 | 18 | 16.7 | 6.67 | 0.97 | -15.13 | 122 |
| 49 | Three white soldiers | momentum | 94.54 | -5.46 | 46 | 17.4 | -50.39 | -28.09 | -50.39 | 607 |
| 50 | ADX DI cross · 1h | trend | 94.48 | -5.52 | 31 | 6.5 | -14.81 | -2.75 | -17.51 | 251 |
| 51 | RSI momentum · 1h | momentum | 94.35 | -5.66 | 25 | 4.0 | -1.69 | -0.03 | -15.29 | 218 |
| 52 | Volume breakout · 1h | breakout | 94.28 | -5.72 | 28 | 3.6 | 5.36 | 0.92 | -12.60 | 126 |
| 53 | Bollinger breakout · 1h | breakout | 93.94 | -6.06 | 21 | 9.5 | 5.74 | 0.94 | -11.41 | 287 |
| 54 | Triple EMA stack · 1h | trend | 93.88 | -6.12 | 30 | 6.7 | -6.30 | -0.57 | -22.10 | 227 |
| 55 | VWAP momentum · 1h | momentum | 93.58 | -6.42 | 105 | 13.3 | -33.78 | -5.06 | -35.29 | 1239 |
| 56 | MACD zero-line · 1h | trend | 93.29 | -6.71 | 21 | 4.8 | -6.23 | -0.69 | -14.79 | 228 |
| 57 | Donchian 20/10 · 1h | breakout | 92.80 | -7.20 | 17 | 11.8 | 4.73 | 0.81 | -12.78 | 217 |
| 58 | EMA 9/21 cross · 1h | trend | 92.49 | -7.51 | 45 | 11.1 | -6.10 | -0.64 | -16.92 | 318 |
| 59 | Keltner breakout · 1h | breakout | 92.42 | -7.58 | 12 | 0.0 | -8.33 | -0.96 | -19.20 | 217 |
| 60 | Heikin-Ashi · 1h | trend | 91.99 | -8.01 | 45 | 11.1 | -25.77 | -3.89 | -30.83 | 674 |
| 61 | OBV trend · 1h | momentum | 91.74 | -8.26 | 57 | 7.0 | -14.16 | -1.64 | -25.03 | 325 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.20 | -21.35 | -71.25 | 1467 |
| 63 | ROC + volume · 1h | momentum | 88.18 | -11.81 | 54 | 5.6 | -10.66 | -1.35 | -20.45 | 409 |
| 64 | Squeeze breakout | breakout | 87.79 | -12.21 | 102 | 13.7 | -59.88 | -18.66 | -59.91 | 1195 |
| 65 | Donchian 55/20 | breakout | 86.21 | -13.79 | 101 | 14.9 | -67.48 | -15.38 | -67.82 | 1300 |
| 66 | ROC + volume | momentum | 85.36 | -14.64 | 160 | 18.1 | -72.94 | -17.87 | -72.95 | 1652 |
| 67 | Volume breakout | breakout | 85.28 | -14.72 | 113 | 15.0 | -62.40 | -19.95 | -62.71 | 900 |
| 68 | EMA 20/50 cross | trend | 84.72 | -15.28 | 135 | 14.8 | -78.67 | -17.49 | -78.87 | 1477 |
| 69 | Keltner breakout | breakout | 83.97 | -16.03 | 160 | 13.8 | -84.58 | -34.39 | -84.62 | 1890 |
| 70 | VWAP reversion | reversion | 83.90 | -16.10 | 145 | 22.1 | -71.86 | -17.77 | -71.97 | 1394 |
| 71 | Z-score reversion | reversion | 83.65 | -16.34 | 193 | 30.6 | -84.59 | -27.49 | -84.60 | 2103 |
| 72 | Ichimoku | trend | 83.21 | -16.79 | 126 | 7.9 | -80.59 | -26.19 | -80.59 | 1745 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.06 | -19.94 | 190 | 18.9 | -88.08 | -35.19 | -88.11 | 2141 |
| 76 | Supertrend | trend | 79.94 | -20.06 | 196 | 17.9 | -87.41 | -24.51 | -87.57 | 1960 |
| 77 | Donchian 20/10 | breakout | 79.48 | -20.52 | 219 | 17.8 | -90.67 | -29.25 | -90.69 | 2671 |
| 78 | MACD zero-line | trend | 79.27 | -20.73 | 220 | 15.0 | -91.83 | -35.92 | -91.84 | 2356 |
| 79 | Trend pullback | trend | 78.91 | -21.09 | 180 | 18.9 | -90.56 | -33.06 | -90.63 | 2263 |
| 80 | Triple EMA stack | trend | 78.46 | -21.54 | 226 | 14.6 | -92.94 | -35.46 | -93.02 | 2616 |
| 81 | Bollinger breakout | breakout | 77.90 | -22.10 | 226 | 15.9 | -93.85 | -42.46 | -93.85 | 2863 |
| 82 | RSI momentum | momentum | 77.61 | -22.39 | 215 | 14.0 | -90.58 | -29.32 | -90.62 | 2399 |
| 83 | ADX DI cross | trend | 77.04 | -22.95 | 212 | 7.5 | -89.40 | -44.73 | -89.43 | 2095 |
| 84 | Connors RSI(2) | reversion | 75.64 | -24.36 | 250 | 16.4 | -96.32 | -39.65 | -96.32 | 3605 |
| 85 | Consensus | meta | 75.37 | -24.62 | 199 | 7.0 | -94.72 | -30.32 | -94.72 | 2655 |
| 86 | Stochastic reversion | reversion | 74.89 | -25.11 | 343 | 23.3 | -95.89 | -44.13 | -95.93 | 4051 |
| 87 | EMA 9/21 cross | trend | 73.93 | -26.07 | 301 | 15.9 | -97.41 | -41.12 | -97.44 | 3550 |
| 88 | Candlestick reversal | reversion | 73.84 | -26.16 | 296 | 12.2 | -99.35 | -48.38 | -99.35 | 5577 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.73 | 323 | 14.9 | -95.77 | -42.92 | -95.80 | 3681 |
| 90 | OBV trend | momentum | 71.44 | -28.56 | 300 | 14.7 | -95.95 | -48.14 | -95.95 | 3554 |
| 91 | CCI reversion | reversion | 70.86 | -29.14 | 266 | 10.5 | -98.45 | -48.88 | -98.46 | 4696 |
| 92 | Parabolic SAR | trend | 69.80 | -30.20 | 295 | 12.5 | -97.02 | -55.87 | -97.02 | 3633 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.53 | -36.11 | -98.54 | 5258 |
| 94 | Williams %R | reversion | 68.53 | -31.47 | 374 | 19.8 | -99.52 | -56.58 | -99.52 | 6106 |
| 95 | MACD cross | trend | 68.19 | -31.81 | 309 | 13.6 | -99.72 | -64.76 | -99.72 | 6095 |
| 96 | Heikin-Ashi | trend | 67.16 | -32.84 | 271 | 3.7 | -99.89 | -78.27 | -99.89 | 8300 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T13:40 | Agent (rotation) | buy | TECL | 16.30 | — | entry |
| 2026-09-30T13:40 | Day trade: Stocks in Play ORB | buy | TECL | 24.92 | — | entry |
| 2026-09-30T13:40 | Agent (ML meta-label) | sell | BTC-USD | 2.50 | -0.05 | selected signal exited |
| 2026-09-30T13:40 | Consensus | buy | DOGE-USD | 3.81 | — | rebalance up |
| 2026-09-30T13:40 | Consensus | sell | XRP-USD | 15.02 | -0.26 | target is flat |
| 2026-09-30T13:40 | Consensus | sell | SOL-USD | 15.10 | -0.18 | target is flat |
| 2026-09-30T13:40 | Consensus | sell | ETH-USD | 15.06 | -0.14 | target is flat |
| 2026-09-30T13:40 | Consensus | sell | BTC-USD | 15.14 | -0.14 | target is flat |
| 2026-09-30T13:40 | Volume breakout · 1h | sell | BTC-USD | 23.24 | -0.44 | stop-loss |
| 2026-09-30T13:40 | Squeeze breakout · 1h | buy | XRP-USD | 4.88 | — | rebalance up |
| 2026-09-30T13:40 | Squeeze breakout · 1h | buy | SOL-USD | 9.49 | — | rebalance up |
| 2026-09-30T13:40 | Squeeze breakout · 1h | buy | DOGE-USD | 4.89 | — | rebalance up |
| 2026-09-30T13:40 | Squeeze breakout · 1h | sell | ETH-USD | 19.04 | -0.35 | stop-loss |
| 2026-09-30T13:40 | Squeeze breakout · 1h | sell | BTC-USD | 19.03 | -0.36 | stop-loss |
| 2026-09-30T13:40 | Keltner breakout · 1h | sell | ETH-USD | 23.08 | -0.43 | stop-loss |
| 2026-09-30T13:40 | Keltner breakout · 1h | sell | BTC-USD | 23.07 | -0.44 | stop-loss |
| 2026-09-30T13:40 | Bollinger breakout · 1h | buy | XRP-USD | 4.78 | — | rebalance up |
| 2026-09-30T13:40 | Bollinger breakout · 1h | buy | SOL-USD | 4.77 | — | rebalance up |
| 2026-09-30T13:40 | Bollinger breakout · 1h | buy | DOGE-USD | 7.82 | — | rebalance up |
| 2026-09-30T13:40 | Bollinger breakout · 1h | sell | ETH-USD | 15.62 | -0.29 | stop-loss |
| 2026-09-30T13:40 | Bollinger breakout · 1h | sell | BTC-USD | 15.67 | -0.05 | stop-loss |
| 2026-09-30T13:40 | Donchian 55/20 · 1h | sell | BTC-USD | 13.63 | -0.24 | stop-loss |
| 2026-09-30T13:40 | Donchian 20/10 · 1h | buy | XRP-USD | 6.25 | — | rebalance up |
| 2026-09-30T13:40 | Donchian 20/10 · 1h | sell | BTC-USD | 15.43 | -0.29 | stop-loss |
| 2026-09-30T13:40 | OBV trend · 1h | sell | BTC-USD | 13.04 | -0.23 | stop-loss |
| 2026-09-30T13:40 | RSI momentum · 1h | sell | BTC-USD | 11.57 | -0.22 | stop-loss |
| 2026-09-30T13:40 | ROC + volume · 1h | buy | XRP-USD | 4.45 | — | rebalance up |
| 2026-09-30T13:40 | ROC + volume · 1h | sell | BTC-USD | 17.59 | -0.33 | stop-loss |
| 2026-09-30T13:40 | Ichimoku · 1h | sell | BTC-USD | 23.38 | -0.44 | stop-loss |
| 2026-09-30T13:40 | EMA 20/50 cross · 1h | buy | META | 8.91 | — | entry |
| 2026-09-30T13:40 | EMA 20/50 cross · 1h | sell | BTC-USD | 8.69 | -0.16 | stop-loss |
| 2026-09-30T13:40 | Williams %R | buy | SQQQ | 17.14 | — | entry signal |
| 2026-09-30T13:40 | Williams %R | buy | META | 17.14 | — | entry signal |
| 2026-09-30T13:40 | Bollinger reversion | buy | META | 18.32 | — | entry signal |
| 2026-09-30T13:40 | Connors RSI(2) | buy | XRP-USD | 18.98 | — | entry signal |
| 2026-09-30T13:40 | Connors RSI(2) | buy | DOGE-USD | 18.98 | — | entry signal |
| 2026-09-30T13:40 | Connors RSI(2) | buy | BTC-USD | 18.98 | — | entry signal |
| 2026-09-30T13:40 | Connors RSI(2) | sell | SOL-USD | 18.74 | -0.36 | stop-loss |
| 2026-09-30T13:40 | Connors RSI(2) | sell | ETH-USD | 18.83 | -0.29 | stop-loss |
| 2026-09-30T13:40 | Three white soldiers | sell | XRP-USD | 23.38 | -0.41 | stop-loss |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
