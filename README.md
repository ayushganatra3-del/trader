# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T14:00:05.000142+00:00 · 15644 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.46 (-4.54%)

Closed trades 44, win rate 54.5%, fees £1.89, max drawdown -4.98%.

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

Today: 11806 decisions in 2042 calls, $0.1612 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T14:00 | 4 / 19 / 8 | cash |  |
| Breezy | 2026-10-08T14:00 | 0 / 26 / 5 | cash |  |
| Boozy | 2026-10-08T14:00 | 4 / 24 / 3 | MSTR 54% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |
| RSI(14) reversion | SOXL | 1.90 | +5.73% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 103.74 | 3.74 | 0 | — | -2.66 | -0.40 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.70 | 2.70 | 34 | 41.2 | -8.37 | -2.59 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.63 | 1.63 | 0 | — | -0.42 | -0.20 | -5.09 | 1 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.43 | 1.43 | 0 | — | 2.11 | 1.03 | -3.62 | 1 |
| 6 | Copy: Warren Buffett (BRK-B) | copy | 101.36 | 1.36 | 0 | — | -2.08 | -0.80 | -7.65 | 1 |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.54 | 0.65 | -4.29 | 18 |
| 8 | Hold SPY | benchmark | 101.13 | 1.13 | 0 | — | 0.28 | 0.21 | -3.66 | 1 |
| 9 | Donchian 55/20 · 1h | breakout | 100.17 | 0.17 | 18 | 5.6 | 10.78 | 1.49 | -16.96 | 108 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 99.94 | -0.06 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 30 | 36.7 | 4.99 | 2.36 | -1.52 | 85 |
| 14 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 5 | 40.0 | -4.05 | -1.37 | -9.74 | 23 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Daily: SMA 20/50 cross · AAPL | daily | 99.07 | -0.93 | 0 | — | 0.18 | 0.16 | -5.18 | 1 |
| 18 | Trend pullback · 1h | trend | 98.57 | -1.43 | 69 | 24.6 | -21.64 | -6.27 | -24.25 | 168 |
| 19 | Hold BTC | benchmark | 98.44 | -1.56 | 0 | — | 26.24 | 3.18 | -8.68 | 1 |
| 20 | Three white soldiers · 1h | momentum | 98.06 | -1.94 | 4 | 0.0 | -2.58 | -2.01 | -3.95 | 25 |
| 21 | Daily: Bullish score | daily | 98.03 | -1.97 | 3 | 0.0 | 1.08 | 0.34 | -12.76 | 10 |
| 22 | EMA 20/50 cross · 1h | trend | 97.25 | -2.75 | 35 | 8.6 | 0.66 | 0.29 | -17.82 | 140 |
| 23 | Stochastic reversion · 1h | reversion | 97.17 | -2.83 | 70 | 52.9 | -12.93 | -2.57 | -13.26 | 341 |
| 24 | Copy: Insider buying | copy | 97.04 | -2.96 | 11 | 54.5 | -16.64 | -3.02 | -21.08 | 75 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.97 | -3.03 | 0 | — | 12.00 | 1.96 | -7.38 | 1 |
| 26 | Agent (rotation) | meta | 96.34 | -3.66 | 75 | 26.7 | -1.82 | -0.35 | -10.44 | 285 |
| 27 | Connors RSI(2) · 1h | reversion | 96.19 | -3.81 | 92 | 44.6 | -16.13 | -5.88 | -18.20 | 231 |
| 28 | Parabolic SAR · 1h | trend | 96.07 | -3.93 | 80 | 21.2 | -5.49 | -0.60 | -20.87 | 291 |
| 29 | Daily: Momentum burst | daily | 95.84 | -4.16 | 4 | 0.0 | -4.03 | -0.46 | -17.52 | 40 |
| 30 | MACD cross · 1h | trend | 95.73 | -4.27 | 103 | 22.3 | -14.20 | -2.22 | -17.27 | 462 |
| 31 | Supertrend · 1h | trend | 95.71 | -4.29 | 42 | 9.5 | -1.08 | 0.04 | -17.11 | 203 |
| 32 | ADX DI cross · 1h | trend | 95.58 | -4.42 | 47 | 14.9 | -3.30 | -0.35 | -13.84 | 252 |
| 33 | Agent | meta | 95.46 | -4.54 | 44 | 54.5 | -9.72 | -5.50 | -10.54 | 253 |
| 34 | Z-score reversion · 1h | reversion | 95.26 | -4.74 | 34 | 38.2 | -2.80 | -0.43 | -8.60 | 158 |
| 35 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -1.18 | -0.48 | -6.03 | 110 |
| 36 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 12.78 | 2.12 | -8.12 | 111 |
| 37 | Candlestick reversal · 1h | reversion | 94.71 | -5.29 | 89 | 31.5 | -27.17 | -5.91 | -27.42 | 504 |
| 38 | RSI(14) reversion · 1h | reversion | 94.36 | -5.64 | 22 | 31.8 | -5.27 | -1.16 | -8.11 | 137 |
| 39 | Agent (ML meta-label) | meta | 94.33 | -5.67 | 296 | 15.9 | -8.10 | -1.37 | -14.71 | 364 |
| 40 | Gap and go | momentum | 93.99 | -6.01 | 49 | 8.2 | 7.49 | 1.93 | -6.41 | 194 |
| 41 | RSI momentum · 1h | momentum | 93.79 | -6.21 | 51 | 3.9 | 2.08 | 0.46 | -16.53 | 219 |
| 42 | Bollinger breakout · 1h | breakout | 93.52 | -6.47 | 63 | 30.2 | 7.86 | 1.16 | -12.06 | 290 |
| 43 | Ichimoku · 1h | trend | 93.09 | -6.91 | 39 | 17.9 | -3.48 | -0.29 | -19.68 | 120 |
| 44 | Bollinger reversion · 1h | reversion | 92.94 | -7.07 | 61 | 37.7 | -21.09 | -5.33 | -21.40 | 307 |
| 45 | Max aggression: 1-day momentum | meta | 92.67 | -7.33 | 9 | 33.3 | -23.01 | -1.16 | -37.31 | 43 |
| 46 | Volume breakout · 1h | breakout | 92.67 | -7.33 | 45 | 17.8 | 6.84 | 1.10 | -12.60 | 121 |
| 47 | Triple EMA stack · 1h | trend | 92.48 | -7.52 | 61 | 11.5 | -9.02 | -0.88 | -24.51 | 240 |
| 48 | Opening range 30m | breakout | 92.33 | -7.67 | 113 | 20.4 | -16.30 | -4.95 | -16.77 | 551 |
| 49 | Williams %R · 1h | reversion | 91.98 | -8.02 | 100 | 48.0 | -25.01 | -4.50 | -25.05 | 499 |
| 50 | MFI reversion · 1h | reversion | 91.65 | -8.35 | 89 | 27.0 | -15.09 | -2.62 | -16.99 | 121 |
| 51 | MACD zero-line · 1h | trend | 90.53 | -9.47 | 57 | 19.3 | -7.01 | -0.78 | -19.10 | 241 |
| 52 | Opening range 15m | breakout | 90.50 | -9.49 | 131 | 19.1 | -17.95 | -5.22 | -18.28 | 671 |
| 53 | Donchian 20/10 · 1h | breakout | 90.44 | -9.56 | 50 | 20.0 | 1.62 | 0.40 | -16.18 | 220 |
| 54 | EMA 9/21 cross · 1h | trend | 90.22 | -9.78 | 91 | 12.1 | -6.14 | -0.63 | -18.91 | 341 |
| 55 | Three white soldiers | momentum | 89.95 | -10.05 | 109 | 18.3 | -48.58 | -24.23 | -48.58 | 582 |
| 56 | CCI reversion · 1h | reversion | 89.39 | -10.61 | 86 | 41.9 | -8.17 | -1.09 | -12.57 | 405 |
| 57 | Keltner breakout · 1h | breakout | 88.88 | -11.12 | 39 | 17.9 | -10.11 | -1.14 | -23.68 | 215 |
| 58 | OBV trend · 1h | momentum | 88.81 | -11.19 | 127 | 17.3 | -15.28 | -1.80 | -28.16 | 324 |
| 59 | VWAP momentum · 1h | momentum | 88.81 | -11.20 | 251 | 21.9 | -37.24 | -5.72 | -38.98 | 1271 |
| 60 | Heikin-Ashi · 1h | trend | 88.59 | -11.41 | 128 | 25.0 | -31.82 | -5.41 | -35.72 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.52 | -12.48 | 124 | 19.4 | -7.50 | -0.84 | -23.15 | 404 |
| 62 | Max aggression: 5-day momentum | meta | 84.87 | -15.13 | 7 | 28.6 | -26.18 | -2.32 | -33.47 | 30 |
| 63 | RSI(14) reversion | reversion | 78.80 | -21.20 | 285 | 29.5 | -73.06 | -19.38 | -73.13 | 1473 |
| 64 | ROC + volume | momentum | 75.80 | -24.20 | 334 | 20.4 | -73.10 | -16.92 | -73.71 | 1647 |
| 65 | Squeeze breakout | breakout | 75.13 | -24.87 | 268 | 14.6 | -62.27 | -18.40 | -62.39 | 1217 |
| 66 | Donchian 55/20 | breakout | 72.78 | -27.22 | 273 | 16.8 | -68.77 | -14.90 | -68.88 | 1290 |
| 67 | Volume breakout | breakout | 72.74 | -27.26 | 217 | 12.0 | -64.05 | -18.71 | -64.05 | 903 |
| 68 | EMA 20/50 cross | trend | 72.52 | -27.48 | 281 | 18.1 | -78.30 | -15.92 | -78.34 | 1475 |
| 69 | VWAP reversion | reversion | 71.47 | -28.53 | 335 | 27.5 | -70.92 | -16.21 | -71.05 | 1406 |
| 70 | Supertrend | trend | 67.95 | -32.05 | 387 | 19.4 | -86.94 | -21.65 | -86.95 | 1929 |
| 71 | Keltner breakout | breakout | 65.88 | -34.12 | 370 | 13.0 | -84.99 | -28.88 | -84.99 | 1862 |
| 72 | Ichimoku | trend | 64.95 | -35.05 | 338 | 8.9 | -81.68 | -23.55 | -81.73 | 1734 |
| 73 | AI bee: Bizzy | ai | 64.59 | -35.41 | 666 | 8.4 | — | — | — | — |
| 74 | MFI reversion | reversion | 64.42 | -35.58 | 421 | 21.1 | -87.78 | -29.67 | -87.78 | 2121 |
| 75 | Z-score reversion | reversion | 63.44 | -36.56 | 428 | 23.6 | -85.70 | -24.09 | -85.73 | 2076 |
| 76 | ADX DI cross | trend | 61.84 | -38.16 | 439 | 8.9 | -89.49 | -34.92 | -89.49 | 2103 |
| 77 | AI bee: Boozy | ai | 61.08 | -38.92 | 232 | 3.9 | — | — | — | — |
| 78 | MACD zero-line | trend | 60.95 | -39.05 | 493 | 15.0 | -91.51 | -29.90 | -91.52 | 2362 |
| 79 | Donchian 20/10 | breakout | 60.92 | -39.08 | 524 | 17.9 | -91.04 | -26.59 | -91.04 | 2654 |
| 80 | Trend pullback | trend | 59.86 | -40.15 | 496 | 15.5 | -90.84 | -27.94 | -90.85 | 2314 |
| 81 | RSI momentum | momentum | 59.68 | -40.32 | 487 | 16.6 | -90.53 | -25.82 | -90.53 | 2361 |
| 82 | Triple EMA stack | trend | 59.06 | -40.94 | 522 | 15.5 | -93.28 | -31.16 | -93.29 | 2610 |
| 83 | Consensus | meta | 56.60 | -43.40 | 509 | 10.2 | -94.22 | -25.23 | -94.22 | 2680 |
| 84 | Bollinger breakout | breakout | 56.54 | -43.46 | 548 | 13.7 | -93.78 | -34.01 | -93.78 | 2820 |
| 85 | EMA 9/21 cross | trend | 53.28 | -46.72 | 666 | 16.1 | -97.42 | -33.98 | -97.42 | 3538 |
| 86 | Connors RSI(2) | reversion | 52.75 | -47.25 | 699 | 19.9 | -96.29 | -32.28 | -96.29 | 3579 |
| 87 | Stochastic reversion | reversion | 51.83 | -48.17 | 784 | 21.7 | -95.70 | -35.28 | -95.71 | 4056 |
| 88 | Bollinger reversion | reversion | 50.77 | -49.23 | 731 | 16.4 | -95.88 | -34.41 | -95.88 | 3721 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -31.03 | -98.70 | 5367 |
| 90 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.36 | -37.10 | -96.36 | 3577 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -38.00 | -99.34 | 5669 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.53 | -99.73 | 6138 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -39.56 | -97.35 | 3652 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.91 | -98.50 | 4697 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.33 | -99.52 | 6115 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.42 | -99.90 | 8243 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T14:00 | Agent (ML meta-label) | buy | SOL-USD | 5.55 | — | entry |
| 2026-10-08T14:00 | Williams %R · 1h | buy | XRP-USD | 18.27 | — | entry signal |
| 2026-10-08T14:00 | Williams %R · 1h | buy | ETH-USD | 18.42 | — | entry signal |
| 2026-10-08T14:00 | Williams %R · 1h | sell | BTC-USD | 4.63 | -0.05 | rebalance down |
| 2026-10-08T14:00 | Candlestick reversal · 1h | buy | SOL-USD | 23.69 | — | entry signal |
| 2026-10-08T14:00 | MFI reversion | buy | BITX | 16.11 | — | entry |
| 2026-10-08T14:00 | MFI reversion | sell | ETHU | 16.17 | 0.03 | target is flat |
| 2026-10-08T14:00 | Stochastic reversion | buy | TQQQ | 4.31 | — | entry |
| 2026-10-08T14:00 | Stochastic reversion | buy | TECL | 4.32 | — | entry signal |
| 2026-10-08T14:00 | Stochastic reversion | buy | SOXL | 4.32 | — | entry signal |
| 2026-10-08T14:00 | Stochastic reversion | buy | QQQ | 4.32 | — | entry |
| 2026-10-08T14:00 | Stochastic reversion | buy | NVDA | 4.32 | — | entry signal |
| 2026-10-08T14:00 | Stochastic reversion | sell | TNA | 3.07 | 0.00 | rebalance down |
| 2026-10-08T14:00 | Stochastic reversion | sell | MSTR | 3.13 | 0.03 | rebalance down |
| 2026-10-08T14:00 | Stochastic reversion | sell | LABU | 3.03 | -0.02 | rebalance down |
| 2026-10-08T14:00 | Stochastic reversion | sell | ETHU | 3.11 | 0.02 | rebalance down |
| 2026-10-08T14:00 | Stochastic reversion | sell | COIN | 3.12 | 0.02 | rebalance down |
| 2026-10-08T14:00 | Stochastic reversion | sell | BITX | 3.09 | 0.01 | rebalance down |
| 2026-10-08T14:00 | Stochastic reversion | sell | AMD | 3.04 | -0.01 | rebalance down |
| 2026-10-08T14:00 | Z-score reversion | buy | UPRO | 6.36 | — | entry signal |
| 2026-10-08T14:00 | Z-score reversion | buy | COIN | 12.69 | — | entry signal |
| 2026-10-08T14:00 | Z-score reversion | sell | SOL-USD | 3.20 | -0.02 | rebalance down |
| 2026-10-08T14:00 | Connors RSI(2) | sell | AMZN | 13.17 | -0.02 | exit signal |
| 2026-10-08T14:00 | RSI(14) reversion | buy | MSTR | 9.84 | — | entry signal |
| 2026-10-08T14:00 | RSI momentum | buy | MSFT | 14.92 | — | entry signal |
| 2026-10-08T13:55 | Stochastic reversion · 1h | buy | TSLA | 5.77 | — | rebalance up |
| 2026-10-08T13:55 | Stochastic reversion · 1h | buy | TNA | 5.73 | — | rebalance up |
| 2026-10-08T13:55 | Stochastic reversion · 1h | buy | SQQQ | 5.68 | — | rebalance up |
| 2026-10-08T13:55 | Stochastic reversion · 1h | buy | SOL-USD | 6.46 | — | rebalance up |
| 2026-10-08T13:55 | Stochastic reversion · 1h | buy | META | 5.80 | — | rebalance up |
| 2026-10-08T13:55 | Stochastic reversion · 1h | buy | IWM | 5.75 | — | rebalance up |
| 2026-10-08T13:55 | Stochastic reversion · 1h | buy | ETH-USD | 6.46 | — | rebalance up |
| 2026-10-08T13:55 | Stochastic reversion · 1h | sell | NVDA | 8.11 | -0.03 | stop-loss |
| 2026-10-08T13:55 | VWAP momentum · 1h | sell | TQQQ | 5.89 | -0.06 | stop-loss |
| 2026-10-08T13:55 | Heikin-Ashi · 1h | sell | TQQQ | 12.58 | -0.13 | stop-loss |
| 2026-10-08T13:55 | MACD cross · 1h | buy | GOOGL | 4.83 | — | rebalance up |
| 2026-10-08T13:55 | MACD cross · 1h | sell | SQQQ | 4.83 | 0.04 | rebalance down |
| 2026-10-08T13:55 | Z-score reversion | sell | TSLA | 15.78 | -0.12 | stop-loss |
| 2026-10-08T13:55 | Bollinger reversion | buy | BITX | 3.17 | — | entry signal |
| 2026-10-08T13:55 | Bollinger reversion | sell | TSLA | 3.63 | -0.03 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 14:00:05.000142+00:00 -> 2026-10-08 14:10:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
