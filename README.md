# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T01:40:05.000130+00:00 · 5161 ticks

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
| Copy: Insider buying | 2026-09-28 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 1240 decisions in 248 calls, $0.0175 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T01:40 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-09-29T01:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T01:40 | 4 / 1 / 0 | ETH-USD 26%, SOL-USD 22% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |
| CCI reversion | AMD | 2.08 | +3.00% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.36 | 1.36 | 1 | 100.0 | 12.70 | 2.77 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.72 | -0.28 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.71 | -0.29 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 12 | Hold SPY | benchmark | 99.50 | -0.50 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 13 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 14 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.05 | -4.73 | 190 |
| 15 | Daily: Bullish score | daily | 99.22 | -0.78 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.77 | -5.16 | 28 |
| 17 | RSI(14) reversion · 1h | reversion | 99.08 | -0.92 | 2 | 100.0 | 14.15 | 2.97 | -6.57 | 136 |
| 18 | Connors RSI(2) · 1h | reversion | 99.07 | -0.93 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 99.06 | -0.94 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 99.05 | -0.95 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 98.96 | -1.04 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 22 | Hold BTC | benchmark | 98.93 | -1.07 | 0 | — | 29.12 | 3.68 | -8.68 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 24 | Stochastic reversion · 1h | reversion | 98.64 | -1.35 | 23 | 56.5 | -12.75 | -2.83 | -13.85 | 323 |
| 25 | Copy: Insider buying | copy | 98.55 | -1.45 | 2 | 100.0 | -12.69 | -2.44 | -17.74 | 73 |
| 26 | Williams %R · 1h | reversion | 98.52 | -1.48 | 29 | 51.7 | -18.51 | -3.41 | -20.37 | 488 |
| 27 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -8.05 | -2.83 | -11.75 | 232 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.21 | -1.79 | 23 | 34.8 | 1.26 | 0.38 | -12.41 | 409 |
| 30 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 31 | Z-score reversion · 1h | reversion | 98.07 | -1.93 | 4 | 25.0 | 2.86 | 0.74 | -8.60 | 155 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.06 | -1.94 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.02 | -1.98 | 7 | 14.3 | 15.68 | 2.76 | -6.26 | 95 |
| 34 | Candlestick reversal · 1h | reversion | 97.95 | -2.05 | 12 | 16.7 | -25.38 | -6.00 | -25.98 | 483 |
| 35 | EMA 20/50 cross · 1h | trend | 97.87 | -2.13 | 8 | 12.5 | 15.66 | 1.87 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.65 | -2.35 | 11 | 9.1 | 3.89 | 0.72 | -16.43 | 196 |
| 37 | Bollinger reversion · 1h | reversion | 97.30 | -2.70 | 19 | 31.6 | -17.61 | -4.89 | -17.88 | 308 |
| 38 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.74 | -16.14 | 692 |
| 39 | Donchian 55/20 · 1h | breakout | 97.21 | -2.79 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.12 | -2.88 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.06 | -2.94 | 79 | 10.1 | 2.98 | 0.67 | -12.01 | 389 |
| 42 | Trend pullback · 1h | trend | 97.05 | -2.95 | 22 | 13.6 | -26.02 | -6.92 | -26.61 | 149 |
| 43 | MACD cross · 1h | trend | 96.95 | -3.05 | 29 | 10.3 | -16.26 | -2.75 | -20.81 | 455 |
| 44 | Parabolic SAR · 1h | trend | 96.94 | -3.06 | 19 | 15.8 | -5.58 | -0.63 | -18.82 | 300 |
| 45 | Bollinger breakout · 1h | breakout | 96.85 | -3.15 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 46 | MACD zero-line · 1h | trend | 96.69 | -3.31 | 14 | 7.1 | -3.35 | -0.28 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.44 | -3.56 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Triple EMA stack · 1h | trend | 95.98 | -4.03 | 24 | 8.3 | -2.85 | -0.13 | -22.95 | 223 |
| 49 | EMA 9/21 cross · 1h | trend | 95.95 | -4.05 | 33 | 12.1 | 2.85 | 0.59 | -16.92 | 312 |
| 50 | Ichimoku · 1h | trend | 95.93 | -4.07 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 51 | Three white soldiers | momentum | 95.87 | -4.13 | 34 | 11.8 | -51.81 | -28.38 | -51.81 | 620 |
| 52 | ADX DI cross · 1h | trend | 95.85 | -4.15 | 25 | 8.0 | -11.67 | -2.19 | -15.39 | 249 |
| 53 | Donchian 20/10 · 1h | breakout | 95.79 | -4.21 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 54 | Max aggression: 1-day momentum | meta | 95.55 | -4.45 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | OBV trend · 1h | momentum | 95.43 | -4.57 | 47 | 6.4 | -9.43 | -0.98 | -25.24 | 317 |
| 56 | MFI reversion · 1h | reversion | 95.29 | -4.71 | 38 | 13.2 | -10.13 | -1.88 | -17.20 | 126 |
| 57 | Volume breakout · 1h | breakout | 95.16 | -4.84 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 58 | Keltner breakout · 1h | breakout | 95.11 | -4.89 | 7 | 0.0 | -0.52 | 0.14 | -18.68 | 221 |
| 59 | VWAP momentum · 1h | momentum | 95.05 | -4.95 | 82 | 7.3 | -33.45 | -4.98 | -33.96 | 1250 |
| 60 | Heikin-Ashi · 1h | trend | 94.32 | -5.68 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 61 | Max aggression: 5-day momentum | meta | 93.97 | -6.03 | 1 | 0.0 | -2.53 | 0.14 | -29.56 | 29 |
| 62 | RSI(14) reversion | reversion | 92.20 | -7.80 | 88 | 35.2 | -71.17 | -21.96 | -71.25 | 1476 |
| 63 | ROC + volume · 1h | momentum | 91.86 | -8.14 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 64 | AI bee: Bizzy | ai | 90.62 | -9.38 | 200 | 13.5 | — | — | — | — |
| 65 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.84 | -18.63 | -59.92 | 1179 |
| 66 | ROC + volume | momentum | 89.31 | -10.69 | 115 | 16.5 | -71.92 | -17.85 | -72.35 | 1655 |
| 67 | Volume breakout | breakout | 88.63 | -11.37 | 76 | 9.2 | -62.56 | -20.50 | -62.56 | 908 |
| 68 | Donchian 55/20 | breakout | 88.55 | -11.45 | 77 | 11.7 | -68.81 | -15.95 | -68.82 | 1331 |
| 69 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.50 | -26.27 | -80.50 | 1755 |
| 71 | EMA 20/50 cross | trend | 87.61 | -12.39 | 95 | 13.7 | -78.99 | -17.85 | -79.11 | 1483 |
| 72 | Keltner breakout | breakout | 87.49 | -12.51 | 120 | 10.0 | -84.93 | -35.02 | -84.94 | 1928 |
| 73 | Z-score reversion | reversion | 85.99 | -14.01 | 143 | 29.4 | -84.67 | -28.43 | -84.67 | 2084 |
| 74 | VWAP reversion | reversion | 85.12 | -14.88 | 103 | 13.6 | -70.54 | -16.54 | -71.87 | 1402 |
| 75 | MACD zero-line | trend | 84.66 | -15.34 | 154 | 15.6 | -91.51 | -35.76 | -91.68 | 2365 |
| 76 | RSI momentum | momentum | 84.06 | -15.94 | 145 | 11.0 | -90.39 | -29.94 | -90.41 | 2398 |
| 77 | Bollinger breakout | breakout | 84.00 | -16.00 | 158 | 14.6 | -93.94 | -42.03 | -93.95 | 2874 |
| 78 | Supertrend | trend | 83.97 | -16.03 | 142 | 15.5 | -87.31 | -24.94 | -87.39 | 1963 |
| 79 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.53 | -33.79 | -90.53 | 2281 |
| 80 | Triple EMA stack | trend | 82.99 | -17.01 | 169 | 13.6 | -93.05 | -37.12 | -93.08 | 2628 |
| 81 | Donchian 20/10 | breakout | 82.73 | -17.27 | 159 | 15.1 | -90.94 | -30.26 | -90.95 | 2686 |
| 82 | MFI reversion | reversion | 82.11 | -17.89 | 151 | 16.6 | -87.81 | -34.99 | -87.91 | 2174 |
| 83 | ADX DI cross | trend | 82.08 | -17.92 | 160 | 6.9 | -89.40 | -48.12 | -89.40 | 2129 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.43 | -42.10 | -96.43 | 3653 |
| 85 | Candlestick reversal | reversion | 79.89 | -20.11 | 188 | 14.4 | -99.36 | -52.25 | -99.36 | 5565 |
| 86 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.75 | -30.40 | -94.75 | 2662 |
| 87 | EMA 9/21 cross | trend | 78.91 | -21.09 | 221 | 13.6 | -97.41 | -42.89 | -97.42 | 3548 |
| 88 | Stochastic reversion | reversion | 78.72 | -21.28 | 252 | 23.8 | -95.95 | -48.92 | -95.95 | 4059 |
| 89 | OBV trend | momentum | 78.46 | -21.54 | 220 | 12.7 | -95.86 | -50.82 | -95.86 | 3564 |
| 90 | Bollinger reversion | reversion | 77.78 | -22.22 | 238 | 13.0 | -95.79 | -46.33 | -95.79 | 3678 |
| 91 | VWAP momentum | momentum | 76.72 | -23.28 | 287 | 9.4 | -98.48 | -36.80 | -98.48 | 5210 |
| 92 | Parabolic SAR | trend | 76.69 | -23.31 | 229 | 12.2 | -96.96 | -58.00 | -96.96 | 3655 |
| 93 | CCI reversion | reversion | 76.13 | -23.87 | 163 | 5.5 | -98.47 | -52.68 | -98.47 | 4699 |
| 94 | MACD cross | trend | 75.67 | -24.33 | 182 | 8.2 | -99.70 | -66.54 | -99.70 | 6090 |
| 95 | Williams %R | reversion | 74.93 | -25.07 | 238 | 20.6 | -99.53 | -62.48 | -99.53 | 6089 |
| 96 | Heikin-Ashi | trend | 74.79 | -25.21 | 194 | 3.1 | -99.89 | -86.40 | -99.89 | 8317 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T01:40 | MACD cross · 1h | buy | ETH-USD | 5.41 | — | rebalance up |
| 2026-09-29T01:40 | MACD cross · 1h | sell | SOL-USD | 10.60 | -0.30 | stop-loss |
| 2026-09-29T01:40 | Williams %R | sell | XRP-USD | 18.61 | -0.29 | stop-loss |
| 2026-09-29T01:40 | Stochastic reversion | buy | SOL-USD | 3.95 | — | rebalance up |
| 2026-09-29T01:40 | Stochastic reversion | sell | XRP-USD | 15.66 | -0.25 | stop-loss |
| 2026-09-29T01:40 | Stochastic reversion | sell | DOGE-USD | 15.69 | -0.22 | stop-loss |
| 2026-09-29T01:40 | VWAP reversion | sell | DOGE-USD | 21.09 | -0.29 | stop-loss |
| 2026-09-29T01:40 | Z-score reversion | sell | XRP-USD | 21.33 | -0.34 | stop-loss |
| 2026-09-29T01:40 | Bollinger reversion | buy | SOL-USD | 3.91 | — | rebalance up |
| 2026-09-29T01:40 | Bollinger reversion | sell | XRP-USD | 15.47 | -0.24 | stop-loss |
| 2026-09-29T01:40 | Bollinger reversion | sell | DOGE-USD | 15.50 | -0.22 | stop-loss |
| 2026-09-29T01:40 | RSI(14) reversion | buy | SOL-USD | 4.63 | — | rebalance up |
| 2026-09-29T01:40 | RSI(14) reversion | sell | XRP-USD | 18.34 | -0.29 | stop-loss |
| 2026-09-29T01:40 | RSI(14) reversion | sell | DOGE-USD | 18.37 | -0.25 | stop-loss |
| 2026-09-29T01:40 | Candlestick reversal | sell | SOL-USD | 19.88 | -0.18 | exit signal |
| 2026-09-29T01:35 | VWAP reversion | buy | SOL-USD | 21.34 | — | entry signal |
| 2026-09-29T01:35 | Candlestick reversal | buy | XRP-USD | 20.06 | — | entry signal |
| 2026-09-29T01:35 | Candlestick reversal | buy | SOL-USD | 20.06 | — | entry signal |
| 2026-09-29T01:25 | MFI reversion | buy | ETH-USD | 20.58 | — | entry signal |
| 2026-09-29T01:25 | MFI reversion | buy | BTC-USD | 20.58 | — | entry signal |
| 2026-09-29T01:25 | Williams %R | buy | XRP-USD | 18.90 | — | entry signal |
| 2026-09-29T01:25 | Williams %R | buy | SOL-USD | 18.90 | — | entry signal |
| 2026-09-29T01:25 | Williams %R | buy | ETH-USD | 18.90 | — | entry signal |
| 2026-09-29T01:25 | Williams %R | buy | BTC-USD | 18.90 | — | entry signal |
| 2026-09-29T01:25 | Stochastic reversion | buy | XRP-USD | 15.91 | — | entry signal |
| 2026-09-29T01:25 | Stochastic reversion | buy | SOL-USD | 15.91 | — | entry signal |
| 2026-09-29T01:25 | Stochastic reversion | buy | ETH-USD | 15.91 | — | entry signal |
| 2026-09-29T01:25 | Stochastic reversion | buy | DOGE-USD | 15.91 | — | entry signal |
| 2026-09-29T01:25 | Stochastic reversion | buy | BTC-USD | 15.91 | — | entry signal |
| 2026-09-29T01:25 | VWAP reversion | buy | DOGE-USD | 21.39 | — | entry signal |
| 2026-09-29T01:25 | Z-score reversion | buy | XRP-USD | 21.67 | — | entry signal |
| 2026-09-29T01:25 | Z-score reversion | buy | SOL-USD | 21.67 | — | entry signal |
| 2026-09-29T01:25 | Z-score reversion | buy | ETH-USD | 21.67 | — | entry signal |
| 2026-09-29T01:25 | Bollinger reversion | buy | XRP-USD | 15.72 | — | entry signal |
| 2026-09-29T01:25 | Bollinger reversion | buy | SOL-USD | 15.72 | — | entry signal |
| 2026-09-29T01:25 | Bollinger reversion | buy | ETH-USD | 15.72 | — | entry signal |
| 2026-09-29T01:25 | Bollinger reversion | buy | DOGE-USD | 15.72 | — | entry signal |
| 2026-09-29T01:25 | Bollinger reversion | buy | BTC-USD | 15.72 | — | entry signal |
| 2026-09-29T01:25 | RSI(14) reversion | buy | XRP-USD | 18.63 | — | entry signal |
| 2026-09-29T01:25 | RSI(14) reversion | buy | SOL-USD | 18.63 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
