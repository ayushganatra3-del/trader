# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T02:35:05.000123+00:00 · 54084 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.80 (-13.20%)

Closed trades 163, win rate 35.0%, fees £4.99, max drawdown -13.60%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 29.11 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 2010 decisions in 402 calls, $0.0281 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T02:35 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-10T02:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-10T02:35 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.60 | +6.02% | 3 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 20.73 | 3.75 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.31 | 12.31 | 0 | — | 13.79 | 4.66 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.93 | 11.93 | 31 | 29.0 | 20.12 | 3.01 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.55 | 1.55 | 126 | 36.5 | 10.08 | 3.80 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 101.09 | 1.09 | 0 | — | 4.81 | 1.38 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.88 | 0.88 | 7 | 42.9 | -0.93 | 0.19 | -18.73 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.65 | 1.09 | -9.06 | 239 |
| 11 | Agent (rotation) | meta | 98.09 | -1.91 | 177 | 28.2 | -2.94 | -1.09 | -10.59 | 169 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.69 | -3.20 | -12.84 | 150 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.39 | -3.61 | 0 | — | -1.49 | -0.45 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.79 | -5.21 | 0 | — | -3.54 | -0.88 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.71 | -7.29 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 19 | Trend pullback · 1h | trend | 92.52 | -7.49 | 108 | 23.1 | -13.74 | -5.12 | -17.96 | 79 |
| 20 | Copy: Insider buying | copy | 91.98 | -8.02 | 42 | 38.1 | -9.58 | -2.00 | -16.06 | 63 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 90.34 | -9.66 | 391 | 34.3 | -13.39 | -4.24 | -15.24 | 595 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.56 | -3.42 | -14.68 | 80 |
| 24 | Agent | meta | 86.80 | -13.20 | 163 | 35.0 | -13.70 | -7.04 | -14.27 | 204 |
| 25 | Hold BTC | benchmark | 86.76 | -13.24 | 1 | 0.0 | -5.17 | -0.65 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.08 | -13.92 | 15 | 20.0 | -10.31 | -1.57 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.50 | -14.51 | 167 | 26.9 | -11.32 | -2.03 | -21.29 | 227 |
| 28 | Agent (aggressive) | meta | 83.88 | -16.12 | 76 | 31.6 | -16.53 | -4.71 | -18.49 | 94 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 83.68 | -16.32 | 2 | 0.0 | -7.65 | -0.84 | -24.16 | 1 |
| 30 | Opening range 15m | breakout | 83.50 | -16.50 | 481 | 32.4 | -18.38 | -5.20 | -19.91 | 728 |
| 31 | Donchian 55/20 · 1h | breakout | 83.35 | -16.65 | 71 | 14.1 | -18.18 | -3.97 | -22.45 | 104 |
| 32 | Stochastic reversion · 1h | reversion | 83.13 | -16.87 | 279 | 48.4 | -23.91 | -3.52 | -28.00 | 387 |
| 33 | Keltner breakout · 1h | breakout | 81.90 | -18.10 | 107 | 23.4 | -22.13 | -4.45 | -25.12 | 173 |
| 34 | Volume breakout · 1h | breakout | 81.29 | -18.71 | 145 | 27.6 | -14.82 | -3.34 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.57 | -19.43 | 205 | 40.0 | -19.67 | -6.55 | -19.99 | 124 |
| 36 | Heikin-Ashi · 1h | trend | 79.74 | -20.26 | 401 | 22.7 | -39.78 | -7.37 | -43.08 | 675 |
| 37 | ADX DI cross · 1h | trend | 79.29 | -20.71 | 179 | 18.4 | -22.47 | -3.85 | -28.34 | 275 |
| 38 | Max aggression: 5-day momentum | meta | 79.24 | -20.76 | 18 | 44.4 | -39.47 | -2.63 | -45.81 | 25 |
| 39 | MFI reversion · 1h | reversion | 79.09 | -20.91 | 352 | 34.4 | -16.52 | -2.08 | -21.28 | 168 |
| 40 | CCI reversion · 1h | reversion | 78.88 | -21.12 | 320 | 45.9 | -23.61 | -3.56 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.05 | -22.95 | 96 | 15.6 | -29.76 | -8.45 | -29.87 | 120 |
| 42 | Bollinger breakout · 1h | breakout | 76.78 | -23.22 | 170 | 22.9 | -22.64 | -4.72 | -27.92 | 240 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -25.24 | -3.80 | -32.07 | 371 |
| 44 | MACD cross · 1h | trend | 75.10 | -24.89 | 349 | 22.6 | -32.48 | -5.29 | -39.46 | 483 |
| 45 | Z-score reversion · 1h | reversion | 75.06 | -24.94 | 179 | 37.4 | -21.40 | -3.08 | -27.66 | 226 |
| 46 | Williams %R · 1h | reversion | 74.86 | -25.14 | 337 | 46.9 | -35.28 | -5.71 | -38.39 | 538 |
| 47 | MACD zero-line · 1h | trend | 74.36 | -25.64 | 157 | 16.6 | -24.85 | -5.07 | -29.19 | 214 |
| 48 | EMA 20/50 cross · 1h | trend | 74.09 | -25.91 | 102 | 10.8 | -24.55 | -4.40 | -32.62 | 127 |
| 49 | Supertrend · 1h | trend | 73.25 | -26.75 | 167 | 13.2 | -29.29 | -5.03 | -34.92 | 226 |
| 50 | RSI momentum · 1h | momentum | 72.93 | -27.07 | 159 | 12.6 | -23.55 | -3.74 | -33.01 | 218 |
| 51 | Triple EMA stack · 1h | trend | 72.38 | -27.62 | 143 | 14.7 | -26.43 | -4.59 | -34.87 | 204 |
| 52 | ROC + volume · 1h | momentum | 71.71 | -28.29 | 349 | 25.5 | -36.07 | -6.73 | -38.89 | 383 |
| 53 | OBV trend · 1h | momentum | 71.62 | -28.38 | 274 | 18.2 | -27.25 | -5.03 | -34.12 | 275 |
| 54 | Donchian 20/10 · 1h | breakout | 70.38 | -29.62 | 142 | 19.7 | -29.88 | -5.49 | -35.64 | 207 |
| 55 | Daily: Momentum burst | daily | 70.36 | -29.64 | 26 | 11.5 | -39.31 | -5.63 | -39.66 | 31 |
| 56 | RSI(14) reversion · 1h | reversion | 68.37 | -31.63 | 162 | 31.5 | -31.22 | -4.58 | -34.81 | 248 |
| 57 | Max aggression: 1-day momentum | meta | 68.25 | -31.75 | 27 | 25.9 | -31.45 | -1.58 | -57.50 | 42 |
| 58 | VWAP momentum · 1h | momentum | 67.53 | -32.47 | 812 | 21.6 | -51.71 | -11.03 | -53.44 | 1236 |
| 59 | Agent (ML meta-label) | meta | 67.50 | -32.49 | 1635 | 24.2 | -8.22 | -1.22 | -17.71 | 316 |
| 60 | EMA 9/21 cross · 1h | trend | 65.51 | -34.49 | 247 | 9.7 | -38.39 | -7.57 | -40.15 | 336 |
| 61 | Candlestick reversal · 1h | reversion | 64.73 | -35.27 | 434 | 28.6 | -37.07 | -6.64 | -37.76 | 592 |
| 62 | Three white soldiers | momentum | 61.82 | -38.18 | 498 | 15.1 | -48.74 | -22.67 | -48.74 | 647 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.97 | -98.94 | 5240 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.85 | -26.22 | -79.85 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.18 | -45.08 | -93.20 | 2515 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.00 | -31.36 | -89.02 | 1901 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.60 | -38.41 | -90.61 | 2315 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.11 | -31.04 | -90.17 | 2200 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.68 | -52.24 | -97.69 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -56.26 | -96.31 | 3423 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -32.00 | -93.78 | 2437 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.12 | -33.71 | -82.17 | 1675 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -53.77 | -99.53 | 5969 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.31 | -42.41 | -92.36 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -36.15 | -95.49 | 3409 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.34 | -99.80 | 6162 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -42.02 | -91.76 | 2257 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.39 | -24.36 | -75.64 | 1595 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -58.74 | -97.68 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -60.31 | -98.84 | 4879 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.54 | -26.81 | -69.10 | 1218 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.52 | -51.62 | -94.52 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.58 | -36.45 | -84.58 | 1780 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -69.49 | -99.65 | 6362 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.66 | -31.90 | -89.68 | 2272 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.47 | -19.85 | -78.53 | 1745 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.49 | -35.71 | -90.58 | 2218 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.80 | -50.13 | -96.80 | 3878 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.20 | -54.39 | -89.23 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.13 | -28.31 | -66.44 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -70.99 | -22.61 | -71.58 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.80 | -19.12 | -79.80 | 1681 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.29 | -48.02 | -97.31 | 4311 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -95.49 | -99.93 | 8311 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T02:25 | Agent (ML meta-label) | buy | XRP-USD | 6.08 | — | entry |
| 2026-11-10T02:20 | Agent (ML meta-label) | sell | XRP-USD | 5.15 | -0.05 | selected signal exited |
| 2026-11-10T02:15 | Agent (ML meta-label) | buy | XRP-USD | 5.20 | — | entry |
| 2026-11-10T02:05 | Agent (ML meta-label) | sell | XRP-USD | 5.17 | -0.04 | selected signal exited |
| 2026-11-10T02:00 | Agent (ML meta-label) | buy | XRP-USD | 5.21 | — | entry |
| 2026-11-10T02:00 | VWAP momentum · 1h | sell | XRP-USD | 3.54 | -0.02 | exit signal |
| 2026-11-10T02:00 | Heikin-Ashi · 1h | sell | BTC-USD | 4.94 | -0.05 | exit signal |
| 2026-11-10T01:00 | VWAP momentum · 1h | buy | XRP-USD | 3.56 | — | entry signal |
| 2026-11-10T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 5.96 | -0.04 | exit signal |
| 2026-11-10T00:20 | Three white soldiers | sell | XRP-USD | 15.36 | -0.12 | exit signal |
| 2026-11-10T00:10 | Three white soldiers | buy | XRP-USD | 15.49 | — | entry signal |
| 2026-11-10T00:00 | Heikin-Ashi · 1h | buy | BTC-USD | 4.99 | — | entry signal |
| 2026-11-09T23:05 | Three white soldiers | sell | XRP-USD | 15.50 | -0.08 | exit signal |
| 2026-11-09T23:05 | Three white soldiers | sell | SOL-USD | 15.42 | -0.16 | stop-loss |
| 2026-11-09T23:05 | Three white soldiers | sell | ETH-USD | 15.45 | -0.13 | exit signal |
| 2026-11-09T23:00 | CCI reversion · 1h | buy | SOL-USD | 4.75 | — | rebalance up |
| 2026-11-09T23:00 | CCI reversion · 1h | sell | BTC-USD | 9.93 | 0.00 | exit signal |
| 2026-11-09T23:00 | Candlestick reversal · 1h | buy | SOL-USD | 1.98 | — | entry signal |
| 2026-11-09T22:40 | Three white soldiers | buy | XRP-USD | 15.58 | — | entry signal |
| 2026-11-09T22:40 | Three white soldiers | buy | SOL-USD | 15.58 | — | entry signal |
| 2026-11-09T22:40 | Three white soldiers | buy | ETH-USD | 15.58 | — | entry signal |
| 2026-11-09T22:00 | Agent (ML meta-label) | sell | SOL-USD | 7.51 | -0.10 | selected signal exited |
| 2026-11-09T22:00 | MFI reversion · 1h | sell | SOL-USD | 13.15 | -0.15 | exit signal |
| 2026-11-09T21:06 | Candlestick reversal · 1h | buy | XRP-USD | 9.28 | — | entry |
| 2026-11-09T21:06 | Candlestick reversal · 1h | sell | ETH-USD | 3.75 | -0.01 | rebalance down |
| 2026-11-09T21:06 | Candlestick reversal · 1h | sell | DOGE-USD | 3.75 | -0.02 | rebalance down |
| 2026-11-09T21:06 | Candlestick reversal · 1h | sell | BTC-USD | 3.76 | -0.01 | rebalance down |
| 2026-11-09T21:00 | MFI reversion · 1h | buy | SOL-USD | 4.72 | — | rebalance up |
| 2026-11-09T21:00 | MFI reversion · 1h | buy | ETH-USD | 4.72 | — | rebalance up |
| 2026-11-09T21:00 | MFI reversion · 1h | buy | DOGE-USD | 4.57 | — | rebalance up |
| 2026-11-09T20:55 | Agent (rotation) | sell | TQQQ | 66.10 | 2.93 | selected signal exited |
| 2026-11-09T20:55 | Day trade: Stocks in Play ORB | sell | TNA | 25.44 | 1.11 | target is flat |
| 2026-11-09T20:55 | Day trade: Stocks in Play ORB | sell | SOXL | 27.20 | 2.87 | target is flat |
| 2026-11-09T20:55 | Day trade: Stocks in Play ORB | sell | ETHU | 24.79 | 0.10 | target is flat |
| 2026-11-09T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 103.97 | 2.31 | target is flat |
| 2026-11-09T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 117.56 | 3.97 | target is flat |
| 2026-11-09T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 93.19 | -0.91 | target is flat |
| 2026-11-09T20:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 111.93 | 6.10 | target is flat |
| 2026-11-09T20:55 | Agent | sell | TSLA | 17.43 | -0.06 | selected signal exited |
| 2026-11-09T20:55 | Agent | sell | SQQQ | 17.43 | -0.01 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 02:35:05.000123+00:00 -> 2026-11-10 02:45:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-12 02:35:05.000123+00:00 -> 2026-11-10 02:45:05.000123+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-12 02:35:05.000123+00:00 -> 2026-11-10 02:45:05.000123+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
