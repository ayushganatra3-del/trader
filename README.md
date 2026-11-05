# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T15:55:05.000186+00:00 · 48618 ticks

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

Today: 18366 decisions in 2556 calls, $0.2419 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T15:55 | 1 / 9 / 21 | cash |  |
| Breezy | 2026-11-05T15:55 | 0 / 22 / 9 | cash |  |
| Boozy | 2026-11-05T15:55 | 4 / 25 / 2 | cash |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.79 | 13.79 | 18 | 66.7 | 15.55 | 3.28 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.54 | 13.54 | 0 | — | 15.03 | 5.19 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 108.00 | 8.00 | 28 | 25.0 | 16.77 | 2.73 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.90 | 3.90 | 28 | 42.9 | 2.28 | 0.66 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.84 | -0.16 | 0 | — | 3.67 | 1.13 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 106 | 46.2 | -11.51 | -3.01 | -12.83 | 138 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.81 | -2.19 | 116 | 34.5 | 4.97 | 2.52 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Gap and go | momentum | 95.83 | -4.17 | 160 | 28.8 | 1.01 | 0.41 | -9.18 | 220 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 95.37 | -4.62 | 0 | — | -3.49 | -1.29 | -6.35 | 1 |
| 14 | Agent (rotation) | meta | 95.36 | -4.64 | 174 | 27.6 | -6.18 | -3.73 | -10.28 | 176 |
| 15 | Hold SPY | benchmark | 94.56 | -5.44 | 0 | — | -4.14 | -1.66 | -5.38 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 17 | Trend pullback · 1h | trend | 92.44 | -7.56 | 105 | 22.9 | -14.91 | -5.25 | -17.67 | 79 |
| 18 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -11.98 | -1.32 | -17.57 | 8 |
| 19 | Copy: Congress Democrats (NANC) | copy | 91.54 | -8.46 | 0 | — | -5.80 | -1.95 | -9.15 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 89.94 | -10.06 | 365 | 32.9 | -15.00 | -4.82 | -17.21 | 584 |
| 22 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -14.03 | -7.86 | -14.43 | 214 |
| 23 | Hold BTC | benchmark | 88.92 | -11.08 | 0 | — | -5.42 | -0.68 | -13.31 | 1 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.50 | -3.31 | -14.15 | 85 |
| 25 | Daily: Bullish score | daily | 88.58 | -11.42 | 14 | 21.4 | -7.90 | -1.18 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 88.42 | -11.58 | 38 | 39.5 | -23.10 | -4.68 | -23.79 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.91 | -13.09 | 164 | 26.8 | -18.49 | -4.03 | -21.06 | 243 |
| 28 | Donchian 55/20 · 1h | breakout | 86.51 | -13.49 | 70 | 14.3 | -13.56 | -2.90 | -19.86 | 105 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -34.61 | -2.16 | -37.53 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -16.79 | -4.84 | -18.47 | 98 |
| 31 | Opening range 15m | breakout | 83.71 | -16.29 | 445 | 30.6 | -19.11 | -5.64 | -21.20 | 712 |
| 32 | Volume breakout · 1h | breakout | 82.50 | -17.50 | 144 | 27.8 | -13.77 | -3.13 | -18.36 | 96 |
| 33 | Keltner breakout · 1h | breakout | 81.80 | -18.20 | 105 | 23.8 | -24.83 | -5.28 | -25.57 | 189 |
| 34 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -24.50 | -4.36 | -25.07 | 374 |
| 35 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -15.12 | -2.12 | -22.55 | 1 |
| 36 | Connors RSI(2) · 1h | reversion | 80.05 | -19.95 | 202 | 40.1 | -22.17 | -6.86 | -22.17 | 134 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -23.69 | -4.04 | -26.26 | 272 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -21.21 | -3.07 | -21.25 | 150 |
| 39 | Bollinger breakout · 1h | breakout | 78.99 | -21.01 | 164 | 23.8 | -21.67 | -4.41 | -26.30 | 252 |
| 40 | Ichimoku · 1h | trend | 78.37 | -21.63 | 93 | 15.1 | -24.31 | -4.94 | -28.51 | 130 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -25.27 | -3.64 | -28.54 | 446 |
| 42 | EMA 20/50 cross · 1h | trend | 76.54 | -23.46 | 100 | 10.0 | -20.68 | -3.63 | -27.58 | 132 |
| 43 | Heikin-Ashi · 1h | trend | 76.12 | -23.88 | 385 | 23.1 | -43.00 | -8.85 | -44.13 | 677 |
| 44 | Triple EMA stack · 1h | trend | 74.96 | -25.04 | 141 | 14.9 | -29.97 | -5.99 | -32.95 | 212 |
| 45 | Williams %R · 1h | reversion | 74.56 | -25.44 | 298 | 46.6 | -34.38 | -6.17 | -35.45 | 522 |
| 46 | MACD zero-line · 1h | trend | 74.36 | -25.64 | 153 | 16.3 | -29.59 | -5.83 | -29.61 | 215 |
| 47 | Supertrend · 1h | trend | 73.41 | -26.59 | 165 | 13.3 | -31.19 | -5.71 | -33.58 | 234 |
| 48 | RSI momentum · 1h | momentum | 73.35 | -26.65 | 157 | 12.7 | -31.11 | -5.90 | -32.22 | 226 |
| 49 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -38.65 | -6.73 | -38.96 | 479 |
| 50 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -24.32 | -3.77 | -24.88 | 216 |
| 51 | Bollinger reversion · 1h | reversion | 72.97 | -27.03 | 237 | 40.1 | -32.27 | -6.18 | -32.71 | 368 |
| 52 | Donchian 20/10 · 1h | breakout | 72.30 | -27.70 | 139 | 20.1 | -30.69 | -5.58 | -33.98 | 219 |
| 53 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -34.87 | -4.90 | -36.76 | 32 |
| 54 | ROC + volume · 1h | momentum | 71.61 | -28.39 | 339 | 25.7 | -36.48 | -7.13 | -38.08 | 384 |
| 55 | OBV trend · 1h | momentum | 71.57 | -28.43 | 263 | 17.5 | -35.12 | -7.26 | -35.13 | 300 |
| 56 | VWAP momentum · 1h | momentum | 68.20 | -31.80 | 756 | 22.2 | -53.78 | -11.39 | -55.83 | 1226 |
| 57 | Candlestick reversal · 1h | reversion | 67.60 | -32.40 | 378 | 29.9 | -35.32 | -6.48 | -36.35 | 547 |
| 58 | EMA 9/21 cross · 1h | trend | 67.39 | -32.62 | 240 | 10.0 | -40.94 | -8.10 | -41.11 | 336 |
| 59 | Three white soldiers | momentum | 67.32 | -32.67 | 445 | 16.2 | -47.19 | -21.86 | -47.19 | 634 |
| 60 | Agent (ML meta-label) | meta | 66.47 | -33.53 | 1475 | 22.2 | -6.07 | -1.04 | -15.43 | 311 |
| 61 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -27.11 | -4.17 | -29.66 | 218 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -43.42 | -2.73 | -54.65 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -46.56 | -98.95 | 5175 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.75 | -25.28 | -80.00 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -47.37 | -93.33 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.70 | -30.89 | -88.72 | 1903 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.51 | -38.50 | -90.51 | 2289 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.93 | -32.93 | -90.93 | 2248 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.65 | -54.21 | -97.65 | 3438 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -58.98 | -96.19 | 3382 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.75 | -33.25 | -93.83 | 2465 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.87 | -36.77 | -81.87 | 1646 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -54.22 | -99.51 | 5890 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.46 | -41.83 | -92.63 | 2579 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.95 | -38.07 | -95.95 | 3440 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -71.77 | -99.80 | 6137 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.53 | -43.32 | -91.53 | 2250 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.12 | -24.86 | -74.73 | 1550 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -62.60 | -97.73 | 3521 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.76 | -60.76 | -98.76 | 4840 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.55 | -26.51 | -69.79 | 1191 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.48 | -53.95 | -94.49 | 2732 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.43 | -35.77 | -84.45 | 1782 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -70.76 | -99.64 | 6302 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.99 | -30.36 | -88.99 | 2255 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.30 | -19.33 | -77.30 | 1701 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.91 | -36.77 | -90.91 | 2225 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.59 | -50.19 | -96.59 | 3853 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.20 | -51.82 | -89.20 | 2153 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.14 | -27.08 | -65.47 | 802 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.83 | -23.73 | -73.67 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.47 | -17.75 | -77.49 | 1627 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -49.07 | -97.24 | 4308 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.10 | -99.93 | 8190 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-05T15:35 | Agent (ML meta-label) | sell | GOOGL | 9.66 | -0.00 | selected signal exited |
| 2026-11-05T15:30 | Agent (ML meta-label) | buy | TNA | 4.46 | — | entry |
| 2026-11-05T15:30 | Agent (ML meta-label) | buy | SQQQ | 12.43 | — | entry |
| 2026-11-05T15:30 | Agent (ML meta-label) | buy | NVDA | 12.43 | — | entry |
| 2026-11-05T15:30 | Agent (ML meta-label) | sell | TQQQ | 9.51 | -0.09 | selected signal exited |
| 2026-11-05T15:30 | Agent (ML meta-label) | sell | MSTR | 9.47 | -0.23 | selected signal exited |
| 2026-11-05T15:30 | Agent (ML meta-label) | sell | ETHU | 9.39 | -0.22 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 15:55:05.000186+00:00 -> 2026-11-05 16:05:05.000186+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 15:55:05.000186+00:00 -> 2026-11-05 16:05:05.000186+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 15:55:05.000186+00:00 -> 2026-11-05 16:05:05.000186+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
