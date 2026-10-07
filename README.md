# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-07T14:25:05.000188+00:00 · 14697 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.92 (-3.08%)

Closed trades 40, win rate 57.5%, fees £1.62, max drawdown -3.52%.

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

### Market regime (QQQ, 2026-10-06)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.15 · VIX 15.01 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.5, MSTR 7.5, AMD 7.3, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 14118 decisions in 2130 calls, $0.1885 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-07T14:25 | 2 / 25 / 3 | SOXL 14% |  |
| Breezy | 2026-10-07T14:25 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-07T14:25 | 3 / 25 / 2 | MSTR 68% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 104.49 | 4.50 | 0 | — | -1.53 | -0.16 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -9.17 | -2.87 | -13.93 | 113 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 101.85 | 1.85 | 0 | — | -0.00 | 0.04 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.40 | 1.40 | 0 | — | 2.74 | 1.30 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.05 | 1.05 | 0 | — | 0.67 | 0.44 | -3.66 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 100.74 | 0.74 | 28 | 39.3 | 5.29 | 2.51 | -1.52 | 83 |
| 9 | Copy: Hedge-fund gurus (GURU) | copy | 100.49 | 0.49 | 0 | — | -3.44 | -1.67 | -5.14 | 1 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.44 | 0.44 | 0 | — | -2.61 | -1.00 | -7.65 | 1 |
| 11 | Donchian 55/20 · 1h | breakout | 100.38 | 0.38 | 17 | 0.0 | 10.60 | 1.47 | -16.96 | 109 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.77 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -6.02 | -2.08 | -9.74 | 23 |
| 16 | Hold BTC | benchmark | 99.67 | -0.33 | 0 | — | 28.01 | 3.38 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.34 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.58 | -1.42 | 0 | — | -0.52 | -0.11 | -5.18 | 1 |
| 19 | Copy: Insider buying | copy | 98.57 | -1.43 | 11 | 54.5 | -15.68 | -2.88 | -21.08 | 74 |
| 20 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.36 | -3.95 | 25 |
| 21 | EMA 20/50 cross · 1h | trend | 97.80 | -2.20 | 34 | 5.9 | 10.52 | 1.33 | -16.12 | 138 |
| 22 | Stochastic reversion · 1h | reversion | 97.70 | -2.30 | 59 | 61.0 | -10.77 | -2.16 | -11.21 | 330 |
| 23 | Daily: Bullish score | daily | 97.69 | -2.31 | 3 | 0.0 | 1.01 | 0.33 | -12.76 | 10 |
| 24 | Trend pullback · 1h | trend | 97.67 | -2.33 | 68 | 23.5 | -22.55 | -6.57 | -24.27 | 170 |
| 25 | RSI(14) reversion · 1h | reversion | 97.60 | -2.40 | 16 | 43.8 | 4.60 | 1.23 | -6.57 | 125 |
| 26 | Z-score reversion · 1h | reversion | 97.22 | -2.78 | 27 | 44.4 | 2.20 | 0.58 | -8.60 | 154 |
| 27 | Daily: Momentum burst | daily | 96.97 | -3.03 | 3 | 0.0 | -1.09 | 0.01 | -16.91 | 40 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 96.94 | -3.06 | 0 | — | 15.35 | 2.33 | -7.19 | 1 |
| 29 | Agent | meta | 96.92 | -3.08 | 40 | 57.5 | -9.66 | -5.79 | -9.79 | 238 |
| 30 | Candlestick reversal · 1h | reversion | 96.89 | -3.11 | 78 | 34.6 | -24.91 | -5.75 | -25.15 | 489 |
| 31 | Agent (rotation) | meta | 96.56 | -3.44 | 70 | 28.6 | 2.70 | 0.72 | -8.85 | 293 |
| 32 | Connors RSI(2) · 1h | reversion | 96.44 | -3.56 | 76 | 43.4 | -13.69 | -4.60 | -15.82 | 218 |
| 33 | Bollinger reversion · 1h | reversion | 95.57 | -4.43 | 55 | 41.8 | -16.40 | -3.91 | -18.92 | 302 |
| 34 | Supertrend · 1h | trend | 95.21 | -4.79 | 36 | 8.3 | -1.00 | 0.06 | -16.76 | 209 |
| 35 | Agent (aggressive) | meta | 95.06 | -4.94 | 19 | 47.4 | -2.74 | -1.22 | -5.52 | 107 |
| 36 | ADX DI cross · 1h | trend | 94.97 | -5.03 | 43 | 11.6 | -7.15 | -1.08 | -13.84 | 256 |
| 37 | Agent (ML meta-label) | meta | 94.83 | -5.17 | 269 | 14.9 | -4.98 | -0.76 | -14.46 | 391 |
| 38 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 13.45 | 2.27 | -8.12 | 108 |
| 39 | Parabolic SAR · 1h | trend | 94.73 | -5.27 | 70 | 15.7 | -6.06 | -0.62 | -19.80 | 296 |
| 40 | MACD cross · 1h | trend | 94.56 | -5.44 | 95 | 22.1 | -14.42 | -2.33 | -17.27 | 466 |
| 41 | MFI reversion · 1h | reversion | 94.42 | -5.58 | 81 | 28.4 | -10.55 | -1.82 | -16.99 | 119 |
| 42 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.13 | 1.86 | -6.34 | 200 |
| 43 | Max aggression: 1-day momentum | meta | 93.91 | -6.09 | 8 | 37.5 | -21.96 | -1.08 | -37.31 | 42 |
| 44 | Opening range 30m | breakout | 93.57 | -6.43 | 103 | 21.4 | -17.19 | -5.28 | -17.25 | 558 |
| 45 | RSI momentum · 1h | momentum | 93.55 | -6.45 | 50 | 2.0 | -1.15 | 0.04 | -16.65 | 224 |
| 46 | Ichimoku · 1h | trend | 93.45 | -6.55 | 36 | 13.9 | 0.17 | 0.22 | -17.96 | 124 |
| 47 | Bollinger breakout · 1h | breakout | 93.09 | -6.91 | 63 | 30.2 | 5.09 | 0.83 | -12.06 | 294 |
| 48 | Williams %R · 1h | reversion | 92.90 | -7.10 | 90 | 50.0 | -22.32 | -4.04 | -23.02 | 493 |
| 49 | Triple EMA stack · 1h | trend | 92.73 | -7.27 | 60 | 10.0 | -14.39 | -1.64 | -25.49 | 253 |
| 50 | Volume breakout · 1h | breakout | 92.64 | -7.36 | 42 | 16.7 | 5.30 | 0.90 | -12.60 | 124 |
| 51 | CCI reversion · 1h | reversion | 92.46 | -7.54 | 79 | 44.3 | -3.27 | -0.34 | -12.41 | 404 |
| 52 | Opening range 15m | breakout | 91.71 | -8.29 | 120 | 20.0 | -18.79 | -5.53 | -18.92 | 678 |
| 53 | Three white soldiers | momentum | 90.78 | -9.22 | 103 | 19.4 | -49.17 | -24.30 | -49.32 | 585 |
| 54 | EMA 9/21 cross · 1h | trend | 90.68 | -9.32 | 90 | 11.1 | -5.43 | -0.53 | -18.86 | 344 |
| 55 | Donchian 20/10 · 1h | breakout | 90.56 | -9.44 | 44 | 13.6 | 1.02 | 0.33 | -16.18 | 222 |
| 56 | VWAP momentum · 1h | momentum | 90.53 | -9.47 | 233 | 22.7 | -37.16 | -5.70 | -37.99 | 1258 |
| 57 | MACD zero-line · 1h | trend | 90.13 | -9.87 | 54 | 16.7 | -6.20 | -0.64 | -18.94 | 240 |
| 58 | OBV trend · 1h | momentum | 89.35 | -10.65 | 114 | 12.3 | -16.64 | -1.93 | -27.48 | 337 |
| 59 | Heikin-Ashi · 1h | trend | 89.24 | -10.76 | 122 | 25.4 | -31.99 | -5.49 | -34.94 | 687 |
| 60 | Keltner breakout · 1h | breakout | 88.52 | -11.48 | 39 | 17.9 | -14.01 | -1.67 | -23.67 | 226 |
| 61 | ROC + volume · 1h | momentum | 86.32 | -13.68 | 121 | 19.0 | -11.52 | -1.43 | -23.18 | 413 |
| 62 | Max aggression: 5-day momentum ⏸ | meta | 85.74 | -14.26 | 7 | 28.6 | -24.38 | -2.14 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.70 | -19.30 | 253 | 29.2 | -72.49 | -19.70 | -72.54 | 1448 |
| 64 | Squeeze breakout | breakout | 76.70 | -23.30 | 256 | 15.2 | -62.36 | -18.79 | -62.37 | 1222 |
| 65 | ROC + volume | momentum | 76.39 | -23.61 | 322 | 20.5 | -73.97 | -17.56 | -73.97 | 1661 |
| 66 | Donchian 55/20 | breakout | 74.99 | -25.01 | 265 | 17.0 | -68.68 | -15.04 | -68.68 | 1301 |
| 67 | VWAP reversion | reversion | 73.66 | -26.34 | 304 | 26.6 | -70.14 | -16.36 | -70.18 | 1411 |
| 68 | EMA 20/50 cross | trend | 73.46 | -26.54 | 272 | 18.0 | -78.11 | -15.86 | -78.11 | 1465 |
| 69 | Volume breakout | breakout | 73.03 | -26.97 | 214 | 12.1 | -65.08 | -19.17 | -65.08 | 922 |
| 70 | Supertrend | trend | 68.22 | -31.78 | 368 | 19.6 | -86.93 | -21.91 | -86.94 | 1914 |
| 71 | Keltner breakout | breakout | 67.29 | -32.71 | 355 | 13.0 | -85.26 | -29.26 | -85.27 | 1877 |
| 72 | MFI reversion | reversion | 67.07 | -32.93 | 379 | 20.3 | -87.50 | -30.63 | -87.54 | 2119 |
| 73 | Z-score reversion | reversion | 66.75 | -33.25 | 386 | 25.6 | -85.49 | -25.06 | -85.51 | 2067 |
| 74 | Ichimoku | trend | 66.35 | -33.65 | 324 | 9.0 | -81.87 | -24.08 | -81.87 | 1756 |
| 75 | AI bee: Bizzy | ai | 66.07 | -33.93 | 631 | 8.6 | — | — | — | — |
| 76 | AI bee: Boozy | ai | 63.41 | -36.59 | 221 | 3.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 63.11 | -36.89 | 415 | 8.9 | -89.59 | -36.58 | -89.59 | 2098 |
| 78 | MACD zero-line | trend | 62.03 | -37.98 | 466 | 15.0 | -91.41 | -30.20 | -91.41 | 2352 |
| 79 | Donchian 20/10 | breakout | 61.45 | -38.55 | 503 | 17.7 | -90.95 | -26.84 | -90.96 | 2654 |
| 80 | RSI momentum | momentum | 60.84 | -39.16 | 465 | 16.6 | -90.53 | -26.01 | -90.54 | 2370 |
| 81 | Trend pullback | trend | 59.92 | -40.08 | 493 | 15.4 | -91.39 | -29.63 | -91.41 | 2344 |
| 82 | Triple EMA stack | trend | 59.14 | -40.86 | 518 | 15.1 | -93.20 | -31.34 | -93.20 | 2616 |
| 83 | Bollinger breakout | breakout | 57.92 | -42.08 | 515 | 13.6 | -93.93 | -34.69 | -93.94 | 2816 |
| 84 | Consensus | meta | 56.62 | -43.38 | 495 | 9.9 | -94.38 | -26.08 | -94.38 | 2679 |
| 85 | EMA 9/21 cross | trend | 54.03 | -45.97 | 645 | 16.0 | -97.40 | -34.69 | -97.40 | 3540 |
| 86 | Stochastic reversion ⏸ | reversion | 53.82 | -46.18 | 760 | 22.2 | -95.61 | -37.07 | -95.62 | 4056 |
| 87 | Connors RSI(2) | reversion | 53.43 | -46.58 | 685 | 20.1 | -96.55 | -34.08 | -96.55 | 3635 |
| 88 | Bollinger reversion ⏸ | reversion | 53.42 | -46.58 | 706 | 16.9 | -95.82 | -36.13 | -95.83 | 3706 |
| 89 | OBV trend | momentum | 51.24 | -48.76 | 748 | 14.6 | -96.39 | -37.77 | -96.39 | 3606 |
| 90 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.73 | -31.81 | -98.73 | 5390 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.32 | -39.86 | -99.32 | 5659 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -45.48 | -99.73 | 6114 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -40.24 | -97.37 | 3665 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -40.02 | -98.48 | 4705 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -43.41 | -99.51 | 6102 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -50.36 | -99.90 | 8230 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-07T14:25 | VWAP momentum · 1h | buy | SQQQ | 4.53 | — | rebalance up |
| 2026-10-07T14:25 | VWAP reversion | buy | TNA | 2.29 | — | entry |
| 2026-10-07T14:25 | VWAP reversion | buy | PLTR | 8.19 | — | entry |
| 2026-10-07T14:25 | VWAP reversion | sell | UPRO | 10.47 | -0.00 | target is flat |
| 2026-10-07T14:25 | Z-score reversion | buy | UPRO | 3.57 | — | entry |
| 2026-10-07T14:25 | Z-score reversion | buy | TQQQ | 3.71 | — | entry |
| 2026-10-07T14:25 | Z-score reversion | buy | TECL | 3.71 | — | entry |
| 2026-10-07T14:25 | Z-score reversion | buy | SPY | 3.71 | — | entry |
| 2026-10-07T14:25 | Z-score reversion | buy | SOXL | 3.71 | — | entry |
| 2026-10-07T14:25 | Z-score reversion | buy | META | 3.71 | — | entry signal |
| 2026-10-07T14:25 | Z-score reversion | buy | ETHU | 3.71 | — | entry signal |
| 2026-10-07T14:25 | Z-score reversion | buy | BITX | 3.71 | — | entry signal |
| 2026-10-07T14:25 | Z-score reversion | sell | XRP-USD | 3.60 | -0.03 | rebalance down |
| 2026-10-07T14:25 | Z-score reversion | sell | SOL-USD | 3.71 | -0.02 | rebalance down |
| 2026-10-07T14:25 | Z-score reversion | sell | NVDA | 3.72 | -0.01 | rebalance down |
| 2026-10-07T14:25 | Z-score reversion | sell | GOOGL | 3.71 | -0.02 | rebalance down |
| 2026-10-07T14:25 | Z-score reversion | sell | ETH-USD | 3.71 | -0.01 | rebalance down |
| 2026-10-07T14:25 | Z-score reversion | sell | DOGE-USD | 3.70 | -0.02 | rebalance down |
| 2026-10-07T14:25 | Z-score reversion | sell | BTC-USD | 3.70 | -0.03 | rebalance down |
| 2026-10-07T14:25 | Z-score reversion | sell | AMZN | 3.72 | -0.01 | rebalance down |
| 2026-10-07T14:25 | Connors RSI(2) | buy | SQQQ | 13.36 | — | entry signal |
| 2026-10-07T14:25 | Connors RSI(2) | buy | AMZN | 13.36 | — | entry signal |
| 2026-10-07T14:25 | Volume breakout | sell | SQQQ | 18.13 | -0.17 | stop-loss |
| 2026-10-07T14:25 | Squeeze breakout | sell | SQQQ | 19.03 | -0.18 | stop-loss |
| 2026-10-07T14:25 | Opening range 30m | buy | TECL | 23.40 | — | entry signal |
| 2026-10-07T14:25 | Opening range 30m | buy | SOXL | 23.40 | — | entry signal |
| 2026-10-07T14:25 | Opening range 30m | sell | NVDA | 23.30 | -0.13 | exit signal |
| 2026-10-07T14:25 | Opening range 15m | buy | TECL | 22.94 | — | entry signal |
| 2026-10-07T14:25 | Opening range 15m | buy | SOXL | 22.94 | — | entry signal |
| 2026-10-07T14:25 | Opening range 15m | sell | NVDA | 22.88 | -0.13 | exit signal |
| 2026-10-07T14:25 | Donchian 55/20 | sell | SQQQ | 18.61 | -0.18 | stop-loss |
| 2026-10-07T14:25 | Donchian 20/10 | sell | SQQQ | 15.25 | -0.15 | stop-loss |
| 2026-10-07T14:25 | ROC + volume | sell | SQQQ | 18.96 | -0.18 | stop-loss |
| 2026-10-07T14:22 | AI bee: Bizzy | buy | SOXL | 9.31 | — | Jev: buy (buy p=0.56) |
| 2026-10-07T14:20 | Keltner breakout · 1h | sell | TSLA | 21.95 | -0.14 | stop-loss |
| 2026-10-07T14:20 | Bollinger breakout · 1h | sell | TSLA | 23.19 | -0.22 | stop-loss |
| 2026-10-07T14:20 | ROC + volume · 1h | buy | TSLA | 4.38 | — | rebalance up |
| 2026-10-07T14:20 | ROC + volume · 1h | buy | PLTR | 4.35 | — | rebalance up |
| 2026-10-07T14:20 | ROC + volume · 1h | sell | GOOGL | 17.27 | -0.06 | target is flat |
| 2026-10-07T14:20 | Z-score reversion | buy | QQQ | 3.05 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-09 14:25:05.000188+00:00 -> 2026-10-07 14:35:05.000188+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
