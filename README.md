# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T20:25:05.000144+00:00 · 18293 ticks

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
| Copy: Insider buying | 2026-10-10 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 15427 decisions in 3086 calls, $0.2155 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T20:25 | 1 / 3 / 1 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-10T20:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T20:25 | 1 / 4 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Z-score reversion | TNA | 1.94 | +3.40% | 7 |
| Keltner breakout | LABU | 1.94 | +8.17% | 7 |
| Bollinger reversion | TECL | 1.82 | +2.00% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.79 | -2.38 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -13.59 | -2.18 | -22.02 | 69 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.50 | -0.55 | -37.31 | 43 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.22 | 2.44 | -1.58 | 86 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 18 | Hold BTC | benchmark | 99.25 | -0.75 | 0 | — | 27.11 | 3.25 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -10.80 | -2.10 | -14.73 | 344 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.82 | -3.18 | 38 | 13.2 | 5.98 | 0.87 | -19.85 | 132 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -0.30 | 0.04 | -10.38 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.94 | -0.14 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.67 | -0.19 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.87 | -4.13 | 110 | 24.5 | -15.81 | -2.55 | -17.84 | 469 |
| 34 | Supertrend · 1h | trend | 95.32 | -4.68 | 52 | 13.5 | -0.11 | 0.18 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.01 | -5.99 | 36 | 25.0 | 23.91 | 3.26 | -8.81 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.27 | -1.79 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.62 | -0.47 | -9.03 | 148 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Ichimoku · 1h | trend | 92.95 | -7.05 | 41 | 19.5 | -0.62 | 0.13 | -20.02 | 122 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -1.55 | -0.11 | -13.06 | 406 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.85 | -4.99 | -23.54 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.45 | 0.62 | -17.07 | 224 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 91.74 | -8.26 | 68 | 29.4 | 6.31 | 0.98 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.73 | -8.27 | 120 | 47.5 | -24.44 | -4.22 | -26.91 | 512 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.67 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.23 | -9.77 | 115 | 31.3 | -27.68 | -5.44 | -29.50 | 518 |
| 51 | CCI reversion · 1h | reversion | 89.78 | -10.22 | 100 | 45.0 | -8.60 | -1.11 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.71 | -10.29 | 278 | 22.3 | -34.00 | -5.12 | -39.30 | 1280 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 89.12 | -10.88 | 62 | 19.4 | -6.68 | -0.72 | -19.79 | 242 |
| 55 | Donchian 20/10 · 1h | breakout | 88.83 | -11.17 | 58 | 19.0 | -0.15 | 0.19 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.11 | -1.37 | -28.63 | 317 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.61 | -5.14 | -36.60 | 701 |
| 58 | Three white soldiers | momentum | 88.02 | -11.98 | 136 | 18.4 | -48.02 | -23.43 | -48.02 | 589 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.87 | -12.13 | 101 | 13.9 | -8.93 | -1.00 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.61 | -1.29 | -23.91 | 413 |
| 63 | RSI(14) reversion | reversion | 75.28 | -24.72 | 355 | 28.7 | -72.71 | -18.14 | -72.78 | 1492 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.90 | -16.72 | -73.79 | 1670 |
| 65 | Squeeze breakout | breakout | 71.44 | -28.56 | 322 | 14.9 | -62.54 | -18.43 | -62.54 | 1232 |
| 66 | Donchian 55/20 | breakout | 71.01 | -28.98 | 325 | 18.2 | -67.51 | -14.43 | -67.51 | 1291 |
| 67 | EMA 20/50 cross | trend | 70.93 | -29.07 | 321 | 20.2 | -77.32 | -15.44 | -77.32 | 1462 |
| 68 | Volume breakout | breakout | 70.50 | -29.50 | 258 | 13.2 | -62.97 | -18.33 | -62.97 | 904 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -72.12 | -16.37 | -72.26 | 1442 |
| 70 | Supertrend | trend | 65.26 | -34.74 | 448 | 20.3 | -86.31 | -21.15 | -86.31 | 1918 |
| 71 | Keltner breakout | breakout | 63.45 | -36.55 | 441 | 14.5 | -84.03 | -28.28 | -84.03 | 1854 |
| 72 | Z-score reversion | reversion | 61.19 | -38.81 | 486 | 23.5 | -85.53 | -23.23 | -85.53 | 2084 |
| 73 | Ichimoku | trend | 60.64 | -39.36 | 401 | 9.7 | -81.90 | -23.59 | -81.90 | 1751 |
| 74 | AI bee: Boozy | ai | 60.55 | -39.45 | 253 | 5.1 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.54 | -39.46 | 497 | 21.7 | -87.64 | -28.46 | -87.67 | 2123 |
| 76 | AI bee: Bizzy | ai | 59.14 | -40.86 | 809 | 9.0 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.64 | -42.36 | 530 | 10.4 | -89.52 | -34.34 | -89.52 | 2128 |
| 78 | Donchian 20/10 | breakout | 56.50 | -43.50 | 621 | 18.4 | -90.92 | -26.49 | -90.92 | 2671 |
| 79 | RSI momentum | momentum | 55.75 | -44.25 | 587 | 17.4 | -90.36 | -25.80 | -90.37 | 2384 |
| 80 | Trend pullback ⏸ | trend | 55.45 | -44.55 | 581 | 15.0 | -90.82 | -27.24 | -90.82 | 2328 |
| 81 | MACD zero-line | trend | 55.30 | -44.70 | 568 | 15.1 | -91.62 | -29.92 | -91.62 | 2367 |
| 82 | Triple EMA stack | trend | 54.46 | -45.54 | 612 | 15.7 | -93.20 | -30.58 | -93.21 | 2618 |
| 83 | Bollinger breakout | breakout | 51.94 | -48.06 | 653 | 14.4 | -93.61 | -33.70 | -93.61 | 2823 |
| 84 | Consensus | meta | 50.96 | -49.03 | 611 | 10.0 | -94.21 | -26.11 | -94.21 | 2687 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.74 | -98.69 | 5406 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -33.25 | -97.37 | 3548 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -36.72 | -96.48 | 3613 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.42 | -99.35 | 5699 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.31 | -31.89 | -96.31 | 3611 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.57 | -99.74 | 6209 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.88 | -97.36 | 3685 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.56 | -98.47 | 4714 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.53 | -99.51 | 6146 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -33.98 | -95.86 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.61 | -35.26 | -95.61 | 4090 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.39 | -99.90 | 8326 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T20:25 | MACD zero-line | sell | BTC-USD | 13.79 | -0.09 | exit signal |
| 2026-10-10T20:20 | Squeeze breakout | sell | XRP-USD | 17.84 | -0.12 | exit signal |
| 2026-10-10T20:20 | Bollinger breakout | sell | XRP-USD | 12.97 | -0.09 | exit signal |
| 2026-10-10T20:20 | Donchian 55/20 | sell | ETH-USD | 17.65 | -0.14 | stop-loss |
| 2026-10-10T20:20 | Donchian 20/10 | sell | SOL-USD | 14.12 | -0.08 | exit signal |
| 2026-10-10T20:20 | RSI momentum | sell | ETH-USD | 13.93 | -0.10 | exit signal |
| 2026-10-10T20:20 | Supertrend | sell | ETH-USD | 13.12 | -0.02 | exit signal |
| 2026-10-10T20:20 | Triple EMA stack | sell | ETH-USD | 13.63 | -0.08 | exit signal |
| 2026-10-10T20:15 | Squeeze breakout | sell | SOL-USD | 17.87 | -0.09 | exit signal |
| 2026-10-10T20:15 | Keltner breakout | sell | SOL-USD | 15.82 | -0.10 | exit signal |
| 2026-10-10T20:15 | Bollinger breakout | sell | SOL-USD | 13.00 | -0.05 | exit signal |
| 2026-10-10T20:15 | Donchian 20/10 | sell | ETH-USD | 14.13 | -0.09 | exit signal |
| 2026-10-10T20:15 | MACD zero-line | sell | SOL-USD | 13.82 | -0.08 | exit signal |
| 2026-10-10T20:10 | Consensus | sell | ETH-USD | 12.70 | -0.07 | target is flat |
| 2026-10-10T20:10 | Squeeze breakout | sell | ETH-USD | 17.88 | -0.10 | stop-loss |
| 2026-10-10T20:10 | Keltner breakout | sell | ETH-USD | 15.79 | -0.12 | stop-loss |
| 2026-10-10T20:10 | Bollinger breakout | sell | ETH-USD | 13.00 | -0.06 | stop-loss |
| 2026-10-10T20:10 | Ichimoku | sell | ETH-USD | 15.13 | -0.07 | exit signal |
| 2026-10-10T20:10 | EMA 20/50 cross | buy | XRP-USD | 17.76 | — | entry signal |
| 2026-10-10T20:05 | Donchian 20/10 | buy | BTC-USD | 14.13 | — | entry signal |
| 2026-10-10T20:05 | RSI momentum | buy | BTC-USD | 13.93 | — | entry signal |
| 2026-10-10T20:00 | Triple EMA stack | sell | DOGE-USD | 13.58 | -0.09 | exit signal |
| 2026-10-10T19:55 | MACD zero-line | sell | DOGE-USD | 13.80 | -0.10 | exit signal |
| 2026-10-10T19:53 | AI bee: Boozy | sell | ETH-USD | 14.80 | -0.11 | Jev: sell |
| 2026-10-10T19:50 | AI bee: Bizzy | sell | ETH-USD | 9.13 | -0.06 | Jev: sell (sell p=0.63) after 11 min |
| 2026-10-10T19:50 | Squeeze breakout | sell | DOGE-USD | 17.83 | -0.14 | stop-loss |
| 2026-10-10T19:50 | Bollinger breakout | sell | DOGE-USD | 12.96 | -0.10 | stop-loss |
| 2026-10-10T19:50 | Donchian 20/10 | sell | DOGE-USD | 14.10 | -0.11 | stop-loss |
| 2026-10-10T19:50 | RSI momentum | sell | DOGE-USD | 13.90 | -0.11 | stop-loss |
| 2026-10-10T19:50 | Ichimoku | sell | DOGE-USD | 15.09 | -0.12 | target is flat |
| 2026-10-10T19:50 | EMA 20/50 cross | sell | DOGE-USD | 17.66 | -0.14 | stop-loss |
| 2026-10-10T19:40 | Consensus | buy | BTC-USD | 12.77 | — | entry |
| 2026-10-10T19:40 | RSI momentum | buy | DOGE-USD | 14.01 | — | entry |
| 2026-10-10T19:40 | MACD zero-line | buy | BTC-USD | 13.88 | — | entry signal |
| 2026-10-10T19:40 | Triple EMA stack | buy | BTC-USD | 13.66 | — | entry signal |
| 2026-10-10T19:39 | AI bee: Bizzy | buy | ETH-USD | 9.19 | — | Jev: buy (buy p=0.62) |
| 2026-10-10T19:38 | AI bee: Boozy | buy | ETH-USD | 14.91 | — | Jev: buy (buy p=0.77) |
| 2026-10-10T19:37 | AI bee: Bizzy | sell | SOL-USD | 9.59 | -0.05 | Jev: sell (sell p=0.54) after 16 min |
| 2026-10-10T19:35 | Squeeze breakout | buy | XRP-USD | 17.97 | — | entry signal |
| 2026-10-10T19:35 | Squeeze breakout | buy | DOGE-USD | 17.97 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 20:25:05.000144+00:00 -> 2026-10-10 20:35:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
