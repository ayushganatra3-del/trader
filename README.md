# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T09:55:05.000149+00:00 · 23479 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.10 (-6.91%)

Closed trades 72, win rate 41.7%, fees £2.56, max drawdown -7.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-14 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 7335 decisions in 1467 calls, $0.1028 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T09:55 | 0 / 5 / 0 | TNA 15% |  |
| Breezy | 2026-10-15T09:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-15T09:55 | 1 / 4 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| ROC + volume | META | 1.74 | +2.50% | 3 |
| MFI reversion | AAPL | 1.54 | +0.60% | 4 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Triple EMA stack | NVDA | 1.50 | +0.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.31 | 4.31 | 0 | — | 4.16 | 1.99 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.49 | 2.69 | -3.27 | 19 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.45 | -0.74 | -9.84 | 26 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.05 | 1.05 | 13 | 38.5 | 2.90 | 0.97 | -7.55 | 43 |
| 6 | VWAP reversion · 1h | reversion | 100.74 | 0.74 | 46 | 39.1 | -8.86 | -2.64 | -13.79 | 125 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.33 | 0.33 | 0 | — | 4.04 | 1.58 | -5.18 | 1 |
| 8 | Copy: Insider buying | copy | 100.16 | 0.15 | 20 | 45.0 | -16.02 | -2.54 | -21.97 | 76 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Hold SPY | benchmark | 99.95 | -0.05 | 0 | — | -0.98 | -0.53 | -3.44 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.28 | -3.79 | -3.91 | 21 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.61 | -1.39 | 0 | — | -1.10 | -0.42 | -3.75 | 1 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 98.42 | -1.58 | 48 | 33.3 | 1.68 | 1.01 | -2.07 | 67 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 98.40 | -1.60 | 0 | — | -5.15 | -2.02 | -6.99 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 98.33 | -1.67 | 0 | — | -4.93 | -2.74 | -5.36 | 1 |
| 17 | Donchian 55/20 · 1h | breakout | 96.99 | -3.02 | 36 | 16.7 | 5.91 | 0.86 | -22.11 | 114 |
| 18 | Hold BTC | benchmark | 96.89 | -3.11 | 0 | — | 28.98 | 3.35 | -8.68 | 1 |
| 19 | Trend pullback · 1h | trend | 96.85 | -3.15 | 86 | 24.4 | -24.03 | -6.88 | -24.88 | 168 |
| 20 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.60 | -0.55 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.53 | -3.47 | 10 | 0.0 | -3.93 | -2.98 | -5.08 | 30 |
| 22 | Agent (rotation) | meta | 96.14 | -3.86 | 93 | 30.1 | -12.50 | -4.58 | -13.57 | 277 |
| 23 | ADX DI cross · 1h | trend | 95.68 | -4.32 | 70 | 21.4 | -10.60 | -1.93 | -14.52 | 251 |
| 24 | Daily: Bullish score | daily | 94.67 | -5.33 | 5 | 0.0 | -2.87 | -0.17 | -12.76 | 12 |
| 25 | Max aggression: 1-day momentum | meta | 94.58 | -5.42 | 13 | 38.5 | -9.94 | -0.18 | -37.31 | 42 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 94.51 | -5.49 | 0 | — | -15.33 | -2.92 | -16.54 | 1 |
| 27 | Gap and go | momentum | 93.89 | -6.11 | 63 | 12.7 | 9.60 | 2.41 | -6.73 | 199 |
| 28 | EMA 20/50 cross · 1h | trend | 93.79 | -6.21 | 48 | 16.7 | 0.88 | 0.31 | -23.87 | 132 |
| 29 | Parabolic SAR · 1h | trend | 93.77 | -6.23 | 93 | 22.6 | 0.58 | 0.27 | -23.42 | 287 |
| 30 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.62 | 1.01 | -9.46 | 104 |
| 31 | MACD cross · 1h | trend | 93.24 | -6.76 | 149 | 22.8 | -12.38 | -1.68 | -21.42 | 458 |
| 32 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -7.58 | -2.72 | -11.15 | 242 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 92.76 | -7.24 | 0 | — | 3.87 | 0.74 | -11.29 | 1 |
| 34 | Max aggression: 5-day momentum | meta | 91.90 | -8.10 | 8 | 37.5 | -6.02 | -0.21 | -34.64 | 27 |
| 35 | Bollinger breakout · 1h | breakout | 91.79 | -8.21 | 78 | 29.5 | 7.86 | 1.16 | -14.21 | 276 |
| 36 | RSI momentum · 1h | momentum | 91.68 | -8.32 | 73 | 17.8 | 0.78 | 0.30 | -25.52 | 225 |
| 37 | Supertrend · 1h | trend | 91.49 | -8.51 | 73 | 13.7 | 1.72 | 0.41 | -23.21 | 207 |
| 38 | Stochastic reversion · 1h | reversion | 91.26 | -8.74 | 119 | 47.1 | -17.26 | -3.23 | -17.97 | 358 |
| 39 | Volume breakout · 1h | breakout | 90.83 | -9.17 | 77 | 22.1 | 7.66 | 1.21 | -12.60 | 121 |
| 40 | Ichimoku · 1h | trend | 90.39 | -9.61 | 51 | 15.7 | -0.36 | 0.17 | -23.46 | 125 |
| 41 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -8.21 | -2.67 | -10.58 | 120 |
| 42 | Triple EMA stack · 1h | trend | 90.22 | -9.78 | 77 | 16.9 | -11.30 | -1.02 | -34.69 | 238 |
| 43 | Connors RSI(2) · 1h | reversion | 89.37 | -10.63 | 137 | 40.1 | -23.31 | -6.98 | -24.82 | 248 |
| 44 | Opening range 30m | breakout | 89.19 | -10.81 | 168 | 23.2 | -13.51 | -4.00 | -17.60 | 556 |
| 45 | Z-score reversion · 1h | reversion | 88.81 | -11.19 | 65 | 35.4 | -9.41 | -1.71 | -14.33 | 168 |
| 46 | MFI reversion · 1h | reversion | 88.32 | -11.68 | 180 | 29.4 | -17.77 | -3.13 | -18.57 | 137 |
| 47 | OBV trend · 1h | momentum | 88.01 | -11.98 | 164 | 18.9 | -10.96 | -0.95 | -35.00 | 320 |
| 48 | Keltner breakout · 1h | breakout | 87.52 | -12.48 | 51 | 21.6 | -7.59 | -0.80 | -26.76 | 216 |
| 49 | Agent (ML meta-label) | meta | 87.44 | -12.56 | 540 | 18.1 | -6.58 | -0.97 | -15.53 | 384 |
| 50 | MACD zero-line · 1h | trend | 87.23 | -12.77 | 74 | 16.2 | -22.58 | -4.35 | -23.07 | 223 |
| 51 | Donchian 20/10 · 1h | breakout | 86.53 | -13.47 | 71 | 19.7 | -0.72 | 0.11 | -20.38 | 216 |
| 52 | ROC + volume · 1h | momentum | 85.64 | -14.36 | 179 | 21.2 | -11.73 | -1.59 | -25.35 | 396 |
| 53 | Heikin-Ashi · 1h | trend | 85.58 | -14.42 | 169 | 26.0 | -31.37 | -5.13 | -39.47 | 663 |
| 54 | VWAP momentum · 1h | momentum | 85.39 | -14.61 | 348 | 21.8 | -37.00 | -5.57 | -42.67 | 1244 |
| 55 | RSI(14) reversion · 1h | reversion | 85.27 | -14.73 | 53 | 24.5 | -4.64 | -0.64 | -15.77 | 155 |
| 56 | EMA 9/21 cross · 1h | trend | 85.03 | -14.97 | 120 | 12.5 | -9.56 | -1.08 | -26.92 | 321 |
| 57 | Opening range 15m | breakout | 84.93 | -15.07 | 214 | 20.6 | -18.22 | -4.91 | -21.41 | 692 |
| 58 | Bollinger reversion · 1h | reversion | 84.62 | -15.38 | 110 | 32.7 | -25.96 | -5.47 | -28.77 | 331 |
| 59 | Three white soldiers | momentum | 84.01 | -15.99 | 184 | 16.3 | -48.84 | -21.86 | -48.84 | 593 |
| 60 | CCI reversion · 1h | reversion | 83.59 | -16.41 | 132 | 41.7 | -17.34 | -2.28 | -21.76 | 419 |
| 61 | Williams %R · 1h | reversion | 82.21 | -17.79 | 158 | 42.4 | -32.97 | -5.44 | -34.41 | 507 |
| 62 | Candlestick reversal · 1h | reversion | 80.95 | -19.05 | 168 | 26.2 | -31.50 | -5.81 | -31.52 | 516 |
| 63 | ROC + volume | momentum | 66.48 | -33.52 | 488 | 21.3 | -74.56 | -16.58 | -76.64 | 1673 |
| 64 | Volume breakout | breakout | 65.76 | -34.24 | 308 | 13.6 | -63.16 | -17.69 | -63.16 | 886 |
| 65 | RSI(14) reversion | reversion | 65.56 | -34.44 | 547 | 26.9 | -73.98 | -16.81 | -74.25 | 1556 |
| 66 | Squeeze breakout | breakout | 64.64 | -35.36 | 401 | 14.7 | -63.22 | -17.73 | -63.25 | 1211 |
| 67 | Donchian 55/20 | breakout | 63.25 | -36.75 | 398 | 16.8 | -68.94 | -14.31 | -70.95 | 1269 |
| 68 | EMA 20/50 cross | trend | 61.84 | -38.16 | 414 | 19.1 | -77.34 | -15.07 | -78.17 | 1434 |
| 69 | VWAP reversion | reversion | 58.61 | -41.39 | 574 | 24.2 | -72.47 | -14.96 | -72.77 | 1438 |
| 70 | AI bee: Boozy | ai | 57.58 | -42.42 | 273 | 4.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 55.80 | -44.20 | 554 | 14.1 | -83.38 | -26.28 | -83.41 | 1827 |
| 72 | Supertrend | trend | 54.66 | -45.34 | 574 | 18.8 | -86.40 | -19.97 | -86.47 | 1894 |
| 73 | Ichimoku | trend | 53.88 | -46.12 | 489 | 9.8 | -81.92 | -22.24 | -81.92 | 1703 |
| 74 | AI bee: Bizzy | ai | 51.35 | -48.66 | 1000 | 8.2 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.11 | -98.64 | 5310 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -29.17 | -93.48 | 2571 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.59 | -24.07 | -90.61 | 2341 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.64 | -25.98 | -91.67 | 2337 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.48 | -31.73 | -97.48 | 3511 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.56 | -34.52 | -96.56 | 3562 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.38 | -24.39 | -94.39 | 2623 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -35.27 | -99.40 | 5748 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.13 | -24.98 | -91.14 | 2615 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.30 | -30.10 | -96.30 | 3563 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.19 | -99.73 | 6148 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.98 | -29.00 | -91.98 | 2353 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -36.57 | -97.45 | 3642 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.84 | -98.53 | 4684 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.53 | -31.61 | -93.53 | 2779 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -38.11 | -99.55 | 6152 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.20 | -21.94 | -86.29 | 2095 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.75 | -26.64 | -87.83 | 2126 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.02 | -31.94 | -96.03 | 3758 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.56 | -33.48 | -89.56 | 2100 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.79 | -32.91 | -95.81 | 4072 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.40 | -99.89 | 8198 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T09:30 | MFI reversion · 1h | buy | ETH-USD | 6.51 | — | rebalance up |
| 2026-10-15T09:30 | MFI reversion · 1h | sell | SOL-USD | 6.51 | -0.01 | rebalance down |
| 2026-10-15T09:25 | ROC + volume | sell | SOL-USD | 16.56 | -0.13 | exit signal |
| 2026-10-15T09:20 | Volume breakout | sell | SOL-USD | 16.34 | -0.13 | exit signal |
| 2026-10-15T09:20 | Keltner breakout | sell | SOL-USD | 13.88 | -0.13 | exit signal |
| 2026-10-15T09:20 | EMA 20/50 cross | buy | ETH-USD | 3.19 | — | entry |
| 2026-10-15T09:20 | EMA 20/50 cross | sell | XRP-USD | 3.09 | -0.01 | rebalance down |
| 2026-10-15T09:00 | Three white soldiers · 1h | buy | XRP-USD | 24.16 | — | entry signal |
| 2026-10-15T09:00 | VWAP momentum · 1h | buy | XRP-USD | 10.40 | — | rebalance up |
| 2026-10-15T09:00 | VWAP momentum · 1h | sell | ETH-USD | 14.19 | -0.12 | exit signal |
| 2026-10-15T09:00 | MACD cross · 1h | buy | BTC-USD | 23.35 | — | entry signal |
| 2026-10-15T08:39 | AI bee: Bizzy | sell | XRP-USD | 8.06 | -0.04 | Jev: sell (sell p=0.51) after 12 min |
| 2026-10-15T08:37 | AI bee: Bizzy | sell | SOL-USD | 7.30 | -0.05 | Jev: sell (sell p=0.61) after 10 min |
| 2026-10-15T08:35 | Squeeze breakout | buy | XRP-USD | 16.17 | — | entry signal |
| 2026-10-15T08:30 | EMA 20/50 cross | buy | XRP-USD | 15.48 | — | entry signal |
| 2026-10-15T08:26 | AI bee: Bizzy | buy | XRP-USD | 8.10 | — | Jev: buy (buy p=0.63) |
| 2026-10-15T08:26 | AI bee: Bizzy | buy | SOL-USD | 7.34 | — | Jev: buy (buy p=0.57) |
| 2026-10-15T08:25 | Keltner breakout | sell | BTC-USD | 13.89 | -0.12 | stop-loss |
| 2026-10-15T08:25 | ROC + volume | sell | BTC-USD | 16.52 | -0.17 | stop-loss |
| 2026-10-15T08:25 | EMA 20/50 cross | buy | SOL-USD | 15.50 | — | entry signal |
| 2026-10-15T08:25 | EMA 20/50 cross | buy | DOGE-USD | 15.50 | — | entry signal |
| 2026-10-15T08:05 | Supertrend | buy | SOL-USD | 2.73 | — | rebalance up |
| 2026-10-15T08:05 | Supertrend | sell | XRP-USD | 2.73 | -0.01 | rebalance down |
| 2026-10-15T08:00 | AI bee: Boozy | sell | ETH-USD | 13.29 | -0.07 | Jev: add (buy p=0.56) |
| 2026-10-15T08:00 | Z-score reversion · 1h | buy | ETH-USD | 3.17 | — | entry signal |
| 2026-10-15T08:00 | Z-score reversion · 1h | buy | DOGE-USD | 11.13 | — | entry signal |
| 2026-10-15T08:00 | Candlestick reversal · 1h | buy | SOL-USD | 4.27 | — | entry signal |
| 2026-10-15T08:00 | Candlestick reversal · 1h | buy | ETH-USD | 4.27 | — | entry signal |
| 2026-10-15T08:00 | Candlestick reversal · 1h | buy | BTC-USD | 4.27 | — | entry signal |
| 2026-10-15T08:00 | VWAP momentum · 1h | buy | XRP-USD | 6.72 | — | entry signal |
| 2026-10-15T08:00 | VWAP momentum · 1h | buy | SOL-USD | 14.31 | — | entry signal |
| 2026-10-15T08:00 | VWAP momentum · 1h | buy | ETH-USD | 14.31 | — | entry signal |
| 2026-10-15T08:00 | VWAP momentum · 1h | buy | DOGE-USD | 14.31 | — | entry signal |
| 2026-10-15T08:00 | VWAP momentum · 1h | buy | BTC-USD | 14.31 | — | entry signal |
| 2026-10-15T08:00 | Keltner breakout | buy | SOL-USD | 14.01 | — | entry signal |
| 2026-10-15T08:00 | ROC + volume | buy | BTC-USD | 16.69 | — | entry signal |
| 2026-10-15T07:55 | VWAP reversion | sell | SOL-USD | 14.68 | 0.12 | exit signal |
| 2026-10-15T07:55 | Volume breakout | buy | SOL-USD | 16.47 | — | entry signal |
| 2026-10-15T07:55 | ROC + volume | buy | SOL-USD | 16.69 | — | entry signal |
| 2026-10-15T07:55 | EMA 20/50 cross | buy | BTC-USD | 15.53 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 09:55:05.000149+00:00 -> 2026-10-15 10:05:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
