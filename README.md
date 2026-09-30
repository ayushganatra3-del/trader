# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T02:10:05.000127+00:00 · 6352 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.68 (-0.32%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 20.02 | +0.03 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-30 | ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, ADRX 12%, BBD 12%, ENHA 12%, CX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.07 · VIX 16.04 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 1740 decisions in 348 calls, $0.0245 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T02:10 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-09-30T02:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T02:10 | 4 / 1 / 0 | SOL-USD 36%, XRP-USD 27% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| RSI(14) reversion · 1h | SOL-USD | 2.42 | +2.64% | 3 |
| Z-score reversion | MSFT | 2.34 | +2.58% | 5 |
| Williams %R | TQQQ | 2.04 | +2.09% | 14 |
| Candlestick reversal | TQQQ | 2.01 | +4.48% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.02 | 1.02 | 2 | 50.0 | 13.82 | 2.99 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | 0.64 | 0.29 | -9.74 | 24 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.05 | 0.05 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.65 | -7.93 | 7 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Hold BTC | benchmark | 99.87 | -0.13 | 0 | — | 29.83 | 3.73 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.71 | -0.29 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 11 | Agent | meta | 99.68 | -0.32 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 12 | Agent (aggressive) | meta | 99.56 | -0.44 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.48 | -0.52 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.40 | -0.60 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.39 | -0.61 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.13 | -0.87 | 20 | 25.0 | -13.02 | -4.40 | -14.79 | 122 |
| 18 | Daily: Bullish score | daily | 99.05 | -0.95 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.01 | -0.99 | 7 | 57.1 | 2.48 | 0.69 | -7.03 | 124 |
| 20 | Z-score reversion · 1h | reversion | 98.88 | -1.12 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.85 | -1.15 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Williams %R · 1h | reversion | 98.60 | -1.40 | 40 | 45.0 | -17.78 | -3.28 | -19.41 | 488 |
| 24 | Candlestick reversal · 1h | reversion | 98.57 | -1.43 | 23 | 21.7 | -27.51 | -6.77 | -28.27 | 491 |
| 25 | Stochastic reversion · 1h | reversion | 98.53 | -1.47 | 26 | 53.8 | -13.66 | -2.99 | -14.89 | 329 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.67 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.43 | -1.57 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.25 | -1.75 | 35 | 34.3 | 0.47 | 0.24 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.85 | -2.15 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.76 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.78 | -2.22 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | Max aggression: 5-day momentum | meta | 97.69 | -2.31 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 34 | EMA 20/50 cross · 1h | trend | 97.66 | -2.34 | 13 | 7.7 | 16.53 | 1.96 | -14.13 | 126 |
| 35 | Bollinger reversion · 1h | reversion | 97.27 | -2.73 | 22 | 27.3 | -17.91 | -4.95 | -18.53 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.07 | -2.93 | 9 | 11.1 | 15.55 | 2.73 | -5.11 | 92 |
| 38 | Max aggression: 1-day momentum | meta | 96.66 | -3.35 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.61 | -3.39 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.57 | -3.43 | 18 | 5.6 | 1.99 | 0.47 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.49 | -3.51 | 139 | 12.9 | 2.64 | 0.60 | -11.92 | 379 |
| 42 | Trend pullback · 1h | trend | 96.27 | -3.73 | 28 | 10.7 | -28.93 | -7.09 | -29.45 | 147 |
| 43 | MACD cross · 1h | trend | 96.12 | -3.88 | 40 | 10.0 | -18.58 | -3.14 | -21.75 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.90 | -4.10 | 26 | 11.5 | -7.76 | -0.96 | -18.82 | 292 |
| 45 | Donchian 55/20 · 1h | breakout | 95.84 | -4.16 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.85 | -16.91 | 684 |
| 47 | MFI reversion · 1h | reversion | 95.54 | -4.46 | 44 | 13.6 | -9.61 | -1.75 | -17.20 | 128 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -50.24 | -27.70 | -50.38 | 607 |
| 49 | Ichimoku · 1h | trend | 95.17 | -4.83 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.91 | -5.09 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | MACD zero-line · 1h | trend | 94.28 | -5.72 | 20 | 5.0 | -5.35 | -0.56 | -14.64 | 222 |
| 53 | RSI momentum · 1h | momentum | 94.28 | -5.72 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 54 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | ADX DI cross · 1h | trend | 94.02 | -5.98 | 30 | 6.7 | -16.13 | -2.98 | -17.81 | 255 |
| 56 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | -0.03 | 0.23 | -18.68 | 213 |
| 57 | Triple EMA stack · 1h | trend | 93.84 | -6.16 | 30 | 6.7 | -6.76 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.68 | -6.32 | 103 | 12.6 | -34.81 | -5.26 | -35.28 | 1236 |
| 59 | EMA 9/21 cross · 1h | trend | 93.05 | -6.95 | 44 | 11.4 | -4.09 | -0.36 | -16.92 | 309 |
| 60 | Heikin-Ashi · 1h | trend | 92.70 | -7.30 | 45 | 11.1 | -26.43 | -4.01 | -30.59 | 672 |
| 61 | OBV trend · 1h | momentum | 92.48 | -7.52 | 54 | 7.4 | -13.04 | -1.43 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.83 | -9.17 | 119 | 34.5 | -71.43 | -21.58 | -71.49 | 1478 |
| 63 | Squeeze breakout | breakout | 89.48 | -10.52 | 94 | 14.9 | -59.67 | -18.34 | -59.84 | 1193 |
| 64 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.99 | -19.88 | -62.05 | 897 |
| 66 | ROC + volume | momentum | 87.03 | -12.97 | 149 | 18.8 | -72.00 | -17.57 | -72.02 | 1628 |
| 67 | Donchian 55/20 | breakout | 86.95 | -13.05 | 97 | 15.5 | -68.07 | -15.54 | -68.09 | 1304 |
| 68 | EMA 20/50 cross | trend | 86.33 | -13.67 | 125 | 16.0 | -78.72 | -17.44 | -78.74 | 1472 |
| 69 | Ichimoku | trend | 85.31 | -14.69 | 114 | 8.8 | -80.45 | -25.85 | -80.45 | 1744 |
| 70 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.84 | -34.02 | -84.84 | 1898 |
| 71 | Z-score reversion | reversion | 84.82 | -15.19 | 182 | 32.4 | -84.41 | -27.07 | -84.43 | 2096 |
| 72 | VWAP reversion | reversion | 84.59 | -15.41 | 138 | 22.5 | -72.10 | -17.96 | -72.19 | 1409 |
| 73 | AI bee: Bizzy | ai | 82.95 | -17.05 | 285 | 9.5 | — | — | — | — |
| 74 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 75 | MACD zero-line | trend | 81.68 | -18.32 | 204 | 16.2 | -91.76 | -35.08 | -91.78 | 2356 |
| 76 | Supertrend | trend | 81.67 | -18.32 | 182 | 17.6 | -87.44 | -24.50 | -87.48 | 1959 |
| 77 | Donchian 20/10 | breakout | 80.71 | -19.29 | 207 | 17.4 | -90.88 | -29.25 | -90.90 | 2677 |
| 78 | MFI reversion | reversion | 80.69 | -19.31 | 186 | 19.4 | -88.17 | -35.51 | -88.20 | 2157 |
| 79 | Bollinger breakout | breakout | 80.20 | -19.80 | 208 | 16.3 | -93.89 | -41.06 | -93.91 | 2866 |
| 80 | Triple EMA stack | trend | 79.58 | -20.42 | 218 | 15.1 | -93.06 | -35.33 | -93.06 | 2620 |
| 81 | RSI momentum | momentum | 79.41 | -20.59 | 200 | 13.0 | -90.43 | -28.87 | -90.46 | 2381 |
| 82 | Trend pullback | trend | 79.25 | -20.75 | 170 | 17.1 | -90.72 | -33.84 | -90.72 | 2268 |
| 83 | ADX DI cross | trend | 78.92 | -21.08 | 199 | 8.0 | -89.51 | -44.89 | -89.52 | 2119 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.38 | -40.37 | -96.38 | 3619 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.60 | -29.54 | -94.61 | 2646 |
| 86 | EMA 9/21 cross | trend | 75.91 | -24.09 | 284 | 16.9 | -97.42 | -40.57 | -97.43 | 3536 |
| 87 | Stochastic reversion | reversion | 75.72 | -24.28 | 332 | 23.8 | -95.94 | -44.84 | -95.95 | 4058 |
| 88 | Candlestick reversal | reversion | 75.70 | -24.30 | 274 | 12.8 | -99.36 | -48.56 | -99.36 | 5586 |
| 89 | OBV trend | momentum | 74.23 | -25.77 | 278 | 15.1 | -95.90 | -47.17 | -95.90 | 3550 |
| 90 | Bollinger reversion | reversion | 74.20 | -25.80 | 311 | 15.4 | -95.78 | -43.33 | -95.78 | 3684 |
| 91 | Parabolic SAR | trend | 72.41 | -27.59 | 271 | 12.9 | -97.00 | -52.89 | -97.00 | 3632 |
| 92 | CCI reversion | reversion | 72.25 | -27.75 | 248 | 10.9 | -98.47 | -49.66 | -98.47 | 4700 |
| 93 | VWAP momentum | momentum | 72.16 | -27.84 | 380 | 10.0 | -98.45 | -35.15 | -98.46 | 5194 |
| 94 | MACD cross | trend | 71.97 | -28.03 | 272 | 14.0 | -99.71 | -61.44 | -99.72 | 6076 |
| 95 | Williams %R | reversion | 70.59 | -29.41 | 348 | 20.7 | -99.53 | -56.51 | -99.53 | 6110 |
| 96 | Heikin-Ashi | trend | 70.12 | -29.88 | 238 | 3.4 | -99.90 | -75.53 | -99.90 | 8301 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T02:10 | CCI reversion | sell | ETH-USD | 18.03 | -0.10 | exit signal |
| 2026-09-30T02:10 | CCI reversion | sell | BTC-USD | 18.03 | -0.08 | exit signal |
| 2026-09-30T02:10 | OBV trend | buy | DOGE-USD | 18.57 | — | entry signal |
| 2026-09-30T02:10 | Parabolic SAR | buy | BTC-USD | 18.11 | — | entry signal |
| 2026-09-30T02:10 | Triple EMA stack | buy | DOGE-USD | 19.91 | — | entry signal |
| 2026-09-30T02:09 | AI bee: Bizzy | sell | XRP-USD | 11.59 | -0.05 | Jev: sell (buy p=0.29) |
| 2026-09-30T02:09 | AI bee: Bizzy | sell | SOL-USD | 16.33 | -0.08 | Jev: sell (buy p=0.23) |
| 2026-09-30T02:09 | AI bee: Bizzy | sell | DOGE-USD | 10.54 | -0.06 | Jev: sell (buy p=0.11) |
| 2026-09-30T02:07 | AI bee: Bizzy | buy | XRP-USD | 11.64 | — | Jev: buy (buy p=0.56) |
| 2026-09-30T02:07 | AI bee: Bizzy | buy | SOL-USD | 16.42 | — | Jev: buy (buy p=0.79) |
| 2026-09-30T02:07 | AI bee: Bizzy | buy | DOGE-USD | 10.60 | — | Jev: buy (buy p=0.51) |
| 2026-09-30T02:06 | AI bee: Bizzy | sell | XRP-USD | 12.44 | -0.06 | Jev: sell (buy p=0.31) |
| 2026-09-30T02:06 | AI bee: Bizzy | sell | SOL-USD | 13.27 | -0.06 | Jev: sell (buy p=0.36) |
| 2026-09-30T02:05 | AI bee: Bizzy | sell | DOGE-USD | 18.04 | -0.09 | Jev: sell (buy p=0.34) |
| 2026-09-30T02:05 | VWAP reversion | sell | BTC-USD | 21.08 | -0.09 | exit signal |
| 2026-09-30T02:05 | Donchian 55/20 | buy | SOL-USD | 21.74 | — | entry signal |
| 2026-09-30T02:05 | VWAP momentum | buy | ETH-USD | 14.13 | — | entry signal |
| 2026-09-30T02:05 | VWAP momentum | buy | BTC-USD | 14.45 | — | entry signal |
| 2026-09-30T02:05 | VWAP momentum | sell | SOL-USD | 3.62 | -0.01 | rebalance down |
| 2026-09-30T02:05 | EMA 20/50 cross | buy | DOGE-USD | 21.59 | — | entry signal |
| 2026-09-30T02:04 | AI bee: Bizzy | buy | XRP-USD | 12.50 | — | Jev: buy (buy p=0.60) |
| 2026-09-30T02:04 | AI bee: Bizzy | buy | SOL-USD | 13.34 | — | Jev: buy (buy p=0.64) |
| 2026-09-30T02:04 | AI bee: Bizzy | buy | DOGE-USD | 18.13 | — | Jev: buy (buy p=0.87) |
| 2026-09-30T02:03 | AI bee: Bizzy | sell | DOGE-USD | 13.89 | -0.10 | Jev: sell (buy p=0.06) |
| 2026-09-30T02:02 | AI bee: Bizzy | buy | DOGE-USD | 13.98 | — | Jev: buy (buy p=0.67) |
| 2026-09-30T02:02 | AI bee: Bizzy | sell | SOL-USD | 15.17 | -0.08 | Jev: sell (buy p=0.35) |
| 2026-09-30T02:01 | AI bee: Bizzy | buy | SOL-USD | 15.26 | — | Jev: buy (buy p=0.73) |
| 2026-09-30T02:01 | AI bee: Bizzy | sell | XRP-USD | 12.48 | -0.06 | Jev: sell (buy p=0.36) |
| 2026-09-30T02:01 | AI bee: Bizzy | sell | DOGE-USD | 12.07 | -0.05 | Jev: sell (buy p=0.39) |
| 2026-09-30T02:00 | AI bee: Bizzy | buy | XRP-USD | 12.55 | — | Jev: buy (buy p=0.60) |
| 2026-09-30T02:00 | AI bee: Bizzy | buy | DOGE-USD | 12.13 | — | Jev: buy (buy p=0.58) |
| 2026-09-30T02:00 | Agent (ML meta-label) | buy | XRP-USD | 5.08 | — | entry |
| 2026-09-30T02:00 | Agent (ML meta-label) | buy | SOL-USD | 5.08 | — | following RSI(14) reversion · 1h |
| 2026-09-30T02:00 | EMA 20/50 cross · 1h | sell | ETH-USD | 9.61 | -0.19 | exit signal |
| 2026-09-30T02:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 18.61 | — | entry signal |
| 2026-09-30T02:00 | VWAP momentum | sell | ETH-USD | 17.96 | -0.12 | exit signal |
| 2026-09-30T02:00 | Heikin-Ashi | sell | SOL-USD | 17.47 | -0.11 | exit signal |
| 2026-09-30T02:00 | Heikin-Ashi | sell | ETH-USD | 17.48 | -0.11 | exit signal |
| 2026-09-30T01:59 | AI bee: Bizzy | sell | XRP-USD | 16.25 | -0.11 | Jev: sell (buy p=0.02) |
| 2026-09-30T01:59 | AI bee: Bizzy | sell | SOL-USD | 12.71 | -0.09 | Jev: sell (buy p=0.01) |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
