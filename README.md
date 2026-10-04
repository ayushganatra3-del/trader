# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T20:34:05.000162+00:00 · 11650 ticks

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

Today: 15449 decisions in 3091 calls, $0.2159 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T20:34 | 1 / 4 / 0 | AMZN 17%, COIN 17%, MSTR 17% |  |
| Breezy | 2026-10-04T20:34 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T20:34 | 3 / 2 / 0 | MSTR 66% |  |

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
| 2 | Hold BTC | benchmark | 102.15 | 2.15 | 0 | — | 33.87 | 4.14 | -8.68 | 1 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -24.51 | -5.58 | -26.81 | 498 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 3.70 | 1.08 | -6.57 | 121 |
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
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.92 | 0.48 | -12.41 | 411 |
| 24 | Trend pullback · 1h | trend | 98.83 | -1.17 | 47 | 21.3 | -21.70 | -5.56 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -3.94 | -1.48 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.73 | 1.72 | -14.40 | 136 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.14 | -3.16 | -19.41 | 495 |
| 34 | Connors RSI(2) · 1h | reversion | 97.40 | -2.60 | 59 | 44.1 | -11.83 | -3.99 | -14.21 | 222 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 1.58 | 0.43 | -12.72 | 374 |
| 37 | Parabolic SAR · 1h | trend | 96.37 | -3.63 | 49 | 16.3 | -5.53 | -0.61 | -19.70 | 303 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.82 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.45 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -25.95 | -1.41 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 95.89 | -4.11 | 28 | 7.1 | 3.36 | 0.64 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 43 | MACD cross · 1h | trend | 95.78 | -4.22 | 72 | 16.7 | -12.24 | -1.92 | -17.27 | 476 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.69 | -0.63 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.15 | -4.85 | 23 | 17.4 | 20.26 | 2.92 | -8.06 | 116 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 7.50 | 1.04 | -16.19 | 122 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.76 | 0.43 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.15 | -6.85 | 179 | 22.3 | -39.39 | -6.22 | -39.94 | 1281 |
| 50 | Bollinger breakout · 1h | breakout | 93.13 | -6.87 | 39 | 17.9 | 6.29 | 1.00 | -12.06 | 297 |
| 51 | Triple EMA stack · 1h | trend | 93.13 | -6.87 | 50 | 8.0 | -7.74 | -0.74 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.17 | 0.63 | -12.60 | 128 |
| 54 | EMA 9/21 cross · 1h | trend | 91.76 | -8.24 | 69 | 11.6 | -3.53 | -0.29 | -18.47 | 340 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | Donchian 20/10 · 1h | breakout | 90.84 | -9.16 | 31 | 12.9 | 0.04 | 0.22 | -16.18 | 224 |
| 57 | MACD zero-line · 1h | trend | 90.84 | -9.16 | 39 | 15.4 | -3.19 | -0.21 | -18.32 | 236 |
| 58 | Three white soldiers | momentum | 90.81 | -9.19 | 77 | 14.3 | -49.60 | -26.51 | -49.92 | 593 |
| 59 | Heikin-Ashi · 1h | trend | 90.69 | -9.31 | 95 | 24.2 | -32.38 | -5.71 | -33.92 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.71 | -1.40 | -26.59 | 337 |
| 61 | Keltner breakout · 1h | breakout | 88.34 | -11.66 | 22 | 0.0 | -10.97 | -1.29 | -23.19 | 213 |
| 62 | ROC + volume · 1h | momentum | 87.17 | -12.83 | 86 | 14.0 | -10.18 | -1.26 | -23.16 | 418 |
| 63 | RSI(14) reversion | reversion | 86.90 | -13.10 | 182 | 34.1 | -70.72 | -20.25 | -70.78 | 1430 |
| 64 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.87 | -17.18 | -69.87 | 1364 |
| 65 | ROC + volume | momentum | 79.20 | -20.80 | 262 | 19.8 | -73.13 | -17.58 | -73.77 | 1662 |
| 66 | Donchian 55/20 | breakout | 79.19 | -20.81 | 196 | 16.3 | -68.76 | -15.63 | -68.80 | 1313 |
| 67 | Squeeze breakout | breakout | 78.54 | -21.46 | 208 | 13.9 | -61.94 | -18.89 | -62.98 | 1231 |
| 68 | EMA 20/50 cross | trend | 77.53 | -22.47 | 219 | 17.4 | -79.17 | -16.85 | -79.23 | 1490 |
| 69 | Volume breakout | breakout | 77.44 | -22.56 | 175 | 12.6 | -64.44 | -20.17 | -64.44 | 913 |
| 70 | Z-score reversion | reversion | 75.93 | -24.07 | 293 | 29.0 | -84.78 | -26.07 | -84.80 | 2083 |
| 71 | MFI reversion | reversion | 73.73 | -26.27 | 291 | 21.0 | -87.73 | -33.02 | -87.77 | 2117 |
| 72 | Supertrend | trend | 72.41 | -27.59 | 297 | 19.5 | -87.51 | -23.67 | -87.54 | 1955 |
| 73 | AI bee: Bizzy | ai | 71.04 | -28.95 | 500 | 8.2 | — | — | — | — |
| 74 | Keltner breakout | breakout | 70.63 | -29.37 | 290 | 12.1 | -85.79 | -32.85 | -85.81 | 1910 |
| 75 | ADX DI cross | trend | 69.61 | -30.39 | 321 | 9.7 | -89.68 | -40.74 | -89.70 | 2115 |
| 76 | Ichimoku | trend | 68.94 | -31.06 | 267 | 8.2 | -82.77 | -25.98 | -82.86 | 1802 |
| 77 | AI bee: Boozy ⏸ | ai | 67.68 | -32.32 | 198 | 4.0 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 66.54 | -33.46 | 393 | 17.3 | -91.27 | -28.63 | -91.31 | 2699 |
| 79 | MACD zero-line | trend | 66.51 | -33.49 | 378 | 15.1 | -92.04 | -33.29 | -92.05 | 2386 |
| 80 | RSI momentum | momentum | 65.01 | -34.99 | 373 | 14.2 | -91.02 | -28.36 | -91.03 | 2417 |
| 81 | Trend pullback | trend | 63.85 | -36.15 | 388 | 14.2 | -91.90 | -34.09 | -91.90 | 2385 |
| 82 | Stochastic reversion | reversion | 63.50 | -36.50 | 573 | 23.4 | -95.66 | -40.82 | -95.69 | 4059 |
| 83 | Triple EMA stack | trend | 63.41 | -36.59 | 426 | 14.1 | -93.78 | -34.89 | -93.78 | 2674 |
| 84 | Bollinger reversion | reversion | 62.89 | -37.11 | 538 | 16.9 | -95.65 | -39.54 | -95.65 | 3696 |
| 85 | Bollinger breakout | breakout | 62.58 | -37.42 | 413 | 13.8 | -94.23 | -38.85 | -94.27 | 2870 |
| 86 | Consensus ⏸ | meta | 60.98 | -39.02 | 381 | 8.7 | -94.33 | -28.11 | -94.33 | 2633 |
| 87 | EMA 9/21 cross | trend | 58.92 | -41.08 | 533 | 15.9 | -97.58 | -38.37 | -97.59 | 3591 |
| 88 | Connors RSI(2) ⏸ | reversion | 58.75 | -41.25 | 506 | 16.0 | -96.66 | -39.24 | -96.66 | 3667 |
| 89 | CCI reversion | reversion | 57.76 | -42.23 | 540 | 15.6 | -98.46 | -44.73 | -98.46 | 4721 |
| 90 | Candlestick reversal | reversion | 57.58 | -42.42 | 638 | 14.9 | -99.30 | -43.90 | -99.30 | 5637 |
| 91 | OBV trend | momentum | 56.93 | -43.07 | 590 | 13.9 | -96.45 | -44.04 | -96.47 | 3667 |
| 92 | VWAP momentum | momentum | 56.75 | -43.25 | 595 | 8.6 | -98.69 | -34.26 | -98.70 | 5344 |
| 93 | Parabolic SAR ⏸ | trend | 54.05 | -45.95 | 551 | 12.9 | -97.41 | -47.53 | -97.42 | 3712 |
| 94 | Williams %R | reversion | 52.62 | -47.38 | 675 | 19.9 | -99.50 | -49.62 | -99.50 | 6146 |
| 95 | MACD cross ⏸ | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -53.62 | -99.73 | 6198 |
| 96 | Heikin-Ashi ⏸ | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -62.71 | -99.90 | 8367 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T20:30 | Williams %R | buy | XRP-USD | 13.16 | — | entry signal |
| 2026-10-04T20:30 | Stochastic reversion | buy | XRP-USD | 15.89 | — | entry signal |
| 2026-10-04T20:30 | Candlestick reversal | buy | SOL-USD | 14.41 | — | entry signal |
| 2026-10-04T20:30 | OBV trend | buy | BTC-USD | 14.24 | — | entry signal |
| 2026-10-04T20:25 | Squeeze breakout | sell | XRP-USD | 19.58 | -0.12 | exit signal |
| 2026-10-04T20:25 | Bollinger breakout | sell | XRP-USD | 15.63 | -0.09 | exit signal |
| 2026-10-04T20:25 | OBV trend | buy | DOGE-USD | 14.26 | — | entry signal |
| 2026-10-04T20:20 | CCI reversion | buy | ETH-USD | 14.45 | — | entry signal |
| 2026-10-04T20:20 | Williams %R | buy | ETH-USD | 13.18 | — | entry signal |
| 2026-10-04T20:20 | Bollinger reversion | sell | ETH-USD | 15.67 | -0.08 | exit signal |
| 2026-10-04T20:20 | Trend pullback | buy | ETH-USD | 15.92 | — | entry signal |
| 2026-10-04T20:15 | Williams %R | buy | SOL-USD | 13.18 | — | entry signal |
| 2026-10-04T20:15 | Stochastic reversion | buy | ETH-USD | 15.90 | — | entry signal |
| 2026-10-04T20:15 | Bollinger reversion | buy | SOL-USD | 15.76 | — | entry signal |
| 2026-10-04T20:15 | Bollinger reversion | buy | ETH-USD | 15.76 | — | entry signal |
| 2026-10-04T20:15 | RSI(14) reversion | buy | SOL-USD | 21.74 | — | entry signal |
| 2026-10-04T20:15 | Trend pullback | buy | BTC-USD | 15.99 | — | entry signal |
| 2026-10-04T20:10 | Keltner breakout | sell | XRP-USD | 17.59 | -0.13 | exit signal |
| 2026-10-04T20:10 | OBV trend | sell | XRP-USD | 14.26 | -0.08 | exit signal |
| 2026-10-04T20:10 | Ichimoku | sell | DOGE-USD | 17.15 | -0.12 | exit signal |
| 2026-10-04T20:10 | Supertrend | sell | ETH-USD | 18.07 | -0.12 | exit signal |
| 2026-10-04T20:10 | MACD zero-line | sell | XRP-USD | 16.58 | -0.10 | exit signal |
| 2026-10-04T20:10 | Triple EMA stack | sell | ETH-USD | 15.77 | -0.11 | stop-loss |
| 2026-10-04T20:10 | EMA 9/21 cross | sell | ETH-USD | 14.68 | -0.10 | stop-loss |
| 2026-10-04T20:09 | AI bee: Bizzy | sell | XRP-USD | 11.61 | -0.09 | Jev: sell (sell p=0.83) after 11 min |
| 2026-10-04T20:05 | Stochastic reversion | buy | SOL-USD | 15.91 | — | entry signal |
| 2026-10-04T20:05 | RSI momentum | sell | ETH-USD | 16.22 | -0.11 | exit signal |
| 2026-10-04T20:00 | Connors RSI(2) · 1h | buy | SOL-USD | 23.99 | — | entry signal |
| 2026-10-04T20:00 | Squeeze breakout · 1h | buy | DOGE-USD | 3.14 | — | entry |
| 2026-10-04T20:00 | Squeeze breakout · 1h | buy | BTC-USD | 10.35 | — | rebalance up |
| 2026-10-04T20:00 | Squeeze breakout · 1h | sell | SOL-USD | 13.49 | -0.05 | exit signal |
| 2026-10-04T20:00 | Bollinger breakout · 1h | sell | SOL-USD | 7.17 | 0.01 | exit signal |
| 2026-10-04T20:00 | ROC + volume · 1h | sell | SOL-USD | 7.90 | -0.03 | exit signal |
| 2026-10-04T20:00 | ROC + volume · 1h | sell | ETH-USD | 7.21 | -0.05 | exit signal |
| 2026-10-04T20:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.51 | — | entry |
| 2026-10-04T20:00 | VWAP momentum · 1h | buy | BTC-USD | 8.19 | — | rebalance up |
| 2026-10-04T20:00 | VWAP momentum · 1h | sell | SOL-USD | 15.69 | 0.16 | exit signal |
| 2026-10-04T20:00 | Parabolic SAR · 1h | sell | SOL-USD | 6.38 | -0.05 | exit signal |
| 2026-10-04T20:00 | MACD zero-line · 1h | buy | DOGE-USD | 2.57 | — | entry |
| 2026-10-04T20:00 | MACD zero-line · 1h | buy | BTC-USD | 7.57 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
