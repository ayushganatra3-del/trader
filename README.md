# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T17:00:05.000144+00:00 · 13664 ticks

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

Today: 22906 decisions in 2384 calls, $0.2904 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T17:00 | 0 / 16 / 13 | AMD 15%, TSLA 14% |  |
| Breezy | 2026-10-06T17:00 | 0 / 23 / 6 | cash |  |
| Boozy | 2026-10-06T17:00 | 1 / 26 / 2 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.52 | 6.52 | 0 | — | -0.82 | -0.02 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -8.81 | -2.78 | -13.79 | 113 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.11 | 2.11 | 0 | — | 0.24 | 0.18 | -5.09 | 1 |
| 4 | Donchian 55/20 · 1h | breakout | 102.04 | 2.04 | 17 | 0.0 | 13.24 | 1.79 | -16.96 | 110 |
| 5 | Hold BTC | benchmark | 102.01 | 2.01 | 0 | — | 31.87 | 3.85 | -8.68 | 1 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.87 | 1.87 | 0 | — | 3.65 | 1.73 | -3.62 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 8 | Daily: Bullish score | daily | 101.54 | 1.54 | 3 | 0.0 | 5.61 | 0.94 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.17 | 1.17 | 0 | — | 0.97 | 0.63 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.56 | 0.56 | 67 | 38.8 | -20.65 | -4.81 | -23.10 | 487 |
| 13 | Stochastic reversion · 1h | reversion | 100.19 | 0.19 | 56 | 64.3 | -7.55 | -1.54 | -10.65 | 326 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.18 | 0.18 | 0 | — | -1.92 | -0.72 | -7.65 | 1 |
| 15 | EMA 20/50 cross · 1h | trend | 100.17 | 0.17 | 28 | 7.1 | 14.40 | 1.78 | -15.31 | 142 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 100.15 | 0.15 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.86 | 1.86 | -1.59 | 85 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 19 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 20 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 21 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 99.84 | -0.16 | 0 | — | 18.68 | 2.85 | -6.29 | 1 |
| 23 | Connors RSI(2) · 1h | reversion | 99.66 | -0.34 | 72 | 44.4 | -11.11 | -4.05 | -15.07 | 217 |
| 24 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.30 | 1.21 | -6.57 | 117 |
| 25 | Trend pullback · 1h | trend | 99.33 | -0.67 | 64 | 25.0 | -20.52 | -5.96 | -24.51 | 166 |
| 26 | Bollinger reversion · 1h | reversion | 98.65 | -1.35 | 48 | 47.9 | -15.10 | -3.89 | -17.00 | 303 |
| 27 | Z-score reversion · 1h | reversion | 98.61 | -1.39 | 22 | 54.5 | 4.18 | 1.01 | -8.60 | 149 |
| 28 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -1.32 | -0.68 | -4.23 | 103 |
| 29 | Daily: Momentum burst | daily | 98.39 | -1.61 | 3 | 0.0 | 1.08 | 0.34 | -16.91 | 41 |
| 30 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 31 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -7.26 | -4.66 | -9.05 | 223 |
| 32 | Copy: Insider buying | copy | 97.48 | -2.52 | 9 | 55.6 | -15.91 | -2.94 | -21.08 | 73 |
| 33 | Agent (rotation) | meta | 97.36 | -2.64 | 62 | 29.0 | -1.35 | -0.22 | -11.44 | 263 |
| 34 | Williams %R · 1h | reversion | 97.26 | -2.74 | 84 | 53.6 | -19.42 | -3.66 | -20.54 | 492 |
| 35 | ADX DI cross · 1h | trend | 97.23 | -2.77 | 41 | 12.2 | -2.89 | -0.36 | -13.84 | 257 |
| 36 | Daily: SMA 20/50 cross · AAPL | daily | 97.13 | -2.87 | 0 | — | -0.29 | -0.02 | -5.18 | 1 |
| 37 | Supertrend · 1h | trend | 97.12 | -2.88 | 32 | 9.4 | 3.12 | 0.60 | -16.43 | 213 |
| 38 | Agent (ML meta-label) | meta | 97.04 | -2.96 | 259 | 14.7 | 6.11 | 1.21 | -13.54 | 392 |
| 39 | Parabolic SAR · 1h | trend | 96.78 | -3.23 | 63 | 15.9 | -2.70 | -0.17 | -19.45 | 300 |
| 40 | CCI reversion · 1h | reversion | 96.54 | -3.46 | 71 | 49.3 | 0.65 | 0.27 | -12.41 | 407 |
| 41 | MACD cross · 1h | trend | 96.00 | -4.00 | 82 | 19.5 | -11.05 | -1.75 | -17.27 | 473 |
| 42 | RSI momentum · 1h | momentum | 95.78 | -4.22 | 45 | 2.2 | 0.98 | 0.32 | -16.65 | 228 |
| 43 | Squeeze breakout · 1h | breakout | 95.50 | -4.50 | 30 | 20.0 | 16.03 | 2.68 | -8.06 | 105 |
| 44 | Ichimoku · 1h | trend | 95.29 | -4.71 | 32 | 15.6 | 8.87 | 1.22 | -15.84 | 124 |
| 45 | MFI reversion · 1h | reversion | 95.16 | -4.84 | 74 | 28.4 | -10.22 | -1.77 | -16.99 | 119 |
| 46 | Max aggression: 1-day momentum | meta | 95.03 | -4.97 | 7 | 42.9 | -23.45 | -1.21 | -37.31 | 42 |
| 47 | Triple EMA stack · 1h | trend | 94.99 | -5.01 | 56 | 10.7 | -9.63 | -1.00 | -24.06 | 256 |
| 48 | Bollinger breakout · 1h | breakout | 94.69 | -5.30 | 50 | 24.0 | 7.86 | 1.17 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.36 | -5.64 | 46 | 6.5 | 6.85 | 1.79 | -6.43 | 201 |
| 50 | Opening range 30m | breakout | 94.16 | -5.84 | 94 | 22.3 | -17.41 | -5.42 | -17.61 | 572 |
| 51 | Volume breakout · 1h | breakout | 93.94 | -6.06 | 36 | 11.1 | 6.84 | 1.11 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 93.04 | -6.96 | 79 | 11.4 | -1.77 | -0.04 | -18.47 | 345 |
| 53 | Max aggression: 5-day momentum | meta | 92.78 | -7.22 | 5 | 40.0 | -18.60 | -1.57 | -29.56 | 29 |
| 54 | Opening range 15m | breakout | 92.60 | -7.40 | 110 | 20.0 | -18.42 | -5.47 | -19.05 | 692 |
| 55 | Donchian 20/10 · 1h | breakout | 91.58 | -8.42 | 38 | 15.8 | 2.91 | 0.56 | -16.18 | 223 |
| 56 | MACD zero-line · 1h | trend | 91.51 | -8.49 | 43 | 18.6 | -1.83 | -0.05 | -18.32 | 248 |
| 57 | Three white soldiers | momentum | 91.07 | -8.93 | 99 | 20.2 | -49.27 | -24.82 | -49.52 | 587 |
| 58 | VWAP momentum · 1h | momentum | 91.01 | -8.99 | 226 | 23.0 | -38.02 | -5.86 | -38.02 | 1273 |
| 59 | OBV trend · 1h | momentum | 90.90 | -9.10 | 103 | 11.7 | -12.25 | -1.35 | -26.73 | 338 |
| 60 | Heikin-Ashi · 1h | trend | 90.21 | -9.79 | 112 | 23.2 | -31.62 | -5.44 | -34.14 | 692 |
| 61 | Keltner breakout · 1h | breakout | 90.02 | -9.98 | 30 | 6.7 | -10.48 | -1.21 | -23.31 | 226 |
| 62 | ROC + volume · 1h | momentum | 87.60 | -12.40 | 104 | 15.4 | -8.82 | -1.05 | -23.04 | 412 |
| 63 | RSI(14) reversion | reversion | 85.83 | -14.17 | 218 | 32.1 | -70.98 | -19.82 | -71.36 | 1427 |
| 64 | VWAP reversion | reversion | 77.92 | -22.08 | 260 | 29.2 | -68.66 | -15.98 | -69.18 | 1373 |
| 65 | Squeeze breakout | breakout | 77.79 | -22.21 | 246 | 15.9 | -62.40 | -19.12 | -62.44 | 1225 |
| 66 | ROC + volume | momentum | 76.92 | -23.08 | 318 | 20.8 | -73.95 | -17.90 | -73.95 | 1661 |
| 67 | Donchian 55/20 | breakout | 76.18 | -23.82 | 254 | 17.7 | -68.86 | -15.33 | -68.86 | 1304 |
| 68 | EMA 20/50 cross | trend | 74.76 | -25.24 | 261 | 18.8 | -78.41 | -16.19 | -78.41 | 1476 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.19 | -19.68 | -65.19 | 935 |
| 70 | Z-score reversion | reversion | 71.99 | -28.01 | 345 | 28.1 | -85.25 | -25.48 | -85.25 | 2055 |
| 71 | MFI reversion | reversion | 70.45 | -29.55 | 336 | 21.4 | -86.93 | -30.56 | -86.96 | 2108 |
| 72 | Supertrend | trend | 70.06 | -29.94 | 347 | 20.5 | -87.03 | -22.55 | -87.03 | 1931 |
| 73 | Keltner breakout | breakout | 68.20 | -31.80 | 346 | 13.0 | -85.58 | -30.84 | -85.59 | 1896 |
| 74 | AI bee: Bizzy | ai | 67.74 | -32.26 | 596 | 8.9 | — | — | — | — |
| 75 | Ichimoku | trend | 67.06 | -32.94 | 314 | 8.6 | -82.21 | -24.88 | -82.21 | 1768 |
| 76 | AI bee: Boozy | ai | 66.21 | -33.79 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 65.07 | -34.93 | 385 | 9.1 | -89.67 | -37.93 | -89.68 | 2106 |
| 78 | MACD zero-line | trend | 63.68 | -36.32 | 441 | 15.9 | -91.55 | -31.16 | -91.55 | 2362 |
| 79 | Donchian 20/10 | breakout | 63.04 | -36.96 | 479 | 18.6 | -91.29 | -28.23 | -91.29 | 2674 |
| 80 | RSI momentum | momentum | 62.10 | -37.90 | 449 | 16.5 | -90.63 | -27.03 | -90.63 | 2379 |
| 81 | Triple EMA stack | trend | 60.56 | -39.44 | 493 | 15.6 | -93.36 | -32.58 | -93.36 | 2631 |
| 82 | Trend pullback | trend | 60.46 | -39.53 | 469 | 15.6 | -91.51 | -31.18 | -91.51 | 2343 |
| 83 | Bollinger breakout | breakout | 59.83 | -40.17 | 490 | 14.3 | -94.08 | -36.42 | -94.08 | 2828 |
| 84 | Stochastic reversion | reversion | 58.48 | -41.52 | 674 | 23.0 | -95.52 | -37.95 | -95.58 | 4033 |
| 85 | Bollinger reversion | reversion | 58.28 | -41.72 | 630 | 17.9 | -95.59 | -36.78 | -95.64 | 3681 |
| 86 | Consensus | meta | 57.76 | -42.24 | 462 | 10.0 | -94.66 | -27.39 | -94.66 | 2700 |
| 87 | EMA 9/21 cross | trend | 56.00 | -44.00 | 605 | 16.5 | -97.44 | -35.74 | -97.45 | 3554 |
| 88 | Connors RSI(2) | reversion | 54.14 | -45.85 | 646 | 20.0 | -96.58 | -35.56 | -96.58 | 3632 |
| 89 | OBV trend | momentum | 52.52 | -47.48 | 713 | 15.1 | -96.46 | -40.16 | -96.46 | 3610 |
| 90 | CCI reversion | reversion | 52.37 | -47.63 | 653 | 16.4 | -98.44 | -41.04 | -98.44 | 4696 |
| 91 | Candlestick reversal | reversion | 51.40 | -48.60 | 750 | 14.7 | -99.28 | -40.68 | -99.28 | 5601 |
| 92 | VWAP momentum | momentum | 50.85 | -49.15 | 697 | 8.6 | -98.73 | -32.65 | -98.73 | 5398 |
| 93 | Parabolic SAR | trend | 50.57 | -49.43 | 651 | 14.9 | -97.39 | -42.45 | -97.39 | 3675 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -47.96 | -99.73 | 6121 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -45.02 | -99.50 | 6089 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -53.59 | -99.90 | 8241 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T17:00 | Squeeze breakout · 1h | buy | NVDA | 4.91 | — | rebalance up |
| 2026-10-06T17:00 | Squeeze breakout · 1h | sell | DOGE-USD | 19.02 | -0.31 | exit signal |
| 2026-10-06T17:00 | Bollinger breakout · 1h | sell | SOL-USD | 5.52 | -0.10 | exit signal |
| 2026-10-06T17:00 | Bollinger breakout · 1h | sell | DOGE-USD | 5.52 | -0.11 | exit signal |
| 2026-10-06T17:00 | ROC + volume · 1h | buy | SOL-USD | 2.03 | — | entry |
| 2026-10-06T17:00 | ROC + volume · 1h | buy | PLTR | 4.17 | — | entry |
| 2026-10-06T17:00 | ROC + volume · 1h | sell | BTC-USD | 6.20 | -0.09 | stop-loss |
| 2026-10-06T17:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 5.59 | -0.09 | exit signal |
| 2026-10-06T17:00 | Parabolic SAR · 1h | buy | PLTR | 2.77 | — | entry |
| 2026-10-06T17:00 | Parabolic SAR · 1h | buy | BITX | 5.09 | — | entry |
| 2026-10-06T17:00 | Parabolic SAR · 1h | sell | BTC-USD | 7.31 | -0.10 | exit signal |
| 2026-10-06T17:00 | MFI reversion | sell | ETHU | 7.82 | -0.02 | stop-loss |
| 2026-10-06T17:00 | CCI reversion | buy | QQQ | 2.59 | — | entry |
| 2026-10-06T17:00 | CCI reversion | buy | GOOGL | 2.91 | — | entry |
| 2026-10-06T17:00 | CCI reversion | buy | AAPL | 2.91 | — | entry |
| 2026-10-06T17:00 | CCI reversion | sell | ETHU | 4.02 | -0.02 | stop-loss |
| 2026-10-06T17:00 | CCI reversion | sell | ETH-USD | 3.87 | -0.04 | stop-loss |
| 2026-10-06T17:00 | Z-score reversion | buy | DOGE-USD | 5.95 | — | entry |
| 2026-10-06T17:00 | Z-score reversion | buy | AAPL | 6.06 | — | rebalance up |
| 2026-10-06T17:00 | Z-score reversion | sell | ETH-USD | 12.01 | -0.12 | stop-loss |
| 2026-10-06T17:00 | Connors RSI(2) | buy | GOOGL | 13.54 | — | entry signal |
| 2026-10-06T17:00 | Connors RSI(2) | sell | NVDA | 13.55 | -0.02 | exit signal |
| 2026-10-06T17:00 | RSI momentum | sell | GOOGL | 12.46 | -0.04 | exit signal |
| 2026-10-06T17:00 | Parabolic SAR | buy | TSLA | 5.07 | — | rebalance up |
| 2026-10-06T17:00 | Parabolic SAR | sell | MSFT | 2.54 | -0.00 | rebalance down |
| 2026-10-06T17:00 | Parabolic SAR | sell | AMZN | 2.53 | -0.00 | rebalance down |
| 2026-10-06T16:56 | AI bee: Bizzy | buy | TSLA | 9.72 | — | Jev: buy (buy p=0.57) |
| 2026-10-06T16:56 | Consensus | buy | TSLA | 14.44 | — | entry |
| 2026-10-06T16:56 | ROC + volume · 1h | buy | MSTR | 2.36 | — | entry |
| 2026-10-06T16:56 | ROC + volume · 1h | sell | ETH-USD | 2.36 | -0.02 | stop-loss |
| 2026-10-06T16:56 | MFI reversion | buy | MSTR | 7.81 | — | entry |
| 2026-10-06T16:56 | MFI reversion | buy | ETHU | 7.84 | — | entry |
| 2026-10-06T16:56 | MFI reversion | buy | COIN | 7.84 | — | entry signal |
| 2026-10-06T16:56 | MFI reversion | sell | XRP-USD | 3.94 | -0.03 | rebalance down |
| 2026-10-06T16:56 | MFI reversion | sell | TQQQ | 3.86 | -0.01 | rebalance down |
| 2026-10-06T16:56 | MFI reversion | sell | TECL | 3.93 | -0.01 | rebalance down |
| 2026-10-06T16:56 | MFI reversion | sell | QQQ | 3.91 | -0.00 | rebalance down |
| 2026-10-06T16:56 | MFI reversion | sell | MSFT | 3.91 | -0.01 | rebalance down |
| 2026-10-06T16:56 | MFI reversion | sell | DOGE-USD | 3.94 | -0.02 | rebalance down |
| 2026-10-06T16:56 | Bollinger reversion | buy | AAPL | 4.17 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 17:00:05.000144+00:00 -> 2026-10-06 17:10:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
