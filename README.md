# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T06:55:05.000143+00:00 · 17617 ticks

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

Today: 5295 decisions in 1059 calls, $0.0740 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T06:55 | 0 / 1 / 4 | NANC 17%, COIN 14% |  |
| Breezy | 2026-10-10T06:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T06:55 | 0 / 4 / 1 | COIN 75% |  |

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
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.31 | 2.48 | -1.52 | 90 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.33 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.19 | -0.81 | 88 | 55.7 | -10.88 | -2.11 | -14.99 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.94 | -1.06 | 0 | — | 27.34 | 3.28 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.23 | -2.77 | 41 | 43.9 | 1.52 | 0.43 | -8.60 | 162 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.59 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 0.51 | 0.23 | -8.66 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.88 | -0.13 | -13.84 | 257 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.86 | -4.14 | 108 | 23.1 | -16.29 | -2.64 | -17.97 | 473 |
| 34 | Supertrend · 1h | trend | 95.20 | -4.80 | 52 | 13.5 | -0.18 | 0.17 | -18.22 | 211 |
| 35 | Squeeze breakout · 1h | breakout | 94.18 | -5.82 | 35 | 25.7 | 24.13 | 3.28 | -8.65 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.43 | -1.96 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -3.28 | -0.61 | -9.03 | 153 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -1.67 | -0.15 | -12.51 | 414 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.85 | -4.99 | -23.54 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.06 | 0.69 | -17.07 | 222 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.90 | -8.10 | 67 | 29.9 | 6.57 | 1.01 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.80 | -8.20 | 119 | 47.9 | -25.08 | -4.32 | -27.28 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.64 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.27 | -9.73 | 114 | 30.7 | -28.26 | -5.59 | -30.10 | 523 |
| 51 | CCI reversion · 1h | reversion | 89.77 | -10.23 | 98 | 44.9 | -9.16 | -1.20 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.73 | -10.27 | 277 | 22.0 | -35.61 | -5.40 | -39.28 | 1287 |
| 53 | MACD zero-line · 1h | trend | 89.42 | -10.58 | 60 | 20.0 | -6.30 | -0.66 | -19.50 | 240 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Donchian 20/10 · 1h | breakout | 88.85 | -11.15 | 58 | 19.0 | -0.02 | 0.20 | -17.72 | 221 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.10 | -1.37 | -28.47 | 317 |
| 57 | Three white soldiers | momentum | 88.76 | -11.24 | 131 | 19.1 | -47.85 | -23.40 | -47.85 | 587 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.23 | -5.26 | -36.60 | 702 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.85 | -12.15 | 101 | 13.9 | -9.46 | -1.08 | -21.49 | 338 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.44 | -1.27 | -23.88 | 413 |
| 63 | RSI(14) reversion | reversion | 75.51 | -24.49 | 352 | 29.0 | -72.91 | -18.29 | -73.07 | 1497 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.04 | -16.74 | -73.92 | 1666 |
| 65 | Squeeze breakout | breakout | 73.14 | -26.86 | 307 | 15.6 | -61.87 | -18.41 | -61.88 | 1222 |
| 66 | EMA 20/50 cross | trend | 72.15 | -27.86 | 309 | 20.4 | -77.19 | -15.35 | -77.41 | 1460 |
| 67 | Donchian 55/20 | breakout | 72.06 | -27.94 | 316 | 18.7 | -67.79 | -14.57 | -68.00 | 1297 |
| 68 | Volume breakout | breakout | 71.23 | -28.77 | 252 | 13.5 | -63.23 | -18.39 | -63.25 | 902 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.80 | -16.18 | -71.94 | 1437 |
| 70 | Supertrend | trend | 66.14 | -33.86 | 438 | 20.8 | -86.37 | -21.23 | -86.38 | 1923 |
| 71 | Keltner breakout | breakout | 64.58 | -35.42 | 429 | 14.9 | -84.10 | -28.37 | -84.17 | 1858 |
| 72 | Z-score reversion | reversion | 61.41 | -38.59 | 483 | 23.6 | -85.72 | -23.52 | -85.73 | 2094 |
| 73 | Ichimoku | trend | 61.41 | -38.59 | 393 | 9.9 | -81.81 | -23.69 | -81.81 | 1751 |
| 74 | MFI reversion | reversion | 61.17 | -38.83 | 490 | 22.0 | -87.69 | -28.56 | -87.69 | 2120 |
| 75 | AI bee: Boozy | ai | 61.06 | -38.94 | 248 | 5.2 | — | — | — | — |
| 76 | AI bee: Bizzy | ai | 60.45 | -39.55 | 783 | 9.3 | — | — | — | — |
| 77 | ADX DI cross | trend | 58.56 | -41.44 | 520 | 10.6 | -89.53 | -34.61 | -89.53 | 2130 |
| 78 | Donchian 20/10 | breakout | 58.25 | -41.75 | 603 | 18.9 | -90.78 | -26.35 | -90.78 | 2663 |
| 79 | Trend pullback | trend | 58.17 | -41.83 | 548 | 15.9 | -90.40 | -27.16 | -90.40 | 2300 |
| 80 | RSI momentum | momentum | 57.46 | -42.54 | 569 | 17.9 | -90.26 | -25.85 | -90.27 | 2379 |
| 81 | MACD zero-line | trend | 56.92 | -43.08 | 551 | 15.6 | -91.57 | -29.97 | -91.57 | 2363 |
| 82 | Triple EMA stack | trend | 56.33 | -43.67 | 589 | 16.3 | -93.12 | -30.88 | -93.12 | 2613 |
| 83 | Bollinger breakout | breakout | 53.66 | -46.34 | 632 | 14.9 | -93.53 | -33.76 | -93.53 | 2818 |
| 84 | Consensus | meta | 51.93 | -48.07 | 600 | 10.2 | -94.26 | -26.07 | -94.26 | 2691 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.89 | -98.69 | 5392 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.62 | -97.36 | 3544 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.45 | -37.42 | -96.45 | 3611 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.02 | -99.34 | 5687 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.14 | -31.55 | -96.14 | 3581 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.04 | -99.73 | 6205 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -39.46 | -97.35 | 3683 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.53 | -98.47 | 4715 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.67 | -99.51 | 6148 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -33.77 | -95.85 | 3742 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.55 | -34.76 | -95.55 | 4082 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.39 | -99.90 | 8346 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T06:55 | Trend pullback | sell | SOL-USD | 14.47 | -0.11 | exit signal |
| 2026-10-10T06:54 | AI bee: Bizzy | sell | XRP-USD | 9.10 | -0.07 | Jev: sell (sell p=0.85) after 11 min |
| 2026-10-10T06:50 | Consensus | sell | XRP-USD | 12.90 | -0.11 | target is flat |
| 2026-10-10T06:50 | Three white soldiers | sell | XRP-USD | 22.05 | -0.18 | stop-loss |
| 2026-10-10T06:45 | Consensus | buy | XRP-USD | 13.01 | — | entry |
| 2026-10-10T06:45 | Three white soldiers | buy | XRP-USD | 22.23 | — | entry signal |
| 2026-10-10T06:45 | Trend pullback | buy | SOL-USD | 14.58 | — | entry signal |
| 2026-10-10T06:43 | AI bee: Bizzy | buy | XRP-USD | 9.17 | — | Jev: buy (buy p=0.61) |
| 2026-10-10T06:35 | Consensus | sell | BTC-USD | 13.00 | -0.08 | target is flat |
| 2026-10-10T06:35 | MACD zero-line | sell | BTC-USD | 14.22 | -0.07 | exit signal |
| 2026-10-10T06:30 | Donchian 55/20 | sell | DOGE-USD | 18.27 | 0.14 | exit signal |
| 2026-10-10T06:30 | RSI momentum | sell | SOL-USD | 14.33 | -0.11 | exit signal |
| 2026-10-10T06:30 | Trend pullback | sell | SOL-USD | 14.52 | -0.08 | exit signal |
| 2026-10-10T06:30 | Ichimoku | sell | ETH-USD | 15.40 | -0.08 | exit signal |
| 2026-10-10T06:30 | Supertrend | buy | XRP-USD | 3.45 | — | rebalance up |
| 2026-10-10T06:30 | Supertrend | sell | SOL-USD | 13.22 | -0.03 | exit signal |
| 2026-10-10T06:30 | Supertrend | sell | DOGE-USD | 13.33 | 0.14 | exit signal |
| 2026-10-10T06:30 | Triple EMA stack | sell | SOL-USD | 13.97 | -0.08 | exit signal |
| 2026-10-10T06:15 | Squeeze breakout | sell | ETH-USD | 18.23 | -0.13 | exit signal |
| 2026-10-10T06:15 | Bollinger breakout | sell | ETH-USD | 13.39 | -0.09 | exit signal |
| 2026-10-10T06:15 | Donchian 20/10 | sell | XRP-USD | 14.52 | -0.10 | exit signal |
| 2026-10-10T06:15 | Donchian 20/10 | sell | SOL-USD | 14.52 | -0.11 | exit signal |
| 2026-10-10T06:15 | RSI momentum | buy | SOL-USD | 3.14 | — | rebalance up |
| 2026-10-10T06:15 | RSI momentum | sell | DOGE-USD | 11.67 | 0.10 | exit signal |
| 2026-10-10T06:15 | Trend pullback | buy | BTC-USD | 5.83 | — | rebalance up |
| 2026-10-10T06:15 | Trend pullback | sell | DOGE-USD | 11.64 | -0.08 | exit signal |
| 2026-10-10T06:15 | MACD zero-line | sell | ETH-USD | 14.22 | -0.08 | exit signal |
| 2026-10-10T06:15 | Triple EMA stack | sell | DOGE-USD | 8.47 | -0.06 | exit signal |
| 2026-10-10T06:10 | Consensus | sell | XRP-USD | 13.03 | -0.05 | target is flat |
| 2026-10-10T06:05 | Consensus | sell | SOL-USD | 12.98 | -0.08 | target is flat |
| 2026-10-10T06:05 | Consensus | sell | DOGE-USD | 12.99 | -0.08 | target is flat |
| 2026-10-10T06:05 | Volume breakout | sell | ETH-USD | 17.73 | -0.11 | exit signal |
| 2026-10-10T06:05 | Squeeze breakout | sell | SOL-USD | 18.24 | -0.12 | stop-loss |
| 2026-10-10T06:05 | Keltner breakout | sell | XRP-USD | 16.09 | -0.14 | stop-loss |
| 2026-10-10T06:05 | Keltner breakout | sell | SOL-USD | 16.08 | -0.15 | stop-loss |
| 2026-10-10T06:05 | Bollinger breakout | sell | XRP-USD | 10.72 | -0.06 | stop-loss |
| 2026-10-10T06:05 | Bollinger breakout | sell | SOL-USD | 10.72 | -0.07 | stop-loss |
| 2026-10-10T06:05 | Donchian 55/20 | sell | SOL-USD | 17.68 | -0.16 | stop-loss |
| 2026-10-10T06:05 | Trend pullback | buy | BTC-USD | 2.91 | — | rebalance up |
| 2026-10-10T06:05 | Trend pullback | sell | ETH-USD | 2.91 | -0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 06:55:05.000143+00:00 -> 2026-10-10 07:05:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
