# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T17:57:05.000113+00:00 · 64696 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.88 (-15.12%)

Closed trades 222, win rate 36.0%, fees £6.13, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SPY | 16.96 | -0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-18 | PEPG 12%, FUN 12%, STWD 12%, LRN 12%, PSEC 12%, TEAM 12%, BH 12%, LILA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-17)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 34.44 · VIX 25.46 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 6.1, AMZN 4.3, TSLA 2.4, META 1.9, AMD 1.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 26487 decisions in 2802 calls, $0.3362 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T17:57 | 5 / 12 / 13 | AMZN 15%, AMD 14% |  |
| Breezy | 2026-11-18T17:57 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-18T17:57 | 5 / 23 / 2 | BITX 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| OBV trend | SQQQ | 1.90 | +5.25% | 11 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 115.03 | 15.03 | 0 | — | 12.92 | 4.44 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 17.51 | 3.58 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.31 | 4.31 | 0 | — | 5.28 | 1.40 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.65 | 0.65 | 150 | 34.7 | -3.11 | -2.62 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 7.96 | 2.22 | -9.06 | 214 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.62 | -3.38 | 8 | 50.0 | -4.21 | -0.10 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.85 | -4.15 | 0 | — | -4.04 | -1.32 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.20 | -1.48 | -8.74 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.57 | -5.92 | -5.99 | 22 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.48 | -7.52 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Copy: Insider buying | copy | 91.78 | -8.22 | 50 | 42.0 | -9.18 | -1.83 | -14.79 | 64 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.39 | -8.61 | 0 | — | -7.40 | -1.98 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.32 | -9.68 | 113 | 23.9 | -12.53 | -6.89 | -12.89 | 56 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -11.42 | -3.36 | -18.48 | 147 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.11 | -12.89 | 17 | 17.6 | -5.40 | -0.83 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.00 | -8.98 | -16.05 | 70 |
| 24 | Opening range 30m | breakout | 84.98 | -15.02 | 443 | 33.4 | -10.54 | -3.33 | -14.48 | 566 |
| 25 | Agent | meta | 84.88 | -15.12 | 222 | 36.0 | -15.11 | -7.33 | -17.06 | 201 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 104 | 33.7 | -15.70 | -4.17 | -19.74 | 97 |
| 27 | Parabolic SAR · 1h | trend | 81.67 | -18.33 | 188 | 28.2 | -24.31 | -6.72 | -27.41 | 199 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.31 | -6.36 | -14.63 | 87 |
| 29 | Keltner breakout · 1h | breakout | 79.83 | -20.17 | 124 | 25.8 | -24.10 | -6.41 | -27.04 | 155 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -14.35 | -4.42 | -21.17 | 77 |
| 31 | Max aggression: 5-day momentum | meta | 79.10 | -20.90 | 21 | 42.9 | -48.02 | -3.21 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 79.03 | -20.97 | 78 | 12.8 | -25.45 | -6.68 | -30.57 | 84 |
| 33 | Opening range 15m | breakout | 77.81 | -22.19 | 536 | 31.5 | -16.88 | -4.55 | -21.44 | 676 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.55 | -22.45 | 2 | 0.0 | -17.63 | -2.34 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.06 | -24.94 | 209 | 19.1 | -27.34 | -4.48 | -35.44 | 269 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 37 | Hold BTC | benchmark | 73.99 | -26.01 | 2 | 0.0 | -17.83 | -2.50 | -28.91 | 1 |
| 38 | Stochastic reversion · 1h | reversion | 73.09 | -26.91 | 350 | 42.3 | -34.20 | -5.20 | -35.58 | 426 |
| 39 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.27 | -8.02 | -34.15 | 221 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -39.32 | -2.40 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.71 | -28.29 | 191 | 16.2 | -32.27 | -5.45 | -39.50 | 202 |
| 42 | Triple EMA stack · 1h | trend | 70.87 | -29.13 | 156 | 14.7 | -31.71 | -6.38 | -37.58 | 176 |
| 43 | MFI reversion · 1h | reversion | 70.75 | -29.25 | 445 | 33.7 | -26.92 | -3.98 | -30.08 | 169 |
| 44 | RSI momentum · 1h | momentum | 70.28 | -29.72 | 179 | 14.5 | -32.73 | -6.01 | -39.00 | 200 |
| 45 | MACD zero-line · 1h | trend | 69.83 | -30.17 | 184 | 17.9 | -27.77 | -5.55 | -33.89 | 202 |
| 46 | Heikin-Ashi · 1h | trend | 69.48 | -30.52 | 474 | 23.0 | -45.05 | -9.91 | -45.84 | 633 |
| 47 | EMA 20/50 cross · 1h | trend | 69.41 | -30.59 | 116 | 10.3 | -36.53 | -9.46 | -40.47 | 116 |
| 48 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 49 | ROC + volume · 1h | momentum | 68.57 | -31.43 | 413 | 28.1 | -32.89 | -5.90 | -39.35 | 342 |
| 50 | OBV trend · 1h | momentum | 68.29 | -31.71 | 310 | 19.4 | -36.06 | -7.72 | -40.30 | 254 |
| 51 | MACD cross · 1h | trend | 67.91 | -32.09 | 417 | 22.3 | -40.44 | -6.63 | -46.40 | 489 |
| 52 | CCI reversion · 1h | reversion | 67.39 | -32.61 | 386 | 41.5 | -42.07 | -7.06 | -44.29 | 472 |
| 53 | Donchian 20/10 · 1h | breakout | 66.52 | -33.48 | 162 | 17.9 | -35.71 | -6.66 | -41.57 | 199 |
| 54 | Bollinger reversion · 1h | reversion | 64.18 | -35.82 | 348 | 37.9 | -38.48 | -5.84 | -39.58 | 413 |
| 55 | Williams %R · 1h | reversion | 63.78 | -36.22 | 436 | 40.6 | -46.58 | -8.13 | -47.61 | 568 |
| 56 | EMA 9/21 cross · 1h | trend | 62.97 | -37.03 | 284 | 11.3 | -40.42 | -7.93 | -46.40 | 323 |
| 57 | Agent (ML meta-label) | meta | 60.24 | -39.76 | 1924 | 24.5 | -21.45 | -4.08 | -23.44 | 297 |
| 58 | RSI(14) reversion · 1h | reversion | 59.20 | -40.80 | 206 | 32.0 | -40.96 | -6.06 | -43.22 | 257 |
| 59 | Z-score reversion · 1h | reversion | 57.87 | -42.13 | 227 | 35.2 | -36.51 | -5.03 | -39.63 | 256 |
| 60 | VWAP momentum · 1h | momentum | 55.42 | -44.58 | 975 | 21.7 | -56.05 | -11.16 | -59.65 | 1203 |
| 61 | Candlestick reversal · 1h | reversion | 55.36 | -44.64 | 552 | 26.4 | -47.63 | -8.76 | -48.92 | 640 |
| 62 | Three white soldiers | momentum | 54.75 | -45.25 | 588 | 14.5 | -49.66 | -21.86 | -50.71 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.87 | -99.04 | 5286 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.42 | -25.63 | -82.55 | 1405 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.67 | -41.96 | -93.95 | 2457 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.90 | -31.55 | -90.27 | 1942 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.02 | -38.93 | -91.46 | 2304 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.04 | -31.26 | -90.07 | 2089 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -48.41 | -97.92 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -53.28 | -96.43 | 3385 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -38.82 | -93.63 | 2215 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.45 | -34.53 | -82.71 | 1590 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -55.11 | -99.61 | 6104 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.92 | -42.64 | -92.15 | 2554 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.90 | -39.32 | -94.92 | 3252 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.29 | -99.81 | 6195 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.41 | -43.39 | -92.65 | 2271 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.58 | -26.06 | -76.28 | 1650 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -61.25 | -97.71 | 3425 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.37 | -99.07 | 4968 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.60 | -29.47 | -70.00 | 1235 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -57.12 | -94.65 | 2758 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.62 | -38.18 | -84.97 | 1735 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.29 | -99.70 | 6384 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.87 | -31.21 | -91.06 | 2372 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.96 | -18.96 | -80.38 | 1840 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.47 | -36.85 | -91.60 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.58 | -46.39 | -97.60 | 3920 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -59.01 | -89.35 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.22 | -30.00 | -67.11 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.61 | -24.08 | -73.07 | 1219 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.59 | -18.36 | -81.89 | 1770 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -46.32 | -97.61 | 4329 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.80 | -99.94 | 8451 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T17:55 | Agent (ML meta-label) | sell | TSLA | 2.16 | 0.00 | selected signal exited |
| 2026-11-18T17:55 | Agent (ML meta-label) | sell | AAPL | 4.63 | -0.00 | selected signal exited |
| 2026-11-18T17:50 | Agent (ML meta-label) | buy | TSLA | 2.16 | — | following Stochastic reversion |
| 2026-11-18T17:50 | Agent (ML meta-label) | sell | ETHU | 2.16 | -0.01 | selected signal exited |
| 2026-11-18T17:50 | MFI reversion · 1h | buy | QQQ | 7.08 | — | entry |
| 2026-11-18T17:50 | MFI reversion · 1h | buy | MSTR | 3.80 | — | rebalance up |
| 2026-11-18T17:50 | MFI reversion · 1h | buy | META | 7.08 | — | entry |
| 2026-11-18T17:50 | MFI reversion · 1h | sell | SPY | 4.73 | -0.01 | rebalance down |
| 2026-11-18T17:50 | MFI reversion · 1h | sell | LABU | 4.72 | -0.00 | rebalance down |
| 2026-11-18T17:50 | MFI reversion · 1h | sell | GOOGL | 4.69 | -0.01 | rebalance down |
| 2026-11-18T17:50 | MFI reversion · 1h | sell | AMD | 4.81 | 0.03 | rebalance down |
| 2026-11-18T17:45 | Agent (ML meta-label) | buy | ETHU | 2.17 | — | entry |
| 2026-11-18T17:45 | Agent (ML meta-label) | buy | AAPL | 4.63 | — | entry |
| 2026-11-18T17:40 | Agent (ML meta-label) | sell | AAPL | 6.06 | -0.00 | selected signal exited |
| 2026-11-18T17:35 | Agent (ML meta-label) | buy | AAPL | 6.07 | — | entry |
| 2026-11-18T17:35 | Agent (ML meta-label) | sell | ETHU | 6.81 | 0.08 | selected signal exited |
| 2026-11-18T17:35 | Opening range 15m | buy | LABU | 12.84 | — | entry signal |
| 2026-11-18T17:35 | Opening range 15m | sell | TNA | 4.44 | 0.11 | rebalance down |
| 2026-11-18T17:35 | Opening range 15m | sell | IWM | 4.12 | 0.03 | rebalance down |
| 2026-11-18T17:35 | Opening range 15m | sell | AMZN | 4.27 | 0.05 | rebalance down |
| 2026-11-18T17:30 | Agent (ML meta-label) | buy | TQQQ | 6.66 | — | entry |
| 2026-11-18T17:30 | Agent (ML meta-label) | buy | ETHU | 6.73 | — | entry |
| 2026-11-18T17:30 | MFI reversion · 1h | buy | MSTR | 3.29 | — | entry signal |
| 2026-11-18T17:30 | MFI reversion · 1h | buy | MSFT | 10.15 | — | entry signal |
| 2026-11-18T17:30 | MFI reversion · 1h | buy | ETHU | 10.15 | — | entry signal |
| 2026-11-18T17:30 | MFI reversion · 1h | sell | AMZN | 11.88 | 0.23 | exit signal |
| 2026-11-18T17:30 | CCI reversion · 1h | buy | TQQQ | 4.25 | — | entry |
| 2026-11-18T17:30 | CCI reversion · 1h | sell | AMZN | 4.25 | 0.16 | exit signal |
| 2026-11-18T17:30 | Williams %R · 1h | buy | BITX | 1.24 | — | entry signal |
| 2026-11-18T17:30 | Z-score reversion · 1h | buy | META | 2.74 | — | entry signal |
| 2026-11-18T17:30 | Z-score reversion · 1h | buy | COIN | 5.28 | — | entry signal |
| 2026-11-18T17:30 | Z-score reversion · 1h | sell | AMZN | 7.45 | 0.24 | exit signal |
| 2026-11-18T17:30 | Bollinger reversion · 1h | buy | UPRO | 4.81 | — | rebalance up |
| 2026-11-18T17:30 | Bollinger reversion · 1h | buy | TNA | 4.68 | — | rebalance up |
| 2026-11-18T17:30 | Bollinger reversion · 1h | buy | SPY | 4.79 | — | rebalance up |
| 2026-11-18T17:30 | Bollinger reversion · 1h | buy | MSFT | 5.02 | — | rebalance up |
| 2026-11-18T17:30 | Bollinger reversion · 1h | buy | IWM | 4.75 | — | rebalance up |
| 2026-11-18T17:30 | Bollinger reversion · 1h | sell | TSLA | 8.17 | 0.18 | exit signal |
| 2026-11-18T17:30 | Bollinger reversion · 1h | sell | AAPL | 8.11 | 0.06 | exit signal |
| 2026-11-18T17:30 | RSI(14) reversion · 1h | buy | COIN | 3.01 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 17:57:05.000113+00:00 -> 2026-11-18 18:07:05.000113+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 17:57:05.000113+00:00 -> 2026-11-18 18:07:05.000113+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
