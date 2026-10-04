# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T18:05:05.000141+00:00 · 11525 ticks

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

Today: 13574 decisions in 2716 calls, $0.1897 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T18:05 | 0 / 4 / 1 | AMZN 17%, COIN 17%, MSTR 16% |  |
| Breezy | 2026-10-04T18:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T18:05 | 0 / 4 / 1 | MSTR 66% |  |

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
| 3 | Hold BTC | benchmark | 101.98 | 1.98 | 0 | — | 33.23 | 4.07 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -24.22 | -5.55 | -26.56 | 497 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 4.57 | 1.32 | -6.57 | 118 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.80 | -3.94 | -17.52 | 304 |
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
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.85 | 0.47 | -12.41 | 412 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 47 | 21.3 | -21.72 | -5.57 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -3.94 | -1.48 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.55 | 1.70 | -14.40 | 137 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.51 | -2.49 | 59 | 44.1 | -11.73 | -3.95 | -14.21 | 221 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.14 | -3.16 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 0.92 | 0.31 | -12.26 | 371 |
| 37 | Parabolic SAR · 1h | trend | 96.39 | -3.61 | 48 | 16.7 | -5.50 | -0.61 | -19.70 | 303 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.82 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.45 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -25.95 | -1.41 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 95.90 | -4.10 | 28 | 7.1 | 3.35 | 0.64 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 43 | MACD cross · 1h | trend | 95.81 | -4.19 | 71 | 15.5 | -12.55 | -1.98 | -17.27 | 478 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.65 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.24 | -4.76 | 22 | 18.2 | 20.06 | 2.89 | -8.06 | 117 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.02 | 40 | 2.5 | 1.82 | 0.44 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.25 | -6.75 | 178 | 21.9 | -39.52 | -6.24 | -40.07 | 1282 |
| 50 | Triple EMA stack · 1h | trend | 93.14 | -6.86 | 50 | 8.0 | -8.17 | -0.80 | -23.88 | 245 |
| 51 | Bollinger breakout · 1h | breakout | 93.13 | -6.87 | 38 | 15.8 | 6.37 | 1.01 | -12.06 | 297 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.16 | 0.63 | -12.60 | 128 |
| 54 | EMA 9/21 cross · 1h | trend | 91.77 | -8.23 | 69 | 11.6 | -3.77 | -0.32 | -18.47 | 341 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | MACD zero-line · 1h | trend | 90.91 | -9.09 | 38 | 13.2 | -3.18 | -0.21 | -18.32 | 236 |
| 57 | Donchian 20/10 · 1h | breakout | 90.83 | -9.17 | 31 | 12.9 | 0.03 | 0.22 | -16.18 | 224 |
| 58 | Three white soldiers | momentum | 90.81 | -9.19 | 77 | 14.3 | -49.60 | -26.51 | -49.92 | 593 |
| 59 | Heikin-Ashi · 1h | trend | 90.69 | -9.31 | 95 | 24.2 | -32.39 | -5.71 | -33.92 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.69 | -1.40 | -26.45 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.34 | -11.66 | 22 | 0.0 | -10.97 | -1.29 | -23.19 | 213 |
| 62 | ROC + volume · 1h | momentum | 87.21 | -12.79 | 84 | 14.3 | -10.15 | -1.26 | -23.16 | 418 |
| 63 | RSI(14) reversion | reversion | 86.96 | -13.04 | 182 | 34.1 | -70.63 | -20.16 | -70.69 | 1428 |
| 64 | Donchian 55/20 | breakout | 79.33 | -20.68 | 195 | 16.4 | -68.70 | -15.60 | -68.75 | 1312 |
| 65 | ROC + volume | momentum | 79.30 | -20.70 | 261 | 19.9 | -73.13 | -17.56 | -73.80 | 1661 |
| 66 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -70.07 | -17.31 | -70.07 | 1367 |
| 67 | Squeeze breakout | breakout | 78.88 | -21.12 | 205 | 13.7 | -62.03 | -19.13 | -62.91 | 1232 |
| 68 | Volume breakout | breakout | 77.68 | -22.32 | 173 | 12.7 | -64.35 | -20.13 | -64.40 | 913 |
| 69 | EMA 20/50 cross | trend | 77.63 | -22.38 | 218 | 17.0 | -79.15 | -16.83 | -79.24 | 1489 |
| 70 | Z-score reversion | reversion | 76.00 | -24.00 | 292 | 29.1 | -84.99 | -26.52 | -85.01 | 2088 |
| 71 | MFI reversion | reversion | 73.78 | -26.22 | 289 | 21.1 | -87.72 | -32.97 | -87.76 | 2114 |
| 72 | Supertrend | trend | 72.49 | -27.51 | 296 | 19.6 | -87.47 | -23.59 | -87.50 | 1953 |
| 73 | AI bee: Bizzy | ai | 71.44 | -28.56 | 495 | 8.3 | — | — | — | — |
| 74 | Keltner breakout | breakout | 70.97 | -29.03 | 287 | 11.8 | -85.72 | -32.88 | -85.75 | 1908 |
| 75 | ADX DI cross | trend | 69.67 | -30.33 | 320 | 9.7 | -89.58 | -40.33 | -89.60 | 2110 |
| 76 | Ichimoku | trend | 69.43 | -30.57 | 263 | 8.0 | -82.54 | -25.96 | -82.65 | 1795 |
| 77 | AI bee: Boozy ⏸ | ai | 67.68 | -32.32 | 198 | 4.0 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 66.83 | -33.17 | 391 | 17.1 | -91.25 | -28.66 | -91.31 | 2698 |
| 79 | MACD zero-line | trend | 66.71 | -33.29 | 376 | 15.2 | -92.03 | -33.31 | -92.04 | 2385 |
| 80 | RSI momentum | momentum | 65.20 | -34.80 | 371 | 14.3 | -91.00 | -28.30 | -91.01 | 2415 |
| 81 | Trend pullback | trend | 64.50 | -35.50 | 382 | 14.4 | -91.82 | -34.15 | -91.82 | 2377 |
| 82 | Stochastic reversion | reversion | 63.77 | -36.23 | 569 | 23.6 | -95.66 | -40.90 | -95.69 | 4057 |
| 83 | Triple EMA stack | trend | 63.69 | -36.31 | 423 | 14.2 | -93.75 | -34.84 | -93.76 | 2671 |
| 84 | Bollinger reversion | reversion | 63.09 | -36.91 | 536 | 17.0 | -95.68 | -39.86 | -95.68 | 3697 |
| 85 | Bollinger breakout | breakout | 62.94 | -37.06 | 409 | 13.7 | -94.23 | -39.18 | -94.26 | 2869 |
| 86 | Consensus | meta | 61.44 | -38.56 | 375 | 8.5 | -94.31 | -28.12 | -94.31 | 2632 |
| 87 | EMA 9/21 cross | trend | 59.26 | -40.74 | 529 | 16.1 | -97.58 | -38.57 | -97.59 | 3590 |
| 88 | Connors RSI(2) | reversion | 59.07 | -40.93 | 501 | 16.2 | -96.64 | -39.30 | -96.64 | 3661 |
| 89 | CCI reversion | reversion | 58.04 | -41.96 | 537 | 15.6 | -98.47 | -45.05 | -98.47 | 4723 |
| 90 | Candlestick reversal | reversion | 57.80 | -42.20 | 635 | 15.0 | -99.30 | -44.18 | -99.30 | 5638 |
| 91 | OBV trend | momentum | 57.55 | -42.45 | 584 | 13.9 | -96.41 | -43.90 | -96.44 | 3663 |
| 92 | VWAP momentum | momentum | 56.75 | -43.25 | 594 | 8.4 | -98.72 | -34.89 | -98.72 | 5362 |
| 93 | Parabolic SAR ⏸ | trend | 54.05 | -45.95 | 551 | 12.9 | -97.41 | -47.64 | -97.41 | 3709 |
| 94 | Williams %R | reversion | 52.94 | -47.06 | 670 | 20.0 | -99.50 | -50.03 | -99.51 | 6145 |
| 95 | MACD cross ⏸ | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -53.99 | -99.73 | 6198 |
| 96 | Heikin-Ashi ⏸ | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -63.32 | -99.90 | 8365 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T18:05 | Consensus | buy | BTC-USD | 15.38 | — | entry |
| 2026-10-04T18:05 | Consensus | sell | SOL-USD | 15.29 | -0.11 | target is flat |
| 2026-10-04T18:05 | Stochastic reversion | buy | BTC-USD | 15.95 | — | entry signal |
| 2026-10-04T18:05 | Candlestick reversal | sell | XRP-USD | 14.38 | -0.11 | stop-loss |
| 2026-10-04T18:05 | Donchian 55/20 | sell | ETH-USD | 19.70 | -0.16 | stop-loss |
| 2026-10-04T18:05 | Donchian 20/10 | sell | ETH-USD | 16.57 | -0.13 | stop-loss |
| 2026-10-04T18:05 | Supertrend | sell | SOL-USD | 14.62 | 0.07 | exit signal |
| 2026-10-04T18:00 | Consensus | buy | SOL-USD | 15.40 | — | entry |
| 2026-10-04T18:00 | Heikin-Ashi · 1h | sell | SOL-USD | 18.11 | 0.05 | exit signal |
| 2026-10-04T18:00 | Williams %R | buy | SOL-USD | 13.25 | — | entry signal |
| 2026-10-04T18:00 | Stochastic reversion | buy | SOL-USD | 15.97 | — | entry signal |
| 2026-10-04T18:00 | Connors RSI(2) | buy | SOL-USD | 14.78 | — | entry signal |
| 2026-10-04T18:00 | Candlestick reversal | buy | SOL-USD | 14.48 | — | entry signal |
| 2026-10-04T18:00 | EMA 20/50 cross | sell | XRP-USD | 19.28 | 0.04 | exit signal |
| 2026-10-04T17:55 | Consensus | sell | BTC-USD | 15.32 | -0.09 | target is flat |
| 2026-10-04T17:55 | Squeeze breakout | sell | ETH-USD | 19.57 | -0.13 | exit signal |
| 2026-10-04T17:55 | Bollinger breakout | sell | ETH-USD | 15.65 | -0.10 | exit signal |
| 2026-10-04T17:55 | Bollinger breakout | sell | BTC-USD | 15.64 | -0.11 | exit signal |
| 2026-10-04T17:55 | OBV trend | sell | BTC-USD | 14.30 | -0.08 | exit signal |
| 2026-10-04T17:55 | RSI momentum | sell | SOL-USD | 16.19 | -0.14 | exit signal |
| 2026-10-04T17:55 | Trend pullback | sell | XRP-USD | 16.05 | -0.11 | exit signal |
| 2026-10-04T17:54 | AI bee: Bizzy | sell | DOGE-USD | 11.26 | -0.03 | Jev: sell (sell p=0.54) after 12 min |
| 2026-10-04T17:50 | Consensus | sell | SOL-USD | 15.33 | -0.09 | target is flat |
| 2026-10-04T17:50 | Triple EMA stack | sell | SOL-USD | 15.88 | -0.12 | exit signal |
| 2026-10-04T17:50 | EMA 9/21 cross | sell | SOL-USD | 14.77 | -0.11 | exit signal |
| 2026-10-04T17:45 | Williams %R | buy | XRP-USD | 13.27 | — | entry signal |
| 2026-10-04T17:45 | Connors RSI(2) | sell | XRP-USD | 14.73 | -0.07 | exit signal |
| 2026-10-04T17:45 | Candlestick reversal | buy | XRP-USD | 14.49 | — | entry signal |
| 2026-10-04T17:45 | Trend pullback | buy | XRP-USD | 16.16 | — | entry signal |
| 2026-10-04T17:45 | EMA 9/21 cross | buy | ETH-USD | 2.98 | — | rebalance up |
| 2026-10-04T17:42 | AI bee: Bizzy | buy | DOGE-USD | 11.29 | — | Jev: buy (buy p=0.63) |
| 2026-10-04T17:40 | Candlestick reversal | sell | XRP-USD | 14.43 | -0.12 | exit signal |
| 2026-10-04T17:40 | Keltner breakout | sell | ETH-USD | 17.63 | -0.14 | exit signal |
| 2026-10-04T17:40 | Trend pullback | sell | SOL-USD | 16.14 | -0.10 | exit signal |
| 2026-10-04T17:40 | Ichimoku | sell | SOL-USD | 17.25 | -0.12 | exit signal |
| 2026-10-04T17:35 | MFI reversion | sell | SOL-USD | 18.39 | -0.11 | exit signal |
| 2026-10-04T17:35 | MACD zero-line | sell | SOL-USD | 16.58 | -0.13 | exit signal |
| 2026-10-04T17:31 | AI bee: Boozy | sell | ETH-USD | 23.12 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-04T17:30 | Stochastic reversion | buy | XRP-USD | 15.98 | — | entry signal |
| 2026-10-04T17:30 | Supertrend | buy | ETH-USD | 3.64 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
