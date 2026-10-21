# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T14:24:05.000144+00:00 · 30776 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.77 (-9.23%)

Closed trades 90, win rate 41.1%, fees £2.99, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 18.08 | -0.09 |

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

Today: 13233 decisions in 2091 calls, $0.1772 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T14:24 | 13 / 12 / 5 | MSTR 17%, COIN 15% |  |
| Breezy | 2026-10-21T14:24 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-21T14:24 | 7 / 22 / 1 | MSTR 83% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.03 | 6.04 | 0 | — | 8.24 | 3.84 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -0.43 | -0.03 | -8.92 | 26 |
| 4 | Max aggression: 5-day momentum | meta | 104.40 | 4.40 | 10 | 50.0 | -4.65 | -0.09 | -34.64 | 26 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold BTC | benchmark | 98.98 | -1.02 | 0 | — | 15.96 | 2.28 | -8.68 | 1 |
| 10 | Hold SPY | benchmark | 98.82 | -1.18 | 0 | — | 0.28 | 0.21 | -3.13 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.79 | -1.21 | 63 | 34.9 | 2.13 | 1.26 | -2.29 | 64 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 98.52 | -1.48 | 0 | — | -0.52 | -0.14 | -5.02 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.42 | -1.58 | 4 | 50.0 | 6.99 | 1.54 | -7.93 | 8 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.17 | -1.80 | -5.83 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 96.94 | -3.06 | 0 | — | 0.48 | 0.26 | -5.31 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 96.81 | -3.19 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 18 | Copy: Insider buying | copy | 96.52 | -3.48 | 25 | 40.0 | -11.49 | -1.96 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 96.09 | -3.91 | 114 | 31.6 | -6.09 | -3.05 | -7.93 | 286 |
| 20 | Donchian 55/20 · 1h | breakout | 96.06 | -3.94 | 40 | 15.0 | -14.37 | -2.88 | -15.92 | 100 |
| 21 | Trend pullback · 1h | trend | 95.55 | -4.45 | 90 | 23.3 | -19.34 | -5.85 | -19.73 | 130 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 95.37 | -4.63 | 89 | 18.0 | -12.32 | -2.25 | -16.68 | 256 |
| 24 | Daily: Momentum burst | daily | 94.47 | -5.53 | 6 | 16.7 | -8.61 | -1.24 | -20.58 | 38 |
| 25 | Squeeze breakout · 1h | breakout | 92.76 | -7.24 | 46 | 21.7 | -1.74 | -0.34 | -11.48 | 97 |
| 26 | Gap and go | momentum | 92.68 | -7.32 | 82 | 17.1 | 3.84 | 1.24 | -7.13 | 202 |
| 27 | Parabolic SAR · 1h | trend | 92.63 | -7.38 | 106 | 21.7 | -16.57 | -3.53 | -20.05 | 272 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 92.41 | -7.59 | 0 | — | 1.33 | 0.37 | -14.37 | 1 |
| 29 | Opening range 30m | breakout | 92.09 | -7.91 | 225 | 32.4 | -12.23 | -3.57 | -17.26 | 556 |
| 30 | Bollinger breakout · 1h | breakout | 91.69 | -8.31 | 87 | 29.9 | -11.16 | -2.04 | -16.38 | 255 |
| 31 | Daily: Bullish score | daily | 91.26 | -8.74 | 8 | 0.0 | -4.30 | -0.41 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -1.96 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.82 | -9.18 | 87 | 24.1 | -13.09 | -2.35 | -14.48 | 106 |
| 34 | Agent | meta | 90.77 | -9.23 | 90 | 41.1 | -13.20 | -7.16 | -15.11 | 251 |
| 35 | Connors RSI(2) · 1h | reversion | 89.85 | -10.15 | 155 | 41.9 | -21.66 | -6.41 | -23.42 | 195 |
| 36 | RSI momentum · 1h | momentum | 89.76 | -10.24 | 83 | 15.7 | -22.37 | -4.44 | -23.79 | 218 |
| 37 | Supertrend · 1h | trend | 89.32 | -10.68 | 88 | 12.5 | -21.23 | -4.13 | -26.62 | 221 |
| 38 | EMA 20/50 cross · 1h | trend | 89.17 | -10.83 | 62 | 12.9 | -20.37 | -3.60 | -23.33 | 135 |
| 39 | Stochastic reversion · 1h | reversion | 88.37 | -11.63 | 165 | 46.7 | -13.79 | -2.27 | -22.24 | 362 |
| 40 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 60 | 21.7 | -20.17 | -3.92 | -27.09 | 201 |
| 41 | Agent (aggressive) | meta | 87.88 | -12.12 | 44 | 36.4 | -9.32 | -2.78 | -10.86 | 109 |
| 42 | Ichimoku · 1h | trend | 87.27 | -12.73 | 60 | 13.3 | -18.19 | -3.41 | -20.25 | 117 |
| 43 | Opening range 15m | breakout | 87.08 | -12.93 | 272 | 29.0 | -17.65 | -4.76 | -19.78 | 694 |
| 44 | MACD cross · 1h | trend | 86.93 | -13.07 | 197 | 20.8 | -26.32 | -5.04 | -28.85 | 470 |
| 45 | Triple EMA stack · 1h | trend | 85.72 | -14.28 | 91 | 14.3 | -30.69 | -5.67 | -31.27 | 228 |
| 46 | Donchian 20/10 · 1h | breakout | 85.59 | -14.41 | 81 | 17.3 | -20.38 | -3.79 | -29.11 | 219 |
| 47 | Z-score reversion · 1h | reversion | 85.44 | -14.56 | 96 | 30.2 | -13.07 | -2.10 | -21.32 | 195 |
| 48 | MFI reversion · 1h | reversion | 85.10 | -14.90 | 226 | 32.3 | -15.22 | -2.32 | -21.11 | 140 |
| 49 | Agent (ML meta-label) | meta | 84.42 | -15.58 | 711 | 19.1 | -6.41 | -0.99 | -15.45 | 361 |
| 50 | MACD zero-line · 1h | trend | 84.34 | -15.66 | 91 | 15.4 | -25.56 | -4.98 | -27.29 | 221 |
| 51 | OBV trend · 1h | momentum | 84.01 | -15.99 | 186 | 17.2 | -30.70 | -5.76 | -31.65 | 312 |
| 52 | Three white soldiers | momentum | 82.36 | -17.64 | 252 | 19.4 | -46.42 | -18.16 | -47.10 | 610 |
| 53 | Bollinger reversion · 1h | reversion | 82.23 | -17.77 | 162 | 35.8 | -29.39 | -5.69 | -32.83 | 347 |
| 54 | ROC + volume · 1h | momentum | 82.17 | -17.83 | 209 | 23.0 | -27.31 | -4.99 | -33.70 | 386 |
| 55 | Williams %R · 1h | reversion | 81.94 | -18.06 | 195 | 43.6 | -29.86 | -4.56 | -36.50 | 523 |
| 56 | CCI reversion · 1h | reversion | 81.26 | -18.74 | 178 | 41.6 | -18.48 | -2.33 | -27.44 | 441 |
| 57 | Heikin-Ashi · 1h | trend | 80.95 | -19.05 | 235 | 20.9 | -44.42 | -9.61 | -47.28 | 673 |
| 58 | RSI(14) reversion · 1h | reversion | 80.61 | -19.39 | 83 | 22.9 | -11.36 | -1.90 | -23.28 | 171 |
| 59 | EMA 9/21 cross · 1h | trend | 80.56 | -19.44 | 143 | 10.5 | -28.85 | -5.87 | -30.70 | 327 |
| 60 | Candlestick reversal · 1h | reversion | 78.04 | -21.96 | 226 | 28.8 | -37.60 | -6.72 | -40.44 | 535 |
| 61 | VWAP momentum · 1h | momentum | 78.02 | -21.98 | 468 | 20.7 | -45.74 | -8.36 | -51.76 | 1252 |
| 62 | Max aggression: 1-day momentum | meta | 74.74 | -25.26 | 17 | 29.4 | -36.23 | -2.31 | -41.57 | 42 |
| 63 | Volume breakout | breakout | 59.78 | -40.22 | 390 | 13.6 | -64.54 | -20.21 | -64.81 | 862 |
| 64 | ROC + volume | momentum | 59.73 | -40.27 | 647 | 22.6 | -78.11 | -22.13 | -79.12 | 1726 |
| 65 | RSI(14) reversion | reversion | 57.12 | -42.88 | 747 | 26.5 | -74.09 | -16.19 | -74.89 | 1602 |
| 66 | Squeeze breakout | breakout | 56.46 | -43.55 | 511 | 13.7 | -67.18 | -22.75 | -67.77 | 1222 |
| 67 | Donchian 55/20 | breakout | 56.16 | -43.84 | 520 | 18.7 | -71.92 | -18.73 | -74.04 | 1284 |
| 68 | EMA 20/50 cross | trend | 54.95 | -45.05 | 562 | 19.4 | -78.37 | -17.70 | -80.87 | 1455 |
| 69 | VWAP reversion | reversion | 53.62 | -46.38 | 757 | 25.2 | -71.28 | -14.44 | -72.15 | 1470 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.79 | -31.43 | -98.80 | 5327 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.00 | -33.79 | -94.25 | 2607 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.56 | -22.08 | -88.67 | 1901 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.93 | -25.90 | -91.71 | 2372 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.44 | -26.31 | -91.65 | 2279 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.67 | -34.16 | -97.77 | 3531 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -38.23 | -96.98 | 3615 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.49 | -27.97 | -94.66 | 2544 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.95 | -27.69 | -83.33 | 1725 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.90 | -99.37 | 5719 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.04 | -28.06 | -92.66 | 2628 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.96 | -31.65 | -95.97 | 3455 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.72 | -99.76 | 6184 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.72 | -29.57 | -91.89 | 2356 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -39.70 | -97.78 | 3615 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.41 | -98.49 | 4710 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.32 | -35.88 | -94.45 | 2809 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.61 | -27.94 | -84.43 | 1806 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.24 | -99.53 | 6181 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.71 | -22.17 | -87.01 | 2145 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.69 | -25.90 | -88.05 | 2144 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -32.75 | -95.94 | 3763 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.38 | -33.77 | -89.45 | 2109 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -33.35 | -95.76 | 4107 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.71 | -99.91 | 8292 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T14:20 | Opening range 30m | buy | PLTR | 23.03 | — | entry signal |
| 2026-10-21T14:20 | Opening range 15m | buy | PLTR | 21.77 | — | entry signal |
| 2026-10-21T14:16 | VWAP reversion | buy | SOXL | 13.40 | — | entry signal |
| 2026-10-21T14:16 | Squeeze breakout | buy | TSLA | 6.00 | — | rebalance up |
| 2026-10-21T14:16 | Squeeze breakout | buy | TQQQ | 6.06 | — | rebalance up |
| 2026-10-21T14:16 | Squeeze breakout | buy | QQQ | 6.02 | — | rebalance up |
| 2026-10-21T14:16 | Squeeze breakout | sell | SOXL | 7.99 | -0.17 | exit signal |
| 2026-10-21T14:16 | Squeeze breakout | sell | NVDA | 8.04 | -0.10 | stop-loss |
| 2026-10-21T14:16 | Squeeze breakout | sell | META | 8.06 | -0.04 | stop-loss |
| 2026-10-21T14:16 | ROC + volume | buy | QQQ | 3.17 | — | rebalance up |
| 2026-10-21T14:16 | ROC + volume | buy | BITX | 3.15 | — | rebalance up |
| 2026-10-21T14:16 | ROC + volume | sell | NVDA | 4.96 | -0.06 | stop-loss |
| 2026-10-21T14:10 | Squeeze breakout | sell | SPY | 8.10 | -0.03 | stop-loss |
| 2026-10-21T14:10 | ROC + volume | sell | UPRO | 5.97 | -0.03 | stop-loss |
| 2026-10-21T14:10 | EMA 20/50 cross | sell | UPRO | 4.93 | -0.04 | stop-loss |
| 2026-10-21T14:10 | EMA 20/50 cross | sell | SPY | 5.02 | -0.02 | stop-loss |
| 2026-10-21T14:05 | Day trade: Stocks in Play ORB | sell | TSLA | 24.55 | -0.16 | target is flat |
| 2026-10-21T14:05 | VWAP momentum · 1h | buy | XRP-USD | 5.04 | — | rebalance up |
| 2026-10-21T14:05 | VWAP momentum · 1h | sell | TSLA | 8.85 | 0.27 | target is flat |
| 2026-10-21T14:05 | Squeeze breakout | buy | TSLA | 3.32 | — | rebalance up |
| 2026-10-21T14:05 | Squeeze breakout | buy | TQQQ | 3.36 | — | rebalance up |
| 2026-10-21T14:05 | Squeeze breakout | buy | SPY | 3.37 | — | rebalance up |
| 2026-10-21T14:05 | Squeeze breakout | buy | SOXL | 3.40 | — | rebalance up |
| 2026-10-21T14:05 | Squeeze breakout | buy | QQQ | 3.36 | — | rebalance up |
| 2026-10-21T14:05 | Squeeze breakout | buy | NVDA | 3.37 | — | rebalance up |
| 2026-10-21T14:05 | Squeeze breakout | buy | META | 3.33 | — | rebalance up |
| 2026-10-21T14:05 | Squeeze breakout | sell | TNA | 4.71 | -0.05 | stop-loss |
| 2026-10-21T14:05 | Squeeze breakout | sell | MSTR | 4.70 | -0.07 | stop-loss |
| 2026-10-21T14:05 | Squeeze breakout | sell | IWM | 4.74 | -0.02 | stop-loss |
| 2026-10-21T14:05 | Squeeze breakout | sell | COIN | 4.68 | -0.08 | stop-loss |
| 2026-10-21T14:05 | Opening range 15m | sell | LABU | 17.09 | -0.56 | target is flat |
| 2026-10-21T14:05 | Opening range 15m | sell | COIN | 17.24 | -0.41 | stop-loss |
| 2026-10-21T14:05 | Donchian 55/20 | buy | XRP-USD | 4.20 | — | rebalance up |
| 2026-10-21T14:05 | Donchian 55/20 | buy | TSLA | 4.26 | — | rebalance up |
| 2026-10-21T14:05 | Donchian 55/20 | buy | PLTR | 4.22 | — | rebalance up |
| 2026-10-21T14:05 | Donchian 55/20 | buy | META | 4.19 | — | rebalance up |
| 2026-10-21T14:05 | Donchian 55/20 | buy | ETH-USD | 4.21 | — | rebalance up |
| 2026-10-21T14:05 | Donchian 55/20 | buy | BITX | 4.23 | — | rebalance up |
| 2026-10-21T14:05 | Donchian 55/20 | sell | TNA | 5.09 | -0.06 | stop-loss |
| 2026-10-21T14:05 | Donchian 55/20 | sell | MSTR | 5.08 | -0.07 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 14:24:05.000144+00:00 -> 2026-10-21 14:34:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
