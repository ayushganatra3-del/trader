# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T14:35:05.000168+00:00 · 12547 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.03 (-0.97%)

Closed trades 33, win rate 66.7%, fees £1.08, max drawdown -1.59%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 39.61 | -0.08 |

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

Today: 13591 decisions in 2165 calls, $0.1824 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T14:35 | 0 / 11 / 19 | TECL 14% |  |
| Breezy | 2026-10-05T14:35 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-05T14:35 | 0 / 25 / 5 | MSTR 68% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 103.88 | 3.88 | 0 | — | -5.80 | -1.00 | -15.27 | 2 |
| 2 | Hold BTC | benchmark | 102.54 | 2.54 | 0 | — | 33.52 | 4.05 | -8.68 | 1 |
| 3 | VWAP reversion · 1h | reversion | 101.90 | 1.90 | 27 | 40.7 | -8.54 | -2.73 | -14.05 | 112 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 5 | Timing: Nasdaq FTD · QQQ | daily | 101.64 | 1.64 | 0 | — | -1.49 | -0.81 | -5.09 | 2 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.60 | 1.60 | 0 | — | 2.30 | 1.13 | -3.62 | 1 |
| 7 | Daily: Bullish score | daily | 101.40 | 1.40 | 3 | 0.0 | 3.81 | 0.71 | -12.76 | 12 |
| 8 | Copy: Cathie Wood (ARKK) | copy | 101.16 | 1.17 | 0 | — | 21.21 | 3.27 | -6.29 | 1 |
| 9 | Hold SPY | benchmark | 100.70 | 0.70 | 0 | — | 0.47 | 0.34 | -3.66 | 1 |
| 10 | Candlestick reversal · 1h | reversion | 100.62 | 0.62 | 55 | 36.4 | -23.68 | -5.48 | -25.43 | 489 |
| 11 | Donchian 55/20 · 1h | breakout | 100.43 | 0.43 | 17 | 0.0 | 6.46 | 1.00 | -16.96 | 110 |
| 12 | Bollinger reversion · 1h | reversion | 100.38 | 0.38 | 43 | 44.2 | -14.44 | -3.75 | -17.67 | 302 |
| 13 | RSI(14) reversion · 1h | reversion | 100.36 | 0.36 | 11 | 63.6 | 3.76 | 1.09 | -6.57 | 116 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.30 | 0.30 | 0 | — | -2.02 | -0.77 | -7.65 | 1 |
| 15 | Z-score reversion · 1h | reversion | 100.13 | 0.13 | 20 | 55.0 | 6.43 | 1.45 | -8.60 | 155 |
| 16 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 17 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 18 | Day trade: Stocks in Play ORB | daytrade | 99.99 | -0.01 | 20 | 35.0 | 4.20 | 2.04 | -1.46 | 86 |
| 19 | Connors RSI(2) · 1h | reversion | 99.97 | -0.03 | 68 | 45.6 | -12.71 | -4.43 | -16.84 | 221 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 99.93 | -0.07 | 0 | — | -2.68 | -1.29 | -5.14 | 1 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.76 | -0.24 | 5 | 20.0 | 4.85 | 1.51 | -7.55 | 43 |
| 22 | Trend pullback · 1h | trend | 99.56 | -0.44 | 52 | 23.1 | -17.89 | -5.09 | -22.12 | 160 |
| 23 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.25 | -0.27 | -1.79 | 19 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.22 | -0.78 | 3 | 33.3 | 0.36 | 0.21 | -4.17 | 19 |
| 25 | EMA 20/50 cross · 1h | trend | 99.19 | -0.81 | 25 | 8.0 | 12.14 | 1.55 | -15.33 | 137 |
| 26 | Stochastic reversion · 1h | reversion | 99.11 | -0.89 | 47 | 61.7 | -8.28 | -1.70 | -10.74 | 327 |
| 27 | Agent | meta | 99.03 | -0.97 | 33 | 66.7 | -9.52 | -6.24 | -10.13 | 216 |
| 28 | Williams %R · 1h | reversion | 98.37 | -1.63 | 72 | 55.6 | -16.50 | -2.93 | -19.41 | 498 |
| 29 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 30 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -3.40 | -1.73 | -5.44 | 104 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 98.05 | -1.95 | 0 | — | 0.87 | 0.42 | -5.18 | 1 |
| 32 | Daily: Momentum burst | daily | 97.96 | -2.04 | 3 | 0.0 | -0.77 | 0.06 | -16.91 | 44 |
| 33 | CCI reversion · 1h | reversion | 97.96 | -2.04 | 65 | 49.2 | -0.64 | 0.06 | -12.41 | 409 |
| 34 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.87 | -2.13 | 3 | 33.3 | -5.94 | -2.15 | -9.74 | 24 |
| 35 | Agent (rotation) | meta | 97.73 | -2.27 | 55 | 25.5 | -1.28 | -0.27 | -10.69 | 270 |
| 36 | Agent (ML meta-label) | meta | 97.15 | -2.85 | 220 | 16.4 | 2.87 | 0.65 | -12.54 | 375 |
| 37 | ADX DI cross · 1h | trend | 96.66 | -3.35 | 41 | 12.2 | -5.77 | -0.87 | -13.84 | 263 |
| 38 | Parabolic SAR · 1h | trend | 96.61 | -3.39 | 58 | 17.2 | -5.54 | -0.56 | -19.61 | 296 |
| 39 | Supertrend · 1h | trend | 96.43 | -3.57 | 29 | 10.3 | 1.40 | 0.38 | -16.43 | 205 |
| 40 | MACD cross · 1h | trend | 95.91 | -4.09 | 79 | 19.0 | -7.08 | -0.97 | -17.27 | 474 |
| 41 | Copy: Insider buying | copy | 95.81 | -4.19 | 6 | 50.0 | -19.92 | -3.96 | -21.08 | 73 |
| 42 | Squeeze breakout · 1h | breakout | 95.41 | -4.59 | 27 | 22.2 | 12.76 | 2.18 | -8.06 | 111 |
| 43 | MFI reversion · 1h | reversion | 95.06 | -4.95 | 73 | 27.4 | -9.92 | -1.73 | -16.99 | 119 |
| 44 | Gap and go | momentum | 95.03 | -4.97 | 39 | 7.7 | 6.47 | 1.71 | -5.79 | 195 |
| 45 | RSI momentum · 1h | momentum | 94.95 | -5.05 | 41 | 2.4 | 0.29 | 0.23 | -16.65 | 226 |
| 46 | Ichimoku · 1h | trend | 94.52 | -5.48 | 30 | 16.7 | 6.20 | 0.93 | -15.84 | 122 |
| 47 | Max aggression: 1-day momentum | meta | 94.27 | -5.73 | 6 | 33.3 | -28.07 | -1.58 | -39.72 | 42 |
| 48 | Opening range 30m | breakout | 94.09 | -5.91 | 76 | 17.1 | -16.48 | -5.12 | -17.14 | 553 |
| 49 | Triple EMA stack · 1h | trend | 94.00 | -6.00 | 51 | 9.8 | -7.33 | -0.67 | -24.28 | 232 |
| 50 | Bollinger breakout · 1h | breakout | 93.75 | -6.25 | 46 | 26.1 | 7.23 | 1.10 | -12.06 | 299 |
| 51 | Volume breakout · 1h | breakout | 93.02 | -6.98 | 32 | 9.4 | 3.74 | 0.70 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.45 | -7.55 | 70 | 12.9 | -4.69 | -0.44 | -18.47 | 347 |
| 53 | Opening range 15m | breakout | 92.37 | -7.63 | 93 | 16.1 | -19.24 | -5.76 | -19.24 | 686 |
| 54 | MACD zero-line · 1h | trend | 91.33 | -8.67 | 42 | 16.7 | 0.05 | 0.21 | -18.32 | 241 |
| 55 | Donchian 20/10 · 1h | breakout | 91.27 | -8.73 | 32 | 15.6 | -0.28 | 0.18 | -16.18 | 226 |
| 56 | VWAP momentum · 1h | momentum | 91.15 | -8.85 | 189 | 22.8 | -40.00 | -6.21 | -40.00 | 1280 |
| 57 | Three white soldiers | momentum | 90.79 | -9.21 | 81 | 14.8 | -49.80 | -26.43 | -49.95 | 583 |
| 58 | Heikin-Ashi · 1h | trend | 90.58 | -9.42 | 99 | 25.3 | -32.15 | -5.62 | -34.14 | 685 |
| 59 | Max aggression: 5-day momentum | meta | 90.44 | -9.56 | 5 | 40.0 | -22.35 | -2.01 | -29.56 | 30 |
| 60 | OBV trend · 1h | momentum | 90.05 | -9.96 | 99 | 11.1 | -13.34 | -1.51 | -26.78 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.56 | -11.44 | 30 | 6.7 | -12.13 | -1.47 | -23.27 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.26 | -12.74 | 92 | 15.2 | -10.48 | -1.29 | -23.18 | 422 |
| 63 | RSI(14) reversion | reversion | 86.94 | -13.06 | 193 | 33.7 | -70.33 | -19.55 | -70.66 | 1428 |
| 64 | VWAP reversion | reversion | 78.98 | -21.02 | 223 | 28.3 | -69.24 | -16.54 | -69.51 | 1353 |
| 65 | Squeeze breakout | breakout | 78.26 | -21.74 | 217 | 13.4 | -63.20 | -19.69 | -63.27 | 1230 |
| 66 | Donchian 55/20 | breakout | 76.70 | -23.30 | 219 | 15.5 | -69.77 | -15.85 | -69.77 | 1302 |
| 67 | ROC + volume | momentum | 76.70 | -23.30 | 287 | 18.8 | -74.60 | -18.49 | -74.74 | 1668 |
| 68 | Z-score reversion | reversion | 75.31 | -24.69 | 309 | 28.8 | -84.79 | -25.57 | -84.87 | 2076 |
| 69 | Volume breakout | breakout | 75.14 | -24.86 | 191 | 11.5 | -65.09 | -20.24 | -65.09 | 921 |
| 70 | EMA 20/50 cross | trend | 75.13 | -24.87 | 241 | 17.0 | -79.36 | -16.73 | -79.36 | 1493 |
| 71 | MFI reversion | reversion | 72.12 | -27.88 | 306 | 20.6 | -87.60 | -31.81 | -87.61 | 2097 |
| 72 | Supertrend | trend | 70.96 | -29.04 | 315 | 19.4 | -87.54 | -23.32 | -87.56 | 1938 |
| 73 | AI bee: Bizzy | ai | 69.20 | -30.80 | 539 | 8.3 | — | — | — | — |
| 74 | Keltner breakout | breakout | 68.05 | -31.95 | 313 | 11.2 | -85.91 | -31.72 | -86.03 | 1905 |
| 75 | ADX DI cross | trend | 67.83 | -32.17 | 339 | 9.4 | -89.69 | -39.44 | -89.71 | 2097 |
| 76 | Ichimoku | trend | 67.48 | -32.52 | 279 | 7.9 | -82.91 | -25.86 | -82.95 | 1769 |
| 77 | AI bee: Boozy | ai | 66.78 | -33.22 | 209 | 3.8 | — | — | — | — |
| 78 | MACD zero-line | trend | 64.87 | -35.13 | 397 | 14.4 | -91.92 | -32.75 | -91.93 | 2370 |
| 79 | Donchian 20/10 | breakout | 63.96 | -36.04 | 424 | 16.5 | -91.53 | -28.51 | -91.60 | 2690 |
| 80 | RSI momentum | momentum | 62.62 | -37.38 | 400 | 13.8 | -91.13 | -28.33 | -91.14 | 2397 |
| 81 | Trend pullback | trend | 61.48 | -38.52 | 417 | 13.9 | -91.46 | -32.34 | -91.46 | 2346 |
| 82 | Triple EMA stack | trend | 61.25 | -38.75 | 452 | 13.9 | -93.71 | -34.83 | -93.71 | 2657 |
| 83 | Stochastic reversion | reversion | 61.24 | -38.76 | 610 | 22.3 | -95.62 | -39.63 | -95.65 | 4038 |
| 84 | Bollinger reversion | reversion | 60.66 | -39.34 | 569 | 16.7 | -95.64 | -38.13 | -95.67 | 3673 |
| 85 | Bollinger breakout | breakout | 60.43 | -39.57 | 436 | 13.3 | -94.26 | -38.02 | -94.30 | 2851 |
| 86 | Consensus | meta | 58.10 | -41.90 | 408 | 8.1 | -94.49 | -27.78 | -94.49 | 2656 |
| 87 | EMA 9/21 cross | trend | 56.45 | -43.55 | 562 | 15.7 | -97.57 | -37.94 | -97.58 | 3569 |
| 88 | Connors RSI(2) | reversion | 56.44 | -43.56 | 534 | 15.9 | -96.62 | -37.49 | -96.62 | 3628 |
| 89 | CCI reversion | reversion | 55.40 | -44.60 | 577 | 15.1 | -98.44 | -42.27 | -98.45 | 4688 |
| 90 | Candlestick reversal | reversion | 54.50 | -45.50 | 687 | 14.4 | -99.29 | -42.03 | -99.29 | 5622 |
| 91 | VWAP momentum ⏸ | momentum | 53.60 | -46.40 | 634 | 8.7 | -98.73 | -33.96 | -98.73 | 5372 |
| 92 | OBV trend | momentum | 53.47 | -46.53 | 635 | 13.5 | -96.52 | -43.67 | -96.53 | 3632 |
| 93 | Parabolic SAR | trend | 51.73 | -48.27 | 579 | 12.6 | -97.46 | -46.41 | -97.46 | 3666 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -51.69 | -99.73 | 6139 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -46.85 | -99.50 | 6092 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -58.49 | -99.90 | 8273 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T14:35 | Agent (rotation) | sell | SOL-USD | 6.39 | -0.15 | selected signal exited |
| 2026-10-05T14:35 | Consensus | buy | META | 7.27 | — | entry |
| 2026-10-05T14:35 | Consensus | sell | TNA | 5.79 | -0.05 | target is flat |
| 2026-10-05T14:35 | Consensus | sell | IWM | 5.82 | -0.02 | target is flat |
| 2026-10-05T14:35 | Consensus | sell | BTC-USD | 5.76 | -0.08 | target is flat |
| 2026-10-05T14:35 | Agent | buy | SQQQ | 19.76 | — | rebalance up |
| 2026-10-05T14:35 | MFI reversion · 1h | sell | LABU | 22.86 | -1.19 | stop-loss |
| 2026-10-05T14:35 | CCI reversion · 1h | sell | SOL-USD | 12.96 | -0.17 | stop-loss |
| 2026-10-05T14:35 | Candlestick reversal · 1h | sell | SOL-USD | 24.99 | -0.32 | stop-loss |
| 2026-10-05T14:35 | OBV trend · 1h | buy | META | 5.26 | — | entry |
| 2026-10-05T14:35 | OBV trend · 1h | sell | ETH-USD | 5.26 | -0.06 | stop-loss |
| 2026-10-05T14:35 | VWAP momentum · 1h | sell | BTC-USD | 6.04 | -0.09 | stop-loss |
| 2026-10-05T14:35 | Trend pullback · 1h | buy | TSLA | 2.41 | — | entry |
| 2026-10-05T14:35 | Trend pullback · 1h | buy | META | 9.96 | — | entry |
| 2026-10-05T14:35 | Trend pullback · 1h | sell | ETH-USD | 12.37 | -0.13 | stop-loss |
| 2026-10-05T14:35 | Parabolic SAR · 1h | sell | SOL-USD | 6.32 | -0.11 | stop-loss |
| 2026-10-05T14:35 | Parabolic SAR · 1h | sell | DOGE-USD | 6.29 | -0.14 | stop-loss |
| 2026-10-05T14:35 | Parabolic SAR · 1h | sell | BTC-USD | 2.37 | -0.04 | stop-loss |
| 2026-10-05T14:35 | MFI reversion | sell | XRP-USD | 17.96 | -0.18 | stop-loss |
| 2026-10-05T14:35 | MFI reversion | sell | SOL-USD | 17.87 | -0.24 | stop-loss |
| 2026-10-05T14:35 | CCI reversion | buy | SQQQ | 13.85 | — | entry signal |
| 2026-10-05T14:35 | Z-score reversion | buy | SQQQ | 18.83 | — | entry signal |
| 2026-10-05T14:35 | Connors RSI(2) | buy | TSLA | 9.41 | — | entry signal |
| 2026-10-05T14:35 | Connors RSI(2) | buy | TNA | 9.41 | — | entry signal |
| 2026-10-05T14:35 | Connors RSI(2) | buy | MSTR | 9.41 | — | entry signal |
| 2026-10-05T14:35 | Connors RSI(2) | buy | IWM | 9.41 | — | entry signal |
| 2026-10-05T14:35 | Connors RSI(2) | buy | BITX | 9.41 | — | entry signal |
| 2026-10-05T14:35 | Connors RSI(2) | sell | ETHU | 4.57 | -0.06 | rebalance down |
| 2026-10-05T14:35 | Three white soldiers | sell | TSLA | 22.77 | 0.11 | exit signal |
| 2026-10-05T14:35 | Three white soldiers | sell | IWM | 22.55 | -0.10 | exit signal |
| 2026-10-05T14:35 | Candlestick reversal | buy | SQQQ | 13.63 | — | entry signal |
| 2026-10-05T14:35 | Volume breakout | sell | BITX | 18.43 | -0.52 | stop-loss |
| 2026-10-05T14:35 | Keltner breakout | buy | TQQQ | 11.35 | — | entry |
| 2026-10-05T14:35 | Keltner breakout | buy | QQQ | 3.76 | — | rebalance up |
| 2026-10-05T14:35 | Keltner breakout | sell | TNA | 8.43 | -0.07 | stop-loss |
| 2026-10-05T14:35 | Keltner breakout | sell | IWM | 8.53 | -0.03 | stop-loss |
| 2026-10-05T14:35 | Keltner breakout | sell | BTC-USD | 8.40 | -0.16 | stop-loss |
| 2026-10-05T14:35 | Bollinger breakout | buy | UPRO | 6.47 | — | rebalance up |
| 2026-10-05T14:35 | Bollinger breakout | buy | TSLA | 6.45 | — | rebalance up |
| 2026-10-05T14:35 | Bollinger breakout | buy | SPY | 6.44 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 14:35:05.000168+00:00 -> 2026-10-05 14:45:05.000168+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
