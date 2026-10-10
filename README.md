# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T21:25:05.000142+00:00 · 18338 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.94 (-4.06%)

Closed trades 53, win rate 54.7%, fees £2.10, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 16102 decisions in 3221 calls, $0.2250 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T21:25 | 1 / 2 / 2 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-10T21:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T21:25 | 2 / 3 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Z-score reversion | TNA | 1.94 | +3.40% | 7 |
| Keltner breakout | LABU | 1.94 | +8.17% | 7 |
| Bollinger reversion | TECL | 1.82 | +2.00% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.79 | -2.38 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -13.59 | -2.18 | -22.02 | 69 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.50 | -0.55 | -37.31 | 43 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.22 | 2.44 | -1.58 | 86 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 18 | Hold BTC | benchmark | 99.25 | -0.76 | 0 | — | 26.93 | 3.23 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -10.80 | -2.10 | -14.73 | 344 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.80 | -3.20 | 38 | 13.2 | 5.88 | 0.86 | -19.85 | 133 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -0.30 | 0.04 | -10.38 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -2.50 | -0.22 | -13.84 | 261 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.66 | -0.18 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.87 | -4.13 | 110 | 24.5 | -15.80 | -2.55 | -17.84 | 469 |
| 34 | Supertrend · 1h | trend | 95.35 | -4.65 | 52 | 13.5 | -0.09 | 0.18 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.01 | -5.99 | 36 | 25.0 | 23.92 | 3.26 | -8.82 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.27 | -1.79 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -3.26 | -0.61 | -9.03 | 154 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Ichimoku · 1h | trend | 92.95 | -7.05 | 41 | 19.5 | -0.13 | 0.19 | -20.02 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -1.70 | -0.16 | -12.16 | 405 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.85 | -4.99 | -23.54 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.38 | 0.61 | -17.07 | 224 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Williams %R · 1h | reversion | 91.76 | -8.24 | 120 | 47.5 | -24.17 | -4.16 | -26.91 | 511 |
| 47 | Bollinger breakout · 1h | breakout | 91.74 | -8.26 | 68 | 29.4 | 6.31 | 0.98 | -12.90 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.49 | -0.84 | -26.38 | 235 |
| 50 | Candlestick reversal · 1h | reversion | 90.23 | -9.77 | 115 | 31.3 | -27.60 | -5.42 | -29.43 | 518 |
| 51 | CCI reversion · 1h | reversion | 89.78 | -10.22 | 100 | 45.0 | -8.60 | -1.11 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.71 | -10.29 | 278 | 22.3 | -34.04 | -5.13 | -39.30 | 1282 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 89.12 | -10.88 | 62 | 19.4 | -6.68 | -0.72 | -19.79 | 242 |
| 55 | Donchian 20/10 · 1h | breakout | 88.84 | -11.16 | 58 | 19.0 | -0.12 | 0.19 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.22 | -1.39 | -28.63 | 318 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.63 | -5.15 | -36.60 | 701 |
| 58 | Three white soldiers | momentum | 88.02 | -11.98 | 136 | 18.4 | -47.91 | -23.25 | -47.91 | 588 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.87 | -12.13 | 101 | 13.9 | -8.91 | -1.00 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.61 | -1.29 | -23.91 | 413 |
| 63 | RSI(14) reversion | reversion | 75.28 | -24.72 | 355 | 28.7 | -72.63 | -18.17 | -72.71 | 1491 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.77 | -16.62 | -73.79 | 1668 |
| 65 | Squeeze breakout | breakout | 71.40 | -28.60 | 322 | 14.9 | -62.57 | -18.42 | -62.58 | 1233 |
| 66 | EMA 20/50 cross | trend | 70.96 | -29.04 | 321 | 20.2 | -77.31 | -15.44 | -77.33 | 1462 |
| 67 | Donchian 55/20 | breakout | 70.91 | -29.09 | 326 | 18.1 | -67.56 | -14.45 | -67.57 | 1292 |
| 68 | Volume breakout | breakout | 70.39 | -29.61 | 259 | 13.1 | -62.76 | -18.14 | -62.76 | 902 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -72.03 | -16.32 | -72.18 | 1440 |
| 70 | Supertrend | trend | 65.22 | -34.78 | 448 | 20.3 | -86.31 | -21.16 | -86.32 | 1919 |
| 71 | Keltner breakout | breakout | 63.41 | -36.59 | 441 | 14.5 | -83.90 | -27.90 | -83.90 | 1850 |
| 72 | Z-score reversion | reversion | 61.19 | -38.81 | 486 | 23.5 | -85.53 | -23.23 | -85.53 | 2083 |
| 73 | Ichimoku | trend | 60.64 | -39.36 | 401 | 9.7 | -81.90 | -23.59 | -81.90 | 1751 |
| 74 | AI bee: Boozy | ai | 60.55 | -39.45 | 253 | 5.1 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.53 | -39.47 | 498 | 21.7 | -87.65 | -28.46 | -87.67 | 2123 |
| 76 | AI bee: Bizzy | ai | 59.05 | -40.95 | 811 | 9.0 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.54 | -42.46 | 531 | 10.4 | -89.51 | -34.50 | -89.51 | 2128 |
| 78 | Donchian 20/10 | breakout | 56.49 | -43.51 | 622 | 18.3 | -90.83 | -26.21 | -90.84 | 2666 |
| 79 | RSI momentum | momentum | 55.73 | -44.27 | 588 | 17.3 | -90.37 | -25.80 | -90.37 | 2384 |
| 80 | Trend pullback ⏸ | trend | 55.45 | -44.55 | 581 | 15.0 | -90.90 | -27.14 | -90.90 | 2333 |
| 81 | MACD zero-line | trend | 55.33 | -44.67 | 568 | 15.1 | -91.61 | -29.91 | -91.62 | 2367 |
| 82 | Triple EMA stack | trend | 54.17 | -45.83 | 616 | 15.6 | -93.22 | -30.54 | -93.22 | 2620 |
| 83 | Bollinger breakout | breakout | 51.92 | -48.09 | 653 | 14.4 | -93.55 | -33.25 | -93.55 | 2819 |
| 84 | Consensus | meta | 50.72 | -49.27 | 614 | 9.9 | -94.27 | -26.23 | -94.27 | 2696 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.61 | -98.69 | 5403 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -33.26 | -97.39 | 3550 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -36.70 | -96.48 | 3615 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.20 | -99.34 | 5696 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -31.88 | -96.32 | 3613 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.62 | -99.73 | 6207 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -38.89 | -97.37 | 3688 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.51 | -98.47 | 4716 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.56 | -99.51 | 6148 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.83 | -33.65 | -95.83 | 3742 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.61 | -35.27 | -95.61 | 4090 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.84 | -99.90 | 8324 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T21:25 | Triple EMA stack | sell | SOL-USD | 13.47 | -0.09 | exit signal |
| 2026-10-10T21:20 | Triple EMA stack | buy | SOL-USD | 13.57 | — | entry signal |
| 2026-10-10T21:15 | Triple EMA stack | sell | SOL-USD | 13.59 | -0.08 | exit signal |
| 2026-10-10T21:10 | Consensus | sell | BTC-USD | 12.62 | -0.08 | target is flat |
| 2026-10-10T21:10 | Volume breakout | sell | XRP-USD | 17.52 | -0.10 | exit signal |
| 2026-10-10T21:10 | Donchian 55/20 | sell | BTC-USD | 14.28 | -0.08 | exit signal |
| 2026-10-10T21:10 | Triple EMA stack | sell | BTC-USD | 13.51 | -0.09 | exit signal |
| 2026-10-10T21:05 | Consensus | buy | BTC-USD | 12.70 | — | entry |
| 2026-10-10T21:03 | AI bee: Bizzy | sell | DOGE-USD | 8.61 | -0.06 | Jev: sell (sell p=0.74) after 10 min |
| 2026-10-10T21:00 | Consensus | sell | BTC-USD | 12.65 | -0.08 | target is flat |
| 2026-10-10T21:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 8.57 | — | entry signal |
| 2026-10-10T21:00 | MFI reversion | sell | XRP-USD | 15.11 | -0.04 | exit signal |
| 2026-10-10T21:00 | ADX DI cross | sell | ETH-USD | 14.30 | -0.11 | exit signal |
| 2026-10-10T20:55 | ADX DI cross | buy | ETH-USD | 14.41 | — | entry signal |
| 2026-10-10T20:53 | AI bee: Bizzy | buy | DOGE-USD | 8.67 | — | Jev: buy (buy p=0.59) |
| 2026-10-10T20:50 | AI bee: Bizzy | sell | XRP-USD | 8.15 | -0.03 | Jev: sell (sell p=0.57) after 20 min |
| 2026-10-10T20:50 | Donchian 55/20 | buy | XRP-USD | 17.75 | — | entry signal |
| 2026-10-10T20:45 | Consensus | buy | XRP-USD | 12.73 | — | entry |
| 2026-10-10T20:45 | Consensus | buy | BTC-USD | 12.73 | — | entry |
| 2026-10-10T20:45 | Squeeze breakout | buy | XRP-USD | 17.86 | — | entry signal |
| 2026-10-10T20:45 | Keltner breakout | buy | XRP-USD | 15.86 | — | entry signal |
| 2026-10-10T20:45 | Triple EMA stack | buy | BTC-USD | 13.60 | — | entry signal |
| 2026-10-10T20:40 | Volume breakout | buy | XRP-USD | 17.62 | — | entry signal |
| 2026-10-10T20:40 | Bollinger breakout | buy | XRP-USD | 12.99 | — | entry signal |
| 2026-10-10T20:40 | Supertrend | buy | XRP-USD | 16.32 | — | entry signal |
| 2026-10-10T20:35 | Triple EMA stack | sell | BTC-USD | 13.57 | -0.09 | exit signal |
| 2026-10-10T20:30 | AI bee: Bizzy | buy | XRP-USD | 8.19 | — | Jev: buy (buy p=0.55) |
| 2026-10-10T20:30 | Consensus | sell | BTC-USD | 12.68 | -0.08 | target is flat |
| 2026-10-10T20:30 | Donchian 20/10 | sell | BTC-USD | 14.03 | -0.10 | stop-loss |
| 2026-10-10T20:30 | RSI momentum | sell | BTC-USD | 13.84 | -0.10 | stop-loss |
| 2026-10-10T20:30 | Triple EMA stack | buy | XRP-USD | 13.61 | — | entry signal |
| 2026-10-10T20:25 | MACD zero-line | sell | BTC-USD | 13.79 | -0.09 | exit signal |
| 2026-10-10T20:20 | Squeeze breakout | sell | XRP-USD | 17.84 | -0.12 | exit signal |
| 2026-10-10T20:20 | Bollinger breakout | sell | XRP-USD | 12.97 | -0.09 | exit signal |
| 2026-10-10T20:20 | Donchian 55/20 | sell | ETH-USD | 17.65 | -0.14 | stop-loss |
| 2026-10-10T20:20 | Donchian 20/10 | sell | SOL-USD | 14.12 | -0.08 | exit signal |
| 2026-10-10T20:20 | RSI momentum | sell | ETH-USD | 13.93 | -0.10 | exit signal |
| 2026-10-10T20:20 | Supertrend | sell | ETH-USD | 13.12 | -0.02 | exit signal |
| 2026-10-10T20:20 | Triple EMA stack | sell | ETH-USD | 13.63 | -0.08 | exit signal |
| 2026-10-10T20:15 | Squeeze breakout | sell | SOL-USD | 17.87 | -0.09 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 21:25:05.000142+00:00 -> 2026-10-10 21:35:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
