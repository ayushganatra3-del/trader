# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T11:55:05.000170+00:00 · 24748 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.85 (-7.14%)

Closed trades 76, win rate 39.5%, fees £2.65, max drawdown -7.57%.

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

Today: 8974 decisions in 1796 calls, $0.1256 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T11:55 | 0 / 2 / 3 | MSTR 15% |  |
| Breezy | 2026-10-16T11:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T11:55 | 2 / 3 / 0 | COIN 72% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.51 | 4.51 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 103.53 | 3.53 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.17 | 0.74 | -7.55 | 43 |
| 8 | VWAP reversion · 1h | reversion | 99.69 | -0.30 | 58 | 39.7 | -11.19 | -3.15 | -13.80 | 126 |
| 9 | Hold SPY | benchmark | 99.62 | -0.38 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.40 | -0.60 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 11 | Copy: Insider buying | copy | 98.97 | -1.03 | 20 | 45.0 | -11.57 | -1.93 | -20.62 | 75 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.24 | -1.76 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 97.93 | -2.07 | 0 | — | 30.65 | 3.49 | -8.68 | 1 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.61 | -2.39 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.18 | -2.82 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.92 | -3.08 | 36 | 16.7 | 7.59 | 1.03 | -22.11 | 108 |
| 19 | Trend pullback · 1h | trend | 96.45 | -3.55 | 86 | 24.4 | -22.58 | -6.44 | -23.29 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.18 | -3.82 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.04 | -3.96 | 106 | 32.1 | -14.64 | -5.15 | -15.80 | 296 |
| 22 | Daily: Momentum burst | daily | 95.53 | -4.47 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.07 | -4.93 | 76 | 19.7 | -10.90 | -1.98 | -15.34 | 258 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.40 | 1.16 | -9.46 | 99 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 93.54 | -6.46 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 26 | Parabolic SAR · 1h | trend | 93.43 | -6.58 | 93 | 22.6 | 3.25 | 0.59 | -22.09 | 278 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.33 | 2.32 | -6.73 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.04 | -6.96 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | EMA 20/50 cross · 1h | trend | 92.95 | -7.05 | 51 | 15.7 | -6.07 | -0.64 | -23.77 | 132 |
| 30 | Daily: Bullish score | daily | 92.89 | -7.11 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -11.47 | -6.31 | -12.00 | 248 |
| 32 | MACD cross · 1h | trend | 92.63 | -7.37 | 155 | 21.9 | -12.04 | -1.58 | -26.23 | 455 |
| 33 | Bollinger breakout · 1h | breakout | 91.92 | -8.08 | 80 | 30.0 | 6.60 | 1.02 | -14.21 | 273 |
| 34 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 35 | Max aggression: 5-day momentum | meta | 91.68 | -8.32 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.80 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.30 | -8.70 | 74 | 13.5 | -1.47 | 0.04 | -28.77 | 214 |
| 38 | RSI momentum · 1h | momentum | 91.25 | -8.75 | 73 | 17.8 | 0.23 | 0.24 | -26.67 | 223 |
| 39 | Stochastic reversion · 1h | reversion | 90.80 | -9.20 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.67 | -3.21 | -9.57 | 122 |
| 42 | Triple EMA stack · 1h | trend | 89.95 | -10.05 | 77 | 16.9 | -7.50 | -0.57 | -32.08 | 235 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.01 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.56 | -10.44 | 195 | 31.3 | -15.69 | -2.71 | -18.75 | 141 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -13.89 | -1.90 | -29.15 | 211 |
| 47 | Z-score reversion · 1h | reversion | 88.07 | -11.93 | 74 | 36.5 | -10.17 | -1.82 | -17.27 | 178 |
| 48 | OBV trend · 1h | momentum | 87.68 | -12.32 | 165 | 18.8 | -10.95 | -0.93 | -34.99 | 318 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.90 | -4.32 | -21.41 | 704 |
| 50 | Agent (ML meta-label) | meta | 86.96 | -13.04 | 568 | 18.5 | -3.30 | -0.37 | -15.60 | 413 |
| 51 | MACD zero-line · 1h | trend | 86.79 | -13.21 | 75 | 16.0 | -21.01 | -4.01 | -22.72 | 226 |
| 52 | VWAP momentum · 1h | momentum | 86.02 | -13.98 | 361 | 21.9 | -34.07 | -4.89 | -43.06 | 1258 |
| 53 | Heikin-Ashi · 1h | trend | 85.81 | -14.19 | 177 | 25.4 | -30.19 | -4.84 | -39.47 | 672 |
| 54 | Donchian 20/10 · 1h | breakout | 85.79 | -14.21 | 72 | 19.4 | 0.18 | 0.22 | -20.96 | 220 |
| 55 | ROC + volume · 1h | momentum | 85.51 | -14.49 | 184 | 22.3 | -9.09 | -1.11 | -25.32 | 398 |
| 56 | Three white soldiers | momentum | 85.01 | -14.99 | 205 | 19.0 | -47.70 | -18.83 | -48.81 | 605 |
| 57 | Bollinger reversion · 1h | reversion | 84.62 | -15.38 | 132 | 31.8 | -26.59 | -5.68 | -31.47 | 337 |
| 58 | EMA 9/21 cross · 1h | trend | 84.59 | -15.41 | 120 | 12.5 | -5.13 | -0.38 | -29.27 | 322 |
| 59 | Williams %R · 1h | reversion | 83.62 | -16.38 | 168 | 42.9 | -31.17 | -5.05 | -34.85 | 525 |
| 60 | RSI(14) reversion · 1h | reversion | 83.04 | -16.96 | 62 | 24.2 | -12.43 | -2.31 | -18.95 | 169 |
| 61 | CCI reversion · 1h | reversion | 83.01 | -16.99 | 143 | 42.7 | -15.10 | -1.93 | -23.38 | 428 |
| 62 | Candlestick reversal · 1h | reversion | 79.89 | -20.11 | 186 | 26.3 | -32.11 | -5.96 | -33.79 | 516 |
| 63 | RSI(14) reversion | reversion | 66.20 | -33.80 | 580 | 28.4 | -73.30 | -16.07 | -74.03 | 1560 |
| 64 | ROC + volume | momentum | 64.87 | -35.13 | 533 | 22.3 | -75.26 | -16.89 | -76.87 | 1708 |
| 65 | Volume breakout | breakout | 63.85 | -36.15 | 323 | 13.3 | -63.74 | -17.87 | -63.74 | 888 |
| 66 | Squeeze breakout | breakout | 63.76 | -36.24 | 425 | 14.8 | -62.98 | -17.42 | -63.72 | 1216 |
| 67 | Donchian 55/20 | breakout | 61.33 | -38.67 | 429 | 17.9 | -69.40 | -14.27 | -71.57 | 1286 |
| 68 | EMA 20/50 cross | trend | 60.51 | -39.49 | 442 | 19.7 | -77.24 | -14.85 | -78.71 | 1448 |
| 69 | AI bee: Boozy | ai | 57.94 | -42.06 | 287 | 5.2 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.71 | -42.29 | 592 | 24.3 | -72.56 | -14.79 | -72.60 | 1428 |
| 71 | Keltner breakout | breakout | 55.04 | -44.96 | 600 | 16.2 | -83.68 | -25.79 | -83.68 | 1853 |
| 72 | Supertrend | trend | 53.19 | -46.81 | 622 | 20.1 | -86.26 | -19.72 | -86.57 | 1913 |
| 73 | Ichimoku | trend | 52.39 | -47.60 | 541 | 11.8 | -82.00 | -22.12 | -82.05 | 1731 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -28.52 | -98.64 | 5300 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.48 | -28.51 | -93.49 | 2593 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.61 | -23.85 | -90.62 | 2369 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.72 | -25.99 | -91.72 | 2335 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.44 | -30.59 | -97.45 | 3521 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -34.12 | -96.70 | 3602 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -24.79 | -94.36 | 2628 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -33.41 | -99.38 | 5711 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.40 | -24.90 | -91.40 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.28 | -29.99 | -96.28 | 3564 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.15 | -99.73 | 6161 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -28.07 | -91.77 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -35.62 | -97.46 | 3653 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.43 | -33.73 | -98.44 | 4676 |
| 88 | AI bee: Bizzy ⛔ | ai | 49.97 | -50.03 | 1066 | 8.9 | — | — | — | — |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.70 | -31.25 | -93.70 | 2805 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -36.17 | -99.52 | 6159 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -85.93 | -21.24 | -86.09 | 2102 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.41 | -25.54 | -87.54 | 2112 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -30.42 | -95.91 | 3757 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.16 | -31.31 | -89.21 | 2100 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.66 | -31.49 | -95.67 | 4066 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.84 | -99.89 | 8234 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T11:55 | Three white soldiers | sell | BTC-USD | 21.11 | -0.19 | stop-loss |
| 2026-10-16T11:55 | Keltner breakout | sell | DOGE-USD | 10.98 | -0.11 | stop-loss |
| 2026-10-16T11:55 | Donchian 55/20 | buy | DOGE-USD | 3.07 | — | rebalance up |
| 2026-10-16T11:55 | ROC + volume | buy | DOGE-USD | 3.25 | — | rebalance up |
| 2026-10-16T11:50 | Volume breakout | sell | XRP-USD | 12.78 | -0.10 | exit signal |
| 2026-10-16T11:50 | Volume breakout | sell | ETH-USD | 15.96 | -0.16 | exit signal |
| 2026-10-16T11:45 | Volume breakout | sell | DOGE-USD | 12.78 | -0.11 | exit signal |
| 2026-10-16T11:40 | Volume breakout | buy | ETH-USD | 3.23 | — | rebalance up |
| 2026-10-16T11:40 | Volume breakout | sell | SOL-USD | 12.73 | -0.15 | stop-loss |
| 2026-10-16T11:40 | Keltner breakout | sell | SOL-USD | 10.96 | -0.13 | stop-loss |
| 2026-10-16T11:40 | Donchian 55/20 | sell | SOL-USD | 12.21 | -0.14 | stop-loss |
| 2026-10-16T11:40 | ROC + volume | buy | ETH-USD | 3.29 | — | rebalance up |
| 2026-10-16T11:40 | ROC + volume | sell | SOL-USD | 12.90 | -0.15 | stop-loss |
| 2026-10-16T11:28 | AI bee: Boozy | sell | ETH-USD | 16.48 | -0.01 | Jev: add (buy p=0.57) |
| 2026-10-16T11:25 | Three white soldiers | buy | BTC-USD | 21.30 | — | entry signal |
| 2026-10-16T11:15 | AI bee: Bizzy | sell | ETH-USD | 7.91 | -0.04 | Kill switch: down 50% from peak |
| 2026-10-16T11:15 | Volume breakout | buy | XRP-USD | 12.88 | — | entry signal |
| 2026-10-16T11:15 | Volume breakout | buy | SOL-USD | 12.88 | — | entry signal |
| 2026-10-16T11:15 | Volume breakout | buy | ETH-USD | 12.88 | — | entry signal |
| 2026-10-16T11:15 | Volume breakout | buy | DOGE-USD | 12.88 | — | entry signal |
| 2026-10-16T11:15 | Volume breakout | buy | BTC-USD | 12.88 | — | entry signal |
| 2026-10-16T11:15 | Keltner breakout | buy | XRP-USD | 11.08 | — | entry signal |
| 2026-10-16T11:15 | Keltner breakout | buy | SOL-USD | 11.09 | — | entry signal |
| 2026-10-16T11:15 | Keltner breakout | buy | DOGE-USD | 11.09 | — | entry signal |
| 2026-10-16T11:15 | Keltner breakout | buy | BTC-USD | 11.09 | — | entry signal |
| 2026-10-16T11:15 | Keltner breakout | sell | ETH-USD | 2.83 | 0.01 | rebalance down |
| 2026-10-16T11:15 | Donchian 55/20 | buy | XRP-USD | 12.34 | — | entry signal |
| 2026-10-16T11:15 | Donchian 55/20 | buy | SOL-USD | 12.35 | — | entry signal |
| 2026-10-16T11:15 | Donchian 55/20 | buy | DOGE-USD | 12.35 | — | entry signal |
| 2026-10-16T11:15 | Donchian 55/20 | buy | BTC-USD | 12.35 | — | entry signal |
| 2026-10-16T11:15 | Donchian 55/20 | sell | ETH-USD | 3.16 | 0.01 | rebalance down |
| 2026-10-16T11:15 | ROC + volume | buy | SOL-USD | 13.06 | — | entry signal |
| 2026-10-16T11:15 | ROC + volume | buy | ETH-USD | 13.07 | — | entry signal |
| 2026-10-16T11:15 | ROC + volume | buy | DOGE-USD | 13.07 | — | entry signal |
| 2026-10-16T11:15 | ROC + volume | buy | BTC-USD | 13.07 | — | entry signal |
| 2026-10-16T11:15 | ROC + volume | sell | XRP-USD | 3.28 | -0.00 | rebalance down |
| 2026-10-16T11:15 | EMA 20/50 cross | buy | BTC-USD | 15.19 | — | entry signal |
| 2026-10-16T11:14 | AI bee: Bizzy | buy | ETH-USD | 7.96 | — | Jev: buy (buy p=0.64) |
| 2026-10-16T11:12 | AI bee: Boozy | buy | ETH-USD | 16.48 | — | Jev: buy (buy p=0.75) |
| 2026-10-16T11:10 | Supertrend | buy | SOL-USD | 2.65 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 11:55:05.000170+00:00 -> 2026-10-16 12:05:05.000170+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
