# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T14:15:05.000138+00:00 · 33144 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.95 (-10.05%)

Closed trades 98, win rate 39.8%, fees £3.15, max drawdown -10.53%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSTR | 17.86 | -0.16 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 13797 decisions in 2199 calls, $0.1849 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T14:15 | 1 / 18 / 11 | cash |  |
| Breezy | 2026-10-23T14:15 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-23T14:15 | 6 / 22 / 2 | MSTR 59% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.05 | 7.05 | 0 | — | 8.61 | 4.62 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.52 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.90 | 0.90 | 0 | — | 3.60 | 1.69 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.73 | 0.73 | 83 | 43.4 | -11.65 | -3.27 | -13.74 | 153 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.73 | -1.27 | 72 | 33.3 | 5.26 | 2.57 | -2.25 | 102 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.81 | -2.19 | 0 | — | -0.67 | -0.36 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.58 | -3.42 | 118 | 31.4 | -1.84 | -1.07 | -6.22 | 193 |
| 14 | Hold BTC | benchmark | 96.44 | -3.56 | 0 | — | 1.50 | 0.43 | -8.68 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 17 | Copy: Congress Democrats (NANC) | copy | 95.36 | -4.64 | 0 | — | -1.14 | -0.43 | -5.87 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.87 | -5.13 | 0 | — | -6.12 | -2.61 | -7.32 | 1 |
| 19 | Gap and go | momentum | 94.19 | -5.81 | 91 | 22.0 | 4.99 | 1.67 | -8.69 | 183 |
| 20 | Copy: Insider buying | copy | 94.15 | -5.85 | 25 | 40.0 | -14.78 | -2.83 | -20.68 | 71 |
| 21 | Trend pullback · 1h | trend | 93.78 | -6.22 | 95 | 23.2 | -21.52 | -7.07 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.62 | -6.38 | 238 | 35.3 | -10.54 | -3.28 | -17.21 | 549 |
| 23 | Donchian 55/20 · 1h | breakout | 93.02 | -6.98 | 48 | 16.7 | -16.19 | -3.68 | -17.30 | 98 |
| 24 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -16.94 | -1.58 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 92.13 | -7.87 | 115 | 26.1 | -20.83 | -4.95 | -24.17 | 254 |
| 26 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 28 | ADX DI cross · 1h | trend | 91.13 | -8.87 | 107 | 18.7 | -11.68 | -2.40 | -14.21 | 255 |
| 29 | Daily: Momentum burst | daily | 90.91 | -9.09 | 10 | 10.0 | -18.38 | -3.57 | -20.52 | 40 |
| 30 | Agent | meta | 89.95 | -10.05 | 98 | 39.8 | -10.15 | -7.17 | -11.03 | 203 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 32 | Daily: Bullish score | daily | 89.19 | -10.81 | 9 | 0.0 | -8.32 | -1.09 | -14.40 | 14 |
| 33 | Bollinger breakout · 1h | breakout | 89.18 | -10.82 | 104 | 27.9 | -12.04 | -2.38 | -16.00 | 241 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.91 | -11.09 | 0 | — | -5.50 | -0.81 | -14.52 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -11.87 | -4.10 | -14.77 | 94 |
| 36 | Stochastic reversion · 1h | reversion | 87.48 | -12.52 | 185 | 45.4 | -20.08 | -3.80 | -22.47 | 382 |
| 37 | Opening range 15m | breakout | 86.40 | -13.60 | 302 | 30.5 | -15.81 | -4.62 | -17.87 | 696 |
| 38 | EMA 20/50 cross · 1h | trend | 86.39 | -13.61 | 71 | 11.3 | -22.57 | -4.52 | -24.84 | 137 |
| 39 | Keltner breakout · 1h | breakout | 86.19 | -13.81 | 73 | 23.3 | -22.79 | -4.85 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 86.19 | -13.81 | 105 | 15.2 | -23.57 | -4.98 | -26.14 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.78 | -14.22 | 98 | 16.3 | -21.22 | -4.56 | -22.81 | 216 |
| 42 | MACD cross · 1h | trend | 85.08 | -14.92 | 216 | 23.1 | -22.60 | -4.52 | -26.08 | 451 |
| 43 | Connors RSI(2) · 1h | reversion | 84.66 | -15.34 | 170 | 39.4 | -26.95 | -8.32 | -27.04 | 193 |
| 44 | Ichimoku · 1h | trend | 83.80 | -16.20 | 65 | 12.3 | -23.80 | -4.97 | -25.45 | 110 |
| 45 | Z-score reversion · 1h | reversion | 83.72 | -16.29 | 106 | 34.0 | -14.88 | -2.52 | -21.48 | 192 |
| 46 | Triple EMA stack · 1h | trend | 83.52 | -16.48 | 98 | 15.3 | -26.11 | -5.24 | -28.27 | 210 |
| 47 | MFI reversion · 1h | reversion | 82.26 | -17.73 | 256 | 31.6 | -17.33 | -2.83 | -20.54 | 141 |
| 48 | MACD zero-line · 1h | trend | 82.16 | -17.84 | 103 | 15.5 | -21.13 | -4.42 | -24.69 | 217 |
| 49 | Donchian 20/10 · 1h | breakout | 81.70 | -18.30 | 94 | 20.2 | -24.03 | -4.68 | -26.92 | 217 |
| 50 | OBV trend · 1h | momentum | 81.49 | -18.51 | 199 | 17.6 | -31.38 | -6.94 | -32.86 | 303 |
| 51 | Three white soldiers | momentum | 81.47 | -18.54 | 269 | 19.7 | -43.33 | -20.88 | -43.47 | 585 |
| 52 | Williams %R · 1h | reversion | 81.07 | -18.93 | 213 | 44.1 | -35.29 | -6.34 | -36.69 | 510 |
| 53 | CCI reversion · 1h | reversion | 80.51 | -19.49 | 198 | 42.9 | -26.14 | -3.93 | -28.17 | 434 |
| 54 | Bollinger reversion · 1h | reversion | 80.25 | -19.75 | 171 | 34.5 | -31.12 | -6.52 | -32.19 | 356 |
| 55 | Agent (ML meta-label) | meta | 79.94 | -20.06 | 839 | 18.8 | -12.74 | -2.49 | -15.60 | 377 |
| 56 | Heikin-Ashi · 1h | trend | 79.83 | -20.17 | 262 | 23.3 | -42.37 | -9.89 | -43.38 | 646 |
| 57 | ROC + volume · 1h | momentum | 79.00 | -21.00 | 236 | 24.2 | -30.35 | -6.08 | -31.40 | 378 |
| 58 | RSI(14) reversion · 1h | reversion | 77.96 | -22.04 | 91 | 23.1 | -14.98 | -2.77 | -23.51 | 184 |
| 59 | Candlestick reversal · 1h | reversion | 77.55 | -22.45 | 251 | 29.1 | -34.65 | -6.56 | -36.06 | 534 |
| 60 | EMA 9/21 cross · 1h | trend | 77.18 | -22.82 | 157 | 11.5 | -30.08 | -6.19 | -33.23 | 317 |
| 61 | VWAP momentum · 1h | momentum | 76.36 | -23.64 | 499 | 21.4 | -49.74 | -11.61 | -49.89 | 1194 |
| 62 | Max aggression: 1-day momentum | meta | 67.03 | -32.97 | 18 | 27.8 | -42.74 | -3.01 | -49.68 | 42 |
| 63 | ROC + volume | momentum | 57.95 | -42.05 | 700 | 22.9 | -74.80 | -27.45 | -74.81 | 1540 |
| 64 | Volume breakout | breakout | 57.15 | -42.85 | 417 | 13.2 | -60.51 | -26.14 | -60.51 | 757 |
| 65 | Donchian 55/20 | breakout | 54.29 | -45.71 | 556 | 19.4 | -70.91 | -24.02 | -71.05 | 1244 |
| 66 | Squeeze breakout | breakout | 53.87 | -46.13 | 544 | 14.2 | -66.07 | -28.86 | -66.12 | 1138 |
| 67 | EMA 20/50 cross | trend | 53.01 | -46.99 | 601 | 20.5 | -78.23 | -23.65 | -78.52 | 1389 |
| 68 | RSI(14) reversion | reversion | 52.97 | -47.03 | 811 | 26.0 | -76.51 | -19.75 | -76.67 | 1658 |
| 69 | VWAP reversion | reversion | 50.65 | -49.35 | 809 | 25.0 | -74.57 | -17.49 | -74.77 | 1540 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -45.09 | -98.65 | 4968 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -48.39 | -93.56 | 2479 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.31 | -30.29 | -88.42 | 1863 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.01 | -38.32 | -91.08 | 2286 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.11 | -31.35 | -90.15 | 2130 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.59 | -54.39 | -97.61 | 3403 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.87 | -62.72 | -95.88 | 3290 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -35.44 | -93.71 | 2419 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.43 | -36.46 | -82.48 | 1662 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -53.99 | -99.31 | 5612 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.09 | -42.07 | -92.14 | 2559 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.22 | -40.57 | -95.23 | 3339 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.86 | -99.74 | 6013 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.80 | -46.11 | -91.81 | 2279 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.44 | -66.62 | -97.45 | 3484 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.43 | -58.67 | -98.45 | 4661 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.08 | -60.07 | -94.10 | 2716 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.43 | -40.16 | -83.50 | 1762 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -65.11 | -99.52 | 6093 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.56 | -28.96 | -87.58 | 2162 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.95 | -38.11 | -90.05 | 2224 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -47.13 | -95.85 | 3707 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.15 | -49.47 | -89.25 | 2062 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.00 | -48.03 | -96.04 | 4075 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -111.78 | -99.90 | 8050 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T14:15 | Max aggression: 5-day momentum | sell | LABU | 92.92 | -9.83 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-23T14:15 | Day trade: Stocks in Play ORB | sell | UPRO | 24.66 | -0.05 | target is flat |
| 2026-10-23T14:15 | Day trade: Stocks in Play ORB | sell | SPY | 24.68 | -0.04 | target is flat |
| 2026-10-23T14:15 | Williams %R · 1h | buy | COIN | 4.18 | — | rebalance up |
| 2026-10-23T14:15 | Williams %R · 1h | sell | LABU | 16.15 | -0.27 | stop-loss |
| 2026-10-23T14:15 | VWAP reversion | buy | SQQQ | 12.66 | — | entry signal |
| 2026-10-23T14:15 | Volume breakout | sell | ETH-USD | 14.20 | -0.16 | stop-loss |
| 2026-10-23T14:15 | Squeeze breakout | buy | TECL | 10.74 | — | rebalance up |
| 2026-10-23T14:15 | Squeeze breakout | sell | SOL-USD | 13.41 | -0.15 | stop-loss |
| 2026-10-23T14:15 | Squeeze breakout | sell | ETH-USD | 13.43 | -0.15 | stop-loss |
| 2026-10-23T14:15 | Squeeze breakout | sell | BTC-USD | 13.44 | -0.13 | stop-loss |
| 2026-10-23T14:15 | Opening range 30m | buy | MSFT | 23.41 | — | entry signal |
| 2026-10-23T14:15 | Donchian 55/20 | buy | SOL-USD | 4.53 | — | rebalance up |
| 2026-10-23T14:15 | Donchian 55/20 | buy | MSTR | 4.54 | — | rebalance up |
| 2026-10-23T14:15 | Donchian 55/20 | sell | ETHU | 9.03 | -0.11 | stop-loss |
| 2026-10-23T14:15 | Donchian 55/20 | sell | ETH-USD | 9.04 | -0.10 | stop-loss |
| 2026-10-23T14:15 | Donchian 55/20 | sell | BTC-USD | 9.07 | -0.08 | stop-loss |
| 2026-10-23T14:15 | Donchian 55/20 | sell | BITX | 9.05 | -0.08 | stop-loss |
| 2026-10-23T14:15 | Gap and go | sell | ETHU | 23.33 | -0.29 | stop-loss |
| 2026-10-23T14:15 | ROC + volume | sell | SOL-USD | 14.41 | -0.16 | stop-loss |
| 2026-10-23T14:15 | ROC + volume | sell | BITX | 14.41 | -0.14 | stop-loss |
| 2026-10-23T14:15 | EMA 20/50 cross | buy | SOL-USD | 4.39 | — | rebalance up |
| 2026-10-23T14:15 | EMA 20/50 cross | buy | MSTR | 4.47 | — | rebalance up |
| 2026-10-23T14:15 | EMA 20/50 cross | buy | ETH-USD | 4.39 | — | rebalance up |
| 2026-10-23T14:15 | EMA 20/50 cross | sell | ETHU | 8.77 | -0.11 | stop-loss |
| 2026-10-23T14:15 | EMA 20/50 cross | sell | BTC-USD | 8.86 | -0.08 | stop-loss |
| 2026-10-23T14:15 | EMA 20/50 cross | sell | BITX | 8.84 | -0.09 | stop-loss |
| 2026-10-23T14:10 | OBV trend · 1h | buy | IWM | 20.39 | — | entry |
| 2026-10-23T14:10 | VWAP reversion | buy | AAPL | 12.67 | — | entry signal |
| 2026-10-23T14:10 | RSI(14) reversion | buy | TSLA | 6.20 | — | rebalance up |
| 2026-10-23T14:10 | RSI(14) reversion | sell | MSFT | 8.00 | 0.04 | exit signal |
| 2026-10-23T14:10 | Three white soldiers | buy | TSLA | 20.36 | — | entry signal |
| 2026-10-23T14:10 | Volume breakout | sell | BTC-USD | 14.25 | -0.11 | exit signal |
| 2026-10-23T14:05 | Squeeze breakout | buy | TECL | 2.76 | — | entry signal |
| 2026-10-23T14:05 | Squeeze breakout | sell | QQQ | 2.71 | -0.00 | rebalance down |
| 2026-10-23T14:05 | Opening range 30m | buy | TECL | 23.44 | — | entry signal |
| 2026-10-23T14:05 | Opening range 30m | buy | PLTR | 23.44 | — | entry signal |
| 2026-10-23T14:05 | Opening range 30m | buy | GOOGL | 23.44 | — | entry signal |
| 2026-10-23T14:00 | MFI reversion · 1h | sell | META | 20.79 | 0.29 | target is flat |
| 2026-10-23T14:00 | CCI reversion · 1h | buy | XRP-USD | 13.76 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 14:15:05.000138+00:00 -> 2026-10-23 14:25:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
