# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T08:10:05.000172+00:00 · 5481 ticks

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

Today: 6040 decisions in 1208 calls, $0.0845 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T08:10 | 3 / 1 / 1 | ETH-USD 14%, XRP-USD 13% |  |
| Breezy | 2026-09-29T08:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T08:10 | 4 / 1 / 0 | ETH-USD 38%, XRP-USD 28% |  |

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
| 3 | Hold BTC | benchmark | 100.40 | 0.40 | 0 | — | 30.07 | 3.78 | -8.68 | 1 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 11 | RSI(14) reversion · 1h | reversion | 99.91 | -0.09 | 3 | 100.0 | 15.29 | 3.20 | -6.57 | 136 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.78 | -0.22 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.77 | -0.23 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.56 | -0.44 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 17 | Daily: Bullish score | daily | 99.27 | -0.73 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | Z-score reversion · 1h | reversion | 99.13 | -0.87 | 6 | 50.0 | 3.75 | 0.93 | -8.60 | 155 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.12 | -0.88 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.11 | -0.90 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Connors RSI(2) · 1h | reversion | 99.10 | -0.90 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 23 | Stochastic reversion · 1h | reversion | 99.09 | -0.91 | 25 | 56.0 | -12.38 | -2.74 | -13.85 | 324 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.01 | -0.99 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | Williams %R · 1h | reversion | 98.64 | -1.36 | 33 | 51.5 | -17.95 | -3.30 | -19.54 | 485 |
| 27 | CCI reversion · 1h | reversion | 98.63 | -1.37 | 26 | 38.5 | 1.56 | 0.43 | -12.41 | 405 |
| 28 | Copy: Insider buying | copy | 98.60 | -1.40 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.15 | -2.52 | -11.75 | 234 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.24 | -1.76 | 12 | 16.7 | -25.72 | -6.00 | -26.26 | 490 |
| 32 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 98.11 | -1.89 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 34 | Supertrend · 1h | trend | 98.06 | -1.94 | 11 | 9.1 | 5.59 | 0.94 | -16.43 | 194 |
| 35 | Squeeze breakout · 1h | breakout | 97.99 | -2.01 | 7 | 14.3 | 16.32 | 2.86 | -6.26 | 94 |
| 36 | EMA 20/50 cross · 1h | trend | 97.91 | -2.09 | 8 | 12.5 | 15.62 | 1.87 | -14.36 | 125 |
| 37 | Bollinger reversion · 1h | reversion | 97.35 | -2.65 | 19 | 31.6 | -17.70 | -4.92 | -17.79 | 306 |
| 38 | MACD cross · 1h | trend | 97.26 | -2.74 | 31 | 9.7 | -15.97 | -2.70 | -20.52 | 459 |
| 39 | Donchian 55/20 · 1h | breakout | 97.25 | -2.75 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 40 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.18 | -2.83 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 42 | Agent (ML meta-label) | meta | 97.10 | -2.90 | 79 | 10.1 | 5.78 | 1.15 | -9.83 | 383 |
| 43 | Trend pullback · 1h | trend | 97.09 | -2.91 | 22 | 13.6 | -25.76 | -6.84 | -26.34 | 148 |
| 44 | Parabolic SAR · 1h | trend | 96.89 | -3.11 | 20 | 15.0 | -5.72 | -0.65 | -18.82 | 303 |
| 45 | Bollinger breakout · 1h | breakout | 96.88 | -3.12 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 285 |
| 46 | MACD zero-line · 1h | trend | 96.54 | -3.46 | 15 | 6.7 | -3.22 | -0.27 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.46 | -3.54 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 213 |
| 48 | Max aggression: 5-day momentum | meta | 96.29 | -3.71 | 1 | 0.0 | -0.17 | 0.34 | -29.56 | 29 |
| 49 | Triple EMA stack · 1h | trend | 96.02 | -3.98 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 50 | Ichimoku · 1h | trend | 95.88 | -4.12 | 11 | 9.1 | 8.10 | 1.13 | -15.13 | 121 |
| 51 | EMA 9/21 cross · 1h | trend | 95.88 | -4.12 | 34 | 11.8 | 2.85 | 0.59 | -16.92 | 313 |
| 52 | Donchian 20/10 · 1h | breakout | 95.81 | -4.18 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 53 | MFI reversion · 1h | reversion | 95.80 | -4.20 | 38 | 13.2 | -9.20 | -1.68 | -17.20 | 125 |
| 54 | ADX DI cross · 1h | trend | 95.72 | -4.29 | 25 | 8.0 | -11.91 | -2.24 | -15.43 | 251 |
| 55 | Three white soldiers | momentum | 95.63 | -4.37 | 40 | 17.5 | -51.83 | -28.60 | -52.21 | 626 |
| 56 | Max aggression: 1-day momentum | meta | 95.60 | -4.40 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 57 | OBV trend · 1h | momentum | 95.46 | -4.54 | 47 | 6.4 | -9.59 | -1.00 | -25.24 | 317 |
| 58 | VWAP momentum · 1h | momentum | 95.30 | -4.70 | 82 | 7.3 | -31.89 | -4.70 | -34.09 | 1251 |
| 59 | Volume breakout · 1h | breakout | 95.17 | -4.83 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.12 | -4.88 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 94.05 | -5.95 | 35 | 11.4 | -22.87 | -3.42 | -29.48 | 683 |
| 62 | ROC + volume · 1h | momentum | 91.90 | -8.10 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.90 | -22.35 | -71.98 | 1484 |
| 64 | Squeeze breakout | breakout | 89.45 | -10.55 | 73 | 5.5 | -60.12 | -18.88 | -60.45 | 1185 |
| 65 | ROC + volume | momentum | 89.32 | -10.68 | 118 | 16.9 | -71.77 | -17.79 | -72.42 | 1656 |
| 66 | Donchian 55/20 | breakout | 89.06 | -10.94 | 77 | 11.7 | -68.25 | -15.76 | -68.56 | 1330 |
| 67 | Volume breakout | breakout | 88.69 | -11.31 | 80 | 12.5 | -62.16 | -20.34 | -62.47 | 907 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | EMA 20/50 cross | trend | 87.95 | -12.05 | 97 | 13.4 | -78.89 | -17.78 | -79.32 | 1488 |
| 71 | Ichimoku | trend | 87.79 | -12.21 | 85 | 8.2 | -80.25 | -25.96 | -80.34 | 1755 |
| 72 | Keltner breakout | breakout | 87.66 | -12.34 | 120 | 10.0 | -84.78 | -34.63 | -84.97 | 1928 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.62 | -28.42 | -84.69 | 2086 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -71.08 | -17.38 | -71.75 | 1418 |
| 75 | Supertrend | trend | 84.45 | -15.55 | 143 | 15.4 | -87.13 | -24.46 | -87.53 | 1961 |
| 76 | MACD zero-line | trend | 83.80 | -16.20 | 159 | 15.1 | -91.60 | -36.33 | -91.77 | 2365 |
| 77 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.50 | -33.62 | -90.50 | 2280 |
| 78 | Donchian 20/10 | breakout | 83.02 | -16.98 | 162 | 14.8 | -90.82 | -30.02 | -91.02 | 2686 |
| 79 | RSI momentum | momentum | 82.80 | -17.20 | 153 | 10.5 | -90.40 | -30.25 | -90.63 | 2403 |
| 80 | Bollinger breakout | breakout | 82.71 | -17.29 | 168 | 13.7 | -93.95 | -42.36 | -94.06 | 2877 |
| 81 | Triple EMA stack | trend | 82.71 | -17.29 | 173 | 13.3 | -92.91 | -36.91 | -93.07 | 2621 |
| 82 | MFI reversion | reversion | 82.15 | -17.86 | 153 | 17.0 | -87.79 | -34.84 | -87.92 | 2167 |
| 83 | ADX DI cross | trend | 81.43 | -18.57 | 167 | 6.6 | -89.39 | -48.30 | -89.49 | 2126 |
| 84 | Connors RSI(2) | reversion | 80.92 | -19.08 | 200 | 17.0 | -96.37 | -41.09 | -96.37 | 3651 |
| 85 | EMA 9/21 cross | trend | 79.37 | -20.63 | 223 | 13.5 | -97.35 | -41.99 | -97.43 | 3543 |
| 86 | Consensus | meta | 79.24 | -20.76 | 160 | 6.9 | -94.71 | -30.29 | -94.72 | 2661 |
| 87 | Candlestick reversal | reversion | 78.66 | -21.34 | 201 | 13.9 | -99.36 | -53.21 | -99.36 | 5567 |
| 88 | Stochastic reversion | reversion | 78.43 | -21.57 | 258 | 23.3 | -95.93 | -48.97 | -95.94 | 4052 |
| 89 | OBV trend | momentum | 78.19 | -21.81 | 225 | 12.4 | -95.75 | -49.98 | -95.85 | 3559 |
| 90 | Bollinger reversion | reversion | 77.13 | -22.87 | 246 | 12.6 | -95.80 | -46.92 | -95.80 | 3677 |
| 91 | VWAP momentum | momentum | 75.40 | -24.60 | 301 | 9.0 | -98.48 | -37.33 | -98.49 | 5218 |
| 92 | Parabolic SAR | trend | 75.23 | -24.77 | 244 | 13.5 | -96.94 | -58.44 | -96.96 | 3657 |
| 93 | CCI reversion | reversion | 75.22 | -24.78 | 176 | 5.7 | -98.47 | -53.48 | -98.47 | 4700 |
| 94 | Williams %R | reversion | 74.01 | -25.99 | 256 | 19.5 | -99.53 | -63.51 | -99.53 | 6092 |
| 95 | MACD cross | trend | 73.93 | -26.07 | 202 | 10.9 | -99.71 | -69.05 | -99.71 | 6100 |
| 96 | Heikin-Ashi | trend | 71.57 | -28.43 | 226 | 3.5 | -99.89 | -92.08 | -99.89 | 8328 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T08:10 | Connors RSI(2) | buy | XRP-USD | 20.28 | — | entry signal |
| 2026-09-29T08:10 | Connors RSI(2) | buy | SOL-USD | 20.28 | — | entry signal |
| 2026-09-29T08:10 | Connors RSI(2) | buy | DOGE-USD | 20.28 | — | entry signal |
| 2026-09-29T08:10 | Volume breakout | sell | ETH-USD | 22.21 | 0.08 | time stop |
| 2026-09-29T08:10 | Squeeze breakout | sell | XRP-USD | 22.28 | -0.07 | exit signal |
| 2026-09-29T08:10 | Squeeze breakout | sell | SOL-USD | 22.26 | -0.08 | exit signal |
| 2026-09-29T08:10 | Bollinger breakout | sell | XRP-USD | 16.49 | -0.05 | exit signal |
| 2026-09-29T08:10 | Bollinger breakout | sell | SOL-USD | 16.47 | -0.06 | exit signal |
| 2026-09-29T08:10 | Bollinger breakout | sell | DOGE-USD | 16.51 | -0.02 | exit signal |
| 2026-09-29T08:10 | ROC + volume | sell | SOL-USD | 22.19 | -0.08 | exit signal |
| 2026-09-29T08:10 | ROC + volume | sell | DOGE-USD | 17.85 | 0.11 | exit signal |
| 2026-09-29T08:10 | Parabolic SAR | sell | XRP-USD | 18.79 | -0.17 | exit signal |
| 2026-09-29T08:10 | Parabolic SAR | sell | DOGE-USD | 18.76 | -0.20 | exit signal |
| 2026-09-29T08:05 | Consensus | sell | DOGE-USD | 15.89 | 0.00 | target is flat |
| 2026-09-29T08:05 | Z-score reversion · 1h | sell | DOGE-USD | 16.54 | 0.09 | target is flat |
| 2026-09-29T08:05 | Three white soldiers | sell | DOGE-USD | 23.90 | 0.14 | exit signal |
| 2026-09-29T08:05 | Volume breakout | sell | SOL-USD | 22.21 | 0.05 | time stop |
| 2026-09-29T08:05 | Volume breakout | sell | DOGE-USD | 22.18 | 0.01 | exit signal |
| 2026-09-29T08:00 | Consensus | sell | SOL-USD | 19.81 | -0.04 | target is flat |
| 2026-09-29T08:00 | Williams %R · 1h | sell | SOL-USD | 5.52 | -0.02 | exit signal |
| 2026-09-29T08:00 | Williams %R · 1h | sell | ETH-USD | 4.17 | 0.05 | exit signal |
| 2026-09-29T08:00 | Stochastic reversion · 1h | sell | SOL-USD | 10.91 | -0.06 | exit signal |
| 2026-09-29T08:00 | Stochastic reversion · 1h | sell | ETH-USD | 12.50 | 0.15 | exit signal |
| 2026-09-29T08:00 | RSI(14) reversion · 1h | buy | SOL-USD | 8.57 | — | rebalance up |
| 2026-09-29T08:00 | RSI(14) reversion · 1h | sell | DOGE-USD | 16.92 | 0.28 | exit signal |
| 2026-09-29T08:00 | Squeeze breakout · 1h | buy | ETH-USD | 24.51 | — | entry signal |
| 2026-09-29T08:00 | Heikin-Ashi · 1h | buy | XRP-USD | 12.40 | — | entry signal |
| 2026-09-29T08:00 | Heikin-Ashi · 1h | buy | SOL-USD | 15.72 | — | entry signal |
| 2026-09-29T08:00 | Heikin-Ashi · 1h | buy | ETH-USD | 15.72 | — | entry signal |
| 2026-09-29T08:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 15.72 | — | entry signal |
| 2026-09-29T08:00 | Heikin-Ashi · 1h | buy | BTC-USD | 15.72 | — | entry signal |
| 2026-09-29T08:00 | Ichimoku · 1h | buy | BTC-USD | 23.98 | — | entry signal |
| 2026-09-29T08:00 | Parabolic SAR · 1h | buy | ETH-USD | 11.57 | — | entry signal |
| 2026-09-29T08:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 5.27 | — | entry signal |
| 2026-09-29T08:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 5.27 | -0.02 | rebalance down |
| 2026-09-29T08:00 | Three white soldiers | sell | BTC-USD | 23.81 | 0.03 | exit signal |
| 2026-09-29T08:00 | Volume breakout | sell | BTC-USD | 22.09 | -0.08 | exit signal |
| 2026-09-29T08:00 | ROC + volume | buy | XRP-USD | 8.88 | — | rebalance up |
| 2026-09-29T08:00 | ROC + volume | sell | BTC-USD | 17.81 | -0.06 | exit signal |
| 2026-09-29T08:00 | Parabolic SAR | sell | SOL-USD | 15.09 | 0.05 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
