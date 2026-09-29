# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T12:10:05.000163+00:00 · 5680 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.98 (-0.02%)

Closed trades 17, win rate 70.6%, fees £0.52, max drawdown -1.39%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | — | — | No insider purchases returned |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 9015 decisions in 1803 calls, $0.1260 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T12:10 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-09-29T12:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T12:10 | 5 / 0 / 0 | BTC-USD 34%, ETH-USD 27% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.36 | 1.36 | 1 | 100.0 | 12.70 | 2.77 | -7.55 | 43 |
| 2 | Hold BTC | benchmark | 100.79 | 0.79 | 0 | — | 30.83 | 3.86 | -8.68 | 1 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 11 | RSI(14) reversion · 1h | reversion | 99.97 | -0.03 | 4 | 100.0 | 15.46 | 3.23 | -6.57 | 135 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.79 | -0.21 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.78 | -0.22 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.57 | -0.43 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 17 | Daily: Bullish score | daily | 99.28 | -0.72 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Z-score reversion · 1h | reversion | 99.20 | -0.80 | 7 | 57.1 | 4.37 | 1.07 | -8.60 | 154 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.13 | -0.87 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.12 | -0.88 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Connors RSI(2) · 1h | reversion | 99.11 | -0.89 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 23 | Stochastic reversion · 1h | reversion | 99.10 | -0.91 | 25 | 56.0 | -12.38 | -2.74 | -13.85 | 324 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.02 | -0.98 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | CCI reversion · 1h | reversion | 98.65 | -1.35 | 28 | 42.9 | 1.57 | 0.43 | -12.41 | 405 |
| 27 | Williams %R · 1h | reversion | 98.65 | -1.35 | 33 | 51.5 | -17.95 | -3.30 | -19.54 | 485 |
| 28 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -6.95 | -2.44 | -11.75 | 225 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 30 | Candlestick reversal · 1h | reversion | 98.28 | -1.72 | 13 | 23.1 | -25.49 | -5.97 | -26.04 | 490 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Supertrend · 1h | trend | 98.17 | -1.83 | 11 | 9.1 | 5.69 | 0.95 | -16.43 | 194 |
| 33 | Squeeze breakout · 1h | breakout | 98.13 | -1.87 | 7 | 14.3 | 15.78 | 2.78 | -6.26 | 96 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 98.13 | -1.87 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 35 | EMA 20/50 cross · 1h | trend | 97.97 | -2.03 | 8 | 12.5 | 15.74 | 1.88 | -14.36 | 126 |
| 36 | MACD cross · 1h | trend | 97.59 | -2.41 | 31 | 9.7 | -15.71 | -2.65 | -20.56 | 459 |
| 37 | Bollinger reversion · 1h | reversion | 97.36 | -2.64 | 19 | 31.6 | -17.67 | -4.91 | -17.76 | 306 |
| 38 | Donchian 55/20 · 1h | breakout | 97.26 | -2.74 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.19 | -2.81 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.13 | -2.87 | 79 | 10.1 | 5.18 | 1.05 | -10.35 | 383 |
| 42 | Trend pullback · 1h | trend | 97.10 | -2.90 | 22 | 13.6 | -25.55 | -6.77 | -26.30 | 147 |
| 43 | Parabolic SAR · 1h | trend | 97.08 | -2.92 | 20 | 15.0 | -5.47 | -0.62 | -18.82 | 304 |
| 44 | Bollinger breakout · 1h | breakout | 97.02 | -2.98 | 13 | 7.7 | 13.43 | 1.90 | -9.85 | 285 |
| 45 | Max aggression: 5-day momentum | meta | 96.91 | -3.10 | 1 | 0.0 | 0.45 | 0.39 | -29.56 | 29 |
| 46 | MACD zero-line · 1h | trend | 96.74 | -3.26 | 15 | 6.7 | -3.01 | -0.23 | -14.64 | 221 |
| 47 | RSI momentum · 1h | momentum | 96.55 | -3.45 | 20 | 5.0 | 1.66 | 0.43 | -15.29 | 214 |
| 48 | Triple EMA stack · 1h | trend | 96.13 | -3.87 | 24 | 8.3 | -2.69 | -0.11 | -22.95 | 224 |
| 49 | Ichimoku · 1h | trend | 96.12 | -3.88 | 11 | 9.1 | 8.36 | 1.16 | -15.13 | 121 |
| 50 | ADX DI cross · 1h | trend | 96.05 | -3.95 | 25 | 8.0 | -11.35 | -2.12 | -15.39 | 250 |
| 51 | EMA 9/21 cross · 1h | trend | 95.99 | -4.01 | 34 | 11.8 | 3.68 | 0.70 | -16.92 | 312 |
| 52 | MFI reversion · 1h | reversion | 95.93 | -4.07 | 38 | 13.2 | -9.09 | -1.66 | -17.20 | 125 |
| 53 | Donchian 20/10 · 1h | breakout | 95.78 | -4.22 | 12 | 16.7 | 12.01 | 1.69 | -12.78 | 214 |
| 54 | Max aggression: 1-day momentum | meta | 95.61 | -4.39 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | Three white soldiers | momentum | 95.57 | -4.43 | 41 | 19.5 | -51.78 | -28.65 | -52.20 | 625 |
| 56 | OBV trend · 1h | momentum | 95.57 | -4.43 | 47 | 6.4 | -9.34 | -0.97 | -25.24 | 318 |
| 57 | VWAP momentum · 1h | momentum | 95.51 | -4.49 | 82 | 7.3 | -31.11 | -4.56 | -34.09 | 1248 |
| 58 | Volume breakout · 1h | breakout | 95.18 | -4.82 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 59 | Keltner breakout · 1h | breakout | 95.13 | -4.87 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 60 | Heikin-Ashi · 1h | trend | 94.56 | -5.44 | 35 | 11.4 | -21.95 | -3.25 | -29.64 | 680 |
| 61 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.27 | -22.06 | -71.36 | 1474 |
| 62 | ROC + volume · 1h | momentum | 91.83 | -8.17 | 44 | 6.8 | -4.24 | -0.39 | -17.54 | 404 |
| 63 | Squeeze breakout | breakout | 89.18 | -10.82 | 75 | 6.7 | -60.28 | -18.98 | -60.51 | 1188 |
| 64 | Donchian 55/20 | breakout | 89.12 | -10.88 | 79 | 11.4 | -68.23 | -15.74 | -68.56 | 1332 |
| 65 | EMA 20/50 cross | trend | 88.48 | -11.53 | 97 | 13.4 | -78.76 | -17.66 | -79.34 | 1488 |
| 66 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 67 | ROC + volume | momentum | 88.16 | -11.84 | 123 | 17.1 | -72.18 | -18.09 | -72.77 | 1663 |
| 68 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 69 | Volume breakout | breakout | 87.88 | -12.12 | 82 | 12.2 | -62.45 | -20.64 | -62.73 | 913 |
| 70 | Keltner breakout | breakout | 86.66 | -13.34 | 127 | 10.2 | -84.95 | -35.46 | -85.09 | 1934 |
| 71 | Ichimoku | trend | 86.65 | -13.35 | 94 | 8.5 | -80.53 | -26.52 | -80.60 | 1765 |
| 72 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.39 | -27.89 | -84.48 | 2077 |
| 73 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -70.58 | -16.78 | -71.75 | 1411 |
| 74 | Supertrend | trend | 84.08 | -15.92 | 148 | 16.2 | -87.13 | -24.45 | -87.53 | 1964 |
| 75 | MACD zero-line | trend | 83.55 | -16.45 | 161 | 14.9 | -91.59 | -36.23 | -91.81 | 2367 |
| 76 | Trend pullback | trend | 82.86 | -17.14 | 146 | 17.1 | -90.46 | -33.99 | -90.49 | 2284 |
| 77 | Donchian 20/10 | breakout | 82.47 | -17.53 | 167 | 17.4 | -90.88 | -30.28 | -91.02 | 2690 |
| 78 | MFI reversion | reversion | 82.14 | -17.86 | 155 | 17.4 | -87.77 | -34.75 | -87.92 | 2168 |
| 79 | Triple EMA stack | trend | 82.03 | -17.97 | 179 | 14.5 | -92.99 | -37.35 | -93.09 | 2629 |
| 80 | Bollinger breakout | breakout | 82.01 | -17.99 | 172 | 14.5 | -94.02 | -42.79 | -94.12 | 2884 |
| 81 | RSI momentum | momentum | 81.91 | -18.09 | 161 | 11.2 | -90.47 | -30.38 | -90.67 | 2410 |
| 82 | ADX DI cross | trend | 81.35 | -18.65 | 168 | 6.5 | -89.27 | -46.88 | -89.50 | 2121 |
| 83 | Connors RSI(2) | reversion | 79.81 | -20.19 | 212 | 16.0 | -96.37 | -41.95 | -96.37 | 3650 |
| 84 | EMA 9/21 cross | trend | 78.63 | -21.37 | 231 | 15.2 | -97.36 | -42.29 | -97.43 | 3548 |
| 85 | Consensus | meta | 78.59 | -21.41 | 165 | 7.3 | -94.73 | -30.45 | -94.73 | 2667 |
| 86 | Candlestick reversal | reversion | 78.52 | -21.48 | 208 | 14.4 | -99.34 | -52.09 | -99.34 | 5555 |
| 87 | Stochastic reversion | reversion | 77.93 | -22.07 | 267 | 22.5 | -95.87 | -48.27 | -95.88 | 4052 |
| 88 | OBV trend | momentum | 77.26 | -22.74 | 235 | 13.6 | -95.80 | -50.85 | -95.86 | 3567 |
| 89 | Bollinger reversion | reversion | 76.89 | -23.11 | 249 | 12.4 | -95.71 | -46.40 | -95.72 | 3667 |
| 90 | VWAP momentum | momentum | 75.91 | -24.09 | 301 | 9.0 | -98.45 | -37.03 | -98.47 | 5216 |
| 91 | CCI reversion | reversion | 75.08 | -24.92 | 181 | 5.5 | -98.43 | -52.13 | -98.43 | 4691 |
| 92 | Parabolic SAR | trend | 74.23 | -25.77 | 254 | 13.0 | -96.95 | -58.01 | -97.01 | 3668 |
| 93 | Williams %R | reversion | 73.53 | -26.47 | 266 | 18.8 | -99.52 | -62.21 | -99.52 | 6091 |
| 94 | MACD cross | trend | 73.36 | -26.64 | 207 | 10.6 | -99.70 | -65.67 | -99.71 | 6096 |
| 95 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.95 | -99.89 | 8339 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T12:05 | Ichimoku | buy | DOGE-USD | 21.69 | — | entry signal |
| 2026-09-29T12:00 | Z-score reversion · 1h | sell | SOL-USD | 16.42 | 0.06 | exit signal |
| 2026-09-29T12:00 | ROC + volume · 1h | buy | ETH-USD | 21.34 | — | entry signal |
| 2026-09-29T11:55 | Volume breakout | buy | XRP-USD | 13.27 | — | entry signal |
| 2026-09-29T11:55 | Volume breakout | buy | SOL-USD | 17.64 | — | entry signal |
| 2026-09-29T11:55 | Volume breakout | buy | BTC-USD | 17.64 | — | entry signal |
| 2026-09-29T11:55 | Volume breakout | sell | ETH-USD | 4.40 | -0.02 | rebalance down |
| 2026-09-29T11:55 | Trend pullback | sell | XRP-USD | 16.60 | 0.07 | take-profit |
| 2026-09-29T11:51 | Keltner breakout | sell | ETH-USD | 4.35 | -0.02 | rebalance down |
| 2026-09-29T11:51 | Bollinger breakout | buy | SOL-USD | 4.11 | — | rebalance up |
| 2026-09-29T11:51 | Bollinger breakout | sell | ETH-USD | 4.11 | -0.02 | rebalance down |
| 2026-09-29T11:51 | Donchian 20/10 | sell | ETH-USD | 4.14 | -0.02 | rebalance down |
| 2026-09-29T11:51 | OBV trend | buy | DOGE-USD | 3.86 | — | rebalance up |
| 2026-09-29T11:51 | OBV trend | sell | SOL-USD | 3.86 | -0.01 | rebalance down |
| 2026-09-29T11:50 | Consensus | buy | XRP-USD | 15.75 | — | entry |
| 2026-09-29T11:50 | Consensus | buy | SOL-USD | 15.77 | — | entry |
| 2026-09-29T11:50 | Consensus | buy | BTC-USD | 15.77 | — | entry |
| 2026-09-29T11:50 | Consensus | sell | ETH-USD | 4.13 | 0.02 | rebalance down |
| 2026-09-29T11:50 | Consensus | sell | DOGE-USD | 3.93 | -0.01 | rebalance down |
| 2026-09-29T11:50 | Candlestick reversal | sell | SOL-USD | 19.63 | -0.01 | take-profit |
| 2026-09-29T11:50 | Candlestick reversal | sell | DOGE-USD | 19.66 | 0.04 | take-profit |
| 2026-09-29T11:50 | Candlestick reversal | sell | BTC-USD | 19.56 | -0.05 | take-profit |
| 2026-09-29T11:50 | Volume breakout | buy | DOGE-USD | 22.06 | — | entry signal |
| 2026-09-29T11:50 | Keltner breakout | buy | XRP-USD | 13.07 | — | entry signal |
| 2026-09-29T11:50 | Keltner breakout | buy | SOL-USD | 17.39 | — | entry signal |
| 2026-09-29T11:50 | Keltner breakout | buy | DOGE-USD | 17.39 | — | entry signal |
| 2026-09-29T11:50 | Keltner breakout | buy | BTC-USD | 17.39 | — | entry signal |
| 2026-09-29T11:50 | Bollinger breakout | buy | SOL-USD | 12.35 | — | entry signal |
| 2026-09-29T11:50 | Bollinger breakout | buy | DOGE-USD | 16.46 | — | entry signal |
| 2026-09-29T11:50 | Bollinger breakout | buy | BTC-USD | 16.46 | — | entry signal |
| 2026-09-29T11:50 | Bollinger breakout | sell | XRP-USD | 4.12 | -0.01 | rebalance down |
| 2026-09-29T11:50 | Donchian 55/20 | buy | XRP-USD | 17.54 | — | entry signal |
| 2026-09-29T11:50 | Donchian 55/20 | buy | BTC-USD | 17.87 | — | entry signal |
| 2026-09-29T11:50 | Donchian 55/20 | sell | SOL-USD | 4.52 | 0.03 | rebalance down |
| 2026-09-29T11:50 | Donchian 20/10 | buy | XRP-USD | 12.44 | — | entry signal |
| 2026-09-29T11:50 | Donchian 20/10 | buy | SOL-USD | 16.55 | — | entry signal |
| 2026-09-29T11:50 | Donchian 20/10 | buy | DOGE-USD | 16.55 | — | entry signal |
| 2026-09-29T11:50 | Donchian 20/10 | buy | BTC-USD | 16.55 | — | entry signal |
| 2026-09-29T11:50 | OBV trend | buy | DOGE-USD | 11.62 | — | entry signal |
| 2026-09-29T11:50 | OBV trend | buy | BTC-USD | 15.50 | — | entry signal |

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
