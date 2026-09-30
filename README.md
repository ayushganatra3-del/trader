# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T12:10:05.000141+00:00 · 6863 ticks

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

Today: 9405 decisions in 1881 calls, $0.1316 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T12:10 | 1 / 2 / 2 | SOL-USD 18% |  |
| Breezy | 2026-09-30T12:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T12:10 | 3 / 2 / 0 | ETH-USD 30%, SOL-USD 30% |  |

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
| 7 | Hold BTC | benchmark | 99.72 | -0.28 | 0 | — | 28.96 | 3.64 | -8.68 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Agent | meta | 99.58 | -0.42 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 10 | Copy: Congress Democrats (NANC) | copy | 99.56 | -0.44 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 11 | Agent (aggressive) | meta | 99.31 | -0.69 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.22 | -0.78 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 13 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 14 | Hold SPY | benchmark | 98.99 | -1.01 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 98.91 | -1.09 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 98.90 | -1.10 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 17 | RSI(14) reversion · 1h | reversion | 98.89 | -1.11 | 7 | 57.1 | 5.23 | 1.36 | -7.03 | 119 |
| 18 | VWAP reversion · 1h | reversion | 98.89 | -1.11 | 20 | 25.0 | -12.98 | -4.39 | -14.76 | 122 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 20 | Daily: Bullish score | daily | 98.56 | -1.44 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 21 | Z-score reversion · 1h | reversion | 98.51 | -1.49 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 23 | Copy: Insider buying | copy | 98.42 | -1.58 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Williams %R · 1h | reversion | 98.24 | -1.76 | 43 | 44.2 | -17.70 | -3.27 | -19.41 | 488 |
| 26 | Candlestick reversal · 1h | reversion | 98.08 | -1.93 | 27 | 22.2 | -26.31 | -6.58 | -26.96 | 488 |
| 27 | Stochastic reversion · 1h | reversion | 98.04 | -1.96 | 26 | 53.8 | -12.86 | -2.85 | -14.12 | 328 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 97.95 | -2.05 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 30 | CCI reversion · 1h | reversion | 97.76 | -2.24 | 35 | 34.3 | 1.36 | 0.39 | -12.41 | 409 |
| 31 | Connors RSI(2) · 1h | reversion | 97.49 | -2.51 | 45 | 44.4 | -11.29 | -3.59 | -11.74 | 233 |
| 32 | EMA 20/50 cross · 1h | trend | 97.32 | -2.68 | 13 | 7.7 | 17.09 | 2.02 | -14.13 | 124 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 97.30 | -2.70 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 34 | Max aggression: 5-day momentum | meta | 97.21 | -2.79 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Squeeze breakout · 1h | breakout | 96.95 | -3.05 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 37 | Bollinger reversion · 1h | reversion | 96.79 | -3.21 | 22 | 27.3 | -17.47 | -4.86 | -18.09 | 312 |
| 38 | Supertrend · 1h | trend | 96.20 | -3.80 | 18 | 5.6 | 2.06 | 0.48 | -16.43 | 194 |
| 39 | Max aggression: 1-day momentum | meta | 96.18 | -3.82 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 40 | Daily: SMA 20/50 cross · AAPL | daily | 96.14 | -3.86 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 41 | Trend pullback · 1h | trend | 95.92 | -4.08 | 28 | 10.7 | -29.22 | -7.18 | -29.64 | 148 |
| 42 | Agent (ML meta-label) | meta | 95.88 | -4.12 | 144 | 12.5 | 1.94 | 0.48 | -12.17 | 396 |
| 43 | MACD cross · 1h | trend | 95.64 | -4.36 | 40 | 10.0 | -18.47 | -3.13 | -21.37 | 465 |
| 44 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 45 | Parabolic SAR · 1h | trend | 95.43 | -4.57 | 26 | 11.5 | -7.75 | -0.96 | -18.82 | 295 |
| 46 | Donchian 55/20 · 1h | breakout | 95.37 | -4.63 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 47 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.28 | -27.84 | -50.33 | 607 |
| 48 | MFI reversion · 1h | reversion | 95.04 | -4.96 | 44 | 13.6 | -9.60 | -1.75 | -17.20 | 129 |
| 49 | Ichimoku · 1h | trend | 94.87 | -5.13 | 16 | 18.8 | 6.82 | 0.99 | -15.13 | 123 |
| 50 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 51 | Bollinger breakout · 1h | breakout | 94.55 | -5.45 | 17 | 5.9 | 8.08 | 1.24 | -10.10 | 285 |
| 52 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.31 | 0.27 | -18.68 | 213 |
| 53 | Donchian 20/10 · 1h | breakout | 93.90 | -6.10 | 16 | 12.5 | 6.90 | 1.07 | -12.78 | 214 |
| 54 | RSI momentum · 1h | momentum | 93.86 | -6.14 | 24 | 4.2 | 1.54 | 0.41 | -15.29 | 208 |
| 55 | Triple EMA stack · 1h | trend | 93.63 | -6.37 | 30 | 6.7 | -6.75 | -0.63 | -22.58 | 226 |
| 56 | ADX DI cross · 1h | trend | 93.56 | -6.44 | 30 | 6.7 | -15.88 | -2.93 | -17.71 | 254 |
| 57 | MACD zero-line · 1h | trend | 93.40 | -6.61 | 21 | 4.8 | -6.09 | -0.67 | -14.73 | 227 |
| 58 | VWAP momentum · 1h | momentum | 93.22 | -6.78 | 103 | 12.6 | -34.56 | -5.21 | -35.64 | 1241 |
| 59 | EMA 9/21 cross · 1h | trend | 92.29 | -7.71 | 45 | 11.1 | -4.67 | -0.44 | -16.92 | 314 |
| 60 | Heikin-Ashi · 1h | trend | 92.23 | -7.77 | 45 | 11.1 | -26.51 | -4.02 | -30.79 | 676 |
| 61 | OBV trend · 1h | momentum | 92.02 | -7.98 | 54 | 7.4 | -12.74 | -1.39 | -25.19 | 315 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.13 | -71.11 | 1470 |
| 63 | ROC + volume · 1h | momentum | 89.25 | -10.75 | 53 | 5.7 | -4.55 | -0.37 | -19.59 | 406 |
| 64 | Squeeze breakout | breakout | 88.27 | -11.73 | 100 | 14.0 | -59.75 | -18.60 | -59.75 | 1190 |
| 65 | Volume breakout | breakout | 86.60 | -13.40 | 107 | 15.0 | -61.79 | -19.82 | -61.90 | 896 |
| 66 | ROC + volume | momentum | 86.25 | -13.74 | 155 | 18.1 | -72.13 | -17.66 | -72.21 | 1630 |
| 67 | Donchian 55/20 | breakout | 86.10 | -13.90 | 101 | 14.9 | -67.65 | -15.47 | -67.86 | 1298 |
| 68 | Keltner breakout | breakout | 84.69 | -15.31 | 155 | 12.9 | -84.65 | -34.36 | -84.65 | 1893 |
| 69 | EMA 20/50 cross | trend | 84.41 | -15.59 | 135 | 14.8 | -79.00 | -17.68 | -79.13 | 1478 |
| 70 | VWAP reversion | reversion | 83.90 | -16.10 | 145 | 22.1 | -71.80 | -17.69 | -72.04 | 1405 |
| 71 | Ichimoku | trend | 83.73 | -16.27 | 123 | 8.1 | -80.51 | -26.13 | -80.51 | 1745 |
| 72 | Z-score reversion | reversion | 83.65 | -16.34 | 193 | 30.6 | -84.59 | -27.49 | -84.60 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.06 | -19.94 | 190 | 18.9 | -88.08 | -35.26 | -88.14 | 2146 |
| 76 | Supertrend | trend | 79.84 | -20.16 | 191 | 16.8 | -87.51 | -24.71 | -87.62 | 1960 |
| 77 | Donchian 20/10 | breakout | 79.63 | -20.37 | 213 | 16.9 | -90.75 | -29.42 | -90.79 | 2673 |
| 78 | MACD zero-line | trend | 79.28 | -20.72 | 220 | 15.0 | -91.87 | -36.10 | -91.87 | 2359 |
| 79 | Bollinger breakout | breakout | 78.58 | -21.42 | 221 | 15.4 | -93.84 | -42.28 | -93.84 | 2862 |
| 80 | Trend pullback | trend | 78.36 | -21.64 | 174 | 16.7 | -90.60 | -33.34 | -90.62 | 2263 |
| 81 | Triple EMA stack | trend | 78.14 | -21.86 | 226 | 14.6 | -93.05 | -35.93 | -93.09 | 2619 |
| 82 | RSI momentum | momentum | 77.77 | -22.23 | 209 | 12.4 | -90.37 | -29.03 | -90.44 | 2379 |
| 83 | ADX DI cross | trend | 77.26 | -22.74 | 210 | 7.6 | -89.36 | -44.78 | -89.39 | 2109 |
| 84 | Connors RSI(2) | reversion | 76.46 | -23.54 | 248 | 16.5 | -96.28 | -39.10 | -96.28 | 3602 |
| 85 | Consensus | meta | 76.00 | -24.00 | 195 | 7.2 | -94.60 | -29.88 | -94.60 | 2647 |
| 86 | Stochastic reversion | reversion | 74.89 | -25.11 | 343 | 23.3 | -95.90 | -44.43 | -95.93 | 4054 |
| 87 | Candlestick reversal | reversion | 73.85 | -26.15 | 296 | 12.2 | -99.36 | -49.24 | -99.36 | 5588 |
| 88 | EMA 9/21 cross | trend | 73.66 | -26.34 | 301 | 15.9 | -97.43 | -41.52 | -97.46 | 3538 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.77 | -42.91 | -95.80 | 3680 |
| 90 | OBV trend | momentum | 71.62 | -28.38 | 296 | 14.2 | -95.91 | -48.57 | -95.91 | 3548 |
| 91 | CCI reversion | reversion | 70.86 | -29.14 | 266 | 10.5 | -98.46 | -49.13 | -98.46 | 4696 |
| 92 | Parabolic SAR | trend | 70.44 | -29.56 | 287 | 12.2 | -96.96 | -54.65 | -96.96 | 3627 |
| 93 | MACD cross | trend | 68.76 | -31.24 | 303 | 13.5 | -99.72 | -64.84 | -99.72 | 6079 |
| 94 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.54 | -36.26 | -98.55 | 5238 |
| 95 | Williams %R | reversion | 68.43 | -31.57 | 373 | 19.6 | -99.52 | -57.16 | -99.53 | 6110 |
| 96 | Heikin-Ashi | trend | 67.42 | -32.58 | 266 | 3.0 | -99.89 | -79.61 | -99.89 | 8299 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T12:10 | Consensus | sell | XRP-USD | 18.90 | -0.16 | target is flat |
| 2026-09-30T12:10 | Squeeze breakout | sell | XRP-USD | 21.89 | -0.23 | exit signal |
| 2026-09-30T12:10 | Keltner breakout | sell | XRP-USD | 21.02 | -0.22 | exit signal |
| 2026-09-30T12:10 | Bollinger breakout | sell | XRP-USD | 19.53 | -0.21 | exit signal |
| 2026-09-30T12:10 | Bollinger breakout | sell | ETH-USD | 19.58 | -0.15 | exit signal |
| 2026-09-30T12:10 | OBV trend | sell | XRP-USD | 17.85 | -0.17 | exit signal |
| 2026-09-30T12:10 | OBV trend | sell | BTC-USD | 14.35 | -0.09 | exit signal |
| 2026-09-30T12:10 | Ichimoku | buy | SOL-USD | 20.98 | — | entry signal |
| 2026-09-30T12:10 | Ichimoku | sell | XRP-USD | 20.86 | -0.22 | exit signal |
| 2026-09-30T12:10 | Ichimoku | sell | BTC-USD | 20.99 | -0.13 | exit signal |
| 2026-09-30T12:10 | MACD cross | sell | XRP-USD | 17.07 | -0.18 | exit signal |
| 2026-09-30T12:01 | MACD zero-line · 1h | buy | SOL-USD | 4.67 | — | rebalance up |
| 2026-09-30T12:01 | MACD zero-line · 1h | sell | XRP-USD | 4.67 | -0.02 | rebalance down |
| 2026-09-30T12:00 | Agent (ML meta-label) | buy | XRP-USD | 2.56 | — | entry |
| 2026-09-30T12:00 | Agent (ML meta-label) | buy | DOGE-USD | 5.05 | — | entry |
| 2026-09-30T12:00 | Consensus | buy | XRP-USD | 19.05 | — | entry |
| 2026-09-30T12:00 | Consensus | buy | DOGE-USD | 19.05 | — | entry |
| 2026-09-30T12:00 | Bollinger breakout · 1h | buy | XRP-USD | 4.42 | — | entry signal |
| 2026-09-30T12:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 23.49 | — | entry signal |
| 2026-09-30T12:00 | RSI momentum · 1h | buy | DOGE-USD | 23.48 | — | entry signal |
| 2026-09-30T12:00 | Heikin-Ashi · 1h | buy | SOL-USD | 6.46 | — | entry signal |
| 2026-09-30T12:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 13.20 | — | entry signal |
| 2026-09-30T12:00 | Heikin-Ashi · 1h | buy | BTC-USD | 13.20 | — | entry signal |
| 2026-09-30T12:00 | Heikin-Ashi · 1h | sell | ETH-USD | 9.82 | -0.06 | rebalance down |
| 2026-09-30T12:00 | Ichimoku · 1h | buy | DOGE-USD | 23.74 | — | entry signal |
| 2026-09-30T12:00 | MACD zero-line · 1h | buy | SOL-USD | 9.43 | — | entry signal |
| 2026-09-30T12:00 | MACD zero-line · 1h | buy | DOGE-USD | 18.73 | — | entry signal |
| 2026-09-30T12:00 | MACD zero-line · 1h | buy | BTC-USD | 18.73 | — | entry signal |
| 2026-09-30T12:00 | Heikin-Ashi | sell | DOGE-USD | 16.79 | -0.16 | exit signal |
| 2026-09-30T11:56 | Agent (ML meta-label) | sell | XRP-USD | 5.63 | -0.01 | selected signal exited |
| 2026-09-30T11:56 | Consensus | sell | XRP-USD | 18.96 | -0.13 | target is flat |
| 2026-09-30T11:56 | OBV trend | buy | XRP-USD | 7.42 | — | rebalance up |
| 2026-09-30T11:56 | OBV trend | sell | SOL-USD | 14.29 | -0.13 | exit signal |
| 2026-09-30T11:56 | Heikin-Ashi | sell | XRP-USD | 16.80 | -0.12 | exit signal |
| 2026-09-30T11:56 | Heikin-Ashi | sell | ETH-USD | 16.84 | -0.12 | exit signal |
| 2026-09-30T11:56 | Ichimoku | buy | ETH-USD | 21.02 | — | entry signal |
| 2026-09-30T11:56 | Ichimoku | sell | SOL-USD | 21.01 | -0.08 | exit signal |
| 2026-09-30T11:50 | Consensus | buy | XRP-USD | 19.09 | — | entry |
| 2026-09-30T11:50 | Heikin-Ashi | buy | XRP-USD | 16.92 | — | entry signal |
| 2026-09-30T11:46 | Parabolic SAR | buy | SOL-USD | 3.52 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
