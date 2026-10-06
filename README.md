# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T16:31:05.000192+00:00 · 13646 ticks

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

Today: 21298 decisions in 2330 calls, $0.2715 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T16:31 | 0 / 24 / 6 | AMD 15% |  |
| Breezy | 2026-10-06T16:31 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-06T16:31 | 2 / 26 / 2 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.47 | 6.47 | 0 | — | -1.07 | -0.07 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -9.17 | -2.90 | -13.93 | 113 |
| 3 | Hold BTC | benchmark | 102.18 | 2.18 | 0 | — | 32.43 | 3.91 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 102.10 | 2.10 | 0 | — | 0.15 | 0.13 | -5.09 | 1 |
| 5 | Donchian 55/20 · 1h | breakout | 102.03 | 2.03 | 17 | 0.0 | 9.55 | 1.35 | -16.96 | 111 |
| 6 | Copy: Congress Democrats (NANC) | copy | 102.00 | 2.00 | 0 | — | 4.07 | 1.91 | -3.62 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 8 | Daily: Bullish score | daily | 101.69 | 1.69 | 3 | 0.0 | 5.64 | 0.94 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.20 | 1.20 | 0 | — | 1.08 | 0.70 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.56 | 0.56 | 67 | 38.8 | -18.34 | -3.98 | -20.89 | 495 |
| 13 | Stochastic reversion · 1h | reversion | 100.32 | 0.32 | 56 | 64.3 | -7.37 | -1.50 | -10.59 | 326 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.21 | 0.21 | 0 | — | -1.75 | -0.65 | -7.65 | 1 |
| 15 | EMA 20/50 cross · 1h | trend | 100.21 | 0.21 | 28 | 7.1 | 14.41 | 1.78 | -15.31 | 142 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 100.15 | 0.15 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.95 | 1.91 | -1.59 | 84 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 19 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 20 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 21 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 99.65 | -0.35 | 0 | — | 18.56 | 2.83 | -6.29 | 1 |
| 23 | Connors RSI(2) · 1h | reversion | 99.62 | -0.38 | 72 | 44.4 | -12.04 | -4.36 | -15.92 | 220 |
| 24 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.41 | 1.24 | -6.57 | 118 |
| 25 | Trend pullback · 1h | trend | 99.36 | -0.65 | 64 | 25.0 | -20.48 | -5.95 | -24.51 | 166 |
| 26 | Bollinger reversion · 1h | reversion | 98.88 | -1.12 | 48 | 47.9 | -14.89 | -3.84 | -16.99 | 303 |
| 27 | Z-score reversion · 1h | reversion | 98.80 | -1.20 | 22 | 54.5 | 4.40 | 1.05 | -8.60 | 149 |
| 28 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -1.15 | -0.59 | -4.23 | 103 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.99 | 0.33 | -16.91 | 41 |
| 30 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 31 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -8.90 | -5.39 | -10.19 | 230 |
| 32 | Williams %R · 1h | reversion | 97.59 | -2.41 | 84 | 53.6 | -19.15 | -3.60 | -20.55 | 492 |
| 33 | Copy: Insider buying | copy | 97.53 | -2.48 | 9 | 55.6 | -15.88 | -2.94 | -21.08 | 73 |
| 34 | Agent (rotation) | meta | 97.46 | -2.54 | 62 | 29.0 | -2.38 | -0.70 | -8.81 | 262 |
| 35 | ADX DI cross · 1h | trend | 97.26 | -2.74 | 41 | 12.2 | -3.33 | -0.43 | -13.84 | 260 |
| 36 | Supertrend · 1h | trend | 97.14 | -2.86 | 32 | 9.4 | 3.17 | 0.61 | -16.43 | 213 |
| 37 | Agent (ML meta-label) | meta | 97.11 | -2.88 | 257 | 14.8 | 0.48 | 0.23 | -13.03 | 376 |
| 38 | Daily: SMA 20/50 cross · AAPL | daily | 96.99 | -3.01 | 0 | — | -0.38 | -0.06 | -5.18 | 1 |
| 39 | Parabolic SAR · 1h | trend | 96.84 | -3.16 | 62 | 16.1 | -2.64 | -0.16 | -19.45 | 300 |
| 40 | CCI reversion · 1h | reversion | 96.67 | -3.33 | 71 | 49.3 | 0.05 | 0.17 | -12.41 | 408 |
| 41 | MACD cross · 1h | trend | 96.06 | -3.94 | 82 | 19.5 | -11.58 | -1.87 | -17.27 | 473 |
| 42 | RSI momentum · 1h | momentum | 95.80 | -4.20 | 45 | 2.2 | 1.92 | 0.45 | -16.65 | 230 |
| 43 | Squeeze breakout · 1h | breakout | 95.58 | -4.42 | 29 | 20.7 | 15.75 | 2.64 | -8.06 | 107 |
| 44 | Ichimoku · 1h | trend | 95.32 | -4.68 | 32 | 15.6 | 8.91 | 1.23 | -15.84 | 124 |
| 45 | MFI reversion · 1h | reversion | 95.16 | -4.84 | 74 | 28.4 | -10.16 | -1.76 | -16.99 | 119 |
| 46 | Triple EMA stack · 1h | trend | 95.04 | -4.96 | 56 | 10.7 | -9.42 | -0.97 | -24.08 | 255 |
| 47 | Max aggression: 1-day momentum | meta | 94.84 | -5.16 | 7 | 42.9 | -23.61 | -1.22 | -37.31 | 42 |
| 48 | Bollinger breakout · 1h | breakout | 94.76 | -5.24 | 48 | 25.0 | 7.39 | 1.11 | -12.06 | 296 |
| 49 | Gap and go | momentum | 94.36 | -5.64 | 46 | 6.5 | 6.85 | 1.79 | -6.43 | 201 |
| 50 | Opening range 30m | breakout | 94.16 | -5.83 | 94 | 22.3 | -17.40 | -5.42 | -17.61 | 572 |
| 51 | Volume breakout · 1h | breakout | 93.94 | -6.06 | 36 | 11.1 | 6.83 | 1.11 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 93.08 | -6.92 | 79 | 11.4 | -1.68 | -0.03 | -18.47 | 345 |
| 53 | Opening range 15m | breakout | 92.60 | -7.40 | 110 | 20.0 | -18.41 | -5.47 | -19.04 | 692 |
| 54 | Max aggression: 5-day momentum | meta | 92.55 | -7.45 | 5 | 40.0 | -18.80 | -1.59 | -29.56 | 29 |
| 55 | Donchian 20/10 · 1h | breakout | 91.62 | -8.38 | 38 | 15.8 | 2.02 | 0.46 | -16.18 | 224 |
| 56 | MACD zero-line · 1h | trend | 91.59 | -8.40 | 43 | 18.6 | -1.79 | -0.04 | -18.32 | 252 |
| 57 | Three white soldiers | momentum | 91.07 | -8.93 | 99 | 20.2 | -49.27 | -24.82 | -49.52 | 587 |
| 58 | VWAP momentum · 1h | momentum | 91.03 | -8.97 | 226 | 23.0 | -38.26 | -5.90 | -38.26 | 1274 |
| 59 | OBV trend · 1h | momentum | 90.91 | -9.09 | 103 | 11.7 | -12.25 | -1.35 | -26.73 | 337 |
| 60 | Heikin-Ashi · 1h | trend | 90.22 | -9.78 | 111 | 23.4 | -31.47 | -5.44 | -34.14 | 703 |
| 61 | Keltner breakout · 1h | breakout | 90.02 | -9.98 | 30 | 6.7 | -12.16 | -1.42 | -23.31 | 228 |
| 62 | ROC + volume · 1h | momentum | 87.74 | -12.26 | 101 | 15.8 | -9.02 | -1.07 | -23.04 | 413 |
| 63 | RSI(14) reversion | reversion | 85.83 | -14.17 | 218 | 32.1 | -70.92 | -19.77 | -71.29 | 1429 |
| 64 | VWAP reversion | reversion | 78.07 | -21.93 | 260 | 29.2 | -68.58 | -15.93 | -69.17 | 1376 |
| 65 | Squeeze breakout | breakout | 77.79 | -22.21 | 246 | 15.9 | -62.55 | -19.18 | -62.59 | 1226 |
| 66 | ROC + volume | momentum | 76.92 | -23.08 | 318 | 20.8 | -74.05 | -17.96 | -74.05 | 1664 |
| 67 | Donchian 55/20 | breakout | 76.21 | -23.79 | 253 | 17.4 | -68.84 | -15.32 | -68.84 | 1304 |
| 68 | EMA 20/50 cross | trend | 74.90 | -25.10 | 260 | 18.8 | -78.42 | -16.18 | -78.42 | 1476 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.51 | -19.83 | -65.51 | 939 |
| 70 | Z-score reversion | reversion | 72.25 | -27.75 | 344 | 28.2 | -85.18 | -25.44 | -85.21 | 2054 |
| 71 | MFI reversion | reversion | 70.61 | -29.39 | 335 | 21.5 | -86.92 | -30.46 | -87.01 | 2098 |
| 72 | Supertrend | trend | 70.10 | -29.90 | 346 | 20.5 | -87.06 | -22.57 | -87.06 | 1931 |
| 73 | Keltner breakout | breakout | 68.19 | -31.81 | 346 | 13.0 | -85.51 | -30.62 | -85.52 | 1894 |
| 74 | AI bee: Bizzy | ai | 67.78 | -32.22 | 595 | 8.9 | — | — | — | — |
| 75 | Ichimoku | trend | 67.16 | -32.84 | 311 | 8.7 | -82.42 | -25.02 | -82.42 | 1776 |
| 76 | AI bee: Boozy | ai | 66.28 | -33.72 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 65.13 | -34.87 | 382 | 8.9 | -89.68 | -37.92 | -89.70 | 2106 |
| 78 | MACD zero-line | trend | 63.68 | -36.32 | 441 | 15.9 | -91.57 | -31.30 | -91.57 | 2366 |
| 79 | Donchian 20/10 | breakout | 63.04 | -36.96 | 479 | 18.6 | -91.30 | -28.26 | -91.30 | 2675 |
| 80 | RSI momentum | momentum | 62.14 | -37.86 | 446 | 16.6 | -90.71 | -27.20 | -90.71 | 2384 |
| 81 | Triple EMA stack | trend | 60.63 | -39.37 | 491 | 15.5 | -93.39 | -32.96 | -93.39 | 2633 |
| 82 | Trend pullback | trend | 60.54 | -39.46 | 467 | 15.6 | -91.47 | -31.13 | -91.47 | 2344 |
| 83 | Bollinger breakout | breakout | 59.84 | -40.16 | 490 | 14.3 | -94.10 | -36.55 | -94.10 | 2831 |
| 84 | Stochastic reversion | reversion | 58.66 | -41.34 | 673 | 23.0 | -95.51 | -37.86 | -95.58 | 4029 |
| 85 | Bollinger reversion | reversion | 58.40 | -41.60 | 627 | 17.9 | -95.58 | -36.80 | -95.64 | 3679 |
| 86 | Consensus | meta | 57.82 | -42.17 | 458 | 10.0 | -94.67 | -27.43 | -94.67 | 2702 |
| 87 | EMA 9/21 cross | trend | 56.04 | -43.96 | 603 | 16.4 | -97.45 | -35.96 | -97.45 | 3555 |
| 88 | Connors RSI(2) | reversion | 54.23 | -45.77 | 635 | 19.7 | -96.59 | -35.67 | -96.59 | 3632 |
| 89 | OBV trend | momentum | 52.60 | -47.40 | 711 | 15.2 | -96.51 | -40.61 | -96.51 | 3611 |
| 90 | CCI reversion | reversion | 52.51 | -47.49 | 650 | 16.5 | -98.44 | -41.00 | -98.44 | 4689 |
| 91 | Candlestick reversal | reversion | 51.49 | -48.51 | 746 | 14.7 | -99.28 | -40.92 | -99.29 | 5607 |
| 92 | VWAP momentum | momentum | 50.96 | -49.04 | 692 | 8.7 | -98.73 | -32.74 | -98.73 | 5412 |
| 93 | Parabolic SAR | trend | 50.67 | -49.33 | 651 | 14.9 | -97.39 | -42.57 | -97.39 | 3671 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -48.24 | -99.73 | 6125 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -44.96 | -99.50 | 6081 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -53.65 | -99.90 | 8248 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T16:31 | MFI reversion · 1h | sell | SPY | 24.21 | 0.16 | exit signal |
| 2026-10-06T16:31 | Connors RSI(2) · 1h | buy | AAPL | 24.91 | — | entry signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | buy | UPRO | 16.68 | — | rebalance up |
| 2026-10-06T16:31 | VWAP momentum · 1h | buy | SPY | 18.19 | — | rebalance up |
| 2026-10-06T16:31 | VWAP momentum · 1h | buy | AMZN | 18.18 | — | rebalance up |
| 2026-10-06T16:31 | VWAP momentum · 1h | buy | AMD | 16.46 | — | rebalance up |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | TQQQ | 4.56 | -0.03 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | TNA | 4.52 | -0.07 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | TECL | 5.90 | 0.11 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | SOXL | 4.55 | -0.04 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | QQQ | 4.58 | -0.01 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | PLTR | 4.56 | -0.03 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | MSFT | 4.58 | -0.02 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | IWM | 4.56 | -0.02 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | ETHU | 4.54 | -0.05 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | BITX | 4.52 | -0.07 | exit signal |
| 2026-10-06T16:31 | VWAP momentum · 1h | sell | AAPL | 4.57 | -0.02 | exit signal |
| 2026-10-06T16:31 | Heikin-Ashi · 1h | buy | AMZN | 7.52 | — | entry signal |
| 2026-10-06T16:31 | Heikin-Ashi · 1h | buy | AMD | 7.52 | — | entry signal |
| 2026-10-06T16:31 | Heikin-Ashi · 1h | sell | ETHU | 5.61 | -0.07 | exit signal |
| 2026-10-06T16:31 | EMA 9/21 cross · 1h | buy | DOGE-USD | 1.13 | — | entry |
| 2026-10-06T16:31 | EMA 9/21 cross · 1h | buy | COIN | 4.23 | — | entry |
| 2026-10-06T16:31 | EMA 9/21 cross · 1h | sell | AAPL | 5.36 | -0.06 | exit signal |
| 2026-10-06T16:31 | MFI reversion | buy | TECL | 17.67 | — | entry |
| 2026-10-06T16:31 | MFI reversion | buy | DOGE-USD | 17.67 | — | entry signal |
| 2026-10-06T16:31 | MFI reversion | sell | ETHU | 17.65 | -0.05 | target is flat |
| 2026-10-06T16:31 | CCI reversion | buy | XRP-USD | 1.18 | — | entry |
| 2026-10-06T16:31 | CCI reversion | buy | SOXL | 4.04 | — | entry signal |
| 2026-10-06T16:31 | CCI reversion | buy | ETHU | 4.04 | — | entry |
| 2026-10-06T16:31 | CCI reversion | buy | BTC-USD | 4.04 | — | entry signal |
| 2026-10-06T16:31 | CCI reversion | buy | BITX | 4.04 | — | entry signal |
| 2026-10-06T16:31 | CCI reversion | sell | PLTR | 3.49 | -0.00 | rebalance down |
| 2026-10-06T16:31 | CCI reversion | sell | NVDA | 3.47 | -0.01 | rebalance down |
| 2026-10-06T16:31 | CCI reversion | sell | MSFT | 3.49 | -0.00 | rebalance down |
| 2026-10-06T16:31 | CCI reversion | sell | LABU | 3.41 | 0.00 | rebalance down |
| 2026-10-06T16:31 | CCI reversion | sell | IWM | 3.49 | -0.01 | rebalance down |
| 2026-10-06T16:31 | VWAP reversion | buy | COIN | 19.52 | — | entry signal |
| 2026-10-06T16:31 | Connors RSI(2) | buy | UPRO | 5.42 | — | entry signal |
| 2026-10-06T16:31 | Connors RSI(2) | buy | GOOGL | 5.42 | — | entry signal |
| 2026-10-06T16:31 | Connors RSI(2) | sell | TQQQ | 4.87 | -0.03 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 16:31:05.000192+00:00 -> 2026-10-06 16:41:05.000192+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
