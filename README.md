# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T17:25:05.000108+00:00 · 49899 ticks

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

Today: 23193 decisions in 2637 calls, $0.2965 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T17:25 | 5 / 14 / 11 | cash |  |
| Breezy | 2026-11-06T17:25 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-06T17:25 | 4 / 23 / 3 | MSTR 69% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.34 | 12.34 | 0 | — | 13.14 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.39 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 120 | 47.5 | -13.55 | -3.24 | -14.99 | 144 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.89 | -0.11 | 0 | — | 2.91 | 0.91 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.83 | -2.17 | 119 | 35.3 | 5.00 | 2.55 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Hold SPY | benchmark | 95.30 | -4.70 | 0 | — | -3.63 | -1.31 | -6.18 | 1 |
| 13 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.17 | -4.37 | -10.36 | 173 |
| 14 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.35 | -0.36 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 93.47 | -6.53 | 7 | 42.9 | -8.78 | -0.78 | -18.73 | 8 |
| 17 | Trend pullback · 1h | trend | 92.33 | -7.67 | 107 | 23.4 | -15.48 | -5.57 | -17.86 | 82 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 92.21 | -7.79 | 0 | — | -7.11 | -2.13 | -9.25 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 91.41 | -8.59 | 0 | — | -6.54 | -1.90 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 89.68 | -10.32 | 366 | 33.1 | -15.88 | -5.07 | -17.56 | 587 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.53 | -3.65 | -14.68 | 86 |
| 23 | Hold BTC | benchmark | 88.55 | -11.45 | 1 | 0.0 | -5.48 | -0.70 | -14.09 | 1 |
| 24 | Agent | meta | 88.41 | -11.59 | 150 | 37.3 | -14.19 | -7.55 | -14.62 | 212 |
| 25 | Daily: Bullish score | daily | 88.37 | -11.63 | 15 | 20.0 | -5.39 | -0.72 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 88.03 | -11.97 | 40 | 37.5 | -23.92 | -4.62 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.55 | -13.45 | 166 | 27.1 | -14.55 | -3.20 | -20.50 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 85.59 | -14.41 | 71 | 14.1 | -13.64 | -2.77 | -20.43 | 104 |
| 29 | Agent (aggressive) | meta | 84.28 | -15.72 | 73 | 31.5 | -18.53 | -5.51 | -19.08 | 100 |
| 30 | Max aggression: 5-day momentum | meta | 83.82 | -16.18 | 17 | 47.1 | -33.65 | -2.15 | -40.71 | 25 |
| 31 | Opening range 15m | breakout | 82.78 | -17.22 | 453 | 30.2 | -20.78 | -6.14 | -21.40 | 723 |
| 32 | Stochastic reversion · 1h | reversion | 82.24 | -17.76 | 260 | 46.9 | -25.78 | -3.77 | -29.25 | 393 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.73 | -3.67 | -21.28 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.76 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.58 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.25 | -19.75 | 2 | 0.0 | -12.24 | -1.59 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.48 | -20.52 | 172 | 18.6 | -25.42 | -4.25 | -27.04 | 264 |
| 38 | MFI reversion · 1h | reversion | 79.06 | -20.93 | 329 | 34.0 | -19.41 | -2.56 | -22.54 | 155 |
| 39 | Bollinger breakout · 1h | breakout | 77.92 | -22.08 | 166 | 23.5 | -23.50 | -4.87 | -27.04 | 247 |
| 40 | Ichimoku · 1h | trend | 77.80 | -22.20 | 94 | 14.9 | -23.38 | -4.76 | -29.43 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.16 | -22.84 | 286 | 46.2 | -29.79 | -4.84 | -31.33 | 465 |
| 42 | EMA 20/50 cross · 1h | trend | 75.83 | -24.18 | 102 | 10.8 | -24.03 | -4.34 | -30.58 | 132 |
| 43 | Heikin-Ashi · 1h | trend | 75.77 | -24.23 | 389 | 23.1 | -42.95 | -8.98 | -43.20 | 673 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.85 | -5.31 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.16 | -25.84 | 142 | 14.8 | -29.13 | -6.10 | -33.48 | 204 |
| 46 | MACD cross · 1h | trend | 73.60 | -26.40 | 334 | 23.1 | -35.86 | -6.31 | -38.81 | 475 |
| 47 | Supertrend · 1h | trend | 73.53 | -26.47 | 166 | 13.3 | -30.19 | -5.22 | -34.80 | 216 |
| 48 | Z-score reversion · 1h | reversion | 73.37 | -26.63 | 161 | 36.0 | -25.34 | -3.73 | -28.33 | 234 |
| 49 | RSI momentum · 1h | momentum | 73.36 | -26.64 | 158 | 12.7 | -28.18 | -5.33 | -32.60 | 219 |
| 50 | Bollinger reversion · 1h | reversion | 73.19 | -26.81 | 250 | 40.0 | -30.86 | -5.18 | -34.52 | 375 |
| 51 | Williams %R · 1h | reversion | 72.71 | -27.29 | 314 | 44.9 | -36.88 | -5.87 | -39.34 | 533 |
| 52 | Daily: Momentum burst | daily | 72.02 | -27.98 | 26 | 11.5 | -36.18 | -5.06 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.38 | -28.62 | 140 | 20.0 | -30.20 | -5.55 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 71.17 | -28.83 | 270 | 17.8 | -29.60 | -6.30 | -33.60 | 283 |
| 55 | ROC + volume · 1h | momentum | 70.13 | -29.87 | 345 | 25.5 | -37.88 | -7.37 | -38.11 | 380 |
| 56 | VWAP momentum · 1h | momentum | 67.57 | -32.42 | 764 | 22.4 | -55.79 | -12.30 | -55.99 | 1227 |
| 57 | EMA 9/21 cross · 1h | trend | 67.43 | -32.57 | 241 | 10.0 | -40.11 | -8.25 | -40.48 | 336 |
| 58 | Agent (ML meta-label) | meta | 66.78 | -33.22 | 1521 | 22.8 | -5.32 | -0.72 | -17.41 | 334 |
| 59 | RSI(14) reversion · 1h | reversion | 66.56 | -33.44 | 142 | 27.5 | -29.07 | -4.54 | -31.29 | 220 |
| 60 | Three white soldiers | momentum | 66.16 | -33.84 | 454 | 16.1 | -47.62 | -21.75 | -47.62 | 636 |
| 61 | Candlestick reversal · 1h | reversion | 65.68 | -34.32 | 401 | 28.7 | -38.91 | -7.13 | -39.66 | 571 |
| 62 | Max aggression: 1-day momentum | meta | 61.24 | -38.76 | 26 | 26.9 | -43.86 | -2.78 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.23 | -98.93 | 5178 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.49 | -25.56 | -80.72 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.38 | -46.58 | -93.40 | 2498 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.14 | -31.19 | -89.33 | 1905 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.80 | -39.46 | -90.87 | 2297 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.23 | -31.56 | -90.23 | 2196 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -53.71 | -97.73 | 3456 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -57.64 | -96.27 | 3378 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.72 | -33.07 | -93.75 | 2440 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.19 | -36.38 | -82.30 | 1649 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -53.42 | -99.52 | 5959 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.64 | -43.38 | -92.68 | 2595 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.67 | -36.47 | -95.69 | 3405 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -71.02 | -99.80 | 6159 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.74 | -43.27 | -91.79 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.72 | -26.76 | -75.86 | 1582 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -59.99 | -97.69 | 3486 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.79 | -59.59 | -98.79 | 4864 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.45 | -28.71 | -69.76 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.65 | -54.86 | -94.68 | 2741 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.16 | -37.13 | -85.23 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.26 | -99.65 | 6341 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.20 | -30.93 | -89.29 | 2289 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.77 | -19.54 | -77.91 | 1742 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.94 | -36.74 | -91.00 | 2220 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.61 | -51.13 | -96.62 | 3859 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.56 | -55.02 | -89.56 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.39 | -28.69 | -66.39 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.43 | -24.27 | -73.70 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.37 | -17.88 | -78.74 | 1665 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -48.25 | -97.28 | 4316 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.35 | -99.93 | 8269 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T17:15 | Agent (ML meta-label) | buy | UPRO | 4.45 | — | entry |
| 2026-11-06T17:10 | VWAP reversion · 1h | sell | NVDA | 24.89 | -0.08 | target is flat |
| 2026-11-06T17:05 | Agent (ML meta-label) | sell | IWM | 5.03 | 0.02 | selected signal exited |
| 2026-11-06T17:00 | VWAP reversion · 1h | sell | XRP-USD | 20.21 | 0.14 | exit signal |
| 2026-11-06T17:00 | OBV trend · 1h | sell | AMZN | 18.26 | 0.37 | target is flat |
| 2026-11-06T17:00 | ADX DI cross · 1h | buy | DOGE-USD | 12.31 | — | entry signal |
| 2026-11-06T17:00 | ADX DI cross · 1h | sell | META | 4.01 | 0.00 | rebalance down |
| 2026-11-06T17:00 | ADX DI cross · 1h | sell | GOOGL | 4.02 | -0.00 | rebalance down |
| 2026-11-06T17:00 | ADX DI cross · 1h | sell | AMZN | 4.13 | 0.02 | rebalance down |
| 2026-11-06T16:56 | Agent (ML meta-label) | buy | ETHU | 2.99 | — | entry |
| 2026-11-06T16:56 | Agent (ML meta-label) | sell | DOGE-USD | 2.99 | 0.00 | selected signal exited |
| 2026-11-06T16:50 | Agent (aggressive) | sell | AMZN | 42.16 | 0.04 | selected signal exited |
| 2026-11-06T16:50 | Agent | sell | AMZN | 17.71 | 0.02 | selected signal exited |
| 2026-11-06T16:30 | Stochastic reversion · 1h | buy | QQQ | 2.23 | — | entry |
| 2026-11-06T16:30 | Stochastic reversion · 1h | buy | LABU | 5.12 | — | entry |
| 2026-11-06T16:30 | Stochastic reversion · 1h | buy | ETHU | 5.12 | — | entry signal |
| 2026-11-06T16:30 | Stochastic reversion · 1h | sell | TSLA | 4.22 | 0.14 | rebalance down |
| 2026-11-06T16:30 | Stochastic reversion · 1h | sell | TNA | 4.14 | 0.10 | rebalance down |
| 2026-11-06T16:30 | Stochastic reversion · 1h | sell | AMD | 4.11 | 0.08 | rebalance down |
| 2026-11-06T16:30 | Z-score reversion · 1h | buy | UPRO | 1.95 | — | entry |
| 2026-11-06T16:30 | Z-score reversion · 1h | buy | TSLA | 4.32 | — | entry |
| 2026-11-06T16:30 | Z-score reversion · 1h | buy | TNA | 4.32 | — | entry signal |
| 2026-11-06T16:30 | Z-score reversion · 1h | buy | LABU | 4.32 | — | entry signal |
| 2026-11-06T16:30 | Z-score reversion · 1h | buy | IWM | 4.32 | — | entry signal |
| 2026-11-06T16:30 | Z-score reversion · 1h | sell | XRP-USD | 3.83 | 0.02 | rebalance down |
| 2026-11-06T16:30 | Z-score reversion · 1h | sell | SOXL | 3.74 | -0.02 | rebalance down |
| 2026-11-06T16:30 | Z-score reversion · 1h | sell | GOOGL | 3.77 | -0.01 | rebalance down |
| 2026-11-06T16:30 | Z-score reversion · 1h | sell | DOGE-USD | 3.93 | 0.04 | rebalance down |
| 2026-11-06T16:30 | Z-score reversion · 1h | sell | AMD | 3.95 | 0.08 | rebalance down |
| 2026-11-06T16:30 | Connors RSI(2) · 1h | sell | MSFT | 20.13 | -0.02 | exit signal |
| 2026-11-06T16:30 | Candlestick reversal · 1h | buy | QQQ | 4.75 | — | entry signal |
| 2026-11-06T16:30 | Candlestick reversal · 1h | buy | BITX | 5.46 | — | entry signal |
| 2026-11-06T16:30 | VWAP momentum · 1h | buy | LABU | 1.06 | — | entry signal |
| 2026-11-06T16:30 | VWAP momentum · 1h | buy | GOOGL | 4.51 | — | entry signal |
| 2026-11-06T16:30 | VWAP momentum · 1h | sell | SQQQ | 5.57 | 0.37 | exit signal |
| 2026-11-06T16:30 | Trend pullback · 1h | buy | AAPL | 23.13 | — | entry signal |
| 2026-11-06T16:30 | Heikin-Ashi · 1h | buy | TSLA | 12.66 | — | entry signal |
| 2026-11-06T16:30 | Heikin-Ashi · 1h | buy | QQQ | 12.66 | — | entry signal |
| 2026-11-06T16:30 | Heikin-Ashi · 1h | buy | PLTR | 12.66 | — | entry signal |
| 2026-11-06T16:30 | Heikin-Ashi · 1h | buy | META | 12.66 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 17:25:05.000108+00:00 -> 2026-11-06 17:35:05.000108+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 17:25:05.000108+00:00 -> 2026-11-06 17:35:05.000108+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 17:25:05.000108+00:00 -> 2026-11-06 17:35:05.000108+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
