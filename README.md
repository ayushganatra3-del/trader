# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T22:35:05.000119+00:00 · 53881 ticks

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
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 29.11 · VIX 19.90 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 39030 decisions in 3507 calls, $0.4857 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T22:35 | 2 / 3 / 0 | SOL-USD 14% |  |
| Breezy | 2026-11-09T22:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-09T22:35 | 2 / 3 / 0 | BTC-USD 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| VWAP momentum | TSLA | 1.69 | +2.40% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 18.87 | 3.81 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.33 | 12.33 | 0 | — | 13.79 | 4.70 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.93 | 11.93 | 31 | 29.0 | 20.12 | 3.03 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.01 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.55 | 1.55 | 126 | 36.5 | 10.08 | 3.83 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 101.12 | 1.12 | 0 | — | 4.81 | 1.39 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.90 | 0.90 | 7 | 42.9 | -0.93 | 0.20 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.68 | 1.10 | -9.06 | 240 |
| 11 | Agent (rotation) | meta | 98.10 | -1.90 | 177 | 28.2 | -3.43 | -1.36 | -10.59 | 169 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -13.23 | -3.42 | -13.23 | 152 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.41 | -3.59 | 0 | — | -1.49 | -0.45 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.82 | -5.18 | 0 | — | -3.54 | -0.89 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.78 | -8.67 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.73 | -7.27 | 0 | — | -4.02 | -1.06 | -10.64 | 1 |
| 19 | Trend pullback · 1h | trend | 92.53 | -7.47 | 108 | 23.1 | -13.74 | -5.16 | -17.96 | 79 |
| 20 | Copy: Insider buying | copy | 91.98 | -8.02 | 42 | 38.1 | -9.58 | -2.01 | -16.06 | 63 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 90.34 | -9.66 | 391 | 34.3 | -13.39 | -4.27 | -15.24 | 595 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.56 | -3.45 | -14.68 | 80 |
| 24 | Hold BTC | benchmark | 87.13 | -12.87 | 1 | 0.0 | -4.63 | -0.52 | -15.58 | 1 |
| 25 | Agent | meta | 86.80 | -13.20 | 163 | 35.0 | -13.72 | -7.11 | -14.18 | 205 |
| 26 | Daily: Bullish score | daily | 86.09 | -13.91 | 15 | 20.0 | -10.31 | -1.58 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.52 | -14.48 | 167 | 26.9 | -11.32 | -2.05 | -21.29 | 227 |
| 28 | Agent (aggressive) | meta | 83.88 | -16.12 | 76 | 31.6 | -16.53 | -4.75 | -18.49 | 94 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 83.70 | -16.30 | 2 | 0.0 | -7.65 | -0.85 | -24.16 | 1 |
| 30 | Opening range 15m | breakout | 83.50 | -16.50 | 481 | 32.4 | -18.38 | -5.25 | -19.91 | 728 |
| 31 | Donchian 55/20 · 1h | breakout | 83.36 | -16.64 | 71 | 14.1 | -18.18 | -4.00 | -22.45 | 104 |
| 32 | Stochastic reversion · 1h | reversion | 83.15 | -16.85 | 279 | 48.4 | -23.96 | -3.55 | -28.05 | 387 |
| 33 | Keltner breakout · 1h | breakout | 81.92 | -18.08 | 107 | 23.4 | -22.13 | -4.49 | -25.12 | 173 |
| 34 | Volume breakout · 1h | breakout | 81.30 | -18.70 | 145 | 27.6 | -14.82 | -3.37 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.58 | -19.43 | 205 | 40.0 | -19.67 | -6.61 | -19.99 | 124 |
| 36 | Heikin-Ashi · 1h | trend | 79.80 | -20.20 | 400 | 22.8 | -39.74 | -7.43 | -43.08 | 674 |
| 37 | ADX DI cross · 1h | trend | 79.31 | -20.69 | 179 | 18.4 | -22.37 | -3.86 | -28.34 | 274 |
| 38 | MFI reversion · 1h | reversion | 79.24 | -20.76 | 352 | 34.4 | -16.66 | -2.14 | -21.23 | 167 |
| 39 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -39.47 | -2.65 | -45.81 | 25 |
| 40 | CCI reversion · 1h | reversion | 79.14 | -20.86 | 319 | 45.8 | -23.35 | -3.54 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.06 | -22.94 | 96 | 15.6 | -29.65 | -8.49 | -29.87 | 119 |
| 42 | Bollinger breakout · 1h | breakout | 76.79 | -23.21 | 170 | 22.9 | -22.64 | -4.76 | -27.92 | 240 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -25.50 | -3.90 | -32.28 | 372 |
| 44 | MACD cross · 1h | trend | 75.26 | -24.74 | 349 | 22.6 | -32.93 | -5.41 | -39.46 | 485 |
| 45 | Z-score reversion · 1h | reversion | 75.24 | -24.75 | 179 | 37.4 | -20.10 | -2.86 | -27.66 | 228 |
| 46 | Williams %R · 1h | reversion | 74.87 | -25.13 | 337 | 46.9 | -35.76 | -5.85 | -38.92 | 540 |
| 47 | MACD zero-line · 1h | trend | 74.37 | -25.62 | 157 | 16.6 | -24.78 | -5.10 | -29.19 | 213 |
| 48 | EMA 20/50 cross · 1h | trend | 74.10 | -25.90 | 102 | 10.8 | -24.45 | -4.40 | -32.62 | 127 |
| 49 | Supertrend · 1h | trend | 73.27 | -26.73 | 167 | 13.2 | -29.27 | -5.07 | -34.92 | 226 |
| 50 | RSI momentum · 1h | momentum | 72.95 | -27.05 | 159 | 12.6 | -23.55 | -3.77 | -33.01 | 218 |
| 51 | Triple EMA stack · 1h | trend | 72.39 | -27.61 | 143 | 14.7 | -26.52 | -4.65 | -34.87 | 203 |
| 52 | ROC + volume · 1h | momentum | 71.72 | -28.28 | 349 | 25.5 | -36.08 | -6.79 | -38.89 | 385 |
| 53 | OBV trend · 1h | momentum | 71.64 | -28.36 | 274 | 18.2 | -26.98 | -5.01 | -34.09 | 275 |
| 54 | Donchian 20/10 · 1h | breakout | 70.39 | -29.61 | 142 | 19.7 | -29.88 | -5.53 | -35.64 | 207 |
| 55 | Daily: Momentum burst | daily | 70.36 | -29.64 | 26 | 11.5 | -39.31 | -5.68 | -39.66 | 31 |
| 56 | RSI(14) reversion · 1h | reversion | 68.55 | -31.45 | 162 | 31.5 | -31.43 | -4.64 | -35.13 | 249 |
| 57 | Max aggression: 1-day momentum | meta | 68.27 | -31.73 | 27 | 25.9 | -31.45 | -1.60 | -57.50 | 42 |
| 58 | Agent (ML meta-label) | meta | 67.71 | -32.29 | 1633 | 24.2 | -5.94 | -0.84 | -16.95 | 325 |
| 59 | VWAP momentum · 1h | momentum | 67.60 | -32.40 | 810 | 21.6 | -51.92 | -11.22 | -53.43 | 1237 |
| 60 | EMA 9/21 cross · 1h | trend | 65.56 | -34.44 | 247 | 9.7 | -38.34 | -7.62 | -40.15 | 335 |
| 61 | Candlestick reversal · 1h | reversion | 64.96 | -35.04 | 434 | 28.6 | -37.86 | -6.88 | -38.67 | 594 |
| 62 | Three white soldiers | momentum | 62.31 | -37.69 | 494 | 15.2 | -48.59 | -22.77 | -48.59 | 645 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -45.92 | -98.96 | 5253 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.78 | -26.51 | -79.80 | 1421 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.12 | -46.36 | -93.20 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.02 | -32.18 | -89.09 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.57 | -39.85 | -90.64 | 2317 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.01 | -31.49 | -90.07 | 2195 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -54.83 | -97.66 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -58.95 | -96.24 | 3419 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -32.68 | -93.71 | 2431 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.00 | -34.31 | -82.22 | 1675 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -56.10 | -99.53 | 5967 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.33 | -43.65 | -92.47 | 2613 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.44 | -36.94 | -95.44 | 3399 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -76.92 | -99.80 | 6161 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.70 | -43.89 | -91.71 | 2258 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.60 | -24.77 | -75.70 | 1601 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -62.27 | -97.66 | 3519 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.90 | -98.84 | 4882 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.54 | -27.25 | -69.23 | 1218 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.48 | -55.24 | -94.48 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.72 | -37.82 | -84.72 | 1786 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.27 | -99.65 | 6365 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.59 | -32.62 | -89.67 | 2270 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.39 | -20.17 | -78.45 | 1744 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.47 | -36.71 | -90.60 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -52.78 | -96.81 | 3878 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.45 | -58.11 | -89.45 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.22 | -29.18 | -66.43 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.07 | -22.93 | -71.81 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.71 | -19.19 | -79.71 | 1680 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -49.98 | -97.32 | 4311 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.18 | -99.93 | 8311 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-09T20:55 | Opening range 30m | sell | UPRO | 8.24 | 0.14 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | TQQQ | 7.42 | 0.14 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | TNA | 8.37 | 0.25 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | TECL | 8.30 | 0.18 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | SPY | 8.14 | 0.03 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | SOXL | 8.40 | 0.28 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | QQQ | 8.16 | 0.04 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | PLTR | 2.36 | 0.01 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | LABU | 6.48 | 0.06 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | IWM | 8.19 | 0.07 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | COIN | 2.32 | -0.01 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | AMD | 8.38 | 0.26 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | AAPL | 5.60 | 0.00 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | UPRO | 5.59 | 0.12 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | TQQQ | 5.63 | 0.16 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | TNA | 5.69 | 0.21 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | TECL | 5.68 | 0.20 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | SPY | 5.51 | 0.03 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | SOXL | 5.86 | 0.39 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | QQQ | 5.52 | 0.05 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | PLTR | 5.53 | 0.05 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 22:35:05.000119+00:00 -> 2026-11-09 22:45:05.000119+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 22:35:05.000119+00:00 -> 2026-11-09 22:45:05.000119+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 22:35:05.000119+00:00 -> 2026-11-09 22:45:05.000119+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
