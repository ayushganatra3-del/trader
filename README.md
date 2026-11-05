# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T16:56:05.000122+00:00 · 48668 ticks

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

Today: 22926 decisions in 2706 calls, $0.2953 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T16:56 | 2 / 4 / 25 | cash |  |
| Breezy | 2026-11-05T16:56 | 0 / 23 / 8 | cash |  |
| Boozy | 2026-11-05T16:56 | 3 / 22 / 6 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.11 | 13.11 | 0 | — | 14.57 | 5.04 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.85 | 10.85 | 18 | 66.7 | 12.66 | 3.18 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.21 | 5.21 | 28 | 25.0 | 13.85 | 2.61 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.21 | 1.21 | 28 | 42.9 | -0.28 | 0.02 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 106 | 46.2 | -11.51 | -3.01 | -12.83 | 138 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.34 | -0.66 | 0 | — | 3.23 | 1.00 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.13 | -2.87 | 116 | 34.5 | 4.32 | 2.29 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.29 | -4.71 | 0 | — | -3.49 | -1.29 | -6.35 | 1 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.34 | 0.20 | -9.18 | 220 |
| 14 | Hold SPY | benchmark | 94.84 | -5.16 | 0 | — | -3.59 | -1.49 | -5.38 | 1 |
| 15 | Agent (rotation) | meta | 94.33 | -5.67 | 174 | 27.6 | -5.96 | -4.15 | -9.19 | 167 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 17 | Trend pullback · 1h | trend | 92.49 | -7.51 | 105 | 22.9 | -15.06 | -5.31 | -17.86 | 81 |
| 18 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -8.85 | -1.08 | -17.57 | 8 |
| 19 | Copy: Congress Democrats (NANC) | copy | 91.50 | -8.50 | 0 | — | -5.86 | -1.97 | -10.27 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Hold BTC | benchmark | 89.79 | -10.21 | 0 | — | -4.08 | -0.48 | -13.31 | 1 |
| 22 | Opening range 30m | breakout | 89.33 | -10.67 | 365 | 32.9 | -15.53 | -5.07 | -17.21 | 584 |
| 23 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -14.11 | -7.93 | -14.50 | 206 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.48 | -3.30 | -14.15 | 85 |
| 25 | Daily: Bullish score | daily | 88.18 | -11.82 | 14 | 21.4 | -8.52 | -1.29 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 87.54 | -12.46 | 38 | 39.5 | -23.98 | -4.82 | -24.51 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.78 | -13.22 | 165 | 27.3 | -18.55 | -4.03 | -21.06 | 243 |
| 28 | Donchian 55/20 · 1h | breakout | 85.81 | -14.19 | 70 | 14.3 | -14.41 | -3.10 | -19.99 | 105 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -33.02 | -2.07 | -37.46 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.09 | -5.34 | -19.03 | 98 |
| 31 | Opening range 15m | breakout | 83.14 | -16.86 | 445 | 30.6 | -19.61 | -5.90 | -21.20 | 712 |
| 32 | Volume breakout · 1h | breakout | 81.95 | -18.05 | 144 | 27.8 | -14.31 | -3.28 | -18.40 | 96 |
| 33 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -25.99 | -4.52 | -26.24 | 377 |
| 34 | Keltner breakout · 1h | breakout | 81.21 | -18.79 | 106 | 23.6 | -25.79 | -5.53 | -26.12 | 188 |
| 35 | Connors RSI(2) · 1h | reversion | 80.92 | -19.08 | 202 | 40.1 | -21.30 | -6.84 | -22.17 | 135 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -14.52 | -2.05 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -23.46 | -3.76 | -26.45 | 260 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -20.36 | -3.00 | -21.23 | 152 |
| 39 | Bollinger breakout · 1h | breakout | 78.43 | -21.57 | 165 | 23.6 | -22.32 | -4.50 | -26.52 | 252 |
| 40 | Ichimoku · 1h | trend | 78.27 | -21.73 | 93 | 15.1 | -24.39 | -4.95 | -28.59 | 130 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -25.28 | -3.79 | -28.54 | 446 |
| 42 | Heikin-Ashi · 1h | trend | 76.38 | -23.62 | 385 | 23.1 | -42.80 | -8.85 | -44.12 | 676 |
| 43 | EMA 20/50 cross · 1h | trend | 75.96 | -24.04 | 102 | 10.8 | -21.13 | -3.76 | -27.81 | 134 |
| 44 | MACD zero-line · 1h | trend | 74.89 | -25.11 | 153 | 16.3 | -29.05 | -5.82 | -29.61 | 215 |
| 45 | Triple EMA stack · 1h | trend | 74.37 | -25.63 | 141 | 14.9 | -30.89 | -6.25 | -33.29 | 211 |
| 46 | Supertrend · 1h | trend | 73.48 | -26.52 | 165 | 13.3 | -31.41 | -5.73 | -33.58 | 234 |
| 47 | RSI momentum · 1h | momentum | 73.38 | -26.62 | 157 | 12.7 | -30.09 | -5.70 | -32.33 | 223 |
| 48 | Williams %R · 1h | reversion | 73.33 | -26.67 | 298 | 46.6 | -35.40 | -6.27 | -35.66 | 534 |
| 49 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -37.90 | -6.76 | -38.90 | 479 |
| 50 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -26.29 | -4.28 | -26.67 | 216 |
| 51 | Bollinger reversion · 1h | reversion | 72.90 | -27.10 | 237 | 40.1 | -32.25 | -6.21 | -32.63 | 366 |
| 52 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -34.50 | -4.90 | -36.81 | 32 |
| 53 | Donchian 20/10 · 1h | breakout | 71.73 | -28.27 | 139 | 20.1 | -31.26 | -5.64 | -34.25 | 219 |
| 54 | OBV trend · 1h | momentum | 71.52 | -28.48 | 264 | 17.4 | -34.72 | -7.37 | -34.80 | 301 |
| 55 | ROC + volume · 1h | momentum | 71.44 | -28.56 | 339 | 25.7 | -36.54 | -7.11 | -38.11 | 384 |
| 56 | VWAP momentum · 1h | momentum | 67.73 | -32.27 | 756 | 22.2 | -55.21 | -11.88 | -56.15 | 1224 |
| 57 | EMA 9/21 cross · 1h | trend | 67.55 | -32.45 | 240 | 10.0 | -41.28 | -8.19 | -41.56 | 338 |
| 58 | Three white soldiers | momentum | 67.20 | -32.80 | 446 | 16.1 | -47.28 | -21.90 | -47.28 | 635 |
| 59 | Candlestick reversal · 1h | reversion | 66.70 | -33.30 | 378 | 29.9 | -36.92 | -6.84 | -37.09 | 567 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -25.66 | -4.01 | -29.66 | 221 |
| 61 | Agent (ML meta-label) | meta | 65.98 | -34.02 | 1482 | 22.1 | -8.20 | -1.32 | -16.61 | 308 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -42.04 | -2.64 | -54.60 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.97 | -98.93 | 5164 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.85 | -25.34 | -80.07 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -46.90 | -93.33 | 2507 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.66 | -30.62 | -88.77 | 1899 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.51 | -38.29 | -90.53 | 2286 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.82 | -32.62 | -90.85 | 2243 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -53.89 | -97.64 | 3436 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.16 | -58.16 | -96.16 | 3382 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.87 | -33.75 | -93.92 | 2479 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.82 | -36.50 | -81.82 | 1642 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -54.04 | -99.51 | 5899 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.50 | -42.37 | -92.63 | 2578 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.93 | -38.09 | -95.95 | 3441 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -71.31 | -99.80 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.48 | -42.81 | -91.48 | 2235 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.28 | -25.51 | -74.65 | 1557 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -61.56 | -97.71 | 3514 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.74 | -60.22 | -98.76 | 4846 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.97 | -27.63 | -69.98 | 1188 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.50 | -54.09 | -94.51 | 2731 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.41 | -35.68 | -84.43 | 1784 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -70.00 | -99.64 | 6322 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.85 | -30.75 | -89.07 | 2268 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.11 | -19.22 | -77.21 | 1734 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.92 | -36.80 | -91.02 | 2249 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.55 | -50.23 | -96.59 | 3842 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -52.71 | -89.24 | 2145 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.31 | -27.42 | -65.64 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.17 | -24.09 | -73.84 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.22 | -17.85 | -77.61 | 1653 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.18 | -49.78 | -97.23 | 4292 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -95.45 | -99.93 | 8209 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T16:55 | Agent (ML meta-label) | sell | QQQ | 5.49 | -0.00 | selected signal exited |
| 2026-11-05T16:50 | Agent (ML meta-label) | buy | SQQQ | 5.50 | — | entry |
| 2026-11-05T16:50 | Agent (ML meta-label) | buy | SPY | 5.50 | — | entry |
| 2026-11-05T16:50 | Agent (ML meta-label) | buy | QQQ | 5.50 | — | entry |
| 2026-11-05T16:50 | OBV trend · 1h | sell | AAPL | 14.35 | -0.32 | stop-loss |
| 2026-11-05T16:50 | EMA 20/50 cross · 1h | sell | AAPL | 15.32 | -0.31 | stop-loss |
| 2026-11-05T16:45 | Agent (ML meta-label) | sell | SPY | 6.00 | -0.02 | selected signal exited |
| 2026-11-05T16:45 | Parabolic SAR · 1h | buy | AAPL | 4.37 | — | rebalance up |
| 2026-11-05T16:45 | Three white soldiers | sell | TSLA | 16.70 | -0.13 | exit signal |
| 2026-11-05T16:40 | Agent (ML meta-label) | sell | TECL | 5.08 | -0.03 | selected signal exited |
| 2026-11-05T16:35 | Agent (ML meta-label) | buy | SPY | 6.01 | — | entry |
| 2026-11-05T16:35 | Agent (ML meta-label) | sell | SQQQ | 5.15 | -0.03 | selected signal exited |
| 2026-11-05T16:35 | Agent (ML meta-label) | sell | QQQ | 5.09 | -0.02 | selected signal exited |
| 2026-11-05T16:35 | Agent (ML meta-label) | sell | ETHU | 5.07 | -0.04 | selected signal exited |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | UPRO | 5.09 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | TSLA | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | TECL | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | QQQ | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | PLTR | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | ETHU | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | COIN | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | BITX | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | AMZN | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | sell | SQQQ | 11.31 | -0.14 | rebalance down |
| 2026-11-05T16:30 | Agent (ML meta-label) | sell | NVDA | 11.44 | -0.02 | rebalance down |
| 2026-11-05T16:30 | Agent (ML meta-label) | sell | MSFT | 11.63 | -0.05 | rebalance down |
| 2026-11-05T16:30 | Agent (ML meta-label) | sell | AAPL | 11.41 | -0.14 | rebalance down |
| 2026-11-05T16:30 | Williams %R · 1h | buy | UPRO | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | TQQQ | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | TECL | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | SPY | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | SOXL | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | QQQ | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | MSTR | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | META | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | LABU | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | COIN | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | BITX | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Williams %R · 1h | buy | AMD | 6.21 | — | entry signal |
| 2026-11-05T16:30 | Bollinger reversion · 1h | buy | META | 18.24 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 16:56:05.000122+00:00 -> 2026-11-05 17:06:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 16:56:05.000122+00:00 -> 2026-11-05 17:06:05.000122+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 16:56:05.000122+00:00 -> 2026-11-05 17:06:05.000122+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
