# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T16:56:05.000141+00:00 · 29727 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.98 (-9.03%)

Closed trades 87, win rate 40.2%, fees £2.92, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.54 | +0.27 |

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

Today: 26001 decisions in 2481 calls, $0.3261 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T16:56 | 4 / 15 / 11 | cash |  |
| Breezy | 2026-10-20T16:56 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-20T16:56 | 5 / 23 / 2 | COIN 78% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | BITX | 1.90 | +3.32% | 6 |
| VWAP reversion | ETHU | 1.90 | +4.27% | 5 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.56 | 5.56 | 0 | — | 7.01 | 3.34 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 101.76 | 1.76 | 9 | 44.4 | -12.39 | -0.83 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.92 | -1.08 | 0 | — | -0.18 | -0.06 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.88 | -1.12 | 59 | 35.6 | 2.36 | 1.35 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.72 | -1.28 | 0 | — | 0.14 | 0.14 | -5.15 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.05 | -1.95 | 3 | 33.3 | 3.70 | 0.88 | -7.93 | 8 |
| 14 | Hold BTC | benchmark | 97.77 | -2.23 | 0 | — | 20.86 | 2.75 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.24 | -2.76 | 0 | — | -3.70 | -1.38 | -7.04 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.99 | -2.26 | -5.83 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.97 | -3.03 | 0 | — | -0.05 | 0.04 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.30 | -3.70 | 40 | 15.0 | -16.96 | -3.39 | -21.99 | 103 |
| 19 | Agent (rotation) | meta | 96.16 | -3.84 | 114 | 31.6 | -7.44 | -3.39 | -9.02 | 312 |
| 20 | Trend pullback · 1h | trend | 95.66 | -4.34 | 90 | 23.3 | -20.33 | -6.09 | -20.75 | 133 |
| 21 | Copy: Insider buying | copy | 95.48 | -4.52 | 23 | 43.5 | -12.28 | -2.12 | -20.62 | 72 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.18 | -3.18 | -6.31 | 33 |
| 23 | ADX DI cross · 1h | trend | 94.57 | -5.43 | 89 | 18.0 | -11.77 | -2.14 | -15.39 | 255 |
| 24 | Daily: Momentum burst | daily | 94.51 | -5.49 | 6 | 16.7 | -6.67 | -0.88 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.29 | 1.37 | -6.51 | 198 |
| 26 | Opening range 30m | breakout | 92.32 | -7.68 | 208 | 29.3 | -13.22 | -3.83 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.76 | -8.24 | 105 | 21.9 | -18.49 | -3.97 | -22.26 | 274 |
| 28 | Squeeze breakout · 1h | breakout | 91.73 | -8.27 | 46 | 21.7 | -3.32 | -0.73 | -11.34 | 97 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 91.40 | -8.60 | 0 | — | 1.52 | 0.40 | -14.37 | 1 |
| 30 | Daily: Bullish score | daily | 91.37 | -8.63 | 7 | 0.0 | -6.84 | -0.74 | -13.10 | 13 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.72 | -2.42 | -16.91 | 1 |
| 32 | Agent | meta | 90.98 | -9.03 | 87 | 40.2 | -8.28 | -2.52 | -13.96 | 284 |
| 33 | Volume breakout · 1h | breakout | 90.61 | -9.39 | 84 | 22.6 | -12.56 | -2.26 | -15.57 | 107 |
| 34 | Bollinger breakout · 1h | breakout | 90.47 | -9.53 | 87 | 29.9 | -11.38 | -2.08 | -16.34 | 259 |
| 35 | Connors RSI(2) · 1h | reversion | 89.47 | -10.54 | 150 | 41.3 | -22.76 | -6.76 | -24.22 | 201 |
| 36 | RSI momentum · 1h | momentum | 89.11 | -10.89 | 83 | 15.7 | -21.01 | -4.18 | -26.37 | 215 |
| 37 | EMA 20/50 cross · 1h | trend | 88.86 | -11.14 | 62 | 12.9 | -18.95 | -3.50 | -21.33 | 131 |
| 38 | Opening range 15m | breakout | 88.45 | -11.55 | 256 | 25.8 | -17.75 | -4.74 | -20.98 | 700 |
| 39 | Supertrend · 1h | trend | 88.27 | -11.73 | 88 | 12.5 | -21.53 | -4.29 | -26.49 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 88.13 | -11.87 | 163 | 46.6 | -14.11 | -2.34 | -22.24 | 362 |
| 41 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -13.72 | -2.79 | -15.36 | 159 |
| 42 | Keltner breakout · 1h | breakout | 87.14 | -12.86 | 60 | 21.7 | -15.04 | -2.43 | -25.09 | 204 |
| 43 | Ichimoku · 1h | trend | 86.76 | -13.24 | 60 | 13.3 | -19.16 | -3.61 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.32 | -13.68 | 192 | 20.3 | -26.90 | -5.15 | -33.21 | 471 |
| 45 | Triple EMA stack · 1h | trend | 85.41 | -14.59 | 91 | 14.3 | -31.68 | -5.87 | -35.44 | 231 |
| 46 | Z-score reversion · 1h | reversion | 84.81 | -15.19 | 95 | 30.5 | -14.67 | -2.43 | -21.32 | 197 |
| 47 | Donchian 20/10 · 1h | breakout | 84.47 | -15.53 | 81 | 17.3 | -13.69 | -1.82 | -28.41 | 219 |
| 48 | MFI reversion · 1h | reversion | 84.26 | -15.74 | 213 | 31.0 | -15.04 | -2.34 | -20.43 | 146 |
| 49 | OBV trend · 1h | momentum | 84.02 | -15.98 | 186 | 17.2 | -30.02 | -5.30 | -36.99 | 319 |
| 50 | Agent (ML meta-label) | meta | 83.80 | -16.20 | 705 | 19.3 | -1.33 | -0.08 | -15.19 | 371 |
| 51 | MACD zero-line · 1h | trend | 83.53 | -16.47 | 89 | 14.6 | -25.42 | -5.05 | -26.37 | 224 |
| 52 | Three white soldiers | momentum | 82.67 | -17.33 | 249 | 19.7 | -46.56 | -17.74 | -47.79 | 615 |
| 53 | Bollinger reversion · 1h | reversion | 82.28 | -17.72 | 162 | 35.8 | -28.23 | -5.41 | -33.45 | 350 |
| 54 | Williams %R · 1h | reversion | 81.74 | -18.26 | 193 | 43.5 | -32.12 | -5.05 | -36.49 | 526 |
| 55 | ROC + volume · 1h | momentum | 81.47 | -18.53 | 199 | 21.6 | -26.35 | -4.57 | -34.31 | 396 |
| 56 | CCI reversion · 1h | reversion | 80.91 | -19.09 | 177 | 41.8 | -18.50 | -2.32 | -27.44 | 444 |
| 57 | Heikin-Ashi · 1h | trend | 80.47 | -19.53 | 229 | 21.0 | -41.11 | -8.64 | -45.69 | 680 |
| 58 | RSI(14) reversion · 1h | reversion | 79.89 | -20.11 | 83 | 22.9 | -15.40 | -2.79 | -23.28 | 175 |
| 59 | EMA 9/21 cross · 1h | trend | 79.42 | -20.58 | 143 | 10.5 | -29.49 | -6.15 | -30.19 | 323 |
| 60 | VWAP momentum · 1h | momentum | 77.90 | -22.10 | 447 | 20.6 | -42.47 | -6.91 | -50.36 | 1249 |
| 61 | Candlestick reversal · 1h | reversion | 77.33 | -22.67 | 220 | 28.2 | -33.49 | -5.93 | -36.93 | 544 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.05 | -1.55 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 62.04 | -37.95 | 619 | 23.3 | -76.99 | -19.57 | -78.74 | 1725 |
| 64 | Volume breakout | breakout | 61.70 | -38.30 | 376 | 14.1 | -63.18 | -18.80 | -64.29 | 872 |
| 65 | Squeeze breakout | breakout | 58.95 | -41.05 | 485 | 14.2 | -64.78 | -20.19 | -66.58 | 1206 |
| 66 | Donchian 55/20 | breakout | 58.37 | -41.63 | 491 | 18.3 | -70.60 | -17.69 | -73.50 | 1280 |
| 67 | RSI(14) reversion | reversion | 57.36 | -42.64 | 739 | 26.3 | -74.65 | -16.57 | -75.10 | 1634 |
| 68 | EMA 20/50 cross | trend | 56.05 | -43.95 | 534 | 19.1 | -77.15 | -16.21 | -80.87 | 1442 |
| 69 | VWAP reversion | reversion | 53.69 | -46.31 | 752 | 25.3 | -71.62 | -14.62 | -72.28 | 1502 |
| 70 | Keltner breakout | breakout | 50.70 | -49.30 | 700 | 16.9 | -82.56 | -25.08 | -83.82 | 1810 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -29.82 | -98.77 | 5335 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.73 | -32.98 | -93.86 | 2594 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.84 | -20.92 | -88.38 | 1902 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.40 | -25.10 | -91.32 | 2353 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.97 | -25.50 | -91.20 | 2249 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.57 | -33.31 | -97.64 | 3526 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.76 | -37.05 | -96.84 | 3598 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -27.87 | -94.42 | 2512 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.69 | -26.94 | -82.69 | 1690 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.87 | -99.38 | 5751 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.35 | -25.74 | -92.18 | 2621 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -31.38 | -95.93 | 3450 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -39.77 | -99.76 | 6198 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.51 | -28.71 | -91.65 | 2345 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -39.08 | -97.70 | 3611 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.43 | -98.50 | 4704 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.87 | -32.78 | -94.15 | 2804 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.58 | -99.52 | 6178 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.77 | -22.25 | -87.05 | 2150 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.77 | -26.05 | -88.17 | 2135 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.32 | -95.99 | 3761 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -32.53 | -89.30 | 2118 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.68 | -32.93 | -95.83 | 4104 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.05 | -99.90 | 8269 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T16:56 | EMA 20/50 cross | sell | TQQQ | 4.64 | -0.03 | exit signal |
| 2026-10-20T16:50 | Donchian 55/20 · 1h | buy | AMZN | 4.82 | — | rebalance up |
| 2026-10-20T16:50 | ROC + volume | buy | XRP-USD | 15.59 | — | entry signal |
| 2026-10-20T16:50 | ROC + volume | buy | SOL-USD | 15.59 | — | entry signal |
| 2026-10-20T16:50 | ROC + volume | buy | ETH-USD | 15.59 | — | entry signal |
| 2026-10-20T16:50 | ROC + volume | buy | DOGE-USD | 15.59 | — | entry signal |
| 2026-10-20T16:41 | EMA 20/50 cross | buy | NVDA | 4.31 | — | entry signal |
| 2026-10-20T16:35 | Agent (ML meta-label) | buy | QQQ | 7.40 | — | entry |
| 2026-10-20T16:35 | EMA 20/50 cross | buy | TQQQ | 4.67 | — | entry signal |
| 2026-10-20T16:30 | Agent (ML meta-label) | sell | QQQ | 5.41 | -0.00 | selected signal exited |
| 2026-10-20T16:30 | Agent (ML meta-label) | sell | COIN | 1.99 | -0.00 | selected signal exited |
| 2026-10-20T16:30 | Bollinger reversion · 1h | buy | AAPL | 20.57 | — | entry signal |
| 2026-10-20T16:30 | VWAP momentum · 1h | sell | AMZN | 3.55 | -0.01 | exit signal |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | buy | TNA | 11.48 | — | entry signal |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | buy | MSTR | 11.48 | — | entry signal |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | buy | IWM | 11.48 | — | entry signal |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | sell | TSLA | 8.51 | 0.09 | rebalance down |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | sell | LABU | 4.59 | 0.40 | rebalance down |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | sell | BTC-USD | 4.56 | -0.03 | rebalance down |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | sell | AMZN | 19.50 | -0.06 | exit signal |
| 2026-10-20T16:30 | MACD zero-line · 1h | buy | IWM | 3.56 | — | entry signal |
| 2026-10-20T16:30 | MACD zero-line · 1h | buy | BITX | 11.91 | — | entry signal |
| 2026-10-20T16:30 | MACD zero-line · 1h | sell | LABU | 4.63 | -0.05 | rebalance down |
| 2026-10-20T16:30 | RSI(14) reversion | sell | MSFT | 14.41 | 0.02 | exit signal |
| 2026-10-20T16:25 | EMA 20/50 cross | buy | SQQQ | 5.08 | — | entry signal |
| 2026-10-20T16:25 | EMA 20/50 cross | sell | NVDA | 5.07 | -0.02 | exit signal |
| 2026-10-20T16:20 | Donchian 55/20 | buy | ETHU | 2.94 | — | rebalance up |
| 2026-10-20T16:20 | Donchian 55/20 | sell | TSLA | 3.89 | -0.01 | exit signal |
| 2026-10-20T16:15 | MFI reversion · 1h | buy | PLTR | 6.82 | — | entry |
| 2026-10-20T16:15 | Volume breakout · 1h | buy | LABU | 4.55 | — | rebalance up |
| 2026-10-20T16:15 | Three white soldiers | sell | TECL | 20.58 | -0.12 | target is flat |
| 2026-10-20T16:15 | Donchian 55/20 | sell | TNA | 3.93 | 0.08 | exit signal |
| 2026-10-20T16:15 | Donchian 55/20 | sell | IWM | 3.90 | 0.02 | exit signal |
| 2026-10-20T16:10 | Agent (ML meta-label) | buy | QQQ | 5.41 | — | entry |
| 2026-10-20T16:10 | Agent (ML meta-label) | buy | COIN | 1.99 | — | entry |
| 2026-10-20T16:10 | MFI reversion · 1h | buy | UPRO | 7.16 | — | rebalance up |
| 2026-10-20T16:10 | MFI reversion · 1h | sell | COIN | 13.98 | -0.18 | target is flat |
| 2026-10-20T16:10 | RSI(14) reversion | sell | GOOGL | 14.29 | -0.12 | stop-loss |
| 2026-10-20T16:10 | Keltner breakout | sell | LABU | 12.58 | -0.19 | exit signal |
| 2026-10-20T16:05 | Agent (ML meta-label) | sell | COIN | 7.00 | 0.01 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 16:56:05.000141+00:00 -> 2026-10-20 17:06:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
