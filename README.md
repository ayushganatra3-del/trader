# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-29T16:46:05.000125+00:00 · 40435 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.42 (-8.58%)

Closed trades 119, win rate 39.5%, fees £3.55, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-29 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, RENT 12%, CTY 12%, ACN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-28)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 23.78 · VIX 16.91 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, MSFT 5.4, PLTR 5.0, AAPL 4.2, LABU 3.9, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 24054 decisions in 2538 calls, $0.3051 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-29T16:46 | 4 / 13 / 11 | cash |  |
| Breezy | 2026-10-29T16:46 | 0 / 27 / 1 | cash |  |
| Boozy | 2026-10-29T16:46 | 4 / 23 / 1 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.83 | +8.30% | 12 |
| VWAP momentum · 1h | LABU | 2.51 | +26.96% | 3 |
| VWAP reversion | SQQQ | 2.50 | +4.75% | 5 |
| MACD zero-line | MSFT | 2.39 | +0.71% | 6 |
| Z-score reversion | TSLA | 2.35 | +3.07% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.92 | 6.92 | 0 | — | 7.73 | 3.76 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.05 | 1.97 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.23 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.39 | 1.39 | 0 | — | 4.58 | 1.97 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 101.12 | 1.12 | 93 | 46.2 | -10.56 | -2.86 | -12.63 | 142 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.03 | -0.97 | 0 | — | -0.11 | -0.01 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 7.05 | 3.33 | -1.98 | 90 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -4.59 | -5.34 | -4.72 | 21 |
| 12 | Copy: Congress Democrats (NANC) | copy | 97.27 | -2.73 | 0 | — | -0.28 | -0.06 | -5.99 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.10 | -2.90 | 0 | — | -4.83 | -1.91 | -7.83 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.72 | -2.50 | -5.83 | 1 |
| 15 | Hold BTC | benchmark | 96.22 | -3.78 | 0 | — | 3.98 | 0.83 | -9.28 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 17 | Agent (rotation) | meta | 95.70 | -4.30 | 127 | 31.5 | -2.38 | -1.59 | -7.47 | 175 |
| 18 | Three white soldiers · 1h | momentum | 95.26 | -4.74 | 15 | 13.3 | -2.37 | -2.17 | -4.63 | 27 |
| 19 | Gap and go | momentum | 95.12 | -4.88 | 122 | 29.5 | 4.98 | 1.63 | -8.76 | 204 |
| 20 | Copy: Cathie Wood (ARKK) | copy | 94.00 | -6.00 | 0 | — | 2.17 | 0.53 | -14.57 | 1 |
| 21 | Copy: Insider buying | copy | 92.96 | -7.04 | 32 | 37.5 | -20.06 | -3.95 | -24.43 | 67 |
| 22 | Opening range 30m | breakout | 92.86 | -7.14 | 293 | 36.5 | -9.54 | -2.81 | -17.21 | 581 |
| 23 | Donchian 55/20 · 1h | breakout | 92.73 | -7.27 | 53 | 15.1 | -13.47 | -3.02 | -15.47 | 102 |
| 24 | Daily: Momentum burst | daily | 92.28 | -7.72 | 15 | 13.3 | -13.01 | -2.45 | -17.57 | 35 |
| 25 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -20.93 | -7.21 | -21.07 | 102 |
| 26 | Agent | meta | 91.42 | -8.58 | 119 | 39.5 | -8.77 | -5.19 | -12.20 | 209 |
| 27 | Parabolic SAR · 1h | trend | 91.40 | -8.60 | 132 | 28.8 | -18.54 | -4.40 | -19.74 | 248 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.66 | -2.65 | -16.91 | 1 |
| 29 | Squeeze breakout · 1h | breakout | 90.73 | -9.27 | 56 | 23.2 | -5.37 | -1.45 | -12.65 | 95 |
| 30 | Daily: Bullish score | daily | 90.16 | -9.84 | 12 | 25.0 | -6.48 | -0.81 | -14.40 | 14 |
| 31 | ADX DI cross · 1h | trend | 89.71 | -10.29 | 132 | 18.2 | -14.54 | -2.88 | -16.63 | 259 |
| 32 | Stochastic reversion · 1h | reversion | 87.69 | -12.31 | 217 | 47.9 | -16.94 | -3.15 | -22.35 | 379 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 87.67 | -12.33 | 14 | 42.9 | -14.34 | -1.24 | -27.23 | 25 |
| 34 | Volume breakout · 1h | breakout | 87.30 | -12.70 | 123 | 30.1 | -13.97 | -2.97 | -16.64 | 107 |
| 35 | Z-score reversion · 1h | reversion | 87.14 | -12.86 | 125 | 36.0 | -11.50 | -1.75 | -21.48 | 205 |
| 36 | Agent (aggressive) | meta | 86.92 | -13.08 | 60 | 35.0 | -9.13 | -2.89 | -14.77 | 98 |
| 37 | Bollinger breakout · 1h | breakout | 86.60 | -13.40 | 126 | 26.2 | -13.59 | -2.50 | -18.40 | 249 |
| 38 | Keltner breakout · 1h | breakout | 86.08 | -13.92 | 80 | 25.0 | -20.41 | -3.95 | -23.14 | 190 |
| 39 | Opening range 15m | breakout | 85.38 | -14.62 | 366 | 32.2 | -14.41 | -4.12 | -17.87 | 710 |
| 40 | Supertrend · 1h | trend | 84.96 | -15.04 | 120 | 13.3 | -21.61 | -4.29 | -25.11 | 230 |
| 41 | Ichimoku · 1h | trend | 84.85 | -15.15 | 71 | 11.3 | -18.42 | -3.68 | -24.73 | 117 |
| 42 | RSI momentum · 1h | momentum | 83.96 | -16.04 | 117 | 13.7 | -20.74 | -4.08 | -24.06 | 214 |
| 43 | Connors RSI(2) · 1h | reversion | 83.71 | -16.29 | 185 | 40.5 | -21.34 | -6.82 | -21.67 | 163 |
| 44 | Triple EMA stack · 1h | trend | 83.16 | -16.84 | 110 | 14.5 | -28.81 | -5.61 | -30.81 | 210 |
| 45 | MACD cross · 1h | trend | 82.92 | -17.08 | 268 | 24.6 | -27.37 | -5.00 | -28.78 | 477 |
| 46 | EMA 20/50 cross · 1h | trend | 82.84 | -17.16 | 83 | 12.0 | -20.57 | -3.74 | -23.90 | 135 |
| 47 | CCI reversion · 1h | reversion | 82.59 | -17.41 | 242 | 46.7 | -18.90 | -2.45 | -28.07 | 448 |
| 48 | MFI reversion · 1h | reversion | 82.31 | -17.69 | 285 | 32.3 | -15.34 | -2.37 | -19.62 | 151 |
| 49 | Williams %R · 1h | reversion | 81.40 | -18.60 | 248 | 47.6 | -32.53 | -5.70 | -34.28 | 528 |
| 50 | Bollinger reversion · 1h | reversion | 80.90 | -19.10 | 191 | 38.7 | -27.54 | -5.42 | -29.78 | 360 |
| 51 | Donchian 20/10 · 1h | breakout | 80.84 | -19.16 | 108 | 21.3 | -23.15 | -4.29 | -26.02 | 221 |
| 52 | RSI(14) reversion · 1h | reversion | 80.42 | -19.58 | 109 | 27.5 | -10.82 | -1.79 | -24.48 | 199 |
| 53 | OBV trend · 1h | momentum | 80.32 | -19.68 | 221 | 17.2 | -36.16 | -7.19 | -37.04 | 307 |
| 54 | MACD zero-line · 1h | trend | 80.31 | -19.69 | 122 | 14.8 | -21.45 | -4.33 | -24.63 | 212 |
| 55 | Agent (ML meta-label) | meta | 78.69 | -21.31 | 1068 | 21.0 | -13.52 | -2.53 | -18.98 | 346 |
| 56 | Heikin-Ashi · 1h | trend | 78.10 | -21.90 | 318 | 24.2 | -41.90 | -9.15 | -42.93 | 671 |
| 57 | ROC + volume · 1h | momentum | 77.86 | -22.14 | 276 | 26.4 | -29.66 | -5.50 | -31.11 | 390 |
| 58 | Candlestick reversal · 1h | reversion | 76.85 | -23.15 | 302 | 30.1 | -32.87 | -6.17 | -34.42 | 548 |
| 59 | VWAP momentum · 1h | momentum | 76.22 | -23.78 | 619 | 23.3 | -49.23 | -10.54 | -50.30 | 1233 |
| 60 | EMA 9/21 cross · 1h | trend | 75.27 | -24.73 | 189 | 10.6 | -32.35 | -6.54 | -33.10 | 345 |
| 61 | Three white soldiers | momentum | 74.65 | -25.35 | 353 | 17.6 | -44.97 | -21.01 | -44.98 | 610 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 72.15 | -27.85 | 21 | 33.3 | -35.76 | -2.15 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -44.77 | -98.92 | 5246 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.72 | -23.37 | -78.80 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.59 | -44.22 | -93.61 | 2548 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.75 | -30.53 | -88.79 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.29 | -38.20 | -91.31 | 2363 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.60 | -31.91 | -90.61 | 2264 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.79 | -53.10 | -97.79 | 3538 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.14 | -56.99 | -96.14 | 3393 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.26 | -36.02 | -94.26 | 2488 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.09 | -33.95 | -82.15 | 1702 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -53.32 | -99.41 | 5727 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -43.10 | -92.94 | 2639 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.54 | -37.05 | -95.58 | 3471 |
| 76 | ROC + volume | momentum | 50.24 | -49.76 | 878 | 21.8 | -74.77 | -27.24 | -74.80 | 1564 |
| 77 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -71.95 | -99.77 | 6172 |
| 78 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.19 | -45.65 | -92.23 | 2326 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -61.11 | -97.74 | 3604 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.59 | -59.15 | -98.59 | 4781 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.71 | -29.68 | -69.72 | 1218 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.82 | -55.64 | -94.83 | 2805 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.89 | -38.67 | -84.90 | 1830 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -67.81 | -99.58 | 6288 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.39 | -28.66 | -87.48 | 2200 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -75.99 | -19.19 | -76.34 | 1656 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.26 | -37.27 | -90.29 | 2222 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.11 | -51.63 | -96.14 | 3769 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.47 | -49.66 | -89.55 | 2124 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.80 | -25.72 | -64.80 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.30 | -25.16 | -73.41 | 1283 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.57 | -18.40 | -75.70 | 1582 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.57 | -52.15 | -96.62 | 4195 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -95.65 | -99.92 | 8294 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-29T16:45 | Agent (ML meta-label) | buy | META | 1.01 | — | entry |
| 2026-10-29T16:40 | Agent (ML meta-label) | buy | SQQQ | 8.84 | — | rebalance up |
| 2026-10-29T16:40 | Agent (ML meta-label) | sell | IWM | 9.85 | -0.02 | selected signal exited |
| 2026-10-29T16:35 | Agent (ML meta-label) | buy | SQQQ | 1.00 | — | following VWAP reversion |
| 2026-10-29T16:35 | Agent (ML meta-label) | buy | MSFT | 8.73 | — | following MACD zero-line |
| 2026-10-29T16:35 | Agent (ML meta-label) | sell | SOL-USD | 9.74 | -0.09 | selected signal exited |
| 2026-10-29T16:35 | ROC + volume | buy | META | 12.57 | — | entry signal |
| 2026-10-29T16:35 | ROC + volume | sell | SOL-USD | 12.51 | -0.10 | stop-loss |
| 2026-10-29T16:30 | Agent (ML meta-label) | buy | SOL-USD | 9.82 | — | entry |
| 2026-10-29T16:30 | Agent (ML meta-label) | buy | IWM | 9.87 | — | entry |
| 2026-10-29T16:30 | Agent (ML meta-label) | buy | ETHU | 9.87 | — | entry |
| 2026-10-29T16:30 | Agent (ML meta-label) | sell | XRP-USD | 5.89 | -0.05 | rebalance down |
| 2026-10-29T16:30 | Agent (ML meta-label) | sell | TSLA | 5.91 | -0.01 | rebalance down |
| 2026-10-29T16:30 | Agent (ML meta-label) | sell | TNA | 5.91 | -0.01 | rebalance down |
| 2026-10-29T16:30 | Agent (ML meta-label) | sell | SOXL | 5.97 | -0.03 | rebalance down |
| 2026-10-29T16:30 | Agent (ML meta-label) | sell | DOGE-USD | 5.88 | -0.04 | rebalance down |
| 2026-10-29T16:30 | Agent (aggressive) | sell | LABU | 43.07 | -0.78 | selected signal exited |
| 2026-10-29T16:30 | Agent | sell | LABU | 19.40 | 1.40 | selected signal exited |
| 2026-10-29T16:30 | Williams %R · 1h | buy | MSFT | 20.36 | — | entry signal |
| 2026-10-29T16:30 | Bollinger reversion · 1h | buy | MSFT | 20.23 | — | entry signal |
| 2026-10-29T16:30 | Candlestick reversal · 1h | buy | XRP-USD | 6.39 | — | rebalance up |
| 2026-10-29T16:30 | Candlestick reversal · 1h | buy | TQQQ | 6.46 | — | rebalance up |
| 2026-10-29T16:30 | Candlestick reversal · 1h | sell | QQQ | 15.43 | -0.06 | exit signal |
| 2026-10-29T16:30 | Candlestick reversal · 1h | sell | PLTR | 15.39 | -0.06 | exit signal |
| 2026-10-29T16:30 | Candlestick reversal · 1h | sell | GOOGL | 15.39 | -0.11 | exit signal |
| 2026-10-29T16:30 | VWAP momentum · 1h | buy | XRP-USD | 1.38 | — | entry |
| 2026-10-29T16:30 | VWAP momentum · 1h | buy | AAPL | 5.87 | — | entry signal |
| 2026-10-29T16:30 | VWAP momentum · 1h | sell | LABU | 7.24 | 0.41 | exit signal |
| 2026-10-29T16:30 | MACD zero-line · 1h | sell | UPRO | 10.09 | -0.06 | exit signal |
| 2026-10-29T16:30 | MACD zero-line · 1h | sell | SPY | 10.10 | -0.04 | exit signal |
| 2026-10-29T16:30 | MACD cross · 1h | sell | UPRO | 3.95 | -0.05 | exit signal |
| 2026-10-29T16:30 | MACD cross · 1h | sell | SPY | 4.64 | 0.00 | exit signal |
| 2026-10-29T16:25 | Agent (ML meta-label) | buy | XRP-USD | 4.48 | — | rebalance up |
| 2026-10-29T16:25 | Agent (ML meta-label) | buy | TSLA | 4.43 | — | rebalance up |
| 2026-10-29T16:25 | Agent (ML meta-label) | buy | TNA | 4.44 | — | rebalance up |
| 2026-10-29T16:25 | Agent (ML meta-label) | buy | SOXL | 4.71 | — | rebalance up |
| 2026-10-29T16:25 | Agent (ML meta-label) | buy | DOGE-USD | 4.47 | — | rebalance up |
| 2026-10-29T16:25 | Agent (ML meta-label) | sell | SQQQ | 2.79 | 0.00 | selected signal exited |
| 2026-10-29T16:25 | Agent (ML meta-label) | sell | MSFT | 9.88 | 0.00 | selected signal exited |
| 2026-10-29T16:25 | Agent (ML meta-label) | sell | META | 9.86 | -0.02 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-31 16:46:05.000125+00:00 -> 2026-10-29 16:56:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
