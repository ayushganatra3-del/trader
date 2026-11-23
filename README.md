# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T19:46:05.000124+00:00 · 70918 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £79.13 (-20.87%)

Closed trades 240, win rate 35.8%, fees £6.51, max drawdown -21.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 16.04 | +0.27 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 31676 decisions in 2920 calls, $0.3954 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T19:46 | 1 / 11 / 18 | cash |  |
| Breezy | 2026-11-23T19:46 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-23T19:46 | 2 / 22 / 6 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.81% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 32.17 | 4.75 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.48 | 15.48 | 0 | — | 13.07 | 4.43 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.06 | 4.06 | 0 | — | 2.79 | 0.82 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.90 | -0.19 | -8.58 | 209 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.78 | -3.55 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.97 | -0.23 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.34 | -4.66 | 0 | — | -6.28 | -1.61 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.54 | -3.35 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.54 | -7.46 | 0 | — | -8.65 | -1.76 | -13.87 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 16 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -4.94 | -3.08 | -8.11 | 30 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.86 | -9.14 | 0 | — | -10.51 | -2.24 | -17.03 | 1 |
| 18 | VWAP reversion · 1h | reversion | 90.00 | -10.00 | 163 | 46.0 | -7.49 | -1.31 | -20.49 | 156 |
| 19 | Copy: Insider buying | copy | 89.55 | -10.45 | 57 | 40.4 | -17.91 | -3.45 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -16.67 | -3.46 | -20.94 | 1 |
| 21 | Opening range 30m | breakout | 86.39 | -13.61 | 457 | 33.3 | -13.16 | -4.37 | -14.39 | 542 |
| 22 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.24 | -13.76 | 9 | 44.4 | -11.42 | -0.64 | -26.65 | 6 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -17.03 | -3.92 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -17.49 | -6.37 | -18.27 | 73 |
| 25 | Connors RSI(2) · 1h | reversion | 80.68 | -19.32 | 220 | 40.9 | -14.06 | -6.14 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.16 | -19.84 | 203 | 28.1 | -28.35 | -7.57 | -30.33 | 190 |
| 27 | Agent | meta | 79.13 | -20.87 | 240 | 35.8 | -25.75 | -5.63 | -26.43 | 200 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -26.36 | -4.46 | -26.36 | 94 |
| 29 | Opening range 15m | breakout | 77.29 | -22.71 | 567 | 30.9 | -22.53 | -6.94 | -23.30 | 660 |
| 30 | Donchian 55/20 · 1h ⏸ | breakout | 76.80 | -23.20 | 85 | 14.1 | -29.17 | -7.70 | -29.50 | 84 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.99 | -6.93 | -23.25 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -26.66 | -6.83 | -27.16 | 149 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.47 | -7.96 | -31.34 | 103 |
| 34 | Hold BTC | benchmark | 70.97 | -29.03 | 3 | 0.0 | -29.57 | -5.29 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 70.58 | -29.42 | 200 | 17.0 | -34.99 | -6.70 | -38.68 | 218 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.57 | -29.43 | 3 | 0.0 | -24.29 | -2.94 | -32.18 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -36.58 | -6.49 | -38.98 | 281 |
| 38 | EMA 20/50 cross · 1h | trend | 69.61 | -30.39 | 119 | 10.1 | -36.95 | -10.25 | -39.51 | 124 |
| 39 | Triple EMA stack · 1h | trend | 69.59 | -30.41 | 162 | 14.8 | -36.51 | -9.20 | -38.10 | 168 |
| 40 | Daily: Momentum burst | daily | 69.43 | -30.57 | 30 | 13.3 | -37.64 | -5.37 | -38.43 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.56 | -31.44 | 207 | 22.2 | -33.48 | -8.75 | -34.52 | 213 |
| 42 | OBV trend · 1h | momentum | 66.94 | -33.06 | 320 | 19.7 | -40.22 | -10.38 | -41.40 | 230 |
| 43 | Stochastic reversion · 1h | reversion | 66.70 | -33.30 | 394 | 40.9 | -35.74 | -3.94 | -43.67 | 434 |
| 44 | MACD zero-line · 1h | trend | 65.81 | -34.19 | 198 | 16.7 | -34.10 | -9.17 | -34.29 | 211 |
| 45 | RSI momentum · 1h ⏸ | momentum | 65.10 | -34.90 | 196 | 15.3 | -40.28 | -9.07 | -41.60 | 203 |
| 46 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -47.25 | -9.43 | -47.75 | 630 |
| 47 | Max aggression: 5-day momentum ⏸ | meta | 64.49 | -35.51 | 25 | 36.0 | -61.60 | -3.98 | -65.46 | 23 |
| 48 | MFI reversion · 1h | reversion | 63.09 | -36.91 | 486 | 32.9 | -31.96 | -4.64 | -37.45 | 184 |
| 49 | Donchian 20/10 · 1h ⏸ | breakout | 62.04 | -37.97 | 178 | 18.0 | -39.64 | -8.38 | -41.27 | 193 |
| 50 | ROC + volume · 1h ⏸ | momentum | 61.62 | -38.38 | 451 | 27.1 | -42.57 | -8.51 | -42.57 | 345 |
| 51 | EMA 9/21 cross · 1h | trend | 59.84 | -40.16 | 299 | 11.4 | -45.08 | -10.50 | -46.09 | 328 |
| 52 | Agent (ML meta-label) | meta | 59.52 | -40.48 | 2046 | 25.0 | -24.18 | -3.23 | -34.17 | 338 |
| 53 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -54.14 | -3.88 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 58.73 | -41.27 | 464 | 20.9 | -49.79 | -9.54 | -51.14 | 515 |
| 55 | CCI reversion · 1h | reversion | 57.80 | -42.20 | 430 | 40.0 | -49.87 | -8.32 | -52.16 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 57.76 | -42.24 | 391 | 37.6 | -37.89 | -4.55 | -45.42 | 434 |
| 57 | Williams %R · 1h | reversion | 53.69 | -46.31 | 500 | 38.4 | -55.36 | -9.13 | -56.25 | 594 |
| 58 | VWAP momentum · 1h | momentum | 53.58 | -46.42 | 1052 | 21.8 | -58.23 | -13.34 | -58.78 | 1181 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.24 | -8.37 | -53.84 | 689 |
| 60 | RSI(14) reversion · 1h | reversion | 50.80 | -49.20 | 240 | 31.7 | -48.34 | -7.38 | -50.82 | 314 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -47.85 | -99.13 | 5329 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.99 | -33.08 | -84.49 | 1430 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.47 | -47.33 | -94.49 | 2428 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.88 | -31.64 | -91.04 | 1926 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.79 | -40.44 | -91.79 | 2253 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.53 | -27.52 | -89.59 | 1947 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -47.77 | -98.15 | 3419 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.99 | -50.46 | -97.01 | 3363 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -38.12 | -93.67 | 2141 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.26 | -22.44 | -52.27 | 647 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.40 | -34.36 | -83.49 | 1560 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -53.74 | -99.67 | 6287 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.24 | -39.20 | -93.24 | 2491 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.46 | -35.35 | -94.46 | 3180 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -61.28 | -99.82 | 6124 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.19 | -42.49 | -93.40 | 2263 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.29 | -24.04 | -78.61 | 1612 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -54.96 | -97.79 | 3289 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -57.06 | -99.19 | 5110 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.74 | -27.44 | -70.75 | 1193 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.98 | -47.92 | -94.98 | 2671 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -45.13 | -6.26 | -48.78 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.67 | -37.06 | -85.67 | 1677 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.53 | -99.76 | 6539 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.52 | -29.88 | -91.69 | 2463 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.96 | -20.00 | -82.96 | 1953 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.85 | -30.46 | -91.98 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -47.30 | -98.15 | 4044 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.25 | -46.73 | -90.29 | 2199 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.39 | -29.79 | -68.40 | 796 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.10 | -27.74 | -74.18 | 1170 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.42 | -19.15 | -84.44 | 1845 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.00 | -47.73 | -98.00 | 4422 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -89.42 | -99.94 | 8276 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T19:40 | Max aggression: 5-day momentum | sell | SOL-USD | 64.49 | -4.49 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:40 | Agent (ML meta-label) | buy | BITX | 14.88 | — | entry |
| 2026-11-23T19:40 | Donchian 20/10 · 1h | sell | XRP-USD | 15.48 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:40 | Donchian 20/10 · 1h | sell | SOL-USD | 15.42 | 0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:40 | Donchian 20/10 · 1h | sell | NVDA | 12.60 | -0.32 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:40 | Donchian 20/10 · 1h | sell | BTC-USD | 15.51 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:35 | Agent (ML meta-label) | sell | SQQQ | 15.01 | -0.01 | selected signal exited |
| 2026-11-23T19:35 | Donchian 55/20 · 1h | sell | XRP-USD | 18.83 | -0.19 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:35 | Donchian 55/20 · 1h | sell | SOL-USD | 19.08 | 0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:30 | Agent | buy | SQQQ | 15.77 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T19:30 | Williams %R · 1h | sell | TNA | 5.44 | 0.02 | exit signal |
| 2026-11-23T19:30 | Connors RSI(2) · 1h | sell | SQQQ | 20.65 | 0.56 | exit signal |
| 2026-11-23T19:30 | VWAP momentum · 1h | buy | SQQQ | 4.88 | — | entry signal |
| 2026-11-23T19:30 | VWAP momentum · 1h | sell | QQQ | 4.88 | -0.01 | exit signal |
| 2026-11-23T19:30 | MACD zero-line · 1h | buy | TSLA | 16.50 | — | entry signal |
| 2026-11-23T19:25 | Agent (ML meta-label) | sell | BITX | 14.90 | -0.08 | selected signal exited |
| 2026-11-23T19:20 | Agent (ML meta-label) | buy | BITX | 14.98 | — | entry |
| 2026-11-23T19:17 | Agent (ML meta-label) | sell | BITX | 14.97 | -0.03 | selected signal exited |
| 2026-11-23T19:15 | Agent (ML meta-label) | buy | BITX | 15.00 | — | entry |
| 2026-11-23T19:11 | Agent (ML meta-label) | buy | SQQQ | 15.01 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T19:11 | Agent (ML meta-label) | sell | BITX | 14.99 | -0.03 | selected signal exited |
| 2026-11-23T19:00 | Agent (ML meta-label) | sell | SQQQ | 15.02 | 0.06 | selected signal exited |
| 2026-11-23T19:00 | Connors RSI(2) · 1h | buy | SOL-USD | 20.31 | — | entry signal |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | XRP-USD | 7.96 | -0.50 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | TSLA | 5.48 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | SOL-USD | 8.06 | 0.21 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | PLTR | 8.27 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | NVDA | 8.13 | -0.29 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | ETH-USD | 10.93 | 0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | DOGE-USD | 8.12 | 0.20 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | BTC-USD | 8.15 | 0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | Ichimoku · 1h | sell | DOGE-USD | 19.86 | 0.52 | exit signal |
| 2026-11-23T19:00 | Supertrend · 1h | buy | AMZN | 2.86 | — | entry |
| 2026-11-23T19:00 | Supertrend · 1h | sell | XRP-USD | 2.86 | -0.08 | exit signal |
| 2026-11-23T18:55 | Agent (ML meta-label) | buy | SQQQ | 14.96 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T18:51 | Agent (ML meta-label) | sell | SQQQ | 14.32 | -0.04 | selected signal exited |
| 2026-11-23T18:40 | Donchian 55/20 · 1h | sell | DOGE-USD | 19.24 | -0.48 | stop-loss |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | buy | XRP-USD | 4.74 | — | rebalance up |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | buy | SOL-USD | 4.70 | — | rebalance up |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | buy | BTC-USD | 4.67 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 19:46:05.000124+00:00 -> 2026-11-23 19:56:05.000124+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
