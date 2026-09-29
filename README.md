# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T08:40:05.000162+00:00 · 5503 ticks

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

Today: 6370 decisions in 1274 calls, $0.0891 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T08:40 | 2 / 3 / 0 | SOL-USD 14% |  |
| Breezy | 2026-09-29T08:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T08:40 | 3 / 2 / 0 | ETH-USD 24%, SOL-USD 22% |  |

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
| 3 | Hold BTC | benchmark | 100.33 | 0.33 | 0 | — | 29.63 | 3.73 | -8.68 | 1 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 11 | RSI(14) reversion · 1h | reversion | 99.94 | -0.07 | 3 | 100.0 | 15.28 | 3.20 | -6.57 | 136 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.83 | -0.17 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.81 | -0.18 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.61 | -0.39 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 16 | Daily: Bullish score | daily | 99.32 | -0.68 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 17 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.05 | -4.73 | 190 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 99.17 | -0.83 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 99.15 | -0.85 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 21 | Z-score reversion · 1h | reversion | 99.15 | -0.85 | 6 | 50.0 | 3.74 | 0.93 | -8.60 | 155 |
| 22 | Connors RSI(2) · 1h | reversion | 99.13 | -0.87 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 23 | Stochastic reversion · 1h | reversion | 99.12 | -0.88 | 25 | 56.0 | -12.31 | -2.73 | -13.78 | 324 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.06 | -0.94 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | Williams %R · 1h | reversion | 98.68 | -1.32 | 33 | 51.5 | -17.93 | -3.29 | -19.52 | 485 |
| 27 | CCI reversion · 1h | reversion | 98.66 | -1.34 | 26 | 38.5 | 1.56 | 0.43 | -12.41 | 405 |
| 28 | Copy: Insider buying | copy | 98.64 | -1.36 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.32 | -2.59 | -11.75 | 233 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.25 | -1.75 | 12 | 16.7 | -25.74 | -6.01 | -26.25 | 490 |
| 32 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 98.16 | -1.84 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 34 | Supertrend · 1h | trend | 98.09 | -1.91 | 11 | 9.1 | 5.57 | 0.94 | -16.43 | 194 |
| 35 | Squeeze breakout · 1h | breakout | 97.99 | -2.01 | 7 | 14.3 | 15.89 | 2.80 | -6.26 | 95 |
| 36 | EMA 20/50 cross · 1h | trend | 97.95 | -2.05 | 8 | 12.5 | 15.62 | 1.87 | -14.36 | 125 |
| 37 | Bollinger reversion · 1h | reversion | 97.40 | -2.60 | 19 | 31.6 | -17.68 | -4.91 | -17.77 | 306 |
| 38 | Donchian 55/20 · 1h | breakout | 97.29 | -2.71 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 39 | MACD cross · 1h | trend | 97.25 | -2.75 | 31 | 9.7 | -16.02 | -2.71 | -20.52 | 459 |
| 40 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.74 | -16.14 | 692 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.22 | -2.78 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 42 | Agent (ML meta-label) | meta | 97.15 | -2.85 | 79 | 10.1 | 4.83 | 0.98 | -10.87 | 383 |
| 43 | Trend pullback · 1h | trend | 97.13 | -2.87 | 22 | 13.6 | -25.76 | -6.84 | -26.34 | 148 |
| 44 | Parabolic SAR · 1h | trend | 96.93 | -3.07 | 20 | 15.0 | -5.76 | -0.66 | -18.82 | 303 |
| 45 | Bollinger breakout · 1h | breakout | 96.91 | -3.09 | 13 | 7.7 | 13.26 | 1.88 | -9.85 | 285 |
| 46 | MACD zero-line · 1h | trend | 96.54 | -3.46 | 15 | 6.7 | -3.24 | -0.27 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.48 | -3.52 | 20 | 5.0 | 1.56 | 0.41 | -15.29 | 213 |
| 48 | Max aggression: 5-day momentum | meta | 96.29 | -3.71 | 1 | 0.0 | -0.22 | 0.33 | -29.56 | 29 |
| 49 | Triple EMA stack · 1h | trend | 96.05 | -3.95 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 50 | EMA 9/21 cross · 1h | trend | 95.91 | -4.09 | 34 | 11.8 | 2.82 | 0.58 | -16.92 | 313 |
| 51 | Ichimoku · 1h | trend | 95.89 | -4.11 | 11 | 9.1 | 8.06 | 1.13 | -15.13 | 121 |
| 52 | Donchian 20/10 · 1h | breakout | 95.84 | -4.16 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 53 | MFI reversion · 1h | reversion | 95.83 | -4.17 | 38 | 13.2 | -9.21 | -1.68 | -17.20 | 125 |
| 54 | ADX DI cross · 1h | trend | 95.72 | -4.28 | 25 | 8.0 | -12.07 | -2.27 | -15.43 | 252 |
| 55 | Max aggression: 1-day momentum | meta | 95.65 | -4.35 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 56 | Three white soldiers | momentum | 95.57 | -4.43 | 41 | 19.5 | -51.86 | -28.66 | -52.21 | 626 |
| 57 | OBV trend · 1h | momentum | 95.48 | -4.52 | 47 | 6.4 | -9.59 | -1.00 | -25.24 | 317 |
| 58 | VWAP momentum · 1h | momentum | 95.33 | -4.67 | 82 | 7.3 | -31.93 | -4.71 | -34.09 | 1251 |
| 59 | Volume breakout · 1h | breakout | 95.19 | -4.82 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.14 | -4.86 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 94.02 | -5.98 | 35 | 11.4 | -22.94 | -3.43 | -29.54 | 683 |
| 62 | ROC + volume · 1h | momentum | 91.94 | -8.06 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.21 | -22.00 | -71.30 | 1473 |
| 64 | Squeeze breakout | breakout | 89.38 | -10.62 | 74 | 6.8 | -60.17 | -18.91 | -60.47 | 1185 |
| 65 | ROC + volume | momentum | 89.18 | -10.82 | 120 | 17.5 | -71.83 | -17.84 | -72.42 | 1656 |
| 66 | Donchian 55/20 | breakout | 88.93 | -11.07 | 78 | 11.5 | -68.31 | -15.81 | -68.54 | 1330 |
| 67 | Volume breakout | breakout | 88.47 | -11.53 | 81 | 12.3 | -62.25 | -20.44 | -62.47 | 908 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | EMA 20/50 cross | trend | 87.90 | -12.10 | 97 | 13.4 | -78.93 | -17.80 | -79.30 | 1488 |
| 71 | Ichimoku | trend | 87.53 | -12.46 | 90 | 8.9 | -80.34 | -26.09 | -80.36 | 1755 |
| 72 | Keltner breakout | breakout | 87.35 | -12.65 | 125 | 10.4 | -84.82 | -34.90 | -84.97 | 1927 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.59 | -28.36 | -84.65 | 2085 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -71.30 | -17.54 | -71.87 | 1417 |
| 75 | Supertrend | trend | 84.40 | -15.60 | 143 | 15.4 | -87.09 | -24.49 | -87.47 | 1960 |
| 76 | MACD zero-line | trend | 83.80 | -16.20 | 159 | 15.1 | -91.60 | -36.33 | -91.77 | 2365 |
| 77 | Donchian 20/10 | breakout | 82.88 | -17.12 | 164 | 15.9 | -90.85 | -30.12 | -91.02 | 2686 |
| 78 | Trend pullback | trend | 82.87 | -17.13 | 140 | 15.7 | -90.54 | -33.82 | -90.54 | 2283 |
| 79 | RSI momentum | momentum | 82.75 | -17.25 | 153 | 10.5 | -90.41 | -30.26 | -90.64 | 2403 |
| 80 | Triple EMA stack | trend | 82.66 | -17.34 | 173 | 13.3 | -92.94 | -37.03 | -93.07 | 2622 |
| 81 | Bollinger breakout | breakout | 82.61 | -17.39 | 170 | 14.7 | -93.95 | -42.31 | -94.06 | 2876 |
| 82 | MFI reversion | reversion | 82.15 | -17.86 | 153 | 17.0 | -87.79 | -34.84 | -87.92 | 2167 |
| 83 | ADX DI cross | trend | 81.43 | -18.57 | 167 | 6.6 | -89.40 | -48.47 | -89.48 | 2127 |
| 84 | Connors RSI(2) | reversion | 80.82 | -19.18 | 203 | 16.7 | -96.38 | -41.19 | -96.38 | 3652 |
| 85 | EMA 9/21 cross | trend | 79.33 | -20.67 | 223 | 13.5 | -97.36 | -42.15 | -97.43 | 3544 |
| 86 | Consensus | meta | 79.19 | -20.81 | 161 | 7.5 | -94.72 | -30.33 | -94.73 | 2662 |
| 87 | Candlestick reversal | reversion | 78.66 | -21.34 | 201 | 13.9 | -99.35 | -52.66 | -99.35 | 5556 |
| 88 | Stochastic reversion | reversion | 78.43 | -21.57 | 258 | 23.3 | -95.93 | -48.97 | -95.94 | 4052 |
| 89 | OBV trend | momentum | 78.03 | -21.97 | 227 | 13.2 | -95.76 | -50.27 | -95.85 | 3557 |
| 90 | Bollinger reversion | reversion | 77.13 | -22.87 | 246 | 12.6 | -95.80 | -46.92 | -95.80 | 3677 |
| 91 | VWAP momentum | momentum | 75.36 | -24.64 | 301 | 9.0 | -98.46 | -37.22 | -98.47 | 5209 |
| 92 | CCI reversion | reversion | 75.22 | -24.78 | 176 | 5.7 | -98.47 | -53.47 | -98.47 | 4700 |
| 93 | Parabolic SAR | trend | 74.66 | -25.34 | 249 | 13.3 | -96.97 | -59.36 | -96.98 | 3662 |
| 94 | MACD cross | trend | 73.93 | -26.07 | 202 | 10.9 | -99.70 | -68.32 | -99.70 | 6097 |
| 95 | Williams %R | reversion | 73.84 | -26.16 | 256 | 19.5 | -99.53 | -63.72 | -99.53 | 6094 |
| 96 | Heikin-Ashi | trend | 70.94 | -29.05 | 231 | 3.5 | -99.89 | -92.62 | -99.89 | 8330 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T08:40 | Consensus | sell | ETH-USD | 15.91 | 0.06 | target is flat |
| 2026-09-29T08:40 | Williams %R | buy | XRP-USD | 18.50 | — | entry signal |
| 2026-09-29T08:40 | Williams %R | buy | SOL-USD | 18.50 | — | entry signal |
| 2026-09-29T08:40 | Williams %R | buy | DOGE-USD | 18.50 | — | entry signal |
| 2026-09-29T08:40 | Connors RSI(2) | buy | XRP-USD | 20.22 | — | entry signal |
| 2026-09-29T08:40 | Squeeze breakout | sell | ETH-USD | 22.50 | 0.15 | stop-loss |
| 2026-09-29T08:40 | Keltner breakout | sell | ETH-USD | 17.56 | 0.06 | stop-loss |
| 2026-09-29T08:40 | Keltner breakout | sell | BTC-USD | 21.82 | -0.05 | stop-loss |
| 2026-09-29T08:40 | Bollinger breakout | sell | ETH-USD | 16.61 | 0.11 | stop-loss |
| 2026-09-29T08:40 | Donchian 55/20 | buy | SOL-USD | 4.49 | — | rebalance up |
| 2026-09-29T08:40 | Donchian 55/20 | buy | BTC-USD | 4.48 | — | rebalance up |
| 2026-09-29T08:40 | Donchian 55/20 | sell | XRP-USD | 17.70 | 0.00 | exit signal |
| 2026-09-29T08:40 | Donchian 20/10 | sell | XRP-USD | 12.29 | 0.00 | exit signal |
| 2026-09-29T08:40 | Donchian 20/10 | sell | BTC-USD | 20.59 | 0.02 | exit signal |
| 2026-09-29T08:40 | ROC + volume | sell | ETH-USD | 17.94 | 0.06 | exit signal |
| 2026-09-29T08:40 | Ichimoku | sell | ETH-USD | 17.57 | 0.04 | exit signal |
| 2026-09-29T08:40 | Parabolic SAR | sell | ETH-USD | 14.94 | -0.10 | exit signal |
| 2026-09-29T08:36 | Three white soldiers | sell | ETH-USD | 23.97 | 0.21 | exit signal |
| 2026-09-29T08:36 | Volume breakout | sell | ETH-USD | 21.95 | -0.22 | exit signal |
| 2026-09-29T08:36 | Keltner breakout | buy | BTC-USD | 4.40 | — | rebalance up |
| 2026-09-29T08:36 | Keltner breakout | sell | XRP-USD | 17.43 | -0.06 | exit signal |
| 2026-09-29T08:36 | Keltner breakout | sell | SOL-USD | 17.44 | -0.05 | exit signal |
| 2026-09-29T08:36 | Keltner breakout | sell | DOGE-USD | 17.48 | -0.02 | exit signal |
| 2026-09-29T08:36 | Bollinger breakout | sell | BTC-USD | 16.54 | 0.02 | exit signal |
| 2026-09-29T08:36 | OBV trend | buy | ETH-USD | 11.50 | — | rebalance up |
| 2026-09-29T08:36 | OBV trend | sell | XRP-USD | 19.32 | 0.10 | exit signal |
| 2026-09-29T08:36 | OBV trend | sell | SOL-USD | 15.58 | 0.10 | exit signal |
| 2026-09-29T08:36 | ROC + volume | sell | XRP-USD | 22.27 | -0.13 | exit signal |
| 2026-09-29T08:36 | Heikin-Ashi | sell | XRP-USD | 7.13 | -0.06 | exit signal |
| 2026-09-29T08:36 | Heikin-Ashi | sell | SOL-USD | 14.17 | -0.12 | exit signal |
| 2026-09-29T08:36 | Heikin-Ashi | sell | ETH-USD | 14.20 | -0.09 | exit signal |
| 2026-09-29T08:36 | Heikin-Ashi | sell | DOGE-USD | 17.71 | -0.19 | exit signal |
| 2026-09-29T08:36 | Heikin-Ashi | sell | BTC-USD | 17.74 | -0.15 | exit signal |
| 2026-09-29T08:36 | Ichimoku | sell | XRP-USD | 17.47 | -0.06 | exit signal |
| 2026-09-29T08:36 | Ichimoku | sell | SOL-USD | 17.50 | -0.04 | exit signal |
| 2026-09-29T08:36 | Ichimoku | sell | DOGE-USD | 17.52 | -0.01 | exit signal |
| 2026-09-29T08:36 | Ichimoku | sell | BTC-USD | 17.47 | -0.07 | exit signal |
| 2026-09-29T08:36 | Parabolic SAR | sell | XRP-USD | 14.90 | -0.14 | exit signal |
| 2026-09-29T08:36 | Parabolic SAR | sell | SOL-USD | 14.93 | -0.13 | exit signal |
| 2026-09-29T08:36 | Parabolic SAR | sell | DOGE-USD | 14.90 | -0.16 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
