# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T05:40:05.000149+00:00 · 5355 ticks

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

Today: 4150 decisions in 830 calls, $0.0582 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T05:40 | 5 / 0 / 0 | SOL-USD 19%, XRP-USD 17%, BTC-USD 14%, ETH-USD 14% |  |
| Breezy | 2026-09-29T05:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T05:40 | 5 / 0 / 0 | ETH-USD 38%, SOL-USD 36% |  |

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
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.81 | -0.19 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.80 | -0.20 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 12 | Hold SPY | benchmark | 99.59 | -0.41 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.42 | -0.58 | 2 | 100.0 | 14.53 | 3.05 | -6.57 | 136 |
| 14 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 15 | Hold BTC | benchmark | 99.34 | -0.66 | 0 | — | 28.67 | 3.62 | -8.68 | 1 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 17 | Daily: Bullish score | daily | 99.30 | -0.70 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 99.15 | -0.85 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 99.13 | -0.87 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 21 | Connors RSI(2) · 1h | reversion | 99.12 | -0.88 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 99.04 | -0.96 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 98.77 | -1.23 | 23 | 56.5 | -12.57 | -2.80 | -13.73 | 324 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 25 | Copy: Insider buying | copy | 98.62 | -1.38 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 26 | Williams %R · 1h | reversion | 98.53 | -1.47 | 30 | 50.0 | -17.80 | -3.26 | -19.78 | 490 |
| 27 | Z-score reversion · 1h | reversion | 98.48 | -1.52 | 4 | 25.0 | 3.16 | 0.81 | -8.60 | 155 |
| 28 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.15 | -2.52 | -11.75 | 234 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 30 | CCI reversion · 1h | reversion | 98.35 | -1.66 | 24 | 33.3 | 1.30 | 0.38 | -12.41 | 405 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.14 | -1.86 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.04 | -1.96 | 7 | 14.3 | 16.37 | 2.87 | -6.26 | 93 |
| 34 | Candlestick reversal · 1h | reversion | 98.01 | -1.99 | 12 | 16.7 | -25.78 | -6.08 | -25.98 | 489 |
| 35 | EMA 20/50 cross · 1h | trend | 97.94 | -2.06 | 8 | 12.5 | 15.73 | 1.88 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.77 | -2.23 | 11 | 9.1 | 4.77 | 0.84 | -16.43 | 195 |
| 37 | Bollinger reversion · 1h | reversion | 97.38 | -2.62 | 19 | 31.6 | -17.66 | -4.91 | -17.74 | 306 |
| 38 | Donchian 55/20 · 1h | breakout | 97.27 | -2.73 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.20 | -2.80 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.14 | -2.86 | 79 | 10.1 | 6.30 | 1.25 | -11.14 | 380 |
| 42 | Trend pullback · 1h | trend | 97.12 | -2.88 | 22 | 13.6 | -25.74 | -6.83 | -26.36 | 148 |
| 43 | Parabolic SAR · 1h | trend | 96.99 | -3.01 | 20 | 15.0 | -5.60 | -0.64 | -18.82 | 300 |
| 44 | Bollinger breakout · 1h | breakout | 96.91 | -3.09 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 45 | MACD cross · 1h | trend | 96.84 | -3.17 | 31 | 9.7 | -16.34 | -2.77 | -20.52 | 455 |
| 46 | MACD zero-line · 1h | trend | 96.55 | -3.45 | 15 | 6.7 | -3.46 | -0.30 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.48 | -3.52 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Triple EMA stack · 1h | trend | 96.04 | -3.96 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 49 | Ichimoku · 1h | trend | 95.97 | -4.03 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 50 | EMA 9/21 cross · 1h | trend | 95.94 | -4.06 | 34 | 11.8 | 3.07 | 0.61 | -16.92 | 311 |
| 51 | ADX DI cross · 1h | trend | 95.88 | -4.12 | 25 | 8.0 | -11.54 | -2.16 | -15.39 | 248 |
| 52 | Donchian 20/10 · 1h | breakout | 95.83 | -4.17 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 53 | Max aggression: 1-day momentum | meta | 95.63 | -4.37 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 54 | MFI reversion · 1h | reversion | 95.53 | -4.47 | 38 | 13.2 | -9.48 | -1.74 | -17.20 | 125 |
| 55 | OBV trend · 1h | momentum | 95.47 | -4.53 | 47 | 6.4 | -9.59 | -1.00 | -25.24 | 317 |
| 56 | Volume breakout · 1h | breakout | 95.18 | -4.82 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 57 | Keltner breakout · 1h | breakout | 95.13 | -4.87 | 7 | 0.0 | -0.48 | 0.14 | -18.68 | 221 |
| 58 | Three white soldiers | momentum | 95.13 | -4.87 | 37 | 10.8 | -52.09 | -28.95 | -52.09 | 622 |
| 59 | VWAP momentum · 1h | momentum | 95.03 | -4.97 | 82 | 7.3 | -32.67 | -4.85 | -34.04 | 1248 |
| 60 | Max aggression: 5-day momentum | meta | 94.86 | -5.14 | 1 | 0.0 | -1.68 | 0.21 | -29.56 | 29 |
| 61 | Heikin-Ashi · 1h | trend | 94.33 | -5.67 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | ROC + volume · 1h | momentum | 91.92 | -8.08 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.17 | -21.95 | -71.26 | 1473 |
| 64 | Squeeze breakout | breakout | 89.38 | -10.62 | 71 | 5.6 | -60.23 | -18.96 | -60.38 | 1183 |
| 65 | ROC + volume | momentum | 89.31 | -10.69 | 115 | 16.5 | -71.76 | -17.77 | -72.35 | 1651 |
| 66 | Volume breakout | breakout | 88.63 | -11.37 | 76 | 9.2 | -62.37 | -20.45 | -62.40 | 905 |
| 67 | Donchian 55/20 | breakout | 88.55 | -11.45 | 77 | 11.7 | -68.44 | -15.90 | -68.44 | 1325 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.28 | -26.04 | -80.28 | 1750 |
| 71 | Keltner breakout | breakout | 87.49 | -12.51 | 120 | 10.0 | -84.91 | -35.00 | -84.93 | 1926 |
| 72 | EMA 20/50 cross | trend | 86.94 | -13.06 | 97 | 13.4 | -79.15 | -17.97 | -79.29 | 1487 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.73 | -28.59 | -84.80 | 2089 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -71.14 | -17.44 | -71.75 | 1418 |
| 75 | MACD zero-line | trend | 83.80 | -16.20 | 159 | 15.1 | -91.62 | -36.45 | -91.77 | 2367 |
| 76 | Supertrend | trend | 83.30 | -16.70 | 143 | 15.4 | -87.44 | -25.09 | -87.53 | 1963 |
| 77 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.50 | -33.62 | -90.50 | 2280 |
| 78 | Bollinger breakout | breakout | 82.63 | -17.37 | 165 | 13.9 | -94.03 | -43.05 | -94.05 | 2877 |
| 79 | RSI momentum | momentum | 82.36 | -17.64 | 153 | 10.5 | -90.49 | -30.46 | -90.60 | 2400 |
| 80 | MFI reversion | reversion | 82.11 | -17.89 | 152 | 16.4 | -87.81 | -34.96 | -87.92 | 2169 |
| 81 | Donchian 20/10 | breakout | 82.08 | -17.92 | 162 | 14.8 | -91.06 | -30.64 | -91.07 | 2690 |
| 82 | Triple EMA stack | trend | 81.93 | -18.07 | 173 | 13.3 | -93.07 | -37.63 | -93.07 | 2626 |
| 83 | ADX DI cross | trend | 81.43 | -18.57 | 167 | 6.6 | -89.46 | -48.89 | -89.49 | 2130 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.36 | -40.96 | -96.36 | 3648 |
| 85 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.72 | -30.35 | -94.72 | 2659 |
| 86 | Candlestick reversal | reversion | 78.71 | -21.29 | 200 | 14.0 | -99.36 | -53.21 | -99.36 | 5570 |
| 87 | Stochastic reversion | reversion | 78.43 | -21.57 | 258 | 23.3 | -95.94 | -49.07 | -95.95 | 4057 |
| 88 | EMA 9/21 cross | trend | 78.31 | -21.69 | 223 | 13.5 | -97.42 | -43.31 | -97.43 | 3548 |
| 89 | OBV trend | momentum | 77.38 | -22.62 | 225 | 12.4 | -95.87 | -51.78 | -95.87 | 3562 |
| 90 | Bollinger reversion | reversion | 77.10 | -22.90 | 243 | 12.8 | -95.81 | -46.98 | -95.81 | 3681 |
| 91 | CCI reversion | reversion | 75.54 | -24.46 | 171 | 5.8 | -98.47 | -53.34 | -98.47 | 4701 |
| 92 | Parabolic SAR | trend | 75.34 | -24.66 | 237 | 11.8 | -96.95 | -58.75 | -96.95 | 3651 |
| 93 | VWAP momentum | momentum | 74.89 | -25.11 | 301 | 9.0 | -98.51 | -37.57 | -98.51 | 5221 |
| 94 | MACD cross | trend | 73.93 | -26.07 | 195 | 8.7 | -99.71 | -69.40 | -99.71 | 6096 |
| 95 | Williams %R | reversion | 73.89 | -26.11 | 251 | 19.5 | -99.53 | -63.77 | -99.53 | 6097 |
| 96 | Heikin-Ashi | trend | 72.18 | -27.82 | 215 | 3.3 | -99.89 | -92.54 | -99.89 | 8323 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T05:40 | Williams %R | buy | XRP-USD | 14.82 | — | entry signal |
| 2026-09-29T05:40 | Williams %R | buy | SOL-USD | 14.82 | — | entry signal |
| 2026-09-29T05:40 | Williams %R | buy | ETH-USD | 14.82 | — | entry signal |
| 2026-09-29T05:40 | Williams %R | buy | DOGE-USD | 14.82 | — | entry signal |
| 2026-09-29T05:40 | Williams %R | buy | BTC-USD | 14.82 | — | entry signal |
| 2026-09-29T05:40 | Bollinger reversion | buy | XRP-USD | 19.32 | — | entry signal |
| 2026-09-29T05:40 | Bollinger reversion | buy | SOL-USD | 19.32 | — | entry signal |
| 2026-09-29T05:40 | Bollinger reversion | buy | ETH-USD | 19.32 | — | entry signal |
| 2026-09-29T05:40 | MACD cross | sell | DOGE-USD | 18.50 | -0.16 | exit signal |
| 2026-09-29T05:40 | Triple EMA stack | sell | XRP-USD | 20.51 | -0.18 | exit signal |
| 2026-09-29T05:40 | EMA 9/21 cross | sell | ETH-USD | 15.65 | -0.12 | exit signal |
| 2026-09-29T05:35 | Three white soldiers | sell | SOL-USD | 23.60 | -0.32 | stop-loss |
| 2026-09-29T05:35 | Three white soldiers | sell | BTC-USD | 23.69 | -0.24 | stop-loss |
| 2026-09-29T05:35 | Candlestick reversal | sell | XRP-USD | 19.52 | -0.22 | stop-loss |
| 2026-09-29T05:35 | Squeeze breakout | sell | DOGE-USD | 22.13 | -0.33 | stop-loss |
| 2026-09-29T05:35 | Squeeze breakout | sell | BTC-USD | 22.26 | -0.22 | stop-loss |
| 2026-09-29T05:35 | Bollinger breakout | sell | SOL-USD | 20.56 | -0.28 | stop-loss |
| 2026-09-29T05:35 | Bollinger breakout | sell | DOGE-USD | 20.54 | -0.30 | stop-loss |
| 2026-09-29T05:35 | Bollinger breakout | sell | BTC-USD | 20.65 | -0.20 | stop-loss |
| 2026-09-29T05:35 | Donchian 20/10 | sell | BTC-USD | 16.40 | -0.12 | exit signal |
| 2026-09-29T05:35 | OBV trend | sell | XRP-USD | 19.24 | -0.27 | stop-loss |
| 2026-09-29T05:35 | OBV trend | sell | SOL-USD | 19.30 | -0.22 | stop-loss |
| 2026-09-29T05:35 | OBV trend | sell | BTC-USD | 19.35 | -0.16 | stop-loss |
| 2026-09-29T05:35 | RSI momentum | sell | SOL-USD | 20.54 | -0.28 | stop-loss |
| 2026-09-29T05:35 | RSI momentum | sell | ETH-USD | 20.59 | -0.23 | stop-loss |
| 2026-09-29T05:35 | RSI momentum | sell | DOGE-USD | 20.53 | -0.30 | stop-loss |
| 2026-09-29T05:35 | RSI momentum | sell | BTC-USD | 16.65 | -0.14 | stop-loss |
| 2026-09-29T05:35 | VWAP momentum | sell | XRP-USD | 14.96 | -0.17 | exit signal |
| 2026-09-29T05:35 | VWAP momentum | sell | SOL-USD | 14.99 | -0.13 | exit signal |
| 2026-09-29T05:35 | VWAP momentum | sell | ETH-USD | 14.86 | -0.14 | stop-loss |
| 2026-09-29T05:35 | VWAP momentum | sell | DOGE-USD | 15.02 | -0.11 | exit signal |
| 2026-09-29T05:35 | VWAP momentum | sell | BTC-USD | 15.06 | -0.11 | exit signal |
| 2026-09-29T05:35 | Heikin-Ashi | sell | XRP-USD | 14.44 | -0.17 | stop-loss |
| 2026-09-29T05:35 | Heikin-Ashi | sell | SOL-USD | 14.37 | -0.18 | stop-loss |
| 2026-09-29T05:35 | Heikin-Ashi | sell | ETH-USD | 14.44 | -0.16 | stop-loss |
| 2026-09-29T05:35 | Heikin-Ashi | sell | DOGE-USD | 14.42 | -0.14 | exit signal |
| 2026-09-29T05:35 | Heikin-Ashi | sell | BTC-USD | 14.52 | -0.12 | stop-loss |
| 2026-09-29T05:35 | Parabolic SAR | sell | XRP-USD | 15.04 | -0.21 | stop-loss |
| 2026-09-29T05:35 | Parabolic SAR | sell | SOL-USD | 15.05 | -0.19 | stop-loss |
| 2026-09-29T05:35 | Parabolic SAR | sell | ETH-USD | 15.08 | -0.16 | stop-loss |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
