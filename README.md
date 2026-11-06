# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T12:25:05.000143+00:00 · 49660 ticks

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

Today: 9597 decisions in 1920 calls, $0.1341 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T12:25 | 2 / 2 / 1 | SOL-USD 15% |  |
| Breezy | 2026-11-06T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T12:25 | 4 / 1 / 0 | ETH-USD 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.17 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.13 | 12.13 | 0 | — | 13.22 | 4.52 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.82 | 7.82 | 29 | 27.6 | 16.51 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.06 | 0.61 | -9.63 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.68 | -0.32 | 0 | — | 2.97 | 0.93 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.53 | -1.47 | 111 | 44.1 | -13.54 | -3.28 | -14.25 | 150 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.77 | -2.23 | 117 | 35.0 | 4.93 | 2.51 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Agent (rotation) | meta | 95.25 | -4.75 | 175 | 28.0 | -6.68 | -3.77 | -10.36 | 173 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.06 | 0.10 | -9.18 | 218 |
| 14 | Hold SPY | benchmark | 94.25 | -5.75 | 0 | — | -4.45 | -1.64 | -6.18 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Trend pullback · 1h | trend | 92.40 | -7.60 | 105 | 22.9 | -15.25 | -5.48 | -17.86 | 81 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.31 | -7.68 | 7 | 42.9 | -13.15 | -1.39 | -18.73 | 8 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 91.07 | -8.93 | 0 | — | -8.33 | -2.52 | -9.25 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.40 | -9.60 | 0 | — | -7.33 | -2.17 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.95 | -5.09 | -17.56 | 579 |
| 22 | Daily: Bullish score | daily | 89.24 | -10.76 | 14 | 21.4 | -4.51 | -0.57 | -16.58 | 14 |
| 23 | Hold BTC | benchmark | 88.78 | -11.22 | 1 | 0.0 | -4.76 | -0.58 | -13.78 | 1 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.53 | -3.65 | -14.68 | 86 |
| 25 | Agent | meta | 88.46 | -11.54 | 148 | 37.2 | -14.20 | -7.57 | -14.60 | 211 |
| 26 | Parabolic SAR · 1h | trend | 87.68 | -12.32 | 166 | 27.1 | -14.07 | -3.08 | -20.02 | 240 |
| 27 | Copy: Insider buying | copy | 86.82 | -13.18 | 40 | 37.5 | -25.08 | -4.95 | -26.04 | 65 |
| 28 | Donchian 55/20 · 1h | breakout | 86.74 | -13.27 | 71 | 14.1 | -12.50 | -2.52 | -19.94 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.13 | -14.87 | 17 | 47.1 | -30.71 | -1.88 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.53 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.67 | -16.33 | 446 | 30.7 | -19.82 | -5.84 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.83 | -17.16 | 144 | 27.8 | -15.84 | -3.55 | -21.39 | 101 |
| 33 | Keltner breakout · 1h | breakout | 82.09 | -17.91 | 106 | 23.6 | -21.20 | -4.34 | -24.41 | 172 |
| 34 | Stochastic reversion · 1h | reversion | 81.58 | -18.43 | 259 | 47.1 | -28.62 | -4.45 | -29.25 | 386 |
| 35 | Connors RSI(2) · 1h | reversion | 80.82 | -19.18 | 203 | 39.9 | -20.51 | -6.77 | -21.05 | 129 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.06 | -19.94 | 2 | 0.0 | -14.78 | -2.03 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.76 | -20.23 | 171 | 18.1 | -23.93 | -3.97 | -26.36 | 262 |
| 38 | MFI reversion · 1h | reversion | 79.39 | -20.61 | 328 | 33.8 | -18.85 | -2.70 | -20.96 | 153 |
| 39 | Bollinger breakout · 1h | breakout | 79.27 | -20.73 | 165 | 23.6 | -22.07 | -4.55 | -26.52 | 245 |
| 40 | Ichimoku · 1h | trend | 78.80 | -21.20 | 94 | 14.9 | -22.37 | -4.53 | -28.82 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.85 | -22.15 | 286 | 46.2 | -29.54 | -4.77 | -30.72 | 452 |
| 42 | Heikin-Ashi · 1h | trend | 77.11 | -22.89 | 386 | 23.1 | -42.65 | -8.92 | -43.30 | 672 |
| 43 | EMA 20/50 cross · 1h | trend | 76.64 | -23.36 | 102 | 10.8 | -23.25 | -4.17 | -30.17 | 133 |
| 44 | Triple EMA stack · 1h | trend | 75.13 | -24.87 | 142 | 14.8 | -28.62 | -5.96 | -33.06 | 206 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.66 | -5.50 | -29.20 | 212 |
| 46 | RSI momentum · 1h | momentum | 74.15 | -25.85 | 158 | 12.7 | -27.35 | -5.15 | -32.33 | 219 |
| 47 | Supertrend · 1h | trend | 74.14 | -25.86 | 166 | 13.3 | -29.52 | -5.07 | -34.26 | 216 |
| 48 | MACD cross · 1h | trend | 73.91 | -26.09 | 334 | 23.1 | -35.17 | -6.14 | -38.81 | 475 |
| 49 | Z-score reversion · 1h | reversion | 73.26 | -26.74 | 160 | 35.6 | -27.74 | -4.28 | -28.32 | 225 |
| 50 | Donchian 20/10 · 1h | breakout | 72.48 | -27.52 | 140 | 20.0 | -29.12 | -5.32 | -34.25 | 212 |
| 51 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.53 | -4.93 | -37.45 | 30 |
| 52 | Bollinger reversion · 1h | reversion | 72.11 | -27.89 | 248 | 39.5 | -33.71 | -6.18 | -34.17 | 375 |
| 53 | Williams %R · 1h | reversion | 71.96 | -28.04 | 314 | 44.9 | -39.01 | -6.49 | -39.38 | 529 |
| 54 | ROC + volume · 1h | momentum | 71.68 | -28.32 | 344 | 25.6 | -36.73 | -7.11 | -37.13 | 380 |
| 55 | OBV trend · 1h | momentum | 71.53 | -28.47 | 266 | 17.3 | -31.75 | -6.74 | -33.83 | 292 |
| 56 | VWAP momentum · 1h | momentum | 68.41 | -31.59 | 760 | 22.2 | -55.54 | -12.21 | -56.28 | 1220 |
| 57 | EMA 9/21 cross · 1h | trend | 68.16 | -31.84 | 241 | 10.0 | -39.26 | -8.01 | -39.93 | 335 |
| 58 | RSI(14) reversion · 1h | reversion | 66.83 | -33.17 | 142 | 27.5 | -28.09 | -4.34 | -31.29 | 206 |
| 59 | Three white soldiers | momentum | 66.21 | -33.79 | 453 | 16.1 | -47.84 | -21.95 | -47.84 | 635 |
| 60 | Agent (ML meta-label) | meta | 65.34 | -34.66 | 1508 | 22.3 | -11.30 | -1.68 | -18.37 | 328 |
| 61 | Candlestick reversal · 1h | reversion | 65.17 | -34.83 | 397 | 28.5 | -39.06 | -7.22 | -39.41 | 566 |
| 62 | Max aggression: 1-day momentum | meta | 62.20 | -37.80 | 26 | 26.9 | -41.38 | -2.54 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.85 | -98.94 | 5139 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.15 | -25.40 | -80.30 | 1407 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.25 | -46.71 | -93.37 | 2488 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.00 | -30.79 | -89.13 | 1895 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.62 | -38.92 | -90.80 | 2284 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.15 | -31.00 | -90.24 | 2194 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -53.10 | -97.70 | 3433 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -58.19 | -96.16 | 3345 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -32.63 | -93.62 | 2432 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.59 | -35.66 | -81.89 | 1630 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -52.65 | -99.51 | 5940 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.48 | -42.62 | -92.58 | 2580 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.71 | -36.62 | -95.71 | 3403 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -68.55 | -99.80 | 6127 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.51 | -41.75 | -91.67 | 2244 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.90 | -26.59 | -75.15 | 1566 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -59.37 | -97.68 | 3478 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -58.92 | -98.77 | 4841 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.32 | -28.45 | -70.08 | 1198 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.48 | -53.35 | -94.55 | 2735 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.73 | -36.87 | -84.90 | 1770 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.84 | -99.64 | 6315 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.08 | -30.65 | -89.10 | 2271 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.53 | -19.28 | -77.74 | 1732 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.04 | -36.31 | -91.07 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.58 | -50.72 | -96.58 | 3836 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.47 | -55.79 | -89.49 | 2162 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.54 | -27.68 | -65.96 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.09 | -24.05 | -73.81 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.54 | -17.96 | -78.66 | 1664 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.25 | -47.98 | -97.25 | 4302 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -95.56 | -99.93 | 8200 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T12:00 | CCI reversion · 1h | buy | XRP-USD | 7.41 | — | entry |
| 2026-11-06T12:00 | CCI reversion · 1h | buy | ETH-USD | 10.35 | — | rebalance up |
| 2026-11-06T12:00 | CCI reversion · 1h | buy | BTC-USD | 4.47 | — | rebalance up |
| 2026-11-06T12:00 | CCI reversion · 1h | sell | SOL-USD | 11.11 | 0.04 | exit signal |
| 2026-11-06T12:00 | CCI reversion · 1h | sell | DOGE-USD | 11.13 | 0.04 | exit signal |
| 2026-11-06T12:00 | Williams %R · 1h | sell | SOL-USD | 5.53 | -0.01 | exit signal |
| 2026-11-06T12:00 | Williams %R · 1h | sell | ETH-USD | 5.15 | 0.02 | exit signal |
| 2026-11-06T12:00 | Stochastic reversion · 1h | sell | SOL-USD | 5.88 | 0.06 | exit signal |
| 2026-11-06T12:00 | Stochastic reversion · 1h | sell | ETH-USD | 5.82 | 0.00 | exit signal |
| 2026-11-06T12:00 | Bollinger reversion · 1h | sell | ETH-USD | 4.00 | 0.00 | exit signal |
| 2026-11-06T12:00 | Candlestick reversal · 1h | buy | XRP-USD | 5.01 | — | entry signal |
| 2026-11-06T12:00 | Heikin-Ashi · 1h | buy | SOL-USD | 19.26 | — | entry signal |
| 2026-11-06T12:00 | MACD cross · 1h | buy | XRP-USD | 12.29 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 12:25:05.000143+00:00 -> 2026-11-06 12:35:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 12:25:05.000143+00:00 -> 2026-11-06 12:35:05.000143+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 12:25:05.000143+00:00 -> 2026-11-06 12:35:05.000143+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
