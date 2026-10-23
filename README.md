# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T17:43:05.000139+00:00 · 33305 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.30 (-10.70%)

Closed trades 101, win rate 38.6%, fees £3.19, max drawdown -11.12%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 28182 decisions in 2682 calls, $0.3529 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T17:43 | 1 / 12 / 17 | cash |  |
| Breezy | 2026-10-23T17:43 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-10-23T17:43 | 5 / 23 / 2 | COIN 64% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| Stochastic reversion | BITX | 1.69 | +8.43% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.41 | 6.41 | 0 | — | 7.85 | 4.13 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.17 | 2.05 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.72 | -3.30 | -13.74 | 150 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.37 | 0.37 | 0 | — | 2.95 | 1.40 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.15 | -0.85 | 73 | 34.2 | 5.24 | 2.57 | -2.26 | 102 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.94 | -2.06 | 0 | — | -0.64 | -0.34 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.51 | -3.49 | 0 | — | 1.47 | 0.42 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 95.98 | -4.02 | 120 | 30.8 | -2.47 | -1.44 | -6.22 | 195 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.75 | -4.25 | 0 | — | -0.85 | -0.30 | -5.99 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.83 | -5.17 | 0 | — | -6.26 | -2.67 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.13 | -5.87 | 25 | 40.0 | -14.89 | -2.85 | -20.68 | 71 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 21 | Trend pullback · 1h | trend | 93.65 | -6.35 | 95 | 23.2 | -21.64 | -7.12 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.29 | -6.71 | 241 | 34.9 | -10.84 | -3.38 | -17.21 | 562 |
| 23 | Donchian 55/20 · 1h | breakout | 93.06 | -6.94 | 48 | 16.7 | -16.18 | -3.67 | -17.44 | 98 |
| 24 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -14.47 | -1.33 | -27.80 | 24 |
| 25 | Daily: Momentum burst | daily | 92.07 | -7.93 | 10 | 10.0 | -17.20 | -3.34 | -20.97 | 40 |
| 26 | Parabolic SAR · 1h | trend | 91.95 | -8.05 | 118 | 25.4 | -21.04 | -5.00 | -24.17 | 254 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.13 | -8.87 | 108 | 18.5 | -11.72 | -2.41 | -14.53 | 255 |
| 30 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 31 | Agent | meta | 89.30 | -10.70 | 101 | 38.6 | -10.98 | -7.59 | -11.70 | 205 |
| 32 | Daily: Bullish score | daily | 89.27 | -10.73 | 9 | 0.0 | -8.36 | -1.10 | -14.40 | 14 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.18 | -10.82 | 0 | — | -5.32 | -0.78 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.94 | -11.06 | 105 | 27.6 | -12.32 | -2.45 | -16.56 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.57 | -12.43 | 186 | 45.2 | -19.96 | -3.77 | -22.47 | 385 |
| 36 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.78 | -4.42 | -15.12 | 95 |
| 37 | EMA 20/50 cross · 1h | trend | 86.63 | -13.37 | 71 | 11.3 | -22.39 | -4.48 | -25.11 | 138 |
| 38 | Opening range 15m | breakout | 86.40 | -13.60 | 305 | 30.2 | -15.71 | -4.59 | -17.87 | 703 |
| 39 | Keltner breakout · 1h | breakout | 86.23 | -13.77 | 73 | 23.3 | -22.77 | -4.84 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 86.03 | -13.97 | 108 | 14.8 | -23.78 | -5.03 | -26.46 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.44 | -14.55 | 101 | 15.8 | -21.64 | -4.65 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.30 | -8.05 | -27.06 | 196 |
| 43 | MACD cross · 1h | trend | 85.07 | -14.93 | 216 | 23.1 | -22.69 | -4.54 | -26.15 | 451 |
| 44 | Z-score reversion · 1h | reversion | 83.93 | -16.07 | 106 | 34.0 | -14.81 | -2.51 | -21.48 | 197 |
| 45 | Ichimoku · 1h | trend | 83.83 | -16.17 | 65 | 12.3 | -23.79 | -4.97 | -25.68 | 110 |
| 46 | Triple EMA stack · 1h | trend | 83.79 | -16.21 | 98 | 15.3 | -25.97 | -5.21 | -28.44 | 211 |
| 47 | MFI reversion · 1h | reversion | 82.24 | -17.76 | 257 | 31.9 | -17.41 | -2.85 | -20.54 | 143 |
| 48 | MACD zero-line · 1h | trend | 81.99 | -18.01 | 103 | 15.5 | -21.36 | -4.48 | -24.82 | 218 |
| 49 | OBV trend · 1h | momentum | 81.49 | -18.51 | 202 | 17.3 | -31.82 | -7.04 | -33.60 | 304 |
| 50 | Donchian 20/10 · 1h | breakout | 81.42 | -18.58 | 96 | 19.8 | -24.36 | -4.75 | -27.45 | 217 |
| 51 | Three white soldiers | momentum | 81.33 | -18.67 | 274 | 20.1 | -43.50 | -21.10 | -43.62 | 588 |
| 52 | Williams %R · 1h | reversion | 81.32 | -18.68 | 213 | 44.1 | -35.20 | -6.32 | -36.69 | 522 |
| 53 | Bollinger reversion · 1h | reversion | 80.44 | -19.56 | 171 | 34.5 | -30.96 | -6.47 | -32.19 | 359 |
| 54 | CCI reversion · 1h | reversion | 80.31 | -19.69 | 198 | 42.9 | -26.40 | -3.98 | -28.17 | 451 |
| 55 | Agent (ML meta-label) | meta | 80.03 | -19.97 | 849 | 18.8 | -12.00 | -2.18 | -16.23 | 381 |
| 56 | Heikin-Ashi · 1h | trend | 79.03 | -20.97 | 268 | 23.1 | -42.96 | -10.10 | -43.65 | 653 |
| 57 | ROC + volume · 1h | momentum | 78.18 | -21.82 | 239 | 23.8 | -30.93 | -6.22 | -32.05 | 380 |
| 58 | RSI(14) reversion · 1h | reversion | 78.03 | -21.97 | 91 | 23.1 | -15.01 | -2.78 | -23.51 | 186 |
| 59 | Candlestick reversal · 1h | reversion | 77.73 | -22.27 | 253 | 28.9 | -34.59 | -6.54 | -36.06 | 539 |
| 60 | EMA 9/21 cross · 1h | trend | 77.52 | -22.48 | 158 | 12.0 | -29.82 | -6.13 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 76.05 | -23.95 | 515 | 21.4 | -50.15 | -11.70 | -50.30 | 1209 |
| 62 | Max aggression: 1-day momentum | meta | 67.14 | -32.86 | 18 | 27.8 | -42.71 | -3.00 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.67 | -42.33 | 705 | 22.7 | -74.64 | -27.22 | -74.68 | 1543 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -61.04 | -26.20 | -61.04 | 765 |
| 65 | Squeeze breakout | breakout | 53.96 | -46.04 | 546 | 14.3 | -66.00 | -28.81 | -66.19 | 1139 |
| 66 | RSI(14) reversion | reversion | 53.33 | -46.67 | 821 | 26.4 | -76.42 | -19.64 | -76.81 | 1665 |
| 67 | Donchian 55/20 | breakout | 53.22 | -46.78 | 564 | 19.1 | -71.49 | -23.75 | -71.63 | 1251 |
| 68 | EMA 20/50 cross | trend | 52.02 | -47.98 | 612 | 20.1 | -78.77 | -23.91 | -79.06 | 1407 |
| 69 | VWAP reversion | reversion | 50.68 | -49.33 | 814 | 25.1 | -74.54 | -17.58 | -74.76 | 1544 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -45.13 | -98.66 | 5006 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.74 | -47.84 | -93.78 | 2502 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.33 | -30.35 | -88.50 | 1873 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.07 | -38.55 | -91.13 | 2301 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.32 | -31.57 | -90.35 | 2143 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.61 | -54.70 | -97.63 | 3435 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.93 | -62.52 | -95.95 | 3315 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -35.49 | -93.74 | 2424 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.61 | -36.45 | -82.65 | 1676 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -54.29 | -99.31 | 5645 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.13 | -42.30 | -92.19 | 2569 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -40.60 | -95.29 | 3348 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.88 | -99.74 | 6056 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.89 | -46.36 | -91.90 | 2301 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -66.27 | -97.49 | 3505 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -59.43 | -98.46 | 4695 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.14 | -60.16 | -94.16 | 2722 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.58 | -39.90 | -83.65 | 1767 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -66.10 | -99.53 | 6135 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.46 | -28.62 | -87.65 | 2173 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.06 | -38.24 | -90.13 | 2226 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -47.47 | -95.87 | 3731 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -50.68 | -89.36 | 2076 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.00 | -47.97 | -96.06 | 4098 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -112.00 | -99.90 | 8107 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T17:40 | Agent | sell | MSTR | 17.72 | -0.17 | selected signal exited |
| 2026-10-23T17:40 | ROC + volume | sell | MSTR | 14.35 | -0.08 | exit signal |
| 2026-10-23T17:35 | OBV trend · 1h | sell | IWM | 20.28 | -0.01 | target is flat |
| 2026-10-23T17:35 | Opening range 30m | buy | TNA | 3.68 | — | entry |
| 2026-10-23T17:35 | Opening range 30m | buy | MSTR | 5.67 | — | rebalance up |
| 2026-10-23T17:35 | Opening range 30m | sell | GOOGL | 9.35 | -0.06 | stop-loss |
| 2026-10-23T17:30 | Connors RSI(2) · 1h | sell | SQQQ | 21.53 | 0.23 | exit signal |
| 2026-10-23T17:30 | Candlestick reversal · 1h | buy | PLTR | 1.79 | — | entry |
| 2026-10-23T17:30 | Candlestick reversal · 1h | buy | IWM | 5.55 | — | entry |
| 2026-10-23T17:30 | Candlestick reversal · 1h | sell | SOXL | 7.02 | -0.01 | exit signal |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | SOL-USD | 3.95 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | MSTR | 3.91 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | MSFT | 3.97 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | META | 3.97 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | ETHU | 8.47 | — | entry signal |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | ETH-USD | 3.96 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | DOGE-USD | 3.97 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | BTC-USD | 3.96 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | BITX | 8.47 | — | entry signal |
| 2026-10-23T17:30 | VWAP momentum · 1h | sell | UPRO | 4.39 | -0.04 | exit signal |
| 2026-10-23T17:30 | VWAP momentum · 1h | sell | TECL | 4.45 | 0.01 | exit signal |
| 2026-10-23T17:30 | VWAP momentum · 1h | sell | SOXL | 4.44 | -0.06 | exit signal |
| 2026-10-23T17:30 | VWAP momentum · 1h | sell | QQQ | 6.35 | -0.01 | exit signal |
| 2026-10-23T17:30 | VWAP momentum · 1h | sell | AMD | 4.47 | -0.02 | exit signal |
| 2026-10-23T17:30 | Heikin-Ashi · 1h | buy | TECL | 6.61 | — | rebalance up |
| 2026-10-23T17:30 | Heikin-Ashi · 1h | buy | MSTR | 19.79 | — | entry signal |
| 2026-10-23T17:30 | Heikin-Ashi · 1h | buy | MSFT | 6.50 | — | rebalance up |
| 2026-10-23T17:30 | Heikin-Ashi · 1h | sell | TQQQ | 13.18 | -0.08 | exit signal |
| 2026-10-23T17:30 | Heikin-Ashi · 1h | sell | SOXL | 13.06 | -0.21 | exit signal |
| 2026-10-23T17:30 | Heikin-Ashi · 1h | sell | QQQ | 13.24 | -0.03 | exit signal |
| 2026-10-23T17:30 | Heikin-Ashi · 1h | sell | AMD | 13.17 | -0.09 | exit signal |
| 2026-10-23T17:30 | Parabolic SAR · 1h | sell | AAPL | 22.93 | -0.00 | exit signal |
| 2026-10-23T17:30 | Triple EMA stack · 1h | buy | MSTR | 20.41 | — | entry signal |
| 2026-10-23T17:30 | RSI(14) reversion | buy | AAPL | 13.34 | — | entry signal |
| 2026-10-23T17:25 | VWAP reversion | sell | SQQQ | 12.77 | 0.13 | exit signal |
| 2026-10-23T17:25 | Squeeze breakout | buy | SQQQ | 13.50 | — | entry signal |
| 2026-10-23T17:25 | Opening range 30m | buy | MSTR | 2.11 | — | entry |
| 2026-10-23T17:25 | Opening range 30m | sell | SPY | 2.11 | -0.01 | exit signal |
| 2026-10-23T17:25 | Donchian 55/20 | sell | SOXL | 13.21 | -0.34 | stop-loss |
| 2026-10-23T17:25 | EMA 20/50 cross | buy | SQQQ | 5.78 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 17:43:05.000139+00:00 -> 2026-10-23 17:53:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
