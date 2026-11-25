# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T15:40:05.000103+00:00 · 73205 ticks

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

Today: 17202 decisions in 2439 calls, $0.2271 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T15:40 | 1 / 11 / 18 | cash |  |
| Breezy | 2026-11-25T15:40 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-25T15:40 | 4 / 23 / 3 | BITX 75% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.62 | 15.62 | 0 | — | 13.17 | 4.66 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 108.94 | 8.95 | 41 | 43.9 | 6.81 | 1.28 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.86 | 2.86 | 0 | — | 2.98 | 0.88 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.28 | -1.72 | 220 | 31.4 | -0.63 | -0.11 | -8.58 | 212 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -3.98 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 231 | 28.6 | -2.72 | -0.84 | -7.61 | 137 |
| 12 | Trend pullback · 1h | trend | 94.08 | -5.92 | 116 | 24.1 | -4.71 | -1.88 | -10.58 | 38 |
| 13 | Three white soldiers · 1h | momentum | 92.57 | -7.43 | 21 | 9.5 | -6.32 | -6.83 | -6.44 | 19 |
| 14 | Hold SPY | benchmark | 92.28 | -7.72 | 0 | — | -8.89 | -2.23 | -11.71 | 1 |
| 15 | Copy: Insider buying | copy | 90.85 | -9.15 | 61 | 41.0 | -8.89 | -1.65 | -14.79 | 72 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 90.79 | -9.21 | 0 | — | -10.88 | -2.25 | -13.91 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Daily: Bullish score | daily | 88.21 | -11.79 | 20 | 20.0 | -10.57 | -2.27 | -19.56 | 14 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.22 | -2.97 | -20.94 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 86.77 | -13.23 | 0 | — | -14.57 | -3.06 | -17.03 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.84 | -2.38 | -20.49 | 156 |
| 22 | Opening range 30m | breakout | 83.27 | -16.73 | 478 | 32.4 | -14.86 | -4.86 | -14.94 | 531 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.13 | -7.32 | -21.45 | 77 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.91 | -13.02 | 61 |
| 26 | Agent | meta | 77.56 | -22.43 | 246 | 35.8 | -26.35 | -5.97 | -26.54 | 196 |
| 27 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.51 | -4.32 | -18.81 | 87 |
| 28 | Volume breakout · 1h | breakout | 76.66 | -23.34 | 170 | 28.2 | -23.19 | -9.82 | -23.19 | 69 |
| 29 | Parabolic SAR · 1h | trend | 76.50 | -23.50 | 209 | 27.8 | -35.30 | -8.71 | -35.53 | 179 |
| 30 | Keltner breakout · 1h | breakout | 74.83 | -25.17 | 140 | 25.0 | -27.43 | -7.01 | -27.94 | 149 |
| 31 | Opening range 15m | breakout | 74.81 | -25.19 | 600 | 30.3 | -24.29 | -7.43 | -24.61 | 665 |
| 32 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -30.59 | -8.23 | -30.60 | 79 |
| 33 | Ichimoku · 1h | trend | 73.50 | -26.50 | 113 | 15.9 | -30.72 | -7.88 | -31.53 | 102 |
| 34 | Daily: Momentum burst | daily | 69.89 | -30.11 | 31 | 16.1 | -34.02 | -4.91 | -36.38 | 25 |
| 35 | ADX DI cross · 1h | trend | 69.60 | -30.40 | 264 | 18.9 | -38.36 | -7.30 | -38.90 | 286 |
| 36 | Max aggression: 5-day momentum | meta | 69.33 | -30.67 | 27 | 37.0 | -59.66 | -3.57 | -67.33 | 23 |
| 37 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -31.71 | -8.30 | -32.18 | 203 |
| 38 | EMA 20/50 cross · 1h | trend | 67.76 | -32.24 | 126 | 9.5 | -38.47 | -10.67 | -39.42 | 112 |
| 39 | Hold BTC | benchmark | 67.64 | -32.36 | 3 | 0.0 | -31.31 | -5.59 | -36.10 | 1 |
| 40 | OBV trend · 1h | momentum | 67.20 | -32.80 | 324 | 19.8 | -38.72 | -9.54 | -40.29 | 225 |
| 41 | Triple EMA stack · 1h | trend | 66.48 | -33.52 | 171 | 15.2 | -40.87 | -10.40 | -41.28 | 170 |
| 42 | Supertrend · 1h | trend | 66.07 | -33.93 | 221 | 17.6 | -40.59 | -7.85 | -41.29 | 209 |
| 43 | Copy: Cathie Wood (ARKK) | copy | 64.40 | -35.60 | 3 | 0.0 | -29.76 | -3.88 | -33.66 | 1 |
| 44 | MACD zero-line · 1h | trend | 63.20 | -36.80 | 201 | 16.4 | -35.36 | -9.69 | -35.50 | 198 |
| 45 | RSI momentum · 1h | momentum | 62.78 | -37.22 | 202 | 14.9 | -42.98 | -9.69 | -43.44 | 190 |
| 46 | Stochastic reversion · 1h | reversion | 62.11 | -37.89 | 410 | 39.8 | -38.18 | -4.21 | -42.70 | 438 |
| 47 | Heikin-Ashi · 1h | trend | 62.09 | -37.91 | 546 | 22.0 | -49.63 | -10.30 | -50.29 | 624 |
| 48 | ROC + volume · 1h | momentum | 60.81 | -39.20 | 461 | 26.9 | -42.15 | -8.35 | -42.64 | 337 |
| 49 | Donchian 20/10 · 1h | breakout | 60.18 | -39.82 | 183 | 17.5 | -43.11 | -9.65 | -43.75 | 194 |
| 50 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -57.91 | -4.39 | -60.94 | 38 |
| 51 | MFI reversion · 1h | reversion | 59.87 | -40.13 | 512 | 32.0 | -35.02 | -5.13 | -37.84 | 187 |
| 52 | EMA 9/21 cross · 1h | trend | 57.60 | -42.40 | 313 | 12.1 | -46.74 | -10.81 | -47.21 | 324 |
| 53 | Agent (ML meta-label) | meta | 57.19 | -42.80 | 2073 | 25.4 | -25.41 | -2.98 | -33.65 | 325 |
| 54 | MACD cross · 1h | trend | 55.92 | -44.08 | 490 | 20.4 | -55.21 | -11.09 | -55.69 | 496 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -55.12 | -9.14 | -55.15 | 492 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -43.56 | -5.29 | -45.50 | 432 |
| 57 | VWAP momentum · 1h | momentum | 50.98 | -49.02 | 1085 | 21.5 | -61.36 | -13.19 | -62.28 | 1174 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -57.83 | -8.97 | -58.05 | 686 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -58.78 | -9.73 | -59.48 | 592 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.19 | -50.24 | -99.19 | 5407 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.14 | -33.92 | -84.28 | 1405 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.51 | -49.34 | -94.51 | 2413 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.07 | -33.10 | -91.19 | 1893 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.87 | -42.08 | -91.87 | 2209 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.17 | -27.85 | -89.26 | 1930 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.25 | -50.03 | -98.25 | 3414 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -53.84 | -96.89 | 3329 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.82 | -35.29 | -92.82 | 2043 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.47 | -35.94 | -82.53 | 1510 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -57.56 | -99.70 | 6308 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.31 | -39.03 | -93.34 | 2470 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.04 | -35.35 | -94.06 | 3129 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -70.59 | -99.83 | 6115 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.29 | -44.82 | -93.29 | 2251 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -52.45 | -22.87 | -52.47 | 653 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.56 | -24.05 | -78.62 | 1599 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -58.93 | -97.75 | 3245 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.22 | -64.13 | -99.23 | 5162 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.41 | -27.43 | -71.42 | 1193 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.84 | -49.00 | -94.87 | 2640 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -50.39 | -7.09 | -51.22 | 282 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.73 | -36.14 | -84.96 | 1636 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -77.08 | -99.78 | 6548 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.97 | -32.00 | -92.02 | 2518 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.36 | -20.56 | -83.47 | 1971 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.13 | -34.91 | -92.25 | 2177 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -50.33 | -98.22 | 4100 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.67 | -48.02 | -90.67 | 2207 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.95 | -29.43 | -67.96 | 774 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.49 | -28.48 | -73.49 | 1151 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.87 | -19.64 | -85.18 | 1834 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.12 | -51.49 | -98.14 | 4430 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.92 | -99.94 | 8258 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -50.74 | -7.70 | -53.62 | 290 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-25T15:30 | Supertrend · 1h | sell | SPY | 2.91 | -0.12 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | QQQ | 2.82 | -0.21 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | PLTR | 2.89 | -0.14 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | NVDA | 2.55 | -0.48 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | MSFT | 2.88 | -0.15 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | LABU | 3.31 | 0.28 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | GOOGL | 2.85 | -0.18 | exit signal |
| 2026-11-25T15:30 | Supertrend · 1h | sell | ETHU | 2.52 | -0.51 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 15:40:05.000103+00:00 -> 2026-11-25 15:50:05.000103+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
