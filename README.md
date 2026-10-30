# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T18:55:05.000117+00:00 · 41665 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.34 (-8.66%)

Closed trades 128, win rate 39.8%, fees £3.73, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.26 | -0.06 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-29 | MSM 12%, LRN 12%, SRRK 12%, BPRE 12%, RENT 12%, ACN 12%, SCQCU 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-29)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.18 · VIX 17.20 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, IWM 5.9, LABU 5.7, AAPL 5.2, SQQQ 4.9, PLTR 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 29580 decisions in 2667 calls, $0.3695 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T18:55 | 1 / 7 / 16 | cash |  |
| Breezy | 2026-10-30T18:55 | 0 / 19 / 5 | cash |  |
| Boozy | 2026-10-30T18:55 | 4 / 18 / 2 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.77 | +1.01% | 7 |
| VWAP reversion | SQQQ | 2.64 | +4.39% | 5 |
| Candlestick reversal | LABU | 2.56 | +7.90% | 14 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Candlestick reversal | PLTR | 2.37 | +5.05% | 17 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.69 | 6.69 | 0 | — | 7.89 | 3.85 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.18 | 6.18 | 22 | 45.5 | 10.08 | 3.23 | -4.92 | 27 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.85 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.20 | -0.80 | 0 | — | 2.41 | 1.03 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.33 | -2.67 | 96 | 35.4 | 6.38 | 3.00 | -1.98 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.47 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.11 | -4.72 | 20 |
| 12 | Hold SPY | benchmark | 96.83 | -3.17 | 0 | — | -1.73 | -0.84 | -3.66 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 14 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.46 | -8.76 | 203 |
| 16 | Agent (rotation) | meta | 94.75 | -5.25 | 129 | 31.0 | -3.66 | -2.29 | -8.60 | 166 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.69 | -5.31 | 0 | — | -7.12 | -2.73 | -7.83 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.50 | -6.50 | 0 | — | -4.14 | -1.46 | -7.63 | 1 |
| 19 | Parabolic SAR · 1h | trend | 91.86 | -8.14 | 140 | 28.6 | -17.69 | -3.96 | -20.27 | 250 |
| 20 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -21.15 | -7.54 | -21.15 | 98 |
| 21 | Agent | meta | 91.34 | -8.66 | 128 | 39.8 | -9.88 | -5.72 | -12.21 | 226 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.62 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 90.59 | -9.41 | 312 | 34.6 | -12.39 | -3.67 | -17.21 | 591 |
| 24 | Hold BTC | benchmark | 90.44 | -9.56 | 0 | — | -2.46 | -0.23 | -12.47 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -6.03 | -1.64 | -12.70 | 88 |
| 26 | Copy: Insider buying | copy | 89.50 | -10.49 | 34 | 35.3 | -23.68 | -4.81 | -23.91 | 69 |
| 27 | Donchian 55/20 · 1h | breakout | 89.44 | -10.56 | 57 | 14.0 | -16.73 | -3.69 | -17.65 | 103 |
| 28 | Daily: Bullish score | daily | 88.34 | -11.66 | 14 | 21.4 | -6.99 | -0.87 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) ⏸ | copy | 87.72 | -12.28 | 1 | 0.0 | -5.26 | -0.62 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.10 | -3.66 | -15.04 | 101 |
| 31 | Volume breakout · 1h | breakout | 86.27 | -13.72 | 127 | 29.1 | -12.60 | -2.64 | -16.25 | 103 |
| 32 | Keltner breakout · 1h | breakout | 85.43 | -14.57 | 86 | 24.4 | -24.38 | -4.80 | -25.77 | 187 |
| 33 | ADX DI cross · 1h | trend | 85.40 | -14.60 | 141 | 19.1 | -16.49 | -3.21 | -20.33 | 260 |
| 34 | Stochastic reversion · 1h | reversion | 83.98 | -16.02 | 221 | 47.5 | -19.33 | -3.30 | -24.64 | 385 |
| 35 | Bollinger breakout · 1h | breakout | 83.75 | -16.25 | 132 | 26.5 | -16.18 | -3.00 | -21.61 | 242 |
| 36 | Connors RSI(2) · 1h | reversion | 83.01 | -16.99 | 188 | 40.4 | -21.72 | -6.90 | -22.04 | 162 |
| 37 | Opening range 15m | breakout | 82.97 | -17.04 | 387 | 31.3 | -17.44 | -4.96 | -19.41 | 723 |
| 38 | Ichimoku · 1h | trend | 82.42 | -17.58 | 79 | 13.9 | -20.45 | -4.09 | -24.80 | 118 |
| 39 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -27.68 | -3.41 | -30.04 | 35 |
| 40 | Max aggression: 5-day momentum ⏸ | meta | 82.08 | -17.92 | 15 | 40.0 | -37.06 | -2.62 | -37.16 | 25 |
| 41 | Supertrend · 1h | trend | 80.63 | -19.37 | 137 | 13.1 | -26.16 | -4.82 | -28.91 | 216 |
| 42 | MFI reversion · 1h | reversion | 80.35 | -19.65 | 294 | 31.6 | -19.00 | -3.00 | -20.24 | 154 |
| 43 | EMA 20/50 cross · 1h | trend | 79.89 | -20.11 | 88 | 11.4 | -23.17 | -4.35 | -26.95 | 135 |
| 44 | CCI reversion · 1h | reversion | 79.68 | -20.32 | 247 | 46.2 | -26.75 | -4.13 | -28.85 | 448 |
| 45 | MACD cross · 1h | trend | 79.27 | -20.73 | 282 | 24.1 | -30.43 | -5.40 | -32.86 | 474 |
| 46 | RSI momentum · 1h | momentum | 78.91 | -21.09 | 130 | 13.1 | -27.27 | -4.88 | -30.19 | 215 |
| 47 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -23.99 | -4.81 | -27.15 | 213 |
| 48 | Heikin-Ashi · 1h | trend | 78.82 | -21.18 | 333 | 23.7 | -41.55 | -8.98 | -42.17 | 668 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -18.82 | -2.86 | -22.53 | 211 |
| 50 | Williams %R · 1h | reversion | 78.49 | -21.51 | 252 | 47.2 | -35.67 | -6.25 | -36.15 | 530 |
| 51 | Triple EMA stack · 1h | trend | 78.15 | -21.85 | 119 | 15.1 | -30.66 | -5.68 | -33.21 | 208 |
| 52 | OBV trend · 1h | momentum | 77.69 | -22.31 | 232 | 17.7 | -34.21 | -6.82 | -36.79 | 299 |
| 53 | Bollinger reversion · 1h | reversion | 76.86 | -23.14 | 197 | 38.1 | -32.25 | -6.62 | -33.09 | 372 |
| 54 | Donchian 20/10 · 1h | breakout | 76.36 | -23.64 | 116 | 20.7 | -27.25 | -4.81 | -29.81 | 219 |
| 55 | ROC + volume · 1h | momentum | 75.94 | -24.06 | 293 | 25.6 | -29.65 | -5.07 | -31.91 | 386 |
| 56 | Max aggression: 1-day momentum | meta | 74.56 | -25.45 | 21 | 33.3 | -27.23 | -1.40 | -50.32 | 42 |
| 57 | Three white soldiers | momentum | 74.11 | -25.89 | 370 | 17.6 | -44.59 | -20.69 | -44.62 | 615 |
| 58 | VWAP momentum · 1h | momentum | 73.45 | -26.55 | 641 | 22.8 | -53.36 | -11.09 | -54.29 | 1232 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -21.56 | -3.70 | -26.27 | 194 |
| 60 | Candlestick reversal · 1h | reversion | 72.33 | -27.67 | 312 | 29.2 | -36.22 | -7.02 | -36.77 | 551 |
| 61 | Agent (ML meta-label) ⏸ | meta | 71.93 | -28.07 | 1173 | 21.1 | -18.25 | -3.18 | -18.97 | 360 |
| 62 | EMA 9/21 cross · 1h | trend | 70.97 | -29.03 | 205 | 10.2 | -35.30 | -6.61 | -36.67 | 333 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -44.11 | -98.89 | 5233 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.53 | -23.70 | -79.53 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -44.40 | -93.61 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.86 | -30.65 | -88.86 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -37.48 | -91.19 | 2345 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.01 | -30.52 | -90.01 | 2225 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -51.58 | -97.76 | 3518 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.14 | -56.18 | -96.14 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.89 | -34.66 | -93.93 | 2457 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.78 | -32.37 | -81.91 | 1682 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -54.10 | -99.49 | 5924 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.98 | -43.16 | -92.98 | 2633 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -37.18 | -95.46 | 3456 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.92 | -99.78 | 6233 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.01 | -44.03 | -92.02 | 2311 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.61 | -27.41 | -75.64 | 1575 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -58.88 | -97.66 | 3567 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -59.11 | -98.70 | 4860 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.16 | -28.29 | -69.33 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -52.71 | -94.77 | 2794 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.69 | -37.61 | -84.80 | 1817 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.34 | -99.62 | 6381 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.41 | -30.04 | -88.41 | 2256 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.26 | -20.02 | -78.26 | 1740 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.97 | -37.70 | -90.97 | 2269 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.44 | -49.58 | -96.44 | 3848 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.05 | -52.74 | -90.05 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.56 | -25.56 | -64.70 | 824 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.88 | -25.48 | -74.03 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.68 | -18.78 | -76.68 | 1596 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.84 | -49.94 | -96.84 | 4273 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -94.56 | -99.92 | 8323 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T18:50 | Opening range 30m | sell | AMZN | 22.65 | -0.21 | stop-loss |
| 2026-10-30T18:45 | Donchian 55/20 · 1h | sell | LABU | 22.03 | -1.34 | stop-loss |
| 2026-10-30T18:35 | CCI reversion · 1h | buy | TSLA | 15.68 | — | entry |
| 2026-10-30T18:35 | CCI reversion · 1h | sell | SOL-USD | 15.68 | -0.63 | stop-loss |
| 2026-10-30T18:35 | Connors RSI(2) · 1h | sell | TNA | 20.40 | -0.70 | target is flat |
| 2026-10-30T18:35 | Connors RSI(2) · 1h | sell | IWM | 20.84 | -0.25 | stop-loss |
| 2026-10-30T18:35 | VWAP momentum · 1h | buy | ETH-USD | 3.60 | — | rebalance up |
| 2026-10-30T18:35 | VWAP momentum · 1h | sell | ETHU | 3.60 | -0.03 | target is flat |
| 2026-10-30T18:35 | Supertrend · 1h | sell | TSLA | 20.14 | -0.15 | target is flat |
| 2026-10-30T18:35 | Opening range 30m | buy | ETHU | 4.72 | — | rebalance up |
| 2026-10-30T18:35 | Opening range 30m | buy | AMZN | 4.57 | — | rebalance up |
| 2026-10-30T18:35 | Opening range 30m | sell | BITX | 15.06 | -0.20 | exit signal |
| 2026-10-30T18:35 | Opening range 15m | sell | ETHU | 20.62 | -0.25 | exit signal |
| 2026-10-30T18:31 | OBV trend · 1h | sell | LABU | 18.66 | -0.56 | exit signal |
| 2026-10-30T18:31 | Ichimoku · 1h | sell | LABU | 20.22 | -0.04 | exit signal |
| 2026-10-30T18:31 | Supertrend · 1h | sell | LABU | 20.10 | -0.13 | exit signal |
| 2026-10-30T18:30 | Candlestick reversal · 1h | sell | ETHU | 8.15 | -0.04 | exit signal |
| 2026-10-30T18:30 | RSI momentum · 1h | sell | TSLA | 16.35 | 0.10 | exit signal |
| 2026-10-30T18:30 | ROC + volume · 1h | sell | AAPL | 18.74 | -0.22 | exit signal |
| 2026-10-30T18:30 | VWAP momentum · 1h | buy | ETHU | 3.63 | — | entry signal |
| 2026-10-30T18:30 | Supertrend · 1h | buy | TSLA | 4.15 | — | rebalance up |
| 2026-10-30T18:30 | Supertrend · 1h | buy | LABU | 4.17 | — | rebalance up |
| 2026-10-30T18:30 | Supertrend · 1h | sell | META | 16.05 | -0.23 | exit signal |
| 2026-10-30T18:30 | Supertrend · 1h | sell | AAPL | 16.02 | -0.15 | exit signal |
| 2026-10-30T18:30 | Triple EMA stack · 1h | sell | TSLA | 16.23 | -0.03 | exit signal |
| 2026-10-30T18:30 | EMA 9/21 cross · 1h | sell | TSLA | 17.68 | 0.07 | exit signal |
| 2026-10-30T18:30 | EMA 9/21 cross · 1h | sell | IWM | 17.75 | -0.14 | exit signal |
| 2026-10-30T18:21 | Opening range 15m | buy | ETHU | 4.23 | — | rebalance up |
| 2026-10-30T18:21 | Opening range 15m | buy | AMZN | 4.17 | — | rebalance up |
| 2026-10-30T18:21 | Opening range 15m | sell | BITX | 16.61 | -0.21 | exit signal |
| 2026-10-30T18:13 | Copy: Insider buying | buy | FBK | 10.33 | — | entry |
| 2026-10-30T18:13 | Copy: Insider buying | sell | IAM | 9.82 | -2.07 | target is flat |
| 2026-10-30T18:11 | Trend pullback · 1h | sell | AAPL | 22.60 | -0.31 | stop-loss |
| 2026-10-30T18:07 | Opening range 30m | buy | SQQQ | 6.49 | — | rebalance up |
| 2026-10-30T18:07 | Opening range 15m | buy | SQQQ | 6.19 | — | rebalance up |
| 2026-10-30T18:05 | Opening range 30m | buy | TSLA | 6.90 | — | rebalance up |
| 2026-10-30T18:05 | Opening range 30m | buy | ETHU | 6.71 | — | rebalance up |
| 2026-10-30T18:05 | Opening range 30m | buy | AMZN | 6.76 | — | rebalance up |
| 2026-10-30T18:05 | Opening range 30m | sell | META | 11.32 | -0.12 | stop-loss |
| 2026-10-30T18:05 | Opening range 15m | buy | TSLA | 6.29 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 18:55:05.000117+00:00 -> 2026-10-30 19:05:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
