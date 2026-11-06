# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T15:25:05.000137+00:00 · 49807 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.49 (-11.51%)

Closed trades 148, win rate 37.2%, fees £4.18, max drawdown -11.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMZN | 17.72 | +0.03 |

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

Today: 14853 decisions in 2361 calls, $0.1991 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T15:25 | 1 / 22 / 8 | cash |  |
| Breezy | 2026-11-06T15:25 | 0 / 28 / 3 | cash |  |
| Boozy | 2026-11-06T15:25 | 4 / 24 / 3 | BITX 55% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.73 | 11.73 | 0 | — | 12.53 | 4.26 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.39 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.65 | 2.65 | 29 | 44.8 | 1.00 | 0.36 | -9.64 | 30 |
| 5 | VWAP reversion · 1h | reversion | 100.17 | 0.17 | 115 | 46.1 | -12.62 | -2.97 | -14.50 | 147 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.80 | -0.20 | 0 | — | 2.82 | 0.89 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.98 | -2.02 | 119 | 35.3 | 5.16 | 2.62 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Hold SPY | benchmark | 95.43 | -4.57 | 0 | — | -3.50 | -1.25 | -6.18 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 13 | Gap and go | momentum | 95.18 | -4.82 | 166 | 28.3 | -0.25 | 0.00 | -9.18 | 226 |
| 14 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.17 | -4.37 | -10.36 | 173 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 93.76 | -6.24 | 7 | 42.9 | -8.50 | -0.74 | -18.73 | 8 |
| 17 | Trend pullback · 1h | trend | 92.49 | -7.51 | 106 | 22.6 | -15.34 | -5.51 | -17.86 | 81 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.58 | -8.42 | 0 | — | -6.36 | -1.84 | -10.64 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 91.30 | -8.70 | 0 | — | -8.02 | -2.46 | -9.25 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 89.68 | -10.32 | 366 | 33.1 | -16.14 | -5.17 | -17.56 | 584 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.26 | -3.55 | -14.68 | 86 |
| 23 | Agent | meta | 88.49 | -11.51 | 148 | 37.2 | -14.17 | -7.55 | -14.62 | 212 |
| 24 | Daily: Bullish score | daily | 88.29 | -11.71 | 15 | 20.0 | -5.47 | -0.74 | -16.58 | 14 |
| 25 | Hold BTC | benchmark | 88.26 | -11.74 | 1 | 0.0 | -5.72 | -0.74 | -14.09 | 1 |
| 26 | Copy: Insider buying | copy | 87.01 | -12.99 | 40 | 37.5 | -24.93 | -4.91 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.49 | -13.52 | 166 | 27.1 | -14.63 | -3.22 | -20.50 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 85.52 | -14.48 | 71 | 14.1 | -13.71 | -2.79 | -20.43 | 104 |
| 29 | Agent (aggressive) | meta | 84.31 | -15.69 | 72 | 30.6 | -18.50 | -5.50 | -19.08 | 100 |
| 30 | Max aggression: 5-day momentum | meta | 83.55 | -16.45 | 17 | 47.1 | -33.86 | -2.17 | -40.71 | 25 |
| 31 | Opening range 15m | breakout | 82.65 | -17.35 | 449 | 30.5 | -20.73 | -6.13 | -21.31 | 719 |
| 32 | Stochastic reversion · 1h | reversion | 82.29 | -17.71 | 260 | 46.9 | -25.82 | -3.78 | -29.25 | 387 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.73 | -3.67 | -21.28 | 100 |
| 34 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.58 | -24.50 | 172 |
| 35 | Connors RSI(2) · 1h | reversion | 80.90 | -19.10 | 204 | 40.2 | -20.62 | -6.82 | -21.05 | 129 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.44 | -19.56 | 2 | 0.0 | -12.03 | -1.55 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.63 | -20.36 | 171 | 18.1 | -25.00 | -4.18 | -27.04 | 263 |
| 38 | MFI reversion · 1h | reversion | 79.02 | -20.98 | 329 | 34.0 | -19.45 | -2.57 | -22.54 | 154 |
| 39 | Bollinger breakout · 1h | breakout | 78.10 | -21.90 | 166 | 23.5 | -23.24 | -4.82 | -26.78 | 246 |
| 40 | Ichimoku · 1h | trend | 77.74 | -22.26 | 94 | 14.9 | -23.44 | -4.78 | -29.43 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.03 | -22.97 | 286 | 46.2 | -30.39 | -4.94 | -31.56 | 452 |
| 42 | Heikin-Ashi · 1h | trend | 75.79 | -24.21 | 388 | 22.9 | -42.94 | -8.97 | -43.20 | 667 |
| 43 | EMA 20/50 cross · 1h | trend | 75.78 | -24.23 | 102 | 10.8 | -24.35 | -4.40 | -30.58 | 133 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.12 | -5.38 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.10 | -25.90 | 142 | 14.8 | -29.71 | -6.24 | -33.48 | 206 |
| 46 | MACD cross · 1h | trend | 73.63 | -26.37 | 334 | 23.1 | -35.93 | -6.34 | -38.81 | 474 |
| 47 | Supertrend · 1h | trend | 73.57 | -26.43 | 166 | 13.3 | -30.58 | -5.31 | -34.80 | 217 |
| 48 | Z-score reversion · 1h | reversion | 73.37 | -26.63 | 160 | 35.6 | -25.24 | -3.70 | -28.32 | 225 |
| 49 | RSI momentum · 1h | momentum | 73.35 | -26.65 | 158 | 12.7 | -28.20 | -5.34 | -32.60 | 219 |
| 50 | Bollinger reversion · 1h | reversion | 73.00 | -27.00 | 249 | 39.8 | -31.10 | -5.27 | -34.52 | 375 |
| 51 | Williams %R · 1h | reversion | 72.41 | -27.59 | 314 | 44.9 | -37.36 | -5.97 | -39.71 | 529 |
| 52 | Daily: Momentum burst | daily | 71.96 | -28.04 | 26 | 11.5 | -36.23 | -5.07 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.40 | -28.60 | 140 | 20.0 | -30.19 | -5.55 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 71.15 | -28.85 | 268 | 17.2 | -31.65 | -6.87 | -34.18 | 291 |
| 55 | ROC + volume · 1h | momentum | 70.32 | -29.68 | 345 | 25.5 | -37.67 | -7.37 | -37.80 | 381 |
| 56 | VWAP momentum · 1h | momentum | 67.45 | -32.55 | 763 | 22.3 | -56.34 | -12.45 | -56.47 | 1216 |
| 57 | EMA 9/21 cross · 1h | trend | 67.42 | -32.58 | 241 | 10.0 | -39.91 | -8.20 | -40.24 | 335 |
| 58 | Agent (ML meta-label) | meta | 66.77 | -33.23 | 1516 | 22.7 | -10.96 | -1.65 | -21.81 | 338 |
| 59 | RSI(14) reversion · 1h | reversion | 66.61 | -33.39 | 142 | 27.5 | -28.28 | -4.38 | -31.29 | 205 |
| 60 | Three white soldiers | momentum | 66.20 | -33.80 | 453 | 16.1 | -47.58 | -21.71 | -47.61 | 636 |
| 61 | Candlestick reversal · 1h | reversion | 65.55 | -34.45 | 400 | 28.5 | -38.27 | -6.99 | -38.94 | 563 |
| 62 | Max aggression: 1-day momentum | meta | 61.04 | -38.96 | 26 | 26.9 | -44.04 | -2.79 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -44.89 | -98.95 | 5159 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.51 | -25.70 | -80.58 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.39 | -47.38 | -93.40 | 2493 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.14 | -31.18 | -89.21 | 1901 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.76 | -39.40 | -90.77 | 2290 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.12 | -31.08 | -90.16 | 2191 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -53.57 | -97.70 | 3439 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -59.20 | -96.24 | 3363 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -32.80 | -93.67 | 2430 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.03 | -36.75 | -82.03 | 1639 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -53.27 | -99.52 | 5947 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.61 | -43.31 | -92.71 | 2592 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.70 | -36.74 | -95.71 | 3405 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.21 | -99.80 | 6136 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.68 | -43.03 | -91.68 | 2250 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.32 | -26.78 | -75.64 | 1576 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -60.67 | -97.68 | 3478 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.79 | -59.60 | -98.79 | 4856 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.34 | -28.42 | -69.98 | 1203 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -54.66 | -94.66 | 2739 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.03 | -37.46 | -85.21 | 1777 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -70.06 | -99.65 | 6330 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.26 | -31.07 | -89.29 | 2287 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.75 | -19.51 | -77.84 | 1740 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.07 | -36.31 | -91.16 | 2223 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.61 | -51.15 | -96.62 | 3855 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.49 | -55.20 | -89.50 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.31 | -28.35 | -66.74 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.41 | -24.34 | -73.54 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.56 | -17.89 | -78.67 | 1657 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -48.31 | -97.28 | 4308 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -93.93 | -99.93 | 8227 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T15:25 | Agent (ML meta-label) | buy | SQQQ | 4.45 | — | following MFI reversion |
| 2026-11-06T15:25 | VWAP reversion · 1h | buy | UPRO | 8.34 | — | rebalance up |
| 2026-11-06T15:25 | VWAP reversion · 1h | buy | TNA | 8.18 | — | rebalance up |
| 2026-11-06T15:25 | VWAP reversion · 1h | buy | IWM | 8.28 | — | rebalance up |
| 2026-11-06T15:25 | VWAP reversion · 1h | sell | NVDA | 16.53 | 0.44 | target is flat |
| 2026-11-06T15:25 | Opening range 30m | buy | AAPL | 9.03 | — | entry signal |
| 2026-11-06T15:25 | Opening range 30m | sell | TSLA | 4.55 | 0.00 | rebalance down |
| 2026-11-06T15:25 | Opening range 30m | sell | IWM | 4.48 | -0.01 | rebalance down |
| 2026-11-06T15:25 | Gap and go | sell | AMD | 23.58 | -0.31 | exit signal |
| 2026-11-06T15:21 | Opening range 15m | buy | MSFT | 7.46 | — | entry |
| 2026-11-06T15:21 | Opening range 15m | sell | COIN | 7.46 | -0.15 | exit signal |
| 2026-11-06T15:15 | Opening range 30m | buy | TSLA | 22.47 | — | entry signal |
| 2026-11-06T15:15 | Opening range 30m | buy | TNA | 22.47 | — | entry signal |
| 2026-11-06T15:15 | Opening range 30m | buy | MSFT | 22.47 | — | entry signal |
| 2026-11-06T15:15 | Opening range 30m | buy | IWM | 22.47 | — | entry signal |
| 2026-11-06T15:10 | Opening range 15m | buy | TSLA | 7.12 | — | entry |
| 2026-11-06T15:10 | Opening range 15m | buy | AAPL | 7.50 | — | entry |
| 2026-11-06T15:10 | Opening range 15m | sell | TECL | 7.39 | -0.21 | exit signal |
| 2026-11-06T15:10 | Opening range 15m | sell | SOXL | 7.22 | -0.39 | exit signal |
| 2026-11-06T15:10 | Gap and go | buy | TSLA | 7.69 | — | rebalance up |
| 2026-11-06T15:10 | Gap and go | buy | TQQQ | 7.94 | — | rebalance up |
| 2026-11-06T15:10 | Gap and go | buy | PLTR | 7.84 | — | rebalance up |
| 2026-11-06T15:10 | Gap and go | buy | AMD | 8.00 | — | rebalance up |
| 2026-11-06T15:10 | Gap and go | sell | QQQ | 15.86 | -0.03 | exit signal |
| 2026-11-06T15:06 | Agent (ML meta-label) | buy | NVDA | 1.53 | — | entry |
| 2026-11-06T15:06 | Agent (ML meta-label) | buy | IWM | 5.01 | — | entry |
| 2026-11-06T15:06 | Agent (ML meta-label) | sell | SQQQ | 4.81 | 0.04 | selected signal exited |
| 2026-11-06T15:06 | Agent (ML meta-label) | sell | SPY | 2.05 | 0.01 | selected signal exited |
| 2026-11-06T15:06 | MFI reversion · 1h | buy | SOXL | 9.31 | — | entry |
| 2026-11-06T15:06 | MFI reversion · 1h | sell | SPY | 9.31 | 0.03 | target is flat |
| 2026-11-06T15:06 | VWAP reversion · 1h | buy | XRP-USD | 7.78 | — | rebalance up |
| 2026-11-06T15:06 | VWAP reversion · 1h | sell | PLTR | 16.55 | 0.41 | target is flat |
| 2026-11-06T15:06 | Candlestick reversal · 1h | sell | BTC-USD | 5.35 | -0.07 | stop-loss |
| 2026-11-06T15:06 | Gap and go | sell | TECL | 2.12 | -0.03 | exit signal |
| 2026-11-06T15:06 | Gap and go | sell | SOXL | 13.49 | -0.21 | target is flat |
| 2026-11-06T15:00 | Day trade: Stocks in Play ORB | sell | NVDA | 24.45 | 0.01 | target is flat |
| 2026-11-06T15:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 103.72 | — | entry |
| 2026-11-06T15:00 | Agent (ML meta-label) | buy | SQQQ | 4.78 | — | following MFI reversion |
| 2026-11-06T15:00 | Agent (ML meta-label) | sell | NVDA | 2.91 | 0.00 | selected signal exited |
| 2026-11-06T15:00 | Agent (ML meta-label) | sell | IWM | 6.00 | 0.05 | selected signal exited |

## Data problems on the last tick

- GURU: yfinance: $GURU: possibly delisted; no price data found  (5m 2026-11-05 15:25:05.000137+00:00 -> 2026-11-06 15:35:05.000137+00:00); yahoo: cooling down after a rate limit
- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 15:25:05.000137+00:00 -> 2026-11-06 15:35:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 15:25:05.000137+00:00 -> 2026-11-06 15:35:05.000137+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 15:25:05.000137+00:00 -> 2026-11-06 15:35:05.000137+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
