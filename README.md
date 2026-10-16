# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T18:55:05.000112+00:00 · 25094 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.05 (-7.95%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.12 | -0.26 |
| SQQQ | 19.27 | +0.90 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 34817 decisions in 2833 calls, $0.4313 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T18:55 | 1 / 6 / 23 | cash |  |
| Breezy | 2026-10-16T18:55 | 0 / 21 / 9 | cash |  |
| Boozy | 2026-10-16T18:55 | 1 / 24 / 5 | BITX 52% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 108.12 | 8.12 | 9 | 66.7 | 9.50 | 3.09 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.40 | 7.40 | 10 | 70.0 | 1.48 | 0.52 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.20 | 6.20 | 14 | 35.7 | 8.43 | 2.05 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.39 | 4.39 | 0 | — | 5.39 | 2.62 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.64 | -0.36 | 59 | 39.0 | -11.52 | -3.36 | -13.79 | 126 |
| 8 | Max aggression: 5-day momentum | meta | 99.23 | -0.77 | 8 | 37.5 | -16.84 | -1.35 | -34.64 | 26 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.21 | -0.79 | 0 | — | 3.16 | 1.28 | -5.18 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.97 | -1.03 | 51 | 31.4 | 2.16 | 1.18 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.96 | -1.04 | 36 | 16.7 | 9.13 | 1.22 | -22.12 | 109 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.79 | -3.91 | 20 |
| 13 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 98.63 | -1.37 | 3 | 33.3 | -0.60 | 0.02 | -7.93 | 9 |
| 14 | Copy: Insider buying | copy | 98.50 | -1.50 | 20 | 45.0 | -12.11 | -2.08 | -20.62 | 75 |
| 15 | Hold SPY | benchmark | 98.48 | -1.52 | 0 | — | -1.80 | -0.97 | -3.23 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.36 | -2.64 | 0 | — | -4.87 | -1.96 | -7.50 | 1 |
| 17 | Agent (rotation) | meta | 97.19 | -2.81 | 107 | 32.7 | -7.64 | -2.85 | -11.55 | 290 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.48 | -3.52 | 0 | — | -2.65 | -1.05 | -5.20 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.41 | -3.59 | 0 | — | -6.65 | -3.61 | -6.83 | 1 |
| 20 | Hold BTC | benchmark | 96.09 | -3.90 | 0 | — | 27.84 | 3.27 | -8.68 | 1 |
| 21 | Trend pullback · 1h | trend | 96.04 | -3.96 | 87 | 24.1 | -21.29 | -6.36 | -22.47 | 151 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.71 | -5.29 | 81 | 19.8 | -8.85 | -1.58 | -13.33 | 257 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Parabolic SAR · 1h | trend | 93.37 | -6.63 | 96 | 21.9 | 3.39 | 0.62 | -22.55 | 278 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.32 | -6.78 | 197 |
| 27 | EMA 20/50 cross · 1h | trend | 93.01 | -6.99 | 54 | 14.8 | -3.84 | -0.33 | -22.92 | 128 |
| 28 | Daily: Momentum burst | daily | 92.56 | -7.44 | 5 | 20.0 | -7.73 | -1.03 | -20.35 | 42 |
| 29 | Agent (aggressive) | meta | 92.39 | -7.61 | 38 | 31.6 | -5.90 | -2.02 | -9.34 | 122 |
| 30 | Agent | meta | 92.05 | -7.95 | 77 | 39.0 | -9.71 | -5.24 | -10.75 | 244 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.79 | -0.11 | -14.55 | 118 |
| 32 | Opening range 30m | breakout | 91.31 | -8.70 | 193 | 29.5 | -12.16 | -3.39 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.12 | -8.88 | 76 | 17.1 | 0.77 | 0.31 | -26.55 | 219 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.48 | 0.89 | -14.21 | 274 |
| 35 | Triple EMA stack · 1h | trend | 90.51 | -9.49 | 80 | 16.2 | -8.37 | -0.67 | -33.23 | 235 |
| 36 | Daily: Bullish score | daily | 90.35 | -9.65 | 7 | 0.0 | -6.36 | -0.63 | -13.04 | 13 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.40 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.34 | -10.66 | 0 | — | -19.89 | -3.78 | -20.45 | 1 |
| 39 | Keltner breakout · 1h | breakout | 89.21 | -10.79 | 52 | 23.1 | -9.15 | -1.13 | -27.05 | 210 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.13 | -10.87 | 0 | — | -0.38 | 0.12 | -13.95 | 1 |
| 41 | Supertrend · 1h | trend | 89.02 | -10.98 | 84 | 11.9 | -4.08 | -0.26 | -30.09 | 213 |
| 42 | MACD cross · 1h | trend | 89.00 | -11.00 | 171 | 22.8 | -14.66 | -1.94 | -27.78 | 453 |
| 43 | OBV trend · 1h | momentum | 88.04 | -11.96 | 168 | 18.5 | -8.81 | -0.72 | -33.94 | 320 |
| 44 | Connors RSI(2) · 1h | reversion | 87.89 | -12.11 | 144 | 40.3 | -25.09 | -7.49 | -25.86 | 243 |
| 45 | Opening range 15m | breakout | 86.66 | -13.34 | 242 | 25.2 | -17.16 | -4.49 | -21.40 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.66 | -13.34 | 136 | 43.4 | -20.95 | -3.78 | -22.00 | 357 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -23.28 | -4.59 | -23.33 | 221 |
| 48 | Max aggression: 1-day momentum | meta | 85.08 | -14.92 | 14 | 35.7 | -11.69 | -0.30 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 85.06 | -14.94 | 78 | 17.9 | 1.01 | 0.33 | -21.63 | 219 |
| 50 | Three white soldiers | momentum | 84.93 | -15.07 | 207 | 18.8 | -47.66 | -20.10 | -48.45 | 609 |
| 51 | MFI reversion · 1h ⏸ | reversion | 84.04 | -15.96 | 204 | 30.4 | -22.95 | -3.73 | -23.22 | 141 |
| 52 | Heikin-Ashi · 1h | trend | 84.01 | -15.99 | 189 | 24.3 | -31.06 | -5.12 | -40.33 | 673 |
| 53 | VWAP momentum · 1h | momentum | 83.99 | -16.01 | 387 | 21.2 | -36.15 | -5.51 | -43.85 | 1253 |
| 54 | Z-score reversion · 1h | reversion | 83.68 | -16.32 | 84 | 32.1 | -15.42 | -2.68 | -19.63 | 181 |
| 55 | Agent (ML meta-label) | meta | 83.21 | -16.79 | 605 | 19.0 | -2.90 | -0.23 | -14.83 | 373 |
| 56 | ROC + volume · 1h | momentum | 83.08 | -16.92 | 192 | 21.4 | -12.33 | -1.64 | -26.42 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.10 | -17.90 | 127 | 11.8 | -7.26 | -0.66 | -29.70 | 320 |
| 58 | Williams %R · 1h | reversion | 80.19 | -19.81 | 180 | 42.2 | -34.49 | -5.63 | -35.73 | 523 |
| 59 | Bollinger reversion · 1h | reversion | 80.03 | -19.97 | 138 | 31.2 | -30.48 | -6.26 | -32.32 | 340 |
| 60 | RSI(14) reversion · 1h | reversion | 79.78 | -20.22 | 74 | 20.3 | -14.70 | -2.59 | -21.70 | 159 |
| 61 | CCI reversion · 1h | reversion | 79.17 | -20.83 | 161 | 38.5 | -19.32 | -2.51 | -25.19 | 425 |
| 62 | Candlestick reversal · 1h | reversion | 76.36 | -23.64 | 204 | 25.0 | -34.54 | -6.27 | -35.30 | 515 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -62.94 | -18.02 | -62.94 | 897 |
| 64 | ROC + volume | momentum | 63.51 | -36.48 | 546 | 21.8 | -75.69 | -17.69 | -77.37 | 1708 |
| 65 | Squeeze breakout | breakout | 63.25 | -36.76 | 428 | 14.7 | -63.01 | -18.09 | -63.96 | 1218 |
| 66 | RSI(14) reversion | reversion | 62.47 | -37.53 | 636 | 26.3 | -74.86 | -16.83 | -74.86 | 1627 |
| 67 | Donchian 55/20 | breakout | 61.58 | -38.42 | 434 | 17.7 | -69.04 | -14.56 | -71.81 | 1283 |
| 68 | EMA 20/50 cross | trend | 60.00 | -40.00 | 454 | 19.2 | -77.18 | -15.27 | -79.04 | 1451 |
| 69 | VWAP reversion | reversion | 55.47 | -44.53 | 649 | 22.5 | -73.69 | -15.64 | -73.69 | 1494 |
| 70 | AI bee: Boozy | ai | 55.26 | -44.74 | 296 | 6.1 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.83 | -45.17 | 606 | 16.0 | -83.56 | -27.37 | -83.72 | 1845 |
| 72 | Ichimoku | trend | 52.06 | -47.94 | 552 | 11.6 | -81.96 | -23.13 | -82.11 | 1733 |
| 73 | Supertrend ⏸ | trend | 50.88 | -49.12 | 638 | 19.6 | -86.66 | -20.63 | -87.06 | 1916 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -30.07 | -98.63 | 5311 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -30.31 | -93.49 | 2597 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.46 | -24.85 | -90.54 | 2366 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.82 | -27.75 | -91.84 | 2346 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -32.89 | -97.45 | 3529 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.68 | -36.72 | -96.70 | 3587 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.34 | -26.65 | -94.41 | 2614 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -37.11 | -99.41 | 5831 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.39 | -26.24 | -91.47 | 2648 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -32.56 | -96.38 | 3572 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.07 | -99.73 | 6215 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -29.69 | -91.75 | 2367 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.44 | -38.68 | -97.46 | 3652 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -37.23 | -98.52 | 4761 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.65 | -33.58 | -93.71 | 2807 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -40.56 | -99.55 | 6252 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.77 | -22.48 | -86.77 | 2165 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.20 | -27.67 | -88.20 | 2149 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.04 | -33.10 | -96.04 | 3819 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -34.51 | -89.36 | 2109 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.90 | -34.40 | -95.90 | 4158 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.97 | -99.89 | 8275 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T18:55 | Agent (ML meta-label) | sell | TECL | 8.26 | -0.39 | selected signal exited |
| 2026-10-16T18:55 | CCI reversion · 1h | sell | AMD | 19.88 | -0.22 | stop-loss |
| 2026-10-16T18:55 | Stochastic reversion · 1h | sell | TECL | 7.82 | -0.39 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion · 1h | sell | AMD | 16.01 | -0.25 | stop-loss |
| 2026-10-16T18:55 | VWAP reversion | sell | UPRO | 2.21 | -0.02 | stop-loss |
| 2026-10-16T18:55 | VWAP reversion | sell | TQQQ | 2.20 | -0.03 | stop-loss |
| 2026-10-16T18:55 | VWAP reversion | sell | SOXL | 2.11 | -0.03 | stop-loss |
| 2026-10-16T18:55 | VWAP reversion | sell | QQQ | 2.22 | -0.01 | stop-loss |
| 2026-10-16T18:55 | VWAP reversion | sell | NVDA | 1.81 | -0.01 | stop-loss |
| 2026-10-16T18:55 | VWAP reversion | sell | MSTR | 2.20 | -0.03 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion | buy | PLTR | 4.90 | — | rebalance up |
| 2026-10-16T18:55 | RSI(14) reversion | buy | META | 3.33 | — | rebalance up |
| 2026-10-16T18:55 | RSI(14) reversion | buy | IWM | 4.76 | — | rebalance up |
| 2026-10-16T18:55 | RSI(14) reversion | buy | GOOGL | 3.27 | — | rebalance up |
| 2026-10-16T18:55 | RSI(14) reversion | buy | AMZN | 3.27 | — | rebalance up |
| 2026-10-16T18:55 | RSI(14) reversion | sell | UPRO | 2.35 | -0.01 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion | sell | TSLA | 4.48 | -0.04 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion | sell | SOL-USD | 3.27 | -0.03 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion | sell | NVDA | 4.48 | -0.03 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion | sell | MSTR | 4.44 | -0.07 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion | sell | ETHU | 2.96 | -0.04 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion | sell | ETH-USD | 2.32 | -0.02 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion | sell | BTC-USD | 3.28 | -0.03 | stop-loss |
| 2026-10-16T18:55 | RSI(14) reversion | sell | BITX | 3.29 | -0.02 | stop-loss |
| 2026-10-16T18:55 | Supertrend | sell | XRP-USD | 8.45 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:55 | Supertrend | sell | SOL-USD | 8.46 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:55 | Supertrend | sell | ETHU | 8.43 | -0.19 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:55 | Supertrend | sell | ETH-USD | 8.49 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:55 | Supertrend | sell | BTC-USD | 8.54 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:55 | Supertrend | sell | BITX | 8.50 | -0.12 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:50 | Daily: Connors RSI(2) · 3x ETFs | sell | UPRO | 49.84 | -1.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:50 | Daily: Connors RSI(2) · 3x ETFs | sell | TQQQ | 48.79 | -2.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:50 | VWAP reversion | buy | AAPL | 2.17 | — | entry signal |
| 2026-10-16T18:50 | RSI(14) reversion | buy | UPRO | 2.35 | — | entry |
| 2026-10-16T18:50 | RSI(14) reversion | buy | TNA | 3.30 | — | entry |
| 2026-10-16T18:50 | RSI(14) reversion | buy | SOL-USD | 3.30 | — | entry |
| 2026-10-16T18:50 | RSI(14) reversion | sell | TQQQ | 4.46 | -0.06 | stop-loss |
| 2026-10-16T18:50 | RSI(14) reversion | sell | QQQ | 4.50 | -0.02 | stop-loss |
| 2026-10-16T18:49 | AI bee: Boozy | buy | BITX | 28.95 | — | Jev: buy (buy p=0.52) |
| 2026-10-16T18:46 | AI bee: Boozy | sell | ETHU | 31.68 | -0.40 | Jev: sell (sell p=0.53) after 27 min |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 18:55:05.000112+00:00 -> 2026-10-16 19:05:05.000112+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
