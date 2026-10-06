# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T23:25:05.000152+00:00 · 13964 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £98.29 (-1.71%)

Closed trades 37, win rate 62.2%, fees £1.28, max drawdown -2.16%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-06 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, PAM 12%, BORR 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-06)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.15 · VIX 15.01 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.5, MSTR 7.5, AMD 7.3, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 38429 decisions in 3283 calls, $0.4775 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T23:25 | 4 / 1 / 0 | XRP-USD 14% |  |
| Breezy | 2026-10-06T23:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-06T23:25 | 5 / 0 / 0 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 3.08 | +5.12% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| VWAP reversion · 1h | DOGE-USD | 1.89 | +3.24% | 5 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |
| VWAP reversion | TECL | 1.77 | +2.87% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.01 | 6.01 | 0 | — | 0.74 | 0.28 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -8.81 | -2.78 | -13.79 | 113 |
| 3 | Hold BTC | benchmark | 101.97 | 1.97 | 0 | — | 31.95 | 3.86 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.96 | 1.96 | 0 | — | 0.76 | 0.49 | -5.09 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.62 | 1.62 | 0 | — | 3.28 | 1.57 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 101.43 | 1.43 | 17 | 0.0 | 12.29 | 1.68 | -16.96 | 110 |
| 8 | Daily: Bullish score | daily | 101.34 | 1.34 | 3 | 0.0 | 5.96 | 0.99 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.07 | 1.07 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.32 | 0.32 | 68 | 38.2 | -21.18 | -4.83 | -23.37 | 487 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.88 | 1.87 | -1.59 | 85 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.02 | 0.02 | 0 | — | -2.39 | -0.91 | -7.65 | 1 |
| 15 | Stochastic reversion · 1h | reversion | 100.00 | 0.00 | 56 | 64.3 | -7.61 | -1.56 | -10.60 | 325 |
| 16 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 17 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 18 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 99.94 | -0.06 | 0 | — | -3.61 | -1.76 | -5.14 | 1 |
| 20 | EMA 20/50 cross · 1h | trend | 99.84 | -0.16 | 30 | 6.7 | 7.24 | 1.08 | -17.11 | 139 |
| 21 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.63 | 1.33 | -6.57 | 116 |
| 22 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.37 | -1.47 | -2.90 | 21 |
| 23 | Connors RSI(2) · 1h | reversion | 99.28 | -0.72 | 74 | 44.6 | -11.03 | -3.98 | -14.77 | 217 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 99.23 | -0.77 | 0 | — | 18.30 | 2.78 | -6.29 | 1 |
| 25 | Trend pullback · 1h | trend | 98.79 | -1.21 | 66 | 24.2 | -20.76 | -6.11 | -24.41 | 166 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -0.17 | -0.04 | -4.23 | 102 |
| 27 | Daily: Momentum burst | daily | 98.38 | -1.62 | 3 | 0.0 | 1.48 | 0.40 | -16.91 | 41 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -7.71 | -4.92 | -9.35 | 222 |
| 30 | Z-score reversion · 1h | reversion | 98.27 | -1.73 | 23 | 52.2 | 3.79 | 0.92 | -8.60 | 151 |
| 31 | Copy: Insider buying | copy | 97.94 | -2.06 | 11 | 54.5 | -15.61 | -2.88 | -21.08 | 73 |
| 32 | Bollinger reversion · 1h | reversion | 97.86 | -2.13 | 49 | 46.9 | -15.19 | -3.78 | -17.00 | 302 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.47 | -2.53 | 0 | — | -0.63 | -0.16 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.20 | -2.80 | 63 | 28.6 | -3.28 | -0.79 | -10.76 | 279 |
| 35 | ADX DI cross · 1h | trend | 96.78 | -3.22 | 43 | 11.6 | -2.87 | -0.36 | -13.84 | 257 |
| 36 | Supertrend · 1h | trend | 96.70 | -3.30 | 33 | 9.1 | 1.66 | 0.41 | -16.43 | 212 |
| 37 | Agent (ML meta-label) | meta | 96.61 | -3.40 | 265 | 14.7 | 7.52 | 1.43 | -12.24 | 376 |
| 38 | Williams %R · 1h | reversion | 96.39 | -3.61 | 85 | 52.9 | -19.43 | -3.64 | -19.95 | 493 |
| 39 | Parabolic SAR · 1h | trend | 96.35 | -3.65 | 65 | 15.4 | -4.29 | -0.39 | -19.45 | 300 |
| 40 | CCI reversion · 1h | reversion | 96.26 | -3.74 | 71 | 49.3 | 0.54 | 0.25 | -12.41 | 406 |
| 41 | MACD cross · 1h | trend | 95.64 | -4.36 | 90 | 20.0 | -13.04 | -2.10 | -17.27 | 465 |
| 42 | RSI momentum · 1h | momentum | 95.37 | -4.63 | 45 | 2.2 | 0.07 | 0.20 | -16.65 | 229 |
| 43 | MFI reversion · 1h | reversion | 95.06 | -4.94 | 75 | 28.0 | -9.69 | -1.67 | -16.99 | 118 |
| 44 | Squeeze breakout · 1h | breakout | 95.00 | -5.00 | 30 | 20.0 | 15.08 | 2.53 | -8.06 | 108 |
| 45 | Max aggression: 1-day momentum | meta | 94.94 | -5.06 | 7 | 42.9 | -23.54 | -1.22 | -37.31 | 42 |
| 46 | Ichimoku · 1h | trend | 94.81 | -5.19 | 34 | 14.7 | 2.40 | 0.50 | -16.99 | 125 |
| 47 | Triple EMA stack · 1h | trend | 94.50 | -5.50 | 57 | 10.5 | -9.73 | -0.96 | -24.82 | 253 |
| 48 | Bollinger breakout · 1h | breakout | 94.47 | -5.53 | 51 | 23.5 | 7.53 | 1.13 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 7.10 | 1.86 | -6.09 | 199 |
| 50 | Opening range 30m | breakout | 93.72 | -6.28 | 102 | 21.6 | -17.53 | -5.43 | -17.86 | 567 |
| 51 | Volume breakout · 1h | breakout | 93.57 | -6.43 | 36 | 11.1 | 6.35 | 1.04 | -12.60 | 132 |
| 52 | EMA 9/21 cross · 1h | trend | 92.58 | -7.42 | 83 | 10.8 | -2.98 | -0.20 | -18.47 | 347 |
| 53 | Opening range 15m | breakout | 92.26 | -7.74 | 118 | 20.3 | -18.95 | -5.62 | -19.29 | 686 |
| 54 | Max aggression: 5-day momentum | meta | 91.30 | -8.70 | 5 | 40.0 | -19.91 | -1.72 | -29.56 | 29 |
| 55 | Donchian 20/10 · 1h | breakout | 91.21 | -8.79 | 42 | 14.3 | 2.78 | 0.55 | -16.18 | 222 |
| 56 | MACD zero-line · 1h | trend | 91.21 | -8.79 | 50 | 18.0 | -4.55 | -0.42 | -18.32 | 244 |
| 57 | Three white soldiers | momentum | 90.94 | -9.06 | 102 | 19.6 | -49.48 | -25.10 | -49.68 | 591 |
| 58 | VWAP momentum · 1h | momentum | 90.66 | -9.35 | 229 | 22.7 | -36.85 | -5.67 | -36.99 | 1266 |
| 59 | OBV trend · 1h | momentum | 90.40 | -9.61 | 109 | 11.9 | -12.68 | -1.42 | -26.73 | 334 |
| 60 | Heikin-Ashi · 1h | trend | 89.91 | -10.09 | 116 | 25.0 | -31.13 | -5.35 | -34.35 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.64 | -10.36 | 30 | 6.7 | -10.65 | -1.24 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.23 | -12.77 | 112 | 16.1 | -9.48 | -1.14 | -23.04 | 416 |
| 63 | RSI(14) reversion | reversion | 85.39 | -14.61 | 226 | 31.9 | -71.74 | -19.65 | -71.99 | 1424 |
| 64 | Squeeze breakout | breakout | 77.25 | -22.75 | 252 | 15.5 | -62.47 | -19.06 | -62.57 | 1225 |
| 65 | VWAP reversion | reversion | 77.05 | -22.95 | 279 | 28.3 | -69.03 | -16.23 | -69.17 | 1377 |
| 66 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.95 | -17.84 | -73.95 | 1660 |
| 67 | Donchian 55/20 | breakout | 75.88 | -24.12 | 260 | 17.3 | -68.98 | -15.35 | -68.98 | 1305 |
| 68 | EMA 20/50 cross | trend | 74.08 | -25.92 | 268 | 18.3 | -78.57 | -16.27 | -78.57 | 1477 |
| 69 | Volume breakout | breakout | 73.30 | -26.70 | 212 | 12.3 | -65.66 | -19.58 | -65.66 | 928 |
| 70 | Z-score reversion | reversion | 70.91 | -29.09 | 358 | 27.4 | -84.88 | -25.30 | -84.88 | 2035 |
| 71 | MFI reversion | reversion | 69.68 | -30.32 | 358 | 20.9 | -87.10 | -30.61 | -87.11 | 2104 |
| 72 | Supertrend | trend | 69.06 | -30.94 | 362 | 19.9 | -87.20 | -22.47 | -87.21 | 1926 |
| 73 | Keltner breakout | breakout | 67.78 | -32.22 | 351 | 13.1 | -85.51 | -30.59 | -85.53 | 1885 |
| 74 | AI bee: Bizzy | ai | 67.17 | -32.83 | 613 | 8.8 | — | — | — | — |
| 75 | Ichimoku | trend | 66.52 | -33.48 | 322 | 9.0 | -82.29 | -24.96 | -82.30 | 1769 |
| 76 | AI bee: Boozy | ai | 65.97 | -34.03 | 219 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.20 | -35.80 | 404 | 9.2 | -89.65 | -37.28 | -89.65 | 2099 |
| 78 | MACD zero-line | trend | 62.62 | -37.38 | 459 | 15.3 | -91.56 | -31.18 | -91.57 | 2363 |
| 79 | Donchian 20/10 | breakout | 62.12 | -37.88 | 496 | 17.9 | -91.14 | -27.68 | -91.15 | 2666 |
| 80 | RSI momentum | momentum | 61.30 | -38.70 | 460 | 16.7 | -90.71 | -27.02 | -90.72 | 2383 |
| 81 | Trend pullback | trend | 59.91 | -40.09 | 493 | 15.4 | -91.46 | -30.75 | -91.46 | 2348 |
| 82 | Triple EMA stack | trend | 59.77 | -40.23 | 512 | 15.2 | -93.42 | -32.69 | -93.42 | 2633 |
| 83 | Bollinger breakout | breakout | 58.86 | -41.14 | 505 | 13.9 | -94.01 | -35.82 | -94.03 | 2822 |
| 84 | Stochastic reversion | reversion | 57.58 | -42.42 | 724 | 23.2 | -95.54 | -37.22 | -95.54 | 4040 |
| 85 | Bollinger reversion | reversion | 57.01 | -42.99 | 669 | 17.8 | -95.67 | -36.32 | -95.67 | 3675 |
| 86 | Consensus | meta | 56.94 | -43.06 | 492 | 10.0 | -94.66 | -27.31 | -94.66 | 2714 |
| 87 | EMA 9/21 cross | trend | 54.98 | -45.02 | 633 | 16.3 | -97.44 | -35.60 | -97.44 | 3549 |
| 88 | Connors RSI(2) | reversion | 53.60 | -46.40 | 681 | 20.1 | -96.59 | -35.41 | -96.59 | 3641 |
| 89 | OBV trend | momentum | 51.78 | -48.22 | 742 | 14.7 | -96.46 | -40.12 | -96.46 | 3607 |
| 90 | CCI reversion | reversion | 51.53 | -48.47 | 701 | 17.3 | -98.44 | -40.32 | -98.44 | 4686 |
| 91 | Candlestick reversal ⏸ | reversion | 50.65 | -49.35 | 803 | 14.9 | -99.29 | -39.54 | -99.29 | 5616 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -31.94 | -98.70 | 5356 |
| 93 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -46.80 | -99.73 | 6129 |
| 94 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.42 | -42.57 | -97.42 | 3684 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -43.88 | -99.50 | 6092 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -52.31 | -99.90 | 8246 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T23:25 | AI bee: Bizzy | buy | XRP-USD | 9.27 | — | Jev: buy (buy p=0.55) |
| 2026-10-06T23:25 | CCI reversion | buy | XRP-USD | 12.86 | — | entry signal |
| 2026-10-06T23:25 | Stochastic reversion | buy | BTC-USD | 14.43 | — | entry |
| 2026-10-06T23:25 | Stochastic reversion | sell | XRP-USD | 14.38 | -0.09 | exit signal |
| 2026-10-06T23:25 | Stochastic reversion | sell | DOGE-USD | 14.38 | -0.10 | exit signal |
| 2026-10-06T23:25 | Bollinger reversion | buy | SOL-USD | 14.27 | — | entry signal |
| 2026-10-06T23:25 | Bollinger reversion | sell | XRP-USD | 14.21 | -0.07 | exit signal |
| 2026-10-06T23:20 | Connors RSI(2) | sell | SOL-USD | 13.31 | -0.12 | stop-loss |
| 2026-10-06T23:20 | OBV trend | sell | SOL-USD | 12.88 | -0.13 | stop-loss |
| 2026-10-06T23:20 | EMA 20/50 cross | sell | SOL-USD | 18.42 | -0.18 | stop-loss |
| 2026-10-06T23:15 | Supertrend | sell | SOL-USD | 17.20 | -0.16 | exit signal |
| 2026-10-06T23:15 | Triple EMA stack | buy | ETH-USD | 14.95 | — | entry signal |
| 2026-10-06T23:05 | Stochastic reversion | buy | SOL-USD | 14.43 | — | entry signal |
| 2026-10-06T23:05 | Bollinger reversion | buy | XRP-USD | 14.28 | — | entry signal |
| 2026-10-06T23:05 | EMA 9/21 cross | buy | ETH-USD | 13.76 | — | entry signal |
| 2026-10-06T23:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 5.83 | -0.04 | exit signal |
| 2026-10-06T23:00 | CCI reversion | sell | XRP-USD | 12.85 | -0.11 | stop-loss |
| 2026-10-06T23:00 | VWAP reversion | buy | DOGE-USD | 19.27 | — | entry signal |
| 2026-10-06T23:00 | EMA 9/21 cross | sell | SOL-USD | 13.79 | -0.08 | exit signal |
| 2026-10-06T23:00 | EMA 9/21 cross | sell | ETH-USD | 13.80 | -0.06 | exit signal |
| 2026-10-06T22:55 | Consensus | sell | SOL-USD | 14.17 | -0.08 | target is flat |
| 2026-10-06T22:55 | MFI reversion | sell | DOGE-USD | 17.35 | -0.18 | stop-loss |
| 2026-10-06T22:55 | VWAP reversion | sell | DOGE-USD | 19.13 | -0.20 | stop-loss |
| 2026-10-06T22:55 | Z-score reversion | sell | DOGE-USD | 17.63 | -0.18 | stop-loss |
| 2026-10-06T22:55 | Bollinger reversion | sell | DOGE-USD | 14.23 | -0.14 | stop-loss |
| 2026-10-06T22:55 | Connors RSI(2) | buy | SOL-USD | 13.43 | — | entry signal |
| 2026-10-06T22:55 | RSI(14) reversion | sell | DOGE-USD | 21.18 | -0.22 | stop-loss |
| 2026-10-06T22:55 | Donchian 20/10 | sell | SOL-USD | 15.44 | -0.14 | exit signal |
| 2026-10-06T22:55 | RSI momentum | sell | SOL-USD | 15.23 | -0.12 | exit signal |
| 2026-10-06T22:55 | Trend pullback | sell | SOL-USD | 14.91 | -0.09 | exit signal |
| 2026-10-06T22:55 | Triple EMA stack | sell | SOL-USD | 14.91 | -0.10 | exit signal |
| 2026-10-06T22:50 | Bollinger reversion | sell | BTC-USD | 14.24 | -0.08 | exit signal |
| 2026-10-06T22:50 | OBV trend | buy | ETH-USD | 12.98 | — | entry signal |
| 2026-10-06T22:46 | CCI reversion | buy | ETH-USD | 12.91 | — | entry signal |
| 2026-10-06T22:46 | Stochastic reversion | buy | ETH-USD | 14.44 | — | entry signal |
| 2026-10-06T22:40 | CCI reversion | buy | BTC-USD | 12.92 | — | entry signal |
| 2026-10-06T22:40 | Squeeze breakout | sell | SOL-USD | 19.18 | -0.18 | stop-loss |
| 2026-10-06T22:40 | Keltner breakout | sell | SOL-USD | 16.83 | -0.16 | stop-loss |
| 2026-10-06T22:40 | Bollinger breakout | sell | SOL-USD | 14.65 | -0.12 | stop-loss |
| 2026-10-06T22:40 | Donchian 55/20 | sell | SOL-USD | 18.84 | -0.18 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 23:25:05.000152+00:00 -> 2026-10-06 23:35:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
