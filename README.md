# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T19:10:05.000138+00:00 · 6005 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.91 (-0.09%)

Closed trades 23, win rate 69.6%, fees £0.69, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 39.89 | -0.06 |
| COIN | 20.01 | +0.03 |

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

Today: 33540 decisions in 2777 calls, $0.4152 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T19:10 | 4 / 12 / 14 | LABU 17%, TECL 15%, XRP-USD 14%, SQQQ 13% |  |
| Breezy | 2026-09-29T19:10 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-09-29T19:10 | 12 / 14 / 4 | MSTR 38%, COIN 37% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.20 | 1.20 | 1 | 100.0 | 13.81 | 3.01 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -1.88 | -0.52 | -9.74 | 24 |
| 4 | Hold BTC | benchmark | 100.22 | 0.22 | 0 | — | 31.21 | 3.91 | -8.68 | 1 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.15 | 0.15 | 0 | — | 6.85 | 2.83 | -3.62 | 1 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.42 | 1.40 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent (aggressive) | meta | 99.92 | -0.08 | 9 | 55.6 | -0.20 | -0.08 | -3.92 | 97 |
| 10 | Agent | meta | 99.91 | -0.09 | 23 | 69.6 | -10.13 | -6.82 | -10.72 | 216 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 99.88 | -0.12 | 0 | — | -0.47 | -0.13 | -7.65 | 1 |
| 12 | Hold SPY | benchmark | 99.71 | -0.29 | 0 | — | 3.80 | 2.11 | -3.66 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.13 | 1.60 | -1.88 | 83 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 99.64 | -0.36 | 0 | — | -3.37 | -2.06 | -5.09 | 2 |
| 15 | Daily: Bullish score | daily | 99.58 | -0.42 | 2 | 0.0 | -0.98 | 0.06 | -12.76 | 13 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.50 | -0.50 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 17 | VWAP reversion · 1h | reversion | 99.33 | -0.67 | 20 | 25.0 | -12.93 | -4.39 | -14.85 | 122 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | RSI(14) reversion · 1h | reversion | 99.13 | -0.87 | 7 | 57.1 | 13.06 | 2.52 | -6.57 | 137 |
| 20 | Williams %R · 1h | reversion | 98.97 | -1.03 | 40 | 45.0 | -17.88 | -3.32 | -19.57 | 484 |
| 21 | Z-score reversion · 1h | reversion | 98.93 | -1.07 | 10 | 50.0 | 4.50 | 1.10 | -8.60 | 154 |
| 22 | Candlestick reversal · 1h | reversion | 98.87 | -1.13 | 20 | 25.0 | -26.77 | -6.48 | -27.60 | 496 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 98.66 | -1.34 | 0 | — | 25.17 | 3.69 | -6.29 | 1 |
| 25 | Stochastic reversion · 1h | reversion | 98.66 | -1.34 | 26 | 53.8 | -13.47 | -3.01 | -14.66 | 325 |
| 26 | CCI reversion · 1h | reversion | 98.53 | -1.47 | 35 | 34.3 | 2.56 | 0.59 | -12.41 | 406 |
| 27 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.49 | 3.84 | -4.73 | 193 |
| 28 | Copy: Insider buying | copy | 98.44 | -1.56 | 2 | 100.0 | -14.78 | -2.95 | -17.74 | 72 |
| 29 | Max aggression: 5-day momentum | meta | 98.42 | -1.58 | 2 | 50.0 | -8.05 | -0.39 | -29.56 | 29 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.75 | -0.09 | -15.21 | 47 |
| 31 | EMA 20/50 cross · 1h | trend | 98.22 | -1.78 | 11 | 9.1 | 16.40 | 1.97 | -14.36 | 127 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 98.18 | -1.82 | 0 | — | -10.92 | -2.24 | -15.27 | 2 |
| 33 | Connors RSI(2) · 1h | reversion | 98.15 | -1.84 | 42 | 45.2 | -11.34 | -3.65 | -11.79 | 235 |
| 34 | Agent (rotation) | meta | 97.90 | -2.10 | 32 | 12.5 | -6.41 | -2.21 | -11.49 | 229 |
| 35 | Bollinger reversion · 1h | reversion | 97.33 | -2.67 | 22 | 27.3 | -17.90 | -5.01 | -18.44 | 312 |
| 36 | Squeeze breakout · 1h | breakout | 97.20 | -2.80 | 9 | 11.1 | 10.32 | 1.80 | -11.22 | 100 |
| 37 | Opening range 30m | breakout | 97.10 | -2.90 | 36 | 11.1 | -9.07 | -2.61 | -14.21 | 563 |
| 38 | Daily: SMA 20/50 cross · AAPL | daily | 97.08 | -2.92 | 0 | — | -10.48 | -2.57 | -12.28 | 1 |
| 39 | Supertrend · 1h | trend | 96.93 | -3.07 | 18 | 5.6 | 2.84 | 0.58 | -16.43 | 190 |
| 40 | Trend pullback · 1h | trend | 96.89 | -3.11 | 26 | 11.5 | -24.92 | -6.60 | -26.21 | 148 |
| 41 | Agent (ML meta-label) | meta | 96.73 | -3.27 | 132 | 11.4 | 1.06 | 0.35 | -12.21 | 381 |
| 42 | Max aggression: 1-day momentum | meta | 96.58 | -3.42 | 2 | 0.0 | -38.12 | -2.27 | -49.44 | 42 |
| 43 | Donchian 55/20 · 1h | breakout | 96.40 | -3.60 | 12 | 0.0 | 4.96 | 0.85 | -16.96 | 112 |
| 44 | MACD cross · 1h | trend | 96.29 | -3.71 | 40 | 10.0 | -18.93 | -3.24 | -22.09 | 460 |
| 45 | Parabolic SAR · 1h | trend | 96.17 | -3.83 | 26 | 11.5 | -7.66 | -0.95 | -18.82 | 292 |
| 46 | MFI reversion · 1h | reversion | 95.71 | -4.29 | 44 | 13.6 | -8.08 | -1.42 | -16.99 | 129 |
| 47 | Opening range 15m | breakout | 95.50 | -4.50 | 47 | 10.6 | -10.83 | -2.93 | -16.70 | 695 |
| 48 | Ichimoku · 1h | trend | 95.48 | -4.52 | 16 | 18.8 | 7.17 | 1.03 | -15.13 | 122 |
| 49 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -51.31 | -28.11 | -51.45 | 611 |
| 50 | Bollinger breakout · 1h | breakout | 95.00 | -5.00 | 17 | 5.9 | 6.69 | 1.07 | -11.16 | 283 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.72 | 0.98 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.70 | -5.30 | 24 | 4.2 | -0.58 | 0.12 | -15.29 | 211 |
| 53 | ADX DI cross · 1h | trend | 94.40 | -5.60 | 29 | 6.9 | -15.80 | -2.99 | -17.79 | 253 |
| 54 | Triple EMA stack · 1h | trend | 94.30 | -5.70 | 29 | 6.9 | -6.92 | -0.64 | -22.92 | 229 |
| 55 | MACD zero-line · 1h | trend | 94.27 | -5.73 | 20 | 5.0 | -6.03 | -0.66 | -14.64 | 224 |
| 56 | Donchian 20/10 · 1h | breakout | 94.06 | -5.94 | 16 | 12.5 | 7.57 | 1.15 | -12.78 | 214 |
| 57 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | -8.00 | -0.92 | -18.68 | 216 |
| 58 | VWAP momentum · 1h | momentum | 93.91 | -6.09 | 102 | 12.7 | -33.40 | -5.07 | -35.20 | 1228 |
| 59 | EMA 9/21 cross · 1h | trend | 93.64 | -6.36 | 42 | 11.9 | -4.05 | -0.36 | -16.92 | 309 |
| 60 | OBV trend · 1h | momentum | 92.90 | -7.10 | 54 | 7.4 | -9.58 | -1.01 | -25.24 | 327 |
| 61 | Heikin-Ashi · 1h | trend | 92.71 | -7.29 | 43 | 11.6 | -23.76 | -3.57 | -30.58 | 678 |
| 62 | RSI(14) reversion | reversion | 91.09 | -8.91 | 116 | 35.3 | -71.18 | -21.74 | -71.32 | 1473 |
| 63 | Squeeze breakout | breakout | 90.10 | -9.90 | 81 | 9.9 | -59.68 | -18.53 | -60.06 | 1192 |
| 64 | ROC + volume · 1h | momentum | 89.32 | -10.68 | 51 | 5.9 | -4.81 | -0.41 | -19.29 | 406 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | EMA 20/50 cross | trend | 87.86 | -12.14 | 108 | 14.8 | -78.51 | -17.50 | -78.71 | 1470 |
| 68 | ROC + volume | momentum | 87.83 | -12.17 | 139 | 18.0 | -72.39 | -18.16 | -72.58 | 1611 |
| 69 | Volume breakout | breakout | 87.73 | -12.28 | 96 | 13.5 | -62.08 | -20.65 | -62.35 | 894 |
| 70 | Donchian 55/20 | breakout | 87.35 | -12.65 | 92 | 14.1 | -68.50 | -15.73 | -68.57 | 1308 |
| 71 | Ichimoku | trend | 86.30 | -13.70 | 106 | 8.5 | -80.44 | -26.19 | -80.50 | 1750 |
| 72 | Keltner breakout | breakout | 85.86 | -14.14 | 138 | 11.6 | -85.12 | -34.50 | -85.20 | 1910 |
| 73 | Z-score reversion | reversion | 85.24 | -14.77 | 178 | 33.1 | -84.35 | -27.61 | -84.42 | 2092 |
| 74 | VWAP reversion | reversion | 85.03 | -14.97 | 128 | 20.3 | -71.91 | -17.70 | -72.25 | 1403 |
| 75 | MACD zero-line | trend | 83.64 | -16.36 | 177 | 15.8 | -91.68 | -36.08 | -91.73 | 2362 |
| 76 | Supertrend | trend | 83.02 | -16.98 | 160 | 16.2 | -87.45 | -24.89 | -87.49 | 1963 |
| 77 | Donchian 20/10 | breakout | 81.83 | -18.17 | 181 | 16.6 | -90.92 | -29.70 | -90.98 | 2686 |
| 78 | MFI reversion | reversion | 81.71 | -18.29 | 177 | 19.8 | -87.86 | -36.38 | -87.93 | 2151 |
| 79 | Bollinger breakout | breakout | 81.57 | -18.43 | 187 | 14.4 | -93.96 | -42.23 | -94.00 | 2871 |
| 80 | Triple EMA stack | trend | 81.31 | -18.69 | 195 | 14.9 | -93.07 | -36.39 | -93.11 | 2619 |
| 81 | RSI momentum | momentum | 81.11 | -18.89 | 175 | 11.4 | -90.55 | -29.84 | -90.60 | 2400 |
| 82 | ADX DI cross | trend | 80.46 | -19.54 | 184 | 7.1 | -89.22 | -46.88 | -89.28 | 2104 |
| 83 | Trend pullback | trend | 79.67 | -20.33 | 167 | 17.4 | -91.02 | -35.19 | -91.02 | 2283 |
| 84 | EMA 9/21 cross | trend | 78.41 | -21.59 | 253 | 15.0 | -97.42 | -41.60 | -97.44 | 3546 |
| 85 | Connors RSI(2) | reversion | 77.12 | -22.88 | 241 | 16.6 | -96.47 | -43.08 | -96.47 | 3645 |
| 86 | Consensus | meta | 77.06 | -22.94 | 184 | 7.1 | -94.65 | -30.74 | -94.66 | 2651 |
| 87 | Stochastic reversion | reversion | 76.50 | -23.50 | 318 | 24.8 | -95.92 | -47.32 | -95.93 | 4060 |
| 88 | OBV trend | momentum | 76.24 | -23.76 | 255 | 14.5 | -95.91 | -49.06 | -95.94 | 3526 |
| 89 | Candlestick reversal ⏸ | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.34 | -50.69 | -99.34 | 5575 |
| 90 | Bollinger reversion | reversion | 75.16 | -24.84 | 300 | 16.0 | -95.76 | -45.47 | -95.77 | 3681 |
| 91 | VWAP momentum | momentum | 74.38 | -25.62 | 350 | 9.7 | -98.43 | -36.32 | -98.44 | 5176 |
| 92 | CCI reversion | reversion | 74.07 | -25.93 | 228 | 11.8 | -98.44 | -51.87 | -98.45 | 4695 |
| 93 | MACD cross | trend | 72.92 | -27.08 | 245 | 12.7 | -99.71 | -67.29 | -99.71 | 6084 |
| 94 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -96.99 | -56.84 | -97.01 | 3644 |
| 95 | Williams %R | reversion | 71.81 | -28.19 | 335 | 21.5 | -99.52 | -61.21 | -99.52 | 6105 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -92.17 | -99.89 | 8311 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T19:10 | Consensus | sell | NVDA | 19.24 | -0.03 | target is flat |
| 2026-09-29T19:10 | VWAP reversion · 1h | buy | AMD | 24.84 | — | entry |
| 2026-09-29T19:10 | CCI reversion | buy | SQQQ | 18.52 | — | entry signal |
| 2026-09-29T19:10 | Z-score reversion | sell | XRP-USD | 17.12 | 0.08 | exit signal |
| 2026-09-29T19:10 | Connors RSI(2) | sell | SQQQ | 19.28 | 0.00 | exit signal |
| 2026-09-29T19:10 | Volume breakout | sell | LABU | 12.56 | 0.00 | target is flat |
| 2026-09-29T19:05 | MFI reversion · 1h | buy | TSLA | 4.79 | — | rebalance up |
| 2026-09-29T19:05 | MFI reversion · 1h | sell | TNA | 4.79 | 0.00 | rebalance down |
| 2026-09-29T19:05 | MFI reversion | buy | SQQQ | 6.82 | — | rebalance up |
| 2026-09-29T19:05 | MFI reversion | buy | SOXL | 4.12 | — | rebalance up |
| 2026-09-29T19:05 | MFI reversion | sell | TECL | 16.35 | -0.00 | exit signal |
| 2026-09-29T19:05 | VWAP reversion | sell | IWM | 7.71 | 0.02 | exit signal |
| 2026-09-29T19:05 | RSI momentum | buy | SPY | 4.06 | — | entry |
| 2026-09-29T19:05 | RSI momentum | buy | DOGE-USD | 4.06 | — | entry |
| 2026-09-29T19:05 | RSI momentum | sell | SOL-USD | 4.09 | -0.00 | rebalance down |
| 2026-09-29T19:05 | RSI momentum | sell | BITX | 4.08 | 0.02 | rebalance down |
| 2026-09-29T19:05 | ROC + volume | buy | ETH-USD | 8.79 | — | entry |
| 2026-09-29T19:05 | ROC + volume | sell | META | 9.74 | 0.08 | exit signal |
| 2026-09-29T19:05 | MACD zero-line | buy | MSTR | 2.25 | — | entry |
| 2026-09-29T19:05 | MACD zero-line | buy | MSFT | 4.18 | — | entry |
| 2026-09-29T19:05 | MACD zero-line | sell | META | 6.43 | 0.07 | exit signal |
| 2026-09-29T19:05 | MACD cross | buy | NVDA | 2.40 | — | entry |
| 2026-09-29T19:05 | MACD cross | buy | MSFT | 3.32 | — | entry |
| 2026-09-29T19:05 | MACD cross | sell | META | 1.71 | 0.02 | exit signal |
| 2026-09-29T19:05 | MACD cross | sell | AMD | 3.01 | -0.01 | exit signal |
| 2026-09-29T19:00 | Consensus | buy | ETHU | 19.10 | — | entry |
| 2026-09-29T19:00 | Williams %R · 1h | buy | DOGE-USD | 7.03 | — | entry signal |
| 2026-09-29T19:00 | Williams %R · 1h | buy | BTC-USD | 7.07 | — | entry signal |
| 2026-09-29T19:00 | Candlestick reversal · 1h | buy | ETH-USD | 4.21 | — | entry signal |
| 2026-09-29T19:00 | OBV trend · 1h | buy | ETHU | 23.25 | — | entry |
| 2026-09-29T19:00 | Trend pullback · 1h | buy | ETH-USD | 9.13 | — | entry signal |
| 2026-09-29T19:00 | Trend pullback · 1h | buy | AMD | 6.59 | — | rebalance up |
| 2026-09-29T19:00 | Trend pullback · 1h | sell | META | 8.01 | 0.01 | rebalance down |
| 2026-09-29T19:00 | Trend pullback · 1h | sell | ETHU | 7.71 | 0.05 | rebalance down |
| 2026-09-29T19:00 | MFI reversion | buy | TECL | 6.12 | — | rebalance up |
| 2026-09-29T19:00 | MFI reversion | buy | SOXL | 4.64 | — | rebalance up |
| 2026-09-29T19:00 | MFI reversion | buy | PLTR | 6.11 | — | rebalance up |
| 2026-09-29T19:00 | MFI reversion | buy | NVDA | 6.15 | — | rebalance up |
| 2026-09-29T19:00 | MFI reversion | sell | XRP-USD | 11.71 | 0.04 | exit signal |
| 2026-09-29T19:00 | Bollinger reversion | sell | NVDA | 18.81 | 0.00 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
