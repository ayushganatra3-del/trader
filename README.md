# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T19:26:05.000141+00:00 · 49999 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.31 (-11.69%)

Closed trades 150, win rate 37.3%, fees £4.30, max drawdown -12.09%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMZN | 17.58 | -0.10 |

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

Today: 32205 decisions in 2937 calls, $0.4017 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T19:26 | 8 / 16 / 6 | cash |  |
| Breezy | 2026-11-06T19:26 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-06T19:26 | 5 / 23 / 2 | MSTR 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |
| MFI reversion | SQQQ | 1.72 | +3.74% | 7 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.02 | 13.02 | 0 | — | 13.75 | 4.67 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.39 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.98 | -0.02 | 0 | — | 2.94 | 0.92 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 120 | 47.5 | -12.02 | -2.77 | -14.52 | 147 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.29 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Hold SPY | benchmark | 95.18 | -4.82 | 0 | — | -3.81 | -1.38 | -6.18 | 1 |
| 13 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.17 | -4.37 | -10.36 | 173 |
| 14 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.35 | -0.36 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 93.13 | -6.87 | 7 | 42.9 | -9.17 | -0.83 | -18.73 | 8 |
| 17 | Trend pullback · 1h | trend | 92.33 | -7.67 | 107 | 23.4 | -15.50 | -5.58 | -17.86 | 82 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 92.27 | -7.74 | 0 | — | -7.11 | -2.13 | -9.25 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 91.24 | -8.76 | 0 | — | -6.77 | -1.99 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 89.35 | -10.65 | 369 | 32.8 | -16.31 | -5.22 | -17.56 | 588 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.27 | -3.55 | -14.68 | 85 |
| 23 | Daily: Bullish score | daily | 88.49 | -11.51 | 15 | 20.0 | -5.28 | -0.70 | -16.58 | 14 |
| 24 | Hold BTC | benchmark | 88.41 | -11.59 | 1 | 0.0 | -5.40 | -0.69 | -14.09 | 1 |
| 25 | Agent | meta | 88.31 | -11.69 | 150 | 37.3 | -14.28 | -7.62 | -14.68 | 213 |
| 26 | Copy: Insider buying | copy | 88.12 | -11.88 | 40 | 37.5 | -24.01 | -4.65 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.66 | -13.34 | 166 | 27.1 | -15.08 | -3.32 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.70 | -14.30 | 71 | 14.1 | -13.54 | -2.75 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 84.24 | -15.76 | 17 | 47.1 | -33.36 | -2.12 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.05 | -15.96 | 73 | 31.5 | -18.76 | -5.60 | -19.21 | 101 |
| 31 | Opening range 15m | breakout | 82.27 | -17.73 | 458 | 29.9 | -21.26 | -6.25 | -21.40 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.03 | -17.97 | 260 | 46.9 | -26.01 | -3.83 | -29.25 | 393 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.71 | -3.67 | -21.28 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.76 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.58 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.25 | -19.75 | 2 | 0.0 | -12.29 | -1.60 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.44 | -20.56 | 173 | 18.5 | -24.77 | -4.13 | -27.04 | 261 |
| 38 | MFI reversion · 1h | reversion | 78.89 | -21.11 | 330 | 34.2 | -18.82 | -2.69 | -20.68 | 154 |
| 39 | Bollinger breakout · 1h | breakout | 77.86 | -22.14 | 166 | 23.5 | -23.51 | -4.87 | -27.12 | 247 |
| 40 | Ichimoku · 1h | trend | 77.85 | -22.15 | 94 | 14.9 | -23.33 | -4.75 | -29.43 | 126 |
| 41 | CCI reversion · 1h | reversion | 76.95 | -23.05 | 286 | 46.2 | -30.42 | -4.95 | -31.76 | 467 |
| 42 | EMA 20/50 cross · 1h | trend | 75.90 | -24.10 | 102 | 10.8 | -24.74 | -4.47 | -30.58 | 134 |
| 43 | Heikin-Ashi · 1h | trend | 75.48 | -24.52 | 391 | 23.0 | -43.20 | -9.02 | -43.54 | 675 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.41 | -5.45 | -29.20 | 211 |
| 45 | Triple EMA stack · 1h | trend | 74.25 | -25.75 | 142 | 14.8 | -29.45 | -6.18 | -33.48 | 205 |
| 46 | Supertrend · 1h | trend | 73.61 | -26.39 | 166 | 13.3 | -30.14 | -5.21 | -34.80 | 216 |
| 47 | RSI momentum · 1h | momentum | 73.44 | -26.56 | 158 | 12.7 | -28.12 | -5.32 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.44 | -26.56 | 334 | 23.1 | -36.05 | -6.37 | -38.81 | 479 |
| 49 | Z-score reversion · 1h | reversion | 73.24 | -26.76 | 161 | 36.0 | -25.51 | -3.77 | -28.33 | 234 |
| 50 | Bollinger reversion · 1h | reversion | 73.09 | -26.91 | 250 | 40.0 | -31.01 | -5.23 | -34.54 | 375 |
| 51 | Williams %R · 1h | reversion | 72.46 | -27.54 | 314 | 44.9 | -37.23 | -5.97 | -39.52 | 533 |
| 52 | Daily: Momentum burst | daily | 72.11 | -27.89 | 26 | 11.5 | -36.10 | -5.04 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.43 | -28.57 | 140 | 20.0 | -30.18 | -5.55 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 71.02 | -28.98 | 272 | 18.0 | -30.57 | -6.51 | -33.62 | 287 |
| 55 | ROC + volume · 1h | momentum | 70.17 | -29.83 | 345 | 25.5 | -37.82 | -7.35 | -38.16 | 379 |
| 56 | EMA 9/21 cross · 1h | trend | 67.43 | -32.57 | 241 | 10.0 | -40.43 | -8.32 | -40.77 | 338 |
| 57 | VWAP momentum · 1h | momentum | 67.18 | -32.82 | 776 | 22.0 | -56.08 | -12.35 | -56.11 | 1229 |
| 58 | Agent (ML meta-label) | meta | 66.57 | -33.43 | 1528 | 22.8 | -7.44 | -0.95 | -20.77 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 66.46 | -33.54 | 142 | 27.5 | -28.52 | -4.43 | -31.54 | 218 |
| 60 | Three white soldiers | momentum | 65.93 | -34.07 | 456 | 16.0 | -47.74 | -21.87 | -47.74 | 637 |
| 61 | Candlestick reversal · 1h | reversion | 65.44 | -34.56 | 405 | 28.6 | -38.66 | -7.10 | -39.14 | 572 |
| 62 | Max aggression: 1-day momentum | meta | 61.55 | -38.45 | 26 | 26.9 | -43.62 | -2.76 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -45.13 | -98.94 | 5203 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.60 | -25.42 | -80.78 | 1427 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -45.81 | -93.47 | 2506 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.21 | -31.23 | -89.33 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.81 | -38.80 | -90.88 | 2299 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.22 | -31.47 | -90.22 | 2195 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -53.23 | -97.73 | 3475 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -55.74 | -96.28 | 3386 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.84 | -33.09 | -93.84 | 2449 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.52 | -35.61 | -82.54 | 1659 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -52.92 | -99.52 | 5974 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.71 | -43.44 | -92.71 | 2599 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.68 | -36.58 | -95.68 | 3408 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -69.49 | -99.80 | 6179 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.81 | -42.28 | -91.85 | 2274 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.59 | -25.37 | -75.69 | 1586 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -59.56 | -97.72 | 3505 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -58.57 | -98.79 | 4879 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.83 | -29.24 | -69.83 | 1207 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -54.44 | -94.71 | 2746 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.17 | -37.12 | -85.23 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -67.84 | -99.64 | 6361 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.17 | -30.85 | -89.28 | 2290 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.58 | -19.33 | -77.79 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.97 | -36.72 | -91.05 | 2214 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.56 | -49.97 | -96.60 | 3870 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -53.15 | -89.53 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.55 | -28.70 | -66.55 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -24.31 | -73.78 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.08 | -17.59 | -78.59 | 1664 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -47.68 | -97.26 | 4323 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.28 | -99.93 | 8292 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T19:25 | OBV trend · 1h | sell | SQQQ | 17.64 | -0.17 | target is flat |
| 2026-11-06T19:20 | Agent (ML meta-label) | buy | LABU | 3.50 | — | entry |
| 2026-11-06T19:15 | MFI reversion · 1h | sell | ETHU | 4.63 | 0.00 | target is flat |
| 2026-11-06T19:10 | Agent (ML meta-label) | buy | MSTR | 4.37 | — | entry |
| 2026-11-06T19:10 | Agent (ML meta-label) | sell | META | 4.14 | 0.01 | selected signal exited |
| 2026-11-06T19:10 | Agent (ML meta-label) | sell | LABU | 4.13 | -0.03 | selected signal exited |
| 2026-11-06T19:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 16.88 | — | entry signal |
| 2026-11-06T19:00 | Opening range 30m | buy | LABU | 5.16 | — | rebalance up |
| 2026-11-06T19:00 | Opening range 30m | sell | SQQQ | 12.40 | -0.25 | stop-loss |
| 2026-11-06T18:55 | Three white soldiers | sell | XRP-USD | 16.39 | -0.15 | exit signal |
| 2026-11-06T18:50 | Agent (ML meta-label) | buy | LABU | 4.17 | — | entry |
| 2026-11-06T18:50 | Agent (ML meta-label) | sell | MSTR | 4.64 | -0.04 | selected signal exited |
| 2026-11-06T18:50 | Candlestick reversal · 1h | sell | LABU | 5.44 | -0.01 | target is flat |
| 2026-11-06T18:40 | Three white soldiers | sell | UPRO | 16.47 | -0.07 | target is flat |
| 2026-11-06T18:35 | Agent (aggressive) | buy | AMZN | 42.14 | — | following OBV trend |
| 2026-11-06T18:35 | Agent | buy | AMZN | 17.68 | — | following OBV trend |
| 2026-11-06T18:35 | Three white soldiers | buy | XRP-USD | 16.54 | — | entry signal |
| 2026-11-06T18:35 | Three white soldiers | buy | UPRO | 16.54 | — | entry signal |
| 2026-11-06T18:35 | Opening range 15m | buy | TSLA | 4.26 | — | rebalance up |
| 2026-11-06T18:35 | Opening range 15m | buy | TNA | 4.13 | — | rebalance up |
| 2026-11-06T18:35 | Opening range 15m | buy | PLTR | 4.36 | — | rebalance up |
| 2026-11-06T18:35 | Opening range 15m | buy | MSFT | 4.33 | — | rebalance up |
| 2026-11-06T18:35 | Opening range 15m | buy | IWM | 4.24 | — | rebalance up |
| 2026-11-06T18:35 | Opening range 15m | buy | AAPL | 4.29 | — | rebalance up |
| 2026-11-06T18:35 | Opening range 15m | sell | SQQQ | 8.98 | -0.16 | exit signal |
| 2026-11-06T18:30 | Agent (ML meta-label) | buy | DOGE-USD | 4.15 | — | following Candlestick reversal · 1h |
| 2026-11-06T18:30 | Agent (ML meta-label) | sell | MSFT | 4.15 | -0.00 | selected signal exited |
| 2026-11-06T18:30 | Candlestick reversal · 1h | buy | TSLA | 5.45 | — | entry signal |
| 2026-11-06T18:30 | Candlestick reversal · 1h | buy | LABU | 5.45 | — | entry signal |
| 2026-11-06T18:30 | Candlestick reversal · 1h | buy | ETHU | 5.45 | — | entry signal |
| 2026-11-06T18:30 | OBV trend · 1h | buy | SQQQ | 17.81 | — | entry signal |
| 2026-11-06T18:30 | OBV trend · 1h | buy | AMZN | 17.81 | — | entry |
| 2026-11-06T18:30 | VWAP momentum · 1h | buy | TNA | 7.75 | — | rebalance up |
| 2026-11-06T18:30 | VWAP momentum · 1h | buy | LABU | 8.23 | — | rebalance up |
| 2026-11-06T18:30 | VWAP momentum · 1h | buy | IWM | 7.81 | — | rebalance up |
| 2026-11-06T18:30 | VWAP momentum · 1h | buy | DOGE-USD | 7.82 | — | rebalance up |
| 2026-11-06T18:30 | VWAP momentum · 1h | buy | AAPL | 7.82 | — | rebalance up |
| 2026-11-06T18:30 | VWAP momentum · 1h | sell | UPRO | 5.53 | -0.04 | exit signal |
| 2026-11-06T18:30 | VWAP momentum · 1h | sell | TQQQ | 5.13 | -0.06 | exit signal |
| 2026-11-06T18:30 | VWAP momentum · 1h | sell | SPY | 5.62 | -0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 19:26:05.000141+00:00 -> 2026-11-06 19:36:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 19:26:05.000141+00:00 -> 2026-11-06 19:36:05.000141+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 19:26:05.000141+00:00 -> 2026-11-06 19:36:05.000141+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
