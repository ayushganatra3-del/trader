# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T07:25:05.000121+00:00 · 22218 ticks

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
| Copy: Insider buying | 2026-10-14 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-13)

**Uptrend** since 2026-09-21 · level caution · 4 distribution days in 25 sessions · timing exposure 75% · VXN 21.14 · VIX 15.27 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.0, MSFT 7.9, BITX 6.5, META 6.1, MSTR 6.0, UPRO 5.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 5560 decisions in 1112 calls, $0.0777 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T07:25 | 0 / 2 / 3 | XRP-USD 14%, AMD 14% |  |
| Breezy | 2026-10-14T07:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T07:25 | 1 / 4 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.37 | +3.06% | 4 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Z-score reversion | GOOGL | 1.73 | +0.66% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.03 | 3.03 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.06 | -2.68 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.73 | 1.73 | 18 | 50.0 | -15.68 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 100.96 | 0.96 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.33 | 0.33 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 99.76 | -0.24 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 99.75 | -0.25 | 0 | — | 4.58 | 1.76 | -5.18 | 1 |
| 14 | Hold BTC | benchmark | 99.45 | -0.56 | 0 | — | 30.45 | 3.51 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.88 | -1.12 | 0 | — | -8.34 | -1.50 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.32 | -1.68 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.71 | -2.29 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.39 | -2.61 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.29 | -2.71 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.75 | -3.23 | -9.41 | 302 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.26 | -3.75 | 65 | 18.5 | -11.26 | -2.07 | -14.81 | 253 |
| 26 | Stochastic reversion · 1h | reversion | 96.17 | -3.83 | 107 | 51.4 | -14.16 | -2.74 | -16.23 | 343 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.70 | -4.30 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.46 | -4.54 | 132 | 23.5 | -8.65 | -1.11 | -19.25 | 458 |
| 29 | Z-score reversion · 1h | reversion | 95.40 | -4.60 | 52 | 44.2 | 2.85 | 0.69 | -8.60 | 158 |
| 30 | EMA 20/50 cross · 1h | trend | 95.29 | -4.71 | 45 | 15.6 | 10.35 | 1.31 | -20.35 | 136 |
| 31 | Max aggression: 1-day momentum | meta | 95.28 | -4.72 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.87 | -5.08 | -8.87 | 233 |
| 33 | Squeeze breakout · 1h | breakout | 93.92 | -6.08 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 34 | Supertrend · 1h | trend | 93.92 | -6.08 | 60 | 13.3 | 2.23 | 0.47 | -20.32 | 213 |
| 35 | Parabolic SAR · 1h | trend | 93.57 | -6.43 | 90 | 22.2 | 1.74 | 0.41 | -22.79 | 288 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.97 | -0.62 | -5.61 | 111 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.62 | 2.18 | -6.70 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.54 | -7.46 | 66 | 15.2 | 1.20 | 0.35 | -25.56 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.46 | -7.54 | 165 | 31.5 | -8.80 | -1.38 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 91.94 | -8.06 | 127 | 42.5 | -19.97 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.43 | -8.57 | 38 | 34.2 | 4.53 | 1.06 | -9.40 | 133 |
| 42 | Ichimoku · 1h | trend | 91.22 | -8.78 | 48 | 16.7 | 2.06 | 0.44 | -22.34 | 124 |
| 43 | Agent (ML meta-label) | meta | 90.99 | -9.01 | 485 | 18.1 | -0.34 | 0.08 | -13.51 | 377 |
| 44 | Volume breakout · 1h | breakout | 90.64 | -9.36 | 75 | 22.7 | 8.60 | 1.31 | -12.60 | 120 |
| 45 | Triple EMA stack · 1h | trend | 90.64 | -9.36 | 71 | 15.5 | -7.25 | -0.55 | -32.27 | 239 |
| 46 | Bollinger breakout · 1h | breakout | 90.64 | -9.36 | 77 | 28.6 | 7.26 | 1.07 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 89.95 | -10.05 | 97 | 37.1 | -23.78 | -5.71 | -24.98 | 321 |
| 48 | Williams %R · 1h | reversion | 89.35 | -10.65 | 143 | 45.5 | -27.99 | -4.75 | -29.52 | 510 |
| 49 | CCI reversion · 1h | reversion | 88.91 | -11.09 | 119 | 45.4 | -9.53 | -1.24 | -14.42 | 416 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.51 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.03 | -11.96 | 158 | 18.4 | -9.47 | -0.78 | -33.87 | 320 |
| 52 | MACD zero-line · 1h | trend | 87.42 | -12.58 | 69 | 17.4 | -22.16 | -4.31 | -22.65 | 230 |
| 53 | VWAP momentum · 1h | momentum | 87.27 | -12.73 | 333 | 22.8 | -33.67 | -5.00 | -40.76 | 1256 |
| 54 | Donchian 20/10 · 1h | breakout | 86.92 | -13.08 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 86.69 | -13.31 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 86.65 | -13.35 | 49 | 20.4 | -8.31 | -0.89 | -26.76 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 86.61 | -13.39 | 110 | 12.7 | -10.24 | -1.29 | -24.20 | 329 |
| 58 | Heikin-Ashi · 1h | trend | 86.53 | -13.47 | 166 | 26.5 | -30.03 | -4.93 | -38.65 | 678 |
| 59 | Candlestick reversal · 1h | reversion | 86.41 | -13.59 | 142 | 31.0 | -30.86 | -5.92 | -31.38 | 481 |
| 60 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.83 | 698 |
| 61 | Three white soldiers | momentum | 85.93 | -14.07 | 167 | 18.0 | -47.84 | -22.26 | -47.84 | 585 |
| 62 | ROC + volume · 1h | momentum | 85.25 | -14.75 | 173 | 20.2 | -8.96 | -1.02 | -24.87 | 399 |
| 63 | ROC + volume | momentum | 70.74 | -29.27 | 458 | 22.3 | -73.14 | -16.36 | -75.21 | 1668 |
| 64 | Volume breakout | breakout | 67.41 | -32.59 | 296 | 14.2 | -61.82 | -17.28 | -62.10 | 887 |
| 65 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.64 | -16.88 | -74.02 | 1481 |
| 66 | Squeeze breakout | breakout | 67.30 | -32.70 | 381 | 15.2 | -62.37 | -17.83 | -62.58 | 1219 |
| 67 | EMA 20/50 cross | trend | 65.32 | -34.68 | 395 | 20.0 | -76.61 | -14.99 | -76.92 | 1440 |
| 68 | Donchian 55/20 | breakout | 63.83 | -36.17 | 390 | 16.9 | -69.03 | -14.44 | -70.45 | 1283 |
| 69 | VWAP reversion | reversion | 62.53 | -37.47 | 488 | 25.4 | -72.65 | -15.25 | -72.67 | 1406 |
| 70 | AI bee: Boozy | ai | 59.84 | -40.16 | 270 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 58.54 | -41.46 | 551 | 19.6 | -85.78 | -20.32 | -85.78 | 1912 |
| 72 | Keltner breakout | breakout | 58.02 | -41.98 | 535 | 14.4 | -83.11 | -26.66 | -83.11 | 1843 |
| 73 | Ichimoku | trend | 54.01 | -45.99 | 482 | 9.5 | -82.34 | -22.79 | -82.34 | 1722 |
| 74 | AI bee: Bizzy | ai | 53.10 | -46.90 | 958 | 8.5 | — | — | — | — |
| 75 | MFI reversion | reversion | 52.77 | -47.23 | 674 | 20.2 | -87.88 | -26.96 | -87.88 | 2115 |
| 76 | Z-score reversion | reversion | 52.31 | -47.69 | 623 | 23.1 | -85.98 | -21.72 | -85.99 | 2084 |
| 77 | ADX DI cross | trend | 51.23 | -48.77 | 652 | 10.4 | -89.20 | -33.17 | -89.20 | 2113 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -28.81 | -98.48 | 5302 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.38 | -29.48 | -93.38 | 2612 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.37 | -24.54 | -90.37 | 2370 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.68 | -26.38 | -91.68 | 2356 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -31.72 | -97.34 | 3531 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -34.90 | -96.50 | 3600 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.51 | -25.33 | -94.51 | 2643 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.21 | -99.37 | 5646 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.87 | -25.37 | -90.87 | 2630 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -30.49 | -96.38 | 3600 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.67 | -99.72 | 6164 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.50 | -29.06 | -91.50 | 2360 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.41 | -36.41 | -97.41 | 3677 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.03 | -98.52 | 4678 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.36 | -31.63 | -93.36 | 2796 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.79 | -99.54 | 6129 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.99 | -31.49 | -95.99 | 3742 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.68 | -32.92 | -95.68 | 4047 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.61 | -99.89 | 8210 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T07:25 | Z-score reversion | sell | XRP-USD | 13.05 | -0.02 | exit signal |
| 2026-10-14T07:21 | AI bee: Bizzy | buy | XRP-USD | 7.32 | — | Jev: buy (buy p=0.55) |
| 2026-10-14T07:20 | ADX DI cross | sell | ETH-USD | 12.76 | -0.08 | exit signal |
| 2026-10-14T07:18 | AI bee: Bizzy | sell | SOL-USD | 7.28 | -0.05 | Jev: sell (sell p=0.65) after 10 min |
| 2026-10-14T07:15 | VWAP reversion | sell | XRP-USD | 15.62 | -0.02 | exit signal |
| 2026-10-14T07:10 | MFI reversion | sell | XRP-USD | 13.16 | -0.06 | exit signal |
| 2026-10-14T07:10 | ADX DI cross | buy | XRP-USD | 12.83 | — | entry signal |
| 2026-10-14T07:10 | ADX DI cross | buy | ETH-USD | 12.83 | — | entry signal |
| 2026-10-14T07:08 | AI bee: Bizzy | buy | SOL-USD | 7.33 | — | Jev: buy (buy p=0.55) |
| 2026-10-14T06:25 | AI bee: Bizzy | sell | SOL-USD | 7.34 | -0.05 | Jev: sell (sell p=0.71) after 10 min |
| 2026-10-14T06:15 | AI bee: Bizzy | buy | SOL-USD | 7.39 | — | Jev: buy (buy p=0.56) |
| 2026-10-14T06:15 | MFI reversion | buy | XRP-USD | 13.22 | — | entry signal |
| 2026-10-14T06:15 | MFI reversion | buy | ETH-USD | 13.22 | — | entry signal |
| 2026-10-14T06:10 | Z-score reversion | buy | XRP-USD | 13.07 | — | entry signal |
| 2026-10-14T06:05 | EMA 20/50 cross | sell | BTC-USD | 16.32 | -0.13 | exit signal |
| 2026-10-14T06:00 | Candlestick reversal · 1h | sell | SOL-USD | 7.79 | -0.08 | exit signal |
| 2026-10-14T06:00 | VWAP momentum · 1h | sell | XRP-USD | 2.30 | -0.03 | exit signal |
| 2026-10-14T06:00 | VWAP momentum · 1h | sell | SOL-USD | 6.19 | -0.02 | exit signal |
| 2026-10-14T06:00 | VWAP momentum · 1h | sell | ETH-USD | 5.41 | -0.06 | exit signal |
| 2026-10-14T06:00 | VWAP momentum · 1h | sell | DOGE-USD | 5.41 | -0.06 | exit signal |
| 2026-10-14T06:00 | VWAP momentum · 1h | sell | BTC-USD | 5.42 | -0.05 | exit signal |
| 2026-10-14T06:00 | Heikin-Ashi · 1h | sell | BTC-USD | 21.48 | -0.21 | exit signal |
| 2026-10-14T06:00 | ADX DI cross · 1h | sell | DOGE-USD | 7.66 | -0.09 | exit signal |
| 2026-10-14T06:00 | VWAP reversion | buy | XRP-USD | 15.64 | — | entry signal |
| 2026-10-14T06:00 | Z-score reversion | buy | SOL-USD | 13.09 | — | entry signal |
| 2026-10-14T06:00 | Z-score reversion | buy | DOGE-USD | 13.09 | — | entry signal |
| 2026-10-14T05:40 | EMA 20/50 cross | sell | XRP-USD | 16.27 | -0.18 | stop-loss |
| 2026-10-14T05:35 | AI bee: Bizzy | sell | DOGE-USD | 7.53 | -0.05 | Jev: sell (sell p=0.71) after 10 min |
| 2026-10-14T05:30 | MFI reversion | sell | DOGE-USD | 13.18 | -0.09 | exit signal |
| 2026-10-14T05:25 | AI bee: Bizzy | buy | DOGE-USD | 7.58 | — | Jev: buy (buy p=0.57) |
| 2026-10-14T05:10 | MFI reversion | sell | BTC-USD | 13.15 | -0.12 | stop-loss |
| 2026-10-14T05:10 | Keltner breakout | sell | DOGE-USD | 14.39 | -0.16 | target is flat |
| 2026-10-14T05:10 | Donchian 55/20 | sell | DOGE-USD | 15.83 | -0.18 | stop-loss |
| 2026-10-14T05:10 | Ichimoku | sell | SOL-USD | 13.44 | -0.13 | exit signal |
| 2026-10-14T05:10 | Ichimoku | sell | DOGE-USD | 13.46 | -0.12 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | XRP-USD | 11.72 | -0.12 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | SOL-USD | 11.71 | -0.16 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | ETH-USD | 11.73 | -0.12 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | DOGE-USD | 11.62 | -0.09 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | BTC-USD | 11.76 | -0.10 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 07:25:05.000121+00:00 -> 2026-10-14 07:35:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
