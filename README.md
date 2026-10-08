# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T22:01:05.000131+00:00 · 16048 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.72 (-4.28%)

Closed trades 50, win rate 54.0%, fees £2.06, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 19.15 | +0.00 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-08 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, BORR 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-08)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 22.10 · VIX 15.57 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.3, AMD 7.1, TECL 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 40558 decisions in 3253 calls, $0.5017 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T22:01 | 2 / 3 / 0 | SOXL 15%, AMD 14% |  |
| Breezy | 2026-10-08T22:01 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T22:01 | 3 / 2 / 0 | COIN 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| VWAP reversion | MSFT | 1.92 | +0.90% | 3 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.08 | 3.08 | 35 | 40.0 | -8.30 | -2.56 | -13.79 | 120 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 101.44 | 1.44 | 0 | — | -4.29 | -1.80 | -7.31 | 1 |
| 5 | Timing: Nasdaq FTD · TQQQ | daily | 101.29 | 1.29 | 0 | — | -6.17 | -1.08 | -15.27 | 1 |
| 6 | Hold SPY | benchmark | 100.74 | 0.74 | 0 | — | -0.11 | -0.02 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.70 | 0.70 | 0 | — | 1.17 | 0.59 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 100.69 | 0.69 | 0 | — | -1.64 | -0.90 | -5.09 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -3.83 | -1.26 | -9.74 | 25 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.79 | -0.21 | 0 | — | 0.61 | 0.31 | -5.18 | 1 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.41 | -1.48 | -3.04 | 21 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.20 | -1.52 | 86 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 98.79 | -1.21 | 0 | — | -5.06 | -2.43 | -5.36 | 1 |
| 17 | Copy: Insider buying | copy | 98.50 | -1.50 | 12 | 50.0 | -15.22 | -2.67 | -21.08 | 75 |
| 18 | Stochastic reversion · 1h | reversion | 98.16 | -1.84 | 76 | 50.0 | -12.73 | -2.57 | -15.23 | 345 |
| 19 | Donchian 55/20 · 1h | breakout | 98.12 | -1.88 | 26 | 15.4 | 10.01 | 1.35 | -16.96 | 109 |
| 20 | Three white soldiers · 1h | momentum | 97.70 | -2.30 | 5 | 0.0 | -2.87 | -2.25 | -4.07 | 26 |
| 21 | Hold BTC | benchmark | 97.68 | -2.33 | 0 | — | 25.51 | 3.09 | -8.68 | 1 |
| 22 | ADX DI cross · 1h | trend | 96.58 | -3.42 | 54 | 22.2 | -5.07 | -0.74 | -13.84 | 251 |
| 23 | Agent (rotation) | meta | 96.58 | -3.42 | 77 | 27.3 | 5.82 | 1.49 | -8.33 | 252 |
| 24 | Trend pullback · 1h | trend | 96.55 | -3.44 | 78 | 23.1 | -23.76 | -6.76 | -25.53 | 172 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.39 | -3.61 | 0 | — | 8.88 | 1.51 | -8.33 | 1 |
| 26 | EMA 20/50 cross · 1h | trend | 96.22 | -3.78 | 36 | 11.1 | 0.50 | 0.28 | -20.52 | 135 |
| 27 | Daily: Momentum burst | daily | 96.00 | -4.00 | 4 | 0.0 | -4.75 | -0.57 | -17.67 | 40 |
| 28 | Z-score reversion · 1h | reversion | 95.87 | -4.13 | 36 | 38.9 | -0.72 | -0.02 | -8.60 | 170 |
| 29 | Daily: Bullish score | daily | 95.81 | -4.19 | 3 | 0.0 | -1.35 | 0.02 | -12.76 | 10 |
| 30 | Agent | meta | 95.72 | -4.28 | 50 | 54.0 | -10.84 | -5.85 | -11.29 | 249 |
| 31 | Parabolic SAR · 1h | trend | 95.15 | -4.85 | 82 | 22.0 | -5.24 | -0.55 | -20.80 | 291 |
| 32 | MACD cross · 1h | trend | 95.13 | -4.87 | 105 | 22.9 | -18.68 | -3.02 | -19.87 | 462 |
| 33 | Squeeze breakout · 1h | breakout | 94.90 | -5.10 | 34 | 26.5 | 15.40 | 2.54 | -8.14 | 102 |
| 34 | Supertrend · 1h | trend | 94.44 | -5.56 | 51 | 13.7 | -4.58 | -0.47 | -18.09 | 209 |
| 35 | Agent (aggressive) | meta | 94.25 | -5.75 | 22 | 45.5 | -12.44 | -3.66 | -12.72 | 121 |
| 36 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.25 | 1.87 | -6.56 | 194 |
| 37 | Connors RSI(2) · 1h | reversion | 93.45 | -6.55 | 102 | 41.2 | -18.29 | -6.07 | -20.97 | 252 |
| 38 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.08 | 0.21 | -19.98 | 119 |
| 39 | Agent (ML meta-label) | meta | 92.65 | -7.35 | 350 | 18.6 | -5.26 | -0.88 | -13.16 | 402 |
| 40 | Bollinger breakout · 1h | breakout | 92.58 | -7.42 | 65 | 30.8 | 6.44 | 0.99 | -12.06 | 285 |
| 41 | RSI momentum · 1h | momentum | 92.45 | -7.55 | 60 | 15.0 | 1.31 | 0.36 | -16.65 | 218 |
| 42 | RSI(14) reversion · 1h | reversion | 92.35 | -7.65 | 26 | 26.9 | -4.47 | -0.87 | -9.03 | 155 |
| 43 | Volume breakout · 1h | breakout | 92.16 | -7.84 | 45 | 17.8 | 6.13 | 1.00 | -12.60 | 122 |
| 44 | Bollinger reversion · 1h | reversion | 91.63 | -8.37 | 68 | 33.8 | -22.03 | -5.38 | -23.89 | 319 |
| 45 | Max aggression: 1-day momentum | meta | 91.33 | -8.66 | 9 | 33.3 | -23.96 | -1.23 | -37.31 | 43 |
| 46 | Triple EMA stack · 1h | trend | 91.24 | -8.76 | 68 | 16.2 | -10.86 | -1.19 | -25.80 | 237 |
| 47 | MFI reversion · 1h | reversion | 90.98 | -9.02 | 96 | 28.1 | -14.84 | -2.58 | -16.99 | 134 |
| 48 | Opening range 30m | breakout | 90.76 | -9.23 | 131 | 20.6 | -17.37 | -5.28 | -17.94 | 562 |
| 49 | Candlestick reversal · 1h ⏸ | reversion | 90.44 | -9.56 | 97 | 29.9 | -30.05 | -6.05 | -31.27 | 506 |
| 50 | MACD zero-line · 1h | trend | 90.37 | -9.63 | 58 | 20.7 | -6.40 | -0.69 | -19.00 | 241 |
| 51 | Williams %R · 1h | reversion | 90.25 | -9.75 | 107 | 44.9 | -26.90 | -4.76 | -27.42 | 515 |
| 52 | Three white soldiers | momentum | 89.43 | -10.57 | 120 | 19.2 | -48.39 | -23.89 | -48.49 | 588 |
| 53 | Opening range 15m | breakout | 88.59 | -11.41 | 153 | 19.0 | -19.52 | -5.62 | -20.06 | 683 |
| 54 | EMA 9/21 cross · 1h | trend | 88.56 | -11.44 | 99 | 14.1 | -11.10 | -1.31 | -20.61 | 334 |
| 55 | Donchian 20/10 · 1h | breakout | 88.39 | -11.61 | 55 | 20.0 | -1.95 | -0.03 | -17.36 | 219 |
| 56 | OBV trend · 1h | momentum | 88.30 | -11.70 | 139 | 18.0 | -15.12 | -1.73 | -29.61 | 313 |
| 57 | VWAP momentum · 1h | momentum | 88.28 | -11.72 | 262 | 21.4 | -36.63 | -5.59 | -39.09 | 1260 |
| 58 | CCI reversion · 1h | reversion | 87.72 | -12.28 | 91 | 40.7 | -11.30 | -1.55 | -14.35 | 419 |
| 59 | Keltner breakout · 1h | breakout | 87.68 | -12.32 | 41 | 19.5 | -11.06 | -1.28 | -24.35 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 87.63 | -12.37 | 133 | 25.6 | -33.10 | -5.70 | -36.32 | 694 |
| 61 | ROC + volume · 1h | momentum | 87.20 | -12.80 | 128 | 21.1 | -10.10 | -1.22 | -23.15 | 408 |
| 62 | Max aggression: 5-day momentum | meta | 83.65 | -16.36 | 7 | 28.6 | -27.10 | -2.41 | -34.64 | 30 |
| 63 | ROC + volume | momentum | 76.94 | -23.06 | 349 | 21.2 | -72.87 | -16.67 | -73.89 | 1634 |
| 64 | RSI(14) reversion ⏸ | reversion | 75.63 | -24.37 | 338 | 28.1 | -73.60 | -18.76 | -73.80 | 1504 |
| 65 | Squeeze breakout | breakout | 74.72 | -25.28 | 275 | 14.9 | -62.25 | -18.46 | -62.41 | 1210 |
| 66 | Volume breakout | breakout | 72.74 | -27.26 | 224 | 13.4 | -63.51 | -18.27 | -63.62 | 897 |
| 67 | Donchian 55/20 | breakout | 72.71 | -27.29 | 278 | 17.3 | -68.40 | -14.79 | -68.49 | 1281 |
| 68 | EMA 20/50 cross | trend | 72.17 | -27.83 | 287 | 18.5 | -77.52 | -15.64 | -77.62 | 1452 |
| 69 | VWAP reversion ⏸ | reversion | 68.88 | -31.12 | 376 | 25.5 | -71.71 | -16.24 | -72.16 | 1437 |
| 70 | Supertrend | trend | 67.73 | -32.27 | 410 | 20.0 | -86.68 | -21.44 | -86.98 | 1928 |
| 71 | Keltner breakout | breakout | 66.36 | -33.64 | 383 | 13.8 | -84.60 | -28.12 | -84.77 | 1856 |
| 72 | Ichimoku | trend | 64.57 | -35.43 | 348 | 9.5 | -81.59 | -23.36 | -81.72 | 1731 |
| 73 | AI bee: Bizzy | ai | 63.95 | -36.05 | 695 | 9.2 | — | — | — | — |
| 74 | MFI reversion ⏸ | reversion | 62.56 | -37.44 | 446 | 20.9 | -88.05 | -29.14 | -88.15 | 2122 |
| 75 | Z-score reversion ⏸ | reversion | 62.25 | -37.75 | 459 | 23.7 | -86.07 | -23.90 | -86.17 | 2095 |
| 76 | ADX DI cross | trend | 62.02 | -37.98 | 478 | 10.0 | -89.39 | -34.19 | -89.65 | 2122 |
| 77 | Donchian 20/10 | breakout | 60.93 | -39.07 | 541 | 18.5 | -90.82 | -26.09 | -91.02 | 2638 |
| 78 | MACD zero-line | trend | 60.23 | -39.77 | 515 | 16.1 | -91.35 | -29.66 | -91.41 | 2350 |
| 79 | AI bee: Boozy | ai | 60.03 | -39.97 | 239 | 5.4 | — | — | — | — |
| 80 | Trend pullback | trend | 59.63 | -40.37 | 507 | 15.8 | -90.64 | -27.63 | -90.67 | 2290 |
| 81 | RSI momentum | momentum | 59.53 | -40.47 | 509 | 17.7 | -90.20 | -25.50 | -90.38 | 2344 |
| 82 | Triple EMA stack | trend | 58.95 | -41.05 | 535 | 15.9 | -93.05 | -30.33 | -93.12 | 2587 |
| 83 | Bollinger breakout | breakout | 56.72 | -43.28 | 568 | 15.0 | -93.63 | -33.25 | -93.75 | 2805 |
| 84 | Consensus | meta | 55.92 | -44.08 | 526 | 10.5 | -94.23 | -25.50 | -94.24 | 2661 |
| 85 | EMA 9/21 cross | trend | 52.99 | -47.01 | 691 | 16.6 | -97.31 | -33.13 | -97.35 | 3523 |
| 86 | Connors RSI(2) | reversion | 52.75 | -47.25 | 718 | 21.2 | -96.23 | -32.24 | -96.23 | 3561 |
| 87 | Stochastic reversion | reversion | 51.30 | -48.70 | 857 | 23.1 | -95.68 | -34.59 | -95.74 | 4065 |
| 88 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.67 | -30.47 | -98.68 | 5306 |
| 89 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -36.46 | -96.28 | 3538 |
| 90 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.93 | -99.35 | 5674 |
| 91 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.55 | -99.73 | 6132 |
| 92 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.32 | -38.92 | -97.33 | 3630 |
| 93 | Bollinger reversion ⏸ | reversion | 50.09 | -49.91 | 772 | 17.5 | -95.90 | -33.82 | -95.93 | 3728 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -37.49 | -98.52 | 4701 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.50 | -99.53 | 6118 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.34 | -99.90 | 8240 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T22:00 | Consensus | buy | DOGE-USD | 13.99 | — | entry |
| 2026-10-08T22:00 | MACD cross · 1h | buy | BTC-USD | 13.21 | — | entry signal |
| 2026-10-08T21:50 | Keltner breakout | sell | DOGE-USD | 13.24 | -0.05 | exit signal |
| 2026-10-08T21:50 | Donchian 20/10 | sell | XRP-USD | 15.14 | -0.04 | exit signal |
| 2026-10-08T21:50 | ADX DI cross | buy | XRP-USD | 3.10 | — | rebalance up |
| 2026-10-08T21:50 | Triple EMA stack | buy | XRP-USD | 2.96 | — | rebalance up |
| 2026-10-08T21:50 | Triple EMA stack | buy | SOL-USD | 5.82 | — | rebalance up |
| 2026-10-08T21:50 | Triple EMA stack | sell | BTC-USD | 11.72 | -0.10 | exit signal |
| 2026-10-08T21:50 | EMA 9/21 cross | buy | XRP-USD | 2.70 | — | rebalance up |
| 2026-10-08T21:50 | EMA 9/21 cross | sell | BTC-USD | 10.52 | -0.06 | exit signal |
| 2026-10-08T21:47 | AI bee: Bizzy | sell | SOL-USD | 9.16 | -0.07 | Jev: sell (sell p=0.74) after 10 min |
| 2026-10-08T21:45 | Consensus | sell | DOGE-USD | 13.94 | -0.10 | target is flat |
| 2026-10-08T21:45 | Keltner breakout | sell | XRP-USD | 16.52 | 0.01 | stop-loss |
| 2026-10-08T21:45 | Bollinger breakout | sell | DOGE-USD | 14.17 | 0.02 | exit signal |
| 2026-10-08T21:45 | Donchian 55/20 | sell | XRP-USD | 18.00 | -0.20 | stop-loss |
| 2026-10-08T21:45 | ROC + volume | sell | XRP-USD | 19.14 | -0.01 | exit signal |
| 2026-10-08T21:45 | Triple EMA stack | buy | SOL-USD | 2.94 | — | rebalance up |
| 2026-10-08T21:45 | Triple EMA stack | sell | ETH-USD | 2.94 | -0.01 | rebalance down |
| 2026-10-08T21:37 | AI bee: Bizzy | buy | SOL-USD | 9.23 | — | Jev: buy (buy p=0.58) |
| 2026-10-08T21:35 | Bollinger breakout | sell | XRP-USD | 14.12 | 0.00 | exit signal |
| 2026-10-08T21:32 | AI bee: Bizzy | sell | XRP-USD | 9.59 | -0.09 | Jev: sell (sell p=0.88) after 12 min |
| 2026-10-08T21:30 | Consensus | sell | XRP-USD | 13.80 | -0.13 | target is flat |
| 2026-10-08T21:30 | ROC + volume | sell | DOGE-USD | 15.37 | -0.02 | exit signal |
| 2026-10-08T21:27 | AI bee: Bizzy | sell | DOGE-USD | 9.61 | -0.07 | Jev: sell (sell p=0.83) after 12 min |
| 2026-10-08T21:25 | ADX DI cross | sell | BTC-USD | 12.21 | -0.08 | exit signal |
| 2026-10-08T21:20 | AI bee: Bizzy | buy | XRP-USD | 9.68 | — | Jev: buy (buy p=0.60) |
| 2026-10-08T21:20 | Consensus | buy | XRP-USD | 13.94 | — | entry |
| 2026-10-08T21:20 | Three white soldiers | buy | SOL-USD | 22.35 | — | entry signal |
| 2026-10-08T21:20 | Donchian 55/20 | buy | XRP-USD | 18.20 | — | entry signal |
| 2026-10-08T21:20 | ROC + volume | buy | ETH-USD | 3.85 | — | rebalance up |
| 2026-10-08T21:15 | AI bee: Bizzy | buy | DOGE-USD | 9.69 | — | Jev: buy (buy p=0.60) |
| 2026-10-08T21:15 | ADX DI cross | buy | BTC-USD | 12.29 | — | entry signal |
| 2026-10-08T21:15 | ADX DI cross | sell | XRP-USD | 3.09 | -0.00 | rebalance down |
| 2026-10-08T21:07 | AI bee: Bizzy | sell | SOL-USD | 9.31 | -0.07 | Jev: sell (sell p=0.63) after 12 min |
| 2026-10-08T21:05 | Consensus | sell | XRP-USD | 13.94 | -0.10 | target is flat |
| 2026-10-08T21:05 | Three white soldiers | sell | ETH-USD | 22.36 | -0.02 | exit signal |
| 2026-10-08T21:05 | Keltner breakout | buy | XRP-USD | 3.34 | — | rebalance up |
| 2026-10-08T21:05 | Keltner breakout | sell | BTC-USD | 13.19 | -0.07 | exit signal |
| 2026-10-08T21:05 | Donchian 20/10 | buy | XRP-USD | 3.07 | — | rebalance up |
| 2026-10-08T21:05 | Donchian 20/10 | sell | BTC-USD | 12.10 | -0.07 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 22:01:05.000131+00:00 -> 2026-10-08 22:11:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
