# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T01:40:05.000148+00:00 · 6324 ticks

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
| Copy: Insider buying | 2026-09-29 | ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, BBD 12%, ENHA 12%, CX 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.07 · VIX 16.04 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 1320 decisions in 264 calls, $0.0186 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T01:40 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-09-30T01:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T01:40 | 4 / 1 / 0 | SOL-USD 30%, DOGE-USD 28% |  |

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
| 8 | Copy: Warren Buffett (BRK-B) | copy | 99.71 | -0.29 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 9 | Hold BTC | benchmark | 99.68 | -0.32 | 0 | — | 29.33 | 3.68 | -8.68 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 11 | Agent | meta | 99.68 | -0.32 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 12 | Agent (aggressive) | meta | 99.56 | -0.44 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.48 | -0.52 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.40 | -0.60 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.39 | -0.61 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.13 | -0.87 | 20 | 25.0 | -13.02 | -4.40 | -14.79 | 122 |
| 18 | Daily: Bullish score | daily | 99.05 | -0.95 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.01 | -0.99 | 7 | 57.1 | 3.16 | 0.86 | -7.03 | 124 |
| 20 | Z-score reversion · 1h | reversion | 98.88 | -1.12 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.85 | -1.15 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Williams %R · 1h | reversion | 98.55 | -1.45 | 40 | 45.0 | -17.91 | -3.31 | -19.41 | 488 |
| 24 | Candlestick reversal · 1h | reversion | 98.53 | -1.47 | 23 | 21.7 | -27.71 | -6.81 | -28.41 | 492 |
| 25 | Stochastic reversion · 1h | reversion | 98.53 | -1.47 | 26 | 53.8 | -13.89 | -3.04 | -15.08 | 329 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.43 | -1.57 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.25 | -1.75 | 35 | 34.3 | 0.42 | 0.24 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.85 | -2.15 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.78 | -2.22 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | Max aggression: 5-day momentum | meta | 97.69 | -2.31 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 34 | EMA 20/50 cross · 1h | trend | 97.68 | -2.32 | 12 | 8.3 | 16.57 | 1.97 | -14.13 | 126 |
| 35 | Bollinger reversion · 1h | reversion | 97.27 | -2.73 | 22 | 27.3 | -17.85 | -4.93 | -18.46 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.07 | -2.93 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 38 | Max aggression: 1-day momentum | meta | 96.66 | -3.35 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.61 | -3.39 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.54 | -3.46 | 18 | 5.6 | 1.95 | 0.46 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.49 | -3.51 | 139 | 12.9 | 1.78 | 0.47 | -11.86 | 380 |
| 42 | Trend pullback · 1h | trend | 96.27 | -3.73 | 28 | 10.7 | -29.04 | -7.12 | -29.77 | 148 |
| 43 | MACD cross · 1h | trend | 96.12 | -3.88 | 40 | 10.0 | -18.64 | -3.15 | -21.73 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.90 | -4.10 | 26 | 11.5 | -7.76 | -0.96 | -18.82 | 292 |
| 45 | Donchian 55/20 · 1h | breakout | 95.84 | -4.16 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 47 | MFI reversion · 1h | reversion | 95.48 | -4.52 | 44 | 13.6 | -9.72 | -1.77 | -17.20 | 128 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -50.24 | -27.70 | -50.38 | 607 |
| 49 | Ichimoku · 1h | trend | 95.17 | -4.83 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.91 | -5.09 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | MACD zero-line · 1h | trend | 94.28 | -5.72 | 20 | 5.0 | -5.32 | -0.56 | -14.64 | 222 |
| 53 | RSI momentum · 1h | momentum | 94.28 | -5.72 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 54 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | ADX DI cross · 1h | trend | 94.02 | -5.98 | 30 | 6.7 | -15.99 | -2.96 | -17.81 | 254 |
| 56 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | -0.03 | 0.23 | -18.68 | 213 |
| 57 | Triple EMA stack · 1h | trend | 93.84 | -6.16 | 30 | 6.7 | -6.76 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.68 | -6.32 | 103 | 12.6 | -34.83 | -5.26 | -35.28 | 1235 |
| 59 | EMA 9/21 cross · 1h | trend | 93.05 | -6.95 | 44 | 11.4 | -4.08 | -0.36 | -16.92 | 308 |
| 60 | Heikin-Ashi · 1h | trend | 92.70 | -7.30 | 45 | 11.1 | -26.45 | -4.01 | -30.63 | 672 |
| 61 | OBV trend · 1h | momentum | 92.48 | -7.52 | 54 | 7.4 | -13.04 | -1.43 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 119 | 34.5 | -71.16 | -21.31 | -71.21 | 1473 |
| 63 | Squeeze breakout | breakout | 89.27 | -10.73 | 94 | 14.9 | -59.77 | -18.43 | -59.85 | 1193 |
| 64 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.99 | -19.88 | -62.05 | 897 |
| 66 | ROC + volume | momentum | 87.09 | -12.91 | 149 | 18.8 | -71.98 | -17.55 | -71.99 | 1627 |
| 67 | Donchian 55/20 | breakout | 86.90 | -13.10 | 97 | 15.5 | -68.12 | -15.57 | -68.12 | 1303 |
| 68 | EMA 20/50 cross | trend | 86.30 | -13.70 | 125 | 16.0 | -78.79 | -17.47 | -78.80 | 1471 |
| 69 | Ichimoku | trend | 85.31 | -14.69 | 114 | 8.8 | -80.44 | -25.84 | -80.44 | 1743 |
| 70 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.84 | -34.02 | -84.84 | 1898 |
| 71 | AI bee: Bizzy | ai | 84.90 | -15.10 | 262 | 10.3 | — | — | — | — |
| 72 | Z-score reversion | reversion | 84.74 | -15.26 | 182 | 32.4 | -84.43 | -27.11 | -84.43 | 2096 |
| 73 | VWAP reversion | reversion | 84.62 | -15.38 | 137 | 22.6 | -71.95 | -17.85 | -72.05 | 1406 |
| 74 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 75 | MACD zero-line | trend | 81.49 | -18.51 | 204 | 16.2 | -91.80 | -35.22 | -91.80 | 2357 |
| 76 | Supertrend | trend | 81.41 | -18.59 | 182 | 17.6 | -87.48 | -24.59 | -87.48 | 1959 |
| 77 | MFI reversion | reversion | 80.59 | -19.41 | 186 | 19.4 | -88.12 | -35.39 | -88.14 | 2154 |
| 78 | Donchian 20/10 | breakout | 80.51 | -19.49 | 207 | 17.4 | -90.89 | -29.32 | -90.89 | 2677 |
| 79 | Bollinger breakout | breakout | 80.01 | -19.99 | 208 | 16.3 | -93.90 | -41.26 | -93.91 | 2866 |
| 80 | Triple EMA stack | trend | 79.57 | -20.43 | 218 | 15.1 | -93.06 | -35.34 | -93.06 | 2618 |
| 81 | Trend pullback | trend | 79.25 | -20.75 | 170 | 17.1 | -90.74 | -33.90 | -90.74 | 2269 |
| 82 | RSI momentum | momentum | 79.22 | -20.78 | 200 | 13.0 | -90.47 | -28.97 | -90.47 | 2382 |
| 83 | ADX DI cross | trend | 78.85 | -21.15 | 199 | 8.0 | -89.39 | -44.76 | -89.39 | 2111 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.39 | -40.56 | -96.39 | 3620 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.58 | -29.56 | -94.59 | 2645 |
| 86 | Stochastic reversion | reversion | 75.68 | -24.32 | 332 | 23.8 | -95.95 | -45.00 | -95.96 | 4060 |
| 87 | EMA 9/21 cross | trend | 75.67 | -24.33 | 284 | 16.9 | -97.43 | -40.79 | -97.43 | 3537 |
| 88 | Candlestick reversal | reversion | 75.63 | -24.37 | 274 | 12.8 | -99.36 | -48.46 | -99.36 | 5583 |
| 89 | OBV trend | momentum | 74.32 | -25.68 | 278 | 15.1 | -95.90 | -47.05 | -95.90 | 3548 |
| 90 | Bollinger reversion | reversion | 74.20 | -25.80 | 311 | 15.4 | -95.80 | -43.51 | -95.80 | 3685 |
| 91 | Parabolic SAR | trend | 72.47 | -27.53 | 271 | 12.9 | -96.99 | -52.79 | -96.99 | 3630 |
| 92 | CCI reversion | reversion | 72.29 | -27.70 | 246 | 11.0 | -98.47 | -49.76 | -98.47 | 4701 |
| 93 | VWAP momentum | momentum | 72.18 | -27.82 | 379 | 10.0 | -98.44 | -35.02 | -98.44 | 5189 |
| 94 | MACD cross | trend | 71.78 | -28.22 | 272 | 14.0 | -99.72 | -61.81 | -99.72 | 6078 |
| 95 | Williams %R | reversion | 70.60 | -29.40 | 348 | 20.7 | -99.53 | -56.60 | -99.53 | 6110 |
| 96 | Heikin-Ashi | trend | 70.34 | -29.66 | 236 | 3.4 | -99.89 | -74.96 | -99.89 | 8299 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T01:40 | VWAP reversion | buy | BTC-USD | 21.17 | — | entry signal |
| 2026-09-30T01:40 | VWAP momentum | buy | SOL-USD | 18.06 | — | entry signal |
| 2026-09-30T01:37 | AI bee: Bizzy | sell | XRP-USD | 18.17 | -0.10 | Jev: sell (buy p=0.20) |
| 2026-09-30T01:36 | AI bee: Bizzy | buy | XRP-USD | 18.28 | — | Jev: buy (buy p=0.86) |
| 2026-09-30T01:35 | Keltner breakout | sell | DOGE-USD | 21.13 | -0.25 | stop-loss |
| 2026-09-30T01:35 | Bollinger breakout | sell | DOGE-USD | 19.88 | -0.23 | stop-loss |
| 2026-09-30T01:35 | Donchian 20/10 | sell | DOGE-USD | 20.00 | -0.23 | stop-loss |
| 2026-09-30T01:35 | OBV trend | sell | SOL-USD | 18.44 | -0.19 | exit signal |
| 2026-09-30T01:35 | RSI momentum | sell | DOGE-USD | 19.68 | -0.23 | stop-loss |
| 2026-09-30T01:35 | ROC + volume | sell | SOL-USD | 21.60 | -0.23 | exit signal |
| 2026-09-30T01:35 | VWAP momentum | sell | SOL-USD | 14.43 | -0.07 | exit signal |
| 2026-09-30T01:35 | Heikin-Ashi | sell | XRP-USD | 17.55 | -0.13 | exit signal |
| 2026-09-30T01:35 | Heikin-Ashi | sell | SOL-USD | 17.57 | -0.12 | exit signal |
| 2026-09-30T01:35 | Heikin-Ashi | sell | DOGE-USD | 17.55 | -0.14 | exit signal |
| 2026-09-30T01:35 | Ichimoku | sell | SOL-USD | 21.16 | -0.22 | exit signal |
| 2026-09-30T01:35 | ADX DI cross | sell | ETH-USD | 19.61 | -0.17 | stop-loss |
| 2026-09-30T01:35 | MACD zero-line | sell | DOGE-USD | 20.24 | -0.23 | stop-loss |
| 2026-09-30T01:30 | AI bee: Boozy | sell | XRP-USD | 19.80 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-30T01:30 | AI bee: Boozy | sell | SOL-USD | 30.69 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-30T01:30 | VWAP momentum | sell | ETH-USD | 14.27 | -0.11 | exit signal |
| 2026-09-30T01:30 | VWAP momentum | sell | BTC-USD | 14.43 | -0.10 | exit signal |
| 2026-09-30T01:29 | AI bee: Boozy | buy | XRP-USD | 19.94 | — | Jev: buy (buy p=0.48) |
| 2026-09-30T01:29 | AI bee: Boozy | sell | DOGE-USD | 27.31 | -0.16 | Jev: sell (buy p=0.31) |
| 2026-09-30T01:26 | AI bee: Bizzy | sell | XRP-USD | 11.86 | -0.07 | Jev: sell (buy p=0.28) |
| 2026-09-30T01:26 | AI bee: Bizzy | sell | SOL-USD | 16.74 | -0.09 | Jev: sell (buy p=0.23) |
| 2026-09-30T01:25 | Williams %R | sell | ETH-USD | 17.66 | -0.08 | exit signal |
| 2026-09-30T01:25 | Bollinger reversion | sell | BTC-USD | 18.54 | -0.10 | exit signal |
| 2026-09-30T01:25 | Candlestick reversal | sell | SOL-USD | 18.94 | -0.02 | exit signal |
| 2026-09-30T01:25 | Candlestick reversal | sell | DOGE-USD | 15.19 | 0.02 | exit signal |
| 2026-09-30T01:25 | Squeeze breakout | buy | SOL-USD | 22.37 | — | entry signal |
| 2026-09-30T01:25 | Keltner breakout | buy | DOGE-USD | 21.37 | — | entry signal |
| 2026-09-30T01:25 | Bollinger breakout | buy | SOL-USD | 20.11 | — | entry signal |
| 2026-09-30T01:25 | Bollinger breakout | buy | DOGE-USD | 20.11 | — | entry signal |
| 2026-09-30T01:25 | Donchian 55/20 | buy | XRP-USD | 21.76 | — | entry signal |
| 2026-09-30T01:25 | Donchian 20/10 | buy | SOL-USD | 20.23 | — | entry signal |
| 2026-09-30T01:25 | Donchian 20/10 | buy | DOGE-USD | 20.23 | — | entry signal |
| 2026-09-30T01:25 | OBV trend | buy | SOL-USD | 18.63 | — | entry signal |
| 2026-09-30T01:25 | RSI momentum | buy | SOL-USD | 19.91 | — | entry signal |
| 2026-09-30T01:25 | RSI momentum | buy | DOGE-USD | 19.91 | — | entry signal |
| 2026-09-30T01:25 | ROC + volume | buy | SOL-USD | 21.83 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
