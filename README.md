# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-02T19:05:05.000122+00:00 · 9181 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.24 (-0.76%)

Closed trades 32, win rate 65.6%, fees £0.92, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, ETRA 12%, BBD 12%, BPRE 12%, GME 12%, NYAX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-01)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.51 · VIX 16.39 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.6, PLTR 8.5, META 7.7, AMD 7.5, TECL 7.1, BITX 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 32736 decisions in 2691 calls, $0.4054 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-02T19:05 | 4 / 21 / 5 | AMD 15%, NANC 18% |  |
| Breezy | 2026-10-02T19:05 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-02T19:05 | 4 / 24 / 2 | ETHU 51% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| Bollinger reversion · 1h | UPRO | 2.12 | +4.42% | 3 |
| Connors RSI(2) · 1h | TQQQ | 2.12 | +4.58% | 4 |
| Z-score reversion | MSFT | 2.05 | +2.32% | 5 |
| Stochastic reversion · 1h | SPY | 2.03 | +1.53% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.25 | 2.25 | 0 | — | 2.99 | 0.90 | -7.93 | 7 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.00 | 2.00 | 0 | — | -7.24 | -1.32 | -15.27 | 2 |
| 3 | Copy: Congress Democrats (NANC) | copy | 100.82 | 0.82 | 0 | — | 4.06 | 1.85 | -3.62 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 100.81 | 0.81 | 0 | — | -2.01 | -1.13 | -5.09 | 2 |
| 5 | Hold BTC | benchmark | 100.70 | 0.70 | 0 | — | 34.41 | 4.20 | -8.68 | 1 |
| 6 | Candlestick reversal · 1h | reversion | 100.59 | 0.59 | 53 | 37.7 | -22.85 | -5.18 | -26.03 | 488 |
| 7 | RSI(14) reversion · 1h | reversion | 100.30 | 0.30 | 10 | 60.0 | 4.59 | 1.33 | -6.57 | 116 |
| 8 | Hold SPY | benchmark | 100.08 | 0.08 | 0 | — | 1.87 | 1.11 | -3.66 | 1 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.96 | -0.04 | 15 | 33.3 | 4.00 | 1.99 | -1.46 | 86 |
| 12 | Bollinger reversion · 1h | reversion | 99.92 | -0.08 | 38 | 44.7 | -14.97 | -4.00 | -17.68 | 303 |
| 13 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 24 | 33.3 | -10.69 | -3.60 | -14.05 | 112 |
| 14 | Donchian 55/20 · 1h | breakout | 99.68 | -0.32 | 17 | 0.0 | 6.68 | 1.05 | -16.96 | 115 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.67 | -0.33 | 0 | — | -2.26 | -0.87 | -7.65 | 1 |
| 16 | Z-score reversion · 1h | reversion | 99.49 | -0.51 | 18 | 55.6 | 5.20 | 1.21 | -8.60 | 157 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.42 | -0.57 | 0 | — | -2.29 | -1.06 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.42 | -0.58 | 3 | 0.0 | 1.65 | 0.42 | -12.76 | 14 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 20 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.45 | -5.95 | -11.27 | 222 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Trend pullback · 1h | trend | 98.78 | -1.22 | 45 | 20.0 | -23.30 | -6.00 | -25.84 | 164 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 24 | CCI reversion · 1h | reversion | 98.59 | -1.41 | 63 | 49.2 | 1.51 | 0.41 | -12.41 | 413 |
| 25 | Stochastic reversion · 1h | reversion | 98.52 | -1.49 | 40 | 60.0 | -9.33 | -1.94 | -9.86 | 332 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 98.47 | -1.53 | 0 | — | 22.72 | 3.40 | -6.29 | 1 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.97 | -0.47 | -4.23 | 104 |
| 29 | Agent (rotation) | meta | 97.78 | -2.22 | 49 | 18.4 | -3.70 | -1.39 | -8.90 | 228 |
| 30 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.71 | -2.29 | 0 | — | 0.18 | 0.16 | -5.18 | 1 |
| 32 | EMA 20/50 cross · 1h | trend | 97.61 | -2.39 | 25 | 8.0 | 13.35 | 1.68 | -14.40 | 129 |
| 33 | Williams %R · 1h | reversion | 97.16 | -2.84 | 70 | 54.3 | -17.03 | -3.12 | -19.41 | 495 |
| 34 | Connors RSI(2) · 1h | reversion | 97.16 | -2.84 | 56 | 46.4 | -12.98 | -4.32 | -14.16 | 224 |
| 35 | MFI reversion · 1h | reversion | 96.64 | -3.36 | 68 | 29.4 | -6.00 | -0.97 | -16.99 | 121 |
| 36 | Agent (ML meta-label) | meta | 96.60 | -3.40 | 206 | 17.5 | 6.56 | 1.28 | -9.92 | 364 |
| 37 | Daily: Momentum burst | daily | 96.55 | -3.45 | 3 | 0.0 | -1.53 | -0.06 | -16.91 | 46 |
| 38 | Parabolic SAR · 1h | trend | 96.39 | -3.62 | 46 | 15.2 | -8.03 | -0.98 | -19.70 | 312 |
| 39 | Max aggression: 1-day momentum | meta | 96.32 | -3.68 | 5 | 40.0 | -23.22 | -1.16 | -41.28 | 43 |
| 40 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.84 | 2.87 | -4.73 | 199 |
| 41 | Supertrend · 1h | trend | 95.90 | -4.10 | 27 | 7.4 | 1.94 | 0.45 | -16.43 | 203 |
| 42 | ADX DI cross · 1h | trend | 95.87 | -4.13 | 41 | 12.2 | -5.63 | -0.79 | -13.84 | 271 |
| 43 | Copy: Insider buying | copy | 95.57 | -4.43 | 6 | 50.0 | -18.83 | -3.73 | -21.08 | 71 |
| 44 | MACD cross · 1h | trend | 95.47 | -4.53 | 69 | 14.5 | -16.23 | -2.60 | -18.46 | 487 |
| 45 | Squeeze breakout · 1h | breakout | 95.32 | -4.68 | 22 | 18.2 | 20.07 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.27 | -4.73 | 68 | 17.6 | -13.83 | -4.12 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.29 | -5.71 | 30 | 16.7 | 5.97 | 0.88 | -16.19 | 129 |
| 48 | RSI momentum · 1h | momentum | 93.84 | -6.16 | 40 | 2.5 | 1.09 | 0.34 | -16.65 | 229 |
| 49 | VWAP momentum · 1h | momentum | 93.76 | -6.24 | 170 | 22.9 | -40.38 | -6.31 | -42.55 | 1277 |
| 50 | Bollinger breakout · 1h | breakout | 93.23 | -6.77 | 36 | 16.7 | 5.42 | 0.89 | -12.06 | 293 |
| 51 | Opening range 15m | breakout | 93.15 | -6.85 | 85 | 16.5 | -16.09 | -4.56 | -18.84 | 695 |
| 52 | Triple EMA stack · 1h | trend | 92.99 | -7.01 | 50 | 8.0 | -8.90 | -0.89 | -23.88 | 244 |
| 53 | Three white soldiers | momentum | 92.81 | -7.19 | 64 | 17.2 | -49.18 | -26.09 | -49.34 | 595 |
| 54 | Volume breakout · 1h | breakout | 92.56 | -7.44 | 30 | 6.7 | 2.98 | 0.60 | -12.60 | 130 |
| 55 | EMA 9/21 cross · 1h | trend | 91.65 | -8.35 | 68 | 11.8 | -5.09 | -0.50 | -18.47 | 342 |
| 56 | Max aggression: 5-day momentum | meta | 91.48 | -8.52 | 5 | 40.0 | -21.23 | -1.89 | -29.56 | 30 |
| 57 | Heikin-Ashi · 1h | trend | 91.40 | -8.60 | 85 | 25.9 | -32.72 | -5.79 | -33.58 | 687 |
| 58 | Donchian 20/10 · 1h | breakout | 90.71 | -9.29 | 31 | 12.9 | -1.12 | 0.08 | -16.18 | 222 |
| 59 | MACD zero-line · 1h | trend | 90.71 | -9.29 | 36 | 8.3 | -5.59 | -0.52 | -18.32 | 237 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 96 | 10.4 | -15.91 | -1.84 | -27.04 | 340 |
| 61 | Keltner breakout · 1h | breakout | 88.34 | -11.66 | 22 | 0.0 | -12.26 | -1.48 | -23.19 | 217 |
| 62 | RSI(14) reversion | reversion | 87.52 | -12.48 | 171 | 35.1 | -72.40 | -20.99 | -72.47 | 1461 |
| 63 | ROC + volume · 1h | momentum | 87.19 | -12.81 | 84 | 14.3 | -13.82 | -1.79 | -24.44 | 421 |
| 64 | Squeeze breakout | breakout | 83.07 | -16.93 | 170 | 15.9 | -60.35 | -18.30 | -60.88 | 1207 |
| 65 | Donchian 55/20 | breakout | 82.46 | -17.54 | 168 | 18.5 | -68.08 | -15.25 | -68.40 | 1308 |
| 66 | Volume breakout | breakout | 80.20 | -19.80 | 155 | 14.2 | -64.09 | -20.07 | -64.13 | 912 |
| 67 | EMA 20/50 cross | trend | 80.16 | -19.84 | 191 | 18.8 | -78.85 | -16.71 | -79.03 | 1478 |
| 68 | ROC + volume | momentum | 79.82 | -20.18 | 257 | 20.2 | -73.74 | -17.90 | -74.00 | 1658 |
| 69 | VWAP reversion | reversion | 79.65 | -20.35 | 193 | 26.4 | -71.24 | -17.11 | -71.33 | 1393 |
| 70 | AI bee: Bizzy | ai | 79.03 | -20.96 | 381 | 10.8 | — | — | — | — |
| 71 | AI bee: Boozy | ai | 77.86 | -22.14 | 135 | 4.4 | — | — | — | — |
| 72 | Z-score reversion | reversion | 77.82 | -22.18 | 266 | 31.6 | -85.82 | -26.92 | -85.82 | 2112 |
| 73 | MFI reversion | reversion | 76.22 | -23.78 | 256 | 21.9 | -88.29 | -33.45 | -88.32 | 2133 |
| 74 | Keltner breakout | breakout | 76.22 | -23.78 | 243 | 13.6 | -85.32 | -32.34 | -85.34 | 1905 |
| 75 | Ichimoku | trend | 75.86 | -24.14 | 206 | 10.2 | -81.51 | -25.46 | -81.62 | 1768 |
| 76 | Supertrend | trend | 75.22 | -24.78 | 263 | 20.5 | -87.33 | -23.49 | -87.40 | 1949 |
| 77 | Donchian 20/10 | breakout | 72.42 | -27.58 | 335 | 19.1 | -90.80 | -27.90 | -90.86 | 2684 |
| 78 | MACD zero-line | trend | 71.81 | -28.19 | 324 | 16.7 | -91.69 | -32.34 | -91.69 | 2364 |
| 79 | ADX DI cross | trend | 71.75 | -28.25 | 297 | 9.4 | -89.77 | -41.39 | -89.77 | 2116 |
| 80 | Trend pullback | trend | 70.99 | -29.01 | 310 | 16.8 | -91.66 | -33.12 | -91.66 | 2355 |
| 81 | Triple EMA stack | trend | 70.85 | -29.15 | 346 | 16.8 | -93.19 | -33.74 | -93.26 | 2636 |
| 82 | Bollinger breakout | breakout | 70.06 | -29.95 | 339 | 16.2 | -93.95 | -38.31 | -93.95 | 2854 |
| 83 | RSI momentum | momentum | 70.03 | -29.96 | 321 | 15.6 | -90.64 | -27.70 | -90.73 | 2401 |
| 84 | Stochastic reversion | reversion | 67.94 | -32.06 | 504 | 25.6 | -95.84 | -41.18 | -95.85 | 4068 |
| 85 | Consensus ⏸ | meta | 67.00 | -33.00 | 319 | 9.7 | -94.81 | -29.10 | -94.82 | 2667 |
| 86 | Bollinger reversion | reversion | 66.44 | -33.56 | 490 | 18.6 | -95.89 | -40.23 | -95.90 | 3728 |
| 87 | Connors RSI(2) ⏸ | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.65 | -38.97 | -96.65 | 3656 |
| 88 | EMA 9/21 cross | trend | 65.45 | -34.55 | 448 | 17.9 | -97.41 | -37.54 | -97.43 | 3561 |
| 89 | OBV trend | momentum | 64.09 | -35.91 | 494 | 16.0 | -96.10 | -42.84 | -96.12 | 3589 |
| 90 | Candlestick reversal ⏸ | reversion | 63.68 | -36.32 | 565 | 16.8 | -99.34 | -43.62 | -99.35 | 5660 |
| 91 | CCI reversion | reversion | 63.57 | -36.43 | 450 | 17.3 | -98.50 | -44.16 | -98.51 | 4725 |
| 92 | VWAP momentum | momentum | 62.81 | -37.19 | 520 | 9.4 | -98.60 | -33.40 | -98.61 | 5314 |
| 93 | Parabolic SAR | trend | 61.46 | -38.54 | 462 | 14.7 | -97.16 | -47.91 | -97.17 | 3670 |
| 94 | MACD cross ⏸ | trend | 59.48 | -40.52 | 545 | 14.9 | -99.72 | -52.85 | -99.72 | 6168 |
| 95 | Williams %R ⏸ | reversion | 59.36 | -40.64 | 582 | 23.0 | -99.52 | -49.21 | -99.52 | 6149 |
| 96 | Heikin-Ashi ⏸ | trend | 58.33 | -41.67 | 502 | 10.0 | -99.90 | -62.62 | -99.90 | 8355 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-02T19:05 | AI bee: Boozy | buy | ETHU | 39.92 | — | Jev: buy (buy p=0.51) |
| 2026-10-02T19:05 | AI bee: Boozy | sell | COIN | 39.25 | 0.05 | Jev: add (buy p=0.51) |
| 2026-10-02T19:05 | CCI reversion | buy | BTC-USD | 3.35 | — | entry signal |
| 2026-10-02T19:05 | CCI reversion | buy | BITX | 3.35 | — | entry signal |
| 2026-10-02T19:05 | Stochastic reversion | buy | SOL-USD | 5.23 | — | entry |
| 2026-10-02T19:05 | Stochastic reversion | sell | COIN | 4.88 | 0.01 | exit signal |
| 2026-10-02T19:05 | Z-score reversion | buy | XRP-USD | 11.14 | — | entry signal |
| 2026-10-02T19:05 | Z-score reversion | buy | SOL-USD | 11.14 | — | entry signal |
| 2026-10-02T19:05 | Z-score reversion | sell | LABU | 4.43 | -0.04 | rebalance down |
| 2026-10-02T19:05 | Z-score reversion | sell | ETH-USD | 8.19 | -0.03 | rebalance down |
| 2026-10-02T19:05 | Z-score reversion | sell | BTC-USD | 8.29 | -0.05 | rebalance down |
| 2026-10-02T19:05 | Z-score reversion | sell | BITX | 4.44 | 0.00 | rebalance down |
| 2026-10-02T19:05 | Bollinger reversion | sell | COIN | 5.55 | 0.03 | exit signal |
| 2026-10-02T19:05 | Three white soldiers | buy | COIN | 23.20 | — | entry signal |
| 2026-10-02T19:05 | Bollinger breakout | sell | MSFT | 17.49 | -0.04 | exit signal |
| 2026-10-02T19:05 | MACD zero-line | buy | UPRO | 10.80 | — | entry signal |
| 2026-10-02T19:05 | MACD zero-line | buy | TSLA | 14.37 | — | entry signal |
| 2026-10-02T19:05 | MACD zero-line | buy | SPY | 14.37 | — | entry signal |
| 2026-10-02T19:05 | MACD zero-line | sell | MSFT | 3.59 | -0.00 | rebalance down |
| 2026-10-02T19:05 | Triple EMA stack | buy | TSLA | 10.12 | — | entry signal |
| 2026-10-02T19:05 | Triple EMA stack | buy | TNA | 10.12 | — | entry signal |
| 2026-10-02T19:05 | Triple EMA stack | sell | UPRO | 7.60 | -0.01 | rebalance down |
| 2026-10-02T19:05 | Triple EMA stack | sell | SPY | 4.05 | -0.00 | rebalance down |
| 2026-10-02T19:05 | Triple EMA stack | sell | AMD | 4.04 | -0.00 | rebalance down |
| 2026-10-02T19:05 | Triple EMA stack | sell | AAPL | 7.59 | -0.01 | rebalance down |
| 2026-10-02T19:05 | EMA 9/21 cross | buy | TSLA | 6.52 | — | entry signal |
| 2026-10-02T19:05 | EMA 9/21 cross | buy | TECL | 8.18 | — | entry signal |
| 2026-10-02T19:05 | EMA 9/21 cross | sell | MSFT | 4.91 | -0.01 | rebalance down |
| 2026-10-02T19:05 | EMA 9/21 cross | sell | AMD | 4.89 | -0.01 | rebalance down |
| 2026-10-02T19:05 | EMA 9/21 cross | sell | AAPL | 4.90 | -0.01 | rebalance down |
| 2026-10-02T19:00 | AI bee: Bizzy | buy | AMD | 12.26 | — | Jev: buy (buy p=0.62) |
| 2026-10-02T19:00 | Agent (ML meta-label) | sell | SOL-USD | 3.81 | -0.09 | selected signal exited |
| 2026-10-02T19:00 | Agent (ML meta-label) | sell | DOGE-USD | 3.57 | -0.18 | selected signal exited |
| 2026-10-02T19:00 | Stochastic reversion · 1h | buy | XRP-USD | 1.14 | — | entry signal |
| 2026-10-02T19:00 | Stochastic reversion · 1h | buy | SOL-USD | 9.86 | — | entry signal |
| 2026-10-02T19:00 | Stochastic reversion · 1h | buy | ETH-USD | 5.23 | — | rebalance up |
| 2026-10-02T19:00 | Stochastic reversion · 1h | buy | BTC-USD | 9.86 | — | entry signal |
| 2026-10-02T19:00 | Stochastic reversion · 1h | sell | MSTR | 6.48 | -0.06 | rebalance down |
| 2026-10-02T19:00 | Stochastic reversion · 1h | sell | ETHU | 6.38 | -0.21 | rebalance down |
| 2026-10-02T19:00 | Stochastic reversion · 1h | sell | BITX | 6.36 | -0.06 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
