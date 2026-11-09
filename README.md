# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T21:05:05.000131+00:00 · 53800 ticks

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
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 37815 decisions in 3264 calls, $0.4687 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T21:05 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-09T21:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-09T21:05 | 2 / 3 / 0 | BTC-USD 51% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| VWAP momentum | TSLA | 1.69 | +2.40% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 18.87 | 3.81 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.20 | 12.20 | 0 | — | 13.65 | 4.66 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.93 | 11.93 | 31 | 29.0 | 20.12 | 3.03 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.01 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.55 | 1.55 | 126 | 36.5 | 10.07 | 3.83 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 101.13 | 1.13 | 0 | — | 4.81 | 1.39 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.91 | 0.91 | 7 | 42.9 | -0.93 | 0.20 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.67 | 1.10 | -9.06 | 239 |
| 11 | Agent (rotation) | meta | 98.10 | -1.90 | 177 | 28.2 | -3.43 | -1.36 | -10.59 | 169 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.87 | -3.34 | -12.87 | 151 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.43 | -3.57 | 0 | — | -1.49 | -0.45 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.58 | -5.42 | 0 | — | -3.79 | -0.98 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.78 | -8.67 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.81 | -7.19 | 0 | — | -3.95 | -1.03 | -10.64 | 1 |
| 19 | Trend pullback · 1h | trend | 92.53 | -7.47 | 108 | 23.1 | -13.74 | -5.16 | -17.96 | 79 |
| 20 | Copy: Insider buying | copy | 91.78 | -8.22 | 42 | 38.1 | -9.74 | -2.07 | -16.06 | 63 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 90.34 | -9.66 | 391 | 34.3 | -13.39 | -4.27 | -15.24 | 595 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.25 | -3.34 | -14.68 | 81 |
| 24 | Hold BTC | benchmark | 86.94 | -13.06 | 1 | 0.0 | -4.87 | -0.56 | -15.58 | 1 |
| 25 | Agent | meta | 86.80 | -13.20 | 163 | 35.0 | -13.72 | -7.11 | -14.18 | 205 |
| 26 | Daily: Bullish score | daily | 86.09 | -13.91 | 15 | 20.0 | -10.31 | -1.58 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.52 | -14.48 | 167 | 26.9 | -11.32 | -2.05 | -21.29 | 227 |
| 28 | Agent (aggressive) | meta | 83.88 | -16.12 | 76 | 31.6 | -16.53 | -4.75 | -18.49 | 94 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 83.80 | -16.20 | 2 | 0.0 | -7.56 | -0.83 | -24.16 | 1 |
| 30 | Opening range 15m | breakout | 83.50 | -16.50 | 481 | 32.4 | -18.38 | -5.25 | -19.91 | 728 |
| 31 | Donchian 55/20 · 1h | breakout | 83.36 | -16.64 | 71 | 14.1 | -18.19 | -4.00 | -22.45 | 104 |
| 32 | Stochastic reversion · 1h | reversion | 83.17 | -16.83 | 279 | 48.4 | -23.94 | -3.55 | -28.04 | 387 |
| 33 | Keltner breakout · 1h | breakout | 81.92 | -18.08 | 107 | 23.4 | -22.14 | -4.49 | -25.12 | 173 |
| 34 | Volume breakout · 1h | breakout | 81.30 | -18.70 | 145 | 27.6 | -15.00 | -3.42 | -21.11 | 96 |
| 35 | Connors RSI(2) · 1h | reversion | 80.58 | -19.42 | 205 | 40.0 | -19.67 | -6.61 | -19.99 | 124 |
| 36 | Heikin-Ashi · 1h | trend | 79.81 | -20.19 | 400 | 22.8 | -39.73 | -7.42 | -43.08 | 674 |
| 37 | MFI reversion · 1h | reversion | 79.33 | -20.67 | 351 | 34.5 | -16.02 | -2.04 | -21.23 | 166 |
| 38 | ADX DI cross · 1h | trend | 79.31 | -20.68 | 179 | 18.4 | -22.37 | -3.86 | -28.34 | 274 |
| 39 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -39.47 | -2.65 | -45.81 | 25 |
| 40 | CCI reversion · 1h | reversion | 79.11 | -20.89 | 319 | 45.8 | -23.48 | -3.56 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.08 | -22.92 | 96 | 15.6 | -29.64 | -8.49 | -29.86 | 119 |
| 42 | Bollinger breakout · 1h | breakout | 76.79 | -23.21 | 170 | 22.9 | -22.64 | -4.76 | -27.92 | 240 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -25.37 | -3.87 | -32.17 | 372 |
| 44 | MACD cross · 1h | trend | 75.25 | -24.75 | 349 | 22.6 | -32.80 | -5.39 | -39.46 | 484 |
| 45 | Z-score reversion · 1h | reversion | 75.23 | -24.77 | 179 | 37.4 | -20.12 | -2.87 | -27.66 | 228 |
| 46 | Williams %R · 1h | reversion | 74.88 | -25.12 | 337 | 46.9 | -36.14 | -5.92 | -39.29 | 540 |
| 47 | MACD zero-line · 1h | trend | 74.39 | -25.61 | 157 | 16.6 | -24.77 | -5.10 | -29.19 | 213 |
| 48 | EMA 20/50 cross · 1h | trend | 74.10 | -25.90 | 102 | 10.8 | -24.45 | -4.40 | -32.62 | 127 |
| 49 | Supertrend · 1h | trend | 73.27 | -26.73 | 167 | 13.2 | -29.27 | -5.07 | -34.92 | 226 |
| 50 | RSI momentum · 1h | momentum | 72.95 | -27.05 | 159 | 12.6 | -23.55 | -3.77 | -33.01 | 218 |
| 51 | Triple EMA stack · 1h | trend | 72.40 | -27.60 | 143 | 14.7 | -26.21 | -4.57 | -34.87 | 203 |
| 52 | ROC + volume · 1h | momentum | 71.73 | -28.27 | 349 | 25.5 | -36.10 | -6.80 | -38.89 | 384 |
| 53 | OBV trend · 1h | momentum | 71.64 | -28.36 | 274 | 18.2 | -26.98 | -5.01 | -34.09 | 275 |
| 54 | Donchian 20/10 · 1h | breakout | 70.39 | -29.61 | 142 | 19.7 | -29.88 | -5.53 | -35.64 | 207 |
| 55 | Daily: Momentum burst | daily | 70.36 | -29.64 | 26 | 11.5 | -39.31 | -5.68 | -39.66 | 31 |
| 56 | RSI(14) reversion · 1h | reversion | 68.53 | -31.47 | 162 | 31.5 | -29.64 | -4.38 | -33.90 | 245 |
| 57 | Max aggression: 1-day momentum | meta | 68.27 | -31.73 | 27 | 25.9 | -31.45 | -1.60 | -57.50 | 42 |
| 58 | Agent (ML meta-label) | meta | 67.76 | -32.24 | 1632 | 24.2 | -7.07 | -1.02 | -18.53 | 323 |
| 59 | VWAP momentum · 1h | momentum | 67.61 | -32.39 | 810 | 21.6 | -52.04 | -11.26 | -53.55 | 1236 |
| 60 | EMA 9/21 cross · 1h | trend | 65.56 | -34.44 | 247 | 9.7 | -38.33 | -7.62 | -40.15 | 335 |
| 61 | Candlestick reversal · 1h | reversion | 64.98 | -35.02 | 434 | 28.6 | -37.63 | -6.82 | -38.42 | 591 |
| 62 | Three white soldiers | momentum | 62.31 | -37.69 | 494 | 15.2 | -48.60 | -22.79 | -48.60 | 646 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -45.93 | -98.96 | 5253 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.75 | -26.48 | -79.76 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.15 | -46.42 | -93.25 | 2516 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.04 | -32.19 | -89.09 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.68 | -40.09 | -90.75 | 2322 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.04 | -31.67 | -90.05 | 2196 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.65 | -54.73 | -97.65 | 3457 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -58.65 | -96.26 | 3422 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -32.53 | -93.73 | 2428 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.99 | -34.29 | -82.22 | 1674 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -56.01 | -99.53 | 5961 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.30 | -43.66 | -92.44 | 2611 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -37.32 | -95.48 | 3401 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -76.86 | -99.80 | 6159 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.71 | -44.04 | -91.71 | 2258 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.49 | -24.80 | -75.70 | 1597 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -62.37 | -97.66 | 3519 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -63.67 | -98.83 | 4877 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.64 | -27.38 | -69.32 | 1220 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.52 | -55.42 | -94.52 | 2758 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.69 | -37.85 | -84.69 | 1785 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.31 | -99.65 | 6362 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.60 | -32.63 | -89.67 | 2271 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.38 | -20.17 | -78.44 | 1743 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.47 | -36.74 | -90.59 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -52.69 | -96.81 | 3876 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -58.79 | -89.36 | 2142 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.24 | -29.23 | -66.40 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.13 | -22.95 | -71.87 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.70 | -19.19 | -79.70 | 1680 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -49.89 | -97.32 | 4309 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -113.82 | -99.93 | 8312 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T21:00 | MFI reversion · 1h | buy | SOL-USD | 4.72 | — | rebalance up |
| 2026-11-09T21:00 | MFI reversion · 1h | buy | ETH-USD | 4.72 | — | rebalance up |
| 2026-11-09T21:00 | MFI reversion · 1h | buy | DOGE-USD | 4.57 | — | rebalance up |
| 2026-11-09T20:55 | Agent (rotation) | sell | TQQQ | 66.10 | 2.93 | selected signal exited |
| 2026-11-09T20:55 | Day trade: Stocks in Play ORB | sell | TNA | 25.44 | 1.11 | target is flat |
| 2026-11-09T20:55 | Day trade: Stocks in Play ORB | sell | SOXL | 27.20 | 2.87 | target is flat |
| 2026-11-09T20:55 | Day trade: Stocks in Play ORB | sell | ETHU | 24.79 | 0.10 | target is flat |
| 2026-11-09T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 103.97 | 2.31 | target is flat |
| 2026-11-09T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 117.56 | 3.97 | target is flat |
| 2026-11-09T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 93.19 | -0.91 | target is flat |
| 2026-11-09T20:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 111.93 | 6.10 | target is flat |
| 2026-11-09T20:55 | Agent | sell | TSLA | 17.43 | -0.06 | selected signal exited |
| 2026-11-09T20:55 | Agent | sell | SQQQ | 17.43 | -0.01 | selected signal exited |
| 2026-11-09T20:55 | Opening range 30m | sell | UPRO | 8.24 | 0.14 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | TQQQ | 7.42 | 0.14 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | TNA | 8.37 | 0.25 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | TECL | 8.30 | 0.18 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | SPY | 8.14 | 0.03 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | SOXL | 8.40 | 0.28 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | QQQ | 8.16 | 0.04 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | PLTR | 2.36 | 0.01 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | LABU | 6.48 | 0.06 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | IWM | 8.19 | 0.07 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | COIN | 2.32 | -0.01 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | AMD | 8.38 | 0.26 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 30m | sell | AAPL | 5.60 | 0.00 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | UPRO | 5.59 | 0.12 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | TQQQ | 5.63 | 0.16 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | TNA | 5.69 | 0.21 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | TECL | 5.68 | 0.20 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | SPY | 5.51 | 0.03 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | SOXL | 5.86 | 0.39 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | QQQ | 5.52 | 0.05 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | PLTR | 5.53 | 0.05 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | NVDA | 5.48 | 0.00 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | MSTR | 5.48 | 0.00 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | IWM | 5.54 | 0.07 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | COIN | 5.49 | 0.02 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | BITX | 5.45 | -0.02 | end-of-day flatten |
| 2026-11-09T20:55 | Opening range 15m | sell | AMD | 5.66 | 0.19 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 21:05:05.000131+00:00 -> 2026-11-09 21:15:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 21:05:05.000131+00:00 -> 2026-11-09 21:15:05.000131+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 21:05:05.000131+00:00 -> 2026-11-09 21:15:05.000131+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
