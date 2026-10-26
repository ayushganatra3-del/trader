# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T19:40:05.000172+00:00 · 37007 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.22 (-9.78%)

Closed trades 108, win rate 38.9%, fees £3.37, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.04 | +0.00 |
| PLTR | 18.23 | +0.37 |

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

Today: 37326 decisions in 2946 calls, $0.4590 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T19:40 | 4 / 16 / 10 | LABU 15% |  |
| Breezy | 2026-10-26T19:40 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-26T19:40 | 3 / 24 / 3 | COIN 67% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.74 | 7.74 | 0 | — | 8.43 | 4.29 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.71 | 6.71 | 13 | 69.2 | 4.09 | 1.33 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.20 | 6.20 | 20 | 30.0 | 11.23 | 2.87 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.86 | 4.86 | 18 | 44.4 | 6.83 | 2.19 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.04 | 0.04 | 0 | — | 3.26 | 1.36 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.76 | -1.24 | 0 | — | -0.11 | -0.02 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.39 | -1.61 | 77 | 33.8 | 8.05 | 3.37 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.36 | -1.64 | 13 | 23.1 | -3.56 | -4.14 | -4.11 | 23 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.06 | -2.01 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.75 | -3.25 | 0 | — | 0.04 | 0.08 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.53 | -3.47 | 120 | 30.8 | -1.65 | -0.93 | -6.28 | 191 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.88 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.96 | -5.04 | 0 | — | -6.82 | -2.89 | -7.83 | 1 |
| 18 | Gap and go | momentum | 94.85 | -5.15 | 105 | 24.8 | 5.52 | 1.80 | -8.76 | 200 |
| 19 | Hold BTC | benchmark | 94.69 | -5.31 | 0 | — | 1.50 | 0.46 | -9.28 | 1 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -7.05 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.95 | -7.05 | 257 | 33.9 | -10.60 | -3.24 | -17.21 | 577 |
| 22 | Copy: Insider buying | copy | 92.48 | -7.52 | 27 | 37.0 | -17.02 | -3.26 | -21.73 | 60 |
| 23 | Donchian 55/20 · 1h | breakout | 91.72 | -8.28 | 49 | 16.3 | -15.82 | -3.61 | -16.47 | 98 |
| 24 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.98 | -2.18 | -16.91 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 91.22 | -8.78 | 51 | 23.5 | -3.17 | -0.75 | -11.68 | 92 |
| 26 | Daily: Momentum burst | daily | 91.15 | -8.85 | 10 | 10.0 | -19.42 | -3.84 | -20.15 | 40 |
| 27 | Daily: Bullish score | daily | 90.69 | -9.31 | 11 | 18.2 | -6.40 | -0.81 | -14.40 | 13 |
| 28 | Max aggression: 5-day momentum | meta | 90.42 | -9.58 | 11 | 45.5 | -16.17 | -1.50 | -27.80 | 25 |
| 29 | Agent | meta | 90.22 | -9.78 | 108 | 38.9 | -10.36 | -6.51 | -12.54 | 210 |
| 30 | Parabolic SAR · 1h | trend | 89.80 | -10.21 | 121 | 25.6 | -22.06 | -5.58 | -22.32 | 246 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.31 | -10.69 | 0 | — | -5.19 | -0.74 | -14.57 | 1 |
| 32 | ADX DI cross · 1h | trend | 89.09 | -10.91 | 114 | 17.5 | -11.83 | -2.49 | -15.10 | 267 |
| 33 | Volume breakout · 1h | breakout | 89.04 | -10.96 | 103 | 23.3 | -12.63 | -2.64 | -15.73 | 111 |
| 34 | Agent (aggressive) | meta | 88.64 | -11.36 | 53 | 37.7 | -9.97 | -3.27 | -14.77 | 95 |
| 35 | Stochastic reversion · 1h | reversion | 87.54 | -12.46 | 198 | 47.0 | -20.82 | -3.81 | -22.88 | 393 |
| 36 | Bollinger breakout · 1h | breakout | 87.48 | -12.52 | 107 | 27.1 | -12.12 | -2.36 | -17.52 | 238 |
| 37 | Opening range 15m | breakout | 86.53 | -13.47 | 323 | 30.3 | -14.18 | -4.02 | -17.87 | 704 |
| 38 | Keltner breakout · 1h | breakout | 85.70 | -14.30 | 74 | 23.0 | -21.69 | -4.38 | -23.30 | 186 |
| 39 | Connors RSI(2) · 1h | reversion | 85.08 | -14.92 | 174 | 40.2 | -26.44 | -8.02 | -26.96 | 198 |
| 40 | Z-score reversion · 1h | reversion | 85.00 | -15.00 | 116 | 33.6 | -14.23 | -2.34 | -21.48 | 210 |
| 41 | EMA 20/50 cross · 1h | trend | 84.39 | -15.61 | 72 | 11.1 | -21.75 | -4.31 | -23.13 | 128 |
| 42 | RSI momentum · 1h | momentum | 83.54 | -16.46 | 104 | 15.4 | -22.30 | -4.40 | -23.62 | 202 |
| 43 | MACD cross · 1h | trend | 83.16 | -16.84 | 237 | 22.8 | -29.33 | -6.19 | -30.18 | 472 |
| 44 | Supertrend · 1h | trend | 83.14 | -16.86 | 114 | 14.0 | -28.17 | -6.13 | -29.63 | 225 |
| 45 | MFI reversion · 1h | reversion | 82.51 | -17.49 | 263 | 31.6 | -16.13 | -2.51 | -20.70 | 154 |
| 46 | Ichimoku · 1h | trend | 82.39 | -17.61 | 67 | 11.9 | -21.50 | -4.54 | -24.50 | 109 |
| 47 | Triple EMA stack · 1h | trend | 81.68 | -18.32 | 101 | 14.9 | -31.40 | -6.32 | -31.46 | 208 |
| 48 | Bollinger reversion · 1h | reversion | 81.13 | -18.88 | 179 | 37.4 | -29.08 | -5.96 | -31.14 | 372 |
| 49 | CCI reversion · 1h | reversion | 81.08 | -18.92 | 222 | 44.6 | -24.30 | -3.46 | -28.06 | 467 |
| 50 | Williams %R · 1h | reversion | 81.00 | -19.00 | 228 | 46.1 | -34.84 | -5.96 | -35.65 | 543 |
| 51 | MACD zero-line · 1h | trend | 80.33 | -19.67 | 108 | 15.7 | -23.90 | -5.14 | -24.68 | 219 |
| 52 | Donchian 20/10 · 1h | breakout | 79.76 | -20.24 | 99 | 20.2 | -24.47 | -4.68 | -27.44 | 212 |
| 53 | Agent (ML meta-label) | meta | 79.05 | -20.95 | 924 | 19.4 | -18.94 | -3.65 | -20.60 | 378 |
| 54 | OBV trend · 1h | momentum | 79.00 | -21.00 | 206 | 17.5 | -34.83 | -7.35 | -35.20 | 294 |
| 55 | Three white soldiers | momentum | 78.73 | -21.27 | 301 | 19.3 | -44.07 | -20.69 | -44.07 | 600 |
| 56 | RSI(14) reversion · 1h | reversion | 78.38 | -21.62 | 100 | 24.0 | -15.63 | -2.44 | -24.48 | 212 |
| 57 | Heikin-Ashi · 1h | trend | 76.76 | -23.24 | 289 | 22.1 | -44.77 | -10.26 | -45.66 | 661 |
| 58 | ROC + volume · 1h | momentum | 76.69 | -23.31 | 248 | 24.2 | -30.82 | -6.09 | -32.63 | 380 |
| 59 | Candlestick reversal · 1h | reversion | 76.34 | -23.66 | 272 | 27.9 | -33.53 | -6.06 | -35.19 | 574 |
| 60 | EMA 9/21 cross · 1h | trend | 75.28 | -24.73 | 174 | 10.9 | -32.14 | -6.55 | -35.24 | 334 |
| 61 | VWAP momentum · 1h | momentum | 75.27 | -24.73 | 553 | 21.0 | -49.68 | -11.23 | -50.20 | 1242 |
| 62 | Max aggression: 1-day momentum | meta | 67.42 | -32.58 | 19 | 26.3 | -41.78 | -2.86 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.24 | -44.76 | 759 | 22.1 | -74.35 | -26.97 | -74.43 | 1573 |
| 64 | Volume breakout | breakout | 54.18 | -45.82 | 456 | 12.9 | -62.61 | -26.54 | -62.64 | 799 |
| 65 | Donchian 55/20 | breakout | 51.22 | -48.78 | 605 | 19.2 | -71.90 | -23.85 | -72.35 | 1275 |
| 66 | Squeeze breakout | breakout | 51.22 | -48.78 | 590 | 14.4 | -67.08 | -28.24 | -67.82 | 1169 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -45.52 | -98.91 | 5157 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.08 | -23.53 | -79.10 | 1423 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.89 | -47.36 | -93.93 | 2546 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.25 | -31.17 | -89.27 | 1930 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.32 | -38.51 | -91.36 | 2342 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.62 | -31.03 | -90.63 | 2171 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.97 | -56.23 | -97.97 | 3538 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.16 | -60.63 | -96.18 | 3373 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.15 | -37.53 | -94.19 | 2468 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.65 | -35.14 | -82.93 | 1699 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -56.95 | -99.43 | 5792 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.65 | -43.22 | -92.66 | 2616 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -38.53 | -95.55 | 3382 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -83.53 | -99.78 | 6177 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.42 | -46.94 | -92.43 | 2339 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -66.69 | -97.73 | 3580 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -61.96 | -98.65 | 4807 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -58.26 | -94.57 | 2769 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.40 | -39.83 | -84.41 | 1809 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -68.87 | -99.60 | 6309 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.30 | -29.68 | -88.43 | 2228 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.93 | -19.35 | -77.45 | 1700 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.66 | -38.23 | -90.72 | 2293 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.28 | -49.85 | -96.28 | 3825 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.25 | -51.50 | -90.25 | 2141 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.07 | -17.99 | -76.24 | 1580 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.52 | -50.73 | -96.53 | 4215 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -112.22 | -99.92 | 8274 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T19:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | TQQQ | 98.21 | — | entry |
| 2026-10-26T19:30 | Agent (ML meta-label) | buy | TSLA | 1.81 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T19:30 | Agent (ML meta-label) | buy | SOXL | 7.90 | — | entry |
| 2026-10-26T19:30 | CCI reversion · 1h | buy | UPRO | 5.37 | — | rebalance up |
| 2026-10-26T19:30 | CCI reversion · 1h | buy | SPY | 5.35 | — | rebalance up |
| 2026-10-26T19:30 | CCI reversion · 1h | buy | META | 5.48 | — | rebalance up |
| 2026-10-26T19:30 | CCI reversion · 1h | buy | ETH-USD | 6.48 | — | rebalance up |
| 2026-10-26T19:30 | CCI reversion · 1h | buy | BITX | 5.91 | — | rebalance up |
| 2026-10-26T19:30 | CCI reversion · 1h | buy | AMZN | 5.38 | — | rebalance up |
| 2026-10-26T19:30 | CCI reversion · 1h | sell | TQQQ | 4.86 | 0.11 | exit signal |
| 2026-10-26T19:30 | CCI reversion · 1h | sell | SOXL | 5.16 | 0.47 | exit signal |
| 2026-10-26T19:30 | CCI reversion · 1h | sell | QQQ | 4.79 | 0.04 | exit signal |
| 2026-10-26T19:30 | CCI reversion · 1h | sell | PLTR | 4.81 | 0.07 | exit signal |
| 2026-10-26T19:30 | CCI reversion · 1h | sell | NVDA | 4.85 | 0.10 | exit signal |
| 2026-10-26T19:30 | Stochastic reversion · 1h | buy | SQQQ | 12.46 | — | entry |
| 2026-10-26T19:30 | Stochastic reversion · 1h | buy | AAPL | 12.49 | — | entry signal |
| 2026-10-26T19:30 | Stochastic reversion · 1h | sell | META | 4.84 | -0.07 | rebalance down |
| 2026-10-26T19:30 | Stochastic reversion · 1h | sell | LABU | 4.84 | -0.11 | rebalance down |
| 2026-10-26T19:30 | Stochastic reversion · 1h | sell | GOOGL | 5.05 | -0.06 | rebalance down |
| 2026-10-26T19:30 | Stochastic reversion · 1h | sell | ETH-USD | 5.06 | -0.05 | rebalance down |
| 2026-10-26T19:30 | Stochastic reversion · 1h | sell | AMZN | 5.16 | -0.02 | rebalance down |
| 2026-10-26T19:30 | Connors RSI(2) · 1h | sell | SQQQ | 21.01 | -0.34 | exit signal |
| 2026-10-26T19:30 | VWAP momentum · 1h | buy | SOXL | 4.20 | — | rebalance up |
| 2026-10-26T19:30 | VWAP momentum · 1h | sell | ETHU | 4.71 | 0.01 | exit signal |
| 2026-10-26T19:30 | VWAP momentum · 1h | sell | COIN | 4.69 | -0.01 | exit signal |
| 2026-10-26T19:30 | VWAP momentum · 1h | sell | BITX | 3.94 | -0.03 | exit signal |
| 2026-10-26T19:30 | Heikin-Ashi · 1h | buy | PLTR | 8.27 | — | rebalance up |
| 2026-10-26T19:30 | Heikin-Ashi · 1h | sell | UPRO | 7.65 | -0.05 | exit signal |
| 2026-10-26T19:30 | Heikin-Ashi · 1h | sell | TSLA | 7.67 | -0.04 | exit signal |
| 2026-10-26T19:30 | Heikin-Ashi · 1h | sell | SPY | 7.68 | -0.02 | exit signal |
| 2026-10-26T19:30 | MACD zero-line · 1h | buy | TECL | 7.89 | — | entry signal |
| 2026-10-26T19:30 | MACD zero-line · 1h | buy | MSFT | 13.39 | — | entry signal |
| 2026-10-26T19:30 | MACD zero-line · 1h | sell | XRP-USD | 6.67 | -0.04 | rebalance down |
| 2026-10-26T19:30 | MACD zero-line · 1h | sell | DOGE-USD | 6.62 | -0.10 | rebalance down |
| 2026-10-26T19:30 | EMA 9/21 cross · 1h | buy | AMD | 7.53 | — | entry signal |
| 2026-10-26T19:30 | EMA 9/21 cross · 1h | sell | SQQQ | 8.37 | -0.15 | exit signal |
| 2026-10-26T19:30 | Three white soldiers | sell | PLTR | 19.63 | -0.07 | exit signal |
| 2026-10-26T19:30 | Squeeze breakout | sell | MSFT | 12.79 | -0.02 | stop-loss |
| 2026-10-26T19:25 | Agent (ML meta-label) | sell | TSLA | 8.77 | -0.02 | selected signal exited |
| 2026-10-26T19:20 | Agent (ML meta-label) | buy | TSLA | 8.79 | — | following Connors RSI(2), RSI(14) reversion |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 19:40:05.000172+00:00 -> 2026-10-26 19:50:05.000172+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
