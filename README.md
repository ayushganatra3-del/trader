# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T17:20:05.000572+00:00 · 30913 ticks

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

Today: 25494 decisions in 2502 calls, $0.3202 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T17:20 | 9 / 15 / 6 | AMD 20%, SOXL 15%, TECL 15% |  |
| Breezy | 2026-10-21T17:20 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-10-21T17:20 | 11 / 17 / 2 | COIN 72% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.45 | 6.45 | 0 | — | 8.73 | 4.06 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.11 | 5.11 | 13 | 53.8 | 7.48 | 2.46 | -3.45 | 22 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 5 | Max aggression: 5-day momentum | meta | 103.48 | 3.48 | 10 | 50.0 | -5.56 | -0.18 | -34.64 | 26 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.29 | 1.29 | 4 | 50.0 | 10.13 | 2.07 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.82 | -0.18 | 0 | — | 0.64 | 0.34 | -5.02 | 1 |
| 11 | Hold BTC | benchmark | 99.81 | -0.19 | 0 | — | 15.75 | 2.25 | -8.68 | 1 |
| 12 | Hold SPY | benchmark | 99.57 | -0.43 | 0 | — | 1.32 | 0.80 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.73 | 63 | 34.9 | 2.67 | 1.56 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.42 | -2.58 | 0 | — | 0.81 | 0.40 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.21 | -2.79 | 0 | — | -3.90 | -1.48 | -7.04 | 1 |
| 17 | Copy: Insider buying | copy | 97.21 | -2.79 | 25 | 40.0 | -10.95 | -1.85 | -20.62 | 72 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.14 | -1.78 | -5.83 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 96.50 | -3.50 | 41 | 17.1 | -14.10 | -2.82 | -16.01 | 103 |
| 20 | Agent (rotation) | meta | 96.44 | -3.56 | 115 | 31.3 | -5.08 | -2.63 | -7.41 | 276 |
| 21 | ADX DI cross · 1h | trend | 96.08 | -3.92 | 91 | 19.8 | -11.50 | -1.98 | -17.48 | 255 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 95.48 | -4.52 | 6 | 16.7 | -8.62 | -1.24 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 95.04 | -4.96 | 91 | 24.2 | -20.29 | -6.21 | -20.44 | 131 |
| 25 | Gap and go | momentum | 94.55 | -5.45 | 87 | 19.5 | 6.05 | 1.87 | -7.13 | 207 |
| 26 | Opening range 30m | breakout | 93.99 | -6.01 | 225 | 32.4 | -10.47 | -2.91 | -17.26 | 571 |
| 27 | Parabolic SAR · 1h | trend | 93.79 | -6.21 | 108 | 23.1 | -15.80 | -3.37 | -19.76 | 274 |
| 28 | Squeeze breakout · 1h | breakout | 93.54 | -6.46 | 46 | 21.7 | -0.78 | -0.09 | -11.48 | 99 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 93.37 | -6.63 | 0 | — | 3.57 | 0.70 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.84 | -7.16 | 87 | 29.9 | -8.81 | -1.53 | -15.28 | 258 |
| 31 | Daily: Bullish score | daily | 92.17 | -7.83 | 8 | 0.0 | -2.34 | -0.14 | -13.10 | 13 |
| 32 | Volume breakout · 1h | breakout | 91.33 | -8.66 | 89 | 23.6 | -12.09 | -2.14 | -13.90 | 112 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.34 | -1.95 | -16.91 | 1 |
| 34 | Agent | meta | 90.65 | -9.35 | 91 | 40.7 | -11.31 | -6.21 | -11.62 | 243 |
| 35 | Supertrend · 1h | trend | 90.58 | -9.42 | 88 | 12.5 | -21.22 | -4.06 | -26.98 | 227 |
| 36 | RSI momentum · 1h | momentum | 90.24 | -9.76 | 84 | 16.7 | -18.67 | -3.65 | -21.66 | 217 |
| 37 | Connors RSI(2) · 1h | reversion | 89.70 | -10.30 | 158 | 42.4 | -21.82 | -6.47 | -23.42 | 197 |
| 38 | Stochastic reversion · 1h | reversion | 89.50 | -10.50 | 169 | 47.3 | -13.67 | -2.24 | -22.24 | 362 |
| 39 | EMA 20/50 cross · 1h | trend | 89.29 | -10.71 | 62 | 12.9 | -20.07 | -3.48 | -23.09 | 137 |
| 40 | Opening range 15m | breakout | 88.70 | -11.30 | 274 | 28.8 | -16.07 | -4.28 | -19.78 | 709 |
| 41 | Keltner breakout · 1h | breakout | 88.49 | -11.51 | 61 | 23.0 | -19.70 | -3.75 | -25.18 | 204 |
| 42 | MACD cross · 1h | trend | 87.93 | -12.07 | 199 | 21.1 | -23.30 | -4.36 | -26.96 | 468 |
| 43 | Agent (aggressive) | meta | 87.58 | -12.41 | 45 | 35.6 | -13.90 | -3.88 | -14.24 | 113 |
| 44 | Ichimoku · 1h | trend | 87.51 | -12.49 | 60 | 13.3 | -17.97 | -3.36 | -20.25 | 118 |
| 45 | Z-score reversion · 1h | reversion | 87.02 | -12.98 | 101 | 33.7 | -11.26 | -1.73 | -21.32 | 195 |
| 46 | Donchian 20/10 · 1h | breakout | 86.42 | -13.58 | 83 | 19.3 | -20.55 | -3.76 | -29.99 | 227 |
| 47 | Triple EMA stack · 1h | trend | 86.04 | -13.96 | 92 | 15.2 | -28.78 | -5.31 | -30.43 | 224 |
| 48 | MFI reversion · 1h | reversion | 85.18 | -14.82 | 228 | 32.9 | -14.49 | -2.20 | -21.11 | 139 |
| 49 | Agent (ML meta-label) | meta | 85.14 | -14.86 | 725 | 19.9 | -12.96 | -2.37 | -16.86 | 367 |
| 50 | MACD zero-line · 1h | trend | 84.80 | -15.20 | 92 | 15.2 | -22.85 | -4.38 | -25.88 | 223 |
| 51 | OBV trend · 1h | momentum | 84.51 | -15.49 | 188 | 17.6 | -30.98 | -5.81 | -32.21 | 313 |
| 52 | ROC + volume · 1h | momentum | 83.44 | -16.56 | 212 | 23.6 | -26.89 | -4.83 | -33.30 | 392 |
| 53 | Three white soldiers | momentum | 82.63 | -17.38 | 257 | 20.6 | -46.02 | -17.82 | -46.93 | 607 |
| 54 | Bollinger reversion · 1h | reversion | 82.60 | -17.40 | 163 | 36.2 | -29.10 | -5.62 | -32.84 | 348 |
| 55 | Williams %R · 1h | reversion | 82.37 | -17.62 | 199 | 44.7 | -31.64 | -4.92 | -36.57 | 516 |
| 56 | CCI reversion · 1h | reversion | 82.15 | -17.85 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 436 |
| 57 | Heikin-Ashi · 1h | trend | 81.92 | -18.08 | 236 | 21.2 | -43.05 | -9.17 | -46.42 | 679 |
| 58 | EMA 9/21 cross · 1h | trend | 81.39 | -18.61 | 143 | 10.5 | -26.45 | -5.10 | -29.76 | 328 |
| 59 | RSI(14) reversion · 1h | reversion | 81.17 | -18.83 | 84 | 23.8 | -10.64 | -1.76 | -23.28 | 177 |
| 60 | VWAP momentum · 1h | momentum | 79.53 | -20.47 | 474 | 21.1 | -45.01 | -8.18 | -51.85 | 1254 |
| 61 | Candlestick reversal · 1h | reversion | 78.82 | -21.18 | 228 | 29.4 | -34.38 | -5.87 | -37.83 | 546 |
| 62 | Max aggression: 1-day momentum | meta | 78.33 | -21.67 | 17 | 29.4 | -33.22 | -2.05 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 60.31 | -39.69 | 666 | 23.1 | -77.79 | -21.83 | -79.14 | 1726 |
| 64 | Volume breakout | breakout | 59.31 | -40.69 | 397 | 13.6 | -64.94 | -20.30 | -65.22 | 875 |
| 65 | RSI(14) reversion | reversion | 57.04 | -42.96 | 750 | 26.7 | -74.00 | -16.10 | -74.89 | 1606 |
| 66 | Donchian 55/20 | breakout | 56.86 | -43.14 | 522 | 18.8 | -71.81 | -19.03 | -74.04 | 1293 |
| 67 | Squeeze breakout | breakout | 56.79 | -43.21 | 514 | 13.6 | -66.70 | -22.53 | -67.80 | 1218 |
| 68 | EMA 20/50 cross | trend | 55.80 | -44.20 | 563 | 19.5 | -78.66 | -18.91 | -80.89 | 1443 |
| 69 | VWAP reversion | reversion | 53.88 | -46.12 | 760 | 25.5 | -71.02 | -14.26 | -72.15 | 1473 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.76 | -30.98 | -98.80 | 5314 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.84 | -33.02 | -94.23 | 2612 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.43 | -21.90 | -88.67 | 1904 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.80 | -25.94 | -91.71 | 2379 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.59 | -26.37 | -91.62 | 2282 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.62 | -33.69 | -97.77 | 3518 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.90 | -38.05 | -96.97 | 3604 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -28.05 | -94.58 | 2549 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.77 | -27.74 | -83.42 | 1734 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -35.97 | -99.38 | 5707 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.84 | -27.63 | -92.66 | 2639 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -31.55 | -95.95 | 3459 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.43 | -99.76 | 6179 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.59 | -29.13 | -91.89 | 2347 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -39.39 | -97.78 | 3635 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.21 | -98.48 | 4691 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.20 | -35.30 | -94.43 | 2818 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.30 | -27.77 | -84.44 | 1815 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.23 | -99.53 | 6158 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.81 | -22.35 | -87.01 | 2138 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.74 | -25.98 | -88.05 | 2133 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -32.55 | -95.91 | 3743 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -33.21 | -89.42 | 2103 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.76 | -33.44 | -95.76 | 4078 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.13 | -99.91 | 8297 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T17:20 | Gap and go | sell | MSTR | 23.55 | 0.57 | stop-loss |
| 2026-10-21T17:20 | ROC + volume | buy | LABU | 8.62 | — | entry |
| 2026-10-21T17:20 | ROC + volume | sell | MSTR | 6.64 | -0.08 | exit signal |
| 2026-10-21T17:15 | Squeeze breakout | buy | GOOGL | 9.05 | — | entry signal |
| 2026-10-21T17:15 | Squeeze breakout | sell | TQQQ | 3.18 | 0.07 | rebalance down |
| 2026-10-21T17:15 | Squeeze breakout | sell | QQQ | 2.91 | 0.02 | rebalance down |
| 2026-10-21T17:15 | Squeeze breakout | sell | AMD | 2.96 | 0.02 | rebalance down |
| 2026-10-21T17:10 | Agent (ML meta-label) | buy | ETHU | 7.74 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T17:10 | Donchian 55/20 | buy | MSFT | 2.29 | — | entry |
| 2026-10-21T17:10 | Donchian 55/20 | buy | AMZN | 3.34 | — | entry |
| 2026-10-21T17:10 | Donchian 55/20 | sell | META | 5.63 | 0.01 | exit signal |
| 2026-10-21T17:05 | Agent (ML meta-label) | sell | ETHU | 7.71 | -0.03 | selected signal exited |
| 2026-10-21T17:05 | Volume breakout | sell | TNA | 14.78 | -0.10 | exit signal |
| 2026-10-21T17:05 | Gap and go | buy | MSTR | 7.64 | — | rebalance up |
| 2026-10-21T17:05 | Gap and go | buy | COIN | 7.95 | — | rebalance up |
| 2026-10-21T17:05 | Gap and go | sell | ETHU | 15.84 | 0.29 | stop-loss |
| 2026-10-21T17:05 | Gap and go | sell | BITX | 18.96 | 0.28 | stop-loss |
| 2026-10-21T17:00 | Agent (rotation) | buy | TQQQ | 32.10 | — | entry |
| 2026-10-21T17:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 104.83 | — | entry |
| 2026-10-21T17:00 | Agent (ML meta-label) | buy | ETHU | 7.74 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T17:00 | Squeeze breakout · 1h | buy | SOL-USD | 14.89 | — | entry signal |
| 2026-10-21T17:00 | Squeeze breakout · 1h | sell | DOGE-USD | 4.70 | 0.09 | rebalance down |
| 2026-10-21T17:00 | Squeeze breakout · 1h | sell | BTC-USD | 4.77 | 0.06 | rebalance down |
| 2026-10-21T17:00 | Squeeze breakout · 1h | sell | BITX | 5.42 | 0.22 | rebalance down |
| 2026-10-21T16:55 | MFI reversion · 1h | sell | GOOGL | 21.32 | 0.03 | target is flat |
| 2026-10-21T16:55 | Volume breakout · 1h | buy | TQQQ | 5.10 | — | entry |
| 2026-10-21T16:55 | Volume breakout · 1h | buy | MSTR | 10.16 | — | entry |
| 2026-10-21T16:55 | Volume breakout · 1h | sell | XRP-USD | 5.09 | -0.02 | rebalance down |
| 2026-10-21T16:55 | Volume breakout · 1h | sell | TSLA | 5.05 | 0.03 | rebalance down |
| 2026-10-21T16:55 | Volume breakout · 1h | sell | ETHU | 5.12 | 0.03 | rebalance down |
| 2026-10-21T16:55 | VWAP reversion | buy | LABU | 13.46 | — | entry |
| 2026-10-21T16:55 | RSI(14) reversion | sell | GOOGL | 14.30 | 0.02 | exit signal |
| 2026-10-21T16:55 | Volume breakout | sell | ETH-USD | 14.74 | -0.15 | exit signal |
| 2026-10-21T16:55 | Squeeze breakout | buy | NVDA | 13.62 | — | entry signal |
| 2026-10-21T16:55 | Squeeze breakout | sell | BTC-USD | 13.62 | -0.14 | exit signal |
| 2026-10-21T16:55 | ROC + volume | sell | BITX | 6.66 | -0.06 | target is flat |
| 2026-10-21T16:50 | Agent (ML meta-label) | sell | ETHU | 7.71 | -0.02 | selected signal exited |
| 2026-10-21T16:50 | ROC + volume | sell | TECL | 6.70 | 0.04 | exit signal |
| 2026-10-21T16:45 | Day trade: Stocks in Play ORB | buy | AMD | 24.78 | — | entry |
| 2026-10-21T16:45 | Agent (ML meta-label) | buy | ETHU | 7.73 | — | following VWAP reversion, Bollinger reversion |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 17:20:05.000572+00:00 -> 2026-10-21 17:30:05.000572+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
