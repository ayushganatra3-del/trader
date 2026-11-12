# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T19:40:05.000133+00:00 · 57281 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.69 (-14.31%)

Closed trades 187, win rate 35.3%, fees £5.51, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 17.11 | -0.04 |
| SQQQ | 17.24 | +0.07 |

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

Today: 34514 decisions in 3065 calls, $0.4298 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T19:40 | 0 / 5 / 26 | cash |  |
| Breezy | 2026-11-12T19:40 | 0 / 25 / 6 | cash |  |
| Boozy | 2026-11-12T19:40 | 2 / 21 / 8 | COIN 53% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.40 | +8.04% | 5 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.30 | 17.30 | 0 | — | 14.51 | 4.85 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.62 | 12.62 | 21 | 66.7 | 18.96 | 3.75 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.73 | 11.73 | 33 | 27.3 | 19.98 | 2.98 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.24 | 4.24 | 0 | — | 6.35 | 1.75 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.53 | 0.53 | 137 | 33.6 | 6.96 | 2.75 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.39 | 1.82 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -2.56 | 0.06 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.62 | -1.38 | 0 | — | -0.41 | -0.06 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 97.84 | -2.16 | 190 | 30.5 | -2.60 | -0.92 | -9.43 | 174 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.82 | -2.18 | 1 | 0.0 | -2.18 | -1.50 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.73 | -3.27 | 0 | — | -3.56 | -0.90 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.39 | -4.61 | 142 | 47.2 | -12.85 | -3.33 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 95.35 | -4.65 | 43 | 39.5 | -6.20 | -1.20 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.67 | -5.33 | 0 | — | -3.04 | -0.77 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 93.01 | -6.99 | 1 | 0.0 | -7.31 | -1.63 | -16.91 | 2 |
| 21 | Trend pullback · 1h | trend | 91.91 | -8.09 | 110 | 22.7 | -13.18 | -4.59 | -17.79 | 73 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -7.23 | -2.29 | -14.89 | 74 |
| 23 | Parabolic SAR · 1h | trend | 86.19 | -13.81 | 171 | 27.5 | -13.99 | -2.98 | -21.98 | 221 |
| 24 | Opening range 30m | breakout | 85.90 | -14.10 | 419 | 32.7 | -10.21 | -3.23 | -14.11 | 601 |
| 25 | Agent | meta | 85.69 | -14.31 | 187 | 35.3 | -15.07 | -7.61 | -15.54 | 211 |
| 26 | Daily: Bullish score | daily | 84.93 | -15.07 | 16 | 18.8 | -10.42 | -1.62 | -19.56 | 15 |
| 27 | Hold BTC | benchmark | 84.25 | -15.75 | 1 | 0.0 | -7.99 | -1.02 | -18.34 | 1 |
| 28 | Donchian 55/20 · 1h | breakout | 83.98 | -16.02 | 73 | 13.7 | -22.41 | -4.69 | -29.68 | 94 |
| 29 | Agent (aggressive) | meta | 83.98 | -16.02 | 91 | 34.1 | -17.00 | -4.79 | -18.70 | 104 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.68 | -17.32 | 2 | 0.0 | -7.97 | -0.87 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.50 | -18.50 | 114 | 23.7 | -18.08 | -3.73 | -25.87 | 176 |
| 32 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -26.78 | -1.40 | -45.81 | 24 |
| 33 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 210 | 40.5 | -17.97 | -6.24 | -18.78 | 118 |
| 34 | ADX DI cross · 1h | trend | 80.97 | -19.03 | 191 | 19.4 | -21.26 | -3.30 | -30.22 | 267 |
| 35 | Volume breakout · 1h | breakout | 80.23 | -19.77 | 158 | 28.5 | -13.74 | -3.21 | -21.12 | 91 |
| 36 | MFI reversion · 1h | reversion | 79.77 | -20.23 | 382 | 35.9 | -18.05 | -2.29 | -23.02 | 162 |
| 37 | Stochastic reversion · 1h | reversion | 79.54 | -20.46 | 297 | 47.5 | -27.17 | -4.05 | -27.73 | 390 |
| 38 | Opening range 15m | breakout | 78.20 | -21.80 | 513 | 31.2 | -17.60 | -4.74 | -21.36 | 715 |
| 39 | Heikin-Ashi · 1h | trend | 77.71 | -22.29 | 434 | 24.7 | -36.03 | -6.73 | -38.20 | 658 |
| 40 | MACD cross · 1h | trend | 77.11 | -22.89 | 371 | 22.1 | -28.88 | -4.44 | -38.74 | 466 |
| 41 | Bollinger breakout · 1h | breakout | 76.24 | -23.76 | 179 | 22.3 | -22.20 | -4.59 | -29.88 | 241 |
| 42 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -19.40 | -0.55 | -57.50 | 41 |
| 43 | MACD zero-line · 1h | trend | 75.59 | -24.41 | 164 | 17.1 | -21.78 | -4.25 | -30.95 | 204 |
| 44 | Supertrend · 1h | trend | 75.43 | -24.57 | 172 | 14.0 | -27.68 | -4.77 | -35.57 | 217 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 46 | RSI momentum · 1h | momentum | 74.95 | -25.05 | 162 | 13.6 | -25.01 | -3.89 | -37.22 | 211 |
| 47 | EMA 20/50 cross · 1h | trend | 74.53 | -25.47 | 105 | 10.5 | -26.79 | -4.52 | -37.91 | 120 |
| 48 | Daily: Momentum burst | daily | 74.19 | -25.81 | 27 | 11.1 | -34.32 | -4.70 | -37.79 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.24 | -26.76 | 147 | 14.3 | -26.79 | -4.41 | -37.61 | 205 |
| 50 | ROC + volume · 1h | momentum | 72.98 | -27.02 | 385 | 27.8 | -31.41 | -5.90 | -38.37 | 378 |
| 51 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -36.95 | -5.71 | -36.96 | 457 |
| 52 | Bollinger reversion · 1h | reversion | 72.20 | -27.80 | 290 | 41.0 | -31.79 | -4.92 | -35.67 | 378 |
| 53 | Donchian 20/10 · 1h | breakout | 72.00 | -28.00 | 145 | 19.3 | -28.13 | -5.12 | -35.89 | 211 |
| 54 | OBV trend · 1h | momentum | 71.52 | -28.48 | 289 | 19.4 | -27.66 | -4.77 | -37.30 | 269 |
| 55 | Williams %R · 1h ⏸ | reversion | 67.95 | -32.05 | 372 | 43.8 | -41.56 | -6.79 | -41.72 | 529 |
| 56 | Z-score reversion · 1h | reversion | 67.66 | -32.34 | 199 | 38.2 | -27.63 | -3.82 | -29.17 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 67.15 | -32.85 | 257 | 9.7 | -33.34 | -6.17 | -41.74 | 332 |
| 58 | VWAP momentum · 1h | momentum | 66.30 | -33.70 | 890 | 22.4 | -51.42 | -10.48 | -51.88 | 1215 |
| 59 | Agent (ML meta-label) | meta | 66.19 | -33.81 | 1813 | 24.9 | -24.16 | -3.01 | -28.78 | 357 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -32.97 | -4.60 | -35.15 | 245 |
| 61 | Candlestick reversal · 1h | reversion | 62.71 | -37.28 | 469 | 28.4 | -41.34 | -7.32 | -41.34 | 592 |
| 62 | Three white soldiers | momentum | 58.62 | -41.38 | 537 | 14.5 | -49.62 | -22.55 | -49.62 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -44.87 | -99.01 | 5264 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.19 | -25.98 | -80.19 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.78 | -46.52 | -93.79 | 2533 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.39 | -32.19 | -89.54 | 1920 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -41.27 | -91.20 | 2330 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.13 | -32.02 | -90.18 | 2213 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -53.93 | -97.90 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.36 | -57.87 | -96.36 | 3427 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.49 | -32.32 | -93.50 | 2317 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.11 | -34.70 | -83.11 | 1657 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -55.47 | -99.57 | 5977 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.25 | -43.93 | -92.26 | 2605 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -37.16 | -95.42 | 3473 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -79.20 | -99.82 | 6140 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.39 | -44.23 | -92.41 | 2275 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.18 | -25.37 | -75.23 | 1621 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -61.08 | -97.68 | 3517 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -63.94 | -98.88 | 4910 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.46 | -27.04 | -68.53 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.78 | -58.90 | -94.80 | 2782 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.07 | -39.44 | -85.07 | 1789 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.31 | -99.65 | 6344 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.93 | -32.59 | -90.00 | 2295 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.90 | -19.91 | -78.30 | 1758 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.73 | -36.84 | -90.84 | 2178 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.87 | -52.45 | -96.87 | 3853 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.16 | -57.90 | -89.16 | 2143 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.23 | -30.35 | -66.23 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.49 | -23.17 | -71.58 | 1254 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.11 | -18.88 | -79.40 | 1711 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.30 | -49.96 | -97.32 | 4300 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -117.03 | -99.93 | 8369 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-12T19:31 | MFI reversion · 1h | buy | XRP-USD | 4.12 | — | rebalance up |
| 2026-11-12T19:31 | MFI reversion · 1h | sell | LABU | 6.12 | -0.06 | target is flat |
| 2026-11-12T19:31 | Candlestick reversal · 1h | sell | META | 5.73 | -0.03 | exit signal |
| 2026-11-12T19:31 | VWAP momentum · 1h | buy | TECL | 1.85 | — | entry signal |
| 2026-11-12T19:31 | VWAP momentum · 1h | buy | PLTR | 6.05 | — | entry signal |
| 2026-11-12T19:31 | VWAP momentum · 1h | buy | MSTR | 6.05 | — | entry signal |
| 2026-11-12T19:31 | VWAP momentum · 1h | buy | COIN | 6.05 | — | entry signal |
| 2026-11-12T19:31 | VWAP momentum · 1h | sell | TSLA | 5.92 | -0.03 | exit signal |
| 2026-11-12T19:31 | VWAP momentum · 1h | sell | SPY | 6.69 | -0.03 | exit signal |
| 2026-11-12T19:31 | VWAP momentum · 1h | sell | QQQ | 7.40 | -0.03 | exit signal |
| 2026-11-12T19:31 | Trend pullback · 1h | sell | IWM | 22.93 | -0.16 | exit signal |
| 2026-11-12T19:31 | Heikin-Ashi · 1h | sell | MSFT | 19.19 | -0.20 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 19:40:05.000133+00:00 -> 2026-11-12 19:50:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
