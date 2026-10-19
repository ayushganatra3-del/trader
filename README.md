# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T17:55:05.000148+00:00 · 28628 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.75 (-9.25%)

Closed trades 82, win rate 40.2%, fees £2.80, max drawdown -9.80%.

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

Today: 27726 decisions in 2613 calls, $0.3468 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T17:55 | 2 / 13 / 14 | cash |  |
| Breezy | 2026-10-19T17:55 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-10-19T17:55 | 0 / 25 / 4 | COIN 72% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 105.06 | 5.06 | 0 | — | 5.74 | 2.81 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.95 | -0.05 | 0 | — | 2.37 | 1.00 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.30 | -0.70 | 0 | — | -0.11 | -0.02 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.56 | -1.44 | 3 | 33.3 | 2.59 | 0.65 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.25 | -1.75 | 54 | 31.5 | 3.04 | 1.68 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -3.45 | -1.61 | -6.06 | 278 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.42 | -2.58 | 0 | — | -0.61 | -0.19 | -5.31 | 1 |
| 15 | Donchian 55/20 · 1h | breakout | 97.37 | -2.63 | 36 | 16.7 | -8.82 | -1.42 | -19.34 | 100 |
| 16 | Hold BTC | benchmark | 97.29 | -2.71 | 0 | — | 25.96 | 3.10 | -8.68 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.06 | -2.29 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.60 | -3.40 | 0 | — | -5.71 | -2.25 | -7.04 | 1 |
| 19 | Copy: Insider buying | copy | 96.51 | -3.50 | 23 | 43.5 | -14.92 | -2.70 | -20.62 | 73 |
| 20 | Trend pullback · 1h | trend | 96.48 | -3.52 | 88 | 23.9 | -19.64 | -5.80 | -20.58 | 136 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.23 | -4.77 | 8 | 37.5 | -20.26 | -1.71 | -34.64 | 26 |
| 23 | Gap and go | momentum | 93.64 | -6.36 | 74 | 17.6 | 9.86 | 2.48 | -6.51 | 202 |
| 24 | ADX DI cross · 1h | trend | 93.55 | -6.45 | 87 | 18.4 | -14.02 | -2.52 | -16.51 | 257 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.33 | -0.24 | -9.46 | 92 |
| 26 | Daily: Momentum burst | daily | 93.16 | -6.84 | 6 | 16.7 | -5.74 | -0.72 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.23 | -7.77 | 7 | 0.0 | -2.73 | -0.15 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.91 | -8.09 | 78 | 23.1 | -5.11 | -0.65 | -16.37 | 107 |
| 29 | Parabolic SAR · 1h | trend | 91.89 | -8.11 | 102 | 22.5 | -13.99 | -2.65 | -24.44 | 267 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.93 | -2.46 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 91.09 | -8.90 | 201 | 28.9 | -12.01 | -3.31 | -17.61 | 564 |
| 32 | Bollinger breakout · 1h | breakout | 90.80 | -9.20 | 84 | 28.6 | -8.21 | -1.36 | -16.88 | 257 |
| 33 | Agent | meta | 90.75 | -9.25 | 82 | 40.2 | -7.35 | -2.90 | -17.19 | 246 |
| 34 | EMA 20/50 cross · 1h | trend | 90.41 | -9.59 | 58 | 13.8 | -18.81 | -3.43 | -21.09 | 125 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 90.11 | -9.89 | 0 | — | 4.05 | 0.76 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.70 | -10.30 | 78 | 16.7 | -18.15 | -3.16 | -28.43 | 213 |
| 37 | Connors RSI(2) · 1h | reversion | 89.43 | -10.57 | 149 | 40.9 | -22.99 | -6.83 | -24.51 | 206 |
| 38 | Ichimoku · 1h | trend | 88.70 | -11.30 | 55 | 14.5 | -17.54 | -3.31 | -18.08 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.36 | -11.64 | 152 | 46.1 | -17.31 | -2.99 | -22.24 | 362 |
| 40 | Agent (aggressive) | meta | 87.92 | -12.08 | 41 | 34.1 | -3.40 | -0.82 | -13.96 | 114 |
| 41 | Keltner breakout · 1h | breakout | 87.73 | -12.27 | 56 | 23.2 | -12.91 | -1.87 | -28.09 | 201 |
| 42 | Triple EMA stack · 1h | trend | 87.66 | -12.34 | 85 | 15.3 | -21.11 | -2.83 | -32.93 | 230 |
| 43 | Supertrend · 1h | trend | 87.34 | -12.66 | 86 | 12.8 | -23.93 | -4.99 | -27.50 | 218 |
| 44 | Opening range 15m | breakout | 86.58 | -13.42 | 250 | 24.8 | -17.01 | -4.41 | -21.40 | 702 |
| 45 | MACD cross · 1h | trend | 86.10 | -13.90 | 189 | 20.6 | -26.13 | -4.88 | -32.54 | 469 |
| 46 | OBV trend · 1h | momentum | 85.65 | -14.35 | 176 | 17.6 | -23.32 | -3.20 | -35.39 | 319 |
| 47 | Z-score reversion · 1h | reversion | 85.42 | -14.58 | 91 | 30.8 | -13.68 | -2.22 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.69 | -15.31 | 209 | 31.1 | -17.61 | -2.75 | -21.34 | 137 |
| 49 | MACD zero-line · 1h | trend | 84.24 | -15.76 | 87 | 14.9 | -24.96 | -4.99 | -25.24 | 219 |
| 50 | Agent (ML meta-label) | meta | 83.91 | -16.09 | 670 | 18.8 | -9.53 | -1.71 | -16.15 | 379 |
| 51 | Donchian 20/10 · 1h | breakout | 83.73 | -16.27 | 81 | 17.3 | -0.41 | 0.17 | -25.26 | 214 |
| 52 | Bollinger reversion · 1h | reversion | 82.70 | -17.30 | 157 | 34.4 | -27.93 | -5.36 | -33.52 | 349 |
| 53 | Three white soldiers | momentum | 82.64 | -17.36 | 230 | 19.1 | -47.22 | -18.83 | -47.41 | 602 |
| 54 | Max aggression: 1-day momentum | meta | 82.48 | -17.52 | 15 | 33.3 | -15.96 | -0.60 | -37.31 | 42 |
| 55 | Williams %R · 1h | reversion | 82.13 | -17.87 | 182 | 42.9 | -33.60 | -5.35 | -36.50 | 534 |
| 56 | ROC + volume · 1h | momentum | 81.47 | -18.53 | 197 | 20.8 | -16.84 | -2.12 | -33.72 | 389 |
| 57 | CCI reversion · 1h | reversion | 80.77 | -19.23 | 163 | 39.3 | -20.12 | -2.56 | -27.44 | 438 |
| 58 | EMA 9/21 cross · 1h | trend | 80.41 | -19.59 | 133 | 11.3 | -28.99 | -6.00 | -29.26 | 312 |
| 59 | RSI(14) reversion · 1h | reversion | 80.31 | -19.69 | 75 | 21.3 | -14.37 | -2.58 | -22.27 | 173 |
| 60 | Heikin-Ashi · 1h | trend | 79.00 | -21.00 | 221 | 21.7 | -36.57 | -6.08 | -44.68 | 681 |
| 61 | VWAP momentum · 1h | momentum | 78.14 | -21.86 | 431 | 20.9 | -37.26 | -5.18 | -48.05 | 1246 |
| 62 | Candlestick reversal · 1h | reversion | 77.22 | -22.78 | 212 | 27.4 | -35.68 | -6.52 | -37.50 | 535 |
| 63 | ROC + volume | momentum | 62.54 | -37.46 | 589 | 22.6 | -75.55 | -17.37 | -78.03 | 1734 |
| 64 | Volume breakout | breakout | 61.60 | -38.40 | 358 | 13.1 | -62.53 | -17.62 | -64.19 | 877 |
| 65 | Squeeze breakout | breakout | 60.80 | -39.20 | 457 | 14.4 | -63.13 | -18.94 | -65.58 | 1201 |
| 66 | Donchian 55/20 | breakout | 59.33 | -40.67 | 472 | 18.2 | -67.97 | -13.74 | -72.80 | 1266 |
| 67 | RSI(14) reversion | reversion | 58.02 | -41.98 | 702 | 25.1 | -74.57 | -16.50 | -74.66 | 1616 |
| 68 | EMA 20/50 cross | trend | 57.11 | -42.89 | 493 | 18.9 | -75.34 | -13.85 | -80.26 | 1418 |
| 69 | VWAP reversion | reversion | 53.85 | -46.15 | 740 | 25.1 | -72.32 | -14.96 | -72.96 | 1511 |
| 70 | Keltner breakout | breakout | 51.60 | -48.40 | 666 | 16.4 | -82.52 | -26.23 | -83.37 | 1814 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.68 | -98.65 | 5302 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.10 | -28.20 | -93.67 | 2568 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.24 | -19.90 | -88.01 | 1893 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.77 | -22.70 | -90.99 | 2341 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.92 | -25.51 | -90.99 | 2266 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.40 | -31.99 | -97.50 | 3477 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.53 | -34.33 | -96.71 | 3576 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -27.11 | -94.49 | 2535 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.01 | -24.69 | -82.93 | 1694 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.13 | -99.37 | 5739 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.98 | -24.91 | -91.86 | 2611 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.13 | -31.57 | -96.13 | 3487 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.29 | -99.74 | 6166 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.64 | -29.46 | -91.68 | 2331 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -36.79 | -97.57 | 3625 |
| 86 | AI bee: Boozy | ai | 50.09 | -49.91 | 346 | 5.8 | — | — | — | — |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.35 | -98.46 | 4699 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.57 | -32.00 | -93.85 | 2789 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.06 | -99.53 | 6165 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.85 | -22.38 | -86.88 | 2131 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.98 | -26.85 | -87.99 | 2138 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.61 | -95.89 | 3745 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.91 | -32.30 | -88.97 | 2095 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -33.38 | -95.75 | 4111 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.79 | -99.90 | 8255 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T17:50 | Keltner breakout | sell | LABU | 12.92 | 0.14 | stop-loss |
| 2026-10-19T17:50 | Opening range 30m | buy | TSLA | 4.96 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 30m | buy | PLTR | 4.90 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 30m | buy | NVDA | 6.08 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 30m | buy | MSFT | 5.08 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 30m | buy | GOOGL | 6.11 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 30m | buy | AMZN | 4.93 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 30m | sell | UPRO | 10.10 | -0.03 | exit signal |
| 2026-10-19T17:50 | Opening range 30m | sell | TQQQ | 10.05 | -0.06 | exit signal |
| 2026-10-19T17:50 | Opening range 30m | sell | QQQ | 10.09 | -0.02 | exit signal |
| 2026-10-19T17:50 | Opening range 15m | buy | TSLA | 4.72 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 15m | buy | PLTR | 4.66 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 15m | buy | NVDA | 4.92 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 15m | buy | MSFT | 4.83 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 15m | buy | GOOGL | 4.84 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 15m | buy | AMZN | 4.69 | — | rebalance up |
| 2026-10-19T17:50 | Opening range 15m | sell | TQQQ | 9.54 | -0.06 | exit signal |
| 2026-10-19T17:50 | Opening range 15m | sell | QQQ | 9.58 | -0.02 | exit signal |
| 2026-10-19T17:45 | VWAP reversion | sell | COIN | 13.31 | -0.12 | stop-loss |
| 2026-10-19T17:45 | ROC + volume | buy | SQQQ | 15.63 | — | entry signal |
| 2026-10-19T17:41 | VWAP reversion | buy | AMD | 13.50 | — | entry signal |
| 2026-10-19T17:41 | RSI(14) reversion | buy | AMD | 14.53 | — | entry signal |
| 2026-10-19T17:41 | RSI(14) reversion | sell | AAPL | 14.53 | 0.04 | exit signal |
| 2026-10-19T17:41 | ROC + volume | sell | LABU | 12.70 | 0.20 | exit signal |
| 2026-10-19T17:41 | EMA 20/50 cross | buy | SPY | 4.77 | — | entry |
| 2026-10-19T17:41 | EMA 20/50 cross | sell | SOXL | 5.60 | -0.11 | exit signal |
| 2026-10-19T17:36 | Squeeze breakout | buy | AAPL | 15.20 | — | entry signal |
| 2026-10-19T17:36 | Donchian 55/20 | sell | NVDA | 14.83 | -0.04 | exit signal |
| 2026-10-19T17:36 | EMA 20/50 cross | buy | NVDA | 3.35 | — | entry |
| 2026-10-19T17:36 | EMA 20/50 cross | sell | IWM | 3.35 | -0.01 | exit signal |
| 2026-10-19T17:30 | Agent (ML meta-label) | buy | GOOGL | 4.95 | — | entry |
| 2026-10-19T17:30 | Agent (ML meta-label) | buy | AMZN | 4.95 | — | entry |
| 2026-10-19T17:30 | Agent (ML meta-label) | sell | TECL | 4.66 | -0.03 | selected signal exited |
| 2026-10-19T17:30 | Agent (ML meta-label) | sell | MSTR | 5.21 | -0.10 | selected signal exited |
| 2026-10-19T17:30 | Agent | sell | BITX | 18.17 | 0.04 | selected signal exited |
| 2026-10-19T17:30 | Candlestick reversal · 1h | buy | MSTR | 6.67 | — | entry |
| 2026-10-19T17:30 | OBV trend · 1h | buy | AMZN | 14.23 | — | entry signal |
| 2026-10-19T17:30 | OBV trend · 1h | buy | AAPL | 14.28 | — | entry |
| 2026-10-19T17:30 | OBV trend · 1h | sell | XRP-USD | 7.04 | -0.03 | rebalance down |
| 2026-10-19T17:30 | OBV trend · 1h | sell | SQQQ | 7.42 | 0.39 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 17:55:05.000148+00:00 -> 2026-10-19 18:05:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
