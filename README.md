# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-07T22:30:05.000136+00:00 · 14880 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.56 (-3.44%)

Closed trades 41, win rate 56.1%, fees £1.82, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.44 | +0.06 |
| DOGE-USD | 19.33 | -0.08 |
| ETHU | 19.45 | +0.07 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-07 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, BORR 12%, PSUS 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 23574 decisions in 2679 calls, $0.3024 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-07T22:30 | 0 / 4 / 1 | DOGE-USD 15%, PLTR 14% |  |
| Breezy | 2026-10-07T22:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-07T22:30 | 1 / 4 / 0 | MSTR 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.34 | +4.22% | 5 |
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| Stochastic reversion · 1h | XRP-USD | 2.19 | +4.46% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| RSI(14) reversion | ETHU | 1.93 | +0.48% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.69 | 5.69 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.54 | 2.54 | 30 | 46.7 | -9.27 | -2.91 | -13.84 | 116 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.16 | 2.16 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.57 | 1.57 | 0 | — | 2.17 | 1.07 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.26 | 1.26 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.09 | 1.09 | 18 | 5.6 | 11.49 | 1.58 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.63 | 0.63 | 4 | 50.0 | -4.52 | -1.56 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.59 | 0.59 | 0 | — | -2.78 | -1.12 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.51 | 0.51 | 28 | 39.3 | 5.12 | 2.44 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.77 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.83 | -0.17 | 0 | — | -4.16 | -2.03 | -5.14 | 1 |
| 16 | Hold BTC | benchmark | 99.71 | -0.29 | 0 | — | 29.31 | 3.52 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.34 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.78 | -1.22 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.46 | -1.54 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.46 | -1.54 | 68 | 23.5 | -20.89 | -6.03 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.40 | -1.60 | 34 | 5.9 | 7.47 | 1.03 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.03 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.46 | -2.54 | 61 | 59.0 | -10.50 | -2.09 | -11.21 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.35 | -2.65 | 0 | — | 12.75 | 2.08 | -7.19 | 1 |
| 25 | Connors RSI(2) · 1h | reversion | 97.03 | -2.96 | 77 | 44.2 | -15.42 | -5.66 | -17.97 | 231 |
| 26 | RSI(14) reversion · 1h | reversion | 96.98 | -3.02 | 16 | 43.8 | 3.49 | 1.00 | -6.57 | 114 |
| 27 | Daily: Momentum burst | daily | 96.76 | -3.24 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 28 | Agent | meta | 96.56 | -3.44 | 41 | 56.1 | -10.68 | -6.00 | -10.97 | 256 |
| 29 | Agent (rotation) | meta | 96.49 | -3.51 | 70 | 28.6 | 1.51 | 0.51 | -10.39 | 275 |
| 30 | Copy: Insider buying | copy | 96.45 | -3.55 | 11 | 54.5 | -17.32 | -3.20 | -21.08 | 74 |
| 31 | Z-score reversion · 1h | reversion | 96.40 | -3.60 | 28 | 46.4 | 0.38 | 0.20 | -8.60 | 159 |
| 32 | Candlestick reversal · 1h | reversion | 96.33 | -3.67 | 81 | 34.6 | -25.94 | -5.90 | -26.54 | 480 |
| 33 | Supertrend · 1h | trend | 95.75 | -4.25 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 34 | Parabolic SAR · 1h | trend | 95.47 | -4.53 | 80 | 21.2 | -6.67 | -0.78 | -20.87 | 294 |
| 35 | ADX DI cross · 1h | trend | 95.16 | -4.84 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.13 | -4.87 | 55 | 41.8 | -17.17 | -4.32 | -18.92 | 308 |
| 37 | Agent (ML meta-label) | meta | 94.95 | -5.05 | 286 | 15.7 | 1.08 | 0.34 | -12.94 | 361 |
| 38 | MACD cross · 1h | trend | 94.94 | -5.07 | 100 | 23.0 | -11.92 | -1.68 | -17.27 | 465 |
| 39 | Max aggression: 1-day momentum | meta | 94.88 | -5.12 | 8 | 37.5 | -21.09 | -1.02 | -37.31 | 42 |
| 40 | Agent (aggressive) | meta | 94.87 | -5.13 | 19 | 47.4 | -3.47 | -1.43 | -6.03 | 114 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.15 | 2.54 | -8.12 | 101 |
| 42 | RSI momentum · 1h | momentum | 94.15 | -5.85 | 51 | 3.9 | -3.94 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.95 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.87 | -6.13 | 104 | 21.2 | -17.38 | -5.32 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.54 | -6.46 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.52 | -6.48 | 63 | 30.2 | 7.62 | 1.13 | -12.06 | 290 |
| 47 | MFI reversion · 1h | reversion | 93.40 | -6.60 | 84 | 28.6 | -11.41 | -1.96 | -16.99 | 123 |
| 48 | Triple EMA stack · 1h | trend | 93.19 | -6.81 | 61 | 11.5 | -8.80 | -0.89 | -24.26 | 243 |
| 49 | Williams %R · 1h | reversion | 93.05 | -6.95 | 91 | 49.5 | -22.47 | -4.09 | -23.05 | 498 |
| 50 | Volume breakout · 1h | breakout | 92.74 | -7.26 | 44 | 15.9 | 6.77 | 1.10 | -12.60 | 122 |
| 51 | Opening range 15m | breakout | 92.19 | -7.81 | 121 | 19.8 | -19.15 | -5.59 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.14 | -8.86 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.14 | -8.86 | 90 | 11.1 | -4.63 | -0.42 | -18.86 | 340 |
| 54 | CCI reversion · 1h | reversion | 91.04 | -8.96 | 80 | 45.0 | -5.23 | -0.64 | -12.41 | 406 |
| 55 | VWAP momentum · 1h | momentum | 90.69 | -9.31 | 236 | 23.3 | -36.32 | -5.56 | -37.98 | 1267 |
| 56 | Three white soldiers | momentum | 90.57 | -9.43 | 105 | 19.0 | -48.67 | -24.33 | -48.79 | 584 |
| 57 | MACD zero-line · 1h | trend | 90.54 | -9.46 | 57 | 19.3 | -5.21 | -0.50 | -19.00 | 238 |
| 58 | OBV trend · 1h | momentum | 89.33 | -10.68 | 126 | 16.7 | -14.15 | -1.59 | -28.48 | 328 |
| 59 | Heikin-Ashi · 1h | trend | 88.96 | -11.04 | 124 | 25.0 | -31.95 | -5.49 | -35.56 | 690 |
| 60 | Keltner breakout · 1h | breakout | 88.96 | -11.04 | 39 | 17.9 | -9.09 | -1.02 | -23.68 | 226 |
| 61 | ROC + volume · 1h | momentum | 86.99 | -13.01 | 123 | 19.5 | -9.20 | -1.10 | -23.15 | 410 |
| 62 | Max aggression: 5-day momentum ⏸ | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.11 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.73 | -19.27 | 269 | 31.2 | -72.09 | -19.18 | -72.16 | 1430 |
| 64 | Squeeze breakout | breakout | 76.22 | -23.78 | 261 | 14.9 | -62.11 | -18.59 | -62.11 | 1215 |
| 65 | ROC + volume | momentum | 76.17 | -23.83 | 327 | 20.2 | -73.38 | -17.30 | -73.58 | 1651 |
| 66 | Donchian 55/20 | breakout | 74.53 | -25.47 | 265 | 17.0 | -68.44 | -14.91 | -68.65 | 1288 |
| 67 | VWAP reversion | reversion | 73.29 | -26.71 | 317 | 27.8 | -70.04 | -15.98 | -70.18 | 1393 |
| 68 | Volume breakout | breakout | 73.04 | -26.96 | 214 | 12.1 | -64.92 | -19.09 | -64.92 | 919 |
| 69 | EMA 20/50 cross | trend | 72.91 | -27.09 | 274 | 17.9 | -77.78 | -15.82 | -77.85 | 1464 |
| 70 | Supertrend | trend | 68.71 | -31.29 | 371 | 19.4 | -86.73 | -21.73 | -86.74 | 1927 |
| 71 | Keltner breakout | breakout | 66.70 | -33.30 | 359 | 12.8 | -85.17 | -29.58 | -85.17 | 1873 |
| 72 | MFI reversion | reversion | 66.66 | -33.34 | 401 | 21.7 | -87.53 | -29.95 | -87.55 | 2119 |
| 73 | Z-score reversion ⏸ | reversion | 66.43 | -33.57 | 408 | 24.8 | -85.33 | -24.44 | -85.35 | 2067 |
| 74 | Ichimoku | trend | 66.12 | -33.88 | 326 | 8.9 | -81.82 | -23.98 | -81.82 | 1737 |
| 75 | AI bee: Bizzy | ai | 65.70 | -34.30 | 642 | 8.6 | — | — | — | — |
| 76 | AI bee: Boozy | ai | 63.40 | -36.60 | 221 | 3.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 63.10 | -36.90 | 421 | 8.8 | -89.70 | -35.86 | -89.70 | 2113 |
| 78 | MACD zero-line | trend | 62.16 | -37.84 | 471 | 15.1 | -91.35 | -29.98 | -91.35 | 2355 |
| 79 | Donchian 20/10 | breakout | 61.69 | -38.31 | 506 | 17.6 | -91.02 | -26.83 | -91.02 | 2662 |
| 80 | RSI momentum | momentum | 60.37 | -39.63 | 472 | 16.3 | -90.34 | -25.94 | -90.34 | 2365 |
| 81 | Trend pullback | trend | 59.85 | -40.15 | 495 | 15.4 | -91.19 | -29.45 | -91.20 | 2335 |
| 82 | Triple EMA stack | trend | 58.91 | -41.09 | 518 | 15.1 | -93.23 | -31.41 | -93.23 | 2615 |
| 83 | Bollinger breakout | breakout | 57.79 | -42.21 | 522 | 13.6 | -93.84 | -34.52 | -93.84 | 2829 |
| 84 | Consensus | meta | 56.65 | -43.35 | 500 | 10.0 | -94.39 | -26.16 | -94.39 | 2685 |
| 85 | EMA 9/21 cross | trend | 53.99 | -46.01 | 649 | 15.9 | -97.35 | -33.99 | -97.35 | 3530 |
| 86 | Stochastic reversion ⏸ | reversion | 53.82 | -46.18 | 760 | 22.2 | -95.62 | -35.67 | -95.62 | 4038 |
| 87 | Bollinger reversion ⏸ | reversion | 53.42 | -46.58 | 706 | 16.9 | -95.76 | -34.73 | -95.76 | 3693 |
| 88 | Connors RSI(2) | reversion | 53.37 | -46.63 | 692 | 20.1 | -96.45 | -33.88 | -96.45 | 3608 |
| 89 | OBV trend | momentum | 50.70 | -49.30 | 752 | 14.5 | -96.40 | -38.15 | -96.40 | 3595 |
| 90 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -31.08 | -98.68 | 5347 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -38.15 | -99.30 | 5586 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -44.59 | -99.73 | 6133 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -40.64 | -97.34 | 3658 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -38.74 | -98.47 | 4682 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -42.11 | -99.51 | 6092 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -49.41 | -99.90 | 8250 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-07T22:30 | RSI momentum | sell | DOGE-USD | 15.01 | -0.11 | target is flat |
| 2026-10-07T22:30 | MACD zero-line | buy | DOGE-USD | 15.55 | — | entry signal |
| 2026-10-07T22:29 | AI bee: Bizzy | buy | DOGE-USD | 9.84 | — | Jev: buy (buy p=0.60) |
| 2026-10-07T22:25 | OBV trend | buy | ETH-USD | 12.39 | — | entry signal |
| 2026-10-07T22:25 | RSI momentum | buy | DOGE-USD | 15.12 | — | entry signal |
| 2026-10-07T22:25 | Supertrend | buy | DOGE-USD | 6.73 | — | entry signal |
| 2026-10-07T22:25 | EMA 9/21 cross | buy | DOGE-USD | 10.59 | — | entry signal |
| 2026-10-07T22:11 | AI bee: Bizzy | sell | SOL-USD | 9.16 | -0.04 | Jev: sell (sell p=0.63) after 11 min |
| 2026-10-07T22:05 | VWAP reversion | buy | SOL-USD | 3.65 | — | entry |
| 2026-10-07T22:05 | VWAP reversion | sell | BTC-USD | 3.65 | -0.03 | rebalance down |
| 2026-10-07T22:00 | AI bee: Bizzy | buy | SOL-USD | 9.20 | — | Jev: buy (buy p=0.56) |
| 2026-10-07T22:00 | Candlestick reversal · 1h | sell | DOGE-USD | 19.21 | -0.18 | exit signal |
| 2026-10-07T22:00 | RSI(14) reversion | buy | BTC-USD | 2.75 | — | entry signal |
| 2026-10-07T21:55 | Agent | sell | XRP-USD | 18.98 | -0.42 | selected signal exited |
| 2026-10-07T21:55 | MFI reversion · 1h | sell | XRP-USD | 13.27 | -0.30 | stop-loss |
| 2026-10-07T21:55 | Williams %R · 1h | buy | ETH-USD | 11.62 | — | entry |
| 2026-10-07T21:55 | Williams %R · 1h | sell | XRP-USD | 13.10 | -0.29 | stop-loss |
| 2026-10-07T21:55 | Stochastic reversion · 1h | sell | XRP-USD | 6.43 | -0.09 | stop-loss |
| 2026-10-07T21:50 | MFI reversion | buy | SOL-USD | 2.34 | — | entry signal |
| 2026-10-07T21:50 | MFI reversion | buy | DOGE-USD | 16.67 | — | entry signal |
| 2026-10-07T21:50 | VWAP reversion | buy | ETH-USD | 6.57 | — | rebalance up |
| 2026-10-07T21:50 | VWAP reversion | sell | XRP-USD | 6.57 | -0.13 | stop-loss |
| 2026-10-07T21:45 | VWAP reversion | buy | DOGE-USD | 2.94 | — | rebalance up |
| 2026-10-07T21:45 | VWAP reversion | buy | BTC-USD | 3.69 | — | rebalance up |
| 2026-10-07T21:45 | VWAP reversion | sell | SOL-USD | 6.63 | -0.09 | stop-loss |
| 2026-10-07T21:45 | Supertrend | sell | ETH-USD | 6.73 | -0.05 | exit signal |
| 2026-10-07T21:40 | OBV trend | sell | BTC-USD | 12.39 | -0.12 | exit signal |
| 2026-10-07T21:40 | Supertrend | buy | ETH-USD | 6.78 | — | entry |
| 2026-10-07T21:40 | Supertrend | sell | BTC-USD | 6.78 | -0.07 | exit signal |
| 2026-10-07T21:40 | EMA 9/21 cross | sell | ETH-USD | 10.59 | -0.06 | exit signal |
| 2026-10-07T21:35 | Donchian 20/10 | sell | ETH-USD | 3.84 | -0.02 | exit signal |
| 2026-10-07T21:35 | Donchian 20/10 | sell | DOGE-USD | 7.62 | -0.07 | stop-loss |
| 2026-10-07T21:35 | RSI momentum | sell | ETH-USD | 15.06 | -0.10 | exit signal |
| 2026-10-07T21:35 | EMA 20/50 cross | buy | ETH-USD | 17.91 | — | entry |
| 2026-10-07T21:35 | EMA 20/50 cross | sell | BTC-USD | 17.91 | -0.17 | exit signal |
| 2026-10-07T21:35 | EMA 9/21 cross | buy | ETH-USD | 10.66 | — | entry |
| 2026-10-07T21:35 | EMA 9/21 cross | sell | DOGE-USD | 10.66 | -0.11 | exit signal |
| 2026-10-07T21:30 | RSI momentum | buy | ETH-USD | 13.50 | — | rebalance up |
| 2026-10-07T21:30 | RSI momentum | sell | DOGE-USD | 13.99 | -0.11 | exit signal |
| 2026-10-07T21:25 | Squeeze breakout | sell | DOGE-USD | 19.03 | -0.12 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-09 22:30:05.000136+00:00 -> 2026-10-07 22:40:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
