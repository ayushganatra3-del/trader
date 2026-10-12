# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T18:52:05.000150+00:00 · 20478 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.31 (-4.70%)

Closed trades 57, win rate 50.9%, fees £2.26, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AAPL | 19.07 | +0.00 |
| TNA | 19.03 | -0.06 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 28806 decisions in 2661 calls, $0.3604 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T18:52 | 2 / 5 / 23 | AMD 15%, SOXL 14% |  |
| Breezy | 2026-10-12T18:52 | 0 / 22 / 8 | cash |  |
| Boozy | 2026-10-12T18:52 | 1 / 26 / 3 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.92 | 2.92 | 0 | — | 0.13 | 0.12 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 3 | Copy: Insider buying | copy | 101.64 | 1.64 | 14 | 57.1 | -13.07 | -2.16 | -20.64 | 71 |
| 4 | VWAP reversion · 1h | reversion | 101.60 | 1.60 | 39 | 41.0 | -8.92 | -2.68 | -13.79 | 118 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.56 | 1.56 | 6 | 50.0 | 4.97 | 2.21 | -3.27 | 17 |
| 6 | Hold SPY | benchmark | 101.36 | 1.36 | 0 | — | 0.86 | 0.55 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.16 | 1.16 | 0 | — | 1.63 | 0.79 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.77 | 0.77 | 6 | 50.0 | -3.68 | -1.21 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.56 | 0.56 | 0 | — | -1.13 | -0.59 | -5.09 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.56 | 0.56 | 10 | 30.0 | 4.80 | 1.50 | -7.55 | 43 |
| 11 | Timing: Nasdaq FTD · TQQQ | daily | 100.40 | 0.40 | 0 | — | -4.84 | -0.78 | -15.27 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.74 | -0.26 | 0 | — | 3.61 | 1.42 | -5.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.58 | -0.42 | 0 | — | -4.71 | -2.17 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 18 | Hold BTC | benchmark | 98.61 | -1.39 | 0 | — | 29.35 | 3.45 | -8.68 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 97.95 | -2.05 | 31 | 12.9 | 14.65 | 1.71 | -16.92 | 113 |
| 20 | Trend pullback · 1h | trend | 97.68 | -2.32 | 78 | 23.1 | -23.15 | -6.48 | -25.60 | 168 |
| 21 | Daily: Bullish score | daily | 97.40 | -2.60 | 4 | 0.0 | 0.40 | 0.25 | -12.76 | 11 |
| 22 | Stochastic reversion · 1h | reversion | 97.27 | -2.73 | 96 | 53.1 | -11.61 | -2.25 | -13.98 | 337 |
| 23 | Max aggression: 1-day momentum | meta | 97.22 | -2.78 | 11 | 36.4 | -17.40 | -0.67 | -37.31 | 42 |
| 24 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.76 | -3.25 | 0 | — | 8.93 | 1.48 | -8.33 | 1 |
| 26 | Z-score reversion · 1h | reversion | 96.73 | -3.27 | 44 | 43.2 | 3.35 | 0.79 | -8.60 | 158 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -2.43 | -0.20 | -17.67 | 39 |
| 28 | Agent (rotation) | meta | 96.42 | -3.58 | 82 | 29.3 | -9.97 | -3.12 | -14.32 | 291 |
| 29 | ADX DI cross · 1h | trend | 96.38 | -3.62 | 62 | 19.4 | -7.42 | -1.25 | -13.69 | 253 |
| 30 | MACD cross · 1h | trend | 95.62 | -4.38 | 124 | 23.4 | -13.15 | -2.17 | -17.27 | 465 |
| 31 | EMA 20/50 cross · 1h | trend | 95.41 | -4.59 | 45 | 15.6 | 3.29 | 0.58 | -23.39 | 136 |
| 32 | Agent | meta | 95.31 | -4.70 | 57 | 50.9 | -8.64 | -4.15 | -8.83 | 241 |
| 33 | Parabolic SAR · 1h | trend | 95.29 | -4.71 | 85 | 22.4 | 1.09 | 0.33 | -21.52 | 291 |
| 34 | Supertrend · 1h | trend | 94.32 | -5.68 | 58 | 13.8 | 2.70 | 0.52 | -18.79 | 211 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.23 | 2.10 | -6.21 | 202 |
| 36 | Squeeze breakout · 1h | breakout | 93.56 | -6.43 | 39 | 23.1 | 14.55 | 2.39 | -9.46 | 106 |
| 37 | Agent (aggressive) | meta | 93.24 | -6.76 | 29 | 37.9 | -6.95 | -3.04 | -7.14 | 122 |
| 38 | MFI reversion · 1h | reversion | 92.98 | -7.02 | 138 | 32.6 | -8.19 | -1.25 | -16.93 | 128 |
| 39 | Connors RSI(2) · 1h | reversion | 92.45 | -7.55 | 115 | 43.5 | -18.96 | -6.26 | -21.19 | 255 |
| 40 | RSI momentum · 1h | momentum | 92.44 | -7.56 | 66 | 15.2 | 0.33 | 0.24 | -21.70 | 228 |
| 41 | Agent (ML meta-label) | meta | 92.18 | -7.82 | 430 | 18.1 | -2.13 | -0.24 | -13.41 | 398 |
| 42 | RSI(14) reversion · 1h | reversion | 91.72 | -8.28 | 30 | 30.0 | -4.34 | -0.86 | -9.03 | 141 |
| 43 | Volume breakout · 1h | breakout | 91.57 | -8.43 | 67 | 19.4 | 8.88 | 1.35 | -12.60 | 117 |
| 44 | Bollinger reversion · 1h | reversion | 91.31 | -8.69 | 83 | 37.3 | -23.80 | -5.88 | -24.67 | 317 |
| 45 | Ichimoku · 1h | trend | 90.99 | -9.01 | 47 | 17.0 | 0.74 | 0.30 | -22.34 | 126 |
| 46 | Bollinger breakout · 1h | breakout | 90.87 | -9.13 | 74 | 28.4 | 8.30 | 1.20 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.62 | -9.38 | 71 | 15.5 | -7.79 | -0.70 | -27.13 | 239 |
| 48 | Opening range 30m | breakout | 89.63 | -10.37 | 152 | 21.7 | -15.57 | -4.69 | -15.92 | 569 |
| 49 | Williams %R · 1h | reversion | 89.60 | -10.40 | 131 | 46.6 | -26.46 | -4.47 | -27.58 | 506 |
| 50 | OBV trend · 1h | momentum | 88.48 | -11.52 | 150 | 18.7 | -9.13 | -0.84 | -28.76 | 323 |
| 51 | VWAP momentum · 1h | momentum | 88.42 | -11.58 | 307 | 23.5 | -33.42 | -4.99 | -40.22 | 1255 |
| 52 | CCI reversion · 1h | reversion | 88.42 | -11.59 | 111 | 45.9 | -10.35 | -1.38 | -14.35 | 404 |
| 53 | Candlestick reversal · 1h | reversion | 88.16 | -11.84 | 127 | 31.5 | -29.22 | -5.68 | -29.68 | 495 |
| 54 | Heikin-Ashi · 1h | trend | 87.87 | -12.13 | 152 | 28.3 | -29.67 | -4.94 | -37.08 | 682 |
| 55 | MACD zero-line · 1h | trend | 87.84 | -12.16 | 67 | 17.9 | -19.92 | -3.61 | -21.38 | 232 |
| 56 | Donchian 20/10 · 1h | breakout | 87.60 | -12.40 | 63 | 17.5 | -0.70 | 0.12 | -19.48 | 214 |
| 57 | Max aggression: 5-day momentum | meta | 87.20 | -12.80 | 7 | 28.6 | -15.24 | -1.13 | -34.64 | 28 |
| 58 | EMA 9/21 cross · 1h | trend | 87.12 | -12.88 | 108 | 13.0 | -8.52 | -0.89 | -22.93 | 333 |
| 59 | Opening range 15m | breakout | 86.86 | -13.14 | 180 | 20.0 | -18.11 | -5.00 | -19.41 | 692 |
| 60 | Keltner breakout · 1h | breakout | 86.68 | -13.32 | 45 | 20.0 | -12.32 | -1.44 | -26.77 | 216 |
| 61 | Three white soldiers | momentum | 86.54 | -13.46 | 152 | 17.1 | -48.68 | -23.38 | -48.68 | 589 |
| 62 | ROC + volume · 1h | momentum | 85.48 | -14.52 | 151 | 20.5 | -9.49 | -1.12 | -24.96 | 401 |
| 63 | ROC + volume | momentum | 72.84 | -27.16 | 417 | 22.5 | -73.17 | -16.64 | -74.43 | 1660 |
| 64 | RSI(14) reversion | reversion | 70.82 | -29.18 | 404 | 26.7 | -72.86 | -17.81 | -72.88 | 1471 |
| 65 | Squeeze breakout | breakout | 69.91 | -30.09 | 347 | 15.3 | -62.14 | -17.96 | -62.15 | 1217 |
| 66 | Volume breakout | breakout | 69.59 | -30.41 | 274 | 14.2 | -61.82 | -17.48 | -61.85 | 893 |
| 67 | EMA 20/50 cross | trend | 68.20 | -31.80 | 351 | 19.7 | -76.18 | -14.93 | -76.25 | 1428 |
| 68 | Donchian 55/20 | breakout | 67.07 | -32.93 | 357 | 17.6 | -68.04 | -14.27 | -68.90 | 1288 |
| 69 | VWAP reversion | reversion | 65.48 | -34.52 | 432 | 25.5 | -71.35 | -15.64 | -71.35 | 1400 |
| 70 | Keltner breakout | breakout | 60.72 | -39.28 | 478 | 14.6 | -83.46 | -27.26 | -83.47 | 1842 |
| 71 | Supertrend | trend | 60.35 | -39.65 | 496 | 19.2 | -85.99 | -20.74 | -86.00 | 1894 |
| 72 | AI bee: Boozy | ai | 59.70 | -40.30 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.36 | -42.65 | 432 | 10.0 | -82.19 | -22.86 | -82.19 | 1739 |
| 74 | Z-score reversion | reversion | 55.73 | -44.27 | 549 | 21.3 | -85.69 | -22.81 | -85.69 | 2064 |
| 75 | AI bee: Bizzy | ai | 55.59 | -44.41 | 882 | 8.4 | — | — | — | — |
| 76 | MFI reversion | reversion | 55.54 | -44.46 | 591 | 19.3 | -87.86 | -27.89 | -87.86 | 2117 |
| 77 | ADX DI cross | trend | 53.88 | -46.12 | 587 | 9.9 | -89.09 | -33.85 | -89.09 | 2103 |
| 78 | Donchian 20/10 | breakout | 52.20 | -47.80 | 673 | 17.5 | -90.93 | -25.80 | -90.93 | 2639 |
| 79 | MACD zero-line | trend | 51.22 | -48.78 | 626 | 14.4 | -91.44 | -29.30 | -91.44 | 2341 |
| 80 | RSI momentum | momentum | 50.64 | -49.36 | 651 | 16.6 | -90.49 | -25.29 | -90.49 | 2369 |
| 81 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -30.22 | -98.63 | 5349 |
| 82 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.33 | -26.48 | -91.33 | 2332 |
| 83 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.20 | -29.67 | -93.20 | 2603 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -32.48 | -97.35 | 3509 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.40 | -35.44 | -96.40 | 3596 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.26 | -25.33 | -94.26 | 2623 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.00 | -99.35 | 5626 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -30.96 | -96.32 | 3603 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.92 | -99.73 | 6148 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -37.36 | -97.35 | 3668 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.27 | -98.49 | 4657 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.42 | -32.56 | -93.42 | 2790 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.08 | -99.53 | 6095 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.64 | -95.89 | 3717 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -33.79 | -95.71 | 4051 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.24 | -99.89 | 8210 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T18:50 | Agent (ML meta-label) | buy | LABU | 4.98 | — | following Donchian 20/10 |
| 2026-10-12T18:50 | Agent (ML meta-label) | sell | AMD | 4.98 | -0.01 | selected signal exited |
| 2026-10-12T18:50 | MFI reversion | buy | BITX | 6.17 | — | entry signal |
| 2026-10-12T18:50 | ADX DI cross | sell | DOGE-USD | 13.34 | -0.09 | exit signal |
| 2026-10-12T18:45 | AI bee: Bizzy | buy | SOXL | 7.92 | — | Jev: buy (buy p=0.57) |
| 2026-10-12T18:45 | AI bee: Bizzy | buy | AMD | 8.22 | — | Jev: buy (buy p=0.59) |
| 2026-10-12T18:45 | Agent (ML meta-label) | buy | AMD | 4.99 | — | entry |
| 2026-10-12T18:45 | Agent (ML meta-label) | sell | QQQ | 4.99 | -0.00 | selected signal exited |
| 2026-10-12T18:45 | MFI reversion | buy | TSLA | 2.89 | — | rebalance up |
| 2026-10-12T18:45 | MFI reversion | buy | SOXL | 2.87 | — | rebalance up |
| 2026-10-12T18:45 | MFI reversion | buy | ETHU | 2.88 | — | rebalance up |
| 2026-10-12T18:45 | MFI reversion | buy | AMD | 2.88 | — | rebalance up |
| 2026-10-12T18:45 | MFI reversion | sell | DOGE-USD | 6.93 | -0.02 | exit signal |
| 2026-10-12T18:45 | ADX DI cross | buy | DOGE-USD | 13.44 | — | entry signal |
| 2026-10-12T18:40 | Agent (ML meta-label) | buy | QQQ | 4.99 | — | entry |
| 2026-10-12T18:40 | Agent (ML meta-label) | sell | AMD | 4.99 | -0.01 | selected signal exited |
| 2026-10-12T18:40 | MFI reversion | buy | DOGE-USD | 2.96 | — | rebalance up |
| 2026-10-12T18:40 | MFI reversion | sell | MSTR | 3.96 | -0.05 | stop-loss |
| 2026-10-12T18:40 | MFI reversion | sell | COIN | 5.55 | -0.04 | stop-loss |
| 2026-10-12T18:40 | VWAP reversion | buy | SOXL | 5.96 | — | entry |
| 2026-10-12T18:40 | VWAP reversion | sell | MSTR | 5.92 | -0.04 | stop-loss |
| 2026-10-12T18:40 | Donchian 20/10 | buy | NVDA | 13.05 | — | entry signal |
| 2026-10-12T18:40 | RSI momentum | buy | NVDA | 12.66 | — | entry signal |
| 2026-10-12T18:35 | Agent (ML meta-label) | buy | AMD | 5.00 | — | entry |
| 2026-10-12T18:35 | Agent (ML meta-label) | sell | IWM | 5.00 | -0.01 | selected signal exited |
| 2026-10-12T18:35 | MFI reversion | sell | GOOGL | 3.98 | -0.01 | exit signal |
| 2026-10-12T18:34 | AI bee: Bizzy | sell | META | 8.51 | -0.02 | Jev: sell (sell p=0.57) after 15 min |
| 2026-10-12T18:30 | MFI reversion · 1h | buy | QQQ | 23.26 | — | entry |
| 2026-10-12T18:30 | MFI reversion · 1h | sell | SOXL | 18.60 | 0.02 | target is flat |
| 2026-10-12T18:30 | MFI reversion · 1h | sell | BITX | 18.45 | -0.02 | target is flat |
| 2026-10-12T18:30 | Connors RSI(2) · 1h | buy | UPRO | 12.46 | — | entry signal |
| 2026-10-12T18:30 | Connors RSI(2) · 1h | buy | SPY | 13.22 | — | entry signal |
| 2026-10-12T18:30 | Connors RSI(2) · 1h | buy | AMZN | 8.56 | — | rebalance up |
| 2026-10-12T18:30 | Connors RSI(2) · 1h | sell | TQQQ | 5.24 | -0.00 | rebalance down |
| 2026-10-12T18:30 | Connors RSI(2) · 1h | sell | TECL | 5.21 | -0.02 | rebalance down |
| 2026-10-12T18:30 | Connors RSI(2) · 1h | sell | QQQ | 5.25 | 0.00 | rebalance down |
| 2026-10-12T18:30 | Connors RSI(2) · 1h | sell | AMD | 18.54 | 0.05 | exit signal |
| 2026-10-12T18:30 | ROC + volume · 1h | buy | PLTR | 5.18 | — | entry |
| 2026-10-12T18:30 | VWAP momentum · 1h | buy | NVDA | 22.07 | — | entry signal |
| 2026-10-12T18:30 | VWAP momentum · 1h | buy | AMD | 22.14 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 18:52:05.000150+00:00 -> 2026-10-12 19:02:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
