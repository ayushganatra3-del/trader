# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T07:40:05.000127+00:00 · 6635 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.64 (-0.36%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.98 | -0.01 |

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

Today: 5985 decisions in 1197 calls, $0.0839 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T07:40 | 1 / 3 / 1 | DOGE-USD 14% |  |
| Breezy | 2026-09-30T07:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T07:40 | 5 / 0 / 0 | ETH-USD 38%, BTC-USD 34% |  |

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
| 7 | Copy: Congress Democrats (NANC) | copy | 99.86 | -0.14 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Agent | meta | 99.64 | -0.36 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 10 | Hold BTC | benchmark | 99.53 | -0.47 | 0 | — | 29.33 | 3.68 | -8.68 | 1 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 99.52 | -0.48 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 12 | Agent (aggressive) | meta | 99.46 | -0.54 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.29 | -0.71 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.20 | -0.80 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.20 | -0.80 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.03 | -0.97 | 20 | 25.0 | -12.98 | -4.39 | -14.76 | 122 |
| 18 | RSI(14) reversion · 1h | reversion | 98.96 | -1.04 | 7 | 57.1 | 6.29 | 1.61 | -7.03 | 117 |
| 19 | Daily: Bullish score | daily | 98.85 | -1.15 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 20 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 21 | Z-score reversion · 1h | reversion | 98.73 | -1.27 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Copy: Insider buying | copy | 98.68 | -1.32 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 24 | Williams %R · 1h | reversion | 98.37 | -1.63 | 40 | 45.0 | -17.82 | -3.29 | -19.41 | 488 |
| 25 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 26 | Stochastic reversion · 1h | reversion | 98.33 | -1.67 | 26 | 53.8 | -13.79 | -3.01 | -15.00 | 330 |
| 27 | Candlestick reversal · 1h | reversion | 98.27 | -1.73 | 25 | 20.0 | -25.67 | -6.43 | -26.70 | 483 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.24 | -1.76 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | CCI reversion · 1h | reversion | 98.06 | -1.95 | 35 | 34.3 | 0.47 | 0.24 | -12.41 | 410 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.71 | -2.29 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.59 | -2.41 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.53 | -2.47 | 13 | 7.7 | 16.22 | 1.93 | -14.13 | 127 |
| 34 | Max aggression: 5-day momentum | meta | 97.50 | -2.50 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Bollinger reversion · 1h | reversion | 97.08 | -2.92 | 22 | 27.3 | -17.88 | -4.94 | -18.50 | 313 |
| 37 | Squeeze breakout · 1h | breakout | 97.02 | -2.98 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 38 | Max aggression: 1-day momentum | meta | 96.47 | -3.53 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.43 | -3.58 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.38 | -3.62 | 18 | 5.6 | 1.96 | 0.47 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.22 | -3.78 | 140 | 12.9 | -1.32 | -0.06 | -13.19 | 406 |
| 42 | Trend pullback · 1h | trend | 96.13 | -3.87 | 28 | 10.7 | -29.16 | -7.16 | -29.64 | 148 |
| 43 | MACD cross · 1h | trend | 95.93 | -4.07 | 40 | 10.0 | -18.97 | -3.21 | -21.84 | 462 |
| 44 | Parabolic SAR · 1h | trend | 95.71 | -4.29 | 26 | 11.5 | -7.94 | -0.99 | -18.82 | 293 |
| 45 | Donchian 55/20 · 1h | breakout | 95.65 | -4.35 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 47 | MFI reversion · 1h | reversion | 95.24 | -4.76 | 44 | 13.6 | -9.85 | -1.80 | -17.20 | 129 |
| 48 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.28 | -27.84 | -50.33 | 607 |
| 49 | Ichimoku · 1h | trend | 95.08 | -4.92 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.82 | -5.17 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.14 | -5.86 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 53 | Donchian 20/10 · 1h | breakout | 94.03 | -5.97 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 54 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.03 | 0.23 | -18.68 | 213 |
| 55 | ADX DI cross · 1h | trend | 93.84 | -6.16 | 30 | 6.7 | -16.14 | -2.99 | -17.96 | 255 |
| 56 | Triple EMA stack · 1h | trend | 93.76 | -6.24 | 30 | 6.7 | -7.53 | -0.72 | -22.58 | 228 |
| 57 | MACD zero-line · 1h | trend | 93.75 | -6.25 | 21 | 4.8 | -5.66 | -0.61 | -14.64 | 223 |
| 58 | VWAP momentum · 1h | momentum | 93.50 | -6.50 | 103 | 12.6 | -34.97 | -5.29 | -35.50 | 1237 |
| 59 | Heikin-Ashi · 1h | trend | 92.61 | -7.39 | 45 | 11.1 | -26.26 | -3.97 | -30.63 | 671 |
| 60 | EMA 9/21 cross · 1h | trend | 92.59 | -7.41 | 45 | 11.1 | -4.29 | -0.39 | -16.92 | 308 |
| 61 | OBV trend · 1h | momentum | 92.30 | -7.70 | 54 | 7.4 | -13.29 | -1.47 | -25.19 | 318 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.13 | -71.11 | 1470 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 88.51 | -11.49 | 99 | 14.1 | -60.07 | -18.67 | -60.07 | 1194 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.89 | -19.83 | -61.96 | 895 |
| 66 | ROC + volume | momentum | 86.90 | -13.10 | 150 | 18.7 | -72.02 | -17.59 | -72.02 | 1626 |
| 67 | Donchian 55/20 | breakout | 86.18 | -13.82 | 100 | 15.0 | -68.23 | -15.70 | -68.23 | 1301 |
| 68 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.82 | -34.04 | -84.82 | 1896 |
| 69 | Ichimoku | trend | 85.15 | -14.85 | 115 | 8.7 | -80.31 | -25.78 | -80.31 | 1738 |
| 70 | EMA 20/50 cross | trend | 84.79 | -15.21 | 132 | 15.2 | -78.98 | -17.67 | -78.98 | 1471 |
| 71 | VWAP reversion | reversion | 83.95 | -16.05 | 143 | 21.7 | -71.73 | -17.62 | -72.01 | 1400 |
| 72 | Z-score reversion | reversion | 83.76 | -16.24 | 192 | 30.7 | -84.57 | -27.45 | -84.59 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.30 | -19.70 | 188 | 19.1 | -88.10 | -35.32 | -88.11 | 2150 |
| 76 | MACD zero-line | trend | 80.00 | -20.00 | 213 | 15.5 | -91.87 | -36.00 | -91.87 | 2360 |
| 77 | Donchian 20/10 | breakout | 79.70 | -20.30 | 212 | 17.0 | -90.96 | -29.63 | -90.96 | 2678 |
| 78 | Supertrend | trend | 79.66 | -20.34 | 190 | 16.8 | -87.68 | -24.94 | -87.68 | 1962 |
| 79 | Bollinger breakout | breakout | 79.26 | -20.74 | 214 | 15.9 | -93.89 | -42.00 | -93.89 | 2863 |
| 80 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.58 | -33.23 | -90.58 | 2259 |
| 81 | Triple EMA stack | trend | 78.35 | -21.65 | 224 | 14.7 | -93.15 | -36.07 | -93.15 | 2621 |
| 82 | ADX DI cross | trend | 78.16 | -21.84 | 203 | 7.9 | -89.35 | -44.98 | -89.37 | 2112 |
| 83 | RSI momentum | momentum | 78.13 | -21.87 | 206 | 12.6 | -90.59 | -29.38 | -90.59 | 2384 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.28 | -39.10 | -96.28 | 3599 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.54 | -29.50 | -94.55 | 2640 |
| 86 | Stochastic reversion | reversion | 74.93 | -25.07 | 342 | 23.4 | -95.93 | -44.85 | -95.94 | 4057 |
| 87 | Candlestick reversal | reversion | 74.18 | -25.82 | 289 | 12.1 | -99.36 | -49.33 | -99.36 | 5591 |
| 88 | EMA 9/21 cross | trend | 73.91 | -26.09 | 296 | 16.2 | -97.44 | -41.55 | -97.44 | 3536 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.79 | -43.47 | -95.80 | 3687 |
| 90 | OBV trend | momentum | 72.63 | -27.36 | 287 | 14.6 | -95.94 | -48.59 | -95.94 | 3550 |
| 91 | Parabolic SAR | trend | 71.30 | -28.70 | 279 | 12.5 | -97.00 | -54.61 | -97.00 | 3628 |
| 92 | CCI reversion | reversion | 71.15 | -28.85 | 259 | 10.4 | -98.46 | -49.60 | -98.47 | 4702 |
| 93 | MACD cross | trend | 69.66 | -30.34 | 290 | 13.1 | -99.72 | -64.54 | -99.72 | 6080 |
| 94 | Heikin-Ashi | trend | 69.06 | -30.94 | 246 | 3.3 | -99.89 | -77.58 | -99.89 | 8301 |
| 95 | VWAP momentum | momentum | 68.92 | -31.08 | 405 | 9.4 | -98.53 | -36.08 | -98.53 | 5222 |
| 96 | Williams %R | reversion | 68.77 | -31.23 | 367 | 19.9 | -99.53 | -57.42 | -99.53 | 6110 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T07:40 | CCI reversion | buy | XRP-USD | 14.19 | — | rebalance up |
| 2026-09-30T07:40 | CCI reversion | buy | DOGE-USD | 3.57 | — | rebalance up |
| 2026-09-30T07:40 | CCI reversion | sell | ETH-USD | 17.75 | -0.05 | exit signal |
| 2026-09-30T07:40 | CCI reversion | sell | BTC-USD | 17.74 | -0.04 | exit signal |
| 2026-09-30T07:40 | Candlestick reversal | sell | BTC-USD | 18.55 | -0.04 | take-profit |
| 2026-09-30T07:40 | RSI momentum | buy | BTC-USD | 19.55 | — | entry signal |
| 2026-09-30T07:40 | VWAP momentum | buy | DOGE-USD | 17.14 | — | entry signal |
| 2026-09-30T07:40 | Supertrend | buy | ETH-USD | 19.93 | — | entry signal |
| 2026-09-30T07:40 | MACD zero-line | buy | XRP-USD | 20.06 | — | entry signal |
| 2026-09-30T07:40 | MACD zero-line | buy | ETH-USD | 20.06 | — | entry signal |
| 2026-09-30T07:40 | MACD zero-line | buy | DOGE-USD | 20.06 | — | entry signal |
| 2026-09-30T07:40 | MACD zero-line | buy | BTC-USD | 20.06 | — | entry signal |
| 2026-09-30T07:35 | OBV trend | buy | XRP-USD | 18.17 | — | entry signal |
| 2026-09-30T07:35 | VWAP momentum | buy | BTC-USD | 17.26 | — | entry signal |
| 2026-09-30T07:35 | VWAP momentum | sell | DOGE-USD | 17.18 | -0.15 | exit signal |
| 2026-09-30T07:35 | Triple EMA stack | buy | XRP-USD | 19.60 | — | entry signal |
| 2026-09-30T07:35 | EMA 20/50 cross | buy | XRP-USD | 21.21 | — | entry signal |
| 2026-09-30T07:35 | EMA 9/21 cross | buy | XRP-USD | 18.50 | — | entry signal |
| 2026-09-30T07:35 | EMA 9/21 cross | buy | ETH-USD | 18.50 | — | entry signal |
| 2026-09-30T07:35 | EMA 9/21 cross | buy | BTC-USD | 18.50 | — | entry signal |
| 2026-09-30T07:30 | Candlestick reversal | sell | SOL-USD | 18.56 | -0.04 | exit signal |
| 2026-09-30T07:30 | VWAP momentum | sell | BTC-USD | 17.21 | -0.11 | exit signal |
| 2026-09-30T07:30 | Heikin-Ashi | buy | XRP-USD | 13.84 | — | entry signal |
| 2026-09-30T07:30 | Heikin-Ashi | buy | SOL-USD | 13.84 | — | entry signal |
| 2026-09-30T07:30 | Heikin-Ashi | buy | ETH-USD | 13.84 | — | entry signal |
| 2026-09-30T07:30 | Heikin-Ashi | buy | DOGE-USD | 13.84 | — | entry signal |
| 2026-09-30T07:30 | Heikin-Ashi | buy | BTC-USD | 13.84 | — | entry signal |
| 2026-09-30T07:30 | ADX DI cross | buy | SOL-USD | 3.90 | — | rebalance up |
| 2026-09-30T07:30 | ADX DI cross | sell | ETH-USD | 3.90 | -0.02 | rebalance down |
| 2026-09-30T07:30 | MACD cross | buy | XRP-USD | 10.45 | — | entry signal |
| 2026-09-30T07:30 | MACD cross | sell | ETH-USD | 3.47 | -0.02 | rebalance down |
| 2026-09-30T07:30 | MACD cross | sell | DOGE-USD | 3.48 | -0.02 | rebalance down |
| 2026-09-30T07:30 | MACD cross | sell | BTC-USD | 3.48 | -0.02 | rebalance down |
| 2026-09-30T07:30 | EMA 9/21 cross | buy | DOGE-USD | 18.51 | — | entry signal |
| 2026-09-30T07:26 | ADX DI cross | buy | SOL-USD | 3.90 | — | rebalance up |
| 2026-09-30T07:26 | ADX DI cross | sell | BTC-USD | 3.90 | -0.02 | rebalance down |
| 2026-09-30T07:25 | CCI reversion | buy | XRP-USD | 3.65 | — | entry |
| 2026-09-30T07:25 | CCI reversion | sell | DOGE-USD | 3.57 | 0.01 | rebalance down |
| 2026-09-30T07:25 | Williams %R | sell | XRP-USD | 17.18 | -0.07 | exit signal |
| 2026-09-30T07:25 | Williams %R | sell | SOL-USD | 17.17 | -0.09 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
