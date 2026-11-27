# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T14:36:05.000170+00:00 · 75601 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.43 (-23.57%)

Closed trades 250, win rate 36.0%, fees £6.88, max drawdown -24.09%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 15.28 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-27 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 26.80 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 11562 decisions in 2313 calls, $0.1612 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T14:36 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-27T14:36 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T14:36 | 3 / 2 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| EMA 20/50 cross | TECL | 1.74 | +5.81% | 3 |
| Bollinger reversion · 1h | MSFT | 1.74 | +7.75% | 3 |
| Z-score reversion | SQQQ | 1.74 | +8.59% | 5 |
| EMA 20/50 cross | TQQQ | 1.64 | +4.16% | 4 |
| OBV trend | COIN | 1.45 | +1.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.21 | 3.56 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.62 | 16.61 | 0 | — | 15.24 | 5.05 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.76 | 5.76 | 0 | — | 4.67 | 1.28 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.17 | 1.17 | 43 | 27.9 | -1.26 | 0.00 | -14.70 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.20 | 0.03 | -7.66 | 206 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.81 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.64 | -3.96 | -5.47 | 51 |
| 11 | Hold SPY | benchmark | 94.90 | -5.10 | 0 | — | -5.70 | -1.42 | -11.71 | 1 |
| 12 | Agent (rotation) | meta | 94.61 | -5.39 | 232 | 28.4 | 0.90 | 0.37 | -6.10 | 178 |
| 13 | Three white soldiers · 1h | momentum | 94.44 | -5.56 | 24 | 12.5 | -4.02 | -4.43 | -6.53 | 26 |
| 14 | Copy: Insider buying | copy | 94.06 | -5.94 | 63 | 41.3 | -2.99 | -0.43 | -14.79 | 70 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.28 | -6.72 | 0 | — | -7.99 | -1.59 | -13.91 | 1 |
| 16 | Trend pullback · 1h | trend | 90.85 | -9.15 | 116 | 24.1 | -7.19 | -4.57 | -9.64 | 27 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.71 | -9.29 | 0 | — | -10.04 | -2.08 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.34 | -11.13 | 22 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.89 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -9.23 | -2.79 | -15.30 | 538 |
| 21 | Daily: Bullish score | daily | 85.14 | -14.86 | 20 | 20.0 | -13.84 | -3.07 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.40 | -20.49 | 152 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.42 | -6.03 | -17.45 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 79.38 | -20.62 | 224 | 41.1 | -13.54 | -6.30 | -13.73 | 60 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.18 | -4.99 | -24.20 | 663 |
| 27 | Volume breakout · 1h | breakout | 77.16 | -22.84 | 177 | 29.4 | -21.18 | -8.32 | -21.32 | 69 |
| 28 | Agent | meta | 76.43 | -23.57 | 250 | 36.0 | -26.17 | -5.77 | -26.89 | 207 |
| 29 | Parabolic SAR · 1h | trend | 76.05 | -23.95 | 216 | 27.8 | -31.29 | -7.75 | -33.18 | 181 |
| 30 | Agent (aggressive) | meta | 75.81 | -24.19 | 115 | 33.0 | -14.78 | -4.03 | -16.35 | 92 |
| 31 | Max aggression: 5-day momentum | meta | 75.45 | -24.55 | 27 | 37.0 | -51.66 | -2.51 | -67.33 | 21 |
| 32 | Ichimoku · 1h | trend | 74.00 | -26.00 | 114 | 15.8 | -28.27 | -7.00 | -29.63 | 100 |
| 33 | Donchian 55/20 · 1h | breakout | 73.68 | -26.32 | 89 | 13.5 | -30.29 | -7.97 | -30.32 | 77 |
| 34 | Keltner breakout · 1h | breakout | 72.41 | -27.59 | 147 | 23.8 | -27.08 | -6.64 | -27.08 | 147 |
| 35 | Daily: Momentum burst | daily | 71.43 | -28.57 | 31 | 16.1 | -31.82 | -4.28 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 70.39 | -29.61 | 272 | 19.9 | -39.16 | -7.43 | -40.68 | 280 |
| 37 | Hold BTC | benchmark | 70.20 | -29.80 | 3 | 0.0 | -28.00 | -4.86 | -36.10 | 1 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 68.96 | -31.04 | 3 | 0.0 | -23.27 | -2.79 | -33.66 | 1 |
| 39 | Supertrend · 1h | trend | 67.76 | -32.24 | 221 | 17.6 | -38.71 | -7.42 | -41.52 | 208 |
| 40 | Stochastic reversion · 1h | reversion | 67.63 | -32.37 | 412 | 39.8 | -31.21 | -3.15 | -42.39 | 428 |
| 41 | Bollinger breakout · 1h | breakout | 67.09 | -32.91 | 220 | 23.2 | -30.54 | -7.90 | -31.70 | 206 |
| 42 | OBV trend · 1h | momentum | 66.57 | -33.43 | 326 | 19.9 | -39.08 | -9.34 | -39.74 | 212 |
| 43 | EMA 20/50 cross · 1h | trend | 65.83 | -34.17 | 126 | 9.5 | -37.96 | -10.13 | -38.91 | 118 |
| 44 | Triple EMA stack · 1h | trend | 65.32 | -34.68 | 172 | 15.1 | -40.09 | -9.69 | -41.38 | 162 |
| 45 | MACD zero-line · 1h | trend | 64.24 | -35.76 | 206 | 16.5 | -35.64 | -9.34 | -37.39 | 188 |
| 46 | RSI momentum · 1h | momentum | 63.67 | -36.33 | 203 | 14.8 | -41.80 | -8.82 | -43.11 | 189 |
| 47 | MFI reversion · 1h | reversion | 63.37 | -36.63 | 528 | 33.7 | -31.88 | -4.62 | -38.15 | 194 |
| 48 | Donchian 20/10 · 1h | breakout | 62.31 | -37.69 | 183 | 17.5 | -38.05 | -8.19 | -40.84 | 195 |
| 49 | Heikin-Ashi · 1h | trend | 60.68 | -39.32 | 563 | 22.0 | -48.67 | -9.60 | -49.90 | 644 |
| 50 | ROC + volume · 1h | momentum | 60.57 | -39.43 | 475 | 26.9 | -40.06 | -7.71 | -40.68 | 333 |
| 51 | Max aggression: 1-day momentum | meta | 60.08 | -39.92 | 35 | 28.6 | -60.06 | -4.30 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 59.30 | -40.70 | 314 | 12.1 | -44.25 | -9.90 | -46.70 | 308 |
| 53 | MACD cross · 1h | trend | 57.94 | -42.06 | 499 | 21.0 | -53.30 | -10.28 | -55.75 | 506 |
| 54 | Agent (ML meta-label) | meta | 55.95 | -44.05 | 2074 | 25.4 | -25.40 | -3.20 | -31.14 | 304 |
| 55 | CCI reversion · 1h | reversion | 52.55 | -47.45 | 467 | 38.3 | -51.42 | -8.31 | -55.11 | 494 |
| 56 | Bollinger reversion · 1h | reversion | 52.18 | -47.82 | 406 | 36.5 | -39.84 | -4.74 | -45.50 | 428 |
| 57 | VWAP momentum · 1h | momentum | 51.14 | -48.86 | 1114 | 21.3 | -60.61 | -12.80 | -61.80 | 1173 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.92 | -9.10 | -59.06 | 682 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.65 | -9.02 | -59.51 | 595 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -43.94 | -99.16 | 5310 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.20 | -29.32 | -83.38 | 1400 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.11 | -42.45 | -94.11 | 2381 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.00 | -28.52 | -90.23 | 1856 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.21 | -36.22 | -91.24 | 2186 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.53 | -26.10 | -88.53 | 1916 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.08 | -43.41 | -98.08 | 3353 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.86 | -46.98 | -96.86 | 3335 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.37 | -33.20 | -93.37 | 2074 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.07 | -33.98 | -82.07 | 1502 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -50.48 | -99.69 | 6215 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.69 | -35.45 | -92.69 | 2437 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.43 | -34.39 | -94.43 | 3124 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -58.56 | -99.81 | 6013 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.74 | -38.72 | -92.76 | 2221 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.00 | -18.47 | -51.19 | 652 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.02 | -22.66 | -78.02 | 1593 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -51.30 | -97.66 | 3197 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -54.29 | -99.15 | 5053 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.54 | -22.72 | -69.54 | 1198 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.54 | -43.00 | -94.54 | 2633 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -45.88 | -6.21 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.32 | -32.40 | -84.32 | 1635 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -62.85 | -99.77 | 6442 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.54 | -29.92 | -91.67 | 2465 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.72 | -19.56 | -83.08 | 1949 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.26 | -31.51 | -91.43 | 2125 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.20 | -45.85 | -98.20 | 3996 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.02 | -42.25 | -90.16 | 2182 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.97 | -28.23 | -67.97 | 779 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.75 | -26.48 | -72.86 | 1146 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.36 | -18.59 | -84.62 | 1809 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.07 | -46.41 | -98.07 | 4347 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -81.42 | -99.94 | 8204 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -44.85 | -6.44 | -52.59 | 294 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T14:35 | Max aggression: 1-day momentum | buy | SOXL | 60.11 | — | entry |
| 2026-11-27T14:35 | Agent (rotation) | buy | SHMD | 3.94 | — | entry |
| 2026-11-27T14:35 | Agent (rotation) | buy | PLTR | 3.94 | — | entry |
| 2026-11-27T14:35 | Agent (rotation) | buy | PEPG | 3.94 | — | entry |
| 2026-11-27T14:35 | Agent (rotation) | buy | COHR | 3.94 | — | entry |
| 2026-11-27T14:35 | Agent (rotation) | buy | BORR | 3.94 | — | entry |
| 2026-11-27T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 101.22 | — | entry |
| 2026-11-27T14:35 | Agent (aggressive) | buy | MSFT | 37.91 | — | following Bollinger reversion · 1h |
| 2026-11-27T14:35 | Agent | buy | MSFT | 15.29 | — | following Bollinger reversion · 1h |
| 2026-11-27T14:35 | MFI reversion · 1h | buy | TNA | 7.92 | — | entry |
| 2026-11-27T14:35 | MFI reversion · 1h | buy | MSTR | 3.41 | — | rebalance up |
| 2026-11-27T14:35 | MFI reversion · 1h | buy | IWM | 7.92 | — | entry |
| 2026-11-27T14:35 | MFI reversion · 1h | buy | ETHU | 7.92 | — | entry |
| 2026-11-27T14:35 | MFI reversion · 1h | buy | COIN | 7.92 | — | entry |
| 2026-11-27T14:35 | MFI reversion · 1h | sell | TSLA | 1.45 | 0.02 | target is flat |
| 2026-11-27T14:35 | MFI reversion · 1h | sell | TQQQ | 3.68 | 0.33 | target is flat |
| 2026-11-27T14:35 | MFI reversion · 1h | sell | SOXL | 4.55 | 0.84 | target is flat |
| 2026-11-27T14:35 | MFI reversion · 1h | sell | NVDA | 5.17 | 0.13 | target is flat |
| 2026-11-27T14:35 | MFI reversion · 1h | sell | MSFT | 5.16 | 0.12 | target is flat |
| 2026-11-27T14:35 | MFI reversion · 1h | sell | GOOGL | 3.83 | 0.04 | target is flat |
| 2026-11-27T14:35 | MFI reversion · 1h | sell | AMD | 4.89 | 0.13 | target is flat |
| 2026-11-27T14:35 | MFI reversion · 1h | sell | AAPL | 4.48 | 0.03 | target is flat |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | UPRO | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | TQQQ | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | TECL | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | SOXL | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | QQQ | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | MSTR | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | MSFT | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | GOOGL | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | COIN | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | BITX | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | AMZN | 4.38 | — | entry |
| 2026-11-27T14:35 | CCI reversion · 1h | buy | AMD | 4.38 | — | entry |
| 2026-11-27T14:35 | Stochastic reversion · 1h | sell | ETHU | 6.62 | -0.02 | target is flat |
| 2026-11-27T14:35 | Bollinger reversion · 1h | buy | MSFT | 13.05 | — | entry |
| 2026-11-27T14:35 | Bollinger reversion · 1h | buy | AMZN | 13.05 | — | entry |
| 2026-11-27T14:35 | Bollinger reversion · 1h | buy | AMD | 13.05 | — | entry |
| 2026-11-27T14:35 | Three white soldiers · 1h | buy | UPRO | 5.23 | — | rebalance up |
| 2026-11-27T14:35 | Three white soldiers · 1h | buy | SPY | 5.39 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 14:36:05.000170+00:00 -> 2026-11-27 14:46:05.000170+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
