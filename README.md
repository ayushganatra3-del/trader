# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T11:40:05.000115+00:00 · 6835 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.58 (-0.42%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.92 | -0.07 |

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

Today: 8985 decisions in 1797 calls, $0.1257 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T11:40 | 2 / 3 / 0 | DOGE-USD 21%, XRP-USD 19% |  |
| Breezy | 2026-09-30T11:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T11:40 | 4 / 1 / 0 | DOGE-USD 38%, XRP-USD 37% |  |

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
| 7 | Hold BTC | benchmark | 99.85 | -0.15 | 0 | — | 29.13 | 3.66 | -8.68 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Agent | meta | 99.58 | -0.42 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 10 | Copy: Congress Democrats (NANC) | copy | 99.56 | -0.44 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 11 | Agent (aggressive) | meta | 99.31 | -0.69 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.22 | -0.78 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 13 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 14 | Hold SPY | benchmark | 98.99 | -1.01 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 98.91 | -1.09 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 98.90 | -1.10 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 17 | RSI(14) reversion · 1h | reversion | 98.89 | -1.11 | 7 | 57.1 | 5.60 | 1.45 | -7.03 | 118 |
| 18 | VWAP reversion · 1h | reversion | 98.89 | -1.11 | 20 | 25.0 | -13.02 | -4.40 | -14.79 | 122 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 20 | Daily: Bullish score | daily | 98.56 | -1.44 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 21 | Z-score reversion · 1h | reversion | 98.51 | -1.49 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 23 | Copy: Insider buying | copy | 98.42 | -1.58 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Williams %R · 1h | reversion | 98.24 | -1.76 | 43 | 44.2 | -17.68 | -3.26 | -19.41 | 488 |
| 26 | Candlestick reversal · 1h | reversion | 98.09 | -1.91 | 27 | 22.2 | -27.08 | -6.75 | -27.74 | 492 |
| 27 | Stochastic reversion · 1h | reversion | 98.04 | -1.96 | 26 | 53.8 | -13.69 | -2.99 | -14.94 | 330 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 97.95 | -2.05 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 30 | CCI reversion · 1h | reversion | 97.76 | -2.24 | 35 | 34.3 | 1.37 | 0.39 | -12.41 | 409 |
| 31 | Connors RSI(2) · 1h | reversion | 97.49 | -2.51 | 45 | 44.4 | -11.34 | -3.61 | -11.74 | 234 |
| 32 | EMA 20/50 cross · 1h | trend | 97.32 | -2.68 | 13 | 7.7 | 17.16 | 2.03 | -14.13 | 124 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 97.30 | -2.70 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 34 | Max aggression: 5-day momentum | meta | 97.21 | -2.79 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Squeeze breakout · 1h | breakout | 96.95 | -3.05 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 37 | Bollinger reversion · 1h | reversion | 96.79 | -3.21 | 22 | 27.3 | -17.44 | -4.85 | -18.06 | 312 |
| 38 | Supertrend · 1h | trend | 96.22 | -3.78 | 18 | 5.6 | 2.09 | 0.48 | -16.43 | 194 |
| 39 | Max aggression: 1-day momentum | meta | 96.18 | -3.82 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 40 | Daily: SMA 20/50 cross · AAPL | daily | 96.14 | -3.86 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 41 | Agent (ML meta-label) | meta | 95.93 | -4.07 | 143 | 12.6 | 1.47 | 0.42 | -11.05 | 381 |
| 42 | Trend pullback · 1h | trend | 95.92 | -4.08 | 28 | 10.7 | -29.22 | -7.18 | -29.64 | 148 |
| 43 | MACD cross · 1h | trend | 95.64 | -4.36 | 40 | 10.0 | -18.52 | -3.13 | -21.44 | 465 |
| 44 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 45 | Parabolic SAR · 1h | trend | 95.43 | -4.57 | 26 | 11.5 | -7.63 | -0.94 | -18.82 | 294 |
| 46 | Donchian 55/20 · 1h | breakout | 95.37 | -4.63 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 47 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.28 | -27.84 | -50.33 | 607 |
| 48 | MFI reversion · 1h | reversion | 95.06 | -4.94 | 44 | 13.6 | -9.54 | -1.74 | -17.20 | 129 |
| 49 | Ichimoku · 1h | trend | 94.94 | -5.06 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 51 | Bollinger breakout · 1h | breakout | 94.56 | -5.44 | 17 | 5.9 | 8.20 | 1.25 | -10.10 | 284 |
| 52 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | -0.05 | 0.22 | -18.68 | 214 |
| 53 | Donchian 20/10 · 1h | breakout | 93.97 | -6.03 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 54 | RSI momentum · 1h | momentum | 93.94 | -6.07 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 55 | Triple EMA stack · 1h | trend | 93.63 | -6.37 | 30 | 6.7 | -6.77 | -0.63 | -22.58 | 226 |
| 56 | MACD zero-line · 1h | trend | 93.63 | -6.37 | 21 | 4.8 | -5.84 | -0.63 | -14.64 | 224 |
| 57 | ADX DI cross · 1h | trend | 93.56 | -6.44 | 30 | 6.7 | -15.90 | -2.94 | -17.73 | 254 |
| 58 | VWAP momentum · 1h | momentum | 93.22 | -6.78 | 103 | 12.6 | -34.54 | -5.20 | -35.64 | 1241 |
| 59 | Heikin-Ashi · 1h | trend | 92.41 | -7.59 | 45 | 11.1 | -26.29 | -3.98 | -30.65 | 672 |
| 60 | EMA 9/21 cross · 1h | trend | 92.31 | -7.69 | 45 | 11.1 | -4.40 | -0.41 | -16.92 | 311 |
| 61 | OBV trend · 1h | momentum | 92.02 | -7.98 | 54 | 7.4 | -12.79 | -1.40 | -25.19 | 315 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.13 | -71.11 | 1470 |
| 63 | ROC + volume · 1h | momentum | 89.21 | -10.79 | 53 | 5.7 | -4.60 | -0.38 | -19.59 | 406 |
| 64 | Squeeze breakout | breakout | 88.51 | -11.49 | 99 | 14.1 | -59.96 | -18.66 | -59.96 | 1192 |
| 65 | Volume breakout | breakout | 86.56 | -13.44 | 107 | 15.0 | -61.97 | -19.97 | -62.02 | 898 |
| 66 | ROC + volume | momentum | 86.22 | -13.78 | 155 | 18.1 | -72.14 | -17.67 | -72.21 | 1630 |
| 67 | Donchian 55/20 | breakout | 86.17 | -13.83 | 101 | 14.9 | -67.62 | -15.46 | -67.86 | 1298 |
| 68 | Keltner breakout | breakout | 84.88 | -15.12 | 154 | 13.0 | -84.65 | -34.26 | -84.67 | 1893 |
| 69 | EMA 20/50 cross | trend | 84.48 | -15.52 | 135 | 14.8 | -78.91 | -17.63 | -79.06 | 1476 |
| 70 | Ichimoku | trend | 84.28 | -15.72 | 120 | 8.3 | -80.42 | -26.01 | -80.45 | 1743 |
| 71 | VWAP reversion | reversion | 83.90 | -16.10 | 145 | 22.1 | -71.74 | -17.62 | -72.04 | 1402 |
| 72 | Z-score reversion | reversion | 83.65 | -16.34 | 193 | 30.6 | -84.59 | -27.49 | -84.60 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.06 | -19.94 | 190 | 18.9 | -88.08 | -35.26 | -88.14 | 2146 |
| 76 | Supertrend | trend | 79.92 | -20.08 | 191 | 16.8 | -87.46 | -24.63 | -87.58 | 1959 |
| 77 | Donchian 20/10 | breakout | 79.71 | -20.29 | 213 | 16.9 | -90.74 | -29.40 | -90.80 | 2673 |
| 78 | MACD zero-line | trend | 79.28 | -20.72 | 220 | 15.0 | -91.87 | -36.09 | -91.87 | 2359 |
| 79 | Bollinger breakout | breakout | 78.85 | -21.15 | 219 | 15.5 | -93.84 | -42.17 | -93.85 | 2863 |
| 80 | Trend pullback | trend | 78.49 | -21.51 | 174 | 16.7 | -90.59 | -33.27 | -90.62 | 2263 |
| 81 | Triple EMA stack | trend | 78.21 | -21.79 | 226 | 14.6 | -93.05 | -35.90 | -93.10 | 2619 |
| 82 | RSI momentum | momentum | 77.84 | -22.16 | 209 | 12.4 | -90.36 | -29.00 | -90.44 | 2379 |
| 83 | ADX DI cross | trend | 77.29 | -22.71 | 210 | 7.6 | -89.34 | -44.58 | -89.39 | 2108 |
| 84 | Connors RSI(2) | reversion | 76.46 | -23.54 | 248 | 16.5 | -96.28 | -39.09 | -96.28 | 3602 |
| 85 | Consensus | meta | 76.35 | -23.65 | 193 | 7.3 | -94.56 | -29.75 | -94.56 | 2643 |
| 86 | Stochastic reversion | reversion | 74.89 | -25.11 | 343 | 23.3 | -95.91 | -44.60 | -95.93 | 4055 |
| 87 | Candlestick reversal | reversion | 73.85 | -26.15 | 296 | 12.2 | -99.36 | -49.47 | -99.36 | 5593 |
| 88 | EMA 9/21 cross | trend | 73.73 | -26.27 | 301 | 15.9 | -97.44 | -41.65 | -97.47 | 3540 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.78 | -43.24 | -95.79 | 3684 |
| 90 | OBV trend | momentum | 71.99 | -28.01 | 293 | 14.3 | -95.89 | -48.33 | -95.89 | 3546 |
| 91 | CCI reversion | reversion | 70.86 | -29.14 | 266 | 10.5 | -98.46 | -49.37 | -98.46 | 4701 |
| 92 | Parabolic SAR | trend | 70.52 | -29.48 | 287 | 12.2 | -96.97 | -54.73 | -96.97 | 3629 |
| 93 | MACD cross | trend | 68.90 | -31.10 | 302 | 13.6 | -99.72 | -64.74 | -99.72 | 6079 |
| 94 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.55 | -36.38 | -98.57 | 5244 |
| 95 | Williams %R | reversion | 68.46 | -31.54 | 372 | 19.6 | -99.52 | -57.01 | -99.52 | 6109 |
| 96 | Heikin-Ashi | trend | 67.83 | -32.17 | 263 | 3.0 | -99.90 | -79.43 | -99.90 | 8300 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T11:40 | CCI reversion | sell | XRP-USD | 17.69 | -0.05 | exit signal |
| 2026-09-30T11:40 | CCI reversion | sell | ETH-USD | 17.69 | -0.05 | exit signal |
| 2026-09-30T11:40 | Williams %R | sell | XRP-USD | 17.09 | -0.04 | exit signal |
| 2026-09-30T11:40 | Bollinger breakout | buy | ETH-USD | 19.73 | — | entry signal |
| 2026-09-30T11:40 | Parabolic SAR | buy | XRP-USD | 17.67 | — | entry signal |
| 2026-09-30T11:40 | Parabolic SAR | buy | ETH-USD | 17.67 | — | entry signal |
| 2026-09-30T11:40 | Parabolic SAR | buy | BTC-USD | 17.67 | — | entry signal |
| 2026-09-30T11:40 | MACD cross | buy | DOGE-USD | 17.24 | — | entry signal |
| 2026-09-30T11:35 | Ichimoku | sell | XRP-USD | 21.04 | -0.05 | exit signal |
| 2026-09-30T11:30 | Agent (ML meta-label) | sell | DOGE-USD | 1.98 | -0.01 | selected signal exited |
| 2026-09-30T11:30 | MACD cross | sell | DOGE-USD | 17.15 | -0.12 | exit signal |
| 2026-09-30T11:25 | Connors RSI(2) | sell | XRP-USD | 19.12 | -0.09 | exit signal |
| 2026-09-30T11:25 | Connors RSI(2) | sell | SOL-USD | 19.07 | -0.09 | exit signal |
| 2026-09-30T11:25 | Connors RSI(2) | sell | ETH-USD | 19.11 | -0.11 | exit signal |
| 2026-09-30T11:25 | OBV trend | buy | ETH-USD | 17.99 | — | entry signal |
| 2026-09-30T11:25 | Parabolic SAR | buy | DOGE-USD | 17.67 | — | entry signal |
| 2026-09-30T11:25 | MACD cross | buy | DOGE-USD | 17.27 | — | entry signal |
| 2026-09-30T11:20 | MACD cross | sell | DOGE-USD | 13.84 | 0.09 | exit signal |
| 2026-09-30T11:16 | Agent (ML meta-label) | buy | DOGE-USD | 1.98 | — | entry |
| 2026-09-30T11:16 | CCI reversion | buy | XRP-USD | 17.74 | — | entry signal |
| 2026-09-30T11:16 | CCI reversion | buy | ETH-USD | 17.74 | — | entry signal |
| 2026-09-30T11:16 | Williams %R | buy | XRP-USD | 17.13 | — | entry signal |
| 2026-09-30T11:16 | Williams %R | buy | SOL-USD | 17.13 | — | entry signal |
| 2026-09-30T11:16 | Connors RSI(2) | sell | BTC-USD | 19.10 | -0.11 | exit signal |
| 2026-09-30T11:16 | Trend pullback | buy | XRP-USD | 19.64 | — | entry signal |
| 2026-09-30T11:16 | Trend pullback | buy | SOL-USD | 19.64 | — | entry signal |
| 2026-09-30T11:16 | Trend pullback | buy | ETH-USD | 19.64 | — | entry signal |
| 2026-09-30T11:16 | Trend pullback | buy | BTC-USD | 19.64 | — | entry signal |
| 2026-09-30T11:16 | ADX DI cross | buy | XRP-USD | 19.32 | — | entry signal |
| 2026-09-30T11:16 | Parabolic SAR | sell | DOGE-USD | 17.68 | -0.07 | exit signal |
| 2026-09-30T11:11 | Agent (ML meta-label) | buy | XRP-USD | 5.64 | — | entry |
| 2026-09-30T11:10 | Connors RSI(2) | buy | SOL-USD | 19.16 | — | entry signal |
| 2026-09-30T11:10 | Keltner breakout | sell | SOL-USD | 21.16 | -0.18 | stop-loss |
| 2026-09-30T11:10 | Donchian 55/20 | buy | ETH-USD | 4.30 | — | rebalance up |
| 2026-09-30T11:10 | Donchian 55/20 | sell | SOL-USD | 8.55 | -0.09 | stop-loss |
| 2026-09-30T11:10 | OBV trend | sell | SOL-USD | 17.93 | -0.13 | exit signal |
| 2026-09-30T11:10 | OBV trend | sell | ETH-USD | 17.97 | -0.07 | exit signal |
| 2026-09-30T11:10 | ROC + volume | sell | SOL-USD | 21.48 | -0.19 | exit signal |
| 2026-09-30T11:10 | ROC + volume | sell | ETH-USD | 21.50 | -0.18 | exit signal |
| 2026-09-30T11:10 | ROC + volume | sell | BTC-USD | 17.23 | -0.11 | stop-loss |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
