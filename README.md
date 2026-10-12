# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T19:56:05.000133+00:00 · 20517 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.28 (-4.72%)

Closed trades 59, win rate 49.2%, fees £2.28, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 32307 decisions in 2778 calls, $0.4014 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T19:56 | 3 / 19 / 8 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-12T19:56 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-12T19:56 | 4 / 25 / 1 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.81 | 2.81 | 0 | — | 1.41 | 0.74 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.95 | 1.95 | 40 | 42.5 | -8.65 | -2.61 | -13.79 | 118 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.65 | 1.65 | 16 | 50.0 | -13.27 | -2.19 | -20.64 | 71 |
| 5 | Hold SPY | benchmark | 101.43 | 1.43 | 0 | — | 0.61 | 0.41 | -3.66 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.24 | 1.24 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 100.63 | 0.63 | 0 | — | -1.26 | -0.66 | -5.09 | 1 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.61 | 0.61 | 0 | — | -5.20 | -0.86 | -15.27 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.96 | -0.04 | 0 | — | 3.38 | 1.33 | -5.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.58 | -0.42 | 0 | — | -4.71 | -2.17 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Hold BTC | benchmark | 99.08 | -0.92 | 0 | — | 29.44 | 3.47 | -8.68 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.21 | -1.79 | 31 | 12.9 | 11.98 | 1.44 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.06 | -1.94 | 4 | 0.0 | 1.18 | 0.35 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.94 | -2.06 | 11 | 36.4 | -16.79 | -0.63 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.83 | -2.17 | 78 | 23.1 | -23.05 | -6.43 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.54 | -2.46 | 96 | 53.1 | -11.63 | -2.25 | -14.10 | 338 |
| 24 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.91 | -3.09 | 0 | — | 8.65 | 1.45 | -8.33 | 1 |
| 26 | Z-score reversion · 1h | reversion | 96.84 | -3.16 | 44 | 43.2 | 3.54 | 0.83 | -8.60 | 159 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.05 | -0.30 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.45 | -3.55 | 62 | 19.4 | -6.27 | -1.00 | -13.79 | 254 |
| 29 | Agent (rotation) | meta | 96.37 | -3.63 | 84 | 31.0 | -6.21 | -2.36 | -11.45 | 303 |
| 30 | MACD cross · 1h | trend | 95.70 | -4.30 | 125 | 24.0 | -11.65 | -1.82 | -17.79 | 461 |
| 31 | EMA 20/50 cross · 1h | trend | 95.38 | -4.62 | 45 | 15.6 | 4.91 | 0.75 | -23.71 | 136 |
| 32 | Parabolic SAR · 1h | trend | 95.38 | -4.62 | 86 | 22.1 | 1.20 | 0.35 | -21.52 | 291 |
| 33 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -8.17 | -3.89 | -8.62 | 236 |
| 34 | Supertrend · 1h | trend | 94.44 | -5.56 | 58 | 13.8 | 2.78 | 0.53 | -18.81 | 211 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.52 | -6.48 | 39 | 23.1 | 14.37 | 2.38 | -9.46 | 106 |
| 37 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.74 | -2.93 | -6.93 | 120 |
| 38 | MFI reversion · 1h | reversion | 93.13 | -6.87 | 151 | 32.5 | -7.99 | -1.21 | -16.91 | 128 |
| 39 | RSI momentum · 1h | momentum | 92.59 | -7.41 | 66 | 15.2 | -0.67 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.52 | -7.48 | 115 | 43.5 | -18.91 | -6.24 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.35 | -7.65 | 439 | 17.8 | -2.78 | -0.38 | -12.87 | 415 |
| 42 | RSI(14) reversion · 1h | reversion | 91.98 | -8.02 | 31 | 29.0 | 2.06 | 0.57 | -9.03 | 126 |
| 43 | Volume breakout · 1h | breakout | 91.67 | -8.33 | 70 | 20.0 | 9.09 | 1.38 | -12.60 | 118 |
| 44 | Bollinger reversion · 1h | reversion | 91.57 | -8.43 | 83 | 37.3 | -23.78 | -5.87 | -24.84 | 318 |
| 45 | Ichimoku · 1h | trend | 90.97 | -9.03 | 48 | 16.7 | 0.53 | 0.27 | -22.34 | 127 |
| 46 | Bollinger breakout · 1h | breakout | 90.85 | -9.14 | 74 | 28.4 | 8.28 | 1.20 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.70 | -9.30 | 71 | 15.5 | -7.65 | -0.68 | -27.19 | 239 |
| 48 | Williams %R · 1h | reversion | 89.63 | -10.37 | 132 | 46.2 | -25.51 | -4.24 | -27.71 | 502 |
| 49 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.67 | -4.71 | -16.08 | 569 |
| 50 | CCI reversion · 1h | reversion | 88.74 | -11.26 | 111 | 45.9 | -10.39 | -1.38 | -14.35 | 405 |
| 51 | OBV trend · 1h | momentum | 88.68 | -11.32 | 150 | 18.7 | -13.06 | -1.25 | -34.14 | 319 |
| 52 | Candlestick reversal · 1h | reversion | 88.40 | -11.60 | 127 | 31.5 | -27.26 | -5.21 | -28.12 | 491 |
| 53 | VWAP momentum · 1h | momentum | 88.25 | -11.75 | 311 | 23.2 | -33.64 | -5.02 | -40.37 | 1256 |
| 54 | Max aggression: 5-day momentum | meta | 88.02 | -11.98 | 7 | 28.6 | -14.45 | -1.05 | -34.64 | 28 |
| 55 | Donchian 20/10 · 1h | breakout | 87.77 | -12.23 | 63 | 17.5 | -0.58 | 0.14 | -19.51 | 214 |
| 56 | Heikin-Ashi · 1h | trend | 87.74 | -12.26 | 153 | 28.1 | -30.64 | -5.08 | -37.65 | 678 |
| 57 | MACD zero-line · 1h | trend | 87.70 | -12.30 | 67 | 17.9 | -21.53 | -3.99 | -21.69 | 234 |
| 58 | EMA 9/21 cross · 1h | trend | 87.13 | -12.87 | 108 | 13.0 | -8.53 | -0.90 | -23.06 | 333 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.65 | -13.35 | 45 | 20.0 | -11.34 | -1.25 | -26.77 | 216 |
| 61 | Three white soldiers | momentum | 86.47 | -13.53 | 152 | 17.1 | -48.72 | -23.41 | -48.72 | 590 |
| 62 | ROC + volume · 1h | momentum | 85.50 | -14.50 | 164 | 20.1 | -9.13 | -1.06 | -25.03 | 400 |
| 63 | ROC + volume | momentum | 72.74 | -27.26 | 417 | 22.5 | -72.89 | -16.47 | -74.40 | 1659 |
| 64 | RSI(14) reversion | reversion | 70.74 | -29.26 | 416 | 26.7 | -72.77 | -17.77 | -72.80 | 1467 |
| 65 | Squeeze breakout | breakout | 69.70 | -30.30 | 349 | 15.8 | -62.31 | -18.02 | -62.31 | 1224 |
| 66 | Volume breakout | breakout | 69.56 | -30.44 | 277 | 14.8 | -61.84 | -17.49 | -61.85 | 894 |
| 67 | EMA 20/50 cross | trend | 68.10 | -31.90 | 353 | 20.1 | -76.27 | -14.96 | -76.30 | 1430 |
| 68 | Donchian 55/20 | breakout | 66.99 | -33.01 | 358 | 17.6 | -68.07 | -14.27 | -68.94 | 1289 |
| 69 | VWAP reversion | reversion | 65.38 | -34.62 | 455 | 25.7 | -71.33 | -15.63 | -71.35 | 1398 |
| 70 | Keltner breakout | breakout | 60.64 | -39.36 | 480 | 14.8 | -83.27 | -27.06 | -83.29 | 1838 |
| 71 | Supertrend | trend | 60.28 | -39.72 | 498 | 19.5 | -86.03 | -20.75 | -86.03 | 1894 |
| 72 | AI bee: Boozy | ai | 60.06 | -39.94 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.25 | -42.75 | 434 | 9.9 | -82.24 | -22.85 | -82.24 | 1735 |
| 74 | Z-score reversion | reversion | 55.80 | -44.20 | 563 | 22.2 | -85.68 | -22.81 | -85.71 | 2066 |
| 75 | AI bee: Bizzy | ai | 55.51 | -44.49 | 888 | 8.3 | — | — | — | — |
| 76 | MFI reversion | reversion | 55.46 | -44.54 | 617 | 19.4 | -87.91 | -27.90 | -87.95 | 2115 |
| 77 | ADX DI cross | trend | 53.65 | -46.35 | 594 | 10.1 | -89.09 | -33.78 | -89.09 | 2110 |
| 78 | Donchian 20/10 | breakout | 52.00 | -48.00 | 679 | 17.7 | -90.90 | -25.66 | -90.91 | 2645 |
| 79 | MACD zero-line | trend | 51.08 | -48.92 | 630 | 14.6 | -91.49 | -29.39 | -91.49 | 2347 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -30.35 | -98.62 | 5327 |
| 81 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.29 | -26.35 | -91.29 | 2327 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -29.59 | -93.21 | 2599 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.53 | -25.25 | -90.53 | 2368 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -32.53 | -97.38 | 3526 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -35.25 | -96.39 | 3583 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.26 | -25.12 | -94.26 | 2628 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.01 | -99.36 | 5638 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -30.93 | -96.32 | 3599 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.85 | -99.73 | 6157 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -37.22 | -97.35 | 3664 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.27 | -98.49 | 4661 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.45 | -32.52 | -93.45 | 2800 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.02 | -99.53 | 6100 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.65 | -95.90 | 3724 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -33.78 | -95.71 | 4050 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.24 | -99.89 | 8209 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T19:56 | Agent (rotation) | sell | SQQQ | 64.37 | 0.24 | selected signal exited |
| 2026-10-12T19:56 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 101.31 | 0.28 | target is flat |
| 2026-10-12T19:56 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 100.52 | 0.05 | target is flat |
| 2026-10-12T19:56 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 98.81 | -0.25 | target is flat |
| 2026-10-12T19:56 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 100.31 | 0.74 | target is flat |
| 2026-10-12T19:56 | Agent (aggressive) | sell | TNA | 46.50 | -0.25 | selected signal exited |
| 2026-10-12T19:56 | Agent | sell | TNA | 18.99 | -0.10 | selected signal exited |
| 2026-10-12T19:56 | MFI reversion · 1h | buy | NVDA | 18.55 | — | entry |
| 2026-10-12T19:56 | MFI reversion · 1h | buy | BITX | 18.63 | — | entry |
| 2026-10-12T19:56 | MFI reversion · 1h | sell | SOXL | 23.30 | -0.04 | target is flat |
| 2026-10-12T19:56 | MFI reversion · 1h | sell | QQQ | 4.68 | -0.00 | rebalance down |
| 2026-10-12T19:56 | Volume breakout · 1h | buy | MSFT | 22.92 | — | entry |
| 2026-10-12T19:56 | ROC + volume · 1h | buy | PLTR | 12.21 | — | entry |
| 2026-10-12T19:56 | ROC + volume · 1h | sell | AMZN | 12.21 | -0.01 | target is flat |
| 2026-10-12T19:56 | VWAP momentum · 1h | buy | BITX | 17.65 | — | entry |
| 2026-10-12T19:56 | VWAP momentum · 1h | sell | SQQQ | 4.43 | -0.00 | rebalance down |
| 2026-10-12T19:56 | VWAP momentum · 1h | sell | AMD | 4.41 | 0.02 | rebalance down |
| 2026-10-12T19:56 | VWAP momentum · 1h | sell | AAPL | 4.41 | -0.00 | rebalance down |
| 2026-10-12T19:56 | MFI reversion | buy | SOL-USD | 6.92 | — | rebalance up |
| 2026-10-12T19:56 | MFI reversion | sell | TECL | 9.24 | -0.01 | end-of-day flatten |
| 2026-10-12T19:56 | MFI reversion | sell | QQQ | 6.94 | -0.00 | end-of-day flatten |
| 2026-10-12T19:56 | MFI reversion | sell | LABU | 9.30 | -0.02 | end-of-day flatten |
| 2026-10-12T19:56 | MFI reversion | sell | COIN | 7.86 | -0.06 | end-of-day flatten |
| 2026-10-12T19:56 | MFI reversion | sell | BITX | 9.25 | 0.06 | end-of-day flatten |
| 2026-10-12T19:56 | VWAP reversion | buy | XRP-USD | 9.21 | — | rebalance up |
| 2026-10-12T19:56 | VWAP reversion | buy | SOL-USD | 8.71 | — | rebalance up |
| 2026-10-12T19:56 | VWAP reversion | buy | ETH-USD | 6.84 | — | rebalance up |
| 2026-10-12T19:56 | VWAP reversion | buy | DOGE-USD | 9.24 | — | rebalance up |
| 2026-10-12T19:56 | VWAP reversion | buy | BTC-USD | 9.24 | — | rebalance up |
| 2026-10-12T19:56 | VWAP reversion | sell | UPRO | 1.48 | 0.00 | end-of-day flatten |
| 2026-10-12T19:56 | VWAP reversion | sell | TSLA | 3.85 | -0.00 | end-of-day flatten |
| 2026-10-12T19:56 | VWAP reversion | sell | TQQQ | 3.60 | -0.01 | target is flat |
| 2026-10-12T19:56 | VWAP reversion | sell | TECL | 3.87 | 0.02 | end-of-day flatten |
| 2026-10-12T19:56 | VWAP reversion | sell | SPY | 3.85 | -0.00 | end-of-day flatten |
| 2026-10-12T19:56 | VWAP reversion | sell | QQQ | 1.29 | -0.00 | end-of-day flatten |
| 2026-10-12T19:56 | VWAP reversion | sell | MSTR | 3.86 | 0.01 | end-of-day flatten |
| 2026-10-12T19:56 | VWAP reversion | sell | LABU | 5.03 | -0.01 | end-of-day flatten |
| 2026-10-12T19:56 | VWAP reversion | sell | IWM | 3.84 | -0.00 | end-of-day flatten |
| 2026-10-12T19:56 | VWAP reversion | sell | GOOGL | 4.09 | -0.01 | target is flat |
| 2026-10-12T19:56 | VWAP reversion | sell | COIN | 4.65 | -0.03 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 19:56:05.000133+00:00 -> 2026-10-12 20:06:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
