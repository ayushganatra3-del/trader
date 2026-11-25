# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T18:11:05.000160+00:00 · 73320 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.24 (-22.76%)

Closed trades 249, win rate 36.1%, fees £6.80, max drawdown -23.32%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 26.36 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 27582 decisions in 2784 calls, $0.3480 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T18:11 | 7 / 16 / 7 | MSTR 15% |  |
| Breezy | 2026-11-25T18:11 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-25T18:11 | 6 / 22 / 2 | MSTR 79% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| Bollinger reversion · 1h | ETH-USD | 1.78 | +4.64% | 7 |
| RSI(14) reversion · 1h | ETH-USD | 1.77 | +5.50% | 3 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 23.12 | 3.47 | -5.42 | 29 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.94 | 15.94 | 0 | — | 14.04 | 4.91 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.61 | 1.09 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.69 | 4.69 | 0 | — | 4.85 | 1.44 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.98 | -0.22 | -8.58 | 212 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.47 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | -0.45 | -0.06 | -6.21 | 167 |
| 12 | Hold SPY | benchmark | 93.49 | -6.51 | 0 | — | -7.32 | -1.87 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 92.57 | -7.43 | 21 | 9.5 | -6.32 | -6.83 | -6.44 | 19 |
| 14 | Trend pullback · 1h | trend | 92.51 | -7.49 | 116 | 24.1 | -5.45 | -2.64 | -9.95 | 36 |
| 15 | Copy: Insider buying | copy | 91.74 | -8.26 | 61 | 41.0 | -6.18 | -1.10 | -14.79 | 72 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 90.46 | -9.54 | 0 | — | -10.88 | -2.25 | -13.91 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 88.33 | -11.67 | 0 | — | -12.51 | -2.71 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.58 | -2.97 | -20.94 | 1 |
| 20 | Daily: Bullish score | daily | 86.72 | -13.28 | 20 | 20.0 | -11.77 | -2.67 | -19.56 | 14 |
| 21 | Opening range 30m | breakout | 85.77 | -14.22 | 478 | 32.4 | -12.04 | -4.01 | -15.61 | 550 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.79 | -2.38 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -16.51 | -6.06 | -16.51 | 69 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.91 | -13.02 | 61 |
| 26 | Opening range 15m | breakout | 77.55 | -22.45 | 601 | 30.3 | -21.36 | -6.45 | -24.95 | 683 |
| 27 | Agent | meta | 77.24 | -22.76 | 249 | 36.1 | -27.20 | -6.20 | -27.58 | 197 |
| 28 | Agent (aggressive) | meta | 76.74 | -23.26 | 114 | 33.3 | -17.00 | -4.44 | -18.44 | 91 |
| 29 | Volume breakout · 1h | breakout | 76.66 | -23.34 | 170 | 28.2 | -22.12 | -9.39 | -22.21 | 67 |
| 30 | Parabolic SAR · 1h | trend | 75.30 | -24.70 | 209 | 27.8 | -35.46 | -8.66 | -35.60 | 180 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.44 | -7.82 | -29.45 | 74 |
| 32 | Keltner breakout · 1h | breakout | 73.68 | -26.32 | 140 | 25.0 | -28.09 | -6.87 | -28.10 | 147 |
| 33 | Ichimoku · 1h | trend | 73.12 | -26.88 | 113 | 15.9 | -31.14 | -7.95 | -31.69 | 102 |
| 34 | Max aggression: 5-day momentum | meta | 72.12 | -27.88 | 27 | 37.0 | -57.88 | -3.24 | -67.33 | 23 |
| 35 | Daily: Momentum burst | daily | 70.59 | -29.41 | 31 | 16.1 | -33.60 | -4.76 | -36.38 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.54 | -30.46 | 264 | 18.9 | -39.57 | -7.75 | -40.10 | 271 |
| 37 | Hold BTC | benchmark | 69.11 | -30.89 | 3 | 0.0 | -29.58 | -5.24 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -31.77 | -8.31 | -32.19 | 203 |
| 39 | OBV trend · 1h | momentum | 66.76 | -33.24 | 324 | 19.8 | -38.89 | -9.46 | -40.59 | 225 |
| 40 | Supertrend · 1h | trend | 66.74 | -33.26 | 221 | 17.6 | -38.36 | -7.40 | -39.92 | 216 |
| 41 | EMA 20/50 cross · 1h | trend | 66.57 | -33.43 | 126 | 9.5 | -37.86 | -10.64 | -38.06 | 112 |
| 42 | Copy: Cathie Wood (ARKK) | copy | 66.54 | -33.45 | 3 | 0.0 | -27.90 | -3.57 | -33.66 | 1 |
| 43 | Triple EMA stack · 1h | trend | 65.46 | -34.54 | 171 | 15.2 | -41.88 | -10.40 | -42.21 | 169 |
| 44 | Stochastic reversion · 1h | reversion | 64.69 | -35.31 | 411 | 39.9 | -36.06 | -3.97 | -43.38 | 441 |
| 45 | MACD zero-line · 1h | trend | 63.27 | -36.73 | 202 | 16.3 | -35.56 | -9.85 | -35.84 | 201 |
| 46 | RSI momentum · 1h | momentum | 62.48 | -37.52 | 202 | 14.9 | -43.11 | -9.67 | -43.45 | 188 |
| 47 | MFI reversion · 1h | reversion | 61.51 | -38.49 | 512 | 32.0 | -33.49 | -5.02 | -37.72 | 198 |
| 48 | Heikin-Ashi · 1h | trend | 61.15 | -38.85 | 546 | 22.0 | -50.26 | -10.40 | -50.86 | 623 |
| 49 | Donchian 20/10 · 1h | breakout | 60.80 | -39.20 | 183 | 17.5 | -41.77 | -9.35 | -42.89 | 192 |
| 50 | ROC + volume · 1h | momentum | 60.45 | -39.55 | 461 | 26.9 | -41.11 | -8.13 | -41.50 | 337 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -60.35 | -4.58 | -62.11 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 57.82 | -42.18 | 313 | 12.1 | -46.36 | -10.84 | -47.25 | 324 |
| 53 | Agent (ML meta-label) | meta | 56.80 | -43.20 | 2073 | 25.4 | -22.78 | -2.87 | -29.67 | 322 |
| 54 | MACD cross · 1h | trend | 56.72 | -43.28 | 491 | 20.4 | -54.30 | -11.00 | -55.47 | 502 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.98 | -9.15 | -55.48 | 502 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -41.74 | -5.13 | -45.50 | 432 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -57.71 | -9.50 | -59.36 | 703 |
| 58 | VWAP momentum · 1h | momentum | 50.68 | -49.32 | 1086 | 21.5 | -60.74 | -13.21 | -61.85 | 1174 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -57.30 | -9.65 | -59.60 | 605 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.17 | -49.95 | -99.20 | 5408 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.95 | -33.54 | -84.48 | 1424 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.35 | -48.51 | -94.44 | 2404 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.73 | -32.33 | -91.19 | 1905 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.59 | -41.51 | -91.80 | 2229 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.09 | -27.86 | -89.12 | 1920 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -49.42 | -98.26 | 3424 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.86 | -52.52 | -96.92 | 3335 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.78 | -35.16 | -92.81 | 2035 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.13 | -35.14 | -82.40 | 1507 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -57.72 | -99.70 | 6310 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.16 | -38.41 | -93.35 | 2483 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.02 | -35.33 | -94.04 | 3124 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.10 | -99.83 | 6107 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.12 | -44.27 | -93.29 | 2266 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -50.80 | -20.98 | -52.43 | 664 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.34 | -23.30 | -79.10 | 1604 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -57.87 | -97.74 | 3229 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.57 | -99.23 | 5149 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.11 | -24.20 | -71.35 | 1208 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -46.28 | -94.84 | 2657 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -48.45 | -6.90 | -51.26 | 292 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.43 | -34.56 | -84.80 | 1657 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.77 | -99.78 | 6536 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.59 | -31.57 | -91.98 | 2507 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.78 | -20.24 | -83.45 | 1969 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.07 | -34.43 | -92.31 | 2175 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.22 | -50.33 | -98.24 | 4083 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.35 | -48.26 | -90.70 | 2205 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.32 | -27.97 | -68.03 | 776 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.12 | -28.17 | -73.46 | 1143 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.85 | -19.63 | -85.15 | 1835 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.09 | -51.09 | -98.13 | 4411 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -108.80 | -99.94 | 8276 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -48.89 | -7.55 | -52.72 | 292 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T18:00 | Agent (aggressive) | sell | SQQQ | 38.38 | 0.02 | selected signal exited |
| 2026-11-25T18:00 | Agent | sell | SQQQ | 15.45 | 0.01 | selected signal exited |
| 2026-11-25T18:00 | Stochastic reversion · 1h | sell | DOGE-USD | 6.37 | 0.21 | exit signal |
| 2026-11-25T18:00 | ROC + volume · 1h | buy | XRP-USD | 10.05 | — | entry signal |
| 2026-11-25T18:00 | ROC + volume · 1h | buy | SOL-USD | 10.06 | — | entry signal |
| 2026-11-25T18:00 | ROC + volume · 1h | buy | ETH-USD | 10.06 | — | entry signal |
| 2026-11-25T18:00 | ROC + volume · 1h | buy | BTC-USD | 10.06 | — | entry signal |
| 2026-11-25T18:00 | ROC + volume · 1h | sell | SQQQ | 4.15 | -0.27 | rebalance down |
| 2026-11-25T18:00 | ROC + volume · 1h | sell | LABU | 5.86 | 0.29 | rebalance down |
| 2026-11-25T18:00 | VWAP momentum · 1h | buy | XRP-USD | 8.45 | — | entry signal |
| 2026-11-25T18:00 | VWAP momentum · 1h | buy | SOL-USD | 8.45 | — | entry signal |
| 2026-11-25T18:00 | VWAP momentum · 1h | buy | ETH-USD | 8.45 | — | entry signal |
| 2026-11-25T18:00 | VWAP momentum · 1h | buy | DOGE-USD | 8.45 | — | entry signal |
| 2026-11-25T18:00 | VWAP momentum · 1h | buy | BTC-USD | 8.45 | — | entry signal |
| 2026-11-25T18:00 | VWAP momentum · 1h | sell | META | 4.36 | 0.06 | rebalance down |
| 2026-11-25T18:00 | ADX DI cross · 1h | buy | XRP-USD | 17.33 | — | entry signal |
| 2026-11-25T18:00 | Parabolic SAR · 1h | buy | XRP-USD | 18.86 | — | entry signal |
| 2026-11-25T18:00 | Parabolic SAR · 1h | buy | DOGE-USD | 18.86 | — | entry signal |
| 2026-11-25T18:00 | Supertrend · 1h | buy | SOL-USD | 6.67 | — | entry signal |
| 2026-11-25T18:00 | Supertrend · 1h | buy | DOGE-USD | 9.53 | — | entry signal |
| 2026-11-25T18:00 | Supertrend · 1h | sell | TNA | 4.29 | 0.17 | rebalance down |
| 2026-11-25T18:00 | Supertrend · 1h | sell | META | 4.24 | 0.15 | rebalance down |
| 2026-11-25T18:00 | Supertrend · 1h | sell | IWM | 3.83 | 0.04 | rebalance down |
| 2026-11-25T18:00 | Supertrend · 1h | sell | AAPL | 3.85 | 0.04 | rebalance down |
| 2026-11-25T18:00 | MACD cross · 1h | buy | BTC-USD | 2.87 | — | entry signal |
| 2026-11-25T18:00 | MACD cross · 1h | sell | SQQQ | 2.87 | -0.17 | rebalance down |
| 2026-11-25T17:45 | Agent (aggressive) | buy | SQQQ | 38.36 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |
| 2026-11-25T17:45 | Agent | buy | SQQQ | 15.45 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |
| 2026-11-25T17:35 | MFI reversion · 1h | buy | TQQQ | 3.35 | — | entry |
| 2026-11-25T17:35 | MFI reversion · 1h | sell | SOL-USD | 3.35 | 0.02 | rebalance down |
| 2026-11-25T17:30 | Agent (aggressive) | sell | SQQQ | 38.40 | 0.08 | selected signal exited |
| 2026-11-25T17:30 | Agent | sell | SQQQ | 15.47 | 0.03 | selected signal exited |
| 2026-11-25T17:30 | MFI reversion · 1h | buy | SOXL | 3.71 | — | entry signal |
| 2026-11-25T17:30 | MFI reversion · 1h | buy | QQQ | 5.05 | — | entry signal |
| 2026-11-25T17:30 | MFI reversion · 1h | buy | NVDA | 5.05 | — | entry signal |
| 2026-11-25T17:30 | MFI reversion · 1h | buy | MSFT | 5.05 | — | entry signal |
| 2026-11-25T17:30 | MFI reversion · 1h | buy | AMZN | 5.05 | — | entry signal |
| 2026-11-25T17:30 | MFI reversion · 1h | sell | XRP-USD | 5.02 | 0.02 | rebalance down |
| 2026-11-25T17:30 | MFI reversion · 1h | sell | TNA | 5.21 | 0.16 | rebalance down |
| 2026-11-25T17:30 | MFI reversion · 1h | sell | IWM | 5.00 | 0.04 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 18:11:05.000160+00:00 -> 2026-11-25 18:21:05.000160+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
