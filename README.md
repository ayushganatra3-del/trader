# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T16:55:05.000137+00:00 · 49871 ticks

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

Today: 20664 decisions in 2553 calls, $0.2669 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T16:55 | 5 / 20 / 5 | TNA 14%, LABU 14% |  |
| Breezy | 2026-11-06T16:55 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-06T16:55 | 4 / 24 / 2 | BITX 70% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.27 | 12.27 | 0 | — | 13.07 | 4.45 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.39 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.01 | 0.01 | 0 | — | 3.04 | 0.95 | -6.60 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.01 | 0.01 | 118 | 47.5 | -11.69 | -2.66 | -14.46 | 148 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.02 | -1.98 | 119 | 35.3 | 5.21 | 2.64 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Hold SPY | benchmark | 95.46 | -4.54 | 0 | — | -3.47 | -1.24 | -6.18 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 13 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.17 | -4.37 | -10.36 | 173 |
| 14 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.35 | -0.36 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 94.04 | -5.96 | 7 | 42.9 | -8.22 | -0.70 | -18.73 | 8 |
| 17 | Trend pullback · 1h | trend | 92.48 | -7.52 | 107 | 23.4 | -15.34 | -5.51 | -17.86 | 82 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.35 | -8.64 | 0 | — | -6.60 | -1.92 | -10.64 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 91.30 | -8.70 | 0 | — | -8.02 | -2.46 | -9.25 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 89.92 | -10.08 | 366 | 33.1 | -15.69 | -4.99 | -17.56 | 587 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.53 | -3.65 | -14.68 | 86 |
| 23 | Hold BTC | benchmark | 88.64 | -11.37 | 1 | 0.0 | -5.52 | -0.71 | -14.09 | 1 |
| 24 | Agent | meta | 88.41 | -11.59 | 150 | 37.3 | -14.19 | -7.55 | -14.62 | 212 |
| 25 | Daily: Bullish score | daily | 88.19 | -11.81 | 15 | 20.0 | -5.56 | -0.75 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 87.72 | -12.28 | 40 | 37.5 | -24.13 | -4.69 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.40 | -13.60 | 166 | 27.1 | -15.33 | -3.37 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.43 | -14.57 | 71 | 14.1 | -13.79 | -2.80 | -20.43 | 104 |
| 29 | Agent (aggressive) | meta | 84.28 | -15.72 | 73 | 31.5 | -18.53 | -5.51 | -19.08 | 100 |
| 30 | Max aggression: 5-day momentum | meta | 83.22 | -16.78 | 17 | 47.1 | -34.13 | -2.19 | -40.71 | 25 |
| 31 | Opening range 15m | breakout | 82.97 | -17.03 | 453 | 30.2 | -20.60 | -6.09 | -21.40 | 723 |
| 32 | Stochastic reversion · 1h | reversion | 82.44 | -17.56 | 260 | 46.9 | -25.55 | -3.71 | -29.25 | 393 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.71 | -3.67 | -21.28 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.76 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.58 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 79.93 | -20.07 | 2 | 0.0 | -12.59 | -1.65 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.62 | -20.38 | 172 | 18.6 | -25.05 | -4.19 | -27.04 | 265 |
| 38 | MFI reversion · 1h | reversion | 79.35 | -20.65 | 329 | 34.0 | -19.10 | -2.50 | -22.54 | 154 |
| 39 | Bollinger breakout · 1h | breakout | 78.04 | -21.96 | 166 | 23.5 | -23.30 | -4.83 | -27.04 | 247 |
| 40 | Ichimoku · 1h | trend | 77.66 | -22.34 | 94 | 14.9 | -23.51 | -4.79 | -29.43 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.41 | -22.59 | 286 | 46.2 | -29.97 | -4.86 | -31.70 | 466 |
| 42 | Heikin-Ashi · 1h | trend | 75.97 | -24.03 | 389 | 23.1 | -42.81 | -8.94 | -43.20 | 673 |
| 43 | EMA 20/50 cross · 1h | trend | 75.71 | -24.29 | 102 | 10.8 | -24.38 | -4.40 | -30.58 | 132 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.12 | -5.38 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.02 | -25.98 | 142 | 14.8 | -29.66 | -6.22 | -33.48 | 206 |
| 46 | MACD cross · 1h | trend | 73.71 | -26.29 | 334 | 23.1 | -36.01 | -6.36 | -38.81 | 478 |
| 47 | Z-score reversion · 1h | reversion | 73.59 | -26.41 | 161 | 36.0 | -25.09 | -3.67 | -28.33 | 234 |
| 48 | Supertrend · 1h | trend | 73.49 | -26.51 | 166 | 13.3 | -30.65 | -5.32 | -34.80 | 217 |
| 49 | Bollinger reversion · 1h | reversion | 73.40 | -26.60 | 250 | 40.0 | -30.64 | -5.09 | -34.54 | 375 |
| 50 | RSI momentum · 1h | momentum | 73.33 | -26.67 | 158 | 12.7 | -28.22 | -5.34 | -32.60 | 219 |
| 51 | Williams %R · 1h | reversion | 72.92 | -27.08 | 314 | 44.9 | -37.12 | -5.89 | -39.72 | 533 |
| 52 | Daily: Momentum burst | daily | 71.89 | -28.11 | 26 | 11.5 | -36.29 | -5.08 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.31 | -28.69 | 140 | 20.0 | -30.28 | -5.57 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 71.19 | -28.81 | 269 | 17.5 | -30.96 | -6.56 | -33.83 | 289 |
| 55 | ROC + volume · 1h | momentum | 70.12 | -29.88 | 345 | 25.5 | -38.09 | -7.42 | -38.21 | 380 |
| 56 | VWAP momentum · 1h | momentum | 67.76 | -32.24 | 764 | 22.4 | -55.86 | -12.34 | -56.18 | 1228 |
| 57 | EMA 9/21 cross · 1h | trend | 67.40 | -32.60 | 241 | 10.0 | -40.20 | -8.25 | -40.58 | 337 |
| 58 | Agent (ML meta-label) | meta | 66.90 | -33.10 | 1519 | 22.7 | -11.48 | -1.57 | -22.59 | 331 |
| 59 | RSI(14) reversion · 1h | reversion | 66.74 | -33.26 | 142 | 27.5 | -28.16 | -4.36 | -31.29 | 216 |
| 60 | Three white soldiers | momentum | 66.16 | -33.84 | 454 | 16.1 | -47.62 | -21.75 | -47.62 | 636 |
| 61 | Candlestick reversal · 1h | reversion | 65.77 | -34.23 | 401 | 28.7 | -37.72 | -6.84 | -38.72 | 565 |
| 62 | Max aggression: 1-day momentum | meta | 60.80 | -39.20 | 26 | 26.9 | -44.26 | -2.81 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.62 | -98.94 | 5178 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.45 | -25.62 | -80.72 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.38 | -47.11 | -93.42 | 2496 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.11 | -31.10 | -89.33 | 1905 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.77 | -39.42 | -90.87 | 2297 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.20 | -31.42 | -90.21 | 2196 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -53.28 | -97.72 | 3452 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.25 | -58.02 | -96.26 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.73 | -32.99 | -93.74 | 2439 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.16 | -36.55 | -82.30 | 1641 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -53.26 | -99.52 | 5957 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.62 | -43.34 | -92.68 | 2595 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.68 | -36.58 | -95.69 | 3407 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.35 | -99.80 | 6157 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.71 | -43.19 | -91.79 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.58 | -26.71 | -75.72 | 1579 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -60.38 | -97.69 | 3486 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.79 | -59.58 | -98.79 | 4862 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.44 | -28.70 | -69.77 | 1206 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -54.85 | -94.68 | 2741 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.16 | -37.12 | -85.16 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.29 | -99.65 | 6339 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.22 | -30.96 | -89.29 | 2289 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.84 | -19.61 | -77.91 | 1742 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.98 | -36.50 | -91.07 | 2229 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.61 | -51.13 | -96.62 | 3858 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.52 | -54.85 | -89.52 | 2164 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.33 | -28.66 | -66.33 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.43 | -24.35 | -73.70 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.29 | -17.79 | -78.71 | 1664 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -48.34 | -97.28 | 4312 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -99.85 | -99.93 | 8266 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-06T16:30 | Heikin-Ashi · 1h | buy | GOOGL | 12.66 | — | entry signal |
| 2026-11-06T16:30 | Heikin-Ashi · 1h | buy | AMD | 12.66 | — | entry signal |
| 2026-11-06T16:30 | ADX DI cross · 1h | buy | META | 19.92 | — | entry signal |
| 2026-11-06T16:30 | Gap and go | sell | TSLA | 24.00 | 0.43 | target is flat |
| 2026-11-06T16:21 | Agent (ML meta-label) | buy | DOGE-USD | 2.99 | — | entry |
| 2026-11-06T16:10 | Agent (ML meta-label) | sell | DOGE-USD | 2.99 | -0.03 | selected signal exited |
| 2026-11-06T16:10 | Gap and go | sell | TQQQ | 23.25 | -0.19 | exit signal |
| 2026-11-06T16:10 | Gap and go | sell | QQQ | 23.55 | -0.08 | exit signal |
| 2026-11-06T16:06 | Agent (ML meta-label) | buy | DOGE-USD | 3.02 | — | entry |
| 2026-11-06T16:00 | Agent | sell | DOGE-USD | 17.64 | -0.07 | selected signal exited |
| 2026-11-06T16:00 | Candlestick reversal · 1h | buy | BTC-USD | 6.56 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 16:55:05.000137+00:00 -> 2026-11-06 17:05:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 16:55:05.000137+00:00 -> 2026-11-06 17:05:05.000137+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 16:55:05.000137+00:00 -> 2026-11-06 17:05:05.000137+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
