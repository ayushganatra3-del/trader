# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T20:25:05.000138+00:00 · 50048 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.30 (-11.70%)

Closed trades 151, win rate 37.1%, fees £4.31, max drawdown -12.11%.

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

Today: 36666 decisions in 3084 calls, $0.4537 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T20:25 | 3 / 13 / 14 | cash |  |
| Breezy | 2026-11-06T20:25 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-06T20:25 | 3 / 22 / 5 | MSTR 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |
| Candlestick reversal · 1h | DOGE-USD | 1.64 | +5.59% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.74 | 12.74 | 0 | — | 13.50 | 4.63 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 100.00 | -0.00 | 120 | 47.5 | -11.96 | -2.80 | -14.15 | 156 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.81 | -0.19 | 0 | — | 2.80 | 0.89 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.45 | -6.50 | 21 |
| 12 | Hold SPY | benchmark | 95.14 | -4.86 | 0 | — | -3.83 | -1.40 | -6.18 | 1 |
| 13 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.75 | -4.87 | -10.36 | 169 |
| 14 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.35 | -0.36 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 93.16 | -6.84 | 7 | 42.9 | -9.12 | -0.83 | -18.73 | 8 |
| 17 | Trend pullback · 1h | trend | 92.26 | -7.74 | 107 | 23.4 | -15.56 | -5.65 | -17.86 | 82 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 92.24 | -7.76 | 0 | — | -7.11 | -2.15 | -9.25 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 91.10 | -8.90 | 0 | — | -6.89 | -2.04 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.48 | -10.52 | 369 | 32.8 | -16.16 | -5.22 | -17.56 | 588 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.26 | -3.58 | -14.68 | 86 |
| 23 | Daily: Bullish score | daily | 88.47 | -11.53 | 15 | 20.0 | -5.29 | -0.71 | -16.58 | 14 |
| 24 | Hold BTC | benchmark | 88.39 | -11.61 | 1 | 0.0 | -5.56 | -0.67 | -14.09 | 1 |
| 25 | Agent | meta | 88.30 | -11.70 | 151 | 37.1 | -13.66 | -7.29 | -14.12 | 206 |
| 26 | Copy: Insider buying | copy | 87.95 | -12.05 | 40 | 37.5 | -24.09 | -4.71 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.64 | -13.36 | 166 | 27.1 | -15.09 | -3.35 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.68 | -14.32 | 71 | 14.1 | -13.55 | -2.77 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 84.17 | -15.83 | 17 | 47.1 | -33.40 | -2.14 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.60 | -5.59 | -18.68 | 98 |
| 31 | Stochastic reversion · 1h | reversion | 82.38 | -17.62 | 260 | 46.9 | -25.78 | -3.80 | -29.25 | 393 |
| 32 | Opening range 15m | breakout | 82.36 | -17.64 | 458 | 29.9 | -21.11 | -6.27 | -21.40 | 724 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.73 | -3.70 | -21.28 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.82 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.62 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.46 | -19.54 | 2 | 0.0 | -12.04 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.34 | -20.66 | 173 | 18.5 | -25.24 | -4.25 | -27.04 | 263 |
| 38 | MFI reversion · 1h | reversion | 78.69 | -21.31 | 331 | 34.4 | -18.88 | -2.72 | -20.68 | 158 |
| 39 | Ichimoku · 1h | trend | 77.81 | -22.19 | 94 | 14.9 | -23.36 | -4.80 | -29.43 | 126 |
| 40 | Bollinger breakout · 1h | breakout | 77.74 | -22.26 | 166 | 23.5 | -23.61 | -4.93 | -27.12 | 247 |
| 41 | CCI reversion · 1h | reversion | 77.06 | -22.94 | 286 | 46.2 | -30.23 | -4.96 | -31.74 | 467 |
| 42 | EMA 20/50 cross · 1h | trend | 75.89 | -24.11 | 102 | 10.8 | -24.76 | -4.51 | -30.58 | 134 |
| 43 | Heikin-Ashi · 1h | trend | 75.80 | -24.20 | 393 | 22.9 | -42.95 | -9.06 | -43.54 | 675 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.41 | -5.50 | -29.20 | 211 |
| 45 | Triple EMA stack · 1h | trend | 74.23 | -25.77 | 142 | 14.8 | -28.97 | -6.12 | -33.48 | 204 |
| 46 | Supertrend · 1h | trend | 73.59 | -26.41 | 166 | 13.3 | -30.56 | -5.35 | -34.80 | 217 |
| 47 | MACD cross · 1h | trend | 73.43 | -26.57 | 335 | 23.0 | -36.09 | -6.43 | -38.81 | 483 |
| 48 | RSI momentum · 1h | momentum | 73.40 | -26.60 | 158 | 12.7 | -28.15 | -5.37 | -32.60 | 219 |
| 49 | Z-score reversion · 1h | reversion | 73.31 | -26.69 | 161 | 36.0 | -25.42 | -3.78 | -28.33 | 234 |
| 50 | Bollinger reversion · 1h | reversion | 73.24 | -26.76 | 250 | 40.0 | -30.94 | -5.23 | -34.52 | 372 |
| 51 | Williams %R · 1h | reversion | 72.67 | -27.33 | 314 | 44.9 | -37.26 | -6.00 | -39.71 | 534 |
| 52 | Daily: Momentum burst | daily | 72.10 | -27.91 | 26 | 11.5 | -36.11 | -5.09 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.37 | -28.63 | 140 | 20.0 | -30.22 | -5.60 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 70.99 | -29.01 | 273 | 17.9 | -30.60 | -6.56 | -33.60 | 285 |
| 55 | ROC + volume · 1h | momentum | 70.05 | -29.95 | 345 | 25.5 | -37.02 | -7.21 | -37.27 | 378 |
| 56 | EMA 9/21 cross · 1h | trend | 67.34 | -32.66 | 241 | 10.0 | -40.48 | -8.41 | -40.76 | 338 |
| 57 | VWAP momentum · 1h | momentum | 67.25 | -32.75 | 776 | 22.0 | -56.05 | -12.48 | -56.13 | 1235 |
| 58 | Agent (ML meta-label) | meta | 66.68 | -33.32 | 1532 | 23.0 | -6.83 | -0.89 | -19.37 | 341 |
| 59 | RSI(14) reversion · 1h | reversion | 66.47 | -33.53 | 142 | 27.5 | -28.21 | -4.40 | -31.54 | 218 |
| 60 | Candlestick reversal · 1h | reversion | 65.60 | -34.40 | 406 | 28.6 | -38.07 | -7.00 | -38.76 | 570 |
| 61 | Three white soldiers | momentum | 65.60 | -34.40 | 458 | 15.9 | -48.00 | -22.48 | -48.01 | 640 |
| 62 | Max aggression: 1-day momentum | meta | 61.50 | -38.50 | 26 | 26.9 | -43.65 | -2.78 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -46.51 | -98.93 | 5218 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.62 | -25.97 | -80.80 | 1433 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -48.52 | -93.48 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.19 | -32.16 | -89.33 | 1910 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.80 | -40.50 | -90.90 | 2309 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.18 | -32.17 | -90.18 | 2192 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -55.78 | -97.72 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -60.12 | -96.29 | 3396 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.86 | -33.99 | -93.87 | 2450 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.56 | -36.89 | -82.58 | 1659 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -55.61 | -99.52 | 5983 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.61 | -44.53 | -92.70 | 2604 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.69 | -38.08 | -95.69 | 3409 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.89 | -99.80 | 6196 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -44.39 | -91.87 | 2281 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.44 | -26.10 | -75.60 | 1573 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -65.47 | -97.72 | 3513 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -62.71 | -98.78 | 4884 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.76 | -29.59 | -69.97 | 1206 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -56.64 | -94.71 | 2752 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.15 | -38.31 | -85.23 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -74.54 | -99.64 | 6372 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.16 | -31.71 | -89.27 | 2289 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.78 | -19.64 | -77.99 | 1744 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.07 | -38.21 | -91.13 | 2211 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.57 | -52.93 | -96.60 | 3874 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.58 | -57.47 | -89.60 | 2171 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.31 | -29.06 | -66.31 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.51 | -24.83 | -73.78 | 1269 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.91 | -17.68 | -78.55 | 1663 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.25 | -50.01 | -97.26 | 4329 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -121.31 | -99.93 | 8304 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T20:25 | MFI reversion · 1h | buy | NVDA | 6.13 | — | entry |
| 2026-11-06T20:25 | MFI reversion · 1h | buy | COIN | 7.16 | — | entry |
| 2026-11-06T20:25 | MFI reversion · 1h | buy | BITX | 7.16 | — | entry |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | XRP-USD | 3.97 | -0.08 | rebalance down |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | SOL-USD | 4.17 | 0.02 | rebalance down |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | ETH-USD | 4.12 | 0.00 | rebalance down |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | BTC-USD | 4.10 | 0.00 | rebalance down |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | AMZN | 4.09 | -0.01 | rebalance down |
| 2026-11-06T20:20 | Three white soldiers | sell | PLTR | 16.35 | -0.13 | stop-loss |
| 2026-11-06T20:15 | VWAP reversion · 1h | buy | COIN | 25.02 | — | entry |
| 2026-11-06T20:15 | Three white soldiers | sell | BTC-USD | 16.35 | -0.13 | exit signal |
| 2026-11-06T20:10 | Three white soldiers | buy | PLTR | 16.48 | — | entry signal |
| 2026-11-06T20:10 | Three white soldiers | buy | COIN | 16.48 | — | entry signal |
| 2026-11-06T20:10 | Three white soldiers | buy | BTC-USD | 16.48 | — | entry signal |
| 2026-11-06T20:05 | Agent (ML meta-label) | buy | LABU | 3.93 | — | entry |
| 2026-11-06T20:05 | Agent (ML meta-label) | sell | MSTR | 4.40 | 0.03 | selected signal exited |
| 2026-11-06T20:05 | OBV trend · 1h | sell | AMZN | 17.74 | -0.07 | target is flat |
| 2026-11-06T20:00 | MFI reversion · 1h | buy | PLTR | 4.67 | — | entry |
| 2026-11-06T20:00 | MFI reversion · 1h | sell | ETHU | 4.67 | 0.03 | target is flat |
| 2026-11-06T20:00 | Candlestick reversal · 1h | buy | QQQ | 4.69 | — | entry |
| 2026-11-06T19:55 | Agent (ML meta-label) | buy | IWM | 3.42 | — | entry |
| 2026-11-06T19:55 | Agent (ML meta-label) | sell | BTC-USD | 3.42 | -0.02 | selected signal exited |
| 2026-11-06T19:40 | Agent (ML meta-label) | buy | UPRO | 1.32 | — | entry |
| 2026-11-06T19:40 | Agent (ML meta-label) | buy | TQQQ | 3.53 | — | entry |
| 2026-11-06T19:40 | Agent (ML meta-label) | sell | IWM | 3.91 | 0.00 | selected signal exited |
| 2026-11-06T19:40 | VWAP reversion · 1h | buy | NVDA | 24.98 | — | entry |
| 2026-11-06T19:35 | Agent (aggressive) | sell | AMZN | 41.87 | -0.27 | selected signal exited |
| 2026-11-06T19:35 | Agent | sell | AMZN | 17.57 | -0.11 | selected signal exited |
| 2026-11-06T19:31 | Agent (ML meta-label) | buy | BTC-USD | 3.44 | — | entry |
| 2026-11-06T19:31 | Agent (ML meta-label) | sell | LABU | 3.50 | 0.00 | selected signal exited |
| 2026-11-06T19:31 | MFI reversion · 1h | buy | ETHU | 4.63 | — | entry signal |
| 2026-11-06T19:31 | Candlestick reversal · 1h | buy | AMD | 5.94 | — | entry |
| 2026-11-06T19:31 | Candlestick reversal · 1h | sell | QQQ | 4.73 | -0.02 | target is flat |
| 2026-11-06T19:31 | VWAP momentum · 1h | buy | ETHU | 7.43 | — | entry signal |
| 2026-11-06T19:31 | VWAP momentum · 1h | buy | BTC-USD | 7.46 | — | entry |
| 2026-11-06T19:31 | VWAP momentum · 1h | buy | BITX | 7.46 | — | entry signal |
| 2026-11-06T19:31 | VWAP momentum · 1h | buy | AMD | 7.46 | — | entry signal |
| 2026-11-06T19:31 | VWAP momentum · 1h | sell | TNA | 6.01 | 0.04 | rebalance down |
| 2026-11-06T19:31 | VWAP momentum · 1h | sell | LABU | 5.90 | -0.02 | rebalance down |
| 2026-11-06T19:31 | VWAP momentum · 1h | sell | IWM | 6.01 | 0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 20:25:05.000138+00:00 -> 2026-11-06 20:35:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 20:25:05.000138+00:00 -> 2026-11-06 20:35:05.000138+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 20:25:05.000138+00:00 -> 2026-11-06 20:35:05.000138+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
