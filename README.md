# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T15:25:05.000137+00:00 · 24915 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.55 (-8.45%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.87%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.27 | -0.10 |
| SQQQ | 18.62 | +0.24 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 18611 decisions in 2296 calls, $0.2410 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T15:25 | 1 / 5 / 25 | cash |  |
| Breezy | 2026-10-16T15:25 | 0 / 24 / 7 | cash |  |
| Boozy | 2026-10-16T15:25 | 2 / 26 / 3 | COIN 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.44 | 4.44 | 9 | 66.7 | 6.12 | 2.62 | -3.27 | 19 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.31 | 4.32 | 0 | — | 5.66 | 2.70 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.74 | 3.74 | 10 | 70.0 | -1.65 | -0.47 | -9.61 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 102.58 | 2.58 | 14 | 35.7 | 5.08 | 1.52 | -7.55 | 44 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.30 | 1.30 | 1 | 100.0 | 2.70 | 0.73 | -7.93 | 9 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.44 | 0.44 | 0 | — | 4.79 | 1.84 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | VWAP reversion · 1h | reversion | 99.84 | -0.16 | 59 | 39.0 | -11.47 | -3.33 | -13.79 | 124 |
| 10 | Hold SPY | benchmark | 99.11 | -0.89 | 0 | — | -0.84 | -0.45 | -3.23 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.76 | -3.91 | 20 |
| 12 | Copy: Insider buying | copy | 98.41 | -1.59 | 20 | 45.0 | -11.94 | -2.03 | -20.62 | 75 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 98.10 | -1.90 | 51 | 31.4 | 1.36 | 0.79 | -2.96 | 69 |
| 14 | Donchian 55/20 · 1h | breakout | 98.05 | -1.95 | 36 | 16.7 | 8.28 | 1.13 | -22.12 | 109 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.06 | -2.94 | 0 | — | -1.74 | -0.70 | -4.45 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.04 | -2.96 | 0 | — | -4.87 | -1.95 | -7.50 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 96.81 | -3.19 | 0 | — | -6.11 | -3.39 | -6.38 | 1 |
| 18 | Hold BTC | benchmark | 96.53 | -3.47 | 0 | — | 28.84 | 3.36 | -8.68 | 1 |
| 19 | Trend pullback · 1h | trend | 96.34 | -3.66 | 87 | 24.1 | -21.49 | -6.37 | -22.23 | 152 |
| 20 | Max aggression: 5-day momentum | meta | 95.85 | -4.15 | 8 | 37.5 | -19.41 | -1.70 | -34.64 | 26 |
| 21 | Agent (rotation) | meta | 95.83 | -4.17 | 107 | 32.7 | -9.29 | -3.63 | -11.40 | 294 |
| 22 | Three white soldiers · 1h | momentum | 95.70 | -4.30 | 11 | 0.0 | 0.04 | 0.07 | -5.01 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.79 | -5.21 | 78 | 20.5 | -8.46 | -1.49 | -13.33 | 257 |
| 24 | Daily: Momentum burst | daily | 94.19 | -5.81 | 5 | 20.0 | -5.74 | -0.73 | -18.64 | 42 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 3.35 | 0.78 | -9.46 | 102 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.31 | -6.78 | 197 |
| 27 | Parabolic SAR · 1h | trend | 92.92 | -7.08 | 94 | 22.3 | 3.08 | 0.58 | -22.32 | 277 |
| 28 | EMA 20/50 cross · 1h | trend | 92.49 | -7.51 | 53 | 15.1 | -4.87 | -0.47 | -22.92 | 130 |
| 29 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 30 | Agent | meta | 91.55 | -8.45 | 77 | 39.0 | -11.36 | -6.28 | -11.97 | 247 |
| 31 | RSI momentum · 1h | momentum | 91.32 | -8.68 | 73 | 17.8 | 1.14 | 0.34 | -26.55 | 219 |
| 32 | Daily: Bullish score | daily | 91.12 | -8.88 | 7 | 0.0 | -5.38 | -0.50 | -12.76 | 13 |
| 33 | Bollinger breakout · 1h | breakout | 90.90 | -9.10 | 82 | 29.3 | 5.62 | 0.91 | -14.21 | 274 |
| 34 | Timing: Nasdaq FTD · TQQQ | daily | 90.78 | -9.22 | 0 | — | -18.45 | -3.56 | -19.22 | 1 |
| 35 | Agent (aggressive) | meta | 90.77 | -9.23 | 38 | 31.6 | -7.50 | -2.77 | -9.47 | 125 |
| 36 | Opening range 30m | breakout | 90.53 | -9.47 | 192 | 29.7 | -12.77 | -3.52 | -17.60 | 572 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 90.48 | -9.52 | 0 | — | 1.46 | 0.39 | -13.89 | 1 |
| 38 | MACD cross · 1h | trend | 90.39 | -9.61 | 162 | 23.5 | -13.54 | -1.80 | -26.35 | 458 |
| 39 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 40 | Supertrend · 1h | trend | 89.88 | -10.12 | 75 | 13.3 | -2.59 | -0.09 | -28.93 | 213 |
| 41 | Triple EMA stack · 1h | trend | 89.76 | -10.24 | 79 | 16.5 | -9.00 | -0.74 | -33.23 | 235 |
| 42 | Connors RSI(2) · 1h | reversion | 88.92 | -11.08 | 143 | 40.6 | -24.00 | -7.24 | -25.02 | 241 |
| 43 | Stochastic reversion · 1h | reversion | 88.68 | -11.32 | 131 | 45.0 | -18.80 | -3.53 | -19.90 | 349 |
| 44 | Keltner breakout · 1h | breakout | 88.42 | -11.58 | 52 | 23.1 | -10.00 | -1.26 | -27.05 | 210 |
| 45 | OBV trend · 1h | momentum | 87.77 | -12.23 | 167 | 18.6 | -9.15 | -0.75 | -33.99 | 321 |
| 46 | Max aggression: 1-day momentum | meta | 87.71 | -12.29 | 14 | 35.7 | -8.66 | -0.11 | -37.31 | 43 |
| 47 | MACD zero-line · 1h | trend | 86.22 | -13.78 | 79 | 16.5 | -23.12 | -4.53 | -23.20 | 224 |
| 48 | Opening range 15m | breakout | 86.07 | -13.93 | 241 | 25.3 | -17.73 | -4.61 | -21.40 | 709 |
| 49 | Z-score reversion · 1h | reversion | 85.77 | -14.23 | 75 | 36.0 | -12.65 | -2.31 | -17.27 | 178 |
| 50 | MFI reversion · 1h | reversion | 85.54 | -14.46 | 200 | 30.5 | -19.98 | -3.46 | -20.26 | 140 |
| 51 | Donchian 20/10 · 1h | breakout | 85.10 | -14.90 | 74 | 18.9 | 1.09 | 0.34 | -21.10 | 219 |
| 52 | Agent (ML meta-label) | meta | 84.78 | -15.22 | 574 | 19.0 | -3.81 | -0.42 | -15.39 | 382 |
| 53 | Three white soldiers | momentum | 84.72 | -15.28 | 207 | 18.8 | -47.88 | -19.98 | -48.52 | 610 |
| 54 | VWAP momentum · 1h | momentum | 83.44 | -16.56 | 380 | 21.3 | -36.30 | -5.49 | -43.67 | 1252 |
| 55 | Heikin-Ashi · 1h | trend | 83.33 | -16.67 | 185 | 24.9 | -31.67 | -5.17 | -40.19 | 673 |
| 56 | ROC + volume · 1h | momentum | 83.29 | -16.71 | 187 | 21.9 | -11.79 | -1.55 | -25.71 | 403 |
| 57 | EMA 9/21 cross · 1h | trend | 83.14 | -16.86 | 121 | 12.4 | -6.42 | -0.55 | -28.65 | 321 |
| 58 | Williams %R · 1h | reversion | 82.05 | -17.95 | 174 | 43.7 | -32.85 | -5.44 | -34.85 | 524 |
| 59 | Bollinger reversion · 1h | reversion | 81.83 | -18.17 | 134 | 32.1 | -28.78 | -6.16 | -31.36 | 336 |
| 60 | RSI(14) reversion · 1h | reversion | 81.46 | -18.54 | 64 | 23.4 | -12.43 | -2.25 | -19.65 | 160 |
| 61 | CCI reversion · 1h | reversion | 81.05 | -18.95 | 146 | 42.5 | -17.04 | -2.23 | -23.38 | 427 |
| 62 | Candlestick reversal · 1h | reversion | 78.05 | -21.95 | 193 | 25.9 | -33.33 | -6.19 | -33.72 | 519 |
| 63 | RSI(14) reversion | reversion | 64.45 | -35.55 | 591 | 28.1 | -73.80 | -16.68 | -73.82 | 1572 |
| 64 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.61 | -18.27 | -63.61 | 889 |
| 65 | ROC + volume | momentum | 63.31 | -36.69 | 545 | 21.8 | -75.84 | -17.48 | -77.41 | 1726 |
| 66 | Squeeze breakout | breakout | 63.30 | -36.70 | 427 | 14.8 | -62.92 | -17.79 | -63.90 | 1217 |
| 67 | Donchian 55/20 | breakout | 61.03 | -38.97 | 434 | 17.7 | -69.45 | -14.56 | -71.81 | 1286 |
| 68 | EMA 20/50 cross | trend | 59.67 | -40.33 | 450 | 19.3 | -77.42 | -15.24 | -79.02 | 1453 |
| 69 | AI bee: Boozy | ai | 56.87 | -43.13 | 289 | 5.5 | — | — | — | — |
| 70 | VWAP reversion | reversion | 56.70 | -43.30 | 602 | 23.9 | -72.96 | -15.32 | -72.96 | 1444 |
| 71 | Keltner breakout | breakout | 54.35 | -45.65 | 606 | 16.0 | -83.72 | -26.88 | -83.73 | 1846 |
| 72 | Supertrend | trend | 51.80 | -48.20 | 631 | 19.8 | -86.52 | -20.44 | -86.84 | 1914 |
| 73 | Ichimoku | trend | 51.70 | -48.30 | 550 | 11.6 | -82.11 | -22.91 | -82.16 | 1734 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.71 | -98.66 | 5319 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.56 | -30.09 | -93.57 | 2603 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.63 | -24.72 | -90.63 | 2373 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.79 | -27.13 | -91.83 | 2343 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -32.29 | -97.48 | 3530 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -36.05 | -96.74 | 3620 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.51 | -26.29 | -94.53 | 2633 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -35.84 | -99.39 | 5736 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.48 | -25.80 | -91.49 | 2650 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.71 | -96.37 | 3570 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.97 | -99.73 | 6176 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.81 | -29.31 | -91.81 | 2372 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -37.73 | -97.48 | 3656 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.23 | -98.47 | 4697 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.72 | -32.86 | -93.74 | 2810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.21 | -99.54 | 6198 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.28 | -22.24 | -86.28 | 2116 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.83 | -27.22 | -87.83 | 2132 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.96 | -32.38 | -95.96 | 3786 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.31 | -33.64 | -89.31 | 2105 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -33.82 | -95.80 | 4107 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.24 | -99.89 | 8246 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T15:25 | Agent (ML meta-label) | buy | TSLA | 1.20 | — | entry |
| 2026-10-16T15:25 | Agent (ML meta-label) | buy | DOGE-USD | 3.69 | — | entry |
| 2026-10-16T15:25 | Agent (ML meta-label) | sell | LABU | 4.89 | -0.35 | selected signal exited |
| 2026-10-16T15:25 | Agent | sell | LABU | 17.13 | -1.44 | selected signal exited |
| 2026-10-16T15:25 | Williams %R · 1h | buy | AMD | 4.12 | — | rebalance up |
| 2026-10-16T15:25 | Williams %R · 1h | sell | GOOGL | 6.61 | -0.18 | stop-loss |
| 2026-10-16T15:25 | Candlestick reversal · 1h | buy | TSLA | 4.17 | — | rebalance up |
| 2026-10-16T15:25 | Candlestick reversal · 1h | buy | SPY | 4.10 | — | rebalance up |
| 2026-10-16T15:25 | Candlestick reversal · 1h | buy | NVDA | 4.10 | — | rebalance up |
| 2026-10-16T15:25 | Candlestick reversal · 1h | buy | MSFT | 4.15 | — | rebalance up |
| 2026-10-16T15:25 | Candlestick reversal · 1h | buy | AMZN | 4.10 | — | rebalance up |
| 2026-10-16T15:25 | Candlestick reversal · 1h | sell | LABU | 5.50 | -0.46 | stop-loss |
| 2026-10-16T15:25 | Candlestick reversal · 1h | sell | GOOGL | 5.57 | -0.05 | stop-loss |
| 2026-10-16T15:25 | Triple EMA stack · 1h | sell | SOL-USD | 21.88 | -0.62 | stop-loss |
| 2026-10-16T15:25 | EMA 20/50 cross · 1h | sell | SOL-USD | 22.58 | -0.68 | stop-loss |
| 2026-10-16T15:25 | VWAP reversion | sell | LABU | 4.28 | -0.18 | stop-loss |
| 2026-10-16T15:20 | MFI reversion · 1h | buy | TNA | 6.95 | — | rebalance up |
| 2026-10-16T15:20 | MFI reversion · 1h | buy | AMZN | 6.73 | — | rebalance up |
| 2026-10-16T15:20 | MFI reversion · 1h | sell | MSFT | 17.16 | -0.07 | target is flat |
| 2026-10-16T15:20 | MFI reversion · 1h | sell | LABU | 13.75 | -1.01 | stop-loss |
| 2026-10-16T15:20 | VWAP reversion | buy | PLTR | 4.37 | — | entry signal |
| 2026-10-16T15:20 | VWAP reversion | sell | TNA | 4.38 | -0.04 | stop-loss |
| 2026-10-16T15:20 | RSI(14) reversion | sell | LABU | 7.11 | -0.17 | stop-loss |
| 2026-10-16T15:15 | VWAP reversion | buy | UPRO | 4.37 | — | entry signal |
| 2026-10-16T15:15 | VWAP reversion | buy | TQQQ | 4.39 | — | entry signal |
| 2026-10-16T15:15 | VWAP reversion | buy | TECL | 4.39 | — | entry signal |
| 2026-10-16T15:15 | VWAP reversion | buy | SPY | 4.39 | — | entry signal |
| 2026-10-16T15:15 | VWAP reversion | buy | QQQ | 4.39 | — | entry signal |
| 2026-10-16T15:15 | VWAP reversion | buy | MSFT | 4.39 | — | entry signal |
| 2026-10-16T15:15 | VWAP reversion | buy | DOGE-USD | 4.39 | — | entry signal |
| 2026-10-16T15:15 | VWAP reversion | buy | BTC-USD | 4.39 | — | entry signal |
| 2026-10-16T15:15 | VWAP reversion | sell | TSLA | 5.16 | -0.02 | rebalance down |
| 2026-10-16T15:15 | VWAP reversion | sell | TNA | 5.13 | -0.04 | rebalance down |
| 2026-10-16T15:15 | VWAP reversion | sell | MSTR | 5.05 | 0.02 | rebalance down |
| 2026-10-16T15:15 | VWAP reversion | sell | META | 5.18 | -0.02 | rebalance down |
| 2026-10-16T15:15 | VWAP reversion | sell | LABU | 5.06 | -0.09 | rebalance down |
| 2026-10-16T15:15 | VWAP reversion | sell | IWM | 9.48 | -0.01 | target is flat |
| 2026-10-16T15:15 | RSI(14) reversion | buy | SOL-USD | 7.18 | — | entry signal |
| 2026-10-16T15:15 | RSI(14) reversion | buy | MSTR | 7.20 | — | entry signal |
| 2026-10-16T15:15 | RSI(14) reversion | buy | ETH-USD | 7.20 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 15:25:05.000137+00:00 -> 2026-10-16 15:35:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
