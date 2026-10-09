# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T22:25:05.000141+00:00 · 17191 ticks

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
| Copy: Insider buying | 2026-10-09 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.54 · VIX 14.79 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 37308 decisions in 3147 calls, $0.4625 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T22:25 | 2 / 3 / 0 | SOL-USD 15%, NANC 16%, COIN 14% |  |
| Breezy | 2026-10-09T22:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-09T22:25 | 3 / 2 / 0 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| MFI reversion | IWM | 2.14 | +1.01% | 5 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.79 | -2.38 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.26 | 2.26 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.06 | 2.06 | 14 | 57.1 | -12.06 | -1.91 | -21.08 | 72 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.30 | 1.30 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.14 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.50 | -0.55 | -37.31 | 43 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.26 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.31 | 2.48 | -1.52 | 90 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.30 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.17 | -0.83 | 88 | 55.7 | -11.00 | -2.14 | -15.04 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 21 | Copy: Cathie Wood (ARKK) | copy | 98.61 | -1.39 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 22 | Hold BTC | benchmark | 98.60 | -1.40 | 0 | — | 26.69 | 3.21 | -8.68 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.18 | -2.82 | 38 | 42.1 | 0.25 | 0.18 | -8.60 | 165 |
| 26 | Trend pullback · 1h | trend | 97.09 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.57 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 3.06 | 0.81 | -8.88 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.71 | -0.10 | -13.84 | 256 |
| 31 | Parabolic SAR · 1h | trend | 96.31 | -3.69 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.71 | -4.29 | 108 | 23.1 | -16.18 | -2.62 | -17.97 | 471 |
| 34 | Supertrend · 1h | trend | 94.95 | -5.05 | 52 | 13.5 | -0.37 | 0.14 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.26 | -5.74 | 35 | 25.7 | 24.23 | 3.30 | -8.62 | 105 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.53 | -6.47 | 119 | 34.5 | -12.46 | -1.97 | -17.79 | 128 |
| 39 | RSI(14) reversion · 1h | reversion | 93.13 | -6.87 | 26 | 26.9 | -2.46 | -0.43 | -9.03 | 152 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.38 | 0.16 | -19.98 | 120 |
| 42 | Agent (ML meta-label) | meta | 92.86 | -7.14 | 392 | 18.4 | -2.32 | -0.29 | -12.39 | 404 |
| 43 | Bollinger reversion · 1h | reversion | 92.77 | -7.23 | 73 | 37.0 | -20.89 | -5.00 | -23.70 | 319 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.76 | 0.66 | -17.07 | 221 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.98 | -8.02 | 67 | 29.9 | 6.65 | 1.02 | -12.90 | 284 |
| 47 | Williams %R · 1h | reversion | 91.68 | -8.32 | 116 | 48.3 | -25.29 | -4.36 | -27.39 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.72 | -9.28 | 69 | 15.9 | -9.29 | -0.94 | -26.38 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.15 | -9.85 | 114 | 30.7 | -28.00 | -5.55 | -29.70 | 519 |
| 51 | CCI reversion · 1h | reversion | 89.68 | -10.32 | 96 | 43.8 | -9.34 | -1.23 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.65 | -10.35 | 277 | 22.0 | -35.38 | -5.35 | -39.29 | 1279 |
| 53 | MACD zero-line · 1h | trend | 89.43 | -10.57 | 60 | 20.0 | -6.29 | -0.66 | -19.41 | 238 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Three white soldiers | momentum | 89.12 | -10.88 | 128 | 19.5 | -47.76 | -23.13 | -47.95 | 587 |
| 56 | Donchian 20/10 · 1h | breakout | 88.83 | -11.17 | 58 | 19.0 | 0.02 | 0.21 | -17.72 | 219 |
| 57 | OBV trend · 1h | momentum | 88.77 | -11.23 | 149 | 18.8 | -12.15 | -1.37 | -28.48 | 319 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.76 | -5.37 | -36.59 | 703 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.04 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.80 | -12.20 | 101 | 13.9 | -9.55 | -1.09 | -21.49 | 335 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.27 | -13.73 | 132 | 21.2 | -10.70 | -1.31 | -24.11 | 412 |
| 63 | RSI(14) reversion | reversion | 75.53 | -24.47 | 351 | 29.1 | -73.30 | -18.51 | -73.47 | 1505 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.02 | -16.73 | -73.90 | 1667 |
| 65 | Squeeze breakout | breakout | 73.91 | -26.09 | 299 | 15.7 | -61.58 | -18.17 | -61.67 | 1216 |
| 66 | Donchian 55/20 | breakout | 72.50 | -27.50 | 310 | 18.4 | -68.07 | -14.54 | -68.48 | 1299 |
| 67 | EMA 20/50 cross | trend | 72.08 | -27.92 | 307 | 20.5 | -77.54 | -15.51 | -77.73 | 1465 |
| 68 | Volume breakout | breakout | 71.54 | -28.46 | 248 | 13.7 | -63.34 | -18.20 | -63.52 | 902 |
| 69 | VWAP reversion | reversion | 68.36 | -31.64 | 393 | 26.2 | -71.85 | -16.14 | -72.23 | 1444 |
| 70 | Supertrend | trend | 66.18 | -33.83 | 434 | 20.5 | -86.57 | -21.38 | -86.60 | 1928 |
| 71 | Keltner breakout | breakout | 65.35 | -34.65 | 421 | 15.0 | -84.20 | -27.78 | -84.47 | 1860 |
| 72 | Ichimoku | trend | 62.41 | -37.59 | 383 | 10.2 | -81.75 | -23.47 | -81.87 | 1749 |
| 73 | AI bee: Bizzy | ai | 61.80 | -38.20 | 759 | 9.6 | — | — | — | — |
| 74 | Z-score reversion | reversion | 61.41 | -38.59 | 483 | 23.6 | -85.85 | -23.68 | -85.86 | 2101 |
| 75 | MFI reversion | reversion | 61.33 | -38.67 | 486 | 22.0 | -87.98 | -29.13 | -87.98 | 2134 |
| 76 | AI bee: Boozy | ai | 61.26 | -38.74 | 246 | 5.3 | — | — | — | — |
| 77 | Trend pullback | trend | 59.05 | -40.95 | 537 | 16.0 | -90.44 | -27.26 | -90.54 | 2299 |
| 78 | Donchian 20/10 | breakout | 59.03 | -40.97 | 593 | 18.9 | -90.84 | -26.18 | -90.91 | 2664 |
| 79 | ADX DI cross | trend | 58.60 | -41.40 | 518 | 10.4 | -89.79 | -34.89 | -89.79 | 2142 |
| 80 | RSI momentum | momentum | 58.00 | -42.00 | 560 | 17.9 | -90.32 | -25.74 | -90.35 | 2379 |
| 81 | MACD zero-line | trend | 57.37 | -42.63 | 546 | 15.8 | -91.59 | -29.91 | -91.59 | 2365 |
| 82 | Triple EMA stack | trend | 57.02 | -42.98 | 578 | 16.3 | -93.13 | -30.49 | -93.14 | 2612 |
| 83 | Bollinger breakout | breakout | 54.48 | -45.52 | 619 | 15.0 | -93.56 | -33.24 | -93.56 | 2819 |
| 84 | Consensus | meta | 52.91 | -47.09 | 586 | 10.4 | -94.23 | -25.73 | -94.24 | 2681 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.67 | -98.70 | 5401 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -33.24 | -97.37 | 3545 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.43 | -36.73 | -96.44 | 3606 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.02 | -99.36 | 5711 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.27 | -32.19 | -96.27 | 3602 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.59 | -99.73 | 6204 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.33 | -38.73 | -97.33 | 3677 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.43 | -98.50 | 4726 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.56 | -99.52 | 6159 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -33.72 | -95.89 | 3747 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.60 | -34.45 | -95.61 | 4087 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.03 | -99.90 | 8336 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T22:25 | Z-score reversion | sell | SOL-USD | 15.32 | -0.05 | exit signal |
| 2026-10-09T22:25 | Bollinger breakout | buy | ETH-USD | 13.63 | — | entry signal |
| 2026-10-09T22:25 | Supertrend | buy | ETH-USD | 16.56 | — | entry signal |
| 2026-10-09T22:23 | AI bee: Bizzy | buy | SOL-USD | 9.04 | — | Jev: buy (buy p=0.58) |
| 2026-10-09T22:20 | Trend pullback | buy | XRP-USD | 14.77 | — | entry signal |
| 2026-10-09T22:20 | ADX DI cross | buy | XRP-USD | 14.66 | — | entry signal |
| 2026-10-09T22:10 | MACD zero-line | sell | DOGE-USD | 11.49 | 0.00 | exit signal |
| 2026-10-09T22:05 | Keltner breakout | sell | DOGE-USD | 16.28 | -0.08 | stop-loss |
| 2026-10-09T22:05 | Bollinger breakout | sell | DOGE-USD | 13.60 | -0.07 | stop-loss |
| 2026-10-09T22:05 | Bollinger breakout | sell | BTC-USD | 13.58 | -0.09 | stop-loss |
| 2026-10-09T22:05 | Donchian 20/10 | sell | XRP-USD | 14.67 | -0.12 | exit signal |
| 2026-10-09T22:05 | Donchian 20/10 | sell | BTC-USD | 14.71 | -0.10 | exit signal |
| 2026-10-09T22:05 | RSI momentum | sell | ETH-USD | 14.43 | -0.12 | stop-loss |
| 2026-10-09T22:05 | RSI momentum | sell | BTC-USD | 14.45 | -0.10 | exit signal |
| 2026-10-09T22:05 | MACD zero-line | sell | XRP-USD | 11.47 | -0.07 | exit signal |
| 2026-10-09T22:05 | MACD zero-line | sell | SOL-USD | 5.77 | -0.06 | stop-loss |
| 2026-10-09T22:05 | MACD zero-line | sell | ETH-USD | 14.32 | -0.10 | exit signal |
| 2026-10-09T22:05 | MACD zero-line | sell | BTC-USD | 14.32 | -0.10 | exit signal |
| 2026-10-09T22:00 | Williams %R · 1h | buy | BTC-USD | 5.17 | — | entry signal |
| 2026-10-09T22:00 | Williams %R · 1h | sell | XRP-USD | 5.17 | 0.00 | rebalance down |
| 2026-10-09T21:59 | AI bee: Bizzy | sell | DOGE-USD | 8.58 | -0.06 | Jev: sell (sell p=0.74) after 10 min |
| 2026-10-09T21:50 | MACD zero-line | buy | SOL-USD | 2.88 | — | rebalance up |
| 2026-10-09T21:50 | MACD zero-line | sell | XRP-USD | 2.88 | -0.01 | rebalance down |
| 2026-10-09T21:49 | AI bee: Bizzy | buy | DOGE-USD | 8.64 | — | Jev: buy (buy p=0.56) |
| 2026-10-09T21:45 | MACD zero-line | buy | SOL-USD | 2.95 | — | entry signal |
| 2026-10-09T21:45 | MACD zero-line | sell | DOGE-USD | 2.93 | 0.01 | rebalance down |
| 2026-10-09T21:40 | RSI momentum | buy | ETH-USD | 14.55 | — | entry signal |
| 2026-10-09T21:26 | AI bee: Bizzy | sell | DOGE-USD | 8.93 | -0.03 | Jev: sell (sell p=0.54) after 23 min |
| 2026-10-09T21:20 | Donchian 55/20 | buy | XRP-USD | 18.13 | — | entry signal |
| 2026-10-09T21:20 | MACD zero-line | buy | ETH-USD | 14.42 | — | entry signal |
| 2026-10-09T21:15 | Donchian 20/10 | buy | XRP-USD | 14.79 | — | entry signal |
| 2026-10-09T21:10 | MACD zero-line | buy | BTC-USD | 14.42 | — | entry signal |
| 2026-10-09T21:05 | AI bee: Bizzy | sell | XRP-USD | 8.82 | -0.04 | Jev: sell (sell p=0.51) after 11 min |
| 2026-10-09T21:05 | Z-score reversion | sell | ETH-USD | 15.37 | -0.07 | exit signal |
| 2026-10-09T21:05 | Z-score reversion | sell | BTC-USD | 15.37 | -0.07 | exit signal |
| 2026-10-09T21:05 | Keltner breakout | buy | DOGE-USD | 16.36 | — | entry signal |
| 2026-10-09T21:05 | Bollinger breakout | buy | DOGE-USD | 13.67 | — | entry signal |
| 2026-10-09T21:05 | Bollinger breakout | buy | BTC-USD | 13.67 | — | entry signal |
| 2026-10-09T21:05 | Donchian 55/20 | buy | DOGE-USD | 18.14 | — | entry signal |
| 2026-10-09T21:05 | Donchian 20/10 | buy | DOGE-USD | 14.81 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 22:25:05.000141+00:00 -> 2026-10-09 22:35:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
