# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T20:27:05.000179+00:00 · 21681 ticks

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

### Market regime (QQQ, 2026-10-13)

**Uptrend** since 2026-09-21 · level caution · 4 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.32 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.0, MSFT 7.9, BITX 6.5, META 6.1, MSTR 6.0, UPRO 5.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 35548 decisions in 2879 calls, $0.4392 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T20:27 | 1 / 3 / 1 | AMD 14% |  |
| Breezy | 2026-10-13T20:27 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T20:27 | 2 / 2 / 1 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.13 | 3.13 | 0 | — | 2.51 | 1.27 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -10.84 | -3.15 | -13.79 | 118 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.46 | 1.46 | 18 | 50.0 | -15.65 | -2.49 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.66 | 1.73 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.06 | 1.06 | 0 | — | -0.21 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.15 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.44 | 0.44 | 0 | — | 0.24 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 4.59 | 1.78 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.83 | -0.17 | 0 | — | -2.37 | -1.31 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.26 | -0.74 | 0 | — | 30.70 | 3.56 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.95 | -1.05 | 0 | — | -8.33 | -1.51 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.50 | -1.50 | 0 | — | -5.08 | -2.34 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.71 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.80 | -2.20 | 82 | 25.6 | -22.66 | -6.42 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.49 | -2.51 | 32 | 12.5 | 7.03 | 0.99 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.39 | -2.61 | 5 | 0.0 | 0.46 | 0.26 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -8.98 | -3.54 | -10.75 | 297 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.43 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.53 | -3.47 | 63 | 19.0 | -10.91 | -2.01 | -14.81 | 248 |
| 26 | Stochastic reversion · 1h | reversion | 96.24 | -3.76 | 107 | 51.4 | -14.39 | -2.80 | -16.52 | 345 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.77 | -4.23 | 0 | — | 5.88 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.58 | -4.42 | 131 | 23.7 | -8.94 | -1.16 | -19.25 | 458 |
| 29 | Z-score reversion · 1h | reversion | 95.43 | -4.57 | 50 | 44.0 | 2.77 | 0.68 | -8.60 | 159 |
| 30 | EMA 20/50 cross · 1h | trend | 95.39 | -4.61 | 45 | 15.6 | 10.11 | 1.29 | -20.35 | 137 |
| 31 | Max aggression: 1-day momentum | meta | 95.37 | -4.62 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.87 | -5.04 | -9.05 | 235 |
| 33 | Supertrend · 1h | trend | 93.98 | -6.01 | 60 | 13.3 | 2.19 | 0.47 | -20.32 | 213 |
| 34 | Squeeze breakout · 1h | breakout | 93.95 | -6.05 | 40 | 22.5 | 5.69 | 1.23 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.78 | -6.22 | 90 | 22.2 | 1.25 | 0.35 | -22.66 | 290 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.09 | -0.31 | -5.63 | 113 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.29 | 2.12 | -6.98 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.63 | -7.37 | 66 | 15.2 | 1.17 | 0.35 | -25.56 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.54 | -7.46 | 165 | 31.5 | -6.47 | -0.95 | -17.02 | 133 |
| 40 | Connors RSI(2) · 1h | reversion | 92.04 | -7.96 | 127 | 42.5 | -19.96 | -5.90 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.44 | -8.56 | 37 | 32.4 | 2.79 | 0.70 | -9.40 | 135 |
| 42 | Ichimoku · 1h | trend | 91.31 | -8.69 | 48 | 16.7 | 1.67 | 0.40 | -22.34 | 126 |
| 43 | Agent (ML meta-label) | meta | 91.08 | -8.92 | 485 | 18.1 | -3.59 | -0.54 | -11.96 | 380 |
| 44 | Triple EMA stack · 1h | trend | 90.69 | -9.31 | 71 | 15.5 | -7.44 | -0.57 | -32.27 | 240 |
| 45 | Volume breakout · 1h | breakout | 90.69 | -9.31 | 75 | 22.7 | 7.73 | 1.20 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 90.68 | -9.32 | 77 | 28.6 | 7.25 | 1.08 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 90.01 | -9.99 | 97 | 37.1 | -23.83 | -5.76 | -24.98 | 322 |
| 48 | Williams %R · 1h | reversion | 89.43 | -10.57 | 143 | 45.5 | -28.14 | -4.80 | -29.98 | 511 |
| 49 | CCI reversion · 1h | reversion | 88.96 | -11.04 | 117 | 45.3 | -9.82 | -1.29 | -14.42 | 416 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.55 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.11 | -11.89 | 158 | 18.4 | -9.73 | -0.82 | -33.90 | 320 |
| 52 | MACD zero-line · 1h | trend | 87.64 | -12.36 | 69 | 17.4 | -21.94 | -4.28 | -22.69 | 227 |
| 53 | VWAP momentum · 1h | momentum | 87.60 | -12.40 | 325 | 23.1 | -33.88 | -5.07 | -40.35 | 1253 |
| 54 | Heikin-Ashi · 1h | trend | 87.01 | -12.99 | 164 | 26.8 | -29.83 | -4.92 | -38.32 | 678 |
| 55 | Donchian 20/10 · 1h | breakout | 87.00 | -13.00 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 56 | Max aggression: 5-day momentum | meta | 86.78 | -13.22 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 57 | Three white soldiers | momentum | 86.76 | -13.24 | 161 | 18.6 | -47.51 | -22.15 | -47.87 | 584 |
| 58 | Keltner breakout · 1h | breakout | 86.69 | -13.31 | 49 | 20.4 | -8.10 | -0.87 | -26.76 | 214 |
| 59 | EMA 9/21 cross · 1h | trend | 86.68 | -13.32 | 110 | 12.7 | -10.78 | -1.38 | -24.14 | 328 |
| 60 | Candlestick reversal · 1h | reversion | 86.59 | -13.41 | 140 | 30.7 | -30.69 | -5.94 | -31.45 | 483 |
| 61 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -5.03 | -20.82 | 698 |
| 62 | ROC + volume · 1h | momentum | 85.34 | -14.66 | 173 | 20.2 | -10.00 | -1.17 | -25.73 | 394 |
| 63 | ROC + volume | momentum | 71.59 | -28.41 | 452 | 22.6 | -72.70 | -16.36 | -74.63 | 1660 |
| 64 | Volume breakout | breakout | 68.17 | -31.83 | 290 | 14.5 | -61.62 | -17.48 | -61.62 | 890 |
| 65 | Squeeze breakout | breakout | 67.97 | -32.03 | 375 | 15.5 | -62.36 | -17.98 | -62.36 | 1220 |
| 66 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.77 | -17.18 | -74.14 | 1484 |
| 67 | EMA 20/50 cross | trend | 66.88 | -33.12 | 383 | 20.6 | -76.22 | -14.92 | -76.35 | 1437 |
| 68 | Donchian 55/20 | breakout | 65.11 | -34.89 | 381 | 17.3 | -68.53 | -14.36 | -69.93 | 1279 |
| 69 | VWAP reversion | reversion | 62.55 | -37.45 | 487 | 25.5 | -71.74 | -15.24 | -71.75 | 1387 |
| 70 | Supertrend | trend | 60.14 | -39.85 | 536 | 20.1 | -85.61 | -20.26 | -85.64 | 1910 |
| 71 | AI bee: Boozy | ai | 60.10 | -39.90 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.10 | -40.90 | 524 | 14.7 | -83.18 | -26.81 | -83.18 | 1846 |
| 73 | Ichimoku | trend | 55.24 | -44.76 | 470 | 9.8 | -82.20 | -22.86 | -82.24 | 1723 |
| 74 | AI bee: Bizzy | ai | 53.92 | -46.08 | 941 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.23 | -46.77 | 668 | 20.2 | -87.80 | -27.71 | -87.80 | 2106 |
| 76 | Z-score reversion | reversion | 52.56 | -47.44 | 618 | 23.3 | -86.18 | -22.15 | -86.22 | 2087 |
| 77 | ADX DI cross | trend | 51.92 | -48.08 | 644 | 10.6 | -89.27 | -33.61 | -89.27 | 2118 |
| 78 | Donchian 20/10 | breakout | 50.89 | -49.11 | 732 | 17.3 | -90.70 | -25.29 | -90.70 | 2625 |
| 79 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -29.10 | -98.49 | 5287 |
| 80 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.18 | -29.43 | -93.18 | 2601 |
| 81 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.18 | -24.51 | -90.18 | 2365 |
| 82 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.59 | -26.93 | -91.59 | 2352 |
| 83 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.29 | -31.81 | -97.29 | 3525 |
| 84 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -35.11 | -96.38 | 3573 |
| 85 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.41 | -25.50 | -94.41 | 2635 |
| 86 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.97 | -99.36 | 5627 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.34 | -31.05 | -96.34 | 3590 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.23 | -99.72 | 6158 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.37 | -29.14 | -91.37 | 2354 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.20 | -97.36 | 3673 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.80 | -98.52 | 4674 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.34 | -32.05 | -93.34 | 2795 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.79 | -99.54 | 6122 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.98 | -32.18 | -95.98 | 3738 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.65 | -33.45 | -95.65 | 4041 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.27 | -99.89 | 8214 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T20:20 | Supertrend | sell | SOL-USD | 14.99 | -0.12 | exit signal |
| 2026-10-13T20:00 | OBV trend · 1h | buy | BTC-USD | 4.12 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 20:27:05.000179+00:00 -> 2026-10-13 20:37:05.000179+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
