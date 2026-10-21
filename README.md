# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T22:20:05.000166+00:00 · 31159 ticks

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
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.44 · VIX 16.63 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 39258 decisions in 3240 calls, $0.4847 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T22:20 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-21T22:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T22:20 | 0 / 5 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.03 | 6.03 | 0 | — | 8.54 | 4.02 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.62 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.81 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.21 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.50 | 1.50 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.23 | 0.23 | 4 | 50.0 | 9.05 | 1.92 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold BTC | benchmark | 99.89 | -0.11 | 0 | — | 15.44 | 2.23 | -8.68 | 1 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.62 | -0.38 | 0 | — | 2.33 | 1.07 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.40 | -0.60 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.56 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.97 | -4.04 | 21 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.50 | -2.50 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.79 | -5.83 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.06 | -2.94 | 0 | — | -4.00 | -1.53 | -7.04 | 1 |
| 18 | Copy: Insider buying | copy | 96.69 | -3.31 | 25 | 40.0 | -11.33 | -1.94 | -20.62 | 72 |
| 19 | Donchian 55/20 · 1h | breakout | 95.97 | -4.03 | 41 | 17.1 | -14.52 | -2.97 | -16.00 | 103 |
| 20 | Agent (rotation) | meta | 95.78 | -4.22 | 117 | 30.8 | -8.38 | -4.92 | -8.45 | 235 |
| 21 | ADX DI cross · 1h | trend | 95.61 | -4.39 | 91 | 19.8 | -11.48 | -2.12 | -16.14 | 262 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.18 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 94.93 | -5.07 | 6 | 16.7 | -9.31 | -1.38 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.86 | -5.14 | 92 | 23.9 | -20.41 | -6.41 | -20.58 | 129 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.05 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.11 | -17.26 | 568 |
| 27 | Parabolic SAR · 1h | trend | 93.23 | -6.77 | 108 | 23.1 | -16.26 | -3.60 | -19.79 | 272 |
| 28 | Squeeze breakout · 1h | breakout | 92.96 | -7.04 | 47 | 23.4 | -1.99 | -0.40 | -11.48 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 92.92 | -7.08 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.20 | -7.80 | 89 | 30.3 | -9.36 | -1.67 | -15.29 | 263 |
| 31 | Daily: Bullish score | daily | 92.19 | -7.81 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.95 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -16.87 | -7.06 | -17.38 | 264 |
| 34 | Volume breakout · 1h | breakout | 90.61 | -9.39 | 92 | 23.9 | -12.81 | -2.30 | -14.13 | 113 |
| 35 | Supertrend · 1h | trend | 90.14 | -9.86 | 88 | 12.5 | -20.81 | -4.17 | -26.66 | 218 |
| 36 | Connors RSI(2) · 1h | reversion | 89.85 | -10.15 | 159 | 42.1 | -22.01 | -6.61 | -23.74 | 194 |
| 37 | RSI momentum · 1h | momentum | 89.69 | -10.31 | 84 | 16.7 | -20.93 | -4.18 | -22.44 | 223 |
| 38 | Stochastic reversion · 1h | reversion | 89.55 | -10.45 | 169 | 47.3 | -13.60 | -2.23 | -22.24 | 363 |
| 39 | EMA 20/50 cross · 1h | trend | 88.87 | -11.13 | 62 | 12.9 | -20.91 | -3.62 | -23.61 | 140 |
| 40 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.22 | -19.07 | 704 |
| 41 | Keltner breakout · 1h | breakout | 87.93 | -12.07 | 63 | 23.8 | -17.97 | -3.36 | -25.20 | 204 |
| 42 | MACD cross · 1h | trend | 87.53 | -12.47 | 199 | 21.1 | -23.71 | -4.51 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -17.35 | -4.53 | -17.35 | 130 |
| 44 | Ichimoku · 1h | trend | 86.82 | -13.18 | 60 | 13.3 | -17.91 | -3.38 | -20.25 | 118 |
| 45 | Z-score reversion · 1h | reversion | 86.79 | -13.21 | 102 | 34.3 | -11.48 | -1.79 | -21.32 | 196 |
| 46 | Donchian 20/10 · 1h | breakout | 85.97 | -14.03 | 83 | 19.3 | -19.90 | -3.70 | -29.03 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.71 | -14.29 | 92 | 15.2 | -25.96 | -4.79 | -27.29 | 223 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.57 | -2.03 | -21.11 | 140 |
| 49 | Agent (ML meta-label) | meta | 84.63 | -15.37 | 735 | 20.1 | -11.60 | -2.13 | -16.14 | 367 |
| 50 | MACD zero-line · 1h | trend | 84.52 | -15.48 | 92 | 15.2 | -23.36 | -4.58 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 83.98 | -16.02 | 188 | 17.6 | -30.75 | -5.80 | -32.22 | 310 |
| 52 | ROC + volume · 1h | momentum | 82.94 | -17.06 | 213 | 23.5 | -25.74 | -4.59 | -32.91 | 395 |
| 53 | Williams %R · 1h | reversion | 82.60 | -17.40 | 199 | 44.7 | -31.50 | -4.92 | -36.62 | 517 |
| 54 | Bollinger reversion · 1h | reversion | 82.59 | -17.41 | 163 | 36.2 | -29.10 | -5.66 | -32.84 | 348 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.58 | -18.30 | -46.47 | 605 |
| 56 | CCI reversion · 1h | reversion | 82.12 | -17.88 | 188 | 43.6 | -20.26 | -2.65 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.41 | -18.59 | 251 | 23.9 | -42.85 | -9.25 | -46.38 | 678 |
| 58 | EMA 9/21 cross · 1h | trend | 80.92 | -19.08 | 143 | 10.5 | -26.88 | -5.25 | -29.94 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 80.88 | -19.12 | 85 | 24.7 | -16.91 | -2.91 | -24.99 | 172 |
| 60 | VWAP momentum · 1h | momentum | 79.10 | -20.90 | 478 | 21.3 | -46.56 | -8.93 | -52.84 | 1254 |
| 61 | Candlestick reversal · 1h | reversion | 79.02 | -20.98 | 231 | 30.3 | -38.28 | -7.06 | -41.79 | 535 |
| 62 | Max aggression: 1-day momentum | meta | 77.14 | -22.86 | 17 | 29.4 | -34.21 | -2.15 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.90 | -22.54 | -78.99 | 1722 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.59 | -20.28 | -64.95 | 870 |
| 65 | RSI(14) reversion | reversion | 57.33 | -42.67 | 761 | 27.2 | -74.28 | -16.56 | -74.90 | 1608 |
| 66 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.11 | -19.60 | -74.04 | 1283 |
| 67 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.07 | -23.23 | -67.93 | 1208 |
| 68 | EMA 20/50 cross | trend | 55.32 | -44.68 | 574 | 20.6 | -78.91 | -19.64 | -80.87 | 1439 |
| 69 | VWAP reversion | reversion | 54.37 | -45.63 | 765 | 26.0 | -70.79 | -14.23 | -72.15 | 1462 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.77 | -31.71 | -98.81 | 5289 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.10 | -35.38 | -94.29 | 2604 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.88 | -23.74 | -88.68 | 1895 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.22 | -28.56 | -91.74 | 2366 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.51 | -26.68 | -91.51 | 2280 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -35.61 | -97.81 | 3506 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -39.23 | -97.01 | 3609 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.55 | -28.32 | -94.71 | 2576 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.01 | -28.27 | -83.51 | 1736 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -37.39 | -99.39 | 5716 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.06 | -29.48 | -92.67 | 2626 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -32.34 | -95.92 | 3483 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -43.72 | -99.77 | 6165 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -30.99 | -91.92 | 2338 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -40.98 | -97.82 | 3639 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.93 | -98.50 | 4700 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.25 | -36.42 | -94.46 | 2808 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.52 | -28.86 | -84.44 | 1806 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.64 | -99.54 | 6179 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.96 | -23.00 | -87.01 | 2145 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.88 | -26.96 | -88.05 | 2144 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.97 | -33.82 | -95.98 | 3761 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.45 | -34.64 | -89.52 | 2099 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.83 | -34.61 | -95.85 | 4080 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.33 | -99.91 | 8300 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-21T21:35 | RSI(14) reversion | sell | ETH-USD | 14.30 | -0.04 | exit signal |
| 2026-10-21T21:35 | Squeeze breakout | buy | ETH-USD | 14.07 | — | entry signal |
| 2026-10-21T20:55 | EMA 20/50 cross | sell | SOL-USD | 13.78 | -0.11 | exit signal |
| 2026-10-21T20:40 | EMA 20/50 cross | buy | SOL-USD | 13.89 | — | entry signal |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | buy | XRP-USD | 11.75 | — | rebalance up |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | sell | SOL-USD | 4.52 | 0.06 | exit signal |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | sell | ETH-USD | 4.51 | 0.03 | exit signal |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 3.37 | -0.04 | exit signal |
| 2026-10-21T20:00 | Heikin-Ashi · 1h | sell | BTC-USD | 3.27 | 0.03 | exit signal |
| 2026-10-21T20:00 | Three white soldiers | sell | BTC-USD | 20.50 | -0.15 | exit signal |
| 2026-10-21T19:55 | Day trade: Stocks in Play ORB | sell | PLTR | 25.41 | 0.74 | target is flat |
| 2026-10-21T19:55 | Day trade: Stocks in Play ORB | sell | AMD | 24.75 | -0.02 | target is flat |
| 2026-10-21T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 98.30 | -0.10 | target is flat |
| 2026-10-21T19:55 | Agent (ML meta-label) | sell | ETHU | 9.40 | -0.02 | selected signal exited |
| 2026-10-21T19:55 | Agent (aggressive) | sell | TSLA | 43.60 | -0.19 | selected signal exited |
| 2026-10-21T19:55 | Agent | sell | TSLA | 18.05 | -0.08 | selected signal exited |
| 2026-10-21T19:55 | Agent | sell | ETHU | 18.21 | 0.10 | selected signal exited |
| 2026-10-21T19:55 | MFI reversion · 1h | sell | GOOGL | 21.36 | 0.07 | target is flat |
| 2026-10-21T19:55 | VWAP reversion | sell | TNA | 13.66 | 0.12 | end-of-day flatten |
| 2026-10-21T19:55 | VWAP reversion | sell | LABU | 13.58 | 0.04 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | buy | ETH-USD | 6.18 | — | rebalance up |
| 2026-10-21T19:55 | RSI(14) reversion | sell | TNA | 9.56 | -0.01 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | sell | META | 9.53 | -0.04 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | sell | IWM | 8.19 | 0.02 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | sell | ETHU | 9.57 | 0.00 | end-of-day flatten |
| 2026-10-21T19:55 | RSI(14) reversion | sell | AMZN | 8.20 | 0.04 | end-of-day flatten |
| 2026-10-21T19:55 | Squeeze breakout | sell | PLTR | 14.08 | 0.02 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | UPRO | 8.54 | 0.04 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | TQQQ | 8.55 | 0.09 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | TECL | 8.59 | 0.07 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 22:20:05.000166+00:00 -> 2026-10-21 22:30:05.000166+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
