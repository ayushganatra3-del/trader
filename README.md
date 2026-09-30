# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T12:40:05.000117+00:00 · 6887 ticks

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

Today: 9765 decisions in 1953 calls, $0.1366 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T12:40 | 3 / 2 / 0 | BTC-USD 21%, XRP-USD 20%, SOL-USD 14% |  |
| Breezy | 2026-09-30T12:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T12:40 | 5 / 0 / 0 | ETH-USD 42%, SOL-USD 42% |  |

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
| 1 | Hold BTC | benchmark | 101.03 | 1.03 | 0 | — | 30.21 | 3.76 | -8.68 | 1 |
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
| 17 | VWAP reversion · 1h | reversion | 98.92 | -1.08 | 20 | 25.0 | -12.98 | -4.39 | -14.76 | 122 |
| 18 | RSI(14) reversion · 1h | reversion | 98.91 | -1.09 | 7 | 57.1 | 5.23 | 1.36 | -7.03 | 119 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 20 | Daily: Bullish score | daily | 98.62 | -1.38 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 21 | Z-score reversion · 1h | reversion | 98.56 | -1.44 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Copy: Insider buying | copy | 98.48 | -1.52 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.67 | -4.73 | 182 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Williams %R · 1h | reversion | 98.29 | -1.71 | 43 | 44.2 | -17.65 | -3.26 | -19.41 | 488 |
| 26 | Candlestick reversal · 1h | reversion | 98.21 | -1.79 | 27 | 22.2 | -26.12 | -6.52 | -26.88 | 488 |
| 27 | Stochastic reversion · 1h | reversion | 98.11 | -1.89 | 26 | 53.8 | -12.83 | -2.84 | -14.09 | 329 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.01 | -1.99 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.76 | -11.16 | 207 |
| 30 | CCI reversion · 1h | reversion | 97.83 | -2.17 | 35 | 34.3 | 1.37 | 0.39 | -12.41 | 409 |
| 31 | Connors RSI(2) · 1h | reversion | 97.54 | -2.46 | 45 | 44.4 | -11.29 | -3.59 | -11.74 | 233 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.37 | -2.63 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.36 | -2.64 | 13 | 7.7 | 17.09 | 2.02 | -14.13 | 124 |
| 34 | Max aggression: 5-day momentum | meta | 97.27 | -2.73 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Squeeze breakout · 1h | breakout | 96.97 | -3.03 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 37 | Bollinger reversion · 1h | reversion | 96.85 | -3.15 | 22 | 27.3 | -17.40 | -4.85 | -18.02 | 312 |
| 38 | Supertrend · 1h | trend | 96.46 | -3.54 | 18 | 5.6 | 2.32 | 0.51 | -16.43 | 194 |
| 39 | Max aggression: 1-day momentum | meta | 96.24 | -3.76 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 40 | Daily: SMA 20/50 cross · AAPL | daily | 96.20 | -3.80 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 41 | Agent (ML meta-label) | meta | 96.10 | -3.90 | 145 | 12.4 | 0.63 | 0.27 | -12.38 | 407 |
| 42 | Trend pullback · 1h | trend | 95.96 | -4.04 | 28 | 10.7 | -28.99 | -7.11 | -29.45 | 147 |
| 43 | MACD cross · 1h | trend | 95.71 | -4.29 | 40 | 10.0 | -17.80 | -2.99 | -21.37 | 465 |
| 44 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.85 | -16.91 | 684 |
| 45 | Parabolic SAR · 1h | trend | 95.49 | -4.51 | 26 | 11.5 | -7.17 | -0.87 | -18.82 | 295 |
| 46 | Donchian 55/20 · 1h | breakout | 95.43 | -4.57 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 47 | Bollinger breakout · 1h | breakout | 95.37 | -4.63 | 17 | 5.9 | 9.31 | 1.39 | -10.10 | 285 |
| 48 | MFI reversion · 1h | reversion | 95.32 | -4.68 | 44 | 13.6 | -9.09 | -1.64 | -17.20 | 129 |
| 49 | Ichimoku · 1h | trend | 95.30 | -4.70 | 16 | 18.8 | 7.26 | 1.03 | -15.13 | 123 |
| 50 | Three white soldiers | momentum | 95.23 | -4.78 | 44 | 18.2 | -50.04 | -27.45 | -50.14 | 607 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | MACD zero-line · 1h | trend | 94.53 | -5.47 | 21 | 4.8 | -4.94 | -0.50 | -14.79 | 227 |
| 53 | Donchian 20/10 · 1h | breakout | 94.31 | -5.69 | 16 | 12.5 | 7.34 | 1.12 | -12.78 | 214 |
| 54 | RSI momentum · 1h | momentum | 94.30 | -5.70 | 24 | 4.2 | 1.95 | 0.46 | -15.29 | 208 |
| 55 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.01 | 0.23 | -18.68 | 214 |
| 56 | Triple EMA stack · 1h | trend | 93.66 | -6.34 | 30 | 6.7 | -6.75 | -0.63 | -22.58 | 226 |
| 57 | ADX DI cross · 1h | trend | 93.62 | -6.38 | 30 | 6.7 | -16.05 | -2.96 | -17.73 | 255 |
| 58 | VWAP momentum · 1h | momentum | 93.29 | -6.71 | 103 | 12.6 | -34.22 | -5.14 | -35.64 | 1241 |
| 59 | EMA 9/21 cross · 1h | trend | 92.95 | -7.05 | 45 | 11.1 | -3.93 | -0.34 | -16.92 | 314 |
| 60 | Heikin-Ashi · 1h | trend | 92.93 | -7.07 | 45 | 11.1 | -25.72 | -3.87 | -30.80 | 676 |
| 61 | OBV trend · 1h | momentum | 92.08 | -7.92 | 54 | 7.4 | -12.74 | -1.39 | -25.19 | 315 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.12 | -71.11 | 1469 |
| 63 | ROC + volume · 1h | momentum | 89.63 | -10.37 | 53 | 5.7 | -4.16 | -0.32 | -19.59 | 406 |
| 64 | Squeeze breakout | breakout | 88.28 | -11.72 | 100 | 14.0 | -59.74 | -18.60 | -59.81 | 1192 |
| 65 | Donchian 55/20 | breakout | 87.29 | -12.71 | 101 | 14.9 | -67.19 | -15.19 | -67.83 | 1299 |
| 66 | ROC + volume | momentum | 86.55 | -13.45 | 155 | 18.1 | -72.02 | -17.58 | -72.21 | 1634 |
| 67 | Volume breakout | breakout | 86.48 | -13.52 | 108 | 15.7 | -61.58 | -19.59 | -61.99 | 898 |
| 68 | EMA 20/50 cross | trend | 85.69 | -14.31 | 135 | 14.8 | -78.67 | -17.47 | -79.12 | 1478 |
| 69 | Keltner breakout | breakout | 85.10 | -14.90 | 155 | 12.9 | -84.42 | -33.75 | -84.51 | 1893 |
| 70 | Ichimoku | trend | 83.97 | -16.03 | 124 | 8.1 | -80.46 | -26.07 | -80.52 | 1745 |
| 71 | VWAP reversion | reversion | 83.90 | -16.10 | 145 | 22.1 | -71.72 | -17.62 | -72.02 | 1402 |
| 72 | Z-score reversion | reversion | 83.65 | -16.34 | 193 | 30.6 | -84.58 | -27.48 | -84.60 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 81.07 | -18.93 | 191 | 16.8 | -87.33 | -24.39 | -87.61 | 1960 |
| 76 | Donchian 20/10 | breakout | 80.62 | -19.38 | 214 | 16.8 | -90.58 | -28.87 | -90.73 | 2670 |
| 77 | MFI reversion | reversion | 80.06 | -19.94 | 190 | 18.9 | -88.09 | -35.29 | -88.15 | 2147 |
| 78 | Triple EMA stack | trend | 79.33 | -20.67 | 226 | 14.6 | -92.92 | -35.12 | -93.07 | 2617 |
| 79 | MACD zero-line | trend | 79.28 | -20.72 | 220 | 15.0 | -91.87 | -36.09 | -91.87 | 2359 |
| 80 | Bollinger breakout | breakout | 78.96 | -21.04 | 221 | 15.4 | -93.76 | -41.77 | -93.80 | 2863 |
| 81 | Trend pullback | trend | 78.91 | -21.09 | 180 | 18.9 | -90.54 | -33.05 | -90.62 | 2265 |
| 82 | RSI momentum | momentum | 78.72 | -21.28 | 210 | 12.4 | -90.22 | -28.59 | -90.41 | 2378 |
| 83 | ADX DI cross | trend | 77.40 | -22.59 | 211 | 7.6 | -89.33 | -44.43 | -89.42 | 2111 |
| 84 | Connors RSI(2) | reversion | 76.46 | -23.54 | 248 | 16.5 | -96.28 | -39.09 | -96.28 | 3602 |
| 85 | Consensus | meta | 76.41 | -23.59 | 195 | 7.2 | -94.52 | -29.74 | -94.56 | 2646 |
| 86 | Stochastic reversion | reversion | 74.89 | -25.11 | 343 | 23.3 | -95.90 | -44.34 | -95.93 | 4052 |
| 87 | EMA 9/21 cross | trend | 74.82 | -25.18 | 301 | 15.9 | -97.38 | -40.73 | -97.45 | 3536 |
| 88 | Candlestick reversal | reversion | 73.85 | -26.15 | 296 | 12.2 | -99.37 | -49.58 | -99.37 | 5594 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.77 | -42.92 | -95.79 | 3680 |
| 90 | OBV trend | momentum | 72.41 | -27.59 | 296 | 14.2 | -95.86 | -48.01 | -95.91 | 3550 |
| 91 | CCI reversion | reversion | 70.86 | -29.14 | 266 | 10.5 | -98.46 | -49.13 | -98.46 | 4696 |
| 92 | Parabolic SAR | trend | 70.80 | -29.20 | 290 | 12.1 | -96.95 | -54.26 | -96.97 | 3630 |
| 93 | MACD cross | trend | 68.91 | -31.09 | 304 | 13.5 | -99.72 | -64.57 | -99.72 | 6083 |
| 94 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.53 | -36.15 | -98.56 | 5240 |
| 95 | Williams %R | reversion | 68.55 | -31.45 | 374 | 19.8 | -99.52 | -56.58 | -99.52 | 6106 |
| 96 | Heikin-Ashi | trend | 67.39 | -32.61 | 266 | 3.0 | -99.90 | -79.66 | -99.90 | 8301 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T12:40 | Donchian 55/20 | buy | SOL-USD | 4.38 | — | rebalance up |
| 2026-09-30T12:40 | Donchian 55/20 | sell | XRP-USD | 4.38 | 0.05 | rebalance down |
| 2026-09-30T12:40 | Heikin-Ashi | buy | ETH-USD | 16.86 | — | entry signal |
| 2026-09-30T12:40 | Parabolic SAR | sell | BTC-USD | 3.55 | 0.02 | rebalance down |
| 2026-09-30T12:37 | Consensus | buy | XRP-USD | 3.82 | — | rebalance up |
| 2026-09-30T12:37 | Consensus | sell | ETH-USD | 3.82 | 0.00 | rebalance down |
| 2026-09-30T12:37 | Keltner breakout | buy | XRP-USD | 4.26 | — | rebalance up |
| 2026-09-30T12:37 | Keltner breakout | sell | ETH-USD | 4.26 | 0.00 | rebalance down |
| 2026-09-30T12:37 | Bollinger breakout | buy | XRP-USD | 3.95 | — | rebalance up |
| 2026-09-30T12:37 | Bollinger breakout | sell | ETH-USD | 3.95 | 0.00 | rebalance down |
| 2026-09-30T12:37 | RSI momentum | buy | XRP-USD | 3.92 | — | rebalance up |
| 2026-09-30T12:37 | RSI momentum | sell | ETH-USD | 3.92 | 0.03 | rebalance down |
| 2026-09-30T12:35 | Consensus | buy | XRP-USD | 11.47 | — | entry |
| 2026-09-30T12:35 | Consensus | buy | SOL-USD | 15.28 | — | entry |
| 2026-09-30T12:35 | Consensus | buy | BTC-USD | 15.28 | — | entry |
| 2026-09-30T12:35 | Consensus | sell | DOGE-USD | 4.02 | 0.04 | rebalance down |
| 2026-09-30T12:35 | Williams %R | sell | XRP-USD | 17.22 | 0.12 | exit signal |
| 2026-09-30T12:35 | Three white soldiers | buy | XRP-USD | 23.79 | — | entry signal |
| 2026-09-30T12:35 | Three white soldiers | buy | BTC-USD | 23.79 | — | entry signal |
| 2026-09-30T12:35 | Volume breakout | buy | XRP-USD | 17.30 | — | entry signal |
| 2026-09-30T12:35 | Volume breakout | buy | SOL-USD | 17.30 | — | entry signal |
| 2026-09-30T12:35 | Volume breakout | buy | ETH-USD | 17.30 | — | entry signal |
| 2026-09-30T12:35 | Volume breakout | buy | DOGE-USD | 17.30 | — | entry signal |
| 2026-09-30T12:35 | Volume breakout | buy | BTC-USD | 17.30 | — | entry signal |
| 2026-09-30T12:35 | Squeeze breakout | buy | SOL-USD | 22.07 | — | entry signal |
| 2026-09-30T12:35 | Squeeze breakout | buy | BTC-USD | 22.07 | — | entry signal |
| 2026-09-30T12:35 | Keltner breakout | buy | XRP-USD | 12.29 | — | entry signal |
| 2026-09-30T12:35 | Keltner breakout | buy | SOL-USD | 17.01 | — | entry signal |
| 2026-09-30T12:35 | Keltner breakout | buy | BTC-USD | 17.01 | — | entry signal |
| 2026-09-30T12:35 | Bollinger breakout | buy | XRP-USD | 11.39 | — | entry signal |
| 2026-09-30T12:35 | Bollinger breakout | buy | SOL-USD | 15.78 | — | entry signal |
| 2026-09-30T12:35 | Bollinger breakout | buy | BTC-USD | 15.78 | — | entry signal |
| 2026-09-30T12:35 | Donchian 55/20 | buy | SOL-USD | 4.25 | — | entry signal |
| 2026-09-30T12:35 | Donchian 20/10 | buy | XRP-USD | 7.86 | — | entry signal |
| 2026-09-30T12:35 | Donchian 20/10 | sell | SOL-USD | 4.05 | 0.04 | rebalance down |
| 2026-09-30T12:35 | OBV trend | buy | XRP-USD | 10.52 | — | entry signal |
| 2026-09-30T12:35 | OBV trend | sell | SOL-USD | 3.61 | 0.02 | rebalance down |
| 2026-09-30T12:35 | OBV trend | sell | ETH-USD | 3.68 | 0.02 | rebalance down |
| 2026-09-30T12:35 | RSI momentum | buy | XRP-USD | 7.64 | — | entry signal |
| 2026-09-30T12:35 | RSI momentum | sell | SOL-USD | 3.96 | 0.04 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
