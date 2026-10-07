# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-07T21:03:05.000154+00:00 · 14809 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.80 (-3.19%)

Closed trades 40, win rate 57.5%, fees £1.76, max drawdown -3.71%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.44 | +0.07 |
| DOGE-USD | 19.37 | -0.04 |
| ETHU | 19.46 | +0.07 |
| XRP-USD | 19.18 | -0.22 |

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

Today: 22509 decisions in 2466 calls, $0.2875 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-07T21:03 | 0 / 3 / 2 | PLTR 14% |  |
| Breezy | 2026-10-07T21:03 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-07T21:03 | 1 / 3 / 1 | MSTR 68% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.70 | 5.70 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.64 | 2.64 | 30 | 46.7 | -9.19 | -2.88 | -13.84 | 116 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.17 | 2.17 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.58 | 1.58 | 0 | — | 2.17 | 1.07 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.28 | 1.27 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.10 | 1.10 | 18 | 5.6 | 11.49 | 1.58 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.64 | 0.64 | 4 | 50.0 | -4.52 | -1.56 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.60 | 0.60 | 0 | — | -2.78 | -1.12 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.52 | 0.52 | 28 | 39.3 | 5.12 | 2.44 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.77 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Hold BTC | benchmark | 99.87 | -0.13 | 0 | — | 29.20 | 3.52 | -8.68 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.82 | -0.18 | 0 | — | -4.19 | -2.04 | -5.14 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.34 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.79 | -1.21 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.48 | -1.52 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.48 | -1.52 | 68 | 23.5 | -20.89 | -6.03 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.41 | -1.59 | 34 | 5.9 | 7.21 | 1.00 | -19.45 | 135 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.03 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.58 | -2.42 | 60 | 60.0 | -10.48 | -2.09 | -11.21 | 341 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.36 | -2.64 | 0 | — | 12.75 | 2.08 | -7.19 | 1 |
| 25 | RSI(14) reversion · 1h | reversion | 97.17 | -2.83 | 16 | 43.8 | 3.49 | 1.00 | -6.57 | 113 |
| 26 | Connors RSI(2) · 1h | reversion | 97.05 | -2.95 | 77 | 44.2 | -15.42 | -5.66 | -17.97 | 231 |
| 27 | Agent | meta | 96.80 | -3.19 | 40 | 57.5 | -10.35 | -5.94 | -10.86 | 253 |
| 28 | Daily: Momentum burst | daily | 96.77 | -3.23 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 29 | Candlestick reversal · 1h | reversion | 96.59 | -3.41 | 80 | 35.0 | -25.78 | -5.90 | -26.51 | 479 |
| 30 | Z-score reversion · 1h | reversion | 96.55 | -3.45 | 28 | 46.4 | 0.52 | 0.23 | -8.60 | 159 |
| 31 | Agent (rotation) | meta | 96.53 | -3.48 | 70 | 28.6 | 1.54 | 0.52 | -10.39 | 275 |
| 32 | Copy: Insider buying | copy | 96.47 | -3.53 | 11 | 54.5 | -17.32 | -3.20 | -21.08 | 74 |
| 33 | Supertrend · 1h | trend | 95.76 | -4.24 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 34 | Parabolic SAR · 1h | trend | 95.48 | -4.52 | 80 | 21.2 | -6.67 | -0.78 | -20.87 | 294 |
| 35 | ADX DI cross · 1h | trend | 95.17 | -4.83 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.14 | -4.86 | 55 | 41.8 | -17.00 | -4.27 | -18.92 | 309 |
| 37 | Agent (aggressive) | meta | 94.97 | -5.03 | 19 | 47.4 | -4.89 | -2.04 | -6.03 | 114 |
| 38 | MACD cross · 1h | trend | 94.96 | -5.04 | 100 | 23.0 | -11.86 | -1.67 | -17.27 | 465 |
| 39 | Agent (ML meta-label) | meta | 94.96 | -5.04 | 286 | 15.7 | 2.57 | 0.61 | -12.24 | 368 |
| 40 | Max aggression: 1-day momentum | meta | 94.89 | -5.11 | 8 | 37.5 | -21.09 | -1.02 | -37.31 | 42 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.15 | 2.54 | -8.12 | 101 |
| 42 | RSI momentum · 1h | momentum | 94.16 | -5.84 | 51 | 3.9 | -3.94 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.95 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.88 | -6.12 | 104 | 21.2 | -17.38 | -5.32 | -17.84 | 562 |
| 45 | MFI reversion · 1h | reversion | 93.65 | -6.35 | 83 | 28.9 | -11.18 | -1.92 | -16.99 | 123 |
| 46 | Ichimoku · 1h | trend | 93.54 | -6.46 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 47 | Bollinger breakout · 1h | breakout | 93.52 | -6.47 | 63 | 30.2 | 7.63 | 1.13 | -12.06 | 290 |
| 48 | Williams %R · 1h | reversion | 93.30 | -6.70 | 90 | 50.0 | -22.32 | -4.07 | -23.05 | 498 |
| 49 | Triple EMA stack · 1h | trend | 93.20 | -6.80 | 61 | 11.5 | -8.85 | -0.90 | -24.26 | 244 |
| 50 | Volume breakout · 1h | breakout | 92.74 | -7.26 | 44 | 15.9 | 6.77 | 1.10 | -12.60 | 122 |
| 51 | Opening range 15m | breakout | 92.20 | -7.80 | 121 | 19.8 | -19.15 | -5.59 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.15 | -8.85 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.15 | -8.85 | 90 | 11.1 | -4.65 | -0.43 | -18.86 | 340 |
| 54 | CCI reversion · 1h | reversion | 91.13 | -8.87 | 80 | 45.0 | -5.10 | -0.62 | -12.41 | 406 |
| 55 | VWAP momentum · 1h | momentum | 90.70 | -9.30 | 236 | 23.3 | -36.32 | -5.56 | -37.98 | 1267 |
| 56 | Three white soldiers | momentum | 90.57 | -9.43 | 105 | 19.0 | -48.67 | -24.33 | -48.79 | 584 |
| 57 | MACD zero-line · 1h | trend | 90.54 | -9.46 | 57 | 19.3 | -5.21 | -0.50 | -19.00 | 238 |
| 58 | OBV trend · 1h | momentum | 89.33 | -10.67 | 126 | 16.7 | -14.80 | -1.68 | -28.48 | 330 |
| 59 | Heikin-Ashi · 1h | trend | 88.96 | -11.04 | 124 | 25.0 | -32.06 | -5.51 | -35.56 | 693 |
| 60 | Keltner breakout · 1h | breakout | 88.96 | -11.04 | 39 | 17.9 | -8.83 | -0.98 | -23.68 | 226 |
| 61 | ROC + volume · 1h | momentum | 87.00 | -13.00 | 123 | 19.5 | -9.06 | -1.08 | -23.15 | 410 |
| 62 | Max aggression: 5-day momentum ⏸ | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.11 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.74 | -19.25 | 269 | 31.2 | -72.14 | -19.25 | -72.22 | 1429 |
| 64 | Squeeze breakout | breakout | 76.31 | -23.69 | 260 | 15.0 | -62.07 | -18.57 | -62.09 | 1215 |
| 65 | ROC + volume | momentum | 76.17 | -23.83 | 327 | 20.2 | -73.38 | -17.30 | -73.58 | 1651 |
| 66 | Donchian 55/20 | breakout | 74.54 | -25.46 | 265 | 17.0 | -68.44 | -14.91 | -68.65 | 1288 |
| 67 | VWAP reversion | reversion | 73.52 | -26.48 | 315 | 27.9 | -69.97 | -16.14 | -70.04 | 1394 |
| 68 | EMA 20/50 cross | trend | 73.05 | -26.95 | 273 | 17.9 | -77.83 | -15.83 | -77.86 | 1467 |
| 69 | Volume breakout | breakout | 73.04 | -26.96 | 214 | 12.1 | -64.92 | -19.09 | -64.92 | 919 |
| 70 | Supertrend | trend | 68.83 | -31.17 | 369 | 19.5 | -86.67 | -21.61 | -86.68 | 1926 |
| 71 | Keltner breakout | breakout | 66.71 | -33.30 | 359 | 12.8 | -85.21 | -29.59 | -85.21 | 1874 |
| 72 | MFI reversion | reversion | 66.67 | -33.33 | 401 | 21.7 | -87.56 | -30.06 | -87.56 | 2118 |
| 73 | Z-score reversion ⏸ | reversion | 66.43 | -33.57 | 408 | 24.8 | -85.28 | -24.50 | -85.30 | 2064 |
| 74 | Ichimoku | trend | 66.12 | -33.88 | 326 | 8.9 | -81.86 | -23.99 | -81.87 | 1738 |
| 75 | AI bee: Bizzy | ai | 65.79 | -34.21 | 641 | 8.6 | — | — | — | — |
| 76 | AI bee: Boozy | ai | 63.40 | -36.60 | 221 | 3.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 63.11 | -36.89 | 421 | 8.8 | -89.68 | -35.92 | -89.68 | 2112 |
| 78 | MACD zero-line | trend | 62.21 | -37.79 | 471 | 15.1 | -91.40 | -30.04 | -91.40 | 2358 |
| 79 | Donchian 20/10 | breakout | 61.78 | -38.22 | 504 | 17.7 | -91.01 | -26.77 | -91.02 | 2663 |
| 80 | RSI momentum | momentum | 60.67 | -39.33 | 469 | 16.4 | -90.40 | -26.02 | -90.41 | 2369 |
| 81 | Trend pullback | trend | 59.85 | -40.15 | 495 | 15.4 | -91.36 | -29.72 | -91.37 | 2343 |
| 82 | Triple EMA stack | trend | 58.92 | -41.08 | 518 | 15.1 | -93.20 | -31.32 | -93.20 | 2614 |
| 83 | Bollinger breakout | breakout | 57.86 | -42.14 | 521 | 13.6 | -93.84 | -34.52 | -93.85 | 2830 |
| 84 | Consensus | meta | 56.71 | -43.29 | 499 | 10.0 | -94.37 | -26.13 | -94.37 | 2683 |
| 85 | EMA 9/21 cross | trend | 54.19 | -45.81 | 647 | 15.9 | -97.36 | -33.98 | -97.36 | 3533 |
| 86 | Stochastic reversion ⏸ | reversion | 53.82 | -46.18 | 760 | 22.2 | -95.61 | -36.19 | -95.61 | 4037 |
| 87 | Bollinger reversion ⏸ | reversion | 53.42 | -46.58 | 706 | 16.9 | -95.75 | -35.18 | -95.76 | 3693 |
| 88 | Connors RSI(2) | reversion | 53.38 | -46.62 | 692 | 20.1 | -96.50 | -34.10 | -96.50 | 3616 |
| 89 | OBV trend | momentum | 50.80 | -49.20 | 751 | 14.5 | -96.40 | -38.03 | -96.41 | 3596 |
| 90 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -31.25 | -98.69 | 5351 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -38.40 | -99.30 | 5587 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -44.71 | -99.73 | 6134 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -40.61 | -97.38 | 3663 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -39.26 | -98.47 | 4685 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -42.55 | -99.51 | 6092 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -49.66 | -99.90 | 8249 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-07T21:00 | Consensus | buy | DOGE-USD | 14.19 | — | entry |
| 2026-10-07T21:00 | Z-score reversion · 1h | buy | XRP-USD | 7.29 | — | entry signal |
| 2026-10-07T21:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 24.31 | — | entry signal |
| 2026-10-07T20:55 | EMA 9/21 cross | buy | DOGE-USD | 10.77 | — | entry |
| 2026-10-07T20:55 | EMA 9/21 cross | sell | BTC-USD | 10.77 | -0.06 | exit signal |
| 2026-10-07T20:45 | MACD zero-line | sell | ETH-USD | 15.47 | -0.13 | exit signal |
| 2026-10-07T20:40 | Keltner breakout | sell | ETH-USD | 16.61 | -0.15 | stop-loss |
| 2026-10-07T20:40 | Bollinger breakout | sell | ETH-USD | 3.38 | -0.03 | stop-loss |
| 2026-10-07T20:40 | Donchian 20/10 | buy | DOGE-USD | 3.84 | — | rebalance up |
| 2026-10-07T20:40 | Donchian 20/10 | sell | BTC-USD | 3.84 | -0.02 | stop-loss |
| 2026-10-07T20:40 | RSI momentum | buy | DOGE-USD | 9.03 | — | rebalance up |
| 2026-10-07T20:40 | RSI momentum | sell | BTC-USD | 9.03 | -0.07 | exit signal |
| 2026-10-07T20:37 | Consensus | sell | DOGE-USD | 14.10 | -0.11 | target is flat |
| 2026-10-07T20:37 | Three white soldiers | sell | DOGE-USD | 22.51 | -0.18 | exit signal |
| 2026-10-07T20:37 | Bollinger breakout | buy | DOGE-USD | 10.21 | — | rebalance up |
| 2026-10-07T20:37 | Bollinger breakout | sell | BTC-USD | 10.21 | -0.08 | exit signal |
| 2026-10-07T20:37 | Ichimoku | sell | BTC-USD | 16.44 | -0.13 | exit signal |
| 2026-10-07T20:37 | EMA 9/21 cross | buy | BTC-USD | 5.40 | — | rebalance up |
| 2026-10-07T20:37 | EMA 9/21 cross | sell | SOL-USD | 5.40 | -0.04 | exit signal |
| 2026-10-07T20:34 | Agent (rotation) | buy | DOGE-USD | 8.05 | — | following Stochastic reversion · 1h |
| 2026-10-07T20:34 | Consensus | buy | DOGE-USD | 14.22 | — | entry |
| 2026-10-07T20:34 | MFI reversion · 1h | buy | SOL-USD | 13.41 | — | entry |
| 2026-10-07T20:34 | MFI reversion · 1h | buy | ETH-USD | 13.41 | — | entry |
| 2026-10-07T20:34 | MFI reversion · 1h | sell | XRP-USD | 9.85 | -0.14 | rebalance down |
| 2026-10-07T20:34 | MFI reversion · 1h | sell | DOGE-USD | 10.07 | -0.05 | rebalance down |
| 2026-10-07T20:34 | MFI reversion · 1h | sell | BTC-USD | 10.08 | -0.04 | rebalance down |
| 2026-10-07T20:34 | CCI reversion · 1h | buy | BTC-USD | 15.21 | — | entry |
| 2026-10-07T20:34 | CCI reversion · 1h | sell | ETH-USD | 7.84 | -0.02 | rebalance down |
| 2026-10-07T20:34 | CCI reversion · 1h | sell | DOGE-USD | 7.80 | -0.04 | rebalance down |
| 2026-10-07T20:34 | Stochastic reversion · 1h | buy | XRP-USD | 6.52 | — | entry |
| 2026-10-07T20:34 | Stochastic reversion · 1h | buy | DOGE-USD | 6.52 | — | entry |
| 2026-10-07T20:34 | Stochastic reversion · 1h | sell | SOL-USD | 9.70 | -0.05 | rebalance down |
| 2026-10-07T20:34 | Stochastic reversion · 1h | sell | ETH-USD | 16.32 | -0.00 | target is flat |
| 2026-10-07T20:34 | Stochastic reversion · 1h | sell | BTC-USD | 9.80 | -0.02 | rebalance down |
| 2026-10-07T20:34 | VWAP reversion · 1h | buy | DOGE-USD | 25.69 | — | entry |
| 2026-10-07T20:34 | Z-score reversion · 1h | buy | SOL-USD | 16.13 | — | entry |
| 2026-10-07T20:34 | Z-score reversion · 1h | buy | ETH-USD | 16.13 | — | entry |
| 2026-10-07T20:34 | Z-score reversion · 1h | sell | DOGE-USD | 8.05 | -0.04 | rebalance down |
| 2026-10-07T20:34 | Z-score reversion · 1h | sell | BTC-USD | 8.06 | -0.03 | rebalance down |
| 2026-10-07T20:34 | RSI(14) reversion · 1h | buy | ETH-USD | 24.36 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-09 21:03:05.000154+00:00 -> 2026-10-07 21:13:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
