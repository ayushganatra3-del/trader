# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T16:35:05.000147+00:00 · 11450 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.25 (-0.76%)

Closed trades 33, win rate 66.7%, fees £1.04, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, GME 12%, BPRE 12%, PAM 12%, CX 12%, GPUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 12449 decisions in 2491 calls, $0.1739 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T16:35 | 2 / 3 / 0 | AMZN 17%, COIN 17%, MSTR 16% |  |
| Breezy | 2026-10-04T16:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T16:35 | 2 / 3 / 0 | MSTR 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.66 | +5.70% | 4 |
| Bollinger reversion · 1h | UPRO | 2.43 | +6.89% | 3 |
| RSI(14) reversion | SQQQ | 2.18 | +4.27% | 5 |
| Bollinger reversion · 1h | SPY | 2.00 | +1.40% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.94 | +3.45% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.27 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 101.95 | 1.95 | 0 | — | 33.34 | 4.09 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.78 | -5.44 | -26.10 | 494 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 4.95 | 1.42 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.82 | -3.95 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.77 | -0.23 | 20 | 55.0 | 6.18 | 1.41 | -8.60 | 158 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.41 | 1.01 | -16.96 | 114 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.36 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.02 | -0.98 | 45 | 60.0 | -8.07 | -1.66 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.83 | 0.46 | -12.41 | 412 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 47 | 21.3 | -21.73 | -5.57 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -3.94 | -1.48 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.86 | 1.73 | -14.40 | 135 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.51 | -2.49 | 59 | 44.1 | -11.73 | -3.95 | -14.21 | 221 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.14 | -3.16 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 1.68 | 0.45 | -10.84 | 364 |
| 37 | Parabolic SAR · 1h | trend | 96.42 | -3.58 | 48 | 16.7 | -5.46 | -0.60 | -19.70 | 302 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.82 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.45 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -25.95 | -1.41 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 95.92 | -4.08 | 28 | 7.1 | 3.31 | 0.63 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 43 | MACD cross · 1h | trend | 95.76 | -4.24 | 71 | 15.5 | -12.68 | -2.00 | -17.27 | 478 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.62 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.27 | -4.73 | 22 | 18.2 | 19.90 | 2.87 | -8.06 | 117 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.02 | 40 | 2.5 | 1.39 | 0.38 | -16.65 | 232 |
| 49 | VWAP momentum · 1h | momentum | 93.29 | -6.71 | 178 | 21.9 | -39.54 | -6.25 | -40.07 | 1281 |
| 50 | Triple EMA stack · 1h | trend | 93.15 | -6.85 | 50 | 8.0 | -8.13 | -0.79 | -23.88 | 244 |
| 51 | Bollinger breakout · 1h | breakout | 93.14 | -6.86 | 38 | 15.8 | 6.33 | 1.00 | -12.06 | 297 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.05 | 0.61 | -12.60 | 128 |
| 54 | EMA 9/21 cross · 1h | trend | 91.79 | -8.21 | 69 | 11.6 | -3.58 | -0.29 | -18.47 | 340 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | MACD zero-line · 1h | trend | 90.94 | -9.06 | 38 | 13.2 | -3.23 | -0.21 | -18.32 | 236 |
| 57 | Three white soldiers | momentum | 90.81 | -9.19 | 77 | 14.3 | -49.66 | -26.60 | -49.92 | 594 |
| 58 | Donchian 20/10 · 1h | breakout | 90.79 | -9.21 | 31 | 12.9 | -0.01 | 0.21 | -16.18 | 224 |
| 59 | Heikin-Ashi · 1h | trend | 90.50 | -9.50 | 94 | 23.4 | -32.51 | -5.75 | -33.92 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.85 | -1.42 | -26.45 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.02 | -1.30 | -23.19 | 212 |
| 62 | ROC + volume · 1h | momentum | 87.17 | -12.83 | 84 | 14.3 | -10.40 | -1.30 | -23.16 | 419 |
| 63 | RSI(14) reversion | reversion | 86.96 | -13.04 | 182 | 34.1 | -70.79 | -20.31 | -70.85 | 1432 |
| 64 | Donchian 55/20 | breakout | 79.34 | -20.66 | 193 | 16.6 | -68.70 | -15.60 | -68.75 | 1311 |
| 65 | ROC + volume | momentum | 79.32 | -20.68 | 261 | 19.9 | -73.13 | -17.56 | -73.74 | 1660 |
| 66 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.93 | -17.22 | -69.93 | 1364 |
| 67 | Squeeze breakout | breakout | 78.78 | -21.22 | 204 | 13.7 | -61.98 | -19.07 | -62.91 | 1230 |
| 68 | Volume breakout | breakout | 77.69 | -22.30 | 173 | 12.7 | -64.35 | -20.23 | -64.35 | 912 |
| 69 | EMA 20/50 cross | trend | 77.53 | -22.47 | 217 | 16.6 | -79.22 | -16.89 | -79.28 | 1490 |
| 70 | Z-score reversion | reversion | 76.00 | -24.00 | 292 | 29.1 | -85.09 | -26.73 | -85.11 | 2091 |
| 71 | MFI reversion | reversion | 73.92 | -26.08 | 288 | 21.2 | -87.66 | -32.77 | -87.71 | 2113 |
| 72 | Supertrend | trend | 72.57 | -27.43 | 294 | 19.0 | -87.44 | -23.54 | -87.50 | 1952 |
| 73 | AI bee: Bizzy | ai | 71.58 | -28.42 | 492 | 8.3 | — | — | — | — |
| 74 | Keltner breakout | breakout | 71.03 | -28.97 | 285 | 11.9 | -85.71 | -32.88 | -85.75 | 1906 |
| 75 | ADX DI cross | trend | 69.67 | -30.33 | 320 | 9.7 | -89.63 | -40.72 | -89.65 | 2113 |
| 76 | Ichimoku | trend | 69.48 | -30.52 | 261 | 8.0 | -82.60 | -26.14 | -82.70 | 1795 |
| 77 | AI bee: Boozy | ai | 67.97 | -32.03 | 196 | 4.1 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.84 | -33.16 | 375 | 15.2 | -92.05 | -33.46 | -92.05 | 2386 |
| 79 | Donchian 20/10 | breakout | 66.76 | -33.23 | 390 | 17.2 | -91.31 | -28.85 | -91.35 | 2701 |
| 80 | RSI momentum | momentum | 65.33 | -34.67 | 370 | 14.3 | -91.00 | -28.35 | -91.01 | 2413 |
| 81 | Trend pullback | trend | 64.70 | -35.30 | 378 | 14.3 | -91.79 | -34.15 | -91.79 | 2376 |
| 82 | Stochastic reversion | reversion | 63.94 | -36.06 | 569 | 23.6 | -95.65 | -40.78 | -95.68 | 4054 |
| 83 | Triple EMA stack | trend | 63.80 | -36.20 | 421 | 14.3 | -93.77 | -35.03 | -93.77 | 2671 |
| 84 | Bollinger reversion | reversion | 63.09 | -36.91 | 536 | 17.0 | -95.68 | -39.86 | -95.68 | 3697 |
| 85 | Bollinger breakout | breakout | 63.01 | -36.99 | 407 | 13.8 | -94.25 | -39.44 | -94.28 | 2869 |
| 86 | Consensus | meta | 61.62 | -38.38 | 371 | 8.6 | -94.26 | -28.18 | -94.26 | 2626 |
| 87 | EMA 9/21 cross | trend | 59.33 | -40.67 | 527 | 16.1 | -97.59 | -38.75 | -97.60 | 3593 |
| 88 | Connors RSI(2) | reversion | 59.21 | -40.79 | 500 | 16.2 | -96.63 | -39.27 | -96.63 | 3659 |
| 89 | CCI reversion | reversion | 58.10 | -41.90 | 536 | 15.7 | -98.47 | -45.09 | -98.47 | 4725 |
| 90 | Candlestick reversal | reversion | 58.09 | -41.91 | 632 | 15.0 | -99.31 | -44.37 | -99.31 | 5642 |
| 91 | OBV trend | momentum | 57.52 | -42.48 | 583 | 13.9 | -96.43 | -44.37 | -96.45 | 3663 |
| 92 | VWAP momentum | momentum | 56.68 | -43.33 | 594 | 8.4 | -98.71 | -34.85 | -98.72 | 5366 |
| 93 | Parabolic SAR ⏸ | trend | 54.05 | -45.95 | 551 | 12.9 | -97.39 | -47.98 | -97.40 | 3705 |
| 94 | Williams %R | reversion | 53.12 | -46.88 | 667 | 20.1 | -99.50 | -50.00 | -99.50 | 6145 |
| 95 | MACD cross ⏸ | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -54.64 | -99.73 | 6199 |
| 96 | Heikin-Ashi ⏸ | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -63.50 | -99.90 | 8363 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T16:35 | Consensus | buy | SOL-USD | 15.43 | — | entry |
| 2026-10-04T16:35 | Consensus | buy | ETH-USD | 15.43 | — | entry |
| 2026-10-04T16:35 | MFI reversion | buy | SOL-USD | 18.49 | — | entry signal |
| 2026-10-04T16:35 | CCI reversion | buy | XRP-USD | 14.55 | — | entry signal |
| 2026-10-04T16:35 | CCI reversion | buy | SOL-USD | 14.55 | — | entry signal |
| 2026-10-04T16:35 | Williams %R | sell | ETH-USD | 13.26 | -0.06 | exit signal |
| 2026-10-04T16:35 | Candlestick reversal | buy | XRP-USD | 14.54 | — | entry signal |
| 2026-10-04T16:35 | Candlestick reversal | buy | SOL-USD | 14.54 | — | entry signal |
| 2026-10-04T16:35 | Trend pullback | buy | XRP-USD | 12.96 | — | entry signal |
| 2026-10-04T16:35 | Trend pullback | buy | SOL-USD | 12.97 | — | entry signal |
| 2026-10-04T16:35 | Trend pullback | buy | ETH-USD | 12.97 | — | entry signal |
| 2026-10-04T16:35 | Trend pullback | buy | BTC-USD | 12.97 | — | entry signal |
| 2026-10-04T16:35 | Trend pullback | sell | DOGE-USD | 3.25 | -0.02 | rebalance down |
| 2026-10-04T16:35 | Triple EMA stack | buy | ETH-USD | 15.98 | — | entry signal |
| 2026-10-04T16:35 | Triple EMA stack | buy | BTC-USD | 15.98 | — | entry signal |
| 2026-10-04T16:35 | EMA 20/50 cross | buy | ETH-USD | 19.40 | — | entry signal |
| 2026-10-04T16:35 | EMA 9/21 cross | buy | BTC-USD | 14.84 | — | entry signal |
| 2026-10-04T16:30 | RSI momentum | sell | XRP-USD | 16.31 | -0.11 | exit signal |
| 2026-10-04T16:30 | Triple EMA stack | sell | XRP-USD | 15.95 | -0.11 | exit signal |
| 2026-10-04T16:30 | EMA 9/21 cross | sell | XRP-USD | 14.81 | -0.10 | exit signal |
| 2026-10-04T16:25 | Consensus | sell | XRP-USD | 15.34 | -0.12 | target is flat |
| 2026-10-04T16:25 | Candlestick reversal | sell | SOL-USD | 14.47 | -0.10 | exit signal |
| 2026-10-04T16:25 | OBV trend | sell | XRP-USD | 14.31 | -0.11 | exit signal |
| 2026-10-04T16:25 | Trend pullback | sell | XRP-USD | 16.22 | -0.09 | exit signal |
| 2026-10-04T16:25 | Trend pullback | sell | BTC-USD | 16.15 | -0.11 | exit signal |
| 2026-10-04T16:20 | Consensus | buy | XRP-USD | 15.46 | — | entry |
| 2026-10-04T16:20 | OBV trend | buy | XRP-USD | 14.42 | — | entry signal |
| 2026-10-04T16:20 | OBV trend | sell | BTC-USD | 14.34 | -0.09 | exit signal |
| 2026-10-04T16:15 | Consensus | sell | SOL-USD | 15.39 | -0.09 | target is flat |
| 2026-10-04T16:15 | Connors RSI(2) | sell | SOL-USD | 14.77 | -0.10 | exit signal |
| 2026-10-04T16:15 | Connors RSI(2) | sell | ETH-USD | 14.76 | -0.07 | exit signal |
| 2026-10-04T16:15 | Connors RSI(2) | sell | BTC-USD | 14.77 | -0.08 | exit signal |
| 2026-10-04T16:15 | OBV trend | buy | BTC-USD | 14.43 | — | entry signal |
| 2026-10-04T16:15 | VWAP momentum | buy | ETH-USD | 10.82 | — | entry signal |
| 2026-10-04T16:15 | Trend pullback | buy | BTC-USD | 16.26 | — | entry signal |
| 2026-10-04T16:10 | Consensus | buy | SOL-USD | 15.48 | — | entry |
| 2026-10-04T16:10 | Williams %R | buy | XRP-USD | 13.32 | — | entry signal |
| 2026-10-04T16:10 | Williams %R | buy | SOL-USD | 13.32 | — | entry signal |
| 2026-10-04T16:10 | Williams %R | buy | ETH-USD | 13.32 | — | entry signal |
| 2026-10-04T16:10 | Williams %R | buy | BTC-USD | 13.32 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
