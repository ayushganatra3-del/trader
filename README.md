# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T17:57:05.000164+00:00 · 54829 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.51 (-12.49%)

Closed trades 168, win rate 35.1%, fees £5.09, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 17.55 | +0.06 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-10 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 23900 decisions in 2635 calls, $0.3050 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T17:57 | 10 / 17 / 3 | AMD 16%, SOXL 15% |  |
| Breezy | 2026-11-10T17:57 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-10T17:57 | 9 / 20 / 1 | MSTR 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| MFI reversion | LABU | 1.77 | +6.58% | 4 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| MFI reversion | TSLA | 1.42 | +2.27% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.49 | 3.91 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.91 | 14.91 | 0 | — | 14.83 | 4.91 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.87 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.20 | 1.20 | 0 | — | 3.96 | 1.16 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.52 | 1.06 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -2.80 | -1.11 | -9.22 | 148 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.47 | -3.53 | 0 | — | -2.23 | -0.71 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.61 | -4.39 | 136 | 46.3 | -13.52 | -3.45 | -13.73 | 151 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.65 | -5.35 | 0 | — | -4.82 | -1.26 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.98 | -7.01 | 108 | 23.1 | -13.24 | -4.91 | -17.51 | 78 |
| 19 | Copy: Insider buying | copy | 92.44 | -7.56 | 42 | 38.1 | -8.47 | -1.76 | -15.11 | 67 |
| 20 | Copy: Congress Democrats (NANC) | copy | 92.17 | -7.83 | 0 | — | -4.44 | -1.16 | -10.64 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.28 | -2.87 | -14.15 | 77 |
| 23 | Opening range 30m | breakout | 88.71 | -11.29 | 403 | 33.3 | -14.71 | -4.56 | -14.77 | 605 |
| 24 | Agent | meta | 87.51 | -12.49 | 168 | 35.1 | -13.18 | -6.66 | -14.34 | 205 |
| 25 | Daily: Bullish score | daily | 86.89 | -13.11 | 15 | 20.0 | -8.31 | -1.24 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 85.67 | -14.34 | 1 | 0.0 | -7.01 | -0.94 | -16.64 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.21 | -14.79 | 168 | 26.8 | -13.66 | -2.78 | -21.70 | 224 |
| 28 | Agent (aggressive) | meta | 84.98 | -15.02 | 79 | 32.9 | -14.48 | -3.91 | -18.49 | 97 |
| 29 | Donchian 55/20 · 1h | breakout | 84.56 | -15.44 | 71 | 14.1 | -16.20 | -3.36 | -22.08 | 101 |
| 30 | Keltner breakout · 1h | breakout | 81.64 | -18.36 | 110 | 23.6 | -20.31 | -4.22 | -25.10 | 175 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 81.40 | -18.60 | 2 | 0.0 | -10.42 | -1.22 | -24.16 | 1 |
| 32 | Opening range 15m | breakout | 81.18 | -18.82 | 499 | 31.5 | -19.65 | -5.39 | -20.32 | 740 |
| 33 | Stochastic reversion · 1h | reversion | 80.84 | -19.16 | 284 | 47.5 | -26.22 | -3.85 | -27.87 | 390 |
| 34 | Connors RSI(2) · 1h | reversion | 80.83 | -19.17 | 206 | 39.8 | -19.58 | -6.52 | -19.99 | 126 |
| 35 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -15.42 | -3.59 | -22.08 | 93 |
| 36 | Max aggression: 5-day momentum | meta | 79.25 | -20.75 | 18 | 44.4 | -37.21 | -2.39 | -45.81 | 25 |
| 37 | Heikin-Ashi · 1h | trend | 78.90 | -21.10 | 416 | 24.5 | -40.18 | -7.47 | -42.50 | 664 |
| 38 | ADX DI cross · 1h | trend | 78.57 | -21.43 | 184 | 19.0 | -25.13 | -4.33 | -29.95 | 270 |
| 39 | CCI reversion · 1h | reversion | 77.26 | -22.74 | 326 | 45.1 | -25.82 | -3.91 | -30.69 | 453 |
| 40 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.33 | -4.40 | -27.99 | 236 |
| 41 | MFI reversion · 1h | reversion | 76.48 | -23.52 | 359 | 33.7 | -19.67 | -2.49 | -22.13 | 158 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.53 | -8.91 | -31.64 | 121 |
| 43 | EMA 20/50 cross · 1h | trend | 75.11 | -24.89 | 102 | 10.8 | -25.05 | -4.21 | -35.49 | 121 |
| 44 | MACD cross · 1h | trend | 74.13 | -25.87 | 359 | 22.0 | -32.86 | -5.41 | -39.48 | 470 |
| 45 | Bollinger reversion · 1h | reversion | 73.55 | -26.45 | 278 | 40.3 | -27.36 | -4.21 | -32.16 | 368 |
| 46 | MACD zero-line · 1h | trend | 73.53 | -26.47 | 159 | 16.4 | -25.82 | -5.26 | -30.82 | 214 |
| 47 | Supertrend · 1h | trend | 73.09 | -26.91 | 168 | 13.1 | -33.33 | -6.06 | -36.07 | 233 |
| 48 | RSI momentum · 1h | momentum | 73.05 | -26.95 | 159 | 12.6 | -24.53 | -3.94 | -34.05 | 210 |
| 49 | Triple EMA stack · 1h | trend | 72.14 | -27.86 | 144 | 14.6 | -27.36 | -4.82 | -35.44 | 204 |
| 50 | Williams %R · 1h | reversion | 71.95 | -28.05 | 346 | 45.7 | -35.72 | -5.57 | -36.05 | 529 |
| 51 | OBV trend · 1h | momentum | 71.90 | -28.10 | 275 | 18.2 | -27.37 | -4.81 | -35.74 | 277 |
| 52 | ROC + volume · 1h | momentum | 70.74 | -29.26 | 360 | 26.7 | -36.20 | -6.87 | -38.46 | 377 |
| 53 | Donchian 20/10 · 1h | breakout | 70.64 | -29.36 | 142 | 19.7 | -31.58 | -5.84 | -35.64 | 208 |
| 54 | Z-score reversion · 1h ⏸ | reversion | 70.59 | -29.41 | 190 | 36.3 | -27.34 | -3.87 | -29.00 | 227 |
| 55 | Daily: Momentum burst | daily | 70.21 | -29.79 | 27 | 11.1 | -39.34 | -5.65 | -39.69 | 34 |
| 56 | VWAP momentum · 1h | momentum | 66.35 | -33.65 | 838 | 22.0 | -53.32 | -11.32 | -54.41 | 1223 |
| 57 | RSI(14) reversion · 1h | reversion | 66.06 | -33.94 | 170 | 30.6 | -25.98 | -3.54 | -32.56 | 236 |
| 58 | Max aggression: 1-day momentum | meta | 65.46 | -34.54 | 27 | 25.9 | -32.61 | -1.65 | -57.50 | 41 |
| 59 | EMA 9/21 cross · 1h | trend | 65.15 | -34.85 | 251 | 9.6 | -37.53 | -7.41 | -41.69 | 333 |
| 60 | Agent (ML meta-label) | meta | 65.11 | -34.89 | 1681 | 24.3 | -11.56 | -1.57 | -19.78 | 331 |
| 61 | Candlestick reversal · 1h | reversion | 63.48 | -36.52 | 445 | 27.9 | -39.00 | -7.04 | -40.27 | 587 |
| 62 | Three white soldiers | momentum | 61.08 | -38.92 | 502 | 14.9 | -48.95 | -22.85 | -48.95 | 649 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.46 | -98.94 | 5241 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.65 | -25.85 | -79.76 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.17 | -44.34 | -93.20 | 2501 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.37 | -31.64 | -89.40 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.66 | -38.43 | -90.69 | 2310 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.25 | -31.53 | -90.30 | 2199 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -51.82 | -97.77 | 3442 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.17 | -53.76 | -96.18 | 3409 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.51 | -32.38 | -93.62 | 2382 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.31 | -33.80 | -82.40 | 1672 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -53.93 | -99.56 | 6033 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.20 | -41.95 | -92.21 | 2594 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.51 | -36.65 | -95.54 | 3431 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -70.03 | -99.81 | 6162 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.00 | -42.07 | -92.00 | 2249 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.51 | -24.34 | -75.51 | 1593 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -58.33 | -97.72 | 3516 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.87 | -61.74 | -98.88 | 4895 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.56 | -26.84 | -68.99 | 1217 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -51.74 | -94.57 | 2754 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.39 | -35.92 | -84.52 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -71.80 | -99.65 | 6368 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.82 | -31.58 | -89.88 | 2295 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.95 | -20.38 | -79.06 | 1790 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.87 | -36.21 | -90.92 | 2226 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.84 | -52.26 | -96.86 | 3885 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -54.99 | -89.40 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.36 | -27.08 | -66.08 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.03 | -22.56 | -71.09 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.50 | -19.56 | -80.61 | 1709 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -49.13 | -97.30 | 4302 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -100.13 | -99.93 | 8286 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T17:55 | Three white soldiers | buy | TNA | 15.29 | — | entry signal |
| 2026-11-10T17:55 | Three white soldiers | buy | SOXL | 15.29 | — | entry signal |
| 2026-11-10T17:55 | Three white soldiers | buy | BTC-USD | 15.29 | — | entry signal |
| 2026-11-10T17:50 | Agent (ML meta-label) | sell | SQQQ | 1.31 | -0.00 | selected signal exited |
| 2026-11-10T17:50 | Agent (ML meta-label) | sell | SOXL | 2.66 | 0.02 | selected signal exited |
| 2026-11-10T17:45 | Agent (ML meta-label) | buy | SQQQ | 1.31 | — | following Stochastic reversion |
| 2026-11-10T17:45 | Agent (ML meta-label) | buy | SOXL | 2.65 | — | entry |
| 2026-11-10T17:45 | Agent (ML meta-label) | sell | META | 3.93 | -0.01 | rebalance down |
| 2026-11-10T17:45 | Agent | buy | TSLA | 17.49 | — | following Ichimoku, MFI reversion |
| 2026-11-10T17:45 | Parabolic SAR · 1h | buy | AAPL | 13.96 | — | entry |
| 2026-11-10T17:45 | Parabolic SAR · 1h | sell | MSFT | 13.96 | -0.27 | stop-loss |
| 2026-11-10T17:45 | Triple EMA stack · 1h | sell | MSFT | 17.86 | -0.33 | stop-loss |
| 2026-11-10T17:45 | EMA 9/21 cross · 1h | buy | TSLA | 4.57 | — | entry |
| 2026-11-10T17:45 | EMA 9/21 cross · 1h | sell | MSFT | 4.57 | -0.08 | stop-loss |
| 2026-11-10T17:45 | Opening range 30m | sell | TSLA | 22.03 | -0.21 | stop-loss |
| 2026-11-10T17:45 | Opening range 15m | sell | TSLA | 20.37 | -0.20 | stop-loss |
| 2026-11-10T17:40 | Agent (ML meta-label) | buy | TSLA | 8.11 | — | following Ichimoku |
| 2026-11-10T17:40 | Agent (ML meta-label) | sell | SPY | 8.14 | -0.03 | selected signal exited |
| 2026-11-10T17:40 | Z-score reversion · 1h | sell | TSLA | 14.64 | 0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-10T17:40 | Z-score reversion · 1h | sell | TQQQ | 17.78 | -0.34 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-10T17:40 | Z-score reversion · 1h | sell | TECL | 17.43 | -0.67 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-10T17:40 | Z-score reversion · 1h | sell | SOXL | 17.34 | 0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-10T17:40 | Volume breakout · 1h | sell | AMD | 19.21 | -1.12 | stop-loss |
| 2026-11-10T17:40 | ROC + volume · 1h | sell | MSFT | 5.43 | -0.10 | stop-loss |
| 2026-11-10T17:40 | ROC + volume · 1h | sell | AMD | 5.22 | -0.30 | stop-loss |
| 2026-11-10T17:40 | EMA 9/21 cross · 1h | buy | SOXL | 2.02 | — | entry |
| 2026-11-10T17:40 | EMA 9/21 cross · 1h | sell | TQQQ | 2.02 | -0.04 | stop-loss |
| 2026-11-10T17:35 | Agent (ML meta-label) | buy | TECL | 5.39 | — | entry |
| 2026-11-10T17:35 | Agent (ML meta-label) | buy | GOOGL | 8.15 | — | entry |
| 2026-11-10T17:35 | Agent (ML meta-label) | buy | AAPL | 8.15 | — | entry |
| 2026-11-10T17:35 | Agent (ML meta-label) | sell | TSLA | 8.15 | 0.01 | selected signal exited |
| 2026-11-10T17:30 | Agent (ML meta-label) | buy | META | 10.87 | — | entry |
| 2026-11-10T17:30 | Agent (ML meta-label) | sell | TECL | 8.12 | -0.11 | selected signal exited |
| 2026-11-10T17:30 | Agent | sell | LABU | 17.76 | 0.34 | selected signal exited |
| 2026-11-10T17:30 | Bollinger reversion · 1h | buy | NVDA | 18.37 | — | entry signal |
| 2026-11-10T17:30 | Bollinger reversion · 1h | buy | ETHU | 18.37 | — | entry signal |
| 2026-11-10T17:30 | Connors RSI(2) · 1h | buy | MSFT | 20.25 | — | entry signal |
| 2026-11-10T17:30 | Candlestick reversal · 1h | buy | ETHU | 15.84 | — | entry signal |
| 2026-11-10T17:30 | OBV trend · 1h | buy | SQQQ | 17.96 | — | entry signal |
| 2026-11-10T17:30 | OBV trend · 1h | sell | MSFT | 17.81 | -0.14 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 17:57:05.000164+00:00 -> 2026-11-10 18:07:05.000164+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
