# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T05:10:05.000209+00:00 · 6507 ticks

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
| Copy: Insider buying | 2026-09-30 | ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, ADRX 12%, BBD 12%, ENHA 12%, CX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.07 · VIX 16.04 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 4065 decisions in 813 calls, $0.0570 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T05:10 | 1 / 3 / 1 | XRP-USD 22% |  |
| Breezy | 2026-09-30T05:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T05:10 | 3 / 1 / 1 | XRP-USD 40%, BTC-USD 30% |  |

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
| 4 | Copy: Congress Democrats (NANC) | copy | 100.07 | 0.07 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.65 | -7.93 | 7 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Copy: Warren Buffett (BRK-B) | copy | 99.73 | -0.27 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 9 | Agent | meta | 99.68 | -0.32 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 11 | Hold BTC | benchmark | 99.64 | -0.36 | 0 | — | 29.89 | 3.74 | -8.68 | 1 |
| 12 | Agent (aggressive) | meta | 99.57 | -0.43 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.50 | -0.50 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.42 | -0.58 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.41 | -0.59 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.14 | -0.86 | 20 | 25.0 | -13.02 | -4.40 | -14.79 | 122 |
| 18 | Daily: Bullish score | daily | 99.07 | -0.93 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.02 | -0.98 | 7 | 57.1 | 2.90 | 0.80 | -7.03 | 123 |
| 20 | Z-score reversion · 1h | reversion | 98.89 | -1.11 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.87 | -1.13 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Stochastic reversion · 1h | reversion | 98.55 | -1.45 | 26 | 53.8 | -13.84 | -3.03 | -15.02 | 330 |
| 24 | Williams %R · 1h | reversion | 98.54 | -1.46 | 40 | 45.0 | -17.92 | -3.31 | -19.41 | 488 |
| 25 | Candlestick reversal · 1h | reversion | 98.48 | -1.52 | 25 | 20.0 | -28.03 | -6.85 | -28.65 | 493 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 98.45 | -1.55 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 27 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.27 | -1.73 | 35 | 34.3 | 0.39 | 0.23 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.87 | -2.13 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.80 | -2.19 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | Max aggression: 5-day momentum | meta | 97.71 | -2.29 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 34 | EMA 20/50 cross · 1h | trend | 97.68 | -2.32 | 13 | 7.7 | 16.51 | 1.96 | -14.13 | 126 |
| 35 | Bollinger reversion · 1h | reversion | 97.29 | -2.71 | 22 | 27.3 | -17.88 | -4.94 | -18.49 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.08 | -2.92 | 9 | 11.1 | 15.55 | 2.73 | -5.11 | 92 |
| 38 | Max aggression: 1-day momentum | meta | 96.68 | -3.33 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.63 | -3.37 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.55 | -3.45 | 18 | 5.6 | 1.94 | 0.46 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.41 | -3.59 | 140 | 12.9 | -1.18 | -0.04 | -13.17 | 379 |
| 42 | Trend pullback · 1h | trend | 96.28 | -3.72 | 28 | 10.7 | -29.16 | -7.16 | -29.64 | 148 |
| 43 | MACD cross · 1h | trend | 96.14 | -3.86 | 40 | 10.0 | -18.91 | -3.20 | -21.93 | 462 |
| 44 | Parabolic SAR · 1h | trend | 95.92 | -4.08 | 26 | 11.5 | -7.94 | -0.99 | -18.82 | 293 |
| 45 | Donchian 55/20 · 1h | breakout | 95.86 | -4.14 | 12 | 0.0 | 4.53 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 47 | MFI reversion · 1h | reversion | 95.44 | -4.56 | 44 | 13.6 | -9.88 | -1.81 | -17.20 | 129 |
| 48 | Ichimoku · 1h | trend | 95.18 | -4.82 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 49 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.32 | -27.90 | -50.38 | 608 |
| 50 | Bollinger breakout · 1h | breakout | 94.92 | -5.08 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.30 | -5.70 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 53 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 54 | ADX DI cross · 1h | trend | 94.04 | -5.96 | 30 | 6.7 | -16.11 | -2.99 | -17.94 | 255 |
| 55 | MACD zero-line · 1h | trend | 94.03 | -5.97 | 20 | 5.0 | -5.79 | -0.62 | -14.64 | 224 |
| 56 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | -0.03 | 0.23 | -18.68 | 213 |
| 57 | Triple EMA stack · 1h | trend | 93.85 | -6.15 | 30 | 6.7 | -6.79 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.70 | -6.30 | 103 | 12.6 | -34.92 | -5.28 | -35.35 | 1236 |
| 59 | EMA 9/21 cross · 1h | trend | 92.90 | -7.10 | 44 | 11.4 | -4.08 | -0.36 | -16.92 | 308 |
| 60 | Heikin-Ashi · 1h | trend | 92.71 | -7.29 | 45 | 11.1 | -26.26 | -3.97 | -30.63 | 671 |
| 61 | OBV trend · 1h | momentum | 92.50 | -7.50 | 54 | 7.4 | -13.07 | -1.44 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.13 | -71.11 | 1470 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 89.18 | -10.82 | 96 | 14.6 | -59.60 | -18.43 | -59.69 | 1191 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.99 | -19.88 | -62.05 | 897 |
| 66 | ROC + volume | momentum | 86.90 | -13.10 | 150 | 18.7 | -72.04 | -17.61 | -72.05 | 1628 |
| 67 | Donchian 55/20 | breakout | 86.49 | -13.51 | 99 | 15.2 | -68.29 | -15.67 | -68.29 | 1302 |
| 68 | EMA 20/50 cross | trend | 85.54 | -14.46 | 129 | 15.5 | -78.80 | -17.55 | -78.80 | 1467 |
| 69 | Ichimoku | trend | 85.31 | -14.69 | 114 | 8.8 | -80.40 | -25.81 | -80.40 | 1741 |
| 70 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.84 | -34.03 | -84.84 | 1898 |
| 71 | VWAP reversion | reversion | 84.55 | -15.45 | 138 | 22.5 | -71.61 | -17.52 | -71.94 | 1398 |
| 72 | Z-score reversion | reversion | 84.33 | -15.67 | 185 | 31.9 | -84.48 | -27.24 | -84.48 | 2098 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MACD zero-line | trend | 81.11 | -18.89 | 208 | 15.9 | -91.76 | -35.42 | -91.77 | 2353 |
| 76 | Supertrend | trend | 81.02 | -18.98 | 185 | 17.3 | -87.52 | -24.68 | -87.52 | 1956 |
| 77 | MFI reversion | reversion | 80.47 | -19.53 | 187 | 19.3 | -88.06 | -35.12 | -88.09 | 2149 |
| 78 | Donchian 20/10 | breakout | 80.33 | -19.67 | 209 | 17.2 | -90.89 | -29.40 | -90.89 | 2676 |
| 79 | Bollinger breakout | breakout | 79.93 | -20.07 | 210 | 16.2 | -93.88 | -41.40 | -93.88 | 2864 |
| 80 | RSI momentum | momentum | 79.04 | -20.95 | 202 | 12.9 | -90.51 | -29.05 | -90.51 | 2381 |
| 81 | Triple EMA stack | trend | 78.83 | -21.17 | 222 | 14.9 | -93.14 | -35.83 | -93.14 | 2621 |
| 82 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.65 | -33.62 | -90.65 | 2263 |
| 83 | ADX DI cross | trend | 78.39 | -21.61 | 202 | 7.9 | -89.36 | -44.99 | -89.39 | 2110 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.31 | -39.61 | -96.32 | 3606 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.61 | -29.59 | -94.62 | 2647 |
| 86 | Stochastic reversion | reversion | 75.49 | -24.51 | 333 | 23.7 | -95.91 | -44.46 | -95.91 | 4055 |
| 87 | Candlestick reversal | reversion | 75.13 | -24.88 | 278 | 12.6 | -99.36 | -48.81 | -99.36 | 5585 |
| 88 | EMA 9/21 cross | trend | 74.80 | -25.20 | 291 | 16.5 | -97.44 | -41.30 | -97.44 | 3536 |
| 89 | Bollinger reversion | reversion | 73.65 | -26.36 | 317 | 15.1 | -95.79 | -43.47 | -95.79 | 3686 |
| 90 | OBV trend | momentum | 73.34 | -26.66 | 284 | 14.8 | -95.93 | -48.04 | -95.93 | 3550 |
| 91 | Parabolic SAR | trend | 71.88 | -28.12 | 275 | 12.7 | -97.00 | -53.87 | -97.00 | 3628 |
| 92 | CCI reversion | reversion | 71.31 | -28.69 | 252 | 10.7 | -98.47 | -50.13 | -98.48 | 4703 |
| 93 | MACD cross | trend | 70.41 | -29.59 | 285 | 13.3 | -99.72 | -63.79 | -99.72 | 6078 |
| 94 | VWAP momentum | momentum | 70.15 | -29.86 | 396 | 9.6 | -98.51 | -35.95 | -98.51 | 5213 |
| 95 | Heikin-Ashi | trend | 69.76 | -30.24 | 241 | 3.3 | -99.89 | -76.27 | -99.89 | 8298 |
| 96 | Williams %R | reversion | 69.67 | -30.33 | 354 | 20.3 | -99.53 | -57.18 | -99.53 | 6111 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T05:10 | MFI reversion | sell | DOGE-USD | 20.05 | -0.12 | exit signal |
| 2026-09-30T05:10 | VWAP momentum | buy | XRP-USD | 17.55 | — | entry signal |
| 2026-09-30T05:10 | MACD cross | buy | XRP-USD | 17.62 | — | entry signal |
| 2026-09-30T05:06 | Williams %R | buy | ETH-USD | 3.48 | — | rebalance up |
| 2026-09-30T05:06 | Williams %R | sell | SOL-USD | 3.48 | -0.03 | rebalance down |
| 2026-09-30T05:05 | CCI reversion | buy | ETH-USD | 17.76 | — | entry signal |
| 2026-09-30T05:05 | Williams %R | buy | ETH-USD | 10.49 | — | entry signal |
| 2026-09-30T05:05 | Williams %R | buy | DOGE-USD | 13.97 | — | entry signal |
| 2026-09-30T05:05 | Williams %R | buy | BTC-USD | 13.97 | — | entry signal |
| 2026-09-30T05:05 | Williams %R | sell | XRP-USD | 3.51 | -0.02 | rebalance down |
| 2026-09-30T05:05 | Z-score reversion | buy | SOL-USD | 21.11 | — | entry signal |
| 2026-09-30T05:05 | Bollinger reversion | buy | SOL-USD | 18.45 | — | entry signal |
| 2026-09-30T05:05 | Bollinger reversion | buy | BTC-USD | 18.45 | — | entry signal |
| 2026-09-30T05:05 | Candlestick reversal | buy | SOL-USD | 18.72 | — | entry signal |
| 2026-09-30T05:05 | Candlestick reversal | buy | BTC-USD | 18.81 | — | entry signal |
| 2026-09-30T05:00 | CCI reversion | sell | SOL-USD | 17.74 | -0.20 | stop-loss |
| 2026-09-30T05:00 | Stochastic reversion | buy | SOL-USD | 18.88 | — | entry signal |
| 2026-09-30T05:00 | Stochastic reversion | buy | BTC-USD | 18.88 | — | entry signal |
| 2026-09-30T05:00 | OBV trend | sell | SOL-USD | 18.17 | -0.22 | stop-loss |
| 2026-09-30T05:00 | MACD cross | sell | DOGE-USD | 17.58 | -0.15 | exit signal |
| 2026-09-30T04:55 | MACD cross | sell | XRP-USD | 17.59 | -0.13 | exit signal |
| 2026-09-30T04:50 | MACD cross | sell | BTC-USD | 17.62 | -0.12 | exit signal |
| 2026-09-30T04:50 | EMA 9/21 cross | sell | ETH-USD | 18.65 | -0.13 | exit signal |
| 2026-09-30T04:45 | Williams %R | buy | SOL-USD | 3.50 | — | rebalance up |
| 2026-09-30T04:45 | VWAP momentum | sell | XRP-USD | 17.46 | -0.12 | exit signal |
| 2026-09-30T04:40 | VWAP momentum | buy | XRP-USD | 17.58 | — | entry signal |
| 2026-09-30T04:40 | Parabolic SAR | sell | SOL-USD | 17.85 | -0.16 | exit signal |
| 2026-09-30T04:35 | VWAP momentum | sell | XRP-USD | 17.56 | -0.13 | exit signal |
| 2026-09-30T04:35 | VWAP momentum | sell | ETH-USD | 17.62 | -0.13 | exit signal |
| 2026-09-30T04:35 | VWAP momentum | sell | DOGE-USD | 17.52 | -0.14 | target is flat |
| 2026-09-30T04:35 | Heikin-Ashi | sell | XRP-USD | 17.39 | -0.12 | exit signal |
| 2026-09-30T04:35 | Heikin-Ashi | sell | DOGE-USD | 17.36 | -0.14 | exit signal |
| 2026-09-30T04:35 | MACD zero-line | sell | ETH-USD | 20.18 | -0.14 | exit signal |
| 2026-09-30T04:35 | MACD cross | sell | ETH-USD | 17.64 | -0.10 | exit signal |
| 2026-09-30T04:30 | Z-score reversion | buy | DOGE-USD | 21.14 | — | entry |
| 2026-09-30T04:25 | Williams %R | sell | DOGE-USD | 14.02 | -0.02 | exit signal |
| 2026-09-30T04:25 | Z-score reversion | sell | DOGE-USD | 21.13 | -0.03 | exit signal |
| 2026-09-30T04:25 | Candlestick reversal | sell | SOL-USD | 18.73 | -0.13 | exit signal |
| 2026-09-30T04:25 | Candlestick reversal | sell | BTC-USD | 18.77 | -0.09 | exit signal |
| 2026-09-30T04:25 | VWAP momentum | buy | DOGE-USD | 17.66 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
