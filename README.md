# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T13:10:05.000185+00:00 · 6909 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.59 (-0.41%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.93 | -0.06 |

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

Today: 10095 decisions in 2019 calls, $0.1412 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T13:10 | 2 / 3 / 0 | SOL-USD 20%, BTC-USD 16% |  |
| Breezy | 2026-09-30T13:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T13:10 | 5 / 0 / 0 | SOL-USD 42%, ETH-USD 39% |  |

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
| 1 | Hold BTC | benchmark | 101.92 | 1.92 | 0 | — | 31.92 | 3.93 | -8.68 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.02 | 1.02 | 2 | 50.0 | 13.82 | 2.99 | -7.55 | 43 |
| 3 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | 0.64 | 0.29 | -9.74 | 24 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.65 | -7.93 | 7 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Copy: Congress Democrats (NANC) | copy | 99.63 | -0.38 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 10 | Agent | meta | 99.59 | -0.41 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 11 | Agent (aggressive) | meta | 99.34 | -0.66 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.29 | -0.71 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 13 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 14 | Hold SPY | benchmark | 99.06 | -0.94 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 98.97 | -1.03 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 98.97 | -1.03 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 17 | VWAP reversion · 1h | reversion | 98.92 | -1.08 | 20 | 25.0 | -12.87 | -4.37 | -14.65 | 121 |
| 18 | RSI(14) reversion · 1h | reversion | 98.91 | -1.09 | 7 | 57.1 | 4.01 | 1.06 | -7.03 | 122 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 20 | Daily: Bullish score | daily | 98.62 | -1.38 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 21 | Z-score reversion · 1h | reversion | 98.56 | -1.44 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Copy: Insider buying | copy | 98.48 | -1.52 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Williams %R · 1h | reversion | 98.29 | -1.71 | 43 | 44.2 | -18.11 | -3.33 | -19.72 | 488 |
| 26 | Candlestick reversal · 1h | reversion | 98.19 | -1.81 | 28 | 25.0 | -26.56 | -6.64 | -27.27 | 489 |
| 27 | Stochastic reversion · 1h | reversion | 98.11 | -1.89 | 26 | 53.8 | -12.39 | -2.76 | -13.65 | 327 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.01 | -1.99 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 30 | CCI reversion · 1h | reversion | 97.83 | -2.17 | 35 | 34.3 | 1.25 | 0.38 | -12.41 | 409 |
| 31 | Connors RSI(2) · 1h | reversion | 97.54 | -2.46 | 45 | 44.4 | -11.29 | -3.59 | -11.74 | 233 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.37 | -2.63 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.35 | -2.65 | 13 | 7.7 | 17.26 | 2.04 | -14.13 | 128 |
| 34 | Max aggression: 5-day momentum | meta | 97.27 | -2.73 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Squeeze breakout · 1h | breakout | 96.99 | -3.01 | 9 | 11.1 | 15.58 | 2.73 | -5.11 | 97 |
| 37 | Bollinger reversion · 1h | reversion | 96.85 | -3.15 | 22 | 27.3 | -17.59 | -4.88 | -18.21 | 312 |
| 38 | Supertrend · 1h | trend | 96.60 | -3.40 | 18 | 5.6 | 2.45 | 0.53 | -16.43 | 197 |
| 39 | Max aggression: 1-day momentum | meta | 96.24 | -3.76 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 40 | Daily: SMA 20/50 cross · AAPL | daily | 96.20 | -3.80 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 41 | Agent (ML meta-label) | meta | 96.16 | -3.84 | 145 | 12.4 | 0.97 | 0.33 | -13.42 | 404 |
| 42 | Trend pullback · 1h | trend | 95.96 | -4.04 | 28 | 10.7 | -29.21 | -7.18 | -29.64 | 148 |
| 43 | MACD cross · 1h | trend | 95.71 | -4.29 | 40 | 10.0 | -17.12 | -2.86 | -21.03 | 463 |
| 44 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 45 | Bollinger breakout · 1h | breakout | 95.52 | -4.48 | 17 | 5.9 | 9.50 | 1.41 | -10.10 | 287 |
| 46 | Parabolic SAR · 1h | trend | 95.49 | -4.51 | 26 | 11.5 | -6.93 | -0.83 | -18.82 | 295 |
| 47 | MFI reversion · 1h | reversion | 95.46 | -4.54 | 44 | 13.6 | -8.89 | -1.59 | -17.20 | 129 |
| 48 | Three white soldiers | momentum | 95.44 | -4.56 | 44 | 18.2 | -49.92 | -27.18 | -50.14 | 607 |
| 49 | Donchian 55/20 · 1h | breakout | 95.43 | -4.57 | 12 | 0.0 | 4.56 | 0.80 | -16.96 | 115 |
| 50 | Ichimoku · 1h | trend | 95.36 | -4.63 | 16 | 18.8 | 7.42 | 1.05 | -15.13 | 125 |
| 51 | MACD zero-line · 1h | trend | 94.89 | -5.11 | 21 | 4.8 | -4.61 | -0.45 | -14.79 | 228 |
| 52 | Volume breakout · 1h | breakout | 94.73 | -5.27 | 27 | 3.7 | 5.90 | 0.99 | -12.60 | 126 |
| 53 | Donchian 20/10 · 1h | breakout | 94.35 | -5.65 | 16 | 12.5 | 7.38 | 1.13 | -12.78 | 218 |
| 54 | RSI momentum · 1h | momentum | 94.30 | -5.70 | 24 | 4.2 | 1.98 | 0.47 | -15.29 | 212 |
| 55 | Keltner breakout · 1h | breakout | 94.07 | -5.93 | 10 | 0.0 | 0.38 | 0.28 | -18.68 | 216 |
| 56 | Triple EMA stack · 1h | trend | 93.63 | -6.37 | 30 | 6.7 | -6.74 | -0.62 | -22.58 | 227 |
| 57 | ADX DI cross · 1h | trend | 93.62 | -6.38 | 30 | 6.7 | -15.61 | -2.88 | -17.71 | 252 |
| 58 | VWAP momentum · 1h | momentum | 93.29 | -6.71 | 103 | 12.6 | -34.10 | -5.11 | -35.64 | 1241 |
| 59 | Heikin-Ashi · 1h | trend | 93.19 | -6.81 | 45 | 11.1 | -25.48 | -3.81 | -30.82 | 676 |
| 60 | EMA 9/21 cross · 1h | trend | 93.13 | -6.88 | 45 | 11.1 | -3.64 | -0.30 | -16.92 | 314 |
| 61 | OBV trend · 1h | momentum | 92.08 | -7.92 | 54 | 7.4 | -12.71 | -1.39 | -25.19 | 319 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.05 | -21.16 | -71.11 | 1471 |
| 63 | ROC + volume · 1h | momentum | 89.68 | -10.31 | 53 | 5.7 | -4.10 | -0.31 | -19.59 | 410 |
| 64 | Squeeze breakout | breakout | 88.71 | -11.29 | 100 | 14.0 | -59.55 | -18.48 | -59.81 | 1192 |
| 65 | Donchian 55/20 | breakout | 87.68 | -12.32 | 101 | 14.9 | -67.06 | -15.07 | -67.86 | 1299 |
| 66 | ROC + volume | momentum | 86.98 | -13.02 | 155 | 18.1 | -71.90 | -17.49 | -72.21 | 1634 |
| 67 | Volume breakout | breakout | 86.91 | -13.09 | 108 | 15.7 | -61.38 | -19.41 | -61.99 | 898 |
| 68 | EMA 20/50 cross | trend | 86.12 | -13.88 | 135 | 14.8 | -78.57 | -17.38 | -79.12 | 1478 |
| 69 | Keltner breakout | breakout | 85.53 | -14.47 | 155 | 12.9 | -84.31 | -33.31 | -84.48 | 1892 |
| 70 | Ichimoku | trend | 83.97 | -16.03 | 124 | 8.1 | -80.46 | -26.07 | -80.52 | 1746 |
| 71 | VWAP reversion | reversion | 83.90 | -16.10 | 145 | 22.1 | -71.64 | -17.54 | -71.95 | 1400 |
| 72 | Z-score reversion | reversion | 83.65 | -16.34 | 193 | 30.6 | -84.59 | -27.49 | -84.60 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 81.48 | -18.52 | 191 | 16.8 | -87.23 | -24.20 | -87.58 | 1959 |
| 76 | Donchian 20/10 | breakout | 81.03 | -18.97 | 214 | 16.8 | -90.49 | -28.58 | -90.69 | 2669 |
| 77 | MFI reversion | reversion | 80.06 | -19.94 | 190 | 18.9 | -88.09 | -35.26 | -88.14 | 2146 |
| 78 | Triple EMA stack | trend | 79.72 | -20.28 | 226 | 14.6 | -92.87 | -34.79 | -93.05 | 2616 |
| 79 | Bollinger breakout | breakout | 79.36 | -20.64 | 221 | 15.4 | -93.75 | -41.56 | -93.82 | 2864 |
| 80 | MACD zero-line | trend | 79.28 | -20.72 | 220 | 15.0 | -91.87 | -36.10 | -91.87 | 2359 |
| 81 | RSI momentum | momentum | 79.11 | -20.89 | 210 | 12.4 | -90.17 | -28.41 | -90.42 | 2378 |
| 82 | Trend pullback | trend | 78.91 | -21.09 | 180 | 18.9 | -90.54 | -33.05 | -90.62 | 2265 |
| 83 | ADX DI cross | trend | 77.41 | -22.59 | 211 | 7.6 | -89.31 | -44.38 | -89.41 | 2109 |
| 84 | Consensus | meta | 76.79 | -23.20 | 195 | 7.2 | -94.50 | -29.39 | -94.56 | 2646 |
| 85 | Connors RSI(2) | reversion | 76.46 | -23.54 | 248 | 16.5 | -96.28 | -39.09 | -96.28 | 3603 |
| 86 | EMA 9/21 cross | trend | 75.15 | -24.85 | 301 | 15.9 | -97.37 | -40.48 | -97.45 | 3536 |
| 87 | Stochastic reversion | reversion | 74.89 | -25.11 | 343 | 23.3 | -95.89 | -44.13 | -95.93 | 4051 |
| 88 | Candlestick reversal | reversion | 73.85 | -26.15 | 296 | 12.2 | -99.36 | -49.51 | -99.37 | 5592 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.77 | -42.92 | -95.79 | 3680 |
| 90 | OBV trend | momentum | 72.78 | -27.22 | 296 | 14.2 | -95.83 | -47.60 | -95.90 | 3549 |
| 91 | Parabolic SAR | trend | 71.16 | -28.84 | 290 | 12.1 | -96.93 | -53.83 | -96.97 | 3630 |
| 92 | CCI reversion | reversion | 70.86 | -29.14 | 266 | 10.5 | -98.45 | -49.09 | -98.46 | 4696 |
| 93 | MACD cross | trend | 69.25 | -30.75 | 304 | 13.5 | -99.71 | -63.80 | -99.72 | 6080 |
| 94 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.50 | -35.90 | -98.54 | 5238 |
| 95 | Williams %R | reversion | 68.55 | -31.45 | 374 | 19.8 | -99.52 | -56.57 | -99.52 | 6106 |
| 96 | Heikin-Ashi | trend | 67.37 | -32.63 | 269 | 3.0 | -99.89 | -78.75 | -99.89 | 8299 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T13:10 | Ichimoku | buy | XRP-USD | 21.01 | — | entry signal |
| 2026-09-30T13:05 | Heikin-Ashi | sell | XRP-USD | 13.39 | -0.09 | exit signal |
| 2026-09-30T13:05 | Heikin-Ashi | sell | ETH-USD | 13.42 | -0.06 | exit signal |
| 2026-09-30T13:05 | Heikin-Ashi | sell | DOGE-USD | 13.38 | -0.10 | exit signal |
| 2026-09-30T13:05 | EMA 9/21 cross | buy | BTC-USD | 3.77 | — | rebalance up |
| 2026-09-30T13:05 | EMA 9/21 cross | sell | SOL-USD | 3.77 | 0.08 | rebalance down |
| 2026-09-30T13:00 | Agent (ML meta-label) | buy | BTC-USD | 2.54 | — | entry |
| 2026-09-30T13:00 | Candlestick reversal · 1h | sell | ETH-USD | 6.07 | 0.05 | exit signal |
| 2026-09-30T13:00 | Volume breakout · 1h | buy | BTC-USD | 23.68 | — | entry signal |
| 2026-09-30T13:00 | Squeeze breakout · 1h | buy | SOL-USD | 14.70 | — | entry signal |
| 2026-09-30T13:00 | Squeeze breakout · 1h | buy | ETH-USD | 19.39 | — | entry signal |
| 2026-09-30T13:00 | Squeeze breakout · 1h | buy | DOGE-USD | 19.39 | — | entry signal |
| 2026-09-30T13:00 | Squeeze breakout · 1h | buy | BTC-USD | 19.39 | — | entry signal |
| 2026-09-30T13:00 | Keltner breakout · 1h | buy | SOL-USD | 23.51 | — | entry signal |
| 2026-09-30T13:00 | Keltner breakout · 1h | buy | ETH-USD | 23.51 | — | entry signal |
| 2026-09-30T13:00 | Keltner breakout · 1h | buy | DOGE-USD | 23.51 | — | entry signal |
| 2026-09-30T13:00 | Keltner breakout · 1h | buy | BTC-USD | 23.51 | — | entry signal |
| 2026-09-30T13:00 | Bollinger breakout · 1h | buy | ETH-USD | 15.91 | — | entry signal |
| 2026-09-30T13:00 | Bollinger breakout · 1h | sell | DOGE-USD | 8.15 | 0.11 | rebalance down |
| 2026-09-30T13:00 | Bollinger breakout · 1h | sell | BTC-USD | 8.05 | 0.08 | rebalance down |
| 2026-09-30T13:00 | Donchian 20/10 · 1h | buy | XRP-USD | 12.53 | — | entry signal |
| 2026-09-30T13:00 | Donchian 20/10 · 1h | buy | SOL-USD | 15.72 | — | entry signal |
| 2026-09-30T13:00 | Donchian 20/10 · 1h | buy | ETH-USD | 15.72 | — | entry signal |
| 2026-09-30T13:00 | Donchian 20/10 · 1h | buy | BTC-USD | 15.72 | — | entry signal |
| 2026-09-30T13:00 | Donchian 20/10 · 1h | sell | DOGE-USD | 8.07 | 0.08 | rebalance down |
| 2026-09-30T13:00 | RSI momentum · 1h | buy | BTC-USD | 11.79 | — | entry signal |
| 2026-09-30T13:00 | RSI momentum · 1h | sell | DOGE-USD | 11.98 | 0.13 | rebalance down |
| 2026-09-30T13:00 | ROC + volume · 1h | buy | XRP-USD | 17.91 | — | entry signal |
| 2026-09-30T13:00 | ROC + volume · 1h | buy | SOL-USD | 17.92 | — | entry signal |
| 2026-09-30T13:00 | ROC + volume · 1h | buy | ETH-USD | 17.92 | — | entry signal |
| 2026-09-30T13:00 | ROC + volume · 1h | buy | BTC-USD | 17.92 | — | entry signal |
| 2026-09-30T13:00 | ROC + volume · 1h | sell | DOGE-USD | 4.75 | 0.07 | rebalance down |
| 2026-09-30T13:00 | Ichimoku · 1h | buy | BTC-USD | 23.82 | — | entry signal |
| 2026-09-30T13:00 | Supertrend · 1h | buy | DOGE-USD | 9.72 | — | entry signal |
| 2026-09-30T13:00 | Triple EMA stack · 1h | buy | ETH-USD | 23.41 | — | entry signal |
| 2026-09-30T13:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 8.85 | — | entry signal |
| 2026-09-30T13:00 | EMA 20/50 cross · 1h | buy | DOGE-USD | 8.85 | — | entry signal |
| 2026-09-30T13:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 8.85 | — | entry signal |
| 2026-09-30T13:00 | OBV trend | buy | XRP-USD | 3.62 | — | rebalance up |
| 2026-09-30T13:00 | OBV trend | sell | BTC-USD | 3.62 | 0.04 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
