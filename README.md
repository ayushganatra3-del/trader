# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T01:50:05.000160+00:00 · 31316 ticks

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

Today: 1260 decisions in 252 calls, $0.0177 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T01:50 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-22T01:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T01:50 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.01 | 6.01 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.48 | 1.48 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.21 | 0.21 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.60 | -0.40 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.38 | -0.62 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Hold BTC | benchmark | 98.78 | -1.22 | 0 | — | 12.07 | 1.88 | -8.68 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.47 | -2.52 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.04 | -2.96 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 18 | Copy: Insider buying | copy | 96.67 | -3.33 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.77 | -4.23 | 117 | 30.8 | -8.72 | -5.12 | -8.77 | 235 |
| 20 | ADX DI cross · 1h | trend | 95.50 | -4.50 | 91 | 19.8 | -10.26 | -1.86 | -16.14 | 258 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 22 | Donchian 55/20 · 1h | breakout | 95.03 | -4.96 | 43 | 16.3 | -15.34 | -3.14 | -16.40 | 103 |
| 23 | Daily: Momentum burst | daily | 94.91 | -5.09 | 6 | 16.7 | -9.30 | -1.37 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.85 | -5.15 | 92 | 23.9 | -20.40 | -6.36 | -20.58 | 129 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.56 | 2.04 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.90 | -7.10 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.81 | -7.19 | 113 | 25.7 | -16.39 | -3.62 | -19.79 | 271 |
| 29 | Squeeze breakout · 1h | breakout | 92.49 | -7.51 | 50 | 24.0 | -3.00 | -0.66 | -11.48 | 101 |
| 30 | Daily: Bullish score | daily | 92.18 | -7.83 | 8 | 0.0 | -2.44 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.00 | -8.00 | 93 | 30.1 | -10.21 | -1.85 | -15.29 | 262 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -17.67 | -6.54 | -17.91 | 259 |
| 34 | Volume breakout · 1h | breakout | 90.36 | -9.64 | 95 | 24.2 | -15.06 | -2.63 | -15.06 | 109 |
| 35 | Supertrend · 1h | trend | 89.78 | -10.22 | 88 | 12.5 | -21.03 | -4.20 | -26.66 | 218 |
| 36 | Stochastic reversion · 1h | reversion | 89.54 | -10.46 | 169 | 47.3 | -13.60 | -2.22 | -22.24 | 363 |
| 37 | RSI momentum · 1h | momentum | 89.25 | -10.75 | 84 | 16.7 | -17.46 | -3.46 | -20.65 | 218 |
| 38 | Connors RSI(2) · 1h | reversion | 88.65 | -11.35 | 159 | 42.1 | -23.01 | -6.92 | -23.74 | 198 |
| 39 | EMA 20/50 cross · 1h | trend | 88.65 | -11.35 | 62 | 12.9 | -21.25 | -3.66 | -23.57 | 142 |
| 40 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 41 | Keltner breakout · 1h | breakout | 87.66 | -12.34 | 67 | 23.9 | -19.32 | -3.65 | -24.72 | 202 |
| 42 | MACD cross · 1h | trend | 87.42 | -12.58 | 202 | 22.3 | -23.77 | -4.50 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -18.26 | -4.51 | -18.26 | 123 |
| 44 | Z-score reversion · 1h | reversion | 86.78 | -13.22 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 45 | Ichimoku · 1h | trend | 86.61 | -13.38 | 60 | 13.3 | -18.08 | -3.40 | -20.25 | 118 |
| 46 | Donchian 20/10 · 1h | breakout | 85.54 | -14.46 | 83 | 19.3 | -21.50 | -4.02 | -29.36 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.41 | -14.59 | 92 | 15.2 | -26.08 | -4.77 | -27.44 | 221 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.57 | -2.02 | -21.11 | 141 |
| 49 | Agent (ML meta-label) | meta | 84.62 | -15.38 | 735 | 20.1 | -10.74 | -2.02 | -16.25 | 380 |
| 50 | MACD zero-line · 1h | trend | 84.50 | -15.50 | 92 | 15.2 | -23.35 | -4.54 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 83.71 | -16.29 | 189 | 18.0 | -30.44 | -5.69 | -31.52 | 306 |
| 52 | ROC + volume · 1h | momentum | 82.76 | -17.24 | 218 | 23.9 | -26.97 | -4.87 | -32.91 | 388 |
| 53 | Bollinger reversion · 1h | reversion | 82.59 | -17.41 | 163 | 36.2 | -29.10 | -5.61 | -32.84 | 348 |
| 54 | Williams %R · 1h | reversion | 82.59 | -17.41 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.64 | -18.08 | -46.47 | 606 |
| 56 | CCI reversion · 1h | reversion | 82.11 | -17.89 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.40 | -18.60 | 251 | 23.9 | -42.85 | -9.17 | -46.38 | 678 |
| 58 | RSI(14) reversion · 1h | reversion | 80.87 | -19.13 | 85 | 24.7 | -16.02 | -2.70 | -24.99 | 173 |
| 59 | EMA 9/21 cross · 1h | trend | 80.80 | -19.20 | 143 | 10.5 | -26.73 | -5.18 | -29.94 | 331 |
| 60 | Candlestick reversal · 1h | reversion | 79.00 | -21.00 | 231 | 30.3 | -38.66 | -7.12 | -41.83 | 538 |
| 61 | VWAP momentum · 1h | momentum | 78.97 | -21.03 | 483 | 22.2 | -46.58 | -8.86 | -52.83 | 1254 |
| 62 | Max aggression: 1-day momentum | meta | 77.12 | -22.88 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.85 | -21.99 | -78.97 | 1712 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.31 | -19.56 | -64.95 | 862 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.31 | -19.59 | -74.04 | 1283 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.25 | -23.16 | -67.93 | 1209 |
| 67 | RSI(14) reversion | reversion | 55.95 | -44.05 | 770 | 26.9 | -74.86 | -16.77 | -75.07 | 1621 |
| 68 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.99 | -19.49 | -80.87 | 1439 |
| 69 | VWAP reversion | reversion | 54.37 | -45.63 | 765 | 26.0 | -70.79 | -14.07 | -72.15 | 1466 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -32.22 | -98.86 | 5302 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.04 | -33.90 | -94.26 | 2595 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.04 | -23.78 | -88.71 | 1894 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.27 | -28.13 | -91.74 | 2364 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.18 | -25.43 | -91.26 | 2265 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -34.93 | -97.83 | 3509 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.94 | -37.68 | -97.03 | 3612 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.57 | -28.30 | -94.68 | 2559 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.20 | -28.14 | -83.42 | 1733 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -36.71 | -99.41 | 5739 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.11 | -29.10 | -92.69 | 2623 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.91 | -31.26 | -95.91 | 3477 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -42.01 | -99.77 | 6157 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -30.06 | -91.92 | 2341 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -39.39 | -97.82 | 3631 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -37.22 | -98.54 | 4706 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.27 | -35.39 | -94.47 | 2803 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.48 | -28.08 | -84.44 | 1798 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.46 | -99.56 | 6194 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.29 | -23.01 | -87.35 | 2155 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.00 | -26.69 | -88.06 | 2141 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -33.07 | -96.03 | 3766 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.46 | -33.69 | -89.56 | 2101 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.93 | -33.69 | -95.95 | 4088 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.03 | -99.91 | 8304 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T01:45 | ROC + volume · 1h | sell | BTC-USD | 3.92 | -0.03 | stop-loss |
| 2026-10-22T01:40 | Squeeze breakout · 1h | sell | BTC-USD | 18.51 | 0.08 | stop-loss |
| 2026-10-22T01:40 | Keltner breakout · 1h | sell | BTC-USD | 9.73 | 0.04 | stop-loss |
| 2026-10-22T01:40 | Bollinger breakout · 1h | sell | BTC-USD | 7.63 | 0.08 | stop-loss |
| 2026-10-22T01:40 | RSI(14) reversion | sell | XRP-USD | 13.96 | -0.19 | stop-loss |
| 2026-10-22T01:40 | RSI(14) reversion | sell | ETH-USD | 14.01 | -0.18 | stop-loss |
| 2026-10-22T01:40 | RSI(14) reversion | sell | DOGE-USD | 13.97 | -0.18 | stop-loss |
| 2026-10-22T01:40 | RSI(14) reversion | sell | BTC-USD | 14.01 | -0.16 | stop-loss |
| 2026-10-22T00:50 | RSI(14) reversion | buy | XRP-USD | 2.81 | — | rebalance up |
| 2026-10-22T00:50 | RSI(14) reversion | buy | ETH-USD | 2.83 | — | rebalance up |
| 2026-10-22T00:50 | RSI(14) reversion | buy | DOGE-USD | 2.84 | — | rebalance up |
| 2026-10-22T00:50 | RSI(14) reversion | buy | BTC-USD | 5.64 | — | rebalance up |
| 2026-10-22T00:50 | RSI(14) reversion | sell | SOL-USD | 11.29 | -0.02 | exit signal |
| 2026-10-22T00:40 | RSI(14) reversion | sell | SOL-USD | 2.82 | -0.01 | rebalance down |
| 2026-10-22T00:25 | RSI(14) reversion | buy | BTC-USD | 2.83 | — | rebalance up |
| 2026-10-22T00:25 | RSI(14) reversion | sell | DOGE-USD | 2.83 | -0.01 | rebalance down |
| 2026-10-22T00:10 | RSI(14) reversion | buy | BTC-USD | 2.83 | — | rebalance up |
| 2026-10-22T00:10 | RSI(14) reversion | sell | ETH-USD | 2.83 | -0.01 | rebalance down |
| 2026-10-22T00:05 | RSI(14) reversion | buy | BTC-USD | 2.87 | — | entry signal |
| 2026-10-22T00:05 | RSI(14) reversion | sell | XRP-USD | 2.84 | -0.01 | rebalance down |
| 2026-10-22T00:00 | Connors RSI(2) · 1h | buy | SOL-USD | 22.38 | — | entry signal |
| 2026-10-22T00:00 | Connors RSI(2) · 1h | buy | ETH-USD | 22.38 | — | entry signal |
| 2026-10-22T00:00 | Volume breakout · 1h | sell | BTC-USD | 12.86 | -0.05 | exit signal |
| 2026-10-22T00:00 | OBV trend · 1h | sell | ETH-USD | 9.22 | 0.07 | exit signal |
| 2026-10-22T00:00 | VWAP momentum · 1h | sell | XRP-USD | 3.56 | 0.02 | exit signal |
| 2026-10-22T00:00 | VWAP momentum · 1h | sell | ETH-USD | 3.55 | 0.00 | exit signal |
| 2026-10-22T00:00 | VWAP momentum · 1h | sell | BTC-USD | 3.57 | 0.02 | exit signal |
| 2026-10-22T00:00 | Parabolic SAR · 1h | sell | SOL-USD | 13.17 | -0.14 | exit signal |
| 2026-10-22T00:00 | Parabolic SAR · 1h | sell | BTC-USD | 13.23 | 0.22 | exit signal |
| 2026-10-22T00:00 | MACD cross · 1h | sell | BTC-USD | 5.41 | 0.03 | exit signal |
| 2026-10-22T00:00 | RSI(14) reversion | buy | SOL-USD | 14.14 | — | entry signal |
| 2026-10-21T23:50 | ROC + volume · 1h | sell | SOL-USD | 2.46 | -0.03 | stop-loss |
| 2026-10-21T23:45 | Volume breakout · 1h | sell | BTC-USD | 5.13 | -0.01 | rebalance down |
| 2026-10-21T23:45 | RSI(14) reversion | buy | DOGE-USD | 14.16 | — | entry signal |
| 2026-10-21T23:45 | RSI(14) reversion | sell | SOL-USD | 14.11 | -0.14 | stop-loss |
| 2026-10-21T23:35 | RSI(14) reversion | buy | XRP-USD | 14.20 | — | entry signal |
| 2026-10-21T23:35 | RSI(14) reversion | buy | ETH-USD | 14.20 | — | entry signal |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | buy | XRP-USD | 9.40 | — | rebalance up |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | buy | SOL-USD | 5.52 | — | rebalance up |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | buy | BTC-USD | 5.36 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 01:50:05.000160+00:00 -> 2026-10-22 02:00:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
