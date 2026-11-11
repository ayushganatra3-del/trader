# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T12:25:05.000151+00:00 · 55763 ticks

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

Today: 9375 decisions in 1875 calls, $0.1310 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T12:25 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-11T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-11T12:25 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.01 | 15.01 | 0 | — | 15.13 | 5.00 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.87 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.50 | 1.50 | 0 | — | 4.26 | 1.24 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.80 | 1.13 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -4.33 | -1.77 | -9.87 | 155 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.95 | -3.05 | 0 | — | -1.28 | -0.38 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 95.21 | -4.79 | 0 | — | -4.27 | -1.11 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.49 | -3.29 | -5.99 | 26 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Insider buying | copy | 93.04 | -6.96 | 43 | 39.5 | -8.00 | -1.64 | -15.11 | 67 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.83 | -7.17 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 92.72 | -7.28 | 108 | 23.1 | -12.81 | -4.75 | -16.85 | 78 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -11.76 | -3.33 | -15.49 | 80 |
| 23 | Opening range 30m | breakout | 88.22 | -11.78 | 404 | 33.2 | -15.00 | -4.57 | -15.00 | 604 |
| 24 | Agent | meta | 87.46 | -12.54 | 172 | 35.5 | -13.28 | -6.71 | -14.21 | 201 |
| 25 | Hold BTC | benchmark | 86.57 | -13.43 | 1 | 0.0 | -4.22 | -0.50 | -16.64 | 1 |
| 26 | Daily: Bullish score | daily | 86.48 | -13.52 | 15 | 20.0 | -4.92 | -0.64 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.64 | -14.36 | 168 | 26.8 | -13.99 | -2.84 | -21.70 | 226 |
| 28 | Agent (aggressive) | meta | 84.97 | -15.03 | 81 | 33.3 | -15.80 | -4.42 | -18.49 | 94 |
| 29 | Donchian 55/20 · 1h | breakout | 84.11 | -15.89 | 71 | 14.1 | -22.52 | -4.75 | -27.94 | 100 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.49 | -17.51 | 2 | 0.0 | -8.31 | -0.93 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.67 | -18.33 | 110 | 23.6 | -19.07 | -3.82 | -24.55 | 165 |
| 32 | Stochastic reversion · 1h | reversion | 81.36 | -18.64 | 287 | 47.7 | -24.60 | -3.61 | -27.06 | 390 |
| 33 | Connors RSI(2) · 1h | reversion | 80.95 | -19.05 | 207 | 40.1 | -19.42 | -6.44 | -19.98 | 125 |
| 34 | Opening range 15m | breakout | 80.79 | -19.21 | 500 | 31.4 | -20.74 | -5.58 | -20.74 | 733 |
| 35 | Max aggression: 5-day momentum | meta | 80.51 | -19.49 | 18 | 44.4 | -36.21 | -2.28 | -45.81 | 25 |
| 36 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -13.97 | -3.22 | -21.11 | 92 |
| 37 | ADX DI cross · 1h | trend | 79.50 | -20.50 | 185 | 18.9 | -25.23 | -4.34 | -30.45 | 273 |
| 38 | Heikin-Ashi · 1h | trend | 78.91 | -21.09 | 417 | 24.5 | -39.98 | -7.39 | -42.28 | 665 |
| 39 | CCI reversion · 1h | reversion | 76.93 | -23.07 | 327 | 45.0 | -26.49 | -4.00 | -30.86 | 453 |
| 40 | MFI reversion · 1h | reversion | 76.89 | -23.11 | 366 | 34.4 | -16.82 | -2.15 | -22.43 | 157 |
| 41 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.50 | -4.46 | -27.99 | 235 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.15 | -8.75 | -31.64 | 118 |
| 43 | MACD cross · 1h | trend | 75.09 | -24.91 | 360 | 21.9 | -31.72 | -5.16 | -39.47 | 478 |
| 44 | EMA 20/50 cross · 1h | trend | 75.00 | -25.00 | 102 | 10.8 | -25.82 | -4.40 | -36.26 | 114 |
| 45 | Bollinger reversion · 1h | reversion | 74.29 | -25.71 | 283 | 41.0 | -26.20 | -3.99 | -32.30 | 371 |
| 46 | MACD zero-line · 1h | trend | 74.01 | -25.99 | 159 | 16.4 | -23.07 | -4.64 | -31.08 | 208 |
| 47 | Supertrend · 1h | trend | 73.70 | -26.30 | 168 | 13.1 | -28.54 | -4.93 | -36.14 | 222 |
| 48 | RSI momentum · 1h | momentum | 73.53 | -26.47 | 159 | 12.6 | -25.22 | -4.08 | -34.73 | 209 |
| 49 | Triple EMA stack · 1h | trend | 72.33 | -27.67 | 144 | 14.6 | -28.81 | -5.08 | -36.37 | 211 |
| 50 | Williams %R · 1h | reversion | 71.80 | -28.20 | 349 | 45.8 | -35.28 | -5.53 | -36.18 | 530 |
| 51 | OBV trend · 1h | momentum | 71.75 | -28.25 | 277 | 18.4 | -29.26 | -5.34 | -35.84 | 287 |
| 52 | ROC + volume · 1h | momentum | 71.38 | -28.62 | 369 | 27.1 | -35.42 | -6.63 | -38.52 | 374 |
| 53 | Daily: Momentum burst | daily | 71.18 | -28.82 | 27 | 11.1 | -34.82 | -4.87 | -38.23 | 34 |
| 54 | Donchian 20/10 · 1h | breakout | 70.95 | -29.05 | 142 | 19.7 | -30.78 | -5.73 | -35.64 | 204 |
| 55 | Z-score reversion · 1h | reversion | 70.58 | -29.42 | 190 | 36.3 | -25.79 | -3.73 | -28.98 | 234 |
| 56 | Max aggression: 1-day momentum | meta | 68.48 | -31.52 | 27 | 25.9 | -29.50 | -1.42 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 66.84 | -33.16 | 170 | 30.6 | -32.20 | -5.02 | -33.96 | 228 |
| 58 | VWAP momentum · 1h | momentum | 65.93 | -34.07 | 843 | 21.8 | -54.09 | -11.52 | -55.21 | 1238 |
| 59 | EMA 9/21 cross · 1h | trend | 65.69 | -34.31 | 252 | 9.9 | -37.32 | -7.47 | -41.74 | 334 |
| 60 | Agent (ML meta-label) | meta | 65.62 | -34.38 | 1700 | 24.5 | -12.23 | -1.93 | -20.32 | 334 |
| 61 | Candlestick reversal · 1h | reversion | 63.81 | -36.19 | 452 | 28.1 | -39.61 | -7.47 | -40.51 | 583 |
| 62 | Three white soldiers | momentum | 60.40 | -39.60 | 512 | 14.6 | -49.19 | -22.49 | -49.19 | 652 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -45.98 | -99.03 | 5312 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.13 | -26.54 | -80.16 | 1435 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.49 | -46.57 | -93.50 | 2534 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.40 | -31.97 | -89.41 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -39.99 | -91.13 | 2343 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.22 | -31.67 | -90.33 | 2218 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -54.56 | -97.82 | 3475 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -58.08 | -96.32 | 3460 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -32.44 | -93.60 | 2356 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.08 | -34.94 | -83.10 | 1683 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -52.77 | -99.54 | 5962 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -43.34 | -92.22 | 2617 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.59 | -37.24 | -95.59 | 3447 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.87 | -99.80 | 6163 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.15 | -44.07 | -92.15 | 2282 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.88 | -24.95 | -75.88 | 1617 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -60.05 | -97.73 | 3535 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -60.38 | -98.83 | 4891 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.79 | -27.29 | -69.09 | 1237 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -53.83 | -94.70 | 2788 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.93 | -37.61 | -85.10 | 1786 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -70.45 | -99.63 | 6332 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.36 | -31.30 | -89.47 | 2284 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.42 | -19.44 | -77.75 | 1737 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.44 | -35.45 | -90.53 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.68 | -50.20 | -96.68 | 3838 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -55.91 | -89.22 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.60 | -27.76 | -66.48 | 818 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.53 | -22.87 | -71.79 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.54 | -18.57 | -78.85 | 1675 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.16 | -47.10 | -97.16 | 4286 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -104.51 | -99.93 | 8337 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-11T06:00 | Bollinger reversion · 1h | sell | XRP-USD | 8.11 | -0.00 | exit signal |
| 2026-11-11T06:00 | Bollinger reversion · 1h | sell | SOL-USD | 8.23 | 0.03 | exit signal |
| 2026-11-11T06:00 | Bollinger reversion · 1h | sell | DOGE-USD | 8.22 | 0.05 | exit signal |
| 2026-11-11T06:00 | Bollinger reversion · 1h | sell | BTC-USD | 8.24 | 0.00 | exit signal |
| 2026-11-11T06:00 | Candlestick reversal · 1h | buy | XRP-USD | 5.00 | — | entry signal |
| 2026-11-11T05:50 | MFI reversion · 1h | buy | XRP-USD | 4.31 | — | rebalance up |
| 2026-11-11T05:50 | MFI reversion · 1h | buy | DOGE-USD | 4.41 | — | rebalance up |
| 2026-11-11T05:00 | Bollinger reversion · 1h | sell | ETH-USD | 8.27 | 0.08 | exit signal |
| 2026-11-11T05:00 | Candlestick reversal · 1h | buy | BTC-USD | 8.00 | — | entry |
| 2026-11-11T05:00 | Candlestick reversal · 1h | sell | XRP-USD | 4.99 | -0.04 | exit signal |
| 2026-11-11T05:00 | Candlestick reversal · 1h | sell | DOGE-USD | 8.00 | 0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 12:25:05.000151+00:00 -> 2026-11-11 12:35:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
