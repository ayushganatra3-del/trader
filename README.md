# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T09:00:05.000150+00:00 · 38868 ticks

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

Today: 6672 decisions in 1338 calls, $0.0932 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T09:00 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-10-28T09:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T09:00 | 1 / 4 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.28 | 7.29 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.76 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.29 | 1.29 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.09 | -3.62 | -14.02 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.74 | -0.26 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 7.80 | 3.65 | -2.12 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.89 | -2.11 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Hold BTC | benchmark | 96.90 | -3.10 | 0 | — | 1.31 | 0.39 | -9.28 | 1 |
| 15 | Agent (rotation) | meta | 96.44 | -3.56 | 123 | 31.7 | -4.47 | -2.47 | -7.67 | 186 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.17 | -3.83 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.18 | 1.69 | -8.76 | 203 |
| 20 | Donchian 55/20 · 1h | breakout | 94.00 | -6.00 | 49 | 16.3 | -12.87 | -2.85 | -15.40 | 101 |
| 21 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 22 | Trend pullback · 1h | trend | 93.48 | -6.52 | 96 | 22.9 | -20.76 | -6.87 | -20.97 | 110 |
| 23 | Parabolic SAR · 1h | trend | 93.10 | -6.90 | 122 | 26.2 | -19.72 | -4.79 | -22.91 | 247 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 92.74 | -7.26 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 25 | ADX DI cross · 1h | trend | 92.42 | -7.58 | 120 | 18.3 | -14.09 | -3.02 | -16.18 | 272 |
| 26 | Daily: Momentum burst | daily | 92.07 | -7.93 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 27 | Copy: Insider buying | copy | 91.99 | -8.01 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Squeeze breakout · 1h | breakout | 91.55 | -8.45 | 52 | 23.1 | -4.43 | -1.14 | -12.21 | 96 |
| 29 | Daily: Bullish score | daily | 91.47 | -8.53 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 30 | Max aggression: 5-day momentum | meta | 91.39 | -8.61 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 32 | Volume breakout · 1h | breakout | 90.33 | -9.67 | 113 | 26.5 | -12.16 | -2.51 | -16.10 | 106 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.32 | -6.60 | -12.20 | 209 |
| 34 | Bollinger breakout · 1h | breakout | 89.25 | -10.75 | 109 | 26.6 | -11.13 | -2.15 | -18.15 | 247 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.62 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.97 | -12.03 | 205 | 47.3 | -20.78 | -3.84 | -22.35 | 389 |
| 37 | Keltner breakout · 1h | breakout | 87.47 | -12.53 | 74 | 23.0 | -18.79 | -3.59 | -23.13 | 187 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.10 | -12.90 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 86.09 | -13.91 | 114 | 14.0 | -23.56 | -4.75 | -26.59 | 232 |
| 41 | RSI momentum · 1h | momentum | 85.35 | -14.65 | 104 | 15.4 | -23.86 | -4.73 | -26.87 | 212 |
| 42 | Connors RSI(2) · 1h | reversion | 85.19 | -14.81 | 176 | 40.9 | -23.29 | -7.25 | -23.76 | 176 |
| 43 | EMA 20/50 cross · 1h | trend | 84.96 | -15.04 | 73 | 11.0 | -22.60 | -4.56 | -24.49 | 138 |
| 44 | MACD cross · 1h | trend | 84.67 | -15.33 | 245 | 22.4 | -27.19 | -5.24 | -29.94 | 475 |
| 45 | Ichimoku · 1h | trend | 84.25 | -15.75 | 68 | 11.8 | -19.52 | -3.94 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.99 | -16.01 | 101 | 14.9 | -27.80 | -5.25 | -31.19 | 205 |
| 47 | MFI reversion · 1h | reversion | 83.56 | -16.44 | 274 | 32.1 | -16.25 | -2.51 | -20.70 | 154 |
| 48 | CCI reversion · 1h | reversion | 82.72 | -17.28 | 230 | 45.2 | -23.99 | -3.42 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 82.44 | -17.56 | 99 | 20.2 | -22.85 | -4.30 | -26.02 | 220 |
| 50 | Williams %R · 1h | reversion | 82.27 | -17.73 | 232 | 47.0 | -34.69 | -5.85 | -35.77 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.59 | -18.41 | 111 | 15.3 | -23.72 | -5.05 | -25.67 | 229 |
| 52 | OBV trend · 1h | momentum | 81.00 | -19.00 | 209 | 17.7 | -31.16 | -6.37 | -33.82 | 294 |
| 53 | Agent (ML meta-label) | meta | 80.97 | -19.03 | 982 | 20.6 | -7.15 | -1.21 | -18.40 | 352 |
| 54 | Bollinger reversion · 1h | reversion | 80.93 | -19.07 | 182 | 37.4 | -29.08 | -5.94 | -30.19 | 364 |
| 55 | RSI(14) reversion · 1h | reversion | 80.53 | -19.46 | 107 | 27.1 | -16.17 | -2.99 | -24.48 | 191 |
| 56 | ROC + volume · 1h | momentum | 79.49 | -20.51 | 259 | 25.9 | -29.03 | -5.49 | -31.39 | 376 |
| 57 | Heikin-Ashi · 1h | trend | 78.55 | -21.45 | 302 | 22.5 | -42.59 | -9.29 | -43.96 | 664 |
| 58 | Candlestick reversal · 1h | reversion | 77.55 | -22.45 | 285 | 29.5 | -38.10 | -7.64 | -39.00 | 549 |
| 59 | VWAP momentum · 1h | momentum | 77.21 | -22.79 | 581 | 22.5 | -49.63 | -10.81 | -50.81 | 1240 |
| 60 | EMA 9/21 cross · 1h | trend | 77.13 | -22.87 | 176 | 10.8 | -29.05 | -6.08 | -31.61 | 336 |
| 61 | Three white soldiers | momentum | 76.26 | -23.74 | 333 | 18.6 | -45.24 | -21.31 | -45.47 | 614 |
| 62 | Max aggression: 1-day momentum | meta | 72.70 | -27.30 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 52.25 | -47.75 | 822 | 22.0 | -75.19 | -27.23 | -75.40 | 1569 |
| 64 | Volume breakout | breakout | 51.03 | -48.97 | 501 | 12.4 | -64.65 | -26.53 | -64.79 | 815 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -43.64 | -98.86 | 5119 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.87 | -22.96 | -79.48 | 1413 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.58 | -44.38 | -93.68 | 2528 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.09 | -29.91 | -89.30 | 1922 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.44 | -37.07 | -91.62 | 2341 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.27 | -31.14 | -90.30 | 2190 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -51.16 | -97.86 | 3503 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.15 | -57.61 | -96.20 | 3389 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.12 | -37.04 | -94.13 | 2479 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.45 | -34.21 | -82.59 | 1695 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.99 | -99.42 | 5757 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.06 | -43.20 | -93.14 | 2640 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.38 | -38.20 | -95.38 | 3384 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -74.89 | -99.79 | 6182 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.35 | -44.25 | -92.46 | 2314 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -64.74 | -97.82 | 3592 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -57.38 | -98.65 | 4787 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.26 | -30.06 | -69.51 | 1193 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -56.18 | -94.82 | 2778 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.77 | -39.32 | -84.85 | 1815 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.21 | -99.61 | 6293 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -28.64 | -88.27 | 2221 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.50 | -18.86 | -76.79 | 1683 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.48 | -36.21 | -90.48 | 2261 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -46.53 | -96.24 | 3809 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.06 | -48.51 | -90.06 | 2130 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.19 | -24.81 | -73.50 | 1281 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.26 | -17.99 | -76.47 | 1577 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -48.26 | -96.54 | 4192 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -103.66 | -99.92 | 8289 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-28T09:00 | Donchian 55/20 · 1h | buy | BTC-USD | 5.53 | — | entry signal |
| 2026-10-28T09:00 | Donchian 55/20 · 1h | sell | DOGE-USD | 5.53 | 0.05 | rebalance down |
| 2026-10-28T09:00 | VWAP momentum · 1h | buy | BTC-USD | 4.29 | — | entry signal |
| 2026-10-28T09:00 | Heikin-Ashi · 1h | buy | SOL-USD | 4.91 | — | entry signal |
| 2026-10-28T09:00 | Three white soldiers | sell | ETH-USD | 19.08 | -0.01 | exit signal |
| 2026-10-28T09:00 | Volume breakout | sell | ETH-USD | 10.21 | -0.02 | exit signal |
| 2026-10-28T09:00 | Volume breakout | sell | DOGE-USD | 12.74 | -0.08 | exit signal |
| 2026-10-28T09:00 | ROC + volume | buy | DOGE-USD | 2.64 | — | rebalance up |
| 2026-10-28T09:00 | ROC + volume | sell | SOL-USD | 10.42 | -0.10 | stop-loss |
| 2026-10-28T08:55 | Three white soldiers | sell | SOL-USD | 19.04 | -0.05 | exit signal |
| 2026-10-28T08:55 | Volume breakout | buy | DOGE-USD | 5.13 | — | rebalance up |
| 2026-10-28T08:55 | Volume breakout | sell | XRP-USD | 12.75 | -0.06 | exit signal |
| 2026-10-28T08:55 | Volume breakout | sell | SOL-USD | 10.20 | -0.02 | exit signal |
| 2026-10-28T08:45 | ROC + volume | buy | DOGE-USD | 2.62 | — | rebalance up |
| 2026-10-28T08:45 | ROC + volume | sell | XRP-USD | 2.62 | -0.01 | rebalance down |
| 2026-10-28T08:40 | ROC + volume | buy | DOGE-USD | 7.87 | — | entry signal |
| 2026-10-28T08:40 | ROC + volume | sell | SOL-USD | 2.62 | -0.01 | rebalance down |
| 2026-10-28T08:40 | ROC + volume | sell | ETH-USD | 2.62 | -0.01 | rebalance down |
| 2026-10-28T08:40 | ROC + volume | sell | BTC-USD | 2.63 | -0.01 | rebalance down |
| 2026-10-28T08:32 | Volume breakout | buy | DOGE-USD | 2.56 | — | rebalance up |
| 2026-10-28T08:32 | Volume breakout | sell | SOL-USD | 2.56 | 0.00 | rebalance down |
| 2026-10-28T08:30 | Volume breakout | buy | DOGE-USD | 5.13 | — | entry signal |
| 2026-10-28T08:30 | Volume breakout | sell | ETH-USD | 2.57 | -0.00 | rebalance down |
| 2026-10-28T08:30 | Volume breakout | sell | BTC-USD | 2.56 | -0.00 | rebalance down |
| 2026-10-28T08:30 | ROC + volume | buy | XRP-USD | 13.15 | — | entry signal |
| 2026-10-28T08:30 | ROC + volume | buy | SOL-USD | 13.15 | — | entry signal |
| 2026-10-28T08:30 | ROC + volume | buy | ETH-USD | 13.15 | — | entry signal |
| 2026-10-28T08:30 | ROC + volume | buy | BTC-USD | 13.15 | — | entry signal |
| 2026-10-28T08:16 | Three white soldiers | sell | DOGE-USD | 18.97 | -0.14 | exit signal |
| 2026-10-28T08:16 | Volume breakout | buy | SOL-USD | 12.77 | — | entry |
| 2026-10-28T08:16 | Volume breakout | sell | DOGE-USD | 12.73 | -0.09 | exit signal |
| 2026-10-28T08:10 | Three white soldiers | buy | BTC-USD | 19.08 | — | entry signal |
| 2026-10-28T08:00 | VWAP momentum · 1h | buy | ETH-USD | 4.54 | — | entry signal |
| 2026-10-28T08:00 | Trend pullback · 1h | buy | XRP-USD | 23.39 | — | entry signal |
| 2026-10-28T08:00 | Parabolic SAR · 1h | sell | XRP-USD | 11.39 | 0.13 | exit signal |
| 2026-10-28T08:00 | Three white soldiers | buy | SOL-USD | 19.09 | — | entry signal |
| 2026-10-28T08:00 | Volume breakout | buy | XRP-USD | 12.81 | — | entry signal |
| 2026-10-28T08:00 | Volume breakout | buy | ETH-USD | 12.81 | — | entry signal |
| 2026-10-28T07:55 | Three white soldiers | buy | ETH-USD | 19.10 | — | entry signal |
| 2026-10-28T07:55 | Volume breakout | buy | BTC-USD | 12.81 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 09:00:05.000150+00:00 -> 2026-10-28 09:10:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
