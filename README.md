# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T18:26:05.000132+00:00 · 49942 ticks

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

Today: 27069 decisions in 2766 calls, $0.3418 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T18:26 | 6 / 14 / 9 | TNA 15% |  |
| Breezy | 2026-11-06T18:26 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-11-06T18:26 | 5 / 21 / 3 | COIN 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |
| Candlestick reversal · 1h | DOGE-USD | 1.64 | +5.59% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.56 | 12.56 | 0 | — | 13.46 | 4.58 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.39 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 120 | 47.5 | -13.55 | -3.24 | -14.99 | 144 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.74 | -0.26 | 0 | — | 2.84 | 0.89 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.29 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.17 | -4.37 | -10.36 | 173 |
| 13 | Hold SPY | benchmark | 94.89 | -5.11 | 0 | — | -3.97 | -1.45 | -6.18 | 1 |
| 14 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.35 | -0.36 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Trend pullback · 1h | trend | 92.26 | -7.74 | 107 | 23.4 | -15.51 | -5.58 | -17.86 | 82 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.13 | -7.87 | 0 | — | -7.11 | -2.13 | -9.25 | 1 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 91.97 | -8.03 | 7 | 42.9 | -10.18 | -0.98 | -18.73 | 8 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.94 | -9.06 | 0 | — | -6.94 | -2.04 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.27 | -10.73 | 368 | 32.9 | -16.24 | -5.20 | -17.56 | 588 |
| 22 | Daily: Bullish score | daily | 88.76 | -11.24 | 15 | 20.0 | -4.99 | -0.65 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.26 | -3.55 | -14.68 | 86 |
| 24 | Agent | meta | 88.41 | -11.59 | 150 | 37.3 | -13.90 | -7.35 | -14.71 | 213 |
| 25 | Hold BTC | benchmark | 88.36 | -11.64 | 1 | 0.0 | -5.60 | -0.72 | -14.09 | 1 |
| 26 | Copy: Insider buying | copy | 88.25 | -11.75 | 40 | 37.5 | -23.68 | -4.55 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.90 | -13.10 | 166 | 27.1 | -14.83 | -3.26 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.94 | -14.06 | 71 | 14.1 | -13.27 | -2.69 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.16 | -14.85 | 17 | 47.1 | -32.54 | -2.05 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.28 | -15.72 | 73 | 31.5 | -18.53 | -5.51 | -19.08 | 100 |
| 31 | Opening range 15m | breakout | 82.26 | -17.74 | 457 | 30.0 | -21.21 | -6.24 | -21.40 | 724 |
| 32 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.73 | -3.67 | -21.28 | 100 |
| 33 | Stochastic reversion · 1h | reversion | 81.12 | -18.88 | 260 | 46.9 | -26.54 | -3.97 | -29.25 | 393 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.76 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.58 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 79.67 | -20.33 | 2 | 0.0 | -12.80 | -1.69 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.59 | -20.41 | 172 | 18.6 | -24.42 | -4.06 | -27.04 | 260 |
| 38 | MFI reversion · 1h | reversion | 78.54 | -21.46 | 329 | 34.0 | -19.94 | -2.66 | -22.54 | 156 |
| 39 | Ichimoku · 1h | trend | 78.11 | -21.89 | 94 | 14.9 | -23.05 | -4.69 | -29.43 | 125 |
| 40 | Bollinger breakout · 1h | breakout | 77.87 | -22.13 | 166 | 23.5 | -23.44 | -4.86 | -27.12 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.29 | -23.71 | 286 | 46.2 | -30.82 | -5.02 | -31.74 | 467 |
| 42 | EMA 20/50 cross · 1h | trend | 76.08 | -23.92 | 102 | 10.8 | -23.54 | -4.24 | -30.58 | 131 |
| 43 | Heikin-Ashi · 1h | trend | 75.23 | -24.77 | 389 | 23.1 | -43.30 | -9.04 | -43.54 | 674 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.97 | -5.34 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.45 | -25.55 | 142 | 14.8 | -28.85 | -6.04 | -33.48 | 204 |
| 46 | Supertrend · 1h | trend | 73.71 | -26.29 | 166 | 13.3 | -30.39 | -5.27 | -34.80 | 217 |
| 47 | RSI momentum · 1h | momentum | 73.62 | -26.38 | 158 | 12.7 | -27.89 | -5.27 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.32 | -26.68 | 334 | 23.1 | -36.09 | -6.38 | -38.81 | 479 |
| 49 | Z-score reversion · 1h | reversion | 72.75 | -27.25 | 161 | 36.0 | -25.95 | -3.88 | -28.33 | 234 |
| 50 | Bollinger reversion · 1h | reversion | 72.49 | -27.51 | 250 | 40.0 | -31.57 | -5.45 | -34.52 | 375 |
| 51 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.91 | -5.01 | -38.31 | 31 |
| 52 | Williams %R · 1h | reversion | 71.75 | -28.25 | 314 | 44.9 | -37.85 | -6.14 | -39.71 | 534 |
| 53 | Donchian 20/10 · 1h | breakout | 71.63 | -28.36 | 140 | 20.0 | -29.92 | -5.50 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 71.23 | -28.77 | 271 | 18.1 | -29.73 | -6.33 | -33.60 | 283 |
| 55 | ROC + volume · 1h | momentum | 70.37 | -29.63 | 345 | 25.5 | -37.67 | -7.33 | -38.16 | 380 |
| 56 | EMA 9/21 cross · 1h | trend | 67.67 | -32.33 | 241 | 10.0 | -40.34 | -8.27 | -40.91 | 338 |
| 57 | VWAP momentum · 1h | momentum | 67.14 | -32.86 | 770 | 22.2 | -56.02 | -12.34 | -56.11 | 1228 |
| 58 | Agent (ML meta-label) | meta | 66.37 | -33.63 | 1523 | 22.8 | -13.82 | -2.06 | -24.90 | 330 |
| 59 | Three white soldiers | momentum | 66.16 | -33.84 | 454 | 16.1 | -47.62 | -21.75 | -47.62 | 636 |
| 60 | RSI(14) reversion · 1h | reversion | 66.13 | -33.87 | 142 | 27.5 | -29.22 | -4.56 | -31.54 | 219 |
| 61 | Candlestick reversal · 1h | reversion | 65.22 | -34.78 | 404 | 28.7 | -38.85 | -7.15 | -39.16 | 570 |
| 62 | Max aggression: 1-day momentum | meta | 62.22 | -37.78 | 26 | 26.9 | -42.92 | -2.69 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -45.79 | -98.95 | 5191 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.60 | -25.47 | -80.81 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -45.87 | -93.46 | 2499 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.28 | -31.49 | -89.33 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.78 | -38.81 | -90.86 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.29 | -31.73 | -90.29 | 2198 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -53.31 | -97.73 | 3455 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -55.88 | -96.27 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -32.84 | -93.72 | 2439 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.43 | -35.90 | -82.45 | 1650 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -53.59 | -99.52 | 5977 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.68 | -43.44 | -92.69 | 2596 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.68 | -36.63 | -95.69 | 3407 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -69.77 | -99.80 | 6158 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -43.06 | -91.78 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.53 | -26.24 | -75.66 | 1587 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -59.72 | -97.73 | 3491 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.79 | -59.28 | -98.79 | 4882 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.61 | -28.89 | -69.77 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -54.63 | -94.68 | 2741 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.18 | -37.10 | -85.23 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.48 | -99.65 | 6363 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.20 | -30.93 | -89.29 | 2290 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.84 | -19.62 | -77.99 | 1745 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.05 | -37.01 | -91.08 | 2231 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.59 | -50.41 | -96.60 | 3871 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.62 | -55.51 | -89.62 | 2168 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.64 | -28.70 | -66.64 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.56 | -24.32 | -73.78 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.46 | -17.94 | -78.66 | 1667 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -48.07 | -97.27 | 4322 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.04 | -99.93 | 8274 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T18:15 | Agent (ML meta-label) | sell | TSLA | 0.99 | 0.02 | selected signal exited |
| 2026-11-06T18:11 | Agent (ML meta-label) | buy | MSFT | 4.15 | — | following Bollinger reversion · 1h |
| 2026-11-06T18:11 | Agent (ML meta-label) | buy | DOGE-USD | 4.36 | — | entry |
| 2026-11-06T18:11 | Agent (ML meta-label) | sell | UPRO | 4.41 | -0.04 | selected signal exited |
| 2026-11-06T18:11 | Agent (ML meta-label) | sell | TSLA | 3.53 | 0.05 | rebalance down |
| 2026-11-06T18:00 | Candlestick reversal · 1h | sell | XRP-USD | 4.97 | -0.03 | exit signal |
| 2026-11-06T18:00 | Candlestick reversal · 1h | sell | BTC-USD | 6.51 | -0.05 | exit signal |
| 2026-11-06T18:00 | VWAP momentum · 1h | sell | XRP-USD | 1.62 | -0.02 | exit signal |
| 2026-11-06T18:00 | VWAP momentum · 1h | sell | SOL-USD | 5.57 | -0.03 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 18:26:05.000132+00:00 -> 2026-11-06 18:36:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 18:26:05.000132+00:00 -> 2026-11-06 18:36:05.000132+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 18:26:05.000132+00:00 -> 2026-11-06 18:36:05.000132+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
