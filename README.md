# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T00:30:05.000145+00:00 · 16166 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.72 (-4.28%)

Closed trades 50, win rate 54.0%, fees £2.06, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 19.15 | +0.00 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-08 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-08)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 21.98 · VIX 15.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.3, AMD 7.1, TECL 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 360 decisions in 72 calls, $0.0051 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T00:30 | 0 / 4 / 1 | SOXL 15%, AMD 14% |  |
| Breezy | 2026-10-09T00:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-09T00:30 | 1 / 3 / 1 | COIN 73% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.07 | 3.07 | 35 | 40.0 | -7.97 | -2.42 | -13.79 | 119 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 101.44 | 1.44 | 0 | — | -4.29 | -1.79 | -7.31 | 1 |
| 5 | Timing: Nasdaq FTD · TQQQ | daily | 101.28 | 1.28 | 0 | — | -6.17 | -1.07 | -15.27 | 1 |
| 6 | Hold SPY | benchmark | 100.73 | 0.73 | 0 | — | -0.11 | -0.02 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.70 | 0.70 | 0 | — | 1.17 | 0.59 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 100.69 | 0.69 | 0 | — | -1.64 | -0.89 | -5.09 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -3.83 | -1.25 | -9.74 | 25 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.79 | -0.21 | 0 | — | 0.61 | 0.31 | -5.18 | 1 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.97 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.41 | -1.47 | -3.04 | 21 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.18 | -1.52 | 86 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 98.79 | -1.22 | 0 | — | -5.06 | -2.42 | -5.36 | 1 |
| 17 | Copy: Insider buying | copy | 98.49 | -1.51 | 12 | 50.0 | -15.22 | -2.65 | -21.08 | 75 |
| 18 | Donchian 55/20 · 1h | breakout | 98.12 | -1.88 | 26 | 15.4 | 10.01 | 1.34 | -16.96 | 109 |
| 19 | Stochastic reversion · 1h | reversion | 98.07 | -1.93 | 76 | 50.0 | -12.79 | -2.56 | -15.24 | 345 |
| 20 | Hold BTC | benchmark | 97.71 | -2.29 | 0 | — | 25.52 | 3.07 | -8.68 | 1 |
| 21 | Three white soldiers · 1h | momentum | 97.53 | -2.47 | 6 | 0.0 | -3.03 | -2.34 | -4.15 | 26 |
| 22 | ADX DI cross · 1h | trend | 96.58 | -3.42 | 54 | 22.2 | -4.84 | -0.69 | -13.84 | 250 |
| 23 | Agent (rotation) | meta | 96.57 | -3.43 | 77 | 27.3 | 4.65 | 1.20 | -8.33 | 264 |
| 24 | Trend pullback · 1h | trend | 96.55 | -3.45 | 78 | 23.1 | -23.56 | -6.63 | -25.53 | 171 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.39 | -3.61 | 0 | — | 8.88 | 1.50 | -8.33 | 1 |
| 26 | EMA 20/50 cross · 1h | trend | 96.22 | -3.78 | 36 | 11.1 | 0.50 | 0.28 | -20.52 | 135 |
| 27 | Daily: Momentum burst | daily | 96.00 | -4.00 | 4 | 0.0 | -4.75 | -0.57 | -17.67 | 40 |
| 28 | Z-score reversion · 1h | reversion | 95.90 | -4.10 | 36 | 38.9 | -0.86 | -0.05 | -8.60 | 168 |
| 29 | Daily: Bullish score | daily | 95.81 | -4.19 | 3 | 0.0 | -1.35 | 0.02 | -12.76 | 10 |
| 30 | Agent | meta | 95.72 | -4.28 | 50 | 54.0 | -10.41 | -5.62 | -10.96 | 250 |
| 31 | Parabolic SAR · 1h | trend | 95.15 | -4.85 | 82 | 22.0 | -5.24 | -0.55 | -20.80 | 291 |
| 32 | MACD cross · 1h | trend | 95.13 | -4.87 | 105 | 22.9 | -18.78 | -3.01 | -19.88 | 464 |
| 33 | Squeeze breakout · 1h | breakout | 94.90 | -5.10 | 34 | 26.5 | 15.40 | 2.52 | -8.14 | 102 |
| 34 | Supertrend · 1h | trend | 94.43 | -5.57 | 51 | 13.7 | -4.58 | -0.47 | -18.09 | 209 |
| 35 | Agent (aggressive) | meta | 94.25 | -5.75 | 22 | 45.5 | -10.08 | -3.61 | -10.37 | 116 |
| 36 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.31 | 1.87 | -6.52 | 194 |
| 37 | Connors RSI(2) · 1h | reversion | 93.45 | -6.55 | 102 | 41.2 | -18.29 | -6.02 | -20.97 | 252 |
| 38 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.08 | 0.21 | -19.98 | 119 |
| 39 | Agent (ML meta-label) | meta | 92.65 | -7.35 | 350 | 18.6 | -6.30 | -1.09 | -13.86 | 404 |
| 40 | Bollinger breakout · 1h | breakout | 92.58 | -7.42 | 65 | 30.8 | 6.44 | 0.98 | -12.06 | 285 |
| 41 | RSI momentum · 1h | momentum | 92.44 | -7.56 | 60 | 15.0 | 1.31 | 0.36 | -16.65 | 218 |
| 42 | RSI(14) reversion · 1h | reversion | 92.34 | -7.66 | 26 | 26.9 | -4.33 | -0.83 | -9.03 | 154 |
| 43 | Volume breakout · 1h | breakout | 92.16 | -7.84 | 45 | 17.8 | 6.47 | 1.04 | -12.60 | 121 |
| 44 | Bollinger reversion · 1h | reversion | 91.63 | -8.37 | 68 | 33.8 | -22.14 | -5.35 | -23.94 | 319 |
| 45 | Max aggression: 1-day momentum | meta | 91.33 | -8.67 | 9 | 33.3 | -23.96 | -1.22 | -37.31 | 43 |
| 46 | Triple EMA stack · 1h | trend | 91.24 | -8.76 | 68 | 16.2 | -10.91 | -1.19 | -25.80 | 236 |
| 47 | MFI reversion · 1h | reversion | 90.84 | -9.16 | 96 | 28.1 | -15.55 | -2.67 | -16.99 | 129 |
| 48 | Opening range 30m | breakout | 90.76 | -9.23 | 131 | 20.6 | -17.37 | -5.24 | -17.94 | 562 |
| 49 | MACD zero-line · 1h | trend | 90.37 | -9.63 | 58 | 20.7 | -6.41 | -0.69 | -19.00 | 241 |
| 50 | Candlestick reversal · 1h | reversion | 90.30 | -9.70 | 97 | 29.9 | -29.85 | -5.88 | -30.94 | 501 |
| 51 | Williams %R · 1h | reversion | 90.24 | -9.76 | 107 | 44.9 | -26.94 | -4.73 | -27.42 | 515 |
| 52 | Three white soldiers | momentum | 89.14 | -10.86 | 122 | 18.9 | -48.50 | -23.42 | -48.50 | 587 |
| 53 | Opening range 15m | breakout | 88.59 | -11.41 | 153 | 19.0 | -19.52 | -5.58 | -20.06 | 683 |
| 54 | EMA 9/21 cross · 1h | trend | 88.56 | -11.44 | 99 | 14.1 | -11.03 | -1.29 | -20.61 | 334 |
| 55 | Donchian 20/10 · 1h | breakout | 88.38 | -11.62 | 55 | 20.0 | -1.95 | -0.03 | -17.36 | 219 |
| 56 | OBV trend · 1h | momentum | 88.30 | -11.70 | 139 | 18.0 | -15.69 | -1.79 | -30.22 | 319 |
| 57 | VWAP momentum · 1h | momentum | 88.28 | -11.72 | 262 | 21.4 | -36.65 | -5.55 | -39.20 | 1261 |
| 58 | CCI reversion · 1h | reversion | 87.72 | -12.28 | 91 | 40.7 | -11.36 | -1.55 | -14.35 | 419 |
| 59 | Keltner breakout · 1h | breakout | 87.68 | -12.32 | 41 | 19.5 | -11.06 | -1.27 | -24.35 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 87.63 | -12.37 | 133 | 25.6 | -33.13 | -5.66 | -36.31 | 693 |
| 61 | ROC + volume · 1h | momentum | 87.20 | -12.80 | 128 | 21.1 | -10.71 | -1.30 | -23.22 | 406 |
| 62 | Max aggression: 5-day momentum | meta | 83.64 | -16.36 | 7 | 28.6 | -27.10 | -2.40 | -34.64 | 30 |
| 63 | ROC + volume | momentum | 76.72 | -23.29 | 351 | 21.7 | -72.74 | -16.38 | -73.75 | 1645 |
| 64 | RSI(14) reversion | reversion | 75.58 | -24.42 | 338 | 28.1 | -73.47 | -18.40 | -73.64 | 1501 |
| 65 | Squeeze breakout | breakout | 74.48 | -25.52 | 277 | 15.2 | -62.27 | -18.21 | -62.30 | 1209 |
| 66 | Volume breakout | breakout | 72.74 | -27.26 | 224 | 13.4 | -63.49 | -18.05 | -63.61 | 897 |
| 67 | Donchian 55/20 | breakout | 72.28 | -27.72 | 281 | 17.1 | -68.41 | -14.58 | -68.45 | 1278 |
| 68 | EMA 20/50 cross | trend | 71.94 | -28.06 | 288 | 18.4 | -77.53 | -15.44 | -77.56 | 1450 |
| 69 | VWAP reversion | reversion | 68.60 | -31.40 | 379 | 25.3 | -71.96 | -16.01 | -72.25 | 1435 |
| 70 | Supertrend | trend | 67.48 | -32.52 | 413 | 20.3 | -86.71 | -21.12 | -86.96 | 1927 |
| 71 | Keltner breakout | breakout | 66.20 | -33.80 | 385 | 14.0 | -84.59 | -27.63 | -84.72 | 1853 |
| 72 | Ichimoku | trend | 64.25 | -35.75 | 351 | 9.4 | -81.61 | -22.97 | -81.65 | 1731 |
| 73 | AI bee: Bizzy | ai | 63.78 | -36.22 | 698 | 9.2 | — | — | — | — |
| 74 | MFI reversion | reversion | 62.36 | -37.64 | 447 | 20.8 | -87.99 | -28.43 | -88.02 | 2125 |
| 75 | Z-score reversion | reversion | 62.24 | -37.76 | 459 | 23.7 | -86.06 | -23.47 | -86.16 | 2095 |
| 76 | ADX DI cross | trend | 61.64 | -38.36 | 483 | 10.8 | -89.51 | -33.58 | -89.69 | 2128 |
| 77 | Donchian 20/10 | breakout | 60.56 | -39.44 | 545 | 18.7 | -90.92 | -25.73 | -91.02 | 2640 |
| 78 | MACD zero-line | trend | 60.23 | -39.77 | 515 | 16.1 | -91.32 | -28.88 | -91.37 | 2347 |
| 79 | AI bee: Boozy | ai | 60.03 | -39.97 | 239 | 5.4 | — | — | — | — |
| 80 | Trend pullback | trend | 59.63 | -40.37 | 507 | 15.8 | -90.59 | -26.91 | -90.63 | 2287 |
| 81 | RSI momentum | momentum | 59.38 | -40.62 | 512 | 17.8 | -90.24 | -25.06 | -90.37 | 2343 |
| 82 | Triple EMA stack | trend | 58.65 | -41.35 | 539 | 15.8 | -93.12 | -29.73 | -93.13 | 2589 |
| 83 | Bollinger breakout | breakout | 56.27 | -43.73 | 573 | 15.0 | -93.68 | -32.52 | -93.75 | 2806 |
| 84 | Consensus | meta | 54.90 | -45.10 | 537 | 10.2 | -94.25 | -25.13 | -94.25 | 2655 |
| 85 | EMA 9/21 cross | trend | 52.82 | -47.18 | 694 | 16.6 | -97.30 | -32.09 | -97.34 | 3518 |
| 86 | Connors RSI(2) | reversion | 52.75 | -47.25 | 718 | 21.2 | -96.17 | -31.23 | -96.17 | 3550 |
| 87 | Stochastic reversion | reversion | 50.98 | -49.02 | 859 | 23.1 | -95.71 | -33.65 | -95.74 | 4071 |
| 88 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.51 | -98.65 | 5317 |
| 89 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -35.39 | -96.30 | 3553 |
| 90 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -35.73 | -99.35 | 5667 |
| 91 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.73 | -99.73 | 6130 |
| 92 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -37.61 | -97.35 | 3634 |
| 93 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -36.39 | -98.51 | 4702 |
| 94 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.14 | -99.52 | 6120 |
| 95 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -32.98 | -95.92 | 3730 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.67 | -99.90 | 8238 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T00:30 | Consensus | buy | XRP-USD | 13.73 | — | entry |
| 2026-10-09T00:30 | Stochastic reversion | buy | SOL-USD | 12.69 | — | entry signal |
| 2026-10-09T00:30 | RSI(14) reversion | buy | SOL-USD | 18.91 | — | entry signal |
| 2026-10-09T00:25 | Z-score reversion | buy | DOGE-USD | 15.56 | — | entry signal |
| 2026-10-09T00:25 | EMA 20/50 cross | buy | DOGE-USD | 3.63 | — | rebalance up |
| 2026-10-09T00:25 | EMA 20/50 cross | buy | BTC-USD | 3.60 | — | rebalance up |
| 2026-10-09T00:25 | EMA 20/50 cross | sell | SOL-USD | 14.25 | -0.15 | exit signal |
| 2026-10-09T00:20 | Consensus | sell | XRP-USD | 13.66 | -0.10 | target is flat |
| 2026-10-09T00:20 | MFI reversion | sell | SOL-USD | 15.45 | -0.19 | stop-loss |
| 2026-10-09T00:20 | Stochastic reversion | sell | SOL-USD | 12.65 | -0.15 | stop-loss |
| 2026-10-09T00:20 | Ichimoku | sell | XRP-USD | 16.03 | -0.11 | exit signal |
| 2026-10-09T00:18 | AI bee: Bizzy | sell | XRP-USD | 9.04 | -0.06 | Jev: sell (sell p=0.67) after 10 min |
| 2026-10-09T00:15 | MFI reversion | buy | SOL-USD | 15.64 | — | entry signal |
| 2026-10-09T00:12 | Bollinger reversion | sell | SOL-USD | 12.43 | -0.07 | Kill switch: down 50% from peak |
| 2026-10-09T00:12 | Bollinger reversion | sell | DOGE-USD | 12.43 | -0.08 | Kill switch: down 50% from peak |
| 2026-10-09T00:12 | Bollinger reversion | sell | BTC-USD | 12.45 | -0.07 | Kill switch: down 50% from peak |
| 2026-10-09T00:10 | VWAP reversion | sell | SOL-USD | 17.09 | -0.13 | exit signal |
| 2026-10-09T00:10 | Bollinger reversion | buy | SOL-USD | 12.50 | — | entry signal |
| 2026-10-09T00:08 | AI bee: Bizzy | buy | XRP-USD | 9.10 | — | Jev: buy (buy p=0.57) |
| 2026-10-09T00:05 | Consensus | buy | XRP-USD | 13.76 | — | entry |
| 2026-10-09T00:05 | Stochastic reversion | buy | DOGE-USD | 12.79 | — | entry |
| 2026-10-09T00:05 | VWAP reversion | sell | ETH-USD | 17.13 | -0.09 | exit signal |
| 2026-10-09T00:05 | VWAP reversion | sell | DOGE-USD | 17.16 | -0.06 | exit signal |
| 2026-10-09T00:05 | Bollinger reversion | buy | DOGE-USD | 12.52 | — | entry signal |
| 2026-10-09T00:05 | ADX DI cross | buy | XRP-USD | 15.42 | — | entry signal |
| 2026-10-09T00:05 | Triple EMA stack | buy | ETH-USD | 14.67 | — | entry signal |
| 2026-10-09T00:00 | Three white soldiers · 1h | sell | DOGE-USD | 24.22 | -0.21 | exit signal |
| 2026-10-09T00:00 | Candlestick reversal · 1h | buy | XRP-USD | 11.31 | — | entry |
| 2026-10-09T00:00 | Candlestick reversal · 1h | buy | SOL-USD | 11.31 | — | entry |
| 2026-10-09T00:00 | Candlestick reversal · 1h | buy | ETH-USD | 11.31 | — | entry |
| 2026-10-09T00:00 | Candlestick reversal · 1h | buy | BTC-USD | 11.31 | — | entry |
| 2026-10-09T00:00 | Stochastic reversion | buy | XRP-USD | 12.80 | — | entry signal |
| 2026-10-09T00:00 | Stochastic reversion | buy | SOL-USD | 12.80 | — | entry signal |
| 2026-10-09T00:00 | VWAP reversion | buy | SOL-USD | 17.22 | — | entry |
| 2026-10-09T00:00 | VWAP reversion | buy | ETH-USD | 17.22 | — | entry |
| 2026-10-09T00:00 | VWAP reversion | buy | DOGE-USD | 17.22 | — | entry |
| 2026-10-09T00:00 | Bollinger reversion | buy | BTC-USD | 12.52 | — | entry signal |
| 2026-10-09T00:00 | Triple EMA stack | sell | ETH-USD | 11.74 | -0.05 | exit signal |
| 2026-10-08T23:55 | Stochastic reversion | buy | BTC-USD | 12.81 | — | entry signal |
| 2026-10-08T23:55 | Donchian 55/20 | sell | DOGE-USD | 14.41 | -0.07 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 00:30:05.000145+00:00 -> 2026-10-09 00:40:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
