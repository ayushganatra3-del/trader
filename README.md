# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T12:25:05.000165+00:00 · 24772 ticks

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

Today: 9334 decisions in 1868 calls, $0.1307 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T12:25 | 3 / 2 / 0 | MSTR 15%, SOL-USD 14% |  |
| Breezy | 2026-10-16T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T12:25 | 4 / 1 / 0 | COIN 72% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.51 | 4.51 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 103.53 | 3.53 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.73 | -7.55 | 43 |
| 8 | VWAP reversion · 1h | reversion | 99.69 | -0.30 | 58 | 39.7 | -11.10 | -3.14 | -13.79 | 127 |
| 9 | Hold SPY | benchmark | 99.62 | -0.38 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.40 | -0.60 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 11 | Copy: Insider buying | copy | 98.97 | -1.03 | 20 | 45.0 | -11.57 | -1.93 | -20.62 | 75 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.24 | -1.76 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 15 | Hold BTC | benchmark | 97.62 | -2.38 | 0 | — | 30.30 | 3.46 | -8.68 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.61 | -2.39 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.18 | -2.82 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.92 | -3.08 | 36 | 16.7 | 7.04 | 0.98 | -22.11 | 109 |
| 19 | Trend pullback · 1h | trend | 96.45 | -3.55 | 86 | 24.4 | -22.58 | -6.44 | -23.29 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.18 | -3.82 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.04 | -3.96 | 106 | 32.1 | -13.59 | -4.48 | -14.77 | 291 |
| 22 | Daily: Momentum burst | daily | 95.53 | -4.47 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.05 | -4.95 | 76 | 19.7 | -11.12 | -2.02 | -15.34 | 259 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.68 | 1.02 | -9.46 | 103 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 93.54 | -6.46 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 26 | Parabolic SAR · 1h | trend | 93.39 | -6.61 | 93 | 22.6 | 3.21 | 0.58 | -22.09 | 278 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.31 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.04 | -6.96 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | EMA 20/50 cross · 1h | trend | 92.89 | -7.11 | 51 | 15.7 | -6.39 | -0.69 | -23.78 | 133 |
| 30 | Daily: Bullish score | daily | 92.89 | -7.11 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.99 | -6.20 | -11.52 | 247 |
| 32 | MACD cross · 1h | trend | 92.53 | -7.47 | 155 | 21.9 | -12.13 | -1.60 | -26.23 | 456 |
| 33 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 34 | Max aggression: 5-day momentum | meta | 91.68 | -8.32 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 35 | Bollinger breakout · 1h | breakout | 91.66 | -8.34 | 80 | 30.0 | 6.28 | 0.98 | -14.21 | 275 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.83 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.23 | -8.77 | 74 | 13.5 | -1.56 | 0.03 | -28.77 | 214 |
| 38 | RSI momentum · 1h | momentum | 91.20 | -8.80 | 73 | 17.8 | 0.43 | 0.26 | -26.67 | 222 |
| 39 | Stochastic reversion · 1h | reversion | 90.80 | -9.20 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.18 | -3.01 | -9.08 | 123 |
| 42 | Triple EMA stack · 1h | trend | 89.83 | -10.16 | 77 | 16.9 | -7.64 | -0.59 | -32.18 | 236 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.00 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.56 | -10.44 | 195 | 31.3 | -16.46 | -2.82 | -19.82 | 140 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -13.66 | -1.86 | -29.15 | 209 |
| 47 | Z-score reversion · 1h | reversion | 88.07 | -11.93 | 74 | 36.5 | -10.17 | -1.82 | -17.27 | 178 |
| 48 | OBV trend · 1h | momentum | 87.63 | -12.37 | 165 | 18.8 | -10.72 | -0.91 | -34.79 | 318 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.32 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 86.91 | -13.09 | 568 | 18.5 | -4.70 | -0.61 | -17.09 | 399 |
| 51 | MACD zero-line · 1h | trend | 86.67 | -13.33 | 75 | 16.0 | -21.29 | -4.07 | -22.72 | 226 |
| 52 | VWAP momentum · 1h | momentum | 85.98 | -14.02 | 361 | 21.9 | -34.10 | -4.89 | -43.06 | 1258 |
| 53 | Heikin-Ashi · 1h | trend | 85.80 | -14.20 | 177 | 25.4 | -29.83 | -4.77 | -39.15 | 672 |
| 54 | Donchian 20/10 · 1h | breakout | 85.64 | -14.36 | 72 | 19.4 | -0.02 | 0.20 | -20.97 | 220 |
| 55 | ROC + volume · 1h | momentum | 85.42 | -14.58 | 184 | 22.3 | -9.43 | -1.15 | -25.32 | 399 |
| 56 | Three white soldiers | momentum | 85.01 | -14.99 | 205 | 19.0 | -47.89 | -19.46 | -48.69 | 610 |
| 57 | Bollinger reversion · 1h | reversion | 84.62 | -15.38 | 132 | 31.8 | -26.62 | -5.70 | -31.47 | 337 |
| 58 | EMA 9/21 cross · 1h | trend | 84.48 | -15.52 | 120 | 12.5 | -5.30 | -0.40 | -29.27 | 321 |
| 59 | Williams %R · 1h | reversion | 83.62 | -16.38 | 168 | 42.9 | -31.03 | -5.03 | -34.85 | 524 |
| 60 | RSI(14) reversion · 1h | reversion | 83.04 | -16.96 | 62 | 24.2 | -12.54 | -2.33 | -18.95 | 172 |
| 61 | CCI reversion · 1h | reversion | 83.01 | -16.99 | 143 | 42.7 | -14.89 | -1.89 | -23.38 | 427 |
| 62 | Candlestick reversal · 1h | reversion | 79.89 | -20.11 | 186 | 26.3 | -31.73 | -5.89 | -33.43 | 519 |
| 63 | RSI(14) reversion | reversion | 66.20 | -33.80 | 580 | 28.4 | -73.23 | -16.02 | -73.96 | 1559 |
| 64 | ROC + volume | momentum | 64.53 | -35.47 | 537 | 22.2 | -75.40 | -16.95 | -77.00 | 1710 |
| 65 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.71 | -17.86 | -63.71 | 887 |
| 66 | Squeeze breakout | breakout | 63.76 | -36.24 | 425 | 14.8 | -62.99 | -17.42 | -63.72 | 1216 |
| 67 | Donchian 55/20 | breakout | 61.07 | -38.93 | 432 | 17.8 | -69.50 | -14.27 | -71.74 | 1285 |
| 68 | EMA 20/50 cross | trend | 60.22 | -39.78 | 444 | 19.6 | -77.33 | -14.88 | -78.84 | 1447 |
| 69 | AI bee: Boozy | ai | 57.94 | -42.06 | 287 | 5.2 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.71 | -42.29 | 592 | 24.3 | -72.49 | -14.75 | -72.52 | 1426 |
| 71 | Keltner breakout | breakout | 54.85 | -45.15 | 603 | 16.1 | -83.80 | -25.92 | -83.80 | 1855 |
| 72 | Supertrend | trend | 52.77 | -47.23 | 627 | 19.9 | -86.36 | -19.81 | -86.62 | 1912 |
| 73 | Ichimoku | trend | 52.05 | -47.95 | 545 | 11.7 | -82.12 | -22.24 | -82.12 | 1731 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -28.45 | -98.63 | 5295 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -28.63 | -93.53 | 2593 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.67 | -23.90 | -90.67 | 2368 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.75 | -26.02 | -91.75 | 2336 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -30.76 | -97.47 | 3523 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.72 | -34.08 | -96.72 | 3607 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.50 | -25.13 | -94.50 | 2638 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -33.40 | -99.37 | 5706 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.43 | -24.92 | -91.43 | 2648 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -30.09 | -96.32 | 3563 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.14 | -99.73 | 6160 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -28.07 | -91.77 | 2368 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -35.65 | -97.46 | 3654 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -33.78 | -98.44 | 4679 |
| 88 | AI bee: Bizzy ⛔ | ai | 49.97 | -50.03 | 1066 | 8.9 | — | — | — | — |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.73 | -31.29 | -93.73 | 2805 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -36.23 | -99.53 | 6164 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -85.93 | -21.24 | -86.09 | 2102 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.47 | -25.49 | -87.60 | 2109 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -30.42 | -95.91 | 3759 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.24 | -31.60 | -89.24 | 2099 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -31.54 | -95.68 | 4071 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.72 | -99.89 | 8231 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T12:15 | Ichimoku | sell | ETH-USD | 13.02 | -0.09 | exit signal |
| 2026-10-16T12:15 | Supertrend | sell | SOL-USD | 13.17 | -0.13 | exit signal |
| 2026-10-16T12:15 | Supertrend | sell | ETH-USD | 10.58 | -0.05 | exit signal |
| 2026-10-16T12:15 | EMA 20/50 cross | sell | SOL-USD | 14.98 | -0.18 | stop-loss |
| 2026-10-16T12:10 | Donchian 55/20 | sell | BTC-USD | 12.23 | -0.12 | stop-loss |
| 2026-10-16T12:10 | Ichimoku | sell | BTC-USD | 13.01 | -0.07 | exit signal |
| 2026-10-16T12:10 | EMA 20/50 cross | sell | BTC-USD | 15.04 | -0.15 | stop-loss |
| 2026-10-16T12:05 | Keltner breakout | sell | XRP-USD | 10.95 | -0.13 | stop-loss |
| 2026-10-16T12:05 | Keltner breakout | sell | ETH-USD | 10.97 | -0.04 | stop-loss |
| 2026-10-16T12:05 | Keltner breakout | sell | BTC-USD | 10.99 | -0.10 | stop-loss |
| 2026-10-16T12:05 | Donchian 55/20 | sell | XRP-USD | 12.20 | -0.14 | stop-loss |
| 2026-10-16T12:05 | Donchian 55/20 | sell | DOGE-USD | 15.23 | -0.19 | stop-loss |
| 2026-10-16T12:05 | ROC + volume | sell | XRP-USD | 12.95 | -0.09 | stop-loss |
| 2026-10-16T12:05 | ROC + volume | sell | ETH-USD | 16.15 | -0.21 | stop-loss |
| 2026-10-16T12:05 | ROC + volume | sell | DOGE-USD | 16.11 | -0.20 | stop-loss |
| 2026-10-16T12:05 | ROC + volume | sell | BTC-USD | 12.94 | -0.12 | stop-loss |
| 2026-10-16T12:05 | Ichimoku | sell | XRP-USD | 13.02 | -0.09 | exit signal |
| 2026-10-16T12:05 | Ichimoku | sell | SOL-USD | 12.97 | -0.14 | exit signal |
| 2026-10-16T12:05 | Supertrend | buy | SOL-USD | 7.95 | — | rebalance up |
| 2026-10-16T12:05 | Supertrend | sell | XRP-USD | 13.20 | -0.07 | exit signal |
| 2026-10-16T12:05 | Supertrend | sell | DOGE-USD | 13.17 | -0.10 | exit signal |
| 2026-10-16T12:05 | Supertrend | sell | BTC-USD | 10.59 | -0.04 | exit signal |
| 2026-10-16T12:00 | Bollinger breakout · 1h | buy | ETH-USD | 22.98 | — | entry signal |
| 2026-10-16T12:00 | Bollinger breakout · 1h | buy | BTC-USD | 22.98 | — | entry signal |
| 2026-10-16T12:00 | ROC + volume · 1h | buy | SOL-USD | 21.38 | — | entry signal |
| 2026-10-16T12:00 | MACD cross · 1h | buy | BTC-USD | 6.17 | — | entry signal |
| 2026-10-16T12:00 | Triple EMA stack · 1h | buy | ETH-USD | 21.93 | — | entry signal |
| 2026-10-16T12:00 | Volume breakout | sell | BTC-USD | 12.79 | -0.09 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 12:25:05.000165+00:00 -> 2026-10-16 12:35:05.000165+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
