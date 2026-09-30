# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T14:40:05.000181+00:00 · 6979 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.65 (-0.35%)

Closed trades 25, win rate 68.0%, fees £0.72, max drawdown -1.39%.

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

Today: 15288 decisions in 2229 calls, $0.2024 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T14:40 | 1 / 19 / 10 | LABU 18% |  |
| Breezy | 2026-09-30T14:40 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-09-30T14:40 | 6 / 23 / 1 | COIN 36%, LABU 35% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.39 | 1.39 | 2 | 50.0 | 14.55 | 3.14 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.73 | 1.12 | -1.49 | 17 |
| 3 | Copy: Congress Democrats (NANC) | copy | 100.28 | 0.28 | 0 | — | 7.37 | 3.00 | -3.62 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.91 | -0.09 | 1 | 100.0 | -0.27 | -0.01 | -9.74 | 24 |
| 7 | Agent | meta | 99.65 | -0.35 | 25 | 68.0 | -9.39 | -6.15 | -10.16 | 211 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 99.62 | -0.38 | 0 | — | -2.83 | -1.68 | -5.09 | 2 |
| 9 | Hold BTC | benchmark | 99.60 | -0.40 | 0 | — | 28.81 | 3.63 | -8.68 | 1 |
| 10 | RSI(14) reversion · 1h | reversion | 99.56 | -0.44 | 8 | 62.5 | 1.31 | 0.45 | -6.83 | 123 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 7 | 42.9 | 3.14 | 1.60 | -1.76 | 83 |
| 12 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 22 | 27.3 | -12.80 | -4.28 | -14.92 | 123 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.54 | -0.46 | 0 | — | 4.63 | 1.34 | -7.93 | 7 |
| 14 | Hold SPY | benchmark | 99.53 | -0.47 | 0 | — | 4.17 | 2.28 | -3.66 | 1 |
| 15 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -0.63 | -0.29 | -4.81 | 96 |
| 16 | Copy: Insider buying | copy | 99.49 | -0.51 | 2 | 100.0 | -13.41 | -2.60 | -17.74 | 73 |
| 17 | Timing: Nasdaq FTD · TQQQ | daily | 99.24 | -0.76 | 0 | — | -9.43 | -1.86 | -15.27 | 2 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 99.00 | -1.00 | 0 | — | -3.33 | -1.59 | -5.14 | 1 |
| 20 | Daily: Bullish score | daily | 98.99 | -1.01 | 3 | 0.0 | -0.19 | 0.17 | -12.76 | 14 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.90 | -1.10 | 0 | — | -5.27 | -1.12 | -10.06 | 1 |
| 22 | Copy: Warren Buffett (BRK-B) | copy | 98.86 | -1.14 | 0 | — | -0.65 | -0.20 | -7.65 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 2 | 0.0 | -0.61 | -0.18 | -4.88 | 17 |
| 24 | Gap and go | momentum | 98.49 | -1.51 | 10 | 10.0 | 15.55 | 3.84 | -4.73 | 183 |
| 25 | Stochastic reversion · 1h | reversion | 98.41 | -1.59 | 26 | 53.8 | -12.31 | -2.73 | -13.54 | 326 |
| 26 | Williams %R · 1h | reversion | 98.37 | -1.63 | 47 | 46.8 | -18.22 | -3.43 | -19.93 | 489 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.49 | 0.26 | -15.21 | 46 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.27 | -1.73 | 0 | — | 24.27 | 3.56 | -6.29 | 1 |
| 29 | Z-score reversion · 1h | reversion | 98.25 | -1.75 | 11 | 45.5 | 4.82 | 1.16 | -8.60 | 154 |
| 30 | CCI reversion · 1h | reversion | 98.19 | -1.81 | 38 | 34.2 | 1.88 | 0.48 | -12.41 | 411 |
| 31 | Candlestick reversal · 1h | reversion | 98.07 | -1.93 | 33 | 24.2 | -26.06 | -6.35 | -26.96 | 492 |
| 32 | Agent (rotation) | meta | 97.94 | -2.06 | 33 | 12.1 | -6.17 | -2.23 | -10.90 | 213 |
| 33 | Connors RSI(2) · 1h | reversion | 97.65 | -2.35 | 47 | 46.8 | -11.29 | -3.58 | -11.76 | 233 |
| 34 | Bollinger reversion · 1h | reversion | 97.03 | -2.97 | 31 | 32.3 | -17.40 | -4.83 | -18.25 | 312 |
| 35 | EMA 20/50 cross · 1h | trend | 96.93 | -3.07 | 16 | 6.2 | 14.95 | 1.90 | -12.19 | 129 |
| 36 | Opening range 30m | breakout | 96.89 | -3.11 | 38 | 13.2 | -10.07 | -2.93 | -14.28 | 557 |
| 37 | Supertrend · 1h | trend | 96.31 | -3.69 | 18 | 5.6 | 2.90 | 0.59 | -16.43 | 197 |
| 38 | Trend pullback · 1h | trend | 96.11 | -3.89 | 29 | 10.3 | -25.19 | -6.69 | -25.81 | 147 |
| 39 | Opening range 15m | breakout | 95.80 | -4.20 | 49 | 12.2 | -11.62 | -3.17 | -16.70 | 687 |
| 40 | Agent (ML meta-label) | meta | 95.71 | -4.29 | 150 | 12.7 | 3.57 | 0.77 | -12.52 | 401 |
| 41 | Donchian 55/20 · 1h | breakout | 95.42 | -4.58 | 15 | 0.0 | 3.63 | 0.68 | -16.96 | 115 |
| 42 | Max aggression: 5-day momentum | meta | 95.22 | -4.78 | 3 | 66.7 | -13.55 | -0.96 | -29.56 | 29 |
| 43 | MACD cross · 1h | trend | 94.96 | -5.04 | 40 | 10.0 | -13.72 | -2.17 | -17.31 | 470 |
| 44 | MFI reversion · 1h | reversion | 94.95 | -5.05 | 50 | 18.0 | -9.50 | -1.73 | -17.27 | 129 |
| 45 | Squeeze breakout · 1h | breakout | 94.92 | -5.08 | 15 | 6.7 | 10.38 | 1.83 | -7.74 | 105 |
| 46 | Parabolic SAR · 1h | trend | 94.72 | -5.28 | 26 | 11.5 | -8.04 | -1.00 | -18.82 | 304 |
| 47 | Three white soldiers | momentum | 94.34 | -5.66 | 47 | 17.0 | -50.34 | -27.84 | -50.39 | 608 |
| 48 | Volume breakout · 1h | breakout | 94.22 | -5.78 | 28 | 3.6 | 5.05 | 0.88 | -12.60 | 127 |
| 49 | ADX DI cross · 1h | trend | 93.98 | -6.02 | 32 | 6.2 | -15.84 | -2.94 | -17.86 | 259 |
| 50 | Max aggression: 1-day momentum | meta | 93.86 | -6.14 | 3 | 33.3 | -21.69 | -1.04 | -41.28 | 42 |
| 51 | Ichimoku · 1h | trend | 93.47 | -6.54 | 19 | 15.8 | 5.42 | 0.83 | -15.13 | 122 |
| 52 | Bollinger breakout · 1h | breakout | 93.41 | -6.59 | 24 | 8.3 | 6.58 | 1.05 | -10.17 | 288 |
| 53 | VWAP momentum · 1h | momentum | 93.39 | -6.61 | 109 | 13.8 | -34.13 | -5.13 | -35.38 | 1246 |
| 54 | RSI momentum · 1h | momentum | 93.34 | -6.67 | 28 | 3.6 | -1.56 | -0.01 | -15.29 | 218 |
| 55 | Triple EMA stack · 1h | trend | 92.44 | -7.56 | 32 | 6.2 | -6.62 | -0.61 | -22.22 | 216 |
| 56 | MACD zero-line · 1h | trend | 92.10 | -7.90 | 23 | 4.3 | -7.72 | -0.90 | -16.16 | 229 |
| 57 | Keltner breakout · 1h | breakout | 91.92 | -8.08 | 14 | 0.0 | -8.24 | -0.94 | -19.66 | 223 |
| 58 | EMA 9/21 cross · 1h | trend | 91.56 | -8.44 | 46 | 10.9 | -5.25 | -0.52 | -16.92 | 318 |
| 59 | Donchian 20/10 · 1h | breakout | 91.48 | -8.52 | 21 | 9.5 | 3.31 | 0.63 | -13.35 | 218 |
| 60 | Heikin-Ashi · 1h | trend | 91.37 | -8.63 | 46 | 10.9 | -26.32 | -3.99 | -31.31 | 676 |
| 61 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -70.91 | -20.96 | -71.11 | 1482 |
| 62 | OBV trend · 1h | momentum | 90.11 | -9.89 | 63 | 6.3 | -14.29 | -1.67 | -24.90 | 328 |
| 63 | Squeeze breakout | breakout | 87.72 | -12.28 | 103 | 13.6 | -59.89 | -18.65 | -59.89 | 1193 |
| 64 | ROC + volume · 1h | momentum | 87.06 | -12.94 | 59 | 5.1 | -12.00 | -1.54 | -21.75 | 416 |
| 65 | Donchian 55/20 | breakout | 85.97 | -14.03 | 106 | 16.0 | -67.80 | -15.55 | -67.87 | 1306 |
| 66 | Volume breakout | breakout | 85.28 | -14.72 | 113 | 15.0 | -62.30 | -19.91 | -62.61 | 899 |
| 67 | ROC + volume | momentum | 85.04 | -14.96 | 166 | 17.5 | -72.84 | -17.80 | -72.92 | 1652 |
| 68 | EMA 20/50 cross | trend | 83.81 | -16.19 | 139 | 14.4 | -78.79 | -17.52 | -78.84 | 1479 |
| 69 | Keltner breakout | breakout | 83.54 | -16.46 | 163 | 13.5 | -84.65 | -34.53 | -84.71 | 1894 |
| 70 | Ichimoku | trend | 83.32 | -16.68 | 127 | 8.7 | -80.50 | -26.05 | -80.55 | 1748 |
| 71 | Z-score reversion | reversion | 83.32 | -16.68 | 194 | 30.4 | -84.65 | -27.61 | -84.66 | 2109 |
| 72 | VWAP reversion | reversion | 82.93 | -17.07 | 150 | 22.7 | -71.95 | -17.85 | -72.06 | 1404 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 80.06 | -19.94 | 196 | 17.9 | -87.46 | -24.61 | -87.58 | 1960 |
| 76 | MFI reversion | reversion | 80.03 | -19.97 | 190 | 18.9 | -88.15 | -35.41 | -88.17 | 2158 |
| 77 | Donchian 20/10 | breakout | 79.70 | -20.30 | 219 | 17.8 | -90.65 | -29.17 | -90.69 | 2675 |
| 78 | MACD zero-line | trend | 79.48 | -20.52 | 221 | 14.9 | -91.86 | -36.01 | -91.89 | 2361 |
| 79 | Trend pullback | trend | 78.69 | -21.32 | 182 | 18.7 | -90.59 | -33.16 | -90.65 | 2262 |
| 80 | Triple EMA stack | trend | 78.54 | -21.46 | 231 | 16.5 | -92.90 | -35.26 | -92.98 | 2599 |
| 81 | Bollinger breakout | breakout | 77.97 | -22.03 | 230 | 15.7 | -93.82 | -42.27 | -93.83 | 2861 |
| 82 | RSI momentum | momentum | 77.51 | -22.49 | 216 | 13.9 | -90.50 | -29.25 | -90.53 | 2392 |
| 83 | ADX DI cross | trend | 76.89 | -23.11 | 214 | 7.5 | -89.48 | -45.42 | -89.48 | 2100 |
| 84 | Consensus | meta | 74.85 | -25.15 | 201 | 7.0 | -94.61 | -30.24 | -94.62 | 2644 |
| 85 | Stochastic reversion | reversion | 74.25 | -25.75 | 345 | 23.2 | -95.94 | -44.96 | -95.96 | 4056 |
| 86 | Connors RSI(2) | reversion | 74.20 | -25.80 | 258 | 16.3 | -96.38 | -40.30 | -96.39 | 3612 |
| 87 | EMA 9/21 cross | trend | 74.13 | -25.87 | 306 | 17.0 | -97.42 | -41.30 | -97.45 | 3540 |
| 88 | Candlestick reversal | reversion | 73.20 | -26.80 | 303 | 12.5 | -99.35 | -48.75 | -99.35 | 5590 |
| 89 | Bollinger reversion | reversion | 72.85 | -27.15 | 325 | 15.1 | -95.81 | -43.67 | -95.82 | 3687 |
| 90 | OBV trend | momentum | 71.02 | -28.98 | 304 | 14.8 | -95.93 | -47.58 | -95.95 | 3539 |
| 91 | CCI reversion | reversion | 70.42 | -29.58 | 268 | 10.8 | -98.47 | -49.59 | -98.47 | 4686 |
| 92 | Parabolic SAR | trend | 69.99 | -30.01 | 295 | 12.5 | -96.99 | -55.30 | -97.00 | 3625 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.54 | -36.19 | -98.55 | 5265 |
| 94 | MACD cross | trend | 68.27 | -31.73 | 310 | 13.5 | -99.71 | -64.05 | -99.72 | 6076 |
| 95 | Williams %R | reversion | 67.74 | -32.26 | 381 | 19.7 | -99.53 | -57.23 | -99.53 | 6096 |
| 96 | Heikin-Ashi | trend | 67.20 | -32.80 | 287 | 5.6 | -99.89 | -77.30 | -99.89 | 8301 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T14:40 | MACD cross · 1h | buy | SPY | 4.77 | — | entry |
| 2026-09-30T14:40 | MACD cross · 1h | sell | LABU | 4.77 | 0.19 | rebalance down |
| 2026-09-30T14:40 | Stochastic reversion | buy | SOL-USD | 5.68 | — | entry signal |
| 2026-09-30T14:40 | Stochastic reversion | buy | MSTR | 5.72 | — | entry signal |
| 2026-09-30T14:40 | Stochastic reversion | buy | ETHU | 5.72 | — | entry signal |
| 2026-09-30T14:40 | Stochastic reversion | buy | ETH-USD | 5.72 | — | entry signal |
| 2026-09-30T14:40 | Stochastic reversion | buy | BTC-USD | 5.72 | — | entry signal |
| 2026-09-30T14:40 | Stochastic reversion | buy | BITX | 5.72 | — | entry signal |
| 2026-09-30T14:40 | Stochastic reversion | sell | XRP-USD | 4.84 | -0.04 | rebalance down |
| 2026-09-30T14:40 | Stochastic reversion | sell | TSLA | 4.93 | 0.05 | rebalance down |
| 2026-09-30T14:40 | Stochastic reversion | sell | SQQQ | 4.96 | 0.02 | rebalance down |
| 2026-09-30T14:40 | Stochastic reversion | sell | SOXL | 4.83 | -0.05 | rebalance down |
| 2026-09-30T14:40 | Stochastic reversion | sell | DOGE-USD | 4.83 | -0.05 | rebalance down |
| 2026-09-30T14:40 | Stochastic reversion | sell | COIN | 4.94 | 0.02 | rebalance down |
| 2026-09-30T14:40 | Stochastic reversion | sell | AMD | 4.93 | -0.02 | rebalance down |
| 2026-09-30T14:40 | VWAP reversion | buy | MSTR | 11.84 | — | entry signal |
| 2026-09-30T14:40 | VWAP reversion | buy | ETHU | 11.85 | — | entry signal |
| 2026-09-30T14:40 | VWAP reversion | buy | COIN | 11.85 | — | entry signal |
| 2026-09-30T14:40 | VWAP reversion | buy | BITX | 11.85 | — | entry signal |
| 2026-09-30T14:40 | VWAP reversion | sell | SQQQ | 4.90 | 0.02 | rebalance down |
| 2026-09-30T14:40 | VWAP reversion | sell | IWM | 8.89 | -0.01 | rebalance down |
| 2026-09-30T14:40 | VWAP reversion | sell | AMD | 8.88 | -0.01 | rebalance down |
| 2026-09-30T14:40 | Z-score reversion | buy | XRP-USD | 12.56 | — | entry signal |
| 2026-09-30T14:40 | Z-score reversion | buy | ETH-USD | 16.68 | — | entry signal |
| 2026-09-30T14:40 | Z-score reversion | sell | TSLA | 4.33 | 0.02 | rebalance down |
| 2026-09-30T14:40 | Z-score reversion | sell | SQQQ | 4.22 | 0.01 | rebalance down |
| 2026-09-30T14:40 | Bollinger reversion | buy | XRP-USD | 7.24 | — | entry signal |
| 2026-09-30T14:40 | Bollinger reversion | buy | ETHU | 7.30 | — | entry signal |
| 2026-09-30T14:40 | Bollinger reversion | buy | DOGE-USD | 7.30 | — | entry signal |
| 2026-09-30T14:40 | Bollinger reversion | buy | COIN | 7.30 | — | entry signal |
| 2026-09-30T14:40 | Bollinger reversion | buy | BTC-USD | 7.30 | — | entry signal |
| 2026-09-30T14:40 | Bollinger reversion | sell | SQQQ | 7.28 | -0.02 | rebalance down |
| 2026-09-30T14:40 | Bollinger reversion | sell | SOL-USD | 3.71 | -0.02 | rebalance down |
| 2026-09-30T14:40 | Bollinger reversion | sell | META | 7.30 | -0.03 | rebalance down |
| 2026-09-30T14:40 | Bollinger reversion | sell | ETH-USD | 10.85 | -0.09 | rebalance down |
| 2026-09-30T14:40 | Bollinger reversion | sell | AMD | 7.29 | -0.02 | rebalance down |
| 2026-09-30T14:40 | RSI(14) reversion | buy | XRP-USD | 12.98 | — | entry signal |
| 2026-09-30T14:40 | RSI(14) reversion | buy | SOL-USD | 12.99 | — | entry signal |
| 2026-09-30T14:40 | RSI(14) reversion | buy | ETH-USD | 12.99 | — | entry signal |
| 2026-09-30T14:40 | RSI(14) reversion | buy | COIN | 12.99 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
