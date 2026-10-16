# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T16:56:05.000211+00:00 · 24995 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.68 (-8.32%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.24 | -0.13 |
| SQQQ | 18.77 | +0.40 |

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

Today: 25868 decisions in 2536 calls, $0.3262 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T16:56 | 1 / 3 / 26 | cash |  |
| Breezy | 2026-10-16T16:56 | 0 / 20 / 10 | cash |  |
| Boozy | 2026-10-16T16:56 | 0 / 24 / 6 | COIN 56% |  |

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
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.32 | 5.32 | 9 | 66.7 | 6.79 | 2.78 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.62 | 4.62 | 10 | 70.0 | -1.04 | -0.26 | -9.61 | 27 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 104.08 | 4.08 | 0 | — | 5.19 | 2.52 | -5.18 | 1 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.45 | 3.45 | 14 | 35.7 | 5.74 | 1.65 | -7.55 | 44 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.62 | 0.62 | 1 | 100.0 | 1.79 | 0.52 | -7.93 | 9 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.32 | 0.32 | 0 | — | 4.43 | 1.72 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | VWAP reversion · 1h | reversion | 99.84 | -0.16 | 59 | 39.0 | -11.47 | -3.33 | -13.79 | 124 |
| 10 | Hold SPY | benchmark | 98.98 | -1.02 | 0 | — | -1.19 | -0.65 | -3.23 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.76 | -3.91 | 20 |
| 12 | Copy: Insider buying | copy | 98.47 | -1.53 | 20 | 45.0 | -12.06 | -2.06 | -20.62 | 75 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 98.31 | -1.69 | 51 | 31.4 | 1.52 | 0.87 | -2.96 | 69 |
| 14 | Donchian 55/20 · 1h | breakout | 98.27 | -1.73 | 36 | 16.7 | 8.45 | 1.14 | -22.12 | 109 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.25 | -2.75 | 0 | — | -4.87 | -1.95 | -7.50 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 97.17 | -2.83 | 0 | — | -1.84 | -0.74 | -4.50 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 96.80 | -3.20 | 0 | — | -6.22 | -3.43 | -6.40 | 1 |
| 18 | Max aggression: 5-day momentum | meta | 96.66 | -3.34 | 8 | 37.5 | -18.91 | -1.63 | -34.64 | 26 |
| 19 | Hold BTC | benchmark | 96.59 | -3.41 | 0 | — | 28.75 | 3.35 | -8.68 | 1 |
| 20 | Trend pullback · 1h | trend | 96.31 | -3.69 | 87 | 24.1 | -21.56 | -6.40 | -22.30 | 152 |
| 21 | Agent (rotation) | meta | 96.17 | -3.83 | 107 | 32.7 | -10.36 | -3.57 | -13.20 | 297 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.86 | -5.14 | 80 | 20.0 | -8.51 | -1.51 | -13.33 | 257 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Daily: Momentum burst | daily | 93.41 | -6.59 | 5 | 20.0 | -6.73 | -0.88 | -19.55 | 42 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.31 | -6.78 | 197 |
| 27 | Parabolic SAR · 1h | trend | 92.93 | -7.07 | 95 | 22.1 | 2.98 | 0.56 | -22.55 | 278 |
| 28 | EMA 20/50 cross · 1h | trend | 92.64 | -7.36 | 53 | 15.1 | -4.57 | -0.43 | -22.92 | 129 |
| 29 | Agent | meta | 91.68 | -8.32 | 77 | 39.0 | -10.05 | -5.26 | -10.78 | 244 |
| 30 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.79 | -0.11 | -14.55 | 118 |
| 31 | Agent (aggressive) | meta | 91.16 | -8.84 | 38 | 31.6 | -7.16 | -2.61 | -9.42 | 123 |
| 32 | RSI momentum · 1h | momentum | 90.95 | -9.05 | 75 | 17.3 | 0.54 | 0.28 | -26.55 | 219 |
| 33 | Daily: Bullish score | daily | 90.81 | -9.19 | 7 | 0.0 | -5.83 | -0.56 | -12.76 | 13 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.48 | 0.89 | -14.21 | 274 |
| 35 | Opening range 30m | breakout | 90.76 | -9.24 | 192 | 29.7 | -12.63 | -3.49 | -17.60 | 572 |
| 36 | Timing: Nasdaq FTD · TQQQ | daily | 90.56 | -9.44 | 0 | — | -18.73 | -3.60 | -19.30 | 1 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 90.26 | -9.74 | 0 | — | 1.00 | 0.32 | -13.89 | 1 |
| 39 | MACD cross · 1h | trend | 89.98 | -10.02 | 168 | 23.2 | -14.04 | -1.86 | -26.85 | 458 |
| 40 | Triple EMA stack · 1h | trend | 89.86 | -10.14 | 80 | 16.2 | -8.78 | -0.72 | -33.23 | 235 |
| 41 | Supertrend · 1h | trend | 89.49 | -10.51 | 79 | 12.7 | -3.30 | -0.17 | -29.45 | 213 |
| 42 | Keltner breakout · 1h | breakout | 88.61 | -11.39 | 52 | 23.1 | -9.72 | -1.21 | -27.05 | 210 |
| 43 | Connors RSI(2) · 1h | reversion | 88.55 | -11.45 | 144 | 40.3 | -24.44 | -7.34 | -25.22 | 243 |
| 44 | Stochastic reversion · 1h | reversion | 88.41 | -11.59 | 133 | 44.4 | -19.22 | -3.58 | -20.36 | 349 |
| 45 | OBV trend · 1h | momentum | 87.77 | -12.23 | 168 | 18.5 | -9.00 | -0.73 | -33.94 | 320 |
| 46 | Max aggression: 1-day momentum | meta | 87.39 | -12.61 | 14 | 35.7 | -9.19 | -0.14 | -37.31 | 43 |
| 47 | Opening range 15m | breakout | 86.26 | -13.73 | 241 | 25.3 | -17.60 | -4.58 | -21.40 | 709 |
| 48 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -23.25 | -4.56 | -23.33 | 224 |
| 49 | Z-score reversion · 1h | reversion | 85.28 | -14.72 | 79 | 34.2 | -13.34 | -2.41 | -17.67 | 180 |
| 50 | MFI reversion · 1h | reversion | 85.04 | -14.96 | 201 | 30.8 | -20.55 | -3.52 | -20.84 | 142 |
| 51 | Three white soldiers | momentum | 84.72 | -15.28 | 207 | 18.8 | -47.95 | -20.05 | -48.59 | 611 |
| 52 | Donchian 20/10 · 1h | breakout | 84.69 | -15.31 | 77 | 18.2 | 0.48 | 0.27 | -21.63 | 219 |
| 53 | Agent (ML meta-label) | meta | 84.43 | -15.57 | 590 | 19.2 | -8.32 | -1.17 | -18.96 | 395 |
| 54 | VWAP momentum · 1h | momentum | 83.50 | -16.50 | 386 | 21.2 | -36.48 | -5.52 | -43.85 | 1253 |
| 55 | Heikin-Ashi · 1h | trend | 83.45 | -16.55 | 189 | 24.3 | -31.49 | -5.14 | -40.33 | 673 |
| 56 | ROC + volume · 1h | momentum | 82.94 | -17.06 | 190 | 21.6 | -12.40 | -1.64 | -26.33 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.65 | -17.35 | 125 | 12.0 | -7.07 | -0.63 | -29.26 | 321 |
| 58 | Williams %R · 1h | reversion | 81.87 | -18.13 | 177 | 42.9 | -33.17 | -5.48 | -34.85 | 524 |
| 59 | Bollinger reversion · 1h | reversion | 81.72 | -18.29 | 136 | 31.6 | -28.99 | -6.18 | -31.36 | 336 |
| 60 | RSI(14) reversion · 1h | reversion | 81.09 | -18.91 | 67 | 22.4 | -13.73 | -2.49 | -20.19 | 164 |
| 61 | CCI reversion · 1h | reversion | 80.76 | -19.24 | 151 | 41.1 | -17.53 | -2.30 | -23.45 | 427 |
| 62 | Candlestick reversal · 1h | reversion | 77.62 | -22.38 | 199 | 25.6 | -33.65 | -6.20 | -34.23 | 518 |
| 63 | RSI(14) reversion | reversion | 63.99 | -36.01 | 603 | 27.7 | -74.27 | -16.82 | -74.27 | 1599 |
| 64 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.47 | -18.19 | -63.47 | 896 |
| 65 | Squeeze breakout | breakout | 63.25 | -36.76 | 428 | 14.7 | -62.95 | -17.80 | -63.91 | 1217 |
| 66 | ROC + volume | momentum | 63.23 | -36.77 | 546 | 21.8 | -75.83 | -17.44 | -77.40 | 1719 |
| 67 | Donchian 55/20 | breakout | 61.16 | -38.84 | 434 | 17.7 | -69.41 | -14.55 | -71.81 | 1286 |
| 68 | EMA 20/50 cross | trend | 59.68 | -40.32 | 453 | 19.2 | -77.41 | -15.22 | -79.04 | 1454 |
| 69 | VWAP reversion | reversion | 56.40 | -43.60 | 613 | 23.5 | -73.27 | -15.44 | -73.27 | 1466 |
| 70 | AI bee: Boozy | ai | 56.23 | -43.77 | 292 | 5.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.46 | -45.53 | 606 | 16.0 | -83.69 | -26.88 | -83.74 | 1846 |
| 72 | Supertrend | trend | 51.83 | -48.17 | 631 | 19.8 | -86.52 | -20.44 | -86.84 | 1914 |
| 73 | Ichimoku | trend | 51.71 | -48.29 | 552 | 11.6 | -82.13 | -22.92 | -82.16 | 1735 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.33 | -98.64 | 5313 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.54 | -29.97 | -93.55 | 2602 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.60 | -24.65 | -90.62 | 2371 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.81 | -27.13 | -91.83 | 2345 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -32.24 | -97.47 | 3531 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.72 | -35.91 | -96.73 | 3614 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -26.21 | -94.48 | 2626 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -35.95 | -99.40 | 5786 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.44 | -25.75 | -91.47 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.69 | -96.38 | 3572 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.81 | -99.73 | 6192 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.80 | -29.23 | -91.80 | 2371 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -37.66 | -97.47 | 3656 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.25 | -98.48 | 4727 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.72 | -32.77 | -93.74 | 2809 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.27 | -99.54 | 6224 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.45 | -22.25 | -86.45 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.84 | -27.18 | -87.84 | 2132 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.96 | -32.18 | -95.96 | 3793 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -33.61 | -89.30 | 2105 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.84 | -33.73 | -95.84 | 4125 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.06 | -99.89 | 8263 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T16:55 | RSI(14) reversion | buy | UPRO | 3.76 | — | entry signal |
| 2026-10-16T16:50 | Agent (ML meta-label) | sell | SQQQ | 4.46 | 0.01 | selected signal exited |
| 2026-10-16T16:50 | Agent (ML meta-label) | sell | BITX | 4.43 | -0.02 | selected signal exited |
| 2026-10-16T16:50 | CCI reversion · 1h | sell | UPRO | 5.78 | -0.15 | stop-loss |
| 2026-10-16T16:50 | Z-score reversion · 1h | sell | UPRO | 7.04 | -0.18 | stop-loss |
| 2026-10-16T16:50 | RSI(14) reversion · 1h | sell | UPRO | 7.26 | -0.19 | stop-loss |
| 2026-10-16T16:50 | MACD cross · 1h | sell | TNA | 12.80 | -0.29 | stop-loss |
| 2026-10-16T16:50 | VWAP reversion | buy | GOOGL | 3.12 | — | entry |
| 2026-10-16T16:50 | VWAP reversion | buy | AMZN | 3.32 | — | entry |
| 2026-10-16T16:50 | VWAP reversion | sell | TNA | 3.31 | -0.02 | stop-loss |
| 2026-10-16T16:50 | VWAP reversion | sell | IWM | 3.13 | -0.01 | stop-loss |
| 2026-10-16T16:50 | RSI(14) reversion | buy | LABU | 4.00 | — | entry signal |
| 2026-10-16T16:50 | RSI(14) reversion | sell | UPRO | 4.56 | -0.02 | stop-loss |
| 2026-10-16T16:50 | RSI(14) reversion | sell | SPY | 4.27 | -0.01 | stop-loss |
| 2026-10-16T16:45 | AI bee: Boozy | buy | COIN | 31.51 | — | Jev: buy (buy p=0.56) |
| 2026-10-16T16:45 | Agent (ML meta-label) | buy | SQQQ | 4.45 | — | following VWAP momentum · 1h |
| 2026-10-16T16:45 | Agent (ML meta-label) | buy | BITX | 4.45 | — | entry |
| 2026-10-16T16:45 | RSI(14) reversion | buy | MSFT | 2.61 | — | entry signal |
| 2026-10-16T16:45 | RSI(14) reversion | buy | GOOGL | 3.77 | — | entry signal |
| 2026-10-16T16:45 | RSI(14) reversion | buy | AMZN | 3.77 | — | entry signal |
| 2026-10-16T16:45 | RSI(14) reversion | sell | TQQQ | 3.33 | -0.01 | rebalance down |
| 2026-10-16T16:45 | RSI(14) reversion | sell | QQQ | 3.40 | -0.00 | rebalance down |
| 2026-10-16T16:45 | RSI(14) reversion | sell | DOGE-USD | 3.43 | -0.01 | rebalance down |
| 2026-10-16T16:43 | AI bee: Boozy | sell | ETHU | 33.39 | -0.26 | Jev: sell (sell p=0.56) after 16 min |
| 2026-10-16T16:40 | Agent (ML meta-label) | sell | GOOGL | 3.25 | -0.09 | selected signal exited |
| 2026-10-16T16:40 | Stochastic reversion · 1h | buy | TECL | 6.93 | — | rebalance up |
| 2026-10-16T16:40 | Stochastic reversion · 1h | buy | SOXL | 4.81 | — | rebalance up |
| 2026-10-16T16:40 | Stochastic reversion · 1h | sell | GOOGL | 14.71 | -0.14 | stop-loss |
| 2026-10-16T16:40 | VWAP reversion | buy | TSLA | 1.04 | — | entry signal |
| 2026-10-16T16:40 | VWAP reversion | buy | TNA | 3.33 | — | entry |
| 2026-10-16T16:40 | VWAP reversion | buy | SPY | 3.33 | — | entry |
| 2026-10-16T16:40 | VWAP reversion | sell | META | 4.37 | -0.03 | stop-loss |
| 2026-10-16T16:40 | VWAP reversion | sell | GOOGL | 3.32 | -0.02 | stop-loss |
| 2026-10-16T16:40 | RSI(14) reversion | buy | XRP-USD | 1.83 | — | entry |
| 2026-10-16T16:40 | RSI(14) reversion | buy | UPRO | 4.59 | — | entry |
| 2026-10-16T16:40 | RSI(14) reversion | sell | MSFT | 6.42 | -0.01 | stop-loss |
| 2026-10-16T16:40 | EMA 20/50 cross | sell | NVDA | 14.86 | -0.04 | exit signal |
| 2026-10-16T16:35 | CCI reversion · 1h | sell | META | 4.47 | -0.14 | stop-loss |
| 2026-10-16T16:35 | Candlestick reversal · 1h | buy | NVDA | 10.45 | — | rebalance up |
| 2026-10-16T16:35 | Candlestick reversal · 1h | sell | SPY | 15.59 | -0.07 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 16:56:05.000211+00:00 -> 2026-10-16 17:06:05.000211+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
