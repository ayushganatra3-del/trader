# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T10:10:05.000148+00:00 · 5578 ticks

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

Today: 7495 decisions in 1499 calls, $0.1048 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T10:10 | 3 / 1 / 1 | SOL-USD 20%, ETH-USD 19%, XRP-USD 19% |  |
| Breezy | 2026-09-29T10:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T10:10 | 5 / 0 / 0 | ETH-USD 42%, BTC-USD 39% |  |

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
| 2 | Hold BTC | benchmark | 100.73 | 0.73 | 0 | — | 30.33 | 3.80 | -8.68 | 1 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | RSI(14) reversion · 1h | reversion | 99.98 | -0.02 | 4 | 100.0 | 15.52 | 3.24 | -6.57 | 138 |
| 11 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.80 | -0.20 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.79 | -0.21 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.58 | -0.41 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 17 | Daily: Bullish score | daily | 99.30 | -0.70 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Z-score reversion · 1h | reversion | 99.23 | -0.77 | 6 | 50.0 | 4.41 | 1.07 | -8.60 | 154 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.14 | -0.85 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.13 | -0.87 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Connors RSI(2) · 1h | reversion | 99.11 | -0.89 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 23 | Stochastic reversion · 1h | reversion | 99.10 | -0.90 | 25 | 56.0 | -12.40 | -2.74 | -13.87 | 324 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.04 | -0.96 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | CCI reversion · 1h | reversion | 98.66 | -1.34 | 28 | 42.9 | 1.57 | 0.43 | -12.41 | 405 |
| 27 | Williams %R · 1h | reversion | 98.66 | -1.34 | 33 | 51.5 | -17.95 | -3.30 | -19.54 | 485 |
| 28 | Copy: Insider buying | copy | 98.62 | -1.38 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.15 | -2.52 | -11.75 | 234 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.27 | -1.73 | 13 | 23.1 | -25.89 | -6.03 | -26.45 | 493 |
| 32 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 33 | Supertrend · 1h | trend | 98.14 | -1.86 | 11 | 9.1 | 5.65 | 0.95 | -16.43 | 194 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 98.14 | -1.86 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 35 | Squeeze breakout · 1h | breakout | 98.05 | -1.95 | 7 | 14.3 | 16.38 | 2.87 | -6.26 | 94 |
| 36 | EMA 20/50 cross · 1h | trend | 97.95 | -2.05 | 8 | 12.5 | 15.60 | 1.87 | -14.36 | 126 |
| 37 | MACD cross · 1h | trend | 97.51 | -2.49 | 31 | 9.7 | -15.98 | -2.70 | -20.74 | 460 |
| 38 | Bollinger reversion · 1h | reversion | 97.38 | -2.62 | 19 | 31.6 | -17.67 | -4.91 | -17.76 | 306 |
| 39 | Donchian 55/20 · 1h | breakout | 97.27 | -2.73 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 40 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.20 | -2.80 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 42 | Agent (ML meta-label) | meta | 97.14 | -2.86 | 79 | 10.1 | 4.42 | 0.92 | -10.68 | 394 |
| 43 | Trend pullback · 1h | trend | 97.12 | -2.88 | 22 | 13.6 | -25.55 | -6.77 | -26.30 | 147 |
| 44 | Parabolic SAR · 1h | trend | 97.03 | -2.97 | 20 | 15.0 | -5.58 | -0.63 | -18.82 | 304 |
| 45 | Bollinger breakout · 1h | breakout | 96.95 | -3.05 | 13 | 7.7 | 13.33 | 1.89 | -9.85 | 285 |
| 46 | Max aggression: 5-day momentum | meta | 96.80 | -3.19 | 1 | 0.0 | 0.33 | 0.38 | -29.56 | 29 |
| 47 | MACD zero-line · 1h | trend | 96.55 | -3.45 | 15 | 6.7 | -3.21 | -0.26 | -14.64 | 220 |
| 48 | RSI momentum · 1h | momentum | 96.46 | -3.54 | 20 | 5.0 | 1.56 | 0.41 | -15.29 | 214 |
| 49 | Triple EMA stack · 1h | trend | 96.06 | -3.94 | 24 | 8.3 | -2.84 | -0.12 | -22.95 | 224 |
| 50 | Ichimoku · 1h | trend | 96.03 | -3.97 | 11 | 9.1 | 8.24 | 1.15 | -15.13 | 121 |
| 51 | ADX DI cross · 1h | trend | 96.00 | -4.00 | 25 | 8.0 | -11.41 | -2.13 | -15.39 | 250 |
| 52 | EMA 9/21 cross · 1h | trend | 95.95 | -4.05 | 34 | 11.8 | 3.00 | 0.61 | -16.92 | 315 |
| 53 | MFI reversion · 1h | reversion | 95.92 | -4.08 | 38 | 13.2 | -9.11 | -1.66 | -17.20 | 125 |
| 54 | Donchian 20/10 · 1h | breakout | 95.74 | -4.26 | 12 | 16.7 | 11.95 | 1.68 | -12.78 | 214 |
| 55 | Max aggression: 1-day momentum | meta | 95.63 | -4.38 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 56 | Three white soldiers | momentum | 95.57 | -4.43 | 41 | 19.5 | -51.86 | -28.66 | -52.21 | 626 |
| 57 | OBV trend · 1h | momentum | 95.50 | -4.50 | 47 | 6.4 | -9.50 | -0.99 | -25.24 | 318 |
| 58 | VWAP momentum · 1h | momentum | 95.46 | -4.54 | 82 | 7.3 | -31.73 | -4.67 | -34.09 | 1251 |
| 59 | Volume breakout · 1h | breakout | 95.18 | -4.82 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.13 | -4.87 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 94.40 | -5.60 | 35 | 11.4 | -22.60 | -3.37 | -29.64 | 683 |
| 62 | ROC + volume · 1h | momentum | 91.92 | -8.08 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.50 | -22.23 | -71.59 | 1479 |
| 64 | Squeeze breakout | breakout | 89.31 | -10.69 | 74 | 6.8 | -60.19 | -18.92 | -60.45 | 1186 |
| 65 | Donchian 55/20 | breakout | 89.14 | -10.86 | 79 | 11.4 | -68.22 | -15.73 | -68.56 | 1330 |
| 66 | ROC + volume | momentum | 88.93 | -11.07 | 120 | 17.5 | -71.91 | -17.90 | -72.51 | 1659 |
| 67 | Volume breakout | breakout | 88.37 | -11.63 | 81 | 12.3 | -62.30 | -20.48 | -62.50 | 909 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | EMA 20/50 cross | trend | 88.26 | -11.74 | 97 | 13.4 | -78.77 | -17.70 | -79.32 | 1487 |
| 70 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 71 | Ichimoku | trend | 87.31 | -12.69 | 90 | 8.9 | -80.37 | -26.23 | -80.39 | 1759 |
| 72 | Keltner breakout | breakout | 87.21 | -12.79 | 125 | 10.4 | -84.84 | -35.02 | -84.99 | 1929 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.50 | -28.17 | -84.57 | 2081 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -71.12 | -17.41 | -71.75 | 1419 |
| 75 | Supertrend | trend | 84.25 | -15.75 | 146 | 15.8 | -87.18 | -24.56 | -87.53 | 1964 |
| 76 | MACD zero-line | trend | 83.77 | -16.23 | 159 | 15.1 | -91.61 | -36.39 | -91.78 | 2367 |
| 77 | Trend pullback | trend | 83.07 | -16.93 | 141 | 15.6 | -90.50 | -33.74 | -90.53 | 2285 |
| 78 | Donchian 20/10 | breakout | 83.01 | -16.99 | 165 | 16.4 | -90.83 | -30.04 | -91.02 | 2686 |
| 79 | Bollinger breakout | breakout | 82.55 | -17.45 | 170 | 14.7 | -93.96 | -42.36 | -94.06 | 2878 |
| 80 | Triple EMA stack | trend | 82.53 | -17.47 | 175 | 14.3 | -92.93 | -37.05 | -93.07 | 2625 |
| 81 | RSI momentum | momentum | 82.38 | -17.62 | 157 | 10.8 | -90.42 | -30.31 | -90.63 | 2406 |
| 82 | MFI reversion | reversion | 82.17 | -17.83 | 154 | 17.5 | -87.77 | -34.69 | -87.92 | 2168 |
| 83 | ADX DI cross | trend | 81.48 | -18.52 | 167 | 6.6 | -89.35 | -47.86 | -89.50 | 2125 |
| 84 | Connors RSI(2) | reversion | 80.42 | -19.58 | 207 | 16.4 | -96.39 | -41.50 | -96.39 | 3654 |
| 85 | EMA 9/21 cross | trend | 79.08 | -20.92 | 227 | 15.0 | -97.37 | -42.33 | -97.43 | 3547 |
| 86 | Consensus | meta | 78.96 | -21.04 | 163 | 7.4 | -94.73 | -30.43 | -94.74 | 2666 |
| 87 | Candlestick reversal | reversion | 78.53 | -21.47 | 205 | 14.1 | -99.35 | -53.05 | -99.36 | 5564 |
| 88 | Stochastic reversion | reversion | 78.17 | -21.83 | 262 | 22.9 | -95.91 | -48.83 | -95.92 | 4052 |
| 89 | OBV trend | momentum | 78.15 | -21.85 | 228 | 13.6 | -95.74 | -49.91 | -95.85 | 3561 |
| 90 | Bollinger reversion | reversion | 76.89 | -23.11 | 249 | 12.4 | -95.76 | -46.80 | -95.76 | 3674 |
| 91 | VWAP momentum | momentum | 75.74 | -24.26 | 301 | 9.0 | -98.46 | -37.13 | -98.48 | 5214 |
| 92 | CCI reversion | reversion | 75.08 | -24.92 | 181 | 5.5 | -98.45 | -53.07 | -98.45 | 4700 |
| 93 | Parabolic SAR | trend | 74.64 | -25.36 | 249 | 13.3 | -96.93 | -57.89 | -96.99 | 3662 |
| 94 | MACD cross | trend | 73.86 | -26.14 | 202 | 10.9 | -99.70 | -68.00 | -99.70 | 6100 |
| 95 | Williams %R | reversion | 73.75 | -26.25 | 261 | 19.2 | -99.52 | -63.12 | -99.52 | 6092 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.64 | -99.89 | 8334 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T10:10 | CCI reversion | sell | ETH-USD | 18.77 | -0.03 | exit signal |
| 2026-09-29T10:10 | Candlestick reversal | sell | ETH-USD | 19.60 | -0.01 | take-profit |
| 2026-09-29T10:10 | Parabolic SAR | buy | ETH-USD | 3.72 | — | rebalance up |
| 2026-09-29T10:10 | Parabolic SAR | sell | SOL-USD | 3.72 | -0.01 | rebalance down |
| 2026-09-29T10:10 | Triple EMA stack | buy | ETH-USD | 4.12 | — | rebalance up |
| 2026-09-29T10:10 | Triple EMA stack | sell | SOL-USD | 4.12 | -0.01 | rebalance down |
| 2026-09-29T10:10 | EMA 9/21 cross | buy | ETH-USD | 3.94 | — | rebalance up |
| 2026-09-29T10:10 | EMA 9/21 cross | sell | SOL-USD | 3.94 | -0.01 | rebalance down |
| 2026-09-29T10:05 | Ichimoku | buy | BTC-USD | 21.83 | — | entry signal |
| 2026-09-29T10:05 | Parabolic SAR | buy | ETH-USD | 3.72 | — | rebalance up |
| 2026-09-29T10:05 | Parabolic SAR | sell | BTC-USD | 3.72 | -0.01 | rebalance down |
| 2026-09-29T10:00 | Consensus | sell | SOL-USD | 19.64 | -0.12 | target is flat |
| 2026-09-29T10:00 | CCI reversion · 1h | sell | XRP-USD | 2.15 | 0.02 | exit signal |
| 2026-09-29T10:00 | CCI reversion · 1h | sell | SOL-USD | 5.25 | 0.07 | exit signal |
| 2026-09-29T10:00 | RSI(14) reversion · 1h | sell | SOL-USD | 24.99 | 0.03 | exit signal |
| 2026-09-29T10:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 23.96 | — | entry signal |
| 2026-09-29T10:00 | RSI momentum · 1h | buy | BTC-USD | 24.13 | — | entry signal |
| 2026-09-29T10:00 | MACD zero-line · 1h | buy | DOGE-USD | 24.15 | — | entry signal |
| 2026-09-29T09:55 | Consensus | buy | SOL-USD | 19.76 | — | entry |
| 2026-09-29T09:55 | Candlestick reversal | sell | BTC-USD | 19.60 | -0.04 | take-profit |
| 2026-09-29T09:55 | Volume breakout | buy | DOGE-USD | 22.12 | — | entry signal |
| 2026-09-29T09:55 | Keltner breakout | buy | DOGE-USD | 21.82 | — | entry signal |
| 2026-09-29T09:55 | ROC + volume | buy | SOL-USD | 22.28 | — | entry signal |
| 2026-09-29T09:55 | ROC + volume | buy | DOGE-USD | 22.28 | — | entry signal |
| 2026-09-29T09:55 | Ichimoku | buy | XRP-USD | 21.89 | — | entry signal |
| 2026-09-29T09:55 | Ichimoku | buy | SOL-USD | 21.89 | — | entry signal |
| 2026-09-29T09:55 | Supertrend | buy | ETH-USD | 8.14 | — | entry signal |
| 2026-09-29T09:52 | OBV trend | buy | XRP-USD | 3.90 | — | rebalance up |
| 2026-09-29T09:52 | OBV trend | sell | ETH-USD | 3.90 | 0.00 | rebalance down |
| 2026-09-29T09:52 | RSI momentum | buy | XRP-USD | 4.13 | — | rebalance up |
| 2026-09-29T09:52 | RSI momentum | sell | SOL-USD | 4.13 | -0.01 | rebalance down |
| 2026-09-29T09:50 | MFI reversion | sell | XRP-USD | 20.55 | 0.02 | exit signal |
| 2026-09-29T09:50 | CCI reversion | sell | XRP-USD | 18.79 | -0.00 | exit signal |
| 2026-09-29T09:50 | CCI reversion | sell | BTC-USD | 18.74 | -0.03 | exit signal |
| 2026-09-29T09:50 | Williams %R | sell | ETH-USD | 18.43 | -0.05 | exit signal |
| 2026-09-29T09:50 | Stochastic reversion | sell | ETH-USD | 19.53 | -0.05 | exit signal |
| 2026-09-29T09:50 | Candlestick reversal | sell | XRP-USD | 19.65 | 0.04 | take-profit |
| 2026-09-29T09:50 | Squeeze breakout | buy | DOGE-USD | 22.35 | — | entry signal |
| 2026-09-29T09:50 | Keltner breakout | buy | BTC-USD | 21.84 | — | entry signal |
| 2026-09-29T09:50 | Bollinger breakout | buy | SOL-USD | 20.65 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
