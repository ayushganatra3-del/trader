# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T20:10:05.000119+00:00 · 6054 ticks

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

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.96 · VIX 16.02 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 37128 decisions in 2924 calls, $0.4575 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T20:10 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-09-29T20:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T20:10 | 5 / 0 / 0 | ETH-USD 26%, BTC-USD 23% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |
| CCI reversion | AMD | 2.04 | +3.07% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.02 | 1.02 | 2 | 50.0 | 13.82 | 3.01 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | 0.64 | 0.29 | -9.74 | 24 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.05 | 0.05 | 0 | — | 7.20 | 2.96 | -3.62 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.68 | -7.93 | 7 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Hold BTC | benchmark | 99.90 | -0.10 | 0 | — | 31.27 | 3.91 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.71 | -0.29 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.63 | -1.84 | 83 |
| 11 | Agent | meta | 99.68 | -0.32 | 24 | 66.7 | -10.29 | -6.91 | -10.75 | 216 |
| 12 | Agent (aggressive) | meta | 99.56 | -0.44 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.47 | -0.53 | 0 | — | 3.45 | 1.94 | -3.66 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 99.39 | -0.61 | 0 | — | -3.44 | -2.11 | -5.09 | 2 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.33 | -0.67 | 0 | — | -2.80 | -1.36 | -5.14 | 1 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.13 | -0.87 | 20 | 25.0 | -12.94 | -4.42 | -14.72 | 123 |
| 18 | Daily: Bullish score | daily | 99.05 | -0.95 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.01 | -0.99 | 7 | 57.1 | 6.88 | 1.76 | -7.03 | 115 |
| 20 | Z-score reversion · 1h | reversion | 98.86 | -1.14 | 10 | 50.0 | 5.15 | 1.24 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.86 | -1.14 | 2 | 100.0 | -14.25 | -2.83 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Candlestick reversal · 1h | reversion | 98.61 | -1.39 | 20 | 25.0 | -26.29 | -6.63 | -27.08 | 486 |
| 24 | Williams %R · 1h | reversion | 98.59 | -1.41 | 40 | 45.0 | -17.96 | -3.34 | -19.45 | 488 |
| 25 | Stochastic reversion · 1h | reversion | 98.52 | -1.48 | 26 | 53.8 | -13.87 | -3.06 | -15.09 | 328 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.70 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.44 | -1.56 | 0 | — | 23.27 | 3.46 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.25 | -1.75 | 35 | 34.3 | 0.23 | 0.21 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.85 | -2.15 | 45 | 44.4 | -11.43 | -3.67 | -11.77 | 235 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.78 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.79 | -2.21 | 0 | — | -11.11 | -2.29 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.75 | -2.25 | 12 | 8.3 | 16.23 | 1.95 | -14.13 | 127 |
| 34 | Max aggression: 5-day momentum | meta | 97.69 | -2.31 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Bollinger reversion · 1h | reversion | 97.27 | -2.73 | 22 | 27.3 | -17.90 | -4.99 | -18.51 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.63 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.07 | -2.93 | 9 | 11.1 | 15.55 | 2.75 | -5.11 | 92 |
| 38 | Max aggression: 1-day momentum | meta | 96.69 | -3.31 | 2 | 0.0 | -37.93 | -2.25 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.61 | -3.39 | 0 | — | -9.73 | -2.36 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.57 | -3.42 | 18 | 5.6 | 1.99 | 0.47 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.49 | -3.52 | 139 | 12.9 | -0.48 | 0.06 | -12.35 | 385 |
| 42 | Trend pullback · 1h | trend | 96.39 | -3.61 | 27 | 11.1 | -28.54 | -7.01 | -29.65 | 149 |
| 43 | MACD cross · 1h | trend | 96.13 | -3.87 | 40 | 10.0 | -19.11 | -3.27 | -22.23 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.91 | -4.09 | 26 | 11.5 | -7.76 | -0.97 | -18.82 | 292 |
| 45 | Donchian 55/20 · 1h | breakout | 95.84 | -4.16 | 12 | 0.0 | 4.53 | 0.80 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.87 | -16.91 | 684 |
| 47 | MFI reversion · 1h | reversion | 95.43 | -4.57 | 44 | 13.6 | -10.02 | -1.85 | -17.20 | 131 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -50.31 | -28.59 | -50.46 | 608 |
| 49 | Ichimoku · 1h | trend | 95.18 | -4.83 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.91 | -5.09 | 17 | 5.9 | 7.92 | 1.23 | -10.10 | 283 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 1.00 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.28 | -5.72 | 24 | 4.2 | 1.62 | 0.42 | -15.29 | 207 |
| 53 | MACD zero-line · 1h | trend | 94.28 | -5.72 | 20 | 5.0 | -5.22 | -0.55 | -14.64 | 222 |
| 54 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.51 | 1.03 | -12.78 | 214 |
| 55 | ADX DI cross · 1h | trend | 94.02 | -5.98 | 30 | 6.7 | -16.26 | -3.03 | -17.94 | 256 |
| 56 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.33 | 0.27 | -18.68 | 212 |
| 57 | Triple EMA stack · 1h | trend | 93.84 | -6.16 | 30 | 6.7 | -7.71 | -0.75 | -22.58 | 230 |
| 58 | VWAP momentum · 1h | momentum | 93.68 | -6.32 | 103 | 12.6 | -35.21 | -5.37 | -35.53 | 1233 |
| 59 | EMA 9/21 cross · 1h | trend | 93.10 | -6.90 | 43 | 11.6 | -3.83 | -0.33 | -16.92 | 307 |
| 60 | Heikin-Ashi · 1h | trend | 92.88 | -7.12 | 44 | 11.4 | -26.42 | -4.04 | -30.59 | 674 |
| 61 | OBV trend · 1h | momentum | 92.48 | -7.52 | 54 | 7.4 | -10.88 | -1.17 | -25.19 | 315 |
| 62 | RSI(14) reversion | reversion | 90.97 | -9.03 | 118 | 34.7 | -71.10 | -21.65 | -71.21 | 1471 |
| 63 | Squeeze breakout | breakout | 89.86 | -10.14 | 92 | 15.2 | -59.67 | -18.52 | -60.04 | 1192 |
| 64 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.87 | -0.42 | -19.29 | 405 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | ROC + volume | momentum | 87.31 | -12.69 | 148 | 18.9 | -72.43 | -18.16 | -72.48 | 1615 |
| 68 | Volume breakout | breakout | 87.29 | -12.71 | 102 | 15.7 | -62.22 | -20.68 | -62.35 | 894 |
| 69 | EMA 20/50 cross | trend | 87.23 | -12.78 | 121 | 16.5 | -78.53 | -17.54 | -78.59 | 1467 |
| 70 | Donchian 55/20 | breakout | 87.22 | -12.78 | 96 | 15.6 | -68.36 | -15.72 | -68.43 | 1306 |
| 71 | Ichimoku | trend | 86.15 | -13.85 | 109 | 9.2 | -80.46 | -26.19 | -80.51 | 1744 |
| 72 | Keltner breakout | breakout | 85.64 | -14.36 | 148 | 13.5 | -85.01 | -34.56 | -85.05 | 1905 |
| 73 | Z-score reversion | reversion | 85.08 | -14.92 | 180 | 32.8 | -84.37 | -27.64 | -84.41 | 2093 |
| 74 | VWAP reversion | reversion | 84.68 | -15.32 | 137 | 22.6 | -71.86 | -17.64 | -72.20 | 1399 |
| 75 | MACD zero-line | trend | 83.15 | -16.85 | 196 | 16.8 | -91.66 | -35.84 | -91.68 | 2350 |
| 76 | Supertrend | trend | 82.45 | -17.55 | 175 | 18.3 | -87.46 | -24.92 | -87.48 | 1960 |
| 77 | Donchian 20/10 | breakout | 81.48 | -18.52 | 203 | 17.7 | -90.95 | -29.68 | -90.99 | 2681 |
| 78 | MFI reversion | reversion | 81.43 | -18.57 | 181 | 19.9 | -87.87 | -36.54 | -87.91 | 2138 |
| 79 | Bollinger breakout | breakout | 81.26 | -18.75 | 202 | 16.8 | -93.91 | -42.35 | -93.94 | 2868 |
| 80 | Triple EMA stack | trend | 80.76 | -19.24 | 211 | 15.6 | -93.09 | -36.19 | -93.10 | 2623 |
| 81 | RSI momentum | momentum | 80.47 | -19.53 | 194 | 13.4 | -90.41 | -29.56 | -90.41 | 2380 |
| 82 | ADX DI cross | trend | 79.74 | -20.26 | 193 | 8.3 | -89.32 | -47.17 | -89.35 | 2112 |
| 83 | Trend pullback | trend | 79.54 | -20.46 | 168 | 17.3 | -91.00 | -35.26 | -91.00 | 2287 |
| 84 | EMA 9/21 cross | trend | 77.80 | -22.20 | 270 | 17.8 | -97.39 | -41.94 | -97.39 | 3529 |
| 85 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.46 | -43.05 | -96.46 | 3638 |
| 86 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.47 | -30.23 | -94.48 | 2632 |
| 87 | Candlestick reversal ⏸ | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.35 | -50.99 | -99.35 | 5570 |
| 88 | Stochastic reversion | reversion | 76.11 | -23.89 | 323 | 24.5 | -95.94 | -47.21 | -95.94 | 4060 |
| 89 | OBV trend | momentum | 75.84 | -24.16 | 268 | 15.7 | -95.96 | -48.73 | -95.96 | 3535 |
| 90 | Bollinger reversion | reversion | 75.07 | -24.93 | 303 | 15.8 | -95.77 | -45.47 | -95.77 | 3683 |
| 91 | VWAP momentum | momentum | 73.99 | -26.01 | 364 | 10.4 | -98.41 | -35.97 | -98.42 | 5154 |
| 92 | CCI reversion | reversion | 73.64 | -26.36 | 232 | 11.6 | -98.44 | -51.79 | -98.45 | 4695 |
| 93 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -96.98 | -56.62 | -96.99 | 3631 |
| 94 | MACD cross | trend | 72.54 | -27.46 | 268 | 14.2 | -99.71 | -66.94 | -99.71 | 6067 |
| 95 | Williams %R ⏸ | reversion | 71.59 | -28.41 | 340 | 21.2 | -99.52 | -60.93 | -99.52 | 6106 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -88.76 | -99.89 | 8300 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T20:10 | CCI reversion | buy | XRP-USD | 18.47 | — | entry signal |
| 2026-09-29T20:10 | CCI reversion | buy | SOL-USD | 18.47 | — | entry signal |
| 2026-09-29T20:10 | CCI reversion | buy | ETH-USD | 18.47 | — | entry signal |
| 2026-09-29T20:10 | CCI reversion | buy | DOGE-USD | 18.47 | — | entry signal |
| 2026-09-29T20:10 | Triple EMA stack | sell | ETH-USD | 20.12 | -0.14 | exit signal |
| 2026-09-29T20:10 | EMA 9/21 cross | sell | SOL-USD | 19.43 | -0.12 | exit signal |
| 2026-09-29T20:05 | RSI momentum | sell | SOL-USD | 20.08 | -0.14 | exit signal |
| 2026-09-29T20:05 | RSI momentum | sell | ETH-USD | 20.07 | -0.15 | exit signal |
| 2026-09-29T20:05 | EMA 20/50 cross | sell | SOL-USD | 21.77 | -0.14 | stop-loss |
| 2026-09-29T20:05 | EMA 20/50 cross | sell | ETH-USD | 21.76 | -0.15 | stop-loss |
| 2026-09-29T20:00 | Triple EMA stack · 1h | sell | ETH-USD | 23.58 | -0.23 | exit signal |
| 2026-09-29T20:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 18.62 | -0.32 | exit signal |
| 2026-09-29T20:00 | EMA 9/21 cross | sell | XRP-USD | 19.38 | -0.12 | exit signal |
| 2026-09-29T19:55 | Agent (rotation) | sell | SQQQ | 32.71 | -0.11 | selected signal exited |
| 2026-09-29T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 101.02 | -0.34 | target is flat |
| 2026-09-29T19:55 | Consensus | sell | META | 19.47 | 0.21 | target is flat |
| 2026-09-29T19:55 | MFI reversion | buy | ETH-USD | 20.39 | — | entry signal |
| 2026-09-29T19:55 | MFI reversion | sell | SQQQ | 20.43 | -0.08 | end-of-day flatten |
| 2026-09-29T19:55 | MFI reversion | sell | SOXL | 20.23 | -0.19 | end-of-day flatten |
| 2026-09-29T19:55 | MFI reversion | sell | PLTR | 16.42 | 0.04 | end-of-day flatten |
| 2026-09-29T19:55 | MFI reversion | sell | NVDA | 16.30 | -0.06 | end-of-day flatten |
| 2026-09-29T19:55 | CCI reversion | sell | SQQQ | 18.48 | -0.04 | end-of-day flatten |
| 2026-09-29T19:55 | CCI reversion | sell | NVDA | 18.48 | -0.06 | end-of-day flatten |
| 2026-09-29T19:55 | CCI reversion | sell | COIN | 18.48 | -0.05 | end-of-day flatten |
| 2026-09-29T19:55 | Stochastic reversion | buy | XRP-USD | 19.07 | — | entry signal |
| 2026-09-29T19:55 | Stochastic reversion | buy | SOL-USD | 19.07 | — | entry signal |
| 2026-09-29T19:55 | Stochastic reversion | buy | DOGE-USD | 19.07 | — | entry signal |
| 2026-09-29T19:55 | Stochastic reversion | sell | SOXL | 19.11 | -0.01 | end-of-day flatten |
| 2026-09-29T19:55 | Stochastic reversion | sell | NVDA | 15.29 | -0.04 | end-of-day flatten |
| 2026-09-29T19:55 | VWAP reversion | sell | TECL | 12.08 | 0.00 | end-of-day flatten |
| 2026-09-29T19:55 | VWAP reversion | sell | NVDA | 14.09 | -0.03 | end-of-day flatten |
| 2026-09-29T19:55 | VWAP reversion | sell | MSTR | 12.10 | 0.02 | end-of-day flatten |
| 2026-09-29T19:55 | VWAP reversion | sell | ETHU | 12.05 | 0.01 | end-of-day flatten |
| 2026-09-29T19:55 | VWAP reversion | sell | COIN | 12.16 | -0.00 | end-of-day flatten |
| 2026-09-29T19:55 | VWAP reversion | sell | BITX | 12.10 | 0.07 | end-of-day flatten |
| 2026-09-29T19:55 | Z-score reversion | sell | NVDA | 21.26 | -0.08 | end-of-day flatten |
| 2026-09-29T19:55 | Bollinger reversion | sell | AMD | 18.73 | -0.05 | end-of-day flatten |
| 2026-09-29T19:55 | RSI(14) reversion | sell | NVDA | 22.73 | -0.07 | end-of-day flatten |
| 2026-09-29T19:55 | RSI(14) reversion | sell | COIN | 22.71 | -0.07 | end-of-day flatten |
| 2026-09-29T19:55 | Squeeze breakout | sell | TNA | 17.92 | 0.05 | end-of-day flatten |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
