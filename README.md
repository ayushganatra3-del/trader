# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T16:55:05.000169+00:00 · 28589 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.73 (-9.27%)

Closed trades 81, win rate 39.5%, fees £2.79, max drawdown -9.80%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.14 | +0.02 |

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

Today: 24243 decisions in 2496 calls, $0.3059 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T16:55 | 3 / 11 / 16 | cash |  |
| Breezy | 2026-10-19T16:55 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-10-19T16:55 | 1 / 26 / 3 | COIN 73% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.83 | 4.83 | 0 | — | 5.61 | 2.74 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.61 | -0.39 | 0 | — | 1.95 | 0.84 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.33 | -0.67 | 0 | — | -0.06 | 0.01 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.87 | -1.13 | 3 | 33.3 | 2.92 | 0.71 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.27 | -1.73 | 54 | 31.5 | 3.15 | 1.75 | -2.17 | 63 |
| 13 | Copy: Congress Democrats (NANC) | copy | 97.64 | -2.36 | 0 | — | -0.30 | -0.06 | -5.31 | 1 |
| 14 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -5.82 | -3.04 | -6.56 | 260 |
| 15 | Hold BTC | benchmark | 97.39 | -2.61 | 0 | — | 26.31 | 3.13 | -8.68 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 97.35 | -2.65 | 36 | 16.7 | -8.65 | -1.37 | -19.37 | 100 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.30 | -2.43 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.61 | -3.39 | 0 | — | -5.68 | -2.23 | -7.04 | 1 |
| 19 | Copy: Insider buying | copy | 96.30 | -3.70 | 23 | 43.5 | -15.10 | -2.73 | -20.62 | 73 |
| 20 | Trend pullback · 1h | trend | 96.26 | -3.74 | 88 | 23.9 | -19.81 | -5.86 | -20.58 | 136 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 94.72 | -5.28 | 8 | 37.5 | -20.68 | -1.75 | -34.64 | 26 |
| 23 | Gap and go | momentum | 93.66 | -6.34 | 74 | 17.6 | 9.84 | 2.47 | -6.54 | 203 |
| 24 | ADX DI cross · 1h | trend | 93.57 | -6.43 | 87 | 18.4 | -12.88 | -2.44 | -15.20 | 256 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.33 | -0.24 | -9.46 | 92 |
| 26 | Daily: Momentum burst | daily | 93.34 | -6.66 | 6 | 16.7 | -5.72 | -0.71 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.09 | -7.91 | 7 | 0.0 | -3.21 | -0.21 | -13.10 | 12 |
| 28 | Parabolic SAR · 1h | trend | 91.97 | -8.03 | 102 | 22.5 | -12.73 | -2.33 | -23.89 | 269 |
| 29 | Volume breakout · 1h | breakout | 91.93 | -8.07 | 78 | 23.1 | -3.85 | -0.41 | -16.37 | 107 |
| 30 | Opening range 30m | breakout | 91.30 | -8.70 | 197 | 29.4 | -11.79 | -3.25 | -17.60 | 564 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -13.60 | -2.60 | -16.91 | 1 |
| 32 | Bollinger breakout · 1h | breakout | 90.82 | -9.18 | 84 | 28.6 | -3.79 | -0.46 | -16.89 | 259 |
| 33 | Agent | meta | 90.73 | -9.27 | 81 | 39.5 | -6.93 | -2.79 | -14.78 | 238 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 90.60 | -9.40 | 0 | — | 4.36 | 0.80 | -14.37 | 1 |
| 35 | EMA 20/50 cross · 1h | trend | 90.36 | -9.64 | 58 | 13.8 | -19.59 | -3.57 | -21.79 | 125 |
| 36 | RSI momentum · 1h | momentum | 89.75 | -10.25 | 78 | 16.7 | -15.80 | -2.63 | -27.20 | 215 |
| 37 | Connors RSI(2) · 1h | reversion | 89.31 | -10.69 | 149 | 40.9 | -23.09 | -6.89 | -24.51 | 206 |
| 38 | Ichimoku · 1h | trend | 88.74 | -11.26 | 55 | 14.5 | -17.50 | -3.30 | -18.08 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.73 | -11.27 | 152 | 46.1 | -18.05 | -3.08 | -22.24 | 366 |
| 40 | Agent (aggressive) | meta | 87.92 | -12.08 | 41 | 34.1 | -5.06 | -1.43 | -14.01 | 113 |
| 41 | Keltner breakout · 1h | breakout | 87.75 | -12.24 | 56 | 23.2 | -7.85 | -0.91 | -27.04 | 208 |
| 42 | Triple EMA stack · 1h | trend | 87.58 | -12.42 | 85 | 15.3 | -23.39 | -3.09 | -35.30 | 232 |
| 43 | Supertrend · 1h | trend | 87.50 | -12.50 | 86 | 12.8 | -23.66 | -4.92 | -27.21 | 218 |
| 44 | Opening range 15m | breakout | 86.75 | -13.25 | 247 | 25.1 | -16.83 | -4.36 | -21.40 | 702 |
| 45 | MACD cross · 1h | trend | 86.33 | -13.67 | 189 | 20.6 | -25.94 | -4.84 | -32.36 | 468 |
| 46 | Z-score reversion · 1h | reversion | 85.81 | -14.19 | 91 | 30.8 | -13.32 | -2.13 | -21.32 | 198 |
| 47 | OBV trend · 1h | momentum | 85.70 | -14.30 | 176 | 17.6 | -27.61 | -4.47 | -34.72 | 321 |
| 48 | MFI reversion · 1h | reversion | 84.81 | -15.19 | 209 | 31.1 | -17.22 | -2.67 | -21.34 | 139 |
| 49 | Max aggression: 1-day momentum | meta | 84.45 | -15.55 | 15 | 33.3 | -13.95 | -0.47 | -37.31 | 42 |
| 50 | MACD zero-line · 1h | trend | 84.27 | -15.73 | 87 | 14.9 | -24.88 | -4.97 | -25.12 | 219 |
| 51 | Agent (ML meta-label) | meta | 84.24 | -15.76 | 668 | 18.9 | -12.59 | -2.28 | -17.64 | 399 |
| 52 | Donchian 20/10 · 1h | breakout | 83.75 | -16.25 | 81 | 17.3 | -0.27 | 0.19 | -25.09 | 215 |
| 53 | Bollinger reversion · 1h | reversion | 82.74 | -17.26 | 157 | 34.4 | -27.89 | -5.35 | -33.52 | 349 |
| 54 | Three white soldiers | momentum | 82.64 | -17.36 | 230 | 19.1 | -47.36 | -18.96 | -47.41 | 606 |
| 55 | Williams %R · 1h | reversion | 82.47 | -17.53 | 182 | 42.9 | -33.38 | -5.28 | -36.50 | 536 |
| 56 | ROC + volume · 1h | momentum | 81.55 | -18.45 | 197 | 20.8 | -18.00 | -2.31 | -33.65 | 391 |
| 57 | CCI reversion · 1h | reversion | 81.06 | -18.93 | 163 | 39.3 | -19.62 | -2.50 | -27.44 | 440 |
| 58 | RSI(14) reversion · 1h | reversion | 80.77 | -19.23 | 75 | 21.3 | -15.47 | -2.71 | -22.27 | 181 |
| 59 | EMA 9/21 cross · 1h | trend | 80.61 | -19.39 | 131 | 11.5 | -25.98 | -5.07 | -29.74 | 313 |
| 60 | Heikin-Ashi · 1h | trend | 79.28 | -20.72 | 212 | 22.6 | -36.31 | -6.04 | -44.45 | 681 |
| 61 | VWAP momentum · 1h | momentum | 78.43 | -21.57 | 427 | 21.1 | -37.11 | -5.16 | -47.94 | 1246 |
| 62 | Candlestick reversal · 1h | reversion | 77.81 | -22.19 | 212 | 27.4 | -35.44 | -6.25 | -37.13 | 536 |
| 63 | ROC + volume | momentum | 62.43 | -37.57 | 588 | 22.4 | -75.63 | -17.40 | -78.19 | 1733 |
| 64 | Volume breakout | breakout | 61.60 | -38.40 | 358 | 13.1 | -62.51 | -17.62 | -64.19 | 877 |
| 65 | Squeeze breakout | breakout | 60.79 | -39.21 | 457 | 14.4 | -63.99 | -20.71 | -65.58 | 1201 |
| 66 | Donchian 55/20 | breakout | 59.43 | -40.57 | 470 | 18.1 | -68.06 | -13.98 | -72.80 | 1272 |
| 67 | RSI(14) reversion | reversion | 58.10 | -41.90 | 701 | 25.0 | -74.24 | -16.25 | -74.41 | 1615 |
| 68 | EMA 20/50 cross | trend | 57.29 | -42.71 | 491 | 18.9 | -75.63 | -14.43 | -80.26 | 1424 |
| 69 | VWAP reversion | reversion | 54.09 | -45.91 | 738 | 25.1 | -72.29 | -14.89 | -73.08 | 1527 |
| 70 | Keltner breakout | breakout | 51.61 | -48.39 | 664 | 16.3 | -82.52 | -26.19 | -83.37 | 1816 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -29.77 | -98.66 | 5320 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.18 | -29.19 | -93.67 | 2566 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.22 | -19.90 | -88.01 | 1898 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.00 | -23.94 | -90.97 | 2340 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.96 | -25.58 | -91.04 | 2266 |
| 76 | AI bee: Boozy | ai | 50.39 | -49.61 | 346 | 5.8 | — | — | — | — |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -32.16 | -97.49 | 3485 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.56 | -35.30 | -96.71 | 3576 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.31 | -26.59 | -94.61 | 2559 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.01 | -24.71 | -82.93 | 1697 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.15 | -99.37 | 5740 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.04 | -25.09 | -91.86 | 2618 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.14 | -31.63 | -96.14 | 3489 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.39 | -99.74 | 6168 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.44 | -28.90 | -91.48 | 2337 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.53 | -38.09 | -97.56 | 3628 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -36.32 | -98.46 | 4692 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.60 | -32.14 | -93.85 | 2793 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.15 | -99.53 | 6173 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.89 | -22.46 | -86.92 | 2133 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.88 | -26.72 | -87.90 | 2143 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.54 | -95.87 | 3741 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.02 | -32.72 | -89.08 | 2102 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.43 | -95.73 | 4100 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.08 | -99.90 | 8274 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T16:55 | VWAP reversion | sell | SQQQ | 13.70 | 0.24 | exit signal |
| 2026-10-19T16:55 | RSI(14) reversion | sell | SQQQ | 14.61 | 0.12 | exit signal |
| 2026-10-19T16:55 | Donchian 55/20 | buy | TSLA | 4.94 | — | rebalance up |
| 2026-10-19T16:55 | Donchian 55/20 | buy | PLTR | 4.96 | — | rebalance up |
| 2026-10-19T16:55 | Donchian 55/20 | buy | NVDA | 4.95 | — | rebalance up |
| 2026-10-19T16:55 | Donchian 55/20 | buy | AMZN | 4.95 | — | rebalance up |
| 2026-10-19T16:55 | Donchian 55/20 | sell | UPRO | 9.89 | -0.05 | exit signal |
| 2026-10-19T16:55 | Donchian 55/20 | sell | SPY | 9.91 | -0.01 | exit signal |
| 2026-10-19T16:50 | Donchian 55/20 | buy | UPRO | 4.52 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | TSLA | 4.46 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | SPY | 4.49 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | PLTR | 4.48 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | NVDA | 4.49 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | AMZN | 4.46 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | sell | TQQQ | 5.38 | 0.01 | exit signal |
| 2026-10-19T16:50 | Donchian 55/20 | sell | TECL | 5.36 | -0.07 | exit signal |
| 2026-10-19T16:50 | Donchian 55/20 | sell | QQQ | 5.42 | 0.01 | exit signal |
| 2026-10-19T16:45 | VWAP reversion | buy | COIN | 13.44 | — | entry signal |
| 2026-10-19T16:41 | Donchian 55/20 | sell | SOXL | 5.30 | -0.14 | stop-loss |
| 2026-10-19T16:35 | Agent (ML meta-label) | buy | TQQQ | 4.70 | — | entry |
| 2026-10-19T16:35 | Agent (ML meta-label) | buy | TECL | 4.70 | — | entry |
| 2026-10-19T16:35 | Agent (ML meta-label) | sell | GOOGL | 4.23 | 0.00 | selected signal exited |
| 2026-10-19T16:35 | Agent (ML meta-label) | sell | BITX | 5.27 | -0.05 | selected signal exited |
| 2026-10-19T16:31 | Agent (rotation) | sell | TQQQ | 32.32 | -0.29 | selected signal exited |
| 2026-10-19T16:31 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 106.82 | -0.97 | target is flat |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | TQQQ | 4.51 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | SOXL | 4.41 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | MSFT | 4.71 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | ETHU | 4.87 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | AMD | 4.65 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | sell | MSTR | 6.48 | 0.11 | exit signal |
| 2026-10-19T16:31 | Candlestick reversal · 1h | sell | BITX | 6.44 | 0.07 | exit signal |
| 2026-10-19T16:31 | VWAP momentum · 1h | buy | TSLA | 4.87 | — | rebalance up |
| 2026-10-19T16:31 | VWAP momentum · 1h | buy | TNA | 9.84 | — | entry |
| 2026-10-19T16:31 | VWAP momentum · 1h | buy | SOXL | 4.90 | — | rebalance up |
| 2026-10-19T16:31 | VWAP momentum · 1h | buy | PLTR | 4.89 | — | rebalance up |
| 2026-10-19T16:31 | VWAP momentum · 1h | buy | NVDA | 4.91 | — | rebalance up |
| 2026-10-19T16:31 | VWAP momentum · 1h | buy | LABU | 4.86 | — | rebalance up |
| 2026-10-19T16:31 | VWAP momentum · 1h | buy | GOOGL | 4.92 | — | rebalance up |
| 2026-10-19T16:31 | VWAP momentum · 1h | buy | AMZN | 4.86 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 16:55:05.000169+00:00 -> 2026-10-19 17:05:05.000169+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
