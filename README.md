# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T11:30:05.000158+00:00 · 38980 ticks

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
| Copy: Insider buying | 2026-10-28 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.91 · VIX 17.52 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 8349 decisions in 1674 calls, $0.1166 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T11:30 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-28T11:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T11:30 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.31 | +6.31% | 11 |
| MACD zero-line | MSFT | 2.19 | +0.66% | 5 |
| VWAP momentum · 1h | LABU | 2.05 | +21.96% | 3 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.37 | 7.37 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.37 | 1.37 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.19 | -3.65 | -14.07 | 148 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.82 | -0.18 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 7.46 | 3.49 | -2.42 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.97 | -2.03 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Hold BTC | benchmark | 96.87 | -3.13 | 0 | — | 2.05 | 0.51 | -9.28 | 1 |
| 15 | Agent (rotation) | meta | 96.46 | -3.54 | 123 | 31.7 | -3.52 | -2.07 | -7.67 | 175 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.25 | -3.75 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.18 | 1.69 | -8.76 | 203 |
| 20 | Donchian 55/20 · 1h | breakout | 94.05 | -5.95 | 49 | 16.3 | -12.97 | -2.88 | -15.40 | 101 |
| 21 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 22 | Trend pullback · 1h | trend | 93.46 | -6.54 | 96 | 22.9 | -20.83 | -6.90 | -21.02 | 110 |
| 23 | Parabolic SAR · 1h | trend | 93.10 | -6.89 | 122 | 26.2 | -19.77 | -4.80 | -22.91 | 247 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 92.81 | -7.19 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 25 | ADX DI cross · 1h | trend | 92.47 | -7.53 | 120 | 18.3 | -14.11 | -3.03 | -16.18 | 272 |
| 26 | Daily: Momentum burst | daily | 92.13 | -7.88 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 27 | Copy: Insider buying | copy | 92.07 | -7.93 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.55 | -8.45 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Squeeze breakout · 1h | breakout | 91.47 | -8.53 | 52 | 23.1 | -4.28 | -1.11 | -12.21 | 95 |
| 30 | Max aggression: 5-day momentum | meta | 91.46 | -8.54 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 32 | Volume breakout · 1h | breakout | 90.37 | -9.63 | 113 | 26.5 | -12.82 | -2.67 | -16.02 | 105 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.02 | -6.38 | -12.20 | 209 |
| 34 | Bollinger breakout · 1h | breakout | 89.28 | -10.72 | 109 | 26.6 | -11.16 | -2.15 | -18.15 | 247 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.62 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 88.03 | -11.97 | 205 | 47.3 | -20.55 | -3.80 | -22.35 | 388 |
| 37 | Keltner breakout · 1h | breakout | 87.54 | -12.46 | 74 | 23.0 | -18.79 | -3.59 | -23.13 | 187 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.15 | -12.85 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 86.15 | -13.85 | 114 | 14.0 | -23.58 | -4.76 | -26.59 | 232 |
| 41 | RSI momentum · 1h | momentum | 85.39 | -14.61 | 104 | 15.4 | -23.72 | -4.71 | -26.87 | 212 |
| 42 | Connors RSI(2) · 1h | reversion | 85.20 | -14.80 | 176 | 40.9 | -23.29 | -7.25 | -23.76 | 176 |
| 43 | EMA 20/50 cross · 1h | trend | 84.97 | -15.03 | 73 | 11.0 | -22.34 | -4.52 | -24.49 | 137 |
| 44 | MACD cross · 1h | trend | 84.72 | -15.28 | 245 | 22.4 | -27.27 | -5.27 | -29.94 | 475 |
| 45 | Ichimoku · 1h | trend | 84.32 | -15.68 | 68 | 11.8 | -19.57 | -3.95 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 84.02 | -15.98 | 101 | 14.9 | -27.98 | -5.29 | -31.19 | 205 |
| 47 | MFI reversion · 1h | reversion | 83.60 | -16.40 | 274 | 32.1 | -16.05 | -2.47 | -20.70 | 153 |
| 48 | CCI reversion · 1h | reversion | 82.78 | -17.22 | 230 | 45.2 | -23.71 | -3.38 | -28.06 | 461 |
| 49 | Donchian 20/10 · 1h | breakout | 82.47 | -17.53 | 99 | 20.2 | -22.81 | -4.30 | -26.02 | 220 |
| 50 | Williams %R · 1h | reversion | 82.33 | -17.67 | 232 | 47.0 | -34.69 | -5.85 | -35.77 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.62 | -18.38 | 111 | 15.3 | -23.74 | -5.05 | -25.67 | 229 |
| 52 | OBV trend · 1h | momentum | 81.03 | -18.97 | 209 | 17.7 | -31.04 | -6.35 | -33.78 | 294 |
| 53 | Agent (ML meta-label) | meta | 81.03 | -18.97 | 982 | 20.6 | -10.15 | -1.97 | -17.21 | 361 |
| 54 | Bollinger reversion · 1h | reversion | 80.98 | -19.02 | 182 | 37.4 | -29.08 | -5.94 | -30.19 | 364 |
| 55 | RSI(14) reversion · 1h | reversion | 80.59 | -19.41 | 107 | 27.1 | -17.30 | -3.19 | -24.48 | 192 |
| 56 | ROC + volume · 1h | momentum | 79.56 | -20.44 | 259 | 25.9 | -28.94 | -5.44 | -31.48 | 377 |
| 57 | Heikin-Ashi · 1h | trend | 78.60 | -21.41 | 302 | 22.5 | -42.63 | -9.31 | -43.95 | 666 |
| 58 | Candlestick reversal · 1h | reversion | 77.61 | -22.39 | 285 | 29.5 | -37.49 | -7.60 | -38.27 | 549 |
| 59 | VWAP momentum · 1h | momentum | 77.25 | -22.75 | 581 | 22.5 | -49.34 | -10.76 | -50.49 | 1234 |
| 60 | EMA 9/21 cross · 1h | trend | 77.17 | -22.83 | 176 | 10.8 | -29.47 | -6.20 | -31.61 | 337 |
| 61 | Three white soldiers | momentum | 76.19 | -23.81 | 334 | 18.6 | -45.36 | -21.41 | -45.54 | 614 |
| 62 | Max aggression: 1-day momentum | meta | 72.76 | -27.24 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 52.08 | -47.92 | 826 | 21.9 | -75.31 | -27.38 | -75.52 | 1570 |
| 64 | Volume breakout | breakout | 51.00 | -49.00 | 502 | 12.4 | -64.62 | -26.61 | -64.76 | 813 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -43.46 | -98.85 | 5117 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.88 | -23.06 | -79.17 | 1409 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.67 | -45.43 | -93.71 | 2529 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.26 | -30.50 | -89.34 | 1921 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.61 | -38.14 | -91.64 | 2341 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.44 | -31.58 | -90.44 | 2198 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.85 | -52.01 | -97.87 | 3502 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.25 | -59.91 | -96.26 | 3393 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.22 | -37.29 | -94.22 | 2483 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.61 | -34.64 | -82.61 | 1696 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -52.10 | -99.41 | 5748 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.10 | -43.59 | -93.15 | 2640 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.36 | -37.62 | -95.36 | 3391 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -75.75 | -99.78 | 6175 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.39 | -44.77 | -92.42 | 2311 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -65.68 | -97.82 | 3592 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -56.77 | -98.65 | 4786 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.34 | -30.13 | -69.59 | 1193 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.78 | -56.49 | -94.84 | 2779 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.88 | -39.56 | -84.95 | 1818 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -63.55 | -99.61 | 6295 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -28.64 | -88.27 | 2221 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.35 | -18.67 | -76.79 | 1678 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.49 | -36.17 | -90.54 | 2261 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.23 | -46.22 | -96.23 | 3806 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.99 | -48.15 | -90.11 | 2134 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.47 | -25.16 | -73.49 | 1281 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.26 | -17.99 | -76.49 | 1577 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -48.51 | -96.56 | 4196 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -104.72 | -99.92 | 8289 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-28T10:00 | Heikin-Ashi · 1h | buy | BTC-USD | 4.36 | — | entry signal |
| 2026-10-28T09:30 | Three white soldiers | sell | BTC-USD | 19.03 | -0.05 | exit signal |
| 2026-10-28T09:30 | Volume breakout | sell | BTC-USD | 10.23 | -0.02 | exit signal |
| 2026-10-28T09:30 | ROC + volume | sell | BTC-USD | 10.45 | -0.07 | exit signal |
| 2026-10-28T09:25 | ROC + volume | sell | XRP-USD | 10.43 | -0.09 | stop-loss |
| 2026-10-28T09:10 | ROC + volume | sell | ETH-USD | 10.42 | -0.09 | stop-loss |
| 2026-10-28T09:05 | ROC + volume | sell | DOGE-USD | 13.01 | -0.12 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 11:30:05.000158+00:00 -> 2026-10-28 11:40:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
