# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T10:40:05.000180+00:00 · 6791 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.60 (-0.40%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.94 | -0.05 |

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

Today: 8325 decisions in 1665 calls, $0.1165 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T10:40 | 1 / 2 / 2 | DOGE-USD 17% |  |
| Breezy | 2026-09-30T10:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T10:40 | 5 / 0 / 0 | DOGE-USD 38%, BTC-USD 32% |  |

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
| 7 | Hold BTC | benchmark | 99.90 | -0.10 | 0 | — | 29.42 | 3.69 | -8.68 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Copy: Congress Democrats (NANC) | copy | 99.67 | -0.33 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 10 | Agent | meta | 99.60 | -0.40 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 11 | Agent (aggressive) | meta | 99.36 | -0.64 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.33 | -0.67 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 13 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 14 | Hold SPY | benchmark | 99.10 | -0.90 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.01 | -0.98 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 99.01 | -0.99 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 17 | VWAP reversion · 1h | reversion | 98.94 | -1.06 | 20 | 25.0 | -12.98 | -4.39 | -14.75 | 122 |
| 18 | RSI(14) reversion · 1h | reversion | 98.92 | -1.08 | 7 | 57.1 | 6.37 | 1.63 | -7.03 | 116 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 20 | Daily: Bullish score | daily | 98.67 | -1.33 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 21 | Z-score reversion · 1h | reversion | 98.59 | -1.41 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Copy: Insider buying | copy | 98.51 | -1.49 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Williams %R · 1h | reversion | 98.35 | -1.65 | 40 | 45.0 | -17.63 | -3.25 | -19.41 | 488 |
| 26 | Candlestick reversal · 1h | reversion | 98.18 | -1.82 | 25 | 20.0 | -25.94 | -6.50 | -26.70 | 487 |
| 27 | Stochastic reversion · 1h | reversion | 98.15 | -1.85 | 26 | 53.8 | -13.86 | -3.02 | -15.12 | 331 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.05 | -1.95 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | CCI reversion · 1h | reversion | 97.87 | -2.13 | 35 | 34.3 | 1.38 | 0.40 | -12.41 | 409 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.57 | -2.43 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.41 | -2.59 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.39 | -2.61 | 13 | 7.7 | 16.98 | 2.01 | -14.13 | 125 |
| 34 | Max aggression: 5-day momentum | meta | 97.31 | -2.69 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Squeeze breakout · 1h | breakout | 96.98 | -3.02 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 37 | Bollinger reversion · 1h | reversion | 96.90 | -3.10 | 22 | 27.3 | -17.38 | -4.84 | -18.00 | 312 |
| 38 | Supertrend · 1h | trend | 96.31 | -3.69 | 18 | 5.6 | 2.08 | 0.48 | -16.43 | 194 |
| 39 | Max aggression: 1-day momentum | meta | 96.28 | -3.72 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 40 | Daily: SMA 20/50 cross · AAPL | daily | 96.24 | -3.76 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 41 | Agent (ML meta-label) | meta | 96.07 | -3.93 | 141 | 12.8 | -1.61 | -0.12 | -13.41 | 397 |
| 42 | Trend pullback · 1h | trend | 95.99 | -4.01 | 28 | 10.7 | -29.16 | -7.16 | -29.64 | 148 |
| 43 | MACD cross · 1h | trend | 95.75 | -4.25 | 40 | 10.0 | -18.67 | -3.15 | -21.59 | 464 |
| 44 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 45 | Parabolic SAR · 1h | trend | 95.53 | -4.47 | 26 | 11.5 | -7.86 | -0.98 | -18.82 | 295 |
| 46 | Donchian 55/20 · 1h | breakout | 95.47 | -4.53 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 47 | MFI reversion · 1h | reversion | 95.17 | -4.83 | 44 | 13.6 | -9.57 | -1.74 | -17.20 | 129 |
| 48 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.28 | -27.84 | -50.33 | 607 |
| 49 | Ichimoku · 1h | trend | 94.99 | -5.01 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.74 | -5.26 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.03 | 0.23 | -18.68 | 213 |
| 53 | RSI momentum · 1h | momentum | 94.01 | -5.99 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 54 | Donchian 20/10 · 1h | breakout | 93.99 | -6.01 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | MACD zero-line · 1h | trend | 93.71 | -6.29 | 21 | 4.8 | -5.98 | -0.65 | -14.64 | 224 |
| 56 | Triple EMA stack · 1h | trend | 93.68 | -6.32 | 30 | 6.7 | -6.73 | -0.62 | -22.58 | 226 |
| 57 | ADX DI cross · 1h | trend | 93.66 | -6.34 | 30 | 6.7 | -15.90 | -2.94 | -17.73 | 254 |
| 58 | VWAP momentum · 1h | momentum | 93.33 | -6.67 | 103 | 12.6 | -34.58 | -5.21 | -35.64 | 1241 |
| 59 | Heikin-Ashi · 1h | trend | 92.52 | -7.48 | 45 | 11.1 | -26.26 | -3.97 | -30.63 | 671 |
| 60 | EMA 9/21 cross · 1h | trend | 92.49 | -7.51 | 45 | 11.1 | -4.29 | -0.39 | -16.92 | 308 |
| 61 | OBV trend · 1h | momentum | 92.12 | -7.88 | 54 | 7.4 | -12.85 | -1.41 | -25.19 | 316 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.13 | -71.11 | 1470 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 88.51 | -11.49 | 99 | 14.1 | -59.64 | -18.54 | -59.64 | 1189 |
| 65 | Volume breakout | breakout | 86.76 | -13.24 | 104 | 15.4 | -61.89 | -19.89 | -61.96 | 898 |
| 66 | ROC + volume | momentum | 86.49 | -13.51 | 152 | 18.4 | -72.06 | -17.61 | -72.17 | 1630 |
| 67 | Donchian 55/20 | breakout | 86.16 | -13.85 | 100 | 15.0 | -67.72 | -15.51 | -67.84 | 1299 |
| 68 | Keltner breakout | breakout | 85.21 | -14.79 | 150 | 13.3 | -84.61 | -34.02 | -84.67 | 1894 |
| 69 | Ichimoku | trend | 84.45 | -15.55 | 119 | 8.4 | -80.36 | -25.93 | -80.41 | 1742 |
| 70 | EMA 20/50 cross | trend | 84.43 | -15.57 | 135 | 14.8 | -78.98 | -17.67 | -79.10 | 1477 |
| 71 | VWAP reversion | reversion | 83.90 | -16.10 | 145 | 22.1 | -71.74 | -17.62 | -72.04 | 1402 |
| 72 | Z-score reversion | reversion | 83.65 | -16.34 | 193 | 30.6 | -84.59 | -27.49 | -84.60 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.06 | -19.94 | 190 | 18.9 | -88.14 | -35.50 | -88.15 | 2148 |
| 76 | Supertrend | trend | 79.87 | -20.13 | 191 | 16.8 | -87.60 | -24.84 | -87.69 | 1963 |
| 77 | Donchian 20/10 | breakout | 79.66 | -20.34 | 213 | 16.9 | -90.79 | -29.49 | -90.82 | 2674 |
| 78 | MACD zero-line | trend | 79.46 | -20.54 | 218 | 15.1 | -91.89 | -36.13 | -91.91 | 2361 |
| 79 | Bollinger breakout | breakout | 79.15 | -20.85 | 215 | 15.8 | -93.83 | -41.98 | -93.85 | 2863 |
| 80 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.58 | -33.23 | -90.58 | 2259 |
| 81 | Triple EMA stack | trend | 78.16 | -21.84 | 226 | 14.6 | -93.06 | -35.99 | -93.10 | 2620 |
| 82 | RSI momentum | momentum | 77.80 | -22.20 | 209 | 12.4 | -90.45 | -29.22 | -90.51 | 2382 |
| 83 | ADX DI cross | trend | 77.28 | -22.71 | 210 | 7.6 | -89.45 | -45.64 | -89.45 | 2112 |
| 84 | Connors RSI(2) | reversion | 76.86 | -23.14 | 244 | 16.8 | -96.26 | -38.85 | -96.26 | 3598 |
| 85 | Consensus | meta | 76.58 | -23.42 | 190 | 7.4 | -94.52 | -29.51 | -94.52 | 2640 |
| 86 | Stochastic reversion | reversion | 74.89 | -25.11 | 343 | 23.3 | -95.91 | -44.60 | -95.93 | 4055 |
| 87 | Candlestick reversal | reversion | 73.85 | -26.15 | 296 | 12.2 | -99.36 | -49.47 | -99.36 | 5593 |
| 88 | EMA 9/21 cross | trend | 73.69 | -26.31 | 301 | 15.9 | -97.45 | -41.71 | -97.47 | 3540 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.78 | -43.22 | -95.80 | 3684 |
| 90 | OBV trend | momentum | 72.30 | -27.70 | 290 | 14.5 | -95.89 | -48.38 | -95.91 | 3548 |
| 91 | Parabolic SAR | trend | 70.95 | -29.05 | 284 | 12.3 | -96.96 | -54.35 | -96.96 | 3626 |
| 92 | CCI reversion | reversion | 70.95 | -29.05 | 264 | 10.6 | -98.46 | -49.30 | -98.46 | 4699 |
| 93 | MACD cross | trend | 69.39 | -30.61 | 296 | 12.8 | -99.72 | -64.67 | -99.72 | 6081 |
| 94 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.56 | -36.45 | -98.57 | 5243 |
| 95 | Williams %R | reversion | 68.53 | -31.46 | 371 | 19.7 | -99.52 | -56.95 | -99.52 | 6107 |
| 96 | Heikin-Ashi | trend | 68.16 | -31.84 | 258 | 3.1 | -99.90 | -79.14 | -99.90 | 8305 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T10:40 | Heikin-Ashi | buy | XRP-USD | 3.42 | — | entry signal |
| 2026-09-30T10:40 | Heikin-Ashi | sell | DOGE-USD | 3.42 | -0.01 | rebalance down |
| 2026-09-30T10:40 | Parabolic SAR | buy | XRP-USD | 17.75 | — | entry signal |
| 2026-09-30T10:40 | MACD cross | buy | XRP-USD | 6.96 | — | entry signal |
| 2026-09-30T10:40 | MACD cross | sell | DOGE-USD | 3.53 | 0.02 | rebalance down |
| 2026-09-30T10:35 | Consensus | buy | SOL-USD | 19.17 | — | entry |
| 2026-09-30T10:35 | Donchian 55/20 | buy | SOL-USD | 8.65 | — | entry signal |
| 2026-09-30T10:35 | Donchian 55/20 | sell | ETH-USD | 4.32 | -0.01 | rebalance down |
| 2026-09-30T10:35 | Donchian 55/20 | sell | DOGE-USD | 4.32 | -0.01 | rebalance down |
| 2026-09-30T10:35 | ROC + volume | buy | ETH-USD | 4.34 | — | rebalance up |
| 2026-09-30T10:35 | ROC + volume | sell | XRP-USD | 17.22 | -0.11 | exit signal |
| 2026-09-30T10:30 | Consensus | buy | ETH-USD | 19.17 | — | entry |
| 2026-09-30T10:30 | Heikin-Ashi | buy | SOL-USD | 17.08 | — | entry signal |
| 2026-09-30T10:30 | Heikin-Ashi | buy | ETH-USD | 17.08 | — | entry signal |
| 2026-09-30T10:30 | Heikin-Ashi | buy | DOGE-USD | 17.08 | — | entry signal |
| 2026-09-30T10:30 | Heikin-Ashi | buy | BTC-USD | 17.08 | — | entry signal |
| 2026-09-30T10:25 | Agent (ML meta-label) | sell | XRP-USD | 5.31 | -0.02 | selected signal exited |
| 2026-09-30T10:25 | Connors RSI(2) | sell | XRP-USD | 19.15 | -0.09 | exit signal |
| 2026-09-30T10:25 | Volume breakout | buy | DOGE-USD | 21.56 | — | entry signal |
| 2026-09-30T10:25 | Parabolic SAR | buy | DOGE-USD | 17.75 | — | entry signal |
| 2026-09-30T10:20 | Agent (ML meta-label) | buy | XRP-USD | 5.34 | — | entry |
| 2026-09-30T10:20 | Consensus | sell | ETH-USD | 19.10 | -0.11 | target is flat |
| 2026-09-30T10:20 | Donchian 20/10 | buy | BTC-USD | 3.96 | — | rebalance up |
| 2026-09-30T10:20 | Donchian 20/10 | sell | SOL-USD | 3.96 | -0.01 | rebalance down |
| 2026-09-30T10:20 | Heikin-Ashi | sell | BTC-USD | 17.13 | -0.02 | exit signal |
| 2026-09-30T10:20 | Parabolic SAR | sell | ETH-USD | 17.75 | -0.01 | exit signal |
| 2026-09-30T10:20 | MACD zero-line | sell | XRP-USD | 19.79 | -0.07 | exit signal |
| 2026-09-30T10:20 | MACD cross | buy | BTC-USD | 10.36 | — | rebalance up |
| 2026-09-30T10:20 | MACD cross | sell | XRP-USD | 13.79 | -0.01 | exit signal |
| 2026-09-30T10:15 | Connors RSI(2) | buy | XRP-USD | 19.24 | — | entry signal |
| 2026-09-30T10:15 | Volume breakout | sell | XRP-USD | 21.56 | -0.22 | exit signal |
| 2026-09-30T10:15 | Parabolic SAR | sell | XRP-USD | 17.70 | -0.05 | exit signal |
| 2026-09-30T10:10 | Donchian 20/10 | buy | BTC-USD | 3.98 | — | rebalance up |
| 2026-09-30T10:10 | Donchian 20/10 | sell | DOGE-USD | 3.98 | -0.01 | rebalance down |
| 2026-09-30T10:10 | RSI momentum | buy | XRP-USD | 3.88 | — | rebalance up |
| 2026-09-30T10:10 | Heikin-Ashi | sell | SOL-USD | 17.03 | -0.11 | exit signal |
| 2026-09-30T10:05 | Parabolic SAR | sell | DOGE-USD | 17.74 | -0.01 | exit signal |
| 2026-09-30T10:00 | Consensus | buy | ETH-USD | 19.21 | — | entry |
| 2026-09-30T10:00 | Consensus | buy | BTC-USD | 19.21 | — | entry |
| 2026-09-30T10:00 | Candlestick reversal · 1h | buy | ETH-USD | 6.01 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
