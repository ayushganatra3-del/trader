# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-21T12:20:05.000140+00:00 · 68107 ticks

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
| Copy: Insider buying | 2026-11-21 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 9930 decisions in 1986 calls, $0.1389 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-21T12:20 | 1 / 4 / 0 | SOL-USD 14% |  |
| Breezy | 2026-11-21T12:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-21T12:20 | 4 / 1 / 0 | ETH-USD 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.76 | +27.55% | 6 |
| Opening range 30m | SQQQ | 1.44 | +19.43% | 6 |
| Opening range 15m | SQQQ | 1.43 | +19.52% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.49 | 14.49 | 0 | — | 12.18 | 4.08 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.74 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 0.96 | 0.41 | -7.56 | 153 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -9.71 | -5.05 | -12.45 | 51 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.21 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -2.72 | -19.56 | 14 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.98 | -7.58 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -9.45 | -1.94 | -14.79 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.77 | -12.23 | 160 | 45.0 | -14.66 | -4.24 | -20.40 | 156 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.47 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -3.84 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.78 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.90 | -15.10 | 194 | 27.8 | -22.87 | -6.12 | -27.87 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -24.07 | -6.68 | -27.44 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.49 | -6.51 | -21.29 | 71 |
| 28 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 126 | 26.2 | -20.52 | -5.39 | -25.26 | 141 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.04 | -5.13 | -21.68 | 204 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.82 | -4.05 | -18.47 | 93 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.44 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -28.01 | -7.61 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.74 | -25.26 | 228 | 20.2 | -30.69 | -5.71 | -35.87 | 270 |
| 35 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.96 | -3.42 | -58.28 | 39 |
| 36 | Bollinger breakout · 1h | breakout | 72.97 | -27.03 | 195 | 21.5 | -30.70 | -7.41 | -36.25 | 213 |
| 37 | Supertrend · 1h | trend | 72.95 | -27.05 | 198 | 16.7 | -33.51 | -6.52 | -37.64 | 200 |
| 38 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -33.20 | -8.00 | -37.59 | 171 |
| 39 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.74 | -9.72 | -40.64 | 122 |
| 40 | RSI momentum · 1h | momentum | 70.70 | -29.30 | 184 | 14.1 | -36.77 | -7.99 | -40.52 | 201 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -36.81 | -9.42 | -41.11 | 236 |
| 43 | Heikin-Ashi · 1h | trend | 69.66 | -30.34 | 487 | 22.8 | -43.57 | -8.81 | -47.85 | 615 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 47 | Hold BTC | benchmark | 67.69 | -32.31 | 3 | 0.0 | -27.67 | -4.59 | -36.23 | 1 |
| 48 | Donchian 20/10 · 1h | breakout | 67.34 | -32.66 | 165 | 17.6 | -36.69 | -7.51 | -43.26 | 191 |
| 49 | Stochastic reversion · 1h | reversion | 66.72 | -33.28 | 382 | 39.8 | -43.41 | -6.18 | -44.08 | 447 |
| 50 | ROC + volume · 1h | momentum | 66.42 | -33.58 | 431 | 27.6 | -38.92 | -7.68 | -43.29 | 340 |
| 51 | EMA 9/21 cross · 1h | trend | 64.80 | -35.20 | 291 | 11.3 | -42.42 | -9.85 | -46.01 | 318 |
| 52 | MFI reversion · 1h | reversion | 63.86 | -36.15 | 481 | 32.6 | -36.73 | -5.49 | -39.46 | 179 |
| 53 | MACD cross · 1h | trend | 62.30 | -37.70 | 446 | 20.9 | -50.24 | -10.10 | -51.44 | 503 |
| 54 | CCI reversion · 1h ⏸ | reversion | 58.33 | -41.67 | 423 | 39.5 | -48.97 | -8.07 | -51.36 | 489 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.73 | -45.42 | 445 |
| 56 | Agent (ML meta-label) | meta | 55.08 | -44.92 | 2014 | 24.6 | -30.09 | -5.38 | -32.58 | 337 |
| 57 | VWAP momentum · 1h | momentum | 55.08 | -44.92 | 1019 | 21.3 | -56.75 | -11.39 | -60.93 | 1201 |
| 58 | Williams %R · 1h ⏸ | reversion | 53.97 | -46.03 | 480 | 37.7 | -54.73 | -9.10 | -55.96 | 587 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 51.76 | -48.24 | 234 | 31.6 | -45.29 | -6.70 | -49.45 | 276 |
| 60 | Three white soldiers | momentum | 51.40 | -48.60 | 627 | 14.5 | -52.10 | -22.41 | -53.01 | 669 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.43 | -9.14 | -54.45 | 686 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -46.88 | -99.15 | 5344 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.73 | -30.61 | -84.65 | 1414 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.56 | -46.54 | -94.67 | 2463 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.91 | -32.14 | -91.46 | 1949 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.79 | -41.74 | -92.03 | 2288 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.35 | -27.07 | -89.78 | 1996 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -45.87 | -98.20 | 3480 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.92 | -55.87 | -96.98 | 3414 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.93 | -41.19 | -93.98 | 2194 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.61 | -35.46 | -83.83 | 1584 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -54.22 | -99.65 | 6332 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.84 | -40.67 | -93.01 | 2535 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.37 | -36.96 | -94.41 | 3129 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -64.17 | -99.84 | 6272 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.35 | -44.18 | -93.37 | 2279 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.28 | -24.71 | -79.73 | 1653 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.85 | -59.06 | -97.87 | 3386 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.12 | -56.26 | -99.14 | 5113 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.58 | -29.06 | -71.20 | 1233 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.85 | -49.42 | -94.94 | 2728 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -45.53 | -6.35 | -49.04 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.66 | -38.63 | -85.89 | 1713 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.74 | -72.49 | -99.74 | 6564 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.38 | -30.44 | -91.55 | 2480 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.55 | -19.59 | -82.79 | 1954 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.65 | -33.13 | -92.79 | 2208 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.01 | -47.27 | -98.02 | 4060 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.10 | -47.55 | -90.32 | 2207 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.31 | -31.26 | -67.72 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.06 | -27.79 | -74.90 | 1203 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.02 | -19.39 | -84.38 | 1861 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.79 | -46.91 | -97.81 | 4451 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -99.75 | -99.94 | 8422 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-21T12:01 | Heikin-Ashi · 1h | buy | XRP-USD | 3.47 | — | rebalance up |
| 2026-11-21T12:01 | Heikin-Ashi · 1h | sell | BTC-USD | 3.47 | -0.00 | rebalance down |
| 2026-11-21T12:00 | Bollinger reversion · 1h | sell | SOL-USD | 2.85 | 0.10 | exit signal |
| 2026-11-21T12:00 | Heikin-Ashi · 1h | buy | XRP-USD | 4.07 | — | entry signal |
| 2026-11-21T12:00 | Heikin-Ashi · 1h | buy | SOL-USD | 13.90 | — | entry signal |
| 2026-11-21T12:00 | Heikin-Ashi · 1h | sell | ETH-USD | 3.62 | 0.03 | rebalance down |
| 2026-11-21T12:00 | ADX DI cross · 1h | buy | ETH-USD | 18.68 | — | entry signal |
| 2026-11-21T12:00 | Supertrend · 1h | buy | ETH-USD | 18.23 | — | entry signal |
| 2026-11-21T11:00 | Heikin-Ashi · 1h | buy | BTC-USD | 17.34 | — | entry signal |
| 2026-11-21T11:00 | Three white soldiers | sell | DOGE-USD | 12.77 | -0.11 | exit signal |
| 2026-11-21T10:50 | Three white soldiers | buy | DOGE-USD | 12.88 | — | entry signal |
| 2026-11-21T10:00 | Bollinger reversion · 1h | sell | ETH-USD | 2.44 | 0.01 | exit signal |
| 2026-11-21T10:00 | VWAP momentum · 1h | buy | XRP-USD | 4.13 | — | entry signal |
| 2026-11-21T09:05 | Agent (ML meta-label) | buy | XRP-USD | 3.66 | — | entry |
| 2026-11-21T09:05 | Agent (ML meta-label) | sell | ETH-USD | 3.76 | 0.12 | selected signal exited |
| 2026-11-21T09:00 | VWAP momentum · 1h | sell | XRP-USD | 4.13 | -0.05 | exit signal |
| 2026-11-21T09:00 | Heikin-Ashi · 1h | buy | ETH-USD | 17.32 | — | entry signal |
| 2026-11-21T09:00 | MACD cross · 1h | buy | XRP-USD | 6.18 | — | entry signal |
| 2026-11-21T09:00 | MACD cross · 1h | buy | SOL-USD | 10.23 | — | entry signal |
| 2026-11-21T09:00 | MACD cross · 1h | buy | DOGE-USD | 10.23 | — | entry signal |
| 2026-11-21T09:00 | MACD cross · 1h | buy | BTC-USD | 10.23 | — | entry signal |
| 2026-11-21T09:00 | MACD cross · 1h | sell | ETH-USD | 4.98 | -0.07 | rebalance down |
| 2026-11-21T08:35 | RSI(14) reversion · 1h | sell | XRP-USD | 10.32 | -0.29 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:35 | RSI(14) reversion · 1h | sell | SOL-USD | 10.31 | -0.30 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:35 | RSI(14) reversion · 1h | sell | ETH-USD | 10.41 | -0.20 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:35 | RSI(14) reversion · 1h | sell | DOGE-USD | 10.30 | -0.31 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:35 | RSI(14) reversion · 1h | sell | BTC-USD | 10.42 | -0.19 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | CCI reversion · 1h | sell | XRP-USD | 11.69 | -0.22 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | CCI reversion · 1h | sell | SOL-USD | 14.55 | -0.35 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | CCI reversion · 1h | sell | ETH-USD | 11.67 | -0.19 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | CCI reversion · 1h | sell | DOGE-USD | 14.53 | -0.37 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | CCI reversion · 1h | sell | BTC-USD | 5.88 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | Williams %R · 1h | sell | XRP-USD | 10.80 | -0.20 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | Williams %R · 1h | sell | SOL-USD | 10.74 | -0.26 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | Williams %R · 1h | sell | ETH-USD | 10.83 | -0.18 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | Williams %R · 1h | sell | DOGE-USD | 10.73 | -0.28 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:10 | Williams %R · 1h | sell | BTC-USD | 10.87 | -0.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-21T08:00 | CCI reversion · 1h | buy | BTC-USD | 5.94 | — | entry signal |
| 2026-11-21T08:00 | CCI reversion · 1h | sell | XRP-USD | 2.94 | -0.05 | rebalance down |
| 2026-11-21T08:00 | CCI reversion · 1h | sell | ETH-USD | 3.00 | -0.04 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-23 12:20:05.000140+00:00 -> 2026-11-21 12:30:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
