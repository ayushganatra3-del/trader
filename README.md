# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T16:10:05.000105+00:00 · 73224 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.56 (-22.43%)

Closed trades 246, win rate 35.8%, fees £6.75, max drawdown -22.79%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 26.36 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 18918 decisions in 2496 calls, $0.2472 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T16:10 | 1 / 5 / 24 | cash |  |
| Breezy | 2026-11-25T16:10 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-25T16:10 | 3 / 20 / 7 | BITX 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| Bollinger reversion · 1h | ETH-USD | 1.78 | +4.64% | 7 |
| RSI(14) reversion · 1h | ETH-USD | 1.77 | +5.50% | 3 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.66 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.18 | 16.18 | 0 | — | 13.93 | 4.85 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 6.15 | 1.17 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.65 | 2.65 | 0 | — | 2.49 | 0.82 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.50 | -1.50 | 220 | 31.4 | -0.40 | -0.04 | -8.58 | 212 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -3.98 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.80 | -5.20 | 231 | 28.6 | -2.18 | -0.66 | -6.92 | 170 |
| 12 | Trend pullback · 1h | trend | 94.32 | -5.68 | 116 | 24.1 | -3.82 | -1.53 | -9.95 | 36 |
| 13 | Three white soldiers · 1h | momentum | 92.57 | -7.43 | 21 | 9.5 | -6.32 | -6.83 | -6.44 | 19 |
| 14 | Hold SPY | benchmark | 92.08 | -7.92 | 0 | — | -9.18 | -2.27 | -11.71 | 1 |
| 15 | Copy: Insider buying | copy | 90.92 | -9.08 | 61 | 41.0 | -8.78 | -1.63 | -14.79 | 72 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 90.79 | -9.21 | 0 | — | -10.88 | -2.25 | -13.91 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Daily: Bullish score | daily | 88.43 | -11.57 | 20 | 20.0 | -10.26 | -2.21 | -19.56 | 14 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.19 | -2.97 | -20.94 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 87.18 | -12.82 | 0 | — | -14.17 | -3.00 | -17.03 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.84 | -2.38 | -20.49 | 156 |
| 22 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -20.31 | -7.27 | -20.31 | 74 |
| 23 | Opening range 30m | breakout | 83.14 | -16.86 | 478 | 32.4 | -14.99 | -4.87 | -15.03 | 532 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.91 | -13.02 | 61 |
| 26 | Agent | meta | 77.56 | -22.43 | 246 | 35.8 | -26.37 | -5.97 | -26.56 | 195 |
| 27 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -14.67 | -4.12 | -17.05 | 85 |
| 28 | Parabolic SAR · 1h | trend | 76.68 | -23.32 | 209 | 27.8 | -35.17 | -8.71 | -35.55 | 179 |
| 29 | Volume breakout · 1h | breakout | 76.66 | -23.34 | 170 | 28.2 | -22.72 | -9.69 | -22.72 | 68 |
| 30 | Keltner breakout · 1h | breakout | 75.00 | -25.00 | 140 | 25.0 | -25.82 | -6.56 | -26.16 | 144 |
| 31 | Opening range 15m | breakout | 74.74 | -25.26 | 601 | 30.3 | -24.37 | -7.44 | -24.56 | 665 |
| 32 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -30.62 | -8.24 | -30.63 | 79 |
| 33 | Ichimoku · 1h | trend | 73.10 | -26.91 | 113 | 15.9 | -31.12 | -7.96 | -31.55 | 102 |
| 34 | Daily: Momentum burst | daily | 69.51 | -30.49 | 31 | 16.1 | -34.21 | -4.98 | -36.38 | 25 |
| 35 | ADX DI cross · 1h | trend | 69.37 | -30.63 | 264 | 18.9 | -38.55 | -7.34 | -38.90 | 286 |
| 36 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -31.34 | -8.17 | -31.76 | 202 |
| 37 | EMA 20/50 cross · 1h | trend | 67.93 | -32.07 | 126 | 9.5 | -38.28 | -10.59 | -39.42 | 112 |
| 38 | Max aggression: 5-day momentum | meta | 67.80 | -32.20 | 27 | 37.0 | -60.55 | -3.73 | -67.33 | 23 |
| 39 | Hold BTC | benchmark | 67.76 | -32.24 | 3 | 0.0 | -31.12 | -5.57 | -36.10 | 1 |
| 40 | OBV trend · 1h | momentum | 67.35 | -32.65 | 324 | 19.8 | -38.63 | -9.46 | -40.33 | 225 |
| 41 | Triple EMA stack · 1h | trend | 66.63 | -33.37 | 171 | 15.2 | -40.67 | -10.37 | -41.28 | 170 |
| 42 | Supertrend · 1h | trend | 65.98 | -34.02 | 221 | 17.6 | -40.66 | -7.85 | -41.29 | 209 |
| 43 | Copy: Cathie Wood (ARKK) | copy | 64.44 | -35.56 | 3 | 0.0 | -30.04 | -3.87 | -33.66 | 1 |
| 44 | MACD zero-line · 1h | trend | 63.17 | -36.83 | 201 | 16.4 | -35.36 | -9.68 | -35.53 | 198 |
| 45 | RSI momentum · 1h | momentum | 62.56 | -37.44 | 202 | 14.9 | -43.30 | -9.72 | -43.48 | 190 |
| 46 | Heikin-Ashi · 1h | trend | 62.09 | -37.91 | 546 | 22.0 | -49.71 | -10.33 | -50.31 | 624 |
| 47 | Stochastic reversion · 1h | reversion | 62.00 | -38.00 | 410 | 39.8 | -38.58 | -4.27 | -42.70 | 435 |
| 48 | ROC + volume · 1h | momentum | 60.60 | -39.40 | 461 | 26.9 | -41.52 | -8.20 | -41.70 | 334 |
| 49 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -57.52 | -4.35 | -60.94 | 38 |
| 50 | Donchian 20/10 · 1h | breakout | 59.83 | -40.17 | 183 | 17.5 | -43.41 | -9.66 | -43.50 | 193 |
| 51 | MFI reversion · 1h | reversion | 59.65 | -40.35 | 512 | 32.0 | -35.98 | -5.35 | -37.67 | 189 |
| 52 | EMA 9/21 cross · 1h | trend | 57.43 | -42.57 | 313 | 12.1 | -46.91 | -10.78 | -47.19 | 324 |
| 53 | Agent (ML meta-label) | meta | 57.38 | -42.62 | 2073 | 25.4 | -25.18 | -3.08 | -32.59 | 318 |
| 54 | MACD cross · 1h | trend | 55.56 | -44.44 | 490 | 20.4 | -55.52 | -11.08 | -55.71 | 497 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -55.27 | -9.15 | -55.30 | 495 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -43.45 | -5.28 | -45.50 | 432 |
| 57 | VWAP momentum · 1h | momentum | 51.10 | -48.90 | 1085 | 21.5 | -60.79 | -13.33 | -61.82 | 1174 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -58.41 | -9.14 | -58.69 | 693 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -58.69 | -9.73 | -59.48 | 592 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.20 | -50.29 | -99.20 | 5410 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.14 | -33.95 | -84.30 | 1405 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.42 | -49.38 | -94.42 | 2408 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.02 | -33.09 | -91.19 | 1891 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.74 | -42.18 | -91.75 | 2207 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.10 | -27.87 | -89.20 | 1931 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.25 | -50.05 | -98.25 | 3416 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -54.06 | -96.89 | 3337 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.74 | -34.84 | -92.74 | 2038 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.47 | -35.66 | -82.57 | 1511 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -57.48 | -99.70 | 6304 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.31 | -39.03 | -93.34 | 2470 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.03 | -35.31 | -94.05 | 3128 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -70.63 | -99.83 | 6115 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.30 | -44.90 | -93.30 | 2249 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -52.45 | -22.87 | -52.47 | 653 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.55 | -24.06 | -78.66 | 1613 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -59.18 | -97.75 | 3243 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.23 | -64.18 | -99.23 | 5163 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.44 | -27.38 | -71.44 | 1192 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.84 | -49.00 | -94.87 | 2640 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -50.54 | -7.09 | -51.22 | 282 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.67 | -36.11 | -84.93 | 1635 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.78 | -77.22 | -99.78 | 6549 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -92.03 | -31.90 | -92.03 | 2519 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.56 | -20.56 | -83.56 | 1972 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.20 | -34.92 | -92.28 | 2177 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -50.25 | -98.23 | 4100 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.58 | -48.02 | -90.64 | 2192 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.88 | -29.37 | -67.90 | 778 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -28.46 | -73.52 | 1145 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.95 | -19.65 | -85.20 | 1835 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.14 | -51.63 | -98.14 | 4430 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -110.13 | -99.94 | 8250 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -50.43 | -7.61 | -53.62 | 297 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T16:10 | Opening range 15m | sell | GOOGL | 18.54 | -0.16 | exit signal |
| 2026-11-25T16:00 | Agent (rotation) | sell | SQQQ | 31.57 | -0.01 | rebalance down |
| 2026-11-25T16:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 109.27 | -0.10 | target is flat |
| 2026-11-25T16:00 | MFI reversion · 1h | buy | SOL-USD | 3.18 | — | entry signal |
| 2026-11-25T16:00 | MFI reversion · 1h | buy | BTC-USD | 11.96 | — | entry signal |
| 2026-11-25T16:00 | MACD cross · 1h | buy | ETH-USD | 4.55 | — | entry signal |
| 2026-11-25T16:00 | MACD cross · 1h | sell | AAPL | 4.55 | -0.05 | rebalance down |
| 2026-11-25T15:55 | Opening range 30m | buy | ETHU | 20.83 | — | entry signal |
| 2026-11-25T15:40 | Opening range 15m | sell | NVDA | 18.54 | -0.24 | exit signal |
| 2026-11-25T15:35 | MACD cross · 1h | buy | SQQQ | 3.01 | — | rebalance up |
| 2026-11-25T15:35 | MACD cross · 1h | sell | LABU | 3.01 | 0.13 | rebalance down |
| 2026-11-25T15:35 | Opening range 30m | buy | BITX | 20.81 | — | entry signal |
| 2026-11-25T15:35 | Opening range 15m | buy | BITX | 18.49 | — | entry signal |
| 2026-11-25T15:30 | Agent (rotation) | buy | SQQQ | 31.57 | — | rebalance up |
| 2026-11-25T15:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 109.37 | — | entry |
| 2026-11-25T15:30 | Stochastic reversion · 1h | buy | MSTR | 9.32 | — | entry signal |
| 2026-11-25T15:30 | Stochastic reversion · 1h | buy | COIN | 12.33 | — | entry signal |
| 2026-11-25T15:30 | Stochastic reversion · 1h | sell | SQQQ | 15.17 | 1.38 | exit signal |
| 2026-11-25T15:30 | Stochastic reversion · 1h | sell | ETHU | 3.34 | -0.28 | rebalance down |
| 2026-11-25T15:30 | Stochastic reversion · 1h | sell | DOGE-USD | 3.14 | 0.01 | rebalance down |
| 2026-11-25T15:30 | Keltner breakout · 1h | buy | SQQQ | 18.72 | — | entry signal |
| 2026-11-25T15:30 | RSI momentum · 1h | buy | SQQQ | 15.60 | — | entry signal |
| 2026-11-25T15:30 | ROC + volume · 1h | buy | SQQQ | 15.11 | — | entry signal |
| 2026-11-25T15:30 | ROC + volume · 1h | buy | LABU | 15.11 | — | entry signal |
| 2026-11-25T15:30 | VWAP momentum · 1h | buy | SQQQ | 12.76 | — | entry signal |
| 2026-11-25T15:30 | VWAP momentum · 1h | sell | LABU | 12.46 | -0.61 | exit signal |
| 2026-11-25T15:30 | Heikin-Ashi · 1h | sell | LABU | 14.76 | -0.55 | exit signal |
| 2026-11-25T15:30 | ADX DI cross · 1h | sell | TNA | 17.48 | -0.26 | exit signal |
| 2026-11-25T15:30 | ADX DI cross · 1h | sell | IWM | 17.33 | -0.06 | exit signal |
| 2026-11-25T15:30 | Parabolic SAR · 1h | buy | SQQQ | 19.15 | — | entry signal |
| 2026-11-25T15:30 | Parabolic SAR · 1h | sell | AAPL | 19.73 | -0.19 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | buy | TNA | 10.25 | — | rebalance up |
| 2026-11-25T15:30 | Supertrend · 1h | buy | SQQQ | 13.18 | — | entry signal |
| 2026-11-25T15:30 | Supertrend · 1h | buy | META | 10.25 | — | rebalance up |
| 2026-11-25T15:30 | Supertrend · 1h | buy | IWM | 10.20 | — | rebalance up |
| 2026-11-25T15:30 | Supertrend · 1h | buy | AAPL | 9.81 | — | rebalance up |
| 2026-11-25T15:30 | Supertrend · 1h | sell | UPRO | 2.56 | -0.33 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | TSLA | 2.80 | -0.23 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | TQQQ | 2.43 | -0.60 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | TECL | 2.24 | -0.79 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 16:10:05.000105+00:00 -> 2026-11-25 16:20:05.000105+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
