# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T09:25:05.000113+00:00 · 20062 ticks

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

Today: 7062 decisions in 1413 calls, $0.0989 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T09:25 | 0 / 4 / 1 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T09:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T09:25 | 0 / 5 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| MFI reversion | AAPL | 2.06 | +0.67% | 4 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.25 | 3.25 | 37 | 43.2 | -7.53 | -2.28 | -13.79 | 116 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.49 | 2.49 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.17 | 2.17 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 101.98 | 1.98 | 14 | 57.1 | -12.40 | -2.03 | -20.64 | 68 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.29 | 1.29 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.21 | 1.21 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.05 | 1.05 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.72 | -0.28 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.66 | -0.34 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 15 | Hold BTC | benchmark | 99.65 | -0.35 | 0 | — | 29.44 | 3.47 | -8.68 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Donchian 55/20 · 1h | breakout | 99.12 | -0.88 | 28 | 14.3 | 12.86 | 1.60 | -16.96 | 114 |
| 19 | Stochastic reversion · 1h | reversion | 99.09 | -0.91 | 89 | 55.1 | -9.72 | -1.86 | -14.61 | 336 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.56 | -1.45 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.52 | -1.48 | 0 | — | 11.52 | 1.86 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.76 | -2.24 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.30 | -2.70 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.15 | -2.85 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.01 | -2.99 | 78 | 23.1 | -23.23 | -6.54 | -25.39 | 166 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.87 | -2.29 | -10.19 | 268 |
| 29 | EMA 20/50 cross · 1h | trend | 96.58 | -3.42 | 40 | 12.5 | 6.25 | 0.90 | -19.85 | 136 |
| 30 | ADX DI cross · 1h | trend | 96.27 | -3.73 | 58 | 20.7 | -0.25 | 0.12 | -13.84 | 252 |
| 31 | Parabolic SAR · 1h | trend | 96.23 | -3.77 | 82 | 22.0 | -2.14 | -0.11 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.65 | -4.35 | 117 | 23.1 | -14.80 | -2.35 | -17.27 | 469 |
| 34 | Supertrend · 1h | trend | 95.37 | -4.63 | 53 | 13.2 | 2.22 | 0.47 | -18.22 | 207 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.45 | -6.55 | 119 | 34.5 | -10.24 | -1.62 | -17.79 | 124 |
| 38 | Squeeze breakout · 1h | breakout | 93.40 | -6.60 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.05 | -6.95 | 26 | 26.9 | -1.96 | -0.32 | -9.03 | 146 |
| 40 | Connors RSI(2) · 1h | reversion | 93.00 | -7.00 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.78 | -7.22 | 392 | 18.4 | 1.05 | 0.33 | -12.89 | 412 |
| 42 | Bollinger reversion · 1h | reversion | 92.71 | -7.29 | 78 | 37.2 | -20.86 | -4.95 | -23.26 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.62 | -7.38 | 64 | 15.6 | 4.76 | 0.77 | -17.15 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.08 | -7.92 | 59 | 20.3 | 7.61 | 1.19 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 91.73 | -8.27 | 45 | 17.8 | -1.28 | 0.04 | -21.18 | 125 |
| 46 | Williams %R · 1h | reversion | 91.50 | -8.50 | 126 | 47.6 | -23.74 | -4.04 | -26.91 | 509 |
| 47 | Bollinger breakout · 1h | breakout | 91.18 | -8.82 | 72 | 27.8 | 6.18 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.64 | -9.36 | 69 | 15.9 | -8.09 | -0.78 | -26.49 | 239 |
| 50 | Candlestick reversal · 1h | reversion | 90.34 | -9.66 | 118 | 33.1 | -26.16 | -5.05 | -28.17 | 506 |
| 51 | CCI reversion · 1h | reversion | 89.91 | -10.09 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.36 | -10.64 | 285 | 21.8 | -32.53 | -4.82 | -39.18 | 1279 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.69 | -11.31 | 149 | 18.8 | -12.21 | -1.38 | -28.50 | 323 |
| 55 | Donchian 20/10 · 1h | breakout | 88.62 | -11.38 | 60 | 18.3 | -0.73 | 0.12 | -18.15 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.58 | -11.42 | 138 | 25.4 | -29.75 | -4.94 | -36.59 | 700 |
| 57 | MACD zero-line · 1h | trend | 88.16 | -11.84 | 66 | 18.2 | -7.00 | -0.76 | -20.89 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.89 | -12.11 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.79 | -12.21 | 104 | 13.5 | -8.78 | -0.98 | -21.96 | 340 |
| 60 | Keltner breakout · 1h | breakout | 87.02 | -12.98 | 43 | 18.6 | -12.22 | -1.42 | -25.96 | 220 |
| 61 | Three white soldiers | momentum | 86.80 | -13.20 | 147 | 17.0 | -48.25 | -23.15 | -48.27 | 593 |
| 62 | ROC + volume · 1h | momentum | 86.19 | -13.81 | 132 | 21.2 | -10.39 | -1.25 | -23.76 | 416 |
| 63 | ROC + volume | momentum | 73.99 | -26.01 | 401 | 22.9 | -73.07 | -16.60 | -74.16 | 1684 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 375 | 27.5 | -72.07 | -17.79 | -72.11 | 1484 |
| 65 | Squeeze breakout | breakout | 70.38 | -29.62 | 340 | 15.3 | -62.17 | -18.00 | -62.18 | 1234 |
| 66 | Volume breakout | breakout | 69.88 | -30.12 | 271 | 14.0 | -62.50 | -17.83 | -62.51 | 905 |
| 67 | EMA 20/50 cross | trend | 68.46 | -31.54 | 348 | 19.8 | -76.80 | -15.26 | -76.80 | 1455 |
| 68 | Donchian 55/20 | breakout | 68.19 | -31.81 | 350 | 18.0 | -68.10 | -14.52 | -68.35 | 1301 |
| 69 | VWAP reversion | reversion | 67.74 | -32.26 | 405 | 25.9 | -71.20 | -15.76 | -71.26 | 1427 |
| 70 | Supertrend | trend | 61.79 | -38.21 | 484 | 19.6 | -86.11 | -21.08 | -86.15 | 1916 |
| 71 | Keltner breakout | breakout | 61.17 | -38.83 | 470 | 14.5 | -83.90 | -27.82 | -83.90 | 1858 |
| 72 | AI bee: Boozy | ai | 59.96 | -40.04 | 261 | 5.0 | — | — | — | — |
| 73 | Z-score reversion | reversion | 58.77 | -41.23 | 516 | 22.1 | -85.09 | -22.77 | -85.10 | 2075 |
| 74 | Ichimoku | trend | 58.46 | -41.55 | 425 | 10.1 | -82.00 | -23.21 | -82.00 | 1756 |
| 75 | MFI reversion | reversion | 57.93 | -42.07 | 527 | 20.7 | -87.51 | -27.93 | -87.54 | 2119 |
| 76 | AI bee: Bizzy | ai | 56.04 | -43.96 | 869 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.70 | -45.30 | 564 | 10.1 | -89.38 | -35.29 | -89.38 | 2125 |
| 78 | Donchian 20/10 | breakout | 53.45 | -46.55 | 658 | 17.9 | -90.94 | -26.25 | -90.94 | 2673 |
| 79 | MACD zero-line | trend | 52.03 | -47.97 | 611 | 14.6 | -91.49 | -29.77 | -91.50 | 2366 |
| 80 | RSI momentum | momentum | 51.66 | -48.34 | 636 | 16.7 | -90.56 | -25.91 | -90.56 | 2395 |
| 81 | Trend pullback | trend | 51.55 | -48.45 | 625 | 14.4 | -91.41 | -27.31 | -91.41 | 2360 |
| 82 | Triple EMA stack | trend | 50.68 | -49.32 | 660 | 15.2 | -93.37 | -30.52 | -93.37 | 2634 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -31.25 | -98.66 | 5395 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -33.44 | -97.37 | 3552 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -36.23 | -96.49 | 3630 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -25.63 | -94.33 | 2703 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.51 | -99.34 | 5692 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.53 | -31.99 | -96.53 | 3650 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.70 | -99.73 | 6200 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -38.29 | -97.37 | 3696 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -36.61 | -98.44 | 4706 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.58 | -33.28 | -93.58 | 2826 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -39.90 | -99.51 | 6149 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.74 | -32.91 | -95.74 | 3736 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.63 | -34.14 | -95.63 | 4090 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.94 | -99.89 | 8304 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-12T08:20 | Supertrend | sell | DOGE-USD | 15.41 | -0.16 | exit signal |
| 2026-10-12T08:20 | Triple EMA stack | sell | DOGE-USD | 10.14 | -0.11 | exit signal |
| 2026-10-12T08:15 | Trend pullback | sell | DOGE-USD | 10.38 | -0.07 | exit signal |
| 2026-10-12T08:15 | Ichimoku | sell | DOGE-USD | 14.63 | -0.16 | exit signal |
| 2026-10-12T08:07 | AI bee: Bizzy | sell | DOGE-USD | 8.91 | -0.09 | Jev: sell (sell p=0.86) after 10 min |
| 2026-10-12T08:05 | Donchian 20/10 | sell | ETH-USD | 13.28 | -0.15 | stop-loss |
| 2026-10-12T08:05 | Donchian 20/10 | sell | DOGE-USD | 13.30 | -0.13 | exit signal |
| 2026-10-12T08:05 | RSI momentum | sell | XRP-USD | 10.32 | -0.13 | stop-loss |
| 2026-10-12T08:05 | RSI momentum | sell | SOL-USD | 7.76 | -0.10 | stop-loss |
| 2026-10-12T08:05 | RSI momentum | sell | ETH-USD | 10.34 | -0.11 | exit signal |
| 2026-10-12T08:05 | RSI momentum | sell | BTC-USD | 10.33 | -0.11 | stop-loss |
| 2026-10-12T08:05 | ROC + volume | sell | DOGE-USD | 18.37 | -0.17 | exit signal |
| 2026-10-12T08:05 | Trend pullback | sell | XRP-USD | 10.36 | -0.10 | exit signal |
| 2026-10-12T08:05 | Trend pullback | sell | SOL-USD | 12.92 | -0.12 | exit signal |
| 2026-10-12T08:05 | Trend pullback | sell | ETH-USD | 10.37 | -0.10 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 09:25:05.000113+00:00 -> 2026-10-12 09:35:05.000113+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
