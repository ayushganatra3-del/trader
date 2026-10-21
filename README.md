# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T23:20:05.000127+00:00 · 31203 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.67 (-9.33%)

Closed trades 93, win rate 40.9%, fees £3.03, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-21 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.42 · VIX 16.68 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 39918 decisions in 3372 calls, $0.4940 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T23:20 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-10-21T23:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T23:20 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.05 | 6.05 | 0 | — | 8.54 | 4.02 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.62 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.81 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.21 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.52 | 1.52 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.25 | 0.25 | 4 | 50.0 | 9.05 | 1.92 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.64 | -0.36 | 0 | — | 2.33 | 1.07 | -5.02 | 1 |
| 11 | Hold BTC | benchmark | 99.63 | -0.37 | 0 | — | 13.92 | 2.10 | -8.68 | 1 |
| 12 | Hold SPY | benchmark | 99.42 | -0.58 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.56 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.97 | -4.04 | 21 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.52 | -2.48 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.08 | -2.92 | 0 | — | -4.00 | -1.53 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.79 | -5.83 | 1 |
| 18 | Copy: Insider buying | copy | 96.71 | -3.29 | 25 | 40.0 | -11.33 | -1.94 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.78 | -4.22 | 117 | 30.8 | -8.38 | -4.92 | -8.45 | 235 |
| 20 | Donchian 55/20 · 1h | breakout | 95.75 | -4.25 | 41 | 17.1 | -14.74 | -3.02 | -16.00 | 103 |
| 21 | ADX DI cross · 1h | trend | 95.60 | -4.40 | 91 | 19.8 | -11.00 | -2.02 | -16.14 | 260 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.18 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 94.95 | -5.05 | 6 | 16.7 | -9.30 | -1.38 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.87 | -5.13 | 92 | 23.9 | -20.40 | -6.41 | -20.58 | 129 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.56 | 2.05 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.11 | -17.26 | 568 |
| 27 | Parabolic SAR · 1h | trend | 92.96 | -7.04 | 111 | 25.2 | -16.10 | -3.57 | -19.79 | 272 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 92.94 | -7.06 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 29 | Squeeze breakout · 1h | breakout | 92.67 | -7.33 | 49 | 22.4 | -2.33 | -0.49 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.21 | -7.79 | 8 | 0.0 | -2.44 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.10 | -7.90 | 92 | 29.3 | -9.47 | -1.69 | -15.29 | 263 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.95 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -20.62 | -5.70 | -21.15 | 267 |
| 34 | Volume breakout · 1h | breakout | 90.48 | -9.52 | 94 | 24.5 | -12.58 | -2.25 | -13.95 | 110 |
| 35 | Supertrend · 1h | trend | 90.06 | -9.94 | 88 | 12.5 | -20.87 | -4.19 | -26.66 | 218 |
| 36 | Connors RSI(2) · 1h | reversion | 89.58 | -10.42 | 159 | 42.1 | -22.23 | -6.70 | -23.74 | 196 |
| 37 | RSI momentum · 1h | momentum | 89.58 | -10.42 | 84 | 16.7 | -20.18 | -4.05 | -21.62 | 222 |
| 38 | Stochastic reversion · 1h | reversion | 89.56 | -10.44 | 169 | 47.3 | -13.60 | -2.23 | -22.24 | 363 |
| 39 | EMA 20/50 cross · 1h | trend | 88.84 | -11.16 | 62 | 12.9 | -20.95 | -3.64 | -23.57 | 140 |
| 40 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.22 | -19.07 | 704 |
| 41 | Keltner breakout · 1h | breakout | 87.78 | -12.22 | 66 | 22.7 | -18.76 | -3.56 | -25.20 | 204 |
| 42 | MACD cross · 1h | trend | 87.49 | -12.51 | 201 | 21.9 | -23.79 | -4.53 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -20.94 | -4.39 | -20.95 | 124 |
| 44 | Z-score reversion · 1h | reversion | 86.80 | -13.20 | 102 | 34.3 | -11.48 | -1.79 | -21.32 | 196 |
| 45 | Ichimoku · 1h | trend | 86.80 | -13.20 | 60 | 13.3 | -17.95 | -3.39 | -20.25 | 118 |
| 46 | Donchian 20/10 · 1h | breakout | 85.88 | -14.12 | 83 | 19.3 | -19.97 | -3.72 | -29.03 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.66 | -14.34 | 92 | 15.2 | -25.75 | -4.73 | -27.29 | 221 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.47 | -2.01 | -21.11 | 141 |
| 49 | Agent (ML meta-label) | meta | 84.65 | -15.36 | 735 | 20.1 | -15.01 | -3.07 | -18.29 | 376 |
| 50 | MACD zero-line · 1h | trend | 84.54 | -15.46 | 92 | 15.2 | -23.36 | -4.58 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 83.91 | -16.09 | 188 | 17.6 | -31.69 | -5.99 | -32.25 | 310 |
| 52 | ROC + volume · 1h | momentum | 82.89 | -17.11 | 214 | 23.4 | -25.74 | -4.59 | -32.91 | 394 |
| 53 | Williams %R · 1h | reversion | 82.60 | -17.40 | 199 | 44.7 | -31.50 | -4.92 | -36.62 | 517 |
| 54 | Bollinger reversion · 1h | reversion | 82.60 | -17.40 | 163 | 36.2 | -29.10 | -5.66 | -32.84 | 348 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.61 | -18.33 | -46.47 | 606 |
| 56 | CCI reversion · 1h | reversion | 82.13 | -17.87 | 188 | 43.6 | -20.26 | -2.65 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.42 | -18.58 | 251 | 23.9 | -42.85 | -9.25 | -46.38 | 678 |
| 58 | EMA 9/21 cross · 1h | trend | 80.91 | -19.09 | 143 | 10.5 | -26.91 | -5.26 | -29.94 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 80.89 | -19.11 | 85 | 24.7 | -16.91 | -2.91 | -24.99 | 172 |
| 60 | VWAP momentum · 1h | momentum | 79.05 | -20.95 | 480 | 21.7 | -46.62 | -8.96 | -52.83 | 1253 |
| 61 | Candlestick reversal · 1h | reversion | 79.03 | -20.97 | 231 | 30.3 | -37.91 | -6.97 | -41.83 | 535 |
| 62 | Max aggression: 1-day momentum | meta | 77.16 | -22.84 | 17 | 29.4 | -34.21 | -2.15 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -78.01 | -22.65 | -78.97 | 1721 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.60 | -20.24 | -64.98 | 866 |
| 65 | RSI(14) reversion | reversion | 56.88 | -43.12 | 763 | 27.1 | -74.48 | -16.71 | -74.90 | 1612 |
| 66 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.16 | -19.67 | -74.04 | 1283 |
| 67 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.07 | -23.23 | -67.93 | 1208 |
| 68 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.94 | -19.67 | -80.87 | 1439 |
| 69 | VWAP reversion | reversion | 54.37 | -45.63 | 765 | 26.0 | -70.95 | -14.35 | -72.15 | 1462 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.77 | -31.53 | -98.82 | 5275 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.04 | -34.99 | -94.26 | 2598 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.88 | -23.74 | -88.68 | 1895 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.17 | -28.25 | -91.74 | 2364 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.45 | -26.61 | -91.45 | 2278 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -35.49 | -97.82 | 3507 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.96 | -39.22 | -97.03 | 3615 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.57 | -28.21 | -94.73 | 2571 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.02 | -28.28 | -83.52 | 1736 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -37.56 | -99.40 | 5728 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.13 | -30.06 | -92.67 | 2626 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -32.27 | -95.92 | 3484 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -43.68 | -99.77 | 6161 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -30.99 | -91.92 | 2338 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -41.00 | -97.82 | 3639 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -38.05 | -98.52 | 4703 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.30 | -36.91 | -94.46 | 2807 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.57 | -29.03 | -84.44 | 1805 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -40.66 | -99.55 | 6186 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.08 | -23.12 | -87.14 | 2149 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.79 | -26.73 | -88.06 | 2143 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -34.03 | -96.03 | 3767 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.50 | -34.63 | -89.52 | 2101 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.88 | -34.64 | -95.90 | 4086 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.34 | -99.91 | 8297 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T23:16 | RSI(14) reversion | buy | XRP-USD | 14.25 | — | entry signal |
| 2026-10-21T23:16 | RSI(14) reversion | buy | SOL-USD | 14.25 | — | entry signal |
| 2026-10-21T23:14 | Volume breakout · 1h | buy | BTC-USD | 5.12 | — | rebalance up |
| 2026-10-21T23:10 | Squeeze breakout · 1h | sell | SOL-USD | 23.08 | -0.32 | stop-loss |
| 2026-10-21T23:10 | Keltner breakout · 1h | sell | SOL-USD | 8.71 | -0.09 | stop-loss |
| 2026-10-21T23:10 | Bollinger breakout · 1h | sell | SOL-USD | 5.37 | -0.05 | stop-loss |
| 2026-10-21T23:05 | ROC + volume · 1h | buy | SOL-USD | 2.48 | — | entry |
| 2026-10-21T23:05 | ROC + volume · 1h | sell | DOGE-USD | 1.99 | -0.04 | stop-loss |
| 2026-10-21T23:05 | RSI(14) reversion | sell | XRP-USD | 14.16 | -0.17 | stop-loss |
| 2026-10-21T23:05 | RSI(14) reversion | sell | DOGE-USD | 14.18 | -0.15 | stop-loss |
| 2026-10-21T23:05 | EMA 20/50 cross | sell | BTC-USD | 13.80 | -0.03 | exit signal |
| 2026-10-21T23:00 | Connors RSI(2) · 1h | buy | XRP-USD | 22.46 | — | entry signal |
| 2026-10-21T23:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 22.46 | — | entry signal |
| 2026-10-21T23:00 | Volume breakout · 1h | sell | XRP-USD | 10.04 | -0.13 | exit signal |
| 2026-10-21T23:00 | Volume breakout · 1h | sell | ETH-USD | 12.87 | -0.01 | exit signal |
| 2026-10-21T23:00 | Squeeze breakout · 1h | sell | ETH-USD | 22.25 | -0.39 | stop-loss |
| 2026-10-21T23:00 | Keltner breakout · 1h | sell | XRP-USD | 8.33 | -0.12 | stop-loss |
| 2026-10-21T23:00 | Keltner breakout · 1h | sell | ETH-USD | 9.74 | -0.11 | stop-loss |
| 2026-10-21T23:00 | Bollinger breakout · 1h | sell | XRP-USD | 7.61 | -0.01 | stop-loss |
| 2026-10-21T23:00 | Bollinger breakout · 1h | sell | ETH-USD | 7.65 | -0.01 | stop-loss |
| 2026-10-21T23:00 | VWAP momentum · 1h | sell | SOL-USD | 3.56 | -0.00 | exit signal |
| 2026-10-21T23:00 | VWAP momentum · 1h | sell | DOGE-USD | 3.54 | -0.01 | exit signal |
| 2026-10-21T23:00 | Parabolic SAR · 1h | buy | SOL-USD | 13.31 | — | entry |
| 2026-10-21T23:00 | Parabolic SAR · 1h | sell | XRP-USD | 13.57 | 0.63 | exit signal |
| 2026-10-21T23:00 | Parabolic SAR · 1h | sell | ETH-USD | 13.36 | 0.29 | exit signal |
| 2026-10-21T23:00 | Parabolic SAR · 1h | sell | DOGE-USD | 13.28 | 0.26 | exit signal |
| 2026-10-21T23:00 | MACD cross · 1h | sell | XRP-USD | 5.82 | 0.07 | exit signal |
| 2026-10-21T23:00 | MACD cross · 1h | sell | ETH-USD | 4.04 | 0.00 | exit signal |
| 2026-10-21T22:25 | RSI(14) reversion | buy | XRP-USD | 14.33 | — | entry signal |
| 2026-10-21T22:25 | RSI(14) reversion | buy | DOGE-USD | 14.33 | — | entry signal |
| 2026-10-21T22:20 | Squeeze breakout · 1h | buy | SOL-USD | 8.51 | — | rebalance up |
| 2026-10-21T22:20 | Squeeze breakout · 1h | sell | DOGE-USD | 18.46 | 0.13 | stop-loss |
| 2026-10-21T22:20 | Keltner breakout · 1h | buy | SOL-USD | 8.80 | — | entry |
| 2026-10-21T22:20 | Keltner breakout · 1h | sell | DOGE-USD | 9.70 | -0.11 | stop-loss |
| 2026-10-21T22:20 | Bollinger breakout · 1h | buy | SOL-USD | 5.43 | — | entry |
| 2026-10-21T22:20 | Bollinger breakout · 1h | sell | DOGE-USD | 7.62 | -0.03 | stop-loss |
| 2026-10-21T22:05 | Squeeze breakout | sell | ETH-USD | 13.94 | -0.13 | stop-loss |
| 2026-10-21T22:00 | Heikin-Ashi · 1h | sell | XRP-USD | 16.17 | -0.06 | exit signal |
| 2026-10-21T22:00 | EMA 20/50 cross | sell | XRP-USD | 13.76 | 0.03 | exit signal |
| 2026-10-21T21:50 | Donchian 55/20 | sell | XRP-USD | 14.06 | 0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 23:20:05.000127+00:00 -> 2026-10-21 23:30:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
