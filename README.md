# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T07:45:05.000207+00:00 · 32824 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.11 (-9.89%)

Closed trades 98, win rate 39.8%, fees £3.14, max drawdown -10.53%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 6195 decisions in 1239 calls, $0.0864 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T07:45 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-23T07:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T07:45 | 1 / 4 / 0 | ETH-USD 51% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| Stochastic reversion | BITX | 1.69 | +8.43% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.33 | 7.33 | 0 | — | 8.89 | 4.77 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.52 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.35 | 2.02 | -5.17 | 42 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.93 | 0.94 | 0 | — | 3.62 | 1.70 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.39 | 0.39 | 82 | 43.9 | -11.99 | -3.36 | -13.74 | 154 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.45 | -0.55 | 10 | 50.0 | -11.15 | -0.95 | -27.80 | 24 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 5.35 | 2.62 | -2.17 | 100 |
| 11 | Hold SPY | benchmark | 98.30 | -1.70 | 0 | — | -0.18 | -0.06 | -3.13 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.59 | -3.41 | 118 | 31.4 | -1.83 | -1.07 | -6.22 | 193 |
| 15 | Hold BTC | benchmark | 96.47 | -3.53 | 0 | — | 1.52 | 0.43 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.90 | -4.10 | 0 | — | -0.61 | -0.20 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.39 | 0.86 | -7.93 | 8 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -5.46 | -2.33 | -7.04 | 1 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 5.31 | 1.77 | -8.68 | 182 |
| 21 | Copy: Insider buying | copy | 94.38 | -5.62 | 25 | 40.0 | -14.57 | -2.78 | -20.68 | 71 |
| 22 | Trend pullback · 1h | trend | 93.78 | -6.21 | 95 | 23.2 | -21.51 | -7.07 | -21.85 | 115 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -10.42 | -3.24 | -17.21 | 545 |
| 24 | Donchian 55/20 · 1h | breakout | 93.08 | -6.92 | 48 | 16.7 | -16.14 | -3.66 | -17.29 | 98 |
| 25 | Parabolic SAR · 1h | trend | 93.06 | -6.94 | 115 | 26.1 | -20.04 | -4.74 | -24.17 | 254 |
| 26 | Daily: Momentum burst | daily | 92.67 | -7.33 | 8 | 12.5 | -16.72 | -3.23 | -19.90 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.19 | -7.81 | 104 | 19.2 | -10.52 | -2.16 | -13.49 | 255 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -10.60 | -7.35 | -11.63 | 206 |
| 31 | Daily: Bullish score | daily | 89.83 | -10.17 | 8 | 0.0 | -7.63 | -0.98 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.47 | -10.53 | 104 | 27.9 | -11.78 | -2.33 | -15.96 | 240 |
| 33 | Volume breakout · 1h | breakout | 89.16 | -10.85 | 101 | 22.8 | -13.01 | -2.77 | -16.13 | 112 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 89.05 | -10.95 | 0 | — | -5.36 | -0.78 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -11.87 | -4.10 | -14.77 | 94 |
| 36 | EMA 20/50 cross · 1h | trend | 87.65 | -12.35 | 68 | 11.8 | -21.45 | -4.27 | -24.06 | 137 |
| 37 | Stochastic reversion · 1h | reversion | 87.39 | -12.61 | 183 | 45.9 | -19.79 | -3.73 | -22.47 | 382 |
| 38 | Supertrend · 1h | trend | 87.03 | -12.97 | 104 | 15.4 | -22.82 | -4.80 | -25.65 | 211 |
| 39 | RSI momentum · 1h | momentum | 86.75 | -13.25 | 96 | 16.7 | -20.29 | -4.34 | -22.08 | 215 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.69 | -4.58 | -17.87 | 683 |
| 41 | Keltner breakout · 1h | breakout | 86.25 | -13.76 | 73 | 23.3 | -22.74 | -4.84 | -24.32 | 190 |
| 42 | Connors RSI(2) · 1h | reversion | 85.11 | -14.89 | 168 | 39.9 | -26.56 | -8.16 | -26.65 | 193 |
| 43 | MACD cross · 1h | trend | 85.07 | -14.93 | 216 | 23.1 | -22.47 | -4.49 | -26.08 | 451 |
| 44 | Triple EMA stack · 1h | trend | 84.46 | -15.54 | 96 | 15.6 | -25.06 | -4.99 | -27.76 | 210 |
| 45 | Ichimoku · 1h | trend | 83.85 | -16.15 | 65 | 12.3 | -23.76 | -4.96 | -25.41 | 110 |
| 46 | Z-score reversion · 1h | reversion | 83.37 | -16.62 | 104 | 33.7 | -15.28 | -2.61 | -21.48 | 192 |
| 47 | Donchian 20/10 · 1h | breakout | 82.76 | -17.24 | 93 | 20.4 | -23.06 | -4.47 | -25.99 | 215 |
| 48 | OBV trend · 1h | momentum | 82.36 | -17.64 | 198 | 17.7 | -30.79 | -6.77 | -32.67 | 305 |
| 49 | MACD zero-line · 1h | trend | 82.24 | -17.76 | 103 | 15.5 | -21.06 | -4.41 | -24.69 | 216 |
| 50 | Williams %R · 1h | reversion | 82.23 | -17.77 | 209 | 45.0 | -33.98 | -6.04 | -36.69 | 510 |
| 51 | MFI reversion · 1h | reversion | 82.11 | -17.89 | 245 | 31.4 | -17.27 | -2.80 | -20.59 | 141 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -43.33 | -20.89 | -43.44 | 584 |
| 53 | CCI reversion · 1h | reversion | 80.88 | -19.12 | 195 | 43.1 | -25.75 | -3.86 | -28.17 | 434 |
| 54 | Agent (ML meta-label) | meta | 80.22 | -19.77 | 835 | 18.9 | -13.63 | -2.44 | -16.68 | 381 |
| 55 | Bollinger reversion · 1h | reversion | 80.18 | -19.82 | 168 | 35.1 | -31.28 | -6.57 | -32.19 | 356 |
| 56 | Heikin-Ashi · 1h | trend | 79.95 | -20.05 | 261 | 23.4 | -42.29 | -9.86 | -43.38 | 646 |
| 57 | ROC + volume · 1h | momentum | 79.49 | -20.51 | 235 | 23.8 | -29.67 | -5.93 | -31.10 | 378 |
| 58 | EMA 9/21 cross · 1h | trend | 78.25 | -21.75 | 155 | 11.6 | -29.06 | -5.94 | -32.74 | 316 |
| 59 | RSI(14) reversion · 1h | reversion | 77.90 | -22.10 | 90 | 23.3 | -15.11 | -2.80 | -23.51 | 184 |
| 60 | Candlestick reversal · 1h | reversion | 77.38 | -22.62 | 246 | 28.9 | -34.78 | -6.59 | -36.11 | 534 |
| 61 | VWAP momentum · 1h | momentum | 77.06 | -22.94 | 499 | 21.4 | -49.33 | -11.47 | -49.61 | 1192 |
| 62 | Max aggression: 1-day momentum | meta | 67.94 | -32.06 | 18 | 27.8 | -41.16 | -2.84 | -48.56 | 41 |
| 63 | ROC + volume | momentum | 58.45 | -41.55 | 696 | 23.0 | -74.63 | -27.15 | -74.64 | 1540 |
| 64 | Volume breakout | breakout | 57.69 | -42.31 | 413 | 13.3 | -60.14 | -26.03 | -60.14 | 753 |
| 65 | Donchian 55/20 | breakout | 54.97 | -45.03 | 550 | 19.6 | -70.55 | -23.89 | -70.70 | 1238 |
| 66 | Squeeze breakout | breakout | 54.49 | -45.51 | 539 | 14.3 | -65.69 | -28.42 | -65.75 | 1131 |
| 67 | EMA 20/50 cross | trend | 54.13 | -45.87 | 591 | 20.5 | -77.73 | -22.92 | -78.22 | 1380 |
| 68 | RSI(14) reversion | reversion | 53.11 | -46.89 | 808 | 26.0 | -76.45 | -19.69 | -76.66 | 1650 |
| 69 | VWAP reversion | reversion | 50.67 | -49.33 | 809 | 25.0 | -74.50 | -17.56 | -74.71 | 1540 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.55 | -44.03 | -98.58 | 4918 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -46.69 | -93.37 | 2464 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.07 | -29.53 | -88.22 | 1848 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.88 | -37.52 | -90.94 | 2276 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.90 | -30.73 | -89.94 | 2118 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.50 | -51.58 | -97.52 | 3375 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.77 | -60.55 | -95.78 | 3267 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.59 | -35.13 | -93.62 | 2413 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.99 | -35.32 | -82.03 | 1651 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.29 | -52.75 | -99.29 | 5587 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.99 | -41.38 | -92.04 | 2547 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.06 | -39.66 | -95.07 | 3311 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -80.09 | -99.72 | 5982 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.61 | -44.61 | -91.62 | 2262 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -64.32 | -97.36 | 3467 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.40 | -56.84 | -98.42 | 4636 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.99 | -59.09 | -94.01 | 2704 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.25 | -40.11 | -83.31 | 1756 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -63.10 | -99.51 | 6068 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.47 | -28.64 | -87.49 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.85 | -37.69 | -89.92 | 2216 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.80 | -46.29 | -95.81 | 3686 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.10 | -48.57 | -89.19 | 2053 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.96 | -47.06 | -95.99 | 4061 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -107.12 | -99.89 | 8018 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T07:30 | Agent (ML meta-label) | buy | ETH-USD | 3.34 | — | entry |
| 2026-10-23T07:30 | CCI reversion · 1h | buy | XRP-USD | 6.57 | — | entry |
| 2026-10-23T07:30 | Candlestick reversal · 1h | sell | BTC-USD | 4.81 | -0.03 | target is flat |
| 2026-10-23T07:30 | ROC + volume · 1h | sell | XRP-USD | 19.79 | -0.13 | target is flat |
| 2026-10-23T07:30 | ROC + volume · 1h | sell | ETH-USD | 19.80 | -0.13 | target is flat |
| 2026-10-23T07:30 | Heikin-Ashi · 1h | buy | DOGE-USD | 20.00 | — | entry |
| 2026-10-23T07:20 | Agent (ML meta-label) | sell | XRP-USD | 3.46 | -0.02 | selected signal exited |
| 2026-10-23T07:20 | CCI reversion · 1h | buy | ETH-USD | 4.61 | — | rebalance up |
| 2026-10-23T07:20 | CCI reversion · 1h | buy | BTC-USD | 4.63 | — | rebalance up |
| 2026-10-23T07:20 | CCI reversion · 1h | sell | XRP-USD | 13.47 | 0.02 | target is flat |
| 2026-10-23T07:20 | ROC + volume · 1h | buy | XRP-USD | 19.92 | — | entry |
| 2026-10-23T07:20 | Heikin-Ashi · 1h | sell | DOGE-USD | 19.97 | -0.03 | target is flat |
| 2026-10-23T07:16 | Candlestick reversal · 1h | buy | BTC-USD | 4.84 | — | entry |
| 2026-10-23T07:16 | ROC + volume · 1h | buy | ETH-USD | 19.94 | — | entry |
| 2026-10-23T07:15 | Agent (ML meta-label) | buy | XRP-USD | 3.49 | — | entry |
| 2026-10-23T07:00 | Williams %R · 1h | sell | SOL-USD | 8.24 | -0.01 | exit signal |
| 2026-10-23T07:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 6.22 | — | entry signal |
| 2026-10-23T06:55 | Agent (ML meta-label) | sell | XRP-USD | 3.62 | -0.02 | selected signal exited |
| 2026-10-23T06:50 | Agent (ML meta-label) | buy | XRP-USD | 3.65 | — | entry |
| 2026-10-23T06:40 | Agent (ML meta-label) | sell | XRP-USD | 1.05 | -0.01 | selected signal exited |
| 2026-10-23T06:30 | Volume breakout | sell | SOL-USD | 14.34 | -0.11 | exit signal |
| 2026-10-23T06:25 | Agent (ML meta-label) | buy | XRP-USD | 1.06 | — | entry |
| 2026-10-23T06:20 | Volume breakout | buy | SOL-USD | 14.45 | — | entry signal |
| 2026-10-23T06:05 | Volume breakout | sell | XRP-USD | 14.38 | -0.08 | exit signal |
| 2026-10-23T06:00 | Agent (ML meta-label) | sell | XRP-USD | 3.33 | -0.01 | selected signal exited |
| 2026-10-23T06:00 | Williams %R · 1h | sell | XRP-USD | 8.21 | 0.07 | exit signal |
| 2026-10-23T06:00 | Stochastic reversion · 1h | sell | XRP-USD | 2.41 | 0.03 | exit signal |
| 2026-10-23T06:00 | ADX DI cross · 1h | buy | SOL-USD | 6.59 | — | entry signal |
| 2026-10-23T06:00 | ADX DI cross · 1h | buy | DOGE-USD | 15.36 | — | entry signal |
| 2026-10-23T05:45 | Donchian 55/20 | buy | XRP-USD | 13.76 | — | entry signal |
| 2026-10-23T05:20 | Agent (ML meta-label) | buy | XRP-USD | 3.34 | — | entry |
| 2026-10-23T05:17 | Agent (ML meta-label) | sell | XRP-USD | 3.63 | -0.02 | selected signal exited |
| 2026-10-23T05:15 | Agent (ML meta-label) | buy | XRP-USD | 3.65 | — | entry |
| 2026-10-23T05:15 | Donchian 55/20 | buy | DOGE-USD | 13.76 | — | entry signal |
| 2026-10-23T05:10 | Volume breakout | buy | XRP-USD | 14.47 | — | entry signal |
| 2026-10-23T05:00 | ADX DI cross · 1h | sell | ETH-USD | 21.95 | -0.34 | exit signal |
| 2026-10-23T04:46 | Agent (ML meta-label) | sell | XRP-USD | 3.80 | -0.03 | selected signal exited |
| 2026-10-23T04:30 | Donchian 55/20 | sell | ETH-USD | 13.74 | -0.15 | exit signal |
| 2026-10-23T04:30 | Donchian 55/20 | sell | BTC-USD | 13.76 | -0.12 | exit signal |
| 2026-10-23T04:20 | Donchian 55/20 | sell | DOGE-USD | 14.00 | -0.01 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 07:45:05.000207+00:00 -> 2026-10-23 07:55:05.000207+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
