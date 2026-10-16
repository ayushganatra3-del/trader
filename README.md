# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T08:55:05.000126+00:00 · 24582 ticks

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

Today: 6487 decisions in 1298 calls, $0.0908 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T08:55 | 0 / 5 / 0 | MSTR 15% |  |
| Breezy | 2026-10-16T08:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T08:55 | 0 / 5 / 0 | COIN 71% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.72 | 4.72 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 103.73 | 3.73 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.17 | 0.74 | -7.55 | 43 |
| 8 | Hold SPY | benchmark | 99.82 | -0.18 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 9 | VWAP reversion · 1h | reversion | 99.74 | -0.26 | 58 | 39.7 | -11.19 | -3.15 | -13.80 | 126 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.60 | -0.40 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 11 | Copy: Insider buying | copy | 99.14 | -0.86 | 20 | 45.0 | -11.57 | -1.93 | -20.62 | 75 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.43 | -1.57 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.71 | -2.29 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Hold BTC | benchmark | 97.69 | -2.31 | 0 | — | 30.13 | 3.44 | -8.68 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.37 | -2.62 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.97 | -3.03 | 36 | 16.7 | 6.49 | 0.92 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.55 | -3.45 | 86 | 24.4 | -22.58 | -6.44 | -23.29 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.22 | -3.77 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.06 | -3.94 | 106 | 32.1 | -15.03 | -5.31 | -16.18 | 302 |
| 22 | Daily: Momentum burst | daily | 95.57 | -4.43 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.18 | -4.82 | 75 | 20.0 | -11.64 | -2.13 | -15.34 | 262 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.78 | 1.04 | -9.46 | 102 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 93.73 | -6.27 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 26 | Parabolic SAR · 1h | trend | 93.48 | -6.52 | 93 | 22.6 | 3.19 | 0.58 | -22.05 | 277 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.33 | 2.32 | -6.73 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.13 | -6.87 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | EMA 20/50 cross · 1h | trend | 93.09 | -6.91 | 51 | 15.7 | -6.14 | -0.65 | -23.70 | 131 |
| 30 | Daily: Bullish score | daily | 93.04 | -6.96 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.23 | -5.30 | -10.77 | 247 |
| 32 | MACD cross · 1h | trend | 92.78 | -7.22 | 154 | 22.1 | -12.23 | -1.61 | -26.23 | 456 |
| 33 | Bollinger breakout · 1h | breakout | 92.17 | -7.83 | 79 | 30.4 | 6.80 | 1.04 | -14.21 | 273 |
| 34 | Max aggression: 5-day momentum | meta | 91.86 | -8.14 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.82 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.38 | -8.62 | 74 | 13.5 | -1.57 | 0.03 | -28.77 | 214 |
| 38 | RSI momentum · 1h | momentum | 91.32 | -8.68 | 73 | 17.8 | 0.09 | 0.22 | -26.67 | 223 |
| 39 | Stochastic reversion · 1h | reversion | 90.99 | -9.01 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.67 | -3.21 | -9.57 | 122 |
| 42 | Triple EMA stack · 1h | trend | 90.07 | -9.94 | 77 | 16.9 | -7.52 | -0.58 | -32.05 | 234 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.01 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.68 | -10.32 | 194 | 30.9 | -15.65 | -2.71 | -18.75 | 141 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.23 | -11.77 | 74 | 36.5 | -10.17 | -1.82 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.81 | -12.19 | 165 | 18.8 | -10.70 | -0.90 | -34.93 | 317 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.90 | -4.32 | -21.41 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.07 | -12.93 | 568 | 18.5 | -6.97 | -1.01 | -17.66 | 410 |
| 51 | MACD zero-line · 1h | trend | 86.97 | -13.03 | 74 | 16.2 | -21.10 | -4.03 | -22.72 | 226 |
| 52 | VWAP momentum · 1h | momentum | 86.15 | -13.85 | 360 | 21.9 | -34.35 | -4.94 | -43.06 | 1259 |
| 53 | Heikin-Ashi · 1h | trend | 85.99 | -14.01 | 175 | 25.7 | -30.28 | -4.86 | -39.47 | 671 |
| 54 | Donchian 20/10 · 1h | breakout | 85.78 | -14.22 | 72 | 19.4 | -0.03 | 0.20 | -20.96 | 220 |
| 55 | ROC + volume · 1h | momentum | 85.57 | -14.43 | 184 | 22.3 | -9.09 | -1.11 | -25.32 | 398 |
| 56 | Three white soldiers | momentum | 85.20 | -14.80 | 204 | 19.1 | -47.59 | -18.75 | -48.81 | 604 |
| 57 | Bollinger reversion · 1h | reversion | 84.79 | -15.21 | 132 | 31.8 | -26.70 | -5.71 | -31.47 | 338 |
| 58 | EMA 9/21 cross · 1h | trend | 84.60 | -15.40 | 120 | 12.5 | -5.30 | -0.40 | -29.27 | 322 |
| 59 | Williams %R · 1h | reversion | 83.79 | -16.21 | 168 | 42.9 | -31.21 | -5.06 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.19 | -16.81 | 62 | 24.2 | -12.28 | -2.28 | -18.95 | 169 |
| 61 | CCI reversion · 1h | reversion | 83.16 | -16.84 | 143 | 42.7 | -15.10 | -1.93 | -23.38 | 428 |
| 62 | Candlestick reversal · 1h | reversion | 80.05 | -19.95 | 185 | 25.9 | -31.94 | -5.92 | -33.79 | 516 |
| 63 | RSI(14) reversion | reversion | 66.26 | -33.74 | 577 | 28.4 | -73.22 | -16.01 | -73.97 | 1556 |
| 64 | ROC + volume | momentum | 65.30 | -34.70 | 532 | 22.4 | -75.09 | -16.79 | -76.72 | 1703 |
| 65 | Volume breakout | breakout | 64.41 | -35.59 | 319 | 13.5 | -63.46 | -17.70 | -63.46 | 884 |
| 66 | Squeeze breakout | breakout | 63.85 | -36.15 | 424 | 14.9 | -63.05 | -17.46 | -63.68 | 1218 |
| 67 | Donchian 55/20 | breakout | 61.97 | -38.03 | 426 | 18.1 | -69.27 | -14.25 | -71.29 | 1284 |
| 68 | EMA 20/50 cross | trend | 60.95 | -39.05 | 440 | 19.8 | -77.21 | -14.83 | -78.64 | 1447 |
| 69 | AI bee: Boozy | ai | 58.02 | -41.98 | 285 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.75 | -42.25 | 591 | 24.4 | -72.50 | -14.75 | -72.54 | 1426 |
| 71 | Keltner breakout | breakout | 55.35 | -44.65 | 598 | 16.2 | -83.65 | -25.79 | -83.65 | 1851 |
| 72 | Supertrend | trend | 53.74 | -46.26 | 617 | 20.3 | -86.22 | -19.65 | -86.46 | 1912 |
| 73 | Ichimoku | trend | 52.69 | -47.31 | 538 | 11.9 | -82.03 | -22.14 | -82.03 | 1730 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -28.50 | -98.63 | 5296 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -28.54 | -93.50 | 2593 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.58 | -23.81 | -90.61 | 2366 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.70 | -25.99 | -91.70 | 2334 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -30.61 | -97.45 | 3522 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.66 | -33.97 | -96.66 | 3596 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -24.69 | -94.39 | 2627 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -33.37 | -99.37 | 5710 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.36 | -24.85 | -91.36 | 2648 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.24 | -29.76 | -96.24 | 3555 |
| 84 | AI bee: Bizzy | ai | 50.21 | -49.79 | 1060 | 9.0 | — | — | — | — |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.22 | -99.73 | 6162 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -28.09 | -91.77 | 2367 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -35.78 | -97.48 | 3659 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -33.79 | -98.45 | 4676 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.69 | -31.32 | -93.69 | 2804 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -36.11 | -99.53 | 6159 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -85.93 | -21.24 | -86.12 | 2101 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.43 | -25.59 | -87.56 | 2110 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -30.45 | -95.93 | 3755 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -31.46 | -89.30 | 2104 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.66 | -31.37 | -95.70 | 4066 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.91 | -99.89 | 8234 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T08:50 | Squeeze breakout | buy | SOL-USD | 15.98 | — | entry signal |
| 2026-10-16T08:48 | AI bee: Bizzy | sell | DOGE-USD | 7.02 | -0.04 | Jev: sell (sell p=0.62) after 10 min |
| 2026-10-16T08:40 | Donchian 55/20 | buy | SOL-USD | 15.51 | — | entry signal |
| 2026-10-16T08:40 | Ichimoku | buy | XRP-USD | 13.19 | — | entry signal |
| 2026-10-16T08:38 | AI bee: Bizzy | buy | DOGE-USD | 7.05 | — | Jev: buy (buy p=0.56) |
| 2026-10-16T08:38 | AI bee: Bizzy | sell | SOL-USD | 7.32 | -0.04 | Jev: sell (sell p=0.55) after 12 min |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 08:55:05.000126+00:00 -> 2026-10-16 09:05:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
