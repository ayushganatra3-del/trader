# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T22:30:05.000125+00:00 · 16077 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.72 (-4.28%)

Closed trades 50, win rate 54.0%, fees £2.06, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 19.14 | -0.00 |

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

Today: 40993 decisions in 3340 calls, $0.5078 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T22:30 | 0 / 1 / 4 | SOXL 15%, AMD 14% |  |
| Breezy | 2026-10-08T22:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T22:30 | 0 / 3 / 2 | COIN 73% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.01 | 3.02 | 35 | 40.0 | -8.01 | -2.45 | -13.79 | 119 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 101.42 | 1.42 | 0 | — | -4.29 | -1.80 | -7.31 | 1 |
| 5 | Timing: Nasdaq FTD · TQQQ | daily | 101.27 | 1.27 | 0 | — | -6.17 | -1.08 | -15.27 | 1 |
| 6 | Hold SPY | benchmark | 100.72 | 0.72 | 0 | — | -0.11 | -0.02 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.68 | 0.68 | 0 | — | 1.17 | 0.59 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 100.67 | 0.67 | 0 | — | -1.64 | -0.90 | -5.09 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -3.83 | -1.26 | -9.74 | 25 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.77 | -0.23 | 0 | — | 0.61 | 0.31 | -5.18 | 1 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.41 | -1.48 | -3.04 | 21 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.20 | -1.52 | 86 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 98.77 | -1.23 | 0 | — | -5.06 | -2.43 | -5.36 | 1 |
| 17 | Copy: Insider buying | copy | 98.48 | -1.52 | 12 | 50.0 | -15.22 | -2.67 | -21.08 | 75 |
| 18 | Stochastic reversion · 1h | reversion | 98.11 | -1.89 | 76 | 50.0 | -12.76 | -2.58 | -15.25 | 345 |
| 19 | Donchian 55/20 · 1h | breakout | 98.11 | -1.89 | 26 | 15.4 | 10.01 | 1.35 | -16.96 | 109 |
| 20 | Hold BTC | benchmark | 97.76 | -2.24 | 0 | — | 25.63 | 3.11 | -8.68 | 1 |
| 21 | Three white soldiers · 1h | momentum | 97.69 | -2.31 | 5 | 0.0 | -2.87 | -2.25 | -4.07 | 26 |
| 22 | ADX DI cross · 1h | trend | 96.57 | -3.42 | 54 | 22.2 | -5.01 | -0.73 | -13.84 | 251 |
| 23 | Agent (rotation) | meta | 96.56 | -3.44 | 77 | 27.3 | 4.63 | 1.20 | -8.33 | 264 |
| 24 | Trend pullback · 1h | trend | 96.55 | -3.45 | 78 | 23.1 | -23.76 | -6.76 | -25.53 | 172 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.37 | -3.63 | 0 | — | 8.88 | 1.51 | -8.33 | 1 |
| 26 | EMA 20/50 cross · 1h | trend | 96.20 | -3.80 | 36 | 11.1 | 0.50 | 0.28 | -20.52 | 135 |
| 27 | Daily: Momentum burst | daily | 96.00 | -4.00 | 4 | 0.0 | -4.75 | -0.57 | -17.67 | 40 |
| 28 | Z-score reversion · 1h | reversion | 95.87 | -4.13 | 36 | 38.9 | -0.74 | -0.03 | -8.60 | 170 |
| 29 | Daily: Bullish score | daily | 95.79 | -4.21 | 3 | 0.0 | -1.35 | 0.02 | -12.76 | 10 |
| 30 | Agent | meta | 95.72 | -4.28 | 50 | 54.0 | -10.67 | -5.76 | -11.24 | 250 |
| 31 | Parabolic SAR · 1h | trend | 95.14 | -4.86 | 82 | 22.0 | -5.24 | -0.55 | -20.80 | 291 |
| 32 | MACD cross · 1h | trend | 95.12 | -4.88 | 105 | 22.9 | -18.64 | -3.01 | -19.87 | 462 |
| 33 | Squeeze breakout · 1h | breakout | 94.89 | -5.11 | 34 | 26.5 | 15.40 | 2.54 | -8.14 | 102 |
| 34 | Supertrend · 1h | trend | 94.42 | -5.58 | 51 | 13.7 | -4.58 | -0.47 | -18.09 | 209 |
| 35 | Agent (aggressive) | meta | 94.25 | -5.75 | 22 | 45.5 | -9.50 | -3.81 | -9.80 | 114 |
| 36 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.31 | 1.89 | -6.52 | 194 |
| 37 | Connors RSI(2) · 1h | reversion | 93.43 | -6.57 | 102 | 41.2 | -18.29 | -6.07 | -20.97 | 252 |
| 38 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.08 | 0.21 | -19.98 | 119 |
| 39 | Agent (ML meta-label) | meta | 92.62 | -7.38 | 350 | 18.6 | -3.13 | -0.42 | -13.37 | 397 |
| 40 | Bollinger breakout · 1h | breakout | 92.58 | -7.42 | 65 | 30.8 | 6.44 | 0.99 | -12.06 | 285 |
| 41 | RSI momentum · 1h | momentum | 92.43 | -7.57 | 60 | 15.0 | 1.28 | 0.36 | -16.65 | 218 |
| 42 | RSI(14) reversion · 1h | reversion | 92.33 | -7.67 | 26 | 26.9 | -4.24 | -0.82 | -9.03 | 153 |
| 43 | Volume breakout · 1h | breakout | 92.15 | -7.85 | 45 | 17.8 | 6.47 | 1.05 | -12.60 | 121 |
| 44 | Bollinger reversion · 1h | reversion | 91.61 | -8.39 | 68 | 33.8 | -22.05 | -5.38 | -23.89 | 319 |
| 45 | Max aggression: 1-day momentum | meta | 91.32 | -8.68 | 9 | 33.3 | -23.96 | -1.23 | -37.31 | 43 |
| 46 | Triple EMA stack · 1h | trend | 91.23 | -8.77 | 68 | 16.2 | -10.71 | -1.17 | -25.80 | 236 |
| 47 | MFI reversion · 1h | reversion | 90.94 | -9.06 | 96 | 28.1 | -15.41 | -2.67 | -16.99 | 129 |
| 48 | Opening range 30m | breakout | 90.76 | -9.23 | 131 | 20.6 | -17.37 | -5.28 | -17.94 | 562 |
| 49 | Candlestick reversal · 1h ⏸ | reversion | 90.44 | -9.56 | 97 | 29.9 | -29.85 | -5.96 | -31.07 | 504 |
| 50 | MACD zero-line · 1h | trend | 90.36 | -9.64 | 58 | 20.7 | -6.41 | -0.69 | -19.00 | 241 |
| 51 | Williams %R · 1h | reversion | 90.23 | -9.77 | 107 | 44.9 | -26.91 | -4.76 | -27.42 | 515 |
| 52 | Three white soldiers | momentum | 89.28 | -10.72 | 121 | 19.0 | -48.50 | -23.92 | -48.51 | 587 |
| 53 | Opening range 15m | breakout | 88.59 | -11.41 | 153 | 19.0 | -19.49 | -5.61 | -20.03 | 683 |
| 54 | EMA 9/21 cross · 1h | trend | 88.55 | -11.45 | 99 | 14.1 | -10.81 | -1.27 | -20.61 | 333 |
| 55 | Donchian 20/10 · 1h | breakout | 88.37 | -11.63 | 55 | 20.0 | -1.95 | -0.03 | -17.36 | 219 |
| 56 | OBV trend · 1h | momentum | 88.29 | -11.71 | 139 | 18.0 | -15.69 | -1.81 | -30.22 | 319 |
| 57 | VWAP momentum · 1h | momentum | 88.26 | -11.74 | 262 | 21.4 | -36.74 | -5.61 | -39.20 | 1261 |
| 58 | CCI reversion · 1h | reversion | 87.71 | -12.29 | 91 | 40.7 | -11.33 | -1.56 | -14.35 | 419 |
| 59 | Keltner breakout · 1h | breakout | 87.67 | -12.33 | 41 | 19.5 | -11.23 | -1.30 | -24.35 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 87.62 | -12.38 | 133 | 25.6 | -33.19 | -5.72 | -36.31 | 694 |
| 61 | ROC + volume · 1h | momentum | 87.19 | -12.81 | 128 | 21.1 | -11.04 | -1.36 | -23.22 | 407 |
| 62 | Max aggression: 5-day momentum | meta | 83.63 | -16.37 | 7 | 28.6 | -27.10 | -2.41 | -34.64 | 30 |
| 63 | ROC + volume | momentum | 76.76 | -23.24 | 350 | 21.4 | -72.78 | -16.63 | -73.75 | 1644 |
| 64 | RSI(14) reversion ⏸ | reversion | 75.63 | -24.37 | 338 | 28.1 | -73.63 | -18.78 | -73.82 | 1505 |
| 65 | Squeeze breakout | breakout | 74.62 | -25.38 | 276 | 15.2 | -62.25 | -18.46 | -62.36 | 1209 |
| 66 | Volume breakout | breakout | 72.74 | -27.26 | 224 | 13.4 | -63.54 | -18.31 | -63.65 | 898 |
| 67 | Donchian 55/20 | breakout | 72.59 | -27.41 | 278 | 17.3 | -68.44 | -14.80 | -68.49 | 1281 |
| 68 | EMA 20/50 cross | trend | 72.11 | -27.89 | 287 | 18.5 | -77.51 | -15.62 | -77.59 | 1451 |
| 69 | VWAP reversion ⏸ | reversion | 68.88 | -31.12 | 376 | 25.5 | -71.82 | -16.19 | -72.25 | 1434 |
| 70 | Supertrend | trend | 67.68 | -32.32 | 410 | 20.0 | -86.69 | -21.45 | -86.98 | 1929 |
| 71 | Keltner breakout | breakout | 66.24 | -33.76 | 384 | 13.8 | -84.65 | -28.21 | -84.79 | 1857 |
| 72 | Ichimoku | trend | 64.53 | -35.48 | 348 | 9.5 | -81.60 | -23.37 | -81.72 | 1732 |
| 73 | AI bee: Bizzy | ai | 63.88 | -36.12 | 696 | 9.2 | — | — | — | — |
| 74 | MFI reversion ⏸ | reversion | 62.56 | -37.44 | 446 | 20.9 | -87.97 | -29.08 | -88.07 | 2127 |
| 75 | Z-score reversion ⏸ | reversion | 62.25 | -37.75 | 459 | 23.7 | -86.05 | -23.88 | -86.16 | 2094 |
| 76 | ADX DI cross | trend | 61.97 | -38.03 | 478 | 10.0 | -89.40 | -34.23 | -89.65 | 2122 |
| 77 | Donchian 20/10 | breakout | 60.85 | -39.15 | 541 | 18.5 | -90.86 | -26.16 | -91.02 | 2639 |
| 78 | MACD zero-line | trend | 60.23 | -39.77 | 515 | 16.1 | -91.33 | -29.61 | -91.39 | 2348 |
| 79 | AI bee: Boozy | ai | 60.03 | -39.97 | 239 | 5.4 | — | — | — | — |
| 80 | Trend pullback | trend | 59.63 | -40.37 | 507 | 15.8 | -90.64 | -27.63 | -90.67 | 2290 |
| 81 | RSI momentum | momentum | 59.48 | -40.52 | 509 | 17.7 | -90.21 | -25.52 | -90.38 | 2344 |
| 82 | Triple EMA stack | trend | 58.84 | -41.16 | 535 | 15.9 | -93.06 | -30.36 | -93.12 | 2588 |
| 83 | Bollinger breakout | breakout | 56.52 | -43.48 | 569 | 15.1 | -93.67 | -33.34 | -93.76 | 2807 |
| 84 | Consensus | meta | 55.75 | -44.25 | 528 | 10.4 | -94.28 | -25.59 | -94.28 | 2659 |
| 85 | EMA 9/21 cross | trend | 52.90 | -47.09 | 691 | 16.6 | -97.30 | -33.08 | -97.35 | 3522 |
| 86 | Connors RSI(2) | reversion | 52.75 | -47.25 | 718 | 21.2 | -96.23 | -32.24 | -96.23 | 3561 |
| 87 | Stochastic reversion | reversion | 51.30 | -48.70 | 857 | 23.1 | -95.68 | -34.59 | -95.74 | 4065 |
| 88 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -30.30 | -98.67 | 5319 |
| 89 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -36.43 | -96.27 | 3552 |
| 90 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.85 | -99.35 | 5668 |
| 91 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.54 | -99.73 | 6133 |
| 92 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -38.91 | -97.35 | 3634 |
| 93 | Bollinger reversion ⏸ | reversion | 50.09 | -49.91 | 772 | 17.5 | -95.90 | -33.81 | -95.93 | 3728 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -37.47 | -98.52 | 4700 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.50 | -99.53 | 6118 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.06 | -99.90 | 8238 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T22:30 | AI bee: Bizzy | sell | XRP-USD | 8.87 | -0.07 | Jev: sell (sell p=0.88) after 11 min |
| 2026-10-08T22:30 | Three white soldiers | sell | SOL-USD | 22.24 | -0.11 | exit signal |
| 2026-10-08T22:30 | Ichimoku | buy | BTC-USD | 16.14 | — | entry signal |
| 2026-10-08T22:25 | Consensus | sell | ETH-USD | 14.03 | -0.04 | target is flat |
| 2026-10-08T22:25 | Consensus | sell | DOGE-USD | 13.91 | -0.08 | target is flat |
| 2026-10-08T22:25 | Squeeze breakout | sell | ETH-USD | 18.77 | 0.14 | exit signal |
| 2026-10-08T22:25 | Keltner breakout | sell | ETH-USD | 13.26 | -0.03 | exit signal |
| 2026-10-08T22:25 | Bollinger breakout | sell | ETH-USD | 14.18 | 0.02 | exit signal |
| 2026-10-08T22:25 | ROC + volume | sell | ETH-USD | 19.18 | 0.02 | exit signal |
| 2026-10-08T22:20 | Bollinger breakout | buy | XRP-USD | 14.17 | — | entry signal |
| 2026-10-08T22:20 | Triple EMA stack | buy | BTC-USD | 2.94 | — | rebalance up |
| 2026-10-08T22:20 | Triple EMA stack | sell | DOGE-USD | 2.94 | -0.00 | rebalance down |
| 2026-10-08T22:19 | AI bee: Bizzy | buy | XRP-USD | 8.94 | — | Jev: buy (buy p=0.56) |
| 2026-10-08T22:15 | Triple EMA stack | buy | BTC-USD | 2.95 | — | rebalance up |
| 2026-10-08T22:15 | Triple EMA stack | sell | SOL-USD | 2.95 | 0.00 | rebalance down |
| 2026-10-08T22:10 | Triple EMA stack | buy | BTC-USD | 5.90 | — | entry signal |
| 2026-10-08T22:10 | Triple EMA stack | sell | XRP-USD | 2.95 | -0.01 | rebalance down |
| 2026-10-08T22:10 | EMA 9/21 cross | buy | BTC-USD | 10.48 | — | entry signal |
| 2026-10-08T22:10 | EMA 9/21 cross | sell | XRP-USD | 2.66 | -0.01 | rebalance down |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 22:30:05.000125+00:00 -> 2026-10-08 22:40:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
