# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T15:05:05.000165+00:00 · 10161 ticks

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

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 11157 decisions in 2232 calls, $0.1561 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T15:05 | 1 / 4 / 0 | AMZN 16%, COIN 16%, MSTR 16% |  |
| Breezy | 2026-10-03T15:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T15:05 | 1 / 4 / 0 | MSTR 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion · 1h | UPRO | 2.43 | +6.89% | 3 |
| Stochastic reversion · 1h | SPY | 2.28 | +2.53% | 3 |
| Connors RSI(2) · 1h | COIN | 2.23 | +6.43% | 5 |
| Stochastic reversion | MSFT | 2.20 | +2.95% | 13 |
| RSI(14) reversion | SQQQ | 2.18 | +4.27% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.27 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 101.35 | 1.35 | 0 | — | 34.06 | 4.17 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.62 | -3.14 | -14.05 | 116 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.66 | -5.41 | -26.14 | 495 |
| 8 | RSI(14) reversion · 1h | reversion | 100.61 | 0.61 | 10 | 60.0 | 4.93 | 1.41 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.82 | -3.95 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.74 | -0.26 | 18 | 55.6 | 5.62 | 1.29 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 5.99 | 0.96 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.04 | -0.96 | 43 | 58.1 | -7.16 | -1.45 | -9.82 | 332 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 2.27 | 0.54 | -12.41 | 417 |
| 24 | Trend pullback · 1h | trend | 98.80 | -1.20 | 45 | 20.0 | -21.65 | -5.54 | -25.34 | 156 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.89 | -2.11 | 50 | 20.0 | -4.88 | -1.87 | -9.74 | 234 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.75 | 1.72 | -14.40 | 132 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -11.71 | -3.94 | -14.21 | 222 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.70 | -3.06 | -19.41 | 500 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 0.49 | 0.24 | -12.30 | 361 |
| 37 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -7.06 | -0.84 | -19.70 | 308 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.60 | 2.81 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -7.45 | -1.24 | -16.99 | 124 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 2.56 | 0.53 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.87 | -3.78 | -21.08 | 69 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.74 | -0.64 | -13.84 | 268 |
| 44 | MACD cross · 1h | trend | 95.46 | -4.54 | 71 | 15.5 | -14.47 | -2.32 | -17.27 | 486 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.56 | 0.94 | -16.19 | 126 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.79 | 0.44 | -16.65 | 227 |
| 49 | Bollinger breakout · 1h | breakout | 93.15 | -6.85 | 36 | 16.7 | 5.99 | 0.96 | -12.06 | 292 |
| 50 | VWAP momentum · 1h | momentum | 93.12 | -6.88 | 175 | 22.3 | -41.28 | -6.53 | -42.00 | 1289 |
| 51 | Triple EMA stack · 1h | trend | 93.10 | -6.90 | 50 | 8.0 | -7.89 | -0.76 | -23.88 | 241 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 2.74 | 0.57 | -12.60 | 128 |
| 54 | Three white soldiers | momentum | 91.77 | -8.23 | 71 | 15.5 | -49.35 | -26.33 | -49.39 | 592 |
| 55 | EMA 9/21 cross · 1h | trend | 91.72 | -8.28 | 68 | 11.8 | -5.08 | -0.50 | -18.47 | 344 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | MACD zero-line · 1h | trend | 90.81 | -9.19 | 38 | 13.2 | -3.66 | -0.27 | -18.32 | 232 |
| 58 | Donchian 20/10 · 1h | breakout | 90.65 | -9.35 | 31 | 12.9 | 0.01 | 0.22 | -16.18 | 219 |
| 59 | Heikin-Ashi · 1h | trend | 90.57 | -9.43 | 90 | 24.4 | -33.05 | -5.87 | -33.62 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -13.28 | -1.48 | -26.45 | 338 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.62 | -1.39 | -23.19 | 214 |
| 62 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -11.98 | -1.52 | -23.57 | 422 |
| 63 | RSI(14) reversion | reversion | 87.07 | -12.93 | 181 | 34.3 | -71.96 | -20.60 | -71.96 | 1451 |
| 64 | Squeeze breakout | breakout | 81.82 | -18.18 | 181 | 15.5 | -60.59 | -18.45 | -61.45 | 1211 |
| 65 | Donchian 55/20 | breakout | 80.92 | -19.08 | 179 | 17.9 | -68.67 | -15.59 | -68.67 | 1311 |
| 66 | ROC + volume | momentum | 79.77 | -20.23 | 258 | 20.2 | -73.53 | -17.79 | -73.89 | 1667 |
| 67 | VWAP reversion | reversion | 79.43 | -20.57 | 213 | 28.6 | -71.25 | -17.36 | -71.32 | 1390 |
| 68 | Volume breakout | breakout | 79.33 | -20.67 | 160 | 13.8 | -64.16 | -20.06 | -64.16 | 909 |
| 69 | EMA 20/50 cross | trend | 78.09 | -21.91 | 207 | 17.4 | -79.16 | -16.90 | -79.22 | 1488 |
| 70 | Z-score reversion | reversion | 76.66 | -23.34 | 285 | 29.8 | -85.73 | -26.73 | -85.73 | 2111 |
| 71 | AI bee: Bizzy | ai | 75.60 | -24.40 | 434 | 9.4 | — | — | — | — |
| 72 | MFI reversion | reversion | 75.19 | -24.81 | 275 | 21.8 | -88.08 | -33.70 | -88.08 | 2126 |
| 73 | Keltner breakout | breakout | 74.90 | -25.10 | 254 | 13.4 | -85.49 | -32.82 | -85.49 | 1905 |
| 74 | Ichimoku | trend | 73.86 | -26.14 | 222 | 9.5 | -81.88 | -25.93 | -81.88 | 1773 |
| 75 | Supertrend | trend | 73.45 | -26.55 | 280 | 20.0 | -87.40 | -23.63 | -87.42 | 1952 |
| 76 | AI bee: Boozy ⏸ | ai | 72.08 | -27.92 | 170 | 4.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 70.15 | -29.85 | 315 | 9.8 | -89.80 | -41.40 | -89.80 | 2120 |
| 78 | Donchian 20/10 | breakout | 70.01 | -29.99 | 360 | 18.6 | -91.06 | -28.55 | -91.08 | 2692 |
| 79 | Trend pullback | trend | 69.70 | -30.30 | 327 | 16.5 | -91.55 | -32.72 | -91.55 | 2347 |
| 80 | MACD zero-line | trend | 69.50 | -30.50 | 350 | 16.3 | -91.83 | -32.87 | -91.83 | 2378 |
| 81 | RSI momentum | momentum | 67.75 | -32.25 | 343 | 15.2 | -90.89 | -28.37 | -90.91 | 2409 |
| 82 | Bollinger breakout | breakout | 67.74 | -32.26 | 361 | 15.5 | -93.98 | -38.66 | -93.98 | 2853 |
| 83 | Triple EMA stack | trend | 67.54 | -32.46 | 381 | 15.5 | -93.48 | -34.86 | -93.48 | 2653 |
| 84 | Consensus | meta | 66.24 | -33.76 | 325 | 9.5 | -94.49 | -28.54 | -94.50 | 2644 |
| 85 | Stochastic reversion | reversion | 65.92 | -34.08 | 541 | 24.8 | -95.79 | -41.05 | -95.79 | 4065 |
| 86 | Connors RSI(2) | reversion | 64.57 | -35.43 | 439 | 18.5 | -96.57 | -38.49 | -96.57 | 3648 |
| 87 | Bollinger reversion | reversion | 64.44 | -35.56 | 520 | 17.5 | -95.85 | -39.74 | -95.85 | 3719 |
| 88 | EMA 9/21 cross | trend | 62.13 | -37.87 | 490 | 17.1 | -97.50 | -38.46 | -97.50 | 3575 |
| 89 | Candlestick reversal | reversion | 61.02 | -38.98 | 596 | 15.9 | -99.35 | -43.82 | -99.35 | 5668 |
| 90 | OBV trend | momentum | 60.90 | -39.10 | 541 | 14.8 | -96.30 | -44.40 | -96.30 | 3644 |
| 91 | CCI reversion | reversion | 60.82 | -39.18 | 500 | 16.8 | -98.51 | -44.24 | -98.51 | 4730 |
| 92 | VWAP momentum | momentum | 59.51 | -40.49 | 554 | 9.0 | -98.67 | -34.58 | -98.67 | 5337 |
| 93 | Parabolic SAR ⏸ | trend | 57.56 | -42.44 | 513 | 13.8 | -97.27 | -49.08 | -97.27 | 3682 |
| 94 | Williams %R | reversion | 56.42 | -43.58 | 619 | 21.6 | -99.52 | -49.78 | -99.52 | 6153 |
| 95 | MACD cross ⏸ | trend | 55.83 | -44.17 | 586 | 13.8 | -99.72 | -54.47 | -99.72 | 6179 |
| 96 | Heikin-Ashi ⏸ | trend | 54.73 | -45.27 | 544 | 9.2 | -99.90 | -64.08 | -99.90 | 8353 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T15:05 | Candlestick reversal | sell | BTC-USD | 15.20 | -0.08 | exit signal |
| 2026-10-03T15:05 | Keltner breakout | sell | DOGE-USD | 18.69 | -0.10 | stop-loss |
| 2026-10-03T15:05 | Bollinger breakout | sell | ETH-USD | 16.91 | -0.12 | stop-loss |
| 2026-10-03T15:05 | Bollinger breakout | sell | DOGE-USD | 16.94 | -0.09 | stop-loss |
| 2026-10-03T15:05 | Donchian 20/10 | sell | ETH-USD | 17.46 | -0.13 | stop-loss |
| 2026-10-03T15:05 | RSI momentum | sell | ETH-USD | 16.90 | -0.12 | stop-loss |
| 2026-10-03T15:05 | ADX DI cross | sell | BTC-USD | 17.45 | -0.12 | exit signal |
| 2026-10-03T15:05 | EMA 9/21 cross | buy | BTC-USD | 6.15 | — | rebalance up |
| 2026-10-03T15:05 | EMA 9/21 cross | sell | ETH-USD | 15.42 | -0.11 | stop-loss |
| 2026-10-03T15:02 | EMA 9/21 cross | buy | BTC-USD | 3.11 | — | rebalance up |
| 2026-10-03T15:02 | EMA 9/21 cross | sell | SOL-USD | 3.11 | -0.01 | rebalance down |
| 2026-10-03T15:00 | AI bee: Bizzy | sell | XRP-USD | 11.88 | -0.08 | Jev: sell (sell p=0.56) after 10 min |
| 2026-10-03T15:00 | Consensus | buy | SOL-USD | 16.58 | — | entry |
| 2026-10-03T15:00 | Triple EMA stack · 1h | buy | SOL-USD | 2.77 | — | entry signal |
| 2026-10-03T15:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 5.73 | — | entry signal |
| 2026-10-03T15:00 | Donchian 55/20 | buy | SOL-USD | 20.27 | — | entry signal |
| 2026-10-03T15:00 | Ichimoku | buy | SOL-USD | 18.49 | — | entry signal |
| 2026-10-03T15:00 | MACD zero-line | buy | ETH-USD | 17.40 | — | entry signal |
| 2026-10-03T15:00 | Triple EMA stack | buy | BTC-USD | 16.92 | — | entry signal |
| 2026-10-03T15:00 | EMA 9/21 cross | buy | BTC-USD | 6.32 | — | entry signal |
| 2026-10-03T15:00 | EMA 9/21 cross | sell | XRP-USD | 3.11 | -0.01 | rebalance down |
| 2026-10-03T15:00 | EMA 9/21 cross | sell | DOGE-USD | 3.21 | -0.00 | rebalance down |
| 2026-10-03T14:57 | AI bee: Bizzy | sell | SOL-USD | 11.11 | -0.05 | Jev: sell (sell p=0.57) after 10 min |
| 2026-10-03T14:50 | AI bee: Bizzy | buy | XRP-USD | 11.96 | — | Jev: buy (buy p=0.63) |
| 2026-10-03T14:50 | Consensus | buy | XRP-USD | 16.60 | — | entry |
| 2026-10-03T14:50 | CCI reversion | sell | XRP-USD | 15.21 | -0.02 | exit signal |
| 2026-10-03T14:50 | CCI reversion | sell | SOL-USD | 15.18 | -0.04 | exit signal |
| 2026-10-03T14:50 | CCI reversion | sell | ETH-USD | 15.19 | -0.07 | exit signal |
| 2026-10-03T14:50 | Williams %R | sell | SOL-USD | 14.18 | -0.05 | exit signal |
| 2026-10-03T14:50 | Williams %R | sell | ETH-USD | 14.09 | -0.07 | exit signal |
| 2026-10-03T14:50 | Stochastic reversion | sell | SOL-USD | 16.47 | -0.03 | exit signal |
| 2026-10-03T14:50 | Stochastic reversion | sell | ETH-USD | 16.45 | -0.09 | exit signal |
| 2026-10-03T14:50 | Z-score reversion | sell | ETH-USD | 19.13 | -0.09 | exit signal |
| 2026-10-03T14:50 | Connors RSI(2) | sell | BTC-USD | 16.08 | -0.08 | exit signal |
| 2026-10-03T14:50 | Candlestick reversal | sell | SOL-USD | 15.26 | -0.03 | take-profit |
| 2026-10-03T14:50 | Candlestick reversal | sell | ETH-USD | 15.24 | -0.07 | exit signal |
| 2026-10-03T14:50 | Volume breakout | buy | XRP-USD | 19.88 | — | entry signal |
| 2026-10-03T14:50 | Volume breakout | buy | SOL-USD | 19.88 | — | entry signal |
| 2026-10-03T14:50 | Squeeze breakout | buy | XRP-USD | 20.48 | — | entry signal |
| 2026-10-03T14:50 | Keltner breakout | buy | XRP-USD | 18.80 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
