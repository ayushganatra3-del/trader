# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T09:25:05.000109+00:00 · 30542 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.86 (-9.14%)

Closed trades 90, win rate 41.1%, fees £2.98, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-20)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.22 · VIX 17.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 6939 decisions in 1389 calls, $0.0970 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T09:25 | 1 / 4 / 0 | XRP-USD 17% |  |
| Breezy | 2026-10-21T09:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T09:25 | 3 / 2 / 0 | XRP-USD 64% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.84 | +3.15% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.98 | 5.98 | 0 | — | 8.23 | 3.84 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 100.62 | 0.62 | 9 | 44.4 | -13.29 | -0.93 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.90 | -1.10 | 0 | — | 0.33 | 0.23 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.70 | -1.30 | 62 | 35.5 | 4.19 | 2.20 | -1.45 | 61 |
| 11 | Hold BTC | benchmark | 98.58 | -1.42 | 0 | — | 15.51 | 2.23 | -8.68 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 98.40 | -1.60 | 0 | — | -0.73 | -0.22 | -5.15 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 97.97 | -2.03 | 3 | 33.3 | 4.26 | 0.99 | -7.93 | 8 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.83 | -2.16 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.86 | -3.13 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.72 | -3.28 | 0 | — | 0.02 | 0.07 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.59 | -3.41 | 40 | 15.0 | -14.08 | -2.81 | -15.92 | 100 |
| 19 | Agent (rotation) | meta | 96.05 | -3.95 | 114 | 31.6 | -6.34 | -3.12 | -8.16 | 302 |
| 20 | Copy: Insider buying | copy | 96.05 | -3.95 | 25 | 40.0 | -11.99 | -2.06 | -20.62 | 72 |
| 21 | Trend pullback · 1h | trend | 95.78 | -4.22 | 90 | 23.3 | -19.12 | -5.78 | -19.68 | 130 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.52 | -5.48 | 89 | 18.0 | -13.20 | -2.48 | -16.12 | 252 |
| 24 | Daily: Momentum burst | daily | 94.04 | -5.96 | 6 | 16.7 | -6.94 | -0.92 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.71 | 1.50 | -6.51 | 196 |
| 26 | Parabolic SAR · 1h | trend | 92.24 | -7.76 | 106 | 21.7 | -17.50 | -3.74 | -20.69 | 271 |
| 27 | Opening range 30m | breakout | 92.11 | -7.89 | 225 | 32.4 | -13.40 | -3.91 | -17.26 | 565 |
| 28 | Squeeze breakout · 1h | breakout | 91.98 | -8.02 | 46 | 21.7 | -2.98 | -0.65 | -11.48 | 98 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.25 | -2.32 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 91.06 | -8.94 | 7 | 0.0 | -7.95 | -0.90 | -13.10 | 13 |
| 31 | Agent | meta | 90.86 | -9.14 | 90 | 41.1 | -8.01 | -4.42 | -11.79 | 233 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.72 | -9.28 | 0 | — | 0.92 | 0.30 | -14.37 | 1 |
| 33 | Bollinger breakout · 1h | breakout | 90.62 | -9.38 | 87 | 29.9 | -13.70 | -2.59 | -16.36 | 258 |
| 34 | Volume breakout · 1h | breakout | 90.57 | -9.43 | 85 | 22.4 | -12.73 | -2.28 | -14.09 | 104 |
| 35 | RSI momentum · 1h | momentum | 89.54 | -10.46 | 83 | 15.7 | -24.20 | -4.70 | -25.28 | 217 |
| 36 | Connors RSI(2) · 1h | reversion | 89.26 | -10.74 | 155 | 41.9 | -22.05 | -6.56 | -23.42 | 197 |
| 37 | EMA 20/50 cross · 1h | trend | 88.80 | -11.20 | 62 | 12.9 | -18.93 | -3.47 | -21.45 | 132 |
| 38 | Supertrend · 1h | trend | 88.36 | -11.64 | 88 | 12.5 | -21.99 | -4.34 | -26.62 | 221 |
| 39 | Opening range 15m | breakout | 88.26 | -11.74 | 270 | 29.3 | -17.73 | -4.78 | -20.79 | 699 |
| 40 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -7.70 | -2.30 | -12.85 | 117 |
| 41 | Stochastic reversion · 1h | reversion | 87.71 | -12.29 | 164 | 47.0 | -14.69 | -2.45 | -22.24 | 362 |
| 42 | Keltner breakout · 1h | breakout | 87.37 | -12.63 | 60 | 21.7 | -19.85 | -3.69 | -26.64 | 206 |
| 43 | Ichimoku · 1h | trend | 86.98 | -13.02 | 60 | 13.3 | -18.79 | -3.54 | -20.25 | 118 |
| 44 | MACD cross · 1h | trend | 86.18 | -13.82 | 197 | 20.8 | -25.96 | -4.88 | -33.71 | 468 |
| 45 | Triple EMA stack · 1h | trend | 85.58 | -14.42 | 91 | 14.3 | -29.66 | -5.46 | -31.81 | 227 |
| 46 | Donchian 20/10 · 1h | breakout | 84.87 | -15.13 | 81 | 17.3 | -20.66 | -3.82 | -28.49 | 221 |
| 47 | Z-score reversion · 1h | reversion | 84.45 | -15.55 | 96 | 30.2 | -14.30 | -2.35 | -21.32 | 195 |
| 48 | OBV trend · 1h | momentum | 84.09 | -15.91 | 186 | 17.2 | -31.92 | -5.96 | -32.24 | 312 |
| 49 | MFI reversion · 1h | reversion | 83.91 | -16.09 | 220 | 30.5 | -14.87 | -2.33 | -20.43 | 140 |
| 50 | Agent (ML meta-label) | meta | 83.60 | -16.40 | 711 | 19.1 | -7.54 | -1.23 | -16.61 | 371 |
| 51 | MACD zero-line · 1h | trend | 83.52 | -16.48 | 91 | 15.4 | -25.76 | -5.06 | -26.67 | 227 |
| 52 | Three white soldiers | momentum | 82.36 | -17.64 | 252 | 19.4 | -46.63 | -18.27 | -47.27 | 611 |
| 53 | Bollinger reversion · 1h | reversion | 82.21 | -17.79 | 162 | 35.8 | -29.42 | -5.70 | -32.84 | 347 |
| 54 | ROC + volume · 1h | momentum | 81.38 | -18.62 | 208 | 22.6 | -30.66 | -5.73 | -34.03 | 390 |
| 55 | Williams %R · 1h | reversion | 81.33 | -18.67 | 195 | 43.6 | -30.71 | -4.75 | -36.50 | 524 |
| 56 | CCI reversion · 1h | reversion | 80.71 | -19.29 | 178 | 41.6 | -18.25 | -2.28 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.09 | -19.91 | 233 | 20.6 | -43.30 | -9.21 | -47.30 | 670 |
| 58 | EMA 9/21 cross · 1h | trend | 79.65 | -20.35 | 143 | 10.5 | -29.26 | -6.09 | -30.12 | 326 |
| 59 | RSI(14) reversion · 1h | reversion | 79.54 | -20.46 | 83 | 22.9 | -15.38 | -2.71 | -23.28 | 184 |
| 60 | VWAP momentum · 1h | momentum | 77.61 | -22.39 | 467 | 20.6 | -45.60 | -8.30 | -50.23 | 1259 |
| 61 | Candlestick reversal · 1h | reversion | 77.33 | -22.67 | 226 | 28.8 | -36.94 | -6.76 | -38.97 | 543 |
| 62 | Max aggression: 1-day momentum | meta | 77.11 | -22.89 | 17 | 29.4 | -27.91 | -1.54 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 60.62 | -39.38 | 637 | 22.8 | -77.60 | -21.75 | -78.54 | 1715 |
| 64 | Volume breakout | breakout | 60.55 | -39.45 | 386 | 13.7 | -64.07 | -19.90 | -64.09 | 864 |
| 65 | Squeeze breakout | breakout | 57.94 | -42.06 | 497 | 13.9 | -66.26 | -22.42 | -67.01 | 1208 |
| 66 | RSI(14) reversion | reversion | 57.37 | -42.63 | 745 | 26.6 | -74.17 | -16.23 | -74.89 | 1623 |
| 67 | Donchian 55/20 | breakout | 57.17 | -42.83 | 510 | 19.0 | -71.22 | -18.21 | -73.66 | 1278 |
| 68 | EMA 20/50 cross | trend | 55.45 | -44.55 | 557 | 19.6 | -78.08 | -17.14 | -80.87 | 1445 |
| 69 | VWAP reversion | reversion | 53.60 | -46.40 | 757 | 25.2 | -71.42 | -14.46 | -72.31 | 1495 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.77 | -31.02 | -98.79 | 5284 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.66 | -31.98 | -94.11 | 2596 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.38 | -21.88 | -88.51 | 1898 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.65 | -25.55 | -91.58 | 2360 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.25 | -26.18 | -91.45 | 2254 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.68 | -34.40 | -97.74 | 3530 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.80 | -37.30 | -96.91 | 3603 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.45 | -28.34 | -94.53 | 2529 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.60 | -27.53 | -83.04 | 1706 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.36 | -99.38 | 5754 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.74 | -27.43 | -92.50 | 2621 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.96 | -31.45 | -95.96 | 3461 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -41.52 | -99.75 | 6189 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.66 | -29.45 | -91.80 | 2359 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -39.41 | -97.76 | 3606 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.31 | -98.48 | 4715 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.16 | -35.65 | -94.29 | 2802 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.40 | -28.00 | -84.11 | 1802 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.91 | -99.53 | 6189 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.75 | -22.24 | -87.01 | 2147 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.64 | -25.90 | -88.03 | 2139 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -32.51 | -95.93 | 3766 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -33.14 | -89.36 | 2104 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -33.10 | -95.77 | 4109 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.47 | -99.91 | 8289 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T09:25 | Donchian 55/20 | buy | SOL-USD | 2.86 | — | rebalance up |
| 2026-10-21T09:15 | ROC + volume | buy | XRP-USD | 15.16 | — | entry signal |
| 2026-10-21T09:00 | Heikin-Ashi · 1h | buy | SOL-USD | 7.90 | — | entry signal |
| 2026-10-21T09:00 | MACD cross · 1h | buy | BTC-USD | 5.38 | — | entry signal |
| 2026-10-21T08:55 | ROC + volume | sell | XRP-USD | 15.26 | -0.04 | exit signal |
| 2026-10-21T08:35 | Volume breakout | sell | XRP-USD | 15.05 | -0.14 | exit signal |
| 2026-10-21T08:35 | Volume breakout | sell | BTC-USD | 15.10 | -0.11 | exit signal |
| 2026-10-21T08:35 | Squeeze breakout | sell | SOL-USD | 14.41 | -0.07 | stop-loss |
| 2026-10-21T08:35 | Donchian 55/20 | sell | DOGE-USD | 11.24 | -0.10 | stop-loss |
| 2026-10-21T08:35 | ROC + volume | sell | ETH-USD | 15.14 | -0.15 | exit signal |
| 2026-10-21T08:35 | EMA 20/50 cross | sell | DOGE-USD | 5.44 | -0.05 | stop-loss |
| 2026-10-21T08:30 | ROC + volume | sell | SOL-USD | 15.18 | -0.12 | exit signal |
| 2026-10-21T08:30 | ROC + volume | sell | DOGE-USD | 15.05 | -0.12 | exit signal |
| 2026-10-21T08:26 | Donchian 55/20 | buy | DOGE-USD | 2.85 | — | rebalance up |
| 2026-10-21T08:26 | Donchian 55/20 | sell | SOL-USD | 2.85 | -0.02 | rebalance down |
| 2026-10-21T08:25 | Volume breakout | buy | XRP-USD | 15.19 | — | entry |
| 2026-10-21T08:25 | Donchian 55/20 | buy | DOGE-USD | 8.49 | — | entry |
| 2026-10-21T08:25 | ROC + volume | buy | DOGE-USD | 15.17 | — | entry |
| 2026-10-21T08:25 | EMA 20/50 cross | buy | DOGE-USD | 5.49 | — | entry |
| 2026-10-21T08:20 | Volume breakout | sell | XRP-USD | 15.14 | -0.08 | exit signal |
| 2026-10-21T08:20 | Donchian 55/20 | buy | SOL-USD | 2.87 | — | rebalance up |
| 2026-10-21T08:20 | Donchian 55/20 | sell | DOGE-USD | 11.36 | -0.11 | stop-loss |
| 2026-10-21T08:20 | ROC + volume | sell | DOGE-USD | 15.16 | -0.14 | stop-loss |
| 2026-10-21T08:20 | EMA 20/50 cross | buy | ETH-USD | 8.28 | — | rebalance up |
| 2026-10-21T08:20 | EMA 20/50 cross | sell | DOGE-USD | 13.77 | -0.13 | stop-loss |
| 2026-10-21T08:00 | Connors RSI(2) · 1h | sell | ETH-USD | 22.31 | 0.02 | exit signal |
| 2026-10-21T08:00 | Connors RSI(2) · 1h | sell | DOGE-USD | 22.39 | 0.03 | exit signal |
| 2026-10-21T08:00 | Donchian 55/20 · 1h | buy | XRP-USD | 9.63 | — | entry signal |
| 2026-10-21T08:00 | Donchian 55/20 · 1h | sell | SOL-USD | 5.03 | 0.02 | rebalance down |
| 2026-10-21T08:00 | ROC + volume · 1h | buy | XRP-USD | 9.04 | — | entry signal |
| 2026-10-21T08:00 | VWAP momentum · 1h | buy | XRP-USD | 3.59 | — | entry signal |
| 2026-10-21T08:00 | VWAP momentum · 1h | buy | SOL-USD | 7.77 | — | entry signal |
| 2026-10-21T08:00 | VWAP momentum · 1h | buy | ETH-USD | 7.77 | — | entry signal |
| 2026-10-21T08:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.77 | — | entry signal |
| 2026-10-21T08:00 | VWAP momentum · 1h | buy | BTC-USD | 7.77 | — | entry signal |
| 2026-10-21T08:00 | MACD cross · 1h | buy | XRP-USD | 5.75 | — | entry signal |
| 2026-10-21T07:55 | ROC + volume | buy | ETH-USD | 15.30 | — | entry signal |
| 2026-10-21T07:50 | EMA 20/50 cross | buy | ETH-USD | 2.77 | — | rebalance up |
| 2026-10-21T07:50 | EMA 20/50 cross | sell | BTC-USD | 2.77 | -0.01 | rebalance down |
| 2026-10-21T07:45 | EMA 20/50 cross | buy | ETH-USD | 2.81 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 09:25:05.000109+00:00 -> 2026-10-21 09:35:05.000109+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
