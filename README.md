# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T16:00:05.000134+00:00 · 15749 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.12 (-3.88%)

Closed trades 45, win rate 55.6%, fees £1.91, max drawdown -4.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-08 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 21274 decisions in 2357 calls, $0.2722 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T16:00 | 1 / 15 / 14 | cash |  |
| Breezy | 2026-10-08T16:00 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-10-08T16:00 | 1 / 26 / 3 | MSTR 64% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| VWAP reversion | MSFT | 1.96 | +0.82% | 3 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 103.51 | 3.51 | 0 | — | -3.96 | -0.68 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 35 | 40.0 | -8.49 | -2.63 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.42 | 1.43 | 0 | — | -0.86 | -0.48 | -5.09 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.31 | 0.57 | -4.03 | 18 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.18 | 1.18 | 0 | — | 2.07 | 1.01 | -3.62 | 1 |
| 7 | Hold SPY | benchmark | 100.82 | 0.82 | 0 | — | 0.26 | 0.20 | -3.66 | 1 |
| 8 | Copy: Warren Buffett (BRK-B) | copy | 100.53 | 0.53 | 0 | — | -2.59 | -1.03 | -7.65 | 1 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Donchian 55/20 · 1h | breakout | 99.91 | -0.09 | 18 | 5.6 | 12.46 | 1.64 | -16.96 | 109 |
| 12 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 5 | 40.0 | -4.05 | -1.37 | -9.74 | 23 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 15 | Daily: SMA 20/50 cross · AAPL | daily | 99.14 | -0.86 | 0 | — | 0.30 | 0.20 | -5.18 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.20 | -1.52 | 86 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.67 | -1.32 | 0 | — | -5.19 | -2.48 | -5.49 | 1 |
| 18 | Trend pullback · 1h | trend | 98.09 | -1.91 | 70 | 25.7 | -22.08 | -6.38 | -24.37 | 170 |
| 19 | Three white soldiers · 1h | momentum | 97.86 | -2.13 | 4 | 0.0 | -2.66 | -2.09 | -3.95 | 25 |
| 20 | Copy: Insider buying | copy | 97.86 | -2.14 | 11 | 54.5 | -16.06 | -2.88 | -21.08 | 75 |
| 21 | EMA 20/50 cross · 1h | trend | 97.19 | -2.81 | 35 | 8.6 | -1.39 | 0.01 | -18.58 | 138 |
| 22 | Hold BTC | benchmark | 96.88 | -3.12 | 0 | — | 24.76 | 3.00 | -8.68 | 1 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 96.37 | -3.63 | 0 | — | 11.42 | 1.87 | -7.72 | 1 |
| 24 | Agent (rotation) | meta | 96.29 | -3.71 | 76 | 26.3 | -0.10 | 0.06 | -8.80 | 263 |
| 25 | ADX DI cross · 1h | trend | 96.26 | -3.74 | 53 | 22.6 | -6.12 | -0.90 | -13.84 | 255 |
| 26 | Agent | meta | 96.12 | -3.88 | 45 | 55.6 | -13.19 | -6.54 | -13.52 | 241 |
| 27 | Daily: Momentum burst | daily | 95.80 | -4.20 | 4 | 0.0 | -4.01 | -0.45 | -17.53 | 40 |
| 28 | Parabolic SAR · 1h | trend | 95.42 | -4.58 | 80 | 21.2 | -5.13 | -0.54 | -20.80 | 292 |
| 29 | Supertrend · 1h | trend | 95.38 | -4.62 | 45 | 13.3 | -3.25 | -0.28 | -17.19 | 207 |
| 30 | MACD cross · 1h | trend | 95.20 | -4.80 | 103 | 22.3 | -11.20 | -1.58 | -17.27 | 462 |
| 31 | Daily: Bullish score | daily | 95.19 | -4.81 | 3 | 0.0 | -2.29 | -0.10 | -12.76 | 10 |
| 32 | Stochastic reversion · 1h | reversion | 95.09 | -4.91 | 74 | 50.0 | -14.27 | -2.77 | -14.72 | 342 |
| 33 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -4.93 | -2.22 | -6.03 | 114 |
| 34 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 14.57 | 2.43 | -8.14 | 104 |
| 35 | Connors RSI(2) · 1h | reversion | 94.50 | -5.50 | 93 | 44.1 | -17.57 | -6.14 | -19.60 | 241 |
| 36 | Z-score reversion · 1h | reversion | 94.38 | -5.62 | 35 | 37.1 | -2.44 | -0.36 | -8.60 | 158 |
| 37 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.32 | 1.89 | -6.56 | 194 |
| 38 | Agent (ML meta-label) | meta | 93.55 | -6.45 | 309 | 16.2 | -0.55 | 0.05 | -11.76 | 361 |
| 39 | RSI momentum · 1h | momentum | 93.51 | -6.49 | 52 | 5.8 | 5.41 | 0.84 | -16.57 | 215 |
| 40 | Bollinger breakout · 1h | breakout | 93.28 | -6.72 | 63 | 30.2 | 5.71 | 0.90 | -12.06 | 289 |
| 41 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | -0.92 | 0.09 | -20.61 | 119 |
| 42 | Volume breakout · 1h | breakout | 92.49 | -7.51 | 45 | 17.8 | 6.23 | 1.02 | -12.60 | 122 |
| 43 | Triple EMA stack · 1h | trend | 92.31 | -7.69 | 62 | 12.9 | -11.12 | -1.26 | -24.52 | 241 |
| 44 | RSI(14) reversion · 1h | reversion | 92.17 | -7.83 | 26 | 26.9 | -4.24 | -0.83 | -8.64 | 140 |
| 45 | Candlestick reversal · 1h | reversion | 91.88 | -8.12 | 93 | 30.1 | -29.78 | -6.07 | -29.82 | 505 |
| 46 | Max aggression: 1-day momentum | meta | 91.35 | -8.65 | 9 | 33.3 | -23.96 | -1.23 | -37.31 | 43 |
| 47 | Opening range 30m | breakout | 91.09 | -8.91 | 122 | 18.9 | -17.28 | -5.25 | -17.28 | 563 |
| 48 | MFI reversion · 1h | reversion | 90.74 | -9.26 | 90 | 26.7 | -15.91 | -2.73 | -16.99 | 123 |
| 49 | MACD zero-line · 1h | trend | 90.46 | -9.54 | 57 | 19.3 | -6.36 | -0.68 | -19.10 | 240 |
| 50 | Williams %R · 1h | reversion | 90.40 | -9.60 | 103 | 46.6 | -26.01 | -4.59 | -26.58 | 501 |
| 51 | EMA 9/21 cross · 1h | trend | 90.10 | -9.90 | 92 | 13.0 | -7.02 | -0.76 | -18.95 | 334 |
| 52 | Donchian 20/10 · 1h | breakout | 90.05 | -9.95 | 50 | 20.0 | -0.93 | 0.09 | -16.18 | 221 |
| 53 | Bollinger reversion · 1h | reversion | 89.98 | -10.02 | 68 | 33.8 | -23.49 | -5.35 | -23.63 | 310 |
| 54 | Three white soldiers | momentum | 89.62 | -10.38 | 113 | 18.6 | -48.86 | -24.55 | -48.99 | 586 |
| 55 | Opening range 15m | breakout | 89.03 | -10.97 | 143 | 17.5 | -19.02 | -5.52 | -19.02 | 682 |
| 56 | Keltner breakout · 1h | breakout | 88.62 | -11.38 | 39 | 17.9 | -12.21 | -1.45 | -23.68 | 220 |
| 57 | OBV trend · 1h | momentum | 88.42 | -11.57 | 135 | 17.8 | -15.67 | -1.85 | -28.22 | 322 |
| 58 | VWAP momentum · 1h | momentum | 88.22 | -11.78 | 261 | 21.5 | -36.97 | -5.66 | -39.11 | 1261 |
| 59 | Heikin-Ashi · 1h | trend | 88.14 | -11.86 | 131 | 26.0 | -32.74 | -5.62 | -35.79 | 689 |
| 60 | CCI reversion · 1h | reversion | 87.85 | -12.15 | 89 | 40.4 | -9.82 | -1.32 | -13.78 | 406 |
| 61 | ROC + volume · 1h | momentum | 86.89 | -13.11 | 126 | 20.6 | -9.13 | -1.08 | -23.15 | 408 |
| 62 | Max aggression: 5-day momentum | meta | 83.66 | -16.34 | 7 | 28.6 | -27.09 | -2.41 | -33.65 | 30 |
| 63 | RSI(14) reversion | reversion | 77.76 | -22.24 | 301 | 30.6 | -73.11 | -19.04 | -73.11 | 1466 |
| 64 | ROC + volume | momentum | 75.43 | -24.57 | 337 | 20.2 | -73.40 | -17.11 | -73.95 | 1651 |
| 65 | Squeeze breakout | breakout | 74.51 | -25.49 | 271 | 14.4 | -62.60 | -18.80 | -62.60 | 1211 |
| 66 | Volume breakout | breakout | 72.69 | -27.31 | 218 | 11.9 | -64.17 | -18.81 | -64.17 | 911 |
| 67 | Donchian 55/20 | breakout | 72.63 | -27.37 | 274 | 16.8 | -68.94 | -14.99 | -68.96 | 1288 |
| 68 | EMA 20/50 cross | trend | 72.02 | -27.98 | 283 | 18.0 | -78.05 | -15.74 | -78.09 | 1459 |
| 69 | VWAP reversion | reversion | 69.75 | -30.25 | 343 | 26.8 | -71.88 | -16.39 | -71.88 | 1423 |
| 70 | Supertrend | trend | 66.70 | -33.30 | 397 | 18.9 | -87.15 | -21.76 | -87.15 | 1936 |
| 71 | Keltner breakout | breakout | 65.80 | -34.20 | 371 | 12.9 | -85.05 | -28.86 | -85.06 | 1870 |
| 72 | AI bee: Bizzy | ai | 64.40 | -35.60 | 672 | 8.5 | — | — | — | — |
| 73 | Ichimoku | trend | 64.19 | -35.81 | 343 | 8.7 | -81.87 | -23.61 | -81.88 | 1736 |
| 74 | MFI reversion | reversion | 63.17 | -36.84 | 432 | 21.1 | -87.98 | -29.49 | -87.99 | 2114 |
| 75 | Z-score reversion | reversion | 62.91 | -37.09 | 441 | 24.0 | -85.85 | -24.09 | -85.85 | 2093 |
| 76 | ADX DI cross | trend | 60.97 | -39.03 | 452 | 8.6 | -89.70 | -35.35 | -89.73 | 2121 |
| 77 | AI bee: Boozy | ai | 60.82 | -39.18 | 235 | 5.1 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 59.97 | -40.03 | 529 | 17.8 | -91.14 | -26.70 | -91.14 | 2659 |
| 79 | MACD zero-line | trend | 59.96 | -40.04 | 500 | 14.8 | -91.59 | -30.14 | -91.59 | 2366 |
| 80 | Trend pullback | trend | 59.53 | -40.47 | 502 | 15.3 | -90.80 | -27.99 | -90.80 | 2307 |
| 81 | RSI momentum | momentum | 58.84 | -41.16 | 494 | 16.4 | -90.56 | -25.82 | -90.56 | 2351 |
| 82 | Triple EMA stack | trend | 58.69 | -41.31 | 526 | 15.4 | -93.29 | -31.13 | -93.30 | 2608 |
| 83 | Consensus | meta | 56.50 | -43.50 | 512 | 10.4 | -94.29 | -25.64 | -94.30 | 2675 |
| 84 | Bollinger breakout | breakout | 56.21 | -43.79 | 550 | 13.6 | -93.80 | -33.99 | -93.80 | 2818 |
| 85 | Connors RSI(2) | reversion | 52.73 | -47.27 | 707 | 20.4 | -96.26 | -32.29 | -96.26 | 3573 |
| 86 | EMA 9/21 cross | trend | 52.45 | -47.55 | 677 | 15.8 | -97.43 | -33.95 | -97.43 | 3536 |
| 87 | Stochastic reversion | reversion | 51.47 | -48.53 | 803 | 22.0 | -95.72 | -35.14 | -95.72 | 4072 |
| 88 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -31.07 | -98.71 | 5366 |
| 89 | Bollinger reversion | reversion | 50.43 | -49.57 | 753 | 17.4 | -95.86 | -34.12 | -95.87 | 3722 |
| 90 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -37.08 | -96.37 | 3566 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.40 | -99.34 | 5663 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.15 | -99.73 | 6140 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.38 | -39.62 | -97.38 | 3645 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.85 | -98.51 | 4703 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.16 | -99.52 | 6118 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.89 | -99.90 | 8235 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T16:00 | Agent (ML meta-label) | buy | SQQQ | 6.24 | — | entry |
| 2026-10-08T16:00 | Agent (ML meta-label) | buy | LABU | 6.24 | — | entry |
| 2026-10-08T16:00 | Stochastic reversion | buy | PLTR | 2.15 | — | entry |
| 2026-10-08T16:00 | Stochastic reversion | buy | NVDA | 2.57 | — | entry |
| 2026-10-08T16:00 | Stochastic reversion | buy | MSTR | 2.57 | — | entry |
| 2026-10-08T16:00 | Stochastic reversion | sell | BTC-USD | 3.65 | -0.05 | stop-loss |
| 2026-10-08T16:00 | Stochastic reversion | sell | BITX | 3.65 | -0.05 | stop-loss |
| 2026-10-08T16:00 | Z-score reversion | sell | LABU | 4.82 | -0.08 | stop-loss |
| 2026-10-08T16:00 | RSI(14) reversion | sell | LABU | 11.09 | -0.18 | stop-loss |
| 2026-10-08T16:00 | Opening range 30m | sell | TECL | 22.77 | -0.15 | stop-loss |
| 2026-10-08T16:00 | Opening range 15m | sell | TECL | 22.10 | -0.07 | stop-loss |
| 2026-10-08T16:00 | Trend pullback | sell | MSFT | 14.86 | -0.03 | exit signal |
| 2026-10-08T15:55 | Agent (ML meta-label) | buy | GOOGL | 7.20 | — | entry |
| 2026-10-08T15:55 | Agent (ML meta-label) | sell | SQQQ | 6.28 | 0.02 | selected signal exited |
| 2026-10-08T15:55 | Agent (ML meta-label) | sell | LABU | 6.67 | -0.02 | selected signal exited |
| 2026-10-08T15:55 | MFI reversion | buy | TNA | 10.54 | — | entry |
| 2026-10-08T15:55 | MFI reversion | sell | GOOGL | 9.05 | -0.02 | target is flat |
| 2026-10-08T15:55 | MFI reversion | sell | BITX | 9.01 | -0.06 | target is flat |
| 2026-10-08T15:55 | Stochastic reversion | buy | ETH-USD | 1.27 | — | entry |
| 2026-10-08T15:55 | Stochastic reversion | buy | DOGE-USD | 2.34 | — | entry |
| 2026-10-08T15:55 | Stochastic reversion | sell | ETHU | 3.61 | -0.09 | stop-loss |
| 2026-10-08T15:55 | Opening range 15m | buy | TECL | 22.16 | — | entry |
| 2026-10-08T15:55 | Opening range 15m | sell | SOXL | 22.16 | -0.27 | exit signal |
| 2026-10-08T15:55 | Donchian 20/10 | buy | SQQQ | 14.99 | — | entry signal |
| 2026-10-08T15:54 | AI bee: Bizzy | sell | AAPL | 8.94 | -0.01 | Jev: sell (sell p=0.52) after 16 min |
| 2026-10-08T15:50 | Agent (ML meta-label) | buy | LABU | 6.69 | — | entry |
| 2026-10-08T15:50 | Agent (ML meta-label) | sell | GOOGL | 6.69 | 0.00 | selected signal exited |
| 2026-10-08T15:50 | MFI reversion | buy | QQQ | 9.04 | — | entry |
| 2026-10-08T15:50 | MFI reversion | buy | IWM | 9.06 | — | entry signal |
| 2026-10-08T15:50 | MFI reversion | buy | GOOGL | 9.06 | — | entry signal |
| 2026-10-08T15:50 | MFI reversion | buy | BTC-USD | 9.06 | — | entry signal |
| 2026-10-08T15:50 | MFI reversion | buy | BITX | 9.06 | — | entry signal |
| 2026-10-08T15:50 | MFI reversion | sell | TQQQ | 6.78 | -0.01 | rebalance down |
| 2026-10-08T15:50 | MFI reversion | sell | SOL-USD | 6.78 | -0.02 | rebalance down |
| 2026-10-08T15:50 | Z-score reversion | buy | BITX | 5.68 | — | entry signal |
| 2026-10-08T15:50 | Z-score reversion | buy | AMZN | 6.30 | — | entry signal |
| 2026-10-08T15:50 | Connors RSI(2) | sell | PLTR | 13.20 | 0.02 | exit signal |
| 2026-10-08T15:50 | Connors RSI(2) | sell | AMZN | 13.17 | -0.00 | exit signal |
| 2026-10-08T15:50 | RSI(14) reversion | buy | SOL-USD | 10.62 | — | entry signal |
| 2026-10-08T15:50 | RSI(14) reversion | buy | BTC-USD | 11.15 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 16:00:05.000134+00:00 -> 2026-10-08 16:10:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
