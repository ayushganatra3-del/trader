# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T13:25:05.000162+00:00 · 20255 ticks

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

Today: 9957 decisions in 1992 calls, $0.1395 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T13:25 | 1 / 4 / 0 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T13:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T13:25 | 2 / 3 / 0 | COIN 76% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.53 | -2.28 | -13.79 | 116 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.61 | 2.61 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.28 | 2.28 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.09 | 2.09 | 14 | 57.1 | -12.40 | -2.03 | -20.64 | 68 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.41 | 1.41 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.32 | 1.32 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.17 | 1.17 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.83 | -0.17 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.77 | -0.23 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.76 | 2.24 | -1.52 | 84 |
| 17 | Stochastic reversion · 1h | reversion | 99.19 | -0.81 | 89 | 55.1 | -9.72 | -1.86 | -14.61 | 336 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.76 | -1.24 | 29 | 13.8 | 12.09 | 1.52 | -16.96 | 114 |
| 20 | Hold BTC | benchmark | 98.67 | -1.33 | 0 | — | 28.57 | 3.37 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.66 | -1.33 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.63 | -1.37 | 0 | — | 11.52 | 1.86 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.87 | -2.13 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.33 | -2.67 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.21 | -2.79 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.11 | -2.89 | 78 | 23.1 | -23.23 | -6.54 | -25.39 | 166 |
| 27 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.87 | -2.29 | -10.19 | 268 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 29 | ADX DI cross · 1h | trend | 96.38 | -3.62 | 58 | 20.7 | -0.25 | 0.12 | -13.84 | 252 |
| 30 | EMA 20/50 cross · 1h | trend | 96.34 | -3.66 | 42 | 11.9 | 5.68 | 0.84 | -19.85 | 136 |
| 31 | Parabolic SAR · 1h | trend | 96.33 | -3.67 | 82 | 22.0 | -2.27 | -0.13 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.70 | -4.30 | 120 | 24.2 | -14.79 | -2.35 | -17.27 | 469 |
| 34 | Supertrend · 1h | trend | 94.97 | -5.03 | 55 | 12.7 | 1.72 | 0.41 | -18.22 | 207 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.55 | -6.45 | 119 | 34.5 | -10.24 | -1.62 | -17.79 | 124 |
| 38 | Squeeze breakout · 1h | breakout | 93.43 | -6.57 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.15 | -6.85 | 26 | 26.9 | -4.76 | -0.93 | -9.03 | 153 |
| 40 | Connors RSI(2) · 1h | reversion | 93.03 | -6.97 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.88 | -7.12 | 392 | 18.4 | 0.81 | 0.29 | -12.99 | 420 |
| 42 | Bollinger reversion · 1h | reversion | 92.79 | -7.21 | 78 | 37.2 | -20.61 | -4.88 | -23.11 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.72 | -7.28 | 64 | 15.6 | 4.13 | 0.70 | -17.56 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.13 | -7.87 | 59 | 20.3 | 7.61 | 1.19 | -12.60 | 122 |
| 45 | Williams %R · 1h | reversion | 91.57 | -8.43 | 126 | 47.6 | -23.54 | -4.01 | -26.91 | 507 |
| 46 | Bollinger breakout · 1h | breakout | 91.26 | -8.74 | 72 | 27.8 | 6.15 | 0.95 | -13.62 | 287 |
| 47 | Ichimoku · 1h | trend | 91.17 | -8.83 | 47 | 17.0 | -1.60 | 0.01 | -21.65 | 124 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.74 | -9.26 | 69 | 15.9 | -8.64 | -0.85 | -26.79 | 239 |
| 50 | Candlestick reversal · 1h | reversion | 90.43 | -9.57 | 118 | 33.1 | -26.27 | -5.06 | -28.30 | 507 |
| 51 | CCI reversion · 1h | reversion | 89.98 | -10.02 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.46 | -10.54 | 285 | 21.8 | -32.43 | -4.81 | -39.18 | 1278 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.79 | -11.21 | 149 | 18.8 | -12.33 | -1.39 | -28.53 | 323 |
| 55 | Heikin-Ashi · 1h | trend | 88.68 | -11.32 | 138 | 25.4 | -29.61 | -4.92 | -36.59 | 699 |
| 56 | Donchian 20/10 · 1h | breakout | 88.57 | -11.43 | 62 | 17.7 | -1.25 | 0.05 | -18.45 | 228 |
| 57 | MACD zero-line · 1h | trend | 88.20 | -11.80 | 67 | 17.9 | -7.04 | -0.76 | -20.89 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.98 | -12.02 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.71 | -12.29 | 105 | 13.3 | -8.71 | -0.97 | -22.12 | 338 |
| 60 | Keltner breakout · 1h | breakout | 87.12 | -12.88 | 43 | 18.6 | -12.47 | -1.45 | -26.16 | 220 |
| 61 | Three white soldiers | momentum | 86.62 | -13.38 | 148 | 16.9 | -48.64 | -23.35 | -48.72 | 593 |
| 62 | ROC + volume · 1h | momentum | 86.29 | -13.71 | 132 | 21.2 | -10.48 | -1.26 | -23.88 | 416 |
| 63 | ROC + volume | momentum | 73.80 | -26.20 | 402 | 22.9 | -73.13 | -16.64 | -74.25 | 1685 |
| 64 | RSI(14) reversion | reversion | 72.55 | -27.45 | 380 | 27.1 | -72.46 | -18.10 | -72.47 | 1489 |
| 65 | Squeeze breakout | breakout | 70.38 | -29.62 | 340 | 15.3 | -62.08 | -17.92 | -62.12 | 1233 |
| 66 | Volume breakout | breakout | 69.71 | -30.29 | 272 | 14.0 | -62.35 | -17.80 | -62.37 | 903 |
| 67 | EMA 20/50 cross | trend | 68.46 | -31.54 | 348 | 19.8 | -76.69 | -15.21 | -76.71 | 1451 |
| 68 | Donchian 55/20 | breakout | 68.19 | -31.81 | 350 | 18.0 | -68.14 | -14.54 | -68.35 | 1299 |
| 69 | VWAP reversion | reversion | 66.83 | -33.17 | 409 | 25.7 | -71.39 | -15.93 | -71.40 | 1428 |
| 70 | Supertrend | trend | 61.54 | -38.46 | 486 | 19.5 | -86.08 | -21.05 | -86.12 | 1915 |
| 71 | Keltner breakout | breakout | 61.17 | -38.83 | 470 | 14.5 | -83.72 | -27.74 | -83.73 | 1852 |
| 72 | AI bee: Boozy | ai | 59.96 | -40.04 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 58.46 | -41.55 | 425 | 10.1 | -81.99 | -23.19 | -81.99 | 1757 |
| 74 | Z-score reversion | reversion | 57.37 | -42.63 | 526 | 21.7 | -85.32 | -23.04 | -85.35 | 2076 |
| 75 | MFI reversion | reversion | 56.75 | -43.25 | 536 | 20.3 | -87.71 | -28.30 | -87.75 | 2124 |
| 76 | AI bee: Bizzy | ai | 55.94 | -44.05 | 871 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.58 | -45.42 | 565 | 10.1 | -89.31 | -35.22 | -89.31 | 2122 |
| 78 | Donchian 20/10 | breakout | 53.32 | -46.68 | 659 | 17.9 | -90.85 | -26.10 | -90.86 | 2667 |
| 79 | MACD zero-line | trend | 51.91 | -48.09 | 612 | 14.5 | -91.47 | -29.70 | -91.48 | 2365 |
| 80 | Trend pullback | trend | 51.55 | -48.45 | 625 | 14.4 | -91.29 | -27.09 | -91.29 | 2352 |
| 81 | RSI momentum | momentum | 51.53 | -48.47 | 637 | 16.6 | -90.54 | -25.84 | -90.54 | 2393 |
| 82 | Triple EMA stack | trend | 50.68 | -49.32 | 660 | 15.2 | -93.33 | -30.43 | -93.33 | 2630 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -31.11 | -98.65 | 5389 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -33.44 | -97.38 | 3553 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -36.22 | -96.49 | 3629 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.34 | -25.67 | -94.34 | 2703 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.90 | -99.36 | 5702 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.50 | -31.89 | -96.50 | 3642 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.84 | -99.73 | 6202 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -38.12 | -97.35 | 3692 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.82 | -98.47 | 4710 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.51 | -33.13 | -93.51 | 2819 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.28 | -99.53 | 6156 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.82 | -33.31 | -95.83 | 3742 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -34.44 | -95.69 | 4094 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.97 | -99.89 | 8299 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T13:25 | VWAP reversion | buy | XRP-USD | 13.28 | — | entry signal |
| 2026-10-12T13:25 | VWAP reversion | buy | BTC-USD | 13.38 | — | entry signal |
| 2026-10-12T13:25 | VWAP reversion | sell | ETH-USD | 3.36 | -0.03 | rebalance down |
| 2026-10-12T13:25 | Z-score reversion | buy | DOGE-USD | 14.35 | — | entry signal |
| 2026-10-12T13:25 | RSI(14) reversion | buy | XRP-USD | 18.15 | — | entry signal |
| 2026-10-12T13:20 | MFI reversion | sell | XRP-USD | 14.10 | -0.16 | stop-loss |
| 2026-10-12T13:20 | VWAP reversion | sell | XRP-USD | 16.66 | -0.19 | stop-loss |
| 2026-10-12T13:20 | RSI(14) reversion | sell | XRP-USD | 14.46 | -0.18 | stop-loss |
| 2026-10-12T13:15 | EMA 20/50 cross · 1h | sell | BTC-USD | 11.97 | -0.14 | stop-loss |
| 2026-10-12T13:15 | VWAP reversion | buy | XRP-USD | 3.37 | — | rebalance up |
| 2026-10-12T13:15 | VWAP reversion | buy | ETH-USD | 3.36 | — | rebalance up |
| 2026-10-12T13:15 | VWAP reversion | sell | BTC-USD | 13.36 | -0.13 | stop-loss |
| 2026-10-12T13:15 | Z-score reversion | sell | DOGE-USD | 14.29 | -0.11 | target is flat |
| 2026-10-12T13:15 | RSI(14) reversion | sell | BTC-USD | 14.43 | -0.14 | stop-loss |
| 2026-10-12T13:10 | MFI reversion | buy | DOGE-USD | 14.23 | — | entry signal |
| 2026-10-12T13:10 | Z-score reversion | buy | DOGE-USD | 14.39 | — | entry signal |
| 2026-10-12T13:00 | Donchian 20/10 · 1h | sell | ETH-USD | 6.19 | -0.03 | exit signal |
| 2026-10-12T13:00 | Ichimoku · 1h | sell | ETH-USD | 18.43 | -0.13 | exit signal |
| 2026-10-12T13:00 | Supertrend · 1h | sell | XRP-USD | 3.02 | -0.09 | exit signal |
| 2026-10-12T13:00 | Supertrend · 1h | sell | BTC-USD | 10.45 | -0.07 | exit signal |
| 2026-10-12T13:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.28 | — | rebalance up |
| 2026-10-12T13:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 8.77 | -0.06 | exit signal |
| 2026-10-12T12:55 | RSI(14) reversion | buy | BTC-USD | 3.63 | — | rebalance up |
| 2026-10-12T12:55 | RSI(14) reversion | sell | XRP-USD | 3.63 | -0.03 | rebalance down |
| 2026-10-12T12:50 | MFI reversion | buy | XRP-USD | 14.26 | — | entry signal |
| 2026-10-12T12:50 | MFI reversion | buy | SOL-USD | 14.26 | — | entry signal |
| 2026-10-12T12:50 | Z-score reversion | buy | SOL-USD | 14.43 | — | entry signal |
| 2026-10-12T12:50 | Z-score reversion | buy | ETH-USD | 14.43 | — | entry signal |
| 2026-10-12T12:50 | RSI(14) reversion | buy | BTC-USD | 10.94 | — | entry signal |
| 2026-10-12T12:50 | RSI(14) reversion | sell | SOL-USD | 3.64 | -0.02 | rebalance down |
| 2026-10-12T12:50 | RSI(14) reversion | sell | ETH-USD | 3.65 | -0.02 | rebalance down |
| 2026-10-12T12:50 | RSI(14) reversion | sell | DOGE-USD | 3.65 | -0.02 | rebalance down |
| 2026-10-12T12:45 | VWAP reversion | buy | XRP-USD | 13.49 | — | entry signal |
| 2026-10-12T12:45 | VWAP reversion | buy | SOL-USD | 13.49 | — | entry signal |
| 2026-10-12T12:45 | VWAP reversion | buy | ETH-USD | 13.49 | — | entry signal |
| 2026-10-12T12:45 | VWAP reversion | buy | DOGE-USD | 13.49 | — | entry signal |
| 2026-10-12T12:45 | VWAP reversion | buy | BTC-USD | 13.49 | — | entry signal |
| 2026-10-12T12:45 | RSI(14) reversion | buy | XRP-USD | 18.30 | — | entry signal |
| 2026-10-12T12:45 | RSI(14) reversion | buy | SOL-USD | 18.30 | — | entry signal |
| 2026-10-12T12:45 | RSI(14) reversion | buy | ETH-USD | 18.30 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 13:25:05.000162+00:00 -> 2026-10-12 13:35:05.000162+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
