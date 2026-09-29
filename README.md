# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T02:10:05.000126+00:00 · 5190 ticks

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

Today: 1675 decisions in 335 calls, $0.0236 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T02:10 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-09-29T02:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T02:10 | 1 / 4 / 0 | ETH-USD 20% |  |

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
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 17 | RSI(14) reversion · 1h | reversion | 99.11 | -0.89 | 2 | 100.0 | 10.68 | 2.22 | -6.57 | 144 |
| 18 | Hold BTC | benchmark | 99.09 | -0.91 | 0 | — | 29.51 | 3.72 | -8.68 | 1 |
| 19 | Connors RSI(2) · 1h | reversion | 99.07 | -0.93 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.06 | -0.94 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.05 | -0.95 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.96 | -1.04 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 24 | Stochastic reversion · 1h | reversion | 98.67 | -1.33 | 23 | 56.5 | -12.72 | -2.82 | -13.84 | 323 |
| 25 | Copy: Insider buying | copy | 98.55 | -1.45 | 2 | 100.0 | -12.69 | -2.44 | -17.74 | 73 |
| 26 | Williams %R · 1h | reversion | 98.54 | -1.46 | 29 | 51.7 | -18.22 | -3.35 | -20.10 | 487 |
| 27 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -8.88 | -3.09 | -11.75 | 229 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.24 | -1.76 | 23 | 34.8 | 1.37 | 0.40 | -12.41 | 408 |
| 30 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 31 | Z-score reversion · 1h | reversion | 98.14 | -1.86 | 4 | 25.0 | 2.92 | 0.76 | -8.60 | 155 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.06 | -1.94 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.02 | -1.98 | 7 | 14.3 | 15.85 | 2.79 | -6.26 | 95 |
| 34 | Candlestick reversal · 1h | reversion | 97.91 | -2.09 | 12 | 16.7 | -26.30 | -6.16 | -26.60 | 490 |
| 35 | EMA 20/50 cross · 1h | trend | 97.87 | -2.13 | 8 | 12.5 | 15.79 | 1.88 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.66 | -2.34 | 11 | 9.1 | 5.24 | 0.90 | -16.43 | 194 |
| 37 | Bollinger reversion · 1h | reversion | 97.30 | -2.70 | 19 | 31.6 | -17.67 | -4.91 | -17.76 | 306 |
| 38 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.74 | -16.14 | 692 |
| 39 | Donchian 55/20 · 1h | breakout | 97.21 | -2.79 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.12 | -2.88 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.06 | -2.94 | 79 | 10.1 | 4.67 | 0.98 | -11.92 | 380 |
| 42 | Trend pullback · 1h | trend | 97.05 | -2.95 | 22 | 13.6 | -25.73 | -6.83 | -26.36 | 148 |
| 43 | MACD cross · 1h | trend | 96.95 | -3.05 | 29 | 10.3 | -16.15 | -2.73 | -20.52 | 454 |
| 44 | Parabolic SAR · 1h | trend | 96.93 | -3.07 | 20 | 15.0 | -5.60 | -0.64 | -18.82 | 300 |
| 45 | Bollinger breakout · 1h | breakout | 96.85 | -3.15 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 46 | MACD zero-line · 1h | trend | 96.69 | -3.31 | 14 | 7.1 | -3.47 | -0.30 | -14.64 | 219 |
| 47 | RSI momentum · 1h | momentum | 96.44 | -3.56 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Triple EMA stack · 1h | trend | 95.98 | -4.03 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 49 | EMA 9/21 cross · 1h | trend | 95.95 | -4.05 | 33 | 12.1 | 2.80 | 0.58 | -16.92 | 312 |
| 50 | Ichimoku · 1h | trend | 95.93 | -4.07 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 51 | Three white soldiers | momentum | 95.87 | -4.13 | 34 | 11.8 | -51.81 | -28.38 | -51.81 | 620 |
| 52 | ADX DI cross · 1h | trend | 95.85 | -4.15 | 25 | 8.0 | -12.34 | -2.33 | -16.25 | 252 |
| 53 | Donchian 20/10 · 1h | breakout | 95.79 | -4.21 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 54 | Max aggression: 1-day momentum | meta | 95.55 | -4.45 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | OBV trend · 1h | momentum | 95.43 | -4.57 | 47 | 6.4 | -9.57 | -1.00 | -25.24 | 317 |
| 56 | MFI reversion · 1h | reversion | 95.33 | -4.67 | 38 | 13.2 | -10.14 | -1.88 | -17.20 | 126 |
| 57 | Volume breakout · 1h | breakout | 95.16 | -4.84 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 58 | Keltner breakout · 1h | breakout | 95.11 | -4.89 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 59 | VWAP momentum · 1h | momentum | 95.05 | -4.95 | 82 | 7.3 | -33.47 | -4.98 | -33.96 | 1250 |
| 60 | Heikin-Ashi · 1h | trend | 94.32 | -5.68 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 61 | Max aggression: 5-day momentum | meta | 94.18 | -5.82 | 1 | 0.0 | -2.31 | 0.16 | -29.56 | 29 |
| 62 | RSI(14) reversion | reversion | 92.07 | -7.93 | 88 | 35.2 | -71.09 | -21.88 | -71.12 | 1473 |
| 63 | ROC + volume · 1h | momentum | 91.86 | -8.14 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 64 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.84 | -18.63 | -59.92 | 1179 |
| 65 | AI bee: Bizzy | ai | 89.73 | -10.27 | 209 | 12.9 | — | — | — | — |
| 66 | ROC + volume | momentum | 89.31 | -10.69 | 115 | 16.5 | -71.92 | -17.85 | -72.35 | 1655 |
| 67 | Volume breakout | breakout | 88.63 | -11.37 | 76 | 9.2 | -62.56 | -20.50 | -62.56 | 908 |
| 68 | Donchian 55/20 | breakout | 88.55 | -11.45 | 77 | 11.7 | -68.86 | -15.95 | -68.86 | 1331 |
| 69 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.50 | -26.27 | -80.50 | 1755 |
| 71 | EMA 20/50 cross | trend | 87.61 | -12.39 | 95 | 13.7 | -78.99 | -17.85 | -79.11 | 1483 |
| 72 | Keltner breakout | breakout | 87.49 | -12.51 | 120 | 10.0 | -84.93 | -35.02 | -84.94 | 1928 |
| 73 | Z-score reversion | reversion | 85.78 | -14.22 | 143 | 29.4 | -84.70 | -28.52 | -84.70 | 2087 |
| 74 | VWAP reversion | reversion | 85.17 | -14.83 | 103 | 13.6 | -70.50 | -16.49 | -71.87 | 1401 |
| 75 | MACD zero-line | trend | 84.66 | -15.34 | 154 | 15.6 | -91.51 | -35.76 | -91.68 | 2364 |
| 76 | RSI momentum | momentum | 84.06 | -15.94 | 145 | 11.0 | -90.38 | -29.93 | -90.41 | 2397 |
| 77 | Bollinger breakout | breakout | 84.00 | -16.00 | 158 | 14.6 | -93.94 | -42.03 | -93.95 | 2874 |
| 78 | Supertrend | trend | 83.97 | -16.03 | 142 | 15.5 | -87.31 | -24.94 | -87.39 | 1963 |
| 79 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.61 | -34.18 | -90.61 | 2285 |
| 80 | Triple EMA stack | trend | 82.99 | -17.01 | 169 | 13.6 | -93.08 | -37.12 | -93.08 | 2628 |
| 81 | Donchian 20/10 | breakout | 82.73 | -17.27 | 159 | 15.1 | -90.94 | -30.26 | -90.95 | 2686 |
| 82 | MFI reversion | reversion | 82.14 | -17.86 | 151 | 16.6 | -87.80 | -34.96 | -87.91 | 2174 |
| 83 | ADX DI cross | trend | 82.08 | -17.92 | 160 | 6.9 | -89.38 | -48.01 | -89.38 | 2127 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.43 | -42.09 | -96.43 | 3654 |
| 85 | Candlestick reversal | reversion | 79.64 | -20.36 | 188 | 14.4 | -99.36 | -52.43 | -99.36 | 5563 |
| 86 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.83 | -30.80 | -94.83 | 2671 |
| 87 | EMA 9/21 cross | trend | 78.91 | -21.09 | 221 | 13.6 | -97.41 | -42.88 | -97.42 | 3548 |
| 88 | Stochastic reversion | reversion | 78.71 | -21.29 | 252 | 23.8 | -95.95 | -48.93 | -95.95 | 4060 |
| 89 | OBV trend | momentum | 78.46 | -21.54 | 220 | 12.7 | -95.85 | -50.81 | -95.85 | 3563 |
| 90 | Bollinger reversion | reversion | 77.67 | -22.33 | 238 | 13.0 | -95.79 | -46.45 | -95.79 | 3680 |
| 91 | VWAP momentum | momentum | 76.72 | -23.28 | 287 | 9.4 | -98.45 | -36.77 | -98.46 | 5202 |
| 92 | Parabolic SAR | trend | 76.69 | -23.31 | 229 | 12.2 | -96.96 | -58.00 | -96.96 | 3655 |
| 93 | CCI reversion | reversion | 75.75 | -24.25 | 163 | 5.5 | -98.47 | -53.11 | -98.47 | 4703 |
| 94 | MACD cross | trend | 75.60 | -24.40 | 182 | 8.2 | -99.70 | -66.87 | -99.70 | 6086 |
| 95 | Williams %R | reversion | 74.81 | -25.19 | 238 | 20.6 | -99.53 | -62.67 | -99.53 | 6091 |
| 96 | Heikin-Ashi | trend | 74.79 | -25.21 | 194 | 3.1 | -99.89 | -86.40 | -99.89 | 8317 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T02:08 | AI bee: Bizzy | sell | XRP-USD | 11.82 | -0.08 | Jev: sell (buy p=0.01) |
| 2026-09-29T02:07 | AI bee: Bizzy | buy | XRP-USD | 11.90 | — | Jev: buy (buy p=0.53) |
| 2026-09-29T02:06 | AI bee: Bizzy | sell | XRP-USD | 19.42 | -0.14 | Jev: sell (buy p=0.03) |
| 2026-09-29T02:05 | AI bee: Bizzy | buy | XRP-USD | 19.56 | — | Jev: buy (buy p=0.87) |
| 2026-09-29T02:04 | AI bee: Bizzy | sell | XRP-USD | 16.10 | -0.11 | Jev: sell (buy p=0.01) |
| 2026-09-29T02:03 | AI bee: Bizzy | buy | XRP-USD | 16.21 | — | Jev: buy (buy p=0.72) |
| 2026-09-29T02:02 | AI bee: Bizzy | sell | XRP-USD | 15.67 | -0.11 | Jev: sell (buy p=0.00) |
| 2026-09-29T02:00 | AI bee: Bizzy | buy | XRP-USD | 15.78 | — | Jev: buy (buy p=0.70) |
| 2026-09-29T02:00 | Candlestick reversal · 1h | buy | BTC-USD | 8.90 | — | entry signal |
| 2026-09-29T02:00 | Parabolic SAR · 1h | sell | ETH-USD | 13.80 | -0.12 | exit signal |
| 2026-09-29T02:00 | MACD cross | buy | BTC-USD | 18.92 | — | entry signal |
| 2026-09-29T01:58 | AI bee: Bizzy | sell | SOL-USD | 11.65 | -0.09 | Jev: sell (buy p=0.00) |
| 2026-09-29T01:57 | AI bee: Bizzy | buy | SOL-USD | 11.73 | — | Jev: buy (buy p=0.52) |
| 2026-09-29T01:55 | AI bee: Bizzy | sell | DOGE-USD | 12.33 | -0.09 | Jev: sell (buy p=0.05) |
| 2026-09-29T01:54 | AI bee: Bizzy | buy | DOGE-USD | 12.42 | — | Jev: buy (buy p=0.55) |
| 2026-09-29T01:52 | CCI reversion | sell | ETH-USD | 3.79 | -0.02 | rebalance down |
| 2026-09-29T01:51 | CCI reversion | buy | XRP-USD | 3.79 | — | rebalance up |
| 2026-09-29T01:51 | CCI reversion | sell | BTC-USD | 3.79 | -0.02 | rebalance down |
| 2026-09-29T01:50 | CCI reversion | buy | XRP-USD | 7.66 | — | entry signal |
| 2026-09-29T01:50 | CCI reversion | buy | SOL-USD | 15.20 | — | entry signal |
| 2026-09-29T01:50 | CCI reversion | buy | DOGE-USD | 15.20 | — | entry signal |
| 2026-09-29T01:47 | AI bee: Bizzy | sell | DOGE-USD | 17.80 | -0.07 | Jev: sell (buy p=0.09) |
| 2026-09-29T01:46 | AI bee: Bizzy | sell | XRP-USD | 12.62 | -0.04 | Jev: sell (buy p=0.31) |
| 2026-09-29T01:45 | AI bee: Bizzy | buy | XRP-USD | 12.67 | — | Jev: buy (buy p=0.56) |
| 2026-09-29T01:45 | AI bee: Bizzy | buy | DOGE-USD | 17.87 | — | Jev: buy (buy p=0.79) |
| 2026-09-29T01:45 | CCI reversion | buy | ETH-USD | 19.03 | — | entry signal |
| 2026-09-29T01:45 | CCI reversion | buy | BTC-USD | 19.03 | — | entry signal |
| 2026-09-29T01:45 | Williams %R | buy | XRP-USD | 14.98 | — | entry signal |
| 2026-09-29T01:45 | Williams %R | buy | DOGE-USD | 15.01 | — | entry signal |
| 2026-09-29T01:45 | Williams %R | sell | SOL-USD | 3.77 | -0.03 | rebalance down |
| 2026-09-29T01:45 | Williams %R | sell | ETH-USD | 3.80 | -0.03 | rebalance down |
| 2026-09-29T01:45 | Williams %R | sell | BTC-USD | 3.81 | -0.03 | rebalance down |
| 2026-09-29T01:45 | Stochastic reversion | buy | XRP-USD | 19.71 | — | entry signal |
| 2026-09-29T01:45 | Z-score reversion | buy | XRP-USD | 17.19 | — | entry signal |
| 2026-09-29T01:45 | Z-score reversion | buy | DOGE-USD | 17.22 | — | entry signal |
| 2026-09-29T01:45 | Z-score reversion | buy | BTC-USD | 17.22 | — | entry signal |
| 2026-09-29T01:45 | Z-score reversion | sell | SOL-USD | 4.30 | -0.04 | rebalance down |
| 2026-09-29T01:45 | Z-score reversion | sell | ETH-USD | 4.34 | -0.03 | rebalance down |
| 2026-09-29T01:45 | Bollinger reversion | buy | XRP-USD | 15.42 | — | entry signal |
| 2026-09-29T01:45 | Bollinger reversion | buy | DOGE-USD | 15.58 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
