# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T15:09:05.000139+00:00 · 53524 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.51 (-12.49%)

Closed trades 156, win rate 35.9%, fees £4.84, max drawdown -12.89%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.48 | -0.03 |

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

Today: 13305 decisions in 2436 calls, $0.1828 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T15:09 | 5 / 11 / 14 | cash |  |
| Breezy | 2026-11-09T15:09 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-09T15:09 | 6 / 21 / 3 | MSTR 68% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 114.65 | 14.65 | 19 | 68.4 | 14.25 | 3.07 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.15 | 11.15 | 0 | — | 12.56 | 4.22 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.16 | 9.16 | 30 | 26.7 | 16.97 | 2.74 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.39 | 30 | 43.3 | -0.80 | -0.07 | -9.64 | 31 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.76 | 0.76 | 0 | — | 4.27 | 1.27 | -6.60 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.58 | -0.42 | 122 | 35.2 | 7.90 | 3.70 | -2.27 | 89 |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.60 | -1.40 | 7 | 42.9 | -3.34 | -0.09 | -18.69 | 8 |
| 10 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.05 | -3.08 | -12.05 | 152 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 12 | Agent (rotation) | meta | 96.35 | -3.65 | 176 | 27.8 | -5.70 | -2.93 | -10.98 | 172 |
| 13 | Hold SPY | benchmark | 96.03 | -3.97 | 0 | — | -2.51 | -0.77 | -6.18 | 1 |
| 14 | Gap and go | momentum | 95.64 | -4.36 | 173 | 27.7 | 0.57 | 0.27 | -9.06 | 239 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 17 | Trend pullback · 1h | trend | 93.06 | -6.94 | 108 | 23.1 | -13.24 | -4.90 | -17.86 | 78 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 92.56 | -7.44 | 0 | — | -5.59 | -1.65 | -9.25 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.09 | -7.91 | 0 | — | -5.48 | -1.49 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 89.20 | -10.80 | 375 | 32.5 | -15.21 | -4.94 | -15.99 | 584 |
| 22 | Copy: Insider buying | copy | 89.07 | -10.93 | 40 | 37.5 | -11.94 | -2.81 | -16.06 | 63 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.13 | -2.83 | -14.15 | 80 |
| 24 | Agent | meta | 87.51 | -12.49 | 156 | 35.9 | -13.16 | -6.84 | -13.55 | 199 |
| 25 | Hold BTC | benchmark | 86.93 | -13.07 | 1 | 0.0 | -5.33 | -0.58 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.79 | -13.21 | 15 | 20.0 | -8.95 | -1.33 | -16.58 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.38 | -14.62 | 167 | 26.9 | -11.63 | -2.11 | -21.25 | 220 |
| 28 | Donchian 55/20 · 1h | breakout | 84.17 | -15.82 | 71 | 14.1 | -14.39 | -2.95 | -21.37 | 103 |
| 29 | Agent (aggressive) | meta | 83.94 | -16.06 | 74 | 31.1 | -16.21 | -4.63 | -18.49 | 92 |
| 30 | Stochastic reversion · 1h | reversion | 83.10 | -16.90 | 268 | 46.3 | -24.79 | -3.63 | -28.85 | 392 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 82.58 | -17.42 | 2 | 0.0 | -10.35 | -1.17 | -24.16 | 1 |
| 32 | Opening range 15m | breakout | 82.17 | -17.83 | 465 | 30.5 | -20.23 | -5.97 | -20.97 | 734 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -15.95 | -3.62 | -21.11 | 96 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -19.04 | -6.36 | -19.64 | 124 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -23.43 | -4.94 | -25.06 | 177 |
| 36 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -37.64 | -2.52 | -43.56 | 25 |
| 37 | MFI reversion · 1h | reversion | 78.65 | -21.35 | 345 | 33.6 | -17.19 | -2.17 | -21.38 | 163 |
| 38 | ADX DI cross · 1h | trend | 78.55 | -21.45 | 179 | 18.4 | -25.46 | -4.19 | -28.61 | 262 |
| 39 | Heikin-Ashi · 1h | trend | 78.44 | -21.56 | 394 | 23.1 | -39.07 | -7.66 | -41.75 | 669 |
| 40 | CCI reversion · 1h | reversion | 77.81 | -22.19 | 306 | 43.5 | -28.89 | -4.58 | -30.71 | 470 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 42 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -21.88 | -4.49 | -27.58 | 243 |
| 43 | Bollinger reversion · 1h | reversion | 75.00 | -25.00 | 264 | 39.4 | -27.37 | -4.35 | -33.39 | 373 |
| 44 | EMA 20/50 cross · 1h | trend | 74.73 | -25.27 | 102 | 10.8 | -22.77 | -4.00 | -31.40 | 127 |
| 45 | Williams %R · 1h | reversion | 74.72 | -25.28 | 318 | 44.7 | -33.38 | -5.14 | -36.44 | 540 |
| 46 | MACD zero-line · 1h | trend | 74.45 | -25.55 | 157 | 16.6 | -24.80 | -5.11 | -29.17 | 207 |
| 47 | MACD cross · 1h | trend | 74.30 | -25.70 | 349 | 22.6 | -33.46 | -5.67 | -39.51 | 482 |
| 48 | Z-score reversion · 1h | reversion | 74.08 | -25.92 | 170 | 34.1 | -22.04 | -3.28 | -27.66 | 227 |
| 49 | RSI momentum · 1h | momentum | 72.96 | -27.04 | 159 | 12.6 | -26.95 | -5.03 | -33.06 | 210 |
| 50 | Triple EMA stack · 1h | trend | 72.95 | -27.05 | 142 | 14.8 | -26.13 | -4.41 | -34.92 | 196 |
| 51 | Supertrend · 1h | trend | 72.92 | -27.08 | 166 | 13.3 | -31.33 | -5.83 | -34.42 | 225 |
| 52 | OBV trend · 1h | momentum | 71.80 | -28.20 | 274 | 18.2 | -28.91 | -6.03 | -34.01 | 273 |
| 53 | Daily: Momentum burst | daily | 70.88 | -29.12 | 26 | 11.5 | -37.87 | -5.35 | -39.04 | 31 |
| 54 | ROC + volume · 1h | momentum | 70.62 | -29.38 | 349 | 25.5 | -37.92 | -7.34 | -39.59 | 378 |
| 55 | Donchian 20/10 · 1h | breakout | 70.19 | -29.81 | 142 | 19.7 | -31.12 | -5.79 | -35.56 | 210 |
| 56 | Agent (ML meta-label) | meta | 67.67 | -32.33 | 1554 | 23.2 | -3.48 | -0.49 | -13.98 | 325 |
| 57 | RSI(14) reversion · 1h | reversion | 67.47 | -32.53 | 151 | 26.5 | -29.42 | -4.33 | -32.65 | 244 |
| 58 | VWAP momentum · 1h | momentum | 66.84 | -33.16 | 801 | 21.6 | -53.21 | -11.60 | -53.99 | 1234 |
| 59 | EMA 9/21 cross · 1h | trend | 66.07 | -33.93 | 246 | 9.8 | -39.06 | -7.79 | -40.13 | 327 |
| 60 | Candlestick reversal · 1h | reversion | 65.27 | -34.73 | 430 | 28.1 | -38.32 | -7.15 | -39.32 | 597 |
| 61 | Max aggression: 1-day momentum | meta | 63.70 | -36.30 | 27 | 25.9 | -36.14 | -2.08 | -57.50 | 42 |
| 62 | Three white soldiers | momentum | 62.56 | -37.44 | 488 | 15.0 | -48.71 | -22.51 | -48.79 | 646 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -45.71 | -99.00 | 5303 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.18 | -26.20 | -80.26 | 1431 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -46.86 | -93.37 | 2507 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.43 | -32.26 | -89.52 | 1915 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.92 | -39.98 | -90.96 | 2308 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.68 | -90.03 | 2183 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -54.77 | -97.75 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -57.71 | -96.33 | 3399 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.57 | -32.56 | -93.62 | 2413 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.33 | -35.14 | -82.40 | 1649 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -55.89 | -99.53 | 5994 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.58 | -43.99 | -92.65 | 2606 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.57 | -37.40 | -95.57 | 3393 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -74.73 | -99.80 | 6186 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.99 | -43.96 | -91.99 | 2275 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.04 | -24.84 | -76.27 | 1590 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -62.09 | -97.72 | 3499 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -62.78 | -98.85 | 4903 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.17 | -28.46 | -69.53 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -55.32 | -94.68 | 2741 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.07 | -37.26 | -85.07 | 1766 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.47 | -99.66 | 6391 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.67 | -32.43 | -89.77 | 2305 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.47 | -20.14 | -78.52 | 1754 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.66 | -36.64 | -90.78 | 2217 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.80 | -52.91 | -96.82 | 3905 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.54 | -57.90 | -89.54 | 2156 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.06 | -29.03 | -66.24 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.96 | -23.82 | -72.24 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.41 | -19.04 | -79.73 | 1694 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.31 | -50.48 | -97.34 | 4339 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -108.06 | -99.93 | 8274 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T15:05 | Day trade: Stocks in Play ORB | buy | ETHU | 24.69 | — | entry |
| 2026-11-09T15:05 | Agent (ML meta-label) | sell | AAPL | 2.67 | -0.01 | selected signal exited |
| 2026-11-09T15:05 | Candlestick reversal · 1h | sell | TNA | 5.89 | 0.49 | take-profit |
| 2026-11-09T15:05 | Opening range 30m | buy | UPRO | 22.31 | — | entry signal |
| 2026-11-09T15:05 | Opening range 30m | buy | TNA | 22.31 | — | entry signal |
| 2026-11-09T15:05 | Opening range 30m | buy | SPY | 22.31 | — | entry signal |
| 2026-11-09T15:05 | Opening range 30m | buy | IWM | 22.31 | — | entry signal |
| 2026-11-09T15:01 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 101.66 | — | entry |
| 2026-11-09T15:01 | Agent (ML meta-label) | buy | BITX | 4.01 | — | entry |
| 2026-11-09T15:01 | VWAP momentum · 1h | buy | ETH-USD | 1.47 | — | entry signal |
| 2026-11-09T15:01 | Heikin-Ashi · 1h | buy | DOGE-USD | 3.77 | — | entry signal |
| 2026-11-09T14:56 | Agent (ML meta-label) | sell | BITX | 4.05 | 0.05 | selected signal exited |
| 2026-11-09T14:50 | Day trade: Stocks in Play ORB | sell | ETHU | 24.69 | 0.36 | target is flat |
| 2026-11-09T14:50 | Agent (aggressive) | buy | COIN | 42.01 | — | following Donchian 20/10, Keltner breakout |
| 2026-11-09T14:50 | Agent | buy | COIN | 17.51 | — | following Donchian 20/10, Keltner breakout |
| 2026-11-09T14:50 | Bollinger reversion · 1h | buy | UPRO | 3.96 | — | rebalance up |
| 2026-11-09T14:50 | Bollinger reversion · 1h | buy | TQQQ | 3.84 | — | rebalance up |
| 2026-11-09T14:50 | Bollinger reversion · 1h | buy | TECL | 3.94 | — | rebalance up |
| 2026-11-09T14:50 | Bollinger reversion · 1h | buy | SPY | 4.11 | — | rebalance up |
| 2026-11-09T14:50 | Bollinger reversion · 1h | buy | QQQ | 4.07 | — | rebalance up |
| 2026-11-09T14:50 | Bollinger reversion · 1h | buy | PLTR | 3.87 | — | rebalance up |
| 2026-11-09T14:50 | Bollinger reversion · 1h | buy | LABU | 3.88 | — | rebalance up |
| 2026-11-09T14:50 | Bollinger reversion · 1h | sell | TNA | 5.57 | 0.42 | take-profit |
| 2026-11-09T14:50 | Opening range 15m | buy | UPRO | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | TQQQ | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | TNA | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | TECL | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | SPY | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | SOXL | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | QQQ | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | PLTR | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | NVDA | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | MSTR | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | IWM | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | ETHU | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | COIN | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | BITX | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Opening range 15m | buy | AMD | 5.47 | — | entry signal |
| 2026-11-09T14:50 | Gap and go | buy | AMD | 11.70 | — | entry |
| 2026-11-09T14:50 | Gap and go | sell | AMZN | 11.70 | -0.09 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 15:09:05.000139+00:00 -> 2026-11-09 15:19:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 15:09:05.000139+00:00 -> 2026-11-09 15:19:05.000139+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 15:09:05.000139+00:00 -> 2026-11-09 15:19:05.000139+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
