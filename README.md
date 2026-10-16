# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T23:25:05.000153+00:00 · 25304 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 22.89 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 41294 decisions in 3463 calls, $0.5129 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T23:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-16T23:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T23:25 | 0 / 4 / 1 | COIN 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.15 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.93 | -0.07 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.39 | 60 | 38.3 | -11.58 | -3.36 | -13.80 | 134 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.10 | 1.15 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 9.03 | 1.21 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.74 | -1.26 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.61 | -1.39 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.33 | -2.12 | -20.62 | 75 |
| 16 | Agent (rotation) | meta | 97.13 | -2.88 | 108 | 33.3 | -8.30 | -2.98 | -12.20 | 292 |
| 17 | Hold BTC | benchmark | 96.91 | -3.09 | 0 | — | 29.16 | 3.42 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.78 | 87 | 24.1 | -21.00 | -6.25 | -22.15 | 150 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.56 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.99 | -1.61 | -13.33 | 259 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.17 | 2.34 | -6.73 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.25 | -6.75 | 96 | 21.9 | 3.29 | 0.61 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -3.90 | -0.33 | -22.92 | 128 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -6.79 | -2.37 | -10.02 | 123 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -11.01 | -6.13 | -12.21 | 245 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.39 | -0.04 | -14.55 | 116 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.25 | 0.36 | -26.55 | 218 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.16 | 0.98 | -14.21 | 271 |
| 35 | Daily: Bullish score | daily | 90.66 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.24 | -0.55 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.40 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.47 | -10.53 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -3.70 | -0.22 | -30.08 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | MACD cross · 1h | trend | 89.14 | -10.87 | 171 | 22.8 | -14.50 | -1.92 | -27.78 | 453 |
| 42 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.86 | -1.09 | -27.05 | 208 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.14 | -7.57 | -26.03 | 239 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -9.11 | -0.75 | -34.23 | 321 |
| 45 | Stochastic reversion · 1h | reversion | 86.97 | -13.03 | 136 | 43.4 | -20.54 | -3.74 | -22.11 | 367 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.22 | -4.51 | -21.41 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -22.49 | -4.42 | -23.33 | 218 |
| 48 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.33 | 0.37 | -21.63 | 217 |
| 50 | Three white soldiers | momentum | 84.80 | -15.20 | 208 | 19.2 | -47.46 | -19.39 | -48.49 | 603 |
| 51 | MFI reversion · 1h ⏸ | reversion | 84.04 | -15.96 | 204 | 30.4 | -20.43 | -3.48 | -21.05 | 140 |
| 52 | Heikin-Ashi · 1h | trend | 83.83 | -16.17 | 189 | 24.3 | -31.55 | -5.21 | -40.65 | 674 |
| 53 | VWAP momentum · 1h | momentum | 83.81 | -16.19 | 387 | 21.2 | -36.02 | -5.48 | -43.85 | 1252 |
| 54 | Z-score reversion · 1h | reversion | 83.45 | -16.55 | 86 | 31.4 | -15.37 | -2.67 | -19.86 | 182 |
| 55 | Agent (ML meta-label) | meta | 83.15 | -16.85 | 610 | 19.2 | -6.44 | -0.79 | -17.39 | 381 |
| 56 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -13.39 | -1.76 | -27.23 | 405 |
| 57 | EMA 9/21 cross · 1h | trend | 82.25 | -17.75 | 127 | 11.8 | -6.69 | -0.59 | -29.70 | 318 |
| 58 | Bollinger reversion · 1h | reversion | 80.18 | -19.82 | 138 | 31.2 | -30.19 | -6.26 | -32.42 | 345 |
| 59 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.36 | -5.61 | -35.92 | 528 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.98 | 74 | 20.3 | -14.65 | -2.61 | -21.70 | 164 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.50 | -2.53 | -25.42 | 431 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.47 | -6.38 | -36.41 | 532 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.25 | -18.23 | -63.25 | 879 |
| 64 | ROC + volume | momentum | 63.23 | -36.77 | 550 | 22.0 | -75.82 | -17.71 | -77.39 | 1719 |
| 65 | Squeeze breakout | breakout | 63.04 | -36.96 | 429 | 14.7 | -63.01 | -18.03 | -64.08 | 1218 |
| 66 | RSI(14) reversion ⏸ | reversion | 62.42 | -37.58 | 646 | 25.9 | -74.64 | -16.69 | -74.71 | 1633 |
| 67 | Donchian 55/20 | breakout | 61.43 | -38.57 | 435 | 17.9 | -69.11 | -14.58 | -71.81 | 1285 |
| 68 | EMA 20/50 cross | trend | 59.86 | -40.14 | 455 | 19.3 | -77.06 | -15.23 | -79.04 | 1452 |
| 69 | VWAP reversion | reversion | 55.78 | -44.22 | 676 | 23.7 | -73.38 | -15.56 | -73.57 | 1503 |
| 70 | AI bee: Boozy | ai | 55.30 | -44.70 | 303 | 6.6 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.59 | -45.41 | 608 | 16.1 | -83.49 | -27.05 | -83.58 | 1841 |
| 72 | Ichimoku | trend | 52.02 | -47.98 | 553 | 11.8 | -81.92 | -23.06 | -82.05 | 1731 |
| 73 | Supertrend ⏸ | trend | 50.88 | -49.12 | 638 | 19.6 | -86.47 | -20.48 | -87.08 | 1917 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -29.77 | -98.61 | 5313 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.49 | -30.42 | -93.51 | 2604 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.43 | -24.80 | -90.49 | 2368 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.80 | -27.68 | -91.81 | 2344 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -32.77 | -97.46 | 3534 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.68 | -36.62 | -96.68 | 3610 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -26.69 | -94.46 | 2627 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -36.82 | -99.41 | 5837 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.37 | -25.98 | -91.39 | 2650 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.36 | -32.49 | -96.37 | 3571 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.66 | -99.73 | 6229 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -29.70 | -91.79 | 2372 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -38.71 | -97.46 | 3657 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -36.91 | -98.51 | 4773 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.68 | -33.30 | -93.68 | 2810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.85 | -99.54 | 6256 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.62 | -22.36 | -86.64 | 2160 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.92 | -27.29 | -87.97 | 2164 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.99 | -32.98 | -96.03 | 3825 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -33.90 | -89.30 | 2113 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.81 | -34.03 | -95.84 | 4154 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.06 | -99.89 | 8302 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T23:25 | Keltner breakout | sell | DOGE-USD | 13.55 | -0.13 | stop-loss |
| 2026-10-16T23:25 | ROC + volume | sell | DOGE-USD | 15.73 | -0.12 | exit signal |
| 2026-10-16T23:10 | VWAP reversion | buy | DOGE-USD | 13.96 | — | entry |
| 2026-10-16T23:10 | ROC + volume | sell | SOL-USD | 15.85 | 0.01 | exit signal |
| 2026-10-16T23:05 | VWAP reversion | sell | DOGE-USD | 11.20 | 0.06 | exit signal |
| 2026-10-16T23:05 | Keltner breakout | buy | DOGE-USD | 13.68 | — | entry signal |
| 2026-10-16T23:05 | Donchian 55/20 | buy | XRP-USD | 15.39 | — | entry signal |
| 2026-10-16T23:02 | AI bee: Boozy | sell | ETH-USD | 18.24 | -0.11 | Jev: buy |
| 2026-10-16T23:00 | VWAP reversion · 1h | sell | BTC-USD | 9.97 | -0.02 | exit signal |
| 2026-10-16T23:00 | VWAP momentum · 1h | buy | BTC-USD | 20.97 | — | entry signal |
| 2026-10-16T23:00 | Heikin-Ashi · 1h | buy | SOL-USD | 20.98 | — | entry signal |
| 2026-10-16T22:56 | ROC + volume | buy | DOGE-USD | 15.85 | — | entry signal |
| 2026-10-16T22:50 | EMA 20/50 cross | buy | ETH-USD | 3.05 | — | entry |
| 2026-10-16T22:50 | EMA 20/50 cross | sell | DOGE-USD | 2.99 | -0.01 | rebalance down |
| 2026-10-16T22:47 | AI bee: Boozy | buy | ETH-USD | 18.36 | — | Jev: buy (buy p=0.68) |
| 2026-10-16T22:20 | Squeeze breakout | buy | ETH-USD | 15.77 | — | entry signal |
| 2026-10-16T22:19 | AI bee: Boozy | sell | ETH-USD | 18.36 | -0.09 | Jev: buy |
| 2026-10-16T22:10 | Donchian 55/20 | buy | DOGE-USD | 15.38 | — | entry signal |
| 2026-10-16T22:04 | AI bee: Boozy | buy | ETH-USD | 18.45 | — | Jev: buy (buy p=0.68) |
| 2026-10-16T21:57 | Squeeze breakout | sell | DOGE-USD | 15.66 | -0.15 | exit signal |
| 2026-10-16T21:45 | EMA 20/50 cross | buy | XRP-USD | 14.95 | — | entry signal |
| 2026-10-16T21:35 | Squeeze breakout | buy | DOGE-USD | 15.81 | — | entry signal |
| 2026-10-16T21:34 | AI bee: Boozy | sell | ETH-USD | 18.45 | -0.10 | Jev: buy |
| 2026-10-16T21:30 | EMA 20/50 cross | buy | DOGE-USD | 14.97 | — | entry signal |
| 2026-10-16T21:25 | VWAP reversion | buy | XRP-USD | 2.79 | — | rebalance up |
| 2026-10-16T21:25 | VWAP reversion | buy | ETH-USD | 2.81 | — | rebalance up |
| 2026-10-16T21:25 | VWAP reversion | sell | BTC-USD | 11.11 | -0.03 | exit signal |
| 2026-10-16T21:20 | EMA 20/50 cross | buy | SOL-USD | 14.98 | — | entry signal |
| 2026-10-16T21:18 | AI bee: Boozy | buy | ETH-USD | 18.54 | — | Jev: buy (buy p=0.68) |
| 2026-10-16T21:05 | Agent (ML meta-label) | buy | ETH-USD | 6.11 | — | entry |
| 2026-10-16T21:05 | Agent (ML meta-label) | buy | BTC-USD | 9.24 | — | entry |
| 2026-10-16T20:48 | AI bee: Boozy | sell | SOL-USD | 18.54 | -0.12 | Jev: sell |
| 2026-10-16T20:32 | AI bee: Boozy | buy | SOL-USD | 18.67 | — | Jev: buy (buy p=0.67) |
| 2026-10-16T20:26 | Agent (ML meta-label) | sell | BTC-USD | 8.27 | -0.06 | selected signal exited |
| 2026-10-16T20:25 | EMA 20/50 cross | buy | BTC-USD | 14.99 | — | entry signal |
| 2026-10-16T20:15 | Agent (ML meta-label) | sell | ETH-USD | 7.08 | -0.05 | selected signal exited |
| 2026-10-16T20:05 | Agent (ML meta-label) | buy | ETH-USD | 7.13 | — | entry |
| 2026-10-16T20:05 | Agent (ML meta-label) | buy | BTC-USD | 8.33 | — | entry |
| 2026-10-16T20:05 | ROC + volume | buy | SOL-USD | 15.83 | — | entry signal |
| 2026-10-16T20:00 | Z-score reversion · 1h | buy | XRP-USD | 12.31 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 23:25:05.000153+00:00 -> 2026-10-16 23:35:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
