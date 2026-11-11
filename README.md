# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T15:54:05.000170+00:00 · 55926 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.47 (-13.54%)

Closed trades 174, win rate 35.1%, fees £5.21, max drawdown -13.93%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.35 | +0.01 |

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

Today: 16005 decisions in 2364 calls, $0.2120 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T15:54 | 5 / 21 / 4 | AMD 16%, SOXL 15% |  |
| Breezy | 2026-11-11T15:54 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-11T15:54 | 7 / 22 / 1 | COIN 79% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.11 | 3.83 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.50 | 14.49 | 0 | — | 14.22 | 4.67 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.67 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.73 | 0.98 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.25 | 3.25 | 0 | — | 5.66 | 1.58 | -6.60 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.95 | -0.05 | 133 | 34.6 | 10.39 | 3.58 | -3.34 | 86 |
| 9 | Gap and go | momentum | 99.12 | -0.88 | 183 | 30.6 | 5.80 | 1.67 | -9.06 | 245 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.30 | -1.70 | 0 | — | -0.26 | -0.01 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.03 | -1.97 | 181 | 28.2 | -2.23 | -0.79 | -8.97 | 168 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.19 | -3.81 | 0 | — | -3.14 | -0.78 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Insider buying | copy | 94.17 | -5.83 | 43 | 39.5 | -7.12 | -1.43 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.13 | -5.87 | 0 | — | -3.60 | -0.93 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.76 | -3.50 | -5.99 | 28 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.61 | -8.39 | 109 | 22.9 | -16.28 | -5.70 | -18.84 | 80 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.23 | -2.86 | -14.15 | 76 |
| 23 | Opening range 30m | breakout | 88.60 | -11.40 | 404 | 33.2 | -13.58 | -4.15 | -14.11 | 591 |
| 24 | Max aggression: 5-day momentum | meta | 87.72 | -12.28 | 19 | 47.4 | -27.37 | -1.43 | -45.81 | 25 |
| 25 | Hold BTC | benchmark | 86.94 | -13.06 | 1 | 0.0 | -4.35 | -0.52 | -16.64 | 1 |
| 26 | Agent | meta | 86.47 | -13.54 | 174 | 35.1 | -15.27 | -7.90 | -15.36 | 204 |
| 27 | Parabolic SAR · 1h | trend | 86.36 | -13.64 | 168 | 26.8 | -14.39 | -3.04 | -21.98 | 225 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 84.95 | -15.04 | 2 | 0.0 | -5.35 | -0.50 | -24.16 | 1 |
| 29 | Daily: Bullish score | daily | 84.51 | -15.49 | 16 | 18.8 | -8.14 | -1.20 | -19.04 | 15 |
| 30 | Agent (aggressive) | meta | 84.15 | -15.85 | 82 | 32.9 | -19.16 | -5.54 | -19.50 | 97 |
| 31 | Donchian 55/20 · 1h | breakout | 83.11 | -16.89 | 72 | 13.9 | -23.22 | -4.85 | -28.84 | 97 |
| 32 | ADX DI cross · 1h | trend | 82.47 | -17.53 | 185 | 18.9 | -22.64 | -3.62 | -30.55 | 274 |
| 33 | Keltner breakout · 1h | breakout | 82.15 | -17.85 | 110 | 23.6 | -19.14 | -3.97 | -25.10 | 179 |
| 34 | Stochastic reversion · 1h | reversion | 82.06 | -17.94 | 288 | 47.9 | -24.41 | -3.49 | -27.27 | 392 |
| 35 | Max aggression: 1-day momentum | meta | 81.31 | -18.69 | 27 | 25.9 | -17.43 | -0.42 | -57.50 | 40 |
| 36 | Volume breakout · 1h | breakout | 80.80 | -19.20 | 147 | 27.2 | -13.50 | -3.10 | -21.11 | 95 |
| 37 | Opening range 15m | breakout | 80.70 | -19.30 | 501 | 31.3 | -19.27 | -5.21 | -21.11 | 726 |
| 38 | Connors RSI(2) · 1h | reversion | 80.36 | -19.64 | 208 | 39.9 | -20.06 | -6.68 | -20.11 | 126 |
| 39 | Heikin-Ashi · 1h | trend | 80.28 | -19.72 | 417 | 24.5 | -38.69 | -7.02 | -41.93 | 674 |
| 40 | MFI reversion · 1h | reversion | 79.69 | -20.32 | 371 | 35.0 | -16.82 | -2.10 | -23.02 | 158 |
| 41 | MACD cross · 1h | trend | 78.08 | -21.92 | 362 | 22.1 | -28.24 | -4.39 | -38.78 | 475 |
| 42 | CCI reversion · 1h | reversion | 77.76 | -22.24 | 328 | 44.8 | -26.86 | -4.07 | -31.08 | 452 |
| 43 | Bollinger breakout · 1h | breakout | 77.47 | -22.53 | 171 | 22.8 | -20.58 | -4.20 | -28.24 | 240 |
| 44 | MACD zero-line · 1h | trend | 75.68 | -24.32 | 160 | 16.9 | -21.50 | -4.19 | -31.04 | 213 |
| 45 | Bollinger reversion · 1h | reversion | 75.60 | -24.39 | 284 | 41.2 | -25.05 | -3.76 | -32.54 | 371 |
| 46 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 47 | Supertrend · 1h | trend | 75.27 | -24.73 | 168 | 13.1 | -28.70 | -4.98 | -36.07 | 228 |
| 48 | EMA 20/50 cross · 1h | trend | 75.09 | -24.91 | 102 | 10.8 | -26.05 | -4.45 | -36.29 | 114 |
| 49 | RSI momentum · 1h | momentum | 74.90 | -25.10 | 159 | 12.6 | -25.79 | -3.90 | -37.25 | 214 |
| 50 | Daily: Momentum burst | daily | 74.42 | -25.58 | 27 | 11.1 | -32.70 | -4.35 | -38.23 | 33 |
| 51 | Triple EMA stack · 1h | trend | 73.89 | -26.11 | 144 | 14.6 | -27.23 | -4.53 | -36.72 | 210 |
| 52 | ROC + volume · 1h | momentum | 73.00 | -27.00 | 376 | 27.7 | -33.79 | -6.08 | -39.15 | 385 |
| 53 | Williams %R · 1h | reversion | 72.74 | -27.26 | 350 | 45.7 | -35.06 | -5.46 | -36.47 | 530 |
| 54 | Donchian 20/10 · 1h | breakout | 72.21 | -27.79 | 142 | 19.7 | -29.65 | -5.41 | -35.64 | 214 |
| 55 | Z-score reversion · 1h | reversion | 71.68 | -28.32 | 193 | 37.3 | -22.58 | -3.05 | -28.98 | 234 |
| 56 | OBV trend · 1h | momentum | 71.66 | -28.34 | 279 | 18.6 | -26.95 | -4.83 | -34.77 | 285 |
| 57 | RSI(14) reversion · 1h | reversion | 68.95 | -31.05 | 172 | 31.4 | -29.07 | -4.39 | -33.18 | 225 |
| 58 | VWAP momentum · 1h | momentum | 68.08 | -31.92 | 849 | 22.0 | -51.74 | -10.46 | -54.46 | 1232 |
| 59 | EMA 9/21 cross · 1h | trend | 67.32 | -32.68 | 253 | 9.9 | -35.56 | -6.71 | -41.68 | 339 |
| 60 | Agent (ML meta-label) | meta | 67.21 | -32.79 | 1717 | 24.8 | -12.18 | -1.72 | -20.92 | 323 |
| 61 | Candlestick reversal · 1h | reversion | 65.06 | -34.95 | 457 | 28.4 | -36.37 | -6.58 | -39.86 | 583 |
| 62 | Three white soldiers | momentum | 60.27 | -39.73 | 513 | 14.6 | -49.29 | -22.65 | -49.31 | 654 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.05 | -45.17 | -99.06 | 5352 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.17 | -26.01 | -80.29 | 1433 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.58 | -45.45 | -93.60 | 2550 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.34 | -31.58 | -89.40 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.99 | -38.88 | -91.18 | 2344 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.37 | -32.26 | -90.40 | 2213 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -52.76 | -97.84 | 3463 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -57.74 | -96.46 | 3463 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.33 | -31.58 | -93.52 | 2345 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.03 | -33.88 | -83.28 | 1683 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -53.61 | -99.54 | 5974 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.35 | -43.19 | -92.38 | 2631 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -37.30 | -95.56 | 3425 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.12 | -99.80 | 6153 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.05 | -43.02 | -92.10 | 2277 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.16 | -25.17 | -75.42 | 1643 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -59.59 | -97.76 | 3537 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -61.28 | -98.84 | 4890 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.43 | -26.59 | -69.04 | 1245 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -54.39 | -94.77 | 2795 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.10 | -38.12 | -85.29 | 1798 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.57 | -99.63 | 6318 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.46 | -31.68 | -89.46 | 2285 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.59 | -19.57 | -77.90 | 1754 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.72 | -35.62 | -90.72 | 2174 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.70 | -50.75 | -96.70 | 3831 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -54.01 | -89.07 | 2130 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.63 | -27.78 | -66.56 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.13 | -22.32 | -71.96 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.30 | -18.38 | -78.56 | 1687 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.17 | -47.64 | -97.18 | 4276 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -101.17 | -99.93 | 8349 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T15:50 | Agent (aggressive) | sell | SQQQ | 41.64 | -0.85 | selected signal exited |
| 2026-11-11T15:50 | Agent | sell | SQQQ | 17.23 | -0.39 | selected signal exited |
| 2026-11-11T15:50 | CCI reversion · 1h | buy | DOGE-USD | 6.74 | — | rebalance up |
| 2026-11-11T15:50 | CCI reversion · 1h | sell | SQQQ | 10.26 | -0.59 | stop-loss |
| 2026-11-11T15:50 | Stochastic reversion · 1h | sell | SQQQ | 8.22 | -0.41 | stop-loss |
| 2026-11-11T15:46 | Agent (rotation) | buy | TQQQ | 4.65 | — | entry |
| 2026-11-11T15:46 | Agent (rotation) | buy | QQQ | 4.65 | — | entry |
| 2026-11-11T15:46 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 109.59 | -1.00 | target is flat |
| 2026-11-11T15:46 | Agent (ML meta-label) | buy | AMD | 16.77 | — | entry |
| 2026-11-11T15:46 | Agent (aggressive) | buy | COIN | 42.16 | — | following Donchian 20/10 |
| 2026-11-11T15:46 | Agent | sell | SQQQ | 16.95 | -0.32 | rebalance down |
| 2026-11-11T15:46 | Opening range 30m | buy | QQQ | 3.67 | — | entry signal |
| 2026-11-11T15:46 | Opening range 15m | buy | TQQQ | 8.03 | — | entry signal |
| 2026-11-11T15:46 | Opening range 15m | buy | TECL | 8.04 | — | entry |
| 2026-11-11T15:46 | Opening range 15m | buy | QQQ | 8.04 | — | entry signal |
| 2026-11-11T15:46 | Opening range 15m | buy | COIN | 8.04 | — | entry |
| 2026-11-11T15:46 | Opening range 15m | sell | TSLA | 5.32 | 0.01 | rebalance down |
| 2026-11-11T15:46 | Opening range 15m | sell | SOXL | 5.48 | 0.02 | rebalance down |
| 2026-11-11T15:46 | Opening range 15m | sell | ETHU | 5.29 | -0.02 | rebalance down |
| 2026-11-11T15:46 | Opening range 15m | sell | BITX | 5.31 | -0.02 | rebalance down |
| 2026-11-11T15:46 | Opening range 15m | sell | AMD | 5.39 | 0.00 | rebalance down |
| 2026-11-11T15:46 | Opening range 15m | sell | AAPL | 5.37 | 0.00 | rebalance down |
| 2026-11-11T15:46 | Gap and go | buy | TQQQ | 14.09 | — | entry signal |
| 2026-11-11T15:46 | Gap and go | buy | QQQ | 14.09 | — | entry signal |
| 2026-11-11T15:46 | Gap and go | sell | TSLA | 10.58 | 0.01 | rebalance down |
| 2026-11-11T15:46 | Gap and go | sell | SOXL | 10.64 | 0.03 | rebalance down |
| 2026-11-11T15:46 | Gap and go | sell | NVDA | 5.55 | -0.02 | rebalance down |
| 2026-11-11T15:46 | Gap and go | sell | AMD | 5.61 | 0.00 | rebalance down |
| 2026-11-11T15:41 | Agent (rotation) | buy | TECL | 6.51 | — | entry |
| 2026-11-11T15:41 | Agent (rotation) | buy | NVDA | 6.51 | — | entry |
| 2026-11-11T15:41 | Agent (rotation) | sell | SQQQ | 8.12 | -0.03 | selected signal exited |
| 2026-11-11T15:41 | Day trade: Stocks in Play ORB | sell | SQQQ | 24.99 | -0.10 | target is flat |
| 2026-11-11T15:41 | Agent (ML meta-label) | sell | TSLA | 16.68 | -0.09 | selected signal exited |
| 2026-11-11T15:41 | Agent (ML meta-label) | sell | AMD | 13.71 | 0.74 | selected signal exited |
| 2026-11-11T15:41 | Agent | buy | COIN | 17.34 | — | following Donchian 20/10 |
| 2026-11-11T15:41 | Three white soldiers | buy | COIN | 15.07 | — | entry signal |
| 2026-11-11T15:41 | Opening range 30m | buy | TECL | 12.60 | — | entry signal |
| 2026-11-11T15:41 | Opening range 30m | buy | COIN | 12.60 | — | entry signal |
| 2026-11-11T15:41 | Opening range 30m | sell | TSLA | 4.94 | -0.01 | rebalance down |
| 2026-11-11T15:41 | Opening range 30m | sell | SOXL | 9.42 | -0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 15:54:05.000170+00:00 -> 2026-11-11 16:04:05.000170+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
