# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T11:10:05.000142+00:00 · 6812 ticks

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

Today: 8640 decisions in 1728 calls, $0.1209 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T11:10 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-09-30T11:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T11:10 | 0 / 5 / 0 | cash |  |

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
| 7 | Hold BTC | benchmark | 99.71 | -0.29 | 0 | — | 28.52 | 3.59 | -8.68 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Copy: Congress Democrats (NANC) | copy | 99.67 | -0.33 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 10 | Agent | meta | 99.60 | -0.40 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 11 | Agent (aggressive) | meta | 99.36 | -0.64 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.33 | -0.67 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 13 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 14 | Hold SPY | benchmark | 99.10 | -0.90 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.01 | -0.98 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 99.01 | -0.99 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 17 | VWAP reversion · 1h | reversion | 98.94 | -1.06 | 20 | 25.0 | -13.00 | -4.40 | -14.78 | 122 |
| 18 | RSI(14) reversion · 1h | reversion | 98.92 | -1.08 | 7 | 57.1 | 5.56 | 1.44 | -7.03 | 118 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 20 | Daily: Bullish score | daily | 98.67 | -1.33 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 21 | Z-score reversion · 1h | reversion | 98.59 | -1.41 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Copy: Insider buying | copy | 98.51 | -1.49 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Williams %R · 1h | reversion | 98.32 | -1.68 | 43 | 44.2 | -17.78 | -3.28 | -19.41 | 488 |
| 26 | Candlestick reversal · 1h | reversion | 98.15 | -1.85 | 27 | 22.2 | -26.82 | -6.71 | -27.46 | 491 |
| 27 | Stochastic reversion · 1h | reversion | 98.15 | -1.85 | 26 | 53.8 | -13.75 | -3.01 | -14.99 | 330 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.05 | -1.95 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | CCI reversion · 1h | reversion | 97.87 | -2.13 | 35 | 34.3 | 1.36 | 0.39 | -12.41 | 409 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.57 | -2.43 | 45 | 44.4 | -11.34 | -3.61 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.41 | -2.59 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.39 | -2.61 | 13 | 7.7 | 17.16 | 2.03 | -14.13 | 124 |
| 34 | Max aggression: 5-day momentum | meta | 97.31 | -2.69 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Squeeze breakout · 1h | breakout | 96.98 | -3.02 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 37 | Bollinger reversion · 1h | reversion | 96.90 | -3.10 | 22 | 27.3 | -17.44 | -4.85 | -18.06 | 312 |
| 38 | Max aggression: 1-day momentum | meta | 96.28 | -3.72 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Supertrend · 1h | trend | 96.27 | -3.73 | 18 | 5.6 | 2.04 | 0.48 | -16.43 | 194 |
| 40 | Daily: SMA 20/50 cross · AAPL | daily | 96.24 | -3.76 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 41 | Agent (ML meta-label) | meta | 96.01 | -3.99 | 142 | 12.7 | -0.08 | 0.15 | -13.12 | 402 |
| 42 | Trend pullback · 1h | trend | 95.99 | -4.01 | 28 | 10.7 | -29.22 | -7.18 | -29.64 | 148 |
| 43 | MACD cross · 1h | trend | 95.75 | -4.25 | 40 | 10.0 | -18.70 | -3.17 | -21.44 | 465 |
| 44 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 45 | Parabolic SAR · 1h | trend | 95.53 | -4.47 | 26 | 11.5 | -7.75 | -0.96 | -18.82 | 294 |
| 46 | Donchian 55/20 · 1h | breakout | 95.47 | -4.53 | 12 | 0.0 | 4.53 | 0.79 | -16.96 | 112 |
| 47 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.28 | -27.84 | -50.33 | 607 |
| 48 | MFI reversion · 1h | reversion | 95.12 | -4.88 | 44 | 13.6 | -9.68 | -1.77 | -17.20 | 129 |
| 49 | Ichimoku · 1h | trend | 94.99 | -5.01 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 51 | Bollinger breakout · 1h | breakout | 94.48 | -5.52 | 17 | 5.9 | 8.00 | 1.23 | -10.10 | 284 |
| 52 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.33 | 0.27 | -18.68 | 212 |
| 53 | RSI momentum · 1h | momentum | 94.01 | -5.99 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 54 | Donchian 20/10 · 1h | breakout | 93.99 | -6.01 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | Triple EMA stack · 1h | trend | 93.68 | -6.32 | 30 | 6.7 | -6.77 | -0.63 | -22.58 | 226 |
| 56 | ADX DI cross · 1h | trend | 93.66 | -6.34 | 30 | 6.7 | -15.90 | -2.94 | -17.73 | 254 |
| 57 | MACD zero-line · 1h | trend | 93.57 | -6.43 | 21 | 4.8 | -5.95 | -0.65 | -14.64 | 224 |
| 58 | VWAP momentum · 1h | momentum | 93.33 | -6.67 | 103 | 12.6 | -34.63 | -5.22 | -35.64 | 1241 |
| 59 | Heikin-Ashi · 1h | trend | 92.39 | -7.61 | 45 | 11.1 | -26.36 | -3.99 | -30.64 | 672 |
| 60 | EMA 9/21 cross · 1h | trend | 92.25 | -7.75 | 45 | 11.1 | -4.55 | -0.43 | -16.92 | 311 |
| 61 | OBV trend · 1h | momentum | 92.12 | -7.88 | 54 | 7.4 | -12.79 | -1.40 | -25.19 | 315 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.13 | -71.11 | 1470 |
| 63 | ROC + volume · 1h | momentum | 89.12 | -10.88 | 53 | 5.7 | -4.72 | -0.39 | -19.59 | 406 |
| 64 | Squeeze breakout | breakout | 88.51 | -11.49 | 99 | 14.1 | -59.93 | -18.65 | -59.93 | 1192 |
| 65 | Volume breakout | breakout | 86.47 | -13.53 | 107 | 15.0 | -62.02 | -20.01 | -62.02 | 898 |
| 66 | ROC + volume | momentum | 86.15 | -13.85 | 155 | 18.1 | -72.18 | -17.69 | -72.21 | 1630 |
| 67 | Donchian 55/20 | breakout | 85.93 | -14.07 | 101 | 14.9 | -67.76 | -15.53 | -67.86 | 1298 |
| 68 | Keltner breakout | breakout | 84.81 | -15.19 | 154 | 13.0 | -84.65 | -34.33 | -84.65 | 1893 |
| 69 | EMA 20/50 cross | trend | 84.25 | -15.75 | 135 | 14.8 | -79.03 | -17.70 | -79.10 | 1477 |
| 70 | Ichimoku | trend | 84.24 | -15.76 | 119 | 8.4 | -80.41 | -26.00 | -80.41 | 1742 |
| 71 | VWAP reversion | reversion | 83.90 | -16.10 | 145 | 22.1 | -71.74 | -17.62 | -72.04 | 1402 |
| 72 | Z-score reversion | reversion | 83.65 | -16.34 | 193 | 30.6 | -84.59 | -27.49 | -84.60 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.06 | -19.94 | 190 | 18.9 | -88.08 | -35.26 | -88.14 | 2146 |
| 76 | Supertrend | trend | 79.69 | -20.31 | 191 | 16.8 | -87.57 | -24.79 | -87.64 | 1961 |
| 77 | Donchian 20/10 | breakout | 79.47 | -20.53 | 213 | 16.9 | -90.78 | -29.51 | -90.80 | 2673 |
| 78 | MACD zero-line | trend | 79.28 | -20.72 | 220 | 15.0 | -91.87 | -36.09 | -91.87 | 2359 |
| 79 | Bollinger breakout | breakout | 78.85 | -21.15 | 219 | 15.5 | -93.86 | -42.23 | -93.86 | 2863 |
| 80 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.58 | -33.23 | -90.58 | 2259 |
| 81 | Triple EMA stack | trend | 77.99 | -22.01 | 226 | 14.6 | -93.07 | -36.04 | -93.09 | 2620 |
| 82 | RSI momentum | momentum | 77.62 | -22.38 | 209 | 12.4 | -90.42 | -29.15 | -90.46 | 2380 |
| 83 | ADX DI cross | trend | 77.28 | -22.71 | 210 | 7.6 | -89.50 | -46.08 | -89.50 | 2115 |
| 84 | Connors RSI(2) | reversion | 76.59 | -23.41 | 244 | 16.8 | -96.28 | -39.05 | -96.28 | 3603 |
| 85 | Consensus | meta | 76.35 | -23.65 | 193 | 7.3 | -94.56 | -29.74 | -94.57 | 2643 |
| 86 | Stochastic reversion | reversion | 74.89 | -25.11 | 343 | 23.3 | -95.91 | -44.60 | -95.93 | 4055 |
| 87 | Candlestick reversal | reversion | 73.85 | -26.15 | 296 | 12.2 | -99.36 | -49.50 | -99.36 | 5594 |
| 88 | EMA 9/21 cross | trend | 73.51 | -26.49 | 301 | 15.9 | -97.45 | -41.79 | -97.47 | 3540 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.78 | -43.24 | -95.79 | 3684 |
| 90 | OBV trend | momentum | 71.93 | -28.07 | 293 | 14.3 | -95.89 | -48.40 | -95.89 | 3546 |
| 91 | CCI reversion | reversion | 70.95 | -29.05 | 264 | 10.6 | -98.46 | -49.30 | -98.46 | 4699 |
| 92 | Parabolic SAR | trend | 70.76 | -29.24 | 286 | 12.2 | -96.96 | -54.47 | -96.96 | 3625 |
| 93 | MACD cross | trend | 69.13 | -30.87 | 300 | 13.3 | -99.72 | -64.27 | -99.72 | 6076 |
| 94 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.57 | -36.46 | -98.57 | 5245 |
| 95 | Williams %R | reversion | 68.53 | -31.46 | 371 | 19.7 | -99.52 | -56.95 | -99.52 | 6107 |
| 96 | Heikin-Ashi | trend | 67.83 | -32.17 | 263 | 3.0 | -99.90 | -79.43 | -99.90 | 8300 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T11:10 | Connors RSI(2) | buy | SOL-USD | 19.16 | — | entry signal |
| 2026-09-30T11:10 | Keltner breakout | sell | SOL-USD | 21.16 | -0.18 | stop-loss |
| 2026-09-30T11:10 | Donchian 55/20 | buy | ETH-USD | 4.30 | — | rebalance up |
| 2026-09-30T11:10 | Donchian 55/20 | sell | SOL-USD | 8.55 | -0.09 | stop-loss |
| 2026-09-30T11:10 | OBV trend | sell | SOL-USD | 17.93 | -0.13 | exit signal |
| 2026-09-30T11:10 | OBV trend | sell | ETH-USD | 17.97 | -0.07 | exit signal |
| 2026-09-30T11:10 | ROC + volume | sell | SOL-USD | 21.48 | -0.19 | exit signal |
| 2026-09-30T11:10 | ROC + volume | sell | ETH-USD | 21.50 | -0.18 | exit signal |
| 2026-09-30T11:10 | ROC + volume | sell | BTC-USD | 17.23 | -0.11 | stop-loss |
| 2026-09-30T11:10 | Heikin-Ashi | sell | DOGE-USD | 13.60 | -0.04 | exit signal |
| 2026-09-30T11:10 | Parabolic SAR | sell | XRP-USD | 17.58 | -0.18 | exit signal |
| 2026-09-30T11:05 | Agent (ML meta-label) | sell | XRP-USD | 5.29 | -0.04 | selected signal exited |
| 2026-09-30T11:05 | Consensus | sell | SOL-USD | 19.00 | -0.17 | target is flat |
| 2026-09-30T11:05 | Consensus | sell | BTC-USD | 19.11 | -0.09 | target is flat |
| 2026-09-30T11:05 | Connors RSI(2) | buy | XRP-USD | 19.22 | — | entry signal |
| 2026-09-30T11:05 | Connors RSI(2) | buy | ETH-USD | 19.22 | — | entry signal |
| 2026-09-30T11:05 | Connors RSI(2) | buy | BTC-USD | 19.22 | — | entry signal |
| 2026-09-30T11:05 | Volume breakout | sell | SOL-USD | 21.63 | -0.15 | exit signal |
| 2026-09-30T11:05 | Volume breakout | sell | ETH-USD | 21.62 | -0.16 | exit signal |
| 2026-09-30T11:05 | Volume breakout | sell | BTC-USD | 21.66 | -0.12 | exit signal |
| 2026-09-30T11:05 | Keltner breakout | buy | SOL-USD | 4.29 | — | rebalance up |
| 2026-09-30T11:05 | Keltner breakout | sell | XRP-USD | 16.91 | -0.10 | exit signal |
| 2026-09-30T11:05 | Keltner breakout | sell | ETH-USD | 16.95 | -0.07 | exit signal |
| 2026-09-30T11:05 | Keltner breakout | sell | BTC-USD | 16.96 | -0.09 | stop-loss |
| 2026-09-30T11:05 | Bollinger breakout | sell | XRP-USD | 15.73 | -0.07 | exit signal |
| 2026-09-30T11:05 | Bollinger breakout | sell | SOL-USD | 15.75 | -0.04 | exit signal |
| 2026-09-30T11:05 | Bollinger breakout | sell | ETH-USD | 15.74 | -0.07 | exit signal |
| 2026-09-30T11:05 | Bollinger breakout | sell | BTC-USD | 15.75 | -0.09 | stop-loss |
| 2026-09-30T11:05 | OBV trend | buy | SOL-USD | 10.79 | — | rebalance up |
| 2026-09-30T11:05 | OBV trend | buy | ETH-USD | 3.63 | — | rebalance up |
| 2026-09-30T11:05 | OBV trend | sell | XRP-USD | 17.93 | -0.11 | exit signal |
| 2026-09-30T11:05 | ROC + volume | buy | SOL-USD | 4.33 | — | rebalance up |
| 2026-09-30T11:05 | Heikin-Ashi | sell | SOL-USD | 13.57 | -0.09 | exit signal |
| 2026-09-30T11:05 | Heikin-Ashi | sell | BTC-USD | 13.57 | -0.09 | exit signal |
| 2026-09-30T11:05 | Parabolic SAR | sell | BTC-USD | 17.71 | -0.02 | exit signal |
| 2026-09-30T11:05 | MACD zero-line | sell | SOL-USD | 19.82 | -0.02 | exit signal |
| 2026-09-30T11:05 | MACD zero-line | sell | BTC-USD | 19.81 | -0.04 | exit signal |
| 2026-09-30T11:05 | MACD cross | sell | SOL-USD | 13.85 | 0.05 | exit signal |
| 2026-09-30T11:05 | MACD cross | sell | BTC-USD | 17.26 | -0.06 | exit signal |
| 2026-09-30T11:00 | Agent (ML meta-label) | buy | XRP-USD | 5.34 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
