# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T18:56:05.000168+00:00 · 29819 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.10 (-8.90%)

Closed trades 87, win rate 40.2%, fees £2.93, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.19 | -0.04 |
| TSLA | 36.70 | +0.42 |

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

Today: 34179 decisions in 2757 calls, $0.4216 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T18:56 | 11 / 15 / 3 | TNA 14%, ARKK 14% |  |
| Breezy | 2026-10-20T18:56 | 0 / 28 / 1 | cash |  |
| Boozy | 2026-10-20T18:56 | 7 / 21 / 1 | MSTR 72% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.50 | 5.50 | 0 | — | 7.33 | 3.52 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 100.79 | 0.79 | 9 | 44.4 | -13.20 | -0.92 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.97 | -1.02 | 0 | — | -0.06 | 0.01 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.89 | -1.11 | 59 | 35.6 | 4.45 | 2.29 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.59 | -1.41 | 0 | — | -0.02 | 0.07 | -5.15 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.20 | -1.79 | 3 | 33.3 | 4.13 | 0.96 | -7.93 | 8 |
| 14 | Hold BTC | benchmark | 97.51 | -2.49 | 0 | — | 20.15 | 2.67 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.92 | -2.21 | -5.83 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 97.05 | -2.95 | 0 | — | 0.31 | 0.19 | -5.31 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.01 | -2.99 | 0 | — | -4.14 | -1.58 | -7.04 | 1 |
| 18 | Agent (rotation) | meta | 96.12 | -3.88 | 114 | 31.6 | -6.41 | -2.98 | -8.21 | 307 |
| 19 | Donchian 55/20 · 1h | breakout | 96.10 | -3.90 | 40 | 15.0 | -18.46 | -3.64 | -22.00 | 103 |
| 20 | Trend pullback · 1h | trend | 95.60 | -4.40 | 90 | 23.3 | -20.47 | -6.12 | -20.86 | 133 |
| 21 | Copy: Insider buying | copy | 95.48 | -4.52 | 25 | 40.0 | -12.58 | -2.17 | -20.62 | 72 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.64 | -5.36 | 89 | 18.0 | -12.97 | -2.32 | -16.67 | 255 |
| 24 | Daily: Momentum burst | daily | 93.98 | -6.02 | 6 | 16.7 | -7.04 | -0.94 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.28 | 1.37 | -6.51 | 198 |
| 26 | Opening range 30m | breakout | 92.30 | -7.70 | 208 | 29.3 | -13.21 | -3.83 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.62 | -8.38 | 105 | 21.9 | -17.29 | -3.68 | -23.03 | 274 |
| 28 | Squeeze breakout · 1h | breakout | 91.43 | -8.57 | 46 | 21.7 | -3.80 | -0.86 | -11.39 | 98 |
| 29 | Daily: Bullish score | daily | 91.37 | -8.63 | 7 | 0.0 | -7.09 | -0.77 | -13.10 | 13 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.51 | -2.37 | -16.91 | 1 |
| 31 | Agent | meta | 91.10 | -8.90 | 87 | 40.2 | -6.44 | -2.22 | -15.20 | 226 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.98 | -9.02 | 0 | — | 0.62 | 0.26 | -14.37 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.83 | -9.17 | 84 | 22.6 | -12.25 | -2.19 | -15.57 | 108 |
| 34 | Bollinger breakout · 1h | breakout | 90.65 | -9.35 | 87 | 29.9 | -11.21 | -2.04 | -16.35 | 260 |
| 35 | Connors RSI(2) · 1h | reversion | 89.54 | -10.46 | 151 | 41.7 | -22.80 | -6.78 | -24.31 | 200 |
| 36 | RSI momentum · 1h | momentum | 89.20 | -10.80 | 83 | 15.7 | -20.91 | -4.15 | -26.34 | 216 |
| 37 | EMA 20/50 cross · 1h | trend | 88.64 | -11.36 | 62 | 12.9 | -19.31 | -3.67 | -21.51 | 130 |
| 38 | Opening range 15m | breakout | 88.43 | -11.56 | 256 | 25.8 | -17.75 | -4.74 | -20.98 | 700 |
| 39 | Supertrend · 1h | trend | 88.24 | -11.76 | 88 | 12.5 | -21.42 | -4.19 | -26.62 | 222 |
| 40 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -4.73 | -0.73 | -22.99 | 122 |
| 41 | Stochastic reversion · 1h | reversion | 87.98 | -12.02 | 164 | 47.0 | -14.36 | -2.39 | -22.24 | 362 |
| 42 | Keltner breakout · 1h | breakout | 87.43 | -12.57 | 60 | 21.7 | -15.89 | -2.55 | -26.10 | 206 |
| 43 | Ichimoku · 1h | trend | 86.93 | -13.06 | 60 | 13.3 | -18.99 | -3.58 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.38 | -13.62 | 193 | 20.2 | -27.56 | -5.32 | -33.68 | 469 |
| 45 | Triple EMA stack · 1h | trend | 85.19 | -14.80 | 91 | 14.3 | -31.19 | -5.76 | -35.15 | 228 |
| 46 | Z-score reversion · 1h | reversion | 84.66 | -15.34 | 95 | 30.5 | -14.09 | -2.31 | -21.32 | 195 |
| 47 | Donchian 20/10 · 1h | breakout | 84.52 | -15.48 | 81 | 17.3 | -13.82 | -1.84 | -28.46 | 219 |
| 48 | MFI reversion · 1h | reversion | 84.01 | -15.99 | 217 | 30.9 | -15.29 | -2.41 | -20.43 | 146 |
| 49 | Agent (ML meta-label) | meta | 83.86 | -16.14 | 710 | 19.2 | -3.65 | -0.47 | -16.62 | 383 |
| 50 | OBV trend · 1h | momentum | 83.74 | -16.26 | 186 | 17.2 | -30.05 | -5.19 | -37.21 | 321 |
| 51 | MACD zero-line · 1h | trend | 83.61 | -16.39 | 89 | 14.6 | -25.95 | -5.18 | -26.73 | 224 |
| 52 | Three white soldiers | momentum | 82.67 | -17.33 | 249 | 19.7 | -46.80 | -18.02 | -47.63 | 613 |
| 53 | Bollinger reversion · 1h | reversion | 82.25 | -17.75 | 162 | 35.8 | -29.20 | -5.67 | -32.82 | 348 |
| 54 | Williams %R · 1h | reversion | 81.50 | -18.50 | 194 | 43.8 | -30.79 | -4.79 | -36.49 | 525 |
| 55 | ROC + volume · 1h | momentum | 81.45 | -18.55 | 199 | 21.6 | -28.05 | -5.03 | -34.60 | 398 |
| 56 | CCI reversion · 1h | reversion | 80.78 | -19.22 | 177 | 41.8 | -18.32 | -2.28 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.52 | -19.48 | 229 | 21.0 | -42.24 | -8.77 | -47.32 | 673 |
| 58 | RSI(14) reversion · 1h | reversion | 79.81 | -20.19 | 83 | 22.9 | -13.63 | -2.37 | -23.28 | 172 |
| 59 | EMA 9/21 cross · 1h | trend | 79.57 | -20.43 | 143 | 10.5 | -29.41 | -6.11 | -30.22 | 326 |
| 60 | VWAP momentum · 1h | momentum | 77.77 | -22.23 | 456 | 20.2 | -44.29 | -7.73 | -50.49 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 77.29 | -22.71 | 226 | 28.8 | -34.51 | -6.17 | -37.04 | 547 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.20 | -1.56 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 61.64 | -38.36 | 627 | 23.1 | -77.35 | -20.71 | -78.61 | 1723 |
| 64 | Volume breakout | breakout | 61.59 | -38.41 | 377 | 14.1 | -63.43 | -18.77 | -64.54 | 880 |
| 65 | Squeeze breakout | breakout | 58.59 | -41.41 | 489 | 14.1 | -66.04 | -22.13 | -66.58 | 1203 |
| 66 | Donchian 55/20 | breakout | 58.05 | -41.95 | 501 | 19.0 | -70.38 | -17.37 | -73.50 | 1277 |
| 67 | RSI(14) reversion | reversion | 57.39 | -42.61 | 740 | 26.4 | -74.26 | -16.32 | -74.89 | 1620 |
| 68 | EMA 20/50 cross | trend | 55.75 | -44.25 | 544 | 18.8 | -77.02 | -15.91 | -80.87 | 1448 |
| 69 | VWAP reversion | reversion | 53.70 | -46.30 | 752 | 25.3 | -71.61 | -14.60 | -72.28 | 1500 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.73 | -30.27 | -98.78 | 5312 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.59 | -32.06 | -93.88 | 2598 |
| 72 | Keltner breakout | breakout | 50.49 | -49.51 | 702 | 16.8 | -83.10 | -27.00 | -83.82 | 1803 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.82 | -20.88 | -88.38 | 1901 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.37 | -24.97 | -91.32 | 2356 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.03 | -25.70 | -91.20 | 2250 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.55 | -33.03 | -97.64 | 3521 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -37.21 | -96.71 | 3572 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.34 | -27.66 | -94.49 | 2527 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.74 | -27.29 | -82.76 | 1707 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.81 | -99.38 | 5758 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.52 | -26.52 | -92.20 | 2624 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.95 | -31.58 | -95.95 | 3460 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -40.80 | -99.75 | 6191 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.58 | -29.02 | -91.63 | 2351 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -38.73 | -97.66 | 3615 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.17 | -98.48 | 4712 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.93 | -33.80 | -94.10 | 2799 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.58 | -99.52 | 6185 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.60 | -21.98 | -87.01 | 2140 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.79 | -26.11 | -88.16 | 2132 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -32.22 | -95.95 | 3767 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -32.47 | -89.33 | 2114 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -32.99 | -95.83 | 4118 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -42.91 | -99.90 | 8273 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T18:55 | Agent (ML meta-label) | sell | QQQ | 7.35 | -0.00 | selected signal exited |
| 2026-10-20T18:55 | MFI reversion · 1h | buy | META | 8.41 | — | entry |
| 2026-10-20T18:55 | EMA 20/50 cross | buy | TNA | 2.88 | — | rebalance up |
| 2026-10-20T18:55 | EMA 20/50 cross | buy | SOL-USD | 2.90 | — | rebalance up |
| 2026-10-20T18:55 | EMA 20/50 cross | buy | PLTR | 2.87 | — | rebalance up |
| 2026-10-20T18:55 | EMA 20/50 cross | buy | MSTR | 2.93 | — | rebalance up |
| 2026-10-20T18:55 | EMA 20/50 cross | buy | BTC-USD | 2.88 | — | rebalance up |
| 2026-10-20T18:55 | EMA 20/50 cross | buy | BITX | 2.92 | — | rebalance up |
| 2026-10-20T18:55 | EMA 20/50 cross | sell | UPRO | 3.18 | -0.02 | exit signal |
| 2026-10-20T18:55 | EMA 20/50 cross | sell | SPY | 3.34 | -0.01 | exit signal |
| 2026-10-20T18:50 | VWAP reversion | buy | GOOGL | 13.42 | — | entry signal |
| 2026-10-20T18:50 | RSI(14) reversion | buy | GOOGL | 14.34 | — | entry signal |
| 2026-10-20T18:50 | RSI(14) reversion | buy | COIN | 14.34 | — | entry signal |
| 2026-10-20T18:45 | Squeeze breakout | buy | SQQQ | 14.67 | — | entry signal |
| 2026-10-20T18:45 | Donchian 55/20 | buy | LABU | 4.84 | — | rebalance up |
| 2026-10-20T18:45 | Donchian 55/20 | buy | DOGE-USD | 4.83 | — | rebalance up |
| 2026-10-20T18:45 | Donchian 55/20 | sell | UPRO | 9.63 | -0.06 | exit signal |
| 2026-10-20T18:45 | Donchian 55/20 | sell | SPY | 9.69 | -0.03 | exit signal |
| 2026-10-20T18:45 | Donchian 55/20 | sell | BTC-USD | 9.66 | -0.04 | exit signal |
| 2026-10-20T18:45 | Donchian 55/20 | sell | BITX | 9.68 | 0.01 | exit signal |
| 2026-10-20T18:45 | ROC + volume | buy | SQQQ | 15.43 | — | entry signal |
| 2026-10-20T18:43 | Copy: Insider buying | buy | IAM | 10.87 | — | rebalance up |
| 2026-10-20T18:43 | Copy: Insider buying | sell | BBD | 10.87 | -1.30 | target is flat |
| 2026-10-20T18:40 | Agent (ML meta-label) | buy | QQQ | 7.36 | — | entry |
| 2026-10-20T18:40 | Agent | buy | ETHU | 18.22 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-20T18:40 | EMA 20/50 cross | sell | TECL | 3.98 | -0.03 | stop-loss |
| 2026-10-20T18:35 | Agent (ML meta-label) | sell | QQQ | 7.36 | -0.03 | selected signal exited |
| 2026-10-20T18:35 | Keltner breakout | sell | LABU | 12.50 | -0.16 | stop-loss |
| 2026-10-20T18:35 | ROC + volume | sell | LABU | 15.28 | -0.20 | stop-loss |
| 2026-10-20T18:35 | EMA 20/50 cross | buy | SQQQ | 4.65 | — | entry signal |
| 2026-10-20T18:35 | EMA 20/50 cross | sell | TQQQ | 1.54 | -0.01 | exit signal |
| 2026-10-20T18:35 | EMA 20/50 cross | sell | SOXL | 3.47 | -0.04 | exit signal |
| 2026-10-20T18:35 | EMA 20/50 cross | sell | QQQ | 2.44 | -0.01 | exit signal |
| 2026-10-20T18:35 | EMA 20/50 cross | sell | NVDA | 4.30 | -0.02 | exit signal |
| 2026-10-20T18:35 | EMA 20/50 cross | sell | MSFT | 4.66 | -0.02 | stop-loss |
| 2026-10-20T18:30 | Day trade: Stocks in Play ORB | buy | LABU | 24.73 | — | entry |
| 2026-10-20T18:30 | MFI reversion · 1h | buy | QQQ | 4.79 | — | rebalance up |
| 2026-10-20T18:30 | MFI reversion · 1h | buy | ETH-USD | 4.74 | — | rebalance up |
| 2026-10-20T18:30 | MFI reversion · 1h | sell | TNA | 11.21 | 0.01 | target is flat |
| 2026-10-20T18:30 | Candlestick reversal · 1h | buy | SPY | 7.19 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 18:56:05.000168+00:00 -> 2026-10-20 19:06:05.000168+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
