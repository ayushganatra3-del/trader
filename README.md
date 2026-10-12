# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T14:55:05.000205+00:00 · 20315 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.44 (-4.56%)

Closed trades 55, win rate 52.7%, fees £2.15, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TNA | 19.07 | -0.02 |

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

Today: 14295 decisions in 2172 calls, $0.1904 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T14:55 | 5 / 15 / 10 | NANC 18% |  |
| Breezy | 2026-10-12T14:55 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-12T14:55 | 2 / 27 / 1 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.52 | 2.52 | 0 | — | -1.00 | -0.41 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.33 | 2.33 | 39 | 41.0 | -8.29 | -2.51 | -13.79 | 116 |
| 3 | Copy: Insider buying | copy | 101.92 | 1.92 | 14 | 57.1 | -12.66 | -2.08 | -20.64 | 71 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.44 | 1.44 | 5 | 60.0 | 4.93 | 2.19 | -3.27 | 16 |
| 6 | Hold SPY | benchmark | 101.27 | 1.27 | 0 | — | 0.75 | 0.49 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.18 | 1.18 | 0 | — | 1.74 | 0.85 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.70 | 0.70 | 0 | — | -6.36 | -1.08 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.53 | 0.53 | 0 | — | -1.66 | -0.88 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.09 | 0.09 | 6 | 50.0 | -4.14 | -1.38 | -9.74 | 25 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 100.03 | 0.03 | 0 | — | 3.04 | 1.20 | -5.18 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.88 | -0.12 | 10 | 30.0 | 4.29 | 1.36 | -7.55 | 43 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.76 | -0.24 | 0 | — | -4.06 | -1.87 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 18 | Hold BTC | benchmark | 98.66 | -1.34 | 0 | — | 29.43 | 3.47 | -8.68 | 1 |
| 19 | Max aggression: 1-day momentum | meta | 98.21 | -1.79 | 11 | 36.4 | -16.40 | -0.60 | -37.31 | 42 |
| 20 | Donchian 55/20 · 1h | breakout | 97.99 | -2.01 | 31 | 12.9 | 12.15 | 1.51 | -16.84 | 116 |
| 21 | Trend pullback · 1h | trend | 97.84 | -2.16 | 78 | 23.1 | -22.87 | -6.36 | -25.60 | 167 |
| 22 | Stochastic reversion · 1h | reversion | 97.76 | -2.24 | 96 | 53.1 | -11.58 | -2.25 | -14.06 | 334 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 97.50 | -2.50 | 0 | — | 10.14 | 1.66 | -8.33 | 1 |
| 24 | Daily: Bullish score | daily | 97.31 | -2.69 | 4 | 0.0 | -0.18 | 0.17 | -12.76 | 11 |
| 25 | Three white soldiers · 1h | momentum | 97.21 | -2.79 | 7 | 0.0 | -3.31 | -2.55 | -4.50 | 27 |
| 26 | Z-score reversion · 1h | reversion | 97.00 | -3.00 | 44 | 43.2 | 3.63 | 0.85 | -8.60 | 156 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.16 | -0.32 | -17.67 | 39 |
| 28 | Agent (rotation) | meta | 96.40 | -3.60 | 82 | 29.3 | -10.10 | -3.28 | -14.70 | 274 |
| 29 | ADX DI cross · 1h | trend | 96.11 | -3.89 | 61 | 19.7 | 0.62 | 0.26 | -13.84 | 255 |
| 30 | MACD cross · 1h | trend | 95.97 | -4.03 | 120 | 24.2 | -13.16 | -2.16 | -17.27 | 466 |
| 31 | Parabolic SAR · 1h | trend | 95.73 | -4.27 | 83 | 21.7 | 1.48 | 0.38 | -21.52 | 292 |
| 32 | EMA 20/50 cross · 1h | trend | 95.62 | -4.38 | 44 | 13.6 | 2.87 | 0.54 | -23.03 | 134 |
| 33 | Agent | meta | 95.44 | -4.56 | 55 | 52.7 | -8.78 | -5.19 | -9.75 | 243 |
| 34 | Supertrend · 1h | trend | 94.63 | -5.37 | 55 | 12.7 | 0.97 | 0.31 | -18.28 | 212 |
| 35 | Gap and go | momentum | 93.83 | -6.17 | 58 | 12.1 | 8.43 | 2.15 | -6.20 | 202 |
| 36 | Squeeze breakout · 1h | breakout | 93.58 | -6.42 | 39 | 23.1 | 14.11 | 2.34 | -9.37 | 106 |
| 37 | Agent (aggressive) | meta | 93.44 | -6.56 | 26 | 42.3 | -4.51 | -2.03 | -6.79 | 114 |
| 38 | MFI reversion · 1h | reversion | 93.31 | -6.69 | 122 | 34.4 | -8.00 | -1.21 | -16.99 | 125 |
| 39 | Agent (ML meta-label) | meta | 92.57 | -7.43 | 410 | 18.3 | -4.29 | -0.69 | -13.50 | 424 |
| 40 | RSI momentum · 1h | momentum | 92.51 | -7.49 | 65 | 15.4 | 0.50 | 0.26 | -21.61 | 228 |
| 41 | Connors RSI(2) · 1h | reversion | 92.44 | -7.56 | 114 | 43.0 | -18.63 | -6.14 | -21.02 | 252 |
| 42 | RSI(14) reversion · 1h | reversion | 92.22 | -7.78 | 30 | 30.0 | -3.60 | -0.68 | -9.03 | 142 |
| 43 | Volume breakout · 1h | breakout | 91.63 | -8.37 | 60 | 20.0 | 8.30 | 1.28 | -12.60 | 119 |
| 44 | Bollinger reversion · 1h | reversion | 91.51 | -8.49 | 82 | 37.8 | -22.24 | -5.29 | -23.40 | 314 |
| 45 | Bollinger breakout · 1h | breakout | 90.96 | -9.04 | 74 | 28.4 | 7.38 | 1.09 | -13.96 | 278 |
| 46 | Ichimoku · 1h | trend | 90.93 | -9.07 | 47 | 17.0 | 0.86 | 0.31 | -22.17 | 125 |
| 47 | Triple EMA stack · 1h | trend | 90.72 | -9.28 | 71 | 15.5 | -8.43 | -0.71 | -32.16 | 230 |
| 48 | Opening range 30m | breakout | 90.17 | -9.82 | 149 | 22.1 | -15.00 | -4.55 | -15.49 | 565 |
| 49 | Williams %R · 1h | reversion | 89.81 | -10.19 | 130 | 46.9 | -26.06 | -4.41 | -27.34 | 503 |
| 50 | CCI reversion · 1h | reversion | 89.11 | -10.89 | 111 | 45.9 | -6.49 | -0.76 | -14.35 | 406 |
| 51 | Candlestick reversal · 1h | reversion | 88.62 | -11.38 | 126 | 31.7 | -28.41 | -5.55 | -28.89 | 502 |
| 52 | OBV trend · 1h | momentum | 88.59 | -11.41 | 150 | 18.7 | -9.97 | -0.96 | -28.82 | 323 |
| 53 | VWAP momentum · 1h | momentum | 88.41 | -11.59 | 297 | 23.2 | -33.35 | -4.98 | -39.97 | 1266 |
| 54 | Heikin-Ashi · 1h | trend | 88.07 | -11.93 | 147 | 27.2 | -29.44 | -4.90 | -36.88 | 686 |
| 55 | MACD zero-line · 1h | trend | 87.86 | -12.14 | 67 | 17.9 | -15.19 | -2.42 | -21.02 | 234 |
| 56 | Donchian 20/10 · 1h | breakout | 87.84 | -12.16 | 63 | 17.5 | -1.34 | 0.04 | -19.23 | 218 |
| 57 | Opening range 15m | breakout | 87.53 | -12.47 | 174 | 20.7 | -17.38 | -4.89 | -18.54 | 686 |
| 58 | EMA 9/21 cross · 1h | trend | 87.35 | -12.65 | 106 | 13.2 | -9.60 | -1.09 | -22.60 | 334 |
| 59 | Max aggression: 5-day momentum | meta | 87.15 | -12.85 | 7 | 28.6 | -15.13 | -1.12 | -34.64 | 28 |
| 60 | Keltner breakout · 1h | breakout | 86.75 | -13.25 | 45 | 20.0 | -10.67 | -1.16 | -26.55 | 217 |
| 61 | Three white soldiers | momentum | 86.62 | -13.38 | 148 | 16.9 | -48.66 | -23.38 | -48.69 | 590 |
| 62 | ROC + volume · 1h | momentum | 85.95 | -14.05 | 134 | 21.6 | -10.19 | -1.22 | -24.55 | 413 |
| 63 | ROC + volume | momentum | 73.18 | -26.82 | 409 | 22.7 | -72.98 | -16.53 | -74.39 | 1676 |
| 64 | RSI(14) reversion | reversion | 71.12 | -28.88 | 395 | 26.1 | -72.82 | -18.04 | -72.86 | 1495 |
| 65 | Squeeze breakout | breakout | 69.87 | -30.13 | 345 | 15.1 | -62.08 | -17.83 | -62.36 | 1224 |
| 66 | Volume breakout | breakout | 69.56 | -30.44 | 273 | 13.9 | -62.22 | -17.69 | -62.29 | 900 |
| 67 | EMA 20/50 cross | trend | 68.04 | -31.96 | 351 | 19.7 | -76.37 | -15.00 | -76.39 | 1438 |
| 68 | Donchian 55/20 | breakout | 67.22 | -32.78 | 355 | 17.7 | -68.16 | -14.38 | -68.81 | 1295 |
| 69 | VWAP reversion | reversion | 66.32 | -33.68 | 415 | 25.3 | -71.12 | -15.68 | -71.22 | 1420 |
| 70 | Keltner breakout | breakout | 60.74 | -39.26 | 474 | 14.3 | -83.61 | -27.48 | -83.63 | 1850 |
| 71 | Supertrend | trend | 60.64 | -39.36 | 491 | 19.3 | -85.87 | -20.64 | -85.99 | 1898 |
| 72 | AI bee: Boozy | ai | 60.24 | -39.76 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.63 | -42.37 | 429 | 10.0 | -82.03 | -22.80 | -82.16 | 1749 |
| 74 | MFI reversion | reversion | 56.14 | -43.85 | 544 | 20.2 | -87.79 | -28.17 | -87.81 | 2109 |
| 75 | Z-score reversion | reversion | 55.97 | -44.03 | 538 | 21.4 | -85.56 | -22.88 | -85.59 | 2065 |
| 76 | AI bee: Bizzy | ai | 55.90 | -44.10 | 874 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.29 | -45.71 | 570 | 10.0 | -89.19 | -34.53 | -89.19 | 2102 |
| 78 | Donchian 20/10 | breakout | 52.49 | -47.51 | 666 | 17.7 | -90.81 | -25.71 | -90.83 | 2650 |
| 79 | MACD zero-line | trend | 51.60 | -48.40 | 615 | 14.5 | -91.29 | -29.05 | -91.33 | 2339 |
| 80 | RSI momentum | momentum | 51.11 | -48.88 | 642 | 16.5 | -90.40 | -25.28 | -90.50 | 2370 |
| 81 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -30.46 | -98.62 | 5353 |
| 82 | Trend pullback | trend | 50.61 | -49.39 | 632 | 14.2 | -91.37 | -26.87 | -91.37 | 2340 |
| 83 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.16 | -29.66 | -93.21 | 2604 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.33 | -32.63 | -97.34 | 3511 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.36 | -35.08 | -96.40 | 3599 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.34 | -25.52 | -94.34 | 2646 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.49 | -99.36 | 5632 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.40 | -31.48 | -96.41 | 3600 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.29 | -99.73 | 6127 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.30 | -37.20 | -97.32 | 3673 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.66 | -98.49 | 4673 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.41 | -32.61 | -93.42 | 2793 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.60 | -99.53 | 6107 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.93 | -95.87 | 3722 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -34.22 | -95.71 | 4048 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.33 | -99.89 | 8223 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T14:55 | MFI reversion | buy | PLTR | 14.04 | — | entry signal |
| 2026-10-12T14:55 | Opening range 15m | buy | SQQQ | 4.39 | — | rebalance up |
| 2026-10-12T14:55 | Trend pullback | buy | SPY | 12.65 | — | entry signal |
| 2026-10-12T14:55 | Ichimoku | buy | GOOGL | 14.41 | — | entry signal |
| 2026-10-12T14:55 | ADX DI cross | buy | PLTR | 13.57 | — | entry signal |
| 2026-10-12T14:51 | Agent (rotation) | sell | XRP-USD | 7.88 | -0.17 | selected signal exited |
| 2026-10-12T14:51 | Agent (ML meta-label) | buy | UPRO | 6.61 | — | entry |
| 2026-10-12T14:51 | Agent (ML meta-label) | buy | LABU | 6.61 | — | following Donchian 20/10 |
| 2026-10-12T14:51 | Williams %R · 1h | buy | TQQQ | 6.65 | — | rebalance up |
| 2026-10-12T14:51 | Williams %R · 1h | buy | TECL | 6.77 | — | rebalance up |
| 2026-10-12T14:51 | Williams %R · 1h | buy | QQQ | 6.64 | — | rebalance up |
| 2026-10-12T14:51 | Williams %R · 1h | buy | ETH-USD | 6.77 | — | rebalance up |
| 2026-10-12T14:51 | Williams %R · 1h | buy | BTC-USD | 6.72 | — | rebalance up |
| 2026-10-12T14:51 | Williams %R · 1h | sell | XRP-USD | 11.08 | -0.24 | stop-loss |
| 2026-10-12T14:51 | Stochastic reversion · 1h | sell | XRP-USD | 24.19 | -0.53 | stop-loss |
| 2026-10-12T14:51 | VWAP reversion · 1h | sell | XRP-USD | 25.22 | -0.54 | stop-loss |
| 2026-10-12T14:51 | Donchian 55/20 · 1h | sell | ETH-USD | 22.97 | -0.25 | stop-loss |
| 2026-10-12T14:51 | Z-score reversion | buy | NVDA | 5.06 | — | entry signal |
| 2026-10-12T14:51 | Z-score reversion | sell | BTC-USD | 5.06 | -0.06 | stop-loss |
| 2026-10-12T14:51 | RSI momentum | buy | GOOGL | 12.79 | — | entry signal |
| 2026-10-12T14:51 | RSI momentum | buy | AAPL | 12.79 | — | entry signal |
| 2026-10-12T14:51 | Trend pullback | sell | AMZN | 12.71 | -0.04 | exit signal |
| 2026-10-12T14:51 | ADX DI cross | sell | AMZN | 13.57 | -0.04 | exit signal |
| 2026-10-12T14:51 | Supertrend | sell | BTC-USD | 15.15 | -0.19 | exit signal |
| 2026-10-12T14:51 | Supertrend | sell | BITX | 12.10 | -0.10 | exit signal |
| 2026-10-12T14:51 | EMA 20/50 cross | sell | MSTR | 16.82 | -0.27 | stop-loss |
| 2026-10-12T14:45 | Agent (ML meta-label) | buy | TECL | 7.72 | — | entry |
| 2026-10-12T14:45 | Agent (ML meta-label) | sell | UPRO | 5.79 | -0.04 | selected signal exited |
| 2026-10-12T14:45 | VWAP reversion | buy | XRP-USD | 6.62 | — | entry signal |
| 2026-10-12T14:45 | VWAP reversion | buy | SOL-USD | 6.64 | — | entry signal |
| 2026-10-12T14:45 | VWAP reversion | buy | ETH-USD | 6.64 | — | entry signal |
| 2026-10-12T14:45 | VWAP reversion | buy | DOGE-USD | 6.64 | — | entry signal |
| 2026-10-12T14:45 | VWAP reversion | sell | TQQQ | 4.36 | -0.00 | rebalance down |
| 2026-10-12T14:45 | VWAP reversion | sell | TECL | 4.44 | -0.01 | rebalance down |
| 2026-10-12T14:45 | VWAP reversion | sell | SPY | 4.43 | -0.00 | rebalance down |
| 2026-10-12T14:45 | VWAP reversion | sell | SOXL | 4.46 | 0.01 | rebalance down |
| 2026-10-12T14:45 | VWAP reversion | sell | BTC-USD | 4.42 | -0.02 | rebalance down |
| 2026-10-12T14:45 | VWAP reversion | sell | AMZN | 4.43 | 0.01 | rebalance down |
| 2026-10-12T14:45 | Z-score reversion | buy | XRP-USD | 5.07 | — | entry signal |
| 2026-10-12T14:45 | Z-score reversion | buy | TQQQ | 5.09 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 14:55:05.000205+00:00 -> 2026-10-12 15:05:05.000205+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
