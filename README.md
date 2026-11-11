# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T14:24:05.000123+00:00 · 55867 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.46 (-12.54%)

Closed trades 172, win rate 35.5%, fees £5.15, max drawdown -13.61%.

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

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.57 · VIX 19.46 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 10935 decisions in 2187 calls, $0.1528 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T14:24 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-11T14:24 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-11T14:24 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| MFI reversion | LABU | 2.03 | +7.94% | 4 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 20.23 | 4.05 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.06 | 15.06 | 0 | — | 15.13 | 5.00 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.87 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.55 | 1.55 | 0 | — | 4.26 | 1.24 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.80 | 1.13 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -4.33 | -1.77 | -9.87 | 155 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 97.00 | -3.00 | 0 | — | -1.28 | -0.38 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 95.25 | -4.75 | 0 | — | -4.27 | -1.11 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.11 | -3.80 | -5.99 | 27 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Insider buying | copy | 93.09 | -6.92 | 43 | 39.5 | -8.00 | -1.64 | -15.11 | 67 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.87 | -7.13 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 92.75 | -7.25 | 108 | 23.1 | -12.81 | -4.75 | -16.85 | 78 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.53 | -3.13 | -15.49 | 80 |
| 23 | Opening range 30m | breakout | 88.22 | -11.78 | 404 | 33.2 | -15.00 | -4.57 | -15.00 | 604 |
| 24 | Agent | meta | 87.46 | -12.54 | 172 | 35.5 | -13.28 | -6.71 | -14.21 | 201 |
| 25 | Daily: Bullish score | daily | 86.50 | -13.50 | 15 | 20.0 | -4.92 | -0.64 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 86.26 | -13.74 | 1 | 0.0 | -4.89 | -0.60 | -16.64 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.67 | -14.33 | 168 | 26.8 | -13.63 | -2.77 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.97 | -15.03 | 81 | 33.3 | -15.80 | -4.42 | -18.49 | 94 |
| 29 | Donchian 55/20 · 1h | breakout | 84.12 | -15.88 | 71 | 14.1 | -22.52 | -4.75 | -27.94 | 100 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.53 | -17.47 | 2 | 0.0 | -8.31 | -0.93 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.68 | -18.32 | 110 | 23.6 | -18.31 | -3.71 | -24.55 | 165 |
| 32 | Stochastic reversion · 1h | reversion | 81.41 | -18.59 | 287 | 47.7 | -24.54 | -3.60 | -27.06 | 390 |
| 33 | Connors RSI(2) · 1h | reversion | 80.96 | -19.04 | 207 | 40.1 | -19.42 | -6.44 | -19.98 | 125 |
| 34 | Opening range 15m | breakout | 80.79 | -19.21 | 500 | 31.4 | -20.74 | -5.58 | -20.74 | 733 |
| 35 | Max aggression: 5-day momentum | meta | 80.55 | -19.45 | 18 | 44.4 | -33.09 | -2.01 | -45.81 | 24 |
| 36 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -13.97 | -3.22 | -21.11 | 92 |
| 37 | ADX DI cross · 1h | trend | 79.53 | -20.47 | 185 | 18.9 | -25.32 | -4.36 | -30.45 | 274 |
| 38 | Heikin-Ashi · 1h | trend | 79.00 | -21.00 | 417 | 24.5 | -39.93 | -7.38 | -42.28 | 665 |
| 39 | CCI reversion · 1h | reversion | 77.00 | -23.00 | 327 | 45.0 | -26.44 | -3.99 | -30.86 | 453 |
| 40 | MFI reversion · 1h | reversion | 76.91 | -23.09 | 366 | 34.4 | -16.77 | -2.14 | -22.43 | 157 |
| 41 | Bollinger breakout · 1h | breakout | 76.68 | -23.32 | 171 | 22.8 | -21.83 | -4.54 | -28.16 | 236 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.15 | -8.75 | -31.64 | 118 |
| 43 | MACD cross · 1h | trend | 75.10 | -24.90 | 360 | 21.9 | -31.86 | -5.19 | -39.47 | 479 |
| 44 | EMA 20/50 cross · 1h | trend | 75.02 | -24.98 | 102 | 10.8 | -25.82 | -4.40 | -36.26 | 114 |
| 45 | Bollinger reversion · 1h | reversion | 74.31 | -25.69 | 283 | 41.0 | -26.20 | -3.99 | -32.30 | 371 |
| 46 | MACD zero-line · 1h | trend | 74.04 | -25.96 | 159 | 16.4 | -23.10 | -4.65 | -31.08 | 208 |
| 47 | Supertrend · 1h | trend | 73.73 | -26.27 | 168 | 13.1 | -28.54 | -4.93 | -36.14 | 222 |
| 48 | RSI momentum · 1h | momentum | 73.56 | -26.44 | 159 | 12.6 | -24.93 | -4.02 | -34.73 | 208 |
| 49 | Triple EMA stack · 1h | trend | 72.36 | -27.64 | 144 | 14.6 | -28.90 | -5.12 | -36.37 | 210 |
| 50 | Williams %R · 1h | reversion | 71.86 | -28.14 | 349 | 45.8 | -35.18 | -5.50 | -36.23 | 531 |
| 51 | OBV trend · 1h | momentum | 71.78 | -28.22 | 277 | 18.4 | -28.94 | -5.27 | -35.84 | 285 |
| 52 | ROC + volume · 1h | momentum | 71.27 | -28.73 | 369 | 27.1 | -35.59 | -6.68 | -38.52 | 377 |
| 53 | Daily: Momentum burst | daily | 71.20 | -28.80 | 27 | 11.1 | -34.82 | -4.87 | -38.23 | 34 |
| 54 | Donchian 20/10 · 1h | breakout | 70.80 | -29.20 | 142 | 19.7 | -31.10 | -5.81 | -35.64 | 205 |
| 55 | Z-score reversion · 1h | reversion | 70.62 | -29.38 | 190 | 36.3 | -25.76 | -3.73 | -28.98 | 234 |
| 56 | Max aggression: 1-day momentum | meta | 68.51 | -31.49 | 27 | 25.9 | -30.21 | -1.48 | -57.50 | 40 |
| 57 | RSI(14) reversion · 1h | reversion | 66.99 | -33.01 | 171 | 31.0 | -31.43 | -4.85 | -33.96 | 230 |
| 58 | VWAP momentum · 1h | momentum | 65.94 | -34.06 | 843 | 21.8 | -53.98 | -11.49 | -55.22 | 1236 |
| 59 | EMA 9/21 cross · 1h | trend | 65.72 | -34.28 | 252 | 9.9 | -37.79 | -7.59 | -41.74 | 337 |
| 60 | Agent (ML meta-label) | meta | 65.65 | -34.35 | 1700 | 24.5 | -14.48 | -2.38 | -19.04 | 334 |
| 61 | Candlestick reversal · 1h | reversion | 63.83 | -36.17 | 454 | 28.4 | -38.65 | -7.13 | -40.52 | 591 |
| 62 | Three white soldiers | momentum | 60.26 | -39.74 | 513 | 14.6 | -49.30 | -22.65 | -49.30 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -45.41 | -99.04 | 5322 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.94 | -26.16 | -80.06 | 1431 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.55 | -46.46 | -93.55 | 2540 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.46 | -31.98 | -89.47 | 1930 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.09 | -39.83 | -91.13 | 2341 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.39 | -32.11 | -90.40 | 2228 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -53.86 | -97.83 | 3477 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -58.03 | -96.35 | 3462 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -32.24 | -93.69 | 2360 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.08 | -34.20 | -83.21 | 1683 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -52.64 | -99.54 | 5960 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.25 | -43.16 | -92.25 | 2619 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.58 | -37.28 | -95.58 | 3446 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.20 | -99.80 | 6165 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.18 | -44.06 | -92.18 | 2284 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.95 | -24.98 | -75.95 | 1618 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.82 | -97.75 | 3539 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -61.07 | -98.84 | 4895 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.87 | -27.44 | -69.09 | 1238 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -54.30 | -94.75 | 2792 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.96 | -37.58 | -85.14 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -70.80 | -99.63 | 6335 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.37 | -31.35 | -89.46 | 2283 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.42 | -19.44 | -77.75 | 1737 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.45 | -35.56 | -90.53 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.68 | -50.30 | -96.68 | 3839 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.17 | -55.38 | -89.17 | 2148 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.66 | -27.84 | -66.53 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.31 | -22.58 | -71.79 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.48 | -18.51 | -78.82 | 1674 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.15 | -47.09 | -97.16 | 4286 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -103.06 | -99.93 | 8338 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T14:10 | Three white soldiers | sell | XRP-USD | 14.97 | -0.13 | exit signal |
| 2026-11-11T14:00 | RSI(14) reversion · 1h | sell | SOL-USD | 11.24 | 0.16 | exit signal |
| 2026-11-11T14:00 | Candlestick reversal · 1h | sell | SOL-USD | 4.64 | 0.05 | exit signal |
| 2026-11-11T14:00 | Bollinger breakout · 1h | buy | SOL-USD | 19.22 | — | entry signal |
| 2026-11-11T14:00 | Donchian 20/10 · 1h | buy | SOL-USD | 17.74 | — | entry signal |
| 2026-11-11T14:00 | ROC + volume · 1h | buy | SOL-USD | 14.28 | — | entry signal |
| 2026-11-11T13:55 | Three white soldiers | buy | XRP-USD | 15.10 | — | entry signal |
| 2026-11-11T13:35 | MFI reversion · 1h | sell | XRP-USD | 6.37 | -0.05 | rebalance down |
| 2026-11-11T13:05 | MFI reversion · 1h | buy | XRP-USD | 6.46 | — | rebalance up |
| 2026-11-11T13:00 | Candlestick reversal · 1h | buy | ETH-USD | 7.10 | — | entry |
| 2026-11-11T13:00 | Candlestick reversal · 1h | sell | DOGE-USD | 9.15 | 0.03 | exit signal |
| 2026-11-11T12:00 | Heikin-Ashi · 1h | buy | SOL-USD | 19.76 | — | entry signal |
| 2026-11-11T11:00 | MFI reversion · 1h | sell | XRP-USD | 6.41 | -0.02 | rebalance down |
| 2026-11-11T11:00 | CCI reversion · 1h | buy | DOGE-USD | 4.32 | — | entry |
| 2026-11-11T11:00 | CCI reversion · 1h | sell | BTC-USD | 4.32 | -0.01 | exit signal |
| 2026-11-11T11:00 | Williams %R · 1h | sell | SOL-USD | 6.55 | 0.03 | exit signal |
| 2026-11-11T11:00 | Stochastic reversion · 1h | sell | SOL-USD | 9.07 | 0.11 | exit signal |
| 2026-11-11T09:57 | MFI reversion · 1h | buy | XRP-USD | 6.38 | — | rebalance up |
| 2026-11-11T09:26 | MFI reversion · 1h | sell | XRP-USD | 6.36 | -0.05 | rebalance down |
| 2026-11-11T08:00 | MFI reversion · 1h | buy | XRP-USD | 4.00 | — | rebalance up |
| 2026-11-11T08:00 | MFI reversion · 1h | sell | DOGE-USD | 15.37 | -0.07 | exit signal |
| 2026-11-11T08:00 | Candlestick reversal · 1h | buy | SOL-USD | 4.59 | — | entry signal |
| 2026-11-11T08:00 | Candlestick reversal · 1h | buy | BTC-USD | 7.09 | — | entry signal |
| 2026-11-11T08:00 | VWAP momentum · 1h | buy | BTC-USD | 4.12 | — | entry signal |
| 2026-11-11T07:25 | MFI reversion · 1h | buy | XRP-USD | 4.25 | — | rebalance up |
| 2026-11-11T07:25 | MFI reversion · 1h | buy | DOGE-USD | 4.40 | — | rebalance up |
| 2026-11-11T07:00 | Candlestick reversal · 1h | buy | XRP-USD | 4.16 | — | rebalance up |
| 2026-11-11T07:00 | Candlestick reversal · 1h | buy | DOGE-USD | 9.11 | — | entry |
| 2026-11-11T07:00 | Candlestick reversal · 1h | sell | SOL-USD | 7.90 | -0.04 | exit signal |
| 2026-11-11T07:00 | Candlestick reversal · 1h | sell | ETH-USD | 9.12 | 0.05 | exit signal |
| 2026-11-11T07:00 | Candlestick reversal · 1h | sell | BTC-USD | 7.94 | -0.06 | exit signal |
| 2026-11-11T07:00 | VWAP momentum · 1h | sell | ETH-USD | 4.67 | -0.03 | exit signal |
| 2026-11-11T06:25 | MFI reversion · 1h | sell | XRP-USD | 4.32 | -0.03 | rebalance down |
| 2026-11-11T06:25 | MFI reversion · 1h | sell | DOGE-USD | 4.33 | -0.03 | rebalance down |
| 2026-11-11T06:00 | Williams %R · 1h | sell | ETH-USD | 6.55 | 0.03 | exit signal |
| 2026-11-11T06:00 | Williams %R · 1h | sell | BTC-USD | 6.52 | 0.00 | exit signal |
| 2026-11-11T06:00 | Stochastic reversion · 1h | buy | DOGE-USD | 9.03 | — | entry |
| 2026-11-11T06:00 | Stochastic reversion · 1h | sell | ETH-USD | 9.10 | 0.11 | exit signal |
| 2026-11-11T06:00 | Stochastic reversion · 1h | sell | BTC-USD | 9.01 | 0.00 | exit signal |
| 2026-11-11T06:00 | VWAP reversion · 1h | sell | SOL-USD | 23.90 | 0.09 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 14:24:05.000123+00:00 -> 2026-11-11 14:34:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
