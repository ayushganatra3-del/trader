# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T17:42:05.000126+00:00 · 73292 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.24 (-22.76%)

Closed trades 248, win rate 35.9%, fees £6.78, max drawdown -23.32%.

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

Today: 25047 decisions in 2700 calls, $0.3186 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T17:42 | 6 / 20 / 4 | cash |  |
| Breezy | 2026-11-25T17:42 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-25T17:42 | 8 / 21 / 1 | MSTR 82% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.86 | 15.86 | 0 | — | 13.96 | 4.89 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.31 | 1.04 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.24 | 4.24 | 0 | — | 4.37 | 1.33 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.98 | -0.22 | -8.58 | 212 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.56 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | -0.45 | -0.06 | -6.21 | 167 |
| 12 | Hold SPY | benchmark | 93.22 | -6.78 | 0 | — | -7.61 | -1.94 | -11.71 | 1 |
| 13 | Trend pullback · 1h | trend | 92.81 | -7.19 | 116 | 24.1 | -5.16 | -2.43 | -9.95 | 36 |
| 14 | Three white soldiers · 1h | momentum | 92.57 | -7.43 | 21 | 9.5 | -6.32 | -6.83 | -6.44 | 19 |
| 15 | Copy: Insider buying | copy | 91.64 | -8.36 | 61 | 41.0 | -6.76 | -1.23 | -14.79 | 72 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 90.46 | -9.54 | 0 | — | -10.88 | -2.25 | -13.91 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 87.36 | -12.64 | 0 | — | -13.59 | -2.93 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.83 | -2.97 | -20.94 | 1 |
| 20 | Daily: Bullish score | daily | 87.00 | -13.00 | 20 | 20.0 | -11.64 | -2.59 | -19.56 | 14 |
| 21 | Opening range 30m | breakout | 85.05 | -14.95 | 478 | 32.4 | -12.90 | -4.35 | -15.61 | 548 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.79 | -2.38 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -17.45 | -6.18 | -17.48 | 70 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.91 | -13.02 | 61 |
| 26 | Agent | meta | 77.24 | -22.76 | 248 | 35.9 | -27.21 | -6.21 | -27.58 | 196 |
| 27 | Opening range 15m | breakout | 76.76 | -23.24 | 601 | 30.3 | -22.15 | -6.84 | -24.95 | 682 |
| 28 | Agent (aggressive) | meta | 76.72 | -23.28 | 113 | 32.7 | -17.02 | -4.45 | -18.44 | 90 |
| 29 | Volume breakout · 1h | breakout | 76.66 | -23.34 | 170 | 28.2 | -22.12 | -9.39 | -22.21 | 67 |
| 30 | Parabolic SAR · 1h | trend | 75.55 | -24.45 | 209 | 27.8 | -35.23 | -8.68 | -35.32 | 178 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.44 | -7.82 | -29.45 | 74 |
| 32 | Keltner breakout · 1h | breakout | 73.90 | -26.10 | 140 | 25.0 | -28.26 | -7.04 | -28.35 | 148 |
| 33 | Ichimoku · 1h | trend | 72.93 | -27.07 | 113 | 15.9 | -31.30 | -7.98 | -31.69 | 102 |
| 34 | Max aggression: 5-day momentum | meta | 70.56 | -29.44 | 27 | 37.0 | -58.79 | -3.41 | -67.33 | 23 |
| 35 | Daily: Momentum burst | daily | 70.20 | -29.80 | 31 | 16.1 | -34.04 | -4.84 | -36.38 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.14 | -30.86 | 264 | 18.9 | -39.08 | -7.57 | -39.30 | 270 |
| 37 | Hold BTC | benchmark | 68.90 | -31.10 | 3 | 0.0 | -29.66 | -5.29 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -31.90 | -8.35 | -32.32 | 203 |
| 39 | EMA 20/50 cross · 1h | trend | 66.80 | -33.20 | 126 | 9.5 | -37.22 | -10.49 | -37.40 | 110 |
| 40 | Supertrend · 1h | trend | 66.62 | -33.38 | 221 | 17.6 | -38.43 | -7.38 | -39.87 | 213 |
| 41 | OBV trend · 1h | momentum | 66.59 | -33.41 | 324 | 19.8 | -39.20 | -9.58 | -40.83 | 226 |
| 42 | Copy: Cathie Wood (ARKK) | copy | 65.81 | -34.19 | 3 | 0.0 | -28.66 | -3.68 | -33.66 | 1 |
| 43 | Triple EMA stack · 1h | trend | 65.65 | -34.35 | 171 | 15.2 | -41.85 | -10.46 | -42.11 | 169 |
| 44 | Stochastic reversion · 1h | reversion | 63.94 | -36.06 | 410 | 39.8 | -35.88 | -3.93 | -42.59 | 442 |
| 45 | MACD zero-line · 1h | trend | 63.27 | -36.73 | 202 | 16.3 | -35.54 | -9.84 | -35.84 | 201 |
| 46 | RSI momentum · 1h | momentum | 62.29 | -37.71 | 202 | 14.9 | -43.20 | -9.64 | -43.45 | 188 |
| 47 | Heikin-Ashi · 1h | trend | 61.33 | -38.67 | 546 | 22.0 | -50.14 | -10.37 | -50.79 | 624 |
| 48 | MFI reversion · 1h | reversion | 61.02 | -38.98 | 512 | 32.0 | -34.10 | -5.12 | -37.90 | 197 |
| 49 | Donchian 20/10 · 1h | breakout | 60.45 | -39.55 | 183 | 17.5 | -42.17 | -9.42 | -42.97 | 192 |
| 50 | ROC + volume · 1h | momentum | 60.33 | -39.67 | 461 | 26.9 | -41.06 | -8.10 | -41.50 | 333 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -59.86 | -4.55 | -61.63 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 57.55 | -42.45 | 313 | 12.1 | -46.89 | -10.91 | -47.49 | 326 |
| 53 | Agent (ML meta-label) | meta | 56.85 | -43.15 | 2073 | 25.4 | -22.17 | -2.79 | -29.58 | 318 |
| 54 | MACD cross · 1h | trend | 56.35 | -43.65 | 491 | 20.4 | -54.55 | -11.02 | -55.48 | 499 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -54.32 | -9.17 | -55.56 | 501 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -42.14 | -5.18 | -45.50 | 432 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -57.28 | -9.25 | -58.66 | 695 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -57.36 | -9.61 | -59.60 | 609 |
| 59 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.18 | -50.14 | -99.20 | 5415 |
| 60 | VWAP momentum · 1h | momentum | 50.58 | -49.42 | 1086 | 21.5 | -60.55 | -13.33 | -61.59 | 1169 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.94 | -33.64 | -84.40 | 1420 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.36 | -48.97 | -94.42 | 2401 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.82 | -32.65 | -91.19 | 1905 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.67 | -41.91 | -91.81 | 2227 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.07 | -27.86 | -89.16 | 1925 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.21 | -49.74 | -98.26 | 3426 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -52.97 | -96.90 | 3329 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.79 | -35.22 | -92.80 | 2031 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.29 | -35.53 | -82.46 | 1510 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -57.77 | -99.71 | 6328 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.27 | -38.77 | -93.40 | 2489 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.03 | -35.40 | -94.05 | 3127 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.63 | -99.83 | 6109 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.19 | -44.68 | -93.29 | 2266 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.33 | -21.99 | -52.43 | 664 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.56 | -23.67 | -79.08 | 1617 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -58.59 | -97.74 | 3229 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.54 | -99.23 | 5149 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.47 | -25.24 | -71.38 | 1204 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -47.19 | -94.84 | 2659 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -48.97 | -6.97 | -51.26 | 292 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.61 | -35.43 | -84.84 | 1657 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.56 | -99.78 | 6538 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -31.53 | -91.96 | 2506 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.88 | -20.34 | -83.55 | 1974 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.09 | -34.33 | -92.34 | 2177 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -50.34 | -98.24 | 4083 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.39 | -48.50 | -90.65 | 2198 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.70 | -29.13 | -67.96 | 776 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.33 | -28.29 | -73.54 | 1149 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.84 | -19.64 | -85.16 | 1833 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.08 | -50.77 | -98.13 | 4410 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.17 | -99.94 | 8268 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -49.58 | -7.68 | -52.72 | 292 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-25T17:30 | MFI reversion · 1h | sell | BTC-USD | 3.60 | 0.02 | rebalance down |
| 2026-11-25T17:30 | MFI reversion · 1h | sell | BITX | 5.07 | 0.06 | rebalance down |
| 2026-11-25T17:30 | Stochastic reversion · 1h | buy | TECL | 6.33 | — | entry signal |
| 2026-11-25T17:30 | Stochastic reversion · 1h | buy | SOXL | 6.33 | — | entry signal |
| 2026-11-25T17:30 | Stochastic reversion · 1h | buy | NVDA | 6.33 | — | entry signal |
| 2026-11-25T17:30 | Stochastic reversion · 1h | buy | AMD | 6.33 | — | entry signal |
| 2026-11-25T17:30 | Stochastic reversion · 1h | sell | MSTR | 3.42 | 0.15 | rebalance down |
| 2026-11-25T17:30 | Stochastic reversion · 1h | sell | MSFT | 4.12 | -0.04 | rebalance down |
| 2026-11-25T17:30 | Stochastic reversion · 1h | sell | ETHU | 6.42 | -0.32 | rebalance down |
| 2026-11-25T17:30 | Stochastic reversion · 1h | sell | DOGE-USD | 6.26 | 0.15 | rebalance down |
| 2026-11-25T17:30 | Stochastic reversion · 1h | sell | COIN | 6.34 | 0.16 | rebalance down |
| 2026-11-25T17:30 | OBV trend · 1h | buy | LABU | 16.64 | — | entry |
| 2026-11-25T17:30 | VWAP momentum · 1h | buy | META | 12.63 | — | entry signal |
| 2026-11-25T17:30 | VWAP momentum · 1h | sell | SQQQ | 12.23 | -0.53 | exit signal |
| 2026-11-25T17:30 | ADX DI cross · 1h | buy | PLTR | 17.26 | — | entry signal |
| 2026-11-25T17:30 | MACD cross · 1h | buy | SOL-USD | 3.08 | — | rebalance up |
| 2026-11-25T17:30 | MACD cross · 1h | buy | META | 7.00 | — | entry signal |
| 2026-11-25T17:30 | MACD cross · 1h | buy | ETHU | 7.00 | — | entry signal |
| 2026-11-25T17:30 | MACD cross · 1h | sell | TNA | 4.46 | 0.12 | rebalance down |
| 2026-11-25T17:30 | MACD cross · 1h | sell | LABU | 4.20 | 0.19 | rebalance down |
| 2026-11-25T17:30 | MACD cross · 1h | sell | IWM | 4.29 | 0.02 | rebalance down |
| 2026-11-25T17:30 | MACD cross · 1h | sell | ETH-USD | 4.14 | -0.01 | rebalance down |
| 2026-11-25T17:15 | Agent (aggressive) | buy | SQQQ | 38.32 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |
| 2026-11-25T17:15 | Agent | buy | SQQQ | 15.44 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |
| 2026-11-25T17:15 | MFI reversion · 1h | buy | ETHU | 3.39 | — | entry |
| 2026-11-25T17:15 | MFI reversion · 1h | sell | BTC-USD | 3.39 | 0.02 | rebalance down |
| 2026-11-25T17:11 | Agent (aggressive) | sell | SQQQ | 37.87 | -0.90 | selected signal exited |
| 2026-11-25T17:11 | Agent | sell | SQQQ | 15.15 | -0.36 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 17:42:05.000126+00:00 -> 2026-11-25 17:52:05.000126+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
