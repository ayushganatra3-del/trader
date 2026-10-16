# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T14:56:05.000139+00:00 · 24894 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.97 (-8.03%)

Closed trades 76, win rate 39.5%, fees £2.68, max drawdown -8.62%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.36 | -0.02 |
| LABU | 17.75 | -0.82 |
| SQQQ | 18.33 | -0.05 |

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

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 16715 decisions in 2233 calls, $0.2188 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T14:56 | 2 / 14 / 14 | cash |  |
| Breezy | 2026-10-16T14:56 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-16T14:56 | 5 / 23 / 2 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.29 | 4.29 | 0 | — | 5.63 | 2.65 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -1.84 | -0.52 | -9.61 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.81 | 2.81 | 9 | 66.7 | 4.47 | 1.98 | -3.27 | 19 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.60 | 2.60 | 1 | 100.0 | 4.02 | 1.04 | -7.93 | 9 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 14 | 35.7 | 3.44 | 1.10 | -7.55 | 44 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.19 | 0.19 | 0 | — | 4.52 | 1.73 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | VWAP reversion · 1h | reversion | 99.84 | -0.16 | 59 | 39.0 | -11.47 | -3.28 | -13.79 | 124 |
| 10 | Hold SPY | benchmark | 99.41 | -0.59 | 0 | — | -0.54 | -0.27 | -3.23 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 12 | Copy: Insider buying | copy | 98.55 | -1.45 | 20 | 45.0 | -11.82 | -1.98 | -20.62 | 75 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 97.71 | -2.29 | 51 | 31.4 | 0.96 | 0.57 | -2.96 | 69 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.67 | -2.33 | 0 | — | -1.12 | -0.43 | -4.45 | 1 |
| 15 | Donchian 55/20 · 1h | breakout | 97.65 | -2.35 | 36 | 16.7 | 7.85 | 1.07 | -22.12 | 109 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.07 | -2.93 | 0 | — | -5.85 | -3.22 | -6.38 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.04 | -2.96 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Hold BTC | benchmark | 97.01 | -2.99 | 0 | — | 29.54 | 3.38 | -8.68 | 1 |
| 19 | Trend pullback · 1h | trend | 96.44 | -3.56 | 86 | 24.4 | -21.41 | -6.25 | -22.23 | 152 |
| 20 | Three white soldiers · 1h | momentum | 95.73 | -4.27 | 11 | 0.0 | 0.07 | 0.08 | -5.01 | 31 |
| 21 | Agent (rotation) | meta | 95.67 | -4.33 | 107 | 32.7 | -11.40 | -4.34 | -12.13 | 300 |
| 22 | Daily: Momentum burst | daily | 94.93 | -5.07 | 5 | 20.0 | -5.00 | -0.60 | -17.97 | 42 |
| 23 | ADX DI cross · 1h | trend | 94.87 | -5.13 | 78 | 20.5 | -8.62 | -1.51 | -13.33 | 258 |
| 24 | Max aggression: 5-day momentum | meta | 94.35 | -5.64 | 8 | 37.5 | -20.66 | -1.84 | -34.64 | 26 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 3.80 | 0.85 | -9.46 | 100 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.27 | -6.78 | 197 |
| 27 | Parabolic SAR · 1h | trend | 93.22 | -6.78 | 93 | 22.6 | 3.42 | 0.61 | -22.21 | 277 |
| 28 | EMA 20/50 cross · 1h | trend | 92.78 | -7.22 | 52 | 15.4 | -4.62 | -0.43 | -22.92 | 130 |
| 29 | Daily: Bullish score | daily | 92.10 | -7.90 | 7 | 0.0 | -4.46 | -0.38 | -12.76 | 13 |
| 30 | Agent | meta | 91.97 | -8.03 | 76 | 39.5 | -10.29 | -5.41 | -11.26 | 243 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 91.94 | -8.06 | 0 | — | 3.10 | 0.62 | -13.89 | 1 |
| 32 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.80 | -0.11 | -14.55 | 118 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 91.54 | -8.46 | 0 | — | -17.76 | -3.39 | -19.22 | 1 |
| 34 | RSI momentum · 1h | momentum | 91.42 | -8.58 | 73 | 17.8 | 0.53 | 0.27 | -26.55 | 221 |
| 35 | Bollinger breakout · 1h | breakout | 91.10 | -8.90 | 82 | 29.3 | 5.85 | 0.92 | -14.21 | 274 |
| 36 | MACD cross · 1h | trend | 91.06 | -8.94 | 160 | 23.1 | -12.84 | -1.68 | -25.76 | 458 |
| 37 | Opening range 30m | breakout | 90.94 | -9.06 | 189 | 30.2 | -12.35 | -3.37 | -17.60 | 571 |
| 38 | Supertrend · 1h | trend | 90.47 | -9.53 | 75 | 13.3 | -1.93 | -0.01 | -28.55 | 213 |
| 39 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 40 | Agent (aggressive) | meta | 90.06 | -9.94 | 38 | 31.6 | -8.47 | -3.12 | -9.71 | 125 |
| 41 | Triple EMA stack · 1h | trend | 89.96 | -10.04 | 78 | 16.7 | -8.78 | -0.70 | -33.23 | 235 |
| 42 | Connors RSI(2) · 1h | reversion | 89.83 | -10.17 | 143 | 40.6 | -23.22 | -6.86 | -25.02 | 241 |
| 43 | Stochastic reversion · 1h | reversion | 89.35 | -10.65 | 130 | 45.4 | -18.03 | -3.36 | -19.84 | 349 |
| 44 | Max aggression: 1-day momentum | meta | 89.33 | -10.67 | 14 | 35.7 | -6.97 | 0.00 | -37.31 | 43 |
| 45 | Keltner breakout · 1h | breakout | 88.07 | -11.93 | 52 | 23.1 | -10.35 | -1.29 | -27.05 | 210 |
| 46 | OBV trend · 1h | momentum | 87.61 | -12.39 | 167 | 18.6 | -9.45 | -0.78 | -33.95 | 321 |
| 47 | MFI reversion · 1h | reversion | 86.96 | -13.04 | 196 | 31.1 | -18.48 | -3.19 | -19.89 | 140 |
| 48 | Opening range 15m | breakout | 86.84 | -13.16 | 237 | 25.7 | -17.11 | -4.38 | -21.40 | 709 |
| 49 | Z-score reversion · 1h | reversion | 86.54 | -13.46 | 74 | 36.5 | -11.81 | -2.14 | -17.27 | 178 |
| 50 | MACD zero-line · 1h | trend | 86.48 | -13.52 | 78 | 16.7 | -22.87 | -4.41 | -23.11 | 224 |
| 51 | Agent (ML meta-label) | meta | 85.68 | -14.32 | 570 | 18.8 | -3.98 | -0.45 | -16.49 | 380 |
| 52 | Donchian 20/10 · 1h | breakout | 85.56 | -14.44 | 72 | 19.4 | 1.68 | 0.40 | -20.98 | 219 |
| 53 | Three white soldiers | momentum | 84.79 | -15.21 | 206 | 18.9 | -47.86 | -19.40 | -48.52 | 609 |
| 54 | Heikin-Ashi · 1h | trend | 84.13 | -15.87 | 185 | 24.9 | -31.01 | -5.01 | -39.61 | 673 |
| 55 | VWAP momentum · 1h | momentum | 84.10 | -15.90 | 379 | 21.4 | -36.33 | -5.43 | -43.19 | 1256 |
| 56 | ROC + volume · 1h | momentum | 83.80 | -16.20 | 186 | 22.0 | -11.23 | -1.45 | -25.33 | 403 |
| 57 | EMA 9/21 cross · 1h | trend | 83.75 | -16.25 | 121 | 12.4 | -5.71 | -0.46 | -28.20 | 321 |
| 58 | Bollinger reversion · 1h | reversion | 82.80 | -17.20 | 133 | 32.3 | -27.91 | -5.97 | -31.36 | 337 |
| 59 | Williams %R · 1h | reversion | 82.63 | -17.37 | 172 | 44.2 | -32.17 | -5.25 | -34.85 | 524 |
| 60 | RSI(14) reversion · 1h | reversion | 82.26 | -17.74 | 63 | 23.8 | -11.48 | -2.06 | -18.95 | 160 |
| 61 | CCI reversion · 1h | reversion | 81.83 | -18.18 | 145 | 42.8 | -16.28 | -2.10 | -23.38 | 427 |
| 62 | Candlestick reversal · 1h | reversion | 78.82 | -21.18 | 190 | 25.8 | -32.33 | -5.93 | -33.21 | 515 |
| 63 | RSI(14) reversion | reversion | 65.35 | -34.65 | 586 | 28.3 | -73.69 | -16.31 | -74.13 | 1575 |
| 64 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.47 | -17.73 | -63.47 | 889 |
| 65 | ROC + volume | momentum | 63.46 | -36.54 | 543 | 21.9 | -75.79 | -17.09 | -77.36 | 1729 |
| 66 | Squeeze breakout | breakout | 63.26 | -36.74 | 427 | 14.8 | -63.00 | -17.39 | -63.90 | 1218 |
| 67 | Donchian 55/20 | breakout | 60.90 | -39.10 | 433 | 17.8 | -69.51 | -14.26 | -71.81 | 1286 |
| 68 | EMA 20/50 cross | trend | 59.53 | -40.47 | 449 | 19.4 | -77.51 | -14.94 | -79.02 | 1454 |
| 69 | VWAP reversion | reversion | 57.55 | -42.45 | 596 | 24.2 | -72.50 | -14.75 | -72.58 | 1434 |
| 70 | AI bee: Boozy | ai | 57.00 | -42.99 | 289 | 5.5 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.32 | -45.68 | 606 | 16.0 | -83.75 | -25.87 | -83.75 | 1846 |
| 72 | Supertrend | trend | 52.20 | -47.80 | 627 | 19.9 | -86.42 | -19.81 | -86.73 | 1914 |
| 73 | Ichimoku | trend | 51.57 | -48.43 | 549 | 11.7 | -82.21 | -22.26 | -82.21 | 1735 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -28.46 | -98.66 | 5325 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.55 | -28.63 | -93.55 | 2600 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.61 | -23.81 | -90.61 | 2372 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.83 | -26.04 | -91.83 | 2343 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.48 | -30.68 | -97.48 | 3531 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -33.96 | -96.73 | 3616 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.54 | -25.27 | -94.54 | 2631 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -33.74 | -99.39 | 5740 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.46 | -24.83 | -91.46 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.34 | -30.11 | -96.34 | 3568 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -37.92 | -99.73 | 6174 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -28.03 | -91.79 | 2373 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -35.36 | -97.46 | 3655 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -34.05 | -98.46 | 4699 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.76 | -31.20 | -93.76 | 2811 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -36.48 | -99.53 | 6189 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.04 | -21.36 | -86.05 | 2114 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.70 | -25.90 | -87.71 | 2124 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -30.49 | -95.91 | 3772 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -31.82 | -89.30 | 2105 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.75 | -31.89 | -95.76 | 4091 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.52 | -99.89 | 8245 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T14:56 | Supertrend | buy | NVDA | 2.60 | — | rebalance up |
| 2026-10-16T14:56 | Supertrend | sell | ETH-USD | 2.60 | -0.04 | rebalance down |
| 2026-10-16T14:55 | AI bee: Boozy | sell | ETHU | 41.20 | -0.56 | Jev: sell (sell p=0.51) after 36 min |
| 2026-10-16T14:55 | RSI(14) reversion | buy | META | 3.85 | — | rebalance up |
| 2026-10-16T14:55 | RSI(14) reversion | sell | MSTR | 8.12 | -0.17 | stop-loss |
| 2026-10-16T14:55 | Three white soldiers | sell | PLTR | 21.03 | -0.22 | exit signal |
| 2026-10-16T14:55 | Squeeze breakout | sell | XRP-USD | 15.68 | -0.26 | stop-loss |
| 2026-10-16T14:55 | Squeeze breakout | sell | ETHU | 15.72 | -0.22 | stop-loss |
| 2026-10-16T14:55 | Keltner breakout | sell | ETHU | 13.51 | -0.19 | stop-loss |
| 2026-10-16T14:55 | Opening range 30m | buy | SOXL | 9.12 | — | rebalance up |
| 2026-10-16T14:55 | Opening range 30m | buy | ETHU | 4.57 | — | rebalance up |
| 2026-10-16T14:55 | Opening range 30m | sell | COIN | 22.63 | -0.37 | stop-loss |
| 2026-10-16T14:55 | ROC + volume | sell | DOGE-USD | 15.76 | -0.19 | stop-loss |
| 2026-10-16T14:55 | Ichimoku | buy | SQQQ | 4.18 | — | rebalance up |
| 2026-10-16T14:55 | Ichimoku | buy | NVDA | 4.29 | — | rebalance up |
| 2026-10-16T14:55 | Ichimoku | sell | ETHU | 8.55 | -0.11 | stop-loss |
| 2026-10-16T14:55 | Ichimoku | sell | ETH-USD | 8.56 | -0.10 | exit signal |
| 2026-10-16T14:55 | Ichimoku | sell | COIN | 8.55 | -0.10 | exit signal |
| 2026-10-16T14:55 | Ichimoku | sell | BITX | 8.57 | -0.08 | stop-loss |
| 2026-10-16T14:55 | Supertrend | buy | NVDA | 2.61 | — | rebalance up |
| 2026-10-16T14:55 | Supertrend | sell | BTC-USD | 2.61 | -0.03 | rebalance down |
| 2026-10-16T14:55 | EMA 20/50 cross | buy | SQQQ | 6.23 | — | rebalance up |
| 2026-10-16T14:55 | EMA 20/50 cross | buy | NVDA | 6.42 | — | rebalance up |
| 2026-10-16T14:55 | EMA 20/50 cross | buy | AMZN | 6.38 | — | rebalance up |
| 2026-10-16T14:55 | EMA 20/50 cross | buy | AAPL | 6.35 | — | rebalance up |
| 2026-10-16T14:55 | EMA 20/50 cross | sell | ETH-USD | 8.47 | -0.12 | stop-loss |
| 2026-10-16T14:55 | EMA 20/50 cross | sell | BTC-USD | 8.45 | -0.09 | stop-loss |
| 2026-10-16T14:55 | EMA 20/50 cross | sell | BITX | 8.46 | -0.08 | stop-loss |
| 2026-10-16T14:50 | RSI(14) reversion | buy | META | 4.34 | — | entry signal |
| 2026-10-16T14:50 | Three white soldiers | buy | PLTR | 21.25 | — | entry signal |
| 2026-10-16T14:50 | Keltner breakout | sell | SQQQ | 13.49 | -0.17 | exit signal |
| 2026-10-16T14:50 | ROC + volume | buy | NVDA | 15.94 | — | entry signal |
| 2026-10-16T14:50 | EMA 20/50 cross | buy | NVDA | 8.51 | — | entry signal |
| 2026-10-16T14:50 | EMA 20/50 cross | buy | BTC-USD | 8.54 | — | entry signal |
| 2026-10-16T14:50 | EMA 20/50 cross | buy | AMZN | 8.54 | — | entry signal |
| 2026-10-16T14:50 | EMA 20/50 cross | sell | SQQQ | 6.32 | -0.07 | rebalance down |
| 2026-10-16T14:50 | EMA 20/50 cross | sell | ETH-USD | 6.37 | -0.06 | rebalance down |
| 2026-10-16T14:50 | EMA 20/50 cross | sell | BITX | 6.39 | -0.01 | rebalance down |
| 2026-10-16T14:50 | EMA 20/50 cross | sell | AAPL | 6.46 | -0.01 | rebalance down |
| 2026-10-16T14:45 | Agent (ML meta-label) | buy | MSTR | 3.37 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 14:56:05.000139+00:00 -> 2026-10-16 15:06:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
