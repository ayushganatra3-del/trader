# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T15:11:05.000150+00:00 · 5827 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.24 (+0.24%)

Closed trades 19, win rate 73.7%, fees £0.56, max drawdown -1.39%.

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

Today: 17673 decisions in 2243 calls, $0.2294 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T15:11 | 4 / 13 / 12 | PLTR 14% |  |
| Breezy | 2026-09-29T15:11 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-09-29T15:11 | 6 / 21 / 2 | COIN 32%, XRP-USD 28% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| VWAP reversion | NVDA | 2.16 | +1.89% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.27 | 1.27 | 1 | 100.0 | 14.06 | 3.06 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 4 | Agent | meta | 100.24 | 0.24 | 19 | 73.7 | -9.11 | -5.77 | -10.53 | 205 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 6 | Copy: Congress Democrats (NANC) | copy | 100.10 | 0.10 | 0 | — | 7.89 | 2.99 | -3.62 | 1 |
| 7 | Hold BTC | benchmark | 100.03 | 0.03 | 0 | — | 30.51 | 3.83 | -8.68 | 1 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 10.25 | 1.95 | -7.93 | 7 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Max aggression: 5-day momentum | meta | 99.97 | -0.03 | 2 | 50.0 | -6.47 | -0.24 | -29.56 | 29 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.45 | 1.78 | -1.51 | 83 |
| 13 | Hold SPY | benchmark | 99.48 | -0.52 | 0 | — | 4.32 | 2.25 | -3.66 | 1 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 99.48 | -0.53 | 0 | — | -1.78 | -0.69 | -7.65 | 1 |
| 15 | Daily: Bullish score | daily | 99.46 | -0.54 | 2 | 0.0 | -0.83 | 0.08 | -12.76 | 13 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 99.42 | -0.58 | 0 | — | -3.44 | -2.11 | -5.09 | 2 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.36 | -0.64 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 18 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 19 | RSI(14) reversion · 1h | reversion | 99.23 | -0.77 | 7 | 57.1 | 4.36 | 1.26 | -6.57 | 125 |
| 20 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 21 | Williams %R · 1h | reversion | 99.01 | -0.99 | 34 | 52.9 | -17.19 | -3.14 | -19.41 | 484 |
| 22 | Gap and go | momentum | 98.78 | -1.22 | 8 | 12.5 | 15.81 | 3.92 | -4.73 | 195 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 98.77 | -1.23 | 0 | — | 26.93 | 3.86 | -6.29 | 1 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 25 | Candlestick reversal · 1h | reversion | 98.62 | -1.38 | 15 | 26.7 | -25.76 | -6.11 | -26.56 | 490 |
| 26 | EMA 20/50 cross · 1h | trend | 98.59 | -1.41 | 8 | 12.5 | 17.16 | 2.04 | -14.36 | 127 |
| 27 | Z-score reversion · 1h | reversion | 98.57 | -1.43 | 9 | 44.4 | 3.65 | 0.91 | -8.60 | 152 |
| 28 | CCI reversion · 1h | reversion | 98.44 | -1.56 | 32 | 37.5 | 2.76 | 0.63 | -12.41 | 406 |
| 29 | Copy: Insider buying | copy | 98.43 | -1.57 | 2 | 100.0 | -14.74 | -2.94 | -17.74 | 72 |
| 30 | Stochastic reversion · 1h | reversion | 98.37 | -1.62 | 26 | 53.8 | -14.64 | -3.24 | -15.72 | 321 |
| 31 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.46 | -0.04 | -15.21 | 47 |
| 32 | Agent (rotation) | meta | 98.03 | -1.97 | 30 | 13.3 | -5.80 | -1.98 | -11.89 | 223 |
| 33 | Opening range 30m | breakout | 97.99 | -2.01 | 31 | 12.9 | -8.18 | -2.35 | -13.54 | 559 |
| 34 | Connors RSI(2) · 1h | reversion | 97.91 | -2.09 | 41 | 46.3 | -12.86 | -4.08 | -13.23 | 236 |
| 35 | Timing: Nasdaq FTD · TQQQ | daily | 97.83 | -2.17 | 0 | — | -11.10 | -2.29 | -15.27 | 2 |
| 36 | Squeeze breakout · 1h | breakout | 97.78 | -2.22 | 8 | 12.5 | 15.80 | 2.78 | -6.17 | 96 |
| 37 | Supertrend · 1h | trend | 97.77 | -2.23 | 12 | 8.3 | 4.82 | 0.84 | -16.43 | 197 |
| 38 | Donchian 55/20 · 1h | breakout | 97.40 | -2.60 | 10 | 0.0 | 4.73 | 0.82 | -16.96 | 114 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 97.36 | -2.64 | 0 | — | -9.64 | -2.37 | -12.73 | 1 |
| 40 | Bollinger reversion · 1h | reversion | 97.26 | -2.74 | 20 | 30.0 | -17.94 | -4.99 | -17.94 | 306 |
| 41 | Trend pullback · 1h | trend | 97.14 | -2.86 | 24 | 12.5 | -28.42 | -6.91 | -29.59 | 148 |
| 42 | MACD cross · 1h | trend | 97.11 | -2.89 | 33 | 9.1 | -17.61 | -3.00 | -21.80 | 459 |
| 43 | Agent (ML meta-label) | meta | 97.01 | -2.99 | 93 | 11.8 | -0.00 | 0.15 | -13.25 | 395 |
| 44 | Parabolic SAR · 1h | trend | 96.78 | -3.22 | 21 | 14.3 | -6.77 | -0.82 | -18.82 | 292 |
| 45 | Ichimoku · 1h | trend | 96.69 | -3.31 | 12 | 16.7 | 7.89 | 1.11 | -15.13 | 121 |
| 46 | Opening range 15m | breakout | 96.61 | -3.39 | 40 | 12.5 | -10.04 | -2.72 | -16.14 | 692 |
| 47 | MACD zero-line · 1h | trend | 96.42 | -3.58 | 15 | 6.7 | -3.54 | -0.31 | -14.64 | 222 |
| 48 | Bollinger breakout · 1h | breakout | 95.99 | -4.00 | 15 | 6.7 | 10.56 | 1.55 | -10.43 | 287 |
| 49 | RSI momentum · 1h | momentum | 95.99 | -4.01 | 20 | 5.0 | 1.40 | 0.39 | -15.29 | 210 |
| 50 | Triple EMA stack · 1h | trend | 95.46 | -4.54 | 26 | 7.7 | -4.45 | -0.33 | -22.53 | 211 |
| 51 | VWAP momentum · 1h | momentum | 95.45 | -4.55 | 93 | 12.9 | -29.59 | -4.29 | -34.02 | 1237 |
| 52 | Donchian 20/10 · 1h | breakout | 95.41 | -4.59 | 12 | 16.7 | 9.02 | 1.34 | -12.78 | 216 |
| 53 | ADX DI cross · 1h | trend | 95.40 | -4.60 | 26 | 7.7 | -12.21 | -2.29 | -15.70 | 256 |
| 54 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -51.92 | -28.85 | -52.20 | 627 |
| 55 | Volume breakout · 1h | breakout | 95.14 | -4.86 | 25 | 4.0 | 7.74 | 1.24 | -12.60 | 128 |
| 56 | MFI reversion · 1h | reversion | 94.88 | -5.12 | 40 | 12.5 | -12.04 | -2.28 | -17.30 | 128 |
| 57 | EMA 9/21 cross · 1h | trend | 94.81 | -5.19 | 36 | 13.9 | -2.28 | -0.12 | -16.92 | 310 |
| 58 | Keltner breakout · 1h | breakout | 94.75 | -5.25 | 7 | 0.0 | -1.59 | 0.00 | -18.68 | 222 |
| 59 | OBV trend · 1h | momentum | 94.30 | -5.70 | 48 | 6.2 | -9.23 | -0.96 | -25.24 | 330 |
| 60 | Heikin-Ashi · 1h | trend | 93.69 | -6.32 | 39 | 12.8 | -21.87 | -3.24 | -29.76 | 677 |
| 61 | Max aggression: 1-day momentum | meta | 93.66 | -6.34 | 2 | 0.0 | -39.89 | -2.44 | -49.44 | 42 |
| 62 | RSI(14) reversion | reversion | 91.56 | -8.44 | 95 | 34.7 | -70.41 | -20.83 | -70.95 | 1485 |
| 63 | ROC + volume · 1h | momentum | 90.61 | -9.39 | 46 | 6.5 | -5.52 | -0.57 | -18.48 | 410 |
| 64 | Squeeze breakout | breakout | 89.93 | -10.07 | 78 | 9.0 | -60.18 | -18.91 | -60.85 | 1190 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | Donchian 55/20 | breakout | 88.27 | -11.73 | 87 | 14.9 | -67.64 | -15.54 | -67.64 | 1309 |
| 67 | EMA 20/50 cross | trend | 88.20 | -11.80 | 100 | 14.0 | -78.40 | -17.45 | -78.72 | 1476 |
| 68 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 69 | ROC + volume | momentum | 87.49 | -12.51 | 132 | 17.4 | -72.45 | -18.18 | -73.03 | 1671 |
| 70 | Volume breakout | breakout | 87.38 | -12.62 | 89 | 12.4 | -62.26 | -20.86 | -62.64 | 926 |
| 71 | Ichimoku | trend | 86.24 | -13.76 | 103 | 8.7 | -80.41 | -26.19 | -80.41 | 1764 |
| 72 | Keltner breakout | breakout | 85.71 | -14.29 | 137 | 11.7 | -85.02 | -35.61 | -85.26 | 1941 |
| 73 | Z-score reversion | reversion | 85.38 | -14.62 | 156 | 30.8 | -84.48 | -28.09 | -84.48 | 2090 |
| 74 | VWAP reversion | reversion | 84.94 | -15.06 | 113 | 17.7 | -71.12 | -17.19 | -71.83 | 1397 |
| 75 | Supertrend | trend | 83.32 | -16.68 | 154 | 16.2 | -87.43 | -25.04 | -87.56 | 1960 |
| 76 | MACD zero-line | trend | 83.13 | -16.88 | 170 | 14.7 | -91.68 | -36.69 | -91.70 | 2356 |
| 77 | MFI reversion | reversion | 82.32 | -17.68 | 157 | 17.8 | -87.51 | -33.53 | -87.82 | 2163 |
| 78 | Donchian 20/10 | breakout | 81.62 | -18.38 | 175 | 17.1 | -90.88 | -30.31 | -91.10 | 2690 |
| 79 | Triple EMA stack | trend | 81.24 | -18.75 | 187 | 15.0 | -92.89 | -36.56 | -92.89 | 2615 |
| 80 | RSI momentum | momentum | 81.13 | -18.87 | 167 | 12.0 | -90.40 | -29.84 | -90.40 | 2382 |
| 81 | Bollinger breakout | breakout | 81.13 | -18.87 | 183 | 14.8 | -93.99 | -42.28 | -94.13 | 2883 |
| 82 | Trend pullback | trend | 80.40 | -19.60 | 161 | 17.4 | -90.71 | -34.72 | -90.71 | 2296 |
| 83 | ADX DI cross | trend | 80.39 | -19.61 | 174 | 6.3 | -89.41 | -47.68 | -89.49 | 2103 |
| 84 | Connors RSI(2) | reversion | 78.68 | -21.32 | 223 | 15.7 | -96.40 | -42.57 | -96.40 | 3650 |
| 85 | Consensus | meta | 78.04 | -21.96 | 173 | 6.9 | -94.60 | -30.47 | -94.60 | 2656 |
| 86 | EMA 9/21 cross | trend | 77.96 | -22.04 | 243 | 15.2 | -97.38 | -42.66 | -97.45 | 3556 |
| 87 | Candlestick reversal | reversion | 77.37 | -22.63 | 229 | 14.0 | -99.33 | -51.11 | -99.34 | 5554 |
| 88 | Stochastic reversion | reversion | 77.20 | -22.80 | 277 | 22.7 | -95.90 | -48.19 | -95.93 | 4045 |
| 89 | OBV trend | momentum | 76.59 | -23.41 | 244 | 13.9 | -95.91 | -51.38 | -95.91 | 3563 |
| 90 | Bollinger reversion | reversion | 76.06 | -23.94 | 264 | 13.6 | -95.75 | -46.53 | -95.75 | 3672 |
| 91 | VWAP momentum | momentum | 75.45 | -24.55 | 327 | 9.2 | -98.42 | -36.50 | -98.46 | 5232 |
| 92 | CCI reversion | reversion | 74.35 | -25.65 | 187 | 5.9 | -98.44 | -52.25 | -98.44 | 4680 |
| 93 | MACD cross | trend | 72.78 | -27.22 | 223 | 11.7 | -99.70 | -66.16 | -99.70 | 6091 |
| 94 | Williams %R | reversion | 72.74 | -27.27 | 283 | 19.4 | -99.51 | -60.31 | -99.52 | 6094 |
| 95 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -97.00 | -57.03 | -97.00 | 3648 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.60 | -99.89 | 8349 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T15:10 | Agent (ML meta-label) | sell | TNA | 4.34 | -0.20 | selected signal exited |
| 2026-09-29T15:10 | Agent (ML meta-label) | sell | MSTR | 4.03 | -0.03 | selected signal exited |
| 2026-09-29T15:10 | MFI reversion · 1h | buy | TSLA | 4.75 | — | rebalance up |
| 2026-09-29T15:10 | MFI reversion · 1h | buy | LABU | 5.04 | — | rebalance up |
| 2026-09-29T15:10 | MFI reversion · 1h | sell | TNA | 18.73 | -0.55 | stop-loss |
| 2026-09-29T15:10 | CCI reversion · 1h | sell | TNA | 8.77 | -0.24 | stop-loss |
| 2026-09-29T15:10 | CCI reversion · 1h | sell | IWM | 9.88 | -0.11 | stop-loss |
| 2026-09-29T15:10 | Squeeze breakout · 1h | sell | ETH-USD | 24.29 | -0.22 | stop-loss |
| 2026-09-29T15:10 | Bollinger breakout · 1h | buy | XRP-USD | 4.93 | — | rebalance up |
| 2026-09-29T15:10 | Bollinger breakout · 1h | buy | ETHU | 9.60 | — | rebalance up |
| 2026-09-29T15:10 | Bollinger breakout · 1h | sell | ETH-USD | 19.11 | -0.16 | stop-loss |
| 2026-09-29T15:10 | MFI reversion | sell | LABU | 4.33 | -0.00 | target is flat |
| 2026-09-29T15:10 | Williams %R | buy | XRP-USD | 6.61 | — | entry signal |
| 2026-09-29T15:10 | Williams %R | buy | SOL-USD | 6.62 | — | entry signal |
| 2026-09-29T15:10 | Williams %R | buy | ETH-USD | 6.62 | — | entry signal |
| 2026-09-29T15:10 | Williams %R | buy | DOGE-USD | 6.62 | — | entry signal |
| 2026-09-29T15:10 | Williams %R | sell | TSLA | 3.73 | -0.01 | rebalance down |
| 2026-09-29T15:10 | Williams %R | sell | SQQQ | 3.81 | 0.01 | rebalance down |
| 2026-09-29T15:10 | Williams %R | sell | PLTR | 3.78 | -0.01 | rebalance down |
| 2026-09-29T15:10 | Williams %R | sell | LABU | 3.80 | -0.01 | rebalance down |
| 2026-09-29T15:10 | Williams %R | sell | GOOGL | 3.80 | -0.00 | rebalance down |
| 2026-09-29T15:10 | Williams %R | sell | COIN | 3.77 | -0.03 | rebalance down |
| 2026-09-29T15:10 | Williams %R | sell | AAPL | 3.79 | -0.01 | rebalance down |
| 2026-09-29T15:10 | Stochastic reversion | buy | SOL-USD | 3.20 | — | entry signal |
| 2026-09-29T15:10 | Stochastic reversion | buy | MSTR | 5.94 | — | entry signal |
| 2026-09-29T15:10 | Stochastic reversion | buy | ETH-USD | 5.94 | — | entry signal |
| 2026-09-29T15:10 | VWAP reversion | buy | UPRO | 12.13 | — | entry signal |
| 2026-09-29T15:10 | VWAP reversion | buy | BITX | 12.14 | — | entry signal |
| 2026-09-29T15:10 | VWAP reversion | sell | MSTR | 4.86 | -0.04 | rebalance down |
| 2026-09-29T15:10 | VWAP reversion | sell | GOOGL | 4.88 | -0.01 | rebalance down |
| 2026-09-29T15:10 | VWAP reversion | sell | ETHU | 4.83 | -0.04 | rebalance down |
| 2026-09-29T15:10 | VWAP reversion | sell | COIN | 4.83 | -0.03 | rebalance down |
| 2026-09-29T15:10 | VWAP reversion | sell | AAPL | 4.87 | -0.01 | rebalance down |
| 2026-09-29T15:10 | Z-score reversion | buy | DOGE-USD | 8.54 | — | entry signal |
| 2026-09-29T15:10 | Z-score reversion | sell | SQQQ | 9.52 | 0.02 | exit signal |
| 2026-09-29T15:10 | Bollinger reversion | buy | DOGE-USD | 4.54 | — | entry signal |
| 2026-09-29T15:10 | Bollinger reversion | buy | BTC-USD | 9.51 | — | entry signal |
| 2026-09-29T15:10 | Bollinger reversion | sell | UPRO | 10.87 | -0.02 | stop-loss |
| 2026-09-29T15:10 | Candlestick reversal | buy | XRP-USD | 7.74 | — | entry signal |
| 2026-09-29T15:10 | Candlestick reversal | buy | SOL-USD | 7.75 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
