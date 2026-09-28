# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T20:10:05.000159+00:00 · 4897 ticks

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

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.08 · VIX 16.19 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 27204 decisions in 1093 calls, $0.3207 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T20:10 | 2 / 3 / 0 | DOGE-USD 15% |  |
| Breezy | 2026-09-28T20:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-28T20:10 | 4 / 1 / 0 | SOL-USD 34%, ETH-USD 32% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.63 | +2.51% | 11 |
| Stochastic reversion | COIN | 2.50 | +5.60% | 9 |
| Williams %R | ETHU | 2.33 | +8.38% | 17 |
| CCI reversion | AMD | 2.17 | +3.10% | 10 |
| Bollinger reversion | PLTR | 2.11 | +1.89% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.36 | 1.36 | 1 | 100.0 | 12.70 | 2.79 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.11 | -1.49 | 19 |
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.41 | 1.26 | -2.47 | 92 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.63 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.40 | -12.40 | 25 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.34 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -5.02 | -9.84 | 203 |
| 10 | Hold BTC | benchmark | 99.70 | -0.30 | 0 | — | 30.47 | 3.90 | -8.68 | 1 |
| 11 | RSI(14) reversion · 1h | reversion | 99.63 | -0.37 | 2 | 100.0 | 15.03 | 3.18 | -6.57 | 136 |
| 12 | Copy: Congress Democrats (NANC) | copy | 99.63 | -0.37 | 0 | — | 8.08 | 3.11 | -3.62 | 1 |
| 13 | Copy: Warren Buffett (BRK-B) | copy | 99.58 | -0.42 | 0 | — | -1.21 | -0.45 | -7.65 | 1 |
| 14 | Hold SPY | benchmark | 99.40 | -0.60 | 0 | — | 4.05 | 2.11 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.16 | -0.84 | 0 | — | -1.67 | -0.78 | -5.14 | 1 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.79 | -5.16 | 28 |
| 19 | Daily: Bullish score | daily | 99.11 | -0.89 | 2 | 0.0 | -0.95 | 0.07 | -12.76 | 13 |
| 20 | Connors RSI(2) · 1h | reversion | 99.02 | -0.98 | 39 | 48.7 | -11.89 | -3.80 | -13.40 | 237 |
| 21 | Timing: Nasdaq FTD · QQQ | daily | 98.96 | -1.04 | 0 | — | -3.63 | -2.25 | -5.09 | 2 |
| 22 | Daily: SMA 20/50 cross · AAPL | daily | 98.95 | -1.05 | 0 | — | -7.89 | -1.95 | -12.73 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 98.79 | -1.21 | 23 | 56.5 | -12.39 | -2.76 | -14.07 | 324 |
| 24 | Z-score reversion · 1h | reversion | 98.75 | -1.25 | 4 | 25.0 | 3.56 | 0.90 | -8.60 | 155 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | Williams %R · 1h | reversion | 98.63 | -1.37 | 29 | 51.7 | -18.36 | -3.41 | -20.33 | 488 |
| 27 | CCI reversion · 1h | reversion | 98.51 | -1.49 | 23 | 34.8 | 0.08 | 0.18 | -12.41 | 412 |
| 28 | Copy: Insider buying | copy | 98.45 | -1.54 | 2 | 100.0 | -12.70 | -2.46 | -17.74 | 73 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -8.05 | -2.85 | -11.75 | 232 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.02 | -2.61 | -13.54 | 562 |
| 32 | Squeeze breakout · 1h | breakout | 97.99 | -2.00 | 7 | 14.3 | 15.68 | 2.78 | -6.26 | 95 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 97.94 | -2.06 | 0 | — | 25.06 | 3.64 | -6.29 | 1 |
| 34 | Candlestick reversal · 1h | reversion | 97.86 | -2.14 | 12 | 16.7 | -25.59 | -6.01 | -26.38 | 487 |
| 35 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 8 | 12.5 | 15.67 | 1.89 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.74 | -2.26 | 11 | 9.1 | 4.13 | 0.76 | -16.43 | 196 |
| 37 | MACD cross · 1h | trend | 97.58 | -2.42 | 27 | 11.1 | -15.47 | -2.62 | -20.93 | 456 |
| 38 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.77 | -16.14 | 692 |
| 39 | Bollinger reversion · 1h | reversion | 97.21 | -2.79 | 19 | 31.6 | -17.49 | -4.89 | -17.85 | 309 |
| 40 | Donchian 55/20 · 1h | breakout | 97.14 | -2.86 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.02 | -2.98 | 0 | — | -11.60 | -2.43 | -15.27 | 2 |
| 42 | Trend pullback · 1h | trend | 96.96 | -3.04 | 22 | 13.6 | -26.48 | -7.10 | -27.11 | 151 |
| 43 | Parabolic SAR · 1h | trend | 96.95 | -3.05 | 19 | 15.8 | -6.05 | -0.71 | -18.82 | 303 |
| 44 | Agent (ML meta-label) | meta | 96.95 | -3.05 | 79 | 10.1 | 5.49 | 1.15 | -10.81 | 391 |
| 45 | MACD zero-line · 1h | trend | 96.90 | -3.10 | 14 | 7.1 | -3.21 | -0.27 | -14.81 | 221 |
| 46 | Bollinger breakout · 1h | breakout | 96.71 | -3.29 | 13 | 7.7 | 13.20 | 1.89 | -9.85 | 284 |
| 47 | Three white soldiers | momentum | 96.49 | -3.51 | 30 | 13.3 | -51.75 | -28.63 | -51.77 | 621 |
| 48 | RSI momentum · 1h | momentum | 96.39 | -3.60 | 20 | 5.0 | 1.08 | 0.35 | -15.29 | 213 |
| 49 | EMA 9/21 cross · 1h | trend | 96.00 | -4.00 | 33 | 12.1 | 2.63 | 0.56 | -16.92 | 313 |
| 50 | Max aggression: 5-day momentum | meta | 95.93 | -4.07 | 1 | 0.0 | -0.40 | 0.32 | -29.56 | 29 |
| 51 | Triple EMA stack · 1h | trend | 95.91 | -4.09 | 24 | 8.3 | -3.33 | -0.19 | -22.95 | 226 |
| 52 | Ichimoku · 1h | trend | 95.87 | -4.13 | 11 | 9.1 | 8.16 | 1.15 | -15.13 | 119 |
| 53 | ADX DI cross · 1h | trend | 95.86 | -4.14 | 24 | 8.3 | -11.98 | -2.28 | -15.77 | 251 |
| 54 | Donchian 20/10 · 1h | breakout | 95.74 | -4.26 | 12 | 16.7 | 12.05 | 1.71 | -12.78 | 213 |
| 55 | MFI reversion · 1h | reversion | 95.55 | -4.45 | 38 | 13.2 | -9.79 | -1.82 | -17.20 | 126 |
| 56 | Max aggression: 1-day momentum | meta | 95.45 | -4.55 | 1 | 0.0 | -32.05 | -1.81 | -49.41 | 42 |
| 57 | OBV trend · 1h | momentum | 95.38 | -4.62 | 47 | 6.4 | -10.68 | -1.15 | -25.24 | 322 |
| 58 | VWAP momentum · 1h | momentum | 95.18 | -4.82 | 80 | 6.2 | -33.24 | -4.98 | -33.84 | 1249 |
| 59 | Volume breakout · 1h | breakout | 95.14 | -4.86 | 25 | 4.0 | 6.26 | 1.06 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.09 | -4.91 | 7 | 0.0 | -0.48 | 0.15 | -18.68 | 221 |
| 61 | Heikin-Ashi · 1h | trend | 94.25 | -5.75 | 35 | 11.4 | -22.67 | -3.41 | -29.29 | 678 |
| 62 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 63 | AI bee: Bizzy ⏸ | ai | 93.85 | -6.15 | 171 | 15.8 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 93.04 | -6.96 | 81 | 34.6 | -70.93 | -21.89 | -71.30 | 1473 |
| 65 | ROC + volume · 1h | momentum | 91.89 | -8.11 | 43 | 7.0 | -4.01 | -0.36 | -17.39 | 403 |
| 66 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.84 | -18.92 | -59.92 | 1179 |
| 67 | ROC + volume | momentum | 89.60 | -10.40 | 112 | 17.0 | -72.16 | -18.14 | -72.30 | 1658 |
| 68 | Volume breakout | breakout | 88.86 | -11.14 | 75 | 9.3 | -62.55 | -20.79 | -62.55 | 908 |
| 69 | Donchian 55/20 | breakout | 88.82 | -11.18 | 76 | 11.8 | -68.81 | -16.09 | -68.81 | 1332 |
| 70 | EMA 20/50 cross | trend | 88.82 | -11.18 | 89 | 14.6 | -79.07 | -17.90 | -79.07 | 1487 |
| 71 | Keltner breakout | breakout | 87.98 | -12.02 | 117 | 10.3 | -85.10 | -36.19 | -85.10 | 1934 |
| 72 | Ichimoku | trend | 87.87 | -12.13 | 84 | 8.3 | -80.53 | -26.87 | -80.53 | 1758 |
| 73 | Z-score reversion | reversion | 86.96 | -13.04 | 138 | 29.0 | -84.58 | -28.96 | -84.76 | 2085 |
| 74 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -70.80 | -17.14 | -71.87 | 1412 |
| 75 | MACD zero-line | trend | 85.67 | -14.33 | 148 | 16.2 | -91.56 | -37.17 | -91.58 | 2367 |
| 76 | Supertrend | trend | 85.35 | -14.65 | 135 | 16.3 | -87.40 | -25.45 | -87.42 | 1966 |
| 77 | Bollinger breakout | breakout | 85.16 | -14.84 | 152 | 15.1 | -93.93 | -43.49 | -93.93 | 2874 |
| 78 | RSI momentum | momentum | 84.81 | -15.19 | 140 | 11.4 | -90.41 | -30.49 | -90.41 | 2399 |
| 79 | Donchian 20/10 | breakout | 84.45 | -15.55 | 151 | 15.9 | -90.92 | -30.58 | -90.92 | 2686 |
| 80 | Triple EMA stack | trend | 84.05 | -15.95 | 163 | 14.1 | -93.08 | -37.61 | -93.08 | 2629 |
| 81 | Trend pullback | trend | 83.54 | -16.46 | 138 | 15.9 | -90.51 | -34.67 | -90.53 | 2280 |
| 82 | ADX DI cross | trend | 83.19 | -16.82 | 152 | 7.2 | -89.44 | -50.27 | -89.44 | 2130 |
| 83 | MFI reversion | reversion | 82.85 | -17.15 | 144 | 16.0 | -87.83 | -36.65 | -87.86 | 2174 |
| 84 | Connors RSI(2) | reversion | 82.61 | -17.39 | 191 | 17.8 | -96.38 | -43.34 | -96.38 | 3647 |
| 85 | Stochastic reversion | reversion | 81.43 | -18.57 | 238 | 24.8 | -95.88 | -49.95 | -95.90 | 4058 |
| 86 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.35 | -55.37 | -99.35 | 5554 |
| 87 | EMA 9/21 cross | trend | 80.46 | -19.54 | 212 | 14.2 | -97.41 | -44.28 | -97.41 | 3548 |
| 88 | OBV trend | momentum | 79.80 | -20.20 | 212 | 13.2 | -95.81 | -52.40 | -95.81 | 3559 |
| 89 | Consensus | meta | 79.58 | -20.42 | 155 | 7.1 | -94.91 | -32.12 | -94.91 | 2678 |
| 90 | Bollinger reversion ⏸ | reversion | 79.09 | -20.91 | 233 | 13.3 | -95.73 | -47.84 | -95.74 | 3677 |
| 91 | VWAP momentum ⏸ | momentum | 78.10 | -21.90 | 277 | 9.7 | -98.48 | -37.38 | -98.48 | 5211 |
| 92 | Parabolic SAR | trend | 77.42 | -22.58 | 224 | 12.5 | -96.94 | -61.65 | -96.95 | 3654 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.47 | -55.86 | -98.47 | 4703 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -74.77 | -99.70 | 6088 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.52 | -67.36 | -99.52 | 6087 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.88 | -105.69 | -99.88 | 8314 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T20:00 | Candlestick reversal · 1h | sell | XRP-USD | 10.80 | -0.26 | exit signal |
| 2026-09-28T20:00 | Candlestick reversal · 1h | sell | SOL-USD | 7.49 | -0.14 | exit signal |
| 2026-09-28T20:00 | VWAP momentum · 1h | buy | ETH-USD | 12.69 | — | rebalance up |
| 2026-09-28T20:00 | VWAP momentum · 1h | sell | XRP-USD | 3.12 | -0.08 | exit signal |
| 2026-09-28T20:00 | VWAP momentum · 1h | sell | SOL-USD | 6.29 | -0.12 | exit signal |
| 2026-09-28T20:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.26 | -0.14 | exit signal |
| 2026-09-28T20:00 | VWAP momentum · 1h | sell | BTC-USD | 7.32 | -0.07 | exit signal |
| 2026-09-28T20:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 23.49 | -0.35 | exit signal |
| 2026-09-28T20:00 | Heikin-Ashi · 1h | sell | BTC-USD | 23.57 | -0.25 | exit signal |
| 2026-09-28T20:00 | ADX DI cross · 1h | buy | ETH-USD | 4.84 | — | rebalance up |
| 2026-09-28T20:00 | ADX DI cross · 1h | sell | XRP-USD | 18.86 | -0.33 | exit signal |
| 2026-09-28T20:00 | ADX DI cross · 1h | sell | BTC-USD | 14.37 | -0.17 | exit signal |
| 2026-09-28T20:00 | RSI(14) reversion | buy | XRP-USD | 4.66 | — | rebalance up |
| 2026-09-28T19:55 | Agent (rotation) | sell | SQQQ | 33.12 | 0.25 | selected signal exited |
| 2026-09-28T19:55 | Day trade: Stocks in Play ORB | sell | SQQQ | 25.27 | 0.25 | target is flat |
| 2026-09-28T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 100.24 | 0.24 | target is flat |
| 2026-09-28T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 100.47 | 0.47 | target is flat |
| 2026-09-28T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 101.36 | 1.36 | target is flat |
| 2026-09-28T19:55 | Agent (aggressive) | sell | COIN | 49.91 | -0.37 | selected signal exited |
| 2026-09-28T19:55 | Agent | sell | COIN | 19.84 | -0.15 | selected signal exited |
| 2026-09-28T19:55 | MFI reversion | sell | SOXL | 20.78 | -0.09 | end-of-day flatten |
| 2026-09-28T19:55 | MFI reversion | sell | META | 20.68 | -0.25 | end-of-day flatten |
| 2026-09-28T19:55 | MFI reversion | sell | AMZN | 20.73 | -0.03 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | buy | XRP-USD | 18.96 | — | rebalance up |
| 2026-09-28T19:55 | Stochastic reversion | buy | DOGE-USD | 20.37 | — | entry signal |
| 2026-09-28T19:55 | Stochastic reversion | buy | BTC-USD | 14.94 | — | rebalance up |
| 2026-09-28T19:55 | Stochastic reversion | sell | UPRO | 5.53 | -0.01 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | TSLA | 6.84 | -0.01 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | TQQQ | 5.82 | -0.01 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | TNA | 5.80 | -0.03 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | SPY | 5.83 | -0.01 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | QQQ | 5.83 | -0.01 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | MSFT | 6.84 | -0.01 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | META | 6.81 | -0.04 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | IWM | 5.82 | -0.01 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | GOOGL | 5.84 | 0.00 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | COIN | 6.82 | -0.05 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | AMZN | 2.93 | -0.00 | end-of-day flatten |
| 2026-09-28T19:55 | Stochastic reversion | sell | AAPL | 3.90 | -0.00 | end-of-day flatten |
| 2026-09-28T19:55 | Z-score reversion | buy | XRP-USD | 8.64 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
