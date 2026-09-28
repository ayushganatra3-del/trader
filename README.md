# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T14:40:05.000143+00:00 · 4629 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.67 (-0.33%)

Closed trades 10, win rate 70.0%, fees £0.37, max drawdown -0.79%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 19.94 | -0.16 |
| COIN | 19.93 | -0.01 |
| ETHU | 20.03 | +0.08 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-28 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-25)

**Uptrend** since 2026-09-21 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 20.87 · VIX 14.87 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, COIN 8.0, MSFT 7.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 4350 decisions in 303 calls, $0.0528 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T14:40 | 0 / 18 / 12 | SQQQ 15% |  |
| Breezy | 2026-09-28T14:40 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-09-28T14:40 | 8 / 19 / 3 | BITX 39%, MSTR 38% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.63 | +2.51% | 11 |
| Stochastic reversion | COIN | 2.50 | +5.60% | 9 |
| Williams %R | ETHU | 2.33 | +8.38% | 17 |
| CCI reversion | AMD | 2.17 | +3.10% | 10 |
| Bollinger reversion | PLTR | 2.11 | +1.89% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.67 | 1.67 | 0 | — | 13.08 | 2.86 | -7.55 | 43 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.55 | 0.55 | 0 | — | -5.47 | -1.54 | -12.40 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.43 | 0.43 | 0 | — | 1.36 | 0.64 | -4.88 | 16 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.40 | 0.40 | 4 | 50.0 | 2.41 | 1.25 | -2.56 | 92 |
| 5 | Copy: Hedge-fund gurus (GURU) | copy | 100.25 | 0.25 | 0 | — | -0.21 | -0.05 | -5.14 | 1 |
| 6 | Copy: Warren Buffett (BRK-B) | copy | 100.05 | 0.05 | 0 | — | -0.63 | -0.52 | -7.65 | 1 |
| 7 | Agent (aggressive) | meta | 100.00 | 0.00 | 4 | 50.0 | 4.27 | 2.15 | -3.92 | 87 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 9.35 | 1.34 | -7.93 | 7 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | -0.41 | -0.62 | -1.49 | 18 |
| 12 | Agent | meta | 99.67 | -0.33 | 10 | 70.0 | -8.67 | -5.49 | -9.99 | 204 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 99.59 | -0.41 | 0 | — | -6.52 | -1.78 | -12.73 | 1 |
| 14 | Copy: Congress Democrats (NANC) | copy | 99.59 | -0.41 | 0 | — | 6.60 | 2.63 | -3.62 | 1 |
| 15 | RSI(14) reversion · 1h | reversion | 99.52 | -0.48 | 1 | 100.0 | 0.63 | 0.27 | -8.69 | 122 |
| 16 | Hold BTC | benchmark | 99.50 | -0.51 | 0 | — | 30.30 | 3.87 | -8.68 | 1 |
| 17 | Hold SPY | benchmark | 99.50 | -0.51 | 0 | — | 3.23 | 1.76 | -3.66 | 1 |
| 18 | Three white soldiers · 1h | momentum | 99.37 | -0.63 | 1 | 0.0 | -3.07 | -2.54 | -5.16 | 28 |
| 19 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 20 | Gap and go | momentum | 99.30 | -0.70 | 5 | 0.0 | 16.34 | 4.09 | -4.73 | 190 |
| 21 | Daily: Bullish score | daily | 99.28 | -0.72 | 2 | 0.0 | -0.57 | 0.09 | -12.76 | 13 |
| 22 | Copy: Insider buying | copy | 99.21 | -0.79 | 2 | 100.0 | -11.95 | -2.29 | -17.74 | 73 |
| 23 | Agent (rotation) | meta | 99.10 | -0.90 | 26 | 11.5 | -7.67 | -2.65 | -11.53 | 216 |
| 24 | Opening range 30m | breakout | 98.92 | -1.08 | 13 | 15.4 | -7.86 | -2.29 | -13.54 | 547 |
| 25 | Timing: Nasdaq FTD · QQQ | daily | 98.74 | -1.26 | 0 | — | -3.82 | -2.34 | -4.71 | 2 |
| 26 | Z-score reversion · 1h | reversion | 98.57 | -1.43 | 4 | 25.0 | 3.55 | 0.90 | -8.60 | 154 |
| 27 | Williams %R · 1h | reversion | 98.44 | -1.56 | 23 | 56.5 | -20.00 | -3.66 | -22.05 | 481 |
| 28 | Connors RSI(2) · 1h | reversion | 98.43 | -1.57 | 27 | 48.1 | -13.10 | -4.18 | -13.34 | 244 |
| 29 | Stochastic reversion · 1h | reversion | 98.40 | -1.60 | 20 | 50.0 | -9.82 | -2.16 | -11.36 | 322 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.45 | -0.05 | -15.21 | 47 |
| 31 | Parabolic SAR · 1h | trend | 98.28 | -1.72 | 13 | 23.1 | -4.37 | -0.47 | -18.82 | 300 |
| 32 | Squeeze breakout · 1h | breakout | 98.21 | -1.79 | 7 | 14.3 | 16.54 | 2.72 | -10.21 | 103 |
| 33 | Bollinger reversion · 1h | reversion | 98.19 | -1.81 | 17 | 35.3 | -15.06 | -4.18 | -15.93 | 306 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 98.15 | -1.85 | 0 | — | 23.40 | 3.40 | -6.29 | 1 |
| 35 | CCI reversion · 1h | reversion | 98.09 | -1.91 | 18 | 27.8 | -0.23 | 0.13 | -12.41 | 406 |
| 36 | Candlestick reversal · 1h | reversion | 98.03 | -1.97 | 7 | 14.3 | -25.28 | -6.16 | -25.66 | 483 |
| 37 | Supertrend · 1h | trend | 98.01 | -1.99 | 10 | 10.0 | 3.52 | 0.68 | -16.43 | 194 |
| 38 | Opening range 15m | breakout | 97.98 | -2.02 | 22 | 13.6 | -10.60 | -2.85 | -16.14 | 682 |
| 39 | EMA 20/50 cross · 1h | trend | 97.73 | -2.27 | 7 | 14.3 | 15.77 | 1.90 | -14.36 | 125 |
| 40 | MACD cross · 1h | trend | 97.53 | -2.47 | 24 | 12.5 | -17.14 | -2.94 | -22.22 | 460 |
| 41 | ADX DI cross · 1h | trend | 97.32 | -2.68 | 20 | 10.0 | -13.15 | -2.54 | -18.06 | 250 |
| 42 | Trend pullback · 1h | trend | 97.27 | -2.73 | 16 | 18.8 | -26.56 | -7.23 | -26.60 | 153 |
| 43 | MACD zero-line · 1h | trend | 97.20 | -2.80 | 13 | 7.7 | 0.22 | 0.23 | -14.64 | 223 |
| 44 | Bollinger breakout · 1h | breakout | 97.19 | -2.81 | 13 | 7.7 | 14.91 | 2.07 | -11.05 | 283 |
| 45 | Agent (ML meta-label) | meta | 97.15 | -2.85 | 39 | 2.6 | 5.19 | 1.10 | -12.91 | 378 |
| 46 | Donchian 55/20 · 1h | breakout | 97.06 | -2.94 | 5 | 0.0 | 4.77 | 0.84 | -16.96 | 113 |
| 47 | RSI momentum · 1h | momentum | 96.98 | -3.02 | 18 | 5.6 | 2.50 | 0.55 | -15.29 | 216 |
| 48 | Heikin-Ashi · 1h | trend | 96.87 | -3.13 | 23 | 17.4 | -21.80 | -3.30 | -27.53 | 689 |
| 49 | Three white soldiers | momentum | 96.73 | -3.27 | 28 | 14.3 | -51.92 | -28.27 | -51.92 | 622 |
| 50 | Ichimoku · 1h | trend | 96.44 | -3.56 | 10 | 10.0 | 9.10 | 1.25 | -15.13 | 119 |
| 51 | Timing: Nasdaq FTD · TQQQ | daily | 96.40 | -3.60 | 0 | — | -12.14 | -2.51 | -14.23 | 2 |
| 52 | EMA 9/21 cross · 1h | trend | 96.33 | -3.67 | 28 | 14.3 | 2.79 | 0.58 | -16.92 | 315 |
| 53 | Max aggression: 1-day momentum | meta | 96.29 | -3.71 | 1 | 0.0 | -31.43 | -1.76 | -49.41 | 42 |
| 54 | Triple EMA stack · 1h | trend | 96.23 | -3.77 | 20 | 10.0 | -4.76 | -0.36 | -22.96 | 212 |
| 55 | Donchian 20/10 · 1h | breakout | 96.15 | -3.85 | 12 | 16.7 | 13.00 | 1.83 | -12.78 | 213 |
| 56 | VWAP momentum · 1h | momentum | 96.06 | -3.94 | 70 | 7.1 | -34.23 | -5.11 | -34.58 | 1265 |
| 57 | Max aggression: 5-day momentum | meta | 95.91 | -4.09 | 1 | 0.0 | -0.39 | 0.32 | -29.56 | 29 |
| 58 | OBV trend · 1h | momentum | 95.77 | -4.22 | 44 | 6.8 | -8.53 | -0.86 | -25.24 | 331 |
| 59 | AI bee: Bizzy | ai | 95.68 | -4.32 | 62 | 4.8 | — | — | — | — |
| 60 | Volume breakout · 1h | breakout | 95.34 | -4.66 | 25 | 4.0 | 9.63 | 1.49 | -12.60 | 127 |
| 61 | Keltner breakout · 1h | breakout | 95.29 | -4.71 | 7 | 0.0 | -1.67 | -0.02 | -18.68 | 217 |
| 62 | MFI reversion · 1h | reversion | 95.23 | -4.77 | 36 | 11.1 | -10.30 | -1.92 | -17.27 | 126 |
| 63 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 64 | ROC + volume · 1h | momentum | 92.37 | -7.63 | 41 | 4.9 | 0.91 | 0.33 | -17.18 | 403 |
| 65 | RSI(14) reversion | reversion | 92.32 | -7.68 | 60 | 23.3 | -71.71 | -22.34 | -71.79 | 1467 |
| 66 | Squeeze breakout | breakout | 91.14 | -8.86 | 57 | 5.3 | -60.06 | -18.62 | -60.24 | 1184 |
| 67 | EMA 20/50 cross | trend | 91.04 | -8.96 | 68 | 16.2 | -78.37 | -17.57 | -78.49 | 1479 |
| 68 | Volume breakout | breakout | 90.61 | -9.39 | 62 | 8.1 | -62.19 | -20.87 | -62.19 | 902 |
| 69 | Donchian 55/20 | breakout | 90.35 | -9.65 | 65 | 10.8 | -68.46 | -15.84 | -68.48 | 1329 |
| 70 | ROC + volume | momentum | 90.00 | -10.00 | 84 | 11.9 | -72.49 | -18.11 | -72.65 | 1642 |
| 71 | Ichimoku | trend | 88.89 | -11.11 | 78 | 7.7 | -80.39 | -26.44 | -80.53 | 1777 |
| 72 | Keltner breakout | breakout | 88.79 | -11.21 | 87 | 9.2 | -85.10 | -35.82 | -85.12 | 1914 |
| 73 | VWAP reversion | reversion | 86.58 | -13.42 | 92 | 15.2 | -71.05 | -17.42 | -71.74 | 1399 |
| 74 | Z-score reversion | reversion | 86.30 | -13.70 | 108 | 19.4 | -85.07 | -28.85 | -85.07 | 2097 |
| 75 | Supertrend | trend | 86.01 | -13.99 | 108 | 15.7 | -87.41 | -25.34 | -87.45 | 1965 |
| 76 | RSI momentum | momentum | 85.98 | -14.02 | 113 | 13.3 | -90.44 | -30.14 | -90.46 | 2396 |
| 77 | MACD zero-line | trend | 85.94 | -14.06 | 122 | 13.9 | -91.64 | -37.14 | -91.64 | 2361 |
| 78 | Bollinger breakout | breakout | 85.50 | -14.50 | 118 | 11.0 | -94.04 | -43.14 | -94.04 | 2872 |
| 79 | Trend pullback | trend | 85.45 | -14.55 | 121 | 16.5 | -90.76 | -35.71 | -90.76 | 2311 |
| 80 | Triple EMA stack | trend | 85.43 | -14.57 | 139 | 12.9 | -92.98 | -37.13 | -93.01 | 2632 |
| 81 | Donchian 20/10 | breakout | 85.11 | -14.89 | 127 | 14.2 | -91.07 | -30.31 | -91.11 | 2691 |
| 82 | Connors RSI(2) | reversion | 84.23 | -15.77 | 160 | 17.5 | -96.37 | -43.02 | -96.37 | 3657 |
| 83 | ADX DI cross | trend | 84.06 | -15.94 | 121 | 7.4 | -89.44 | -49.92 | -89.45 | 2122 |
| 84 | MFI reversion | reversion | 83.39 | -16.61 | 118 | 8.5 | -87.97 | -37.97 | -88.01 | 2165 |
| 85 | Stochastic reversion | reversion | 82.44 | -17.56 | 177 | 20.3 | -95.91 | -49.69 | -95.93 | 4057 |
| 86 | Consensus | meta | 81.34 | -18.66 | 129 | 6.2 | -94.96 | -32.15 | -94.96 | 2676 |
| 87 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.33 | -56.21 | -99.33 | 5532 |
| 88 | OBV trend | momentum | 81.06 | -18.94 | 179 | 12.3 | -95.87 | -50.80 | -95.88 | 3568 |
| 89 | EMA 9/21 cross | trend | 80.85 | -19.15 | 183 | 12.6 | -97.45 | -43.97 | -97.47 | 3543 |
| 90 | Bollinger reversion | reversion | 79.89 | -20.11 | 198 | 12.1 | -95.86 | -46.89 | -95.86 | 3700 |
| 91 | VWAP momentum | momentum | 79.78 | -20.22 | 221 | 9.5 | -98.48 | -37.18 | -98.48 | 5228 |
| 92 | Parabolic SAR | trend | 78.58 | -21.42 | 196 | 12.2 | -96.90 | -60.74 | -96.91 | 3655 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.45 | -56.59 | -98.46 | 4702 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -75.09 | -99.70 | 6095 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.52 | -68.12 | -99.53 | 6088 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.89 | -104.72 | -99.89 | 8314 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T14:40 | AI bee: Bizzy | sell | LABU | 15.42 | 0.06 | Jev: sell (buy p=0.20) |
| 2026-09-28T14:40 | Agent (ML meta-label) | sell | UPRO | 2.85 | -0.01 | selected signal exited |
| 2026-09-28T14:40 | Agent (aggressive) | buy | COIN | 50.03 | — | following Stochastic reversion |
| 2026-09-28T14:40 | Agent (aggressive) | sell | AMD | 49.77 | -0.48 | selected signal exited |
| 2026-09-28T14:40 | Agent | buy | COIN | 19.94 | — | following Stochastic reversion |
| 2026-09-28T14:40 | Agent | sell | AMD | 19.81 | -0.17 | rebalance down |
| 2026-09-28T14:40 | RSI momentum · 1h | sell | SPY | 24.22 | -0.07 | stop-loss |
| 2026-09-28T14:40 | MACD zero-line · 1h | sell | UPRO | 24.23 | -0.50 | stop-loss |
| 2026-09-28T14:40 | MACD zero-line · 1h | sell | SPY | 19.64 | -0.18 | stop-loss |
| 2026-09-28T14:40 | MACD cross · 1h | buy | NVDA | 7.46 | — | entry |
| 2026-09-28T14:40 | MACD cross · 1h | buy | DOGE-USD | 12.20 | — | entry |
| 2026-09-28T14:40 | MACD cross · 1h | buy | BTC-USD | 8.17 | — | rebalance up |
| 2026-09-28T14:40 | MACD cross · 1h | sell | UPRO | 13.90 | -0.19 | stop-loss |
| 2026-09-28T14:40 | MACD cross · 1h | sell | SPY | 13.94 | -0.09 | stop-loss |
| 2026-09-28T14:40 | Triple EMA stack · 1h | buy | TQQQ | 5.26 | — | rebalance up |
| 2026-09-28T14:40 | Triple EMA stack · 1h | buy | TECL | 5.49 | — | rebalance up |
| 2026-09-28T14:40 | Triple EMA stack · 1h | buy | SOXL | 5.71 | — | rebalance up |
| 2026-09-28T14:40 | Triple EMA stack · 1h | buy | PLTR | 5.14 | — | rebalance up |
| 2026-09-28T14:40 | Triple EMA stack · 1h | buy | AAPL | 8.34 | — | rebalance up |
| 2026-09-28T14:40 | Triple EMA stack · 1h | sell | UPRO | 10.79 | -0.06 | stop-loss |
| 2026-09-28T14:40 | Triple EMA stack · 1h | sell | SPY | 10.82 | -0.04 | stop-loss |
| 2026-09-28T14:40 | EMA 9/21 cross · 1h | buy | SOXL | 5.34 | — | rebalance up |
| 2026-09-28T14:40 | EMA 9/21 cross · 1h | buy | PLTR | 4.87 | — | rebalance up |
| 2026-09-28T14:40 | EMA 9/21 cross · 1h | buy | AAPL | 6.62 | — | rebalance up |
| 2026-09-28T14:40 | EMA 9/21 cross · 1h | sell | UPRO | 9.70 | -0.06 | stop-loss |
| 2026-09-28T14:40 | EMA 9/21 cross · 1h | sell | SPY | 9.73 | -0.03 | stop-loss |
| 2026-09-28T14:40 | MFI reversion | buy | BITX | 20.64 | — | entry signal |
| 2026-09-28T14:40 | Stochastic reversion | buy | SOXL | 3.28 | — | entry |
| 2026-09-28T14:40 | Stochastic reversion | buy | MSTR | 5.89 | — | entry signal |
| 2026-09-28T14:40 | Stochastic reversion | buy | COIN | 5.89 | — | entry signal |
| 2026-09-28T14:40 | Stochastic reversion | sell | AMZN | 7.58 | 0.01 | exit signal |
| 2026-09-28T14:40 | Stochastic reversion | sell | AMD | 7.48 | -0.07 | stop-loss |
| 2026-09-28T14:40 | Bollinger reversion | buy | MSTR | 4.74 | — | entry signal |
| 2026-09-28T14:40 | Bollinger reversion | buy | DOGE-USD | 5.33 | — | entry signal |
| 2026-09-28T14:40 | Bollinger reversion | buy | COIN | 5.33 | — | entry signal |
| 2026-09-28T14:40 | Bollinger reversion | sell | UPRO | 5.34 | -0.04 | stop-loss |
| 2026-09-28T14:40 | Bollinger reversion | sell | TECL | 2.86 | -0.03 | stop-loss |
| 2026-09-28T14:40 | Bollinger reversion | sell | SPY | 5.37 | -0.02 | stop-loss |
| 2026-09-28T14:40 | Connors RSI(2) | buy | MSFT | 21.06 | — | entry signal |
| 2026-09-28T14:40 | RSI(14) reversion | buy | TQQQ | 11.54 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
