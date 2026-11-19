# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T15:55:05.000153+00:00 · 65822 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.14 (-14.86%)

Closed trades 225, win rate 36.4%, fees £6.18, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 17.00 | -0.03 |

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

Today: 17655 decisions in 2532 calls, $0.2328 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T15:55 | 1 / 19 / 10 | cash |  |
| Breezy | 2026-11-19T15:55 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-19T15:55 | 4 / 20 / 6 | COIN 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.97% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| Connors RSI(2) | SQQQ | 1.81 | +3.66% | 10 |
| VWAP reversion | META | 1.80 | +2.54% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.71 | 15.71 | 25 | 64.0 | 23.18 | 4.42 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.45 | 13.45 | 0 | — | 11.57 | 3.77 | -4.64 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.01 | 3.01 | 0 | — | 4.25 | 1.16 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -3.86 | -3.43 | -4.83 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | 1.17 | 0.45 | -9.06 | 212 |
| 10 | Hold SPY | benchmark | 95.28 | -4.72 | 0 | — | -4.30 | -1.50 | -6.99 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 94.75 | -5.25 | 8 | 50.0 | -3.90 | -0.26 | -18.69 | 6 |
| 13 | Agent (rotation) | meta | 94.42 | -5.58 | 210 | 28.6 | -2.40 | -0.83 | -7.63 | 152 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.81 | -7.19 | 0 | — | -7.32 | -1.93 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 92.72 | -7.28 | 0 | — | -6.42 | -1.65 | -12.67 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 18 | Copy: Insider buying | copy | 90.80 | -9.20 | 52 | 40.4 | -9.05 | -1.77 | -14.79 | 67 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 88.66 | -11.35 | 115 | 23.5 | -17.17 | -8.35 | -17.67 | 57 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 86.72 | -13.28 | 17 | 17.6 | -10.04 | -2.39 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.26 | -9.16 | -16.26 | 71 |
| 24 | Opening range 30m | breakout | 85.24 | -14.76 | 448 | 33.5 | -12.60 | -4.32 | -14.66 | 561 |
| 25 | Agent | meta | 85.14 | -14.86 | 225 | 36.4 | -14.63 | -6.95 | -17.06 | 204 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 80.65 | -19.35 | 189 | 28.0 | -28.40 | -8.79 | -29.07 | 199 |
| 28 | Connors RSI(2) · 1h | reversion | 80.62 | -19.38 | 216 | 40.3 | -14.27 | -6.34 | -15.00 | 78 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.45 | -5.37 | -21.50 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -24.73 | -6.53 | -27.88 | 149 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 76.63 | -23.37 | 2 | 0.0 | -19.31 | -2.74 | -26.43 | 1 |
| 33 | Opening range 15m | breakout | 76.29 | -23.71 | 546 | 31.7 | -21.37 | -6.31 | -23.24 | 674 |
| 34 | Hold BTC | benchmark | 73.90 | -26.10 | 2 | 0.0 | -22.37 | -3.61 | -28.91 | 1 |
| 35 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -49.34 | -3.22 | -57.31 | 22 |
| 36 | ADX DI cross · 1h | trend | 73.44 | -26.56 | 211 | 19.9 | -27.72 | -4.47 | -34.67 | 277 |
| 37 | Stochastic reversion · 1h | reversion | 73.01 | -26.99 | 352 | 42.6 | -34.50 | -5.23 | -35.87 | 427 |
| 38 | Ichimoku · 1h | trend | 72.80 | -27.20 | 106 | 14.2 | -32.22 | -9.58 | -33.28 | 111 |
| 39 | Bollinger breakout · 1h | breakout | 71.56 | -28.44 | 193 | 21.8 | -32.19 | -8.74 | -35.28 | 218 |
| 40 | MFI reversion · 1h | reversion | 70.79 | -29.21 | 459 | 34.0 | -28.30 | -4.22 | -31.02 | 171 |
| 41 | Supertrend · 1h | trend | 70.74 | -29.26 | 192 | 16.7 | -32.99 | -5.52 | -39.61 | 206 |
| 42 | Triple EMA stack · 1h | trend | 69.90 | -30.10 | 158 | 14.6 | -31.56 | -6.54 | -38.09 | 177 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.34 | -4.99 | -37.91 | 31 |
| 44 | MACD zero-line · 1h | trend | 68.69 | -31.31 | 186 | 17.7 | -29.29 | -5.90 | -35.30 | 207 |
| 45 | EMA 20/50 cross · 1h | trend | 68.68 | -31.32 | 118 | 10.2 | -38.26 | -8.39 | -44.46 | 125 |
| 46 | Heikin-Ashi · 1h | trend | 68.23 | -31.77 | 479 | 23.0 | -46.85 | -10.32 | -47.72 | 627 |
| 47 | RSI momentum · 1h | momentum | 67.80 | -32.20 | 183 | 14.2 | -34.74 | -6.36 | -41.13 | 202 |
| 48 | CCI reversion · 1h | reversion | 67.51 | -32.49 | 395 | 42.0 | -42.25 | -7.09 | -44.29 | 480 |
| 49 | ROC + volume · 1h | momentum | 67.26 | -32.74 | 420 | 28.3 | -36.77 | -6.78 | -41.75 | 342 |
| 50 | MACD cross · 1h | trend | 67.14 | -32.86 | 420 | 22.1 | -40.79 | -6.63 | -46.96 | 495 |
| 51 | OBV trend · 1h | momentum | 67.01 | -32.99 | 313 | 19.5 | -35.48 | -7.81 | -40.65 | 248 |
| 52 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -38.69 | -2.35 | -57.50 | 39 |
| 53 | Donchian 20/10 · 1h | breakout | 65.24 | -34.76 | 163 | 17.8 | -36.72 | -7.20 | -42.44 | 192 |
| 54 | Williams %R · 1h | reversion | 63.28 | -36.72 | 441 | 41.0 | -46.80 | -8.19 | -47.58 | 572 |
| 55 | Bollinger reversion · 1h | reversion | 62.77 | -37.23 | 354 | 38.4 | -39.48 | -6.06 | -39.90 | 417 |
| 56 | EMA 9/21 cross · 1h | trend | 61.79 | -38.21 | 286 | 11.5 | -40.66 | -7.99 | -46.72 | 324 |
| 57 | Agent (ML meta-label) | meta | 59.36 | -40.64 | 1964 | 24.7 | -21.30 | -3.36 | -21.60 | 266 |
| 58 | RSI(14) reversion · 1h | reversion | 59.09 | -40.91 | 215 | 34.4 | -40.16 | -5.88 | -43.22 | 263 |
| 59 | Z-score reversion · 1h | reversion | 57.21 | -42.79 | 228 | 35.1 | -37.34 | -5.20 | -39.76 | 258 |
| 60 | Candlestick reversal · 1h | reversion | 55.89 | -44.11 | 568 | 27.1 | -47.11 | -8.62 | -48.51 | 649 |
| 61 | VWAP momentum · 1h | momentum | 55.41 | -44.59 | 993 | 21.9 | -57.51 | -11.72 | -60.58 | 1205 |
| 62 | Three white soldiers | momentum | 53.92 | -46.08 | 598 | 14.5 | -51.03 | -23.18 | -51.09 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.08 | -47.42 | -99.09 | 5333 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.07 | -30.32 | -83.23 | 1408 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.35 | -46.99 | -94.35 | 2477 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.57 | -35.40 | -90.66 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.00 | -46.53 | -92.02 | 2301 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.49 | -31.29 | -90.49 | 2057 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.05 | -53.03 | -98.06 | 3469 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -56.51 | -96.78 | 3404 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.84 | -36.95 | -93.84 | 2220 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.55 | -35.81 | -83.58 | 1597 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -54.86 | -99.61 | 6115 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -47.20 | -92.75 | 2559 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.79 | -39.18 | -94.83 | 3206 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -74.92 | -99.83 | 6186 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.89 | -49.27 | -92.91 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.69 | -27.14 | -77.75 | 1662 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.81 | -61.78 | -97.81 | 3408 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.07 | -57.19 | -99.08 | 4978 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.64 | -29.88 | -70.72 | 1239 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.92 | -57.29 | -94.92 | 2749 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.93 | -41.03 | -86.01 | 1741 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -72.50 | -99.71 | 6424 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.80 | -30.91 | -91.01 | 2374 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.88 | -19.00 | -80.34 | 1840 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.53 | -36.44 | -91.65 | 2169 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.67 | -47.59 | -97.68 | 3933 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.70 | -61.65 | -89.78 | 2160 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.56 | -32.08 | -67.61 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.08 | -28.59 | -74.30 | 1215 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.77 | -18.58 | -81.77 | 1763 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.59 | -46.03 | -97.59 | 4345 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -113.07 | -99.94 | 8423 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T15:55 | Agent (ML meta-label) | buy | AMZN | 4.57 | — | entry |
| 2026-11-19T15:55 | Agent (ML meta-label) | sell | MSFT | 4.25 | -0.02 | selected signal exited |
| 2026-11-19T15:55 | Williams %R · 1h | sell | IWM | 3.92 | -0.03 | stop-loss |
| 2026-11-19T15:55 | Z-score reversion · 1h | buy | MSTR | 4.11 | — | entry |
| 2026-11-19T15:55 | Z-score reversion · 1h | buy | META | 2.99 | — | rebalance up |
| 2026-11-19T15:55 | Z-score reversion · 1h | sell | IWM | 7.10 | -0.06 | stop-loss |
| 2026-11-19T15:55 | Bollinger reversion · 1h | sell | IWM | 15.91 | -0.20 | stop-loss |
| 2026-11-19T15:55 | RSI(14) reversion · 1h | buy | ETHU | 4.84 | — | rebalance up |
| 2026-11-19T15:55 | RSI(14) reversion · 1h | sell | IWM | 7.50 | -0.09 | stop-loss |
| 2026-11-19T15:51 | Agent (ML meta-label) | buy | SQQQ | 4.56 | — | following Connors RSI(2) |
| 2026-11-19T15:51 | Agent (ML meta-label) | sell | TNA | 4.27 | -0.10 | selected signal exited |
| 2026-11-19T15:51 | Agent (ML meta-label) | sell | AMD | 3.99 | -0.42 | selected signal exited |
| 2026-11-19T15:51 | MFI reversion · 1h | buy | MSTR | 4.40 | — | rebalance up |
| 2026-11-19T15:51 | MFI reversion · 1h | buy | ETHU | 4.12 | — | rebalance up |
| 2026-11-19T15:51 | MFI reversion · 1h | buy | DOGE-USD | 4.26 | — | rebalance up |
| 2026-11-19T15:51 | MFI reversion · 1h | sell | AMD | 7.14 | -0.95 | target is flat |
| 2026-11-19T15:51 | CCI reversion · 1h | buy | NVDA | 4.02 | — | rebalance up |
| 2026-11-19T15:51 | CCI reversion · 1h | buy | BITX | 5.31 | — | rebalance up |
| 2026-11-19T15:51 | CCI reversion · 1h | sell | TNA | 7.48 | -0.14 | stop-loss |
| 2026-11-19T15:51 | CCI reversion · 1h | sell | IWM | 4.17 | -0.05 | stop-loss |
| 2026-11-19T15:51 | RSI momentum · 1h | sell | SOL-USD | 17.11 | -0.49 | stop-loss |
| 2026-11-19T15:51 | ROC + volume · 1h | sell | XRP-USD | 5.60 | -0.16 | stop-loss |
| 2026-11-19T15:51 | Heikin-Ashi · 1h | sell | AMD | 16.32 | -0.91 | stop-loss |
| 2026-11-19T15:51 | ADX DI cross · 1h | sell | AMD | 4.05 | -0.27 | stop-loss |
| 2026-11-19T15:51 | MACD cross · 1h | buy | GOOGL | 2.59 | — | entry |
| 2026-11-19T15:51 | MACD cross · 1h | buy | ETH-USD | 3.19 | — | entry |
| 2026-11-19T15:51 | MACD cross · 1h | sell | AMD | 4.85 | -0.41 | stop-loss |
| 2026-11-19T15:51 | EMA 9/21 cross · 1h | buy | XRP-USD | 4.46 | — | rebalance up |
| 2026-11-19T15:51 | EMA 9/21 cross · 1h | sell | DOGE-USD | 9.66 | -0.27 | stop-loss |
| 2026-11-19T15:45 | Agent (ML meta-label) | buy | MSFT | 4.26 | — | entry |
| 2026-11-19T15:45 | Agent (ML meta-label) | sell | SQQQ | 4.40 | 0.07 | selected signal exited |
| 2026-11-19T15:45 | ROC + volume · 1h | sell | DOGE-USD | 5.65 | -0.13 | stop-loss |
| 2026-11-19T15:45 | Ichimoku · 1h | sell | XRP-USD | 18.03 | -0.46 | stop-loss |
| 2026-11-19T15:45 | MACD zero-line · 1h | buy | SOL-USD | 3.37 | — | rebalance up |
| 2026-11-19T15:40 | Candlestick reversal · 1h | buy | ETH-USD | 4.21 | — | rebalance up |
| 2026-11-19T15:40 | Candlestick reversal · 1h | sell | UPRO | 6.96 | -0.10 | stop-loss |
| 2026-11-19T15:40 | Candlestick reversal · 1h | sell | SPY | 6.99 | -0.02 | stop-loss |
| 2026-11-19T15:40 | Bollinger breakout · 1h | sell | SOL-USD | 17.82 | -0.43 | stop-loss |
| 2026-11-19T15:40 | RSI momentum · 1h | sell | XRP-USD | 16.83 | -0.51 | stop-loss |
| 2026-11-19T15:40 | ROC + volume · 1h | sell | AMD | 5.38 | -0.34 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 15:55:05.000153+00:00 -> 2026-11-19 16:05:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 15:55:05.000153+00:00 -> 2026-11-19 16:05:05.000153+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
