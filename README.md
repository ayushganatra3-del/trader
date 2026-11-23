# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T00:15:05.000134+00:00 · 69957 ticks

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

Today: 195 decisions in 39 calls, $0.0027 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T00:15 | 3 / 1 / 1 | cash |  |
| Breezy | 2026-11-23T00:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T00:15 | 3 / 2 / 0 | ETH-USD 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.80% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.65 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.49 | 14.49 | 0 | — | 12.18 | 4.59 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.11 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.33 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.27 | -2.33 | -2.86 | 68 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.30 | 0.52 | -7.48 | 144 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.54 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.75 | -3.99 | -9.58 | 34 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.35 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.21 | -19.56 | 18 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.98 | -7.51 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -14.13 | -2.73 | -18.60 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.90 | -12.10 | 161 | 45.3 | -15.19 | -4.39 | -20.49 | 156 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.18 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.96 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -3.97 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.79 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.75 | -15.25 | 194 | 27.8 | -22.81 | -6.05 | -27.61 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.29 | -6.38 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.82 | -7.59 | -20.00 | 67 |
| 28 | Keltner breakout · 1h | breakout | 80.55 | -19.45 | 126 | 26.2 | -22.25 | -6.37 | -24.07 | 138 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -20.58 | -4.93 | -21.36 | 199 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.71 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.50 | -3.92 | -18.44 | 91 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.63 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.99 | -23.01 | 107 | 14.0 | -26.73 | -7.13 | -31.39 | 108 |
| 34 | ADX DI cross · 1h | trend | 74.27 | -25.73 | 234 | 20.1 | -31.22 | -5.79 | -35.87 | 276 |
| 35 | Supertrend · 1h | trend | 74.08 | -25.91 | 198 | 16.7 | -32.54 | -6.19 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -50.89 | -3.79 | -57.08 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.86 | -27.14 | 161 | 14.3 | -31.71 | -7.52 | -36.10 | 167 |
| 38 | EMA 20/50 cross · 1h | trend | 72.67 | -27.33 | 119 | 10.1 | -35.58 | -9.53 | -40.32 | 124 |
| 39 | Bollinger breakout · 1h | breakout | 71.69 | -28.30 | 199 | 21.1 | -33.74 | -8.75 | -35.61 | 213 |
| 40 | Hold BTC | benchmark | 70.88 | -29.11 | 3 | 0.0 | -28.73 | -5.09 | -36.21 | 1 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 70.33 | -29.67 | 316 | 19.6 | -35.86 | -9.02 | -40.13 | 231 |
| 43 | RSI momentum · 1h | momentum | 69.43 | -30.57 | 186 | 14.0 | -36.52 | -7.89 | -39.81 | 202 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.36 | -37.91 | 32 |
| 45 | Heikin-Ashi · 1h | trend | 69.39 | -30.61 | 498 | 23.1 | -45.23 | -9.57 | -46.74 | 615 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.18 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 387 | 40.3 | -43.39 | -6.12 | -43.99 | 448 |
| 48 | Donchian 20/10 · 1h | breakout | 66.28 | -33.72 | 170 | 17.1 | -40.65 | -9.01 | -42.61 | 195 |
| 49 | MACD zero-line · 1h | trend | 66.19 | -33.81 | 197 | 16.8 | -34.61 | -9.47 | -35.13 | 210 |
| 50 | ROC + volume · 1h | momentum | 65.94 | -34.06 | 434 | 27.4 | -40.93 | -8.51 | -41.91 | 337 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.58 | -5.04 | -38.38 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 63.49 | -36.51 | 296 | 11.1 | -43.73 | -10.18 | -46.01 | 328 |
| 53 | MACD cross · 1h | trend | 61.70 | -38.30 | 456 | 21.3 | -48.97 | -9.52 | -49.69 | 504 |
| 54 | CCI reversion · 1h | reversion | 58.93 | -41.07 | 426 | 39.9 | -47.25 | -7.64 | -51.36 | 492 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.67 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.97 | -44.03 | 1027 | 21.6 | -58.70 | -13.48 | -60.42 | 1200 |
| 57 | Agent (ML meta-label) | meta | 55.14 | -44.86 | 2023 | 24.6 | -36.96 | -6.92 | -38.17 | 350 |
| 58 | Williams %R · 1h | reversion | 55.03 | -44.97 | 485 | 38.4 | -53.62 | -8.66 | -55.86 | 588 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.57 | -6.53 | -49.45 | 277 |
| 60 | Three white soldiers | momentum | 50.98 | -49.02 | 632 | 14.4 | -52.46 | -22.38 | -52.48 | 658 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.89 | -8.59 | -55.20 | 689 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -46.92 | -99.12 | 5347 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.58 | -35.25 | -84.64 | 1425 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.65 | -47.29 | -94.69 | 2460 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.06 | -32.14 | -91.26 | 1950 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.69 | -40.18 | -91.81 | 2280 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.55 | -28.00 | -89.58 | 1976 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -46.73 | -98.22 | 3480 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.87 | -52.40 | -96.90 | 3385 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.41 | -37.29 | -93.42 | 2169 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.31 | -34.42 | -83.50 | 1565 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.09 | -99.66 | 6345 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.72 | -39.00 | -92.88 | 2515 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.41 | -36.57 | -94.41 | 3142 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -62.30 | -99.83 | 6263 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.44 | -43.80 | -93.49 | 2285 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.72 | -23.85 | -79.01 | 1633 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -55.14 | -97.78 | 3353 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -55.99 | -99.17 | 5130 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.40 | -27.35 | -70.59 | 1223 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.80 | -47.16 | -94.87 | 2711 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.29 | -6.07 | -49.04 | 272 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.38 | -36.25 | -85.54 | 1693 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -66.65 | -99.76 | 6568 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.63 | -30.57 | -91.65 | 2495 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.94 | -19.71 | -83.06 | 1964 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.34 | -31.81 | -92.37 | 2197 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.08 | -45.82 | -98.08 | 4078 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.18 | -46.05 | -90.33 | 2223 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.59 | -29.99 | -67.80 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.63 | -26.95 | -74.36 | 1190 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.72 | -18.54 | -83.90 | 1863 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.92 | -46.18 | -97.92 | 4467 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -89.62 | -99.94 | 8388 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T00:05 | MACD cross · 1h | buy | DOGE-USD | 7.35 | — | entry |
| 2026-11-23T00:05 | MACD cross · 1h | sell | ETH-USD | 3.13 | -0.01 | rebalance down |
| 2026-11-23T00:05 | MACD cross · 1h | sell | BTC-USD | 3.11 | -0.01 | rebalance down |
| 2026-11-23T00:00 | MACD cross · 1h | buy | SOL-USD | 15.44 | — | entry signal |
| 2026-11-23T00:00 | EMA 20/50 cross · 1h | buy | SOL-USD | 17.19 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 00:15:05.000134+00:00 -> 2026-11-23 00:25:05.000134+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
