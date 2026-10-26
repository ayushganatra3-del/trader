# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T18:40:05.000112+00:00 · 36950 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.21 (-9.79%)

Closed trades 107, win rate 39.3%, fees £3.36, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.25 | +0.39 |
| TSLA | 18.00 | -0.05 |

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

Today: 32220 decisions in 2775 calls, $0.3993 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T18:40 | 3 / 15 / 11 | cash |  |
| Breezy | 2026-10-26T18:40 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-10-26T18:40 | 4 / 20 / 5 | COIN 53% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.47 | 7.47 | 0 | — | 8.44 | 4.32 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.67 | 6.67 | 13 | 69.2 | 4.10 | 1.33 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.16 | 6.16 | 20 | 30.0 | 11.24 | 2.87 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.83 | 4.83 | 18 | 44.4 | 6.90 | 2.21 | -4.92 | 27 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.53 | -0.47 | 0 | — | 2.69 | 1.14 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 98.68 | -1.32 | 0 | — | -0.04 | 0.02 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.35 | -1.65 | 77 | 33.8 | 8.02 | 3.36 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.09 | -2.01 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.79 | -3.21 | 0 | — | 0.18 | 0.14 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.34 | -3.66 | 120 | 30.8 | -0.77 | -0.35 | -6.28 | 186 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.73 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 17 | Hold BTC | benchmark | 94.93 | -5.07 | 0 | — | 1.42 | 0.51 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.92 | -5.08 | 0 | — | -6.82 | -2.89 | -7.83 | 1 |
| 19 | Gap and go | momentum | 94.84 | -5.16 | 105 | 24.8 | 5.13 | 1.69 | -8.76 | 200 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -7.05 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 93.03 | -6.97 | 257 | 33.9 | -10.16 | -3.09 | -17.21 | 578 |
| 22 | Copy: Insider buying | copy | 92.67 | -7.33 | 27 | 37.0 | -16.80 | -3.22 | -21.73 | 60 |
| 23 | Donchian 55/20 · 1h | breakout | 91.75 | -8.25 | 49 | 16.3 | -15.77 | -3.59 | -16.35 | 98 |
| 24 | Daily: Momentum burst | daily | 91.39 | -8.61 | 10 | 10.0 | -19.69 | -3.77 | -20.69 | 40 |
| 25 | Squeeze breakout · 1h | breakout | 91.23 | -8.77 | 51 | 23.5 | -2.80 | -0.64 | -11.66 | 92 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.07 | -2.18 | -16.91 | 1 |
| 27 | Daily: Bullish score | daily | 90.61 | -9.39 | 11 | 18.2 | -6.83 | -0.82 | -14.40 | 13 |
| 28 | Max aggression: 5-day momentum | meta | 90.37 | -9.63 | 11 | 45.5 | -16.18 | -1.50 | -27.80 | 25 |
| 29 | Agent | meta | 90.21 | -9.79 | 107 | 39.3 | -10.84 | -6.82 | -12.54 | 213 |
| 30 | Parabolic SAR · 1h | trend | 90.00 | -10.00 | 121 | 25.6 | -21.85 | -5.54 | -22.03 | 246 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.43 | -10.57 | 0 | — | -4.99 | -0.72 | -14.57 | 1 |
| 32 | ADX DI cross · 1h | trend | 89.06 | -10.94 | 114 | 17.5 | -12.79 | -2.65 | -16.03 | 268 |
| 33 | Volume breakout · 1h | breakout | 89.02 | -10.98 | 103 | 23.3 | -12.64 | -2.64 | -15.73 | 111 |
| 34 | Agent (aggressive) | meta | 88.56 | -11.44 | 52 | 38.5 | -11.37 | -3.75 | -14.77 | 98 |
| 35 | Stochastic reversion · 1h | reversion | 87.77 | -12.23 | 198 | 47.0 | -20.30 | -3.72 | -22.50 | 393 |
| 36 | Bollinger breakout · 1h | breakout | 87.54 | -12.46 | 107 | 27.1 | -12.03 | -2.35 | -17.33 | 238 |
| 37 | Opening range 15m | breakout | 86.61 | -13.39 | 323 | 30.3 | -14.76 | -4.19 | -17.87 | 718 |
| 38 | Keltner breakout · 1h | breakout | 85.68 | -14.32 | 74 | 23.0 | -21.70 | -4.38 | -23.30 | 186 |
| 39 | Z-score reversion · 1h | reversion | 85.01 | -14.99 | 116 | 33.6 | -14.14 | -2.32 | -21.48 | 210 |
| 40 | Connors RSI(2) · 1h | reversion | 84.93 | -15.07 | 173 | 40.5 | -26.56 | -8.06 | -26.96 | 198 |
| 41 | EMA 20/50 cross · 1h | trend | 84.40 | -15.60 | 72 | 11.1 | -22.07 | -4.44 | -23.47 | 126 |
| 42 | RSI momentum · 1h | momentum | 83.58 | -16.42 | 104 | 15.4 | -22.47 | -4.52 | -23.14 | 205 |
| 43 | MACD cross · 1h | trend | 83.24 | -16.76 | 236 | 22.9 | -28.96 | -6.11 | -29.90 | 473 |
| 44 | Supertrend · 1h | trend | 83.09 | -16.91 | 114 | 14.0 | -28.19 | -6.13 | -29.63 | 225 |
| 45 | Ichimoku · 1h | trend | 82.58 | -17.42 | 66 | 12.1 | -22.13 | -4.62 | -24.25 | 110 |
| 46 | MFI reversion · 1h | reversion | 82.57 | -17.43 | 263 | 31.6 | -16.03 | -2.49 | -20.70 | 154 |
| 47 | Triple EMA stack · 1h | trend | 81.73 | -18.27 | 101 | 14.9 | -30.34 | -6.22 | -30.69 | 209 |
| 48 | Bollinger reversion · 1h | reversion | 81.31 | -18.69 | 179 | 37.4 | -28.89 | -5.89 | -31.14 | 372 |
| 49 | Williams %R · 1h | reversion | 81.15 | -18.85 | 228 | 46.1 | -34.65 | -5.92 | -35.61 | 542 |
| 50 | CCI reversion · 1h | reversion | 81.14 | -18.86 | 217 | 43.3 | -24.34 | -3.44 | -28.06 | 467 |
| 51 | MACD zero-line · 1h | trend | 80.61 | -19.39 | 107 | 15.9 | -23.25 | -4.98 | -24.56 | 219 |
| 52 | Donchian 20/10 · 1h | breakout | 79.81 | -20.19 | 99 | 20.2 | -24.39 | -4.66 | -27.27 | 212 |
| 53 | OBV trend · 1h | momentum | 79.05 | -20.95 | 206 | 17.5 | -32.66 | -6.93 | -32.99 | 304 |
| 54 | Agent (ML meta-label) | meta | 79.01 | -20.99 | 921 | 19.3 | -12.82 | -2.57 | -15.23 | 359 |
| 55 | Three white soldiers | momentum | 78.82 | -21.18 | 299 | 19.4 | -44.07 | -20.68 | -44.07 | 600 |
| 56 | RSI(14) reversion · 1h | reversion | 78.48 | -21.52 | 100 | 24.0 | -18.07 | -3.37 | -24.48 | 200 |
| 57 | Heikin-Ashi · 1h | trend | 76.77 | -23.23 | 286 | 22.4 | -44.73 | -10.26 | -45.66 | 661 |
| 58 | ROC + volume · 1h | momentum | 76.75 | -23.25 | 246 | 24.0 | -30.24 | -5.97 | -32.23 | 380 |
| 59 | Candlestick reversal · 1h | reversion | 76.40 | -23.60 | 271 | 28.0 | -33.76 | -6.31 | -35.48 | 567 |
| 60 | VWAP momentum · 1h | momentum | 75.40 | -24.60 | 546 | 21.1 | -49.58 | -11.20 | -50.29 | 1243 |
| 61 | EMA 9/21 cross · 1h | trend | 75.34 | -24.66 | 172 | 11.0 | -31.84 | -6.49 | -34.98 | 332 |
| 62 | Max aggression: 1-day momentum | meta | 67.37 | -32.63 | 19 | 26.3 | -41.81 | -2.86 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.31 | -44.69 | 758 | 22.2 | -74.39 | -26.98 | -74.56 | 1575 |
| 64 | Volume breakout | breakout | 54.18 | -45.82 | 456 | 12.9 | -62.58 | -26.50 | -62.64 | 799 |
| 65 | Donchian 55/20 | breakout | 51.25 | -48.75 | 605 | 19.2 | -71.85 | -23.77 | -72.35 | 1276 |
| 66 | Squeeze breakout | breakout | 51.23 | -48.77 | 589 | 14.4 | -67.25 | -28.54 | -67.82 | 1170 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -45.55 | -98.90 | 5159 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.24 | -23.67 | -79.30 | 1429 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.84 | -47.28 | -93.90 | 2545 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.19 | -89.31 | 1938 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.33 | -38.46 | -91.39 | 2344 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.64 | -31.05 | -90.66 | 2168 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.95 | -56.15 | -97.95 | 3536 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.17 | -60.64 | -96.19 | 3376 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.17 | -36.85 | -94.23 | 2477 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.51 | -34.69 | -82.82 | 1700 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -56.85 | -99.43 | 5784 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.68 | -43.47 | -92.71 | 2623 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.60 | -38.92 | -95.60 | 3392 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -83.28 | -99.78 | 6187 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.46 | -46.88 | -92.46 | 2342 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -66.45 | -97.72 | 3576 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -61.72 | -98.65 | 4806 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -58.15 | -94.59 | 2773 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.55 | -39.84 | -84.56 | 1818 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -69.06 | -99.61 | 6300 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -29.73 | -88.44 | 2228 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.06 | -19.37 | -77.49 | 1705 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.73 | -38.29 | -90.76 | 2297 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.31 | -49.85 | -96.33 | 3831 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.24 | -51.14 | -90.25 | 2140 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.29 | -17.99 | -76.42 | 1586 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.51 | -50.03 | -96.52 | 4209 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -110.41 | -99.92 | 8268 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T18:30 | Agent (ML meta-label) | buy | TSLA | 8.78 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T18:30 | CCI reversion · 1h | buy | LABU | 4.48 | — | rebalance up |
| 2026-10-26T18:30 | CCI reversion · 1h | buy | GOOGL | 4.44 | — | rebalance up |
| 2026-10-26T18:30 | CCI reversion · 1h | sell | TECL | 4.97 | 0.29 | exit signal |
| 2026-10-26T18:30 | CCI reversion · 1h | sell | AMD | 4.87 | 0.13 | exit signal |
| 2026-10-26T18:30 | RSI momentum · 1h | buy | PLTR | 16.72 | — | entry signal |
| 2026-10-26T18:30 | RSI momentum · 1h | buy | MSFT | 16.73 | — | entry signal |
| 2026-10-26T18:30 | RSI momentum · 1h | sell | TSLA | 4.28 | -0.02 | rebalance down |
| 2026-10-26T18:30 | RSI momentum · 1h | sell | TNA | 4.21 | -0.04 | rebalance down |
| 2026-10-26T18:30 | RSI momentum · 1h | sell | IWM | 4.30 | -0.02 | rebalance down |
| 2026-10-26T18:30 | VWAP momentum · 1h | buy | BITX | 3.97 | — | entry signal |
| 2026-10-26T18:30 | VWAP momentum · 1h | sell | AMZN | 4.70 | -0.02 | exit signal |
| 2026-10-26T18:30 | Heikin-Ashi · 1h | buy | PLTR | 1.32 | — | entry |
| 2026-10-26T18:30 | Heikin-Ashi · 1h | buy | MSFT | 6.98 | — | entry |
| 2026-10-26T18:30 | Heikin-Ashi · 1h | buy | AMD | 6.98 | — | entry |
| 2026-10-26T18:30 | Heikin-Ashi · 1h | sell | TNA | 7.61 | -0.10 | exit signal |
| 2026-10-26T18:30 | Heikin-Ashi · 1h | sell | IWM | 7.67 | -0.04 | exit signal |
| 2026-10-26T18:30 | Supertrend · 1h | buy | SOXL | 9.22 | — | entry |
| 2026-10-26T18:30 | Supertrend · 1h | buy | MSFT | 9.23 | — | entry |
| 2026-10-26T18:30 | Supertrend · 1h | buy | AMD | 9.23 | — | entry signal |
| 2026-10-26T18:30 | Supertrend · 1h | sell | TSLA | 4.63 | -0.03 | rebalance down |
| 2026-10-26T18:30 | Supertrend · 1h | sell | TQQQ | 4.57 | -0.03 | rebalance down |
| 2026-10-26T18:30 | Supertrend · 1h | sell | TECL | 4.67 | -0.00 | rebalance down |
| 2026-10-26T18:30 | Supertrend · 1h | sell | QQQ | 4.63 | -0.02 | rebalance down |
| 2026-10-26T18:30 | Supertrend · 1h | sell | NVDA | 4.61 | -0.02 | rebalance down |
| 2026-10-26T18:30 | Supertrend · 1h | sell | AAPL | 4.56 | -0.04 | rebalance down |
| 2026-10-26T18:30 | Triple EMA stack · 1h | buy | TNA | 4.13 | — | rebalance up |
| 2026-10-26T18:30 | Triple EMA stack · 1h | buy | PLTR | 6.41 | — | rebalance up |
| 2026-10-26T18:30 | Triple EMA stack · 1h | sell | SQQQ | 16.38 | -0.29 | exit signal |
| 2026-10-26T18:30 | Triple EMA stack · 1h | sell | AAPL | 16.34 | -0.12 | exit signal |
| 2026-10-26T18:30 | EMA 9/21 cross · 1h | buy | MSFT | 7.54 | — | entry |
| 2026-10-26T18:30 | EMA 9/21 cross · 1h | sell | AAPL | 8.35 | -0.02 | exit signal |
| 2026-10-26T18:30 | Three white soldiers | buy | MSFT | 19.71 | — | entry signal |
| 2026-10-26T18:25 | Agent (ML meta-label) | sell | TSLA | 8.78 | -0.03 | selected signal exited |
| 2026-10-26T18:20 | Agent (ML meta-label) | buy | TSLA | 6.99 | — | rebalance up |
| 2026-10-26T18:20 | Agent (ML meta-label) | sell | SOXL | 7.90 | 0.00 | selected signal exited |
| 2026-10-26T18:20 | Agent (aggressive) | buy | TSLA | 44.34 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T18:20 | Agent | buy | TSLA | 18.05 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T18:20 | Squeeze breakout | buy | MSFT | 12.81 | — | entry signal |
| 2026-10-26T18:20 | ROC + volume | sell | TECL | 13.84 | 0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 18:40:05.000112+00:00 -> 2026-10-26 18:50:05.000112+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
