# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T21:22:05.000174+00:00 · 31108 ticks

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

Today: 38493 decisions in 3087 calls, $0.4740 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T21:22 | 2 / 3 / 0 | ETH-USD 16% |  |
| Breezy | 2026-10-21T21:22 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T21:22 | 2 / 3 / 0 | ETH-USD 65% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.02 | 6.02 | 0 | — | 8.54 | 4.02 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.62 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.81 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.21 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.49 | 1.49 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.22 | 0.22 | 4 | 50.0 | 9.05 | 1.92 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold BTC | benchmark | 99.96 | -0.04 | 0 | — | 15.92 | 2.28 | -8.68 | 1 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.61 | -0.39 | 0 | — | 2.33 | 1.07 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.39 | -0.61 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.56 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.97 | -4.04 | 21 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.48 | -2.52 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.79 | -5.83 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.04 | -2.96 | 0 | — | -4.00 | -1.53 | -7.04 | 1 |
| 18 | Copy: Insider buying | copy | 96.67 | -3.33 | 25 | 40.0 | -11.33 | -1.94 | -20.62 | 72 |
| 19 | Donchian 55/20 · 1h | breakout | 96.21 | -3.79 | 41 | 17.1 | -14.27 | -2.91 | -16.00 | 103 |
| 20 | Agent (rotation) | meta | 95.77 | -4.23 | 117 | 30.8 | -8.38 | -4.92 | -8.45 | 235 |
| 21 | ADX DI cross · 1h | trend | 95.60 | -4.40 | 91 | 19.8 | -11.98 | -2.21 | -16.14 | 262 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.18 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 94.91 | -5.09 | 6 | 16.7 | -9.31 | -1.38 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.85 | -5.15 | 92 | 23.9 | -20.41 | -6.41 | -20.58 | 129 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.56 | 2.05 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.11 | -17.26 | 568 |
| 27 | Parabolic SAR · 1h | trend | 93.45 | -6.55 | 108 | 23.1 | -15.71 | -3.46 | -19.79 | 272 |
| 28 | Squeeze breakout · 1h | breakout | 93.26 | -6.74 | 46 | 21.7 | -1.64 | -0.31 | -11.48 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 92.91 | -7.09 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.36 | -7.64 | 88 | 30.7 | -9.24 | -1.64 | -15.29 | 263 |
| 31 | Daily: Bullish score | daily | 92.18 | -7.83 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.95 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.71 | -9.29 | 92 | 23.9 | -14.51 | -2.57 | -14.65 | 114 |
| 34 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -18.66 | -6.52 | -21.35 | 258 |
| 35 | Supertrend · 1h | trend | 90.23 | -9.77 | 88 | 12.5 | -20.74 | -4.15 | -26.66 | 218 |
| 36 | Connors RSI(2) · 1h | reversion | 89.85 | -10.15 | 159 | 42.1 | -22.01 | -6.61 | -23.74 | 194 |
| 37 | RSI momentum · 1h | momentum | 89.80 | -10.20 | 84 | 16.7 | -18.77 | -3.78 | -20.65 | 220 |
| 38 | Stochastic reversion · 1h | reversion | 89.55 | -10.45 | 169 | 47.3 | -13.60 | -2.23 | -22.24 | 363 |
| 39 | EMA 20/50 cross · 1h | trend | 88.89 | -11.11 | 62 | 12.9 | -20.85 | -3.61 | -23.57 | 140 |
| 40 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.22 | -19.07 | 704 |
| 41 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 62 | 24.2 | -17.79 | -3.31 | -25.20 | 204 |
| 42 | MACD cross · 1h | trend | 87.57 | -12.43 | 199 | 21.1 | -23.64 | -4.49 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -21.14 | -4.35 | -26.08 | 125 |
| 44 | Ichimoku · 1h | trend | 86.83 | -13.17 | 60 | 13.3 | -17.90 | -3.38 | -20.25 | 118 |
| 45 | Z-score reversion · 1h | reversion | 86.78 | -13.22 | 102 | 34.3 | -11.48 | -1.79 | -21.32 | 196 |
| 46 | Donchian 20/10 · 1h | breakout | 86.09 | -13.91 | 83 | 19.3 | -19.81 | -3.68 | -29.03 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.74 | -14.26 | 92 | 15.2 | -26.85 | -4.98 | -27.61 | 224 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -14.49 | -2.21 | -21.11 | 139 |
| 49 | Agent (ML meta-label) | meta | 84.62 | -15.38 | 735 | 20.1 | -10.69 | -2.02 | -14.87 | 373 |
| 50 | MACD zero-line · 1h | trend | 84.51 | -15.49 | 92 | 15.2 | -23.36 | -4.58 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 84.01 | -15.99 | 188 | 17.6 | -30.30 | -5.73 | -31.84 | 308 |
| 52 | ROC + volume · 1h | momentum | 82.99 | -17.01 | 213 | 23.5 | -26.45 | -4.78 | -33.27 | 391 |
| 53 | Williams %R · 1h | reversion | 82.59 | -17.41 | 199 | 44.7 | -31.50 | -4.92 | -36.62 | 517 |
| 54 | Bollinger reversion · 1h | reversion | 82.59 | -17.41 | 163 | 36.2 | -29.10 | -5.66 | -32.84 | 348 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.58 | -18.30 | -46.47 | 605 |
| 56 | CCI reversion · 1h | reversion | 82.12 | -17.88 | 188 | 43.6 | -20.26 | -2.65 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.46 | -18.54 | 250 | 23.6 | -42.80 | -9.23 | -46.38 | 678 |
| 58 | EMA 9/21 cross · 1h | trend | 80.94 | -19.06 | 143 | 10.5 | -26.86 | -5.24 | -29.94 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 80.87 | -19.12 | 85 | 24.7 | -16.91 | -2.91 | -24.99 | 172 |
| 60 | VWAP momentum · 1h | momentum | 79.16 | -20.84 | 478 | 21.3 | -46.44 | -8.87 | -52.82 | 1247 |
| 61 | Candlestick reversal · 1h | reversion | 79.01 | -21.00 | 231 | 30.3 | -38.08 | -7.02 | -41.83 | 537 |
| 62 | Max aggression: 1-day momentum | meta | 77.13 | -22.87 | 17 | 29.4 | -34.21 | -2.15 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.64 | -22.13 | -78.91 | 1711 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -65.11 | -20.58 | -65.35 | 875 |
| 65 | RSI(14) reversion | reversion | 57.32 | -42.68 | 760 | 27.2 | -74.27 | -16.55 | -74.90 | 1610 |
| 66 | Donchian 55/20 | breakout | 56.49 | -43.51 | 534 | 19.7 | -72.20 | -19.76 | -74.04 | 1284 |
| 67 | Squeeze breakout | breakout | 56.28 | -43.72 | 522 | 14.2 | -66.89 | -23.00 | -67.87 | 1211 |
| 68 | EMA 20/50 cross | trend | 55.38 | -44.62 | 573 | 20.4 | -78.89 | -19.61 | -80.87 | 1439 |
| 69 | VWAP reversion | reversion | 54.37 | -45.63 | 765 | 26.0 | -70.67 | -14.15 | -72.15 | 1464 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.77 | -31.96 | -98.80 | 5281 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.10 | -35.48 | -94.28 | 2602 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.84 | -23.64 | -88.67 | 1896 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.18 | -28.37 | -91.74 | 2366 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.51 | -26.71 | -91.51 | 2281 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.68 | -35.43 | -97.80 | 3506 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -39.05 | -97.00 | 3575 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.56 | -28.50 | -94.73 | 2569 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.02 | -28.28 | -83.52 | 1736 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -37.34 | -99.38 | 5716 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.00 | -29.06 | -92.66 | 2626 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.89 | -32.34 | -95.89 | 3480 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -43.56 | -99.77 | 6160 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.74 | -30.93 | -91.89 | 2336 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -41.01 | -97.81 | 3641 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.93 | -98.50 | 4701 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.21 | -36.17 | -94.45 | 2808 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.50 | -28.78 | -84.44 | 1807 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.64 | -99.54 | 6179 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.89 | -22.91 | -87.01 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.90 | -26.99 | -88.05 | 2129 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.96 | -33.78 | -95.96 | 3761 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.50 | -34.61 | -89.50 | 2098 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -34.54 | -95.82 | 4079 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.70 | -99.91 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 21:22:05.000174+00:00 -> 2026-10-21 21:32:05.000174+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
