# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T20:10:05.000134+00:00 · 7238 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.63 (-0.37%)

Closed trades 27, win rate 66.7%, fees £0.80, max drawdown -1.39%.

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

### Market regime (QQQ, 2026-09-30)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.26 · VIX 16.42 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, META 7.4, MSFT 7.2, AMD 7.2, ETHU 7.0, BITX 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 37818 decisions in 3006 calls, $0.4662 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T20:10 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-09-30T20:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T20:10 | 1 / 4 / 0 | cash |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.70 | 0.70 | 3 | 33.3 | 13.60 | 2.94 | -7.55 | 43 |
| 2 | Copy: Congress Democrats (NANC) | copy | 100.15 | 0.15 | 0 | — | 6.54 | 2.71 | -3.62 | 1 |
| 3 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 4 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 5 | Hold BTC | benchmark | 99.68 | -0.32 | 0 | — | 28.75 | 3.62 | -8.68 | 1 |
| 6 | Agent | meta | 99.63 | -0.37 | 27 | 66.7 | -10.23 | -6.84 | -10.80 | 224 |
| 7 | Copy: Hedge-fund gurus (GURU) | copy | 99.54 | -0.46 | 0 | — | -2.19 | -1.03 | -5.14 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.65 | 1.35 | -2.11 | 83 |
| 9 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -1.50 | -0.81 | -4.46 | 99 |
| 10 | VWAP reversion · 1h | reversion | 99.42 | -0.58 | 22 | 27.3 | -12.15 | -4.14 | -14.30 | 123 |
| 11 | RSI(14) reversion · 1h | reversion | 99.40 | -0.60 | 8 | 62.5 | 1.82 | 0.57 | -7.26 | 137 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 99.37 | -0.63 | 0 | — | -3.22 | -1.95 | -5.09 | 2 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 14 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 2 | 50.0 | -1.10 | -0.29 | -9.74 | 24 |
| 15 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 16 | Hold SPY | benchmark | 98.98 | -1.02 | 0 | — | 2.90 | 1.62 | -3.66 | 1 |
| 17 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 14.96 | 3.71 | -4.73 | 182 |
| 18 | Stochastic reversion · 1h | reversion | 98.66 | -1.34 | 30 | 56.7 | -10.26 | -2.28 | -11.63 | 324 |
| 19 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 20 | Copy: Warren Buffett (BRK-B) | copy | 98.61 | -1.39 | 0 | — | -2.23 | -0.87 | -7.65 | 1 |
| 21 | Daily: Bullish score | daily | 98.48 | -1.52 | 3 | 0.0 | -1.05 | 0.05 | -12.76 | 14 |
| 22 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.54 | 0.27 | -15.21 | 46 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 98.25 | -1.75 | 0 | — | -10.46 | -2.12 | -15.27 | 2 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.22 | -1.78 | 0 | — | 2.43 | 0.76 | -7.93 | 7 |
| 25 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.58 | -3.34 | -11.47 | 232 |
| 26 | Copy: Insider buying | copy | 98.15 | -1.85 | 2 | 100.0 | -14.76 | -2.92 | -17.74 | 73 |
| 27 | CCI reversion · 1h | reversion | 98.13 | -1.88 | 42 | 40.5 | 1.52 | 0.42 | -12.41 | 414 |
| 28 | Williams %R · 1h | reversion | 98.11 | -1.89 | 51 | 51.0 | -17.38 | -3.27 | -19.41 | 490 |
| 29 | Candlestick reversal · 1h | reversion | 97.84 | -2.16 | 33 | 24.2 | -26.62 | -6.69 | -27.33 | 496 |
| 30 | Agent (rotation) | meta | 97.76 | -2.24 | 37 | 13.5 | -5.52 | -1.91 | -9.79 | 208 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 97.75 | -2.25 | 0 | — | 26.25 | 3.86 | -6.29 | 1 |
| 32 | Z-score reversion · 1h | reversion | 97.60 | -2.40 | 11 | 45.5 | 3.24 | 0.82 | -8.60 | 153 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.37 | -2.63 | 0 | — | -7.64 | -1.79 | -10.03 | 1 |
| 34 | Bollinger reversion · 1h | reversion | 96.94 | -3.06 | 32 | 34.4 | -16.89 | -4.73 | -17.77 | 306 |
| 35 | EMA 20/50 cross · 1h | trend | 96.33 | -3.67 | 19 | 5.3 | 15.07 | 1.90 | -12.18 | 130 |
| 36 | Opening range 30m | breakout | 96.12 | -3.88 | 49 | 12.2 | -11.24 | -3.27 | -15.06 | 559 |
| 37 | Supertrend · 1h | trend | 95.79 | -4.21 | 19 | 5.3 | 0.69 | 0.29 | -16.43 | 203 |
| 38 | Agent (ML meta-label) | meta | 95.45 | -4.55 | 170 | 12.9 | 4.50 | 0.92 | -13.06 | 411 |
| 39 | Trend pullback · 1h | trend | 95.41 | -4.59 | 33 | 12.1 | -26.13 | -6.99 | -26.13 | 156 |
| 40 | Max aggression: 5-day momentum | meta | 95.36 | -4.64 | 3 | 66.7 | -13.55 | -0.96 | -29.56 | 29 |
| 41 | Donchian 55/20 · 1h | breakout | 95.34 | -4.66 | 15 | 0.0 | 4.58 | 0.80 | -16.96 | 113 |
| 42 | Opening range 15m | breakout | 94.87 | -5.13 | 61 | 14.8 | -12.31 | -3.38 | -17.03 | 686 |
| 43 | Squeeze breakout · 1h | breakout | 94.49 | -5.51 | 16 | 6.2 | 11.75 | 2.08 | -7.61 | 99 |
| 44 | Three white soldiers | momentum | 94.48 | -5.52 | 51 | 19.6 | -50.21 | -27.72 | -50.28 | 605 |
| 45 | MFI reversion · 1h | reversion | 94.42 | -5.58 | 51 | 19.6 | -9.34 | -1.69 | -17.05 | 131 |
| 46 | Parabolic SAR · 1h | trend | 94.32 | -5.68 | 32 | 12.5 | -9.68 | -1.25 | -19.53 | 303 |
| 47 | MACD cross · 1h | trend | 94.11 | -5.89 | 46 | 8.7 | -14.30 | -2.26 | -17.47 | 477 |
| 48 | Max aggression: 1-day momentum | meta | 94.00 | -6.00 | 3 | 33.3 | -21.69 | -1.04 | -41.28 | 42 |
| 49 | Volume breakout · 1h | breakout | 93.79 | -6.21 | 29 | 3.4 | 5.32 | 0.94 | -12.60 | 122 |
| 50 | ADX DI cross · 1h | trend | 93.69 | -6.31 | 35 | 5.7 | -16.00 | -3.02 | -17.41 | 260 |
| 51 | Ichimoku · 1h | trend | 92.89 | -7.11 | 21 | 14.3 | 4.66 | 0.75 | -15.26 | 122 |
| 52 | RSI momentum · 1h | momentum | 92.49 | -7.51 | 30 | 3.3 | -3.55 | -0.29 | -16.03 | 221 |
| 53 | VWAP momentum · 1h | momentum | 92.24 | -7.76 | 127 | 15.7 | -39.17 | -6.29 | -39.25 | 1247 |
| 54 | Bollinger breakout · 1h | breakout | 92.18 | -7.82 | 25 | 8.0 | 5.14 | 0.87 | -10.46 | 280 |
| 55 | Triple EMA stack · 1h | trend | 91.27 | -8.73 | 40 | 5.0 | -8.71 | -0.87 | -22.23 | 233 |
| 56 | EMA 9/21 cross · 1h | trend | 91.10 | -8.90 | 50 | 10.0 | -8.61 | -1.00 | -17.38 | 320 |
| 57 | Keltner breakout · 1h | breakout | 90.92 | -9.08 | 15 | 0.0 | -8.65 | -1.01 | -20.62 | 218 |
| 58 | MACD zero-line · 1h | trend | 90.89 | -9.11 | 28 | 3.6 | -9.26 | -1.11 | -17.32 | 232 |
| 59 | RSI(14) reversion | reversion | 90.66 | -9.34 | 130 | 35.4 | -71.48 | -21.62 | -71.55 | 1477 |
| 60 | Heikin-Ashi · 1h | trend | 90.65 | -9.35 | 59 | 8.5 | -28.97 | -4.77 | -31.77 | 684 |
| 61 | Donchian 20/10 · 1h | breakout | 90.02 | -9.98 | 23 | 8.7 | -1.28 | 0.05 | -14.90 | 218 |
| 62 | OBV trend · 1h | momentum | 88.92 | -11.08 | 70 | 5.7 | -14.46 | -1.67 | -25.03 | 322 |
| 63 | Squeeze breakout | breakout | 87.41 | -12.59 | 110 | 13.6 | -59.64 | -18.48 | -59.71 | 1182 |
| 64 | ROC + volume · 1h | momentum | 86.39 | -13.61 | 60 | 5.0 | -15.11 | -2.02 | -22.35 | 413 |
| 65 | Donchian 55/20 | breakout | 86.05 | -13.95 | 120 | 20.0 | -67.30 | -15.26 | -67.38 | 1292 |
| 66 | Volume breakout | breakout | 85.14 | -14.86 | 115 | 15.7 | -62.64 | -20.19 | -62.73 | 894 |
| 67 | ROC + volume | momentum | 84.44 | -15.56 | 183 | 20.2 | -72.18 | -17.58 | -72.21 | 1625 |
| 68 | Keltner breakout | breakout | 83.44 | -16.56 | 174 | 14.9 | -84.62 | -34.44 | -84.64 | 1886 |
| 69 | Ichimoku | trend | 83.10 | -16.90 | 138 | 10.1 | -80.29 | -25.51 | -80.29 | 1741 |
| 70 | EMA 20/50 cross | trend | 83.06 | -16.93 | 150 | 16.0 | -79.11 | -17.51 | -79.12 | 1468 |
| 71 | VWAP reversion | reversion | 82.98 | -17.02 | 161 | 24.8 | -72.21 | -18.00 | -72.23 | 1405 |
| 72 | Z-score reversion | reversion | 82.83 | -17.17 | 205 | 31.2 | -85.07 | -28.11 | -85.09 | 2104 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 79.96 | -20.04 | 204 | 19.1 | -87.52 | -24.35 | -87.58 | 1942 |
| 76 | Donchian 20/10 | breakout | 78.82 | -21.18 | 248 | 19.4 | -90.63 | -29.09 | -90.63 | 2663 |
| 77 | MFI reversion | reversion | 78.77 | -21.23 | 205 | 19.5 | -88.24 | -35.55 | -88.24 | 2129 |
| 78 | MACD zero-line | trend | 78.76 | -21.24 | 246 | 16.3 | -91.65 | -34.93 | -91.65 | 2350 |
| 79 | Trend pullback | trend | 77.79 | -22.21 | 213 | 16.9 | -90.86 | -33.12 | -90.86 | 2271 |
| 80 | RSI momentum | momentum | 77.30 | -22.70 | 239 | 15.5 | -90.29 | -28.55 | -90.29 | 2372 |
| 81 | Triple EMA stack | trend | 77.13 | -22.87 | 257 | 16.3 | -92.87 | -34.80 | -92.87 | 2588 |
| 82 | Bollinger breakout | breakout | 77.12 | -22.88 | 251 | 16.3 | -93.84 | -42.13 | -93.85 | 2846 |
| 83 | ADX DI cross | trend | 75.94 | -24.06 | 237 | 8.0 | -89.44 | -44.40 | -89.44 | 2107 |
| 84 | Stochastic reversion | reversion | 73.40 | -26.60 | 388 | 24.2 | -95.92 | -45.80 | -95.92 | 4049 |
| 85 | EMA 9/21 cross | trend | 73.07 | -26.93 | 337 | 16.9 | -97.37 | -41.11 | -97.37 | 3531 |
| 86 | Consensus | meta | 72.98 | -27.02 | 230 | 7.4 | -94.70 | -30.51 | -94.70 | 2666 |
| 87 | Connors RSI(2) ⏸ | reversion | 72.37 | -27.63 | 319 | 19.7 | -96.49 | -40.71 | -96.49 | 3639 |
| 88 | Bollinger reversion | reversion | 71.68 | -28.32 | 363 | 17.4 | -95.89 | -44.33 | -95.89 | 3692 |
| 89 | Candlestick reversal ⏸ | reversion | 71.29 | -28.71 | 376 | 14.4 | -99.37 | -49.02 | -99.37 | 5618 |
| 90 | OBV trend ⏸ | momentum | 70.20 | -29.80 | 361 | 16.1 | -95.93 | -45.84 | -95.93 | 3538 |
| 91 | CCI reversion | reversion | 69.76 | -30.23 | 317 | 13.2 | -98.51 | -49.69 | -98.51 | 4698 |
| 92 | Parabolic SAR | trend | 69.41 | -30.59 | 329 | 13.4 | -96.91 | -51.98 | -96.92 | 3609 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.55 | -35.83 | -98.55 | 5224 |
| 94 | MACD cross ⏸ | trend | 67.57 | -32.43 | 368 | 14.1 | -99.72 | -62.77 | -99.72 | 6068 |
| 95 | Williams %R ⏸ | reversion | 67.21 | -32.79 | 441 | 22.0 | -99.54 | -57.35 | -99.54 | 6116 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -75.74 | -99.89 | 8280 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T20:10 | CCI reversion | buy | SOL-USD | 17.45 | — | entry signal |
| 2026-09-30T20:10 | Z-score reversion | buy | BTC-USD | 4.13 | — | rebalance up |
| 2026-09-30T20:10 | Z-score reversion | sell | ETH-USD | 4.13 | -0.03 | rebalance down |
| 2026-09-30T20:05 | CCI reversion | buy | XRP-USD | 17.46 | — | entry signal |
| 2026-09-30T20:05 | Z-score reversion | buy | BTC-USD | 4.15 | — | rebalance up |
| 2026-09-30T20:05 | Z-score reversion | sell | SOL-USD | 4.15 | -0.03 | rebalance down |
| 2026-09-30T20:01 | Agent (ML meta-label) | sell | SOL-USD | 4.94 | -0.14 | selected signal exited |
| 2026-09-30T20:01 | Trend pullback · 1h | sell | BTC-USD | 11.92 | -0.13 | exit signal |
| 2026-09-30T20:01 | Supertrend · 1h | sell | SOL-USD | 1.76 | -0.08 | exit signal |
| 2026-09-30T20:01 | MACD zero-line · 1h | sell | BTC-USD | 18.23 | -0.15 | exit signal |
| 2026-09-30T20:01 | MACD cross · 1h | sell | BTC-USD | 5.27 | -0.13 | exit signal |
| 2026-09-30T20:01 | EMA 9/21 cross · 1h | sell | XRP-USD | 10.32 | -0.21 | exit signal |
| 2026-09-30T20:01 | EMA 9/21 cross · 1h | sell | ETH-USD | 10.13 | -0.25 | exit signal |
| 2026-09-30T20:01 | Stochastic reversion | buy | SOL-USD | 18.38 | — | entry signal |
| 2026-09-30T20:01 | Stochastic reversion | buy | ETH-USD | 18.38 | — | entry signal |
| 2026-09-30T20:01 | Stochastic reversion | buy | BTC-USD | 18.38 | — | entry signal |
| 2026-09-30T20:01 | Z-score reversion | buy | BTC-USD | 8.30 | — | entry signal |
| 2026-09-30T20:01 | Z-score reversion | sell | XRP-USD | 4.14 | -0.04 | rebalance down |
| 2026-09-30T20:01 | Z-score reversion | sell | DOGE-USD | 4.16 | -0.02 | rebalance down |
| 2026-09-30T20:01 | Bollinger reversion | buy | XRP-USD | 17.95 | — | entry signal |
| 2026-09-30T20:01 | Bollinger reversion | buy | ETH-USD | 17.95 | — | entry signal |
| 2026-09-30T20:01 | Bollinger reversion | buy | BTC-USD | 17.95 | — | entry signal |
| 2026-09-30T19:55 | Agent (rotation) | sell | TQQQ | 32.44 | -0.15 | selected signal exited |
| 2026-09-30T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 99.23 | -1.01 | target is flat |
| 2026-09-30T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 99.33 | -1.15 | target is flat |
| 2026-09-30T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 100.70 | -0.33 | target is flat |
| 2026-09-30T19:55 | Agent (ML meta-label) | buy | TNA | 4.78 | — | entry |
| 2026-09-30T19:55 | Agent (ML meta-label) | buy | MSFT | 4.78 | — | following Z-score reversion |
| 2026-09-30T19:55 | Agent (ML meta-label) | sell | XRP-USD | 2.28 | -0.03 | selected signal exited |
| 2026-09-30T19:55 | Agent (ML meta-label) | sell | GOOGL | 4.51 | -0.04 | selected signal exited |
| 2026-09-30T19:55 | Consensus | sell | SOXL | 18.22 | 0.00 | target is flat |
| 2026-09-30T19:55 | Consensus | sell | GOOGL | 18.04 | -0.37 | target is flat |
| 2026-09-30T19:55 | Consensus | sell | AMD | 14.68 | -0.01 | target is flat |
| 2026-09-30T19:55 | Agent | sell | TQQQ | 19.73 | -0.18 | selected signal exited |
| 2026-09-30T19:55 | MFI reversion · 1h | buy | SQQQ | 9.22 | — | entry |
| 2026-09-30T19:55 | MFI reversion · 1h | buy | SPY | 6.12 | — | rebalance up |
| 2026-09-30T19:55 | MFI reversion · 1h | sell | UPRO | 7.70 | -0.10 | rebalance down |
| 2026-09-30T19:55 | MFI reversion · 1h | sell | SOL-USD | 7.64 | -0.19 | rebalance down |
| 2026-09-30T19:55 | Bollinger reversion · 1h | buy | MSTR | 4.86 | — | rebalance up |
| 2026-09-30T19:55 | Volume breakout · 1h | sell | GOOGL | 23.08 | -0.49 | stop-loss |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
