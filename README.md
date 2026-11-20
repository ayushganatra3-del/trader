# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T20:20:05.000136+00:00 · 67254 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £80.18 (-19.82%)

Closed trades 238, win rate 36.1%, fees £6.46, max drawdown -20.19%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-20 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.48 · VIX 28.44 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 37740 decisions in 3123 calls, $0.4678 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T20:20 | 12 / 16 / 3 | cash |  |
| Breezy | 2026-11-20T20:20 | 0 / 24 / 7 | cash |  |
| Boozy | 2026-11-20T20:20 | 10 / 17 / 4 | COIN 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| MFI reversion | META | 2.04 | +2.40% | 6 |
| CCI reversion | SOXL | 1.96 | +18.20% | 16 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 126.36 | 26.36 | 26 | 65.4 | 29.46 | 4.58 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.34 | 14.34 | 0 | — | 12.16 | 4.07 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.70 | 7.70 | 40 | 42.5 | 5.69 | 1.15 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 102.04 | 2.04 | 0 | — | 2.95 | 0.89 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.91 | -0.09 | 203 | 31.5 | 0.74 | 0.33 | -9.06 | 202 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 97.26 | -2.74 | 212 | 28.8 | 0.37 | 0.21 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.02 | -4.43 | -10.81 | 44 |
| 14 | Hold SPY | benchmark | 91.31 | -8.69 | 0 | — | -9.78 | -3.14 | -11.25 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Bullish score | daily | 90.54 | -9.46 | 19 | 15.8 | -11.79 | -2.86 | -19.56 | 14 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.35 | -10.65 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | Squeeze breakout · 1h | breakout | 88.06 | -11.94 | 70 | 20.0 | -17.30 | -7.98 | -18.95 | 72 |
| 19 | VWAP reversion · 1h | reversion | 87.50 | -12.50 | 157 | 45.2 | -14.56 | -4.19 | -19.44 | 153 |
| 20 | Copy: Insider buying | copy | 87.43 | -12.57 | 56 | 39.3 | -8.86 | -1.72 | -14.79 | 66 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Opening range 30m | breakout | 87.03 | -12.97 | 451 | 33.5 | -10.97 | -3.61 | -14.87 | 552 |
| 23 | Copy: Congress Democrats (NANC) | copy | 86.54 | -13.46 | 0 | — | -14.17 | -3.77 | -16.37 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -18.92 | -1.68 | -25.53 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.50 | -15.50 | 194 | 27.8 | -23.98 | -6.59 | -28.86 | 195 |
| 26 | Donchian 55/20 · 1h | breakout | 81.50 | -18.50 | 79 | 12.7 | -24.28 | -6.90 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.32 | -18.68 | 163 | 28.8 | -14.84 | -4.59 | -21.55 | 74 |
| 28 | Keltner breakout · 1h | breakout | 80.18 | -19.82 | 126 | 26.2 | -20.54 | -5.34 | -25.34 | 144 |
| 29 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -20.71 | -5.42 | -21.10 | 212 |
| 30 | Connors RSI(2) · 1h | reversion | 79.90 | -20.10 | 218 | 40.4 | -15.29 | -6.92 | -15.39 | 71 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -16.34 | -4.22 | -19.15 | 98 |
| 32 | Opening range 15m | breakout | 77.37 | -22.63 | 561 | 31.0 | -21.30 | -6.55 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.47 | -23.53 | 107 | 14.0 | -28.29 | -7.83 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.43 | -25.57 | 228 | 20.2 | -25.07 | -3.69 | -35.87 | 273 |
| 35 | Bollinger breakout · 1h | breakout | 72.64 | -27.36 | 195 | 21.5 | -31.54 | -7.92 | -36.32 | 217 |
| 36 | Triple EMA stack · 1h | trend | 72.60 | -27.40 | 161 | 14.3 | -32.02 | -7.63 | -37.24 | 170 |
| 37 | Supertrend · 1h | trend | 72.58 | -27.42 | 198 | 16.7 | -33.80 | -6.65 | -37.64 | 199 |
| 38 | EMA 20/50 cross · 1h | trend | 72.28 | -27.72 | 119 | 10.1 | -36.00 | -9.97 | -40.64 | 122 |
| 39 | Max aggression: 1-day momentum | meta | 71.85 | -28.15 | 33 | 27.3 | -49.73 | -3.49 | -58.27 | 39 |
| 40 | Heikin-Ashi · 1h | trend | 70.69 | -29.31 | 483 | 23.0 | -44.11 | -9.20 | -47.85 | 616 |
| 41 | RSI momentum · 1h | momentum | 70.37 | -29.63 | 184 | 14.1 | -37.25 | -8.16 | -41.33 | 202 |
| 42 | Copy: Cathie Wood (ARKK) ⏸ | copy | 70.36 | -29.64 | 3 | 0.0 | -28.59 | -4.07 | -31.67 | 1 |
| 43 | OBV trend · 1h | momentum | 70.11 | -29.89 | 316 | 19.6 | -41.08 | -11.75 | -41.42 | 239 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -50.09 | -3.32 | -60.06 | 22 |
| 46 | Hold BTC ⏸ | benchmark | 68.38 | -31.62 | 3 | 0.0 | -28.10 | -4.54 | -33.67 | 1 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Donchian 20/10 · 1h | breakout | 67.03 | -32.97 | 165 | 17.6 | -34.77 | -6.33 | -43.26 | 191 |
| 49 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -42.54 | -6.09 | -43.32 | 443 |
| 50 | ROC + volume · 1h | momentum | 66.13 | -33.87 | 431 | 27.6 | -34.71 | -6.23 | -41.19 | 336 |
| 51 | MFI reversion · 1h ⏸ | reversion | 64.95 | -35.05 | 476 | 33.0 | -35.20 | -5.27 | -36.76 | 172 |
| 52 | EMA 9/21 cross · 1h | trend | 64.49 | -35.51 | 291 | 11.3 | -38.34 | -6.95 | -47.42 | 322 |
| 53 | CCI reversion · 1h | reversion | 62.82 | -37.18 | 408 | 40.9 | -46.60 | -7.67 | -47.70 | 479 |
| 54 | MACD cross · 1h | trend | 62.79 | -37.21 | 444 | 20.9 | -49.81 | -9.93 | -51.01 | 496 |
| 55 | Bollinger reversion · 1h ⏸ | reversion | 58.24 | -41.76 | 377 | 36.6 | -43.79 | -6.65 | -44.60 | 430 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -51.91 | -8.54 | -52.74 | 582 |
| 57 | RSI(14) reversion · 1h | reversion | 55.69 | -44.31 | 224 | 33.0 | -41.89 | -6.05 | -45.87 | 272 |
| 58 | Agent (ML meta-label) | meta | 55.67 | -44.33 | 2004 | 24.7 | -26.26 | -4.89 | -28.25 | 305 |
| 59 | VWAP momentum · 1h | momentum | 55.03 | -44.97 | 1013 | 21.4 | -55.83 | -11.11 | -60.51 | 1192 |
| 60 | Z-score reversion · 1h ⏸ | reversion | 52.10 | -47.90 | 242 | 33.1 | -43.59 | -6.03 | -45.98 | 265 |
| 61 | Three white soldiers | momentum | 51.69 | -48.31 | 618 | 14.1 | -51.98 | -23.30 | -52.32 | 664 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -53.16 | -9.57 | -53.26 | 679 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -47.65 | -99.14 | 5328 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.44 | -30.43 | -84.01 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.39 | -46.96 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.27 | -34.16 | -91.37 | 1953 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.05 | -44.85 | -92.23 | 2292 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.93 | -28.40 | -90.21 | 2024 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.26 | -49.97 | -98.26 | 3491 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -51.46 | -96.88 | 3390 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.83 | -40.44 | -93.96 | 2204 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.56 | -35.78 | -83.61 | 1579 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -56.50 | -99.66 | 6360 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.21 | -44.59 | -93.23 | 2536 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.49 | -94.64 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -72.87 | -99.84 | 6289 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.53 | -46.76 | -93.53 | 2287 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.90 | -26.84 | -78.97 | 1637 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.78 | -97.83 | 3381 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -59.26 | -99.15 | 5120 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.03 | -29.85 | -71.12 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.10 | -55.20 | -95.12 | 2731 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.72 | -39.41 | -85.95 | 1705 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -72.58 | -99.73 | 6562 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.64 | -31.86 | -91.67 | 2483 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.79 | -19.28 | -81.86 | 1943 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.45 | -34.61 | -92.46 | 2200 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.86 | -47.27 | -97.87 | 4052 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.59 | -52.89 | -90.61 | 2208 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.23 | -32.14 | -67.32 | 793 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.85 | -27.75 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.77 | -19.06 | -83.81 | 1860 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.75 | -47.09 | -97.75 | 4451 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -117.18 | -99.95 | 8432 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T20:05 | Copy: Cathie Wood (ARKK) | sell | ARKK | 70.36 | -9.70 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T20:05 | Three white soldiers | sell | AMD | 12.83 | -0.12 | exit signal |
| 2026-11-20T20:00 | VWAP reversion · 1h | buy | BTC-USD | 21.89 | — | entry signal |
| 2026-11-20T19:55 | Three white soldiers | buy | AMD | 12.95 | — | entry signal |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | TNA | 6.39 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | SOL-USD | 6.44 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | PLTR | 6.48 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | MSTR | 6.46 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | MSFT | 6.55 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | IWM | 6.54 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | DOGE-USD | 5.81 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | COIN | 6.48 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | AMD | 6.41 | -0.18 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | VWAP momentum · 1h | sell | SQQQ | 2.76 | 0.48 | rebalance down |
| 2026-11-20T19:30 | CCI reversion · 1h | sell | GOOGL | 15.49 | -0.49 | stop-loss |
| 2026-11-20T19:30 | Bollinger reversion · 1h | buy | DOGE-USD | 5.85 | — | entry |
| 2026-11-20T19:30 | Bollinger reversion · 1h | sell | GOOGL | 6.53 | -0.21 | stop-loss |
| 2026-11-20T19:25 | MFI reversion · 1h | sell | DOGE-USD | 16.01 | -0.31 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:25 | OBV trend · 1h | sell | SQQQ | 19.95 | 3.23 | target is flat |
| 2026-11-20T19:20 | VWAP reversion · 1h | sell | BTC-USD | 21.57 | -0.72 | stop-loss |
| 2026-11-20T19:00 | MFI reversion · 1h | buy | DOGE-USD | 16.32 | — | entry signal |
| 2026-11-20T18:50 | Hold BTC | sell | BTC-USD | 68.38 | -6.75 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T18:47 | Three white soldiers | sell | MSTR | 12.79 | -0.22 | stop-loss |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | TNA | 4.69 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | TECL | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | PLTR | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | LABU | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | ETHU | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | buy | COIN | 4.73 | — | entry |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | XRP-USD | 2.91 | -0.01 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | SQQQ | 6.57 | 0.60 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | SOL-USD | 4.70 | -0.02 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | MSTR | 4.78 | 0.07 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | BITX | 4.67 | -0.04 | rebalance down |
| 2026-11-20T18:30 | Agent (ML meta-label) | sell | AMD | 4.71 | 0.02 | rebalance down |
| 2026-11-20T18:30 | Copy: Insider buying | buy | PSEC | 10.99 | — | entry |
| 2026-11-20T18:30 | Copy: Insider buying | sell | LRN | 11.19 | -0.41 | target is flat |
| 2026-11-20T18:30 | CCI reversion · 1h | sell | AAPL | 12.70 | -0.17 | stop-loss |
| 2026-11-20T18:30 | Bollinger reversion · 1h | buy | TNA | 6.55 | — | entry signal |
| 2026-11-20T18:30 | Bollinger reversion · 1h | buy | PLTR | 6.59 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 20:20:05.000136+00:00 -> 2026-11-20 20:30:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
