# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T06:40:05.000118+00:00 · 6582 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.65 (-0.35%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.99 | +0.00 |

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

Today: 5190 decisions in 1038 calls, $0.0727 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T06:40 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-09-30T06:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T06:40 | 4 / 1 / 0 | XRP-USD 24%, BTC-USD 22% |  |

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
| 7 | Copy: Congress Democrats (NANC) | copy | 99.93 | -0.07 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Agent | meta | 99.65 | -0.35 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.58 | -0.41 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 11 | Agent (aggressive) | meta | 99.49 | -0.51 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Hold SPY | benchmark | 99.36 | -0.64 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 99.27 | -0.73 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 99.26 | -0.73 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 15 | Hold BTC | benchmark | 99.19 | -0.81 | 0 | — | 29.41 | 3.68 | -8.68 | 1 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.07 | -0.93 | 20 | 25.0 | -12.98 | -4.39 | -14.76 | 122 |
| 18 | RSI(14) reversion · 1h | reversion | 98.98 | -1.02 | 7 | 57.1 | 3.68 | 0.98 | -7.03 | 123 |
| 19 | Daily: Bullish score | daily | 98.92 | -1.08 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 20 | Z-score reversion · 1h | reversion | 98.78 | -1.22 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 22 | Copy: Insider buying | copy | 98.74 | -1.26 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.67 | -4.73 | 182 |
| 24 | Stochastic reversion · 1h | reversion | 98.40 | -1.60 | 26 | 53.8 | -14.13 | -3.07 | -15.28 | 331 |
| 25 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 26 | Williams %R · 1h | reversion | 98.33 | -1.67 | 40 | 45.0 | -17.88 | -3.31 | -19.41 | 488 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.31 | -1.70 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Candlestick reversal · 1h | reversion | 98.27 | -1.73 | 25 | 20.0 | -27.23 | -6.75 | -27.84 | 490 |
| 29 | CCI reversion · 1h | reversion | 98.12 | -1.88 | 35 | 34.3 | 0.52 | 0.25 | -12.41 | 410 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.76 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.76 | -2.24 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.66 | -2.34 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.57 | -2.42 | 13 | 7.7 | 16.20 | 1.93 | -14.13 | 127 |
| 34 | Max aggression: 5-day momentum | meta | 97.56 | -2.44 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Bollinger reversion · 1h | reversion | 97.15 | -2.85 | 22 | 27.3 | -17.86 | -4.94 | -18.47 | 313 |
| 37 | Squeeze breakout · 1h | breakout | 97.04 | -2.96 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 38 | Max aggression: 1-day momentum | meta | 96.53 | -3.47 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.49 | -3.51 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.37 | -3.63 | 18 | 5.6 | 1.88 | 0.45 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.26 | -3.74 | 140 | 12.9 | -1.08 | -0.02 | -13.65 | 391 |
| 42 | Trend pullback · 1h | trend | 96.18 | -3.82 | 28 | 10.7 | -28.93 | -7.09 | -29.45 | 147 |
| 43 | MACD cross · 1h | trend | 95.99 | -4.00 | 40 | 10.0 | -18.94 | -3.21 | -21.88 | 462 |
| 44 | Parabolic SAR · 1h | trend | 95.78 | -4.22 | 26 | 11.5 | -8.00 | -1.00 | -18.82 | 293 |
| 45 | Donchian 55/20 · 1h | breakout | 95.72 | -4.28 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.85 | -16.91 | 684 |
| 47 | MFI reversion · 1h | reversion | 95.25 | -4.75 | 44 | 13.6 | -10.01 | -1.84 | -17.20 | 129 |
| 48 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.32 | -27.90 | -50.38 | 608 |
| 49 | Ichimoku · 1h | trend | 95.11 | -4.89 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.85 | -5.14 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.19 | -5.81 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 53 | Donchian 20/10 · 1h | breakout | 94.04 | -5.96 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 54 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.01 | 0.23 | -18.68 | 214 |
| 55 | ADX DI cross · 1h | trend | 93.90 | -6.10 | 30 | 6.7 | -16.28 | -3.02 | -17.96 | 256 |
| 56 | MACD zero-line · 1h | trend | 93.87 | -6.13 | 20 | 5.0 | -5.87 | -0.64 | -14.64 | 224 |
| 57 | Triple EMA stack · 1h | trend | 93.79 | -6.21 | 30 | 6.7 | -7.49 | -0.72 | -22.58 | 228 |
| 58 | VWAP momentum · 1h | momentum | 93.57 | -6.43 | 103 | 12.6 | -34.91 | -5.28 | -35.45 | 1237 |
| 59 | EMA 9/21 cross · 1h | trend | 92.71 | -7.29 | 44 | 11.4 | -4.20 | -0.38 | -16.92 | 308 |
| 60 | Heikin-Ashi · 1h | trend | 92.64 | -7.36 | 45 | 11.1 | -26.24 | -3.97 | -30.59 | 671 |
| 61 | OBV trend · 1h | momentum | 92.36 | -7.64 | 54 | 7.4 | -13.37 | -1.48 | -25.19 | 318 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.03 | -21.14 | -71.11 | 1470 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 88.51 | -11.49 | 99 | 14.1 | -59.87 | -18.63 | -59.94 | 1194 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.92 | -19.85 | -61.98 | 896 |
| 66 | ROC + volume | momentum | 86.90 | -13.10 | 150 | 18.7 | -72.04 | -17.61 | -72.05 | 1628 |
| 67 | Donchian 55/20 | breakout | 86.18 | -13.82 | 100 | 15.0 | -68.28 | -15.70 | -68.28 | 1302 |
| 68 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.79 | -34.06 | -84.81 | 1897 |
| 69 | Ichimoku | trend | 85.15 | -14.85 | 115 | 8.7 | -80.43 | -25.89 | -80.43 | 1742 |
| 70 | EMA 20/50 cross | trend | 84.94 | -15.06 | 131 | 15.3 | -78.94 | -17.65 | -78.94 | 1470 |
| 71 | VWAP reversion | reversion | 84.31 | -15.69 | 139 | 22.3 | -71.66 | -17.57 | -71.93 | 1399 |
| 72 | Z-score reversion | reversion | 83.99 | -16.01 | 188 | 31.4 | -84.53 | -27.38 | -84.54 | 2101 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.34 | -19.66 | 188 | 19.1 | -88.08 | -35.22 | -88.11 | 2150 |
| 76 | MACD zero-line | trend | 80.24 | -19.76 | 213 | 15.5 | -91.83 | -35.88 | -91.83 | 2355 |
| 77 | Supertrend | trend | 79.93 | -20.07 | 189 | 16.9 | -87.65 | -24.91 | -87.66 | 1960 |
| 78 | Donchian 20/10 | breakout | 79.70 | -20.30 | 212 | 17.0 | -90.94 | -29.65 | -90.95 | 2678 |
| 79 | Bollinger breakout | breakout | 79.26 | -20.74 | 214 | 15.9 | -93.91 | -41.99 | -93.91 | 2866 |
| 80 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.64 | -33.56 | -90.64 | 2262 |
| 81 | Triple EMA stack | trend | 78.39 | -21.61 | 224 | 14.7 | -93.13 | -36.04 | -93.13 | 2620 |
| 82 | ADX DI cross | trend | 78.33 | -21.67 | 203 | 7.9 | -89.34 | -44.75 | -89.34 | 2109 |
| 83 | RSI momentum | momentum | 78.19 | -21.81 | 206 | 12.6 | -90.62 | -29.37 | -90.62 | 2385 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.29 | -39.16 | -96.29 | 3601 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.58 | -29.61 | -94.59 | 2644 |
| 86 | Stochastic reversion | reversion | 75.09 | -24.91 | 337 | 23.4 | -95.92 | -44.76 | -95.92 | 4057 |
| 87 | Candlestick reversal | reversion | 74.71 | -25.29 | 282 | 12.4 | -99.36 | -48.96 | -99.36 | 5585 |
| 88 | EMA 9/21 cross | trend | 74.05 | -25.95 | 296 | 16.2 | -97.44 | -41.55 | -97.44 | 3535 |
| 89 | Bollinger reversion | reversion | 73.37 | -26.63 | 320 | 15.0 | -95.79 | -43.43 | -95.79 | 3686 |
| 90 | OBV trend | momentum | 72.78 | -27.22 | 286 | 14.7 | -95.95 | -48.50 | -95.95 | 3551 |
| 91 | Parabolic SAR | trend | 71.31 | -28.69 | 279 | 12.5 | -97.02 | -54.64 | -97.02 | 3632 |
| 92 | CCI reversion | reversion | 71.22 | -28.79 | 257 | 10.5 | -98.46 | -49.61 | -98.46 | 4698 |
| 93 | MACD cross | trend | 69.83 | -30.17 | 290 | 13.1 | -99.72 | -64.26 | -99.72 | 6075 |
| 94 | VWAP momentum | momentum | 69.49 | -30.51 | 402 | 9.5 | -98.50 | -35.77 | -98.50 | 5206 |
| 95 | Heikin-Ashi | trend | 69.19 | -30.81 | 246 | 3.3 | -99.90 | -77.52 | -99.90 | 8300 |
| 96 | Williams %R | reversion | 69.14 | -30.86 | 360 | 20.0 | -99.52 | -57.17 | -99.52 | 6109 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T06:40 | Triple EMA stack | sell | XRP-USD | 19.53 | -0.18 | exit signal |
| 2026-09-30T06:40 | EMA 9/21 cross | sell | XRP-USD | 14.81 | -0.12 | exit signal |
| 2026-09-30T06:35 | Supertrend | sell | DOGE-USD | 19.91 | -0.30 | exit signal |
| 2026-09-30T06:30 | Williams %R | buy | XRP-USD | 17.37 | — | entry signal |
| 2026-09-30T06:30 | Williams %R | buy | SOL-USD | 17.37 | — | entry signal |
| 2026-09-30T06:30 | Williams %R | buy | ETH-USD | 17.37 | — | entry signal |
| 2026-09-30T06:30 | Williams %R | buy | BTC-USD | 17.37 | — | entry signal |
| 2026-09-30T06:30 | Stochastic reversion | buy | SOL-USD | 18.84 | — | entry signal |
| 2026-09-30T06:30 | Stochastic reversion | buy | ETH-USD | 18.84 | — | entry signal |
| 2026-09-30T06:30 | Stochastic reversion | buy | BTC-USD | 18.84 | — | entry signal |
| 2026-09-30T06:30 | VWAP reversion | buy | SOL-USD | 21.12 | — | entry signal |
| 2026-09-30T06:30 | Z-score reversion | buy | SOL-USD | 21.08 | — | entry signal |
| 2026-09-30T06:30 | Z-score reversion | buy | ETH-USD | 21.08 | — | entry signal |
| 2026-09-30T06:30 | Z-score reversion | buy | BTC-USD | 21.08 | — | entry signal |
| 2026-09-30T06:30 | Candlestick reversal | buy | SOL-USD | 18.75 | — | entry signal |
| 2026-09-30T06:30 | Candlestick reversal | buy | ETH-USD | 18.75 | — | entry signal |
| 2026-09-30T06:30 | Candlestick reversal | buy | BTC-USD | 18.75 | — | entry signal |
| 2026-09-30T06:30 | ADX DI cross | sell | XRP-USD | 19.50 | -0.11 | exit signal |
| 2026-09-30T06:25 | Donchian 55/20 | sell | XRP-USD | 21.32 | -0.31 | stop-loss |
| 2026-09-30T06:25 | Donchian 20/10 | sell | XRP-USD | 19.84 | -0.24 | exit signal |
| 2026-09-30T06:25 | OBV trend | sell | DOGE-USD | 18.08 | -0.25 | stop-loss |
| 2026-09-30T06:25 | RSI momentum | sell | XRP-USD | 19.52 | -0.24 | exit signal |
| 2026-09-30T06:25 | RSI momentum | sell | DOGE-USD | 19.44 | -0.28 | stop-loss |
| 2026-09-30T06:25 | VWAP momentum | sell | XRP-USD | 13.88 | -0.11 | exit signal |
| 2026-09-30T06:25 | Triple EMA stack | sell | DOGE-USD | 19.44 | -0.26 | stop-loss |
| 2026-09-30T06:25 | EMA 20/50 cross | sell | DOGE-USD | 21.09 | -0.30 | stop-loss |
| 2026-09-30T06:25 | EMA 9/21 cross | sell | DOGE-USD | 14.78 | -0.16 | exit signal |
| 2026-09-30T06:20 | VWAP reversion | buy | BTC-USD | 21.13 | — | entry signal |
| 2026-09-30T06:20 | Bollinger reversion | buy | ETH-USD | 18.38 | — | entry signal |
| 2026-09-30T06:20 | Bollinger reversion | buy | BTC-USD | 18.38 | — | entry signal |
| 2026-09-30T06:20 | MACD zero-line | sell | XRP-USD | 16.08 | -0.11 | exit signal |
| 2026-09-30T06:20 | MACD zero-line | sell | DOGE-USD | 16.06 | -0.16 | exit signal |
| 2026-09-30T06:20 | MACD cross | sell | XRP-USD | 14.01 | -0.08 | exit signal |
| 2026-09-30T06:20 | MACD cross | sell | DOGE-USD | 13.98 | -0.10 | exit signal |
| 2026-09-30T06:15 | MFI reversion | sell | ETH-USD | 20.01 | -0.20 | stop-loss |
| 2026-09-30T06:15 | Squeeze breakout | sell | XRP-USD | 22.06 | -0.23 | exit signal |
| 2026-09-30T06:15 | Squeeze breakout | sell | DOGE-USD | 22.02 | -0.27 | exit signal |
| 2026-09-30T06:15 | Bollinger breakout | sell | XRP-USD | 19.83 | -0.15 | exit signal |
| 2026-09-30T06:15 | Bollinger breakout | sell | DOGE-USD | 19.78 | -0.20 | exit signal |
| 2026-09-30T06:15 | Donchian 20/10 | sell | ETH-USD | 19.85 | -0.23 | stop-loss |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
