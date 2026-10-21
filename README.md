# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T20:20:05.000176+00:00 · 31064 ticks

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

Today: 37833 decisions in 2955 calls, $0.4648 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T20:20 | 1 / 2 / 2 | XRP-USD 15% |  |
| Breezy | 2026-10-21T20:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T20:20 | 2 / 2 / 1 | XRP-USD 61% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.34 | 6.34 | 0 | — | 8.66 | 4.03 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.69 | 1.69 | 10 | 50.0 | -7.20 | -0.33 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.29 | 0.29 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold BTC | benchmark | 99.90 | -0.10 | 0 | — | 15.85 | 2.26 | -8.68 | 1 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.68 | -0.32 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.46 | -0.54 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.56 | -2.44 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.23 | -2.77 | 0 | — | -3.90 | -1.48 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 18 | Copy: Insider buying | copy | 96.64 | -3.36 | 25 | 40.0 | -11.42 | -1.94 | -20.62 | 72 |
| 19 | Donchian 55/20 · 1h | breakout | 96.32 | -3.68 | 41 | 17.1 | -14.21 | -2.88 | -16.00 | 103 |
| 20 | Agent (rotation) | meta | 95.80 | -4.20 | 117 | 30.8 | -6.89 | -3.68 | -8.45 | 255 |
| 21 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 91 | 19.8 | -11.98 | -2.19 | -16.14 | 262 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 95.00 | -5.00 | 6 | 16.7 | -9.35 | -1.37 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.88 | -5.12 | 92 | 23.9 | -20.41 | -6.36 | -20.58 | 129 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.56 | 2.04 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Parabolic SAR · 1h | trend | 93.58 | -6.42 | 108 | 23.1 | -15.67 | -3.42 | -19.79 | 272 |
| 28 | Squeeze breakout · 1h | breakout | 93.30 | -6.70 | 46 | 21.7 | -1.67 | -0.31 | -11.48 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 93.08 | -6.92 | 0 | — | 0.19 | 0.19 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.46 | -7.54 | 88 | 30.7 | -9.21 | -1.62 | -15.29 | 263 |
| 31 | Daily: Bullish score | daily | 92.23 | -7.77 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.83 | -9.17 | 92 | 23.9 | -14.46 | -2.54 | -14.65 | 114 |
| 34 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -15.83 | -7.03 | -20.88 | 256 |
| 35 | Supertrend · 1h | trend | 90.34 | -9.66 | 88 | 12.5 | -20.72 | -4.11 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.92 | -10.08 | 84 | 16.7 | -19.53 | -3.91 | -21.18 | 221 |
| 37 | Connors RSI(2) · 1h | reversion | 89.85 | -10.15 | 159 | 42.1 | -22.01 | -6.55 | -23.74 | 194 |
| 38 | Stochastic reversion · 1h | reversion | 89.58 | -10.42 | 169 | 47.3 | -13.60 | -2.22 | -22.24 | 363 |
| 39 | EMA 20/50 cross · 1h | trend | 88.94 | -11.05 | 62 | 12.9 | -20.88 | -3.59 | -23.61 | 140 |
| 40 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 41 | Keltner breakout · 1h | breakout | 88.22 | -11.78 | 62 | 24.2 | -18.36 | -3.44 | -25.20 | 204 |
| 42 | MACD cross · 1h | trend | 87.67 | -12.33 | 199 | 21.1 | -23.62 | -4.45 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -15.40 | -4.38 | -15.93 | 126 |
| 44 | Ichimoku · 1h | trend | 86.89 | -13.11 | 60 | 13.3 | -17.90 | -3.36 | -20.25 | 118 |
| 45 | Z-score reversion · 1h | reversion | 86.81 | -13.19 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 46 | Donchian 20/10 · 1h | breakout | 86.20 | -13.80 | 83 | 19.3 | -19.79 | -3.64 | -29.03 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.77 | -14.23 | 92 | 15.2 | -27.36 | -5.04 | -27.97 | 224 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -14.49 | -2.20 | -21.11 | 139 |
| 49 | Agent (ML meta-label) | meta | 84.68 | -15.32 | 735 | 20.1 | -13.96 | -2.46 | -17.84 | 368 |
| 50 | MACD zero-line · 1h | trend | 84.58 | -15.42 | 92 | 15.2 | -23.36 | -4.54 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 84.08 | -15.92 | 188 | 17.6 | -30.22 | -5.67 | -31.82 | 308 |
| 52 | ROC + volume · 1h | momentum | 83.08 | -16.92 | 213 | 23.5 | -26.43 | -4.74 | -33.27 | 391 |
| 53 | Williams %R · 1h | reversion | 82.62 | -17.38 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 54 | Bollinger reversion · 1h | reversion | 82.61 | -17.39 | 163 | 36.2 | -29.10 | -5.61 | -32.84 | 348 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.58 | -18.05 | -46.47 | 605 |
| 56 | CCI reversion · 1h | reversion | 82.15 | -17.85 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.60 | -18.40 | 250 | 23.6 | -43.45 | -9.30 | -46.38 | 679 |
| 58 | EMA 9/21 cross · 1h | trend | 81.00 | -19.00 | 143 | 10.5 | -26.86 | -5.20 | -29.94 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 80.91 | -19.09 | 85 | 24.7 | -16.91 | -2.89 | -24.99 | 172 |
| 60 | VWAP momentum · 1h | momentum | 79.24 | -20.76 | 478 | 21.3 | -46.42 | -8.79 | -52.82 | 1247 |
| 61 | Candlestick reversal · 1h | reversion | 79.06 | -20.94 | 231 | 30.3 | -38.46 | -7.07 | -41.73 | 536 |
| 62 | Max aggression: 1-day momentum | meta | 77.23 | -22.77 | 17 | 29.4 | -34.17 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.64 | -21.77 | -78.91 | 1711 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -65.11 | -20.27 | -65.35 | 875 |
| 65 | RSI(14) reversion | reversion | 57.32 | -42.68 | 760 | 27.2 | -74.28 | -16.36 | -74.90 | 1609 |
| 66 | Donchian 55/20 | breakout | 56.59 | -43.41 | 534 | 19.7 | -72.06 | -19.30 | -74.04 | 1286 |
| 67 | Squeeze breakout | breakout | 56.28 | -43.72 | 522 | 14.2 | -66.98 | -22.73 | -67.92 | 1212 |
| 68 | EMA 20/50 cross | trend | 55.58 | -44.42 | 572 | 20.5 | -78.82 | -19.25 | -80.87 | 1438 |
| 69 | VWAP reversion | reversion | 54.37 | -45.63 | 765 | 26.0 | -70.69 | -14.01 | -72.15 | 1465 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.77 | -31.12 | -98.80 | 5280 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.99 | -33.77 | -94.28 | 2602 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.73 | -22.85 | -88.67 | 1896 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -27.47 | -91.74 | 2365 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.43 | -26.11 | -91.49 | 2281 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -34.13 | -97.79 | 3506 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.94 | -37.75 | -96.99 | 3578 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.56 | -27.82 | -94.73 | 2571 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.99 | -27.67 | -83.49 | 1736 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.10 | -99.38 | 5714 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.99 | -28.38 | -92.66 | 2625 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.89 | -31.52 | -95.89 | 3481 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.52 | -99.76 | 6160 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.69 | -29.78 | -91.89 | 2338 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -39.45 | -97.81 | 3644 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.58 | -98.50 | 4704 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.23 | -35.08 | -94.46 | 2809 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.49 | -28.12 | -84.44 | 1807 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.34 | -99.54 | 6182 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.89 | -22.52 | -87.01 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.89 | -26.42 | -88.05 | 2129 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.97 | -32.93 | -95.97 | 3764 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -33.37 | -89.47 | 2097 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -33.53 | -95.82 | 4079 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.57 | -99.91 | 8301 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-21T19:55 | Opening range 30m | sell | SPY | 8.53 | 0.01 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | QQQ | 8.52 | 0.03 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | PLTR | 8.60 | 0.16 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | MSTR | 8.51 | 0.30 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | ETHU | 8.39 | 0.09 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | COIN | 8.47 | 0.01 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | BITX | 8.50 | 0.09 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 30m | sell | AAPL | 8.50 | -0.02 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 15m | sell | UPRO | 5.21 | 0.01 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 15m | sell | TSLA | 3.00 | -0.03 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 15m | sell | TQQQ | 7.64 | 0.09 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 15m | sell | TECL | 5.93 | 0.07 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 15m | sell | SPY | 6.33 | 0.00 | end-of-day flatten |
| 2026-10-21T19:55 | Opening range 15m | sell | QQQ | 6.33 | 0.02 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 20:20:05.000176+00:00 -> 2026-10-21 20:30:05.000176+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
