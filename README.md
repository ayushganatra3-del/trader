# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T23:51:05.000153+00:00 · 67437 ticks

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

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 47.40 · VIX 38.87 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 43062 decisions in 3672 calls, $0.5353 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T23:51 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-20T23:51 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-20T23:51 | 1 / 3 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.03 | +18.56% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.49 | 14.49 | 0 | — | 12.18 | 4.08 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.74 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 0.89 | 0.39 | -8.00 | 156 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.28 | -4.56 | -11.06 | 45 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.21 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -2.72 | -19.56 | 14 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.98 | -7.58 | -18.95 | 72 |
| 18 | VWAP reversion · 1h | reversion | 87.96 | -12.04 | 157 | 45.2 | -14.28 | -4.16 | -20.28 | 155 |
| 19 | Copy: Insider buying | copy | 87.95 | -12.05 | 56 | 39.3 | -8.22 | -1.59 | -14.79 | 66 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.47 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -3.84 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.78 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.90 | -15.10 | 194 | 27.8 | -23.69 | -6.37 | -28.86 | 195 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.98 | -6.67 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -16.91 | -5.91 | -21.60 | 75 |
| 28 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 126 | 26.2 | -20.74 | -5.52 | -25.26 | 147 |
| 29 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -21.40 | -5.23 | -21.75 | 212 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.21 | -6.87 | -15.24 | 71 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -16.48 | -4.23 | -19.15 | 98 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.44 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -28.01 | -7.61 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.72 | -25.28 | 228 | 20.2 | -30.72 | -5.72 | -35.87 | 269 |
| 35 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.96 | -3.42 | -58.28 | 39 |
| 36 | Bollinger breakout · 1h | breakout | 72.97 | -27.03 | 195 | 21.5 | -31.81 | -8.07 | -36.25 | 218 |
| 37 | Supertrend · 1h | trend | 72.93 | -27.07 | 198 | 16.7 | -33.54 | -6.53 | -37.64 | 199 |
| 38 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -31.81 | -7.48 | -37.24 | 170 |
| 39 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.75 | -9.72 | -40.64 | 122 |
| 40 | Heikin-Ashi · 1h | trend | 71.02 | -28.98 | 483 | 23.0 | -44.01 | -9.10 | -47.85 | 616 |
| 41 | RSI momentum · 1h | momentum | 70.70 | -29.30 | 184 | 14.1 | -36.93 | -7.87 | -41.77 | 202 |
| 42 | Copy: Cathie Wood (ARKK) ⏸ | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 43 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -37.20 | -9.52 | -41.22 | 240 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 46 | Hold BTC ⏸ | benchmark | 68.38 | -31.62 | 3 | 0.0 | -27.82 | -4.55 | -33.67 | 1 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Donchian 20/10 · 1h | breakout | 67.34 | -32.66 | 165 | 17.6 | -35.35 | -6.72 | -43.26 | 193 |
| 49 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -43.23 | -6.15 | -43.87 | 445 |
| 50 | ROC + volume · 1h | momentum | 66.42 | -33.58 | 431 | 27.6 | -36.94 | -6.51 | -43.31 | 342 |
| 51 | MFI reversion · 1h ⏸ | reversion | 64.95 | -35.05 | 476 | 33.0 | -35.63 | -5.28 | -37.53 | 176 |
| 52 | EMA 9/21 cross · 1h | trend | 64.80 | -35.20 | 291 | 11.3 | -42.42 | -9.85 | -46.01 | 318 |
| 53 | MACD cross · 1h | trend | 63.03 | -36.97 | 444 | 20.9 | -49.62 | -9.91 | -51.01 | 496 |
| 54 | CCI reversion · 1h ⏸ | reversion | 62.30 | -37.70 | 413 | 40.4 | -46.87 | -7.66 | -48.00 | 484 |
| 55 | Bollinger reversion · 1h ⏸ | reversion | 58.24 | -41.76 | 377 | 36.6 | -44.25 | -6.67 | -45.16 | 444 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -52.50 | -8.62 | -53.01 | 583 |
| 57 | RSI(14) reversion · 1h | reversion | 55.38 | -44.62 | 225 | 32.9 | -42.61 | -6.18 | -46.21 | 275 |
| 58 | Agent (ML meta-label) | meta | 55.28 | -44.72 | 2005 | 24.6 | -30.21 | -5.31 | -32.06 | 318 |
| 59 | VWAP momentum · 1h | momentum | 55.26 | -44.74 | 1013 | 21.4 | -56.12 | -11.18 | -60.93 | 1195 |
| 60 | Z-score reversion · 1h ⏸ | reversion | 52.10 | -47.90 | 242 | 33.1 | -43.80 | -6.04 | -46.19 | 269 |
| 61 | Three white soldiers | momentum | 51.39 | -48.61 | 621 | 14.0 | -52.52 | -22.90 | -52.86 | 668 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -53.37 | -9.55 | -53.65 | 681 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -46.87 | -99.14 | 5326 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.53 | -30.41 | -84.09 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.67 | -94.46 | 2454 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.17 | -34.06 | -91.39 | 1955 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.99 | -44.67 | -92.21 | 2296 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.89 | -28.16 | -90.21 | 2024 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.24 | -50.00 | -98.24 | 3491 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.74 | -54.80 | -96.78 | 3391 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.85 | -39.73 | -93.95 | 2196 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.49 | -35.69 | -83.61 | 1582 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -56.00 | -99.66 | 6356 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.12 | -44.96 | -93.17 | 2537 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.50 | -94.63 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -71.95 | -99.84 | 6289 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.53 | -46.25 | -93.54 | 2289 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.55 | -25.45 | -79.74 | 1646 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.83 | -60.71 | -97.83 | 3381 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -58.32 | -99.15 | 5119 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.06 | -29.84 | -71.12 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.06 | -55.16 | -95.08 | 2733 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.67 | -39.29 | -85.92 | 1708 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -71.32 | -99.73 | 6562 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.49 | -31.12 | -91.58 | 2480 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.07 | -19.44 | -82.27 | 1949 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.70 | -33.53 | -92.70 | 2214 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.88 | -46.05 | -97.89 | 4050 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.41 | -53.41 | -90.51 | 2206 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.33 | -31.99 | -67.49 | 793 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.81 | -27.60 | -74.90 | 1205 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.47 | -19.06 | -83.84 | 1855 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.75 | -46.42 | -97.77 | 4449 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.44 | -99.94 | 8428 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T23:30 | CCI reversion · 1h | sell | XRP-USD | 12.43 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T23:30 | CCI reversion · 1h | sell | SOL-USD | 12.48 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T23:30 | CCI reversion · 1h | sell | ETH-USD | 12.47 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T23:30 | CCI reversion · 1h | sell | DOGE-USD | 12.47 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T23:30 | CCI reversion · 1h | sell | BTC-USD | 12.45 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T23:00 | CCI reversion · 1h | buy | XRP-USD | 12.56 | — | entry signal |
| 2026-11-20T23:00 | CCI reversion · 1h | buy | SOL-USD | 12.56 | — | entry signal |
| 2026-11-20T23:00 | CCI reversion · 1h | buy | ETH-USD | 12.56 | — | entry signal |
| 2026-11-20T23:00 | CCI reversion · 1h | buy | DOGE-USD | 12.56 | — | entry signal |
| 2026-11-20T23:00 | CCI reversion · 1h | buy | BTC-USD | 12.56 | — | entry signal |
| 2026-11-20T22:50 | Three white soldiers | sell | XRP-USD | 12.85 | -0.07 | exit signal |
| 2026-11-20T22:50 | Three white soldiers | sell | SOL-USD | 12.85 | -0.08 | exit signal |
| 2026-11-20T22:35 | Three white soldiers | sell | ETH-USD | 12.77 | -0.15 | exit signal |
| 2026-11-20T22:00 | RSI(14) reversion · 1h | buy | XRP-USD | 13.85 | — | entry signal |
| 2026-11-20T22:00 | RSI(14) reversion · 1h | buy | SOL-USD | 13.85 | — | entry signal |
| 2026-11-20T22:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 13.85 | — | entry signal |
| 2026-11-20T22:00 | RSI(14) reversion · 1h | buy | BTC-USD | 13.85 | — | entry signal |
| 2026-11-20T21:45 | Three white soldiers | buy | XRP-USD | 12.92 | — | entry signal |
| 2026-11-20T21:45 | Three white soldiers | buy | SOL-USD | 12.92 | — | entry signal |
| 2026-11-20T21:45 | Three white soldiers | buy | ETH-USD | 12.92 | — | entry signal |
| 2026-11-20T21:10 | RSI(14) reversion · 1h | sell | SOL-USD | 13.44 | -0.54 | stop-loss |
| 2026-11-20T20:55 | Agent (rotation) | sell | SQQQ | 42.05 | 2.51 | selected signal exited |
| 2026-11-20T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 109.37 | 9.74 | target is flat |
| 2026-11-20T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 128.32 | 6.58 | target is flat |
| 2026-11-20T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 91.73 | 0.70 | target is flat |
| 2026-11-20T20:55 | Opening range 30m | sell | SQQQ | 23.47 | 2.15 | end-of-day flatten |
| 2026-11-20T20:55 | Opening range 15m | sell | SQQQ | 20.96 | 1.92 | end-of-day flatten |
| 2026-11-20T20:55 | Gap and go | sell | SQQQ | 26.94 | 2.47 | end-of-day flatten |
| 2026-11-20T20:48 | Agent (ML meta-label) | buy | BTC-USD | 3.68 | — | entry |
| 2026-11-20T20:48 | Agent (ML meta-label) | sell | XRP-USD | 4.58 | -0.15 | selected signal exited |
| 2026-11-20T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 91.03 | — | entry |
| 2026-11-20T20:30 | VWAP reversion · 1h | buy | ETHU | 14.54 | — | entry signal |
| 2026-11-20T20:30 | VWAP reversion · 1h | buy | AMD | 14.60 | — | entry signal |
| 2026-11-20T20:30 | VWAP reversion · 1h | buy | AAPL | 14.60 | — | entry signal |
| 2026-11-20T20:30 | VWAP reversion · 1h | sell | XRP-USD | 7.19 | -0.18 | rebalance down |
| 2026-11-20T20:30 | VWAP reversion · 1h | sell | DOGE-USD | 7.31 | -0.14 | rebalance down |
| 2026-11-20T20:30 | VWAP reversion · 1h | sell | BTC-USD | 7.28 | -0.02 | rebalance down |
| 2026-11-20T20:25 | OBV trend · 1h | buy | SQQQ | 17.53 | — | entry |
| 2026-11-20T20:05 | Copy: Cathie Wood (ARKK) | sell | ARKK | 70.36 | -9.70 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T20:05 | Three white soldiers | sell | AMD | 12.83 | -0.12 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 23:51:05.000153+00:00 -> 2026-11-21 00:01:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
