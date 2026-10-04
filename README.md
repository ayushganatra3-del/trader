# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T19:05:05.000144+00:00 · 11571 ticks

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

Today: 14264 decisions in 2854 calls, $0.1993 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T19:05 | 5 / 0 / 0 | AMZN 17%, COIN 17%, MSTR 17% |  |
| Breezy | 2026-10-04T19:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T19:05 | 5 / 0 / 0 | MSTR 66% |  |

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
| 2 | Hold BTC | benchmark | 102.06 | 2.06 | 0 | — | 33.34 | 4.08 | -8.68 | 1 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.19 | -5.31 | -25.54 | 491 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 5.03 | 1.44 | -6.57 | 118 |
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
| 24 | Trend pullback · 1h | trend | 98.83 | -1.18 | 47 | 21.3 | -21.71 | -5.57 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -3.94 | -1.48 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.20 | 1.66 | -14.40 | 138 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.51 | -2.49 | 59 | 44.1 | -11.73 | -3.95 | -14.21 | 221 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.14 | -3.16 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 1.41 | 0.40 | -12.86 | 362 |
| 37 | Parabolic SAR · 1h | trend | 96.41 | -3.59 | 48 | 16.7 | -5.48 | -0.60 | -19.70 | 303 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.82 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.45 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -25.95 | -1.41 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 95.92 | -4.08 | 28 | 7.1 | 3.38 | 0.64 | -16.43 | 202 |
| 42 | MACD cross · 1h | trend | 95.84 | -4.16 | 71 | 15.5 | -12.29 | -1.93 | -17.27 | 477 |
| 43 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.62 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.28 | -4.72 | 22 | 18.2 | 20.11 | 2.90 | -8.06 | 117 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.02 | 40 | 2.5 | 1.78 | 0.43 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.30 | -6.70 | 178 | 21.9 | -39.32 | -6.21 | -39.94 | 1281 |
| 50 | Bollinger breakout · 1h | breakout | 93.18 | -6.82 | 38 | 15.8 | 6.33 | 1.00 | -12.06 | 297 |
| 51 | Triple EMA stack · 1h | trend | 93.15 | -6.85 | 50 | 8.0 | -7.83 | -0.76 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.16 | 0.63 | -12.60 | 128 |
| 54 | EMA 9/21 cross · 1h | trend | 91.79 | -8.21 | 69 | 11.6 | -3.49 | -0.28 | -18.47 | 342 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | MACD zero-line · 1h | trend | 90.94 | -9.06 | 38 | 13.2 | -3.13 | -0.20 | -18.32 | 236 |
| 57 | Donchian 20/10 · 1h | breakout | 90.86 | -9.13 | 31 | 12.9 | 0.07 | 0.22 | -16.18 | 224 |
| 58 | Three white soldiers | momentum | 90.81 | -9.19 | 77 | 14.3 | -49.60 | -26.51 | -49.92 | 593 |
| 59 | Heikin-Ashi · 1h | trend | 90.67 | -9.32 | 95 | 24.2 | -32.40 | -5.72 | -33.92 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.65 | -1.39 | -26.45 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.34 | -11.66 | 22 | 0.0 | -10.98 | -1.29 | -23.19 | 213 |
| 62 | ROC + volume · 1h | momentum | 87.25 | -12.75 | 84 | 14.3 | -10.11 | -1.25 | -23.16 | 418 |
| 63 | RSI(14) reversion | reversion | 86.96 | -13.04 | 182 | 34.1 | -70.87 | -20.38 | -70.92 | 1431 |
| 64 | Donchian 55/20 | breakout | 79.31 | -20.69 | 195 | 16.4 | -68.71 | -15.60 | -68.76 | 1312 |
| 65 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -70.06 | -17.30 | -70.06 | 1367 |
| 66 | ROC + volume | momentum | 79.20 | -20.80 | 262 | 19.8 | -73.16 | -17.58 | -73.80 | 1661 |
| 67 | Squeeze breakout | breakout | 78.72 | -21.28 | 206 | 14.1 | -61.93 | -19.01 | -62.91 | 1231 |
| 68 | Volume breakout | breakout | 77.58 | -22.42 | 174 | 12.6 | -64.37 | -20.14 | -64.38 | 912 |
| 69 | EMA 20/50 cross | trend | 77.51 | -22.49 | 219 | 17.4 | -79.19 | -16.86 | -79.24 | 1490 |
| 70 | Z-score reversion | reversion | 75.93 | -24.07 | 293 | 29.0 | -84.78 | -26.07 | -84.80 | 2083 |
| 71 | MFI reversion | reversion | 73.74 | -26.26 | 290 | 21.0 | -87.72 | -33.00 | -87.76 | 2115 |
| 72 | Supertrend | trend | 72.45 | -27.55 | 296 | 19.6 | -87.47 | -23.61 | -87.50 | 1954 |
| 73 | AI bee: Bizzy | ai | 71.30 | -28.70 | 497 | 8.2 | — | — | — | — |
| 74 | Keltner breakout | breakout | 70.88 | -29.12 | 288 | 12.2 | -85.77 | -32.99 | -85.79 | 1909 |
| 75 | ADX DI cross | trend | 69.61 | -30.39 | 321 | 9.7 | -89.57 | -40.26 | -89.58 | 2109 |
| 76 | Ichimoku | trend | 69.33 | -30.67 | 264 | 8.3 | -82.57 | -25.95 | -82.66 | 1795 |
| 77 | AI bee: Boozy ⏸ | ai | 67.68 | -32.32 | 198 | 4.0 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.66 | -33.34 | 376 | 15.2 | -92.02 | -33.23 | -92.03 | 2385 |
| 79 | Donchian 20/10 | breakout | 66.66 | -33.34 | 392 | 17.3 | -91.28 | -28.69 | -91.32 | 2699 |
| 80 | RSI momentum | momentum | 65.10 | -34.90 | 372 | 14.2 | -90.99 | -28.34 | -91.00 | 2415 |
| 81 | Trend pullback | trend | 64.11 | -35.89 | 385 | 14.3 | -91.87 | -34.12 | -91.87 | 2382 |
| 82 | Stochastic reversion | reversion | 63.64 | -36.36 | 573 | 23.4 | -95.67 | -40.99 | -95.70 | 4058 |
| 83 | Triple EMA stack | trend | 63.50 | -36.50 | 425 | 14.1 | -93.77 | -34.87 | -93.77 | 2673 |
| 84 | Bollinger reversion | reversion | 63.02 | -36.98 | 537 | 16.9 | -95.68 | -39.88 | -95.68 | 3697 |
| 85 | Bollinger breakout | breakout | 62.83 | -37.17 | 410 | 13.9 | -94.22 | -39.02 | -94.26 | 2869 |
| 86 | Consensus ⏸ | meta | 60.98 | -39.02 | 381 | 8.7 | -94.36 | -28.20 | -94.36 | 2639 |
| 87 | EMA 9/21 cross | trend | 59.11 | -40.89 | 531 | 16.0 | -97.57 | -38.30 | -97.58 | 3589 |
| 88 | Connors RSI(2) ⏸ | reversion | 58.75 | -41.25 | 506 | 16.0 | -96.66 | -39.28 | -96.66 | 3666 |
| 89 | CCI reversion | reversion | 57.96 | -42.04 | 538 | 15.6 | -98.46 | -44.88 | -98.47 | 4722 |
| 90 | Candlestick reversal | reversion | 57.79 | -42.21 | 636 | 14.9 | -99.31 | -44.21 | -99.31 | 5639 |
| 91 | OBV trend | momentum | 57.34 | -42.66 | 586 | 14.0 | -96.43 | -43.97 | -96.44 | 3664 |
| 92 | VWAP momentum | momentum | 56.83 | -43.17 | 594 | 8.4 | -98.71 | -34.69 | -98.71 | 5352 |
| 93 | Parabolic SAR ⏸ | trend | 54.05 | -45.95 | 551 | 12.9 | -97.41 | -47.61 | -97.42 | 3710 |
| 94 | Williams %R | reversion | 52.75 | -47.25 | 674 | 19.9 | -99.50 | -49.81 | -99.50 | 6144 |
| 95 | MACD cross ⏸ | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -53.82 | -99.73 | 6200 |
| 96 | Heikin-Ashi ⏸ | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -63.09 | -99.90 | 8365 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T19:05 | MFI reversion | buy | DOGE-USD | 18.46 | — | entry signal |
| 2026-10-04T19:05 | MFI reversion | sell | ETH-USD | 18.43 | -0.07 | exit signal |
| 2026-10-04T19:05 | Williams %R | buy | DOGE-USD | 13.24 | — | entry signal |
| 2026-10-04T19:05 | Williams %R | sell | XRP-USD | 13.20 | -0.06 | exit signal |
| 2026-10-04T19:05 | Williams %R | sell | SOL-USD | 13.19 | -0.06 | exit signal |
| 2026-10-04T19:05 | Williams %R | sell | ETH-USD | 13.16 | -0.07 | exit signal |
| 2026-10-04T19:05 | Williams %R | sell | BTC-USD | 13.16 | -0.07 | exit signal |
| 2026-10-04T19:05 | Stochastic reversion | sell | XRP-USD | 15.94 | -0.05 | exit signal |
| 2026-10-04T19:05 | Stochastic reversion | sell | SOL-USD | 15.90 | -0.08 | exit signal |
| 2026-10-04T19:05 | Stochastic reversion | sell | ETH-USD | 15.86 | -0.09 | exit signal |
| 2026-10-04T19:05 | Stochastic reversion | sell | BTC-USD | 15.87 | -0.08 | exit signal |
| 2026-10-04T19:05 | Z-score reversion | sell | SOL-USD | 18.93 | -0.07 | exit signal |
| 2026-10-04T19:05 | Candlestick reversal | sell | XRP-USD | 14.41 | -0.04 | exit signal |
| 2026-10-04T19:05 | Squeeze breakout | buy | XRP-USD | 19.70 | — | entry signal |
| 2026-10-04T19:05 | Bollinger breakout | buy | XRP-USD | 15.72 | — | entry signal |
| 2026-10-04T19:05 | Donchian 20/10 | buy | XRP-USD | 16.68 | — | entry signal |
| 2026-10-04T19:05 | OBV trend | buy | XRP-USD | 14.35 | — | entry signal |
| 2026-10-04T19:05 | RSI momentum | buy | XRP-USD | 16.29 | — | entry signal |
| 2026-10-04T19:05 | Trend pullback | buy | XRP-USD | 16.06 | — | entry signal |
| 2026-10-04T19:05 | Trend pullback | buy | ETH-USD | 16.06 | — | entry signal |
| 2026-10-04T19:05 | Trend pullback | buy | DOGE-USD | 16.06 | — | entry signal |
| 2026-10-04T19:05 | Supertrend | buy | XRP-USD | 18.13 | — | entry signal |
| 2026-10-04T19:05 | MACD zero-line | buy | XRP-USD | 16.68 | — | entry signal |
| 2026-10-04T19:05 | Triple EMA stack | buy | XRP-USD | 15.89 | — | entry signal |
| 2026-10-04T19:05 | EMA 20/50 cross | buy | XRP-USD | 19.39 | — | entry signal |
| 2026-10-04T19:02 | Consensus | sell | SOL-USD | 15.23 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-04T19:02 | Consensus | sell | ETH-USD | 15.33 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-04T19:02 | Consensus | sell | DOGE-USD | 12.53 | 0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-04T19:02 | Connors RSI(2) | sell | DOGE-USD | 14.62 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-04T19:00 | Consensus | sell | XRP-USD | 15.22 | -0.09 | target is flat |
| 2026-10-04T19:00 | CCI reversion | sell | XRP-USD | 14.45 | -0.10 | exit signal |
| 2026-10-04T19:00 | Connors RSI(2) | buy | DOGE-USD | 14.71 | — | entry signal |
| 2026-10-04T19:00 | Donchian 20/10 | sell | DOGE-USD | 16.88 | 0.10 | exit signal |
| 2026-10-04T18:55 | AI bee: Bizzy | sell | XRP-USD | 10.03 | -0.06 | Jev: sell (sell p=0.66) after 12 min |
| 2026-10-04T18:55 | Consensus | buy | XRP-USD | 15.30 | — | entry |
| 2026-10-04T18:55 | EMA 9/21 cross | buy | XRP-USD | 14.77 | — | entry signal |
| 2026-10-04T18:50 | Bollinger reversion | sell | SOL-USD | 15.70 | -0.07 | exit signal |
| 2026-10-04T18:50 | OBV trend | sell | DOGE-USD | 14.63 | 0.15 | exit signal |
| 2026-10-04T18:50 | Trend pullback | sell | ETH-USD | 16.00 | -0.10 | exit signal |
| 2026-10-04T18:50 | Triple EMA stack | buy | BTC-USD | 15.89 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
