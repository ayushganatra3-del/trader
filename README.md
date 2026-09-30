# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T10:10:05.000158+00:00 · 6768 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.61 (-0.39%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.95 | -0.04 |

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

Today: 7980 decisions in 1596 calls, $0.1117 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T10:10 | 1 / 2 / 2 | DOGE-USD 15% |  |
| Breezy | 2026-09-30T10:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T10:10 | 3 / 2 / 0 | DOGE-USD 30%, ETH-USD 28% |  |

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
| 7 | Hold BTC | benchmark | 99.78 | -0.22 | 0 | — | 29.33 | 3.68 | -8.68 | 1 |
| 8 | Copy: Congress Democrats (NANC) | copy | 99.70 | -0.30 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 10 | Agent | meta | 99.61 | -0.39 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 11 | Agent (aggressive) | meta | 99.38 | -0.62 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.36 | -0.64 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 13 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 14 | Hold SPY | benchmark | 99.13 | -0.87 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.05 | -0.95 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 99.04 | -0.96 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 17 | VWAP reversion · 1h | reversion | 98.95 | -1.04 | 20 | 25.0 | -12.98 | -4.39 | -14.75 | 122 |
| 18 | RSI(14) reversion · 1h | reversion | 98.93 | -1.07 | 7 | 57.1 | 6.37 | 1.63 | -7.03 | 116 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 20 | Daily: Bullish score | daily | 98.70 | -1.30 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 21 | Z-score reversion · 1h | reversion | 98.62 | -1.38 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Copy: Insider buying | copy | 98.54 | -1.46 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Williams %R · 1h | reversion | 98.33 | -1.67 | 40 | 45.0 | -17.79 | -3.28 | -19.41 | 488 |
| 26 | Stochastic reversion · 1h | reversion | 98.18 | -1.82 | 26 | 53.8 | -13.81 | -3.02 | -15.06 | 330 |
| 27 | Candlestick reversal · 1h | reversion | 98.15 | -1.84 | 25 | 20.0 | -25.99 | -6.51 | -26.70 | 487 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.08 | -1.92 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | CCI reversion · 1h | reversion | 97.90 | -2.10 | 35 | 34.3 | 1.35 | 0.39 | -12.41 | 409 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.60 | -2.40 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.44 | -2.56 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.42 | -2.58 | 13 | 7.7 | 16.95 | 2.01 | -14.13 | 125 |
| 34 | Max aggression: 5-day momentum | meta | 97.34 | -2.65 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Squeeze breakout · 1h | breakout | 96.99 | -3.01 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 37 | Bollinger reversion · 1h | reversion | 96.93 | -3.07 | 22 | 27.3 | -17.38 | -4.84 | -18.00 | 312 |
| 38 | Max aggression: 1-day momentum | meta | 96.32 | -3.68 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Supertrend · 1h | trend | 96.31 | -3.69 | 18 | 5.6 | 2.05 | 0.48 | -16.43 | 194 |
| 40 | Daily: SMA 20/50 cross · AAPL | daily | 96.27 | -3.73 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 41 | Agent (ML meta-label) | meta | 96.11 | -3.89 | 140 | 12.9 | -0.11 | 0.14 | -12.53 | 398 |
| 42 | Trend pullback · 1h | trend | 96.02 | -3.98 | 28 | 10.7 | -29.16 | -7.16 | -29.64 | 148 |
| 43 | MACD cross · 1h | trend | 95.78 | -4.22 | 40 | 10.0 | -18.78 | -3.18 | -21.59 | 464 |
| 44 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 45 | Parabolic SAR · 1h | trend | 95.56 | -4.44 | 26 | 11.5 | -7.93 | -0.99 | -18.82 | 295 |
| 46 | Donchian 55/20 · 1h | breakout | 95.50 | -4.50 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 47 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.28 | -27.84 | -50.33 | 607 |
| 48 | MFI reversion · 1h | reversion | 95.15 | -4.85 | 44 | 13.6 | -9.66 | -1.76 | -17.20 | 129 |
| 49 | Ichimoku · 1h | trend | 95.01 | -4.99 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.76 | -5.24 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.03 | -5.97 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 53 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.03 | 0.23 | -18.68 | 213 |
| 54 | Donchian 20/10 · 1h | breakout | 94.00 | -6.00 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | MACD zero-line · 1h | trend | 93.71 | -6.29 | 21 | 4.8 | -5.98 | -0.65 | -14.64 | 224 |
| 56 | ADX DI cross · 1h | trend | 93.69 | -6.31 | 30 | 6.7 | -15.90 | -2.94 | -17.73 | 254 |
| 57 | Triple EMA stack · 1h | trend | 93.69 | -6.31 | 30 | 6.7 | -6.73 | -0.62 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.36 | -6.64 | 103 | 12.6 | -34.65 | -5.22 | -35.64 | 1241 |
| 59 | Heikin-Ashi · 1h | trend | 92.54 | -7.46 | 45 | 11.1 | -26.26 | -3.97 | -30.63 | 671 |
| 60 | EMA 9/21 cross · 1h | trend | 92.51 | -7.49 | 45 | 11.1 | -4.26 | -0.39 | -16.92 | 308 |
| 61 | OBV trend · 1h | momentum | 92.15 | -7.85 | 54 | 7.4 | -12.85 | -1.41 | -25.19 | 316 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.07 | -21.19 | -71.11 | 1473 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 88.51 | -11.49 | 99 | 14.1 | -59.86 | -18.63 | -59.86 | 1192 |
| 65 | Volume breakout | breakout | 86.75 | -13.25 | 103 | 15.5 | -61.99 | -19.96 | -62.01 | 898 |
| 66 | ROC + volume | momentum | 86.33 | -13.67 | 151 | 18.5 | -72.17 | -17.70 | -72.19 | 1631 |
| 67 | Donchian 55/20 | breakout | 86.00 | -14.00 | 100 | 15.0 | -67.85 | -15.58 | -67.89 | 1299 |
| 68 | Keltner breakout | breakout | 84.98 | -15.02 | 150 | 13.3 | -84.74 | -34.26 | -84.76 | 1897 |
| 69 | Ichimoku | trend | 84.31 | -15.69 | 119 | 8.4 | -80.44 | -26.05 | -80.47 | 1744 |
| 70 | EMA 20/50 cross | trend | 84.22 | -15.78 | 135 | 14.8 | -79.04 | -17.70 | -79.09 | 1477 |
| 71 | VWAP reversion | reversion | 83.90 | -16.10 | 145 | 22.1 | -71.74 | -17.62 | -72.04 | 1402 |
| 72 | Z-score reversion | reversion | 83.65 | -16.34 | 193 | 30.6 | -84.59 | -27.49 | -84.60 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.06 | -19.94 | 190 | 18.9 | -88.14 | -35.54 | -88.15 | 2149 |
| 76 | Supertrend | trend | 79.66 | -20.34 | 191 | 16.8 | -87.60 | -24.83 | -87.66 | 1962 |
| 77 | MACD zero-line | trend | 79.47 | -20.53 | 217 | 15.2 | -91.89 | -36.14 | -91.91 | 2361 |
| 78 | Donchian 20/10 | breakout | 79.47 | -20.53 | 213 | 16.9 | -90.91 | -29.70 | -90.92 | 2679 |
| 79 | Bollinger breakout | breakout | 78.94 | -21.06 | 215 | 15.8 | -93.88 | -42.22 | -93.89 | 2866 |
| 80 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.58 | -33.23 | -90.58 | 2259 |
| 81 | Triple EMA stack | trend | 77.97 | -22.03 | 226 | 14.6 | -93.07 | -36.06 | -93.09 | 2620 |
| 82 | RSI momentum | momentum | 77.59 | -22.41 | 209 | 12.4 | -90.47 | -29.27 | -90.50 | 2382 |
| 83 | ADX DI cross | trend | 77.28 | -22.71 | 210 | 7.6 | -89.51 | -46.12 | -89.51 | 2115 |
| 84 | Connors RSI(2) | reversion | 76.96 | -23.05 | 243 | 16.9 | -96.26 | -38.78 | -96.26 | 3597 |
| 85 | Consensus | meta | 76.75 | -23.25 | 189 | 7.4 | -94.51 | -29.44 | -94.52 | 2638 |
| 86 | Stochastic reversion | reversion | 74.89 | -25.11 | 343 | 23.3 | -95.91 | -44.60 | -95.93 | 4055 |
| 87 | Candlestick reversal | reversion | 73.85 | -26.15 | 296 | 12.2 | -99.36 | -49.55 | -99.37 | 5594 |
| 88 | EMA 9/21 cross | trend | 73.48 | -26.52 | 301 | 15.9 | -97.46 | -41.88 | -97.48 | 3541 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.78 | -43.22 | -95.80 | 3684 |
| 90 | OBV trend | momentum | 72.12 | -27.88 | 290 | 14.5 | -95.90 | -48.43 | -95.90 | 3548 |
| 91 | Parabolic SAR | trend | 71.13 | -28.86 | 282 | 12.4 | -96.95 | -54.14 | -96.96 | 3624 |
| 92 | CCI reversion | reversion | 70.95 | -29.05 | 264 | 10.6 | -98.46 | -49.30 | -98.46 | 4699 |
| 93 | MACD cross | trend | 69.34 | -30.66 | 295 | 12.9 | -99.72 | -64.77 | -99.72 | 6081 |
| 94 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.56 | -36.34 | -98.56 | 5238 |
| 95 | Williams %R | reversion | 68.53 | -31.46 | 371 | 19.7 | -99.52 | -57.06 | -99.52 | 6109 |
| 96 | Heikin-Ashi | trend | 68.36 | -31.64 | 257 | 3.1 | -99.90 | -78.79 | -99.90 | 8302 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T10:10 | Donchian 20/10 | buy | BTC-USD | 3.98 | — | rebalance up |
| 2026-09-30T10:10 | Donchian 20/10 | sell | DOGE-USD | 3.98 | -0.01 | rebalance down |
| 2026-09-30T10:10 | RSI momentum | buy | XRP-USD | 3.88 | — | rebalance up |
| 2026-09-30T10:10 | Heikin-Ashi | sell | SOL-USD | 17.03 | -0.11 | exit signal |
| 2026-09-30T10:05 | Parabolic SAR | sell | DOGE-USD | 17.74 | -0.01 | exit signal |
| 2026-09-30T10:00 | Consensus | buy | ETH-USD | 19.21 | — | entry |
| 2026-09-30T10:00 | Consensus | buy | BTC-USD | 19.21 | — | entry |
| 2026-09-30T10:00 | Candlestick reversal · 1h | buy | ETH-USD | 6.01 | — | entry signal |
| 2026-09-30T10:00 | Candlestick reversal · 1h | buy | BTC-USD | 6.13 | — | entry signal |
| 2026-09-30T10:00 | Heikin-Ashi | buy | SOL-USD | 17.13 | — | entry signal |
| 2026-09-30T10:00 | Heikin-Ashi | sell | XRP-USD | 17.07 | -0.12 | exit signal |
| 2026-09-30T10:00 | Heikin-Ashi | sell | DOGE-USD | 13.68 | -0.04 | exit signal |
| 2026-09-30T09:47 | Triple EMA stack | buy | SOL-USD | 3.89 | — | rebalance up |
| 2026-09-30T09:47 | Triple EMA stack | sell | ETH-USD | 3.89 | -0.01 | rebalance down |
| 2026-09-30T09:45 | Heikin-Ashi | buy | XRP-USD | 10.27 | — | rebalance up |
| 2026-09-30T09:45 | Heikin-Ashi | sell | SOL-USD | 13.68 | -0.02 | exit signal |
| 2026-09-30T09:45 | Heikin-Ashi | sell | ETH-USD | 17.11 | -0.04 | exit signal |
| 2026-09-30T09:45 | Triple EMA stack | buy | SOL-USD | 7.83 | — | entry signal |
| 2026-09-30T09:45 | Triple EMA stack | sell | XRP-USD | 3.93 | -0.00 | rebalance down |
| 2026-09-30T09:45 | Triple EMA stack | sell | DOGE-USD | 3.90 | -0.01 | rebalance down |
| 2026-09-30T09:40 | OBV trend | buy | SOL-USD | 7.27 | — | entry signal |
| 2026-09-30T09:40 | OBV trend | sell | ETH-USD | 3.62 | -0.01 | rebalance down |
| 2026-09-30T09:40 | OBV trend | sell | DOGE-USD | 3.65 | -0.00 | rebalance down |
| 2026-09-30T09:40 | Heikin-Ashi | buy | XRP-USD | 3.43 | — | rebalance up |
| 2026-09-30T09:40 | Heikin-Ashi | sell | DOGE-USD | 3.43 | -0.00 | rebalance down |
| 2026-09-30T09:40 | EMA 20/50 cross | buy | SOL-USD | 12.66 | — | entry signal |
| 2026-09-30T09:40 | EMA 20/50 cross | sell | XRP-USD | 4.24 | -0.00 | rebalance down |
| 2026-09-30T09:40 | EMA 20/50 cross | sell | ETH-USD | 4.22 | -0.01 | rebalance down |
| 2026-09-30T09:40 | EMA 20/50 cross | sell | DOGE-USD | 4.20 | -0.00 | rebalance down |
| 2026-09-30T09:36 | Keltner breakout | buy | SOL-USD | 8.52 | — | rebalance up |
| 2026-09-30T09:36 | Keltner breakout | sell | XRP-USD | 4.27 | -0.01 | rebalance down |
| 2026-09-30T09:36 | Keltner breakout | sell | ETH-USD | 4.27 | -0.01 | rebalance down |
| 2026-09-30T09:36 | Bollinger breakout | buy | DOGE-USD | 7.90 | — | rebalance up |
| 2026-09-30T09:36 | Bollinger breakout | sell | SOL-USD | 3.96 | -0.01 | rebalance down |
| 2026-09-30T09:36 | Bollinger breakout | sell | ETH-USD | 3.95 | -0.01 | rebalance down |
| 2026-09-30T09:35 | Candlestick reversal | sell | DOGE-USD | 18.58 | 0.07 | target is flat |
| 2026-09-30T09:35 | Candlestick reversal | sell | BTC-USD | 18.21 | -0.02 | take-profit |
| 2026-09-30T09:35 | Volume breakout | buy | XRP-USD | 21.78 | — | entry signal |
| 2026-09-30T09:35 | Volume breakout | buy | SOL-USD | 21.78 | — | entry signal |
| 2026-09-30T09:35 | Volume breakout | buy | ETH-USD | 21.78 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
