# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T20:25:05.000132+00:00 · 64804 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.83 (-15.17%)

Closed trades 224, win rate 36.2%, fees £6.17, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 16.92 | -0.05 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-18 | PEPG 12%, FUN 12%, STWD 12%, LRN 12%, PSEC 12%, TEAM 12%, BH 12%, LILA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-17)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 34.44 · VIX 25.46 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 6.1, AMZN 4.3, TSLA 2.4, META 1.9, AMD 1.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 36051 decisions in 3126 calls, $0.4481 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T20:25 | 4 / 8 / 17 | cash |  |
| Breezy | 2026-11-18T20:25 | 0 / 19 / 10 | cash |  |
| Boozy | 2026-11-18T20:25 | 4 / 22 / 3 | COIN 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| OBV trend | SQQQ | 1.82 | +5.85% | 9 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.55 | 14.55 | 0 | — | 13.14 | 4.35 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.72 | 3.82 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.80 | 3.80 | 0 | — | 4.50 | 1.30 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.00 | 0.00 | 150 | 34.7 | -3.35 | -2.94 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.34 | 1.14 | -9.06 | 207 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.65 | -4.35 | 8 | 50.0 | -4.32 | -0.17 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.56 | -4.44 | 0 | — | -3.93 | -1.29 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.26 | -1.50 | -8.79 | 153 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.95 | -7.93 | -5.54 | 20 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.45 | -7.55 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.16 | -8.84 | 0 | — | -7.51 | -2.02 | -12.67 | 1 |
| 18 | Trend pullback · 1h | trend | 90.39 | -9.61 | 113 | 23.9 | -15.05 | -7.32 | -15.58 | 61 |
| 19 | Copy: Insider buying | copy | 90.33 | -9.68 | 52 | 40.4 | -10.14 | -2.04 | -14.79 | 64 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.88 | -3.79 | -18.48 | 150 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.24 | -12.76 | 17 | 17.6 | -7.16 | -1.33 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.08 | -9.17 | -18.13 | 72 |
| 24 | Agent | meta | 84.83 | -15.17 | 224 | 36.2 | -14.50 | -6.79 | -16.41 | 204 |
| 25 | Opening range 30m | breakout | 84.53 | -15.46 | 443 | 33.4 | -12.44 | -4.16 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 83.21 | -16.79 | 104 | 33.7 | -15.81 | -4.22 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.51 | -18.49 | 188 | 28.2 | -24.26 | -6.69 | -27.22 | 197 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.36 | -6.39 | -14.68 | 86 |
| 29 | Keltner breakout · 1h | breakout | 79.93 | -20.07 | 124 | 25.8 | -23.38 | -6.43 | -25.90 | 148 |
| 30 | Max aggression: 5-day momentum | meta | 79.84 | -20.16 | 21 | 42.9 | -47.51 | -3.15 | -55.24 | 21 |
| 31 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.12 | -5.22 | -21.21 | 73 |
| 32 | Donchian 55/20 · 1h | breakout | 78.78 | -21.22 | 78 | 12.8 | -25.68 | -6.74 | -30.57 | 84 |
| 33 | Opening range 15m | breakout | 77.27 | -22.73 | 537 | 31.5 | -20.30 | -6.03 | -21.81 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.14 | -22.86 | 2 | 0.0 | -18.77 | -2.55 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.23 | -24.77 | 209 | 19.1 | -26.53 | -4.32 | -34.88 | 266 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 37 | Hold BTC | benchmark | 73.27 | -26.73 | 2 | 0.0 | -18.59 | -2.60 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.65 | -8.30 | -33.72 | 216 |
| 39 | Stochastic reversion · 1h | reversion | 72.62 | -27.39 | 351 | 42.5 | -34.90 | -5.32 | -35.78 | 424 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -40.26 | -2.48 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.66 | -28.34 | 191 | 16.2 | -32.53 | -5.40 | -39.71 | 200 |
| 42 | Triple EMA stack · 1h | trend | 70.80 | -29.20 | 157 | 14.6 | -30.69 | -6.22 | -37.70 | 171 |
| 43 | RSI momentum · 1h | momentum | 70.41 | -29.59 | 179 | 14.5 | -31.41 | -5.70 | -38.37 | 198 |
| 44 | MFI reversion · 1h | reversion | 70.33 | -29.67 | 451 | 33.5 | -27.43 | -4.09 | -30.08 | 173 |
| 45 | MACD zero-line · 1h | trend | 69.73 | -30.27 | 184 | 17.9 | -28.20 | -5.63 | -34.28 | 203 |
| 46 | Heikin-Ashi · 1h | trend | 69.56 | -30.44 | 474 | 23.0 | -44.65 | -9.82 | -45.85 | 630 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.36 | -30.64 | 116 | 10.3 | -36.79 | -9.37 | -40.78 | 118 |
| 49 | ROC + volume · 1h | momentum | 68.72 | -31.28 | 413 | 28.1 | -34.12 | -6.24 | -39.51 | 342 |
| 50 | OBV trend · 1h | momentum | 68.38 | -31.62 | 310 | 19.4 | -34.28 | -7.27 | -39.87 | 249 |
| 51 | MACD cross · 1h | trend | 67.28 | -32.72 | 417 | 22.3 | -41.36 | -6.75 | -46.93 | 490 |
| 52 | CCI reversion · 1h | reversion | 66.92 | -33.08 | 387 | 41.6 | -42.37 | -7.12 | -44.29 | 472 |
| 53 | Donchian 20/10 · 1h | breakout | 66.69 | -33.31 | 162 | 17.9 | -35.68 | -6.89 | -41.19 | 194 |
| 54 | Bollinger reversion · 1h | reversion | 63.54 | -36.46 | 348 | 37.9 | -39.10 | -5.98 | -39.61 | 417 |
| 55 | Williams %R · 1h | reversion | 63.32 | -36.68 | 437 | 40.7 | -46.80 | -8.17 | -47.31 | 566 |
| 56 | EMA 9/21 cross · 1h | trend | 62.84 | -37.16 | 285 | 11.6 | -39.60 | -7.77 | -45.66 | 321 |
| 57 | Agent (ML meta-label) | meta | 59.78 | -40.22 | 1946 | 24.6 | -22.92 | -3.94 | -24.30 | 306 |
| 58 | RSI(14) reversion · 1h | reversion | 58.70 | -41.30 | 206 | 32.0 | -40.68 | -6.00 | -43.22 | 257 |
| 59 | Z-score reversion · 1h | reversion | 57.34 | -42.66 | 227 | 35.2 | -36.99 | -5.12 | -39.53 | 257 |
| 60 | VWAP momentum · 1h | momentum | 54.96 | -45.04 | 983 | 21.6 | -56.53 | -11.06 | -60.30 | 1203 |
| 61 | Candlestick reversal · 1h | reversion | 54.92 | -45.08 | 552 | 26.4 | -48.11 | -8.90 | -48.97 | 637 |
| 62 | Three white soldiers | momentum | 54.64 | -45.36 | 589 | 14.4 | -49.73 | -22.00 | -50.82 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -42.55 | -99.04 | 5284 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.49 | -25.18 | -82.59 | 1409 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.74 | -41.98 | -94.02 | 2458 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.90 | -30.51 | -90.40 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.04 | -37.78 | -91.50 | 2302 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.96 | -30.56 | -90.11 | 2072 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -46.51 | -97.94 | 3469 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -52.85 | -96.43 | 3383 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.32 | -37.79 | -93.32 | 2189 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.56 | -34.50 | -82.85 | 1587 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -55.17 | -99.61 | 6100 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.94 | -43.18 | -92.17 | 2547 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.79 | -39.00 | -94.80 | 3225 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.90 | -99.81 | 6195 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.39 | -42.24 | -92.67 | 2264 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.01 | -27.18 | -76.40 | 1635 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -61.60 | -97.73 | 3434 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.52 | -99.07 | 4970 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.22 | -28.64 | -70.13 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -55.68 | -94.67 | 2750 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -37.60 | -85.19 | 1730 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.62 | -99.70 | 6399 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.83 | -31.29 | -91.03 | 2363 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.11 | -19.10 | -80.52 | 1843 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.53 | -37.14 | -91.55 | 2149 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.61 | -46.77 | -97.61 | 3917 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.24 | -58.08 | -89.42 | 2164 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.19 | -30.98 | -66.92 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.73 | -24.18 | -73.12 | 1217 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.81 | -18.38 | -81.96 | 1766 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -46.48 | -97.59 | 4333 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -116.08 | -99.94 | 8450 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T20:25 | MFI reversion · 1h | buy | TQQQ | 3.26 | — | rebalance up |
| 2026-11-18T20:25 | MFI reversion · 1h | buy | TECL | 5.86 | — | entry |
| 2026-11-18T20:25 | MFI reversion · 1h | buy | MSTR | 5.86 | — | entry |
| 2026-11-18T20:25 | MFI reversion · 1h | sell | SPY | 7.06 | -0.03 | target is flat |
| 2026-11-18T20:25 | MFI reversion · 1h | sell | AMD | 7.15 | 0.12 | target is flat |
| 2026-11-18T20:15 | Agent | sell | TSLA | 17.05 | 0.04 | selected signal exited |
| 2026-11-18T20:05 | Agent (ML meta-label) | buy | TQQQ | 3.40 | — | rebalance up |
| 2026-11-18T20:05 | Agent (ML meta-label) | buy | SQQQ | 3.27 | — | rebalance up |
| 2026-11-18T20:05 | Agent (ML meta-label) | buy | SOXL | 3.47 | — | rebalance up |
| 2026-11-18T20:05 | Agent (ML meta-label) | buy | NVDA | 9.99 | — | entry |
| 2026-11-18T20:05 | Agent (ML meta-label) | buy | LABU | 3.43 | — | rebalance up |
| 2026-11-18T20:05 | Agent (ML meta-label) | buy | AMD | 3.17 | — | rebalance up |
| 2026-11-18T20:05 | Agent (ML meta-label) | sell | TSLA | 6.67 | 0.01 | selected signal exited |
| 2026-11-18T20:05 | Agent (ML meta-label) | sell | TNA | 5.94 | -0.10 | selected signal exited |
| 2026-11-18T20:05 | Agent (ML meta-label) | sell | SPY | 6.65 | -0.00 | selected signal exited |
| 2026-11-18T20:05 | Agent (ML meta-label) | sell | AAPL | 6.27 | -0.01 | selected signal exited |
| 2026-11-18T20:00 | Agent (ML meta-label) | buy | SPY | 6.65 | — | following Squeeze breakout |
| 2026-11-18T20:00 | Agent (ML meta-label) | sell | TECL | 4.53 | 0.00 | selected signal exited |
| 2026-11-18T20:00 | Agent (ML meta-label) | sell | GOOGL | 3.32 | -0.00 | selected signal exited |
| 2026-11-18T20:00 | MFI reversion · 1h | buy | META | 5.03 | — | entry |
| 2026-11-18T20:00 | MFI reversion · 1h | sell | TNA | 5.81 | -0.08 | target is flat |
| 2026-11-18T20:00 | VWAP momentum · 1h | buy | TQQQ | 3.63 | — | rebalance up |
| 2026-11-18T20:00 | VWAP momentum · 1h | buy | TECL | 3.66 | — | rebalance up |
| 2026-11-18T20:00 | VWAP momentum · 1h | buy | SPY | 3.60 | — | rebalance up |
| 2026-11-18T20:00 | VWAP momentum · 1h | buy | QQQ | 3.61 | — | rebalance up |
| 2026-11-18T20:00 | VWAP momentum · 1h | buy | MSFT | 3.70 | — | rebalance up |
| 2026-11-18T20:00 | VWAP momentum · 1h | buy | GOOGL | 3.57 | — | rebalance up |
| 2026-11-18T20:00 | VWAP momentum · 1h | buy | AMD | 3.58 | — | rebalance up |
| 2026-11-18T20:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.82 | -0.09 | exit signal |
| 2026-11-18T20:00 | Triple EMA stack · 1h | sell | XRP-USD | 17.64 | -0.16 | exit signal |
| 2026-11-18T20:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 15.66 | 0.01 | exit signal |
| 2026-11-18T19:55 | Agent (ML meta-label) | buy | GOOGL | 3.33 | — | entry |
| 2026-11-18T19:55 | Agent (ML meta-label) | sell | SPY | 3.33 | -0.00 | selected signal exited |
| 2026-11-18T19:50 | Agent (ML meta-label) | buy | TECL | 4.53 | — | entry |
| 2026-11-18T19:50 | Agent (ML meta-label) | buy | AAPL | 6.28 | — | entry |
| 2026-11-18T19:50 | Agent (ML meta-label) | sell | SPY | 4.15 | -0.00 | rebalance down |
| 2026-11-18T19:46 | Agent (ML meta-label) | buy | SPY | 5.40 | — | rebalance up |
| 2026-11-18T19:46 | Agent (ML meta-label) | sell | TECL | 6.62 | -0.03 | selected signal exited |
| 2026-11-18T19:46 | Agent (ML meta-label) | sell | AAPL | 5.43 | -0.02 | selected signal exited |
| 2026-11-18T19:40 | Agent (ML meta-label) | buy | SPY | 2.09 | — | following Squeeze breakout |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 20:25:05.000132+00:00 -> 2026-11-18 20:35:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 20:25:05.000132+00:00 -> 2026-11-18 20:35:05.000132+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
