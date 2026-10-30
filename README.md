# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T19:25:05.000149+00:00 · 41686 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.52 (-8.48%)

Closed trades 130, win rate 40.8%, fees £3.76, max drawdown -11.45%.

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

Today: 31458 decisions in 2730 calls, $0.3915 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T19:25 | 9 / 17 / 3 | TNA 16% |  |
| Breezy | 2026-10-30T19:25 | 0 / 28 / 1 | cash |  |
| Boozy | 2026-10-30T19:25 | 9 / 19 / 1 | MSTR 72% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.71 | 6.71 | 0 | — | 7.91 | 3.86 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.79 | 5.79 | 22 | 45.5 | 9.68 | 3.13 | -4.92 | 27 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.85 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.42 | -0.58 | 0 | — | 2.63 | 1.13 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.53 | -2.47 | 96 | 35.4 | 6.35 | 2.98 | -2.21 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.47 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.11 | -4.72 | 20 |
| 12 | Hold SPY | benchmark | 96.87 | -3.13 | 0 | — | -1.69 | -0.82 | -3.94 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 14 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.46 | -8.76 | 203 |
| 16 | Agent (rotation) | meta | 94.82 | -5.18 | 129 | 31.0 | -3.59 | -2.26 | -8.60 | 166 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.04 | -5.96 | 0 | — | -7.76 | -2.87 | -8.12 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.51 | -6.49 | 0 | — | -4.14 | -1.46 | -7.64 | 1 |
| 19 | Parabolic SAR · 1h | trend | 91.77 | -8.23 | 140 | 28.6 | -17.77 | -3.99 | -20.27 | 250 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -9.76 | -5.67 | -12.21 | 226 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -21.15 | -7.54 | -21.15 | 98 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.62 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 90.84 | -9.16 | 312 | 34.6 | -12.17 | -3.62 | -17.21 | 591 |
| 24 | Hold BTC | benchmark | 90.31 | -9.69 | 0 | — | -2.58 | -0.25 | -12.65 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -6.03 | -1.64 | -12.70 | 88 |
| 26 | Copy: Insider buying | copy | 89.66 | -10.35 | 34 | 35.3 | -23.52 | -4.79 | -23.91 | 69 |
| 27 | Donchian 55/20 · 1h | breakout | 89.52 | -10.48 | 57 | 14.0 | -16.64 | -3.68 | -17.57 | 103 |
| 28 | Daily: Bullish score | daily | 88.49 | -11.51 | 14 | 21.4 | -6.81 | -0.84 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) ⏸ | copy | 87.72 | -12.28 | 1 | 0.0 | -4.74 | -0.55 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.10 | -3.66 | -15.04 | 101 |
| 31 | Volume breakout · 1h | breakout | 86.19 | -13.81 | 127 | 29.1 | -12.68 | -2.66 | -16.25 | 103 |
| 32 | Keltner breakout · 1h | breakout | 85.35 | -14.65 | 86 | 24.4 | -24.10 | -4.74 | -25.77 | 186 |
| 33 | ADX DI cross · 1h | trend | 85.33 | -14.67 | 141 | 19.1 | -16.72 | -3.25 | -20.33 | 261 |
| 34 | Stochastic reversion · 1h | reversion | 84.51 | -15.49 | 221 | 47.5 | -18.82 | -3.24 | -24.77 | 385 |
| 35 | Bollinger breakout · 1h | breakout | 83.68 | -16.32 | 132 | 26.5 | -16.26 | -3.01 | -21.61 | 242 |
| 36 | Connors RSI(2) · 1h | reversion | 83.21 | -16.79 | 188 | 40.4 | -21.53 | -6.86 | -22.04 | 162 |
| 37 | Opening range 15m | breakout | 83.20 | -16.80 | 387 | 31.3 | -17.18 | -4.91 | -19.23 | 723 |
| 38 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -26.45 | -3.42 | -30.48 | 35 |
| 39 | Ichimoku · 1h | trend | 82.34 | -17.66 | 79 | 13.9 | -20.52 | -4.10 | -24.80 | 118 |
| 40 | Max aggression: 5-day momentum ⏸ | meta | 82.08 | -17.92 | 15 | 40.0 | -36.56 | -2.61 | -37.35 | 25 |
| 41 | MFI reversion · 1h | reversion | 80.96 | -19.04 | 295 | 31.9 | -18.89 | -2.98 | -20.31 | 155 |
| 42 | Supertrend · 1h | trend | 80.57 | -19.43 | 137 | 13.1 | -26.25 | -4.83 | -28.99 | 216 |
| 43 | EMA 20/50 cross · 1h | trend | 79.97 | -20.03 | 88 | 11.4 | -23.08 | -4.34 | -26.95 | 135 |
| 44 | CCI reversion · 1h | reversion | 79.84 | -20.16 | 248 | 46.0 | -26.64 | -4.11 | -28.85 | 448 |
| 45 | MACD cross · 1h | trend | 79.22 | -20.79 | 283 | 24.0 | -30.30 | -5.37 | -32.86 | 473 |
| 46 | RSI momentum · 1h | momentum | 78.98 | -21.02 | 130 | 13.1 | -27.15 | -4.87 | -30.14 | 215 |
| 47 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.16 | -4.84 | -27.15 | 213 |
| 48 | Heikin-Ashi · 1h | trend | 78.74 | -21.26 | 333 | 23.7 | -41.60 | -8.99 | -42.17 | 668 |
| 49 | Williams %R · 1h | reversion | 78.72 | -21.28 | 253 | 47.0 | -35.42 | -6.23 | -36.13 | 530 |
| 50 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -18.57 | -2.84 | -22.55 | 211 |
| 51 | Triple EMA stack · 1h | trend | 78.22 | -21.78 | 119 | 15.1 | -30.54 | -5.68 | -33.14 | 208 |
| 52 | OBV trend · 1h | momentum | 77.76 | -22.24 | 232 | 17.7 | -34.16 | -6.80 | -36.79 | 299 |
| 53 | Bollinger reversion · 1h | reversion | 77.31 | -22.69 | 197 | 38.1 | -31.80 | -6.58 | -33.01 | 373 |
| 54 | Donchian 20/10 · 1h | breakout | 76.28 | -23.72 | 116 | 20.7 | -27.34 | -4.82 | -29.81 | 219 |
| 55 | ROC + volume · 1h | momentum | 75.87 | -24.13 | 293 | 25.6 | -29.36 | -5.04 | -31.91 | 385 |
| 56 | Max aggression: 1-day momentum | meta | 74.28 | -25.72 | 21 | 33.3 | -27.50 | -1.43 | -50.32 | 42 |
| 57 | Three white soldiers | momentum | 74.11 | -25.89 | 370 | 17.6 | -44.59 | -20.69 | -44.62 | 615 |
| 58 | VWAP momentum · 1h | momentum | 73.40 | -26.59 | 642 | 22.7 | -53.11 | -11.10 | -54.00 | 1233 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -20.80 | -3.58 | -26.17 | 196 |
| 60 | Candlestick reversal · 1h ⏸ | reversion | 72.04 | -27.96 | 320 | 28.4 | -36.49 | -7.11 | -36.85 | 552 |
| 61 | Agent (ML meta-label) ⏸ | meta | 71.93 | -28.07 | 1173 | 21.1 | -12.95 | -1.93 | -18.92 | 351 |
| 62 | EMA 9/21 cross · 1h | trend | 71.05 | -28.95 | 205 | 10.2 | -35.23 | -6.61 | -36.60 | 333 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -43.98 | -98.89 | 5247 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.49 | -23.65 | -79.49 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -44.45 | -93.61 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.84 | -30.60 | -88.88 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.22 | -37.57 | -91.22 | 2347 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -30.55 | -90.00 | 2225 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -51.66 | -97.77 | 3525 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.14 | -56.26 | -96.14 | 3374 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.90 | -34.65 | -93.94 | 2455 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.79 | -32.44 | -81.91 | 1682 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.92 | -99.49 | 5936 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.98 | -43.19 | -92.99 | 2637 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -37.15 | -95.46 | 3457 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.88 | -99.78 | 6244 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.02 | -44.04 | -92.02 | 2313 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.66 | -27.48 | -75.66 | 1577 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -59.14 | -97.67 | 3571 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -59.17 | -98.70 | 4869 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.15 | -28.27 | -69.33 | 1211 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -52.82 | -94.77 | 2798 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -37.72 | -84.80 | 1818 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.18 | -99.62 | 6387 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.34 | -30.02 | -88.41 | 2260 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.83 | -19.77 | -78.03 | 1743 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.95 | -37.45 | -91.02 | 2274 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -49.78 | -96.44 | 3850 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.07 | -53.07 | -90.11 | 2162 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.52 | -25.53 | -64.72 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.90 | -25.45 | -74.04 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.66 | -18.81 | -76.90 | 1600 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.82 | -49.61 | -96.83 | 4270 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.08 | -99.92 | 8337 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T19:21 | Candlestick reversal · 1h | sell | XRP-USD | 11.99 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T19:21 | Candlestick reversal · 1h | sell | SOL-USD | 12.00 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T19:21 | Candlestick reversal · 1h | sell | PLTR | 12.10 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T19:21 | Candlestick reversal · 1h | sell | DOGE-USD | 11.99 | -0.19 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T19:21 | Candlestick reversal · 1h | sell | BTC-USD | 11.99 | -0.18 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T19:21 | Candlestick reversal · 1h | sell | BITX | 11.98 | -0.31 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T19:15 | Agent | sell | PLTR | 18.37 | 0.05 | selected signal exited |
| 2026-10-30T19:10 | Agent | sell | LABU | 18.34 | 0.06 | selected signal exited |
| 2026-10-30T19:05 | CCI reversion · 1h | buy | TSLA | 4.22 | — | rebalance up |
| 2026-10-30T19:05 | CCI reversion · 1h | sell | BTC-USD | 15.88 | -0.43 | stop-loss |
| 2026-10-30T19:05 | Williams %R · 1h | buy | ETHU | 9.61 | — | rebalance up |
| 2026-10-30T19:05 | Williams %R · 1h | sell | BTC-USD | 15.65 | -0.22 | stop-loss |
| 2026-10-30T19:01 | Agent | buy | LABU | 18.28 | — | following Candlestick reversal |
| 2026-10-30T19:01 | Candlestick reversal · 1h | buy | XRP-USD | 3.96 | — | rebalance up |
| 2026-10-30T19:01 | Candlestick reversal · 1h | buy | SOL-USD | 12.08 | — | entry signal |
| 2026-10-30T19:01 | Candlestick reversal · 1h | buy | PLTR | 4.08 | — | rebalance up |
| 2026-10-30T19:01 | Candlestick reversal · 1h | buy | DOGE-USD | 4.03 | — | rebalance up |
| 2026-10-30T19:01 | Candlestick reversal · 1h | buy | BTC-USD | 4.01 | — | rebalance up |
| 2026-10-30T19:01 | Candlestick reversal · 1h | buy | BITX | 4.13 | — | rebalance up |
| 2026-10-30T19:01 | Candlestick reversal · 1h | sell | MSTR | 7.90 | -0.17 | target is flat |
| 2026-10-30T19:01 | Candlestick reversal · 1h | sell | ETH-USD | 8.12 | -0.01 | exit signal |
| 2026-10-30T19:01 | VWAP momentum · 1h | buy | ETHU | 18.16 | — | entry |
| 2026-10-30T19:01 | VWAP momentum · 1h | sell | DOGE-USD | 18.16 | -0.31 | exit signal |
| 2026-10-30T19:01 | MACD cross · 1h | buy | XRP-USD | 4.13 | — | rebalance up |
| 2026-10-30T19:01 | MACD cross · 1h | buy | ETH-USD | 4.00 | — | rebalance up |
| 2026-10-30T19:01 | MACD cross · 1h | buy | DOGE-USD | 4.16 | — | rebalance up |
| 2026-10-30T19:01 | MACD cross · 1h | sell | BTC-USD | 15.69 | -0.27 | exit signal |
| 2026-10-30T18:56 | MFI reversion · 1h | buy | COIN | 20.13 | — | entry |
| 2026-10-30T18:56 | MFI reversion · 1h | sell | SQQQ | 18.41 | 2.35 | target is flat |
| 2026-10-30T18:56 | OBV trend · 1h | buy | LABU | 19.46 | — | entry |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 19:25:05.000149+00:00 -> 2026-10-30 19:35:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
