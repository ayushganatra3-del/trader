# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T08:25:05.000144+00:00 · 28164 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.97 (-8.03%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.14 | -0.23 |
| SQQQ | 19.17 | +0.79 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, FLSC 12%, REF 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 6105 decisions in 1221 calls, $0.0853 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T08:25 | 0 / 5 / 0 | cash |  |
| Breezy | 2026-10-19T08:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T08:25 | 1 / 4 / 0 | COIN 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | BITX | 2.21 | +2.15% | 7 |
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.06 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.44 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.00 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.77 | 4.77 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.89 | -0.12 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.51 | -0.49 | 64 | 39.1 | -11.34 | -3.26 | -13.80 | 139 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.87 | -1.12 | 36 | 16.7 | -6.73 | -0.81 | -22.12 | 110 |
| 12 | Max aggression: 5-day momentum | meta | 98.70 | -1.30 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.57 | -1.43 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Hold BTC | benchmark | 98.17 | -1.83 | 0 | — | 28.67 | 3.37 | -8.68 | 1 |
| 16 | Copy: Insider buying | copy | 98.12 | -1.88 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 17 | Agent (rotation) | meta | 97.11 | -2.89 | 108 | 33.3 | -4.46 | -2.28 | -5.67 | 262 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.40 | -3.60 | 0 | — | -6.59 | -3.57 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.39 | -3.61 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 21 | Three white soldiers · 1h | momentum | 96.11 | -3.89 | 12 | 0.0 | 0.69 | 0.41 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.52 | -4.48 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 94.98 | -5.02 | 82 | 19.5 | -11.80 | -2.27 | -13.34 | 256 |
| 24 | Parabolic SAR · 1h | trend | 93.46 | -6.54 | 97 | 21.6 | -10.73 | -1.68 | -22.75 | 273 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 3.26 | 0.78 | -9.46 | 97 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 27 | Daily: Momentum burst | daily | 92.96 | -7.04 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.47 | -7.53 | 55 | 14.5 | -18.37 | -3.15 | -21.23 | 129 |
| 29 | Agent (aggressive) | meta | 92.13 | -7.87 | 38 | 31.6 | -5.82 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.97 | -8.03 | 77 | 39.0 | -8.69 | -5.27 | -13.06 | 231 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.95 | -9.05 | 77 | 16.9 | -16.93 | -2.93 | -27.42 | 221 |
| 34 | Daily: Bullish score | daily | 90.63 | -9.38 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.33 | 1.11 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.11 | -9.89 | 52 | 15.4 | -18.06 | -3.39 | -18.38 | 116 |
| 37 | Triple EMA stack · 1h | trend | 89.93 | -10.07 | 81 | 16.0 | -19.80 | -2.52 | -33.23 | 231 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.45 | -10.55 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.21 | -10.79 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.21 | -10.79 | 52 | 23.1 | -7.97 | -0.96 | -27.05 | 204 |
| 41 | Supertrend · 1h | trend | 89.00 | -11.00 | 85 | 11.8 | -22.31 | -4.57 | -26.38 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 87.96 | -12.04 | 145 | 40.0 | -24.75 | -7.60 | -25.12 | 218 |
| 43 | MACD cross · 1h | trend | 87.74 | -12.26 | 181 | 21.5 | -23.60 | -4.10 | -30.63 | 460 |
| 44 | OBV trend · 1h | momentum | 87.56 | -12.44 | 170 | 18.2 | -19.01 | -2.37 | -33.85 | 320 |
| 45 | Stochastic reversion · 1h | reversion | 86.66 | -13.34 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.91 | -14.09 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.42 | -14.58 | 82 | 15.9 | -23.57 | -4.66 | -24.31 | 220 |
| 49 | MFI reversion · 1h | reversion | 85.18 | -14.82 | 207 | 30.4 | -20.90 | -3.21 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.77 | -15.23 | 79 | 17.7 | 1.57 | 0.39 | -21.74 | 216 |
| 51 | Three white soldiers | momentum | 83.08 | -16.92 | 222 | 18.5 | -47.25 | -19.08 | -47.27 | 604 |
| 52 | Z-score reversion · 1h | reversion | 82.76 | -17.24 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.73 | -17.27 | 193 | 21.2 | -12.52 | -1.57 | -27.41 | 392 |
| 54 | Agent (ML meta-label) | meta | 82.18 | -17.82 | 655 | 18.0 | -20.76 | -3.84 | -22.13 | 379 |
| 55 | Heikin-Ashi · 1h | trend | 81.24 | -18.76 | 207 | 22.2 | -31.57 | -5.10 | -42.46 | 678 |
| 56 | EMA 9/21 cross · 1h | trend | 81.15 | -18.85 | 131 | 11.5 | -18.81 | -3.10 | -29.40 | 317 |
| 57 | VWAP momentum · 1h | momentum | 80.28 | -19.72 | 410 | 20.0 | -36.96 | -5.52 | -46.96 | 1253 |
| 58 | Williams %R · 1h | reversion | 80.05 | -19.95 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 59 | RSI(14) reversion · 1h | reversion | 79.98 | -20.02 | 74 | 20.3 | -14.50 | -2.56 | -22.27 | 168 |
| 60 | Bollinger reversion · 1h | reversion | 79.84 | -20.16 | 150 | 32.0 | -30.68 | -6.34 | -33.04 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.00 | -21.00 | 161 | 38.5 | -20.26 | -2.63 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.08 | -23.92 | 205 | 25.4 | -36.30 | -6.52 | -37.22 | 544 |
| 63 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.72 | -17.49 | -77.84 | 1732 |
| 64 | Volume breakout | breakout | 61.88 | -38.12 | 349 | 12.9 | -63.19 | -18.13 | -64.06 | 886 |
| 65 | Squeeze breakout | breakout | 60.56 | -39.44 | 453 | 14.1 | -63.31 | -18.07 | -65.45 | 1218 |
| 66 | Donchian 55/20 | breakout | 59.41 | -40.59 | 462 | 18.0 | -68.57 | -14.35 | -72.80 | 1280 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.51 | -16.46 | -74.60 | 1630 |
| 68 | EMA 20/50 cross | trend | 57.69 | -42.31 | 480 | 18.3 | -75.79 | -14.58 | -80.16 | 1427 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.86 | -15.30 | -73.38 | 1515 |
| 70 | Keltner breakout | breakout | 51.71 | -48.29 | 650 | 15.8 | -82.76 | -26.52 | -83.26 | 1820 |
| 71 | AI bee: Boozy | ai | 51.18 | -48.82 | 343 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -29.99 | -98.66 | 5347 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -30.12 | -93.51 | 2583 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.09 | -19.90 | -87.78 | 1905 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.01 | -23.98 | -90.90 | 2351 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.09 | -25.90 | -91.09 | 2300 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -31.96 | -97.41 | 3519 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -36.73 | -96.70 | 3614 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.41 | -26.53 | -94.76 | 2592 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.88 | -23.24 | -82.72 | 1724 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.35 | -99.38 | 5810 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.29 | -25.69 | -91.77 | 2644 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.02 | -31.16 | -96.02 | 3510 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.20 | -99.74 | 6241 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.39 | -28.58 | -91.51 | 2353 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.54 | -39.00 | -97.54 | 3664 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.41 | -98.47 | 4757 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.69 | -33.30 | -93.70 | 2815 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.01 | -99.53 | 6242 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.77 | -22.18 | -86.81 | 2170 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.13 | -27.08 | -88.17 | 2170 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -32.11 | -95.86 | 3803 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.96 | -32.14 | -89.27 | 2110 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.78 | -33.62 | -95.79 | 4153 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.26 | -99.90 | 8341 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T08:10 | Donchian 55/20 | sell | SOL-USD | 12.02 | 0.20 | exit signal |
| 2026-10-19T08:10 | Donchian 55/20 | sell | BTC-USD | 11.89 | 0.05 | exit signal |
| 2026-10-19T08:05 | Donchian 55/20 | sell | XRP-USD | 14.82 | -0.14 | stop-loss |
| 2026-10-19T08:05 | Donchian 55/20 | sell | ETH-USD | 11.89 | 0.07 | exit signal |
| 2026-10-19T08:00 | OBV trend · 1h | buy | XRP-USD | 6.60 | — | entry signal |
| 2026-10-19T08:00 | OBV trend · 1h | sell | BTC-USD | 4.39 | -0.01 | rebalance down |
| 2026-10-19T08:00 | VWAP momentum · 1h | buy | DOGE-USD | 2.34 | — | entry signal |
| 2026-10-19T08:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 23.11 | — | entry signal |
| 2026-10-19T07:40 | Three white soldiers | sell | SOL-USD | 20.67 | -0.20 | stop-loss |
| 2026-10-19T07:40 | Three white soldiers | sell | DOGE-USD | 20.68 | -0.19 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | XRP-USD | 12.37 | -0.11 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | SOL-USD | 12.37 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | ETH-USD | 12.38 | -0.11 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | DOGE-USD | 12.38 | -0.11 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | BTC-USD | 12.38 | -0.11 | stop-loss |
| 2026-10-19T07:40 | Squeeze breakout | sell | ETH-USD | 15.06 | -0.14 | stop-loss |
| 2026-10-19T07:40 | Squeeze breakout | sell | BTC-USD | 15.10 | -0.10 | stop-loss |
| 2026-10-19T07:40 | Keltner breakout | sell | XRP-USD | 12.93 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Keltner breakout | sell | ETH-USD | 12.93 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Keltner breakout | sell | DOGE-USD | 12.93 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Keltner breakout | sell | BTC-USD | 12.93 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Donchian 55/20 | sell | DOGE-USD | 8.79 | -0.08 | stop-loss |
| 2026-10-19T07:36 | Three white soldiers | buy | SOL-USD | 20.87 | — | entry signal |
| 2026-10-19T07:36 | Three white soldiers | buy | DOGE-USD | 20.87 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | XRP-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | SOL-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | ETH-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | DOGE-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | BTC-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Squeeze breakout | buy | ETH-USD | 15.20 | — | entry signal |
| 2026-10-19T07:36 | Keltner breakout | buy | XRP-USD | 13.05 | — | entry signal |
| 2026-10-19T07:36 | Keltner breakout | buy | ETH-USD | 13.05 | — | entry signal |
| 2026-10-19T07:36 | Keltner breakout | buy | DOGE-USD | 13.05 | — | entry signal |
| 2026-10-19T07:36 | Keltner breakout | buy | BTC-USD | 13.05 | — | entry signal |
| 2026-10-19T07:36 | Donchian 55/20 | buy | DOGE-USD | 8.87 | — | entry signal |
| 2026-10-19T07:36 | Donchian 55/20 | sell | ETH-USD | 3.05 | 0.04 | rebalance down |
| 2026-10-19T07:36 | Donchian 55/20 | sell | BTC-USD | 3.03 | 0.03 | rebalance down |
| 2026-10-19T07:20 | Donchian 55/20 | buy | XRP-USD | 14.96 | — | entry signal |
| 2026-10-19T07:15 | Volume breakout | sell | BTC-USD | 15.54 | -0.10 | exit signal |
| 2026-10-19T07:10 | Squeeze breakout | buy | BTC-USD | 15.20 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 08:25:05.000144+00:00 -> 2026-10-19 08:35:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
