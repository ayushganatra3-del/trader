# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T10:55:05.000139+00:00 · 55690 ticks

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

Today: 8280 decisions in 1656 calls, $0.1157 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T10:55 | 2 / 2 / 1 | cash |  |
| Breezy | 2026-11-11T10:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-11T10:55 | 3 / 2 / 0 | ETH-USD 62% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.96 | 14.96 | 0 | — | 15.13 | 5.00 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.87 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.45 | 1.45 | 0 | — | 4.26 | 1.24 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.78 | 1.12 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -4.33 | -1.77 | -9.87 | 155 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.91 | -3.09 | 0 | — | -1.28 | -0.38 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 95.16 | -4.84 | 0 | — | -4.27 | -1.11 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.04 | -3.75 | -5.99 | 27 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Insider buying | copy | 93.05 | -6.95 | 43 | 39.5 | -7.95 | -1.63 | -15.11 | 67 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.78 | -7.22 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 92.68 | -7.32 | 108 | 23.1 | -12.81 | -4.75 | -16.85 | 78 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.01 | -2.74 | -15.49 | 77 |
| 23 | Opening range 30m | breakout | 88.22 | -11.78 | 404 | 33.2 | -15.00 | -4.57 | -15.00 | 604 |
| 24 | Agent | meta | 87.46 | -12.54 | 172 | 35.5 | -13.34 | -6.73 | -14.27 | 203 |
| 25 | Hold BTC | benchmark | 86.67 | -13.33 | 1 | 0.0 | -5.18 | -0.65 | -16.64 | 1 |
| 26 | Daily: Bullish score | daily | 86.46 | -13.54 | 15 | 20.0 | -4.92 | -0.64 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.59 | -14.41 | 168 | 26.8 | -13.63 | -2.77 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.97 | -15.03 | 81 | 33.3 | -15.80 | -4.42 | -18.49 | 94 |
| 29 | Donchian 55/20 · 1h | breakout | 84.09 | -15.91 | 71 | 14.1 | -22.52 | -4.75 | -27.94 | 100 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.45 | -17.55 | 2 | 0.0 | -8.31 | -0.93 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.66 | -18.34 | 110 | 23.6 | -17.14 | -3.48 | -24.55 | 165 |
| 32 | Stochastic reversion · 1h | reversion | 81.40 | -18.60 | 286 | 47.6 | -24.49 | -3.59 | -27.06 | 390 |
| 33 | Connors RSI(2) · 1h | reversion | 80.94 | -19.06 | 207 | 40.1 | -19.42 | -6.44 | -19.98 | 125 |
| 34 | Opening range 15m | breakout | 80.79 | -19.21 | 500 | 31.4 | -20.74 | -5.58 | -20.74 | 733 |
| 35 | Max aggression: 5-day momentum | meta | 80.48 | -19.52 | 18 | 44.4 | -36.21 | -2.28 | -45.81 | 25 |
| 36 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -13.97 | -3.22 | -21.11 | 92 |
| 37 | ADX DI cross · 1h | trend | 79.46 | -20.54 | 185 | 18.9 | -26.47 | -4.60 | -30.45 | 279 |
| 38 | Heikin-Ashi · 1h | trend | 79.02 | -20.98 | 417 | 24.5 | -39.89 | -7.37 | -42.28 | 664 |
| 39 | CCI reversion · 1h | reversion | 77.06 | -22.94 | 326 | 45.1 | -26.26 | -3.95 | -30.86 | 453 |
| 40 | MFI reversion · 1h | reversion | 77.00 | -23.00 | 366 | 34.4 | -16.65 | -2.09 | -22.84 | 158 |
| 41 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.39 | -4.44 | -27.99 | 235 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.14 | -8.75 | -31.64 | 118 |
| 43 | MACD cross · 1h | trend | 75.07 | -24.93 | 360 | 21.9 | -31.69 | -5.15 | -39.47 | 479 |
| 44 | EMA 20/50 cross · 1h | trend | 74.97 | -25.02 | 102 | 10.8 | -25.54 | -4.32 | -36.26 | 114 |
| 45 | Bollinger reversion · 1h | reversion | 74.28 | -25.72 | 283 | 41.0 | -26.20 | -3.99 | -32.30 | 371 |
| 46 | MACD zero-line · 1h | trend | 73.98 | -26.02 | 159 | 16.4 | -23.01 | -4.63 | -31.08 | 208 |
| 47 | Supertrend · 1h | trend | 73.67 | -26.33 | 168 | 13.1 | -28.54 | -4.93 | -36.14 | 222 |
| 48 | RSI momentum · 1h | momentum | 73.50 | -26.50 | 159 | 12.6 | -25.28 | -4.09 | -34.73 | 209 |
| 49 | Triple EMA stack · 1h | trend | 72.31 | -27.69 | 144 | 14.6 | -28.91 | -5.10 | -36.37 | 210 |
| 50 | Williams %R · 1h | reversion | 71.88 | -28.12 | 348 | 45.7 | -34.62 | -5.42 | -35.97 | 533 |
| 51 | OBV trend · 1h | momentum | 71.72 | -28.28 | 277 | 18.4 | -29.01 | -5.27 | -36.01 | 285 |
| 52 | ROC + volume · 1h | momentum | 71.36 | -28.64 | 369 | 27.1 | -35.37 | -6.63 | -38.45 | 375 |
| 53 | Daily: Momentum burst | daily | 71.15 | -28.85 | 27 | 11.1 | -34.82 | -4.87 | -38.23 | 34 |
| 54 | Donchian 20/10 · 1h | breakout | 70.93 | -29.07 | 142 | 19.7 | -30.75 | -5.72 | -35.64 | 204 |
| 55 | Z-score reversion · 1h | reversion | 70.71 | -29.29 | 190 | 36.3 | -25.64 | -3.70 | -28.98 | 234 |
| 56 | Max aggression: 1-day momentum | meta | 68.44 | -31.56 | 27 | 25.9 | -29.50 | -1.42 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 67.01 | -32.99 | 170 | 30.6 | -32.02 | -4.98 | -33.96 | 228 |
| 58 | VWAP momentum · 1h | momentum | 65.90 | -34.10 | 843 | 21.8 | -54.05 | -11.50 | -55.23 | 1237 |
| 59 | EMA 9/21 cross · 1h | trend | 65.66 | -34.34 | 252 | 9.9 | -37.75 | -7.57 | -41.74 | 335 |
| 60 | Agent (ML meta-label) | meta | 65.59 | -34.41 | 1700 | 24.5 | -10.24 | -1.46 | -19.59 | 333 |
| 61 | Candlestick reversal · 1h | reversion | 63.91 | -36.09 | 452 | 28.1 | -38.08 | -7.02 | -40.19 | 588 |
| 62 | Three white soldiers | momentum | 60.40 | -39.60 | 512 | 14.6 | -49.19 | -22.50 | -49.19 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -46.26 | -99.03 | 5319 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.98 | -26.51 | -80.05 | 1434 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -46.38 | -93.47 | 2533 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.34 | -31.92 | -89.40 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.08 | -40.03 | -91.09 | 2343 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.20 | -31.55 | -90.33 | 2216 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.80 | -54.29 | -97.80 | 3474 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -57.65 | -96.31 | 3459 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.41 | -31.67 | -93.62 | 2358 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.86 | -34.55 | -83.00 | 1680 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -53.43 | -99.54 | 5972 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.19 | -43.20 | -92.20 | 2616 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.56 | -37.06 | -95.56 | 3443 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.23 | -99.80 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.16 | -44.29 | -92.17 | 2286 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.77 | -25.01 | -75.80 | 1615 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -60.14 | -97.73 | 3535 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.82 | -59.86 | -98.82 | 4890 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.67 | -27.03 | -69.09 | 1237 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -53.51 | -94.69 | 2788 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.84 | -37.50 | -85.04 | 1786 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -71.61 | -99.64 | 6338 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.37 | -31.31 | -89.47 | 2284 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.04 | -19.72 | -78.36 | 1748 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.45 | -35.40 | -90.58 | 2190 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.72 | -50.44 | -96.72 | 3843 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -56.48 | -89.30 | 2156 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.56 | -27.69 | -66.45 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.45 | -22.79 | -71.73 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.82 | -18.82 | -79.12 | 1681 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.18 | -47.33 | -97.19 | 4290 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -104.11 | -99.93 | 8337 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-11T05:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 19.74 | -0.01 | exit signal |
| 2026-11-11T04:50 | MFI reversion · 1h | sell | XRP-USD | 4.35 | -0.04 | rebalance down |
| 2026-11-11T04:50 | MFI reversion · 1h | sell | DOGE-USD | 4.37 | -0.01 | rebalance down |
| 2026-11-11T04:19 | MFI reversion · 1h | buy | XRP-USD | 4.41 | — | rebalance up |
| 2026-11-11T04:19 | MFI reversion · 1h | buy | DOGE-USD | 4.42 | — | rebalance up |
| 2026-11-11T03:00 | VWAP reversion · 1h | sell | ETH-USD | 24.04 | 0.14 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 10:55:05.000139+00:00 -> 2026-11-11 11:05:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
