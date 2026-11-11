# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T23:40:05.000128+00:00 · 56240 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.91 (-14.09%)

Closed trades 181, win rate 35.4%, fees £5.39, max drawdown -14.66%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 38952 decisions in 3306 calls, $0.4822 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T23:40 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-11T23:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-11T23:40 | 2 / 3 / 0 | ETH-USD 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.34 | 16.34 | 0 | — | 16.04 | 5.30 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.62 | 15.62 | 20 | 70.0 | 17.89 | 3.60 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.69 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.93 | 3.93 | 0 | — | 6.40 | 1.76 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Gap and go | momentum | 100.36 | 0.36 | 191 | 33.0 | 6.64 | 1.88 | -9.06 | 232 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.71 | -0.29 | 134 | 34.3 | 10.31 | 3.58 | -3.28 | 85 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.55 | -1.45 | 0 | — | -0.64 | -0.14 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.07 | -1.93 | 188 | 30.3 | -3.04 | -1.11 | -9.86 | 165 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.08 | -2.92 | 0 | — | -2.23 | -0.51 | -9.25 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.19 | -13.44 | 153 |
| 16 | Copy: Insider buying | copy | 95.51 | -4.49 | 43 | 39.5 | -5.77 | -1.11 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.43 | -5.57 | 0 | — | -3.37 | -0.86 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 20 | Trend pullback · 1h | trend | 91.71 | -8.29 | 109 | 22.9 | -13.50 | -5.04 | -16.41 | 76 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.82 | -11.18 | 404 | 33.2 | -12.12 | -3.89 | -14.11 | 597 |
| 23 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -4.89 | -0.99 | -17.04 | 78 |
| 24 | Max aggression: 5-day momentum | meta | 87.61 | -12.39 | 19 | 47.4 | -27.43 | -1.45 | -45.81 | 25 |
| 25 | Hold BTC | benchmark | 86.78 | -13.22 | 1 | 0.0 | -4.08 | -0.48 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.48 | -13.52 | 168 | 26.8 | -14.15 | -3.00 | -21.94 | 224 |
| 27 | Agent | meta | 85.91 | -14.09 | 181 | 35.4 | -14.97 | -7.46 | -15.33 | 209 |
| 28 | Daily: Bullish score | daily | 84.40 | -15.60 | 16 | 18.8 | -9.91 | -1.55 | -19.56 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 84.19 | -15.81 | 2 | 0.0 | -6.49 | -0.67 | -24.16 | 1 |
| 30 | Agent (aggressive) | meta | 83.84 | -16.16 | 88 | 34.1 | -16.78 | -4.70 | -18.51 | 97 |
| 31 | Donchian 55/20 · 1h | breakout | 82.96 | -17.04 | 72 | 13.9 | -22.99 | -4.88 | -29.34 | 92 |
| 32 | ADX DI cross · 1h | trend | 82.28 | -17.72 | 186 | 18.8 | -21.91 | -3.73 | -29.87 | 274 |
| 33 | Stochastic reversion · 1h | reversion | 82.22 | -17.78 | 292 | 48.3 | -23.72 | -3.46 | -27.08 | 391 |
| 34 | Keltner breakout · 1h | breakout | 82.01 | -17.99 | 111 | 24.3 | -16.80 | -3.44 | -24.55 | 169 |
| 35 | Max aggression: 1-day momentum | meta | 81.21 | -18.79 | 27 | 25.9 | -17.50 | -0.43 | -57.50 | 40 |
| 36 | Opening range 15m | breakout | 80.86 | -19.14 | 501 | 31.3 | -18.42 | -5.02 | -21.11 | 722 |
| 37 | Volume breakout · 1h | breakout | 80.79 | -19.21 | 149 | 27.5 | -12.79 | -2.93 | -21.11 | 95 |
| 38 | Connors RSI(2) · 1h | reversion | 80.31 | -19.69 | 208 | 39.9 | -20.43 | -6.87 | -20.86 | 123 |
| 39 | Heikin-Ashi · 1h | trend | 80.25 | -19.75 | 418 | 24.6 | -36.37 | -6.78 | -39.57 | 663 |
| 40 | MFI reversion · 1h | reversion | 79.37 | -20.63 | 374 | 35.6 | -16.01 | -2.05 | -23.02 | 158 |
| 41 | CCI reversion · 1h | reversion | 78.14 | -21.86 | 332 | 45.2 | -27.76 | -4.28 | -31.08 | 447 |
| 42 | MACD cross · 1h | trend | 78.11 | -21.89 | 363 | 22.0 | -27.57 | -4.01 | -39.83 | 463 |
| 43 | Bollinger breakout · 1h | breakout | 76.98 | -23.02 | 176 | 22.2 | -21.58 | -4.59 | -28.24 | 240 |
| 44 | Bollinger reversion · 1h | reversion | 75.99 | -24.01 | 286 | 41.6 | -27.67 | -4.22 | -34.84 | 367 |
| 45 | MACD zero-line · 1h | trend | 75.74 | -24.26 | 162 | 16.7 | -20.72 | -4.06 | -30.74 | 210 |
| 46 | Supertrend · 1h | trend | 75.40 | -24.60 | 168 | 13.1 | -28.85 | -5.06 | -36.14 | 221 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 48 | RSI momentum · 1h | momentum | 74.95 | -25.05 | 159 | 12.6 | -26.39 | -4.01 | -37.48 | 217 |
| 49 | Daily: Momentum burst | daily | 74.83 | -25.17 | 27 | 11.1 | -33.22 | -4.49 | -38.23 | 33 |
| 50 | EMA 20/50 cross · 1h | trend | 74.43 | -25.57 | 103 | 10.7 | -27.05 | -4.58 | -37.26 | 118 |
| 51 | Triple EMA stack · 1h | trend | 74.08 | -25.91 | 144 | 14.6 | -25.47 | -4.20 | -35.90 | 210 |
| 52 | ROC + volume · 1h | momentum | 72.92 | -27.08 | 377 | 27.6 | -32.24 | -5.90 | -38.40 | 380 |
| 53 | Williams %R · 1h | reversion | 72.37 | -27.63 | 353 | 46.2 | -35.44 | -5.48 | -36.33 | 525 |
| 54 | Donchian 20/10 · 1h | breakout | 71.94 | -28.06 | 144 | 19.4 | -28.32 | -5.20 | -35.64 | 209 |
| 55 | OBV trend · 1h | momentum | 71.78 | -28.22 | 281 | 19.2 | -28.94 | -5.03 | -37.06 | 294 |
| 56 | Z-score reversion · 1h | reversion | 71.14 | -28.86 | 197 | 38.6 | -23.07 | -3.19 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.09 | -30.91 | 175 | 32.6 | -27.00 | -3.90 | -32.54 | 226 |
| 58 | VWAP momentum · 1h | momentum | 67.91 | -32.09 | 865 | 22.7 | -51.02 | -10.53 | -53.63 | 1226 |
| 59 | EMA 9/21 cross · 1h | trend | 67.22 | -32.78 | 254 | 9.8 | -33.04 | -6.23 | -41.65 | 335 |
| 60 | Agent (ML meta-label) | meta | 66.37 | -33.63 | 1750 | 24.7 | -5.97 | -0.62 | -19.53 | 335 |
| 61 | Candlestick reversal · 1h | reversion | 65.54 | -34.47 | 460 | 28.9 | -37.78 | -6.67 | -40.65 | 576 |
| 62 | Three white soldiers | momentum | 60.27 | -39.73 | 520 | 15.0 | -49.37 | -22.67 | -49.49 | 655 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -45.10 | -99.00 | 5283 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.69 | -25.50 | -80.39 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.54 | -45.17 | -93.66 | 2528 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.27 | -32.06 | -89.48 | 1922 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.05 | -40.48 | -91.30 | 2337 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.44 | -33.02 | -90.44 | 2211 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -53.14 | -97.82 | 3464 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -59.05 | -96.42 | 3439 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -33.17 | -93.56 | 2351 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.18 | -34.64 | -83.50 | 1671 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -55.14 | -99.55 | 5977 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.06 | -42.47 | -92.34 | 2612 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.60 | -38.85 | -95.60 | 3469 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -75.08 | -99.80 | 6132 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -42.44 | -91.98 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.51 | -24.40 | -75.85 | 1628 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -63.12 | -97.71 | 3528 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.97 | -98.84 | 4899 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.42 | -27.03 | -68.91 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -54.10 | -94.76 | 2784 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.63 | -36.82 | -85.18 | 1786 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -76.37 | -99.64 | 6333 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.52 | -32.54 | -89.52 | 2290 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.62 | -19.93 | -77.65 | 1749 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.71 | -37.06 | -90.71 | 2178 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.77 | -53.06 | -96.78 | 3844 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.04 | -57.60 | -89.06 | 2137 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.70 | -29.19 | -66.45 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.38 | -23.04 | -72.14 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.00 | -18.33 | -78.38 | 1681 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -49.74 | -97.27 | 4292 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.92 | -99.93 | 8361 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T23:15 | Donchian 20/10 · 1h | sell | BTC-USD | 6.39 | -0.08 | stop-loss |
| 2026-11-11T23:15 | MACD zero-line · 1h | sell | BTC-USD | 4.27 | -0.04 | stop-loss |
| 2026-11-11T23:15 | EMA 9/21 cross · 1h | sell | SOL-USD | 4.68 | -0.11 | stop-loss |
| 2026-11-11T23:10 | MACD zero-line · 1h | buy | BTC-USD | 4.30 | — | entry |
| 2026-11-11T23:10 | MACD zero-line · 1h | sell | SOL-USD | 4.30 | -0.12 | stop-loss |
| 2026-11-11T23:00 | Squeeze breakout · 1h | sell | BTC-USD | 21.86 | -0.29 | exit signal |
| 2026-11-11T23:00 | Bollinger breakout · 1h | sell | BTC-USD | 10.95 | -0.13 | exit signal |
| 2026-11-11T23:00 | Donchian 20/10 · 1h | buy | BTC-USD | 6.46 | — | entry |
| 2026-11-11T23:00 | Donchian 20/10 · 1h | sell | SOL-USD | 6.46 | -0.10 | exit signal |
| 2026-11-11T23:00 | ROC + volume · 1h | sell | SOL-USD | 7.19 | -0.10 | exit signal |
| 2026-11-11T23:00 | VWAP momentum · 1h | sell | SOL-USD | 4.75 | -0.06 | exit signal |
| 2026-11-11T23:00 | VWAP momentum · 1h | sell | ETH-USD | 6.76 | -0.08 | exit signal |
| 2026-11-11T23:00 | VWAP momentum · 1h | sell | BTC-USD | 4.24 | -0.03 | exit signal |
| 2026-11-11T23:00 | ADX DI cross · 1h | sell | SOL-USD | 8.98 | -0.12 | exit signal |
| 2026-11-11T23:00 | MACD cross · 1h | buy | SOL-USD | 3.81 | — | entry |
| 2026-11-11T23:00 | MACD cross · 1h | sell | DOGE-USD | 3.81 | -0.07 | exit signal |
| 2026-11-11T22:46 | Squeeze breakout · 1h | sell | SOL-USD | 21.77 | -0.41 | stop-loss |
| 2026-11-11T22:46 | Bollinger breakout · 1h | buy | BTC-USD | 3.94 | — | rebalance up |
| 2026-11-11T22:46 | Bollinger breakout · 1h | sell | SOL-USD | 7.00 | -0.09 | stop-loss |
| 2026-11-11T22:46 | Bollinger breakout · 1h | sell | ETH-USD | 7.01 | -0.10 | stop-loss |
| 2026-11-11T22:46 | VWAP momentum · 1h | buy | ETH-USD | 3.73 | — | rebalance up |
| 2026-11-11T22:46 | VWAP momentum · 1h | sell | DOGE-USD | 6.09 | -0.13 | stop-loss |
| 2026-11-11T22:40 | Bollinger breakout · 1h | sell | DOGE-USD | 7.00 | -0.16 | stop-loss |
| 2026-11-11T22:14 | Volume breakout · 1h | sell | ETH-USD | 13.47 | -0.11 | target is flat |
| 2026-11-11T22:14 | Squeeze breakout · 1h | buy | BTC-USD | 22.15 | — | entry |
| 2026-11-11T22:14 | VWAP momentum · 1h | buy | DOGE-USD | 4.19 | — | rebalance up |
| 2026-11-11T20:15 | Agent (rotation) | sell | TSLA | 8.14 | -0.04 | selected signal exited |
| 2026-11-11T20:15 | Day trade: Stocks in Play ORB | sell | TSLA | 24.90 | -0.13 | target is flat |
| 2026-11-11T20:15 | Agent (ML meta-label) | sell | TQQQ | 9.48 | -0.03 | selected signal exited |
| 2026-11-11T20:10 | VWAP momentum · 1h | sell | SPY | 5.16 | 0.10 | target is flat |
| 2026-11-11T20:05 | Agent (ML meta-label) | buy | TQQQ | 9.50 | — | entry |
| 2026-11-11T20:05 | Agent (ML meta-label) | buy | GOOGL | 9.51 | — | entry |
| 2026-11-11T20:05 | Agent (ML meta-label) | buy | AMZN | 9.51 | — | following Supertrend |
| 2026-11-11T20:05 | Agent (ML meta-label) | buy | AAPL | 9.51 | — | entry |
| 2026-11-11T20:05 | Agent (ML meta-label) | sell | TSLA | 7.15 | -0.02 | rebalance down |
| 2026-11-11T20:05 | Agent (ML meta-label) | sell | TECL | 7.11 | -0.10 | rebalance down |
| 2026-11-11T20:05 | Agent (ML meta-label) | sell | AMD | 7.08 | -0.05 | rebalance down |
| 2026-11-11T20:05 | EMA 20/50 cross · 1h | buy | SPY | 3.74 | — | rebalance up |
| 2026-11-11T20:05 | EMA 20/50 cross · 1h | sell | META | 3.74 | -0.01 | rebalance down |
| 2026-11-11T20:00 | Bollinger breakout · 1h | sell | XRP-USD | 7.04 | -0.13 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 23:40:05.000128+00:00 -> 2026-11-11 23:50:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
