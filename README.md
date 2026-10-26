# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T18:10:05.000135+00:00 · 36922 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.26 (-9.74%)

Closed trades 107, win rate 39.3%, fees £3.35, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.24 | +0.38 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-26 | PAM 12%, PEP 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 29739 decisions in 2691 calls, $0.3703 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T18:10 | 5 / 12 / 13 | TECL 14% |  |
| Breezy | 2026-10-26T18:10 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-26T18:10 | 8 / 19 / 3 | COIN 78% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Bollinger reversion | BITX | 2.12 | +2.39% | 13 |
| VWAP momentum | PLTR | 1.73 | +4.99% | 6 |
| Stochastic reversion | BITX | 1.67 | +3.43% | 12 |
| RSI(14) reversion | TSLA | 1.52 | +3.64% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.35 | 7.35 | 0 | — | 8.32 | 4.24 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.96 | 6.96 | 13 | 69.2 | 4.31 | 1.39 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.44 | 6.44 | 20 | 30.0 | 11.46 | 2.91 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.11 | 5.11 | 18 | 44.4 | 7.38 | 2.34 | -4.92 | 27 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.83 | -0.17 | 0 | — | 2.95 | 1.25 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 98.81 | -1.19 | 0 | — | 0.05 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.41 | -1.59 | 77 | 33.8 | 8.06 | 3.38 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.00 | -2.01 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.71 | -3.29 | 0 | — | 0.02 | 0.08 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.61 | -3.39 | 120 | 30.8 | -1.82 | -1.02 | -6.28 | 189 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 5.13 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 95.10 | -4.90 | 0 | — | 1.01 | 0.52 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.99 | -5.01 | 0 | — | -6.82 | -2.89 | -7.83 | 1 |
| 19 | Gap and go | momentum | 94.87 | -5.13 | 105 | 24.8 | 5.54 | 1.80 | -8.76 | 200 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -7.05 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 93.30 | -6.70 | 257 | 33.9 | -10.00 | -3.03 | -17.21 | 578 |
| 22 | Copy: Insider buying | copy | 92.48 | -7.52 | 27 | 37.0 | -17.06 | -3.27 | -21.73 | 60 |
| 23 | Donchian 55/20 · 1h | breakout | 91.95 | -8.05 | 49 | 16.3 | -15.63 | -3.56 | -16.33 | 98 |
| 24 | Daily: Momentum burst | daily | 91.50 | -8.50 | 10 | 10.0 | -19.71 | -3.76 | -20.84 | 40 |
| 25 | Squeeze breakout · 1h | breakout | 91.26 | -8.74 | 51 | 23.5 | -3.18 | -0.75 | -11.66 | 92 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.82 | -2.18 | -16.91 | 1 |
| 27 | Daily: Bullish score | daily | 90.67 | -9.33 | 11 | 18.2 | -6.98 | -0.82 | -14.40 | 13 |
| 28 | Agent | meta | 90.26 | -9.74 | 107 | 39.3 | -10.81 | -6.78 | -12.54 | 212 |
| 29 | Parabolic SAR · 1h | trend | 90.24 | -9.76 | 121 | 25.6 | -22.05 | -5.56 | -22.38 | 248 |
| 30 | Max aggression: 5-day momentum | meta | 90.23 | -9.77 | 11 | 45.5 | -16.36 | -1.53 | -27.80 | 25 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.67 | -10.33 | 0 | — | -5.00 | -0.69 | -14.57 | 1 |
| 32 | ADX DI cross · 1h | trend | 89.24 | -10.76 | 114 | 17.5 | -12.31 | -2.57 | -15.66 | 267 |
| 33 | Volume breakout · 1h | breakout | 89.12 | -10.88 | 103 | 23.3 | -12.55 | -2.63 | -15.73 | 111 |
| 34 | Agent (aggressive) | meta | 88.68 | -11.32 | 52 | 38.5 | -9.91 | -3.24 | -14.77 | 93 |
| 35 | Stochastic reversion · 1h | reversion | 88.10 | -11.90 | 198 | 47.0 | -20.75 | -3.87 | -23.10 | 393 |
| 36 | Bollinger breakout · 1h | breakout | 87.81 | -12.19 | 107 | 27.1 | -11.90 | -2.33 | -17.33 | 238 |
| 37 | Opening range 15m | breakout | 86.85 | -13.15 | 323 | 30.3 | -14.51 | -4.10 | -17.87 | 717 |
| 38 | Keltner breakout · 1h | breakout | 85.78 | -14.22 | 74 | 23.0 | -22.01 | -4.52 | -23.60 | 185 |
| 39 | Z-score reversion · 1h | reversion | 85.30 | -14.70 | 116 | 33.6 | -13.90 | -2.26 | -21.48 | 209 |
| 40 | Connors RSI(2) · 1h | reversion | 84.96 | -15.04 | 173 | 40.5 | -26.56 | -8.06 | -26.96 | 198 |
| 41 | EMA 20/50 cross · 1h | trend | 84.37 | -15.63 | 72 | 11.1 | -22.40 | -4.50 | -23.66 | 127 |
| 42 | RSI momentum · 1h | momentum | 83.79 | -16.21 | 104 | 15.4 | -20.23 | -4.17 | -21.09 | 206 |
| 43 | MACD cross · 1h | trend | 83.38 | -16.62 | 236 | 22.9 | -28.48 | -6.00 | -29.51 | 472 |
| 44 | Supertrend · 1h | trend | 83.26 | -16.74 | 114 | 14.0 | -27.44 | -6.02 | -29.00 | 224 |
| 45 | MFI reversion · 1h | reversion | 82.89 | -17.11 | 263 | 31.6 | -15.77 | -2.44 | -20.70 | 154 |
| 46 | Ichimoku · 1h | trend | 82.78 | -17.22 | 66 | 12.1 | -22.01 | -4.60 | -24.25 | 110 |
| 47 | Triple EMA stack · 1h | trend | 81.89 | -18.11 | 99 | 15.2 | -30.46 | -6.24 | -30.85 | 210 |
| 48 | Bollinger reversion · 1h | reversion | 81.69 | -18.31 | 179 | 37.4 | -28.19 | -5.62 | -30.74 | 373 |
| 49 | Williams %R · 1h | reversion | 81.49 | -18.51 | 228 | 46.1 | -35.48 | -6.13 | -36.65 | 542 |
| 50 | CCI reversion · 1h | reversion | 81.33 | -18.67 | 215 | 42.8 | -23.71 | -3.35 | -28.08 | 466 |
| 51 | MACD zero-line · 1h | trend | 80.86 | -19.14 | 107 | 15.9 | -23.22 | -4.96 | -24.63 | 219 |
| 52 | Donchian 20/10 · 1h | breakout | 80.07 | -19.93 | 99 | 20.2 | -24.32 | -4.66 | -27.39 | 213 |
| 53 | Agent (ML meta-label) | meta | 79.25 | -20.75 | 919 | 19.3 | -15.96 | -2.86 | -18.50 | 354 |
| 54 | OBV trend · 1h | momentum | 79.21 | -20.79 | 206 | 17.5 | -32.78 | -7.03 | -33.20 | 305 |
| 55 | Three white soldiers | momentum | 78.84 | -21.16 | 299 | 19.4 | -44.02 | -20.60 | -44.02 | 599 |
| 56 | RSI(14) reversion · 1h | reversion | 78.71 | -21.29 | 100 | 24.0 | -16.74 | -3.06 | -24.48 | 203 |
| 57 | Heikin-Ashi · 1h | trend | 76.94 | -23.06 | 284 | 22.5 | -44.37 | -10.21 | -45.36 | 664 |
| 58 | ROC + volume · 1h | momentum | 76.93 | -23.07 | 246 | 24.0 | -30.61 | -6.05 | -32.61 | 379 |
| 59 | Candlestick reversal · 1h | reversion | 76.68 | -23.32 | 271 | 28.0 | -33.27 | -6.22 | -35.17 | 571 |
| 60 | VWAP momentum · 1h | momentum | 75.55 | -24.45 | 545 | 21.1 | -49.43 | -11.14 | -50.19 | 1241 |
| 61 | EMA 9/21 cross · 1h | trend | 75.50 | -24.50 | 171 | 11.1 | -31.70 | -6.46 | -34.92 | 331 |
| 62 | Max aggression: 1-day momentum | meta | 67.67 | -32.33 | 19 | 26.3 | -41.59 | -2.84 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.36 | -44.64 | 756 | 22.1 | -74.41 | -27.03 | -74.53 | 1576 |
| 64 | Volume breakout | breakout | 54.18 | -45.82 | 456 | 12.9 | -62.62 | -26.55 | -62.65 | 800 |
| 65 | Donchian 55/20 | breakout | 51.34 | -48.66 | 605 | 19.2 | -71.82 | -23.73 | -72.35 | 1276 |
| 66 | Squeeze breakout | breakout | 51.23 | -48.77 | 589 | 14.4 | -67.30 | -28.64 | -67.82 | 1172 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -45.56 | -98.90 | 5175 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.13 | -23.62 | -79.23 | 1429 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.86 | -47.21 | -93.93 | 2551 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.33 | -31.20 | -89.37 | 1939 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.41 | -38.53 | -91.49 | 2348 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.61 | -30.98 | -90.65 | 2168 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.94 | -56.10 | -97.95 | 3535 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.15 | -60.73 | -96.19 | 3379 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.20 | -36.83 | -94.27 | 2473 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.47 | -34.53 | -82.81 | 1700 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -56.50 | -99.43 | 5786 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.65 | -43.26 | -92.68 | 2623 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.63 | -39.02 | -95.64 | 3389 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -83.05 | -99.78 | 6190 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.48 | -46.66 | -92.49 | 2344 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -66.45 | -97.71 | 3575 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -61.60 | -98.67 | 4814 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -57.91 | -94.58 | 2774 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.50 | -39.70 | -84.55 | 1819 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.96 | -99.61 | 6306 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -29.73 | -88.44 | 2228 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.16 | -19.42 | -77.61 | 1703 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.68 | -38.08 | -90.75 | 2294 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.35 | -49.73 | -96.38 | 3839 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.21 | -51.30 | -90.23 | 2144 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.46 | -18.01 | -76.57 | 1588 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -49.91 | -96.56 | 4209 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -109.65 | -99.92 | 8269 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T18:05 | Opening range 30m | buy | MSFT | 2.07 | — | entry |
| 2026-10-26T18:05 | Opening range 30m | sell | META | 2.07 | -0.02 | stop-loss |
| 2026-10-26T18:05 | Opening range 15m | buy | MSFT | 2.53 | — | entry |
| 2026-10-26T18:05 | Opening range 15m | sell | META | 2.53 | -0.00 | stop-loss |
| 2026-10-26T18:05 | ROC + volume | sell | ETHU | 13.83 | -0.00 | target is flat |
| 2026-10-26T18:00 | Agent (ML meta-label) | buy | TSLA | 1.81 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T18:00 | Agent (ML meta-label) | buy | SOXL | 5.36 | — | rebalance up |
| 2026-10-26T18:00 | Agent (ML meta-label) | sell | MSFT | 7.18 | -0.00 | selected signal exited |
| 2026-10-26T18:00 | ROC + volume · 1h | buy | MSFT | 3.66 | — | entry |
| 2026-10-26T18:00 | ROC + volume · 1h | buy | AMD | 4.82 | — | rebalance up |
| 2026-10-26T18:00 | ROC + volume · 1h | sell | SOL-USD | 8.48 | -0.12 | exit signal |
| 2026-10-26T18:00 | Ichimoku · 1h | buy | XRP-USD | 8.26 | — | entry signal |
| 2026-10-26T18:00 | Ichimoku · 1h | buy | PLTR | 5.29 | — | rebalance up |
| 2026-10-26T18:00 | Ichimoku · 1h | sell | TNA | 6.82 | -0.04 | rebalance down |
| 2026-10-26T18:00 | Ichimoku · 1h | sell | SOL-USD | 6.73 | -0.10 | rebalance down |
| 2026-10-26T18:00 | MACD zero-line · 1h | buy | XRP-USD | 8.35 | — | entry signal |
| 2026-10-26T18:00 | MACD zero-line · 1h | sell | TSLA | 4.10 | -0.00 | rebalance down |
| 2026-10-26T18:00 | MACD zero-line · 1h | sell | PLTR | 4.17 | 0.02 | rebalance down |
| 2026-10-26T17:55 | ROC + volume | buy | TECL | 13.83 | — | entry signal |
| 2026-10-26T17:55 | ROC + volume | buy | ETHU | 13.83 | — | entry signal |
| 2026-10-26T17:50 | Agent (ML meta-label) | buy | SOXL | 2.54 | — | entry |
| 2026-10-26T17:50 | Agent (ML meta-label) | buy | MSFT | 7.18 | — | entry |
| 2026-10-26T17:50 | Agent (aggressive) | sell | TSLA | 44.34 | 0.00 | selected signal exited |
| 2026-10-26T17:50 | Agent | sell | TSLA | 18.05 | 0.00 | selected signal exited |
| 2026-10-26T17:50 | Ichimoku · 1h | buy | PLTR | 4.14 | — | rebalance up |
| 2026-10-26T17:50 | Ichimoku · 1h | sell | IWM | 4.14 | -0.02 | rebalance down |
| 2026-10-26T17:50 | Opening range 15m | buy | META | 2.53 | — | entry |
| 2026-10-26T17:50 | Opening range 15m | sell | LABU | 2.53 | -0.03 | exit signal |
| 2026-10-26T17:46 | Agent (ML meta-label) | sell | SOXL | 7.89 | -0.03 | selected signal exited |
| 2026-10-26T17:46 | ROC + volume · 1h | buy | AMD | 1.58 | — | entry |
| 2026-10-26T17:46 | ROC + volume · 1h | sell | TECL | 1.58 | -0.01 | target is flat |
| 2026-10-26T17:41 | Agent (ML meta-label) | sell | TSLA | 1.83 | -0.00 | selected signal exited |
| 2026-10-26T17:40 | Agent (ML meta-label) | buy | TSLA | 1.83 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T17:40 | Agent (ML meta-label) | buy | SOXL | 5.36 | — | rebalance up |
| 2026-10-26T17:40 | Agent (ML meta-label) | sell | MSFT | 7.19 | -0.01 | selected signal exited |
| 2026-10-26T17:40 | Volume breakout | sell | PLTR | 13.51 | -0.05 | exit signal |
| 2026-10-26T17:35 | Agent (ML meta-label) | buy | SOXL | 2.55 | — | entry |
| 2026-10-26T17:35 | Agent (ML meta-label) | buy | MSFT | 7.20 | — | entry |
| 2026-10-26T17:35 | Agent (aggressive) | buy | TSLA | 44.34 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T17:35 | Agent | buy | TSLA | 18.04 | — | following Connors RSI(2), RSI(14) reversion |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 18:10:05.000135+00:00 -> 2026-10-26 18:20:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
