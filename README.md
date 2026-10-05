# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T01:05:05.000178+00:00 · 11887 ticks

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

Today: 930 decisions in 186 calls, $0.0131 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T01:05 | 0 / 4 / 1 | DOGE-USD 17%, AMZN 18%, COIN 17%, MSTR 17% |  |
| Breezy | 2026-10-05T01:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T01:05 | 1 / 3 / 1 | DOGE-USD 34% |  |

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
| 1 | Hold BTC | benchmark | 103.46 | 3.46 | 0 | — | 35.38 | 4.25 | -8.68 | 1 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.16 | 2.17 | 0 | — | -7.04 | -1.26 | -15.27 | 2 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.04 | 2.04 | 0 | — | 2.82 | 0.85 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.02 | 1.02 | 25 | 36.0 | -9.08 | -2.93 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.93 | 0.93 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.85 | 0.85 | 0 | — | -1.93 | -1.07 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.85 | 0.85 | 53 | 37.7 | -23.42 | -5.32 | -25.76 | 492 |
| 8 | RSI(14) reversion · 1h | reversion | 100.61 | 0.61 | 11 | 63.6 | 4.95 | 1.41 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.08 | 0.08 | 0 | — | 1.92 | 1.13 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.89 | -0.11 | 41 | 43.9 | -14.65 | -3.87 | -17.38 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.80 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.76 | -0.24 | 20 | 55.0 | 6.17 | 1.40 | -8.60 | 158 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.68 | -0.32 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.64 | -0.36 | 17 | 0.0 | 6.32 | 1.00 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.59 | -0.41 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.45 | -0.56 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.30 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.30 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.01 | -0.99 | 45 | 60.0 | -8.07 | -1.65 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.87 | -1.13 | 63 | 49.2 | 2.18 | 0.52 | -12.41 | 410 |
| 24 | Trend pullback · 1h | trend | 98.79 | -1.21 | 49 | 22.4 | -21.73 | -5.52 | -25.34 | 158 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.71 | -1.29 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.42 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -4.27 | -1.61 | -9.74 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.77 | -2.23 | 25 | 8.0 | 13.88 | 1.72 | -14.40 | 137 |
| 31 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 32 | Daily: SMA 20/50 cross · AAPL | daily | 97.75 | -2.25 | 0 | — | 0.26 | 0.18 | -5.18 | 1 |
| 33 | Connors RSI(2) · 1h | reversion | 97.48 | -2.52 | 60 | 43.3 | -11.84 | -3.96 | -14.21 | 220 |
| 34 | Williams %R · 1h | reversion | 97.45 | -2.55 | 70 | 54.3 | -16.93 | -3.09 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.98 | -3.02 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.69 | -3.31 | 207 | 17.4 | 0.30 | 0.20 | -12.05 | 354 |
| 37 | Parabolic SAR · 1h | trend | 96.54 | -3.46 | 49 | 16.3 | -5.40 | -0.59 | -19.70 | 305 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.80 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.50 | -1.44 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.10 | -3.90 | 5 | 40.0 | -25.95 | -1.40 | -40.19 | 42 |
| 41 | MACD cross · 1h | trend | 96.02 | -3.98 | 72 | 16.7 | -11.85 | -1.84 | -17.27 | 476 |
| 42 | Supertrend · 1h | trend | 96.01 | -3.99 | 28 | 7.1 | 3.59 | 0.66 | -16.43 | 202 |
| 43 | Copy: Insider buying | copy | 95.81 | -4.19 | 6 | 50.0 | -18.81 | -3.69 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.65 | -4.35 | 41 | 12.2 | -4.65 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.45 | -4.55 | 24 | 16.7 | 20.67 | 2.95 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.13 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.23 | -5.77 | 30 | 16.7 | 7.50 | 1.03 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 93.96 | -6.04 | 40 | 2.5 | 2.05 | 0.47 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.40 | -6.60 | 179 | 22.3 | -38.57 | -6.00 | -39.46 | 1278 |
| 50 | Bollinger breakout · 1h | breakout | 93.33 | -6.67 | 40 | 20.0 | 6.76 | 1.05 | -12.06 | 296 |
| 51 | Triple EMA stack · 1h | trend | 93.12 | -6.88 | 50 | 8.0 | -7.76 | -0.74 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.60 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.47 | -7.53 | 30 | 6.7 | 3.19 | 0.62 | -12.60 | 131 |
| 54 | EMA 9/21 cross · 1h | trend | 91.83 | -8.18 | 69 | 11.6 | -2.86 | -0.19 | -18.47 | 340 |
| 55 | Max aggression: 5-day momentum | meta | 91.27 | -8.73 | 5 | 40.0 | -21.37 | -1.90 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 91.08 | -8.92 | 31 | 12.9 | 0.11 | 0.23 | -16.18 | 224 |
| 57 | MACD zero-line · 1h | trend | 90.97 | -9.03 | 39 | 15.4 | -2.85 | -0.16 | -18.32 | 236 |
| 58 | Heikin-Ashi · 1h | trend | 90.84 | -9.16 | 96 | 25.0 | -31.75 | -5.52 | -33.92 | 686 |
| 59 | Three white soldiers | momentum | 90.73 | -9.27 | 77 | 14.3 | -49.65 | -26.04 | -49.97 | 594 |
| 60 | OBV trend · 1h | momentum | 89.44 | -10.56 | 97 | 11.3 | -12.44 | -1.35 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.32 | -11.68 | 23 | 4.3 | -11.00 | -1.29 | -23.19 | 217 |
| 62 | ROC + volume · 1h | momentum | 87.24 | -12.76 | 87 | 14.9 | -9.86 | -1.21 | -23.16 | 419 |
| 63 | RSI(14) reversion | reversion | 86.92 | -13.08 | 183 | 33.9 | -70.38 | -19.59 | -70.45 | 1420 |
| 64 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.67 | -16.82 | -69.67 | 1362 |
| 65 | Donchian 55/20 | breakout | 78.85 | -21.15 | 202 | 16.8 | -68.66 | -15.34 | -68.96 | 1314 |
| 66 | ROC + volume | momentum | 78.54 | -21.46 | 267 | 19.5 | -73.22 | -17.32 | -73.98 | 1663 |
| 67 | Squeeze breakout | breakout | 78.35 | -21.65 | 211 | 13.7 | -62.04 | -18.66 | -63.10 | 1234 |
| 68 | EMA 20/50 cross | trend | 77.66 | -22.34 | 221 | 17.6 | -78.94 | -16.51 | -79.03 | 1488 |
| 69 | Volume breakout | breakout | 76.73 | -23.27 | 182 | 12.1 | -64.67 | -19.90 | -64.67 | 918 |
| 70 | Z-score reversion | reversion | 75.89 | -24.11 | 294 | 28.9 | -84.78 | -25.52 | -84.81 | 2081 |
| 71 | MFI reversion | reversion | 73.65 | -26.35 | 293 | 20.8 | -87.56 | -31.57 | -87.61 | 2109 |
| 72 | Supertrend | trend | 72.53 | -27.47 | 300 | 19.7 | -87.39 | -23.09 | -87.43 | 1952 |
| 73 | AI bee: Bizzy | ai | 70.16 | -29.84 | 511 | 8.0 | — | — | — | — |
| 74 | Keltner breakout | breakout | 69.93 | -30.07 | 298 | 11.7 | -85.80 | -31.66 | -85.82 | 1913 |
| 75 | ADX DI cross | trend | 69.17 | -30.83 | 323 | 9.6 | -89.65 | -39.16 | -89.66 | 2115 |
| 76 | Ichimoku | trend | 68.65 | -31.35 | 271 | 8.1 | -82.51 | -25.12 | -82.70 | 1795 |
| 77 | AI bee: Boozy | ai | 67.60 | -32.40 | 198 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.22 | -33.78 | 380 | 15.0 | -92.01 | -32.45 | -92.03 | 2384 |
| 79 | Donchian 20/10 | breakout | 66.11 | -33.89 | 400 | 17.2 | -91.24 | -27.86 | -91.28 | 2699 |
| 80 | RSI momentum | momentum | 64.55 | -35.45 | 381 | 14.4 | -90.97 | -27.93 | -90.98 | 2416 |
| 81 | Triple EMA stack | trend | 63.11 | -36.89 | 432 | 14.6 | -93.71 | -34.31 | -93.71 | 2673 |
| 82 | Trend pullback | trend | 63.01 | -36.99 | 399 | 14.3 | -91.79 | -33.18 | -91.79 | 2382 |
| 83 | Stochastic reversion | reversion | 62.97 | -37.03 | 582 | 23.0 | -95.61 | -38.77 | -95.65 | 4051 |
| 84 | Bollinger reversion | reversion | 62.41 | -37.59 | 545 | 16.7 | -95.61 | -37.82 | -95.62 | 3691 |
| 85 | Bollinger breakout | breakout | 62.37 | -37.63 | 415 | 13.7 | -94.21 | -37.35 | -94.24 | 2871 |
| 86 | Consensus | meta | 60.75 | -39.25 | 382 | 8.6 | -94.35 | -27.45 | -94.36 | 2640 |
| 87 | EMA 9/21 cross | trend | 58.67 | -41.33 | 539 | 16.3 | -97.56 | -37.35 | -97.57 | 3591 |
| 88 | Connors RSI(2) | reversion | 58.57 | -41.43 | 509 | 15.9 | -96.64 | -37.41 | -96.64 | 3665 |
| 89 | Candlestick reversal | reversion | 57.34 | -42.66 | 642 | 14.8 | -99.29 | -41.60 | -99.29 | 5628 |
| 90 | CCI reversion | reversion | 57.11 | -42.89 | 547 | 15.4 | -98.45 | -42.36 | -98.45 | 4716 |
| 91 | VWAP momentum | momentum | 56.39 | -43.61 | 603 | 9.1 | -98.70 | -33.48 | -98.71 | 5353 |
| 92 | OBV trend | momentum | 56.19 | -43.81 | 601 | 14.1 | -96.45 | -42.64 | -96.47 | 3670 |
| 93 | Parabolic SAR | trend | 53.92 | -46.08 | 551 | 12.9 | -97.42 | -45.10 | -97.43 | 3718 |
| 94 | MACD cross | trend | 52.21 | -47.79 | 629 | 12.9 | -99.73 | -50.32 | -99.73 | 6205 |
| 95 | Williams %R | reversion | 51.89 | -48.11 | 686 | 19.5 | -99.50 | -46.59 | -99.50 | 6139 |
| 96 | Heikin-Ashi | trend | 51.12 | -48.88 | 589 | 8.5 | -99.90 | -57.10 | -99.90 | 8368 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T01:05 | VWAP momentum | buy | ETH-USD | 2.82 | — | rebalance up |
| 2026-10-05T01:05 | Heikin-Ashi | sell | SOL-USD | 10.21 | -0.07 | exit signal |
| 2026-10-05T01:05 | Heikin-Ashi | sell | ETH-USD | 10.20 | -0.08 | exit signal |
| 2026-10-05T01:05 | Heikin-Ashi | sell | BTC-USD | 10.21 | -0.07 | exit signal |
| 2026-10-05T01:05 | MACD zero-line | buy | DOGE-USD | 16.57 | — | entry signal |
| 2026-10-05T01:00 | Agent (ML meta-label) | sell | DOGE-USD | 4.38 | -0.02 | selected signal exited |
| 2026-10-05T01:00 | Keltner breakout · 1h | buy | DOGE-USD | 5.89 | — | entry signal |
| 2026-10-05T01:00 | CCI reversion | buy | SOL-USD | 2.92 | — | rebalance up |
| 2026-10-05T01:00 | CCI reversion | sell | DOGE-USD | 11.44 | -0.01 | exit signal |
| 2026-10-05T01:00 | CCI reversion | sell | BTC-USD | 11.39 | -0.06 | exit signal |
| 2026-10-05T01:00 | MACD cross | buy | BTC-USD | 13.07 | — | entry signal |
| 2026-10-05T01:00 | Triple EMA stack | buy | DOGE-USD | 15.80 | — | entry signal |
| 2026-10-05T01:00 | EMA 20/50 cross | buy | DOGE-USD | 19.44 | — | entry signal |
| 2026-10-05T01:00 | EMA 9/21 cross | buy | DOGE-USD | 14.69 | — | entry signal |
| 2026-10-05T00:59 | AI bee: Bizzy | sell | XRP-USD | 11.32 | -0.07 | Jev: sell (sell p=0.61) after 10 min |
| 2026-10-05T00:58 | AI bee: Boozy | buy | DOGE-USD | 23.12 | — | Jev: buy (buy p=0.68) |
| 2026-10-05T00:57 | AI bee: Bizzy | buy | DOGE-USD | 11.99 | — | Jev: buy (buy p=0.68) |
| 2026-10-05T00:55 | VWAP momentum | buy | BTC-USD | 2.83 | — | rebalance up |
| 2026-10-05T00:55 | VWAP momentum | sell | SOL-USD | 11.24 | -0.08 | exit signal |
| 2026-10-05T00:55 | MACD cross | buy | XRP-USD | 13.07 | — | entry signal |
| 2026-10-05T00:50 | MFI reversion | buy | SOL-USD | 18.43 | — | entry signal |
| 2026-10-05T00:50 | Williams %R | sell | XRP-USD | 13.00 | -0.03 | exit signal |
| 2026-10-05T00:50 | Stochastic reversion | sell | XRP-USD | 15.74 | -0.04 | exit signal |
| 2026-10-05T00:50 | Three white soldiers | buy | XRP-USD | 22.70 | — | entry signal |
| 2026-10-05T00:50 | OBV trend | buy | XRP-USD | 14.06 | — | entry signal |
| 2026-10-05T00:50 | RSI momentum | buy | XRP-USD | 16.15 | — | entry signal |
| 2026-10-05T00:50 | Heikin-Ashi | buy | XRP-USD | 10.28 | — | entry signal |
| 2026-10-05T00:50 | Heikin-Ashi | buy | SOL-USD | 10.28 | — | entry signal |
| 2026-10-05T00:50 | Heikin-Ashi | buy | ETH-USD | 10.28 | — | entry signal |
| 2026-10-05T00:50 | Heikin-Ashi | buy | DOGE-USD | 10.28 | — | entry signal |
| 2026-10-05T00:50 | Heikin-Ashi | buy | BTC-USD | 10.28 | — | entry signal |
| 2026-10-05T00:50 | ADX DI cross | buy | DOGE-USD | 17.32 | — | entry signal |
| 2026-10-05T00:50 | Supertrend | buy | XRP-USD | 18.16 | — | entry signal |
| 2026-10-05T00:50 | Triple EMA stack | buy | XRP-USD | 15.83 | — | entry signal |
| 2026-10-05T00:50 | Triple EMA stack | buy | ETH-USD | 15.83 | — | entry signal |
| 2026-10-05T00:50 | EMA 9/21 cross | buy | XRP-USD | 14.71 | — | entry signal |
| 2026-10-05T00:50 | EMA 9/21 cross | buy | ETH-USD | 14.71 | — | entry signal |
| 2026-10-05T00:49 | AI bee: Bizzy | buy | XRP-USD | 11.39 | — | Jev: buy (buy p=0.65) |
| 2026-10-05T00:45 | Agent (ML meta-label) | buy | DOGE-USD | 4.40 | — | following Stochastic reversion · 1h |
| 2026-10-05T00:45 | CCI reversion | buy | SOL-USD | 11.42 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
