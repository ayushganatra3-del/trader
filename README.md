# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-18T13:55:05.000160+00:00 · 27256 ticks

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

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 10563 decisions in 2115 calls, $0.1476 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-18T13:55 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-18T13:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-18T13:55 | 1 / 4 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 2.34 | +2.45% | 9 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| ROC + volume | SQQQ | 1.83 | +2.20% | 12 |
| VWAP reversion | ETHU | 1.80 | +2.34% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.29 | -3.28 | -13.79 | 135 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.92 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 0.65 | 0.28 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.17 | -2.37 | -20.62 | 67 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -5.16 | -2.65 | -6.49 | 290 |
| 17 | Hold BTC | benchmark | 96.62 | -3.38 | 0 | — | 27.11 | 3.24 | -8.68 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -19.52 | -5.88 | -19.70 | 140 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.12 | -0.02 | -5.23 | 30 |
| 23 | ADX DI cross · 1h | trend | 94.58 | -5.42 | 82 | 19.5 | 1.18 | 0.35 | -14.56 | 253 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 4.14 | 0.92 | -9.46 | 98 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.37 | 2.38 | -6.56 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -9.89 | -1.53 | -22.55 | 270 |
| 28 | EMA 20/50 cross · 1h | trend | 92.56 | -7.44 | 55 | 14.5 | -18.32 | -3.16 | -21.23 | 126 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.82 | -2.01 | -8.64 | 115 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.55 | -6.44 | -13.47 | 236 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.57 | -0.07 | -14.55 | 114 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.89 | -9.11 | 77 | 16.9 | -17.00 | -2.97 | -27.38 | 216 |
| 34 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 6.58 | 1.03 | -14.21 | 268 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.38 | -17.98 | 112 |
| 37 | Triple EMA stack · 1h | trend | 90.05 | -9.95 | 81 | 16.0 | -13.19 | -1.41 | -33.23 | 229 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -7.88 | -0.95 | -27.05 | 202 |
| 41 | Supertrend · 1h | trend | 89.04 | -10.96 | 84 | 11.9 | -13.60 | -2.14 | -28.00 | 210 |
| 42 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -24.39 | -7.46 | -25.57 | 231 |
| 43 | MACD cross · 1h | trend | 87.86 | -12.14 | 178 | 21.9 | -16.04 | -2.07 | -30.21 | 459 |
| 44 | OBV trend · 1h | momentum | 87.64 | -12.36 | 170 | 18.2 | -10.55 | -1.00 | -33.81 | 316 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.55 | -13.45 | 143 | 44.1 | -21.11 | -3.87 | -22.11 | 366 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.46 | -14.54 | 82 | 15.9 | -22.40 | -4.38 | -23.90 | 216 |
| 49 | Donchian 20/10 · 1h | breakout | 84.68 | -15.32 | 79 | 17.7 | 1.84 | 0.43 | -21.63 | 213 |
| 50 | MFI reversion · 1h | reversion | 84.01 | -15.99 | 205 | 30.2 | -21.68 | -3.59 | -22.26 | 142 |
| 51 | Three white soldiers | momentum | 83.56 | -16.44 | 216 | 18.5 | -47.72 | -20.23 | -47.74 | 608 |
| 52 | Z-score reversion · 1h | reversion | 83.18 | -16.82 | 86 | 31.4 | -16.23 | -2.84 | -20.59 | 185 |
| 53 | ROC + volume · 1h | momentum | 82.71 | -17.29 | 193 | 21.2 | -12.82 | -1.68 | -27.12 | 396 |
| 54 | Agent (ML meta-label) | meta | 82.34 | -17.66 | 652 | 18.1 | -12.49 | -1.89 | -20.39 | 376 |
| 55 | EMA 9/21 cross · 1h | trend | 81.11 | -18.89 | 130 | 11.5 | -6.72 | -0.56 | -30.25 | 315 |
| 56 | Heikin-Ashi · 1h | trend | 80.95 | -19.05 | 206 | 22.3 | -32.42 | -5.33 | -42.19 | 678 |
| 57 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.33 | -5.81 | -36.60 | 531 |
| 58 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.68 | -2.62 | -21.70 | 162 |
| 59 | Bollinger reversion · 1h | reversion | 79.88 | -20.12 | 146 | 31.5 | -30.68 | -6.39 | -32.71 | 348 |
| 60 | VWAP momentum · 1h | momentum | 79.78 | -20.22 | 408 | 20.1 | -38.09 | -5.82 | -46.77 | 1257 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.47 | -2.68 | -26.95 | 426 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.87 | -6.52 | -36.51 | 537 |
| 63 | Volume breakout | breakout | 62.76 | -37.24 | 335 | 12.8 | -63.12 | -18.33 | -63.47 | 879 |
| 64 | ROC + volume | momentum | 62.11 | -37.89 | 560 | 21.6 | -75.85 | -17.83 | -77.75 | 1724 |
| 65 | Squeeze breakout | breakout | 61.75 | -38.25 | 444 | 14.4 | -62.96 | -18.04 | -64.76 | 1215 |
| 66 | RSI(14) reversion | reversion | 60.33 | -39.67 | 671 | 25.5 | -74.07 | -16.52 | -74.12 | 1627 |
| 67 | Donchian 55/20 | breakout | 59.13 | -40.87 | 455 | 17.1 | -69.17 | -14.71 | -72.67 | 1281 |
| 68 | EMA 20/50 cross | trend | 56.85 | -43.15 | 480 | 18.3 | -77.14 | -15.36 | -80.07 | 1442 |
| 69 | VWAP reversion | reversion | 54.35 | -45.65 | 703 | 23.8 | -73.05 | -15.50 | -73.20 | 1515 |
| 70 | Keltner breakout | breakout | 52.35 | -47.65 | 633 | 15.5 | -83.28 | -27.57 | -83.28 | 1826 |
| 71 | AI bee: Boozy | ai | 52.17 | -47.83 | 333 | 6.0 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -30.51 | -98.66 | 5344 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -31.19 | -93.61 | 2599 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.63 | -20.64 | -87.70 | 1912 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.47 | -25.10 | -90.87 | 2363 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.23 | -26.73 | -91.23 | 2302 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -33.23 | -97.47 | 3526 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.79 | -37.67 | -96.79 | 3623 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -28.17 | -94.55 | 2595 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.15 | -23.73 | -82.50 | 1733 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -37.55 | -99.39 | 5818 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.36 | -26.29 | -91.55 | 2643 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.15 | -32.47 | -96.15 | 3528 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.28 | -99.74 | 6239 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.73 | -29.73 | -91.74 | 2366 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -39.46 | -97.50 | 3659 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.58 | -98.49 | 4771 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.74 | -34.13 | -93.74 | 2810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.60 | -99.53 | 6250 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.62 | -22.26 | -86.63 | 2166 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.24 | -27.63 | -88.28 | 2164 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -33.20 | -95.89 | 3817 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.31 | -34.36 | -89.32 | 2102 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.85 | -34.74 | -95.85 | 4160 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.66 | -99.89 | 8311 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-18T13:52 | RSI(14) reversion | buy | XRP-USD | 6.02 | — | rebalance up |
| 2026-10-18T13:52 | RSI(14) reversion | sell | SOL-USD | 3.03 | -0.01 | rebalance down |
| 2026-10-18T13:52 | RSI(14) reversion | sell | ETH-USD | 3.01 | -0.02 | rebalance down |
| 2026-10-18T13:50 | RSI(14) reversion | buy | XRP-USD | 6.08 | — | entry signal |
| 2026-10-18T13:50 | RSI(14) reversion | buy | DOGE-USD | 12.10 | — | entry signal |
| 2026-10-18T13:50 | RSI(14) reversion | buy | BTC-USD | 12.10 | — | entry signal |
| 2026-10-18T13:40 | VWAP reversion | buy | XRP-USD | 10.89 | — | entry signal |
| 2026-10-18T13:40 | VWAP reversion | buy | SOL-USD | 10.89 | — | entry signal |
| 2026-10-18T13:40 | VWAP reversion | buy | ETH-USD | 10.89 | — | entry signal |
| 2026-10-18T13:40 | VWAP reversion | buy | DOGE-USD | 10.89 | — | entry signal |
| 2026-10-18T13:40 | VWAP reversion | buy | BTC-USD | 10.89 | — | entry signal |
| 2026-10-18T13:40 | RSI(14) reversion | buy | SOL-USD | 15.14 | — | entry signal |
| 2026-10-18T13:40 | RSI(14) reversion | buy | ETH-USD | 15.14 | — | entry signal |
| 2026-10-18T13:35 | Donchian 20/10 · 1h | sell | BTC-USD | 20.95 | -0.29 | stop-loss |
| 2026-10-18T13:35 | OBV trend · 1h | sell | BTC-USD | 21.66 | -0.34 | stop-loss |
| 2026-10-18T13:35 | VWAP momentum · 1h | sell | SOL-USD | 18.51 | -0.35 | stop-loss |
| 2026-10-18T13:35 | VWAP momentum · 1h | sell | ETH-USD | 19.91 | -0.39 | stop-loss |
| 2026-10-18T13:35 | VWAP momentum · 1h | sell | DOGE-USD | 19.85 | -0.46 | stop-loss |
| 2026-10-18T13:35 | MACD zero-line · 1h | sell | BTC-USD | 21.15 | -0.29 | stop-loss |
| 2026-10-18T13:35 | MACD cross · 1h | buy | SOL-USD | 6.44 | — | entry |
| 2026-10-18T13:35 | MACD cross · 1h | sell | DOGE-USD | 6.44 | -0.17 | stop-loss |
| 2026-10-18T13:35 | Triple EMA stack · 1h | sell | BTC-USD | 22.26 | -0.34 | stop-loss |
| 2026-10-18T13:35 | EMA 20/50 cross · 1h | sell | BTC-USD | 22.87 | -0.35 | stop-loss |
| 2026-10-18T13:35 | EMA 9/21 cross · 1h | sell | ETH-USD | 20.01 | -0.41 | stop-loss |
| 2026-10-18T13:30 | Squeeze breakout · 1h | sell | BTC-USD | 23.13 | -0.30 | stop-loss |
| 2026-10-18T13:30 | Bollinger breakout · 1h | sell | BTC-USD | 22.46 | -0.24 | stop-loss |
| 2026-10-18T13:30 | RSI momentum · 1h | sell | BTC-USD | 22.50 | -0.29 | stop-loss |
| 2026-10-18T13:30 | ROC + volume · 1h | sell | BTC-USD | 20.48 | -0.27 | stop-loss |
| 2026-10-18T13:30 | VWAP momentum · 1h | buy | SOL-USD | 5.29 | — | rebalance up |
| 2026-10-18T13:30 | VWAP momentum · 1h | buy | ETH-USD | 6.74 | — | rebalance up |
| 2026-10-18T13:30 | VWAP momentum · 1h | buy | DOGE-USD | 4.10 | — | rebalance up |
| 2026-10-18T13:30 | VWAP momentum · 1h | sell | BTC-USD | 13.39 | -0.18 | stop-loss |
| 2026-10-18T13:25 | EMA 20/50 cross | sell | SOL-USD | 11.34 | -0.15 | stop-loss |
| 2026-10-18T13:15 | EMA 20/50 cross | sell | BTC-USD | 11.40 | -0.08 | exit signal |
| 2026-10-18T13:00 | VWAP momentum · 1h | buy | DOGE-USD | 13.38 | — | rebalance up |
| 2026-10-18T13:00 | VWAP momentum · 1h | sell | XRP-USD | 16.13 | -0.12 | exit signal |
| 2026-10-18T13:00 | Heikin-Ashi · 1h | sell | BTC-USD | 20.13 | -0.15 | exit signal |
| 2026-10-18T12:35 | Three white soldiers | sell | DOGE-USD | 20.79 | -0.13 | exit signal |
| 2026-10-18T12:35 | EMA 20/50 cross | sell | ETH-USD | 14.21 | -0.12 | exit signal |
| 2026-10-18T12:20 | AI bee: Boozy | sell | ETH-USD | 15.11 | -0.11 | Jev: sell (sell p=0.57) after 16 min |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-20 13:55:05.000160+00:00 -> 2026-10-18 14:05:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
