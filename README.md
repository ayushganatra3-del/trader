# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T20:10:05.000123+00:00 · 57310 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.74 (-14.26%)

Closed trades 187, win rate 35.3%, fees £5.52, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 17.14 | -0.00 |
| LABU | 17.16 | +0.01 |
| SQQQ | 17.25 | +0.08 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-12 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 37106 decisions in 3152 calls, $0.4601 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T20:10 | 3 / 14 / 13 | cash |  |
| Breezy | 2026-11-12T20:10 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-12T20:10 | 5 / 20 / 5 | ETHU 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.14 | 17.14 | 0 | — | 14.69 | 4.92 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.52 | 12.52 | 21 | 66.7 | 16.07 | 3.29 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.63 | 11.62 | 33 | 27.3 | 19.87 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.18 | 4.18 | 0 | — | 6.29 | 1.74 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.60 | 0.60 | 137 | 33.6 | 6.96 | 2.76 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.44 | 1.84 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.58 | -1.42 | 0 | — | -0.20 | 0.01 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.79 | -2.21 | 1 | 0.0 | -2.20 | -1.52 | -5.83 | 2 |
| 13 | Agent (rotation) | meta | 97.78 | -2.22 | 190 | 30.5 | -1.14 | -0.36 | -8.69 | 167 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.73 | -3.27 | 0 | — | -3.56 | -0.90 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.52 | -4.47 | 142 | 47.2 | -12.73 | -3.30 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 94.77 | -5.23 | 43 | 39.5 | -6.80 | -1.33 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.20 | -5.80 | 0 | — | -4.14 | -1.09 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 92.92 | -7.08 | 1 | 0.0 | -7.39 | -1.65 | -16.91 | 2 |
| 21 | Trend pullback · 1h | trend | 91.87 | -8.13 | 110 | 22.7 | -12.99 | -4.52 | -17.58 | 73 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Parabolic SAR · 1h | trend | 86.15 | -13.85 | 171 | 27.5 | -13.83 | -2.94 | -21.80 | 219 |
| 24 | Opening range 30m | breakout | 85.96 | -14.04 | 420 | 32.6 | -10.18 | -3.22 | -14.11 | 601 |
| 25 | Agent | meta | 85.74 | -14.26 | 187 | 35.3 | -14.59 | -7.30 | -15.16 | 215 |
| 26 | Daily: Bullish score | daily | 84.91 | -15.09 | 16 | 18.8 | -10.97 | -1.77 | -19.56 | 15 |
| 27 | Hold BTC | benchmark | 84.36 | -15.64 | 1 | 0.0 | -7.81 | -1.00 | -18.34 | 1 |
| 28 | Donchian 55/20 · 1h | breakout | 84.04 | -15.96 | 73 | 13.7 | -22.45 | -4.70 | -29.68 | 94 |
| 29 | Agent (aggressive) | meta | 84.00 | -16.00 | 91 | 34.1 | -17.28 | -4.86 | -18.70 | 104 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.49 | -17.52 | 2 | 0.0 | -8.28 | -0.92 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.63 | -18.37 | 114 | 23.7 | -15.32 | -3.05 | -25.14 | 169 |
| 32 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -33.16 | -2.04 | -45.81 | 22 |
| 33 | ADX DI cross · 1h | trend | 81.14 | -18.86 | 191 | 19.4 | -20.22 | -3.08 | -29.51 | 269 |
| 34 | Connors RSI(2) · 1h | reversion | 81.03 | -18.97 | 210 | 40.5 | -17.87 | -6.27 | -18.41 | 115 |
| 35 | Volume breakout · 1h | breakout | 80.26 | -19.74 | 158 | 28.5 | -12.39 | -2.87 | -21.12 | 90 |
| 36 | MFI reversion · 1h | reversion | 79.92 | -20.08 | 382 | 35.9 | -18.10 | -2.29 | -23.02 | 163 |
| 37 | Stochastic reversion · 1h | reversion | 79.66 | -20.34 | 297 | 47.5 | -26.77 | -3.97 | -27.43 | 389 |
| 38 | Opening range 15m | breakout | 78.22 | -21.78 | 513 | 31.2 | -17.51 | -4.71 | -21.36 | 715 |
| 39 | Heikin-Ashi · 1h | trend | 77.78 | -22.22 | 434 | 24.7 | -36.05 | -6.73 | -38.20 | 657 |
| 40 | MACD cross · 1h | trend | 77.08 | -22.92 | 371 | 22.1 | -27.56 | -4.08 | -38.65 | 467 |
| 41 | Bollinger breakout · 1h | breakout | 76.48 | -23.52 | 179 | 22.3 | -21.04 | -4.34 | -29.92 | 239 |
| 42 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -15.77 | -0.35 | -57.50 | 40 |
| 43 | MACD zero-line · 1h | trend | 75.58 | -24.42 | 164 | 17.1 | -21.83 | -4.26 | -30.99 | 204 |
| 44 | Supertrend · 1h | trend | 75.46 | -24.54 | 172 | 14.0 | -27.93 | -4.79 | -36.51 | 212 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 46 | RSI momentum · 1h | momentum | 74.99 | -25.01 | 162 | 13.6 | -24.15 | -3.73 | -36.35 | 212 |
| 47 | EMA 20/50 cross · 1h | trend | 74.64 | -25.36 | 105 | 10.5 | -27.69 | -4.68 | -38.62 | 124 |
| 48 | Daily: Momentum burst | daily | 74.25 | -25.75 | 27 | 11.1 | -30.18 | -4.07 | -36.97 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.39 | -26.61 | 147 | 14.3 | -26.28 | -4.30 | -37.19 | 205 |
| 50 | ROC + volume · 1h | momentum | 73.03 | -26.96 | 385 | 27.8 | -29.98 | -5.56 | -38.32 | 374 |
| 51 | Bollinger reversion · 1h | reversion | 72.30 | -27.70 | 290 | 41.0 | -31.74 | -4.92 | -35.72 | 378 |
| 52 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -36.47 | -5.65 | -36.64 | 457 |
| 53 | Donchian 20/10 · 1h | breakout | 72.05 | -27.95 | 145 | 19.3 | -27.22 | -4.92 | -35.90 | 209 |
| 54 | OBV trend · 1h | momentum | 71.59 | -28.41 | 289 | 19.4 | -26.78 | -4.62 | -36.52 | 275 |
| 55 | Z-score reversion · 1h | reversion | 67.95 | -32.05 | 199 | 38.2 | -27.31 | -3.79 | -29.17 | 236 |
| 56 | Williams %R · 1h ⏸ | reversion | 67.95 | -32.05 | 372 | 43.8 | -41.86 | -6.88 | -42.09 | 528 |
| 57 | EMA 9/21 cross · 1h | trend | 67.17 | -32.83 | 257 | 9.7 | -35.43 | -7.26 | -41.97 | 330 |
| 58 | VWAP momentum · 1h | momentum | 66.30 | -33.70 | 890 | 22.4 | -51.45 | -10.49 | -51.91 | 1215 |
| 59 | Agent (ML meta-label) | meta | 66.20 | -33.80 | 1817 | 24.8 | -21.24 | -2.84 | -24.80 | 350 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -36.61 | -5.35 | -36.83 | 241 |
| 61 | Candlestick reversal · 1h | reversion | 62.83 | -37.17 | 469 | 28.4 | -43.82 | -8.07 | -43.98 | 590 |
| 62 | Three white soldiers | momentum | 58.62 | -41.38 | 537 | 14.5 | -49.70 | -22.55 | -49.70 | 664 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.74 | -99.00 | 5265 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.90 | -25.57 | -79.90 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.78 | -46.45 | -93.78 | 2533 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.69 | -89.44 | 1917 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -41.24 | -91.19 | 2330 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.95 | -31.71 | -90.00 | 2206 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -53.83 | -97.90 | 3481 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -57.63 | -96.35 | 3425 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.54 | -32.62 | -93.56 | 2327 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.15 | -34.81 | -83.15 | 1659 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.76 | -99.57 | 5978 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.27 | -43.97 | -92.27 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -37.10 | -95.41 | 3471 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -79.09 | -99.82 | 6150 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.38 | -44.17 | -92.40 | 2267 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.28 | -25.46 | -75.31 | 1620 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -61.37 | -97.67 | 3520 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -63.87 | -98.88 | 4917 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.64 | -27.24 | -68.68 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.80 | -59.00 | -94.80 | 2784 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.11 | -39.48 | -85.11 | 1781 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.42 | -99.65 | 6344 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.95 | -32.55 | -90.00 | 2300 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.73 | -19.80 | -78.10 | 1756 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.68 | -36.83 | -90.79 | 2179 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.87 | -52.52 | -96.87 | 3859 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.24 | -58.29 | -89.24 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.24 | -30.37 | -66.24 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.42 | -23.10 | -71.53 | 1254 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.17 | -18.97 | -79.45 | 1711 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.30 | -49.98 | -97.32 | 4303 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.99 | -99.93 | 8368 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T20:05 | Agent (ML meta-label) | buy | QQQ | 4.41 | — | entry |
| 2026-11-12T20:05 | Agent (ML meta-label) | sell | UPRO | 3.88 | -0.02 | selected signal exited |
| 2026-11-12T20:05 | Agent (ML meta-label) | sell | PLTR | 3.88 | -0.02 | selected signal exited |
| 2026-11-12T20:05 | Agent (ML meta-label) | sell | BITX | 3.89 | -0.01 | selected signal exited |
| 2026-11-12T20:05 | Opening range 30m | sell | UPRO | 6.13 | -0.05 | stop-loss |
| 2026-11-12T20:00 | Agent (ML meta-label) | buy | BITX | 3.90 | — | entry |
| 2026-11-12T20:00 | Agent (ML meta-label) | sell | AAPL | 3.90 | -0.00 | selected signal exited |
| 2026-11-12T20:00 | Candlestick reversal · 1h | buy | DOGE-USD | 5.72 | — | entry signal |
| 2026-11-12T20:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.72 | — | entry signal |
| 2026-11-12T19:50 | Agent (aggressive) | buy | LABU | 41.99 | — | following MFI reversion |
| 2026-11-12T19:50 | Agent | buy | LABU | 17.15 | — | following MFI reversion |
| 2026-11-12T19:45 | MFI reversion · 1h | buy | SOXL | 6.25 | — | entry |
| 2026-11-12T19:40 | Opening range 15m | buy | COIN | 2.70 | — | entry |
| 2026-11-12T19:40 | Opening range 15m | buy | AMD | 6.02 | — | entry |
| 2026-11-12T19:40 | Opening range 15m | sell | MSFT | 8.72 | -0.03 | stop-loss |
| 2026-11-12T19:35 | Agent (ML meta-label) | buy | UPRO | 3.90 | — | following Gap and go |
| 2026-11-12T19:35 | Agent (ML meta-label) | buy | PLTR | 3.90 | — | entry |
| 2026-11-12T19:35 | Agent (ML meta-label) | buy | AAPL | 3.90 | — | entry |
| 2026-11-12T19:35 | Agent (ML meta-label) | sell | QQQ | 3.69 | -0.01 | selected signal exited |
| 2026-11-12T19:35 | Agent (aggressive) | sell | LABU | 41.73 | -0.52 | selected signal exited |
| 2026-11-12T19:35 | Agent | sell | LABU | 16.97 | -0.21 | selected signal exited |
| 2026-11-12T19:35 | Williams %R · 1h | sell | XRP-USD | 4.89 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | SQQQ | 4.95 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | SOL-USD | 4.88 | 0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | MSTR | 4.75 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | MSFT | 4.84 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | META | 4.85 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | LABU | 4.73 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | ETHU | 4.91 | -0.21 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | ETH-USD | 4.88 | 0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | DOGE-USD | 4.89 | 0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | COIN | 4.81 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | BTC-USD | 4.84 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | BITX | 4.85 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | Williams %R · 1h | sell | AMZN | 4.87 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T19:35 | VWAP momentum · 1h | buy | TECL | 4.80 | — | rebalance up |
| 2026-11-12T19:35 | VWAP momentum · 1h | sell | ETHU | 6.71 | -0.04 | target is flat |
| 2026-11-12T19:31 | Agent (ML meta-label) | sell | TSLA | 3.90 | -0.01 | selected signal exited |
| 2026-11-12T19:31 | Agent (ML meta-label) | sell | IWM | 3.91 | -0.01 | selected signal exited |
| 2026-11-12T19:31 | Agent | buy | AMD | 17.14 | — | following Parabolic SAR |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 20:10:05.000123+00:00 -> 2026-11-12 20:20:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
