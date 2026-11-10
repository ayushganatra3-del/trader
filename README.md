# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T16:29:05.000263+00:00 · 54762 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.22 (-12.78%)

Closed trades 164, win rate 35.4%, fees £5.02, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 17.43 | -0.02 |

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

Today: 17837 decisions in 2434 calls, $0.2340 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T16:29 | 4 / 15 / 11 | cash |  |
| Breezy | 2026-11-10T16:29 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-10T16:29 | 2 / 23 / 5 | COIN 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| MFI reversion | LABU | 1.68 | +6.28% | 4 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| MFI reversion | TSLA | 1.40 | +2.15% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.49 | 3.91 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.96 | 13.96 | 0 | — | 13.68 | 4.60 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.62 | 12.62 | 31 | 29.0 | 21.47 | 3.19 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.00 | 1.00 | 0 | — | 3.87 | 1.13 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.52 | 1.06 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 98.46 | -1.54 | 178 | 28.7 | -1.98 | -0.76 | -9.30 | 143 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.57 | -3.43 | 0 | — | -2.02 | -0.64 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.48 | -4.52 | 136 | 46.3 | -13.63 | -3.47 | -13.66 | 150 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.51 | -5.49 | 0 | — | -4.85 | -1.27 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.91 | -7.09 | 108 | 23.1 | -13.59 | -5.06 | -17.82 | 78 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.42 | -7.58 | 0 | — | -4.94 | -1.31 | -10.64 | 1 |
| 20 | Copy: Insider buying | copy | 91.87 | -8.13 | 42 | 38.1 | -9.14 | -1.91 | -15.11 | 67 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.89 | -11.11 | 401 | 33.4 | -14.52 | -4.52 | -14.62 | 604 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -7.91 | -2.74 | -14.15 | 78 |
| 24 | Agent | meta | 87.22 | -12.78 | 164 | 35.4 | -13.61 | -6.98 | -14.30 | 202 |
| 25 | Daily: Bullish score | daily | 86.89 | -13.11 | 15 | 20.0 | -7.79 | -1.15 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 85.74 | -14.26 | 1 | 0.0 | -7.34 | -0.99 | -16.43 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.57 | -14.43 | 167 | 26.9 | -13.30 | -2.70 | -21.39 | 224 |
| 28 | Agent (aggressive) | meta | 84.92 | -15.08 | 77 | 32.5 | -15.82 | -4.43 | -18.51 | 96 |
| 29 | Donchian 55/20 · 1h | breakout | 84.16 | -15.84 | 71 | 14.1 | -16.66 | -3.53 | -22.11 | 102 |
| 30 | Opening range 15m | breakout | 82.75 | -17.25 | 495 | 31.7 | -18.06 | -5.13 | -19.09 | 739 |
| 31 | Keltner breakout · 1h | breakout | 82.30 | -17.70 | 109 | 22.9 | -20.65 | -4.24 | -25.32 | 177 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 82.16 | -17.84 | 2 | 0.0 | -9.55 | -1.10 | -24.16 | 1 |
| 33 | Max aggression: 5-day momentum | meta | 81.87 | -18.13 | 18 | 44.4 | -35.06 | -2.15 | -45.81 | 25 |
| 34 | Volume breakout · 1h | breakout | 81.07 | -18.93 | 146 | 27.4 | -14.46 | -3.37 | -21.36 | 93 |
| 35 | Connors RSI(2) · 1h | reversion | 80.94 | -19.06 | 206 | 39.8 | -19.45 | -6.46 | -19.99 | 125 |
| 36 | Stochastic reversion · 1h | reversion | 80.42 | -19.58 | 284 | 47.5 | -25.94 | -3.80 | -27.29 | 390 |
| 37 | Heikin-Ashi · 1h | trend | 79.49 | -20.51 | 415 | 24.3 | -39.77 | -7.39 | -42.55 | 672 |
| 38 | ADX DI cross · 1h | trend | 79.46 | -20.54 | 181 | 19.3 | -24.03 | -4.08 | -29.26 | 270 |
| 39 | MFI reversion · 1h | reversion | 77.14 | -22.86 | 359 | 33.7 | -19.05 | -2.43 | -21.69 | 158 |
| 40 | CCI reversion · 1h | reversion | 76.95 | -23.05 | 326 | 45.1 | -25.70 | -3.90 | -30.69 | 457 |
| 41 | Bollinger breakout · 1h | breakout | 76.91 | -23.09 | 170 | 22.9 | -21.42 | -4.41 | -27.95 | 238 |
| 42 | Ichimoku · 1h | trend | 75.67 | -24.33 | 99 | 15.2 | -31.24 | -8.87 | -31.35 | 120 |
| 43 | EMA 20/50 cross · 1h | trend | 74.82 | -25.18 | 102 | 10.8 | -24.06 | -4.24 | -33.53 | 122 |
| 44 | MACD cross · 1h | trend | 74.77 | -25.23 | 355 | 22.3 | -33.20 | -5.42 | -39.51 | 480 |
| 45 | MACD zero-line · 1h | trend | 74.08 | -25.92 | 157 | 16.6 | -25.77 | -5.17 | -30.30 | 216 |
| 46 | Bollinger reversion · 1h | reversion | 73.50 | -26.50 | 278 | 40.3 | -26.25 | -4.00 | -32.06 | 372 |
| 47 | Supertrend · 1h | trend | 73.37 | -26.63 | 168 | 13.1 | -32.84 | -5.97 | -35.49 | 233 |
| 48 | RSI momentum · 1h | momentum | 73.35 | -26.65 | 159 | 12.6 | -24.37 | -4.03 | -33.41 | 210 |
| 49 | Z-score reversion · 1h | reversion | 72.90 | -27.10 | 186 | 36.0 | -24.86 | -3.58 | -27.66 | 228 |
| 50 | Triple EMA stack · 1h | trend | 72.64 | -27.36 | 143 | 14.7 | -26.40 | -4.62 | -34.51 | 206 |
| 51 | OBV trend · 1h | momentum | 72.20 | -27.80 | 274 | 18.2 | -27.23 | -4.80 | -35.48 | 277 |
| 52 | Williams %R · 1h | reversion | 71.62 | -28.38 | 346 | 45.7 | -35.52 | -5.50 | -36.01 | 529 |
| 53 | ROC + volume · 1h | momentum | 71.33 | -28.67 | 358 | 26.8 | -35.96 | -6.82 | -38.14 | 380 |
| 54 | Donchian 20/10 · 1h | breakout | 71.27 | -28.73 | 142 | 19.7 | -30.68 | -5.60 | -35.64 | 209 |
| 55 | Daily: Momentum burst | daily | 71.12 | -28.88 | 27 | 11.1 | -38.13 | -5.40 | -39.18 | 34 |
| 56 | Max aggression: 1-day momentum | meta | 67.75 | -32.25 | 27 | 25.9 | -30.16 | -1.47 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 66.62 | -33.38 | 170 | 30.6 | -28.06 | -4.14 | -32.51 | 225 |
| 58 | VWAP momentum · 1h | momentum | 66.57 | -33.43 | 829 | 22.0 | -53.15 | -11.32 | -54.31 | 1226 |
| 59 | Agent (ML meta-label) | meta | 66.19 | -33.81 | 1660 | 24.3 | -14.82 | -2.23 | -19.71 | 335 |
| 60 | EMA 9/21 cross · 1h | trend | 65.45 | -34.55 | 249 | 9.6 | -38.09 | -7.47 | -41.12 | 335 |
| 61 | Candlestick reversal · 1h | reversion | 63.26 | -36.74 | 444 | 27.9 | -37.30 | -6.72 | -38.44 | 584 |
| 62 | Three white soldiers | momentum | 61.14 | -38.86 | 502 | 14.9 | -49.01 | -22.96 | -49.01 | 647 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.80 | -98.94 | 5276 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.85 | -25.93 | -79.86 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.23 | -44.68 | -93.24 | 2504 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.42 | -31.71 | -89.43 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.72 | -38.58 | -90.72 | 2313 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.18 | -31.39 | -90.23 | 2202 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -52.34 | -97.77 | 3446 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -54.44 | -96.22 | 3422 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.59 | -32.57 | -93.69 | 2399 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.48 | -33.94 | -82.49 | 1674 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -54.40 | -99.56 | 6026 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.24 | -42.32 | -92.24 | 2594 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -36.45 | -95.51 | 3418 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.48 | -99.81 | 6162 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.00 | -42.16 | -92.00 | 2249 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.51 | -24.37 | -75.55 | 1596 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -58.35 | -97.73 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -62.92 | -98.88 | 4906 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.57 | -26.87 | -68.99 | 1217 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -52.40 | -94.59 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.49 | -36.25 | -84.52 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -72.13 | -99.65 | 6369 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.95 | -32.42 | -89.96 | 2307 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.63 | -20.21 | -78.66 | 1781 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.82 | -36.69 | -90.87 | 2225 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.84 | -52.73 | -96.85 | 3894 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.42 | -56.92 | -89.42 | 2153 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.20 | -27.00 | -65.92 | 818 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.06 | -22.59 | -71.15 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.47 | -19.60 | -80.54 | 1698 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.25 | -48.78 | -97.27 | 4314 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -104.44 | -99.93 | 8298 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T16:25 | Agent (ML meta-label) | sell | TECL | 7.60 | -0.05 | rebalance down |
| 2026-11-10T16:25 | Agent (ML meta-label) | sell | SPY | 13.25 | 0.03 | selected signal exited |
| 2026-11-10T16:16 | Agent (ML meta-label) | buy | TECL | 3.56 | — | rebalance up |
| 2026-11-10T16:16 | Agent (ML meta-label) | sell | SPY | 3.32 | 0.00 | rebalance down |
| 2026-11-10T16:11 | Agent (ML meta-label) | buy | TECL | 9.55 | — | entry |
| 2026-11-10T16:11 | Z-score reversion · 1h | buy | TQQQ | 3.68 | — | rebalance up |
| 2026-11-10T16:11 | Opening range 30m | buy | TSLA | 22.24 | — | entry signal |
| 2026-11-10T16:11 | Opening range 15m | buy | TSLA | 20.57 | — | entry signal |
| 2026-11-10T16:11 | Opening range 15m | buy | SOXL | 20.81 | — | entry signal |
| 2026-11-10T16:05 | Agent (ML meta-label) | buy | SPY | 3.45 | — | rebalance up |
| 2026-11-10T16:05 | Agent (ML meta-label) | sell | TECL | 13.23 | -0.09 | selected signal exited |
| 2026-11-10T16:01 | Agent | buy | TSLA | 17.45 | — | following Ichimoku, MFI reversion |
| 2026-11-10T16:01 | Supertrend · 1h | buy | AMZN | 3.68 | — | entry |
| 2026-11-10T16:01 | Supertrend · 1h | sell | DOGE-USD | 3.68 | -0.09 | exit signal |
| 2026-11-10T15:55 | Williams %R · 1h | sell | COIN | 17.92 | -0.73 | stop-loss |
| 2026-11-10T15:55 | Opening range 30m | sell | AMZN | 22.14 | -0.17 | stop-loss |
| 2026-11-10T15:55 | Opening range 15m | buy | META | 8.77 | — | rebalance up |
| 2026-11-10T15:55 | Opening range 15m | buy | AMD | 8.87 | — | rebalance up |
| 2026-11-10T15:55 | Opening range 15m | sell | TQQQ | 11.82 | -0.13 | exit signal |
| 2026-11-10T15:55 | Opening range 15m | sell | SOXL | 11.65 | -0.40 | stop-loss |
| 2026-11-10T15:55 | Opening range 15m | sell | QQQ | 11.89 | -0.05 | exit signal |
| 2026-11-10T15:55 | Opening range 15m | sell | AMZN | 11.88 | -0.07 | stop-loss |
| 2026-11-10T15:50 | Agent (ML meta-label) | buy | SPY | 13.10 | — | entry |
| 2026-11-10T15:50 | Agent (aggressive) | sell | SQQQ | 42.98 | 1.04 | selected signal exited |
| 2026-11-10T15:50 | Agent | sell | SQQQ | 17.79 | 0.43 | selected signal exited |
| 2026-11-10T15:50 | Williams %R · 1h | sell | NVDA | 17.79 | -0.35 | stop-loss |
| 2026-11-10T15:50 | Z-score reversion · 1h | buy | TECL | 3.66 | — | rebalance up |
| 2026-11-10T15:50 | Z-score reversion · 1h | buy | SOXL | 3.72 | — | rebalance up |
| 2026-11-10T15:50 | Z-score reversion · 1h | sell | NVDA | 14.46 | -0.47 | stop-loss |
| 2026-11-10T15:50 | RSI(14) reversion · 1h | sell | NVDA | 16.52 | -0.58 | stop-loss |
| 2026-11-10T15:50 | Opening range 15m | sell | TECL | 11.78 | -0.19 | stop-loss |
| 2026-11-10T15:45 | Agent (ML meta-label) | sell | DOGE-USD | 13.10 | -0.45 | selected signal exited |
| 2026-11-10T15:45 | MFI reversion · 1h | buy | TECL | 6.03 | — | rebalance up |
| 2026-11-10T15:45 | MFI reversion · 1h | buy | SPY | 6.29 | — | rebalance up |
| 2026-11-10T15:45 | MFI reversion · 1h | buy | AMZN | 7.83 | — | rebalance up |
| 2026-11-10T15:45 | MFI reversion · 1h | buy | AAPL | 6.38 | — | rebalance up |
| 2026-11-10T15:45 | MFI reversion · 1h | sell | SOL-USD | 12.75 | -0.24 | stop-loss |
| 2026-11-10T15:45 | MFI reversion · 1h | sell | DOGE-USD | 12.66 | -0.53 | stop-loss |
| 2026-11-10T15:45 | CCI reversion · 1h | sell | NVDA | 19.07 | -0.57 | stop-loss |
| 2026-11-10T15:45 | Stochastic reversion · 1h | sell | XRP-USD | 19.90 | -0.46 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 16:29:05.000263+00:00 -> 2026-11-10 16:39:05.000263+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
