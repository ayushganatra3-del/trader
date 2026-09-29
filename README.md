# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T01:10:05.000161+00:00 · 5137 ticks

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

Today: 885 decisions in 177 calls, $0.0125 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T01:10 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-09-29T01:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T01:10 | 3 / 2 / 0 | ETH-USD 22%, BTC-USD 20% |  |

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
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.41 | 1.25 | -2.47 | 92 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.67 | -0.33 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.66 | -0.34 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 12 | Hold SPY | benchmark | 99.45 | -0.55 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.40 | -0.60 | 2 | 100.0 | 14.65 | 3.08 | -6.57 | 136 |
| 14 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 15 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 16 | Daily: Bullish score | daily | 99.17 | -0.83 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 17 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 18 | Hold BTC | benchmark | 99.11 | -0.89 | 0 | — | 29.80 | 3.75 | -8.68 | 1 |
| 19 | Connors RSI(2) · 1h | reversion | 99.05 | -0.95 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.01 | -0.99 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.00 | -1.00 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.91 | -1.09 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 24 | Stochastic reversion · 1h | reversion | 98.71 | -1.29 | 23 | 56.5 | -12.62 | -2.80 | -13.85 | 323 |
| 25 | Williams %R · 1h | reversion | 98.57 | -1.43 | 29 | 51.7 | -18.46 | -3.40 | -20.37 | 488 |
| 26 | Copy: Insider buying | copy | 98.51 | -1.49 | 2 | 100.0 | -12.69 | -2.44 | -17.74 | 73 |
| 27 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.88 | -2.76 | -11.75 | 233 |
| 28 | Z-score reversion · 1h | reversion | 98.42 | -1.58 | 4 | 25.0 | 3.22 | 0.82 | -8.60 | 155 |
| 29 | CCI reversion · 1h | reversion | 98.37 | -1.62 | 23 | 34.8 | 1.45 | 0.41 | -12.41 | 409 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.01 | -1.99 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.01 | -1.99 | 7 | 14.3 | 16.09 | 2.83 | -6.26 | 94 |
| 34 | Candlestick reversal · 1h | reversion | 97.91 | -2.09 | 12 | 16.7 | -25.38 | -6.00 | -25.98 | 483 |
| 35 | EMA 20/50 cross · 1h | trend | 97.82 | -2.18 | 8 | 12.5 | 15.66 | 1.87 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.67 | -2.33 | 11 | 9.1 | 4.70 | 0.83 | -16.43 | 195 |
| 37 | MACD cross · 1h | trend | 97.33 | -2.67 | 27 | 11.1 | -15.85 | -2.68 | -20.81 | 455 |
| 38 | Bollinger reversion · 1h | reversion | 97.26 | -2.74 | 19 | 31.6 | -17.61 | -4.89 | -17.88 | 308 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 40 | Donchian 55/20 · 1h | breakout | 97.18 | -2.82 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.07 | -2.93 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 42 | Agent (ML meta-label) | meta | 97.01 | -2.99 | 79 | 10.1 | 3.79 | 0.82 | -10.45 | 389 |
| 43 | Trend pullback · 1h | trend | 97.00 | -3.00 | 22 | 13.6 | -26.02 | -6.92 | -26.61 | 149 |
| 44 | Parabolic SAR · 1h | trend | 96.96 | -3.04 | 19 | 15.8 | -5.51 | -0.62 | -18.82 | 300 |
| 45 | Bollinger breakout · 1h | breakout | 96.81 | -3.19 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 46 | MACD zero-line · 1h | trend | 96.79 | -3.21 | 14 | 7.1 | -3.24 | -0.27 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.42 | -3.58 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | EMA 9/21 cross · 1h | trend | 95.99 | -4.01 | 33 | 12.1 | 2.95 | 0.60 | -16.92 | 312 |
| 49 | Triple EMA stack · 1h | trend | 95.94 | -4.06 | 24 | 8.3 | -2.85 | -0.13 | -22.95 | 223 |
| 50 | Ichimoku · 1h | trend | 95.90 | -4.09 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 51 | Three white soldiers | momentum | 95.87 | -4.13 | 34 | 11.8 | -51.81 | -28.38 | -51.81 | 620 |
| 52 | ADX DI cross · 1h | trend | 95.83 | -4.17 | 25 | 8.0 | -12.14 | -2.29 | -16.04 | 250 |
| 53 | Donchian 20/10 · 1h | breakout | 95.76 | -4.24 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 54 | Max aggression: 1-day momentum | meta | 95.50 | -4.50 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | MFI reversion · 1h | reversion | 95.43 | -4.57 | 38 | 13.2 | -9.95 | -1.84 | -17.20 | 126 |
| 56 | OBV trend · 1h | momentum | 95.41 | -4.59 | 47 | 6.4 | -9.43 | -0.98 | -25.24 | 317 |
| 57 | Volume breakout · 1h | breakout | 95.15 | -4.85 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 58 | Keltner breakout · 1h | breakout | 95.10 | -4.90 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 59 | VWAP momentum · 1h | momentum | 95.01 | -4.99 | 82 | 7.3 | -33.44 | -4.98 | -33.96 | 1250 |
| 60 | Max aggression: 5-day momentum | meta | 94.87 | -5.13 | 1 | 0.0 | -1.54 | 0.22 | -29.56 | 29 |
| 61 | Heikin-Ashi · 1h | trend | 94.31 | -5.69 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | RSI(14) reversion | reversion | 93.14 | -6.86 | 86 | 36.0 | -71.13 | -21.77 | -71.51 | 1473 |
| 63 | ROC + volume · 1h | momentum | 91.83 | -8.17 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 64 | AI bee: Bizzy | ai | 91.16 | -8.84 | 195 | 13.8 | — | — | — | — |
| 65 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.83 | -18.62 | -59.90 | 1179 |
| 66 | ROC + volume | momentum | 89.31 | -10.69 | 115 | 16.5 | -71.99 | -17.88 | -72.35 | 1656 |
| 67 | Volume breakout | breakout | 88.63 | -11.37 | 76 | 9.2 | -62.48 | -20.54 | -62.48 | 907 |
| 68 | Donchian 55/20 | breakout | 88.55 | -11.45 | 77 | 11.7 | -68.83 | -15.95 | -68.84 | 1331 |
| 69 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.48 | -26.30 | -80.48 | 1755 |
| 71 | EMA 20/50 cross | trend | 87.61 | -12.39 | 95 | 13.7 | -79.08 | -17.87 | -79.12 | 1486 |
| 72 | Keltner breakout | breakout | 87.49 | -12.51 | 120 | 10.0 | -84.93 | -35.02 | -84.93 | 1928 |
| 73 | Z-score reversion | reversion | 86.66 | -13.34 | 142 | 29.6 | -84.55 | -28.08 | -84.67 | 2081 |
| 74 | VWAP reversion | reversion | 85.68 | -14.32 | 101 | 13.9 | -70.19 | -16.32 | -71.75 | 1402 |
| 75 | MACD zero-line | trend | 84.66 | -15.34 | 154 | 15.6 | -91.51 | -35.76 | -91.67 | 2365 |
| 76 | RSI momentum | momentum | 84.06 | -15.94 | 145 | 11.0 | -90.37 | -29.93 | -90.40 | 2398 |
| 77 | Bollinger breakout | breakout | 84.00 | -16.00 | 158 | 14.6 | -93.94 | -42.03 | -93.95 | 2874 |
| 78 | Supertrend | trend | 83.97 | -16.03 | 142 | 15.5 | -87.37 | -24.95 | -87.44 | 1964 |
| 79 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.53 | -33.79 | -90.53 | 2281 |
| 80 | Triple EMA stack | trend | 82.99 | -17.01 | 169 | 13.6 | -93.06 | -37.12 | -93.08 | 2628 |
| 81 | Donchian 20/10 | breakout | 82.73 | -17.27 | 159 | 15.1 | -90.94 | -30.26 | -90.95 | 2686 |
| 82 | MFI reversion | reversion | 82.34 | -17.66 | 151 | 16.6 | -87.83 | -35.13 | -87.91 | 2174 |
| 83 | ADX DI cross | trend | 82.08 | -17.92 | 160 | 6.9 | -89.39 | -48.00 | -89.39 | 2128 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.42 | -42.11 | -96.42 | 3653 |
| 85 | Candlestick reversal | reversion | 80.32 | -19.68 | 186 | 14.5 | -99.36 | -51.80 | -99.36 | 5565 |
| 86 | Stochastic reversion | reversion | 80.17 | -19.83 | 245 | 24.5 | -95.87 | -47.29 | -95.87 | 4054 |
| 87 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.76 | -30.49 | -94.76 | 2663 |
| 88 | EMA 9/21 cross | trend | 78.91 | -21.09 | 221 | 13.6 | -97.41 | -42.89 | -97.42 | 3548 |
| 89 | Bollinger reversion | reversion | 78.76 | -21.25 | 235 | 13.2 | -95.74 | -45.28 | -95.74 | 3673 |
| 90 | OBV trend | momentum | 78.46 | -21.54 | 220 | 12.7 | -95.86 | -50.78 | -95.86 | 3565 |
| 91 | VWAP momentum | momentum | 76.72 | -23.28 | 287 | 9.4 | -98.49 | -36.78 | -98.49 | 5216 |
| 92 | Parabolic SAR | trend | 76.69 | -23.31 | 229 | 12.2 | -96.96 | -58.00 | -96.96 | 3655 |
| 93 | CCI reversion | reversion | 76.21 | -23.79 | 162 | 5.6 | -98.47 | -52.57 | -98.47 | 4699 |
| 94 | Williams %R | reversion | 75.69 | -24.31 | 236 | 20.8 | -99.52 | -61.27 | -99.52 | 6088 |
| 95 | MACD cross | trend | 75.67 | -24.33 | 182 | 8.2 | -99.70 | -66.51 | -99.70 | 6090 |
| 96 | Heikin-Ashi | trend | 74.79 | -25.21 | 194 | 3.1 | -99.89 | -86.97 | -99.89 | 8322 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T01:10 | Connors RSI(2) | sell | ETH-USD | 20.16 | -0.19 | stop-loss |
| 2026-09-29T01:10 | Connors RSI(2) | sell | DOGE-USD | 20.14 | -0.24 | stop-loss |
| 2026-09-29T01:10 | Candlestick reversal | sell | SOL-USD | 19.94 | -0.23 | stop-loss |
| 2026-09-29T01:10 | EMA 20/50 cross | sell | DOGE-USD | 21.83 | -0.26 | stop-loss |
| 2026-09-29T01:10 | EMA 9/21 cross | sell | DOGE-USD | 15.75 | -0.18 | exit signal |
| 2026-09-29T01:05 | CCI reversion | buy | DOGE-USD | 19.09 | — | entry signal |
| 2026-09-29T01:05 | Williams %R | buy | DOGE-USD | 18.96 | — | entry signal |
| 2026-09-29T01:05 | Stochastic reversion | buy | XRP-USD | 16.13 | — | entry signal |
| 2026-09-29T01:05 | Stochastic reversion | buy | SOL-USD | 16.13 | — | entry signal |
| 2026-09-29T01:05 | Stochastic reversion | buy | ETH-USD | 16.13 | — | entry signal |
| 2026-09-29T01:05 | Stochastic reversion | buy | DOGE-USD | 16.13 | — | entry signal |
| 2026-09-29T01:05 | Stochastic reversion | buy | BTC-USD | 16.13 | — | entry signal |
| 2026-09-29T01:05 | VWAP reversion | buy | ETH-USD | 21.45 | — | entry signal |
| 2026-09-29T01:05 | Bollinger reversion | buy | XRP-USD | 19.72 | — | entry signal |
| 2026-09-29T01:05 | Candlestick reversal | buy | DOGE-USD | 20.15 | — | entry signal |
| 2026-09-29T01:04 | AI bee: Boozy | sell | XRP-USD | 30.41 | -0.21 | Jev: sell (buy p=0.24) |
| 2026-09-29T01:04 | AI bee: Boozy | sell | DOGE-USD | 33.93 | -0.23 | Jev: sell (buy p=0.35) |
| 2026-09-29T01:04 | AI bee: Bizzy | sell | XRP-USD | 12.25 | -0.08 | Jev: sell (buy p=0.04) |
| 2026-09-29T01:04 | AI bee: Bizzy | sell | DOGE-USD | 20.88 | -0.14 | Jev: sell (buy p=0.15) |
| 2026-09-29T01:03 | AI bee: Boozy | buy | XRP-USD | 30.61 | — | Jev: buy (buy p=0.69) |
| 2026-09-29T01:03 | AI bee: Boozy | buy | DOGE-USD | 34.16 | — | Jev: buy (buy p=0.77) |
| 2026-09-29T01:03 | AI bee: Bizzy | buy | XRP-USD | 12.34 | — | Jev: buy (buy p=0.54) |
| 2026-09-29T01:03 | AI bee: Bizzy | buy | DOGE-USD | 21.02 | — | Jev: buy (buy p=0.92) |
| 2026-09-29T01:02 | AI bee: Boozy | sell | ETH-USD | 17.66 | -0.10 | Jev: sell (buy p=0.30) |
| 2026-09-29T01:01 | AI bee: Boozy | buy | ETH-USD | 17.77 | — | Jev: buy (buy p=0.40) |
| 2026-09-29T01:00 | AI bee: Boozy | sell | SOL-USD | 17.69 | -0.13 | Jev: sell (buy p=0.28) |
| 2026-09-29T01:00 | AI bee: Boozy | sell | ETH-USD | 19.91 | -0.14 | Jev: sell (buy p=0.26) |
| 2026-09-29T01:00 | ROC + volume · 1h | sell | BTC-USD | 18.34 | -0.21 | exit signal |
| 2026-09-29T01:00 | VWAP momentum · 1h | sell | ETH-USD | 18.99 | -0.06 | exit signal |
| 2026-09-29T01:00 | VWAP momentum · 1h | sell | BTC-USD | 11.20 | -0.11 | exit signal |
| 2026-09-29T01:00 | OBV trend | sell | DOGE-USD | 15.68 | -0.16 | exit signal |
| 2026-09-29T01:00 | Supertrend | sell | XRP-USD | 20.96 | -0.20 | exit signal |
| 2026-09-29T01:00 | Supertrend | sell | SOL-USD | 20.99 | -0.18 | exit signal |
| 2026-09-29T01:00 | Triple EMA stack | sell | XRP-USD | 16.57 | -0.19 | stop-loss |
| 2026-09-29T01:00 | Triple EMA stack | sell | DOGE-USD | 16.58 | -0.17 | stop-loss |
| 2026-09-29T01:00 | EMA 20/50 cross | sell | XRP-USD | 17.54 | -0.21 | stop-loss |
| 2026-09-29T01:00 | EMA 9/21 cross | sell | XRP-USD | 15.78 | -0.15 | exit signal |
| 2026-09-29T01:00 | EMA 9/21 cross | sell | SOL-USD | 19.72 | -0.19 | exit signal |
| 2026-09-29T00:59 | AI bee: Boozy | buy | SOL-USD | 17.82 | — | Jev: buy (buy p=0.40) |
| 2026-09-29T00:59 | AI bee: Boozy | buy | ETH-USD | 20.05 | — | Jev: buy (buy p=0.45) |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
