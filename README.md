# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T09:15:05.000144+00:00 · 41225 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.68 (-8.32%)

Closed trades 122, win rate 40.2%, fees £3.61, max drawdown -11.45%.

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

Today: 6735 decisions in 1347 calls, $0.0942 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T09:15 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-30T09:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-30T09:15 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.77 | +1.01% | 7 |
| Candlestick reversal | LABU | 2.56 | +7.90% | 14 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Candlestick reversal | PLTR | 2.37 | +5.05% | 17 |
| Z-score reversion | TSLA | 2.35 | +3.07% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.23 | 2.03 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 106.14 | 6.14 | 0 | — | 7.59 | 3.72 | -5.18 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.23 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.95 | 0.95 | 0 | — | 4.35 | 1.89 | -5.02 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Hold SPY | benchmark | 98.85 | -1.15 | 0 | — | 0.56 | 0.37 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 7.05 | 3.33 | -1.98 | 90 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.74 | -2.52 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -5.09 | -5.81 | -5.22 | 22 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.95 | -3.05 | 0 | — | -0.48 | -0.15 | -5.99 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.67 | -3.33 | 0 | — | -5.05 | -2.01 | -7.83 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -3.20 | -2.06 | -7.40 | 174 |
| 17 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 5.27 | 1.72 | -8.76 | 204 |
| 18 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 19 | Copy: Cathie Wood (ARKK) | copy | 93.35 | -6.65 | 0 | — | 2.42 | 0.57 | -14.57 | 1 |
| 20 | Copy: Insider buying | copy | 92.57 | -7.43 | 33 | 36.4 | -21.70 | -4.41 | -23.91 | 67 |
| 21 | Donchian 55/20 · 1h | breakout | 92.20 | -7.80 | 54 | 14.8 | -13.77 | -3.09 | -15.52 | 102 |
| 22 | Daily: Momentum burst | daily | 91.88 | -8.12 | 15 | 13.3 | -12.93 | -2.43 | -17.57 | 35 |
| 23 | Opening range 30m | breakout | 91.77 | -8.23 | 304 | 35.5 | -11.10 | -3.30 | -17.21 | 580 |
| 24 | Agent | meta | 91.68 | -8.32 | 122 | 40.2 | -9.47 | -5.57 | -12.21 | 218 |
| 25 | Hold BTC | benchmark | 91.67 | -8.33 | 0 | — | -0.37 | 0.11 | -12.47 | 1 |
| 26 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.17 | -7.33 | -21.50 | 99 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.75 | -2.67 | -16.91 | 1 |
| 28 | Squeeze breakout · 1h | breakout | 90.57 | -9.43 | 56 | 23.2 | -4.51 | -1.22 | -12.65 | 93 |
| 29 | Daily: Bullish score | daily | 90.41 | -9.59 | 12 | 25.0 | -5.76 | -0.69 | -14.40 | 14 |
| 30 | Parabolic SAR · 1h | trend | 90.01 | -9.99 | 137 | 28.5 | -19.83 | -4.61 | -19.94 | 247 |
| 31 | ADX DI cross · 1h | trend | 89.37 | -10.63 | 137 | 19.7 | -15.76 | -3.17 | -16.97 | 262 |
| 32 | Stochastic reversion · 1h | reversion | 87.82 | -12.18 | 218 | 48.2 | -16.01 | -2.77 | -22.69 | 381 |
| 33 | Max aggression: 5-day momentum | meta | 87.67 | -12.33 | 14 | 42.9 | -14.69 | -1.27 | -27.23 | 25 |
| 34 | Agent (aggressive) | meta | 87.41 | -12.59 | 62 | 35.5 | -11.10 | -3.66 | -15.04 | 101 |
| 35 | Volume breakout · 1h | breakout | 86.54 | -13.46 | 124 | 29.8 | -14.65 | -3.12 | -17.33 | 107 |
| 36 | Bollinger breakout · 1h | breakout | 85.89 | -14.11 | 128 | 26.6 | -11.99 | -2.16 | -19.10 | 244 |
| 37 | Z-score reversion · 1h | reversion | 85.57 | -14.43 | 126 | 35.7 | -13.85 | -2.16 | -21.48 | 207 |
| 38 | Keltner breakout · 1h | breakout | 85.31 | -14.69 | 84 | 23.8 | -22.78 | -4.60 | -23.96 | 197 |
| 39 | Ichimoku · 1h | trend | 84.38 | -15.62 | 75 | 10.7 | -18.75 | -3.76 | -24.73 | 118 |
| 40 | Opening range 15m | breakout | 84.37 | -15.63 | 376 | 32.2 | -16.00 | -4.59 | -18.10 | 709 |
| 41 | Connors RSI(2) · 1h | reversion | 84.18 | -15.82 | 185 | 40.5 | -20.46 | -6.51 | -21.55 | 159 |
| 42 | Supertrend · 1h | trend | 83.69 | -16.31 | 126 | 14.3 | -23.64 | -4.52 | -26.18 | 218 |
| 43 | RSI momentum · 1h | momentum | 83.27 | -16.73 | 122 | 13.1 | -20.37 | -4.04 | -23.98 | 214 |
| 44 | Triple EMA stack · 1h | trend | 82.41 | -17.59 | 113 | 14.2 | -27.37 | -5.27 | -30.37 | 207 |
| 45 | MFI reversion · 1h | reversion | 82.01 | -17.99 | 288 | 32.3 | -15.82 | -2.47 | -19.58 | 154 |
| 46 | Williams %R · 1h | reversion | 81.72 | -18.28 | 249 | 47.8 | -33.60 | -5.92 | -34.73 | 529 |
| 47 | EMA 20/50 cross · 1h | trend | 81.56 | -18.44 | 86 | 11.6 | -21.79 | -3.91 | -24.96 | 137 |
| 48 | MACD cross · 1h | trend | 81.40 | -18.60 | 276 | 24.6 | -27.48 | -4.91 | -29.46 | 473 |
| 49 | CCI reversion · 1h | reversion | 81.26 | -18.74 | 245 | 46.5 | -21.92 | -3.09 | -28.07 | 452 |
| 50 | Bollinger reversion · 1h | reversion | 80.96 | -19.04 | 191 | 38.7 | -30.14 | -6.24 | -31.74 | 369 |
| 51 | Donchian 20/10 · 1h | breakout | 80.50 | -19.50 | 108 | 21.3 | -22.28 | -4.08 | -26.02 | 219 |
| 52 | OBV trend · 1h | momentum | 79.47 | -20.53 | 225 | 16.9 | -34.11 | -6.64 | -36.19 | 300 |
| 53 | MACD zero-line · 1h | trend | 79.10 | -20.90 | 129 | 16.3 | -23.89 | -4.78 | -26.72 | 212 |
| 54 | RSI(14) reversion · 1h | reversion | 78.20 | -21.80 | 113 | 26.5 | -21.17 | -3.88 | -24.99 | 207 |
| 55 | Candlestick reversal · 1h | reversion | 76.78 | -23.22 | 304 | 29.9 | -34.73 | -6.92 | -36.08 | 548 |
| 56 | Heikin-Ashi · 1h | trend | 76.66 | -23.34 | 331 | 23.6 | -42.38 | -9.19 | -42.43 | 668 |
| 57 | ROC + volume · 1h | momentum | 76.46 | -23.54 | 286 | 25.9 | -30.41 | -5.32 | -31.81 | 388 |
| 58 | Agent (ML meta-label) | meta | 76.13 | -23.87 | 1115 | 20.9 | -13.66 | -2.85 | -18.40 | 350 |
| 59 | EMA 9/21 cross · 1h | trend | 74.62 | -25.38 | 195 | 10.3 | -31.32 | -6.25 | -32.32 | 340 |
| 60 | Three white soldiers | momentum | 74.43 | -25.57 | 364 | 17.9 | -44.59 | -20.68 | -44.59 | 614 |
| 61 | VWAP momentum · 1h | momentum | 73.56 | -26.44 | 632 | 22.9 | -51.54 | -10.89 | -51.75 | 1239 |
| 62 | Max aggression: 1-day momentum | meta | 72.15 | -27.85 | 21 | 33.3 | -35.91 | -2.16 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -42.59 | -98.87 | 5192 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.63 | -23.12 | -78.74 | 1404 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -43.78 | -93.51 | 2531 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.47 | -29.69 | -88.55 | 1905 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.08 | -36.49 | -91.20 | 2340 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.26 | -31.01 | -90.26 | 2240 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -48.91 | -97.69 | 3495 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -55.21 | -96.12 | 3382 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.02 | -35.28 | -94.02 | 2479 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.89 | -32.87 | -81.95 | 1685 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.45 | -54.71 | -99.45 | 5780 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.82 | -41.79 | -92.88 | 2629 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -36.72 | -95.46 | 3454 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -70.93 | -99.78 | 6175 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -41.62 | -91.86 | 2298 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.21 | -27.33 | -75.24 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -60.15 | -97.68 | 3575 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.62 | -59.31 | -98.62 | 4779 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.55 | -28.19 | -70.06 | 1210 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -52.22 | -94.78 | 2795 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.70 | -37.55 | -84.78 | 1827 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -67.85 | -99.60 | 6284 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.09 | -29.68 | -88.17 | 2208 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.11 | -19.60 | -77.33 | 1678 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.62 | -37.58 | -90.63 | 2236 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.27 | -50.78 | -96.27 | 3776 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.73 | -50.91 | -89.76 | 2132 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.52 | -25.61 | -64.52 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.54 | -25.34 | -73.60 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.79 | -18.23 | -75.82 | 1558 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.68 | -50.20 | -96.68 | 4190 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -101.60 | -99.92 | 8305 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T09:05 | MACD cross · 1h | sell | DOGE-USD | 9.01 | -0.04 | target is flat |
| 2026-10-30T09:05 | Three white soldiers | buy | XRP-USD | 18.63 | — | entry signal |
| 2026-10-30T09:00 | Heikin-Ashi · 1h | sell | SOL-USD | 15.30 | -0.07 | exit signal |
| 2026-10-30T09:00 | Heikin-Ashi · 1h | sell | ETH-USD | 7.59 | -0.08 | exit signal |
| 2026-10-30T09:00 | Heikin-Ashi · 1h | sell | BTC-USD | 19.12 | -0.23 | exit signal |
| 2026-10-30T09:00 | MACD cross · 1h | buy | DOGE-USD | 9.05 | — | entry signal |
| 2026-10-30T08:30 | Three white soldiers | sell | SOL-USD | 18.50 | -0.17 | exit signal |
| 2026-10-30T08:25 | Three white soldiers | buy | SOL-USD | 18.68 | — | entry signal |
| 2026-10-30T08:00 | Three white soldiers · 1h | sell | XRP-USD | 23.59 | -0.18 | exit signal |
| 2026-10-30T08:00 | Heikin-Ashi · 1h | buy | ETH-USD | 7.67 | — | entry |
| 2026-10-30T08:00 | Heikin-Ashi · 1h | buy | BTC-USD | 7.57 | — | rebalance up |
| 2026-10-30T08:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 15.24 | -0.19 | exit signal |
| 2026-10-30T07:00 | MACD cross · 1h | buy | SOL-USD | 10.21 | — | entry signal |
| 2026-10-30T06:45 | Three white soldiers | sell | DOGE-USD | 18.58 | -0.12 | exit signal |
| 2026-10-30T06:30 | Heikin-Ashi · 1h | buy | BTC-USD | 3.89 | — | rebalance up |
| 2026-10-30T06:30 | Heikin-Ashi · 1h | sell | DOGE-USD | 3.89 | 0.00 | rebalance down |
| 2026-10-30T06:20 | Three white soldiers | buy | DOGE-USD | 18.71 | — | entry signal |
| 2026-10-30T06:00 | Heikin-Ashi · 1h | buy | BTC-USD | 7.89 | — | entry signal |
| 2026-10-30T06:00 | Heikin-Ashi · 1h | sell | SOL-USD | 3.95 | 0.01 | rebalance down |
| 2026-10-30T06:00 | MACD cross · 1h | buy | XRP-USD | 11.67 | — | entry signal |
| 2026-10-30T05:55 | Agent (ML meta-label) | buy | DOGE-USD | 8.48 | — | entry |
| 2026-10-30T05:55 | Agent (ML meta-label) | sell | ETH-USD | 8.42 | -0.07 | selected signal exited |
| 2026-10-30T05:55 | Three white soldiers | sell | XRP-USD | 15.14 | 0.18 | exit signal |
| 2026-10-30T05:46 | Agent (ML meta-label) | buy | ETH-USD | 8.49 | — | entry |
| 2026-10-30T05:46 | Agent (ML meta-label) | sell | DOGE-USD | 9.09 | -0.00 | selected signal exited |
| 2026-10-30T05:00 | Three white soldiers · 1h | buy | XRP-USD | 23.77 | — | entry signal |
| 2026-10-30T05:00 | Heikin-Ashi · 1h | buy | SOL-USD | 19.31 | — | entry signal |
| 2026-10-30T05:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.31 | — | entry signal |
| 2026-10-30T05:00 | Three white soldiers | sell | SOL-USD | 14.97 | 0.29 | exit signal |
| 2026-10-30T05:00 | Three white soldiers | sell | BTC-USD | 18.42 | -0.05 | exit signal |
| 2026-10-30T04:05 | Three white soldiers | sell | ETH-USD | 14.90 | -0.06 | exit signal |
| 2026-10-30T04:05 | Three white soldiers | sell | DOGE-USD | 11.39 | -0.11 | exit signal |
| 2026-10-30T04:00 | Agent (ML meta-label) | buy | DOGE-USD | 9.09 | — | entry |
| 2026-10-30T04:00 | Agent (ML meta-label) | sell | ETH-USD | 8.67 | -0.05 | selected signal exited |
| 2026-10-30T04:00 | CCI reversion · 1h | buy | XRP-USD | 11.99 | — | entry signal |
| 2026-10-30T04:00 | CCI reversion · 1h | buy | SOL-USD | 16.31 | — | entry signal |
| 2026-10-30T04:00 | CCI reversion · 1h | buy | DOGE-USD | 16.31 | — | entry signal |
| 2026-10-30T04:00 | CCI reversion · 1h | buy | BTC-USD | 16.31 | — | entry signal |
| 2026-10-30T04:00 | Z-score reversion · 1h | buy | DOGE-USD | 8.57 | — | entry signal |
| 2026-10-30T04:00 | Z-score reversion · 1h | buy | BTC-USD | 12.26 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 09:15:05.000144+00:00 -> 2026-10-30 09:25:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
