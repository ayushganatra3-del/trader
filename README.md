# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T16:37:05.000138+00:00 · 53591 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.75 (-12.25%)

Closed trades 158, win rate 36.1%, fees £4.90, max drawdown -12.91%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 17.74 | +0.14 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 19365 decisions in 2637 calls, $0.2533 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T16:37 | 2 / 6 / 22 | cash |  |
| Breezy | 2026-11-09T16:37 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-09T16:37 | 4 / 25 / 1 | COIN 59% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| VWAP momentum | TSLA | 1.69 | +2.40% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.66 | 15.66 | 19 | 68.4 | 15.11 | 3.21 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.14 | 11.14 | 0 | — | 12.38 | 4.16 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.12 | 10.12 | 30 | 26.7 | 17.85 | 2.83 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.29 | 2.29 | 30 | 43.3 | 1.89 | 0.57 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.27 | 1.27 | 0 | — | 4.67 | 1.36 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.59 | 0.59 | 123 | 35.0 | 8.83 | 3.80 | -2.27 | 89 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.47 | -0.53 | 7 | 42.9 | -2.61 | -0.00 | -18.69 | 8 |
| 10 | Gap and go | momentum | 97.25 | -2.75 | 179 | 29.1 | 1.95 | 0.68 | -9.06 | 241 |
| 11 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.05 | -3.08 | -12.05 | 152 |
| 12 | Agent (rotation) | meta | 97.08 | -2.92 | 176 | 27.8 | -3.61 | -1.73 | -9.58 | 161 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.29 | -3.71 | 0 | — | -2.42 | -0.71 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.25 | -5.75 | 0 | — | -4.00 | -1.08 | -9.25 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 18 | Trend pullback · 1h | trend | 92.74 | -7.26 | 108 | 23.1 | -13.57 | -5.08 | -17.86 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.33 | -7.67 | 0 | — | -4.72 | -1.31 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Copy: Insider buying | copy | 89.77 | -10.22 | 40 | 37.5 | -10.94 | -2.48 | -16.06 | 63 |
| 22 | Opening range 30m | breakout | 89.49 | -10.51 | 376 | 32.4 | -15.03 | -4.86 | -15.99 | 598 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -7.83 | -2.71 | -14.15 | 79 |
| 24 | Agent | meta | 87.75 | -12.25 | 158 | 36.1 | -12.96 | -6.71 | -13.58 | 199 |
| 25 | Hold BTC | benchmark | 87.24 | -12.76 | 1 | 0.0 | -4.94 | -0.54 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.62 | -13.38 | 15 | 20.0 | -9.40 | -1.36 | -17.10 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.49 | -14.51 | 167 | 26.9 | -11.56 | -2.10 | -21.29 | 226 |
| 28 | Agent (aggressive) | meta | 84.33 | -15.68 | 75 | 32.0 | -16.29 | -4.67 | -18.49 | 92 |
| 29 | Donchian 55/20 · 1h | breakout | 84.02 | -15.98 | 71 | 14.1 | -15.42 | -3.23 | -21.87 | 103 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 83.65 | -16.35 | 2 | 0.0 | -9.29 | -0.99 | -24.16 | 1 |
| 31 | Stochastic reversion · 1h | reversion | 83.54 | -16.46 | 279 | 48.4 | -22.55 | -3.22 | -27.15 | 387 |
| 32 | Opening range 15m | breakout | 82.90 | -17.10 | 465 | 30.5 | -19.56 | -5.69 | -20.97 | 735 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.85 | -3.37 | -21.11 | 95 |
| 34 | Keltner breakout · 1h | breakout | 81.16 | -18.84 | 107 | 23.4 | -24.35 | -5.19 | -25.48 | 178 |
| 35 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -19.05 | -6.36 | -19.64 | 125 |
| 36 | Heikin-Ashi · 1h | trend | 79.33 | -20.66 | 394 | 23.1 | -38.94 | -7.46 | -41.91 | 683 |
| 37 | MFI reversion · 1h | reversion | 79.30 | -20.70 | 346 | 33.8 | -17.17 | -2.19 | -21.23 | 164 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -38.20 | -2.56 | -44.97 | 25 |
| 39 | ADX DI cross · 1h | trend | 78.80 | -21.20 | 179 | 18.4 | -24.54 | -4.21 | -28.65 | 271 |
| 40 | CCI reversion · 1h | reversion | 78.55 | -21.45 | 308 | 43.8 | -24.89 | -3.85 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 42 | Bollinger breakout · 1h | breakout | 77.00 | -23.00 | 170 | 22.9 | -22.45 | -4.64 | -27.77 | 241 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.13 | -4.02 | -32.86 | 372 |
| 44 | Williams %R · 1h | reversion | 75.19 | -24.81 | 334 | 46.7 | -32.46 | -4.88 | -36.08 | 541 |
| 45 | MACD cross · 1h | trend | 74.97 | -25.03 | 349 | 22.6 | -32.40 | -5.32 | -39.51 | 486 |
| 46 | Z-score reversion · 1h | reversion | 74.74 | -25.26 | 176 | 36.4 | -20.83 | -3.04 | -27.66 | 226 |
| 47 | EMA 20/50 cross · 1h | trend | 74.59 | -25.41 | 102 | 10.8 | -21.67 | -3.63 | -31.13 | 129 |
| 48 | MACD zero-line · 1h | trend | 74.31 | -25.69 | 157 | 16.6 | -25.06 | -5.17 | -29.22 | 208 |
| 49 | Supertrend · 1h | trend | 72.99 | -27.01 | 167 | 13.2 | -31.18 | -5.79 | -34.46 | 232 |
| 50 | Triple EMA stack · 1h | trend | 72.81 | -27.19 | 142 | 14.8 | -26.57 | -4.77 | -34.73 | 203 |
| 51 | RSI momentum · 1h | momentum | 72.73 | -27.27 | 159 | 12.6 | -24.13 | -3.85 | -33.28 | 215 |
| 52 | OBV trend · 1h | momentum | 71.75 | -28.25 | 274 | 18.2 | -28.77 | -5.90 | -34.27 | 277 |
| 53 | ROC + volume · 1h | momentum | 70.85 | -29.15 | 349 | 25.5 | -37.92 | -7.32 | -39.80 | 387 |
| 54 | Daily: Momentum burst | daily | 70.75 | -29.25 | 26 | 11.5 | -38.19 | -5.38 | -39.42 | 31 |
| 55 | Donchian 20/10 · 1h | breakout | 70.11 | -29.89 | 142 | 19.7 | -31.24 | -5.82 | -35.64 | 208 |
| 56 | RSI(14) reversion · 1h | reversion | 68.02 | -31.98 | 158 | 29.7 | -32.05 | -4.85 | -35.16 | 247 |
| 57 | Agent (ML meta-label) | meta | 67.91 | -32.09 | 1566 | 23.4 | -14.06 | -1.89 | -23.62 | 342 |
| 58 | VWAP momentum · 1h | momentum | 67.47 | -32.53 | 804 | 21.8 | -52.46 | -11.34 | -53.70 | 1238 |
| 59 | Max aggression: 1-day momentum | meta | 65.86 | -34.14 | 27 | 25.9 | -34.06 | -1.87 | -57.50 | 42 |
| 60 | EMA 9/21 cross · 1h | trend | 65.56 | -34.44 | 246 | 9.8 | -39.57 | -7.80 | -41.05 | 329 |
| 61 | Candlestick reversal · 1h | reversion | 65.50 | -34.50 | 431 | 28.3 | -38.36 | -7.07 | -39.53 | 592 |
| 62 | Three white soldiers | momentum | 62.39 | -37.61 | 492 | 15.0 | -48.78 | -22.61 | -48.79 | 648 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -45.69 | -98.99 | 5275 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.96 | -26.33 | -80.07 | 1425 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.27 | -46.60 | -93.35 | 2510 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.37 | -32.29 | -89.48 | 1916 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.79 | -40.10 | -90.85 | 2303 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.73 | -90.03 | 2182 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -54.64 | -97.75 | 3467 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -57.91 | -96.32 | 3406 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -32.77 | -93.69 | 2415 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.39 | -35.25 | -82.43 | 1672 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -55.54 | -99.53 | 5972 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.46 | -43.73 | -92.57 | 2598 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.60 | -37.93 | -95.60 | 3409 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -74.72 | -99.80 | 6174 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.87 | -44.08 | -91.88 | 2266 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.90 | -24.84 | -76.22 | 1593 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -62.20 | -97.69 | 3491 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.15 | -98.84 | 4893 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.88 | -27.97 | -69.38 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -55.16 | -94.66 | 2736 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.07 | -37.27 | -85.08 | 1770 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -74.50 | -99.66 | 6387 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.66 | -32.63 | -89.69 | 2293 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.69 | -20.07 | -78.82 | 1754 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.62 | -36.35 | -90.77 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.79 | -52.76 | -96.82 | 3904 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.38 | -58.07 | -89.41 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.06 | -29.04 | -66.26 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.55 | -23.53 | -72.03 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.53 | -19.07 | -79.73 | 1694 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.29 | -50.00 | -97.34 | 4325 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -106.01 | -99.93 | 8270 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T16:35 | Day trade: Stocks in Play ORB | sell | NVDA | 24.12 | -0.21 | target is flat |
| 2026-11-09T16:35 | Agent (ML meta-label) | buy | TECL | 4.25 | — | rebalance up |
| 2026-11-09T16:35 | Agent (ML meta-label) | buy | SPY | 4.95 | — | entry |
| 2026-11-09T16:35 | Agent (ML meta-label) | sell | SOXL | 4.78 | -0.09 | selected signal exited |
| 2026-11-09T16:35 | Gap and go | buy | LABU | 4.88 | — | rebalance up |
| 2026-11-09T16:35 | Gap and go | buy | AMD | 4.91 | — | rebalance up |
| 2026-11-09T16:35 | Gap and go | sell | SOXL | 19.40 | 1.00 | stop-loss |
| 2026-11-09T16:30 | Agent (ML meta-label) | sell | TECL | 3.65 | 0.15 | rebalance down |
| 2026-11-09T16:30 | Agent (aggressive) | sell | COIN | 42.32 | 0.31 | selected signal exited |
| 2026-11-09T16:30 | Agent | sell | COIN | 34.99 | 0.08 | selected signal exited |
| 2026-11-09T16:30 | MFI reversion · 1h | buy | NVDA | 3.46 | — | entry signal |
| 2026-11-09T16:30 | MFI reversion · 1h | buy | ETHU | 7.19 | — | entry signal |
| 2026-11-09T16:30 | MFI reversion · 1h | sell | SOXL | 10.66 | 1.35 | exit signal |
| 2026-11-09T16:30 | Williams %R · 1h | sell | UPRO | 18.67 | -0.07 | exit signal |
| 2026-11-09T16:30 | Williams %R · 1h | sell | SPY | 18.89 | -0.03 | exit signal |
| 2026-11-09T16:30 | Z-score reversion · 1h | buy | TQQQ | 4.18 | — | rebalance up |
| 2026-11-09T16:30 | Z-score reversion · 1h | buy | TECL | 3.90 | — | rebalance up |
| 2026-11-09T16:30 | Z-score reversion · 1h | sell | TNA | 4.66 | 0.35 | exit signal |
| 2026-11-09T16:30 | Z-score reversion · 1h | sell | LABU | 4.70 | 0.39 | exit signal |
| 2026-11-09T16:30 | RSI(14) reversion · 1h | buy | SOL-USD | 3.75 | — | rebalance up |
| 2026-11-09T16:30 | RSI(14) reversion · 1h | buy | ETH-USD | 3.73 | — | rebalance up |
| 2026-11-09T16:30 | RSI(14) reversion · 1h | sell | PLTR | 4.64 | 0.20 | exit signal |
| 2026-11-09T16:30 | Candlestick reversal · 1h | buy | SQQQ | 7.96 | — | entry signal |
| 2026-11-09T16:30 | Keltner breakout · 1h | buy | IWM | 20.31 | — | entry signal |
| 2026-11-09T16:30 | Donchian 20/10 · 1h | buy | AMD | 17.55 | — | entry signal |
| 2026-11-09T16:30 | RSI momentum · 1h | buy | TNA | 10.38 | — | entry signal |
| 2026-11-09T16:30 | RSI momentum · 1h | buy | IWM | 10.40 | — | entry signal |
| 2026-11-09T16:30 | RSI momentum · 1h | sell | META | 4.19 | 0.01 | rebalance down |
| 2026-11-09T16:30 | RSI momentum · 1h | sell | GOOGL | 4.02 | -0.04 | rebalance down |
| 2026-11-09T16:30 | RSI momentum · 1h | sell | AMZN | 4.11 | 0.12 | rebalance down |
| 2026-11-09T16:30 | RSI momentum · 1h | sell | AMD | 4.33 | 0.05 | rebalance down |
| 2026-11-09T16:30 | RSI momentum · 1h | sell | AAPL | 4.13 | -0.01 | rebalance down |
| 2026-11-09T16:30 | VWAP momentum · 1h | buy | XRP-USD | 3.55 | — | entry |
| 2026-11-09T16:30 | VWAP momentum · 1h | sell | QQQ | 3.06 | 0.00 | exit signal |
| 2026-11-09T16:30 | VWAP momentum · 1h | sell | MSTR | 3.02 | 0.06 | exit signal |
| 2026-11-09T16:30 | VWAP momentum · 1h | sell | BITX | 3.04 | -0.09 | exit signal |
| 2026-11-09T16:30 | Heikin-Ashi · 1h | buy | UPRO | 3.89 | — | entry signal |
| 2026-11-09T16:30 | Heikin-Ashi · 1h | buy | TSLA | 3.97 | — | entry signal |
| 2026-11-09T16:30 | Heikin-Ashi · 1h | buy | TQQQ | 3.97 | — | entry signal |
| 2026-11-09T16:30 | Heikin-Ashi · 1h | buy | TECL | 3.97 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 16:37:05.000138+00:00 -> 2026-11-09 16:47:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 16:37:05.000138+00:00 -> 2026-11-09 16:47:05.000138+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 16:37:05.000138+00:00 -> 2026-11-09 16:47:05.000138+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
