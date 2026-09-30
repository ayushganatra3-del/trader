# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T03:10:05.000147+00:00 · 6398 ticks

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

Today: 2430 decisions in 486 calls, $0.0341 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T03:10 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-09-30T03:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T03:10 | 3 / 1 / 1 | SOL-USD 30%, ETH-USD 28% |  |

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
| 8 | Hold BTC | benchmark | 99.72 | -0.28 | 0 | — | 29.75 | 3.72 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.72 | -0.28 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Agent | meta | 99.68 | -0.32 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 12 | Agent (aggressive) | meta | 99.56 | -0.44 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.50 | -0.50 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.41 | -0.59 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.40 | -0.60 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.14 | -0.86 | 20 | 25.0 | -13.00 | -4.40 | -14.77 | 122 |
| 18 | Daily: Bullish score | daily | 99.06 | -0.94 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.02 | -0.98 | 7 | 57.1 | 1.58 | 0.48 | -7.03 | 126 |
| 20 | Z-score reversion · 1h | reversion | 98.89 | -1.11 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.86 | -1.14 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Williams %R · 1h | reversion | 98.56 | -1.44 | 40 | 45.0 | -17.82 | -3.29 | -19.41 | 488 |
| 24 | Stochastic reversion · 1h | reversion | 98.54 | -1.46 | 26 | 53.8 | -13.90 | -3.04 | -15.09 | 330 |
| 25 | Candlestick reversal · 1h | reversion | 98.53 | -1.47 | 23 | 21.7 | -28.22 | -6.89 | -28.90 | 494 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.44 | -1.56 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.26 | -1.74 | 35 | 34.3 | 0.43 | 0.24 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.86 | -2.14 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.80 | -2.20 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | Max aggression: 5-day momentum | meta | 97.70 | -2.30 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 34 | EMA 20/50 cross · 1h | trend | 97.67 | -2.33 | 13 | 7.7 | 16.56 | 1.97 | -14.13 | 126 |
| 35 | Bollinger reversion · 1h | reversion | 97.28 | -2.72 | 22 | 27.3 | -17.88 | -4.94 | -18.50 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.07 | -2.93 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 38 | Max aggression: 1-day momentum | meta | 96.67 | -3.33 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.63 | -3.37 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.56 | -3.44 | 18 | 5.6 | 1.96 | 0.47 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.48 | -3.52 | 139 | 12.9 | 1.67 | 0.44 | -12.00 | 387 |
| 42 | Trend pullback · 1h | trend | 96.28 | -3.72 | 28 | 10.7 | -29.16 | -7.16 | -29.64 | 148 |
| 43 | MACD cross · 1h | trend | 96.13 | -3.87 | 40 | 10.0 | -18.50 | -3.13 | -21.66 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.91 | -4.09 | 26 | 11.5 | -7.81 | -0.97 | -18.82 | 293 |
| 45 | Donchian 55/20 · 1h | breakout | 95.85 | -4.15 | 12 | 0.0 | 4.53 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 47 | MFI reversion · 1h | reversion | 95.55 | -4.45 | 44 | 13.6 | -9.62 | -1.75 | -17.20 | 128 |
| 48 | Three white soldiers | momentum | 95.26 | -4.74 | 43 | 18.6 | -50.28 | -27.80 | -50.38 | 608 |
| 49 | Ichimoku · 1h | trend | 95.18 | -4.82 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.92 | -5.08 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.29 | -5.71 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 53 | MACD zero-line · 1h | trend | 94.23 | -5.77 | 20 | 5.0 | -5.41 | -0.57 | -14.64 | 223 |
| 54 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | ADX DI cross · 1h | trend | 94.04 | -5.96 | 30 | 6.7 | -15.99 | -2.96 | -17.81 | 254 |
| 56 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | -0.03 | 0.23 | -18.68 | 213 |
| 57 | Triple EMA stack · 1h | trend | 93.84 | -6.16 | 30 | 6.7 | -6.79 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.70 | -6.30 | 103 | 12.6 | -34.83 | -5.26 | -35.29 | 1236 |
| 59 | EMA 9/21 cross · 1h | trend | 93.05 | -6.95 | 44 | 11.4 | -3.92 | -0.34 | -16.92 | 308 |
| 60 | Heikin-Ashi · 1h | trend | 92.71 | -7.29 | 45 | 11.1 | -26.45 | -4.01 | -30.63 | 672 |
| 61 | OBV trend · 1h | momentum | 92.49 | -7.51 | 54 | 7.4 | -13.09 | -1.44 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.11 | -21.24 | -71.16 | 1473 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 89.18 | -10.82 | 96 | 14.6 | -59.81 | -18.47 | -59.85 | 1193 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.99 | -19.88 | -62.05 | 897 |
| 66 | ROC + volume | momentum | 86.90 | -13.10 | 150 | 18.7 | -72.04 | -17.61 | -72.05 | 1628 |
| 67 | Donchian 55/20 | breakout | 86.89 | -13.11 | 97 | 15.5 | -68.15 | -15.58 | -68.18 | 1304 |
| 68 | EMA 20/50 cross | trend | 85.94 | -14.06 | 127 | 15.7 | -78.85 | -17.54 | -78.87 | 1473 |
| 69 | Ichimoku | trend | 85.31 | -14.69 | 114 | 8.8 | -80.52 | -25.87 | -80.52 | 1746 |
| 70 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.84 | -34.02 | -84.84 | 1898 |
| 71 | Z-score reversion | reversion | 84.74 | -15.26 | 183 | 32.2 | -84.43 | -27.11 | -84.43 | 2096 |
| 72 | VWAP reversion | reversion | 84.59 | -15.41 | 138 | 22.5 | -71.71 | -17.63 | -71.94 | 1401 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 81.49 | -18.51 | 182 | 17.6 | -87.47 | -24.56 | -87.48 | 1959 |
| 76 | MACD zero-line | trend | 81.35 | -18.65 | 206 | 16.0 | -91.82 | -35.32 | -91.82 | 2358 |
| 77 | Donchian 20/10 | breakout | 80.64 | -19.36 | 207 | 17.4 | -90.87 | -29.26 | -90.89 | 2677 |
| 78 | MFI reversion | reversion | 80.58 | -19.43 | 186 | 19.4 | -88.12 | -35.38 | -88.14 | 2154 |
| 79 | Bollinger breakout | breakout | 79.93 | -20.07 | 210 | 16.2 | -93.91 | -41.34 | -93.91 | 2866 |
| 80 | Triple EMA stack | trend | 79.37 | -20.63 | 219 | 15.1 | -93.08 | -35.49 | -93.09 | 2620 |
| 81 | RSI momentum | momentum | 79.35 | -20.65 | 200 | 13.0 | -90.43 | -28.90 | -90.46 | 2381 |
| 82 | Trend pullback | trend | 79.24 | -20.76 | 170 | 17.1 | -90.69 | -33.72 | -90.69 | 2267 |
| 83 | ADX DI cross | trend | 78.78 | -21.21 | 200 | 8.0 | -89.44 | -45.02 | -89.44 | 2113 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.35 | -40.15 | -96.35 | 3614 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.62 | -29.59 | -94.63 | 2649 |
| 86 | Stochastic reversion | reversion | 75.69 | -24.31 | 332 | 23.8 | -95.91 | -44.48 | -95.92 | 4056 |
| 87 | Candlestick reversal | reversion | 75.51 | -24.49 | 276 | 12.7 | -99.36 | -48.51 | -99.36 | 5582 |
| 88 | EMA 9/21 cross | trend | 75.49 | -24.51 | 286 | 16.8 | -97.44 | -40.95 | -97.44 | 3539 |
| 89 | Bollinger reversion | reversion | 74.13 | -25.87 | 312 | 15.4 | -95.77 | -43.11 | -95.77 | 3682 |
| 90 | OBV trend | momentum | 73.92 | -26.08 | 281 | 14.9 | -95.91 | -47.41 | -95.91 | 3550 |
| 91 | Parabolic SAR | trend | 72.04 | -27.96 | 274 | 12.8 | -97.00 | -53.58 | -97.00 | 3631 |
| 92 | CCI reversion | reversion | 72.03 | -27.97 | 249 | 10.8 | -98.46 | -49.59 | -98.46 | 4701 |
| 93 | VWAP momentum | momentum | 71.73 | -28.27 | 384 | 9.9 | -98.49 | -35.64 | -98.49 | 5210 |
| 94 | MACD cross | trend | 71.21 | -28.79 | 278 | 13.7 | -99.72 | -62.66 | -99.72 | 6076 |
| 95 | Williams %R | reversion | 70.44 | -29.56 | 349 | 20.6 | -99.52 | -56.62 | -99.52 | 6110 |
| 96 | Heikin-Ashi | trend | 70.02 | -29.98 | 239 | 3.3 | -99.90 | -75.80 | -99.90 | 8302 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T03:10 | Parabolic SAR | sell | XRP-USD | 17.90 | -0.14 | exit signal |
| 2026-09-30T03:10 | MACD zero-line | buy | ETH-USD | 20.35 | — | entry signal |
| 2026-09-30T03:05 | Heikin-Ashi | sell | ETH-USD | 17.43 | -0.11 | exit signal |
| 2026-09-30T03:05 | ADX DI cross | sell | DOGE-USD | 19.63 | -0.14 | exit signal |
| 2026-09-30T03:05 | MACD cross | sell | XRP-USD | 17.73 | -0.13 | exit signal |
| 2026-09-30T03:05 | EMA 9/21 cross | sell | DOGE-USD | 18.79 | -0.15 | exit signal |
| 2026-09-30T03:00 | MACD zero-line · 1h | buy | SOL-USD | 23.57 | — | entry signal |
| 2026-09-30T03:00 | Candlestick reversal | sell | BTC-USD | 18.85 | -0.13 | time stop |
| 2026-09-30T03:00 | VWAP momentum | sell | DOGE-USD | 17.85 | -0.13 | exit signal |
| 2026-09-30T03:00 | EMA 20/50 cross | sell | DOGE-USD | 21.38 | -0.16 | exit signal |
| 2026-09-30T02:55 | CCI reversion | sell | ETH-USD | 17.99 | -0.07 | exit signal |
| 2026-09-30T02:55 | Williams %R | sell | ETH-USD | 17.58 | -0.08 | exit signal |
| 2026-09-30T02:55 | Z-score reversion | sell | ETH-USD | 21.15 | -0.10 | exit signal |
| 2026-09-30T02:55 | RSI(14) reversion | sell | ETH-USD | 22.62 | -0.10 | exit signal |
| 2026-09-30T02:55 | MACD cross | buy | SOL-USD | 17.85 | — | entry signal |
| 2026-09-30T02:55 | MACD cross | buy | BTC-USD | 17.85 | — | entry signal |
| 2026-09-30T02:55 | EMA 20/50 cross | buy | DOGE-USD | 21.54 | — | entry signal |
| 2026-09-30T02:55 | EMA 9/21 cross | buy | ETH-USD | 18.87 | — | entry signal |
| 2026-09-30T02:50 | Bollinger reversion | sell | ETH-USD | 18.48 | -0.07 | exit signal |
| 2026-09-30T02:50 | Three white soldiers | buy | ETH-USD | 23.83 | — | entry signal |
| 2026-09-30T02:50 | VWAP momentum | buy | ETH-USD | 17.98 | — | entry signal |
| 2026-09-30T02:50 | Heikin-Ashi | buy | ETH-USD | 17.53 | — | entry signal |
| 2026-09-30T02:50 | MACD cross | buy | XRP-USD | 17.86 | — | entry signal |
| 2026-09-30T02:50 | EMA 9/21 cross | buy | DOGE-USD | 18.94 | — | entry signal |
| 2026-09-30T02:45 | CCI reversion | buy | BTC-USD | 18.04 | — | entry signal |
| 2026-09-30T02:45 | VWAP momentum | buy | DOGE-USD | 17.98 | — | entry signal |
| 2026-09-30T02:45 | Parabolic SAR | buy | XRP-USD | 18.05 | — | entry signal |
| 2026-09-30T02:45 | MACD cross | buy | ETH-USD | 17.87 | — | entry signal |
| 2026-09-30T02:40 | CCI reversion | buy | DOGE-USD | 18.05 | — | entry signal |
| 2026-09-30T02:40 | Williams %R | buy | DOGE-USD | 17.63 | — | entry signal |
| 2026-09-30T02:40 | Bollinger reversion | buy | ETH-USD | 18.55 | — | entry signal |
| 2026-09-30T02:40 | OBV trend | buy | SOL-USD | 18.48 | — | entry signal |
| 2026-09-30T02:40 | Trend pullback | buy | SOL-USD | 19.81 | — | entry signal |
| 2026-09-30T02:35 | Candlestick reversal | sell | ETH-USD | 18.82 | -0.15 | stop-loss |
| 2026-09-30T02:35 | Squeeze breakout | sell | XRP-USD | 22.24 | -0.14 | exit signal |
| 2026-09-30T02:35 | Squeeze breakout | sell | SOL-USD | 22.18 | -0.19 | exit signal |
| 2026-09-30T02:35 | Bollinger breakout | sell | XRP-USD | 19.99 | -0.12 | exit signal |
| 2026-09-30T02:35 | Bollinger breakout | sell | SOL-USD | 19.94 | -0.17 | exit signal |
| 2026-09-30T02:35 | OBV trend | sell | XRP-USD | 18.43 | -0.14 | exit signal |
| 2026-09-30T02:35 | Parabolic SAR | sell | SOL-USD | 17.98 | -0.14 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
