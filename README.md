# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T15:35:05.000179+00:00 · 12597 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £98.87 (-1.13%)

Closed trades 33, win rate 66.7%, fees £1.09, max drawdown -1.63%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 19.79 | -0.11 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-05 | SLBT 12%, KOD 12%, ADRX 12%, GME 12%, BPRE 12%, PAM 12%, CX 12%, GPUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 18112 decisions in 2315 calls, $0.2353 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T15:35 | 1 / 13 / 15 | TNA 14% |  |
| Breezy | 2026-10-05T15:35 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-10-05T15:35 | 1 / 26 / 2 | MSTR 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.58 | +4.45% | 4 |
| VWAP reversion | AMZN | 1.94 | +0.87% | 3 |
| VWAP reversion | TECL | 1.77 | +2.87% | 3 |
| Z-score reversion | SQQQ | 1.74 | +3.40% | 6 |
| RSI(14) reversion | SQQQ | 1.71 | +3.09% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 103.87 | 3.87 | 0 | — | -5.65 | -0.97 | -15.27 | 2 |
| 2 | VWAP reversion · 1h | reversion | 102.52 | 2.52 | 28 | 42.9 | -7.92 | -2.48 | -14.05 | 112 |
| 3 | Hold BTC | benchmark | 102.06 | 2.06 | 0 | — | 32.97 | 3.99 | -8.68 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 5 | Timing: Nasdaq FTD · QQQ | daily | 101.53 | 1.53 | 0 | — | -1.43 | -0.77 | -5.09 | 2 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.29 | 1.29 | 0 | — | 1.99 | 0.99 | -3.62 | 1 |
| 7 | Copy: Cathie Wood (ARKK) | copy | 101.07 | 1.07 | 0 | — | 20.42 | 3.17 | -6.29 | 1 |
| 8 | Daily: Bullish score | daily | 100.96 | 0.96 | 3 | 0.0 | 3.54 | 0.67 | -12.76 | 12 |
| 9 | Hold SPY | benchmark | 100.69 | 0.69 | 0 | — | 0.41 | 0.30 | -3.66 | 1 |
| 10 | Candlestick reversal · 1h | reversion | 100.64 | 0.64 | 55 | 36.4 | -22.92 | -5.21 | -24.82 | 488 |
| 11 | Bollinger reversion · 1h | reversion | 100.30 | 0.30 | 43 | 44.2 | -14.26 | -3.71 | -17.47 | 301 |
| 12 | RSI(14) reversion · 1h | reversion | 100.28 | 0.28 | 11 | 63.6 | 2.72 | 0.82 | -6.57 | 121 |
| 13 | Donchian 55/20 · 1h | breakout | 100.21 | 0.20 | 17 | 0.0 | 7.09 | 1.07 | -16.96 | 109 |
| 14 | Z-score reversion · 1h | reversion | 100.18 | 0.18 | 20 | 55.0 | 6.94 | 1.56 | -8.60 | 155 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 100.06 | 0.06 | 20 | 35.0 | 4.44 | 2.16 | -1.46 | 86 |
| 16 | Copy: Warren Buffett (BRK-B) | copy | 100.04 | 0.04 | 0 | — | -2.24 | -0.86 | -7.65 | 1 |
| 17 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 18 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 19 | Connors RSI(2) · 1h | reversion | 99.97 | -0.03 | 68 | 45.6 | -12.71 | -4.43 | -16.84 | 221 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 99.76 | -0.24 | 0 | — | -2.68 | -1.29 | -5.14 | 1 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.75 | -0.25 | 5 | 20.0 | 5.02 | 1.56 | -7.55 | 43 |
| 22 | Trend pullback · 1h | trend | 99.28 | -0.72 | 55 | 21.8 | -19.05 | -5.44 | -23.10 | 160 |
| 23 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.25 | -0.27 | -1.79 | 19 |
| 24 | Stochastic reversion · 1h | reversion | 99.23 | -0.77 | 47 | 61.7 | -7.81 | -1.60 | -10.60 | 327 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.21 | -0.79 | 3 | 33.3 | 1.01 | 0.47 | -4.03 | 18 |
| 26 | EMA 20/50 cross · 1h | trend | 98.91 | -1.09 | 26 | 7.7 | 12.41 | 1.58 | -15.34 | 139 |
| 27 | Agent | meta | 98.87 | -1.13 | 33 | 66.7 | -9.84 | -6.45 | -10.43 | 220 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 29 | CCI reversion · 1h | reversion | 98.27 | -1.73 | 65 | 49.2 | 0.23 | 0.20 | -12.41 | 406 |
| 30 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -3.97 | -2.03 | -6.00 | 104 |
| 31 | Williams %R · 1h | reversion | 98.03 | -1.97 | 72 | 55.6 | -16.40 | -2.87 | -19.58 | 500 |
| 32 | Daily: Momentum burst | daily | 98.01 | -1.99 | 3 | 0.0 | -0.62 | 0.08 | -16.91 | 44 |
| 33 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.86 | -2.14 | 3 | 33.3 | -5.79 | -2.09 | -9.74 | 24 |
| 34 | Daily: SMA 20/50 cross · AAPL | daily | 97.84 | -2.16 | 0 | — | 0.95 | 0.45 | -5.18 | 1 |
| 35 | Agent (rotation) | meta | 97.84 | -2.16 | 55 | 25.5 | -0.69 | -0.11 | -10.38 | 253 |
| 36 | Agent (ML meta-label) | meta | 97.08 | -2.92 | 223 | 16.1 | -1.84 | -0.19 | -12.61 | 382 |
| 37 | Parabolic SAR · 1h | trend | 96.56 | -3.44 | 59 | 16.9 | -5.22 | -0.52 | -19.61 | 296 |
| 38 | ADX DI cross · 1h | trend | 96.53 | -3.47 | 41 | 12.2 | -4.88 | -0.66 | -13.84 | 263 |
| 39 | Copy: Insider buying | copy | 96.45 | -3.55 | 6 | 50.0 | -19.09 | -3.76 | -21.08 | 73 |
| 40 | Supertrend · 1h | trend | 96.26 | -3.74 | 30 | 10.0 | 2.48 | 0.52 | -16.43 | 207 |
| 41 | MACD cross · 1h | trend | 95.86 | -4.13 | 79 | 19.0 | -7.21 | -0.99 | -17.27 | 472 |
| 42 | Squeeze breakout · 1h | breakout | 95.21 | -4.79 | 27 | 22.2 | 13.04 | 2.25 | -8.06 | 110 |
| 43 | MFI reversion · 1h | reversion | 95.05 | -4.95 | 73 | 27.4 | -9.97 | -1.74 | -16.99 | 119 |
| 44 | Gap and go | momentum | 95.03 | -4.97 | 39 | 7.7 | 6.47 | 1.71 | -5.79 | 195 |
| 45 | RSI momentum · 1h | momentum | 94.73 | -5.27 | 43 | 2.3 | 0.56 | 0.27 | -16.65 | 228 |
| 46 | Ichimoku · 1h | trend | 94.26 | -5.74 | 30 | 16.7 | 6.07 | 0.92 | -15.84 | 123 |
| 47 | Opening range 30m | breakout | 94.22 | -5.78 | 76 | 17.1 | -16.24 | -5.05 | -17.14 | 554 |
| 48 | Triple EMA stack · 1h | trend | 93.71 | -6.29 | 53 | 11.3 | -9.10 | -0.94 | -24.08 | 243 |
| 49 | Bollinger breakout · 1h | breakout | 93.67 | -6.33 | 46 | 26.1 | 3.86 | 0.69 | -12.06 | 297 |
| 50 | Max aggression: 1-day momentum | meta | 93.47 | -6.53 | 6 | 33.3 | -28.55 | -1.62 | -39.72 | 42 |
| 51 | Volume breakout · 1h | breakout | 93.00 | -7.00 | 32 | 9.4 | 5.09 | 0.89 | -12.60 | 130 |
| 52 | Opening range 15m | breakout | 92.47 | -7.53 | 93 | 16.1 | -19.00 | -5.69 | -19.24 | 687 |
| 53 | EMA 9/21 cross · 1h | trend | 92.24 | -7.75 | 71 | 12.7 | -5.02 | -0.49 | -18.47 | 346 |
| 54 | MACD zero-line · 1h | trend | 91.43 | -8.57 | 42 | 16.7 | 0.88 | 0.32 | -18.32 | 243 |
| 55 | VWAP momentum · 1h | momentum | 91.18 | -8.82 | 194 | 22.2 | -39.61 | -6.14 | -39.72 | 1275 |
| 56 | Donchian 20/10 · 1h | breakout | 91.15 | -8.85 | 34 | 17.6 | -0.76 | 0.12 | -16.18 | 224 |
| 57 | Three white soldiers | momentum | 90.74 | -9.26 | 83 | 16.9 | -49.78 | -26.38 | -49.88 | 582 |
| 58 | Heikin-Ashi · 1h | trend | 90.53 | -9.47 | 99 | 25.3 | -31.94 | -5.58 | -34.14 | 690 |
| 59 | Max aggression: 5-day momentum | meta | 90.50 | -9.50 | 5 | 40.0 | -22.17 | -1.99 | -29.56 | 30 |
| 60 | OBV trend · 1h | momentum | 89.85 | -10.15 | 101 | 10.9 | -14.04 | -1.60 | -26.78 | 335 |
| 61 | Keltner breakout · 1h | breakout | 88.48 | -11.52 | 30 | 6.7 | -14.25 | -1.74 | -23.27 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.26 | -12.74 | 94 | 14.9 | -12.71 | -1.63 | -23.18 | 418 |
| 63 | RSI(14) reversion | reversion | 86.37 | -13.63 | 196 | 33.7 | -70.44 | -19.65 | -70.57 | 1428 |
| 64 | VWAP reversion | reversion | 78.31 | -21.69 | 225 | 28.4 | -69.53 | -16.73 | -69.53 | 1361 |
| 65 | Squeeze breakout | breakout | 78.21 | -21.79 | 219 | 13.2 | -62.87 | -19.55 | -62.95 | 1220 |
| 66 | Donchian 55/20 | breakout | 76.80 | -23.20 | 219 | 15.5 | -69.49 | -15.72 | -69.59 | 1295 |
| 67 | ROC + volume | momentum | 76.77 | -23.23 | 288 | 19.1 | -74.71 | -18.60 | -74.76 | 1665 |
| 68 | Volume breakout | breakout | 75.14 | -24.86 | 191 | 11.5 | -65.02 | -20.19 | -65.02 | 919 |
| 69 | EMA 20/50 cross | trend | 75.08 | -24.92 | 241 | 17.0 | -79.34 | -16.70 | -79.36 | 1491 |
| 70 | Z-score reversion | reversion | 74.83 | -25.17 | 312 | 29.2 | -84.87 | -25.73 | -84.87 | 2082 |
| 71 | MFI reversion | reversion | 72.11 | -27.89 | 308 | 20.8 | -87.55 | -31.65 | -87.62 | 2096 |
| 72 | Supertrend | trend | 71.01 | -28.99 | 315 | 19.4 | -87.53 | -23.32 | -87.56 | 1938 |
| 73 | AI bee: Bizzy | ai | 69.11 | -30.89 | 543 | 8.3 | — | — | — | — |
| 74 | Keltner breakout | breakout | 68.09 | -31.91 | 314 | 11.1 | -86.00 | -32.07 | -86.03 | 1902 |
| 75 | ADX DI cross | trend | 67.88 | -32.12 | 339 | 9.4 | -89.60 | -38.86 | -89.65 | 2093 |
| 76 | Ichimoku | trend | 67.48 | -32.52 | 280 | 7.9 | -82.82 | -25.70 | -82.84 | 1767 |
| 77 | AI bee: Boozy | ai | 66.69 | -33.31 | 209 | 3.8 | — | — | — | — |
| 78 | MACD zero-line | trend | 64.88 | -35.12 | 400 | 14.8 | -91.99 | -32.59 | -91.99 | 2371 |
| 79 | Donchian 20/10 | breakout | 64.01 | -35.99 | 425 | 16.5 | -91.57 | -28.70 | -91.60 | 2687 |
| 80 | RSI momentum | momentum | 62.66 | -37.34 | 400 | 13.8 | -91.06 | -28.21 | -91.08 | 2386 |
| 81 | Trend pullback | trend | 61.36 | -38.64 | 420 | 14.0 | -91.42 | -32.16 | -91.42 | 2345 |
| 82 | Triple EMA stack | trend | 61.29 | -38.71 | 452 | 13.9 | -93.67 | -34.69 | -93.68 | 2637 |
| 83 | Stochastic reversion | reversion | 60.89 | -39.11 | 615 | 22.4 | -95.64 | -39.70 | -95.64 | 4047 |
| 84 | Bollinger breakout | breakout | 60.50 | -39.50 | 437 | 13.3 | -94.29 | -38.18 | -94.30 | 2843 |
| 85 | Bollinger reversion | reversion | 60.09 | -39.91 | 574 | 16.9 | -95.68 | -38.41 | -95.68 | 3679 |
| 86 | Consensus | meta | 58.09 | -41.91 | 411 | 8.0 | -94.49 | -27.65 | -94.50 | 2652 |
| 87 | Connors RSI(2) | reversion | 56.54 | -43.46 | 545 | 17.1 | -96.62 | -37.48 | -96.63 | 3631 |
| 88 | EMA 9/21 cross | trend | 56.47 | -43.53 | 564 | 15.6 | -97.57 | -37.86 | -97.57 | 3559 |
| 89 | CCI reversion | reversion | 55.06 | -44.94 | 577 | 15.1 | -98.46 | -42.58 | -98.46 | 4691 |
| 90 | Candlestick reversal ⏸ | reversion | 53.96 | -46.04 | 698 | 14.5 | -99.30 | -42.13 | -99.30 | 5632 |
| 91 | VWAP momentum ⏸ | momentum | 53.60 | -46.40 | 634 | 8.7 | -98.74 | -34.13 | -98.74 | 5371 |
| 92 | OBV trend | momentum | 53.35 | -46.66 | 638 | 13.6 | -96.53 | -43.72 | -96.53 | 3616 |
| 93 | Parabolic SAR | trend | 51.74 | -48.26 | 580 | 12.6 | -97.44 | -46.19 | -97.45 | 3657 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -51.02 | -99.73 | 6129 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -47.06 | -99.50 | 6106 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -58.48 | -99.90 | 8260 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T15:35 | OBV trend · 1h | sell | DOGE-USD | 5.15 | -0.12 | stop-loss |
| 2026-10-05T15:35 | Trend pullback · 1h | buy | NVDA | 5.13 | — | rebalance up |
| 2026-10-05T15:35 | Trend pullback · 1h | buy | AMD | 6.62 | — | rebalance up |
| 2026-10-05T15:35 | Trend pullback · 1h | sell | BTC-USD | 12.32 | -0.18 | stop-loss |
| 2026-10-05T15:35 | Triple EMA stack · 1h | buy | ETHU | 5.80 | — | entry |
| 2026-10-05T15:35 | Triple EMA stack · 1h | sell | DOGE-USD | 5.80 | -0.07 | stop-loss |
| 2026-10-05T15:35 | EMA 20/50 cross · 1h | buy | SOL-USD | 5.35 | — | entry |
| 2026-10-05T15:35 | EMA 20/50 cross · 1h | sell | DOGE-USD | 5.35 | -0.13 | stop-loss |
| 2026-10-05T15:35 | Stochastic reversion | buy | MSTR | 5.54 | — | entry |
| 2026-10-05T15:35 | Stochastic reversion | buy | BITX | 3.75 | — | rebalance up |
| 2026-10-05T15:35 | Stochastic reversion | sell | XRP-USD | 5.49 | -0.07 | stop-loss |
| 2026-10-05T15:35 | Stochastic reversion | sell | DOGE-USD | 5.52 | -0.09 | stop-loss |
| 2026-10-05T15:35 | VWAP reversion | sell | DOGE-USD | 13.02 | -0.21 | stop-loss |
| 2026-10-05T15:35 | Z-score reversion | sell | XRP-USD | 9.88 | -0.13 | stop-loss |
| 2026-10-05T15:35 | Bollinger reversion | buy | NVDA | 12.03 | — | entry signal |
| 2026-10-05T15:35 | Bollinger reversion | sell | XRP-USD | 11.92 | -0.18 | stop-loss |
| 2026-10-05T15:35 | Connors RSI(2) | buy | MSTR | 14.14 | — | entry signal |
| 2026-10-05T15:35 | Connors RSI(2) | buy | BITX | 14.14 | — | entry signal |
| 2026-10-05T15:35 | RSI(14) reversion | sell | DOGE-USD | 21.36 | -0.35 | stop-loss |
| 2026-10-05T15:35 | Trend pullback | sell | UPRO | 6.84 | 0.04 | take-profit |
| 2026-10-05T15:35 | Trend pullback | sell | ETHU | 6.75 | -0.06 | exit signal |
| 2026-10-05T15:30 | AI bee: Bizzy | buy | TNA | 9.86 | — | Jev: buy (buy p=0.57) |
| 2026-10-05T15:30 | Agent (ML meta-label) | sell | BTC-USD | 4.20 | -0.02 | selected signal exited |
| 2026-10-05T15:30 | Williams %R · 1h | buy | LABU | 5.89 | — | entry signal |
| 2026-10-05T15:30 | Williams %R · 1h | sell | SQQQ | 5.82 | -0.12 | rebalance down |
| 2026-10-05T15:30 | VWAP reversion · 1h | sell | LABU | 25.05 | 0.07 | exit signal |
| 2026-10-05T15:30 | Squeeze breakout · 1h | buy | MSFT | 23.81 | — | entry signal |
| 2026-10-05T15:30 | Squeeze breakout · 1h | buy | META | 23.81 | — | entry signal |
| 2026-10-05T15:30 | ROC + volume · 1h | sell | ETHU | 4.82 | -0.06 | exit signal |
| 2026-10-05T15:30 | ROC + volume · 1h | sell | COIN | 4.85 | -0.03 | exit signal |
| 2026-10-05T15:30 | VWAP momentum · 1h | buy | LABU | 9.12 | — | entry signal |
| 2026-10-05T15:30 | VWAP momentum · 1h | sell | TECL | 6.07 | -0.04 | exit signal |
| 2026-10-05T15:30 | VWAP momentum · 1h | sell | NVDA | 6.09 | -0.03 | exit signal |
| 2026-10-05T15:30 | VWAP momentum · 1h | sell | MSTR | 6.03 | -0.08 | exit signal |
| 2026-10-05T15:30 | VWAP momentum · 1h | sell | COIN | 6.08 | -0.03 | exit signal |
| 2026-10-05T15:30 | Heikin-Ashi · 1h | buy | TECL | 10.06 | — | entry signal |
| 2026-10-05T15:30 | Heikin-Ashi · 1h | buy | NVDA | 10.08 | — | entry signal |
| 2026-10-05T15:30 | Heikin-Ashi · 1h | buy | MSTR | 10.08 | — | entry signal |
| 2026-10-05T15:30 | Heikin-Ashi · 1h | buy | MSFT | 10.08 | — | entry signal |
| 2026-10-05T15:30 | Heikin-Ashi · 1h | buy | COIN | 10.08 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 15:35:05.000179+00:00 -> 2026-10-05 15:45:05.000179+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
