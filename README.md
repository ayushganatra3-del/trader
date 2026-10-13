# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T05:25:05.000146+00:00 · 20978 ticks

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
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 3855 decisions in 771 calls, $0.0540 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T05:25 | 0 / 4 / 1 | ETH-USD 15%, PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T05:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T05:25 | 2 / 3 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Z-score reversion | AAPL | 1.77 | +1.13% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.83 | 2.83 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.12 | 2.12 | 16 | 50.0 | -15.07 | -2.39 | -21.97 | 73 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Hold SPY | benchmark | 101.34 | 1.34 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -8.80 | -2.61 | -13.79 | 117 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.14 | 1.14 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.57 | 0.57 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.54 | 0.54 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Hold BTC | benchmark | 100.16 | 0.16 | 0 | — | 31.20 | 3.60 | -8.68 | 1 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 100.04 | 0.04 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 14 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 15 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.28 | -0.72 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.18 | -1.82 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.06 | -1.94 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.93 | -2.07 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.80 | -2.20 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Three white soldiers · 1h | momentum | 97.30 | -2.70 | 8 | 0.0 | -3.25 | -2.49 | -4.64 | 29 |
| 24 | Stochastic reversion · 1h | reversion | 97.29 | -2.71 | 104 | 52.9 | -10.69 | -1.98 | -13.91 | 345 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.95 | -3.05 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 26 | Z-score reversion · 1h | reversion | 96.72 | -3.28 | 46 | 43.5 | 3.68 | 0.86 | -8.60 | 165 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.45 | -3.55 | 62 | 19.4 | -5.83 | -0.92 | -13.79 | 253 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -9.41 | -3.51 | -10.77 | 306 |
| 30 | MACD cross · 1h | trend | 95.83 | -4.17 | 125 | 24.0 | -10.63 | -1.65 | -17.79 | 463 |
| 31 | Parabolic SAR · 1h | trend | 95.30 | -4.70 | 86 | 22.1 | 2.00 | 0.44 | -21.52 | 289 |
| 32 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.86 | -3.80 | -8.72 | 230 |
| 33 | EMA 20/50 cross · 1h | trend | 95.26 | -4.74 | 45 | 15.6 | 4.72 | 0.73 | -23.71 | 137 |
| 34 | Supertrend · 1h | trend | 94.48 | -5.52 | 58 | 13.8 | 0.77 | 0.29 | -18.92 | 217 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.47 | -6.53 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.37 | -6.62 | 151 | 32.5 | -7.33 | -1.09 | -16.91 | 132 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.27 | -2.76 | -6.49 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.54 | -7.46 | 66 | 15.2 | -0.58 | 0.14 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.45 | -7.55 | 115 | 43.5 | -18.87 | -6.23 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.43 | -7.57 | 439 | 17.8 | 1.79 | 0.46 | -12.23 | 392 |
| 42 | RSI(14) reversion · 1h | reversion | 91.70 | -8.30 | 36 | 30.6 | 0.11 | 0.14 | -9.40 | 138 |
| 43 | Volume breakout · 1h | breakout | 91.67 | -8.33 | 70 | 20.0 | 9.16 | 1.39 | -12.60 | 116 |
| 44 | Ichimoku · 1h | trend | 90.95 | -9.05 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger reversion · 1h | reversion | 90.85 | -9.14 | 90 | 35.6 | -23.59 | -5.68 | -24.41 | 319 |
| 46 | Bollinger breakout · 1h | breakout | 90.81 | -9.19 | 74 | 28.4 | 8.33 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.64 | -9.36 | 71 | 15.5 | -6.76 | -0.57 | -27.17 | 235 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 89.04 | -10.96 | 140 | 45.7 | -25.28 | -4.10 | -28.82 | 509 |
| 50 | CCI reversion · 1h | reversion | 88.96 | -11.04 | 114 | 45.6 | -9.44 | -1.23 | -14.35 | 409 |
| 51 | OBV trend · 1h | momentum | 88.64 | -11.36 | 150 | 18.7 | -12.52 | -1.18 | -34.15 | 318 |
| 52 | VWAP momentum · 1h | momentum | 88.18 | -11.82 | 311 | 23.2 | -32.43 | -4.78 | -40.18 | 1254 |
| 53 | Candlestick reversal · 1h | reversion | 88.04 | -11.96 | 130 | 30.8 | -28.77 | -5.47 | -29.09 | 498 |
| 54 | Heikin-Ashi · 1h | trend | 88.03 | -11.97 | 153 | 28.1 | -29.76 | -4.89 | -37.81 | 680 |
| 55 | Max aggression: 5-day momentum | meta | 88.03 | -11.97 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 56 | Donchian 20/10 · 1h | breakout | 87.65 | -12.35 | 63 | 17.5 | -0.60 | 0.13 | -19.51 | 214 |
| 57 | MACD zero-line · 1h | trend | 87.55 | -12.45 | 67 | 17.9 | -20.63 | -3.81 | -21.53 | 230 |
| 58 | EMA 9/21 cross · 1h | trend | 87.05 | -12.95 | 108 | 13.0 | -8.46 | -0.89 | -23.06 | 333 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.29 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.58 | -13.42 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.47 | -13.53 | 154 | 17.5 | -48.10 | -22.98 | -48.17 | 587 |
| 62 | ROC + volume · 1h | momentum | 85.46 | -14.54 | 164 | 20.1 | -9.19 | -1.06 | -25.13 | 397 |
| 63 | ROC + volume | momentum | 73.58 | -26.42 | 423 | 22.7 | -72.41 | -15.88 | -74.72 | 1662 |
| 64 | Squeeze breakout | breakout | 69.52 | -30.48 | 354 | 15.5 | -62.12 | -17.91 | -62.12 | 1220 |
| 65 | Volume breakout | breakout | 69.30 | -30.70 | 281 | 14.6 | -61.59 | -17.44 | -61.65 | 895 |
| 66 | RSI(14) reversion | reversion | 68.73 | -31.27 | 430 | 27.0 | -73.90 | -17.26 | -74.08 | 1487 |
| 67 | EMA 20/50 cross | trend | 68.21 | -31.79 | 357 | 19.9 | -75.95 | -14.70 | -76.31 | 1431 |
| 68 | Donchian 55/20 | breakout | 66.96 | -33.04 | 360 | 17.5 | -68.02 | -14.12 | -69.18 | 1293 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -72.90 | -15.47 | -72.93 | 1416 |
| 70 | Supertrend | trend | 61.33 | -38.67 | 503 | 19.3 | -85.59 | -19.95 | -86.03 | 1891 |
| 71 | Keltner breakout | breakout | 61.20 | -38.80 | 485 | 14.6 | -82.92 | -25.85 | -83.21 | 1838 |
| 72 | AI bee: Boozy | ai | 59.99 | -40.01 | 266 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 57.05 | -42.95 | 436 | 9.9 | -82.10 | -22.65 | -82.11 | 1729 |
| 74 | MFI reversion | reversion | 55.26 | -44.74 | 628 | 20.1 | -87.89 | -27.00 | -88.08 | 2115 |
| 75 | AI bee: Bizzy | ai | 54.96 | -45.04 | 902 | 8.3 | — | — | — | — |
| 76 | Z-score reversion | reversion | 54.68 | -45.32 | 576 | 22.2 | -86.23 | -22.36 | -86.42 | 2078 |
| 77 | ADX DI cross | trend | 54.33 | -45.67 | 600 | 10.0 | -88.93 | -32.18 | -89.16 | 2110 |
| 78 | Donchian 20/10 | breakout | 52.97 | -47.03 | 684 | 17.5 | -90.56 | -24.64 | -90.79 | 2641 |
| 79 | MACD zero-line | trend | 51.34 | -48.66 | 640 | 15.2 | -91.28 | -28.75 | -91.38 | 2342 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.50 | -28.90 | -98.55 | 5299 |
| 81 | Trend pullback | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.12 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.05 | -28.82 | -93.15 | 2593 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.19 | -24.20 | -90.41 | 2357 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.25 | -31.21 | -97.32 | 3512 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -34.13 | -96.35 | 3578 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -25.30 | -94.36 | 2640 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.88 | -99.37 | 5635 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -30.70 | -96.30 | 3592 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.71 | -39.66 | -99.72 | 6133 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.21 | -36.01 | -97.23 | 3643 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.83 | -98.53 | 4662 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.24 | -31.52 | -93.30 | 2792 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.72 | -99.54 | 6107 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.04 | -32.55 | -96.05 | 3729 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.76 | -33.86 | -95.79 | 4047 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -44.72 | -99.88 | 8202 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T05:25 | RSI(14) reversion · 1h | buy | SOL-USD | 3.63 | — | entry |
| 2026-10-13T05:25 | RSI(14) reversion · 1h | buy | DOGE-USD | 5.60 | — | rebalance up |
| 2026-10-13T05:25 | RSI(14) reversion · 1h | sell | ETH-USD | 9.23 | 0.03 | take-profit |
| 2026-10-13T05:23 | AI bee: Bizzy | buy | ETH-USD | 8.11 | — | Jev: buy (buy p=0.59) |
| 2026-10-13T05:22 | AI bee: Bizzy | sell | DOGE-USD | 8.48 | -0.05 | Jev: sell (sell p=0.56) after 10 min |
| 2026-10-13T05:20 | Three white soldiers | buy | ETH-USD | 21.62 | — | entry signal |
| 2026-10-13T05:20 | Keltner breakout | sell | ETH-USD | 3.05 | 0.04 | rebalance down |
| 2026-10-13T05:15 | AI bee: Boozy | sell | ETH-USD | 13.86 | -0.05 | Jev: add (buy p=0.61) |
| 2026-10-13T05:15 | Volume breakout | buy | DOGE-USD | 17.33 | — | entry signal |
| 2026-10-13T05:12 | AI bee: Bizzy | buy | DOGE-USD | 8.53 | — | Jev: buy (buy p=0.62) |
| 2026-10-13T05:10 | Ichimoku | buy | XRP-USD | 14.27 | — | entry signal |
| 2026-10-13T05:09 | AI bee: Bizzy | sell | SOL-USD | 9.07 | -0.05 | Jev: sell (sell p=0.58) after 10 min |
| 2026-10-13T05:05 | Volume breakout | sell | DOGE-USD | 17.27 | -0.09 | exit signal |
| 2026-10-13T05:05 | ROC + volume | sell | DOGE-USD | 14.65 | 0.25 | exit signal |
| 2026-10-13T05:00 | CCI reversion · 1h | buy | DOGE-USD | 3.63 | — | entry |
| 2026-10-13T05:00 | CCI reversion · 1h | sell | BTC-USD | 3.63 | 0.02 | exit signal |
| 2026-10-13T05:00 | Williams %R · 1h | buy | XRP-USD | 14.22 | — | rebalance up |
| 2026-10-13T05:00 | Williams %R · 1h | sell | SOL-USD | 14.92 | 0.22 | exit signal |
| 2026-10-13T05:00 | Williams %R · 1h | sell | ETH-USD | 12.83 | 0.19 | exit signal |
| 2026-10-13T05:00 | Williams %R · 1h | sell | DOGE-USD | 12.82 | 0.18 | exit signal |
| 2026-10-13T05:00 | Stochastic reversion · 1h | buy | XRP-USD | 19.48 | — | entry |
| 2026-10-13T05:00 | Stochastic reversion · 1h | sell | SOL-USD | 10.91 | 0.07 | exit signal |
| 2026-10-13T05:00 | Stochastic reversion · 1h | sell | ETH-USD | 10.26 | 0.32 | exit signal |
| 2026-10-13T05:00 | Stochastic reversion · 1h | sell | DOGE-USD | 11.12 | 0.40 | exit signal |
| 2026-10-13T05:00 | Bollinger reversion · 1h | buy | SOL-USD | 5.72 | — | rebalance up |
| 2026-10-13T05:00 | Bollinger reversion · 1h | sell | ETH-USD | 10.19 | 0.15 | exit signal |
| 2026-10-13T05:00 | Three white soldiers · 1h | buy | ETH-USD | 24.29 | — | entry signal |
| 2026-10-13T05:00 | MACD cross · 1h | buy | ETH-USD | 6.38 | — | entry signal |
| 2026-10-13T05:00 | MACD cross · 1h | buy | DOGE-USD | 6.38 | — | entry signal |
| 2026-10-13T04:59 | AI bee: Boozy | buy | ETH-USD | 13.91 | — | Jev: buy (buy p=0.78) |
| 2026-10-13T04:59 | AI bee: Bizzy | buy | SOL-USD | 9.12 | — | Jev: buy (buy p=0.66) |
| 2026-10-13T04:50 | Volume breakout | sell | BTC-USD | 17.26 | -0.10 | exit signal |
| 2026-10-13T04:39 | AI bee: Bizzy | sell | SOL-USD | 8.16 | -0.04 | Jev: sell (sell p=0.54) after 12 min |
| 2026-10-13T04:35 | ROC + volume | buy | SOL-USD | 10.92 | — | rebalance up |
| 2026-10-13T04:35 | ROC + volume | sell | XRP-USD | 18.24 | 0.17 | exit signal |
| 2026-10-13T04:27 | AI bee: Bizzy | buy | SOL-USD | 8.19 | — | Jev: buy (buy p=0.59) |
| 2026-10-13T04:25 | MACD zero-line | sell | DOGE-USD | 10.32 | 0.15 | target is flat |
| 2026-10-13T04:20 | MACD zero-line | sell | SOL-USD | 12.88 | 0.12 | exit signal |
| 2026-10-13T04:19 | AI bee: Boozy | sell | ETH-USD | 13.91 | -0.09 | Jev: buy |
| 2026-10-13T04:15 | MACD zero-line | sell | ETH-USD | 10.30 | 0.13 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 05:25:05.000146+00:00 -> 2026-10-13 05:35:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
