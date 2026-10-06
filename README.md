# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T17:31:05.000182+00:00 · 13694 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £98.29 (-1.71%)

Closed trades 37, win rate 62.2%, fees £1.28, max drawdown -2.16%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-06 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, PAM 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-05)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.70 · VIX 15.52 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.8, AMD 7.6, TECL 7.6, MSTR 7.5, BITX 7.5, ETHU 7.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 25588 decisions in 2474 calls, $0.3219 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T17:31 | 1 / 11 / 18 | SOXL 14% |  |
| Breezy | 2026-10-06T17:31 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-06T17:31 | 1 / 24 / 5 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 3.08 | +5.12% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| VWAP reversion · 1h | DOGE-USD | 1.89 | +3.24% | 5 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |
| VWAP reversion | TECL | 1.77 | +2.87% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.44 | 6.44 | 0 | — | -0.36 | 0.07 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -9.14 | -2.89 | -13.90 | 113 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.11 | 2.11 | 0 | — | 0.39 | 0.27 | -5.09 | 1 |
| 4 | Hold BTC | benchmark | 102.10 | 2.10 | 0 | — | 32.06 | 3.87 | -8.68 | 1 |
| 5 | Donchian 55/20 · 1h | breakout | 101.96 | 1.96 | 17 | 0.0 | 13.09 | 1.77 | -16.96 | 110 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.90 | 1.90 | 0 | — | 3.65 | 1.73 | -3.62 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 8 | Daily: Bullish score | daily | 101.66 | 1.66 | 3 | 0.0 | 5.84 | 0.97 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.16 | 1.16 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.56 | 0.56 | 67 | 38.8 | -20.82 | -4.85 | -22.99 | 491 |
| 13 | Stochastic reversion · 1h | reversion | 100.33 | 0.33 | 56 | 64.3 | -7.99 | -1.64 | -11.17 | 326 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 100.18 | 0.18 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 15 | EMA 20/50 cross · 1h | trend | 100.12 | 0.12 | 28 | 7.1 | 13.97 | 1.73 | -15.31 | 142 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.86 | 1.86 | -1.59 | 85 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 18 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 19 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 20 | Copy: Warren Buffett (BRK-B) | copy | 99.98 | -0.02 | 0 | — | -2.18 | -0.83 | -7.65 | 1 |
| 21 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 99.91 | -0.09 | 0 | — | 18.89 | 2.88 | -6.29 | 1 |
| 23 | Connors RSI(2) · 1h | reversion | 99.69 | -0.31 | 72 | 44.4 | -11.09 | -4.04 | -15.07 | 217 |
| 24 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 1.91 | 0.59 | -6.57 | 124 |
| 25 | Trend pullback · 1h | trend | 99.31 | -0.69 | 64 | 25.0 | -20.55 | -5.97 | -24.51 | 166 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | 0.17 | 0.14 | -4.23 | 103 |
| 27 | Daily: Momentum burst | daily | 98.33 | -1.67 | 3 | 0.0 | 1.25 | 0.37 | -16.91 | 41 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -7.71 | -4.84 | -9.54 | 232 |
| 30 | Bollinger reversion · 1h | reversion | 98.17 | -1.83 | 49 | 46.9 | -15.49 | -3.96 | -16.97 | 303 |
| 31 | Z-score reversion · 1h | reversion | 98.14 | -1.86 | 23 | 52.2 | 3.65 | 0.89 | -8.60 | 150 |
| 32 | Daily: SMA 20/50 cross · AAPL | daily | 97.26 | -2.74 | 0 | — | -0.49 | -0.10 | -5.18 | 1 |
| 33 | Copy: Insider buying | copy | 97.26 | -2.74 | 10 | 50.0 | -16.05 | -2.97 | -21.08 | 73 |
| 34 | Agent (rotation) | meta | 97.20 | -2.80 | 63 | 28.6 | -0.09 | 0.09 | -11.44 | 253 |
| 35 | ADX DI cross · 1h | trend | 97.18 | -2.82 | 43 | 11.6 | -2.80 | -0.34 | -13.84 | 257 |
| 36 | Supertrend · 1h | trend | 97.08 | -2.92 | 32 | 9.4 | 2.95 | 0.58 | -16.43 | 213 |
| 37 | Agent (ML meta-label) | meta | 96.96 | -3.04 | 260 | 14.6 | 3.32 | 0.74 | -14.20 | 380 |
| 38 | Williams %R · 1h | reversion | 96.88 | -3.12 | 85 | 52.9 | -19.86 | -3.74 | -20.64 | 493 |
| 39 | Parabolic SAR · 1h | trend | 96.70 | -3.30 | 63 | 15.9 | -2.68 | -0.17 | -19.45 | 299 |
| 40 | CCI reversion · 1h | reversion | 96.49 | -3.51 | 71 | 49.3 | -0.54 | 0.08 | -12.41 | 409 |
| 41 | MACD cross · 1h | trend | 95.89 | -4.11 | 84 | 20.2 | -11.13 | -1.77 | -17.27 | 473 |
| 42 | RSI momentum · 1h | momentum | 95.72 | -4.29 | 45 | 2.2 | 0.88 | 0.31 | -16.65 | 228 |
| 43 | Squeeze breakout · 1h | breakout | 95.43 | -4.57 | 30 | 20.0 | 15.61 | 2.62 | -8.06 | 106 |
| 44 | Ichimoku · 1h | trend | 95.27 | -4.73 | 32 | 15.6 | 8.81 | 1.22 | -15.84 | 124 |
| 45 | MFI reversion · 1h | reversion | 95.15 | -4.84 | 74 | 28.4 | -10.18 | -1.76 | -16.99 | 119 |
| 46 | Triple EMA stack · 1h | trend | 94.95 | -5.05 | 56 | 10.7 | -9.71 | -1.01 | -24.06 | 256 |
| 47 | Max aggression: 1-day momentum | meta | 94.86 | -5.14 | 7 | 42.9 | -23.61 | -1.22 | -37.31 | 42 |
| 48 | Bollinger breakout · 1h | breakout | 94.68 | -5.33 | 50 | 24.0 | 7.78 | 1.16 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.34 | -5.66 | 46 | 6.5 | 6.82 | 1.78 | -6.47 | 201 |
| 50 | Opening range 30m | breakout | 94.06 | -5.94 | 97 | 21.6 | -17.61 | -5.47 | -17.90 | 572 |
| 51 | Volume breakout · 1h | breakout | 93.86 | -6.14 | 36 | 11.1 | 6.71 | 1.09 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.97 | -7.04 | 79 | 11.4 | -2.29 | -0.11 | -18.47 | 346 |
| 53 | Max aggression: 5-day momentum | meta | 92.75 | -7.25 | 5 | 40.0 | -18.65 | -1.57 | -29.56 | 29 |
| 54 | Opening range 15m | breakout | 92.51 | -7.49 | 113 | 19.5 | -18.53 | -5.50 | -19.24 | 692 |
| 55 | Donchian 20/10 · 1h | breakout | 91.50 | -8.50 | 39 | 15.4 | 3.30 | 0.61 | -16.18 | 222 |
| 56 | MACD zero-line · 1h | trend | 91.39 | -8.61 | 45 | 17.8 | -2.18 | -0.10 | -18.32 | 249 |
| 57 | Three white soldiers | momentum | 91.07 | -8.93 | 99 | 20.2 | -49.27 | -24.82 | -49.52 | 587 |
| 58 | VWAP momentum · 1h | momentum | 90.93 | -9.07 | 228 | 22.8 | -37.73 | -5.82 | -37.77 | 1271 |
| 59 | OBV trend · 1h | momentum | 90.84 | -9.16 | 104 | 11.5 | -12.57 | -1.39 | -26.73 | 338 |
| 60 | Heikin-Ashi · 1h | trend | 90.16 | -9.84 | 115 | 24.3 | -31.68 | -5.46 | -34.24 | 692 |
| 61 | Keltner breakout · 1h | breakout | 89.93 | -10.07 | 30 | 6.7 | -9.81 | -1.12 | -23.31 | 229 |
| 62 | ROC + volume · 1h | momentum | 87.52 | -12.47 | 104 | 15.4 | -8.98 | -1.07 | -23.04 | 412 |
| 63 | RSI(14) reversion | reversion | 85.80 | -14.20 | 218 | 32.1 | -70.69 | -19.57 | -71.08 | 1419 |
| 64 | Squeeze breakout | breakout | 77.79 | -22.21 | 246 | 15.9 | -62.47 | -19.13 | -62.54 | 1226 |
| 65 | VWAP reversion | reversion | 77.77 | -22.23 | 261 | 29.1 | -68.84 | -16.10 | -69.27 | 1375 |
| 66 | ROC + volume | momentum | 76.92 | -23.08 | 318 | 20.8 | -73.93 | -17.87 | -73.95 | 1657 |
| 67 | Donchian 55/20 | breakout | 76.06 | -23.94 | 258 | 17.4 | -68.96 | -15.35 | -68.96 | 1304 |
| 68 | EMA 20/50 cross | trend | 74.73 | -25.27 | 262 | 18.7 | -78.46 | -16.20 | -78.46 | 1477 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.13 | -19.57 | -65.17 | 936 |
| 70 | Z-score reversion | reversion | 71.76 | -28.24 | 347 | 28.2 | -85.20 | -25.60 | -85.21 | 2054 |
| 71 | MFI reversion | reversion | 70.23 | -29.77 | 342 | 21.1 | -86.91 | -30.61 | -86.93 | 2117 |
| 72 | Supertrend | trend | 70.02 | -29.98 | 348 | 20.4 | -87.03 | -22.55 | -87.03 | 1930 |
| 73 | Keltner breakout | breakout | 68.15 | -31.85 | 348 | 13.2 | -85.58 | -30.81 | -85.58 | 1896 |
| 74 | AI bee: Bizzy | ai | 67.73 | -32.27 | 598 | 8.9 | — | — | — | — |
| 75 | Ichimoku | trend | 67.04 | -32.96 | 315 | 8.9 | -82.19 | -24.88 | -82.19 | 1767 |
| 76 | AI bee: Boozy | ai | 66.18 | -33.81 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 65.07 | -34.93 | 386 | 9.3 | -89.67 | -37.94 | -89.67 | 2103 |
| 78 | MACD zero-line | trend | 63.62 | -36.38 | 442 | 15.8 | -91.58 | -31.25 | -91.58 | 2366 |
| 79 | Donchian 20/10 | breakout | 63.04 | -36.96 | 480 | 18.5 | -91.29 | -28.23 | -91.29 | 2673 |
| 80 | RSI momentum | momentum | 62.06 | -37.94 | 450 | 16.7 | -90.63 | -27.03 | -90.63 | 2376 |
| 81 | Triple EMA stack | trend | 60.52 | -39.48 | 495 | 15.6 | -93.36 | -32.57 | -93.36 | 2630 |
| 82 | Trend pullback | trend | 60.36 | -39.64 | 474 | 15.4 | -91.48 | -31.09 | -91.48 | 2341 |
| 83 | Bollinger breakout | breakout | 59.85 | -40.15 | 490 | 14.3 | -94.05 | -36.15 | -94.05 | 2824 |
| 84 | Stochastic reversion | reversion | 58.41 | -41.59 | 685 | 22.9 | -95.52 | -37.92 | -95.57 | 4036 |
| 85 | Bollinger reversion | reversion | 58.22 | -41.78 | 635 | 18.0 | -95.58 | -36.77 | -95.62 | 3683 |
| 86 | Consensus | meta | 57.59 | -42.41 | 468 | 10.0 | -94.70 | -27.51 | -94.70 | 2709 |
| 87 | EMA 9/21 cross | trend | 55.98 | -44.02 | 607 | 16.5 | -97.44 | -35.74 | -97.44 | 3552 |
| 88 | Connors RSI(2) | reversion | 54.03 | -45.97 | 657 | 19.9 | -96.59 | -35.62 | -96.59 | 3644 |
| 89 | OBV trend | momentum | 52.49 | -47.51 | 716 | 15.2 | -96.45 | -40.15 | -96.45 | 3605 |
| 90 | CCI reversion | reversion | 52.26 | -47.74 | 659 | 16.4 | -98.45 | -41.12 | -98.45 | 4698 |
| 91 | Candlestick reversal | reversion | 51.21 | -48.79 | 759 | 14.6 | -99.28 | -40.82 | -99.28 | 5613 |
| 92 | VWAP momentum | momentum | 50.78 | -49.22 | 702 | 8.5 | -98.72 | -32.50 | -98.72 | 5380 |
| 93 | Parabolic SAR | trend | 50.42 | -49.58 | 656 | 14.8 | -97.40 | -42.53 | -97.40 | 3676 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -48.07 | -99.73 | 6125 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -45.00 | -99.50 | 6101 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -53.43 | -99.90 | 8236 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T17:30 | Agent (rotation) | buy | SQQQ | 8.10 | — | entry |
| 2026-10-06T17:30 | Consensus | buy | UPRO | 11.52 | — | entry |
| 2026-10-06T17:30 | Consensus | buy | SPY | 11.52 | — | entry |
| 2026-10-06T17:30 | Consensus | buy | AMZN | 11.52 | — | entry |
| 2026-10-06T17:30 | Consensus | sell | NVDA | 2.88 | -0.00 | rebalance down |
| 2026-10-06T17:30 | Consensus | sell | AMD | 2.92 | 0.00 | rebalance down |
| 2026-10-06T17:30 | Z-score reversion · 1h | buy | SQQQ | 24.54 | — | entry signal |
| 2026-10-06T17:30 | OBV trend · 1h | buy | AMZN | 1.43 | — | entry |
| 2026-10-06T17:30 | OBV trend · 1h | sell | IWM | 1.43 | -0.01 | exit signal |
| 2026-10-06T17:30 | VWAP momentum · 1h | buy | PLTR | 22.74 | — | entry signal |
| 2026-10-06T17:30 | VWAP momentum · 1h | sell | UPRO | 22.68 | -0.09 | exit signal |
| 2026-10-06T17:30 | VWAP momentum · 1h | sell | SPY | 22.74 | -0.04 | exit signal |
| 2026-10-06T17:30 | Heikin-Ashi · 1h | buy | UPRO | 5.56 | — | rebalance up |
| 2026-10-06T17:30 | Heikin-Ashi · 1h | buy | PLTR | 6.84 | — | rebalance up |
| 2026-10-06T17:30 | Heikin-Ashi · 1h | sell | TECL | 5.71 | 0.13 | exit signal |
| 2026-10-06T17:30 | Heikin-Ashi · 1h | sell | SOXL | 6.95 | -0.02 | exit signal |
| 2026-10-06T17:30 | Heikin-Ashi · 1h | sell | NVDA | 5.65 | 0.05 | exit signal |
| 2026-10-06T17:30 | ADX DI cross · 1h | buy | TSLA | 5.60 | — | rebalance up |
| 2026-10-06T17:30 | ADX DI cross · 1h | buy | SOXL | 7.42 | — | rebalance up |
| 2026-10-06T17:30 | ADX DI cross · 1h | sell | TNA | 9.18 | -0.15 | exit signal |
| 2026-10-06T17:30 | ADX DI cross · 1h | sell | IWM | 13.90 | -0.07 | exit signal |
| 2026-10-06T17:30 | MACD zero-line · 1h | buy | XRP-USD | 3.23 | — | entry |
| 2026-10-06T17:30 | MACD zero-line · 1h | buy | SOL-USD | 7.03 | — | entry |
| 2026-10-06T17:30 | MACD zero-line · 1h | buy | COIN | 7.03 | — | entry |
| 2026-10-06T17:30 | MACD zero-line · 1h | sell | TNA | 9.00 | -0.04 | exit signal |
| 2026-10-06T17:30 | MACD zero-line · 1h | sell | IWM | 8.30 | -0.03 | exit signal |
| 2026-10-06T17:30 | MACD cross · 1h | buy | PLTR | 3.21 | — | entry |
| 2026-10-06T17:30 | MACD cross · 1h | buy | DOGE-USD | 5.05 | — | entry |
| 2026-10-06T17:30 | MACD cross · 1h | buy | AMD | 5.05 | — | entry |
| 2026-10-06T17:30 | MACD cross · 1h | sell | TNA | 5.38 | 0.05 | exit signal |
| 2026-10-06T17:30 | MACD cross · 1h | sell | IWM | 7.93 | -0.01 | exit signal |
| 2026-10-06T17:30 | MFI reversion | buy | SPY | 7.02 | — | entry signal |
| 2026-10-06T17:30 | MFI reversion | buy | IWM | 7.02 | — | entry signal |
| 2026-10-06T17:30 | MFI reversion | buy | COIN | 7.02 | — | entry signal |
| 2026-10-06T17:30 | MFI reversion | sell | MSFT | 7.84 | -0.02 | exit signal |
| 2026-10-06T17:30 | CCI reversion | buy | AMZN | 2.75 | — | entry signal |
| 2026-10-06T17:30 | CCI reversion | buy | AMD | 2.75 | — | entry signal |
| 2026-10-06T17:30 | Stochastic reversion | buy | LABU | 2.78 | — | entry signal |
| 2026-10-06T17:30 | Stochastic reversion | sell | AAPL | 2.55 | 0.01 | exit signal |
| 2026-10-06T17:30 | VWAP reversion | buy | COIN | 9.22 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 17:31:05.000182+00:00 -> 2026-10-06 17:41:05.000182+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
