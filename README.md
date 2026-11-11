# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T16:54:05.000141+00:00 · 55974 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.11 (-13.89%)

Closed trades 174, win rate 35.1%, fees £5.23, max drawdown -14.29%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.41 | +0.07 |
| SQQQ | 34.13 | -0.42 |

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

Today: 20355 decisions in 2508 calls, $0.2627 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T16:54 | 7 / 10 / 13 | SOXL 15% |  |
| Breezy | 2026-11-11T16:54 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-11T16:54 | 8 / 20 / 2 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| MFI reversion | LABU | 1.66 | +5.37% | 3 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.11 | 3.83 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.34 | 14.34 | 0 | — | 14.42 | 4.73 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.67 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.11 | 4.11 | 31 | 45.2 | 4.26 | 1.10 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.36 | 3.36 | 0 | — | 5.87 | 1.63 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.13 | 0.12 | 184 | 30.4 | 7.12 | 1.99 | -9.06 | 247 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.83 | -0.17 | 133 | 34.6 | 10.47 | 3.61 | -3.20 | 85 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 11 | Agent (rotation) | meta | 98.53 | -1.47 | 181 | 28.2 | -1.26 | -0.41 | -8.46 | 165 |
| 12 | Hold SPY | benchmark | 98.48 | -1.52 | 0 | — | 0.11 | 0.12 | -6.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.11 | -3.89 | 0 | — | -3.14 | -0.78 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.32 | -5.68 | 0 | — | -3.62 | -0.93 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 93.99 | -6.01 | 43 | 39.5 | -7.17 | -1.44 | -15.11 | 67 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.59 | -3.30 | -5.99 | 26 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.62 | -8.38 | 109 | 22.9 | -16.23 | -5.69 | -18.84 | 80 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Max aggression: 5-day momentum | meta | 90.98 | -9.02 | 19 | 47.4 | -24.60 | -1.15 | -45.81 | 25 |
| 23 | Opening range 30m | breakout | 89.34 | -10.66 | 404 | 33.2 | -12.99 | -3.91 | -14.11 | 597 |
| 24 | Squeeze breakout · 1h | breakout | 88.63 | -11.37 | 64 | 21.9 | -7.90 | -2.74 | -14.28 | 76 |
| 25 | Hold BTC | benchmark | 87.20 | -12.80 | 1 | 0.0 | -4.36 | -0.52 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.59 | -13.41 | 168 | 26.8 | -14.10 | -2.96 | -21.98 | 225 |
| 27 | Agent | meta | 86.11 | -13.89 | 174 | 35.1 | -15.06 | -7.58 | -15.15 | 204 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 85.26 | -14.74 | 2 | 0.0 | -4.88 | -0.43 | -24.16 | 1 |
| 29 | Max aggression: 1-day momentum | meta | 84.33 | -15.67 | 27 | 25.9 | -14.29 | -0.19 | -57.50 | 40 |
| 30 | Daily: Bullish score | daily | 84.17 | -15.83 | 16 | 18.8 | -8.55 | -1.27 | -19.33 | 15 |
| 31 | Agent (aggressive) | meta | 83.94 | -16.06 | 84 | 33.3 | -18.05 | -5.11 | -18.51 | 97 |
| 32 | Donchian 55/20 · 1h | breakout | 83.37 | -16.63 | 72 | 13.9 | -23.19 | -4.81 | -29.08 | 97 |
| 33 | ADX DI cross · 1h | trend | 83.05 | -16.95 | 185 | 18.9 | -21.96 | -3.46 | -30.90 | 274 |
| 34 | Keltner breakout · 1h | breakout | 83.02 | -16.98 | 110 | 23.6 | -18.03 | -3.66 | -25.10 | 182 |
| 35 | Stochastic reversion · 1h | reversion | 82.11 | -17.89 | 290 | 47.9 | -24.02 | -3.45 | -27.09 | 391 |
| 36 | Volume breakout · 1h | breakout | 81.51 | -18.49 | 148 | 27.7 | -12.61 | -2.84 | -21.11 | 98 |
| 37 | Opening range 15m | breakout | 81.36 | -18.64 | 501 | 31.3 | -18.75 | -5.03 | -21.11 | 732 |
| 38 | Heikin-Ashi · 1h | trend | 80.79 | -19.21 | 417 | 24.5 | -38.48 | -7.00 | -42.11 | 673 |
| 39 | Connors RSI(2) · 1h | reversion | 80.06 | -19.93 | 208 | 39.9 | -20.76 | -6.91 | -20.80 | 124 |
| 40 | MFI reversion · 1h | reversion | 79.85 | -20.15 | 372 | 35.2 | -16.22 | -1.99 | -23.02 | 158 |
| 41 | MACD cross · 1h | trend | 78.62 | -21.38 | 362 | 22.1 | -28.80 | -4.57 | -38.69 | 474 |
| 42 | Bollinger breakout · 1h | breakout | 78.08 | -21.92 | 171 | 22.8 | -19.79 | -3.99 | -28.24 | 245 |
| 43 | CCI reversion · 1h | reversion | 77.92 | -22.08 | 331 | 45.0 | -26.67 | -4.03 | -31.08 | 452 |
| 44 | MACD zero-line · 1h | trend | 76.29 | -23.71 | 160 | 16.9 | -20.66 | -3.85 | -31.20 | 212 |
| 45 | Bollinger reversion · 1h | reversion | 75.92 | -24.08 | 285 | 41.4 | -24.65 | -3.67 | -32.54 | 371 |
| 46 | Supertrend · 1h | trend | 75.48 | -24.52 | 168 | 13.1 | -28.20 | -4.80 | -36.07 | 229 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 48 | RSI momentum · 1h | momentum | 75.36 | -24.64 | 159 | 12.6 | -25.14 | -3.74 | -37.44 | 212 |
| 49 | Daily: Momentum burst | daily | 75.05 | -24.95 | 27 | 11.1 | -31.84 | -4.15 | -38.23 | 33 |
| 50 | EMA 20/50 cross · 1h | trend | 74.87 | -25.13 | 102 | 10.8 | -25.92 | -4.40 | -36.22 | 115 |
| 51 | Triple EMA stack · 1h | trend | 74.18 | -25.82 | 144 | 14.6 | -26.52 | -4.40 | -36.52 | 209 |
| 52 | ROC + volume · 1h | momentum | 73.55 | -26.45 | 376 | 27.7 | -33.71 | -6.04 | -39.15 | 388 |
| 53 | Williams %R · 1h | reversion | 72.86 | -27.14 | 352 | 46.0 | -35.54 | -5.47 | -37.07 | 528 |
| 54 | Donchian 20/10 · 1h | breakout | 72.74 | -27.26 | 142 | 19.7 | -29.31 | -5.29 | -35.64 | 216 |
| 55 | OBV trend · 1h | momentum | 71.79 | -28.21 | 279 | 18.6 | -26.20 | -4.62 | -34.92 | 285 |
| 56 | Z-score reversion · 1h | reversion | 71.62 | -28.38 | 195 | 37.9 | -22.54 | -3.04 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.12 | -30.88 | 174 | 32.2 | -25.12 | -3.51 | -32.54 | 234 |
| 58 | VWAP momentum · 1h | momentum | 68.51 | -31.50 | 851 | 22.2 | -51.85 | -10.45 | -54.81 | 1239 |
| 59 | EMA 9/21 cross · 1h | trend | 67.57 | -32.43 | 253 | 9.9 | -34.29 | -6.34 | -41.69 | 335 |
| 60 | Agent (ML meta-label) | meta | 67.02 | -32.98 | 1724 | 24.8 | -8.09 | -1.15 | -18.87 | 338 |
| 61 | Candlestick reversal · 1h | reversion | 65.19 | -34.81 | 459 | 28.8 | -37.16 | -6.64 | -39.74 | 587 |
| 62 | Three white soldiers | momentum | 60.23 | -39.77 | 515 | 14.8 | -49.18 | -22.50 | -49.19 | 654 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -45.25 | -99.05 | 5327 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.91 | -25.80 | -80.49 | 1425 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -44.84 | -93.55 | 2550 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.35 | -31.67 | -89.42 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.95 | -38.73 | -91.22 | 2343 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.27 | -32.04 | -90.41 | 2206 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -52.95 | -97.84 | 3464 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -56.84 | -96.40 | 3467 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.27 | -31.75 | -93.48 | 2345 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.13 | -33.92 | -83.48 | 1677 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -53.48 | -99.54 | 5950 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.23 | -42.33 | -92.31 | 2628 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -37.35 | -95.55 | 3433 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.89 | -99.80 | 6129 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.00 | -42.28 | -92.02 | 2273 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.71 | -24.61 | -75.46 | 1640 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -58.83 | -97.73 | 3539 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -61.28 | -98.84 | 4886 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.33 | -26.33 | -69.04 | 1246 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -52.52 | -94.75 | 2787 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.80 | -36.68 | -85.22 | 1797 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.55 | -99.63 | 6323 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.46 | -31.71 | -89.46 | 2285 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.44 | -19.50 | -77.68 | 1740 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.51 | -35.95 | -90.61 | 2184 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.68 | -50.47 | -96.69 | 3823 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -54.23 | -89.11 | 2136 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.49 | -27.52 | -66.78 | 824 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.06 | -22.29 | -72.05 | 1268 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.34 | -18.40 | -78.61 | 1697 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.17 | -47.49 | -97.17 | 4276 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -99.53 | -99.93 | 8349 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T16:50 | Agent (ML meta-label) | buy | TECL | 16.76 | — | entry |
| 2026-11-11T16:50 | Agent (ML meta-label) | buy | COIN | 13.57 | — | following Donchian 20/10 |
| 2026-11-11T16:45 | Agent (ML meta-label) | sell | COIN | 9.66 | -0.06 | selected signal exited |
| 2026-11-11T16:45 | Agent (aggressive) | buy | COIN | 41.98 | — | following Donchian 20/10 |
| 2026-11-11T16:45 | Three white soldiers | sell | COIN | 15.07 | 0.00 | exit signal |
| 2026-11-11T16:41 | Triple EMA stack · 1h | buy | LABU | 3.73 | — | rebalance up |
| 2026-11-11T16:41 | Triple EMA stack · 1h | sell | AAPL | 3.73 | 0.07 | rebalance down |
| 2026-11-11T16:41 | Three white soldiers | sell | IWM | 15.04 | -0.04 | exit signal |
| 2026-11-11T16:35 | Agent (ML meta-label) | buy | COIN | 9.72 | — | following Donchian 20/10 |
| 2026-11-11T16:35 | Agent (ML meta-label) | sell | TSLA | 16.72 | -0.05 | selected signal exited |
| 2026-11-11T16:35 | Agent (ML meta-label) | sell | TECL | 16.75 | -0.02 | selected signal exited |
| 2026-11-11T16:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 103.97 | — | entry |
| 2026-11-11T16:30 | Williams %R · 1h | buy | META | 12.18 | — | entry signal |
| 2026-11-11T16:30 | Williams %R · 1h | sell | GOOGL | 10.26 | 0.15 | exit signal |
| 2026-11-11T16:30 | Williams %R · 1h | sell | COIN | 10.51 | 0.39 | exit signal |
| 2026-11-11T16:30 | Stochastic reversion · 1h | buy | NVDA | 7.06 | — | rebalance up |
| 2026-11-11T16:30 | Stochastic reversion · 1h | buy | MSTR | 7.21 | — | rebalance up |
| 2026-11-11T16:30 | Stochastic reversion · 1h | buy | ETHU | 7.03 | — | rebalance up |
| 2026-11-11T16:30 | Stochastic reversion · 1h | buy | DOGE-USD | 7.33 | — | rebalance up |
| 2026-11-11T16:30 | Stochastic reversion · 1h | buy | BITX | 7.23 | — | rebalance up |
| 2026-11-11T16:30 | Stochastic reversion · 1h | sell | GOOGL | 10.18 | 0.03 | exit signal |
| 2026-11-11T16:30 | Stochastic reversion · 1h | sell | COIN | 9.47 | 0.21 | exit signal |
| 2026-11-11T16:30 | Bollinger reversion · 1h | sell | NVDA | 18.91 | 0.55 | exit signal |
| 2026-11-11T16:30 | RSI(14) reversion · 1h | buy | ETHU | 7.11 | — | entry signal |
| 2026-11-11T16:30 | RSI(14) reversion · 1h | sell | MSTR | 3.57 | 0.08 | rebalance down |
| 2026-11-11T16:30 | RSI(14) reversion · 1h | sell | BITX | 3.54 | 0.06 | rebalance down |
| 2026-11-11T16:30 | Volume breakout · 1h | buy | QQQ | 8.79 | — | entry signal |
| 2026-11-11T16:30 | Volume breakout · 1h | sell | SOXL | 4.64 | 0.19 | rebalance down |
| 2026-11-11T16:30 | Volume breakout · 1h | sell | AMD | 4.14 | 0.07 | rebalance down |
| 2026-11-11T16:30 | OBV trend · 1h | buy | LABU | 9.83 | — | entry signal |
| 2026-11-11T16:30 | OBV trend · 1h | sell | META | 3.63 | 0.03 | rebalance down |
| 2026-11-11T16:30 | OBV trend · 1h | sell | IWM | 3.61 | 0.03 | rebalance down |
| 2026-11-11T16:30 | VWAP momentum · 1h | buy | GOOGL | 2.18 | — | entry signal |
| 2026-11-11T16:30 | VWAP momentum · 1h | buy | ETH-USD | 3.11 | — | entry |
| 2026-11-11T16:30 | VWAP momentum · 1h | sell | TSLA | 5.29 | 0.24 | exit signal |
| 2026-11-11T16:30 | Triple EMA stack · 1h | buy | LABU | 4.72 | — | entry signal |
| 2026-11-11T16:30 | Triple EMA stack · 1h | sell | AMD | 4.72 | 0.37 | rebalance down |
| 2026-11-11T16:30 | EMA 20/50 cross · 1h | buy | LABU | 18.79 | — | entry signal |
| 2026-11-11T16:25 | Agent (rotation) | sell | TSLA | 8.11 | -0.01 | rebalance down |
| 2026-11-11T16:25 | Agent (ML meta-label) | buy | TSLA | 16.77 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 16:54:05.000141+00:00 -> 2026-11-11 17:04:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
