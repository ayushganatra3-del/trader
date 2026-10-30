# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T15:45:05.000165+00:00 · 41523 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.66 (-8.34%)

Closed trades 126, win rate 40.5%, fees £3.68, max drawdown -11.45%.

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

Today: 18300 decisions in 2241 calls, $0.2366 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T15:45 | 1 / 10 / 19 | cash |  |
| Breezy | 2026-10-30T15:45 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-30T15:45 | 3 / 21 / 6 | BITX 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.77 | +1.01% | 7 |
| VWAP reversion | SQQQ | 2.67 | +4.28% | 5 |
| Candlestick reversal | LABU | 2.56 | +7.90% | 14 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Candlestick reversal | PLTR | 2.37 | +5.05% | 17 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.11 | 7.11 | 0 | — | 8.38 | 4.04 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.67 | 3.67 | 22 | 45.5 | 7.56 | 2.46 | -4.92 | 26 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 100.49 | 0.49 | 0 | — | 3.81 | 1.66 | -5.02 | 1 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.85 | -5.89 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.74 | -2.25 | 95 | 35.8 | 6.85 | 3.23 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.36 | -2.64 | 0 | — | -1.13 | -0.56 | -3.08 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.47 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.11 | -4.72 | 20 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 96.74 | -3.26 | 0 | — | -5.05 | -2.01 | -7.83 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 15 | Agent (rotation) | meta | 95.17 | -4.83 | 129 | 31.0 | -3.20 | -2.06 | -8.19 | 164 |
| 16 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.90 | -5.10 | 0 | — | -2.65 | -1.02 | -6.39 | 1 |
| 18 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.46 | -8.76 | 203 |
| 19 | Copy: Insider buying | copy | 92.16 | -7.84 | 33 | 36.4 | -22.24 | -4.54 | -23.91 | 69 |
| 20 | Agent | meta | 91.66 | -8.34 | 126 | 40.5 | -9.28 | -5.41 | -12.21 | 222 |
| 21 | Trend pullback · 1h | trend | 91.60 | -8.40 | 100 | 22.0 | -21.15 | -7.44 | -21.21 | 99 |
| 22 | Opening range 30m | breakout | 91.48 | -8.52 | 305 | 35.4 | -11.28 | -3.36 | -17.21 | 590 |
| 23 | Hold BTC | benchmark | 91.38 | -8.62 | 0 | — | -1.17 | -0.02 | -12.47 | 1 |
| 24 | Parabolic SAR · 1h | trend | 91.26 | -8.74 | 140 | 28.6 | -18.21 | -4.16 | -20.27 | 250 |
| 25 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.62 | -16.91 | 1 |
| 26 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -7.25 | -1.99 | -12.70 | 94 |
| 27 | Donchian 55/20 · 1h | breakout | 89.86 | -10.14 | 54 | 14.8 | -16.38 | -3.64 | -17.32 | 103 |
| 28 | Daily: Bullish score | daily | 88.55 | -11.46 | 14 | 21.4 | -6.74 | -0.83 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 88.27 | -11.73 | 0 | — | -3.50 | -0.38 | -14.57 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.10 | -3.66 | -15.04 | 101 |
| 31 | Volume breakout · 1h | breakout | 85.71 | -14.29 | 127 | 29.1 | -13.33 | -2.82 | -16.25 | 105 |
| 32 | Stochastic reversion · 1h | reversion | 85.43 | -14.57 | 221 | 47.5 | -17.80 | -3.08 | -23.72 | 381 |
| 33 | ADX DI cross · 1h | trend | 84.89 | -15.11 | 141 | 19.1 | -17.65 | -3.41 | -20.33 | 261 |
| 34 | Keltner breakout · 1h | breakout | 84.88 | -15.12 | 86 | 24.4 | -24.76 | -4.90 | -25.77 | 189 |
| 35 | Connors RSI(2) · 1h | reversion | 84.12 | -15.88 | 186 | 40.9 | -20.64 | -6.58 | -21.56 | 162 |
| 36 | Opening range 15m | breakout | 83.87 | -16.13 | 379 | 31.9 | -16.26 | -4.66 | -18.52 | 721 |
| 37 | Bollinger breakout · 1h | breakout | 83.21 | -16.79 | 132 | 26.5 | -16.24 | -2.99 | -21.61 | 245 |
| 38 | Max aggression: 5-day momentum | meta | 82.71 | -17.29 | 14 | 42.9 | -35.92 | -2.60 | -36.20 | 25 |
| 39 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -24.44 | -3.44 | -26.88 | 35 |
| 40 | Ichimoku · 1h | trend | 82.11 | -17.89 | 78 | 14.1 | -20.71 | -4.13 | -24.80 | 118 |
| 41 | Supertrend · 1h | trend | 80.97 | -19.03 | 133 | 13.5 | -25.79 | -4.79 | -28.87 | 216 |
| 42 | MFI reversion · 1h | reversion | 80.64 | -19.36 | 292 | 31.8 | -18.71 | -2.96 | -20.24 | 153 |
| 43 | CCI reversion · 1h | reversion | 80.26 | -19.74 | 246 | 46.3 | -26.08 | -4.02 | -28.85 | 449 |
| 44 | EMA 20/50 cross · 1h | trend | 79.69 | -20.31 | 88 | 11.4 | -23.73 | -4.48 | -26.95 | 136 |
| 45 | MACD cross · 1h | trend | 79.33 | -20.67 | 282 | 24.1 | -30.28 | -5.38 | -32.86 | 473 |
| 46 | Williams %R · 1h | reversion | 79.11 | -20.89 | 252 | 47.2 | -35.04 | -6.18 | -35.58 | 529 |
| 47 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.33 | -4.89 | -27.15 | 214 |
| 48 | RSI momentum · 1h | momentum | 78.88 | -21.12 | 128 | 12.5 | -27.16 | -4.87 | -30.13 | 215 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -17.76 | -2.75 | -22.16 | 208 |
| 50 | Heikin-Ashi · 1h | trend | 78.30 | -21.70 | 333 | 23.7 | -41.92 | -9.09 | -42.17 | 668 |
| 51 | Triple EMA stack · 1h | trend | 78.29 | -21.71 | 117 | 13.7 | -30.63 | -5.73 | -33.05 | 208 |
| 52 | Bollinger reversion · 1h | reversion | 77.90 | -22.10 | 195 | 37.9 | -31.13 | -6.49 | -32.42 | 368 |
| 53 | OBV trend · 1h | momentum | 77.40 | -22.60 | 231 | 17.7 | -33.10 | -6.68 | -35.55 | 300 |
| 54 | ROC + volume · 1h | momentum | 75.90 | -24.09 | 291 | 25.8 | -29.54 | -5.05 | -31.91 | 384 |
| 55 | Donchian 20/10 · 1h | breakout | 75.81 | -24.20 | 114 | 21.1 | -28.01 | -4.88 | -29.81 | 220 |
| 56 | Three white soldiers | momentum | 74.19 | -25.81 | 369 | 17.6 | -44.52 | -20.62 | -44.55 | 614 |
| 57 | VWAP momentum · 1h | momentum | 73.61 | -26.39 | 638 | 22.9 | -52.17 | -11.07 | -52.78 | 1238 |
| 58 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -20.48 | -3.58 | -25.90 | 193 |
| 59 | Candlestick reversal · 1h | reversion | 73.05 | -26.95 | 309 | 29.4 | -34.79 | -6.85 | -35.12 | 549 |
| 60 | Agent (ML meta-label) | meta | 72.93 | -27.07 | 1142 | 20.9 | -13.08 | -2.09 | -19.12 | 369 |
| 61 | Max aggression: 1-day momentum | meta | 72.65 | -27.35 | 21 | 33.3 | -29.05 | -1.57 | -50.32 | 42 |
| 62 | EMA 9/21 cross · 1h | trend | 71.28 | -28.72 | 202 | 9.9 | -35.82 | -6.82 | -36.33 | 336 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -44.19 | -98.90 | 5238 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.33 | -23.71 | -79.34 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.60 | -45.11 | -93.60 | 2540 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.71 | -30.47 | -88.71 | 1919 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -37.47 | -91.19 | 2349 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.04 | -30.60 | -90.04 | 2229 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -50.46 | -97.71 | 3511 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.14 | -57.00 | -96.14 | 3388 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.11 | -35.68 | -94.11 | 2479 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.81 | -32.58 | -81.89 | 1682 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -54.56 | -99.47 | 5839 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.99 | -43.75 | -92.99 | 2635 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.44 | -37.05 | -95.44 | 3454 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.23 | -99.78 | 6205 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.90 | -43.16 | -91.90 | 2307 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.88 | -27.80 | -75.88 | 1583 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -60.19 | -97.68 | 3570 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -60.02 | -98.67 | 4816 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.35 | -28.69 | -69.52 | 1212 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.80 | -54.19 | -94.80 | 2797 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.90 | -38.71 | -84.90 | 1821 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -69.03 | -99.61 | 6317 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.21 | -29.91 | -88.23 | 2239 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.32 | -19.66 | -77.32 | 1706 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.85 | -37.58 | -90.85 | 2270 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.35 | -50.82 | -96.35 | 3808 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.00 | -53.53 | -90.00 | 2148 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.99 | -25.87 | -64.99 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.08 | -25.62 | -74.08 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.90 | -18.37 | -75.90 | 1563 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.75 | -50.46 | -96.75 | 4219 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.58 | -99.92 | 8317 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T15:45 | Three white soldiers | sell | GOOGL | 18.56 | -0.02 | exit signal |
| 2026-10-30T15:40 | Opening range 30m | buy | SQQQ | 1.95 | — | entry signal |
| 2026-10-30T15:35 | Agent | sell | PLTR | 18.12 | -0.26 | selected signal exited |
| 2026-10-30T15:30 | Agent (ML meta-label) | buy | MSTR | 1.89 | — | entry |
| 2026-10-30T15:30 | Agent (ML meta-label) | buy | ETHU | 10.80 | — | entry |
| 2026-10-30T15:30 | Agent (ML meta-label) | sell | LABU | 12.69 | -0.03 | selected signal exited |
| 2026-10-30T15:30 | MFI reversion · 1h | buy | AMZN | 20.16 | — | entry signal |
| 2026-10-30T15:30 | Williams %R · 1h | buy | LABU | 12.33 | — | entry signal |
| 2026-10-30T15:30 | Williams %R · 1h | sell | MSFT | 4.27 | -0.04 | rebalance down |
| 2026-10-30T15:30 | Williams %R · 1h | sell | ETH-USD | 4.04 | 0.00 | rebalance down |
| 2026-10-30T15:30 | Williams %R · 1h | sell | BTC-USD | 4.02 | -0.00 | rebalance down |
| 2026-10-30T15:30 | Bollinger reversion · 1h | buy | TSLA | 9.71 | — | entry signal |
| 2026-10-30T15:30 | Bollinger reversion · 1h | buy | MSFT | 9.78 | — | entry signal |
| 2026-10-30T15:30 | Bollinger reversion · 1h | buy | AMZN | 9.78 | — | entry signal |
| 2026-10-30T15:30 | Bollinger reversion · 1h | sell | SOL-USD | 5.63 | -0.08 | rebalance down |
| 2026-10-30T15:30 | Bollinger reversion · 1h | sell | GOOGL | 5.96 | 0.01 | rebalance down |
| 2026-10-30T15:30 | Bollinger reversion · 1h | sell | ETH-USD | 5.90 | 0.01 | rebalance down |
| 2026-10-30T15:30 | Bollinger reversion · 1h | sell | DOGE-USD | 5.90 | 0.01 | rebalance down |
| 2026-10-30T15:30 | Bollinger reversion · 1h | sell | BTC-USD | 5.88 | -0.00 | rebalance down |
| 2026-10-30T15:30 | Candlestick reversal · 1h | buy | MSTR | 12.17 | — | entry signal |
| 2026-10-30T15:30 | Candlestick reversal · 1h | buy | ETHU | 12.25 | — | entry signal |
| 2026-10-30T15:30 | Candlestick reversal · 1h | sell | XRP-USD | 5.98 | 0.01 | rebalance down |
| 2026-10-30T15:30 | Candlestick reversal · 1h | sell | ETH-USD | 6.18 | 0.01 | rebalance down |
| 2026-10-30T15:30 | Candlestick reversal · 1h | sell | DOGE-USD | 6.18 | 0.01 | rebalance down |
| 2026-10-30T15:30 | Candlestick reversal · 1h | sell | BTC-USD | 6.08 | -0.01 | rebalance down |
| 2026-10-30T15:30 | OBV trend · 1h | sell | TNA | 19.20 | -0.23 | exit signal |
| 2026-10-30T15:30 | RSI momentum · 1h | buy | SQQQ | 12.02 | — | rebalance up |
| 2026-10-30T15:30 | RSI momentum · 1h | buy | IWM | 4.04 | — | rebalance up |
| 2026-10-30T15:30 | RSI momentum · 1h | sell | TNA | 19.57 | -0.52 | exit signal |
| 2026-10-30T15:30 | VWAP momentum · 1h | buy | GOOGL | 11.33 | — | entry signal |
| 2026-10-30T15:30 | VWAP momentum · 1h | sell | XRP-USD | 3.74 | 0.01 | rebalance down |
| 2026-10-30T15:30 | VWAP momentum · 1h | sell | ETH-USD | 3.78 | -0.00 | rebalance down |
| 2026-10-30T15:30 | VWAP momentum · 1h | sell | DOGE-USD | 3.80 | -0.01 | rebalance down |
| 2026-10-30T15:30 | Trend pullback · 1h | buy | AAPL | 22.91 | — | entry signal |
| 2026-10-30T15:30 | Heikin-Ashi · 1h | buy | SQQQ | 19.55 | — | entry signal |
| 2026-10-30T15:30 | Ichimoku · 1h | buy | SQQQ | 20.58 | — | entry signal |
| 2026-10-30T15:30 | Parabolic SAR · 1h | sell | LABU | 23.04 | 0.31 | exit signal |
| 2026-10-30T15:20 | Day trade: Stocks in Play ORB | buy | AMD | 24.50 | — | entry |
| 2026-10-30T15:20 | Agent (ML meta-label) | buy | SOL-USD | 9.51 | — | entry |
| 2026-10-30T15:20 | Agent (ML meta-label) | buy | META | 12.81 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 15:45:05.000165+00:00 -> 2026-10-30 15:55:05.000165+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
