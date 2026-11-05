# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T17:55:05.000147+00:00 · 48725 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.06 (-10.94%)

Closed trades 147, win rate 37.4%, fees £4.06, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-05 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 28137 decisions in 2877 calls, $0.3565 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T17:55 | 1 / 11 / 18 | cash |  |
| Breezy | 2026-11-05T17:55 | 0 / 20 / 10 | cash |  |
| Boozy | 2026-11-05T17:55 | 2 / 22 / 6 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.65 | 12.65 | 18 | 66.7 | 16.35 | 3.28 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.47 | 12.47 | 0 | — | 13.97 | 4.83 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.93 | 6.93 | 28 | 25.0 | 15.77 | 2.70 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.86 | 2.86 | 28 | 42.9 | 1.39 | 0.46 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.11 | -0.89 | 0 | — | 3.06 | 0.95 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.29 | -1.71 | 106 | 46.2 | -12.40 | -3.23 | -12.83 | 142 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.55 | -2.45 | 116 | 34.5 | 4.76 | 2.45 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.24 | -4.75 | 0 | — | -3.49 | -1.29 | -6.35 | 1 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.34 | 0.20 | -9.18 | 220 |
| 14 | Agent (rotation) | meta | 94.80 | -5.20 | 174 | 27.6 | -6.69 | -3.83 | -10.81 | 176 |
| 15 | Hold SPY | benchmark | 94.25 | -5.75 | 0 | — | -4.23 | -1.67 | -5.57 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 17 | Trend pullback · 1h | trend | 92.32 | -7.68 | 105 | 22.9 | -15.18 | -5.39 | -17.86 | 81 |
| 18 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -10.91 | -1.25 | -17.57 | 8 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.37 | -9.63 | 0 | — | -6.47 | -2.00 | -10.27 | 1 |
| 21 | Opening range 30m | breakout | 89.70 | -10.30 | 365 | 32.9 | -15.17 | -4.90 | -17.21 | 584 |
| 22 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -14.40 | -8.12 | -14.79 | 214 |
| 23 | Hold BTC | benchmark | 88.98 | -11.02 | 0 | — | -5.08 | -0.63 | -13.31 | 1 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.34 | -3.24 | -14.15 | 86 |
| 25 | Daily: Bullish score | daily | 88.32 | -11.68 | 14 | 21.4 | -7.96 | -1.19 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 87.10 | -12.90 | 38 | 39.5 | -24.75 | -4.92 | -25.35 | 65 |
| 27 | Parabolic SAR · 1h | trend | 87.10 | -12.90 | 166 | 27.1 | -18.24 | -4.00 | -21.06 | 243 |
| 28 | Donchian 55/20 · 1h | breakout | 86.14 | -13.86 | 71 | 14.1 | -13.70 | -2.92 | -19.94 | 105 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -33.95 | -2.12 | -37.46 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.09 | -5.34 | -19.03 | 98 |
| 31 | Opening range 15m | breakout | 83.49 | -16.51 | 445 | 30.6 | -19.28 | -5.73 | -21.20 | 712 |
| 32 | Volume breakout · 1h | breakout | 82.29 | -17.71 | 144 | 27.8 | -13.95 | -3.18 | -18.40 | 96 |
| 33 | Keltner breakout · 1h | breakout | 81.54 | -18.46 | 106 | 23.6 | -24.75 | -5.28 | -25.37 | 188 |
| 34 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -27.78 | -4.54 | -27.92 | 379 |
| 35 | Connors RSI(2) · 1h | reversion | 80.73 | -19.27 | 202 | 40.1 | -21.45 | -6.85 | -22.17 | 135 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -15.86 | -2.16 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -23.96 | -3.88 | -26.45 | 263 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -19.76 | -2.83 | -19.92 | 150 |
| 39 | Bollinger breakout · 1h | breakout | 78.75 | -21.25 | 165 | 23.6 | -23.20 | -4.75 | -26.52 | 252 |
| 40 | Ichimoku · 1h | trend | 78.28 | -21.72 | 94 | 14.9 | -24.37 | -4.94 | -28.68 | 131 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -25.95 | -3.88 | -28.54 | 446 |
| 42 | Heikin-Ashi · 1h | trend | 76.70 | -23.30 | 385 | 23.1 | -42.50 | -8.82 | -44.06 | 676 |
| 43 | EMA 20/50 cross · 1h | trend | 76.22 | -23.78 | 102 | 10.8 | -21.12 | -3.77 | -27.81 | 134 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -28.45 | -5.83 | -29.20 | 215 |
| 45 | Triple EMA stack · 1h | trend | 74.63 | -25.37 | 142 | 14.8 | -31.05 | -6.33 | -33.27 | 211 |
| 46 | Supertrend · 1h | trend | 73.71 | -26.29 | 165 | 13.3 | -30.80 | -5.70 | -33.58 | 234 |
| 47 | RSI momentum · 1h | momentum | 73.58 | -26.42 | 158 | 12.7 | -30.93 | -5.89 | -32.33 | 226 |
| 48 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -37.74 | -6.78 | -38.83 | 478 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -26.47 | -4.29 | -26.67 | 217 |
| 50 | Bollinger reversion · 1h | reversion | 72.84 | -27.16 | 237 | 40.1 | -32.54 | -6.19 | -32.87 | 364 |
| 51 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -34.75 | -4.86 | -37.00 | 32 |
| 52 | Donchian 20/10 · 1h | breakout | 72.00 | -28.00 | 140 | 20.0 | -31.72 | -5.83 | -34.25 | 219 |
| 53 | Williams %R · 1h ⏸ | reversion | 71.97 | -28.03 | 310 | 44.8 | -36.82 | -6.36 | -37.05 | 530 |
| 54 | ROC + volume · 1h | momentum | 71.57 | -28.43 | 339 | 25.7 | -36.51 | -7.12 | -38.26 | 385 |
| 55 | OBV trend · 1h | momentum | 71.40 | -28.60 | 264 | 17.4 | -35.09 | -7.47 | -35.15 | 299 |
| 56 | VWAP momentum · 1h | momentum | 68.02 | -31.98 | 756 | 22.2 | -55.18 | -11.94 | -56.20 | 1224 |
| 57 | EMA 9/21 cross · 1h | trend | 67.73 | -32.27 | 240 | 10.0 | -40.44 | -8.12 | -40.96 | 337 |
| 58 | Three white soldiers | momentum | 67.20 | -32.80 | 446 | 16.1 | -47.28 | -21.90 | -47.28 | 635 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -27.56 | -4.34 | -29.66 | 206 |
| 60 | Candlestick reversal · 1h | reversion | 65.62 | -34.38 | 386 | 29.3 | -36.91 | -6.62 | -36.92 | 557 |
| 61 | Agent (ML meta-label) | meta | 65.52 | -34.48 | 1492 | 22.3 | -5.45 | -0.95 | -17.64 | 319 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -42.85 | -2.70 | -54.60 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.92 | -98.93 | 5143 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.83 | -25.31 | -80.06 | 1411 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.35 | -46.44 | -93.35 | 2504 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.75 | -30.74 | -88.86 | 1899 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.41 | -37.88 | -90.48 | 2284 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.79 | -32.63 | -90.85 | 2243 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.61 | -52.58 | -97.61 | 3417 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.16 | -57.55 | -96.16 | 3372 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.85 | -33.91 | -93.89 | 2466 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.71 | -36.10 | -81.75 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -53.45 | -99.51 | 5916 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.42 | -41.62 | -92.57 | 2563 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -38.02 | -95.93 | 3438 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.54 | -99.80 | 6155 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.49 | -42.54 | -91.49 | 2233 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.31 | -25.20 | -74.72 | 1543 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -60.35 | -97.72 | 3507 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.76 | -60.03 | -98.76 | 4842 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.02 | -27.68 | -70.03 | 1181 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.46 | -53.45 | -94.46 | 2718 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.42 | -35.58 | -84.42 | 1778 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.36 | -99.64 | 6312 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.01 | -30.41 | -89.06 | 2262 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.55 | -19.25 | -77.55 | 1723 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.22 | -36.02 | -91.23 | 2226 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.56 | -50.39 | -96.59 | 3842 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.13 | -51.81 | -89.13 | 2139 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.43 | -27.61 | -65.76 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.13 | -23.80 | -73.91 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.53 | -17.72 | -77.53 | 1646 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.22 | -48.48 | -97.23 | 4309 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -94.28 | -99.92 | 8189 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T17:55 | Agent (ML meta-label) | buy | SPY | 5.96 | — | entry |
| 2026-11-05T17:40 | Agent (ML meta-label) | sell | SPY | 5.46 | -0.02 | selected signal exited |
| 2026-11-05T17:40 | Agent (ML meta-label) | sell | GOOGL | 5.45 | -0.02 | selected signal exited |
| 2026-11-05T17:40 | Williams %R · 1h | sell | UPRO | 6.00 | -0.21 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | TQQQ | 5.95 | -0.27 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | TECL | 5.88 | -0.33 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | SPY | 6.14 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | SOXL | 5.70 | -0.51 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | QQQ | 6.13 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | MSTR | 6.04 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | META | 6.17 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | LABU | 5.86 | -0.35 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | COIN | 6.04 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | BITX | 6.05 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Williams %R · 1h | sell | AMD | 6.02 | -0.20 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T17:40 | Candlestick reversal · 1h | sell | UPRO | 9.34 | -0.19 | stop-loss |
| 2026-11-05T17:35 | Agent (ML meta-label) | buy | SPY | 5.47 | — | entry |
| 2026-11-05T17:35 | Agent (ML meta-label) | buy | GOOGL | 5.47 | — | entry |
| 2026-11-05T17:35 | Agent (ML meta-label) | sell | TECL | 4.82 | 0.01 | selected signal exited |
| 2026-11-05T17:35 | Ichimoku · 1h | sell | AAPL | 19.39 | -0.50 | stop-loss |
| 2026-11-05T17:35 | MACD zero-line · 1h | sell | AAPL | 18.71 | -0.47 | stop-loss |
| 2026-11-05T17:30 | Agent (ML meta-label) | buy | SQQQ | 5.97 | — | entry |
| 2026-11-05T17:30 | Agent (ML meta-label) | buy | QQQ | 5.97 | — | entry |
| 2026-11-05T17:30 | Agent (ML meta-label) | sell | TSLA | 4.98 | -0.13 | selected signal exited |
| 2026-11-05T17:30 | Agent (ML meta-label) | sell | SPY | 5.98 | -0.02 | selected signal exited |
| 2026-11-05T17:30 | Agent (ML meta-label) | sell | SOXL | 5.38 | -0.12 | selected signal exited |
| 2026-11-05T17:30 | Candlestick reversal · 1h | buy | UPRO | 4.71 | — | rebalance up |
| 2026-11-05T17:30 | Candlestick reversal · 1h | buy | TECL | 4.81 | — | rebalance up |
| 2026-11-05T17:30 | Candlestick reversal · 1h | buy | SPY | 4.63 | — | rebalance up |
| 2026-11-05T17:30 | Candlestick reversal · 1h | buy | PLTR | 4.65 | — | rebalance up |
| 2026-11-05T17:30 | Candlestick reversal · 1h | buy | MSTR | 4.71 | — | rebalance up |
| 2026-11-05T17:30 | Candlestick reversal · 1h | buy | GOOGL | 4.58 | — | rebalance up |
| 2026-11-05T17:30 | Candlestick reversal · 1h | buy | BITX | 4.72 | — | rebalance up |
| 2026-11-05T17:30 | Candlestick reversal · 1h | sell | TSLA | 4.70 | -0.13 | exit signal |
| 2026-11-05T17:30 | Candlestick reversal · 1h | sell | TQQQ | 4.66 | -0.17 | exit signal |
| 2026-11-05T17:30 | Candlestick reversal · 1h | sell | SOXL | 4.51 | -0.32 | exit signal |
| 2026-11-05T17:30 | Candlestick reversal · 1h | sell | QQQ | 4.77 | -0.06 | exit signal |
| 2026-11-05T17:30 | Candlestick reversal · 1h | sell | NVDA | 4.76 | -0.07 | exit signal |
| 2026-11-05T17:30 | Candlestick reversal · 1h | sell | ETHU | 4.69 | -0.14 | exit signal |
| 2026-11-05T17:30 | Candlestick reversal · 1h | sell | COIN | 4.71 | -0.12 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 17:55:05.000147+00:00 -> 2026-11-05 18:05:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 17:55:05.000147+00:00 -> 2026-11-05 18:05:05.000147+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 17:55:05.000147+00:00 -> 2026-11-05 18:05:05.000147+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
