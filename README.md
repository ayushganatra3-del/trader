# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T15:25:05.000161+00:00 · 48590 ticks

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

Today: 15798 decisions in 2472 calls, $0.2117 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T15:25 | 0 / 4 / 26 | cash |  |
| Breezy | 2026-11-05T15:25 | 0 / 18 / 12 | cash |  |
| Boozy | 2026-11-05T15:25 | 4 / 20 / 6 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.96 | 13.96 | 0 | — | 15.45 | 5.31 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.20 | 10.21 | 18 | 66.7 | 11.89 | 3.12 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.60 | 4.60 | 28 | 25.0 | 13.07 | 2.56 | -8.66 | 43 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 101.02 | 1.01 | 0 | — | 4.87 | 1.47 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.62 | 0.62 | 28 | 42.9 | -0.96 | -0.18 | -9.64 | 29 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 106 | 46.2 | -11.51 | -3.01 | -12.83 | 138 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 96.99 | -3.01 | 116 | 34.5 | 4.13 | 2.22 | -3.32 | 90 |
| 11 | Hold SPY | benchmark | 95.63 | -4.37 | 0 | — | -3.04 | -1.34 | -4.33 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 95.39 | -4.61 | 0 | — | -3.49 | -1.29 | -6.35 | 1 |
| 14 | Gap and go | momentum | 95.02 | -4.98 | 160 | 28.8 | 0.19 | 0.15 | -9.18 | 220 |
| 15 | Agent (rotation) | meta | 94.66 | -5.34 | 174 | 27.6 | -6.25 | -3.97 | -9.72 | 167 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 17 | Trend pullback · 1h | trend | 92.44 | -7.56 | 105 | 22.9 | -14.91 | -5.25 | -17.67 | 79 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.36 | -7.64 | 0 | — | -4.96 | -1.75 | -8.26 | 1 |
| 19 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -7.99 | -1.00 | -13.83 | 8 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Hold BTC | benchmark | 89.97 | -10.03 | 0 | — | -4.09 | -0.49 | -13.22 | 1 |
| 22 | Opening range 30m | breakout | 89.20 | -10.80 | 365 | 32.9 | -15.68 | -5.13 | -17.21 | 584 |
| 23 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -13.81 | -7.71 | -14.21 | 212 |
| 24 | Copy: Insider buying | copy | 88.79 | -11.21 | 38 | 39.5 | -22.79 | -4.62 | -23.68 | 65 |
| 25 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.30 | -3.23 | -14.15 | 84 |
| 26 | Daily: Bullish score | daily | 88.13 | -11.87 | 14 | 21.4 | -7.90 | -1.18 | -16.58 | 14 |
| 27 | Parabolic SAR · 1h | trend | 86.79 | -13.21 | 164 | 26.8 | -17.92 | -3.78 | -20.87 | 244 |
| 28 | Donchian 55/20 · 1h | breakout | 86.27 | -13.73 | 69 | 14.5 | -14.05 | -3.11 | -19.86 | 105 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -32.44 | -2.04 | -36.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -16.79 | -4.84 | -18.47 | 98 |
| 31 | Opening range 15m | breakout | 83.02 | -16.98 | 445 | 30.6 | -19.76 | -5.97 | -21.20 | 712 |
| 32 | Stochastic reversion · 1h | reversion | 82.78 | -17.22 | 251 | 47.4 | -23.92 | -4.42 | -24.74 | 381 |
| 33 | Volume breakout · 1h | breakout | 81.85 | -18.15 | 144 | 27.8 | -14.42 | -3.30 | -18.36 | 95 |
| 34 | Keltner breakout · 1h | breakout | 81.40 | -18.60 | 105 | 23.8 | -23.90 | -4.98 | -25.77 | 188 |
| 35 | Connors RSI(2) · 1h | reversion | 80.60 | -19.40 | 202 | 40.1 | -21.64 | -6.86 | -21.64 | 132 |
| 36 | MFI reversion · 1h | reversion | 80.24 | -19.76 | 326 | 34.0 | -18.34 | -2.79 | -18.63 | 149 |
| 37 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -13.83 | -2.00 | -21.44 | 1 |
| 38 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -23.78 | -4.07 | -25.93 | 268 |
| 39 | Ichimoku · 1h | trend | 78.82 | -21.18 | 92 | 15.2 | -23.87 | -4.91 | -28.24 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 78.60 | -21.40 | 164 | 23.8 | -22.35 | -4.52 | -26.25 | 252 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 282 | 45.7 | -24.50 | -3.53 | -28.54 | 446 |
| 42 | EMA 20/50 cross · 1h | trend | 77.07 | -22.93 | 98 | 10.2 | -20.24 | -3.66 | -26.52 | 134 |
| 43 | Heikin-Ashi · 1h | trend | 76.18 | -23.82 | 384 | 22.9 | -43.01 | -8.85 | -44.18 | 678 |
| 44 | MACD zero-line · 1h | trend | 75.10 | -24.90 | 152 | 16.4 | -29.26 | -5.90 | -29.38 | 216 |
| 45 | Triple EMA stack · 1h | trend | 74.77 | -25.23 | 140 | 15.0 | -28.47 | -4.86 | -33.43 | 207 |
| 46 | Williams %R · 1h | reversion | 74.56 | -25.44 | 297 | 46.5 | -34.30 | -6.15 | -35.37 | 523 |
| 47 | Daily: Momentum burst | daily | 74.23 | -25.77 | 23 | 13.0 | -32.87 | -4.67 | -35.08 | 32 |
| 48 | Supertrend · 1h | trend | 73.87 | -26.13 | 152 | 13.8 | -30.46 | -5.62 | -33.18 | 232 |
| 49 | RSI momentum · 1h | momentum | 73.49 | -26.51 | 156 | 12.8 | -31.13 | -5.90 | -32.11 | 225 |
| 50 | Z-score reversion · 1h | reversion | 73.42 | -26.58 | 158 | 36.1 | -20.86 | -2.99 | -24.53 | 218 |
| 51 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -38.05 | -6.95 | -38.36 | 480 |
| 52 | Bollinger reversion · 1h | reversion | 72.97 | -27.03 | 237 | 40.1 | -32.27 | -6.18 | -32.71 | 368 |
| 53 | Donchian 20/10 · 1h | breakout | 72.11 | -27.89 | 138 | 20.3 | -31.16 | -5.67 | -33.89 | 219 |
| 54 | OBV trend · 1h | momentum | 71.90 | -28.10 | 261 | 17.6 | -32.71 | -7.24 | -32.82 | 299 |
| 55 | ROC + volume · 1h | momentum | 71.49 | -28.51 | 339 | 25.7 | -36.49 | -7.00 | -37.91 | 386 |
| 56 | VWAP momentum · 1h | momentum | 67.69 | -32.31 | 755 | 22.3 | -55.06 | -11.51 | -56.75 | 1232 |
| 57 | EMA 9/21 cross · 1h | trend | 67.63 | -32.37 | 238 | 10.1 | -40.06 | -8.11 | -40.33 | 338 |
| 58 | Candlestick reversal · 1h | reversion | 67.60 | -32.40 | 378 | 29.9 | -36.81 | -6.96 | -37.82 | 544 |
| 59 | Three white soldiers | momentum | 67.32 | -32.67 | 445 | 16.2 | -47.19 | -21.86 | -47.19 | 634 |
| 60 | Agent (ML meta-label) | meta | 66.79 | -33.21 | 1469 | 22.2 | -10.59 | -1.90 | -18.31 | 318 |
| 61 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -26.96 | -4.30 | -29.66 | 204 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -41.54 | -2.61 | -53.15 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.38 | -98.94 | 5190 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.74 | -25.31 | -79.98 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.39 | -47.82 | -93.39 | 2510 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.70 | -30.91 | -88.72 | 1902 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.54 | -38.74 | -90.55 | 2292 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.97 | -32.94 | -90.97 | 2252 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -54.11 | -97.65 | 3437 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -60.11 | -96.22 | 3400 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -33.16 | -93.83 | 2471 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.87 | -36.77 | -81.87 | 1646 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.50 | -54.84 | -99.50 | 5869 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.52 | -42.60 | -92.64 | 2579 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.95 | -38.16 | -95.95 | 3443 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.87 | -99.80 | 6162 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.53 | -43.33 | -91.53 | 2250 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.18 | -25.49 | -74.56 | 1546 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -62.60 | -97.73 | 3521 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.73 | -61.46 | -98.73 | 4826 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.83 | -27.32 | -69.78 | 1191 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.49 | -54.08 | -94.49 | 2734 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.43 | -35.79 | -84.45 | 1783 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -70.88 | -99.63 | 6298 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.51 | -30.72 | -88.51 | 2248 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.84 | -19.17 | -76.84 | 1694 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.76 | -37.06 | -90.76 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.52 | -50.48 | -96.52 | 3853 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.15 | -51.26 | -89.15 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.33 | -27.47 | -65.62 | 802 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.02 | -24.23 | -73.65 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.99 | -18.14 | -76.99 | 1611 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.16 | -50.99 | -97.16 | 4289 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -95.28 | -99.93 | 8205 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T15:25 | Williams %R · 1h | sell | SPY | 18.03 | -0.35 | stop-loss |
| 2026-11-05T15:25 | OBV trend · 1h | buy | SQQQ | 17.98 | — | entry |
| 2026-11-05T15:25 | OBV trend · 1h | sell | TNA | 17.73 | -0.66 | stop-loss |
| 2026-11-05T15:25 | ADX DI cross · 1h | sell | LABU | 19.94 | -0.52 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | ADX DI cross · 1h | sell | ETHU | 19.40 | -1.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | ADX DI cross · 1h | sell | AMZN | 20.02 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | ADX DI cross · 1h | sell | AAPL | 20.40 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | MACD cross · 1h | sell | MSTR | 9.13 | -0.27 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | MACD cross · 1h | sell | MSFT | 9.25 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | MACD cross · 1h | sell | LABU | 5.66 | -0.22 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | MACD cross · 1h | sell | ETHU | 9.02 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | MACD cross · 1h | sell | COIN | 6.66 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | MACD cross · 1h | sell | BITX | 5.77 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | MACD cross · 1h | sell | AMZN | 9.21 | 0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:25 | MACD cross · 1h | sell | AAPL | 9.23 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T15:20 | Agent (ML meta-label) | buy | TQQQ | 9.60 | — | entry |
| 2026-11-05T15:20 | Agent (ML meta-label) | buy | ETHU | 9.61 | — | entry |
| 2026-11-05T15:20 | Agent (ML meta-label) | buy | BITX | 9.61 | — | entry |
| 2026-11-05T15:20 | Agent (ML meta-label) | sell | MSTR | 7.11 | -0.08 | rebalance down |
| 2026-11-05T15:20 | Agent (ML meta-label) | sell | MSFT | 3.89 | -0.07 | rebalance down |
| 2026-11-05T15:20 | Agent (ML meta-label) | sell | GOOGL | 7.18 | -0.04 | rebalance down |
| 2026-11-05T15:20 | Agent (ML meta-label) | sell | AAPL | 7.30 | -0.05 | rebalance down |
| 2026-11-05T15:20 | Donchian 20/10 · 1h | buy | MSFT | 3.60 | — | rebalance up |
| 2026-11-05T15:20 | ROC + volume · 1h | sell | MSFT | 14.27 | -0.28 | stop-loss |
| 2026-11-05T15:20 | Ichimoku · 1h | sell | TNA | 19.44 | -0.59 | stop-loss |
| 2026-11-05T15:20 | Ichimoku · 1h | sell | IWM | 19.76 | -0.20 | stop-loss |
| 2026-11-05T15:20 | MACD zero-line · 1h | sell | TNA | 18.53 | -0.64 | stop-loss |
| 2026-11-05T15:20 | MACD cross · 1h | buy | MSTR | 4.85 | — | rebalance up |
| 2026-11-05T15:20 | MACD cross · 1h | buy | MSFT | 5.42 | — | rebalance up |
| 2026-11-05T15:20 | MACD cross · 1h | buy | ETHU | 4.70 | — | rebalance up |
| 2026-11-05T15:20 | MACD cross · 1h | buy | AMZN | 4.51 | — | rebalance up |
| 2026-11-05T15:20 | MACD cross · 1h | buy | AAPL | 5.82 | — | rebalance up |
| 2026-11-05T15:20 | MACD cross · 1h | sell | TNA | 5.53 | -0.35 | stop-loss |
| 2026-11-05T15:20 | MACD cross · 1h | sell | SPY | 5.77 | -0.10 | stop-loss |
| 2026-11-05T15:20 | MACD cross · 1h | sell | IWM | 3.51 | -0.05 | stop-loss |
| 2026-11-05T15:20 | Triple EMA stack · 1h | buy | SQQQ | 5.87 | — | rebalance up |
| 2026-11-05T15:20 | Triple EMA stack · 1h | buy | MSFT | 6.25 | — | rebalance up |
| 2026-11-05T15:20 | Triple EMA stack · 1h | buy | AAPL | 6.22 | — | rebalance up |
| 2026-11-05T15:20 | Triple EMA stack · 1h | sell | TNA | 14.76 | -0.42 | stop-loss |
| 2026-11-05T15:20 | Triple EMA stack · 1h | sell | IWM | 14.88 | -0.14 | stop-loss |

## Data problems on the last tick

- GURU: yfinance: $GURU: possibly delisted; no price data found  (5m 2026-11-04 15:25:05.000161+00:00 -> 2026-11-05 15:35:05.000161+00:00); yahoo: cooling down after a rate limit
- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 15:25:05.000161+00:00 -> 2026-11-05 15:35:05.000161+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 15:25:05.000161+00:00 -> 2026-11-05 15:35:05.000161+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 15:25:05.000161+00:00 -> 2026-11-05 15:35:05.000161+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
