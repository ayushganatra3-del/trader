# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T22:50:05.000145+00:00 · 50176 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.30 (-11.70%)

Closed trades 151, win rate 37.1%, fees £4.31, max drawdown -12.11%.

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

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.50 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 40476 decisions in 3468 calls, $0.5018 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T22:50 | 2 / 1 / 2 | cash |  |
| Breezy | 2026-11-06T22:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T22:50 | 2 / 2 / 1 | ETH-USD 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |
| Candlestick reversal · 1h | DOGE-USD | 1.64 | +5.59% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.29 | 12.29 | 0 | — | 13.03 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.76 | -0.24 | 121 | 47.9 | -12.18 | -2.87 | -14.15 | 157 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.43 | -0.57 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.75 | -4.87 | -10.36 | 169 |
| 12 | Hold SPY | benchmark | 94.83 | -5.17 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.29 | -0.34 | -9.18 | 229 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.17 | -7.83 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.13 | -7.87 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -15.74 | -5.72 | -17.86 | 82 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.82 | -9.18 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.48 | -5.32 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.79 | -11.21 | 40 | 37.5 | -23.35 | -4.49 | -26.04 | 65 |
| 23 | Daily: Bullish score | daily | 88.76 | -11.24 | 15 | 20.0 | -5.01 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.25 | -3.57 | -14.68 | 86 |
| 25 | Hold BTC | benchmark | 88.67 | -11.33 | 1 | 0.0 | -5.28 | -0.62 | -14.09 | 1 |
| 26 | Agent | meta | 88.30 | -11.70 | 151 | 37.1 | -13.66 | -7.29 | -14.12 | 206 |
| 27 | Parabolic SAR · 1h | trend | 86.90 | -13.10 | 166 | 27.1 | -14.85 | -3.29 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.94 | -14.05 | 71 | 14.1 | -13.29 | -2.72 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.17 | -14.83 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.60 | -5.59 | -18.68 | 98 |
| 31 | Stochastic reversion · 1h | reversion | 82.13 | -17.87 | 260 | 46.9 | -26.00 | -3.86 | -29.25 | 394 |
| 32 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.72 | -3.70 | -21.28 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.82 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.51 | -4.68 | -24.50 | 173 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.48 | -19.52 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.37 | -20.63 | 175 | 18.3 | -25.31 | -4.26 | -27.04 | 263 |
| 38 | MFI reversion · 1h | reversion | 78.67 | -21.32 | 336 | 34.2 | -19.04 | -2.75 | -20.68 | 157 |
| 39 | Ichimoku · 1h | trend | 77.88 | -22.12 | 94 | 14.9 | -22.89 | -4.69 | -29.43 | 125 |
| 40 | Bollinger breakout · 1h | breakout | 77.69 | -22.31 | 167 | 23.4 | -23.66 | -4.94 | -27.12 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.82 | -23.18 | 287 | 46.0 | -31.21 | -5.15 | -32.02 | 465 |
| 42 | EMA 20/50 cross · 1h | trend | 76.08 | -23.92 | 102 | 10.8 | -24.00 | -4.36 | -30.58 | 133 |
| 43 | Heikin-Ashi · 1h | trend | 75.62 | -24.38 | 393 | 22.9 | -43.10 | -9.09 | -43.54 | 677 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.24 | -5.45 | -29.20 | 211 |
| 45 | Triple EMA stack · 1h | trend | 74.46 | -25.54 | 142 | 14.8 | -28.67 | -6.04 | -33.48 | 203 |
| 46 | Supertrend · 1h | trend | 73.64 | -26.36 | 166 | 13.3 | -30.75 | -5.38 | -34.80 | 217 |
| 47 | RSI momentum · 1h | momentum | 73.47 | -26.53 | 158 | 12.7 | -28.09 | -5.36 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.32 | -26.68 | 335 | 23.0 | -36.29 | -6.48 | -38.81 | 485 |
| 49 | Z-score reversion · 1h | reversion | 73.16 | -26.84 | 162 | 35.8 | -25.30 | -3.77 | -28.10 | 233 |
| 50 | Bollinger reversion · 1h | reversion | 72.98 | -27.02 | 251 | 40.2 | -31.28 | -5.37 | -34.52 | 372 |
| 51 | Williams %R · 1h | reversion | 72.46 | -27.54 | 315 | 44.8 | -37.51 | -6.09 | -39.70 | 535 |
| 52 | Daily: Momentum burst | daily | 72.31 | -27.69 | 26 | 11.5 | -35.93 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.63 | -28.37 | 140 | 20.0 | -29.96 | -5.55 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -30.83 | -6.62 | -33.82 | 286 |
| 55 | ROC + volume · 1h | momentum | 69.95 | -30.05 | 346 | 25.4 | -37.12 | -7.23 | -37.39 | 379 |
| 56 | EMA 9/21 cross · 1h | trend | 67.40 | -32.60 | 241 | 10.0 | -40.21 | -8.34 | -40.52 | 337 |
| 57 | VWAP momentum · 1h | momentum | 67.23 | -32.77 | 776 | 22.0 | -55.80 | -12.36 | -55.84 | 1236 |
| 58 | Agent (ML meta-label) | meta | 66.45 | -33.55 | 1536 | 23.0 | -4.53 | -0.52 | -19.48 | 347 |
| 59 | RSI(14) reversion · 1h | reversion | 66.30 | -33.70 | 143 | 27.3 | -28.48 | -4.45 | -31.54 | 219 |
| 60 | Three white soldiers | momentum | 65.50 | -34.50 | 460 | 15.9 | -48.08 | -22.51 | -48.08 | 641 |
| 61 | Candlestick reversal · 1h | reversion | 65.48 | -34.52 | 407 | 28.5 | -38.51 | -7.14 | -39.05 | 572 |
| 62 | Max aggression: 1-day momentum | meta | 62.23 | -37.77 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -46.41 | -98.93 | 5212 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.72 | -25.76 | -80.72 | 1431 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -48.05 | -93.54 | 2516 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -32.28 | -89.29 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.94 | -40.39 | -90.95 | 2311 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.14 | -31.95 | -90.15 | 2190 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -55.31 | -97.73 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -58.28 | -96.34 | 3399 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.95 | -34.37 | -93.95 | 2457 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.67 | -36.38 | -82.68 | 1663 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -55.89 | -99.52 | 5974 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.69 | -44.40 | -92.76 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.69 | -38.06 | -95.69 | 3410 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -78.16 | -99.80 | 6199 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.90 | -44.11 | -91.90 | 2279 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.29 | -26.30 | -75.39 | 1578 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -64.46 | -97.75 | 3515 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -62.94 | -98.78 | 4882 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.82 | -29.58 | -70.07 | 1207 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -56.19 | -94.74 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.16 | -38.29 | -85.23 | 1774 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -75.28 | -99.64 | 6373 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.18 | -31.74 | -89.27 | 2290 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.58 | -19.64 | -77.79 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.99 | -38.03 | -91.01 | 2220 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.56 | -53.18 | -96.58 | 3874 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.54 | -57.29 | -89.54 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.28 | -29.07 | -66.28 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.82 | -24.90 | -73.86 | 1272 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.07 | -17.85 | -78.55 | 1664 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -50.27 | -97.24 | 4326 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -121.61 | -99.93 | 8309 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T22:45 | Three white soldiers | sell | XRP-USD | 16.31 | -0.09 | exit signal |
| 2026-11-06T22:00 | VWAP reversion · 1h | buy | XRP-USD | 24.97 | — | entry signal |
| 2026-11-06T21:55 | Three white soldiers | buy | XRP-USD | 16.40 | — | entry signal |
| 2026-11-06T21:00 | Agent (ML meta-label) | buy | DOGE-USD | 3.91 | — | following Candlestick reversal · 1h |
| 2026-11-06T21:00 | Bollinger breakout · 1h | sell | SOL-USD | 19.22 | -0.33 | exit signal |
| 2026-11-06T21:00 | ADX DI cross · 1h | sell | DOGE-USD | 19.74 | -0.24 | exit signal |
| 2026-11-06T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 94.10 | -1.21 | target is flat |
| 2026-11-06T20:55 | Agent (ML meta-label) | sell | DOGE-USD | 4.11 | -0.05 | selected signal exited |
| 2026-11-06T20:55 | MFI reversion · 1h | buy | GOOGL | 8.73 | — | entry |
| 2026-11-06T20:55 | MFI reversion · 1h | sell | PLTR | 4.64 | -0.03 | target is flat |
| 2026-11-06T20:55 | MFI reversion · 1h | sell | BITX | 7.17 | 0.01 | target is flat |
| 2026-11-06T20:55 | MFI reversion · 1h | sell | AAPL | 6.03 | -0.03 | target is flat |
| 2026-11-06T20:55 | CCI reversion · 1h | buy | ETHU | 1.02 | — | entry |
| 2026-11-06T20:55 | CCI reversion · 1h | buy | COIN | 4.04 | — | entry |
| 2026-11-06T20:55 | CCI reversion · 1h | sell | XRP-USD | 5.06 | -0.08 | stop-loss |
| 2026-11-06T20:55 | Williams %R · 1h | buy | IWM | 4.52 | — | entry |
| 2026-11-06T20:55 | Williams %R · 1h | sell | XRP-USD | 5.40 | -0.14 | stop-loss |
| 2026-11-06T20:55 | RSI(14) reversion · 1h | buy | SOXL | 4.14 | — | entry |
| 2026-11-06T20:55 | RSI(14) reversion · 1h | sell | XRP-USD | 4.38 | -0.11 | stop-loss |
| 2026-11-06T20:55 | Candlestick reversal · 1h | buy | SOL-USD | 4.90 | — | entry |
| 2026-11-06T20:55 | Candlestick reversal · 1h | sell | QQQ | 4.67 | -0.02 | target is flat |
| 2026-11-06T20:55 | OBV trend · 1h | buy | AMZN | 17.75 | — | entry |
| 2026-11-06T20:55 | Opening range 30m | sell | TSLA | 12.80 | -0.07 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | TNA | 15.17 | 0.06 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | MSFT | 12.70 | -0.06 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | LABU | 15.00 | 0.16 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | IWM | 12.85 | 0.01 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | AAPL | 13.48 | -0.05 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 15m | sell | TSLA | 11.72 | -0.01 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 15m | sell | TNA | 11.69 | 0.08 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 15m | sell | PLTR | 11.78 | -0.07 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 15m | sell | MSFT | 11.75 | -0.05 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 15m | sell | LABU | 7.76 | 0.26 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 15m | sell | IWM | 11.76 | 0.02 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 15m | sell | AAPL | 11.72 | -0.02 | end-of-day flatten |
| 2026-11-06T20:50 | Agent (ML meta-label) | buy | LABU | 3.69 | — | entry |
| 2026-11-06T20:50 | Agent (ML meta-label) | sell | BTC-USD | 3.69 | -0.02 | selected signal exited |
| 2026-11-06T20:40 | MFI reversion · 1h | buy | ETHU | 6.56 | — | entry |
| 2026-11-06T20:40 | MFI reversion · 1h | sell | COIN | 7.15 | -0.01 | target is flat |
| 2026-11-06T20:40 | Three white soldiers | sell | COIN | 16.40 | -0.09 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 22:50:05.000145+00:00 -> 2026-11-06 23:00:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 22:50:05.000145+00:00 -> 2026-11-06 23:00:05.000145+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 22:50:05.000145+00:00 -> 2026-11-06 23:00:05.000145+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
