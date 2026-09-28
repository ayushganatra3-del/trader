# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T19:40:05.000180+00:00 · 4877 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.02 (+0.02%)

Closed trades 16, win rate 75.0%, fees £0.51, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.88 | -0.10 |

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

Today: 25998 decisions in 1033 calls, $0.3063 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T19:40 | 2 / 3 / 25 | LABU 14%, SQQQ 13% |  |
| Breezy | 2026-09-28T19:40 | 0 / 21 / 9 | cash |  |
| Boozy | 2026-09-28T19:40 | 10 / 17 / 3 | BITX 26%, COIN 26% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.33 | 1.32 | 0 | — | 12.66 | 2.79 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.44 | 0.44 | 0 | — | 0.02 | 0.05 | -1.49 | 19 |
| 3 | Agent (aggressive) | meta | 100.35 | 0.35 | 7 | 71.4 | 1.17 | 0.69 | -4.81 | 91 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.31 | 0.31 | 4 | 50.0 | 2.41 | 1.25 | -2.47 | 92 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.20 | 0.20 | 0 | — | -4.78 | -1.41 | -12.40 | 25 |
| 6 | Agent | meta | 100.02 | 0.02 | 16 | 75.0 | -7.97 | -5.01 | -9.47 | 204 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 6.67 | 1.34 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Copy: Congress Democrats (NANC) | copy | 99.63 | -0.37 | 0 | — | 7.91 | 3.04 | -3.62 | 1 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 99.58 | -0.42 | 0 | — | -1.32 | -0.50 | -7.65 | 1 |
| 12 | RSI(14) reversion · 1h | reversion | 99.48 | -0.52 | 2 | 100.0 | 15.31 | 3.20 | -6.57 | 138 |
| 13 | Hold SPY | benchmark | 99.36 | -0.64 | 0 | — | 4.00 | 2.08 | -3.66 | 1 |
| 14 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 15 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 16 | Hold BTC | benchmark | 99.30 | -0.70 | 0 | — | 29.91 | 3.84 | -8.68 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.16 | -0.84 | 0 | — | -1.67 | -0.78 | -5.14 | 1 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.79 | -5.16 | 28 |
| 19 | Connors RSI(2) · 1h | reversion | 99.04 | -0.96 | 39 | 48.7 | -11.93 | -3.81 | -13.45 | 238 |
| 20 | Copy: Insider buying | copy | 98.96 | -1.04 | 2 | 100.0 | -12.22 | -2.35 | -17.74 | 73 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.90 | -1.10 | 0 | — | -7.81 | -1.96 | -12.73 | 1 |
| 22 | Timing: Nasdaq FTD · QQQ | daily | 98.90 | -1.10 | 0 | — | -3.69 | -2.28 | -5.09 | 2 |
| 23 | Daily: Bullish score | daily | 98.86 | -1.14 | 2 | 0.0 | -1.16 | 0.03 | -12.76 | 13 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 25 | Stochastic reversion · 1h | reversion | 98.63 | -1.37 | 23 | 56.5 | -12.58 | -2.81 | -14.07 | 324 |
| 26 | Opening range 30m | breakout | 98.57 | -1.43 | 28 | 7.1 | -8.68 | -2.53 | -13.54 | 562 |
| 27 | Z-score reversion · 1h | reversion | 98.55 | -1.46 | 4 | 25.0 | 3.39 | 0.86 | -8.60 | 155 |
| 28 | Williams %R · 1h | reversion | 98.44 | -1.56 | 29 | 51.7 | -18.49 | -3.43 | -20.33 | 488 |
| 29 | Agent (rotation) | meta | 98.44 | -1.56 | 26 | 11.5 | -8.16 | -2.90 | -11.85 | 232 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -0.87 | -0.05 | -15.21 | 47 |
| 31 | CCI reversion · 1h | reversion | 98.32 | -1.68 | 23 | 34.8 | -0.15 | 0.15 | -12.41 | 412 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.17 | -1.83 | 0 | — | 24.09 | 3.50 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 97.94 | -2.06 | 7 | 14.3 | 14.39 | 2.53 | -7.65 | 97 |
| 34 | Candlestick reversal · 1h | reversion | 97.79 | -2.21 | 10 | 20.0 | -26.24 | -6.16 | -26.89 | 492 |
| 35 | Opening range 15m | breakout | 97.60 | -2.40 | 35 | 8.6 | -9.77 | -2.67 | -16.14 | 692 |
| 36 | EMA 20/50 cross · 1h | trend | 97.58 | -2.42 | 8 | 12.5 | 15.29 | 1.85 | -14.36 | 125 |
| 37 | Supertrend · 1h | trend | 97.57 | -2.43 | 11 | 9.1 | 3.22 | 0.64 | -16.43 | 197 |
| 38 | MACD cross · 1h | trend | 97.45 | -2.55 | 27 | 11.1 | -15.60 | -2.65 | -20.93 | 456 |
| 39 | Bollinger reversion · 1h | reversion | 97.23 | -2.77 | 19 | 31.6 | -17.57 | -4.92 | -17.84 | 309 |
| 40 | Bollinger breakout · 1h | breakout | 97.06 | -2.94 | 13 | 7.7 | 13.59 | 1.94 | -9.86 | 284 |
| 41 | Donchian 55/20 · 1h | breakout | 96.96 | -3.04 | 8 | 0.0 | 4.26 | 0.77 | -16.96 | 113 |
| 42 | Agent (ML meta-label) | meta | 96.93 | -3.07 | 78 | 10.3 | 4.53 | 0.96 | -11.40 | 386 |
| 43 | Parabolic SAR · 1h | trend | 96.91 | -3.10 | 19 | 15.8 | -6.04 | -0.71 | -18.82 | 303 |
| 44 | Timing: Nasdaq FTD · TQQQ | daily | 96.84 | -3.16 | 0 | — | -11.76 | -2.46 | -15.27 | 2 |
| 45 | Trend pullback · 1h | trend | 96.78 | -3.22 | 22 | 13.6 | -26.63 | -7.12 | -27.11 | 151 |
| 46 | MACD zero-line · 1h | trend | 96.75 | -3.25 | 14 | 7.1 | -3.37 | -0.29 | -14.81 | 221 |
| 47 | Three white soldiers | momentum | 96.49 | -3.51 | 30 | 13.3 | -51.75 | -28.63 | -51.77 | 621 |
| 48 | RSI momentum · 1h | momentum | 96.30 | -3.70 | 20 | 5.0 | 1.47 | 0.41 | -15.29 | 212 |
| 49 | EMA 9/21 cross · 1h | trend | 96.02 | -3.98 | 33 | 12.1 | 3.61 | 0.69 | -16.92 | 310 |
| 50 | ADX DI cross · 1h | trend | 95.77 | -4.23 | 22 | 9.1 | -11.92 | -2.25 | -15.46 | 253 |
| 51 | MFI reversion · 1h | reversion | 95.76 | -4.24 | 38 | 13.2 | -9.60 | -1.78 | -17.20 | 126 |
| 52 | Triple EMA stack · 1h | trend | 95.74 | -4.26 | 24 | 8.3 | -4.01 | -0.27 | -22.95 | 228 |
| 53 | Ichimoku · 1h | trend | 95.74 | -4.26 | 11 | 9.1 | 8.02 | 1.13 | -15.13 | 119 |
| 54 | Donchian 20/10 · 1h | breakout | 95.73 | -4.27 | 12 | 16.7 | 12.01 | 1.70 | -12.78 | 213 |
| 55 | OBV trend · 1h | momentum | 95.34 | -4.67 | 47 | 6.4 | -10.80 | -1.17 | -25.24 | 322 |
| 56 | Max aggression: 5-day momentum | meta | 95.27 | -4.73 | 1 | 0.0 | -1.07 | 0.26 | -29.56 | 29 |
| 57 | Max aggression: 1-day momentum | meta | 95.23 | -4.77 | 1 | 0.0 | -32.21 | -1.82 | -49.41 | 42 |
| 58 | VWAP momentum · 1h | momentum | 95.10 | -4.90 | 76 | 6.6 | -33.21 | -4.98 | -33.64 | 1249 |
| 59 | Volume breakout · 1h | breakout | 95.08 | -4.92 | 25 | 4.0 | 5.92 | 1.01 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.03 | -4.97 | 7 | 0.0 | -0.65 | 0.12 | -18.68 | 221 |
| 61 | Heikin-Ashi · 1h | trend | 94.60 | -5.40 | 33 | 12.1 | -22.23 | -3.34 | -28.97 | 678 |
| 62 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 63 | AI bee: Bizzy ⏸ | ai | 93.85 | -6.15 | 171 | 15.8 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 93.02 | -6.98 | 79 | 35.4 | -70.78 | -21.63 | -71.15 | 1476 |
| 65 | ROC + volume · 1h | momentum | 92.02 | -7.98 | 43 | 7.0 | -3.83 | -0.33 | -17.18 | 402 |
| 66 | Squeeze breakout | breakout | 90.43 | -9.57 | 65 | 6.2 | -60.02 | -18.81 | -60.02 | 1180 |
| 67 | ROC + volume | momentum | 89.59 | -10.41 | 111 | 16.2 | -72.16 | -18.14 | -72.30 | 1659 |
| 68 | EMA 20/50 cross | trend | 89.20 | -10.80 | 85 | 12.9 | -79.01 | -17.84 | -79.01 | 1487 |
| 69 | Donchian 55/20 | breakout | 89.09 | -10.91 | 75 | 10.7 | -68.69 | -16.06 | -68.72 | 1332 |
| 70 | Volume breakout | breakout | 88.86 | -11.14 | 75 | 9.3 | -62.60 | -20.79 | -62.60 | 909 |
| 71 | Ichimoku | trend | 88.20 | -11.80 | 83 | 8.4 | -80.61 | -26.84 | -80.62 | 1762 |
| 72 | Keltner breakout | breakout | 88.05 | -11.95 | 116 | 9.5 | -85.15 | -36.17 | -85.15 | 1936 |
| 73 | Z-score reversion | reversion | 87.04 | -12.96 | 135 | 29.6 | -84.57 | -28.97 | -84.76 | 2083 |
| 74 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -70.96 | -17.40 | -71.87 | 1416 |
| 75 | MACD zero-line | trend | 85.65 | -14.35 | 146 | 15.8 | -91.53 | -37.09 | -91.58 | 2368 |
| 76 | Supertrend | trend | 85.64 | -14.36 | 128 | 14.8 | -87.38 | -25.41 | -87.42 | 1976 |
| 77 | Bollinger breakout | breakout | 85.22 | -14.78 | 149 | 14.1 | -93.96 | -43.46 | -93.97 | 2877 |
| 78 | RSI momentum | momentum | 85.11 | -14.89 | 138 | 11.6 | -90.40 | -30.42 | -90.40 | 2401 |
| 79 | Donchian 20/10 | breakout | 84.76 | -15.24 | 149 | 14.8 | -90.88 | -30.46 | -90.90 | 2686 |
| 80 | Triple EMA stack | trend | 84.34 | -15.66 | 161 | 13.0 | -93.02 | -37.58 | -93.03 | 2629 |
| 81 | Trend pullback | trend | 83.54 | -16.46 | 137 | 15.3 | -90.49 | -34.55 | -90.50 | 2282 |
| 82 | ADX DI cross | trend | 83.25 | -16.75 | 151 | 7.3 | -89.43 | -50.26 | -89.44 | 2127 |
| 83 | MFI reversion | reversion | 82.91 | -17.09 | 141 | 16.3 | -87.91 | -37.06 | -87.95 | 2177 |
| 84 | Connors RSI(2) | reversion | 82.61 | -17.39 | 191 | 17.8 | -96.37 | -43.41 | -96.37 | 3648 |
| 85 | Stochastic reversion | reversion | 81.56 | -18.44 | 224 | 25.9 | -95.88 | -49.97 | -95.88 | 4057 |
| 86 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.34 | -55.43 | -99.34 | 5563 |
| 87 | EMA 9/21 cross | trend | 80.69 | -19.31 | 208 | 13.5 | -97.41 | -44.16 | -97.41 | 3550 |
| 88 | OBV trend | momentum | 80.08 | -19.92 | 210 | 12.4 | -95.80 | -52.17 | -95.81 | 3560 |
| 89 | Consensus | meta | 79.66 | -20.34 | 154 | 7.1 | -94.91 | -32.17 | -94.92 | 2681 |
| 90 | Bollinger reversion ⏸ | reversion | 79.09 | -20.91 | 233 | 13.3 | -95.73 | -47.87 | -95.73 | 3672 |
| 91 | VWAP momentum | momentum | 78.40 | -21.60 | 273 | 9.2 | -98.48 | -37.38 | -98.48 | 5209 |
| 92 | Parabolic SAR | trend | 77.70 | -22.30 | 222 | 12.2 | -96.94 | -61.57 | -96.94 | 3654 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.46 | -55.99 | -98.46 | 4703 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -75.05 | -99.70 | 6089 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.52 | -67.46 | -99.52 | 6086 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.88 | -105.38 | -99.88 | 8316 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T19:40 | Agent (ML meta-label) | buy | AMZN | 4.62 | — | entry |
| 2026-09-28T19:40 | Agent (ML meta-label) | sell | QQQ | 4.62 | -0.01 | selected signal exited |
| 2026-09-28T19:40 | ROC + volume · 1h | buy | SQQQ | 5.17 | — | rebalance up |
| 2026-09-28T19:40 | ROC + volume · 1h | buy | NVDA | 5.33 | — | rebalance up |
| 2026-09-28T19:40 | ROC + volume · 1h | buy | BTC-USD | 5.36 | — | rebalance up |
| 2026-09-28T19:40 | ROC + volume · 1h | buy | AAPL | 5.27 | — | rebalance up |
| 2026-09-28T19:40 | ROC + volume · 1h | sell | ETH-USD | 13.02 | -0.19 | stop-loss |
| 2026-09-28T19:40 | MFI reversion | buy | SOXL | 4.19 | — | rebalance up |
| 2026-09-28T19:40 | MFI reversion | buy | AMZN | 16.36 | — | rebalance up |
| 2026-09-28T19:40 | MFI reversion | sell | ETH-USD | 20.59 | -0.27 | stop-loss |
| 2026-09-28T19:40 | MFI reversion | sell | BTC-USD | 20.60 | -0.26 | stop-loss |
| 2026-09-28T19:40 | Stochastic reversion | buy | UPRO | 5.54 | — | entry |
| 2026-09-28T19:40 | Stochastic reversion | buy | TQQQ | 5.83 | — | entry |
| 2026-09-28T19:40 | Stochastic reversion | buy | TNA | 5.83 | — | entry |
| 2026-09-28T19:40 | Stochastic reversion | buy | SPY | 5.83 | — | entry |
| 2026-09-28T19:40 | Stochastic reversion | buy | QQQ | 5.83 | — | entry |
| 2026-09-28T19:40 | Stochastic reversion | buy | IWM | 5.83 | — | entry |
| 2026-09-28T19:40 | Stochastic reversion | buy | GOOGL | 5.83 | — | entry |
| 2026-09-28T19:40 | Stochastic reversion | sell | XRP-USD | 6.72 | -0.11 | stop-loss |
| 2026-09-28T19:40 | Stochastic reversion | sell | SOL-USD | 6.76 | -0.10 | stop-loss |
| 2026-09-28T19:40 | Stochastic reversion | sell | NVDA | 6.80 | -0.06 | stop-loss |
| 2026-09-28T19:40 | Stochastic reversion | sell | ETHU | 6.75 | -0.10 | stop-loss |
| 2026-09-28T19:40 | Stochastic reversion | sell | DOGE-USD | 6.74 | -0.11 | stop-loss |
| 2026-09-28T19:40 | Stochastic reversion | sell | BTC-USD | 6.77 | -0.08 | stop-loss |
| 2026-09-28T19:40 | Connors RSI(2) | sell | XRP-USD | 20.60 | -0.29 | stop-loss |
| 2026-09-28T19:40 | Connors RSI(2) | sell | NVDA | 16.59 | -0.09 | stop-loss |
| 2026-09-28T19:40 | Connors RSI(2) | sell | ETH-USD | 20.66 | -0.22 | stop-loss |
| 2026-09-28T19:40 | Connors RSI(2) | sell | BTC-USD | 16.54 | -0.18 | stop-loss |
| 2026-09-28T19:40 | VWAP momentum | buy | MSFT | 10.88 | — | rebalance up |
| 2026-09-28T19:40 | VWAP momentum | buy | LABU | 10.84 | — | rebalance up |
| 2026-09-28T19:40 | VWAP momentum | buy | GOOGL | 11.72 | — | rebalance up |
| 2026-09-28T19:40 | VWAP momentum | sell | TECL | 9.77 | -0.09 | exit signal |
| 2026-09-28T19:40 | VWAP momentum | sell | SOXL | 9.74 | -0.10 | exit signal |
| 2026-09-28T19:40 | VWAP momentum | sell | QQQ | 8.75 | -0.02 | exit signal |
| 2026-09-28T19:40 | VWAP momentum | sell | ETH-USD | 8.68 | -0.09 | exit signal |
| 2026-09-28T19:40 | VWAP momentum | sell | BTC-USD | 8.68 | -0.09 | exit signal |
| 2026-09-28T19:40 | Supertrend | sell | TQQQ | 8.53 | -0.04 | exit signal |
| 2026-09-28T19:40 | Supertrend | sell | TECL | 8.53 | -0.04 | exit signal |
| 2026-09-28T19:40 | Supertrend | sell | QQQ | 8.57 | -0.02 | exit signal |
| 2026-09-28T19:40 | EMA 20/50 cross | buy | TNA | 13.33 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
