# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T02:40:05.000151+00:00 · 5214 ticks

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

Today: 2035 decisions in 407 calls, $0.0286 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T02:40 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-09-29T02:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T02:40 | 5 / 0 / 0 | SOL-USD 32%, ETH-USD 30% |  |

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
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.71 | -0.29 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.70 | -0.30 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 12 | Hold SPY | benchmark | 99.49 | -0.51 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 13 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 14 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 15 | Daily: Bullish score | daily | 99.21 | -0.80 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.36 | -2.74 | -5.16 | 28 |
| 17 | RSI(14) reversion · 1h | reversion | 99.10 | -0.90 | 2 | 100.0 | 12.12 | 2.53 | -6.57 | 144 |
| 18 | Hold BTC | benchmark | 99.07 | -0.93 | 0 | — | 29.84 | 3.76 | -8.68 | 1 |
| 19 | Connors RSI(2) · 1h | reversion | 99.07 | -0.93 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.05 | -0.95 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.04 | -0.96 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.94 | -1.05 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 24 | Stochastic reversion · 1h | reversion | 98.66 | -1.34 | 23 | 56.5 | -12.72 | -2.83 | -13.85 | 323 |
| 25 | Copy: Insider buying | copy | 98.54 | -1.46 | 2 | 100.0 | -12.69 | -2.44 | -17.74 | 73 |
| 26 | Williams %R · 1h | reversion | 98.48 | -1.52 | 30 | 50.0 | -18.49 | -3.41 | -20.33 | 488 |
| 27 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.88 | -2.76 | -11.75 | 233 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 29 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 30 | CCI reversion · 1h | reversion | 98.19 | -1.81 | 24 | 33.3 | 1.34 | 0.39 | -12.41 | 408 |
| 31 | Z-score reversion · 1h | reversion | 98.12 | -1.88 | 4 | 25.0 | 2.92 | 0.76 | -8.60 | 155 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.05 | -1.95 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.02 | -1.98 | 7 | 14.3 | 15.96 | 2.81 | -6.26 | 94 |
| 34 | Candlestick reversal · 1h | reversion | 97.90 | -2.10 | 12 | 16.7 | -26.29 | -6.16 | -26.59 | 490 |
| 35 | EMA 20/50 cross · 1h | trend | 97.86 | -2.14 | 8 | 12.5 | 15.79 | 1.88 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.64 | -2.36 | 11 | 9.1 | 3.25 | 0.64 | -16.43 | 197 |
| 37 | Bollinger reversion · 1h | reversion | 97.29 | -2.71 | 19 | 31.6 | -17.67 | -4.91 | -17.76 | 306 |
| 38 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 39 | Donchian 55/20 · 1h | breakout | 97.20 | -2.79 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.11 | -2.89 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.05 | -2.95 | 79 | 10.1 | 0.63 | 0.27 | -12.33 | 399 |
| 42 | Trend pullback · 1h | trend | 97.04 | -2.96 | 22 | 13.6 | -25.73 | -6.83 | -26.36 | 148 |
| 43 | Parabolic SAR · 1h | trend | 96.92 | -3.08 | 20 | 15.0 | -5.60 | -0.64 | -18.82 | 300 |
| 44 | MACD cross · 1h | trend | 96.92 | -3.08 | 29 | 10.3 | -16.17 | -2.74 | -20.52 | 454 |
| 45 | Bollinger breakout · 1h | breakout | 96.84 | -3.16 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 46 | MACD zero-line · 1h | trend | 96.55 | -3.45 | 15 | 6.7 | -3.61 | -0.32 | -14.64 | 219 |
| 47 | RSI momentum · 1h | momentum | 96.44 | -3.56 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Triple EMA stack · 1h | trend | 95.97 | -4.03 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 49 | Ichimoku · 1h | trend | 95.92 | -4.08 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 50 | EMA 9/21 cross · 1h | trend | 95.92 | -4.08 | 33 | 12.1 | 2.78 | 0.58 | -16.92 | 312 |
| 51 | Three white soldiers | momentum | 95.87 | -4.13 | 34 | 11.8 | -51.81 | -28.38 | -51.81 | 620 |
| 52 | ADX DI cross · 1h | trend | 95.85 | -4.15 | 25 | 8.0 | -12.89 | -2.43 | -16.90 | 253 |
| 53 | Donchian 20/10 · 1h | breakout | 95.78 | -4.22 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 54 | Max aggression: 1-day momentum | meta | 95.54 | -4.46 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | OBV trend · 1h | momentum | 95.43 | -4.57 | 47 | 6.4 | -9.57 | -1.00 | -25.24 | 317 |
| 56 | MFI reversion · 1h | reversion | 95.32 | -4.67 | 38 | 13.2 | -10.09 | -1.87 | -17.20 | 126 |
| 57 | Volume breakout · 1h | breakout | 95.16 | -4.84 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 58 | Keltner breakout · 1h | breakout | 95.11 | -4.89 | 7 | 0.0 | -0.52 | 0.14 | -18.68 | 221 |
| 59 | VWAP momentum · 1h | momentum | 95.04 | -4.96 | 82 | 7.3 | -33.45 | -4.98 | -33.96 | 1250 |
| 60 | Heikin-Ashi · 1h | trend | 94.32 | -5.68 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 61 | Max aggression: 5-day momentum | meta | 94.18 | -5.82 | 1 | 0.0 | -2.30 | 0.16 | -29.56 | 29 |
| 62 | ROC + volume · 1h | momentum | 91.86 | -8.14 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.68 | -8.32 | 91 | 34.1 | -71.25 | -22.03 | -71.31 | 1478 |
| 64 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.73 | -18.56 | -59.89 | 1178 |
| 65 | ROC + volume | momentum | 89.31 | -10.69 | 115 | 16.5 | -71.92 | -17.85 | -72.35 | 1655 |
| 66 | AI bee: Bizzy | ai | 88.87 | -11.13 | 218 | 12.4 | — | — | — | — |
| 67 | Volume breakout | breakout | 88.63 | -11.37 | 76 | 9.2 | -62.56 | -20.50 | -62.56 | 908 |
| 68 | Donchian 55/20 | breakout | 88.55 | -11.45 | 77 | 11.7 | -68.88 | -15.95 | -68.88 | 1331 |
| 69 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.48 | -26.30 | -80.48 | 1755 |
| 71 | EMA 20/50 cross | trend | 87.61 | -12.39 | 95 | 13.7 | -78.98 | -17.85 | -79.11 | 1483 |
| 72 | Keltner breakout | breakout | 87.49 | -12.51 | 120 | 10.0 | -84.93 | -35.02 | -84.93 | 1928 |
| 73 | Z-score reversion | reversion | 85.29 | -14.71 | 146 | 28.8 | -84.80 | -28.74 | -84.80 | 2089 |
| 74 | VWAP reversion | reversion | 85.11 | -14.89 | 103 | 13.6 | -70.40 | -16.48 | -71.75 | 1406 |
| 75 | MACD zero-line | trend | 84.66 | -15.34 | 154 | 15.6 | -91.52 | -35.84 | -91.67 | 2363 |
| 76 | RSI momentum | momentum | 84.06 | -15.94 | 145 | 11.0 | -90.42 | -29.97 | -90.42 | 2398 |
| 77 | Bollinger breakout | breakout | 84.00 | -16.00 | 158 | 14.6 | -93.94 | -42.03 | -93.95 | 2874 |
| 78 | Supertrend | trend | 83.97 | -16.03 | 142 | 15.5 | -87.36 | -24.93 | -87.40 | 1961 |
| 79 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.53 | -33.79 | -90.53 | 2281 |
| 80 | Triple EMA stack | trend | 82.99 | -17.01 | 169 | 13.6 | -93.08 | -37.12 | -93.08 | 2628 |
| 81 | Donchian 20/10 | breakout | 82.73 | -17.27 | 159 | 15.1 | -90.94 | -30.26 | -90.95 | 2686 |
| 82 | ADX DI cross | trend | 82.08 | -17.92 | 160 | 6.9 | -89.42 | -48.15 | -89.42 | 2128 |
| 83 | MFI reversion | reversion | 82.05 | -17.95 | 152 | 16.4 | -87.82 | -35.04 | -87.92 | 2174 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.39 | -41.43 | -96.39 | 3650 |
| 85 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.88 | -31.05 | -94.88 | 2675 |
| 86 | Candlestick reversal | reversion | 79.04 | -20.96 | 193 | 14.0 | -99.36 | -52.96 | -99.36 | 5568 |
| 87 | EMA 9/21 cross | trend | 78.91 | -21.09 | 221 | 13.6 | -97.41 | -42.91 | -97.42 | 3548 |
| 88 | OBV trend | momentum | 78.46 | -21.54 | 220 | 12.7 | -95.86 | -50.79 | -95.86 | 3564 |
| 89 | Stochastic reversion | reversion | 78.40 | -21.60 | 255 | 23.5 | -95.95 | -49.12 | -95.95 | 4058 |
| 90 | Bollinger reversion | reversion | 77.28 | -22.72 | 242 | 12.8 | -95.81 | -46.83 | -95.81 | 3678 |
| 91 | Parabolic SAR | trend | 76.69 | -23.31 | 229 | 12.2 | -96.94 | -57.74 | -96.94 | 3651 |
| 92 | VWAP momentum | momentum | 76.58 | -23.42 | 288 | 9.4 | -98.46 | -36.83 | -98.46 | 5206 |
| 93 | CCI reversion | reversion | 75.63 | -24.37 | 164 | 5.5 | -98.47 | -53.22 | -98.47 | 4701 |
| 94 | MACD cross | trend | 74.84 | -25.16 | 185 | 8.1 | -99.70 | -68.36 | -99.70 | 6092 |
| 95 | Heikin-Ashi | trend | 74.79 | -25.21 | 194 | 3.1 | -99.89 | -86.37 | -99.89 | 8317 |
| 96 | Williams %R | reversion | 74.27 | -25.73 | 242 | 20.2 | -99.53 | -63.38 | -99.53 | 6093 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T02:40 | AI bee: Bizzy | sell | XRP-USD | 19.24 | -0.11 | Jev: sell (buy p=0.06) |
| 2026-09-29T02:40 | Williams %R | buy | SOL-USD | 18.55 | — | entry signal |
| 2026-09-29T02:40 | Williams %R | buy | ETH-USD | 18.61 | — | entry signal |
| 2026-09-29T02:40 | Williams %R | buy | DOGE-USD | 18.61 | — | entry signal |
| 2026-09-29T02:40 | Z-score reversion | buy | ETH-USD | 21.35 | — | entry signal |
| 2026-09-29T02:40 | Z-score reversion | buy | DOGE-USD | 21.35 | — | entry signal |
| 2026-09-29T02:40 | Candlestick reversal | buy | XRP-USD | 19.79 | — | entry signal |
| 2026-09-29T02:40 | Candlestick reversal | buy | ETH-USD | 19.79 | — | entry signal |
| 2026-09-29T02:40 | MACD cross | buy | XRP-USD | 18.74 | — | entry signal |
| 2026-09-29T02:40 | MACD cross | buy | SOL-USD | 18.74 | — | entry signal |
| 2026-09-29T02:38 | AI bee: Bizzy | buy | XRP-USD | 19.35 | — | Jev: buy (buy p=0.87) |
| 2026-09-29T02:35 | CCI reversion · 1h | sell | SOL-USD | 7.39 | -0.13 | stop-loss |
| 2026-09-29T02:35 | Williams %R · 1h | sell | SOL-USD | 9.59 | -0.35 | stop-loss |
| 2026-09-29T02:35 | MACD zero-line · 1h | sell | ETH-USD | 23.78 | -0.51 | stop-loss |
| 2026-09-29T02:35 | CCI reversion | buy | XRP-USD | 7.53 | — | rebalance up |
| 2026-09-29T02:35 | CCI reversion | buy | SOL-USD | 3.80 | — | rebalance up |
| 2026-09-29T02:35 | CCI reversion | sell | DOGE-USD | 14.98 | -0.22 | stop-loss |
| 2026-09-29T02:35 | Williams %R | sell | SOL-USD | 14.90 | -0.20 | stop-loss |
| 2026-09-29T02:35 | Williams %R | sell | DOGE-USD | 18.51 | -0.28 | stop-loss |
| 2026-09-29T02:35 | Stochastic reversion | sell | SOL-USD | 15.64 | -0.19 | stop-loss |
| 2026-09-29T02:35 | Z-score reversion | sell | SOL-USD | 17.09 | -0.23 | stop-loss |
| 2026-09-29T02:35 | Z-score reversion | sell | DOGE-USD | 21.26 | -0.30 | stop-loss |
| 2026-09-29T02:35 | Bollinger reversion | sell | SOL-USD | 15.46 | -0.19 | stop-loss |
| 2026-09-29T02:35 | Bollinger reversion | sell | DOGE-USD | 19.22 | -0.30 | stop-loss |
| 2026-09-29T02:35 | RSI(14) reversion | sell | SOL-USD | 18.33 | -0.22 | stop-loss |
| 2026-09-29T02:35 | RSI(14) reversion | sell | DOGE-USD | 22.82 | -0.33 | stop-loss |
| 2026-09-29T02:35 | Candlestick reversal | sell | ETH-USD | 19.69 | -0.15 | exit signal |
| 2026-09-29T02:35 | MACD cross | sell | XRP-USD | 18.65 | -0.26 | exit signal |
| 2026-09-29T02:35 | MACD cross | sell | SOL-USD | 18.69 | -0.22 | exit signal |
| 2026-09-29T02:33 | AI bee: Bizzy | sell | XRP-USD | 11.28 | -0.08 | Jev: sell (buy p=0.00) |
| 2026-09-29T02:32 | AI bee: Bizzy | buy | XRP-USD | 11.35 | — | Jev: buy (buy p=0.51) |
| 2026-09-29T02:30 | VWAP reversion | buy | ETH-USD | 21.29 | — | entry signal |
| 2026-09-29T02:30 | Candlestick reversal | buy | ETH-USD | 19.84 | — | entry signal |
| 2026-09-29T02:30 | Candlestick reversal | buy | BTC-USD | 19.84 | — | entry signal |
| 2026-09-29T02:25 | AI bee: Bizzy | sell | XRP-USD | 11.95 | -0.09 | Jev: sell (buy p=0.00) |
| 2026-09-29T02:25 | MFI reversion | sell | ETH-USD | 20.37 | -0.21 | stop-loss |
| 2026-09-29T02:25 | Williams %R | sell | ETH-USD | 14.92 | -0.15 | stop-loss |
| 2026-09-29T02:25 | Stochastic reversion | sell | ETH-USD | 15.74 | -0.16 | stop-loss |
| 2026-09-29T02:25 | Z-score reversion | buy | XRP-USD | 4.32 | — | rebalance up |
| 2026-09-29T02:25 | Z-score reversion | buy | DOGE-USD | 4.34 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
