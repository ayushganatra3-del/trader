# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T16:25:05.000118+00:00 · 28570 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.71 (-9.29%)

Closed trades 81, win rate 39.5%, fees £2.79, max drawdown -9.80%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.12 | -0.00 |

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

Today: 22545 decisions in 2439 calls, $0.2860 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T16:25 | 7 / 15 / 7 | cash |  |
| Breezy | 2026-10-19T16:25 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-10-19T16:25 | 1 / 27 / 1 | COIN 73% |  |

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
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.90 | 6.90 | 10 | 70.0 | 9.42 | 3.13 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.67 | 4.67 | 0 | — | 5.44 | 2.66 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.52 | -0.48 | 0 | — | 2.01 | 0.86 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.34 | -0.66 | 0 | — | -0.05 | 0.02 | -3.13 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.25 | -0.75 | 3 | 33.3 | 3.41 | 0.80 | -7.93 | 9 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.29 | -1.71 | 54 | 31.5 | 3.19 | 1.77 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.56 | -2.44 | 111 | 32.4 | -4.46 | -2.27 | -6.22 | 273 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.55 | -2.45 | 0 | — | -0.30 | -0.06 | -5.31 | 1 |
| 15 | Hold BTC | benchmark | 97.34 | -2.66 | 0 | — | 26.04 | 3.10 | -8.68 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 97.15 | -2.85 | 36 | 16.7 | -10.44 | -1.68 | -20.84 | 107 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.22 | -2.39 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.53 | -3.48 | 0 | — | -5.68 | -2.23 | -7.04 | 1 |
| 19 | Copy: Insider buying | copy | 96.39 | -3.61 | 23 | 43.5 | -14.94 | -2.71 | -20.62 | 73 |
| 20 | Trend pullback · 1h | trend | 96.11 | -3.89 | 87 | 24.1 | -19.90 | -5.90 | -20.58 | 135 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 93.95 | -6.05 | 8 | 37.5 | -21.25 | -1.80 | -34.64 | 26 |
| 23 | Gap and go | momentum | 93.69 | -6.31 | 73 | 16.4 | 9.93 | 2.49 | -6.54 | 203 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 4.59 | 1.04 | -9.46 | 99 |
| 25 | ADX DI cross · 1h | trend | 93.40 | -6.60 | 86 | 18.6 | -13.26 | -2.50 | -15.20 | 254 |
| 26 | Daily: Momentum burst | daily | 93.32 | -6.68 | 6 | 16.7 | -5.41 | -0.66 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.11 | -7.89 | 7 | 0.0 | -3.01 | -0.19 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.95 | -8.05 | 78 | 23.1 | -3.81 | -0.40 | -16.37 | 107 |
| 29 | Parabolic SAR · 1h | trend | 91.92 | -8.08 | 102 | 22.5 | -12.74 | -2.33 | -23.89 | 269 |
| 30 | Opening range 30m | breakout | 91.39 | -8.61 | 197 | 29.4 | -11.51 | -3.17 | -17.61 | 564 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -13.39 | -2.56 | -16.91 | 1 |
| 32 | Bollinger breakout · 1h | breakout | 90.84 | -9.16 | 84 | 28.6 | -4.67 | -0.61 | -17.78 | 260 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 90.77 | -9.23 | 0 | — | 4.53 | 0.83 | -14.37 | 1 |
| 34 | Agent | meta | 90.71 | -9.29 | 81 | 39.5 | -6.41 | -3.14 | -10.12 | 232 |
| 35 | EMA 20/50 cross · 1h | trend | 90.19 | -9.81 | 58 | 13.8 | -19.32 | -3.55 | -21.40 | 126 |
| 36 | RSI momentum · 1h | momentum | 89.63 | -10.38 | 78 | 16.7 | -15.47 | -2.58 | -26.88 | 215 |
| 37 | Connors RSI(2) · 1h | reversion | 89.13 | -10.87 | 149 | 40.9 | -23.51 | -7.05 | -24.79 | 207 |
| 38 | Stochastic reversion · 1h | reversion | 89.04 | -10.96 | 152 | 46.1 | -16.98 | -2.87 | -22.24 | 370 |
| 39 | Ichimoku · 1h | trend | 88.73 | -11.27 | 55 | 14.5 | -17.49 | -3.30 | -18.08 | 113 |
| 40 | Agent (aggressive) | meta | 87.92 | -12.08 | 41 | 34.1 | -1.74 | -0.48 | -9.26 | 114 |
| 41 | Keltner breakout · 1h | breakout | 87.77 | -12.23 | 56 | 23.2 | -8.70 | -1.04 | -27.71 | 207 |
| 42 | Supertrend · 1h | trend | 87.47 | -12.53 | 86 | 12.8 | -20.50 | -4.29 | -24.40 | 220 |
| 43 | Triple EMA stack · 1h | trend | 87.40 | -12.60 | 85 | 15.3 | -22.09 | -2.95 | -34.09 | 233 |
| 44 | Opening range 15m | breakout | 86.83 | -13.17 | 247 | 25.1 | -16.61 | -4.30 | -21.40 | 702 |
| 45 | MACD cross · 1h | trend | 86.48 | -13.52 | 188 | 20.7 | -25.50 | -4.61 | -32.11 | 473 |
| 46 | Z-score reversion · 1h | reversion | 86.12 | -13.88 | 91 | 30.8 | -12.92 | -2.04 | -21.32 | 198 |
| 47 | Max aggression: 1-day momentum | meta | 85.82 | -14.18 | 15 | 33.3 | -12.47 | -0.37 | -37.31 | 42 |
| 48 | OBV trend · 1h | momentum | 85.52 | -14.48 | 176 | 17.6 | -27.82 | -4.50 | -34.83 | 321 |
| 49 | MFI reversion · 1h | reversion | 84.78 | -15.22 | 209 | 31.1 | -17.00 | -2.64 | -21.34 | 138 |
| 50 | Agent (ML meta-label) | meta | 84.48 | -15.52 | 666 | 18.8 | -17.40 | -2.53 | -21.43 | 395 |
| 51 | MACD zero-line · 1h | trend | 84.30 | -15.70 | 87 | 14.9 | -24.91 | -4.98 | -25.15 | 218 |
| 52 | Donchian 20/10 · 1h | breakout | 83.57 | -16.43 | 81 | 17.3 | -0.11 | 0.20 | -25.09 | 215 |
| 53 | Williams %R · 1h | reversion | 82.76 | -17.24 | 182 | 42.9 | -33.08 | -5.20 | -36.50 | 535 |
| 54 | Bollinger reversion · 1h | reversion | 82.74 | -17.26 | 157 | 34.4 | -28.20 | -5.43 | -33.31 | 351 |
| 55 | Three white soldiers | momentum | 82.64 | -17.36 | 230 | 19.1 | -47.31 | -18.91 | -47.41 | 606 |
| 56 | ROC + volume · 1h | momentum | 81.50 | -18.50 | 197 | 20.8 | -17.50 | -2.22 | -33.00 | 391 |
| 57 | CCI reversion · 1h | reversion | 81.25 | -18.75 | 163 | 39.3 | -19.95 | -2.54 | -27.44 | 440 |
| 58 | RSI(14) reversion · 1h | reversion | 81.11 | -18.89 | 75 | 21.3 | -12.77 | -2.23 | -22.27 | 180 |
| 59 | EMA 9/21 cross · 1h | trend | 80.56 | -19.44 | 131 | 11.5 | -24.90 | -4.90 | -28.75 | 315 |
| 60 | Heikin-Ashi · 1h | trend | 79.50 | -20.50 | 212 | 22.6 | -35.99 | -5.97 | -44.28 | 681 |
| 61 | VWAP momentum · 1h | momentum | 78.68 | -21.32 | 418 | 20.3 | -35.61 | -4.73 | -47.97 | 1249 |
| 62 | Candlestick reversal · 1h | reversion | 78.16 | -21.84 | 210 | 26.7 | -34.38 | -6.01 | -37.86 | 534 |
| 63 | ROC + volume | momentum | 62.48 | -37.52 | 585 | 22.2 | -75.59 | -17.38 | -78.19 | 1733 |
| 64 | Volume breakout | breakout | 61.60 | -38.40 | 358 | 13.1 | -62.51 | -17.62 | -64.19 | 877 |
| 65 | Squeeze breakout | breakout | 60.82 | -39.18 | 456 | 14.3 | -64.05 | -20.79 | -65.58 | 1203 |
| 66 | Donchian 55/20 | breakout | 59.59 | -40.41 | 463 | 17.9 | -67.93 | -13.89 | -72.80 | 1273 |
| 67 | RSI(14) reversion | reversion | 57.98 | -42.02 | 700 | 24.9 | -74.52 | -16.45 | -74.59 | 1622 |
| 68 | EMA 20/50 cross | trend | 57.46 | -42.53 | 491 | 18.9 | -75.44 | -14.25 | -80.26 | 1423 |
| 69 | VWAP reversion | reversion | 53.99 | -46.01 | 737 | 25.0 | -72.19 | -14.85 | -72.96 | 1516 |
| 70 | Keltner breakout | breakout | 51.59 | -48.41 | 663 | 16.3 | -82.59 | -26.35 | -83.37 | 1819 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.74 | -98.65 | 5319 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.16 | -29.22 | -93.67 | 2568 |
| 73 | AI bee: Boozy | ai | 50.49 | -49.51 | 346 | 5.8 | — | — | — | — |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.25 | -19.96 | -88.01 | 1896 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.90 | -23.65 | -90.93 | 2341 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.96 | -25.58 | -91.04 | 2266 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -32.19 | -97.48 | 3487 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.54 | -35.01 | -96.71 | 3578 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.26 | -26.15 | -94.61 | 2580 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.60 | -22.95 | -82.93 | 1706 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.15 | -99.38 | 5746 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.04 | -25.14 | -91.85 | 2620 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.12 | -31.63 | -96.12 | 3486 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.64 | -99.74 | 6177 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.41 | -28.76 | -91.45 | 2337 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -38.18 | -97.55 | 3628 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.38 | -98.47 | 4707 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.65 | -32.39 | -93.86 | 2798 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.18 | -99.53 | 6171 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.79 | -22.31 | -86.82 | 2143 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.86 | -26.68 | -87.88 | 2141 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.61 | -95.89 | 3758 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.89 | -32.20 | -88.97 | 2098 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -33.38 | -95.74 | 4106 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.14 | -99.90 | 8275 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T16:25 | Keltner breakout | buy | TSLA | 6.45 | — | rebalance up |
| 2026-10-19T16:25 | Keltner breakout | buy | NVDA | 5.55 | — | rebalance up |
| 2026-10-19T16:25 | Keltner breakout | buy | LABU | 5.45 | — | rebalance up |
| 2026-10-19T16:25 | Keltner breakout | sell | TQQQ | 7.36 | 0.02 | exit signal |
| 2026-10-19T16:25 | Keltner breakout | sell | TECL | 7.34 | 0.03 | stop-loss |
| 2026-10-19T16:25 | Keltner breakout | sell | QQQ | 7.37 | 0.00 | stop-loss |
| 2026-10-19T16:25 | Gap and go | sell | QQQ | 23.34 | 0.04 | stop-loss |
| 2026-10-19T16:20 | Agent (aggressive) | sell | SQQQ | 44.06 | 0.19 | selected signal exited |
| 2026-10-19T16:20 | Agent | sell | SQQQ | 18.21 | 0.08 | selected signal exited |
| 2026-10-19T16:20 | RSI(14) reversion | buy | AAPL | 14.49 | — | entry signal |
| 2026-10-19T16:20 | Three white soldiers | sell | NVDA | 16.56 | 0.05 | exit signal |
| 2026-10-19T16:20 | Keltner breakout | sell | SOXL | 6.42 | -0.04 | exit signal |
| 2026-10-19T16:20 | ROC + volume | buy | TSLA | 3.15 | — | rebalance up |
| 2026-10-19T16:20 | ROC + volume | buy | PLTR | 3.15 | — | rebalance up |
| 2026-10-19T16:20 | ROC + volume | buy | NVDA | 3.17 | — | rebalance up |
| 2026-10-19T16:20 | ROC + volume | sell | QQQ | 12.48 | 0.00 | exit signal |
| 2026-10-19T16:15 | Agent (ML meta-label) | buy | SQQQ | 1.06 | — | following Williams %R, Bollinger reversion, Heikin-Ashi · 1h |
| 2026-10-19T16:15 | Agent (ML meta-label) | buy | GOOGL | 4.23 | — | entry |
| 2026-10-19T16:15 | Agent (ML meta-label) | sell | SPY | 4.44 | -0.00 | selected signal exited |
| 2026-10-19T16:10 | Agent (ML meta-label) | buy | SPY | 4.45 | — | entry |
| 2026-10-19T16:10 | Agent (ML meta-label) | sell | GOOGL | 5.30 | -0.02 | selected signal exited |
| 2026-10-19T16:10 | Keltner breakout | buy | TQQQ | 2.68 | — | rebalance up |
| 2026-10-19T16:10 | Keltner breakout | buy | TECL | 2.67 | — | rebalance up |
| 2026-10-19T16:10 | Keltner breakout | buy | QQQ | 2.68 | — | rebalance up |
| 2026-10-19T16:10 | Keltner breakout | buy | NVDA | 2.65 | — | rebalance up |
| 2026-10-19T16:10 | Keltner breakout | buy | LABU | 2.63 | — | rebalance up |
| 2026-10-19T16:10 | Keltner breakout | sell | GOOGL | 4.68 | 0.02 | exit signal |
| 2026-10-19T16:10 | ROC + volume | buy | TSLA | 5.51 | — | rebalance up |
| 2026-10-19T16:10 | ROC + volume | buy | QQQ | 5.53 | — | rebalance up |
| 2026-10-19T16:10 | ROC + volume | buy | PLTR | 5.49 | — | rebalance up |
| 2026-10-19T16:10 | ROC + volume | buy | NVDA | 5.50 | — | rebalance up |
| 2026-10-19T16:10 | ROC + volume | buy | LABU | 3.55 | — | rebalance up |
| 2026-10-19T16:10 | ROC + volume | sell | TNA | 6.90 | -0.05 | stop-loss |
| 2026-10-19T16:10 | ROC + volume | sell | AMZN | 6.98 | 0.15 | exit signal |
| 2026-10-19T16:05 | VWAP reversion | buy | ETH-USD | 13.48 | — | entry signal |
| 2026-10-19T16:05 | Three white soldiers | sell | TNA | 20.61 | -0.00 | exit signal |
| 2026-10-19T16:05 | Three white soldiers | sell | IWM | 20.65 | 0.00 | exit signal |
| 2026-10-19T16:05 | Three white soldiers | sell | AMZN | 16.53 | -0.05 | exit signal |
| 2026-10-19T16:05 | Volume breakout | sell | LABU | 15.36 | -0.07 | target is flat |
| 2026-10-19T16:05 | Volume breakout | sell | AMZN | 15.39 | -0.05 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 16:25:05.000118+00:00 -> 2026-10-19 16:35:05.000118+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
