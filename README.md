# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T19:30:05.000128+00:00 · 15921 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.66 (-4.34%)

Closed trades 48, win rate 54.2%, fees £2.03, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.27 | +0.12 |
| MSFT | 38.26 | -0.03 |
| TECL | 19.12 | -0.01 |

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

Today: 36694 decisions in 2872 calls, $0.4530 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T19:30 | 1 / 19 / 10 | MSTR 15% |  |
| Breezy | 2026-10-08T19:30 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-08T19:30 | 3 / 26 / 1 | COIN 73% |  |

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
| 1 | VWAP reversion · 1h | reversion | 102.82 | 2.82 | 35 | 40.0 | -8.55 | -2.65 | -13.79 | 120 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.79 | 1.79 | 4 | 50.0 | 2.13 | 0.87 | -3.68 | 18 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 101.74 | 1.74 | 0 | — | -4.44 | -1.82 | -7.59 | 1 |
| 5 | Timing: Nasdaq FTD · TQQQ | daily | 100.92 | 0.92 | 0 | — | -6.34 | -1.10 | -15.27 | 1 |
| 6 | Hold SPY | benchmark | 100.70 | 0.70 | 0 | — | -0.09 | -0.01 | -3.66 | 1 |
| 7 | Timing: Nasdaq FTD · QQQ | daily | 100.59 | 0.59 | 0 | — | -1.68 | -0.91 | -5.09 | 1 |
| 8 | Copy: Congress Democrats (NANC) | copy | 100.59 | 0.58 | 0 | — | 1.02 | 0.52 | -3.62 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.56 | 0.56 | 5 | 40.0 | -3.74 | -1.22 | -9.74 | 25 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 100.12 | 0.12 | 0 | — | 0.92 | 0.42 | -5.18 | 1 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.36 | -0.64 | 5 | 40.0 | -1.31 | -1.38 | -2.95 | 21 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.20 | -1.52 | 86 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 98.69 | -1.31 | 0 | — | -5.19 | -2.48 | -5.49 | 1 |
| 17 | Copy: Insider buying | copy | 98.29 | -1.71 | 12 | 50.0 | -15.67 | -2.79 | -21.08 | 75 |
| 18 | Donchian 55/20 · 1h | breakout | 98.15 | -1.85 | 26 | 15.4 | 10.02 | 1.35 | -16.96 | 109 |
| 19 | Stochastic reversion · 1h | reversion | 97.83 | -2.17 | 76 | 50.0 | -12.84 | -2.59 | -15.16 | 345 |
| 20 | Three white soldiers · 1h | momentum | 97.74 | -2.26 | 5 | 0.0 | -2.81 | -2.21 | -3.95 | 25 |
| 21 | Hold BTC | benchmark | 97.69 | -2.31 | 0 | — | 25.39 | 3.08 | -8.68 | 1 |
| 22 | ADX DI cross · 1h | trend | 96.57 | -3.43 | 54 | 22.2 | -3.95 | -0.51 | -13.84 | 249 |
| 23 | Trend pullback · 1h | trend | 96.53 | -3.47 | 78 | 23.1 | -23.38 | -6.63 | -25.54 | 170 |
| 24 | Agent (rotation) | meta | 96.53 | -3.48 | 76 | 26.3 | 3.17 | 0.90 | -7.89 | 262 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.17 | -3.83 | 0 | — | 9.12 | 1.55 | -8.33 | 1 |
| 26 | EMA 20/50 cross · 1h | trend | 96.12 | -3.88 | 36 | 11.1 | 0.49 | 0.28 | -20.55 | 136 |
| 27 | Daily: Momentum burst | daily | 95.87 | -4.13 | 4 | 0.0 | -4.60 | -0.55 | -17.67 | 40 |
| 28 | Z-score reversion · 1h | reversion | 95.70 | -4.30 | 36 | 38.9 | -0.84 | -0.05 | -8.60 | 167 |
| 29 | Agent | meta | 95.66 | -4.34 | 48 | 54.2 | -11.35 | -5.70 | -11.74 | 245 |
| 30 | Daily: Bullish score | daily | 95.47 | -4.53 | 3 | 0.0 | -1.88 | -0.05 | -12.76 | 10 |
| 31 | MACD cross · 1h | trend | 95.39 | -4.61 | 105 | 22.9 | -18.41 | -2.97 | -19.87 | 460 |
| 32 | Parabolic SAR · 1h | trend | 95.02 | -4.98 | 82 | 22.0 | -5.67 | -0.61 | -20.87 | 291 |
| 33 | Squeeze breakout · 1h | breakout | 94.98 | -5.02 | 34 | 26.5 | 16.17 | 2.66 | -8.14 | 101 |
| 34 | Supertrend · 1h | trend | 94.45 | -5.55 | 51 | 13.7 | -4.28 | -0.43 | -18.09 | 210 |
| 35 | Agent (aggressive) | meta | 94.32 | -5.68 | 21 | 47.6 | -10.31 | -3.24 | -10.66 | 120 |
| 36 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.32 | 1.89 | -6.56 | 194 |
| 37 | Connors RSI(2) · 1h | reversion | 93.23 | -6.77 | 102 | 41.2 | -18.56 | -6.06 | -21.00 | 252 |
| 38 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.08 | 0.21 | -19.98 | 119 |
| 39 | Bollinger breakout · 1h | breakout | 92.75 | -7.25 | 65 | 30.8 | 6.96 | 1.05 | -12.06 | 285 |
| 40 | Agent (ML meta-label) | meta | 92.71 | -7.29 | 347 | 18.2 | -5.24 | -0.74 | -13.67 | 386 |
| 41 | RSI momentum · 1h | momentum | 92.52 | -7.48 | 60 | 15.0 | 3.68 | 0.64 | -16.64 | 217 |
| 42 | RSI(14) reversion · 1h | reversion | 92.34 | -7.66 | 26 | 26.9 | -4.53 | -0.92 | -9.03 | 145 |
| 43 | Volume breakout · 1h | breakout | 92.14 | -7.86 | 45 | 17.8 | 6.09 | 1.00 | -12.60 | 122 |
| 44 | Bollinger reversion · 1h | reversion | 91.35 | -8.65 | 68 | 33.8 | -22.49 | -5.41 | -23.96 | 319 |
| 45 | Triple EMA stack · 1h | trend | 91.29 | -8.71 | 68 | 16.2 | -11.36 | -1.27 | -25.74 | 238 |
| 46 | MFI reversion · 1h | reversion | 91.05 | -8.95 | 94 | 26.6 | -15.66 | -2.70 | -17.31 | 134 |
| 47 | Max aggression: 1-day momentum | meta | 90.92 | -9.09 | 9 | 33.3 | -24.33 | -1.25 | -37.31 | 43 |
| 48 | Opening range 30m | breakout | 90.83 | -9.17 | 127 | 18.1 | -17.53 | -5.31 | -18.09 | 569 |
| 49 | MACD zero-line · 1h | trend | 90.53 | -9.47 | 58 | 20.7 | -6.31 | -0.68 | -19.00 | 241 |
| 50 | Candlestick reversal · 1h ⏸ | reversion | 90.44 | -9.56 | 97 | 29.9 | -30.24 | -6.15 | -31.38 | 512 |
| 51 | Williams %R · 1h | reversion | 90.19 | -9.81 | 107 | 44.9 | -26.28 | -4.62 | -27.07 | 520 |
| 52 | Three white soldiers | momentum | 89.50 | -10.50 | 117 | 18.8 | -48.23 | -23.89 | -48.36 | 588 |
| 53 | EMA 9/21 cross · 1h | trend | 88.78 | -11.22 | 99 | 14.1 | -10.31 | -1.20 | -20.61 | 335 |
| 54 | Opening range 15m | breakout | 88.65 | -11.35 | 149 | 16.8 | -19.55 | -5.63 | -20.09 | 690 |
| 55 | VWAP momentum · 1h | momentum | 88.64 | -11.36 | 262 | 21.4 | -36.16 | -5.54 | -39.09 | 1264 |
| 56 | Donchian 20/10 · 1h | breakout | 88.46 | -11.54 | 55 | 20.0 | -2.36 | -0.08 | -17.36 | 220 |
| 57 | OBV trend · 1h | momentum | 88.29 | -11.71 | 137 | 17.5 | -15.11 | -1.79 | -28.16 | 318 |
| 58 | Heikin-Ashi · 1h | trend | 87.89 | -12.11 | 133 | 25.6 | -32.87 | -5.65 | -36.15 | 689 |
| 59 | CCI reversion · 1h | reversion | 87.88 | -12.12 | 91 | 40.7 | -10.75 | -1.48 | -14.35 | 414 |
| 60 | Keltner breakout · 1h | breakout | 87.84 | -12.16 | 41 | 19.5 | -9.46 | -1.02 | -24.33 | 225 |
| 61 | ROC + volume · 1h | momentum | 87.36 | -12.64 | 128 | 21.1 | -10.05 | -1.19 | -23.15 | 409 |
| 62 | Max aggression: 5-day momentum | meta | 83.26 | -16.74 | 7 | 28.6 | -27.45 | -2.45 | -34.64 | 30 |
| 63 | ROC + volume | momentum | 76.86 | -23.14 | 341 | 21.1 | -72.93 | -16.73 | -73.98 | 1635 |
| 64 | RSI(14) reversion ⏸ | reversion | 75.63 | -24.37 | 338 | 28.1 | -73.64 | -18.65 | -73.82 | 1501 |
| 65 | Squeeze breakout | breakout | 74.75 | -25.25 | 273 | 14.7 | -62.38 | -18.54 | -62.55 | 1210 |
| 66 | Donchian 55/20 | breakout | 73.07 | -26.93 | 274 | 16.8 | -68.20 | -14.70 | -68.46 | 1277 |
| 67 | Volume breakout | breakout | 72.70 | -27.30 | 223 | 13.0 | -63.45 | -18.20 | -63.62 | 898 |
| 68 | EMA 20/50 cross | trend | 72.35 | -27.65 | 283 | 18.0 | -77.33 | -15.50 | -77.68 | 1452 |
| 69 | VWAP reversion ⏸ | reversion | 68.88 | -31.12 | 376 | 25.5 | -72.00 | -16.30 | -72.34 | 1444 |
| 70 | Supertrend | trend | 67.54 | -32.46 | 403 | 18.6 | -86.73 | -21.49 | -87.04 | 1933 |
| 71 | Keltner breakout | breakout | 66.41 | -33.59 | 375 | 13.1 | -84.67 | -28.13 | -84.85 | 1856 |
| 72 | Ichimoku | trend | 64.61 | -35.39 | 345 | 9.3 | -81.50 | -23.28 | -81.66 | 1726 |
| 73 | AI bee: Bizzy | ai | 64.46 | -35.54 | 687 | 9.2 | — | — | — | — |
| 74 | MFI reversion ⏸ | reversion | 62.56 | -37.44 | 446 | 20.9 | -88.13 | -29.26 | -88.22 | 2117 |
| 75 | Z-score reversion ⏸ | reversion | 62.25 | -37.75 | 459 | 23.7 | -86.09 | -23.92 | -86.19 | 2096 |
| 76 | ADX DI cross | trend | 62.00 | -38.00 | 468 | 8.8 | -89.45 | -34.52 | -89.70 | 2125 |
| 77 | AI bee: Boozy | ai | 61.01 | -38.99 | 238 | 5.5 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 60.89 | -39.11 | 532 | 17.9 | -90.90 | -26.20 | -91.06 | 2643 |
| 79 | MACD zero-line | trend | 60.39 | -39.61 | 504 | 15.3 | -91.41 | -29.60 | -91.49 | 2357 |
| 80 | Trend pullback | trend | 59.64 | -40.36 | 506 | 15.6 | -90.67 | -27.73 | -90.71 | 2298 |
| 81 | RSI momentum | momentum | 59.37 | -40.63 | 498 | 16.5 | -90.24 | -25.53 | -90.40 | 2349 |
| 82 | Triple EMA stack | trend | 59.20 | -40.80 | 527 | 15.4 | -93.01 | -30.21 | -93.11 | 2584 |
| 83 | Bollinger breakout | breakout | 56.79 | -43.21 | 557 | 14.0 | -93.69 | -33.48 | -93.81 | 2808 |
| 84 | Consensus | meta | 56.52 | -43.48 | 517 | 10.3 | -94.26 | -25.58 | -94.27 | 2668 |
| 85 | EMA 9/21 cross | trend | 53.02 | -46.98 | 681 | 15.7 | -97.34 | -33.43 | -97.38 | 3528 |
| 86 | Connors RSI(2) | reversion | 52.75 | -47.25 | 717 | 21.1 | -96.23 | -32.26 | -96.24 | 3563 |
| 87 | Stochastic reversion | reversion | 51.19 | -48.81 | 852 | 22.8 | -95.75 | -35.16 | -95.80 | 4076 |
| 88 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.67 | -30.40 | -98.69 | 5321 |
| 89 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.25 | -36.26 | -96.28 | 3532 |
| 90 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.19 | -99.36 | 5682 |
| 91 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.07 | -99.73 | 6143 |
| 92 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.31 | -38.95 | -97.32 | 3630 |
| 93 | Bollinger reversion ⏸ | reversion | 50.09 | -49.91 | 772 | 17.5 | -95.93 | -34.14 | -95.96 | 3734 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -37.83 | -98.54 | 4705 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -41.00 | -99.53 | 6127 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.62 | -99.90 | 8253 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T19:30 | Agent (rotation) | buy | GOOGL | 8.04 | — | entry |
| 2026-10-08T19:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 99.41 | — | entry |
| 2026-10-08T19:30 | Consensus | buy | LABU | 14.13 | — | entry |
| 2026-10-08T19:30 | Consensus | buy | IWM | 14.13 | — | entry |
| 2026-10-08T19:30 | MFI reversion · 1h | buy | ETHU | 2.91 | — | entry signal |
| 2026-10-08T19:30 | MFI reversion · 1h | buy | COIN | 10.12 | — | entry signal |
| 2026-10-08T19:30 | MFI reversion · 1h | sell | TNA | 13.03 | 0.19 | exit signal |
| 2026-10-08T19:30 | CCI reversion · 1h | buy | TSLA | 7.89 | — | entry signal |
| 2026-10-08T19:30 | CCI reversion · 1h | buy | ETHU | 9.77 | — | entry signal |
| 2026-10-08T19:30 | CCI reversion · 1h | buy | BITX | 9.77 | — | entry signal |
| 2026-10-08T19:30 | CCI reversion · 1h | sell | TNA | 4.84 | 0.02 | rebalance down |
| 2026-10-08T19:30 | CCI reversion · 1h | sell | META | 7.94 | -0.05 | rebalance down |
| 2026-10-08T19:30 | CCI reversion · 1h | sell | LABU | 4.92 | 0.02 | rebalance down |
| 2026-10-08T19:30 | CCI reversion · 1h | sell | IWM | 4.84 | 0.00 | rebalance down |
| 2026-10-08T19:30 | CCI reversion · 1h | sell | COIN | 4.89 | 0.02 | rebalance down |
| 2026-10-08T19:30 | VWAP reversion · 1h | buy | GOOGL | 25.71 | — | entry signal |
| 2026-10-08T19:30 | Z-score reversion · 1h | buy | BITX | 3.86 | — | entry signal |
| 2026-10-08T19:30 | Connors RSI(2) · 1h | sell | TSLA | 6.69 | 0.01 | exit signal |
| 2026-10-08T19:30 | Connors RSI(2) · 1h | sell | META | 6.67 | 0.04 | exit signal |
| 2026-10-08T19:30 | Keltner breakout · 1h | buy | AAPL | 21.96 | — | entry signal |
| 2026-10-08T19:30 | Donchian 55/20 · 1h | buy | AAPL | 24.54 | — | entry signal |
| 2026-10-08T19:30 | Donchian 20/10 · 1h | buy | AAPL | 9.07 | — | entry signal |
| 2026-10-08T19:30 | Donchian 20/10 · 1h | sell | PLTR | 4.59 | 0.00 | rebalance down |
| 2026-10-08T19:30 | Donchian 20/10 · 1h | sell | GOOGL | 4.49 | -0.05 | rebalance down |
| 2026-10-08T19:30 | VWAP momentum · 1h | buy | TSLA | 11.07 | — | entry signal |
| 2026-10-08T19:30 | VWAP momentum · 1h | buy | MSTR | 11.08 | — | entry signal |
| 2026-10-08T19:30 | VWAP momentum · 1h | buy | COIN | 11.08 | — | entry signal |
| 2026-10-08T19:30 | VWAP momentum · 1h | sell | TNA | 6.58 | -0.00 | rebalance down |
| 2026-10-08T19:30 | VWAP momentum · 1h | sell | SQQQ | 6.70 | 0.18 | rebalance down |
| 2026-10-08T19:30 | VWAP momentum · 1h | sell | LABU | 6.68 | 0.03 | rebalance down |
| 2026-10-08T19:30 | VWAP momentum · 1h | sell | IWM | 6.59 | -0.00 | rebalance down |
| 2026-10-08T19:30 | VWAP momentum · 1h | sell | AAPL | 6.68 | 0.08 | rebalance down |
| 2026-10-08T19:30 | Heikin-Ashi · 1h | buy | TNA | 13.40 | — | entry signal |
| 2026-10-08T19:30 | Heikin-Ashi · 1h | buy | LABU | 17.58 | — | entry signal |
| 2026-10-08T19:30 | Heikin-Ashi · 1h | buy | IWM | 17.58 | — | entry signal |
| 2026-10-08T19:30 | Heikin-Ashi · 1h | sell | AAPL | 4.80 | 0.05 | rebalance down |
| 2026-10-08T19:30 | MACD cross · 1h | buy | LABU | 23.85 | — | entry signal |
| 2026-10-08T19:30 | EMA 20/50 cross · 1h | buy | UPRO | 5.37 | — | rebalance up |
| 2026-10-08T19:30 | EMA 20/50 cross · 1h | buy | TECL | 5.20 | — | rebalance up |
| 2026-10-08T19:30 | EMA 20/50 cross · 1h | buy | SPY | 4.81 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 19:30:05.000128+00:00 -> 2026-10-08 19:40:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
