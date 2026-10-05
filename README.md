# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T00:05:05.000148+00:00 · 11830 ticks

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

Today: 75 decisions in 15 calls, $0.0011 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T00:05 | 0 / 3 / 2 | AMZN 18%, COIN 17%, MSTR 17% |  |
| Breezy | 2026-10-05T00:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T00:05 | 2 / 1 / 2 | MSTR 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.58 | +4.45% | 4 |
| VWAP reversion | AMZN | 1.94 | +0.87% | 3 |
| Z-score reversion | SQQQ | 1.74 | +3.40% | 6 |
| RSI(14) reversion | SQQQ | 1.71 | +3.09% | 4 |
| VWAP reversion | SQQQ | 1.63 | +1.18% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Hold BTC | benchmark | 103.32 | 3.32 | 0 | — | 35.96 | 4.31 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -21.67 | -4.91 | -24.07 | 484 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 4.95 | 1.41 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.80 | -3.91 | -17.53 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.77 | -0.23 | 20 | 55.0 | 6.18 | 1.40 | -8.60 | 158 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.29 | 0.99 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.02 | -0.98 | 45 | 60.0 | -8.07 | -1.65 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.89 | 0.47 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.19 | 49 | 22.4 | -21.93 | -5.59 | -25.34 | 159 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -4.27 | -1.61 | -9.74 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 14.09 | 1.74 | -14.40 | 136 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.49 | -2.51 | 60 | 43.3 | -11.84 | -3.96 | -14.21 | 220 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.17 | -3.14 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 2.41 | 0.58 | -11.42 | 359 |
| 37 | Parabolic SAR · 1h | trend | 96.52 | -3.48 | 49 | 16.3 | -5.42 | -0.59 | -19.70 | 305 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.44 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 96.03 | -3.97 | 28 | 7.1 | 3.54 | 0.66 | -16.43 | 202 |
| 42 | MACD cross · 1h | trend | 95.96 | -4.04 | 72 | 16.7 | -11.44 | -1.78 | -17.27 | 474 |
| 43 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.69 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.63 | -0.61 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.44 | -4.56 | 24 | 16.7 | 20.63 | 2.94 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.02 | 40 | 2.5 | 1.92 | 0.45 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.35 | -6.65 | 179 | 22.3 | -38.65 | -6.02 | -39.45 | 1278 |
| 50 | Bollinger breakout · 1h | breakout | 93.31 | -6.69 | 40 | 20.0 | 6.72 | 1.04 | -12.06 | 296 |
| 51 | Triple EMA stack · 1h | trend | 93.14 | -6.86 | 50 | 8.0 | -8.06 | -0.78 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.10 | 0.61 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 91.84 | -8.16 | 69 | 11.6 | -3.09 | -0.22 | -18.47 | 339 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 91.04 | -8.96 | 31 | 12.9 | 0.06 | 0.22 | -16.18 | 224 |
| 57 | MACD zero-line · 1h | trend | 90.96 | -9.04 | 39 | 15.4 | -2.91 | -0.17 | -18.32 | 236 |
| 58 | Three white soldiers | momentum | 90.81 | -9.19 | 77 | 14.3 | -49.60 | -25.94 | -49.92 | 593 |
| 59 | Heikin-Ashi · 1h | trend | 90.75 | -9.25 | 96 | 25.0 | -31.83 | -5.54 | -33.92 | 686 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.47 | -1.35 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.33 | -11.67 | 23 | 4.3 | -11.00 | -1.29 | -23.19 | 216 |
| 62 | ROC + volume · 1h | momentum | 87.22 | -12.78 | 87 | 14.9 | -10.19 | -1.26 | -23.16 | 420 |
| 63 | RSI(14) reversion | reversion | 86.92 | -13.08 | 183 | 33.9 | -70.48 | -19.68 | -70.55 | 1425 |
| 64 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.63 | -16.79 | -69.63 | 1358 |
| 65 | Donchian 55/20 | breakout | 79.13 | -20.87 | 199 | 16.6 | -68.74 | -15.42 | -68.83 | 1317 |
| 66 | ROC + volume | momentum | 78.54 | -21.46 | 267 | 19.5 | -73.38 | -17.52 | -73.98 | 1667 |
| 67 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.04 | -18.66 | -63.10 | 1234 |
| 68 | EMA 20/50 cross | trend | 77.71 | -22.29 | 220 | 17.3 | -78.90 | -16.48 | -79.01 | 1486 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.76 | -19.93 | -64.76 | 920 |
| 70 | Z-score reversion | reversion | 75.89 | -24.11 | 294 | 28.9 | -84.78 | -25.52 | -84.81 | 2081 |
| 71 | MFI reversion | reversion | 73.72 | -26.28 | 293 | 20.8 | -87.56 | -31.53 | -87.62 | 2110 |
| 72 | Supertrend | trend | 72.76 | -27.25 | 298 | 19.8 | -87.36 | -23.01 | -87.43 | 1951 |
| 73 | AI bee: Bizzy | ai | 70.26 | -29.75 | 510 | 8.0 | — | — | — | — |
| 74 | Keltner breakout | breakout | 70.00 | -30.00 | 297 | 11.8 | -85.90 | -31.84 | -85.92 | 1917 |
| 75 | ADX DI cross | trend | 69.50 | -30.50 | 322 | 9.6 | -89.50 | -38.34 | -89.52 | 2105 |
| 76 | Ichimoku | trend | 68.77 | -31.23 | 269 | 8.2 | -82.59 | -25.22 | -82.71 | 1798 |
| 77 | AI bee: Boozy | ai | 67.68 | -32.32 | 198 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.26 | -33.73 | 380 | 15.0 | -92.01 | -32.41 | -92.02 | 2383 |
| 79 | Donchian 20/10 | breakout | 66.25 | -33.75 | 398 | 17.1 | -91.29 | -27.97 | -91.33 | 2703 |
| 80 | RSI momentum | momentum | 64.87 | -35.13 | 378 | 14.3 | -90.98 | -27.77 | -90.98 | 2417 |
| 81 | Triple EMA stack | trend | 63.55 | -36.45 | 429 | 14.2 | -93.68 | -33.93 | -93.70 | 2671 |
| 82 | Trend pullback | trend | 63.23 | -36.77 | 397 | 14.4 | -91.81 | -33.07 | -91.81 | 2383 |
| 83 | Stochastic reversion | reversion | 63.10 | -36.90 | 578 | 23.2 | -95.60 | -38.61 | -95.63 | 4048 |
| 84 | Bollinger reversion | reversion | 62.69 | -37.31 | 540 | 16.9 | -95.60 | -37.54 | -95.60 | 3687 |
| 85 | Bollinger breakout | breakout | 62.37 | -37.63 | 415 | 13.7 | -94.24 | -37.40 | -94.27 | 2874 |
| 86 | Consensus | meta | 60.79 | -39.21 | 381 | 8.7 | -94.34 | -27.13 | -94.35 | 2637 |
| 87 | EMA 9/21 cross | trend | 59.08 | -40.91 | 536 | 16.0 | -97.55 | -37.00 | -97.57 | 3589 |
| 88 | Connors RSI(2) | reversion | 58.75 | -41.25 | 506 | 16.0 | -96.64 | -37.39 | -96.64 | 3664 |
| 89 | Candlestick reversal | reversion | 57.50 | -42.50 | 640 | 14.8 | -99.29 | -41.48 | -99.29 | 5625 |
| 90 | CCI reversion | reversion | 57.40 | -42.60 | 544 | 15.4 | -98.44 | -42.03 | -98.44 | 4711 |
| 91 | VWAP momentum | momentum | 57.04 | -42.96 | 596 | 8.7 | -98.67 | -33.10 | -98.68 | 5338 |
| 92 | OBV trend | momentum | 56.46 | -43.54 | 599 | 14.0 | -96.45 | -42.30 | -96.47 | 3670 |
| 93 | Parabolic SAR | trend | 54.05 | -45.95 | 551 | 12.9 | -97.43 | -44.93 | -97.43 | 3717 |
| 94 | MACD cross | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -50.19 | -99.73 | 6201 |
| 95 | Williams %R | reversion | 52.16 | -47.84 | 681 | 19.7 | -99.50 | -46.22 | -99.50 | 6137 |
| 96 | Heikin-Ashi | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -56.64 | -99.90 | 8368 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T00:05 | ROC + volume · 1h | sell | DOGE-USD | 6.82 | 0.12 | stop-loss |
| 2026-10-05T00:05 | Williams %R | buy | ETH-USD | 13.06 | — | entry signal |
| 2026-10-05T00:05 | Williams %R | sell | DOGE-USD | 12.97 | -0.11 | target is flat |
| 2026-10-05T00:05 | Squeeze breakout | sell | XRP-USD | 19.63 | -0.00 | stop-loss |
| 2026-10-05T00:05 | Keltner breakout | sell | XRP-USD | 17.43 | -0.12 | stop-loss |
| 2026-10-05T00:05 | Bollinger breakout | sell | XRP-USD | 15.50 | -0.12 | stop-loss |
| 2026-10-05T00:05 | Donchian 20/10 | sell | XRP-USD | 13.25 | -0.01 | exit signal |
| 2026-10-05T00:05 | OBV trend | sell | XRP-USD | 11.34 | 0.02 | exit signal |
| 2026-10-05T00:05 | OBV trend | sell | ETH-USD | 11.34 | -0.03 | exit signal |
| 2026-10-05T00:05 | VWAP momentum | buy | SOL-USD | 3.41 | — | rebalance up |
| 2026-10-05T00:05 | VWAP momentum | sell | XRP-USD | 11.53 | 0.14 | exit signal |
| 2026-10-05T00:03 | AI bee: Bizzy | sell | DOGE-USD | 10.27 | -0.10 | Jev: sell (sell p=0.80) after 11 min |
| 2026-10-05T00:00 | Consensus | buy | XRP-USD | 15.25 | — | entry |
| 2026-10-05T00:00 | Consensus | buy | ETH-USD | 15.25 | — | entry |
| 2026-10-05T00:00 | Consensus | buy | BTC-USD | 15.25 | — | entry |
| 2026-10-05T00:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 23.11 | 0.47 | exit signal |
| 2026-10-05T00:00 | CCI reversion | buy | SOL-USD | 14.36 | — | entry signal |
| 2026-10-05T00:00 | Williams %R | buy | DOGE-USD | 13.08 | — | entry signal |
| 2026-10-05T00:00 | Stochastic reversion | buy | ETH-USD | 15.80 | — | entry signal |
| 2026-10-05T00:00 | Bollinger breakout | buy | XRP-USD | 15.62 | — | entry |
| 2026-10-05T00:00 | Trend pullback | buy | XRP-USD | 15.86 | — | entry signal |
| 2026-10-05T00:00 | Trend pullback | buy | ETH-USD | 15.86 | — | entry |
| 2026-10-05T00:00 | Trend pullback | buy | BTC-USD | 15.86 | — | entry |
| 2026-10-04T23:52 | AI bee: Bizzy | buy | DOGE-USD | 10.37 | — | Jev: buy (buy p=0.59) |
| 2026-10-04T23:50 | Candlestick reversal | buy | DOGE-USD | 14.39 | — | entry signal |
| 2026-10-04T23:45 | Williams %R | buy | SOL-USD | 13.09 | — | entry signal |
| 2026-10-04T23:45 | Stochastic reversion | buy | DOGE-USD | 15.81 | — | entry signal |
| 2026-10-04T23:45 | Bollinger reversion | buy | SOL-USD | 15.70 | — | entry signal |
| 2026-10-04T23:45 | Bollinger reversion | buy | DOGE-USD | 15.70 | — | entry signal |
| 2026-10-04T23:45 | ROC + volume | sell | ETH-USD | 19.58 | -0.13 | exit signal |
| 2026-10-04T23:45 | EMA 9/21 cross | sell | SOL-USD | 14.74 | -0.10 | exit signal |
| 2026-10-04T23:44 | AI bee: Bizzy | sell | XRP-USD | 11.83 | -0.08 | Jev: sell (sell p=0.54) after 11 min |
| 2026-10-04T23:40 | AI bee: Bizzy | sell | BTC-USD | 10.40 | -0.09 | Jev: sell (sell p=0.76) after 12 min |
| 2026-10-04T23:40 | Squeeze breakout · 1h | buy | ETH-USD | 3.13 | — | rebalance up |
| 2026-10-04T23:40 | Squeeze breakout · 1h | sell | DOGE-USD | 3.13 | -0.01 | stop-loss |
| 2026-10-04T23:40 | Keltner breakout · 1h | sell | DOGE-USD | 7.41 | 0.05 | stop-loss |
| 2026-10-04T23:40 | Bollinger breakout · 1h | sell | DOGE-USD | 2.30 | 0.04 | stop-loss |
| 2026-10-04T23:40 | CCI reversion | sell | DOGE-USD | 14.23 | -0.18 | stop-loss |
| 2026-10-04T23:40 | Williams %R | sell | DOGE-USD | 12.95 | -0.18 | stop-loss |
| 2026-10-04T23:40 | Volume breakout | sell | BTC-USD | 19.23 | -0.05 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
