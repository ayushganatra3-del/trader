# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-22T23:45:05.000131+00:00 · 69934 ticks

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

Today: 18717 decisions in 3744 calls, $0.2615 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-22T23:45 | 0 / 5 / 0 | cash |  |
| Breezy | 2026-11-22T23:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-22T23:45 | 3 / 2 / 0 | ETH-USD 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.73 | +27.26% | 5 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.56 | +8.27% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.46 | 14.46 | 0 | — | 12.16 | 4.62 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.12 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.59 | 0.27 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.37 | -2.45 | -2.96 | 67 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.21 | 0.50 | -7.48 | 143 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.25 | -3.93 | -9.09 | 33 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.38 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.24 | -19.56 | 18 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.87 | -7.54 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -14.12 | -2.75 | -18.60 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.90 | -12.10 | 161 | 45.3 | -15.19 | -4.43 | -20.49 | 156 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -4.00 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -4.01 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.80 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.69 | -15.31 | 194 | 27.8 | -22.85 | -6.12 | -27.61 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.29 | -6.43 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.82 | -7.66 | -20.00 | 67 |
| 28 | Keltner breakout · 1h | breakout | 80.52 | -19.48 | 126 | 26.2 | -21.87 | -6.32 | -24.03 | 138 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.17 | -4.89 | -21.94 | 199 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -24.77 | -4.14 | -25.44 | 94 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.69 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.92 | -23.08 | 107 | 14.0 | -26.80 | -7.22 | -31.39 | 108 |
| 34 | ADX DI cross · 1h | trend | 74.28 | -25.72 | 234 | 20.1 | -31.21 | -5.84 | -35.87 | 276 |
| 35 | Supertrend · 1h | trend | 74.04 | -25.96 | 198 | 16.7 | -32.58 | -6.25 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -50.88 | -3.82 | -57.07 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.84 | -27.16 | 161 | 14.3 | -31.84 | -7.65 | -36.10 | 167 |
| 38 | EMA 20/50 cross · 1h | trend | 72.68 | -27.32 | 119 | 10.1 | -35.69 | -9.68 | -40.35 | 123 |
| 39 | Bollinger breakout · 1h | breakout | 71.67 | -28.33 | 199 | 21.1 | -33.75 | -8.84 | -35.59 | 213 |
| 40 | Hold BTC | benchmark | 70.93 | -29.07 | 3 | 0.0 | -29.25 | -5.25 | -36.21 | 1 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.14 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 70.31 | -29.69 | 316 | 19.6 | -35.96 | -9.17 | -40.12 | 231 |
| 43 | RSI momentum · 1h | momentum | 69.41 | -30.59 | 186 | 14.0 | -36.60 | -8.04 | -39.77 | 202 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.41 | -37.91 | 32 |
| 45 | Heikin-Ashi · 1h | trend | 69.39 | -30.61 | 498 | 23.1 | -45.23 | -9.67 | -46.74 | 615 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 387 | 40.3 | -43.23 | -6.15 | -43.86 | 448 |
| 48 | Donchian 20/10 · 1h | breakout | 66.26 | -33.74 | 170 | 17.1 | -40.69 | -9.11 | -42.63 | 195 |
| 49 | MACD zero-line · 1h | trend | 66.20 | -33.80 | 197 | 16.8 | -34.60 | -9.57 | -35.13 | 210 |
| 50 | ROC + volume · 1h | momentum | 65.91 | -34.09 | 434 | 27.4 | -41.45 | -8.60 | -42.43 | 339 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.60 | -5.09 | -38.40 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 63.48 | -36.52 | 296 | 11.1 | -43.97 | -10.38 | -46.01 | 329 |
| 53 | MACD cross · 1h | trend | 61.75 | -38.25 | 456 | 21.3 | -48.92 | -9.60 | -49.69 | 502 |
| 54 | CCI reversion · 1h | reversion | 58.90 | -41.10 | 426 | 39.9 | -47.28 | -7.71 | -51.36 | 492 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.47 | -6.71 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.93 | -44.07 | 1027 | 21.6 | -59.08 | -13.78 | -60.63 | 1201 |
| 57 | Agent (ML meta-label) | meta | 55.14 | -44.86 | 2023 | 24.6 | -29.46 | -5.15 | -32.75 | 336 |
| 58 | Williams %R · 1h | reversion | 55.03 | -44.97 | 485 | 38.4 | -53.60 | -8.76 | -55.85 | 589 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -45.30 | -6.71 | -49.45 | 281 |
| 60 | Three white soldiers | momentum | 50.98 | -49.02 | 632 | 14.4 | -52.43 | -22.83 | -52.45 | 658 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.59 | -8.76 | -55.85 | 691 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -49.41 | -99.12 | 5343 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.46 | -36.26 | -84.51 | 1425 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.65 | -50.19 | -94.69 | 2459 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.06 | -33.19 | -91.32 | 1951 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.71 | -42.15 | -91.85 | 2281 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.57 | -28.72 | -89.61 | 1976 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -49.62 | -98.22 | 3480 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.91 | -54.62 | -96.95 | 3390 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.45 | -38.72 | -93.46 | 2173 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.41 | -35.59 | -83.60 | 1567 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -57.00 | -99.67 | 6354 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.72 | -40.71 | -92.88 | 2515 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.42 | -38.11 | -94.42 | 3144 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -69.09 | -99.83 | 6263 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.45 | -46.25 | -93.50 | 2285 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.76 | -24.25 | -79.05 | 1634 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -60.00 | -97.78 | 3354 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -61.24 | -99.18 | 5134 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.40 | -28.04 | -70.59 | 1223 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.80 | -50.13 | -94.86 | 2711 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.29 | -6.12 | -49.04 | 272 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.38 | -37.66 | -85.53 | 1693 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.41 | -99.76 | 6570 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.64 | -31.45 | -91.66 | 2495 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.01 | -20.13 | -83.13 | 1966 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.35 | -32.93 | -92.38 | 2195 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.09 | -48.90 | -98.09 | 4082 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.19 | -48.79 | -90.34 | 2223 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.58 | -30.86 | -67.79 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.63 | -27.60 | -74.36 | 1190 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.63 | -18.84 | -83.82 | 1865 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.92 | -48.94 | -97.92 | 4467 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -111.66 | -99.94 | 8391 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-22T23:00 | OBV trend · 1h | buy | BTC-USD | 17.57 | — | entry signal |
| 2026-11-22T23:00 | VWAP momentum · 1h | sell | XRP-USD | 4.44 | -0.05 | exit signal |
| 2026-11-22T23:00 | Ichimoku · 1h | buy | XRP-USD | 16.11 | — | entry signal |
| 2026-11-22T23:00 | MACD zero-line · 1h | sell | DOGE-USD | 16.45 | -0.22 | exit signal |
| 2026-11-22T23:00 | MACD cross · 1h | buy | ETH-USD | 5.06 | — | rebalance up |
| 2026-11-22T23:00 | MACD cross · 1h | buy | BTC-USD | 5.08 | — | rebalance up |
| 2026-11-22T23:00 | MACD cross · 1h | sell | SOL-USD | 12.27 | -0.10 | exit signal |
| 2026-11-22T23:00 | MACD cross · 1h | sell | DOGE-USD | 10.26 | -0.13 | exit signal |
| 2026-11-22T22:00 | ROC + volume · 1h | sell | BTC-USD | 16.39 | -0.07 | exit signal |
| 2026-11-22T22:00 | MACD cross · 1h | buy | SOL-USD | 12.37 | — | entry signal |
| 2026-11-22T22:00 | MACD cross · 1h | sell | XRP-USD | 12.31 | -0.11 | exit signal |
| 2026-11-22T21:00 | MACD zero-line · 1h | sell | SOL-USD | 16.43 | -0.23 | exit signal |
| 2026-11-22T21:00 | MACD cross · 1h | buy | XRP-USD | 6.05 | — | rebalance up |
| 2026-11-22T21:00 | MACD cross · 1h | sell | SOL-USD | 10.26 | -0.14 | exit signal |
| 2026-11-22T19:00 | Heikin-Ashi · 1h | sell | ETH-USD | 17.21 | -0.19 | exit signal |
| 2026-11-22T17:00 | VWAP momentum · 1h | buy | XRP-USD | 4.49 | — | entry signal |
| 2026-11-22T17:00 | Heikin-Ashi · 1h | buy | ETH-USD | 17.39 | — | entry signal |
| 2026-11-22T17:00 | MACD cross · 1h | buy | XRP-USD | 6.38 | — | entry signal |
| 2026-11-22T17:00 | Triple EMA stack · 1h | buy | BTC-USD | 18.22 | — | entry signal |
| 2026-11-22T16:00 | OBV trend · 1h | buy | ETH-USD | 17.58 | — | entry signal |
| 2026-11-22T16:00 | Triple EMA stack · 1h | buy | ETH-USD | 18.23 | — | entry signal |
| 2026-11-22T16:00 | Three white soldiers | sell | DOGE-USD | 12.72 | -0.07 | exit signal |
| 2026-11-22T15:21 | Three white soldiers | sell | XRP-USD | 12.68 | -0.11 | exit signal |
| 2026-11-22T15:00 | Ichimoku · 1h | buy | SOL-USD | 19.21 | — | entry signal |
| 2026-11-22T15:00 | Ichimoku · 1h | buy | ETH-USD | 19.21 | — | entry signal |
| 2026-11-22T15:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 18.15 | — | entry signal |
| 2026-11-22T15:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 18.15 | — | entry signal |
| 2026-11-22T14:45 | Three white soldiers | buy | XRP-USD | 12.79 | — | entry signal |
| 2026-11-22T14:45 | Three white soldiers | buy | DOGE-USD | 12.79 | — | entry signal |
| 2026-11-22T14:00 | Heikin-Ashi · 1h | sell | SOL-USD | 11.53 | -0.16 | exit signal |
| 2026-11-22T14:00 | Heikin-Ashi · 1h | sell | ETH-USD | 11.62 | -0.16 | exit signal |
| 2026-11-22T14:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 11.52 | -0.21 | exit signal |
| 2026-11-22T14:00 | Heikin-Ashi · 1h | sell | BTC-USD | 11.60 | -0.09 | exit signal |
| 2026-11-22T14:00 | ADX DI cross · 1h | sell | DOGE-USD | 18.39 | -0.10 | exit signal |
| 2026-11-22T14:00 | MACD cross · 1h | sell | XRP-USD | 6.38 | -0.15 | exit signal |
| 2026-11-22T13:00 | ROC + volume · 1h | buy | BTC-USD | 16.46 | — | entry signal |
| 2026-11-22T13:00 | VWAP momentum · 1h | sell | XRP-USD | 4.49 | -0.05 | exit signal |
| 2026-11-22T13:00 | Heikin-Ashi · 1h | sell | XRP-USD | 3.04 | -0.05 | exit signal |
| 2026-11-22T11:00 | CCI reversion · 1h | sell | DOGE-USD | 14.75 | 0.06 | exit signal |
| 2026-11-22T11:00 | Heikin-Ashi · 1h | buy | XRP-USD | 3.09 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-24 23:45:05.000131+00:00 -> 2026-11-22 23:55:05.000131+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
