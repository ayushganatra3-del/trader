# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T01:30:05.000148+00:00 · 38497 ticks

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

Today: 1125 decisions in 225 calls, $0.0158 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T01:30 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-10-28T01:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T01:30 | 2 / 3 / 0 | ETH-USD 60% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.15 | 7.15 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.76 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.16 | 1.16 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.15 | -3.64 | -14.07 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.62 | -0.39 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 8.16 | 3.76 | -2.29 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.77 | -2.23 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.40 | -3.60 | 123 | 31.7 | -2.82 | -1.43 | -7.67 | 188 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.05 | -3.95 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 16 | Hold BTC | benchmark | 95.95 | -4.05 | 0 | — | 2.09 | 0.51 | -9.28 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.15 | 1.68 | -8.76 | 203 |
| 20 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 21 | Donchian 55/20 · 1h | breakout | 93.61 | -6.39 | 49 | 16.3 | -13.05 | -2.90 | -15.40 | 99 |
| 22 | Trend pullback · 1h | trend | 93.47 | -6.53 | 96 | 22.9 | -23.23 | -7.38 | -23.27 | 113 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.62 | -7.38 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 24 | Parabolic SAR · 1h | trend | 92.62 | -7.38 | 121 | 25.6 | -19.99 | -4.87 | -22.91 | 247 |
| 25 | ADX DI cross · 1h | trend | 91.99 | -8.01 | 120 | 18.3 | -14.10 | -3.04 | -15.89 | 271 |
| 26 | Daily: Momentum burst | daily | 91.98 | -8.02 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 27 | Copy: Insider buying | copy | 91.88 | -8.12 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.36 | -8.64 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.27 | -8.73 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 91.07 | -8.93 | 52 | 23.1 | -4.51 | -1.17 | -12.21 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.34 | -9.66 | 112 | 26.8 | -11.37 | -2.30 | -16.10 | 111 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.32 | -6.60 | -12.20 | 209 |
| 34 | Bollinger breakout · 1h | breakout | 89.01 | -10.98 | 109 | 26.6 | -11.29 | -2.18 | -18.15 | 246 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.62 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.89 | -12.11 | 205 | 47.3 | -20.56 | -3.81 | -22.35 | 388 |
| 37 | Keltner breakout · 1h | breakout | 87.36 | -12.64 | 74 | 23.0 | -18.84 | -3.60 | -23.13 | 186 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.02 | -12.98 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 85.89 | -14.11 | 114 | 14.0 | -23.68 | -4.78 | -26.59 | 230 |
| 41 | RSI momentum · 1h | momentum | 85.20 | -14.80 | 104 | 15.4 | -23.99 | -4.77 | -26.87 | 211 |
| 42 | Connors RSI(2) · 1h | reversion | 85.16 | -14.84 | 176 | 40.9 | -23.72 | -7.42 | -24.36 | 179 |
| 43 | EMA 20/50 cross · 1h | trend | 84.56 | -15.44 | 73 | 11.0 | -22.67 | -4.60 | -24.49 | 136 |
| 44 | MACD cross · 1h | trend | 84.42 | -15.58 | 244 | 22.1 | -27.93 | -5.43 | -29.94 | 477 |
| 45 | Ichimoku · 1h | trend | 84.15 | -15.85 | 68 | 11.8 | -19.83 | -4.02 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.75 | -16.25 | 101 | 14.9 | -28.24 | -5.35 | -31.19 | 204 |
| 47 | MFI reversion · 1h | reversion | 83.51 | -16.49 | 274 | 32.1 | -16.32 | -2.52 | -20.70 | 154 |
| 48 | CCI reversion · 1h | reversion | 82.62 | -17.38 | 230 | 45.2 | -24.43 | -3.47 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 82.19 | -17.81 | 99 | 20.2 | -22.93 | -4.33 | -26.02 | 219 |
| 50 | Williams %R · 1h | reversion | 82.17 | -17.83 | 232 | 47.0 | -34.83 | -5.87 | -35.93 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.40 | -18.60 | 111 | 15.3 | -24.21 | -5.18 | -25.67 | 230 |
| 52 | Agent (ML meta-label) | meta | 80.87 | -19.13 | 982 | 20.6 | -10.83 | -1.96 | -18.02 | 359 |
| 53 | Bollinger reversion · 1h | reversion | 80.85 | -19.15 | 182 | 37.4 | -29.08 | -5.94 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.71 | -19.29 | 209 | 17.7 | -31.40 | -6.44 | -33.82 | 294 |
| 55 | RSI(14) reversion · 1h | reversion | 80.44 | -19.56 | 107 | 27.1 | -14.96 | -2.75 | -24.48 | 188 |
| 56 | ROC + volume · 1h | momentum | 79.39 | -20.61 | 259 | 25.9 | -29.87 | -5.69 | -31.96 | 379 |
| 57 | Heikin-Ashi · 1h | trend | 78.45 | -21.55 | 301 | 22.6 | -42.99 | -9.43 | -44.66 | 666 |
| 58 | Candlestick reversal · 1h | reversion | 77.45 | -22.55 | 285 | 29.5 | -38.60 | -7.66 | -39.40 | 551 |
| 59 | VWAP momentum · 1h | momentum | 77.11 | -22.89 | 578 | 22.7 | -49.72 | -10.85 | -51.08 | 1236 |
| 60 | Three white soldiers | momentum | 76.92 | -23.08 | 326 | 19.0 | -44.98 | -20.95 | -45.01 | 608 |
| 61 | EMA 9/21 cross · 1h | trend | 76.81 | -23.20 | 176 | 10.8 | -29.61 | -6.24 | -31.61 | 337 |
| 62 | Max aggression: 1-day momentum | meta | 72.61 | -27.39 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 53.17 | -46.83 | 816 | 22.2 | -74.76 | -26.59 | -74.99 | 1568 |
| 64 | Volume breakout | breakout | 51.79 | -48.21 | 491 | 12.6 | -63.74 | -25.78 | -64.25 | 809 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -43.11 | -98.84 | 5110 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.00 | -23.18 | -79.67 | 1416 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -44.65 | -93.74 | 2531 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.99 | -29.47 | -89.25 | 1919 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.43 | -37.00 | -91.61 | 2341 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.41 | -31.82 | -90.43 | 2196 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -52.21 | -97.89 | 3510 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.13 | -56.82 | -96.21 | 3386 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.11 | -36.25 | -94.11 | 2470 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.19 | -33.34 | -82.47 | 1690 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.53 | -99.42 | 5759 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -42.13 | -93.13 | 2635 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -38.72 | -95.41 | 3388 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.96 | -99.78 | 6179 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.27 | -43.27 | -92.43 | 2317 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -62.34 | -97.83 | 3596 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.26 | -98.66 | 4791 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.81 | -29.13 | -68.96 | 1185 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -55.05 | -94.75 | 2778 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.54 | -38.27 | -84.66 | 1810 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -63.41 | -99.61 | 6296 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -28.63 | -88.27 | 2224 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.50 | -18.86 | -76.79 | 1682 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.54 | -36.52 | -90.55 | 2269 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -46.84 | -96.26 | 3814 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.05 | -48.07 | -90.05 | 2129 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.06 | -24.61 | -73.53 | 1279 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.28 | -18.01 | -76.47 | 1578 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.53 | -47.97 | -96.53 | 4190 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.52 | -99.92 | 8290 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-28T01:15 | Volume breakout · 1h | buy | ETH-USD | 5.39 | — | rebalance up |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | XRP-USD | 6.47 | 0.09 | exit signal |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | ETH-USD | 5.45 | 0.02 | exit signal |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | BTC-USD | 2.95 | 0.01 | exit signal |
| 2026-10-28T01:00 | Heikin-Ashi · 1h | sell | BTC-USD | 3.90 | -0.02 | exit signal |
| 2026-10-28T00:20 | ROC + volume | sell | DOGE-USD | 13.22 | -0.14 | stop-loss |
| 2026-10-28T00:05 | ROC + volume | sell | XRP-USD | 13.22 | -0.14 | stop-loss |
| 2026-10-28T00:00 | Donchian 55/20 · 1h | buy | XRP-USD | 3.96 | — | entry signal |
| 2026-10-28T00:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 18.74 | — | entry signal |
| 2026-10-27T23:50 | ROC + volume | buy | XRP-USD | 13.36 | — | entry signal |
| 2026-10-27T23:50 | ROC + volume | buy | DOGE-USD | 13.36 | — | entry signal |
| 2026-10-27T22:25 | Volume breakout | sell | XRP-USD | 12.96 | -0.11 | exit signal |
| 2026-10-27T22:00 | Triple EMA stack · 1h | buy | BTC-USD | 4.60 | — | entry |
| 2026-10-27T22:00 | Triple EMA stack · 1h | sell | XRP-USD | 4.60 | 0.08 | rebalance down |
| 2026-10-27T22:00 | Volume breakout | sell | SOL-USD | 12.94 | -0.13 | stop-loss |
| 2026-10-27T22:00 | Volume breakout | sell | ETH-USD | 12.94 | -0.13 | stop-loss |
| 2026-10-27T22:00 | ROC + volume | sell | SOL-USD | 13.33 | -0.13 | stop-loss |
| 2026-10-27T22:00 | ROC + volume | sell | ETH-USD | 13.33 | -0.13 | stop-loss |
| 2026-10-27T21:45 | Volume breakout | sell | BTC-USD | 12.95 | -0.12 | stop-loss |
| 2026-10-27T21:45 | ROC + volume | sell | BTC-USD | 13.34 | -0.12 | stop-loss |
| 2026-10-27T21:35 | Volume breakout | buy | XRP-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | Volume breakout | buy | SOL-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | Volume breakout | buy | ETH-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | Volume breakout | buy | BTC-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | ROC + volume | buy | SOL-USD | 13.46 | — | entry signal |
| 2026-10-27T21:35 | ROC + volume | buy | ETH-USD | 13.46 | — | entry signal |
| 2026-10-27T21:35 | ROC + volume | buy | BTC-USD | 13.46 | — | entry signal |
| 2026-10-27T21:00 | Heikin-Ashi · 1h | sell | XRP-USD | 4.32 | -0.03 | exit signal |
| 2026-10-27T21:00 | Heikin-Ashi · 1h | sell | ETH-USD | 1.35 | -0.01 | exit signal |
| 2026-10-27T20:20 | Three white soldiers | sell | SOL-USD | 19.16 | -0.12 | exit signal |
| 2026-10-27T20:15 | Three white soldiers | sell | ETH-USD | 19.20 | -0.15 | exit signal |
| 2026-10-27T20:00 | OBV trend · 1h | buy | BTC-USD | 7.33 | — | entry signal |
| 2026-10-27T20:00 | OBV trend · 1h | sell | XRP-USD | 4.13 | 0.02 | rebalance down |
| 2026-10-27T20:00 | OBV trend · 1h | sell | DOGE-USD | 4.14 | -0.00 | rebalance down |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 2.04 | — | entry signal |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 10.56 | — | entry signal |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 6.30 | 0.09 | rebalance down |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 6.29 | 0.00 | rebalance down |
| 2026-10-27T20:00 | Three white soldiers | buy | SOL-USD | 19.28 | — | entry |
| 2026-10-27T19:55 | Agent (rotation) | sell | TQQQ | 32.22 | 0.12 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 01:30:05.000148+00:00 -> 2026-10-28 01:40:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
