# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T16:15:05.000170+00:00 · 41542 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.72 (-8.29%)

Closed trades 126, win rate 40.5%, fees £3.70, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 18.34 | +0.00 |
| PLTR | 18.39 | +0.05 |

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

Today: 20004 decisions in 2298 calls, $0.2566 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T16:15 | 4 / 14 / 12 | MSTR 14% |  |
| Breezy | 2026-10-30T16:15 | 0 / 22 / 8 | cash |  |
| Boozy | 2026-10-30T16:15 | 5 / 20 / 5 | MSTR 74% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.19 | 7.19 | 0 | — | 8.46 | 4.07 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.67 | 3.67 | 22 | 45.5 | 7.56 | 2.46 | -4.92 | 26 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 100.41 | 0.41 | 0 | — | 3.72 | 1.62 | -5.02 | 1 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.85 | -5.89 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.53 | -2.47 | 96 | 35.4 | 6.62 | 3.12 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.31 | -2.69 | 0 | — | -1.18 | -0.58 | -3.13 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.47 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.11 | -4.72 | 20 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 14 | Agent (rotation) | meta | 95.14 | -4.86 | 129 | 31.0 | -1.68 | -1.00 | -8.29 | 167 |
| 15 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 16 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.46 | -8.76 | 203 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.63 | -5.37 | 0 | — | -7.12 | -2.73 | -7.83 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.54 | -5.46 | 0 | — | -3.01 | -1.15 | -6.54 | 1 |
| 19 | Copy: Insider buying | copy | 92.23 | -7.77 | 33 | 36.4 | -22.15 | -4.52 | -23.91 | 69 |
| 20 | Agent | meta | 91.72 | -8.29 | 126 | 40.5 | -9.32 | -5.43 | -12.21 | 224 |
| 21 | Trend pullback · 1h | trend | 91.58 | -8.41 | 100 | 22.0 | -20.94 | -7.45 | -20.99 | 98 |
| 22 | Opening range 30m | breakout | 91.52 | -8.48 | 307 | 35.2 | -11.28 | -3.36 | -17.21 | 590 |
| 23 | Hold BTC | benchmark | 91.50 | -8.50 | 0 | — | -1.10 | -0.01 | -12.47 | 1 |
| 24 | Parabolic SAR · 1h | trend | 91.34 | -8.66 | 140 | 28.6 | -18.14 | -4.13 | -20.27 | 250 |
| 25 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.62 | -16.91 | 1 |
| 26 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -7.59 | -2.08 | -12.70 | 94 |
| 27 | Donchian 55/20 · 1h | breakout | 89.78 | -10.22 | 54 | 14.8 | -16.44 | -3.65 | -17.39 | 103 |
| 28 | Daily: Bullish score | daily | 88.54 | -11.46 | 14 | 21.4 | -6.74 | -0.83 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) ⏸ | copy | 87.72 | -12.28 | 1 | 0.0 | -4.05 | -0.46 | -14.74 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.10 | -3.66 | -15.04 | 101 |
| 31 | Volume breakout · 1h | breakout | 85.79 | -14.21 | 127 | 29.1 | -13.25 | -2.80 | -16.25 | 105 |
| 32 | Stochastic reversion · 1h | reversion | 85.63 | -14.37 | 221 | 47.5 | -17.60 | -3.05 | -23.72 | 381 |
| 33 | ADX DI cross · 1h | trend | 84.96 | -15.04 | 141 | 19.1 | -16.94 | -3.27 | -20.33 | 260 |
| 34 | Keltner breakout · 1h | breakout | 84.95 | -15.05 | 86 | 24.4 | -24.76 | -4.89 | -25.77 | 189 |
| 35 | Connors RSI(2) · 1h | reversion | 84.08 | -15.91 | 186 | 40.9 | -20.68 | -6.60 | -21.56 | 162 |
| 36 | Opening range 15m | breakout | 83.92 | -16.08 | 381 | 31.8 | -16.22 | -4.65 | -18.52 | 721 |
| 37 | Bollinger breakout · 1h | breakout | 83.28 | -16.72 | 132 | 26.5 | -16.19 | -2.98 | -21.61 | 245 |
| 38 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -25.27 | -3.44 | -27.68 | 35 |
| 39 | Max aggression: 5-day momentum ⏸ | meta | 82.08 | -17.92 | 15 | 40.0 | -36.33 | -2.60 | -36.37 | 25 |
| 40 | Ichimoku · 1h | trend | 82.05 | -17.95 | 78 | 14.1 | -20.77 | -4.14 | -24.80 | 118 |
| 41 | Supertrend · 1h | trend | 80.84 | -19.16 | 133 | 13.5 | -25.91 | -4.80 | -28.87 | 216 |
| 42 | MFI reversion · 1h | reversion | 80.55 | -19.45 | 293 | 31.7 | -18.78 | -2.97 | -20.24 | 153 |
| 43 | CCI reversion · 1h | reversion | 80.53 | -19.47 | 246 | 46.3 | -25.90 | -3.99 | -28.85 | 448 |
| 44 | EMA 20/50 cross · 1h | trend | 79.64 | -20.36 | 88 | 11.4 | -23.80 | -4.49 | -26.95 | 136 |
| 45 | MACD cross · 1h | trend | 79.49 | -20.51 | 282 | 24.1 | -30.17 | -5.37 | -32.86 | 474 |
| 46 | Williams %R · 1h | reversion | 79.22 | -20.78 | 252 | 47.2 | -34.99 | -6.17 | -35.60 | 529 |
| 47 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.33 | -4.89 | -27.15 | 214 |
| 48 | RSI momentum · 1h | momentum | 78.82 | -21.18 | 128 | 12.5 | -27.24 | -4.88 | -30.14 | 215 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -17.53 | -2.72 | -22.16 | 208 |
| 50 | Heikin-Ashi · 1h | trend | 78.37 | -21.63 | 333 | 23.7 | -41.87 | -9.08 | -42.17 | 668 |
| 51 | Triple EMA stack · 1h | trend | 78.22 | -21.77 | 117 | 13.7 | -30.55 | -5.70 | -33.05 | 208 |
| 52 | Bollinger reversion · 1h | reversion | 77.97 | -22.03 | 196 | 37.8 | -31.09 | -6.48 | -32.42 | 368 |
| 53 | OBV trend · 1h | momentum | 77.35 | -22.65 | 231 | 17.7 | -34.56 | -6.85 | -36.85 | 300 |
| 54 | ROC + volume · 1h | momentum | 75.86 | -24.14 | 291 | 25.8 | -29.60 | -5.07 | -31.91 | 385 |
| 55 | Donchian 20/10 · 1h | breakout | 75.86 | -24.14 | 114 | 21.1 | -28.00 | -4.89 | -29.81 | 220 |
| 56 | Three white soldiers | momentum | 74.19 | -25.81 | 369 | 17.6 | -44.52 | -20.62 | -44.55 | 614 |
| 57 | VWAP momentum · 1h | momentum | 73.72 | -26.28 | 638 | 22.9 | -52.79 | -11.20 | -53.45 | 1239 |
| 58 | Candlestick reversal · 1h | reversion | 73.33 | -26.67 | 309 | 29.4 | -35.53 | -7.00 | -36.11 | 549 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -19.81 | -3.46 | -25.90 | 194 |
| 60 | Agent (ML meta-label) | meta | 72.97 | -27.03 | 1146 | 21.0 | -13.05 | -2.04 | -19.13 | 355 |
| 61 | Max aggression: 1-day momentum | meta | 72.91 | -27.09 | 21 | 33.3 | -28.79 | -1.54 | -50.32 | 42 |
| 62 | EMA 9/21 cross · 1h | trend | 71.24 | -28.76 | 202 | 9.9 | -35.27 | -6.68 | -36.38 | 334 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -43.91 | -98.88 | 5235 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.27 | -23.69 | -79.32 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.56 | -44.55 | -93.57 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.69 | -30.43 | -88.71 | 1919 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.10 | -36.90 | -91.11 | 2345 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -30.50 | -90.01 | 2227 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -50.54 | -97.71 | 3512 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.14 | -57.06 | -96.14 | 3383 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.03 | -35.44 | -94.04 | 2471 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.82 | -32.55 | -81.91 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -54.87 | -99.47 | 5859 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -43.63 | -93.00 | 2636 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.44 | -37.06 | -95.44 | 3454 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.86 | -99.78 | 6204 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.91 | -43.23 | -91.91 | 2305 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.63 | -27.64 | -75.68 | 1573 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -60.19 | -97.68 | 3570 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.67 | -59.73 | -98.67 | 4822 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.37 | -28.73 | -69.54 | 1212 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.80 | -54.00 | -94.81 | 2797 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.89 | -38.66 | -84.91 | 1821 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.79 | -99.61 | 6329 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.23 | -29.94 | -88.24 | 2239 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.41 | -19.70 | -77.42 | 1714 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.81 | -37.76 | -90.82 | 2266 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.35 | -50.50 | -96.35 | 3808 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.01 | -53.13 | -90.01 | 2148 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.74 | -25.70 | -64.74 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.02 | -25.49 | -74.03 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.93 | -18.40 | -75.93 | 1567 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.76 | -50.48 | -96.76 | 4226 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.89 | -99.92 | 8317 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T16:15 | Agent (ML meta-label) | buy | SOL-USD | 3.63 | — | entry |
| 2026-10-30T16:10 | Agent (ML meta-label) | buy | MSTR | 14.59 | — | entry |
| 2026-10-30T16:10 | Agent (ML meta-label) | sell | SOL-USD | 14.57 | -0.15 | selected signal exited |
| 2026-10-30T16:08 | Copy: Cathie Wood (ARKK) | sell | ARKK | 87.72 | -12.28 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T16:05 | Max aggression: 5-day momentum | sell | LABU | 82.08 | -5.59 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-30T16:05 | Day trade: Stocks in Play ORB | sell | AMD | 24.22 | -0.28 | target is flat |
| 2026-10-30T16:05 | Agent (ML meta-label) | buy | SQQQ | 11.93 | — | rebalance up |
| 2026-10-30T16:05 | Agent (ML meta-label) | buy | SOL-USD | 5.20 | — | rebalance up |
| 2026-10-30T16:05 | Agent (ML meta-label) | buy | ETHU | 3.96 | — | rebalance up |
| 2026-10-30T16:05 | Agent (ML meta-label) | sell | MSTR | 12.18 | 0.03 | selected signal exited |
| 2026-10-30T16:05 | Agent (ML meta-label) | sell | ETH-USD | 12.56 | -0.14 | selected signal exited |
| 2026-10-30T16:05 | Agent | buy | LABU | 18.34 | — | following Candlestick reversal |
| 2026-10-30T16:05 | Opening range 30m | sell | ETHU | 11.16 | -0.20 | exit signal |
| 2026-10-30T16:00 | Agent (ML meta-label) | buy | SQQQ | 2.63 | — | following VWAP reversion |
| 2026-10-30T16:00 | MFI reversion · 1h | sell | ETH-USD | 19.97 | -0.09 | exit signal |
| 2026-10-30T16:00 | Bollinger reversion · 1h | sell | DOGE-USD | 9.72 | -0.02 | exit signal |
| 2026-10-30T16:00 | ROC + volume · 1h | buy | XRP-USD | 18.96 | — | entry signal |
| 2026-10-30T16:00 | VWAP momentum · 1h | buy | BTC-USD | 5.92 | — | entry signal |
| 2026-10-30T16:00 | VWAP momentum · 1h | sell | SQQQ | 5.92 | -0.01 | rebalance down |
| 2026-10-30T16:00 | MACD cross · 1h | buy | BTC-USD | 11.99 | — | entry signal |
| 2026-10-30T16:00 | MACD cross · 1h | sell | XRP-USD | 4.03 | -0.01 | rebalance down |
| 2026-10-30T16:00 | MACD cross · 1h | sell | SQQQ | 3.99 | 0.12 | rebalance down |
| 2026-10-30T16:00 | MACD cross · 1h | sell | DOGE-USD | 3.97 | 0.00 | rebalance down |
| 2026-10-30T16:00 | Opening range 30m | buy | SQQQ | 9.51 | — | rebalance up |
| 2026-10-30T16:00 | Opening range 30m | sell | AAPL | 11.48 | -0.09 | stop-loss |
| 2026-10-30T16:00 | Opening range 15m | sell | AAPL | 10.52 | -0.08 | stop-loss |
| 2026-10-30T15:55 | Opening range 15m | buy | SQQQ | 10.26 | — | entry |
| 2026-10-30T15:55 | Opening range 15m | sell | ETHU | 10.26 | -0.14 | exit signal |
| 2026-10-30T15:50 | Agent | buy | PLTR | 18.33 | — | following Candlestick reversal |
| 2026-10-30T15:46 | Agent (ML meta-label) | buy | MSTR | 10.27 | — | rebalance up |
| 2026-10-30T15:46 | Agent (ML meta-label) | sell | SQQQ | 12.89 | 0.42 | selected signal exited |
| 2026-10-30T15:45 | Three white soldiers | sell | GOOGL | 18.56 | -0.02 | exit signal |
| 2026-10-30T15:40 | Opening range 30m | buy | SQQQ | 1.95 | — | entry signal |
| 2026-10-30T15:35 | Agent | sell | PLTR | 18.12 | -0.26 | selected signal exited |
| 2026-10-30T15:30 | Agent (ML meta-label) | buy | MSTR | 1.89 | — | entry |
| 2026-10-30T15:30 | Agent (ML meta-label) | buy | ETHU | 10.80 | — | entry |
| 2026-10-30T15:30 | Agent (ML meta-label) | sell | LABU | 12.69 | -0.03 | selected signal exited |
| 2026-10-30T15:30 | MFI reversion · 1h | buy | AMZN | 20.16 | — | entry signal |
| 2026-10-30T15:30 | Williams %R · 1h | buy | LABU | 12.33 | — | entry signal |
| 2026-10-30T15:30 | Williams %R · 1h | sell | MSFT | 4.27 | -0.04 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 16:15:05.000170+00:00 -> 2026-10-30 16:25:05.000170+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
