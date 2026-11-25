# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T15:11:05.000171+00:00 · 73176 ticks

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

Today: 14565 decisions in 2352 calls, $0.1962 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T15:11 | 0 / 8 / 22 | cash |  |
| Breezy | 2026-11-25T15:11 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-25T15:11 | 3 / 23 / 4 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.35 | 15.35 | 0 | — | 13.03 | 4.58 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.87 | 1.44 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.01 | 4.01 | 0 | — | 4.16 | 1.18 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.29 | -1.71 | 220 | 31.4 | -0.62 | -0.10 | -8.58 | 211 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -3.95 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.76 | -5.24 | 231 | 28.6 | -2.59 | -0.80 | -7.61 | 136 |
| 12 | Trend pullback · 1h | trend | 93.63 | -6.37 | 116 | 24.1 | -5.13 | -2.15 | -10.58 | 38 |
| 13 | Hold SPY | benchmark | 92.64 | -7.36 | 0 | — | -8.14 | -2.15 | -11.71 | 1 |
| 14 | Three white soldiers · 1h | momentum | 92.57 | -7.43 | 21 | 9.5 | -6.32 | -6.83 | -6.44 | 19 |
| 15 | Copy: Insider buying | copy | 91.40 | -8.60 | 61 | 41.0 | -8.21 | -1.52 | -14.79 | 72 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 90.76 | -9.24 | 0 | — | -10.88 | -2.25 | -13.91 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Daily: Bullish score | daily | 87.78 | -12.22 | 20 | 20.0 | -10.36 | -2.39 | -19.56 | 14 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.14 | -2.97 | -20.94 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 86.68 | -13.32 | 0 | — | -14.50 | -3.07 | -17.03 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.84 | -2.38 | -20.49 | 156 |
| 22 | Opening range 30m | breakout | 84.22 | -15.78 | 473 | 32.8 | -13.88 | -4.66 | -13.91 | 530 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -18.64 | -6.97 | -18.87 | 71 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.91 | -13.02 | 61 |
| 26 | Agent | meta | 77.56 | -22.43 | 246 | 35.8 | -26.82 | -6.11 | -27.00 | 197 |
| 27 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 28 | Volume breakout · 1h | breakout | 76.92 | -23.08 | 169 | 27.8 | -22.78 | -9.46 | -23.24 | 70 |
| 29 | Parabolic SAR · 1h | trend | 76.81 | -23.19 | 208 | 27.9 | -33.90 | -8.66 | -34.10 | 178 |
| 30 | Opening range 15m | breakout | 75.66 | -24.34 | 592 | 30.7 | -23.37 | -7.27 | -23.38 | 664 |
| 31 | Keltner breakout · 1h | breakout | 74.90 | -25.10 | 140 | 25.0 | -27.77 | -7.08 | -27.97 | 150 |
| 32 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -30.86 | -8.29 | -30.87 | 82 |
| 33 | Ichimoku · 1h | trend | 73.42 | -26.58 | 113 | 15.9 | -30.82 | -7.90 | -31.55 | 102 |
| 34 | Daily: Momentum burst | daily | 69.82 | -30.18 | 31 | 16.1 | -33.65 | -4.93 | -36.38 | 25 |
| 35 | ADX DI cross · 1h | trend | 69.39 | -30.61 | 262 | 19.1 | -39.20 | -7.55 | -39.75 | 270 |
| 36 | Max aggression: 5-day momentum | meta | 69.03 | -30.97 | 27 | 37.0 | -59.82 | -3.60 | -67.33 | 23 |
| 37 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -32.90 | -8.66 | -33.51 | 207 |
| 38 | EMA 20/50 cross · 1h | trend | 67.42 | -32.58 | 126 | 9.5 | -37.34 | -10.52 | -38.03 | 112 |
| 39 | Hold BTC | benchmark | 67.20 | -32.80 | 3 | 0.0 | -31.43 | -5.65 | -36.10 | 1 |
| 40 | OBV trend · 1h | momentum | 66.90 | -33.10 | 324 | 19.8 | -39.03 | -9.68 | -40.33 | 227 |
| 41 | Triple EMA stack · 1h | trend | 66.54 | -33.46 | 171 | 15.2 | -39.74 | -10.09 | -40.03 | 153 |
| 42 | Supertrend · 1h | trend | 66.49 | -33.51 | 207 | 18.4 | -38.16 | -7.25 | -39.47 | 213 |
| 43 | Copy: Cathie Wood (ARKK) | copy | 64.56 | -35.44 | 3 | 0.0 | -29.06 | -3.86 | -33.66 | 1 |
| 44 | MACD zero-line · 1h | trend | 63.38 | -36.62 | 201 | 16.4 | -34.82 | -9.55 | -35.06 | 198 |
| 45 | RSI momentum · 1h | momentum | 62.77 | -37.23 | 202 | 14.9 | -43.37 | -9.83 | -43.81 | 192 |
| 46 | Heikin-Ashi · 1h | trend | 62.45 | -37.55 | 545 | 21.8 | -49.40 | -10.26 | -50.30 | 624 |
| 47 | Stochastic reversion · 1h | reversion | 61.66 | -38.34 | 409 | 39.6 | -39.59 | -4.42 | -43.52 | 437 |
| 48 | ROC + volume · 1h | momentum | 60.60 | -39.40 | 460 | 27.0 | -42.58 | -8.44 | -42.80 | 337 |
| 49 | Donchian 20/10 · 1h | breakout | 60.11 | -39.89 | 183 | 17.5 | -43.07 | -9.63 | -43.63 | 195 |
| 50 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -58.64 | -4.45 | -60.94 | 38 |
| 51 | MFI reversion · 1h | reversion | 59.76 | -40.24 | 512 | 32.0 | -35.90 | -5.32 | -37.72 | 187 |
| 52 | EMA 9/21 cross · 1h | trend | 57.77 | -42.23 | 313 | 12.1 | -46.79 | -10.88 | -47.42 | 324 |
| 53 | Agent (ML meta-label) | meta | 56.82 | -43.18 | 2073 | 25.4 | -17.99 | -2.07 | -27.05 | 307 |
| 54 | MACD cross · 1h | trend | 55.95 | -44.05 | 490 | 20.4 | -54.49 | -10.93 | -55.13 | 500 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -55.48 | -9.31 | -55.50 | 497 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -43.50 | -5.25 | -45.43 | 432 |
| 57 | VWAP momentum · 1h | momentum | 51.34 | -48.66 | 1084 | 21.4 | -61.09 | -13.30 | -62.16 | 1175 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -59.13 | -9.38 | -59.13 | 669 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -58.81 | -9.67 | -59.54 | 599 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -49.96 | -99.18 | 5404 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.00 | -33.64 | -84.16 | 1408 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.47 | -49.27 | -94.47 | 2403 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.16 | -33.20 | -91.16 | 1894 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.87 | -42.08 | -91.87 | 2217 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.24 | -27.91 | -89.33 | 1939 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.24 | -50.00 | -98.25 | 3412 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.90 | -53.80 | -96.90 | 3354 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.80 | -35.24 | -92.83 | 2028 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.53 | -36.17 | -82.53 | 1509 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -57.60 | -99.70 | 6308 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.35 | -39.03 | -93.35 | 2474 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.04 | -35.36 | -94.06 | 3130 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -70.55 | -99.83 | 6109 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.25 | -44.80 | -93.26 | 2247 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -52.26 | -22.85 | -52.27 | 652 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.77 | -24.00 | -78.77 | 1597 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -59.06 | -97.75 | 3248 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -64.00 | -99.22 | 5163 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.48 | -27.38 | -71.48 | 1193 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.88 | -49.00 | -94.88 | 2648 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -50.50 | -7.09 | -51.20 | 282 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.96 | -36.14 | -85.05 | 1639 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.97 | -99.78 | 6545 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.91 | -32.06 | -91.91 | 2509 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.20 | -20.49 | -83.28 | 1966 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.14 | -34.87 | -92.28 | 2175 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.19 | -50.25 | -98.22 | 4100 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.58 | -48.15 | -90.58 | 2187 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.95 | -29.43 | -67.96 | 774 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.54 | -28.45 | -73.54 | 1151 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.97 | -19.65 | -85.19 | 1830 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.11 | -51.27 | -98.14 | 4430 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -108.32 | -99.94 | 8260 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -52.48 | -8.33 | -53.30 | 281 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T15:10 | Bollinger reversion · 1h | sell | XRP-USD | 13.02 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-25T15:10 | Bollinger reversion · 1h | sell | SOL-USD | 13.02 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-25T15:10 | Bollinger reversion · 1h | sell | DOGE-USD | 13.05 | -0.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-25T15:10 | Bollinger reversion · 1h | sell | BTC-USD | 13.04 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-25T15:05 | Opening range 30m | buy | UPRO | 17.08 | — | entry signal |
| 2026-11-25T15:05 | Opening range 30m | buy | SPY | 17.08 | — | entry signal |
| 2026-11-25T15:05 | Opening range 30m | buy | PLTR | 17.08 | — | entry signal |
| 2026-11-25T15:05 | Opening range 30m | buy | ETHU | 17.08 | — | entry signal |
| 2026-11-25T15:05 | Opening range 30m | buy | BITX | 17.08 | — | entry signal |
| 2026-11-25T15:00 | Agent (rotation) | sell | SQQQ | 31.14 | -1.24 | selected signal exited |
| 2026-11-25T15:00 | Day trade: Stocks in Play ORB | sell | SQQQ | 23.25 | -0.70 | target is flat |
| 2026-11-25T15:00 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 123.12 | -5.21 | target is flat |
| 2026-11-25T15:00 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 101.22 | -2.69 | target is flat |
| 2026-11-25T15:00 | MFI reversion · 1h | buy | XRP-USD | 14.97 | — | entry signal |
| 2026-11-25T15:00 | MFI reversion · 1h | sell | ETHU | 15.27 | 0.42 | target is flat |
| 2026-11-25T15:00 | Bollinger reversion · 1h | buy | XRP-USD | 13.18 | — | entry signal |
| 2026-11-25T15:00 | Bollinger reversion · 1h | buy | SOL-USD | 13.18 | — | entry signal |
| 2026-11-25T15:00 | Bollinger reversion · 1h | buy | DOGE-USD | 13.18 | — | entry signal |
| 2026-11-25T15:00 | Bollinger reversion · 1h | buy | BTC-USD | 13.18 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | buy | TQQQ | 7.68 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | buy | TECL | 7.69 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | buy | SOXL | 7.69 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | buy | QQQ | 7.69 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | buy | PLTR | 7.69 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | buy | NVDA | 7.69 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | buy | META | 7.69 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | buy | ETHU | 7.69 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | buy | AMD | 7.69 | — | entry signal |
| 2026-11-25T15:00 | Opening range 15m | sell | GOOGL | 11.63 | 0.08 | rebalance down |
| 2026-11-25T14:55 | Agent (rotation) | sell | SQQQ | 7.48 | -0.14 | rebalance down |
| 2026-11-25T14:55 | Stochastic reversion · 1h | buy | SQQQ | 2.82 | — | rebalance up |
| 2026-11-25T14:55 | Opening range 15m | buy | GOOGL | 19.18 | — | entry signal |
| 2026-11-25T14:55 | Gap and go | sell | SQQQ | 24.41 | -0.22 | exit signal |
| 2026-11-25T14:45 | Agent (rotation) | buy | SQQQ | 31.99 | — | rebalance up |
| 2026-11-25T14:45 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 128.32 | — | entry |
| 2026-11-25T14:45 | Agent | sell | ETH-USD | 15.13 | -0.48 | selected signal exited |
| 2026-11-25T14:45 | CCI reversion · 1h | sell | PLTR | 13.09 | -0.26 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-25T14:45 | CCI reversion · 1h | sell | META | 13.12 | -0.21 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-25T14:45 | CCI reversion · 1h | sell | ETH-USD | 13.08 | -0.22 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-25T14:45 | Stochastic reversion · 1h | buy | MSFT | 5.15 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 15:11:05.000171+00:00 -> 2026-11-25 15:21:05.000171+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
