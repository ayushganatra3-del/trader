# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T12:25:05.000149+00:00 · 20210 ticks

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
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 9282 decisions in 1857 calls, $0.1300 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T12:25 | 0 / 3 / 2 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T12:25 | 1 / 4 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.53 | -2.27 | -13.79 | 116 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -12.39 | -2.03 | -20.64 | 68 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 17 | Hold BTC | benchmark | 99.39 | -0.61 | 0 | — | 29.19 | 3.44 | -8.68 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 99.19 | -0.81 | 28 | 14.3 | 12.64 | 1.58 | -16.96 | 114 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.72 | -1.86 | -14.61 | 336 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.87 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.32 | -2.68 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -23.23 | -6.54 | -25.39 | 166 |
| 27 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.92 | -2.30 | -10.19 | 268 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 29 | EMA 20/50 cross · 1h | trend | 96.62 | -3.38 | 40 | 12.5 | 5.98 | 0.87 | -19.85 | 136 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -0.25 | 0.12 | -13.84 | 252 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.27 | -0.13 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.69 | -4.31 | 120 | 24.2 | -14.85 | -2.36 | -17.27 | 469 |
| 34 | Supertrend · 1h | trend | 95.28 | -4.72 | 53 | 13.2 | 2.06 | 0.45 | -18.22 | 207 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.04 | -1.58 | -17.79 | 126 |
| 38 | Squeeze breakout · 1h | breakout | 93.43 | -6.57 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -1.92 | -0.31 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -2.86 | -0.38 | -13.41 | 417 |
| 42 | Bollinger reversion · 1h | reversion | 92.78 | -7.22 | 78 | 37.2 | -20.86 | -4.95 | -23.26 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.29 | 64 | 15.6 | 4.55 | 0.75 | -17.25 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.12 | -7.88 | 59 | 20.3 | 7.61 | 1.19 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 91.70 | -8.30 | 45 | 17.8 | -0.99 | 0.08 | -21.25 | 124 |
| 46 | Williams %R · 1h | reversion | 91.56 | -8.44 | 126 | 47.6 | -23.74 | -4.04 | -26.91 | 509 |
| 47 | Bollinger breakout · 1h | breakout | 91.25 | -8.75 | 72 | 27.8 | 6.18 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.13 | -0.79 | -26.54 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.42 | -9.58 | 118 | 33.1 | -25.57 | -4.92 | -27.86 | 503 |
| 51 | CCI reversion · 1h | reversion | 89.97 | -10.03 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.44 | -10.56 | 285 | 21.8 | -32.44 | -4.81 | -39.19 | 1278 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.43 | -1.40 | -28.57 | 324 |
| 55 | Donchian 20/10 · 1h | breakout | 88.70 | -11.30 | 60 | 18.3 | -0.83 | 0.11 | -18.23 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -29.76 | -4.94 | -36.60 | 700 |
| 57 | MACD zero-line · 1h | trend | 88.19 | -11.81 | 67 | 17.9 | -7.04 | -0.76 | -20.89 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.82 | -12.18 | 104 | 13.5 | -8.86 | -0.99 | -21.96 | 340 |
| 60 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -12.45 | -1.45 | -26.16 | 220 |
| 61 | Three white soldiers | momentum | 86.62 | -13.38 | 148 | 16.9 | -48.26 | -23.13 | -48.34 | 592 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.28 | -1.23 | -23.75 | 416 |
| 63 | ROC + volume | momentum | 73.80 | -26.20 | 402 | 22.9 | -73.13 | -16.64 | -74.22 | 1684 |
| 64 | RSI(14) reversion | reversion | 73.41 | -26.59 | 376 | 27.4 | -72.38 | -17.99 | -72.39 | 1488 |
| 65 | Squeeze breakout | breakout | 70.38 | -29.62 | 340 | 15.3 | -62.19 | -18.01 | -62.19 | 1234 |
| 66 | Volume breakout | breakout | 69.71 | -30.29 | 272 | 14.0 | -62.44 | -17.84 | -62.46 | 904 |
| 67 | EMA 20/50 cross | trend | 68.46 | -31.54 | 348 | 19.8 | -76.67 | -15.20 | -76.69 | 1452 |
| 68 | Donchian 55/20 | breakout | 68.19 | -31.81 | 350 | 18.0 | -68.04 | -14.50 | -68.35 | 1299 |
| 69 | VWAP reversion | reversion | 67.60 | -32.40 | 405 | 25.9 | -71.17 | -15.81 | -71.18 | 1426 |
| 70 | Supertrend | trend | 61.54 | -38.46 | 486 | 19.5 | -86.08 | -21.05 | -86.12 | 1915 |
| 71 | Keltner breakout | breakout | 61.17 | -38.83 | 470 | 14.5 | -83.73 | -27.75 | -83.74 | 1853 |
| 72 | AI bee: Boozy | ai | 59.96 | -40.04 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 58.46 | -41.55 | 425 | 10.1 | -82.00 | -23.21 | -82.00 | 1756 |
| 74 | Z-score reversion | reversion | 57.99 | -42.01 | 522 | 21.8 | -85.18 | -22.91 | -85.21 | 2073 |
| 75 | MFI reversion | reversion | 57.15 | -42.85 | 534 | 20.4 | -87.64 | -28.24 | -87.67 | 2123 |
| 76 | AI bee: Bizzy | ai | 55.94 | -44.05 | 871 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.58 | -45.42 | 565 | 10.1 | -89.31 | -35.22 | -89.31 | 2122 |
| 78 | Donchian 20/10 | breakout | 53.32 | -46.68 | 659 | 17.9 | -90.87 | -26.14 | -90.87 | 2669 |
| 79 | MACD zero-line | trend | 51.91 | -48.09 | 612 | 14.5 | -91.47 | -29.70 | -91.48 | 2365 |
| 80 | Trend pullback | trend | 51.55 | -48.45 | 625 | 14.4 | -91.29 | -27.09 | -91.29 | 2352 |
| 81 | RSI momentum | momentum | 51.53 | -48.47 | 637 | 16.6 | -90.55 | -25.85 | -90.55 | 2394 |
| 82 | Triple EMA stack | trend | 50.68 | -49.32 | 660 | 15.2 | -93.32 | -30.40 | -93.32 | 2630 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -31.08 | -98.65 | 5391 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -33.42 | -97.38 | 3553 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -36.33 | -96.51 | 3628 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.35 | -25.66 | -94.35 | 2708 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.91 | -99.35 | 5697 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.51 | -31.93 | -96.51 | 3645 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.84 | -99.73 | 6206 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -38.12 | -97.35 | 3692 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -36.60 | -98.45 | 4706 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.51 | -33.15 | -93.51 | 2820 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.24 | -99.52 | 6154 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.79 | -33.25 | -95.80 | 3740 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.66 | -34.34 | -95.66 | 4089 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.97 | -99.89 | 8302 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T12:25 | MFI reversion | sell | XRP-USD | 14.22 | -0.14 | stop-loss |
| 2026-10-12T12:25 | MFI reversion | sell | BTC-USD | 14.33 | -0.13 | stop-loss |
| 2026-10-12T12:20 | Supertrend | sell | DOGE-USD | 15.30 | -0.11 | target is flat |
| 2026-10-12T12:15 | MFI reversion | buy | XRP-USD | 14.36 | — | entry signal |
| 2026-10-12T12:15 | MFI reversion | buy | SOL-USD | 14.36 | — | entry signal |
| 2026-10-12T12:15 | Supertrend | buy | DOGE-USD | 15.41 | — | entry signal |
| 2026-10-12T12:00 | MACD cross · 1h | sell | ETH-USD | 3.70 | -0.01 | exit signal |
| 2026-10-12T11:55 | Z-score reversion | buy | XRP-USD | 14.55 | — | entry signal |
| 2026-10-12T11:55 | Z-score reversion | buy | SOL-USD | 14.55 | — | entry signal |
| 2026-10-12T11:55 | Z-score reversion | buy | ETH-USD | 14.55 | — | entry signal |
| 2026-10-12T11:55 | RSI(14) reversion | buy | SOL-USD | 18.39 | — | entry signal |
| 2026-10-12T11:50 | Z-score reversion | sell | SOL-USD | 14.48 | -0.17 | stop-loss |
| 2026-10-12T11:50 | Z-score reversion | sell | ETH-USD | 14.50 | -0.13 | stop-loss |
| 2026-10-12T11:45 | VWAP reversion | buy | XRP-USD | 16.93 | — | entry signal |
| 2026-10-12T11:40 | Z-score reversion | sell | XRP-USD | 14.50 | -0.14 | stop-loss |
| 2026-10-12T11:35 | MFI reversion | sell | XRP-USD | 14.32 | -0.14 | stop-loss |
| 2026-10-12T11:35 | RSI(14) reversion | sell | SOL-USD | 18.25 | -0.18 | stop-loss |
| 2026-10-12T11:35 | Supertrend | sell | DOGE-USD | 15.31 | -0.14 | exit signal |
| 2026-10-12T11:35 | MACD zero-line | sell | DOGE-USD | 12.89 | -0.12 | exit signal |
| 2026-10-12T11:30 | Z-score reversion | buy | ETH-USD | 14.63 | — | entry signal |
| 2026-10-12T11:25 | MFI reversion | sell | ETH-USD | 14.32 | -0.14 | stop-loss |
| 2026-10-12T11:05 | Three white soldiers | sell | DOGE-USD | 21.52 | -0.18 | exit signal |
| 2026-10-12T11:05 | Volume breakout | sell | DOGE-USD | 17.30 | -0.17 | stop-loss |
| 2026-10-12T11:05 | Donchian 20/10 | sell | DOGE-USD | 13.24 | -0.13 | stop-loss |
| 2026-10-12T11:05 | RSI momentum | sell | DOGE-USD | 12.79 | -0.13 | stop-loss |
| 2026-10-12T11:05 | ROC + volume | sell | DOGE-USD | 18.31 | -0.18 | stop-loss |
| 2026-10-12T11:00 | MACD zero-line · 1h | sell | DOGE-USD | 22.20 | -0.07 | exit signal |
| 2026-10-12T11:00 | MACD cross · 1h | sell | DOGE-USD | 5.09 | 0.05 | exit signal |
| 2026-10-12T11:00 | MFI reversion | buy | ETH-USD | 2.89 | — | rebalance up |
| 2026-10-12T11:00 | MFI reversion | buy | BTC-USD | 2.89 | — | rebalance up |
| 2026-10-12T11:00 | MFI reversion | sell | SOL-USD | 8.65 | -0.05 | exit signal |
| 2026-10-12T11:00 | MFI reversion | sell | DOGE-USD | 11.53 | -0.04 | exit signal |
| 2026-10-12T11:00 | MACD zero-line | buy | DOGE-USD | 13.01 | — | entry signal |
| 2026-10-12T10:55 | ADX DI cross | sell | SOL-USD | 13.56 | -0.11 | exit signal |
| 2026-10-12T10:50 | AI bee: Bizzy | sell | DOGE-USD | 7.81 | -0.04 | Jev: sell (sell p=0.51) after 10 min |
| 2026-10-12T10:50 | RSI momentum | buy | DOGE-USD | 12.91 | — | entry |
| 2026-10-12T10:50 | ROC + volume | buy | DOGE-USD | 18.50 | — | entry signal |
| 2026-10-12T10:50 | ADX DI cross | buy | SOL-USD | 13.67 | — | entry signal |
| 2026-10-12T10:45 | Z-score reversion | sell | DOGE-USD | 14.67 | -0.02 | exit signal |
| 2026-10-12T10:45 | Volume breakout | buy | DOGE-USD | 17.47 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 12:25:05.000149+00:00 -> 2026-10-12 12:35:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
