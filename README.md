# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T17:12:05.000121+00:00 · 36874 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.22 (-9.78%)

Closed trades 106, win rate 38.7%, fees £3.33, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.21 | +0.35 |

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

Today: 25485 decisions in 2547 calls, $0.3206 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T17:12 | 4 / 20 / 5 | TECL 16% |  |
| Breezy | 2026-10-26T17:12 | 0 / 28 / 1 | cash |  |
| Boozy | 2026-10-26T17:12 | 6 / 22 / 1 | ETHU 73% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.33 | 7.33 | 0 | — | 8.08 | 4.23 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.74 | 6.74 | 13 | 69.2 | 4.09 | 1.33 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.22 | 6.22 | 20 | 30.0 | 11.22 | 2.87 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.89 | 4.89 | 18 | 44.4 | 6.90 | 2.21 | -4.92 | 27 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.98 | -0.01 | 0 | — | 2.89 | 1.32 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 98.77 | -1.23 | 0 | — | 0.05 | 0.03 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.38 | -1.62 | 77 | 33.8 | 8.03 | 3.37 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.06 | -2.01 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.60 | -3.40 | 0 | — | -0.27 | -0.05 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.53 | -3.47 | 120 | 30.8 | -0.67 | -0.30 | -6.28 | 188 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.86 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 17 | Hold BTC | benchmark | 95.21 | -4.79 | 0 | — | 0.93 | 0.54 | -9.28 | 1 |
| 18 | Gap and go | momentum | 94.78 | -5.22 | 105 | 24.8 | 5.05 | 1.66 | -8.76 | 200 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 94.74 | -5.26 | 0 | — | -7.06 | -3.00 | -7.83 | 1 |
| 20 | Trend pullback · 1h | trend | 93.56 | -6.44 | 95 | 23.2 | -21.86 | -7.04 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 93.34 | -6.66 | 256 | 34.0 | -10.02 | -3.04 | -17.21 | 578 |
| 22 | Copy: Insider buying | copy | 93.01 | -6.99 | 27 | 37.0 | -16.55 | -3.17 | -21.73 | 60 |
| 23 | Donchian 55/20 · 1h | breakout | 92.06 | -7.95 | 49 | 16.3 | -15.54 | -3.54 | -16.29 | 98 |
| 24 | Daily: Momentum burst | daily | 91.62 | -8.38 | 10 | 10.0 | -19.18 | -3.73 | -20.84 | 40 |
| 25 | Squeeze breakout · 1h | breakout | 91.28 | -8.72 | 51 | 23.5 | -2.58 | -0.61 | -11.63 | 92 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.99 | -2.18 | -16.91 | 1 |
| 27 | Daily: Bullish score | daily | 90.65 | -9.35 | 11 | 18.2 | -6.84 | -0.82 | -14.40 | 13 |
| 28 | Max aggression: 5-day momentum | meta | 90.45 | -9.55 | 11 | 45.5 | -16.17 | -1.50 | -27.80 | 25 |
| 29 | Parabolic SAR · 1h | trend | 90.28 | -9.72 | 121 | 25.6 | -23.80 | -5.97 | -24.15 | 247 |
| 30 | Agent | meta | 90.22 | -9.78 | 106 | 38.7 | -10.77 | -6.79 | -12.54 | 210 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.72 | -10.28 | 0 | — | -5.18 | -0.68 | -14.57 | 1 |
| 32 | Volume breakout · 1h | breakout | 89.16 | -10.84 | 103 | 23.3 | -12.52 | -2.62 | -15.73 | 111 |
| 33 | ADX DI cross · 1h | trend | 89.07 | -10.93 | 113 | 17.7 | -12.78 | -2.68 | -15.99 | 266 |
| 34 | Agent (aggressive) | meta | 88.68 | -11.32 | 51 | 37.3 | -9.92 | -3.25 | -14.77 | 92 |
| 35 | Stochastic reversion · 1h | reversion | 88.27 | -11.73 | 198 | 47.0 | -19.44 | -3.56 | -22.39 | 394 |
| 36 | Bollinger breakout · 1h | breakout | 87.93 | -12.07 | 107 | 27.1 | -11.74 | -2.29 | -17.33 | 238 |
| 37 | Opening range 15m | breakout | 86.90 | -13.10 | 321 | 30.5 | -14.64 | -4.14 | -17.87 | 718 |
| 38 | Keltner breakout · 1h | breakout | 85.81 | -14.19 | 74 | 23.0 | -21.82 | -4.42 | -23.26 | 185 |
| 39 | Z-score reversion · 1h | reversion | 85.20 | -14.80 | 116 | 33.6 | -13.98 | -2.28 | -21.48 | 209 |
| 40 | Connors RSI(2) · 1h | reversion | 85.03 | -14.97 | 173 | 40.5 | -26.49 | -8.04 | -26.96 | 197 |
| 41 | EMA 20/50 cross · 1h | trend | 84.37 | -15.63 | 72 | 11.1 | -23.35 | -4.70 | -24.42 | 129 |
| 42 | RSI momentum · 1h | momentum | 83.89 | -16.11 | 104 | 15.4 | -20.45 | -4.16 | -21.05 | 205 |
| 43 | MACD cross · 1h | trend | 83.37 | -16.64 | 236 | 22.9 | -28.11 | -5.94 | -29.14 | 474 |
| 44 | Supertrend · 1h | trend | 83.18 | -16.82 | 114 | 14.0 | -28.26 | -6.28 | -29.46 | 224 |
| 45 | Ichimoku · 1h | trend | 82.96 | -17.04 | 66 | 12.1 | -23.70 | -4.98 | -24.25 | 110 |
| 46 | MFI reversion · 1h | reversion | 82.95 | -17.05 | 263 | 31.6 | -15.70 | -2.42 | -20.70 | 154 |
| 47 | Triple EMA stack · 1h | trend | 82.01 | -17.99 | 99 | 15.2 | -30.21 | -6.22 | -30.62 | 211 |
| 48 | Bollinger reversion · 1h | reversion | 81.95 | -18.05 | 179 | 37.4 | -28.14 | -5.58 | -30.92 | 374 |
| 49 | Williams %R · 1h | reversion | 81.64 | -18.36 | 228 | 46.1 | -34.83 | -5.97 | -36.03 | 542 |
| 50 | CCI reversion · 1h | reversion | 81.26 | -18.74 | 214 | 42.5 | -24.12 | -3.42 | -28.08 | 468 |
| 51 | MACD zero-line · 1h | trend | 80.94 | -19.06 | 107 | 15.9 | -23.20 | -4.95 | -25.11 | 220 |
| 52 | Donchian 20/10 · 1h | breakout | 80.17 | -19.83 | 99 | 20.2 | -24.16 | -4.63 | -27.33 | 213 |
| 53 | OBV trend · 1h | momentum | 79.27 | -20.73 | 206 | 17.5 | -32.39 | -6.94 | -32.80 | 305 |
| 54 | Agent (ML meta-label) | meta | 79.24 | -20.76 | 913 | 19.2 | -16.34 | -2.97 | -20.43 | 344 |
| 55 | Three white soldiers | momentum | 79.15 | -20.85 | 294 | 19.4 | -44.12 | -20.44 | -44.25 | 602 |
| 56 | RSI(14) reversion · 1h | reversion | 78.62 | -21.38 | 100 | 24.0 | -20.60 | -4.05 | -24.48 | 199 |
| 57 | ROC + volume · 1h | momentum | 76.93 | -23.07 | 244 | 24.2 | -30.48 | -6.03 | -32.48 | 382 |
| 58 | Heikin-Ashi · 1h | trend | 76.81 | -23.19 | 284 | 22.5 | -44.76 | -10.28 | -45.65 | 665 |
| 59 | Candlestick reversal · 1h | reversion | 76.73 | -23.27 | 271 | 28.0 | -33.33 | -6.35 | -34.77 | 569 |
| 60 | EMA 9/21 cross · 1h | trend | 75.58 | -24.42 | 171 | 11.1 | -31.60 | -6.43 | -34.90 | 329 |
| 61 | VWAP momentum · 1h | momentum | 75.53 | -24.47 | 542 | 20.8 | -49.63 | -11.19 | -50.37 | 1238 |
| 62 | Max aggression: 1-day momentum | meta | 67.78 | -32.22 | 19 | 26.3 | -41.49 | -2.83 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.39 | -44.61 | 754 | 22.1 | -74.46 | -26.97 | -74.62 | 1577 |
| 64 | Volume breakout | breakout | 54.24 | -45.76 | 455 | 13.0 | -62.56 | -26.45 | -62.65 | 799 |
| 65 | Squeeze breakout | breakout | 51.23 | -48.77 | 589 | 14.4 | -67.43 | -28.67 | -67.81 | 1177 |
| 66 | Donchian 55/20 | breakout | 51.17 | -48.83 | 605 | 19.2 | -71.90 | -23.83 | -72.35 | 1276 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -45.56 | -98.91 | 5179 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.20 | -23.64 | -79.27 | 1428 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.92 | -47.12 | -93.99 | 2553 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.32 | -31.15 | -89.33 | 1932 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.39 | -38.53 | -91.47 | 2343 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.59 | -30.99 | -90.63 | 2169 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.95 | -55.96 | -97.95 | 3527 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.17 | -60.80 | -96.20 | 3378 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.18 | -36.94 | -94.23 | 2470 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.59 | -34.89 | -82.91 | 1693 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -56.29 | -99.44 | 5788 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.71 | -43.32 | -92.71 | 2632 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.61 | -38.90 | -95.62 | 3386 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -82.48 | -99.78 | 6180 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.43 | -46.27 | -92.43 | 2340 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -66.59 | -97.72 | 3574 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -61.37 | -98.68 | 4814 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -57.67 | -94.59 | 2777 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.45 | -39.45 | -84.54 | 1817 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.84 | -99.61 | 6307 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.26 | -29.58 | -88.47 | 2238 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.20 | -19.44 | -77.68 | 1706 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.76 | -38.12 | -90.84 | 2298 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.34 | -49.70 | -96.38 | 3838 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.16 | -51.85 | -90.17 | 2148 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.25 | -17.99 | -76.41 | 1587 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -49.89 | -96.56 | 4212 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -108.31 | -99.92 | 8269 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T17:10 | ROC + volume | buy | PLTR | 13.85 | — | entry signal |
| 2026-10-26T17:05 | Agent (ML meta-label) | sell | IWM | 7.19 | -0.01 | selected signal exited |
| 2026-10-26T17:05 | Agent (aggressive) | sell | BITX | 44.60 | 0.53 | selected signal exited |
| 2026-10-26T17:05 | Agent | sell | BITX | 36.31 | 0.43 | selected signal exited |
| 2026-10-26T17:05 | Three white soldiers | buy | NVDA | 7.96 | — | entry signal |
| 2026-10-26T17:05 | Three white soldiers | buy | COIN | 15.83 | — | entry signal |
| 2026-10-26T17:05 | Three white soldiers | sell | BITX | 4.02 | 0.02 | rebalance down |
| 2026-10-26T17:00 | Agent (ML meta-label) | buy | IWM | 7.19 | — | entry |
| 2026-10-26T17:00 | Candlestick reversal · 1h | buy | ETHU | 3.68 | — | entry |
| 2026-10-26T17:00 | Candlestick reversal · 1h | buy | BITX | 5.47 | — | entry |
| 2026-10-26T17:00 | Candlestick reversal · 1h | sell | ETH-USD | 8.45 | -0.01 | exit signal |
| 2026-10-26T17:00 | Three white soldiers | buy | XRP-USD | 19.77 | — | entry signal |
| 2026-10-26T17:00 | Three white soldiers | buy | BTC-USD | 19.77 | — | entry signal |
| 2026-10-26T17:00 | Three white soldiers | buy | BITX | 19.77 | — | entry signal |
| 2026-10-26T16:50 | Agent (ML meta-label) | sell | IWM | 7.17 | -0.01 | selected signal exited |
| 2026-10-26T16:50 | Donchian 55/20 | buy | TSLA | 2.90 | — | rebalance up |
| 2026-10-26T16:50 | Donchian 55/20 | buy | SOXL | 2.90 | — | rebalance up |
| 2026-10-26T16:50 | Donchian 55/20 | buy | PLTR | 2.90 | — | rebalance up |
| 2026-10-26T16:50 | Donchian 55/20 | buy | MSFT | 2.91 | — | rebalance up |
| 2026-10-26T16:50 | Donchian 55/20 | buy | AMD | 2.91 | — | rebalance up |
| 2026-10-26T16:50 | Donchian 55/20 | sell | TNA | 7.26 | 0.03 | exit signal |
| 2026-10-26T16:50 | Donchian 55/20 | sell | IWM | 7.26 | 0.01 | exit signal |
| 2026-10-26T16:45 | Donchian 55/20 | buy | TSLA | 2.61 | — | rebalance up |
| 2026-10-26T16:45 | Donchian 55/20 | buy | TNA | 2.65 | — | rebalance up |
| 2026-10-26T16:45 | Donchian 55/20 | buy | SOXL | 6.17 | — | rebalance up |
| 2026-10-26T16:45 | Donchian 55/20 | buy | PLTR | 3.35 | — | rebalance up |
| 2026-10-26T16:45 | Donchian 55/20 | buy | MSFT | 2.63 | — | rebalance up |
| 2026-10-26T16:45 | Donchian 55/20 | buy | IWM | 2.64 | — | rebalance up |
| 2026-10-26T16:45 | Donchian 55/20 | buy | AMD | 4.27 | — | rebalance up |
| 2026-10-26T16:45 | Donchian 55/20 | sell | UPRO | 4.62 | 0.02 | exit signal |
| 2026-10-26T16:45 | Donchian 55/20 | sell | TQQQ | 4.12 | 0.00 | exit signal |
| 2026-10-26T16:45 | Donchian 55/20 | sell | TECL | 4.69 | 0.05 | exit signal |
| 2026-10-26T16:45 | Donchian 55/20 | sell | SPY | 4.63 | 0.01 | exit signal |
| 2026-10-26T16:45 | Donchian 55/20 | sell | QQQ | 4.63 | -0.01 | exit signal |
| 2026-10-26T16:45 | Donchian 55/20 | sell | NVDA | 1.63 | -0.02 | stop-loss |
| 2026-10-26T16:45 | Gap and go | sell | SOXL | 19.04 | 0.59 | stop-loss |
| 2026-10-26T16:40 | Agent (ML meta-label) | buy | IWM | 7.19 | — | entry |
| 2026-10-26T16:40 | Agent (aggressive) | buy | BITX | 44.07 | — | following Bollinger reversion, Stochastic reversion |
| 2026-10-26T16:40 | Agent | buy | BITX | 35.88 | — | following Bollinger reversion, Stochastic reversion |
| 2026-10-26T16:35 | Agent (ML meta-label) | buy | UPRO | 7.91 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 17:12:05.000121+00:00 -> 2026-10-26 17:22:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
