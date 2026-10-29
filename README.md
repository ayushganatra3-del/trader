# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-29T23:45:05.000128+00:00 · 40765 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.68 (-8.32%)

Closed trades 122, win rate 40.2%, fees £3.61, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-29 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, RENT 12%, CTY 12%, ACN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-29)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.18 · VIX 17.20 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, IWM 5.9, LABU 5.7, AAPL 5.2, SQQQ 4.9, PLTR 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 39267 decisions in 3528 calls, $0.4898 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-29T23:45 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-29T23:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-29T23:45 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.83 | +8.30% | 12 |
| VWAP momentum · 1h | LABU | 2.51 | +26.96% | 3 |
| VWAP reversion | SQQQ | 2.50 | +4.75% | 5 |
| MACD zero-line | MSFT | 2.39 | +0.71% | 6 |
| Z-score reversion | TSLA | 2.35 | +3.07% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.23 | 2.05 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 106.26 | 6.26 | 0 | — | 7.59 | 3.75 | -5.18 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.88 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.25 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.07 | 1.07 | 0 | — | 4.35 | 1.91 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.40 | 0.40 | 93 | 46.2 | -11.80 | -3.29 | -12.60 | 140 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.97 | -1.03 | 0 | — | 0.56 | 0.37 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 6.78 | 3.21 | -1.98 | 91 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.74 | -2.54 | -5.83 | 1 |
| 12 | Copy: Congress Democrats (NANC) | copy | 97.06 | -2.94 | 0 | — | -0.48 | -0.15 | -5.99 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -5.09 | -5.87 | -5.22 | 22 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.79 | -3.21 | 0 | — | -5.05 | -2.03 | -7.83 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -3.29 | -2.13 | -7.48 | 173 |
| 17 | Three white soldiers · 1h | momentum | 95.09 | -4.91 | 16 | 12.5 | -2.55 | -2.35 | -4.76 | 27 |
| 18 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 4.93 | 1.63 | -8.76 | 204 |
| 19 | Copy: Cathie Wood (ARKK) | copy | 93.46 | -6.54 | 0 | — | 2.42 | 0.58 | -14.57 | 1 |
| 20 | Copy: Insider buying | copy | 92.67 | -7.33 | 33 | 36.4 | -20.02 | -3.97 | -24.43 | 67 |
| 21 | Hold BTC | benchmark | 92.44 | -7.56 | 0 | — | 0.28 | 0.22 | -10.39 | 1 |
| 22 | Donchian 55/20 · 1h | breakout | 92.30 | -7.71 | 54 | 14.8 | -13.77 | -3.12 | -15.51 | 102 |
| 23 | Daily: Momentum burst | daily | 91.98 | -8.02 | 15 | 13.3 | -12.93 | -2.44 | -17.57 | 35 |
| 24 | Opening range 30m | breakout | 91.77 | -8.23 | 304 | 35.5 | -11.10 | -3.33 | -17.21 | 580 |
| 25 | Agent | meta | 91.68 | -8.32 | 122 | 40.2 | -9.57 | -5.77 | -12.21 | 221 |
| 26 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.65 | -7.62 | -21.65 | 101 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.75 | -2.70 | -16.91 | 1 |
| 28 | Squeeze breakout · 1h | breakout | 90.62 | -9.38 | 56 | 23.2 | -4.98 | -1.36 | -12.65 | 93 |
| 29 | Daily: Bullish score | daily | 90.49 | -9.51 | 12 | 25.0 | -5.76 | -0.70 | -14.40 | 14 |
| 30 | Parabolic SAR · 1h | trend | 90.05 | -9.95 | 137 | 28.5 | -19.98 | -4.68 | -20.21 | 248 |
| 31 | ADX DI cross · 1h | trend | 89.47 | -10.53 | 137 | 19.7 | -15.01 | -3.04 | -16.59 | 260 |
| 32 | Stochastic reversion · 1h | reversion | 87.92 | -12.08 | 218 | 48.2 | -15.25 | -2.64 | -22.33 | 376 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 87.67 | -12.33 | 14 | 42.9 | -14.69 | -1.28 | -27.23 | 25 |
| 34 | Agent (aggressive) | meta | 87.41 | -12.59 | 62 | 35.5 | -11.10 | -3.69 | -15.04 | 101 |
| 35 | Volume breakout · 1h | breakout | 86.62 | -13.38 | 124 | 29.8 | -14.65 | -3.15 | -17.33 | 107 |
| 36 | Bollinger breakout · 1h | breakout | 85.99 | -14.01 | 128 | 26.6 | -11.99 | -2.17 | -19.10 | 244 |
| 37 | Z-score reversion · 1h | reversion | 85.83 | -14.17 | 126 | 35.7 | -12.78 | -1.98 | -21.48 | 205 |
| 38 | Keltner breakout · 1h | breakout | 85.36 | -14.64 | 84 | 23.8 | -22.93 | -4.67 | -23.96 | 196 |
| 39 | Ichimoku · 1h | trend | 84.48 | -15.52 | 75 | 10.7 | -18.75 | -3.79 | -24.73 | 118 |
| 40 | Opening range 15m | breakout | 84.37 | -15.63 | 376 | 32.2 | -16.00 | -4.63 | -18.10 | 709 |
| 41 | Connors RSI(2) · 1h | reversion | 84.21 | -15.79 | 185 | 40.5 | -21.05 | -6.78 | -21.83 | 163 |
| 42 | Supertrend · 1h | trend | 83.76 | -16.24 | 126 | 14.3 | -23.64 | -4.55 | -26.18 | 218 |
| 43 | RSI momentum · 1h | momentum | 83.33 | -16.67 | 122 | 13.1 | -20.40 | -4.08 | -23.98 | 214 |
| 44 | Triple EMA stack · 1h | trend | 82.49 | -17.51 | 113 | 14.2 | -27.74 | -5.40 | -30.37 | 208 |
| 45 | MFI reversion · 1h | reversion | 82.11 | -17.89 | 288 | 32.3 | -17.87 | -2.85 | -19.58 | 151 |
| 46 | Williams %R · 1h | reversion | 81.82 | -18.18 | 249 | 47.8 | -32.99 | -5.83 | -34.58 | 524 |
| 47 | MACD cross · 1h | trend | 81.66 | -18.34 | 275 | 24.7 | -28.41 | -5.14 | -29.24 | 476 |
| 48 | EMA 20/50 cross · 1h | trend | 81.62 | -18.38 | 86 | 11.6 | -22.08 | -4.01 | -24.96 | 138 |
| 49 | CCI reversion · 1h | reversion | 81.58 | -18.42 | 245 | 46.5 | -21.56 | -3.05 | -28.07 | 447 |
| 50 | Bollinger reversion · 1h | reversion | 81.06 | -18.95 | 191 | 38.7 | -29.44 | -6.10 | -31.30 | 364 |
| 51 | Donchian 20/10 · 1h | breakout | 80.58 | -19.42 | 108 | 21.3 | -22.28 | -4.12 | -26.02 | 219 |
| 52 | OBV trend · 1h | momentum | 79.54 | -20.46 | 225 | 16.9 | -34.03 | -6.68 | -36.14 | 300 |
| 53 | MACD zero-line · 1h | trend | 79.11 | -20.89 | 129 | 16.3 | -24.19 | -4.90 | -26.72 | 213 |
| 54 | RSI(14) reversion · 1h | reversion | 78.93 | -21.07 | 110 | 27.3 | -19.95 | -3.64 | -24.99 | 205 |
| 55 | Heikin-Ashi · 1h | trend | 77.25 | -22.75 | 327 | 23.9 | -42.48 | -9.31 | -42.81 | 669 |
| 56 | Candlestick reversal · 1h | reversion | 76.87 | -23.13 | 304 | 29.9 | -34.84 | -7.02 | -36.03 | 548 |
| 57 | Agent (ML meta-label) ⏸ | meta | 76.69 | -23.31 | 1105 | 21.0 | -14.71 | -2.79 | -19.65 | 354 |
| 58 | ROC + volume · 1h | momentum | 76.55 | -23.45 | 286 | 25.9 | -30.75 | -5.45 | -31.92 | 391 |
| 59 | EMA 9/21 cross · 1h | trend | 74.69 | -25.31 | 195 | 10.3 | -31.55 | -6.36 | -32.28 | 341 |
| 60 | Three white soldiers | momentum | 74.52 | -25.48 | 357 | 17.6 | -44.82 | -21.21 | -44.83 | 610 |
| 61 | VWAP momentum · 1h | momentum | 73.84 | -26.16 | 632 | 22.9 | -51.38 | -10.92 | -51.49 | 1236 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 72.15 | -27.85 | 21 | 33.3 | -35.91 | -2.18 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -45.24 | -98.88 | 5186 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.90 | -23.91 | -78.91 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.56 | -46.47 | -93.56 | 2535 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.78 | -31.39 | -88.78 | 1913 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -39.37 | -91.31 | 2343 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.65 | -33.12 | -90.65 | 2263 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -55.25 | -97.78 | 3511 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -61.01 | -96.19 | 3391 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.06 | -36.03 | -94.06 | 2477 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.01 | -34.32 | -82.01 | 1688 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -57.35 | -99.43 | 5772 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.94 | -45.08 | -92.95 | 2627 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.63 | -39.48 | -95.63 | 3485 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -83.88 | -99.78 | 6187 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.00 | -46.26 | -92.02 | 2304 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.10 | -27.70 | -75.11 | 1563 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -65.69 | -97.71 | 3579 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.61 | -63.19 | -98.61 | 4786 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.90 | -29.93 | -69.98 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.79 | -57.94 | -94.80 | 2791 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.81 | -39.62 | -84.81 | 1824 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -73.95 | -99.60 | 6295 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.93 | -30.24 | -87.93 | 2209 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.80 | -19.78 | -76.80 | 1678 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.54 | -38.23 | -90.54 | 2241 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.18 | -52.61 | -96.21 | 3775 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.74 | -54.22 | -89.74 | 2123 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.48 | -26.02 | -64.48 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.54 | -25.82 | -73.54 | 1277 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.83 | -18.49 | -75.85 | 1566 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.63 | -52.54 | -96.63 | 4196 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -113.97 | -99.92 | 8294 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-29T22:00 | VWAP reversion · 1h | buy | XRP-USD | 25.28 | — | entry signal |
| 2026-10-29T22:00 | VWAP reversion · 1h | buy | BTC-USD | 25.28 | — | entry signal |
| 2026-10-29T22:00 | RSI(14) reversion · 1h | buy | SOL-USD | 6.61 | — | entry signal |
| 2026-10-29T22:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 13.21 | — | entry signal |
| 2026-10-29T21:01 | Agent (ML meta-label) | sell | XRP-USD | 2.44 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-29T21:01 | Agent (ML meta-label) | sell | SOL-USD | 6.95 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-29T21:00 | Agent (ML meta-label) | buy | XRP-USD | 2.45 | — | entry |
| 2026-10-29T21:00 | Agent (ML meta-label) | buy | SOL-USD | 6.99 | — | entry |
| 2026-10-29T21:00 | Supertrend · 1h | sell | SOL-USD | 2.96 | -0.22 | exit signal |
| 2026-10-29T21:00 | Supertrend · 1h | sell | ETH-USD | 4.76 | -0.27 | exit signal |
| 2026-10-29T21:00 | Supertrend · 1h | sell | DOGE-USD | 4.68 | -0.35 | exit signal |
| 2026-10-29T21:00 | Supertrend · 1h | sell | BTC-USD | 5.86 | -0.23 | exit signal |
| 2026-10-29T20:45 | VWAP momentum · 1h | sell | DOGE-USD | 11.92 | -0.66 | stop-loss |
| 2026-10-29T20:45 | VWAP momentum · 1h | sell | BTC-USD | 12.18 | -0.36 | stop-loss |
| 2026-10-29T20:45 | MACD cross · 1h | sell | ETH-USD | 11.45 | -0.38 | stop-loss |
| 2026-10-29T20:40 | CCI reversion · 1h | sell | SOL-USD | 19.80 | -0.71 | stop-loss |
| 2026-10-29T20:40 | ROC + volume · 1h | sell | BTC-USD | 6.18 | -0.04 | stop-loss |
| 2026-10-29T20:35 | Agent (ML meta-label) | sell | DOGE-USD | 9.44 | -0.32 | selected signal exited |
| 2026-10-29T20:35 | OBV trend · 1h | sell | DOGE-USD | 7.14 | -0.20 | stop-loss |
| 2026-10-29T20:35 | OBV trend · 1h | sell | BTC-USD | 8.75 | -0.19 | stop-loss |
| 2026-10-29T20:35 | RSI momentum · 1h | sell | BTC-USD | 5.88 | -0.17 | stop-loss |
| 2026-10-29T20:35 | ROC + volume · 1h | buy | BTC-USD | 6.22 | — | entry |
| 2026-10-29T20:35 | ROC + volume · 1h | sell | DOGE-USD | 6.22 | -0.18 | stop-loss |
| 2026-10-29T20:35 | Parabolic SAR · 1h | sell | ETH-USD | 17.91 | -0.42 | stop-loss |
| 2026-10-29T20:35 | Parabolic SAR · 1h | sell | BTC-USD | 17.93 | -0.35 | stop-loss |
| 2026-10-29T20:35 | MACD cross · 1h | buy | ETH-USD | 5.91 | — | rebalance up |
| 2026-10-29T20:35 | MACD cross · 1h | sell | DOGE-USD | 5.88 | -0.16 | stop-loss |
| 2026-10-29T20:35 | MACD cross · 1h | sell | BTC-USD | 5.41 | -0.13 | stop-loss |
| 2026-10-29T20:35 | Triple EMA stack · 1h | sell | BTC-USD | 9.03 | -0.14 | stop-loss |
| 2026-10-29T20:35 | EMA 20/50 cross · 1h | sell | DOGE-USD | 16.23 | -0.45 | stop-loss |
| 2026-10-29T20:35 | EMA 20/50 cross · 1h | sell | BTC-USD | 16.21 | -0.30 | stop-loss |
| 2026-10-29T20:05 | CCI reversion · 1h | sell | XRP-USD | 20.03 | -0.64 | stop-loss |
| 2026-10-29T20:05 | Z-score reversion · 1h | sell | XRP-USD | 20.83 | -0.60 | stop-loss |
| 2026-10-29T20:05 | RSI(14) reversion · 1h | sell | XRP-USD | 19.82 | -0.57 | stop-loss |
| 2026-10-29T20:05 | RSI momentum · 1h | sell | DOGE-USD | 5.83 | -0.22 | stop-loss |
| 2026-10-29T20:05 | Parabolic SAR · 1h | buy | ETH-USD | 6.85 | — | rebalance up |
| 2026-10-29T20:05 | Parabolic SAR · 1h | buy | BTC-USD | 6.80 | — | rebalance up |
| 2026-10-29T20:05 | Parabolic SAR · 1h | sell | DOGE-USD | 11.14 | -0.34 | stop-loss |
| 2026-10-29T20:05 | MACD zero-line · 1h | sell | ETH-USD | 19.64 | -0.37 | stop-loss |
| 2026-10-29T20:05 | MACD cross · 1h | sell | SOL-USD | 5.78 | -0.14 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-31 23:45:05.000128+00:00 -> 2026-10-29 23:55:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
