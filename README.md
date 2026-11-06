# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T11:55:05.000128+00:00 · 49638 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.46 (-11.54%)

Closed trades 148, win rate 37.2%, fees £4.17, max drawdown -11.95%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-05)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 38.26 · VIX 28.18 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, AMZN 5.2, AAPL 5.0, MSFT 4.9, TSLA 1.2, MSTR 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 9267 decisions in 1854 calls, $0.1295 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T11:55 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-06T11:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T11:55 | 1 / 4 / 0 | ETH-USD 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.13 | 12.13 | 0 | — | 13.22 | 4.50 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.82 | 7.82 | 29 | 27.6 | 16.51 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.05 | 0.61 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.68 | -0.32 | 0 | — | 2.97 | 0.93 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.49 | -1.51 | 111 | 44.1 | -13.54 | -3.29 | -14.16 | 151 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.77 | -2.23 | 117 | 35.0 | 4.93 | 2.51 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Agent (rotation) | meta | 95.25 | -4.75 | 175 | 28.0 | -7.17 | -4.37 | -10.36 | 173 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.06 | 0.10 | -9.18 | 218 |
| 14 | Hold SPY | benchmark | 94.25 | -5.75 | 0 | — | -4.45 | -1.64 | -6.18 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Trend pullback · 1h | trend | 92.40 | -7.60 | 105 | 22.9 | -15.25 | -5.48 | -17.86 | 81 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.31 | -7.68 | 7 | 42.9 | -13.09 | -1.39 | -18.69 | 8 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 91.07 | -8.93 | 0 | — | -8.33 | -2.52 | -9.25 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.40 | -9.60 | 0 | — | -7.33 | -2.17 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.94 | -5.09 | -17.56 | 579 |
| 22 | Daily: Bullish score | daily | 89.24 | -10.76 | 14 | 21.4 | -4.51 | -0.57 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.26 | -3.55 | -14.68 | 86 |
| 24 | Hold BTC | benchmark | 88.57 | -11.43 | 1 | 0.0 | -4.92 | -0.61 | -13.78 | 1 |
| 25 | Agent | meta | 88.46 | -11.54 | 148 | 37.2 | -14.20 | -7.57 | -14.60 | 211 |
| 26 | Parabolic SAR · 1h | trend | 87.68 | -12.32 | 166 | 27.1 | -14.67 | -3.22 | -20.02 | 241 |
| 27 | Copy: Insider buying | copy | 86.82 | -13.18 | 40 | 37.5 | -25.08 | -4.95 | -26.04 | 65 |
| 28 | Donchian 55/20 · 1h | breakout | 86.74 | -13.27 | 71 | 14.1 | -12.50 | -2.52 | -19.94 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.13 | -14.87 | 17 | 47.1 | -30.71 | -1.88 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.53 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.67 | -16.33 | 446 | 30.7 | -19.82 | -5.84 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.83 | -17.16 | 144 | 27.8 | -15.84 | -3.55 | -21.39 | 101 |
| 33 | Keltner breakout · 1h | breakout | 82.09 | -17.91 | 106 | 23.6 | -21.76 | -4.47 | -24.41 | 174 |
| 34 | Stochastic reversion · 1h | reversion | 81.59 | -18.41 | 257 | 46.7 | -28.59 | -4.44 | -29.25 | 386 |
| 35 | Connors RSI(2) · 1h | reversion | 80.82 | -19.18 | 203 | 39.9 | -20.51 | -6.77 | -21.05 | 129 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.06 | -19.94 | 2 | 0.0 | -14.78 | -2.03 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.76 | -20.23 | 171 | 18.1 | -23.70 | -3.92 | -26.36 | 261 |
| 38 | Bollinger breakout · 1h | breakout | 79.27 | -20.73 | 165 | 23.6 | -22.07 | -4.55 | -26.52 | 245 |
| 39 | MFI reversion · 1h | reversion | 79.22 | -20.78 | 328 | 33.8 | -18.86 | -2.69 | -20.66 | 154 |
| 40 | Ichimoku · 1h | trend | 78.80 | -21.20 | 94 | 14.9 | -22.37 | -4.53 | -28.82 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.89 | -22.11 | 284 | 45.8 | -29.53 | -4.77 | -30.70 | 452 |
| 42 | Heikin-Ashi · 1h | trend | 77.04 | -22.96 | 386 | 23.1 | -42.70 | -8.93 | -43.30 | 671 |
| 43 | EMA 20/50 cross · 1h | trend | 76.64 | -23.36 | 102 | 10.8 | -22.75 | -4.07 | -30.17 | 131 |
| 44 | Triple EMA stack · 1h | trend | 75.13 | -24.87 | 142 | 14.8 | -29.29 | -6.10 | -33.06 | 207 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.12 | -5.38 | -29.20 | 210 |
| 46 | RSI momentum · 1h | momentum | 74.15 | -25.85 | 158 | 12.7 | -28.40 | -5.39 | -32.33 | 221 |
| 47 | Supertrend · 1h | trend | 74.14 | -25.86 | 166 | 13.3 | -29.93 | -5.16 | -34.26 | 217 |
| 48 | MACD cross · 1h | trend | 73.74 | -26.26 | 334 | 23.1 | -36.10 | -6.33 | -38.81 | 477 |
| 49 | Z-score reversion · 1h | reversion | 73.15 | -26.85 | 160 | 35.6 | -27.84 | -4.30 | -28.32 | 225 |
| 50 | Donchian 20/10 · 1h | breakout | 72.48 | -27.52 | 140 | 20.0 | -29.12 | -5.32 | -34.25 | 212 |
| 51 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.53 | -4.93 | -37.46 | 30 |
| 52 | Bollinger reversion · 1h | reversion | 72.12 | -27.88 | 247 | 39.3 | -34.05 | -6.25 | -34.52 | 375 |
| 53 | Williams %R · 1h | reversion | 71.98 | -28.02 | 312 | 44.9 | -39.31 | -6.55 | -39.70 | 529 |
| 54 | ROC + volume · 1h | momentum | 71.68 | -28.32 | 344 | 25.6 | -36.75 | -7.15 | -37.14 | 381 |
| 55 | OBV trend · 1h | momentum | 71.53 | -28.47 | 266 | 17.3 | -32.65 | -6.89 | -34.09 | 294 |
| 56 | VWAP momentum · 1h | momentum | 68.32 | -31.68 | 760 | 22.2 | -55.64 | -12.25 | -56.28 | 1220 |
| 57 | EMA 9/21 cross · 1h | trend | 68.16 | -31.84 | 241 | 10.0 | -39.23 | -8.01 | -39.91 | 335 |
| 58 | RSI(14) reversion · 1h | reversion | 66.65 | -33.35 | 142 | 27.5 | -28.05 | -4.33 | -31.29 | 205 |
| 59 | Three white soldiers | momentum | 66.21 | -33.79 | 453 | 16.1 | -47.63 | -21.79 | -47.63 | 636 |
| 60 | Agent (ML meta-label) | meta | 65.35 | -34.65 | 1508 | 22.3 | -9.66 | -1.38 | -19.60 | 329 |
| 61 | Candlestick reversal · 1h | reversion | 65.10 | -34.90 | 397 | 28.5 | -38.29 | -7.00 | -38.69 | 560 |
| 62 | Max aggression: 1-day momentum | meta | 62.20 | -37.80 | 26 | 26.9 | -41.38 | -2.54 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.12 | -98.94 | 5139 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.21 | -25.47 | -80.30 | 1407 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.26 | -46.81 | -93.37 | 2488 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.04 | -30.90 | -89.13 | 1895 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.61 | -38.85 | -90.78 | 2282 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.15 | -31.01 | -90.24 | 2194 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.67 | -53.41 | -97.70 | 3434 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.11 | -58.29 | -96.18 | 3349 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.60 | -32.41 | -93.61 | 2427 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.56 | -35.56 | -81.87 | 1627 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -52.51 | -99.51 | 5937 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.51 | -42.88 | -92.58 | 2579 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.72 | -36.67 | -95.72 | 3405 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -68.74 | -99.80 | 6126 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.59 | -42.63 | -91.61 | 2244 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.85 | -26.52 | -75.11 | 1561 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -59.36 | -97.67 | 3479 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -58.74 | -98.77 | 4841 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.28 | -28.36 | -70.08 | 1197 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.49 | -53.46 | -94.55 | 2734 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.68 | -36.65 | -84.88 | 1768 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.71 | -99.64 | 6315 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.08 | -30.66 | -89.10 | 2271 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.54 | -19.28 | -77.75 | 1732 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.01 | -36.22 | -91.04 | 2217 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.58 | -50.82 | -96.58 | 3837 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -56.17 | -89.51 | 2163 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.47 | -27.50 | -65.89 | 802 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.17 | -24.18 | -73.80 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.62 | -17.85 | -78.72 | 1663 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.25 | -47.94 | -97.25 | 4302 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -95.59 | -99.93 | 8206 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T10:35 | RSI(14) reversion · 1h | buy | XRP-USD | 3.32 | — | rebalance up |
| 2026-11-06T10:35 | RSI(14) reversion · 1h | sell | BTC-USD | 3.32 | 0.00 | rebalance down |
| 2026-11-06T10:01 | Williams %R · 1h | buy | XRP-USD | 5.54 | — | entry signal |
| 2026-11-06T10:01 | Williams %R · 1h | sell | DOGE-USD | 5.54 | 0.00 | exit signal |
| 2026-11-06T10:01 | Williams %R · 1h | sell | BTC-USD | 5.52 | -0.02 | exit signal |
| 2026-11-06T10:01 | Stochastic reversion · 1h | sell | DOGE-USD | 5.91 | 0.09 | exit signal |
| 2026-11-06T10:01 | Stochastic reversion · 1h | sell | BTC-USD | 5.81 | -0.00 | exit signal |
| 2026-11-06T10:01 | Bollinger reversion · 1h | sell | SOL-USD | 4.03 | 0.02 | exit signal |
| 2026-11-06T10:01 | Bollinger reversion · 1h | sell | DOGE-USD | 4.06 | 0.06 | exit signal |
| 2026-11-06T10:01 | Bollinger reversion · 1h | sell | BTC-USD | 4.00 | -0.00 | exit signal |
| 2026-11-06T10:01 | RSI(14) reversion · 1h | buy | XRP-USD | 6.78 | — | entry signal |
| 2026-11-06T10:01 | RSI(14) reversion · 1h | sell | SOL-USD | 3.42 | 0.02 | rebalance down |
| 2026-11-06T10:01 | RSI(14) reversion · 1h | sell | DOGE-USD | 3.36 | 0.00 | rebalance down |
| 2026-11-06T10:01 | Candlestick reversal · 1h | buy | ETH-USD | 5.42 | — | entry signal |
| 2026-11-06T10:01 | VWAP momentum · 1h | buy | ETH-USD | 5.33 | — | entry signal |
| 2026-11-06T10:01 | VWAP momentum · 1h | buy | BTC-USD | 13.67 | — | entry signal |
| 2026-11-06T10:01 | VWAP momentum · 1h | sell | DOGE-USD | 3.47 | 0.01 | rebalance down |
| 2026-11-06T10:01 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.26 | — | entry signal |
| 2026-11-06T09:00 | VWAP reversion · 1h | buy | XRP-USD | 12.30 | — | entry signal |
| 2026-11-06T09:00 | Z-score reversion · 1h | buy | XRP-USD | 8.09 | — | entry signal |
| 2026-11-06T09:00 | Candlestick reversal · 1h | sell | ETH-USD | 5.37 | -0.04 | exit signal |
| 2026-11-06T09:00 | VWAP momentum · 1h | buy | DOGE-USD | 17.06 | — | entry signal |
| 2026-11-06T08:02 | MACD cross · 1h | sell | SOL-USD | 3.65 | -0.02 | rebalance down |
| 2026-11-06T08:00 | MACD cross · 1h | buy | ETH-USD | 14.65 | — | entry signal |
| 2026-11-06T08:00 | MACD cross · 1h | buy | BTC-USD | 14.65 | — | entry signal |
| 2026-11-06T08:00 | MACD cross · 1h | sell | DOGE-USD | 3.66 | -0.01 | rebalance down |
| 2026-11-06T07:00 | MFI reversion · 1h | buy | BTC-USD | 11.24 | — | entry signal |
| 2026-11-06T07:00 | MFI reversion · 1h | sell | XRP-USD | 4.38 | -0.05 | rebalance down |
| 2026-11-06T07:00 | MFI reversion · 1h | sell | SOL-USD | 4.50 | -0.02 | rebalance down |
| 2026-11-06T07:00 | MFI reversion · 1h | sell | ETH-USD | 4.50 | -0.02 | rebalance down |
| 2026-11-06T07:00 | MACD cross · 1h | buy | SOL-USD | 18.32 | — | entry signal |
| 2026-11-06T07:00 | MACD cross · 1h | buy | DOGE-USD | 18.32 | — | entry signal |
| 2026-11-06T06:20 | MFI reversion · 1h | sell | DOGE-USD | 6.41 | -0.09 | rebalance down |
| 2026-11-06T06:15 | Z-score reversion · 1h | sell | XRP-USD | 7.90 | -0.23 | stop-loss |
| 2026-11-06T06:00 | MFI reversion · 1h | buy | XRP-USD | 15.77 | — | entry signal |
| 2026-11-06T06:00 | MFI reversion · 1h | buy | SOL-USD | 15.77 | — | entry signal |
| 2026-11-06T06:00 | MFI reversion · 1h | buy | ETH-USD | 15.77 | — | entry signal |
| 2026-11-06T06:00 | Williams %R · 1h | buy | ETH-USD | 5.13 | — | entry signal |
| 2026-11-06T06:00 | Candlestick reversal · 1h | buy | SOL-USD | 5.41 | — | entry signal |
| 2026-11-06T04:00 | Candlestick reversal · 1h | sell | SOL-USD | 5.41 | -0.00 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 11:55:05.000128+00:00 -> 2026-11-06 12:05:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 11:55:05.000128+00:00 -> 2026-11-06 12:05:05.000128+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 11:55:05.000128+00:00 -> 2026-11-06 12:05:05.000128+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
