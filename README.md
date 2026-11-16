# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T20:40:05.000135+00:00 · 62317 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.11 (-13.89%)

Closed trades 203, win rate 36.5%, fees £5.77, max drawdown -15.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-16 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 38529 decisions in 3249 calls, $0.4775 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T20:40 | 0 / 11 / 19 | cash |  |
| Breezy | 2026-11-16T20:40 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-16T20:40 | 3 / 22 / 5 | BITX 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.82 | +5.11% | 10 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| CCI reversion | SOXL | 2.19 | +16.29% | 10 |
| Bollinger reversion | TSLA | 2.18 | +2.18% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.95 | 17.95 | 0 | — | 13.85 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.81 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.45 | 11.45 | 23 | 65.2 | 16.75 | 3.42 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.43 | 3.43 | 0 | — | 5.18 | 1.44 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.01 | 2.01 | 35 | 40.0 | 0.55 | 0.25 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.52 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.08 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.31 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.45 | -3.55 | 0 | — | -2.78 | -0.86 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.02 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.05 | -5.95 | 0 | — | -6.44 | -1.69 | -8.27 | 1 |
| 14 | Agent (rotation) | meta | 94.04 | -5.96 | 195 | 29.7 | -2.62 | -0.91 | -8.15 | 158 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.23 | -5.99 | 22 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.44 | -7.56 | 23 | 17.4 | -8.74 | -7.21 | -9.27 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.83 | -8.17 | 0 | — | -6.88 | -1.87 | -10.92 | 1 |
| 18 | Copy: Insider buying | copy | 91.56 | -8.44 | 47 | 42.6 | -10.19 | -2.05 | -14.95 | 62 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.36 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.99 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -8.45 | -2.40 | -16.01 | 79 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.69 | -13.31 | 16 | 18.8 | -4.54 | -0.70 | -19.56 | 15 |
| 24 | Opening range 30m | breakout | 86.23 | -13.77 | 436 | 33.5 | -10.64 | -3.41 | -14.11 | 583 |
| 25 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.11 | -7.03 | -15.83 | 196 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.21 | -16.78 | 96 |
| 27 | Parabolic SAR · 1h | trend | 83.21 | -16.79 | 180 | 28.3 | -17.93 | -3.94 | -24.65 | 216 |
| 28 | Keltner breakout · 1h | breakout | 80.67 | -19.33 | 121 | 25.6 | -19.12 | -4.41 | -25.84 | 157 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -22.26 | -4.98 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.23 | -19.77 | 213 | 39.9 | -14.29 | -6.33 | -14.88 | 98 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 161 | 28.6 | -16.38 | -5.22 | -21.95 | 85 |
| 32 | Max aggression: 5-day momentum | meta | 78.43 | -21.57 | 21 | 42.9 | -48.39 | -3.26 | -55.24 | 23 |
| 33 | Opening range 15m | breakout | 78.26 | -21.74 | 530 | 31.5 | -17.23 | -4.67 | -21.37 | 692 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.49 | -22.51 | 2 | 0.0 | -14.36 | -1.77 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 75.95 | -24.05 | 2 | 0.0 | -14.50 | -1.97 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.37 | -31.62 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 75.24 | -24.76 | 30 | 26.7 | -23.10 | -0.83 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.82 | -25.18 | 207 | 19.3 | -23.91 | -3.71 | -34.65 | 258 |
| 39 | Bollinger breakout · 1h | breakout | 74.48 | -25.52 | 184 | 22.3 | -23.63 | -4.98 | -31.78 | 234 |
| 40 | Stochastic reversion · 1h ⏸ | reversion | 74.07 | -25.93 | 333 | 44.1 | -31.88 | -4.69 | -32.87 | 416 |
| 41 | MACD zero-line · 1h | trend | 72.59 | -27.41 | 173 | 18.5 | -24.86 | -4.93 | -31.62 | 194 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -26.18 | -3.73 | -29.42 | 165 |
| 43 | Heikin-Ashi · 1h | trend | 71.86 | -28.14 | 459 | 23.3 | -39.01 | -7.51 | -43.26 | 637 |
| 44 | Supertrend · 1h | trend | 71.51 | -28.49 | 187 | 16.0 | -32.43 | -5.56 | -39.67 | 200 |
| 45 | RSI momentum · 1h | momentum | 71.33 | -28.67 | 175 | 14.3 | -27.32 | -4.34 | -38.07 | 204 |
| 46 | Triple EMA stack · 1h | trend | 71.30 | -28.70 | 154 | 14.9 | -26.92 | -4.59 | -37.77 | 192 |
| 47 | EMA 20/50 cross · 1h | trend | 70.95 | -29.05 | 112 | 9.8 | -35.45 | -9.74 | -38.88 | 113 |
| 48 | MACD cross · 1h | trend | 70.91 | -29.09 | 402 | 22.6 | -33.42 | -4.83 | -43.17 | 473 |
| 49 | ROC + volume · 1h | momentum | 70.85 | -29.15 | 404 | 28.5 | -27.97 | -4.61 | -37.95 | 357 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.94 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.26 | -30.74 | 303 | 19.1 | -29.61 | -5.16 | -39.75 | 261 |
| 52 | Donchian 20/10 · 1h | breakout | 67.74 | -32.26 | 157 | 18.5 | -30.03 | -4.95 | -39.25 | 206 |
| 53 | CCI reversion · 1h | reversion | 67.73 | -32.27 | 375 | 41.6 | -40.12 | -6.52 | -42.07 | 458 |
| 54 | Bollinger reversion · 1h ⏸ | reversion | 66.56 | -33.45 | 333 | 39.0 | -36.25 | -5.47 | -36.96 | 406 |
| 55 | EMA 9/21 cross · 1h | trend | 64.35 | -35.65 | 271 | 11.4 | -35.15 | -5.93 | -44.37 | 321 |
| 56 | Williams %R · 1h | reversion | 63.93 | -36.07 | 418 | 41.1 | -44.45 | -7.49 | -45.12 | 546 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -21.69 | -3.23 | -26.98 | 330 |
| 58 | Z-score reversion · 1h | reversion | 59.47 | -40.52 | 221 | 35.7 | -34.93 | -4.82 | -36.18 | 242 |
| 59 | RSI(14) reversion · 1h | reversion | 59.25 | -40.75 | 202 | 32.2 | -39.83 | -5.82 | -42.15 | 245 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.61 | -9.63 | -57.26 | 1213 |
| 61 | Candlestick reversal · 1h ⏸ | reversion | 57.30 | -42.70 | 537 | 27.0 | -45.76 | -8.32 | -46.11 | 622 |
| 62 | Three white soldiers | momentum | 56.57 | -43.43 | 570 | 14.7 | -49.59 | -22.03 | -49.59 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -42.50 | -99.04 | 5310 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.64 | -26.01 | -81.64 | 1437 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.11 | -44.51 | -94.11 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.01 | -32.39 | -90.02 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.44 | -41.42 | -91.44 | 2324 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.98 | -31.03 | -89.99 | 2146 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.97 | -48.48 | -97.97 | 3471 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -56.53 | -96.49 | 3438 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.46 | -37.94 | -93.47 | 2265 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.90 | -34.16 | -82.90 | 1639 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -54.79 | -99.59 | 6041 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -42.87 | -92.22 | 2585 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.16 | -36.89 | -95.16 | 3347 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.77 | -99.81 | 6155 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.47 | -43.52 | -92.47 | 2266 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.39 | -26.28 | -76.39 | 1647 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -62.15 | -97.64 | 3472 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -57.31 | -98.98 | 4943 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.45 | -27.25 | -68.45 | 1225 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -56.88 | -94.74 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -38.24 | -84.71 | 1745 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -70.13 | -99.69 | 6380 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.48 | -30.60 | -90.49 | 2336 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.58 | -18.76 | -79.58 | 1812 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.99 | -36.36 | -91.02 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.43 | -45.83 | -97.43 | 3903 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.15 | -60.94 | -89.15 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -30.06 | -66.40 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.96 | -23.53 | -72.20 | 1246 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.34 | -17.77 | -80.60 | 1760 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -46.71 | -97.56 | 4360 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.54 | -99.94 | 8392 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T20:40 | Agent (aggressive) | sell | COIN | 41.62 | -0.09 | selected signal exited |
| 2026-11-16T20:40 | Agent | sell | COIN | 17.12 | -0.04 | selected signal exited |
| 2026-11-16T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 92.12 | — | entry |
| 2026-11-16T20:30 | Williams %R · 1h | buy | COIN | 5.83 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | MSTR | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | LABU | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | BITX | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | AMZN | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | sell | ETHU | 3.05 | 0.01 | rebalance down |
| 2026-11-16T20:30 | RSI(14) reversion · 1h | buy | COIN | 14.89 | — | entry signal |
| 2026-11-16T20:30 | EMA 20/50 cross · 1h | sell | META | 17.70 | -0.19 | exit signal |
| 2026-11-16T20:25 | Three white soldiers | sell | XRP-USD | 14.05 | -0.13 | exit signal |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | TNA | 5.73 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | SOXL | 5.61 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | NVDA | 5.74 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | MSFT | 5.75 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | LABU | 5.73 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | BTC-USD | 5.76 | 0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | BITX | 5.79 | 0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | AMD | 5.71 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:10 | Agent | sell | TSLA | 17.20 | 0.04 | selected signal exited |
| 2026-11-16T20:00 | Agent | sell | SOXL | 17.29 | 0.08 | selected signal exited |
| 2026-11-16T20:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 5.69 | — | entry signal |
| 2026-11-16T20:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 12.89 | — | entry signal |
| 2026-11-16T20:00 | Three white soldiers | buy | XRP-USD | 14.17 | — | entry signal |
| 2026-11-16T19:50 | Agent (aggressive) | buy | COIN | 41.72 | — | following MACD cross |
| 2026-11-16T19:50 | Agent | buy | TSLA | 17.16 | — | following Bollinger reversion |
| 2026-11-16T19:50 | Agent | buy | COIN | 17.16 | — | following MACD cross |
| 2026-11-16T19:45 | Agent (aggressive) | sell | COIN | 41.69 | -0.06 | selected signal exited |
| 2026-11-16T19:45 | Agent | sell | COIN | 17.12 | -0.02 | selected signal exited |
| 2026-11-16T19:45 | Candlestick reversal · 1h | sell | MSTR | 5.72 | -0.02 | target is flat |
| 2026-11-16T19:45 | Candlestick reversal · 1h | sell | IWM | 5.76 | -0.01 | target is flat |
| 2026-11-16T19:45 | OBV trend · 1h | buy | META | 17.29 | — | entry |
| 2026-11-16T19:31 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 100.98 | — | entry |
| 2026-11-16T19:31 | CCI reversion · 1h | buy | AMD | 16.99 | — | entry signal |
| 2026-11-16T19:31 | Z-score reversion · 1h | buy | ETHU | 14.96 | — | entry signal |
| 2026-11-16T19:31 | Connors RSI(2) · 1h | buy | AAPL | 20.07 | — | entry signal |
| 2026-11-16T19:31 | RSI(14) reversion · 1h | buy | NVDA | 14.90 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | TNA | 5.75 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | SOXL | 5.77 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 20:40:05.000135+00:00 -> 2026-11-16 20:50:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 20:40:05.000135+00:00 -> 2026-11-16 20:50:05.000135+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
