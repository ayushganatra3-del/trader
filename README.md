# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T17:20:05.000132+00:00 · 45227 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.64 (-8.36%)

Closed trades 131, win rate 41.2%, fees £3.78, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.25 | -0.05 |

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

Today: 20517 decisions in 2565 calls, $0.2656 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T17:20 | 6 / 17 / 8 | cash |  |
| Breezy | 2026-11-02T17:20 | 0 / 28 / 3 | cash |  |
| Boozy | 2026-11-02T17:20 | 5 / 24 / 2 | ETHU 64% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.34 | 8.34 | 0 | — | 10.11 | 4.60 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 5.93 | 1.92 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.35 | 2.35 | 24 | 45.8 | 2.85 | 1.08 | -5.32 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.72 | -1.28 | 99 | 45.5 | -13.27 | -3.67 | -13.28 | 138 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 97.70 | -2.29 | 0 | — | 1.08 | 0.50 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 97.53 | -2.47 | 0 | — | -0.29 | -0.10 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.27 | -2.73 | 101 | 35.6 | 4.02 | 2.04 | -2.46 | 94 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.89 | -1.99 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.82 | 0.94 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.12 | -4.88 | 0 | — | -5.22 | -1.98 | -6.49 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.97 | -5.03 | 0 | — | -1.19 | -0.39 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 17 | Agent (rotation) | meta | 94.10 | -5.90 | 143 | 30.1 | -6.90 | -4.80 | -9.57 | 143 |
| 18 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.18 | 1.07 | -8.76 | 215 |
| 19 | Agent | meta | 91.64 | -8.36 | 131 | 41.2 | -8.37 | -4.91 | -12.28 | 208 |
| 20 | Trend pullback · 1h | trend | 91.39 | -8.61 | 101 | 21.8 | -17.26 | -6.36 | -18.32 | 82 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.33 | -2.14 | -16.91 | 1 |
| 22 | Hold BTC | benchmark | 91.23 | -8.77 | 0 | — | 0.02 | 0.17 | -12.65 | 1 |
| 23 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.00 | -1.80 | -13.40 | 88 |
| 24 | Copy: Insider buying | copy | 89.36 | -10.64 | 34 | 35.3 | -21.42 | -4.31 | -23.10 | 62 |
| 25 | Parabolic SAR · 1h | trend | 89.28 | -10.72 | 145 | 27.6 | -15.50 | -3.66 | -16.86 | 241 |
| 26 | Opening range 30m | breakout | 89.25 | -10.74 | 326 | 33.7 | -13.20 | -4.03 | -17.21 | 584 |
| 27 | Daily: Bullish score | daily | 89.14 | -10.86 | 14 | 21.4 | -5.99 | -0.73 | -14.73 | 14 |
| 28 | Donchian 55/20 · 1h | breakout | 88.61 | -11.39 | 60 | 13.3 | -13.98 | -3.15 | -18.06 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.35 | -12.65 | 1 | 0.0 | -2.65 | -0.25 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -10.37 | -3.36 | -14.77 | 99 |
| 31 | Stochastic reversion · 1h | reversion | 85.34 | -14.66 | 227 | 47.6 | -22.58 | -4.74 | -24.84 | 389 |
| 32 | Volume breakout · 1h | breakout | 85.10 | -14.90 | 128 | 28.9 | -17.06 | -3.83 | -18.61 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.34 | -15.66 | 88 | 23.9 | -20.41 | -4.12 | -23.56 | 177 |
| 34 | Connors RSI(2) · 1h | reversion | 84.04 | -15.96 | 190 | 40.5 | -20.61 | -6.57 | -21.22 | 143 |
| 35 | ADX DI cross · 1h | trend | 83.88 | -16.12 | 142 | 19.0 | -19.51 | -3.61 | -21.81 | 259 |
| 36 | MFI reversion · 1h | reversion | 83.25 | -16.75 | 299 | 32.8 | -16.00 | -2.57 | -17.91 | 145 |
| 37 | Max aggression: 5-day momentum | meta | 82.47 | -17.53 | 15 | 40.0 | -34.46 | -2.49 | -37.35 | 26 |
| 38 | Opening range 15m | breakout | 82.12 | -17.88 | 400 | 30.8 | -18.44 | -5.38 | -20.33 | 716 |
| 39 | Bollinger breakout · 1h | breakout | 82.01 | -17.99 | 139 | 25.2 | -15.14 | -2.80 | -22.52 | 233 |
| 40 | Ichimoku · 1h | trend | 81.26 | -18.74 | 82 | 13.4 | -21.43 | -4.32 | -25.58 | 120 |
| 41 | CCI reversion · 1h | reversion | 80.22 | -19.78 | 258 | 45.7 | -25.88 | -4.04 | -28.51 | 444 |
| 42 | Daily: Momentum burst | daily | 79.44 | -20.56 | 19 | 15.8 | -25.34 | -3.61 | -30.47 | 33 |
| 43 | Supertrend · 1h | trend | 78.45 | -21.55 | 138 | 13.0 | -27.30 | -5.27 | -28.74 | 221 |
| 44 | Bollinger reversion · 1h | reversion | 78.31 | -21.69 | 209 | 39.2 | -29.67 | -6.14 | -30.82 | 372 |
| 45 | EMA 20/50 cross · 1h | trend | 78.26 | -21.74 | 90 | 11.1 | -24.16 | -5.04 | -27.72 | 129 |
| 46 | Williams %R · 1h | reversion | 77.90 | -22.10 | 261 | 47.1 | -34.99 | -6.37 | -35.85 | 518 |
| 47 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.51 | -5.51 | -28.00 | 211 |
| 48 | Z-score reversion · 1h | reversion | 77.55 | -22.45 | 137 | 34.3 | -14.41 | -2.13 | -22.55 | 206 |
| 49 | MACD cross · 1h | trend | 77.54 | -22.46 | 294 | 23.8 | -33.47 | -6.64 | -35.33 | 465 |
| 50 | Triple EMA stack · 1h | trend | 77.05 | -22.95 | 123 | 14.6 | -30.87 | -6.28 | -31.23 | 207 |
| 51 | Heikin-Ashi · 1h | trend | 76.87 | -23.13 | 344 | 23.3 | -38.79 | -7.93 | -42.68 | 660 |
| 52 | RSI momentum · 1h | momentum | 76.75 | -23.25 | 135 | 12.6 | -31.29 | -6.04 | -31.43 | 214 |
| 53 | OBV trend · 1h | momentum | 76.15 | -23.85 | 237 | 17.7 | -36.11 | -7.90 | -36.34 | 308 |
| 54 | Donchian 20/10 · 1h | breakout | 75.32 | -24.68 | 119 | 20.2 | -26.50 | -4.47 | -30.86 | 206 |
| 55 | ROC + volume · 1h | momentum | 74.54 | -25.46 | 299 | 25.4 | -29.60 | -5.04 | -34.36 | 373 |
| 56 | RSI(14) reversion · 1h | reversion | 72.17 | -27.83 | 124 | 26.6 | -20.90 | -3.68 | -26.17 | 198 |
| 57 | Candlestick reversal · 1h | reversion | 70.38 | -29.62 | 337 | 28.5 | -36.88 | -7.55 | -37.15 | 548 |
| 58 | Max aggression: 1-day momentum | meta | 70.22 | -29.78 | 22 | 31.8 | -33.93 | -1.98 | -50.32 | 42 |
| 59 | Three white soldiers | momentum | 70.22 | -29.78 | 404 | 16.1 | -45.62 | -21.21 | -45.96 | 619 |
| 60 | Agent (ML meta-label) | meta | 69.68 | -30.32 | 1242 | 20.9 | -23.60 | -4.45 | -27.99 | 314 |
| 61 | EMA 9/21 cross · 1h | trend | 69.46 | -30.54 | 215 | 9.8 | -36.56 | -6.73 | -40.38 | 328 |
| 62 | VWAP momentum · 1h | momentum | 69.35 | -30.65 | 687 | 21.8 | -51.72 | -10.62 | -52.96 | 1225 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.45 | -98.95 | 5209 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.04 | -23.92 | -80.05 | 1405 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.72 | -44.15 | -93.72 | 2532 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.12 | -32.01 | -89.13 | 1926 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.54 | -37.62 | -91.54 | 2337 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.88 | -32.16 | -90.88 | 2237 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -52.96 | -97.78 | 3486 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -57.71 | -96.32 | 3398 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -34.51 | -93.48 | 2428 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.31 | -33.69 | -82.31 | 1687 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -54.47 | -99.47 | 5818 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.02 | -43.39 | -93.03 | 2616 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.61 | -37.33 | -95.62 | 3398 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -75.47 | -99.79 | 6156 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.01 | -44.88 | -92.01 | 2284 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.04 | -26.23 | -75.08 | 1571 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -60.29 | -97.76 | 3549 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.67 | -61.30 | -98.67 | 4816 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.13 | -27.99 | -69.16 | 1197 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -53.79 | -94.72 | 2768 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.04 | -37.60 | -85.04 | 1812 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -70.87 | -99.62 | 6303 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.97 | -30.03 | -87.99 | 2201 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.30 | -19.02 | -76.53 | 1687 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.20 | -36.90 | -90.26 | 2222 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.37 | -51.29 | -96.38 | 3782 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.72 | -54.57 | -89.72 | 2135 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.18 | -25.25 | -64.70 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.33 | -25.51 | -74.33 | 1275 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.84 | -18.65 | -76.03 | 1576 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.73 | -49.15 | -96.76 | 4211 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.30 | -99.92 | 8230 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T17:20 | Agent (ML meta-label) | buy | UPRO | 8.71 | — | entry |
| 2026-11-02T17:20 | Agent (ML meta-label) | buy | SOXL | 8.71 | — | entry |
| 2026-11-02T17:20 | Agent (ML meta-label) | buy | NVDA | 8.71 | — | entry |
| 2026-11-02T17:20 | Agent (ML meta-label) | buy | ETHU | 8.71 | — | following Stochastic reversion |
| 2026-11-02T17:20 | Agent (ML meta-label) | sell | TSLA | 5.31 | -0.00 | rebalance down |
| 2026-11-02T17:20 | Agent (ML meta-label) | sell | SQQQ | 5.45 | 0.05 | rebalance down |
| 2026-11-02T17:20 | Agent (ML meta-label) | sell | BITX | 8.73 | -0.01 | rebalance down |
| 2026-11-02T17:15 | Agent (ML meta-label) | buy | COIN | 7.95 | — | entry |
| 2026-11-02T17:15 | Agent (ML meta-label) | sell | AMZN | 17.45 | -0.01 | selected signal exited |
| 2026-11-02T17:10 | Agent (ML meta-label) | buy | BITX | 17.46 | — | following Z-score reversion |
| 2026-11-02T17:10 | Agent (ML meta-label) | buy | AMZN | 17.46 | — | following Bollinger reversion |
| 2026-11-02T17:10 | Agent (ML meta-label) | sell | GOOGL | 13.96 | 0.01 | selected signal exited |
| 2026-11-02T17:10 | Agent (ML meta-label) | sell | ETHU | 17.43 | -0.03 | selected signal exited |
| 2026-11-02T17:05 | Agent (rotation) | sell | TNA | 3.14 | -0.01 | selected signal exited |
| 2026-11-02T17:05 | Agent (ML meta-label) | buy | ETHU | 3.50 | — | rebalance up |
| 2026-11-02T17:05 | Agent (ML meta-label) | sell | SOXL | 13.67 | 0.02 | selected signal exited |
| 2026-11-02T17:05 | Stochastic reversion · 1h | buy | DOGE-USD | 5.34 | — | entry |
| 2026-11-02T17:05 | EMA 9/21 cross · 1h | buy | TNA | 3.47 | — | rebalance up |
| 2026-11-02T17:05 | EMA 9/21 cross · 1h | sell | TSLA | 3.48 | 0.01 | rebalance down |
| 2026-11-02T17:05 | Gap and go | sell | TNA | 23.54 | -0.11 | exit signal |
| 2026-11-02T17:00 | Agent (ML meta-label) | buy | SOXL | 13.65 | — | entry |
| 2026-11-02T17:00 | Agent (ML meta-label) | buy | ETHU | 13.95 | — | following Stochastic reversion |
| 2026-11-02T17:00 | Agent (ML meta-label) | sell | MSTR | 17.35 | -0.12 | selected signal exited |
| 2026-11-02T17:00 | Agent (ML meta-label) | sell | GOOGL | 3.52 | -0.00 | rebalance down |
| 2026-11-02T17:00 | Bollinger reversion · 1h | buy | BTC-USD | 6.03 | — | entry signal |
| 2026-11-02T17:00 | RSI momentum · 1h | sell | ETH-USD | 19.14 | -0.14 | exit signal |
| 2026-11-02T17:00 | Triple EMA stack · 1h | buy | TNA | 7.65 | — | rebalance up |
| 2026-11-02T17:00 | Triple EMA stack · 1h | buy | SQQQ | 3.86 | — | rebalance up |
| 2026-11-02T17:00 | Triple EMA stack · 1h | buy | IWM | 3.86 | — | rebalance up |
| 2026-11-02T17:00 | Triple EMA stack · 1h | sell | ETH-USD | 15.38 | -0.17 | exit signal |
| 2026-11-02T17:00 | Opening range 30m | buy | UPRO | 5.90 | — | rebalance up |
| 2026-11-02T17:00 | Opening range 30m | buy | TNA | 5.86 | — | rebalance up |
| 2026-11-02T17:00 | Opening range 30m | buy | SPY | 5.83 | — | rebalance up |
| 2026-11-02T17:00 | Opening range 30m | buy | MSTR | 5.85 | — | rebalance up |
| 2026-11-02T17:00 | Opening range 30m | buy | IWM | 5.82 | — | rebalance up |
| 2026-11-02T17:00 | Opening range 30m | buy | AMZN | 5.83 | — | rebalance up |
| 2026-11-02T17:00 | Opening range 30m | sell | PLTR | 6.85 | -0.11 | stop-loss |
| 2026-11-02T17:00 | Opening range 15m | sell | PLTR | 7.46 | -0.06 | stop-loss |
| 2026-11-02T16:55 | Agent (ML meta-label) | buy | MSTR | 17.47 | — | following Williams %R |
| 2026-11-02T16:55 | Agent (ML meta-label) | buy | GOOGL | 17.47 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 17:20:05.000132+00:00 -> 2026-11-02 17:30:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
