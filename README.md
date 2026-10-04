# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T17:35:05.000138+00:00 · 11501 ticks

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

Today: 13214 decisions in 2644 calls, $0.1846 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T17:35 | 0 / 4 / 1 | AMZN 17%, COIN 17%, MSTR 16% |  |
| Breezy | 2026-10-04T17:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T17:35 | 0 / 4 / 1 | MSTR 66% |  |

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
| 3 | Hold BTC | benchmark | 102.03 | 2.03 | 0 | — | 33.38 | 4.09 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.65 | -5.41 | -25.99 | 494 |
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
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 47 | 21.3 | -21.71 | -5.57 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -3.94 | -1.48 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.69 | 1.71 | -14.40 | 136 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.51 | -2.49 | 59 | 44.1 | -11.73 | -3.95 | -14.21 | 221 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.14 | -3.16 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 1.75 | 0.46 | -11.17 | 373 |
| 37 | Parabolic SAR · 1h | trend | 96.41 | -3.59 | 48 | 16.7 | -5.48 | -0.60 | -19.70 | 303 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.82 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.45 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -25.95 | -1.41 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 95.92 | -4.08 | 28 | 7.1 | 3.35 | 0.64 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 43 | MACD cross · 1h | trend | 95.81 | -4.19 | 71 | 15.5 | -12.31 | -1.94 | -17.27 | 477 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.61 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.28 | -4.72 | 22 | 18.2 | 20.15 | 2.90 | -8.06 | 117 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.02 | 40 | 2.5 | 1.82 | 0.44 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.30 | -6.70 | 178 | 21.9 | -39.52 | -6.24 | -40.07 | 1282 |
| 50 | Bollinger breakout · 1h | breakout | 93.15 | -6.85 | 38 | 15.8 | 6.38 | 1.01 | -12.06 | 297 |
| 51 | Triple EMA stack · 1h | trend | 93.15 | -6.85 | 50 | 8.0 | -8.11 | -0.79 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.13 | 0.62 | -12.60 | 128 |
| 54 | EMA 9/21 cross · 1h | trend | 91.79 | -8.21 | 69 | 11.6 | -3.76 | -0.32 | -18.47 | 342 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | MACD zero-line · 1h | trend | 90.94 | -9.06 | 38 | 13.2 | -3.18 | -0.20 | -18.32 | 236 |
| 57 | Donchian 20/10 · 1h | breakout | 90.83 | -9.17 | 31 | 12.9 | 0.03 | 0.22 | -16.18 | 224 |
| 58 | Three white soldiers | momentum | 90.81 | -9.19 | 77 | 14.3 | -49.60 | -26.51 | -49.92 | 593 |
| 59 | Heikin-Ashi · 1h | trend | 90.69 | -9.31 | 94 | 23.4 | -32.37 | -5.71 | -33.92 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.64 | -1.39 | -26.45 | 335 |
| 61 | Keltner breakout · 1h | breakout | 88.32 | -11.68 | 22 | 0.0 | -11.00 | -1.30 | -23.19 | 213 |
| 62 | ROC + volume · 1h | momentum | 87.22 | -12.78 | 84 | 14.3 | -10.15 | -1.26 | -23.16 | 418 |
| 63 | RSI(14) reversion | reversion | 86.96 | -13.04 | 182 | 34.1 | -70.80 | -20.32 | -70.86 | 1431 |
| 64 | Donchian 55/20 | breakout | 79.32 | -20.68 | 194 | 16.5 | -68.70 | -15.60 | -68.75 | 1312 |
| 65 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -70.06 | -17.30 | -70.06 | 1367 |
| 66 | ROC + volume | momentum | 79.24 | -20.76 | 261 | 19.9 | -73.14 | -17.57 | -73.78 | 1660 |
| 67 | Squeeze breakout | breakout | 78.88 | -21.12 | 204 | 13.7 | -62.11 | -19.17 | -62.91 | 1233 |
| 68 | EMA 20/50 cross | trend | 77.66 | -22.34 | 217 | 16.6 | -79.14 | -16.81 | -79.24 | 1489 |
| 69 | Volume breakout | breakout | 77.62 | -22.38 | 173 | 12.7 | -64.39 | -20.21 | -64.42 | 912 |
| 70 | Z-score reversion | reversion | 76.00 | -24.00 | 292 | 29.1 | -85.02 | -26.59 | -85.04 | 2089 |
| 71 | MFI reversion | reversion | 73.79 | -26.21 | 289 | 21.1 | -87.71 | -32.96 | -87.75 | 2114 |
| 72 | Supertrend | trend | 72.54 | -27.46 | 295 | 19.3 | -87.46 | -23.57 | -87.50 | 1953 |
| 73 | AI bee: Bizzy | ai | 71.47 | -28.53 | 494 | 8.3 | — | — | — | — |
| 74 | Keltner breakout | breakout | 70.97 | -29.03 | 286 | 11.9 | -85.76 | -33.00 | -85.78 | 1909 |
| 75 | ADX DI cross | trend | 69.67 | -30.33 | 320 | 9.7 | -89.58 | -40.36 | -89.60 | 2110 |
| 76 | Ichimoku | trend | 69.44 | -30.56 | 262 | 8.0 | -82.54 | -25.96 | -82.65 | 1795 |
| 77 | AI bee: Boozy ⏸ | ai | 67.68 | -32.32 | 198 | 4.0 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 66.83 | -33.17 | 390 | 17.2 | -91.27 | -28.72 | -91.32 | 2701 |
| 79 | MACD zero-line | trend | 66.71 | -33.29 | 376 | 15.2 | -92.05 | -33.41 | -92.06 | 2386 |
| 80 | RSI momentum | momentum | 65.24 | -34.76 | 370 | 14.3 | -90.99 | -28.29 | -91.01 | 2415 |
| 81 | Trend pullback | trend | 64.69 | -35.31 | 380 | 14.5 | -91.79 | -34.15 | -91.79 | 2376 |
| 82 | Stochastic reversion | reversion | 63.89 | -36.11 | 569 | 23.6 | -95.65 | -40.82 | -95.69 | 4055 |
| 83 | Triple EMA stack | trend | 63.71 | -36.29 | 422 | 14.2 | -93.75 | -34.84 | -93.76 | 2671 |
| 84 | Bollinger reversion | reversion | 63.09 | -36.91 | 536 | 17.0 | -95.67 | -39.86 | -95.68 | 3697 |
| 85 | Bollinger breakout | breakout | 63.00 | -37.00 | 407 | 13.8 | -94.25 | -39.44 | -94.29 | 2871 |
| 86 | Consensus | meta | 61.66 | -38.34 | 372 | 8.6 | -94.32 | -28.28 | -94.32 | 2633 |
| 87 | EMA 9/21 cross | trend | 59.30 | -40.70 | 528 | 16.1 | -97.58 | -38.60 | -97.59 | 3591 |
| 88 | Connors RSI(2) | reversion | 59.16 | -40.84 | 500 | 16.2 | -96.63 | -39.28 | -96.63 | 3660 |
| 89 | CCI reversion | reversion | 58.04 | -41.96 | 537 | 15.6 | -98.47 | -45.05 | -98.47 | 4723 |
| 90 | Candlestick reversal | reversion | 58.02 | -41.98 | 633 | 15.0 | -99.30 | -44.09 | -99.30 | 5637 |
| 91 | OBV trend | momentum | 57.56 | -42.44 | 583 | 13.9 | -96.41 | -43.92 | -96.43 | 3662 |
| 92 | VWAP momentum | momentum | 56.76 | -43.24 | 594 | 8.4 | -98.72 | -34.91 | -98.72 | 5366 |
| 93 | Parabolic SAR ⏸ | trend | 54.05 | -45.95 | 551 | 12.9 | -97.40 | -47.96 | -97.41 | 3709 |
| 94 | Williams %R | reversion | 53.06 | -46.94 | 670 | 20.0 | -99.50 | -49.94 | -99.50 | 6143 |
| 95 | MACD cross ⏸ | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -54.35 | -99.73 | 6200 |
| 96 | Heikin-Ashi ⏸ | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -63.38 | -99.90 | 8365 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T17:35 | MFI reversion | sell | SOL-USD | 18.39 | -0.11 | exit signal |
| 2026-10-04T17:35 | MACD zero-line | sell | SOL-USD | 16.58 | -0.13 | exit signal |
| 2026-10-04T17:31 | AI bee: Boozy | sell | ETH-USD | 23.12 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-04T17:30 | Stochastic reversion | buy | XRP-USD | 15.98 | — | entry signal |
| 2026-10-04T17:30 | Supertrend | buy | ETH-USD | 3.64 | — | rebalance up |
| 2026-10-04T17:30 | Supertrend | buy | BTC-USD | 4.16 | — | rebalance up |
| 2026-10-04T17:30 | Supertrend | sell | XRP-USD | 14.54 | 0.02 | target is flat |
| 2026-10-04T17:27 | AI bee: Boozy | buy | ETH-USD | 23.27 | — | Jev: buy (buy p=0.67) |
| 2026-10-04T17:20 | Donchian 55/20 | sell | XRP-USD | 19.71 | -0.18 | stop-loss |
| 2026-10-04T17:20 | Ichimoku | buy | SOL-USD | 17.36 | — | entry signal |
| 2026-10-04T17:19 | AI bee: Bizzy | sell | DOGE-USD | 9.92 | -0.05 | Jev: sell (sell p=0.52) after 12 min |
| 2026-10-04T17:15 | Consensus | sell | XRP-USD | 2.94 | -0.03 | target is flat |
| 2026-10-04T17:15 | Connors RSI(2) | buy | XRP-USD | 14.80 | — | entry signal |
| 2026-10-04T17:15 | Keltner breakout | sell | BTC-USD | 17.63 | -0.13 | exit signal |
| 2026-10-04T17:15 | Trend pullback | sell | XRP-USD | 16.09 | -0.12 | exit signal |
| 2026-10-04T17:15 | Ichimoku | sell | BTC-USD | 17.25 | -0.13 | exit signal |
| 2026-10-04T17:15 | Triple EMA stack | buy | SOL-USD | 3.22 | — | rebalance up |
| 2026-10-04T17:15 | Triple EMA stack | buy | ETH-USD | 3.19 | — | rebalance up |
| 2026-10-04T17:15 | Triple EMA stack | buy | BTC-USD | 3.20 | — | rebalance up |
| 2026-10-04T17:15 | Triple EMA stack | sell | XRP-USD | 12.67 | -0.11 | exit signal |
| 2026-10-04T17:15 | EMA 9/21 cross | buy | SOL-USD | 3.01 | — | rebalance up |
| 2026-10-04T17:15 | EMA 9/21 cross | sell | XRP-USD | 8.77 | -0.08 | exit signal |
| 2026-10-04T17:10 | Candlestick reversal | sell | SOL-USD | 14.46 | -0.08 | exit signal |
| 2026-10-04T17:10 | Volume breakout | buy | DOGE-USD | 19.42 | — | entry signal |
| 2026-10-04T17:10 | ROC + volume | buy | DOGE-USD | 19.83 | — | entry signal |
| 2026-10-04T17:10 | Trend pullback | buy | XRP-USD | 3.25 | — | rebalance up |
| 2026-10-04T17:10 | Trend pullback | buy | SOL-USD | 3.27 | — | rebalance up |
| 2026-10-04T17:10 | Trend pullback | buy | ETH-USD | 3.27 | — | rebalance up |
| 2026-10-04T17:10 | Trend pullback | buy | BTC-USD | 3.27 | — | rebalance up |
| 2026-10-04T17:10 | Trend pullback | sell | DOGE-USD | 13.05 | 0.05 | take-profit |
| 2026-10-04T17:07 | AI bee: Bizzy | buy | DOGE-USD | 9.96 | — | Jev: buy (buy p=0.56) |
| 2026-10-04T17:00 | Keltner breakout · 1h | buy | DOGE-USD | 7.36 | — | entry signal |
| 2026-10-04T17:00 | Parabolic SAR · 1h | buy | ETH-USD | 6.43 | — | entry signal |
| 2026-10-04T16:57 | AI bee: Boozy | sell | ETH-USD | 23.27 | -0.14 | Jev: sell |
| 2026-10-04T16:55 | CCI reversion | sell | SOL-USD | 14.48 | -0.07 | exit signal |
| 2026-10-04T16:54 | AI bee: Bizzy | sell | ETH-USD | 10.35 | -0.06 | Jev: sell (sell p=0.50) after 10 min |
| 2026-10-04T16:53 | Triple EMA stack | buy | XRP-USD | 3.18 | — | rebalance up |
| 2026-10-04T16:53 | Triple EMA stack | sell | BTC-USD | 3.18 | -0.01 | rebalance down |
| 2026-10-04T16:52 | Triple EMA stack | buy | XRP-USD | 3.18 | — | rebalance up |
| 2026-10-04T16:52 | Triple EMA stack | sell | ETH-USD | 3.18 | -0.01 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
