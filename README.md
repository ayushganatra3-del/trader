# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-28T18:10:05.000124+00:00 · 4796 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.93 (-0.07%)

Closed trades 14, win rate 71.4%, fees £0.45, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 19.96 | -0.03 |

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

Today: 18812 decisions in 791 calls, $0.2221 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-28T18:10 | 5 / 12 / 13 | TNA 20%, LABU 18%, IWM 14%, TECL 13% |  |
| Breezy | 2026-09-28T18:10 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-09-28T18:10 | 9 / 20 / 1 | TNA 44%, BITX 42% |  |

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
| 1 | Agent (aggressive) | meta | 100.52 | 0.52 | 6 | 66.7 | 0.65 | 0.41 | -4.81 | 90 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.48 | 0.48 | 0 | — | 11.75 | 2.62 | -7.55 | 43 |
| 3 | RSI(14) reversion · 1h | reversion | 100.14 | 0.14 | 2 | 100.0 | 6.88 | 1.92 | -6.57 | 124 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.10 | 0.10 | 4 | 50.0 | 2.20 | 1.15 | -2.47 | 92 |
| 5 | Hold BTC | benchmark | 100.08 | 0.08 | 0 | — | 31.33 | 3.96 | -8.68 | 1 |
| 6 | Daily: Bullish score | daily | 100.05 | 0.05 | 2 | 0.0 | 0.07 | 0.21 | -12.76 | 13 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 6.74 | 1.34 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | -0.41 | -0.62 | -1.49 | 18 |
| 11 | Agent | meta | 99.93 | -0.07 | 14 | 71.4 | -9.38 | -6.04 | -10.53 | 201 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.81 | -0.19 | 0 | — | -1.64 | -0.61 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.69 | -0.31 | 0 | — | 7.28 | 2.76 | -3.62 | 1 |
| 14 | Stochastic reversion · 1h | reversion | 99.64 | -0.36 | 21 | 52.4 | -11.44 | -2.53 | -14.07 | 324 |
| 15 | Hold SPY | benchmark | 99.60 | -0.40 | 0 | — | 3.43 | 1.82 | -3.66 | 1 |
| 16 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.37 | -0.63 | 0 | — | -5.54 | -1.66 | -12.40 | 25 |
| 17 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.43 | -14.72 | 121 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 99.33 | -0.67 | 0 | — | -7.36 | -1.85 | -12.73 | 1 |
| 19 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.09 | -4.73 | 190 |
| 20 | Williams %R · 1h | reversion | 99.20 | -0.80 | 27 | 51.9 | -18.55 | -3.43 | -21.00 | 490 |
| 21 | CCI reversion · 1h | reversion | 99.16 | -0.84 | 23 | 34.8 | 0.18 | 0.20 | -12.41 | 415 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 99.16 | -0.84 | 0 | — | -1.64 | -0.77 | -5.14 | 1 |
| 23 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.40 | -2.79 | -5.16 | 28 |
| 24 | Timing: Nasdaq FTD · QQQ | daily | 99.15 | -0.85 | 0 | — | -3.42 | -2.15 | -5.09 | 2 |
| 25 | Connors RSI(2) · 1h | reversion | 99.15 | -0.85 | 34 | 55.9 | -11.88 | -3.80 | -13.49 | 243 |
| 26 | Opening range 30m | breakout | 99.13 | -0.87 | 23 | 8.7 | -8.10 | -2.36 | -13.54 | 562 |
| 27 | Z-score reversion · 1h | reversion | 99.11 | -0.89 | 4 | 25.0 | 4.01 | 1.00 | -8.60 | 155 |
| 28 | Copy: Insider buying | copy | 98.94 | -1.06 | 2 | 100.0 | -12.20 | -2.35 | -17.74 | 73 |
| 29 | Candlestick reversal · 1h | reversion | 98.76 | -1.24 | 9 | 22.2 | -27.11 | -6.71 | -28.14 | 488 |
| 30 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 98.65 | -1.35 | 0 | — | 24.67 | 3.49 | -6.29 | 1 |
| 32 | EMA 20/50 cross · 1h | trend | 98.55 | -1.46 | 8 | 12.5 | 16.28 | 1.95 | -14.36 | 126 |
| 33 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.42 | -0.05 | -15.21 | 47 |
| 34 | Agent (rotation) | meta | 98.16 | -1.84 | 26 | 11.5 | -7.94 | -2.81 | -11.63 | 213 |
| 35 | Opening range 15m | breakout | 98.15 | -1.85 | 30 | 10.0 | -10.68 | -2.88 | -16.14 | 696 |
| 36 | Squeeze breakout · 1h | breakout | 98.12 | -1.88 | 7 | 14.3 | 15.94 | 2.83 | -6.17 | 95 |
| 37 | Supertrend · 1h | trend | 98.11 | -1.89 | 11 | 9.1 | 4.00 | 0.74 | -16.43 | 197 |
| 38 | Parabolic SAR · 1h | trend | 97.95 | -2.05 | 18 | 16.7 | -5.09 | -0.57 | -18.82 | 305 |
| 39 | MACD cross · 1h | trend | 97.92 | -2.08 | 26 | 11.5 | -15.10 | -2.55 | -21.04 | 457 |
| 40 | Trend pullback · 1h | trend | 97.82 | -2.18 | 22 | 13.6 | -25.39 | -6.92 | -26.81 | 152 |
| 41 | Bollinger reversion · 1h | reversion | 97.75 | -2.25 | 19 | 31.6 | -16.23 | -4.53 | -16.88 | 311 |
| 42 | Timing: Nasdaq FTD · TQQQ | daily | 97.65 | -2.35 | 0 | — | -10.99 | -2.32 | -15.27 | 2 |
| 43 | Donchian 55/20 · 1h | breakout | 97.53 | -2.46 | 8 | 0.0 | 5.03 | 0.87 | -16.96 | 113 |
| 44 | Agent (ML meta-label) | meta | 97.53 | -2.47 | 69 | 10.1 | 9.63 | 1.72 | -13.45 | 379 |
| 45 | MACD zero-line · 1h | trend | 97.07 | -2.93 | 13 | 7.7 | 0.21 | 0.23 | -14.64 | 225 |
| 46 | Bollinger breakout · 1h | breakout | 96.85 | -3.15 | 13 | 7.7 | 13.41 | 1.91 | -9.83 | 284 |
| 47 | EMA 9/21 cross · 1h | trend | 96.73 | -3.27 | 31 | 12.9 | 3.67 | 0.70 | -16.92 | 310 |
| 48 | RSI momentum · 1h | momentum | 96.61 | -3.39 | 20 | 5.0 | 1.11 | 0.36 | -15.29 | 215 |
| 49 | Triple EMA stack · 1h | trend | 96.51 | -3.49 | 23 | 8.7 | -3.49 | -0.21 | -22.96 | 227 |
| 50 | Three white soldiers | momentum | 96.49 | -3.51 | 30 | 13.3 | -52.13 | -28.58 | -52.13 | 623 |
| 51 | Max aggression: 5-day momentum | meta | 96.47 | -3.53 | 1 | 0.0 | 0.21 | 0.37 | -29.56 | 29 |
| 52 | ADX DI cross · 1h | trend | 96.40 | -3.60 | 22 | 9.1 | -10.96 | -2.08 | -15.39 | 252 |
| 53 | Ichimoku · 1h | trend | 96.29 | -3.71 | 10 | 10.0 | 8.94 | 1.23 | -15.13 | 119 |
| 54 | VWAP momentum · 1h | momentum | 96.12 | -3.88 | 76 | 6.6 | -32.93 | -4.94 | -33.21 | 1245 |
| 55 | MFI reversion · 1h | reversion | 96.03 | -3.97 | 38 | 13.2 | -9.31 | -1.72 | -17.20 | 126 |
| 56 | Max aggression: 1-day momentum | meta | 95.93 | -4.07 | 1 | 0.0 | -31.69 | -1.78 | -49.41 | 42 |
| 57 | Donchian 20/10 · 1h | breakout | 95.71 | -4.29 | 12 | 16.7 | 13.23 | 1.84 | -12.78 | 213 |
| 58 | OBV trend · 1h | momentum | 95.57 | -4.43 | 47 | 6.4 | -8.67 | -0.88 | -25.24 | 328 |
| 59 | Heikin-Ashi · 1h | trend | 95.50 | -4.50 | 29 | 13.8 | -23.09 | -3.51 | -28.22 | 679 |
| 60 | Volume breakout · 1h | breakout | 95.25 | -4.75 | 25 | 4.0 | 6.40 | 1.07 | -12.60 | 126 |
| 61 | Keltner breakout · 1h | breakout | 95.20 | -4.79 | 7 | 0.0 | 1.49 | 0.41 | -18.68 | 221 |
| 62 | AI bee: Boozy ⏸ | ai | 93.97 | -6.03 | 35 | 2.9 | — | — | — | — |
| 63 | AI bee: Bizzy ⏸ | ai | 93.85 | -6.15 | 171 | 15.8 | — | — | — | — |
| 64 | RSI(14) reversion | reversion | 93.02 | -6.98 | 79 | 35.4 | -71.53 | -22.26 | -71.89 | 1489 |
| 65 | ROC + volume · 1h | momentum | 92.30 | -7.70 | 41 | 4.9 | -3.56 | -0.30 | -17.18 | 403 |
| 66 | Squeeze breakout | breakout | 90.59 | -9.41 | 63 | 6.3 | -59.73 | -18.59 | -59.86 | 1182 |
| 67 | EMA 20/50 cross | trend | 89.99 | -10.01 | 76 | 14.5 | -78.62 | -17.74 | -78.70 | 1494 |
| 68 | ROC + volume | momentum | 89.75 | -10.25 | 108 | 16.7 | -72.41 | -18.12 | -72.46 | 1665 |
| 69 | Donchian 55/20 | breakout | 89.67 | -10.33 | 70 | 11.4 | -68.54 | -15.98 | -68.64 | 1333 |
| 70 | Volume breakout | breakout | 88.86 | -11.14 | 75 | 9.3 | -62.65 | -20.79 | -62.65 | 910 |
| 71 | Ichimoku | trend | 88.68 | -11.32 | 81 | 8.6 | -80.44 | -26.59 | -80.45 | 1761 |
| 72 | Keltner breakout | breakout | 88.52 | -11.48 | 104 | 8.7 | -85.03 | -35.95 | -85.07 | 1939 |
| 73 | Z-score reversion | reversion | 87.22 | -12.78 | 134 | 29.9 | -84.58 | -28.99 | -84.80 | 2087 |
| 74 | Supertrend | trend | 86.32 | -13.68 | 112 | 16.1 | -87.29 | -25.25 | -87.45 | 1982 |
| 75 | VWAP reversion ⏸ | reversion | 85.92 | -14.07 | 100 | 14.0 | -70.85 | -17.48 | -71.87 | 1417 |
| 76 | MACD zero-line | trend | 85.91 | -14.09 | 141 | 15.6 | -91.53 | -37.07 | -91.58 | 2368 |
| 77 | RSI momentum | momentum | 85.76 | -14.24 | 118 | 12.7 | -90.31 | -30.20 | -90.35 | 2399 |
| 78 | Bollinger breakout | breakout | 85.70 | -14.30 | 138 | 13.8 | -93.96 | -43.03 | -93.99 | 2879 |
| 79 | Donchian 20/10 | breakout | 85.59 | -14.41 | 131 | 14.5 | -90.86 | -30.12 | -90.94 | 2692 |
| 80 | Triple EMA stack | trend | 85.15 | -14.85 | 144 | 12.5 | -92.97 | -37.14 | -93.01 | 2624 |
| 81 | Trend pullback | trend | 84.49 | -15.51 | 127 | 16.5 | -90.50 | -34.47 | -90.50 | 2291 |
| 82 | Connors RSI(2) | reversion | 84.03 | -15.97 | 176 | 18.8 | -96.31 | -42.33 | -96.34 | 3645 |
| 83 | ADX DI cross | trend | 83.88 | -16.12 | 136 | 6.6 | -89.41 | -49.93 | -89.48 | 2129 |
| 84 | MFI reversion | reversion | 83.75 | -16.25 | 136 | 16.2 | -87.96 | -37.97 | -88.12 | 2179 |
| 85 | Stochastic reversion | reversion | 82.50 | -17.50 | 208 | 25.5 | -95.91 | -49.71 | -95.94 | 4052 |
| 86 | EMA 9/21 cross | trend | 81.43 | -18.57 | 187 | 12.3 | -97.39 | -43.66 | -97.41 | 3546 |
| 87 | Candlestick reversal ⏸ | reversion | 81.17 | -18.82 | 182 | 14.8 | -99.34 | -55.85 | -99.34 | 5569 |
| 88 | OBV trend | momentum | 80.85 | -19.15 | 187 | 12.3 | -95.82 | -51.30 | -95.83 | 3560 |
| 89 | Consensus | meta | 80.29 | -19.71 | 144 | 6.9 | -94.93 | -31.99 | -94.93 | 2685 |
| 90 | Bollinger reversion | reversion | 79.70 | -20.30 | 218 | 13.8 | -95.82 | -46.86 | -95.84 | 3682 |
| 91 | VWAP momentum | momentum | 79.41 | -20.59 | 247 | 8.9 | -98.46 | -37.26 | -98.46 | 5217 |
| 92 | Parabolic SAR | trend | 78.39 | -21.61 | 206 | 13.1 | -96.90 | -61.06 | -96.91 | 3653 |
| 93 | CCI reversion ⏸ | reversion | 76.76 | -23.24 | 159 | 5.7 | -98.46 | -56.50 | -98.47 | 4694 |
| 94 | MACD cross ⏸ | trend | 76.63 | -23.37 | 175 | 8.6 | -99.70 | -75.22 | -99.70 | 6102 |
| 95 | Williams %R ⏸ | reversion | 76.24 | -23.76 | 232 | 21.1 | -99.53 | -67.95 | -99.53 | 6082 |
| 96 | Heikin-Ashi ⏸ | trend | 75.47 | -24.53 | 190 | 3.2 | -99.89 | -105.27 | -99.89 | 8314 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-28T18:10 | Agent (ML meta-label) | buy | TQQQ | 4.64 | — | entry |
| 2026-09-28T18:10 | Agent (ML meta-label) | buy | COIN | 4.64 | — | following Stochastic reversion |
| 2026-09-28T18:10 | OBV trend | buy | IWM | 4.29 | — | entry |
| 2026-09-28T18:10 | OBV trend | sell | MSFT | 4.29 | -0.01 | rebalance down |
| 2026-09-28T18:10 | Parabolic SAR | buy | TQQQ | 7.13 | — | entry signal |
| 2026-09-28T18:10 | EMA 9/21 cross | buy | IWM | 3.19 | — | entry |
| 2026-09-28T18:10 | EMA 9/21 cross | buy | GOOGL | 3.70 | — | entry |
| 2026-09-28T18:10 | EMA 9/21 cross | sell | PLTR | 6.75 | -0.02 | exit signal |
| 2026-09-28T18:05 | Agent (ML meta-label) | sell | TQQQ | 2.02 | -0.00 | selected signal exited |
| 2026-09-28T18:05 | Agent (ML meta-label) | sell | SPY | 4.64 | -0.00 | selected signal exited |
| 2026-09-28T18:05 | Consensus | buy | TNA | 12.08 | — | entry |
| 2026-09-28T18:05 | Consensus | buy | NVDA | 16.07 | — | entry |
| 2026-09-28T18:05 | Consensus | buy | IWM | 16.07 | — | entry |
| 2026-09-28T18:05 | Consensus | sell | MSTR | 4.15 | 0.02 | rebalance down |
| 2026-09-28T18:05 | Agent (aggressive) | buy | AMD | 50.29 | — | following Stochastic reversion, CCI reversion |
| 2026-09-28T18:05 | Agent | buy | AMD | 19.99 | — | following Stochastic reversion, CCI reversion |
| 2026-09-28T18:05 | Stochastic reversion | buy | PLTR | 11.79 | — | entry signal |
| 2026-09-28T18:05 | Stochastic reversion | buy | AMD | 11.79 | — | entry signal |
| 2026-09-28T18:05 | Stochastic reversion | sell | TSLA | 8.81 | 0.00 | rebalance down |
| 2026-09-28T18:05 | Stochastic reversion | sell | SQQQ | 4.70 | 0.01 | rebalance down |
| 2026-09-28T18:05 | Stochastic reversion | sell | NVDA | 8.81 | -0.02 | rebalance down |
| 2026-09-28T18:05 | Stochastic reversion | sell | AAPL | 4.70 | -0.01 | rebalance down |
| 2026-09-28T18:05 | Connors RSI(2) | sell | AAPL | 20.99 | -0.02 | exit signal |
| 2026-09-28T18:05 | Keltner breakout | sell | TECL | 5.18 | -0.06 | stop-loss |
| 2026-09-28T18:05 | RSI momentum | buy | SOXL | 4.09 | — | entry |
| 2026-09-28T18:05 | RSI momentum | sell | TECL | 4.49 | -0.04 | stop-loss |
| 2026-09-28T18:05 | Parabolic SAR | sell | TECL | 6.49 | -0.04 | stop-loss |
| 2026-09-28T18:00 | Agent (ML meta-label) | buy | SPY | 4.64 | — | entry |
| 2026-09-28T18:00 | Consensus | buy | BTC-USD | 20.10 | — | entry |
| 2026-09-28T18:00 | Consensus | sell | SOL-USD | 19.98 | -0.19 | target is flat |
| 2026-09-28T18:00 | MFI reversion · 1h | buy | TNA | 5.40 | — | rebalance up |
| 2026-09-28T18:00 | MFI reversion · 1h | buy | SPY | 5.52 | — | rebalance up |
| 2026-09-28T18:00 | MFI reversion · 1h | buy | SOL-USD | 7.28 | — | rebalance up |
| 2026-09-28T18:00 | MFI reversion · 1h | buy | LABU | 5.00 | — | rebalance up |
| 2026-09-28T18:00 | MFI reversion · 1h | buy | IWM | 5.49 | — | rebalance up |
| 2026-09-28T18:00 | MFI reversion · 1h | sell | ETH-USD | 13.63 | 0.02 | exit signal |
| 2026-09-28T18:00 | CCI reversion · 1h | buy | SOXL | 4.91 | — | entry |
| 2026-09-28T18:00 | CCI reversion · 1h | sell | ETH-USD | 4.88 | 0.02 | exit signal |
| 2026-09-28T18:00 | Bollinger reversion · 1h | sell | SOL-USD | 9.77 | -0.05 | exit signal |
| 2026-09-28T18:00 | ROC + volume · 1h | buy | LABU | 8.62 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
