# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T15:30:05.000176+00:00 · 15721 ticks

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

Today: 18766 decisions in 2273 calls, $0.2427 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T15:30 | 1 / 15 / 14 | LABU 14% |  |
| Breezy | 2026-10-08T15:30 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-10-08T15:30 | 1 / 26 / 3 | MSTR 64% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 104.00 | 4.00 | 0 | — | -3.63 | -0.61 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 35 | 40.0 | -8.49 | -2.63 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.58 | 1.58 | 0 | — | -0.76 | -0.41 | -5.09 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.31 | 0.57 | -4.03 | 18 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.18 | 1.18 | 0 | — | 2.07 | 1.01 | -3.62 | 1 |
| 7 | Hold SPY | benchmark | 100.85 | 0.85 | 0 | — | 0.30 | 0.23 | -3.66 | 1 |
| 8 | Copy: Warren Buffett (BRK-B) | copy | 100.49 | 0.49 | 0 | — | -2.62 | -1.04 | -7.65 | 1 |
| 9 | Donchian 55/20 · 1h | breakout | 100.19 | 0.19 | 18 | 5.6 | 11.55 | 1.56 | -16.96 | 109 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 13 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 5 | 40.0 | -4.05 | -1.37 | -9.74 | 23 |
| 14 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.25 | -0.76 | 31 | 35.5 | 4.80 | 2.27 | -1.52 | 86 |
| 17 | Daily: SMA 20/50 cross · AAPL | daily | 99.06 | -0.94 | 0 | — | -0.16 | 0.03 | -5.18 | 1 |
| 18 | Trend pullback · 1h | trend | 98.37 | -1.63 | 70 | 25.7 | -21.86 | -6.32 | -24.37 | 170 |
| 19 | Three white soldiers · 1h | momentum | 97.98 | -2.02 | 4 | 0.0 | -2.54 | -1.99 | -3.95 | 25 |
| 20 | EMA 20/50 cross · 1h | trend | 97.43 | -2.57 | 35 | 8.6 | 1.62 | 0.40 | -18.44 | 136 |
| 21 | Copy: Insider buying | copy | 97.35 | -2.65 | 11 | 54.5 | -16.87 | -3.08 | -21.08 | 75 |
| 22 | Hold BTC | benchmark | 97.28 | -2.72 | 0 | — | 24.87 | 3.02 | -8.68 | 1 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 96.75 | -3.25 | 0 | — | 11.52 | 1.89 | -7.38 | 1 |
| 24 | Agent (rotation) | meta | 96.29 | -3.71 | 76 | 26.3 | -1.47 | -0.31 | -8.62 | 274 |
| 25 | ADX DI cross · 1h | trend | 96.22 | -3.78 | 53 | 22.6 | -6.30 | -0.88 | -13.84 | 252 |
| 26 | Agent | meta | 96.12 | -3.88 | 45 | 55.6 | -10.94 | -6.14 | -11.46 | 236 |
| 27 | Daily: Bullish score | daily | 96.00 | -4.00 | 3 | 0.0 | -1.55 | -0.01 | -12.76 | 10 |
| 28 | Daily: Momentum burst | daily | 95.82 | -4.18 | 4 | 0.0 | -3.83 | -0.42 | -17.52 | 40 |
| 29 | Parabolic SAR · 1h | trend | 95.65 | -4.35 | 80 | 21.2 | -4.98 | -0.51 | -20.87 | 291 |
| 30 | Stochastic reversion · 1h | reversion | 95.63 | -4.37 | 74 | 50.0 | -13.74 | -2.69 | -14.25 | 341 |
| 31 | Supertrend · 1h | trend | 95.56 | -4.44 | 45 | 13.3 | -2.94 | -0.23 | -17.19 | 210 |
| 32 | MACD cross · 1h | trend | 95.27 | -4.73 | 103 | 22.3 | -11.26 | -1.53 | -17.27 | 467 |
| 33 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -4.60 | -2.08 | -6.03 | 111 |
| 34 | Connors RSI(2) · 1h | reversion | 94.85 | -5.15 | 92 | 44.6 | -17.25 | -6.11 | -19.29 | 241 |
| 35 | Squeeze breakout · 1h | breakout | 94.72 | -5.28 | 34 | 26.5 | 14.61 | 2.42 | -8.14 | 104 |
| 36 | Z-score reversion · 1h | reversion | 94.26 | -5.74 | 35 | 37.1 | -3.66 | -0.59 | -8.60 | 159 |
| 37 | Agent (ML meta-label) | meta | 93.82 | -6.18 | 304 | 15.5 | 0.40 | 0.21 | -10.54 | 369 |
| 38 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.32 | 1.89 | -6.56 | 194 |
| 39 | RSI momentum · 1h | momentum | 93.73 | -6.27 | 52 | 5.8 | 6.42 | 0.95 | -16.47 | 216 |
| 40 | Bollinger breakout · 1h | breakout | 93.36 | -6.64 | 63 | 30.2 | 7.27 | 1.08 | -12.06 | 291 |
| 41 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | -3.42 | -0.28 | -19.68 | 120 |
| 42 | Volume breakout · 1h | breakout | 92.56 | -7.44 | 45 | 17.8 | 6.17 | 1.01 | -12.60 | 122 |
| 43 | Triple EMA stack · 1h | trend | 92.53 | -7.47 | 62 | 12.9 | -12.25 | -1.37 | -26.86 | 236 |
| 44 | RSI(14) reversion · 1h | reversion | 92.17 | -7.83 | 26 | 26.9 | -2.24 | -0.34 | -8.64 | 151 |
| 45 | Candlestick reversal · 1h | reversion | 91.92 | -8.08 | 93 | 30.1 | -28.15 | -5.67 | -28.32 | 513 |
| 46 | Max aggression: 1-day momentum | meta | 91.65 | -8.35 | 9 | 33.3 | -23.71 | -1.21 | -37.31 | 43 |
| 47 | Opening range 30m | breakout | 91.52 | -8.48 | 119 | 19.3 | -16.83 | -5.13 | -16.86 | 563 |
| 48 | MFI reversion · 1h | reversion | 90.83 | -9.17 | 90 | 26.7 | -15.83 | -2.72 | -16.99 | 123 |
| 49 | Williams %R · 1h | reversion | 90.74 | -9.26 | 103 | 46.6 | -25.76 | -4.57 | -26.30 | 502 |
| 50 | Bollinger reversion · 1h | reversion | 90.57 | -9.43 | 68 | 33.8 | -22.94 | -5.36 | -23.09 | 310 |
| 51 | MACD zero-line · 1h | trend | 90.47 | -9.53 | 57 | 19.3 | -6.21 | -0.66 | -19.00 | 240 |
| 52 | Donchian 20/10 · 1h | breakout | 90.30 | -9.70 | 50 | 20.0 | 1.29 | 0.36 | -16.18 | 221 |
| 53 | EMA 9/21 cross · 1h | trend | 90.28 | -9.72 | 92 | 13.0 | -5.60 | -0.55 | -18.95 | 340 |
| 54 | Three white soldiers | momentum | 89.51 | -10.49 | 113 | 18.6 | -48.58 | -24.23 | -48.64 | 586 |
| 55 | Opening range 15m | breakout | 89.51 | -10.49 | 140 | 17.9 | -18.60 | -5.42 | -18.64 | 681 |
| 56 | Keltner breakout · 1h | breakout | 88.72 | -11.28 | 39 | 17.9 | -9.26 | -0.98 | -23.68 | 226 |
| 57 | OBV trend · 1h | momentum | 88.60 | -11.40 | 135 | 17.8 | -15.46 | -1.82 | -28.12 | 322 |
| 58 | Heikin-Ashi · 1h | trend | 88.30 | -11.70 | 131 | 26.0 | -32.62 | -5.59 | -35.72 | 689 |
| 59 | VWAP momentum · 1h | momentum | 88.10 | -11.90 | 261 | 21.5 | -37.38 | -5.73 | -39.20 | 1270 |
| 60 | CCI reversion · 1h | reversion | 87.89 | -12.11 | 89 | 40.4 | -9.66 | -1.30 | -13.75 | 410 |
| 61 | ROC + volume · 1h | momentum | 87.08 | -12.92 | 125 | 20.0 | -8.60 | -1.00 | -23.15 | 408 |
| 62 | Max aggression: 5-day momentum | meta | 83.94 | -16.07 | 7 | 28.6 | -26.86 | -2.39 | -33.52 | 30 |
| 63 | RSI(14) reversion | reversion | 78.37 | -21.63 | 299 | 30.8 | -72.97 | -19.13 | -73.01 | 1468 |
| 64 | ROC + volume | momentum | 75.43 | -24.57 | 337 | 20.2 | -73.34 | -17.09 | -73.89 | 1652 |
| 65 | Squeeze breakout | breakout | 74.51 | -25.49 | 271 | 14.4 | -62.51 | -18.46 | -62.62 | 1216 |
| 66 | Volume breakout | breakout | 72.69 | -27.31 | 218 | 11.9 | -64.17 | -18.81 | -64.17 | 917 |
| 67 | Donchian 55/20 | breakout | 72.62 | -27.38 | 274 | 16.8 | -68.93 | -14.99 | -68.94 | 1288 |
| 68 | EMA 20/50 cross | trend | 72.02 | -27.98 | 283 | 18.0 | -77.99 | -15.80 | -77.99 | 1464 |
| 69 | VWAP reversion | reversion | 70.69 | -29.31 | 341 | 27.0 | -71.43 | -16.41 | -71.50 | 1422 |
| 70 | Supertrend | trend | 66.91 | -33.09 | 397 | 18.9 | -87.12 | -21.76 | -87.12 | 1941 |
| 71 | Keltner breakout | breakout | 65.80 | -34.20 | 371 | 12.9 | -85.05 | -28.93 | -85.05 | 1871 |
| 72 | AI bee: Bizzy | ai | 64.56 | -35.44 | 670 | 8.5 | — | — | — | — |
| 73 | Ichimoku | trend | 64.16 | -35.84 | 342 | 8.8 | -81.84 | -23.59 | -81.84 | 1735 |
| 74 | MFI reversion | reversion | 63.58 | -36.42 | 427 | 21.3 | -87.97 | -29.59 | -87.98 | 2114 |
| 75 | Z-score reversion | reversion | 63.16 | -36.84 | 440 | 24.1 | -85.76 | -24.12 | -85.78 | 2091 |
| 76 | ADX DI cross | trend | 60.89 | -39.11 | 452 | 8.6 | -89.69 | -35.49 | -89.69 | 2121 |
| 77 | AI bee: Boozy | ai | 60.89 | -39.11 | 235 | 5.1 | — | — | — | — |
| 78 | MACD zero-line | trend | 59.99 | -40.01 | 499 | 14.8 | -91.61 | -30.18 | -91.61 | 2364 |
| 79 | Donchian 20/10 | breakout | 59.97 | -40.03 | 529 | 17.8 | -91.13 | -26.67 | -91.15 | 2658 |
| 80 | Trend pullback | trend | 59.59 | -40.41 | 500 | 15.4 | -90.79 | -27.95 | -90.79 | 2308 |
| 81 | RSI momentum | momentum | 58.82 | -41.18 | 494 | 16.4 | -90.61 | -25.86 | -90.61 | 2352 |
| 82 | Triple EMA stack | trend | 58.61 | -41.39 | 526 | 15.4 | -93.25 | -31.08 | -93.25 | 2601 |
| 83 | Consensus | meta | 56.49 | -43.51 | 512 | 10.4 | -94.36 | -25.66 | -94.36 | 2691 |
| 84 | Bollinger breakout | breakout | 56.21 | -43.79 | 550 | 13.6 | -93.80 | -34.01 | -93.81 | 2821 |
| 85 | Connors RSI(2) | reversion | 52.73 | -47.27 | 705 | 20.3 | -96.27 | -32.29 | -96.28 | 3575 |
| 86 | EMA 9/21 cross | trend | 52.46 | -47.53 | 676 | 15.8 | -97.42 | -33.87 | -97.43 | 3542 |
| 87 | Stochastic reversion | reversion | 51.74 | -48.26 | 799 | 22.2 | -95.71 | -35.28 | -95.71 | 4068 |
| 88 | Bollinger reversion | reversion | 50.84 | -49.16 | 752 | 17.4 | -95.85 | -34.39 | -95.88 | 3726 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -31.07 | -98.71 | 5372 |
| 90 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -37.19 | -96.37 | 3568 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.66 | -99.34 | 5660 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.06 | -99.73 | 6135 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.38 | -39.61 | -97.38 | 3643 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.78 | -98.50 | 4701 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.13 | -99.52 | 6109 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.00 | -99.90 | 8241 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T15:30 | Agent (rotation) | sell | SQQQ | 8.04 | -0.00 | selected signal exited |
| 2026-10-08T15:30 | Agent (ML meta-label) | buy | SQQQ | 6.26 | — | entry |
| 2026-10-08T15:30 | Agent (ML meta-label) | buy | LABU | 6.26 | — | entry |
| 2026-10-08T15:30 | Agent (ML meta-label) | sell | META | 5.52 | -0.00 | selected signal exited |
| 2026-10-08T15:30 | MFI reversion · 1h | buy | NVDA | 22.71 | — | entry signal |
| 2026-10-08T15:30 | CCI reversion · 1h | buy | NVDA | 21.97 | — | entry signal |
| 2026-10-08T15:30 | Stochastic reversion · 1h | buy | LABU | 23.91 | — | entry signal |
| 2026-10-08T15:30 | VWAP reversion · 1h | sell | SQQQ | 25.63 | -0.00 | exit signal |
| 2026-10-08T15:30 | Bollinger reversion · 1h | buy | LABU | 22.65 | — | entry signal |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | buy | UPRO | 9.47 | — | entry signal |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | buy | TQQQ | 9.49 | — | entry signal |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | buy | TECL | 9.49 | — | entry signal |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | buy | SPY | 9.49 | — | entry signal |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | buy | SOXL | 9.49 | — | entry signal |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | buy | QQQ | 9.49 | — | entry signal |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | buy | AMD | 9.49 | — | entry signal |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | sell | TSLA | 14.48 | -0.05 | rebalance down |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | sell | MSTR | 14.21 | -0.21 | rebalance down |
| 2026-10-08T15:30 | Connors RSI(2) · 1h | sell | BITX | 13.67 | -0.52 | rebalance down |
| 2026-10-08T15:30 | OBV trend · 1h | buy | PLTR | 12.43 | — | rebalance up |
| 2026-10-08T15:30 | OBV trend · 1h | buy | MSFT | 12.31 | — | rebalance up |
| 2026-10-08T15:30 | OBV trend · 1h | buy | GOOGL | 12.37 | — | rebalance up |
| 2026-10-08T15:30 | OBV trend · 1h | buy | AAPL | 22.16 | — | entry signal |
| 2026-10-08T15:30 | OBV trend · 1h | sell | UPRO | 9.86 | -0.05 | exit signal |
| 2026-10-08T15:30 | OBV trend · 1h | sell | TQQQ | 9.86 | -0.06 | exit signal |
| 2026-10-08T15:30 | OBV trend · 1h | sell | SPY | 9.88 | -0.04 | exit signal |
| 2026-10-08T15:30 | OBV trend · 1h | sell | QQQ | 9.85 | -0.05 | exit signal |
| 2026-10-08T15:30 | OBV trend · 1h | sell | AMD | 9.89 | -0.03 | exit signal |
| 2026-10-08T15:30 | VWAP momentum · 1h | buy | SQQQ | 22.04 | — | entry signal |
| 2026-10-08T15:30 | VWAP momentum · 1h | buy | AAPL | 9.33 | — | rebalance up |
| 2026-10-08T15:30 | VWAP momentum · 1h | sell | UPRO | 12.59 | -0.09 | exit signal |
| 2026-10-08T15:30 | VWAP momentum · 1h | sell | SPY | 12.66 | -0.05 | exit signal |
| 2026-10-08T15:30 | VWAP momentum · 1h | sell | QQQ | 12.64 | -0.06 | exit signal |
| 2026-10-08T15:30 | VWAP momentum · 1h | sell | AMZN | 12.65 | 0.05 | exit signal |
| 2026-10-08T15:30 | VWAP momentum · 1h | sell | AMD | 12.57 | -0.10 | exit signal |
| 2026-10-08T15:30 | Heikin-Ashi · 1h | sell | AMZN | 22.05 | -0.10 | exit signal |
| 2026-10-08T15:30 | Ichimoku · 1h | sell | SPY | 18.70 | 0.03 | exit signal |
| 2026-10-08T15:30 | Ichimoku · 1h | sell | AMD | 23.18 | -0.18 | exit signal |
| 2026-10-08T15:30 | ADX DI cross · 1h | sell | SPY | 23.96 | -0.09 | exit signal |
| 2026-10-08T15:30 | Supertrend · 1h | buy | UPRO | 5.38 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 15:30:05.000176+00:00 -> 2026-10-08 15:40:05.000176+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
