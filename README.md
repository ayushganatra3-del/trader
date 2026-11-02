# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T20:20:05.000151+00:00 · 45356 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.80 (-9.20%)

Closed trades 137, win rate 40.1%, fees £3.90, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMZN | 18.13 | +0.00 |
| MSTR | 18.18 | +0.05 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BPRE 12%, ACN 12%, SCQCU 12%, NPB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 32115 decisions in 2952 calls, $0.4017 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T20:20 | 8 / 19 / 4 | cash |  |
| Breezy | 2026-11-02T20:20 | 0 / 27 / 4 | cash |  |
| Boozy | 2026-11-02T20:20 | 7 / 24 / 0 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.34 | +0.86% | 5 |
| Bollinger reversion | AMZN | 2.17 | +2.35% | 10 |
| Stochastic reversion | ETHU | 2.10 | +5.34% | 11 |
| Z-score reversion | BITX | 2.10 | +6.37% | 7 |
| Williams %R | MSTR | 2.00 | +3.35% | 15 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.92 | 8.92 | 0 | — | 9.57 | 4.23 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.31 | 5.31 | 16 | 68.8 | 6.84 | 2.21 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.35 | 2.35 | 24 | 45.8 | 2.09 | 0.83 | -5.32 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.99 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.54 | -1.46 | 100 | 46.0 | -13.32 | -3.71 | -13.53 | 140 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.05 | -1.95 | 0 | — | 1.37 | 0.62 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.91 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.99 | -3.01 | 0 | — | -1.45 | -0.74 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.72 | -3.27 | 103 | 35.0 | 3.51 | 1.79 | -2.72 | 94 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.07 | 0.60 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.62 | -5.94 | -6.20 | 20 |
| 14 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.67 | -5.33 | 28 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.33 | -5.67 | 0 | — | -5.13 | -2.01 | -6.35 | 1 |
| 16 | Agent (rotation) | meta | 94.31 | -5.69 | 143 | 30.1 | -5.56 | -3.40 | -8.90 | 159 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.08 | -5.92 | 0 | — | -2.53 | -0.94 | -7.64 | 1 |
| 18 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.87 | 1.30 | -8.76 | 214 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.05 | -16.91 | 1 |
| 20 | Trend pullback · 1h | trend | 90.96 | -9.04 | 101 | 21.8 | -16.64 | -6.22 | -17.65 | 80 |
| 21 | Hold BTC | benchmark | 90.89 | -9.11 | 0 | — | -0.51 | 0.09 | -12.65 | 1 |
| 22 | Agent | meta | 90.80 | -9.20 | 137 | 40.1 | -10.29 | -6.34 | -12.20 | 209 |
| 23 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.73 | -2.11 | -13.40 | 88 |
| 24 | Opening range 30m | breakout | 89.26 | -10.74 | 333 | 33.0 | -13.34 | -4.12 | -17.21 | 578 |
| 25 | Donchian 55/20 · 1h | breakout | 89.01 | -10.99 | 60 | 13.3 | -14.10 | -3.20 | -18.06 | 99 |
| 26 | Copy: Insider buying | copy | 88.86 | -11.14 | 35 | 37.1 | -22.40 | -4.58 | -23.62 | 62 |
| 27 | Daily: Bullish score | daily | 88.74 | -11.26 | 14 | 21.4 | -5.98 | -0.73 | -14.73 | 14 |
| 28 | Parabolic SAR · 1h | trend | 88.65 | -11.35 | 149 | 26.8 | -16.20 | -3.83 | -17.36 | 241 |
| 29 | Agent (aggressive) | meta | 86.96 | -13.04 | 65 | 33.8 | -11.53 | -3.85 | -14.77 | 94 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 85.87 | -14.12 | 1 | 0.0 | -4.72 | -0.59 | -16.45 | 1 |
| 31 | Max aggression: 5-day momentum | meta | 85.62 | -14.38 | 15 | 40.0 | -32.01 | -2.22 | -37.35 | 26 |
| 32 | Volume breakout · 1h | breakout | 84.77 | -15.22 | 129 | 28.7 | -17.56 | -3.97 | -18.81 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.60 | -15.40 | 88 | 23.9 | -20.62 | -4.01 | -24.08 | 172 |
| 34 | Connors RSI(2) · 1h | reversion | 84.16 | -15.84 | 191 | 40.8 | -20.85 | -6.73 | -21.57 | 138 |
| 35 | Stochastic reversion · 1h | reversion | 83.70 | -16.30 | 232 | 46.6 | -25.08 | -5.34 | -25.87 | 390 |
| 36 | ADX DI cross · 1h | trend | 83.40 | -16.59 | 147 | 18.4 | -20.32 | -3.83 | -22.16 | 253 |
| 37 | MFI reversion · 1h | reversion | 83.31 | -16.69 | 299 | 32.8 | -16.54 | -2.68 | -18.26 | 145 |
| 38 | Opening range 15m | breakout | 81.97 | -18.04 | 407 | 30.2 | -18.96 | -5.58 | -20.73 | 708 |
| 39 | Ichimoku · 1h | trend | 81.77 | -18.23 | 82 | 13.4 | -18.34 | -3.75 | -25.58 | 119 |
| 40 | Bollinger breakout · 1h | breakout | 81.61 | -18.39 | 140 | 25.0 | -15.69 | -2.92 | -22.79 | 233 |
| 41 | CCI reversion · 1h | reversion | 78.97 | -21.03 | 263 | 44.9 | -27.16 | -4.36 | -28.51 | 441 |
| 42 | EMA 20/50 cross · 1h | trend | 78.89 | -21.11 | 90 | 11.1 | -21.93 | -4.12 | -27.42 | 126 |
| 43 | Supertrend · 1h | trend | 77.88 | -22.12 | 141 | 12.8 | -27.55 | -5.20 | -30.03 | 222 |
| 44 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.16 | -5.44 | -27.67 | 209 |
| 45 | MACD cross · 1h | trend | 77.28 | -22.72 | 295 | 23.7 | -32.89 | -6.61 | -34.98 | 467 |
| 46 | Daily: Momentum burst ⏸ | daily | 77.04 | -22.96 | 23 | 13.0 | -26.80 | -3.69 | -33.09 | 33 |
| 47 | Bollinger reversion · 1h | reversion | 77.02 | -22.98 | 214 | 38.3 | -30.63 | -6.46 | -31.50 | 372 |
| 48 | Triple EMA stack · 1h | trend | 76.88 | -23.12 | 124 | 14.5 | -30.36 | -5.65 | -30.89 | 208 |
| 49 | RSI momentum · 1h | momentum | 76.77 | -23.23 | 135 | 12.6 | -31.45 | -6.07 | -31.58 | 214 |
| 50 | Williams %R · 1h | reversion | 76.40 | -23.60 | 267 | 46.1 | -35.83 | -6.55 | -36.98 | 518 |
| 51 | Heikin-Ashi · 1h | trend | 76.17 | -23.83 | 356 | 22.5 | -40.89 | -8.85 | -43.18 | 659 |
| 52 | OBV trend · 1h | momentum | 75.77 | -24.23 | 239 | 17.6 | -33.81 | -7.32 | -33.81 | 301 |
| 53 | Donchian 20/10 · 1h | breakout | 75.69 | -24.31 | 119 | 20.2 | -26.29 | -4.46 | -30.95 | 206 |
| 54 | Z-score reversion · 1h | reversion | 75.63 | -24.37 | 138 | 34.1 | -16.43 | -2.54 | -22.92 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.68 | -25.32 | 299 | 25.4 | -29.68 | -5.10 | -34.50 | 370 |
| 56 | RSI(14) reversion · 1h | reversion | 71.19 | -28.82 | 128 | 25.8 | -20.28 | -3.63 | -26.27 | 196 |
| 57 | Three white soldiers | momentum | 70.25 | -29.75 | 406 | 16.3 | -45.48 | -21.45 | -45.69 | 610 |
| 58 | Candlestick reversal · 1h | reversion | 69.43 | -30.57 | 340 | 28.2 | -37.68 | -7.81 | -38.55 | 544 |
| 59 | VWAP momentum · 1h | momentum | 69.08 | -30.92 | 690 | 21.7 | -53.48 | -10.97 | -54.90 | 1222 |
| 60 | EMA 9/21 cross · 1h | trend | 69.02 | -30.98 | 217 | 9.7 | -36.98 | -6.87 | -40.45 | 331 |
| 61 | Max aggression: 1-day momentum ⏸ | meta | 68.78 | -31.22 | 23 | 30.4 | -34.67 | -2.06 | -50.32 | 42 |
| 62 | Agent (ML meta-label) | meta | 68.60 | -31.40 | 1300 | 20.4 | -17.46 | -3.31 | -19.41 | 316 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -45.04 | -98.95 | 5166 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.93 | -24.44 | -80.01 | 1401 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.68 | -46.75 | -93.71 | 2515 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.94 | -31.88 | -88.95 | 1901 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.43 | -39.03 | -91.48 | 2323 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.85 | -33.22 | -90.90 | 2236 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -54.98 | -97.75 | 3465 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -62.19 | -96.35 | 3378 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.45 | -35.89 | -93.54 | 2416 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.14 | -34.91 | -82.14 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -57.42 | -99.48 | 5881 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.04 | -44.82 | -93.08 | 2609 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.62 | -38.82 | -95.63 | 3388 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -82.13 | -99.79 | 6161 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.88 | -46.42 | -91.88 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.90 | -26.55 | -75.07 | 1564 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -66.08 | -97.76 | 3542 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -65.08 | -98.68 | 4835 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.29 | -28.49 | -69.31 | 1200 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -56.55 | -94.73 | 2762 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.85 | -38.57 | -84.95 | 1799 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -76.07 | -99.62 | 6314 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -31.32 | -88.38 | 2234 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.35 | -19.97 | -77.43 | 1712 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.32 | -37.86 | -90.36 | 2242 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.46 | -53.63 | -96.47 | 3818 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.55 | -56.13 | -89.59 | 2136 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -63.91 | -25.50 | -64.70 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.19 | -26.09 | -74.28 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.65 | -19.20 | -76.84 | 1612 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.84 | -52.96 | -96.86 | 4248 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -109.56 | -99.92 | 8223 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T20:20 | Agent (ML meta-label) | buy | TSLA | 3.95 | — | rebalance up |
| 2026-11-02T20:20 | Agent (ML meta-label) | buy | SQQQ | 3.94 | — | rebalance up |
| 2026-11-02T20:20 | Agent (ML meta-label) | buy | ETHU | 3.91 | — | rebalance up |
| 2026-11-02T20:20 | Agent (ML meta-label) | buy | BITX | 3.89 | — | rebalance up |
| 2026-11-02T20:20 | Agent (ML meta-label) | sell | SOXL | 4.27 | 0.01 | rebalance down |
| 2026-11-02T20:20 | Agent (ML meta-label) | sell | COIN | 11.42 | 0.00 | selected signal exited |
| 2026-11-02T20:10 | Agent (ML meta-label) | buy | SOXL | 11.41 | — | entry |
| 2026-11-02T20:10 | Agent (ML meta-label) | buy | COIN | 11.42 | — | entry |
| 2026-11-02T20:10 | Agent (ML meta-label) | sell | TSLA | 5.70 | -0.03 | rebalance down |
| 2026-11-02T20:10 | Agent (ML meta-label) | sell | SQQQ | 5.74 | 0.03 | rebalance down |
| 2026-11-02T20:10 | Agent (ML meta-label) | sell | ETHU | 5.70 | -0.00 | rebalance down |
| 2026-11-02T20:10 | Agent (ML meta-label) | sell | BITX | 5.69 | -0.02 | rebalance down |
| 2026-11-02T20:05 | Agent (ML meta-label) | buy | TSLA | 3.83 | — | rebalance up |
| 2026-11-02T20:05 | Agent (ML meta-label) | buy | SQQQ | 3.80 | — | rebalance up |
| 2026-11-02T20:05 | Agent (ML meta-label) | buy | ETHU | 3.78 | — | rebalance up |
| 2026-11-02T20:05 | Agent (ML meta-label) | buy | BITX | 3.83 | — | rebalance up |
| 2026-11-02T20:05 | Agent (ML meta-label) | sell | MSTR | 1.92 | -0.01 | selected signal exited |
| 2026-11-02T20:05 | Agent (ML meta-label) | sell | COIN | 13.32 | -0.04 | selected signal exited |
| 2026-11-02T20:05 | Williams %R · 1h | sell | DOGE-USD | 10.88 | -0.04 | target is flat |
| 2026-11-02T20:05 | Stochastic reversion · 1h | sell | DOGE-USD | 4.39 | -0.02 | target is flat |
| 2026-11-02T20:05 | Three white soldiers | buy | DOGE-USD | 17.57 | — | entry signal |
| 2026-11-02T20:00 | Agent (ML meta-label) | buy | TSLA | 5.47 | — | rebalance up |
| 2026-11-02T20:00 | Agent (ML meta-label) | buy | SQQQ | 5.49 | — | rebalance up |
| 2026-11-02T20:00 | Agent (ML meta-label) | buy | ETHU | 5.47 | — | rebalance up |
| 2026-11-02T20:00 | Agent (ML meta-label) | buy | COIN | 5.50 | — | rebalance up |
| 2026-11-02T20:00 | Agent (ML meta-label) | buy | BITX | 5.46 | — | rebalance up |
| 2026-11-02T20:00 | Agent (ML meta-label) | sell | TQQQ | 7.85 | -0.01 | selected signal exited |
| 2026-11-02T20:00 | Agent (ML meta-label) | sell | SOXL | 7.85 | -0.01 | selected signal exited |
| 2026-11-02T20:00 | Agent (ML meta-label) | sell | MSTR | 5.91 | -0.01 | rebalance down |
| 2026-11-02T20:00 | Agent | sell | ETHU | 18.31 | 0.20 | selected signal exited |
| 2026-11-02T20:00 | CCI reversion · 1h | buy | XRP-USD | 19.75 | — | entry signal |
| 2026-11-02T20:00 | Williams %R · 1h | buy | SOL-USD | 10.90 | — | entry signal |
| 2026-11-02T20:00 | Williams %R · 1h | buy | DOGE-USD | 10.92 | — | entry signal |
| 2026-11-02T20:00 | Williams %R · 1h | buy | BTC-USD | 10.92 | — | entry signal |
| 2026-11-02T20:00 | Williams %R · 1h | sell | META | 8.11 | -0.04 | rebalance down |
| 2026-11-02T20:00 | Williams %R · 1h | sell | ETHU | 8.27 | 0.07 | rebalance down |
| 2026-11-02T20:00 | Williams %R · 1h | sell | ETH-USD | 4.37 | -0.03 | rebalance down |
| 2026-11-02T20:00 | Williams %R · 1h | sell | BITX | 8.23 | -0.07 | rebalance down |
| 2026-11-02T20:00 | Stochastic reversion · 1h | buy | SOL-USD | 4.08 | — | entry signal |
| 2026-11-02T20:00 | Stochastic reversion · 1h | buy | DOGE-USD | 4.40 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 20:20:05.000151+00:00 -> 2026-11-02 20:30:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
