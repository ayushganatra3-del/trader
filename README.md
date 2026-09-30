# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T08:10:05.000203+00:00 · 6659 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.64 (-0.36%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.98 | -0.01 |

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

Today: 6345 decisions in 1269 calls, $0.0889 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T08:10 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-09-30T08:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T08:10 | 2 / 3 / 0 | ETH-USD 22% |  |

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
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.65 | -7.93 | 7 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Copy: Congress Democrats (NANC) | copy | 99.86 | -0.14 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Agent | meta | 99.64 | -0.36 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.52 | -0.48 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 11 | Agent (aggressive) | meta | 99.46 | -0.54 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Hold BTC | benchmark | 99.31 | -0.69 | 0 | — | 28.93 | 3.64 | -8.68 | 1 |
| 13 | Hold SPY | benchmark | 99.29 | -0.71 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.20 | -0.80 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.20 | -0.80 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.03 | -0.97 | 20 | 25.0 | -13.02 | -4.40 | -14.80 | 122 |
| 18 | RSI(14) reversion · 1h | reversion | 98.96 | -1.04 | 7 | 57.1 | 5.65 | 1.46 | -7.03 | 118 |
| 19 | Daily: Bullish score | daily | 98.85 | -1.15 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 20 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 21 | Z-score reversion · 1h | reversion | 98.73 | -1.27 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Copy: Insider buying | copy | 98.68 | -1.32 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.67 | -4.73 | 182 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Stochastic reversion · 1h | reversion | 98.33 | -1.67 | 26 | 53.8 | -13.97 | -3.05 | -15.13 | 330 |
| 26 | Williams %R · 1h | reversion | 98.31 | -1.69 | 40 | 45.0 | -17.99 | -3.33 | -19.41 | 488 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.24 | -1.76 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Candlestick reversal · 1h | reversion | 98.23 | -1.77 | 25 | 20.0 | -26.19 | -6.57 | -26.82 | 486 |
| 29 | CCI reversion · 1h | reversion | 98.06 | -1.95 | 35 | 34.3 | 0.28 | 0.21 | -12.41 | 410 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.76 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.71 | -2.29 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.59 | -2.41 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.53 | -2.47 | 13 | 7.7 | 16.56 | 1.97 | -14.13 | 126 |
| 34 | Max aggression: 5-day momentum | meta | 97.50 | -2.50 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Bollinger reversion · 1h | reversion | 97.08 | -2.92 | 22 | 27.3 | -17.50 | -4.87 | -18.12 | 312 |
| 37 | Squeeze breakout · 1h | breakout | 97.02 | -2.98 | 9 | 11.1 | 15.55 | 2.73 | -5.11 | 92 |
| 38 | Max aggression: 1-day momentum | meta | 96.47 | -3.53 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.43 | -3.58 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.34 | -3.66 | 18 | 5.6 | 1.92 | 0.46 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.19 | -3.81 | 140 | 12.9 | 1.77 | 0.46 | -11.31 | 399 |
| 42 | Trend pullback · 1h | trend | 96.13 | -3.87 | 28 | 10.7 | -28.93 | -7.09 | -29.45 | 147 |
| 43 | MACD cross · 1h | trend | 95.93 | -4.07 | 40 | 10.0 | -18.59 | -3.14 | -21.48 | 460 |
| 44 | Parabolic SAR · 1h | trend | 95.71 | -4.29 | 26 | 11.5 | -8.02 | -1.00 | -18.82 | 293 |
| 45 | Donchian 55/20 · 1h | breakout | 95.65 | -4.35 | 12 | 0.0 | 4.53 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.85 | -16.91 | 684 |
| 47 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.28 | -27.84 | -50.33 | 607 |
| 48 | MFI reversion · 1h | reversion | 95.16 | -4.83 | 44 | 13.6 | -9.99 | -1.83 | -17.20 | 129 |
| 49 | Ichimoku · 1h | trend | 95.08 | -4.92 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.82 | -5.17 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.14 | -5.86 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 53 | Donchian 20/10 · 1h | breakout | 94.03 | -5.97 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 54 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.33 | 0.27 | -18.68 | 212 |
| 55 | ADX DI cross · 1h | trend | 93.84 | -6.16 | 30 | 6.7 | -16.22 | -3.00 | -17.90 | 256 |
| 56 | Triple EMA stack · 1h | trend | 93.76 | -6.24 | 30 | 6.7 | -6.79 | -0.63 | -22.58 | 226 |
| 57 | MACD zero-line · 1h | trend | 93.75 | -6.25 | 21 | 4.8 | -5.81 | -0.63 | -14.64 | 223 |
| 58 | VWAP momentum · 1h | momentum | 93.50 | -6.50 | 103 | 12.6 | -35.08 | -5.31 | -35.61 | 1240 |
| 59 | Heikin-Ashi · 1h | trend | 92.61 | -7.39 | 45 | 11.1 | -26.24 | -3.97 | -30.59 | 671 |
| 60 | EMA 9/21 cross · 1h | trend | 92.59 | -7.41 | 45 | 11.1 | -4.26 | -0.39 | -16.92 | 308 |
| 61 | OBV trend · 1h | momentum | 92.30 | -7.70 | 54 | 7.4 | -13.09 | -1.44 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.12 | -71.11 | 1469 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 88.51 | -11.49 | 99 | 14.1 | -59.84 | -18.62 | -59.84 | 1192 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.82 | -19.79 | -61.89 | 894 |
| 66 | ROC + volume | momentum | 86.74 | -13.26 | 150 | 18.7 | -72.02 | -17.59 | -72.02 | 1626 |
| 67 | Donchian 55/20 | breakout | 86.18 | -13.82 | 100 | 15.0 | -68.14 | -15.67 | -68.14 | 1300 |
| 68 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.80 | -34.05 | -84.80 | 1895 |
| 69 | Ichimoku | trend | 84.44 | -15.56 | 118 | 8.5 | -80.42 | -26.01 | -80.44 | 1741 |
| 70 | EMA 20/50 cross | trend | 84.37 | -15.62 | 133 | 15.0 | -79.02 | -17.70 | -79.02 | 1472 |
| 71 | VWAP reversion | reversion | 83.95 | -16.05 | 143 | 21.7 | -71.72 | -17.61 | -72.00 | 1400 |
| 72 | Z-score reversion | reversion | 83.65 | -16.35 | 192 | 30.7 | -84.59 | -27.49 | -84.59 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.11 | -19.89 | 188 | 19.1 | -88.13 | -35.49 | -88.14 | 2151 |
| 76 | MACD zero-line | trend | 79.68 | -20.32 | 214 | 15.4 | -91.89 | -36.11 | -91.89 | 2359 |
| 77 | Donchian 20/10 | breakout | 79.52 | -20.48 | 213 | 16.9 | -90.93 | -29.70 | -90.93 | 2675 |
| 78 | Supertrend | trend | 79.47 | -20.53 | 190 | 16.8 | -87.71 | -24.97 | -87.71 | 1962 |
| 79 | Bollinger breakout | breakout | 79.08 | -20.92 | 215 | 15.8 | -93.91 | -42.14 | -93.91 | 2864 |
| 80 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.58 | -33.23 | -90.58 | 2259 |
| 81 | Triple EMA stack | trend | 78.14 | -21.86 | 224 | 14.7 | -93.16 | -36.18 | -93.16 | 2622 |
| 82 | RSI momentum | momentum | 77.74 | -22.26 | 207 | 12.6 | -90.59 | -29.46 | -90.59 | 2384 |
| 83 | ADX DI cross | trend | 77.72 | -22.28 | 206 | 7.8 | -89.45 | -45.69 | -89.45 | 2116 |
| 84 | Connors RSI(2) | reversion | 77.01 | -22.99 | 242 | 16.9 | -96.29 | -39.17 | -96.29 | 3601 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.54 | -29.53 | -94.55 | 2640 |
| 86 | Stochastic reversion | reversion | 74.93 | -25.07 | 342 | 23.4 | -95.92 | -44.79 | -95.93 | 4057 |
| 87 | Candlestick reversal | reversion | 74.07 | -25.93 | 290 | 12.1 | -99.36 | -49.41 | -99.36 | 5591 |
| 88 | EMA 9/21 cross | trend | 73.63 | -26.37 | 297 | 16.2 | -97.45 | -41.79 | -97.45 | 3536 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.80 | -43.45 | -95.80 | 3687 |
| 90 | OBV trend | momentum | 72.17 | -27.83 | 290 | 14.5 | -95.99 | -48.99 | -95.99 | 3554 |
| 91 | Parabolic SAR | trend | 71.03 | -28.97 | 281 | 12.5 | -97.00 | -54.92 | -97.00 | 3627 |
| 92 | CCI reversion | reversion | 71.03 | -28.97 | 262 | 10.7 | -98.47 | -49.69 | -98.47 | 4702 |
| 93 | MACD cross | trend | 69.36 | -30.64 | 291 | 13.1 | -99.72 | -65.03 | -99.72 | 6081 |
| 94 | Heikin-Ashi | trend | 68.78 | -31.22 | 251 | 3.2 | -99.90 | -78.28 | -99.90 | 8301 |
| 95 | Williams %R | reversion | 68.77 | -31.23 | 367 | 19.9 | -99.53 | -57.42 | -99.53 | 6110 |
| 96 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.54 | -36.12 | -98.54 | 5218 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T08:10 | Bollinger breakout | sell | ETH-USD | 19.64 | -0.18 | stop-loss |
| 2026-09-30T08:10 | Donchian 20/10 | sell | ETH-USD | 19.75 | -0.18 | stop-loss |
| 2026-09-30T08:10 | OBV trend | sell | XRP-USD | 18.01 | -0.16 | exit signal |
| 2026-09-30T08:10 | OBV trend | sell | ETH-USD | 17.99 | -0.15 | exit signal |
| 2026-09-30T08:10 | OBV trend | sell | DOGE-USD | 17.97 | -0.19 | exit signal |
| 2026-09-30T08:10 | RSI momentum | sell | DOGE-USD | 19.28 | -0.24 | stop-loss |
| 2026-09-30T08:10 | Ichimoku | sell | XRP-USD | 21.03 | -0.18 | exit signal |
| 2026-09-30T08:10 | Ichimoku | sell | ETH-USD | 21.10 | -0.19 | stop-loss |
| 2026-09-30T08:10 | Ichimoku | sell | DOGE-USD | 21.05 | -0.22 | exit signal |
| 2026-09-30T08:10 | ADX DI cross | buy | DOGE-USD | 3.90 | — | rebalance up |
| 2026-09-30T08:10 | ADX DI cross | sell | XRP-USD | 15.54 | -0.12 | exit signal |
| 2026-09-30T08:10 | ADX DI cross | sell | SOL-USD | 15.47 | -0.16 | exit signal |
| 2026-09-30T08:10 | ADX DI cross | sell | ETH-USD | 15.55 | -0.11 | exit signal |
| 2026-09-30T08:10 | Parabolic SAR | sell | XRP-USD | 17.69 | -0.14 | exit signal |
| 2026-09-30T08:10 | Parabolic SAR | sell | DOGE-USD | 17.69 | -0.14 | exit signal |
| 2026-09-30T08:10 | MACD zero-line | sell | XRP-USD | 19.86 | -0.20 | exit signal |
| 2026-09-30T08:10 | MACD cross | sell | XRP-USD | 10.35 | -0.10 | exit signal |
| 2026-09-30T08:10 | EMA 20/50 cross | sell | ETH-USD | 21.00 | -0.18 | exit signal |
| 2026-09-30T08:05 | Connors RSI(2) | buy | XRP-USD | 19.28 | — | entry signal |
| 2026-09-30T08:05 | Ichimoku | buy | XRP-USD | 21.21 | — | entry signal |
| 2026-09-30T08:00 | OBV trend | buy | ETH-USD | 18.14 | — | entry signal |
| 2026-09-30T08:00 | Heikin-Ashi | sell | XRP-USD | 13.75 | -0.09 | exit signal |
| 2026-09-30T08:00 | Heikin-Ashi | sell | SOL-USD | 13.75 | -0.09 | exit signal |
| 2026-09-30T08:00 | Heikin-Ashi | sell | ETH-USD | 13.77 | -0.07 | exit signal |
| 2026-09-30T08:00 | Heikin-Ashi | sell | DOGE-USD | 13.77 | -0.07 | exit signal |
| 2026-09-30T08:00 | Heikin-Ashi | sell | BTC-USD | 13.75 | -0.08 | exit signal |
| 2026-09-30T08:00 | Triple EMA stack | buy | DOGE-USD | 19.58 | — | entry signal |
| 2026-09-30T08:00 | EMA 20/50 cross | buy | ETH-USD | 21.17 | — | entry signal |
| 2026-09-30T08:00 | EMA 9/21 cross | buy | DOGE-USD | 3.70 | — | rebalance up |
| 2026-09-30T08:00 | EMA 9/21 cross | sell | SOL-USD | 3.73 | -0.03 | exit signal |
| 2026-09-30T07:55 | OBV trend | buy | DOGE-USD | 18.16 | — | entry signal |
| 2026-09-30T07:55 | ROC + volume | buy | DOGE-USD | 21.73 | — | entry signal |
| 2026-09-30T07:55 | Ichimoku | buy | DOGE-USD | 21.27 | — | entry signal |
| 2026-09-30T07:55 | Ichimoku | buy | BTC-USD | 21.27 | — | entry signal |
| 2026-09-30T07:55 | EMA 20/50 cross | buy | DOGE-USD | 21.20 | — | entry signal |
| 2026-09-30T07:50 | Donchian 20/10 | buy | ETH-USD | 19.92 | — | entry signal |
| 2026-09-30T07:50 | RSI momentum | buy | DOGE-USD | 19.52 | — | entry signal |
| 2026-09-30T07:50 | Ichimoku | buy | ETH-USD | 21.29 | — | entry signal |
| 2026-09-30T07:50 | EMA 9/21 cross | buy | SOL-USD | 3.76 | — | entry signal |
| 2026-09-30T07:50 | EMA 9/21 cross | sell | DOGE-USD | 3.72 | -0.01 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
