# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T22:45:05.000166+00:00 · 71071 ticks

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

Today: 37811 decisions in 3379 calls, $0.4706 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T22:45 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-23T22:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T22:45 | 0 / 5 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.43 | 15.43 | 0 | — | 12.43 | 4.24 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.05 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.04 | 4.04 | 0 | — | 2.64 | 0.79 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.40 | -0.03 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.75 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.80 | -0.18 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.45 | -4.55 | 0 | — | -6.09 | -1.55 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -3.19 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.54 | -7.46 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.43 | -3.36 | -8.58 | 31 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.87 | -9.13 | 0 | — | -10.60 | -2.27 | -17.03 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Insider buying | copy | 90.07 | -9.93 | 58 | 39.7 | -17.15 | -3.25 | -22.56 | 68 |
| 19 | VWAP reversion · 1h | reversion | 89.93 | -10.07 | 163 | 46.0 | -7.76 | -1.41 | -20.49 | 158 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -3.29 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.58 | -13.42 | 9 | 44.4 | -10.93 | -0.60 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.39 | -14.39 | 542 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -16.45 | -3.79 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -22.06 | -7.43 | -22.23 | 82 |
| 25 | Connors RSI(2) · 1h | reversion | 80.48 | -19.52 | 220 | 40.9 | -14.26 | -6.34 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.30 | -19.70 | 203 | 28.1 | -28.20 | -7.64 | -30.34 | 190 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -25.91 | -5.63 | -26.52 | 196 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -24.74 | -4.15 | -25.84 | 91 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -22.04 | -6.86 | -23.30 | 660 |
| 30 | Donchian 55/20 · 1h ⏸ | breakout | 76.80 | -23.20 | 85 | 14.1 | -29.44 | -7.74 | -29.70 | 84 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.88 | -7.04 | -23.25 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.15 | -6.40 | -25.01 | 143 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.99 | -31.19 | 102 |
| 34 | Hold BTC | benchmark | 71.06 | -28.95 | 3 | 0.0 | -29.33 | -5.23 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 70.88 | -29.12 | 202 | 17.8 | -35.10 | -6.84 | -39.07 | 211 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.42 | -29.58 | 3 | 0.0 | -23.26 | -2.84 | -32.18 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -37.56 | -6.72 | -40.30 | 278 |
| 38 | Triple EMA stack · 1h | trend | 69.17 | -30.83 | 162 | 14.8 | -37.70 | -9.57 | -38.76 | 169 |
| 39 | Daily: Momentum burst | daily | 69.17 | -30.83 | 30 | 13.3 | -37.24 | -5.37 | -37.81 | 25 |
| 40 | EMA 20/50 cross · 1h | trend | 69.08 | -30.92 | 119 | 10.1 | -37.67 | -10.22 | -40.18 | 118 |
| 41 | Bollinger breakout · 1h | breakout | 68.65 | -31.35 | 207 | 22.2 | -32.55 | -8.54 | -33.70 | 211 |
| 42 | Stochastic reversion · 1h | reversion | 66.72 | -33.28 | 394 | 40.9 | -33.23 | -3.57 | -42.70 | 431 |
| 43 | OBV trend · 1h | momentum | 66.44 | -33.56 | 321 | 19.9 | -39.60 | -10.03 | -40.77 | 234 |
| 44 | MACD zero-line · 1h | trend | 65.89 | -34.12 | 198 | 16.7 | -35.13 | -9.62 | -35.49 | 206 |
| 45 | RSI momentum · 1h ⏸ | momentum | 65.10 | -34.90 | 196 | 15.3 | -39.57 | -8.90 | -40.95 | 201 |
| 46 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -46.88 | -9.56 | -47.76 | 630 |
| 47 | Max aggression: 5-day momentum ⏸ | meta | 64.49 | -35.51 | 25 | 36.0 | -61.95 | -4.02 | -65.69 | 23 |
| 48 | MFI reversion · 1h | reversion | 63.68 | -36.32 | 486 | 32.9 | -32.14 | -4.67 | -37.87 | 186 |
| 49 | Donchian 20/10 · 1h ⏸ | breakout | 62.04 | -37.97 | 178 | 18.0 | -39.72 | -8.48 | -41.27 | 193 |
| 50 | ROC + volume · 1h ⏸ | momentum | 61.62 | -38.38 | 451 | 27.1 | -42.87 | -8.64 | -42.87 | 344 |
| 51 | EMA 9/21 cross · 1h | trend | 59.79 | -40.21 | 299 | 11.4 | -44.45 | -10.46 | -45.46 | 333 |
| 52 | Agent (ML meta-label) | meta | 59.63 | -40.37 | 2049 | 25.0 | -13.84 | -1.70 | -25.90 | 311 |
| 53 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -52.64 | -3.86 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 58.92 | -41.08 | 467 | 21.4 | -49.37 | -9.52 | -51.01 | 516 |
| 55 | CCI reversion · 1h | reversion | 58.11 | -41.89 | 430 | 40.0 | -49.48 | -8.24 | -52.09 | 501 |
| 56 | Bollinger reversion · 1h | reversion | 57.96 | -42.04 | 391 | 37.6 | -37.11 | -4.41 | -45.42 | 431 |
| 57 | Williams %R · 1h | reversion | 54.00 | -46.00 | 500 | 38.4 | -54.43 | -8.98 | -55.78 | 587 |
| 58 | VWAP momentum · 1h | momentum | 53.54 | -46.46 | 1054 | 21.8 | -57.84 | -13.30 | -58.29 | 1182 |
| 59 | RSI(14) reversion · 1h | reversion | 51.03 | -48.97 | 241 | 32.0 | -49.69 | -7.91 | -52.23 | 290 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.81 | -8.71 | -54.81 | 666 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -48.94 | -99.11 | 5323 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.89 | -33.71 | -84.47 | 1433 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.45 | -49.61 | -94.50 | 2434 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.64 | -32.39 | -90.85 | 1911 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.71 | -42.10 | -91.80 | 2251 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.59 | -28.31 | -89.66 | 1961 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -49.56 | -98.18 | 3427 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.00 | -53.53 | -97.04 | 3370 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -38.81 | -93.67 | 2125 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.09 | -22.75 | -52.09 | 644 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.34 | -35.39 | -83.49 | 1558 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.39 | -99.67 | 6290 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.22 | -39.70 | -93.23 | 2494 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.46 | -36.70 | -94.47 | 3178 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -68.69 | -99.83 | 6142 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.17 | -44.42 | -93.32 | 2266 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.24 | -24.24 | -78.39 | 1611 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -59.43 | -97.79 | 3285 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -61.62 | -99.19 | 5120 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.75 | -27.54 | -70.78 | 1196 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.97 | -49.44 | -94.98 | 2671 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.79 | -6.22 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.53 | -37.73 | -85.53 | 1670 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.99 | -99.76 | 6546 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.56 | -30.99 | -91.69 | 2467 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.12 | -20.39 | -83.13 | 1955 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.99 | -31.58 | -92.05 | 2169 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -50.04 | -98.14 | 4052 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.22 | -48.52 | -90.35 | 2194 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.41 | -30.37 | -68.41 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.71 | -28.72 | -73.85 | 1168 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.56 | -19.48 | -84.56 | 1834 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.98 | -50.10 | -97.99 | 4412 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.74 | -99.94 | 8296 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T22:00 | Stochastic reversion · 1h | buy | XRP-USD | 7.42 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 22:45:05.000166+00:00 -> 2026-11-23 22:55:05.000166+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
