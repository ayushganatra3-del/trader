# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T19:27:05.000134+00:00 · 64765 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.95 (-15.05%)

Closed trades 223, win rate 35.9%, fees £6.15, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 17.08 | +0.11 |

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

Today: 32565 decisions in 3009 calls, $0.4072 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T19:27 | 3 / 14 / 12 | AMD 15% |  |
| Breezy | 2026-11-18T19:27 | 0 / 28 / 1 | cash |  |
| Boozy | 2026-11-18T19:27 | 5 / 24 / 0 | COIN 59% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |
| OBV trend | SQQQ | 1.76 | +6.31% | 9 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.70 | 14.70 | 0 | — | 13.11 | 4.37 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.09 | 3.70 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.01 | 4.01 | 0 | — | 4.63 | 1.32 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.14 | 0.14 | 150 | 34.7 | -3.59 | -3.17 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.19 | 1.09 | -9.06 | 207 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.19 | -3.81 | 8 | 50.0 | -4.29 | -0.15 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.70 | -4.30 | 0 | — | -3.84 | -1.26 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.18 | -1.47 | -8.74 | 148 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.26 | -8.34 | -5.84 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.47 | -7.53 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.51 | -8.49 | 0 | — | -7.25 | -1.93 | -12.67 | 1 |
| 18 | Copy: Insider buying | copy | 90.73 | -9.27 | 52 | 40.4 | -9.77 | -1.96 | -14.79 | 64 |
| 19 | Trend pullback · 1h | trend | 90.24 | -9.76 | 113 | 23.9 | -12.60 | -6.94 | -12.99 | 57 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -11.42 | -3.36 | -18.48 | 147 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.06 | -12.94 | 17 | 17.6 | -5.28 | -0.84 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.00 | -8.98 | -16.05 | 70 |
| 24 | Agent | meta | 84.95 | -15.05 | 223 | 35.9 | -15.05 | -7.28 | -17.06 | 202 |
| 25 | Opening range 30m | breakout | 84.77 | -15.23 | 443 | 33.4 | -10.76 | -3.38 | -14.65 | 566 |
| 26 | Agent (aggressive) | meta | 83.61 | -16.39 | 104 | 33.7 | -15.42 | -4.05 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.69 | -18.32 | 188 | 28.2 | -24.32 | -6.72 | -27.42 | 200 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.42 | -6.42 | -14.74 | 86 |
| 29 | Keltner breakout · 1h | breakout | 79.88 | -20.12 | 124 | 25.8 | -24.66 | -6.63 | -27.09 | 154 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.07 | -5.20 | -21.17 | 73 |
| 31 | Max aggression: 5-day momentum | meta | 79.14 | -20.86 | 21 | 42.9 | -47.99 | -3.21 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.95 | -21.05 | 78 | 12.8 | -25.51 | -6.70 | -30.57 | 84 |
| 33 | Opening range 15m | breakout | 77.46 | -22.54 | 537 | 31.5 | -20.20 | -6.01 | -21.80 | 670 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.09 | -22.91 | 2 | 0.0 | -18.72 | -2.54 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.17 | -24.84 | 209 | 19.1 | -27.23 | -4.46 | -35.44 | 269 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 37 | Hold BTC | benchmark | 73.66 | -26.34 | 2 | 0.0 | -18.34 | -2.55 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -31.10 | -8.40 | -34.15 | 217 |
| 39 | Stochastic reversion · 1h | reversion | 72.95 | -27.05 | 350 | 42.3 | -34.34 | -5.22 | -35.59 | 426 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -39.70 | -2.43 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.77 | -28.23 | 191 | 16.2 | -32.21 | -5.44 | -39.50 | 202 |
| 42 | Triple EMA stack · 1h | trend | 70.82 | -29.18 | 156 | 14.7 | -30.34 | -6.05 | -36.85 | 175 |
| 43 | MFI reversion · 1h | reversion | 70.64 | -29.36 | 448 | 33.5 | -27.04 | -4.00 | -30.08 | 171 |
| 44 | RSI momentum · 1h | momentum | 70.35 | -29.65 | 179 | 14.5 | -31.24 | -5.65 | -38.17 | 199 |
| 45 | MACD zero-line · 1h | trend | 69.83 | -30.17 | 184 | 17.9 | -27.83 | -5.56 | -33.94 | 202 |
| 46 | Heikin-Ashi · 1h | trend | 69.66 | -30.34 | 474 | 23.0 | -44.86 | -9.87 | -45.81 | 633 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.36 | -30.64 | 116 | 10.3 | -36.29 | -9.35 | -40.28 | 117 |
| 49 | ROC + volume · 1h | momentum | 68.66 | -31.34 | 413 | 28.1 | -33.69 | -6.15 | -39.35 | 342 |
| 50 | OBV trend · 1h | momentum | 68.25 | -31.75 | 310 | 19.4 | -34.92 | -7.47 | -39.78 | 253 |
| 51 | MACD cross · 1h | trend | 67.66 | -32.34 | 417 | 22.3 | -40.36 | -6.59 | -46.29 | 491 |
| 52 | CCI reversion · 1h | reversion | 67.24 | -32.76 | 386 | 41.5 | -42.25 | -7.10 | -44.29 | 475 |
| 53 | Donchian 20/10 · 1h | breakout | 66.53 | -33.47 | 162 | 17.9 | -36.97 | -7.09 | -41.40 | 199 |
| 54 | Bollinger reversion · 1h | reversion | 63.85 | -36.15 | 348 | 37.9 | -38.79 | -5.91 | -39.58 | 417 |
| 55 | Williams %R · 1h | reversion | 63.65 | -36.35 | 436 | 40.6 | -46.81 | -8.20 | -47.63 | 572 |
| 56 | EMA 9/21 cross · 1h | trend | 62.98 | -37.02 | 284 | 11.3 | -40.26 | -7.88 | -46.27 | 322 |
| 57 | Agent (ML meta-label) | meta | 60.00 | -40.00 | 1935 | 24.6 | -24.25 | -4.44 | -25.53 | 313 |
| 58 | RSI(14) reversion · 1h | reversion | 58.98 | -41.02 | 206 | 32.0 | -41.50 | -6.20 | -43.32 | 253 |
| 59 | Z-score reversion · 1h | reversion | 57.58 | -42.42 | 227 | 35.2 | -36.82 | -5.09 | -39.63 | 258 |
| 60 | VWAP momentum · 1h | momentum | 55.28 | -44.72 | 976 | 21.7 | -56.15 | -11.13 | -59.88 | 1204 |
| 61 | Candlestick reversal · 1h | reversion | 55.19 | -44.81 | 552 | 26.4 | -47.48 | -8.72 | -48.88 | 643 |
| 62 | Three white soldiers | momentum | 54.75 | -45.25 | 588 | 14.5 | -49.66 | -21.86 | -50.71 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -42.98 | -99.04 | 5270 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.45 | -25.65 | -82.57 | 1411 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.74 | -42.28 | -93.98 | 2459 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.90 | -31.31 | -90.36 | 1942 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.04 | -38.46 | -91.48 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.02 | -30.87 | -90.14 | 2082 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -47.64 | -97.94 | 3475 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -52.71 | -96.42 | 3388 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.43 | -37.97 | -93.44 | 2196 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.49 | -34.34 | -82.82 | 1589 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.99 | -99.61 | 6101 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.89 | -43.02 | -92.15 | 2548 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.79 | -39.03 | -94.80 | 3232 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.41 | -99.81 | 6194 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.41 | -42.55 | -92.66 | 2266 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.19 | -27.38 | -76.60 | 1641 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -61.62 | -97.72 | 3434 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.39 | -99.07 | 4966 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.21 | -28.61 | -70.12 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -55.80 | -94.67 | 2752 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.62 | -36.92 | -85.12 | 1734 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.18 | -99.70 | 6395 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.82 | -31.27 | -91.03 | 2362 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.95 | -19.08 | -80.36 | 1840 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.39 | -36.82 | -91.53 | 2164 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.59 | -46.62 | -97.61 | 3916 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -59.70 | -89.36 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.17 | -30.93 | -66.94 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.71 | -24.33 | -73.12 | 1218 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.55 | -18.37 | -81.88 | 1766 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -46.20 | -97.59 | 4327 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -115.41 | -99.94 | 8451 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T19:25 | Agent (ML meta-label) | buy | TSLA | 2.77 | — | following Stochastic reversion |
| 2026-11-18T19:25 | Agent (ML meta-label) | buy | IWM | 4.74 | — | rebalance up |
| 2026-11-18T19:25 | Agent (ML meta-label) | sell | TECL | 7.52 | 0.04 | selected signal exited |
| 2026-11-18T19:20 | Agent (aggressive) | buy | SOXL | 41.67 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T19:20 | Agent | buy | SOXL | 16.97 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T19:15 | Agent (ML meta-label) | buy | IWM | 1.26 | — | entry |
| 2026-11-18T19:15 | Agent (ML meta-label) | buy | AAPL | 5.44 | — | entry |
| 2026-11-18T19:10 | Agent (ML meta-label) | buy | TECL | 7.47 | — | entry |
| 2026-11-18T19:10 | Agent (ML meta-label) | sell | TSLA | 2.72 | -0.01 | selected signal exited |
| 2026-11-18T19:10 | Agent (ML meta-label) | sell | IWM | 5.99 | -0.02 | selected signal exited |
| 2026-11-18T19:10 | Agent (ML meta-label) | sell | AAPL | 5.46 | -0.02 | selected signal exited |
| 2026-11-18T19:06 | Agent (ML meta-label) | buy | TSLA | 2.74 | — | following Stochastic reversion |
| 2026-11-18T19:06 | Agent (ML meta-label) | buy | IWM | 4.01 | — | rebalance up |
| 2026-11-18T19:06 | Agent (ML meta-label) | sell | TECL | 6.75 | 0.11 | selected signal exited |
| 2026-11-18T19:06 | MFI reversion · 1h | buy | TQQQ | 1.19 | — | entry |
| 2026-11-18T19:06 | MFI reversion · 1h | buy | ETHU | 5.89 | — | entry |
| 2026-11-18T19:06 | MFI reversion · 1h | sell | META | 7.06 | -0.02 | target is flat |
| 2026-11-18T19:06 | Opening range 15m | buy | TNA | 3.98 | — | rebalance up |
| 2026-11-18T19:06 | Opening range 15m | sell | LABU | 12.53 | -0.31 | stop-loss |
| 2026-11-18T19:00 | Agent (ML meta-label) | buy | IWM | 1.99 | — | entry |
| 2026-11-18T19:00 | Agent (ML meta-label) | buy | AAPL | 5.48 | — | entry |
| 2026-11-18T18:58 | Agent (ML meta-label) | sell | TSLA | 1.45 | -0.00 | selected signal exited |
| 2026-11-18T18:58 | Agent (ML meta-label) | sell | AAPL | 6.03 | -0.01 | selected signal exited |
| 2026-11-18T18:56 | Agent (ML meta-label) | buy | TSLA | 1.45 | — | following Stochastic reversion |
| 2026-11-18T18:56 | Agent (ML meta-label) | buy | TNA | 6.04 | — | entry |
| 2026-11-18T18:56 | Agent (ML meta-label) | buy | AAPL | 6.04 | — | entry |
| 2026-11-18T18:50 | Agent (ML meta-label) | sell | TNA | 7.54 | 0.02 | selected signal exited |
| 2026-11-18T18:50 | Agent (ML meta-label) | sell | ETHU | 5.98 | -0.01 | selected signal exited |
| 2026-11-18T18:46 | Agent (ML meta-label) | buy | ETHU | 5.99 | — | entry |
| 2026-11-18T18:37 | Copy: Insider buying | buy | STWD | 7.78 | — | rebalance up |
| 2026-11-18T18:37 | Copy: Insider buying | buy | PEPG | 11.38 | — | entry |
| 2026-11-18T18:37 | Copy: Insider buying | sell | PAM | 8.65 | -0.07 | target is flat |
| 2026-11-18T18:37 | Copy: Insider buying | sell | HUBS | 10.51 | -0.83 | target is flat |
| 2026-11-18T18:30 | Agent (ML meta-label) | buy | TNA | 7.52 | — | entry |
| 2026-11-18T18:30 | Keltner breakout · 1h | buy | AMZN | 19.96 | — | entry signal |
| 2026-11-18T18:30 | VWAP momentum · 1h | buy | MSFT | 4.16 | — | entry signal |
| 2026-11-18T18:30 | VWAP momentum · 1h | sell | SOXL | 4.16 | -0.13 | exit signal |
| 2026-11-18T18:30 | Trend pullback · 1h | buy | SQQQ | 22.58 | — | entry signal |
| 2026-11-18T18:27 | Agent (ML meta-label) | sell | TNA | 6.73 | 0.04 | selected signal exited |
| 2026-11-18T18:25 | MFI reversion · 1h | buy | TNA | 5.89 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 19:27:05.000134+00:00 -> 2026-11-18 19:37:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 19:27:05.000134+00:00 -> 2026-11-18 19:37:05.000134+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
