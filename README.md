# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T14:55:05.000180+00:00 · 55891 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.31 (-12.69%)

Closed trades 172, win rate 35.5%, fees £5.18, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.28 | -0.21 |
| SQQQ | 34.95 | +0.06 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.57 · VIX 19.46 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 12822 decisions in 2259 calls, $0.1749 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T14:55 | 2 / 17 / 11 | cash |  |
| Breezy | 2026-11-11T14:55 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-11T14:55 | 4 / 24 / 2 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 20.23 | 4.05 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.57 | 14.57 | 0 | — | 14.57 | 4.79 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.83 | 11.83 | 32 | 28.1 | 20.19 | 3.00 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 4.06 | 1.05 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.23 | 3.23 | 0 | — | 5.76 | 1.61 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.24 | 0.24 | 132 | 34.8 | 10.95 | 3.78 | -2.84 | 84 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 5.26 | 1.53 | -9.06 | 238 |
| 11 | Hold SPY | benchmark | 97.97 | -2.03 | 0 | — | -0.40 | -0.06 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 97.83 | -2.17 | 180 | 28.3 | -2.28 | -0.80 | -9.01 | 168 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.72 | -3.28 | 0 | — | -2.50 | -0.59 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Insider buying | copy | 94.01 | -5.99 | 43 | 39.5 | -7.19 | -1.45 | -15.11 | 67 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.76 | -3.50 | -5.99 | 28 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 19 | Copy: Congress Democrats (NANC) | copy | 93.06 | -6.94 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 91.78 | -8.22 | 109 | 22.9 | -16.09 | -5.65 | -18.63 | 80 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -7.97 | -2.99 | -14.15 | 77 |
| 23 | Opening range 30m | breakout | 88.22 | -11.78 | 404 | 33.2 | -13.82 | -4.23 | -13.96 | 582 |
| 24 | Agent | meta | 87.31 | -12.69 | 172 | 35.5 | -13.54 | -6.89 | -14.32 | 203 |
| 25 | Parabolic SAR · 1h | trend | 86.43 | -13.57 | 168 | 26.8 | -14.02 | -2.94 | -21.98 | 224 |
| 26 | Hold BTC | benchmark | 86.33 | -13.66 | 1 | 0.0 | -5.11 | -0.64 | -16.64 | 1 |
| 27 | Daily: Bullish score | daily | 85.16 | -14.84 | 16 | 18.8 | -7.79 | -1.15 | -18.44 | 15 |
| 28 | Agent (aggressive) | meta | 85.15 | -14.85 | 81 | 33.3 | -15.36 | -4.25 | -18.51 | 95 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 85.14 | -14.86 | 2 | 0.0 | -5.40 | -0.50 | -24.16 | 1 |
| 30 | Donchian 55/20 · 1h | breakout | 83.23 | -16.77 | 71 | 14.1 | -23.41 | -4.95 | -28.39 | 100 |
| 31 | Max aggression: 5-day momentum | meta | 82.78 | -17.23 | 19 | 47.4 | -31.38 | -1.84 | -45.81 | 25 |
| 32 | Keltner breakout · 1h | breakout | 81.65 | -18.35 | 110 | 23.6 | -19.04 | -3.91 | -25.10 | 173 |
| 33 | Stochastic reversion · 1h | reversion | 81.40 | -18.60 | 287 | 47.7 | -24.78 | -3.60 | -27.09 | 391 |
| 34 | ADX DI cross · 1h | trend | 81.13 | -18.87 | 185 | 18.9 | -23.65 | -3.88 | -30.55 | 270 |
| 35 | Connors RSI(2) · 1h | reversion | 80.83 | -19.18 | 207 | 40.1 | -19.60 | -6.52 | -19.98 | 125 |
| 36 | Opening range 15m | breakout | 80.76 | -19.23 | 500 | 31.4 | -19.13 | -5.16 | -20.64 | 717 |
| 37 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -14.13 | -3.28 | -21.11 | 92 |
| 38 | Heikin-Ashi · 1h | trend | 79.47 | -20.53 | 417 | 24.5 | -39.58 | -7.29 | -42.23 | 665 |
| 39 | MFI reversion · 1h | reversion | 78.89 | -21.11 | 370 | 34.9 | -17.34 | -2.20 | -23.02 | 159 |
| 40 | MACD cross · 1h | trend | 77.01 | -22.99 | 360 | 21.9 | -30.64 | -4.91 | -39.51 | 479 |
| 41 | CCI reversion · 1h | reversion | 76.97 | -23.03 | 327 | 45.0 | -26.47 | -3.98 | -31.08 | 453 |
| 42 | Max aggression: 1-day momentum | meta | 76.73 | -23.27 | 27 | 25.9 | -22.00 | -0.80 | -57.50 | 40 |
| 43 | Bollinger breakout · 1h | breakout | 76.72 | -23.28 | 171 | 22.8 | -21.13 | -4.37 | -28.19 | 236 |
| 44 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.15 | -8.75 | -31.64 | 118 |
| 45 | MACD zero-line · 1h | trend | 74.97 | -25.03 | 159 | 16.4 | -22.22 | -4.41 | -31.04 | 208 |
| 46 | Supertrend · 1h | trend | 74.80 | -25.20 | 168 | 13.1 | -29.41 | -5.19 | -36.07 | 228 |
| 47 | EMA 20/50 cross · 1h | trend | 74.80 | -25.20 | 102 | 10.8 | -26.13 | -4.47 | -36.22 | 114 |
| 48 | Bollinger reversion · 1h | reversion | 74.66 | -25.34 | 283 | 41.0 | -25.99 | -3.96 | -32.54 | 371 |
| 49 | RSI momentum · 1h | momentum | 74.44 | -25.56 | 159 | 12.6 | -25.68 | -4.00 | -36.77 | 206 |
| 50 | Daily: Momentum burst | daily | 73.27 | -26.73 | 27 | 11.1 | -33.95 | -4.64 | -38.23 | 33 |
| 51 | Triple EMA stack · 1h | trend | 73.18 | -26.82 | 144 | 14.6 | -26.26 | -4.40 | -36.34 | 190 |
| 52 | ROC + volume · 1h | momentum | 72.16 | -27.84 | 373 | 27.6 | -34.48 | -6.34 | -38.75 | 380 |
| 53 | Williams %R · 1h | reversion | 71.75 | -28.25 | 350 | 45.7 | -35.12 | -5.49 | -36.28 | 532 |
| 54 | Donchian 20/10 · 1h | breakout | 71.35 | -28.65 | 142 | 19.7 | -30.81 | -5.70 | -35.64 | 206 |
| 55 | OBV trend · 1h | momentum | 71.27 | -28.73 | 278 | 18.3 | -28.35 | -5.15 | -35.23 | 284 |
| 56 | Z-score reversion · 1h | reversion | 70.51 | -29.49 | 190 | 36.3 | -23.90 | -3.35 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 68.00 | -32.00 | 171 | 31.0 | -27.05 | -3.96 | -32.54 | 238 |
| 58 | VWAP momentum · 1h | momentum | 67.17 | -32.83 | 844 | 21.9 | -52.77 | -10.73 | -54.74 | 1236 |
| 59 | EMA 9/21 cross · 1h | trend | 66.80 | -33.20 | 253 | 9.9 | -36.38 | -7.01 | -41.68 | 337 |
| 60 | Agent (ML meta-label) | meta | 66.44 | -33.56 | 1705 | 24.6 | -6.27 | -0.84 | -19.19 | 316 |
| 61 | Candlestick reversal · 1h | reversion | 64.28 | -35.73 | 455 | 28.6 | -37.86 | -6.88 | -40.47 | 593 |
| 62 | Three white soldiers | momentum | 60.26 | -39.74 | 513 | 14.6 | -49.30 | -22.65 | -49.30 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.05 | -45.10 | -99.05 | 5317 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.34 | -26.18 | -80.34 | 1436 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.66 | -45.93 | -93.66 | 2539 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.48 | -31.99 | -89.50 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.09 | -39.27 | -91.18 | 2339 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.33 | -32.02 | -90.34 | 2217 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.84 | -53.51 | -97.84 | 3477 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -57.98 | -96.44 | 3455 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.35 | -31.49 | -93.55 | 2345 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.09 | -34.23 | -83.21 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -53.15 | -99.54 | 5973 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.29 | -42.76 | -92.29 | 2619 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.59 | -37.25 | -95.59 | 3432 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.28 | -99.80 | 6141 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.08 | -43.25 | -92.08 | 2272 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.66 | -25.43 | -75.71 | 1636 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.30 | -97.75 | 3533 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -61.44 | -98.84 | 4896 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.65 | -26.97 | -69.04 | 1242 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -54.01 | -94.75 | 2791 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.99 | -37.30 | -85.21 | 1792 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.34 | -99.63 | 6336 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.40 | -31.46 | -89.47 | 2283 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.39 | -19.42 | -77.77 | 1742 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.49 | -35.58 | -90.62 | 2186 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.67 | -50.13 | -96.68 | 3835 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -53.97 | -89.07 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.66 | -27.84 | -66.53 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.31 | -22.56 | -71.80 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.46 | -18.38 | -78.66 | 1701 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.16 | -47.16 | -97.17 | 4288 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -100.19 | -99.93 | 8333 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T14:55 | Agent (ML meta-label) | buy | COIN | 3.42 | — | rebalance up |
| 2026-11-11T14:55 | Agent (ML meta-label) | buy | AMZN | 5.76 | — | rebalance up |
| 2026-11-11T14:55 | Agent (ML meta-label) | sell | SOXL | 13.40 | 0.14 | selected signal exited |
| 2026-11-11T14:55 | Agent (ML meta-label) | sell | META | 10.86 | -0.06 | selected signal exited |
| 2026-11-11T14:50 | Agent (ML meta-label) | buy | SOXL | 13.26 | — | entry |
| 2026-11-11T14:50 | Agent (ML meta-label) | buy | COIN | 3.63 | — | rebalance up |
| 2026-11-11T14:50 | Agent (ML meta-label) | buy | AMD | 3.81 | — | rebalance up |
| 2026-11-11T14:50 | Agent (ML meta-label) | sell | TSLA | 11.05 | 0.18 | selected signal exited |
| 2026-11-11T14:50 | Agent (ML meta-label) | sell | SPY | 11.06 | 0.14 | selected signal exited |
| 2026-11-11T14:50 | Agent | buy | SQQQ | 17.40 | — | rebalance up |
| 2026-11-11T14:50 | MFI reversion · 1h | sell | SPY | 13.15 | 0.11 | target is flat |
| 2026-11-11T14:50 | Opening range 15m | buy | SQQQ | 20.20 | — | entry signal |
| 2026-11-11T14:50 | Opening range 15m | buy | AAPL | 20.20 | — | entry signal |
| 2026-11-11T14:46 | Agent (rotation) | sell | NVDA | 8.02 | -0.13 | selected signal exited |
| 2026-11-11T14:46 | Day trade: Stocks in Play ORB | sell | NVDA | 24.67 | -0.41 | target is flat |
| 2026-11-11T14:46 | Agent (ML meta-label) | buy | TSLA | 4.37 | — | rebalance up |
| 2026-11-11T14:46 | Agent (ML meta-label) | sell | SOXL | 7.76 | -0.13 | selected signal exited |
| 2026-11-11T14:46 | Agent (aggressive) | buy | SQQQ | 42.49 | — | following Stochastic reversion, Williams %R |
| 2026-11-11T14:46 | Agent | buy | SQQQ | 17.48 | — | following Stochastic reversion, Williams %R |
| 2026-11-11T14:40 | Agent (rotation) | buy | SQQQ | 8.16 | — | following Stochastic reversion, Williams %R |
| 2026-11-11T14:40 | Agent (rotation) | buy | NVDA | 8.16 | — | entry |
| 2026-11-11T14:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 25.09 | — | entry |
| 2026-11-11T14:40 | Day trade: Stocks in Play ORB | buy | NVDA | 25.09 | — | entry |
| 2026-11-11T14:40 | Agent | buy | COIN | 17.49 | — | following Donchian 20/10 |
| 2026-11-11T14:35 | Max aggression: 5-day momentum | buy | SOXL | 83.31 | — | entry |
| 2026-11-11T14:35 | Max aggression: 5-day momentum | sell | AMD | 83.31 | 4.07 | target is flat |
| 2026-11-11T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 110.59 | — | entry |
| 2026-11-11T14:35 | Agent (ML meta-label) | buy | SOXL | 7.89 | — | entry |
| 2026-11-11T14:35 | Agent (ML meta-label) | sell | COIN | 3.81 | 0.09 | rebalance down |
| 2026-11-11T14:35 | Agent (ML meta-label) | sell | AMD | 4.07 | 0.17 | rebalance down |
| 2026-11-11T14:35 | Daily: Bullish score | buy | AMZN | 21.32 | — | entry |
| 2026-11-11T14:35 | Daily: Bullish score | sell | MSFT | 21.46 | -0.21 | target is flat |
| 2026-11-11T14:35 | MFI reversion · 1h | buy | TECL | 4.81 | — | rebalance up |
| 2026-11-11T14:35 | MFI reversion · 1h | buy | SPY | 5.36 | — | rebalance up |
| 2026-11-11T14:35 | MFI reversion · 1h | buy | ETHU | 13.18 | — | entry |
| 2026-11-11T14:35 | MFI reversion · 1h | buy | AMZN | 13.18 | — | entry |
| 2026-11-11T14:35 | MFI reversion · 1h | buy | AAPL | 5.36 | — | rebalance up |
| 2026-11-11T14:35 | MFI reversion · 1h | sell | TQQQ | 8.19 | 0.48 | target is flat |
| 2026-11-11T14:35 | MFI reversion · 1h | sell | SOXL | 8.70 | 0.99 | target is flat |
| 2026-11-11T14:35 | MFI reversion · 1h | sell | BITX | 7.68 | -0.03 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 14:55:05.000180+00:00 -> 2026-11-11 15:05:05.000180+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
