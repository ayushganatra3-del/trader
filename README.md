# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T13:10:05.000138+00:00 · 71839 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.69 (-21.31%)

Closed trades 241, win rate 35.7%, fees £6.52, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-24 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, BH 12%, FUN 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-23)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.62 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.4, AAPL 4.1, TSLA 3.2, AMZN 1.1, GOOGL 0.8, META 0.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 10482 decisions in 2097 calls, $0.1467 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T13:10 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-24T13:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-24T13:10 | 0 / 4 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| MFI reversion | SQQQ | 1.67 | +10.14% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.92 | 14.92 | 0 | — | 12.43 | 4.42 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 0.77 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.57 | 3.57 | 0 | — | 2.64 | 1.06 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.10 | 0.06 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.75 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.07 | 0.06 | -7.48 | 149 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 95.03 | -4.97 | 0 | — | -6.09 | -1.50 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.13 | -7.87 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.21 | -3.62 | -9.41 | 34 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.46 | -9.54 | 0 | — | -10.60 | -2.27 | -17.03 | 1 |
| 18 | Copy: Insider buying | copy | 89.67 | -10.33 | 58 | 39.7 | -8.96 | -1.74 | -14.79 | 68 |
| 19 | VWAP reversion · 1h | reversion | 89.64 | -10.36 | 163 | 46.0 | -7.82 | -1.42 | -20.49 | 153 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -2.99 | -20.94 | 1 |
| 21 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.39 | -14.39 | 542 |
| 22 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.20 | -13.80 | 9 | 44.4 | -10.93 | -0.60 | -26.65 | 6 |
| 23 | Daily: Bullish score | daily | 85.32 | -14.68 | 20 | 20.0 | -16.45 | -3.46 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -20.72 | -6.91 | -21.47 | 81 |
| 25 | Parabolic SAR · 1h | trend | 79.97 | -20.03 | 204 | 28.4 | -28.42 | -7.72 | -29.63 | 188 |
| 26 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.80 | -6.59 | -14.96 | 66 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -25.59 | -5.79 | -25.94 | 195 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -22.04 | -6.77 | -23.30 | 660 |
| 30 | Volume breakout · 1h | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.90 | -7.05 | -23.27 | 72 |
| 31 | Donchian 55/20 · 1h | breakout | 75.98 | -24.02 | 87 | 13.8 | -30.17 | -8.04 | -30.17 | 84 |
| 32 | Keltner breakout · 1h | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.34 | -6.45 | -24.99 | 143 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.34 | -8.00 | -31.21 | 102 |
| 34 | Supertrend · 1h | trend | 70.59 | -29.41 | 204 | 18.6 | -34.62 | -6.86 | -37.07 | 206 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 70.11 | -29.89 | 3 | 0.0 | -23.26 | -2.75 | -32.18 | 1 |
| 36 | ADX DI cross · 1h | trend | 69.58 | -30.42 | 253 | 19.0 | -39.00 | -7.24 | -39.37 | 274 |
| 37 | Hold BTC | benchmark | 69.38 | -30.62 | 3 | 0.0 | -29.63 | -5.20 | -36.10 | 1 |
| 38 | Daily: Momentum burst | daily | 69.09 | -30.91 | 30 | 13.3 | -37.24 | -5.04 | -37.81 | 25 |
| 39 | Bollinger breakout · 1h | breakout | 68.57 | -31.43 | 207 | 22.2 | -32.74 | -8.61 | -33.88 | 211 |
| 40 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -39.26 | -10.11 | -39.30 | 175 |
| 41 | EMA 20/50 cross · 1h | trend | 67.24 | -32.76 | 123 | 9.8 | -38.32 | -10.57 | -38.60 | 116 |
| 42 | Stochastic reversion · 1h | reversion | 65.95 | -34.05 | 396 | 40.7 | -33.47 | -3.60 | -42.70 | 431 |
| 43 | OBV trend · 1h | momentum | 65.77 | -34.23 | 322 | 19.9 | -40.78 | -10.62 | -40.78 | 235 |
| 44 | MACD zero-line · 1h | trend | 65.74 | -34.26 | 198 | 16.7 | -34.89 | -9.52 | -35.08 | 203 |
| 45 | Heikin-Ashi · 1h | trend | 64.52 | -35.48 | 527 | 22.2 | -46.72 | -9.50 | -47.76 | 629 |
| 46 | RSI momentum · 1h | momentum | 64.21 | -35.79 | 200 | 15.0 | -40.83 | -9.49 | -40.90 | 200 |
| 47 | MFI reversion · 1h | reversion | 63.40 | -36.60 | 486 | 32.9 | -31.85 | -4.61 | -37.87 | 185 |
| 48 | Max aggression: 5-day momentum | meta | 62.28 | -37.72 | 25 | 36.0 | -62.97 | -4.15 | -66.61 | 23 |
| 49 | ROC + volume · 1h | momentum | 61.61 | -38.39 | 452 | 27.0 | -42.64 | -8.52 | -42.95 | 341 |
| 50 | Donchian 20/10 · 1h | breakout | 60.97 | -39.03 | 181 | 17.7 | -40.48 | -8.73 | -42.01 | 193 |
| 51 | Agent (ML meta-label) | meta | 59.38 | -40.62 | 2049 | 25.0 | -17.40 | -2.02 | -29.71 | 313 |
| 52 | EMA 9/21 cross · 1h | trend | 59.28 | -40.72 | 307 | 12.4 | -44.96 | -10.66 | -45.88 | 336 |
| 53 | Max aggression: 1-day momentum | meta | 59.16 | -40.84 | 34 | 26.5 | -52.65 | -3.86 | -54.72 | 38 |
| 54 | MACD cross · 1h | trend | 58.68 | -41.32 | 467 | 21.4 | -49.99 | -9.78 | -51.09 | 512 |
| 55 | Bollinger reversion · 1h | reversion | 57.90 | -42.10 | 391 | 37.6 | -37.42 | -4.46 | -45.42 | 430 |
| 56 | CCI reversion · 1h | reversion | 57.83 | -42.17 | 430 | 40.0 | -49.36 | -8.20 | -51.92 | 501 |
| 57 | Williams %R · 1h | reversion | 53.61 | -46.39 | 500 | 38.4 | -53.98 | -8.82 | -55.78 | 586 |
| 58 | VWAP momentum · 1h | momentum | 53.31 | -46.69 | 1054 | 21.8 | -58.21 | -13.51 | -58.23 | 1188 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.63 | -8.65 | -54.78 | 667 |
| 60 | RSI(14) reversion · 1h | reversion | 50.87 | -49.13 | 241 | 32.0 | -49.14 | -7.74 | -52.25 | 290 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -49.46 | -99.16 | 5351 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.31 | -33.95 | -84.46 | 1442 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.53 | -50.07 | -94.54 | 2438 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.70 | -32.42 | -90.70 | 1916 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.90 | -42.25 | -91.90 | 2258 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.72 | -28.69 | -89.73 | 1969 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -49.05 | -98.20 | 3437 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.04 | -53.66 | -97.04 | 3389 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.35 | -38.68 | -93.37 | 2103 |
| 70 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.40 | -35.21 | -83.41 | 1557 |
| 71 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.31 | -99.67 | 6289 |
| 72 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.27 | -39.12 | -93.27 | 2497 |
| 73 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.47 | -36.88 | -94.47 | 3179 |
| 74 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.08 | -99.82 | 6145 |
| 75 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.34 | -44.88 | -93.34 | 2278 |
| 76 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.75 | -22.33 | -51.75 | 641 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.51 | -24.09 | -78.51 | 1606 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.81 | -59.40 | -97.81 | 3290 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -61.51 | -99.17 | 5117 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.28 | -27.44 | -71.31 | 1203 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.02 | -48.64 | -95.02 | 2672 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.79 | -6.22 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.50 | -37.36 | -85.50 | 1667 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.14 | -99.76 | 6541 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.34 | -30.96 | -91.36 | 2466 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.89 | -20.12 | -82.95 | 1952 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.96 | -31.35 | -91.96 | 2170 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.11 | -49.33 | -98.11 | 4048 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.39 | -48.54 | -90.39 | 2200 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.08 | -30.47 | -68.08 | 792 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.55 | -28.39 | -73.55 | 1165 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.88 | -18.91 | -83.99 | 1825 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.99 | -49.89 | -98.01 | 4411 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -100.50 | -99.94 | 8284 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T13:10 | Stochastic reversion · 1h | buy | BTC-USD | 5.93 | — | entry |
| 2026-11-24T13:10 | Stochastic reversion · 1h | sell | DOGE-USD | 5.93 | -0.15 | stop-loss |
| 2026-11-24T13:10 | EMA 20/50 cross · 1h | sell | XRP-USD | 16.62 | -0.47 | stop-loss |
| 2026-11-24T13:00 | EMA 20/50 cross · 1h | sell | SOL-USD | 16.86 | -0.15 | exit signal |
| 2026-11-24T11:00 | Donchian 55/20 · 1h | sell | XRP-USD | 18.81 | -0.39 | exit signal |
| 2026-11-24T11:00 | Donchian 20/10 · 1h | sell | XRP-USD | 15.19 | -0.32 | exit signal |
| 2026-11-24T11:00 | OBV trend · 1h | sell | XRP-USD | 16.26 | -0.38 | exit signal |
| 2026-11-24T10:00 | RSI momentum · 1h | sell | XRP-USD | 12.76 | -0.18 | exit signal |
| 2026-11-24T10:00 | RSI momentum · 1h | sell | DOGE-USD | 12.75 | -0.26 | exit signal |
| 2026-11-24T09:55 | EMA 20/50 cross · 1h | buy | DOGE-USD | 3.40 | — | rebalance up |
| 2026-11-24T09:00 | Triple EMA stack · 1h | sell | XRP-USD | 16.95 | -0.31 | exit signal |
| 2026-11-24T09:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 3.45 | — | rebalance up |
| 2026-11-24T09:00 | EMA 20/50 cross · 1h | buy | SOL-USD | 5.03 | — | rebalance up |
| 2026-11-24T09:00 | EMA 20/50 cross · 1h | sell | BTC-USD | 14.30 | -0.20 | exit signal |
| 2026-11-24T09:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 8.37 | -0.15 | exit signal |
| 2026-11-24T08:00 | Heikin-Ashi · 1h | sell | XRP-USD | 4.52 | -0.09 | exit signal |
| 2026-11-24T08:00 | Triple EMA stack · 1h | sell | DOGE-USD | 16.98 | -0.30 | exit signal |
| 2026-11-24T08:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 7.33 | -0.13 | exit signal |
| 2026-11-24T06:00 | Heikin-Ashi · 1h | buy | XRP-USD | 4.61 | — | entry signal |
| 2026-11-24T06:00 | Triple EMA stack · 1h | buy | DOGE-USD | 17.28 | — | entry signal |
| 2026-11-24T06:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 7.46 | — | entry signal |
| 2026-11-24T05:00 | CCI reversion · 1h | buy | ETH-USD | 2.53 | — | entry signal |
| 2026-11-24T05:00 | Triple EMA stack · 1h | buy | XRP-USD | 17.26 | — | entry signal |
| 2026-11-24T05:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 8.53 | — | entry signal |
| 2026-11-24T05:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 7.39 | 0.12 | exit signal |
| 2026-11-24T04:00 | Triple EMA stack · 1h | sell | DOGE-USD | 17.22 | 0.05 | exit signal |
| 2026-11-24T03:10 | Stochastic reversion · 1h | buy | ETH-USD | 3.96 | — | entry |
| 2026-11-24T03:10 | Stochastic reversion · 1h | buy | DOGE-USD | 4.12 | — | rebalance up |
| 2026-11-24T03:10 | Stochastic reversion · 1h | sell | BTC-USD | 8.08 | -0.27 | stop-loss |
| 2026-11-24T03:10 | Connors RSI(2) · 1h | sell | SOL-USD | 19.37 | -0.94 | stop-loss |
| 2026-11-24T03:10 | EMA 20/50 cross · 1h | buy | XRP-USD | 6.31 | — | rebalance up |
| 2026-11-24T03:10 | EMA 20/50 cross · 1h | buy | DOGE-USD | 4.88 | — | rebalance up |
| 2026-11-24T03:10 | EMA 20/50 cross · 1h | sell | ETH-USD | 14.13 | -0.38 | stop-loss |
| 2026-11-24T03:00 | Donchian 55/20 · 1h | sell | SOL-USD | 18.77 | -0.43 | exit signal |
| 2026-11-24T03:00 | Donchian 20/10 · 1h | sell | SOL-USD | 15.16 | -0.34 | exit signal |
| 2026-11-24T03:00 | Donchian 20/10 · 1h | sell | BTC-USD | 15.10 | -0.41 | exit signal |
| 2026-11-24T03:00 | RSI momentum · 1h | buy | XRP-USD | 3.64 | — | rebalance up |
| 2026-11-24T03:00 | RSI momentum · 1h | buy | DOGE-USD | 3.71 | — | rebalance up |
| 2026-11-24T03:00 | RSI momentum · 1h | sell | SOL-USD | 9.09 | -0.21 | exit signal |
| 2026-11-24T03:00 | RSI momentum · 1h | sell | BTC-USD | 9.06 | -0.24 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 13:10:05.000138+00:00 -> 2026-11-24 13:20:05.000138+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
