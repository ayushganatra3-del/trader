# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T19:50:05.000148+00:00 · 31044 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.72 (-9.28%)

Closed trades 91, win rate 40.7%, fees £3.01, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.20 | +0.09 |
| TSLA | 18.11 | -0.02 |

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

### Market regime (QQQ, 2026-10-20)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.22 · VIX 17.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 37158 decisions in 2895 calls, $0.4564 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T19:50 | 6 / 16 / 8 | cash |  |
| Breezy | 2026-10-21T19:50 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-21T19:50 | 9 / 18 / 3 | MSTR 72% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.27 | 6.27 | 0 | — | 8.35 | 3.86 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | Max aggression: 5-day momentum | meta | 102.95 | 2.95 | 10 | 50.0 | -6.06 | -0.22 | -34.64 | 26 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.86 | 0.86 | 4 | 50.0 | 9.51 | 1.97 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold BTC | benchmark | 99.92 | -0.08 | 0 | — | 16.05 | 2.29 | -8.68 | 1 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.78 | -0.22 | 0 | — | 1.99 | 0.91 | -5.02 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.59 | -0.41 | 63 | 34.9 | 2.99 | 1.71 | -2.29 | 65 |
| 13 | Hold SPY | benchmark | 99.53 | -0.47 | 0 | — | 1.11 | 0.68 | -3.13 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.57 | -1.43 | 11 | 27.3 | -3.35 | -3.62 | -4.04 | 21 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.56 | -2.44 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.23 | -2.77 | 0 | — | -3.90 | -1.48 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.18 | -1.81 | -5.83 | 1 |
| 18 | Copy: Insider buying | copy | 96.43 | -3.57 | 25 | 40.0 | -11.64 | -1.99 | -20.62 | 72 |
| 19 | Donchian 55/20 · 1h | breakout | 96.40 | -3.60 | 41 | 17.1 | -14.14 | -2.86 | -16.00 | 103 |
| 20 | ADX DI cross · 1h | trend | 95.85 | -4.15 | 91 | 19.8 | -12.13 | -2.22 | -16.15 | 262 |
| 21 | Agent (rotation) | meta | 95.83 | -4.17 | 117 | 30.8 | -6.84 | -3.65 | -8.43 | 255 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 95.23 | -4.77 | 6 | 16.7 | -9.09 | -1.33 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.91 | -5.09 | 92 | 23.9 | -20.38 | -6.35 | -20.58 | 129 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.25 | 1.94 | -7.13 | 201 |
| 26 | Opening range 30m | breakout | 93.83 | -6.17 | 225 | 32.4 | -10.70 | -3.01 | -17.26 | 568 |
| 27 | Parabolic SAR · 1h | trend | 93.62 | -6.38 | 108 | 23.1 | -15.60 | -3.40 | -19.79 | 272 |
| 28 | Squeeze breakout · 1h | breakout | 93.43 | -6.57 | 46 | 21.7 | -1.66 | -0.31 | -11.48 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 93.23 | -6.77 | 0 | — | 0.25 | 0.20 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.56 | -7.44 | 88 | 30.7 | -9.24 | -1.62 | -15.46 | 263 |
| 31 | Daily: Bullish score | daily | 92.33 | -7.67 | 8 | 0.0 | -2.39 | -0.14 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.44 | -1.97 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 91.05 | -8.95 | 92 | 23.9 | -12.40 | -2.20 | -14.13 | 113 |
| 34 | Agent | meta | 90.72 | -9.28 | 91 | 40.7 | -15.04 | -7.18 | -20.36 | 252 |
| 35 | Supertrend · 1h | trend | 90.51 | -9.49 | 88 | 12.5 | -20.55 | -4.06 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 90.07 | -9.94 | 84 | 16.7 | -19.49 | -3.88 | -21.28 | 222 |
| 37 | Connors RSI(2) · 1h | reversion | 89.85 | -10.15 | 159 | 42.1 | -22.01 | -6.55 | -23.74 | 194 |
| 38 | Stochastic reversion · 1h | reversion | 89.45 | -10.55 | 169 | 47.3 | -13.74 | -2.25 | -22.24 | 363 |
| 39 | EMA 20/50 cross · 1h | trend | 89.05 | -10.95 | 62 | 12.9 | -20.78 | -3.57 | -23.61 | 140 |
| 40 | Opening range 15m | breakout | 88.43 | -11.57 | 277 | 28.5 | -15.30 | -4.12 | -19.06 | 704 |
| 41 | Keltner breakout · 1h | breakout | 88.28 | -11.72 | 62 | 24.2 | -16.94 | -3.11 | -24.52 | 204 |
| 42 | MACD cross · 1h | trend | 87.90 | -12.10 | 199 | 21.1 | -23.45 | -4.40 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.54 | -12.46 | 45 | 35.6 | -13.54 | -4.00 | -18.93 | 125 |
| 44 | Ichimoku · 1h | trend | 87.21 | -12.79 | 60 | 13.3 | -17.59 | -3.28 | -20.25 | 118 |
| 45 | Z-score reversion · 1h | reversion | 86.90 | -13.10 | 102 | 34.3 | -11.39 | -1.76 | -21.32 | 196 |
| 46 | Donchian 20/10 · 1h | breakout | 86.37 | -13.63 | 83 | 19.3 | -19.55 | -3.58 | -29.00 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.83 | -14.17 | 92 | 15.2 | -27.82 | -5.11 | -28.48 | 224 |
| 48 | MFI reversion · 1h | reversion | 85.21 | -14.79 | 228 | 32.9 | -14.51 | -2.20 | -21.11 | 140 |
| 49 | Agent (ML meta-label) | meta | 84.84 | -15.15 | 734 | 20.2 | -11.44 | -1.90 | -16.15 | 349 |
| 50 | MACD zero-line · 1h | trend | 84.75 | -15.25 | 92 | 15.2 | -23.18 | -4.49 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 84.30 | -15.70 | 188 | 17.6 | -31.22 | -5.87 | -32.08 | 309 |
| 52 | ROC + volume · 1h | momentum | 83.32 | -16.68 | 213 | 23.5 | -26.51 | -4.77 | -33.07 | 390 |
| 53 | Bollinger reversion · 1h | reversion | 82.61 | -17.39 | 163 | 36.2 | -29.10 | -5.61 | -32.84 | 348 |
| 54 | Three white soldiers | momentum | 82.50 | -17.50 | 258 | 20.5 | -45.64 | -18.11 | -46.47 | 606 |
| 55 | Williams %R · 1h | reversion | 82.50 | -17.50 | 199 | 44.7 | -31.63 | -4.91 | -36.64 | 517 |
| 56 | CCI reversion · 1h | reversion | 82.14 | -17.86 | 188 | 43.6 | -20.27 | -2.63 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.73 | -18.27 | 246 | 22.8 | -43.30 | -9.23 | -46.38 | 679 |
| 58 | EMA 9/21 cross · 1h | trend | 81.15 | -18.85 | 143 | 10.5 | -26.67 | -5.13 | -29.95 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 81.04 | -18.96 | 85 | 24.7 | -17.03 | -2.92 | -24.99 | 172 |
| 60 | VWAP momentum · 1h | momentum | 79.40 | -20.59 | 478 | 21.3 | -46.28 | -8.73 | -52.79 | 1247 |
| 61 | Candlestick reversal · 1h | reversion | 78.98 | -21.02 | 231 | 30.3 | -38.45 | -7.08 | -41.73 | 536 |
| 62 | Max aggression: 1-day momentum | meta | 77.86 | -22.14 | 17 | 29.4 | -33.63 | -2.09 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.88 | -40.12 | 678 | 23.3 | -77.62 | -21.74 | -78.91 | 1710 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -65.07 | -20.29 | -65.31 | 874 |
| 65 | RSI(14) reversion | reversion | 57.40 | -42.60 | 755 | 27.0 | -73.97 | -16.08 | -74.92 | 1613 |
| 66 | Donchian 55/20 | breakout | 56.72 | -43.28 | 532 | 19.5 | -72.08 | -19.38 | -74.04 | 1287 |
| 67 | Squeeze breakout | breakout | 56.36 | -43.64 | 521 | 14.0 | -66.87 | -22.65 | -67.87 | 1210 |
| 68 | EMA 20/50 cross | trend | 55.71 | -44.29 | 566 | 19.6 | -78.79 | -19.23 | -80.87 | 1439 |
| 69 | VWAP reversion | reversion | 54.46 | -45.54 | 763 | 25.8 | -70.55 | -13.90 | -72.15 | 1465 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.76 | -30.99 | -98.80 | 5284 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.98 | -33.84 | -94.27 | 2606 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.60 | -22.39 | -88.67 | 1899 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.94 | -26.68 | -91.71 | 2362 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.43 | -26.20 | -91.51 | 2285 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -34.22 | -97.79 | 3507 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.92 | -37.89 | -96.99 | 3579 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.56 | -27.80 | -94.74 | 2571 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.98 | -27.68 | -83.48 | 1735 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -35.99 | -99.38 | 5718 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.98 | -28.45 | -92.66 | 2630 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.89 | -31.51 | -95.89 | 3481 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.35 | -99.76 | 6164 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.65 | -29.45 | -91.89 | 2339 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -39.45 | -97.81 | 3648 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.44 | -98.49 | 4706 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.25 | -35.45 | -94.45 | 2811 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.50 | -28.15 | -84.44 | 1810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.20 | -99.54 | 6185 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.84 | -22.46 | -87.01 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.80 | -26.21 | -88.05 | 2125 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.96 | -32.85 | -95.97 | 3764 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.38 | -33.37 | -89.50 | 2099 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.79 | -33.62 | -95.81 | 4081 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.72 | -99.91 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T19:50 | Agent (ML meta-label) | buy | AMZN | 9.43 | — | entry |
| 2026-10-21T19:50 | RSI(14) reversion | buy | TNA | 9.57 | — | entry |
| 2026-10-21T19:50 | RSI(14) reversion | buy | META | 9.57 | — | entry |
| 2026-10-21T19:50 | RSI(14) reversion | buy | ETHU | 9.57 | — | entry |
| 2026-10-21T19:50 | RSI(14) reversion | sell | UPRO | 8.23 | 0.06 | take-profit |
| 2026-10-21T19:50 | RSI(14) reversion | sell | TQQQ | 8.25 | 0.09 | take-profit |
| 2026-10-21T19:50 | RSI(14) reversion | sell | SPY | 8.19 | 0.02 | take-profit |
| 2026-10-21T19:50 | RSI(14) reversion | sell | QQQ | 8.19 | 0.03 | take-profit |
| 2026-10-21T19:45 | Ichimoku · 1h | buy | COIN | 4.36 | — | rebalance up |
| 2026-10-21T19:45 | Ichimoku · 1h | sell | LABU | 4.36 | 0.01 | rebalance down |
| 2026-10-21T19:40 | Agent (ML meta-label) | sell | AMZN | 8.47 | -0.02 | selected signal exited |
| 2026-10-21T19:40 | Three white soldiers | buy | BTC-USD | 20.65 | — | entry signal |
| 2026-10-21T19:40 | Three white soldiers | sell | AMZN | 20.61 | -0.05 | exit signal |
| 2026-10-21T19:35 | Agent (ML meta-label) | buy | ETHU | 9.42 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T19:35 | EMA 20/50 cross | buy | MSFT | 2.88 | — | rebalance up |
| 2026-10-21T19:35 | EMA 20/50 cross | sell | ETH-USD | 5.08 | 0.06 | exit signal |
| 2026-10-21T19:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | TQQQ | 98.40 | — | entry |
| 2026-10-21T19:30 | CCI reversion · 1h | buy | GOOGL | 20.53 | — | entry signal |
| 2026-10-21T19:30 | Stochastic reversion · 1h | buy | SQQQ | 22.37 | — | entry signal |
| 2026-10-21T19:30 | Connors RSI(2) · 1h | sell | SQQQ | 22.35 | -0.15 | exit signal |
| 2026-10-21T19:30 | Candlestick reversal · 1h | buy | GOOGL | 19.75 | — | entry signal |
| 2026-10-21T19:30 | Candlestick reversal · 1h | sell | PLTR | 19.81 | 0.27 | exit signal |
| 2026-10-21T19:30 | OBV trend · 1h | buy | TNA | 2.32 | — | entry signal |
| 2026-10-21T19:30 | OBV trend · 1h | buy | MSTR | 7.67 | — | entry signal |
| 2026-10-21T19:30 | OBV trend · 1h | buy | IWM | 7.67 | — | entry |
| 2026-10-21T19:30 | OBV trend · 1h | sell | TSLA | 4.43 | 0.03 | rebalance down |
| 2026-10-21T19:30 | OBV trend · 1h | sell | SOL-USD | 4.39 | 0.04 | rebalance down |
| 2026-10-21T19:30 | OBV trend · 1h | sell | BTC-USD | 4.43 | 0.04 | rebalance down |
| 2026-10-21T19:30 | OBV trend · 1h | sell | AAPL | 4.40 | -0.01 | rebalance down |
| 2026-10-21T19:30 | ROC + volume · 1h | buy | META | 4.17 | — | entry |
| 2026-10-21T19:30 | ROC + volume · 1h | sell | AMZN | 3.96 | -0.02 | exit signal |
| 2026-10-21T19:30 | VWAP momentum · 1h | buy | UPRO | 1.70 | — | entry |
| 2026-10-21T19:30 | VWAP momentum · 1h | buy | TSLA | 3.78 | — | entry |
| 2026-10-21T19:30 | VWAP momentum · 1h | buy | GOOGL | 3.78 | — | entry |
| 2026-10-21T19:30 | VWAP momentum · 1h | sell | TNA | 2.20 | -0.01 | exit signal |
| 2026-10-21T19:30 | VWAP momentum · 1h | sell | IWM | 3.45 | -0.00 | exit signal |
| 2026-10-21T19:30 | VWAP momentum · 1h | sell | AMZN | 3.60 | 0.00 | exit signal |
| 2026-10-21T19:30 | Heikin-Ashi · 1h | buy | TSLA | 5.21 | — | rebalance up |
| 2026-10-21T19:30 | Heikin-Ashi · 1h | buy | PLTR | 6.28 | — | entry |
| 2026-10-21T19:30 | Heikin-Ashi · 1h | sell | TQQQ | 4.56 | 0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 19:50:05.000148+00:00 -> 2026-10-21 20:00:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
