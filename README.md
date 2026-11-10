# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T20:25:05.000117+00:00 · 54962 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.45 (-12.55%)

Closed trades 170, win rate 35.3%, fees £5.12, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.48 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-10 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 35813 decisions in 3033 calls, $0.4440 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T20:25 | 9 / 17 / 4 | cash |  |
| Breezy | 2026-11-10T20:25 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-10T20:25 | 7 / 21 / 2 | MSTR 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.60 | +6.02% | 3 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| OBV trend | MSTR | 1.43 | +3.47% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 20.23 | 4.08 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.00 | 15.00 | 0 | — | 15.32 | 5.07 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.89 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.01 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.36 | 1.36 | 0 | — | 4.29 | 1.25 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.07 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.65 | 1.10 | -9.06 | 237 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -4.33 | -1.78 | -9.87 | 155 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.71 | -3.29 | 0 | — | -1.36 | -0.40 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 96.11 | -3.89 | 138 | 46.4 | -12.55 | -3.25 | -13.48 | 154 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.37 | -5.63 | 0 | — | -4.95 | -1.31 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.06 | -3.80 | -5.99 | 27 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.78 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.74 | -7.25 | 108 | 23.1 | -12.68 | -4.73 | -16.85 | 78 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.52 | -7.48 | 0 | — | -4.18 | -1.11 | -10.64 | 1 |
| 20 | Copy: Insider buying | copy | 92.50 | -7.50 | 43 | 39.5 | -8.37 | -1.74 | -15.11 | 67 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.69 | -2.67 | -15.49 | 78 |
| 23 | Opening range 30m | breakout | 88.22 | -11.78 | 404 | 33.2 | -15.00 | -4.61 | -15.00 | 604 |
| 24 | Agent | meta | 87.45 | -12.55 | 170 | 35.3 | -13.29 | -6.78 | -14.21 | 200 |
| 25 | Daily: Bullish score | daily | 86.48 | -13.52 | 15 | 20.0 | -4.84 | -0.64 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 86.05 | -13.95 | 1 | 0.0 | -6.28 | -0.79 | -16.64 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.54 | -14.46 | 168 | 26.8 | -13.58 | -2.78 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.95 | -15.05 | 79 | 32.9 | -15.84 | -4.48 | -18.49 | 93 |
| 29 | Donchian 55/20 · 1h | breakout | 84.19 | -15.81 | 71 | 14.1 | -22.37 | -4.75 | -27.94 | 100 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 81.75 | -18.25 | 2 | 0.0 | -8.98 | -1.03 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.73 | -18.27 | 110 | 23.6 | -17.96 | -3.67 | -24.55 | 165 |
| 32 | Stochastic reversion · 1h | reversion | 81.15 | -18.85 | 284 | 47.5 | -24.85 | -3.68 | -27.06 | 392 |
| 33 | Connors RSI(2) · 1h | reversion | 80.93 | -19.07 | 207 | 40.1 | -19.42 | -6.50 | -19.98 | 125 |
| 34 | Opening range 15m | breakout | 80.79 | -19.21 | 500 | 31.4 | -20.74 | -5.62 | -20.74 | 733 |
| 35 | Max aggression: 5-day momentum | meta | 80.65 | -19.35 | 18 | 44.4 | -35.99 | -2.28 | -45.81 | 25 |
| 36 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -15.25 | -3.56 | -22.08 | 93 |
| 37 | ADX DI cross · 1h | trend | 79.11 | -20.89 | 185 | 18.9 | -26.60 | -4.66 | -30.45 | 278 |
| 38 | Heikin-Ashi · 1h | trend | 78.90 | -21.10 | 416 | 24.5 | -40.29 | -7.54 | -42.60 | 664 |
| 39 | MFI reversion · 1h | reversion | 77.07 | -22.93 | 362 | 34.3 | -17.58 | -2.24 | -22.46 | 159 |
| 40 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.39 | -4.47 | -27.99 | 235 |
| 41 | CCI reversion · 1h | reversion | 76.83 | -23.17 | 326 | 45.1 | -26.52 | -4.00 | -30.85 | 453 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.26 | -8.88 | -31.64 | 119 |
| 43 | EMA 20/50 cross · 1h | trend | 75.11 | -24.89 | 102 | 10.8 | -26.19 | -4.48 | -36.26 | 118 |
| 44 | MACD cross · 1h | trend | 74.83 | -25.17 | 360 | 21.9 | -31.74 | -5.21 | -39.47 | 471 |
| 45 | Bollinger reversion · 1h | reversion | 74.12 | -25.88 | 278 | 40.3 | -26.30 | -4.03 | -32.30 | 371 |
| 46 | MACD zero-line · 1h | trend | 73.94 | -26.06 | 159 | 16.4 | -25.17 | -5.11 | -31.08 | 214 |
| 47 | RSI momentum · 1h | momentum | 73.48 | -26.52 | 159 | 12.6 | -25.21 | -4.11 | -34.73 | 209 |
| 48 | Supertrend · 1h | trend | 73.48 | -26.52 | 168 | 13.1 | -29.97 | -5.22 | -36.14 | 227 |
| 49 | Triple EMA stack · 1h | trend | 72.39 | -27.61 | 144 | 14.6 | -27.77 | -4.90 | -36.37 | 206 |
| 50 | OBV trend · 1h | momentum | 71.84 | -28.16 | 276 | 18.5 | -28.17 | -5.13 | -35.53 | 281 |
| 51 | Williams %R · 1h | reversion | 71.73 | -28.27 | 346 | 45.7 | -35.82 | -5.65 | -36.23 | 534 |
| 52 | ROC + volume · 1h | momentum | 71.32 | -28.68 | 363 | 26.7 | -35.07 | -6.66 | -38.08 | 378 |
| 53 | Donchian 20/10 · 1h | breakout | 71.03 | -28.97 | 142 | 19.7 | -30.57 | -5.73 | -35.64 | 204 |
| 54 | Daily: Momentum burst | daily | 70.96 | -29.04 | 27 | 11.1 | -34.94 | -4.93 | -38.23 | 34 |
| 55 | Z-score reversion · 1h ⏸ | reversion | 70.59 | -29.41 | 190 | 36.3 | -25.97 | -3.78 | -28.98 | 233 |
| 56 | Max aggression: 1-day momentum | meta | 68.29 | -31.71 | 27 | 25.9 | -29.57 | -1.44 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 66.67 | -33.33 | 170 | 30.6 | -31.38 | -4.83 | -33.96 | 233 |
| 58 | VWAP momentum · 1h | momentum | 65.87 | -34.12 | 839 | 21.9 | -53.86 | -11.53 | -54.91 | 1214 |
| 59 | Agent (ML meta-label) | meta | 65.61 | -34.39 | 1699 | 24.5 | -9.30 | -1.32 | -20.17 | 328 |
| 60 | EMA 9/21 cross · 1h | trend | 65.50 | -34.50 | 252 | 9.9 | -37.42 | -7.56 | -41.74 | 335 |
| 61 | Candlestick reversal · 1h | reversion | 63.89 | -36.11 | 446 | 28.0 | -38.35 | -7.10 | -40.12 | 591 |
| 62 | Three white soldiers | momentum | 60.63 | -39.37 | 510 | 14.7 | -49.18 | -23.00 | -49.18 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -46.10 | -98.96 | 5254 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.58 | -26.46 | -79.61 | 1426 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.26 | -47.35 | -93.28 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.23 | -32.44 | -89.30 | 1920 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.75 | -40.33 | -90.80 | 2329 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.24 | -32.73 | -90.33 | 2217 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -55.19 | -97.78 | 3467 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.13 | -58.20 | -96.13 | 3407 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -33.51 | -93.60 | 2356 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.45 | -35.10 | -82.47 | 1668 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -55.53 | -99.55 | 5973 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.17 | -43.66 | -92.22 | 2616 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -37.72 | -95.56 | 3431 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.17 | -99.80 | 6167 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.01 | -44.03 | -92.06 | 2275 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.49 | -24.87 | -75.50 | 1586 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -63.96 | -97.74 | 3534 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.85 | -63.74 | -98.86 | 4896 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.66 | -27.66 | -69.09 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -55.63 | -94.58 | 2783 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.41 | -37.43 | -84.54 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -74.83 | -99.65 | 6344 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.67 | -32.64 | -89.83 | 2293 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.50 | -20.07 | -78.79 | 1752 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.51 | -37.19 | -90.71 | 2197 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.77 | -52.61 | -96.80 | 3855 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.34 | -58.86 | -89.44 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.46 | -27.93 | -66.14 | 802 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.25 | -23.07 | -71.25 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.66 | -19.36 | -79.92 | 1690 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.20 | -49.50 | -97.24 | 4284 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -117.95 | -99.93 | 8323 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T20:25 | Opening range 30m | sell | SQQQ | 21.73 | -0.45 | stop-loss |
| 2026-11-10T20:20 | Agent (aggressive) | buy | COIN | 42.49 | — | following Donchian 20/10 |
| 2026-11-10T20:20 | Agent | buy | COIN | 17.49 | — | following Donchian 20/10 |
| 2026-11-10T20:05 | Agent (ML meta-label) | sell | AMZN | 13.12 | 0.08 | selected signal exited |
| 2026-11-10T20:05 | Agent | sell | TSLA | 17.46 | -0.04 | selected signal exited |
| 2026-11-10T20:01 | CCI reversion · 1h | buy | ETH-USD | 3.84 | — | rebalance up |
| 2026-11-10T20:01 | CCI reversion · 1h | sell | COIN | 3.84 | -0.08 | rebalance down |
| 2026-11-10T20:00 | Agent (ML meta-label) | buy | SPY | 12.08 | — | rebalance up |
| 2026-11-10T20:00 | Agent (ML meta-label) | buy | COIN | 3.29 | — | rebalance up |
| 2026-11-10T20:00 | Agent (ML meta-label) | sell | TECL | 10.92 | 0.03 | selected signal exited |
| 2026-11-10T20:00 | Agent (ML meta-label) | sell | META | 10.91 | -0.01 | selected signal exited |
| 2026-11-10T20:00 | MFI reversion · 1h | buy | NVDA | 12.76 | — | entry |
| 2026-11-10T20:00 | MFI reversion · 1h | sell | BITX | 12.76 | 0.04 | target is flat |
| 2026-11-10T20:00 | CCI reversion · 1h | buy | ETH-USD | 8.16 | — | entry signal |
| 2026-11-10T20:00 | CCI reversion · 1h | sell | SQQQ | 4.31 | 0.08 | rebalance down |
| 2026-11-10T20:00 | CCI reversion · 1h | sell | NVDA | 3.86 | -0.02 | rebalance down |
| 2026-11-10T20:00 | OBV trend · 1h | buy | IWM | 3.53 | — | rebalance up |
| 2026-11-10T20:00 | OBV trend · 1h | buy | AAPL | 14.38 | — | entry |
| 2026-11-10T20:00 | OBV trend · 1h | sell | AMD | 17.91 | 0.11 | target is flat |
| 2026-11-10T20:00 | ROC + volume · 1h | buy | PLTR | 5.47 | — | entry |
| 2026-11-10T20:00 | ROC + volume · 1h | sell | AMD | 5.49 | 0.04 | target is flat |
| 2026-11-10T20:00 | VWAP momentum · 1h | buy | TNA | 6.52 | — | rebalance up |
| 2026-11-10T20:00 | VWAP momentum · 1h | buy | SQQQ | 3.32 | — | rebalance up |
| 2026-11-10T20:00 | VWAP momentum · 1h | sell | XRP-USD | 16.35 | -0.20 | exit signal |
| 2026-11-10T19:56 | Agent (ML meta-label) | buy | SPY | 4.31 | — | entry |
| 2026-11-10T19:56 | Agent (ML meta-label) | buy | META | 10.92 | — | entry |
| 2026-11-10T19:56 | Agent (ML meta-label) | sell | TECL | 5.48 | 0.01 | rebalance down |
| 2026-11-10T19:50 | Agent (ML meta-label) | buy | TECL | 3.31 | — | rebalance up |
| 2026-11-10T19:50 | Agent (ML meta-label) | sell | META | 13.06 | -0.02 | selected signal exited |
| 2026-11-10T19:50 | Opening range 15m | sell | SQQQ | 19.95 | -0.35 | exit signal |
| 2026-11-10T19:45 | Agent (ML meta-label) | buy | TECL | 13.05 | — | entry |
| 2026-11-10T19:45 | Agent (ML meta-label) | buy | COIN | 13.07 | — | following Donchian 20/10 |
| 2026-11-10T19:45 | Agent (ML meta-label) | sell | SPY | 16.33 | 0.00 | selected signal exited |
| 2026-11-10T19:45 | Agent (ML meta-label) | sell | AMD | 3.29 | -0.00 | rebalance down |
| 2026-11-10T19:40 | Agent (ML meta-label) | buy | SPY | 5.45 | — | rebalance up |
| 2026-11-10T19:40 | Agent (ML meta-label) | buy | AMD | 3.30 | — | rebalance up |
| 2026-11-10T19:40 | Agent (ML meta-label) | sell | COIN | 13.06 | -0.02 | selected signal exited |
| 2026-11-10T19:40 | MFI reversion · 1h | buy | BITX | 12.72 | — | entry |
| 2026-11-10T19:40 | MFI reversion · 1h | sell | ETHU | 12.72 | 0.03 | target is flat |
| 2026-11-10T19:35 | Agent (ML meta-label) | buy | META | 13.08 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 20:25:05.000117+00:00 -> 2026-11-10 20:35:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
