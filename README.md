# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T22:55:05.000126+00:00 · 13942 ticks

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

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.09 · VIX 15.13 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, MSTR 7.5, AMD 7.3, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 38099 decisions in 3217 calls, $0.4729 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T22:55 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-06T22:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-06T22:55 | 0 / 3 / 2 | MSTR 69% |  |

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
| 3 | Hold BTC | benchmark | 101.99 | 1.99 | 0 | — | 32.03 | 3.87 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.96 | 1.96 | 0 | — | 0.76 | 0.49 | -5.09 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.62 | 1.62 | 0 | — | 3.28 | 1.57 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 101.43 | 1.43 | 17 | 0.0 | 12.29 | 1.68 | -16.96 | 110 |
| 8 | Daily: Bullish score | daily | 101.34 | 1.34 | 3 | 0.0 | 5.96 | 0.99 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.07 | 1.07 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.31 | 0.31 | 68 | 38.2 | -21.02 | -4.78 | -23.37 | 486 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.95 | 1.91 | -1.59 | 84 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.02 | 0.02 | 0 | — | -2.39 | -0.91 | -7.65 | 1 |
| 15 | Stochastic reversion · 1h | reversion | 100.00 | 0.00 | 56 | 64.3 | -7.62 | -1.56 | -10.60 | 325 |
| 16 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 17 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 18 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 99.94 | -0.06 | 0 | — | -3.61 | -1.76 | -5.14 | 1 |
| 20 | EMA 20/50 cross · 1h | trend | 99.87 | -0.13 | 29 | 6.9 | 7.31 | 1.09 | -17.11 | 139 |
| 21 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.09 | 1.18 | -6.57 | 116 |
| 22 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.37 | -1.47 | -2.90 | 21 |
| 23 | Connors RSI(2) · 1h | reversion | 99.28 | -0.72 | 74 | 44.6 | -11.03 | -3.98 | -14.77 | 217 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 99.23 | -0.77 | 0 | — | 18.30 | 2.78 | -6.29 | 1 |
| 25 | Trend pullback · 1h | trend | 98.81 | -1.19 | 66 | 24.2 | -20.96 | -6.19 | -24.41 | 167 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -0.17 | -0.04 | -4.23 | 102 |
| 27 | Daily: Momentum burst | daily | 98.38 | -1.62 | 3 | 0.0 | 1.48 | 0.40 | -16.91 | 41 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -7.71 | -4.92 | -9.35 | 222 |
| 30 | Z-score reversion · 1h | reversion | 98.26 | -1.74 | 23 | 52.2 | 3.78 | 0.92 | -8.60 | 151 |
| 31 | Copy: Insider buying | copy | 97.94 | -2.06 | 11 | 54.5 | -15.61 | -2.88 | -21.08 | 73 |
| 32 | Bollinger reversion · 1h | reversion | 97.81 | -2.19 | 49 | 46.9 | -15.26 | -3.80 | -17.03 | 302 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.47 | -2.53 | 0 | — | -0.63 | -0.16 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.20 | -2.81 | 63 | 28.6 | 0.53 | 0.24 | -9.99 | 269 |
| 35 | ADX DI cross · 1h | trend | 96.78 | -3.22 | 43 | 11.6 | -3.01 | -0.38 | -13.84 | 257 |
| 36 | Supertrend · 1h | trend | 96.70 | -3.30 | 33 | 9.1 | 1.69 | 0.42 | -16.43 | 212 |
| 37 | Agent (ML meta-label) | meta | 96.61 | -3.40 | 265 | 14.7 | 6.22 | 1.19 | -14.05 | 384 |
| 38 | Williams %R · 1h | reversion | 96.38 | -3.62 | 85 | 52.9 | -19.46 | -3.65 | -19.97 | 493 |
| 39 | Parabolic SAR · 1h | trend | 96.36 | -3.64 | 65 | 15.4 | -4.29 | -0.39 | -19.45 | 300 |
| 40 | CCI reversion · 1h | reversion | 96.25 | -3.75 | 71 | 49.3 | 0.57 | 0.25 | -12.41 | 406 |
| 41 | MACD cross · 1h | trend | 95.65 | -4.35 | 90 | 20.0 | -13.81 | -2.24 | -17.27 | 469 |
| 42 | RSI momentum · 1h | momentum | 95.37 | -4.63 | 45 | 2.2 | 0.08 | 0.20 | -16.65 | 229 |
| 43 | MFI reversion · 1h | reversion | 95.06 | -4.94 | 75 | 28.0 | -9.66 | -1.67 | -16.99 | 118 |
| 44 | Squeeze breakout · 1h | breakout | 95.00 | -5.00 | 30 | 20.0 | 15.03 | 2.52 | -8.06 | 108 |
| 45 | Max aggression: 1-day momentum | meta | 94.94 | -5.06 | 7 | 42.9 | -23.54 | -1.22 | -37.31 | 42 |
| 46 | Ichimoku · 1h | trend | 94.83 | -5.17 | 34 | 14.7 | 2.42 | 0.50 | -16.99 | 125 |
| 47 | Triple EMA stack · 1h | trend | 94.50 | -5.50 | 57 | 10.5 | -9.67 | -0.96 | -24.82 | 253 |
| 48 | Bollinger breakout · 1h | breakout | 94.47 | -5.53 | 51 | 23.5 | 7.53 | 1.13 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 7.12 | 1.87 | -6.07 | 199 |
| 50 | Opening range 30m | breakout | 93.72 | -6.28 | 102 | 21.6 | -17.53 | -5.43 | -17.86 | 567 |
| 51 | Volume breakout · 1h | breakout | 93.57 | -6.43 | 36 | 11.1 | 6.28 | 1.04 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.58 | -7.42 | 83 | 10.8 | -2.95 | -0.20 | -18.47 | 347 |
| 53 | Opening range 15m | breakout | 92.26 | -7.74 | 118 | 20.3 | -18.95 | -5.62 | -19.29 | 686 |
| 54 | Max aggression: 5-day momentum | meta | 91.30 | -8.70 | 5 | 40.0 | -19.91 | -1.72 | -29.56 | 29 |
| 55 | MACD zero-line · 1h | trend | 91.23 | -8.77 | 50 | 18.0 | -4.38 | -0.39 | -18.32 | 243 |
| 56 | Donchian 20/10 · 1h | breakout | 91.22 | -8.78 | 42 | 14.3 | 2.45 | 0.51 | -16.18 | 223 |
| 57 | Three white soldiers | momentum | 90.94 | -9.06 | 102 | 19.6 | -49.33 | -24.88 | -49.53 | 589 |
| 58 | VWAP momentum · 1h | momentum | 90.66 | -9.35 | 229 | 22.7 | -37.04 | -5.70 | -37.06 | 1269 |
| 59 | OBV trend · 1h | momentum | 90.40 | -9.60 | 109 | 11.9 | -12.68 | -1.42 | -26.73 | 334 |
| 60 | Heikin-Ashi · 1h | trend | 89.91 | -10.09 | 116 | 25.0 | -31.15 | -5.36 | -34.37 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.64 | -10.36 | 30 | 6.7 | -10.61 | -1.23 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.24 | -12.76 | 112 | 16.1 | -9.42 | -1.13 | -23.04 | 414 |
| 63 | RSI(14) reversion | reversion | 85.39 | -14.61 | 226 | 31.9 | -71.95 | -19.53 | -72.20 | 1427 |
| 64 | Squeeze breakout | breakout | 77.25 | -22.75 | 252 | 15.5 | -62.47 | -19.06 | -62.57 | 1225 |
| 65 | VWAP reversion | reversion | 77.06 | -22.94 | 279 | 28.3 | -69.07 | -16.25 | -69.16 | 1376 |
| 66 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.95 | -17.84 | -73.95 | 1655 |
| 67 | Donchian 55/20 | breakout | 75.88 | -24.12 | 260 | 17.3 | -68.98 | -15.35 | -68.98 | 1305 |
| 68 | EMA 20/50 cross | trend | 74.19 | -25.81 | 267 | 18.4 | -78.53 | -16.25 | -78.53 | 1477 |
| 69 | Volume breakout | breakout | 73.30 | -26.70 | 212 | 12.3 | -65.57 | -19.58 | -65.58 | 924 |
| 70 | Z-score reversion | reversion | 70.91 | -29.09 | 358 | 27.4 | -84.89 | -25.31 | -84.89 | 2036 |
| 71 | MFI reversion | reversion | 69.68 | -30.32 | 358 | 20.9 | -87.08 | -30.56 | -87.08 | 2097 |
| 72 | Supertrend | trend | 69.13 | -30.87 | 361 | 19.9 | -87.19 | -22.47 | -87.20 | 1926 |
| 73 | Keltner breakout | breakout | 67.78 | -32.22 | 351 | 13.1 | -85.51 | -30.58 | -85.53 | 1885 |
| 74 | AI bee: Bizzy | ai | 67.20 | -32.80 | 613 | 8.8 | — | — | — | — |
| 75 | Ichimoku | trend | 66.52 | -33.48 | 322 | 9.0 | -82.29 | -24.96 | -82.30 | 1769 |
| 76 | AI bee: Boozy | ai | 65.97 | -34.03 | 219 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.20 | -35.80 | 404 | 9.2 | -89.65 | -37.28 | -89.65 | 2099 |
| 78 | MACD zero-line | trend | 62.62 | -37.38 | 459 | 15.3 | -91.56 | -31.18 | -91.57 | 2363 |
| 79 | Donchian 20/10 | breakout | 62.12 | -37.88 | 496 | 17.9 | -91.14 | -27.68 | -91.15 | 2666 |
| 80 | RSI momentum | momentum | 61.29 | -38.71 | 460 | 16.7 | -90.71 | -27.02 | -90.72 | 2383 |
| 81 | Trend pullback | trend | 59.91 | -40.09 | 493 | 15.4 | -91.46 | -30.75 | -91.46 | 2348 |
| 82 | Triple EMA stack | trend | 59.82 | -40.18 | 512 | 15.2 | -93.41 | -32.69 | -93.41 | 2632 |
| 83 | Bollinger breakout | breakout | 58.86 | -41.14 | 505 | 13.9 | -94.01 | -35.82 | -94.03 | 2822 |
| 84 | Stochastic reversion | reversion | 57.71 | -42.29 | 722 | 23.3 | -95.53 | -37.20 | -95.53 | 4038 |
| 85 | Bollinger reversion | reversion | 57.12 | -42.88 | 668 | 17.8 | -95.66 | -36.31 | -95.66 | 3673 |
| 86 | Consensus | meta | 56.94 | -43.06 | 492 | 10.0 | -94.70 | -27.35 | -94.70 | 2720 |
| 87 | EMA 9/21 cross | trend | 55.11 | -44.89 | 631 | 16.3 | -97.44 | -35.61 | -97.44 | 3550 |
| 88 | Connors RSI(2) | reversion | 53.68 | -46.32 | 680 | 20.1 | -96.58 | -35.40 | -96.58 | 3640 |
| 89 | OBV trend | momentum | 51.85 | -48.15 | 741 | 14.7 | -96.47 | -40.00 | -96.47 | 3636 |
| 90 | CCI reversion | reversion | 51.58 | -48.42 | 700 | 17.3 | -98.44 | -40.31 | -98.44 | 4685 |
| 91 | Candlestick reversal ⏸ | reversion | 50.65 | -49.35 | 803 | 14.9 | -99.30 | -39.44 | -99.30 | 5619 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -32.01 | -98.71 | 5362 |
| 93 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -46.81 | -99.73 | 6129 |
| 94 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.41 | -42.55 | -97.41 | 3683 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -43.83 | -99.50 | 6092 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -52.30 | -99.90 | 8243 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-06T22:40 | Ichimoku | sell | SOL-USD | 16.51 | -0.16 | stop-loss |
| 2026-10-06T22:35 | Bollinger reversion | buy | BTC-USD | 14.31 | — | entry signal |
| 2026-10-06T22:30 | Volume breakout | sell | SOL-USD | 18.23 | -0.13 | exit signal |
| 2026-10-06T22:30 | Donchian 20/10 | sell | ETH-USD | 15.52 | -0.09 | exit signal |
| 2026-10-06T22:30 | OBV trend | sell | ETH-USD | 12.91 | -0.10 | stop-loss |
| 2026-10-06T22:30 | Triple EMA stack | sell | ETH-USD | 14.90 | -0.11 | stop-loss |
| 2026-10-06T22:30 | EMA 20/50 cross | sell | ETH-USD | 18.46 | -0.14 | stop-loss |
| 2026-10-06T22:25 | AI bee: Boozy | sell | SOL-USD | 20.27 | -0.14 | Jev: sell (sell p=0.52) after 16 min |
| 2026-10-06T22:25 | MACD zero-line | sell | BTC-USD | 15.57 | -0.11 | exit signal |
| 2026-10-06T22:25 | EMA 9/21 cross | sell | BTC-USD | 13.71 | -0.09 | exit signal |
| 2026-10-06T22:15 | AI bee: Bizzy | sell | SOL-USD | 9.43 | -0.05 | Jev: sell (sell p=0.57) after 11 min |
| 2026-10-06T22:15 | Bollinger breakout | sell | ETH-USD | 14.67 | -0.10 | exit signal |
| 2026-10-06T22:10 | CCI reversion | sell | BTC-USD | 12.88 | -0.06 | exit signal |
| 2026-10-06T22:10 | Squeeze breakout | buy | SOL-USD | 19.36 | — | entry signal |
| 2026-10-06T22:10 | Keltner breakout | buy | SOL-USD | 16.99 | — | entry signal |
| 2026-10-06T22:10 | Donchian 55/20 | buy | SOL-USD | 19.01 | — | entry signal |
| 2026-10-06T22:10 | Ichimoku | buy | SOL-USD | 16.67 | — | entry signal |
| 2026-10-06T22:10 | Triple EMA stack | buy | ETH-USD | 15.01 | — | entry signal |
| 2026-10-06T22:09 | AI bee: Boozy | buy | SOL-USD | 20.42 | — | Jev: buy (buy p=0.69) |
| 2026-10-06T22:05 | Bollinger reversion | sell | XRP-USD | 14.26 | -0.07 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 22:55:05.000126+00:00 -> 2026-10-06 23:05:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
