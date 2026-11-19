# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T21:50:05.000108+00:00 · 66104 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.36 (-14.64%)

Closed trades 233, win rate 36.9%, fees £6.31, max drawdown -17.33%.

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

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 35.92 · VIX 27.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 39846 decisions in 3378 calls, $0.4943 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T21:50 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-19T21:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-19T21:50 | 2 / 3 / 0 | cash |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.75 | 21.75 | 26 | 65.4 | 24.79 | 4.05 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.66 | 14.66 | 0 | — | 12.51 | 4.19 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.34 | 3.34 | 0 | — | 4.30 | 1.24 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.10 | -3.64 | -4.86 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 40 | 42.5 | -2.13 | -0.35 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.76 | -0.50 | -9.06 | 201 |
| 10 | Agent (rotation) | meta | 96.11 | -3.89 | 211 | 28.9 | -1.12 | -0.32 | -7.73 | 153 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.09 | -5.91 | 0 | — | -7.00 | -2.37 | -8.40 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.22 | -6.78 | 0 | — | -6.89 | -1.81 | -8.68 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 90.54 | -9.46 | 8 | 50.0 | -10.85 | -0.87 | -18.69 | 6 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.99 | -10.01 | 0 | — | -10.71 | -3.01 | -13.05 | 1 |
| 18 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.67 | -3.74 | -18.48 | 149 |
| 19 | Trend pullback · 1h | trend | 89.81 | -10.20 | 115 | 23.5 | -10.99 | -6.45 | -12.80 | 49 |
| 20 | Copy: Insider buying | copy | 89.38 | -10.62 | 55 | 40.0 | -9.31 | -1.84 | -14.79 | 67 |
| 21 | Daily: Bullish score | daily | 87.55 | -12.45 | 17 | 17.6 | -14.48 | -3.83 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.41 | -13.59 | 449 | 33.6 | -11.54 | -3.84 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.61 | -18.94 | 71 |
| 25 | Agent | meta | 85.36 | -14.64 | 233 | 36.9 | -13.70 | -6.20 | -16.51 | 213 |
| 26 | Agent (aggressive) | meta | 83.60 | -16.40 | 107 | 33.6 | -15.49 | -4.02 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 81.37 | -18.63 | 194 | 27.8 | -26.67 | -8.11 | -28.86 | 197 |
| 28 | Connors RSI(2) · 1h | reversion | 80.44 | -19.56 | 217 | 40.6 | -14.85 | -6.62 | -15.33 | 78 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.50 | -5.38 | -21.55 | 73 |
| 30 | Donchian 55/20 · 1h | breakout | 78.59 | -21.41 | 79 | 12.7 | -26.18 | -6.91 | -30.98 | 85 |
| 31 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.07 | -5.96 | -25.33 | 143 |
| 32 | Opening range 15m | breakout | 77.33 | -22.67 | 547 | 31.8 | -21.22 | -6.52 | -23.60 | 658 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 74.94 | -25.07 | 2 | 0.0 | -23.95 | -3.45 | -27.37 | 1 |
| 34 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -53.52 | -3.74 | -58.09 | 21 |
| 35 | Ichimoku · 1h | trend | 73.64 | -26.36 | 107 | 14.0 | -30.75 | -9.50 | -32.08 | 109 |
| 36 | ADX DI cross · 1h | trend | 72.88 | -27.12 | 226 | 20.4 | -28.62 | -4.54 | -35.87 | 279 |
| 37 | Hold BTC | benchmark | 72.41 | -27.59 | 2 | 0.0 | -24.44 | -3.93 | -29.58 | 1 |
| 38 | Stochastic reversion · 1h | reversion | 71.25 | -28.75 | 356 | 42.1 | -36.63 | -5.62 | -36.74 | 426 |
| 39 | Triple EMA stack · 1h | trend | 70.26 | -29.74 | 161 | 14.3 | -30.40 | -6.32 | -37.24 | 170 |
| 40 | Bollinger breakout · 1h | breakout | 70.05 | -29.95 | 195 | 21.5 | -32.97 | -8.56 | -36.32 | 216 |
| 41 | Supertrend · 1h | trend | 69.94 | -30.06 | 197 | 16.8 | -33.38 | -5.61 | -39.90 | 204 |
| 42 | EMA 20/50 cross · 1h | trend | 69.61 | -30.39 | 118 | 10.2 | -36.45 | -7.90 | -43.51 | 127 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 44 | MFI reversion · 1h | reversion | 68.97 | -31.03 | 466 | 33.7 | -30.44 | -4.60 | -31.94 | 175 |
| 45 | Heikin-Ashi · 1h | trend | 68.12 | -31.88 | 483 | 23.0 | -46.26 | -10.34 | -47.85 | 619 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -28.11 | -5.62 | -34.12 | 207 |
| 47 | RSI momentum · 1h | momentum | 67.81 | -32.19 | 184 | 14.1 | -35.08 | -6.65 | -41.55 | 203 |
| 48 | OBV trend · 1h | momentum | 67.75 | -32.25 | 315 | 19.4 | -35.33 | -7.66 | -41.18 | 239 |
| 49 | CCI reversion · 1h | reversion | 66.44 | -33.56 | 398 | 42.0 | -42.63 | -7.19 | -44.29 | 480 |
| 50 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -47.44 | -3.25 | -57.50 | 38 |
| 51 | MACD cross · 1h | trend | 64.84 | -35.16 | 431 | 21.6 | -43.50 | -7.05 | -49.08 | 496 |
| 52 | ROC + volume · 1h ⏸ | momentum | 64.82 | -35.18 | 431 | 27.6 | -40.04 | -6.97 | -44.84 | 342 |
| 53 | Donchian 20/10 · 1h | breakout | 64.64 | -35.36 | 165 | 17.6 | -37.12 | -7.22 | -43.26 | 192 |
| 54 | Bollinger reversion · 1h | reversion | 62.18 | -37.82 | 357 | 38.1 | -39.39 | -6.00 | -40.40 | 416 |
| 55 | EMA 9/21 cross · 1h | trend | 62.11 | -37.89 | 291 | 11.3 | -40.95 | -8.01 | -47.32 | 323 |
| 56 | Williams %R · 1h | reversion | 61.30 | -38.70 | 447 | 40.5 | -48.85 | -8.67 | -48.85 | 575 |
| 57 | Agent (ML meta-label) | meta | 58.03 | -41.98 | 1995 | 24.7 | -30.32 | -5.35 | -30.44 | 310 |
| 58 | RSI(14) reversion · 1h | reversion | 57.91 | -42.09 | 219 | 33.8 | -40.39 | -5.86 | -43.68 | 271 |
| 59 | Z-score reversion · 1h | reversion | 55.48 | -44.52 | 233 | 34.3 | -39.02 | -5.45 | -41.60 | 256 |
| 60 | Candlestick reversal · 1h | reversion | 54.65 | -45.35 | 578 | 26.8 | -49.67 | -9.30 | -49.67 | 671 |
| 61 | VWAP momentum · 1h | momentum | 54.61 | -45.39 | 1004 | 21.6 | -57.56 | -11.73 | -60.81 | 1191 |
| 62 | Three white soldiers | momentum | 52.98 | -47.02 | 608 | 14.3 | -51.66 | -23.34 | -51.66 | 665 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.09 | -47.83 | -99.09 | 5274 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.04 | -30.10 | -83.44 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.41 | -47.00 | -94.44 | 2462 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.68 | -35.39 | -90.68 | 1943 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.96 | -45.36 | -92.01 | 2285 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.43 | -30.40 | -90.51 | 2036 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -51.65 | -98.15 | 3482 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -52.75 | -96.73 | 3368 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -35.59 | -93.81 | 2216 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.63 | -35.78 | -83.63 | 1583 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.64 | -57.86 | -99.64 | 6224 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.88 | -46.59 | -92.89 | 2529 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.69 | -38.46 | -94.75 | 3178 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -75.28 | -99.83 | 6236 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.16 | -48.69 | -93.16 | 2274 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.31 | -25.55 | -78.33 | 1627 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.81 | -60.83 | -97.82 | 3383 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.11 | -59.75 | -99.11 | 5026 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.68 | -29.70 | -70.71 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.88 | -57.02 | -94.89 | 2717 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.11 | -40.58 | -86.12 | 1711 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -74.13 | -99.72 | 6479 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.21 | -32.30 | -91.21 | 2406 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.72 | -19.54 | -80.72 | 1881 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.73 | -37.86 | -91.74 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.73 | -48.07 | -97.73 | 3975 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.07 | -56.47 | -90.07 | 2176 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.87 | -31.37 | -67.87 | 800 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.40 | -29.06 | -74.57 | 1206 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.63 | -18.93 | -82.63 | 1810 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.65 | -47.65 | -97.65 | 4377 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.48 | -99.94 | 8412 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T21:00 | Supertrend · 1h | sell | ETH-USD | 17.34 | -0.47 | exit signal |
| 2026-11-19T20:55 | Agent (rotation) | sell | SQQQ | 33.96 | 2.89 | selected signal exited |
| 2026-11-19T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 99.63 | 1.04 | target is flat |
| 2026-11-19T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 121.75 | 10.36 | target is flat |
| 2026-11-19T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 91.03 | -0.62 | target is flat |
| 2026-11-19T20:55 | Agent (ML meta-label) | buy | TQQQ | 7.30 | — | entry |
| 2026-11-19T20:55 | Agent (aggressive) | sell | SOXL | 41.73 | -0.15 | selected signal exited |
| 2026-11-19T20:55 | Agent | sell | TSLA | 17.23 | 0.11 | selected signal exited |
| 2026-11-19T20:55 | Agent | sell | SQQQ | 17.18 | 0.08 | selected signal exited |
| 2026-11-19T20:55 | Agent | sell | SOXL | 17.02 | -0.06 | selected signal exited |
| 2026-11-19T20:55 | Agent | sell | META | 17.00 | -0.06 | selected signal exited |
| 2026-11-19T20:55 | MFI reversion · 1h | buy | AMD | 11.58 | — | entry |
| 2026-11-19T20:55 | MFI reversion · 1h | sell | TSLA | 9.96 | 0.02 | target is flat |
| 2026-11-19T20:55 | MFI reversion · 1h | sell | BITX | 9.88 | -0.21 | target is flat |
| 2026-11-19T20:55 | Candlestick reversal · 1h | buy | MSTR | 4.69 | — | entry |
| 2026-11-19T20:55 | Opening range 30m | sell | SQQQ | 23.53 | 2.26 | end-of-day flatten |
| 2026-11-19T20:55 | Opening range 15m | sell | SQQQ | 21.06 | 2.03 | end-of-day flatten |
| 2026-11-19T20:52 | Agent (ML meta-label) | sell | AAPL | 7.30 | -0.01 | selected signal exited |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 21:50:05.000108+00:00 -> 2026-11-19 22:00:05.000108+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 21:50:05.000108+00:00 -> 2026-11-19 22:00:05.000108+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
