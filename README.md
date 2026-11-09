# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T19:35:05.000142+00:00 · 53724 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.43 (-12.57%)

Closed trades 159, win rate 35.8%, fees £4.92, max drawdown -13.04%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 17.47 | -0.14 |
| TSLA | 17.48 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 31386 decisions in 3036 calls, $0.3936 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T19:35 | 6 / 16 / 8 | META 14% |  |
| Breezy | 2026-11-09T19:35 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-09T19:35 | 7 / 20 / 3 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| VWAP momentum | TSLA | 1.69 | +2.40% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 116.86 | 16.86 | 19 | 68.4 | 16.96 | 3.51 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.39 | 12.39 | 0 | — | 13.99 | 4.76 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.26 | 11.26 | 30 | 26.7 | 19.26 | 2.97 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.35 | 3.35 | 30 | 43.3 | 3.10 | 0.85 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.50 | 1.50 | 0 | — | 5.07 | 1.45 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.02 | 1.02 | 123 | 35.0 | 9.39 | 3.83 | -2.27 | 89 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.50 | 0.50 | 7 | 42.9 | -1.45 | 0.14 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.51 | -1.49 | 181 | 29.8 | 3.49 | 1.06 | -9.06 | 241 |
| 11 | Agent (rotation) | meta | 97.82 | -2.18 | 176 | 27.8 | -2.72 | -1.14 | -9.58 | 161 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.28 | -3.14 | -12.28 | 152 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.50 | -3.50 | 0 | — | -1.59 | -0.49 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.63 | -5.37 | 0 | — | -3.76 | -0.98 | -9.25 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 18 | Trend pullback · 1h | trend | 92.73 | -7.27 | 108 | 23.1 | -13.30 | -4.96 | -17.67 | 78 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.70 | -7.30 | 0 | — | -4.08 | -1.09 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 90.13 | -9.87 | 378 | 32.3 | -13.62 | -4.38 | -15.21 | 595 |
| 22 | Copy: Insider buying | copy | 89.35 | -10.65 | 40 | 37.5 | -11.22 | -2.57 | -16.06 | 63 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -7.84 | -2.74 | -14.15 | 78 |
| 24 | Agent | meta | 87.43 | -12.57 | 159 | 35.8 | -13.18 | -6.84 | -13.71 | 203 |
| 25 | Hold BTC | benchmark | 86.63 | -13.38 | 1 | 0.0 | -5.39 | -0.63 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.27 | -13.73 | 15 | 20.0 | -9.47 | -1.41 | -17.10 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.75 | -14.25 | 167 | 26.9 | -11.18 | -2.02 | -21.29 | 227 |
| 28 | Agent (aggressive) | meta | 84.33 | -15.68 | 75 | 32.0 | -15.74 | -4.46 | -18.49 | 93 |
| 29 | Donchian 55/20 · 1h | breakout | 83.70 | -16.30 | 71 | 14.1 | -16.48 | -3.50 | -21.90 | 103 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 83.55 | -16.45 | 2 | 0.0 | -8.28 | -0.94 | -24.16 | 1 |
| 31 | Opening range 15m | breakout | 83.25 | -16.75 | 466 | 30.5 | -18.62 | -5.38 | -19.85 | 730 |
| 32 | Stochastic reversion · 1h | reversion | 82.92 | -17.08 | 279 | 48.4 | -24.14 | -3.58 | -28.16 | 388 |
| 33 | Keltner breakout · 1h | breakout | 81.93 | -18.07 | 107 | 23.4 | -21.84 | -4.54 | -25.10 | 180 |
| 34 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.85 | -3.37 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.74 | -19.26 | 205 | 40.0 | -19.53 | -6.56 | -19.85 | 124 |
| 36 | Heikin-Ashi · 1h | trend | 79.71 | -20.29 | 400 | 22.8 | -39.35 | -7.48 | -42.54 | 679 |
| 37 | ADX DI cross · 1h | trend | 79.29 | -20.71 | 179 | 18.4 | -22.60 | -3.86 | -28.65 | 269 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -39.06 | -2.62 | -44.97 | 25 |
| 39 | MFI reversion · 1h | reversion | 79.03 | -20.97 | 349 | 34.1 | -17.79 | -2.29 | -21.38 | 164 |
| 40 | CCI reversion · 1h | reversion | 78.71 | -21.29 | 314 | 44.9 | -24.74 | -3.82 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -28.42 | -7.96 | -29.12 | 117 |
| 42 | Bollinger breakout · 1h | breakout | 76.91 | -23.09 | 170 | 22.9 | -22.51 | -4.65 | -27.85 | 241 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.54 | -4.09 | -33.23 | 373 |
| 44 | MACD cross · 1h | trend | 75.11 | -24.89 | 349 | 22.6 | -33.76 | -5.60 | -39.46 | 488 |
| 45 | Z-score reversion · 1h | reversion | 74.83 | -25.17 | 176 | 36.4 | -20.63 | -2.99 | -27.66 | 228 |
| 46 | Williams %R · 1h | reversion | 74.78 | -25.22 | 336 | 46.7 | -35.92 | -5.85 | -38.86 | 542 |
| 47 | MACD zero-line · 1h | trend | 74.48 | -25.52 | 157 | 16.6 | -24.79 | -5.11 | -29.19 | 213 |
| 48 | EMA 20/50 cross · 1h | trend | 74.34 | -25.66 | 102 | 10.8 | -22.56 | -3.77 | -32.00 | 127 |
| 49 | Supertrend · 1h | trend | 73.35 | -26.65 | 167 | 13.2 | -31.26 | -5.64 | -34.87 | 229 |
| 50 | RSI momentum · 1h | momentum | 73.11 | -26.89 | 159 | 12.6 | -22.82 | -3.59 | -32.61 | 214 |
| 51 | Triple EMA stack · 1h | trend | 72.64 | -27.36 | 143 | 14.7 | -26.16 | -4.63 | -34.72 | 202 |
| 52 | OBV trend · 1h | momentum | 71.85 | -28.15 | 274 | 18.2 | -25.81 | -4.44 | -34.49 | 274 |
| 53 | ROC + volume · 1h | momentum | 71.59 | -28.41 | 349 | 25.5 | -36.79 | -6.96 | -39.43 | 387 |
| 54 | Daily: Momentum burst | daily | 70.49 | -29.51 | 26 | 11.5 | -37.97 | -5.41 | -39.42 | 31 |
| 55 | Donchian 20/10 · 1h | breakout | 70.48 | -29.52 | 142 | 19.7 | -31.87 | -5.93 | -35.64 | 210 |
| 56 | RSI(14) reversion · 1h | reversion | 67.88 | -32.12 | 160 | 30.6 | -29.86 | -4.69 | -33.00 | 238 |
| 57 | Agent (ML meta-label) | meta | 67.79 | -32.21 | 1617 | 24.0 | -7.44 | -1.10 | -16.24 | 331 |
| 58 | VWAP momentum · 1h | momentum | 67.59 | -32.41 | 810 | 21.6 | -52.32 | -11.31 | -53.66 | 1233 |
| 59 | Max aggression: 1-day momentum | meta | 67.04 | -32.96 | 27 | 25.9 | -32.76 | -1.74 | -57.50 | 42 |
| 60 | EMA 9/21 cross · 1h | trend | 65.64 | -34.36 | 247 | 9.7 | -39.11 | -7.47 | -40.85 | 334 |
| 61 | Candlestick reversal · 1h | reversion | 65.06 | -34.94 | 434 | 28.6 | -38.24 | -6.98 | -39.05 | 585 |
| 62 | Three white soldiers | momentum | 62.31 | -37.69 | 494 | 15.2 | -48.64 | -22.77 | -48.64 | 646 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -45.90 | -98.98 | 5263 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.69 | -26.41 | -79.77 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.17 | -46.22 | -93.28 | 2507 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.07 | -32.28 | -89.16 | 1901 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.64 | -40.03 | -90.71 | 2308 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.73 | -90.05 | 2191 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -54.68 | -97.67 | 3452 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -58.01 | -96.28 | 3411 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -32.71 | -93.67 | 2413 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.04 | -34.42 | -82.21 | 1675 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -56.09 | -99.53 | 5968 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.26 | -43.14 | -92.46 | 2593 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -37.57 | -95.49 | 3402 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -76.27 | -99.79 | 6147 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.73 | -44.10 | -91.73 | 2255 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.32 | -24.80 | -75.70 | 1583 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -62.39 | -97.67 | 3511 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.75 | -98.85 | 4883 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.52 | -26.91 | -69.32 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.50 | -55.18 | -94.52 | 2736 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -37.71 | -84.73 | 1767 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.41 | -99.65 | 6376 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.66 | -32.75 | -89.67 | 2270 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.45 | -20.17 | -78.46 | 1746 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -37.02 | -90.63 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -52.54 | -96.81 | 3879 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -58.56 | -89.31 | 2145 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.01 | -29.05 | -66.26 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.34 | -23.17 | -72.00 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.58 | -19.13 | -79.74 | 1685 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -50.26 | -97.32 | 4316 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -110.71 | -99.93 | 8288 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T19:35 | Agent (ML meta-label) | buy | SOXL | 4.41 | — | rebalance up |
| 2026-11-09T19:35 | Agent (ML meta-label) | buy | AAPL | 6.16 | — | entry |
| 2026-11-09T19:35 | Agent (ML meta-label) | sell | TQQQ | 4.84 | 0.01 | selected signal exited |
| 2026-11-09T19:35 | Agent (ML meta-label) | sell | QQQ | 4.52 | -0.01 | selected signal exited |
| 2026-11-09T19:35 | Agent (ML meta-label) | sell | LABU | 4.77 | 0.01 | selected signal exited |
| 2026-11-09T19:35 | Agent (ML meta-label) | sell | BITX | 2.61 | -0.01 | selected signal exited |
| 2026-11-09T19:35 | Agent | buy | TSLA | 17.49 | — | following VWAP momentum |
| 2026-11-09T19:30 | Agent (ML meta-label) | buy | TQQQ | 4.84 | — | entry |
| 2026-11-09T19:30 | Agent (ML meta-label) | sell | UPRO | 5.24 | 0.10 | selected signal exited |
| 2026-11-09T19:30 | Agent (ML meta-label) | sell | META | 4.24 | 0.00 | selected signal exited |
| 2026-11-09T19:30 | MFI reversion · 1h | sell | UPRO | 7.29 | 0.10 | exit signal |
| 2026-11-09T19:30 | CCI reversion · 1h | buy | SOL-USD | 4.35 | — | rebalance up |
| 2026-11-09T19:30 | CCI reversion · 1h | sell | TSLA | 5.35 | 0.22 | exit signal |
| 2026-11-09T19:30 | CCI reversion · 1h | sell | TNA | 1.58 | 0.03 | exit signal |
| 2026-11-09T19:30 | CCI reversion · 1h | sell | QQQ | 5.24 | 0.12 | exit signal |
| 2026-11-09T19:30 | CCI reversion · 1h | sell | LABU | 4.28 | 0.15 | exit signal |
| 2026-11-09T19:30 | Stochastic reversion · 1h | buy | SQQQ | 4.43 | — | entry signal |
| 2026-11-09T19:30 | Stochastic reversion · 1h | sell | COIN | 4.25 | -0.01 | rebalance down |
| 2026-11-09T19:30 | OBV trend · 1h | buy | META | 17.95 | — | entry signal |
| 2026-11-09T19:30 | VWAP momentum · 1h | buy | AAPL | 4.22 | — | entry signal |
| 2026-11-09T19:30 | Heikin-Ashi · 1h | sell | COIN | 4.41 | -0.01 | exit signal |
| 2026-11-09T19:30 | Heikin-Ashi · 1h | sell | AMZN | 3.96 | -0.01 | exit signal |
| 2026-11-09T19:30 | MACD zero-line · 1h | buy | TNA | 12.38 | — | entry signal |
| 2026-11-09T19:30 | MACD zero-line · 1h | buy | LABU | 12.40 | — | entry signal |
| 2026-11-09T19:30 | MACD zero-line · 1h | sell | META | 6.31 | 0.03 | rebalance down |
| 2026-11-09T19:30 | MACD zero-line · 1h | sell | IWM | 6.16 | -0.01 | rebalance down |
| 2026-11-09T19:30 | MACD zero-line · 1h | sell | GOOGL | 5.95 | -0.09 | rebalance down |
| 2026-11-09T19:30 | MACD zero-line · 1h | sell | AMD | 6.31 | 0.03 | rebalance down |
| 2026-11-09T19:30 | EMA 20/50 cross · 1h | buy | META | 18.59 | — | entry signal |
| 2026-11-09T19:30 | EMA 9/21 cross · 1h | buy | QQQ | 3.46 | — | entry signal |
| 2026-11-09T19:30 | EMA 9/21 cross · 1h | sell | MSFT | 3.46 | 0.02 | rebalance down |
| 2026-11-09T19:30 | Gap and go | sell | TNA | 19.67 | 0.54 | stop-loss |
| 2026-11-09T19:30 | Gap and go | sell | IWM | 24.42 | 0.16 | stop-loss |
| 2026-11-09T19:25 | Agent (ML meta-label) | buy | META | 4.24 | — | entry |
| 2026-11-09T19:25 | Agent (ML meta-label) | sell | AAPL | 5.23 | 0.00 | selected signal exited |
| 2026-11-09T19:20 | Agent (ML meta-label) | buy | SOXL | 1.75 | — | entry |
| 2026-11-09T19:20 | Agent (ML meta-label) | buy | BITX | 2.62 | — | entry |
| 2026-11-09T19:20 | Agent (ML meta-label) | sell | SPY | 4.07 | -0.01 | selected signal exited |
| 2026-11-09T19:15 | Agent (ML meta-label) | buy | QQQ | 4.53 | — | entry |
| 2026-11-09T19:15 | Agent (ML meta-label) | sell | SOXL | 4.83 | -0.02 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 19:35:05.000142+00:00 -> 2026-11-09 19:45:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 19:35:05.000142+00:00 -> 2026-11-09 19:45:05.000142+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 19:35:05.000142+00:00 -> 2026-11-09 19:45:05.000142+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
