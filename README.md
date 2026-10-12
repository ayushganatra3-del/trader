# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T03:55:05.000183+00:00 · 19795 ticks

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

Today: 3060 decisions in 612 calls, $0.0429 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T03:55 | 0 / 2 / 3 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T03:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T03:55 | 1 / 3 / 1 | COIN 76% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.26 | 3.26 | 37 | 43.2 | -7.44 | -2.25 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.53 | 2.53 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.20 | 2.20 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.01 | 2.01 | 14 | 57.1 | -15.29 | -2.50 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.33 | 1.33 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.24 | 1.25 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.09 | 1.09 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Hold BTC | benchmark | 99.83 | -0.17 | 0 | — | 30.19 | 3.55 | -8.68 | 1 |
| 14 | Max aggression: 1-day momentum | meta | 99.75 | -0.25 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.69 | -0.31 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Stochastic reversion · 1h | reversion | 99.12 | -0.88 | 89 | 55.1 | -9.77 | -1.87 | -14.61 | 337 |
| 19 | Donchian 55/20 · 1h | breakout | 99.06 | -0.94 | 28 | 14.3 | 12.98 | 1.61 | -16.96 | 113 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.59 | -1.41 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.56 | -1.44 | 0 | — | 11.52 | 1.86 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.80 | -2.20 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.31 | -2.69 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.17 | -2.83 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.04 | -2.96 | 78 | 23.1 | -23.14 | -6.51 | -25.39 | 167 |
| 27 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.23 | -2.08 | -9.70 | 259 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 29 | EMA 20/50 cross · 1h | trend | 96.59 | -3.40 | 40 | 12.5 | 5.06 | 0.77 | -19.85 | 139 |
| 30 | ADX DI cross · 1h | trend | 96.30 | -3.70 | 58 | 20.7 | -0.58 | 0.07 | -13.84 | 253 |
| 31 | Parabolic SAR · 1h | trend | 96.26 | -3.74 | 82 | 22.0 | -2.65 | -0.18 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.77 | -4.23 | 115 | 23.5 | -14.66 | -2.33 | -17.27 | 467 |
| 34 | Supertrend · 1h | trend | 95.35 | -4.65 | 53 | 13.2 | 0.22 | 0.22 | -18.22 | 212 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.04 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.48 | -6.52 | 119 | 34.5 | -9.93 | -1.55 | -17.79 | 123 |
| 38 | Squeeze breakout · 1h | breakout | 93.41 | -6.59 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.08 | -6.92 | 26 | 26.9 | -1.81 | -0.28 | -9.03 | 147 |
| 40 | Connors RSI(2) · 1h | reversion | 93.01 | -6.99 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.81 | -7.19 | 392 | 18.4 | -3.47 | -0.47 | -12.61 | 426 |
| 42 | Bollinger reversion · 1h | reversion | 92.73 | -7.27 | 78 | 37.2 | -20.80 | -4.93 | -23.20 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.65 | -7.35 | 64 | 15.6 | 4.36 | 0.72 | -17.15 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.10 | -7.90 | 58 | 19.0 | 7.61 | 1.19 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 91.95 | -8.05 | 44 | 18.2 | -1.08 | 0.07 | -21.18 | 124 |
| 46 | Williams %R · 1h | reversion | 91.52 | -8.48 | 126 | 47.6 | -23.65 | -4.03 | -26.91 | 511 |
| 47 | Bollinger breakout · 1h | breakout | 91.21 | -8.79 | 72 | 27.8 | 6.18 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.67 | -9.33 | 69 | 15.9 | -9.24 | -0.93 | -26.49 | 243 |
| 50 | Candlestick reversal · 1h | reversion | 90.37 | -9.63 | 118 | 33.1 | -26.04 | -5.02 | -28.11 | 507 |
| 51 | CCI reversion · 1h | reversion | 89.93 | -10.07 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.41 | -10.59 | 284 | 21.8 | -31.86 | -4.69 | -39.14 | 1278 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.72 | -11.28 | 149 | 18.8 | -12.98 | -1.48 | -28.50 | 325 |
| 55 | Donchian 20/10 · 1h | breakout | 88.62 | -11.38 | 60 | 18.3 | -0.62 | 0.13 | -18.15 | 227 |
| 56 | Heikin-Ashi · 1h | trend | 88.61 | -11.39 | 138 | 25.4 | -29.96 | -4.99 | -36.59 | 702 |
| 57 | MACD zero-line · 1h | trend | 88.10 | -11.90 | 66 | 18.2 | -6.79 | -0.73 | -20.89 | 239 |
| 58 | Max aggression: 5-day momentum | meta | 87.92 | -12.08 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.82 | -12.18 | 104 | 13.5 | -8.66 | -0.96 | -21.96 | 339 |
| 60 | Three white soldiers | momentum | 87.18 | -12.82 | 142 | 17.6 | -48.06 | -22.87 | -48.07 | 590 |
| 61 | Keltner breakout · 1h | breakout | 87.05 | -12.95 | 43 | 18.6 | -11.90 | -1.37 | -25.51 | 218 |
| 62 | ROC + volume · 1h | momentum | 86.22 | -13.78 | 132 | 21.2 | -10.07 | -1.20 | -23.62 | 414 |
| 63 | ROC + volume | momentum | 74.87 | -25.13 | 395 | 23.3 | -72.75 | -16.37 | -73.92 | 1679 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 375 | 27.5 | -72.59 | -17.93 | -72.63 | 1493 |
| 65 | Squeeze breakout | breakout | 70.67 | -29.33 | 336 | 15.5 | -62.03 | -17.90 | -62.16 | 1230 |
| 66 | Volume breakout | breakout | 70.12 | -29.88 | 269 | 14.1 | -62.39 | -17.74 | -62.49 | 905 |
| 67 | Donchian 55/20 | breakout | 69.26 | -30.74 | 342 | 18.4 | -67.74 | -14.41 | -67.88 | 1298 |
| 68 | EMA 20/50 cross | trend | 68.78 | -31.22 | 344 | 20.1 | -76.84 | -15.25 | -76.86 | 1457 |
| 69 | VWAP reversion | reversion | 67.74 | -32.26 | 405 | 25.9 | -71.56 | -15.84 | -71.62 | 1435 |
| 70 | Supertrend | trend | 62.61 | -37.39 | 474 | 20.0 | -86.08 | -20.99 | -86.12 | 1918 |
| 71 | Keltner breakout | breakout | 61.76 | -38.24 | 463 | 14.7 | -83.84 | -27.57 | -83.85 | 1856 |
| 72 | AI bee: Boozy | ai | 60.06 | -39.94 | 259 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 59.84 | -40.16 | 415 | 10.4 | -81.68 | -23.00 | -81.69 | 1751 |
| 74 | Z-score reversion | reversion | 58.93 | -41.07 | 516 | 22.1 | -85.05 | -22.69 | -85.06 | 2073 |
| 75 | MFI reversion | reversion | 58.30 | -41.70 | 524 | 20.8 | -87.55 | -27.85 | -87.58 | 2122 |
| 76 | AI bee: Bizzy | ai | 56.52 | -43.48 | 859 | 8.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.71 | -44.29 | 554 | 10.3 | -89.19 | -34.46 | -89.19 | 2118 |
| 78 | Donchian 20/10 | breakout | 54.16 | -45.84 | 651 | 18.1 | -90.85 | -26.03 | -90.85 | 2670 |
| 79 | Trend pullback | trend | 52.91 | -47.09 | 607 | 14.5 | -91.17 | -27.05 | -91.17 | 2345 |
| 80 | RSI momentum | momentum | 52.62 | -47.38 | 626 | 16.9 | -90.44 | -25.75 | -90.44 | 2391 |
| 81 | MACD zero-line | trend | 52.39 | -47.61 | 606 | 14.7 | -91.50 | -29.71 | -91.50 | 2367 |
| 82 | Triple EMA stack | trend | 51.67 | -48.33 | 650 | 15.4 | -93.24 | -30.11 | -93.24 | 2628 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.98 | -98.64 | 5390 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.27 | -97.36 | 3551 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.45 | -35.87 | -96.45 | 3622 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.21 | -25.47 | -94.21 | 2692 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.46 | -99.35 | 5695 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.49 | -31.96 | -96.49 | 3642 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.67 | -99.73 | 6204 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.88 | -97.36 | 3694 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -36.42 | -98.45 | 4706 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.54 | -33.02 | -93.54 | 2823 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.87 | -99.52 | 6159 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.80 | -33.02 | -95.81 | 3742 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.60 | -33.77 | -95.60 | 4086 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.52 | -99.89 | 8314 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T03:55 | Donchian 20/10 | sell | SOL-USD | 13.51 | -0.14 | exit signal |
| 2026-10-12T03:55 | RSI momentum | sell | SOL-USD | 13.15 | -0.13 | exit signal |
| 2026-10-12T03:55 | Trend pullback | buy | DOGE-USD | 13.25 | — | entry |
| 2026-10-12T03:55 | Trend pullback | sell | SOL-USD | 13.24 | -0.07 | exit signal |
| 2026-10-12T03:55 | Ichimoku | sell | SOL-USD | 14.95 | -0.15 | exit signal |
| 2026-10-12T03:55 | ADX DI cross | sell | SOL-USD | 13.89 | -0.08 | exit signal |
| 2026-10-12T03:50 | Trend pullback | sell | DOGE-USD | 13.25 | -0.07 | exit signal |
| 2026-10-12T03:40 | Triple EMA stack | sell | SOL-USD | 12.96 | -0.04 | exit signal |
| 2026-10-12T03:35 | MFI reversion | buy | BTC-USD | 14.59 | — | entry signal |
| 2026-10-12T03:34 | AI bee: Bizzy | sell | DOGE-USD | 7.91 | -0.05 | Jev: sell (sell p=0.79) after 10 min |
| 2026-10-12T03:30 | RSI momentum | sell | ETH-USD | 10.55 | -0.08 | exit signal |
| 2026-10-12T03:30 | Trend pullback | sell | ETH-USD | 13.21 | -0.11 | exit signal |
| 2026-10-12T03:24 | AI bee: Bizzy | buy | DOGE-USD | 7.95 | — | Jev: buy (buy p=0.56) |
| 2026-10-12T03:20 | Triple EMA stack | sell | ETH-USD | 12.93 | -0.08 | exit signal |
| 2026-10-12T03:10 | Keltner breakout | sell | SOL-USD | 15.41 | -0.15 | exit signal |
| 2026-10-12T03:10 | RSI momentum | sell | BTC-USD | 10.54 | -0.10 | stop-loss |
| 2026-10-12T03:10 | Ichimoku | sell | DOGE-USD | 14.97 | -0.13 | exit signal |
| 2026-10-12T03:10 | Ichimoku | sell | BTC-USD | 14.96 | -0.13 | exit signal |
| 2026-10-12T03:10 | Triple EMA stack | sell | BTC-USD | 12.89 | -0.09 | exit signal |
| 2026-10-12T03:05 | RSI momentum | sell | XRP-USD | 13.16 | -0.13 | stop-loss |
| 2026-10-12T03:05 | Trend pullback | sell | BTC-USD | 13.22 | -0.08 | exit signal |
| 2026-10-12T03:05 | ADX DI cross | sell | BTC-USD | 13.88 | -0.09 | exit signal |
| 2026-10-12T03:05 | MACD zero-line | sell | BTC-USD | 13.03 | -0.09 | exit signal |
| 2026-10-12T03:00 | Keltner breakout | sell | ETH-USD | 15.40 | -0.16 | stop-loss |
| 2026-10-12T03:00 | Donchian 55/20 | sell | ETH-USD | 17.26 | -0.18 | stop-loss |
| 2026-10-12T03:00 | Donchian 20/10 | sell | ETH-USD | 13.51 | -0.14 | stop-loss |
| 2026-10-12T03:00 | Ichimoku | sell | ETH-USD | 14.96 | -0.13 | exit signal |
| 2026-10-12T02:58 | AI bee: Bizzy | sell | DOGE-USD | 7.96 | -0.05 | Jev: sell (sell p=0.71) after 11 min |
| 2026-10-12T02:55 | Trend pullback | buy | ETH-USD | 13.32 | — | entry signal |
| 2026-10-12T02:50 | Volume breakout | sell | ETH-USD | 17.40 | -0.17 | exit signal |
| 2026-10-12T02:47 | AI bee: Bizzy | buy | DOGE-USD | 8.01 | — | Jev: buy (buy p=0.57) |
| 2026-10-12T02:44 | AI bee: Bizzy | sell | SOL-USD | 8.55 | -0.05 | Jev: sell (sell p=0.57) after 13 min |
| 2026-10-12T02:40 | Ichimoku | buy | SOL-USD | 15.10 | — | entry signal |
| 2026-10-12T02:40 | Ichimoku | buy | ETH-USD | 15.10 | — | entry signal |
| 2026-10-12T02:40 | Ichimoku | buy | DOGE-USD | 15.10 | — | entry signal |
| 2026-10-12T02:40 | Ichimoku | buy | BTC-USD | 15.10 | — | entry signal |
| 2026-10-12T02:31 | AI bee: Bizzy | buy | SOL-USD | 8.60 | — | Jev: buy (buy p=0.61) |
| 2026-10-12T02:30 | Trend pullback | buy | DOGE-USD | 13.31 | — | entry signal |
| 2026-10-12T02:30 | MACD zero-line | buy | BTC-USD | 13.12 | — | entry signal |
| 2026-10-12T02:29 | AI bee: Bizzy | sell | ETH-USD | 8.79 | -0.08 | Jev: sell (sell p=0.65) after 10 min |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 03:55:05.000183+00:00 -> 2026-10-12 04:05:05.000183+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
