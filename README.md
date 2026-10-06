# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T18:59:05.000150+00:00 · 13761 ticks

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
| Copy: Insider buying | 2026-10-06 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, PAM 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-05)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.70 · VIX 15.52 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.8, AMD 7.6, TECL 7.6, MSTR 7.5, BITX 7.5, ETHU 7.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 31570 decisions in 2675 calls, $0.3919 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T18:59 | 1 / 15 / 14 | AMD 14% |  |
| Breezy | 2026-10-06T18:59 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-06T18:59 | 0 / 26 / 4 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.48 | 6.48 | 0 | — | -0.18 | 0.10 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -9.17 | -2.90 | -13.93 | 113 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.09 | 2.09 | 0 | — | 0.45 | 0.31 | -5.09 | 1 |
| 4 | Hold BTC | benchmark | 101.96 | 1.96 | 0 | — | 31.64 | 3.83 | -8.68 | 1 |
| 5 | Donchian 55/20 · 1h | breakout | 101.90 | 1.90 | 17 | 0.0 | 13.07 | 1.77 | -16.96 | 110 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.71 | 1.71 | 0 | — | 3.41 | 1.63 | -3.62 | 1 |
| 8 | Daily: Bullish score | daily | 101.36 | 1.36 | 3 | 0.0 | 5.64 | 0.94 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.14 | 1.14 | 0 | — | 1.28 | 0.82 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.43 | 0.43 | 67 | 38.8 | -19.41 | -4.31 | -21.55 | 494 |
| 13 | Copy: Warren Buffett (BRK-B) | copy | 100.16 | 0.16 | 0 | — | -2.30 | -0.88 | -7.65 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 100.13 | 0.13 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 15 | Stochastic reversion · 1h | reversion | 100.11 | 0.11 | 56 | 64.3 | -7.38 | -1.51 | -10.46 | 326 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.86 | 1.86 | -1.59 | 85 |
| 17 | EMA 20/50 cross · 1h | trend | 100.07 | 0.07 | 28 | 7.1 | 13.91 | 1.72 | -15.31 | 141 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 19 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 20 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 21 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 99.60 | -0.40 | 0 | — | 18.98 | 2.89 | -6.29 | 1 |
| 23 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 3.92 | 1.05 | -6.57 | 132 |
| 24 | Connors RSI(2) · 1h | reversion | 99.50 | -0.50 | 73 | 45.2 | -10.88 | -3.93 | -14.73 | 218 |
| 25 | Trend pullback · 1h | trend | 99.10 | -0.90 | 65 | 24.6 | -20.59 | -6.07 | -24.41 | 167 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | 0.03 | 0.07 | -4.23 | 104 |
| 27 | Copy: Insider buying | copy | 98.33 | -1.67 | 11 | 54.5 | -15.27 | -2.81 | -21.08 | 73 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.42 | -3.95 | 25 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -8.85 | -5.37 | -10.05 | 228 |
| 30 | Daily: Momentum burst | daily | 98.22 | -1.78 | 3 | 0.0 | 1.39 | 0.39 | -16.91 | 41 |
| 31 | Bollinger reversion · 1h | reversion | 98.13 | -1.87 | 49 | 46.9 | -15.06 | -3.78 | -17.05 | 301 |
| 32 | Z-score reversion · 1h | reversion | 98.12 | -1.88 | 23 | 52.2 | 3.66 | 0.89 | -8.60 | 150 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.31 | -2.69 | 0 | — | -0.16 | 0.03 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.10 | -2.90 | 63 | 28.6 | -2.21 | -0.44 | -11.45 | 267 |
| 35 | ADX DI cross · 1h | trend | 97.07 | -2.93 | 43 | 11.6 | -3.03 | -0.37 | -13.84 | 253 |
| 36 | Supertrend · 1h | trend | 96.97 | -3.03 | 32 | 9.4 | 2.30 | 0.50 | -16.43 | 211 |
| 37 | Agent (ML meta-label) | meta | 96.82 | -3.18 | 265 | 14.7 | -0.26 | 0.09 | -13.61 | 366 |
| 38 | Williams %R · 1h | reversion | 96.56 | -3.44 | 85 | 52.9 | -19.99 | -3.75 | -20.52 | 495 |
| 39 | Parabolic SAR · 1h | trend | 96.55 | -3.45 | 65 | 15.4 | -3.10 | -0.22 | -19.45 | 301 |
| 40 | CCI reversion · 1h | reversion | 96.18 | -3.82 | 71 | 49.3 | -0.64 | 0.06 | -12.41 | 409 |
| 41 | MACD cross · 1h | trend | 95.78 | -4.22 | 88 | 19.3 | -13.71 | -2.22 | -17.27 | 468 |
| 42 | RSI momentum · 1h | momentum | 95.62 | -4.38 | 45 | 2.2 | 1.05 | 0.33 | -16.65 | 230 |
| 43 | Squeeze breakout · 1h | breakout | 95.38 | -4.62 | 30 | 20.0 | 15.31 | 2.57 | -8.06 | 106 |
| 44 | MFI reversion · 1h | reversion | 95.12 | -4.88 | 75 | 28.0 | -10.65 | -1.86 | -16.99 | 120 |
| 45 | Ichimoku · 1h | trend | 95.12 | -4.88 | 33 | 15.2 | 8.64 | 1.20 | -15.84 | 124 |
| 46 | Triple EMA stack · 1h | trend | 94.86 | -5.14 | 56 | 10.7 | -10.00 | -1.06 | -24.32 | 255 |
| 47 | Max aggression: 1-day momentum | meta | 94.76 | -5.24 | 7 | 42.9 | -23.66 | -1.23 | -37.31 | 42 |
| 48 | Bollinger breakout · 1h | breakout | 94.63 | -5.37 | 50 | 24.0 | 7.77 | 1.16 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 6.75 | 1.77 | -6.49 | 201 |
| 50 | Opening range 30m | breakout | 94.02 | -5.98 | 98 | 21.4 | -17.59 | -5.47 | -17.88 | 573 |
| 51 | Volume breakout · 1h | breakout | 93.82 | -6.18 | 36 | 11.1 | 6.72 | 1.09 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.85 | -7.15 | 80 | 11.2 | -2.37 | -0.12 | -18.47 | 346 |
| 53 | Max aggression: 5-day momentum | meta | 92.53 | -7.47 | 5 | 40.0 | -18.80 | -1.59 | -29.56 | 29 |
| 54 | Opening range 15m | breakout | 92.48 | -7.52 | 113 | 19.5 | -18.52 | -5.50 | -19.24 | 692 |
| 55 | Donchian 20/10 · 1h | breakout | 91.50 | -8.50 | 39 | 15.4 | 2.81 | 0.55 | -16.18 | 223 |
| 56 | MACD zero-line · 1h | trend | 91.35 | -8.65 | 48 | 16.7 | -4.14 | -0.36 | -18.32 | 245 |
| 57 | Three white soldiers | momentum | 90.94 | -9.06 | 102 | 19.6 | -49.36 | -24.90 | -49.56 | 590 |
| 58 | VWAP momentum · 1h | momentum | 90.89 | -9.11 | 228 | 22.8 | -37.23 | -5.74 | -37.27 | 1270 |
| 59 | OBV trend · 1h | momentum | 90.73 | -9.27 | 106 | 12.3 | -12.65 | -1.40 | -26.73 | 338 |
| 60 | Heikin-Ashi · 1h | trend | 90.11 | -9.89 | 116 | 25.0 | -30.93 | -5.31 | -34.24 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.92 | -10.08 | 30 | 6.7 | -11.06 | -1.29 | -23.32 | 228 |
| 62 | ROC + volume · 1h | momentum | 87.42 | -12.58 | 107 | 15.9 | -9.00 | -1.07 | -23.04 | 412 |
| 63 | RSI(14) reversion | reversion | 85.91 | -14.09 | 219 | 32.4 | -70.71 | -19.51 | -71.16 | 1417 |
| 64 | Squeeze breakout | breakout | 77.56 | -22.44 | 247 | 15.8 | -62.31 | -19.01 | -62.31 | 1225 |
| 65 | VWAP reversion | reversion | 77.54 | -22.46 | 265 | 28.7 | -68.95 | -16.16 | -69.25 | 1379 |
| 66 | ROC + volume | momentum | 76.82 | -23.18 | 318 | 20.8 | -74.03 | -17.87 | -74.04 | 1647 |
| 67 | Donchian 55/20 | breakout | 76.03 | -23.97 | 258 | 17.4 | -68.97 | -15.35 | -68.97 | 1305 |
| 68 | EMA 20/50 cross | trend | 74.64 | -25.36 | 262 | 18.7 | -78.51 | -16.22 | -78.51 | 1481 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.28 | -19.60 | -65.28 | 931 |
| 70 | Z-score reversion | reversion | 71.67 | -28.33 | 350 | 28.0 | -85.04 | -25.38 | -85.04 | 2047 |
| 71 | MFI reversion | reversion | 70.08 | -29.92 | 348 | 21.0 | -86.98 | -30.70 | -86.99 | 2109 |
| 72 | Supertrend | trend | 69.72 | -30.28 | 349 | 20.3 | -87.04 | -22.49 | -87.04 | 1938 |
| 73 | Keltner breakout | breakout | 67.96 | -32.04 | 349 | 13.2 | -85.52 | -30.70 | -85.52 | 1889 |
| 74 | AI bee: Bizzy | ai | 67.58 | -32.42 | 603 | 9.0 | — | — | — | — |
| 75 | Ichimoku | trend | 66.85 | -33.15 | 317 | 8.8 | -82.24 | -24.92 | -82.24 | 1771 |
| 76 | AI bee: Boozy | ai | 65.91 | -34.09 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.56 | -35.44 | 398 | 9.3 | -89.71 | -37.38 | -89.72 | 2111 |
| 78 | MACD zero-line | trend | 63.33 | -36.67 | 449 | 15.6 | -91.54 | -31.23 | -91.54 | 2366 |
| 79 | Donchian 20/10 | breakout | 62.68 | -37.32 | 485 | 18.4 | -91.26 | -27.98 | -91.26 | 2674 |
| 80 | RSI momentum | momentum | 61.82 | -38.18 | 451 | 16.9 | -90.64 | -27.03 | -90.64 | 2381 |
| 81 | Triple EMA stack | trend | 60.26 | -39.74 | 501 | 15.4 | -93.37 | -32.69 | -93.37 | 2631 |
| 82 | Trend pullback | trend | 60.21 | -39.79 | 481 | 15.4 | -91.48 | -30.98 | -91.48 | 2348 |
| 83 | Bollinger breakout | breakout | 59.51 | -40.49 | 494 | 14.2 | -94.05 | -36.17 | -94.05 | 2823 |
| 84 | Stochastic reversion | reversion | 58.40 | -41.60 | 702 | 23.4 | -95.50 | -37.71 | -95.55 | 4033 |
| 85 | Bollinger reversion | reversion | 58.06 | -41.94 | 651 | 18.1 | -95.66 | -36.61 | -95.69 | 3674 |
| 86 | Consensus | meta | 57.41 | -42.59 | 477 | 9.9 | -94.72 | -27.30 | -94.72 | 2720 |
| 87 | EMA 9/21 cross | trend | 55.68 | -44.32 | 616 | 16.2 | -97.44 | -35.55 | -97.44 | 3558 |
| 88 | Connors RSI(2) | reversion | 53.93 | -46.07 | 669 | 20.0 | -96.58 | -35.49 | -96.58 | 3644 |
| 89 | OBV trend | momentum | 52.31 | -47.69 | 724 | 15.1 | -96.46 | -40.12 | -96.46 | 3606 |
| 90 | CCI reversion | reversion | 52.24 | -47.76 | 680 | 17.2 | -98.46 | -40.80 | -98.46 | 4686 |
| 91 | Candlestick reversal | reversion | 50.97 | -49.03 | 781 | 14.9 | -99.29 | -40.65 | -99.29 | 5626 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -32.31 | -98.72 | 5370 |
| 93 | Parabolic SAR | trend | 50.25 | -49.75 | 666 | 14.6 | -97.39 | -42.42 | -97.39 | 3679 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -47.71 | -99.73 | 6127 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -44.96 | -99.50 | 6096 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -52.83 | -99.90 | 8244 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T18:55 | CCI reversion | buy | TSLA | 7.46 | — | entry signal |
| 2026-10-06T18:55 | CCI reversion | sell | NVDA | 5.81 | -0.00 | exit signal |
| 2026-10-06T18:55 | Connors RSI(2) | buy | MSFT | 2.70 | — | rebalance up |
| 2026-10-06T18:55 | Connors RSI(2) | buy | AMZN | 2.70 | — | rebalance up |
| 2026-10-06T18:55 | Connors RSI(2) | sell | TSLA | 10.77 | -0.00 | exit signal |
| 2026-10-06T18:55 | Connors RSI(2) | sell | MSTR | 10.80 | -0.03 | exit signal |
| 2026-10-06T18:55 | Bollinger breakout | buy | GOOGL | 2.99 | — | rebalance up |
| 2026-10-06T18:55 | Bollinger breakout | buy | AAPL | 6.98 | — | rebalance up |
| 2026-10-06T18:55 | Bollinger breakout | sell | META | 11.92 | -0.03 | exit signal |
| 2026-10-06T18:55 | OBV trend | buy | SPY | 3.74 | — | entry |
| 2026-10-06T18:55 | OBV trend | sell | AMD | 3.74 | -0.00 | exit signal |
| 2026-10-06T18:55 | ADX DI cross | buy | NVDA | 16.12 | — | entry signal |
| 2026-10-06T18:52 | AI bee: Bizzy | buy | AMD | 9.70 | — | Jev: buy (buy p=0.57) |
| 2026-10-06T18:50 | Consensus | buy | SPY | 9.57 | — | entry |
| 2026-10-06T18:50 | Consensus | sell | NVDA | 8.21 | -0.00 | target is flat |
| 2026-10-06T18:50 | MFI reversion | sell | NVDA | 6.38 | -0.00 | exit signal |
| 2026-10-06T18:50 | CCI reversion | buy | UPRO | 3.11 | — | rebalance up |
| 2026-10-06T18:50 | CCI reversion | buy | SQQQ | 3.10 | — | rebalance up |
| 2026-10-06T18:50 | CCI reversion | sell | COIN | 5.79 | -0.04 | stop-loss |
| 2026-10-06T18:50 | Stochastic reversion | buy | MSTR | 2.32 | — | entry signal |
| 2026-10-06T18:50 | Stochastic reversion | buy | COIN | 5.84 | — | entry signal |
| 2026-10-06T18:50 | Stochastic reversion | sell | NVDA | 7.31 | -0.01 | exit signal |
| 2026-10-06T18:50 | VWAP reversion | buy | TNA | 11.06 | — | entry signal |
| 2026-10-06T18:50 | VWAP reversion | sell | ETHU | 11.06 | -0.13 | stop-loss |
| 2026-10-06T18:50 | Z-score reversion | buy | TSLA | 1.71 | — | rebalance up |
| 2026-10-06T18:50 | Z-score reversion | buy | MSFT | 10.24 | — | entry |
| 2026-10-06T18:50 | Z-score reversion | sell | ETHU | 11.95 | -0.14 | stop-loss |
| 2026-10-06T18:50 | Bollinger reversion | buy | TSLA | 9.67 | — | entry signal |
| 2026-10-06T18:50 | Bollinger reversion | sell | AMD | 9.68 | -0.00 | exit signal |
| 2026-10-06T18:50 | Connors RSI(2) | buy | TSLA | 10.77 | — | entry |
| 2026-10-06T18:50 | Connors RSI(2) | buy | MSTR | 3.10 | — | rebalance up |
| 2026-10-06T18:50 | Connors RSI(2) | buy | MSFT | 10.79 | — | entry |
| 2026-10-06T18:50 | Connors RSI(2) | buy | COIN | 3.10 | — | rebalance up |
| 2026-10-06T18:50 | Connors RSI(2) | buy | AMZN | 10.79 | — | entry signal |
| 2026-10-06T18:50 | Connors RSI(2) | sell | TQQQ | 7.71 | -0.00 | exit signal |
| 2026-10-06T18:50 | Connors RSI(2) | sell | TECL | 7.71 | -0.01 | target is flat |
| 2026-10-06T18:50 | Connors RSI(2) | sell | SPY | 6.75 | -0.01 | exit signal |
| 2026-10-06T18:50 | Connors RSI(2) | sell | SOXL | 7.70 | -0.01 | exit signal |
| 2026-10-06T18:50 | Connors RSI(2) | sell | QQQ | 7.71 | -0.01 | exit signal |
| 2026-10-06T18:50 | Candlestick reversal | buy | UPRO | 4.64 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 18:59:05.000150+00:00 -> 2026-10-06 19:09:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
