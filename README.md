# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T06:55:05.000138+00:00 · 24480 ticks

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
| Copy: Insider buying | 2026-10-15 | GGR 12%, BORR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 4957 decisions in 992 calls, $0.0694 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T06:55 | 0 / 1 / 4 | MSTR 15% |  |
| Breezy | 2026-10-16T06:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T06:55 | 1 / 4 / 0 | COIN 71% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.84 | 4.84 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 103.85 | 3.85 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Hold SPY | benchmark | 99.93 | -0.07 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.17 | 0.74 | -7.55 | 43 |
| 9 | VWAP reversion · 1h | reversion | 99.77 | -0.23 | 58 | 39.7 | -11.19 | -3.15 | -13.80 | 126 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.71 | -0.29 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 11 | Copy: Insider buying | copy | 99.24 | -0.76 | 20 | 45.0 | -11.57 | -1.93 | -20.62 | 75 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.55 | -1.45 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.77 | -2.23 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Hold BTC | benchmark | 97.71 | -2.29 | 0 | — | 29.90 | 3.42 | -8.68 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.49 | -2.51 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 97.00 | -3.00 | 36 | 16.7 | 6.62 | 0.93 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.60 | -3.40 | 86 | 24.4 | -22.58 | -6.44 | -23.29 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.25 | -3.75 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.07 | -3.93 | 106 | 32.1 | -14.29 | -4.61 | -15.92 | 293 |
| 22 | Daily: Momentum burst | daily | 95.60 | -4.40 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.23 | -4.77 | 75 | 20.0 | -11.59 | -2.12 | -15.34 | 261 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 93.84 | -6.16 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.96 | 1.08 | -9.46 | 101 |
| 26 | Parabolic SAR · 1h | trend | 93.53 | -6.47 | 93 | 22.6 | 3.19 | 0.58 | -22.05 | 277 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.33 | 2.32 | -6.73 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.19 | -6.81 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.13 | -6.87 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.11 | -6.89 | 51 | 15.7 | -1.08 | 0.07 | -24.95 | 133 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.21 | -5.29 | -10.74 | 248 |
| 32 | MACD cross · 1h | trend | 92.82 | -7.18 | 154 | 22.1 | -11.76 | -1.54 | -26.23 | 453 |
| 33 | Bollinger breakout · 1h | breakout | 92.13 | -7.87 | 79 | 30.4 | 6.70 | 1.03 | -14.21 | 273 |
| 34 | Max aggression: 5-day momentum | meta | 91.97 | -8.03 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.42 | -8.58 | 74 | 13.5 | -1.63 | 0.02 | -28.77 | 214 |
| 38 | RSI momentum · 1h | momentum | 91.31 | -8.69 | 73 | 17.8 | 0.56 | 0.28 | -26.67 | 221 |
| 39 | Stochastic reversion · 1h | reversion | 91.09 | -8.91 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.67 | -3.21 | -9.57 | 122 |
| 42 | Triple EMA stack · 1h | trend | 90.12 | -9.88 | 77 | 16.9 | -6.88 | -0.51 | -32.05 | 234 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.01 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.73 | -10.27 | 194 | 30.9 | -15.69 | -2.71 | -18.75 | 141 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.33 | -11.67 | 74 | 36.5 | -10.17 | -1.82 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.83 | -12.17 | 165 | 18.8 | -10.73 | -0.91 | -34.85 | 316 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.90 | -4.32 | -21.41 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.14 | -12.86 | 568 | 18.5 | 0.91 | 0.30 | -15.46 | 396 |
| 51 | MACD zero-line · 1h | trend | 86.93 | -13.07 | 74 | 16.2 | -21.73 | -4.18 | -22.72 | 228 |
| 52 | VWAP momentum · 1h | momentum | 86.21 | -13.79 | 360 | 21.9 | -34.36 | -4.95 | -43.06 | 1258 |
| 53 | Heikin-Ashi · 1h | trend | 86.07 | -13.94 | 175 | 25.7 | -30.28 | -4.86 | -39.47 | 671 |
| 54 | Donchian 20/10 · 1h | breakout | 85.77 | -14.23 | 72 | 19.4 | -0.15 | 0.19 | -20.96 | 220 |
| 55 | ROC + volume · 1h | momentum | 85.60 | -14.40 | 184 | 22.3 | -9.09 | -1.11 | -25.32 | 398 |
| 56 | Three white soldiers | momentum | 85.20 | -14.80 | 204 | 19.1 | -47.67 | -18.80 | -48.89 | 605 |
| 57 | Bollinger reversion · 1h | reversion | 84.89 | -15.12 | 132 | 31.8 | -26.66 | -5.70 | -31.47 | 338 |
| 58 | EMA 9/21 cross · 1h | trend | 84.59 | -15.41 | 120 | 12.5 | -5.41 | -0.41 | -29.27 | 322 |
| 59 | Williams %R · 1h | reversion | 83.89 | -16.11 | 168 | 42.9 | -31.08 | -5.04 | -34.85 | 525 |
| 60 | RSI(14) reversion · 1h | reversion | 83.28 | -16.72 | 62 | 24.2 | -13.40 | -2.50 | -18.95 | 177 |
| 61 | CCI reversion · 1h | reversion | 83.26 | -16.75 | 143 | 42.7 | -15.23 | -1.94 | -23.38 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 80.12 | -19.88 | 185 | 25.9 | -33.26 | -6.19 | -34.68 | 527 |
| 63 | RSI(14) reversion | reversion | 66.26 | -33.74 | 577 | 28.4 | -73.36 | -16.09 | -74.10 | 1560 |
| 64 | ROC + volume | momentum | 65.58 | -34.42 | 530 | 22.5 | -75.00 | -16.73 | -76.65 | 1702 |
| 65 | Volume breakout | breakout | 64.41 | -35.59 | 319 | 13.5 | -63.46 | -17.70 | -63.46 | 884 |
| 66 | Squeeze breakout | breakout | 64.27 | -35.73 | 421 | 15.0 | -62.82 | -17.31 | -63.46 | 1215 |
| 67 | Donchian 55/20 | breakout | 62.30 | -37.70 | 424 | 18.2 | -69.16 | -14.21 | -71.16 | 1283 |
| 68 | EMA 20/50 cross | trend | 61.01 | -38.99 | 440 | 19.8 | -77.34 | -14.89 | -78.63 | 1450 |
| 69 | AI bee: Boozy | ai | 58.26 | -41.74 | 283 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.75 | -42.25 | 591 | 24.4 | -72.81 | -14.93 | -72.85 | 1434 |
| 71 | Keltner breakout | breakout | 55.64 | -44.37 | 595 | 16.3 | -83.60 | -25.71 | -83.60 | 1851 |
| 72 | Supertrend | trend | 53.72 | -46.28 | 617 | 20.3 | -86.32 | -19.74 | -86.46 | 1916 |
| 73 | Ichimoku | trend | 53.07 | -46.93 | 534 | 11.8 | -81.94 | -21.99 | -81.95 | 1728 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -28.54 | -98.64 | 5303 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.46 | -28.40 | -93.46 | 2589 |
| 76 | AI bee: Bizzy | ai | 50.47 | -49.53 | 1054 | 9.0 | — | — | — | — |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.57 | -23.78 | -90.57 | 2365 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.58 | -25.78 | -91.60 | 2325 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -30.74 | -97.48 | 3527 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.61 | -33.60 | -96.61 | 3587 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -24.74 | -94.37 | 2628 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -33.54 | -99.38 | 5718 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.29 | -24.69 | -91.30 | 2644 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.24 | -29.81 | -96.24 | 3555 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.06 | -99.73 | 6157 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -28.19 | -91.83 | 2372 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -35.64 | -97.47 | 3657 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -33.84 | -98.46 | 4678 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.65 | -31.21 | -93.65 | 2802 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -36.25 | -99.53 | 6166 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -85.93 | -21.24 | -86.12 | 2101 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.48 | -25.67 | -87.63 | 2112 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -30.59 | -95.97 | 3760 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -31.54 | -89.37 | 2106 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -31.48 | -95.73 | 4070 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.88 | -99.89 | 8233 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T06:50 | Squeeze breakout | buy | XRP-USD | 16.09 | — | entry signal |
| 2026-10-16T06:50 | Keltner breakout | buy | SOL-USD | 13.93 | — | entry signal |
| 2026-10-16T06:50 | Donchian 55/20 | buy | XRP-USD | 15.60 | — | entry signal |
| 2026-10-16T06:50 | ROC + volume | buy | SOL-USD | 16.41 | — | entry signal |
| 2026-10-16T06:50 | Ichimoku | buy | ETH-USD | 13.29 | — | entry signal |
| 2026-10-16T06:49 | AI bee: Bizzy | sell | XRP-USD | 6.95 | -0.02 | Jev: sell (sell p=0.54) after 16 min |
| 2026-10-16T06:44 | AI bee: Bizzy | sell | SOL-USD | 7.33 | -0.04 | Jev: sell (sell p=0.54) after 11 min |
| 2026-10-16T06:35 | Ichimoku | buy | SOL-USD | 13.29 | — | entry signal |
| 2026-10-16T06:33 | AI bee: Bizzy | buy | XRP-USD | 6.97 | — | Jev: buy (buy p=0.55) |
| 2026-10-16T06:33 | AI bee: Bizzy | buy | SOL-USD | 7.37 | — | Jev: buy (buy p=0.58) |
| 2026-10-16T06:33 | AI bee: Bizzy | sell | DOGE-USD | 7.59 | -0.03 | Jev: sell (sell p=0.50) after 10 min |
| 2026-10-16T06:23 | AI bee: Bizzy | buy | DOGE-USD | 7.62 | — | Jev: buy (buy p=0.60) |
| 2026-10-16T06:10 | EMA 20/50 cross | sell | BTC-USD | 15.18 | -0.11 | exit signal |
| 2026-10-16T06:07 | AI bee: Bizzy | sell | XRP-USD | 7.61 | -0.06 | Jev: sell (sell p=0.84) after 12 min |
| 2026-10-16T06:05 | Donchian 55/20 | sell | XRP-USD | 15.56 | -0.17 | stop-loss |
| 2026-10-16T06:05 | ROC + volume | sell | ETH-USD | 16.34 | -0.15 | exit signal |
| 2026-10-16T06:05 | ROC + volume | sell | DOGE-USD | 16.40 | -0.13 | exit signal |
| 2026-10-16T06:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 12.24 | — | entry signal |
| 2026-10-16T06:00 | Donchian 20/10 · 1h | sell | SOL-USD | 4.90 | -0.06 | rebalance down |
| 2026-10-16T06:00 | Donchian 20/10 · 1h | sell | ETH-USD | 4.97 | -0.04 | rebalance down |
| 2026-10-16T06:00 | Donchian 20/10 · 1h | sell | BTC-USD | 4.87 | -0.06 | rebalance down |
| 2026-10-16T06:00 | VWAP momentum · 1h | buy | XRP-USD | 3.45 | — | entry signal |
| 2026-10-16T06:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 7.82 | — | entry signal |
| 2026-10-16T06:00 | ADX DI cross · 1h | buy | ETH-USD | 11.90 | — | entry signal |
| 2026-10-16T06:00 | ADX DI cross · 1h | buy | DOGE-USD | 11.90 | — | entry signal |
| 2026-10-16T05:55 | AI bee: Bizzy | buy | XRP-USD | 7.67 | — | Jev: buy (buy p=0.61) |
| 2026-10-16T05:45 | Keltner breakout | sell | ETH-USD | 11.13 | -0.11 | stop-loss |
| 2026-10-16T05:45 | Donchian 55/20 | sell | ETH-USD | 15.58 | -0.16 | stop-loss |
| 2026-10-16T05:45 | EMA 20/50 cross | sell | ETH-USD | 15.22 | -0.15 | stop-loss |
| 2026-10-16T05:40 | Keltner breakout | sell | XRP-USD | 13.90 | -0.14 | exit signal |
| 2026-10-16T05:40 | Keltner breakout | sell | BTC-USD | 11.14 | -0.10 | stop-loss |
| 2026-10-16T05:30 | Three white soldiers | sell | BTC-USD | 21.16 | -0.18 | stop-loss |
| 2026-10-16T05:30 | Volume breakout | sell | SOL-USD | 15.95 | -0.20 | stop-loss |
| 2026-10-16T05:30 | Keltner breakout | buy | XRP-USD | 2.79 | — | rebalance up |
| 2026-10-16T05:30 | Keltner breakout | sell | SOL-USD | 11.10 | -0.14 | stop-loss |
| 2026-10-16T05:30 | Donchian 55/20 | sell | SOL-USD | 15.54 | -0.19 | stop-loss |
| 2026-10-16T05:30 | ROC + volume | sell | SOL-USD | 16.33 | -0.20 | stop-loss |
| 2026-10-16T05:30 | EMA 20/50 cross | buy | BTC-USD | 12.13 | — | rebalance up |
| 2026-10-16T05:30 | EMA 20/50 cross | sell | SOL-USD | 15.19 | -0.19 | stop-loss |
| 2026-10-16T05:20 | EMA 20/50 cross | buy | BTC-USD | 3.16 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 06:55:05.000138+00:00 -> 2026-10-16 07:05:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
