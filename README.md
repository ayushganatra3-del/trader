# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-21T07:50:05.000119+00:00 · 67873 ticks

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

Today: 6420 decisions in 1284 calls, $0.0899 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-21T07:50 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-21T07:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-21T07:50 | 1 / 4 / 0 | cash |  |

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
| 25 | Parabolic SAR · 1h | trend | 84.90 | -15.10 | 194 | 27.8 | -22.90 | -6.13 | -28.66 | 194 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -24.07 | -6.68 | -27.44 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.49 | -6.51 | -21.29 | 71 |
| 28 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 126 | 26.2 | -19.32 | -4.72 | -25.26 | 142 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.04 | -5.13 | -21.68 | 204 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.82 | -4.05 | -18.47 | 93 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.44 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -28.01 | -7.61 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.72 | -25.28 | 228 | 20.2 | -30.72 | -5.72 | -35.87 | 269 |
| 35 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.96 | -3.42 | -58.28 | 39 |
| 36 | Bollinger breakout · 1h | breakout | 72.97 | -27.03 | 195 | 21.5 | -30.70 | -7.41 | -36.25 | 213 |
| 37 | Supertrend · 1h | trend | 72.93 | -27.07 | 198 | 16.7 | -33.54 | -6.53 | -37.64 | 199 |
| 38 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -33.09 | -8.00 | -37.33 | 171 |
| 39 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.74 | -9.72 | -40.64 | 122 |
| 40 | RSI momentum · 1h | momentum | 70.70 | -29.30 | 184 | 14.1 | -37.01 | -8.01 | -40.93 | 201 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -36.64 | -9.33 | -41.21 | 237 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 44 | Heikin-Ashi · 1h | trend | 69.27 | -30.73 | 487 | 22.8 | -44.68 | -9.31 | -47.85 | 615 |
| 45 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 47 | Donchian 20/10 · 1h | breakout | 67.34 | -32.66 | 165 | 17.6 | -36.69 | -7.51 | -43.26 | 191 |
| 48 | Hold BTC | benchmark | 66.94 | -33.06 | 3 | 0.0 | -28.23 | -4.73 | -36.23 | 1 |
| 49 | Stochastic reversion · 1h | reversion | 66.62 | -33.38 | 382 | 39.8 | -43.50 | -6.20 | -44.08 | 447 |
| 50 | ROC + volume · 1h | momentum | 66.42 | -33.58 | 431 | 27.6 | -38.93 | -7.68 | -43.29 | 340 |
| 51 | EMA 9/21 cross · 1h | trend | 64.80 | -35.20 | 291 | 11.3 | -42.42 | -9.85 | -46.01 | 318 |
| 52 | MFI reversion · 1h | reversion | 63.06 | -36.94 | 481 | 32.6 | -37.51 | -5.62 | -39.46 | 179 |
| 53 | MACD cross · 1h | trend | 61.39 | -38.61 | 446 | 20.9 | -51.02 | -10.29 | -51.34 | 499 |
| 54 | CCI reversion · 1h | reversion | 58.75 | -41.25 | 418 | 40.0 | -49.83 | -8.14 | -50.87 | 488 |
| 55 | Bollinger reversion · 1h | reversion | 57.85 | -42.15 | 381 | 36.2 | -44.61 | -6.74 | -45.42 | 445 |
| 56 | Agent (ML meta-label) | meta | 54.90 | -45.10 | 2013 | 24.5 | -32.37 | -5.68 | -33.97 | 331 |
| 57 | VWAP momentum · 1h | momentum | 54.45 | -45.55 | 1018 | 21.3 | -57.48 | -11.74 | -60.93 | 1201 |
| 58 | Williams %R · 1h | reversion | 54.30 | -45.70 | 475 | 38.1 | -55.46 | -9.16 | -55.58 | 587 |
| 59 | RSI(14) reversion · 1h | reversion | 52.36 | -47.64 | 229 | 32.3 | -46.34 | -6.81 | -49.01 | 276 |
| 60 | Three white soldiers | momentum | 51.50 | -48.50 | 626 | 14.5 | -52.27 | -22.25 | -53.01 | 671 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.26 | -9.48 | -54.46 | 684 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -47.44 | -99.16 | 5356 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.32 | -28.13 | -84.61 | 1420 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.60 | -47.21 | -94.62 | 2467 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.01 | -32.89 | -91.46 | 1954 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.86 | -41.82 | -92.08 | 2293 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.78 | -27.63 | -90.10 | 2012 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.21 | -46.87 | -98.23 | 3488 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -55.58 | -96.91 | 3407 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.90 | -41.11 | -93.94 | 2188 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.58 | -35.38 | -83.75 | 1584 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -54.18 | -99.66 | 6345 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.05 | -41.52 | -93.12 | 2540 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.50 | -36.63 | -94.54 | 3147 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -63.80 | -99.84 | 6283 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.46 | -43.98 | -93.46 | 2288 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.43 | -24.59 | -79.73 | 1651 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.86 | -59.01 | -97.86 | 3386 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -56.18 | -99.14 | 5114 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.80 | -28.64 | -71.03 | 1234 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.96 | -49.63 | -95.03 | 2734 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.46 | -48.68 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.74 | -37.99 | -85.97 | 1716 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.74 | -72.39 | -99.75 | 6561 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.38 | -30.44 | -91.55 | 2480 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.55 | -19.59 | -82.79 | 1953 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.71 | -33.24 | -92.83 | 2209 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.01 | -47.24 | -98.02 | 4057 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.20 | -47.57 | -90.40 | 2207 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.29 | -31.03 | -67.54 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.79 | -27.50 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.03 | -19.39 | -84.39 | 1861 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.80 | -46.89 | -97.82 | 4453 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -92.24 | -99.94 | 8424 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-21T07:50 | Three white soldiers | sell | ETH-USD | 10.30 | 0.02 | exit signal |
| 2026-11-21T07:50 | Three white soldiers | sell | BTC-USD | 10.33 | 0.05 | exit signal |
| 2026-11-21T07:45 | Three white soldiers | sell | XRP-USD | 10.31 | 0.04 | exit signal |
| 2026-11-21T07:45 | Three white soldiers | sell | SOL-USD | 10.27 | -0.01 | exit signal |
| 2026-11-21T07:45 | Three white soldiers | sell | DOGE-USD | 10.29 | 0.02 | exit signal |
| 2026-11-21T07:00 | MFI reversion · 1h | buy | BTC-USD | 15.87 | — | entry signal |
| 2026-11-21T07:00 | CCI reversion · 1h | buy | XRP-USD | 14.90 | — | entry signal |
| 2026-11-21T07:00 | CCI reversion · 1h | buy | SOL-USD | 14.90 | — | entry signal |
| 2026-11-21T07:00 | CCI reversion · 1h | buy | ETH-USD | 14.90 | — | entry signal |
| 2026-11-21T07:00 | CCI reversion · 1h | buy | DOGE-USD | 14.90 | — | entry signal |
| 2026-11-21T07:00 | Williams %R · 1h | buy | XRP-USD | 11.00 | — | entry signal |
| 2026-11-21T07:00 | Williams %R · 1h | buy | SOL-USD | 11.00 | — | entry signal |
| 2026-11-21T07:00 | Williams %R · 1h | buy | ETH-USD | 11.00 | — | entry signal |
| 2026-11-21T07:00 | Williams %R · 1h | buy | DOGE-USD | 11.00 | — | entry signal |
| 2026-11-21T07:00 | Williams %R · 1h | buy | BTC-USD | 11.00 | — | entry signal |
| 2026-11-21T07:00 | Stochastic reversion · 1h | sell | ETH-USD | 4.61 | 0.19 | exit signal |
| 2026-11-21T07:00 | RSI(14) reversion · 1h | buy | XRP-USD | 10.61 | — | entry signal |
| 2026-11-21T07:00 | RSI(14) reversion · 1h | buy | SOL-USD | 10.61 | — | entry signal |
| 2026-11-21T07:00 | RSI(14) reversion · 1h | buy | ETH-USD | 10.61 | — | entry signal |
| 2026-11-21T07:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 10.61 | — | entry signal |
| 2026-11-21T07:00 | RSI(14) reversion · 1h | buy | BTC-USD | 10.61 | — | entry signal |
| 2026-11-21T07:00 | VWAP momentum · 1h | buy | ETH-USD | 13.65 | — | entry signal |
| 2026-11-21T07:00 | MACD cross · 1h | buy | ETH-USD | 15.39 | — | entry signal |
| 2026-11-21T06:45 | Three white soldiers | buy | XRP-USD | 10.28 | — | entry signal |
| 2026-11-21T06:45 | Three white soldiers | buy | SOL-USD | 10.28 | — | entry signal |
| 2026-11-21T06:45 | Three white soldiers | buy | ETH-USD | 10.28 | — | entry signal |
| 2026-11-21T06:45 | Three white soldiers | buy | DOGE-USD | 10.28 | — | entry signal |
| 2026-11-21T06:45 | Three white soldiers | buy | BTC-USD | 10.28 | — | entry signal |
| 2026-11-21T06:20 | Agent (ML meta-label) | buy | SOL-USD | 1.43 | — | entry |
| 2026-11-21T06:20 | Agent (ML meta-label) | buy | ETH-USD | 3.65 | — | entry |
| 2026-11-21T06:20 | Agent (ML meta-label) | buy | DOGE-USD | 3.65 | — | entry |
| 2026-11-21T06:05 | Agent (ML meta-label) | sell | SOL-USD | 4.51 | -0.06 | selected signal exited |
| 2026-11-21T06:05 | Agent (ML meta-label) | sell | DOGE-USD | 3.87 | -0.04 | selected signal exited |
| 2026-11-21T06:00 | MFI reversion · 1h | buy | XRP-USD | 15.57 | — | entry signal |
| 2026-11-21T06:00 | MFI reversion · 1h | buy | ETH-USD | 15.57 | — | entry signal |
| 2026-11-21T06:00 | Stochastic reversion · 1h | buy | ETH-USD | 4.42 | — | entry signal |
| 2026-11-21T06:00 | Stochastic reversion · 1h | buy | DOGE-USD | 4.42 | — | entry signal |
| 2026-11-21T05:45 | Agent (ML meta-label) | buy | DOGE-USD | 3.91 | — | entry |
| 2026-11-21T05:20 | Agent (ML meta-label) | buy | SOL-USD | 3.03 | — | rebalance up |
| 2026-11-21T05:20 | Agent (ML meta-label) | sell | ETH-USD | 3.64 | -0.02 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-23 07:50:05.000119+00:00 -> 2026-11-21 08:00:05.000119+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
