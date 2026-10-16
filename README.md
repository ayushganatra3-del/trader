# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T01:55:05.000178+00:00 · 24234 ticks

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

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 1287 decisions in 258 calls, $0.0180 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T01:55 | 0 / 2 / 3 | MSTR 15% |  |
| Breezy | 2026-10-16T01:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T01:55 | 1 / 3 / 1 | COIN 71% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 105.06 | 5.06 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.06 | 4.06 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Hold SPY | benchmark | 100.14 | 0.14 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.73 | -7.55 | 43 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.91 | -0.09 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.82 | -0.18 | 58 | 39.7 | -11.10 | -3.14 | -13.79 | 127 |
| 11 | Copy: Insider buying | copy | 99.42 | -0.58 | 20 | 45.0 | -16.49 | -2.61 | -21.97 | 76 |
| 12 | Copy: Congress Democrats (NANC) | copy | 98.75 | -1.25 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.87 | -2.13 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Hold BTC | benchmark | 97.80 | -2.20 | 0 | — | 29.63 | 3.39 | -8.68 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.69 | -2.31 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 18 | Donchian 55/20 · 1h | breakout | 97.05 | -2.95 | 36 | 16.7 | 6.62 | 0.93 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.70 | -3.30 | 86 | 24.4 | -21.45 | -5.97 | -23.30 | 155 |
| 20 | Three white soldiers · 1h | momentum | 96.30 | -3.70 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.09 | -3.91 | 106 | 32.1 | -15.04 | -5.20 | -16.66 | 302 |
| 22 | Daily: Momentum burst | daily | 95.65 | -4.35 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.45 | -4.55 | 73 | 20.5 | -11.26 | -2.05 | -15.34 | 258 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 94.03 | -5.97 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.16 | 1.12 | -9.46 | 100 |
| 26 | Parabolic SAR · 1h | trend | 93.63 | -6.37 | 93 | 22.6 | 3.05 | 0.56 | -22.05 | 279 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.31 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.28 | -6.72 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.28 | -6.72 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.20 | -6.80 | 51 | 15.7 | -1.12 | 0.07 | -24.95 | 133 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.97 | -6.19 | -11.50 | 248 |
| 32 | MACD cross · 1h | trend | 92.69 | -7.31 | 154 | 22.1 | -13.19 | -1.76 | -26.23 | 459 |
| 33 | Max aggression: 5-day momentum | meta | 92.16 | -7.84 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 34 | Bollinger breakout · 1h | breakout | 91.91 | -8.09 | 79 | 30.4 | 6.33 | 0.98 | -14.21 | 273 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.41 | -8.59 | 74 | 13.5 | -1.83 | -0.00 | -28.77 | 213 |
| 38 | Stochastic reversion · 1h | reversion | 91.28 | -8.72 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 39 | RSI momentum · 1h | momentum | 91.15 | -8.85 | 73 | 17.8 | -0.88 | 0.12 | -26.59 | 225 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 41 | Triple EMA stack · 1h | trend | 90.21 | -9.79 | 77 | 16.9 | -7.19 | -0.54 | -32.05 | 234 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -6.34 | -2.24 | -7.81 | 122 |
| 43 | MFI reversion · 1h | reversion | 89.77 | -10.23 | 191 | 30.4 | -17.00 | -2.93 | -19.95 | 142 |
| 44 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.00 | 239 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.46 | -11.54 | 73 | 35.6 | -10.21 | -1.83 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.91 | -12.09 | 165 | 18.8 | -10.49 | -0.88 | -34.70 | 316 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.32 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.16 | -12.84 | 568 | 18.5 | -2.04 | -0.17 | -14.84 | 397 |
| 51 | MACD zero-line · 1h | trend | 86.73 | -13.27 | 74 | 16.2 | -22.46 | -4.35 | -22.47 | 228 |
| 52 | VWAP momentum · 1h | momentum | 86.35 | -13.65 | 357 | 22.1 | -34.69 | -5.00 | -43.06 | 1257 |
| 53 | Heikin-Ashi · 1h | trend | 86.19 | -13.81 | 175 | 25.7 | -30.10 | -4.83 | -39.15 | 672 |
| 54 | ROC + volume · 1h | momentum | 85.81 | -14.19 | 180 | 21.7 | -8.96 | -1.09 | -25.32 | 398 |
| 55 | Donchian 20/10 · 1h | breakout | 85.59 | -14.40 | 72 | 19.4 | -0.51 | 0.14 | -20.79 | 219 |
| 56 | Three white soldiers | momentum | 85.57 | -14.43 | 202 | 19.3 | -47.72 | -19.25 | -48.85 | 609 |
| 57 | Bollinger reversion · 1h | reversion | 85.06 | -14.94 | 132 | 31.8 | -26.70 | -5.71 | -31.47 | 339 |
| 58 | EMA 9/21 cross · 1h | trend | 84.43 | -15.57 | 120 | 12.5 | -6.13 | -0.50 | -29.15 | 322 |
| 59 | Williams %R · 1h | reversion | 84.06 | -15.94 | 168 | 42.9 | -31.27 | -5.08 | -34.85 | 526 |
| 60 | CCI reversion · 1h | reversion | 83.41 | -16.59 | 143 | 42.7 | -15.27 | -1.95 | -23.38 | 429 |
| 61 | RSI(14) reversion · 1h | reversion | 83.40 | -16.60 | 61 | 23.0 | -12.31 | -2.29 | -18.95 | 169 |
| 62 | Candlestick reversal · 1h | reversion | 80.25 | -19.75 | 185 | 25.9 | -31.62 | -5.86 | -33.43 | 516 |
| 63 | RSI(14) reversion | reversion | 66.31 | -33.69 | 575 | 28.5 | -73.30 | -16.06 | -74.05 | 1558 |
| 64 | ROC + volume | momentum | 66.12 | -33.88 | 527 | 22.6 | -74.79 | -16.57 | -76.63 | 1700 |
| 65 | Volume breakout | breakout | 64.80 | -35.20 | 317 | 13.6 | -63.24 | -17.52 | -63.24 | 882 |
| 66 | Squeeze breakout | breakout | 64.49 | -35.51 | 420 | 15.0 | -62.69 | -17.21 | -63.44 | 1213 |
| 67 | Donchian 55/20 | breakout | 63.12 | -36.88 | 420 | 18.3 | -68.76 | -14.00 | -71.15 | 1277 |
| 68 | EMA 20/50 cross | trend | 61.40 | -38.60 | 437 | 19.9 | -77.31 | -14.84 | -78.49 | 1448 |
| 69 | AI bee: Boozy | ai | 58.53 | -41.47 | 281 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.99 | -42.01 | 586 | 24.6 | -72.68 | -14.85 | -72.72 | 1427 |
| 71 | Keltner breakout | breakout | 56.36 | -43.64 | 590 | 16.4 | -83.46 | -25.33 | -83.66 | 1847 |
| 72 | Supertrend | trend | 53.94 | -46.06 | 615 | 20.3 | -86.44 | -19.76 | -86.49 | 1915 |
| 73 | Ichimoku | trend | 53.14 | -46.86 | 533 | 11.8 | -81.90 | -21.94 | -81.90 | 1724 |
| 74 | AI bee: Bizzy | ai | 50.96 | -49.04 | 1043 | 9.1 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.58 | -28.12 | -98.58 | 5271 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -28.21 | -93.42 | 2585 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.53 | -23.59 | -90.61 | 2362 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.56 | -25.79 | -91.56 | 2321 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -30.50 | -97.46 | 3521 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.59 | -33.29 | -96.59 | 3586 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -24.43 | -94.47 | 2638 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -33.57 | -99.39 | 5715 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.20 | -24.44 | -91.20 | 2638 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.25 | -29.87 | -96.25 | 3552 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -37.70 | -99.73 | 6155 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -27.86 | -91.77 | 2368 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -35.24 | -97.45 | 3650 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -33.77 | -98.49 | 4679 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.54 | -30.71 | -93.54 | 2793 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -36.17 | -99.54 | 6170 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.13 | -21.43 | -86.36 | 2108 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.64 | -25.73 | -87.82 | 2112 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.97 | -30.60 | -96.03 | 3765 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.42 | -31.83 | -89.47 | 2109 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.76 | -31.60 | -95.81 | 4079 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -40.76 | -99.89 | 8220 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T01:55 | Supertrend | sell | BTC-USD | 13.42 | -0.14 | exit signal |
| 2026-10-16T01:30 | RSI(14) reversion | sell | ETH-USD | 16.46 | -0.16 | stop-loss |
| 2026-10-16T01:30 | Supertrend | sell | XRP-USD | 13.42 | -0.15 | exit signal |
| 2026-10-16T01:30 | EMA 20/50 cross | sell | BTC-USD | 15.25 | -0.14 | stop-loss |
| 2026-10-16T01:24 | AI bee: Bizzy | sell | SOL-USD | 8.09 | -0.07 | Jev: sell (sell p=0.72) after 10 min |
| 2026-10-16T01:14 | AI bee: Bizzy | buy | SOL-USD | 8.15 | — | Jev: buy (buy p=0.64) |
| 2026-10-16T01:00 | VWAP momentum · 1h | sell | XRP-USD | 6.11 | 0.01 | exit signal |
| 2026-10-16T01:00 | VWAP momentum · 1h | sell | ETH-USD | 6.17 | 0.07 | exit signal |
| 2026-10-16T01:00 | VWAP momentum · 1h | sell | BTC-USD | 6.13 | -0.01 | exit signal |
| 2026-10-16T00:45 | AI bee: Bizzy | sell | DOGE-USD | 7.34 | -0.03 | Jev: sell (sell p=0.72) after 11 min |
| 2026-10-16T00:40 | RSI(14) reversion | sell | DOGE-USD | 16.61 | -0.04 | exit signal |
| 2026-10-16T00:40 | Supertrend | buy | DOGE-USD | 13.56 | — | entry signal |
| 2026-10-16T00:40 | Supertrend | buy | BTC-USD | 13.56 | — | entry signal |
| 2026-10-16T00:40 | EMA 20/50 cross | buy | BTC-USD | 15.39 | — | entry signal |
| 2026-10-16T00:34 | AI bee: Bizzy | buy | DOGE-USD | 7.38 | — | Jev: buy (buy p=0.58) |
| 2026-10-16T00:32 | AI bee: Boozy | sell | BTC-USD | 17.07 | -0.10 | Jev: buy |
| 2026-10-16T00:25 | AI bee: Bizzy | sell | XRP-USD | 7.48 | -0.06 | Jev: sell (sell p=0.75) after 10 min |
| 2026-10-16T00:20 | RSI(14) reversion | sell | XRP-USD | 16.63 | -0.03 | exit signal |
| 2026-10-16T00:20 | Supertrend | buy | XRP-USD | 13.57 | — | entry signal |
| 2026-10-16T00:17 | AI bee: Boozy | buy | BTC-USD | 17.17 | — | Jev: buy (buy p=0.72) |
| 2026-10-16T00:15 | AI bee: Bizzy | buy | XRP-USD | 7.53 | — | Jev: buy (buy p=0.59) |
| 2026-10-16T00:03 | AI bee: Bizzy | sell | DOGE-USD | 7.43 | -0.06 | Jev: sell (sell p=0.82) after 10 min |
| 2026-10-16T00:00 | Heikin-Ashi · 1h | sell | SOL-USD | 6.08 | -0.06 | exit signal |
| 2026-10-16T00:00 | Heikin-Ashi · 1h | sell | ETH-USD | 6.11 | -0.03 | exit signal |
| 2026-10-16T00:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 6.13 | -0.02 | exit signal |
| 2026-10-16T00:00 | ADX DI cross · 1h | sell | XRP-USD | 9.39 | -0.13 | exit signal |
| 2026-10-16T00:00 | ADX DI cross · 1h | sell | BTC-USD | 9.43 | -0.09 | exit signal |
| 2026-10-15T23:53 | AI bee: Bizzy | buy | DOGE-USD | 7.49 | — | Jev: buy (buy p=0.59) |
| 2026-10-15T23:50 | RSI(14) reversion | buy | ETH-USD | 16.62 | — | entry signal |
| 2026-10-15T23:35 | EMA 20/50 cross | sell | BTC-USD | 12.35 | -0.06 | exit signal |
| 2026-10-15T23:30 | RSI(14) reversion | buy | XRP-USD | 16.65 | — | entry signal |
| 2026-10-15T23:30 | RSI(14) reversion | buy | SOL-USD | 16.65 | — | entry signal |
| 2026-10-15T23:30 | RSI(14) reversion | buy | DOGE-USD | 16.65 | — | entry signal |
| 2026-10-15T23:30 | EMA 20/50 cross | sell | ETH-USD | 12.31 | -0.00 | exit signal |
| 2026-10-15T23:20 | EMA 20/50 cross | sell | SOL-USD | 12.32 | -0.01 | exit signal |
| 2026-10-15T23:20 | EMA 20/50 cross | sell | DOGE-USD | 15.37 | -0.20 | exit signal |
| 2026-10-15T23:15 | Supertrend | sell | BTC-USD | 13.55 | -0.11 | exit signal |
| 2026-10-15T23:10 | EMA 20/50 cross | buy | DOGE-USD | 3.11 | — | rebalance up |
| 2026-10-15T23:10 | EMA 20/50 cross | sell | XRP-USD | 12.30 | -0.07 | exit signal |
| 2026-10-15T23:05 | Candlestick reversal · 1h | sell | DOGE-USD | 6.19 | 0.05 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 01:55:05.000178+00:00 -> 2026-10-16 02:05:05.000178+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
