# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T05:40:05.000166+00:00 · 6536 ticks

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

Today: 4500 decisions in 900 calls, $0.0631 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T05:40 | 3 / 2 / 0 | XRP-USD 21%, SOL-USD 19% |  |
| Breezy | 2026-09-30T05:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T05:40 | 5 / 0 / 0 | SOL-USD 44%, XRP-USD 41% |  |

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
| 8 | Hold BTC | benchmark | 99.82 | -0.18 | 0 | — | 30.13 | 3.76 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.73 | -0.27 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Agent | meta | 99.68 | -0.32 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 12 | Agent (aggressive) | meta | 99.56 | -0.44 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.50 | -0.50 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.41 | -0.59 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.41 | -0.59 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.14 | -0.86 | 20 | 25.0 | -13.00 | -4.40 | -14.77 | 122 |
| 18 | Daily: Bullish score | daily | 99.06 | -0.94 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.02 | -0.98 | 7 | 57.1 | 2.96 | 0.81 | -7.03 | 123 |
| 20 | Z-score reversion · 1h | reversion | 98.89 | -1.11 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.86 | -1.14 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Williams %R · 1h | reversion | 98.60 | -1.41 | 40 | 45.0 | -17.76 | -3.28 | -19.41 | 488 |
| 24 | Stochastic reversion · 1h | reversion | 98.54 | -1.46 | 26 | 53.8 | -13.95 | -3.04 | -15.17 | 331 |
| 25 | Candlestick reversal · 1h | reversion | 98.47 | -1.52 | 25 | 20.0 | -28.01 | -6.84 | -28.64 | 493 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.44 | -1.56 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.26 | -1.74 | 35 | 34.3 | 0.49 | 0.25 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.86 | -2.13 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.80 | -2.20 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | Max aggression: 5-day momentum | meta | 97.70 | -2.30 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 34 | EMA 20/50 cross · 1h | trend | 97.67 | -2.33 | 13 | 7.7 | 16.51 | 1.96 | -14.13 | 126 |
| 35 | Bollinger reversion · 1h | reversion | 97.28 | -2.72 | 22 | 27.3 | -17.85 | -4.94 | -18.46 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.07 | -2.92 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 38 | Max aggression: 1-day momentum | meta | 96.67 | -3.33 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.63 | -3.37 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.58 | -3.42 | 18 | 5.6 | 1.98 | 0.47 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.44 | -3.56 | 140 | 12.9 | 1.27 | 0.38 | -12.33 | 373 |
| 42 | Trend pullback · 1h | trend | 96.28 | -3.72 | 28 | 10.7 | -29.16 | -7.16 | -29.64 | 148 |
| 43 | MACD cross · 1h | trend | 96.13 | -3.87 | 40 | 10.0 | -18.72 | -3.16 | -21.84 | 462 |
| 44 | Parabolic SAR · 1h | trend | 95.91 | -4.09 | 26 | 11.5 | -7.85 | -0.97 | -18.82 | 293 |
| 45 | Donchian 55/20 · 1h | breakout | 95.85 | -4.15 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 47 | MFI reversion · 1h | reversion | 95.52 | -4.48 | 44 | 13.6 | -9.72 | -1.77 | -17.20 | 129 |
| 48 | Ichimoku · 1h | trend | 95.18 | -4.82 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 49 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.32 | -27.90 | -50.38 | 608 |
| 50 | Bollinger breakout · 1h | breakout | 94.92 | -5.08 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.29 | -5.71 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 53 | MACD zero-line · 1h | trend | 94.17 | -5.83 | 20 | 5.0 | -5.64 | -0.60 | -14.64 | 224 |
| 54 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | ADX DI cross · 1h | trend | 94.04 | -5.96 | 30 | 6.7 | -16.11 | -2.99 | -17.94 | 255 |
| 56 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.01 | 0.23 | -18.68 | 214 |
| 57 | Triple EMA stack · 1h | trend | 93.85 | -6.15 | 30 | 6.7 | -6.79 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.70 | -6.30 | 103 | 12.6 | -34.92 | -5.28 | -35.35 | 1236 |
| 59 | EMA 9/21 cross · 1h | trend | 93.00 | -7.00 | 44 | 11.4 | -4.00 | -0.35 | -16.92 | 308 |
| 60 | Heikin-Ashi · 1h | trend | 92.71 | -7.29 | 45 | 11.1 | -26.26 | -3.97 | -30.63 | 671 |
| 61 | OBV trend · 1h | momentum | 92.49 | -7.51 | 54 | 7.4 | -13.07 | -1.44 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.13 | -71.11 | 1470 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 89.12 | -10.88 | 96 | 14.6 | -59.64 | -18.45 | -59.69 | 1192 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.99 | -19.88 | -62.05 | 897 |
| 66 | ROC + volume | momentum | 86.90 | -13.10 | 150 | 18.7 | -72.04 | -17.61 | -72.05 | 1628 |
| 67 | Donchian 55/20 | breakout | 86.49 | -13.51 | 99 | 15.2 | -68.21 | -15.66 | -68.21 | 1301 |
| 68 | EMA 20/50 cross | trend | 85.54 | -14.46 | 129 | 15.5 | -78.81 | -17.56 | -78.82 | 1468 |
| 69 | Ichimoku | trend | 85.31 | -14.69 | 114 | 8.8 | -80.40 | -25.81 | -80.40 | 1741 |
| 70 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.84 | -34.02 | -84.84 | 1898 |
| 71 | VWAP reversion | reversion | 84.52 | -15.48 | 139 | 22.3 | -71.66 | -17.57 | -71.94 | 1400 |
| 72 | Z-score reversion | reversion | 84.30 | -15.70 | 188 | 31.4 | -84.48 | -27.25 | -84.50 | 2098 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MACD zero-line | trend | 80.94 | -19.06 | 208 | 15.9 | -91.77 | -35.52 | -91.79 | 2358 |
| 76 | Supertrend | trend | 80.90 | -19.10 | 185 | 17.3 | -87.51 | -24.69 | -87.52 | 1957 |
| 77 | MFI reversion | reversion | 80.52 | -19.48 | 187 | 19.3 | -88.05 | -35.08 | -88.09 | 2149 |
| 78 | Donchian 20/10 | breakout | 80.16 | -19.84 | 209 | 17.2 | -90.90 | -29.47 | -90.91 | 2679 |
| 79 | Bollinger breakout | breakout | 79.76 | -20.23 | 210 | 16.2 | -93.90 | -41.56 | -93.90 | 2868 |
| 80 | RSI momentum | momentum | 78.87 | -21.13 | 202 | 12.9 | -90.53 | -29.13 | -90.53 | 2384 |
| 81 | Triple EMA stack | trend | 78.82 | -21.18 | 222 | 14.9 | -93.14 | -35.83 | -93.14 | 2622 |
| 82 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.65 | -33.62 | -90.65 | 2263 |
| 83 | ADX DI cross | trend | 78.47 | -21.53 | 202 | 7.9 | -89.35 | -44.84 | -89.37 | 2109 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.31 | -39.47 | -96.31 | 3605 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.59 | -29.62 | -94.61 | 2646 |
| 86 | Stochastic reversion | reversion | 75.37 | -24.63 | 337 | 23.4 | -95.91 | -44.57 | -95.91 | 4056 |
| 87 | Candlestick reversal | reversion | 75.06 | -24.94 | 281 | 12.5 | -99.35 | -48.68 | -99.36 | 5582 |
| 88 | EMA 9/21 cross | trend | 74.70 | -25.30 | 291 | 16.5 | -97.41 | -41.13 | -97.42 | 3535 |
| 89 | Bollinger reversion | reversion | 73.53 | -26.47 | 320 | 15.0 | -95.80 | -43.59 | -95.80 | 3687 |
| 90 | OBV trend | momentum | 73.34 | -26.66 | 284 | 14.8 | -95.94 | -48.05 | -95.94 | 3552 |
| 91 | Parabolic SAR | trend | 71.79 | -28.21 | 275 | 12.7 | -97.01 | -54.02 | -97.01 | 3633 |
| 92 | CCI reversion | reversion | 71.25 | -28.75 | 256 | 10.5 | -98.47 | -49.95 | -98.47 | 4701 |
| 93 | MACD cross | trend | 70.39 | -29.61 | 285 | 13.3 | -99.72 | -63.71 | -99.72 | 6079 |
| 94 | VWAP momentum | momentum | 69.95 | -30.05 | 397 | 9.6 | -98.50 | -35.89 | -98.50 | 5215 |
| 95 | Heikin-Ashi | trend | 69.57 | -30.43 | 241 | 3.3 | -99.90 | -76.89 | -99.90 | 8303 |
| 96 | Williams %R | reversion | 69.51 | -30.49 | 359 | 20.1 | -99.53 | -57.43 | -99.53 | 6112 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T05:40 | Squeeze breakout | buy | XRP-USD | 22.30 | — | entry signal |
| 2026-09-30T05:40 | RSI momentum | buy | ETH-USD | 19.75 | — | entry signal |
| 2026-09-30T05:40 | RSI momentum | buy | BTC-USD | 19.75 | — | entry signal |
| 2026-09-30T05:40 | VWAP momentum | buy | SOL-USD | 3.49 | — | rebalance up |
| 2026-09-30T05:40 | VWAP momentum | sell | DOGE-USD | 3.49 | -0.01 | rebalance down |
| 2026-09-30T05:40 | Heikin-Ashi | buy | XRP-USD | 3.51 | — | entry signal |
| 2026-09-30T05:40 | Heikin-Ashi | buy | DOGE-USD | 13.92 | — | entry signal |
| 2026-09-30T05:40 | MACD zero-line | buy | BTC-USD | 20.25 | — | entry signal |
| 2026-09-30T05:35 | CCI reversion | sell | ETH-USD | 17.69 | -0.07 | exit signal |
| 2026-09-30T05:35 | CCI reversion | sell | DOGE-USD | 17.86 | -0.08 | exit signal |
| 2026-09-30T05:35 | CCI reversion | sell | BTC-USD | 17.85 | -0.08 | exit signal |
| 2026-09-30T05:35 | Williams %R | sell | SOL-USD | 17.38 | -0.03 | exit signal |
| 2026-09-30T05:35 | Stochastic reversion | sell | SOL-USD | 18.86 | -0.02 | exit signal |
| 2026-09-30T05:35 | VWAP reversion | sell | BTC-USD | 21.08 | -0.07 | exit signal |
| 2026-09-30T05:35 | Z-score reversion | sell | SOL-USD | 21.05 | -0.06 | exit signal |
| 2026-09-30T05:35 | Bollinger breakout | buy | ETH-USD | 19.98 | — | entry signal |
| 2026-09-30T05:35 | Bollinger breakout | buy | DOGE-USD | 19.98 | — | entry signal |
| 2026-09-30T05:35 | Bollinger breakout | buy | BTC-USD | 19.98 | — | entry signal |
| 2026-09-30T05:35 | Donchian 20/10 | buy | XRP-USD | 20.08 | — | entry signal |
| 2026-09-30T05:35 | Donchian 20/10 | buy | ETH-USD | 20.08 | — | entry signal |
| 2026-09-30T05:35 | Donchian 20/10 | buy | BTC-USD | 20.08 | — | entry signal |
| 2026-09-30T05:35 | RSI momentum | buy | XRP-USD | 19.76 | — | entry signal |
| 2026-09-30T05:35 | VWAP momentum | buy | SOL-USD | 7.04 | — | entry signal |
| 2026-09-30T05:35 | VWAP momentum | buy | BTC-USD | 14.00 | — | entry signal |
| 2026-09-30T05:35 | VWAP momentum | sell | XRP-USD | 3.52 | -0.01 | rebalance down |
| 2026-09-30T05:35 | Heikin-Ashi | buy | SOL-USD | 17.44 | — | entry signal |
| 2026-09-30T05:35 | Heikin-Ashi | buy | ETH-USD | 17.44 | — | entry signal |
| 2026-09-30T05:35 | Heikin-Ashi | buy | BTC-USD | 17.44 | — | entry signal |
| 2026-09-30T05:35 | Supertrend | buy | XRP-USD | 20.25 | — | entry signal |
| 2026-09-30T05:35 | Supertrend | buy | BTC-USD | 20.25 | — | entry signal |
| 2026-09-30T05:35 | MACD zero-line | buy | ETH-USD | 20.28 | — | entry signal |
| 2026-09-30T05:35 | MACD zero-line | buy | DOGE-USD | 20.28 | — | entry signal |
| 2026-09-30T05:35 | EMA 9/21 cross | buy | ETH-USD | 18.70 | — | entry signal |
| 2026-09-30T05:35 | EMA 9/21 cross | buy | BTC-USD | 18.70 | — | entry signal |
| 2026-09-30T05:32 | MACD cross | buy | SOL-USD | 3.51 | — | rebalance up |
| 2026-09-30T05:32 | MACD cross | sell | DOGE-USD | 3.51 | -0.02 | rebalance down |
| 2026-09-30T05:31 | MACD cross | buy | SOL-USD | 3.51 | — | rebalance up |
| 2026-09-30T05:31 | MACD cross | sell | XRP-USD | 3.51 | -0.02 | rebalance down |
| 2026-09-30T05:30 | Williams %R | sell | ETH-USD | 13.89 | -0.06 | exit signal |
| 2026-09-30T05:30 | Williams %R | sell | BTC-USD | 13.89 | -0.07 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
