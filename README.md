# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T13:56:05.000137+00:00 · 29570 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.71 (-9.29%)

Closed trades 87, win rate 40.2%, fees £2.91, max drawdown -9.99%.

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

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 11955 decisions in 2013 calls, $0.1622 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T13:56 | 4 / 20 / 6 | TNA 17% |  |
| Breezy | 2026-10-20T13:56 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-10-20T13:56 | 7 / 22 / 1 | COIN 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| VWAP reversion | BITX | 1.77 | +3.00% | 6 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.75 | 5.75 | 11 | 72.7 | 0.64 | 0.27 | -8.92 | 26 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 105.55 | 5.55 | 0 | — | 6.56 | 3.11 | -5.18 | 1 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.43 | 5.43 | 16 | 37.5 | 7.08 | 1.79 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.02 | -0.97 | 0 | — | 0.21 | 0.17 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 98.72 | -1.27 | 0 | — | -0.79 | -0.41 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.56 | -1.44 | 58 | 34.5 | 2.19 | 1.26 | -1.45 | 61 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 12 | Max aggression: 5-day momentum | meta | 98.11 | -1.89 | 9 | 44.4 | -15.58 | -1.20 | -34.64 | 26 |
| 13 | Donchian 55/20 · 1h | breakout | 97.70 | -2.30 | 37 | 16.2 | -10.91 | -2.02 | -19.38 | 97 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.66 | -2.06 | -5.83 | 1 |
| 15 | Agent (rotation) | meta | 97.03 | -2.97 | 112 | 32.1 | -6.06 | -3.04 | -7.61 | 317 |
| 16 | Hold BTC | benchmark | 96.88 | -3.12 | 0 | — | 23.83 | 2.99 | -8.68 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.87 | -3.13 | 3 | 33.3 | 3.45 | 0.83 | -7.93 | 8 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.42 | -3.58 | 0 | — | -1.28 | -0.47 | -5.31 | 1 |
| 19 | Trend pullback · 1h | trend | 96.23 | -3.77 | 89 | 23.6 | -20.17 | -5.97 | -20.65 | 136 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 95.75 | -4.25 | 0 | — | -5.50 | -2.18 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Copy: Insider buying | copy | 94.78 | -5.22 | 23 | 43.5 | -12.25 | -2.11 | -20.62 | 72 |
| 23 | ADX DI cross · 1h | trend | 94.28 | -5.72 | 88 | 18.2 | -15.26 | -2.77 | -17.13 | 261 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.97 | -0.42 | -9.46 | 95 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.29 | 1.37 | -6.51 | 198 |
| 26 | Daily: Momentum burst | daily | 93.29 | -6.71 | 6 | 16.7 | -5.65 | -0.71 | -20.58 | 40 |
| 27 | Volume breakout · 1h | breakout | 91.77 | -8.23 | 78 | 23.1 | -12.60 | -2.26 | -16.37 | 102 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.80 | -2.22 | -16.91 | 1 |
| 29 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -14.35 | -4.27 | -17.26 | 547 |
| 30 | Daily: Bullish score | daily | 90.93 | -9.07 | 7 | 0.0 | -7.59 | -0.84 | -13.10 | 13 |
| 31 | Parabolic SAR · 1h | trend | 90.76 | -9.24 | 105 | 21.9 | -20.21 | -4.51 | -22.26 | 270 |
| 32 | Agent | meta | 90.71 | -9.29 | 87 | 40.2 | -11.84 | -4.03 | -17.54 | 252 |
| 33 | Bollinger breakout · 1h | breakout | 90.66 | -9.34 | 84 | 28.6 | -9.19 | -1.56 | -17.01 | 253 |
| 34 | EMA 20/50 cross · 1h | trend | 90.17 | -9.83 | 60 | 13.3 | -17.36 | -3.21 | -19.72 | 126 |
| 35 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.34 | -6.59 | -23.84 | 203 |
| 36 | RSI momentum · 1h | momentum | 89.27 | -10.73 | 82 | 15.9 | -22.87 | -4.52 | -23.53 | 211 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 88.53 | -11.47 | 0 | — | -1.29 | -0.04 | -14.37 | 1 |
| 38 | Ichimoku · 1h | trend | 88.49 | -11.51 | 57 | 14.0 | -17.74 | -3.35 | -18.21 | 114 |
| 39 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -13.10 | -3.77 | -14.88 | 133 |
| 40 | Keltner breakout · 1h | breakout | 87.60 | -12.40 | 56 | 23.2 | -17.16 | -2.88 | -27.42 | 194 |
| 41 | Stochastic reversion · 1h | reversion | 87.21 | -12.79 | 154 | 45.5 | -17.29 | -2.99 | -22.24 | 364 |
| 42 | Triple EMA stack · 1h | trend | 87.07 | -12.93 | 88 | 14.8 | -26.64 | -4.50 | -34.23 | 231 |
| 43 | Supertrend · 1h | trend | 86.94 | -13.06 | 88 | 12.5 | -23.56 | -4.73 | -27.35 | 212 |
| 44 | Opening range 15m | breakout | 86.58 | -13.42 | 256 | 25.8 | -19.30 | -5.40 | -20.98 | 691 |
| 45 | MACD cross · 1h | trend | 85.30 | -14.70 | 192 | 20.3 | -28.50 | -5.58 | -33.49 | 470 |
| 46 | OBV trend · 1h | momentum | 84.92 | -15.07 | 181 | 17.7 | -28.75 | -5.03 | -35.64 | 324 |
| 47 | MFI reversion · 1h | reversion | 84.29 | -15.71 | 210 | 31.0 | -15.81 | -2.49 | -20.43 | 139 |
| 48 | MACD zero-line · 1h | trend | 84.12 | -15.88 | 87 | 14.9 | -24.32 | -4.70 | -25.37 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 84.08 | -15.92 | 81 | 17.3 | -12.83 | -1.62 | -28.09 | 214 |
| 50 | Z-score reversion · 1h | reversion | 83.64 | -16.36 | 94 | 29.8 | -15.72 | -2.61 | -21.32 | 198 |
| 51 | Agent (ML meta-label) | meta | 83.08 | -16.93 | 687 | 18.9 | -13.43 | -2.52 | -18.02 | 371 |
| 52 | Bollinger reversion · 1h | reversion | 82.29 | -17.71 | 159 | 34.6 | -28.11 | -5.38 | -33.50 | 352 |
| 53 | Three white soldiers | momentum | 81.85 | -18.15 | 235 | 18.7 | -48.13 | -19.61 | -48.13 | 606 |
| 54 | ROC + volume · 1h | momentum | 81.28 | -18.72 | 197 | 20.8 | -25.73 | -4.40 | -33.84 | 383 |
| 55 | Williams %R · 1h | reversion | 81.01 | -18.99 | 186 | 41.9 | -33.94 | -5.42 | -36.49 | 532 |
| 56 | CCI reversion · 1h | reversion | 79.72 | -20.28 | 168 | 38.7 | -18.18 | -2.26 | -27.44 | 443 |
| 57 | EMA 9/21 cross · 1h | trend | 79.23 | -20.77 | 140 | 10.7 | -29.65 | -6.17 | -29.85 | 315 |
| 58 | Heikin-Ashi · 1h | trend | 79.03 | -20.97 | 228 | 21.1 | -41.26 | -8.91 | -44.88 | 680 |
| 59 | RSI(14) reversion · 1h | reversion | 78.39 | -21.61 | 80 | 20.0 | -20.46 | -3.98 | -23.27 | 165 |
| 60 | Max aggression: 1-day momentum | meta | 77.93 | -22.07 | 16 | 31.2 | -26.73 | -1.46 | -39.19 | 42 |
| 61 | VWAP momentum · 1h | momentum | 77.72 | -22.28 | 437 | 20.6 | -42.42 | -7.10 | -48.96 | 1245 |
| 62 | Candlestick reversal · 1h | reversion | 75.60 | -24.40 | 216 | 27.3 | -37.12 | -6.93 | -39.03 | 525 |
| 63 | ROC + volume | momentum | 61.79 | -38.21 | 599 | 22.2 | -77.13 | -19.93 | -78.70 | 1725 |
| 64 | Volume breakout | breakout | 61.09 | -38.91 | 364 | 12.9 | -63.40 | -19.20 | -64.20 | 861 |
| 65 | Squeeze breakout | breakout | 58.78 | -41.22 | 481 | 13.7 | -64.08 | -18.86 | -66.50 | 1210 |
| 66 | Donchian 55/20 | breakout | 57.48 | -42.52 | 487 | 18.1 | -70.24 | -16.78 | -73.52 | 1277 |
| 67 | RSI(14) reversion | reversion | 56.86 | -43.14 | 723 | 24.9 | -74.63 | -16.47 | -74.98 | 1620 |
| 68 | EMA 20/50 cross | trend | 55.38 | -44.62 | 525 | 19.4 | -77.73 | -16.69 | -80.87 | 1430 |
| 69 | VWAP reversion | reversion | 53.62 | -46.38 | 751 | 25.2 | -71.56 | -14.57 | -72.28 | 1490 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -29.84 | -98.76 | 5307 |
| 71 | Keltner breakout | breakout | 50.53 | -49.47 | 681 | 16.0 | -82.95 | -26.39 | -83.82 | 1795 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -31.00 | -93.89 | 2571 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.85 | -20.88 | -88.38 | 1891 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.31 | -24.50 | -91.32 | 2350 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.95 | -25.49 | -91.20 | 2252 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.52 | -32.50 | -97.64 | 3494 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.72 | -35.98 | -96.87 | 3584 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -28.21 | -94.50 | 2506 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.13 | -24.76 | -83.09 | 1690 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.15 | -99.38 | 5759 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.50 | -26.46 | -92.18 | 2623 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.90 | -31.12 | -95.90 | 3439 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -39.82 | -99.76 | 6193 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.61 | -29.07 | -91.67 | 2335 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -37.55 | -97.71 | 3628 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.42 | -98.49 | 4704 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.94 | -33.24 | -94.15 | 2791 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.85 | -99.53 | 6175 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.97 | -22.51 | -87.09 | 2152 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.15 | -26.82 | -88.32 | 2136 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -32.50 | -95.98 | 3768 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.05 | -32.51 | -89.26 | 2110 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -33.48 | -95.84 | 4113 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.39 | -99.90 | 8261 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T13:56 | Day trade: Stocks in Play ORB | sell | TNA | 24.83 | 0.26 | target is flat |
| 2026-10-20T13:56 | Day trade: Stocks in Play ORB | sell | SQQQ | 24.47 | -0.10 | target is flat |
| 2026-10-20T13:56 | Agent (ML meta-label) | sell | IWM | 6.92 | 0.01 | selected signal exited |
| 2026-10-20T13:56 | VWAP momentum · 1h | buy | TSLA | 4.47 | — | rebalance up |
| 2026-10-20T13:56 | VWAP momentum · 1h | buy | SQQQ | 4.13 | — | rebalance up |
| 2026-10-20T13:56 | VWAP momentum · 1h | buy | LABU | 4.01 | — | rebalance up |
| 2026-10-20T13:56 | VWAP momentum · 1h | buy | AMZN | 4.51 | — | rebalance up |
| 2026-10-20T13:56 | VWAP momentum · 1h | sell | PLTR | 10.93 | -0.22 | target is flat |
| 2026-10-20T13:50 | Day trade: Stocks in Play ORB | sell | COIN | 24.61 | 0.04 | target is flat |
| 2026-10-20T13:50 | Agent (ML meta-label) | buy | IWM | 6.92 | — | entry |
| 2026-10-20T13:50 | Agent | sell | ETHU | 18.21 | 0.08 | selected signal exited |
| 2026-10-20T13:50 | RSI(14) reversion | buy | UPRO | 4.05 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | buy | TQQQ | 4.06 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | buy | TECL | 4.06 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | buy | SOXL | 4.06 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | buy | QQQ | 4.06 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | buy | PLTR | 4.06 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | buy | MSFT | 4.06 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | buy | GOOGL | 4.06 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | buy | AMZN | 4.06 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | buy | AMD | 4.06 | — | entry signal |
| 2026-10-20T13:50 | RSI(14) reversion | sell | SPY | 7.29 | -0.00 | rebalance down |
| 2026-10-20T13:50 | RSI(14) reversion | sell | MSTR | 7.34 | 0.03 | rebalance down |
| 2026-10-20T13:50 | RSI(14) reversion | sell | COIN | 10.23 | 0.04 | rebalance down |
| 2026-10-20T13:50 | RSI(14) reversion | sell | BITX | 7.34 | 0.03 | rebalance down |
| 2026-10-20T13:50 | Volume breakout | buy | TNA | 15.23 | — | entry signal |
| 2026-10-20T13:50 | Volume breakout | buy | BTC-USD | 15.23 | — | entry signal |
| 2026-10-20T13:50 | Keltner breakout | buy | DOGE-USD | 7.61 | — | entry signal |
| 2026-10-20T13:50 | Keltner breakout | buy | BTC-USD | 10.08 | — | entry signal |
| 2026-10-20T13:50 | Keltner breakout | sell | TNA | 2.52 | 0.01 | rebalance down |
| 2026-10-20T13:50 | Keltner breakout | sell | LABU | 2.64 | 0.04 | rebalance down |
| 2026-10-20T13:50 | Opening range 15m | buy | UPRO | 10.80 | — | entry signal |
| 2026-10-20T13:50 | Opening range 15m | buy | TNA | 10.80 | — | entry signal |
| 2026-10-20T13:50 | Opening range 15m | buy | MSTR | 10.80 | — | entry signal |
| 2026-10-20T13:50 | Opening range 15m | buy | LABU | 10.80 | — | entry signal |
| 2026-10-20T13:50 | Opening range 15m | buy | IWM | 10.80 | — | entry signal |
| 2026-10-20T13:50 | Opening range 15m | buy | ETHU | 10.80 | — | entry signal |
| 2026-10-20T13:50 | Opening range 15m | buy | COIN | 10.80 | — | entry signal |
| 2026-10-20T13:50 | Opening range 15m | buy | BITX | 10.80 | — | entry signal |
| 2026-10-20T13:50 | Donchian 55/20 | buy | XRP-USD | 7.15 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 13:56:05.000137+00:00 -> 2026-10-20 14:06:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
