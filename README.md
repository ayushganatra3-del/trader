# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-07T01:25:05.000121+00:00 · 14057 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £98.10 (-1.90%)

Closed trades 37, win rate 62.2%, fees £1.39, max drawdown -2.35%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| DOGE-USD | 19.59 | -0.07 |
| XRP-USD | 19.54 | -0.12 |

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

Today: 1050 decisions in 210 calls, $0.0147 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-07T01:25 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-07T01:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-07T01:25 | 1 / 3 / 1 | MSTR 69% |  |

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
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.02 | 2.02 | 0 | — | 0.76 | 0.48 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Hold BTC | benchmark | 101.78 | 1.78 | 0 | — | 31.95 | 3.83 | -8.68 | 1 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.68 | 1.68 | 0 | — | 3.28 | 1.56 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 101.48 | 1.48 | 17 | 0.0 | 12.29 | 1.67 | -16.96 | 110 |
| 8 | Daily: Bullish score | daily | 101.40 | 1.40 | 3 | 0.0 | 5.96 | 0.98 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.13 | 1.13 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.53 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.11 | 0.11 | 68 | 38.2 | -21.68 | -4.94 | -23.39 | 489 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.95 | 1.89 | -1.59 | 84 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.08 | 0.08 | 0 | — | -2.39 | -0.91 | -7.65 | 1 |
| 15 | Stochastic reversion · 1h | reversion | 100.06 | 0.06 | 56 | 64.3 | -7.94 | -1.62 | -10.60 | 328 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 100.00 | 0.00 | 0 | — | -3.61 | -1.75 | -5.14 | 1 |
| 17 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 18 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 19 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.38 | -9.74 | 23 |
| 20 | EMA 20/50 cross · 1h | trend | 99.86 | -0.14 | 30 | 6.7 | 7.56 | 1.11 | -17.11 | 138 |
| 21 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.19 | 1.20 | -6.57 | 119 |
| 22 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.37 | -1.45 | -2.90 | 21 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 99.29 | -0.71 | 0 | — | 18.30 | 2.76 | -6.29 | 1 |
| 24 | Connors RSI(2) · 1h | reversion | 99.12 | -0.88 | 74 | 44.6 | -11.19 | -4.02 | -14.77 | 218 |
| 25 | Trend pullback · 1h | trend | 98.76 | -1.25 | 66 | 24.2 | -21.27 | -6.26 | -24.41 | 168 |
| 26 | Daily: Momentum burst | daily | 98.41 | -1.59 | 3 | 0.0 | 1.48 | 0.40 | -16.91 | 41 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.98 | -2.35 | -3.95 | 25 |
| 28 | Z-score reversion · 1h | reversion | 98.13 | -1.87 | 23 | 52.2 | 3.59 | 0.87 | -8.60 | 152 |
| 29 | Agent | meta | 98.10 | -1.90 | 37 | 62.2 | -7.89 | -5.01 | -9.35 | 224 |
| 30 | Agent (aggressive) | meta | 98.00 | -2.00 | 16 | 56.2 | -0.66 | -0.31 | -4.23 | 104 |
| 31 | Copy: Insider buying | copy | 98.00 | -2.00 | 11 | 54.5 | -15.61 | -2.86 | -21.08 | 73 |
| 32 | Bollinger reversion · 1h | reversion | 97.92 | -2.08 | 49 | 46.9 | -15.11 | -3.74 | -17.03 | 301 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.53 | -2.47 | 0 | — | -0.63 | -0.15 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.12 | -2.88 | 65 | 27.7 | 1.26 | 0.42 | -9.99 | 270 |
| 35 | ADX DI cross · 1h | trend | 96.83 | -3.17 | 43 | 11.6 | -3.12 | -0.40 | -13.84 | 257 |
| 36 | Supertrend · 1h | trend | 96.72 | -3.28 | 33 | 9.1 | 1.22 | 0.35 | -16.43 | 209 |
| 37 | Agent (ML meta-label) | meta | 96.66 | -3.34 | 265 | 14.7 | 1.62 | 0.43 | -13.50 | 396 |
| 38 | Parabolic SAR · 1h | trend | 96.38 | -3.62 | 65 | 15.4 | -4.33 | -0.39 | -19.45 | 300 |
| 39 | Williams %R · 1h | reversion | 96.35 | -3.65 | 85 | 52.9 | -19.21 | -3.57 | -19.58 | 490 |
| 40 | CCI reversion · 1h | reversion | 96.24 | -3.76 | 71 | 49.3 | 0.26 | 0.20 | -12.41 | 407 |
| 41 | MACD cross · 1h | trend | 95.65 | -4.34 | 90 | 20.0 | -13.21 | -2.11 | -17.27 | 466 |
| 42 | RSI momentum · 1h | momentum | 95.43 | -4.57 | 45 | 2.2 | -0.03 | 0.19 | -16.65 | 228 |
| 43 | MFI reversion · 1h | reversion | 95.09 | -4.91 | 75 | 28.0 | -9.65 | -1.65 | -16.99 | 117 |
| 44 | Squeeze breakout · 1h | breakout | 95.05 | -4.95 | 30 | 20.0 | 14.84 | 2.48 | -8.06 | 109 |
| 45 | Max aggression: 1-day momentum | meta | 95.00 | -5.00 | 7 | 42.9 | -23.54 | -1.21 | -37.31 | 42 |
| 46 | Ichimoku · 1h | trend | 94.79 | -5.21 | 34 | 14.7 | 2.32 | 0.49 | -16.99 | 125 |
| 47 | Triple EMA stack · 1h | trend | 94.55 | -5.45 | 57 | 10.5 | -10.05 | -1.00 | -24.82 | 254 |
| 48 | Bollinger breakout · 1h | breakout | 94.52 | -5.49 | 51 | 23.5 | 7.48 | 1.12 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 7.12 | 1.86 | -6.07 | 199 |
| 50 | Opening range 30m | breakout | 93.72 | -6.28 | 102 | 21.6 | -17.53 | -5.39 | -17.86 | 567 |
| 51 | Volume breakout · 1h | breakout | 93.61 | -6.39 | 36 | 11.1 | 6.25 | 1.02 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.62 | -7.38 | 84 | 10.7 | -2.96 | -0.20 | -18.47 | 347 |
| 53 | Opening range 15m | breakout | 92.26 | -7.74 | 118 | 20.3 | -18.95 | -5.58 | -19.29 | 686 |
| 54 | Max aggression: 5-day momentum | meta | 91.35 | -8.65 | 5 | 40.0 | -19.91 | -1.71 | -29.56 | 29 |
| 55 | Donchian 20/10 · 1h | breakout | 91.21 | -8.79 | 43 | 14.0 | 2.69 | 0.53 | -16.18 | 222 |
| 56 | MACD zero-line · 1h | trend | 91.13 | -8.87 | 51 | 17.6 | -4.36 | -0.39 | -18.32 | 242 |
| 57 | Three white soldiers | momentum | 90.78 | -9.22 | 103 | 19.4 | -49.42 | -24.58 | -49.53 | 590 |
| 58 | VWAP momentum · 1h | momentum | 90.71 | -9.29 | 229 | 22.7 | -36.90 | -5.63 | -37.13 | 1268 |
| 59 | OBV trend · 1h | momentum | 90.42 | -9.58 | 110 | 11.8 | -12.68 | -1.41 | -26.73 | 334 |
| 60 | Heikin-Ashi · 1h | trend | 89.96 | -10.04 | 116 | 25.0 | -31.15 | -5.32 | -34.37 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.69 | -10.31 | 30 | 6.7 | -10.47 | -1.20 | -23.31 | 226 |
| 62 | ROC + volume · 1h | momentum | 87.22 | -12.78 | 113 | 15.9 | -9.54 | -1.14 | -23.04 | 414 |
| 63 | RSI(14) reversion | reversion | 85.39 | -14.61 | 226 | 31.9 | -71.32 | -19.47 | -71.57 | 1418 |
| 64 | Squeeze breakout | breakout | 77.12 | -22.88 | 253 | 15.4 | -62.53 | -18.83 | -62.63 | 1226 |
| 65 | VWAP reversion | reversion | 77.00 | -23.00 | 281 | 28.1 | -68.88 | -15.96 | -68.95 | 1371 |
| 66 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.95 | -17.60 | -73.95 | 1655 |
| 67 | Donchian 55/20 | breakout | 75.88 | -24.12 | 260 | 17.3 | -68.79 | -15.09 | -68.79 | 1302 |
| 68 | EMA 20/50 cross | trend | 73.94 | -26.06 | 269 | 18.2 | -78.43 | -16.04 | -78.43 | 1474 |
| 69 | Volume breakout | breakout | 73.30 | -26.70 | 212 | 12.3 | -65.57 | -19.29 | -65.58 | 924 |
| 70 | Z-score reversion | reversion | 70.28 | -29.71 | 362 | 27.1 | -85.02 | -25.02 | -85.02 | 2040 |
| 71 | MFI reversion | reversion | 69.45 | -30.55 | 360 | 20.8 | -87.06 | -29.94 | -87.06 | 2096 |
| 72 | Supertrend | trend | 68.93 | -31.07 | 363 | 19.8 | -87.19 | -22.10 | -87.19 | 1925 |
| 73 | Keltner breakout | breakout | 67.65 | -32.35 | 352 | 13.1 | -85.57 | -29.90 | -85.57 | 1887 |
| 74 | AI bee: Bizzy | ai | 66.90 | -33.10 | 618 | 8.7 | — | — | — | — |
| 75 | Ichimoku | trend | 66.42 | -33.58 | 323 | 9.0 | -82.30 | -24.53 | -82.30 | 1769 |
| 76 | AI bee: Boozy | ai | 65.97 | -34.03 | 219 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.12 | -35.88 | 405 | 9.1 | -89.66 | -36.08 | -89.66 | 2100 |
| 78 | MACD zero-line | trend | 62.40 | -37.60 | 461 | 15.2 | -91.57 | -30.45 | -91.59 | 2364 |
| 79 | Donchian 20/10 | breakout | 62.07 | -37.93 | 496 | 17.9 | -91.14 | -27.07 | -91.16 | 2667 |
| 80 | RSI momentum | momentum | 61.13 | -38.87 | 462 | 16.7 | -90.75 | -26.47 | -90.75 | 2383 |
| 81 | Trend pullback | trend | 59.91 | -40.09 | 493 | 15.4 | -91.41 | -29.75 | -91.42 | 2345 |
| 82 | Triple EMA stack | trend | 59.51 | -40.49 | 515 | 15.1 | -93.46 | -31.89 | -93.46 | 2636 |
| 83 | Bollinger breakout | breakout | 58.66 | -41.34 | 507 | 13.8 | -94.04 | -34.78 | -94.05 | 2824 |
| 84 | Stochastic reversion | reversion | 57.08 | -42.92 | 730 | 23.0 | -95.52 | -36.48 | -95.52 | 4038 |
| 85 | Consensus | meta | 56.84 | -43.16 | 493 | 9.9 | -94.70 | -26.68 | -94.70 | 2719 |
| 86 | Bollinger reversion | reversion | 56.72 | -43.28 | 673 | 17.7 | -95.62 | -35.38 | -95.62 | 3670 |
| 87 | EMA 9/21 cross | trend | 54.50 | -45.50 | 638 | 16.1 | -97.45 | -34.69 | -97.45 | 3553 |
| 88 | Connors RSI(2) | reversion | 53.60 | -46.40 | 681 | 20.1 | -96.57 | -34.18 | -96.57 | 3638 |
| 89 | OBV trend | momentum | 51.55 | -48.45 | 745 | 14.6 | -96.49 | -38.71 | -96.49 | 3637 |
| 90 | CCI reversion | reversion | 50.92 | -49.08 | 709 | 17.1 | -98.45 | -39.13 | -98.45 | 4687 |
| 91 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -31.46 | -98.72 | 5363 |
| 92 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.29 | -38.72 | -99.29 | 5613 |
| 93 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -45.15 | -99.73 | 6133 |
| 94 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.44 | -41.20 | -97.44 | 3688 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -42.33 | -99.50 | 6090 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -49.91 | -99.90 | 8250 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-07T01:25 | Donchian 20/10 · 1h | sell | SOL-USD | 4.75 | -0.09 | stop-loss |
| 2026-10-07T01:25 | ROC + volume · 1h | sell | SOL-USD | 6.67 | -0.05 | stop-loss |
| 2026-10-07T01:25 | MACD zero-line · 1h | sell | SOL-USD | 15.06 | -0.15 | stop-loss |
| 2026-10-07T01:25 | EMA 9/21 cross · 1h | sell | SOL-USD | 1.11 | -0.01 | stop-loss |
| 2026-10-07T01:25 | CCI reversion | sell | BTC-USD | 12.71 | -0.10 | stop-loss |
| 2026-10-07T01:25 | Stochastic reversion | buy | XRP-USD | 14.30 | — | entry signal |
| 2026-10-07T01:25 | Stochastic reversion | sell | SOL-USD | 14.22 | -0.13 | stop-loss |
| 2026-10-07T01:25 | Stochastic reversion | sell | ETH-USD | 14.21 | -0.12 | stop-loss |
| 2026-10-07T01:25 | RSI momentum | sell | DOGE-USD | 15.20 | -0.10 | exit signal |
| 2026-10-07T01:20 | MFI reversion | sell | BTC-USD | 17.40 | -0.14 | stop-loss |
| 2026-10-07T01:20 | CCI reversion | sell | SOL-USD | 12.70 | -0.12 | stop-loss |
| 2026-10-07T01:20 | CCI reversion | sell | ETH-USD | 12.69 | -0.11 | stop-loss |
| 2026-10-07T01:20 | Z-score reversion | sell | XRP-USD | 17.56 | -0.15 | stop-loss |
| 2026-10-07T01:20 | Z-score reversion | sell | SOL-USD | 17.54 | -0.15 | stop-loss |
| 2026-10-07T01:20 | Z-score reversion | sell | ETH-USD | 17.52 | -0.14 | stop-loss |
| 2026-10-07T01:15 | Stochastic reversion | buy | ETH-USD | 14.33 | — | entry signal |
| 2026-10-07T01:10 | Z-score reversion | buy | ETH-USD | 17.66 | — | entry signal |
| 2026-10-07T01:05 | OBV trend | sell | ETH-USD | 12.81 | -0.10 | exit signal |
| 2026-10-07T01:05 | Supertrend | sell | ETH-USD | 17.23 | -0.09 | exit signal |
| 2026-10-07T01:05 | EMA 20/50 cross | sell | ETH-USD | 18.38 | -0.14 | exit signal |
| 2026-10-07T01:00 | Agent (aggressive) | buy | XRP-USD | 49.20 | — | following Stochastic reversion · 1h |
| 2026-10-07T01:00 | Agent | buy | XRP-USD | 19.65 | — | following Stochastic reversion · 1h |
| 2026-10-07T01:00 | Connors RSI(2) · 1h | buy | SOL-USD | 24.82 | — | entry signal |
| 2026-10-07T01:00 | OBV trend · 1h | sell | SOL-USD | 4.87 | -0.02 | exit signal |
| 2026-10-07T01:00 | MACD zero-line | sell | ETH-USD | 15.52 | -0.10 | exit signal |
| 2026-10-07T01:00 | Triple EMA stack | sell | ETH-USD | 14.81 | -0.10 | exit signal |
| 2026-10-07T01:00 | EMA 9/21 cross | sell | ETH-USD | 13.57 | -0.09 | exit signal |
| 2026-10-07T00:59 | AI bee: Bizzy | sell | XRP-USD | 9.57 | -0.06 | Jev: sell (sell p=0.70) after 11 min |
| 2026-10-07T00:59 | AI bee: Bizzy | sell | DOGE-USD | 9.69 | -0.06 | Jev: sell (sell p=0.65) after 10 min |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-09 01:25:05.000121+00:00 -> 2026-10-07 01:35:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
