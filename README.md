# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T02:55:05.000116+00:00 · 55273 ticks

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

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.46 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 2025 decisions in 405 calls, $0.0283 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T02:55 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-11T02:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-11T02:55 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.71 | 14.71 | 0 | — | 15.13 | 5.00 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.87 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.23 | 1.23 | 0 | — | 4.26 | 1.24 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.80 | 1.13 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -4.33 | -1.77 | -9.87 | 155 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.70 | -3.30 | 0 | — | -1.28 | -0.38 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 96.11 | -3.89 | 138 | 46.4 | -12.74 | -3.27 | -13.67 | 154 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.95 | -5.05 | 0 | — | -4.27 | -1.11 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.04 | -3.75 | -5.99 | 27 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Insider buying | copy | 92.80 | -7.20 | 43 | 39.5 | -8.00 | -1.64 | -15.11 | 67 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.58 | -7.42 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 92.53 | -7.47 | 108 | 23.1 | -12.81 | -4.75 | -16.85 | 78 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.41 | -2.56 | -15.49 | 77 |
| 23 | Opening range 30m | breakout | 88.22 | -11.78 | 404 | 33.2 | -15.00 | -4.57 | -15.00 | 604 |
| 24 | Agent | meta | 87.46 | -12.54 | 172 | 35.5 | -13.28 | -6.71 | -14.21 | 201 |
| 25 | Daily: Bullish score | daily | 86.36 | -13.64 | 15 | 20.0 | -4.92 | -0.64 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 85.93 | -14.07 | 1 | 0.0 | -6.36 | -0.84 | -16.64 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.41 | -14.59 | 168 | 26.8 | -13.63 | -2.77 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.97 | -15.03 | 81 | 33.3 | -15.80 | -4.42 | -18.49 | 94 |
| 29 | Donchian 55/20 · 1h | breakout | 84.00 | -16.00 | 71 | 14.1 | -22.52 | -4.75 | -27.94 | 100 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.27 | -17.73 | 2 | 0.0 | -8.31 | -0.93 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.61 | -18.39 | 110 | 23.6 | -17.14 | -3.48 | -24.55 | 165 |
| 32 | Stochastic reversion · 1h | reversion | 81.18 | -18.82 | 284 | 47.5 | -24.38 | -3.57 | -27.06 | 393 |
| 33 | Connors RSI(2) · 1h | reversion | 80.90 | -19.10 | 207 | 40.1 | -19.42 | -6.44 | -19.98 | 125 |
| 34 | Opening range 15m | breakout | 80.79 | -19.21 | 500 | 31.4 | -20.74 | -5.58 | -20.74 | 733 |
| 35 | Max aggression: 5-day momentum | meta | 80.30 | -19.70 | 18 | 44.4 | -36.21 | -2.28 | -45.81 | 25 |
| 36 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -13.97 | -3.22 | -21.11 | 92 |
| 37 | ADX DI cross · 1h | trend | 79.29 | -20.71 | 185 | 18.9 | -26.13 | -4.53 | -30.45 | 280 |
| 38 | Heikin-Ashi · 1h | trend | 79.08 | -20.92 | 416 | 24.5 | -40.14 | -7.44 | -42.60 | 666 |
| 39 | MFI reversion · 1h | reversion | 77.08 | -22.92 | 365 | 34.5 | -17.45 | -2.25 | -22.43 | 159 |
| 40 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.39 | -4.44 | -27.99 | 235 |
| 41 | CCI reversion · 1h | reversion | 76.79 | -23.21 | 326 | 45.1 | -26.03 | -3.90 | -30.85 | 457 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.15 | -8.75 | -31.64 | 118 |
| 43 | MACD cross · 1h | trend | 74.88 | -25.12 | 360 | 21.9 | -31.95 | -5.22 | -39.47 | 479 |
| 44 | EMA 20/50 cross · 1h | trend | 74.85 | -25.15 | 102 | 10.8 | -26.44 | -4.50 | -36.26 | 118 |
| 45 | Bollinger reversion · 1h | reversion | 74.22 | -25.78 | 278 | 40.3 | -26.15 | -3.98 | -32.30 | 371 |
| 46 | MACD zero-line · 1h | trend | 73.85 | -26.15 | 159 | 16.4 | -25.72 | -5.15 | -31.08 | 213 |
| 47 | Supertrend · 1h | trend | 73.51 | -26.49 | 168 | 13.1 | -29.56 | -5.09 | -36.14 | 227 |
| 48 | RSI momentum · 1h | momentum | 73.34 | -26.66 | 159 | 12.6 | -25.29 | -4.09 | -34.73 | 209 |
| 49 | Triple EMA stack · 1h | trend | 72.19 | -27.81 | 144 | 14.6 | -28.51 | -5.01 | -36.37 | 208 |
| 50 | Williams %R · 1h | reversion | 71.65 | -28.35 | 346 | 45.7 | -35.35 | -5.53 | -36.23 | 535 |
| 51 | OBV trend · 1h | momentum | 71.56 | -28.44 | 277 | 18.4 | -28.52 | -5.17 | -35.84 | 283 |
| 52 | ROC + volume · 1h | momentum | 71.24 | -28.76 | 369 | 27.1 | -35.46 | -6.64 | -38.52 | 376 |
| 53 | Daily: Momentum burst | daily | 71.03 | -28.96 | 27 | 11.1 | -34.82 | -4.87 | -38.23 | 34 |
| 54 | Donchian 20/10 · 1h | breakout | 70.85 | -29.15 | 142 | 19.7 | -30.75 | -5.73 | -35.64 | 204 |
| 55 | Z-score reversion · 1h | reversion | 70.50 | -29.50 | 190 | 36.3 | -25.79 | -3.73 | -28.98 | 234 |
| 56 | Max aggression: 1-day momentum | meta | 68.30 | -31.70 | 27 | 25.9 | -29.50 | -1.42 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 66.72 | -33.28 | 170 | 30.6 | -32.10 | -4.96 | -33.96 | 235 |
| 58 | VWAP momentum · 1h | momentum | 65.81 | -34.19 | 842 | 21.9 | -53.86 | -11.43 | -55.01 | 1227 |
| 59 | EMA 9/21 cross · 1h | trend | 65.52 | -34.48 | 252 | 9.9 | -37.32 | -7.47 | -41.74 | 336 |
| 60 | Agent (ML meta-label) | meta | 65.45 | -34.55 | 1700 | 24.5 | -9.81 | -1.33 | -19.29 | 332 |
| 61 | Candlestick reversal · 1h | reversion | 63.99 | -36.01 | 447 | 28.0 | -38.52 | -7.14 | -40.51 | 589 |
| 62 | Three white soldiers | momentum | 60.40 | -39.60 | 512 | 14.6 | -49.19 | -22.49 | -49.19 | 652 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -45.02 | -98.97 | 5281 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.47 | -25.97 | -79.52 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.25 | -45.02 | -93.26 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.25 | -31.79 | -89.27 | 1923 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.85 | -39.36 | -90.85 | 2332 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.22 | -31.65 | -90.33 | 2217 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.79 | -53.38 | -97.79 | 3471 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.17 | -54.82 | -96.18 | 3440 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -33.50 | -93.80 | 2374 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.29 | -33.59 | -82.41 | 1663 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -52.60 | -99.55 | 5979 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.16 | -43.05 | -92.16 | 2613 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -36.31 | -95.56 | 3431 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -71.73 | -99.80 | 6168 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.10 | -43.58 | -92.10 | 2279 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.36 | -24.35 | -75.37 | 1607 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -59.02 | -97.70 | 3529 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -58.78 | -98.85 | 4895 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.86 | -27.29 | -69.17 | 1237 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -52.93 | -94.60 | 2782 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.62 | -36.85 | -84.80 | 1777 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -68.23 | -99.64 | 6346 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.65 | -31.70 | -89.79 | 2293 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.03 | -19.74 | -78.33 | 1747 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.58 | -35.50 | -90.73 | 2191 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -49.52 | -96.78 | 3854 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.32 | -55.52 | -89.35 | 2156 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.47 | -27.53 | -66.35 | 816 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.27 | -22.59 | -71.53 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.81 | -19.07 | -80.03 | 1696 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.20 | -46.75 | -97.22 | 4291 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.58 | -99.93 | 8329 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T02:45 | MFI reversion · 1h | sell | XRP-USD | 4.40 | -0.03 | rebalance down |
| 2026-11-11T02:45 | MFI reversion · 1h | sell | DOGE-USD | 4.43 | 0.02 | rebalance down |
| 2026-11-11T02:15 | MFI reversion · 1h | buy | XRP-USD | 6.80 | — | rebalance up |
| 2026-11-11T02:15 | MFI reversion · 1h | buy | DOGE-USD | 6.87 | — | rebalance up |
| 2026-11-11T02:01 | VWAP momentum · 1h | sell | DOGE-USD | 5.02 | -0.03 | exit signal |
| 2026-11-11T01:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.05 | — | entry signal |
| 2026-11-11T00:46 | Three white soldiers | sell | SOL-USD | 15.02 | -0.10 | exit signal |
| 2026-11-11T00:44 | MFI reversion · 1h | sell | XRP-USD | 4.20 | -0.07 | rebalance down |
| 2026-11-11T00:44 | MFI reversion · 1h | sell | DOGE-USD | 4.40 | 0.03 | rebalance down |
| 2026-11-11T00:00 | Z-score reversion · 1h | buy | XRP-USD | 7.06 | — | entry |
| 2026-11-11T00:00 | Z-score reversion · 1h | buy | SOL-USD | 7.06 | — | entry |
| 2026-11-11T00:00 | Z-score reversion · 1h | buy | ETH-USD | 7.06 | — | entry |
| 2026-11-11T00:00 | Z-score reversion · 1h | buy | DOGE-USD | 7.06 | — | entry |
| 2026-11-11T00:00 | Z-score reversion · 1h | buy | BTC-USD | 7.06 | — | entry |
| 2026-11-11T00:00 | Candlestick reversal · 1h | buy | XRP-USD | 5.03 | — | entry signal |
| 2026-11-11T00:00 | MACD cross · 1h | buy | ETH-USD | 4.41 | — | entry signal |
| 2026-11-11T00:00 | MACD cross · 1h | buy | BTC-USD | 4.41 | — | entry signal |
| 2026-11-10T23:45 | Three white soldiers | buy | SOL-USD | 15.12 | — | entry signal |
| 2026-11-10T23:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.03 | — | rebalance up |
| 2026-11-10T23:00 | Candlestick reversal · 1h | sell | BTC-USD | 9.07 | -0.02 | exit signal |
| 2026-11-10T23:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.75 | — | entry signal |
| 2026-11-10T23:00 | Three white soldiers | sell | DOGE-USD | 15.03 | -0.13 | target is flat |
| 2026-11-10T22:55 | Three white soldiers | buy | DOGE-USD | 15.16 | — | entry signal |
| 2026-11-10T22:00 | CCI reversion · 1h | buy | BTC-USD | 4.33 | — | entry |
| 2026-11-10T22:00 | CCI reversion · 1h | sell | ETH-USD | 4.33 | -0.00 | rebalance down |
| 2026-11-10T21:00 | MFI reversion · 1h | buy | XRP-USD | 5.16 | — | rebalance up |
| 2026-11-10T21:00 | MFI reversion · 1h | buy | DOGE-USD | 5.13 | — | rebalance up |
| 2026-11-10T20:55 | Agent (aggressive) | sell | SQQQ | 42.23 | -0.26 | selected signal exited |
| 2026-11-10T20:55 | Agent (aggressive) | sell | COIN | 42.74 | 0.25 | selected signal exited |
| 2026-11-10T20:55 | Agent | sell | SQQQ | 17.39 | -0.11 | selected signal exited |
| 2026-11-10T20:55 | Agent | sell | COIN | 17.60 | 0.10 | selected signal exited |
| 2026-11-10T20:55 | MFI reversion · 1h | sell | UPRO | 7.69 | 0.03 | target is flat |
| 2026-11-10T20:55 | MFI reversion · 1h | sell | META | 7.68 | -0.03 | target is flat |
| 2026-11-10T20:51 | VWAP momentum · 1h | sell | TECL | 5.05 | -0.01 | target is flat |
| 2026-11-10T20:35 | Agent (ML meta-label) | buy | TSLA | 6.50 | — | following Ichimoku |
| 2026-11-10T20:35 | Agent (ML meta-label) | buy | META | 10.92 | — | entry |
| 2026-11-10T20:35 | Agent (ML meta-label) | sell | SPY | 5.46 | -0.00 | rebalance down |
| 2026-11-10T20:35 | Agent (ML meta-label) | sell | AMZN | 5.48 | -0.00 | rebalance down |
| 2026-11-10T20:30 | Agent (ML meta-label) | buy | AMZN | 3.29 | — | rebalance up |
| 2026-11-10T20:30 | Agent (ML meta-label) | sell | TSLA | 9.78 | -0.01 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 02:55:05.000116+00:00 -> 2026-11-11 03:05:05.000116+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
