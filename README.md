# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-07T00:55:05.000149+00:00 · 14028 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £98.28 (-1.72%)

Closed trades 37, win rate 62.2%, fees £1.33, max drawdown -2.23%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| DOGE-USD | 19.65 | -0.01 |

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

Today: 615 decisions in 123 calls, $0.0086 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-07T00:55 | 0 / 3 / 2 | DOGE-USD 15%, XRP-USD 14% |  |
| Breezy | 2026-10-07T00:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-07T00:55 | 1 / 4 / 0 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.34 | +4.22% | 5 |
| Stochastic reversion · 1h | XRP-USD | 2.19 | +4.46% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| RSI(14) reversion | ETHU | 1.93 | +0.48% | 3 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.07 | 6.07 | 0 | — | 0.74 | 0.28 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -8.81 | -2.76 | -13.79 | 113 |
| 3 | Hold BTC | benchmark | 102.04 | 2.04 | 0 | — | 32.17 | 3.86 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 102.02 | 2.02 | 0 | — | 0.76 | 0.48 | -5.09 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.68 | 1.68 | 0 | — | 3.28 | 1.56 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 101.48 | 1.48 | 17 | 0.0 | 12.29 | 1.67 | -16.96 | 110 |
| 8 | Daily: Bullish score | daily | 101.40 | 1.40 | 3 | 0.0 | 5.96 | 0.98 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.13 | 1.13 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.53 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.28 | 0.28 | 68 | 38.2 | -21.37 | -4.85 | -23.37 | 489 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.88 | 1.86 | -1.59 | 85 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.08 | 0.08 | 0 | — | -2.39 | -0.91 | -7.65 | 1 |
| 15 | Stochastic reversion · 1h | reversion | 100.06 | 0.06 | 56 | 64.3 | -7.69 | -1.56 | -10.60 | 327 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 100.00 | 0.00 | 0 | — | -3.61 | -1.75 | -5.14 | 1 |
| 17 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 18 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 19 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.38 | -9.74 | 23 |
| 20 | EMA 20/50 cross · 1h | trend | 99.89 | -0.11 | 30 | 6.7 | 7.24 | 1.07 | -17.11 | 139 |
| 21 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.66 | 1.32 | -6.57 | 118 |
| 22 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.37 | -1.45 | -2.90 | 21 |
| 23 | Connors RSI(2) · 1h | reversion | 99.29 | -0.71 | 74 | 44.6 | -11.03 | -3.95 | -14.77 | 217 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 99.29 | -0.71 | 0 | — | 18.30 | 2.76 | -6.29 | 1 |
| 25 | Trend pullback · 1h | trend | 98.83 | -1.17 | 66 | 24.2 | -20.77 | -6.07 | -24.41 | 166 |
| 26 | Agent (aggressive) | meta | 98.43 | -1.57 | 16 | 56.2 | -0.22 | -0.07 | -4.23 | 103 |
| 27 | Daily: Momentum burst | daily | 98.41 | -1.59 | 3 | 0.0 | 1.48 | 0.40 | -16.91 | 41 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.36 | -3.95 | 25 |
| 29 | Z-score reversion · 1h | reversion | 98.30 | -1.70 | 23 | 52.2 | 3.76 | 0.91 | -8.60 | 152 |
| 30 | Agent | meta | 98.28 | -1.72 | 37 | 62.2 | -7.73 | -4.90 | -9.35 | 223 |
| 31 | Copy: Insider buying | copy | 98.00 | -2.00 | 11 | 54.5 | -15.61 | -2.86 | -21.08 | 73 |
| 32 | Bollinger reversion · 1h | reversion | 97.99 | -2.01 | 49 | 46.9 | -15.02 | -3.71 | -17.00 | 301 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.53 | -2.47 | 0 | — | -0.63 | -0.15 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.12 | -2.88 | 65 | 27.7 | -2.92 | -0.69 | -10.40 | 280 |
| 35 | ADX DI cross · 1h | trend | 96.83 | -3.17 | 43 | 11.6 | -2.87 | -0.35 | -13.84 | 256 |
| 36 | Supertrend · 1h | trend | 96.76 | -3.25 | 33 | 9.1 | 1.90 | 0.44 | -16.43 | 211 |
| 37 | Agent (ML meta-label) | meta | 96.66 | -3.34 | 265 | 14.7 | 2.17 | 0.53 | -13.19 | 398 |
| 38 | Williams %R · 1h | reversion | 96.45 | -3.55 | 85 | 52.9 | -19.11 | -3.54 | -19.58 | 490 |
| 39 | Parabolic SAR · 1h | trend | 96.41 | -3.60 | 65 | 15.4 | -4.30 | -0.39 | -19.45 | 300 |
| 40 | CCI reversion · 1h | reversion | 96.32 | -3.69 | 71 | 49.3 | 0.45 | 0.23 | -12.41 | 407 |
| 41 | MACD cross · 1h | trend | 95.68 | -4.32 | 90 | 20.0 | -13.20 | -2.11 | -17.27 | 466 |
| 42 | RSI momentum · 1h | momentum | 95.43 | -4.57 | 45 | 2.2 | -0.12 | 0.18 | -16.65 | 229 |
| 43 | MFI reversion · 1h | reversion | 95.09 | -4.91 | 75 | 28.0 | -10.04 | -1.73 | -16.99 | 119 |
| 44 | Squeeze breakout · 1h | breakout | 95.05 | -4.95 | 30 | 20.0 | 15.68 | 2.60 | -8.06 | 106 |
| 45 | Max aggression: 1-day momentum | meta | 95.00 | -5.00 | 7 | 42.9 | -23.54 | -1.21 | -37.31 | 42 |
| 46 | Ichimoku · 1h | trend | 94.85 | -5.15 | 34 | 14.7 | 2.39 | 0.50 | -16.99 | 125 |
| 47 | Triple EMA stack · 1h | trend | 94.55 | -5.45 | 57 | 10.5 | -9.79 | -0.96 | -24.82 | 253 |
| 48 | Bollinger breakout · 1h | breakout | 94.52 | -5.49 | 51 | 23.5 | 7.53 | 1.12 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 7.10 | 1.85 | -6.09 | 199 |
| 50 | Opening range 30m | breakout | 93.72 | -6.28 | 102 | 21.6 | -17.53 | -5.39 | -17.86 | 567 |
| 51 | Volume breakout · 1h | breakout | 93.61 | -6.39 | 36 | 11.1 | 6.35 | 1.04 | -12.60 | 132 |
| 52 | EMA 9/21 cross · 1h | trend | 92.63 | -7.37 | 83 | 10.8 | -2.96 | -0.20 | -18.47 | 347 |
| 53 | Opening range 15m | breakout | 92.26 | -7.74 | 118 | 20.3 | -18.95 | -5.58 | -19.29 | 686 |
| 54 | Max aggression: 5-day momentum | meta | 91.35 | -8.65 | 5 | 40.0 | -19.91 | -1.71 | -29.56 | 29 |
| 55 | Donchian 20/10 · 1h | breakout | 91.25 | -8.75 | 42 | 14.3 | 2.44 | 0.50 | -16.18 | 223 |
| 56 | MACD zero-line · 1h | trend | 91.24 | -8.76 | 50 | 18.0 | -4.56 | -0.41 | -18.32 | 244 |
| 57 | Three white soldiers | momentum | 90.78 | -9.22 | 103 | 19.4 | -49.57 | -24.80 | -49.68 | 592 |
| 58 | VWAP momentum · 1h | momentum | 90.71 | -9.29 | 229 | 22.7 | -36.85 | -5.62 | -37.00 | 1266 |
| 59 | OBV trend · 1h | momentum | 90.44 | -9.55 | 109 | 11.9 | -12.70 | -1.41 | -26.73 | 334 |
| 60 | Heikin-Ashi · 1h | trend | 89.96 | -10.04 | 116 | 25.0 | -31.13 | -5.31 | -34.35 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.69 | -10.31 | 30 | 6.7 | -10.61 | -1.22 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.27 | -12.73 | 112 | 16.1 | -9.47 | -1.13 | -23.04 | 416 |
| 63 | RSI(14) reversion | reversion | 85.39 | -14.61 | 226 | 31.9 | -71.43 | -19.46 | -71.68 | 1419 |
| 64 | Squeeze breakout | breakout | 77.12 | -22.88 | 253 | 15.4 | -62.53 | -18.83 | -62.63 | 1226 |
| 65 | VWAP reversion | reversion | 77.00 | -23.00 | 281 | 28.1 | -68.96 | -16.01 | -69.06 | 1375 |
| 66 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.95 | -17.60 | -73.95 | 1660 |
| 67 | Donchian 55/20 | breakout | 75.88 | -24.12 | 260 | 17.3 | -68.79 | -15.09 | -68.79 | 1302 |
| 68 | EMA 20/50 cross | trend | 74.03 | -25.97 | 268 | 18.3 | -78.56 | -16.07 | -78.56 | 1477 |
| 69 | Volume breakout | breakout | 73.30 | -26.70 | 212 | 12.3 | -65.66 | -19.29 | -65.66 | 928 |
| 70 | Z-score reversion | reversion | 70.71 | -29.29 | 359 | 27.3 | -84.93 | -24.82 | -84.95 | 2039 |
| 71 | MFI reversion | reversion | 69.54 | -30.46 | 359 | 20.9 | -87.11 | -29.91 | -87.11 | 2104 |
| 72 | Supertrend | trend | 69.06 | -30.94 | 362 | 19.9 | -87.17 | -22.06 | -87.21 | 1926 |
| 73 | Keltner breakout | breakout | 67.65 | -32.35 | 352 | 13.1 | -85.54 | -29.88 | -85.56 | 1886 |
| 74 | AI bee: Bizzy | ai | 66.96 | -33.04 | 616 | 8.8 | — | — | — | — |
| 75 | Ichimoku | trend | 66.42 | -33.58 | 323 | 9.0 | -82.30 | -24.53 | -82.30 | 1769 |
| 76 | AI bee: Boozy | ai | 65.97 | -34.03 | 219 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.12 | -35.88 | 405 | 9.1 | -89.66 | -36.08 | -89.66 | 2100 |
| 78 | MACD zero-line | trend | 62.45 | -37.55 | 460 | 15.2 | -91.58 | -30.43 | -91.60 | 2365 |
| 79 | Donchian 20/10 | breakout | 62.11 | -37.89 | 496 | 17.9 | -91.14 | -27.05 | -91.16 | 2667 |
| 80 | RSI momentum | momentum | 61.22 | -38.78 | 461 | 16.7 | -90.75 | -26.44 | -90.76 | 2384 |
| 81 | Trend pullback | trend | 59.91 | -40.09 | 493 | 15.4 | -91.45 | -29.91 | -91.45 | 2347 |
| 82 | Triple EMA stack | trend | 59.56 | -40.44 | 514 | 15.2 | -93.45 | -31.85 | -93.45 | 2635 |
| 83 | Bollinger breakout | breakout | 58.66 | -41.34 | 507 | 13.8 | -94.03 | -34.78 | -94.05 | 2824 |
| 84 | Stochastic reversion | reversion | 57.35 | -42.65 | 728 | 23.1 | -95.52 | -36.20 | -95.52 | 4038 |
| 85 | Consensus | meta | 56.84 | -43.16 | 493 | 9.9 | -94.72 | -26.75 | -94.72 | 2722 |
| 86 | Bollinger reversion | reversion | 56.72 | -43.28 | 673 | 17.7 | -95.63 | -35.38 | -95.63 | 3671 |
| 87 | EMA 9/21 cross | trend | 54.59 | -45.41 | 637 | 16.2 | -97.45 | -34.63 | -97.46 | 3554 |
| 88 | Connors RSI(2) | reversion | 53.60 | -46.40 | 681 | 20.1 | -96.58 | -34.24 | -96.58 | 3639 |
| 89 | OBV trend | momentum | 51.60 | -48.40 | 744 | 14.7 | -96.47 | -38.81 | -96.47 | 3609 |
| 90 | CCI reversion | reversion | 51.16 | -48.84 | 706 | 17.1 | -98.45 | -38.91 | -98.45 | 4688 |
| 91 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -31.29 | -98.71 | 5362 |
| 92 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.29 | -38.51 | -99.29 | 5612 |
| 93 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -44.86 | -99.73 | 6134 |
| 94 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.43 | -41.03 | -97.43 | 3688 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -42.16 | -99.50 | 6092 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -49.64 | -99.90 | 8251 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-07T00:55 | MACD zero-line | buy | ETH-USD | 15.62 | — | entry signal |
| 2026-10-07T00:55 | Triple EMA stack | buy | ETH-USD | 14.90 | — | entry signal |
| 2026-10-07T00:55 | EMA 9/21 cross | buy | ETH-USD | 13.66 | — | entry signal |
| 2026-10-07T00:50 | CCI reversion | sell | XRP-USD | 12.78 | -0.05 | exit signal |
| 2026-10-07T00:50 | Stochastic reversion | sell | XRP-USD | 14.30 | -0.05 | exit signal |
| 2026-10-07T00:50 | OBV trend | buy | ETH-USD | 12.91 | — | entry signal |
| 2026-10-07T00:50 | EMA 20/50 cross | buy | ETH-USD | 18.52 | — | entry signal |
| 2026-10-07T00:49 | AI bee: Bizzy | buy | DOGE-USD | 9.75 | — | Jev: buy (buy p=0.58) |
| 2026-10-07T00:48 | AI bee: Bizzy | buy | XRP-USD | 9.63 | — | Jev: buy (buy p=0.57) |
| 2026-10-07T00:45 | Bollinger reversion | sell | BTC-USD | 14.12 | -0.08 | exit signal |
| 2026-10-07T00:40 | CCI reversion | buy | ETH-USD | 12.81 | — | entry signal |
| 2026-10-07T00:40 | CCI reversion | buy | BTC-USD | 12.81 | — | entry signal |
| 2026-10-07T00:40 | Stochastic reversion | buy | SOL-USD | 14.35 | — | entry signal |
| 2026-10-07T00:35 | Stochastic reversion | buy | XRP-USD | 14.36 | — | entry signal |
| 2026-10-07T00:35 | Z-score reversion | buy | BTC-USD | 17.67 | — | entry signal |
| 2026-10-07T00:35 | Bollinger reversion | buy | BTC-USD | 14.20 | — | entry signal |
| 2026-10-07T00:35 | MACD zero-line | sell | DOGE-USD | 15.54 | -0.12 | exit signal |
| 2026-10-07T00:30 | Squeeze breakout | sell | DOGE-USD | 19.18 | -0.13 | stop-loss |
| 2026-10-07T00:30 | Keltner breakout | sell | DOGE-USD | 16.81 | -0.13 | stop-loss |
| 2026-10-07T00:30 | Bollinger breakout | sell | DOGE-USD | 14.62 | -0.10 | stop-loss |
| 2026-10-07T00:27 | Candlestick reversal | sell | XRP-USD | 12.55 | -0.09 | Kill switch: down 50% from peak |
| 2026-10-07T00:25 | Bollinger reversion | sell | SOL-USD | 14.15 | -0.12 | stop-loss |
| 2026-10-07T00:25 | Candlestick reversal | sell | SOL-USD | 12.55 | -0.11 | stop-loss |
| 2026-10-07T00:25 | OBV trend | sell | ETH-USD | 12.84 | -0.10 | exit signal |
| 2026-10-07T00:25 | Ichimoku | sell | ETH-USD | 16.53 | -0.10 | exit signal |
| 2026-10-07T00:25 | ADX DI cross | sell | DOGE-USD | 15.97 | -0.08 | exit signal |
| 2026-10-07T00:25 | Triple EMA stack | sell | ETH-USD | 14.83 | -0.10 | exit signal |
| 2026-10-07T00:25 | EMA 9/21 cross | sell | ETH-USD | 13.64 | -0.09 | exit signal |
| 2026-10-07T00:25 | EMA 9/21 cross | sell | BTC-USD | 13.59 | -0.10 | exit signal |
| 2026-10-07T00:22 | AI bee: Bizzy | sell | DOGE-USD | 9.41 | -0.07 | Jev: sell (sell p=0.76) after 10 min |
| 2026-10-07T00:20 | MFI reversion | sell | SOL-USD | 17.27 | -0.16 | stop-loss |
| 2026-10-07T00:20 | Candlestick reversal | sell | ETH-USD | 12.56 | -0.08 | exit signal |
| 2026-10-07T00:20 | Candlestick reversal | sell | BTC-USD | 12.58 | -0.08 | exit signal |
| 2026-10-07T00:15 | OBV trend | buy | ETH-USD | 12.93 | — | entry signal |
| 2026-10-07T00:15 | EMA 9/21 cross | buy | BTC-USD | 13.69 | — | entry signal |
| 2026-10-07T00:12 | AI bee: Bizzy | buy | DOGE-USD | 9.48 | — | Jev: buy (buy p=0.57) |
| 2026-10-07T00:10 | VWAP reversion | sell | ETH-USD | 19.28 | -0.04 | exit signal |
| 2026-10-07T00:10 | VWAP reversion | sell | DOGE-USD | 19.25 | -0.02 | exit signal |
| 2026-10-07T00:10 | Z-score reversion | buy | SOL-USD | 17.69 | — | entry signal |
| 2026-10-07T00:10 | Bollinger reversion | sell | XRP-USD | 14.19 | -0.06 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-09 00:55:05.000149+00:00 -> 2026-10-07 01:05:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
