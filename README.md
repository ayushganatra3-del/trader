# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T05:55:05.000183+00:00 · 24435 ticks

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

Today: 4282 decisions in 857 calls, $0.0600 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T05:55 | 2 / 3 / 0 | XRP-USD 15%, MSTR 15% |  |
| Breezy | 2026-10-16T05:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T05:55 | 5 / 0 / 0 | COIN 71% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.79 | 4.79 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 103.80 | 3.80 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.73 | -7.55 | 43 |
| 8 | Hold SPY | benchmark | 99.88 | -0.12 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 9 | VWAP reversion · 1h | reversion | 99.76 | -0.24 | 58 | 39.7 | -11.10 | -3.14 | -13.79 | 127 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.66 | -0.34 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 11 | Copy: Insider buying | copy | 99.20 | -0.80 | 20 | 45.0 | -11.57 | -1.93 | -20.62 | 75 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.50 | -1.50 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.74 | -2.26 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Hold BTC | benchmark | 97.66 | -2.34 | 0 | — | 29.82 | 3.41 | -8.68 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.44 | -2.56 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.99 | -3.01 | 36 | 16.7 | 6.62 | 0.93 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.58 | -3.42 | 86 | 24.4 | -22.58 | -6.44 | -23.29 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.24 | -3.76 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.07 | -3.93 | 106 | 32.1 | -14.90 | -5.15 | -16.52 | 302 |
| 22 | Daily: Momentum burst | daily | 95.59 | -4.41 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.24 | -4.76 | 75 | 20.0 | -11.35 | -2.07 | -15.34 | 258 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 93.79 | -6.21 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.16 | 1.12 | -9.46 | 100 |
| 26 | Parabolic SAR · 1h | trend | 93.51 | -6.49 | 93 | 22.6 | 3.19 | 0.58 | -22.05 | 277 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.31 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.16 | -6.84 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | EMA 20/50 cross · 1h | trend | 93.09 | -6.91 | 51 | 15.7 | -1.01 | 0.08 | -24.95 | 133 |
| 30 | Daily: Bullish score | daily | 93.09 | -6.91 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.97 | -6.19 | -11.50 | 248 |
| 32 | MACD cross · 1h | trend | 92.73 | -7.27 | 154 | 22.1 | -12.44 | -1.65 | -26.23 | 456 |
| 33 | Bollinger breakout · 1h | breakout | 92.01 | -7.99 | 79 | 30.4 | 6.59 | 1.02 | -14.21 | 273 |
| 34 | Max aggression: 5-day momentum | meta | 91.92 | -8.08 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.33 | -8.67 | 74 | 13.5 | -1.66 | 0.02 | -28.77 | 213 |
| 38 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 73 | 17.8 | -0.88 | 0.12 | -26.67 | 225 |
| 39 | Stochastic reversion · 1h | reversion | 91.04 | -8.96 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.18 | -3.01 | -9.08 | 123 |
| 42 | Triple EMA stack · 1h | trend | 90.09 | -9.90 | 77 | 16.9 | -7.26 | -0.55 | -32.05 | 234 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.00 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.66 | -10.34 | 194 | 30.9 | -16.51 | -2.83 | -19.82 | 140 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.29 | -11.71 | 74 | 36.5 | -10.17 | -1.82 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.81 | -12.19 | 165 | 18.8 | -11.05 | -0.94 | -34.70 | 318 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.32 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.07 | -12.93 | 568 | 18.5 | -3.76 | -0.48 | -15.90 | 402 |
| 51 | MACD zero-line · 1h | trend | 86.80 | -13.20 | 74 | 16.2 | -22.04 | -4.25 | -22.72 | 229 |
| 52 | VWAP momentum · 1h | momentum | 86.16 | -13.84 | 360 | 21.9 | -34.50 | -4.97 | -43.06 | 1258 |
| 53 | Heikin-Ashi · 1h | trend | 86.05 | -13.95 | 175 | 25.7 | -29.90 | -4.79 | -39.15 | 670 |
| 54 | Donchian 20/10 · 1h | breakout | 85.73 | -14.27 | 72 | 19.4 | -0.17 | 0.18 | -20.97 | 219 |
| 55 | ROC + volume · 1h | momentum | 85.58 | -14.41 | 184 | 22.3 | -9.10 | -1.11 | -25.32 | 398 |
| 56 | Three white soldiers | momentum | 85.20 | -14.80 | 204 | 19.1 | -47.86 | -19.43 | -48.77 | 610 |
| 57 | Bollinger reversion · 1h | reversion | 84.84 | -15.16 | 132 | 31.8 | -26.70 | -5.71 | -31.47 | 339 |
| 58 | EMA 9/21 cross · 1h | trend | 84.47 | -15.53 | 120 | 12.5 | -5.67 | -0.44 | -29.27 | 323 |
| 59 | Williams %R · 1h | reversion | 83.85 | -16.15 | 168 | 42.9 | -31.25 | -5.07 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.24 | -16.76 | 62 | 24.2 | -12.28 | -2.28 | -18.95 | 169 |
| 61 | CCI reversion · 1h | reversion | 83.22 | -16.79 | 143 | 42.7 | -15.23 | -1.94 | -23.38 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 80.08 | -19.92 | 185 | 25.9 | -31.66 | -5.87 | -33.43 | 517 |
| 63 | RSI(14) reversion | reversion | 66.26 | -33.74 | 577 | 28.4 | -73.27 | -16.04 | -74.02 | 1558 |
| 64 | ROC + volume | momentum | 65.79 | -34.21 | 528 | 22.5 | -74.91 | -16.67 | -76.63 | 1703 |
| 65 | Volume breakout | breakout | 64.41 | -35.59 | 319 | 13.5 | -63.46 | -17.70 | -63.46 | 884 |
| 66 | Squeeze breakout | breakout | 64.35 | -35.65 | 421 | 15.0 | -62.78 | -17.27 | -63.44 | 1214 |
| 67 | Donchian 55/20 | breakout | 62.47 | -37.53 | 423 | 18.2 | -69.08 | -14.17 | -71.15 | 1282 |
| 68 | EMA 20/50 cross | trend | 61.04 | -38.96 | 439 | 19.8 | -77.48 | -14.94 | -78.61 | 1454 |
| 69 | AI bee: Boozy | ai | 58.26 | -41.74 | 283 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.75 | -42.25 | 591 | 24.4 | -72.70 | -14.88 | -72.75 | 1432 |
| 71 | Keltner breakout | breakout | 55.68 | -44.32 | 595 | 16.3 | -83.62 | -25.71 | -83.63 | 1851 |
| 72 | Supertrend | trend | 53.63 | -46.37 | 617 | 20.3 | -86.37 | -19.79 | -86.44 | 1916 |
| 73 | Ichimoku | trend | 53.15 | -46.85 | 534 | 11.8 | -81.90 | -21.95 | -81.95 | 1726 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -28.46 | -98.63 | 5293 |
| 75 | AI bee: Bizzy | ai | 50.60 | -49.40 | 1050 | 9.0 | — | — | — | — |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -28.41 | -93.48 | 2590 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.58 | -23.78 | -90.59 | 2365 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.57 | -25.80 | -91.57 | 2325 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -30.72 | -97.48 | 3526 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.61 | -33.52 | -96.61 | 3592 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.43 | -24.65 | -94.43 | 2632 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -33.50 | -99.38 | 5710 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.27 | -24.65 | -91.28 | 2643 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.26 | -29.93 | -96.26 | 3556 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.04 | -99.73 | 6158 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -28.19 | -91.84 | 2372 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -35.53 | -97.46 | 3654 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -33.94 | -98.47 | 4681 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.62 | -31.09 | -93.63 | 2799 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -36.24 | -99.53 | 6166 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -85.93 | -21.24 | -86.12 | 2101 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.59 | -25.69 | -87.74 | 2109 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -30.59 | -95.97 | 3760 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.29 | -31.68 | -89.32 | 2102 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -31.47 | -95.75 | 4070 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.74 | -99.89 | 8229 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-16T05:20 | EMA 20/50 cross | sell | DOGE-USD | 3.16 | 0.00 | rebalance down |
| 2026-10-16T05:18 | AI bee: Boozy | sell | ETH-USD | 16.80 | -0.13 | Jev: sell |
| 2026-10-16T05:18 | AI bee: Bizzy | sell | DOGE-USD | 7.37 | -0.06 | Jev: sell (sell p=0.76) after 11 min |
| 2026-10-16T05:17 | AI bee: Bizzy | sell | SOL-USD | 7.61 | -0.01 | Jev: sell (sell p=0.50) after 18 min |
| 2026-10-16T05:15 | Supertrend | buy | XRP-USD | 2.68 | — | rebalance up |
| 2026-10-16T05:15 | Supertrend | sell | DOGE-USD | 2.68 | -0.00 | rebalance down |
| 2026-10-16T05:10 | ROC + volume | buy | ETH-USD | 16.49 | — | entry signal |
| 2026-10-16T05:10 | EMA 20/50 cross | buy | XRP-USD | 15.31 | — | entry signal |
| 2026-10-16T05:07 | AI bee: Bizzy | buy | DOGE-USD | 7.43 | — | Jev: buy (buy p=0.59) |
| 2026-10-16T05:05 | VWAP reversion | sell | BTC-USD | 14.43 | -0.02 | exit signal |
| 2026-10-16T05:05 | Three white soldiers | buy | BTC-USD | 21.35 | — | entry signal |
| 2026-10-16T05:05 | Volume breakout | buy | SOL-USD | 16.15 | — | entry signal |
| 2026-10-16T05:05 | Keltner breakout | buy | XRP-USD | 11.24 | — | entry signal |
| 2026-10-16T05:05 | Keltner breakout | buy | SOL-USD | 11.24 | — | entry signal |
| 2026-10-16T05:05 | Keltner breakout | buy | ETH-USD | 11.24 | — | entry signal |
| 2026-10-16T05:05 | Keltner breakout | buy | DOGE-USD | 11.24 | — | entry signal |
| 2026-10-16T05:05 | Keltner breakout | buy | BTC-USD | 11.24 | — | entry signal |
| 2026-10-16T05:05 | Donchian 55/20 | buy | XRP-USD | 15.74 | — | entry signal |
| 2026-10-16T05:05 | Donchian 55/20 | buy | SOL-USD | 15.74 | — | entry signal |
| 2026-10-16T05:05 | Donchian 55/20 | buy | ETH-USD | 15.74 | — | entry signal |
| 2026-10-16T05:05 | Donchian 55/20 | buy | DOGE-USD | 15.74 | — | entry signal |
| 2026-10-16T05:05 | ROC + volume | buy | SOL-USD | 16.53 | — | entry signal |
| 2026-10-16T05:05 | ROC + volume | buy | DOGE-USD | 16.53 | — | entry signal |
| 2026-10-16T05:05 | Supertrend | buy | XRP-USD | 2.77 | — | entry signal |
| 2026-10-16T05:05 | Supertrend | sell | SOL-USD | 2.71 | 0.00 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 05:55:05.000183+00:00 -> 2026-10-16 06:05:05.000183+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
