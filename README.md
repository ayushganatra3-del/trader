# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T11:55:05.000193+00:00 · 23580 ticks

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

Today: 8850 decisions in 1770 calls, $0.1241 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T11:55 | 0 / 3 / 2 | TNA 15% |  |
| Breezy | 2026-10-15T11:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-15T11:55 | 0 / 5 / 0 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.39 | 4.39 | 0 | — | 4.16 | 1.99 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.49 | 2.69 | -3.27 | 19 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.45 | -0.74 | -9.84 | 26 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.05 | 1.05 | 13 | 38.5 | 2.90 | 0.97 | -7.55 | 43 |
| 6 | VWAP reversion · 1h | reversion | 100.81 | 0.81 | 46 | 39.1 | -8.86 | -2.64 | -13.79 | 125 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.40 | 0.40 | 0 | — | 4.04 | 1.58 | -5.18 | 1 |
| 8 | Copy: Insider buying | copy | 100.22 | 0.22 | 20 | 45.0 | -16.02 | -2.54 | -21.97 | 76 |
| 9 | Hold SPY | benchmark | 100.02 | 0.02 | 0 | — | -0.98 | -0.53 | -3.44 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.28 | -3.79 | -3.91 | 21 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.68 | -1.32 | 0 | — | -1.10 | -0.42 | -3.75 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 98.47 | -1.53 | 0 | — | -5.15 | -2.02 | -6.99 | 1 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 98.42 | -1.58 | 48 | 33.3 | 1.68 | 1.01 | -2.07 | 67 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 98.38 | -1.62 | 0 | — | -4.93 | -2.74 | -5.36 | 1 |
| 17 | Donchian 55/20 · 1h | breakout | 97.00 | -3.00 | 36 | 16.7 | 6.39 | 0.91 | -22.11 | 112 |
| 18 | Trend pullback · 1h | trend | 96.87 | -3.13 | 86 | 24.4 | -24.26 | -6.92 | -24.77 | 168 |
| 19 | Hold BTC | benchmark | 96.71 | -3.29 | 0 | — | 28.83 | 3.34 | -8.68 | 1 |
| 20 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.60 | -0.55 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.18 | -3.16 | -5.30 | 30 |
| 22 | Agent (rotation) | meta | 96.16 | -3.84 | 93 | 30.1 | -14.02 | -5.12 | -15.36 | 275 |
| 23 | ADX DI cross · 1h | trend | 95.71 | -4.29 | 70 | 21.4 | -10.51 | -1.91 | -14.52 | 251 |
| 24 | Daily: Bullish score | daily | 94.74 | -5.26 | 5 | 0.0 | -2.87 | -0.17 | -12.76 | 12 |
| 25 | Max aggression: 1-day momentum | meta | 94.65 | -5.35 | 13 | 38.5 | -9.94 | -0.18 | -37.31 | 42 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 94.56 | -5.44 | 0 | — | -15.33 | -2.92 | -16.54 | 1 |
| 27 | Gap and go | momentum | 93.89 | -6.11 | 63 | 12.7 | 9.60 | 2.41 | -6.73 | 199 |
| 28 | EMA 20/50 cross · 1h | trend | 93.85 | -6.15 | 48 | 16.7 | 7.43 | 0.97 | -24.53 | 133 |
| 29 | Parabolic SAR · 1h | trend | 93.79 | -6.21 | 93 | 22.6 | 0.59 | 0.27 | -23.42 | 287 |
| 30 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.62 | 1.01 | -9.46 | 104 |
| 31 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -6.44 | -2.27 | -10.02 | 243 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 92.83 | -7.17 | 0 | — | 3.87 | 0.74 | -11.29 | 1 |
| 33 | MACD cross · 1h | trend | 92.66 | -7.34 | 149 | 22.8 | -12.54 | -1.70 | -22.03 | 459 |
| 34 | Max aggression: 5-day momentum | meta | 91.97 | -8.03 | 8 | 37.5 | -6.02 | -0.21 | -34.64 | 27 |
| 35 | Bollinger breakout · 1h | breakout | 91.80 | -8.20 | 78 | 29.5 | 7.86 | 1.16 | -14.21 | 276 |
| 36 | RSI momentum · 1h | momentum | 91.71 | -8.29 | 73 | 17.8 | 0.77 | 0.30 | -25.52 | 225 |
| 37 | Supertrend · 1h | trend | 91.54 | -8.46 | 73 | 13.7 | 1.72 | 0.41 | -23.21 | 207 |
| 38 | Stochastic reversion · 1h | reversion | 91.31 | -8.69 | 119 | 47.1 | -17.26 | -3.23 | -17.97 | 358 |
| 39 | Volume breakout · 1h | breakout | 90.85 | -9.15 | 77 | 22.1 | 7.66 | 1.21 | -12.60 | 121 |
| 40 | Ichimoku · 1h | trend | 90.41 | -9.59 | 51 | 15.7 | -0.36 | 0.17 | -23.46 | 125 |
| 41 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -8.21 | -2.67 | -10.58 | 120 |
| 42 | Triple EMA stack · 1h | trend | 90.23 | -9.77 | 77 | 16.9 | -11.32 | -1.02 | -34.69 | 238 |
| 43 | Connors RSI(2) · 1h | reversion | 89.42 | -10.57 | 137 | 40.1 | -23.31 | -6.98 | -24.82 | 248 |
| 44 | Opening range 30m | breakout | 89.19 | -10.81 | 168 | 23.2 | -13.51 | -4.00 | -17.60 | 556 |
| 45 | Z-score reversion · 1h | reversion | 88.67 | -11.33 | 65 | 35.4 | -9.59 | -1.74 | -14.33 | 168 |
| 46 | MFI reversion · 1h | reversion | 88.31 | -11.69 | 180 | 29.4 | -17.87 | -3.14 | -18.57 | 136 |
| 47 | OBV trend · 1h | momentum | 88.04 | -11.96 | 164 | 18.9 | -10.96 | -0.95 | -35.00 | 320 |
| 48 | Keltner breakout · 1h | breakout | 87.54 | -12.46 | 51 | 21.6 | -7.59 | -0.80 | -26.76 | 216 |
| 49 | Agent (ML meta-label) | meta | 87.45 | -12.55 | 540 | 18.1 | -8.52 | -1.36 | -15.56 | 391 |
| 50 | MACD zero-line · 1h | trend | 87.24 | -12.76 | 74 | 16.2 | -22.58 | -4.35 | -23.07 | 223 |
| 51 | Donchian 20/10 · 1h | breakout | 86.55 | -13.45 | 71 | 19.7 | -0.72 | 0.11 | -20.38 | 216 |
| 52 | ROC + volume · 1h | momentum | 85.65 | -14.35 | 179 | 21.2 | -11.73 | -1.59 | -25.35 | 396 |
| 53 | Heikin-Ashi · 1h | trend | 85.59 | -14.41 | 169 | 26.0 | -31.37 | -5.13 | -39.47 | 663 |
| 54 | RSI(14) reversion · 1h | reversion | 85.17 | -14.83 | 53 | 24.5 | -4.77 | -0.66 | -15.77 | 157 |
| 55 | VWAP momentum · 1h | momentum | 85.06 | -14.94 | 351 | 21.7 | -37.03 | -5.58 | -42.94 | 1240 |
| 56 | EMA 9/21 cross · 1h | trend | 85.05 | -14.95 | 120 | 12.5 | -9.56 | -1.08 | -26.92 | 321 |
| 57 | Opening range 15m | breakout | 84.93 | -15.07 | 214 | 20.6 | -18.22 | -4.91 | -21.41 | 692 |
| 58 | Bollinger reversion · 1h | reversion | 84.63 | -15.37 | 110 | 32.7 | -26.01 | -5.49 | -28.77 | 331 |
| 59 | Three white soldiers | momentum | 84.01 | -15.99 | 184 | 16.3 | -48.84 | -21.86 | -48.84 | 593 |
| 60 | CCI reversion · 1h | reversion | 83.57 | -16.43 | 132 | 41.7 | -17.50 | -2.30 | -21.76 | 419 |
| 61 | Williams %R · 1h | reversion | 82.15 | -17.85 | 158 | 42.4 | -33.12 | -5.46 | -34.41 | 507 |
| 62 | Candlestick reversal · 1h | reversion | 80.88 | -19.12 | 171 | 25.7 | -31.77 | -5.86 | -31.80 | 520 |
| 63 | ROC + volume | momentum | 66.48 | -33.52 | 488 | 21.3 | -74.56 | -16.58 | -76.64 | 1673 |
| 64 | Volume breakout | breakout | 65.76 | -34.24 | 308 | 13.6 | -63.16 | -17.69 | -63.16 | 886 |
| 65 | RSI(14) reversion | reversion | 65.58 | -34.42 | 548 | 27.0 | -73.87 | -16.76 | -74.15 | 1555 |
| 66 | Squeeze breakout | breakout | 64.57 | -35.44 | 402 | 14.7 | -63.11 | -17.66 | -63.27 | 1208 |
| 67 | Donchian 55/20 | breakout | 63.25 | -36.75 | 398 | 16.8 | -68.85 | -14.27 | -70.95 | 1267 |
| 68 | EMA 20/50 cross | trend | 61.20 | -38.80 | 419 | 18.9 | -77.33 | -15.04 | -78.38 | 1430 |
| 69 | VWAP reversion | reversion | 58.61 | -41.39 | 574 | 24.2 | -72.29 | -14.85 | -72.60 | 1435 |
| 70 | AI bee: Boozy | ai | 57.58 | -42.42 | 273 | 4.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 55.80 | -44.20 | 554 | 14.1 | -83.37 | -26.25 | -83.41 | 1827 |
| 72 | Supertrend | trend | 54.03 | -45.97 | 580 | 18.6 | -86.55 | -20.07 | -86.58 | 1895 |
| 73 | Ichimoku | trend | 53.88 | -46.12 | 489 | 9.8 | -81.79 | -22.04 | -81.85 | 1700 |
| 74 | AI bee: Bizzy | ai | 51.20 | -48.80 | 1003 | 8.2 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -28.79 | -98.62 | 5300 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -29.31 | -93.51 | 2572 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.63 | -24.10 | -90.65 | 2339 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.61 | -25.97 | -91.64 | 2335 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -31.57 | -97.47 | 3506 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.58 | -34.62 | -96.58 | 3562 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -24.48 | -94.40 | 2625 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -35.21 | -99.40 | 5743 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.14 | -24.97 | -91.17 | 2614 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.26 | -30.09 | -96.26 | 3557 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.06 | -99.72 | 6146 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.95 | -28.93 | -91.96 | 2352 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.43 | -36.38 | -97.44 | 3637 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -35.69 | -98.52 | 4682 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.50 | -31.42 | -93.50 | 2776 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -38.14 | -99.55 | 6151 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.17 | -21.90 | -86.28 | 2092 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.75 | -26.66 | -87.82 | 2128 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.98 | -31.78 | -95.98 | 3753 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.58 | -33.54 | -89.58 | 2102 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.82 | -32.92 | -95.83 | 4077 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.47 | -99.89 | 8200 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T11:50 | AI bee: Bizzy | sell | DOGE-USD | 7.58 | -0.05 | Jev: sell (sell p=0.63) after 10 min |
| 2026-10-15T11:43 | AI bee: Bizzy | sell | XRP-USD | 7.32 | -0.04 | Jev: sell (sell p=0.55) after 11 min |
| 2026-10-15T11:40 | AI bee: Bizzy | buy | DOGE-USD | 7.63 | — | Jev: buy (buy p=0.60) |
| 2026-10-15T11:40 | RSI(14) reversion | sell | SOL-USD | 16.41 | 0.02 | exit signal |
| 2026-10-15T11:40 | Supertrend | buy | DOGE-USD | 13.52 | — | entry signal |
| 2026-10-15T11:36 | Supertrend | sell | DOGE-USD | 13.45 | -0.09 | target is flat |
| 2026-10-15T11:32 | AI bee: Bizzy | buy | XRP-USD | 7.36 | — | Jev: buy (buy p=0.57) |
| 2026-10-15T11:30 | Supertrend | buy | DOGE-USD | 13.54 | — | entry signal |
| 2026-10-15T11:16 | Ichimoku | buy | DOGE-USD | 13.47 | — | entry signal |
| 2026-10-15T11:16 | EMA 20/50 cross | buy | DOGE-USD | 15.30 | — | entry signal |
| 2026-10-15T11:00 | Three white soldiers · 1h | sell | XRP-USD | 23.81 | -0.35 | exit signal |
| 2026-10-15T11:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.49 | — | entry signal |
| 2026-10-15T11:00 | Candlestick reversal · 1h | sell | XRP-USD | 4.43 | -0.06 | exit signal |
| 2026-10-15T11:00 | Candlestick reversal · 1h | sell | ETH-USD | 4.22 | -0.05 | exit signal |
| 2026-10-15T11:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.04 | — | rebalance up |
| 2026-10-15T11:00 | VWAP momentum · 1h | sell | XRP-USD | 16.90 | -0.23 | exit signal |
| 2026-10-15T11:00 | VWAP momentum · 1h | sell | SOL-USD | 14.08 | -0.23 | exit signal |
| 2026-10-15T11:00 | VWAP momentum · 1h | sell | BTC-USD | 14.12 | -0.19 | exit signal |
| 2026-10-15T11:00 | MACD cross · 1h | buy | ETH-USD | 7.23 | — | entry signal |
| 2026-10-15T11:00 | MACD cross · 1h | buy | DOGE-USD | 15.44 | — | entry signal |
| 2026-10-15T11:00 | MACD cross · 1h | sell | XRP-USD | 7.40 | -0.11 | rebalance down |
| 2026-10-15T11:00 | MACD cross · 1h | sell | SOL-USD | 7.59 | -0.11 | rebalance down |
| 2026-10-15T11:00 | MACD cross · 1h | sell | BTC-USD | 7.68 | -0.09 | rebalance down |
| 2026-10-15T10:45 | EMA 20/50 cross | sell | XRP-USD | 12.21 | -0.17 | stop-loss |
| 2026-10-15T10:44 | AI bee: Bizzy | sell | DOGE-USD | 7.01 | -0.05 | Jev: sell (sell p=0.81) after 10 min |
| 2026-10-15T10:34 | AI bee: Bizzy | buy | DOGE-USD | 7.07 | — | Jev: buy (buy p=0.55) |
| 2026-10-15T10:30 | RSI(14) reversion | buy | SOL-USD | 16.39 | — | entry signal |
| 2026-10-15T10:25 | Supertrend | sell | XRP-USD | 10.86 | -0.09 | exit signal |
| 2026-10-15T10:25 | Supertrend | sell | ETH-USD | 13.54 | -0.13 | exit signal |
| 2026-10-15T10:25 | Supertrend | sell | DOGE-USD | 13.55 | -0.13 | exit signal |
| 2026-10-15T10:25 | Supertrend | sell | BTC-USD | 13.53 | -0.12 | exit signal |
| 2026-10-15T10:25 | EMA 20/50 cross | sell | ETH-USD | 15.28 | -0.14 | stop-loss |
| 2026-10-15T10:15 | EMA 20/50 cross | sell | SOL-USD | 15.28 | -0.22 | stop-loss |
| 2026-10-15T10:15 | EMA 20/50 cross | sell | DOGE-USD | 15.32 | -0.18 | exit signal |
| 2026-10-15T10:10 | Supertrend | buy | ETH-USD | 2.73 | — | rebalance up |
| 2026-10-15T10:10 | Supertrend | buy | DOGE-USD | 2.73 | — | rebalance up |
| 2026-10-15T10:10 | Supertrend | sell | SOL-USD | 8.15 | -0.09 | exit signal |
| 2026-10-15T10:10 | EMA 20/50 cross | buy | ETH-USD | 12.24 | — | rebalance up |
| 2026-10-15T10:10 | EMA 20/50 cross | sell | BTC-USD | 15.34 | -0.19 | stop-loss |
| 2026-10-15T10:05 | Squeeze breakout | sell | XRP-USD | 16.06 | -0.11 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 11:55:05.000193+00:00 -> 2026-10-15 12:05:05.000193+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
