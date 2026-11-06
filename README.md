# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T17:55:05.000153+00:00 · 49921 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.41 (-11.59%)

Closed trades 150, win rate 37.3%, fees £4.29, max drawdown -11.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-05)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 38.26 · VIX 28.18 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, AMZN 5.2, AAPL 5.0, MSFT 4.9, TSLA 1.2, MSTR 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 25197 decisions in 2703 calls, $0.3199 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T17:55 | 4 / 13 / 13 | cash |  |
| Breezy | 2026-11-06T17:55 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-06T17:55 | 6 / 19 / 5 | BITX 56% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.31 | 12.31 | 0 | — | 13.20 | 4.49 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.39 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 120 | 47.5 | -13.21 | -3.13 | -14.84 | 145 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.69 | -0.31 | 0 | — | 2.79 | 0.88 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.50 | 2.29 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.17 | -4.37 | -10.36 | 173 |
| 13 | Hold SPY | benchmark | 94.77 | -5.23 | 0 | — | -4.09 | -1.50 | -6.18 | 1 |
| 14 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.35 | -0.36 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Trend pullback · 1h | trend | 92.19 | -7.82 | 107 | 23.4 | -15.58 | -5.61 | -17.86 | 82 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.13 | -7.87 | 0 | — | -7.11 | -2.13 | -9.25 | 1 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.44 | -8.56 | 7 | 42.9 | -10.69 | -1.05 | -18.73 | 8 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 91.02 | -8.98 | 0 | — | -6.87 | -2.02 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.18 | -10.81 | 368 | 32.9 | -16.31 | -5.22 | -17.56 | 588 |
| 22 | Daily: Bullish score | daily | 88.91 | -11.09 | 15 | 20.0 | -4.84 | -0.63 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.52 | -3.64 | -14.68 | 86 |
| 24 | Agent | meta | 88.41 | -11.59 | 150 | 37.3 | -14.19 | -7.55 | -14.62 | 212 |
| 25 | Hold BTC | benchmark | 88.11 | -11.89 | 1 | 0.0 | -5.92 | -0.77 | -14.09 | 1 |
| 26 | Copy: Insider buying | copy | 87.68 | -12.32 | 40 | 37.5 | -24.22 | -4.71 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 87.04 | -12.96 | 166 | 27.1 | -14.72 | -3.24 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 86.08 | -13.92 | 71 | 14.1 | -13.14 | -2.67 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.69 | -14.31 | 17 | 47.1 | -32.12 | -2.01 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.28 | -15.72 | 73 | 31.5 | -18.53 | -5.51 | -19.08 | 100 |
| 31 | Opening range 15m | breakout | 82.24 | -17.76 | 457 | 30.0 | -21.25 | -6.25 | -21.40 | 724 |
| 32 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.73 | -3.67 | -21.28 | 100 |
| 33 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.76 | -21.05 | 129 |
| 34 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.51 | -4.64 | -24.50 | 173 |
| 35 | Stochastic reversion · 1h | reversion | 80.69 | -19.31 | 260 | 46.9 | -26.90 | -4.06 | -29.25 | 393 |
| 36 | ADX DI cross · 1h | trend | 79.55 | -20.45 | 172 | 18.6 | -25.20 | -4.20 | -27.04 | 263 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 79.40 | -20.60 | 2 | 0.0 | -13.10 | -1.74 | -24.16 | 1 |
| 38 | Ichimoku · 1h | trend | 78.23 | -21.77 | 94 | 14.9 | -22.94 | -4.67 | -29.43 | 125 |
| 39 | MFI reversion · 1h | reversion | 78.14 | -21.86 | 329 | 34.0 | -20.32 | -2.72 | -22.54 | 156 |
| 40 | Bollinger breakout · 1h | breakout | 77.66 | -22.34 | 166 | 23.5 | -23.72 | -4.91 | -27.12 | 247 |
| 41 | EMA 20/50 cross · 1h | trend | 76.18 | -23.82 | 102 | 10.8 | -23.59 | -4.26 | -30.58 | 132 |
| 42 | CCI reversion · 1h | reversion | 75.94 | -24.06 | 286 | 46.2 | -30.74 | -5.00 | -31.36 | 466 |
| 43 | Heikin-Ashi · 1h | trend | 75.00 | -25.00 | 389 | 23.1 | -43.46 | -9.07 | -43.54 | 674 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.85 | -5.31 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.57 | -25.43 | 142 | 14.8 | -28.72 | -6.01 | -33.48 | 204 |
| 46 | Supertrend · 1h | trend | 73.79 | -26.21 | 166 | 13.3 | -30.64 | -5.32 | -34.80 | 218 |
| 47 | RSI momentum · 1h | momentum | 73.69 | -26.31 | 158 | 12.7 | -27.83 | -5.26 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.15 | -26.85 | 334 | 23.1 | -36.23 | -6.39 | -38.81 | 478 |
| 49 | Z-score reversion · 1h | reversion | 72.43 | -27.57 | 161 | 36.0 | -26.29 | -3.96 | -28.33 | 234 |
| 50 | Daily: Momentum burst | daily | 72.42 | -27.58 | 26 | 11.5 | -35.81 | -4.99 | -38.31 | 31 |
| 51 | Bollinger reversion · 1h | reversion | 72.21 | -27.79 | 250 | 40.0 | -31.89 | -5.56 | -34.52 | 375 |
| 52 | Donchian 20/10 · 1h | breakout | 71.63 | -28.37 | 140 | 20.0 | -29.93 | -5.50 | -34.69 | 213 |
| 53 | Williams %R · 1h | reversion | 71.39 | -28.61 | 314 | 44.9 | -37.80 | -6.17 | -39.34 | 535 |
| 54 | OBV trend · 1h | momentum | 71.23 | -28.77 | 271 | 18.1 | -29.60 | -6.30 | -33.60 | 283 |
| 55 | ROC + volume · 1h | momentum | 70.29 | -29.71 | 345 | 25.5 | -37.75 | -7.34 | -38.16 | 380 |
| 56 | EMA 9/21 cross · 1h | trend | 67.73 | -32.27 | 241 | 10.0 | -39.81 | -8.17 | -40.48 | 336 |
| 57 | VWAP momentum · 1h | momentum | 67.01 | -32.99 | 768 | 22.3 | -56.14 | -12.36 | -56.14 | 1228 |
| 58 | Agent (ML meta-label) | meta | 66.17 | -33.83 | 1521 | 22.8 | -8.58 | -1.22 | -19.62 | 328 |
| 59 | Three white soldiers | momentum | 66.16 | -33.84 | 454 | 16.1 | -47.62 | -21.75 | -47.62 | 636 |
| 60 | RSI(14) reversion · 1h | reversion | 65.88 | -34.12 | 142 | 27.5 | -29.82 | -4.68 | -31.54 | 220 |
| 61 | Candlestick reversal · 1h | reversion | 65.08 | -34.92 | 402 | 28.9 | -39.34 | -7.27 | -39.52 | 572 |
| 62 | Max aggression: 1-day momentum | meta | 62.61 | -37.39 | 26 | 26.9 | -42.56 | -2.66 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -45.40 | -98.94 | 5181 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.67 | -25.54 | -80.80 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -46.14 | -93.44 | 2497 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.51 | -89.33 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.82 | -39.15 | -90.86 | 2296 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.26 | -31.66 | -90.26 | 2196 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -53.46 | -97.73 | 3456 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -56.18 | -96.28 | 3376 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -33.20 | -93.77 | 2445 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.41 | -35.88 | -82.45 | 1649 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -52.85 | -99.52 | 5959 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.69 | -43.44 | -92.69 | 2596 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.69 | -36.64 | -95.69 | 3407 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -69.78 | -99.80 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -43.30 | -91.81 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.68 | -26.57 | -75.87 | 1584 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -59.99 | -97.72 | 3488 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.80 | -59.80 | -98.80 | 4864 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.62 | -28.97 | -69.77 | 1206 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -54.66 | -94.68 | 2741 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.17 | -37.11 | -85.23 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -70.35 | -99.65 | 6348 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.22 | -30.98 | -89.29 | 2289 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.74 | -19.50 | -77.86 | 1741 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.08 | -37.20 | -91.08 | 2225 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.62 | -51.45 | -96.63 | 3864 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.54 | -54.43 | -89.54 | 2165 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.24 | -28.62 | -66.30 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.62 | -24.33 | -73.77 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.67 | -18.11 | -78.78 | 1667 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -48.24 | -97.27 | 4320 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.46 | -99.93 | 8272 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T17:55 | Day trade: Stocks in Play ORB | sell | UPRO | 24.21 | -0.23 | target is flat |
| 2026-11-06T17:55 | Day trade: Stocks in Play ORB | sell | SPY | 24.34 | -0.11 | target is flat |
| 2026-11-06T17:55 | Opening range 30m | buy | SQQQ | 12.65 | — | entry |
| 2026-11-06T17:55 | Opening range 30m | sell | AMZN | 12.65 | -0.14 | stop-loss |
| 2026-11-06T17:55 | Opening range 15m | sell | AMZN | 7.43 | -0.08 | stop-loss |
| 2026-11-06T17:50 | Opening range 15m | buy | SQQQ | 9.14 | — | entry signal |
| 2026-11-06T17:50 | Opening range 15m | sell | UPRO | 7.38 | -0.11 | stop-loss |
| 2026-11-06T17:50 | Opening range 15m | sell | SPY | 7.46 | -0.04 | stop-loss |
| 2026-11-06T17:45 | Stochastic reversion · 1h | buy | SPY | 4.05 | — | entry |
| 2026-11-06T17:45 | Stochastic reversion · 1h | sell | IWM | 4.05 | 0.03 | rebalance down |
| 2026-11-06T17:40 | ADX DI cross · 1h | sell | SQQQ | 4.02 | -0.01 | rebalance down |
| 2026-11-06T17:40 | Opening range 30m | buy | LABU | 9.69 | — | entry |
| 2026-11-06T17:40 | Opening range 30m | sell | META | 9.69 | -0.12 | stop-loss |
| 2026-11-06T17:40 | Opening range 15m | sell | META | 7.42 | -0.08 | stop-loss |
| 2026-11-06T17:35 | OBV trend · 1h | sell | SQQQ | 17.86 | 0.07 | target is flat |
| 2026-11-06T17:30 | MFI reversion · 1h | buy | ETHU | 4.63 | — | entry signal |
| 2026-11-06T17:30 | MFI reversion · 1h | sell | DOGE-USD | 4.63 | 0.04 | rebalance down |
| 2026-11-06T17:30 | Candlestick reversal · 1h | sell | TSLA | 5.56 | 0.15 | exit signal |
| 2026-11-06T17:30 | OBV trend · 1h | buy | SQQQ | 17.79 | — | entry signal |
| 2026-11-06T17:30 | VWAP momentum · 1h | buy | XRP-USD | 1.63 | — | entry |
| 2026-11-06T17:30 | VWAP momentum · 1h | buy | TQQQ | 5.19 | — | entry |
| 2026-11-06T17:30 | VWAP momentum · 1h | buy | QQQ | 5.19 | — | entry |
| 2026-11-06T17:30 | VWAP momentum · 1h | buy | MSFT | 5.19 | — | entry signal |
| 2026-11-06T17:30 | VWAP momentum · 1h | buy | LABU | 4.12 | — | rebalance up |
| 2026-11-06T17:30 | VWAP momentum · 1h | sell | TSLA | 5.61 | -0.02 | exit signal |
| 2026-11-06T17:30 | VWAP momentum · 1h | sell | META | 5.62 | -0.01 | exit signal |
| 2026-11-06T17:30 | VWAP momentum · 1h | sell | GOOGL | 4.48 | -0.02 | exit signal |
| 2026-11-06T17:30 | VWAP momentum · 1h | sell | AMZN | 5.61 | -0.02 | exit signal |
| 2026-11-06T17:30 | MACD cross · 1h | buy | TSLA | 4.57 | — | entry signal |
| 2026-11-06T17:30 | MACD cross · 1h | buy | PLTR | 6.68 | — | entry |
| 2026-11-06T17:30 | MACD cross · 1h | buy | META | 6.68 | — | entry signal |
| 2026-11-06T17:30 | MACD cross · 1h | buy | AMD | 6.68 | — | entry signal |
| 2026-11-06T17:30 | MACD cross · 1h | sell | XRP-USD | 5.52 | -0.05 | rebalance down |
| 2026-11-06T17:30 | MACD cross · 1h | sell | SOL-USD | 3.77 | 0.02 | rebalance down |
| 2026-11-06T17:30 | MACD cross · 1h | sell | GOOGL | 3.80 | -0.01 | rebalance down |
| 2026-11-06T17:30 | MACD cross · 1h | sell | ETH-USD | 3.86 | -0.01 | rebalance down |
| 2026-11-06T17:30 | MACD cross · 1h | sell | DOGE-USD | 3.82 | 0.06 | rebalance down |
| 2026-11-06T17:30 | MACD cross · 1h | sell | BTC-USD | 3.84 | 0.00 | rebalance down |
| 2026-11-06T17:15 | Agent (ML meta-label) | buy | UPRO | 4.45 | — | entry |
| 2026-11-06T17:10 | VWAP reversion · 1h | sell | NVDA | 24.89 | -0.08 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 17:55:05.000153+00:00 -> 2026-11-06 18:05:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 17:55:05.000153+00:00 -> 2026-11-06 18:05:05.000153+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 17:55:05.000153+00:00 -> 2026-11-06 18:05:05.000153+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
