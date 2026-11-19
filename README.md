# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T20:50:05.000135+00:00 · 66054 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.44 (-14.56%)

Closed trades 229, win rate 36.7%, fees £6.28, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| META | 16.98 | -0.08 |
| SOXL | 17.10 | +0.02 |
| SQQQ | 17.20 | +0.11 |
| TSLA | 17.23 | +0.10 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-19 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, LRN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-18)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 33.12 · VIX 24.56 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 6.2, AMZN 6.2, TSLA 4.1, AMD 3.9, META 1.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 38496 decisions in 3228 calls, $0.4770 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T20:50 | 8 / 21 / 1 | cash |  |
| Breezy | 2026-11-19T20:50 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-19T20:50 | 6 / 23 / 1 | COIN 59% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.97% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| VWAP reversion | META | 1.90 | +2.79% | 4 |
| OBV trend | SQQQ | 1.88 | +3.85% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.93 | 21.93 | 25 | 64.0 | 24.98 | 4.05 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.56 | 14.56 | 0 | — | 12.43 | 4.16 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.08 | 3.08 | 0 | — | 4.04 | 1.17 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.78 | -0.22 | 39 | 41.0 | -1.98 | -0.32 | -9.74 | 35 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.10 | -3.64 | -4.86 | 71 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.76 | -0.50 | -9.06 | 201 |
| 10 | Agent (rotation) | meta | 96.16 | -3.84 | 210 | 28.6 | -1.07 | -0.30 | -7.73 | 153 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.26 | -5.74 | 0 | — | -6.82 | -2.32 | -8.32 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.21 | -6.79 | 0 | — | -6.89 | -1.81 | -8.68 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.17 | -8.83 | 25 | 16.0 | -10.04 | -8.43 | -10.04 | 24 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.05 | -8.95 | 8 | 50.0 | -10.34 | -0.82 | -18.69 | 6 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.98 | -10.02 | 0 | — | -10.71 | -3.01 | -13.05 | 1 |
| 18 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.67 | -3.74 | -18.48 | 149 |
| 19 | Copy: Insider buying | copy | 89.68 | -10.32 | 55 | 40.0 | -9.17 | -1.80 | -14.79 | 67 |
| 20 | Trend pullback · 1h | trend | 89.64 | -10.36 | 115 | 23.5 | -11.13 | -6.51 | -12.77 | 49 |
| 21 | Daily: Bullish score | daily | 87.35 | -12.65 | 17 | 17.6 | -14.64 | -3.88 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.44 | -13.56 | 448 | 33.5 | -11.51 | -3.82 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.61 | -18.94 | 71 |
| 25 | Agent | meta | 85.44 | -14.56 | 229 | 36.7 | -13.51 | -6.09 | -16.51 | 213 |
| 26 | Agent (aggressive) | meta | 83.80 | -16.20 | 106 | 34.0 | -15.30 | -3.96 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 81.22 | -18.78 | 194 | 27.8 | -26.80 | -8.15 | -28.86 | 197 |
| 28 | Connors RSI(2) · 1h | reversion | 80.48 | -19.52 | 217 | 40.6 | -14.80 | -6.60 | -15.33 | 78 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.50 | -5.38 | -21.55 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.31 | -6.04 | -25.33 | 144 |
| 31 | Donchian 55/20 · 1h | breakout | 78.45 | -21.55 | 79 | 12.7 | -26.31 | -6.96 | -30.97 | 85 |
| 32 | Opening range 15m | breakout | 77.36 | -22.64 | 546 | 31.7 | -21.19 | -6.51 | -23.60 | 658 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 74.85 | -25.15 | 2 | 0.0 | -24.03 | -3.46 | -27.37 | 1 |
| 34 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -52.95 | -3.70 | -57.76 | 21 |
| 35 | Ichimoku · 1h | trend | 73.50 | -26.50 | 107 | 14.0 | -30.88 | -9.54 | -32.08 | 109 |
| 36 | Hold BTC | benchmark | 73.18 | -26.82 | 2 | 0.0 | -23.73 | -3.80 | -29.17 | 1 |
| 37 | ADX DI cross · 1h | trend | 72.94 | -27.06 | 226 | 20.4 | -28.44 | -4.51 | -35.87 | 278 |
| 38 | Stochastic reversion · 1h | reversion | 71.56 | -28.44 | 356 | 42.1 | -36.19 | -5.55 | -36.70 | 426 |
| 39 | Triple EMA stack · 1h | trend | 70.15 | -29.85 | 161 | 14.3 | -30.38 | -6.25 | -37.24 | 170 |
| 40 | Supertrend · 1h | trend | 70.10 | -29.90 | 196 | 16.8 | -33.22 | -5.58 | -39.81 | 204 |
| 41 | Bollinger breakout · 1h | breakout | 69.92 | -30.08 | 195 | 21.5 | -33.53 | -8.71 | -36.30 | 218 |
| 42 | EMA 20/50 cross · 1h | trend | 69.65 | -30.34 | 118 | 10.2 | -36.64 | -7.93 | -43.94 | 127 |
| 43 | MFI reversion · 1h | reversion | 69.48 | -30.52 | 464 | 33.6 | -29.96 | -4.52 | -31.89 | 173 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -28.11 | -5.62 | -34.12 | 207 |
| 46 | Heikin-Ashi · 1h | trend | 68.00 | -32.00 | 483 | 23.0 | -46.36 | -10.35 | -47.85 | 619 |
| 47 | RSI momentum · 1h | momentum | 67.69 | -32.31 | 184 | 14.1 | -35.34 | -6.78 | -41.55 | 203 |
| 48 | OBV trend · 1h | momentum | 67.62 | -32.38 | 315 | 19.4 | -35.68 | -7.90 | -41.18 | 240 |
| 49 | CCI reversion · 1h | reversion | 66.77 | -33.23 | 398 | 42.0 | -42.38 | -7.13 | -44.29 | 480 |
| 50 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -46.40 | -3.16 | -57.50 | 38 |
| 51 | MACD cross · 1h | trend | 65.12 | -34.88 | 431 | 21.6 | -43.15 | -7.01 | -49.03 | 496 |
| 52 | ROC + volume · 1h ⏸ | momentum | 64.82 | -35.18 | 431 | 27.6 | -40.04 | -6.97 | -44.84 | 342 |
| 53 | Donchian 20/10 · 1h | breakout | 64.52 | -35.48 | 165 | 17.6 | -37.24 | -7.23 | -43.24 | 192 |
| 54 | Bollinger reversion · 1h | reversion | 62.28 | -37.72 | 357 | 38.1 | -39.28 | -5.99 | -40.36 | 416 |
| 55 | EMA 9/21 cross · 1h | trend | 61.99 | -38.01 | 291 | 11.3 | -41.06 | -8.04 | -47.32 | 323 |
| 56 | Williams %R · 1h | reversion | 61.69 | -38.31 | 447 | 40.5 | -48.48 | -8.61 | -48.74 | 575 |
| 57 | Agent (ML meta-label) | meta | 58.43 | -41.57 | 1994 | 24.7 | -29.24 | -5.26 | -29.71 | 312 |
| 58 | RSI(14) reversion · 1h | reversion | 58.27 | -41.73 | 219 | 33.8 | -39.99 | -5.78 | -43.68 | 271 |
| 59 | Z-score reversion · 1h | reversion | 55.80 | -44.20 | 233 | 34.3 | -38.63 | -5.40 | -41.55 | 256 |
| 60 | Candlestick reversal · 1h | reversion | 55.01 | -44.99 | 578 | 26.8 | -49.36 | -9.25 | -49.66 | 671 |
| 61 | VWAP momentum · 1h | momentum | 54.50 | -45.50 | 1004 | 21.6 | -57.62 | -11.74 | -60.81 | 1191 |
| 62 | Three white soldiers | momentum | 52.98 | -47.02 | 608 | 14.3 | -51.66 | -23.34 | -51.66 | 665 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -47.82 | -99.10 | 5284 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.08 | -30.21 | -83.44 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.41 | -47.02 | -94.44 | 2463 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.68 | -35.39 | -90.68 | 1943 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.03 | -45.61 | -92.07 | 2288 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.42 | -30.39 | -90.53 | 2037 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -51.65 | -98.15 | 3482 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -53.25 | -96.75 | 3371 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.73 | -36.41 | -93.76 | 2216 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.66 | -35.79 | -83.66 | 1584 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.63 | -57.36 | -99.63 | 6222 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.88 | -46.63 | -92.89 | 2529 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.70 | -38.56 | -94.76 | 3180 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -75.73 | -99.83 | 6240 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.20 | -48.77 | -93.21 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.32 | -25.53 | -78.34 | 1627 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.93 | -97.83 | 3385 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -59.47 | -99.10 | 5029 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.67 | -29.72 | -70.71 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.88 | -57.05 | -94.89 | 2717 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.11 | -40.58 | -86.12 | 1711 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -73.91 | -99.72 | 6476 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.03 | -31.99 | -91.05 | 2401 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.42 | -19.42 | -80.48 | 1876 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.65 | -37.64 | -91.67 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.70 | -47.87 | -97.72 | 3976 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.10 | -56.43 | -90.10 | 2178 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.78 | -31.58 | -67.78 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.39 | -29.08 | -74.57 | 1206 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.46 | -18.95 | -82.52 | 1809 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.62 | -47.19 | -97.64 | 4373 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.50 | -99.94 | 8413 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T20:50 | Agent (ML meta-label) | buy | AAPL | 7.30 | — | entry |
| 2026-11-19T20:45 | Agent (ML meta-label) | sell | TQQQ | 7.28 | -0.02 | selected signal exited |
| 2026-11-19T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 91.65 | — | entry |
| 2026-11-19T20:30 | CCI reversion · 1h | buy | AMD | 1.68 | — | entry signal |
| 2026-11-19T20:30 | Candlestick reversal · 1h | buy | TQQQ | 3.11 | — | rebalance up |
| 2026-11-19T20:30 | Candlestick reversal · 1h | buy | QQQ | 3.24 | — | rebalance up |
| 2026-11-19T20:30 | Candlestick reversal · 1h | sell | TECL | 4.98 | -0.03 | exit signal |
| 2026-11-19T20:30 | Candlestick reversal · 1h | sell | COIN | 6.05 | -0.09 | stop-loss |
| 2026-11-19T20:30 | Bollinger breakout · 1h | buy | SQQQ | 17.50 | — | entry signal |
| 2026-11-19T20:30 | Donchian 55/20 · 1h | buy | SQQQ | 19.64 | — | entry signal |
| 2026-11-19T20:30 | Donchian 20/10 · 1h | buy | SQQQ | 16.15 | — | entry signal |
| 2026-11-19T20:30 | VWAP momentum · 1h | sell | AAPL | 13.53 | -0.04 | exit signal |
| 2026-11-19T20:30 | ADX DI cross · 1h | sell | TSLA | 18.05 | -0.08 | exit signal |
| 2026-11-19T20:30 | MACD cross · 1h | buy | SQQQ | 7.21 | — | entry signal |
| 2026-11-19T20:30 | MACD cross · 1h | sell | BITX | 5.04 | -0.29 | stop-loss |
| 2026-11-19T20:25 | Agent (ML meta-label) | buy | TQQQ | 7.30 | — | entry |
| 2026-11-19T20:21 | Agent (ML meta-label) | sell | TSLA | 2.05 | 0.00 | selected signal exited |
| 2026-11-19T20:21 | Agent (ML meta-label) | sell | TQQQ | 6.52 | 0.06 | selected signal exited |
| 2026-11-19T20:20 | Agent (aggressive) | buy | SOXL | 41.87 | — | following CCI reversion, Z-score reversion |
| 2026-11-19T20:20 | Agent | buy | SOXL | 17.08 | — | following CCI reversion, Z-score reversion |
| 2026-11-19T20:05 | Agent (ML meta-label) | buy | TSLA | 2.05 | — | following Stochastic reversion |
| 2026-11-19T20:05 | Agent (ML meta-label) | buy | TQQQ | 6.46 | — | entry |
| 2026-11-19T20:05 | Agent (ML meta-label) | sell | TECL | 7.21 | -0.09 | selected signal exited |
| 2026-11-19T20:05 | MFI reversion · 1h | buy | TSLA | 7.98 | — | rebalance up |
| 2026-11-19T20:05 | MFI reversion · 1h | sell | QQQ | 9.90 | -0.22 | stop-loss |
| 2026-11-19T20:00 | Agent (ML meta-label) | buy | TECL | 7.31 | — | entry |
| 2026-11-19T20:00 | CCI reversion · 1h | buy | AAPL | 7.66 | — | rebalance up |
| 2026-11-19T20:00 | CCI reversion · 1h | sell | NVDA | 9.34 | -0.41 | stop-loss |
| 2026-11-19T20:00 | Candlestick reversal · 1h | buy | TQQQ | 2.99 | — | entry |
| 2026-11-19T20:00 | Candlestick reversal · 1h | buy | TECL | 5.02 | — | entry |
| 2026-11-19T20:00 | Candlestick reversal · 1h | buy | SOXL | 5.02 | — | entry |
| 2026-11-19T20:00 | Candlestick reversal · 1h | sell | SOL-USD | 6.87 | -0.14 | exit signal |
| 2026-11-19T20:00 | Candlestick reversal · 1h | sell | BTC-USD | 6.15 | -0.10 | exit signal |
| 2026-11-19T20:00 | Supertrend · 1h | sell | BTC-USD | 17.34 | -0.42 | exit signal |
| 2026-11-19T20:00 | MACD cross · 1h | sell | GOOGL | 5.92 | -0.15 | stop-loss |
| 2026-11-19T19:55 | Agent | buy | SQQQ | 17.10 | — | following OBV trend |
| 2026-11-19T19:50 | Agent (ML meta-label) | sell | TECL | 7.30 | -0.06 | selected signal exited |
| 2026-11-19T19:50 | MACD cross · 1h | buy | MSFT | 3.59 | — | rebalance up |
| 2026-11-19T19:50 | MACD cross · 1h | buy | COIN | 3.49 | — | rebalance up |
| 2026-11-19T19:50 | MACD cross · 1h | sell | NVDA | 5.10 | -0.19 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 20:50:05.000135+00:00 -> 2026-11-19 21:00:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 20:50:05.000135+00:00 -> 2026-11-19 21:00:05.000135+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
