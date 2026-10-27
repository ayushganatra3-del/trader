# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T13:35:05.000127+00:00 · 37917 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.18 (-9.82%)

Closed trades 110, win rate 39.1%, fees £3.39, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-27 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, PLUR 12%, RAPP 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 10465 decisions in 2024 calls, $0.1453 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T13:35 | 6 / 17 / 7 | AMD 21%, SOXL 16%, TECL 14% |  |
| Breezy | 2026-10-27T13:35 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-27T13:35 | 7 / 16 / 7 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.34 | +7.11% | 6 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 3 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.05 | 8.05 | 0 | — | 8.51 | 4.26 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 4.79 | 1.55 | -5.58 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.52 | 5.52 | 21 | 33.3 | 10.52 | 2.72 | -5.17 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 19 | 47.4 | 6.21 | 2.01 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -12.91 | -3.56 | -13.83 | 149 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.00 | 0.00 | 0 | — | 2.85 | 1.30 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.14 | -0.86 | 0 | — | 0.26 | 0.20 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.33 | -1.67 | 78 | 34.6 | 8.77 | 3.65 | -1.52 | 99 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.12 | -1.97 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.60 | -3.40 | 0 | — | -0.27 | -0.05 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.12 | -3.88 | 121 | 31.4 | -2.26 | -1.26 | -6.39 | 173 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.63 | 1.10 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.19 | -2.64 | -4.59 | 27 |
| 17 | Hold BTC | benchmark | 94.97 | -5.03 | 0 | — | 2.05 | 0.51 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.96 | -5.04 | 0 | — | -6.95 | -2.93 | -7.83 | 1 |
| 19 | Gap and go | momentum | 94.72 | -5.28 | 106 | 25.5 | 5.02 | 1.64 | -8.76 | 200 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.62 | -7.38 | 271 | 34.3 | -10.98 | -3.35 | -17.21 | 577 |
| 22 | Donchian 55/20 · 1h | breakout | 92.32 | -7.68 | 49 | 16.3 | -15.37 | -3.44 | -16.70 | 98 |
| 23 | Copy: Insider buying | copy | 92.23 | -7.77 | 27 | 37.0 | -20.52 | -4.07 | -22.94 | 63 |
| 24 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.14 | -2.14 | -16.91 | 1 |
| 25 | Daily: Momentum burst | daily | 91.04 | -8.96 | 13 | 15.4 | -18.40 | -3.57 | -19.65 | 41 |
| 26 | Squeeze breakout · 1h | breakout | 90.98 | -9.02 | 52 | 23.1 | -6.15 | -1.62 | -12.00 | 93 |
| 27 | Daily: Bullish score | daily | 90.75 | -9.25 | 11 | 18.2 | -5.39 | -0.60 | -14.40 | 15 |
| 28 | ADX DI cross · 1h | trend | 90.38 | -9.62 | 116 | 19.0 | -12.99 | -2.84 | -14.45 | 271 |
| 29 | Agent | meta | 90.18 | -9.82 | 110 | 39.1 | -10.55 | -6.61 | -12.47 | 214 |
| 30 | Parabolic SAR · 1h | trend | 90.11 | -9.89 | 121 | 25.6 | -22.00 | -5.61 | -22.16 | 251 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.36 | -10.64 | 0 | — | -4.64 | -0.64 | -14.57 | 1 |
| 32 | Max aggression: 5-day momentum | meta | 89.29 | -10.71 | 12 | 41.7 | -17.33 | -1.63 | -27.80 | 26 |
| 33 | Volume breakout · 1h | breakout | 89.05 | -10.96 | 104 | 23.1 | -13.13 | -2.73 | -16.10 | 107 |
| 34 | Agent (aggressive) | meta | 88.57 | -11.43 | 54 | 37.0 | -10.74 | -3.53 | -14.77 | 96 |
| 35 | Bollinger breakout · 1h | breakout | 87.62 | -12.38 | 109 | 26.6 | -14.70 | -2.96 | -18.15 | 239 |
| 36 | Stochastic reversion · 1h | reversion | 87.49 | -12.51 | 199 | 46.7 | -22.49 | -4.24 | -23.46 | 391 |
| 37 | Opening range 15m | breakout | 86.22 | -13.78 | 337 | 30.9 | -14.54 | -4.12 | -17.87 | 704 |
| 38 | Keltner breakout · 1h | breakout | 86.02 | -13.98 | 74 | 23.0 | -23.29 | -4.70 | -24.37 | 179 |
| 39 | Z-score reversion · 1h | reversion | 85.81 | -14.19 | 118 | 33.1 | -13.53 | -2.18 | -21.48 | 211 |
| 40 | Connors RSI(2) · 1h | reversion | 85.06 | -14.94 | 175 | 40.6 | -26.52 | -7.97 | -27.00 | 197 |
| 41 | Supertrend · 1h | trend | 84.38 | -15.62 | 114 | 14.0 | -26.40 | -5.59 | -28.09 | 222 |
| 42 | EMA 20/50 cross · 1h | trend | 84.15 | -15.85 | 73 | 11.0 | -23.81 | -4.74 | -25.07 | 132 |
| 43 | RSI momentum · 1h | momentum | 84.09 | -15.91 | 104 | 15.4 | -20.13 | -3.91 | -22.24 | 200 |
| 44 | MACD cross · 1h | trend | 83.47 | -16.53 | 244 | 22.1 | -28.34 | -5.85 | -29.38 | 482 |
| 45 | MFI reversion · 1h | reversion | 82.92 | -17.08 | 265 | 31.7 | -16.92 | -2.64 | -20.70 | 153 |
| 46 | Ichimoku · 1h | trend | 82.73 | -17.27 | 68 | 11.8 | -21.10 | -4.37 | -24.73 | 109 |
| 47 | Triple EMA stack · 1h | trend | 82.37 | -17.63 | 101 | 14.9 | -28.20 | -5.61 | -30.27 | 203 |
| 48 | Williams %R · 1h | reversion | 81.26 | -18.74 | 229 | 46.3 | -36.03 | -6.31 | -36.29 | 537 |
| 49 | CCI reversion · 1h | reversion | 81.19 | -18.81 | 224 | 44.6 | -25.51 | -3.69 | -27.90 | 463 |
| 50 | Bollinger reversion · 1h | reversion | 81.03 | -18.97 | 180 | 37.2 | -28.41 | -5.70 | -30.52 | 365 |
| 51 | MACD zero-line · 1h | trend | 80.62 | -19.38 | 111 | 15.3 | -23.90 | -5.10 | -25.18 | 219 |
| 52 | Donchian 20/10 · 1h | breakout | 80.35 | -19.65 | 99 | 20.2 | -25.49 | -5.00 | -26.91 | 210 |
| 53 | Agent (ML meta-label) | meta | 80.15 | -19.85 | 927 | 19.6 | -13.88 | -2.64 | -18.66 | 345 |
| 54 | OBV trend · 1h | momentum | 79.53 | -20.47 | 206 | 17.5 | -32.07 | -6.82 | -32.55 | 299 |
| 55 | RSI(14) reversion · 1h | reversion | 79.36 | -20.64 | 103 | 24.3 | -17.90 | -3.27 | -24.48 | 192 |
| 56 | Three white soldiers | momentum | 77.84 | -22.16 | 310 | 19.0 | -44.20 | -20.27 | -44.64 | 603 |
| 57 | ROC + volume · 1h | momentum | 77.58 | -22.42 | 256 | 25.4 | -32.00 | -6.29 | -33.26 | 373 |
| 58 | Heikin-Ashi · 1h | trend | 77.54 | -22.46 | 293 | 22.9 | -44.03 | -10.00 | -44.86 | 657 |
| 59 | Candlestick reversal · 1h | reversion | 76.89 | -23.11 | 276 | 28.6 | -34.90 | -6.35 | -35.39 | 560 |
| 60 | VWAP momentum · 1h | momentum | 75.89 | -24.11 | 559 | 21.1 | -49.08 | -10.75 | -50.72 | 1233 |
| 61 | EMA 9/21 cross · 1h | trend | 75.73 | -24.27 | 176 | 10.8 | -32.33 | -6.96 | -33.40 | 331 |
| 62 | Max aggression: 1-day momentum | meta | 68.36 | -31.64 | 20 | 30.0 | -41.06 | -2.75 | -50.32 | 43 |
| 63 | ROC + volume | momentum | 54.29 | -45.71 | 769 | 22.0 | -74.34 | -26.32 | -74.48 | 1570 |
| 64 | Volume breakout | breakout | 53.20 | -46.80 | 467 | 12.6 | -63.02 | -26.31 | -63.27 | 806 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -42.75 | -98.87 | 5161 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.39 | -23.11 | -79.94 | 1420 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.67 | -43.37 | -93.72 | 2536 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.07 | -29.34 | -89.32 | 1923 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.32 | -36.17 | -91.49 | 2344 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.32 | -31.57 | -90.36 | 2155 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -51.08 | -97.89 | 3525 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -53.53 | -96.17 | 3379 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.13 | -36.23 | -94.14 | 2453 |
| 74 | Squeeze breakout | breakout | 50.33 | -49.67 | 601 | 14.1 | -67.76 | -28.76 | -68.19 | 1186 |
| 75 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.31 | -32.54 | -82.58 | 1685 |
| 76 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.34 | -99.42 | 5769 |
| 77 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.66 | -40.48 | -92.82 | 2621 |
| 78 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -38.06 | -95.43 | 3363 |
| 79 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -70.43 | -99.78 | 6168 |
| 80 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.24 | -44.14 | -92.27 | 2333 |
| 81 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -60.10 | -97.75 | 3578 |
| 82 | Donchian 55/20 | breakout | 50.11 | -49.89 | 616 | 19.5 | -72.16 | -23.34 | -72.71 | 1281 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -58.11 | -98.67 | 4805 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -54.59 | -94.59 | 2775 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.51 | -39.08 | -84.51 | 1810 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.65 | -99.61 | 6304 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -28.89 | -88.31 | 2231 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.75 | -19.02 | -77.09 | 1691 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -36.89 | -90.63 | 2276 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.28 | -47.25 | -96.28 | 3822 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.15 | -50.86 | -90.15 | 2139 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.20 | -17.87 | -76.47 | 1579 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.53 | -47.80 | -96.55 | 4201 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -95.98 | -99.92 | 8273 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T13:35 | Max aggression: 5-day momentum | buy | TSLA | 89.34 | — | entry |
| 2026-10-27T13:35 | Max aggression: 5-day momentum | sell | SQQQ | 89.34 | -3.58 | target is flat |
| 2026-10-27T13:35 | Max aggression: 1-day momentum | buy | SOXL | 68.39 | — | entry |
| 2026-10-27T13:35 | Max aggression: 1-day momentum | sell | TSLA | 68.39 | 1.74 | target is flat |
| 2026-10-27T13:35 | Agent (rotation) | buy | TQQQ | 32.05 | — | entry |
| 2026-10-27T13:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | TQQQ | 105.57 | — | entry |
| 2026-10-27T13:35 | Agent (ML meta-label) | buy | TSLA | 9.62 | — | rebalance up |
| 2026-10-27T13:35 | Agent (ML meta-label) | sell | TECL | 10.13 | 0.38 | selected signal exited |
| 2026-10-27T13:35 | Agent (ML meta-label) | sell | SOXL | 8.17 | 0.27 | selected signal exited |
| 2026-10-27T13:35 | Agent (ML meta-label) | sell | NVDA | 6.14 | 0.11 | selected signal exited |
| 2026-10-27T13:35 | Daily: Bullish score | buy | TSLA | 20.81 | — | entry |
| 2026-10-27T13:35 | Daily: Bullish score | buy | MSFT | 22.69 | — | entry |
| 2026-10-27T13:35 | Daily: Momentum burst | buy | SQQQ | 5.48 | — | rebalance up |
| 2026-10-27T13:35 | Daily: Momentum burst | buy | SOXL | 22.77 | — | entry |
| 2026-10-27T13:35 | Daily: Momentum burst | buy | PLTR | 7.21 | — | rebalance up |
| 2026-10-27T13:35 | Daily: Momentum burst | sell | TNA | 15.86 | 0.21 | target is flat |
| 2026-10-27T13:35 | Daily: Momentum burst | sell | MSTR | 15.28 | -0.48 | target is flat |
| 2026-10-27T13:35 | Daily: Momentum burst | sell | LABU | 14.63 | -1.04 | target is flat |
| 2026-10-27T13:35 | MFI reversion · 1h | sell | META | 10.11 | -0.31 | stop-loss |
| 2026-10-27T13:35 | CCI reversion · 1h | sell | META | 10.05 | -0.18 | stop-loss |
| 2026-10-27T13:35 | Z-score reversion · 1h | buy | ETHU | 8.58 | — | entry |
| 2026-10-27T13:35 | Z-score reversion · 1h | sell | META | 8.19 | -0.24 | stop-loss |
| 2026-10-27T13:35 | Bollinger reversion · 1h | sell | LABU | 20.14 | -0.25 | target is flat |
| 2026-10-27T13:35 | Connors RSI(2) · 1h | sell | AAPL | 21.26 | 0.00 | target is flat |
| 2026-10-27T13:35 | RSI(14) reversion · 1h | buy | TQQQ | 4.10 | — | rebalance up |
| 2026-10-27T13:35 | RSI(14) reversion · 1h | buy | QQQ | 4.15 | — | rebalance up |
| 2026-10-27T13:35 | RSI(14) reversion · 1h | buy | ETHU | 4.22 | — | rebalance up |
| 2026-10-27T13:35 | RSI(14) reversion · 1h | buy | COIN | 4.20 | — | rebalance up |
| 2026-10-27T13:35 | RSI(14) reversion · 1h | buy | BITX | 4.27 | — | rebalance up |
| 2026-10-27T13:35 | RSI(14) reversion · 1h | sell | AMD | 7.38 | 0.50 | take-profit |
| 2026-10-27T13:35 | Candlestick reversal · 1h | buy | SOL-USD | 7.70 | — | entry |
| 2026-10-27T13:35 | Candlestick reversal · 1h | buy | MSTR | 5.70 | — | rebalance up |
| 2026-10-27T13:35 | Candlestick reversal · 1h | buy | ETHU | 3.99 | — | rebalance up |
| 2026-10-27T13:35 | Candlestick reversal · 1h | buy | DOGE-USD | 7.70 | — | entry |
| 2026-10-27T13:35 | Candlestick reversal · 1h | sell | TECL | 8.51 | 0.66 | take-profit |
| 2026-10-27T13:35 | Candlestick reversal · 1h | sell | NVDA | 8.02 | 0.21 | target is flat |
| 2026-10-27T13:35 | Candlestick reversal · 1h | sell | META | 7.64 | -0.09 | stop-loss |
| 2026-10-27T13:35 | Candlestick reversal · 1h | sell | AMD | 5.59 | 0.42 | take-profit |
| 2026-10-27T13:35 | Bollinger breakout · 1h | buy | XRP-USD | 14.62 | — | entry |
| 2026-10-27T13:35 | Bollinger breakout · 1h | buy | ETH-USD | 7.63 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 13:35:05.000127+00:00 -> 2026-10-27 13:45:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
