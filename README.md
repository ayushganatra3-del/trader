# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T17:56:05.000124+00:00 · 47432 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.73 (-10.27%)

Closed trades 144, win rate 38.2%, fees £4.01, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 22443 decisions in 2262 calls, $0.2829 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T17:56 | 3 / 13 / 14 | cash |  |
| Breezy | 2026-11-04T17:56 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-04T17:56 | 4 / 24 / 2 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 111.85 | 11.85 | 0 | — | 12.95 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.91 | 7.91 | 17 | 70.6 | 7.23 | 2.22 | -4.91 | 26 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.92 | 1.92 | 0 | — | 5.77 | 1.57 | -6.60 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.56 | 0.56 | 5 | 40.0 | 5.19 | 1.18 | -7.93 | 8 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.10 | -13.53 | 140 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.43 | -0.57 | 27 | 44.4 | -2.25 | -0.67 | -9.07 | 28 |
| 9 | Hold SPY | benchmark | 98.35 | -1.65 | 0 | — | -0.70 | -0.30 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 96.25 | -3.75 | 111 | 35.1 | 6.08 | 2.81 | -3.27 | 90 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.36 | -4.64 | 0 | — | -1.98 | -0.70 | -7.64 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Hold BTC | benchmark | 94.49 | -5.51 | 0 | — | -1.44 | -0.07 | -13.22 | 1 |
| 17 | Agent (rotation) | meta | 94.48 | -5.52 | 163 | 27.6 | -6.84 | -5.36 | -9.38 | 191 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.41 | -5.59 | 0 | — | -4.91 | -1.85 | -6.35 | 1 |
| 19 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.01 | -0.27 | -8.76 | 223 |
| 20 | Max aggression: 5-day momentum | meta | 91.83 | -8.17 | 16 | 43.8 | -23.40 | -1.33 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Parabolic SAR · 1h | trend | 90.69 | -9.31 | 154 | 26.6 | -12.98 | -2.59 | -19.39 | 239 |
| 23 | Trend pullback · 1h | trend | 90.38 | -9.62 | 103 | 22.3 | -17.00 | -6.31 | -17.97 | 79 |
| 24 | Opening range 30m | breakout | 89.77 | -10.23 | 355 | 33.0 | -15.34 | -5.08 | -17.21 | 591 |
| 25 | Agent | meta | 89.73 | -10.27 | 144 | 38.2 | -11.58 | -6.98 | -12.62 | 205 |
| 26 | Copy: Insider buying | copy | 89.32 | -10.68 | 37 | 37.8 | -21.63 | -4.36 | -23.56 | 63 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.84 | -3.38 | -14.15 | 85 |
| 28 | Stochastic reversion · 1h | reversion | 86.92 | -13.08 | 249 | 47.8 | -20.36 | -3.84 | -24.94 | 385 |
| 29 | Daily: Bullish score | daily | 86.91 | -13.09 | 14 | 21.4 | -11.86 | -1.86 | -16.58 | 14 |
| 30 | Donchian 55/20 · 1h | breakout | 86.91 | -13.09 | 62 | 12.9 | -14.52 | -3.13 | -19.86 | 107 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.63 | -13.38 | 1 | 0.0 | -7.33 | -1.07 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -11.94 | -3.93 | -14.77 | 95 |
| 33 | ADX DI cross · 1h | trend | 85.57 | -14.43 | 155 | 18.1 | -19.42 | -3.45 | -23.75 | 271 |
| 34 | Volume breakout · 1h | breakout | 85.25 | -14.75 | 130 | 28.5 | -13.55 | -3.07 | -18.08 | 103 |
| 35 | MFI reversion · 1h | reversion | 84.88 | -15.12 | 319 | 34.5 | -13.92 | -2.06 | -19.36 | 154 |
| 36 | Keltner breakout · 1h | breakout | 84.27 | -15.73 | 94 | 24.5 | -22.14 | -4.62 | -24.53 | 185 |
| 37 | Opening range 15m | breakout | 82.96 | -17.04 | 433 | 30.3 | -20.07 | -6.16 | -21.19 | 724 |
| 38 | Connors RSI(2) · 1h | reversion | 82.93 | -17.07 | 192 | 40.6 | -18.88 | -6.17 | -19.59 | 127 |
| 39 | Ichimoku · 1h | trend | 82.38 | -17.62 | 85 | 12.9 | -19.55 | -4.13 | -26.10 | 126 |
| 40 | Bollinger breakout · 1h | breakout | 81.82 | -18.18 | 148 | 25.0 | -17.60 | -3.54 | -23.94 | 251 |
| 41 | CCI reversion · 1h | reversion | 80.91 | -19.09 | 278 | 46.4 | -22.25 | -3.30 | -27.71 | 456 |
| 42 | Heikin-Ashi · 1h | trend | 79.34 | -20.66 | 372 | 22.6 | -39.96 | -8.17 | -43.81 | 673 |
| 43 | EMA 20/50 cross · 1h | trend | 79.21 | -20.80 | 92 | 10.9 | -19.48 | -3.66 | -27.52 | 133 |
| 44 | MACD zero-line · 1h | trend | 78.91 | -21.09 | 141 | 15.6 | -24.74 | -5.17 | -29.63 | 223 |
| 45 | Z-score reversion · 1h | reversion | 78.66 | -21.34 | 151 | 37.1 | -14.87 | -2.15 | -23.02 | 218 |
| 46 | MACD cross · 1h | trend | 78.62 | -21.38 | 310 | 22.9 | -31.16 | -6.04 | -33.65 | 472 |
| 47 | Supertrend · 1h | trend | 78.33 | -21.67 | 147 | 12.9 | -26.85 | -5.01 | -30.19 | 237 |
| 48 | Bollinger reversion · 1h | reversion | 77.06 | -22.94 | 233 | 40.3 | -27.88 | -5.50 | -30.31 | 381 |
| 49 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.35 | -4.47 | -33.57 | 33 |
| 50 | RSI momentum · 1h | momentum | 76.98 | -23.02 | 142 | 12.0 | -28.49 | -5.52 | -30.82 | 227 |
| 51 | Williams %R · 1h | reversion | 76.98 | -23.02 | 290 | 47.6 | -35.71 | -6.36 | -37.26 | 535 |
| 52 | Triple EMA stack · 1h | trend | 76.04 | -23.96 | 131 | 13.7 | -29.02 | -5.89 | -31.99 | 210 |
| 53 | OBV trend · 1h | momentum | 75.62 | -24.39 | 248 | 17.3 | -30.51 | -6.62 | -31.89 | 293 |
| 54 | Donchian 20/10 · 1h | breakout | 74.86 | -25.14 | 124 | 19.4 | -26.92 | -4.87 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.57 | -25.43 | 318 | 25.2 | -34.02 | -6.62 | -36.91 | 388 |
| 56 | RSI(14) reversion · 1h | reversion | 72.83 | -27.17 | 136 | 28.7 | -21.94 | -3.76 | -26.28 | 216 |
| 57 | Agent (ML meta-label) | meta | 70.44 | -29.56 | 1412 | 22.5 | -10.76 | -2.46 | -17.31 | 261 |
| 58 | VWAP momentum · 1h | momentum | 69.94 | -30.06 | 723 | 22.1 | -54.81 | -11.33 | -56.13 | 1233 |
| 59 | EMA 9/21 cross · 1h | trend | 69.86 | -30.14 | 225 | 9.8 | -36.47 | -7.31 | -40.02 | 341 |
| 60 | Candlestick reversal · 1h | reversion | 69.47 | -30.53 | 376 | 30.1 | -35.48 | -6.79 | -38.27 | 560 |
| 61 | Three white soldiers | momentum | 68.44 | -31.56 | 433 | 16.2 | -46.98 | -21.65 | -47.44 | 632 |
| 62 | Max aggression: 1-day momentum | meta | 66.86 | -33.14 | 24 | 29.2 | -35.76 | -2.13 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -45.22 | -99.00 | 5185 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.99 | -24.42 | -80.18 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.32 | -43.24 | -93.36 | 2505 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -30.22 | -89.13 | 1912 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.89 | -35.89 | -91.09 | 2314 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.26 | -31.45 | -90.31 | 2199 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.68 | -48.83 | -97.74 | 3451 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -52.26 | -96.15 | 3351 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.41 | -32.34 | -93.53 | 2436 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.01 | -35.80 | -82.09 | 1647 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.23 | -99.49 | 5890 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.94 | -41.57 | -93.06 | 2605 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.54 | -36.92 | -95.55 | 3376 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -67.60 | -99.80 | 6162 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -40.47 | -91.87 | 2264 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.59 | -26.23 | -74.83 | 1560 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -55.20 | -97.73 | 3498 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -59.35 | -98.70 | 4827 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.63 | -27.92 | -70.60 | 1194 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -51.23 | -94.85 | 2760 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.77 | -36.34 | -84.96 | 1794 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.53 | -99.63 | 6311 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.16 | -29.78 | -88.52 | 2238 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.30 | -18.79 | -76.93 | 1718 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.59 | -36.99 | -90.61 | 2235 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -49.24 | -96.53 | 3837 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -50.49 | -89.41 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.40 | -26.83 | -65.91 | 824 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -24.41 | -73.90 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.85 | -18.61 | -77.65 | 1618 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.96 | -51.83 | -96.99 | 4249 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.87 | -99.93 | 8206 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T17:50 | Agent (ML meta-label) | sell | TQQQ | 5.06 | 0.04 | selected signal exited |
| 2026-11-04T17:50 | Agent (ML meta-label) | sell | AMZN | 5.42 | 0.01 | selected signal exited |
| 2026-11-04T17:50 | MFI reversion · 1h | buy | TSLA | 16.86 | — | rebalance up |
| 2026-11-04T17:50 | MFI reversion · 1h | sell | SPY | 16.94 | -0.01 | target is flat |
| 2026-11-04T17:45 | Agent (ML meta-label) | sell | TNA | 5.43 | 0.03 | selected signal exited |
| 2026-11-04T17:45 | MFI reversion · 1h | buy | TSLA | 4.34 | — | entry |
| 2026-11-04T17:45 | MFI reversion · 1h | sell | SPY | 4.25 | -0.01 | rebalance down |
| 2026-11-04T17:40 | Agent (ML meta-label) | buy | AMZN | 5.41 | — | entry |
| 2026-11-04T17:40 | Agent (ML meta-label) | sell | IWM | 5.04 | 0.01 | selected signal exited |
| 2026-11-04T17:40 | Keltner breakout · 1h | sell | SOL-USD | 5.96 | 0.00 | stop-loss |
| 2026-11-04T17:40 | Keltner breakout · 1h | sell | DOGE-USD | 5.97 | -0.03 | stop-loss |
| 2026-11-04T17:40 | Bollinger breakout · 1h | buy | TNA | 4.81 | — | entry |
| 2026-11-04T17:40 | Bollinger breakout · 1h | buy | LABU | 4.81 | — | entry |
| 2026-11-04T17:40 | Bollinger breakout · 1h | sell | SOL-USD | 4.77 | 0.00 | stop-loss |
| 2026-11-04T17:40 | Bollinger breakout · 1h | sell | DOGE-USD | 4.77 | -0.02 | stop-loss |
| 2026-11-04T17:40 | Gap and go | sell | ETHU | 23.34 | 0.29 | stop-loss |
| 2026-11-04T17:35 | Agent (ML meta-label) | sell | AMZN | 5.05 | 0.02 | selected signal exited |
| 2026-11-04T17:35 | ROC + volume · 1h | buy | QQQ | 3.23 | — | entry |
| 2026-11-04T17:35 | ROC + volume · 1h | sell | IWM | 3.23 | -0.01 | target is flat |
| 2026-11-04T17:30 | Day trade: Stocks in Play ORB | buy | GOOGL | 24.08 | — | entry |
| 2026-11-04T17:30 | Agent (ML meta-label) | buy | GOOGL | 4.68 | — | entry |
| 2026-11-04T17:30 | Agent (ML meta-label) | sell | AMD | 4.41 | 0.01 | selected signal exited |
| 2026-11-04T17:30 | MFI reversion · 1h | buy | SPY | 21.20 | — | entry signal |
| 2026-11-04T17:30 | MFI reversion · 1h | buy | NVDA | 21.20 | — | entry signal |
| 2026-11-04T17:30 | CCI reversion · 1h | buy | SQQQ | 15.19 | — | rebalance up |
| 2026-11-04T17:30 | CCI reversion · 1h | sell | LABU | 16.65 | 1.01 | exit signal |
| 2026-11-04T17:30 | Williams %R · 1h | buy | NVDA | 10.99 | — | entry signal |
| 2026-11-04T17:30 | Williams %R · 1h | sell | LABU | 12.12 | 0.71 | exit signal |
| 2026-11-04T17:30 | Stochastic reversion · 1h | buy | SPY | 4.62 | — | rebalance up |
| 2026-11-04T17:30 | Stochastic reversion · 1h | buy | PLTR | 5.23 | — | rebalance up |
| 2026-11-04T17:30 | Stochastic reversion · 1h | buy | IWM | 4.52 | — | rebalance up |
| 2026-11-04T17:30 | Stochastic reversion · 1h | sell | LABU | 18.62 | 1.51 | exit signal |
| 2026-11-04T17:30 | Bollinger reversion · 1h | buy | TSLA | 19.27 | — | entry signal |
| 2026-11-04T17:30 | Bollinger reversion · 1h | buy | SOXL | 19.27 | — | entry signal |
| 2026-11-04T17:30 | RSI(14) reversion · 1h | buy | SOXL | 10.43 | — | entry signal |
| 2026-11-04T17:30 | Keltner breakout · 1h | buy | META | 5.97 | — | entry signal |
| 2026-11-04T17:30 | Bollinger breakout · 1h | buy | IWM | 4.31 | — | entry signal |
| 2026-11-04T17:30 | RSI momentum · 1h | buy | IWM | 1.09 | — | entry signal |
| 2026-11-04T17:30 | ROC + volume · 1h | buy | IWM | 3.24 | — | entry signal |
| 2026-11-04T17:30 | VWAP momentum · 1h | buy | QQQ | 3.09 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 17:56:05.000124+00:00 -> 2026-11-04 18:06:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 17:56:05.000124+00:00 -> 2026-11-04 18:06:05.000124+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 17:56:05.000124+00:00 -> 2026-11-04 18:06:05.000124+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
