# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T21:25:05.000160+00:00 · 26422 ticks

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

Today: 16302 decisions in 3261 calls, $0.2279 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T21:25 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-17T21:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T21:25 | 0 / 4 / 1 | COIN 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 2.27 | +3.35% | 6 |
| VWAP momentum · 1h | SQQQ | 2.13 | +12.90% | 7 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 2.01 | +0.94% | 8 |
| Opening range 30m | AMZN | 1.94 | +3.77% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.15 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.39 | -3.30 | -13.80 | 134 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.94 | 1.65 | -2.15 | 66 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.66 | 1.18 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -10.40 | -4.41 | -11.57 | 289 |
| 17 | Hold BTC | benchmark | 96.66 | -3.34 | 0 | — | 29.28 | 3.43 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -20.22 | -6.11 | -20.39 | 142 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | 1.64 | 0.41 | -14.97 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.34 | 0.95 | -9.46 | 103 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.40 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -18.01 | -3.09 | -21.23 | 125 |
| 28 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -0.53 | 0.11 | -22.55 | 273 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.42 | -1.85 | -8.74 | 122 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -8.94 | -5.30 | -12.50 | 249 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.77 | -0.10 | -14.55 | 115 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.29 | 0.36 | -26.55 | 217 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.60 | 1.04 | -14.21 | 268 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.07 | -0.52 | -33.23 | 229 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -8.65 | -1.24 | -20.21 | 114 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -22.34 | -4.62 | -26.17 | 207 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -7.87 | -0.94 | -27.05 | 202 |
| 42 | MACD cross · 1h | trend | 88.45 | -11.55 | 175 | 22.3 | -15.35 | -2.05 | -28.89 | 459 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.61 | -7.79 | -25.98 | 235 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -8.15 | -0.64 | -34.04 | 317 |
| 45 | Stochastic reversion · 1h | reversion | 86.84 | -13.16 | 140 | 44.3 | -20.77 | -3.79 | -22.11 | 368 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.22 | -4.51 | -21.41 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.75 | -14.25 | 81 | 16.0 | -22.51 | -4.42 | -23.64 | 217 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 2.34 | 0.48 | -21.63 | 212 |
| 50 | Three white soldiers | momentum | 84.53 | -15.47 | 210 | 19.0 | -47.03 | -19.09 | -47.90 | 598 |
| 51 | MFI reversion · 1h | reversion | 83.96 | -16.04 | 204 | 30.4 | -20.96 | -3.46 | -21.51 | 142 |
| 52 | Z-score reversion · 1h | reversion | 83.32 | -16.68 | 86 | 31.4 | -15.53 | -2.70 | -19.86 | 182 |
| 53 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.46 | -1.63 | -27.07 | 395 |
| 54 | VWAP momentum · 1h | momentum | 82.51 | -17.49 | 395 | 20.8 | -36.35 | -5.53 | -44.69 | 1253 |
| 55 | Heikin-Ashi · 1h | trend | 82.50 | -17.50 | 196 | 23.5 | -31.16 | -5.12 | -40.96 | 675 |
| 56 | Agent (ML meta-label) | meta | 82.43 | -17.57 | 649 | 18.2 | -17.17 | -3.16 | -23.24 | 392 |
| 57 | EMA 9/21 cross · 1h | trend | 81.67 | -18.33 | 129 | 11.6 | -5.70 | -0.43 | -29.74 | 312 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.85 | -5.72 | -36.19 | 531 |
| 59 | Bollinger reversion · 1h | reversion | 80.03 | -19.97 | 141 | 31.2 | -30.48 | -6.35 | -32.42 | 345 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.53 | -2.59 | -21.70 | 162 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.40 | -2.52 | -25.90 | 425 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.19 | -6.55 | -36.66 | 536 |
| 63 | Volume breakout | breakout | 63.34 | -36.66 | 329 | 13.1 | -63.41 | -18.28 | -63.41 | 882 |
| 64 | ROC + volume | momentum | 62.81 | -37.19 | 554 | 21.8 | -75.97 | -17.84 | -77.53 | 1725 |
| 65 | Squeeze breakout | breakout | 62.36 | -37.64 | 437 | 14.6 | -62.89 | -17.93 | -64.44 | 1216 |
| 66 | RSI(14) reversion | reversion | 60.85 | -39.15 | 662 | 25.2 | -74.40 | -16.67 | -74.44 | 1628 |
| 67 | Donchian 55/20 | breakout | 60.32 | -39.68 | 445 | 17.5 | -69.37 | -14.69 | -72.07 | 1286 |
| 68 | EMA 20/50 cross | trend | 58.57 | -41.43 | 465 | 18.9 | -76.90 | -15.19 | -79.43 | 1444 |
| 69 | VWAP reversion | reversion | 54.48 | -45.52 | 695 | 23.5 | -73.14 | -15.50 | -73.27 | 1506 |
| 70 | AI bee: Boozy | ai | 53.62 | -46.38 | 318 | 6.3 | — | — | — | — |
| 71 | Keltner breakout | breakout | 53.50 | -46.49 | 620 | 15.8 | -83.31 | -26.90 | -83.31 | 1833 |
| 72 | Ichimoku | trend | 50.69 | -49.31 | 567 | 11.5 | -82.18 | -23.41 | -82.18 | 1735 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -29.94 | -98.61 | 5313 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -30.52 | -93.55 | 2603 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.55 | -20.52 | -87.49 | 1914 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -24.93 | -90.65 | 2370 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.53 | -27.21 | -91.53 | 2325 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.44 | -32.77 | -97.44 | 3530 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -36.82 | -96.82 | 3631 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.14 | -26.89 | -94.32 | 2592 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -37.05 | -99.39 | 5821 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.36 | -25.99 | -91.38 | 2647 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.18 | -32.30 | -96.18 | 3540 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.88 | -99.74 | 6242 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.66 | -91.78 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -39.02 | -97.52 | 3667 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.95 | -98.49 | 4768 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.75 | -33.43 | -93.75 | 2815 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.04 | -99.53 | 6248 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.37 | -86.75 | 2166 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.99 | -27.32 | -87.99 | 2165 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -33.05 | -95.93 | 3816 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -33.95 | -89.30 | 2113 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.84 | -34.07 | -95.84 | 4157 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.34 | -99.89 | 8304 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T21:25 | Keltner breakout | sell | ETH-USD | 13.37 | -0.13 | stop-loss |
| 2026-10-17T21:25 | Keltner breakout | sell | BTC-USD | 13.39 | -0.08 | stop-loss |
| 2026-10-17T21:25 | Donchian 55/20 | sell | XRP-USD | 15.05 | -0.15 | stop-loss |
| 2026-10-17T21:25 | Donchian 55/20 | sell | ETH-USD | 15.07 | -0.15 | stop-loss |
| 2026-10-17T21:25 | Donchian 55/20 | sell | DOGE-USD | 15.09 | -0.12 | exit signal |
| 2026-10-17T21:25 | Donchian 55/20 | sell | BTC-USD | 15.10 | -0.11 | exit signal |
| 2026-10-17T21:25 | Ichimoku | sell | BTC-USD | 12.62 | -0.07 | exit signal |
| 2026-10-17T21:25 | EMA 20/50 cross | buy | ETH-USD | 2.94 | — | rebalance up |
| 2026-10-17T21:25 | EMA 20/50 cross | sell | BTC-USD | 2.94 | -0.02 | rebalance down |
| 2026-10-17T21:20 | Squeeze breakout | sell | DOGE-USD | 15.63 | 0.02 | stop-loss |
| 2026-10-17T21:20 | Keltner breakout | sell | XRP-USD | 13.38 | -0.10 | stop-loss |
| 2026-10-17T21:20 | Keltner breakout | sell | DOGE-USD | 10.72 | -0.01 | stop-loss |
| 2026-10-17T21:19 | AI bee: Boozy | sell | ETH-USD | 16.56 | -0.11 | Jev: buy |
| 2026-10-17T21:10 | Volume breakout | sell | SOL-USD | 15.76 | -0.10 | exit signal |
| 2026-10-17T21:10 | Keltner breakout | buy | XRP-USD | 8.03 | — | rebalance up |
| 2026-10-17T21:10 | Keltner breakout | buy | ETH-USD | 2.71 | — | rebalance up |
| 2026-10-17T21:10 | Keltner breakout | sell | SOL-USD | 13.39 | -0.07 | exit signal |
| 2026-10-17T21:05 | VWAP reversion | sell | ETH-USD | 13.64 | 0.02 | exit signal |
| 2026-10-17T21:05 | Keltner breakout | buy | XRP-USD | 5.45 | — | entry signal |
| 2026-10-17T21:05 | Keltner breakout | buy | ETH-USD | 10.79 | — | entry signal |
| 2026-10-17T21:05 | Keltner breakout | sell | DOGE-USD | 2.74 | 0.01 | rebalance down |
| 2026-10-17T21:05 | Donchian 55/20 | buy | ETH-USD | 15.21 | — | entry signal |
| 2026-10-17T21:04 | AI bee: Boozy | buy | ETH-USD | 16.67 | — | Jev: buy (buy p=0.70) |
| 2026-10-17T21:00 | Bollinger reversion · 1h | buy | SOL-USD | 1.64 | — | entry |
| 2026-10-17T21:00 | Bollinger reversion · 1h | buy | ETH-USD | 7.28 | — | entry |
| 2026-10-17T21:00 | Bollinger reversion · 1h | sell | DOGE-USD | 8.01 | 0.00 | exit signal |
| 2026-10-17T21:00 | Heikin-Ashi · 1h | buy | XRP-USD | 6.11 | — | entry signal |
| 2026-10-17T21:00 | Heikin-Ashi · 1h | buy | SOL-USD | 13.81 | — | entry signal |
| 2026-10-17T21:00 | Heikin-Ashi · 1h | sell | ETH-USD | 6.16 | -0.03 | rebalance down |
| 2026-10-17T21:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 6.89 | -0.03 | rebalance down |
| 2026-10-17T21:00 | Heikin-Ashi · 1h | sell | BTC-USD | 6.86 | -0.04 | rebalance down |
| 2026-10-17T20:35 | Donchian 55/20 | buy | XRP-USD | 15.20 | — | entry signal |
| 2026-10-17T20:00 | VWAP momentum · 1h | buy | XRP-USD | 19.90 | — | entry signal |
| 2026-10-17T20:00 | VWAP momentum · 1h | buy | DOGE-USD | 20.70 | — | entry signal |
| 2026-10-17T20:00 | VWAP momentum · 1h | buy | BTC-USD | 20.70 | — | entry signal |
| 2026-10-17T20:00 | Heikin-Ashi · 1h | buy | ETH-USD | 20.02 | — | entry signal |
| 2026-10-17T20:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 20.74 | — | entry signal |
| 2026-10-17T20:00 | Heikin-Ashi · 1h | buy | BTC-USD | 20.74 | — | entry signal |
| 2026-10-17T20:00 | MACD cross · 1h | buy | XRP-USD | 8.06 | — | entry signal |
| 2026-10-17T20:00 | MACD cross · 1h | buy | BTC-USD | 17.71 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 21:25:05.000160+00:00 -> 2026-10-17 21:35:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
