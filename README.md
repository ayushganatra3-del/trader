# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T00:05:05.000132+00:00 · 53955 ticks

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

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 29.11 · VIX 19.90 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 75 decisions in 15 calls, $0.0010 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T00:05 | 1 / 3 / 1 | XRP-USD 14% |  |
| Breezy | 2026-11-10T00:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-10T00:05 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.36 | 12.36 | 0 | — | 13.79 | 4.66 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.93 | 11.93 | 31 | 29.0 | 20.12 | 3.01 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.55 | 1.55 | 126 | 36.5 | 10.08 | 3.80 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 101.14 | 1.14 | 0 | — | 4.81 | 1.38 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.93 | 0.93 | 7 | 42.9 | -0.93 | 0.19 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.68 | 1.09 | -9.06 | 240 |
| 11 | Agent (rotation) | meta | 98.11 | -1.90 | 177 | 28.2 | -3.44 | -1.36 | -10.59 | 169 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -13.02 | -3.34 | -13.02 | 152 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.44 | -3.56 | 0 | — | -1.49 | -0.45 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.84 | -5.16 | 0 | — | -3.54 | -0.88 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.75 | -7.25 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 19 | Trend pullback · 1h | trend | 92.54 | -7.46 | 108 | 23.1 | -13.74 | -5.12 | -17.96 | 79 |
| 20 | Copy: Insider buying | copy | 92.01 | -7.99 | 42 | 38.1 | -9.58 | -2.00 | -16.06 | 63 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 90.34 | -9.66 | 391 | 34.3 | -13.39 | -4.24 | -15.24 | 595 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.49 | -3.40 | -14.68 | 82 |
| 24 | Hold BTC | benchmark | 87.37 | -12.63 | 1 | 0.0 | -4.80 | -0.59 | -15.58 | 1 |
| 25 | Agent | meta | 86.80 | -13.20 | 163 | 35.0 | -13.72 | -7.04 | -14.18 | 205 |
| 26 | Daily: Bullish score | daily | 86.09 | -13.91 | 15 | 20.0 | -10.31 | -1.57 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.54 | -14.46 | 167 | 26.9 | -11.32 | -2.03 | -21.29 | 227 |
| 28 | Agent (aggressive) | meta | 83.88 | -16.12 | 76 | 31.6 | -16.53 | -4.71 | -18.49 | 94 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 83.72 | -16.28 | 2 | 0.0 | -7.65 | -0.84 | -24.16 | 1 |
| 30 | Opening range 15m | breakout | 83.50 | -16.50 | 481 | 32.4 | -18.38 | -5.20 | -19.91 | 728 |
| 31 | Donchian 55/20 · 1h | breakout | 83.37 | -16.63 | 71 | 14.1 | -18.18 | -3.97 | -22.45 | 104 |
| 32 | Stochastic reversion · 1h | reversion | 83.17 | -16.83 | 279 | 48.4 | -23.96 | -3.52 | -28.05 | 387 |
| 33 | Keltner breakout · 1h | breakout | 81.94 | -18.06 | 107 | 23.4 | -22.13 | -4.45 | -25.12 | 173 |
| 34 | Volume breakout · 1h | breakout | 81.30 | -18.70 | 145 | 27.6 | -14.82 | -3.34 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.58 | -19.42 | 205 | 40.0 | -19.67 | -6.55 | -19.99 | 124 |
| 36 | Heikin-Ashi · 1h | trend | 79.80 | -20.20 | 400 | 22.8 | -39.75 | -7.37 | -43.08 | 675 |
| 37 | ADX DI cross · 1h | trend | 79.33 | -20.67 | 179 | 18.4 | -22.38 | -3.83 | -28.34 | 274 |
| 38 | MFI reversion · 1h | reversion | 79.26 | -20.74 | 352 | 34.4 | -16.12 | -2.04 | -21.23 | 167 |
| 39 | Max aggression: 5-day momentum | meta | 79.24 | -20.76 | 18 | 44.4 | -39.47 | -2.63 | -45.81 | 25 |
| 40 | CCI reversion · 1h | reversion | 79.17 | -20.83 | 320 | 45.9 | -23.35 | -3.51 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.08 | -22.92 | 96 | 15.6 | -29.76 | -8.45 | -29.87 | 120 |
| 42 | Bollinger breakout · 1h | breakout | 76.79 | -23.21 | 170 | 22.9 | -22.64 | -4.72 | -27.92 | 240 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -25.37 | -3.84 | -32.17 | 372 |
| 44 | MACD cross · 1h | trend | 75.31 | -24.69 | 349 | 22.6 | -32.37 | -5.27 | -39.46 | 483 |
| 45 | Z-score reversion · 1h | reversion | 75.30 | -24.70 | 179 | 37.4 | -21.18 | -3.04 | -27.66 | 226 |
| 46 | Williams %R · 1h | reversion | 74.88 | -25.12 | 337 | 46.9 | -35.80 | -5.80 | -38.97 | 540 |
| 47 | MACD zero-line · 1h | trend | 74.39 | -25.61 | 157 | 16.6 | -24.78 | -5.06 | -29.19 | 213 |
| 48 | EMA 20/50 cross · 1h | trend | 74.11 | -25.89 | 102 | 10.8 | -24.55 | -4.40 | -32.62 | 127 |
| 49 | Supertrend · 1h | trend | 73.28 | -26.72 | 167 | 13.2 | -29.28 | -5.03 | -34.92 | 226 |
| 50 | RSI momentum · 1h | momentum | 72.96 | -27.04 | 159 | 12.6 | -23.55 | -3.74 | -33.01 | 218 |
| 51 | Triple EMA stack · 1h | trend | 72.41 | -27.59 | 143 | 14.7 | -26.43 | -4.59 | -34.87 | 204 |
| 52 | ROC + volume · 1h | momentum | 71.74 | -28.26 | 349 | 25.5 | -36.07 | -6.73 | -38.89 | 385 |
| 53 | OBV trend · 1h | momentum | 71.65 | -28.35 | 274 | 18.2 | -27.13 | -5.00 | -34.09 | 275 |
| 54 | Donchian 20/10 · 1h | breakout | 70.40 | -29.60 | 142 | 19.7 | -29.88 | -5.49 | -35.64 | 207 |
| 55 | Daily: Momentum burst | daily | 70.36 | -29.64 | 26 | 11.5 | -39.31 | -5.63 | -39.66 | 31 |
| 56 | RSI(14) reversion · 1h | reversion | 68.60 | -31.40 | 162 | 31.5 | -31.07 | -4.54 | -34.82 | 248 |
| 57 | Max aggression: 1-day momentum | meta | 68.28 | -31.72 | 27 | 25.9 | -31.45 | -1.58 | -57.50 | 42 |
| 58 | Agent (ML meta-label) | meta | 67.72 | -32.28 | 1633 | 24.2 | -1.91 | -0.16 | -16.56 | 305 |
| 59 | VWAP momentum · 1h | momentum | 67.61 | -32.39 | 810 | 21.6 | -51.91 | -11.10 | -53.43 | 1238 |
| 60 | EMA 9/21 cross · 1h | trend | 65.57 | -34.43 | 247 | 9.7 | -38.35 | -7.56 | -40.15 | 336 |
| 61 | Candlestick reversal · 1h | reversion | 65.02 | -34.98 | 434 | 28.6 | -37.77 | -6.78 | -38.59 | 594 |
| 62 | Three white soldiers | momentum | 61.94 | -38.06 | 497 | 15.1 | -48.70 | -22.55 | -48.70 | 646 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -43.92 | -98.95 | 5245 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.86 | -26.01 | -79.91 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.16 | -44.33 | -93.22 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.99 | -31.16 | -89.08 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.59 | -38.20 | -90.64 | 2318 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.05 | -30.73 | -90.10 | 2198 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.67 | -51.33 | -97.67 | 3462 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -55.20 | -96.29 | 3429 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.73 | -31.80 | -93.77 | 2432 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.04 | -33.37 | -82.10 | 1676 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -52.09 | -99.52 | 5962 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.27 | -41.92 | -92.37 | 2611 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -35.73 | -95.45 | 3403 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -67.66 | -99.80 | 6159 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -41.82 | -91.76 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.53 | -24.22 | -75.65 | 1600 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -56.98 | -97.66 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -58.35 | -98.84 | 4880 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.54 | -26.81 | -69.10 | 1218 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.51 | -51.40 | -94.51 | 2757 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.58 | -36.35 | -84.58 | 1781 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -66.80 | -99.65 | 6363 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.61 | -31.64 | -89.67 | 2267 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.37 | -19.83 | -78.42 | 1743 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.44 | -35.46 | -90.57 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -49.42 | -96.80 | 3877 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -54.50 | -89.30 | 2139 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.16 | -28.35 | -66.43 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.06 | -22.58 | -71.75 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.67 | -18.88 | -79.68 | 1679 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -47.09 | -97.31 | 4311 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -92.07 | -99.93 | 8311 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T00:00 | Heikin-Ashi · 1h | buy | BTC-USD | 4.99 | — | entry signal |
| 2026-11-09T23:05 | Three white soldiers | sell | XRP-USD | 15.50 | -0.08 | exit signal |
| 2026-11-09T23:05 | Three white soldiers | sell | SOL-USD | 15.42 | -0.16 | stop-loss |
| 2026-11-09T23:05 | Three white soldiers | sell | ETH-USD | 15.45 | -0.13 | exit signal |
| 2026-11-09T23:00 | CCI reversion · 1h | buy | SOL-USD | 4.75 | — | rebalance up |
| 2026-11-09T23:00 | CCI reversion · 1h | sell | BTC-USD | 9.93 | 0.00 | exit signal |
| 2026-11-09T23:00 | Candlestick reversal · 1h | buy | SOL-USD | 1.98 | — | entry signal |
| 2026-11-09T22:40 | Three white soldiers | buy | XRP-USD | 15.58 | — | entry signal |
| 2026-11-09T22:40 | Three white soldiers | buy | SOL-USD | 15.58 | — | entry signal |
| 2026-11-09T22:40 | Three white soldiers | buy | ETH-USD | 15.58 | — | entry signal |
| 2026-11-09T22:00 | Agent (ML meta-label) | sell | SOL-USD | 7.51 | -0.10 | selected signal exited |
| 2026-11-09T22:00 | MFI reversion · 1h | sell | SOL-USD | 13.15 | -0.15 | exit signal |
| 2026-11-09T21:06 | Candlestick reversal · 1h | buy | XRP-USD | 9.28 | — | entry |
| 2026-11-09T21:06 | Candlestick reversal · 1h | sell | ETH-USD | 3.75 | -0.01 | rebalance down |
| 2026-11-09T21:06 | Candlestick reversal · 1h | sell | DOGE-USD | 3.75 | -0.02 | rebalance down |
| 2026-11-09T21:06 | Candlestick reversal · 1h | sell | BTC-USD | 3.76 | -0.01 | rebalance down |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 00:05:05.000132+00:00 -> 2026-11-10 00:15:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-12 00:05:05.000132+00:00 -> 2026-11-10 00:15:05.000132+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-12 00:05:05.000132+00:00 -> 2026-11-10 00:15:05.000132+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
