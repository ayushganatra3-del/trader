# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-08T02:20:05.000129+00:00 · 51575 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.54 (-12.46%)

Closed trades 156, win rate 35.9%, fees £4.84, max drawdown -12.87%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 1740 decisions in 348 calls, $0.0244 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-08T02:20 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-08T02:20 | 0 / 4 / 1 | cash |  |
| Boozy | 2026-11-08T02:20 | 0 / 2 / 3 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 1.95 | +8.75% | 6 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| VWAP reversion | SQQQ | 1.93 | +6.85% | 4 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.81 | -1.19 | 123 | 47.2 | -12.92 | -3.06 | -13.86 | 150 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.46 | 2.83 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.36 | -4.63 | -10.34 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.52 | -0.42 | -9.14 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -15.76 | -5.92 | -17.86 | 80 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.48 | -5.32 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -23.46 | -4.41 | -26.45 | 64 |
| 23 | Daily: Bullish score | daily | 88.75 | -11.25 | 15 | 20.0 | -5.01 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.27 | -3.58 | -14.68 | 85 |
| 25 | Hold BTC | benchmark | 88.35 | -11.65 | 1 | 0.0 | -5.51 | -0.53 | -14.09 | 1 |
| 26 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -14.32 | -7.67 | -14.33 | 197 |
| 27 | Parabolic SAR · 1h | trend | 86.90 | -13.10 | 166 | 27.1 | -13.51 | -2.98 | -20.50 | 236 |
| 28 | Donchian 55/20 · 1h | breakout | 85.94 | -14.06 | 71 | 14.1 | -12.75 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 85.15 | -14.85 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.23 | -5.45 | -18.65 | 93 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.02 | -17.98 | 261 | 46.7 | -25.09 | -3.70 | -29.25 | 392 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.62 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.36 | -20.64 | 175 | 18.3 | -24.06 | -4.02 | -27.04 | 261 |
| 38 | MFI reversion · 1h | reversion | 78.26 | -21.74 | 337 | 34.1 | -18.64 | -2.64 | -19.84 | 156 |
| 39 | Ichimoku · 1h | trend | 77.87 | -22.12 | 94 | 14.9 | -22.75 | -4.65 | -29.43 | 124 |
| 40 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.48 | -4.89 | -27.58 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.43 | -23.57 | 292 | 45.5 | -29.56 | -4.81 | -29.99 | 465 |
| 42 | EMA 20/50 cross · 1h | trend | 76.07 | -23.93 | 102 | 10.8 | -23.17 | -4.20 | -30.58 | 130 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -43.00 | -9.00 | -43.00 | 676 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.57 | -5.28 | -29.20 | 209 |
| 45 | Triple EMA stack · 1h | trend | 74.45 | -25.55 | 142 | 14.8 | -29.18 | -6.17 | -33.47 | 203 |
| 46 | Supertrend · 1h | trend | 73.62 | -26.38 | 166 | 13.3 | -29.40 | -5.10 | -34.80 | 214 |
| 47 | RSI momentum · 1h | momentum | 73.46 | -26.54 | 158 | 12.7 | -27.53 | -5.25 | -32.60 | 217 |
| 48 | Z-score reversion · 1h | reversion | 72.90 | -27.11 | 163 | 35.6 | -25.24 | -3.75 | -27.66 | 227 |
| 49 | MACD cross · 1h | trend | 72.85 | -27.15 | 341 | 23.2 | -35.07 | -6.22 | -38.91 | 479 |
| 50 | Bollinger reversion · 1h | reversion | 72.75 | -27.25 | 252 | 40.1 | -30.03 | -5.14 | -32.99 | 369 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -36.21 | -5.81 | -38.11 | 536 |
| 52 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.93 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.46 | -28.54 | 141 | 19.9 | -30.01 | -5.56 | -34.69 | 212 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -29.88 | -6.13 | -34.37 | 285 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -38.08 | -7.41 | -38.98 | 381 |
| 56 | EMA 9/21 cross · 1h | trend | 67.14 | -32.86 | 243 | 9.9 | -38.78 | -7.98 | -39.18 | 332 |
| 57 | VWAP momentum · 1h | momentum | 66.67 | -33.33 | 788 | 21.8 | -55.06 | -12.08 | -55.06 | 1235 |
| 58 | Agent (ML meta-label) | meta | 66.34 | -33.66 | 1540 | 23.0 | -12.18 | -1.97 | -22.56 | 345 |
| 59 | RSI(14) reversion · 1h | reversion | 66.11 | -33.89 | 143 | 27.3 | -30.80 | -4.85 | -31.54 | 226 |
| 60 | Candlestick reversal · 1h | reversion | 65.11 | -34.89 | 415 | 28.2 | -38.98 | -7.21 | -39.16 | 583 |
| 61 | Three white soldiers | momentum | 63.96 | -36.04 | 476 | 15.3 | -49.08 | -22.37 | -49.08 | 651 |
| 62 | Max aggression: 1-day momentum | meta | 62.21 | -37.79 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -44.23 | -98.92 | 5218 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.75 | -25.72 | -80.75 | 1433 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.38 | -45.52 | -93.38 | 2509 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -31.53 | -88.85 | 1898 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.60 | -38.73 | -90.64 | 2296 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.10 | -31.66 | -90.10 | 2190 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -52.22 | -97.73 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -54.47 | -96.27 | 3400 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.72 | -33.66 | -93.72 | 2440 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.08 | -33.71 | -82.16 | 1645 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -52.59 | -99.53 | 5998 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.62 | -42.59 | -92.62 | 2601 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.67 | -37.61 | -95.67 | 3410 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -68.83 | -99.80 | 6182 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.74 | -41.88 | -91.74 | 2275 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.45 | -24.42 | -75.45 | 1572 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -59.74 | -97.75 | 3511 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.81 | -59.34 | -98.81 | 4889 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.08 | -28.96 | -70.08 | 1207 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -51.95 | -94.59 | 2740 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.56 | -35.93 | -84.56 | 1752 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -68.98 | -99.64 | 6382 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.45 | -31.31 | -89.45 | 2303 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.08 | -19.59 | -78.08 | 1754 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.24 | -37.06 | -91.24 | 2233 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.73 | -49.94 | -96.73 | 3900 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.48 | -53.85 | -89.48 | 2165 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.25 | -27.91 | -65.33 | 792 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.89 | -23.85 | -72.94 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.64 | -18.24 | -78.68 | 1673 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.31 | -48.56 | -97.31 | 4339 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -95.71 | -99.93 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-08T02:00 | VWAP momentum · 1h | sell | BTC-USD | 7.36 | -0.05 | exit signal |
| 2026-11-08T01:00 | VWAP momentum · 1h | buy | BTC-USD | 7.42 | — | entry signal |
| 2026-11-08T01:00 | VWAP momentum · 1h | sell | ETH-USD | 7.36 | -0.05 | exit signal |
| 2026-11-08T00:05 | Agent | sell | DOGE-USD | 17.41 | -0.12 | selected signal exited |
| 2026-11-08T00:00 | Agent | buy | DOGE-USD | 17.53 | — | following Candlestick reversal · 1h |
| 2026-11-08T00:00 | CCI reversion · 1h | buy | DOGE-USD | 3.48 | — | entry signal |
| 2026-11-08T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.10 | — | entry signal |
| 2026-11-08T00:00 | VWAP momentum · 1h | buy | ETH-USD | 7.42 | — | entry signal |
| 2026-11-08T00:00 | MACD cross · 1h | buy | ETH-USD | 5.61 | — | entry signal |
| 2026-11-07T23:05 | Agent | sell | DOGE-USD | 17.46 | -0.09 | selected signal exited |
| 2026-11-07T23:05 | Candlestick reversal · 1h | sell | DOGE-USD | 4.10 | -0.02 | target is flat |
| 2026-11-07T23:00 | CCI reversion · 1h | buy | ETH-USD | 3.82 | — | entry signal |
| 2026-11-07T23:00 | MACD cross · 1h | buy | BTC-USD | 6.08 | — | entry signal |
| 2026-11-07T22:00 | Agent | buy | DOGE-USD | 17.55 | — | following Candlestick reversal · 1h |
| 2026-11-07T22:00 | VWAP reversion · 1h | buy | SOL-USD | 24.78 | — | entry signal |
| 2026-11-07T22:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.78 | — | entry signal |
| 2026-11-07T22:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.12 | — | entry signal |
| 2026-11-07T22:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.93 | — | entry signal |
| 2026-11-07T21:20 | CCI reversion · 1h | sell | DOGE-USD | 3.76 | -0.07 | stop-loss |
| 2026-11-07T21:15 | CCI reversion · 1h | sell | SOL-USD | 3.95 | -0.09 | stop-loss |
| 2026-11-07T21:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.26 | -0.03 | exit signal |
| 2026-11-07T21:00 | MACD cross · 1h | sell | BTC-USD | 6.65 | -0.00 | exit signal |
| 2026-11-07T20:55 | Bollinger reversion · 1h | buy | BTC-USD | 4.37 | — | entry |
| 2026-11-07T20:55 | Bollinger reversion · 1h | sell | SOL-USD | 4.37 | -0.08 | stop-loss |
| 2026-11-07T20:55 | Candlestick reversal · 1h | sell | SOL-USD | 4.79 | -0.09 | stop-loss |
| 2026-11-07T20:55 | MACD cross · 1h | sell | DOGE-USD | 5.53 | -0.09 | stop-loss |
| 2026-11-07T20:50 | Agent | sell | DOGE-USD | 17.32 | -0.29 | selected signal exited |
| 2026-11-07T20:50 | Candlestick reversal · 1h | buy | BTC-USD | 5.29 | — | entry |
| 2026-11-07T20:50 | Candlestick reversal · 1h | sell | DOGE-USD | 5.29 | -0.09 | stop-loss |
| 2026-11-07T20:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.36 | -0.07 | exit signal |
| 2026-11-07T19:00 | CCI reversion · 1h | buy | BTC-USD | 1.31 | — | entry signal |
| 2026-11-07T19:00 | VWAP reversion · 1h | sell | DOGE-USD | 24.75 | -0.04 | exit signal |
| 2026-11-07T19:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.43 | — | entry signal |
| 2026-11-07T19:00 | MACD cross · 1h | buy | DOGE-USD | 5.62 | — | entry signal |
| 2026-11-07T18:00 | MACD cross · 1h | sell | ETH-USD | 6.68 | 0.01 | exit signal |
| 2026-11-07T17:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.79 | — | entry signal |
| 2026-11-07T16:00 | Bollinger breakout · 1h | sell | ETH-USD | 19.20 | -0.19 | exit signal |
| 2026-11-07T16:00 | Donchian 20/10 · 1h | sell | SOL-USD | 17.45 | -0.37 | exit signal |
| 2026-11-07T16:00 | MACD cross · 1h | sell | SOL-USD | 6.61 | -0.01 | exit signal |
| 2026-11-07T16:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 16.66 | -0.16 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-10 02:20:05.000129+00:00 -> 2026-11-08 02:30:05.000129+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-10 02:20:05.000129+00:00 -> 2026-11-08 02:30:05.000129+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-10 02:20:05.000129+00:00 -> 2026-11-08 02:30:05.000129+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
