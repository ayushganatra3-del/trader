# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T14:45:05.000137+00:00 · 70691 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £80.45 (-19.55%)

Closed trades 238, win rate 36.1%, fees £6.47, max drawdown -20.20%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 32.17 | +0.27 |

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

Today: 11168 decisions in 2239 calls, $0.1560 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T14:45 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-23T14:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T14:45 | 4 / 1 / 0 | ETH-USD 61% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.58 | 14.58 | 0 | — | 12.16 | 4.58 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.90 | 11.89 | 40 | 30.0 | 13.49 | 2.13 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.44 | 1.36 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 102.97 | 2.97 | 0 | — | 1.88 | 0.60 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.19 | 0.19 | 204 | 31.9 | 0.43 | 0.22 | -8.71 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent (rotation) | meta | 98.43 | -1.57 | 213 | 29.1 | 1.73 | 0.67 | -7.48 | 146 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.22 | -1.78 | 163 | 33.7 | -3.29 | -3.36 | -3.99 | 64 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.17 | -3.10 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.49 | -5.51 | 0 | — | -7.27 | -1.95 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | VWAP reversion · 1h | reversion | 92.33 | -7.67 | 161 | 45.3 | -4.79 | -0.60 | -20.49 | 156 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 16 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.56 | -3.47 | -8.72 | 31 |
| 17 | Copy: Insider buying | copy | 88.32 | -11.68 | 56 | 39.3 | -19.53 | -3.89 | -22.56 | 68 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 87.63 | -12.37 | 0 | — | -12.95 | -3.18 | -13.87 | 1 |
| 19 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -11.89 | -3.97 | -14.52 | 531 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.69 | -3.21 | -20.94 | 1 |
| 21 | Daily: Bullish score | daily | 86.63 | -13.37 | 19 | 15.8 | -15.94 | -3.68 | -19.56 | 14 |
| 22 | Copy: Congress Democrats (NANC) | copy | 86.03 | -13.97 | 0 | — | -14.84 | -3.97 | -17.03 | 1 |
| 23 | Squeeze breakout · 1h | breakout | 85.26 | -14.74 | 71 | 19.7 | -16.25 | -6.72 | -17.05 | 74 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 84.60 | -15.40 | 9 | 44.4 | -12.82 | -0.81 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 83.34 | -16.66 | 198 | 27.3 | -24.62 | -6.69 | -29.75 | 186 |
| 26 | Agent | meta | 80.45 | -19.55 | 238 | 36.1 | -24.10 | -5.46 | -24.36 | 200 |
| 27 | Donchian 55/20 · 1h | breakout | 80.20 | -19.80 | 79 | 12.7 | -26.06 | -7.16 | -29.11 | 85 |
| 28 | Connors RSI(2) · 1h | reversion | 80.08 | -19.92 | 218 | 40.4 | -14.07 | -6.21 | -14.37 | 67 |
| 29 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -23.68 | -4.02 | -24.18 | 93 |
| 30 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.72 | -6.69 | -23.54 | 650 |
| 31 | Volume breakout · 1h | breakout | 77.37 | -22.63 | 164 | 28.7 | -20.56 | -7.97 | -20.74 | 72 |
| 32 | Ichimoku · 1h | trend | 76.90 | -23.10 | 109 | 13.8 | -25.71 | -6.86 | -30.74 | 108 |
| 33 | Keltner breakout · 1h | breakout | 76.84 | -23.16 | 129 | 25.6 | -24.98 | -7.02 | -25.41 | 146 |
| 34 | Supertrend · 1h | trend | 73.44 | -26.56 | 198 | 16.7 | -32.62 | -6.05 | -39.05 | 199 |
| 35 | Hold BTC | benchmark | 73.38 | -26.62 | 3 | 0.0 | -27.10 | -4.59 | -36.21 | 1 |
| 36 | Triple EMA stack · 1h | trend | 72.68 | -27.32 | 161 | 14.3 | -33.27 | -8.21 | -38.25 | 163 |
| 37 | EMA 20/50 cross · 1h | trend | 72.37 | -27.63 | 119 | 10.1 | -34.05 | -9.14 | -39.77 | 123 |
| 38 | ADX DI cross · 1h | trend | 71.80 | -28.20 | 234 | 20.1 | -32.67 | -6.09 | -35.49 | 270 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 40 | Bollinger breakout · 1h | breakout | 69.91 | -30.09 | 202 | 20.8 | -32.54 | -8.54 | -34.86 | 213 |
| 41 | Daily: Momentum burst | daily | 69.70 | -30.30 | 30 | 13.3 | -36.90 | -5.22 | -37.74 | 25 |
| 42 | OBV trend · 1h | momentum | 69.68 | -30.32 | 318 | 19.5 | -36.07 | -9.29 | -40.43 | 232 |
| 43 | Max aggression: 5-day momentum | meta | 68.41 | -31.59 | 24 | 37.5 | -59.36 | -3.92 | -63.35 | 23 |
| 44 | RSI momentum · 1h | momentum | 68.12 | -31.88 | 187 | 13.9 | -35.45 | -7.70 | -39.47 | 201 |
| 45 | Stochastic reversion · 1h | reversion | 66.52 | -33.48 | 388 | 40.2 | -34.67 | -3.67 | -43.17 | 435 |
| 46 | Heikin-Ashi · 1h | trend | 66.50 | -33.50 | 500 | 23.2 | -46.67 | -9.88 | -46.80 | 614 |
| 47 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -35.20 | -9.52 | -35.53 | 209 |
| 48 | Donchian 20/10 · 1h | breakout | 65.22 | -34.78 | 171 | 17.0 | -37.48 | -8.07 | -40.76 | 194 |
| 49 | MFI reversion · 1h | reversion | 64.83 | -35.17 | 484 | 33.1 | -30.62 | -4.28 | -37.45 | 176 |
| 50 | ROC + volume · 1h | momentum | 63.80 | -36.20 | 437 | 27.2 | -40.52 | -8.34 | -40.64 | 337 |
| 51 | EMA 9/21 cross · 1h | trend | 62.46 | -37.53 | 298 | 11.1 | -42.81 | -9.81 | -45.93 | 328 |
| 52 | MACD cross · 1h | trend | 61.10 | -38.90 | 461 | 21.0 | -48.79 | -9.43 | -49.70 | 503 |
| 53 | Agent (ML meta-label) | meta | 59.81 | -40.19 | 2024 | 24.7 | -24.21 | -2.79 | -35.84 | 316 |
| 54 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -54.42 | -3.89 | -54.62 | 38 |
| 55 | CCI reversion · 1h | reversion | 59.00 | -41.00 | 429 | 40.1 | -48.69 | -8.00 | -52.15 | 483 |
| 56 | Bollinger reversion · 1h | reversion | 57.41 | -42.59 | 383 | 36.6 | -39.12 | -4.80 | -45.48 | 436 |
| 57 | VWAP momentum · 1h | momentum | 55.27 | -44.73 | 1031 | 21.6 | -57.44 | -12.99 | -59.34 | 1185 |
| 58 | Williams %R · 1h | reversion | 54.96 | -45.04 | 487 | 38.4 | -53.03 | -8.56 | -55.62 | 587 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -45.75 | -6.79 | -50.46 | 294 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -50.91 | -8.36 | -54.33 | 688 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -47.18 | -99.14 | 5311 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.95 | -32.70 | -84.60 | 1427 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.62 | -50.19 | -94.66 | 2433 |
| 64 | Three white soldiers | momentum | 50.43 | -49.57 | 636 | 14.3 | -52.23 | -22.49 | -52.23 | 653 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.73 | -30.46 | -91.12 | 1932 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.69 | -40.42 | -91.82 | 2253 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.18 | -27.49 | -89.40 | 1945 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.13 | -47.79 | -98.16 | 3434 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.04 | -53.27 | -97.06 | 3368 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -38.85 | -93.57 | 2171 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.46 | -35.58 | -83.62 | 1535 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -52.73 | -99.66 | 6287 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.04 | -40.35 | -93.07 | 2497 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.22 | -35.53 | -94.29 | 3108 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -61.79 | -99.83 | 6164 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.29 | -43.51 | -93.44 | 2267 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.91 | -24.45 | -79.12 | 1623 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -57.08 | -97.81 | 3299 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -55.79 | -99.17 | 5098 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.91 | -28.21 | -70.91 | 1210 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.92 | -48.58 | -94.96 | 2690 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -43.64 | -5.90 | -48.72 | 267 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.67 | -37.38 | -85.82 | 1681 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -68.36 | -99.76 | 6525 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.58 | -30.27 | -91.68 | 2487 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.92 | -19.65 | -82.99 | 1959 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.79 | -29.15 | -92.08 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.10 | -46.61 | -98.11 | 4058 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.05 | -45.77 | -90.21 | 2200 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.29 | -30.63 | -68.48 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.53 | -28.28 | -74.60 | 1173 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.67 | -18.78 | -83.75 | 1843 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.92 | -47.19 | -97.93 | 4435 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.46 | -99.94 | 8300 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T14:45 | Agent (rotation) | buy | LABU | 8.20 | — | entry |
| 2026-11-23T14:45 | Day trade: Stocks in Play ORB | sell | TSLA | 24.54 | -0.14 | target is flat |
| 2026-11-23T14:45 | Day trade: Stocks in Play ORB | sell | PLTR | 24.43 | -0.25 | target is flat |
| 2026-11-23T14:45 | Agent | buy | SQQQ | 15.87 | — | rebalance up |
| 2026-11-23T14:45 | Gap and go | buy | LABU | 25.05 | — | entry signal |
| 2026-11-23T14:40 | Agent (rotation) | buy | TSLA | 8.22 | — | entry |
| 2026-11-23T14:40 | Day trade: Stocks in Play ORB | buy | TSLA | 24.68 | — | entry |
| 2026-11-23T14:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 24.68 | — | entry |
| 2026-11-23T14:40 | Day trade: Stocks in Play ORB | buy | PLTR | 24.68 | — | entry |
| 2026-11-23T14:40 | Agent (ML meta-label) | buy | NVDA | 4.14 | — | rebalance up |
| 2026-11-23T14:40 | EMA 20/50 cross · 1h | buy | DOGE-USD | 3.72 | — | rebalance up |
| 2026-11-23T14:40 | EMA 20/50 cross · 1h | sell | SQQQ | 3.72 | 0.27 | rebalance down |
| 2026-11-23T14:40 | Gap and go | buy | TSLA | 25.08 | — | entry signal |
| 2026-11-23T14:35 | Max aggression: 5-day momentum | buy | SOL-USD | 68.98 | — | entry |
| 2026-11-23T14:35 | Max aggression: 1-day momentum | sell | SQQQ | 59.16 | -6.41 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T14:35 | Agent (rotation) | buy | SQQQ | 32.63 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 109.98 | — | entry |
| 2026-11-23T14:35 | Agent (ML meta-label) | buy | SOXL | 5.88 | — | entry |
| 2026-11-23T14:35 | Agent (ML meta-label) | buy | NVDA | 1.32 | — | entry |
| 2026-11-23T14:35 | Agent (ML meta-label) | sell | MSTR | 5.18 | 0.52 | selected signal exited |
| 2026-11-23T14:35 | Agent | buy | SQQQ | 16.04 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T14:35 | Daily: Connors RSI(2) · 3x ETFs | buy | UPRO | 85.09 | — | entry |
| 2026-11-23T14:35 | Daily: Momentum burst | buy | SQQQ | 17.35 | — | entry |
| 2026-11-23T14:35 | MFI reversion · 1h | buy | BITX | 16.22 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | TECL | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | SOXL | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | PLTR | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | NVDA | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | MSTR | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | MSFT | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | LABU | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | IWM | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | ETHU | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | BITX | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | AMZN | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | AMD | 5.15 | — | entry |
| 2026-11-23T14:35 | Stochastic reversion · 1h | buy | AAPL | 5.15 | — | entry |
| 2026-11-23T14:35 | VWAP reversion · 1h | buy | ETHU | 5.13 | — | rebalance up |
| 2026-11-23T14:35 | VWAP reversion · 1h | buy | BITX | 23.28 | — | entry |
| 2026-11-23T14:35 | VWAP reversion · 1h | buy | AMD | 7.53 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 14:45:05.000137+00:00 -> 2026-11-23 14:55:05.000137+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
