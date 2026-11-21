# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-21T05:50:05.000107+00:00 · 67757 ticks

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

Today: 4680 decisions in 936 calls, $0.0655 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-21T05:50 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-21T05:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-21T05:50 | 1 / 4 / 0 | ETH-USD 55% |  |

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
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 0.74 | 0.34 | -7.76 | 153 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -9.71 | -5.05 | -12.45 | 51 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.21 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -2.72 | -19.56 | 14 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.98 | -7.58 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -8.22 | -1.59 | -14.79 | 66 |
| 19 | VWAP reversion · 1h | reversion | 87.77 | -12.23 | 160 | 45.0 | -14.66 | -4.24 | -20.40 | 156 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.47 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -3.84 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.78 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.90 | -15.10 | 194 | 27.8 | -22.90 | -6.13 | -28.66 | 194 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.98 | -6.67 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.49 | -6.51 | -21.29 | 71 |
| 28 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 126 | 26.2 | -19.21 | -4.66 | -25.26 | 142 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.04 | -5.13 | -21.68 | 204 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.82 | -4.05 | -18.47 | 93 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.44 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -28.01 | -7.61 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.72 | -25.28 | 228 | 20.2 | -30.72 | -5.72 | -35.87 | 269 |
| 35 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.96 | -3.42 | -58.28 | 39 |
| 36 | Bollinger breakout · 1h | breakout | 72.97 | -27.03 | 195 | 21.5 | -30.70 | -7.41 | -36.25 | 213 |
| 37 | Supertrend · 1h | trend | 72.93 | -27.07 | 198 | 16.7 | -33.54 | -6.53 | -37.64 | 199 |
| 38 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -32.14 | -7.63 | -37.44 | 171 |
| 39 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.74 | -9.72 | -40.64 | 122 |
| 40 | RSI momentum · 1h | momentum | 70.70 | -29.30 | 184 | 14.1 | -36.98 | -7.88 | -41.77 | 202 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -36.20 | -9.14 | -41.21 | 237 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 44 | Heikin-Ashi · 1h | trend | 69.27 | -30.73 | 487 | 22.8 | -44.68 | -9.31 | -47.85 | 615 |
| 45 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 47 | Donchian 20/10 · 1h | breakout | 67.34 | -32.66 | 165 | 17.6 | -36.69 | -7.51 | -43.26 | 191 |
| 48 | ROC + volume · 1h | momentum | 66.42 | -33.58 | 431 | 27.6 | -36.68 | -6.37 | -43.29 | 340 |
| 49 | Stochastic reversion · 1h | reversion | 66.32 | -33.68 | 381 | 39.6 | -43.74 | -6.25 | -44.03 | 445 |
| 50 | EMA 9/21 cross · 1h | trend | 64.80 | -35.20 | 291 | 11.3 | -42.42 | -9.85 | -46.01 | 318 |
| 51 | Hold BTC | benchmark | 64.74 | -35.26 | 3 | 0.0 | -30.63 | -5.04 | -36.21 | 1 |
| 52 | MFI reversion · 1h | reversion | 62.29 | -37.71 | 481 | 32.6 | -38.28 | -5.74 | -39.28 | 176 |
| 53 | MACD cross · 1h | trend | 61.56 | -38.44 | 446 | 20.9 | -50.89 | -10.27 | -51.20 | 498 |
| 54 | CCI reversion · 1h | reversion | 59.61 | -40.39 | 418 | 40.0 | -49.10 | -8.08 | -50.15 | 484 |
| 55 | Bollinger reversion · 1h | reversion | 57.69 | -42.31 | 381 | 36.2 | -44.77 | -6.78 | -45.41 | 445 |
| 56 | Williams %R · 1h | reversion | 55.01 | -44.99 | 475 | 38.1 | -54.88 | -9.11 | -55.01 | 582 |
| 57 | Agent (ML meta-label) | meta | 54.74 | -45.26 | 2011 | 24.6 | -32.69 | -5.79 | -33.63 | 340 |
| 58 | VWAP momentum · 1h | momentum | 54.61 | -45.39 | 1018 | 21.3 | -57.36 | -11.70 | -60.93 | 1200 |
| 59 | RSI(14) reversion · 1h | reversion | 53.04 | -46.96 | 229 | 32.3 | -45.65 | -6.74 | -48.35 | 271 |
| 60 | Three white soldiers | momentum | 51.39 | -48.61 | 621 | 14.0 | -52.33 | -22.34 | -52.86 | 666 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -54.25 | -9.78 | -54.37 | 684 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.17 | -47.73 | -99.17 | 5357 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.55 | -30.25 | -84.29 | 1418 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.52 | -46.24 | -94.55 | 2461 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.20 | -33.62 | -91.44 | 1952 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.94 | -42.62 | -92.10 | 2290 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.72 | -27.61 | -90.10 | 2016 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.24 | -47.66 | -98.24 | 3489 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -54.46 | -96.86 | 3404 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.80 | -39.95 | -93.91 | 2185 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.51 | -34.78 | -83.57 | 1582 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -54.31 | -99.66 | 6349 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.13 | -42.45 | -93.14 | 2536 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.50 | -36.59 | -94.54 | 3146 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -66.93 | -99.84 | 6288 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.52 | -43.80 | -93.52 | 2288 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.54 | -24.84 | -79.73 | 1646 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.87 | -59.01 | -97.87 | 3389 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -56.93 | -99.14 | 5120 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.95 | -28.84 | -71.03 | 1231 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.05 | -51.40 | -95.06 | 2731 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -45.83 | -6.39 | -48.12 | 270 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.69 | -38.00 | -85.92 | 1708 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.75 | -72.37 | -99.75 | 6567 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.52 | -31.10 | -91.54 | 2482 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.90 | -19.59 | -82.99 | 1960 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.79 | -33.57 | -92.81 | 2208 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.01 | -47.22 | -98.03 | 4059 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.38 | -50.03 | -90.44 | 2203 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.33 | -31.13 | -67.49 | 793 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.72 | -27.34 | -74.90 | 1203 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.34 | -19.36 | -84.45 | 1867 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.81 | -46.93 | -97.82 | 4452 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.31 | -99.94 | 8427 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-21T05:45 | Agent (ML meta-label) | buy | DOGE-USD | 3.91 | — | entry |
| 2026-11-21T05:20 | Agent (ML meta-label) | buy | SOL-USD | 3.03 | — | rebalance up |
| 2026-11-21T05:20 | Agent (ML meta-label) | sell | ETH-USD | 3.64 | -0.02 | selected signal exited |
| 2026-11-21T05:20 | Agent (ML meta-label) | sell | DOGE-USD | 3.63 | -0.02 | selected signal exited |
| 2026-11-21T05:00 | Agent (ML meta-label) | buy | SOL-USD | 1.54 | — | entry |
| 2026-11-21T05:00 | Agent (ML meta-label) | buy | ETH-USD | 3.65 | — | entry |
| 2026-11-21T05:00 | Agent (ML meta-label) | buy | DOGE-USD | 3.65 | — | entry |
| 2026-11-21T05:00 | Bollinger reversion · 1h | buy | SOL-USD | 2.75 | — | entry signal |
| 2026-11-21T04:10 | Agent (ML meta-label) | sell | ETH-USD | 3.85 | -0.07 | selected signal exited |
| 2026-11-21T04:10 | Williams %R · 1h | sell | ETH-USD | 10.91 | -0.62 | stop-loss |
| 2026-11-21T04:10 | Stochastic reversion · 1h | sell | ETH-USD | 3.96 | -0.22 | stop-loss |
| 2026-11-21T04:05 | Agent (ML meta-label) | buy | ETH-USD | 3.92 | — | entry |
| 2026-11-21T03:45 | Agent (ML meta-label) | sell | BTC-USD | 3.55 | -0.13 | selected signal exited |
| 2026-11-21T03:45 | Stochastic reversion · 1h | sell | BTC-USD | 4.01 | -0.18 | stop-loss |
| 2026-11-21T03:45 | Bollinger reversion · 1h | sell | BTC-USD | 2.32 | -0.10 | stop-loss |
| 2026-11-21T03:40 | Agent (ML meta-label) | sell | ETH-USD | 3.54 | -0.12 | selected signal exited |
| 2026-11-21T03:35 | Agent (ML meta-label) | sell | SOL-USD | 1.83 | -0.06 | selected signal exited |
| 2026-11-21T03:35 | MFI reversion · 1h | sell | XRP-USD | 12.44 | -0.55 | stop-loss |
| 2026-11-21T03:35 | MFI reversion · 1h | sell | SOL-USD | 10.35 | -0.50 | stop-loss |
| 2026-11-21T03:35 | MFI reversion · 1h | sell | ETH-USD | 9.30 | -0.43 | stop-loss |
| 2026-11-21T03:35 | MFI reversion · 1h | sell | DOGE-USD | 12.34 | -0.63 | stop-loss |
| 2026-11-21T03:35 | MFI reversion · 1h | sell | BTC-USD | 12.50 | -0.49 | stop-loss |
| 2026-11-21T03:35 | CCI reversion · 1h | sell | XRP-USD | 11.93 | -0.53 | stop-loss |
| 2026-11-21T03:35 | CCI reversion · 1h | sell | SOL-USD | 11.90 | -0.56 | stop-loss |
| 2026-11-21T03:35 | CCI reversion · 1h | sell | ETH-USD | 11.93 | -0.53 | stop-loss |
| 2026-11-21T03:35 | CCI reversion · 1h | sell | DOGE-USD | 11.86 | -0.60 | stop-loss |
| 2026-11-21T03:35 | CCI reversion · 1h | sell | BTC-USD | 11.99 | -0.47 | stop-loss |
| 2026-11-21T03:35 | Williams %R · 1h | sell | XRP-USD | 11.03 | -0.49 | stop-loss |
| 2026-11-21T03:35 | Williams %R · 1h | sell | SOL-USD | 11.00 | -0.52 | stop-loss |
| 2026-11-21T03:35 | Williams %R · 1h | sell | DOGE-USD | 10.97 | -0.55 | stop-loss |
| 2026-11-21T03:35 | Williams %R · 1h | sell | BTC-USD | 11.09 | -0.43 | stop-loss |
| 2026-11-21T03:35 | Stochastic reversion · 1h | sell | DOGE-USD | 3.98 | -0.20 | stop-loss |
| 2026-11-21T03:35 | Z-score reversion · 1h | sell | XRP-USD | 9.98 | -0.45 | Kill switch: down 50% from peak |
| 2026-11-21T03:35 | Z-score reversion · 1h | sell | SOL-USD | 9.95 | -0.47 | Kill switch: down 50% from peak |
| 2026-11-21T03:35 | Z-score reversion · 1h | sell | ETH-USD | 8.30 | -0.37 | Kill switch: down 50% from peak |
| 2026-11-21T03:35 | Z-score reversion · 1h | sell | DOGE-USD | 9.92 | -0.50 | Kill switch: down 50% from peak |
| 2026-11-21T03:35 | Z-score reversion · 1h | sell | BTC-USD | 10.03 | -0.39 | Kill switch: down 50% from peak |
| 2026-11-21T03:35 | Bollinger reversion · 1h | sell | XRP-USD | 2.32 | -0.10 | stop-loss |
| 2026-11-21T03:35 | Bollinger reversion · 1h | sell | SOL-USD | 2.32 | -0.11 | stop-loss |
| 2026-11-21T03:35 | Bollinger reversion · 1h | sell | DOGE-USD | 2.31 | -0.12 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-23 05:50:05.000107+00:00 -> 2026-11-21 06:00:05.000107+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
