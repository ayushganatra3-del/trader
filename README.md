# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T00:25:05.000156+00:00 · 24169 ticks

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
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 312 decisions in 63 calls, $0.0044 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T00:25 | 0 / 2 / 3 | MSTR 15% |  |
| Breezy | 2026-10-16T00:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T00:25 | 0 / 5 / 0 | BTC-USD 29% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 105.01 | 5.01 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.02 | 4.02 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.73 | -7.55 | 43 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.87 | -0.13 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.81 | -0.19 | 58 | 39.7 | -11.10 | -3.14 | -13.79 | 127 |
| 11 | Copy: Insider buying | copy | 99.39 | -0.61 | 20 | 45.0 | -16.49 | -2.61 | -21.97 | 76 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.71 | -1.29 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 97.95 | -2.06 | 0 | — | 30.08 | 3.44 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.85 | -2.15 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.65 | -2.35 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 18 | Donchian 55/20 · 1h | breakout | 97.04 | -2.96 | 36 | 16.7 | 6.62 | 0.93 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.68 | -3.32 | 86 | 24.4 | -21.45 | -5.97 | -23.30 | 155 |
| 20 | Three white soldiers · 1h | momentum | 96.29 | -3.71 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.08 | -3.92 | 106 | 32.1 | -15.82 | -5.43 | -17.70 | 300 |
| 22 | Daily: Momentum burst | daily | 95.64 | -4.36 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.47 | -4.53 | 73 | 20.5 | -11.37 | -2.07 | -15.34 | 259 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 93.99 | -6.01 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.92 | 1.07 | -9.46 | 101 |
| 26 | Parabolic SAR · 1h | trend | 93.61 | -6.39 | 93 | 22.6 | 3.02 | 0.56 | -22.05 | 281 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.31 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.27 | -6.74 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.25 | -6.75 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.18 | -6.82 | 51 | 15.7 | 2.92 | 0.53 | -25.21 | 137 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.91 | -6.16 | -11.44 | 248 |
| 32 | MACD cross · 1h | trend | 92.71 | -7.29 | 154 | 22.1 | -13.15 | -1.76 | -26.23 | 459 |
| 33 | Max aggression: 5-day momentum | meta | 92.12 | -7.88 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 34 | Bollinger breakout · 1h | breakout | 91.99 | -8.01 | 79 | 30.4 | 6.44 | 1.00 | -14.21 | 273 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.44 | -8.55 | 74 | 13.5 | -1.75 | 0.01 | -28.77 | 213 |
| 38 | Stochastic reversion · 1h | reversion | 91.24 | -8.76 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 39 | RSI momentum · 1h | momentum | 91.21 | -8.79 | 73 | 17.8 | -0.52 | 0.16 | -26.54 | 225 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 41 | Triple EMA stack · 1h | trend | 90.19 | -9.81 | 77 | 16.9 | -7.68 | -0.59 | -32.05 | 234 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -6.19 | -2.18 | -7.66 | 122 |
| 43 | MFI reversion · 1h | reversion | 89.79 | -10.21 | 191 | 30.4 | -16.84 | -2.90 | -19.98 | 143 |
| 44 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.26 | -6.88 | -25.00 | 240 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.41 | -11.59 | 73 | 35.6 | -10.22 | -1.83 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.90 | -12.10 | 165 | 18.8 | -10.44 | -0.87 | -34.70 | 315 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.32 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.16 | -12.84 | 568 | 18.5 | -3.52 | -0.42 | -15.14 | 414 |
| 51 | MACD zero-line · 1h | trend | 86.84 | -13.16 | 74 | 16.2 | -22.27 | -4.30 | -22.40 | 228 |
| 52 | VWAP momentum · 1h | momentum | 86.37 | -13.63 | 354 | 21.8 | -34.56 | -4.98 | -43.06 | 1256 |
| 53 | Heikin-Ashi · 1h | trend | 86.17 | -13.83 | 175 | 25.7 | -30.11 | -4.83 | -39.15 | 672 |
| 54 | ROC + volume · 1h | momentum | 85.92 | -14.08 | 180 | 21.7 | -8.78 | -1.06 | -25.32 | 399 |
| 55 | Donchian 20/10 · 1h | breakout | 85.73 | -14.27 | 72 | 19.4 | -0.35 | 0.16 | -20.75 | 219 |
| 56 | Three white soldiers | momentum | 85.57 | -14.43 | 202 | 19.3 | -47.72 | -19.25 | -48.85 | 609 |
| 57 | Bollinger reversion · 1h | reversion | 85.02 | -14.98 | 132 | 31.8 | -26.70 | -5.71 | -31.47 | 339 |
| 58 | EMA 9/21 cross · 1h | trend | 84.52 | -15.48 | 120 | 12.5 | -5.97 | -0.48 | -29.15 | 323 |
| 59 | Williams %R · 1h | reversion | 84.03 | -15.97 | 168 | 42.9 | -31.28 | -5.08 | -34.85 | 526 |
| 60 | CCI reversion · 1h | reversion | 83.38 | -16.62 | 143 | 42.7 | -15.27 | -1.95 | -23.38 | 429 |
| 61 | RSI(14) reversion · 1h | reversion | 83.35 | -16.65 | 61 | 23.0 | -12.53 | -2.33 | -18.95 | 172 |
| 62 | Candlestick reversal · 1h | reversion | 80.23 | -19.77 | 185 | 25.9 | -32.02 | -5.96 | -33.45 | 520 |
| 63 | RSI(14) reversion | reversion | 66.43 | -33.56 | 573 | 28.6 | -73.27 | -16.03 | -74.08 | 1559 |
| 64 | ROC + volume | momentum | 66.12 | -33.88 | 527 | 22.6 | -74.94 | -16.67 | -76.65 | 1704 |
| 65 | Volume breakout | breakout | 64.80 | -35.20 | 317 | 13.6 | -63.32 | -17.55 | -63.32 | 885 |
| 66 | Squeeze breakout | breakout | 64.49 | -35.51 | 420 | 15.0 | -62.88 | -17.30 | -63.44 | 1217 |
| 67 | Donchian 55/20 | breakout | 63.12 | -36.88 | 420 | 18.3 | -68.76 | -14.00 | -71.15 | 1277 |
| 68 | EMA 20/50 cross | trend | 61.54 | -38.46 | 436 | 20.0 | -77.22 | -14.78 | -78.49 | 1446 |
| 69 | AI bee: Boozy | ai | 58.55 | -41.45 | 280 | 5.4 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.99 | -42.01 | 586 | 24.6 | -72.50 | -14.76 | -72.55 | 1425 |
| 71 | Keltner breakout | breakout | 56.36 | -43.64 | 590 | 16.4 | -83.56 | -25.39 | -83.76 | 1851 |
| 72 | Supertrend | trend | 54.21 | -45.79 | 613 | 20.4 | -86.37 | -19.66 | -86.49 | 1913 |
| 73 | Ichimoku | trend | 53.14 | -46.86 | 533 | 11.8 | -81.99 | -22.02 | -81.99 | 1727 |
| 74 | AI bee: Bizzy | ai | 51.06 | -48.94 | 1041 | 9.1 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.56 | -27.85 | -98.59 | 5279 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.48 | -28.24 | -93.48 | 2589 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.56 | -23.57 | -90.66 | 2364 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.55 | -25.72 | -91.55 | 2321 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -30.30 | -97.45 | 3517 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.60 | -33.23 | -96.60 | 3586 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -24.08 | -94.44 | 2635 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -33.39 | -99.39 | 5714 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.26 | -24.48 | -91.26 | 2642 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.25 | -29.80 | -96.25 | 3550 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -37.58 | -99.73 | 6158 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.73 | -27.72 | -91.78 | 2366 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.43 | -34.98 | -97.43 | 3648 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -33.68 | -98.49 | 4679 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.53 | -30.57 | -93.53 | 2794 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -35.97 | -99.54 | 6166 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.10 | -21.38 | -86.36 | 2108 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.67 | -25.75 | -87.86 | 2119 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -30.48 | -96.03 | 3761 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.41 | -31.79 | -89.47 | 2109 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -31.47 | -95.81 | 4075 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -40.76 | -99.89 | 8225 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-15T23:05 | Supertrend | sell | DOGE-USD | 10.87 | -0.06 | exit signal |
| 2026-10-15T23:00 | ADX DI cross · 1h | buy | BTC-USD | 9.52 | — | entry signal |
| 2026-10-15T23:00 | Ichimoku | sell | SOL-USD | 13.26 | -0.09 | exit signal |
| 2026-10-15T22:50 | Ichimoku | sell | ETH-USD | 13.26 | -0.08 | exit signal |
| 2026-10-15T22:36 | AI bee: Bizzy | sell | BTC-USD | 7.73 | -0.06 | Jev: sell (sell p=0.73) after 11 min |
| 2026-10-15T22:25 | AI bee: Bizzy | buy | BTC-USD | 7.79 | — | Jev: buy (buy p=0.61) |
| 2026-10-15T22:20 | Three white soldiers | sell | BTC-USD | 21.29 | -0.14 | exit signal |
| 2026-10-15T22:18 | AI bee: Boozy | sell | ETH-USD | 17.17 | -0.13 | Jev: sell |
| 2026-10-15T22:07 | AI bee: Bizzy | sell | SOL-USD | 7.25 | -0.04 | Jev: sell (sell p=0.59) after 10 min |
| 2026-10-15T22:02 | AI bee: Boozy | buy | ETH-USD | 17.30 | — | Jev: buy (buy p=0.71) |
| 2026-10-15T22:00 | Heikin-Ashi · 1h | sell | XRP-USD | 6.11 | -0.03 | exit signal |
| 2026-10-15T22:00 | Three white soldiers | buy | BTC-USD | 21.43 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 00:25:05.000156+00:00 -> 2026-10-16 00:35:05.000156+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
