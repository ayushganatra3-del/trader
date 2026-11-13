# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T21:40:05.000125+00:00 · 58659 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.50 (-14.50%)

Closed trades 195, win rate 35.9%, fees £5.63, max drawdown -15.42%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 0 distribution days in 25 sessions · timing exposure 0% · VXN 28.60 · VIX 18.82 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 42105 decisions in 3432 calls, $0.5204 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T21:40 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-13T21:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-13T21:40 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| MFI reversion | LABU | 1.92 | +6.76% | 3 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.84 | 17.84 | 0 | — | 15.31 | 5.11 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 3.29 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.99 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.59 | 4.59 | 0 | — | 6.58 | 1.81 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 1.00 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 7.52 | 2.97 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.28 | -1.72 | 0 | — | -0.61 | -0.13 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.84 | -3.16 | 1 | 0.0 | -3.27 | -2.15 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.66 | -3.34 | 191 | 30.4 | -2.23 | -0.76 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.21 | -3.79 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.96 | -3.36 | -13.35 | 154 |
| 16 | Copy: Insider buying | copy | 94.21 | -5.79 | 43 | 39.5 | -5.00 | -0.93 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.69 | -6.31 | 0 | — | -4.77 | -1.27 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.07 | -10.13 | 22 |
| 20 | Trend pullback · 1h | trend | 91.81 | -8.19 | 110 | 22.7 | -15.11 | -5.58 | -17.77 | 70 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.28 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.26 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.66 | -14.34 | 16 | 18.8 | -10.26 | -1.63 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.71 | -7.28 | -15.69 | 208 |
| 26 | Parabolic SAR · 1h | trend | 85.24 | -14.76 | 176 | 29.0 | -15.62 | -3.37 | -22.50 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -15.48 | -4.18 | -18.51 | 97 |
| 28 | Donchian 55/20 · 1h | breakout | 81.96 | -18.04 | 73 | 13.7 | -23.08 | -4.82 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.82 | -19.18 | 2 | 0.0 | -9.89 | -1.14 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.63 | -19.37 | 212 | 40.1 | -18.15 | -6.39 | -18.32 | 115 |
| 31 | Hold BTC | benchmark | 80.55 | -19.45 | 1 | 0.0 | -11.90 | -1.67 | -22.00 | 1 |
| 32 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 33 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.48 | -3.54 | -25.39 | 171 |
| 34 | Stochastic reversion · 1h | reversion | 79.55 | -20.45 | 303 | 47.5 | -26.49 | -3.91 | -28.07 | 398 |
| 35 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.71 | -21.36 | 720 |
| 36 | MFI reversion · 1h | reversion | 77.83 | -22.18 | 401 | 35.4 | -22.26 | -2.90 | -27.13 | 172 |
| 37 | ADX DI cross · 1h ⏸ | trend | 76.53 | -23.47 | 200 | 20.0 | -24.37 | -3.66 | -32.49 | 273 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.59 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -23.19 | -4.84 | -30.71 | 240 |
| 41 | Max aggression: 1-day momentum | meta | 74.86 | -25.14 | 29 | 27.6 | -20.15 | -0.61 | -57.50 | 41 |
| 42 | Heikin-Ashi · 1h | trend | 74.64 | -25.36 | 444 | 24.1 | -38.27 | -7.10 | -39.41 | 671 |
| 43 | MACD cross · 1h | trend | 74.13 | -25.87 | 385 | 23.6 | -29.68 | -4.39 | -38.65 | 470 |
| 44 | MACD zero-line · 1h | trend | 73.47 | -26.53 | 171 | 18.7 | -23.70 | -4.66 | -30.99 | 202 |
| 45 | RSI momentum · 1h | momentum | 72.57 | -27.43 | 171 | 14.0 | -26.67 | -4.08 | -37.92 | 208 |
| 46 | EMA 20/50 cross · 1h | trend | 72.51 | -27.49 | 109 | 10.1 | -28.28 | -4.78 | -40.51 | 120 |
| 47 | Supertrend · 1h | trend | 72.28 | -27.72 | 180 | 15.0 | -30.78 | -5.25 | -36.51 | 216 |
| 48 | Bollinger reversion · 1h | reversion | 71.77 | -28.23 | 303 | 41.6 | -33.33 | -5.22 | -35.72 | 383 |
| 49 | Triple EMA stack · 1h | trend | 71.61 | -28.39 | 151 | 14.6 | -27.75 | -4.57 | -38.65 | 203 |
| 50 | ROC + volume · 1h | momentum | 71.17 | -28.83 | 399 | 28.8 | -31.51 | -5.79 | -38.37 | 377 |
| 51 | CCI reversion · 1h | reversion | 70.89 | -29.11 | 346 | 43.4 | -37.63 | -5.89 | -38.71 | 471 |
| 52 | OBV trend · 1h | momentum | 69.66 | -30.34 | 299 | 19.1 | -29.52 | -5.20 | -37.94 | 275 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -33.12 | -4.51 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.21 | -30.79 | 153 | 19.0 | -30.32 | -5.43 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.62 | -32.38 | 383 | 43.6 | -42.42 | -6.92 | -44.04 | 543 |
| 56 | Agent (ML meta-label) | meta | 65.04 | -34.96 | 1855 | 24.7 | -20.37 | -3.69 | -23.84 | 349 |
| 57 | Z-score reversion · 1h | reversion | 64.84 | -35.16 | 204 | 37.3 | -31.16 | -4.39 | -31.55 | 237 |
| 58 | EMA 9/21 cross · 1h | trend | 64.67 | -35.33 | 267 | 11.6 | -37.71 | -7.60 | -43.16 | 329 |
| 59 | RSI(14) reversion · 1h | reversion | 63.96 | -36.04 | 186 | 32.8 | -37.32 | -5.54 | -38.29 | 239 |
| 60 | VWAP momentum · 1h | momentum | 62.59 | -37.41 | 914 | 22.3 | -52.87 | -10.68 | -53.43 | 1241 |
| 61 | Candlestick reversal · 1h | reversion | 62.06 | -37.94 | 487 | 28.3 | -44.82 | -8.25 | -45.94 | 602 |
| 62 | Three white soldiers | momentum | 58.34 | -41.66 | 542 | 14.6 | -49.50 | -22.28 | -49.51 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.57 | -99.00 | 5305 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.19 | -25.53 | -80.47 | 1426 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.80 | -46.36 | -93.83 | 2549 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.32 | -31.88 | -89.32 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.21 | -41.29 | -91.24 | 2350 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.83 | -31.38 | -89.83 | 2199 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -51.96 | -97.87 | 3501 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.20 | -56.12 | -96.21 | 3431 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -32.89 | -93.70 | 2335 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.03 | -34.47 | -83.09 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.71 | -99.57 | 6045 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.17 | -43.05 | -92.22 | 2634 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.44 | -37.33 | -95.44 | 3480 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.19 | -99.81 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.26 | -43.14 | -92.27 | 2282 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.88 | -26.25 | -75.92 | 1645 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -60.30 | -97.62 | 3525 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -64.06 | -98.88 | 4943 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.70 | -27.21 | -68.70 | 1254 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -58.01 | -94.76 | 2814 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.21 | -39.85 | -85.24 | 1794 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -75.28 | -99.66 | 6386 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.09 | -32.68 | -90.19 | 2329 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.60 | -20.17 | -78.91 | 1801 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.64 | -36.29 | -90.79 | 2177 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.05 | -51.04 | -97.05 | 3893 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -58.47 | -89.44 | 2162 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.20 | -30.27 | -66.42 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.35 | -23.02 | -71.39 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.09 | -19.28 | -80.42 | 1752 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.44 | -50.70 | -97.44 | 4361 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -114.41 | -99.93 | 8466 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T21:00 | Candlestick reversal · 1h | buy | XRP-USD | 2.24 | — | entry |
| 2026-11-13T21:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.89 | — | entry |
| 2026-11-13T21:00 | Candlestick reversal · 1h | sell | BTC-USD | 6.13 | -0.01 | exit signal |
| 2026-11-13T20:55 | Day trade: Stocks in Play ORB | sell | SQQQ | 25.65 | 0.46 | target is flat |
| 2026-11-13T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 103.88 | -0.01 | target is flat |
| 2026-11-13T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 111.21 | -1.41 | target is flat |
| 2026-11-13T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 92.12 | -1.06 | target is flat |
| 2026-11-13T20:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 114.23 | 2.50 | target is flat |
| 2026-11-13T20:55 | ADX DI cross · 1h | sell | TSLA | 15.71 | 0.32 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-13T20:55 | ADX DI cross · 1h | sell | SQQQ | 18.79 | -0.45 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-13T20:55 | Opening range 30m | sell | SQQQ | 21.21 | -0.27 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 30m | sell | MSFT | 21.60 | 0.06 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 30m | sell | META | 21.63 | 0.13 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 15m | sell | SQQQ | 19.69 | 0.14 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 15m | sell | MSFT | 19.78 | 0.17 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 15m | sell | META | 19.75 | 0.15 | end-of-day flatten |
| 2026-11-13T20:35 | Keltner breakout · 1h | sell | AAPL | 20.10 | -0.14 | stop-loss |
| 2026-11-13T20:35 | OBV trend · 1h | buy | TSLA | 17.41 | — | entry |
| 2026-11-13T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 93.19 | — | entry |
| 2026-11-13T20:30 | Connors RSI(2) · 1h | buy | AAPL | 20.16 | — | entry signal |
| 2026-11-13T20:30 | OBV trend · 1h | sell | TSLA | 17.37 | -0.03 | target is flat |
| 2026-11-13T20:30 | ROC + volume · 1h | sell | AAPL | 18.15 | -0.00 | exit signal |
| 2026-11-13T20:30 | VWAP momentum · 1h | buy | AMD | 2.84 | — | entry signal |
| 2026-11-13T20:30 | VWAP momentum · 1h | sell | TSLA | 3.29 | -0.00 | exit signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | UPRO | 9.30 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | TNA | 9.34 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | TECL | 9.34 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | SPY | 9.34 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | MSTR | 9.34 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | sell | MSFT | 9.37 | -0.02 | rebalance down |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | sell | META | 9.50 | 0.04 | rebalance down |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | sell | DOGE-USD | 9.12 | -0.08 | rebalance down |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | sell | AAPL | 18.68 | -0.10 | exit signal |
| 2026-11-13T20:30 | EMA 9/21 cross · 1h | buy | META | 12.95 | — | entry |
| 2026-11-13T20:30 | EMA 9/21 cross · 1h | sell | AMD | 13.09 | 0.52 | exit signal |
| 2026-11-13T20:06 | Agent (ML meta-label) | buy | META | 3.10 | — | entry |
| 2026-11-13T20:06 | Agent (ML meta-label) | buy | AMZN | 4.07 | — | following Supertrend |
| 2026-11-13T20:00 | Bollinger reversion · 1h | buy | MSTR | 3.54 | — | entry |
| 2026-11-13T20:00 | Bollinger reversion · 1h | buy | ETHU | 6.75 | — | rebalance up |
| 2026-11-13T20:00 | Bollinger reversion · 1h | sell | ETH-USD | 10.30 | -0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 21:40:05.000125+00:00 -> 2026-11-13 21:50:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
