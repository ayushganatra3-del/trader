# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T18:40:05.000141+00:00 · 5984 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.04 (+0.04%)

Closed trades 23, win rate 69.6%, fees £0.69, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 40.00 | +0.06 |
| COIN | 20.03 | +0.04 |

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

Today: 31656 decisions in 2714 calls, $0.3932 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T18:40 | 13 / 12 / 5 | TNA 20%, META 17%, ARKK 16%, MSFT 15% |  |
| Breezy | 2026-09-29T18:40 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-09-29T18:40 | 12 / 17 / 1 | BITX 44%, TNA 42% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.17 | 1.17 | 1 | 100.0 | 13.78 | 3.01 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -2.39 | -0.68 | -9.74 | 24 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.13 | 0.13 | 0 | — | 6.84 | 2.82 | -3.62 | 1 |
| 5 | Hold BTC | benchmark | 100.10 | 0.10 | 0 | — | 30.52 | 3.83 | -8.68 | 1 |
| 6 | Agent (aggressive) | meta | 100.10 | 0.10 | 9 | 55.6 | -0.02 | 0.04 | -3.92 | 97 |
| 7 | Agent | meta | 100.04 | 0.04 | 23 | 69.6 | -10.02 | -6.73 | -10.72 | 216 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.58 | 1.43 | -7.93 | 7 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 99.81 | -0.19 | 0 | — | -1.21 | -0.45 | -7.65 | 1 |
| 12 | Hold SPY | benchmark | 99.73 | -0.27 | 0 | — | 4.54 | 2.37 | -3.66 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.54 | 1.82 | -1.51 | 83 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 99.65 | -0.35 | 0 | — | -3.36 | -2.06 | -5.09 | 2 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.50 | -0.50 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 16 | Daily: Bullish score | daily | 99.43 | -0.57 | 2 | 0.0 | -1.26 | 0.02 | -12.76 | 13 |
| 17 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.96 | -4.41 | -14.82 | 121 |
| 18 | RSI(14) reversion · 1h | reversion | 99.19 | -0.81 | 7 | 57.1 | 11.36 | 2.18 | -6.57 | 139 |
| 19 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 20 | Z-score reversion · 1h | reversion | 98.97 | -1.03 | 10 | 50.0 | 4.54 | 1.11 | -8.60 | 154 |
| 21 | Williams %R · 1h | reversion | 98.95 | -1.05 | 40 | 45.0 | -17.84 | -3.31 | -19.54 | 479 |
| 22 | Candlestick reversal · 1h | reversion | 98.85 | -1.15 | 20 | 25.0 | -27.22 | -6.55 | -28.08 | 495 |
| 23 | Max aggression: 5-day momentum | meta | 98.81 | -1.19 | 2 | 50.0 | -7.69 | -0.36 | -29.56 | 29 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 25 | Copy: Insider buying | copy | 98.63 | -1.37 | 2 | 100.0 | -14.59 | -2.91 | -17.74 | 72 |
| 26 | Stochastic reversion · 1h | reversion | 98.62 | -1.38 | 26 | 53.8 | -13.54 | -3.02 | -14.71 | 325 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.53 | -1.47 | 0 | — | 25.50 | 3.67 | -6.29 | 1 |
| 28 | CCI reversion · 1h | reversion | 98.51 | -1.49 | 35 | 34.3 | 2.54 | 0.59 | -12.41 | 406 |
| 29 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.34 | 3.80 | -4.73 | 195 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.75 | -0.09 | -15.21 | 47 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 98.21 | -1.79 | 0 | — | -10.88 | -2.23 | -15.27 | 2 |
| 32 | EMA 20/50 cross · 1h | trend | 98.16 | -1.84 | 11 | 9.1 | 16.72 | 2.00 | -14.36 | 126 |
| 33 | Connors RSI(2) · 1h | reversion | 98.15 | -1.84 | 42 | 45.2 | -11.35 | -3.65 | -11.80 | 235 |
| 34 | Agent (rotation) | meta | 97.89 | -2.11 | 32 | 12.5 | -5.32 | -1.79 | -11.69 | 223 |
| 35 | Bollinger reversion · 1h | reversion | 97.36 | -2.64 | 22 | 27.3 | -17.87 | -5.00 | -18.44 | 312 |
| 36 | Daily: SMA 20/50 cross · AAPL | daily | 97.30 | -2.70 | 0 | — | -10.76 | -2.64 | -12.64 | 1 |
| 37 | Squeeze breakout · 1h | breakout | 97.21 | -2.79 | 9 | 11.1 | 10.67 | 1.85 | -10.94 | 99 |
| 38 | Opening range 30m | breakout | 97.11 | -2.89 | 36 | 11.1 | -9.06 | -2.60 | -14.21 | 563 |
| 39 | Supertrend · 1h | trend | 96.87 | -3.13 | 18 | 5.6 | 2.77 | 0.57 | -16.43 | 190 |
| 40 | Trend pullback · 1h | trend | 96.80 | -3.20 | 26 | 11.5 | -25.08 | -6.68 | -26.16 | 145 |
| 41 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 131 | 10.7 | -0.65 | 0.03 | -12.45 | 391 |
| 42 | Max aggression: 1-day momentum | meta | 96.52 | -3.48 | 2 | 0.0 | -38.15 | -2.27 | -49.44 | 42 |
| 43 | Donchian 55/20 · 1h | breakout | 96.46 | -3.54 | 12 | 0.0 | 5.02 | 0.86 | -16.96 | 112 |
| 44 | MACD cross · 1h | trend | 96.22 | -3.77 | 40 | 10.0 | -18.48 | -3.15 | -21.60 | 459 |
| 45 | Parabolic SAR · 1h | trend | 96.16 | -3.84 | 26 | 11.5 | -7.84 | -0.98 | -18.82 | 292 |
| 46 | MFI reversion · 1h | reversion | 95.63 | -4.37 | 44 | 13.6 | -8.12 | -1.43 | -16.99 | 128 |
| 47 | Ichimoku · 1h | trend | 95.58 | -4.42 | 16 | 18.8 | 7.27 | 1.04 | -15.13 | 122 |
| 48 | Opening range 15m | breakout | 95.52 | -4.49 | 47 | 10.6 | -11.06 | -2.98 | -16.91 | 696 |
| 49 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -51.31 | -28.11 | -51.45 | 611 |
| 50 | Bollinger breakout · 1h | breakout | 95.00 | -5.00 | 17 | 5.9 | 6.55 | 1.05 | -11.06 | 284 |
| 51 | RSI momentum · 1h | momentum | 94.78 | -5.22 | 24 | 4.2 | -0.64 | 0.11 | -15.29 | 211 |
| 52 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.82 | 0.99 | -12.60 | 125 |
| 53 | ADX DI cross · 1h | trend | 94.54 | -5.46 | 29 | 6.9 | -16.20 | -3.08 | -18.17 | 256 |
| 54 | Triple EMA stack · 1h | trend | 94.34 | -5.66 | 29 | 6.9 | -6.00 | -0.52 | -22.92 | 226 |
| 55 | MACD zero-line · 1h | trend | 94.27 | -5.73 | 20 | 5.0 | -5.88 | -0.64 | -14.64 | 223 |
| 56 | Donchian 20/10 · 1h | breakout | 94.05 | -5.95 | 16 | 12.5 | 7.48 | 1.14 | -12.78 | 214 |
| 57 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | -8.07 | -0.94 | -18.68 | 215 |
| 58 | VWAP momentum · 1h | momentum | 93.86 | -6.14 | 102 | 12.7 | -33.08 | -5.00 | -35.30 | 1227 |
| 59 | EMA 9/21 cross · 1h | trend | 93.61 | -6.39 | 42 | 11.9 | -4.61 | -0.44 | -16.92 | 311 |
| 60 | OBV trend · 1h | momentum | 93.01 | -6.99 | 54 | 7.4 | -9.50 | -1.00 | -25.24 | 326 |
| 61 | Heikin-Ashi · 1h | trend | 92.70 | -7.30 | 43 | 11.6 | -23.74 | -3.57 | -30.54 | 678 |
| 62 | RSI(14) reversion | reversion | 91.16 | -8.84 | 115 | 35.7 | -71.18 | -21.77 | -71.33 | 1468 |
| 63 | Squeeze breakout | breakout | 90.01 | -9.99 | 81 | 9.9 | -59.80 | -18.54 | -60.20 | 1194 |
| 64 | ROC + volume · 1h | momentum | 89.32 | -10.68 | 51 | 5.9 | -4.85 | -0.42 | -19.28 | 406 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | EMA 20/50 cross | trend | 87.91 | -12.09 | 107 | 15.0 | -78.55 | -17.51 | -78.75 | 1466 |
| 68 | Volume breakout | breakout | 87.72 | -12.28 | 95 | 13.7 | -61.69 | -20.46 | -61.98 | 892 |
| 69 | ROC + volume | momentum | 87.72 | -12.28 | 137 | 17.5 | -72.47 | -18.20 | -72.65 | 1615 |
| 70 | Donchian 55/20 | breakout | 87.31 | -12.70 | 92 | 14.1 | -68.49 | -15.73 | -68.53 | 1308 |
| 71 | Ichimoku | trend | 86.25 | -13.75 | 106 | 8.5 | -80.51 | -26.19 | -80.56 | 1752 |
| 72 | Keltner breakout | breakout | 85.83 | -14.17 | 138 | 11.6 | -84.87 | -34.77 | -84.96 | 1901 |
| 73 | Z-score reversion | reversion | 85.24 | -14.77 | 177 | 32.8 | -84.35 | -27.61 | -84.41 | 2092 |
| 74 | VWAP reversion | reversion | 85.01 | -14.99 | 127 | 19.7 | -71.91 | -17.72 | -72.20 | 1403 |
| 75 | MACD zero-line | trend | 83.65 | -16.36 | 175 | 14.9 | -91.67 | -36.24 | -91.72 | 2358 |
| 76 | Supertrend | trend | 82.93 | -17.07 | 160 | 16.2 | -87.40 | -24.94 | -87.42 | 1967 |
| 77 | MFI reversion | reversion | 81.86 | -18.14 | 173 | 19.1 | -87.59 | -35.62 | -87.68 | 2153 |
| 78 | Donchian 20/10 | breakout | 81.74 | -18.26 | 181 | 16.6 | -90.82 | -29.85 | -90.87 | 2686 |
| 79 | Bollinger breakout | breakout | 81.51 | -18.49 | 187 | 14.4 | -93.94 | -42.17 | -93.98 | 2869 |
| 80 | Triple EMA stack | trend | 81.37 | -18.63 | 195 | 14.9 | -93.03 | -36.41 | -93.09 | 2613 |
| 81 | RSI momentum | momentum | 81.05 | -18.95 | 175 | 11.4 | -90.54 | -29.80 | -90.59 | 2401 |
| 82 | ADX DI cross | trend | 80.35 | -19.65 | 182 | 6.6 | -89.49 | -47.56 | -89.54 | 2115 |
| 83 | Trend pullback | trend | 79.75 | -20.25 | 167 | 17.4 | -90.94 | -35.31 | -90.94 | 2285 |
| 84 | EMA 9/21 cross | trend | 78.35 | -21.66 | 253 | 15.0 | -97.39 | -41.75 | -97.41 | 3546 |
| 85 | Connors RSI(2) | reversion | 77.12 | -22.88 | 240 | 16.2 | -96.47 | -43.11 | -96.47 | 3645 |
| 86 | Consensus | meta | 77.05 | -22.95 | 183 | 7.1 | -94.67 | -30.75 | -94.68 | 2649 |
| 87 | Stochastic reversion | reversion | 76.55 | -23.45 | 318 | 24.8 | -95.90 | -47.20 | -95.91 | 4065 |
| 88 | OBV trend | momentum | 76.25 | -23.75 | 255 | 14.5 | -95.95 | -49.05 | -95.97 | 3530 |
| 89 | Candlestick reversal ⏸ | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.34 | -51.02 | -99.34 | 5569 |
| 90 | Bollinger reversion | reversion | 75.15 | -24.85 | 299 | 15.7 | -95.75 | -45.38 | -95.76 | 3683 |
| 91 | VWAP momentum | momentum | 74.36 | -25.64 | 350 | 9.7 | -98.42 | -36.30 | -98.42 | 5175 |
| 92 | CCI reversion | reversion | 74.15 | -25.85 | 227 | 11.9 | -98.44 | -52.12 | -98.45 | 4700 |
| 93 | MACD cross | trend | 72.91 | -27.09 | 241 | 12.0 | -99.71 | -67.50 | -99.71 | 6085 |
| 94 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -97.01 | -56.64 | -97.02 | 3645 |
| 95 | Williams %R | reversion | 71.91 | -28.09 | 335 | 21.5 | -99.52 | -61.57 | -99.52 | 6106 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -91.63 | -99.89 | 8315 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T18:40 | Consensus | buy | NVDA | 19.27 | — | entry |
| 2026-09-29T18:40 | MFI reversion · 1h | buy | TNA | 18.49 | — | rebalance up |
| 2026-09-29T18:40 | MFI reversion · 1h | buy | LABU | 4.87 | — | rebalance up |
| 2026-09-29T18:40 | MFI reversion · 1h | sell | MSTR | 23.44 | 0.03 | target is flat |
| 2026-09-29T18:40 | MFI reversion | buy | TSLA | 4.18 | — | rebalance up |
| 2026-09-29T18:40 | MFI reversion | buy | TECL | 7.52 | — | rebalance up |
| 2026-09-29T18:40 | MFI reversion | sell | ETH-USD | 11.70 | -0.01 | exit signal |
| 2026-09-29T18:40 | CCI reversion | buy | PLTR | 3.71 | — | rebalance up |
| 2026-09-29T18:40 | CCI reversion | buy | NVDA | 3.72 | — | rebalance up |
| 2026-09-29T18:40 | CCI reversion | buy | COIN | 3.73 | — | rebalance up |
| 2026-09-29T18:40 | CCI reversion | buy | AMD | 3.71 | — | rebalance up |
| 2026-09-29T18:40 | CCI reversion | sell | MSFT | 14.87 | 0.08 | exit signal |
| 2026-09-29T18:40 | Williams %R | buy | NVDA | 5.98 | — | rebalance up |
| 2026-09-29T18:40 | Williams %R | buy | AMD | 5.97 | — | rebalance up |
| 2026-09-29T18:40 | Williams %R | buy | AAPL | 6.00 | — | rebalance up |
| 2026-09-29T18:40 | Williams %R | sell | SQQQ | 11.93 | -0.09 | stop-loss |
| 2026-09-29T18:40 | Williams %R | sell | PLTR | 12.01 | 0.01 | exit signal |
| 2026-09-29T18:40 | Stochastic reversion | sell | PLTR | 15.35 | 0.03 | exit signal |
| 2026-09-29T18:40 | VWAP reversion | buy | NVDA | 8.50 | — | entry |
| 2026-09-29T18:40 | VWAP reversion | sell | UPRO | 7.73 | 0.06 | exit signal |
| 2026-09-29T18:40 | VWAP reversion | sell | SPY | 7.70 | 0.01 | exit signal |
| 2026-09-29T18:40 | Z-score reversion | sell | PLTR | 21.34 | -0.02 | exit signal |
| 2026-09-29T18:40 | RSI(14) reversion | sell | PLTR | 22.81 | 0.02 | exit signal |
| 2026-09-29T18:40 | Keltner breakout | buy | UPRO | 9.49 | — | entry signal |
| 2026-09-29T18:40 | Keltner breakout | buy | TNA | 9.54 | — | entry signal |
| 2026-09-29T18:40 | Keltner breakout | buy | SPY | 9.54 | — | entry signal |
| 2026-09-29T18:40 | Keltner breakout | buy | MSFT | 9.54 | — | entry signal |
| 2026-09-29T18:40 | Keltner breakout | buy | GOOGL | 9.54 | — | entry signal |
| 2026-09-29T18:40 | Keltner breakout | sell | META | 11.96 | 0.08 | rebalance down |
| 2026-09-29T18:40 | Keltner breakout | sell | LABU | 12.07 | 0.12 | rebalance down |
| 2026-09-29T18:40 | Keltner breakout | sell | BTC-USD | 11.70 | -0.07 | rebalance down |
| 2026-09-29T18:40 | Keltner breakout | sell | BITX | 11.94 | 0.01 | rebalance down |
| 2026-09-29T18:40 | Donchian 55/20 | buy | GOOGL | 21.74 | — | entry signal |
| 2026-09-29T18:40 | Donchian 55/20 | buy | AMZN | 21.83 | — | entry signal |
| 2026-09-29T18:40 | Donchian 20/10 | buy | XRP-USD | 3.20 | — | entry |
| 2026-09-29T18:40 | Donchian 20/10 | buy | UPRO | 4.09 | — | entry signal |
| 2026-09-29T18:40 | Donchian 20/10 | buy | TQQQ | 4.09 | — | entry signal |
| 2026-09-29T18:40 | Donchian 20/10 | buy | SOL-USD | 4.09 | — | entry |
| 2026-09-29T18:40 | Donchian 20/10 | buy | QQQ | 4.09 | — | entry signal |
| 2026-09-29T18:40 | Donchian 20/10 | buy | MSTR | 4.09 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
