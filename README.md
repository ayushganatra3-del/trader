# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T03:16:05.000154+00:00 · 70112 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £80.18 (-19.82%)

Closed trades 238, win rate 36.1%, fees £6.46, max drawdown -20.19%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-21 | WWB 12%, PEPG 12%, KNOP 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 2510 decisions in 502 calls, $0.0352 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T03:16 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-23T03:16 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T03:16 | 5 / 0 / 0 | ETH-USD 74% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.65 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.20 | 14.20 | 0 | — | 12.16 | 4.58 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.11 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.33 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.35 | 1.35 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.59 | 0.27 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.37 | -2.43 | -2.96 | 67 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.21 | 0.49 | -7.48 | 143 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.54 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.81 | -4.03 | -9.64 | 34 |
| 15 | Daily: Bullish score | daily | 90.88 | -9.12 | 19 | 15.8 | -11.44 | -3.21 | -19.56 | 18 |
| 16 | Hold SPY | benchmark | 90.74 | -9.26 | 0 | — | -10.23 | -3.35 | -11.71 | 1 |
| 17 | Squeeze breakout · 1h | breakout | 88.40 | -11.60 | 70 | 20.0 | -17.62 | -7.77 | -19.53 | 74 |
| 18 | VWAP reversion · 1h | reversion | 87.80 | -12.20 | 161 | 45.3 | -15.19 | -4.39 | -20.49 | 156 |
| 19 | Copy: Insider buying | copy | 87.74 | -12.26 | 56 | 39.3 | -14.12 | -2.73 | -18.60 | 65 |
| 20 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.96 | -14.87 | 552 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 87.34 | -12.66 | 0 | — | -12.95 | -3.18 | -13.87 | 1 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.75 | -14.25 | 0 | — | -14.84 | -3.97 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.79 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.15 | -15.85 | 197 | 27.4 | -23.34 | -6.22 | -27.61 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.82 | -18.18 | 79 | 12.7 | -23.29 | -6.38 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.63 | -18.37 | 163 | 28.8 | -17.82 | -7.59 | -20.00 | 67 |
| 28 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.17 | -4.85 | -21.94 | 199 |
| 29 | Keltner breakout · 1h | breakout | 79.85 | -20.15 | 128 | 25.8 | -22.38 | -6.44 | -24.03 | 138 |
| 30 | Connors RSI(2) · 1h | reversion | 79.77 | -20.23 | 218 | 40.4 | -15.04 | -6.71 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -24.76 | -4.11 | -25.44 | 94 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.63 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.77 | -23.23 | 108 | 13.9 | -26.82 | -7.16 | -31.39 | 108 |
| 34 | ADX DI cross · 1h | trend | 74.16 | -25.84 | 234 | 20.1 | -31.24 | -5.79 | -35.87 | 276 |
| 35 | Supertrend · 1h | trend | 73.84 | -26.16 | 198 | 16.7 | -32.63 | -6.21 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 72.87 | -27.13 | 33 | 27.3 | -50.88 | -3.79 | -57.07 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.68 | -27.32 | 161 | 14.3 | -31.75 | -7.55 | -36.01 | 167 |
| 38 | EMA 20/50 cross · 1h | trend | 72.50 | -27.50 | 119 | 10.1 | -35.53 | -9.50 | -40.32 | 124 |
| 39 | Bollinger breakout · 1h | breakout | 71.07 | -28.93 | 201 | 20.9 | -34.18 | -8.91 | -35.59 | 213 |
| 40 | Hold BTC | benchmark | 70.62 | -29.38 | 3 | 0.0 | -28.80 | -5.10 | -36.21 | 1 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 69.66 | -30.34 | 318 | 19.5 | -36.28 | -9.17 | -40.13 | 232 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.36 | -37.91 | 32 |
| 44 | Heikin-Ashi · 1h | trend | 69.34 | -30.66 | 498 | 23.1 | -45.23 | -9.57 | -46.74 | 615 |
| 45 | RSI momentum · 1h | momentum | 68.99 | -31.01 | 187 | 13.9 | -36.88 | -8.04 | -39.81 | 202 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.18 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 388 | 40.2 | -43.66 | -6.15 | -44.25 | 448 |
| 48 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -34.69 | -9.51 | -35.13 | 210 |
| 49 | Donchian 20/10 · 1h | breakout | 65.90 | -34.10 | 171 | 17.0 | -40.90 | -9.10 | -42.63 | 195 |
| 50 | ROC + volume · 1h | momentum | 65.63 | -34.37 | 435 | 27.4 | -41.52 | -8.53 | -42.27 | 338 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.60 | -5.04 | -38.40 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 63.13 | -36.87 | 298 | 11.1 | -44.26 | -10.39 | -46.01 | 329 |
| 53 | MACD cross · 1h | trend | 61.04 | -38.96 | 460 | 21.1 | -49.78 | -9.77 | -49.99 | 505 |
| 54 | CCI reversion · 1h | reversion | 58.87 | -41.13 | 426 | 39.9 | -47.25 | -7.64 | -51.36 | 492 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.47 | -6.65 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.34 | -44.66 | 1031 | 21.6 | -58.70 | -13.51 | -60.44 | 1197 |
| 57 | Williams %R · 1h | reversion | 55.03 | -44.97 | 485 | 38.4 | -53.95 | -8.72 | -56.18 | 589 |
| 58 | Agent (ML meta-label) | meta | 55.03 | -44.97 | 2023 | 24.6 | -36.12 | -6.14 | -38.66 | 345 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -45.13 | -6.64 | -49.45 | 279 |
| 60 | Three white soldiers | momentum | 50.98 | -49.02 | 632 | 14.4 | -52.43 | -22.40 | -52.45 | 658 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.59 | -8.67 | -55.85 | 691 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -48.16 | -99.13 | 5356 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.65 | -35.84 | -84.69 | 1424 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.64 | -48.78 | -94.68 | 2458 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.18 | -32.76 | -91.26 | 1955 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.77 | -41.10 | -91.81 | 2284 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.56 | -28.27 | -89.56 | 1970 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.21 | -47.73 | -98.21 | 3480 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -52.36 | -96.95 | 3391 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.51 | -37.75 | -93.51 | 2176 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.45 | -34.96 | -83.60 | 1566 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -53.94 | -99.67 | 6353 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -39.22 | -92.83 | 2517 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.39 | -36.59 | -94.39 | 3141 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -63.24 | -99.83 | 6262 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.47 | -44.37 | -93.48 | 2284 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.72 | -23.91 | -79.00 | 1633 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -56.52 | -97.80 | 3357 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -58.35 | -99.19 | 5140 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.41 | -27.41 | -70.56 | 1222 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.83 | -47.83 | -94.89 | 2714 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.29 | -6.07 | -49.04 | 272 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.45 | -36.63 | -85.57 | 1696 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -70.30 | -99.76 | 6575 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.72 | -30.97 | -91.77 | 2500 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.92 | -19.69 | -83.02 | 1968 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.23 | -31.36 | -92.28 | 2193 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.10 | -46.78 | -98.11 | 4085 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.21 | -47.67 | -90.36 | 2225 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.65 | -30.15 | -67.72 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.69 | -27.09 | -74.36 | 1191 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.65 | -18.55 | -83.73 | 1870 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.94 | -47.33 | -97.95 | 4471 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -89.18 | -99.94 | 8390 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T03:05 | Stochastic reversion · 1h | sell | DOGE-USD | 4.78 | -0.01 | target is flat |
| 2026-11-23T03:00 | Stochastic reversion · 1h | buy | DOGE-USD | 4.79 | — | entry signal |
| 2026-11-23T03:00 | Keltner breakout · 1h | sell | ETH-USD | 19.84 | -0.30 | exit signal |
| 2026-11-23T03:00 | Keltner breakout · 1h | sell | BTC-USD | 19.80 | -0.33 | exit signal |
| 2026-11-23T03:00 | Bollinger breakout · 1h | sell | ETH-USD | 17.66 | -0.26 | exit signal |
| 2026-11-23T03:00 | Bollinger breakout · 1h | sell | BTC-USD | 17.62 | -0.30 | exit signal |
| 2026-11-23T03:00 | Donchian 20/10 · 1h | sell | ETH-USD | 16.32 | -0.24 | exit signal |
| 2026-11-23T03:00 | OBV trend · 1h | sell | SOL-USD | 17.15 | -0.28 | exit signal |
| 2026-11-23T03:00 | OBV trend · 1h | sell | ETH-USD | 17.31 | -0.27 | exit signal |
| 2026-11-23T03:00 | ROC + volume · 1h | sell | ETH-USD | 16.25 | -0.24 | exit signal |
| 2026-11-23T03:00 | Parabolic SAR · 1h | sell | SOL-USD | 17.30 | -0.23 | exit signal |
| 2026-11-23T03:00 | MACD cross · 1h | sell | SOL-USD | 15.21 | -0.22 | exit signal |
| 2026-11-23T03:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.18 | — | rebalance up |
| 2026-11-23T03:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 5.23 | — | rebalance up |
| 2026-11-23T03:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 10.34 | -0.27 | exit signal |
| 2026-11-23T02:05 | RSI momentum · 1h | sell | DOGE-USD | 17.00 | -0.38 | target is flat |
| 2026-11-23T02:00 | VWAP momentum · 1h | sell | SOL-USD | 13.80 | -0.06 | exit signal |
| 2026-11-23T02:00 | VWAP momentum · 1h | sell | ETH-USD | 13.81 | -0.01 | exit signal |
| 2026-11-23T02:00 | VWAP momentum · 1h | sell | BTC-USD | 13.79 | 0.02 | exit signal |
| 2026-11-23T02:00 | Parabolic SAR · 1h | buy | SOL-USD | 3.38 | — | rebalance up |
| 2026-11-23T02:00 | Parabolic SAR · 1h | buy | ETH-USD | 7.01 | — | rebalance up |
| 2026-11-23T02:00 | Parabolic SAR · 1h | buy | BTC-USD | 7.01 | — | rebalance up |
| 2026-11-23T02:00 | Parabolic SAR · 1h | sell | XRP-USD | 3.55 | -0.10 | exit signal |
| 2026-11-23T02:00 | Parabolic SAR · 1h | sell | DOGE-USD | 13.85 | -0.30 | exit signal |
| 2026-11-23T02:00 | MACD zero-line · 1h | sell | BTC-USD | 16.46 | -0.20 | exit signal |
| 2026-11-23T02:00 | MACD cross · 1h | sell | ETH-USD | 15.23 | -0.20 | exit signal |
| 2026-11-23T02:00 | MACD cross · 1h | sell | BTC-USD | 15.26 | -0.17 | exit signal |
| 2026-11-23T02:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 10.27 | — | rebalance up |
| 2026-11-23T02:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 10.36 | -0.18 | exit signal |
| 2026-11-23T01:20 | MACD cross · 1h | buy | BTC-USD | 3.07 | — | rebalance up |
| 2026-11-23T01:00 | OBV trend · 1h | buy | SOL-USD | 17.43 | — | entry signal |
| 2026-11-23T01:00 | VWAP momentum · 1h | buy | SOL-USD | 4.61 | — | rebalance up |
| 2026-11-23T01:00 | VWAP momentum · 1h | buy | ETH-USD | 4.56 | — | rebalance up |
| 2026-11-23T01:00 | VWAP momentum · 1h | buy | BTC-USD | 4.51 | — | rebalance up |
| 2026-11-23T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 9.24 | -0.02 | exit signal |
| 2026-11-23T01:00 | Ichimoku · 1h | sell | XRP-USD | 16.02 | -0.09 | exit signal |
| 2026-11-23T01:00 | MACD cross · 1h | buy | ETH-USD | 3.10 | — | rebalance up |
| 2026-11-23T01:00 | MACD cross · 1h | sell | DOGE-USD | 7.27 | -0.07 | exit signal |
| 2026-11-23T00:05 | MACD cross · 1h | buy | DOGE-USD | 7.35 | — | entry |
| 2026-11-23T00:05 | MACD cross · 1h | sell | ETH-USD | 3.13 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 03:16:05.000154+00:00 -> 2026-11-23 03:26:05.000154+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
