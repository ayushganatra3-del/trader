# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T05:10:05.000146+00:00 · 5333 ticks

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

Today: 3820 decisions in 764 calls, $0.0536 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T05:10 | 3 / 2 / 0 | SOL-USD 14%, BTC-USD 12% |  |
| Breezy | 2026-09-29T05:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T05:10 | 5 / 0 / 0 | BTC-USD 36%, ETH-USD 34% |  |

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
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.78 | -0.23 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.76 | -0.24 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 12 | Hold SPY | benchmark | 99.56 | -0.44 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.44 | -0.56 | 2 | 100.0 | 14.59 | 3.07 | -6.57 | 136 |
| 14 | Hold BTC | benchmark | 99.43 | -0.57 | 0 | — | 29.51 | 3.72 | -8.68 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.05 | -4.73 | 190 |
| 17 | Daily: Bullish score | daily | 99.27 | -0.73 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 99.12 | -0.88 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 99.10 | -0.90 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 21 | Connors RSI(2) · 1h | reversion | 99.10 | -0.90 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 99.01 | -0.99 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 98.77 | -1.23 | 23 | 56.5 | -12.66 | -2.81 | -13.85 | 324 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 25 | Copy: Insider buying | copy | 98.60 | -1.40 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 26 | Williams %R · 1h | reversion | 98.51 | -1.49 | 30 | 50.0 | -17.83 | -3.27 | -19.83 | 490 |
| 27 | Z-score reversion · 1h | reversion | 98.51 | -1.49 | 4 | 25.0 | 3.22 | 0.82 | -8.60 | 155 |
| 28 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.32 | -2.59 | -11.75 | 233 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 30 | CCI reversion · 1h | reversion | 98.35 | -1.65 | 24 | 33.3 | 1.31 | 0.39 | -12.41 | 405 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.11 | -1.89 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.03 | -1.97 | 7 | 14.3 | 15.68 | 2.76 | -6.26 | 95 |
| 34 | Candlestick reversal · 1h | reversion | 98.01 | -1.99 | 12 | 16.7 | -25.74 | -6.07 | -25.98 | 489 |
| 35 | EMA 20/50 cross · 1h | trend | 97.91 | -2.09 | 8 | 12.5 | 15.73 | 1.88 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.77 | -2.23 | 11 | 9.1 | 5.30 | 0.90 | -16.43 | 194 |
| 37 | Bollinger reversion · 1h | reversion | 97.35 | -2.65 | 19 | 31.6 | -17.67 | -4.91 | -17.76 | 306 |
| 38 | Donchian 55/20 · 1h | breakout | 97.25 | -2.75 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.74 | -16.14 | 692 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.17 | -2.83 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.11 | -2.89 | 79 | 10.1 | 4.65 | 0.98 | -10.88 | 385 |
| 42 | Trend pullback · 1h | trend | 97.09 | -2.91 | 22 | 13.6 | -25.74 | -6.83 | -26.36 | 148 |
| 43 | Parabolic SAR · 1h | trend | 96.97 | -3.03 | 20 | 15.0 | -5.60 | -0.64 | -18.82 | 300 |
| 44 | Bollinger breakout · 1h | breakout | 96.88 | -3.12 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 45 | MACD cross · 1h | trend | 96.85 | -3.15 | 31 | 9.7 | -16.31 | -2.76 | -20.52 | 455 |
| 46 | MACD zero-line · 1h | trend | 96.55 | -3.45 | 15 | 6.7 | -3.46 | -0.30 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.47 | -3.53 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Triple EMA stack · 1h | trend | 96.01 | -3.99 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 49 | Ichimoku · 1h | trend | 95.95 | -4.05 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 50 | EMA 9/21 cross · 1h | trend | 95.92 | -4.08 | 34 | 11.8 | 3.07 | 0.61 | -16.92 | 311 |
| 51 | ADX DI cross · 1h | trend | 95.87 | -4.13 | 25 | 8.0 | -11.67 | -2.19 | -15.39 | 249 |
| 52 | Donchian 20/10 · 1h | breakout | 95.81 | -4.19 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 53 | Three white soldiers | momentum | 95.69 | -4.31 | 35 | 11.4 | -51.90 | -28.55 | -51.90 | 621 |
| 54 | Max aggression: 1-day momentum | meta | 95.60 | -4.40 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | MFI reversion · 1h | reversion | 95.52 | -4.48 | 38 | 13.2 | -9.46 | -1.74 | -17.20 | 125 |
| 56 | OBV trend · 1h | momentum | 95.46 | -4.54 | 47 | 6.4 | -9.59 | -1.00 | -25.24 | 317 |
| 57 | Volume breakout · 1h | breakout | 95.17 | -4.83 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 58 | Keltner breakout · 1h | breakout | 95.12 | -4.88 | 7 | 0.0 | -0.52 | 0.14 | -18.68 | 221 |
| 59 | VWAP momentum · 1h | momentum | 95.03 | -4.97 | 82 | 7.3 | -32.68 | -4.85 | -34.01 | 1248 |
| 60 | Max aggression: 5-day momentum | meta | 94.94 | -5.06 | 1 | 0.0 | -1.58 | 0.22 | -29.56 | 29 |
| 61 | Heikin-Ashi · 1h | trend | 94.33 | -5.67 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | ROC + volume · 1h | momentum | 91.90 | -8.10 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.24 | -22.02 | -71.32 | 1474 |
| 64 | Squeeze breakout | breakout | 89.93 | -10.07 | 69 | 5.8 | -60.01 | -18.80 | -60.16 | 1181 |
| 65 | ROC + volume | momentum | 89.31 | -10.69 | 115 | 16.5 | -71.75 | -17.77 | -72.35 | 1651 |
| 66 | Volume breakout | breakout | 88.63 | -11.37 | 76 | 9.2 | -62.37 | -20.45 | -62.40 | 905 |
| 67 | Donchian 55/20 | breakout | 88.55 | -11.45 | 77 | 11.7 | -68.50 | -15.91 | -68.50 | 1326 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.42 | -26.17 | -80.42 | 1753 |
| 71 | Keltner breakout | breakout | 87.49 | -12.51 | 120 | 10.0 | -85.00 | -35.08 | -85.00 | 1928 |
| 72 | EMA 20/50 cross | trend | 87.36 | -12.64 | 95 | 13.7 | -79.05 | -17.90 | -79.17 | 1486 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.73 | -28.59 | -84.80 | 2089 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -71.25 | -17.48 | -71.87 | 1415 |
| 75 | MACD zero-line | trend | 83.90 | -16.10 | 158 | 15.2 | -91.60 | -36.33 | -91.76 | 2366 |
| 76 | Supertrend | trend | 83.75 | -16.25 | 142 | 15.5 | -87.31 | -24.95 | -87.41 | 1960 |
| 77 | Bollinger breakout | breakout | 83.41 | -16.59 | 162 | 14.2 | -93.99 | -42.57 | -94.01 | 2875 |
| 78 | RSI momentum | momentum | 83.26 | -16.74 | 149 | 10.7 | -90.42 | -30.22 | -90.51 | 2399 |
| 79 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.50 | -33.62 | -90.50 | 2280 |
| 80 | Triple EMA stack | trend | 82.65 | -17.35 | 170 | 13.5 | -93.02 | -37.26 | -93.02 | 2623 |
| 81 | Donchian 20/10 | breakout | 82.20 | -17.80 | 161 | 14.9 | -91.04 | -30.58 | -91.06 | 2690 |
| 82 | MFI reversion | reversion | 82.12 | -17.88 | 152 | 16.4 | -87.80 | -34.94 | -87.92 | 2169 |
| 83 | ADX DI cross | trend | 81.43 | -18.57 | 167 | 6.6 | -89.48 | -49.10 | -89.48 | 2131 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.36 | -40.96 | -96.36 | 3648 |
| 85 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.73 | -30.36 | -94.73 | 2660 |
| 86 | Candlestick reversal | reversion | 78.82 | -21.18 | 198 | 14.1 | -99.36 | -53.04 | -99.36 | 5565 |
| 87 | EMA 9/21 cross | trend | 78.56 | -21.44 | 221 | 13.6 | -97.41 | -43.03 | -97.42 | 3547 |
| 88 | Stochastic reversion | reversion | 78.43 | -21.57 | 258 | 23.3 | -95.94 | -49.07 | -95.95 | 4057 |
| 89 | OBV trend | momentum | 77.98 | -22.02 | 222 | 12.6 | -95.83 | -51.20 | -95.83 | 3560 |
| 90 | Bollinger reversion | reversion | 77.28 | -22.72 | 243 | 12.8 | -95.81 | -46.83 | -95.81 | 3678 |
| 91 | Parabolic SAR | trend | 76.13 | -23.87 | 232 | 12.1 | -96.92 | -57.87 | -96.92 | 3649 |
| 92 | CCI reversion | reversion | 75.50 | -24.50 | 169 | 5.9 | -98.47 | -53.37 | -98.47 | 4701 |
| 93 | VWAP momentum | momentum | 75.41 | -24.59 | 296 | 9.1 | -98.49 | -37.39 | -98.49 | 5215 |
| 94 | MACD cross | trend | 74.71 | -25.29 | 190 | 8.9 | -99.70 | -68.50 | -99.70 | 6094 |
| 95 | Williams %R | reversion | 74.10 | -25.90 | 247 | 19.8 | -99.53 | -63.47 | -99.53 | 6091 |
| 96 | Heikin-Ashi | trend | 72.78 | -27.22 | 210 | 3.3 | -99.89 | -91.75 | -99.89 | 8325 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T05:10 | OBV trend | buy | BTC-USD | 19.51 | — | entry signal |
| 2026-09-29T05:10 | VWAP momentum | buy | XRP-USD | 3.80 | — | rebalance up |
| 2026-09-29T05:10 | VWAP momentum | buy | SOL-USD | 3.78 | — | rebalance up |
| 2026-09-29T05:10 | VWAP momentum | sell | ETH-USD | 15.03 | -0.10 | exit signal |
| 2026-09-29T05:10 | Heikin-Ashi | buy | XRP-USD | 3.66 | — | rebalance up |
| 2026-09-29T05:10 | Heikin-Ashi | buy | DOGE-USD | 3.65 | — | rebalance up |
| 2026-09-29T05:10 | Heikin-Ashi | sell | SOL-USD | 14.54 | -0.10 | exit signal |
| 2026-09-29T05:10 | Heikin-Ashi | sell | ETH-USD | 14.53 | -0.10 | exit signal |
| 2026-09-29T05:10 | MACD cross | sell | ETH-USD | 18.58 | -0.12 | exit signal |
| 2026-09-29T05:10 | EMA 20/50 cross | buy | BTC-USD | 21.86 | — | entry signal |
| 2026-09-29T05:05 | OBV trend | buy | DOGE-USD | 19.53 | — | entry signal |
| 2026-09-29T05:05 | Heikin-Ashi | buy | XRP-USD | 14.63 | — | entry signal |
| 2026-09-29T05:05 | Heikin-Ashi | buy | SOL-USD | 14.63 | — | entry signal |
| 2026-09-29T05:05 | Heikin-Ashi | buy | ETH-USD | 14.63 | — | entry signal |
| 2026-09-29T05:05 | Heikin-Ashi | buy | DOGE-USD | 14.63 | — | entry signal |
| 2026-09-29T05:05 | Heikin-Ashi | buy | BTC-USD | 14.63 | — | entry signal |
| 2026-09-29T05:05 | Parabolic SAR | buy | DOGE-USD | 19.05 | — | entry signal |
| 2026-09-29T05:05 | EMA 20/50 cross | buy | DOGE-USD | 21.89 | — | entry signal |
| 2026-09-29T05:00 | CCI reversion · 1h | buy | SOL-USD | 5.18 | — | entry signal |
| 2026-09-29T05:00 | VWAP momentum · 1h | buy | BTC-USD | 19.02 | — | entry signal |
| 2026-09-29T05:00 | MACD cross | buy | ETH-USD | 18.71 | — | entry signal |
| 2026-09-29T05:00 | Triple EMA stack | buy | XRP-USD | 20.68 | — | entry signal |
| 2026-09-29T04:55 | CCI reversion | buy | XRP-USD | 18.91 | — | entry signal |
| 2026-09-29T04:55 | CCI reversion | buy | SOL-USD | 18.91 | — | entry signal |
| 2026-09-29T04:55 | Williams %R | buy | SOL-USD | 18.56 | — | entry signal |
| 2026-09-29T04:55 | Williams %R | buy | ETH-USD | 18.56 | — | entry signal |
| 2026-09-29T04:55 | Williams %R | buy | DOGE-USD | 18.56 | — | entry signal |
| 2026-09-29T04:55 | Candlestick reversal | buy | XRP-USD | 19.74 | — | entry signal |
| 2026-09-29T04:55 | Candlestick reversal | buy | SOL-USD | 19.74 | — | entry signal |
| 2026-09-29T04:55 | VWAP momentum | buy | XRP-USD | 15.12 | — | entry signal |
| 2026-09-29T04:55 | VWAP momentum | buy | SOL-USD | 15.13 | — | entry signal |
| 2026-09-29T04:55 | VWAP momentum | buy | ETH-USD | 15.13 | — | entry signal |
| 2026-09-29T04:55 | VWAP momentum | buy | DOGE-USD | 15.13 | — | entry signal |
| 2026-09-29T04:55 | VWAP momentum | sell | BTC-USD | 3.87 | -0.02 | rebalance down |
| 2026-09-29T04:50 | Squeeze breakout | sell | BTC-USD | 22.44 | -0.14 | exit signal |
| 2026-09-29T04:50 | Bollinger breakout | sell | DOGE-USD | 20.80 | -0.20 | stop-loss |
| 2026-09-29T04:50 | Bollinger breakout | sell | BTC-USD | 20.88 | -0.12 | exit signal |
| 2026-09-29T04:50 | Donchian 20/10 | buy | DOGE-USD | 4.11 | — | rebalance up |
| 2026-09-29T04:50 | Donchian 20/10 | sell | XRP-USD | 20.44 | -0.24 | exit signal |
| 2026-09-29T04:50 | Donchian 20/10 | sell | ETH-USD | 12.29 | -0.11 | stop-loss |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
