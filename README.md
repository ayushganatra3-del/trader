# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T20:50:05.000131+00:00 · 67280 ticks

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

Today: 40101 decisions in 3201 calls, $0.4955 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T20:50 | 10 / 18 / 2 | TECL 14% |  |
| Breezy | 2026-11-20T20:50 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-20T20:50 | 7 / 22 / 1 | COIN 56% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 126.34 | 26.34 | 26 | 65.4 | 29.37 | 4.57 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.88 | 13.88 | 0 | — | 11.64 | 3.89 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.68 | 7.68 | 40 | 42.5 | 5.61 | 1.14 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 102.11 | 2.11 | 0 | — | 2.96 | 0.89 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.91 | -0.09 | 203 | 31.5 | 0.72 | 0.32 | -9.06 | 202 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 97.25 | -2.75 | 212 | 28.8 | 0.35 | 0.20 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.02 | -4.43 | -10.81 | 44 |
| 14 | Hold SPY | benchmark | 91.31 | -8.69 | 0 | — | -9.83 | -3.15 | -11.71 | 1 |
| 15 | Daily: Bullish score | daily | 90.53 | -9.47 | 19 | 15.8 | -11.80 | -2.86 | -19.56 | 14 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.31 | -9.69 | 26 | 15.4 | -10.89 | -8.95 | -10.89 | 25 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.40 | -10.60 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | Squeeze breakout · 1h | breakout | 88.06 | -11.94 | 70 | 20.0 | -17.31 | -7.99 | -18.95 | 72 |
| 19 | Copy: Insider buying | copy | 87.54 | -12.46 | 56 | 39.3 | -9.11 | -1.76 | -14.79 | 66 |
| 20 | VWAP reversion · 1h | reversion | 87.51 | -12.49 | 157 | 45.2 | -14.59 | -4.20 | -20.28 | 156 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Opening range 30m | breakout | 87.03 | -12.97 | 451 | 33.5 | -10.98 | -3.62 | -14.87 | 552 |
| 23 | Copy: Congress Democrats (NANC) | copy | 86.85 | -13.15 | 0 | — | -13.90 | -3.74 | -16.54 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -19.16 | -1.70 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.49 | -15.51 | 194 | 27.8 | -23.99 | -6.59 | -28.86 | 195 |
| 26 | Donchian 55/20 · 1h | breakout | 81.50 | -18.50 | 79 | 12.7 | -24.29 | -6.91 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.32 | -18.68 | 163 | 28.8 | -14.87 | -4.62 | -21.55 | 74 |
| 28 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -21.20 | -5.31 | -22.00 | 212 |
| 29 | Keltner breakout · 1h | breakout | 80.18 | -19.82 | 126 | 26.2 | -21.21 | -5.65 | -25.34 | 147 |
| 30 | Connors RSI(2) · 1h | reversion | 79.91 | -20.09 | 218 | 40.4 | -15.29 | -6.92 | -15.43 | 71 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -16.63 | -4.27 | -19.15 | 98 |
| 32 | Opening range 15m | breakout | 77.37 | -22.64 | 561 | 31.0 | -21.31 | -6.56 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.47 | -23.53 | 107 | 14.0 | -28.30 | -7.84 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.42 | -25.58 | 228 | 20.2 | -25.08 | -3.69 | -35.87 | 273 |
| 35 | Bollinger breakout · 1h | breakout | 72.64 | -27.36 | 195 | 21.5 | -31.55 | -7.92 | -36.32 | 217 |
| 36 | Triple EMA stack · 1h | trend | 72.60 | -27.40 | 161 | 14.3 | -32.02 | -7.64 | -37.24 | 170 |
| 37 | Supertrend · 1h | trend | 72.58 | -27.42 | 198 | 16.7 | -33.81 | -6.66 | -37.64 | 199 |
| 38 | EMA 20/50 cross · 1h | trend | 72.27 | -27.73 | 119 | 10.1 | -36.01 | -9.98 | -40.64 | 122 |
| 39 | Max aggression: 1-day momentum | meta | 71.83 | -28.17 | 33 | 27.3 | -49.76 | -3.50 | -58.27 | 39 |
| 40 | Heikin-Ashi · 1h | trend | 70.69 | -29.31 | 483 | 23.0 | -44.18 | -9.24 | -47.85 | 616 |
| 41 | RSI momentum · 1h | momentum | 70.37 | -29.63 | 184 | 14.1 | -37.25 | -8.16 | -41.33 | 202 |
| 42 | Copy: Cathie Wood (ARKK) ⏸ | copy | 70.36 | -29.64 | 3 | 0.0 | -29.12 | -4.12 | -32.18 | 1 |
| 43 | OBV trend · 1h | momentum | 70.03 | -29.97 | 316 | 19.6 | -39.93 | -10.98 | -41.43 | 240 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -50.12 | -3.32 | -60.06 | 22 |
| 46 | Hold BTC ⏸ | benchmark | 68.38 | -31.62 | 3 | 0.0 | -28.11 | -4.53 | -33.67 | 1 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Donchian 20/10 · 1h | breakout | 67.03 | -32.97 | 165 | 17.6 | -34.90 | -6.41 | -43.26 | 192 |
| 49 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -42.49 | -6.09 | -43.86 | 446 |
| 50 | ROC + volume · 1h | momentum | 66.12 | -33.88 | 431 | 27.6 | -34.72 | -6.23 | -41.19 | 336 |
| 51 | MFI reversion · 1h ⏸ | reversion | 64.95 | -35.05 | 476 | 33.0 | -35.23 | -5.27 | -36.88 | 172 |
| 52 | EMA 9/21 cross · 1h | trend | 64.49 | -35.51 | 291 | 11.3 | -38.35 | -6.95 | -47.42 | 322 |
| 53 | CCI reversion · 1h | reversion | 62.82 | -37.18 | 408 | 40.9 | -46.60 | -7.67 | -47.70 | 479 |
| 54 | MACD cross · 1h | trend | 62.79 | -37.21 | 444 | 20.9 | -49.82 | -9.93 | -51.01 | 496 |
| 55 | Bollinger reversion · 1h ⏸ | reversion | 58.24 | -41.76 | 377 | 36.6 | -43.83 | -6.65 | -45.16 | 441 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -52.03 | -8.52 | -52.83 | 582 |
| 57 | Agent (ML meta-label) | meta | 55.59 | -44.41 | 2005 | 24.6 | -29.18 | -5.61 | -31.76 | 326 |
| 58 | RSI(14) reversion · 1h | reversion | 55.56 | -44.44 | 224 | 33.0 | -42.07 | -6.07 | -45.95 | 272 |
| 59 | VWAP momentum · 1h | momentum | 55.03 | -44.97 | 1013 | 21.4 | -55.84 | -11.12 | -60.51 | 1192 |
| 60 | Z-score reversion · 1h ⏸ | reversion | 52.10 | -47.90 | 242 | 33.1 | -43.57 | -6.03 | -46.09 | 265 |
| 61 | Three white soldiers | momentum | 51.69 | -48.31 | 618 | 14.1 | -52.23 | -23.16 | -52.57 | 665 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -53.54 | -9.52 | -53.65 | 679 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -47.70 | -99.14 | 5328 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.44 | -30.43 | -84.01 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.37 | -46.66 | -94.42 | 2450 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.19 | -33.95 | -91.37 | 1950 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.03 | -44.83 | -92.21 | 2291 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.89 | -28.16 | -90.21 | 2024 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.26 | -49.97 | -98.26 | 3491 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -51.67 | -96.87 | 3389 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.87 | -40.28 | -94.00 | 2204 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.56 | -35.78 | -83.61 | 1579 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -56.19 | -99.67 | 6366 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.21 | -44.58 | -93.23 | 2536 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.49 | -94.64 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.85 | -71.79 | -99.85 | 6293 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.51 | -46.73 | -93.51 | 2285 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.95 | -26.73 | -79.02 | 1638 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.81 | -60.53 | -97.82 | 3379 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -59.06 | -99.16 | 5120 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.03 | -29.85 | -71.12 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.08 | -55.01 | -95.10 | 2730 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.71 | -39.41 | -85.94 | 1705 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -72.11 | -99.74 | 6566 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.67 | -31.77 | -91.76 | 2488 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.07 | -19.39 | -82.26 | 1949 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.44 | -34.47 | -92.56 | 2209 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.89 | -46.64 | -97.90 | 4053 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.62 | -52.24 | -90.62 | 2208 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.23 | -32.14 | -67.32 | 793 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.86 | -27.76 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.79 | -19.05 | -83.99 | 1862 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.75 | -47.11 | -97.77 | 4451 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -117.21 | -99.95 | 8432 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 20:50:05.000131+00:00 -> 2026-11-20 21:00:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
