# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T16:58:05.000130+00:00 · 54781 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.12 (-12.88%)

Closed trades 166, win rate 34.9%, fees £5.06, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 17.42 | -0.01 |
| TSLA | 17.42 | -0.01 |

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

Today: 19550 decisions in 2491 calls, $0.2541 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T16:58 | 0 / 15 / 15 | cash |  |
| Breezy | 2026-11-10T16:58 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-10T16:58 | 4 / 24 / 2 | COIN 51% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 1.91 | +7.15% | 4 |
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| MFI reversion | TSLA | 1.42 | +2.30% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.49 | 3.91 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.36 | 14.36 | 0 | — | 14.00 | 4.67 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.87 | 10.87 | 31 | 29.0 | 19.58 | 2.93 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.21 | 1.21 | 0 | — | 4.09 | 1.19 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.52 | 1.06 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.95 | -2.05 | 178 | 28.7 | -3.03 | -1.20 | -9.81 | 146 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.40 | -3.60 | 0 | — | -2.20 | -0.70 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.48 | -4.52 | 136 | 46.3 | -13.63 | -3.47 | -13.66 | 150 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.51 | -5.49 | 0 | — | -4.85 | -1.27 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.90 | -7.09 | 108 | 23.1 | -13.26 | -4.92 | -17.51 | 77 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.21 | -7.79 | 0 | — | -5.16 | -1.37 | -10.64 | 1 |
| 20 | Copy: Insider buying | copy | 92.16 | -7.84 | 42 | 38.1 | -8.81 | -1.83 | -15.11 | 67 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.74 | -11.26 | 402 | 33.3 | -14.66 | -4.55 | -14.70 | 604 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.29 | -2.88 | -14.15 | 77 |
| 24 | Daily: Bullish score | daily | 87.22 | -12.78 | 15 | 20.0 | -7.76 | -1.14 | -17.42 | 14 |
| 25 | Agent | meta | 87.12 | -12.88 | 166 | 34.9 | -13.30 | -6.83 | -14.16 | 205 |
| 26 | Parabolic SAR · 1h | trend | 85.35 | -14.65 | 167 | 26.9 | -13.46 | -2.73 | -21.42 | 224 |
| 27 | Hold BTC | benchmark | 85.26 | -14.74 | 1 | 0.0 | -7.76 | -1.05 | -16.51 | 1 |
| 28 | Agent (aggressive) | meta | 84.90 | -15.10 | 77 | 32.5 | -15.47 | -4.31 | -18.51 | 97 |
| 29 | Donchian 55/20 · 1h | breakout | 84.31 | -15.70 | 71 | 14.1 | -16.40 | -3.48 | -21.99 | 103 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 81.60 | -18.40 | 2 | 0.0 | -10.40 | -1.22 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.53 | -18.47 | 110 | 23.6 | -20.70 | -4.29 | -25.32 | 176 |
| 32 | Opening range 15m | breakout | 81.21 | -18.79 | 498 | 31.5 | -19.59 | -5.38 | -20.21 | 739 |
| 33 | Connors RSI(2) · 1h | reversion | 80.98 | -19.02 | 206 | 39.8 | -19.41 | -6.44 | -19.99 | 125 |
| 34 | Volume breakout · 1h | breakout | 80.51 | -19.49 | 146 | 27.4 | -15.06 | -3.51 | -21.74 | 93 |
| 35 | Stochastic reversion · 1h | reversion | 80.35 | -19.65 | 284 | 47.5 | -25.86 | -3.79 | -27.14 | 391 |
| 36 | Max aggression: 5-day momentum | meta | 79.60 | -20.40 | 18 | 44.4 | -36.86 | -2.36 | -45.81 | 25 |
| 37 | Heikin-Ashi · 1h | trend | 78.94 | -21.06 | 415 | 24.3 | -40.16 | -7.46 | -42.52 | 664 |
| 38 | ADX DI cross · 1h | trend | 78.84 | -21.16 | 182 | 19.2 | -24.66 | -4.25 | -29.47 | 268 |
| 39 | CCI reversion · 1h | reversion | 77.01 | -22.99 | 326 | 45.1 | -25.80 | -3.92 | -30.69 | 458 |
| 40 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.49 | -4.43 | -27.99 | 238 |
| 41 | MFI reversion · 1h | reversion | 76.76 | -23.24 | 359 | 33.7 | -19.27 | -2.45 | -21.69 | 158 |
| 42 | Ichimoku · 1h | trend | 75.67 | -24.33 | 99 | 15.2 | -31.24 | -8.87 | -31.40 | 121 |
| 43 | EMA 20/50 cross · 1h | trend | 74.94 | -25.06 | 102 | 10.8 | -23.60 | -4.15 | -33.20 | 121 |
| 44 | MACD cross · 1h | trend | 74.10 | -25.90 | 356 | 22.2 | -33.33 | -5.48 | -39.51 | 473 |
| 45 | Bollinger reversion · 1h | reversion | 73.50 | -26.50 | 278 | 40.3 | -27.45 | -4.23 | -32.28 | 369 |
| 46 | MACD zero-line · 1h | trend | 73.36 | -26.64 | 158 | 16.5 | -26.51 | -5.42 | -30.63 | 215 |
| 47 | Supertrend · 1h | trend | 73.00 | -27.00 | 168 | 13.1 | -33.14 | -5.95 | -35.92 | 232 |
| 48 | RSI momentum · 1h | momentum | 72.91 | -27.09 | 159 | 12.6 | -24.95 | -4.17 | -33.69 | 210 |
| 49 | Triple EMA stack · 1h | trend | 72.53 | -27.47 | 143 | 14.7 | -27.12 | -4.76 | -35.10 | 205 |
| 50 | OBV trend · 1h | momentum | 72.02 | -27.98 | 274 | 18.2 | -27.37 | -4.80 | -35.57 | 277 |
| 51 | Williams %R · 1h | reversion | 71.82 | -28.18 | 346 | 45.7 | -35.82 | -5.58 | -36.06 | 529 |
| 52 | Z-score reversion · 1h | reversion | 71.53 | -28.48 | 186 | 36.0 | -27.01 | -3.85 | -28.37 | 227 |
| 53 | ROC + volume · 1h | momentum | 70.76 | -29.24 | 358 | 26.8 | -36.76 | -7.05 | -38.79 | 379 |
| 54 | Donchian 20/10 · 1h | breakout | 70.62 | -29.38 | 142 | 19.7 | -31.37 | -5.78 | -35.64 | 209 |
| 55 | Daily: Momentum burst | daily | 70.24 | -29.76 | 27 | 11.1 | -39.16 | -5.62 | -39.44 | 34 |
| 56 | VWAP momentum · 1h | momentum | 66.41 | -33.59 | 836 | 22.0 | -53.35 | -11.36 | -54.39 | 1226 |
| 57 | RSI(14) reversion · 1h | reversion | 66.33 | -33.67 | 170 | 30.6 | -27.85 | -3.95 | -32.51 | 231 |
| 58 | Agent (ML meta-label) | meta | 65.31 | -34.69 | 1665 | 24.3 | -12.22 | -1.91 | -18.26 | 329 |
| 59 | EMA 9/21 cross · 1h | trend | 65.09 | -34.91 | 249 | 9.6 | -37.63 | -7.44 | -41.46 | 334 |
| 60 | Max aggression: 1-day momentum | meta | 65.04 | -34.96 | 27 | 25.9 | -32.96 | -1.68 | -57.50 | 41 |
| 61 | Candlestick reversal · 1h | reversion | 63.31 | -36.69 | 445 | 27.9 | -39.43 | -7.17 | -40.59 | 588 |
| 62 | Three white soldiers | momentum | 61.14 | -38.86 | 502 | 14.9 | -48.89 | -22.83 | -48.89 | 646 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.71 | -98.95 | 5263 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.84 | -25.87 | -79.93 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -44.63 | -93.23 | 2504 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.39 | -31.66 | -89.41 | 1917 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.72 | -38.59 | -90.73 | 2313 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.21 | -31.50 | -90.26 | 2201 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -52.57 | -97.77 | 3447 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.21 | -54.35 | -96.22 | 3417 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -32.43 | -93.66 | 2381 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.42 | -33.94 | -82.49 | 1673 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -54.14 | -99.56 | 6029 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.24 | -42.32 | -92.24 | 2595 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.53 | -36.81 | -95.53 | 3430 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.48 | -99.81 | 6158 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.99 | -42.07 | -91.99 | 2249 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.48 | -24.36 | -75.52 | 1594 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -58.33 | -97.73 | 3517 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -62.42 | -98.88 | 4899 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.53 | -26.80 | -68.99 | 1216 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -52.06 | -94.57 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.41 | -36.03 | -84.52 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -72.13 | -99.65 | 6361 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.83 | -31.56 | -89.84 | 2289 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.75 | -20.26 | -78.77 | 1778 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.95 | -36.52 | -90.95 | 2218 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.86 | -52.76 | -96.86 | 3891 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -56.01 | -89.40 | 2147 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.21 | -27.00 | -65.89 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.16 | -22.64 | -71.16 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.66 | -19.61 | -80.66 | 1711 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -49.18 | -97.28 | 4318 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -102.48 | -99.93 | 8288 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T16:56 | Agent (ML meta-label) | buy | TSLA | 7.26 | — | following Ichimoku, MFI reversion |
| 2026-11-10T16:56 | Agent (ML meta-label) | buy | SQQQ | 7.26 | — | following Stochastic reversion |
| 2026-11-10T16:56 | Agent (ML meta-label) | buy | META | 7.26 | — | entry |
| 2026-11-10T16:56 | Agent (ML meta-label) | sell | TECL | 4.56 | -0.07 | rebalance down |
| 2026-11-10T16:56 | Agent (ML meta-label) | sell | SPY | 4.63 | -0.01 | rebalance down |
| 2026-11-10T16:56 | Agent (ML meta-label) | sell | COIN | 4.57 | -0.08 | rebalance down |
| 2026-11-10T16:56 | Agent (ML meta-label) | sell | AMZN | 4.63 | -0.00 | rebalance down |
| 2026-11-10T16:56 | Agent (ML meta-label) | sell | AMD | 4.47 | -0.06 | rebalance down |
| 2026-11-10T16:56 | Agent (aggressive) | buy | LABU | 42.46 | — | following MFI reversion |
| 2026-11-10T16:56 | Agent | buy | TSLA | 17.43 | — | following Ichimoku, MFI reversion |
| 2026-11-10T16:56 | Agent | buy | LABU | 17.43 | — | following MFI reversion |
| 2026-11-10T16:56 | Keltner breakout · 1h | sell | AMD | 21.10 | 0.86 | stop-loss |
| 2026-11-10T16:56 | MACD cross · 1h | buy | UPRO | 4.30 | — | entry |
| 2026-11-10T16:56 | MACD cross · 1h | sell | COIN | 4.30 | -0.08 | stop-loss |
| 2026-11-10T16:56 | Opening range 15m | sell | META | 20.59 | -0.11 | stop-loss |
| 2026-11-10T16:50 | Agent | sell | TSLA | 17.38 | -0.06 | selected signal exited |
| 2026-11-10T16:50 | MACD zero-line · 1h | buy | QQQ | 11.63 | — | entry |
| 2026-11-10T16:50 | MACD zero-line · 1h | sell | LABU | 11.63 | -0.76 | stop-loss |
| 2026-11-10T16:50 | Opening range 30m | sell | META | 22.21 | -0.10 | stop-loss |
| 2026-11-10T16:50 | Opening range 15m | sell | SOXL | 19.77 | -1.04 | stop-loss |
| 2026-11-10T16:50 | Opening range 15m | sell | AMD | 20.41 | -0.40 | stop-loss |
| 2026-11-10T16:45 | Agent (ML meta-label) | buy | TECL | 3.75 | — | rebalance up |
| 2026-11-10T16:45 | Agent (ML meta-label) | buy | SPY | 11.91 | — | entry |
| 2026-11-10T16:45 | Agent (ML meta-label) | buy | SOXL | 6.30 | — | entry |
| 2026-11-10T16:45 | Agent (ML meta-label) | sell | COIN | 4.58 | -0.05 | rebalance down |
| 2026-11-10T16:45 | Agent (ML meta-label) | sell | AMZN | 4.55 | 0.00 | rebalance down |
| 2026-11-10T16:45 | Agent (ML meta-label) | sell | AMD | 4.54 | 0.01 | rebalance down |
| 2026-11-10T16:45 | Agent | buy | TSLA | 17.44 | — | following Ichimoku, MFI reversion |
| 2026-11-10T16:40 | Agent (ML meta-label) | buy | COIN | 8.24 | — | rebalance up |
| 2026-11-10T16:40 | Agent (ML meta-label) | buy | AMZN | 8.20 | — | rebalance up |
| 2026-11-10T16:40 | Agent (ML meta-label) | buy | AMD | 8.26 | — | rebalance up |
| 2026-11-10T16:40 | Agent (ML meta-label) | sell | TSLA | 8.23 | -0.01 | selected signal exited |
| 2026-11-10T16:40 | Agent (ML meta-label) | sell | SQQQ | 8.30 | 0.05 | selected signal exited |
| 2026-11-10T16:40 | Agent (ML meta-label) | sell | SPY | 8.24 | -0.02 | selected signal exited |
| 2026-11-10T16:40 | Agent (ML meta-label) | sell | META | 8.21 | -0.04 | selected signal exited |
| 2026-11-10T16:40 | Candlestick reversal · 1h | sell | COIN | 15.67 | -0.59 | stop-loss |
| 2026-11-10T16:35 | Agent (ML meta-label) | buy | TSLA | 8.24 | — | following Ichimoku, MFI reversion |
| 2026-11-10T16:35 | Agent (ML meta-label) | buy | TECL | 8.25 | — | entry |
| 2026-11-10T16:35 | Agent (ML meta-label) | buy | SQQQ | 8.25 | — | following Stochastic reversion |
| 2026-11-10T16:35 | Agent (ML meta-label) | buy | META | 8.25 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 16:58:05.000130+00:00 -> 2026-11-10 17:08:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
