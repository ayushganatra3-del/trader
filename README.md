# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T05:25:05.000154+00:00 · 24412 ticks

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

Today: 3952 decisions in 791 calls, $0.0554 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T05:24 | 2 / 2 / 1 | MSTR 15% | HTTP 529: HTTP 529: {"detail":{"error_type":"system_overloaded","message":"We are currently experiencing high traffic and cannot process your request. Please try again later."}} |
| Breezy | 2026-10-16T05:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T05:25 | 1 / 4 / 0 | COIN 71% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.81 | 4.81 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 103.82 | 3.82 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.73 | -7.55 | 43 |
| 8 | Hold SPY | benchmark | 99.90 | -0.10 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 9 | VWAP reversion · 1h | reversion | 99.76 | -0.23 | 58 | 39.7 | -11.10 | -3.14 | -13.79 | 127 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.68 | -0.32 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 11 | Copy: Insider buying | copy | 99.22 | -0.79 | 20 | 45.0 | -11.57 | -1.93 | -20.62 | 75 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.51 | -1.49 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.75 | -2.25 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Hold BTC | benchmark | 97.74 | -2.26 | 0 | — | 30.06 | 3.44 | -8.68 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.45 | -2.55 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.99 | -3.00 | 36 | 16.7 | 6.62 | 0.93 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.59 | -3.41 | 86 | 24.4 | -22.58 | -6.44 | -23.29 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.24 | -3.76 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.07 | -3.93 | 106 | 32.1 | -15.28 | -5.24 | -16.89 | 300 |
| 22 | Daily: Momentum burst | daily | 95.59 | -4.41 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.25 | -4.75 | 75 | 20.0 | -11.54 | -2.11 | -15.34 | 259 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 93.80 | -6.20 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.68 | 1.02 | -9.46 | 103 |
| 26 | Parabolic SAR · 1h | trend | 93.52 | -6.49 | 93 | 22.6 | 3.19 | 0.58 | -22.05 | 277 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.31 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.17 | -6.83 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.10 | -6.90 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.10 | -6.90 | 51 | 15.7 | -1.01 | 0.08 | -24.95 | 133 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -9.73 | -5.16 | -10.27 | 247 |
| 32 | MACD cross · 1h | trend | 92.75 | -7.25 | 154 | 22.1 | -12.45 | -1.65 | -26.23 | 456 |
| 33 | Bollinger breakout · 1h | breakout | 92.05 | -7.95 | 79 | 30.4 | 6.62 | 1.02 | -14.21 | 273 |
| 34 | Max aggression: 5-day momentum | meta | 91.94 | -8.06 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.82 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.35 | -8.65 | 74 | 13.5 | -1.65 | 0.02 | -28.77 | 213 |
| 38 | RSI momentum · 1h | momentum | 91.20 | -8.79 | 73 | 17.8 | -0.87 | 0.12 | -26.67 | 225 |
| 39 | Stochastic reversion · 1h | reversion | 91.06 | -8.94 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.18 | -3.01 | -9.08 | 123 |
| 42 | Triple EMA stack · 1h | trend | 90.10 | -9.90 | 77 | 16.9 | -7.26 | -0.55 | -32.05 | 234 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.00 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.68 | -10.32 | 194 | 30.9 | -16.74 | -2.88 | -19.82 | 141 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.30 | -11.70 | 74 | 36.5 | -10.17 | -1.82 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -13.80 | -1.88 | -29.15 | 210 |
| 48 | OBV trend · 1h | momentum | 87.82 | -12.18 | 165 | 18.8 | -11.06 | -0.94 | -34.70 | 318 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.32 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.09 | -12.91 | 568 | 18.5 | -3.80 | -0.49 | -14.84 | 403 |
| 51 | MACD zero-line · 1h | trend | 86.84 | -13.16 | 74 | 16.2 | -22.10 | -4.26 | -22.75 | 229 |
| 52 | VWAP momentum · 1h | momentum | 86.17 | -13.83 | 360 | 21.9 | -34.49 | -4.97 | -43.06 | 1258 |
| 53 | Heikin-Ashi · 1h | trend | 86.06 | -13.94 | 175 | 25.7 | -29.91 | -4.79 | -39.15 | 670 |
| 54 | Donchian 20/10 · 1h | breakout | 85.76 | -14.24 | 72 | 19.4 | -0.16 | 0.18 | -20.97 | 219 |
| 55 | ROC + volume · 1h | momentum | 85.59 | -14.41 | 184 | 22.3 | -9.33 | -1.14 | -25.32 | 398 |
| 56 | Three white soldiers | momentum | 85.29 | -14.71 | 203 | 19.2 | -47.81 | -19.38 | -48.77 | 610 |
| 57 | Bollinger reversion · 1h | reversion | 84.85 | -15.14 | 132 | 31.8 | -26.74 | -5.72 | -31.47 | 339 |
| 58 | EMA 9/21 cross · 1h | trend | 84.50 | -15.50 | 120 | 12.5 | -5.67 | -0.44 | -29.27 | 323 |
| 59 | Williams %R · 1h | reversion | 83.86 | -16.14 | 168 | 42.9 | -31.28 | -5.08 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.25 | -16.75 | 62 | 24.2 | -12.27 | -2.28 | -18.95 | 169 |
| 61 | CCI reversion · 1h | reversion | 83.23 | -16.77 | 143 | 42.7 | -15.04 | -1.92 | -23.38 | 428 |
| 62 | Candlestick reversal · 1h | reversion | 80.09 | -19.91 | 185 | 25.9 | -31.64 | -5.87 | -33.43 | 517 |
| 63 | RSI(14) reversion | reversion | 66.26 | -33.74 | 577 | 28.4 | -73.77 | -16.26 | -74.51 | 1568 |
| 64 | ROC + volume | momentum | 65.87 | -34.13 | 527 | 22.6 | -74.88 | -16.65 | -76.63 | 1703 |
| 65 | Volume breakout | breakout | 64.50 | -35.51 | 318 | 13.5 | -63.41 | -17.66 | -63.41 | 884 |
| 66 | Squeeze breakout | breakout | 64.35 | -35.65 | 421 | 15.0 | -62.77 | -17.27 | -63.44 | 1214 |
| 67 | Donchian 55/20 | breakout | 62.61 | -37.39 | 421 | 18.3 | -69.01 | -14.14 | -71.15 | 1282 |
| 68 | EMA 20/50 cross | trend | 61.22 | -38.78 | 437 | 19.9 | -77.27 | -14.85 | -78.53 | 1450 |
| 69 | AI bee: Boozy | ai | 58.26 | -41.74 | 283 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.75 | -42.25 | 591 | 24.4 | -72.82 | -14.94 | -72.87 | 1435 |
| 71 | Keltner breakout | breakout | 55.92 | -44.08 | 591 | 16.4 | -83.54 | -25.57 | -83.61 | 1851 |
| 72 | Supertrend | trend | 53.65 | -46.35 | 617 | 20.3 | -86.37 | -19.79 | -86.43 | 1916 |
| 73 | Ichimoku | trend | 53.14 | -46.86 | 534 | 11.8 | -81.94 | -21.98 | -81.98 | 1727 |
| 74 | AI bee: Bizzy | ai | 50.62 | -49.38 | 1050 | 9.0 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -28.46 | -98.63 | 5295 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.43 | -28.28 | -93.43 | 2588 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.56 | -23.74 | -90.57 | 2366 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.54 | -25.73 | -91.56 | 2320 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.48 | -30.73 | -97.49 | 3527 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.58 | -33.30 | -96.58 | 3588 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -24.62 | -94.37 | 2627 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -33.67 | -99.39 | 5719 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.25 | -24.61 | -91.25 | 2643 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.25 | -29.91 | -96.26 | 3555 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -37.99 | -99.73 | 6160 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -28.04 | -91.78 | 2371 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -35.43 | -97.46 | 3654 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -33.97 | -98.47 | 4682 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.60 | -31.03 | -93.60 | 2800 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -36.25 | -99.53 | 6168 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -85.93 | -21.24 | -86.12 | 2101 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.59 | -25.69 | -87.74 | 2109 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -30.62 | -95.98 | 3761 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.29 | -31.68 | -89.32 | 2102 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -31.50 | -95.74 | 4069 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.76 | -99.89 | 8231 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-16T05:05 | EMA 20/50 cross | buy | SOL-USD | 15.37 | — | entry signal |
| 2026-10-16T05:05 | EMA 20/50 cross | buy | ETH-USD | 15.37 | — | entry signal |
| 2026-10-16T05:03 | AI bee: Boozy | buy | ETH-USD | 16.93 | — | Jev: buy (buy p=0.71) |
| 2026-10-16T05:00 | Z-score reversion · 1h | sell | DOGE-USD | 7.37 | 0.14 | exit signal |
| 2026-10-16T05:00 | RSI(14) reversion · 1h | sell | DOGE-USD | 7.59 | 0.12 | exit signal |
| 2026-10-16T05:00 | VWAP momentum · 1h | buy | SOL-USD | 3.59 | — | entry signal |
| 2026-10-16T05:00 | VWAP momentum · 1h | buy | ETH-USD | 3.59 | — | entry signal |
| 2026-10-16T05:00 | RSI(14) reversion | sell | BTC-USD | 16.51 | -0.07 | exit signal |
| 2026-10-16T05:00 | Supertrend | buy | ETH-USD | 13.40 | — | entry signal |
| 2026-10-16T05:00 | Supertrend | buy | DOGE-USD | 13.40 | — | entry signal |
| 2026-10-16T04:59 | AI bee: Bizzy | buy | SOL-USD | 7.62 | — | Jev: buy (buy p=0.60) |
| 2026-10-16T04:34 | AI bee: Bizzy | sell | SOL-USD | 8.32 | -0.07 | Jev: sell (sell p=0.72) after 11 min |
| 2026-10-16T04:30 | Ichimoku | buy | DOGE-USD | 13.27 | — | entry signal |
| 2026-10-16T04:25 | Supertrend | buy | SOL-USD | 13.42 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 05:25:05.000154+00:00 -> 2026-10-16 05:35:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
