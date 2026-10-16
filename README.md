# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T02:55:05.000170+00:00 · 24291 ticks

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

Today: 2142 decisions in 429 calls, $0.0300 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T02:55 | 1 / 4 / 0 | MSTR 15% |  |
| Breezy | 2026-10-16T02:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T02:55 | 2 / 3 / 0 | COIN 71% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 105.03 | 5.03 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.04 | 4.04 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Hold SPY | benchmark | 100.11 | 0.11 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.73 | -7.55 | 43 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.89 | -0.11 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.82 | -0.18 | 58 | 39.7 | -11.10 | -3.14 | -13.79 | 127 |
| 11 | Copy: Insider buying | copy | 99.40 | -0.60 | 20 | 45.0 | -16.49 | -2.61 | -21.97 | 76 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.72 | -1.28 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.85 | -2.15 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Hold BTC | benchmark | 97.70 | -2.30 | 0 | — | 29.70 | 3.40 | -8.68 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.66 | -2.34 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 18 | Donchian 55/20 · 1h | breakout | 97.05 | -2.95 | 36 | 16.7 | 6.62 | 0.93 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.69 | -3.31 | 86 | 24.4 | -21.42 | -5.97 | -23.24 | 155 |
| 20 | Three white soldiers · 1h | momentum | 96.30 | -3.71 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.08 | -3.92 | 106 | 32.1 | -14.44 | -4.70 | -16.07 | 297 |
| 22 | Daily: Momentum burst | daily | 95.64 | -4.36 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.37 | -4.63 | 75 | 20.0 | -11.53 | -2.10 | -15.34 | 259 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 94.00 | -6.00 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.16 | 1.12 | -9.46 | 100 |
| 26 | Parabolic SAR · 1h | trend | 93.61 | -6.39 | 93 | 22.6 | 3.19 | 0.58 | -22.05 | 277 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.31 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.27 | -6.73 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.26 | -6.74 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.19 | -6.81 | 51 | 15.7 | -0.98 | 0.09 | -24.95 | 132 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -9.75 | -5.17 | -10.29 | 246 |
| 32 | MACD cross · 1h | trend | 92.73 | -7.27 | 154 | 22.1 | -12.88 | -1.71 | -26.23 | 457 |
| 33 | Max aggression: 5-day momentum | meta | 92.13 | -7.87 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 34 | Bollinger breakout · 1h | breakout | 91.93 | -8.07 | 79 | 30.4 | 6.37 | 0.99 | -14.21 | 273 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.42 | -8.58 | 74 | 13.5 | -1.78 | 0.00 | -28.77 | 213 |
| 38 | Stochastic reversion · 1h | reversion | 91.25 | -8.75 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 39 | RSI momentum · 1h | momentum | 91.20 | -8.80 | 73 | 17.8 | -0.75 | 0.13 | -26.60 | 224 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 41 | Triple EMA stack · 1h | trend | 90.20 | -9.80 | 77 | 16.9 | -6.78 | -0.49 | -32.05 | 234 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.18 | -3.01 | -9.08 | 123 |
| 43 | MFI reversion · 1h | reversion | 89.83 | -10.17 | 191 | 30.4 | -16.93 | -2.92 | -19.96 | 142 |
| 44 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.00 | 239 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.46 | -11.54 | 73 | 35.6 | -10.19 | -1.82 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.90 | -12.10 | 165 | 18.8 | -10.36 | -0.86 | -34.70 | 316 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.32 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.16 | -12.84 | 568 | 18.5 | -3.30 | -0.38 | -14.75 | 412 |
| 51 | MACD zero-line · 1h | trend | 86.77 | -13.23 | 74 | 16.2 | -22.15 | -4.28 | -22.51 | 227 |
| 52 | VWAP momentum · 1h | momentum | 86.29 | -13.71 | 359 | 22.0 | -34.72 | -5.01 | -43.06 | 1257 |
| 53 | Heikin-Ashi · 1h | trend | 86.18 | -13.82 | 175 | 25.7 | -30.02 | -4.81 | -39.15 | 671 |
| 54 | ROC + volume · 1h | momentum | 85.87 | -14.13 | 180 | 21.7 | -8.86 | -1.07 | -25.32 | 398 |
| 55 | Donchian 20/10 · 1h | breakout | 85.66 | -14.34 | 72 | 19.4 | -0.42 | 0.15 | -20.82 | 219 |
| 56 | Three white soldiers | momentum | 85.57 | -14.43 | 202 | 19.3 | -47.72 | -19.25 | -48.85 | 609 |
| 57 | Bollinger reversion · 1h | reversion | 85.03 | -14.97 | 132 | 31.8 | -26.70 | -5.71 | -31.47 | 339 |
| 58 | EMA 9/21 cross · 1h | trend | 84.48 | -15.52 | 120 | 12.5 | -6.00 | -0.48 | -29.18 | 322 |
| 59 | Williams %R · 1h | reversion | 84.04 | -15.96 | 168 | 42.9 | -31.27 | -5.08 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.41 | -16.59 | 61 | 23.0 | -13.73 | -2.57 | -18.95 | 179 |
| 61 | CCI reversion · 1h | reversion | 83.39 | -16.61 | 143 | 42.7 | -15.04 | -1.92 | -23.38 | 428 |
| 62 | Candlestick reversal · 1h | reversion | 80.23 | -19.77 | 185 | 25.9 | -32.71 | -6.09 | -34.12 | 526 |
| 63 | RSI(14) reversion | reversion | 66.33 | -33.67 | 576 | 28.5 | -73.31 | -16.06 | -74.07 | 1558 |
| 64 | ROC + volume | momentum | 66.12 | -33.88 | 527 | 22.6 | -74.79 | -16.57 | -76.63 | 1700 |
| 65 | Volume breakout | breakout | 64.80 | -35.20 | 317 | 13.6 | -63.24 | -17.52 | -63.24 | 882 |
| 66 | Squeeze breakout | breakout | 64.40 | -35.60 | 420 | 15.0 | -62.75 | -17.25 | -63.44 | 1214 |
| 67 | Donchian 55/20 | breakout | 63.12 | -36.88 | 420 | 18.3 | -68.76 | -14.00 | -71.15 | 1277 |
| 68 | EMA 20/50 cross | trend | 61.35 | -38.65 | 437 | 19.9 | -77.25 | -14.83 | -78.49 | 1447 |
| 69 | AI bee: Boozy | ai | 58.39 | -41.61 | 282 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.89 | -42.10 | 587 | 24.5 | -72.95 | -14.98 | -72.95 | 1434 |
| 71 | Keltner breakout | breakout | 56.36 | -43.64 | 590 | 16.4 | -83.43 | -25.31 | -83.63 | 1846 |
| 72 | Supertrend | trend | 53.92 | -46.08 | 615 | 20.3 | -86.39 | -19.74 | -86.43 | 1914 |
| 73 | Ichimoku | trend | 53.10 | -46.90 | 533 | 11.8 | -81.91 | -21.97 | -81.91 | 1725 |
| 74 | AI bee: Bizzy | ai | 50.80 | -49.20 | 1046 | 9.1 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.58 | -28.14 | -98.58 | 5272 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -28.21 | -93.42 | 2584 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.50 | -23.58 | -90.57 | 2361 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.55 | -25.76 | -91.55 | 2320 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -30.63 | -97.47 | 3524 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.57 | -33.17 | -96.58 | 3584 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.42 | -24.49 | -94.42 | 2634 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -33.63 | -99.39 | 5718 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.22 | -24.50 | -91.22 | 2639 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.26 | -29.93 | -96.26 | 3554 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -37.84 | -99.73 | 6159 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -27.87 | -91.75 | 2367 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.44 | -35.26 | -97.44 | 3650 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -33.87 | -98.49 | 4681 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.55 | -30.76 | -93.55 | 2794 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -36.23 | -99.54 | 6171 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.03 | -21.34 | -86.27 | 2104 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.67 | -25.80 | -87.82 | 2113 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.96 | -30.62 | -96.02 | 3763 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.32 | -31.76 | -89.36 | 2104 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -31.58 | -95.79 | 4075 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.08 | -99.89 | 8222 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T02:54 | AI bee: Boozy | sell | ETH-USD | 16.93 | -0.15 | Jev: sell |
| 2026-10-16T02:50 | Ichimoku | buy | DOGE-USD | 13.29 | — | entry signal |
| 2026-10-16T02:40 | RSI(14) reversion | sell | SOL-USD | 16.60 | -0.05 | exit signal |
| 2026-10-16T02:40 | Squeeze breakout | buy | DOGE-USD | 16.12 | — | entry signal |
| 2026-10-16T02:40 | Supertrend | buy | XRP-USD | 13.50 | — | entry signal |
| 2026-10-16T02:39 | AI bee: Boozy | buy | ETH-USD | 17.07 | — | Jev: buy (buy p=0.72) |
| 2026-10-16T02:33 | AI bee: Bizzy | sell | SOL-USD | 7.89 | -0.06 | Jev: sell (sell p=0.74) after 10 min |
| 2026-10-16T02:26 | AI bee: Bizzy | sell | DOGE-USD | 7.60 | -0.05 | Jev: sell (sell p=0.63) after 11 min |
| 2026-10-16T02:25 | AI bee: Bizzy | sell | XRP-USD | 7.93 | -0.05 | Jev: sell (sell p=0.79) after 11 min |
| 2026-10-16T02:23 | AI bee: Bizzy | buy | SOL-USD | 7.95 | — | Jev: buy (buy p=0.62) |
| 2026-10-16T02:20 | VWAP reversion | sell | ETH-USD | 14.45 | -0.04 | exit signal |
| 2026-10-16T02:20 | EMA 20/50 cross | buy | DOGE-USD | 15.35 | — | entry signal |
| 2026-10-16T02:16 | AI bee: Bizzy | buy | DOGE-USD | 7.65 | — | Jev: buy (buy p=0.60) |
| 2026-10-16T02:14 | AI bee: Bizzy | buy | XRP-USD | 7.98 | — | Jev: buy (buy p=0.63) |
| 2026-10-16T02:05 | VWAP reversion | buy | ETH-USD | 14.50 | — | entry signal |
| 2026-10-16T02:05 | VWAP reversion | buy | BTC-USD | 14.50 | — | entry signal |
| 2026-10-16T02:00 | VWAP momentum · 1h | sell | SOL-USD | 6.10 | -0.02 | exit signal |
| 2026-10-16T02:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.11 | -0.01 | exit signal |
| 2026-10-16T02:00 | ADX DI cross · 1h | sell | SOL-USD | 9.49 | -0.16 | exit signal |
| 2026-10-16T02:00 | ADX DI cross · 1h | sell | ETH-USD | 9.48 | -0.10 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 02:55:05.000170+00:00 -> 2026-10-16 03:05:05.000170+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
