# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T19:57:05.000152+00:00 · 21659 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.12 (-4.88%)

Closed trades 64, win rate 46.9%, fees £2.37, max drawdown -5.38%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-13 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 35143 decisions in 2813 calls, $0.4338 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T19:57 | 2 / 22 / 7 | AMD 14% |  |
| Breezy | 2026-10-13T19:57 | 0 / 29 / 2 | cash |  |
| Boozy | 2026-10-13T19:57 | 1 / 28 / 2 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.22 | +2.54% | 5 |
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.20 | 3.20 | 0 | — | 2.46 | 1.24 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -10.88 | -3.16 | -13.79 | 118 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.51 | 1.51 | 18 | 50.0 | -15.61 | -2.49 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.66 | 1.73 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.07 | 1.07 | 0 | — | -0.19 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.15 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.35 | 0.35 | 0 | — | 0.27 | 0.18 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 4.89 | 1.89 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.80 | -0.20 | 0 | — | -2.42 | -1.34 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.28 | -0.72 | 0 | — | 30.50 | 3.54 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.84 | -1.16 | 0 | — | -8.47 | -1.53 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.50 | -1.50 | 0 | — | -5.08 | -2.34 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.71 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.91 | -2.08 | 82 | 25.6 | -22.56 | -6.38 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.61 | -2.39 | 32 | 12.5 | 7.17 | 1.00 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.42 | -2.58 | 5 | 0.0 | 0.48 | 0.26 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.51 | -3.12 | -9.69 | 308 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.78 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.61 | -3.39 | 63 | 19.0 | -10.60 | -1.93 | -14.11 | 248 |
| 26 | Stochastic reversion · 1h | reversion | 96.16 | -3.84 | 107 | 51.4 | -14.69 | -2.86 | -16.78 | 344 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.73 | -4.27 | 0 | — | 5.67 | 1.02 | -8.36 | 1 |
| 28 | EMA 20/50 cross · 1h | trend | 95.55 | -4.45 | 45 | 15.6 | 10.16 | 1.29 | -19.71 | 138 |
| 29 | MACD cross · 1h | trend | 95.52 | -4.48 | 131 | 23.7 | -8.99 | -1.17 | -19.25 | 458 |
| 30 | Max aggression: 1-day momentum | meta | 95.50 | -4.50 | 12 | 33.3 | -11.12 | -0.26 | -37.31 | 42 |
| 31 | Z-score reversion · 1h | reversion | 95.39 | -4.61 | 50 | 44.0 | 2.68 | 0.66 | -8.60 | 159 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -9.90 | -5.53 | -10.07 | 235 |
| 33 | Supertrend · 1h | trend | 94.06 | -5.94 | 60 | 13.3 | 3.38 | 0.62 | -20.32 | 212 |
| 34 | Squeeze breakout · 1h | breakout | 94.01 | -5.99 | 40 | 22.5 | 4.89 | 1.07 | -9.46 | 104 |
| 35 | Parabolic SAR · 1h | trend | 93.84 | -6.17 | 90 | 22.2 | 1.32 | 0.36 | -22.60 | 290 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -2.03 | -0.64 | -5.63 | 114 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.29 | 2.12 | -6.98 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.72 | -7.28 | 66 | 15.2 | 0.91 | 0.32 | -25.56 | 228 |
| 39 | MFI reversion · 1h | reversion | 92.33 | -7.67 | 165 | 31.5 | -6.70 | -1.00 | -17.05 | 133 |
| 40 | Connors RSI(2) · 1h | reversion | 92.16 | -7.84 | 127 | 42.5 | -19.85 | -5.85 | -22.90 | 254 |
| 41 | Ichimoku · 1h | trend | 91.39 | -8.62 | 48 | 16.7 | 1.75 | 0.41 | -22.34 | 126 |
| 42 | RSI(14) reversion · 1h | reversion | 91.35 | -8.65 | 37 | 32.4 | 5.92 | 1.37 | -9.40 | 125 |
| 43 | Agent (ML meta-label) | meta | 91.13 | -8.87 | 485 | 18.1 | -2.83 | -0.42 | -11.96 | 362 |
| 44 | Bollinger breakout · 1h | breakout | 90.77 | -9.23 | 77 | 28.6 | 7.36 | 1.09 | -14.21 | 278 |
| 45 | Triple EMA stack · 1h | trend | 90.77 | -9.23 | 71 | 15.5 | -7.17 | -0.54 | -32.27 | 240 |
| 46 | Volume breakout · 1h | breakout | 90.76 | -9.24 | 75 | 22.7 | 7.83 | 1.22 | -12.60 | 120 |
| 47 | Bollinger reversion · 1h | reversion | 89.90 | -10.10 | 97 | 37.1 | -23.93 | -5.79 | -24.98 | 322 |
| 48 | Williams %R · 1h | reversion | 89.30 | -10.70 | 143 | 45.5 | -28.10 | -4.79 | -29.91 | 509 |
| 49 | CCI reversion · 1h | reversion | 88.91 | -11.09 | 117 | 45.3 | -9.69 | -1.27 | -14.42 | 416 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.12 | -4.57 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.19 | -11.81 | 158 | 18.4 | -9.48 | -0.79 | -33.87 | 319 |
| 52 | MACD zero-line · 1h | trend | 87.74 | -12.26 | 69 | 17.4 | -21.84 | -4.26 | -22.68 | 227 |
| 53 | VWAP momentum · 1h | momentum | 87.52 | -12.48 | 325 | 23.1 | -33.88 | -5.06 | -40.35 | 1253 |
| 54 | Donchian 20/10 · 1h | breakout | 87.08 | -12.92 | 67 | 17.9 | 0.71 | 0.29 | -19.51 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 86.89 | -13.11 | 8 | 37.5 | -11.19 | -0.73 | -34.64 | 28 |
| 56 | Heikin-Ashi · 1h | trend | 86.88 | -13.12 | 164 | 26.8 | -29.94 | -4.95 | -38.32 | 678 |
| 57 | Keltner breakout · 1h | breakout | 86.78 | -13.22 | 49 | 20.4 | -7.56 | -0.79 | -26.77 | 214 |
| 58 | Three white soldiers | momentum | 86.76 | -13.24 | 161 | 18.6 | -47.51 | -22.15 | -47.87 | 584 |
| 59 | EMA 9/21 cross · 1h | trend | 86.74 | -13.26 | 110 | 12.7 | -10.62 | -1.36 | -24.14 | 327 |
| 60 | Candlestick reversal · 1h | reversion | 86.47 | -13.53 | 140 | 30.7 | -29.50 | -5.75 | -30.01 | 472 |
| 61 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.30 | -5.03 | -20.82 | 698 |
| 62 | ROC + volume · 1h | momentum | 85.43 | -14.57 | 173 | 20.2 | -9.82 | -1.15 | -25.60 | 394 |
| 63 | ROC + volume | momentum | 71.59 | -28.41 | 452 | 22.6 | -72.70 | -16.36 | -74.63 | 1660 |
| 64 | Volume breakout | breakout | 68.17 | -31.83 | 290 | 14.5 | -61.62 | -17.48 | -61.62 | 890 |
| 65 | Squeeze breakout | breakout | 67.97 | -32.03 | 375 | 15.5 | -62.37 | -17.98 | -62.37 | 1219 |
| 66 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.81 | -17.22 | -74.18 | 1494 |
| 67 | EMA 20/50 cross | trend | 66.92 | -33.08 | 383 | 20.6 | -76.35 | -14.96 | -76.38 | 1439 |
| 68 | Donchian 55/20 | breakout | 65.11 | -34.89 | 381 | 17.3 | -68.53 | -14.36 | -69.93 | 1279 |
| 69 | VWAP reversion | reversion | 62.55 | -37.45 | 487 | 25.5 | -71.79 | -15.27 | -71.79 | 1388 |
| 70 | Supertrend | trend | 60.22 | -39.78 | 535 | 20.2 | -85.58 | -20.22 | -85.64 | 1909 |
| 71 | AI bee: Boozy | ai | 60.12 | -39.88 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.10 | -40.90 | 524 | 14.7 | -83.26 | -26.79 | -83.26 | 1848 |
| 73 | Ichimoku | trend | 55.24 | -44.76 | 470 | 9.8 | -82.30 | -22.88 | -82.31 | 1726 |
| 74 | AI bee: Bizzy | ai | 53.90 | -46.09 | 941 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.23 | -46.77 | 668 | 20.2 | -87.77 | -27.63 | -87.77 | 2105 |
| 76 | Z-score reversion | reversion | 52.56 | -47.44 | 618 | 23.3 | -86.18 | -22.15 | -86.22 | 2087 |
| 77 | ADX DI cross | trend | 51.93 | -48.07 | 644 | 10.6 | -89.22 | -33.67 | -89.22 | 2120 |
| 78 | Donchian 20/10 | breakout | 50.89 | -49.11 | 732 | 17.3 | -90.70 | -25.29 | -90.70 | 2625 |
| 79 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -29.14 | -98.49 | 5288 |
| 80 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -29.50 | -93.21 | 2606 |
| 81 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.19 | -24.52 | -90.20 | 2368 |
| 82 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.60 | -26.95 | -91.61 | 2353 |
| 83 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.28 | -31.78 | -97.28 | 3524 |
| 84 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.40 | -35.16 | -96.40 | 3580 |
| 85 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.31 | -24.93 | -94.31 | 2625 |
| 86 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.99 | -99.36 | 5651 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.33 | -31.04 | -96.33 | 3590 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.24 | -99.72 | 6160 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.36 | -29.11 | -91.36 | 2353 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.29 | -97.37 | 3673 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.86 | -98.52 | 4674 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.34 | -32.05 | -93.34 | 2795 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.82 | -99.54 | 6123 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.00 | -32.40 | -96.00 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.65 | -33.41 | -95.65 | 4040 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.23 | -99.89 | 8213 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T19:55 | Agent (rotation) | sell | TQQQ | 32.40 | 0.35 | selected signal exited |
| 2026-10-13T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 100.53 | 0.01 | target is flat |
| 2026-10-13T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 101.41 | 1.10 | target is flat |
| 2026-10-13T19:55 | Agent | sell | IWM | 19.00 | -0.04 | selected signal exited |
| 2026-10-13T19:55 | MFI reversion · 1h | buy | TECL | 10.73 | — | entry |
| 2026-10-13T19:55 | MFI reversion · 1h | sell | TNA | 10.73 | -0.03 | target is flat |
| 2026-10-13T19:55 | MFI reversion | sell | UPRO | 10.67 | 0.01 | end-of-day flatten |
| 2026-10-13T19:55 | MFI reversion | sell | SPY | 10.65 | -0.01 | end-of-day flatten |
| 2026-10-13T19:55 | MFI reversion | sell | QQQ | 13.30 | -0.01 | end-of-day flatten |
| 2026-10-13T19:55 | MFI reversion | sell | ETHU | 13.33 | -0.03 | end-of-day flatten |
| 2026-10-13T19:55 | VWAP reversion | sell | MSTR | 15.74 | 0.03 | end-of-day flatten |
| 2026-10-13T19:55 | VWAP reversion | sell | MSFT | 15.65 | -0.07 | end-of-day flatten |
| 2026-10-13T19:55 | VWAP reversion | sell | LABU | 12.47 | -0.13 | end-of-day flatten |
| 2026-10-13T19:55 | VWAP reversion | sell | AMZN | 15.65 | -0.01 | end-of-day flatten |
| 2026-10-13T19:55 | Z-score reversion | sell | LABU | 13.03 | -0.14 | end-of-day flatten |
| 2026-10-13T19:55 | Z-score reversion | sell | AMZN | 13.18 | -0.03 | end-of-day flatten |
| 2026-10-13T19:55 | Squeeze breakout | sell | IWM | 13.67 | -0.03 | end-of-day flatten |
| 2026-10-13T19:55 | Keltner breakout | sell | UPRO | 11.83 | -0.02 | end-of-day flatten |
| 2026-10-13T19:55 | Keltner breakout | sell | TNA | 11.83 | -0.04 | end-of-day flatten |
| 2026-10-13T19:55 | Keltner breakout | sell | SPY | 14.79 | -0.02 | end-of-day flatten |
| 2026-10-13T19:55 | Keltner breakout | sell | IWM | 11.84 | -0.03 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 30m | sell | TSLA | 17.62 | 0.04 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 30m | sell | SOXL | 15.00 | 0.31 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 30m | sell | NVDA | 14.81 | 0.12 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 30m | sell | COIN | 14.71 | -0.04 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 30m | sell | AMD | 17.77 | 0.32 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 15m | sell | TSLA | 14.26 | 0.02 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 15m | sell | SOXL | 10.91 | 0.21 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 15m | sell | NVDA | 11.44 | 0.09 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 15m | sell | META | 14.25 | 0.01 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 15m | sell | COIN | 14.28 | 0.04 | end-of-day flatten |
| 2026-10-13T19:55 | Opening range 15m | sell | AMD | 12.39 | 0.31 | end-of-day flatten |
| 2026-10-13T19:55 | Donchian 55/20 | sell | UPRO | 16.03 | -0.03 | end-of-day flatten |
| 2026-10-13T19:55 | Donchian 55/20 | sell | SPY | 16.23 | -0.03 | end-of-day flatten |
| 2026-10-13T19:55 | Donchian 55/20 | sell | NVDA | 16.35 | 0.03 | end-of-day flatten |
| 2026-10-13T19:55 | Donchian 55/20 | sell | AMD | 16.51 | 0.19 | end-of-day flatten |
| 2026-10-13T19:55 | Donchian 20/10 | sell | UPRO | 7.27 | -0.02 | end-of-day flatten |
| 2026-10-13T19:55 | Donchian 20/10 | sell | TNA | 5.67 | -0.02 | end-of-day flatten |
| 2026-10-13T19:55 | Donchian 20/10 | sell | SPY | 5.68 | -0.01 | end-of-day flatten |
| 2026-10-13T19:55 | Donchian 20/10 | sell | NVDA | 5.69 | 0.02 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 19:57:05.000152+00:00 -> 2026-10-13 20:07:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
