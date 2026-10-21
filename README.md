# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T23:50:05.000150+00:00 · 31226 ticks

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

Today: 40263 decisions in 3441 calls, $0.4988 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T23:50 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-21T23:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T23:50 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.81 | +2.89% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.08 | 6.08 | 0 | — | 8.54 | 4.02 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.62 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.81 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.21 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.54 | 1.54 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.27 | 0.27 | 4 | 50.0 | 9.05 | 1.92 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.66 | -0.34 | 0 | — | 2.33 | 1.07 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.44 | -0.56 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Hold BTC | benchmark | 99.42 | -0.58 | 0 | — | 13.85 | 2.09 | -8.68 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.56 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.97 | -4.04 | 21 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.54 | -2.46 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.10 | -2.90 | 0 | — | -4.00 | -1.53 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.79 | -5.83 | 1 |
| 18 | Copy: Insider buying | copy | 96.73 | -3.27 | 25 | 40.0 | -11.33 | -1.94 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.79 | -4.21 | 117 | 30.8 | -8.38 | -4.92 | -8.45 | 235 |
| 20 | ADX DI cross · 1h | trend | 95.60 | -4.40 | 91 | 19.8 | -11.02 | -2.02 | -16.14 | 260 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.18 | -6.31 | 31 |
| 22 | Donchian 55/20 · 1h | breakout | 95.40 | -4.60 | 43 | 16.3 | -15.06 | -3.09 | -16.13 | 103 |
| 23 | Daily: Momentum burst | daily | 94.97 | -5.04 | 6 | 16.7 | -9.31 | -1.38 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.87 | -5.13 | 92 | 23.9 | -20.41 | -6.41 | -20.58 | 129 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.05 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.11 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.96 | -7.04 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.90 | -7.10 | 111 | 25.2 | -16.17 | -3.59 | -19.79 | 272 |
| 29 | Squeeze breakout · 1h | breakout | 92.64 | -7.36 | 49 | 22.4 | -2.39 | -0.51 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.22 | -7.78 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.09 | -7.91 | 92 | 29.3 | -9.49 | -1.70 | -15.29 | 263 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.95 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -19.50 | -6.09 | -19.99 | 267 |
| 34 | Volume breakout · 1h | breakout | 90.44 | -9.56 | 94 | 24.5 | -14.77 | -2.62 | -14.77 | 114 |
| 35 | Supertrend · 1h | trend | 89.99 | -10.01 | 88 | 12.5 | -20.93 | -4.21 | -26.66 | 218 |
| 36 | Stochastic reversion · 1h | reversion | 89.57 | -10.43 | 169 | 47.3 | -13.60 | -2.23 | -22.24 | 363 |
| 37 | RSI momentum · 1h | momentum | 89.49 | -10.51 | 84 | 16.7 | -20.25 | -4.07 | -21.62 | 222 |
| 38 | Connors RSI(2) · 1h | reversion | 89.44 | -10.56 | 159 | 42.1 | -22.37 | -6.75 | -23.74 | 196 |
| 39 | EMA 20/50 cross · 1h | trend | 88.80 | -11.20 | 62 | 12.9 | -21.00 | -3.65 | -23.57 | 140 |
| 40 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.22 | -19.07 | 704 |
| 41 | Keltner breakout · 1h | breakout | 87.77 | -12.23 | 66 | 22.7 | -18.19 | -3.41 | -25.20 | 204 |
| 42 | MACD cross · 1h | trend | 87.49 | -12.51 | 201 | 21.9 | -23.80 | -4.54 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -20.94 | -4.39 | -20.95 | 124 |
| 44 | Z-score reversion · 1h | reversion | 86.81 | -13.19 | 102 | 34.3 | -11.48 | -1.79 | -21.32 | 196 |
| 45 | Ichimoku · 1h | trend | 86.77 | -13.23 | 60 | 13.3 | -18.00 | -3.40 | -20.25 | 118 |
| 46 | Donchian 20/10 · 1h | breakout | 85.80 | -14.20 | 83 | 19.3 | -19.98 | -3.73 | -28.97 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.60 | -14.40 | 92 | 15.2 | -25.82 | -4.75 | -27.29 | 221 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.57 | -2.03 | -21.11 | 140 |
| 49 | Agent (ML meta-label) | meta | 84.66 | -15.34 | 735 | 20.1 | -10.93 | -2.10 | -15.52 | 384 |
| 50 | MACD zero-line · 1h | trend | 84.56 | -15.44 | 92 | 15.2 | -23.36 | -4.58 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 83.84 | -16.16 | 188 | 17.6 | -31.74 | -6.01 | -32.25 | 310 |
| 52 | ROC + volume · 1h | momentum | 82.84 | -17.16 | 217 | 24.0 | -25.92 | -4.65 | -32.91 | 395 |
| 53 | Williams %R · 1h | reversion | 82.61 | -17.39 | 199 | 44.7 | -31.50 | -4.92 | -36.62 | 517 |
| 54 | Bollinger reversion · 1h | reversion | 82.60 | -17.40 | 163 | 36.2 | -29.10 | -5.66 | -32.84 | 348 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.58 | -18.30 | -46.47 | 605 |
| 56 | CCI reversion · 1h | reversion | 82.14 | -17.86 | 188 | 43.6 | -20.26 | -2.65 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.42 | -18.58 | 251 | 23.9 | -42.85 | -9.25 | -46.38 | 678 |
| 58 | EMA 9/21 cross · 1h | trend | 80.90 | -19.09 | 143 | 10.5 | -26.93 | -5.27 | -29.94 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 80.90 | -19.10 | 85 | 24.7 | -16.91 | -2.91 | -24.99 | 172 |
| 60 | Candlestick reversal · 1h | reversion | 79.05 | -20.95 | 231 | 30.3 | -37.97 | -6.98 | -41.90 | 536 |
| 61 | VWAP momentum · 1h | momentum | 79.03 | -20.97 | 480 | 21.7 | -46.64 | -8.97 | -52.84 | 1254 |
| 62 | Max aggression: 1-day momentum | meta | 77.17 | -22.83 | 17 | 29.4 | -34.21 | -2.15 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -78.14 | -22.98 | -78.99 | 1721 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.57 | -20.25 | -64.95 | 868 |
| 65 | RSI(14) reversion | reversion | 56.50 | -43.50 | 765 | 27.1 | -74.65 | -16.82 | -74.90 | 1615 |
| 66 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.06 | -19.51 | -74.04 | 1282 |
| 67 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.06 | -23.22 | -67.93 | 1207 |
| 68 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.94 | -19.67 | -80.87 | 1439 |
| 69 | VWAP reversion | reversion | 54.37 | -45.63 | 765 | 26.0 | -70.79 | -14.23 | -72.15 | 1462 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.76 | -31.30 | -98.83 | 5280 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.05 | -35.01 | -94.26 | 2598 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.88 | -23.74 | -88.68 | 1895 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.21 | -28.48 | -91.74 | 2364 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.44 | -26.58 | -91.44 | 2277 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -35.61 | -97.82 | 3506 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -39.22 | -97.02 | 3606 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.57 | -28.26 | -94.73 | 2577 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.01 | -28.27 | -83.51 | 1736 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -37.59 | -99.40 | 5725 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.16 | -30.27 | -92.67 | 2626 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.91 | -32.10 | -95.91 | 3480 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -43.62 | -99.77 | 6160 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -30.99 | -91.92 | 2338 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -40.98 | -97.82 | 3636 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -38.09 | -98.52 | 4704 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.33 | -37.19 | -94.46 | 2807 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.69 | -29.32 | -84.44 | 1804 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -40.65 | -99.55 | 6186 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.16 | -23.18 | -87.22 | 2152 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.98 | -27.10 | -88.05 | 2146 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -34.05 | -96.03 | 3767 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.48 | -34.66 | -89.52 | 2098 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.91 | -34.60 | -95.93 | 4089 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.34 | -99.91 | 8296 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T23:50 | ROC + volume · 1h | sell | SOL-USD | 2.46 | -0.03 | stop-loss |
| 2026-10-21T23:45 | Volume breakout · 1h | sell | BTC-USD | 5.13 | -0.01 | rebalance down |
| 2026-10-21T23:45 | RSI(14) reversion | buy | DOGE-USD | 14.16 | — | entry signal |
| 2026-10-21T23:45 | RSI(14) reversion | sell | SOL-USD | 14.11 | -0.14 | stop-loss |
| 2026-10-21T23:35 | RSI(14) reversion | buy | XRP-USD | 14.20 | — | entry signal |
| 2026-10-21T23:35 | RSI(14) reversion | buy | ETH-USD | 14.20 | — | entry signal |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | buy | XRP-USD | 9.40 | — | rebalance up |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | buy | SOL-USD | 5.52 | — | rebalance up |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | buy | BTC-USD | 5.36 | — | rebalance up |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | sell | ETH-USD | 13.53 | -0.27 | stop-loss |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | sell | DOGE-USD | 14.96 | -0.33 | stop-loss |
| 2026-10-21T23:30 | ROC + volume · 1h | sell | XRP-USD | 4.85 | 0.03 | stop-loss |
| 2026-10-21T23:30 | ROC + volume · 1h | sell | ETH-USD | 3.91 | -0.02 | stop-loss |
| 2026-10-21T23:30 | RSI(14) reversion | sell | XRP-USD | 14.10 | -0.15 | stop-loss |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 23:50:05.000150+00:00 -> 2026-10-22 00:00:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
