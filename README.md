# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T01:30:05.000165+00:00 · 15030 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.66 (-3.35%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.45 | +0.07 |
| ETHU | 19.46 | +0.08 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-07 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, BORR 12%, PSUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 1170 decisions in 234 calls, $0.0164 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T01:30 | 4 / 1 / 0 | PLTR 14% |  |
| Breezy | 2026-10-08T01:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T01:30 | 3 / 2 / 0 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| VWAP reversion | MSFT | 1.95 | +0.75% | 3 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.74 | 5.74 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.21 | 2.21 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.61 | 1.61 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.13 | 1.13 | 18 | 5.6 | 11.49 | 1.57 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.67 | 0.67 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.64 | 0.64 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.52 | 0.52 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.88 | -0.12 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Hold BTC | benchmark | 99.73 | -0.27 | 0 | — | 29.14 | 3.49 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.83 | -1.18 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.51 | -1.49 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.51 | -1.49 | 68 | 23.5 | -20.89 | -5.98 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.43 | -1.57 | 34 | 5.9 | 7.47 | 1.02 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.55 | -2.46 | 62 | 58.1 | -10.45 | -2.07 | -11.21 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.39 | -2.60 | 0 | — | 12.75 | 2.06 | -7.19 | 1 |
| 25 | RSI(14) reversion · 1h | reversion | 97.36 | -2.64 | 16 | 43.8 | 3.90 | 1.10 | -6.57 | 115 |
| 26 | Connors RSI(2) · 1h | reversion | 97.08 | -2.92 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 27 | Daily: Momentum burst | daily | 96.78 | -3.22 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 28 | Z-score reversion · 1h | reversion | 96.72 | -3.28 | 28 | 46.4 | 0.67 | 0.26 | -8.60 | 159 |
| 29 | Agent | meta | 96.66 | -3.35 | 42 | 57.1 | -10.92 | -5.97 | -11.25 | 254 |
| 30 | Candlestick reversal · 1h | reversion | 96.51 | -3.49 | 81 | 34.6 | -25.81 | -5.84 | -26.54 | 480 |
| 31 | Copy: Insider buying | copy | 96.50 | -3.50 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 32 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 0.35 | 0.19 | -10.39 | 279 |
| 33 | Supertrend · 1h | trend | 95.79 | -4.21 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 34 | Parabolic SAR · 1h | trend | 95.50 | -4.50 | 80 | 21.2 | -6.67 | -0.77 | -20.87 | 294 |
| 35 | ADX DI cross · 1h | trend | 95.19 | -4.81 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.16 | -4.84 | 55 | 41.8 | -17.15 | -4.28 | -18.92 | 308 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -4.33 | -1.59 | -6.03 | 114 |
| 38 | MACD cross · 1h | trend | 94.98 | -5.02 | 100 | 23.0 | -11.72 | -1.64 | -17.27 | 466 |
| 39 | Agent (ML meta-label) | meta | 94.97 | -5.03 | 287 | 15.7 | 0.62 | 0.25 | -11.87 | 360 |
| 40 | Max aggression: 1-day momentum | meta | 94.93 | -5.07 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 14.94 | 2.49 | -8.12 | 103 |
| 42 | RSI momentum · 1h | momentum | 94.19 | -5.81 | 51 | 3.9 | -3.57 | -0.35 | -18.16 | 221 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.91 | -6.09 | 104 | 21.2 | -17.38 | -5.27 | -17.84 | 562 |
| 45 | MFI reversion · 1h | reversion | 93.66 | -6.34 | 84 | 28.6 | -11.19 | -1.90 | -16.99 | 123 |
| 46 | Ichimoku · 1h | trend | 93.56 | -6.44 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 47 | Bollinger breakout · 1h | breakout | 93.54 | -6.46 | 63 | 30.2 | 7.56 | 1.12 | -12.06 | 290 |
| 48 | Triple EMA stack · 1h | trend | 93.22 | -6.78 | 61 | 11.5 | -8.69 | -0.87 | -24.26 | 242 |
| 49 | Williams %R · 1h | reversion | 93.18 | -6.83 | 93 | 49.5 | -22.44 | -4.05 | -23.05 | 499 |
| 50 | Volume breakout · 1h | breakout | 92.75 | -7.25 | 44 | 15.9 | 6.77 | 1.09 | -12.60 | 122 |
| 51 | Opening range 15m | breakout | 92.23 | -7.77 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | CCI reversion · 1h | reversion | 91.24 | -8.76 | 80 | 45.0 | -5.24 | -0.64 | -12.41 | 406 |
| 53 | Donchian 20/10 · 1h | breakout | 91.18 | -8.82 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 54 | EMA 9/21 cross · 1h | trend | 91.17 | -8.83 | 90 | 11.1 | -4.63 | -0.42 | -18.86 | 340 |
| 55 | VWAP momentum · 1h | momentum | 90.69 | -9.31 | 236 | 23.3 | -36.52 | -5.56 | -37.98 | 1272 |
| 56 | MACD zero-line · 1h | trend | 90.56 | -9.44 | 57 | 19.3 | -5.21 | -0.50 | -19.00 | 238 |
| 57 | Three white soldiers | momentum | 90.29 | -9.71 | 107 | 18.7 | -48.55 | -24.08 | -48.55 | 583 |
| 58 | OBV trend · 1h | momentum | 89.34 | -10.66 | 126 | 16.7 | -14.14 | -1.57 | -28.48 | 328 |
| 59 | Keltner breakout · 1h | breakout | 88.97 | -11.03 | 39 | 17.9 | -9.49 | -1.07 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.94 | -11.06 | 124 | 25.0 | -31.80 | -5.41 | -35.56 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.02 | -12.98 | 123 | 19.5 | -8.98 | -1.06 | -23.15 | 409 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.76 | -19.24 | 270 | 31.1 | -72.07 | -18.82 | -72.10 | 1428 |
| 64 | ROC + volume | momentum | 76.19 | -23.81 | 327 | 20.2 | -73.39 | -17.08 | -73.59 | 1652 |
| 65 | Squeeze breakout | breakout | 75.87 | -24.13 | 263 | 14.8 | -62.29 | -18.49 | -62.31 | 1218 |
| 66 | Donchian 55/20 | breakout | 74.35 | -25.65 | 266 | 16.9 | -68.62 | -14.85 | -68.82 | 1293 |
| 67 | VWAP reversion | reversion | 73.19 | -26.81 | 321 | 27.4 | -70.16 | -15.96 | -70.18 | 1393 |
| 68 | EMA 20/50 cross | trend | 73.03 | -26.97 | 274 | 17.9 | -77.80 | -15.65 | -77.92 | 1467 |
| 69 | Volume breakout | breakout | 72.78 | -27.22 | 216 | 12.0 | -64.79 | -18.92 | -64.79 | 917 |
| 70 | Supertrend | trend | 68.79 | -31.21 | 371 | 19.4 | -86.61 | -21.19 | -86.78 | 1926 |
| 71 | MFI reversion | reversion | 66.65 | -33.35 | 403 | 21.8 | -87.54 | -29.20 | -87.54 | 2119 |
| 72 | Z-score reversion | reversion | 66.43 | -33.57 | 408 | 24.8 | -85.21 | -23.75 | -85.21 | 2062 |
| 73 | Keltner breakout | breakout | 66.20 | -33.80 | 364 | 12.6 | -85.29 | -29.31 | -85.30 | 1878 |
| 74 | Ichimoku | trend | 66.19 | -33.81 | 326 | 8.9 | -81.64 | -23.40 | -81.69 | 1734 |
| 75 | AI bee: Bizzy | ai | 65.32 | -34.68 | 649 | 8.5 | — | — | — | — |
| 76 | AI bee: Boozy | ai | 63.06 | -36.94 | 224 | 3.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 63.03 | -36.97 | 422 | 8.8 | -89.57 | -34.70 | -89.59 | 2106 |
| 78 | MACD zero-line | trend | 61.75 | -38.25 | 477 | 14.9 | -91.41 | -29.57 | -91.41 | 2359 |
| 79 | Donchian 20/10 | breakout | 61.72 | -38.28 | 506 | 17.6 | -90.94 | -26.20 | -90.98 | 2662 |
| 80 | RSI momentum | momentum | 60.34 | -39.66 | 473 | 16.3 | -90.39 | -25.53 | -90.40 | 2371 |
| 81 | Trend pullback | trend | 59.86 | -40.14 | 495 | 15.4 | -91.13 | -28.58 | -91.13 | 2331 |
| 82 | Triple EMA stack | trend | 58.94 | -41.06 | 518 | 15.1 | -93.17 | -30.57 | -93.20 | 2615 |
| 83 | Bollinger breakout | breakout | 57.61 | -42.39 | 527 | 13.5 | -93.84 | -34.00 | -93.84 | 2831 |
| 84 | Consensus | meta | 55.98 | -44.02 | 507 | 9.9 | -94.45 | -25.89 | -94.45 | 2691 |
| 85 | EMA 9/21 cross | trend | 54.08 | -45.92 | 649 | 15.9 | -97.32 | -33.06 | -97.34 | 3527 |
| 86 | Stochastic reversion | reversion | 53.82 | -46.18 | 760 | 22.2 | -95.62 | -34.47 | -95.62 | 4037 |
| 87 | Bollinger reversion | reversion | 53.42 | -46.58 | 706 | 16.9 | -95.74 | -33.63 | -95.74 | 3691 |
| 88 | Connors RSI(2) | reversion | 53.35 | -46.65 | 692 | 20.1 | -96.39 | -32.60 | -96.40 | 3600 |
| 89 | OBV trend | momentum | 50.67 | -49.33 | 753 | 14.5 | -96.39 | -37.00 | -96.40 | 3596 |
| 90 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -30.40 | -98.65 | 5333 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -36.86 | -99.30 | 5587 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.09 | -99.73 | 6133 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -39.76 | -97.37 | 3663 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -37.29 | -98.46 | 4678 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.35 | -99.51 | 6090 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.36 | -99.90 | 8256 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T01:25 | Consensus | sell | SOL-USD | 13.45 | -0.13 | target is flat |
| 2026-10-08T01:25 | Consensus | sell | ETH-USD | 13.94 | -0.11 | target is flat |
| 2026-10-08T01:25 | Connors RSI(2) | buy | DOGE-USD | 13.34 | — | entry signal |
| 2026-10-08T01:25 | Volume breakout | sell | ETH-USD | 18.09 | -0.15 | exit signal |
| 2026-10-08T01:25 | Squeeze breakout | sell | SOL-USD | 18.85 | -0.18 | stop-loss |
| 2026-10-08T01:25 | Keltner breakout | buy | XRP-USD | 16.58 | — | entry |
| 2026-10-08T01:25 | Keltner breakout | sell | SOL-USD | 4.52 | -0.04 | stop-loss |
| 2026-10-08T01:25 | Keltner breakout | sell | ETH-USD | 16.50 | -0.13 | stop-loss |
| 2026-10-08T01:25 | Keltner breakout | sell | DOGE-USD | 16.60 | -0.06 | stop-loss |
| 2026-10-08T01:25 | Bollinger breakout | buy | XRP-USD | 14.42 | — | entry |
| 2026-10-08T01:25 | Bollinger breakout | sell | ETH-USD | 2.34 | -0.02 | stop-loss |
| 2026-10-08T01:25 | Bollinger breakout | sell | DOGE-USD | 14.40 | -0.04 | stop-loss |
| 2026-10-08T01:25 | RSI momentum | buy | DOGE-USD | 3.34 | — | entry |
| 2026-10-08T01:25 | RSI momentum | sell | BTC-USD | 3.34 | -0.03 | stop-loss |
| 2026-10-08T01:25 | MACD zero-line | sell | BTC-USD | 15.34 | -0.12 | stop-loss |
| 2026-10-08T01:20 | AI bee: Boozy | sell | ETH-USD | 19.65 | -0.13 | Jev: sell |
| 2026-10-08T01:15 | Three white soldiers | sell | BTC-USD | 22.47 | -0.14 | exit signal |
| 2026-10-08T01:05 | AI bee: Boozy | buy | ETH-USD | 19.78 | — | Jev: buy (buy p=0.69) |
| 2026-10-08T01:05 | Agent (ML meta-label) | sell | SOL-USD | 4.23 | -0.01 | selected signal exited |
| 2026-10-08T01:05 | Consensus | buy | SOL-USD | 13.58 | — | entry |
| 2026-10-08T01:05 | Consensus | buy | ETH-USD | 14.05 | — | entry |
| 2026-10-08T01:05 | Volume breakout | buy | ETH-USD | 18.23 | — | entry signal |
| 2026-10-08T01:05 | Squeeze breakout | buy | XRP-USD | 19.03 | — | entry signal |
| 2026-10-08T01:05 | Squeeze breakout | buy | SOL-USD | 19.03 | — | entry signal |
| 2026-10-08T01:05 | Keltner breakout | buy | SOL-USD | 4.57 | — | entry signal |
| 2026-10-08T01:05 | Keltner breakout | buy | ETH-USD | 16.63 | — | entry signal |
| 2026-10-08T01:05 | Bollinger breakout | buy | ETH-USD | 2.36 | — | entry signal |
| 2026-10-08T01:05 | Donchian 55/20 | buy | ETH-USD | 18.62 | — | entry signal |
| 2026-10-08T01:05 | RSI momentum | buy | BTC-USD | 3.37 | — | entry |
| 2026-10-08T01:05 | RSI momentum | sell | SOL-USD | 3.02 | -0.01 | rebalance down |
| 2026-10-08T01:01 | Agent (ML meta-label) | buy | SOL-USD | 4.24 | — | entry |
| 2026-10-08T01:00 | Agent (rotation) | sell | XRP-USD | 6.42 | -0.01 | selected signal exited |
| 2026-10-08T01:00 | Agent (rotation) | sell | SOL-USD | 6.42 | -0.02 | selected signal exited |
| 2026-10-08T01:00 | Agent (rotation) | sell | ETH-USD | 8.02 | -0.03 | selected signal exited |
| 2026-10-08T01:00 | Agent (rotation) | sell | DOGE-USD | 8.04 | -0.01 | selected signal exited |
| 2026-10-08T01:00 | Consensus | sell | DOGE-USD | 13.99 | -0.09 | target is flat |
| 2026-10-08T01:00 | Agent (aggressive) | sell | DOGE-USD | 47.54 | 0.01 | selected signal exited |
| 2026-10-08T01:00 | Agent | sell | DOGE-USD | 19.41 | 0.01 | selected signal exited |
| 2026-10-08T01:00 | Williams %R · 1h | buy | XRP-USD | 11.84 | — | rebalance up |
| 2026-10-08T01:00 | Williams %R · 1h | sell | ETH-USD | 11.59 | -0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 01:30:05.000165+00:00 -> 2026-10-08 01:40:05.000165+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
