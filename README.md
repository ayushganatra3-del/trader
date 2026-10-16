# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T01:25:05.000114+00:00 · 24213 ticks

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

Today: 972 decisions in 195 calls, $0.0136 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T01:25 | 0 / 1 / 4 | MSTR 15% |  |
| Breezy | 2026-10-16T01:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T01:25 | 0 / 3 / 2 | COIN 71% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 105.05 | 5.05 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.06 | 4.06 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Hold SPY | benchmark | 100.13 | 0.13 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.73 | -7.55 | 43 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.91 | -0.09 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.82 | -0.18 | 58 | 39.7 | -11.10 | -3.14 | -13.79 | 127 |
| 11 | Copy: Insider buying | copy | 99.42 | -0.58 | 20 | 45.0 | -16.49 | -2.61 | -21.97 | 76 |
| 12 | Copy: Congress Democrats (NANC) | copy | 98.74 | -1.26 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 14 | Hold BTC | benchmark | 97.97 | -2.03 | 0 | — | 29.94 | 3.42 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.86 | -2.14 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.68 | -2.32 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 18 | Donchian 55/20 · 1h | breakout | 97.05 | -2.95 | 36 | 16.7 | 6.62 | 0.93 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.70 | -3.30 | 86 | 24.4 | -21.45 | -5.97 | -23.30 | 155 |
| 20 | Three white soldiers · 1h | momentum | 96.30 | -3.70 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.09 | -3.91 | 106 | 32.1 | -15.04 | -5.20 | -16.66 | 302 |
| 22 | Daily: Momentum burst | daily | 95.64 | -4.36 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.48 | -4.52 | 73 | 20.5 | -11.23 | -2.04 | -15.34 | 258 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 94.02 | -5.98 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.92 | 1.07 | -9.46 | 101 |
| 26 | Parabolic SAR · 1h | trend | 93.62 | -6.38 | 93 | 22.6 | 3.05 | 0.56 | -22.05 | 279 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.31 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.28 | -6.72 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.27 | -6.73 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.19 | -6.81 | 51 | 15.7 | -1.12 | 0.07 | -24.95 | 133 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.91 | -6.16 | -11.44 | 248 |
| 32 | MACD cross · 1h | trend | 92.74 | -7.26 | 154 | 22.1 | -13.15 | -1.76 | -26.23 | 459 |
| 33 | Max aggression: 5-day momentum | meta | 92.15 | -7.85 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 34 | Bollinger breakout · 1h | breakout | 92.00 | -8.00 | 79 | 30.4 | 6.44 | 1.00 | -14.21 | 273 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.45 | -8.55 | 74 | 13.5 | -1.78 | 0.00 | -28.77 | 213 |
| 38 | Stochastic reversion · 1h | reversion | 91.27 | -8.73 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 39 | RSI momentum · 1h | momentum | 91.20 | -8.80 | 73 | 17.8 | -0.82 | 0.12 | -26.54 | 225 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 41 | Triple EMA stack · 1h | trend | 90.21 | -9.79 | 77 | 16.9 | -7.19 | -0.54 | -32.05 | 234 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -6.19 | -2.18 | -7.66 | 122 |
| 43 | MFI reversion · 1h | reversion | 89.81 | -10.19 | 191 | 30.4 | -16.96 | -2.92 | -19.96 | 142 |
| 44 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.00 | 239 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.47 | -11.53 | 73 | 35.6 | -10.20 | -1.83 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.91 | -12.09 | 165 | 18.8 | -10.40 | -0.87 | -34.70 | 315 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.32 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.18 | -12.82 | 568 | 18.5 | -1.98 | -0.16 | -15.77 | 406 |
| 51 | MACD zero-line · 1h | trend | 86.83 | -13.17 | 74 | 16.2 | -22.35 | -4.32 | -22.40 | 228 |
| 52 | VWAP momentum · 1h | momentum | 86.37 | -13.63 | 357 | 22.1 | -34.57 | -4.98 | -43.06 | 1256 |
| 53 | Heikin-Ashi · 1h | trend | 86.19 | -13.81 | 175 | 25.7 | -30.11 | -4.83 | -39.15 | 672 |
| 54 | ROC + volume · 1h | momentum | 85.89 | -14.11 | 180 | 21.7 | -8.85 | -1.07 | -25.32 | 398 |
| 55 | Donchian 20/10 · 1h | breakout | 85.69 | -14.31 | 72 | 19.4 | -0.42 | 0.15 | -20.75 | 219 |
| 56 | Three white soldiers | momentum | 85.57 | -14.43 | 202 | 19.3 | -47.72 | -19.25 | -48.85 | 609 |
| 57 | Bollinger reversion · 1h | reversion | 85.05 | -14.95 | 132 | 31.8 | -26.70 | -5.71 | -31.47 | 339 |
| 58 | EMA 9/21 cross · 1h | trend | 84.50 | -15.50 | 120 | 12.5 | -6.04 | -0.49 | -29.15 | 322 |
| 59 | Williams %R · 1h | reversion | 84.05 | -15.95 | 168 | 42.9 | -31.27 | -5.08 | -34.85 | 526 |
| 60 | CCI reversion · 1h | reversion | 83.41 | -16.59 | 143 | 42.7 | -15.27 | -1.95 | -23.38 | 429 |
| 61 | RSI(14) reversion · 1h | reversion | 83.40 | -16.59 | 61 | 23.0 | -12.31 | -2.28 | -18.95 | 169 |
| 62 | Candlestick reversal · 1h | reversion | 80.24 | -19.76 | 185 | 25.9 | -31.62 | -5.86 | -33.43 | 516 |
| 63 | RSI(14) reversion | reversion | 66.43 | -33.57 | 574 | 28.6 | -73.42 | -16.11 | -74.22 | 1562 |
| 64 | ROC + volume | momentum | 66.12 | -33.88 | 527 | 22.6 | -74.92 | -16.66 | -76.64 | 1703 |
| 65 | Volume breakout | breakout | 64.80 | -35.20 | 317 | 13.6 | -63.31 | -17.55 | -63.31 | 884 |
| 66 | Squeeze breakout | breakout | 64.49 | -35.51 | 420 | 15.0 | -62.70 | -17.21 | -63.44 | 1213 |
| 67 | Donchian 55/20 | breakout | 63.12 | -36.88 | 420 | 18.3 | -68.76 | -14.00 | -71.15 | 1277 |
| 68 | EMA 20/50 cross | trend | 61.46 | -38.54 | 436 | 20.0 | -77.25 | -14.80 | -78.49 | 1447 |
| 69 | AI bee: Boozy | ai | 58.53 | -41.47 | 281 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.99 | -42.01 | 586 | 24.6 | -72.56 | -14.79 | -72.61 | 1426 |
| 71 | Keltner breakout | breakout | 56.36 | -43.64 | 590 | 16.4 | -83.53 | -25.37 | -83.72 | 1849 |
| 72 | Supertrend | trend | 54.07 | -45.93 | 613 | 20.4 | -86.40 | -19.71 | -86.49 | 1915 |
| 73 | Ichimoku | trend | 53.14 | -46.86 | 533 | 11.8 | -81.90 | -21.94 | -81.90 | 1724 |
| 74 | AI bee: Bizzy | ai | 50.96 | -49.04 | 1043 | 9.1 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.58 | -28.10 | -98.58 | 5283 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -28.17 | -93.42 | 2584 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.52 | -23.56 | -90.61 | 2362 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.57 | -25.81 | -91.57 | 2322 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -30.50 | -97.46 | 3521 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.58 | -33.20 | -96.58 | 3584 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -24.43 | -94.47 | 2638 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -33.52 | -99.39 | 5717 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.25 | -24.49 | -91.25 | 2641 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.24 | -29.77 | -96.24 | 3549 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -37.65 | -99.73 | 6158 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -27.82 | -91.78 | 2368 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.44 | -35.19 | -97.44 | 3650 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -33.73 | -98.49 | 4679 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.54 | -30.67 | -93.54 | 2793 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -36.04 | -99.54 | 6165 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.10 | -21.39 | -86.36 | 2108 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.65 | -25.75 | -87.82 | 2116 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -30.47 | -96.03 | 3761 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.47 | -31.85 | -89.52 | 2112 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -31.47 | -95.81 | 4075 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -40.76 | -99.89 | 8220 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-15T23:05 | Donchian 55/20 | sell | ETH-USD | 15.81 | -0.04 | exit signal |
| 2026-10-15T23:05 | Donchian 55/20 | sell | DOGE-USD | 15.76 | -0.15 | exit signal |
| 2026-10-15T23:05 | Supertrend | sell | SOL-USD | 13.60 | -0.14 | exit signal |
| 2026-10-15T23:05 | Supertrend | sell | ETH-USD | 10.91 | 0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 01:25:05.000114+00:00 -> 2026-10-16 01:35:05.000114+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
