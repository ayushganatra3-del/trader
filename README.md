# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-25T16:35:05.000146+00:00 · 1230 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £100.27 (+0.27%)

Closed trades 6, win rate 83.3%, fees £0.24, max drawdown -0.52%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-25 | ETRA 12%, FTK 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, FOX 12%, ENHA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-24)

**Uptrend** since 2026-09-21 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 21.24 · VIX 15.67 · last follow-through day 2026-08-04

Best bullish scores: COIN 9.0, BITX 8.5, MSTR 8.5, ETHU 8.5, PLTR 8.0, META 8.0

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 2.63 | +8.92% | 5 |
| Stochastic reversion | PLTR | 2.58 | +5.23% | 12 |
| Williams %R | ETHU | 2.54 | +9.69% | 21 |
| Bollinger reversion | PLTR | 2.47 | +2.71% | 8 |
| Bollinger reversion | META | 2.46 | +1.15% | 9 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Donchian 20/10 · 1h | breakout | 100.67 | 0.67 | 1 | 0.0 | 20.39 | 2.75 | -12.78 | 211 |
| 2 | Parabolic SAR · 1h | trend | 100.63 | 0.63 | 1 | 0.0 | -2.13 | -0.13 | -18.82 | 301 |
| 3 | Agent (aggressive) | meta | 100.51 | 0.51 | 3 | 66.7 | 4.81 | 2.38 | -3.92 | 87 |
| 4 | Supertrend · 1h | trend | 100.40 | 0.40 | 1 | 0.0 | 3.74 | 0.71 | -16.43 | 196 |
| 5 | Max aggression: 5-day momentum | meta | 100.40 | 0.40 | 0 | — | 4.12 | 0.69 | -29.56 | 28 |
| 6 | Max aggression: 1-day momentum | meta | 100.40 | 0.40 | 0 | — | -28.62 | -1.54 | -49.41 | 41 |
| 7 | Candlestick reversal · 1h | reversion | 100.35 | 0.35 | 2 | 0.0 | -27.09 | -6.66 | -27.34 | 472 |
| 8 | EMA 20/50 cross · 1h | trend | 100.35 | 0.35 | 1 | 0.0 | 15.94 | 1.96 | -14.36 | 129 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.30 | 0.30 | 0 | — | -8.73 | -1.86 | -14.11 | 2 |
| 10 | Agent | meta | 100.27 | 0.27 | 6 | 83.3 | -8.28 | -5.10 | -10.19 | 221 |
| 11 | Ichimoku · 1h | trend | 100.26 | 0.26 | 1 | 0.0 | 12.20 | 1.61 | -15.13 | 117 |
| 12 | Triple EMA stack · 1h | trend | 100.25 | 0.25 | 3 | 0.0 | 1.99 | 0.48 | -22.96 | 218 |
| 13 | RSI momentum · 1h | momentum | 100.24 | 0.24 | 2 | 0.0 | 4.54 | 0.84 | -15.29 | 211 |
| 14 | Trend pullback · 1h | trend | 100.22 | 0.22 | 13 | 23.1 | -24.12 | -6.62 | -26.36 | 144 |
| 15 | Candlestick reversal | reversion | 100.21 | 0.21 | 26 | 46.2 | -99.23 | -55.46 | -99.23 | 5440 |
| 16 | Hold SPY | benchmark | 100.20 | 0.20 | 0 | — | 4.44 | 2.27 | -3.66 | 1 |
| 17 | EMA 9/21 cross · 1h | trend | 100.19 | 0.19 | 5 | 20.0 | 8.54 | 1.35 | -16.92 | 305 |
| 18 | RSI(14) reversion · 1h | reversion | 100.17 | 0.17 | 0 | — | 2.44 | 0.78 | -6.57 | 124 |
| 19 | Daily: Bullish score | daily | 100.16 | 0.16 | 2 | 0.0 | -0.02 | 0.20 | -12.76 | 13 |
| 20 | Williams %R · 1h | reversion | 100.16 | 0.16 | 14 | 78.6 | -18.94 | -3.53 | -22.09 | 483 |
| 21 | Hold BTC | benchmark | 100.16 | 0.16 | 0 | — | 29.36 | 3.62 | -8.68 | 1 |
| 22 | Three white soldiers | momentum | 100.13 | 0.13 | 2 | 50.0 | -50.59 | -28.83 | -50.62 | 604 |
| 23 | Timing: Nasdaq FTD · QQQ | daily | 100.13 | 0.13 | 0 | — | -2.62 | -1.68 | -4.71 | 2 |
| 24 | Squeeze breakout · 1h | breakout | 100.12 | 0.12 | 2 | 50.0 | 19.56 | 3.19 | -9.42 | 98 |
| 25 | Day trade: Stocks in Play ORB | daytrade | 100.11 | 0.11 | 0 | — | 9.72 | 3.78 | -2.67 | 95 |
| 26 | Copy: Congress Democrats (NANC) | copy | 100.08 | 0.08 | 0 | — | 6.94 | 2.66 | -3.62 | 1 |
| 27 | CCI reversion · 1h | reversion | 100.07 | 0.07 | 3 | 33.3 | -0.11 | 0.16 | -12.41 | 397 |
| 28 | Copy: Warren Buffett (BRK-B) | copy | 100.07 | 0.07 | 0 | — | -0.85 | -0.30 | -7.65 | 1 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 100.04 | 0.04 | 0 | — | 29.07 | 4.11 | -6.29 | 1 |
| 30 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | 10.05 | 2.28 | -7.87 | 43 |
| 31 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.56 | 1.43 | -7.93 | 7 |
| 32 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | 0.93 | 0.46 | -4.88 | 15 |
| 33 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 34 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | -0.41 | -0.62 | -1.49 | 18 |
| 35 | Three white soldiers · 1h | momentum | 100.00 | 0.00 | 0 | — | -3.69 | -2.89 | -5.45 | 29 |
| 36 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.00 | 0.00 | 0 | — | -6.03 | -1.74 | -12.40 | 24 |
| 37 | Daily: Momentum burst | daily | 99.98 | -0.01 | 0 | — | 1.61 | 0.44 | -14.85 | 49 |
| 38 | ADX DI cross · 1h | trend | 99.98 | -0.02 | 8 | 0.0 | -8.70 | -1.65 | -16.24 | 247 |
| 39 | Copy: Hedge-fund gurus (GURU) | copy | 99.93 | -0.07 | 0 | — | -0.69 | -0.29 | -5.14 | 1 |
| 40 | Z-score reversion · 1h | reversion | 99.90 | -0.10 | 2 | 0.0 | 4.39 | 1.09 | -8.60 | 149 |
| 41 | Connors RSI(2) · 1h | reversion | 99.86 | -0.14 | 3 | 33.3 | -12.45 | -4.04 | -13.88 | 221 |
| 42 | Donchian 55/20 · 1h | breakout | 99.85 | -0.15 | 1 | 0.0 | 7.00 | 1.14 | -16.96 | 113 |
| 43 | EMA 20/50 cross | trend | 99.73 | -0.27 | 14 | 35.7 | -77.54 | -17.29 | -77.68 | 1458 |
| 44 | Stochastic reversion · 1h | reversion | 99.64 | -0.36 | 12 | 58.3 | -9.47 | -2.06 | -12.08 | 318 |
| 45 | Bollinger reversion · 1h | reversion | 99.54 | -0.46 | 8 | 50.0 | -15.13 | -4.21 | -16.75 | 307 |
| 46 | OBV trend · 1h | momentum | 99.54 | -0.46 | 21 | 9.5 | -5.35 | -0.46 | -25.24 | 322 |
| 47 | MACD cross · 1h | trend | 99.44 | -0.56 | 6 | 0.0 | -14.37 | -2.44 | -21.81 | 452 |
| 48 | VWAP momentum · 1h | momentum | 99.44 | -0.56 | 25 | 4.0 | -33.63 | -5.00 | -35.50 | 1236 |
| 49 | Opening range 30m | breakout | 99.34 | -0.66 | 2 | 0.0 | -6.64 | -1.91 | -13.54 | 549 |
| 50 | Bollinger breakout · 1h | breakout | 99.17 | -0.83 | 5 | 20.0 | 16.35 | 2.26 | -11.13 | 281 |
| 51 | Gap and go | momentum | 99.13 | -0.87 | 4 | 0.0 | 16.78 | 4.19 | -4.73 | 189 |
| 52 | Keltner breakout · 1h | breakout | 98.86 | -1.14 | 2 | 0.0 | 3.21 | 0.64 | -18.68 | 218 |
| 53 | Copy: Insider buying | copy | 98.84 | -1.16 | 0 | — | -9.20 | -1.67 | -17.74 | 73 |
| 54 | MACD zero-line · 1h | trend | 98.83 | -1.17 | 4 | 0.0 | 1.96 | 0.48 | -14.64 | 221 |
| 55 | RSI(14) reversion | reversion | 98.70 | -1.30 | 17 | 41.2 | -70.70 | -22.00 | -70.98 | 1464 |
| 56 | Heikin-Ashi · 1h | trend | 98.52 | -1.48 | 17 | 23.5 | -19.69 | -2.95 | -27.53 | 671 |
| 57 | VWAP reversion · 1h | reversion | 98.44 | -1.56 | 13 | 0.0 | -14.07 | -5.01 | -15.07 | 114 |
| 58 | Opening range 15m | breakout | 98.38 | -1.62 | 9 | 0.0 | -9.56 | -2.56 | -16.14 | 685 |
| 59 | Agent (rotation) | meta | 98.36 | -1.64 | 24 | 8.3 | -5.38 | -1.67 | -11.50 | 221 |
| 60 | Supertrend | trend | 98.20 | -1.80 | 26 | 26.9 | -86.87 | -24.88 | -86.92 | 1940 |
| 61 | Stochastic reversion | reversion | 97.40 | -2.60 | 53 | 35.8 | -95.67 | -48.27 | -95.69 | 3993 |
| 62 | MACD zero-line | trend | 97.34 | -2.66 | 25 | 20.0 | -91.41 | -36.68 | -91.41 | 2338 |
| 63 | Triple EMA stack | trend | 97.32 | -2.68 | 38 | 18.4 | -92.61 | -36.98 | -92.65 | 2591 |
| 64 | MFI reversion · 1h | reversion | 97.03 | -2.97 | 25 | 0.0 | -9.34 | -1.74 | -17.28 | 134 |
| 65 | Volume breakout · 1h | breakout | 96.86 | -3.14 | 21 | 4.8 | 10.23 | 1.61 | -12.60 | 127 |
| 66 | Z-score reversion | reversion | 96.77 | -3.23 | 29 | 24.1 | -83.96 | -28.53 | -84.03 | 2042 |
| 67 | ROC + volume · 1h | momentum | 96.74 | -3.26 | 24 | 8.3 | 4.88 | 0.87 | -17.18 | 398 |
| 68 | ROC + volume | momentum | 96.56 | -3.44 | 31 | 12.9 | -71.21 | -17.82 | -71.46 | 1612 |
| 69 | Keltner breakout | breakout | 96.43 | -3.57 | 24 | 12.5 | -84.56 | -36.31 | -84.68 | 1898 |
| 70 | Volume breakout | breakout | 96.39 | -3.61 | 23 | 8.7 | -61.78 | -21.70 | -62.02 | 879 |
| 71 | Donchian 55/20 | breakout | 96.32 | -3.68 | 22 | 13.6 | -68.11 | -16.02 | -68.14 | 1317 |
| 72 | RSI momentum | momentum | 96.25 | -3.75 | 30 | 23.3 | -90.10 | -30.55 | -90.15 | 2367 |
| 73 | Ichimoku | trend | 96.19 | -3.81 | 30 | 16.7 | -79.41 | -26.54 | -79.46 | 1747 |
| 74 | EMA 9/21 cross | trend | 96.06 | -3.94 | 44 | 15.9 | -97.27 | -44.02 | -97.28 | 3482 |
| 75 | Bollinger reversion | reversion | 95.97 | -4.04 | 55 | 29.1 | -95.56 | -45.64 | -95.62 | 3617 |
| 76 | Squeeze breakout | breakout | 95.68 | -4.32 | 24 | 0.0 | -59.18 | -19.43 | -59.24 | 1179 |
| 77 | VWAP momentum | momentum | 95.04 | -4.96 | 78 | 10.3 | -98.25 | -36.62 | -98.26 | 5076 |
| 78 | Donchian 20/10 | breakout | 94.85 | -5.15 | 36 | 16.7 | -90.65 | -30.96 | -90.72 | 2669 |
| 79 | Bollinger breakout | breakout | 94.76 | -5.24 | 35 | 8.6 | -93.69 | -44.73 | -93.75 | 2845 |
| 80 | OBV trend | momentum | 94.66 | -5.34 | 53 | 11.3 | -95.45 | -53.33 | -95.48 | 3495 |
| 81 | Connors RSI(2) | reversion | 94.57 | -5.43 | 57 | 24.6 | -96.19 | -43.55 | -96.21 | 3595 |
| 82 | Trend pullback | trend | 94.16 | -5.84 | 48 | 18.8 | -90.03 | -34.90 | -90.13 | 2266 |
| 83 | Parabolic SAR | trend | 94.15 | -5.85 | 55 | 20.0 | -96.61 | -61.52 | -96.61 | 3587 |
| 84 | ADX DI cross | trend | 94.10 | -5.90 | 47 | 4.3 | -88.78 | -49.53 | -88.78 | 2076 |
| 85 | VWAP reversion ⏸ | reversion | 93.88 | -6.12 | 46 | 4.3 | -69.35 | -17.12 | -70.19 | 1403 |
| 86 | Williams %R | reversion | 93.67 | -6.33 | 88 | 38.6 | -99.43 | -67.22 | -99.44 | 5970 |
| 87 | CCI reversion ⏸ | reversion | 93.00 | -7.00 | 48 | 8.3 | -98.19 | -56.20 | -98.20 | 4595 |
| 88 | MACD cross ⏸ | trend | 92.91 | -7.09 | 58 | 17.2 | -99.65 | -73.19 | -99.65 | 5975 |
| 89 | Consensus ⏸ | meta | 92.69 | -7.32 | 51 | 11.8 | -94.51 | -31.92 | -94.52 | 2625 |
| 90 | MFI reversion ⏸ | reversion | 92.37 | -7.63 | 54 | 3.7 | -87.81 | -41.47 | -87.86 | 2150 |
| 91 | Heikin-Ashi ⏸ | trend | 91.62 | -8.38 | 65 | 6.2 | -99.86 | -103.19 | -99.86 | 8210 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-25T16:35 | Candlestick reversal | buy | XRP-USD | 10.02 | — | rebalance up |
| 2026-09-25T16:35 | Candlestick reversal | buy | META | 5.70 | — | rebalance up |
| 2026-09-25T16:35 | Candlestick reversal | buy | DOGE-USD | 5.74 | — | rebalance up |
| 2026-09-25T16:35 | Candlestick reversal | buy | BITX | 5.75 | — | rebalance up |
| 2026-09-25T16:35 | Candlestick reversal | buy | AMD | 5.68 | — | rebalance up |
| 2026-09-25T16:35 | Candlestick reversal | sell | ETH-USD | 14.28 | -0.11 | exit signal |
| 2026-09-25T16:35 | Candlestick reversal | sell | COIN | 14.30 | -0.03 | exit signal |
| 2026-09-25T16:35 | Volume breakout | sell | IWM | 24.15 | -0.07 | exit signal |
| 2026-09-25T16:35 | Bollinger breakout | sell | GOOGL | 7.28 | -0.02 | exit signal |
| 2026-09-25T16:35 | VWAP momentum | sell | XRP-USD | 5.51 | -0.05 | exit signal |
| 2026-09-25T16:35 | VWAP momentum | sell | GOOGL | 5.58 | -0.01 | exit signal |
| 2026-09-25T16:35 | VWAP momentum | sell | COIN | 5.16 | -0.03 | exit signal |
| 2026-09-25T16:35 | VWAP momentum | sell | BITX | 5.91 | -0.03 | exit signal |
| 2026-09-25T16:35 | ADX DI cross | buy | TNA | 7.84 | — | rebalance up |
| 2026-09-25T16:35 | ADX DI cross | buy | AAPL | 7.77 | — | rebalance up |
| 2026-09-25T16:35 | ADX DI cross | sell | ETHU | 18.83 | -0.08 | exit signal |
| 2026-09-25T16:35 | ADX DI cross | sell | ETH-USD | 12.37 | -0.11 | exit signal |
| 2026-09-25T16:35 | ADX DI cross | sell | BTC-USD | 15.66 | -0.12 | exit signal |
| 2026-09-25T16:35 | ADX DI cross | sell | BITX | 15.75 | -0.05 | exit signal |
| 2026-09-25T16:35 | Parabolic SAR | buy | DOGE-USD | 3.83 | — | entry |
| 2026-09-25T16:35 | Parabolic SAR | buy | AAPL | 5.54 | — | entry signal |
| 2026-09-25T16:35 | Parabolic SAR | sell | GOOGL | 9.37 | 0.01 | exit signal |
| 2026-09-25T16:30 | Agent (aggressive) | sell | PLTR | 50.32 | 0.13 | selected signal exited |
| 2026-09-25T16:30 | Agent | sell | PLTR | 20.02 | 0.02 | selected signal exited |
| 2026-09-25T16:30 | MFI reversion · 1h | buy | UPRO | 2.16 | — | entry |
| 2026-09-25T16:30 | MFI reversion · 1h | buy | SPY | 8.84 | — | entry |
| 2026-09-25T16:30 | MFI reversion · 1h | buy | MSTR | 8.84 | — | entry |
| 2026-09-25T16:30 | MFI reversion · 1h | buy | LABU | 5.30 | — | rebalance up |
| 2026-09-25T16:30 | MFI reversion · 1h | sell | TNA | 5.14 | 0.05 | rebalance down |
| 2026-09-25T16:30 | MFI reversion · 1h | sell | IWM | 5.05 | 0.02 | rebalance down |
| 2026-09-25T16:30 | MFI reversion · 1h | sell | COIN | 4.87 | -0.07 | rebalance down |
| 2026-09-25T16:30 | MFI reversion · 1h | sell | BTC-USD | 4.98 | -0.08 | rebalance down |
| 2026-09-25T16:30 | MFI reversion · 1h | sell | AMZN | 5.11 | 0.02 | rebalance down |
| 2026-09-25T16:30 | Williams %R · 1h | buy | TSLA | 12.56 | — | entry signal |
| 2026-09-25T16:30 | Williams %R · 1h | buy | MSTR | 12.56 | — | entry signal |
| 2026-09-25T16:30 | Williams %R · 1h | buy | BITX | 6.30 | — | rebalance up |
| 2026-09-25T16:30 | Williams %R · 1h | sell | TQQQ | 9.15 | 0.06 | exit signal |
| 2026-09-25T16:30 | Williams %R · 1h | sell | TNA | 4.66 | 0.07 | exit signal |
| 2026-09-25T16:30 | Williams %R · 1h | sell | SPY | 9.12 | 0.02 | exit signal |
| 2026-09-25T16:30 | Williams %R · 1h | sell | QQQ | 9.11 | 0.02 | exit signal |

## Data problems on the last tick

- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-07-28 16:35:05.000146+00:00 -> 2026-09-25 16:45:05.000146+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
