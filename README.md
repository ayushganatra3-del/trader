# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T08:40:05.000121+00:00 · 6688 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.62 (-0.38%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.96 | -0.03 |

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

Today: 6780 decisions in 1356 calls, $0.0950 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T08:40 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-09-30T08:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T08:40 | 3 / 2 / 0 | ETH-USD 27%, XRP-USD 22% |  |

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
| 7 | Copy: Congress Democrats (NANC) | copy | 99.78 | -0.22 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Agent | meta | 99.62 | -0.38 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.44 | -0.56 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 11 | Agent (aggressive) | meta | 99.42 | -0.58 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Hold SPY | benchmark | 99.21 | -0.79 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 13 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 14 | Hold BTC | benchmark | 99.14 | -0.86 | 0 | — | 28.45 | 3.58 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.13 | -0.88 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 99.12 | -0.88 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 17 | VWAP reversion · 1h | reversion | 98.99 | -1.01 | 20 | 25.0 | -13.14 | -4.42 | -14.91 | 123 |
| 18 | RSI(14) reversion · 1h | reversion | 98.94 | -1.05 | 7 | 57.1 | 5.65 | 1.46 | -7.03 | 118 |
| 19 | Daily: Bullish score | daily | 98.78 | -1.22 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 20 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 21 | Z-score reversion · 1h | reversion | 98.67 | -1.33 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Copy: Insider buying | copy | 98.61 | -1.39 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.67 | -4.73 | 182 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Stochastic reversion · 1h | reversion | 98.26 | -1.74 | 26 | 53.8 | -14.26 | -3.08 | -15.43 | 332 |
| 26 | Williams %R · 1h | reversion | 98.24 | -1.76 | 40 | 45.0 | -17.87 | -3.31 | -19.41 | 488 |
| 27 | Candlestick reversal · 1h | reversion | 98.17 | -1.83 | 25 | 20.0 | -26.14 | -6.55 | -26.78 | 486 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.16 | -1.84 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | CCI reversion · 1h | reversion | 97.98 | -2.02 | 35 | 34.3 | 0.52 | 0.25 | -12.41 | 410 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.76 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.65 | -2.35 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.52 | -2.48 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.47 | -2.53 | 13 | 7.7 | 16.56 | 1.97 | -14.13 | 126 |
| 34 | Max aggression: 5-day momentum | meta | 97.42 | -2.58 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Squeeze breakout · 1h | breakout | 97.00 | -3.00 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 37 | Bollinger reversion · 1h | reversion | 97.00 | -3.00 | 22 | 27.3 | -17.49 | -4.87 | -18.11 | 312 |
| 38 | Max aggression: 1-day momentum | meta | 96.39 | -3.61 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.35 | -3.65 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.26 | -3.74 | 18 | 5.6 | 1.90 | 0.46 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.12 | -3.88 | 140 | 12.9 | -0.20 | 0.14 | -13.26 | 385 |
| 42 | Trend pullback · 1h | trend | 96.07 | -3.93 | 28 | 10.7 | -28.93 | -7.09 | -29.45 | 147 |
| 43 | MACD cross · 1h | trend | 95.85 | -4.15 | 40 | 10.0 | -18.50 | -3.13 | -21.39 | 460 |
| 44 | Parabolic SAR · 1h | trend | 95.64 | -4.36 | 26 | 11.5 | -8.03 | -1.00 | -18.82 | 293 |
| 45 | Donchian 55/20 · 1h | breakout | 95.58 | -4.42 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.85 | -16.91 | 684 |
| 47 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.28 | -27.84 | -50.33 | 607 |
| 48 | MFI reversion · 1h | reversion | 95.08 | -4.92 | 44 | 13.6 | -9.99 | -1.83 | -17.20 | 129 |
| 49 | Ichimoku · 1h | trend | 95.04 | -4.96 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.79 | -5.21 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.09 | -5.91 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 53 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.01 | 0.23 | -18.68 | 214 |
| 54 | Donchian 20/10 · 1h | breakout | 94.02 | -5.99 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | ADX DI cross · 1h | trend | 93.77 | -6.24 | 30 | 6.7 | -16.25 | -3.01 | -17.93 | 256 |
| 56 | MACD zero-line · 1h | trend | 93.73 | -6.27 | 21 | 4.8 | -5.81 | -0.63 | -14.64 | 223 |
| 57 | Triple EMA stack · 1h | trend | 93.72 | -6.28 | 30 | 6.7 | -6.79 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.43 | -6.57 | 103 | 12.6 | -35.07 | -5.31 | -35.63 | 1240 |
| 59 | Heikin-Ashi · 1h | trend | 92.57 | -7.43 | 45 | 11.1 | -26.24 | -3.97 | -30.59 | 671 |
| 60 | EMA 9/21 cross · 1h | trend | 92.55 | -7.45 | 45 | 11.1 | -4.29 | -0.39 | -16.92 | 308 |
| 61 | OBV trend · 1h | momentum | 92.22 | -7.78 | 54 | 7.4 | -13.09 | -1.44 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.02 | -21.12 | -71.11 | 1469 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 88.51 | -11.49 | 99 | 14.1 | -59.95 | -18.65 | -59.95 | 1193 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.82 | -19.79 | -61.89 | 894 |
| 66 | ROC + volume | momentum | 86.68 | -13.32 | 151 | 18.5 | -72.05 | -17.61 | -72.05 | 1626 |
| 67 | Donchian 55/20 | breakout | 86.18 | -13.82 | 100 | 15.0 | -68.14 | -15.67 | -68.14 | 1300 |
| 68 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.76 | -34.08 | -84.76 | 1894 |
| 69 | Ichimoku | trend | 84.34 | -15.66 | 119 | 8.4 | -80.44 | -26.04 | -80.45 | 1741 |
| 70 | EMA 20/50 cross | trend | 84.20 | -15.80 | 135 | 14.8 | -79.06 | -17.71 | -79.06 | 1472 |
| 71 | VWAP reversion | reversion | 83.87 | -16.14 | 143 | 21.7 | -71.74 | -17.64 | -72.02 | 1401 |
| 72 | Z-score reversion | reversion | 83.62 | -16.38 | 192 | 30.7 | -84.59 | -27.49 | -84.60 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.02 | -19.98 | 189 | 19.0 | -88.12 | -35.44 | -88.15 | 2150 |
| 76 | Donchian 20/10 | breakout | 79.52 | -20.48 | 213 | 16.9 | -90.91 | -29.69 | -90.91 | 2674 |
| 77 | MACD zero-line | trend | 79.41 | -20.59 | 217 | 15.2 | -91.91 | -36.19 | -91.91 | 2359 |
| 78 | Supertrend | trend | 79.35 | -20.64 | 191 | 16.8 | -87.72 | -24.99 | -87.72 | 1962 |
| 79 | Bollinger breakout | breakout | 79.08 | -20.92 | 215 | 15.8 | -93.89 | -42.15 | -93.89 | 2863 |
| 80 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.58 | -33.23 | -90.58 | 2259 |
| 81 | Triple EMA stack | trend | 77.96 | -22.04 | 226 | 14.6 | -93.18 | -36.24 | -93.18 | 2622 |
| 82 | RSI momentum | momentum | 77.56 | -22.44 | 209 | 12.4 | -90.60 | -29.49 | -90.60 | 2383 |
| 83 | ADX DI cross | trend | 77.28 | -22.71 | 210 | 7.6 | -89.50 | -45.98 | -89.50 | 2117 |
| 84 | Connors RSI(2) | reversion | 76.96 | -23.05 | 243 | 16.9 | -96.29 | -39.22 | -96.29 | 3600 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.53 | -29.54 | -94.54 | 2639 |
| 86 | Stochastic reversion | reversion | 74.86 | -25.14 | 342 | 23.4 | -95.93 | -44.91 | -95.94 | 4058 |
| 87 | Candlestick reversal | reversion | 73.78 | -26.22 | 291 | 12.0 | -99.36 | -49.51 | -99.36 | 5592 |
| 88 | EMA 9/21 cross | trend | 73.30 | -26.70 | 301 | 15.9 | -97.46 | -41.87 | -97.46 | 3537 |
| 89 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.79 | -43.45 | -95.80 | 3687 |
| 90 | OBV trend | momentum | 72.17 | -27.83 | 290 | 14.5 | -95.96 | -48.90 | -95.96 | 3551 |
| 91 | Parabolic SAR | trend | 71.03 | -28.97 | 281 | 12.5 | -97.00 | -54.87 | -97.00 | 3626 |
| 92 | CCI reversion | reversion | 70.96 | -29.04 | 262 | 10.7 | -98.47 | -49.74 | -98.47 | 4703 |
| 93 | MACD cross | trend | 69.09 | -30.91 | 295 | 12.9 | -99.72 | -65.27 | -99.72 | 6079 |
| 94 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.54 | -36.17 | -98.54 | 5220 |
| 95 | Heikin-Ashi | trend | 68.64 | -31.36 | 252 | 3.2 | -99.89 | -78.27 | -99.89 | 8298 |
| 96 | Williams %R | reversion | 68.55 | -31.45 | 367 | 19.9 | -99.53 | -57.62 | -99.53 | 6114 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T08:40 | Williams %R | buy | ETH-USD | 17.18 | — | entry signal |
| 2026-09-30T08:40 | Williams %R | buy | DOGE-USD | 17.18 | — | entry signal |
| 2026-09-30T08:40 | Williams %R | buy | BTC-USD | 17.18 | — | entry signal |
| 2026-09-30T08:40 | Candlestick reversal | buy | BTC-USD | 18.35 | — | entry signal |
| 2026-09-30T08:35 | Heikin-Ashi | sell | DOGE-USD | 17.06 | -0.14 | exit signal |
| 2026-09-30T08:35 | ADX DI cross | sell | ETH-USD | 19.26 | -0.13 | exit signal |
| 2026-09-30T08:35 | ADX DI cross | sell | DOGE-USD | 19.25 | -0.14 | exit signal |
| 2026-09-30T08:35 | Supertrend | sell | BTC-USD | 19.75 | -0.20 | exit signal |
| 2026-09-30T08:35 | Triple EMA stack | sell | DOGE-USD | 19.38 | -0.20 | exit signal |
| 2026-09-30T08:35 | EMA 9/21 cross | sell | ETH-USD | 18.34 | -0.16 | exit signal |
| 2026-09-30T08:35 | EMA 9/21 cross | sell | DOGE-USD | 18.31 | -0.18 | exit signal |
| 2026-09-30T08:30 | Candlestick reversal | sell | SOL-USD | 18.35 | -0.11 | exit signal |
| 2026-09-30T08:30 | Heikin-Ashi | buy | DOGE-USD | 17.20 | — | entry signal |
| 2026-09-30T08:30 | EMA 20/50 cross | sell | XRP-USD | 21.01 | -0.20 | exit signal |
| 2026-09-30T08:25 | MFI reversion | sell | XRP-USD | 19.93 | -0.15 | exit signal |
| 2026-09-30T08:25 | Connors RSI(2) | sell | XRP-USD | 19.12 | -0.16 | exit signal |
| 2026-09-30T08:20 | CCI reversion | buy | SOL-USD | 17.76 | — | entry signal |
| 2026-09-30T08:20 | Williams %R | buy | SOL-USD | 17.19 | — | entry signal |
| 2026-09-30T08:20 | Stochastic reversion | buy | SOL-USD | 18.73 | — | entry signal |
| 2026-09-30T08:20 | VWAP reversion | buy | SOL-USD | 20.99 | — | entry signal |
| 2026-09-30T08:20 | Candlestick reversal | buy | SOL-USD | 18.47 | — | entry signal |
| 2026-09-30T08:20 | Candlestick reversal | buy | ETH-USD | 18.51 | — | entry signal |
| 2026-09-30T08:20 | Candlestick reversal | buy | DOGE-USD | 18.51 | — | entry signal |
| 2026-09-30T08:20 | ROC + volume | sell | DOGE-USD | 21.50 | -0.22 | target is flat |
| 2026-09-30T08:20 | ADX DI cross | buy | ETH-USD | 19.39 | — | entry signal |
| 2026-09-30T08:20 | ADX DI cross | buy | DOGE-USD | 19.39 | — | entry signal |
| 2026-09-30T08:20 | EMA 9/21 cross | sell | BTC-USD | 18.34 | -0.16 | exit signal |
| 2026-09-30T08:15 | RSI momentum | sell | ETH-USD | 19.34 | -0.20 | stop-loss |
| 2026-09-30T08:15 | RSI momentum | sell | BTC-USD | 19.35 | -0.20 | stop-loss |
| 2026-09-30T08:15 | Ichimoku | sell | BTC-USD | 21.06 | -0.21 | stop-loss |
| 2026-09-30T08:15 | ADX DI cross | sell | DOGE-USD | 19.37 | -0.18 | exit signal |
| 2026-09-30T08:15 | ADX DI cross | sell | BTC-USD | 15.53 | -0.13 | exit signal |
| 2026-09-30T08:15 | MACD zero-line | sell | ETH-USD | 19.87 | -0.19 | exit signal |
| 2026-09-30T08:15 | MACD zero-line | sell | DOGE-USD | 19.81 | -0.25 | exit signal |
| 2026-09-30T08:15 | MACD zero-line | sell | BTC-USD | 19.86 | -0.20 | stop-loss |
| 2026-09-30T08:15 | MACD cross | sell | SOL-USD | 17.22 | -0.22 | stop-loss |
| 2026-09-30T08:15 | MACD cross | sell | ETH-USD | 13.85 | -0.11 | exit signal |
| 2026-09-30T08:15 | MACD cross | sell | DOGE-USD | 13.83 | -0.13 | exit signal |
| 2026-09-30T08:15 | MACD cross | sell | BTC-USD | 13.84 | -0.12 | exit signal |
| 2026-09-30T08:15 | Triple EMA stack | sell | XRP-USD | 19.37 | -0.22 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
