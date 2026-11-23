# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T15:45:05.000134+00:00 · 70728 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.58 (-21.42%)

Closed trades 238, win rate 36.1%, fees £6.48, max drawdown -21.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 15.87 | -0.74 |

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

Today: 14507 decisions in 2350 calls, $0.1946 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T15:45 | 1 / 10 / 19 | cash |  |
| Breezy | 2026-11-23T15:45 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-23T15:45 | 1 / 24 / 5 | COIN 69% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.44 | 15.44 | 0 | — | 13.56 | 4.55 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 8.02 | 1.45 | -9.74 | 35 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.51 | 4.51 | 0 | — | 2.51 | 0.74 | -6.60 | 0 |
| 6 | Gap and go | momentum | 101.38 | 1.38 | 205 | 31.7 | 1.56 | 0.57 | -8.71 | 210 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.81 | -3.57 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.61 | -3.39 | 215 | 28.8 | 0.38 | 0.21 | -7.48 | 156 |
| 11 | Hold SPY | benchmark | 95.67 | -4.33 | 0 | — | -6.35 | -1.57 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.13 | -3.07 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | VWAP reversion · 1h | reversion | 92.50 | -7.50 | 163 | 46.0 | -4.78 | -0.60 | -20.49 | 156 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.74 | -8.26 | 0 | — | -9.29 | -1.98 | -13.87 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 17 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.56 | -3.47 | -8.72 | 31 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.04 | -8.96 | 0 | — | -10.74 | -2.25 | -17.03 | 1 |
| 19 | Copy: Insider buying | copy | 89.56 | -10.44 | 57 | 40.4 | -18.31 | -3.57 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.58 | -3.18 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 87.27 | -12.73 | 9 | 44.4 | -10.21 | -0.50 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 87.24 | -12.76 | 452 | 33.6 | -12.08 | -4.04 | -14.52 | 540 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -17.83 | -3.98 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 84.38 | -15.62 | 75 | 20.0 | -15.98 | -6.40 | -16.80 | 74 |
| 25 | Parabolic SAR · 1h | trend | 81.99 | -18.01 | 199 | 27.1 | -25.95 | -7.15 | -29.75 | 191 |
| 26 | Connors RSI(2) · 1h | reversion | 80.50 | -19.50 | 219 | 40.6 | -13.60 | -5.88 | -14.31 | 66 |
| 27 | Donchian 55/20 · 1h | breakout | 79.43 | -20.57 | 80 | 12.5 | -26.52 | -7.58 | -28.72 | 84 |
| 28 | Agent | meta | 78.58 | -21.42 | 238 | 36.1 | -26.32 | -5.67 | -26.52 | 199 |
| 29 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -24.95 | -4.15 | -25.44 | 96 |
| 30 | Opening range 15m | breakout | 78.24 | -21.76 | 562 | 31.1 | -21.23 | -6.47 | -23.54 | 659 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -20.90 | -7.65 | -21.10 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -25.91 | -6.89 | -26.33 | 149 |
| 33 | Ichimoku · 1h | trend | 75.38 | -24.62 | 110 | 13.6 | -27.28 | -7.34 | -30.69 | 107 |
| 34 | Hold BTC | benchmark | 73.14 | -26.86 | 3 | 0.0 | -27.36 | -4.68 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 72.18 | -27.82 | 199 | 16.6 | -33.85 | -6.45 | -39.05 | 218 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 71.47 | -28.54 | 3 | 0.0 | -22.80 | -2.62 | -32.18 | 1 |
| 37 | Triple EMA stack · 1h | trend | 71.46 | -28.54 | 161 | 14.3 | -34.74 | -8.92 | -38.27 | 168 |
| 38 | EMA 20/50 cross · 1h | trend | 71.31 | -28.69 | 119 | 10.1 | -35.26 | -9.77 | -39.90 | 124 |
| 39 | ADX DI cross · 1h | trend | 70.45 | -29.55 | 235 | 20.0 | -34.11 | -6.20 | -36.61 | 286 |
| 40 | Bollinger breakout · 1h | breakout | 68.98 | -31.02 | 207 | 22.2 | -32.98 | -8.65 | -34.32 | 213 |
| 41 | Daily: Momentum burst | daily | 68.78 | -31.22 | 30 | 13.3 | -38.24 | -5.49 | -38.52 | 25 |
| 42 | OBV trend · 1h | momentum | 68.58 | -31.42 | 318 | 19.5 | -37.14 | -9.70 | -40.46 | 234 |
| 43 | Stochastic reversion · 1h | reversion | 67.72 | -32.28 | 392 | 40.6 | -34.04 | -3.43 | -43.45 | 434 |
| 44 | Max aggression: 5-day momentum | meta | 67.52 | -32.48 | 24 | 37.5 | -59.96 | -3.94 | -63.89 | 23 |
| 45 | RSI momentum · 1h | momentum | 66.87 | -33.13 | 188 | 13.8 | -36.90 | -8.24 | -39.43 | 203 |
| 46 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -35.45 | -9.59 | -35.79 | 211 |
| 47 | Heikin-Ashi · 1h | trend | 65.71 | -34.29 | 501 | 23.2 | -47.36 | -9.92 | -47.36 | 614 |
| 48 | MFI reversion · 1h | reversion | 64.55 | -35.45 | 484 | 33.1 | -30.95 | -4.37 | -37.45 | 182 |
| 49 | Donchian 20/10 · 1h | breakout | 64.54 | -35.46 | 172 | 16.9 | -38.02 | -8.30 | -40.54 | 194 |
| 50 | ROC + volume · 1h | momentum | 63.13 | -36.87 | 440 | 27.5 | -41.07 | -8.53 | -41.07 | 339 |
| 51 | EMA 9/21 cross · 1h | trend | 61.56 | -38.44 | 298 | 11.1 | -44.01 | -10.37 | -46.21 | 330 |
| 52 | Agent (ML meta-label) | meta | 60.60 | -39.40 | 2033 | 24.9 | -15.56 | -1.69 | -29.68 | 322 |
| 53 | MACD cross · 1h | trend | 60.45 | -39.55 | 462 | 21.0 | -48.68 | -9.36 | -49.73 | 508 |
| 54 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -52.14 | -3.81 | -54.71 | 38 |
| 55 | CCI reversion · 1h | reversion | 58.75 | -41.25 | 429 | 40.1 | -48.92 | -8.06 | -52.17 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 58.14 | -41.85 | 389 | 37.5 | -38.34 | -4.51 | -45.48 | 437 |
| 57 | Williams %R · 1h | reversion | 54.73 | -45.27 | 487 | 38.4 | -53.41 | -8.67 | -55.62 | 610 |
| 58 | VWAP momentum · 1h | momentum | 54.24 | -45.76 | 1032 | 21.6 | -57.95 | -13.29 | -59.10 | 1198 |
| 59 | RSI(14) reversion · 1h | reversion | 51.54 | -48.46 | 234 | 31.6 | -45.81 | -6.93 | -49.37 | 288 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.39 | -8.66 | -55.53 | 682 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -47.08 | -99.14 | 5327 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.74 | -31.35 | -84.71 | 1436 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.61 | -49.77 | -94.70 | 2431 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.78 | -30.88 | -91.08 | 1928 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.70 | -40.31 | -91.82 | 2243 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.14 | -27.41 | -89.36 | 1943 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -48.38 | -98.16 | 3425 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.00 | -52.71 | -97.04 | 3354 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.48 | -39.00 | -93.50 | 2154 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.26 | -22.44 | -52.28 | 650 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.21 | -34.97 | -83.50 | 1550 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.60 | -99.66 | 6293 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.07 | -40.61 | -93.12 | 2503 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.21 | -35.33 | -94.25 | 3109 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -62.89 | -99.83 | 6155 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.21 | -42.36 | -93.45 | 2267 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.58 | -24.17 | -79.08 | 1625 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -56.57 | -97.80 | 3287 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -56.38 | -99.17 | 5086 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.79 | -28.26 | -71.01 | 1200 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.92 | -48.52 | -94.96 | 2688 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.27 | -6.04 | -48.72 | 281 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.46 | -36.64 | -85.72 | 1691 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.53 | -99.76 | 6506 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -30.20 | -91.68 | 2487 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.95 | -19.67 | -83.07 | 1963 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.80 | -29.25 | -92.09 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.13 | -47.22 | -98.13 | 4055 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.11 | -46.38 | -90.19 | 2194 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.51 | -30.31 | -68.57 | 804 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.10 | -28.15 | -74.31 | 1172 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.66 | -18.77 | -83.77 | 1845 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.96 | -48.06 | -97.97 | 4424 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -87.64 | -99.94 | 8298 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T15:45 | ROC + volume · 1h | sell | SOL-USD | 7.86 | -0.16 | stop-loss |
| 2026-11-23T15:41 | Bollinger reversion · 1h | sell | AMZN | 14.63 | 0.09 | take-profit |
| 2026-11-23T15:35 | Agent (ML meta-label) | sell | BITX | 10.09 | 0.60 | selected signal exited |
| 2026-11-23T15:35 | Keltner breakout · 1h | sell | TSLA | 18.95 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T15:35 | Keltner breakout · 1h | sell | PLTR | 18.97 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T15:35 | Keltner breakout · 1h | sell | NVDA | 18.79 | -0.19 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T15:30 | Agent (ML meta-label) | buy | TNA | 5.14 | — | rebalance up |
| 2026-11-23T15:30 | Agent (ML meta-label) | buy | TECL | 4.36 | — | rebalance up |
| 2026-11-23T15:30 | Agent (ML meta-label) | buy | SQQQ | 6.31 | — | rebalance up |
| 2026-11-23T15:30 | Agent (ML meta-label) | buy | ETHU | 4.55 | — | rebalance up |
| 2026-11-23T15:30 | Agent (ML meta-label) | buy | BITX | 4.72 | — | rebalance up |
| 2026-11-23T15:30 | Agent (ML meta-label) | buy | AMD | 5.11 | — | rebalance up |
| 2026-11-23T15:30 | Agent (ML meta-label) | sell | SOXL | 3.94 | 0.04 | selected signal exited |
| 2026-11-23T15:30 | Agent (ML meta-label) | sell | PLTR | 5.18 | 0.45 | selected signal exited |
| 2026-11-23T15:30 | Agent (ML meta-label) | sell | NVDA | 5.86 | 0.40 | selected signal exited |
| 2026-11-23T15:30 | Agent (ML meta-label) | sell | LABU | 5.15 | 0.43 | selected signal exited |
| 2026-11-23T15:30 | Agent (ML meta-label) | sell | COIN | 4.97 | 0.25 | selected signal exited |
| 2026-11-23T15:30 | MFI reversion · 1h | buy | TSLA | 7.20 | — | entry signal |
| 2026-11-23T15:30 | MFI reversion · 1h | buy | TQQQ | 7.21 | — | entry signal |
| 2026-11-23T15:30 | MFI reversion · 1h | buy | SOXL | 7.21 | — | entry signal |
| 2026-11-23T15:30 | MFI reversion · 1h | buy | QQQ | 7.21 | — | entry signal |
| 2026-11-23T15:30 | MFI reversion · 1h | buy | PLTR | 7.21 | — | entry signal |
| 2026-11-23T15:30 | MFI reversion · 1h | buy | NVDA | 7.21 | — | entry signal |
| 2026-11-23T15:30 | MFI reversion · 1h | buy | COIN | 7.21 | — | entry signal |
| 2026-11-23T15:30 | MFI reversion · 1h | buy | AMZN | 7.21 | — | entry signal |
| 2026-11-23T15:30 | MFI reversion · 1h | sell | BITX | 9.01 | -0.00 | rebalance down |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | UPRO | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | TSLA | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | TQQQ | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | TNA | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | TECL | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | SPY | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | SOXL | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | QQQ | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | PLTR | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | NVDA | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | MSTR | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | MSFT | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | META | 2.68 | — | entry signal |
| 2026-11-23T15:30 | CCI reversion · 1h | buy | LABU | 2.68 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 15:45:05.000134+00:00 -> 2026-11-23 15:55:05.000134+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
