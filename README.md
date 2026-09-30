# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T00:40:05.000147+00:00 · 6268 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.67 (-0.33%)

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
| Copy: Insider buying | 2026-09-29 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.07 · VIX 16.04 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 480 decisions in 96 calls, $0.0068 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T00:40 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-09-30T00:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T00:40 | 1 / 4 / 0 | SOL-USD 22% |  |

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
| 8 | Hold BTC | benchmark | 99.85 | -0.15 | 0 | — | 30.08 | 3.76 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.70 | -0.29 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 11 | Agent | meta | 99.67 | -0.33 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 12 | Agent (aggressive) | meta | 99.55 | -0.45 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.48 | -0.52 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.39 | -0.61 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.38 | -0.61 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.13 | -0.87 | 20 | 25.0 | -13.02 | -4.40 | -14.79 | 122 |
| 18 | Daily: Bullish score | daily | 99.04 | -0.96 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.01 | -0.99 | 7 | 57.1 | 6.80 | 1.73 | -7.03 | 114 |
| 20 | Z-score reversion · 1h | reversion | 98.87 | -1.13 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.85 | -1.15 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Williams %R · 1h | reversion | 98.54 | -1.46 | 40 | 45.0 | -17.93 | -3.31 | -19.41 | 488 |
| 24 | Stochastic reversion · 1h | reversion | 98.52 | -1.48 | 26 | 53.8 | -13.85 | -3.04 | -15.02 | 329 |
| 25 | Candlestick reversal · 1h | reversion | 98.51 | -1.49 | 22 | 22.7 | -25.48 | -6.38 | -26.70 | 481 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.42 | -1.58 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.24 | -1.76 | 35 | 34.3 | 0.42 | 0.24 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.85 | -2.15 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.78 | -2.22 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.68 | -2.31 | 12 | 8.3 | 16.66 | 1.98 | -14.13 | 126 |
| 34 | Max aggression: 5-day momentum | meta | 97.68 | -2.32 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Bollinger reversion · 1h | reversion | 97.26 | -2.74 | 22 | 27.3 | -17.88 | -4.94 | -18.50 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.07 | -2.93 | 9 | 11.1 | 15.55 | 2.73 | -5.11 | 92 |
| 38 | Max aggression: 1-day momentum | meta | 96.65 | -3.35 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.61 | -3.39 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.57 | -3.44 | 18 | 5.6 | 1.99 | 0.47 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.48 | -3.52 | 139 | 12.9 | -0.17 | 0.14 | -13.00 | 380 |
| 42 | Trend pullback · 1h | trend | 96.26 | -3.74 | 28 | 10.7 | -29.04 | -7.12 | -29.77 | 148 |
| 43 | MACD cross · 1h | trend | 96.11 | -3.89 | 40 | 10.0 | -18.65 | -3.16 | -21.69 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.89 | -4.11 | 26 | 11.5 | -7.76 | -0.96 | -18.82 | 292 |
| 45 | Donchian 55/20 · 1h | breakout | 95.83 | -4.17 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 47 | MFI reversion · 1h | reversion | 95.43 | -4.57 | 44 | 13.6 | -9.80 | -1.79 | -17.20 | 128 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -50.24 | -27.70 | -50.38 | 607 |
| 49 | Ichimoku · 1h | trend | 95.17 | -4.83 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.91 | -5.09 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | MACD zero-line · 1h | trend | 94.28 | -5.72 | 20 | 5.0 | -5.35 | -0.56 | -14.64 | 222 |
| 53 | RSI momentum · 1h | momentum | 94.28 | -5.72 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 54 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.33 | 0.27 | -18.68 | 212 |
| 56 | ADX DI cross · 1h | trend | 94.02 | -5.98 | 30 | 6.7 | -16.34 | -3.03 | -18.16 | 256 |
| 57 | Triple EMA stack · 1h | trend | 93.84 | -6.16 | 30 | 6.7 | -7.30 | -0.69 | -22.58 | 228 |
| 58 | VWAP momentum · 1h | momentum | 93.68 | -6.32 | 103 | 12.6 | -34.83 | -5.26 | -35.27 | 1235 |
| 59 | EMA 9/21 cross · 1h | trend | 93.04 | -6.96 | 44 | 11.4 | -3.90 | -0.34 | -16.92 | 307 |
| 60 | Heikin-Ashi · 1h | trend | 92.70 | -7.30 | 45 | 11.1 | -26.45 | -4.01 | -30.63 | 672 |
| 61 | OBV trend · 1h | momentum | 92.47 | -7.53 | 54 | 7.4 | -13.13 | -1.44 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.81 | -9.19 | 119 | 34.5 | -71.18 | -21.33 | -71.24 | 1475 |
| 63 | Squeeze breakout | breakout | 89.51 | -10.49 | 94 | 14.9 | -59.66 | -18.33 | -59.85 | 1191 |
| 64 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.83 | -0.41 | -19.49 | 406 |
| 65 | ROC + volume | momentum | 87.31 | -12.69 | 148 | 18.9 | -71.90 | -17.49 | -71.97 | 1626 |
| 66 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.99 | -19.88 | -62.05 | 897 |
| 67 | Donchian 55/20 | breakout | 87.04 | -12.96 | 97 | 15.5 | -68.07 | -15.54 | -68.08 | 1302 |
| 68 | AI bee: Bizzy | ai | 86.92 | -13.07 | 239 | 11.3 | — | — | — | — |
| 69 | EMA 20/50 cross | trend | 86.50 | -13.50 | 124 | 16.1 | -78.72 | -17.41 | -78.72 | 1470 |
| 70 | Ichimoku | trend | 85.53 | -14.47 | 113 | 8.8 | -80.44 | -25.75 | -80.44 | 1743 |
| 71 | Keltner breakout | breakout | 85.48 | -14.52 | 149 | 13.4 | -84.80 | -33.81 | -84.81 | 1897 |
| 72 | AI bee: Boozy | ai | 85.47 | -14.53 | 85 | 1.2 | — | — | — | — |
| 73 | Z-score reversion | reversion | 84.80 | -15.20 | 180 | 32.8 | -84.42 | -27.09 | -84.43 | 2096 |
| 74 | VWAP reversion | reversion | 84.68 | -15.32 | 137 | 22.6 | -71.54 | -17.46 | -71.94 | 1396 |
| 75 | MACD zero-line | trend | 81.93 | -18.07 | 203 | 16.3 | -91.77 | -34.89 | -91.77 | 2355 |
| 76 | Supertrend | trend | 81.71 | -18.29 | 182 | 17.6 | -87.46 | -24.52 | -87.46 | 1957 |
| 77 | Donchian 20/10 | breakout | 80.96 | -19.04 | 206 | 17.5 | -90.84 | -29.10 | -90.84 | 2674 |
| 78 | MFI reversion | reversion | 80.69 | -19.31 | 185 | 19.5 | -88.10 | -35.28 | -88.10 | 2153 |
| 79 | Bollinger breakout | breakout | 80.45 | -19.55 | 207 | 16.4 | -93.87 | -40.81 | -93.87 | 2863 |
| 80 | Triple EMA stack | trend | 79.69 | -20.31 | 218 | 15.1 | -93.08 | -35.24 | -93.08 | 2619 |
| 81 | RSI momentum | momentum | 79.66 | -20.34 | 199 | 13.1 | -90.40 | -28.74 | -90.41 | 2378 |
| 82 | Trend pullback | trend | 79.25 | -20.75 | 170 | 17.1 | -90.82 | -34.10 | -90.82 | 2274 |
| 83 | ADX DI cross | trend | 79.10 | -20.90 | 198 | 8.1 | -89.43 | -44.57 | -89.43 | 2113 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.39 | -40.64 | -96.39 | 3622 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.46 | -29.29 | -94.48 | 2633 |
| 86 | EMA 9/21 cross | trend | 75.89 | -24.11 | 284 | 16.9 | -97.42 | -40.59 | -97.42 | 3533 |
| 87 | Candlestick reversal | reversion | 75.83 | -24.17 | 271 | 12.5 | -99.36 | -48.62 | -99.36 | 5585 |
| 88 | Stochastic reversion | reversion | 75.71 | -24.29 | 329 | 24.0 | -95.96 | -44.99 | -95.96 | 4061 |
| 89 | OBV trend | momentum | 74.57 | -25.43 | 276 | 15.2 | -95.91 | -46.67 | -95.91 | 3550 |
| 90 | Bollinger reversion | reversion | 74.30 | -25.70 | 308 | 15.6 | -95.79 | -43.39 | -95.79 | 3685 |
| 91 | VWAP momentum | momentum | 72.70 | -27.30 | 374 | 10.2 | -98.45 | -35.02 | -98.45 | 5189 |
| 92 | CCI reversion | reversion | 72.67 | -27.33 | 240 | 11.2 | -98.46 | -49.29 | -98.46 | 4698 |
| 93 | Parabolic SAR | trend | 72.55 | -27.45 | 270 | 13.0 | -97.03 | -52.37 | -97.03 | 3636 |
| 94 | MACD cross | trend | 71.87 | -28.13 | 272 | 14.0 | -99.72 | -61.65 | -99.72 | 6075 |
| 95 | Williams %R | reversion | 70.78 | -29.22 | 343 | 21.0 | -99.53 | -56.34 | -99.53 | 6109 |
| 96 | Heikin-Ashi | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -73.96 | -99.89 | 8297 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T00:40 | AI bee: Boozy | buy | SOL-USD | 18.82 | — | Jev: buy (buy p=0.44) |
| 2026-09-30T00:40 | Candlestick reversal | sell | SOL-USD | 18.96 | -0.09 | exit signal |
| 2026-09-30T00:40 | Candlestick reversal | sell | ETH-USD | 18.92 | -0.13 | exit signal |
| 2026-09-30T00:40 | Candlestick reversal | sell | DOGE-USD | 18.90 | -0.14 | exit signal |
| 2026-09-30T00:40 | VWAP momentum | sell | SOL-USD | 10.91 | -0.10 | exit signal |
| 2026-09-30T00:40 | VWAP momentum | sell | ETH-USD | 14.53 | -0.11 | exit signal |
| 2026-09-30T00:40 | VWAP momentum | sell | DOGE-USD | 14.51 | -0.13 | exit signal |
| 2026-09-30T00:40 | VWAP momentum | sell | BTC-USD | 14.53 | -0.11 | exit signal |
| 2026-09-30T00:39 | AI bee: Boozy | sell | SOL-USD | 19.58 | -0.12 | Jev: sell (buy p=0.25) |
| 2026-09-30T00:38 | AI bee: Boozy | buy | SOL-USD | 19.70 | — | Jev: buy (buy p=0.46) |
| 2026-09-30T00:37 | AI bee: Boozy | sell | XRP-USD | 29.20 | -0.17 | Jev: sell (buy p=0.23) |
| 2026-09-30T00:37 | AI bee: Boozy | sell | SOL-USD | 24.32 | -0.21 | Jev: sell (buy p=0.29) |
| 2026-09-30T00:37 | AI bee: Bizzy | sell | SOL-USD | 14.30 | -0.12 | Jev: sell (buy p=0.03) |
| 2026-09-30T00:37 | AI bee: Bizzy | sell | DOGE-USD | 12.10 | -0.10 | Jev: sell (buy p=0.00) |
| 2026-09-30T00:37 | VWAP momentum | sell | XRP-USD | 3.65 | -0.02 | rebalance down |
| 2026-09-30T00:35 | AI bee: Bizzy | buy | DOGE-USD | 12.20 | — | Jev: buy (buy p=0.56) |
| 2026-09-30T00:35 | AI bee: Bizzy | sell | XRP-USD | 14.76 | -0.08 | Jev: sell (buy p=0.34) |
| 2026-09-30T00:35 | CCI reversion | buy | ETH-USD | 14.57 | — | entry signal |
| 2026-09-30T00:35 | CCI reversion | buy | DOGE-USD | 14.59 | — | entry signal |
| 2026-09-30T00:35 | CCI reversion | buy | BTC-USD | 14.59 | — | entry signal |
| 2026-09-30T00:35 | CCI reversion | sell | XRP-USD | 3.67 | -0.02 | rebalance down |
| 2026-09-30T00:35 | CCI reversion | sell | SOL-USD | 3.70 | -0.02 | rebalance down |
| 2026-09-30T00:35 | Bollinger reversion | buy | ETH-USD | 3.75 | — | rebalance up |
| 2026-09-30T00:35 | Bollinger reversion | buy | DOGE-USD | 3.74 | — | rebalance up |
| 2026-09-30T00:35 | Bollinger reversion | sell | XRP-USD | 14.88 | -0.10 | exit signal |
| 2026-09-30T00:35 | Bollinger reversion | sell | SOL-USD | 11.17 | -0.04 | exit signal |
| 2026-09-30T00:35 | OBV trend | buy | BTC-USD | 18.66 | — | entry signal |
| 2026-09-30T00:35 | VWAP momentum | buy | SOL-USD | 11.01 | — | entry signal |
| 2026-09-30T00:35 | VWAP momentum | buy | ETH-USD | 14.64 | — | entry signal |
| 2026-09-30T00:35 | VWAP momentum | buy | DOGE-USD | 14.64 | — | entry signal |
| 2026-09-30T00:35 | VWAP momentum | buy | BTC-USD | 14.64 | — | entry signal |
| 2026-09-30T00:35 | Parabolic SAR | buy | SOL-USD | 18.16 | — | entry signal |
| 2026-09-30T00:35 | MACD cross | buy | XRP-USD | 17.99 | — | entry signal |
| 2026-09-30T00:34 | AI bee: Boozy | buy | SOL-USD | 24.53 | — | Jev: buy (buy p=0.57) |
| 2026-09-30T00:34 | AI bee: Boozy | sell | DOGE-USD | 30.42 | -0.20 | Jev: sell (buy p=0.42) |
| 2026-09-30T00:34 | AI bee: Bizzy | sell | DOGE-USD | 19.75 | -0.13 | Jev: sell (buy p=0.26) |
| 2026-09-30T00:33 | AI bee: Boozy | buy | DOGE-USD | 30.62 | — | Jev: buy (buy p=0.71) |
| 2026-09-30T00:33 | AI bee: Boozy | sell | ETH-USD | 26.22 | -0.14 | Jev: buy (buy p=0.47) |
| 2026-09-30T00:33 | AI bee: Bizzy | buy | XRP-USD | 14.85 | — | Jev: buy (buy p=0.68) |
| 2026-09-30T00:33 | AI bee: Bizzy | buy | SOL-USD | 14.41 | — | Jev: buy (buy p=0.66) |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
