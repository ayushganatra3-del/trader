# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T08:26:05.000143+00:00 · 24554 ticks

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

Today: 6067 decisions in 1214 calls, $0.0850 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T08:26 | 1 / 4 / 0 | MSTR 15%, SOL-USD 15% |  |
| Breezy | 2026-10-16T08:26 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T08:26 | 3 / 2 / 0 | COIN 71% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.74 | 4.74 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 103.75 | 3.75 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.17 | 0.74 | -7.55 | 43 |
| 8 | Hold SPY | benchmark | 99.83 | -0.17 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 9 | VWAP reversion · 1h | reversion | 99.75 | -0.25 | 58 | 39.7 | -11.19 | -3.15 | -13.80 | 126 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.61 | -0.39 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 11 | Copy: Insider buying | copy | 99.16 | -0.84 | 20 | 45.0 | -11.57 | -1.93 | -20.62 | 75 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.45 | -1.55 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.72 | -2.28 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 16 | Hold BTC | benchmark | 97.57 | -2.43 | 0 | — | 30.05 | 3.43 | -8.68 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.39 | -2.61 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.98 | -3.02 | 36 | 16.7 | 6.48 | 0.92 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.55 | -3.44 | 86 | 24.4 | -22.58 | -6.44 | -23.29 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.23 | -3.77 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.06 | -3.94 | 106 | 32.1 | -15.03 | -5.31 | -16.18 | 302 |
| 22 | Daily: Momentum burst | daily | 95.58 | -4.42 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.11 | -4.89 | 75 | 20.0 | -11.81 | -2.16 | -15.34 | 262 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.68 | 1.02 | -9.46 | 103 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 93.74 | -6.26 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 26 | Parabolic SAR · 1h | trend | 93.48 | -6.51 | 93 | 22.6 | 3.19 | 0.58 | -22.05 | 277 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.33 | 2.32 | -6.73 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.14 | -6.86 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.05 | -6.95 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.00 | -7.00 | 51 | 15.7 | -6.24 | -0.66 | -23.70 | 131 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.23 | -5.30 | -10.77 | 247 |
| 32 | MACD cross · 1h | trend | 92.68 | -7.32 | 154 | 22.1 | -12.32 | -1.63 | -26.23 | 456 |
| 33 | Bollinger breakout · 1h | breakout | 92.05 | -7.95 | 79 | 30.4 | 6.65 | 1.02 | -14.21 | 273 |
| 34 | Max aggression: 5-day momentum | meta | 91.88 | -8.12 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.82 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.31 | -8.69 | 74 | 13.5 | -1.69 | 0.02 | -28.77 | 214 |
| 38 | RSI momentum · 1h | momentum | 91.22 | -8.79 | 73 | 17.8 | -0.04 | 0.21 | -26.67 | 223 |
| 39 | Stochastic reversion · 1h | reversion | 91.00 | -9.00 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.67 | -3.21 | -9.57 | 122 |
| 42 | Triple EMA stack · 1h | trend | 90.07 | -9.93 | 77 | 16.9 | -7.53 | -0.58 | -32.05 | 234 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.01 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.66 | -10.34 | 194 | 30.9 | -15.70 | -2.72 | -18.75 | 141 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.25 | -11.76 | 74 | 36.5 | -10.17 | -1.82 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.06 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.73 | -12.27 | 165 | 18.8 | -10.79 | -0.91 | -34.93 | 317 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.90 | -4.32 | -21.41 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.02 | -12.98 | 568 | 18.5 | -7.14 | -1.08 | -17.68 | 399 |
| 51 | MACD zero-line · 1h | trend | 86.82 | -13.18 | 74 | 16.2 | -21.34 | -4.09 | -22.72 | 226 |
| 52 | VWAP momentum · 1h | momentum | 86.10 | -13.90 | 360 | 21.9 | -34.39 | -4.95 | -43.06 | 1259 |
| 53 | Heikin-Ashi · 1h | trend | 85.97 | -14.04 | 175 | 25.7 | -30.32 | -4.86 | -39.47 | 671 |
| 54 | Donchian 20/10 · 1h | breakout | 85.59 | -14.41 | 72 | 19.4 | -0.26 | 0.17 | -20.96 | 220 |
| 55 | ROC + volume · 1h | momentum | 85.57 | -14.43 | 184 | 22.3 | -9.33 | -1.14 | -25.32 | 398 |
| 56 | Three white soldiers | momentum | 85.20 | -14.80 | 204 | 19.1 | -47.59 | -18.75 | -48.81 | 604 |
| 57 | Bollinger reversion · 1h | reversion | 84.80 | -15.20 | 132 | 31.8 | -26.70 | -5.71 | -31.47 | 338 |
| 58 | EMA 9/21 cross · 1h | trend | 84.48 | -15.52 | 120 | 12.5 | -5.49 | -0.42 | -29.27 | 322 |
| 59 | Williams %R · 1h | reversion | 83.81 | -16.20 | 168 | 42.9 | -31.08 | -5.04 | -34.85 | 525 |
| 60 | RSI(14) reversion · 1h | reversion | 83.20 | -16.80 | 62 | 24.2 | -12.27 | -2.28 | -18.95 | 169 |
| 61 | CCI reversion · 1h | reversion | 83.18 | -16.82 | 143 | 42.7 | -14.94 | -1.90 | -23.38 | 427 |
| 62 | Candlestick reversal · 1h | reversion | 80.05 | -19.95 | 185 | 25.9 | -31.94 | -5.92 | -33.79 | 516 |
| 63 | RSI(14) reversion | reversion | 66.26 | -33.74 | 577 | 28.4 | -73.18 | -15.99 | -73.93 | 1555 |
| 64 | ROC + volume | momentum | 65.30 | -34.70 | 532 | 22.4 | -75.09 | -16.79 | -76.72 | 1703 |
| 65 | Volume breakout | breakout | 64.41 | -35.59 | 319 | 13.5 | -63.46 | -17.70 | -63.46 | 884 |
| 66 | Squeeze breakout | breakout | 63.91 | -36.09 | 424 | 14.9 | -63.01 | -17.44 | -63.64 | 1217 |
| 67 | Donchian 55/20 | breakout | 61.97 | -38.03 | 426 | 18.1 | -69.30 | -14.27 | -71.29 | 1284 |
| 68 | EMA 20/50 cross | trend | 60.83 | -39.17 | 440 | 19.8 | -77.42 | -14.93 | -78.64 | 1452 |
| 69 | AI bee: Boozy | ai | 58.02 | -41.98 | 285 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.75 | -42.25 | 591 | 24.4 | -72.46 | -14.73 | -72.51 | 1425 |
| 71 | Keltner breakout | breakout | 55.35 | -44.65 | 598 | 16.2 | -83.65 | -25.78 | -83.65 | 1851 |
| 72 | Supertrend | trend | 53.59 | -46.41 | 617 | 20.3 | -86.26 | -19.71 | -86.46 | 1912 |
| 73 | Ichimoku | trend | 52.71 | -47.29 | 538 | 11.9 | -82.05 | -22.16 | -82.05 | 1730 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -28.53 | -98.64 | 5296 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.49 | -28.51 | -93.49 | 2591 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.61 | -23.85 | -90.61 | 2366 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.69 | -25.99 | -91.70 | 2332 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -30.71 | -97.47 | 3524 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.66 | -33.99 | -96.66 | 3594 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -24.71 | -94.39 | 2626 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -33.41 | -99.38 | 5711 |
| 82 | AI bee: Bizzy | ai | 50.26 | -49.74 | 1058 | 9.0 | — | — | — | — |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.34 | -24.82 | -91.34 | 2645 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.24 | -29.76 | -96.24 | 3555 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.24 | -99.73 | 6160 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -28.11 | -91.79 | 2368 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -35.79 | -97.48 | 3657 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -33.81 | -98.45 | 4676 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.70 | -31.33 | -93.70 | 2803 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -36.11 | -99.52 | 6159 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -85.93 | -21.24 | -86.12 | 2101 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.46 | -25.65 | -87.58 | 2111 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -30.48 | -95.93 | 3756 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.17 | -31.33 | -89.24 | 2100 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.66 | -31.39 | -95.70 | 4066 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.84 | -99.89 | 8229 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T08:26 | AI bee: Bizzy | buy | SOL-USD | 7.36 | — | Jev: buy (buy p=0.59) |
| 2026-10-16T08:20 | Squeeze breakout | sell | ETH-USD | 15.95 | -0.12 | exit signal |
| 2026-10-16T08:20 | Squeeze breakout | sell | BTC-USD | 15.90 | -0.13 | stop-loss |
| 2026-10-16T08:20 | Keltner breakout | sell | ETH-USD | 13.77 | -0.13 | exit signal |
| 2026-10-16T08:20 | ROC + volume | sell | ETH-USD | 16.24 | -0.15 | exit signal |
| 2026-10-16T08:20 | Supertrend | buy | XRP-USD | 2.67 | — | rebalance up |
| 2026-10-16T08:20 | Supertrend | sell | ETH-USD | 2.67 | -0.01 | rebalance down |
| 2026-10-16T08:19 | AI bee: Boozy | sell | ETH-USD | 16.56 | -0.13 | Jev: sell |
| 2026-10-16T08:16 | AI bee: Bizzy | sell | BTC-USD | 6.94 | -0.05 | Jev: sell (sell p=0.86) after 11 min |
| 2026-10-16T08:10 | AI bee: Bizzy | sell | XRP-USD | 7.09 | -0.04 | Jev: sell (sell p=0.85) after 11 min |
| 2026-10-16T08:05 | AI bee: Bizzy | buy | BTC-USD | 7.00 | — | Jev: buy (buy p=0.56) |
| 2026-10-16T08:05 | Squeeze breakout | buy | BTC-USD | 16.03 | — | entry signal |
| 2026-10-16T08:03 | AI bee: Boozy | buy | ETH-USD | 16.69 | — | Jev: buy (buy p=0.72) |
| 2026-10-16T08:00 | OBV trend · 1h | buy | SOL-USD | 21.95 | — | entry signal |
| 2026-10-16T08:00 | EMA 20/50 cross · 1h | buy | SOL-USD | 23.27 | — | entry signal |
| 2026-10-16T07:59 | AI bee: Bizzy | buy | XRP-USD | 7.13 | — | Jev: buy (buy p=0.57) |
| 2026-10-16T07:54 | AI bee: Bizzy | sell | SOL-USD | 7.34 | -0.05 | Jev: sell (sell p=0.77) after 10 min |
| 2026-10-16T07:44 | AI bee: Bizzy | buy | SOL-USD | 7.39 | — | Jev: buy (buy p=0.59) |
| 2026-10-16T07:35 | Squeeze breakout | sell | XRP-USD | 15.90 | -0.19 | stop-loss |
| 2026-10-16T07:35 | Keltner breakout | sell | SOL-USD | 13.77 | -0.16 | exit signal |
| 2026-10-16T07:35 | Donchian 55/20 | sell | XRP-USD | 15.42 | -0.18 | stop-loss |
| 2026-10-16T07:35 | Donchian 55/20 | sell | DOGE-USD | 15.57 | -0.17 | exit signal |
| 2026-10-16T07:35 | ROC + volume | sell | SOL-USD | 16.23 | -0.18 | exit signal |
| 2026-10-16T07:35 | Ichimoku | sell | SOL-USD | 13.17 | -0.12 | exit signal |
| 2026-10-16T07:35 | Ichimoku | sell | BTC-USD | 13.13 | -0.11 | exit signal |
| 2026-10-16T07:29 | AI bee: Boozy | sell | ETH-USD | 16.69 | -0.11 | Jev: sell |
| 2026-10-16T07:25 | AI bee: Bizzy | sell | ETH-USD | 7.13 | -0.04 | Jev: sell (sell p=0.56) after 11 min |
| 2026-10-16T07:20 | Keltner breakout | buy | ETH-USD | 13.90 | — | entry signal |
| 2026-10-16T07:20 | Donchian 55/20 | buy | ETH-USD | 15.58 | — | entry signal |
| 2026-10-16T07:20 | ROC + volume | buy | ETH-USD | 16.40 | — | entry signal |
| 2026-10-16T07:20 | Ichimoku | buy | BTC-USD | 13.24 | — | entry signal |
| 2026-10-16T07:14 | AI bee: Boozy | buy | ETH-USD | 16.80 | — | Jev: buy (buy p=0.74) |
| 2026-10-16T07:14 | AI bee: Bizzy | buy | ETH-USD | 7.17 | — | Jev: buy (buy p=0.57) |
| 2026-10-16T07:10 | Keltner breakout | sell | DOGE-USD | 11.16 | -0.08 | exit signal |
| 2026-10-16T07:10 | Ichimoku | buy | ETH-USD | 13.25 | — | entry signal |
| 2026-10-16T07:10 | Ichimoku | sell | DOGE-USD | 13.29 | 0.03 | exit signal |
| 2026-10-16T07:05 | Squeeze breakout | buy | ETH-USD | 16.07 | — | entry signal |
| 2026-10-16T07:00 | VWAP momentum · 1h | buy | BTC-USD | 3.32 | — | entry signal |
| 2026-10-16T07:00 | Ichimoku | sell | ETH-USD | 13.19 | -0.10 | exit signal |
| 2026-10-16T07:00 | EMA 20/50 cross | buy | BTC-USD | 15.24 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 08:26:05.000143+00:00 -> 2026-10-16 08:36:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
