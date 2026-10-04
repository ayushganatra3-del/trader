# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T10:05:05.000143+00:00 · 11117 ticks

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
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, ETRA 12%, BBD 12%, BPRE 12%, GME 12%, NYAX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 7454 decisions in 1492 calls, $0.1041 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T10:05 | 2 / 2 / 1 | DOGE-USD 15%, AMZN 17%, COIN 17%, MSTR 16% |  |
| Breezy | 2026-10-04T10:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T10:05 | 4 / 1 / 0 | MSTR 64% |  |

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
| 3 | Hold BTC | benchmark | 101.92 | 1.92 | 0 | — | 35.97 | 4.36 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -24.17 | -5.55 | -26.68 | 500 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 4.53 | 1.31 | -6.57 | 119 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.82 | -3.95 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.86 | -0.14 | 19 | 57.9 | 5.78 | 1.32 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 5.70 | 0.93 | -16.96 | 116 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.36 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.02 | -0.98 | 45 | 60.0 | -8.07 | -1.66 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.55 | 0.42 | -12.41 | 416 |
| 24 | Trend pullback · 1h | trend | 98.83 | -1.17 | 46 | 19.6 | -22.00 | -5.65 | -25.34 | 160 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.94 | -2.06 | 51 | 21.6 | -3.92 | -1.47 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.47 | 1.69 | -14.40 | 135 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.62 | -2.38 | 58 | 44.8 | -11.63 | -3.91 | -14.21 | 220 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.14 | -3.16 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 0.27 | 0.20 | -11.72 | 364 |
| 37 | Parabolic SAR · 1h | trend | 96.45 | -3.55 | 47 | 17.0 | -6.16 | -0.70 | -19.70 | 305 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.60 | 2.81 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.16 | -1.38 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.92 | -4.08 | 28 | 7.1 | 3.35 | 0.64 | -16.43 | 199 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 43 | MACD cross · 1h | trend | 95.69 | -4.31 | 71 | 15.5 | -11.44 | -1.79 | -17.27 | 473 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.74 | -0.64 | -13.84 | 268 |
| 45 | Squeeze breakout · 1h | breakout | 95.26 | -4.74 | 22 | 18.2 | 19.97 | 2.88 | -8.06 | 115 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.02 | 40 | 2.5 | 1.61 | 0.41 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.26 | -6.74 | 178 | 21.9 | -40.52 | -6.40 | -40.97 | 1287 |
| 50 | Triple EMA stack · 1h | trend | 93.14 | -6.86 | 50 | 8.0 | -8.39 | -0.83 | -23.88 | 244 |
| 51 | Bollinger breakout · 1h | breakout | 93.10 | -6.90 | 38 | 15.8 | 6.25 | 0.99 | -12.06 | 297 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.04 | 0.61 | -12.60 | 127 |
| 54 | EMA 9/21 cross · 1h | trend | 91.78 | -8.22 | 69 | 11.6 | -4.24 | -0.39 | -18.47 | 342 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | Three white soldiers | momentum | 91.14 | -8.86 | 75 | 14.7 | -49.48 | -26.29 | -49.74 | 592 |
| 57 | MACD zero-line · 1h | trend | 90.92 | -9.08 | 38 | 13.2 | -3.26 | -0.22 | -18.32 | 235 |
| 58 | Donchian 20/10 · 1h | breakout | 90.73 | -9.27 | 31 | 12.9 | -0.08 | 0.20 | -16.18 | 224 |
| 59 | Heikin-Ashi · 1h | trend | 90.54 | -9.46 | 91 | 24.2 | -32.48 | -5.74 | -33.86 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.34 | -1.35 | -26.45 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.02 | -1.30 | -23.19 | 212 |
| 62 | ROC + volume · 1h | momentum | 87.14 | -12.86 | 84 | 14.3 | -10.41 | -1.30 | -23.16 | 417 |
| 63 | RSI(14) reversion | reversion | 86.96 | -13.04 | 182 | 34.1 | -70.98 | -20.47 | -70.98 | 1436 |
| 64 | Donchian 55/20 | breakout | 79.77 | -20.23 | 189 | 16.9 | -69.01 | -15.69 | -69.05 | 1314 |
| 65 | Squeeze breakout | breakout | 79.46 | -20.54 | 199 | 14.1 | -61.70 | -19.04 | -62.57 | 1228 |
| 66 | ROC + volume | momentum | 79.45 | -20.55 | 260 | 20.0 | -73.36 | -17.66 | -73.97 | 1667 |
| 67 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.75 | -17.11 | -69.75 | 1363 |
| 68 | Volume breakout | breakout | 78.02 | -21.98 | 171 | 12.9 | -64.34 | -20.25 | -64.34 | 913 |
| 69 | EMA 20/50 cross | trend | 77.83 | -22.17 | 213 | 16.9 | -79.10 | -16.77 | -79.24 | 1486 |
| 70 | Z-score reversion | reversion | 76.11 | -23.89 | 291 | 29.2 | -85.07 | -26.67 | -85.08 | 2090 |
| 71 | MFI reversion | reversion | 74.08 | -25.91 | 286 | 21.0 | -87.74 | -33.01 | -87.77 | 2112 |
| 72 | Supertrend | trend | 72.68 | -27.32 | 291 | 19.2 | -87.39 | -23.42 | -87.53 | 1952 |
| 73 | AI bee: Bizzy | ai | 72.63 | -27.37 | 477 | 8.6 | — | — | — | — |
| 74 | Keltner breakout | breakout | 72.13 | -27.87 | 275 | 12.4 | -85.64 | -33.19 | -85.65 | 1910 |
| 75 | Ichimoku | trend | 70.85 | -29.15 | 249 | 8.4 | -82.51 | -26.60 | -82.55 | 1795 |
| 76 | ADX DI cross | trend | 69.91 | -30.09 | 318 | 9.7 | -89.58 | -40.34 | -89.62 | 2115 |
| 77 | AI bee: Boozy | ai | 69.12 | -30.88 | 189 | 4.2 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 67.89 | -32.11 | 381 | 17.6 | -91.24 | -28.81 | -91.24 | 2701 |
| 79 | MACD zero-line | trend | 67.61 | -32.39 | 368 | 15.5 | -91.93 | -32.92 | -91.97 | 2384 |
| 80 | Trend pullback | trend | 66.41 | -33.59 | 361 | 15.0 | -91.73 | -33.15 | -91.75 | 2370 |
| 81 | RSI momentum | momentum | 65.98 | -34.02 | 361 | 14.7 | -91.07 | -28.58 | -91.08 | 2416 |
| 82 | Triple EMA stack | trend | 65.43 | -34.57 | 405 | 14.8 | -93.73 | -35.02 | -93.74 | 2671 |
| 83 | Stochastic reversion | reversion | 64.48 | -35.52 | 561 | 23.9 | -95.64 | -40.67 | -95.65 | 4053 |
| 84 | Bollinger breakout | breakout | 64.24 | -35.76 | 395 | 14.2 | -94.20 | -39.77 | -94.20 | 2874 |
| 85 | Consensus | meta | 63.80 | -36.20 | 349 | 8.9 | -94.15 | -27.72 | -94.16 | 2614 |
| 86 | Bollinger reversion | reversion | 63.31 | -36.69 | 533 | 17.1 | -95.68 | -39.88 | -95.68 | 3699 |
| 87 | Connors RSI(2) | reversion | 61.19 | -38.81 | 476 | 17.0 | -96.57 | -38.65 | -96.57 | 3647 |
| 88 | EMA 9/21 cross | trend | 60.76 | -39.24 | 511 | 16.6 | -97.53 | -38.05 | -97.55 | 3586 |
| 89 | Candlestick reversal | reversion | 58.89 | -41.11 | 623 | 15.2 | -99.30 | -43.69 | -99.30 | 5634 |
| 90 | OBV trend | momentum | 58.87 | -41.13 | 566 | 14.1 | -96.40 | -44.49 | -96.42 | 3663 |
| 91 | CCI reversion | reversion | 58.78 | -41.22 | 528 | 15.9 | -98.46 | -44.79 | -98.46 | 4724 |
| 92 | VWAP momentum | momentum | 56.84 | -43.16 | 590 | 8.5 | -98.72 | -34.92 | -98.72 | 5360 |
| 93 | Parabolic SAR | trend | 55.02 | -44.98 | 539 | 13.2 | -97.37 | -49.65 | -97.37 | 3703 |
| 94 | Williams %R | reversion | 54.08 | -45.92 | 653 | 20.5 | -99.50 | -49.83 | -99.50 | 6142 |
| 95 | MACD cross | trend | 53.11 | -46.89 | 618 | 13.1 | -99.72 | -54.07 | -99.72 | 6185 |
| 96 | Heikin-Ashi | trend | 51.80 | -48.20 | 581 | 8.6 | -99.90 | -64.43 | -99.90 | 8367 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T10:05 | MACD cross | sell | ETH-USD | 10.52 | -0.07 | exit signal |
| 2026-10-04T10:03 | AI bee: Bizzy | buy | DOGE-USD | 10.88 | — | Jev: buy (buy p=0.60) |
| 2026-10-04T10:00 | Ichimoku | sell | ETH-USD | 17.69 | -0.11 | exit signal |
| 2026-10-04T10:00 | Parabolic SAR | buy | ETH-USD | 2.74 | — | rebalance up |
| 2026-10-04T10:00 | Parabolic SAR | sell | DOGE-USD | 2.74 | -0.02 | rebalance down |
| 2026-10-04T09:59 | AI bee: Bizzy | sell | SOL-USD | 10.55 | -0.06 | Jev: sell (sell p=0.51) after 12 min |
| 2026-10-04T09:57 | AI bee: Boozy | sell | BTC-USD | 24.56 | -0.16 | Jev: buy |
| 2026-10-04T09:55 | Keltner breakout | buy | SOL-USD | 18.03 | — | entry signal |
| 2026-10-04T09:55 | Heikin-Ashi | sell | BTC-USD | 12.89 | -0.08 | exit signal |
| 2026-10-04T09:55 | Ichimoku | buy | SOL-USD | 17.73 | — | entry signal |
| 2026-10-04T09:55 | Ichimoku | buy | DOGE-USD | 17.74 | — | entry signal |
| 2026-10-04T09:52 | Parabolic SAR | buy | ETH-USD | 2.75 | — | rebalance up |
| 2026-10-04T09:52 | Parabolic SAR | sell | XRP-USD | 2.75 | -0.02 | rebalance down |
| 2026-10-04T09:50 | Bollinger breakout | buy | ETH-USD | 16.07 | — | entry signal |
| 2026-10-04T09:50 | Heikin-Ashi | buy | SOL-USD | 12.98 | — | entry signal |
| 2026-10-04T09:50 | Heikin-Ashi | buy | BTC-USD | 12.98 | — | entry signal |
| 2026-10-04T09:50 | Parabolic SAR | buy | ETH-USD | 5.51 | — | entry signal |
| 2026-10-04T09:50 | Parabolic SAR | sell | SOL-USD | 2.75 | -0.01 | rebalance down |
| 2026-10-04T09:50 | Parabolic SAR | sell | BTC-USD | 2.75 | -0.01 | rebalance down |
| 2026-10-04T09:47 | AI bee: Bizzy | buy | SOL-USD | 10.61 | — | Jev: buy (buy p=0.58) |
| 2026-10-04T09:45 | Squeeze breakout | buy | SOL-USD | 19.87 | — | entry signal |
| 2026-10-04T09:45 | MACD cross | buy | ETH-USD | 10.59 | — | entry signal |
| 2026-10-04T09:45 | MACD cross | sell | DOGE-USD | 2.66 | -0.02 | rebalance down |
| 2026-10-04T09:42 | AI bee: Boozy | buy | BTC-USD | 24.71 | — | Jev: buy (buy p=0.71) |
| 2026-10-04T09:42 | AI bee: Boozy | sell | SOL-USD | 24.71 | -0.15 | Jev: sell |
| 2026-10-04T09:40 | Heikin-Ashi | sell | XRP-USD | 10.40 | -0.04 | exit signal |
| 2026-10-04T09:40 | Heikin-Ashi | sell | SOL-USD | 12.97 | -0.08 | exit signal |
| 2026-10-04T09:40 | Heikin-Ashi | sell | ETH-USD | 12.98 | -0.08 | exit signal |
| 2026-10-04T09:40 | Heikin-Ashi | sell | BTC-USD | 10.40 | -0.05 | exit signal |
| 2026-10-04T09:40 | MACD cross | sell | ETH-USD | 7.93 | -0.05 | exit signal |
| 2026-10-04T09:38 | AI bee: Bizzy | sell | XRP-USD | 10.27 | -0.07 | Jev: sell (sell p=0.74) after 11 min |
| 2026-10-04T09:35 | Heikin-Ashi | buy | SOL-USD | 5.20 | — | rebalance up |
| 2026-10-04T09:35 | Heikin-Ashi | buy | ETH-USD | 2.62 | — | rebalance up |
| 2026-10-04T09:35 | Heikin-Ashi | sell | DOGE-USD | 12.98 | -0.09 | exit signal |
| 2026-10-04T09:35 | Ichimoku | sell | DOGE-USD | 17.65 | -0.13 | exit signal |
| 2026-10-04T09:32 | Heikin-Ashi | buy | SOL-USD | 2.61 | — | rebalance up |
| 2026-10-04T09:32 | Heikin-Ashi | sell | BTC-USD | 2.61 | -0.01 | rebalance down |
| 2026-10-04T09:32 | MACD cross | buy | ETH-USD | 2.66 | — | rebalance up |
| 2026-10-04T09:32 | MACD cross | sell | SOL-USD | 2.66 | -0.02 | rebalance down |
| 2026-10-04T09:31 | Consensus | buy | XRP-USD | 15.74 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
