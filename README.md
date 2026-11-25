# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T16:40:05.000130+00:00 · 73243 ticks

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

Today: 20640 decisions in 2553 calls, $0.2673 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T16:40 | 8 / 18 / 4 | cash |  |
| Breezy | 2026-11-25T16:40 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-25T16:40 | 2 / 25 / 3 | MSTR 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| Bollinger reversion · 1h | ETH-USD | 1.78 | +4.64% | 7 |
| RSI(14) reversion · 1h | ETH-USD | 1.77 | +5.50% | 3 |
| MFI reversion | SQQQ | 1.70 | +11.40% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.16 | 3.61 | -5.42 | 29 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.14 | 16.14 | 0 | — | 13.91 | 4.85 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 6.79 | 1.27 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.26 | 3.26 | 0 | — | 2.84 | 0.99 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.33 | -1.67 | 220 | 31.4 | -0.64 | -0.11 | -8.58 | 212 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.67 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.74 | -5.26 | 231 | 28.6 | -1.98 | -0.59 | -7.29 | 154 |
| 12 | Trend pullback · 1h | trend | 94.14 | -5.86 | 116 | 24.1 | -3.97 | -1.63 | -9.95 | 36 |
| 13 | Three white soldiers · 1h | momentum | 92.57 | -7.43 | 21 | 9.5 | -6.32 | -6.83 | -6.44 | 19 |
| 14 | Hold SPY | benchmark | 92.14 | -7.86 | 0 | — | -8.83 | -2.25 | -11.71 | 1 |
| 15 | Copy: Insider buying | copy | 91.02 | -8.97 | 61 | 41.0 | -8.77 | -1.63 | -14.79 | 72 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 90.76 | -9.24 | 0 | — | -10.88 | -2.25 | -13.91 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Daily: Bullish score | daily | 88.26 | -11.74 | 20 | 20.0 | -11.03 | -2.25 | -19.56 | 14 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.12 | -2.97 | -20.94 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 86.91 | -13.09 | 0 | — | -14.36 | -3.06 | -17.03 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.76 | -2.37 | -20.49 | 156 |
| 22 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -17.35 | -6.41 | -17.35 | 71 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 24 | Opening range 30m | breakout | 82.72 | -17.28 | 478 | 32.4 | -15.41 | -4.92 | -15.44 | 532 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.91 | -13.02 | 61 |
| 26 | Agent | meta | 77.56 | -22.43 | 246 | 35.8 | -26.70 | -6.08 | -26.89 | 196 |
| 27 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.09 | -4.19 | -18.44 | 88 |
| 28 | Volume breakout · 1h | breakout | 76.66 | -23.34 | 170 | 28.2 | -22.70 | -9.67 | -22.70 | 68 |
| 29 | Parabolic SAR · 1h | trend | 76.55 | -23.45 | 209 | 27.8 | -35.25 | -8.71 | -35.53 | 179 |
| 30 | Keltner breakout · 1h | breakout | 74.87 | -25.13 | 140 | 25.0 | -26.94 | -6.86 | -27.15 | 147 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.44 | -7.82 | -29.45 | 74 |
| 32 | Opening range 15m | breakout | 74.33 | -25.66 | 601 | 30.3 | -24.76 | -7.46 | -24.76 | 666 |
| 33 | Ichimoku · 1h | trend | 72.93 | -27.07 | 113 | 15.9 | -31.42 | -7.99 | -31.69 | 102 |
| 34 | Daily: Momentum burst | daily | 69.30 | -30.70 | 31 | 16.1 | -35.24 | -5.02 | -36.38 | 25 |
| 35 | ADX DI cross · 1h | trend | 69.03 | -30.97 | 264 | 18.9 | -39.15 | -7.56 | -39.20 | 273 |
| 36 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -31.88 | -8.34 | -32.29 | 203 |
| 37 | EMA 20/50 cross · 1h | trend | 67.80 | -32.20 | 126 | 9.5 | -36.62 | -10.27 | -37.69 | 111 |
| 38 | Hold BTC | benchmark | 67.70 | -32.30 | 3 | 0.0 | -30.90 | -5.57 | -36.10 | 1 |
| 39 | OBV trend · 1h | momentum | 67.24 | -32.76 | 324 | 19.8 | -38.85 | -9.51 | -40.45 | 225 |
| 40 | Max aggression: 5-day momentum | meta | 66.96 | -33.04 | 27 | 37.0 | -61.03 | -3.81 | -67.33 | 23 |
| 41 | Triple EMA stack · 1h | trend | 66.51 | -33.49 | 171 | 15.2 | -40.81 | -10.51 | -41.33 | 168 |
| 42 | Supertrend · 1h | trend | 66.02 | -33.98 | 221 | 17.6 | -39.79 | -7.57 | -40.48 | 213 |
| 43 | Copy: Cathie Wood (ARKK) | copy | 64.71 | -35.29 | 3 | 0.0 | -29.69 | -3.84 | -33.66 | 1 |
| 44 | MACD zero-line · 1h | trend | 63.27 | -36.73 | 202 | 16.3 | -35.42 | -9.79 | -35.70 | 201 |
| 45 | RSI momentum · 1h | momentum | 62.26 | -37.74 | 202 | 14.9 | -43.82 | -9.79 | -43.82 | 191 |
| 46 | Heikin-Ashi · 1h | trend | 62.14 | -37.86 | 546 | 22.0 | -49.48 | -10.31 | -50.13 | 623 |
| 47 | Stochastic reversion · 1h | reversion | 61.91 | -38.09 | 410 | 39.8 | -39.38 | -4.40 | -43.45 | 437 |
| 48 | ROC + volume · 1h | momentum | 60.31 | -39.69 | 461 | 26.9 | -41.87 | -8.31 | -41.96 | 334 |
| 49 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -57.80 | -4.38 | -60.94 | 38 |
| 50 | Donchian 20/10 · 1h | breakout | 59.64 | -40.36 | 183 | 17.5 | -43.37 | -9.59 | -43.37 | 193 |
| 51 | MFI reversion · 1h | reversion | 59.49 | -40.51 | 512 | 32.0 | -36.03 | -5.34 | -37.67 | 190 |
| 52 | EMA 9/21 cross · 1h | trend | 57.28 | -42.72 | 313 | 12.1 | -47.11 | -10.77 | -47.22 | 324 |
| 53 | Agent (ML meta-label) | meta | 57.06 | -42.94 | 2073 | 25.4 | -21.39 | -2.72 | -28.82 | 326 |
| 54 | MACD cross · 1h | trend | 55.32 | -44.68 | 491 | 20.4 | -55.47 | -11.00 | -55.49 | 496 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -55.31 | -9.10 | -55.33 | 497 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -43.56 | -5.29 | -45.50 | 436 |
| 57 | VWAP momentum · 1h | momentum | 51.01 | -48.99 | 1085 | 21.5 | -60.90 | -13.35 | -61.86 | 1172 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -58.90 | -9.22 | -58.93 | 694 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -58.85 | -9.77 | -59.59 | 598 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.20 | -50.28 | -99.20 | 5430 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.23 | -34.14 | -84.40 | 1411 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.38 | -49.68 | -94.38 | 2395 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.05 | -33.11 | -91.19 | 1887 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.76 | -42.24 | -91.77 | 2206 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.05 | -27.83 | -89.15 | 1926 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.26 | -50.10 | -98.26 | 3421 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.83 | -53.80 | -96.84 | 3325 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.67 | -34.67 | -92.68 | 2025 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.52 | -35.97 | -82.55 | 1510 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.71 | -57.47 | -99.71 | 6325 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.35 | -39.17 | -93.39 | 2471 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.02 | -35.18 | -94.05 | 3128 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -70.60 | -99.83 | 6104 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.33 | -44.94 | -93.33 | 2248 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -52.45 | -22.87 | -52.47 | 653 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.64 | -24.12 | -78.75 | 1616 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -59.05 | -97.75 | 3235 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.23 | -64.17 | -99.23 | 5146 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.32 | -27.41 | -71.48 | 1193 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.86 | -49.00 | -94.86 | 2637 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -50.65 | -7.10 | -51.22 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.81 | -36.19 | -84.93 | 1635 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -77.17 | -99.78 | 6553 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.95 | -31.70 | -91.96 | 2515 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.45 | -20.53 | -83.54 | 1987 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.14 | -34.86 | -92.24 | 2169 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.22 | -50.31 | -98.23 | 4082 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.66 | -47.76 | -90.66 | 2185 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.84 | -29.33 | -67.85 | 785 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -28.46 | -73.52 | 1145 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.83 | -19.64 | -85.16 | 1844 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.12 | -51.57 | -98.13 | 4419 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -110.31 | -99.94 | 8256 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -48.99 | -7.25 | -52.66 | 294 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T16:30 | MFI reversion · 1h | buy | SOL-USD | 4.78 | — | rebalance up |
| 2026-11-25T16:30 | MFI reversion · 1h | buy | BITX | 9.99 | — | entry signal |
| 2026-11-25T16:30 | MFI reversion · 1h | sell | XRP-USD | 4.94 | -0.03 | rebalance down |
| 2026-11-25T16:30 | MFI reversion · 1h | sell | TNA | 4.94 | 0.03 | rebalance down |
| 2026-11-25T16:30 | MFI reversion · 1h | sell | IWM | 4.88 | 0.01 | rebalance down |
| 2026-11-25T16:30 | Stochastic reversion · 1h | buy | AMZN | 4.97 | — | entry signal |
| 2026-11-25T16:30 | Stochastic reversion · 1h | sell | MSFT | 4.97 | -0.08 | rebalance down |
| 2026-11-25T16:30 | Heikin-Ashi · 1h | buy | SQQQ | 15.52 | — | entry signal |
| 2026-11-25T16:30 | Ichimoku · 1h | buy | SQQQ | 18.29 | — | entry signal |
| 2026-11-25T16:30 | MACD zero-line · 1h | sell | AAPL | 15.91 | -0.11 | exit signal |
| 2026-11-25T16:30 | MACD cross · 1h | buy | ETH-USD | 6.60 | — | rebalance up |
| 2026-11-25T16:30 | MACD cross · 1h | sell | AAPL | 9.31 | -0.05 | exit signal |
| 2026-11-25T16:30 | Opening range 15m | buy | META | 18.74 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 16:40:05.000130+00:00 -> 2026-11-25 16:50:05.000130+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
