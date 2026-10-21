# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T17:50:05.000108+00:00 · 30942 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.65 (-9.35%)

Closed trades 91, win rate 40.7%, fees £3.01, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 18.13 | -0.00 |

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

### Market regime (QQQ, 2026-10-20)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.22 · VIX 17.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 28080 decisions in 2589 calls, $0.3504 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T17:50 | 2 / 9 / 19 | cash |  |
| Breezy | 2026-10-21T17:50 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-21T17:50 | 4 / 20 / 6 | MSTR 69% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.24 | 6.24 | 0 | — | 8.59 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.56 | 4.57 | 13 | 53.8 | 7.01 | 2.30 | -3.61 | 22 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 5 | Max aggression: 5-day momentum | meta | 103.45 | 3.45 | 10 | 50.0 | -5.51 | -0.17 | -34.64 | 26 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.76 | 0.76 | 4 | 50.0 | 9.63 | 1.99 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold BTC | benchmark | 99.88 | -0.12 | 0 | — | 16.32 | 2.32 | -8.68 | 1 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.74 | -0.26 | 0 | — | 0.86 | 0.43 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.47 | -0.53 | 0 | — | 1.30 | 0.79 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.01 | -0.99 | 63 | 34.9 | 2.45 | 1.44 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.64 | -2.36 | 0 | — | 1.16 | 0.54 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.13 | -2.87 | 0 | — | -3.90 | -1.48 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -1.79 | -5.83 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.59 | -3.41 | 41 | 17.1 | -13.92 | -2.81 | -16.00 | 103 |
| 19 | Copy: Insider buying | copy | 96.43 | -3.56 | 25 | 40.0 | -11.56 | -1.97 | -20.62 | 72 |
| 20 | Agent (rotation) | meta | 96.24 | -3.76 | 115 | 31.3 | -5.03 | -2.70 | -7.40 | 266 |
| 21 | ADX DI cross · 1h | trend | 96.12 | -3.88 | 91 | 19.8 | -11.03 | -1.93 | -16.94 | 256 |
| 22 | Daily: Momentum burst | daily | 95.64 | -4.36 | 6 | 16.7 | -8.86 | -1.28 | -20.58 | 38 |
| 23 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 24 | Trend pullback · 1h | trend | 95.05 | -4.95 | 92 | 23.9 | -20.24 | -6.19 | -20.44 | 131 |
| 25 | Gap and go | momentum | 94.53 | -5.47 | 87 | 19.5 | 6.04 | 1.87 | -7.13 | 207 |
| 26 | Opening range 30m | breakout | 93.89 | -6.11 | 225 | 32.4 | -10.58 | -2.95 | -17.26 | 571 |
| 27 | Parabolic SAR · 1h | trend | 93.86 | -6.14 | 108 | 23.1 | -15.72 | -3.40 | -19.79 | 272 |
| 28 | Squeeze breakout · 1h | breakout | 93.64 | -6.36 | 46 | 21.7 | -1.77 | -0.34 | -11.48 | 101 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 93.27 | -6.73 | 0 | — | 3.33 | 0.67 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.93 | -7.07 | 87 | 29.9 | -8.95 | -1.55 | -15.47 | 262 |
| 31 | Daily: Bullish score | daily | 92.01 | -7.99 | 8 | 0.0 | -2.90 | -0.21 | -13.10 | 13 |
| 32 | Volume breakout · 1h | breakout | 91.37 | -8.63 | 89 | 23.6 | -12.04 | -2.13 | -13.90 | 113 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.35 | -1.95 | -16.91 | 1 |
| 34 | Agent | meta | 90.65 | -9.35 | 91 | 40.7 | -11.60 | -6.33 | -12.44 | 250 |
| 35 | Supertrend · 1h | trend | 90.59 | -9.41 | 88 | 12.5 | -20.11 | -3.80 | -26.62 | 226 |
| 36 | RSI momentum · 1h | momentum | 90.21 | -9.79 | 84 | 16.7 | -18.58 | -3.62 | -21.66 | 220 |
| 37 | Connors RSI(2) · 1h | reversion | 89.79 | -10.21 | 158 | 42.4 | -21.72 | -6.43 | -23.42 | 197 |
| 38 | Stochastic reversion · 1h | reversion | 89.51 | -10.49 | 169 | 47.3 | -13.67 | -2.24 | -22.24 | 362 |
| 39 | EMA 20/50 cross · 1h | trend | 89.39 | -10.62 | 62 | 12.9 | -20.60 | -3.60 | -23.73 | 137 |
| 40 | Opening range 15m | breakout | 88.60 | -11.40 | 274 | 28.8 | -16.08 | -4.29 | -19.72 | 709 |
| 41 | Keltner breakout · 1h | breakout | 88.53 | -11.47 | 61 | 23.0 | -16.45 | -2.98 | -24.60 | 205 |
| 42 | MACD cross · 1h | trend | 87.90 | -12.10 | 199 | 21.1 | -23.24 | -4.34 | -26.95 | 467 |
| 43 | Ichimoku · 1h | trend | 87.59 | -12.41 | 60 | 13.3 | -17.83 | -3.32 | -20.25 | 118 |
| 44 | Agent (aggressive) | meta | 87.58 | -12.42 | 45 | 35.6 | -12.66 | -3.43 | -13.03 | 115 |
| 45 | Z-score reversion · 1h | reversion | 86.84 | -13.16 | 102 | 34.3 | -11.41 | -1.76 | -21.32 | 196 |
| 46 | Donchian 20/10 · 1h | breakout | 86.46 | -13.54 | 83 | 19.3 | -19.44 | -3.55 | -29.01 | 229 |
| 47 | Triple EMA stack · 1h | trend | 86.12 | -13.88 | 92 | 15.2 | -28.66 | -5.32 | -30.40 | 223 |
| 48 | MFI reversion · 1h | reversion | 85.18 | -14.82 | 228 | 32.9 | -14.53 | -2.19 | -21.11 | 139 |
| 49 | Agent (ML meta-label) | meta | 85.06 | -14.94 | 729 | 20.2 | -12.10 | -2.18 | -16.04 | 351 |
| 50 | MACD zero-line · 1h | trend | 84.82 | -15.18 | 92 | 15.2 | -22.99 | -4.43 | -26.06 | 225 |
| 51 | OBV trend · 1h | momentum | 84.56 | -15.44 | 188 | 17.6 | -31.09 | -5.85 | -32.38 | 314 |
| 52 | ROC + volume · 1h | momentum | 83.48 | -16.52 | 212 | 23.6 | -26.56 | -4.77 | -33.04 | 390 |
| 53 | Three white soldiers | momentum | 82.63 | -17.38 | 257 | 20.6 | -46.02 | -17.82 | -46.93 | 607 |
| 54 | Bollinger reversion · 1h | reversion | 82.61 | -17.39 | 163 | 36.2 | -29.07 | -5.61 | -32.84 | 348 |
| 55 | Williams %R · 1h | reversion | 82.48 | -17.52 | 199 | 44.7 | -31.54 | -4.90 | -36.58 | 517 |
| 56 | CCI reversion · 1h | reversion | 82.10 | -17.90 | 188 | 43.6 | -20.33 | -2.64 | -27.44 | 436 |
| 57 | Heikin-Ashi · 1h | trend | 81.83 | -18.16 | 236 | 21.2 | -42.92 | -9.13 | -46.27 | 682 |
| 58 | EMA 9/21 cross · 1h | trend | 81.38 | -18.61 | 143 | 10.5 | -27.00 | -5.11 | -30.32 | 333 |
| 59 | RSI(14) reversion · 1h | reversion | 81.18 | -18.82 | 85 | 24.7 | -13.62 | -2.44 | -23.28 | 170 |
| 60 | VWAP momentum · 1h | momentum | 79.45 | -20.55 | 475 | 21.3 | -45.16 | -8.21 | -51.96 | 1255 |
| 61 | Candlestick reversal · 1h | reversion | 78.72 | -21.29 | 230 | 30.0 | -36.42 | -6.44 | -39.73 | 538 |
| 62 | Max aggression: 1-day momentum | meta | 77.42 | -22.58 | 17 | 29.4 | -33.94 | -2.11 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 60.15 | -39.85 | 673 | 23.3 | -77.83 | -21.88 | -79.10 | 1724 |
| 64 | Volume breakout | breakout | 59.25 | -40.75 | 398 | 13.6 | -64.95 | -20.29 | -65.21 | 874 |
| 65 | RSI(14) reversion | reversion | 57.10 | -42.90 | 750 | 26.7 | -74.03 | -16.13 | -74.89 | 1609 |
| 66 | Donchian 55/20 | breakout | 56.90 | -43.10 | 522 | 18.8 | -71.95 | -19.24 | -74.04 | 1292 |
| 67 | Squeeze breakout | breakout | 56.61 | -43.39 | 516 | 14.0 | -66.90 | -22.86 | -67.80 | 1216 |
| 68 | EMA 20/50 cross | trend | 55.69 | -44.31 | 563 | 19.5 | -78.48 | -18.43 | -80.88 | 1445 |
| 69 | VWAP reversion | reversion | 54.00 | -46.00 | 761 | 25.6 | -70.86 | -14.15 | -72.15 | 1465 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.76 | -30.99 | -98.80 | 5304 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.84 | -32.99 | -94.23 | 2611 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.47 | -22.10 | -88.67 | 1903 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.83 | -26.16 | -91.71 | 2378 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.53 | -26.37 | -91.56 | 2282 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.63 | -33.81 | -97.77 | 3512 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.88 | -37.81 | -96.96 | 3594 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.38 | -28.00 | -94.57 | 2539 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.85 | -27.79 | -83.42 | 1736 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.79 | -99.37 | 5705 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.85 | -27.67 | -92.66 | 2636 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.91 | -31.51 | -95.95 | 3458 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.30 | -99.76 | 6179 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.63 | -29.40 | -91.89 | 2346 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -39.41 | -97.81 | 3630 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.27 | -98.48 | 4690 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.22 | -35.27 | -94.45 | 2815 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.36 | -27.86 | -84.44 | 1814 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.26 | -99.53 | 6155 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.84 | -22.45 | -87.01 | 2135 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.70 | -25.89 | -88.05 | 2136 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -32.52 | -95.91 | 3743 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.25 | -33.06 | -89.42 | 2101 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -33.33 | -95.75 | 4066 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.94 | -99.91 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T17:50 | Volume breakout | buy | AMZN | 14.81 | — | entry signal |
| 2026-10-21T17:50 | Squeeze breakout | buy | GOOGL | 5.10 | — | rebalance up |
| 2026-10-21T17:50 | Squeeze breakout | buy | AMD | 2.84 | — | rebalance up |
| 2026-10-21T17:50 | Squeeze breakout | sell | TQQQ | 11.29 | 0.22 | exit signal |
| 2026-10-21T17:50 | Squeeze breakout | sell | QQQ | 11.32 | 0.07 | exit signal |
| 2026-10-21T17:45 | VWAP reversion | sell | LABU | 13.59 | 0.12 | exit signal |
| 2026-10-21T17:40 | ROC + volume | buy | UPRO | 8.33 | — | rebalance up |
| 2026-10-21T17:40 | ROC + volume | buy | LABU | 6.41 | — | rebalance up |
| 2026-10-21T17:40 | ROC + volume | sell | TQQQ | 6.67 | -0.04 | exit signal |
| 2026-10-21T17:40 | ROC + volume | sell | QQQ | 6.71 | -0.00 | exit signal |
| 2026-10-21T17:40 | ROC + volume | sell | PLTR | 6.71 | 0.05 | exit signal |
| 2026-10-21T17:40 | ROC + volume | sell | COIN | 6.69 | -0.04 | exit signal |
| 2026-10-21T17:40 | ROC + volume | sell | AMD | 6.71 | 0.03 | exit signal |
| 2026-10-21T17:35 | Agent (ML meta-label) | buy | QQQ | 4.57 | — | rebalance up |
| 2026-10-21T17:35 | Agent (ML meta-label) | sell | ETHU | 9.46 | 0.01 | selected signal exited |
| 2026-10-21T17:35 | Volume breakout | sell | UPRO | 14.85 | -0.03 | exit signal |
| 2026-10-21T17:35 | ROC + volume | buy | LABU | 8.59 | — | entry |
| 2026-10-21T17:35 | ROC + volume | sell | TECL | 7.49 | -0.04 | target is flat |
| 2026-10-21T17:30 | Agent (ML meta-label) | buy | ETHU | 9.45 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T17:30 | Agent (ML meta-label) | sell | SQQQ | 7.39 | -0.24 | selected signal exited |
| 2026-10-21T17:30 | Agent (ML meta-label) | sell | NVDA | 7.78 | 0.12 | selected signal exited |
| 2026-10-21T17:30 | Williams %R · 1h | buy | GOOGL | 20.60 | — | entry signal |
| 2026-10-21T17:30 | Z-score reversion · 1h | buy | GOOGL | 21.72 | — | entry signal |
| 2026-10-21T17:30 | Z-score reversion · 1h | sell | NVDA | 21.72 | 0.27 | exit signal |
| 2026-10-21T17:30 | RSI(14) reversion · 1h | buy | GOOGL | 20.29 | — | entry signal |
| 2026-10-21T17:30 | RSI(14) reversion · 1h | sell | AMD | 20.48 | 0.53 | exit signal |
| 2026-10-21T17:30 | Candlestick reversal · 1h | buy | SQQQ | 6.66 | — | rebalance up |
| 2026-10-21T17:30 | Candlestick reversal · 1h | buy | QQQ | 6.67 | — | rebalance up |
| 2026-10-21T17:30 | Candlestick reversal · 1h | buy | PLTR | 6.50 | — | rebalance up |
| 2026-10-21T17:30 | Candlestick reversal · 1h | buy | MSFT | 6.81 | — | rebalance up |
| 2026-10-21T17:30 | Candlestick reversal · 1h | sell | SPY | 12.94 | 0.05 | exit signal |
| 2026-10-21T17:30 | Candlestick reversal · 1h | sell | META | 13.20 | 0.27 | exit signal |
| 2026-10-21T17:30 | RSI momentum · 1h | buy | PLTR | 5.00 | — | entry |
| 2026-10-21T17:30 | RSI momentum · 1h | buy | NVDA | 5.01 | — | entry signal |
| 2026-10-21T17:30 | RSI momentum · 1h | buy | MSTR | 5.01 | — | entry |
| 2026-10-21T17:30 | RSI momentum · 1h | buy | ETHU | 5.01 | — | entry |
| 2026-10-21T17:30 | RSI momentum · 1h | buy | COIN | 5.01 | — | entry |
| 2026-10-21T17:30 | RSI momentum · 1h | sell | TNA | 4.98 | 0.05 | rebalance down |
| 2026-10-21T17:30 | RSI momentum · 1h | sell | LABU | 5.24 | 0.18 | rebalance down |
| 2026-10-21T17:30 | RSI momentum · 1h | sell | IWM | 4.90 | 0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 17:50:05.000108+00:00 -> 2026-10-21 18:00:05.000108+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
