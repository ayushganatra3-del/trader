# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T00:40:05.000139+00:00 · 5108 ticks

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

Today: 450 decisions in 90 calls, $0.0063 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T00:40 | 2 / 3 / 0 | XRP-USD 23%, DOGE-USD 21% |  |
| Breezy | 2026-09-29T00:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T00:40 | 3 / 2 / 0 | DOGE-USD 40%, XRP-USD 38% |  |

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
| 10 | RSI(14) reversion · 1h | reversion | 99.76 | -0.24 | 2 | 100.0 | 12.28 | 2.55 | -6.57 | 145 |
| 11 | Hold BTC | benchmark | 99.69 | -0.31 | 0 | — | 30.60 | 3.84 | -8.68 | 1 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.67 | -0.33 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.66 | -0.34 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.45 | -0.55 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.05 | -4.73 | 190 |
| 17 | Daily: Bullish score | daily | 99.17 | -0.83 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.77 | -5.16 | 28 |
| 19 | Connors RSI(2) · 1h | reversion | 99.05 | -0.95 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.01 | -0.99 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.00 | -1.00 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.91 | -1.09 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Z-score reversion · 1h | reversion | 98.87 | -1.13 | 4 | 25.0 | 3.63 | 0.91 | -8.60 | 155 |
| 24 | Stochastic reversion · 1h | reversion | 98.82 | -1.18 | 23 | 56.5 | -12.40 | -2.74 | -14.07 | 324 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | Williams %R · 1h | reversion | 98.67 | -1.33 | 29 | 51.7 | -18.40 | -3.39 | -20.37 | 488 |
| 27 | CCI reversion · 1h | reversion | 98.61 | -1.39 | 23 | 34.8 | 1.66 | 0.45 | -12.41 | 409 |
| 28 | Copy: Insider buying | copy | 98.51 | -1.49 | 2 | 100.0 | -12.69 | -2.44 | -17.74 | 73 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -8.05 | -2.83 | -11.75 | 232 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.01 | -1.99 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.01 | -1.99 | 7 | 14.3 | 16.09 | 2.83 | -6.26 | 94 |
| 34 | Candlestick reversal · 1h | reversion | 97.91 | -2.09 | 12 | 16.7 | -25.95 | -6.05 | -26.71 | 492 |
| 35 | EMA 20/50 cross · 1h | trend | 97.82 | -2.18 | 8 | 12.5 | 15.79 | 1.88 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.80 | -2.20 | 11 | 9.1 | 3.49 | 0.67 | -16.43 | 197 |
| 37 | MACD cross · 1h | trend | 97.73 | -2.27 | 27 | 11.1 | -15.36 | -2.58 | -20.52 | 454 |
| 38 | Bollinger reversion · 1h | reversion | 97.26 | -2.74 | 19 | 31.6 | -17.61 | -4.89 | -17.88 | 308 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.74 | -16.14 | 692 |
| 40 | Donchian 55/20 · 1h | breakout | 97.18 | -2.82 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.07 | -2.93 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 42 | Parabolic SAR · 1h | trend | 97.06 | -2.94 | 19 | 15.8 | -5.63 | -0.64 | -18.82 | 301 |
| 43 | Agent (ML meta-label) | meta | 97.01 | -2.99 | 79 | 10.1 | 1.91 | 0.49 | -12.82 | 403 |
| 44 | Trend pullback · 1h | trend | 97.00 | -3.00 | 22 | 13.6 | -26.02 | -6.92 | -26.61 | 149 |
| 45 | MACD zero-line · 1h | trend | 96.96 | -3.04 | 14 | 7.1 | -3.34 | -0.28 | -14.81 | 221 |
| 46 | Bollinger breakout · 1h | breakout | 96.81 | -3.19 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 47 | RSI momentum · 1h | momentum | 96.42 | -3.58 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | EMA 9/21 cross · 1h | trend | 96.12 | -3.88 | 33 | 12.1 | 3.32 | 0.65 | -16.92 | 311 |
| 49 | Triple EMA stack · 1h | trend | 95.94 | -4.06 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 50 | Ichimoku · 1h | trend | 95.90 | -4.09 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 51 | Three white soldiers | momentum | 95.87 | -4.13 | 34 | 11.8 | -51.81 | -28.38 | -51.81 | 620 |
| 52 | Max aggression: 5-day momentum | meta | 95.85 | -4.15 | 1 | 0.0 | -0.52 | 0.31 | -29.56 | 29 |
| 53 | ADX DI cross · 1h | trend | 95.83 | -4.17 | 25 | 8.0 | -12.37 | -2.34 | -16.00 | 251 |
| 54 | Donchian 20/10 · 1h | breakout | 95.76 | -4.24 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 55 | MFI reversion · 1h | reversion | 95.63 | -4.37 | 38 | 13.2 | -9.77 | -1.80 | -17.20 | 126 |
| 56 | Max aggression: 1-day momentum | meta | 95.50 | -4.50 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 57 | OBV trend · 1h | momentum | 95.41 | -4.59 | 47 | 6.4 | -9.57 | -1.00 | -25.24 | 317 |
| 58 | VWAP momentum · 1h | momentum | 95.24 | -4.76 | 80 | 6.2 | -33.29 | -4.95 | -33.83 | 1250 |
| 59 | Volume breakout · 1h | breakout | 95.15 | -4.85 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.10 | -4.90 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 94.31 | -5.69 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | RSI(14) reversion | reversion | 93.14 | -6.86 | 86 | 36.0 | -70.73 | -21.47 | -71.14 | 1469 |
| 63 | ROC + volume · 1h | momentum | 91.96 | -8.04 | 43 | 7.0 | -3.98 | -0.35 | -17.40 | 403 |
| 64 | AI bee: Bizzy | ai | 91.75 | -8.25 | 189 | 14.3 | — | — | — | — |
| 65 | AI bee: Boozy | ai | 90.61 | -9.39 | 50 | 2.0 | — | — | — | — |
| 66 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.94 | -18.68 | -59.94 | 1180 |
| 67 | ROC + volume | momentum | 89.50 | -10.50 | 114 | 16.7 | -71.93 | -17.82 | -72.35 | 1656 |
| 68 | Volume breakout | breakout | 88.82 | -11.18 | 75 | 9.3 | -62.48 | -20.41 | -62.49 | 908 |
| 69 | Donchian 55/20 | breakout | 88.78 | -11.22 | 76 | 11.8 | -68.77 | -15.89 | -68.78 | 1332 |
| 70 | EMA 20/50 cross | trend | 88.46 | -11.54 | 90 | 14.4 | -78.89 | -17.66 | -79.01 | 1488 |
| 71 | Ichimoku | trend | 87.86 | -12.14 | 84 | 8.3 | -80.45 | -26.16 | -80.56 | 1757 |
| 72 | Keltner breakout | breakout | 87.56 | -12.44 | 119 | 10.1 | -84.95 | -35.08 | -84.95 | 1929 |
| 73 | Z-score reversion | reversion | 86.66 | -13.34 | 142 | 29.6 | -84.55 | -28.08 | -84.67 | 2081 |
| 74 | VWAP reversion | reversion | 85.79 | -14.21 | 101 | 13.9 | -70.34 | -16.43 | -71.87 | 1402 |
| 75 | MACD zero-line | trend | 84.89 | -15.11 | 153 | 15.7 | -91.49 | -35.62 | -91.66 | 2365 |
| 76 | Supertrend | trend | 84.75 | -15.25 | 138 | 15.9 | -87.19 | -24.64 | -87.31 | 1963 |
| 77 | RSI momentum | momentum | 84.41 | -15.59 | 143 | 11.2 | -90.30 | -29.69 | -90.38 | 2398 |
| 78 | Bollinger breakout | breakout | 84.23 | -15.77 | 156 | 14.7 | -93.95 | -42.02 | -93.95 | 2876 |
| 79 | Triple EMA stack | trend | 83.71 | -16.29 | 164 | 14.0 | -92.99 | -36.52 | -93.03 | 2628 |
| 80 | Trend pullback | trend | 83.31 | -16.69 | 139 | 15.8 | -90.54 | -33.88 | -90.54 | 2282 |
| 81 | Donchian 20/10 | breakout | 83.16 | -16.84 | 157 | 15.3 | -90.91 | -30.07 | -90.94 | 2687 |
| 82 | ADX DI cross | trend | 82.58 | -17.42 | 157 | 7.0 | -89.33 | -47.20 | -89.35 | 2128 |
| 83 | MFI reversion | reversion | 82.34 | -17.66 | 151 | 16.6 | -87.83 | -35.18 | -87.91 | 2174 |
| 84 | Connors RSI(2) | reversion | 81.54 | -18.46 | 198 | 17.2 | -96.41 | -41.72 | -96.41 | 3651 |
| 85 | Candlestick reversal | reversion | 80.96 | -19.04 | 183 | 14.8 | -99.35 | -51.17 | -99.35 | 5560 |
| 86 | Stochastic reversion | reversion | 80.66 | -19.34 | 245 | 24.5 | -95.84 | -46.66 | -95.85 | 4053 |
| 87 | EMA 9/21 cross | trend | 79.71 | -20.30 | 216 | 13.9 | -97.41 | -42.35 | -97.41 | 3552 |
| 88 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.92 | -31.17 | -94.92 | 2679 |
| 89 | OBV trend | momentum | 79.14 | -20.86 | 215 | 13.0 | -95.82 | -49.84 | -95.82 | 3564 |
| 90 | Bollinger reversion | reversion | 78.88 | -21.12 | 235 | 13.2 | -95.73 | -45.13 | -95.73 | 3672 |
| 91 | VWAP momentum | momentum | 77.22 | -22.78 | 282 | 9.6 | -98.48 | -36.52 | -98.48 | 5214 |
| 92 | Parabolic SAR | trend | 77.19 | -22.81 | 224 | 12.5 | -96.94 | -56.95 | -96.94 | 3655 |
| 93 | CCI reversion | reversion | 76.56 | -23.44 | 160 | 5.6 | -98.46 | -52.08 | -98.46 | 4701 |
| 94 | MACD cross | trend | 76.18 | -23.82 | 179 | 8.4 | -99.70 | -65.48 | -99.70 | 6089 |
| 95 | Williams %R | reversion | 75.92 | -24.08 | 235 | 20.9 | -99.52 | -60.89 | -99.52 | 6089 |
| 96 | Heikin-Ashi | trend | 75.25 | -24.75 | 191 | 3.1 | -99.89 | -85.32 | -99.89 | 8321 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T00:40 | AI bee: Boozy | buy | XRP-USD | 34.51 | — | Jev: buy (buy p=0.76) |
| 2026-09-29T00:40 | AI bee: Boozy | buy | DOGE-USD | 35.87 | — | Jev: buy (buy p=0.79) |
| 2026-09-29T00:40 | AI bee: Bizzy | buy | XRP-USD | 21.13 | — | Jev: buy (buy p=0.92) |
| 2026-09-29T00:40 | AI bee: Bizzy | buy | DOGE-USD | 19.29 | — | Jev: buy (buy p=0.84) |
| 2026-09-29T00:40 | Williams %R | sell | XRP-USD | 18.98 | -0.08 | exit signal |
| 2026-09-29T00:40 | Candlestick reversal | sell | BTC-USD | 20.17 | -0.13 | exit signal |
| 2026-09-29T00:40 | Keltner breakout | buy | DOGE-USD | 21.91 | — | entry signal |
| 2026-09-29T00:40 | Bollinger breakout | buy | XRP-USD | 21.09 | — | entry signal |
| 2026-09-29T00:40 | Bollinger breakout | buy | DOGE-USD | 21.09 | — | entry signal |
| 2026-09-29T00:40 | Heikin-Ashi | buy | XRP-USD | 18.84 | — | entry signal |
| 2026-09-29T00:40 | Heikin-Ashi | buy | ETH-USD | 18.84 | — | entry signal |
| 2026-09-29T00:39 | AI bee: Boozy | sell | ETH-USD | 35.36 | -0.24 | Jev: sell (buy p=0.33) |
| 2026-09-29T00:39 | AI bee: Boozy | sell | DOGE-USD | 34.92 | -0.21 | Jev: sell (buy p=0.37) |
| 2026-09-29T00:38 | AI bee: Bizzy | sell | XRP-USD | 13.73 | -0.08 | Jev: sell (buy p=0.16) |
| 2026-09-29T00:38 | AI bee: Bizzy | sell | DOGE-USD | 16.70 | -0.11 | Jev: sell (buy p=0.17) |
| 2026-09-29T00:38 | VWAP momentum | sell | BTC-USD | 3.85 | -0.02 | rebalance down |
| 2026-09-29T00:38 | Parabolic SAR | sell | BTC-USD | 3.85 | -0.02 | rebalance down |
| 2026-09-29T00:37 | AI bee: Bizzy | buy | XRP-USD | 13.82 | — | Jev: buy (buy p=0.60) |
| 2026-09-29T00:37 | AI bee: Bizzy | buy | DOGE-USD | 16.81 | — | Jev: buy (buy p=0.73) |
| 2026-09-29T00:37 | AI bee: Bizzy | sell | ETH-USD | 16.78 | -0.09 | Jev: sell (buy p=0.09) |
| 2026-09-29T00:37 | VWAP momentum | buy | XRP-USD | 3.87 | — | rebalance up |
| 2026-09-29T00:37 | VWAP momentum | sell | DOGE-USD | 3.87 | -0.02 | rebalance down |
| 2026-09-29T00:37 | Parabolic SAR | buy | SOL-USD | 7.72 | — | rebalance up |
| 2026-09-29T00:37 | Parabolic SAR | sell | XRP-USD | 3.86 | -0.02 | rebalance down |
| 2026-09-29T00:37 | Parabolic SAR | sell | DOGE-USD | 3.86 | -0.02 | rebalance down |
| 2026-09-29T00:35 | AI bee: Bizzy | sell | XRP-USD | 13.32 | -0.09 | Jev: sell (buy p=0.13) |
| 2026-09-29T00:35 | AI bee: Bizzy | sell | DOGE-USD | 15.61 | -0.11 | Jev: sell (buy p=0.27) |
| 2026-09-29T00:35 | AI bee: Bizzy | sell | BTC-USD | 13.78 | -0.09 | Jev: sell (buy p=0.04) |
| 2026-09-29T00:35 | CCI reversion | sell | SOL-USD | 19.10 | -0.09 | exit signal |
| 2026-09-29T00:35 | Williams %R | sell | SOL-USD | 18.97 | -0.09 | exit signal |
| 2026-09-29T00:35 | Williams %R | sell | ETH-USD | 18.97 | -0.09 | exit signal |
| 2026-09-29T00:35 | Bollinger reversion | sell | ETH-USD | 19.68 | -0.09 | exit signal |
| 2026-09-29T00:35 | Bollinger reversion | sell | BTC-USD | 19.66 | -0.12 | exit signal |
| 2026-09-29T00:35 | Volume breakout | buy | DOGE-USD | 22.21 | — | entry signal |
| 2026-09-29T00:35 | Donchian 55/20 | buy | DOGE-USD | 22.21 | — | entry signal |
| 2026-09-29T00:35 | OBV trend | buy | XRP-USD | 11.85 | — | entry signal |
| 2026-09-29T00:35 | OBV trend | buy | SOL-USD | 15.85 | — | entry signal |
| 2026-09-29T00:35 | OBV trend | sell | DOGE-USD | 4.03 | -0.01 | rebalance down |
| 2026-09-29T00:35 | VWAP momentum | buy | XRP-USD | 7.78 | — | entry signal |
| 2026-09-29T00:35 | VWAP momentum | buy | SOL-USD | 15.47 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
