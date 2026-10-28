# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T07:30:05.000111+00:00 · 38800 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.98 (-10.02%)

Closed trades 116, win rate 38.8%, fees £3.50, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-27 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.91 · VIX 17.52 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 5652 decisions in 1134 calls, $0.0790 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T07:30 | 2 / 0 / 3 | cash |  |
| Breezy | 2026-10-28T07:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T07:30 | 2 / 1 / 2 | ETH-USD 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.31 | +6.31% | 11 |
| MACD zero-line | MSFT | 2.19 | +0.66% | 5 |
| VWAP reversion | META | 2.17 | +2.15% | 4 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP momentum · 1h | TSLA | 1.89 | +11.08% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.36 | 7.36 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.76 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.36 | 1.36 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.15 | -3.64 | -14.07 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.81 | -0.19 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 7.80 | 3.65 | -2.12 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.96 | -2.04 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.46 | -3.54 | 123 | 31.7 | -4.47 | -2.47 | -7.67 | 186 |
| 15 | Hold BTC | benchmark | 96.32 | -3.68 | 0 | — | 0.92 | 0.32 | -9.28 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.24 | -3.76 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.18 | 1.69 | -8.76 | 203 |
| 20 | Donchian 55/20 · 1h | breakout | 93.97 | -6.03 | 49 | 16.3 | -12.94 | -2.87 | -15.40 | 99 |
| 21 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 22 | Trend pullback · 1h | trend | 93.56 | -6.44 | 96 | 22.9 | -20.73 | -6.86 | -20.95 | 109 |
| 23 | Parabolic SAR · 1h | trend | 92.92 | -7.08 | 121 | 25.6 | -19.89 | -4.84 | -22.91 | 247 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 92.80 | -7.20 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 25 | ADX DI cross · 1h | trend | 92.31 | -7.69 | 120 | 18.3 | -13.97 | -3.01 | -15.89 | 271 |
| 26 | Daily: Momentum burst | daily | 92.12 | -7.88 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 27 | Copy: Insider buying | copy | 92.05 | -7.95 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.53 | -8.47 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.45 | -8.55 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 30 | Squeeze breakout · 1h | breakout | 91.26 | -8.74 | 52 | 23.1 | -4.49 | -1.17 | -12.21 | 95 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 32 | Volume breakout · 1h | breakout | 90.36 | -9.64 | 113 | 26.5 | -12.16 | -2.51 | -16.10 | 106 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.32 | -6.60 | -12.20 | 209 |
| 34 | Bollinger breakout · 1h | breakout | 89.19 | -10.81 | 109 | 26.6 | -11.24 | -2.17 | -18.15 | 246 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.62 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 88.02 | -11.98 | 205 | 47.3 | -20.55 | -3.80 | -22.35 | 388 |
| 37 | Keltner breakout · 1h | breakout | 87.53 | -12.47 | 74 | 23.0 | -18.84 | -3.60 | -23.13 | 187 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.14 | -12.86 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 86.10 | -13.90 | 114 | 14.0 | -23.67 | -4.78 | -26.59 | 232 |
| 41 | RSI momentum · 1h | momentum | 85.35 | -14.65 | 104 | 15.4 | -24.18 | -4.80 | -26.87 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 85.20 | -14.80 | 176 | 40.9 | -23.19 | -7.22 | -23.85 | 177 |
| 43 | EMA 20/50 cross · 1h | trend | 84.82 | -15.18 | 73 | 11.0 | -22.60 | -4.58 | -24.49 | 137 |
| 44 | MACD cross · 1h | trend | 84.60 | -15.40 | 245 | 22.4 | -27.57 | -5.34 | -29.94 | 476 |
| 45 | Ichimoku · 1h | trend | 84.31 | -15.69 | 68 | 11.8 | -19.70 | -3.99 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.94 | -16.06 | 101 | 14.9 | -28.10 | -5.32 | -31.19 | 205 |
| 47 | MFI reversion · 1h | reversion | 83.59 | -16.41 | 274 | 32.1 | -16.29 | -2.52 | -20.70 | 154 |
| 48 | CCI reversion · 1h | reversion | 82.77 | -17.23 | 230 | 45.2 | -24.22 | -3.45 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 82.40 | -17.60 | 99 | 20.2 | -22.88 | -4.31 | -26.02 | 219 |
| 50 | Williams %R · 1h | reversion | 82.32 | -17.68 | 232 | 47.0 | -34.67 | -5.85 | -35.75 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.58 | -18.42 | 111 | 15.3 | -23.72 | -5.05 | -25.67 | 229 |
| 52 | Agent (ML meta-label) | meta | 81.02 | -18.98 | 982 | 20.6 | -9.97 | -1.95 | -17.65 | 355 |
| 53 | Bollinger reversion · 1h | reversion | 80.97 | -19.03 | 182 | 37.4 | -29.08 | -5.94 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.93 | -19.07 | 209 | 17.7 | -31.36 | -6.42 | -33.82 | 295 |
| 55 | RSI(14) reversion · 1h | reversion | 80.58 | -19.42 | 107 | 27.1 | -15.85 | -2.95 | -24.48 | 183 |
| 56 | ROC + volume · 1h | momentum | 79.54 | -20.45 | 259 | 25.9 | -29.17 | -5.53 | -31.39 | 376 |
| 57 | Heikin-Ashi · 1h | trend | 78.58 | -21.42 | 302 | 22.5 | -42.60 | -9.29 | -43.96 | 663 |
| 58 | Candlestick reversal · 1h | reversion | 77.60 | -22.40 | 285 | 29.5 | -35.52 | -7.17 | -36.41 | 536 |
| 59 | VWAP momentum · 1h | momentum | 77.21 | -22.79 | 581 | 22.5 | -49.56 | -10.79 | -50.79 | 1237 |
| 60 | EMA 9/21 cross · 1h | trend | 77.05 | -22.95 | 176 | 10.8 | -29.55 | -6.22 | -31.61 | 337 |
| 61 | Three white soldiers | momentum | 76.45 | -23.55 | 330 | 18.8 | -45.12 | -21.20 | -45.28 | 610 |
| 62 | Max aggression: 1-day momentum | meta | 72.75 | -27.25 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 52.59 | -47.41 | 821 | 22.0 | -75.27 | -27.12 | -75.27 | 1567 |
| 64 | Volume breakout | breakout | 51.29 | -48.71 | 496 | 12.5 | -64.44 | -26.32 | -64.58 | 809 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -43.31 | -98.85 | 5113 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.19 | -23.43 | -79.62 | 1412 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -44.82 | -93.68 | 2528 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.11 | -29.97 | -89.28 | 1918 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.46 | -37.24 | -91.62 | 2338 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.37 | -31.54 | -90.37 | 2196 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.85 | -51.98 | -97.86 | 3502 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -58.70 | -96.21 | 3389 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.06 | -36.76 | -94.06 | 2466 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.49 | -34.31 | -82.56 | 1693 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.81 | -99.42 | 5754 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.17 | -43.96 | -93.17 | 2640 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -38.48 | -95.41 | 3389 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -76.32 | -99.79 | 6182 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.35 | -44.29 | -92.45 | 2311 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -65.32 | -97.82 | 3593 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -57.03 | -98.65 | 4786 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.15 | -29.94 | -69.40 | 1188 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -56.10 | -94.80 | 2774 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.81 | -39.46 | -84.87 | 1814 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.08 | -99.61 | 6293 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -28.61 | -88.27 | 2222 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.35 | -18.67 | -76.79 | 1678 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.47 | -36.14 | -90.47 | 2260 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.25 | -46.51 | -96.25 | 3809 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.08 | -48.61 | -90.08 | 2130 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.22 | -24.85 | -73.50 | 1279 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.24 | -17.96 | -76.47 | 1575 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -48.41 | -96.55 | 4193 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -103.34 | -99.92 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-28T06:50 | Three white soldiers | sell | SOL-USD | 19.02 | -0.13 | exit signal |
| 2026-10-28T06:45 | Three white soldiers | buy | SOL-USD | 19.14 | — | entry |
| 2026-10-28T06:40 | Three white soldiers | sell | SOL-USD | 19.05 | -0.14 | exit signal |
| 2026-10-28T06:40 | Three white soldiers | sell | DOGE-USD | 19.10 | -0.10 | target is flat |
| 2026-10-28T06:20 | Three white soldiers | buy | SOL-USD | 19.19 | — | entry signal |
| 2026-10-28T06:15 | Three white soldiers | buy | DOGE-USD | 19.20 | — | entry signal |
| 2026-10-28T06:01 | Volume breakout · 1h | sell | ETH-USD | 22.47 | -0.11 | exit signal |
| 2026-10-28T06:01 | VWAP momentum · 1h | sell | ETH-USD | 4.03 | -0.03 | exit signal |
| 2026-10-28T06:01 | VWAP momentum · 1h | sell | BTC-USD | 4.04 | -0.02 | exit signal |
| 2026-10-28T06:01 | MACD cross · 1h | buy | DOGE-USD | 3.68 | — | entry |
| 2026-10-28T06:01 | MACD cross · 1h | sell | XRP-USD | 4.94 | 0.07 | exit signal |
| 2026-10-28T05:01 | VWAP momentum · 1h | sell | XRP-USD | 4.01 | -0.05 | exit signal |
| 2026-10-28T05:01 | Heikin-Ashi · 1h | sell | ETH-USD | 4.87 | -0.04 | exit signal |
| 2026-10-28T04:25 | ROC + volume | sell | DOGE-USD | 13.07 | -0.15 | stop-loss |
| 2026-10-28T04:10 | ROC + volume | sell | SOL-USD | 13.09 | -0.12 | stop-loss |
| 2026-10-28T04:00 | Heikin-Ashi · 1h | buy | ETH-USD | 4.91 | — | entry signal |
| 2026-10-28T03:55 | Volume breakout | sell | SOL-USD | 12.74 | -0.11 | exit signal |
| 2026-10-28T03:35 | Volume breakout | buy | SOL-USD | 12.85 | — | entry signal |
| 2026-10-28T03:35 | ROC + volume | buy | SOL-USD | 13.22 | — | entry signal |
| 2026-10-28T03:35 | ROC + volume | buy | DOGE-USD | 13.22 | — | entry signal |
| 2026-10-28T03:15 | ROC + volume | sell | ETH-USD | 13.20 | -0.09 | exit signal |
| 2026-10-28T02:45 | ROC + volume | sell | XRP-USD | 13.19 | -0.10 | stop-loss |
| 2026-10-28T02:45 | ROC + volume | sell | SOL-USD | 13.18 | -0.11 | exit signal |
| 2026-10-28T02:30 | Three white soldiers | sell | XRP-USD | 19.13 | -0.10 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | XRP-USD | 12.88 | -0.07 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | SOL-USD | 12.83 | -0.12 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | ETH-USD | 12.83 | -0.12 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | BTC-USD | 12.85 | -0.09 | exit signal |
| 2026-10-28T02:20 | Volume breakout | buy | SOL-USD | 12.94 | — | entry signal |
| 2026-10-28T02:20 | Volume breakout | buy | ETH-USD | 12.94 | — | entry signal |
| 2026-10-28T02:20 | ROC + volume | buy | SOL-USD | 13.30 | — | entry signal |
| 2026-10-28T02:15 | Volume breakout | buy | BTC-USD | 12.94 | — | entry signal |
| 2026-10-28T02:15 | ROC + volume | buy | ETH-USD | 13.29 | — | entry signal |
| 2026-10-28T02:00 | VWAP momentum · 1h | buy | XRP-USD | 4.06 | — | entry signal |
| 2026-10-28T02:00 | VWAP momentum · 1h | buy | ETH-USD | 4.06 | — | entry signal |
| 2026-10-28T02:00 | VWAP momentum · 1h | buy | BTC-USD | 4.06 | — | entry signal |
| 2026-10-28T01:45 | Volume breakout · 1h | buy | ETH-USD | 9.63 | — | rebalance up |
| 2026-10-28T01:45 | Three white soldiers | buy | XRP-USD | 19.23 | — | entry signal |
| 2026-10-28T01:45 | Volume breakout | buy | XRP-USD | 12.95 | — | entry signal |
| 2026-10-28T01:45 | ROC + volume | buy | XRP-USD | 13.29 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 07:30:05.000111+00:00 -> 2026-10-28 07:40:05.000111+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
