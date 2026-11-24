# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T23:10:05.000153+00:00 · 72349 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.44 (-21.56%)

Closed trades 244, win rate 36.1%, fees £6.57, max drawdown -22.02%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-24 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, BH 12%, FUN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.39 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 42807 decisions in 3627 calls, $0.5308 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T23:10 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-24T23:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-24T23:10 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |
| Opening range 30m | SQQQ | 1.57 | +20.80% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.59 | 15.59 | 0 | — | 13.68 | 4.63 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.73 | 4.73 | 0 | — | 5.25 | 1.43 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.12 | 0.05 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.36 | -3.64 | 229 | 28.4 | -1.65 | -0.49 | -7.61 | 142 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.72 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.39 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.37 | -5.63 | 0 | — | -6.20 | -1.58 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 94.06 | -5.95 | 20 | 10.0 | -4.59 | -7.46 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.65 | -7.35 | 0 | — | -7.92 | -1.60 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 92.45 | -7.55 | 61 | 41.0 | -6.79 | -1.23 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.10 | -8.90 | 116 | 24.1 | -8.02 | -4.03 | -10.94 | 40 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.58 | -10.42 | 0 | — | -11.39 | -2.46 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.48 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.58 | -13.42 | 167 | 46.1 | -11.07 | -2.03 | -20.49 | 154 |
| 21 | Opening range 30m | breakout | 85.41 | -14.59 | 473 | 32.8 | -12.69 | -4.28 | -13.73 | 543 |
| 22 | Daily: Bullish score | daily | 85.37 | -14.62 | 20 | 20.0 | -13.12 | -2.91 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.17 | -7.39 | -21.55 | 75 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.53 | -6.46 | -14.68 | 65 |
| 26 | Parabolic SAR · 1h | trend | 78.99 | -21.01 | 206 | 28.2 | -32.04 | -8.42 | -32.72 | 184 |
| 27 | Agent | meta | 78.44 | -21.56 | 244 | 36.1 | -26.25 | -5.97 | -26.53 | 196 |
| 28 | Volume breakout · 1h | breakout | 78.42 | -21.58 | 169 | 27.8 | -21.81 | -6.58 | -23.66 | 71 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 77.02 | -22.98 | 138 | 24.6 | -24.69 | -6.38 | -27.01 | 148 |
| 31 | Opening range 15m | breakout | 76.71 | -23.29 | 592 | 30.7 | -21.85 | -6.77 | -22.57 | 670 |
| 32 | Donchian 55/20 · 1h | breakout | 76.40 | -23.60 | 87 | 13.8 | -29.20 | -7.82 | -29.68 | 82 |
| 33 | Ichimoku · 1h | trend | 74.83 | -25.18 | 113 | 15.9 | -29.47 | -7.53 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.57 | -29.43 | 260 | 19.2 | -37.07 | -7.03 | -38.49 | 291 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.80 | -36.38 | 24 |
| 36 | Hold BTC | benchmark | 69.32 | -30.68 | 3 | 0.0 | -29.13 | -5.23 | -36.10 | 1 |
| 37 | Bollinger breakout · 1h | breakout | 69.28 | -30.72 | 208 | 22.1 | -30.94 | -8.05 | -33.57 | 207 |
| 38 | Supertrend · 1h | trend | 68.89 | -31.11 | 207 | 18.4 | -36.58 | -7.25 | -37.75 | 208 |
| 39 | Triple EMA stack · 1h | trend | 68.48 | -31.52 | 169 | 15.4 | -39.07 | -9.99 | -39.44 | 173 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 67.99 | -32.01 | 3 | 0.0 | -25.78 | -3.22 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.81 | -32.19 | 124 | 9.7 | -37.95 | -10.16 | -39.04 | 111 |
| 42 | OBV trend · 1h | momentum | 66.64 | -33.36 | 323 | 19.8 | -39.59 | -10.00 | -40.70 | 228 |
| 43 | RSI momentum · 1h | momentum | 65.68 | -34.32 | 200 | 15.0 | -40.17 | -9.23 | -41.95 | 196 |
| 44 | Heikin-Ashi · 1h | trend | 64.79 | -35.22 | 542 | 22.0 | -48.01 | -9.78 | -49.69 | 627 |
| 45 | MACD zero-line · 1h | trend | 64.54 | -35.46 | 199 | 16.6 | -34.06 | -9.28 | -34.73 | 198 |
| 46 | Max aggression: 1-day momentum | meta | 64.12 | -35.88 | 34 | 26.5 | -55.97 | -4.17 | -60.68 | 38 |
| 47 | Stochastic reversion · 1h | reversion | 63.40 | -36.60 | 400 | 40.5 | -35.14 | -3.82 | -42.69 | 432 |
| 48 | ROC + volume · 1h | momentum | 63.03 | -36.97 | 456 | 27.0 | -41.74 | -8.15 | -43.11 | 340 |
| 49 | Donchian 20/10 · 1h | breakout | 62.32 | -37.68 | 181 | 17.7 | -40.71 | -9.06 | -42.38 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 61.90 | -38.10 | 26 | 34.6 | -63.25 | -4.19 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.37 | -39.63 | 310 | 12.3 | -43.92 | -10.30 | -45.77 | 330 |
| 52 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.66 | -5.09 | -35.72 | 188 |
| 53 | MACD cross · 1h | trend | 58.14 | -41.85 | 478 | 20.9 | -52.80 | -10.73 | -54.25 | 502 |
| 54 | Agent (ML meta-label) | meta | 56.65 | -43.35 | 2072 | 25.4 | -25.01 | -3.23 | -34.14 | 322 |
| 55 | CCI reversion · 1h | reversion | 56.11 | -43.89 | 444 | 39.4 | -51.66 | -8.83 | -52.59 | 494 |
| 56 | Bollinger reversion · 1h | reversion | 55.92 | -44.08 | 392 | 37.5 | -39.26 | -4.74 | -45.42 | 424 |
| 57 | VWAP momentum · 1h | momentum | 53.47 | -46.53 | 1077 | 21.5 | -58.33 | -13.07 | -59.87 | 1175 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.62 | -8.53 | -53.17 | 687 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.80 | -9.29 | -56.43 | 591 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -49.62 | -99.14 | 5357 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.71 | -33.21 | -83.80 | 1417 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.44 | -50.96 | -94.45 | 2437 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.73 | -32.45 | -90.78 | 1904 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.76 | -42.15 | -91.78 | 2238 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.72 | -28.99 | -89.81 | 1965 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -49.80 | -98.19 | 3444 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -56.23 | -96.95 | 3330 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.86 | -36.32 | -92.91 | 2063 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.95 | -36.84 | -83.01 | 1540 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -57.55 | -99.68 | 6274 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.17 | -39.51 | -93.19 | 2498 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.35 | -36.86 | -94.36 | 3171 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.81 | -99.82 | 6107 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.22 | -45.04 | -93.24 | 2265 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.65 | -22.36 | -51.70 | 642 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.27 | -23.82 | -78.31 | 1612 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -58.75 | -97.75 | 3278 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -61.55 | -99.17 | 5144 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.20 | -27.71 | -71.59 | 1211 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.85 | -49.04 | -94.88 | 2673 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.73 | -6.57 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.11 | -37.04 | -85.33 | 1662 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -76.16 | -99.76 | 6536 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.50 | -31.26 | -91.66 | 2464 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.91 | -20.38 | -83.27 | 1950 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.77 | -31.76 | -91.89 | 2172 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.16 | -50.02 | -98.17 | 4071 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.30 | -48.00 | -90.33 | 2201 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.56 | -29.99 | -68.56 | 796 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.15 | -28.34 | -73.26 | 1162 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.97 | -19.25 | -84.31 | 1815 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -50.75 | -98.07 | 4425 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.26 | -99.94 | 8262 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.61 | -7.35 | -50.46 | 306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T23:00 | MACD cross · 1h | buy | ETH-USD | 4.47 | — | entry signal |
| 2026-11-24T23:00 | MACD cross · 1h | buy | BTC-USD | 4.47 | — | entry signal |
| 2026-11-24T21:01 | CCI reversion · 1h | buy | SOL-USD | 3.30 | — | entry signal |
| 2026-11-24T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 89.28 | -1.31 | target is flat |
| 2026-11-24T20:55 | Agent (ML meta-label) | buy | SQQQ | 6.12 | — | rebalance up |
| 2026-11-24T20:55 | Agent (ML meta-label) | buy | MSTR | 6.11 | — | rebalance up |
| 2026-11-24T20:55 | Agent (ML meta-label) | buy | ETHU | 6.07 | — | rebalance up |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | TECL | 8.15 | 0.04 | selected signal exited |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | MSFT | 8.12 | 0.00 | selected signal exited |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | COIN | 8.10 | -0.00 | selected signal exited |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | AMD | 8.12 | 0.01 | selected signal exited |
| 2026-11-24T20:55 | Opening range 30m | sell | TNA | 21.26 | -0.02 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 30m | sell | MSFT | 21.14 | -0.08 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 30m | sell | LABU | 17.71 | 0.90 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 30m | sell | IWM | 21.31 | -0.02 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | UPRO | 10.19 | -0.01 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | TNA | 11.66 | 0.02 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | SPY | 10.92 | -0.01 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | MSFT | 10.82 | 0.01 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | LABU | 11.29 | 0.57 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | IWM | 10.93 | -0.00 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | AAPL | 10.89 | 0.00 | end-of-day flatten |
| 2026-11-24T20:50 | Agent (ML meta-label) | buy | TECL | 8.11 | — | entry |
| 2026-11-24T20:50 | Agent (ML meta-label) | buy | MSFT | 8.12 | — | entry |
| 2026-11-24T20:50 | Agent (ML meta-label) | buy | AMD | 8.12 | — | entry |
| 2026-11-24T20:50 | Agent (ML meta-label) | sell | SQQQ | 3.22 | -0.03 | rebalance down |
| 2026-11-24T20:50 | Agent (ML meta-label) | sell | MSTR | 6.04 | -0.14 | rebalance down |
| 2026-11-24T20:50 | Agent (ML meta-label) | sell | ETHU | 6.04 | -0.18 | rebalance down |
| 2026-11-24T20:50 | Agent (ML meta-label) | sell | COIN | 6.08 | 0.01 | rebalance down |
| 2026-11-24T20:45 | ROC + volume · 1h | buy | TNA | 15.67 | — | entry |
| 2026-11-24T20:45 | VWAP momentum · 1h | buy | TSLA | 2.69 | — | rebalance up |
| 2026-11-24T20:45 | VWAP momentum · 1h | buy | IWM | 2.68 | — | rebalance up |
| 2026-11-24T20:45 | VWAP momentum · 1h | sell | TNA | 10.65 | -0.02 | target is flat |
| 2026-11-24T20:45 | VWAP momentum · 1h | sell | AMD | 10.69 | -0.03 | target is flat |
| 2026-11-24T20:40 | Agent (ML meta-label) | buy | COIN | 14.17 | — | entry |
| 2026-11-24T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 90.60 | — | entry |
| 2026-11-24T20:30 | ROC + volume · 1h | buy | LABU | 5.08 | — | rebalance up |
| 2026-11-24T20:30 | ROC + volume · 1h | buy | IWM | 5.24 | — | rebalance up |
| 2026-11-24T20:30 | ROC + volume · 1h | buy | AAPL | 5.25 | — | rebalance up |
| 2026-11-24T20:30 | ROC + volume · 1h | sell | TSLA | 10.44 | -0.17 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 23:10:05.000153+00:00 -> 2026-11-24 23:20:05.000153+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
