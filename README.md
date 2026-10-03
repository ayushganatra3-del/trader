# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T04:05:05.000153+00:00 · 9619 ticks

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

Today: 3030 decisions in 606 calls, $0.0424 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T04:05 | 2 / 3 / 0 | AMZN 16%, COIN 16%, MSTR 15% |  |
| Breezy | 2026-10-03T04:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T04:05 | 4 / 1 / 0 | BTC-USD 40% |  |

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
| 3 | Hold BTC | benchmark | 101.25 | 1.25 | 0 | — | 33.15 | 4.07 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.70 | -3.16 | -14.05 | 116 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -22.84 | -5.16 | -26.06 | 496 |
| 8 | RSI(14) reversion · 1h | reversion | 100.65 | 0.65 | 10 | 60.0 | 5.04 | 1.45 | -6.57 | 120 |
| 9 | Bollinger reversion · 1h | reversion | 100.23 | 0.23 | 38 | 44.7 | -14.63 | -3.89 | -17.68 | 307 |
| 10 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.91 | 1.94 | -1.46 | 86 |
| 14 | Z-score reversion · 1h | reversion | 99.77 | -0.23 | 18 | 55.6 | 5.68 | 1.30 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.70 | 1.05 | -16.96 | 115 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.12 | -0.88 | 40 | 60.0 | -8.60 | -1.78 | -9.86 | 334 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.83 | 0.46 | -12.41 | 419 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 45 | 20.0 | -22.54 | -5.78 | -25.84 | 158 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.91 | -2.09 | 50 | 20.0 | -3.16 | -1.18 | -8.90 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 14.05 | 1.75 | -14.40 | 132 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -12.45 | -4.20 | -14.21 | 225 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.58 | -3.03 | -19.41 | 500 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 2.09 | 0.51 | -13.46 | 369 |
| 37 | MFI reversion · 1h | reversion | 96.54 | -3.46 | 69 | 29.0 | -7.02 | -1.16 | -16.99 | 122 |
| 38 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -7.71 | -0.93 | -19.70 | 310 |
| 39 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.84 | 2.87 | -4.73 | 199 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 2.56 | 0.53 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.60 | -3.69 | -21.08 | 71 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -5.91 | -0.84 | -13.84 | 273 |
| 44 | MACD cross · 1h | trend | 95.50 | -4.50 | 71 | 15.5 | -13.96 | -2.24 | -17.27 | 479 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.31 | 0.92 | -16.19 | 127 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.85 | 0.44 | -16.65 | 227 |
| 49 | VWAP momentum · 1h | momentum | 93.29 | -6.71 | 173 | 22.5 | -41.54 | -6.59 | -42.62 | 1291 |
| 50 | Bollinger breakout · 1h | breakout | 93.18 | -6.82 | 36 | 16.7 | 6.03 | 0.97 | -12.06 | 291 |
| 51 | Triple EMA stack · 1h | trend | 93.11 | -6.89 | 50 | 8.0 | -7.58 | -0.72 | -23.88 | 240 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.24 | -4.58 | -18.91 | 695 |
| 53 | Three white soldiers | momentum | 92.52 | -7.48 | 66 | 16.7 | -49.27 | -26.28 | -49.27 | 591 |
| 54 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 2.74 | 0.57 | -12.60 | 128 |
| 55 | EMA 9/21 cross · 1h | trend | 91.74 | -8.26 | 68 | 11.8 | -5.13 | -0.51 | -18.47 | 343 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | Heikin-Ashi · 1h | trend | 91.12 | -8.88 | 86 | 25.6 | -32.97 | -5.85 | -33.58 | 691 |
| 58 | MACD zero-line · 1h | trend | 90.81 | -9.19 | 38 | 13.2 | -4.99 | -0.44 | -18.32 | 238 |
| 59 | Donchian 20/10 · 1h | breakout | 90.65 | -9.35 | 31 | 12.9 | 0.01 | 0.22 | -16.18 | 219 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -13.85 | -1.55 | -26.66 | 338 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.33 | -1.34 | -23.19 | 213 |
| 62 | RSI(14) reversion | reversion | 87.33 | -12.67 | 179 | 34.6 | -72.56 | -21.05 | -72.61 | 1464 |
| 63 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -11.74 | -1.49 | -23.45 | 421 |
| 64 | Squeeze breakout | breakout | 82.76 | -17.24 | 175 | 16.0 | -60.31 | -18.32 | -61.02 | 1206 |
| 65 | Donchian 55/20 | breakout | 81.90 | -18.10 | 174 | 18.4 | -68.35 | -15.41 | -68.37 | 1307 |
| 66 | EMA 20/50 cross | trend | 80.22 | -19.78 | 191 | 18.8 | -78.72 | -16.61 | -78.97 | 1480 |
| 67 | Volume breakout | breakout | 79.88 | -20.12 | 157 | 14.0 | -64.12 | -19.98 | -64.12 | 908 |
| 68 | VWAP reversion | reversion | 79.82 | -20.18 | 209 | 28.7 | -71.67 | -17.58 | -71.88 | 1399 |
| 69 | ROC + volume | momentum | 79.77 | -20.23 | 258 | 20.2 | -73.57 | -17.83 | -73.88 | 1668 |
| 70 | Z-score reversion | reversion | 77.69 | -22.31 | 274 | 31.0 | -85.85 | -26.94 | -85.87 | 2113 |
| 71 | AI bee: Bizzy | ai | 77.64 | -22.36 | 407 | 10.1 | — | — | — | — |
| 72 | MFI reversion | reversion | 76.05 | -23.95 | 268 | 22.4 | -88.30 | -33.51 | -88.30 | 2136 |
| 73 | Keltner breakout | breakout | 75.89 | -24.11 | 247 | 13.8 | -85.32 | -32.23 | -85.32 | 1898 |
| 74 | Ichimoku | trend | 75.32 | -24.68 | 211 | 10.0 | -81.62 | -25.63 | -81.62 | 1767 |
| 75 | Supertrend | trend | 75.19 | -24.81 | 268 | 20.5 | -87.36 | -23.53 | -87.39 | 1953 |
| 76 | AI bee: Boozy | ai | 74.88 | -25.12 | 154 | 5.2 | — | — | — | — |
| 77 | Donchian 20/10 | breakout | 71.90 | -28.10 | 347 | 19.3 | -90.90 | -28.22 | -90.90 | 2683 |
| 78 | MACD zero-line | trend | 71.46 | -28.54 | 334 | 17.1 | -91.76 | -32.68 | -91.77 | 2374 |
| 79 | ADX DI cross | trend | 71.06 | -28.94 | 307 | 10.1 | -89.84 | -41.69 | -89.85 | 2124 |
| 80 | Trend pullback | trend | 70.85 | -29.15 | 318 | 17.0 | -91.52 | -32.51 | -91.52 | 2347 |
| 81 | Triple EMA stack | trend | 70.17 | -29.83 | 358 | 16.5 | -93.23 | -33.98 | -93.23 | 2635 |
| 82 | RSI momentum | momentum | 69.72 | -30.28 | 328 | 15.9 | -90.70 | -27.86 | -90.70 | 2402 |
| 83 | Bollinger breakout | breakout | 69.02 | -30.98 | 351 | 16.0 | -93.94 | -38.26 | -93.94 | 2848 |
| 84 | Stochastic reversion | reversion | 67.36 | -32.64 | 523 | 25.6 | -95.86 | -41.36 | -95.86 | 4070 |
| 85 | Consensus | meta | 66.73 | -33.27 | 322 | 9.6 | -94.70 | -28.98 | -94.70 | 2665 |
| 86 | Connors RSI(2) | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.58 | -38.34 | -96.58 | 3645 |
| 87 | Bollinger reversion | reversion | 65.55 | -34.45 | 507 | 17.9 | -95.93 | -40.46 | -95.93 | 3731 |
| 88 | EMA 9/21 cross | trend | 65.19 | -34.81 | 461 | 18.2 | -97.44 | -37.99 | -97.44 | 3566 |
| 89 | Candlestick reversal | reversion | 63.43 | -36.57 | 569 | 16.7 | -99.36 | -43.90 | -99.36 | 5674 |
| 90 | OBV trend | momentum | 63.34 | -36.66 | 516 | 15.5 | -96.15 | -42.76 | -96.15 | 3625 |
| 91 | CCI reversion | reversion | 62.60 | -37.40 | 479 | 17.5 | -98.52 | -44.51 | -98.52 | 4730 |
| 92 | VWAP momentum | momentum | 61.73 | -38.27 | 532 | 9.4 | -98.66 | -34.40 | -98.66 | 5339 |
| 93 | Parabolic SAR | trend | 60.35 | -39.65 | 483 | 14.7 | -97.16 | -48.29 | -97.16 | 3666 |
| 94 | Williams %R | reversion | 58.76 | -41.24 | 590 | 22.7 | -99.53 | -49.56 | -99.53 | 6153 |
| 95 | MACD cross | trend | 58.50 | -41.50 | 555 | 14.6 | -99.72 | -53.76 | -99.72 | 6175 |
| 96 | Heikin-Ashi | trend | 56.98 | -43.02 | 516 | 9.7 | -99.90 | -62.54 | -99.90 | 8351 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T04:05 | Candlestick reversal | sell | BTC-USD | 15.81 | -0.07 | take-profit |
| 2026-10-03T04:05 | Keltner breakout | buy | BTC-USD | 18.99 | — | entry signal |
| 2026-10-03T04:05 | Heikin-Ashi | buy | XRP-USD | 2.84 | — | rebalance up |
| 2026-10-03T04:05 | Heikin-Ashi | sell | BTC-USD | 2.84 | -0.01 | rebalance down |
| 2026-10-03T04:05 | Ichimoku | buy | BTC-USD | 18.84 | — | entry signal |
| 2026-10-03T04:02 | AI bee: Boozy | buy | BTC-USD | 30.40 | — | Jev: buy (buy p=0.66) |
| 2026-10-03T04:02 | AI bee: Boozy | sell | SOL-USD | 30.40 | -0.15 | Jev: buy |
| 2026-10-03T04:02 | AI bee: Bizzy | sell | XRP-USD | 11.08 | -0.06 | Jev: sell (sell p=0.69) after 10 min |
| 2026-10-03T04:00 | MFI reversion · 1h | buy | SOL-USD | 24.15 | — | entry signal |
| 2026-10-03T04:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.88 | — | entry signal |
| 2026-10-03T04:00 | VWAP momentum · 1h | buy | BTC-USD | 13.34 | — | entry signal |
| 2026-10-03T04:00 | CCI reversion | sell | BTC-USD | 15.59 | -0.07 | exit signal |
| 2026-10-03T04:00 | Williams %R | sell | ETH-USD | 14.68 | -0.06 | exit signal |
| 2026-10-03T04:00 | Candlestick reversal | sell | SOL-USD | 15.87 | -0.03 | take-profit |
| 2026-10-03T04:00 | RSI momentum | buy | BTC-USD | 17.42 | — | entry signal |
| 2026-10-03T04:00 | Ichimoku | buy | SOL-USD | 18.87 | — | entry signal |
| 2026-10-03T04:00 | Ichimoku | buy | ETH-USD | 18.87 | — | entry signal |
| 2026-10-03T04:00 | MACD zero-line | buy | XRP-USD | 17.88 | — | entry signal |
| 2026-10-03T04:00 | Triple EMA stack | buy | XRP-USD | 7.07 | — | entry |
| 2026-10-03T04:00 | Triple EMA stack | sell | SOL-USD | 3.50 | -0.02 | rebalance down |
| 2026-10-03T04:00 | Triple EMA stack | sell | ETH-USD | 3.50 | -0.02 | rebalance down |
| 2026-10-03T03:57 | EMA 9/21 cross | buy | XRP-USD | 3.25 | — | rebalance up |
| 2026-10-03T03:57 | EMA 9/21 cross | sell | SOL-USD | 3.25 | -0.02 | rebalance down |
| 2026-10-03T03:55 | CCI reversion | sell | XRP-USD | 15.67 | -0.05 | exit signal |
| 2026-10-03T03:55 | CCI reversion | sell | DOGE-USD | 15.69 | -0.07 | exit signal |
| 2026-10-03T03:55 | Williams %R | sell | XRP-USD | 14.70 | -0.07 | exit signal |
| 2026-10-03T03:55 | Williams %R | sell | BTC-USD | 14.66 | -0.08 | exit signal |
| 2026-10-03T03:55 | Stochastic reversion | sell | XRP-USD | 16.83 | -0.08 | exit signal |
| 2026-10-03T03:55 | Stochastic reversion | sell | BTC-USD | 16.78 | -0.08 | exit signal |
| 2026-10-03T03:55 | RSI momentum | buy | XRP-USD | 17.45 | — | entry signal |
| 2026-10-03T03:55 | Heikin-Ashi | buy | XRP-USD | 8.57 | — | entry signal |
| 2026-10-03T03:55 | Heikin-Ashi | buy | ETH-USD | 11.41 | — | entry signal |
| 2026-10-03T03:55 | Heikin-Ashi | sell | SOL-USD | 2.86 | -0.01 | rebalance down |
| 2026-10-03T03:55 | Heikin-Ashi | sell | DOGE-USD | 2.86 | -0.01 | rebalance down |
| 2026-10-03T03:55 | EMA 9/21 cross | buy | XRP-USD | 3.21 | — | entry signal |
| 2026-10-03T03:53 | OBV trend | buy | XRP-USD | 3.16 | — | rebalance up |
| 2026-10-03T03:53 | OBV trend | sell | DOGE-USD | 3.16 | -0.02 | rebalance down |
| 2026-10-03T03:53 | VWAP momentum | buy | XRP-USD | 3.08 | — | rebalance up |
| 2026-10-03T03:53 | VWAP momentum | sell | ETH-USD | 3.08 | -0.02 | rebalance down |
| 2026-10-03T03:52 | AI bee: Bizzy | buy | XRP-USD | 11.14 | — | Jev: buy (buy p=0.57) |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
