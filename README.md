# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T19:25:05.000152+00:00 · 28689 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.51 (-9.49%)

Closed trades 84, win rate 39.3%, fees £2.83, max drawdown -9.90%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, APLD 12%, FLSC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 33141 decisions in 2796 calls, $0.4101 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T19:25 | 9 / 15 / 6 | AMD 17% |  |
| Breezy | 2026-10-19T19:25 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-19T19:25 | 9 / 20 / 1 | COIN 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |
| VWAP reversion | BITX | 1.52 | +2.60% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 105.14 | 5.14 | 0 | — | 5.46 | 2.62 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.93 | -0.07 | 0 | — | 2.47 | 1.04 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.43 | -0.57 | 0 | — | -0.24 | -0.09 | -3.13 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.22 | -0.78 | 3 | 33.3 | 3.31 | 0.78 | -7.93 | 9 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.33 | -1.67 | 54 | 31.5 | 3.14 | 1.74 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -2.42 | -1.01 | -5.70 | 280 |
| 14 | Hold BTC | benchmark | 97.41 | -2.59 | 0 | — | 26.48 | 3.15 | -8.68 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.30 | -2.70 | 0 | — | -1.00 | -0.36 | -5.31 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 97.16 | -2.84 | 36 | 16.7 | -11.58 | -2.14 | -18.86 | 100 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.06 | -2.30 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.56 | -3.44 | 0 | — | -5.71 | -2.25 | -7.04 | 1 |
| 19 | Copy: Insider buying | copy | 96.42 | -3.58 | 23 | 43.5 | -14.96 | -2.71 | -20.62 | 73 |
| 20 | Trend pullback · 1h | trend | 96.24 | -3.76 | 88 | 23.9 | -19.87 | -5.85 | -20.57 | 137 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 94.26 | -5.74 | 8 | 37.5 | -21.04 | -1.78 | -34.64 | 26 |
| 23 | ADX DI cross · 1h | trend | 93.58 | -6.42 | 88 | 18.2 | -14.52 | -2.57 | -16.96 | 258 |
| 24 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 9.10 | 2.39 | -6.51 | 201 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 93.11 | -6.89 | 6 | 16.7 | -5.79 | -0.73 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.13 | -7.87 | 7 | 0.0 | -2.93 | -0.18 | -13.10 | 12 |
| 28 | Parabolic SAR · 1h | trend | 92.02 | -7.98 | 102 | 22.5 | -14.00 | -2.63 | -24.57 | 266 |
| 29 | Volume breakout · 1h | breakout | 91.98 | -8.02 | 78 | 23.1 | -7.51 | -1.17 | -16.37 | 107 |
| 30 | Opening range 30m | breakout | 91.26 | -8.74 | 201 | 28.9 | -11.88 | -3.29 | -17.58 | 564 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.94 | -2.47 | -16.91 | 1 |
| 32 | Bollinger breakout · 1h | breakout | 90.87 | -9.13 | 84 | 28.6 | -8.57 | -1.44 | -16.89 | 256 |
| 33 | Agent | meta | 90.51 | -9.49 | 84 | 39.3 | -4.54 | -1.19 | -17.19 | 254 |
| 34 | EMA 20/50 cross · 1h | trend | 90.31 | -9.69 | 58 | 13.8 | -19.12 | -3.41 | -21.31 | 126 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 90.17 | -9.83 | 0 | — | 1.74 | 0.43 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.74 | -10.26 | 78 | 16.7 | -16.71 | -2.76 | -28.00 | 213 |
| 37 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.38 | -6.61 | -23.94 | 206 |
| 38 | Stochastic reversion · 1h | reversion | 88.91 | -11.09 | 152 | 46.1 | -16.57 | -2.82 | -22.24 | 363 |
| 39 | Ichimoku · 1h | trend | 88.78 | -11.22 | 55 | 14.5 | -17.46 | -3.29 | -18.08 | 113 |
| 40 | Keltner breakout · 1h | breakout | 87.81 | -12.20 | 56 | 23.2 | -11.68 | -1.63 | -26.79 | 201 |
| 41 | Agent (aggressive) | meta | 87.54 | -12.46 | 42 | 33.3 | 6.43 | 1.17 | -19.37 | 121 |
| 42 | Supertrend · 1h | trend | 87.51 | -12.49 | 86 | 12.8 | -22.72 | -4.65 | -26.48 | 214 |
| 43 | Triple EMA stack · 1h | trend | 87.51 | -12.49 | 85 | 15.3 | -22.94 | -3.43 | -33.00 | 230 |
| 44 | Opening range 15m | breakout | 86.74 | -13.27 | 250 | 24.8 | -15.71 | -3.80 | -21.16 | 698 |
| 45 | MACD cross · 1h | trend | 86.45 | -13.55 | 189 | 20.6 | -25.87 | -4.83 | -32.65 | 469 |
| 46 | Z-score reversion · 1h | reversion | 85.94 | -14.06 | 91 | 30.8 | -13.50 | -2.16 | -21.32 | 197 |
| 47 | OBV trend · 1h | momentum | 85.39 | -14.61 | 179 | 17.9 | -23.14 | -3.17 | -34.82 | 320 |
| 48 | Max aggression: 1-day momentum | meta | 84.84 | -15.16 | 15 | 33.3 | -13.53 | -0.44 | -37.31 | 42 |
| 49 | MFI reversion · 1h | reversion | 84.78 | -15.22 | 209 | 31.1 | -17.67 | -2.76 | -21.34 | 139 |
| 50 | MACD zero-line · 1h | trend | 84.31 | -15.69 | 87 | 14.9 | -24.83 | -4.96 | -25.19 | 219 |
| 51 | Agent (ML meta-label) | meta | 84.28 | -15.72 | 675 | 18.7 | -9.00 | -1.58 | -15.53 | 391 |
| 52 | Donchian 20/10 · 1h | breakout | 83.73 | -16.27 | 81 | 17.3 | -4.19 | -0.33 | -25.26 | 214 |
| 53 | Bollinger reversion · 1h | reversion | 82.90 | -17.10 | 157 | 34.4 | -27.75 | -5.29 | -33.53 | 349 |
| 54 | Three white soldiers | momentum | 82.63 | -17.38 | 230 | 19.1 | -47.30 | -18.83 | -47.44 | 603 |
| 55 | Williams %R · 1h | reversion | 82.60 | -17.40 | 182 | 42.9 | -33.21 | -5.23 | -36.50 | 533 |
| 56 | ROC + volume · 1h | momentum | 81.59 | -18.41 | 197 | 20.8 | -20.32 | -2.96 | -33.75 | 386 |
| 57 | CCI reversion · 1h | reversion | 81.16 | -18.84 | 163 | 39.3 | -19.49 | -2.45 | -27.44 | 440 |
| 58 | RSI(14) reversion · 1h | reversion | 80.87 | -19.13 | 75 | 21.3 | -13.81 | -2.43 | -22.27 | 180 |
| 59 | EMA 9/21 cross · 1h | trend | 80.31 | -19.69 | 135 | 11.1 | -29.17 | -6.04 | -29.55 | 314 |
| 60 | Heikin-Ashi · 1h | trend | 79.16 | -20.84 | 223 | 21.5 | -36.41 | -6.05 | -44.79 | 681 |
| 61 | VWAP momentum · 1h | momentum | 77.98 | -22.02 | 433 | 20.8 | -39.60 | -6.21 | -48.22 | 1246 |
| 62 | Candlestick reversal · 1h | reversion | 77.97 | -22.03 | 213 | 27.2 | -35.60 | -6.35 | -37.48 | 535 |
| 63 | ROC + volume | momentum | 62.47 | -37.53 | 590 | 22.5 | -75.90 | -18.24 | -78.03 | 1733 |
| 64 | Volume breakout | breakout | 61.60 | -38.40 | 358 | 13.1 | -62.48 | -17.54 | -64.19 | 876 |
| 65 | Squeeze breakout | breakout | 60.74 | -39.26 | 458 | 14.4 | -63.84 | -20.50 | -65.58 | 1204 |
| 66 | Donchian 55/20 | breakout | 59.19 | -40.81 | 474 | 18.6 | -67.91 | -13.55 | -72.80 | 1262 |
| 67 | RSI(14) reversion | reversion | 58.44 | -41.56 | 705 | 25.2 | -74.10 | -16.16 | -74.50 | 1595 |
| 68 | EMA 20/50 cross | trend | 57.10 | -42.90 | 499 | 19.2 | -75.12 | -13.54 | -80.26 | 1420 |
| 69 | VWAP reversion | reversion | 53.98 | -46.02 | 743 | 25.0 | -72.11 | -14.82 | -72.83 | 1510 |
| 70 | Keltner breakout | breakout | 51.53 | -48.47 | 667 | 16.3 | -82.61 | -26.48 | -83.37 | 1815 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -29.50 | -98.65 | 5280 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.04 | -27.75 | -93.67 | 2563 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.10 | -19.40 | -88.06 | 1897 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.74 | -22.46 | -91.02 | 2345 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.92 | -25.46 | -91.05 | 2265 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -31.72 | -97.52 | 3497 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.51 | -34.06 | -96.70 | 3572 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -27.83 | -94.46 | 2524 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.97 | -24.57 | -82.93 | 1698 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.84 | -99.37 | 5747 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.06 | -24.98 | -91.92 | 2625 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.12 | -31.54 | -96.12 | 3477 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.96 | -99.74 | 6193 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.69 | -29.47 | -91.72 | 2332 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -36.17 | -97.59 | 3624 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.39 | -98.47 | 4697 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.67 | -32.64 | -93.88 | 2802 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.80 | -99.52 | 6165 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.80 | -22.32 | -86.94 | 2134 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.92 | -26.71 | -87.98 | 2137 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -32.18 | -95.85 | 3737 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.89 | -32.23 | -88.97 | 2098 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.64 | -32.75 | -95.65 | 4108 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.76 | -99.90 | 8280 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T19:25 | Agent (aggressive) | sell | SQQQ | 43.58 | -0.38 | selected signal exited |
| 2026-10-19T19:25 | Agent | sell | SQQQ | 17.98 | -0.16 | selected signal exited |
| 2026-10-19T19:25 | RSI(14) reversion | sell | SOXL | 14.79 | 0.26 | exit signal |
| 2026-10-19T19:25 | RSI(14) reversion | sell | AMD | 14.57 | 0.13 | take-profit |
| 2026-10-19T19:25 | Three white soldiers | buy | NVDA | 20.66 | — | entry signal |
| 2026-10-19T19:25 | Squeeze breakout | buy | TQQQ | 6.74 | — | entry signal |
| 2026-10-19T19:25 | Squeeze breakout | buy | TNA | 6.75 | — | entry signal |
| 2026-10-19T19:25 | Squeeze breakout | buy | SPY | 6.75 | — | entry signal |
| 2026-10-19T19:25 | Squeeze breakout | buy | QQQ | 6.75 | — | entry signal |
| 2026-10-19T19:25 | Squeeze breakout | buy | NVDA | 6.75 | — | entry signal |
| 2026-10-19T19:25 | Squeeze breakout | sell | UPRO | 8.44 | -0.00 | rebalance down |
| 2026-10-19T19:25 | Squeeze breakout | sell | TSLA | 8.41 | -0.02 | rebalance down |
| 2026-10-19T19:25 | Squeeze breakout | sell | GOOGL | 8.45 | 0.01 | rebalance down |
| 2026-10-19T19:25 | Squeeze breakout | sell | AMZN | 8.43 | -0.01 | rebalance down |
| 2026-10-19T19:25 | Keltner breakout | buy | TECL | 5.16 | — | entry signal |
| 2026-10-19T19:25 | Keltner breakout | buy | SOXL | 10.31 | — | entry signal |
| 2026-10-19T19:25 | Keltner breakout | buy | GOOGL | 10.31 | — | entry signal |
| 2026-10-19T19:25 | ROC + volume | buy | TQQQ | 15.63 | — | entry signal |
| 2026-10-19T19:25 | ROC + volume | buy | TECL | 15.63 | — | entry signal |
| 2026-10-19T19:25 | ROC + volume | buy | MSTR | 15.63 | — | entry signal |
| 2026-10-19T19:25 | ROC + volume | buy | AMD | 15.63 | — | entry signal |
| 2026-10-19T19:25 | EMA 20/50 cross | buy | QQQ | 1.23 | — | entry signal |
| 2026-10-19T19:25 | EMA 20/50 cross | buy | NVDA | 4.39 | — | entry signal |
| 2026-10-19T19:20 | Squeeze breakout | buy | UPRO | 15.19 | — | entry signal |
| 2026-10-19T19:20 | Squeeze breakout | buy | AMZN | 15.19 | — | entry signal |
| 2026-10-19T19:20 | Keltner breakout | buy | AMZN | 12.89 | — | entry signal |
| 2026-10-19T19:10 | Agent (aggressive) | buy | SQQQ | 43.96 | — | following Williams %R, Bollinger reversion, Heikin-Ashi · 1h |
| 2026-10-19T19:10 | Agent | buy | SQQQ | 18.13 | — | following Williams %R, Bollinger reversion, Heikin-Ashi · 1h |
| 2026-10-19T19:10 | VWAP reversion | buy | AMD | 2.68 | — | rebalance up |
| 2026-10-19T19:10 | VWAP reversion | sell | DOGE-USD | 2.68 | -0.00 | rebalance down |
| 2026-10-19T19:10 | Squeeze breakout | buy | GOOGL | 15.19 | — | entry signal |
| 2026-10-19T19:10 | EMA 20/50 cross | sell | BITX | 5.17 | -0.02 | exit signal |
| 2026-10-19T19:05 | Squeeze breakout | buy | TSLA | 15.20 | — | entry signal |
| 2026-10-19T19:05 | Keltner breakout | buy | META | 12.89 | — | entry signal |
| 2026-10-19T19:05 | Donchian 55/20 | buy | META | 14.80 | — | entry signal |
| 2026-10-19T19:05 | EMA 20/50 cross | buy | BITX | 5.19 | — | entry signal |
| 2026-10-19T19:05 | EMA 20/50 cross | sell | SQQQ | 5.65 | -0.05 | stop-loss |
| 2026-10-19T19:03 | OBV trend · 1h | buy | XRP-USD | 4.28 | — | rebalance up |
| 2026-10-19T19:03 | OBV trend · 1h | sell | AMZN | 4.28 | -0.01 | rebalance down |
| 2026-10-19T19:01 | OBV trend · 1h | buy | XRP-USD | 8.63 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 19:25:05.000152+00:00 -> 2026-10-19 19:35:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
