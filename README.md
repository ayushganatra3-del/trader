# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T21:15:05.000132+00:00 · 70985 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.69 (-21.31%)

Closed trades 241, win rate 35.7%, fees £6.52, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-23)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.70 · VIX 27.14 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.4, AAPL 4.1, TSLA 3.2, AMZN 1.1, GOOGL 0.8, META 0.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 36521 decisions in 3121 calls, $0.4526 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T21:15 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-11-23T21:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T21:15 | 1 / 4 / 0 | BTC-USD 54% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.81% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.39 | 15.39 | 0 | — | 12.43 | 4.24 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.05 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.02 | 4.02 | 0 | — | 2.66 | 0.80 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.83 | -0.17 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.75 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.95 | -0.23 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.44 | -4.57 | 0 | — | -6.08 | -1.55 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -3.19 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.47 | -7.53 | 0 | — | -8.65 | -1.78 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.25 | -3.29 | -8.41 | 31 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.98 | -9.02 | 0 | — | -10.46 | -2.22 | -17.03 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Insider buying | copy | 90.05 | -9.95 | 58 | 39.7 | -17.30 | -3.30 | -22.56 | 68 |
| 19 | VWAP reversion · 1h | reversion | 89.92 | -10.08 | 163 | 46.0 | -7.53 | -1.33 | -20.49 | 157 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -3.29 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.50 | -13.50 | 9 | 44.4 | -10.98 | -0.60 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.39 | -14.39 | 542 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -16.45 | -3.79 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -22.06 | -7.43 | -22.23 | 82 |
| 25 | Connors RSI(2) · 1h | reversion | 80.70 | -19.30 | 220 | 40.9 | -14.02 | -6.16 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.42 | -19.57 | 203 | 28.1 | -28.06 | -7.63 | -30.34 | 190 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -26.10 | -5.69 | -26.46 | 195 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -25.37 | -4.30 | -25.84 | 92 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -22.46 | -6.98 | -23.30 | 660 |
| 30 | Donchian 55/20 · 1h ⏸ | breakout | 76.80 | -23.20 | 85 | 14.1 | -29.26 | -7.77 | -29.56 | 84 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.88 | -7.04 | -23.25 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.39 | -6.46 | -25.26 | 144 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.99 | -31.19 | 102 |
| 34 | Hold BTC | benchmark | 71.30 | -28.70 | 3 | 0.0 | -29.11 | -5.17 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 70.89 | -29.11 | 202 | 17.8 | -35.07 | -6.83 | -39.07 | 211 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.39 | -29.61 | 3 | 0.0 | -23.27 | -2.84 | -32.18 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -37.56 | -6.72 | -40.30 | 278 |
| 38 | Triple EMA stack · 1h | trend | 69.59 | -30.41 | 162 | 14.8 | -36.85 | -9.29 | -38.79 | 169 |
| 39 | EMA 20/50 cross · 1h | trend | 69.48 | -30.52 | 119 | 10.1 | -37.35 | -10.23 | -40.18 | 118 |
| 40 | Daily: Momentum burst | daily | 69.16 | -30.84 | 30 | 13.3 | -37.24 | -5.37 | -37.81 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.64 | -31.36 | 207 | 22.2 | -32.55 | -8.54 | -33.70 | 211 |
| 42 | Stochastic reversion · 1h | reversion | 66.81 | -33.19 | 394 | 40.9 | -34.13 | -3.68 | -42.70 | 432 |
| 43 | OBV trend · 1h | momentum | 66.60 | -33.40 | 321 | 19.9 | -39.48 | -10.06 | -40.77 | 234 |
| 44 | MACD zero-line · 1h | trend | 65.87 | -34.13 | 198 | 16.7 | -35.21 | -9.65 | -35.49 | 206 |
| 45 | RSI momentum · 1h ⏸ | momentum | 65.10 | -34.90 | 196 | 15.3 | -39.30 | -8.89 | -40.90 | 201 |
| 46 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -46.90 | -9.56 | -47.76 | 630 |
| 47 | Max aggression: 5-day momentum ⏸ | meta | 64.49 | -35.51 | 25 | 36.0 | -61.52 | -4.01 | -65.46 | 23 |
| 48 | MFI reversion · 1h | reversion | 63.66 | -36.34 | 486 | 32.9 | -32.09 | -4.66 | -37.87 | 184 |
| 49 | Donchian 20/10 · 1h ⏸ | breakout | 62.04 | -37.97 | 178 | 18.0 | -39.50 | -8.48 | -41.23 | 193 |
| 50 | ROC + volume · 1h ⏸ | momentum | 61.62 | -38.38 | 451 | 27.1 | -42.61 | -8.65 | -42.80 | 345 |
| 51 | EMA 9/21 cross · 1h | trend | 60.00 | -40.00 | 299 | 11.4 | -44.33 | -10.45 | -45.46 | 333 |
| 52 | Agent (ML meta-label) | meta | 59.62 | -40.38 | 2049 | 25.0 | -21.24 | -2.74 | -32.12 | 311 |
| 53 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -52.64 | -3.86 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 58.89 | -41.10 | 467 | 21.4 | -49.37 | -9.53 | -51.01 | 516 |
| 55 | CCI reversion · 1h | reversion | 58.09 | -41.91 | 430 | 40.0 | -49.48 | -8.24 | -52.09 | 501 |
| 56 | Bollinger reversion · 1h | reversion | 57.96 | -42.04 | 391 | 37.6 | -37.66 | -4.51 | -45.42 | 434 |
| 57 | Williams %R · 1h | reversion | 53.99 | -46.01 | 500 | 38.4 | -54.43 | -8.98 | -55.78 | 587 |
| 58 | VWAP momentum · 1h | momentum | 53.51 | -46.49 | 1054 | 21.8 | -57.76 | -13.28 | -58.29 | 1180 |
| 59 | RSI(14) reversion · 1h | reversion | 51.01 | -48.99 | 241 | 32.0 | -49.88 | -7.96 | -52.23 | 289 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.13 | -8.80 | -54.93 | 669 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -49.18 | -99.13 | 5338 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.90 | -33.73 | -84.45 | 1433 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.48 | -50.05 | -94.51 | 2440 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.68 | -32.43 | -90.85 | 1913 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.71 | -42.09 | -91.80 | 2251 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.59 | -28.31 | -89.66 | 1961 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -49.74 | -98.16 | 3427 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.02 | -54.51 | -97.03 | 3370 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.66 | -39.35 | -93.66 | 2132 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.27 | -22.75 | -52.27 | 646 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.34 | -35.39 | -83.49 | 1558 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.37 | -99.67 | 6288 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.33 | -39.45 | -93.33 | 2499 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.45 | -36.71 | -94.46 | 3178 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -67.34 | -99.83 | 6146 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.18 | -44.49 | -93.32 | 2267 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.51 | -24.25 | -78.60 | 1615 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -58.73 | -97.79 | 3289 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -61.31 | -99.18 | 5117 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.88 | -27.62 | -70.88 | 1198 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.04 | -49.66 | -95.04 | 2676 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.79 | -6.22 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.69 | -37.73 | -85.69 | 1675 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.99 | -99.76 | 6544 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.49 | -30.55 | -91.69 | 2466 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.96 | -20.26 | -83.00 | 1954 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.92 | -31.13 | -92.06 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.13 | -49.97 | -98.14 | 4051 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.20 | -48.67 | -90.31 | 2193 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.34 | -30.51 | -68.34 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.78 | -28.63 | -73.91 | 1168 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.49 | -19.48 | -84.51 | 1834 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.97 | -50.08 | -97.98 | 4412 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -108.37 | -99.94 | 8300 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T21:00 | Stochastic reversion · 1h | buy | BTC-USD | 8.35 | — | entry signal |
| 2026-11-23T21:00 | OBV trend · 1h | sell | SOL-USD | 14.15 | 0.27 | exit signal |
| 2026-11-23T21:00 | Supertrend · 1h | sell | SOL-USD | 2.88 | 0.08 | exit signal |
| 2026-11-23T21:00 | Supertrend · 1h | sell | ETH-USD | 2.92 | 0.12 | exit signal |
| 2026-11-23T21:00 | MACD cross · 1h | sell | DOGE-USD | 4.47 | 0.07 | exit signal |
| 2026-11-23T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 90.60 | -1.14 | target is flat |
| 2026-11-23T20:55 | Opening range 30m | sell | UPRO | 14.43 | -0.13 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | TSLA | 14.27 | -0.12 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | SPY | 14.36 | -0.05 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | NVDA | 14.41 | -0.33 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | META | 14.44 | 0.10 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | LABU | 14.50 | 0.13 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 15m | sell | UPRO | 12.89 | -0.13 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 15m | sell | TSLA | 12.79 | -0.12 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 15m | sell | SPY | 12.87 | -0.06 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 15m | sell | NVDA | 12.86 | -0.02 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 15m | sell | META | 9.74 | 0.06 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 15m | sell | LABU | 12.97 | 0.10 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 15m | sell | AAPL | 3.18 | -0.01 | end-of-day flatten |
| 2026-11-23T20:45 | Agent (ML meta-label) | buy | SQQQ | 14.87 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T20:36 | Agent (ML meta-label) | sell | SQQQ | 14.65 | -0.26 | selected signal exited |
| 2026-11-23T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | TQQQ | 91.73 | — | entry |
| 2026-11-23T20:30 | Agent | sell | SQQQ | 15.60 | -0.17 | selected signal exited |
| 2026-11-23T20:30 | VWAP reversion · 1h | buy | MSTR | 22.55 | — | entry signal |
| 2026-11-23T20:30 | RSI(14) reversion · 1h | sell | AAPL | 2.35 | 0.00 | exit signal |
| 2026-11-23T20:30 | VWAP momentum · 1h | buy | QQQ | 4.47 | — | entry signal |
| 2026-11-23T20:30 | VWAP momentum · 1h | sell | SQQQ | 4.83 | -0.05 | exit signal |
| 2026-11-23T20:24 | Copy: Insider buying | buy | WWB | 1.31 | — | entry |
| 2026-11-23T20:22 | Copy: Insider buying | buy | KNOP | 9.91 | — | rebalance up |
| 2026-11-23T20:20 | Copy: Insider buying | sell | PAM | 11.21 | -0.07 | target is flat |
| 2026-11-23T20:20 | VWAP momentum · 1h | buy | TQQQ | 4.12 | — | entry |
| 2026-11-23T20:05 | Agent (ML meta-label) | buy | SQQQ | 14.91 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T20:00 | Agent (ML meta-label) | buy | BITX | 14.93 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | buy | QQQ | 1.17 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | buy | MSFT | 2.56 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | buy | AMZN | 2.56 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | buy | AMD | 2.56 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | sell | XRP-USD | 4.40 | 0.05 | exit signal |
| 2026-11-23T20:00 | MACD cross · 1h | sell | SOL-USD | 4.47 | 0.11 | exit signal |
| 2026-11-23T19:55 | Agent (ML meta-label) | sell | SQQQ | 14.79 | -0.09 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 21:15:05.000132+00:00 -> 2026-11-23 21:25:05.000132+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
