# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T11:40:05.000184+00:00 · 5651 ticks

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

Today: 8580 decisions in 1716 calls, $0.1200 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T11:40 | 2 / 2 / 1 | XRP-USD 14% |  |
| Breezy | 2026-09-29T11:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T11:40 | 5 / 0 / 0 | ETH-USD 34%, XRP-USD 34% |  |

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
| 2 | Hold BTC | benchmark | 100.68 | 0.69 | 0 | — | 30.67 | 3.84 | -8.68 | 1 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 11 | RSI(14) reversion · 1h | reversion | 99.97 | -0.03 | 4 | 100.0 | 13.67 | 2.85 | -6.57 | 140 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.79 | -0.21 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.78 | -0.22 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.57 | -0.43 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.94 | -4.41 | -14.79 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 17 | Daily: Bullish score | daily | 99.28 | -0.72 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Z-score reversion · 1h | reversion | 99.20 | -0.80 | 6 | 50.0 | 4.38 | 1.07 | -8.60 | 154 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.13 | -0.87 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.12 | -0.88 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Connors RSI(2) · 1h | reversion | 99.11 | -0.89 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 23 | Stochastic reversion · 1h | reversion | 99.10 | -0.91 | 25 | 56.0 | -12.27 | -2.72 | -13.74 | 324 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.02 | -0.98 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | CCI reversion · 1h | reversion | 98.65 | -1.35 | 28 | 42.9 | 1.57 | 0.43 | -12.41 | 405 |
| 27 | Williams %R · 1h | reversion | 98.65 | -1.35 | 33 | 51.5 | -17.89 | -3.29 | -19.48 | 485 |
| 28 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -6.95 | -2.44 | -11.75 | 225 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 30 | Candlestick reversal · 1h | reversion | 98.25 | -1.75 | 13 | 23.1 | -25.90 | -6.03 | -26.46 | 493 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Supertrend · 1h | trend | 98.15 | -1.85 | 11 | 9.1 | 5.66 | 0.95 | -16.43 | 194 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 98.13 | -1.87 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 34 | Squeeze breakout · 1h | breakout | 98.09 | -1.91 | 7 | 14.3 | 16.43 | 2.88 | -6.26 | 94 |
| 35 | EMA 20/50 cross · 1h | trend | 97.95 | -2.05 | 8 | 12.5 | 15.62 | 1.87 | -14.36 | 126 |
| 36 | MACD cross · 1h | trend | 97.48 | -2.52 | 31 | 9.7 | -15.97 | -2.70 | -20.74 | 460 |
| 37 | Bollinger reversion · 1h | reversion | 97.36 | -2.64 | 19 | 31.6 | -17.68 | -4.91 | -17.77 | 306 |
| 38 | Donchian 55/20 · 1h | breakout | 97.26 | -2.74 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.19 | -2.81 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.13 | -2.87 | 79 | 10.1 | 6.23 | 1.21 | -10.97 | 390 |
| 42 | Trend pullback · 1h | trend | 97.10 | -2.90 | 22 | 13.6 | -25.55 | -6.77 | -26.30 | 147 |
| 43 | Parabolic SAR · 1h | trend | 97.04 | -2.96 | 20 | 15.0 | -5.56 | -0.63 | -18.82 | 304 |
| 44 | Bollinger breakout · 1h | breakout | 96.98 | -3.02 | 13 | 7.7 | 13.39 | 1.89 | -9.85 | 285 |
| 45 | Max aggression: 5-day momentum | meta | 96.66 | -3.34 | 1 | 0.0 | 0.20 | 0.36 | -29.56 | 29 |
| 46 | MACD zero-line · 1h | trend | 96.53 | -3.47 | 15 | 6.7 | -3.20 | -0.26 | -14.64 | 221 |
| 47 | RSI momentum · 1h | momentum | 96.49 | -3.51 | 20 | 5.0 | 1.60 | 0.42 | -15.29 | 214 |
| 48 | Triple EMA stack · 1h | trend | 96.09 | -3.91 | 24 | 8.3 | -2.75 | -0.11 | -22.95 | 224 |
| 49 | Ichimoku · 1h | trend | 96.06 | -3.94 | 11 | 9.1 | 8.29 | 1.15 | -15.13 | 121 |
| 50 | ADX DI cross · 1h | trend | 95.97 | -4.03 | 25 | 8.0 | -11.42 | -2.13 | -15.39 | 250 |
| 51 | EMA 9/21 cross · 1h | trend | 95.96 | -4.04 | 34 | 11.8 | 3.04 | 0.61 | -16.92 | 315 |
| 52 | MFI reversion · 1h | reversion | 95.88 | -4.12 | 38 | 13.2 | -9.14 | -1.67 | -17.20 | 125 |
| 53 | Donchian 20/10 · 1h | breakout | 95.73 | -4.27 | 12 | 16.7 | 11.93 | 1.68 | -12.78 | 214 |
| 54 | Max aggression: 1-day momentum | meta | 95.61 | -4.39 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | Three white soldiers | momentum | 95.57 | -4.43 | 41 | 19.5 | -51.78 | -28.65 | -52.20 | 625 |
| 56 | OBV trend · 1h | momentum | 95.53 | -4.47 | 47 | 6.4 | -9.46 | -0.98 | -25.24 | 318 |
| 57 | VWAP momentum · 1h | momentum | 95.46 | -4.54 | 82 | 7.3 | -31.19 | -4.57 | -34.09 | 1248 |
| 58 | Volume breakout · 1h | breakout | 95.18 | -4.82 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 59 | Keltner breakout · 1h | breakout | 95.13 | -4.87 | 7 | 0.0 | -0.48 | 0.14 | -18.68 | 221 |
| 60 | Heikin-Ashi · 1h | trend | 94.39 | -5.61 | 35 | 11.4 | -22.09 | -3.28 | -29.64 | 680 |
| 61 | ROC + volume · 1h | momentum | 91.91 | -8.09 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 62 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.32 | -22.10 | -71.40 | 1476 |
| 63 | Squeeze breakout | breakout | 89.18 | -10.82 | 75 | 6.7 | -60.35 | -19.03 | -60.49 | 1187 |
| 64 | Donchian 55/20 | breakout | 89.14 | -10.86 | 79 | 11.4 | -68.22 | -15.73 | -68.56 | 1330 |
| 65 | ROC + volume | momentum | 88.53 | -11.47 | 123 | 17.1 | -72.06 | -18.01 | -72.65 | 1659 |
| 66 | EMA 20/50 cross | trend | 88.30 | -11.70 | 97 | 13.4 | -78.76 | -17.69 | -79.29 | 1487 |
| 67 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 68 | Volume breakout | breakout | 88.17 | -11.83 | 82 | 12.2 | -62.39 | -20.58 | -62.60 | 910 |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Keltner breakout | breakout | 86.91 | -13.09 | 127 | 10.2 | -84.91 | -35.29 | -85.04 | 1930 |
| 71 | Ichimoku | trend | 86.71 | -13.29 | 94 | 8.5 | -80.52 | -26.50 | -80.59 | 1763 |
| 72 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.40 | -27.92 | -84.48 | 2078 |
| 73 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -70.73 | -16.97 | -71.75 | 1414 |
| 74 | Supertrend | trend | 83.94 | -16.06 | 148 | 16.2 | -87.23 | -24.67 | -87.53 | 1965 |
| 75 | MACD zero-line | trend | 83.45 | -16.55 | 161 | 14.9 | -91.60 | -36.28 | -91.81 | 2367 |
| 76 | Trend pullback | trend | 82.79 | -17.21 | 143 | 15.4 | -90.47 | -34.02 | -90.49 | 2284 |
| 77 | Donchian 20/10 | breakout | 82.71 | -17.29 | 167 | 17.4 | -90.87 | -30.23 | -91.02 | 2687 |
| 78 | MFI reversion | reversion | 82.21 | -17.79 | 154 | 17.5 | -87.76 | -34.69 | -87.92 | 2168 |
| 79 | Bollinger breakout | breakout | 82.14 | -17.86 | 172 | 14.5 | -93.99 | -42.59 | -94.09 | 2880 |
| 80 | Triple EMA stack | trend | 81.85 | -18.14 | 179 | 14.5 | -92.99 | -37.39 | -93.08 | 2629 |
| 81 | RSI momentum | momentum | 81.72 | -18.28 | 161 | 11.2 | -90.52 | -30.47 | -90.70 | 2410 |
| 82 | ADX DI cross | trend | 81.35 | -18.65 | 168 | 6.5 | -89.30 | -47.22 | -89.50 | 2122 |
| 83 | Connors RSI(2) | reversion | 79.81 | -20.19 | 212 | 16.0 | -96.38 | -41.95 | -96.38 | 3653 |
| 84 | Consensus | meta | 78.71 | -21.29 | 165 | 7.3 | -94.78 | -30.74 | -94.79 | 2670 |
| 85 | Candlestick reversal | reversion | 78.50 | -21.50 | 205 | 14.1 | -99.34 | -52.25 | -99.34 | 5557 |
| 86 | EMA 9/21 cross | trend | 78.46 | -21.54 | 231 | 15.2 | -97.38 | -42.69 | -97.43 | 3550 |
| 87 | Stochastic reversion | reversion | 77.93 | -22.07 | 267 | 22.5 | -95.88 | -48.41 | -95.89 | 4054 |
| 88 | OBV trend | momentum | 77.27 | -22.73 | 235 | 13.6 | -95.80 | -50.84 | -95.86 | 3565 |
| 89 | Bollinger reversion | reversion | 76.89 | -23.11 | 249 | 12.4 | -95.72 | -46.43 | -95.72 | 3669 |
| 90 | VWAP momentum | momentum | 75.74 | -24.26 | 301 | 9.0 | -98.46 | -37.13 | -98.48 | 5217 |
| 91 | CCI reversion | reversion | 75.08 | -24.92 | 181 | 5.5 | -98.43 | -52.35 | -98.43 | 4694 |
| 92 | Parabolic SAR | trend | 74.07 | -25.93 | 254 | 13.0 | -96.96 | -58.10 | -97.01 | 3668 |
| 93 | Williams %R | reversion | 73.53 | -26.47 | 266 | 18.8 | -99.52 | -62.30 | -99.52 | 6091 |
| 94 | MACD cross | trend | 73.20 | -26.80 | 207 | 10.6 | -99.70 | -66.82 | -99.71 | 6099 |
| 95 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -93.12 | -99.89 | 8338 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T11:40 | Consensus | buy | DOGE-USD | 19.69 | — | entry |
| 2026-09-29T11:40 | Supertrend | buy | DOGE-USD | 21.00 | — | entry |
| 2026-09-29T11:36 | Parabolic SAR | buy | SOL-USD | 7.42 | — | rebalance up |
| 2026-09-29T11:36 | Parabolic SAR | sell | XRP-USD | 3.71 | -0.01 | rebalance down |
| 2026-09-29T11:36 | Parabolic SAR | sell | ETH-USD | 3.71 | -0.01 | rebalance down |
| 2026-09-29T11:36 | MACD cross | buy | XRP-USD | 3.66 | — | rebalance up |
| 2026-09-29T11:36 | MACD cross | sell | ETH-USD | 3.69 | -0.01 | rebalance down |
| 2026-09-29T11:36 | Triple EMA stack | buy | SOL-USD | 4.09 | — | rebalance up |
| 2026-09-29T11:36 | Triple EMA stack | sell | XRP-USD | 4.09 | -0.02 | rebalance down |
| 2026-09-29T11:36 | EMA 9/21 cross | buy | SOL-USD | 3.92 | — | rebalance up |
| 2026-09-29T11:36 | EMA 9/21 cross | sell | XRP-USD | 3.92 | -0.02 | rebalance down |
| 2026-09-29T11:35 | Williams %R | sell | XRP-USD | 14.71 | -0.03 | exit signal |
| 2026-09-29T11:35 | Williams %R | sell | SOL-USD | 18.38 | -0.06 | exit signal |
| 2026-09-29T11:35 | Williams %R | sell | ETH-USD | 14.71 | -0.02 | exit signal |
| 2026-09-29T11:35 | Williams %R | sell | DOGE-USD | 11.06 | -0.01 | exit signal |
| 2026-09-29T11:35 | Williams %R | sell | BTC-USD | 14.66 | -0.07 | exit signal |
| 2026-09-29T11:35 | Stochastic reversion | sell | XRP-USD | 15.59 | -0.03 | exit signal |
| 2026-09-29T11:35 | Stochastic reversion | sell | SOL-USD | 15.58 | -0.05 | exit signal |
| 2026-09-29T11:35 | Stochastic reversion | sell | ETH-USD | 11.74 | -0.01 | exit signal |
| 2026-09-29T11:35 | Stochastic reversion | sell | DOGE-USD | 15.59 | -0.03 | exit signal |
| 2026-09-29T11:35 | Stochastic reversion | sell | BTC-USD | 15.54 | -0.08 | exit signal |
| 2026-09-29T11:35 | Volume breakout | buy | ETH-USD | 22.07 | — | entry signal |
| 2026-09-29T11:35 | Keltner breakout | buy | ETH-USD | 21.75 | — | entry signal |
| 2026-09-29T11:35 | Bollinger breakout | buy | XRP-USD | 20.57 | — | entry signal |
| 2026-09-29T11:35 | Bollinger breakout | buy | ETH-USD | 20.57 | — | entry signal |
| 2026-09-29T11:35 | Donchian 20/10 | buy | ETH-USD | 20.70 | — | entry signal |
| 2026-09-29T11:35 | OBV trend | buy | SOL-USD | 19.35 | — | entry signal |
| 2026-09-29T11:35 | RSI momentum | buy | XRP-USD | 16.27 | — | entry signal |
| 2026-09-29T11:35 | RSI momentum | buy | SOL-USD | 16.39 | — | entry signal |
| 2026-09-29T11:35 | RSI momentum | buy | DOGE-USD | 16.39 | — | entry signal |
| 2026-09-29T11:35 | RSI momentum | buy | BTC-USD | 16.39 | — | entry signal |
| 2026-09-29T11:35 | Trend pullback | buy | SOL-USD | 12.55 | — | entry signal |
| 2026-09-29T11:35 | Trend pullback | sell | XRP-USD | 4.18 | 0.00 | rebalance down |
| 2026-09-29T11:35 | Trend pullback | sell | ETH-USD | 4.18 | 0.00 | rebalance down |
| 2026-09-29T11:35 | Trend pullback | sell | DOGE-USD | 4.19 | 0.00 | rebalance down |
| 2026-09-29T11:35 | Ichimoku | buy | BTC-USD | 21.70 | — | entry signal |
| 2026-09-29T11:35 | Parabolic SAR | buy | SOL-USD | 3.76 | — | entry signal |
| 2026-09-29T11:35 | Parabolic SAR | buy | DOGE-USD | 14.84 | — | entry signal |
| 2026-09-29T11:35 | MACD zero-line | buy | SOL-USD | 20.90 | — | entry signal |
| 2026-09-29T11:35 | MACD zero-line | buy | DOGE-USD | 20.90 | — | entry signal |

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
