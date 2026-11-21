# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-21T09:50:05.000175+00:00 · 67982 ticks

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

Today: 8055 decisions in 1611 calls, $0.1128 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-21T09:50 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-21T09:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-21T09:50 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.76 | +27.55% | 6 |
| Opening range 30m | SQQQ | 1.44 | +19.43% | 6 |
| Opening range 15m | SQQQ | 1.43 | +19.52% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.46 | 14.46 | 0 | — | 12.16 | 4.07 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.74 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.59 | 0.27 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.85 | -4.19 | -5.43 | 75 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 0.88 | 0.39 | -7.56 | 152 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -9.71 | -5.05 | -12.45 | 51 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.21 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -2.72 | -19.56 | 14 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.98 | -7.58 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -9.44 | -1.94 | -14.79 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.77 | -12.23 | 160 | 45.0 | -14.66 | -4.24 | -20.40 | 156 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.47 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -3.84 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.78 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.90 | -15.10 | 194 | 27.8 | -23.12 | -6.20 | -28.18 | 193 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -24.07 | -6.68 | -27.44 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.49 | -6.51 | -21.29 | 71 |
| 28 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 126 | 26.2 | -19.53 | -4.84 | -25.26 | 142 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.63 | -5.04 | -22.26 | 204 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.78 | -15.07 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -25.05 | -4.20 | -25.48 | 96 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.44 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -28.01 | -7.61 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.72 | -25.28 | 228 | 20.2 | -30.72 | -5.72 | -35.87 | 269 |
| 35 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.95 | -3.41 | -58.27 | 39 |
| 36 | Bollinger breakout · 1h | breakout | 72.97 | -27.03 | 195 | 21.5 | -30.70 | -7.41 | -36.25 | 213 |
| 37 | Supertrend · 1h | trend | 72.93 | -27.07 | 198 | 16.7 | -33.54 | -6.53 | -37.64 | 199 |
| 38 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -32.99 | -7.93 | -37.59 | 171 |
| 39 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.74 | -9.72 | -40.64 | 122 |
| 40 | RSI momentum · 1h | momentum | 70.70 | -29.30 | 184 | 14.1 | -37.57 | -8.08 | -41.90 | 202 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -36.24 | -9.16 | -41.22 | 236 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 44 | Heikin-Ashi · 1h | trend | 69.33 | -30.67 | 487 | 22.8 | -44.64 | -9.30 | -47.85 | 616 |
| 45 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 47 | Donchian 20/10 · 1h | breakout | 67.34 | -32.66 | 165 | 17.6 | -36.69 | -7.51 | -43.26 | 191 |
| 48 | Hold BTC | benchmark | 67.05 | -32.95 | 3 | 0.0 | -28.21 | -4.71 | -36.23 | 1 |
| 49 | Stochastic reversion · 1h | reversion | 66.65 | -33.35 | 382 | 39.8 | -43.47 | -6.20 | -44.07 | 447 |
| 50 | ROC + volume · 1h | momentum | 66.42 | -33.58 | 431 | 27.6 | -39.32 | -7.67 | -43.61 | 341 |
| 51 | EMA 9/21 cross · 1h | trend | 64.80 | -35.20 | 291 | 11.3 | -42.42 | -9.85 | -46.01 | 318 |
| 52 | MFI reversion · 1h | reversion | 63.29 | -36.71 | 481 | 32.6 | -36.82 | -5.51 | -39.01 | 179 |
| 53 | MACD cross · 1h | trend | 61.65 | -38.35 | 446 | 20.9 | -50.79 | -10.25 | -51.44 | 503 |
| 54 | CCI reversion · 1h ⏸ | reversion | 58.33 | -41.67 | 423 | 39.5 | -49.60 | -8.13 | -51.36 | 489 |
| 55 | Bollinger reversion · 1h | reversion | 57.90 | -42.10 | 381 | 36.2 | -44.56 | -6.73 | -45.42 | 445 |
| 56 | Agent (ML meta-label) | meta | 54.95 | -45.05 | 2014 | 24.6 | -30.76 | -5.32 | -32.84 | 324 |
| 57 | VWAP momentum · 1h | momentum | 54.53 | -45.47 | 1019 | 21.3 | -57.56 | -11.77 | -60.99 | 1205 |
| 58 | Williams %R · 1h ⏸ | reversion | 53.97 | -46.03 | 480 | 37.7 | -55.19 | -9.14 | -55.96 | 587 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 51.76 | -48.24 | 234 | 31.6 | -46.02 | -6.78 | -49.45 | 276 |
| 60 | Three white soldiers | momentum | 51.50 | -48.50 | 626 | 14.5 | -52.29 | -22.22 | -53.11 | 672 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.29 | -9.41 | -54.76 | 683 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -47.65 | -99.15 | 5354 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.81 | -31.00 | -84.65 | 1417 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.56 | -47.43 | -94.67 | 2464 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.04 | -33.02 | -91.46 | 1951 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.83 | -42.95 | -92.03 | 2290 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.61 | -27.54 | -89.93 | 2007 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.21 | -47.05 | -98.22 | 3490 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -54.35 | -97.01 | 3414 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.91 | -41.26 | -93.95 | 2189 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.71 | -35.62 | -83.94 | 1588 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -53.81 | -99.65 | 6341 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.00 | -41.69 | -93.06 | 2537 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.43 | -36.91 | -94.47 | 3138 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -63.61 | -99.84 | 6281 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.39 | -43.99 | -93.40 | 2285 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.31 | -24.49 | -79.76 | 1650 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.85 | -59.03 | -97.88 | 3387 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -56.25 | -99.14 | 5115 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.78 | -28.88 | -71.03 | 1232 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.94 | -50.26 | -94.99 | 2730 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.13 | -6.43 | -49.04 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.67 | -38.38 | -85.90 | 1711 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.74 | -72.41 | -99.75 | 6565 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.39 | -30.41 | -91.56 | 2480 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.61 | -19.59 | -82.83 | 1956 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.66 | -33.22 | -92.79 | 2208 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.01 | -47.27 | -98.02 | 4060 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.24 | -49.35 | -90.34 | 2208 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.29 | -31.03 | -67.54 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.73 | -27.60 | -74.90 | 1202 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.02 | -19.44 | -84.38 | 1866 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.79 | -46.90 | -97.81 | 4452 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -95.83 | -99.94 | 8431 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-21T08:00 | VWAP momentum · 1h | buy | XRP-USD | 4.18 | — | entry signal |
| 2026-11-21T08:00 | VWAP momentum · 1h | buy | SOL-USD | 9.08 | — | entry signal |
| 2026-11-21T08:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.08 | — | entry signal |
| 2026-11-21T08:00 | VWAP momentum · 1h | buy | BTC-USD | 9.08 | — | entry signal |
| 2026-11-21T08:00 | VWAP momentum · 1h | sell | ETH-USD | 4.43 | -0.05 | rebalance down |
| 2026-11-21T07:50 | Three white soldiers | sell | ETH-USD | 10.30 | 0.02 | exit signal |
| 2026-11-21T07:50 | Three white soldiers | sell | BTC-USD | 10.33 | 0.05 | exit signal |
| 2026-11-21T07:45 | Three white soldiers | sell | XRP-USD | 10.31 | 0.04 | exit signal |
| 2026-11-21T07:45 | Three white soldiers | sell | SOL-USD | 10.27 | -0.01 | exit signal |
| 2026-11-21T07:45 | Three white soldiers | sell | DOGE-USD | 10.29 | 0.02 | exit signal |
| 2026-11-21T07:00 | MFI reversion · 1h | buy | BTC-USD | 15.87 | — | entry signal |
| 2026-11-21T07:00 | CCI reversion · 1h | buy | XRP-USD | 14.90 | — | entry signal |
| 2026-11-21T07:00 | CCI reversion · 1h | buy | SOL-USD | 14.90 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-23 09:50:05.000175+00:00 -> 2026-11-21 10:00:05.000175+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
