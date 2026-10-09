# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T21:55:05.000147+00:00 · 17169 ticks

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

Today: 36978 decisions in 3081 calls, $0.4579 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T21:55 | 0 / 3 / 2 | DOGE-USD 14%, NANC 16%, COIN 14% |  |
| Breezy | 2026-10-09T21:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-09T21:55 | 2 / 2 / 1 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.78 | +2.31% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.16 | -2.15 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.26 | 2.26 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -12.05 | -1.91 | -21.08 | 72 |
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
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.16 | 2.42 | -1.52 | 90 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.30 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.17 | -0.83 | 88 | 55.7 | -10.97 | -2.14 | -14.99 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 98.64 | -1.36 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 21 | Hold BTC | benchmark | 98.62 | -1.38 | 0 | — | 26.69 | 3.21 | -8.68 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.61 | -1.39 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.16 | -2.84 | 38 | 42.1 | 0.24 | 0.18 | -8.60 | 165 |
| 26 | Trend pullback · 1h | trend | 97.09 | -2.91 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.55 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 2.65 | 0.73 | -8.65 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.35 | -3.65 | 58 | 20.7 | -1.71 | -0.10 | -13.84 | 256 |
| 31 | Parabolic SAR · 1h | trend | 96.31 | -3.69 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.70 | -4.30 | 108 | 23.1 | -16.83 | -2.74 | -18.30 | 474 |
| 34 | Supertrend · 1h | trend | 94.92 | -5.08 | 52 | 13.5 | -0.39 | 0.14 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.26 | -5.74 | 35 | 25.7 | 24.23 | 3.30 | -8.62 | 105 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.55 | -2.07 | -6.59 | 109 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.72 | 1.98 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.53 | -6.47 | 119 | 34.5 | -13.05 | -2.19 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.13 | -6.87 | 26 | 26.9 | -4.51 | -0.89 | -9.03 | 158 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.38 | 0.16 | -19.98 | 120 |
| 42 | Agent (ML meta-label) | meta | 92.86 | -7.13 | 392 | 18.4 | -6.14 | -1.01 | -14.16 | 407 |
| 43 | Bollinger reversion · 1h | reversion | 92.75 | -7.25 | 73 | 37.0 | -20.91 | -5.00 | -23.70 | 319 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.62 | 0.64 | -17.07 | 221 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.31 | 1.28 | -12.60 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 91.98 | -8.02 | 67 | 29.9 | 6.65 | 1.02 | -12.90 | 284 |
| 47 | Williams %R · 1h | reversion | 91.68 | -8.32 | 116 | 48.3 | -25.17 | -4.34 | -27.32 | 512 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.72 | -9.28 | 69 | 15.9 | -8.63 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.15 | -9.86 | 114 | 30.7 | -29.08 | -5.71 | -30.78 | 524 |
| 51 | CCI reversion · 1h | reversion | 89.67 | -10.33 | 96 | 43.8 | -9.36 | -1.23 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.66 | -10.34 | 277 | 22.0 | -35.58 | -5.40 | -39.46 | 1277 |
| 53 | MACD zero-line · 1h | trend | 89.43 | -10.57 | 60 | 20.0 | -6.60 | -0.71 | -19.41 | 239 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.22 | -19.78 | 700 |
| 55 | Three white soldiers | momentum | 89.12 | -10.88 | 128 | 19.5 | -47.86 | -23.27 | -48.05 | 586 |
| 56 | Donchian 20/10 · 1h | breakout | 88.83 | -11.17 | 58 | 19.0 | 0.02 | 0.21 | -17.72 | 219 |
| 57 | OBV trend · 1h | momentum | 88.77 | -11.23 | 149 | 18.8 | -12.33 | -1.40 | -28.83 | 320 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.76 | -5.37 | -36.59 | 703 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.04 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.80 | -12.20 | 101 | 13.9 | -9.78 | -1.12 | -21.49 | 336 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.55 | -1.33 | -25.35 | 215 |
| 62 | ROC + volume · 1h | momentum | 86.27 | -13.73 | 132 | 21.2 | -9.62 | -1.15 | -23.20 | 411 |
| 63 | RSI(14) reversion | reversion | 75.51 | -24.49 | 351 | 29.1 | -73.29 | -18.55 | -73.44 | 1505 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.41 | -17.08 | -74.27 | 1668 |
| 65 | Squeeze breakout | breakout | 73.91 | -26.09 | 299 | 15.7 | -61.65 | -18.21 | -61.74 | 1217 |
| 66 | Donchian 55/20 | breakout | 72.50 | -27.50 | 310 | 18.4 | -68.07 | -14.54 | -68.48 | 1299 |
| 67 | EMA 20/50 cross | trend | 72.08 | -27.92 | 307 | 20.5 | -77.50 | -15.49 | -77.69 | 1464 |
| 68 | Volume breakout | breakout | 71.54 | -28.46 | 248 | 13.7 | -63.40 | -18.27 | -63.65 | 901 |
| 69 | VWAP reversion | reversion | 68.33 | -31.66 | 393 | 26.2 | -71.94 | -16.32 | -72.24 | 1450 |
| 70 | Supertrend | trend | 66.23 | -33.77 | 434 | 20.5 | -86.62 | -21.44 | -86.66 | 1929 |
| 71 | Keltner breakout | breakout | 65.45 | -34.55 | 420 | 15.0 | -84.15 | -27.76 | -84.45 | 1859 |
| 72 | Ichimoku | trend | 62.41 | -37.59 | 383 | 10.2 | -81.75 | -23.47 | -81.87 | 1749 |
| 73 | AI bee: Bizzy | ai | 61.85 | -38.15 | 758 | 9.6 | — | — | — | — |
| 74 | Z-score reversion | reversion | 61.43 | -38.56 | 482 | 23.7 | -85.88 | -23.70 | -85.88 | 2102 |
| 75 | MFI reversion | reversion | 61.33 | -38.67 | 486 | 22.0 | -88.02 | -28.95 | -88.02 | 2117 |
| 76 | AI bee: Boozy | ai | 61.26 | -38.74 | 246 | 5.3 | — | — | — | — |
| 77 | Donchian 20/10 | breakout | 59.17 | -40.83 | 591 | 19.0 | -90.82 | -26.14 | -90.91 | 2664 |
| 78 | Trend pullback | trend | 59.09 | -40.91 | 537 | 16.0 | -90.42 | -27.21 | -90.52 | 2298 |
| 79 | ADX DI cross | trend | 58.65 | -41.35 | 518 | 10.4 | -89.82 | -34.87 | -89.82 | 2143 |
| 80 | RSI momentum | momentum | 58.13 | -41.87 | 558 | 17.9 | -90.29 | -25.70 | -90.35 | 2379 |
| 81 | MACD zero-line | trend | 57.65 | -42.35 | 541 | 15.7 | -91.55 | -29.91 | -91.55 | 2365 |
| 82 | Triple EMA stack | trend | 57.02 | -42.98 | 578 | 16.3 | -93.13 | -30.49 | -93.14 | 2612 |
| 83 | Bollinger breakout | breakout | 54.65 | -45.35 | 617 | 15.1 | -93.53 | -33.18 | -93.54 | 2818 |
| 84 | Consensus | meta | 52.91 | -47.09 | 586 | 10.4 | -94.25 | -25.87 | -94.27 | 2684 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -30.63 | -98.71 | 5393 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.22 | -97.36 | 3544 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -36.60 | -96.40 | 3585 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.13 | -99.36 | 5703 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.27 | -32.19 | -96.27 | 3602 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.56 | -99.73 | 6204 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.32 | -38.64 | -97.33 | 3675 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.42 | -98.50 | 4725 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.66 | -99.52 | 6155 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -33.70 | -95.88 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.62 | -34.53 | -95.62 | 4088 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.03 | -99.90 | 8339 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-09T21:05 | Donchian 20/10 | buy | BTC-USD | 14.81 | — | entry signal |
| 2026-10-09T21:05 | RSI momentum | buy | DOGE-USD | 14.55 | — | entry signal |
| 2026-10-09T21:05 | RSI momentum | buy | BTC-USD | 14.55 | — | entry signal |
| 2026-10-09T21:05 | Triple EMA stack | buy | DOGE-USD | 14.25 | — | entry signal |
| 2026-10-09T21:04 | AI bee: Bizzy | buy | DOGE-USD | 8.96 | — | Jev: buy (buy p=0.58) |
| 2026-10-09T21:00 | Stochastic reversion · 1h | buy | BTC-USD | 4.99 | — | entry signal |
| 2026-10-09T21:00 | Bollinger reversion · 1h | buy | SOL-USD | 15.46 | — | entry signal |
| 2026-10-09T21:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.31 | — | entry signal |
| 2026-10-09T21:00 | MACD cross · 1h | buy | XRP-USD | 4.78 | — | entry signal |
| 2026-10-09T21:00 | RSI(14) reversion | sell | BTC-USD | 18.86 | -0.11 | exit signal |
| 2026-10-09T21:00 | EMA 20/50 cross | buy | DOGE-USD | 17.99 | — | entry signal |
| 2026-10-09T20:54 | AI bee: Bizzy | buy | XRP-USD | 8.86 | — | Jev: buy (buy p=0.57) |
| 2026-10-09T20:35 | MACD zero-line | buy | DOGE-USD | 14.41 | — | entry signal |
| 2026-10-09T20:32 | AI bee: Bizzy | sell | DOGE-USD | 8.82 | -0.08 | Jev: sell (sell p=0.84) after 10 min |
| 2026-10-09T20:30 | ADX DI cross | sell | BTC-USD | 14.59 | -0.09 | exit signal |
| 2026-10-09T20:29 | AI bee: Bizzy | sell | SOL-USD | 8.73 | -0.06 | Jev: sell (sell p=0.81) after 10 min |
| 2026-10-09T20:25 | ADX DI cross | buy | BTC-USD | 14.68 | — | entry signal |
| 2026-10-09T20:22 | AI bee: Bizzy | buy | DOGE-USD | 8.90 | — | Jev: buy (buy p=0.57) |
| 2026-10-09T20:20 | VWAP reversion | sell | XRP-USD | 17.13 | -0.05 | exit signal |
| 2026-10-09T20:20 | Z-score reversion | sell | DOGE-USD | 15.36 | -0.03 | exit signal |
| 2026-10-09T20:20 | RSI momentum | buy | XRP-USD | 14.55 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 21:55:05.000147+00:00 -> 2026-10-09 22:05:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
