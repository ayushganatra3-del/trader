# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T07:25:05.000103+00:00 · 55512 ticks

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

Today: 5610 decisions in 1122 calls, $0.0784 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T07:25 | 3 / 2 / 0 | ETH-USD 14% |  |
| Breezy | 2026-11-11T07:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-11T07:25 | 3 / 2 / 0 | ETH-USD 69% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.80 | 14.80 | 0 | — | 15.13 | 5.00 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.87 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.31 | 1.31 | 0 | — | 4.26 | 1.24 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.78 | 1.12 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -4.33 | -1.77 | -9.87 | 155 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.77 | -3.23 | 0 | — | -1.28 | -0.38 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 95.03 | -4.97 | 0 | — | -4.27 | -1.11 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.06 | -3.77 | -5.99 | 27 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Insider buying | copy | 92.92 | -7.08 | 43 | 39.5 | -7.95 | -1.63 | -15.11 | 67 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.65 | -7.35 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 92.58 | -7.42 | 108 | 23.1 | -12.81 | -4.75 | -16.85 | 78 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.01 | -2.74 | -15.49 | 77 |
| 23 | Opening range 30m | breakout | 88.22 | -11.78 | 404 | 33.2 | -15.00 | -4.57 | -15.00 | 604 |
| 24 | Agent | meta | 87.46 | -12.54 | 172 | 35.5 | -13.34 | -6.73 | -14.27 | 203 |
| 25 | Hold BTC | benchmark | 86.41 | -13.59 | 1 | 0.0 | -5.73 | -0.73 | -16.64 | 1 |
| 26 | Daily: Bullish score | daily | 86.40 | -13.60 | 15 | 20.0 | -4.92 | -0.64 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.48 | -14.52 | 168 | 26.8 | -13.63 | -2.77 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.97 | -15.03 | 81 | 33.3 | -15.80 | -4.42 | -18.49 | 94 |
| 29 | Donchian 55/20 · 1h | breakout | 84.03 | -15.97 | 71 | 14.1 | -22.52 | -4.75 | -27.94 | 100 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.34 | -17.66 | 2 | 0.0 | -8.31 | -0.93 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.63 | -18.37 | 110 | 23.6 | -18.05 | -3.66 | -24.55 | 165 |
| 32 | Stochastic reversion · 1h | reversion | 81.16 | -18.84 | 286 | 47.6 | -24.02 | -3.50 | -27.06 | 392 |
| 33 | Connors RSI(2) · 1h | reversion | 80.92 | -19.08 | 207 | 40.1 | -19.42 | -6.44 | -19.98 | 125 |
| 34 | Opening range 15m | breakout | 80.79 | -19.21 | 500 | 31.4 | -20.74 | -5.58 | -20.74 | 733 |
| 35 | Max aggression: 5-day momentum | meta | 80.37 | -19.63 | 18 | 44.4 | -36.21 | -2.28 | -45.81 | 25 |
| 36 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -13.97 | -3.22 | -21.11 | 92 |
| 37 | ADX DI cross · 1h | trend | 79.35 | -20.65 | 185 | 18.9 | -26.47 | -4.60 | -30.45 | 279 |
| 38 | Heikin-Ashi · 1h | trend | 78.99 | -21.01 | 417 | 24.5 | -40.10 | -7.43 | -42.47 | 665 |
| 39 | CCI reversion · 1h | reversion | 76.91 | -23.09 | 326 | 45.1 | -26.40 | -3.98 | -30.86 | 453 |
| 40 | MFI reversion · 1h | reversion | 76.91 | -23.09 | 365 | 34.5 | -17.54 | -2.23 | -22.84 | 157 |
| 41 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.39 | -4.44 | -27.99 | 235 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.14 | -8.75 | -31.64 | 118 |
| 43 | MACD cross · 1h | trend | 74.97 | -25.03 | 360 | 21.9 | -31.65 | -5.15 | -39.47 | 478 |
| 44 | EMA 20/50 cross · 1h | trend | 74.90 | -25.10 | 102 | 10.8 | -26.29 | -4.48 | -36.26 | 116 |
| 45 | Bollinger reversion · 1h | reversion | 74.23 | -25.77 | 283 | 41.0 | -26.20 | -3.99 | -32.30 | 371 |
| 46 | MACD zero-line · 1h | trend | 73.90 | -26.10 | 159 | 16.4 | -23.01 | -4.63 | -31.08 | 208 |
| 47 | Supertrend · 1h | trend | 73.56 | -26.43 | 168 | 13.1 | -28.54 | -4.93 | -36.14 | 222 |
| 48 | RSI momentum · 1h | momentum | 73.39 | -26.61 | 159 | 12.6 | -25.28 | -4.09 | -34.73 | 209 |
| 49 | Triple EMA stack · 1h | trend | 72.23 | -27.77 | 144 | 14.6 | -28.93 | -5.10 | -36.37 | 210 |
| 50 | Williams %R · 1h | reversion | 71.67 | -28.32 | 348 | 45.7 | -34.78 | -5.46 | -35.97 | 533 |
| 51 | OBV trend · 1h | momentum | 71.62 | -28.38 | 277 | 18.4 | -28.76 | -5.22 | -36.01 | 284 |
| 52 | ROC + volume · 1h | momentum | 71.29 | -28.71 | 369 | 27.1 | -35.37 | -6.63 | -38.45 | 375 |
| 53 | Daily: Momentum burst | daily | 71.08 | -28.92 | 27 | 11.1 | -34.82 | -4.87 | -38.23 | 34 |
| 54 | Donchian 20/10 · 1h | breakout | 70.89 | -29.11 | 142 | 19.7 | -30.75 | -5.72 | -35.64 | 204 |
| 55 | Z-score reversion · 1h | reversion | 70.53 | -29.48 | 190 | 36.3 | -25.78 | -3.73 | -28.98 | 234 |
| 56 | Max aggression: 1-day momentum | meta | 68.35 | -31.65 | 27 | 25.9 | -29.50 | -1.42 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 66.72 | -33.28 | 170 | 30.6 | -31.38 | -4.83 | -33.96 | 233 |
| 58 | VWAP momentum · 1h | momentum | 65.83 | -34.17 | 843 | 21.8 | -54.23 | -11.58 | -55.10 | 1234 |
| 59 | EMA 9/21 cross · 1h | trend | 65.57 | -34.43 | 252 | 9.9 | -37.14 | -7.43 | -41.74 | 336 |
| 60 | Agent (ML meta-label) | meta | 65.50 | -34.50 | 1700 | 24.5 | -13.07 | -1.92 | -21.13 | 334 |
| 61 | Candlestick reversal · 1h | reversion | 63.76 | -36.24 | 452 | 28.1 | -38.38 | -7.13 | -40.19 | 589 |
| 62 | Three white soldiers | momentum | 60.40 | -39.60 | 512 | 14.6 | -49.19 | -22.50 | -49.19 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -46.33 | -99.04 | 5319 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.86 | -26.49 | -79.86 | 1428 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.36 | -46.10 | -93.36 | 2524 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.94 | -89.29 | 1924 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.00 | -39.92 | -91.00 | 2337 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.20 | -31.55 | -90.33 | 2216 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.80 | -54.39 | -97.80 | 3469 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -57.17 | -96.26 | 3451 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.49 | -32.23 | -93.64 | 2362 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.67 | -34.59 | -82.75 | 1672 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -53.07 | -99.54 | 5974 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.21 | -43.40 | -92.21 | 2614 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.54 | -36.83 | -95.54 | 3439 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.28 | -99.80 | 6165 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.10 | -43.97 | -92.10 | 2279 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.56 | -24.80 | -75.56 | 1608 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -59.97 | -97.71 | 3533 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -59.65 | -98.83 | 4892 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.65 | -26.99 | -69.09 | 1234 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -53.55 | -94.66 | 2784 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -37.28 | -84.92 | 1781 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -70.38 | -99.64 | 6342 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.52 | -31.71 | -89.62 | 2290 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.99 | -19.71 | -78.30 | 1748 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.52 | -35.60 | -90.64 | 2194 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.77 | -50.58 | -96.78 | 3852 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.25 | -55.48 | -89.27 | 2154 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.47 | -27.53 | -66.35 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.39 | -22.72 | -71.64 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.27 | -19.07 | -79.54 | 1688 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.19 | -47.05 | -97.21 | 4293 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -100.00 | -99.93 | 8326 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-11T03:00 | VWAP momentum · 1h | buy | ETH-USD | 4.70 | — | entry signal |
| 2026-11-11T02:45 | MFI reversion · 1h | sell | XRP-USD | 4.40 | -0.03 | rebalance down |
| 2026-11-11T02:45 | MFI reversion · 1h | sell | DOGE-USD | 4.43 | 0.02 | rebalance down |
| 2026-11-11T02:15 | MFI reversion · 1h | buy | XRP-USD | 6.80 | — | rebalance up |
| 2026-11-11T02:15 | MFI reversion · 1h | buy | DOGE-USD | 6.87 | — | rebalance up |
| 2026-11-11T02:01 | VWAP momentum · 1h | sell | DOGE-USD | 5.02 | -0.03 | exit signal |
| 2026-11-11T01:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.05 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 07:25:05.000103+00:00 -> 2026-11-11 07:35:05.000103+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
