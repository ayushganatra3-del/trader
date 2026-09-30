# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T00:10:05.000151+00:00 · 6245 ticks

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
| Copy: Insider buying | 2026-09-29 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.07 · VIX 16.04 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 135 decisions in 27 calls, $0.0019 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T00:10 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-09-30T00:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T00:10 | 0 / 4 / 1 | cash |  |

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
| 8 | Hold BTC | benchmark | 99.97 | -0.03 | 0 | — | 30.95 | 3.84 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.73 | -0.27 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Agent | meta | 99.68 | -0.32 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 12 | Agent (aggressive) | meta | 99.57 | -0.43 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.50 | -0.50 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.41 | -0.58 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.41 | -0.59 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.14 | -0.86 | 20 | 25.0 | -12.95 | -4.39 | -14.73 | 122 |
| 18 | Daily: Bullish score | daily | 99.06 | -0.94 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.02 | -0.98 | 7 | 57.1 | 6.80 | 1.73 | -7.03 | 114 |
| 20 | Z-score reversion · 1h | reversion | 98.89 | -1.11 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.87 | -1.13 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Williams %R · 1h | reversion | 98.59 | -1.41 | 40 | 45.0 | -18.01 | -3.33 | -19.47 | 488 |
| 24 | Candlestick reversal · 1h | reversion | 98.55 | -1.45 | 22 | 22.7 | -25.47 | -6.37 | -26.70 | 481 |
| 25 | Stochastic reversion · 1h | reversion | 98.54 | -1.46 | 26 | 53.8 | -13.63 | -3.00 | -14.80 | 328 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 15.13 | 3.73 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.45 | -1.55 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.26 | -1.74 | 35 | 34.3 | 0.28 | 0.21 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.87 | -2.13 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -4.95 | -1.74 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.80 | -2.20 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.72 | -2.28 | 12 | 8.3 | 16.65 | 1.98 | -14.13 | 126 |
| 34 | Max aggression: 5-day momentum | meta | 97.71 | -2.29 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Bollinger reversion · 1h | reversion | 97.29 | -2.71 | 22 | 27.3 | -17.68 | -4.91 | -18.30 | 312 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.08 | -2.92 | 9 | 11.1 | 15.55 | 2.73 | -5.11 | 92 |
| 38 | Max aggression: 1-day momentum | meta | 96.67 | -3.33 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.63 | -3.37 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.60 | -3.40 | 18 | 5.6 | 2.01 | 0.47 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.50 | -3.50 | 139 | 12.9 | 0.98 | 0.33 | -11.64 | 385 |
| 42 | Trend pullback · 1h | trend | 96.28 | -3.72 | 28 | 10.7 | -29.04 | -7.12 | -29.77 | 148 |
| 43 | MACD cross · 1h | trend | 96.13 | -3.87 | 40 | 10.0 | -18.72 | -3.17 | -21.77 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.92 | -4.08 | 26 | 11.5 | -7.76 | -0.96 | -18.82 | 292 |
| 45 | Donchian 55/20 · 1h | breakout | 95.86 | -4.14 | 12 | 0.0 | 4.53 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.48 | -2.79 | -16.70 | 683 |
| 47 | MFI reversion · 1h | reversion | 95.47 | -4.53 | 44 | 13.6 | -9.77 | -1.79 | -17.20 | 128 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -50.24 | -27.70 | -50.38 | 607 |
| 49 | Ichimoku · 1h | trend | 95.18 | -4.82 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.92 | -5.08 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.30 | -5.71 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 53 | MACD zero-line · 1h | trend | 94.29 | -5.71 | 20 | 5.0 | -5.35 | -0.56 | -14.64 | 222 |
| 54 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | ADX DI cross · 1h | trend | 94.04 | -5.96 | 30 | 6.7 | -15.99 | -2.96 | -17.81 | 254 |
| 56 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.33 | 0.27 | -18.68 | 212 |
| 57 | Triple EMA stack · 1h | trend | 93.85 | -6.15 | 30 | 6.7 | -7.30 | -0.69 | -22.58 | 228 |
| 58 | VWAP momentum · 1h | momentum | 93.70 | -6.30 | 103 | 12.6 | -34.82 | -5.26 | -35.25 | 1235 |
| 59 | EMA 9/21 cross · 1h | trend | 93.06 | -6.94 | 44 | 11.4 | -3.90 | -0.34 | -16.92 | 307 |
| 60 | Heikin-Ashi · 1h | trend | 92.71 | -7.29 | 45 | 11.1 | -26.45 | -4.01 | -30.63 | 672 |
| 61 | OBV trend · 1h | momentum | 92.49 | -7.51 | 54 | 7.4 | -13.13 | -1.44 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.89 | -9.11 | 119 | 34.5 | -71.14 | -21.27 | -71.22 | 1473 |
| 63 | Squeeze breakout | breakout | 89.51 | -10.49 | 94 | 14.9 | -59.66 | -18.33 | -59.85 | 1191 |
| 64 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.83 | -0.41 | -19.49 | 406 |
| 65 | AI bee: Bizzy | ai | 87.82 | -12.18 | 230 | 11.7 | — | — | — | — |
| 66 | AI bee: Boozy | ai | 87.63 | -12.37 | 70 | 1.4 | — | — | — | — |
| 67 | ROC + volume | momentum | 87.31 | -12.69 | 148 | 18.9 | -72.07 | -17.61 | -72.12 | 1629 |
| 68 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -62.07 | -19.91 | -62.13 | 898 |
| 69 | Donchian 55/20 | breakout | 87.12 | -12.88 | 96 | 15.6 | -68.04 | -15.52 | -68.08 | 1302 |
| 70 | EMA 20/50 cross | trend | 86.65 | -13.35 | 123 | 16.3 | -78.76 | -17.40 | -78.76 | 1471 |
| 71 | Ichimoku | trend | 85.53 | -14.47 | 113 | 8.8 | -80.44 | -25.75 | -80.44 | 1743 |
| 72 | Keltner breakout | breakout | 85.48 | -14.52 | 149 | 13.4 | -84.90 | -33.65 | -84.92 | 1900 |
| 73 | Z-score reversion | reversion | 84.96 | -15.04 | 180 | 32.8 | -84.39 | -27.02 | -84.42 | 2094 |
| 74 | VWAP reversion | reversion | 84.68 | -15.32 | 137 | 22.6 | -71.54 | -17.46 | -71.94 | 1396 |
| 75 | MACD zero-line | trend | 81.93 | -18.07 | 203 | 16.3 | -91.75 | -34.89 | -91.75 | 2354 |
| 76 | Supertrend | trend | 81.80 | -18.20 | 181 | 17.7 | -87.45 | -24.48 | -87.45 | 1957 |
| 77 | Donchian 20/10 | breakout | 80.96 | -19.04 | 206 | 17.5 | -90.92 | -29.07 | -90.92 | 2678 |
| 78 | MFI reversion | reversion | 80.96 | -19.04 | 184 | 19.6 | -88.07 | -35.05 | -88.07 | 2151 |
| 79 | Bollinger breakout | breakout | 80.45 | -19.55 | 207 | 16.4 | -93.91 | -40.67 | -93.91 | 2866 |
| 80 | Triple EMA stack | trend | 79.77 | -20.23 | 217 | 15.2 | -93.06 | -35.19 | -93.06 | 2618 |
| 81 | RSI momentum | momentum | 79.66 | -20.34 | 199 | 13.1 | -90.42 | -28.75 | -90.42 | 2379 |
| 82 | Trend pullback | trend | 79.25 | -20.75 | 170 | 17.1 | -90.84 | -34.13 | -90.84 | 2275 |
| 83 | ADX DI cross | trend | 79.10 | -20.90 | 198 | 8.1 | -89.33 | -44.28 | -89.33 | 2108 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.41 | -40.74 | -96.41 | 3626 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.46 | -29.29 | -94.47 | 2633 |
| 86 | Candlestick reversal | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.35 | -48.06 | -99.35 | 5578 |
| 87 | EMA 9/21 cross | trend | 75.95 | -24.05 | 283 | 17.0 | -97.43 | -40.56 | -97.43 | 3535 |
| 88 | Stochastic reversion | reversion | 75.93 | -24.07 | 328 | 24.1 | -95.94 | -44.73 | -95.94 | 4057 |
| 89 | OBV trend | momentum | 74.73 | -25.27 | 275 | 15.3 | -95.89 | -46.50 | -95.89 | 3547 |
| 90 | Bollinger reversion | reversion | 74.68 | -25.32 | 305 | 15.7 | -95.77 | -42.95 | -95.77 | 3681 |
| 91 | VWAP momentum | momentum | 73.22 | -26.78 | 370 | 10.3 | -98.44 | -34.70 | -98.44 | 5186 |
| 92 | CCI reversion | reversion | 73.09 | -26.91 | 238 | 11.3 | -98.45 | -48.79 | -98.45 | 4695 |
| 93 | Parabolic SAR | trend | 72.65 | -27.35 | 270 | 13.0 | -97.00 | -52.34 | -97.00 | 3632 |
| 94 | MACD cross | trend | 71.95 | -28.05 | 272 | 14.0 | -99.72 | -61.49 | -99.72 | 6073 |
| 95 | Williams %R | reversion | 71.27 | -28.73 | 340 | 21.2 | -99.52 | -55.71 | -99.52 | 6107 |
| 96 | Heikin-Ashi | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -73.98 | -99.89 | 8301 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T00:10 | AI bee: Boozy | sell | ETH-USD | 18.75 | -0.12 | Jev: sell (buy p=0.25) |
| 2026-09-30T00:10 | Donchian 20/10 | sell | BTC-USD | 20.18 | -0.16 | exit signal |
| 2026-09-30T00:10 | OBV trend | sell | SOL-USD | 18.59 | -0.19 | exit signal |
| 2026-09-30T00:10 | RSI momentum | sell | BTC-USD | 19.94 | -0.14 | exit signal |
| 2026-09-30T00:10 | Trend pullback | sell | BTC-USD | 19.71 | -0.14 | exit signal |
| 2026-09-30T00:10 | Ichimoku | sell | BTC-USD | 21.36 | -0.15 | exit signal |
| 2026-09-30T00:10 | Supertrend | sell | XRP-USD | 20.44 | -0.20 | exit signal |
| 2026-09-30T00:10 | Supertrend | sell | ETH-USD | 20.43 | -0.20 | exit signal |
| 2026-09-30T00:10 | Supertrend | sell | BTC-USD | 16.39 | -0.11 | exit signal |
| 2026-09-30T00:09 | AI bee: Boozy | buy | ETH-USD | 18.87 | — | Jev: buy (buy p=0.43) |
| 2026-09-30T00:08 | AI bee: Boozy | sell | ETH-USD | 19.65 | -0.12 | Jev: sell (buy p=0.23) |
| 2026-09-30T00:07 | AI bee: Boozy | buy | ETH-USD | 19.77 | — | Jev: buy (buy p=0.45) |
| 2026-09-30T00:05 | AI bee: Boozy | sell | SOL-USD | 36.42 | -0.23 | Jev: sell (buy p=0.26) |
| 2026-09-30T00:05 | AI bee: Boozy | sell | BTC-USD | 32.47 | -0.20 | Jev: sell (buy p=0.24) |
| 2026-09-30T00:05 | AI bee: Bizzy | sell | SOL-USD | 17.51 | -0.11 | Jev: sell (buy p=0.01) |
| 2026-09-30T00:05 | CCI reversion | buy | XRP-USD | 18.32 | — | entry signal |
| 2026-09-30T00:05 | Stochastic reversion | buy | ETH-USD | 19.00 | — | entry signal |
| 2026-09-30T00:05 | VWAP momentum | sell | BTC-USD | 18.22 | -0.11 | exit signal |
| 2026-09-30T00:05 | Trend pullback | buy | BTC-USD | 19.85 | — | entry signal |
| 2026-09-30T00:04 | AI bee: Bizzy | sell | DOGE-USD | 12.91 | -0.07 | Jev: sell (buy p=0.20) |
| 2026-09-30T00:03 | AI bee: Bizzy | sell | XRP-USD | 15.97 | -0.10 | Jev: sell (buy p=0.10) |
| 2026-09-30T00:02 | AI bee: Bizzy | buy | XRP-USD | 16.07 | — | Jev: buy (buy p=0.73) |
| 2026-09-30T00:02 | AI bee: Bizzy | buy | DOGE-USD | 12.99 | — | Jev: buy (buy p=0.59) |
| 2026-09-30T00:00 | AI bee: Boozy | buy | SOL-USD | 36.64 | — | Jev: buy (buy p=0.83) |
| 2026-09-30T00:00 | AI bee: Boozy | buy | BTC-USD | 32.67 | — | Jev: buy (buy p=0.74) |
| 2026-09-30T00:00 | AI bee: Bizzy | buy | SOL-USD | 17.62 | — | Jev: buy (buy p=0.80) |
| 2026-09-30T00:00 | Candlestick reversal · 1h | sell | ETH-USD | 4.15 | -0.06 | exit signal |
| 2026-09-30T00:00 | CCI reversion | buy | DOGE-USD | 18.33 | — | entry signal |
| 2026-09-30T00:00 | Williams %R | buy | XRP-USD | 17.90 | — | entry |
| 2026-09-30T00:00 | Williams %R | buy | SOL-USD | 17.90 | — | entry signal |
| 2026-09-30T00:00 | Williams %R | buy | ETH-USD | 17.90 | — | entry |
| 2026-09-30T00:00 | Williams %R | buy | DOGE-USD | 17.90 | — | entry |
| 2026-09-30T00:00 | VWAP momentum | buy | BTC-USD | 18.33 | — | entry |
| 2026-09-29T23:55 | RSI momentum | sell | SOL-USD | 19.94 | -0.16 | exit signal |
| 2026-09-29T23:55 | ADX DI cross | sell | BTC-USD | 19.72 | -0.12 | exit signal |
| 2026-09-29T23:55 | Triple EMA stack | sell | SOL-USD | 19.93 | -0.16 | exit signal |
| 2026-09-29T23:55 | EMA 9/21 cross | sell | SOL-USD | 15.19 | -0.12 | exit signal |
| 2026-09-29T23:50 | MFI reversion | buy | DOGE-USD | 20.27 | — | entry signal |
| 2026-09-29T23:50 | CCI reversion | buy | SOL-USD | 18.36 | — | entry signal |
| 2026-09-29T23:50 | CCI reversion | buy | ETH-USD | 18.36 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
