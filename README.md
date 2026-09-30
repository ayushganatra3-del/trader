# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T19:41:05.000171+00:00 · 7217 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.86 (-0.14%)

Closed trades 26, win rate 69.2%, fees £0.79, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TQQQ | 19.95 | +0.04 |

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

Today: 36456 decisions in 2943 calls, $0.4500 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T19:41 | 0 / 18 / 11 | cash |  |
| Breezy | 2026-09-30T19:41 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-09-30T19:41 | 4 / 24 / 1 | COIN 76% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.85 | 1.85 | 2 | 50.0 | 14.90 | 3.20 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.72 | 1.11 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.37 | 0.37 | 1 | 100.0 | 0.04 | 0.09 | -9.74 | 24 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.15 | 0.15 | 0 | — | 6.54 | 2.71 | -3.62 | 1 |
| 5 | Hold BTC | benchmark | 100.08 | 0.07 | 0 | — | 29.04 | 3.65 | -8.68 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 99.87 | -0.12 | 0 | — | -2.72 | -1.61 | -5.09 | 2 |
| 9 | Agent | meta | 99.86 | -0.14 | 26 | 69.2 | -10.22 | -6.74 | -10.86 | 222 |
| 10 | Timing: Nasdaq FTD · TQQQ | daily | 99.69 | -0.31 | 0 | — | -9.15 | -1.78 | -15.27 | 2 |
| 11 | VWAP reversion · 1h | reversion | 99.66 | -0.34 | 22 | 27.3 | -12.50 | -4.18 | -14.84 | 124 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 99.54 | -0.46 | 0 | — | -2.19 | -1.03 | -5.14 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.49 | -0.51 | 9 | 33.3 | 2.65 | 1.35 | -2.11 | 83 |
| 14 | Agent (aggressive) | meta | 99.49 | -0.51 | 11 | 54.5 | -1.50 | -0.81 | -4.46 | 99 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.49 | -0.51 | 0 | — | 3.68 | 1.10 | -7.93 | 7 |
| 16 | Hold SPY | benchmark | 99.45 | -0.55 | 0 | — | 3.67 | 2.01 | -3.66 | 1 |
| 17 | RSI(14) reversion · 1h | reversion | 99.38 | -0.62 | 8 | 62.5 | 2.46 | 0.73 | -7.28 | 136 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 19 | Daily: Bullish score | daily | 99.08 | -0.92 | 3 | 0.0 | -0.42 | 0.14 | -12.76 | 14 |
| 20 | Stochastic reversion · 1h | reversion | 99.06 | -0.94 | 30 | 56.7 | -9.86 | -2.18 | -11.66 | 324 |
| 21 | Copy: Insider buying | copy | 98.79 | -1.21 | 2 | 100.0 | -14.17 | -2.79 | -17.74 | 73 |
| 22 | Copy: Warren Buffett (BRK-B) | copy | 98.79 | -1.21 | 0 | — | -2.21 | -0.87 | -7.65 | 1 |
| 23 | Gap and go | momentum | 98.69 | -1.31 | 12 | 16.7 | 14.70 | 3.64 | -4.73 | 183 |
| 24 | Williams %R · 1h | reversion | 98.68 | -1.32 | 51 | 51.0 | -17.31 | -3.25 | -19.41 | 491 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 26 | CCI reversion · 1h | reversion | 98.57 | -1.43 | 42 | 40.5 | 2.01 | 0.50 | -12.41 | 414 |
| 27 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.56 | 0.27 | -15.21 | 46 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.33 | -1.67 | 0 | — | 27.21 | 3.98 | -6.29 | 1 |
| 29 | Candlestick reversal · 1h | reversion | 98.23 | -1.77 | 33 | 24.2 | -26.11 | -6.53 | -27.30 | 496 |
| 30 | Connors RSI(2) · 1h | reversion | 98.16 | -1.84 | 49 | 46.9 | -10.58 | -3.34 | -11.47 | 232 |
| 31 | Agent (rotation) | meta | 98.14 | -1.86 | 36 | 13.9 | -5.16 | -1.78 | -9.79 | 208 |
| 32 | Z-score reversion · 1h | reversion | 98.12 | -1.88 | 11 | 45.5 | 4.19 | 1.03 | -8.60 | 155 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 98.08 | -1.92 | 0 | — | -6.85 | -1.56 | -10.03 | 1 |
| 34 | Bollinger reversion · 1h | reversion | 97.71 | -2.29 | 32 | 34.4 | -16.25 | -4.50 | -17.79 | 307 |
| 35 | EMA 20/50 cross · 1h | trend | 97.52 | -2.48 | 18 | 5.6 | 16.62 | 2.07 | -12.18 | 130 |
| 36 | Opening range 30m | breakout | 96.76 | -3.24 | 42 | 11.9 | -9.74 | -2.81 | -14.44 | 560 |
| 37 | Donchian 55/20 · 1h | breakout | 96.33 | -3.67 | 15 | 0.0 | 5.68 | 0.94 | -16.96 | 113 |
| 38 | Supertrend · 1h | trend | 96.32 | -3.69 | 18 | 5.6 | 1.29 | 0.37 | -16.43 | 201 |
| 39 | Agent (ML meta-label) | meta | 96.14 | -3.86 | 162 | 13.6 | 7.57 | 1.36 | -11.91 | 391 |
| 40 | Trend pullback · 1h | trend | 96.12 | -3.88 | 32 | 12.5 | -25.55 | -6.82 | -25.81 | 156 |
| 41 | Max aggression: 5-day momentum | meta | 96.09 | -3.91 | 3 | 66.7 | -12.89 | -0.89 | -29.56 | 29 |
| 42 | Opening range 15m | breakout | 95.67 | -4.33 | 52 | 11.5 | -10.86 | -2.91 | -16.70 | 687 |
| 43 | Parabolic SAR · 1h | trend | 95.07 | -4.93 | 31 | 12.9 | -8.67 | -1.10 | -19.53 | 303 |
| 44 | Squeeze breakout · 1h | breakout | 94.94 | -5.06 | 15 | 6.7 | 12.29 | 2.18 | -7.19 | 99 |
| 45 | MACD cross · 1h | trend | 94.84 | -5.16 | 45 | 8.9 | -13.59 | -2.14 | -17.47 | 477 |
| 46 | MFI reversion · 1h | reversion | 94.84 | -5.16 | 51 | 19.6 | -9.32 | -1.69 | -17.08 | 130 |
| 47 | Max aggression: 1-day momentum | meta | 94.72 | -5.28 | 3 | 33.3 | -21.09 | -1.00 | -41.28 | 42 |
| 48 | Three white soldiers | momentum | 94.48 | -5.52 | 51 | 19.6 | -50.24 | -27.70 | -50.32 | 606 |
| 49 | ADX DI cross · 1h | trend | 94.40 | -5.60 | 34 | 5.9 | -15.08 | -2.82 | -17.39 | 259 |
| 50 | Volume breakout · 1h | breakout | 94.24 | -5.76 | 28 | 3.6 | 5.82 | 1.01 | -12.60 | 122 |
| 51 | Ichimoku · 1h | trend | 94.04 | -5.96 | 20 | 15.0 | 5.96 | 0.89 | -15.13 | 122 |
| 52 | RSI momentum · 1h | momentum | 93.47 | -6.53 | 28 | 3.6 | -2.93 | -0.20 | -15.43 | 222 |
| 53 | Bollinger breakout · 1h | breakout | 93.15 | -6.85 | 24 | 8.3 | 5.94 | 0.97 | -9.71 | 280 |
| 54 | VWAP momentum · 1h | momentum | 93.01 | -6.99 | 127 | 15.7 | -38.60 | -6.20 | -38.97 | 1247 |
| 55 | Triple EMA stack · 1h | trend | 92.46 | -7.54 | 37 | 5.4 | -7.86 | -0.77 | -22.10 | 233 |
| 56 | EMA 9/21 cross · 1h | trend | 91.96 | -8.04 | 47 | 10.6 | -7.71 | -0.87 | -16.92 | 320 |
| 57 | MACD zero-line · 1h | trend | 91.80 | -8.20 | 26 | 3.8 | -8.28 | -0.98 | -16.50 | 232 |
| 58 | Keltner breakout · 1h | breakout | 91.79 | -8.21 | 14 | 0.0 | -8.83 | -1.04 | -20.06 | 216 |
| 59 | Heikin-Ashi · 1h | trend | 91.28 | -8.72 | 59 | 8.5 | -28.43 | -4.67 | -31.39 | 684 |
| 60 | Donchian 20/10 · 1h | breakout | 91.20 | -8.80 | 21 | 9.5 | 0.33 | 0.26 | -14.01 | 217 |
| 61 | RSI(14) reversion | reversion | 90.98 | -9.02 | 129 | 35.7 | -71.24 | -21.34 | -71.41 | 1477 |
| 62 | OBV trend · 1h | momentum | 89.78 | -10.22 | 68 | 5.9 | -14.08 | -1.62 | -25.03 | 323 |
| 63 | Squeeze breakout | breakout | 87.44 | -12.56 | 109 | 12.8 | -59.58 | -18.45 | -59.67 | 1180 |
| 64 | ROC + volume · 1h | momentum | 87.42 | -12.57 | 59 | 5.1 | -14.19 | -1.90 | -21.75 | 413 |
| 65 | Donchian 55/20 | breakout | 86.21 | -13.79 | 118 | 18.6 | -67.24 | -15.23 | -67.38 | 1292 |
| 66 | Volume breakout | breakout | 85.18 | -14.82 | 114 | 14.9 | -62.75 | -20.21 | -62.80 | 892 |
| 67 | ROC + volume | momentum | 84.59 | -15.41 | 181 | 19.9 | -72.24 | -17.64 | -72.30 | 1626 |
| 68 | Keltner breakout | breakout | 83.58 | -16.42 | 172 | 14.5 | -84.65 | -34.55 | -84.69 | 1889 |
| 69 | VWAP reversion | reversion | 83.47 | -16.53 | 154 | 24.7 | -71.73 | -17.84 | -71.88 | 1409 |
| 70 | Z-score reversion | reversion | 83.35 | -16.66 | 201 | 31.8 | -84.98 | -27.97 | -85.01 | 2103 |
| 71 | EMA 20/50 cross | trend | 83.19 | -16.80 | 146 | 14.4 | -78.90 | -17.43 | -78.95 | 1471 |
| 72 | Ichimoku | trend | 83.10 | -16.90 | 138 | 10.1 | -80.29 | -25.51 | -80.29 | 1741 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | Supertrend | trend | 80.21 | -19.79 | 199 | 18.1 | -87.32 | -24.24 | -87.45 | 1949 |
| 76 | MFI reversion | reversion | 79.43 | -20.57 | 200 | 19.5 | -88.09 | -35.17 | -88.13 | 2130 |
| 77 | Donchian 20/10 | breakout | 79.15 | -20.85 | 245 | 18.8 | -90.58 | -28.98 | -90.59 | 2663 |
| 78 | MACD zero-line | trend | 78.88 | -21.11 | 243 | 16.0 | -91.64 | -35.05 | -91.65 | 2354 |
| 79 | Trend pullback | trend | 78.29 | -21.71 | 208 | 16.8 | -90.76 | -33.04 | -90.78 | 2271 |
| 80 | Triple EMA stack | trend | 77.55 | -22.45 | 251 | 16.3 | -92.81 | -34.56 | -92.83 | 2588 |
| 81 | RSI momentum | momentum | 77.44 | -22.57 | 236 | 14.8 | -90.26 | -28.55 | -90.28 | 2381 |
| 82 | Bollinger breakout | breakout | 77.26 | -22.74 | 249 | 15.7 | -93.83 | -42.08 | -93.84 | 2846 |
| 83 | ADX DI cross | trend | 76.05 | -23.95 | 236 | 8.1 | -89.48 | -44.73 | -89.49 | 2113 |
| 84 | Stochastic reversion | reversion | 74.02 | -25.98 | 380 | 24.5 | -95.89 | -45.64 | -95.89 | 4051 |
| 85 | Consensus | meta | 73.55 | -26.45 | 225 | 7.1 | -94.67 | -30.49 | -94.69 | 2667 |
| 86 | EMA 9/21 cross | trend | 73.48 | -26.52 | 330 | 16.7 | -97.38 | -40.99 | -97.39 | 3538 |
| 87 | Connors RSI(2) | reversion | 72.93 | -27.07 | 315 | 20.0 | -96.46 | -40.69 | -96.46 | 3642 |
| 88 | Bollinger reversion | reversion | 72.13 | -27.87 | 360 | 17.5 | -95.86 | -44.17 | -95.86 | 3689 |
| 89 | Candlestick reversal | reversion | 71.91 | -28.09 | 368 | 14.7 | -99.36 | -49.22 | -99.36 | 5632 |
| 90 | OBV trend | momentum | 70.54 | -29.46 | 353 | 15.6 | -95.89 | -45.58 | -95.89 | 3537 |
| 91 | CCI reversion | reversion | 70.37 | -29.63 | 304 | 13.8 | -98.49 | -49.52 | -98.49 | 4698 |
| 92 | Parabolic SAR | trend | 69.76 | -30.24 | 324 | 13.3 | -96.91 | -52.23 | -96.92 | 3612 |
| 93 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.54 | -35.87 | -98.55 | 5228 |
| 94 | MACD cross ⏸ | trend | 67.57 | -32.43 | 368 | 14.1 | -99.71 | -62.19 | -99.72 | 6072 |
| 95 | Williams %R ⏸ | reversion | 67.21 | -32.79 | 441 | 22.0 | -99.53 | -57.42 | -99.53 | 6123 |
| 96 | Heikin-Ashi ⏸ | trend | 66.45 | -33.55 | 325 | 6.5 | -99.89 | -75.57 | -99.89 | 8281 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T19:41 | MFI reversion | buy | SOL-USD | 3.96 | — | rebalance up |
| 2026-09-30T19:41 | MFI reversion | sell | XRP-USD | 3.96 | -0.02 | rebalance down |
| 2026-09-30T19:40 | Agent (ML meta-label) | buy | XRP-USD | 4.60 | — | entry |
| 2026-09-30T19:40 | Agent (ML meta-label) | buy | PLTR | 4.60 | — | entry |
| 2026-09-30T19:40 | Agent (ML meta-label) | sell | TQQQ | 4.39 | -0.01 | selected signal exited |
| 2026-09-30T19:40 | Agent (ML meta-label) | sell | TNA | 6.91 | 0.02 | selected signal exited |
| 2026-09-30T19:40 | MFI reversion · 1h | buy | SPY | 4.74 | — | rebalance up |
| 2026-09-30T19:40 | MFI reversion · 1h | sell | ETH-USD | 4.74 | -0.06 | rebalance down |
| 2026-09-30T19:40 | MFI reversion | buy | SOL-USD | 11.81 | — | entry signal |
| 2026-09-30T19:40 | CCI reversion | buy | SOL-USD | 5.03 | — | entry signal |
| 2026-09-30T19:40 | CCI reversion | sell | DOGE-USD | 3.90 | -0.02 | exit signal |
| 2026-09-30T19:40 | Stochastic reversion | buy | XRP-USD | 4.34 | — | rebalance up |
| 2026-09-30T19:40 | Stochastic reversion | buy | TNA | 3.94 | — | rebalance up |
| 2026-09-30T19:40 | Stochastic reversion | buy | SPY | 4.32 | — | rebalance up |
| 2026-09-30T19:40 | Stochastic reversion | buy | PLTR | 3.98 | — | rebalance up |
| 2026-09-30T19:40 | Stochastic reversion | buy | LABU | 4.27 | — | rebalance up |
| 2026-09-30T19:40 | Stochastic reversion | buy | IWM | 3.96 | — | rebalance up |
| 2026-09-30T19:40 | Stochastic reversion | buy | GOOGL | 4.33 | — | rebalance up |
| 2026-09-30T19:40 | Stochastic reversion | sell | ETHU | 4.63 | -0.01 | exit signal |
| 2026-09-30T19:40 | Stochastic reversion | sell | ETH-USD | 6.71 | -0.04 | exit signal |
| 2026-09-30T19:40 | Stochastic reversion | sell | BITX | 3.90 | -0.01 | exit signal |
| 2026-09-30T19:40 | Bollinger reversion | buy | UPRO | 7.71 | — | rebalance up |
| 2026-09-30T19:40 | Bollinger reversion | buy | SPY | 7.75 | — | rebalance up |
| 2026-09-30T19:40 | Bollinger reversion | buy | SOL-USD | 7.79 | — | rebalance up |
| 2026-09-30T19:40 | Bollinger reversion | buy | AAPL | 7.75 | — | rebalance up |
| 2026-09-30T19:40 | Bollinger reversion | sell | ETHU | 10.36 | 0.05 | exit signal |
| 2026-09-30T19:40 | Bollinger reversion | sell | BTC-USD | 10.30 | -0.04 | exit signal |
| 2026-09-30T19:40 | Bollinger reversion | sell | BITX | 10.35 | 0.04 | exit signal |
| 2026-09-30T19:40 | Parabolic SAR | buy | TECL | 5.18 | — | rebalance up |
| 2026-09-30T19:40 | Parabolic SAR | buy | NVDA | 5.22 | — | rebalance up |
| 2026-09-30T19:40 | Parabolic SAR | sell | TSLA | 11.59 | -0.04 | exit signal |
| 2026-09-30T19:40 | Triple EMA stack | buy | TQQQ | 4.32 | — | rebalance up |
| 2026-09-30T19:40 | Triple EMA stack | buy | TECL | 4.31 | — | rebalance up |
| 2026-09-30T19:40 | Triple EMA stack | buy | SOXL | 4.26 | — | rebalance up |
| 2026-09-30T19:40 | Triple EMA stack | buy | QQQ | 4.31 | — | rebalance up |
| 2026-09-30T19:40 | Triple EMA stack | buy | NVDA | 4.30 | — | rebalance up |
| 2026-09-30T19:40 | Triple EMA stack | buy | AMD | 4.30 | — | rebalance up |
| 2026-09-30T19:40 | Triple EMA stack | sell | TSLA | 8.60 | -0.01 | exit signal |
| 2026-09-30T19:40 | EMA 20/50 cross | buy | TSLA | 4.22 | — | rebalance up |
| 2026-09-30T19:40 | EMA 20/50 cross | buy | NVDA | 4.17 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
