# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T08:55:05.000158+00:00 · 22286 ticks

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

Today: 6580 decisions in 1316 calls, $0.0920 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T08:55 | 0 / 5 / 0 | AMD 14% |  |
| Breezy | 2026-10-14T08:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T08:55 | 1 / 4 / 0 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.10 | 3.10 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.06 | -2.68 | -13.79 | 117 |
| 3 | Copy: Insider buying | copy | 101.80 | 1.80 | 18 | 50.0 | -15.68 | -2.48 | -21.97 | 75 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.03 | 1.03 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.40 | 0.40 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.82 | -0.18 | 0 | — | 4.58 | 1.76 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.81 | -0.19 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.61 | -0.39 | 0 | — | 30.59 | 3.52 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.93 | -1.07 | 0 | — | -8.34 | -1.50 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.39 | -1.61 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.77 | -2.23 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.46 | -2.54 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.36 | -2.65 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.02 | -2.86 | -8.69 | 309 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.30 | -3.70 | 65 | 18.5 | -11.39 | -2.10 | -14.81 | 254 |
| 26 | Stochastic reversion · 1h | reversion | 96.24 | -3.76 | 107 | 51.4 | -14.16 | -2.74 | -16.23 | 343 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.76 | -4.24 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.55 | -4.45 | 132 | 23.5 | -8.47 | -1.08 | -19.25 | 457 |
| 29 | Z-score reversion · 1h | reversion | 95.44 | -4.56 | 52 | 44.2 | 2.84 | 0.69 | -8.60 | 158 |
| 30 | EMA 20/50 cross · 1h | trend | 95.36 | -4.64 | 45 | 15.6 | 10.05 | 1.28 | -20.35 | 137 |
| 31 | Max aggression: 1-day momentum | meta | 95.34 | -4.66 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -9.18 | -5.23 | -9.18 | 235 |
| 33 | Supertrend · 1h | trend | 94.00 | -6.00 | 60 | 13.3 | 2.25 | 0.48 | -20.32 | 213 |
| 34 | Squeeze breakout · 1h | breakout | 93.94 | -6.06 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.66 | -6.34 | 90 | 22.2 | 1.76 | 0.41 | -22.79 | 288 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -3.19 | -1.02 | -5.84 | 114 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.62 | 2.18 | -6.70 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.61 | -7.39 | 66 | 15.2 | 1.21 | 0.35 | -25.56 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.52 | -7.48 | 165 | 31.5 | -8.80 | -1.38 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 92.01 | -7.99 | 127 | 42.5 | -19.97 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.49 | -8.51 | 38 | 34.2 | 6.03 | 1.38 | -9.40 | 127 |
| 42 | Ichimoku · 1h | trend | 91.29 | -8.71 | 48 | 16.7 | 2.06 | 0.44 | -22.34 | 124 |
| 43 | Agent (ML meta-label) | meta | 91.05 | -8.95 | 485 | 18.1 | 3.66 | 0.76 | -11.97 | 378 |
| 44 | Triple EMA stack · 1h | trend | 90.72 | -9.28 | 71 | 15.5 | -7.21 | -0.54 | -32.27 | 239 |
| 45 | Volume breakout · 1h | breakout | 90.67 | -9.33 | 75 | 22.7 | 8.60 | 1.31 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 90.67 | -9.33 | 77 | 28.6 | 7.26 | 1.07 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 90.00 | -10.00 | 97 | 37.1 | -23.78 | -5.71 | -24.98 | 321 |
| 48 | Williams %R · 1h | reversion | 89.41 | -10.59 | 143 | 45.5 | -28.17 | -4.78 | -29.70 | 511 |
| 49 | CCI reversion · 1h | reversion | 88.98 | -11.02 | 119 | 45.4 | -9.82 | -1.28 | -14.42 | 417 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.51 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.10 | -11.90 | 158 | 18.4 | -9.59 | -0.80 | -33.87 | 321 |
| 52 | MACD zero-line · 1h | trend | 87.50 | -12.50 | 69 | 17.4 | -22.18 | -4.31 | -22.71 | 230 |
| 53 | VWAP momentum · 1h | momentum | 87.31 | -12.69 | 333 | 22.8 | -33.54 | -4.98 | -40.76 | 1255 |
| 54 | Donchian 20/10 · 1h | breakout | 86.98 | -13.02 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 86.75 | -13.25 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 86.68 | -13.32 | 49 | 20.4 | -8.31 | -0.89 | -26.76 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 86.68 | -13.32 | 110 | 12.7 | -10.37 | -1.31 | -24.20 | 330 |
| 58 | Heikin-Ashi · 1h | trend | 86.56 | -13.44 | 166 | 26.5 | -29.46 | -4.81 | -38.65 | 673 |
| 59 | Candlestick reversal · 1h | reversion | 86.47 | -13.53 | 142 | 31.0 | -30.37 | -5.84 | -30.90 | 478 |
| 60 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.83 | 698 |
| 61 | Three white soldiers | momentum | 85.93 | -14.07 | 167 | 18.0 | -47.73 | -22.11 | -47.78 | 584 |
| 62 | ROC + volume · 1h | momentum | 85.31 | -14.69 | 173 | 20.2 | -8.96 | -1.02 | -24.87 | 399 |
| 63 | ROC + volume | momentum | 69.96 | -30.04 | 463 | 22.0 | -73.46 | -16.51 | -75.51 | 1673 |
| 64 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.30 | -16.70 | -73.68 | 1473 |
| 65 | Volume breakout | breakout | 67.00 | -33.00 | 301 | 14.0 | -62.12 | -17.42 | -62.40 | 892 |
| 66 | Squeeze breakout | breakout | 66.91 | -33.09 | 384 | 15.1 | -62.59 | -17.96 | -62.80 | 1222 |
| 67 | EMA 20/50 cross | trend | 64.68 | -35.32 | 399 | 19.8 | -76.86 | -15.09 | -77.17 | 1445 |
| 68 | Donchian 55/20 | breakout | 63.13 | -36.87 | 395 | 16.7 | -69.40 | -14.54 | -70.80 | 1288 |
| 69 | VWAP reversion | reversion | 62.53 | -37.47 | 488 | 25.4 | -72.14 | -15.06 | -72.16 | 1396 |
| 70 | AI bee: Boozy | ai | 59.77 | -40.23 | 271 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 57.96 | -42.04 | 556 | 19.4 | -85.86 | -20.37 | -85.86 | 1914 |
| 72 | Keltner breakout | breakout | 57.50 | -42.50 | 540 | 14.3 | -83.27 | -26.82 | -83.27 | 1848 |
| 73 | Ichimoku | trend | 54.01 | -45.99 | 482 | 9.5 | -82.37 | -22.82 | -82.37 | 1723 |
| 74 | AI bee: Bizzy | ai | 52.97 | -47.03 | 962 | 8.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 52.81 | -47.19 | 675 | 20.1 | -87.77 | -26.85 | -87.78 | 2111 |
| 76 | Z-score reversion | reversion | 52.30 | -47.70 | 625 | 23.0 | -85.93 | -21.68 | -85.95 | 2080 |
| 77 | ADX DI cross | trend | 51.01 | -48.99 | 654 | 10.4 | -89.24 | -33.33 | -89.24 | 2115 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.50 | -28.99 | -98.50 | 5309 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -29.59 | -93.46 | 2617 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.48 | -24.68 | -90.48 | 2375 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.72 | -26.46 | -91.72 | 2359 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -31.84 | -97.36 | 3535 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.54 | -35.05 | -96.54 | 3605 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.53 | -25.31 | -94.53 | 2643 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.03 | -99.36 | 5641 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.93 | -25.46 | -90.94 | 2634 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -30.51 | -96.39 | 3602 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.64 | -99.72 | 6160 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.58 | -29.25 | -91.58 | 2364 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.42 | -36.47 | -97.42 | 3678 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -34.94 | -98.51 | 4674 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.40 | -31.77 | -93.40 | 2800 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.65 | -99.54 | 6122 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -31.40 | -95.95 | 3735 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.66 | -32.94 | -95.66 | 4047 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.70 | -99.89 | 8210 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-14T08:25 | Donchian 55/20 | sell | SOL-USD | 15.77 | -0.17 | stop-loss |
| 2026-10-14T08:25 | Donchian 55/20 | sell | ETH-USD | 12.64 | -0.13 | stop-loss |
| 2026-10-14T08:25 | Donchian 55/20 | sell | DOGE-USD | 12.62 | -0.14 | stop-loss |
| 2026-10-14T08:25 | ROC + volume | sell | XRP-USD | 14.00 | -0.15 | stop-loss |
| 2026-10-14T08:25 | ROC + volume | sell | SOL-USD | 17.48 | -0.19 | stop-loss |
| 2026-10-14T08:25 | ROC + volume | sell | ETH-USD | 14.00 | -0.14 | stop-loss |
| 2026-10-14T08:25 | ROC + volume | sell | DOGE-USD | 13.99 | -0.16 | stop-loss |
| 2026-10-14T08:25 | EMA 20/50 cross | sell | SOL-USD | 16.17 | -0.18 | stop-loss |
| 2026-10-14T08:25 | EMA 20/50 cross | sell | ETH-USD | 16.18 | -0.16 | stop-loss |
| 2026-10-14T08:25 | EMA 20/50 cross | sell | DOGE-USD | 16.16 | -0.17 | stop-loss |
| 2026-10-14T08:20 | AI bee: Bizzy | sell | XRP-USD | 7.79 | -0.03 | Jev: sell (sell p=0.59) after 15 min |
| 2026-10-14T08:20 | Squeeze breakout | sell | BTC-USD | 16.74 | -0.09 | stop-loss |
| 2026-10-14T08:20 | Keltner breakout | buy | SOL-USD | 2.92 | — | rebalance up |
| 2026-10-14T08:20 | Keltner breakout | buy | DOGE-USD | 2.90 | — | rebalance up |
| 2026-10-14T08:20 | Keltner breakout | sell | BTC-USD | 11.54 | -0.06 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 08:55:05.000158+00:00 -> 2026-10-14 09:05:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
