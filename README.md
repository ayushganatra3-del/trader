# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T20:10:05.000134+00:00 · 62298 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.17 (-13.83%)

Closed trades 202, win rate 36.6%, fees £5.76, max drawdown -15.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.19 | +0.03 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-16 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 36819 decisions in 3192 calls, $0.4575 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T20:10 | 13 / 10 / 7 | cash |  |
| Breezy | 2026-11-16T20:10 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-16T20:10 | 9 / 20 / 1 | ETHU 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.82 | +5.11% | 10 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| CCI reversion | SOXL | 2.19 | +16.29% | 10 |
| Bollinger reversion | TSLA | 2.18 | +2.18% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.83 | 17.83 | 0 | — | 13.72 | 4.57 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.37 | 10.37 | 23 | 65.2 | 15.59 | 3.17 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.56 | 3.56 | 0 | — | 5.30 | 1.46 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.02 | 1.02 | 35 | 40.0 | -0.44 | 0.02 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.67 | -3.33 | 0 | — | -2.57 | -0.79 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.07 | -5.93 | 0 | — | -6.44 | -1.68 | -8.27 | 1 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 15 | Agent (rotation) | meta | 93.74 | -6.26 | 195 | 29.7 | -2.94 | -1.02 | -8.15 | 159 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -9.05 | -7.50 | -9.22 | 21 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.84 | -8.16 | 0 | — | -6.88 | -1.85 | -10.92 | 1 |
| 18 | Copy: Insider buying | copy | 91.63 | -8.37 | 47 | 42.6 | -10.21 | -2.04 | -14.95 | 62 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -8.91 | -2.66 | -16.01 | 79 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.55 | -13.45 | 16 | 18.8 | -4.67 | -0.72 | -19.56 | 15 |
| 24 | Agent | meta | 86.17 | -13.83 | 202 | 36.6 | -13.52 | -6.55 | -15.94 | 201 |
| 25 | Opening range 30m | breakout | 86.02 | -13.98 | 436 | 33.5 | -10.86 | -3.46 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.50 | -16.50 | 96 | 34.4 | -13.66 | -3.66 | -16.78 | 100 |
| 27 | Parabolic SAR · 1h | trend | 83.33 | -16.67 | 180 | 28.3 | -17.81 | -3.88 | -24.65 | 216 |
| 28 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -22.26 | -4.94 | -28.90 | 86 |
| 29 | Keltner breakout · 1h | breakout | 80.47 | -19.53 | 121 | 25.6 | -19.69 | -4.62 | -25.84 | 157 |
| 30 | Connors RSI(2) · 1h | reversion | 80.32 | -19.68 | 213 | 39.9 | -14.20 | -6.23 | -14.88 | 98 |
| 31 | Volume breakout · 1h | breakout | 79.70 | -20.30 | 161 | 28.6 | -16.26 | -5.15 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 78.06 | -21.94 | 530 | 31.5 | -17.44 | -4.70 | -21.37 | 692 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 77.79 | -22.21 | 2 | 0.0 | -14.14 | -1.73 | -24.50 | 1 |
| 34 | Max aggression: 5-day momentum | meta | 77.67 | -22.33 | 21 | 42.9 | -48.90 | -3.27 | -55.24 | 23 |
| 35 | Hold BTC | benchmark | 76.13 | -23.87 | 2 | 0.0 | -14.45 | -2.01 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.29 | -31.62 | 116 |
| 37 | ADX DI cross · 1h | trend | 74.63 | -25.37 | 207 | 19.3 | -24.10 | -3.71 | -34.65 | 258 |
| 38 | Max aggression: 1-day momentum | meta | 74.50 | -25.50 | 30 | 26.7 | -23.86 | -0.87 | -57.50 | 40 |
| 39 | Bollinger breakout · 1h | breakout | 74.40 | -25.60 | 184 | 22.3 | -23.72 | -4.96 | -31.78 | 234 |
| 40 | Stochastic reversion · 1h ⏸ | reversion | 74.07 | -25.93 | 333 | 44.1 | -31.36 | -4.63 | -32.75 | 416 |
| 41 | MACD zero-line · 1h | trend | 72.65 | -27.35 | 173 | 18.5 | -24.81 | -4.88 | -31.62 | 194 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -25.62 | -3.64 | -29.32 | 163 |
| 43 | Supertrend · 1h | trend | 71.71 | -28.29 | 187 | 16.0 | -32.22 | -5.46 | -39.67 | 200 |
| 44 | Heikin-Ashi · 1h | trend | 71.68 | -28.32 | 459 | 23.3 | -39.16 | -7.46 | -43.26 | 637 |
| 45 | RSI momentum · 1h | momentum | 71.16 | -28.84 | 175 | 14.3 | -27.50 | -4.33 | -38.07 | 204 |
| 46 | Triple EMA stack · 1h | trend | 71.12 | -28.88 | 154 | 14.9 | -27.10 | -4.59 | -37.77 | 192 |
| 47 | MACD cross · 1h | trend | 71.11 | -28.89 | 402 | 22.6 | -33.21 | -4.76 | -43.17 | 473 |
| 48 | EMA 20/50 cross · 1h | trend | 70.94 | -29.06 | 111 | 9.9 | -35.46 | -9.65 | -38.88 | 113 |
| 49 | ROC + volume · 1h | momentum | 70.79 | -29.21 | 404 | 28.5 | -28.03 | -4.59 | -37.95 | 357 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.56 | -4.90 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.13 | -30.87 | 303 | 19.1 | -29.75 | -5.14 | -39.75 | 261 |
| 52 | CCI reversion · 1h | reversion | 68.13 | -31.87 | 375 | 41.6 | -39.75 | -6.44 | -42.07 | 458 |
| 53 | Donchian 20/10 · 1h | breakout | 67.67 | -32.33 | 157 | 18.5 | -30.10 | -4.92 | -39.25 | 206 |
| 54 | Bollinger reversion · 1h ⏸ | reversion | 66.56 | -33.45 | 333 | 39.0 | -35.68 | -5.40 | -36.78 | 406 |
| 55 | EMA 9/21 cross · 1h | trend | 64.50 | -35.50 | 271 | 11.4 | -34.99 | -5.85 | -44.37 | 321 |
| 56 | Williams %R · 1h | reversion | 64.23 | -35.77 | 418 | 41.1 | -44.14 | -7.41 | -45.12 | 545 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -22.15 | -3.38 | -27.50 | 330 |
| 58 | Z-score reversion · 1h | reversion | 60.00 | -40.00 | 221 | 35.7 | -34.35 | -4.71 | -35.86 | 238 |
| 59 | RSI(14) reversion · 1h | reversion | 59.64 | -40.36 | 202 | 32.2 | -39.42 | -5.73 | -41.97 | 244 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.33 | -9.57 | -57.26 | 1213 |
| 61 | Candlestick reversal · 1h | reversion | 57.62 | -42.38 | 529 | 27.0 | -45.21 | -8.25 | -45.83 | 619 |
| 62 | Three white soldiers | momentum | 56.68 | -43.32 | 569 | 14.8 | -49.49 | -21.94 | -49.51 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -41.64 | -99.03 | 5311 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.58 | -25.55 | -81.59 | 1438 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.09 | -42.49 | -94.09 | 2519 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.95 | -31.89 | -90.01 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.39 | -39.92 | -91.39 | 2324 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.94 | -30.15 | -89.97 | 2144 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.95 | -46.94 | -97.96 | 3472 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.45 | -53.23 | -96.45 | 3435 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.42 | -36.15 | -93.43 | 2261 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.81 | -32.98 | -82.82 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -51.54 | -99.59 | 6038 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.16 | -42.01 | -92.16 | 2585 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.16 | -35.53 | -95.16 | 3345 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -65.52 | -99.81 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.50 | -42.36 | -92.50 | 2272 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.35 | -25.94 | -76.35 | 1646 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -56.76 | -97.64 | 3476 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -53.49 | -98.98 | 4939 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.27 | -26.74 | -68.42 | 1225 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -54.75 | -94.71 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -36.98 | -84.75 | 1746 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -65.17 | -99.69 | 6375 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.40 | -29.62 | -90.45 | 2334 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.44 | -18.41 | -79.55 | 1812 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.93 | -35.04 | -91.00 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.43 | -43.84 | -97.43 | 3901 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.15 | -56.74 | -89.15 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -29.24 | -66.40 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.03 | -23.08 | -72.20 | 1246 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.27 | -17.48 | -80.64 | 1759 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -44.59 | -97.56 | 4357 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.15 | -99.94 | 8391 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T20:10 | Agent | sell | TSLA | 17.20 | 0.04 | selected signal exited |
| 2026-11-16T20:00 | Agent | sell | SOXL | 17.29 | 0.08 | selected signal exited |
| 2026-11-16T20:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 5.69 | — | entry signal |
| 2026-11-16T20:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 12.89 | — | entry signal |
| 2026-11-16T20:00 | Three white soldiers | buy | XRP-USD | 14.17 | — | entry signal |
| 2026-11-16T19:50 | Agent (aggressive) | buy | COIN | 41.72 | — | following MACD cross |
| 2026-11-16T19:50 | Agent | buy | TSLA | 17.16 | — | following Bollinger reversion |
| 2026-11-16T19:50 | Agent | buy | COIN | 17.16 | — | following MACD cross |
| 2026-11-16T19:45 | Agent (aggressive) | sell | COIN | 41.69 | -0.06 | selected signal exited |
| 2026-11-16T19:45 | Agent | sell | COIN | 17.12 | -0.02 | selected signal exited |
| 2026-11-16T19:45 | Candlestick reversal · 1h | sell | MSTR | 5.72 | -0.02 | target is flat |
| 2026-11-16T19:45 | Candlestick reversal · 1h | sell | IWM | 5.76 | -0.01 | target is flat |
| 2026-11-16T19:45 | OBV trend · 1h | buy | META | 17.29 | — | entry |
| 2026-11-16T19:31 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 100.98 | — | entry |
| 2026-11-16T19:31 | CCI reversion · 1h | buy | AMD | 16.99 | — | entry signal |
| 2026-11-16T19:31 | Z-score reversion · 1h | buy | ETHU | 14.96 | — | entry signal |
| 2026-11-16T19:31 | Connors RSI(2) · 1h | buy | AAPL | 20.07 | — | entry signal |
| 2026-11-16T19:31 | RSI(14) reversion · 1h | buy | NVDA | 14.90 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | TNA | 5.75 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | SOXL | 5.77 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | LABU | 5.77 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | buy | IWM | 5.77 | — | entry signal |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | NVDA | 3.70 | -0.08 | rebalance down |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | MSFT | 5.71 | -0.01 | rebalance down |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | BTC-USD | 3.93 | 0.00 | rebalance down |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | BITX | 3.98 | 0.03 | rebalance down |
| 2026-11-16T19:31 | Candlestick reversal · 1h | sell | AMD | 5.74 | -0.00 | rebalance down |
| 2026-11-16T19:31 | Trend pullback · 1h | sell | AAPL | 23.67 | 0.46 | exit signal |
| 2026-11-16T19:31 | EMA 9/21 cross · 1h | sell | AAPL | 16.03 | -0.02 | exit signal |
| 2026-11-16T19:25 | Three white soldiers | sell | AMZN | 14.14 | -0.04 | exit signal |
| 2026-11-16T19:21 | Three white soldiers | buy | AMZN | 14.19 | — | entry signal |
| 2026-11-16T19:15 | Candlestick reversal · 1h | buy | MSTR | 5.74 | — | entry |
| 2026-11-16T19:15 | OBV trend · 1h | sell | META | 17.20 | -0.05 | target is flat |
| 2026-11-16T19:05 | Three white soldiers | sell | AMZN | 14.15 | -0.05 | exit signal |
| 2026-11-16T19:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 100.98 | -0.90 | target is flat |
| 2026-11-16T19:00 | MACD zero-line · 1h | buy | ETH-USD | 18.13 | — | entry signal |
| 2026-11-16T19:00 | MACD zero-line · 1h | buy | DOGE-USD | 18.13 | — | entry signal |
| 2026-11-16T18:55 | Agent | sell | TSLA | 17.18 | -0.03 | selected signal exited |
| 2026-11-16T18:50 | Three white soldiers | buy | AMZN | 14.20 | — | entry signal |
| 2026-11-16T18:35 | Agent (rotation) | buy | SQQQ | 31.32 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 20:10:05.000134+00:00 -> 2026-11-16 20:20:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 20:10:05.000134+00:00 -> 2026-11-16 20:20:05.000134+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
