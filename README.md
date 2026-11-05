# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T16:25:05.000105+00:00 · 48640 ticks

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

Today: 20379 decisions in 2622 calls, $0.2654 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T16:25 | 7 / 22 / 2 | AMD 16%, SOXL 15%, TECL 14% |  |
| Breezy | 2026-11-05T16:25 | 0 / 27 / 4 | cash |  |
| Boozy | 2026-11-05T16:25 | 7 / 23 / 1 | MSTR 75% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.34 | 13.35 | 0 | — | 14.88 | 5.15 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 18 | 66.7 | 13.03 | 3.20 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.02 | 4.02 | 28 | 25.0 | 12.47 | 2.52 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.07 | 0.07 | 28 | 42.9 | -1.49 | -0.34 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.01 | 0.01 | 0 | — | 3.84 | 1.18 | -6.60 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 106 | 46.2 | -11.51 | -3.01 | -12.83 | 138 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 96.84 | -3.16 | 116 | 34.5 | 4.00 | 2.16 | -3.32 | 90 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.37 | -4.62 | 0 | — | -3.49 | -1.29 | -6.35 | 1 |
| 13 | Hold SPY | benchmark | 95.34 | -4.66 | 0 | — | -3.21 | -1.38 | -5.38 | 1 |
| 14 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.34 | 0.20 | -9.18 | 220 |
| 15 | Agent (rotation) | meta | 94.17 | -5.83 | 174 | 27.6 | -7.35 | -4.65 | -10.81 | 176 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 17 | Trend pullback · 1h | trend | 92.44 | -7.56 | 105 | 22.9 | -14.91 | -5.25 | -17.67 | 79 |
| 18 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -7.34 | -0.93 | -17.57 | 8 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.55 | -9.45 | 0 | — | -6.83 | -2.13 | -10.27 | 1 |
| 21 | Hold BTC | benchmark | 90.31 | -9.69 | 0 | — | -3.66 | -0.42 | -13.31 | 1 |
| 22 | Opening range 30m | breakout | 89.08 | -10.92 | 365 | 32.9 | -15.79 | -5.18 | -17.21 | 584 |
| 23 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -14.15 | -7.98 | -14.55 | 213 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.09 | -3.15 | -14.15 | 83 |
| 25 | Daily: Bullish score | daily | 88.23 | -11.77 | 14 | 21.4 | -8.18 | -1.23 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 87.77 | -12.23 | 38 | 39.5 | -23.99 | -4.82 | -24.51 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.63 | -13.37 | 164 | 26.8 | -18.72 | -4.05 | -21.06 | 243 |
| 28 | Donchian 55/20 · 1h | breakout | 85.70 | -14.29 | 70 | 14.3 | -14.34 | -3.08 | -19.94 | 105 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -32.02 | -2.01 | -37.46 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -16.93 | -4.92 | -18.47 | 98 |
| 31 | Opening range 15m | breakout | 82.90 | -17.10 | 445 | 30.6 | -19.86 | -6.02 | -21.20 | 712 |
| 32 | Volume breakout · 1h | breakout | 81.72 | -18.28 | 144 | 27.8 | -14.55 | -3.34 | -18.36 | 96 |
| 33 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -23.99 | -4.32 | -25.24 | 375 |
| 34 | Keltner breakout · 1h | breakout | 80.98 | -19.02 | 106 | 23.6 | -24.56 | -5.18 | -24.93 | 186 |
| 35 | Connors RSI(2) · 1h | reversion | 80.95 | -19.05 | 202 | 40.1 | -21.29 | -6.84 | -22.17 | 134 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -15.13 | -2.10 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -23.56 | -3.99 | -26.26 | 269 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -17.04 | -2.64 | -18.66 | 152 |
| 39 | Ichimoku · 1h | trend | 78.41 | -21.59 | 93 | 15.1 | -24.26 | -4.94 | -28.54 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 78.20 | -21.80 | 165 | 23.6 | -22.53 | -4.52 | -26.49 | 252 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -25.22 | -3.63 | -28.54 | 446 |
| 42 | Heikin-Ashi · 1h | trend | 76.12 | -23.88 | 385 | 23.1 | -42.95 | -8.83 | -44.07 | 677 |
| 43 | EMA 20/50 cross · 1h | trend | 75.89 | -24.11 | 101 | 10.9 | -21.17 | -3.67 | -28.24 | 132 |
| 44 | MACD zero-line · 1h | trend | 74.84 | -25.16 | 153 | 16.3 | -29.36 | -5.88 | -29.84 | 215 |
| 45 | Williams %R · 1h | reversion | 74.56 | -25.44 | 298 | 46.6 | -34.29 | -6.15 | -35.36 | 522 |
| 46 | Triple EMA stack · 1h | trend | 74.28 | -25.72 | 141 | 14.9 | -30.64 | -6.09 | -33.18 | 212 |
| 47 | Supertrend · 1h | trend | 73.54 | -26.46 | 165 | 13.3 | -30.74 | -5.63 | -33.58 | 233 |
| 48 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -37.95 | -6.76 | -38.84 | 478 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -23.88 | -3.74 | -24.89 | 216 |
| 50 | RSI momentum · 1h | momentum | 73.12 | -26.88 | 157 | 12.7 | -30.56 | -5.79 | -32.33 | 224 |
| 51 | Bollinger reversion · 1h | reversion | 72.97 | -27.03 | 237 | 40.1 | -32.20 | -6.16 | -32.64 | 368 |
| 52 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -33.48 | -4.76 | -36.81 | 32 |
| 53 | Donchian 20/10 · 1h | breakout | 71.64 | -28.36 | 139 | 20.1 | -31.45 | -5.67 | -34.22 | 219 |
| 54 | OBV trend · 1h | momentum | 71.60 | -28.40 | 263 | 17.5 | -35.27 | -7.30 | -35.33 | 300 |
| 55 | ROC + volume · 1h | momentum | 71.32 | -28.68 | 339 | 25.7 | -37.13 | -7.19 | -38.49 | 386 |
| 56 | Candlestick reversal · 1h | reversion | 67.60 | -32.40 | 378 | 29.9 | -35.84 | -6.61 | -36.86 | 554 |
| 57 | VWAP momentum · 1h | momentum | 67.53 | -32.47 | 756 | 22.2 | -55.07 | -11.80 | -55.87 | 1226 |
| 58 | Three white soldiers | momentum | 67.36 | -32.64 | 445 | 16.2 | -47.16 | -21.84 | -47.20 | 635 |
| 59 | EMA 9/21 cross · 1h | trend | 67.31 | -32.69 | 240 | 10.0 | -41.25 | -8.16 | -41.28 | 337 |
| 60 | Agent (ML meta-label) | meta | 66.51 | -33.49 | 1476 | 22.2 | -3.60 | -0.50 | -16.02 | 310 |
| 61 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -26.93 | -4.17 | -29.66 | 223 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -41.18 | -2.58 | -54.60 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.36 | -98.95 | 5182 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.67 | -25.20 | -79.95 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.36 | -47.26 | -93.36 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.64 | -30.69 | -88.72 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.52 | -38.50 | -90.52 | 2286 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.93 | -32.93 | -90.93 | 2246 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -53.96 | -97.64 | 3438 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.14 | -57.96 | -96.14 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.84 | -33.61 | -93.88 | 2473 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.87 | -36.77 | -81.87 | 1646 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.50 | -54.46 | -99.51 | 5898 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.52 | -42.56 | -92.63 | 2578 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.94 | -38.09 | -95.95 | 3440 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -71.15 | -99.80 | 6157 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.51 | -43.06 | -91.51 | 2239 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.37 | -25.50 | -74.73 | 1553 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -62.05 | -97.72 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.73 | -60.68 | -98.75 | 4857 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.73 | -27.10 | -69.78 | 1189 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.48 | -53.72 | -94.49 | 2731 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.46 | -35.93 | -84.46 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -70.33 | -99.64 | 6323 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.75 | -30.93 | -89.09 | 2277 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.07 | -19.37 | -77.43 | 1730 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.01 | -36.61 | -91.22 | 2235 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.55 | -50.19 | -96.59 | 3843 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.21 | -51.86 | -89.21 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.18 | -27.17 | -65.51 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.21 | -24.28 | -73.80 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.94 | -18.05 | -77.56 | 1651 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.16 | -50.69 | -97.23 | 4309 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -92.74 | -99.93 | 8209 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T16:20 | Agent (ML meta-label) | buy | SQQQ | 16.62 | — | entry |
| 2026-11-05T16:20 | Keltner breakout · 1h | sell | AAPL | 20.23 | -0.45 | stop-loss |
| 2026-11-05T16:20 | Bollinger breakout · 1h | sell | AAPL | 19.37 | -0.43 | stop-loss |
| 2026-11-05T16:20 | Three white soldiers | buy | TSLA | 16.83 | — | entry signal |
| 2026-11-05T16:15 | Agent (ML meta-label) | sell | SQQQ | 16.81 | 0.09 | selected signal exited |
| 2026-11-05T16:15 | Gap and go | sell | SQQQ | 24.96 | 1.57 | stop-loss |
| 2026-11-05T16:05 | EMA 20/50 cross · 1h | sell | XRP-USD | 18.92 | -0.47 | stop-loss |
| 2026-11-05T15:55 | Daily: Bullish score | buy | TSLA | 4.54 | — | rebalance up |
| 2026-11-05T15:55 | Daily: Momentum burst | sell | MSFT | 18.56 | -0.70 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:55 | Daily: Momentum burst | sell | LABU | 17.54 | -1.72 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:55 | Daily: Momentum burst | sell | ETHU | 16.94 | -2.32 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:55 | Stochastic reversion · 1h | sell | TNA | 19.69 | -1.47 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:55 | Stochastic reversion · 1h | sell | NVDA | 19.66 | -0.36 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:55 | Stochastic reversion · 1h | sell | IWM | 21.02 | -0.53 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:51 | MFI reversion · 1h | sell | LABU | 18.48 | -2.52 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:51 | MFI reversion · 1h | sell | AMZN | 19.25 | -1.25 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:51 | Z-score reversion · 1h | sell | GOOGL | 17.71 | -0.76 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:51 | Donchian 55/20 · 1h | sell | MSFT | 21.23 | -0.52 | stop-loss |
| 2026-11-05T15:51 | Donchian 20/10 · 1h | buy | AAPL | 3.61 | — | rebalance up |
| 2026-11-05T15:51 | Donchian 20/10 · 1h | sell | MSFT | 17.87 | -0.36 | stop-loss |
| 2026-11-05T15:51 | OBV trend · 1h | sell | MSFT | 14.32 | -0.46 | stop-loss |
| 2026-11-05T15:51 | RSI momentum · 1h | sell | MSFT | 18.26 | -0.37 | stop-loss |
| 2026-11-05T15:51 | ROC + volume · 1h | buy | AAPL | 3.58 | — | rebalance up |
| 2026-11-05T15:51 | Ichimoku · 1h | sell | MSFT | 19.59 | -0.54 | stop-loss |
| 2026-11-05T15:51 | MACD zero-line · 1h | sell | MSFT | 18.76 | -0.45 | stop-loss |
| 2026-11-05T15:51 | Triple EMA stack · 1h | sell | MSFT | 18.51 | -0.26 | stop-loss |
| 2026-11-05T15:51 | EMA 20/50 cross · 1h | buy | XRP-USD | 3.85 | — | rebalance up |
| 2026-11-05T15:51 | EMA 20/50 cross · 1h | sell | MSFT | 15.25 | -0.40 | stop-loss |
| 2026-11-05T15:51 | EMA 9/21 cross · 1h | sell | MSFT | 16.78 | -0.25 | stop-loss |
| 2026-11-05T15:45 | EMA 20/50 cross · 1h | sell | LABU | 14.51 | -1.45 | stop-loss |
| 2026-11-05T15:45 | EMA 9/21 cross · 1h | buy | MSFT | 3.40 | — | rebalance up |
| 2026-11-05T15:45 | EMA 9/21 cross · 1h | buy | AMZN | 3.42 | — | rebalance up |
| 2026-11-05T15:45 | EMA 9/21 cross · 1h | buy | AAPL | 3.43 | — | rebalance up |
| 2026-11-05T15:45 | EMA 9/21 cross · 1h | sell | GOOGL | 13.44 | -0.22 | stop-loss |
| 2026-11-05T15:40 | Stochastic reversion · 1h | sell | SPY | 21.08 | -0.54 | stop-loss |
| 2026-11-05T15:35 | Agent (ML meta-label) | buy | SQQQ | 4.29 | — | rebalance up |
| 2026-11-05T15:35 | Agent (ML meta-label) | buy | NVDA | 4.16 | — | rebalance up |
| 2026-11-05T15:35 | Agent (ML meta-label) | buy | MSFT | 7.04 | — | rebalance up |
| 2026-11-05T15:35 | Agent (ML meta-label) | buy | AAPL | 7.06 | — | rebalance up |
| 2026-11-05T15:35 | Agent (ML meta-label) | sell | TNA | 4.47 | 0.01 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 16:25:05.000105+00:00 -> 2026-11-05 16:35:05.000105+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 16:25:05.000105+00:00 -> 2026-11-05 16:35:05.000105+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 16:25:05.000105+00:00 -> 2026-11-05 16:35:05.000105+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
