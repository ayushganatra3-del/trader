# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T18:35:05.000116+00:00 · 10332 ticks

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

Today: 13722 decisions in 2745 calls, $0.1919 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T18:35 | 1 / 1 / 3 | AMZN 16%, COIN 16%, MSTR 16% |  |
| Breezy | 2026-10-03T18:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T18:35 | 2 / 3 / 0 | MSTR 62% |  |

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
| 3 | Hold BTC | benchmark | 101.54 | 1.53 | 0 | — | 33.79 | 4.14 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -8.78 | -2.84 | -14.05 | 114 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.92 | -5.48 | -26.23 | 495 |
| 8 | RSI(14) reversion · 1h | reversion | 100.60 | 0.60 | 10 | 60.0 | 5.17 | 1.48 | -6.57 | 119 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.82 | -3.95 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.79 | -0.21 | 18 | 55.6 | 5.67 | 1.30 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 5.99 | 0.96 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.02 | -0.98 | 44 | 59.1 | -8.08 | -1.67 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.51 | 0.41 | -12.41 | 416 |
| 24 | Trend pullback · 1h | trend | 98.81 | -1.19 | 45 | 20.0 | -21.37 | -5.45 | -25.34 | 155 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.91 | -2.09 | 50 | 20.0 | -4.87 | -1.86 | -9.74 | 234 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.75 | 1.72 | -14.40 | 133 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -11.64 | -3.92 | -14.21 | 221 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.73 | -3.07 | -19.41 | 500 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 1.01 | 0.33 | -11.90 | 364 |
| 37 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -6.16 | -0.70 | -19.70 | 304 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.60 | 2.81 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -7.48 | -1.24 | -16.99 | 124 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 3.38 | 0.64 | -16.43 | 197 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.87 | -3.78 | -21.08 | 69 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -6.02 | -0.86 | -13.84 | 275 |
| 44 | MACD cross · 1h | trend | 95.50 | -4.50 | 71 | 15.5 | -13.89 | -2.23 | -17.27 | 484 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.81 | 0.44 | -16.65 | 227 |
| 49 | VWAP momentum · 1h | momentum | 93.17 | -6.83 | 175 | 22.3 | -41.12 | -6.50 | -41.92 | 1288 |
| 50 | Bollinger breakout · 1h | breakout | 93.14 | -6.86 | 36 | 16.7 | 5.95 | 0.96 | -12.06 | 293 |
| 51 | Triple EMA stack · 1h | trend | 93.11 | -6.89 | 50 | 8.0 | -7.25 | -0.68 | -23.88 | 241 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 2.74 | 0.57 | -12.60 | 128 |
| 54 | EMA 9/21 cross · 1h | trend | 91.71 | -8.29 | 68 | 11.8 | -5.35 | -0.54 | -18.47 | 344 |
| 55 | Three white soldiers | momentum | 91.29 | -8.71 | 74 | 14.9 | -49.54 | -26.28 | -49.65 | 594 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | MACD zero-line · 1h | trend | 90.79 | -9.21 | 38 | 13.2 | -4.22 | -0.34 | -18.32 | 235 |
| 58 | Heikin-Ashi · 1h | trend | 90.61 | -9.39 | 90 | 24.4 | -33.02 | -5.86 | -33.62 | 688 |
| 59 | Donchian 20/10 · 1h | breakout | 90.56 | -9.44 | 31 | 12.9 | -0.10 | 0.20 | -16.18 | 223 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -13.06 | -1.45 | -26.45 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.35 | -1.35 | -23.19 | 213 |
| 62 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -11.40 | -1.45 | -23.16 | 420 |
| 63 | RSI(14) reversion | reversion | 87.07 | -12.93 | 181 | 34.3 | -71.92 | -20.59 | -71.92 | 1450 |
| 64 | Squeeze breakout | breakout | 81.22 | -18.77 | 186 | 15.1 | -60.98 | -18.62 | -61.74 | 1216 |
| 65 | Donchian 55/20 | breakout | 80.80 | -19.20 | 180 | 17.8 | -68.44 | -15.43 | -68.50 | 1309 |
| 66 | ROC + volume | momentum | 79.60 | -20.40 | 259 | 20.1 | -73.50 | -17.78 | -73.91 | 1667 |
| 67 | VWAP reversion | reversion | 79.43 | -20.57 | 213 | 28.6 | -71.25 | -17.32 | -71.32 | 1388 |
| 68 | Volume breakout | breakout | 78.97 | -21.03 | 164 | 13.4 | -64.15 | -20.14 | -64.15 | 911 |
| 69 | EMA 20/50 cross | trend | 78.11 | -21.89 | 207 | 17.4 | -79.11 | -16.86 | -79.23 | 1488 |
| 70 | Z-score reversion | reversion | 76.66 | -23.34 | 285 | 29.8 | -85.73 | -26.73 | -85.73 | 2111 |
| 71 | MFI reversion | reversion | 75.16 | -24.84 | 276 | 21.7 | -88.04 | -33.40 | -88.05 | 2123 |
| 72 | AI bee: Bizzy | ai | 74.98 | -25.02 | 443 | 9.3 | — | — | — | — |
| 73 | Keltner breakout | breakout | 74.19 | -25.81 | 260 | 13.1 | -85.56 | -32.88 | -85.56 | 1905 |
| 74 | Supertrend | trend | 73.38 | -26.62 | 281 | 19.9 | -87.37 | -23.53 | -87.43 | 1951 |
| 75 | Ichimoku | trend | 73.38 | -26.62 | 226 | 9.3 | -81.95 | -25.90 | -81.95 | 1775 |
| 76 | AI bee: Boozy ⏸ | ai | 72.08 | -27.92 | 170 | 4.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 70.15 | -29.85 | 315 | 9.8 | -89.80 | -41.40 | -89.80 | 2120 |
| 78 | Donchian 20/10 | breakout | 69.56 | -30.44 | 363 | 18.5 | -91.13 | -28.68 | -91.14 | 2694 |
| 79 | Trend pullback | trend | 69.37 | -30.63 | 330 | 16.4 | -91.59 | -32.87 | -91.59 | 2351 |
| 80 | MACD zero-line | trend | 69.27 | -30.73 | 354 | 16.1 | -91.84 | -32.82 | -91.85 | 2377 |
| 81 | RSI momentum | momentum | 67.32 | -32.68 | 346 | 15.0 | -90.88 | -28.16 | -90.88 | 2408 |
| 82 | Bollinger breakout | breakout | 67.11 | -32.89 | 368 | 15.2 | -94.03 | -38.73 | -94.03 | 2854 |
| 83 | Triple EMA stack | trend | 67.04 | -32.96 | 386 | 15.3 | -93.48 | -34.44 | -93.51 | 2652 |
| 84 | Stochastic reversion | reversion | 65.77 | -34.23 | 544 | 24.6 | -95.78 | -40.97 | -95.78 | 4065 |
| 85 | Consensus | meta | 65.27 | -34.73 | 335 | 9.3 | -94.29 | -28.45 | -94.29 | 2623 |
| 86 | Bollinger reversion | reversion | 64.35 | -35.65 | 521 | 17.5 | -95.86 | -39.81 | -95.86 | 3720 |
| 87 | Connors RSI(2) | reversion | 63.89 | -36.11 | 446 | 18.2 | -96.60 | -38.81 | -96.60 | 3656 |
| 88 | EMA 9/21 cross | trend | 61.77 | -38.23 | 495 | 17.0 | -97.50 | -38.20 | -97.50 | 3575 |
| 89 | Candlestick reversal | reversion | 60.82 | -39.18 | 598 | 15.9 | -99.35 | -43.71 | -99.35 | 5667 |
| 90 | CCI reversion | reversion | 60.48 | -39.52 | 505 | 16.6 | -98.52 | -44.40 | -98.52 | 4735 |
| 91 | OBV trend | momentum | 60.14 | -39.86 | 549 | 14.6 | -96.30 | -43.63 | -96.30 | 3645 |
| 92 | VWAP momentum | momentum | 59.40 | -40.60 | 556 | 9.0 | -98.66 | -34.38 | -98.66 | 5331 |
| 93 | Parabolic SAR ⏸ | trend | 57.56 | -42.44 | 513 | 13.8 | -97.27 | -47.99 | -97.27 | 3683 |
| 94 | Williams %R | reversion | 56.16 | -43.84 | 623 | 21.5 | -99.52 | -49.52 | -99.52 | 6153 |
| 95 | MACD cross ⏸ | trend | 55.83 | -44.17 | 586 | 13.8 | -99.72 | -53.05 | -99.72 | 6175 |
| 96 | Heikin-Ashi ⏸ | trend | 54.73 | -45.27 | 544 | 9.2 | -99.90 | -62.59 | -99.90 | 8354 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T18:35 | Consensus | sell | BTC-USD | 16.28 | -0.11 | target is flat |
| 2026-10-03T18:35 | Connors RSI(2) | sell | SOL-USD | 15.95 | -0.09 | exit signal |
| 2026-10-03T18:35 | Squeeze breakout | sell | ETH-USD | 20.33 | -0.11 | stop-loss |
| 2026-10-03T18:35 | Keltner breakout | sell | ETH-USD | 18.53 | -0.11 | stop-loss |
| 2026-10-03T18:35 | Bollinger breakout | sell | ETH-USD | 13.44 | -0.07 | stop-loss |
| 2026-10-03T18:30 | CCI reversion | buy | DOGE-USD | 15.13 | — | entry signal |
| 2026-10-03T18:30 | Williams %R | buy | DOGE-USD | 14.05 | — | entry signal |
| 2026-10-03T18:30 | Connors RSI(2) | sell | XRP-USD | 15.96 | -0.08 | exit signal |
| 2026-10-03T18:30 | Connors RSI(2) | sell | DOGE-USD | 15.95 | -0.10 | exit signal |
| 2026-10-03T18:30 | Candlestick reversal | buy | DOGE-USD | 15.22 | — | entry signal |
| 2026-10-03T18:30 | OBV trend | buy | XRP-USD | 15.05 | — | entry signal |
| 2026-10-03T18:30 | MACD zero-line | sell | ETH-USD | 17.26 | -0.07 | exit signal |
| 2026-10-03T18:25 | Williams %R | buy | XRP-USD | 14.06 | — | entry signal |
| 2026-10-03T18:25 | Connors RSI(2) | buy | ETH-USD | 16.01 | — | entry signal |
| 2026-10-03T18:25 | Ichimoku | sell | SOL-USD | 18.39 | -0.11 | exit signal |
| 2026-10-03T18:25 | Supertrend | buy | DOGE-USD | 3.66 | — | rebalance up |
| 2026-10-03T18:25 | Supertrend | sell | BTC-USD | 3.66 | -0.02 | rebalance down |
| 2026-10-03T18:20 | Consensus | sell | SOL-USD | 16.28 | -0.13 | target is flat |
| 2026-10-03T18:20 | Connors RSI(2) | buy | XRP-USD | 16.04 | — | entry signal |
| 2026-10-03T18:20 | Connors RSI(2) | buy | SOL-USD | 16.04 | — | entry signal |
| 2026-10-03T18:20 | Volume breakout | sell | ETH-USD | 19.65 | -0.13 | exit signal |
| 2026-10-03T18:20 | Squeeze breakout | sell | SOL-USD | 20.27 | -0.14 | exit signal |
| 2026-10-03T18:20 | Bollinger breakout | sell | XRP-USD | 16.77 | -0.13 | stop-loss |
| 2026-10-03T18:20 | Bollinger breakout | sell | SOL-USD | 13.44 | -0.08 | exit signal |
| 2026-10-03T18:20 | Donchian 20/10 | buy | BTC-USD | 10.35 | — | rebalance up |
| 2026-10-03T18:20 | Donchian 20/10 | sell | DOGE-USD | 17.32 | -0.16 | stop-loss |
| 2026-10-03T18:20 | OBV trend | sell | XRP-USD | 8.99 | -0.06 | exit signal |
| 2026-10-03T18:20 | OBV trend | sell | SOL-USD | 12.02 | -0.06 | exit signal |
| 2026-10-03T18:20 | RSI momentum | buy | BTC-USD | 10.03 | — | rebalance up |
| 2026-10-03T18:20 | RSI momentum | sell | DOGE-USD | 16.76 | -0.15 | stop-loss |
| 2026-10-03T18:20 | Trend pullback | sell | DOGE-USD | 17.26 | -0.14 | exit signal |
| 2026-10-03T18:20 | Ichimoku | sell | DOGE-USD | 18.24 | -0.16 | stop-loss |
| 2026-10-03T18:20 | Triple EMA stack | buy | ETH-USD | 6.60 | — | rebalance up |
| 2026-10-03T18:20 | Triple EMA stack | sell | DOGE-USD | 16.57 | -0.11 | exit signal |
| 2026-10-03T18:20 | EMA 9/21 cross | sell | DOGE-USD | 12.06 | -0.08 | exit signal |
| 2026-10-03T18:15 | AI bee: Bizzy | sell | DOGE-USD | 10.78 | -0.08 | Jev: sell (sell p=0.90) after 11 min |
| 2026-10-03T18:15 | Consensus | sell | ETH-USD | 16.27 | -0.11 | target is flat |
| 2026-10-03T18:15 | Connors RSI(2) | buy | DOGE-USD | 16.05 | — | entry signal |
| 2026-10-03T18:15 | Squeeze breakout | sell | DOGE-USD | 20.27 | -0.16 | exit signal |
| 2026-10-03T18:15 | Bollinger breakout | buy | XRP-USD | 3.37 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
