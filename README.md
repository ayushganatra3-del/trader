# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T22:54:05.000145+00:00 · 20675 ticks

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

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.55 · VIX 15.24 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 34752 decisions in 3252 calls, $0.4355 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T22:54 | 0 / 2 / 3 | SOL-USD 14%, PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-12T22:54 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T22:54 | 0 / 4 / 1 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.92 | 2.92 | 0 | — | 1.61 | 0.84 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.06 | 2.06 | 16 | 50.0 | -12.87 | -2.14 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 4 | Hold SPY | benchmark | 101.43 | 1.43 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.11 | -3.27 | 17 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -9.45 | -2.83 | -13.79 | 118 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.22 | 1.22 | 0 | — | 1.71 | 0.84 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.66 | 0.66 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.63 | 0.63 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.31 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.44 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.13 | 0.13 | 0 | — | 3.58 | 1.41 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.37 | -0.63 | 0 | — | -4.89 | -2.27 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.66 | -1.80 | 78 |
| 17 | Hold BTC | benchmark | 98.82 | -1.18 | 0 | — | 29.37 | 3.48 | -8.68 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.80 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.25 | -1.75 | 31 | 12.9 | 12.04 | 1.46 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.14 | -1.86 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 98.01 | -1.99 | 11 | 36.4 | -16.71 | -0.63 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.88 | -2.12 | 78 | 23.1 | -23.01 | -6.47 | -25.60 | 168 |
| 23 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.63 | -4.53 | 27 |
| 24 | Stochastic reversion · 1h | reversion | 97.11 | -2.89 | 96 | 53.1 | -12.46 | -2.43 | -14.02 | 342 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 97.03 | -2.97 | 0 | — | 9.02 | 1.51 | -8.33 | 1 |
| 26 | Z-score reversion · 1h | reversion | 96.86 | -3.14 | 44 | 43.2 | 3.43 | 0.81 | -8.60 | 160 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.48 | -3.52 | 62 | 19.4 | -6.63 | -1.08 | -13.79 | 256 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.52 | -2.72 | -8.88 | 305 |
| 30 | MACD cross · 1h | trend | 95.85 | -4.15 | 125 | 24.0 | -11.27 | -1.77 | -17.79 | 460 |
| 31 | Parabolic SAR · 1h | trend | 95.36 | -4.64 | 86 | 22.1 | 2.01 | 0.45 | -21.52 | 289 |
| 32 | EMA 20/50 cross · 1h | trend | 95.35 | -4.65 | 45 | 15.6 | 4.66 | 0.73 | -23.71 | 137 |
| 33 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.95 | -3.86 | -8.72 | 232 |
| 34 | Supertrend · 1h | trend | 94.57 | -5.43 | 58 | 13.8 | 1.33 | 0.36 | -18.92 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.67 | 2.22 | -6.20 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.51 | -6.49 | 39 | 23.1 | 15.62 | 2.48 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.47 | -6.53 | 151 | 32.5 | -7.81 | -1.19 | -16.91 | 129 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.24 | -2.76 | -6.45 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.62 | -7.38 | 66 | 15.2 | -0.62 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.53 | -7.47 | 115 | 43.5 | -18.87 | -6.28 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.51 | -7.49 | 439 | 17.8 | 2.49 | 0.58 | -12.39 | 397 |
| 42 | RSI(14) reversion · 1h | reversion | 91.81 | -8.19 | 32 | 28.1 | 1.29 | 0.41 | -9.03 | 130 |
| 43 | Volume breakout · 1h | breakout | 91.73 | -8.27 | 70 | 20.0 | 9.17 | 1.40 | -12.60 | 118 |
| 44 | Bollinger reversion · 1h | reversion | 91.13 | -8.87 | 83 | 37.3 | -23.35 | -5.78 | -24.16 | 315 |
| 45 | Ichimoku · 1h | trend | 91.02 | -8.98 | 48 | 16.7 | 0.43 | 0.26 | -22.34 | 128 |
| 46 | Bollinger breakout · 1h | breakout | 90.87 | -9.13 | 74 | 28.4 | 8.34 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.72 | -9.28 | 71 | 15.5 | -7.15 | -0.62 | -27.17 | 237 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.74 | -16.08 | 569 |
| 49 | CCI reversion · 1h | reversion | 89.05 | -10.95 | 112 | 45.5 | -10.61 | -1.43 | -14.35 | 409 |
| 50 | Williams %R · 1h | reversion | 88.80 | -11.20 | 134 | 45.5 | -26.54 | -4.42 | -28.42 | 507 |
| 51 | OBV trend · 1h | momentum | 88.72 | -11.28 | 150 | 18.7 | -12.77 | -1.22 | -34.14 | 318 |
| 52 | VWAP momentum · 1h | momentum | 88.25 | -11.75 | 311 | 23.2 | -33.35 | -4.99 | -40.46 | 1255 |
| 53 | Max aggression: 5-day momentum | meta | 88.10 | -11.90 | 7 | 28.6 | -14.35 | -1.05 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 88.06 | -11.95 | 129 | 31.0 | -29.12 | -5.61 | -29.17 | 499 |
| 55 | Donchian 20/10 · 1h | breakout | 87.72 | -12.28 | 63 | 17.5 | -0.59 | 0.13 | -19.51 | 214 |
| 56 | Heikin-Ashi · 1h | trend | 87.72 | -12.28 | 153 | 28.1 | -30.61 | -5.11 | -37.65 | 678 |
| 57 | MACD zero-line · 1h | trend | 87.60 | -12.40 | 67 | 17.9 | -20.79 | -3.88 | -21.53 | 231 |
| 58 | EMA 9/21 cross · 1h | trend | 87.12 | -12.88 | 108 | 13.0 | -8.22 | -0.86 | -23.06 | 332 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.07 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.66 | -13.34 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.46 | -13.54 | 153 | 17.0 | -48.29 | -23.54 | -48.29 | 587 |
| 62 | ROC + volume · 1h | momentum | 85.53 | -14.47 | 164 | 20.1 | -9.06 | -1.05 | -25.01 | 401 |
| 63 | ROC + volume | momentum | 72.29 | -27.71 | 421 | 22.3 | -72.95 | -16.62 | -74.60 | 1661 |
| 64 | RSI(14) reversion | reversion | 70.06 | -29.94 | 418 | 26.6 | -72.90 | -17.87 | -72.90 | 1473 |
| 65 | Squeeze breakout | breakout | 69.52 | -30.48 | 354 | 15.5 | -62.38 | -18.23 | -62.38 | 1224 |
| 66 | Volume breakout | breakout | 69.45 | -30.55 | 279 | 14.7 | -61.75 | -17.62 | -61.75 | 893 |
| 67 | EMA 20/50 cross | trend | 67.43 | -32.57 | 357 | 19.9 | -76.49 | -15.22 | -76.49 | 1432 |
| 68 | Donchian 55/20 | breakout | 66.63 | -33.37 | 360 | 17.5 | -68.18 | -14.39 | -69.10 | 1290 |
| 69 | VWAP reversion | reversion | 64.21 | -35.79 | 460 | 25.4 | -71.96 | -15.81 | -71.96 | 1406 |
| 70 | AI bee: Boozy | ai | 60.33 | -39.66 | 261 | 5.0 | — | — | — | — |
| 71 | Keltner breakout | breakout | 60.30 | -39.70 | 485 | 14.6 | -83.30 | -27.44 | -83.30 | 1837 |
| 72 | Supertrend | trend | 60.00 | -40.00 | 503 | 19.3 | -86.05 | -21.03 | -86.05 | 1892 |
| 73 | Ichimoku | trend | 57.09 | -42.91 | 436 | 9.9 | -82.25 | -23.19 | -82.25 | 1734 |
| 74 | AI bee: Bizzy | ai | 55.38 | -44.62 | 890 | 8.3 | — | — | — | — |
| 75 | Z-score reversion ⏸ | reversion | 55.28 | -44.72 | 567 | 22.0 | -85.81 | -23.10 | -85.81 | 2071 |
| 76 | MFI reversion | reversion | 55.11 | -44.89 | 619 | 19.5 | -87.98 | -28.32 | -87.99 | 2121 |
| 77 | ADX DI cross | trend | 53.41 | -46.59 | 599 | 10.0 | -89.11 | -34.56 | -89.11 | 2101 |
| 78 | Donchian 20/10 | breakout | 51.89 | -48.11 | 684 | 17.5 | -90.91 | -26.09 | -90.91 | 2644 |
| 79 | MACD zero-line | trend | 50.91 | -49.09 | 635 | 14.5 | -91.47 | -30.07 | -91.47 | 2343 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -30.74 | -98.60 | 5318 |
| 81 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.67 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -30.22 | -93.21 | 2596 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.49 | -25.60 | -90.49 | 2359 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -33.33 | -97.37 | 3518 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -36.24 | -96.37 | 3577 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.28 | -25.70 | -94.28 | 2627 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.11 | -99.36 | 5639 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -31.51 | -96.30 | 3592 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.43 | -99.73 | 6146 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.30 | -38.34 | -97.30 | 3654 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -36.96 | -98.52 | 4666 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.39 | -33.01 | -93.39 | 2794 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.22 | -99.53 | 6107 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -33.39 | -95.94 | 3729 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -34.47 | -95.71 | 4048 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.88 | -99.89 | 8201 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T22:51 | AI bee: Bizzy | buy | SOL-USD | 7.62 | — | Jev: buy (buy p=0.55) |
| 2026-10-12T22:50 | VWAP reversion | buy | SOL-USD | 3.45 | — | rebalance up |
| 2026-10-12T22:50 | VWAP reversion | sell | ETH-USD | 12.80 | -0.11 | stop-loss |
| 2026-10-12T22:46 | VWAP reversion | buy | SOL-USD | 3.21 | — | rebalance up |
| 2026-10-12T22:46 | VWAP reversion | sell | ETH-USD | 3.21 | -0.02 | rebalance down |
| 2026-10-12T22:45 | VWAP reversion | buy | SOL-USD | 9.44 | — | entry signal |
| 2026-10-12T22:45 | VWAP reversion | sell | DOGE-USD | 3.21 | -0.03 | rebalance down |
| 2026-10-12T22:45 | RSI(14) reversion | buy | SOL-USD | 17.45 | — | entry signal |
| 2026-10-12T22:45 | RSI(14) reversion | buy | ETH-USD | 17.55 | — | entry signal |
| 2026-10-12T22:40 | VWAP reversion | buy | ETH-USD | 6.56 | — | rebalance up |
| 2026-10-12T22:40 | VWAP reversion | sell | SOL-USD | 12.80 | -0.21 | stop-loss |
| 2026-10-12T22:40 | RSI(14) reversion | sell | SOL-USD | 17.47 | -0.22 | stop-loss |
| 2026-10-12T22:36 | Z-score reversion | sell | XRP-USD | 13.86 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-12T22:36 | Z-score reversion | sell | SOL-USD | 13.81 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-12T22:36 | Z-score reversion | sell | DOGE-USD | 13.79 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-12T22:35 | Z-score reversion | sell | ETH-USD | 13.80 | -0.14 | stop-loss |
| 2026-10-12T22:35 | RSI(14) reversion | sell | ETH-USD | 17.49 | -0.18 | stop-loss |
| 2026-10-12T22:30 | VWAP reversion | buy | ETH-USD | 3.22 | — | rebalance up |
| 2026-10-12T22:30 | VWAP reversion | sell | XRP-USD | 3.22 | -0.02 | rebalance down |
| 2026-10-12T22:25 | Williams %R · 1h | buy | SOL-USD | 9.50 | — | rebalance up |
| 2026-10-12T22:25 | Williams %R · 1h | sell | ETH-USD | 17.71 | -0.29 | stop-loss |
| 2026-10-12T22:19 | AI bee: Bizzy | sell | XRP-USD | 7.72 | -0.07 | Jev: sell (sell p=0.93) after 11 min |
| 2026-10-12T22:15 | MFI reversion | buy | SOL-USD | 13.82 | — | entry signal |
| 2026-10-12T22:10 | Z-score reversion | buy | ETH-USD | 13.94 | — | entry signal |
| 2026-10-12T22:10 | Z-score reversion | buy | DOGE-USD | 13.94 | — | entry signal |
| 2026-10-12T22:10 | RSI(14) reversion | buy | ETH-USD | 17.67 | — | entry signal |
| 2026-10-12T22:08 | AI bee: Bizzy | buy | XRP-USD | 7.79 | — | Jev: buy (buy p=0.56) |
| 2026-10-12T22:05 | VWAP reversion | buy | ETH-USD | 6.36 | — | entry signal |
| 2026-10-12T22:05 | VWAP reversion | sell | SOL-USD | 3.29 | -0.03 | rebalance down |
| 2026-10-12T22:05 | RSI(14) reversion | buy | DOGE-USD | 17.66 | — | entry signal |
| 2026-10-12T22:00 | Candlestick reversal · 1h | sell | BTC-USD | 9.93 | -0.07 | exit signal |
| 2026-10-12T21:56 | MFI reversion | buy | XRP-USD | 13.84 | — | entry signal |
| 2026-10-12T21:56 | MFI reversion | buy | ETH-USD | 13.84 | — | entry signal |
| 2026-10-12T21:56 | VWAP reversion | buy | XRP-USD | 16.17 | — | entry signal |
| 2026-10-12T21:56 | VWAP reversion | buy | DOGE-USD | 16.17 | — | entry signal |
| 2026-10-12T21:56 | Z-score reversion | buy | XRP-USD | 13.95 | — | entry signal |
| 2026-10-12T21:56 | Z-score reversion | buy | SOL-USD | 13.95 | — | entry signal |
| 2026-10-12T21:56 | RSI(14) reversion | buy | XRP-USD | 17.69 | — | entry signal |
| 2026-10-12T21:56 | RSI(14) reversion | buy | SOL-USD | 17.69 | — | entry signal |
| 2026-10-12T21:50 | Agent (rotation) | sell | SOL-USD | 7.83 | -0.18 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 22:54:05.000145+00:00 -> 2026-10-12 23:04:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
