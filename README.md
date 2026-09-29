# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T15:40:05.000152+00:00 · 5849 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.31 (+0.31%)

Closed trades 19, win rate 73.7%, fees £0.58, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 20.05 | -0.01 |
| TQQQ | 20.13 | +0.08 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-29 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 19638 decisions in 2309 calls, $0.2525 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T15:40 | 7 / 13 / 9 | XRP-USD 17%, LABU 16%, ARKK 15%, NVDA 14% |  |
| Breezy | 2026-09-29T15:40 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-09-29T15:40 | 14 / 14 / 1 | ETHU 38%, BITX 37% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |
| VWAP reversion | NVDA | 2.05 | +2.06% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.50 | 1.50 | 1 | 100.0 | 14.24 | 3.10 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Agent | meta | 100.31 | 0.31 | 19 | 73.7 | -8.73 | -5.70 | -10.16 | 208 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 5 | Agent (aggressive) | meta | 100.22 | 0.22 | 8 | 62.5 | 1.03 | 0.61 | -4.81 | 92 |
| 6 | Copy: Congress Democrats (NANC) | copy | 100.02 | 0.02 | 0 | — | 7.72 | 2.93 | -3.62 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 11.61 | 2.22 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.71 | -0.29 | 0 | — | -1.55 | -0.60 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.45 | 1.78 | -1.51 | 83 |
| 12 | Hold BTC | benchmark | 99.63 | -0.38 | 0 | — | 30.40 | 3.82 | -8.68 | 1 |
| 13 | Max aggression: 5-day momentum | meta | 99.61 | -0.39 | 2 | 50.0 | -6.87 | -0.28 | -29.56 | 29 |
| 14 | Hold SPY | benchmark | 99.52 | -0.48 | 0 | — | 4.12 | 2.14 | -3.66 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.44 | -0.56 | 0 | — | -3.49 | -2.15 | -5.09 | 2 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.43 | -0.57 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 17 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 18 | RSI(14) reversion · 1h | reversion | 99.23 | -0.77 | 7 | 57.1 | 0.81 | 0.32 | -6.85 | 123 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Daily: Bullish score | daily | 98.97 | -1.03 | 2 | 0.0 | -1.40 | -0.00 | -12.76 | 13 |
| 21 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 22 | Williams %R · 1h | reversion | 98.69 | -1.31 | 39 | 46.2 | -17.57 | -3.23 | -19.41 | 484 |
| 23 | Z-score reversion · 1h | reversion | 98.62 | -1.38 | 9 | 44.4 | 3.68 | 0.92 | -8.60 | 152 |
| 24 | Copy: Insider buying | copy | 98.46 | -1.54 | 2 | 100.0 | -14.72 | -2.94 | -17.74 | 72 |
| 25 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.64 | 3.88 | -4.73 | 195 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 98.39 | -1.61 | 0 | — | 25.85 | 3.72 | -6.29 | 1 |
| 27 | Candlestick reversal · 1h | reversion | 98.37 | -1.63 | 16 | 25.0 | -26.84 | -6.48 | -27.36 | 486 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.01 | 0.03 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.21 | -1.79 | 34 | 35.3 | 2.36 | 0.56 | -12.41 | 406 |
| 30 | EMA 20/50 cross · 1h | trend | 98.20 | -1.80 | 9 | 11.1 | 16.53 | 1.98 | -14.36 | 127 |
| 31 | Agent (rotation) | meta | 98.00 | -2.00 | 32 | 12.5 | -5.60 | -1.91 | -11.79 | 218 |
| 32 | Opening range 30m | breakout | 97.92 | -2.08 | 31 | 12.9 | -8.27 | -2.38 | -13.54 | 559 |
| 33 | Connors RSI(2) · 1h | reversion | 97.86 | -2.14 | 41 | 46.3 | -12.97 | -4.10 | -13.23 | 236 |
| 34 | Timing: Nasdaq FTD · TQQQ | daily | 97.74 | -2.25 | 0 | — | -11.24 | -2.32 | -15.27 | 2 |
| 35 | Stochastic reversion · 1h | reversion | 97.72 | -2.28 | 26 | 53.8 | -14.69 | -3.25 | -15.14 | 320 |
| 36 | Supertrend · 1h | trend | 97.58 | -2.42 | 15 | 6.7 | 4.60 | 0.81 | -16.43 | 197 |
| 37 | Daily: SMA 20/50 cross · AAPL | daily | 97.55 | -2.45 | 0 | — | -9.56 | -2.36 | -12.73 | 1 |
| 38 | Squeeze breakout · 1h | breakout | 97.47 | -2.54 | 9 | 11.1 | 15.36 | 2.70 | -6.18 | 97 |
| 39 | Donchian 55/20 · 1h | breakout | 97.12 | -2.88 | 11 | 0.0 | 4.75 | 0.83 | -16.96 | 113 |
| 40 | Bollinger reversion · 1h | reversion | 96.97 | -3.03 | 22 | 27.3 | -18.32 | -5.11 | -18.43 | 306 |
| 41 | Agent (ML meta-label) | meta | 96.74 | -3.26 | 100 | 11.0 | -3.22 | -0.48 | -13.41 | 391 |
| 42 | MACD cross · 1h | trend | 96.70 | -3.30 | 34 | 8.8 | -18.18 | -3.10 | -21.85 | 459 |
| 43 | Trend pullback · 1h | trend | 96.68 | -3.32 | 24 | 12.5 | -28.75 | -7.02 | -29.59 | 149 |
| 44 | Opening range 15m | breakout | 96.47 | -3.53 | 40 | 12.5 | -9.94 | -2.69 | -16.14 | 691 |
| 45 | Parabolic SAR · 1h | trend | 96.21 | -3.79 | 22 | 13.6 | -7.67 | -0.96 | -18.82 | 291 |
| 46 | Ichimoku · 1h | trend | 96.18 | -3.82 | 13 | 15.4 | 7.23 | 1.04 | -15.13 | 121 |
| 47 | MACD zero-line · 1h | trend | 95.68 | -4.32 | 16 | 6.2 | -4.44 | -0.44 | -14.64 | 222 |
| 48 | RSI momentum · 1h | momentum | 95.51 | -4.49 | 22 | 4.5 | -0.39 | 0.15 | -15.29 | 212 |
| 49 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -51.93 | -28.85 | -52.16 | 626 |
| 50 | Bollinger breakout · 1h | breakout | 95.28 | -4.72 | 17 | 5.9 | 7.75 | 1.21 | -10.20 | 285 |
| 51 | ADX DI cross · 1h | trend | 95.06 | -4.94 | 28 | 7.1 | -11.39 | -2.10 | -15.39 | 254 |
| 52 | Volume breakout · 1h | breakout | 94.99 | -5.01 | 25 | 4.0 | 6.21 | 1.04 | -12.60 | 125 |
| 53 | Donchian 20/10 · 1h | breakout | 94.94 | -5.06 | 13 | 15.4 | 8.40 | 1.26 | -12.78 | 215 |
| 54 | Triple EMA stack · 1h | trend | 94.92 | -5.08 | 27 | 7.4 | -7.08 | -0.67 | -22.53 | 229 |
| 55 | VWAP momentum · 1h | momentum | 94.77 | -5.23 | 97 | 13.4 | -30.89 | -4.54 | -34.62 | 1236 |
| 56 | MFI reversion · 1h | reversion | 94.75 | -5.25 | 40 | 12.5 | -10.66 | -1.98 | -17.27 | 127 |
| 57 | Keltner breakout · 1h | breakout | 94.32 | -5.68 | 9 | 0.0 | -5.65 | -0.56 | -18.68 | 215 |
| 58 | EMA 9/21 cross · 1h | trend | 94.18 | -5.82 | 39 | 12.8 | -3.26 | -0.25 | -16.92 | 309 |
| 59 | OBV trend · 1h | momentum | 93.90 | -6.10 | 49 | 8.2 | -8.74 | -0.90 | -25.24 | 329 |
| 60 | Max aggression: 1-day momentum | meta | 93.70 | -6.30 | 2 | 0.0 | -39.92 | -2.44 | -49.44 | 42 |
| 61 | Heikin-Ashi · 1h | trend | 93.42 | -6.58 | 39 | 12.8 | -22.27 | -3.31 | -30.23 | 679 |
| 62 | RSI(14) reversion | reversion | 91.38 | -8.62 | 98 | 33.7 | -71.10 | -21.77 | -71.10 | 1474 |
| 63 | ROC + volume · 1h | momentum | 89.83 | -10.17 | 50 | 6.0 | -4.30 | -0.34 | -19.13 | 407 |
| 64 | Squeeze breakout | breakout | 89.78 | -10.21 | 79 | 10.1 | -60.25 | -18.97 | -60.72 | 1184 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | Donchian 55/20 | breakout | 88.05 | -11.95 | 87 | 14.9 | -67.67 | -15.56 | -67.73 | 1309 |
| 68 | EMA 20/50 cross | trend | 87.88 | -12.12 | 103 | 14.6 | -78.32 | -17.45 | -78.55 | 1469 |
| 69 | ROC + volume | momentum | 87.44 | -12.56 | 133 | 17.3 | -72.40 | -18.16 | -73.01 | 1670 |
| 70 | Volume breakout | breakout | 87.38 | -12.62 | 89 | 12.4 | -62.23 | -20.86 | -62.61 | 925 |
| 71 | Ichimoku | trend | 86.09 | -13.91 | 104 | 8.7 | -80.45 | -26.23 | -80.45 | 1765 |
| 72 | Keltner breakout | breakout | 85.58 | -14.42 | 138 | 11.6 | -85.03 | -35.61 | -85.29 | 1937 |
| 73 | Z-score reversion | reversion | 85.15 | -14.85 | 160 | 30.0 | -84.55 | -28.21 | -84.57 | 2096 |
| 74 | VWAP reversion | reversion | 84.60 | -15.40 | 117 | 17.9 | -71.89 | -17.73 | -72.13 | 1393 |
| 75 | Supertrend | trend | 83.23 | -16.77 | 155 | 16.8 | -87.60 | -25.35 | -87.64 | 1958 |
| 76 | MACD zero-line | trend | 83.00 | -17.00 | 172 | 14.5 | -91.65 | -36.48 | -91.66 | 2354 |
| 77 | MFI reversion | reversion | 82.15 | -17.85 | 160 | 18.1 | -87.51 | -34.25 | -87.73 | 2157 |
| 78 | Donchian 20/10 | breakout | 81.35 | -18.65 | 178 | 16.9 | -90.94 | -30.49 | -91.10 | 2691 |
| 79 | Bollinger breakout | breakout | 81.04 | -18.96 | 183 | 14.8 | -94.01 | -42.58 | -94.13 | 2880 |
| 80 | Triple EMA stack | trend | 80.91 | -19.09 | 192 | 14.6 | -92.94 | -36.65 | -92.94 | 2619 |
| 81 | RSI momentum | momentum | 80.78 | -19.23 | 171 | 11.7 | -90.45 | -29.85 | -90.45 | 2384 |
| 82 | Trend pullback | trend | 80.38 | -19.62 | 162 | 17.9 | -90.73 | -34.59 | -90.73 | 2295 |
| 83 | ADX DI cross | trend | 80.34 | -19.66 | 177 | 6.8 | -89.39 | -47.36 | -89.47 | 2099 |
| 84 | EMA 9/21 cross | trend | 77.74 | -22.26 | 248 | 14.9 | -97.37 | -42.28 | -97.39 | 3535 |
| 85 | Consensus | meta | 77.69 | -22.31 | 175 | 7.4 | -94.60 | -30.62 | -94.60 | 2649 |
| 86 | Connors RSI(2) | reversion | 77.66 | -22.34 | 234 | 16.2 | -96.46 | -43.09 | -96.47 | 3649 |
| 87 | Candlestick reversal | reversion | 76.93 | -23.07 | 240 | 13.3 | -99.34 | -52.09 | -99.35 | 5554 |
| 88 | Stochastic reversion | reversion | 76.77 | -23.23 | 285 | 22.1 | -95.92 | -48.18 | -95.96 | 4063 |
| 89 | OBV trend | momentum | 76.28 | -23.73 | 249 | 14.1 | -95.84 | -49.61 | -95.85 | 3546 |
| 90 | Bollinger reversion | reversion | 75.68 | -24.32 | 272 | 13.6 | -95.77 | -46.62 | -95.78 | 3682 |
| 91 | VWAP momentum | momentum | 74.76 | -25.24 | 335 | 9.9 | -98.42 | -36.45 | -98.46 | 5214 |
| 92 | CCI reversion | reversion | 74.31 | -25.69 | 194 | 6.2 | -98.45 | -52.61 | -98.45 | 4680 |
| 93 | MACD cross | trend | 72.66 | -27.34 | 226 | 11.5 | -99.70 | -66.75 | -99.71 | 6098 |
| 94 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -97.00 | -57.02 | -97.00 | 3649 |
| 95 | Williams %R | reversion | 72.35 | -27.65 | 290 | 19.3 | -99.52 | -61.43 | -99.52 | 6095 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -91.73 | -99.89 | 8339 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T15:40 | Consensus | buy | NVDA | 19.43 | — | entry |
| 2026-09-29T15:40 | Agent (aggressive) | buy | AMD | 50.12 | — | following Stochastic reversion |
| 2026-09-29T15:40 | Agent | buy | AMD | 20.06 | — | following Stochastic reversion |
| 2026-09-29T15:40 | MFI reversion | buy | UPRO | 10.23 | — | entry |
| 2026-09-29T15:40 | MFI reversion | buy | SOL-USD | 10.28 | — | entry signal |
| 2026-09-29T15:40 | MFI reversion | buy | BITX | 10.28 | — | entry |
| 2026-09-29T15:40 | MFI reversion | sell | XRP-USD | 6.07 | -0.02 | rebalance down |
| 2026-09-29T15:40 | MFI reversion | sell | TNA | 6.16 | -0.01 | rebalance down |
| 2026-09-29T15:40 | MFI reversion | sell | SQQQ | 6.24 | 0.04 | rebalance down |
| 2026-09-29T15:40 | MFI reversion | sell | SPY | 6.17 | -0.01 | rebalance down |
| 2026-09-29T15:40 | MFI reversion | sell | DOGE-USD | 6.14 | -0.03 | rebalance down |
| 2026-09-29T15:40 | CCI reversion | buy | UPRO | 5.70 | — | entry signal |
| 2026-09-29T15:40 | CCI reversion | buy | TQQQ | 5.72 | — | entry signal |
| 2026-09-29T15:40 | CCI reversion | buy | TNA | 5.72 | — | entry signal |
| 2026-09-29T15:40 | CCI reversion | buy | SPY | 5.72 | — | entry signal |
| 2026-09-29T15:40 | CCI reversion | buy | SOXL | 5.72 | — | entry signal |
| 2026-09-29T15:40 | CCI reversion | buy | QQQ | 5.72 | — | entry signal |
| 2026-09-29T15:40 | CCI reversion | buy | IWM | 5.72 | — | entry signal |
| 2026-09-29T15:40 | CCI reversion | sell | TSLA | 6.66 | 0.01 | rebalance down |
| 2026-09-29T15:40 | CCI reversion | sell | TECL | 6.65 | -0.01 | rebalance down |
| 2026-09-29T15:40 | CCI reversion | sell | PLTR | 6.63 | -0.02 | rebalance down |
| 2026-09-29T15:40 | CCI reversion | sell | LABU | 6.73 | 0.01 | rebalance down |
| 2026-09-29T15:40 | CCI reversion | sell | GOOGL | 6.66 | -0.01 | rebalance down |
| 2026-09-29T15:40 | CCI reversion | sell | AAPL | 6.68 | -0.01 | rebalance down |
| 2026-09-29T15:40 | Williams %R | buy | DOGE-USD | 1.47 | — | entry signal |
| 2026-09-29T15:40 | Williams %R | buy | BITX | 3.81 | — | entry signal |
| 2026-09-29T15:40 | Williams %R | sell | UPRO | 5.28 | 0.01 | rebalance down |
| 2026-09-29T15:40 | Bollinger reversion | sell | AAPL | 5.83 | -0.00 | exit signal |
| 2026-09-29T15:40 | Connors RSI(2) | sell | XRP-USD | 19.41 | -0.03 | exit signal |
| 2026-09-29T15:40 | Connors RSI(2) | sell | SOL-USD | 19.30 | -0.19 | exit signal |
| 2026-09-29T15:40 | Candlestick reversal | buy | BTC-USD | 2.87 | — | entry |
| 2026-09-29T15:40 | Candlestick reversal | buy | BITX | 4.81 | — | entry |
| 2026-09-29T15:40 | Candlestick reversal | sell | GOOGL | 7.68 | -0.01 | exit signal |
| 2026-09-29T15:40 | VWAP momentum | buy | TSLA | 11.25 | — | entry signal |
| 2026-09-29T15:40 | VWAP momentum | buy | SOXL | 14.96 | — | entry signal |
| 2026-09-29T15:40 | VWAP momentum | buy | NVDA | 14.96 | — | entry signal |
| 2026-09-29T15:40 | VWAP momentum | sell | MSFT | 3.80 | 0.01 | rebalance down |
| 2026-09-29T15:40 | VWAP momentum | sell | AMZN | 18.68 | -0.02 | exit signal |
| 2026-09-29T15:40 | ADX DI cross | sell | SQQQ | 20.13 | 0.03 | exit signal |
| 2026-09-29T15:40 | MACD cross | buy | LABU | 7.26 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
