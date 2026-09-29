# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T11:10:05.000152+00:00 · 5623 ticks

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

Today: 8160 decisions in 1632 calls, $0.1141 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T11:10 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-09-29T11:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T11:10 | 2 / 3 / 0 | ETH-USD 34%, DOGE-USD 24% |  |

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
| 2 | Hold BTC | benchmark | 100.55 | 0.55 | 0 | — | 30.08 | 3.78 | -8.68 | 1 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | RSI(14) reversion · 1h | reversion | 100.03 | 0.03 | 4 | 100.0 | 13.67 | 2.85 | -6.57 | 140 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.90 | -0.10 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.89 | -0.11 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.68 | -0.32 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | Daily: Bullish score | daily | 99.40 | -0.60 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 16 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 17 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 99.24 | -0.76 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 19 | Daily: SMA 20/50 cross · AAPL | daily | 99.23 | -0.77 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 20 | Z-score reversion · 1h | reversion | 99.22 | -0.78 | 6 | 50.0 | 4.31 | 1.05 | -8.60 | 154 |
| 21 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 25 | 56.0 | -12.30 | -2.73 | -13.77 | 324 |
| 22 | Connors RSI(2) · 1h | reversion | 99.16 | -0.84 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 23 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.14 | -0.86 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Williams %R · 1h | reversion | 98.75 | -1.25 | 33 | 51.5 | -17.93 | -3.29 | -19.52 | 485 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 27 | CCI reversion · 1h | reversion | 98.73 | -1.27 | 28 | 42.9 | 1.57 | 0.43 | -12.41 | 405 |
| 28 | Copy: Insider buying | copy | 98.71 | -1.29 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.15 | -2.52 | -11.75 | 234 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.30 | -1.71 | 13 | 23.1 | -25.92 | -6.04 | -26.44 | 493 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.24 | -1.76 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Supertrend · 1h | trend | 98.20 | -1.80 | 11 | 9.1 | 5.61 | 0.94 | -16.43 | 194 |
| 34 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 35 | Squeeze breakout · 1h | breakout | 98.08 | -1.92 | 7 | 14.3 | 15.95 | 2.81 | -6.26 | 95 |
| 36 | EMA 20/50 cross · 1h | trend | 98.04 | -1.97 | 8 | 12.5 | 15.59 | 1.86 | -14.36 | 126 |
| 37 | Bollinger reversion · 1h | reversion | 97.46 | -2.54 | 19 | 31.6 | -17.68 | -4.91 | -17.77 | 306 |
| 38 | MACD cross · 1h | trend | 97.43 | -2.57 | 31 | 9.7 | -16.12 | -2.73 | -20.74 | 460 |
| 39 | Donchian 55/20 · 1h | breakout | 97.34 | -2.66 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.30 | -2.70 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 42 | Agent (ML meta-label) | meta | 97.23 | -2.77 | 79 | 10.1 | 4.72 | 0.96 | -11.76 | 389 |
| 43 | Trend pullback · 1h | trend | 97.20 | -2.80 | 22 | 13.6 | -25.55 | -6.77 | -26.30 | 147 |
| 44 | Parabolic SAR · 1h | trend | 97.05 | -2.95 | 20 | 15.0 | -5.69 | -0.65 | -18.82 | 304 |
| 45 | Bollinger breakout · 1h | breakout | 97.04 | -2.96 | 13 | 7.7 | 13.32 | 1.89 | -9.85 | 285 |
| 46 | RSI momentum · 1h | momentum | 96.48 | -3.52 | 20 | 5.0 | 1.47 | 0.40 | -15.29 | 214 |
| 47 | Max aggression: 5-day momentum | meta | 96.45 | -3.55 | 1 | 0.0 | -0.14 | 0.34 | -29.56 | 29 |
| 48 | MACD zero-line · 1h | trend | 96.33 | -3.67 | 15 | 6.7 | -3.50 | -0.31 | -14.64 | 221 |
| 49 | Triple EMA stack · 1h | trend | 96.14 | -3.86 | 24 | 8.3 | -2.81 | -0.12 | -22.95 | 224 |
| 50 | Ichimoku · 1h | trend | 96.05 | -3.95 | 11 | 9.1 | 8.15 | 1.14 | -15.13 | 121 |
| 51 | EMA 9/21 cross · 1h | trend | 96.02 | -3.98 | 34 | 11.8 | 2.86 | 0.59 | -16.92 | 315 |
| 52 | MFI reversion · 1h | reversion | 95.92 | -4.08 | 38 | 13.2 | -9.20 | -1.68 | -17.20 | 125 |
| 53 | ADX DI cross · 1h | trend | 95.89 | -4.11 | 25 | 8.0 | -11.59 | -2.17 | -15.39 | 250 |
| 54 | Max aggression: 1-day momentum | meta | 95.72 | -4.28 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | Donchian 20/10 · 1h | breakout | 95.69 | -4.31 | 12 | 16.7 | 11.81 | 1.66 | -12.78 | 214 |
| 56 | Three white soldiers | momentum | 95.57 | -4.43 | 41 | 19.5 | -51.86 | -28.66 | -52.21 | 626 |
| 57 | OBV trend · 1h | momentum | 95.56 | -4.45 | 47 | 6.4 | -9.52 | -0.99 | -25.24 | 318 |
| 58 | VWAP momentum · 1h | momentum | 95.47 | -4.53 | 82 | 7.3 | -31.32 | -4.60 | -34.09 | 1248 |
| 59 | Volume breakout · 1h | breakout | 95.20 | -4.80 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.15 | -4.85 | 7 | 0.0 | -0.48 | 0.14 | -18.68 | 221 |
| 61 | Heikin-Ashi · 1h | trend | 94.26 | -5.74 | 35 | 11.4 | -22.30 | -3.32 | -29.64 | 680 |
| 62 | ROC + volume · 1h | momentum | 91.99 | -8.01 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.17 | -21.95 | -71.26 | 1473 |
| 64 | Squeeze breakout | breakout | 89.18 | -10.82 | 75 | 6.7 | -60.25 | -18.95 | -60.49 | 1186 |
| 65 | Donchian 55/20 | breakout | 88.99 | -11.01 | 79 | 11.4 | -68.31 | -15.80 | -68.56 | 1330 |
| 66 | ROC + volume | momentum | 88.53 | -11.47 | 123 | 17.1 | -72.06 | -18.01 | -72.65 | 1659 |
| 67 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 68 | Volume breakout | breakout | 88.26 | -11.74 | 82 | 12.2 | -62.36 | -20.54 | -62.56 | 909 |
| 69 | EMA 20/50 cross | trend | 88.15 | -11.85 | 97 | 13.4 | -78.80 | -17.74 | -79.29 | 1487 |
| 70 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 71 | Keltner breakout | breakout | 87.00 | -13.00 | 127 | 10.2 | -84.89 | -35.21 | -85.03 | 1929 |
| 72 | Ichimoku | trend | 86.74 | -13.26 | 94 | 8.5 | -80.49 | -26.46 | -80.54 | 1761 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.46 | -28.09 | -84.53 | 2081 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -70.93 | -17.21 | -71.75 | 1417 |
| 75 | Supertrend | trend | 83.91 | -16.09 | 148 | 16.2 | -87.24 | -24.70 | -87.53 | 1964 |
| 76 | MACD zero-line | trend | 83.60 | -16.40 | 161 | 14.9 | -91.60 | -36.32 | -91.79 | 2366 |
| 77 | Donchian 20/10 | breakout | 82.79 | -17.21 | 167 | 17.4 | -90.86 | -30.19 | -91.02 | 2686 |
| 78 | Trend pullback | trend | 82.74 | -17.26 | 143 | 15.4 | -90.50 | -34.06 | -90.50 | 2283 |
| 79 | Bollinger breakout | breakout | 82.30 | -17.70 | 172 | 14.5 | -93.98 | -42.52 | -94.08 | 2878 |
| 80 | MFI reversion | reversion | 82.18 | -17.82 | 154 | 17.5 | -87.77 | -34.74 | -87.92 | 2168 |
| 81 | Triple EMA stack | trend | 81.93 | -18.07 | 179 | 14.5 | -92.98 | -37.35 | -93.08 | 2626 |
| 82 | RSI momentum | momentum | 81.92 | -18.07 | 161 | 11.2 | -90.49 | -30.44 | -90.68 | 2406 |
| 83 | ADX DI cross | trend | 81.35 | -18.65 | 168 | 6.5 | -89.36 | -47.99 | -89.50 | 2125 |
| 84 | Connors RSI(2) | reversion | 79.81 | -20.19 | 212 | 16.0 | -96.38 | -41.96 | -96.38 | 3653 |
| 85 | Consensus | meta | 78.74 | -21.25 | 165 | 7.3 | -94.79 | -30.78 | -94.80 | 2670 |
| 86 | EMA 9/21 cross | trend | 78.53 | -21.47 | 231 | 15.2 | -97.38 | -42.66 | -97.43 | 3547 |
| 87 | Candlestick reversal | reversion | 78.36 | -21.64 | 205 | 14.1 | -99.35 | -52.63 | -99.35 | 5560 |
| 88 | Stochastic reversion | reversion | 77.95 | -22.05 | 262 | 22.9 | -95.90 | -48.72 | -95.91 | 4056 |
| 89 | OBV trend | momentum | 77.43 | -22.57 | 234 | 13.7 | -95.79 | -50.72 | -95.86 | 3563 |
| 90 | Bollinger reversion | reversion | 76.89 | -23.11 | 249 | 12.4 | -95.72 | -46.43 | -95.72 | 3669 |
| 91 | VWAP momentum | momentum | 75.59 | -24.41 | 301 | 9.0 | -98.47 | -37.27 | -98.49 | 5219 |
| 92 | CCI reversion | reversion | 75.08 | -24.92 | 181 | 5.5 | -98.44 | -52.66 | -98.44 | 4696 |
| 93 | Parabolic SAR | trend | 74.13 | -25.87 | 254 | 13.0 | -96.96 | -58.29 | -97.01 | 3664 |
| 94 | Williams %R | reversion | 73.60 | -26.40 | 261 | 19.2 | -99.52 | -62.56 | -99.52 | 6092 |
| 95 | MACD cross | trend | 73.38 | -26.62 | 207 | 10.6 | -99.70 | -66.85 | -99.70 | 6095 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.58 | -99.89 | 8335 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T11:10 | Williams %R | buy | DOGE-USD | 3.73 | — | entry signal |
| 2026-09-29T11:10 | Williams %R | buy | BTC-USD | 14.73 | — | entry signal |
| 2026-09-29T11:10 | Connors RSI(2) | sell | BTC-USD | 19.88 | -0.09 | exit signal |
| 2026-09-29T11:10 | Candlestick reversal | buy | BTC-USD | 19.60 | — | entry signal |
| 2026-09-29T11:10 | Ichimoku | buy | XRP-USD | 21.70 | — | entry signal |
| 2026-09-29T11:10 | Parabolic SAR | buy | XRP-USD | 18.56 | — | entry signal |
| 2026-09-29T11:10 | Parabolic SAR | buy | ETH-USD | 18.56 | — | entry signal |
| 2026-09-29T11:10 | MACD cross | buy | ETH-USD | 18.36 | — | entry signal |
| 2026-09-29T11:05 | Connors RSI(2) | buy | BTC-USD | 19.98 | — | entry signal |
| 2026-09-29T11:05 | OBV trend | buy | ETH-USD | 19.37 | — | entry signal |
| 2026-09-29T11:05 | OBV trend | sell | DOGE-USD | 15.67 | 0.21 | exit signal |
| 2026-09-29T11:05 | RSI momentum | sell | BTC-USD | 16.37 | -0.13 | stop-loss |
| 2026-09-29T11:05 | Trend pullback | sell | BTC-USD | 16.50 | -0.09 | exit signal |
| 2026-09-29T11:05 | ADX DI cross | sell | BTC-USD | 20.28 | -0.08 | exit signal |
| 2026-09-29T11:05 | Supertrend | sell | BTC-USD | 16.74 | -0.14 | exit signal |
| 2026-09-29T11:05 | Triple EMA stack | sell | BTC-USD | 20.12 | -0.12 | exit signal |
| 2026-09-29T11:05 | EMA 9/21 cross | sell | BTC-USD | 15.71 | -0.09 | exit signal |
| 2026-09-29T11:00 | MACD zero-line · 1h | buy | XRP-USD | 24.09 | — | entry signal |
| 2026-09-29T11:00 | Triple EMA stack | buy | XRP-USD | 20.51 | — | entry signal |
| 2026-09-29T11:00 | EMA 9/21 cross | buy | XRP-USD | 19.66 | — | entry signal |
| 2026-09-29T10:58 | Stochastic reversion | sell | SOL-USD | 3.89 | -0.02 | rebalance down |
| 2026-09-29T10:57 | Stochastic reversion | buy | ETH-USD | 3.91 | — | rebalance up |
| 2026-09-29T10:57 | Stochastic reversion | sell | XRP-USD | 3.91 | -0.02 | rebalance down |
| 2026-09-29T10:55 | Williams %R | buy | ETH-USD | 18.42 | — | entry signal |
| 2026-09-29T10:55 | Stochastic reversion | buy | ETH-USD | 7.85 | — | entry signal |
| 2026-09-29T10:55 | Stochastic reversion | buy | DOGE-USD | 15.62 | — | entry signal |
| 2026-09-29T10:55 | Stochastic reversion | buy | BTC-USD | 15.62 | — | entry signal |
| 2026-09-29T10:55 | Connors RSI(2) | sell | XRP-USD | 19.98 | -0.13 | exit signal |
| 2026-09-29T10:55 | Connors RSI(2) | sell | SOL-USD | 19.94 | -0.12 | exit signal |
| 2026-09-29T10:55 | Connors RSI(2) | sell | DOGE-USD | 19.94 | -0.16 | exit signal |
| 2026-09-29T10:55 | Connors RSI(2) | sell | BTC-USD | 19.93 | -0.11 | exit signal |
| 2026-09-29T10:55 | Candlestick reversal | buy | DOGE-USD | 19.62 | — | entry signal |
| 2026-09-29T10:55 | OBV trend | buy | XRP-USD | 19.39 | — | entry signal |
| 2026-09-29T10:50 | Williams %R | buy | XRP-USD | 18.44 | — | entry signal |
| 2026-09-29T10:50 | Williams %R | buy | SOL-USD | 18.44 | — | entry signal |
| 2026-09-29T10:50 | Stochastic reversion | buy | XRP-USD | 19.54 | — | entry signal |
| 2026-09-29T10:50 | Stochastic reversion | buy | SOL-USD | 19.54 | — | entry signal |
| 2026-09-29T10:50 | Connors RSI(2) | buy | BTC-USD | 20.03 | — | entry signal |
| 2026-09-29T10:50 | Candlestick reversal | buy | SOL-USD | 19.63 | — | entry signal |
| 2026-09-29T10:45 | Parabolic SAR | sell | ETH-USD | 18.54 | -0.13 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
