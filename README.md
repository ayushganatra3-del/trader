# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T07:25:05.000122+00:00 · 49406 ticks

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

Today: 5787 decisions in 1158 calls, $0.0809 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T07:25 | 1 / 1 / 3 | cash |  |
| Breezy | 2026-11-06T07:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T07:25 | 0 / 5 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.87 | 11.87 | 0 | — | 13.22 | 4.50 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.82 | 7.82 | 29 | 27.6 | 16.51 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.05 | 0.61 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.45 | -0.55 | 0 | — | 2.97 | 0.93 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.30 | -1.70 | 111 | 44.1 | -13.59 | -3.31 | -14.16 | 150 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.77 | -2.23 | 117 | 35.0 | 4.93 | 2.51 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Agent (rotation) | meta | 95.18 | -4.82 | 175 | 28.0 | -7.17 | -4.37 | -10.36 | 173 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.06 | 0.10 | -9.18 | 218 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 15 | Hold SPY | benchmark | 94.03 | -5.97 | 0 | — | -4.45 | -1.64 | -6.18 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.31 | -7.68 | 7 | 42.9 | -13.09 | -1.39 | -18.69 | 8 |
| 17 | Trend pullback · 1h | trend | 92.24 | -7.76 | 105 | 22.9 | -15.25 | -5.48 | -17.86 | 81 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 90.86 | -9.14 | 0 | — | -8.33 | -2.52 | -9.25 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.19 | -9.81 | 0 | — | -7.33 | -2.17 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.95 | -5.09 | -17.56 | 579 |
| 22 | Daily: Bullish score | daily | 89.13 | -10.87 | 14 | 21.4 | -4.51 | -0.57 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.26 | -3.55 | -14.68 | 86 |
| 24 | Agent | meta | 88.46 | -11.54 | 148 | 37.2 | -14.20 | -7.57 | -14.60 | 211 |
| 25 | Parabolic SAR · 1h | trend | 87.63 | -12.38 | 166 | 27.1 | -14.67 | -3.22 | -20.02 | 241 |
| 26 | Hold BTC | benchmark | 87.55 | -12.45 | 1 | 0.0 | -5.73 | -0.74 | -13.74 | 1 |
| 27 | Donchian 55/20 · 1h | breakout | 86.68 | -13.32 | 71 | 14.1 | -12.50 | -2.52 | -19.94 | 104 |
| 28 | Copy: Insider buying | copy | 86.62 | -13.38 | 40 | 37.5 | -25.08 | -4.95 | -26.04 | 65 |
| 29 | Max aggression: 5-day momentum | meta | 85.13 | -14.87 | 17 | 47.1 | -30.71 | -1.88 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.53 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.67 | -16.33 | 446 | 30.7 | -19.82 | -5.84 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.79 | -17.21 | 144 | 27.8 | -16.01 | -3.59 | -21.39 | 102 |
| 33 | Keltner breakout · 1h | breakout | 82.04 | -17.96 | 106 | 23.6 | -22.10 | -4.55 | -24.41 | 175 |
| 34 | Stochastic reversion · 1h | reversion | 81.25 | -18.75 | 255 | 46.7 | -28.84 | -4.49 | -29.24 | 386 |
| 35 | Connors RSI(2) · 1h | reversion | 80.73 | -19.27 | 203 | 39.9 | -20.51 | -6.77 | -21.05 | 129 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.06 | -19.94 | 2 | 0.0 | -14.78 | -2.03 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.76 | -20.23 | 171 | 18.1 | -23.48 | -3.88 | -26.36 | 260 |
| 38 | Bollinger breakout · 1h | breakout | 79.23 | -20.77 | 165 | 23.6 | -22.40 | -4.63 | -26.52 | 246 |
| 39 | Ichimoku · 1h | trend | 78.75 | -21.25 | 94 | 14.9 | -22.37 | -4.53 | -28.82 | 125 |
| 40 | MFI reversion · 1h | reversion | 78.43 | -21.57 | 328 | 33.8 | -19.51 | -2.80 | -20.56 | 154 |
| 41 | CCI reversion · 1h | reversion | 77.27 | -22.73 | 284 | 45.8 | -29.98 | -4.87 | -30.69 | 451 |
| 42 | Heikin-Ashi · 1h | trend | 76.99 | -23.01 | 386 | 23.1 | -42.70 | -8.93 | -43.30 | 670 |
| 43 | EMA 20/50 cross · 1h | trend | 76.60 | -23.40 | 102 | 10.8 | -22.53 | -4.03 | -30.17 | 131 |
| 44 | Triple EMA stack · 1h | trend | 75.08 | -24.92 | 142 | 14.8 | -29.45 | -6.15 | -33.06 | 207 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.84 | -5.54 | -29.20 | 213 |
| 46 | RSI momentum · 1h | momentum | 74.06 | -25.94 | 158 | 12.7 | -27.86 | -5.27 | -32.33 | 220 |
| 47 | Supertrend · 1h | trend | 74.01 | -25.98 | 166 | 13.3 | -29.83 | -5.14 | -34.26 | 217 |
| 48 | MACD cross · 1h | trend | 73.13 | -26.87 | 334 | 23.1 | -36.39 | -6.41 | -38.81 | 475 |
| 49 | Z-score reversion · 1h | reversion | 72.71 | -27.29 | 160 | 35.6 | -28.82 | -4.49 | -28.88 | 226 |
| 50 | Donchian 20/10 · 1h | breakout | 72.43 | -27.57 | 140 | 20.0 | -29.52 | -5.41 | -34.25 | 213 |
| 51 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.53 | -4.93 | -37.46 | 30 |
| 52 | Bollinger reversion · 1h | reversion | 71.96 | -28.04 | 244 | 38.9 | -34.16 | -6.28 | -34.52 | 375 |
| 53 | Williams %R · 1h | reversion | 71.75 | -28.25 | 310 | 44.8 | -39.45 | -6.58 | -39.70 | 528 |
| 54 | ROC + volume · 1h | momentum | 71.63 | -28.37 | 344 | 25.6 | -37.24 | -7.26 | -37.68 | 383 |
| 55 | OBV trend · 1h | momentum | 71.41 | -28.59 | 266 | 17.3 | -32.65 | -6.89 | -34.09 | 294 |
| 56 | VWAP momentum · 1h | momentum | 68.18 | -31.82 | 760 | 22.2 | -55.67 | -12.26 | -56.28 | 1216 |
| 57 | EMA 9/21 cross · 1h | trend | 68.08 | -31.92 | 241 | 10.0 | -39.24 | -8.01 | -39.91 | 335 |
| 58 | Three white soldiers | momentum | 66.21 | -33.79 | 453 | 16.1 | -47.89 | -22.10 | -47.89 | 639 |
| 59 | RSI(14) reversion · 1h | reversion | 65.84 | -34.16 | 142 | 27.5 | -28.97 | -4.52 | -31.28 | 205 |
| 60 | Agent (ML meta-label) | meta | 65.20 | -34.80 | 1508 | 22.3 | -11.33 | -1.69 | -18.95 | 331 |
| 61 | Candlestick reversal · 1h | reversion | 64.87 | -35.13 | 396 | 28.5 | -38.95 | -7.20 | -39.07 | 564 |
| 62 | Max aggression: 1-day momentum | meta | 62.20 | -37.80 | 26 | 26.9 | -41.38 | -2.54 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -45.53 | -98.92 | 5126 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.24 | -25.53 | -80.31 | 1406 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.24 | -46.56 | -93.31 | 2486 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.12 | -31.24 | -89.13 | 1894 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.62 | -38.93 | -90.73 | 2281 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.25 | -31.11 | -90.33 | 2200 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -53.14 | -97.68 | 3428 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.10 | -58.63 | -96.14 | 3347 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -32.42 | -93.63 | 2425 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.52 | -35.46 | -81.82 | 1628 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -52.56 | -99.51 | 5937 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.50 | -42.79 | -92.53 | 2579 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.73 | -36.47 | -95.76 | 3406 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -69.39 | -99.80 | 6124 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.61 | -42.83 | -91.61 | 2243 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.95 | -26.74 | -75.04 | 1562 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -59.73 | -97.65 | 3476 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -58.83 | -98.77 | 4837 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.30 | -28.41 | -70.08 | 1199 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.48 | -53.44 | -94.50 | 2733 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.73 | -36.89 | -84.77 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -70.84 | -99.65 | 6321 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.09 | -30.68 | -89.09 | 2268 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.55 | -19.30 | -77.75 | 1732 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.00 | -36.16 | -91.01 | 2217 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.58 | -50.91 | -96.58 | 3837 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -55.00 | -89.40 | 2155 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.49 | -27.57 | -65.86 | 804 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.97 | -23.86 | -73.80 | 1253 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.61 | -17.85 | -78.61 | 1661 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -48.30 | -97.27 | 4306 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -93.65 | -99.93 | 8199 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-06T04:00 | VWAP momentum · 1h | sell | SOL-USD | 15.74 | -0.19 | exit signal |
| 2026-11-06T04:00 | VWAP momentum · 1h | sell | DOGE-USD | 16.86 | -0.14 | exit signal |
| 2026-11-06T04:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 19.11 | -0.17 | exit signal |
| 2026-11-06T03:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.28 | — | entry signal |
| 2026-11-06T02:50 | MFI reversion · 1h | buy | DOGE-USD | 6.54 | — | rebalance up |
| 2026-11-06T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 17.00 | — | entry signal |
| 2026-11-06T02:00 | VWAP momentum · 1h | sell | BTC-USD | 17.00 | -0.16 | exit signal |
| 2026-11-06T01:45 | MFI reversion · 1h | buy | DOGE-USD | 4.42 | — | rebalance up |
| 2026-11-06T01:15 | MFI reversion · 1h | sell | DOGE-USD | 4.34 | -0.03 | rebalance down |
| 2026-11-06T01:05 | Three white soldiers | sell | SOL-USD | 16.46 | -0.18 | exit signal |
| 2026-11-06T01:05 | Three white soldiers | sell | DOGE-USD | 16.49 | -0.14 | exit signal |
| 2026-11-06T01:00 | MFI reversion · 1h | buy | DOGE-USD | 13.18 | — | entry signal |
| 2026-11-06T01:00 | CCI reversion · 1h | buy | ETH-USD | 1.34 | — | rebalance up |
| 2026-11-06T01:00 | CCI reversion · 1h | buy | DOGE-USD | 11.09 | — | entry signal |
| 2026-11-06T01:00 | CCI reversion · 1h | sell | SOL-USD | 4.51 | -0.00 | rebalance down |
| 2026-11-06T01:00 | CCI reversion · 1h | sell | BTC-USD | 7.93 | 0.05 | rebalance down |
| 2026-11-06T01:00 | Williams %R · 1h | buy | SOL-USD | 5.54 | — | entry signal |
| 2026-11-06T01:00 | Williams %R · 1h | buy | DOGE-USD | 5.54 | — | entry signal |
| 2026-11-06T01:00 | Williams %R · 1h | buy | BTC-USD | 5.54 | — | entry signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | SOL-USD | 9.92 | -0.04 | exit signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | ETH-USD | 9.87 | -0.12 | exit signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 9.82 | -0.01 | exit signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | BTC-USD | 9.91 | -0.05 | exit signal |
| 2026-11-06T01:00 | Z-score reversion · 1h | buy | XRP-USD | 8.14 | — | entry signal |
| 2026-11-06T01:00 | Z-score reversion · 1h | buy | DOGE-USD | 8.14 | — | entry signal |
| 2026-11-06T01:00 | RSI(14) reversion · 1h | buy | ETH-USD | 16.57 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 07:25:05.000122+00:00 -> 2026-11-06 07:35:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 07:25:05.000122+00:00 -> 2026-11-06 07:35:05.000122+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 07:25:05.000122+00:00 -> 2026-11-06 07:35:05.000122+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
