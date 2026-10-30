# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T04:15:05.000155+00:00 · 40980 ticks

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

Today: 3060 decisions in 612 calls, $0.0429 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T04:15 | 2 / 3 / 0 | XRP-USD 19% |  |
| Breezy | 2026-10-30T04:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-30T04:15 | 4 / 1 / 0 | ETH-USD 59% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 106.21 | 6.21 | 0 | — | 7.59 | 3.72 | -5.18 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.23 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.02 | 1.02 | 0 | — | 4.35 | 1.89 | -5.02 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Hold SPY | benchmark | 98.92 | -1.08 | 0 | — | 0.56 | 0.37 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 6.78 | 3.18 | -1.98 | 91 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.74 | -2.52 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -5.09 | -5.81 | -5.22 | 22 |
| 13 | Copy: Congress Democrats (NANC) | copy | 97.01 | -2.99 | 0 | — | -0.48 | -0.15 | -5.99 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.74 | -3.26 | 0 | — | -5.05 | -2.01 | -7.83 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -3.20 | -2.06 | -7.40 | 174 |
| 17 | Three white soldiers · 1h | momentum | 95.09 | -4.91 | 16 | 12.5 | -2.55 | -2.33 | -4.76 | 27 |
| 18 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 5.27 | 1.72 | -8.76 | 204 |
| 19 | Copy: Cathie Wood (ARKK) | copy | 93.41 | -6.58 | 0 | — | 2.42 | 0.57 | -14.57 | 1 |
| 20 | Copy: Insider buying | copy | 92.63 | -7.37 | 33 | 36.4 | -20.02 | -3.94 | -24.43 | 67 |
| 21 | Donchian 55/20 · 1h | breakout | 92.26 | -7.74 | 54 | 14.8 | -13.77 | -3.09 | -15.51 | 102 |
| 22 | Hold BTC | benchmark | 92.16 | -7.84 | 0 | — | 0.09 | 0.19 | -12.47 | 1 |
| 23 | Daily: Momentum burst | daily | 91.94 | -8.06 | 15 | 13.3 | -12.93 | -2.42 | -17.57 | 35 |
| 24 | Opening range 30m | breakout | 91.77 | -8.23 | 304 | 35.5 | -11.10 | -3.30 | -17.21 | 580 |
| 25 | Agent | meta | 91.68 | -8.32 | 122 | 40.2 | -9.57 | -5.72 | -12.21 | 221 |
| 26 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.20 | -7.35 | -21.50 | 99 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.75 | -2.67 | -16.91 | 1 |
| 28 | Squeeze breakout · 1h | breakout | 90.60 | -9.40 | 56 | 23.2 | -4.98 | -1.35 | -12.65 | 93 |
| 29 | Daily: Bullish score | daily | 90.46 | -9.54 | 12 | 25.0 | -5.76 | -0.69 | -14.40 | 14 |
| 30 | Parabolic SAR · 1h | trend | 90.03 | -9.97 | 137 | 28.5 | -19.98 | -4.64 | -20.21 | 248 |
| 31 | ADX DI cross · 1h | trend | 89.43 | -10.57 | 137 | 19.7 | -15.07 | -3.02 | -16.59 | 260 |
| 32 | Stochastic reversion · 1h | reversion | 87.88 | -12.12 | 218 | 48.2 | -15.90 | -2.75 | -22.69 | 381 |
| 33 | Max aggression: 5-day momentum | meta | 87.67 | -12.33 | 14 | 42.9 | -14.69 | -1.27 | -27.23 | 25 |
| 34 | Agent (aggressive) | meta | 87.41 | -12.59 | 62 | 35.5 | -11.10 | -3.66 | -15.04 | 101 |
| 35 | Volume breakout · 1h | breakout | 86.58 | -13.41 | 124 | 29.8 | -14.59 | -3.11 | -17.32 | 106 |
| 36 | Bollinger breakout · 1h | breakout | 85.95 | -14.05 | 128 | 26.6 | -12.29 | -2.22 | -19.10 | 244 |
| 37 | Z-score reversion · 1h | reversion | 85.74 | -14.26 | 126 | 35.7 | -13.64 | -2.12 | -21.48 | 206 |
| 38 | Keltner breakout · 1h | breakout | 85.34 | -14.66 | 84 | 23.8 | -22.93 | -4.63 | -23.96 | 196 |
| 39 | Ichimoku · 1h | trend | 84.44 | -15.56 | 75 | 10.7 | -18.75 | -3.76 | -24.73 | 118 |
| 40 | Opening range 15m | breakout | 84.37 | -15.63 | 376 | 32.2 | -16.00 | -4.59 | -18.10 | 709 |
| 41 | Connors RSI(2) · 1h | reversion | 84.20 | -15.80 | 185 | 40.5 | -21.05 | -6.72 | -21.83 | 163 |
| 42 | Supertrend · 1h | trend | 83.73 | -16.27 | 126 | 14.3 | -23.64 | -4.52 | -26.18 | 218 |
| 43 | RSI momentum · 1h | momentum | 83.30 | -16.70 | 122 | 13.1 | -20.37 | -4.04 | -23.98 | 214 |
| 44 | Triple EMA stack · 1h | trend | 82.46 | -17.54 | 113 | 14.2 | -27.74 | -5.35 | -30.37 | 208 |
| 45 | MFI reversion · 1h | reversion | 82.07 | -17.93 | 288 | 32.3 | -17.76 | -2.81 | -19.58 | 152 |
| 46 | Williams %R · 1h | reversion | 81.78 | -18.22 | 249 | 47.8 | -33.51 | -5.90 | -34.73 | 529 |
| 47 | MACD cross · 1h | trend | 81.64 | -18.36 | 275 | 24.7 | -27.33 | -4.87 | -29.24 | 471 |
| 48 | EMA 20/50 cross · 1h | trend | 81.59 | -18.41 | 86 | 11.6 | -21.93 | -3.94 | -24.96 | 137 |
| 49 | CCI reversion · 1h | reversion | 81.46 | -18.54 | 245 | 46.5 | -21.66 | -3.05 | -28.07 | 451 |
| 50 | Bollinger reversion · 1h | reversion | 81.02 | -18.98 | 191 | 38.7 | -29.98 | -6.20 | -31.74 | 369 |
| 51 | Donchian 20/10 · 1h | breakout | 80.55 | -19.45 | 108 | 21.3 | -22.33 | -4.09 | -26.02 | 219 |
| 52 | OBV trend · 1h | momentum | 79.51 | -20.49 | 225 | 16.9 | -34.08 | -6.63 | -36.19 | 300 |
| 53 | MACD zero-line · 1h | trend | 79.11 | -20.89 | 129 | 16.3 | -24.19 | -4.85 | -26.72 | 213 |
| 54 | RSI(14) reversion · 1h | reversion | 78.36 | -21.64 | 113 | 26.5 | -21.05 | -3.85 | -24.99 | 207 |
| 55 | Heikin-Ashi · 1h | trend | 77.23 | -22.77 | 327 | 23.9 | -42.02 | -9.08 | -42.36 | 665 |
| 56 | Candlestick reversal · 1h | reversion | 76.83 | -23.17 | 304 | 29.9 | -34.56 | -6.86 | -36.03 | 548 |
| 57 | ROC + volume · 1h | momentum | 76.51 | -23.49 | 286 | 25.9 | -30.59 | -5.36 | -32.03 | 388 |
| 58 | Agent (ML meta-label) | meta | 76.35 | -23.66 | 1113 | 20.9 | -13.09 | -2.57 | -17.98 | 341 |
| 59 | Three white soldiers | momentum | 74.88 | -25.12 | 359 | 17.5 | -44.30 | -20.27 | -44.59 | 612 |
| 60 | EMA 9/21 cross · 1h | trend | 74.66 | -25.34 | 195 | 10.3 | -31.47 | -6.28 | -32.26 | 341 |
| 61 | VWAP momentum · 1h | momentum | 73.74 | -26.25 | 632 | 22.9 | -51.56 | -10.89 | -51.76 | 1239 |
| 62 | Max aggression: 1-day momentum | meta | 72.15 | -27.85 | 21 | 33.3 | -35.91 | -2.16 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.86 | -42.79 | -98.88 | 5192 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.71 | -23.22 | -78.79 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -43.86 | -93.54 | 2535 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.52 | -29.62 | -88.66 | 1912 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.13 | -36.65 | -91.23 | 2343 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.50 | -31.63 | -90.50 | 2254 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -49.47 | -97.73 | 3505 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -55.60 | -96.14 | 3390 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.96 | -34.88 | -93.97 | 2466 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.01 | -33.20 | -82.01 | 1688 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.45 | -55.06 | -99.45 | 5779 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.82 | -41.27 | -92.94 | 2630 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.54 | -37.02 | -95.54 | 3469 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -69.79 | -99.78 | 6181 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -42.10 | -91.95 | 2304 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.00 | -26.88 | -75.09 | 1564 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -59.13 | -97.68 | 3573 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.62 | -59.06 | -98.63 | 4783 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.57 | -28.15 | -70.06 | 1210 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -51.63 | -94.80 | 2795 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.74 | -37.68 | -84.81 | 1828 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -67.86 | -99.60 | 6288 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.04 | -29.57 | -88.18 | 2206 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.27 | -19.79 | -77.51 | 1682 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -37.39 | -90.68 | 2236 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -50.85 | -96.27 | 3777 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.79 | -50.87 | -89.91 | 2136 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.46 | -25.51 | -64.46 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.49 | -25.21 | -73.51 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.81 | -18.26 | -75.85 | 1561 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.68 | -50.29 | -96.69 | 4191 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.34 | -99.92 | 8298 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-30T04:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.33 | — | entry signal |
| 2026-10-30T04:00 | VWAP momentum · 1h | buy | BTC-USD | 14.76 | — | entry signal |
| 2026-10-30T03:55 | Agent (ML meta-label) | buy | ETH-USD | 8.72 | — | entry |
| 2026-10-30T03:55 | Agent (ML meta-label) | sell | DOGE-USD | 8.46 | -0.03 | selected signal exited |
| 2026-10-30T03:47 | Three white soldiers | buy | DOGE-USD | 3.73 | — | rebalance up |
| 2026-10-30T03:47 | Three white soldiers | sell | ETH-USD | 3.73 | -0.01 | rebalance down |
| 2026-10-30T03:45 | Three white soldiers | buy | DOGE-USD | 7.76 | — | entry signal |
| 2026-10-30T03:45 | Three white soldiers | sell | XRP-USD | 3.74 | -0.01 | rebalance down |
| 2026-10-30T03:45 | Three white soldiers | sell | SOL-USD | 4.02 | 0.07 | rebalance down |
| 2026-10-30T03:40 | Agent (ML meta-label) | buy | DOGE-USD | 8.49 | — | entry |
| 2026-10-30T03:40 | Three white soldiers | buy | BTC-USD | 18.47 | — | entry signal |
| 2026-10-30T03:36 | Three white soldiers | buy | XRP-USD | 18.71 | — | entry signal |
| 2026-10-30T03:36 | Three white soldiers | buy | ETH-USD | 18.71 | — | entry signal |
| 2026-10-30T03:25 | Agent (ML meta-label) | sell | DOGE-USD | 9.17 | 0.16 | selected signal exited |
| 2026-10-30T03:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 5.81 | — | entry signal |
| 2026-10-30T03:00 | RSI(14) reversion · 1h | buy | BTC-USD | 13.04 | — | entry signal |
| 2026-10-30T02:20 | Three white soldiers | buy | SOL-USD | 18.63 | — | entry signal |
| 2026-10-30T02:05 | Agent (ML meta-label) | buy | DOGE-USD | 9.02 | — | entry |
| 2026-10-30T02:00 | Agent (ML meta-label) | sell | DOGE-USD | 9.02 | -0.03 | selected signal exited |
| 2026-10-30T01:25 | Agent (ML meta-label) | buy | DOGE-USD | 9.04 | — | entry |
| 2026-10-30T01:20 | Agent (ML meta-label) | sell | DOGE-USD | 9.04 | -0.06 | selected signal exited |
| 2026-10-30T01:05 | Agent (ML meta-label) | buy | DOGE-USD | 9.11 | — | entry |
| 2026-10-30T01:05 | Agent (ML meta-label) | sell | SOL-USD | 9.11 | -0.09 | selected signal exited |
| 2026-10-30T01:00 | Agent (ML meta-label) | buy | SOL-USD | 9.20 | — | entry |
| 2026-10-30T00:30 | Agent (ML meta-label) | sell | XRP-USD | 9.20 | -0.12 | selected signal exited |
| 2026-10-30T00:25 | Agent (ML meta-label) | buy | XRP-USD | 9.32 | — | entry |
| 2026-10-30T00:25 | VWAP reversion · 1h | sell | XRP-USD | 24.38 | -0.90 | stop-loss |
| 2026-10-30T00:25 | RSI(14) reversion · 1h | sell | XRP-USD | 6.26 | -0.08 | stop-loss |
| 2026-10-30T00:25 | RSI(14) reversion · 1h | sell | DOGE-USD | 12.59 | -0.62 | stop-loss |
| 2026-10-30T00:20 | VWAP reversion · 1h | sell | BTC-USD | 24.60 | -0.68 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 04:15:05.000155+00:00 -> 2026-10-30 04:25:05.000155+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
