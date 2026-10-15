# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T13:55:05.000143+00:00 · 23683 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.10 (-6.91%)

Closed trades 72, win rate 41.7%, fees £2.56, max drawdown -7.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 12207 decisions in 2079 calls, $0.1662 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T13:55 | 2 / 6 / 23 | GOOGL 15% |  |
| Breezy | 2026-10-15T13:55 | 0 / 21 / 10 | cash |  |
| Boozy | 2026-10-15T13:55 | 0 / 25 / 6 | BITX 50% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 1.74 | +3.28% | 7 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| MFI reversion | AAPL | 1.54 | +0.60% | 4 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.41 | 5.41 | 0 | — | 5.43 | 2.53 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.49 | 2.69 | -3.27 | 19 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.65 | -0.80 | -9.61 | 25 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 101.26 | 1.26 | 0 | — | 4.69 | 1.81 | -5.18 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.06 | 1.06 | 1 | 100.0 | 1.65 | 0.53 | -7.93 | 9 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 9 | Copy: Insider buying | copy | 99.92 | -0.08 | 20 | 45.0 | -16.28 | -2.59 | -21.97 | 76 |
| 10 | Hold SPY | benchmark | 99.34 | -0.66 | 0 | — | -1.61 | -0.89 | -3.40 | 1 |
| 11 | VWAP reversion · 1h | reversion | 99.10 | -0.90 | 54 | 35.2 | -11.86 | -3.26 | -13.80 | 125 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Donchian 55/20 · 1h | breakout | 98.34 | -1.66 | 36 | 16.7 | 7.83 | 1.06 | -22.11 | 112 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 97.99 | -2.01 | 50 | 32.0 | 1.57 | 0.93 | -2.14 | 68 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.95 | -2.05 | 0 | — | -1.75 | -0.70 | -4.20 | 1 |
| 16 | ADX DI cross · 1h | trend | 97.25 | -2.75 | 70 | 21.4 | -9.57 | -1.67 | -15.17 | 254 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.10 | -2.90 | 0 | — | -6.32 | -3.40 | -6.38 | 1 |
| 18 | Trend pullback · 1h | trend | 97.08 | -2.92 | 86 | 24.4 | -24.43 | -7.18 | -25.52 | 165 |
| 19 | Max aggression: 5-day momentum | meta | 96.93 | -3.07 | 8 | 37.5 | -2.75 | 0.06 | -34.64 | 26 |
| 20 | Daily: Momentum burst | daily | 96.85 | -3.15 | 5 | 20.0 | -3.98 | -0.45 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.18 | -3.16 | -5.30 | 30 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 96.20 | -3.80 | 0 | — | -6.23 | -2.33 | -7.50 | 1 |
| 23 | Agent (rotation) | meta | 95.62 | -4.38 | 101 | 28.7 | -13.90 | -4.99 | -14.60 | 287 |
| 24 | Hold BTC | benchmark | 95.28 | -4.72 | 0 | — | 27.19 | 3.16 | -8.68 | 1 |
| 25 | Parabolic SAR · 1h | trend | 93.99 | -6.01 | 93 | 22.6 | 1.72 | 0.41 | -22.73 | 285 |
| 26 | EMA 20/50 cross · 1h | trend | 93.93 | -6.07 | 50 | 16.0 | 0.63 | 0.28 | -24.19 | 130 |
| 27 | Gap and go | momentum | 93.88 | -6.12 | 63 | 12.7 | 9.53 | 2.39 | -6.78 | 200 |
| 28 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.56 | 0.95 | -9.46 | 105 |
| 29 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -4.06 | -0.94 | -9.00 | 247 |
| 30 | Bollinger breakout · 1h | breakout | 93.07 | -6.93 | 78 | 29.5 | 9.24 | 1.32 | -14.21 | 276 |
| 31 | Supertrend · 1h | trend | 93.05 | -6.95 | 73 | 13.7 | 4.76 | 0.76 | -23.27 | 205 |
| 32 | RSI momentum · 1h | momentum | 92.90 | -7.10 | 73 | 17.8 | 2.84 | 0.53 | -24.94 | 224 |
| 33 | Daily: Bullish score | daily | 92.42 | -7.58 | 7 | 0.0 | -5.40 | -0.50 | -12.76 | 13 |
| 34 | MACD cross · 1h | trend | 92.24 | -7.76 | 153 | 22.2 | -12.93 | -1.77 | -22.73 | 456 |
| 35 | Volume breakout · 1h | breakout | 92.09 | -7.91 | 77 | 22.1 | 9.13 | 1.39 | -12.60 | 121 |
| 36 | Triple EMA stack · 1h | trend | 91.49 | -8.51 | 77 | 16.9 | -8.50 | -0.68 | -33.48 | 236 |
| 37 | Timing: Nasdaq FTD · TQQQ | daily | 90.92 | -9.08 | 0 | — | -19.00 | -3.56 | -19.22 | 1 |
| 38 | Ichimoku · 1h | trend | 90.61 | -9.39 | 51 | 15.7 | 0.04 | 0.21 | -23.46 | 124 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 90.37 | -9.63 | 0 | — | 1.31 | 0.36 | -13.53 | 1 |
| 40 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -6.68 | -1.75 | -10.86 | 125 |
| 41 | Stochastic reversion · 1h | reversion | 89.22 | -10.78 | 127 | 44.1 | -18.24 | -3.30 | -19.84 | 354 |
| 42 | OBV trend · 1h | momentum | 89.22 | -10.78 | 164 | 18.9 | -11.39 | -0.97 | -36.09 | 319 |
| 43 | Opening range 30m | breakout | 89.19 | -10.81 | 168 | 23.2 | -14.02 | -4.18 | -17.60 | 548 |
| 44 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -14.54 | -0.48 | -37.31 | 43 |
| 45 | Connors RSI(2) · 1h | reversion | 88.99 | -11.01 | 139 | 39.6 | -23.23 | -6.95 | -24.89 | 248 |
| 46 | Keltner breakout · 1h | breakout | 88.78 | -11.22 | 51 | 21.6 | -6.58 | -0.65 | -26.77 | 217 |
| 47 | MACD zero-line · 1h | trend | 88.56 | -11.44 | 74 | 16.2 | -20.99 | -3.96 | -22.54 | 224 |
| 48 | MFI reversion · 1h | reversion | 87.33 | -12.67 | 183 | 29.0 | -18.97 | -3.25 | -19.43 | 136 |
| 49 | Donchian 20/10 · 1h | breakout | 87.17 | -12.83 | 72 | 19.4 | 0.12 | 0.21 | -20.38 | 215 |
| 50 | Heikin-Ashi · 1h | trend | 86.76 | -13.24 | 169 | 26.0 | -29.68 | -4.75 | -39.17 | 659 |
| 51 | ROC + volume · 1h | momentum | 86.63 | -13.37 | 179 | 21.2 | -10.51 | -1.39 | -25.32 | 396 |
| 52 | VWAP momentum · 1h | momentum | 85.94 | -14.06 | 352 | 21.6 | -36.13 | -5.42 | -43.06 | 1236 |
| 53 | Z-score reversion · 1h | reversion | 85.87 | -14.13 | 70 | 32.9 | -13.01 | -2.21 | -17.27 | 168 |
| 54 | Agent (ML meta-label) | meta | 85.45 | -14.54 | 552 | 17.8 | -5.10 | -0.66 | -14.10 | 391 |
| 55 | EMA 9/21 cross · 1h | trend | 85.23 | -14.77 | 120 | 12.5 | -9.28 | -1.03 | -26.84 | 322 |
| 56 | Opening range 15m | breakout | 84.75 | -15.25 | 215 | 20.5 | -19.28 | -5.31 | -21.40 | 689 |
| 57 | Three white soldiers | momentum | 83.97 | -16.03 | 184 | 16.3 | -48.57 | -21.44 | -48.79 | 593 |
| 58 | RSI(14) reversion · 1h | reversion | 82.15 | -17.86 | 60 | 21.7 | -12.15 | -2.05 | -18.93 | 160 |
| 59 | Bollinger reversion · 1h | reversion | 81.38 | -18.62 | 126 | 28.6 | -29.28 | -6.01 | -31.44 | 330 |
| 60 | CCI reversion · 1h | reversion | 81.10 | -18.90 | 137 | 40.1 | -19.00 | -2.46 | -23.38 | 419 |
| 61 | Williams %R · 1h | reversion | 81.00 | -19.00 | 162 | 41.4 | -34.03 | -5.55 | -34.80 | 506 |
| 62 | Candlestick reversal · 1h | reversion | 79.00 | -21.00 | 179 | 24.6 | -33.74 | -6.23 | -33.86 | 518 |
| 63 | ROC + volume | momentum | 66.57 | -33.43 | 489 | 21.3 | -74.34 | -16.46 | -76.62 | 1678 |
| 64 | Volume breakout | breakout | 65.73 | -34.27 | 308 | 13.6 | -63.22 | -17.73 | -63.22 | 887 |
| 65 | RSI(14) reversion | reversion | 64.69 | -35.31 | 555 | 26.8 | -73.98 | -16.87 | -74.11 | 1556 |
| 66 | Squeeze breakout | breakout | 64.47 | -35.53 | 402 | 14.7 | -62.94 | -17.51 | -63.33 | 1210 |
| 67 | Donchian 55/20 | breakout | 63.02 | -36.98 | 399 | 16.8 | -68.78 | -14.24 | -70.95 | 1265 |
| 68 | EMA 20/50 cross | trend | 61.04 | -38.96 | 420 | 18.8 | -77.51 | -15.12 | -78.49 | 1430 |
| 69 | VWAP reversion | reversion | 58.03 | -41.97 | 577 | 24.1 | -72.44 | -14.89 | -72.56 | 1432 |
| 70 | Keltner breakout | breakout | 55.56 | -44.44 | 557 | 14.0 | -83.49 | -26.46 | -83.50 | 1831 |
| 71 | AI bee: Boozy | ai | 55.31 | -44.69 | 274 | 4.7 | — | — | — | — |
| 72 | Supertrend | trend | 53.83 | -46.17 | 581 | 18.6 | -86.56 | -20.05 | -86.60 | 1890 |
| 73 | Ichimoku | trend | 53.75 | -46.25 | 490 | 9.8 | -81.82 | -22.08 | -81.88 | 1700 |
| 74 | AI bee: Bizzy | ai | 50.83 | -49.17 | 1009 | 8.1 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -28.71 | -98.64 | 5328 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.49 | -29.06 | -93.52 | 2561 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.68 | -24.16 | -90.71 | 2342 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.52 | -25.89 | -91.55 | 2327 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.48 | -31.57 | -97.48 | 3503 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -34.31 | -96.58 | 3555 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.45 | -24.67 | -94.45 | 2620 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -35.23 | -99.42 | 5754 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.21 | -25.13 | -91.21 | 2616 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.19 | -29.96 | -96.20 | 3544 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.52 | -99.73 | 6152 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.89 | -28.65 | -91.91 | 2347 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -36.31 | -97.45 | 3634 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.55 | -35.54 | -98.55 | 4684 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.50 | -31.39 | -93.55 | 2771 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -37.91 | -99.56 | 6162 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.51 | -21.85 | -86.53 | 2105 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.14 | -26.95 | -88.17 | 2132 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.14 | -31.82 | -96.14 | 3768 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.42 | -33.01 | -89.43 | 2100 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.90 | -32.71 | -95.91 | 4072 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.93 | -99.89 | 8191 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T13:55 | Agent (rotation) | buy | TNA | 5.31 | — | rebalance up |
| 2026-10-15T13:55 | Agent (rotation) | buy | MSFT | 5.30 | — | rebalance up |
| 2026-10-15T13:55 | Agent (rotation) | buy | IWM | 5.31 | — | rebalance up |
| 2026-10-15T13:55 | Agent (rotation) | buy | GOOGL | 5.30 | — | rebalance up |
| 2026-10-15T13:55 | Agent (rotation) | sell | UPRO | 2.62 | -0.06 | selected signal exited |
| 2026-10-15T13:55 | Day trade: Stocks in Play ORB | buy | SQQQ | 24.50 | — | entry |
| 2026-10-15T13:55 | Agent (ML meta-label) | buy | XRP-USD | 4.73 | — | rebalance up |
| 2026-10-15T13:55 | Agent (ML meta-label) | buy | SOL-USD | 4.73 | — | rebalance up |
| 2026-10-15T13:55 | Agent (ML meta-label) | buy | GOOGL | 4.41 | — | rebalance up |
| 2026-10-15T13:55 | Agent (ML meta-label) | buy | ETH-USD | 4.73 | — | rebalance up |
| 2026-10-15T13:55 | Agent (ML meta-label) | buy | DOGE-USD | 4.73 | — | rebalance up |
| 2026-10-15T13:55 | Agent (ML meta-label) | sell | UPRO | 5.43 | -0.12 | selected signal exited |
| 2026-10-15T13:55 | Agent (ML meta-label) | sell | SPY | 5.33 | -0.01 | selected signal exited |
| 2026-10-15T13:55 | Agent (ML meta-label) | sell | BITX | 4.98 | -0.37 | selected signal exited |
| 2026-10-15T13:55 | MFI reversion · 1h | buy | SOL-USD | 7.43 | — | rebalance up |
| 2026-10-15T13:55 | MFI reversion · 1h | buy | DOGE-USD | 4.64 | — | rebalance up |
| 2026-10-15T13:55 | MFI reversion · 1h | sell | XRP-USD | 17.36 | -0.22 | stop-loss |
| 2026-10-15T13:55 | MFI reversion · 1h | sell | ETH-USD | 17.38 | -0.38 | stop-loss |
| 2026-10-15T13:55 | CCI reversion · 1h | buy | ETH-USD | 4.13 | — | rebalance up |
| 2026-10-15T13:55 | CCI reversion · 1h | buy | DOGE-USD | 4.14 | — | rebalance up |
| 2026-10-15T13:55 | CCI reversion · 1h | sell | XRP-USD | 16.11 | -0.21 | stop-loss |
| 2026-10-15T13:55 | CCI reversion · 1h | sell | SOL-USD | 16.18 | -0.33 | stop-loss |
| 2026-10-15T13:55 | Williams %R · 1h | buy | SOL-USD | 4.09 | — | rebalance up |
| 2026-10-15T13:55 | Williams %R · 1h | buy | DOGE-USD | 4.17 | — | rebalance up |
| 2026-10-15T13:55 | Williams %R · 1h | sell | XRP-USD | 12.78 | -0.22 | stop-loss |
| 2026-10-15T13:55 | Williams %R · 1h | sell | ETH-USD | 16.11 | -0.42 | stop-loss |
| 2026-10-15T13:55 | Stochastic reversion · 1h | buy | MSFT | 4.54 | — | rebalance up |
| 2026-10-15T13:55 | Stochastic reversion · 1h | sell | COIN | 9.89 | -0.15 | stop-loss |
| 2026-10-15T13:55 | VWAP reversion · 1h | buy | TNA | 8.38 | — | rebalance up |
| 2026-10-15T13:55 | VWAP reversion · 1h | buy | MSFT | 8.27 | — | rebalance up |
| 2026-10-15T13:55 | VWAP reversion · 1h | buy | IWM | 8.32 | — | rebalance up |
| 2026-10-15T13:55 | VWAP reversion · 1h | buy | GOOGL | 8.04 | — | rebalance up |
| 2026-10-15T13:55 | VWAP reversion · 1h | sell | UPRO | 16.40 | -0.23 | stop-loss |
| 2026-10-15T13:55 | Z-score reversion · 1h | buy | ETH-USD | 4.30 | — | rebalance up |
| 2026-10-15T13:55 | Z-score reversion · 1h | buy | DOGE-USD | 4.35 | — | rebalance up |
| 2026-10-15T13:55 | Z-score reversion · 1h | sell | XRP-USD | 14.39 | -0.50 | stop-loss |
| 2026-10-15T13:55 | Z-score reversion · 1h | sell | SOL-USD | 14.38 | -0.51 | stop-loss |
| 2026-10-15T13:55 | Z-score reversion · 1h | sell | BITX | 14.51 | -1.02 | stop-loss |
| 2026-10-15T13:55 | Bollinger reversion · 1h | buy | XRP-USD | 11.30 | — | rebalance up |
| 2026-10-15T13:55 | Bollinger reversion · 1h | buy | TNA | 11.33 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 13:55:05.000143+00:00 -> 2026-10-15 14:05:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
