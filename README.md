# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T17:41:05.000119+00:00 · 36902 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.18 (-9.82%)

Closed trades 106, win rate 38.7%, fees £3.34, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.19 | +0.33 |
| TSLA | 18.02 | -0.02 |

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

Today: 27966 decisions in 2631 calls, $0.3496 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T17:41 | 1 / 7 / 21 | cash |  |
| Breezy | 2026-10-26T17:41 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-10-26T17:41 | 3 / 22 / 4 | BITX 64% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.44 | 7.44 | 0 | — | 8.25 | 4.28 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.53 | 6.53 | 13 | 69.2 | 3.89 | 1.27 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.02 | 6.02 | 20 | 30.0 | 11.01 | 2.83 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.69 | 4.69 | 18 | 44.4 | 6.78 | 2.19 | -4.92 | 27 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.71 | -0.29 | 0 | — | 2.61 | 1.19 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 98.74 | -1.26 | 0 | — | -0.07 | 0.01 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.36 | -1.64 | 77 | 33.8 | 8.01 | 3.36 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.05 | -2.01 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.75 | -3.25 | 0 | — | -0.09 | 0.03 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.31 | -3.69 | 120 | 30.8 | -1.57 | -0.80 | -6.28 | 196 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.94 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 95.10 | -4.90 | 0 | — | 1.01 | 0.52 | -9.28 | 1 |
| 18 | Gap and go | momentum | 94.78 | -5.22 | 105 | 24.8 | 5.04 | 1.66 | -8.76 | 200 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 94.74 | -5.26 | 0 | — | -7.06 | -3.00 | -7.83 | 1 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -7.05 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 93.13 | -6.87 | 256 | 34.0 | -10.18 | -3.09 | -17.21 | 578 |
| 22 | Copy: Insider buying | copy | 92.97 | -7.03 | 27 | 37.0 | -16.59 | -3.18 | -21.73 | 60 |
| 23 | Donchian 55/20 · 1h | breakout | 91.90 | -8.10 | 49 | 16.3 | -15.68 | -3.57 | -16.29 | 98 |
| 24 | Daily: Momentum burst | daily | 91.44 | -8.56 | 10 | 10.0 | -19.50 | -3.77 | -20.84 | 40 |
| 25 | Squeeze breakout · 1h | breakout | 91.26 | -8.74 | 51 | 23.5 | -3.18 | -0.75 | -11.63 | 92 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.94 | -2.18 | -16.91 | 1 |
| 27 | Max aggression: 5-day momentum | meta | 90.63 | -9.37 | 11 | 45.5 | -15.99 | -1.48 | -27.80 | 25 |
| 28 | Daily: Bullish score | daily | 90.57 | -9.44 | 11 | 18.2 | -7.05 | -0.83 | -14.40 | 13 |
| 29 | Agent | meta | 90.18 | -9.82 | 106 | 38.7 | -10.88 | -6.87 | -12.54 | 212 |
| 30 | Parabolic SAR · 1h | trend | 90.07 | -9.93 | 121 | 25.6 | -22.20 | -5.59 | -22.38 | 248 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.60 | -10.40 | 0 | — | -5.20 | -0.70 | -14.57 | 1 |
| 32 | Volume breakout · 1h | breakout | 89.09 | -10.91 | 103 | 23.3 | -12.59 | -2.63 | -15.73 | 111 |
| 33 | ADX DI cross · 1h | trend | 88.98 | -11.02 | 114 | 17.5 | -12.51 | -2.61 | -15.66 | 267 |
| 34 | Agent (aggressive) | meta | 88.63 | -11.37 | 51 | 37.3 | -9.97 | -3.27 | -14.77 | 93 |
| 35 | Stochastic reversion · 1h | reversion | 88.07 | -11.93 | 198 | 47.0 | -20.63 | -3.86 | -23.02 | 393 |
| 36 | Bollinger breakout · 1h | breakout | 87.77 | -12.23 | 107 | 27.1 | -11.90 | -2.32 | -17.33 | 238 |
| 37 | Opening range 15m | breakout | 86.72 | -13.29 | 321 | 30.5 | -14.76 | -4.19 | -17.87 | 718 |
| 38 | Keltner breakout · 1h | breakout | 85.74 | -14.26 | 74 | 23.0 | -22.06 | -4.53 | -23.70 | 186 |
| 39 | Z-score reversion · 1h | reversion | 85.12 | -14.88 | 116 | 33.6 | -14.07 | -2.30 | -21.48 | 210 |
| 40 | Connors RSI(2) · 1h | reversion | 85.03 | -14.97 | 173 | 40.5 | -26.50 | -8.04 | -26.96 | 198 |
| 41 | EMA 20/50 cross · 1h | trend | 84.39 | -15.61 | 72 | 11.1 | -22.37 | -4.49 | -23.66 | 127 |
| 42 | RSI momentum · 1h | momentum | 83.74 | -16.26 | 104 | 15.4 | -20.78 | -4.28 | -21.14 | 207 |
| 43 | MACD cross · 1h | trend | 83.28 | -16.72 | 236 | 22.9 | -28.56 | -6.02 | -29.51 | 472 |
| 44 | Supertrend · 1h | trend | 83.04 | -16.96 | 114 | 14.0 | -27.67 | -6.07 | -29.00 | 224 |
| 45 | Ichimoku · 1h | trend | 82.80 | -17.20 | 66 | 12.1 | -22.02 | -4.60 | -24.25 | 109 |
| 46 | MFI reversion · 1h | reversion | 82.79 | -17.21 | 263 | 31.6 | -15.87 | -2.46 | -20.70 | 154 |
| 47 | Triple EMA stack · 1h | trend | 81.86 | -18.14 | 99 | 15.2 | -30.61 | -6.29 | -30.96 | 210 |
| 48 | Bollinger reversion · 1h | reversion | 81.63 | -18.37 | 179 | 37.4 | -28.24 | -5.64 | -30.74 | 373 |
| 49 | Williams %R · 1h | reversion | 81.44 | -18.56 | 228 | 46.1 | -35.57 | -6.18 | -36.70 | 540 |
| 50 | CCI reversion · 1h | reversion | 81.19 | -18.81 | 215 | 42.8 | -23.88 | -3.39 | -28.08 | 466 |
| 51 | MACD zero-line · 1h | trend | 80.83 | -19.17 | 107 | 15.9 | -23.44 | -4.99 | -25.24 | 220 |
| 52 | Donchian 20/10 · 1h | breakout | 80.03 | -19.97 | 99 | 20.2 | -24.36 | -4.67 | -27.39 | 213 |
| 53 | Agent (ML meta-label) | meta | 79.12 | -20.88 | 916 | 19.3 | -15.68 | -2.87 | -19.53 | 337 |
| 54 | OBV trend · 1h | momentum | 79.11 | -20.89 | 206 | 17.5 | -32.61 | -7.02 | -32.90 | 305 |
| 55 | Three white soldiers | momentum | 78.84 | -21.16 | 299 | 19.4 | -44.46 | -20.68 | -44.46 | 603 |
| 56 | RSI(14) reversion · 1h | reversion | 78.56 | -21.44 | 100 | 24.0 | -16.32 | -2.97 | -24.48 | 201 |
| 57 | ROC + volume · 1h | momentum | 76.86 | -23.14 | 244 | 24.2 | -30.25 | -5.97 | -32.21 | 380 |
| 58 | Heikin-Ashi · 1h | trend | 76.75 | -23.25 | 284 | 22.5 | -44.48 | -10.25 | -45.33 | 664 |
| 59 | Candlestick reversal · 1h | reversion | 76.60 | -23.40 | 271 | 28.0 | -33.97 | -6.43 | -35.25 | 571 |
| 60 | EMA 9/21 cross · 1h | trend | 75.50 | -24.50 | 171 | 11.1 | -31.72 | -6.46 | -34.92 | 331 |
| 61 | VWAP momentum · 1h | momentum | 75.41 | -24.59 | 545 | 21.1 | -49.52 | -11.17 | -50.21 | 1240 |
| 62 | Max aggression: 1-day momentum | meta | 67.57 | -32.43 | 19 | 26.3 | -41.67 | -2.84 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.29 | -44.71 | 755 | 22.1 | -74.38 | -26.98 | -74.53 | 1575 |
| 64 | Volume breakout | breakout | 54.18 | -45.82 | 456 | 12.9 | -62.60 | -26.51 | -62.65 | 800 |
| 65 | Squeeze breakout | breakout | 51.23 | -48.77 | 589 | 14.4 | -67.31 | -28.67 | -67.82 | 1172 |
| 66 | Donchian 55/20 | breakout | 51.16 | -48.84 | 605 | 19.2 | -71.91 | -23.84 | -72.35 | 1276 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -45.56 | -98.91 | 5170 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.23 | -23.63 | -79.26 | 1430 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.91 | -47.20 | -93.97 | 2555 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.34 | -31.21 | -89.34 | 1938 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.45 | -38.68 | -91.51 | 2350 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.66 | -31.23 | -90.69 | 2166 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.94 | -56.08 | -97.94 | 3534 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -61.05 | -96.20 | 3381 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.22 | -37.12 | -94.26 | 2475 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.53 | -34.78 | -82.82 | 1701 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -56.38 | -99.42 | 5785 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.67 | -43.39 | -92.67 | 2623 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.63 | -39.03 | -95.64 | 3384 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -82.79 | -99.78 | 6186 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.49 | -46.31 | -92.49 | 2348 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -66.40 | -97.71 | 3569 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.55 | -98.66 | 4811 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -58.08 | -94.57 | 2774 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.51 | -39.77 | -84.53 | 1818 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.89 | -99.61 | 6308 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.29 | -29.67 | -88.42 | 2229 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.89 | -19.42 | -77.39 | 1706 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.74 | -38.19 | -90.80 | 2300 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.35 | -49.73 | -96.38 | 3835 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.24 | -51.17 | -90.24 | 2146 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.28 | -17.98 | -76.47 | 1588 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -49.88 | -96.57 | 4212 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -108.84 | -99.92 | 8262 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T17:40 | Agent (ML meta-label) | buy | TSLA | 1.83 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T17:40 | Agent (ML meta-label) | buy | SOXL | 5.36 | — | rebalance up |
| 2026-10-26T17:40 | Agent (ML meta-label) | sell | MSFT | 7.19 | -0.01 | selected signal exited |
| 2026-10-26T17:40 | Volume breakout | sell | PLTR | 13.51 | -0.05 | exit signal |
| 2026-10-26T17:35 | Agent (ML meta-label) | buy | SOXL | 2.55 | — | entry |
| 2026-10-26T17:35 | Agent (ML meta-label) | buy | MSFT | 7.20 | — | entry |
| 2026-10-26T17:35 | Agent (aggressive) | buy | TSLA | 44.34 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T17:35 | Agent | buy | TSLA | 18.04 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T17:35 | Three white soldiers | sell | NVDA | 19.74 | -0.04 | exit signal |
| 2026-10-26T17:35 | Three white soldiers | sell | COIN | 15.80 | -0.03 | exit signal |
| 2026-10-26T17:35 | Three white soldiers | sell | BTC-USD | 19.67 | -0.09 | exit signal |
| 2026-10-26T17:35 | Three white soldiers | sell | BITX | 19.73 | 0.02 | exit signal |
| 2026-10-26T17:35 | ROC + volume | sell | TECL | 13.77 | -0.08 | target is flat |
| 2026-10-26T17:30 | CCI reversion · 1h | sell | MSFT | 4.80 | 0.05 | exit signal |
| 2026-10-26T17:30 | Connors RSI(2) · 1h | buy | AAPL | 21.26 | — | entry signal |
| 2026-10-26T17:30 | OBV trend · 1h | buy | PLTR | 19.81 | — | entry signal |
| 2026-10-26T17:30 | VWAP momentum · 1h | buy | XRP-USD | 1.19 | — | entry |
| 2026-10-26T17:30 | VWAP momentum · 1h | buy | SPY | 4.72 | — | entry signal |
| 2026-10-26T17:30 | VWAP momentum · 1h | buy | NVDA | 4.72 | — | entry signal |
| 2026-10-26T17:30 | VWAP momentum · 1h | buy | AMZN | 4.72 | — | entry signal |
| 2026-10-26T17:30 | VWAP momentum · 1h | sell | TNA | 5.36 | 0.09 | exit signal |
| 2026-10-26T17:30 | VWAP momentum · 1h | sell | META | 4.70 | -0.02 | exit signal |
| 2026-10-26T17:30 | VWAP momentum · 1h | sell | LABU | 5.29 | -0.01 | exit signal |
| 2026-10-26T17:30 | Trend pullback · 1h | sell | AAPL | 23.80 | -0.01 | exit signal |
| 2026-10-26T17:30 | Ichimoku · 1h | buy | PLTR | 4.36 | — | entry signal |
| 2026-10-26T17:30 | Ichimoku · 1h | sell | TSLA | 4.18 | 0.00 | rebalance down |
| 2026-10-26T17:30 | ADX DI cross · 1h | buy | SQQQ | 1.21 | — | entry signal |
| 2026-10-26T17:30 | ADX DI cross · 1h | buy | SOXL | 9.90 | — | entry signal |
| 2026-10-26T17:30 | ADX DI cross · 1h | sell | TQQQ | 11.11 | -0.06 | exit signal |
| 2026-10-26T17:30 | Triple EMA stack · 1h | buy | PLTR | 14.00 | — | entry signal |
| 2026-10-26T17:30 | Triple EMA stack · 1h | sell | TNA | 5.58 | 0.17 | rebalance down |
| 2026-10-26T17:30 | Triple EMA stack · 1h | sell | SQQQ | 4.10 | -0.07 | rebalance down |
| 2026-10-26T17:30 | Triple EMA stack · 1h | sell | AAPL | 4.33 | -0.02 | rebalance down |
| 2026-10-26T17:30 | EMA 20/50 cross · 1h | buy | PLTR | 21.09 | — | entry signal |
| 2026-10-26T17:30 | Three white soldiers | buy | NVDA | 11.81 | — | rebalance up |
| 2026-10-26T17:30 | Three white soldiers | buy | BITX | 3.96 | — | rebalance up |
| 2026-10-26T17:30 | Three white soldiers | sell | XRP-USD | 19.67 | -0.10 | exit signal |
| 2026-10-26T17:28 | ROC + volume | buy | TECL | 13.85 | — | entry |
| 2026-10-26T17:15 | Agent (ML meta-label) | buy | TQQQ | 4.62 | — | rebalance up |
| 2026-10-26T17:15 | Agent (ML meta-label) | buy | TNA | 4.63 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 17:41:05.000119+00:00 -> 2026-10-26 17:51:05.000119+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
