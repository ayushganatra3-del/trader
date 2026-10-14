# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T09:55:05.000179+00:00 · 22338 ticks

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

Today: 7360 decisions in 1472 calls, $0.1029 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T09:55 | 0 / 5 / 0 | AMD 14% |  |
| Breezy | 2026-10-14T09:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T09:55 | 2 / 3 / 0 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.09 | 3.09 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.06 | -2.68 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.78 | 1.78 | 18 | 50.0 | -15.68 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.02 | 1.02 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.39 | 0.39 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.81 | -0.19 | 0 | — | 4.58 | 1.76 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.80 | -0.20 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.28 | -0.72 | 0 | — | 30.44 | 3.51 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.92 | -1.08 | 0 | — | -8.34 | -1.50 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.38 | -1.62 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.76 | -2.24 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.45 | -2.55 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.34 | -2.66 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.75 | -3.23 | -9.41 | 302 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | Stochastic reversion · 1h | reversion | 96.23 | -3.77 | 107 | 51.4 | -14.16 | -2.74 | -16.23 | 343 |
| 26 | ADX DI cross · 1h | trend | 96.22 | -3.78 | 65 | 18.5 | -10.80 | -1.98 | -14.81 | 250 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.75 | -4.25 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | Z-score reversion · 1h | reversion | 95.37 | -4.62 | 52 | 44.2 | 2.77 | 0.68 | -8.60 | 158 |
| 29 | MACD cross · 1h | trend | 95.38 | -4.62 | 133 | 23.3 | -8.64 | -1.11 | -19.25 | 457 |
| 30 | EMA 20/50 cross · 1h | trend | 95.35 | -4.65 | 45 | 15.6 | 10.08 | 1.28 | -20.35 | 137 |
| 31 | Max aggression: 1-day momentum | meta | 95.33 | -4.67 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.87 | -5.08 | -8.87 | 233 |
| 33 | Squeeze breakout · 1h | breakout | 93.94 | -6.06 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 34 | Supertrend · 1h | trend | 93.88 | -6.12 | 60 | 13.3 | 2.10 | 0.46 | -20.32 | 213 |
| 35 | Parabolic SAR · 1h | trend | 93.57 | -6.43 | 90 | 22.2 | 1.68 | 0.40 | -22.83 | 288 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.97 | -0.62 | -5.61 | 111 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.62 | 2.18 | -6.70 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.59 | -7.41 | 66 | 15.2 | 1.18 | 0.35 | -25.56 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.51 | -7.49 | 165 | 31.5 | -8.80 | -1.38 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 92.00 | -8.00 | 127 | 42.5 | -19.97 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.41 | -8.60 | 38 | 34.2 | 3.92 | 0.94 | -9.40 | 134 |
| 42 | Ichimoku · 1h | trend | 91.28 | -8.72 | 48 | 16.7 | 1.92 | 0.43 | -22.34 | 125 |
| 43 | Agent (ML meta-label) | meta | 91.04 | -8.96 | 485 | 18.1 | 1.09 | 0.33 | -11.49 | 375 |
| 44 | Volume breakout · 1h | breakout | 90.67 | -9.33 | 75 | 22.7 | 8.60 | 1.31 | -12.60 | 120 |
| 45 | Bollinger breakout · 1h | breakout | 90.66 | -9.34 | 77 | 28.6 | 7.26 | 1.07 | -14.21 | 278 |
| 46 | Triple EMA stack · 1h | trend | 90.66 | -9.34 | 71 | 15.5 | -7.45 | -0.57 | -32.27 | 240 |
| 47 | Bollinger reversion · 1h | reversion | 89.99 | -10.01 | 97 | 37.1 | -23.78 | -5.71 | -24.98 | 321 |
| 48 | Williams %R · 1h | reversion | 89.40 | -10.60 | 143 | 45.5 | -28.24 | -4.79 | -29.72 | 511 |
| 49 | CCI reversion · 1h | reversion | 88.88 | -11.12 | 120 | 45.0 | -9.92 | -1.30 | -14.42 | 417 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.51 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.07 | -11.93 | 159 | 18.2 | -9.64 | -0.80 | -33.87 | 321 |
| 52 | MACD zero-line · 1h | trend | 87.37 | -12.63 | 69 | 17.4 | -22.39 | -4.36 | -22.71 | 230 |
| 53 | VWAP momentum · 1h | momentum | 87.30 | -12.70 | 333 | 22.8 | -33.44 | -4.96 | -40.76 | 1254 |
| 54 | Donchian 20/10 · 1h | breakout | 86.97 | -13.03 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 86.74 | -13.26 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 86.67 | -13.33 | 49 | 20.4 | -8.31 | -0.89 | -26.76 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 86.61 | -13.39 | 110 | 12.7 | -10.48 | -1.33 | -24.28 | 330 |
| 58 | Heikin-Ashi · 1h | trend | 86.56 | -13.44 | 166 | 26.5 | -29.46 | -4.81 | -38.65 | 673 |
| 59 | Candlestick reversal · 1h | reversion | 86.42 | -13.58 | 143 | 30.8 | -31.11 | -5.98 | -31.59 | 483 |
| 60 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.83 | 698 |
| 61 | Three white soldiers | momentum | 85.93 | -14.07 | 167 | 18.0 | -47.63 | -21.95 | -47.78 | 583 |
| 62 | ROC + volume · 1h | momentum | 85.30 | -14.70 | 173 | 20.2 | -8.96 | -1.02 | -24.87 | 399 |
| 63 | ROC + volume | momentum | 69.96 | -30.04 | 463 | 22.0 | -73.46 | -16.51 | -75.51 | 1673 |
| 64 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.37 | -16.75 | -73.75 | 1476 |
| 65 | Volume breakout | breakout | 67.00 | -33.00 | 301 | 14.0 | -62.12 | -17.42 | -62.40 | 892 |
| 66 | Squeeze breakout | breakout | 66.91 | -33.09 | 384 | 15.1 | -62.59 | -17.96 | -62.80 | 1222 |
| 67 | EMA 20/50 cross | trend | 64.58 | -35.42 | 400 | 19.8 | -76.75 | -15.01 | -77.21 | 1442 |
| 68 | Donchian 55/20 | breakout | 63.13 | -36.87 | 395 | 16.7 | -69.34 | -14.51 | -70.80 | 1287 |
| 69 | VWAP reversion | reversion | 62.40 | -37.60 | 488 | 25.4 | -72.12 | -15.06 | -72.12 | 1397 |
| 70 | AI bee: Boozy | ai | 59.77 | -40.23 | 271 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 57.96 | -42.04 | 556 | 19.4 | -85.85 | -20.36 | -85.85 | 1913 |
| 72 | Keltner breakout | breakout | 57.50 | -42.50 | 540 | 14.3 | -83.27 | -26.82 | -83.27 | 1848 |
| 73 | Ichimoku | trend | 54.01 | -45.99 | 482 | 9.5 | -82.37 | -22.82 | -82.37 | 1723 |
| 74 | AI bee: Bizzy | ai | 52.97 | -47.03 | 962 | 8.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 52.69 | -47.31 | 675 | 20.1 | -87.76 | -26.88 | -87.76 | 2113 |
| 76 | Z-score reversion | reversion | 52.23 | -47.77 | 625 | 23.0 | -85.95 | -21.72 | -85.96 | 2082 |
| 77 | ADX DI cross | trend | 50.88 | -49.12 | 656 | 10.4 | -89.29 | -33.46 | -89.29 | 2116 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.50 | -28.98 | -98.50 | 5308 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -29.65 | -93.47 | 2617 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.46 | -24.64 | -90.46 | 2374 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.68 | -26.36 | -91.68 | 2356 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -31.89 | -97.37 | 3535 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.54 | -35.08 | -96.55 | 3605 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.63 | -25.66 | -94.63 | 2656 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.23 | -99.37 | 5645 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.96 | -25.49 | -90.96 | 2634 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.40 | -30.60 | -96.40 | 3602 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.50 | -99.72 | 6155 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.56 | -29.20 | -91.56 | 2362 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.40 | -36.23 | -97.40 | 3674 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -34.92 | -98.50 | 4673 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.39 | -31.77 | -93.39 | 2800 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.79 | -99.54 | 6125 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -31.35 | -95.94 | 3733 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.68 | -33.14 | -95.68 | 4047 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.59 | -99.89 | 8206 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T09:55 | MFI reversion | buy | XRP-USD | 13.18 | — | entry signal |
| 2026-10-14T09:55 | VWAP reversion | buy | ETH-USD | 15.61 | — | entry signal |
| 2026-10-14T09:40 | MFI reversion | buy | SOL-USD | 13.20 | — | entry signal |
| 2026-10-14T09:35 | VWAP reversion | buy | SOL-USD | 15.63 | — | entry signal |
| 2026-10-14T09:35 | VWAP reversion | buy | DOGE-USD | 15.63 | — | entry signal |
| 2026-10-14T09:35 | Z-score reversion | buy | SOL-USD | 13.07 | — | entry signal |
| 2026-10-14T09:35 | Z-score reversion | buy | DOGE-USD | 13.07 | — | entry signal |
| 2026-10-14T09:30 | MFI reversion | buy | BTC-USD | 13.20 | — | entry signal |
| 2026-10-14T09:30 | EMA 20/50 cross | sell | XRP-USD | 12.89 | -0.12 | stop-loss |
| 2026-10-14T09:05 | ADX DI cross | sell | ETH-USD | 12.68 | -0.10 | exit signal |
| 2026-10-14T09:00 | CCI reversion · 1h | sell | XRP-USD | 9.77 | -0.01 | exit signal |
| 2026-10-14T09:00 | Candlestick reversal · 1h | sell | DOGE-USD | 7.19 | -0.02 | exit signal |
| 2026-10-14T09:00 | OBV trend · 1h | sell | BTC-USD | 4.10 | -0.02 | exit signal |
| 2026-10-14T09:00 | MACD cross · 1h | sell | BTC-USD | 3.60 | -0.03 | exit signal |
| 2026-10-14T09:00 | ADX DI cross | sell | XRP-USD | 12.67 | -0.11 | exit signal |
| 2026-10-14T08:55 | ADX DI cross | buy | XRP-USD | 12.77 | — | entry signal |
| 2026-10-14T08:55 | ADX DI cross | buy | ETH-USD | 12.77 | — | entry signal |
| 2026-10-14T08:50 | ADX DI cross | sell | XRP-USD | 12.77 | -0.06 | exit signal |
| 2026-10-14T08:45 | ADX DI cross | sell | BTC-USD | 12.71 | -0.11 | stop-loss |
| 2026-10-14T08:45 | Supertrend | sell | XRP-USD | 11.61 | -0.08 | exit signal |
| 2026-10-14T08:45 | Supertrend | sell | SOL-USD | 14.48 | -0.17 | exit signal |
| 2026-10-14T08:45 | Supertrend | sell | ETH-USD | 14.50 | -0.13 | exit signal |
| 2026-10-14T08:45 | Supertrend | sell | BTC-USD | 11.60 | -0.10 | exit signal |
| 2026-10-14T08:40 | Volume breakout | sell | XRP-USD | 13.39 | -0.09 | exit signal |
| 2026-10-14T08:40 | Volume breakout | sell | BTC-USD | 13.40 | -0.08 | exit signal |
| 2026-10-14T08:40 | Supertrend | buy | SOL-USD | 5.84 | — | rebalance up |
| 2026-10-14T08:40 | Supertrend | sell | DOGE-USD | 11.61 | -0.09 | exit signal |
| 2026-10-14T08:35 | Volume breakout | sell | SOL-USD | 13.41 | -0.07 | exit signal |
| 2026-10-14T08:35 | Volume breakout | sell | ETH-USD | 16.76 | -0.10 | exit signal |
| 2026-10-14T08:30 | Volume breakout | buy | ETH-USD | 3.37 | — | rebalance up |
| 2026-10-14T08:30 | Volume breakout | sell | DOGE-USD | 13.41 | -0.07 | exit signal |
| 2026-10-14T08:30 | Supertrend | buy | SOL-USD | 2.92 | — | rebalance up |
| 2026-10-14T08:30 | Supertrend | sell | BTC-USD | 2.92 | -0.01 | rebalance down |
| 2026-10-14T08:25 | Squeeze breakout | sell | SOL-USD | 16.64 | -0.20 | stop-loss |
| 2026-10-14T08:25 | Squeeze breakout | sell | ETH-USD | 16.72 | -0.11 | stop-loss |
| 2026-10-14T08:25 | Keltner breakout | sell | XRP-USD | 11.53 | -0.06 | stop-loss |
| 2026-10-14T08:25 | Keltner breakout | sell | SOL-USD | 14.37 | -0.16 | stop-loss |
| 2026-10-14T08:25 | Keltner breakout | sell | ETH-USD | 11.52 | -0.07 | stop-loss |
| 2026-10-14T08:25 | Keltner breakout | sell | DOGE-USD | 14.37 | -0.15 | stop-loss |
| 2026-10-14T08:25 | Donchian 55/20 | sell | XRP-USD | 12.63 | -0.13 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 09:55:05.000179+00:00 -> 2026-10-14 10:05:05.000179+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
