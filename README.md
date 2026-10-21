# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T15:22:05.000145+00:00 · 30815 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.65 (-9.35%)

Closed trades 91, win rate 40.7%, fees £3.00, max drawdown -9.99%.

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

Today: 16737 decisions in 2208 calls, $0.2181 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T15:22 | 4 / 18 / 8 | cash |  |
| Breezy | 2026-10-21T15:22 | 0 / 30 / 0 | cash |  |
| Boozy | 2026-10-21T15:22 | 5 / 23 / 2 | MSTR 72% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.34 | 6.34 | 0 | — | 8.54 | 3.97 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 4 | Max aggression: 5-day momentum | meta | 104.61 | 4.61 | 10 | 50.0 | -4.50 | -0.08 | -34.64 | 26 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold BTC | benchmark | 99.65 | -0.35 | 0 | — | 16.32 | 2.32 | -8.68 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.59 | -0.41 | 4 | 50.0 | 7.76 | 1.68 | -7.93 | 8 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.55 | -0.45 | 0 | — | 0.62 | 0.34 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.15 | -0.85 | 0 | — | 0.61 | 0.40 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 98.97 | -1.03 | 63 | 34.9 | 2.37 | 1.40 | -2.29 | 64 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Copy: Insider buying | copy | 97.30 | -2.70 | 25 | 40.0 | -10.84 | -1.82 | -20.62 | 72 |
| 16 | Copy: Congress Democrats (NANC) | copy | 97.14 | -2.86 | 0 | — | 0.69 | 0.35 | -5.31 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.30 | -1.88 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.86 | -3.14 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 19 | Agent (rotation) | meta | 96.43 | -3.57 | 114 | 31.6 | -6.26 | -3.44 | -8.02 | 302 |
| 20 | Donchian 55/20 · 1h | breakout | 96.29 | -3.71 | 40 | 15.0 | -14.11 | -2.82 | -15.92 | 101 |
| 21 | ADX DI cross · 1h | trend | 95.84 | -4.16 | 90 | 18.9 | -11.64 | -1.99 | -17.56 | 257 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | Daily: Momentum burst | daily | 95.35 | -4.65 | 6 | 16.7 | -8.94 | -1.30 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 95.35 | -4.65 | 91 | 24.2 | -19.52 | -5.92 | -19.73 | 130 |
| 25 | Gap and go | momentum | 93.79 | -6.21 | 84 | 16.7 | 5.10 | 1.61 | -7.13 | 207 |
| 26 | Squeeze breakout · 1h | breakout | 93.53 | -6.47 | 46 | 21.7 | -0.92 | -0.12 | -11.48 | 97 |
| 27 | Parabolic SAR · 1h | trend | 93.41 | -6.59 | 108 | 23.1 | -15.73 | -3.37 | -19.76 | 273 |
| 28 | Opening range 30m | breakout | 93.02 | -6.98 | 225 | 32.4 | -11.26 | -3.22 | -17.26 | 565 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 92.98 | -7.02 | 0 | — | 2.59 | 0.56 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.47 | -7.53 | 87 | 29.9 | -8.39 | -1.49 | -16.72 | 257 |
| 31 | Daily: Bullish score | daily | 91.65 | -8.35 | 8 | 0.0 | -4.75 | -0.47 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.79 | -2.04 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.99 | -9.01 | 88 | 23.9 | -13.17 | -2.36 | -14.67 | 109 |
| 34 | Agent | meta | 90.65 | -9.35 | 91 | 40.7 | -14.16 | -6.93 | -15.02 | 257 |
| 35 | Supertrend · 1h | trend | 90.19 | -9.81 | 88 | 12.5 | -21.61 | -4.17 | -27.01 | 222 |
| 36 | RSI momentum · 1h | momentum | 90.10 | -9.90 | 83 | 15.7 | -20.80 | -4.17 | -22.75 | 217 |
| 37 | Connors RSI(2) · 1h | reversion | 89.91 | -10.09 | 157 | 42.0 | -21.63 | -6.39 | -23.42 | 196 |
| 38 | EMA 20/50 cross · 1h | trend | 89.39 | -10.61 | 62 | 12.9 | -20.22 | -3.56 | -23.33 | 135 |
| 39 | Stochastic reversion · 1h | reversion | 89.12 | -10.88 | 167 | 47.3 | -12.92 | -2.08 | -22.24 | 362 |
| 40 | Keltner breakout · 1h | breakout | 88.34 | -11.66 | 61 | 23.0 | -20.20 | -3.82 | -27.82 | 205 |
| 41 | Opening range 15m | breakout | 87.96 | -12.04 | 273 | 28.9 | -16.75 | -4.51 | -19.78 | 702 |
| 42 | Agent (aggressive) | meta | 87.59 | -12.41 | 45 | 35.6 | -13.24 | -3.88 | -15.64 | 121 |
| 43 | Ichimoku · 1h | trend | 87.53 | -12.47 | 60 | 13.3 | -17.94 | -3.35 | -20.25 | 117 |
| 44 | MACD cross · 1h | trend | 87.51 | -12.49 | 199 | 21.1 | -25.78 | -4.89 | -28.88 | 472 |
| 45 | Z-score reversion · 1h | reversion | 86.30 | -13.70 | 97 | 30.9 | -12.13 | -1.90 | -21.32 | 195 |
| 46 | Donchian 20/10 · 1h | breakout | 86.18 | -13.82 | 82 | 18.3 | -19.87 | -3.65 | -29.14 | 221 |
| 47 | Triple EMA stack · 1h | trend | 85.92 | -14.09 | 91 | 14.3 | -27.95 | -5.09 | -29.74 | 218 |
| 48 | MFI reversion · 1h | reversion | 85.14 | -14.86 | 227 | 32.6 | -14.37 | -2.18 | -21.11 | 139 |
| 49 | Agent (ML meta-label) | meta | 84.87 | -15.13 | 716 | 19.4 | -6.53 | -0.99 | -15.70 | 373 |
| 50 | MACD zero-line · 1h | trend | 84.58 | -15.42 | 92 | 15.2 | -25.06 | -4.78 | -27.46 | 220 |
| 51 | OBV trend · 1h | momentum | 84.39 | -15.61 | 188 | 17.6 | -30.51 | -5.71 | -31.73 | 312 |
| 52 | ROC + volume · 1h | momentum | 83.06 | -16.93 | 211 | 23.7 | -26.93 | -4.89 | -33.56 | 388 |
| 53 | Three white soldiers | momentum | 82.52 | -17.48 | 253 | 19.8 | -46.20 | -17.99 | -47.14 | 611 |
| 54 | Bollinger reversion · 1h | reversion | 82.45 | -17.55 | 162 | 35.8 | -29.22 | -5.65 | -32.84 | 347 |
| 55 | Williams %R · 1h | reversion | 82.40 | -17.60 | 196 | 43.9 | -29.47 | -4.47 | -36.50 | 523 |
| 56 | CCI reversion · 1h | reversion | 81.82 | -18.18 | 181 | 42.0 | -17.80 | -2.22 | -27.44 | 441 |
| 57 | Heikin-Ashi · 1h | trend | 81.44 | -18.56 | 235 | 20.9 | -44.11 | -9.48 | -47.30 | 673 |
| 58 | EMA 9/21 cross · 1h | trend | 81.13 | -18.88 | 143 | 10.5 | -27.37 | -5.44 | -29.91 | 326 |
| 59 | RSI(14) reversion · 1h | reversion | 80.81 | -19.19 | 84 | 23.8 | -16.74 | -3.01 | -23.40 | 173 |
| 60 | VWAP momentum · 1h | momentum | 78.90 | -21.10 | 471 | 21.0 | -45.07 | -8.13 | -51.76 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 78.64 | -21.36 | 227 | 29.1 | -33.88 | -5.78 | -37.34 | 543 |
| 62 | Max aggression: 1-day momentum | meta | 75.75 | -24.25 | 17 | 29.4 | -35.40 | -2.24 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 60.13 | -39.87 | 654 | 22.8 | -78.05 | -22.07 | -79.05 | 1721 |
| 64 | Volume breakout | breakout | 59.54 | -40.46 | 391 | 13.6 | -64.71 | -20.25 | -64.97 | 863 |
| 65 | RSI(14) reversion | reversion | 57.09 | -42.91 | 749 | 26.6 | -74.22 | -16.28 | -74.89 | 1634 |
| 66 | Squeeze breakout | breakout | 56.59 | -43.41 | 512 | 13.7 | -66.84 | -22.52 | -67.80 | 1214 |
| 67 | Donchian 55/20 | breakout | 56.57 | -43.43 | 521 | 18.6 | -71.67 | -18.60 | -74.04 | 1295 |
| 68 | EMA 20/50 cross | trend | 55.37 | -44.62 | 563 | 19.5 | -78.11 | -17.44 | -80.87 | 1454 |
| 69 | VWAP reversion | reversion | 53.91 | -46.09 | 759 | 25.4 | -71.03 | -14.27 | -72.15 | 1472 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.78 | -31.24 | -98.80 | 5332 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.92 | -33.51 | -94.24 | 2606 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.50 | -22.00 | -88.67 | 1907 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.90 | -26.18 | -91.71 | 2374 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.38 | -26.24 | -91.61 | 2270 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.65 | -34.01 | -97.77 | 3526 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -38.17 | -96.99 | 3617 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.50 | -28.07 | -94.71 | 2548 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.80 | -27.59 | -83.33 | 1734 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.12 | -99.38 | 5742 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.04 | -28.15 | -92.66 | 2635 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.95 | -31.63 | -95.97 | 3452 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.73 | -99.76 | 6192 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.70 | -29.52 | -91.89 | 2355 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -39.56 | -97.78 | 3619 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.20 | -98.48 | 4706 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.28 | -35.76 | -94.43 | 2807 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.68 | -28.38 | -84.44 | 1810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.19 | -99.53 | 6167 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.72 | -22.19 | -87.01 | 2141 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.70 | -25.92 | -88.05 | 2141 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -32.77 | -95.93 | 3764 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -33.70 | -89.40 | 2113 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.76 | -33.60 | -95.77 | 4095 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.40 | -99.91 | 8301 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T15:20 | Volume breakout | sell | XRP-USD | 14.74 | -0.21 | exit signal |
| 2026-10-21T15:15 | Volume breakout · 1h | buy | XRP-USD | 4.56 | — | rebalance up |
| 2026-10-21T15:15 | Volume breakout · 1h | sell | TSLA | 4.56 | 0.01 | rebalance down |
| 2026-10-21T15:15 | VWAP reversion | sell | GOOGL | 13.47 | 0.04 | exit signal |
| 2026-10-21T15:10 | Volume breakout | buy | ETH-USD | 14.94 | — | entry signal |
| 2026-10-21T15:05 | Agent (ML meta-label) | buy | AMZN | 2.79 | — | entry |
| 2026-10-21T15:05 | ROC + volume | buy | BTC-USD | 8.56 | — | entry |
| 2026-10-21T15:05 | ROC + volume | sell | META | 8.56 | 0.02 | exit signal |
| 2026-10-21T15:00 | Agent (ML meta-label) | sell | IWM | 2.79 | -0.01 | selected signal exited |
| 2026-10-21T15:00 | Volume breakout · 1h | buy | XRP-USD | 9.33 | — | entry signal |
| 2026-10-21T15:00 | Volume breakout · 1h | sell | ETH-USD | 4.65 | 0.02 | rebalance down |
| 2026-10-21T15:00 | Volume breakout · 1h | sell | BTC-USD | 4.64 | 0.02 | rebalance down |
| 2026-10-21T15:00 | Keltner breakout · 1h | buy | XRP-USD | 8.45 | — | entry |
| 2026-10-21T15:00 | Keltner breakout · 1h | buy | ETH-USD | 9.85 | — | entry signal |
| 2026-10-21T15:00 | Keltner breakout · 1h | buy | DOGE-USD | 6.49 | — | rebalance up |
| 2026-10-21T15:00 | Keltner breakout · 1h | sell | TSLA | 5.12 | 0.14 | rebalance down |
| 2026-10-21T15:00 | Keltner breakout · 1h | sell | TNA | 4.85 | 0.04 | rebalance down |
| 2026-10-21T15:00 | Keltner breakout · 1h | sell | LABU | 5.00 | 0.19 | rebalance down |
| 2026-10-21T15:00 | Keltner breakout · 1h | sell | IWM | 4.76 | 0.01 | rebalance down |
| 2026-10-21T15:00 | Keltner breakout · 1h | sell | BTC-USD | 5.06 | 0.07 | rebalance down |
| 2026-10-21T15:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 15.29 | — | entry signal |
| 2026-10-21T15:00 | Donchian 55/20 · 1h | sell | SQQQ | 7.47 | 0.08 | rebalance down |
| 2026-10-21T15:00 | Donchian 55/20 · 1h | sell | AMZN | 7.82 | -0.08 | rebalance down |
| 2026-10-21T15:00 | ROC + volume · 1h | buy | DOGE-USD | 2.03 | — | entry signal |
| 2026-10-21T15:00 | RSI(14) reversion | sell | SQQQ | 14.17 | -0.16 | stop-loss |
| 2026-10-21T15:00 | RSI(14) reversion | sell | AMZN | 14.34 | 0.07 | exit signal |
| 2026-10-21T15:00 | Gap and go | buy | TQQQ | 6.47 | — | rebalance up |
| 2026-10-21T15:00 | Gap and go | sell | TNA | 15.49 | -0.11 | exit signal |
| 2026-10-21T14:56 | Agent (ML meta-label) | buy | IWM | 2.80 | — | entry |
| 2026-10-21T14:56 | Agent (ML meta-label) | sell | AMZN | 2.80 | 0.00 | selected signal exited |
| 2026-10-21T14:56 | Three white soldiers | buy | AAPL | 20.60 | — | entry signal |
| 2026-10-21T14:56 | Volume breakout | buy | XRP-USD | 14.95 | — | entry signal |
| 2026-10-21T14:56 | Volume breakout | buy | AAPL | 14.95 | — | entry signal |
| 2026-10-21T14:56 | Opening range 15m | buy | TQQQ | 4.90 | — | rebalance up |
| 2026-10-21T14:56 | Opening range 15m | buy | AAPL | 9.76 | — | entry signal |
| 2026-10-21T14:56 | Opening range 15m | sell | PLTR | 4.83 | -0.00 | rebalance down |
| 2026-10-21T14:56 | Opening range 15m | sell | MSTR | 4.99 | 0.11 | rebalance down |
| 2026-10-21T14:56 | Opening range 15m | sell | COIN | 4.84 | 0.01 | rebalance down |
| 2026-10-21T14:56 | Donchian 55/20 | buy | AAPL | 2.91 | — | entry signal |
| 2026-10-21T14:56 | Donchian 55/20 | sell | BTC-USD | 2.91 | 0.00 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 15:22:05.000145+00:00 -> 2026-10-21 15:32:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
