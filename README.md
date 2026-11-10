# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T17:28:05.000140+00:00 · 54800 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.33 (-12.68%)

Closed trades 167, win rate 34.7%, fees £5.07, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 17.64 | +0.21 |

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

Today: 21275 decisions in 2548 calls, $0.2743 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T17:28 | 5 / 16 / 9 | cash |  |
| Breezy | 2026-11-10T17:28 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-10T17:28 | 5 / 22 / 3 | COIN 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.60 | +6.02% | 3 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.49 | 3.91 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.69 | 14.69 | 0 | — | 14.35 | 4.77 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.87 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.41 | 1.41 | 0 | — | 4.18 | 1.21 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.52 | 1.06 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -3.32 | -1.32 | -9.96 | 145 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.50 | -3.50 | 0 | — | -2.19 | -0.70 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.49 | -4.51 | 136 | 46.3 | -13.63 | -3.47 | -13.73 | 151 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.62 | -5.38 | 0 | — | -4.85 | -1.27 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.97 | -7.03 | 108 | 23.1 | -13.25 | -4.92 | -17.51 | 77 |
| 19 | Copy: Insider buying | copy | 92.60 | -7.40 | 42 | 38.1 | -8.34 | -1.72 | -15.11 | 67 |
| 20 | Copy: Congress Democrats (NANC) | copy | 92.31 | -7.69 | 0 | — | -5.16 | -1.37 | -10.64 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.78 | -11.22 | 402 | 33.3 | -14.66 | -4.55 | -14.77 | 605 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.28 | -2.87 | -14.15 | 77 |
| 24 | Agent | meta | 87.33 | -12.68 | 167 | 34.7 | -13.59 | -6.96 | -14.59 | 202 |
| 25 | Daily: Bullish score | daily | 87.14 | -12.86 | 15 | 20.0 | -8.09 | -1.20 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 85.41 | -14.59 | 1 | 0.0 | -7.53 | -1.02 | -16.58 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.38 | -14.62 | 167 | 26.9 | -13.50 | -2.74 | -21.46 | 224 |
| 28 | Agent (aggressive) | meta | 84.98 | -15.02 | 79 | 32.9 | -15.53 | -4.33 | -18.49 | 95 |
| 29 | Donchian 55/20 · 1h | breakout | 84.50 | -15.50 | 71 | 14.1 | -16.27 | -3.45 | -22.01 | 103 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 81.75 | -18.25 | 2 | 0.0 | -10.18 | -1.19 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.61 | -18.39 | 110 | 23.6 | -21.16 | -4.37 | -25.32 | 176 |
| 32 | Opening range 15m | breakout | 81.24 | -18.76 | 498 | 31.5 | -19.59 | -5.38 | -20.32 | 740 |
| 33 | Connors RSI(2) · 1h | reversion | 81.02 | -18.98 | 206 | 39.8 | -19.39 | -6.43 | -19.99 | 125 |
| 34 | Stochastic reversion · 1h | reversion | 80.60 | -19.40 | 284 | 47.5 | -25.59 | -3.75 | -27.04 | 391 |
| 35 | Volume breakout · 1h | breakout | 80.43 | -19.57 | 146 | 27.4 | -15.17 | -3.54 | -21.85 | 93 |
| 36 | Max aggression: 5-day momentum | meta | 79.26 | -20.74 | 18 | 44.4 | -37.20 | -2.39 | -45.81 | 25 |
| 37 | Heikin-Ashi · 1h | trend | 78.86 | -21.14 | 415 | 24.3 | -40.17 | -7.47 | -42.45 | 664 |
| 38 | ADX DI cross · 1h | trend | 78.62 | -21.38 | 182 | 19.2 | -24.91 | -4.27 | -29.74 | 268 |
| 39 | CCI reversion · 1h | reversion | 77.19 | -22.81 | 326 | 45.1 | -25.78 | -3.91 | -30.69 | 457 |
| 40 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.48 | -4.43 | -27.99 | 238 |
| 41 | MFI reversion · 1h | reversion | 76.69 | -23.30 | 359 | 33.7 | -19.38 | -2.46 | -21.69 | 158 |
| 42 | Ichimoku · 1h | trend | 75.50 | -24.50 | 99 | 15.2 | -31.42 | -8.89 | -31.52 | 121 |
| 43 | EMA 20/50 cross · 1h | trend | 75.12 | -24.88 | 102 | 10.8 | -23.35 | -4.09 | -33.19 | 121 |
| 44 | MACD cross · 1h | trend | 74.09 | -25.91 | 356 | 22.2 | -33.44 | -5.50 | -39.51 | 472 |
| 45 | Bollinger reversion · 1h | reversion | 73.50 | -26.50 | 278 | 40.3 | -27.45 | -4.23 | -32.28 | 369 |
| 46 | MACD zero-line · 1h | trend | 73.44 | -26.56 | 158 | 16.5 | -26.47 | -5.42 | -30.65 | 215 |
| 47 | Supertrend · 1h | trend | 73.06 | -26.94 | 168 | 13.1 | -33.35 | -6.03 | -35.96 | 233 |
| 48 | RSI momentum · 1h | momentum | 73.00 | -27.00 | 159 | 12.6 | -25.01 | -4.19 | -33.74 | 210 |
| 49 | Triple EMA stack · 1h | trend | 72.47 | -27.53 | 143 | 14.7 | -27.14 | -4.76 | -35.20 | 204 |
| 50 | OBV trend · 1h | momentum | 71.94 | -28.06 | 274 | 18.2 | -27.35 | -4.79 | -35.69 | 277 |
| 51 | Williams %R · 1h | reversion | 71.92 | -28.08 | 346 | 45.7 | -35.67 | -5.57 | -36.02 | 529 |
| 52 | Z-score reversion · 1h | reversion | 71.28 | -28.72 | 186 | 36.0 | -27.35 | -3.87 | -28.38 | 227 |
| 53 | ROC + volume · 1h | momentum | 70.78 | -29.22 | 358 | 26.8 | -36.58 | -6.96 | -38.63 | 379 |
| 54 | Donchian 20/10 · 1h | breakout | 70.62 | -29.38 | 142 | 19.7 | -31.34 | -5.78 | -35.64 | 209 |
| 55 | Daily: Momentum burst | daily | 70.25 | -29.75 | 27 | 11.1 | -39.30 | -5.64 | -39.35 | 34 |
| 56 | VWAP momentum · 1h | momentum | 66.43 | -33.57 | 836 | 22.0 | -53.28 | -11.32 | -54.39 | 1224 |
| 57 | RSI(14) reversion · 1h | reversion | 66.20 | -33.80 | 170 | 30.6 | -27.12 | -3.79 | -32.51 | 229 |
| 58 | Agent (ML meta-label) | meta | 65.20 | -34.80 | 1674 | 24.3 | -15.90 | -2.67 | -21.59 | 312 |
| 59 | EMA 9/21 cross · 1h | trend | 65.14 | -34.86 | 249 | 9.6 | -37.70 | -7.46 | -41.52 | 334 |
| 60 | Max aggression: 1-day momentum | meta | 64.79 | -35.21 | 27 | 25.9 | -33.29 | -1.70 | -57.50 | 41 |
| 61 | Candlestick reversal · 1h | reversion | 63.38 | -36.62 | 445 | 27.9 | -39.52 | -7.11 | -41.01 | 591 |
| 62 | Three white soldiers | momentum | 61.14 | -38.86 | 502 | 14.9 | -48.90 | -22.83 | -48.90 | 646 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.58 | -98.94 | 5246 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.69 | -25.86 | -79.80 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.18 | -44.45 | -93.21 | 2501 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.38 | -31.67 | -89.41 | 1917 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.69 | -38.53 | -90.72 | 2311 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.21 | -31.50 | -90.26 | 2201 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -52.07 | -97.77 | 3441 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -54.01 | -96.20 | 3416 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.51 | -32.27 | -93.61 | 2385 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.29 | -33.76 | -82.38 | 1671 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -54.04 | -99.56 | 6038 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.21 | -42.08 | -92.22 | 2593 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.51 | -36.74 | -95.53 | 3428 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.30 | -99.81 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.00 | -42.07 | -92.00 | 2249 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.49 | -24.30 | -75.49 | 1594 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -58.34 | -97.72 | 3516 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -62.40 | -98.88 | 4906 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.56 | -26.86 | -68.99 | 1217 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -51.84 | -94.57 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.39 | -35.94 | -84.52 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -72.11 | -99.65 | 6360 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.84 | -31.56 | -89.85 | 2293 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.83 | -20.34 | -78.92 | 1790 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.92 | -36.38 | -90.94 | 2223 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.86 | -52.71 | -96.86 | 3887 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -55.09 | -89.37 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.32 | -27.06 | -66.04 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.13 | -22.63 | -71.18 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.58 | -19.61 | -80.64 | 1705 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.29 | -49.33 | -97.29 | 4311 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -102.11 | -99.93 | 8293 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T17:25 | Agent (ML meta-label) | buy | TSLA | 8.14 | — | following Ichimoku |
| 2026-11-10T17:25 | Agent (ML meta-label) | buy | SQQQ | 8.15 | — | following Stochastic reversion |
| 2026-11-10T17:25 | Agent (ML meta-label) | buy | META | 8.15 | — | entry |
| 2026-11-10T17:25 | Agent (ML meta-label) | sell | TECL | 4.82 | -0.05 | rebalance down |
| 2026-11-10T17:25 | Agent (ML meta-label) | sell | SPY | 4.92 | -0.01 | rebalance down |
| 2026-11-10T17:25 | Agent (ML meta-label) | sell | COIN | 4.91 | -0.02 | rebalance down |
| 2026-11-10T17:25 | Agent (ML meta-label) | sell | AMZN | 4.93 | -0.00 | rebalance down |
| 2026-11-10T17:25 | Agent (ML meta-label) | sell | AMD | 4.87 | -0.04 | rebalance down |
| 2026-11-10T17:20 | Agent (ML meta-label) | buy | TECL | 4.90 | — | rebalance up |
| 2026-11-10T17:20 | Agent (ML meta-label) | buy | SPY | 4.91 | — | rebalance up |
| 2026-11-10T17:20 | Agent (ML meta-label) | buy | COIN | 4.88 | — | rebalance up |
| 2026-11-10T17:20 | Agent (ML meta-label) | buy | AMZN | 4.90 | — | rebalance up |
| 2026-11-10T17:20 | Agent (ML meta-label) | buy | AMD | 4.93 | — | rebalance up |
| 2026-11-10T17:20 | Agent (ML meta-label) | sell | TSLA | 8.16 | -0.01 | selected signal exited |
| 2026-11-10T17:20 | Agent (ML meta-label) | sell | SQQQ | 8.17 | -0.01 | selected signal exited |
| 2026-11-10T17:20 | Agent (ML meta-label) | sell | META | 8.18 | -0.01 | selected signal exited |
| 2026-11-10T17:20 | Agent (aggressive) | sell | LABU | 42.47 | -0.05 | selected signal exited |
| 2026-11-10T17:15 | Agent (ML meta-label) | buy | TSLA | 8.17 | — | following Ichimoku |
| 2026-11-10T17:15 | Agent (ML meta-label) | buy | SQQQ | 8.19 | — | following Stochastic reversion |
| 2026-11-10T17:15 | Agent (ML meta-label) | buy | SPY | 8.19 | — | entry |
| 2026-11-10T17:15 | Agent (ML meta-label) | buy | META | 8.19 | — | entry |
| 2026-11-10T17:15 | Agent (ML meta-label) | sell | TECL | 7.38 | -0.02 | rebalance down |
| 2026-11-10T17:15 | Agent (ML meta-label) | sell | SOXL | 3.56 | 0.04 | selected signal exited |
| 2026-11-10T17:15 | Agent (ML meta-label) | sell | COIN | 7.25 | -0.05 | rebalance down |
| 2026-11-10T17:15 | Agent (ML meta-label) | sell | AMZN | 7.23 | -0.01 | rebalance down |
| 2026-11-10T17:15 | Agent (ML meta-label) | sell | AMD | 7.32 | -0.02 | rebalance down |
| 2026-11-10T17:15 | Agent (aggressive) | buy | LABU | 42.52 | — | following MFI reversion |
| 2026-11-10T17:11 | Agent (ML meta-label) | buy | TECL | 8.23 | — | rebalance up |
| 2026-11-10T17:11 | Agent (ML meta-label) | buy | SOXL | 3.52 | — | entry |
| 2026-11-10T17:11 | Agent (ML meta-label) | buy | COIN | 8.16 | — | rebalance up |
| 2026-11-10T17:11 | Agent (ML meta-label) | buy | AMZN | 8.17 | — | rebalance up |
| 2026-11-10T17:11 | Agent (ML meta-label) | buy | AMD | 8.19 | — | rebalance up |
| 2026-11-10T17:11 | Agent (ML meta-label) | sell | TSLA | 7.26 | -0.00 | selected signal exited |
| 2026-11-10T17:11 | Agent (ML meta-label) | sell | SQQQ | 7.27 | 0.01 | selected signal exited |
| 2026-11-10T17:11 | Agent (ML meta-label) | sell | SPY | 7.27 | -0.00 | selected signal exited |
| 2026-11-10T17:11 | Agent (ML meta-label) | sell | META | 7.29 | 0.03 | selected signal exited |
| 2026-11-10T17:05 | Agent (aggressive) | sell | LABU | 42.57 | 0.11 | selected signal exited |
| 2026-11-10T17:00 | Agent (rotation) | sell | TQQQ | 32.37 | -0.39 | selected signal exited |
| 2026-11-10T17:00 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 110.59 | -1.34 | target is flat |
| 2026-11-10T17:00 | Agent (ML meta-label) | sell | SOXL | 6.10 | -0.19 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 17:28:05.000140+00:00 -> 2026-11-10 17:38:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
