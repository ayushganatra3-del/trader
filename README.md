# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-21T14:20:05.000115+00:00 · 68211 ticks

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

Today: 11490 decisions in 2298 calls, $0.1607 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-21T14:20 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-21T14:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-21T14:20 | 2 / 3 / 0 | ETH-USD 55% |  |

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
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.82 | -3.91 | -5.40 | 76 |
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
| 25 | Parabolic SAR · 1h | trend | 84.90 | -15.10 | 194 | 27.8 | -22.78 | -6.09 | -27.68 | 190 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -24.07 | -6.68 | -27.44 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -19.61 | -9.31 | -21.16 | 69 |
| 28 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 126 | 26.2 | -22.11 | -6.25 | -25.15 | 140 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.04 | -5.13 | -21.68 | 204 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.82 | -4.05 | -18.47 | 93 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.44 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -28.01 | -7.61 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.75 | -25.25 | 228 | 20.2 | -30.73 | -5.72 | -35.87 | 274 |
| 35 | Supertrend · 1h | trend | 73.47 | -26.53 | 198 | 16.7 | -33.10 | -6.40 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.96 | -3.42 | -58.28 | 39 |
| 37 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -33.07 | -7.96 | -37.57 | 171 |
| 38 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.74 | -9.72 | -40.64 | 122 |
| 39 | Bollinger breakout · 1h | breakout | 72.50 | -27.50 | 195 | 21.5 | -32.12 | -8.27 | -35.72 | 213 |
| 40 | Heikin-Ashi · 1h | trend | 70.71 | -29.29 | 487 | 22.8 | -42.62 | -8.55 | -47.85 | 616 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | RSI momentum · 1h | momentum | 70.35 | -29.66 | 184 | 14.1 | -37.11 | -8.09 | -40.55 | 203 |
| 43 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -37.22 | -9.34 | -41.80 | 236 |
| 44 | Hold BTC | benchmark | 69.67 | -30.32 | 3 | 0.0 | -25.81 | -4.11 | -36.23 | 1 |
| 45 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Donchian 20/10 · 1h | breakout | 66.93 | -33.07 | 165 | 17.6 | -38.50 | -8.31 | -43.13 | 196 |
| 49 | Stochastic reversion · 1h | reversion | 66.71 | -33.30 | 383 | 39.9 | -43.42 | -6.19 | -44.08 | 447 |
| 50 | ROC + volume · 1h | momentum | 66.14 | -33.85 | 431 | 27.6 | -39.76 | -8.06 | -43.31 | 342 |
| 51 | MFI reversion · 1h | reversion | 64.96 | -35.04 | 481 | 32.6 | -35.65 | -5.27 | -39.46 | 179 |
| 52 | EMA 9/21 cross · 1h | trend | 64.61 | -35.39 | 291 | 11.3 | -42.58 | -9.91 | -46.01 | 319 |
| 53 | MACD cross · 1h | trend | 63.30 | -36.70 | 446 | 20.9 | -49.05 | -9.69 | -50.91 | 502 |
| 54 | CCI reversion · 1h ⏸ | reversion | 58.33 | -41.67 | 423 | 39.5 | -47.77 | -7.86 | -51.36 | 489 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.73 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.93 | -44.07 | 1019 | 21.3 | -55.99 | -11.03 | -60.93 | 1201 |
| 57 | Agent (ML meta-label) | meta | 55.24 | -44.76 | 2017 | 24.7 | -33.73 | -5.75 | -36.00 | 344 |
| 58 | Williams %R · 1h ⏸ | reversion | 53.97 | -46.03 | 480 | 37.7 | -54.46 | -9.06 | -55.96 | 587 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.01 | -6.48 | -49.45 | 276 |
| 60 | Three white soldiers | momentum | 51.28 | -48.72 | 628 | 14.5 | -52.21 | -22.56 | -53.02 | 670 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.48 | -8.68 | -54.45 | 686 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -45.48 | -99.15 | 5343 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.54 | -30.22 | -84.65 | 1414 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.43 | -44.80 | -94.64 | 2461 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.72 | -30.51 | -91.46 | 1949 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.63 | -39.16 | -92.04 | 2287 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.20 | -26.60 | -89.78 | 1991 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.10 | -43.79 | -98.19 | 3472 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -54.76 | -96.94 | 3409 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.49 | -39.66 | -93.68 | 2164 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.46 | -35.02 | -83.83 | 1584 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -54.22 | -99.65 | 6331 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.66 | -38.09 | -93.01 | 2532 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.35 | -37.07 | -94.37 | 3123 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -62.69 | -99.84 | 6273 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.35 | -44.18 | -93.35 | 2277 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.99 | -23.66 | -79.73 | 1654 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -56.67 | -97.84 | 3381 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.12 | -56.26 | -99.13 | 5111 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.19 | -27.20 | -71.00 | 1230 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -46.07 | -94.94 | 2724 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.60 | -6.19 | -49.04 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.33 | -36.55 | -85.86 | 1711 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.74 | -72.49 | -99.74 | 6557 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.38 | -30.44 | -91.55 | 2480 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.53 | -19.59 | -82.79 | 1951 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.63 | -33.13 | -92.79 | 2206 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.01 | -47.27 | -98.02 | 4060 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.99 | -44.36 | -90.34 | 2208 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.13 | -31.13 | -67.72 | 802 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -26.62 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.98 | -19.36 | -84.35 | 1859 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.79 | -46.91 | -97.81 | 4451 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -100.20 | -99.94 | 8423 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-21T14:15 | Agent (ML meta-label) | sell | XRP-USD | 3.79 | 0.13 | selected signal exited |
| 2026-11-21T14:10 | Three white soldiers | sell | XRP-USD | 12.74 | -0.11 | exit signal |
| 2026-11-21T14:00 | Bollinger breakout · 1h | buy | XRP-USD | 8.72 | — | entry signal |
| 2026-11-21T14:00 | Bollinger breakout · 1h | buy | SOL-USD | 14.59 | — | entry signal |
| 2026-11-21T14:00 | Bollinger breakout · 1h | buy | ETH-USD | 14.59 | — | entry signal |
| 2026-11-21T14:00 | Bollinger breakout · 1h | buy | BTC-USD | 14.59 | — | entry signal |
| 2026-11-21T14:00 | Donchian 20/10 · 1h | buy | XRP-USD | 3.56 | — | entry signal |
| 2026-11-21T14:00 | Donchian 20/10 · 1h | buy | SOL-USD | 11.22 | — | entry signal |
| 2026-11-21T14:00 | Donchian 20/10 · 1h | buy | ETH-USD | 11.22 | — | entry signal |
| 2026-11-21T14:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 11.22 | — | entry signal |
| 2026-11-21T14:00 | Donchian 20/10 · 1h | buy | BTC-USD | 11.22 | — | entry signal |
| 2026-11-21T14:00 | RSI momentum · 1h | buy | ETH-USD | 17.68 | — | entry signal |
| 2026-11-21T14:00 | RSI momentum · 1h | buy | BTC-USD | 17.68 | — | entry signal |
| 2026-11-21T14:00 | ROC + volume · 1h | buy | SOL-USD | 16.60 | — | entry signal |
| 2026-11-21T14:00 | ROC + volume · 1h | buy | BTC-USD | 16.60 | — | entry signal |
| 2026-11-21T14:00 | ADX DI cross · 1h | buy | XRP-USD | 7.12 | — | entry signal |
| 2026-11-21T14:00 | ADX DI cross · 1h | buy | SOL-USD | 12.54 | — | entry signal |
| 2026-11-21T14:00 | ADX DI cross · 1h | buy | DOGE-USD | 12.54 | — | entry signal |
| 2026-11-21T14:00 | ADX DI cross · 1h | buy | BTC-USD | 12.54 | — | entry signal |
| 2026-11-21T14:00 | ADX DI cross · 1h | sell | ETH-USD | 6.62 | 0.15 | rebalance down |
| 2026-11-21T14:00 | Supertrend · 1h | buy | XRP-USD | 3.39 | — | entry signal |
| 2026-11-21T14:00 | Supertrend · 1h | buy | SOL-USD | 12.31 | — | entry signal |
| 2026-11-21T14:00 | Supertrend · 1h | buy | DOGE-USD | 12.31 | — | entry signal |
| 2026-11-21T14:00 | Supertrend · 1h | sell | ETH-USD | 6.39 | 0.15 | rebalance down |
| 2026-11-21T14:00 | Supertrend · 1h | sell | BTC-USD | 6.38 | 0.14 | rebalance down |
| 2026-11-21T14:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 16.20 | — | entry signal |
| 2026-11-21T13:40 | Agent (ML meta-label) | sell | DOGE-USD | 3.89 | 0.24 | selected signal exited |
| 2026-11-21T13:40 | Three white soldiers | buy | XRP-USD | 12.85 | — | entry signal |
| 2026-11-21T13:20 | Agent (ML meta-label) | sell | SOL-USD | 1.49 | 0.07 | selected signal exited |
| 2026-11-21T13:00 | Stochastic reversion · 1h | sell | DOGE-USD | 4.61 | 0.19 | exit signal |
| 2026-11-21T13:00 | Supertrend · 1h | buy | BTC-USD | 18.25 | — | entry signal |
| 2026-11-21T12:01 | Heikin-Ashi · 1h | buy | XRP-USD | 3.47 | — | rebalance up |
| 2026-11-21T12:01 | Heikin-Ashi · 1h | sell | BTC-USD | 3.47 | -0.00 | rebalance down |
| 2026-11-21T12:00 | Bollinger reversion · 1h | sell | SOL-USD | 2.85 | 0.10 | exit signal |
| 2026-11-21T12:00 | Heikin-Ashi · 1h | buy | XRP-USD | 4.07 | — | entry signal |
| 2026-11-21T12:00 | Heikin-Ashi · 1h | buy | SOL-USD | 13.90 | — | entry signal |
| 2026-11-21T12:00 | Heikin-Ashi · 1h | sell | ETH-USD | 3.62 | 0.03 | rebalance down |
| 2026-11-21T12:00 | ADX DI cross · 1h | buy | ETH-USD | 18.68 | — | entry signal |
| 2026-11-21T12:00 | Supertrend · 1h | buy | ETH-USD | 18.23 | — | entry signal |
| 2026-11-21T11:00 | Heikin-Ashi · 1h | buy | BTC-USD | 17.34 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-23 14:20:05.000115+00:00 -> 2026-11-21 14:30:05.000115+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
