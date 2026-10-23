# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T15:15:05.000117+00:00 · 33195 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.68 (-10.31%)

Closed trades 99, win rate 39.4%, fees £3.16, max drawdown -10.73%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 18399 decisions in 2352 calls, $0.2386 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T15:15 | 0 / 14 / 16 | cash |  |
| Breezy | 2026-10-23T15:15 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-23T15:15 | 2 / 25 / 3 | COIN 52% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| Stochastic reversion | BITX | 1.69 | +8.43% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.01 | 7.01 | 0 | — | 8.50 | 4.55 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.19 | 4.19 | 16 | 50.0 | 6.84 | 2.28 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.53 | -3.20 | -13.74 | 153 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.77 | 0.77 | 0 | — | 3.39 | 1.60 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.22 | -0.78 | 72 | 33.3 | 5.36 | 2.63 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 98.13 | -1.87 | 0 | — | -0.42 | -0.21 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.32 | -3.68 | 118 | 31.4 | -2.12 | -1.25 | -6.22 | 194 |
| 14 | Hold BTC | benchmark | 96.30 | -3.71 | 0 | — | 1.28 | 0.39 | -8.68 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.90 | -4.10 | 0 | — | -0.67 | -0.22 | -5.99 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Insider buying | copy | 94.60 | -5.40 | 25 | 40.0 | -14.46 | -2.75 | -20.68 | 71 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 94.49 | -5.51 | 0 | — | -6.56 | -2.78 | -7.76 | 1 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.76 | 1.60 | -8.69 | 184 |
| 21 | Trend pullback · 1h | trend | 93.75 | -6.25 | 95 | 23.2 | -21.56 | -7.08 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.71 | -6.29 | 238 | 35.3 | -10.43 | -3.24 | -17.21 | 559 |
| 23 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -15.97 | -1.49 | -27.80 | 24 |
| 24 | Donchian 55/20 · 1h | breakout | 92.88 | -7.12 | 48 | 16.7 | -16.33 | -3.71 | -17.44 | 98 |
| 25 | Parabolic SAR · 1h | trend | 91.87 | -8.13 | 117 | 25.6 | -21.10 | -5.01 | -24.17 | 254 |
| 26 | Daily: Momentum burst | daily | 91.37 | -8.63 | 10 | 10.0 | -17.91 | -3.48 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.96 | -9.04 | 108 | 18.5 | -11.87 | -2.44 | -14.53 | 255 |
| 30 | Agent | meta | 89.68 | -10.31 | 99 | 39.4 | -10.58 | -7.43 | -11.31 | 203 |
| 31 | Daily: Bullish score | daily | 89.66 | -10.34 | 9 | 0.0 | -7.87 | -1.02 | -14.40 | 14 |
| 32 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 88.90 | -11.10 | 0 | — | -5.58 | -0.82 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.77 | -11.23 | 105 | 27.6 | -12.47 | -2.48 | -16.55 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.83 | -12.17 | 186 | 45.2 | -19.80 | -3.74 | -22.47 | 383 |
| 36 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -12.23 | -4.22 | -15.12 | 94 |
| 37 | Opening range 15m | breakout | 86.68 | -13.32 | 305 | 30.2 | -15.49 | -4.51 | -17.87 | 701 |
| 38 | EMA 20/50 cross · 1h | trend | 86.28 | -13.72 | 71 | 11.3 | -22.70 | -4.54 | -25.07 | 137 |
| 39 | Keltner breakout · 1h | breakout | 86.06 | -13.94 | 73 | 23.3 | -22.91 | -4.88 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 85.96 | -14.04 | 108 | 14.8 | -23.83 | -5.04 | -26.46 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.37 | -14.63 | 101 | 15.8 | -21.70 | -4.66 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.15 | -14.85 | 170 | 39.4 | -26.53 | -8.15 | -27.06 | 195 |
| 43 | MACD cross · 1h | trend | 84.91 | -15.09 | 216 | 23.1 | -22.81 | -4.57 | -26.15 | 451 |
| 44 | Z-score reversion · 1h | reversion | 84.17 | -15.83 | 106 | 34.0 | -14.52 | -2.45 | -21.48 | 193 |
| 45 | Triple EMA stack · 1h | trend | 83.74 | -16.26 | 98 | 15.3 | -26.00 | -5.21 | -28.44 | 210 |
| 46 | Ichimoku · 1h | trend | 83.67 | -16.32 | 65 | 12.3 | -23.93 | -5.01 | -25.68 | 110 |
| 47 | MFI reversion · 1h | reversion | 82.26 | -17.73 | 256 | 31.6 | -17.33 | -2.83 | -20.54 | 141 |
| 48 | MACD zero-line · 1h | trend | 82.14 | -17.86 | 103 | 15.5 | -21.18 | -4.44 | -24.81 | 217 |
| 49 | Three white soldiers | momentum | 81.40 | -18.59 | 272 | 20.2 | -43.48 | -21.08 | -43.62 | 588 |
| 50 | Williams %R · 1h | reversion | 81.37 | -18.63 | 213 | 44.1 | -35.14 | -6.31 | -36.69 | 514 |
| 51 | OBV trend · 1h | momentum | 81.25 | -18.75 | 201 | 17.4 | -31.43 | -6.96 | -33.00 | 302 |
| 52 | Donchian 20/10 · 1h | breakout | 81.24 | -18.76 | 96 | 19.8 | -24.51 | -4.78 | -27.43 | 217 |
| 53 | Bollinger reversion · 1h | reversion | 80.59 | -19.41 | 171 | 34.5 | -30.81 | -6.42 | -32.19 | 356 |
| 54 | CCI reversion · 1h | reversion | 80.54 | -19.46 | 198 | 42.9 | -26.15 | -3.93 | -28.17 | 437 |
| 55 | Agent (ML meta-label) | meta | 80.15 | -19.85 | 841 | 18.8 | -11.97 | -2.23 | -15.66 | 368 |
| 56 | Heikin-Ashi · 1h | trend | 79.69 | -20.32 | 262 | 23.3 | -42.49 | -9.94 | -43.38 | 646 |
| 57 | ROC + volume · 1h | momentum | 78.26 | -21.74 | 239 | 23.8 | -30.85 | -6.20 | -31.99 | 379 |
| 58 | RSI(14) reversion · 1h | reversion | 78.13 | -21.87 | 91 | 23.1 | -14.87 | -2.74 | -23.51 | 185 |
| 59 | Candlestick reversal · 1h | reversion | 77.70 | -22.30 | 252 | 29.0 | -34.56 | -6.54 | -36.06 | 535 |
| 60 | EMA 9/21 cross · 1h | trend | 77.22 | -22.78 | 158 | 12.0 | -30.07 | -6.19 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 76.38 | -23.62 | 504 | 21.6 | -49.91 | -11.64 | -50.26 | 1196 |
| 62 | Max aggression: 1-day momentum | meta | 66.64 | -33.36 | 18 | 27.8 | -43.12 | -3.04 | -50.31 | 42 |
| 63 | ROC + volume | momentum | 57.87 | -42.13 | 700 | 22.9 | -75.20 | -27.62 | -75.26 | 1549 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -60.73 | -26.30 | -60.73 | 761 |
| 65 | Squeeze breakout | breakout | 53.97 | -46.03 | 545 | 14.1 | -66.00 | -28.81 | -66.19 | 1138 |
| 66 | Donchian 55/20 | breakout | 53.56 | -46.44 | 558 | 19.4 | -71.31 | -23.89 | -71.45 | 1250 |
| 67 | RSI(14) reversion | reversion | 53.06 | -46.94 | 817 | 26.2 | -76.51 | -19.76 | -76.81 | 1664 |
| 68 | EMA 20/50 cross | trend | 52.18 | -47.82 | 605 | 20.3 | -78.67 | -23.90 | -78.96 | 1398 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -45.20 | -98.66 | 4986 |
| 70 | VWAP reversion | reversion | 50.58 | -49.42 | 812 | 25.0 | -74.63 | -17.58 | -74.78 | 1540 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.67 | -48.29 | -93.71 | 2486 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.27 | -30.21 | -88.50 | 1870 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.04 | -38.43 | -91.13 | 2295 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.23 | -31.53 | -90.26 | 2134 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.58 | -54.31 | -97.62 | 3415 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.92 | -62.97 | -95.94 | 3302 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -35.55 | -93.73 | 2422 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.47 | -36.48 | -82.51 | 1665 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -54.45 | -99.31 | 5623 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.10 | -42.14 | -92.20 | 2562 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.26 | -40.60 | -95.27 | 3341 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.95 | -99.74 | 6028 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -45.97 | -91.85 | 2287 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -66.48 | -97.48 | 3492 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.43 | -58.86 | -98.45 | 4674 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.13 | -60.18 | -94.15 | 2719 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.56 | -39.96 | -83.62 | 1766 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -65.24 | -99.52 | 6107 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.54 | -28.90 | -87.65 | 2173 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.94 | -37.95 | -90.05 | 2211 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -47.11 | -95.87 | 3715 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.24 | -50.44 | -89.33 | 2075 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.99 | -47.80 | -96.06 | 4083 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -112.12 | -99.90 | 8075 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T15:10 | Volume breakout | sell | TQQQ | 14.22 | -0.07 | exit signal |
| 2026-10-23T15:10 | ROC + volume | buy | TSLA | 14.48 | — | entry signal |
| 2026-10-23T15:05 | VWAP reversion | buy | SQQQ | 12.64 | — | entry signal |
| 2026-10-23T15:05 | RSI(14) reversion | buy | XRP-USD | 3.12 | — | rebalance up |
| 2026-10-23T15:05 | RSI(14) reversion | buy | LABU | 2.98 | — | rebalance up |
| 2026-10-23T15:05 | RSI(14) reversion | buy | DOGE-USD | 3.07 | — | rebalance up |
| 2026-10-23T15:05 | RSI(14) reversion | buy | COIN | 3.02 | — | rebalance up |
| 2026-10-23T15:05 | RSI(14) reversion | buy | BTC-USD | 3.08 | — | rebalance up |
| 2026-10-23T15:05 | RSI(14) reversion | sell | TSLA | 7.60 | 0.10 | exit signal |
| 2026-10-23T15:05 | Three white soldiers | sell | COIN | 20.24 | -0.16 | exit signal |
| 2026-10-23T15:05 | Gap and go | sell | ETHU | 23.32 | -0.22 | exit signal |
| 2026-10-23T15:05 | EMA 20/50 cross | buy | MSFT | 7.45 | — | entry signal |
| 2026-10-23T15:05 | EMA 20/50 cross | sell | BTC-USD | 7.45 | -0.07 | exit signal |
| 2026-10-23T15:00 | Agent (rotation) | buy | TQQQ | 32.19 | — | entry |
| 2026-10-23T15:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 104.90 | — | entry |
| 2026-10-23T15:00 | Agent (ML meta-label) | buy | ETH-USD | 4.24 | — | entry |
| 2026-10-23T15:00 | VWAP momentum · 1h | sell | XRP-USD | 10.86 | -0.04 | exit signal |
| 2026-10-23T15:00 | ADX DI cross · 1h | sell | DOGE-USD | 21.81 | -0.09 | exit signal |
| 2026-10-23T15:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 9.68 | — | entry signal |
| 2026-10-23T15:00 | EMA 20/50 cross | buy | SOXL | 7.49 | — | entry signal |
| 2026-10-23T15:00 | EMA 20/50 cross | buy | QQQ | 7.51 | — | entry signal |
| 2026-10-23T15:00 | EMA 20/50 cross | buy | BTC-USD | 7.51 | — | entry signal |
| 2026-10-23T15:00 | EMA 20/50 cross | sell | TECL | 5.65 | 0.00 | rebalance down |
| 2026-10-23T15:00 | EMA 20/50 cross | sell | ETH-USD | 5.58 | -0.04 | rebalance down |
| 2026-10-23T15:00 | EMA 20/50 cross | sell | BITX | 5.59 | 0.01 | rebalance down |
| 2026-10-23T15:00 | EMA 20/50 cross | sell | AMD | 5.70 | 0.04 | rebalance down |
| 2026-10-23T14:55 | Triple EMA stack · 1h | buy | SQQQ | 4.20 | — | rebalance up |
| 2026-10-23T14:55 | RSI(14) reversion | sell | TNA | 7.61 | 0.03 | take-profit |
| 2026-10-23T14:50 | VWAP reversion | sell | SQQQ | 12.52 | -0.15 | stop-loss |
| 2026-10-23T14:50 | Three white soldiers | buy | UPRO | 20.39 | — | entry signal |
| 2026-10-23T14:50 | Three white soldiers | buy | SPY | 20.39 | — | entry signal |
| 2026-10-23T14:50 | Three white soldiers | buy | COIN | 20.39 | — | entry signal |
| 2026-10-23T14:50 | Donchian 55/20 | buy | TQQQ | 8.98 | — | entry signal |
| 2026-10-23T14:50 | Donchian 55/20 | buy | QQQ | 8.98 | — | entry signal |
| 2026-10-23T14:50 | Donchian 55/20 | sell | TECL | 4.54 | 0.01 | rebalance down |
| 2026-10-23T14:50 | Donchian 55/20 | sell | SOXL | 4.41 | -0.02 | rebalance down |
| 2026-10-23T14:50 | Donchian 55/20 | sell | NVDA | 4.49 | -0.01 | rebalance down |
| 2026-10-23T14:50 | Donchian 55/20 | sell | AMD | 4.52 | 0.01 | rebalance down |
| 2026-10-23T14:50 | EMA 20/50 cross | buy | BITX | 13.09 | — | entry signal |
| 2026-10-23T14:45 | VWAP reversion | sell | LABU | 12.74 | 0.08 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 15:15:05.000117+00:00 -> 2026-10-23 15:25:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
