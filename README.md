# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T19:25:05.000156+00:00 · 20498 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.28 (-4.72%)

Closed trades 58, win rate 50.0%, fees £2.27, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
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
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 30588 decisions in 2721 calls, $0.3813 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T19:25 | 7 / 19 / 4 | GOOGL 14% |  |
| Breezy | 2026-10-12T19:25 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-12T19:25 | 7 / 22 / 1 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.93 | 2.93 | 0 | — | 1.06 | 0.57 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 3 | VWAP reversion · 1h | reversion | 101.67 | 1.68 | 39 | 41.0 | -9.07 | -2.73 | -13.79 | 118 |
| 4 | Copy: Insider buying | copy | 101.59 | 1.59 | 14 | 57.1 | -13.10 | -2.16 | -20.64 | 71 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.57 | 1.57 | 6 | 50.0 | 4.99 | 2.22 | -3.27 | 17 |
| 6 | Hold SPY | benchmark | 101.35 | 1.35 | 0 | — | 0.56 | 0.38 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.16 | 1.16 | 0 | — | 1.63 | 0.79 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.78 | 0.78 | 6 | 50.0 | -3.67 | -1.21 | -9.74 | 25 |
| 9 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.57 | 0.57 | 10 | 30.0 | 4.81 | 1.50 | -7.55 | 43 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.56 | 0.56 | 0 | — | -1.22 | -0.64 | -5.09 | 1 |
| 11 | Timing: Nasdaq FTD · TQQQ | daily | 100.41 | 0.41 | 0 | — | -5.08 | -0.83 | -15.27 | 1 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.00 | 0.00 | 0 | — | 3.42 | 1.35 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.58 | -0.42 | 0 | — | -4.71 | -2.17 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 4.88 | 2.37 | -1.95 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 18 | Hold BTC | benchmark | 98.81 | -1.19 | 0 | — | 29.21 | 3.44 | -8.68 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 97.98 | -2.02 | 31 | 12.9 | 14.68 | 1.72 | -16.92 | 113 |
| 20 | Trend pullback · 1h | trend | 97.79 | -2.21 | 78 | 23.1 | -23.07 | -6.44 | -25.60 | 168 |
| 21 | Max aggression: 1-day momentum | meta | 97.59 | -2.41 | 11 | 36.4 | -17.09 | -0.65 | -37.31 | 42 |
| 22 | Daily: Bullish score | daily | 97.51 | -2.49 | 4 | 0.0 | 0.47 | 0.26 | -12.76 | 11 |
| 23 | Stochastic reversion · 1h | reversion | 97.19 | -2.81 | 96 | 53.1 | -11.75 | -2.27 | -13.87 | 340 |
| 24 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 25 | Z-score reversion · 1h | reversion | 96.76 | -3.24 | 44 | 43.2 | 3.35 | 0.79 | -8.60 | 158 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 96.74 | -3.26 | 0 | — | 8.35 | 1.40 | -8.33 | 1 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -2.57 | -0.22 | -17.67 | 39 |
| 28 | Agent (rotation) | meta | 96.46 | -3.54 | 82 | 29.3 | -14.07 | -4.26 | -18.24 | 306 |
| 29 | ADX DI cross · 1h | trend | 96.38 | -3.62 | 62 | 19.4 | -7.54 | -1.27 | -13.69 | 254 |
| 30 | MACD cross · 1h | trend | 95.64 | -4.36 | 124 | 23.4 | -12.35 | -2.04 | -17.27 | 462 |
| 31 | EMA 20/50 cross · 1h | trend | 95.36 | -4.64 | 45 | 15.6 | 3.01 | 0.55 | -23.45 | 137 |
| 32 | Agent | meta | 95.28 | -4.72 | 58 | 50.0 | -8.83 | -4.23 | -8.92 | 236 |
| 33 | Parabolic SAR · 1h | trend | 95.23 | -4.77 | 85 | 22.4 | 1.03 | 0.32 | -21.52 | 291 |
| 34 | Supertrend · 1h | trend | 94.36 | -5.64 | 58 | 13.8 | 1.07 | 0.33 | -18.92 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.27 | 2.11 | -6.21 | 201 |
| 36 | Squeeze breakout · 1h | breakout | 93.53 | -6.46 | 39 | 23.1 | 4.11 | 0.92 | -9.46 | 102 |
| 37 | Agent (aggressive) | meta | 93.16 | -6.84 | 29 | 37.9 | -6.86 | -2.98 | -6.86 | 116 |
| 38 | MFI reversion · 1h | reversion | 93.12 | -6.88 | 145 | 33.1 | -8.62 | -1.32 | -17.05 | 128 |
| 39 | RSI momentum · 1h | momentum | 92.46 | -7.54 | 66 | 15.2 | 0.45 | 0.26 | -21.63 | 228 |
| 40 | Connors RSI(2) · 1h | reversion | 92.40 | -7.60 | 115 | 43.5 | -19.00 | -6.27 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.20 | -7.80 | 436 | 17.9 | -4.00 | -0.60 | -13.81 | 390 |
| 42 | RSI(14) reversion · 1h | reversion | 91.69 | -8.31 | 31 | 29.0 | -4.58 | -0.91 | -9.03 | 143 |
| 43 | Volume breakout · 1h | breakout | 91.50 | -8.50 | 68 | 19.1 | 8.86 | 1.35 | -12.60 | 118 |
| 44 | Bollinger reversion · 1h | reversion | 91.30 | -8.70 | 83 | 37.3 | -23.92 | -5.90 | -24.73 | 319 |
| 45 | Ichimoku · 1h | trend | 90.95 | -9.05 | 47 | 17.0 | 0.51 | 0.27 | -22.34 | 127 |
| 46 | Bollinger breakout · 1h | breakout | 90.86 | -9.14 | 74 | 28.4 | 8.30 | 1.20 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.63 | -9.37 | 71 | 15.5 | -7.93 | -0.72 | -27.16 | 239 |
| 48 | Opening range 30m | breakout | 89.57 | -10.44 | 152 | 21.7 | -15.66 | -4.71 | -15.97 | 569 |
| 49 | Williams %R · 1h | reversion | 89.52 | -10.48 | 132 | 46.2 | -26.37 | -4.45 | -27.73 | 504 |
| 50 | CCI reversion · 1h | reversion | 88.58 | -11.42 | 111 | 45.9 | -10.70 | -1.43 | -14.35 | 404 |
| 51 | OBV trend · 1h | momentum | 88.54 | -11.46 | 150 | 18.7 | -9.13 | -0.84 | -28.76 | 323 |
| 52 | VWAP momentum · 1h | momentum | 88.31 | -11.69 | 308 | 23.4 | -33.38 | -4.98 | -40.22 | 1253 |
| 53 | Candlestick reversal · 1h | reversion | 88.08 | -11.92 | 127 | 31.5 | -29.02 | -5.64 | -29.61 | 497 |
| 54 | Heikin-Ashi · 1h | trend | 87.81 | -12.19 | 152 | 28.3 | -30.24 | -5.01 | -37.57 | 682 |
| 55 | MACD zero-line · 1h | trend | 87.63 | -12.37 | 67 | 17.9 | -20.46 | -3.71 | -21.40 | 233 |
| 56 | Donchian 20/10 · 1h | breakout | 87.53 | -12.47 | 63 | 17.5 | -0.80 | 0.11 | -19.51 | 214 |
| 57 | Max aggression: 5-day momentum | meta | 87.32 | -12.68 | 7 | 28.6 | -15.13 | -1.12 | -34.64 | 28 |
| 58 | EMA 9/21 cross · 1h | trend | 87.03 | -12.97 | 108 | 13.0 | -8.64 | -0.91 | -23.04 | 333 |
| 59 | Opening range 15m | breakout | 86.80 | -13.20 | 180 | 20.0 | -18.22 | -5.02 | -19.41 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.65 | -13.35 | 45 | 20.0 | -10.51 | -1.14 | -26.77 | 217 |
| 61 | Three white soldiers | momentum | 86.54 | -13.46 | 152 | 17.1 | -48.68 | -23.38 | -48.68 | 589 |
| 62 | ROC + volume · 1h | momentum | 85.45 | -14.55 | 157 | 20.4 | -9.24 | -1.07 | -25.03 | 400 |
| 63 | ROC + volume | momentum | 72.84 | -27.16 | 417 | 22.5 | -72.85 | -16.46 | -74.37 | 1657 |
| 64 | RSI(14) reversion | reversion | 70.79 | -29.21 | 406 | 26.8 | -72.66 | -17.74 | -72.71 | 1472 |
| 65 | Squeeze breakout | breakout | 69.93 | -30.07 | 347 | 15.3 | -62.04 | -17.88 | -62.06 | 1217 |
| 66 | Volume breakout | breakout | 69.59 | -30.41 | 274 | 14.2 | -61.82 | -17.48 | -61.85 | 893 |
| 67 | EMA 20/50 cross | trend | 68.15 | -31.85 | 351 | 19.7 | -76.15 | -14.91 | -76.19 | 1426 |
| 68 | Donchian 55/20 | breakout | 67.04 | -32.96 | 357 | 17.6 | -68.05 | -14.27 | -68.91 | 1289 |
| 69 | VWAP reversion | reversion | 65.45 | -34.55 | 438 | 25.6 | -71.35 | -15.64 | -71.39 | 1407 |
| 70 | Keltner breakout | breakout | 60.71 | -39.29 | 478 | 14.6 | -83.32 | -27.06 | -83.38 | 1839 |
| 71 | Supertrend | trend | 60.32 | -39.68 | 496 | 19.2 | -86.00 | -20.74 | -86.00 | 1893 |
| 72 | AI bee: Boozy | ai | 59.82 | -40.18 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.34 | -42.66 | 433 | 9.9 | -82.23 | -22.88 | -82.23 | 1734 |
| 74 | Z-score reversion | reversion | 55.72 | -44.28 | 550 | 21.5 | -85.69 | -22.81 | -85.71 | 2066 |
| 75 | AI bee: Bizzy | ai | 55.53 | -44.47 | 886 | 8.4 | — | — | — | — |
| 76 | MFI reversion | reversion | 55.40 | -44.60 | 604 | 19.0 | -87.97 | -27.87 | -87.99 | 2120 |
| 77 | ADX DI cross | trend | 53.84 | -46.16 | 589 | 9.8 | -89.10 | -33.85 | -89.10 | 2106 |
| 78 | Donchian 20/10 | breakout | 52.17 | -47.83 | 673 | 17.5 | -90.91 | -25.71 | -90.91 | 2641 |
| 79 | MACD zero-line | trend | 51.21 | -48.79 | 627 | 14.4 | -91.44 | -29.30 | -91.44 | 2341 |
| 80 | RSI momentum | momentum | 50.63 | -49.37 | 652 | 16.6 | -90.50 | -25.30 | -90.50 | 2370 |
| 81 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.28 | -98.64 | 5340 |
| 82 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.31 | -26.41 | -91.31 | 2329 |
| 83 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.20 | -29.67 | -93.20 | 2602 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -32.49 | -97.35 | 3515 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.39 | -35.23 | -96.39 | 3585 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.27 | -25.22 | -94.27 | 2637 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.00 | -99.35 | 5647 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -30.93 | -96.32 | 3604 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.80 | -99.73 | 6155 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -37.35 | -97.37 | 3667 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.27 | -98.49 | 4664 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.41 | -32.46 | -93.41 | 2792 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.08 | -99.53 | 6104 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -32.64 | -95.90 | 3724 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -33.75 | -95.73 | 4055 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.20 | -99.89 | 8203 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T19:25 | Agent (ML meta-label) | buy | LABU | 4.61 | — | following Donchian 20/10 |
| 2026-10-12T19:25 | Agent (ML meta-label) | buy | IWM | 5.12 | — | entry |
| 2026-10-12T19:25 | MFI reversion · 1h | buy | SOXL | 4.73 | — | rebalance up |
| 2026-10-12T19:25 | MFI reversion · 1h | buy | QQQ | 4.67 | — | rebalance up |
| 2026-10-12T19:25 | MFI reversion · 1h | sell | NVDA | 18.60 | -0.01 | target is flat |
| 2026-10-12T19:25 | ROC + volume · 1h | sell | AMZN | 6.57 | -0.01 | target is flat |
| 2026-10-12T19:25 | MFI reversion | buy | TECL | 6.16 | — | entry |
| 2026-10-12T19:25 | MFI reversion | sell | ETHU | 6.16 | 0.01 | target is flat |
| 2026-10-12T19:25 | VWAP reversion | sell | TNA | 3.84 | -0.01 | target is flat |
| 2026-10-12T19:25 | VWAP reversion | sell | ETHU | 3.85 | 0.01 | target is flat |
| 2026-10-12T19:25 | Keltner breakout | buy | AAPL | 15.18 | — | entry signal |
| 2026-10-12T19:25 | Donchian 20/10 | buy | BTC-USD | 2.64 | — | entry signal |
| 2026-10-12T19:25 | Donchian 20/10 | sell | AAPL | 2.63 | 0.00 | rebalance down |
| 2026-10-12T19:22 | AI bee: Bizzy | buy | GOOGL | 7.96 | — | Jev: buy (buy p=0.57) |
| 2026-10-12T19:20 | Agent (ML meta-label) | sell | TSLA | 5.41 | -0.00 | selected signal exited |
| 2026-10-12T19:20 | Agent (ML meta-label) | sell | QQQ | 4.32 | -0.00 | selected signal exited |
| 2026-10-12T19:20 | MFI reversion · 1h | buy | SOXL | 18.52 | — | entry |
| 2026-10-12T19:20 | MFI reversion · 1h | buy | NVDA | 18.62 | — | entry |
| 2026-10-12T19:20 | MFI reversion · 1h | sell | QQQ | 4.66 | -0.01 | rebalance down |
| 2026-10-12T19:20 | MFI reversion · 1h | sell | BITX | 23.26 | -0.01 | target is flat |
| 2026-10-12T19:20 | ROC + volume · 1h | buy | PLTR | 6.57 | — | entry |
| 2026-10-12T19:20 | MFI reversion | buy | ETHU | 6.15 | — | entry |
| 2026-10-12T19:20 | MFI reversion | sell | TECL | 3.13 | -0.00 | target is flat |
| 2026-10-12T19:20 | MFI reversion | sell | IWM | 5.53 | -0.01 | target is flat |
| 2026-10-12T19:20 | VWAP reversion | buy | TNA | 3.85 | — | entry |
| 2026-10-12T19:20 | VWAP reversion | buy | ETHU | 3.85 | — | entry |
| 2026-10-12T19:20 | VWAP reversion | sell | TQQQ | 3.85 | 0.00 | target is flat |
| 2026-10-12T19:20 | VWAP reversion | sell | PLTR | 3.63 | -0.00 | target is flat |
| 2026-10-12T19:20 | Z-score reversion | buy | ETHU | 4.64 | — | entry |
| 2026-10-12T19:20 | Z-score reversion | sell | GOOGL | 4.66 | 0.01 | exit signal |
| 2026-10-12T19:20 | RSI(14) reversion | buy | MSTR | 7.07 | — | entry |
| 2026-10-12T19:20 | RSI(14) reversion | sell | GOOGL | 7.90 | 0.02 | exit signal |
| 2026-10-12T19:20 | Donchian 20/10 | buy | GOOGL | 13.04 | — | entry signal |
| 2026-10-12T19:20 | ADX DI cross | sell | AMZN | 13.46 | -0.05 | stop-loss |
| 2026-10-12T19:20 | MACD zero-line | buy | GOOGL | 12.80 | — | entry signal |
| 2026-10-12T19:15 | AI bee: Bizzy | sell | BITX | 8.05 | -0.04 | Jev: sell (sell p=0.89) after 10 min |
| 2026-10-12T19:15 | AI bee: Bizzy | sell | AAPL | 8.16 | -0.01 | Jev: sell (sell p=0.52) after 16 min |
| 2026-10-12T19:15 | MFI reversion · 1h | buy | QQQ | 4.66 | — | rebalance up |
| 2026-10-12T19:15 | MFI reversion · 1h | buy | BITX | 23.27 | — | entry |
| 2026-10-12T19:15 | MFI reversion · 1h | sell | SOXL | 18.54 | 0.04 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 19:25:05.000156+00:00 -> 2026-10-12 19:35:05.000156+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
