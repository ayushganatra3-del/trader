# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T05:50:05.000114+00:00 · 66511 ticks

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
| Copy: Insider buying | 2026-11-19 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.48 · VIX 28.44 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, AMD 1.4, TSLA 1.2, SOXL 0.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 4470 decisions in 894 calls, $0.0626 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T05:50 | 2 / 3 / 0 | XRP-USD 19% |  |
| Breezy | 2026-11-20T05:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-20T05:50 | 5 / 0 / 0 | ETH-USD 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| CCI reversion | SOXL | 1.96 | +18.18% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.75 | 21.75 | 26 | 65.4 | 24.79 | 4.02 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.59 | 14.59 | 0 | — | 12.51 | 4.16 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.94 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.28 | 3.28 | 0 | — | 4.30 | 1.23 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.10 | -3.61 | -4.86 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 40 | 42.5 | -2.13 | -0.35 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.76 | -0.50 | -9.06 | 201 |
| 10 | Agent (rotation) | meta | 96.11 | -3.89 | 211 | 28.9 | -1.67 | -0.51 | -8.24 | 162 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.03 | -5.97 | 0 | — | -7.00 | -2.35 | -8.40 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.28 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.20 | -8.80 | 0 | — | -8.86 | -2.30 | -10.09 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.41 | -10.18 | 24 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 90.48 | -9.52 | 8 | 50.0 | -10.85 | -0.86 | -18.69 | 6 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.84 | -10.16 | 0 | — | -10.81 | -3.01 | -13.10 | 1 |
| 18 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.64 | -18.48 | 149 |
| 19 | Trend pullback · 1h | trend | 89.79 | -10.21 | 115 | 23.5 | -11.67 | -6.49 | -12.89 | 50 |
| 20 | Copy: Insider buying | copy | 89.32 | -10.68 | 55 | 40.0 | -6.73 | -1.27 | -14.79 | 65 |
| 21 | Daily: Bullish score | daily | 87.51 | -12.49 | 17 | 17.6 | -14.48 | -3.80 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.41 | -13.59 | 449 | 33.6 | -11.54 | -3.81 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.51 | -18.94 | 71 |
| 25 | Agent | meta | 85.36 | -14.64 | 233 | 36.9 | -13.89 | -6.32 | -16.51 | 214 |
| 26 | Agent (aggressive) | meta | 83.60 | -16.40 | 107 | 33.6 | -15.49 | -3.98 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 81.36 | -18.64 | 194 | 27.8 | -26.95 | -8.20 | -28.86 | 196 |
| 28 | Connors RSI(2) · 1h | reversion | 80.43 | -19.57 | 217 | 40.6 | -14.98 | -6.64 | -15.33 | 75 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.50 | -5.34 | -21.55 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.60 | -6.17 | -25.33 | 145 |
| 31 | Donchian 55/20 · 1h | breakout | 78.58 | -21.42 | 79 | 12.7 | -26.97 | -7.91 | -30.50 | 85 |
| 32 | Opening range 15m | breakout | 77.33 | -22.67 | 547 | 31.8 | -21.22 | -6.47 | -23.60 | 658 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 74.89 | -25.11 | 2 | 0.0 | -23.95 | -3.42 | -27.37 | 1 |
| 34 | Ichimoku · 1h | trend | 73.63 | -26.37 | 107 | 14.0 | -30.75 | -9.41 | -32.08 | 109 |
| 35 | Max aggression: 5-day momentum | meta | 73.05 | -26.95 | 22 | 40.9 | -53.15 | -3.70 | -58.33 | 21 |
| 36 | ADX DI cross · 1h | trend | 72.86 | -27.14 | 226 | 20.4 | -28.34 | -4.45 | -35.87 | 277 |
| 37 | Hold BTC | benchmark | 72.81 | -27.19 | 2 | 0.0 | -23.88 | -3.90 | -29.74 | 1 |
| 38 | Stochastic reversion · 1h | reversion | 71.26 | -28.74 | 356 | 42.1 | -36.29 | -5.49 | -36.83 | 426 |
| 39 | Triple EMA stack · 1h | trend | 70.25 | -29.75 | 161 | 14.3 | -33.09 | -8.11 | -37.24 | 170 |
| 40 | Bollinger breakout · 1h | breakout | 70.04 | -29.96 | 195 | 21.5 | -32.97 | -8.48 | -36.32 | 216 |
| 41 | Supertrend · 1h | trend | 69.89 | -30.11 | 198 | 16.7 | -33.42 | -5.57 | -39.93 | 204 |
| 42 | EMA 20/50 cross · 1h | trend | 69.54 | -30.46 | 119 | 10.1 | -38.19 | -11.62 | -40.64 | 122 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.14 | -37.91 | 31 |
| 44 | MFI reversion · 1h | reversion | 68.86 | -31.14 | 468 | 33.5 | -30.51 | -4.59 | -32.40 | 173 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -28.15 | -5.58 | -34.12 | 207 |
| 46 | Heikin-Ashi · 1h | trend | 68.11 | -31.89 | 483 | 23.0 | -46.09 | -10.17 | -47.85 | 616 |
| 47 | RSI momentum · 1h | momentum | 67.80 | -32.20 | 184 | 14.1 | -35.64 | -6.96 | -41.55 | 202 |
| 48 | OBV trend · 1h | momentum | 67.74 | -32.26 | 315 | 19.4 | -35.75 | -7.96 | -41.22 | 240 |
| 49 | CCI reversion · 1h | reversion | 66.40 | -33.60 | 398 | 42.0 | -41.95 | -6.93 | -44.29 | 482 |
| 50 | Max aggression: 1-day momentum | meta | 65.56 | -34.44 | 33 | 27.3 | -47.44 | -3.22 | -57.50 | 38 |
| 51 | ROC + volume · 1h | momentum | 64.82 | -35.18 | 431 | 27.6 | -38.27 | -6.67 | -43.63 | 341 |
| 52 | MACD cross · 1h | trend | 64.81 | -35.19 | 431 | 21.6 | -47.92 | -9.40 | -48.26 | 491 |
| 53 | Donchian 20/10 · 1h | breakout | 64.63 | -35.37 | 165 | 17.6 | -37.12 | -7.15 | -43.26 | 192 |
| 54 | EMA 9/21 cross · 1h | trend | 62.10 | -37.90 | 291 | 11.3 | -40.95 | -7.94 | -47.32 | 323 |
| 55 | Bollinger reversion · 1h | reversion | 61.74 | -38.26 | 358 | 38.0 | -39.89 | -6.05 | -41.37 | 422 |
| 56 | Williams %R · 1h | reversion | 61.25 | -38.75 | 448 | 40.4 | -48.65 | -8.55 | -48.80 | 579 |
| 57 | Agent (ML meta-label) | meta | 57.99 | -42.01 | 1995 | 24.7 | -26.29 | -4.65 | -27.85 | 296 |
| 58 | RSI(14) reversion · 1h | reversion | 57.87 | -42.13 | 219 | 33.8 | -41.14 | -5.96 | -43.68 | 274 |
| 59 | Z-score reversion · 1h | reversion | 55.40 | -44.60 | 233 | 34.3 | -39.39 | -5.47 | -42.29 | 262 |
| 60 | Candlestick reversal · 1h | reversion | 54.48 | -45.52 | 582 | 26.6 | -49.36 | -9.10 | -49.71 | 672 |
| 61 | VWAP momentum · 1h | momentum | 54.17 | -45.83 | 1006 | 21.6 | -56.92 | -11.41 | -60.64 | 1191 |
| 62 | Three white soldiers | momentum | 52.86 | -47.14 | 609 | 14.3 | -51.52 | -22.69 | -51.52 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -47.56 | -99.14 | 5335 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.17 | -29.68 | -83.62 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.34 | -44.91 | -94.36 | 2456 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.76 | -34.74 | -90.79 | 1942 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.03 | -43.15 | -92.12 | 2287 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.13 | -28.63 | -90.21 | 2022 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -49.90 | -98.18 | 3488 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -50.88 | -96.79 | 3393 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.79 | -38.07 | -93.80 | 2215 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.38 | -34.35 | -83.51 | 1577 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.64 | -55.28 | -99.64 | 6232 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.82 | -44.93 | -92.84 | 2527 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.58 | -35.91 | -94.64 | 3161 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -69.06 | -99.83 | 6237 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.28 | -46.64 | -93.28 | 2279 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.52 | -25.20 | -78.52 | 1634 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.84 | -58.39 | -97.85 | 3385 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.09 | -55.41 | -99.10 | 5026 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.62 | -29.01 | -70.74 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.88 | -54.39 | -94.88 | 2719 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.90 | -38.57 | -85.91 | 1705 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -68.23 | -99.72 | 6470 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.07 | -31.09 | -91.15 | 2407 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.35 | -19.11 | -80.43 | 1875 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.84 | -37.13 | -91.88 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.70 | -45.46 | -97.72 | 3975 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.29 | -53.80 | -90.30 | 2184 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.81 | -32.15 | -67.84 | 800 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.41 | -28.42 | -74.67 | 1207 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.35 | -18.52 | -82.58 | 1800 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.60 | -45.05 | -97.61 | 4370 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -100.84 | -99.94 | 8414 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T05:00 | VWAP momentum · 1h | sell | BTC-USD | 13.34 | -0.26 | exit signal |
| 2026-11-20T04:36 | MFI reversion · 1h | buy | XRP-USD | 2.90 | — | rebalance up |
| 2026-11-20T04:36 | MFI reversion · 1h | buy | BTC-USD | 5.72 | — | rebalance up |
| 2026-11-20T04:36 | MFI reversion · 1h | sell | ETH-USD | 8.63 | -0.29 | stop-loss |
| 2026-11-20T04:00 | Candlestick reversal · 1h | buy | XRP-USD | 5.94 | — | entry signal |
| 2026-11-20T04:00 | VWAP momentum · 1h | buy | XRP-USD | 13.58 | — | entry signal |
| 2026-11-20T03:00 | VWAP momentum · 1h | buy | BTC-USD | 13.60 | — | entry signal |
| 2026-11-20T02:30 | Bollinger reversion · 1h | buy | XRP-USD | 2.73 | — | entry |
| 2026-11-20T02:30 | Bollinger reversion · 1h | buy | SOL-USD | 5.92 | — | rebalance up |
| 2026-11-20T02:30 | Bollinger reversion · 1h | sell | DOGE-USD | 8.65 | -0.23 | stop-loss |
| 2026-11-20T02:10 | Williams %R · 1h | buy | BTC-USD | 3.41 | — | entry |
| 2026-11-20T02:10 | Williams %R · 1h | sell | DOGE-USD | 3.34 | -0.11 | stop-loss |
| 2026-11-20T02:00 | Candlestick reversal · 1h | sell | XRP-USD | 1.00 | -0.01 | exit signal |
| 2026-11-20T02:00 | Candlestick reversal · 1h | sell | ETH-USD | 4.94 | -0.02 | exit signal |
| 2026-11-20T02:00 | VWAP momentum · 1h | sell | BTC-USD | 13.44 | -0.21 | exit signal |
| 2026-11-20T01:55 | MFI reversion · 1h | buy | XRP-USD | 6.03 | — | rebalance up |
| 2026-11-20T01:55 | MFI reversion · 1h | buy | BTC-USD | 3.88 | — | rebalance up |
| 2026-11-20T01:55 | MFI reversion · 1h | sell | DOGE-USD | 9.91 | -0.25 | stop-loss |
| 2026-11-20T01:55 | Candlestick reversal · 1h | buy | XRP-USD | 1.01 | — | entry |
| 2026-11-20T01:55 | Candlestick reversal · 1h | buy | ETH-USD | 4.96 | — | entry |
| 2026-11-20T01:55 | Candlestick reversal · 1h | sell | DOGE-USD | 5.34 | -0.12 | stop-loss |
| 2026-11-20T01:01 | VWAP momentum · 1h | buy | BTC-USD | 13.66 | — | entry signal |
| 2026-11-20T00:00 | Max aggression: 5-day momentum | buy | SOL-USD | 73.75 | — | entry |
| 2026-11-20T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 5.47 | — | entry signal |
| 2026-11-19T23:10 | Three white soldiers | sell | DOGE-USD | 13.12 | -0.12 | exit signal |
| 2026-11-19T23:00 | MFI reversion · 1h | buy | XRP-USD | 2.48 | — | entry signal |
| 2026-11-19T23:00 | MFI reversion · 1h | buy | BTC-USD | 7.69 | — | entry signal |
| 2026-11-19T23:00 | Stochastic reversion · 1h | buy | XRP-USD | 6.48 | — | entry signal |
| 2026-11-19T23:00 | Z-score reversion · 1h | buy | BTC-USD | 5.53 | — | entry signal |
| 2026-11-19T23:00 | Bollinger reversion · 1h | buy | SOL-USD | 4.45 | — | entry signal |
| 2026-11-19T23:00 | Bollinger reversion · 1h | buy | ETH-USD | 8.89 | — | entry signal |
| 2026-11-19T23:00 | Bollinger reversion · 1h | buy | DOGE-USD | 8.89 | — | entry signal |
| 2026-11-19T23:00 | Bollinger reversion · 1h | buy | BTC-USD | 8.89 | — | entry signal |
| 2026-11-19T22:36 | Three white soldiers | buy | DOGE-USD | 13.24 | — | entry signal |
| 2026-11-19T22:00 | Candlestick reversal · 1h | sell | ETH-USD | 6.10 | -0.16 | time stop |
| 2026-11-19T22:00 | Supertrend · 1h | sell | SOL-USD | 17.04 | -0.71 | exit signal |
| 2026-11-19T22:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 16.87 | -0.41 | exit signal |
| 2026-11-19T21:00 | Supertrend · 1h | sell | ETH-USD | 17.34 | -0.47 | exit signal |
| 2026-11-19T20:55 | Agent (rotation) | sell | SQQQ | 33.96 | 2.89 | selected signal exited |
| 2026-11-19T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 99.63 | 1.04 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 05:50:05.000114+00:00 -> 2026-11-20 06:00:05.000114+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
