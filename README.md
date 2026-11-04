# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T18:55:05.000127+00:00 · 47489 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.73 (-10.27%)

Closed trades 144, win rate 38.2%, fees £4.01, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 27588 decisions in 2433 calls, $0.3429 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T18:55 | 2 / 7 / 21 | cash |  |
| Breezy | 2026-11-04T18:55 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-04T18:55 | 4 / 21 / 5 | MSTR 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 111.87 | 11.87 | 0 | — | 12.98 | 4.90 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.29 | 6.29 | 17 | 70.6 | 5.75 | 1.81 | -4.91 | 26 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.59 | 1.59 | 0 | — | 5.54 | 1.54 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.10 | -13.53 | 140 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.51 | -0.49 | 5 | 40.0 | 4.28 | 1.03 | -7.85 | 8 |
| 8 | Hold SPY | benchmark | 98.08 | -1.93 | 0 | — | -0.80 | -0.35 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 27 | 44.4 | -3.60 | -1.02 | -9.60 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 96.20 | -3.80 | 112 | 34.8 | 5.87 | 2.72 | -3.32 | 90 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.23 | -4.76 | 0 | — | -1.91 | -0.67 | -7.64 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.31 | -5.70 | 0 | — | -4.91 | -1.85 | -6.35 | 1 |
| 17 | Hold BTC | benchmark | 94.25 | -5.75 | 0 | — | -2.16 | -0.20 | -13.22 | 1 |
| 18 | Agent (rotation) | meta | 93.89 | -6.11 | 163 | 27.6 | -7.35 | -5.80 | -9.38 | 191 |
| 19 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.02 | -0.28 | -8.76 | 223 |
| 20 | Max aggression: 5-day momentum | meta | 91.30 | -8.70 | 16 | 43.8 | -23.75 | -1.37 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.69 | -9.31 | 103 | 22.3 | -16.69 | -6.19 | -17.97 | 79 |
| 23 | Parabolic SAR · 1h | trend | 90.34 | -9.66 | 154 | 26.6 | -14.87 | -3.34 | -19.39 | 239 |
| 24 | Agent | meta | 89.73 | -10.27 | 144 | 38.2 | -12.13 | -7.30 | -13.15 | 207 |
| 25 | Copy: Insider buying | copy | 89.48 | -10.52 | 38 | 39.5 | -21.56 | -4.34 | -23.32 | 63 |
| 26 | Opening range 30m | breakout | 89.46 | -10.54 | 355 | 33.0 | -15.54 | -5.15 | -17.21 | 591 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.31 | -3.24 | -14.15 | 84 |
| 28 | Daily: Bullish score | daily | 87.08 | -12.92 | 14 | 21.4 | -11.58 | -1.81 | -16.58 | 14 |
| 29 | Donchian 55/20 · 1h | breakout | 86.72 | -13.28 | 62 | 12.9 | -14.61 | -3.15 | -19.85 | 107 |
| 30 | Stochastic reversion · 1h | reversion | 86.65 | -13.35 | 249 | 47.8 | -20.47 | -3.89 | -24.88 | 384 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.22 | -13.78 | 1 | 0.0 | -7.61 | -1.13 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -11.94 | -3.93 | -14.77 | 95 |
| 33 | ADX DI cross · 1h | trend | 85.04 | -14.96 | 155 | 18.1 | -19.79 | -3.55 | -23.76 | 271 |
| 34 | Volume breakout · 1h | breakout | 84.89 | -15.11 | 130 | 28.5 | -13.75 | -3.13 | -18.08 | 104 |
| 35 | MFI reversion · 1h | reversion | 84.23 | -15.77 | 320 | 34.4 | -15.23 | -2.37 | -19.26 | 156 |
| 36 | Keltner breakout · 1h | breakout | 83.93 | -16.07 | 94 | 24.5 | -21.61 | -4.45 | -23.66 | 185 |
| 37 | Connors RSI(2) · 1h | reversion | 83.09 | -16.91 | 192 | 40.6 | -19.31 | -6.37 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.63 | -17.37 | 434 | 30.2 | -20.29 | -6.24 | -21.19 | 725 |
| 39 | Ichimoku · 1h | trend | 82.04 | -17.96 | 85 | 12.9 | -19.74 | -4.18 | -26.10 | 126 |
| 40 | Bollinger breakout · 1h | breakout | 81.47 | -18.53 | 148 | 25.0 | -17.87 | -3.60 | -23.94 | 251 |
| 41 | CCI reversion · 1h | reversion | 80.59 | -19.41 | 278 | 46.4 | -22.04 | -3.28 | -27.71 | 454 |
| 42 | EMA 20/50 cross · 1h | trend | 79.11 | -20.89 | 92 | 10.9 | -18.45 | -3.47 | -26.55 | 133 |
| 43 | Heikin-Ashi · 1h | trend | 79.05 | -20.95 | 372 | 22.6 | -40.07 | -8.26 | -43.76 | 673 |
| 44 | MACD zero-line · 1h | trend | 78.49 | -21.51 | 141 | 15.6 | -25.18 | -5.36 | -29.93 | 223 |
| 45 | MACD cross · 1h | trend | 78.13 | -21.86 | 310 | 22.9 | -32.26 | -6.32 | -34.38 | 472 |
| 46 | Z-score reversion · 1h | reversion | 78.09 | -21.91 | 152 | 37.5 | -15.54 | -2.28 | -23.02 | 218 |
| 47 | Supertrend · 1h | trend | 78.01 | -21.99 | 147 | 12.9 | -28.16 | -5.22 | -30.97 | 236 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.28 | -4.45 | -33.57 | 33 |
| 49 | Williams %R · 1h | reversion | 76.65 | -23.35 | 290 | 47.6 | -35.20 | -6.30 | -36.57 | 532 |
| 50 | RSI momentum · 1h | momentum | 76.61 | -23.39 | 142 | 12.0 | -28.95 | -5.65 | -31.18 | 229 |
| 51 | Bollinger reversion · 1h | reversion | 76.44 | -23.56 | 233 | 40.3 | -29.03 | -5.70 | -30.94 | 375 |
| 52 | Triple EMA stack · 1h | trend | 75.90 | -24.10 | 131 | 13.7 | -28.98 | -5.87 | -32.00 | 210 |
| 53 | OBV trend · 1h | momentum | 75.31 | -24.69 | 248 | 17.3 | -29.73 | -6.41 | -31.07 | 290 |
| 54 | Donchian 20/10 · 1h | breakout | 74.50 | -25.50 | 124 | 19.4 | -27.19 | -4.93 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.20 | -25.80 | 320 | 25.6 | -34.31 | -6.70 | -36.91 | 389 |
| 56 | RSI(14) reversion · 1h | reversion | 71.82 | -28.18 | 136 | 28.7 | -20.89 | -3.72 | -26.28 | 220 |
| 57 | Agent (ML meta-label) | meta | 70.18 | -29.82 | 1424 | 22.5 | -8.67 | -1.56 | -17.99 | 295 |
| 58 | VWAP momentum · 1h | momentum | 69.65 | -30.35 | 723 | 22.1 | -54.40 | -11.25 | -55.77 | 1223 |
| 59 | EMA 9/21 cross · 1h | trend | 69.62 | -30.38 | 225 | 9.8 | -36.84 | -7.41 | -40.23 | 343 |
| 60 | Candlestick reversal · 1h | reversion | 69.41 | -30.59 | 376 | 30.1 | -34.44 | -6.47 | -37.20 | 556 |
| 61 | Three white soldiers | momentum | 68.34 | -31.66 | 436 | 16.5 | -47.23 | -21.87 | -47.64 | 631 |
| 62 | Max aggression: 1-day momentum | meta | 66.53 | -33.47 | 24 | 29.2 | -36.00 | -2.15 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -45.14 | -98.99 | 5170 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.13 | -24.58 | -80.23 | 1421 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.43 | -43.74 | -93.43 | 2507 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -30.14 | -89.09 | 1911 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.94 | -36.23 | -91.11 | 2314 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.27 | -31.65 | -90.28 | 2198 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -50.03 | -97.74 | 3455 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.15 | -52.95 | -96.18 | 3345 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.46 | -32.50 | -93.54 | 2439 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.13 | -36.11 | -82.13 | 1649 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.69 | -99.49 | 5882 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.95 | -41.12 | -93.06 | 2601 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.58 | -36.89 | -95.58 | 3391 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -66.64 | -99.80 | 6149 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.62 | -40.56 | -91.78 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.73 | -26.37 | -74.75 | 1552 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -56.42 | -97.73 | 3503 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -59.53 | -98.70 | 4826 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.55 | -27.80 | -70.53 | 1192 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -51.37 | -94.81 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -36.21 | -84.86 | 1791 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.28 | -99.63 | 6303 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.20 | -30.03 | -88.46 | 2235 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.57 | -19.02 | -76.98 | 1709 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.55 | -36.51 | -90.56 | 2237 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -49.27 | -96.51 | 3822 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -51.34 | -89.37 | 2147 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.43 | -27.24 | -65.80 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.54 | -24.58 | -73.84 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.81 | -18.56 | -77.60 | 1616 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.96 | -51.76 | -96.98 | 4257 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.78 | -99.92 | 8198 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T18:55 | ROC + volume · 1h | buy | TQQQ | 3.83 | — | entry |
| 2026-11-04T18:55 | ROC + volume · 1h | buy | IWM | 3.91 | — | entry |
| 2026-11-04T18:55 | ROC + volume · 1h | sell | XRP-USD | 3.87 | 0.02 | stop-loss |
| 2026-11-04T18:55 | ROC + volume · 1h | sell | SOL-USD | 3.87 | -0.02 | stop-loss |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | SQQQ | 4.97 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | MSTR | 4.97 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | MSFT | 5.03 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | ETHU | 5.07 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | BITX | 5.05 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | AMZN | 5.04 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | buy | AAPL | 5.02 | — | rebalance up |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | UPRO | 5.01 | 0.00 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | TQQQ | 4.22 | -0.03 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | TNA | 6.36 | -0.04 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | SPY | 5.02 | -0.00 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | IWM | 5.02 | -0.02 | selected signal exited |
| 2026-11-04T18:50 | Agent (ML meta-label) | sell | COIN | 5.04 | 0.02 | selected signal exited |
| 2026-11-04T18:45 | Agent (ML meta-label) | sell | GOOGL | 4.48 | -0.01 | selected signal exited |
| 2026-11-04T18:45 | ADX DI cross · 1h | buy | TQQQ | 4.26 | — | entry |
| 2026-11-04T18:45 | ADX DI cross · 1h | sell | LABU | 4.26 | 0.15 | rebalance down |
| 2026-11-04T18:45 | Opening range 15m | sell | AMZN | 6.85 | -0.07 | stop-loss |
| 2026-11-04T18:40 | Agent (ML meta-label) | buy | GOOGL | 4.49 | — | entry |
| 2026-11-04T18:40 | Agent (ML meta-label) | sell | AMD | 4.49 | -0.01 | selected signal exited |
| 2026-11-04T18:40 | Three white soldiers | sell | LABU | 17.37 | 0.42 | exit signal |
| 2026-11-04T18:35 | Agent (ML meta-label) | buy | TQQQ | 4.24 | — | entry |
| 2026-11-04T18:35 | Agent (ML meta-label) | sell | QQQ | 4.24 | -0.01 | selected signal exited |
| 2026-11-04T18:35 | Copy: Insider buying | buy | PLBY | 1.15 | — | entry |
| 2026-11-04T18:35 | Copy: Insider buying | buy | MGM | 11.20 | — | entry |
| 2026-11-04T18:35 | Copy: Insider buying | sell | ACN | 12.35 | 0.78 | target is flat |
| 2026-11-04T18:30 | Day trade: Stocks in Play ORB | sell | GOOGL | 24.04 | -0.03 | target is flat |
| 2026-11-04T18:30 | Agent (ML meta-label) | buy | QQQ | 4.25 | — | entry |
| 2026-11-04T18:30 | Agent (ML meta-label) | buy | AMD | 4.49 | — | following Supertrend |
| 2026-11-04T18:30 | Agent (ML meta-label) | sell | GOOGL | 4.67 | -0.01 | selected signal exited |
| 2026-11-04T18:30 | MFI reversion · 1h | buy | SPY | 6.96 | — | rebalance up |
| 2026-11-04T18:30 | MFI reversion · 1h | buy | SOXL | 14.14 | — | entry |
| 2026-11-04T18:30 | MFI reversion · 1h | buy | AMZN | 14.14 | — | entry |
| 2026-11-04T18:30 | MFI reversion · 1h | sell | TSLA | 21.07 | -0.12 | exit signal |
| 2026-11-04T18:30 | MFI reversion · 1h | sell | LABU | 7.15 | 0.08 | rebalance down |
| 2026-11-04T18:30 | MFI reversion · 1h | sell | COIN | 7.02 | 0.02 | rebalance down |
| 2026-11-04T18:30 | Z-score reversion · 1h | sell | COIN | 10.04 | 0.45 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 18:55:05.000127+00:00 -> 2026-11-04 19:05:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 18:55:05.000127+00:00 -> 2026-11-04 19:05:05.000127+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 18:55:05.000127+00:00 -> 2026-11-04 19:05:05.000127+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
