# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T18:25:05.000175+00:00 · 48744 ticks

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

Today: 29868 decisions in 2934 calls, $0.3768 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T18:25 | 2 / 12 / 16 | cash |  |
| Breezy | 2026-11-05T18:25 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-05T18:25 | 4 / 22 / 4 | BITX 70% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.68 | 13.68 | 18 | 66.7 | 15.60 | 3.28 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.61 | 12.61 | 0 | — | 14.26 | 4.94 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.90 | 7.90 | 28 | 25.0 | 16.82 | 2.73 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.80 | 3.80 | 28 | 42.9 | 2.32 | 0.67 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 98.57 | -1.43 | 0 | — | 2.49 | 0.79 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.39 | -1.61 | 106 | 46.2 | -12.31 | -3.21 | -12.92 | 142 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.79 | -2.21 | 116 | 34.5 | 5.03 | 2.55 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.24 | -4.75 | 0 | — | -3.49 | -1.29 | -6.35 | 1 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.34 | 0.20 | -9.18 | 220 |
| 14 | Agent (rotation) | meta | 94.94 | -5.06 | 174 | 27.6 | -7.06 | -4.28 | -10.81 | 176 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Hold SPY | benchmark | 93.96 | -6.04 | 0 | — | -4.50 | -1.72 | -5.91 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -12.01 | -1.32 | -17.84 | 8 |
| 18 | Trend pullback · 1h | trend | 91.96 | -8.04 | 105 | 22.9 | -15.52 | -5.59 | -17.86 | 81 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.41 | -9.59 | 0 | — | -6.43 | -1.99 | -10.50 | 1 |
| 21 | Opening range 30m | breakout | 89.91 | -10.09 | 365 | 32.9 | -14.98 | -4.81 | -17.21 | 584 |
| 22 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -14.35 | -8.09 | -14.74 | 210 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.48 | -3.30 | -14.15 | 85 |
| 24 | Daily: Bullish score | daily | 88.44 | -11.56 | 14 | 21.4 | -7.97 | -1.19 | -16.58 | 14 |
| 25 | Hold BTC ⏸ | benchmark | 88.43 | -11.57 | 1 | 0.0 | -5.06 | -0.63 | -13.41 | 1 |
| 26 | Parabolic SAR · 1h | trend | 87.30 | -12.70 | 166 | 27.1 | -17.83 | -3.95 | -21.06 | 242 |
| 27 | Copy: Insider buying | copy | 86.78 | -13.22 | 40 | 37.5 | -24.62 | -4.90 | -25.46 | 65 |
| 28 | Donchian 55/20 · 1h | breakout | 86.35 | -13.65 | 71 | 14.1 | -13.50 | -2.87 | -19.94 | 105 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -33.97 | -2.12 | -37.55 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.63 | -5.51 | -18.86 | 98 |
| 31 | Opening range 15m | breakout | 83.69 | -16.31 | 445 | 30.6 | -19.09 | -5.63 | -21.20 | 712 |
| 32 | Volume breakout · 1h | breakout | 82.48 | -17.52 | 144 | 27.8 | -13.75 | -3.13 | -18.40 | 96 |
| 33 | Keltner breakout · 1h | breakout | 81.73 | -18.27 | 106 | 23.6 | -24.21 | -5.20 | -25.00 | 190 |
| 34 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -27.94 | -4.54 | -28.53 | 379 |
| 35 | Connors RSI(2) · 1h | reversion | 80.30 | -19.70 | 202 | 40.1 | -21.86 | -6.87 | -22.17 | 135 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -15.62 | -2.15 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -23.68 | -3.84 | -26.45 | 262 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -19.23 | -2.76 | -19.73 | 150 |
| 39 | Bollinger breakout · 1h | breakout | 78.93 | -21.07 | 165 | 23.6 | -23.08 | -4.74 | -26.52 | 252 |
| 40 | Ichimoku · 1h | trend | 78.46 | -21.54 | 94 | 14.9 | -24.20 | -4.93 | -28.68 | 131 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -25.95 | -3.88 | -28.54 | 446 |
| 42 | Heikin-Ashi · 1h | trend | 76.87 | -23.13 | 385 | 23.1 | -42.36 | -8.81 | -44.05 | 676 |
| 43 | EMA 20/50 cross · 1h | trend | 76.37 | -23.63 | 102 | 10.8 | -20.84 | -3.73 | -27.81 | 134 |
| 44 | Triple EMA stack · 1h | trend | 74.80 | -25.20 | 142 | 14.8 | -30.93 | -6.30 | -33.27 | 211 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -28.48 | -5.84 | -29.20 | 214 |
| 46 | RSI momentum · 1h | momentum | 73.58 | -26.42 | 158 | 12.7 | -30.93 | -5.89 | -32.33 | 226 |
| 47 | Supertrend · 1h | trend | 73.54 | -26.46 | 165 | 13.3 | -31.08 | -5.74 | -33.58 | 235 |
| 48 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -37.60 | -6.75 | -38.83 | 477 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -26.68 | -4.30 | -26.79 | 217 |
| 50 | Bollinger reversion · 1h | reversion | 72.71 | -27.29 | 237 | 40.1 | -32.72 | -6.22 | -32.98 | 364 |
| 51 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -34.99 | -4.90 | -37.28 | 32 |
| 52 | Donchian 20/10 · 1h | breakout | 72.16 | -27.84 | 140 | 20.0 | -32.65 | -6.00 | -34.25 | 221 |
| 53 | Williams %R · 1h ⏸ | reversion | 71.97 | -28.03 | 310 | 44.8 | -36.98 | -6.34 | -37.55 | 530 |
| 54 | ROC + volume · 1h | momentum | 71.41 | -28.59 | 340 | 25.6 | -36.98 | -7.25 | -38.28 | 386 |
| 55 | OBV trend · 1h | momentum | 71.12 | -28.88 | 264 | 17.4 | -35.16 | -7.40 | -35.34 | 298 |
| 56 | VWAP momentum · 1h | momentum | 68.18 | -31.82 | 756 | 22.2 | -54.98 | -11.91 | -56.07 | 1223 |
| 57 | EMA 9/21 cross · 1h | trend | 67.63 | -32.37 | 241 | 10.0 | -41.02 | -8.09 | -41.46 | 337 |
| 58 | Three white soldiers | momentum | 67.20 | -32.80 | 446 | 16.1 | -47.28 | -21.90 | -47.28 | 635 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -27.59 | -4.34 | -29.66 | 206 |
| 60 | Agent (ML meta-label) | meta | 65.39 | -34.61 | 1498 | 22.2 | -4.11 | -0.50 | -14.95 | 313 |
| 61 | Candlestick reversal · 1h | reversion | 65.37 | -34.63 | 388 | 29.1 | -38.40 | -7.03 | -38.68 | 559 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -42.87 | -2.70 | -54.67 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.11 | -98.94 | 5134 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.80 | -25.13 | -80.12 | 1406 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -46.34 | -93.33 | 2503 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -30.87 | -88.93 | 1901 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.39 | -37.76 | -90.48 | 2284 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.73 | -32.54 | -90.82 | 2241 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.63 | -52.86 | -97.63 | 3418 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.15 | -57.25 | -96.15 | 3373 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.74 | -33.49 | -93.80 | 2454 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.67 | -36.01 | -81.75 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -53.55 | -99.52 | 5925 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.42 | -41.53 | -92.57 | 2563 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.91 | -37.95 | -95.92 | 3438 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.42 | -99.80 | 6145 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.56 | -42.90 | -91.56 | 2235 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.25 | -25.41 | -74.59 | 1535 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -60.46 | -97.71 | 3506 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -59.71 | -98.78 | 4849 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.02 | -27.68 | -70.03 | 1181 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.46 | -53.45 | -94.46 | 2718 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.42 | -35.60 | -84.46 | 1779 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.33 | -99.64 | 6315 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.04 | -30.34 | -89.09 | 2261 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.58 | -19.19 | -77.68 | 1730 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.19 | -36.04 | -91.23 | 2235 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.57 | -50.28 | -96.59 | 3845 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -52.52 | -89.22 | 2139 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.46 | -27.66 | -65.80 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.07 | -23.66 | -73.91 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.63 | -17.66 | -77.72 | 1652 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -48.53 | -97.25 | 4306 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.90 | -99.93 | 8185 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T18:25 | EMA 9/21 cross · 1h | sell | AAPL | 16.56 | -0.41 | stop-loss |
| 2026-11-05T18:20 | Agent (ML meta-label) | sell | GOOGL | 6.52 | -0.03 | selected signal exited |
| 2026-11-05T18:15 | Agent (ML meta-label) | buy | GOOGL | 6.55 | — | entry |
| 2026-11-05T18:15 | Agent (ML meta-label) | sell | SOXL | 6.65 | 0.12 | selected signal exited |
| 2026-11-05T18:15 | Candlestick reversal · 1h | buy | GOOGL | 3.30 | — | rebalance up |
| 2026-11-05T18:10 | Agent (ML meta-label) | buy | SOXL | 6.53 | — | following Connors RSI(2) |
| 2026-11-05T18:08 | Copy: Insider buying | buy | KNOP | 1.99 | — | entry |
| 2026-11-05T18:08 | Copy: Insider buying | buy | ASPE | 10.85 | — | entry |
| 2026-11-05T18:08 | Copy: Insider buying | sell | PLBY | 1.03 | -0.12 | target is flat |
| 2026-11-05T18:08 | Copy: Insider buying | sell | BPRE | 11.82 | -0.90 | target is flat |
| 2026-11-05T18:05 | Agent (ML meta-label) | buy | AAPL | 7.25 | — | entry |
| 2026-11-05T18:05 | Agent (ML meta-label) | sell | UPRO | 4.85 | -0.24 | selected signal exited |
| 2026-11-05T18:05 | Agent (ML meta-label) | sell | TECL | 6.44 | -0.10 | selected signal exited |
| 2026-11-05T18:05 | Hold BTC | sell | BTC-USD | 88.43 | -11.57 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T18:05 | Candlestick reversal · 1h | buy | BITX | 3.26 | — | rebalance up |
| 2026-11-05T18:05 | Candlestick reversal · 1h | sell | TECL | 12.90 | -0.61 | stop-loss |
| 2026-11-05T18:00 | Agent (ML meta-label) | buy | TECL | 6.55 | — | entry |
| 2026-11-05T18:00 | Agent (ML meta-label) | sell | AAPL | 5.06 | -0.11 | selected signal exited |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | TECL | 3.86 | — | rebalance up |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | PLTR | 3.71 | — | rebalance up |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | MSTR | 3.73 | — | rebalance up |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | GOOGL | 3.74 | — | rebalance up |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | BITX | 3.68 | — | rebalance up |
| 2026-11-05T18:00 | Candlestick reversal · 1h | sell | SPY | 9.38 | -0.08 | stop-loss |
| 2026-11-05T18:00 | ROC + volume · 1h | sell | AAPL | 17.68 | -0.44 | target is flat |
| 2026-11-05T17:56 | Agent (ML meta-label) | sell | SPY | 5.95 | -0.01 | selected signal exited |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 18:25:05.000175+00:00 -> 2026-11-05 18:35:05.000175+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 18:25:05.000175+00:00 -> 2026-11-05 18:35:05.000175+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 18:25:05.000175+00:00 -> 2026-11-05 18:35:05.000175+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
