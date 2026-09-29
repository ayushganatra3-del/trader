# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T04:10:05.000159+00:00 · 5288 ticks

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

Today: 3145 decisions in 629 calls, $0.0442 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T04:10 | 2 / 3 / 0 | XRP-USD 17%, SOL-USD 15% |  |
| Breezy | 2026-09-29T04:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T04:10 | 5 / 0 / 0 | SOL-USD 34%, ETH-USD 30% |  |

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
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.70 | -0.30 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.69 | -0.31 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 12 | Hold SPY | benchmark | 99.48 | -0.52 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 13 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 14 | RSI(14) reversion · 1h | reversion | 99.32 | -0.68 | 2 | 100.0 | 14.48 | 3.04 | -6.57 | 137 |
| 15 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.05 | -4.73 | 190 |
| 16 | Daily: Bullish score | daily | 99.19 | -0.81 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 17 | Hold BTC | benchmark | 99.19 | -0.81 | 0 | — | 29.54 | 3.72 | -8.68 | 1 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | Connors RSI(2) · 1h | reversion | 99.06 | -0.94 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.04 | -0.96 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.03 | -0.97 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.93 | -1.07 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 24 | Stochastic reversion · 1h | reversion | 98.68 | -1.32 | 23 | 56.5 | -12.68 | -2.82 | -13.85 | 324 |
| 25 | Copy: Insider buying | copy | 98.53 | -1.47 | 2 | 100.0 | -12.69 | -2.44 | -17.74 | 73 |
| 26 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -8.05 | -2.83 | -11.75 | 232 |
| 27 | Williams %R · 1h | reversion | 98.42 | -1.58 | 30 | 50.0 | -17.85 | -3.27 | -19.83 | 490 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 29 | Z-score reversion · 1h | reversion | 98.35 | -1.65 | 4 | 25.0 | 3.14 | 0.80 | -8.60 | 155 |
| 30 | CCI reversion · 1h | reversion | 98.26 | -1.74 | 24 | 33.3 | 1.33 | 0.39 | -12.41 | 404 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.03 | -1.97 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.01 | -1.99 | 7 | 14.3 | 15.85 | 2.79 | -6.26 | 95 |
| 34 | Candlestick reversal · 1h | reversion | 97.91 | -2.09 | 12 | 16.7 | -26.22 | -6.15 | -26.40 | 491 |
| 35 | EMA 20/50 cross · 1h | trend | 97.85 | -2.15 | 8 | 12.5 | 15.73 | 1.88 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.67 | -2.33 | 11 | 9.1 | 5.27 | 0.90 | -16.43 | 194 |
| 37 | Bollinger reversion · 1h | reversion | 97.28 | -2.72 | 19 | 31.6 | -17.67 | -4.91 | -17.76 | 306 |
| 38 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.74 | -16.14 | 692 |
| 39 | Donchian 55/20 · 1h | breakout | 97.20 | -2.81 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.10 | -2.90 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.03 | -2.97 | 79 | 10.1 | 4.47 | 0.93 | -11.10 | 390 |
| 42 | Trend pullback · 1h | trend | 97.03 | -2.97 | 22 | 13.6 | -25.73 | -6.83 | -26.36 | 148 |
| 43 | Parabolic SAR · 1h | trend | 96.91 | -3.09 | 20 | 15.0 | -5.60 | -0.64 | -18.82 | 300 |
| 44 | Bollinger breakout · 1h | breakout | 96.83 | -3.17 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 45 | MACD cross · 1h | trend | 96.74 | -3.26 | 31 | 9.7 | -16.38 | -2.78 | -20.54 | 455 |
| 46 | MACD zero-line · 1h | trend | 96.55 | -3.45 | 15 | 6.7 | -3.46 | -0.30 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.43 | -3.57 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Triple EMA stack · 1h | trend | 95.96 | -4.04 | 24 | 8.3 | -2.81 | -0.12 | -22.95 | 223 |
| 49 | Ichimoku · 1h | trend | 95.92 | -4.08 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 50 | EMA 9/21 cross · 1h | trend | 95.86 | -4.14 | 34 | 11.8 | 2.67 | 0.56 | -16.92 | 312 |
| 51 | ADX DI cross · 1h | trend | 95.84 | -4.16 | 25 | 8.0 | -11.67 | -2.19 | -15.39 | 249 |
| 52 | Donchian 20/10 · 1h | breakout | 95.78 | -4.22 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 53 | Three white soldiers | momentum | 95.69 | -4.31 | 35 | 11.4 | -51.90 | -28.55 | -51.90 | 621 |
| 54 | Max aggression: 1-day momentum | meta | 95.52 | -4.48 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | MFI reversion · 1h | reversion | 95.44 | -4.56 | 38 | 13.2 | -9.48 | -1.74 | -17.20 | 125 |
| 56 | OBV trend · 1h | momentum | 95.42 | -4.58 | 47 | 6.4 | -9.59 | -1.00 | -25.24 | 317 |
| 57 | Volume breakout · 1h | breakout | 95.16 | -4.84 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 58 | Keltner breakout · 1h | breakout | 95.11 | -4.89 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 59 | VWAP momentum · 1h | momentum | 95.03 | -4.97 | 82 | 7.3 | -33.49 | -4.99 | -33.96 | 1250 |
| 60 | Max aggression: 5-day momentum | meta | 94.79 | -5.21 | 1 | 0.0 | -1.65 | 0.21 | -29.56 | 29 |
| 61 | Heikin-Ashi · 1h | trend | 94.31 | -5.69 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | ROC + volume · 1h | momentum | 91.85 | -8.15 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.16 | -21.95 | -71.27 | 1474 |
| 64 | Squeeze breakout | breakout | 90.08 | -9.92 | 66 | 6.1 | -60.05 | -18.81 | -60.08 | 1183 |
| 65 | ROC + volume | momentum | 89.31 | -10.69 | 115 | 16.5 | -71.83 | -17.81 | -72.35 | 1653 |
| 66 | Volume breakout | breakout | 88.63 | -11.37 | 76 | 9.2 | -62.56 | -20.50 | -62.56 | 908 |
| 67 | Donchian 55/20 | breakout | 88.55 | -11.45 | 77 | 11.7 | -68.57 | -15.92 | -68.57 | 1327 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.50 | -26.27 | -80.50 | 1755 |
| 71 | EMA 20/50 cross | trend | 87.61 | -12.39 | 95 | 13.7 | -78.99 | -17.85 | -79.11 | 1483 |
| 72 | Keltner breakout | breakout | 87.49 | -12.51 | 120 | 10.0 | -84.84 | -34.86 | -84.93 | 1924 |
| 73 | Z-score reversion | reversion | 85.69 | -14.30 | 149 | 29.5 | -84.73 | -28.58 | -84.80 | 2089 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -70.51 | -16.55 | -71.87 | 1402 |
| 75 | MACD zero-line | trend | 84.16 | -15.84 | 154 | 15.6 | -91.56 | -36.08 | -91.73 | 2365 |
| 76 | Supertrend | trend | 83.83 | -16.17 | 142 | 15.5 | -87.30 | -24.92 | -87.37 | 1959 |
| 77 | RSI momentum | momentum | 83.66 | -16.34 | 145 | 11.0 | -90.35 | -30.01 | -90.45 | 2396 |
| 78 | Bollinger breakout | breakout | 83.63 | -16.37 | 158 | 14.6 | -93.97 | -42.38 | -93.97 | 2877 |
| 79 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.52 | -33.58 | -90.52 | 2282 |
| 80 | Triple EMA stack | trend | 82.99 | -17.01 | 169 | 13.6 | -93.01 | -37.09 | -93.01 | 2623 |
| 81 | Donchian 20/10 | breakout | 82.29 | -17.71 | 159 | 15.1 | -91.02 | -30.50 | -91.02 | 2690 |
| 82 | MFI reversion | reversion | 82.07 | -17.93 | 152 | 16.4 | -87.81 | -34.97 | -87.92 | 2169 |
| 83 | ADX DI cross | trend | 81.77 | -18.23 | 162 | 6.8 | -89.41 | -48.47 | -89.42 | 2130 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.36 | -40.95 | -96.36 | 3649 |
| 85 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.74 | -30.39 | -94.74 | 2661 |
| 86 | Candlestick reversal | reversion | 78.95 | -21.05 | 198 | 14.1 | -99.36 | -53.02 | -99.36 | 5568 |
| 87 | OBV trend | momentum | 78.46 | -21.54 | 220 | 12.7 | -95.82 | -50.71 | -95.82 | 3558 |
| 88 | Stochastic reversion | reversion | 78.43 | -21.57 | 258 | 23.3 | -95.94 | -49.07 | -95.95 | 4057 |
| 89 | EMA 9/21 cross | trend | 78.39 | -21.61 | 221 | 13.6 | -97.41 | -43.15 | -97.42 | 3548 |
| 90 | Bollinger reversion | reversion | 77.28 | -22.72 | 243 | 12.8 | -95.81 | -46.83 | -95.81 | 3678 |
| 91 | Parabolic SAR | trend | 76.62 | -23.38 | 229 | 12.2 | -96.93 | -57.62 | -96.93 | 3650 |
| 92 | VWAP momentum | momentum | 76.14 | -23.86 | 291 | 9.3 | -98.45 | -36.97 | -98.45 | 5200 |
| 93 | CCI reversion | reversion | 75.62 | -24.38 | 169 | 5.9 | -98.47 | -53.22 | -98.47 | 4699 |
| 94 | MACD cross | trend | 75.04 | -24.96 | 185 | 8.1 | -99.70 | -67.67 | -99.70 | 6092 |
| 95 | Williams %R | reversion | 74.32 | -25.68 | 247 | 19.8 | -99.53 | -63.20 | -99.53 | 6088 |
| 96 | Heikin-Ashi | trend | 73.83 | -26.17 | 203 | 3.4 | -99.89 | -89.13 | -99.89 | 8319 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T04:05 | VWAP momentum | sell | DOGE-USD | 15.20 | -0.13 | exit signal |
| 2026-09-29T04:05 | ADX DI cross | buy | DOGE-USD | 4.11 | — | rebalance up |
| 2026-09-29T04:05 | ADX DI cross | sell | SOL-USD | 16.33 | -0.08 | exit signal |
| 2026-09-29T04:05 | ADX DI cross | sell | ETH-USD | 12.26 | -0.09 | exit signal |
| 2026-09-29T04:05 | EMA 9/21 cross | buy | ETH-USD | 3.91 | — | rebalance up |
| 2026-09-29T04:05 | EMA 9/21 cross | sell | BTC-USD | 3.91 | -0.03 | rebalance down |
| 2026-09-29T04:00 | Williams %R · 1h | buy | ETH-USD | 4.12 | — | entry signal |
| 2026-09-29T04:00 | Williams %R · 1h | buy | DOGE-USD | 5.47 | — | entry signal |
| 2026-09-29T04:00 | Stochastic reversion · 1h | buy | ETH-USD | 12.34 | — | entry signal |
| 2026-09-29T04:00 | Candlestick reversal · 1h | buy | DOGE-USD | 1.22 | — | entry signal |
| 2026-09-29T04:00 | MACD cross · 1h | buy | DOGE-USD | 19.37 | — | entry signal |
| 2026-09-29T04:00 | VWAP momentum | sell | BTC-USD | 19.03 | -0.13 | exit signal |
| 2026-09-29T04:00 | Heikin-Ashi | sell | SOL-USD | 14.82 | 0.00 | exit signal |
| 2026-09-29T04:00 | MACD zero-line | buy | ETH-USD | 8.50 | — | entry signal |
| 2026-09-29T04:00 | MACD zero-line | sell | XRP-USD | 4.22 | -0.03 | rebalance down |
| 2026-09-29T04:00 | MACD zero-line | sell | SOL-USD | 4.21 | -0.03 | rebalance down |
| 2026-09-29T03:55 | Three white soldiers | sell | BTC-USD | 23.79 | -0.18 | exit signal |
| 2026-09-29T03:50 | Heikin-Ashi | sell | XRP-USD | 18.47 | -0.11 | exit signal |
| 2026-09-29T03:50 | Heikin-Ashi | sell | ETH-USD | 18.46 | -0.11 | exit signal |
| 2026-09-29T03:50 | Heikin-Ashi | sell | DOGE-USD | 18.46 | -0.13 | exit signal |
| 2026-09-29T03:50 | Supertrend | buy | SOL-USD | 20.99 | — | entry signal |
| 2026-09-29T03:45 | Heikin-Ashi | buy | XRP-USD | 3.72 | — | rebalance up |
| 2026-09-29T03:45 | Heikin-Ashi | buy | ETH-USD | 3.71 | — | rebalance up |
| 2026-09-29T03:45 | Heikin-Ashi | buy | DOGE-USD | 3.72 | — | rebalance up |
| 2026-09-29T03:45 | Heikin-Ashi | sell | BTC-USD | 14.76 | -0.10 | exit signal |
| 2026-09-29T03:40 | Candlestick reversal | sell | ETH-USD | 19.74 | -0.05 | exit signal |
| 2026-09-29T03:40 | VWAP momentum | sell | ETH-USD | 7.66 | -0.05 | exit signal |
| 2026-09-29T03:40 | MACD zero-line | buy | BTC-USD | 21.11 | — | entry signal |
| 2026-09-29T03:35 | VWAP reversion | sell | ETH-USD | 21.25 | -0.04 | exit signal |
| 2026-09-29T03:35 | Squeeze breakout | buy | BTC-USD | 22.58 | — | entry signal |
| 2026-09-29T03:35 | VWAP momentum | buy | ETH-USD | 7.71 | — | entry signal |
| 2026-09-29T03:35 | VWAP momentum | sell | XRP-USD | 3.89 | 0.00 | rebalance down |
| 2026-09-29T03:35 | VWAP momentum | sell | DOGE-USD | 3.82 | -0.02 | rebalance down |
| 2026-09-29T03:35 | MACD zero-line | buy | SOL-USD | 21.15 | — | entry signal |
| 2026-09-29T03:35 | MACD zero-line | buy | DOGE-USD | 21.15 | — | entry signal |
| 2026-09-29T03:35 | EMA 9/21 cross | buy | ETH-USD | 7.91 | — | entry signal |
| 2026-09-29T03:35 | EMA 9/21 cross | sell | XRP-USD | 3.93 | -0.02 | rebalance down |
| 2026-09-29T03:35 | EMA 9/21 cross | sell | SOL-USD | 3.93 | -0.02 | rebalance down |
| 2026-09-29T03:30 | Z-score reversion | sell | DOGE-USD | 21.47 | 0.12 | target is flat |
| 2026-09-29T03:30 | Z-score reversion | sell | BTC-USD | 17.16 | -0.06 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
