# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T18:25:05.000136+00:00 · 41637 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.32 (-8.68%)

Closed trades 128, win rate 39.8%, fees £3.73, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.24 | -0.08 |

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

Today: 27765 decisions in 2583 calls, $0.3478 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T18:25 | 3 / 10 / 12 | cash |  |
| Breezy | 2026-10-30T18:25 | 0 / 20 / 5 | cash |  |
| Boozy | 2026-10-30T18:25 | 5 / 16 / 4 | MSTR 55% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.63 | 6.63 | 0 | — | 7.93 | 3.87 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.70 | 5.70 | 22 | 45.5 | 9.69 | 3.13 | -4.92 | 27 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.85 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.50 | -0.50 | 0 | — | 2.81 | 1.22 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.40 | -2.60 | 96 | 35.4 | 6.49 | 3.05 | -1.98 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.47 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.11 | -4.72 | 20 |
| 12 | Hold SPY | benchmark | 96.86 | -3.14 | 0 | — | -1.60 | -0.78 | -3.54 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 14 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 15 | Agent (rotation) | meta | 94.85 | -5.15 | 129 | 31.0 | -3.51 | -2.21 | -8.52 | 164 |
| 16 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.46 | -8.76 | 203 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.60 | -5.40 | 0 | — | -7.12 | -2.73 | -7.83 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.89 | -6.11 | 0 | — | -3.65 | -1.34 | -7.16 | 1 |
| 19 | Parabolic SAR · 1h | trend | 91.75 | -8.25 | 140 | 28.6 | -17.77 | -3.99 | -20.27 | 250 |
| 20 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -21.15 | -7.54 | -21.15 | 98 |
| 21 | Agent | meta | 91.32 | -8.68 | 128 | 39.8 | -9.87 | -5.72 | -12.21 | 226 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.62 | -16.91 | 1 |
| 23 | Hold BTC | benchmark | 90.87 | -9.13 | 0 | — | -1.97 | -0.15 | -12.47 | 1 |
| 24 | Opening range 30m | breakout | 90.84 | -9.16 | 310 | 34.8 | -12.01 | -3.58 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -7.04 | -1.93 | -12.70 | 92 |
| 26 | Copy: Insider buying | copy | 89.99 | -10.01 | 34 | 35.3 | -23.13 | -4.72 | -23.91 | 69 |
| 27 | Donchian 55/20 · 1h | breakout | 89.54 | -10.46 | 56 | 14.3 | -16.56 | -3.67 | -17.59 | 103 |
| 28 | Daily: Bullish score | daily | 88.32 | -11.68 | 14 | 21.4 | -6.99 | -0.87 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) ⏸ | copy | 87.72 | -12.28 | 1 | 0.0 | -5.08 | -0.60 | -15.66 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.10 | -3.66 | -15.04 | 101 |
| 31 | Volume breakout · 1h | breakout | 86.18 | -13.82 | 127 | 29.1 | -12.68 | -2.66 | -16.25 | 103 |
| 32 | Keltner breakout · 1h | breakout | 85.33 | -14.67 | 86 | 24.4 | -24.27 | -4.78 | -25.77 | 188 |
| 33 | ADX DI cross · 1h | trend | 85.31 | -14.69 | 141 | 19.1 | -16.56 | -3.22 | -20.33 | 260 |
| 34 | Stochastic reversion · 1h | reversion | 84.42 | -15.58 | 221 | 47.5 | -18.83 | -3.24 | -24.20 | 385 |
| 35 | Bollinger breakout · 1h | breakout | 83.66 | -16.34 | 132 | 26.5 | -16.28 | -3.02 | -21.61 | 242 |
| 36 | Connors RSI(2) · 1h | reversion | 83.15 | -16.85 | 186 | 40.9 | -21.54 | -6.86 | -21.85 | 162 |
| 37 | Opening range 15m | breakout | 83.11 | -16.89 | 386 | 31.3 | -17.17 | -4.90 | -19.16 | 723 |
| 38 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -27.05 | -3.42 | -29.44 | 35 |
| 39 | Ichimoku · 1h | trend | 82.38 | -17.62 | 78 | 14.1 | -20.45 | -4.09 | -24.80 | 118 |
| 40 | Max aggression: 5-day momentum ⏸ | meta | 82.08 | -17.92 | 15 | 40.0 | -36.47 | -2.61 | -36.73 | 25 |
| 41 | Supertrend · 1h | trend | 80.64 | -19.36 | 133 | 13.5 | -26.07 | -4.81 | -28.91 | 216 |
| 42 | MFI reversion · 1h | reversion | 80.42 | -19.58 | 294 | 31.6 | -18.67 | -2.95 | -20.24 | 153 |
| 43 | CCI reversion · 1h | reversion | 80.04 | -19.96 | 246 | 46.3 | -26.38 | -4.07 | -28.85 | 448 |
| 44 | EMA 20/50 cross · 1h | trend | 79.96 | -20.04 | 88 | 11.4 | -23.06 | -4.33 | -26.95 | 135 |
| 45 | MACD cross · 1h | trend | 79.44 | -20.56 | 282 | 24.1 | -30.21 | -5.37 | -32.86 | 474 |
| 46 | RSI momentum · 1h | momentum | 78.96 | -21.04 | 129 | 12.4 | -27.14 | -4.88 | -30.14 | 215 |
| 47 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -23.99 | -4.81 | -27.15 | 213 |
| 48 | Williams %R · 1h | reversion | 78.85 | -21.15 | 252 | 47.2 | -35.28 | -6.21 | -35.83 | 530 |
| 49 | Heikin-Ashi · 1h | trend | 78.72 | -21.27 | 333 | 23.7 | -41.60 | -8.99 | -42.17 | 668 |
| 50 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -18.24 | -2.80 | -22.16 | 210 |
| 51 | Triple EMA stack · 1h | trend | 78.20 | -21.80 | 118 | 14.4 | -30.54 | -5.67 | -33.15 | 208 |
| 52 | OBV trend · 1h | momentum | 77.65 | -22.35 | 231 | 17.7 | -34.13 | -6.81 | -36.78 | 300 |
| 53 | Bollinger reversion · 1h | reversion | 77.20 | -22.80 | 197 | 38.1 | -31.86 | -6.59 | -32.73 | 372 |
| 54 | Donchian 20/10 · 1h | breakout | 76.27 | -23.73 | 116 | 20.7 | -27.39 | -4.83 | -29.81 | 219 |
| 55 | ROC + volume · 1h | momentum | 75.86 | -24.14 | 292 | 25.7 | -29.40 | -5.04 | -31.91 | 385 |
| 56 | Max aggression: 1-day momentum | meta | 74.22 | -25.78 | 21 | 33.3 | -27.49 | -1.43 | -50.32 | 42 |
| 57 | Three white soldiers | momentum | 74.11 | -25.89 | 370 | 17.6 | -44.59 | -20.69 | -44.62 | 615 |
| 58 | VWAP momentum · 1h | momentum | 73.58 | -26.42 | 640 | 22.8 | -53.25 | -11.10 | -54.29 | 1232 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -21.03 | -3.65 | -25.90 | 194 |
| 60 | Candlestick reversal · 1h | reversion | 72.65 | -27.35 | 311 | 29.3 | -35.77 | -6.97 | -36.37 | 551 |
| 61 | Agent (ML meta-label) ⏸ | meta | 71.93 | -28.07 | 1173 | 21.1 | -17.31 | -3.32 | -18.69 | 341 |
| 62 | EMA 9/21 cross · 1h | trend | 71.03 | -28.97 | 203 | 9.9 | -35.17 | -6.61 | -36.58 | 333 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -44.25 | -98.89 | 5239 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.51 | -23.75 | -79.52 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.62 | -44.49 | -93.62 | 2539 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.84 | -30.62 | -88.84 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.20 | -37.52 | -91.20 | 2346 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -30.50 | -90.01 | 2226 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -51.68 | -97.76 | 3519 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.14 | -56.19 | -96.14 | 3378 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.91 | -34.77 | -93.96 | 2459 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.76 | -32.29 | -81.91 | 1682 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -54.52 | -99.48 | 5913 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.00 | -43.42 | -93.00 | 2634 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -37.18 | -95.46 | 3456 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -73.00 | -99.78 | 6230 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.01 | -44.02 | -92.01 | 2311 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.66 | -27.45 | -75.68 | 1577 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -59.30 | -97.67 | 3570 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -59.25 | -98.69 | 4847 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.29 | -28.54 | -69.45 | 1210 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -53.20 | -94.78 | 2795 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.70 | -37.67 | -84.80 | 1817 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.40 | -99.62 | 6365 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.35 | -30.02 | -88.35 | 2243 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.89 | -19.83 | -77.89 | 1730 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.84 | -37.87 | -90.84 | 2274 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -49.97 | -96.42 | 3835 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.00 | -52.36 | -90.00 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.63 | -25.63 | -64.74 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.90 | -25.49 | -74.03 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.45 | -18.66 | -76.45 | 1583 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.82 | -50.12 | -96.82 | 4259 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -94.58 | -99.92 | 8321 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-30T18:05 | Opening range 15m | buy | ETHU | 4.70 | — | rebalance up |
| 2026-10-30T18:05 | Opening range 15m | buy | BITX | 6.25 | — | rebalance up |
| 2026-10-30T18:05 | Opening range 15m | buy | AMZN | 6.16 | — | rebalance up |
| 2026-10-30T18:05 | Opening range 15m | sell | META | 10.38 | -0.10 | stop-loss |
| 2026-10-30T18:02 | Agent (ML meta-label) | sell | SQQQ | 7.29 | 0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T18:02 | Agent (ML meta-label) | sell | SOXL | 8.99 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T18:02 | Agent (ML meta-label) | sell | COIN | 7.20 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T18:00 | Bollinger reversion · 1h | buy | ETHU | 2.03 | — | entry |
| 2026-10-30T18:00 | Bollinger reversion · 1h | buy | BITX | 7.74 | — | entry |
| 2026-10-30T18:00 | Bollinger reversion · 1h | sell | ETH-USD | 9.77 | 0.03 | exit signal |
| 2026-10-30T18:00 | Donchian 55/20 · 1h | buy | TSLA | 4.54 | — | rebalance up |
| 2026-10-30T17:56 | Agent (ML meta-label) | sell | TSLA | 7.17 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T17:56 | Agent (ML meta-label) | sell | SOL-USD | 7.65 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T17:56 | Agent (ML meta-label) | sell | MSTR | 8.32 | -0.30 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T17:56 | Agent (ML meta-label) | sell | META | 7.21 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T17:56 | Agent (ML meta-label) | sell | ETHU | 10.30 | 0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T17:56 | Agent (ML meta-label) | sell | BITX | 7.22 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T17:56 | Agent | sell | LABU | 18.27 | -0.07 | selected signal exited |
| 2026-10-30T17:56 | Williams %R · 1h | buy | ETHU | 6.16 | — | entry |
| 2026-10-30T17:56 | Williams %R · 1h | sell | SOL-USD | 6.16 | -0.13 | rebalance down |
| 2026-10-30T17:45 | Agent (ML meta-label) | buy | TSLA | 7.22 | — | entry |
| 2026-10-30T17:45 | Agent (ML meta-label) | sell | TNA | 7.78 | -0.00 | selected signal exited |
| 2026-10-30T17:45 | MACD cross · 1h | buy | BTC-USD | 3.97 | — | rebalance up |
| 2026-10-30T17:45 | MACD cross · 1h | sell | ETH-USD | 3.97 | 0.00 | rebalance down |
| 2026-10-30T17:35 | Agent (ML meta-label) | buy | TNA | 7.78 | — | entry |
| 2026-10-30T17:35 | Agent (ML meta-label) | buy | SOL-USD | 7.73 | — | entry |
| 2026-10-30T17:30 | Agent (ML meta-label) | buy | ETHU | 3.68 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 18:25:05.000136+00:00 -> 2026-10-30 18:35:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
