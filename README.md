# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T17:15:05.000141+00:00 · 70795 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £79.17 (-20.83%)

Closed trades 239, win rate 36.0%, fees £6.49, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 20579 decisions in 2551 calls, $0.2656 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T17:15 | 16 / 10 / 4 | cash |  |
| Breezy | 2026-11-23T17:15 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-23T17:15 | 11 / 18 / 1 | COIN 64% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.81% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 32.17 | 4.75 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.60 | 15.60 | 0 | — | 13.76 | 4.63 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.55 | 1.38 | -9.74 | 35 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.85 | 3.85 | 0 | — | 1.91 | 0.61 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.63 | -0.37 | 215 | 32.1 | -0.80 | -0.16 | -8.71 | 210 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.78 | -3.55 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.17 | -3.83 | 225 | 28.9 | -0.95 | -0.22 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.77 | -4.23 | 0 | — | -6.52 | -1.63 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.26 | -3.16 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.15 | -7.86 | 0 | — | -9.10 | -1.91 | -13.87 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 16 | VWAP reversion · 1h | reversion | 91.70 | -8.30 | 163 | 46.0 | -5.72 | -0.82 | -20.49 | 156 |
| 17 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.56 | -3.47 | -8.72 | 31 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.41 | -9.59 | 0 | — | -10.98 | -2.42 | -17.03 | 1 |
| 19 | Copy: Insider buying | copy | 89.35 | -10.65 | 57 | 40.4 | -18.64 | -3.66 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.92 | -3.27 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 87.17 | -12.83 | 9 | 44.4 | -10.51 | -0.54 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.87 | -13.12 | 455 | 33.4 | -12.60 | -4.22 | -14.52 | 542 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -17.52 | -3.94 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 84.09 | -15.91 | 75 | 20.0 | -18.34 | -7.23 | -18.74 | 74 |
| 25 | Parabolic SAR · 1h | trend | 81.29 | -18.70 | 200 | 27.0 | -26.73 | -7.31 | -29.75 | 191 |
| 26 | Connors RSI(2) · 1h | reversion | 80.75 | -19.25 | 219 | 40.6 | -13.37 | -5.72 | -14.31 | 66 |
| 27 | Agent | meta | 79.17 | -20.83 | 239 | 36.0 | -25.61 | -5.60 | -26.32 | 200 |
| 28 | Donchian 55/20 · 1h | breakout | 78.32 | -21.68 | 82 | 12.2 | -27.73 | -7.75 | -28.72 | 84 |
| 29 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -25.70 | -4.32 | -26.03 | 95 |
| 30 | Opening range 15m | breakout | 77.77 | -22.23 | 566 | 30.9 | -22.20 | -6.86 | -23.54 | 661 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.15 | -7.23 | -22.73 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -27.80 | -7.28 | -28.76 | 152 |
| 33 | Ichimoku · 1h | trend | 74.60 | -25.40 | 110 | 13.6 | -28.63 | -7.69 | -30.49 | 106 |
| 34 | Hold BTC | benchmark | 72.20 | -27.80 | 3 | 0.0 | -28.64 | -5.04 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 71.81 | -28.19 | 199 | 16.6 | -33.22 | -6.28 | -38.02 | 222 |
| 36 | Triple EMA stack · 1h | trend | 71.04 | -28.95 | 161 | 14.3 | -35.30 | -9.02 | -38.27 | 166 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 70.97 | -29.03 | 3 | 0.0 | -23.93 | -2.86 | -32.18 | 1 |
| 38 | EMA 20/50 cross · 1h | trend | 70.80 | -29.20 | 119 | 10.1 | -35.52 | -9.81 | -39.53 | 123 |
| 39 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -35.58 | -6.53 | -38.55 | 281 |
| 40 | Daily: Momentum burst | daily | 68.99 | -31.01 | 30 | 13.3 | -37.91 | -5.42 | -38.52 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.83 | -31.17 | 207 | 22.2 | -33.16 | -8.69 | -34.38 | 213 |
| 42 | OBV trend · 1h | momentum | 68.01 | -31.99 | 319 | 19.4 | -37.80 | -9.82 | -40.32 | 231 |
| 43 | Stochastic reversion · 1h | reversion | 67.50 | -32.50 | 392 | 40.6 | -35.63 | -3.74 | -44.44 | 436 |
| 44 | Max aggression: 5-day momentum | meta | 66.61 | -33.40 | 24 | 37.5 | -60.59 | -3.96 | -64.62 | 23 |
| 45 | RSI momentum · 1h | momentum | 66.28 | -33.72 | 188 | 13.8 | -37.42 | -8.26 | -39.43 | 203 |
| 46 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -35.05 | -9.53 | -35.30 | 208 |
| 47 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -46.62 | -9.49 | -47.47 | 633 |
| 48 | MFI reversion · 1h | reversion | 64.17 | -35.83 | 486 | 32.9 | -31.11 | -4.43 | -37.45 | 185 |
| 49 | Donchian 20/10 · 1h | breakout | 63.73 | -36.27 | 173 | 16.8 | -38.99 | -8.52 | -40.83 | 194 |
| 50 | ROC + volume · 1h | momentum | 62.49 | -37.51 | 443 | 27.3 | -42.06 | -8.62 | -42.36 | 342 |
| 51 | EMA 9/21 cross · 1h | trend | 61.11 | -38.89 | 298 | 11.1 | -44.18 | -10.55 | -45.87 | 327 |
| 52 | Agent (ML meta-label) | meta | 60.47 | -39.53 | 2035 | 25.0 | -18.41 | -2.06 | -30.30 | 313 |
| 53 | MACD cross · 1h | trend | 59.91 | -40.09 | 464 | 20.9 | -48.30 | -9.20 | -50.16 | 518 |
| 54 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -52.67 | -3.83 | -54.71 | 38 |
| 55 | CCI reversion · 1h | reversion | 58.58 | -41.42 | 430 | 40.0 | -49.03 | -8.13 | -52.02 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 58.19 | -41.80 | 391 | 37.6 | -38.00 | -4.47 | -45.42 | 436 |
| 57 | Williams %R · 1h | reversion | 54.61 | -45.39 | 492 | 38.2 | -54.16 | -8.87 | -55.92 | 595 |
| 58 | VWAP momentum · 1h | momentum | 54.00 | -45.99 | 1039 | 21.7 | -58.08 | -13.38 | -58.96 | 1197 |
| 59 | RSI(14) reversion · 1h | reversion | 51.42 | -48.58 | 239 | 31.4 | -46.40 | -7.01 | -49.37 | 292 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.91 | -8.55 | -54.94 | 690 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -47.80 | -99.14 | 5340 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.84 | -32.14 | -84.56 | 1437 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.47 | -48.43 | -94.53 | 2424 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.88 | -31.47 | -91.06 | 1927 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.77 | -40.83 | -91.82 | 2256 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.28 | -27.59 | -89.39 | 1945 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.16 | -48.33 | -98.16 | 3415 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.97 | -51.74 | -97.00 | 3357 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -38.58 | -93.63 | 2158 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.23 | -22.39 | -52.28 | 649 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.22 | -34.73 | -83.41 | 1545 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.01 | -99.66 | 6291 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.23 | -40.33 | -93.23 | 2495 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.30 | -35.56 | -94.31 | 3139 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -62.34 | -99.82 | 6134 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.22 | -42.60 | -93.43 | 2264 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.52 | -24.11 | -78.93 | 1617 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -55.82 | -97.78 | 3285 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -56.87 | -99.17 | 5103 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.85 | -28.23 | -71.00 | 1198 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.96 | -48.99 | -94.98 | 2676 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.44 | -6.09 | -48.72 | 281 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.69 | -37.06 | -85.73 | 1687 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.51 | -99.76 | 6527 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.55 | -30.08 | -91.68 | 2468 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.97 | -19.72 | -83.00 | 1959 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.72 | -28.73 | -92.06 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.11 | -46.77 | -98.13 | 4057 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.17 | -46.86 | -90.20 | 2191 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.54 | -30.00 | -68.55 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.14 | -28.39 | -74.32 | 1170 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.89 | -18.97 | -83.93 | 1849 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.96 | -47.97 | -97.98 | 4436 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -90.98 | -99.94 | 8284 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T17:05 | ROC + volume · 1h | buy | BTC-USD | 7.68 | — | entry |
| 2026-11-23T17:05 | ROC + volume · 1h | sell | XRP-USD | 7.68 | -0.18 | stop-loss |
| 2026-11-23T17:00 | Agent (rotation) | buy | LABU | 8.02 | — | entry |
| 2026-11-23T17:00 | VWAP momentum · 1h | sell | SOL-USD | 2.31 | 0.10 | exit signal |
| 2026-11-23T17:00 | VWAP momentum · 1h | sell | BTC-USD | 2.33 | 0.04 | exit signal |
| 2026-11-23T17:00 | Gap and go | buy | LABU | 24.97 | — | entry |
| 2026-11-23T16:55 | Agent (rotation) | sell | LABU | 8.21 | 0.11 | selected signal exited |
| 2026-11-23T16:55 | Agent (ML meta-label) | buy | BITX | 4.13 | — | entry |
| 2026-11-23T16:55 | Opening range 30m | sell | AAPL | 9.67 | -0.08 | stop-loss |
| 2026-11-23T16:55 | Opening range 15m | sell | AAPL | 8.67 | -0.07 | stop-loss |
| 2026-11-23T16:55 | Gap and go | sell | LABU | 25.01 | 0.11 | target is flat |
| 2026-11-23T16:50 | Agent (rotation) | sell | TQQQ | 3.50 | -0.09 | selected signal exited |
| 2026-11-23T16:50 | Agent (ML meta-label) | sell | BITX | 4.13 | -0.08 | selected signal exited |
| 2026-11-23T16:50 | VWAP momentum · 1h | buy | SPY | 2.83 | — | entry |
| 2026-11-23T16:50 | Gap and go | sell | TQQQ | 24.96 | -0.44 | target is flat |
| 2026-11-23T16:45 | Agent (rotation) | sell | UPRO | 3.51 | -0.07 | selected signal exited |
| 2026-11-23T16:45 | Gap and go | sell | UPRO | 24.87 | -0.43 | exit signal |
| 2026-11-23T16:40 | Agent (rotation) | sell | TSLA | 7.96 | -0.08 | selected signal exited |
| 2026-11-23T16:40 | Agent | sell | SQQQ | 16.47 | -0.14 | selected signal exited |
| 2026-11-23T16:40 | Donchian 55/20 · 1h | sell | BTC-USD | 19.64 | -0.38 | stop-loss |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | XRP-USD | 2.58 | 0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | UPRO | 2.46 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | TSLA | 2.60 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | TQQQ | 2.57 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | TNA | 2.59 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | TECL | 2.57 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | SPY | 2.60 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | SOXL | 2.55 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | SOL-USD | 2.58 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | QQQ | 2.60 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | PLTR | 2.58 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | NVDA | 2.57 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | MSTR | 2.58 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | MSFT | 2.61 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | META | 2.61 | -0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | LABU | 2.59 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | IWM | 2.61 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | GOOGL | 2.60 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | ETHU | 2.60 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.58 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 17:15:05.000141+00:00 -> 2026-11-23 17:25:05.000141+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
