# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T11:00:05.000148+00:00 · 16667 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.71 (-4.29%)

Closed trades 50, win rate 54.0%, fees £2.06, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 19.13 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-09 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-08)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 21.98 · VIX 15.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.3, AMD 7.1, TECL 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 7875 decisions in 1575 calls, $0.1101 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T11:00 | 0 / 3 / 2 | SOXL 15%, AMD 15% |  |
| Breezy | 2026-10-09T11:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-09T11:00 | 3 / 2 / 0 | COIN 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.00 | 3.00 | 36 | 41.7 | -8.13 | -2.48 | -13.79 | 120 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 101.36 | 1.36 | 0 | — | -4.29 | -1.79 | -7.31 | 1 |
| 5 | Timing: Nasdaq FTD · TQQQ | daily | 101.21 | 1.21 | 0 | — | -6.17 | -1.07 | -15.27 | 1 |
| 6 | Hold SPY | benchmark | 100.66 | 0.66 | 0 | — | -0.11 | -0.02 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.62 | 0.62 | 0 | — | 1.17 | 0.59 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 100.61 | 0.61 | 0 | — | -1.64 | -0.89 | -5.09 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -3.83 | -1.25 | -9.74 | 25 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.71 | -0.29 | 0 | — | 0.61 | 0.31 | -5.18 | 1 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.97 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.41 | -1.47 | -3.04 | 21 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.18 | -1.52 | 86 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 98.71 | -1.29 | 0 | — | -5.06 | -2.42 | -5.36 | 1 |
| 17 | Hold BTC | benchmark | 98.61 | -1.39 | 0 | — | 26.70 | 3.19 | -8.68 | 1 |
| 18 | Copy: Insider buying | copy | 98.42 | -1.58 | 12 | 50.0 | -15.88 | -2.79 | -21.08 | 71 |
| 19 | Stochastic reversion · 1h | reversion | 98.20 | -1.80 | 81 | 53.1 | -12.46 | -2.49 | -15.06 | 344 |
| 20 | Donchian 55/20 · 1h | breakout | 98.06 | -1.94 | 26 | 15.4 | 10.01 | 1.34 | -16.96 | 109 |
| 21 | Three white soldiers · 1h | momentum | 97.53 | -2.47 | 6 | 0.0 | -3.03 | -2.34 | -4.15 | 26 |
| 22 | Agent (rotation) | meta | 96.55 | -3.45 | 78 | 28.2 | 0.90 | 0.37 | -7.43 | 255 |
| 23 | Trend pullback · 1h | trend | 96.54 | -3.46 | 78 | 23.1 | -23.26 | -6.53 | -25.53 | 168 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 96.32 | -3.68 | 0 | — | 8.88 | 1.50 | -8.33 | 1 |
| 25 | EMA 20/50 cross · 1h | trend | 96.15 | -3.85 | 36 | 11.1 | 0.53 | 0.28 | -20.52 | 135 |
| 26 | ADX DI cross · 1h | trend | 96.08 | -3.92 | 55 | 21.8 | -4.90 | -0.70 | -13.84 | 249 |
| 27 | Daily: Momentum burst | daily | 95.98 | -4.02 | 4 | 0.0 | -4.75 | -0.57 | -17.67 | 40 |
| 28 | Z-score reversion · 1h | reversion | 95.94 | -4.06 | 36 | 38.9 | -0.65 | -0.01 | -8.60 | 168 |
| 29 | Daily: Bullish score | daily | 95.73 | -4.27 | 3 | 0.0 | -1.35 | 0.02 | -12.76 | 10 |
| 30 | Agent | meta | 95.71 | -4.29 | 50 | 54.0 | -9.25 | -5.16 | -9.81 | 244 |
| 31 | MACD cross · 1h | trend | 95.19 | -4.81 | 105 | 22.9 | -17.78 | -2.83 | -18.84 | 460 |
| 32 | Parabolic SAR · 1h | trend | 95.11 | -4.89 | 82 | 22.0 | -4.58 | -0.46 | -20.80 | 289 |
| 33 | Squeeze breakout · 1h | breakout | 94.88 | -5.12 | 34 | 26.5 | 15.40 | 2.52 | -8.14 | 102 |
| 34 | Supertrend · 1h | trend | 94.36 | -5.64 | 51 | 13.7 | -5.42 | -0.58 | -18.09 | 213 |
| 35 | Agent (aggressive) | meta | 94.25 | -5.75 | 22 | 45.5 | -6.66 | -3.08 | -7.27 | 109 |
| 36 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.31 | 1.87 | -6.52 | 194 |
| 37 | Connors RSI(2) · 1h | reversion | 93.39 | -6.61 | 102 | 41.2 | -18.29 | -6.02 | -20.97 | 252 |
| 38 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.21 | 0.23 | -19.98 | 118 |
| 39 | Bollinger breakout · 1h | breakout | 92.55 | -7.45 | 65 | 30.8 | 6.38 | 0.97 | -12.06 | 285 |
| 40 | RSI momentum · 1h | momentum | 92.37 | -7.63 | 60 | 15.0 | 1.60 | 0.40 | -16.65 | 217 |
| 41 | RSI(14) reversion · 1h | reversion | 92.27 | -7.73 | 26 | 26.9 | -4.56 | -0.88 | -9.03 | 156 |
| 42 | Volume breakout · 1h | breakout | 92.12 | -7.88 | 45 | 17.8 | 6.47 | 1.04 | -12.60 | 121 |
| 43 | Agent (ML meta-label) | meta | 92.07 | -7.93 | 366 | 18.0 | -2.53 | -0.31 | -14.07 | 386 |
| 44 | Bollinger reversion · 1h | reversion | 91.56 | -8.44 | 68 | 33.8 | -21.98 | -5.31 | -23.94 | 318 |
| 45 | Max aggression: 1-day momentum | meta | 91.26 | -8.74 | 9 | 33.3 | -23.96 | -1.22 | -37.31 | 43 |
| 46 | Triple EMA stack · 1h | trend | 91.20 | -8.80 | 68 | 16.2 | -10.07 | -1.08 | -25.80 | 233 |
| 47 | MFI reversion · 1h | reversion | 91.01 | -8.99 | 99 | 30.3 | -14.92 | -2.55 | -16.99 | 129 |
| 48 | Opening range 30m | breakout | 90.76 | -9.23 | 131 | 20.6 | -17.37 | -5.24 | -17.94 | 562 |
| 49 | Candlestick reversal · 1h | reversion | 90.45 | -9.55 | 100 | 30.0 | -30.29 | -6.00 | -31.51 | 507 |
| 50 | MACD zero-line · 1h | trend | 90.27 | -9.73 | 58 | 20.7 | -5.78 | -0.60 | -19.00 | 239 |
| 51 | Williams %R · 1h | reversion | 90.17 | -9.83 | 107 | 44.9 | -26.95 | -4.74 | -27.50 | 516 |
| 52 | Three white soldiers | momentum | 89.14 | -10.86 | 122 | 18.9 | -47.86 | -22.88 | -47.91 | 581 |
| 53 | Opening range 15m | breakout | 88.59 | -11.41 | 153 | 19.0 | -19.52 | -5.58 | -20.06 | 683 |
| 54 | Donchian 20/10 · 1h | breakout | 88.31 | -11.69 | 55 | 20.0 | -1.95 | -0.03 | -17.36 | 219 |
| 55 | OBV trend · 1h | momentum | 88.26 | -11.74 | 139 | 18.0 | -14.84 | -1.68 | -30.19 | 314 |
| 56 | EMA 9/21 cross · 1h | trend | 88.23 | -11.77 | 99 | 14.1 | -10.83 | -1.26 | -20.93 | 334 |
| 57 | VWAP momentum · 1h | momentum | 88.21 | -11.79 | 262 | 21.4 | -36.81 | -5.58 | -39.21 | 1266 |
| 58 | CCI reversion · 1h | reversion | 87.65 | -12.35 | 91 | 40.7 | -11.37 | -1.55 | -14.35 | 419 |
| 59 | Keltner breakout · 1h | breakout | 87.65 | -12.35 | 41 | 19.5 | -11.28 | -1.30 | -24.35 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 87.56 | -12.44 | 133 | 25.6 | -32.63 | -5.55 | -36.34 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.17 | -12.84 | 128 | 21.1 | -10.45 | -1.26 | -23.15 | 407 |
| 62 | Max aggression: 5-day momentum | meta | 83.58 | -16.42 | 7 | 28.6 | -27.10 | -2.40 | -34.64 | 30 |
| 63 | ROC + volume | momentum | 76.28 | -23.72 | 354 | 21.5 | -72.65 | -16.33 | -73.75 | 1643 |
| 64 | RSI(14) reversion | reversion | 75.55 | -24.45 | 339 | 28.0 | -73.44 | -18.39 | -73.60 | 1502 |
| 65 | Squeeze breakout | breakout | 74.17 | -25.83 | 280 | 15.0 | -62.08 | -18.18 | -62.13 | 1206 |
| 66 | EMA 20/50 cross | trend | 72.14 | -27.86 | 292 | 19.2 | -77.39 | -15.35 | -77.47 | 1448 |
| 67 | Donchian 55/20 | breakout | 71.96 | -28.05 | 287 | 17.4 | -68.33 | -14.55 | -68.40 | 1275 |
| 68 | Volume breakout | breakout | 71.89 | -28.11 | 230 | 13.0 | -63.56 | -18.16 | -63.56 | 897 |
| 69 | VWAP reversion | reversion | 68.56 | -31.44 | 379 | 25.3 | -72.16 | -16.18 | -72.43 | 1442 |
| 70 | Supertrend | trend | 67.23 | -32.77 | 420 | 20.5 | -86.66 | -21.11 | -86.85 | 1924 |
| 71 | Keltner breakout | breakout | 65.23 | -34.77 | 392 | 13.8 | -84.42 | -27.86 | -84.42 | 1843 |
| 72 | Ichimoku | trend | 62.56 | -37.45 | 365 | 9.0 | -81.83 | -23.24 | -81.83 | 1733 |
| 73 | AI bee: Bizzy | ai | 62.28 | -37.72 | 722 | 8.9 | — | — | — | — |
| 74 | MFI reversion | reversion | 62.24 | -37.76 | 447 | 20.8 | -87.97 | -28.41 | -87.97 | 2127 |
| 75 | Z-score reversion | reversion | 61.79 | -38.21 | 464 | 23.5 | -86.10 | -23.59 | -86.11 | 2097 |
| 76 | ADX DI cross | trend | 60.47 | -39.53 | 498 | 10.4 | -89.59 | -34.08 | -89.59 | 2131 |
| 77 | MACD zero-line | trend | 59.80 | -40.20 | 520 | 16.0 | -91.28 | -28.82 | -91.28 | 2344 |
| 78 | AI bee: Boozy | ai | 59.45 | -40.55 | 245 | 5.3 | — | — | — | — |
| 79 | Donchian 20/10 | breakout | 59.36 | -40.64 | 558 | 18.3 | -90.97 | -25.96 | -90.98 | 2640 |
| 80 | Trend pullback | trend | 58.98 | -41.02 | 515 | 15.7 | -90.59 | -26.92 | -90.59 | 2288 |
| 81 | RSI momentum | momentum | 58.44 | -41.56 | 524 | 17.6 | -90.38 | -25.43 | -90.38 | 2346 |
| 82 | Triple EMA stack | trend | 57.48 | -42.52 | 555 | 15.3 | -93.17 | -30.15 | -93.17 | 2590 |
| 83 | Bollinger breakout | breakout | 55.22 | -44.77 | 584 | 14.7 | -93.62 | -32.78 | -93.62 | 2798 |
| 84 | Consensus | meta | 53.60 | -46.40 | 554 | 9.9 | -94.26 | -25.45 | -94.26 | 2660 |
| 85 | EMA 9/21 cross | trend | 51.93 | -48.07 | 709 | 16.2 | -97.31 | -32.43 | -97.31 | 3519 |
| 86 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -30.32 | -98.71 | 5336 |
| 87 | Connors RSI(2) | reversion | 50.52 | -49.48 | 748 | 20.3 | -96.20 | -31.34 | -96.20 | 3559 |
| 88 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.46 | -36.49 | -96.46 | 3575 |
| 89 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.04 | -99.35 | 5668 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.51 | -99.73 | 6137 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.02 | -97.36 | 3633 |
| 92 | Stochastic reversion | reversion | 50.07 | -49.93 | 872 | 22.8 | -95.70 | -34.16 | -95.70 | 4071 |
| 93 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -36.60 | -98.51 | 4701 |
| 94 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.70 | -99.53 | 6126 |
| 95 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -33.23 | -95.92 | 3735 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.71 | -99.90 | 8231 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T11:00 | Agent (ML meta-label) | buy | XRP-USD | 5.12 | — | entry |
| 2026-10-09T11:00 | ADX DI cross · 1h | sell | XRP-USD | 23.67 | -0.46 | exit signal |
| 2026-10-09T11:00 | MACD zero-line · 1h | buy | BTC-USD | 22.58 | — | entry signal |
| 2026-10-09T11:00 | MFI reversion | buy | XRP-USD | 15.58 | — | entry signal |
| 2026-10-09T11:00 | MFI reversion | buy | SOL-USD | 15.58 | — | entry signal |
| 2026-10-09T11:00 | Connors RSI(2) | sell | ETH-USD | 12.60 | -0.08 | exit signal |
| 2026-10-09T11:00 | RSI(14) reversion | buy | ETH-USD | 18.90 | — | entry signal |
| 2026-10-09T10:55 | Stochastic reversion | buy | ETH-USD | 7.52 | — | entry signal |
| 2026-10-09T10:55 | Stochastic reversion | sell | SOL-USD | 2.50 | -0.02 | rebalance down |
| 2026-10-09T10:55 | Stochastic reversion | sell | DOGE-USD | 2.50 | -0.02 | rebalance down |
| 2026-10-09T10:55 | Stochastic reversion | sell | BTC-USD | 2.52 | -0.01 | rebalance down |
| 2026-10-09T10:55 | VWAP reversion | buy | DOGE-USD | 17.15 | — | entry signal |
| 2026-10-09T10:55 | Z-score reversion | buy | BTC-USD | 15.46 | — | entry signal |
| 2026-10-09T10:55 | Connors RSI(2) | sell | BTC-USD | 12.65 | -0.08 | exit signal |
| 2026-10-09T10:55 | RSI(14) reversion | buy | SOL-USD | 18.91 | — | entry signal |
| 2026-10-09T10:50 | MFI reversion | buy | BTC-USD | 15.59 | — | entry signal |
| 2026-10-09T10:50 | EMA 20/50 cross | sell | ETH-USD | 14.44 | 0.04 | exit signal |
| 2026-10-09T10:45 | Stochastic reversion | buy | XRP-USD | 12.57 | — | entry signal |
| 2026-10-09T10:45 | Stochastic reversion | buy | SOL-USD | 12.57 | — | entry signal |
| 2026-10-09T10:45 | Stochastic reversion | buy | DOGE-USD | 12.57 | — | entry signal |
| 2026-10-09T10:45 | Stochastic reversion | buy | BTC-USD | 12.57 | — | entry signal |
| 2026-10-09T10:45 | Connors RSI(2) | buy | XRP-USD | 12.67 | — | entry signal |
| 2026-10-09T10:45 | Connors RSI(2) | sell | DOGE-USD | 12.61 | -0.12 | stop-loss |
| 2026-10-09T10:40 | AI bee: Bizzy | sell | XRP-USD | 10.01 | -0.12 | Jev: sell (sell p=0.90) after 10 min |
| 2026-10-09T10:40 | Agent (ML meta-label) | sell | XRP-USD | 6.08 | -0.06 | selected signal exited |
| 2026-10-09T10:40 | Stochastic reversion | sell | SOL-USD | 12.61 | -0.12 | stop-loss |
| 2026-10-09T10:40 | Stochastic reversion | sell | ETH-USD | 12.57 | -0.11 | stop-loss |
| 2026-10-09T10:40 | Connors RSI(2) | buy | ETH-USD | 12.69 | — | entry signal |
| 2026-10-09T10:40 | EMA 9/21 cross | sell | BTC-USD | 10.53 | -0.00 | exit signal |
| 2026-10-09T10:35 | Stochastic reversion | sell | XRP-USD | 12.59 | -0.12 | stop-loss |
| 2026-10-09T10:35 | Stochastic reversion | sell | DOGE-USD | 12.51 | -0.13 | stop-loss |
| 2026-10-09T10:35 | Z-score reversion | sell | XRP-USD | 15.37 | -0.15 | stop-loss |
| 2026-10-09T10:35 | Z-score reversion | sell | DOGE-USD | 15.36 | -0.18 | stop-loss |
| 2026-10-09T10:35 | Connors RSI(2) | buy | DOGE-USD | 12.73 | — | entry signal |
| 2026-10-09T10:35 | Connors RSI(2) | buy | BTC-USD | 12.73 | — | entry signal |
| 2026-10-09T10:35 | Connors RSI(2) | sell | ETH-USD | 12.68 | -0.11 | stop-loss |
| 2026-10-09T10:35 | Donchian 55/20 | sell | ETH-USD | 17.90 | -0.03 | exit signal |
| 2026-10-09T10:35 | Donchian 55/20 | sell | BTC-USD | 18.08 | 0.00 | exit signal |
| 2026-10-09T10:35 | Donchian 20/10 | sell | BTC-USD | 14.82 | -0.11 | stop-loss |
| 2026-10-09T10:35 | RSI momentum | sell | BTC-USD | 11.88 | 0.00 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 11:00:05.000148+00:00 -> 2026-10-09 11:10:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
