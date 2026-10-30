# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T21:25:05.000124+00:00 · 41772 ticks

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

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 29.90 · VIX 20.80 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, TSLA 6.7, LABU 4.9, AAPL 4.7, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 34203 decisions in 2988 calls, $0.4258 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T21:25 | 3 / 2 / 0 | SOL-USD 15% |  |
| Breezy | 2026-10-30T21:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-30T21:25 | 5 / 0 / 0 | ETH-USD 68% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.46 | 6.46 | 0 | — | 7.73 | 3.81 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.60 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.65 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.87 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.90 | -0.10 | 95 | 45.3 | -12.25 | -3.43 | -12.61 | 143 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.81 | -0.19 | 0 | — | 3.11 | 1.36 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.50 | 3.08 | -2.21 | 94 |
| 10 | Hold SPY | benchmark | 97.14 | -2.86 | 0 | — | -1.35 | -0.67 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.49 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.61 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.95 | -5.05 | 129 | 31.0 | -3.02 | -1.93 | -8.60 | 151 |
| 15 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.52 | -4.94 | 28 |
| 16 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.48 | -8.76 | 203 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.60 | -5.40 | 0 | — | -7.15 | -2.76 | -8.12 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.01 | -5.99 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -9.76 | -5.72 | -12.21 | 226 |
| 20 | Parabolic SAR · 1h | trend | 91.48 | -8.52 | 140 | 28.6 | -18.02 | -4.12 | -20.27 | 250 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -20.65 | -7.55 | -20.66 | 97 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.64 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -3.68 | -17.21 | 591 |
| 24 | Hold BTC | benchmark | 90.70 | -9.30 | 0 | — | -2.06 | -0.14 | -12.65 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -6.03 | -1.66 | -12.70 | 88 |
| 26 | Copy: Insider buying | copy | 89.69 | -10.31 | 34 | 35.3 | -23.46 | -4.82 | -23.91 | 69 |
| 27 | Donchian 55/20 · 1h | breakout | 89.31 | -10.69 | 57 | 14.0 | -16.81 | -3.73 | -17.83 | 103 |
| 28 | Daily: Bullish score | daily | 88.56 | -11.44 | 14 | 21.4 | -6.72 | -0.84 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) ⏸ | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.44 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.10 | -3.69 | -15.04 | 101 |
| 31 | Volume breakout · 1h | breakout | 85.92 | -14.09 | 127 | 29.1 | -12.57 | -2.66 | -16.25 | 102 |
| 32 | Stochastic reversion · 1h | reversion | 85.38 | -14.62 | 221 | 47.5 | -17.93 | -3.13 | -24.77 | 395 |
| 33 | ADX DI cross · 1h | trend | 85.08 | -14.92 | 141 | 19.1 | -16.81 | -3.28 | -20.33 | 260 |
| 34 | Keltner breakout · 1h | breakout | 85.08 | -14.92 | 86 | 24.4 | -24.20 | -4.81 | -25.77 | 185 |
| 35 | Bollinger breakout · 1h | breakout | 83.40 | -16.59 | 132 | 26.5 | -16.37 | -3.05 | -21.61 | 241 |
| 36 | Connors RSI(2) · 1h | reversion | 83.37 | -16.63 | 188 | 40.4 | -21.38 | -6.88 | -22.04 | 161 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -4.98 | -19.33 | 723 |
| 38 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -24.65 | -3.47 | -30.48 | 35 |
| 39 | MFI reversion · 1h | reversion | 82.33 | -17.67 | 295 | 31.9 | -17.67 | -2.82 | -20.55 | 157 |
| 40 | Max aggression: 5-day momentum ⏸ | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.61 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.07 | -17.93 | 79 | 13.9 | -20.76 | -4.17 | -24.80 | 118 |
| 42 | Supertrend · 1h | trend | 80.36 | -19.64 | 137 | 13.1 | -26.47 | -4.89 | -29.25 | 216 |
| 43 | CCI reversion · 1h | reversion | 80.19 | -19.81 | 248 | 46.0 | -26.26 | -4.09 | -28.85 | 451 |
| 44 | EMA 20/50 cross · 1h | trend | 80.07 | -19.93 | 88 | 11.4 | -22.94 | -4.34 | -26.95 | 135 |
| 45 | MACD cross · 1h | trend | 79.31 | -20.69 | 283 | 24.0 | -30.39 | -5.44 | -32.86 | 475 |
| 46 | Williams %R · 1h | reversion | 79.22 | -20.78 | 253 | 47.0 | -35.09 | -6.25 | -36.14 | 528 |
| 47 | RSI momentum · 1h | momentum | 79.09 | -20.91 | 130 | 13.1 | -27.01 | -4.91 | -30.14 | 215 |
| 48 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -23.99 | -4.85 | -27.15 | 213 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -17.75 | -2.77 | -22.55 | 213 |
| 50 | Heikin-Ashi · 1h | trend | 78.49 | -21.51 | 333 | 23.7 | -41.79 | -9.14 | -42.17 | 668 |
| 51 | Triple EMA stack · 1h | trend | 78.03 | -21.97 | 120 | 15.0 | -30.80 | -5.76 | -33.28 | 208 |
| 52 | Bollinger reversion · 1h | reversion | 78.01 | -21.99 | 197 | 38.1 | -31.12 | -6.55 | -33.01 | 381 |
| 53 | OBV trend · 1h | momentum | 77.89 | -22.11 | 232 | 17.7 | -33.90 | -6.83 | -36.79 | 299 |
| 54 | Donchian 20/10 · 1h | breakout | 76.04 | -23.96 | 116 | 20.7 | -26.43 | -4.64 | -29.81 | 215 |
| 55 | ROC + volume · 1h | momentum | 75.62 | -24.38 | 293 | 25.6 | -29.86 | -5.18 | -31.91 | 384 |
| 56 | Three white soldiers | momentum | 74.00 | -26.00 | 371 | 17.5 | -44.62 | -21.07 | -44.62 | 615 |
| 57 | VWAP momentum · 1h | momentum | 73.63 | -26.37 | 643 | 22.7 | -52.95 | -11.23 | -54.00 | 1235 |
| 58 | Max aggression: 1-day momentum | meta | 73.34 | -26.66 | 21 | 33.3 | -28.37 | -1.52 | -50.32 | 42 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -20.69 | -3.64 | -26.17 | 194 |
| 60 | Candlestick reversal · 1h ⏸ | reversion | 72.04 | -27.96 | 320 | 28.4 | -35.79 | -7.04 | -36.85 | 556 |
| 61 | Agent (ML meta-label) ⏸ | meta | 71.93 | -28.07 | 1173 | 21.1 | -16.06 | -3.01 | -18.32 | 350 |
| 62 | EMA 9/21 cross · 1h | trend | 71.15 | -28.85 | 205 | 10.2 | -35.11 | -6.67 | -36.61 | 333 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -45.17 | -98.87 | 5243 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.36 | -23.98 | -79.40 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.57 | -46.51 | -93.59 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.62 | -31.11 | -88.78 | 1932 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.11 | -38.66 | -91.14 | 2347 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.04 | -31.57 | -90.04 | 2224 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -54.60 | -97.75 | 3528 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.11 | -60.35 | -96.12 | 3373 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.87 | -35.48 | -93.90 | 2452 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.74 | -33.31 | -81.91 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -57.13 | -99.48 | 5931 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.95 | -45.03 | -92.99 | 2640 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -38.65 | -95.46 | 3457 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -82.38 | -99.78 | 6252 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.98 | -46.14 | -91.99 | 2314 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.71 | -28.10 | -75.71 | 1579 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -63.88 | -97.64 | 3568 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.67 | -63.44 | -98.69 | 4865 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.05 | -28.74 | -69.29 | 1213 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -56.82 | -94.77 | 2803 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.70 | -38.94 | -84.82 | 1820 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -73.80 | -99.62 | 6380 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.28 | -30.83 | -88.41 | 2260 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.77 | -20.05 | -78.08 | 1745 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.87 | -38.63 | -91.00 | 2282 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.39 | -52.29 | -96.42 | 3844 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.98 | -55.44 | -90.09 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.52 | -26.12 | -64.72 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.90 | -26.01 | -73.98 | 1277 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.26 | -18.88 | -76.78 | 1596 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.81 | -52.23 | -96.81 | 4267 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -111.76 | -99.92 | 8341 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T21:00 | CCI reversion · 1h | buy | SOL-USD | 2.51 | — | entry |
| 2026-10-30T21:00 | CCI reversion · 1h | buy | BTC-USD | 11.46 | — | entry signal |
| 2026-10-30T21:00 | CCI reversion · 1h | sell | XRP-USD | 4.63 | -0.01 | rebalance down |
| 2026-10-30T21:00 | CCI reversion · 1h | sell | ETH-USD | 4.66 | 0.00 | rebalance down |
| 2026-10-30T21:00 | CCI reversion · 1h | sell | DOGE-USD | 4.67 | -0.06 | rebalance down |
| 2026-10-30T21:00 | MACD cross · 1h | buy | BTC-USD | 15.60 | — | entry signal |
| 2026-10-30T21:00 | MACD cross · 1h | sell | XRP-USD | 4.10 | -0.02 | rebalance down |
| 2026-10-30T21:00 | MACD cross · 1h | sell | ETH-USD | 4.01 | -0.01 | rebalance down |
| 2026-10-30T21:00 | MACD cross · 1h | sell | DOGE-USD | 4.09 | -0.02 | rebalance down |
| 2026-10-30T20:39 | VWAP momentum · 1h | buy | ETH-USD | 3.67 | — | rebalance up |
| 2026-10-30T20:25 | Three white soldiers | sell | DOGE-USD | 18.42 | -0.11 | exit signal |
| 2026-10-30T20:00 | Williams %R · 1h | buy | BTC-USD | 10.60 | — | entry signal |
| 2026-10-30T20:00 | Williams %R · 1h | sell | ETH-USD | 4.56 | 0.00 | rebalance down |
| 2026-10-30T19:55 | Day trade: Stocks in Play ORB | sell | AMZN | 24.83 | 0.37 | target is flat |
| 2026-10-30T19:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 104.15 | 0.48 | target is flat |
| 2026-10-30T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 95.53 | -1.51 | target is flat |
| 2026-10-30T19:55 | Opening range 30m | sell | TSLA | 18.35 | 0.10 | end-of-day flatten |
| 2026-10-30T19:55 | Opening range 30m | sell | SQQQ | 22.52 | -0.01 | end-of-day flatten |
| 2026-10-30T19:55 | Opening range 30m | sell | ETHU | 22.94 | 0.08 | end-of-day flatten |
| 2026-10-30T19:55 | Opening range 15m | sell | TSLA | 16.79 | 0.18 | end-of-day flatten |
| 2026-10-30T19:55 | Opening range 15m | sell | SQQQ | 20.61 | -0.03 | end-of-day flatten |
| 2026-10-30T19:55 | Opening range 15m | sell | AMZN | 20.97 | 0.13 | end-of-day flatten |
| 2026-10-30T19:50 | MFI reversion · 1h | buy | GOOGL | 4.20 | — | rebalance up |
| 2026-10-30T19:50 | MFI reversion · 1h | sell | SOXL | 4.20 | 0.05 | rebalance down |
| 2026-10-30T19:50 | VWAP momentum · 1h | sell | ETH-USD | 3.67 | -0.00 | rebalance down |
| 2026-10-30T19:50 | Three white soldiers | buy | DOGE-USD | 18.53 | — | entry signal |
| 2026-10-30T19:50 | Opening range 30m | buy | SQQQ | 4.57 | — | rebalance up |
| 2026-10-30T19:50 | Opening range 15m | buy | SQQQ | 4.19 | — | rebalance up |
| 2026-10-30T19:40 | MFI reversion · 1h | buy | GOOGL | 4.39 | — | entry |
| 2026-10-30T19:40 | MFI reversion · 1h | sell | COIN | 4.33 | 0.09 | rebalance down |
| 2026-10-30T19:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 97.03 | — | entry |
| 2026-10-30T19:30 | MFI reversion · 1h | buy | SOXL | 20.26 | — | entry signal |
| 2026-10-30T19:30 | CCI reversion · 1h | buy | AMZN | 15.73 | — | entry signal |
| 2026-10-30T19:30 | CCI reversion · 1h | sell | TSLA | 4.06 | 0.02 | rebalance down |
| 2026-10-30T19:30 | Stochastic reversion · 1h | buy | UPRO | 4.39 | — | entry signal |
| 2026-10-30T19:30 | Stochastic reversion · 1h | buy | TQQQ | 4.45 | — | entry signal |
| 2026-10-30T19:30 | Stochastic reversion · 1h | buy | TNA | 4.45 | — | entry signal |
| 2026-10-30T19:30 | Stochastic reversion · 1h | buy | TECL | 4.45 | — | entry signal |
| 2026-10-30T19:30 | Stochastic reversion · 1h | buy | SPY | 4.45 | — | entry signal |
| 2026-10-30T19:30 | Stochastic reversion · 1h | buy | QQQ | 4.45 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 21:25:05.000124+00:00 -> 2026-10-30 21:35:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
