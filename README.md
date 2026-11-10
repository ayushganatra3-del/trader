# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T15:00:05.000153+00:00 · 54707 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.80 (-13.20%)

Closed trades 163, win rate 35.0%, fees £4.99, max drawdown -13.60%.

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

Today: 12866 decisions in 2269 calls, $0.1758 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T15:00 | 5 / 22 / 3 | AMD 21%, SOXL 15% |  |
| Breezy | 2026-11-10T15:00 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-10T15:00 | 9 / 20 / 1 | COIN 73% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 18.87 | 3.78 | -4.91 | 26 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.72 | 14.72 | 31 | 29.0 | 24.26 | 3.51 | -8.66 | 44 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 113.45 | 13.45 | 0 | — | 14.07 | 4.74 | -5.18 | 1 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.97 | 0.96 | 130 | 35.4 | 8.36 | 3.13 | -2.67 | 90 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.78 | 0.78 | 0 | — | 4.08 | 1.19 | -6.60 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent (rotation) | meta | 99.08 | -0.92 | 178 | 28.7 | -1.90 | -0.72 | -9.90 | 161 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 11 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.62 | 1.08 | -9.06 | 239 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | VWAP reversion · 1h | reversion | 96.70 | -3.30 | 133 | 47.4 | -12.45 | -3.20 | -13.01 | 150 |
| 14 | Hold SPY | benchmark | 96.53 | -3.48 | 0 | — | -1.57 | -0.48 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.36 | -5.64 | 0 | — | -3.57 | -0.89 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.91 | -7.09 | 108 | 23.1 | -13.62 | -5.07 | -18.02 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.41 | -7.59 | 0 | — | -4.62 | -1.22 | -10.64 | 1 |
| 20 | Copy: Insider buying | copy | 92.14 | -7.86 | 42 | 38.1 | -8.60 | -1.78 | -15.11 | 67 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 90.34 | -9.66 | 391 | 34.3 | -12.76 | -4.03 | -14.62 | 591 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.33 | -2.89 | -14.15 | 77 |
| 24 | Agent | meta | 86.80 | -13.20 | 163 | 35.0 | -13.82 | -7.15 | -14.28 | 203 |
| 25 | Hold BTC | benchmark | 86.59 | -13.40 | 1 | 0.0 | -5.89 | -0.77 | -15.65 | 1 |
| 26 | Daily: Bullish score | daily | 86.16 | -13.84 | 15 | 20.0 | -9.08 | -1.37 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.79 | -14.21 | 167 | 26.9 | -12.76 | -2.58 | -21.13 | 224 |
| 28 | Opening range 15m | breakout | 84.86 | -15.14 | 481 | 32.4 | -15.55 | -4.27 | -19.09 | 736 |
| 29 | Agent (aggressive) | meta | 83.88 | -16.12 | 76 | 31.6 | -16.96 | -4.86 | -18.51 | 94 |
| 30 | Donchian 55/20 · 1h | breakout | 83.56 | -16.44 | 71 | 14.1 | -17.47 | -3.79 | -22.44 | 103 |
| 31 | Max aggression: 5-day momentum | meta | 83.01 | -17.00 | 18 | 44.4 | -33.88 | -2.02 | -45.81 | 25 |
| 32 | Keltner breakout · 1h | breakout | 82.53 | -17.47 | 109 | 22.9 | -21.26 | -4.28 | -25.12 | 175 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 82.48 | -17.52 | 2 | 0.0 | -8.77 | -1.00 | -24.16 | 1 |
| 34 | Stochastic reversion · 1h | reversion | 82.12 | -17.88 | 280 | 48.2 | -23.93 | -3.54 | -27.05 | 388 |
| 35 | Volume breakout · 1h | breakout | 81.32 | -18.68 | 146 | 27.4 | -14.82 | -3.34 | -21.11 | 95 |
| 36 | Connors RSI(2) · 1h | reversion | 80.63 | -19.37 | 205 | 40.0 | -19.68 | -6.56 | -19.99 | 124 |
| 37 | Heikin-Ashi · 1h | trend | 80.21 | -19.79 | 401 | 22.7 | -39.62 | -7.30 | -43.14 | 675 |
| 38 | ADX DI cross · 1h | trend | 79.70 | -20.30 | 179 | 18.4 | -23.67 | -4.01 | -29.26 | 271 |
| 39 | MFI reversion · 1h | reversion | 78.83 | -21.17 | 355 | 34.1 | -15.95 | -2.05 | -21.69 | 157 |
| 40 | CCI reversion · 1h | reversion | 78.27 | -21.73 | 324 | 45.4 | -23.59 | -3.60 | -30.29 | 456 |
| 41 | Bollinger breakout · 1h | breakout | 77.05 | -22.95 | 170 | 22.9 | -22.57 | -4.63 | -27.92 | 241 |
| 42 | Ichimoku · 1h | trend | 76.76 | -23.24 | 98 | 15.3 | -30.22 | -8.62 | -30.94 | 120 |
| 43 | MACD cross · 1h | trend | 75.80 | -24.20 | 355 | 22.3 | -31.73 | -5.14 | -39.49 | 483 |
| 44 | MACD zero-line · 1h | trend | 75.28 | -24.72 | 157 | 16.6 | -24.23 | -4.81 | -30.11 | 214 |
| 45 | Z-score reversion · 1h | reversion | 74.89 | -25.11 | 182 | 36.8 | -22.50 | -3.26 | -27.66 | 228 |
| 46 | Bollinger reversion · 1h | reversion | 74.89 | -25.11 | 273 | 41.0 | -24.56 | -3.76 | -32.06 | 372 |
| 47 | EMA 20/50 cross · 1h | trend | 74.28 | -25.72 | 102 | 10.8 | -23.65 | -4.16 | -32.57 | 124 |
| 48 | Williams %R · 1h | reversion | 73.76 | -26.24 | 340 | 46.5 | -33.97 | -5.36 | -35.82 | 528 |
| 49 | RSI momentum · 1h | momentum | 73.70 | -26.30 | 159 | 12.6 | -23.46 | -3.93 | -33.05 | 210 |
| 50 | Supertrend · 1h | trend | 73.66 | -26.34 | 167 | 13.2 | -28.74 | -4.91 | -35.31 | 226 |
| 51 | Daily: Momentum burst | daily | 72.99 | -27.01 | 27 | 11.1 | -36.82 | -5.04 | -39.25 | 34 |
| 52 | Triple EMA stack · 1h | trend | 72.42 | -27.57 | 143 | 14.7 | -26.79 | -4.62 | -35.38 | 191 |
| 53 | ROC + volume · 1h | momentum | 72.43 | -27.57 | 355 | 26.5 | -35.60 | -6.51 | -39.49 | 375 |
| 54 | OBV trend · 1h | momentum | 72.07 | -27.93 | 274 | 18.2 | -27.28 | -4.84 | -35.55 | 277 |
| 55 | Max aggression: 1-day momentum | meta | 71.80 | -28.20 | 27 | 25.9 | -25.67 | -1.11 | -57.50 | 41 |
| 56 | Donchian 20/10 · 1h | breakout | 71.47 | -28.53 | 142 | 19.7 | -29.55 | -5.37 | -35.64 | 208 |
| 57 | RSI(14) reversion · 1h | reversion | 68.49 | -31.51 | 166 | 31.3 | -25.99 | -3.78 | -32.51 | 232 |
| 58 | Agent (ML meta-label) | meta | 67.85 | -32.15 | 1643 | 24.2 | -8.58 | -1.25 | -20.25 | 346 |
| 59 | VWAP momentum · 1h | momentum | 67.38 | -32.62 | 818 | 21.5 | -51.97 | -11.01 | -54.01 | 1235 |
| 60 | EMA 9/21 cross · 1h | trend | 65.99 | -34.02 | 249 | 9.6 | -37.30 | -7.39 | -40.79 | 335 |
| 61 | Candlestick reversal · 1h | reversion | 63.64 | -36.36 | 443 | 28.0 | -37.05 | -6.76 | -38.16 | 588 |
| 62 | Three white soldiers | momentum | 61.45 | -38.55 | 501 | 15.0 | -48.77 | -22.81 | -48.80 | 647 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -44.61 | -98.94 | 5290 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.67 | -25.86 | -79.67 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.09 | -44.01 | -93.09 | 2501 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.99 | -31.29 | -89.18 | 1913 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.52 | -38.02 | -90.59 | 2313 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.98 | -30.44 | -90.18 | 2202 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -53.42 | -97.73 | 3469 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.16 | -53.23 | -96.20 | 3421 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -31.84 | -93.75 | 2400 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.12 | -33.57 | -82.12 | 1669 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -55.55 | -99.55 | 6005 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.13 | -41.82 | -92.20 | 2602 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.48 | -36.19 | -95.50 | 3404 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.90 | -99.81 | 6162 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.98 | -43.34 | -91.98 | 2258 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.92 | -23.69 | -75.20 | 1591 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -57.37 | -97.70 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -62.33 | -98.88 | 4892 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.64 | -27.02 | -69.02 | 1220 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.51 | -52.17 | -94.55 | 2758 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.21 | -35.26 | -84.26 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -71.38 | -99.65 | 6353 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.88 | -32.76 | -90.03 | 2301 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.42 | -20.08 | -78.67 | 1780 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.72 | -37.38 | -90.83 | 2206 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -51.91 | -96.83 | 3886 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -54.02 | -89.19 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.29 | -27.07 | -66.01 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -70.51 | -22.04 | -71.15 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.05 | -19.47 | -80.21 | 1689 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -48.50 | -97.27 | 4293 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -105.56 | -99.93 | 8302 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T15:00 | Agent (ML meta-label) | sell | TSLA | 5.83 | 0.00 | selected signal exited |
| 2026-11-10T15:00 | Agent (ML meta-label) | sell | META | 6.14 | 0.02 | selected signal exited |
| 2026-11-10T15:00 | MFI reversion · 1h | buy | ETH-USD | 1.56 | — | entry signal |
| 2026-11-10T15:00 | Z-score reversion · 1h | buy | BTC-USD | 9.36 | — | entry signal |
| 2026-11-10T15:00 | Bollinger reversion · 1h | buy | ETH-USD | 11.09 | — | entry signal |
| 2026-11-10T15:00 | Bollinger reversion · 1h | sell | SOL-USD | 3.74 | -0.03 | rebalance down |
| 2026-11-10T15:00 | RSI(14) reversion · 1h | buy | ETH-USD | 13.71 | — | entry signal |
| 2026-11-10T15:00 | RSI(14) reversion · 1h | sell | SOXL | 14.51 | 1.87 | take-profit |
| 2026-11-10T15:00 | Candlestick reversal · 1h | buy | BTC-USD | 15.92 | — | entry signal |
| 2026-11-10T15:00 | ROC + volume · 1h | buy | SOXL | 4.30 | — | rebalance up |
| 2026-11-10T15:00 | ROC + volume · 1h | buy | QQQ | 4.88 | — | rebalance up |
| 2026-11-10T15:00 | ROC + volume · 1h | buy | GOOGL | 5.07 | — | rebalance up |
| 2026-11-10T15:00 | ROC + volume · 1h | buy | AMZN | 4.95 | — | rebalance up |
| 2026-11-10T15:00 | ROC + volume · 1h | buy | AMD | 4.39 | — | rebalance up |
| 2026-11-10T15:00 | ROC + volume · 1h | buy | AAPL | 4.99 | — | rebalance up |
| 2026-11-10T15:00 | ROC + volume · 1h | sell | UPRO | 7.10 | 0.04 | target is flat |
| 2026-11-10T15:00 | ROC + volume · 1h | sell | TQQQ | 7.19 | 0.13 | target is flat |
| 2026-11-10T15:00 | ROC + volume · 1h | sell | TNA | 7.14 | 0.08 | target is flat |
| 2026-11-10T15:00 | ROC + volume · 1h | sell | META | 7.13 | 0.06 | target is flat |
| 2026-11-10T15:00 | VWAP momentum · 1h | buy | DOGE-USD | 3.74 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | UPRO | 5.63 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | TNA | 5.66 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | SPY | 5.66 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | MSTR | 5.66 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | META | 5.66 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | LABU | 5.66 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | IWM | 5.66 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | GOOGL | 5.66 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | COIN | 5.66 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | buy | BITX | 5.66 | — | entry signal |
| 2026-11-10T15:00 | Opening range 15m | sell | TQQQ | 11.27 | 0.15 | rebalance down |
| 2026-11-10T15:00 | Opening range 15m | sell | TECL | 11.27 | 0.15 | rebalance down |
| 2026-11-10T15:00 | Opening range 15m | sell | SOXL | 11.63 | 0.40 | rebalance down |
| 2026-11-10T15:00 | Opening range 15m | sell | QQQ | 11.11 | 0.04 | rebalance down |
| 2026-11-10T15:00 | Opening range 15m | sell | AMD | 11.31 | 0.18 | rebalance down |
| 2026-11-10T14:55 | Agent (ML meta-label) | buy | TSLA | 5.82 | — | following Ichimoku |
| 2026-11-10T14:55 | Agent (ML meta-label) | buy | META | 6.12 | — | entry |
| 2026-11-10T14:55 | Agent (ML meta-label) | sell | TECL | 7.62 | 0.18 | selected signal exited |
| 2026-11-10T14:55 | Agent (ML meta-label) | sell | SPY | 4.32 | -0.01 | selected signal exited |
| 2026-11-10T14:55 | Supertrend · 1h | buy | DOGE-USD | 3.77 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 15:00:05.000153+00:00 -> 2026-11-10 15:10:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
