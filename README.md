# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T14:25:05.000178+00:00 · 20296 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.35 (-4.65%)

Closed trades 54, win rate 53.7%, fees £2.14, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.87 | -0.31 |
| TNA | 18.99 | -0.10 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 12588 decisions in 2115 calls, $0.1704 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T14:25 | 0 / 11 / 19 | NANC 18% |  |
| Breezy | 2026-10-12T14:25 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-12T14:25 | 1 / 26 / 3 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | AAPL | 2.49 | +0.83% | 6 |
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 102.68 | 2.68 | 38 | 42.1 | -8.05 | -2.44 | -13.79 | 116 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 102.65 | 2.65 | 0 | — | -1.01 | -0.41 | -5.18 | 1 |
| 3 | Copy: Insider buying | copy | 102.30 | 2.30 | 14 | 57.1 | -12.37 | -2.03 | -20.64 | 71 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 5.19 | 2.31 | -3.27 | 15 |
| 6 | Hold SPY | benchmark | 101.22 | 1.22 | 0 | — | 0.65 | 0.43 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.10 | 1.10 | 0 | — | 2.05 | 0.98 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.46 | 0.46 | 6 | 50.0 | -3.78 | -1.25 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.40 | 0.40 | 0 | — | -1.63 | -0.87 | -5.09 | 1 |
| 10 | Timing: Nasdaq FTD · TQQQ | daily | 100.31 | 0.31 | 0 | — | -6.28 | -1.06 | -15.27 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.25 | 0.26 | 10 | 30.0 | 4.69 | 1.47 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.15 | 0.15 | 0 | — | 3.28 | 1.28 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.76 | -0.24 | 0 | — | -4.06 | -1.87 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Hold BTC | benchmark | 99.06 | -0.94 | 0 | — | 29.41 | 3.47 | -8.68 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 19 | Max aggression: 1-day momentum | meta | 98.69 | -1.31 | 11 | 36.4 | -15.98 | -0.58 | -37.31 | 42 |
| 20 | Stochastic reversion · 1h | reversion | 98.31 | -1.69 | 92 | 53.3 | -11.05 | -2.14 | -14.02 | 334 |
| 21 | Donchian 55/20 · 1h | breakout | 98.15 | -1.85 | 30 | 13.3 | 12.35 | 1.53 | -16.84 | 115 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 97.82 | -2.18 | 0 | — | 9.96 | 1.64 | -8.33 | 1 |
| 23 | Trend pullback · 1h | trend | 97.70 | -2.29 | 78 | 23.1 | -22.97 | -6.40 | -25.60 | 167 |
| 24 | Daily: Bullish score | daily | 97.46 | -2.54 | 4 | 0.0 | 0.07 | 0.21 | -12.76 | 11 |
| 25 | Z-score reversion · 1h | reversion | 97.23 | -2.77 | 43 | 41.9 | 3.98 | 0.92 | -8.60 | 156 |
| 26 | Three white soldiers · 1h | momentum | 97.22 | -2.78 | 7 | 0.0 | -3.29 | -2.54 | -4.50 | 27 |
| 27 | Agent (rotation) | meta | 96.71 | -3.29 | 81 | 29.6 | -9.26 | -3.15 | -14.18 | 274 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.41 | -0.36 | -17.67 | 39 |
| 29 | ADX DI cross · 1h | trend | 96.33 | -3.67 | 61 | 19.7 | -11.63 | -2.10 | -14.38 | 253 |
| 30 | MACD cross · 1h | trend | 96.23 | -3.77 | 120 | 24.2 | -13.42 | -2.24 | -17.27 | 465 |
| 31 | Parabolic SAR · 1h | trend | 95.99 | -4.01 | 83 | 21.7 | 1.70 | 0.41 | -21.52 | 291 |
| 32 | EMA 20/50 cross · 1h | trend | 95.51 | -4.49 | 43 | 11.6 | 3.81 | 0.64 | -23.02 | 135 |
| 33 | Agent | meta | 95.35 | -4.65 | 54 | 53.7 | -7.86 | -4.75 | -8.68 | 244 |
| 34 | Supertrend · 1h | trend | 94.86 | -5.14 | 55 | 12.7 | 1.29 | 0.36 | -18.01 | 208 |
| 35 | MFI reversion · 1h | reversion | 94.12 | -5.88 | 122 | 34.4 | -7.52 | -1.13 | -16.91 | 126 |
| 36 | Gap and go | momentum | 93.80 | -6.20 | 58 | 12.1 | 8.40 | 2.14 | -6.20 | 202 |
| 37 | Squeeze breakout · 1h | breakout | 93.53 | -6.47 | 39 | 23.1 | 14.41 | 2.39 | -9.37 | 105 |
| 38 | Agent (aggressive) | meta | 93.26 | -6.74 | 26 | 42.3 | -5.14 | -2.30 | -7.20 | 113 |
| 39 | Agent (ML meta-label) | meta | 92.73 | -7.27 | 401 | 18.5 | -4.12 | -0.61 | -14.03 | 421 |
| 40 | RSI(14) reversion · 1h | reversion | 92.51 | -7.49 | 30 | 30.0 | -5.65 | -1.10 | -9.03 | 144 |
| 41 | Connors RSI(2) · 1h | reversion | 92.45 | -7.55 | 114 | 43.0 | -18.64 | -6.14 | -21.00 | 248 |
| 42 | RSI momentum · 1h | momentum | 92.45 | -7.55 | 65 | 15.4 | 0.60 | 0.28 | -21.50 | 225 |
| 43 | Bollinger reversion · 1h | reversion | 91.78 | -8.22 | 80 | 37.5 | -22.03 | -5.25 | -23.43 | 314 |
| 44 | Volume breakout · 1h | breakout | 91.64 | -8.36 | 60 | 20.0 | 8.31 | 1.28 | -12.60 | 118 |
| 45 | Ichimoku · 1h | trend | 90.99 | -9.01 | 47 | 17.0 | 0.93 | 0.32 | -22.13 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 90.91 | -9.09 | 74 | 28.4 | 7.49 | 1.11 | -13.94 | 277 |
| 47 | Opening range 30m | breakout | 90.58 | -9.42 | 147 | 22.4 | -14.61 | -4.44 | -15.49 | 565 |
| 48 | Triple EMA stack · 1h | trend | 90.56 | -9.44 | 71 | 15.5 | -8.45 | -0.79 | -26.96 | 239 |
| 49 | Williams %R · 1h | reversion | 90.06 | -9.94 | 127 | 47.2 | -26.81 | -4.63 | -27.07 | 505 |
| 50 | CCI reversion · 1h | reversion | 89.64 | -10.36 | 109 | 45.0 | -6.10 | -0.70 | -14.35 | 406 |
| 51 | Candlestick reversal · 1h | reversion | 89.15 | -10.85 | 124 | 32.3 | -27.51 | -5.34 | -28.45 | 504 |
| 52 | VWAP momentum · 1h | momentum | 88.81 | -11.19 | 288 | 21.5 | -33.01 | -4.92 | -39.70 | 1262 |
| 53 | OBV trend · 1h | momentum | 88.51 | -11.49 | 150 | 18.7 | -8.58 | -0.79 | -28.05 | 322 |
| 54 | Opening range 15m | breakout | 88.33 | -11.67 | 171 | 21.1 | -16.61 | -4.70 | -18.50 | 686 |
| 55 | MACD zero-line · 1h | trend | 88.24 | -11.76 | 67 | 17.9 | -16.74 | -2.77 | -20.89 | 234 |
| 56 | Heikin-Ashi · 1h | trend | 88.04 | -11.96 | 142 | 26.8 | -29.47 | -4.90 | -36.87 | 686 |
| 57 | Donchian 20/10 · 1h | breakout | 87.97 | -12.03 | 63 | 17.5 | -1.22 | 0.06 | -18.97 | 217 |
| 58 | EMA 9/21 cross · 1h | trend | 87.68 | -12.32 | 106 | 13.2 | -9.62 | -1.10 | -22.30 | 333 |
| 59 | Max aggression: 5-day momentum | meta | 87.02 | -12.98 | 7 | 28.6 | -15.26 | -1.13 | -34.64 | 28 |
| 60 | Keltner breakout · 1h | breakout | 86.70 | -13.30 | 45 | 20.0 | -11.87 | -1.31 | -26.55 | 217 |
| 61 | Three white soldiers | momentum | 86.62 | -13.38 | 148 | 16.9 | -48.53 | -23.19 | -48.67 | 586 |
| 62 | ROC + volume · 1h | momentum | 86.34 | -13.66 | 133 | 21.1 | -9.76 | -1.15 | -24.20 | 405 |
| 63 | ROC + volume | momentum | 73.58 | -26.41 | 406 | 22.7 | -72.91 | -16.51 | -74.25 | 1677 |
| 64 | RSI(14) reversion | reversion | 71.16 | -28.84 | 393 | 26.2 | -72.54 | -17.86 | -72.56 | 1471 |
| 65 | Squeeze breakout | breakout | 70.34 | -29.66 | 341 | 15.2 | -62.05 | -17.80 | -62.29 | 1224 |
| 66 | Volume breakout | breakout | 69.69 | -30.31 | 272 | 14.0 | -62.15 | -17.65 | -62.21 | 900 |
| 67 | EMA 20/50 cross | trend | 68.49 | -31.51 | 349 | 19.8 | -76.21 | -14.91 | -76.30 | 1436 |
| 68 | Donchian 55/20 | breakout | 67.63 | -32.37 | 353 | 17.8 | -67.98 | -14.37 | -68.62 | 1296 |
| 69 | VWAP reversion | reversion | 66.64 | -33.37 | 411 | 25.5 | -70.95 | -15.62 | -70.95 | 1414 |
| 70 | Supertrend | trend | 61.10 | -38.90 | 489 | 19.4 | -85.77 | -20.62 | -85.90 | 1902 |
| 71 | Keltner breakout | breakout | 60.95 | -39.05 | 472 | 14.4 | -83.61 | -27.47 | -83.62 | 1850 |
| 72 | AI bee: Boozy | ai | 60.72 | -39.28 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 58.25 | -41.75 | 425 | 10.1 | -81.83 | -22.81 | -81.96 | 1748 |
| 74 | MFI reversion | reversion | 56.25 | -43.75 | 541 | 20.1 | -87.71 | -28.09 | -87.74 | 2109 |
| 75 | Z-score reversion | reversion | 56.18 | -43.82 | 535 | 21.5 | -85.47 | -22.84 | -85.52 | 2061 |
| 76 | AI bee: Bizzy | ai | 55.90 | -44.10 | 874 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.37 | -45.62 | 568 | 10.0 | -89.13 | -34.38 | -89.14 | 2098 |
| 78 | Donchian 20/10 | breakout | 52.88 | -47.12 | 662 | 17.8 | -90.77 | -25.75 | -90.77 | 2651 |
| 79 | MACD zero-line | trend | 51.85 | -48.15 | 612 | 14.5 | -91.34 | -29.13 | -91.36 | 2341 |
| 80 | RSI momentum | momentum | 51.54 | -48.46 | 639 | 16.6 | -90.32 | -25.25 | -90.45 | 2368 |
| 81 | Trend pullback | trend | 50.93 | -49.07 | 629 | 14.3 | -91.33 | -26.94 | -91.33 | 2340 |
| 82 | Triple EMA stack | trend | 50.75 | -49.25 | 660 | 15.2 | -93.17 | -29.78 | -93.20 | 2607 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -30.37 | -98.61 | 5335 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.31 | -32.66 | -97.31 | 3516 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -35.19 | -96.39 | 3598 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.31 | -25.33 | -94.31 | 2645 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.36 | -99.35 | 5610 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.39 | -31.45 | -96.39 | 3599 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.17 | -99.73 | 6133 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.30 | -37.32 | -97.31 | 3673 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.74 | -98.49 | 4667 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.39 | -32.53 | -93.39 | 2793 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.69 | -99.52 | 6099 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -32.96 | -95.85 | 3716 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -34.15 | -95.70 | 4050 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.51 | -99.89 | 8224 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T14:25 | CCI reversion · 1h | buy | QQQ | 5.24 | — | rebalance up |
| 2026-10-12T14:25 | CCI reversion · 1h | buy | AAPL | 5.48 | — | rebalance up |
| 2026-10-12T14:25 | CCI reversion · 1h | sell | TECL | 9.95 | -0.24 | stop-loss |
| 2026-10-12T14:25 | Bollinger reversion · 1h | buy | SOL-USD | 4.60 | — | rebalance up |
| 2026-10-12T14:25 | Bollinger reversion · 1h | sell | QQQ | 4.60 | -0.02 | rebalance down |
| 2026-10-12T14:25 | VWAP momentum · 1h | sell | TECL | 6.17 | -0.24 | stop-loss |
| 2026-10-12T14:25 | MFI reversion | buy | TSLA | 14.07 | — | entry signal |
| 2026-10-12T14:25 | MFI reversion | sell | DOGE-USD | 11.22 | -0.15 | stop-loss |
| 2026-10-12T14:25 | VWAP reversion | sell | DOGE-USD | 7.38 | -0.10 | stop-loss |
| 2026-10-12T14:25 | RSI(14) reversion | sell | DOGE-USD | 7.92 | -0.09 | stop-loss |
| 2026-10-12T14:25 | Gap and go | sell | ETHU | 23.35 | -0.12 | exit signal |
| 2026-10-12T14:21 | VWAP reversion | buy | NVDA | 7.40 | — | entry signal |
| 2026-10-12T14:21 | VWAP reversion | sell | SOL-USD | 7.40 | -0.08 | stop-loss |
| 2026-10-12T14:21 | Z-score reversion | buy | UPRO | 1.33 | — | entry signal |
| 2026-10-12T14:21 | Z-score reversion | buy | TSLA | 8.04 | — | entry signal |
| 2026-10-12T14:21 | Z-score reversion | sell | DOGE-USD | 9.37 | -0.10 | stop-loss |
| 2026-10-12T14:21 | RSI(14) reversion | buy | TQQQ | 7.86 | — | entry signal |
| 2026-10-12T14:21 | RSI(14) reversion | buy | SOXL | 7.95 | — | entry signal |
| 2026-10-12T14:21 | RSI(14) reversion | buy | QQQ | 7.95 | — | entry signal |
| 2026-10-12T14:21 | RSI(14) reversion | buy | IWM | 7.95 | — | entry |
| 2026-10-12T14:21 | RSI(14) reversion | buy | AMD | 7.95 | — | entry signal |
| 2026-10-12T14:21 | RSI(14) reversion | sell | XRP-USD | 6.28 | -0.04 | rebalance down |
| 2026-10-12T14:21 | RSI(14) reversion | sell | TSLA | 6.41 | -0.01 | rebalance down |
| 2026-10-12T14:21 | RSI(14) reversion | sell | TNA | 6.41 | 0.00 | rebalance down |
| 2026-10-12T14:21 | RSI(14) reversion | sell | SOL-USD | 14.25 | -0.14 | stop-loss |
| 2026-10-12T14:21 | RSI(14) reversion | sell | DOGE-USD | 6.32 | -0.06 | rebalance down |
| 2026-10-12T14:21 | ROC + volume | buy | MSTR | 3.74 | — | rebalance up |
| 2026-10-12T14:21 | ROC + volume | buy | META | 3.68 | — | rebalance up |
| 2026-10-12T14:21 | ROC + volume | buy | BITX | 7.34 | — | rebalance up |
| 2026-10-12T14:21 | ROC + volume | sell | AAPL | 14.73 | -0.03 | target is flat |
| 2026-10-12T14:21 | Trend pullback | buy | AMZN | 12.75 | — | entry signal |
| 2026-10-12T14:21 | Ichimoku | buy | MSTR | 14.59 | — | entry signal |
| 2026-10-12T14:21 | Ichimoku | buy | COIN | 14.59 | — | entry signal |
| 2026-10-12T14:21 | ADX DI cross | buy | AMZN | 13.61 | — | entry signal |
| 2026-10-12T14:21 | ADX DI cross | sell | BTC-USD | 13.54 | -0.08 | exit signal |
| 2026-10-12T14:21 | EMA 20/50 cross | buy | MSTR | 3.48 | — | rebalance up |
| 2026-10-12T14:15 | Day trade: Stocks in Play ORB | sell | AAPL | 24.76 | -0.03 | target is flat |
| 2026-10-12T14:15 | Agent (ML meta-label) | buy | META | 4.89 | — | entry |
| 2026-10-12T14:15 | Agent (ML meta-label) | sell | IWM | 4.89 | -0.01 | selected signal exited |
| 2026-10-12T14:15 | Agent (aggressive) | buy | TNA | 46.75 | — | following Z-score reversion |

## Data problems on the last tick

- GURU: yfinance: $GURU: possibly delisted; no price data found  (5m 2026-10-11 14:25:05.000178+00:00 -> 2026-10-12 14:35:05.000178+00:00); yahoo: cooling down after a rate limit
- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 14:25:05.000178+00:00 -> 2026-10-12 14:35:05.000178+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
