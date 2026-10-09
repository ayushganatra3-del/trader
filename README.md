# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T17:30:05.000156+00:00 · 16967 ticks

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

### Market regime (QQQ, 2026-10-08)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 21.98 · VIX 15.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.3, AMD 7.1, TECL 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 25431 decisions in 2475 calls, $0.3197 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T17:30 | 2 / 18 / 10 | NANC 15% |  |
| Breezy | 2026-10-09T17:30 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-09T17:30 | 1 / 28 / 1 | COIN 75% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.33 | 3.33 | 37 | 43.2 | -8.02 | -2.46 | -13.79 | 118 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.42 | 2.42 | 0 | — | -4.27 | -0.69 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.22 | 2.22 | 0 | — | -3.64 | -1.49 | -7.31 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.44 | 1.44 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 7 | Hold SPY | benchmark | 101.29 | 1.29 | 0 | — | 0.43 | 0.30 | -3.66 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 101.12 | 1.12 | 0 | — | -0.93 | -0.49 | -5.09 | 1 |
| 9 | Max aggression: 1-day momentum | meta | 100.51 | 0.51 | 10 | 30.0 | -14.94 | -0.50 | -37.31 | 43 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Copy: Insider buying | copy | 100.35 | 0.35 | 14 | 57.1 | -13.62 | -2.30 | -21.08 | 72 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.88 | -0.12 | 9 | 22.2 | 3.58 | 1.13 | -7.55 | 44 |
| 15 | Stochastic reversion · 1h | reversion | 99.68 | -0.32 | 88 | 55.7 | -10.53 | -2.02 | -15.04 | 342 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.64 | -0.36 | 0 | — | -3.97 | -1.85 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.32 | -0.68 | 35 | 37.1 | 4.81 | 2.27 | -1.52 | 90 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.64 | -1.74 | -3.04 | 20 |
| 19 | Hold BTC | benchmark | 98.84 | -1.16 | 0 | — | 26.68 | 3.21 | -8.68 | 1 |
| 20 | Copy: Cathie Wood (ARKK) | copy | 98.77 | -1.23 | 0 | — | 11.65 | 1.89 | -8.33 | 1 |
| 21 | Donchian 55/20 · 1h | breakout | 98.77 | -1.24 | 27 | 14.8 | 12.65 | 1.59 | -16.96 | 109 |
| 22 | Daily: SMA 20/50 cross · AAPL | daily | 98.23 | -1.77 | 0 | — | 1.18 | 0.52 | -5.18 | 1 |
| 23 | Daily: Bullish score | daily | 97.79 | -2.21 | 4 | 0.0 | 0.73 | 0.29 | -12.76 | 11 |
| 24 | Z-score reversion · 1h | reversion | 97.42 | -2.58 | 38 | 42.1 | 0.47 | 0.22 | -8.60 | 165 |
| 25 | Three white soldiers · 1h | momentum | 97.41 | -2.59 | 6 | 0.0 | -3.22 | -2.49 | -4.28 | 27 |
| 26 | Trend pullback · 1h | trend | 97.03 | -2.97 | 78 | 23.1 | -22.76 | -6.41 | -25.39 | 169 |
| 27 | Agent (rotation) | meta | 96.79 | -3.21 | 79 | 29.1 | 2.40 | 0.68 | -8.65 | 253 |
| 28 | EMA 20/50 cross · 1h | trend | 96.73 | -3.27 | 38 | 13.2 | 4.24 | 0.69 | -19.85 | 135 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.49 | -3.51 | 55 | 21.8 | -2.03 | -0.15 | -13.84 | 254 |
| 31 | Parabolic SAR · 1h | trend | 96.28 | -3.72 | 82 | 22.0 | -2.93 | -0.22 | -20.87 | 293 |
| 32 | MACD cross · 1h | trend | 96.04 | -3.96 | 107 | 22.4 | -17.08 | -2.78 | -18.77 | 474 |
| 33 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 34 | Supertrend · 1h | trend | 94.94 | -5.06 | 52 | 13.5 | -0.46 | 0.13 | -18.22 | 209 |
| 35 | Squeeze breakout · 1h | breakout | 94.29 | -5.71 | 35 | 25.7 | 24.25 | 3.30 | -8.61 | 105 |
| 36 | MFI reversion · 1h | reversion | 94.15 | -5.85 | 112 | 35.7 | -11.37 | -1.76 | -17.79 | 129 |
| 37 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.55 | -2.07 | -6.59 | 109 |
| 38 | Gap and go | momentum | 93.87 | -6.13 | 56 | 10.7 | 7.66 | 1.97 | -6.64 | 200 |
| 39 | RSI(14) reversion · 1h | reversion | 93.60 | -6.40 | 26 | 26.9 | -4.21 | -0.81 | -9.03 | 158 |
| 40 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.21 | 0.23 | -19.98 | 118 |
| 41 | Connors RSI(2) · 1h | reversion | 93.05 | -6.95 | 110 | 43.6 | -18.31 | -6.08 | -20.97 | 253 |
| 42 | Agent (ML meta-label) | meta | 93.03 | -6.97 | 389 | 18.3 | -5.42 | -0.86 | -14.09 | 430 |
| 43 | Bollinger reversion · 1h | reversion | 93.02 | -6.98 | 73 | 37.0 | -20.71 | -4.93 | -23.75 | 318 |
| 44 | RSI momentum · 1h | momentum | 92.56 | -7.44 | 63 | 15.9 | 3.43 | 0.62 | -17.07 | 219 |
| 45 | Volume breakout · 1h | breakout | 92.22 | -7.78 | 51 | 15.7 | 7.50 | 1.18 | -12.60 | 123 |
| 46 | Williams %R · 1h | reversion | 91.73 | -8.27 | 116 | 48.3 | -25.20 | -4.34 | -27.37 | 512 |
| 47 | Bollinger breakout · 1h | breakout | 91.70 | -8.30 | 67 | 29.9 | 5.41 | 0.87 | -12.90 | 288 |
| 48 | Opening range 30m | breakout | 91.04 | -8.96 | 135 | 20.0 | -16.86 | -5.11 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.69 | -9.31 | 69 | 15.9 | -8.88 | -0.89 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.64 | -9.36 | 107 | 30.8 | -28.72 | -5.60 | -30.75 | 522 |
| 51 | CCI reversion · 1h | reversion | 90.13 | -9.87 | 94 | 42.6 | -9.06 | -1.18 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.84 | -10.16 | 272 | 22.1 | -35.73 | -5.42 | -39.33 | 1279 |
| 53 | MACD zero-line · 1h | trend | 89.62 | -10.38 | 59 | 20.3 | -6.42 | -0.68 | -19.40 | 238 |
| 54 | Opening range 15m | breakout | 89.24 | -10.76 | 157 | 18.5 | -18.43 | -5.24 | -19.78 | 700 |
| 55 | Three white soldiers | momentum | 89.13 | -10.87 | 126 | 19.0 | -47.87 | -23.28 | -48.05 | 584 |
| 56 | Donchian 20/10 · 1h | breakout | 88.75 | -11.25 | 57 | 19.3 | -1.08 | 0.08 | -17.72 | 222 |
| 57 | Heikin-Ashi · 1h | trend | 88.56 | -11.44 | 135 | 25.2 | -31.69 | -5.35 | -36.59 | 699 |
| 58 | OBV trend · 1h | momentum | 88.53 | -11.47 | 144 | 18.1 | -12.68 | -1.45 | -28.83 | 318 |
| 59 | EMA 9/21 cross · 1h | trend | 87.61 | -12.38 | 101 | 13.9 | -10.18 | -1.18 | -21.49 | 337 |
| 60 | Max aggression: 5-day momentum | meta | 86.83 | -13.16 | 7 | 28.6 | -15.46 | -1.18 | -34.64 | 28 |
| 61 | Keltner breakout · 1h | breakout | 86.65 | -13.35 | 43 | 18.6 | -12.13 | -1.41 | -25.35 | 216 |
| 62 | ROC + volume · 1h | momentum | 86.53 | -13.47 | 130 | 21.5 | -10.44 | -1.27 | -23.72 | 415 |
| 63 | RSI(14) reversion | reversion | 75.82 | -24.18 | 346 | 28.9 | -73.23 | -18.51 | -73.48 | 1501 |
| 64 | ROC + volume | momentum | 75.22 | -24.78 | 380 | 22.6 | -73.39 | -17.13 | -74.31 | 1673 |
| 65 | Squeeze breakout | breakout | 74.10 | -25.90 | 288 | 15.3 | -61.55 | -18.15 | -61.73 | 1207 |
| 66 | Donchian 55/20 | breakout | 72.79 | -27.21 | 294 | 17.0 | -67.94 | -14.45 | -68.48 | 1289 |
| 67 | EMA 20/50 cross | trend | 72.02 | -27.98 | 296 | 19.3 | -77.59 | -15.53 | -77.76 | 1462 |
| 68 | Volume breakout | breakout | 71.60 | -28.39 | 240 | 13.8 | -63.40 | -18.22 | -63.53 | 902 |
| 69 | VWAP reversion | reversion | 68.70 | -31.30 | 386 | 26.2 | -72.28 | -16.54 | -72.66 | 1458 |
| 70 | Supertrend | trend | 66.35 | -33.65 | 429 | 20.0 | -86.70 | -21.51 | -86.75 | 1928 |
| 71 | Keltner breakout | breakout | 65.62 | -34.38 | 409 | 14.4 | -84.13 | -27.72 | -84.45 | 1852 |
| 72 | AI bee: Bizzy | ai | 62.52 | -37.48 | 741 | 9.7 | — | — | — | — |
| 73 | Ichimoku | trend | 62.49 | -37.51 | 373 | 9.1 | -81.74 | -23.46 | -81.87 | 1744 |
| 74 | AI bee: Boozy | ai | 61.97 | -38.03 | 246 | 5.3 | — | — | — | — |
| 75 | Z-score reversion | reversion | 61.86 | -38.15 | 472 | 23.9 | -85.98 | -23.81 | -86.04 | 2100 |
| 76 | MFI reversion | reversion | 61.82 | -38.18 | 469 | 21.7 | -87.99 | -28.91 | -88.03 | 2122 |
| 77 | Donchian 20/10 | breakout | 59.42 | -40.58 | 573 | 18.7 | -90.84 | -26.24 | -90.96 | 2656 |
| 78 | Trend pullback | trend | 59.18 | -40.82 | 525 | 15.8 | -90.45 | -27.26 | -90.55 | 2297 |
| 79 | ADX DI cross | trend | 58.85 | -41.15 | 512 | 10.2 | -89.94 | -35.81 | -89.94 | 2147 |
| 80 | RSI momentum | momentum | 58.45 | -41.55 | 538 | 17.1 | -90.25 | -25.65 | -90.37 | 2369 |
| 81 | MACD zero-line | trend | 57.92 | -42.08 | 534 | 15.7 | -91.55 | -30.15 | -91.56 | 2359 |
| 82 | Triple EMA stack | trend | 57.19 | -42.81 | 563 | 15.5 | -93.11 | -30.43 | -93.14 | 2602 |
| 83 | Bollinger breakout | breakout | 54.87 | -45.13 | 600 | 15.0 | -93.54 | -33.32 | -93.54 | 2806 |
| 84 | Consensus | meta | 52.90 | -47.10 | 571 | 10.2 | -94.33 | -26.21 | -94.34 | 2684 |
| 85 | EMA 9/21 cross | trend | 50.69 | -49.31 | 727 | 15.8 | -97.36 | -33.48 | -97.36 | 3534 |
| 86 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -30.90 | -98.73 | 5399 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -36.73 | -96.42 | 3578 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.40 | -99.36 | 5692 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -32.27 | -96.29 | 3594 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.65 | -99.73 | 6171 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.31 | -38.56 | -97.32 | 3656 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.70 | -98.50 | 4713 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -41.44 | -99.53 | 6152 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -34.23 | -95.93 | 3746 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.68 | -35.26 | -95.68 | 4091 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.55 | -99.90 | 8304 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T17:30 | Consensus | buy | UPRO | 13.23 | — | entry |
| 2026-10-09T17:30 | Stochastic reversion · 1h | buy | SOXL | 5.16 | — | entry signal |
| 2026-10-09T17:30 | Stochastic reversion · 1h | sell | META | 5.16 | 0.01 | rebalance down |
| 2026-10-09T17:30 | Bollinger reversion · 1h | sell | META | 15.55 | 0.05 | exit signal |
| 2026-10-09T17:30 | VWAP momentum · 1h | buy | META | 3.97 | — | entry |
| 2026-10-09T17:30 | VWAP momentum · 1h | sell | GOOGL | 3.97 | -0.03 | exit signal |
| 2026-10-09T17:30 | MFI reversion | buy | SPY | 3.09 | — | rebalance up |
| 2026-10-09T17:30 | MFI reversion | sell | SOL-USD | 3.09 | -0.02 | rebalance down |
| 2026-10-09T17:30 | Bollinger breakout | buy | TECL | 13.70 | — | entry signal |
| 2026-10-09T17:30 | Bollinger breakout | buy | NVDA | 13.72 | — | entry signal |
| 2026-10-09T17:30 | Donchian 20/10 | buy | TECL | 5.39 | — | entry signal |
| 2026-10-09T17:30 | RSI momentum | buy | TECL | 4.50 | — | entry signal |
| 2026-10-09T17:30 | Trend pullback | buy | COIN | 4.61 | — | entry signal |
| 2026-10-09T17:30 | Trend pullback | sell | LABU | 4.61 | 0.19 | rebalance down |
| 2026-10-09T17:30 | EMA 20/50 cross | buy | DOGE-USD | 5.15 | — | entry signal |
| 2026-10-09T17:28 | AI bee: Bizzy | buy | NANC | 9.55 | — | Jev: buy (buy p=0.61) |
| 2026-10-09T17:28 | AI bee: Bizzy | sell | LABU | 8.81 | -0.02 | Jev: sell (sell p=0.62) after 20 min |
| 2026-10-09T17:25 | MFI reversion | buy | SPY | 9.27 | — | entry |
| 2026-10-09T17:25 | MFI reversion | buy | MSFT | 12.36 | — | entry signal |
| 2026-10-09T17:25 | MFI reversion | sell | SOXL | 3.15 | 0.01 | rebalance down |
| 2026-10-09T17:25 | MFI reversion | sell | PLTR | 3.14 | 0.01 | rebalance down |
| 2026-10-09T17:25 | Bollinger breakout | buy | PLTR | 13.72 | — | entry signal |
| 2026-10-09T17:25 | Bollinger breakout | sell | COIN | 13.69 | -0.08 | exit signal |
| 2026-10-09T17:25 | RSI momentum | sell | ETHU | 4.15 | -0.02 | exit signal |
| 2026-10-09T17:25 | RSI momentum | sell | DOGE-USD | 3.63 | -0.03 | exit signal |
| 2026-10-09T17:25 | ROC + volume | buy | LABU | 18.80 | — | entry signal |
| 2026-10-09T17:25 | Supertrend | sell | ETH-USD | 16.46 | -0.20 | exit signal |
| 2026-10-09T17:25 | Triple EMA stack | sell | DOGE-USD | 6.31 | -0.04 | target is flat |
| 2026-10-09T17:25 | EMA 20/50 cross | sell | DOGE-USD | 5.15 | -0.05 | exit signal |
| 2026-10-09T17:25 | EMA 9/21 cross | buy | XRP-USD | 2.65 | — | rebalance up |
| 2026-10-09T17:25 | EMA 9/21 cross | sell | DOGE-USD | 10.11 | -0.07 | exit signal |
| 2026-10-09T17:20 | Consensus | sell | AMZN | 13.19 | -0.03 | target is flat |
| 2026-10-09T17:20 | OBV trend · 1h | buy | TQQQ | 12.61 | — | entry |
| 2026-10-09T17:20 | MFI reversion | sell | SPY | 15.35 | -0.03 | target is flat |
| 2026-10-09T17:20 | Squeeze breakout | sell | SPY | 18.51 | -0.00 | exit signal |
| 2026-10-09T17:20 | Keltner breakout | buy | SPY | 3.77 | — | rebalance up |
| 2026-10-09T17:20 | Keltner breakout | buy | PLTR | 3.77 | — | rebalance up |
| 2026-10-09T17:20 | Keltner breakout | buy | LABU | 5.11 | — | rebalance up |
| 2026-10-09T17:20 | Keltner breakout | buy | COIN | 3.77 | — | rebalance up |
| 2026-10-09T17:20 | Keltner breakout | sell | MSFT | 9.34 | 0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 17:30:05.000156+00:00 -> 2026-10-09 17:40:05.000156+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
