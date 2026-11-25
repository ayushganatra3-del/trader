# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T17:11:05.000144+00:00 · 73262 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.20 (-22.80%)

Closed trades 247, win rate 35.6%, fees £6.77, max drawdown -23.15%.

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

Today: 22353 decisions in 2610 calls, $0.2872 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T17:11 | 12 / 16 / 2 | TECL 18%, TNA 17%, SOXL 17%, COIN 16% |  |
| Breezy | 2026-11-25T17:11 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-25T17:11 | 9 / 20 / 1 | MSTR 84% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.16 | 3.61 | -5.42 | 29 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.98 | 15.98 | 0 | — | 13.75 | 4.80 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.66 | 1.10 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.06 | 4.06 | 0 | — | 3.60 | 1.20 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.98 | -0.22 | -8.58 | 212 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.81 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | -0.45 | -0.06 | -6.21 | 167 |
| 12 | Trend pullback · 1h | trend | 93.23 | -6.77 | 116 | 24.1 | -4.83 | -2.20 | -9.95 | 36 |
| 13 | Hold SPY | benchmark | 93.14 | -6.86 | 0 | — | -7.94 | -2.03 | -11.71 | 1 |
| 14 | Three white soldiers · 1h | momentum | 92.57 | -7.43 | 21 | 9.5 | -6.32 | -6.83 | -6.44 | 19 |
| 15 | Copy: Insider buying | copy | 91.52 | -8.48 | 61 | 41.0 | -7.60 | -1.40 | -14.79 | 72 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 90.76 | -9.24 | 0 | — | -10.88 | -2.25 | -13.91 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Daily: Bullish score | daily | 87.40 | -12.60 | 20 | 20.0 | -11.67 | -2.50 | -19.56 | 14 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.49 | -2.97 | -20.94 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 86.72 | -13.28 | 0 | — | -14.44 | -3.06 | -17.03 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.85 | -2.39 | -20.49 | 155 |
| 22 | Opening range 30m | breakout | 84.57 | -15.43 | 478 | 32.4 | -13.52 | -4.56 | -15.61 | 541 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -16.50 | -6.06 | -16.50 | 69 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.91 | -13.02 | 61 |
| 26 | Agent | meta | 77.20 | -22.80 | 247 | 35.6 | -27.10 | -6.17 | -27.28 | 197 |
| 27 | Volume breakout · 1h | breakout | 76.66 | -23.34 | 170 | 28.2 | -22.12 | -9.39 | -22.21 | 67 |
| 28 | Agent (aggressive) | meta | 76.64 | -23.36 | 112 | 32.1 | -17.15 | -4.48 | -18.48 | 90 |
| 29 | Opening range 15m | breakout | 76.19 | -23.80 | 601 | 30.3 | -22.88 | -7.12 | -24.95 | 678 |
| 30 | Parabolic SAR · 1h | trend | 75.87 | -24.13 | 209 | 27.8 | -35.83 | -8.72 | -35.92 | 179 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.44 | -7.82 | -29.45 | 74 |
| 32 | Keltner breakout · 1h | breakout | 74.21 | -25.80 | 140 | 25.0 | -28.42 | -7.09 | -28.51 | 150 |
| 33 | Ichimoku · 1h | trend | 73.15 | -26.85 | 113 | 15.9 | -31.20 | -7.96 | -31.69 | 102 |
| 34 | Max aggression: 5-day momentum | meta | 70.26 | -29.74 | 27 | 37.0 | -59.10 | -3.47 | -67.33 | 23 |
| 35 | Daily: Momentum burst | daily | 70.13 | -29.87 | 31 | 16.1 | -34.46 | -4.87 | -36.38 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.27 | -30.73 | 264 | 18.9 | -38.96 | -7.54 | -39.20 | 273 |
| 37 | Hold BTC | benchmark | 68.67 | -31.33 | 3 | 0.0 | -29.98 | -5.39 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -31.90 | -8.37 | -32.32 | 204 |
| 39 | EMA 20/50 cross · 1h | trend | 67.11 | -32.89 | 126 | 9.5 | -37.00 | -10.43 | -37.40 | 110 |
| 40 | Supertrend · 1h | trend | 66.73 | -33.27 | 221 | 17.6 | -37.76 | -7.17 | -39.12 | 215 |
| 41 | OBV trend · 1h | momentum | 66.64 | -33.36 | 324 | 19.8 | -39.44 | -9.77 | -40.67 | 225 |
| 42 | Triple EMA stack · 1h | trend | 65.92 | -34.08 | 171 | 15.2 | -41.48 | -10.54 | -41.74 | 168 |
| 43 | Copy: Cathie Wood (ARKK) | copy | 65.42 | -34.58 | 3 | 0.0 | -28.81 | -3.76 | -33.66 | 1 |
| 44 | Stochastic reversion · 1h | reversion | 63.33 | -36.67 | 410 | 39.8 | -37.92 | -4.24 | -43.37 | 437 |
| 45 | MACD zero-line · 1h | trend | 63.27 | -36.73 | 202 | 16.3 | -35.39 | -9.78 | -35.70 | 201 |
| 46 | RSI momentum · 1h | momentum | 62.48 | -37.52 | 202 | 14.9 | -43.48 | -9.76 | -43.82 | 191 |
| 47 | Heikin-Ashi · 1h | trend | 61.58 | -38.42 | 546 | 22.0 | -49.94 | -10.37 | -50.54 | 623 |
| 48 | MFI reversion · 1h | reversion | 60.82 | -39.18 | 512 | 32.0 | -34.55 | -5.18 | -37.70 | 190 |
| 49 | ROC + volume · 1h | momentum | 60.51 | -39.49 | 461 | 26.9 | -40.97 | -8.08 | -41.50 | 333 |
| 50 | Donchian 20/10 · 1h | breakout | 60.39 | -39.61 | 183 | 17.5 | -42.20 | -9.40 | -42.89 | 192 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -59.30 | -4.51 | -61.09 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 57.72 | -42.28 | 313 | 12.1 | -46.85 | -10.91 | -47.47 | 326 |
| 53 | Agent (ML meta-label) | meta | 56.91 | -43.09 | 2073 | 25.4 | -19.28 | -2.39 | -27.31 | 325 |
| 54 | MACD cross · 1h | trend | 56.36 | -43.64 | 491 | 20.4 | -54.76 | -11.03 | -55.48 | 497 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -54.60 | -9.14 | -55.46 | 499 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -42.14 | -5.13 | -45.50 | 436 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -57.38 | -9.18 | -58.46 | 687 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -57.87 | -9.71 | -59.61 | 598 |
| 59 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.20 | -50.26 | -99.21 | 5439 |
| 60 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.13 | -33.86 | -84.37 | 1417 |
| 61 | VWAP momentum · 1h | momentum | 50.56 | -49.44 | 1085 | 21.5 | -61.28 | -13.28 | -62.12 | 1172 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.41 | -49.58 | -94.44 | 2399 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.82 | -32.89 | -91.13 | 1902 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.72 | -41.90 | -91.79 | 2222 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.01 | -27.82 | -89.10 | 1922 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.23 | -49.97 | -98.26 | 3427 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -53.51 | -96.92 | 3330 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.77 | -35.21 | -92.77 | 2032 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.57 | -36.13 | -82.58 | 1514 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -57.69 | -99.71 | 6325 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.34 | -39.03 | -93.41 | 2491 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.05 | -35.52 | -94.05 | 3129 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.99 | -99.83 | 6108 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.33 | -44.90 | -93.37 | 2254 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.95 | -22.72 | -52.60 | 667 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.75 | -24.01 | -79.09 | 1626 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -59.06 | -97.74 | 3240 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.79 | -99.23 | 5152 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.77 | -26.12 | -71.39 | 1203 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -48.05 | -94.86 | 2660 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -49.48 | -7.02 | -51.25 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.78 | -36.05 | -84.90 | 1652 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.74 | -99.78 | 6541 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.67 | -31.74 | -91.96 | 2509 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.71 | -20.26 | -83.46 | 1973 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.06 | -34.22 | -92.34 | 2183 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -50.29 | -98.24 | 4083 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.49 | -48.45 | -90.66 | 2199 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.71 | -28.99 | -67.94 | 792 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.60 | -28.54 | -73.60 | 1149 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.83 | -19.64 | -85.18 | 1834 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -50.50 | -98.12 | 4410 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.65 | -99.94 | 8279 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -48.38 | -7.23 | -52.66 | 287 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T17:11 | Agent (aggressive) | sell | SQQQ | 37.87 | -0.90 | selected signal exited |
| 2026-11-25T17:11 | Agent | sell | SQQQ | 15.15 | -0.36 | selected signal exited |
| 2026-11-25T17:11 | Opening range 30m | buy | UPRO | 7.69 | — | entry signal |
| 2026-11-25T17:11 | Opening range 30m | buy | TQQQ | 7.69 | — | entry signal |
| 2026-11-25T17:11 | Opening range 30m | buy | SPY | 7.69 | — | entry signal |
| 2026-11-25T17:11 | Opening range 30m | buy | QQQ | 7.69 | — | entry signal |
| 2026-11-25T17:11 | Opening range 30m | buy | COIN | 7.69 | — | entry signal |
| 2026-11-25T17:11 | Opening range 30m | sell | TNA | 5.28 | 0.14 | rebalance down |
| 2026-11-25T17:11 | Opening range 30m | sell | PLTR | 9.16 | 0.10 | rebalance down |
| 2026-11-25T17:11 | Opening range 30m | sell | IWM | 9.10 | 0.07 | rebalance down |
| 2026-11-25T17:11 | Opening range 30m | sell | ETHU | 6.39 | 0.05 | rebalance down |
| 2026-11-25T17:11 | Opening range 30m | sell | BITX | 9.30 | 0.27 | rebalance down |
| 2026-11-25T17:11 | Opening range 15m | buy | UPRO | 5.06 | — | entry |
| 2026-11-25T17:11 | Opening range 15m | buy | TQQQ | 5.08 | — | entry signal |
| 2026-11-25T17:11 | Opening range 15m | buy | TECL | 5.08 | — | entry signal |
| 2026-11-25T17:11 | Opening range 15m | buy | SPY | 5.08 | — | entry |
| 2026-11-25T17:11 | Opening range 15m | buy | SOXL | 5.08 | — | entry signal |
| 2026-11-25T17:11 | Opening range 15m | buy | QQQ | 5.08 | — | entry signal |
| 2026-11-25T17:11 | Opening range 15m | buy | COIN | 5.08 | — | entry signal |
| 2026-11-25T17:11 | Opening range 15m | buy | AMD | 5.08 | — | entry signal |
| 2026-11-25T17:11 | Opening range 15m | sell | TNA | 5.92 | 0.15 | rebalance down |
| 2026-11-25T17:11 | Opening range 15m | sell | PLTR | 5.78 | 0.10 | rebalance down |
| 2026-11-25T17:11 | Opening range 15m | sell | META | 5.78 | 0.13 | rebalance down |
| 2026-11-25T17:11 | Opening range 15m | sell | IWM | 5.74 | 0.05 | rebalance down |
| 2026-11-25T17:11 | Opening range 15m | sell | GOOGL | 5.72 | 0.03 | rebalance down |
| 2026-11-25T17:11 | Opening range 15m | sell | ETHU | 5.82 | 0.16 | rebalance down |
| 2026-11-25T17:11 | Opening range 15m | sell | BITX | 5.87 | 0.17 | rebalance down |
| 2026-11-25T17:06 | Opening range 30m | buy | META | 6.86 | — | entry signal |
| 2026-11-25T17:06 | Opening range 30m | sell | ETHU | 6.86 | 0.00 | rebalance down |
| 2026-11-25T17:00 | Agent (rotation) | sell | SQQQ | 7.78 | -0.12 | selected signal exited |
| 2026-11-25T17:00 | Agent (aggressive) | buy | SQQQ | 38.77 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |
| 2026-11-25T17:00 | Agent | buy | SQQQ | 15.51 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |
| 2026-11-25T17:00 | MACD cross · 1h | buy | SOL-USD | 2.72 | — | entry signal |
| 2026-11-25T17:00 | Opening range 30m | buy | TNA | 12.63 | — | entry signal |
| 2026-11-25T17:00 | Opening range 30m | buy | PLTR | 16.65 | — | entry signal |
| 2026-11-25T17:00 | Opening range 30m | buy | IWM | 16.65 | — | entry signal |
| 2026-11-25T17:00 | Opening range 30m | sell | BITX | 4.34 | 0.04 | rebalance down |
| 2026-11-25T17:00 | Opening range 15m | buy | TNA | 10.72 | — | entry signal |
| 2026-11-25T17:00 | Opening range 15m | buy | IWM | 10.73 | — | entry signal |
| 2026-11-25T17:00 | Opening range 15m | buy | GOOGL | 10.73 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 17:11:05.000144+00:00 -> 2026-11-25 17:21:05.000144+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
