# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T10:25:05.000120+00:00 · 20108 ticks

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

Today: 7752 decisions in 1551 calls, $0.1085 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T10:25 | 0 / 2 / 3 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T10:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T10:25 | 1 / 2 / 2 | COIN 76% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.27 | 3.27 | 37 | 43.2 | -7.53 | -2.27 | -13.79 | 116 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.55 | 2.55 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.22 | 2.23 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.03 | 2.03 | 14 | 57.1 | -12.39 | -2.03 | -20.64 | 68 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.35 | 1.35 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.27 | 1.27 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.11 | 1.11 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.77 | -0.23 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 14 | Hold BTC | benchmark | 99.75 | -0.25 | 0 | — | 29.41 | 3.46 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.71 | -0.29 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Stochastic reversion · 1h | reversion | 99.14 | -0.86 | 89 | 55.1 | -9.72 | -1.86 | -14.61 | 336 |
| 19 | Donchian 55/20 · 1h | breakout | 99.12 | -0.88 | 28 | 14.3 | 12.72 | 1.59 | -16.96 | 114 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.61 | -1.39 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.58 | -1.42 | 0 | — | 11.52 | 1.87 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.82 | -2.18 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.31 | -2.69 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.18 | -2.82 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.06 | -2.94 | 78 | 23.1 | -23.23 | -6.54 | -25.39 | 166 |
| 27 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.87 | -2.29 | -10.19 | 268 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 29 | EMA 20/50 cross · 1h | trend | 96.61 | -3.39 | 40 | 12.5 | 6.17 | 0.89 | -19.85 | 136 |
| 30 | ADX DI cross · 1h | trend | 96.32 | -3.68 | 58 | 20.7 | -0.25 | 0.12 | -13.84 | 252 |
| 31 | Parabolic SAR · 1h | trend | 96.28 | -3.72 | 82 | 22.0 | -2.15 | -0.12 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.68 | -4.32 | 118 | 23.7 | -14.85 | -2.36 | -17.27 | 469 |
| 34 | Supertrend · 1h | trend | 95.41 | -4.59 | 53 | 13.2 | 2.19 | 0.47 | -18.22 | 207 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.50 | -6.50 | 119 | 34.5 | -10.04 | -1.58 | -17.79 | 126 |
| 38 | Squeeze breakout · 1h | breakout | 93.42 | -6.58 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.10 | -6.90 | 26 | 26.9 | -1.97 | -0.32 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.01 | -6.99 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.83 | -7.17 | 392 | 18.4 | -0.06 | 0.13 | -13.03 | 424 |
| 42 | Bollinger reversion · 1h | reversion | 92.75 | -7.25 | 78 | 37.2 | -20.86 | -4.95 | -23.26 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.67 | -7.33 | 64 | 15.6 | 4.68 | 0.76 | -17.17 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.10 | -7.90 | 59 | 20.3 | 7.61 | 1.19 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 91.73 | -8.27 | 45 | 17.8 | -1.32 | 0.04 | -21.18 | 125 |
| 46 | Williams %R · 1h | reversion | 91.54 | -8.46 | 126 | 47.6 | -23.74 | -4.04 | -26.91 | 509 |
| 47 | Bollinger breakout · 1h | breakout | 91.22 | -8.78 | 72 | 27.8 | 6.18 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.69 | -9.31 | 69 | 15.9 | -7.97 | -0.77 | -26.49 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.39 | -9.61 | 118 | 33.1 | -25.63 | -4.94 | -27.68 | 502 |
| 51 | CCI reversion · 1h | reversion | 89.95 | -10.05 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.41 | -10.59 | 285 | 21.8 | -32.54 | -4.82 | -39.19 | 1279 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.74 | -11.26 | 149 | 18.8 | -12.38 | -1.40 | -28.57 | 324 |
| 55 | Donchian 20/10 · 1h | breakout | 88.65 | -11.35 | 60 | 18.3 | -0.78 | 0.11 | -18.19 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.63 | -11.37 | 138 | 25.4 | -29.76 | -4.94 | -36.60 | 700 |
| 57 | MACD zero-line · 1h | trend | 88.14 | -11.86 | 66 | 18.2 | -7.06 | -0.77 | -20.89 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.93 | -12.06 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.85 | -12.15 | 104 | 13.5 | -8.64 | -0.96 | -21.96 | 339 |
| 60 | Keltner breakout · 1h | breakout | 87.07 | -12.93 | 43 | 18.6 | -12.30 | -1.43 | -26.07 | 220 |
| 61 | Three white soldiers | momentum | 86.80 | -13.20 | 147 | 17.0 | -48.16 | -23.03 | -48.24 | 591 |
| 62 | ROC + volume · 1h | momentum | 86.24 | -13.76 | 132 | 21.2 | -10.39 | -1.25 | -23.66 | 416 |
| 63 | ROC + volume | momentum | 73.99 | -26.01 | 401 | 22.9 | -73.06 | -16.60 | -74.16 | 1683 |
| 64 | RSI(14) reversion | reversion | 73.68 | -26.32 | 375 | 27.5 | -71.96 | -17.74 | -71.97 | 1482 |
| 65 | Squeeze breakout | breakout | 70.38 | -29.62 | 340 | 15.3 | -62.27 | -18.07 | -62.27 | 1235 |
| 66 | Volume breakout | breakout | 69.88 | -30.12 | 271 | 14.0 | -62.42 | -17.80 | -62.44 | 904 |
| 67 | EMA 20/50 cross | trend | 68.46 | -31.54 | 348 | 19.8 | -76.74 | -15.23 | -76.76 | 1453 |
| 68 | Donchian 55/20 | breakout | 68.19 | -31.81 | 350 | 18.0 | -68.04 | -14.50 | -68.35 | 1299 |
| 69 | VWAP reversion | reversion | 67.72 | -32.27 | 405 | 25.9 | -71.23 | -15.81 | -71.29 | 1429 |
| 70 | Supertrend | trend | 61.79 | -38.21 | 484 | 19.6 | -86.08 | -21.06 | -86.13 | 1915 |
| 71 | Keltner breakout | breakout | 61.17 | -38.83 | 470 | 14.5 | -83.84 | -27.81 | -83.84 | 1856 |
| 72 | AI bee: Boozy | ai | 59.96 | -40.04 | 261 | 5.0 | — | — | — | — |
| 73 | Z-score reversion | reversion | 58.52 | -41.48 | 518 | 22.0 | -85.13 | -22.83 | -85.16 | 2077 |
| 74 | Ichimoku | trend | 58.46 | -41.55 | 425 | 10.1 | -82.00 | -23.21 | -82.00 | 1756 |
| 75 | MFI reversion | reversion | 57.69 | -42.31 | 528 | 20.6 | -87.56 | -28.08 | -87.59 | 2123 |
| 76 | AI bee: Bizzy | ai | 55.98 | -44.02 | 870 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.70 | -45.30 | 564 | 10.1 | -89.44 | -35.30 | -89.44 | 2128 |
| 78 | Donchian 20/10 | breakout | 53.45 | -46.55 | 658 | 17.9 | -90.91 | -26.20 | -90.91 | 2671 |
| 79 | MACD zero-line | trend | 52.03 | -47.97 | 611 | 14.6 | -91.49 | -29.77 | -91.50 | 2366 |
| 80 | RSI momentum | momentum | 51.66 | -48.34 | 636 | 16.7 | -90.55 | -25.89 | -90.55 | 2394 |
| 81 | Trend pullback | trend | 51.55 | -48.45 | 625 | 14.4 | -91.37 | -27.25 | -91.37 | 2358 |
| 82 | Triple EMA stack | trend | 50.68 | -49.32 | 660 | 15.2 | -93.34 | -30.46 | -93.34 | 2631 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -31.22 | -98.66 | 5394 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -33.44 | -97.37 | 3552 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -36.33 | -96.51 | 3628 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.27 | -25.54 | -94.27 | 2699 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.49 | -99.34 | 5683 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.54 | -31.99 | -96.54 | 3651 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.81 | -99.73 | 6206 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -38.09 | -97.35 | 3692 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -36.77 | -98.45 | 4708 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.53 | -33.16 | -93.53 | 2822 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.10 | -99.52 | 6152 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.77 | -33.13 | -95.78 | 3738 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.65 | -34.28 | -95.65 | 4091 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.06 | -99.89 | 8305 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T10:12 | AI bee: Bizzy | sell | ETH-USD | 7.91 | -0.06 | Jev: sell (sell p=0.82) after 10 min |
| 2026-10-12T10:02 | AI bee: Bizzy | buy | ETH-USD | 7.98 | — | Jev: buy (buy p=0.57) |
| 2026-10-12T10:00 | MACD cross · 1h | sell | SOL-USD | 5.10 | 0.06 | exit signal |
| 2026-10-12T10:00 | MFI reversion | buy | XRP-USD | 14.46 | — | entry signal |
| 2026-10-12T10:00 | MFI reversion | buy | DOGE-USD | 14.47 | — | entry signal |
| 2026-10-12T09:55 | MFI reversion | buy | BTC-USD | 14.47 | — | entry signal |
| 2026-10-12T09:55 | Z-score reversion | buy | XRP-USD | 14.65 | — | entry signal |
| 2026-10-12T09:55 | RSI(14) reversion | buy | SOL-USD | 18.43 | — | entry signal |
| 2026-10-12T09:50 | MFI reversion | sell | DOGE-USD | 14.36 | -0.13 | stop-loss |
| 2026-10-12T09:50 | VWAP reversion | buy | BTC-USD | 16.94 | — | entry signal |
| 2026-10-12T09:50 | Z-score reversion | buy | SOL-USD | 14.64 | — | entry signal |
| 2026-10-12T09:50 | RSI(14) reversion | buy | BTC-USD | 18.44 | — | entry signal |
| 2026-10-12T09:45 | Z-score reversion | sell | SOL-USD | 14.57 | -0.15 | stop-loss |
| 2026-10-12T09:40 | Z-score reversion | buy | DOGE-USD | 14.69 | — | entry signal |
| 2026-10-12T09:40 | Z-score reversion | sell | BTC-USD | 14.61 | -0.12 | stop-loss |
| 2026-10-12T09:25 | MFI reversion | buy | DOGE-USD | 14.49 | — | entry signal |
| 2026-10-12T09:15 | MFI reversion | buy | ETH-USD | 14.51 | — | entry signal |
| 2026-10-12T09:00 | Volume breakout · 1h | sell | ETH-USD | 23.17 | 0.03 | exit signal |
| 2026-10-12T09:00 | VWAP momentum · 1h | sell | SOL-USD | 6.84 | -0.03 | exit signal |
| 2026-10-12T09:00 | Ichimoku · 1h | sell | XRP-USD | 22.75 | -0.35 | exit signal |
| 2026-10-12T09:00 | MACD cross · 1h | sell | XRP-USD | 4.50 | -0.07 | exit signal |
| 2026-10-12T09:00 | MACD cross · 1h | sell | BTC-USD | 4.51 | -0.06 | stop-loss |
| 2026-10-12T09:00 | MFI reversion | sell | BTC-USD | 14.41 | -0.13 | stop-loss |
| 2026-10-12T08:55 | EMA 20/50 cross | sell | ETH-USD | 13.88 | -0.01 | exit signal |
| 2026-10-12T08:50 | Z-score reversion | buy | SOL-USD | 14.72 | — | entry signal |
| 2026-10-12T08:50 | ADX DI cross | sell | ETH-USD | 13.58 | -0.12 | exit signal |
| 2026-10-12T08:40 | Trend pullback | sell | ETH-USD | 12.84 | -0.10 | exit signal |
| 2026-10-12T08:40 | Trend pullback | sell | DOGE-USD | 12.83 | -0.11 | exit signal |
| 2026-10-12T08:35 | MFI reversion | buy | BTC-USD | 14.54 | — | entry signal |
| 2026-10-12T08:35 | Trend pullback | buy | ETH-USD | 12.94 | — | entry signal |
| 2026-10-12T08:35 | Trend pullback | buy | DOGE-USD | 12.94 | — | entry signal |
| 2026-10-12T08:35 | ADX DI cross | buy | ETH-USD | 13.70 | — | entry signal |
| 2026-10-12T08:30 | Z-score reversion | buy | BTC-USD | 14.73 | — | entry signal |
| 2026-10-12T08:30 | EMA 20/50 cross | sell | SOL-USD | 17.31 | 0.00 | exit signal |
| 2026-10-12T08:20 | MFI reversion | sell | XRP-USD | 14.42 | -0.16 | stop-loss |
| 2026-10-12T08:20 | RSI momentum | sell | DOGE-USD | 10.31 | -0.14 | target is flat |
| 2026-10-12T08:20 | ADX DI cross | sell | ETH-USD | 10.97 | -0.09 | exit signal |
| 2026-10-12T08:20 | ADX DI cross | sell | DOGE-USD | 10.96 | -0.11 | target is flat |
| 2026-10-12T08:20 | Supertrend | sell | XRP-USD | 15.46 | -0.21 | exit signal |
| 2026-10-12T08:20 | Supertrend | sell | SOL-USD | 15.41 | -0.25 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 10:25:05.000120+00:00 -> 2026-10-12 10:35:05.000120+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
