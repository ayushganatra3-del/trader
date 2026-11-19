# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T16:55:05.000166+00:00 · 65862 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.34 (-14.66%)

Closed trades 226, win rate 36.7%, fees £6.19, max drawdown -17.33%.

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

Today: 21177 decisions in 2652 calls, $0.2740 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T16:55 | 1 / 19 / 10 | cash |  |
| Breezy | 2026-11-19T16:55 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-19T16:55 | 4 / 24 / 2 | COIN 58% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.76 | 15.76 | 25 | 64.0 | 23.82 | 4.47 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.77 | 13.77 | 0 | — | 11.68 | 3.82 | -4.70 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.28 | 3.28 | 0 | — | 4.39 | 1.18 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -3.86 | -3.43 | -4.83 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | 1.17 | 0.45 | -9.06 | 212 |
| 10 | Hold SPY | benchmark | 95.37 | -4.63 | 0 | — | -4.42 | -1.53 | -7.02 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 94.57 | -5.42 | 8 | 50.0 | -4.64 | -0.30 | -18.69 | 6 |
| 13 | Agent (rotation) | meta | 94.44 | -5.56 | 210 | 28.6 | -2.43 | -0.84 | -7.63 | 152 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.78 | -5.44 | 20 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.97 | -7.03 | 0 | — | -7.32 | -1.93 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.63 | -8.37 | 0 | — | -7.68 | -2.04 | -12.67 | 1 |
| 18 | Copy: Insider buying | copy | 91.22 | -8.78 | 52 | 40.4 | -8.83 | -1.72 | -14.79 | 67 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.67 | -3.74 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 88.66 | -11.35 | 115 | 23.5 | -16.44 | -8.47 | -16.94 | 56 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 86.87 | -13.13 | 17 | 17.6 | -10.40 | -2.38 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.40 | -9.24 | -16.67 | 72 |
| 24 | Agent | meta | 85.34 | -14.66 | 226 | 36.7 | -14.25 | -6.67 | -17.06 | 202 |
| 25 | Opening range 30m | breakout | 85.25 | -14.75 | 448 | 33.5 | -12.61 | -4.33 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Connors RSI(2) · 1h | reversion | 80.67 | -19.33 | 216 | 40.3 | -14.58 | -6.48 | -15.33 | 77 |
| 28 | Parabolic SAR · 1h | trend | 80.54 | -19.46 | 193 | 27.5 | -28.29 | -8.72 | -29.07 | 198 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.45 | -5.37 | -21.50 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -24.70 | -6.53 | -27.86 | 149 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 77.56 | -22.44 | 2 | 0.0 | -18.70 | -2.60 | -26.43 | 1 |
| 33 | Opening range 15m | breakout | 76.29 | -23.71 | 546 | 31.7 | -21.38 | -6.32 | -23.54 | 674 |
| 34 | Hold BTC | benchmark | 73.91 | -26.09 | 2 | 0.0 | -22.65 | -3.64 | -28.91 | 1 |
| 35 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -49.54 | -3.23 | -57.37 | 22 |
| 36 | ADX DI cross · 1h | trend | 73.62 | -26.38 | 216 | 19.9 | -27.77 | -4.47 | -34.80 | 276 |
| 37 | Stochastic reversion · 1h | reversion | 73.10 | -26.90 | 352 | 42.6 | -34.76 | -5.29 | -36.16 | 427 |
| 38 | Ichimoku · 1h | trend | 72.70 | -27.30 | 107 | 14.0 | -32.80 | -9.94 | -33.17 | 110 |
| 39 | Bollinger breakout · 1h | breakout | 71.53 | -28.47 | 193 | 21.8 | -32.25 | -8.75 | -35.28 | 218 |
| 40 | MFI reversion · 1h | reversion | 70.66 | -29.34 | 460 | 33.9 | -28.51 | -4.27 | -31.02 | 171 |
| 41 | Supertrend · 1h | trend | 70.60 | -29.40 | 192 | 16.7 | -33.24 | -5.56 | -39.77 | 206 |
| 42 | Triple EMA stack · 1h | trend | 70.00 | -30.00 | 158 | 14.6 | -31.30 | -6.33 | -38.36 | 176 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.38 | -4.99 | -37.91 | 31 |
| 44 | EMA 20/50 cross · 1h | trend | 68.77 | -31.23 | 118 | 10.2 | -38.24 | -8.15 | -44.89 | 126 |
| 45 | MACD zero-line · 1h | trend | 68.72 | -31.28 | 187 | 17.6 | -29.48 | -5.93 | -35.43 | 208 |
| 46 | Heikin-Ashi · 1h | trend | 67.93 | -32.07 | 480 | 22.9 | -47.16 | -10.35 | -48.02 | 629 |
| 47 | RSI momentum · 1h | momentum | 67.86 | -32.14 | 183 | 14.2 | -35.39 | -6.87 | -41.13 | 203 |
| 48 | CCI reversion · 1h | reversion | 67.79 | -32.21 | 395 | 42.0 | -41.86 | -6.98 | -44.29 | 481 |
| 49 | ROC + volume · 1h | momentum | 67.21 | -32.79 | 421 | 28.3 | -36.78 | -6.78 | -41.79 | 340 |
| 50 | MACD cross · 1h | trend | 67.21 | -32.79 | 421 | 22.1 | -40.89 | -6.65 | -47.01 | 500 |
| 51 | OBV trend · 1h | momentum | 66.88 | -33.12 | 315 | 19.4 | -35.42 | -7.84 | -40.39 | 247 |
| 52 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -38.47 | -2.32 | -57.50 | 39 |
| 53 | Donchian 20/10 · 1h | breakout | 65.19 | -34.81 | 163 | 17.8 | -36.62 | -7.18 | -42.33 | 192 |
| 54 | Williams %R · 1h | reversion | 63.34 | -36.66 | 442 | 41.0 | -47.15 | -8.28 | -47.94 | 574 |
| 55 | Bollinger reversion · 1h | reversion | 62.72 | -37.28 | 355 | 38.3 | -39.54 | -6.06 | -39.96 | 418 |
| 56 | EMA 9/21 cross · 1h | trend | 61.85 | -38.15 | 286 | 11.5 | -40.71 | -8.00 | -46.75 | 324 |
| 57 | Agent (ML meta-label) | meta | 59.38 | -40.62 | 1978 | 24.7 | -25.06 | -4.42 | -25.42 | 264 |
| 58 | RSI(14) reversion · 1h | reversion | 59.16 | -40.84 | 216 | 34.3 | -39.95 | -5.82 | -43.22 | 260 |
| 59 | Z-score reversion · 1h | reversion | 57.32 | -42.68 | 229 | 34.9 | -37.32 | -5.20 | -39.76 | 258 |
| 60 | Candlestick reversal · 1h | reversion | 55.93 | -44.07 | 568 | 27.1 | -48.42 | -8.96 | -49.65 | 648 |
| 61 | VWAP momentum · 1h | momentum | 55.04 | -44.96 | 998 | 21.7 | -58.58 | -11.93 | -61.44 | 1203 |
| 62 | Three white soldiers | momentum | 53.92 | -46.08 | 598 | 14.5 | -51.03 | -23.18 | -51.09 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -47.93 | -99.10 | 5325 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.09 | -29.97 | -83.28 | 1408 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.43 | -46.44 | -94.43 | 2483 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.54 | -35.42 | -90.62 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.03 | -46.18 | -92.03 | 2298 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.70 | -30.57 | -90.70 | 2060 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.08 | -53.14 | -98.09 | 3468 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -54.02 | -96.81 | 3413 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -38.22 | -93.67 | 2208 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.78 | -35.84 | -83.78 | 1590 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -55.30 | -99.61 | 6129 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.76 | -47.20 | -92.76 | 2554 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.70 | -39.13 | -94.79 | 3202 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -75.93 | -99.83 | 6197 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.97 | -49.59 | -92.98 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.77 | -26.59 | -77.77 | 1668 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.83 | -60.84 | -97.83 | 3414 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.08 | -57.81 | -99.08 | 4985 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.70 | -29.89 | -70.72 | 1235 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.93 | -57.29 | -94.93 | 2745 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.07 | -40.74 | -86.07 | 1742 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -72.15 | -99.71 | 6429 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.81 | -30.95 | -91.01 | 2382 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.90 | -19.01 | -80.38 | 1843 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.55 | -36.78 | -91.62 | 2156 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.68 | -47.60 | -97.68 | 3932 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.97 | -59.73 | -90.03 | 2171 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.65 | -32.24 | -67.65 | 824 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.18 | -29.05 | -74.30 | 1212 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.71 | -18.60 | -81.72 | 1766 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -45.84 | -97.58 | 4344 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.41 | -99.94 | 8407 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T16:55 | Agent (ML meta-label) | sell | SPY | 3.71 | -0.02 | selected signal exited |
| 2026-11-19T16:55 | Agent (ML meta-label) | sell | MSFT | 4.97 | -0.03 | selected signal exited |
| 2026-11-19T16:55 | Williams %R · 1h | sell | TNA | 3.81 | -0.14 | stop-loss |
| 2026-11-19T16:55 | Z-score reversion · 1h | buy | PLTR | 6.37 | — | entry |
| 2026-11-19T16:55 | Z-score reversion · 1h | sell | TNA | 6.92 | -0.25 | stop-loss |
| 2026-11-19T16:55 | Bollinger reversion · 1h | sell | TNA | 15.55 | -0.66 | stop-loss |
| 2026-11-19T16:55 | RSI(14) reversion · 1h | sell | TNA | 7.27 | -0.30 | stop-loss |
| 2026-11-19T16:50 | Agent (ML meta-label) | buy | SQQQ | 4.69 | — | following OBV trend |
| 2026-11-19T16:50 | Agent (ML meta-label) | buy | SPY | 3.73 | — | entry |
| 2026-11-19T16:50 | Agent (ML meta-label) | sell | NVDA | 4.99 | -0.01 | selected signal exited |
| 2026-11-19T16:45 | Agent (ML meta-label) | buy | NVDA | 5.01 | — | entry |
| 2026-11-19T16:45 | Agent (ML meta-label) | buy | MSFT | 5.01 | — | entry |
| 2026-11-19T16:45 | Agent (ML meta-label) | sell | SPY | 5.46 | -0.01 | selected signal exited |
| 2026-11-19T16:40 | Agent (ML meta-label) | buy | SPY | 5.47 | — | entry |
| 2026-11-19T16:40 | Agent (ML meta-label) | buy | GOOGL | 5.47 | — | entry |
| 2026-11-19T16:40 | Agent | sell | TSLA | 17.20 | 0.17 | selected signal exited |
| 2026-11-19T16:35 | Agent (ML meta-label) | sell | SQQQ | 4.49 | -0.07 | selected signal exited |
| 2026-11-19T16:35 | Agent (ML meta-label) | sell | SPY | 4.60 | -0.01 | selected signal exited |
| 2026-11-19T16:35 | Agent (ML meta-label) | sell | NVDA | 4.60 | -0.02 | selected signal exited |
| 2026-11-19T16:35 | Agent (ML meta-label) | sell | GOOGL | 4.59 | -0.02 | selected signal exited |
| 2026-11-19T16:31 | Agent (ML meta-label) | buy | SPY | 4.61 | — | entry |
| 2026-11-19T16:31 | Agent (ML meta-label) | buy | NVDA | 4.61 | — | entry |
| 2026-11-19T16:31 | Agent (ML meta-label) | buy | GOOGL | 4.61 | — | entry |
| 2026-11-19T16:31 | Agent (ML meta-label) | sell | UPRO | 4.29 | -0.03 | selected signal exited |
| 2026-11-19T16:31 | MFI reversion · 1h | buy | QQQ | 6.35 | — | entry |
| 2026-11-19T16:31 | CCI reversion · 1h | buy | SQQQ | 8.50 | — | entry signal |
| 2026-11-19T16:31 | Williams %R · 1h | buy | AAPL | 3.56 | — | entry signal |
| 2026-11-19T16:31 | Bollinger reversion · 1h | buy | AAPL | 15.79 | — | entry signal |
| 2026-11-19T16:31 | Candlestick reversal · 1h | buy | UPRO | 4.61 | — | entry signal |
| 2026-11-19T16:31 | Candlestick reversal · 1h | buy | SPY | 7.03 | — | entry signal |
| 2026-11-19T16:31 | VWAP momentum · 1h | buy | QQQ | 13.82 | — | entry signal |
| 2026-11-19T16:31 | VWAP momentum · 1h | buy | META | 13.82 | — | entry signal |
| 2026-11-19T16:31 | Heikin-Ashi · 1h | buy | MSFT | 17.08 | — | entry signal |
| 2026-11-19T16:31 | Heikin-Ashi · 1h | buy | GOOGL | 17.08 | — | entry signal |
| 2026-11-19T16:31 | ADX DI cross · 1h | sell | UPRO | 4.31 | -0.03 | exit signal |
| 2026-11-19T16:31 | ADX DI cross · 1h | sell | SPY | 4.40 | -0.00 | exit signal |
| 2026-11-19T16:31 | ADX DI cross · 1h | sell | META | 4.43 | 0.03 | exit signal |
| 2026-11-19T16:27 | Agent (ML meta-label) | sell | SPY | 4.33 | -0.01 | selected signal exited |
| 2026-11-19T16:27 | Agent (ML meta-label) | sell | NVDA | 3.49 | 0.00 | selected signal exited |
| 2026-11-19T16:27 | Agent (ML meta-label) | sell | GOOGL | 4.60 | 0.00 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 16:55:05.000166+00:00 -> 2026-11-19 17:05:05.000166+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 16:55:05.000166+00:00 -> 2026-11-19 17:05:05.000166+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
