# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T16:15:05.000174+00:00 · 70748 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.78 (-21.22%)

Closed trades 238, win rate 36.1%, fees £6.48, max drawdown -21.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 16.08 | -0.53 |

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

Today: 16322 decisions in 2410 calls, $0.2158 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T16:15 | 0 / 17 / 14 | cash |  |
| Breezy | 2026-11-23T16:15 | 0 / 29 / 2 | cash |  |
| Boozy | 2026-11-23T16:15 | 2 / 26 / 3 | COIN 74% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.49 | 15.49 | 0 | — | 13.49 | 4.52 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 8.02 | 1.45 | -9.74 | 35 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.73 | 3.73 | 0 | — | 1.79 | 0.58 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.98 | 0.98 | 209 | 31.6 | 0.64 | 0.29 | -8.71 | 210 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.78 | -3.55 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.44 | -3.56 | 219 | 28.8 | 0.08 | 0.11 | -7.48 | 156 |
| 11 | Hold SPY | benchmark | 95.60 | -4.40 | 0 | — | -6.38 | -1.59 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.20 | -3.12 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.20 | -5.49 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.31 | -7.68 | 0 | — | -8.73 | -1.79 | -13.87 | 1 |
| 15 | VWAP reversion · 1h | reversion | 92.18 | -7.82 | 163 | 46.0 | -5.11 | -0.67 | -20.49 | 156 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 17 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.07 | -3.58 | -9.21 | 32 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.69 | -9.31 | 0 | — | -10.63 | -2.27 | -17.03 | 1 |
| 19 | Copy: Insider buying | copy | 89.01 | -10.99 | 57 | 40.4 | -18.75 | -3.69 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.77 | -3.23 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 87.11 | -12.89 | 9 | 44.4 | -10.38 | -0.52 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 87.00 | -13.00 | 452 | 33.6 | -12.32 | -4.13 | -14.52 | 540 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -17.11 | -3.84 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 84.19 | -15.81 | 75 | 20.0 | -16.03 | -6.35 | -16.95 | 74 |
| 25 | Parabolic SAR · 1h | trend | 81.60 | -18.40 | 200 | 27.0 | -26.75 | -7.35 | -30.20 | 190 |
| 26 | Connors RSI(2) · 1h | reversion | 80.76 | -19.24 | 219 | 40.6 | -13.32 | -5.68 | -14.31 | 66 |
| 27 | Donchian 55/20 · 1h | breakout | 79.05 | -20.95 | 81 | 12.3 | -26.89 | -7.66 | -28.72 | 84 |
| 28 | Agent | meta | 78.78 | -21.22 | 238 | 36.1 | -26.41 | -5.75 | -26.80 | 197 |
| 29 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -25.70 | -4.32 | -26.03 | 95 |
| 30 | Opening range 15m | breakout | 77.96 | -22.04 | 563 | 31.1 | -21.94 | -6.77 | -23.54 | 659 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -21.34 | -7.51 | -21.71 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -26.85 | -7.10 | -27.48 | 150 |
| 33 | Ichimoku · 1h | trend | 75.16 | -24.84 | 110 | 13.6 | -27.96 | -7.61 | -30.49 | 106 |
| 34 | Hold BTC | benchmark | 72.87 | -27.13 | 3 | 0.0 | -27.65 | -4.77 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 71.94 | -28.06 | 199 | 16.6 | -33.69 | -6.41 | -38.65 | 221 |
| 36 | Triple EMA stack · 1h | trend | 71.45 | -28.55 | 161 | 14.3 | -34.45 | -8.71 | -38.30 | 168 |
| 37 | EMA 20/50 cross · 1h | trend | 71.23 | -28.77 | 119 | 10.1 | -35.29 | -9.78 | -39.89 | 124 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 70.80 | -29.20 | 3 | 0.0 | -23.66 | -2.82 | -32.18 | 1 |
| 39 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -34.47 | -6.24 | -37.32 | 287 |
| 40 | Daily: Momentum burst | daily | 69.00 | -31.00 | 30 | 13.3 | -37.65 | -5.37 | -38.52 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.85 | -31.15 | 207 | 22.2 | -33.29 | -8.75 | -34.50 | 213 |
| 42 | OBV trend · 1h | momentum | 68.54 | -31.46 | 319 | 19.4 | -37.29 | -9.73 | -40.48 | 234 |
| 43 | Stochastic reversion · 1h | reversion | 67.47 | -32.53 | 392 | 40.6 | -35.35 | -3.68 | -44.29 | 436 |
| 44 | Max aggression: 5-day momentum | meta | 67.30 | -32.70 | 24 | 37.5 | -60.08 | -3.94 | -64.11 | 23 |
| 45 | RSI momentum · 1h | momentum | 66.61 | -33.39 | 188 | 13.8 | -37.05 | -8.24 | -39.43 | 203 |
| 46 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -35.45 | -9.59 | -35.79 | 211 |
| 47 | Heikin-Ashi · 1h | trend | 65.42 | -34.58 | 501 | 23.2 | -46.45 | -9.61 | -46.78 | 612 |
| 48 | MFI reversion · 1h | reversion | 64.26 | -35.74 | 484 | 33.1 | -30.92 | -4.38 | -37.45 | 183 |
| 49 | Donchian 20/10 · 1h | breakout | 64.19 | -35.81 | 173 | 16.8 | -38.35 | -8.39 | -40.53 | 194 |
| 50 | ROC + volume · 1h | momentum | 62.74 | -37.26 | 442 | 27.4 | -41.57 | -8.60 | -41.77 | 341 |
| 51 | EMA 9/21 cross · 1h | trend | 61.49 | -38.51 | 298 | 11.1 | -44.02 | -10.38 | -46.19 | 330 |
| 52 | Agent (ML meta-label) | meta | 60.49 | -39.51 | 2033 | 24.9 | -18.41 | -2.15 | -30.89 | 320 |
| 53 | MACD cross · 1h | trend | 60.26 | -39.74 | 463 | 21.0 | -48.72 | -9.36 | -50.13 | 507 |
| 54 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -52.78 | -3.84 | -54.71 | 38 |
| 55 | CCI reversion · 1h | reversion | 58.57 | -41.43 | 429 | 40.1 | -48.88 | -8.09 | -51.98 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 57.99 | -42.01 | 389 | 37.5 | -38.35 | -4.55 | -45.42 | 437 |
| 57 | Williams %R · 1h | reversion | 54.56 | -45.44 | 487 | 38.4 | -53.35 | -8.64 | -55.62 | 609 |
| 58 | VWAP momentum · 1h | momentum | 54.05 | -45.95 | 1032 | 21.6 | -58.06 | -13.35 | -59.08 | 1198 |
| 59 | RSI(14) reversion · 1h | reversion | 51.38 | -48.62 | 234 | 31.6 | -45.95 | -6.96 | -49.37 | 286 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.46 | -8.51 | -54.46 | 680 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -47.53 | -99.14 | 5335 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.75 | -31.64 | -84.55 | 1436 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.50 | -49.08 | -94.57 | 2429 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.85 | -31.31 | -91.08 | 1928 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.67 | -40.43 | -91.76 | 2246 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.20 | -27.49 | -89.37 | 1942 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.14 | -48.04 | -98.15 | 3415 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.00 | -52.54 | -97.04 | 3356 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -38.88 | -93.48 | 2153 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.26 | -22.44 | -52.28 | 650 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.26 | -35.05 | -83.50 | 1550 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.60 | -99.66 | 6290 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.09 | -40.29 | -93.13 | 2500 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.24 | -35.43 | -94.26 | 3123 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -62.38 | -99.82 | 6147 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.23 | -42.76 | -93.43 | 2265 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.53 | -24.13 | -78.97 | 1620 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -56.50 | -97.79 | 3286 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -56.82 | -99.17 | 5090 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.85 | -28.24 | -71.00 | 1199 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.93 | -48.65 | -94.96 | 2685 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.49 | -6.10 | -48.72 | 281 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.61 | -37.15 | -85.80 | 1694 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.47 | -99.76 | 6510 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.54 | -30.05 | -91.68 | 2485 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.84 | -19.57 | -82.93 | 1961 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.77 | -29.02 | -92.08 | 2165 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.12 | -47.07 | -98.13 | 4054 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.23 | -47.57 | -90.30 | 2197 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.57 | -30.10 | -68.62 | 802 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.14 | -28.35 | -74.26 | 1170 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.72 | -18.83 | -83.83 | 1845 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.96 | -48.03 | -97.96 | 4426 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -89.19 | -99.94 | 8286 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T16:05 | Donchian 55/20 · 1h | buy | XRP-USD | 5.64 | — | rebalance up |
| 2026-11-23T16:05 | Donchian 55/20 · 1h | buy | SOL-USD | 5.90 | — | rebalance up |
| 2026-11-23T16:05 | Donchian 55/20 · 1h | buy | DOGE-USD | 5.69 | — | rebalance up |
| 2026-11-23T16:05 | Donchian 55/20 · 1h | buy | BTC-USD | 5.99 | — | rebalance up |
| 2026-11-23T16:05 | Donchian 55/20 · 1h | sell | ETH-USD | 15.74 | -0.36 | stop-loss |
| 2026-11-23T16:05 | Donchian 20/10 · 1h | buy | NVDA | 6.80 | — | rebalance up |
| 2026-11-23T16:05 | Donchian 20/10 · 1h | sell | ETH-USD | 12.80 | -0.32 | stop-loss |
| 2026-11-23T16:05 | OBV trend · 1h | sell | ETH-USD | 1.16 | -0.03 | stop-loss |
| 2026-11-23T16:05 | ROC + volume · 1h | sell | BTC-USD | 7.83 | -0.16 | stop-loss |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | UPRO | 4.06 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | TSLA | 4.14 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | TQQQ | 4.08 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | TECL | 4.03 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | SPY | 4.15 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | SOXL | 4.03 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | QQQ | 4.13 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | PLTR | 4.10 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | NVDA | 4.10 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | MSTR | 4.11 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | MSFT | 4.13 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | LABU | 4.14 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | ETHU | 4.07 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | BTC-USD | 4.10 | 0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | BITX | 4.06 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | AMZN | 4.16 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | ADX DI cross · 1h | sell | AMD | 4.12 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:05 | Parabolic SAR · 1h | buy | TSLA | 4.48 | — | rebalance up |
| 2026-11-23T16:05 | Parabolic SAR · 1h | sell | ETH-USD | 10.10 | -0.31 | stop-loss |
| 2026-11-23T16:05 | MACD cross · 1h | sell | ETH-USD | 4.61 | -0.08 | stop-loss |
| 2026-11-23T16:00 | Squeeze breakout · 1h | buy | DOGE-USD | 21.08 | — | entry signal |
| 2026-11-23T16:00 | ROC + volume · 1h | buy | SOL-USD | 7.82 | — | entry signal |
| 2026-11-23T16:00 | ROC + volume · 1h | buy | DOGE-USD | 7.86 | — | entry signal |
| 2026-11-23T16:00 | Heikin-Ashi · 1h | buy | SOL-USD | 16.41 | — | entry signal |
| 2026-11-23T16:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 16.41 | — | entry signal |
| 2026-11-23T15:56 | Agent (rotation) | sell | AAPL | 3.57 | -0.02 | selected signal exited |
| 2026-11-23T15:56 | Gap and go | sell | AAPL | 16.77 | -0.07 | exit signal |
| 2026-11-23T15:50 | Agent (rotation) | sell | TSLA | 8.28 | 0.07 | selected signal exited |
| 2026-11-23T15:50 | Agent (rotation) | sell | QQQ | 3.56 | -0.03 | selected signal exited |
| 2026-11-23T15:50 | Agent (rotation) | sell | PLTR | 8.00 | -0.09 | selected signal exited |
| 2026-11-23T15:50 | ROC + volume · 1h | sell | DOGE-USD | 7.83 | -0.05 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 16:15:05.000174+00:00 -> 2026-11-23 16:25:05.000174+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
