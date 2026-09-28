# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T15:10:05.000156+00:00 · 4650 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.39 (-0.61%)

Closed trades 11, win rate 63.6%, fees £0.39, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 19.90 | +0.07 |
| COIN | 19.80 | -0.13 |
| ETHU | 19.95 | -0.00 |

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

### Market regime (QQQ, 2026-09-25)

**Uptrend** since 2026-09-21 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 20.87 · VIX 14.87 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, COIN 8.0, MSFT 7.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 6082 decisions in 361 calls, $0.0732 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T15:10 | 8 / 20 / 2 | ETHU 16%, NVDA 15%, PLTR 15%, AMZN 14% |  |
| Breezy | 2026-09-28T15:10 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-09-28T15:10 | 17 / 13 / 0 | ETHU 46%, BITX 45% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.76 | 1.76 | 0 | — | 13.17 | 2.88 | -7.55 | 43 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.63 | 0.64 | 0 | — | -4.34 | -1.26 | -12.40 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 0 | — | 1.45 | 0.68 | -4.88 | 16 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.42 | 0.42 | 4 | 50.0 | 2.52 | 1.31 | -2.47 | 92 |
| 5 | Copy: Hedge-fund gurus (GURU) | copy | 100.25 | 0.25 | 0 | — | -0.21 | -0.05 | -5.14 | 1 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 8.15 | 1.34 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | -0.41 | -0.62 | -1.49 | 18 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.92 | -0.08 | 0 | — | -0.65 | -0.57 | -7.65 | 1 |
| 11 | Agent (aggressive) | meta | 99.88 | -0.12 | 4 | 50.0 | 4.14 | 2.08 | -3.92 | 88 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.48 | -0.52 | 0 | — | -7.01 | -1.81 | -12.73 | 1 |
| 13 | Hold SPY | benchmark | 99.39 | -0.61 | 0 | — | 3.19 | 1.71 | -3.66 | 1 |
| 14 | Agent | meta | 99.39 | -0.61 | 11 | 63.6 | -9.00 | -5.65 | -9.99 | 205 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.88 | -4.43 | -14.73 | 121 |
| 16 | RSI(14) reversion · 1h | reversion | 99.32 | -0.68 | 1 | 100.0 | 1.10 | 0.38 | -8.03 | 122 |
| 17 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 18 | Hold BTC | benchmark | 99.26 | -0.74 | 0 | — | 30.12 | 3.84 | -8.68 | 1 |
| 19 | Agent (rotation) | meta | 99.16 | -0.84 | 26 | 11.5 | -7.64 | -2.63 | -11.56 | 215 |
| 20 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.44 | -5.16 | 27 |
| 21 | Daily: Bullish score | daily | 99.11 | -0.89 | 2 | 0.0 | -0.83 | 0.07 | -12.76 | 13 |
| 22 | Copy: Congress Democrats (NANC) | copy | 99.07 | -0.93 | 0 | — | 6.09 | 2.40 | -3.62 | 1 |
| 23 | Copy: Insider buying | copy | 99.00 | -0.99 | 2 | 100.0 | -12.14 | -2.33 | -17.74 | 73 |
| 24 | Opening range 30m | breakout | 98.98 | -1.02 | 13 | 15.4 | -7.79 | -2.27 | -13.54 | 548 |
| 25 | Timing: Nasdaq FTD · QQQ | daily | 98.71 | -1.29 | 0 | — | -3.85 | -2.35 | -5.09 | 2 |
| 26 | Z-score reversion · 1h | reversion | 98.38 | -1.62 | 4 | 25.0 | 3.36 | 0.86 | -8.60 | 154 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -0.56 | -0.05 | -15.21 | 47 |
| 28 | Stochastic reversion · 1h | reversion | 98.31 | -1.69 | 20 | 50.0 | -9.91 | -2.19 | -11.36 | 322 |
| 29 | Williams %R · 1h | reversion | 98.18 | -1.82 | 26 | 50.0 | -20.02 | -3.66 | -21.75 | 479 |
| 30 | Squeeze breakout · 1h | breakout | 98.16 | -1.84 | 7 | 14.3 | 17.04 | 2.80 | -9.25 | 101 |
| 31 | Parabolic SAR · 1h | trend | 98.13 | -1.87 | 14 | 21.4 | -4.69 | -0.51 | -18.82 | 300 |
| 32 | Connors RSI(2) · 1h | reversion | 98.07 | -1.93 | 28 | 46.4 | -13.33 | -4.23 | -13.96 | 244 |
| 33 | Opening range 15m | breakout | 98.05 | -1.96 | 22 | 13.6 | -10.53 | -2.83 | -16.14 | 683 |
| 34 | Candlestick reversal · 1h | reversion | 97.96 | -2.04 | 8 | 12.5 | -25.93 | -6.28 | -26.52 | 490 |
| 35 | CCI reversion · 1h | reversion | 97.94 | -2.06 | 18 | 27.8 | -0.58 | 0.08 | -12.41 | 406 |
| 36 | Supertrend · 1h | trend | 97.91 | -2.09 | 10 | 10.0 | 5.39 | 0.92 | -16.43 | 194 |
| 37 | Bollinger reversion · 1h | reversion | 97.69 | -2.31 | 18 | 33.3 | -15.51 | -4.28 | -16.03 | 306 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 97.54 | -2.46 | 0 | — | 22.69 | 3.29 | -6.29 | 1 |
| 39 | EMA 20/50 cross · 1h | trend | 97.37 | -2.63 | 7 | 14.3 | 15.29 | 1.85 | -14.36 | 125 |
| 40 | MACD cross · 1h | trend | 97.29 | -2.71 | 26 | 11.5 | -16.74 | -2.87 | -21.63 | 457 |
| 41 | MACD zero-line · 1h | trend | 97.18 | -2.82 | 13 | 7.7 | 0.30 | 0.24 | -14.64 | 223 |
| 42 | Bollinger breakout · 1h | breakout | 97.14 | -2.86 | 13 | 7.7 | 15.02 | 2.08 | -10.92 | 283 |
| 43 | Trend pullback · 1h | trend | 96.96 | -3.04 | 20 | 15.0 | -26.84 | -7.27 | -27.51 | 153 |
| 44 | Agent (ML meta-label) | meta | 96.94 | -3.06 | 44 | 4.5 | 5.19 | 1.07 | -13.74 | 379 |
| 45 | ADX DI cross · 1h | trend | 96.76 | -3.24 | 22 | 9.1 | -15.25 | -2.95 | -19.57 | 254 |
| 46 | RSI momentum · 1h | momentum | 96.75 | -3.25 | 18 | 5.6 | 3.12 | 0.64 | -15.29 | 214 |
| 47 | Three white soldiers | momentum | 96.73 | -3.27 | 28 | 14.3 | -51.89 | -28.27 | -51.90 | 621 |
| 48 | Donchian 55/20 · 1h | breakout | 96.60 | -3.40 | 5 | 0.0 | 4.26 | 0.77 | -16.96 | 113 |
| 49 | Ichimoku · 1h | trend | 96.37 | -3.63 | 10 | 10.0 | 9.02 | 1.24 | -15.13 | 119 |
| 50 | Timing: Nasdaq FTD · TQQQ | daily | 96.33 | -3.67 | 0 | — | -12.20 | -2.52 | -15.27 | 2 |
| 51 | Donchian 20/10 · 1h | breakout | 96.10 | -3.90 | 12 | 16.7 | 13.01 | 1.83 | -12.78 | 213 |
| 52 | Max aggression: 1-day momentum | meta | 96.09 | -3.91 | 1 | 0.0 | -31.57 | -1.77 | -49.41 | 42 |
| 53 | EMA 9/21 cross · 1h | trend | 96.09 | -3.91 | 28 | 14.3 | 4.80 | 0.85 | -16.92 | 308 |
| 54 | Heikin-Ashi · 1h | trend | 95.98 | -4.02 | 27 | 14.8 | -22.47 | -3.41 | -27.94 | 689 |
| 55 | Triple EMA stack · 1h | trend | 95.92 | -4.08 | 20 | 10.0 | -4.44 | -0.32 | -22.96 | 210 |
| 56 | AI bee: Bizzy | ai | 95.72 | -4.28 | 70 | 8.6 | — | — | — | — |
| 57 | VWAP momentum · 1h | momentum | 95.70 | -4.30 | 73 | 6.8 | -34.40 | -5.14 | -34.72 | 1265 |
| 58 | Max aggression: 5-day momentum | meta | 95.54 | -4.46 | 1 | 0.0 | -0.76 | 0.29 | -29.56 | 29 |
| 59 | OBV trend · 1h | momentum | 95.44 | -4.56 | 44 | 6.8 | -8.93 | -0.91 | -25.24 | 331 |
| 60 | Volume breakout · 1h | breakout | 95.30 | -4.70 | 25 | 4.0 | 9.58 | 1.48 | -12.60 | 127 |
| 61 | Keltner breakout · 1h | breakout | 95.25 | -4.75 | 7 | 0.0 | -1.01 | 0.07 | -18.68 | 218 |
| 62 | MFI reversion · 1h | reversion | 95.03 | -4.97 | 37 | 10.8 | -10.54 | -1.97 | -17.27 | 126 |
| 63 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 64 | ROC + volume · 1h | momentum | 92.37 | -7.63 | 41 | 4.9 | 0.83 | 0.32 | -17.18 | 403 |
| 65 | RSI(14) reversion | reversion | 92.25 | -7.75 | 65 | 23.1 | -71.70 | -22.34 | -71.84 | 1478 |
| 66 | Squeeze breakout | breakout | 91.15 | -8.85 | 58 | 6.9 | -59.90 | -18.61 | -60.07 | 1186 |
| 67 | Volume breakout | breakout | 90.61 | -9.39 | 62 | 8.1 | -62.19 | -20.87 | -62.19 | 902 |
| 68 | EMA 20/50 cross | trend | 90.40 | -9.60 | 71 | 15.5 | -78.55 | -17.71 | -78.61 | 1479 |
| 69 | Donchian 55/20 | breakout | 90.29 | -9.71 | 66 | 10.6 | -68.49 | -15.86 | -68.49 | 1329 |
| 70 | ROC + volume | momentum | 90.02 | -9.98 | 84 | 11.9 | -72.42 | -18.10 | -72.65 | 1640 |
| 71 | Ichimoku | trend | 88.80 | -11.20 | 79 | 7.6 | -80.47 | -26.48 | -80.49 | 1770 |
| 72 | Keltner breakout | breakout | 88.79 | -11.21 | 87 | 9.2 | -85.31 | -35.81 | -85.31 | 1919 |
| 73 | Z-score reversion | reversion | 86.34 | -13.66 | 115 | 19.1 | -85.09 | -28.84 | -85.15 | 2109 |
| 74 | RSI momentum | momentum | 85.98 | -14.02 | 113 | 13.3 | -90.42 | -30.13 | -90.50 | 2396 |
| 75 | MACD zero-line | trend | 85.94 | -14.06 | 122 | 13.9 | -91.67 | -37.20 | -91.68 | 2364 |
| 76 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -71.20 | -17.38 | -71.87 | 1414 |
| 77 | Supertrend | trend | 85.66 | -14.34 | 110 | 15.5 | -87.46 | -25.41 | -87.52 | 1966 |
| 78 | Bollinger breakout | breakout | 85.50 | -14.50 | 118 | 11.0 | -94.04 | -43.13 | -94.04 | 2872 |
| 79 | Triple EMA stack | trend | 85.45 | -14.55 | 139 | 12.9 | -93.05 | -37.04 | -93.06 | 2617 |
| 80 | Trend pullback | trend | 85.37 | -14.62 | 121 | 16.5 | -90.75 | -35.80 | -90.75 | 2310 |
| 81 | Donchian 20/10 | breakout | 85.05 | -14.95 | 128 | 14.1 | -91.05 | -30.34 | -91.09 | 2689 |
| 82 | Connors RSI(2) | reversion | 84.11 | -15.89 | 163 | 17.2 | -96.37 | -43.11 | -96.37 | 3654 |
| 83 | ADX DI cross | trend | 84.05 | -15.95 | 121 | 7.4 | -89.39 | -49.91 | -89.41 | 2119 |
| 84 | MFI reversion | reversion | 83.03 | -16.97 | 122 | 9.0 | -88.06 | -37.93 | -88.12 | 2178 |
| 85 | Stochastic reversion | reversion | 82.29 | -17.71 | 185 | 19.5 | -95.93 | -49.73 | -95.97 | 4073 |
| 86 | Consensus | meta | 81.34 | -18.66 | 129 | 6.2 | -94.88 | -32.12 | -94.88 | 2665 |
| 87 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.33 | -56.04 | -99.34 | 5553 |
| 88 | OBV trend | momentum | 80.99 | -19.01 | 179 | 12.3 | -95.89 | -50.69 | -95.90 | 3566 |
| 89 | EMA 9/21 cross | trend | 80.87 | -19.13 | 183 | 12.6 | -97.46 | -43.96 | -97.47 | 3543 |
| 90 | Bollinger reversion | reversion | 79.72 | -20.28 | 203 | 12.8 | -95.88 | -46.88 | -95.90 | 3705 |
| 91 | VWAP momentum | momentum | 79.51 | -20.49 | 225 | 9.8 | -98.50 | -37.23 | -98.50 | 5248 |
| 92 | Parabolic SAR | trend | 78.66 | -21.34 | 196 | 12.2 | -96.90 | -60.70 | -96.91 | 3647 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.46 | -56.43 | -98.47 | 4717 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -75.26 | -99.70 | 6099 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.53 | -68.02 | -99.53 | 6105 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.89 | -104.74 | -99.89 | 8313 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T15:10 | AI bee: Bizzy | buy | ETHU | 15.08 | — | Jev: buy (buy p=0.63) |
| 2026-09-28T15:10 | AI bee: Bizzy | buy | AMZN | 13.40 | — | Jev: buy (buy p=0.56) |
| 2026-09-28T15:10 | AI bee: Bizzy | sell | TECL | 12.72 | 0.04 | Jev: buy (buy p=0.54) |
| 2026-09-28T15:10 | AI bee: Bizzy | sell | MSFT | 16.73 | -0.02 | Jev: sell (buy p=0.31) |
| 2026-09-28T15:10 | Agent (rotation) | sell | SQQQ | 8.36 | 0.09 | rebalance down |
| 2026-09-28T15:10 | Z-score reversion | buy | BITX | 1.71 | — | entry signal |
| 2026-09-28T15:10 | Z-score reversion | buy | AMD | 4.55 | — | entry signal |
| 2026-09-28T15:10 | Z-score reversion | sell | DOGE-USD | 6.26 | -0.00 | rebalance down |
| 2026-09-28T15:10 | Bollinger reversion | buy | SOL-USD | 5.32 | — | entry |
| 2026-09-28T15:10 | Bollinger reversion | sell | MSFT | 5.39 | 0.03 | exit signal |
| 2026-09-28T15:10 | Connors RSI(2) | buy | SQQQ | 21.03 | — | entry signal |
| 2026-09-28T15:10 | Connors RSI(2) | sell | AAPL | 21.01 | -0.06 | exit signal |
| 2026-09-28T15:10 | RSI(14) reversion | buy | UPRO | 4.94 | — | entry signal |
| 2026-09-28T15:10 | RSI(14) reversion | buy | TSLA | 7.10 | — | entry signal |
| 2026-09-28T15:10 | RSI(14) reversion | buy | TNA | 7.10 | — | entry signal |
| 2026-09-28T15:10 | RSI(14) reversion | buy | SPY | 7.10 | — | entry signal |
| 2026-09-28T15:10 | RSI(14) reversion | buy | QQQ | 7.10 | — | entry signal |
| 2026-09-28T15:10 | RSI(14) reversion | buy | IWM | 7.10 | — | entry signal |
| 2026-09-28T15:10 | RSI(14) reversion | sell | TQQQ | 6.11 | 0.02 | rebalance down |
| 2026-09-28T15:10 | RSI(14) reversion | sell | TECL | 6.11 | 0.02 | rebalance down |
| 2026-09-28T15:10 | RSI(14) reversion | sell | MSFT | 6.08 | 0.01 | rebalance down |
| 2026-09-28T15:10 | RSI(14) reversion | sell | GOOGL | 6.07 | -0.00 | rebalance down |
| 2026-09-28T15:10 | RSI(14) reversion | sell | COIN | 6.08 | -0.02 | rebalance down |
| 2026-09-28T15:10 | RSI(14) reversion | sell | AMZN | 6.08 | 0.02 | rebalance down |
| 2026-09-28T15:10 | Squeeze breakout | sell | SQQQ | 22.97 | 0.30 | stop-loss |
| 2026-09-28T15:10 | Gap and go | sell | SQQQ | 25.11 | 0.33 | stop-loss |
| 2026-09-28T15:10 | OBV trend | buy | NVDA | 20.27 | — | entry signal |
| 2026-09-28T15:10 | OBV trend | buy | ETH-USD | 20.27 | — | entry signal |
| 2026-09-28T15:10 | VWAP momentum | buy | PLTR | 7.90 | — | entry signal |
| 2026-09-28T15:10 | VWAP momentum | buy | ETH-USD | 5.16 | — | rebalance up |
| 2026-09-28T15:10 | VWAP momentum | sell | SQQQ | 6.40 | -0.00 | rebalance down |
| 2026-09-28T15:10 | VWAP momentum | sell | MSFT | 6.66 | 0.02 | rebalance down |
| 2026-09-28T15:10 | Trend pullback | buy | NVDA | 21.36 | — | entry signal |
| 2026-09-28T15:10 | Trend pullback | buy | ETH-USD | 21.36 | — | entry signal |
| 2026-09-28T15:10 | ADX DI cross | buy | NVDA | 21.01 | — | entry signal |
| 2026-09-28T15:10 | Parabolic SAR | buy | ETH-USD | 19.68 | — | entry signal |
| 2026-09-28T15:08 | AI bee: Bizzy | buy | NVDA | 14.36 | — | Jev: buy (buy p=0.60) |
| 2026-09-28T15:08 | AI bee: Bizzy | buy | MSFT | 16.76 | — | Jev: buy (buy p=0.70) |
| 2026-09-28T15:08 | AI bee: Bizzy | sell | GOOGL | 16.01 | -0.01 | Jev: sell (buy p=0.20) |
| 2026-09-28T15:08 | AI bee: Bizzy | sell | AMZN | 13.40 | 0.00 | Jev: buy (buy p=0.50) |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
