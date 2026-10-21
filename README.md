# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T21:51:05.000136+00:00 · 31137 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.67 (-9.33%)

Closed trades 93, win rate 40.9%, fees £3.03, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.44 · VIX 16.63 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 38928 decisions in 3174 calls, $0.4801 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T21:51 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-21T21:51 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T21:51 | 3 / 2 / 0 | ETH-USD 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.03 | 6.03 | 0 | — | 8.54 | 4.02 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.62 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.81 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.21 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.50 | 1.50 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.23 | 0.23 | 4 | 50.0 | 9.05 | 1.92 | -7.93 | 8 |
| 8 | Hold BTC | benchmark | 100.14 | 0.14 | 0 | — | 16.00 | 2.29 | -8.68 | 1 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.62 | -0.38 | 0 | — | 2.33 | 1.07 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.40 | -0.60 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.56 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.97 | -4.04 | 21 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.50 | -2.50 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.79 | -5.83 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.06 | -2.94 | 0 | — | -4.00 | -1.53 | -7.04 | 1 |
| 18 | Copy: Insider buying | copy | 96.69 | -3.31 | 25 | 40.0 | -11.33 | -1.94 | -20.62 | 72 |
| 19 | Donchian 55/20 · 1h | breakout | 96.29 | -3.71 | 41 | 17.1 | -14.22 | -2.90 | -16.00 | 103 |
| 20 | Agent (rotation) | meta | 95.78 | -4.22 | 117 | 30.8 | -8.38 | -4.92 | -8.45 | 235 |
| 21 | ADX DI cross · 1h | trend | 95.63 | -4.37 | 91 | 19.8 | -11.97 | -2.20 | -16.14 | 262 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.18 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 94.93 | -5.07 | 6 | 16.7 | -9.31 | -1.38 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.86 | -5.14 | 92 | 23.9 | -20.41 | -6.41 | -20.58 | 129 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.56 | 2.05 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.11 | -17.26 | 568 |
| 27 | Parabolic SAR · 1h | trend | 93.49 | -6.51 | 108 | 23.1 | -15.68 | -3.44 | -19.79 | 272 |
| 28 | Squeeze breakout · 1h | breakout | 93.38 | -6.62 | 46 | 21.7 | -1.53 | -0.28 | -11.48 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 92.92 | -7.08 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.39 | -7.61 | 88 | 30.7 | -9.21 | -1.64 | -15.29 | 263 |
| 31 | Daily: Bullish score | daily | 92.19 | -7.81 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.95 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.76 | -9.24 | 92 | 23.9 | -14.49 | -2.57 | -14.65 | 114 |
| 34 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -18.49 | -6.16 | -19.19 | 261 |
| 35 | Supertrend · 1h | trend | 90.27 | -9.73 | 88 | 12.5 | -20.73 | -4.15 | -26.66 | 218 |
| 36 | Connors RSI(2) · 1h | reversion | 89.85 | -10.15 | 159 | 42.1 | -22.01 | -6.61 | -23.74 | 194 |
| 37 | RSI momentum · 1h | momentum | 89.84 | -10.16 | 84 | 16.7 | -18.75 | -3.77 | -20.65 | 220 |
| 38 | Stochastic reversion · 1h | reversion | 89.55 | -10.45 | 169 | 47.3 | -13.60 | -2.23 | -22.24 | 363 |
| 39 | EMA 20/50 cross · 1h | trend | 88.93 | -11.07 | 62 | 12.9 | -20.83 | -3.61 | -23.57 | 140 |
| 40 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.22 | -19.07 | 704 |
| 41 | Keltner breakout · 1h | breakout | 88.16 | -11.84 | 62 | 24.2 | -17.61 | -3.26 | -25.20 | 204 |
| 42 | MACD cross · 1h | trend | 87.60 | -12.40 | 199 | 21.1 | -23.62 | -4.49 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -22.49 | -4.78 | -25.23 | 133 |
| 44 | Ichimoku · 1h | trend | 86.87 | -13.13 | 60 | 13.3 | -17.87 | -3.37 | -20.25 | 118 |
| 45 | Z-score reversion · 1h | reversion | 86.79 | -13.21 | 102 | 34.3 | -11.48 | -1.79 | -21.32 | 196 |
| 46 | Donchian 20/10 · 1h | breakout | 86.12 | -13.88 | 83 | 19.3 | -19.73 | -3.66 | -28.97 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.79 | -14.21 | 92 | 15.2 | -26.81 | -4.97 | -27.61 | 224 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -14.49 | -2.21 | -21.11 | 139 |
| 49 | Agent (ML meta-label) | meta | 84.63 | -15.37 | 735 | 20.1 | -13.73 | -2.46 | -16.96 | 379 |
| 50 | MACD zero-line · 1h | trend | 84.52 | -15.48 | 92 | 15.2 | -23.36 | -4.58 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 84.07 | -15.93 | 188 | 17.6 | -30.26 | -5.72 | -31.84 | 308 |
| 52 | ROC + volume · 1h | momentum | 83.01 | -16.99 | 213 | 23.5 | -26.43 | -4.77 | -33.27 | 391 |
| 53 | Williams %R · 1h | reversion | 82.60 | -17.40 | 199 | 44.7 | -31.50 | -4.92 | -36.62 | 517 |
| 54 | Bollinger reversion · 1h | reversion | 82.59 | -17.41 | 163 | 36.2 | -29.10 | -5.66 | -32.84 | 348 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.58 | -18.30 | -46.47 | 605 |
| 56 | CCI reversion · 1h | reversion | 82.12 | -17.88 | 188 | 43.6 | -20.26 | -2.65 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.45 | -18.55 | 250 | 23.6 | -42.82 | -9.24 | -46.38 | 678 |
| 58 | EMA 9/21 cross · 1h | trend | 80.96 | -19.04 | 143 | 10.5 | -26.85 | -5.24 | -29.94 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 80.88 | -19.12 | 85 | 24.7 | -16.91 | -2.91 | -24.99 | 172 |
| 60 | VWAP momentum · 1h | momentum | 79.19 | -20.81 | 478 | 21.3 | -46.43 | -8.87 | -52.82 | 1247 |
| 61 | Candlestick reversal · 1h | reversion | 79.02 | -20.98 | 231 | 30.3 | -38.08 | -7.02 | -41.83 | 537 |
| 62 | Max aggression: 1-day momentum | meta | 77.14 | -22.86 | 17 | 29.4 | -34.21 | -2.15 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.64 | -22.13 | -78.91 | 1711 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -65.11 | -20.58 | -65.35 | 875 |
| 65 | RSI(14) reversion | reversion | 57.33 | -42.67 | 761 | 27.2 | -74.30 | -16.57 | -74.90 | 1612 |
| 66 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.23 | -19.77 | -74.04 | 1284 |
| 67 | Squeeze breakout | breakout | 56.22 | -43.78 | 522 | 14.2 | -67.08 | -23.35 | -67.94 | 1209 |
| 68 | EMA 20/50 cross | trend | 55.39 | -44.61 | 573 | 20.4 | -78.89 | -19.61 | -80.87 | 1439 |
| 69 | VWAP reversion | reversion | 54.37 | -45.63 | 765 | 26.0 | -70.67 | -14.15 | -72.15 | 1464 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.75 | -31.70 | -98.80 | 5276 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.07 | -35.30 | -94.28 | 2603 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.86 | -23.73 | -88.67 | 1895 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.18 | -28.38 | -91.74 | 2365 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.48 | -26.68 | -91.50 | 2280 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -35.48 | -97.81 | 3507 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.96 | -39.20 | -97.00 | 3575 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.55 | -28.50 | -94.73 | 2569 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.02 | -28.28 | -83.52 | 1736 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -37.35 | -99.38 | 5717 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.02 | -29.12 | -92.66 | 2627 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.89 | -32.32 | -95.89 | 3479 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -43.62 | -99.77 | 6162 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.74 | -30.92 | -91.89 | 2336 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -41.01 | -97.81 | 3640 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.88 | -98.50 | 4700 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.23 | -36.27 | -94.45 | 2808 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.48 | -28.75 | -84.44 | 1806 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.64 | -99.54 | 6180 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.88 | -22.90 | -87.01 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.89 | -26.98 | -88.05 | 2129 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.97 | -33.78 | -95.97 | 3761 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.48 | -34.63 | -89.51 | 2099 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -34.55 | -95.82 | 4078 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.58 | -99.91 | 8306 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T21:50 | Donchian 55/20 | sell | XRP-USD | 14.06 | 0.03 | exit signal |
| 2026-10-21T21:35 | RSI(14) reversion | sell | ETH-USD | 14.30 | -0.04 | exit signal |
| 2026-10-21T21:35 | Squeeze breakout | buy | ETH-USD | 14.07 | — | entry signal |
| 2026-10-21T20:55 | EMA 20/50 cross | sell | SOL-USD | 13.78 | -0.11 | exit signal |
| 2026-10-21T20:40 | EMA 20/50 cross | buy | SOL-USD | 13.89 | — | entry signal |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | buy | XRP-USD | 11.75 | — | rebalance up |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | sell | SOL-USD | 4.52 | 0.06 | exit signal |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | sell | ETH-USD | 4.51 | 0.03 | exit signal |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 3.37 | -0.04 | exit signal |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | sell | BTC-USD | 3.27 | 0.03 | exit signal |
| 2026-10-21T20:00 | Three white soldiers | sell | BTC-USD | 20.50 | -0.15 | exit signal |
| 2026-10-21T19:55 | Day trade: Stocks in Play ORB | sell | PLTR | 25.41 | 0.74 | target is flat |
| 2026-10-21T19:55 | Day trade: Stocks in Play ORB | sell | AMD | 24.75 | -0.02 | target is flat |
| 2026-10-21T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 98.30 | -0.10 | target is flat |
| 2026-10-21T19:55 | Agent (ML meta-label) | sell | ETHU | 9.40 | -0.02 | selected signal exited |
| 2026-10-21T19:55 | Agent (aggressive) | sell | TSLA | 43.60 | -0.19 | selected signal exited |
| 2026-10-21T19:55 | Agent | sell | TSLA | 18.05 | -0.08 | selected signal exited |
| 2026-10-21T19:55 | Agent | sell | ETHU | 18.21 | 0.10 | selected signal exited |
| 2026-10-21T19:55 | MFI reversion · 1h | sell | GOOGL | 21.36 | 0.07 | target is flat |
| 2026-10-21T19:55 | VWAP reversion | sell | TNA | 13.66 | 0.12 | end-of-day flatten |
| 2026-10-21T19:55 | VWAP reversion | sell | LABU | 13.58 | 0.04 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | buy | ETH-USD | 6.18 | — | rebalance up |
| 2026-10-21T19:55 | RSI(14) reversion | sell | TNA | 9.56 | -0.01 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | sell | META | 9.53 | -0.04 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | sell | IWM | 8.19 | 0.02 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | sell | ETHU | 9.57 | 0.00 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | sell | AMZN | 8.20 | 0.04 | end-of-day flatten |
| 2026-10-21T19:55 | Squeeze breakout | sell | PLTR | 14.08 | 0.02 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | UPRO | 8.54 | 0.04 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | TQQQ | 8.55 | 0.09 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | TECL | 8.59 | 0.07 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | SPY | 8.53 | 0.01 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | QQQ | 8.52 | 0.03 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | PLTR | 8.60 | 0.16 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | MSTR | 8.51 | 0.30 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | ETHU | 8.39 | 0.09 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | COIN | 8.47 | 0.01 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | BITX | 8.50 | 0.09 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | AAPL | 8.50 | -0.02 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 15m | sell | UPRO | 5.21 | 0.01 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 21:51:05.000136+00:00 -> 2026-10-21 22:01:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
