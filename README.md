# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-03T03:35:05.000149+00:00 · 9596 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.24 (-0.76%)

Closed trades 32, win rate 65.6%, fees £0.92, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, ETRA 12%, BBD 12%, BPRE 12%, GME 12%, NYAX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 2685 decisions in 537 calls, $0.0376 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-03T03:35 | 2 / 3 / 0 | AMZN 16%, COIN 16%, MSTR 15% |  |
| Breezy | 2026-10-03T03:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-03T03:35 | 2 / 3 / 0 | ETH-USD 41% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion · 1h | UPRO | 2.43 | +6.89% | 3 |
| Stochastic reversion · 1h | SPY | 2.28 | +2.53% | 3 |
| Connors RSI(2) · 1h | COIN | 2.23 | +6.43% | 5 |
| Stochastic reversion | MSFT | 2.20 | +2.95% | 13 |
| RSI(14) reversion | SQQQ | 2.18 | +4.27% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.27 | -15.27 | 2 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 101.13 | 1.13 | 0 | — | 32.88 | 4.04 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.62 | -3.14 | -14.05 | 116 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -22.69 | -5.11 | -26.04 | 494 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 10 | 60.0 | 4.94 | 1.42 | -6.57 | 117 |
| 9 | Bollinger reversion · 1h | reversion | 100.16 | 0.16 | 38 | 44.7 | -14.70 | -3.91 | -17.68 | 307 |
| 10 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.91 | 1.94 | -1.46 | 86 |
| 14 | Z-score reversion · 1h | reversion | 99.72 | -0.28 | 18 | 55.6 | 5.61 | 1.29 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.70 | 1.05 | -16.96 | 115 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.93 | -6.37 | -11.27 | 213 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.07 | -0.93 | 40 | 60.0 | -8.58 | -1.78 | -9.82 | 334 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.75 | 0.45 | -12.41 | 419 |
| 24 | Trend pullback · 1h | trend | 98.82 | -1.18 | 45 | 20.0 | -21.96 | -5.63 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 28 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.94 | -0.45 | -4.23 | 99 |
| 29 | Agent (rotation) | meta | 97.89 | -2.11 | 50 | 20.0 | -3.25 | -1.21 | -8.90 | 228 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 14.00 | 1.75 | -14.40 | 132 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.74 | -2.26 | 57 | 45.6 | -12.45 | -4.20 | -14.21 | 225 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -16.63 | -3.04 | -19.41 | 500 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 3.83 | 0.81 | -11.48 | 380 |
| 37 | MFI reversion · 1h | reversion | 96.62 | -3.38 | 69 | 29.0 | -6.94 | -1.14 | -16.99 | 121 |
| 38 | Parabolic SAR · 1h | trend | 96.48 | -3.52 | 47 | 17.0 | -7.86 | -0.96 | -19.70 | 311 |
| 39 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.60 | 2.81 | -4.73 | 199 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -23.36 | -1.17 | -41.28 | 43 |
| 41 | Supertrend · 1h | trend | 95.95 | -4.05 | 28 | 7.1 | 2.56 | 0.53 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.60 | -3.69 | -21.08 | 71 |
| 43 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -5.59 | -0.78 | -13.84 | 273 |
| 44 | MACD cross · 1h | trend | 95.50 | -4.50 | 71 | 15.5 | -14.48 | -2.33 | -17.27 | 483 |
| 45 | Squeeze breakout · 1h | breakout | 95.29 | -4.71 | 22 | 18.2 | 20.04 | 2.89 | -8.06 | 113 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.31 | 0.92 | -16.19 | 127 |
| 48 | RSI momentum · 1h | momentum | 93.97 | -6.03 | 40 | 2.5 | 1.91 | 0.45 | -16.65 | 227 |
| 49 | VWAP momentum · 1h | momentum | 93.36 | -6.64 | 173 | 22.5 | -41.33 | -6.54 | -42.62 | 1285 |
| 50 | Bollinger breakout · 1h | breakout | 93.18 | -6.82 | 36 | 16.7 | 5.73 | 0.93 | -12.06 | 292 |
| 51 | Triple EMA stack · 1h | trend | 93.11 | -6.89 | 50 | 8.0 | -7.32 | -0.69 | -23.88 | 240 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Three white soldiers | momentum | 92.52 | -7.48 | 66 | 16.7 | -49.26 | -26.26 | -49.26 | 591 |
| 54 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 2.74 | 0.57 | -12.60 | 128 |
| 55 | EMA 9/21 cross · 1h | trend | 91.74 | -8.26 | 68 | 11.8 | -5.12 | -0.51 | -18.47 | 343 |
| 56 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 57 | Heikin-Ashi · 1h | trend | 91.02 | -8.98 | 86 | 25.6 | -33.03 | -5.87 | -33.56 | 691 |
| 58 | MACD zero-line · 1h | trend | 90.81 | -9.19 | 38 | 13.2 | -4.93 | -0.44 | -18.32 | 238 |
| 59 | Donchian 20/10 · 1h | breakout | 90.65 | -9.35 | 31 | 12.9 | 0.01 | 0.22 | -16.18 | 219 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -13.50 | -1.51 | -26.66 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.62 | -1.39 | -23.19 | 214 |
| 62 | RSI(14) reversion | reversion | 87.33 | -12.67 | 179 | 34.6 | -72.40 | -20.98 | -72.45 | 1460 |
| 63 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 84 | 14.3 | -12.45 | -1.60 | -23.45 | 423 |
| 64 | Squeeze breakout | breakout | 82.76 | -17.24 | 175 | 16.0 | -60.31 | -18.32 | -61.02 | 1206 |
| 65 | Donchian 55/20 | breakout | 81.89 | -18.11 | 174 | 18.4 | -68.32 | -15.40 | -68.33 | 1307 |
| 66 | EMA 20/50 cross | trend | 80.12 | -19.89 | 191 | 18.8 | -78.80 | -16.67 | -78.97 | 1481 |
| 67 | Volume breakout | breakout | 79.88 | -20.12 | 157 | 14.0 | -64.12 | -19.98 | -64.12 | 908 |
| 68 | VWAP reversion | reversion | 79.87 | -20.13 | 208 | 28.8 | -71.53 | -17.49 | -71.75 | 1397 |
| 69 | ROC + volume | momentum | 79.77 | -20.23 | 258 | 20.2 | -73.58 | -17.83 | -73.89 | 1668 |
| 70 | AI bee: Bizzy | ai | 77.76 | -22.24 | 405 | 10.1 | — | — | — | — |
| 71 | Z-score reversion | reversion | 77.69 | -22.31 | 274 | 31.0 | -85.84 | -26.93 | -85.86 | 2113 |
| 72 | MFI reversion | reversion | 76.05 | -23.95 | 268 | 22.4 | -88.30 | -33.54 | -88.31 | 2137 |
| 73 | Keltner breakout | breakout | 75.95 | -24.05 | 247 | 13.8 | -85.42 | -32.42 | -85.42 | 1901 |
| 74 | Ichimoku | trend | 75.49 | -24.51 | 211 | 10.0 | -81.58 | -25.55 | -81.58 | 1764 |
| 75 | AI bee: Boozy | ai | 75.22 | -24.78 | 152 | 5.3 | — | — | — | — |
| 76 | Supertrend | trend | 75.17 | -24.83 | 268 | 20.5 | -87.37 | -23.54 | -87.39 | 1952 |
| 77 | Donchian 20/10 | breakout | 71.95 | -28.05 | 347 | 19.3 | -90.92 | -28.26 | -90.92 | 2683 |
| 78 | MACD zero-line | trend | 71.60 | -28.40 | 334 | 17.1 | -91.75 | -32.58 | -91.75 | 2371 |
| 79 | ADX DI cross | trend | 71.02 | -28.98 | 307 | 10.1 | -89.85 | -41.74 | -89.86 | 2126 |
| 80 | Trend pullback | trend | 70.85 | -29.15 | 318 | 17.0 | -91.53 | -32.59 | -91.53 | 2348 |
| 81 | Triple EMA stack | trend | 70.31 | -29.69 | 358 | 16.5 | -93.25 | -34.05 | -93.25 | 2634 |
| 82 | RSI momentum | momentum | 69.84 | -30.16 | 328 | 15.9 | -90.72 | -27.90 | -90.73 | 2401 |
| 83 | Bollinger breakout | breakout | 69.02 | -30.98 | 351 | 16.0 | -93.95 | -38.32 | -93.95 | 2849 |
| 84 | Stochastic reversion | reversion | 67.45 | -32.55 | 520 | 25.8 | -95.85 | -41.27 | -95.86 | 4070 |
| 85 | Consensus | meta | 66.73 | -33.27 | 322 | 9.6 | -94.80 | -29.24 | -94.80 | 2675 |
| 86 | Connors RSI(2) | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.58 | -38.41 | -96.59 | 3646 |
| 87 | Bollinger reversion | reversion | 65.63 | -34.37 | 505 | 18.0 | -95.92 | -40.38 | -95.92 | 3731 |
| 88 | EMA 9/21 cross | trend | 65.31 | -34.69 | 461 | 18.2 | -97.43 | -37.83 | -97.43 | 3561 |
| 89 | Candlestick reversal | reversion | 63.45 | -36.55 | 567 | 16.8 | -99.35 | -43.85 | -99.35 | 5673 |
| 90 | OBV trend | momentum | 63.37 | -36.63 | 516 | 15.5 | -96.16 | -42.98 | -96.17 | 3626 |
| 91 | CCI reversion | reversion | 62.71 | -37.29 | 475 | 17.7 | -98.52 | -44.41 | -98.52 | 4730 |
| 92 | VWAP momentum | momentum | 61.75 | -38.25 | 532 | 9.4 | -98.67 | -34.39 | -98.67 | 5337 |
| 93 | Parabolic SAR | trend | 60.38 | -39.62 | 483 | 14.7 | -97.17 | -48.42 | -97.17 | 3665 |
| 94 | Williams %R | reversion | 58.88 | -41.12 | 586 | 22.9 | -99.53 | -49.43 | -99.53 | 6153 |
| 95 | MACD cross | trend | 58.65 | -41.35 | 555 | 14.6 | -99.72 | -53.61 | -99.72 | 6172 |
| 96 | Heikin-Ashi | trend | 57.05 | -42.95 | 515 | 9.7 | -99.90 | -62.46 | -99.90 | 8352 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-03T03:35 | Williams %R | buy | BTC-USD | 14.74 | — | entry |
| 2026-10-03T03:35 | Williams %R | sell | SOL-USD | 14.69 | -0.06 | exit signal |
| 2026-10-03T03:35 | Stochastic reversion | sell | SOL-USD | 16.81 | -0.06 | exit signal |
| 2026-10-03T03:35 | Bollinger reversion | sell | SOL-USD | 16.39 | -0.06 | exit signal |
| 2026-10-03T03:35 | VWAP momentum | buy | BTC-USD | 15.45 | — | entry signal |
| 2026-10-03T03:35 | Heikin-Ashi | buy | BTC-USD | 14.27 | — | entry signal |
| 2026-10-03T03:35 | Parabolic SAR | buy | SOL-USD | 15.11 | — | entry signal |
| 2026-10-03T03:30 | AI bee: Bizzy | sell | DOGE-USD | 12.27 | -0.09 | Jev: sell (sell p=0.72) after 11 min |
| 2026-10-03T03:30 | CCI reversion | buy | BTC-USD | 15.66 | — | entry signal |
| 2026-10-03T03:30 | CCI reversion | sell | ETH-USD | 15.64 | -0.09 | exit signal |
| 2026-10-03T03:30 | Heikin-Ashi | buy | SOL-USD | 14.29 | — | entry signal |
| 2026-10-03T03:30 | Heikin-Ashi | buy | ETH-USD | 14.29 | — | entry signal |
| 2026-10-03T03:30 | EMA 20/50 cross | sell | ETH-USD | 4.00 | -0.02 | rebalance down |
| 2026-10-03T03:25 | AI bee: Boozy | buy | ETH-USD | 30.75 | — | Jev: buy (buy p=0.61) |
| 2026-10-03T03:25 | Bollinger reversion | sell | DOGE-USD | 16.37 | -0.08 | exit signal |
| 2026-10-03T03:25 | OBV trend | buy | SOL-USD | 15.86 | — | entry signal |
| 2026-10-03T03:25 | OBV trend | buy | DOGE-USD | 15.86 | — | entry signal |
| 2026-10-03T03:25 | VWAP momentum | buy | SOL-USD | 15.46 | — | entry signal |
| 2026-10-03T03:25 | Heikin-Ashi | buy | DOGE-USD | 14.30 | — | entry signal |
| 2026-10-03T03:20 | CCI reversion | buy | XRP-USD | 15.72 | — | entry signal |
| 2026-10-03T03:20 | CCI reversion | buy | SOL-USD | 15.72 | — | entry signal |
| 2026-10-03T03:20 | CCI reversion | buy | ETH-USD | 15.72 | — | entry signal |
| 2026-10-03T03:20 | Bollinger reversion | buy | BTC-USD | 16.43 | — | entry signal |
| 2026-10-03T03:20 | Candlestick reversal | buy | BTC-USD | 15.88 | — | entry signal |
| 2026-10-03T03:20 | Candlestick reversal | sell | DOGE-USD | 15.83 | -0.07 | target is flat |
| 2026-10-03T03:20 | OBV trend | buy | ETH-USD | 15.87 | — | entry signal |
| 2026-10-03T03:20 | VWAP momentum | buy | ETH-USD | 15.47 | — | entry signal |
| 2026-10-03T03:20 | ADX DI cross | buy | SOL-USD | 17.77 | — | entry signal |
| 2026-10-03T03:20 | ADX DI cross | buy | ETH-USD | 17.77 | — | entry signal |
| 2026-10-03T03:20 | Parabolic SAR | buy | DOGE-USD | 15.11 | — | entry signal |
| 2026-10-03T03:20 | Triple EMA stack | buy | ETH-USD | 17.59 | — | entry signal |
| 2026-10-03T03:19 | AI bee: Bizzy | buy | DOGE-USD | 12.35 | — | Jev: buy (buy p=0.63) |
| 2026-10-03T03:15 | MFI reversion | sell | BTC-USD | 18.91 | -0.13 | stop-loss |
| 2026-10-03T03:15 | VWAP reversion | buy | DOGE-USD | 19.97 | — | entry signal |
| 2026-10-03T03:15 | Candlestick reversal | buy | XRP-USD | 15.90 | — | entry signal |
| 2026-10-03T03:15 | Candlestick reversal | buy | SOL-USD | 15.90 | — | entry signal |
| 2026-10-03T03:15 | Candlestick reversal | buy | DOGE-USD | 15.90 | — | entry signal |
| 2026-10-03T03:15 | Triple EMA stack | sell | ETH-USD | 14.09 | -0.07 | exit signal |
| 2026-10-03T03:10 | Stochastic reversion | buy | BTC-USD | 16.86 | — | entry signal |
| 2026-10-03T03:10 | Donchian 55/20 | sell | DOGE-USD | 20.44 | -0.17 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
