# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T14:25:05.000167+00:00 · 28471 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.06 (-8.94%)

Closed trades 78, win rate 38.5%, fees £2.72, max drawdown -9.36%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.38 | +0.07 |
| SQQQ | 36.17 | -0.30 |

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

Today: 13707 decisions in 2142 calls, $0.1828 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T14:25 | 6 / 15 / 9 | LABU 15% |  |
| Breezy | 2026-10-19T14:25 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-10-19T14:25 | 2 / 28 / 0 | COIN 73% |  |

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
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 10.33 | 3.45 | -3.27 | 18 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.77 | 4.77 | 0 | — | 5.47 | 2.67 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.01 | 2.01 | 64 | 39.1 | -8.07 | -2.23 | -13.79 | 136 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.59 | 0.59 | 0 | — | 3.51 | 1.43 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.34 | -0.66 | 0 | — | 0.07 | 0.08 | -3.13 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.17 | -0.83 | 3 | 33.3 | 3.38 | 0.80 | -7.93 | 9 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 97.98 | -2.02 | 54 | 31.5 | 2.88 | 1.59 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.83 | -2.17 | 111 | 32.4 | -4.17 | -1.99 | -5.95 | 274 |
| 14 | Hold BTC | benchmark | 97.40 | -2.60 | 0 | — | 26.25 | 3.13 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.22 | -2.39 | -5.83 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 97.00 | -3.00 | 36 | 16.7 | -10.37 | -1.67 | -20.69 | 107 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.94 | -3.06 | 0 | — | -1.00 | -0.36 | -5.31 | 1 |
| 18 | Copy: Insider buying | copy | 96.50 | -3.50 | 23 | 43.5 | -14.80 | -2.68 | -20.62 | 73 |
| 19 | Trend pullback · 1h | trend | 96.37 | -3.62 | 87 | 24.1 | -19.71 | -5.81 | -20.64 | 134 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.12 | -3.88 | 0 | — | -7.03 | -2.78 | -7.55 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 94.05 | -5.95 | 8 | 37.5 | -21.12 | -1.79 | -34.64 | 26 |
| 23 | Daily: Momentum burst | daily | 93.68 | -6.33 | 6 | 16.7 | -5.22 | -0.63 | -20.58 | 40 |
| 24 | Gap and go | momentum | 93.55 | -6.45 | 67 | 13.4 | 9.81 | 2.47 | -6.51 | 201 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 7.24 | 1.51 | -9.46 | 102 |
| 26 | ADX DI cross · 1h | trend | 93.23 | -6.77 | 84 | 19.0 | -11.81 | -2.32 | -12.84 | 254 |
| 27 | Daily: Bullish score | daily | 92.00 | -8.00 | 7 | 0.0 | -3.13 | -0.20 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.89 | -0.12 | -14.31 | 110 |
| 29 | Parabolic SAR · 1h | trend | 91.55 | -8.45 | 100 | 23.0 | -13.74 | -2.26 | -24.61 | 273 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -13.38 | -2.56 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 91.11 | -8.89 | 195 | 29.7 | -11.48 | -3.16 | -17.60 | 560 |
| 32 | Agent | meta | 91.06 | -8.94 | 78 | 38.5 | -9.71 | -5.76 | -12.79 | 243 |
| 33 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | -2.00 | -0.15 | -15.20 | 262 |
| 34 | EMA 20/50 cross · 1h | trend | 90.35 | -9.65 | 57 | 14.0 | -18.66 | -3.24 | -20.36 | 130 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 90.27 | -9.73 | 0 | — | 4.32 | 0.80 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.42 | -10.58 | 78 | 16.7 | -16.36 | -2.87 | -26.66 | 216 |
| 37 | Connors RSI(2) · 1h | reversion | 89.20 | -10.80 | 147 | 40.1 | -23.44 | -7.01 | -24.79 | 206 |
| 38 | Agent (aggressive) | meta | 88.98 | -11.02 | 39 | 33.3 | -6.90 | -2.43 | -9.01 | 112 |
| 39 | Ichimoku · 1h | trend | 88.63 | -11.37 | 55 | 14.5 | -17.97 | -3.39 | -18.08 | 114 |
| 40 | Stochastic reversion · 1h | reversion | 88.62 | -11.38 | 150 | 45.3 | -17.28 | -2.96 | -22.24 | 371 |
| 41 | Keltner breakout · 1h | breakout | 87.49 | -12.51 | 56 | 23.2 | -11.48 | -1.51 | -27.88 | 204 |
| 42 | Supertrend · 1h | trend | 87.41 | -12.59 | 85 | 11.8 | -24.20 | -5.07 | -27.73 | 215 |
| 43 | Triple EMA stack · 1h | trend | 87.40 | -12.60 | 85 | 15.3 | -20.49 | -2.77 | -32.48 | 234 |
| 44 | Opening range 15m | breakout | 86.56 | -13.44 | 244 | 25.4 | -16.59 | -4.29 | -21.40 | 697 |
| 45 | MACD cross · 1h | trend | 86.39 | -13.61 | 185 | 21.1 | -25.68 | -4.71 | -32.13 | 463 |
| 46 | Z-score reversion · 1h | reversion | 86.12 | -13.88 | 91 | 30.8 | -12.93 | -2.04 | -21.32 | 190 |
| 47 | OBV trend · 1h | momentum | 85.89 | -14.11 | 174 | 17.8 | -22.63 | -3.07 | -34.14 | 315 |
| 48 | Max aggression: 1-day momentum | meta | 85.19 | -14.81 | 15 | 33.3 | -13.07 | -0.41 | -37.31 | 42 |
| 49 | MFI reversion · 1h | reversion | 84.65 | -15.35 | 209 | 31.1 | -17.33 | -2.70 | -21.34 | 138 |
| 50 | MACD zero-line · 1h | trend | 84.35 | -15.65 | 86 | 15.1 | -24.74 | -4.93 | -25.02 | 218 |
| 51 | Agent (ML meta-label) | meta | 83.99 | -16.01 | 660 | 18.5 | -11.52 | -1.62 | -16.18 | 379 |
| 52 | Donchian 20/10 · 1h | breakout | 83.14 | -16.86 | 81 | 17.3 | -0.99 | 0.09 | -23.16 | 216 |
| 53 | Williams %R · 1h | reversion | 82.67 | -17.33 | 180 | 42.2 | -32.97 | -5.16 | -36.50 | 521 |
| 54 | Three white soldiers | momentum | 82.60 | -17.40 | 225 | 18.2 | -47.29 | -19.03 | -47.29 | 602 |
| 55 | Bollinger reversion · 1h | reversion | 82.07 | -17.93 | 151 | 32.5 | -29.33 | -5.81 | -33.14 | 352 |
| 56 | ROC + volume · 1h | momentum | 81.11 | -18.89 | 197 | 20.8 | -15.77 | -2.15 | -28.84 | 389 |
| 57 | CCI reversion · 1h | reversion | 81.10 | -18.90 | 161 | 38.5 | -19.07 | -2.42 | -27.44 | 429 |
| 58 | RSI(14) reversion · 1h | reversion | 80.91 | -19.09 | 75 | 21.3 | -14.49 | -2.51 | -22.27 | 174 |
| 59 | EMA 9/21 cross · 1h | trend | 80.44 | -19.56 | 131 | 11.5 | -19.37 | -3.28 | -28.88 | 315 |
| 60 | Heikin-Ashi · 1h | trend | 79.90 | -20.10 | 211 | 22.7 | -35.18 | -5.85 | -43.58 | 667 |
| 61 | VWAP momentum · 1h | momentum | 78.50 | -21.50 | 416 | 20.4 | -36.04 | -4.82 | -47.74 | 1231 |
| 62 | Candlestick reversal · 1h | reversion | 78.03 | -21.97 | 209 | 26.3 | -34.51 | -5.98 | -36.92 | 540 |
| 63 | ROC + volume | momentum | 62.43 | -37.56 | 572 | 21.9 | -75.54 | -17.35 | -78.19 | 1724 |
| 64 | Volume breakout | breakout | 61.84 | -38.16 | 350 | 12.9 | -62.56 | -17.67 | -64.13 | 874 |
| 65 | Squeeze breakout | breakout | 60.61 | -39.39 | 455 | 14.1 | -62.28 | -15.88 | -65.58 | 1210 |
| 66 | Donchian 55/20 | breakout | 59.45 | -40.55 | 463 | 17.9 | -68.15 | -14.12 | -72.80 | 1276 |
| 67 | RSI(14) reversion | reversion | 57.79 | -42.21 | 693 | 24.8 | -74.61 | -16.53 | -74.61 | 1601 |
| 68 | EMA 20/50 cross | trend | 57.20 | -42.80 | 489 | 18.8 | -75.65 | -14.41 | -80.26 | 1435 |
| 69 | VWAP reversion | reversion | 53.58 | -46.42 | 727 | 24.3 | -72.42 | -15.03 | -72.97 | 1504 |
| 70 | Keltner breakout | breakout | 51.60 | -48.40 | 653 | 15.8 | -82.48 | -26.01 | -83.37 | 1810 |
| 71 | AI bee: Boozy | ai | 50.69 | -49.31 | 346 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.82 | -98.66 | 5323 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.23 | -29.26 | -93.67 | 2578 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.05 | -19.81 | -87.84 | 1888 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.96 | -23.89 | -90.91 | 2342 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.02 | -25.73 | -91.06 | 2278 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -32.33 | -97.46 | 3498 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.60 | -35.76 | -96.71 | 3588 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.53 | -26.77 | -94.87 | 2601 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.51 | -22.74 | -82.83 | 1709 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.05 | -99.37 | 5727 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.11 | -25.29 | -91.85 | 2622 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.11 | -31.69 | -96.11 | 3488 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.73 | -99.74 | 6179 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.37 | -28.71 | -91.49 | 2341 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -38.39 | -97.54 | 3636 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.62 | -98.47 | 4696 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.55 | -32.47 | -93.78 | 2789 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.20 | -99.53 | 6163 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.76 | -22.23 | -86.78 | 2152 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.94 | -26.85 | -87.95 | 2141 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.66 | -95.89 | 3763 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.81 | -32.09 | -88.97 | 2082 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.75 | -33.63 | -95.76 | 4101 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.47 | -99.90 | 8273 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T14:25 | VWAP reversion | sell | IWM | 5.34 | 0.01 | target is flat |
| 2026-10-19T14:25 | Three white soldiers | buy | NVDA | 20.65 | — | entry signal |
| 2026-10-19T14:25 | Gap and go | buy | NVDA | 9.46 | — | entry signal |
| 2026-10-19T14:25 | Gap and go | sell | TQQQ | 4.71 | 0.02 | rebalance down |
| 2026-10-19T14:25 | Gap and go | sell | AMZN | 4.75 | 0.03 | rebalance down |
| 2026-10-19T14:20 | Agent (aggressive) | sell | SQQQ | 44.51 | -0.63 | rebalance down |
| 2026-10-19T14:20 | Candlestick reversal · 1h | sell | TSLA | 6.59 | 0.23 | take-profit |
| 2026-10-19T14:20 | VWAP reversion | sell | TECL | 5.41 | 0.07 | exit signal |
| 2026-10-19T14:20 | Volume breakout | buy | QQQ | 15.46 | — | entry signal |
| 2026-10-19T14:20 | ROC + volume | buy | QQQ | 10.38 | — | entry signal |
| 2026-10-19T14:20 | ROC + volume | buy | NVDA | 10.39 | — | entry signal |
| 2026-10-19T14:20 | ROC + volume | sell | TSLA | 5.14 | 0.05 | rebalance down |
| 2026-10-19T14:20 | ROC + volume | sell | PLTR | 5.14 | 0.05 | rebalance down |
| 2026-10-19T14:20 | ROC + volume | sell | LABU | 5.41 | 0.15 | rebalance down |
| 2026-10-19T14:20 | ROC + volume | sell | AMZN | 5.09 | 0.05 | rebalance down |
| 2026-10-19T14:15 | Agent (rotation) | sell | SQQQ | 32.52 | -0.14 | selected signal exited |
| 2026-10-19T14:15 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 105.42 | -0.46 | target is flat |
| 2026-10-19T14:15 | VWAP reversion | buy | ETH-USD | 5.95 | — | entry signal |
| 2026-10-19T14:15 | VWAP reversion | sell | SPY | 5.35 | 0.01 | exit signal |
| 2026-10-19T14:15 | VWAP reversion | sell | NVDA | 5.36 | 0.03 | exit signal |
| 2026-10-19T14:15 | RSI(14) reversion | buy | XRP-USD | 8.27 | — | entry signal |
| 2026-10-19T14:15 | RSI(14) reversion | buy | SOL-USD | 8.30 | — | entry signal |
| 2026-10-19T14:15 | RSI(14) reversion | buy | META | 8.30 | — | entry signal |
| 2026-10-19T14:15 | RSI(14) reversion | buy | ETH-USD | 8.30 | — | entry signal |
| 2026-10-19T14:15 | RSI(14) reversion | buy | BTC-USD | 8.30 | — | entry signal |
| 2026-10-19T14:15 | RSI(14) reversion | sell | SQQQ | 6.10 | -0.07 | rebalance down |
| 2026-10-19T14:15 | RSI(14) reversion | sell | DOGE-USD | 6.24 | -0.02 | rebalance down |
| 2026-10-19T14:15 | Keltner breakout | buy | UPRO | 7.34 | — | entry signal |
| 2026-10-19T14:15 | Keltner breakout | buy | TQQQ | 7.35 | — | entry signal |
| 2026-10-19T14:15 | Keltner breakout | buy | TECL | 7.35 | — | entry signal |
| 2026-10-19T14:15 | Keltner breakout | buy | SPY | 7.35 | — | entry signal |
| 2026-10-19T14:15 | Keltner breakout | buy | QQQ | 7.35 | — | entry signal |
| 2026-10-19T14:15 | Keltner breakout | sell | LABU | 5.47 | -0.02 | rebalance down |
| 2026-10-19T14:15 | Keltner breakout | sell | GOOGL | 5.57 | 0.03 | rebalance down |
| 2026-10-19T14:15 | Opening range 30m | buy | UPRO | 10.08 | — | entry signal |
| 2026-10-19T14:15 | Opening range 30m | buy | TSLA | 10.10 | — | entry signal |
| 2026-10-19T14:15 | Opening range 30m | buy | TQQQ | 10.10 | — | entry signal |
| 2026-10-19T14:15 | Opening range 30m | buy | SPY | 10.10 | — | entry signal |
| 2026-10-19T14:15 | Opening range 30m | buy | QQQ | 10.10 | — | entry signal |
| 2026-10-19T14:15 | Opening range 30m | buy | PLTR | 10.10 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 14:25:05.000167+00:00 -> 2026-10-19 14:35:05.000167+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
