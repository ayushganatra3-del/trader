# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T08:45:05.000127+00:00 · 32871 ticks

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

Today: 6900 decisions in 1380 calls, $0.0963 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T08:45 | 1 / 4 / 0 | DOGE-USD 16% |  |
| Breezy | 2026-10-23T08:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T08:45 | 3 / 2 / 0 | BTC-USD 54% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.39 | 7.39 | 0 | — | 8.89 | 4.77 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.52 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.35 | 2.02 | -5.17 | 42 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.99 | 0.99 | 0 | — | 3.62 | 1.70 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.41 | 0.41 | 82 | 43.9 | -11.99 | -3.36 | -13.74 | 154 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.50 | -0.50 | 10 | 50.0 | -11.15 | -0.95 | -27.80 | 24 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 5.35 | 2.62 | -2.17 | 100 |
| 11 | Hold SPY | benchmark | 98.35 | -1.65 | 0 | — | -0.18 | -0.06 | -3.13 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 14 | Hold BTC | benchmark | 96.71 | -3.29 | 0 | — | 1.72 | 0.46 | -8.68 | 1 |
| 15 | Agent (rotation) | meta | 96.61 | -3.39 | 118 | 31.4 | -1.83 | -1.07 | -6.22 | 193 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.95 | -4.05 | 0 | — | -0.61 | -0.20 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.39 | 0.86 | -7.93 | 8 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 95.60 | -4.40 | 0 | — | -5.46 | -2.33 | -7.04 | 1 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 5.31 | 1.77 | -8.68 | 182 |
| 21 | Copy: Insider buying | copy | 94.43 | -5.57 | 25 | 40.0 | -14.57 | -2.78 | -20.68 | 71 |
| 22 | Trend pullback · 1h | trend | 93.80 | -6.20 | 95 | 23.2 | -21.51 | -7.07 | -21.85 | 115 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -10.42 | -3.24 | -17.21 | 545 |
| 24 | Parabolic SAR · 1h | trend | 93.11 | -6.89 | 115 | 26.1 | -20.04 | -4.74 | -24.17 | 254 |
| 25 | Donchian 55/20 · 1h | breakout | 93.09 | -6.91 | 48 | 16.7 | -16.14 | -3.66 | -17.29 | 98 |
| 26 | Daily: Momentum burst | daily | 92.71 | -7.29 | 8 | 12.5 | -16.72 | -3.23 | -19.90 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.30 | -7.70 | 104 | 19.2 | -10.41 | -2.13 | -13.49 | 255 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -10.60 | -7.35 | -11.63 | 206 |
| 31 | Daily: Bullish score | daily | 89.88 | -10.12 | 8 | 0.0 | -7.63 | -0.98 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.48 | -10.52 | 104 | 27.9 | -11.78 | -2.33 | -15.96 | 240 |
| 33 | Volume breakout · 1h | breakout | 89.17 | -10.83 | 101 | 22.8 | -13.01 | -2.77 | -16.13 | 112 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 89.09 | -10.90 | 0 | — | -5.36 | -0.78 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -11.87 | -4.10 | -14.77 | 94 |
| 36 | EMA 20/50 cross · 1h | trend | 87.69 | -12.31 | 68 | 11.8 | -21.45 | -4.27 | -24.06 | 137 |
| 37 | Stochastic reversion · 1h | reversion | 87.42 | -12.58 | 183 | 45.9 | -19.79 | -3.73 | -22.47 | 382 |
| 38 | Supertrend · 1h | trend | 87.06 | -12.94 | 104 | 15.4 | -22.82 | -4.80 | -25.65 | 211 |
| 39 | RSI momentum · 1h | momentum | 86.78 | -13.22 | 96 | 16.7 | -20.29 | -4.34 | -22.08 | 215 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.69 | -4.58 | -17.87 | 683 |
| 41 | Keltner breakout · 1h | breakout | 86.26 | -13.74 | 73 | 23.3 | -22.74 | -4.84 | -24.32 | 190 |
| 42 | MACD cross · 1h | trend | 85.22 | -14.78 | 216 | 23.1 | -22.36 | -4.45 | -26.08 | 451 |
| 43 | Connors RSI(2) · 1h | reversion | 85.13 | -14.87 | 168 | 39.9 | -26.56 | -8.16 | -26.65 | 193 |
| 44 | Triple EMA stack · 1h | trend | 84.51 | -15.49 | 96 | 15.6 | -25.06 | -4.99 | -27.76 | 210 |
| 45 | Ichimoku · 1h | trend | 83.86 | -16.14 | 65 | 12.3 | -23.76 | -4.96 | -25.41 | 110 |
| 46 | Z-score reversion · 1h | reversion | 83.48 | -16.52 | 104 | 33.7 | -15.22 | -2.59 | -21.48 | 192 |
| 47 | Donchian 20/10 · 1h | breakout | 82.79 | -17.21 | 93 | 20.4 | -23.06 | -4.47 | -25.99 | 215 |
| 48 | OBV trend · 1h | momentum | 82.41 | -17.59 | 198 | 17.7 | -30.79 | -6.77 | -32.67 | 305 |
| 49 | MACD zero-line · 1h | trend | 82.25 | -17.75 | 103 | 15.5 | -21.06 | -4.41 | -24.69 | 216 |
| 50 | Williams %R · 1h | reversion | 82.25 | -17.75 | 209 | 45.0 | -33.98 | -6.04 | -36.69 | 510 |
| 51 | MFI reversion · 1h | reversion | 82.15 | -17.85 | 246 | 31.3 | -17.38 | -2.83 | -20.59 | 141 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -43.31 | -20.86 | -43.43 | 583 |
| 53 | CCI reversion · 1h | reversion | 81.02 | -18.98 | 195 | 43.1 | -25.66 | -3.84 | -28.17 | 434 |
| 54 | Agent (ML meta-label) | meta | 80.25 | -19.75 | 836 | 18.9 | -11.56 | -2.08 | -16.19 | 369 |
| 55 | Bollinger reversion · 1h | reversion | 80.22 | -19.78 | 168 | 35.1 | -31.28 | -6.57 | -32.19 | 356 |
| 56 | Heikin-Ashi · 1h | trend | 80.04 | -19.96 | 261 | 23.4 | -42.24 | -9.84 | -43.38 | 646 |
| 57 | ROC + volume · 1h | momentum | 79.50 | -20.50 | 235 | 23.8 | -29.67 | -5.93 | -31.10 | 378 |
| 58 | EMA 9/21 cross · 1h | trend | 78.31 | -21.69 | 155 | 11.6 | -29.04 | -5.94 | -32.74 | 316 |
| 59 | RSI(14) reversion · 1h | reversion | 77.98 | -22.02 | 90 | 23.3 | -15.02 | -2.78 | -23.51 | 184 |
| 60 | Candlestick reversal · 1h | reversion | 77.40 | -22.60 | 248 | 29.0 | -34.80 | -6.59 | -36.11 | 534 |
| 61 | VWAP momentum · 1h | momentum | 77.10 | -22.90 | 499 | 21.4 | -49.27 | -11.45 | -49.58 | 1191 |
| 62 | Max aggression: 1-day momentum | meta | 67.94 | -32.06 | 18 | 27.8 | -41.16 | -2.84 | -48.56 | 41 |
| 63 | ROC + volume | momentum | 58.45 | -41.55 | 696 | 23.0 | -74.63 | -27.15 | -74.64 | 1540 |
| 64 | Volume breakout | breakout | 57.69 | -42.31 | 413 | 13.3 | -60.14 | -26.03 | -60.14 | 753 |
| 65 | Donchian 55/20 | breakout | 54.97 | -45.03 | 551 | 19.6 | -70.55 | -23.90 | -70.72 | 1238 |
| 66 | Squeeze breakout | breakout | 54.45 | -45.55 | 539 | 14.3 | -65.72 | -28.47 | -65.78 | 1132 |
| 67 | EMA 20/50 cross | trend | 54.25 | -45.75 | 591 | 20.5 | -77.71 | -22.88 | -78.22 | 1381 |
| 68 | RSI(14) reversion | reversion | 53.11 | -46.89 | 808 | 26.0 | -76.45 | -19.69 | -76.66 | 1650 |
| 69 | VWAP reversion | reversion | 50.67 | -49.33 | 809 | 25.0 | -74.50 | -17.56 | -74.71 | 1540 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.55 | -44.04 | -98.58 | 4919 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.37 | -47.22 | -93.42 | 2469 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.09 | -29.59 | -88.23 | 1849 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.90 | -37.64 | -90.96 | 2278 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.94 | -30.86 | -89.98 | 2121 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.51 | -52.09 | -97.53 | 3379 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.78 | -60.93 | -95.80 | 3270 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -35.14 | -93.65 | 2415 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.02 | -35.50 | -82.07 | 1653 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.29 | -53.00 | -99.30 | 5589 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.00 | -41.45 | -92.06 | 2547 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.09 | -39.89 | -95.10 | 3315 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -81.09 | -99.73 | 5988 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.63 | -44.83 | -91.64 | 2265 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -64.87 | -97.37 | 3472 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.41 | -57.67 | -98.43 | 4641 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.99 | -59.15 | -94.01 | 2705 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.25 | -40.11 | -83.31 | 1756 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -63.76 | -99.52 | 6071 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.48 | -28.68 | -87.50 | 2145 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.88 | -38.00 | -89.95 | 2218 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.81 | -46.56 | -95.82 | 3689 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.09 | -48.57 | -89.19 | 2053 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.96 | -47.23 | -96.00 | 4063 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -108.20 | -99.89 | 8023 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T08:45 | Squeeze breakout | buy | DOGE-USD | 13.62 | — | entry signal |
| 2026-10-23T08:30 | EMA 20/50 cross | buy | BTC-USD | 5.33 | — | entry signal |
| 2026-10-23T08:00 | Agent (ML meta-label) | buy | XRP-USD | 3.82 | — | entry |
| 2026-10-23T08:00 | Agent (ML meta-label) | sell | ETH-USD | 3.32 | -0.02 | selected signal exited |
| 2026-10-23T08:00 | MFI reversion · 1h | buy | SOL-USD | 4.80 | — | rebalance up |
| 2026-10-23T08:00 | MFI reversion · 1h | sell | BTC-USD | 4.80 | -0.02 | exit signal |
| 2026-10-23T08:00 | Candlestick reversal · 1h | sell | XRP-USD | 4.40 | 0.03 | exit signal |
| 2026-10-23T08:00 | Candlestick reversal · 1h | sell | ETH-USD | 5.15 | -0.01 | exit signal |
| 2026-10-23T07:50 | Donchian 55/20 | sell | XRP-USD | 13.63 | -0.12 | stop-loss |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 08:45:05.000127+00:00 -> 2026-10-23 08:55:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
