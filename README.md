# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T16:07:05.000142+00:00 · 53562 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.23 (-11.77%)

Closed trades 156, win rate 35.9%, fees £4.86, max drawdown -12.91%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 35.57 | +0.66 |
| TSLA | 17.57 | +0.03 |

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

Today: 16737 decisions in 2550 calls, $0.2225 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T16:07 | 1 / 13 / 17 | cash |  |
| Breezy | 2026-11-09T16:07 | 0 / 28 / 3 | cash |  |
| Boozy | 2026-11-09T16:07 | 4 / 23 / 4 | COIN 73% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 116.90 | 16.90 | 19 | 68.4 | 16.40 | 3.40 | -4.91 | 27 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.30 | 11.30 | 30 | 26.7 | 19.17 | 2.96 | -8.66 | 44 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 110.67 | 10.67 | 0 | — | 11.90 | 4.00 | -5.18 | 1 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.38 | 3.38 | 30 | 43.3 | 3.03 | 0.83 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.84 | 1.84 | 122 | 35.2 | 10.20 | 3.83 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 101.33 | 1.33 | 0 | — | 4.78 | 1.39 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.54 | 0.54 | 7 | 42.9 | -1.52 | 0.13 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.23 | -1.77 | 174 | 27.6 | 3.04 | 0.96 | -9.06 | 240 |
| 11 | Agent (rotation) | meta | 97.79 | -2.21 | 176 | 27.8 | -3.10 | -1.30 | -9.80 | 159 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.05 | -3.08 | -12.05 | 152 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.40 | -3.60 | 0 | — | -2.24 | -0.64 | -6.18 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 93.75 | -6.25 | 0 | — | -4.45 | -1.24 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.74 | -7.26 | 108 | 23.1 | -13.54 | -5.07 | -17.86 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.53 | -7.47 | 0 | — | -4.84 | -1.33 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 90.32 | -9.68 | 375 | 32.5 | -14.25 | -4.52 | -15.99 | 598 |
| 22 | Copy: Insider buying | copy | 89.54 | -10.46 | 40 | 37.5 | -10.95 | -2.48 | -16.06 | 63 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -7.96 | -2.76 | -14.15 | 78 |
| 24 | Agent | meta | 88.23 | -11.77 | 156 | 35.9 | -13.04 | -6.68 | -13.82 | 199 |
| 25 | Hold BTC | benchmark | 87.44 | -12.56 | 1 | 0.0 | -4.82 | -0.50 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.31 | -13.70 | 15 | 20.0 | -10.07 | -1.41 | -17.10 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.59 | -14.41 | 167 | 26.9 | -11.41 | -2.07 | -21.29 | 226 |
| 28 | Agent (aggressive) | meta | 85.03 | -14.97 | 74 | 31.1 | -15.92 | -4.50 | -18.49 | 91 |
| 29 | Stochastic reversion · 1h | reversion | 84.29 | -15.71 | 279 | 48.4 | -21.79 | -3.05 | -27.12 | 387 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 84.18 | -15.82 | 2 | 0.0 | -8.61 | -0.88 | -24.16 | 1 |
| 31 | Donchian 55/20 · 1h | breakout | 83.73 | -16.27 | 71 | 14.1 | -15.63 | -3.25 | -21.87 | 103 |
| 32 | Opening range 15m | breakout | 83.69 | -16.30 | 465 | 30.5 | -18.85 | -5.36 | -20.97 | 735 |
| 33 | Keltner breakout · 1h | breakout | 81.53 | -18.47 | 107 | 23.4 | -22.53 | -4.78 | -25.10 | 178 |
| 34 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.85 | -3.37 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.77 | -19.23 | 205 | 40.0 | -19.32 | -6.47 | -19.64 | 125 |
| 36 | MFI reversion · 1h | reversion | 79.94 | -20.06 | 345 | 33.6 | -16.29 | -2.03 | -21.23 | 162 |
| 37 | Heikin-Ashi · 1h | trend | 79.82 | -20.18 | 394 | 23.1 | -38.41 | -7.20 | -41.80 | 670 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -39.02 | -2.62 | -44.97 | 25 |
| 39 | CCI reversion · 1h | reversion | 79.20 | -20.80 | 308 | 43.8 | -24.38 | -3.71 | -30.29 | 461 |
| 40 | ADX DI cross · 1h | trend | 79.09 | -20.91 | 179 | 18.4 | -24.64 | -4.07 | -28.65 | 272 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 42 | Bollinger breakout · 1h | breakout | 77.15 | -22.85 | 170 | 22.9 | -21.95 | -4.50 | -27.62 | 242 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.33 | -4.06 | -33.04 | 372 |
| 44 | Williams %R · 1h | reversion | 75.52 | -24.48 | 332 | 47.0 | -32.07 | -4.78 | -35.90 | 542 |
| 45 | MACD cross · 1h | trend | 75.52 | -24.48 | 349 | 22.6 | -32.50 | -5.35 | -39.38 | 488 |
| 46 | Z-score reversion · 1h | reversion | 75.10 | -24.90 | 174 | 35.6 | -20.26 | -2.90 | -27.66 | 226 |
| 47 | MACD zero-line · 1h | trend | 74.51 | -25.49 | 157 | 16.6 | -24.81 | -5.11 | -29.17 | 209 |
| 48 | EMA 20/50 cross · 1h | trend | 74.33 | -25.67 | 102 | 10.8 | -22.73 | -3.84 | -31.81 | 127 |
| 49 | Supertrend · 1h | trend | 73.33 | -26.67 | 167 | 13.2 | -31.13 | -5.78 | -34.46 | 234 |
| 50 | RSI momentum · 1h | momentum | 73.08 | -26.91 | 159 | 12.6 | -25.39 | -4.40 | -33.26 | 213 |
| 51 | Triple EMA stack · 1h | trend | 72.56 | -27.44 | 142 | 14.8 | -27.05 | -4.92 | -34.76 | 202 |
| 52 | OBV trend · 1h | momentum | 71.72 | -28.28 | 274 | 18.2 | -28.97 | -5.96 | -34.22 | 277 |
| 53 | ROC + volume · 1h | momentum | 71.46 | -28.55 | 349 | 25.5 | -37.41 | -7.11 | -39.68 | 386 |
| 54 | Daily: Momentum burst | daily | 70.52 | -29.48 | 26 | 11.5 | -38.84 | -5.41 | -39.42 | 31 |
| 55 | Donchian 20/10 · 1h | breakout | 70.19 | -29.81 | 142 | 19.7 | -31.65 | -5.87 | -35.56 | 210 |
| 56 | Agent (ML meta-label) | meta | 68.43 | -31.57 | 1562 | 23.4 | -7.30 | -0.91 | -20.02 | 344 |
| 57 | RSI(14) reversion · 1h | reversion | 68.39 | -31.61 | 157 | 29.3 | -28.52 | -4.25 | -32.51 | 237 |
| 58 | VWAP momentum · 1h | momentum | 67.95 | -32.05 | 801 | 21.6 | -52.00 | -11.12 | -53.60 | 1239 |
| 59 | Max aggression: 1-day momentum | meta | 67.77 | -32.23 | 27 | 25.9 | -32.11 | -1.67 | -57.50 | 42 |
| 60 | Candlestick reversal · 1h | reversion | 65.88 | -34.12 | 431 | 28.3 | -38.32 | -6.89 | -39.93 | 594 |
| 61 | EMA 9/21 cross · 1h | trend | 65.54 | -34.46 | 246 | 9.8 | -39.70 | -7.65 | -41.14 | 327 |
| 62 | Three white soldiers | momentum | 62.74 | -37.26 | 488 | 15.0 | -48.58 | -22.29 | -48.79 | 648 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -45.56 | -98.99 | 5280 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.01 | -26.04 | -80.24 | 1429 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.24 | -46.00 | -93.37 | 2511 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.27 | -32.11 | -89.48 | 1917 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.79 | -39.82 | -90.91 | 2306 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.05 | -31.81 | -90.05 | 2181 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -54.12 | -97.75 | 3473 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -56.99 | -96.31 | 3406 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -32.46 | -93.61 | 2403 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.24 | -34.78 | -82.44 | 1673 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -55.61 | -99.53 | 5999 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.39 | -43.06 | -92.58 | 2598 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.57 | -37.46 | -95.57 | 3393 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.93 | -99.80 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.89 | -43.91 | -91.90 | 2268 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.68 | -24.76 | -76.24 | 1593 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -60.77 | -97.71 | 3493 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -62.55 | -98.85 | 4894 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.56 | -26.92 | -69.38 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -54.75 | -94.68 | 2737 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.83 | -37.23 | -84.98 | 1767 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -74.73 | -99.66 | 6377 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.60 | -32.39 | -89.71 | 2297 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.63 | -20.05 | -78.81 | 1783 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.62 | -36.33 | -90.77 | 2218 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.79 | -52.72 | -96.82 | 3903 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.37 | -57.87 | -89.41 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.10 | -29.08 | -66.26 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.33 | -23.09 | -72.03 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.56 | -19.11 | -79.73 | 1693 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.30 | -50.14 | -97.34 | 4331 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -104.59 | -99.93 | 8279 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T16:00 | CCI reversion · 1h | buy | XRP-USD | 3.66 | — | entry |
| 2026-11-09T16:00 | CCI reversion · 1h | sell | DOGE-USD | 3.66 | 0.05 | exit signal |
| 2026-11-09T16:00 | Williams %R · 1h | buy | UPRO | 9.32 | — | rebalance up |
| 2026-11-09T16:00 | Williams %R · 1h | buy | SPY | 9.50 | — | rebalance up |
| 2026-11-09T16:00 | Williams %R · 1h | buy | MSFT | 9.50 | — | rebalance up |
| 2026-11-09T16:00 | Williams %R · 1h | buy | COIN | 12.24 | — | rebalance up |
| 2026-11-09T16:00 | Williams %R · 1h | sell | XRP-USD | 9.47 | 0.05 | exit signal |
| 2026-11-09T16:00 | Williams %R · 1h | sell | SOL-USD | 9.43 | 0.01 | exit signal |
| 2026-11-09T16:00 | Williams %R · 1h | sell | ETH-USD | 9.45 | 0.03 | exit signal |
| 2026-11-09T16:00 | Williams %R · 1h | sell | BTC-USD | 9.43 | 0.03 | exit signal |
| 2026-11-09T16:00 | Stochastic reversion · 1h | sell | XRP-USD | 21.02 | 0.13 | exit signal |
| 2026-11-09T16:00 | Z-score reversion · 1h | buy | UPRO | 4.24 | — | rebalance up |
| 2026-11-09T16:00 | Z-score reversion · 1h | sell | DOGE-USD | 4.30 | 0.06 | exit signal |
| 2026-11-09T16:00 | Z-score reversion · 1h | sell | BTC-USD | 4.26 | 0.02 | exit signal |
| 2026-11-09T16:00 | RSI(14) reversion · 1h | sell | DOGE-USD | 4.41 | 0.04 | exit signal |
| 2026-11-09T16:00 | RSI(14) reversion · 1h | sell | BTC-USD | 3.86 | 0.02 | exit signal |
| 2026-11-09T16:00 | Heikin-Ashi · 1h | buy | SOL-USD | 10.65 | — | entry signal |
| 2026-11-09T16:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 7.63 | — | rebalance up |
| 2026-11-09T16:00 | Heikin-Ashi · 1h | sell | LABU | 4.73 | 0.31 | rebalance down |
| 2026-11-09T16:00 | Heikin-Ashi · 1h | sell | IWM | 4.04 | 0.07 | rebalance down |
| 2026-11-09T16:00 | Heikin-Ashi · 1h | sell | BTC-USD | 4.12 | 0.03 | rebalance down |
| 2026-11-09T16:00 | Heikin-Ashi · 1h | sell | AMD | 5.39 | 0.58 | rebalance down |
| 2026-11-09T15:55 | Candlestick reversal · 1h | buy | TSLA | 3.69 | — | rebalance up |
| 2026-11-09T15:55 | Candlestick reversal · 1h | buy | PLTR | 3.63 | — | rebalance up |
| 2026-11-09T15:55 | Candlestick reversal · 1h | buy | DOGE-USD | 3.44 | — | rebalance up |
| 2026-11-09T15:55 | Candlestick reversal · 1h | buy | COIN | 3.89 | — | rebalance up |
| 2026-11-09T15:55 | Candlestick reversal · 1h | sell | AMD | 6.61 | 0.67 | take-profit |
| 2026-11-09T15:55 | Three white soldiers | buy | TQQQ | 15.68 | — | entry signal |
| 2026-11-09T15:55 | Three white soldiers | buy | TECL | 15.68 | — | entry signal |
| 2026-11-09T15:39 | Agent (ML meta-label) | buy | GOOGL | 4.02 | — | entry |
| 2026-11-09T15:39 | Agent (ML meta-label) | sell | SPY | 4.02 | 0.02 | selected signal exited |
| 2026-11-09T15:30 | Agent (ML meta-label) | buy | LABU | 1.69 | — | following MFI reversion |
| 2026-11-09T15:30 | Agent (ML meta-label) | buy | AAPL | 4.53 | — | entry |
| 2026-11-09T15:30 | Agent (ML meta-label) | sell | AMD | 5.99 | 0.96 | selected signal exited |
| 2026-11-09T15:30 | CCI reversion · 1h | buy | TNA | 1.54 | — | entry |
| 2026-11-09T15:30 | CCI reversion · 1h | buy | LABU | 4.13 | — | entry |
| 2026-11-09T15:30 | CCI reversion · 1h | sell | AMD | 5.67 | 0.55 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | buy | XRP-USD | 9.42 | — | entry |
| 2026-11-09T15:30 | Williams %R · 1h | buy | UPRO | 9.42 | — | entry signal |
| 2026-11-09T15:30 | Williams %R · 1h | buy | SPY | 9.42 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 16:07:05.000142+00:00 -> 2026-11-09 16:17:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 16:07:05.000142+00:00 -> 2026-11-09 16:17:05.000142+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 16:07:05.000142+00:00 -> 2026-11-09 16:17:05.000142+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
