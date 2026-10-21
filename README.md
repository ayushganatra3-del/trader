# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T01:55:05.000113+00:00 · 30171 ticks

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

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 17.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 1380 decisions in 276 calls, $0.0193 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T01:55 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-21T01:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T01:55 | 1 / 4 / 0 | ETH-USD 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.77 | +3.00% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.10 | 6.09 | 0 | — | 8.23 | 3.84 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 100.73 | 0.73 | 9 | 44.4 | -13.29 | -0.93 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.01 | -0.99 | 0 | — | 0.33 | 0.23 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.70 | -1.30 | 62 | 35.5 | 4.20 | 2.21 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.50 | -1.50 | 0 | — | -0.73 | -0.22 | -5.15 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 13 | Hold BTC | benchmark | 98.20 | -1.80 | 0 | — | 19.46 | 2.61 | -8.68 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.08 | -1.92 | 3 | 33.3 | 4.26 | 0.99 | -7.93 | 8 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.83 | -2.16 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.97 | -3.03 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.83 | -3.17 | 0 | — | 0.02 | 0.07 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.55 | -3.45 | 40 | 15.0 | -14.24 | -2.85 | -15.92 | 99 |
| 19 | Copy: Insider buying | copy | 96.16 | -3.84 | 25 | 40.0 | -11.99 | -2.06 | -20.62 | 72 |
| 20 | Agent (rotation) | meta | 96.09 | -3.91 | 114 | 31.6 | -6.34 | -3.12 | -8.16 | 302 |
| 21 | Trend pullback · 1h | trend | 95.71 | -4.29 | 90 | 23.3 | -20.34 | -6.15 | -20.85 | 131 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.62 | -5.38 | 89 | 18.0 | -13.78 | -2.60 | -16.12 | 253 |
| 24 | Daily: Momentum burst | daily | 94.14 | -5.86 | 6 | 16.7 | -6.94 | -0.92 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.71 | 1.50 | -6.51 | 196 |
| 26 | Parabolic SAR · 1h | trend | 92.25 | -7.75 | 105 | 21.9 | -17.57 | -3.76 | -20.69 | 271 |
| 27 | Opening range 30m | breakout | 92.11 | -7.89 | 225 | 32.4 | -13.40 | -3.91 | -17.26 | 565 |
| 28 | Squeeze breakout · 1h | breakout | 91.95 | -8.05 | 46 | 21.7 | -2.65 | -0.57 | -11.48 | 97 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.25 | -2.32 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 91.15 | -8.85 | 7 | 0.0 | -7.95 | -0.90 | -13.10 | 13 |
| 31 | Agent | meta | 90.86 | -9.14 | 90 | 41.1 | -11.72 | -6.16 | -17.16 | 232 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.82 | -9.18 | 0 | — | 0.92 | 0.30 | -14.37 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.78 | -9.22 | 84 | 22.6 | -12.60 | -2.25 | -14.09 | 104 |
| 34 | Bollinger breakout · 1h | breakout | 90.65 | -9.35 | 87 | 29.9 | -12.70 | -2.38 | -16.36 | 258 |
| 35 | RSI momentum · 1h | momentum | 89.51 | -10.49 | 83 | 15.7 | -24.29 | -4.72 | -25.28 | 217 |
| 36 | Connors RSI(2) · 1h | reversion | 89.43 | -10.56 | 151 | 41.7 | -22.17 | -6.60 | -23.77 | 196 |
| 37 | EMA 20/50 cross · 1h | trend | 88.80 | -11.20 | 62 | 12.9 | -19.02 | -3.49 | -21.45 | 132 |
| 38 | Supertrend · 1h | trend | 88.35 | -11.65 | 88 | 12.5 | -19.94 | -3.71 | -28.15 | 223 |
| 39 | Opening range 15m | breakout | 88.26 | -11.74 | 270 | 29.3 | -17.73 | -4.78 | -20.79 | 699 |
| 40 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -13.32 | -3.85 | -16.44 | 123 |
| 41 | Stochastic reversion · 1h | reversion | 87.79 | -12.21 | 164 | 47.0 | -14.70 | -2.45 | -22.24 | 362 |
| 42 | Keltner breakout · 1h | breakout | 87.39 | -12.61 | 60 | 21.7 | -18.04 | -3.12 | -26.64 | 207 |
| 43 | Ichimoku · 1h | trend | 86.95 | -13.04 | 60 | 13.3 | -18.97 | -3.58 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.39 | -13.61 | 193 | 20.2 | -25.69 | -4.81 | -33.71 | 466 |
| 45 | Triple EMA stack · 1h | trend | 85.55 | -14.45 | 91 | 14.3 | -31.92 | -5.92 | -32.16 | 229 |
| 46 | Donchian 20/10 · 1h | breakout | 84.81 | -15.20 | 81 | 17.3 | -18.12 | -3.00 | -28.55 | 220 |
| 47 | Z-score reversion · 1h | reversion | 84.53 | -15.47 | 96 | 30.2 | -14.30 | -2.35 | -21.32 | 195 |
| 48 | OBV trend · 1h | momentum | 84.09 | -15.91 | 186 | 17.2 | -34.21 | -6.05 | -36.91 | 316 |
| 49 | MFI reversion · 1h | reversion | 83.98 | -16.02 | 220 | 30.5 | -14.90 | -2.34 | -20.43 | 140 |
| 50 | MACD zero-line · 1h | trend | 83.81 | -16.19 | 89 | 14.6 | -25.35 | -4.99 | -26.48 | 226 |
| 51 | Agent (ML meta-label) | meta | 83.69 | -16.31 | 711 | 19.1 | -6.51 | -1.02 | -15.69 | 362 |
| 52 | Three white soldiers | momentum | 82.36 | -17.64 | 252 | 19.4 | -47.00 | -18.36 | -47.63 | 616 |
| 53 | Bollinger reversion · 1h | reversion | 82.23 | -17.77 | 162 | 35.8 | -29.42 | -5.70 | -32.84 | 347 |
| 54 | ROC + volume · 1h | momentum | 81.61 | -18.39 | 203 | 21.2 | -29.12 | -5.38 | -34.11 | 392 |
| 55 | Williams %R · 1h | reversion | 81.40 | -18.60 | 195 | 43.6 | -30.71 | -4.75 | -36.49 | 524 |
| 56 | CCI reversion · 1h | reversion | 80.76 | -19.24 | 178 | 41.6 | -18.25 | -2.28 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.22 | -19.78 | 232 | 20.7 | -43.93 | -9.38 | -47.30 | 674 |
| 58 | EMA 9/21 cross · 1h | trend | 79.69 | -20.31 | 143 | 10.5 | -29.26 | -6.09 | -30.12 | 326 |
| 59 | RSI(14) reversion · 1h | reversion | 79.60 | -20.40 | 83 | 22.9 | -15.38 | -2.71 | -23.28 | 184 |
| 60 | VWAP momentum · 1h | momentum | 77.89 | -22.11 | 464 | 20.0 | -45.25 | -8.13 | -50.19 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 77.41 | -22.59 | 226 | 28.8 | -37.05 | -6.85 | -38.89 | 543 |
| 62 | Max aggression: 1-day momentum | meta | 77.11 | -22.89 | 17 | 29.4 | -27.91 | -1.54 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 61.21 | -38.79 | 632 | 22.9 | -77.55 | -21.62 | -78.40 | 1722 |
| 64 | Volume breakout | breakout | 61.06 | -38.94 | 381 | 13.9 | -63.71 | -19.61 | -64.10 | 867 |
| 65 | Squeeze breakout | breakout | 58.26 | -41.73 | 493 | 14.0 | -66.00 | -22.17 | -66.75 | 1203 |
| 66 | Donchian 55/20 | breakout | 57.55 | -42.45 | 506 | 19.2 | -70.65 | -17.52 | -73.50 | 1280 |
| 67 | RSI(14) reversion | reversion | 57.37 | -42.63 | 745 | 26.6 | -74.12 | -16.19 | -74.89 | 1623 |
| 68 | EMA 20/50 cross | trend | 55.95 | -44.05 | 551 | 19.4 | -77.18 | -16.17 | -80.87 | 1446 |
| 69 | VWAP reversion | reversion | 53.63 | -46.37 | 754 | 25.2 | -71.58 | -14.58 | -72.28 | 1494 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -29.98 | -98.76 | 5269 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -30.75 | -94.00 | 2598 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.72 | -20.41 | -88.38 | 1901 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.34 | -24.45 | -91.44 | 2359 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.14 | -26.09 | -91.32 | 2255 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.55 | -32.92 | -97.69 | 3525 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.75 | -37.16 | -96.83 | 3604 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -28.31 | -94.59 | 2540 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.52 | -27.43 | -82.85 | 1710 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.86 | -99.37 | 5739 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.71 | -27.35 | -92.41 | 2626 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.95 | -31.50 | -95.95 | 3464 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -41.13 | -99.75 | 6192 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.62 | -29.25 | -91.66 | 2357 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -38.46 | -97.71 | 3619 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -35.92 | -98.46 | 4711 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.06 | -35.02 | -94.19 | 2803 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.19 | -27.54 | -83.91 | 1805 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.32 | -99.52 | 6189 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.64 | -22.06 | -87.01 | 2142 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.78 | -26.00 | -88.12 | 2141 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.29 | -95.95 | 3763 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.99 | -31.86 | -89.41 | 2113 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.63 | -32.54 | -95.77 | 4106 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.75 | -99.91 | 8295 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T01:50 | Volume breakout | buy | XRP-USD | 15.28 | — | entry signal |
| 2026-10-21T01:45 | OBV trend · 1h | sell | SOL-USD | 4.76 | -0.01 | rebalance down |
| 2026-10-21T01:45 | OBV trend · 1h | sell | BTC-USD | 4.80 | -0.02 | rebalance down |
| 2026-10-21T01:10 | Squeeze breakout | sell | DOGE-USD | 14.46 | -0.14 | stop-loss |
| 2026-10-21T01:10 | Donchian 55/20 | sell | BTC-USD | 14.33 | -0.11 | stop-loss |
| 2026-10-21T01:00 | VWAP momentum · 1h | sell | BTC-USD | 8.65 | 0.03 | exit signal |
| 2026-10-21T01:00 | Volume breakout | sell | ETH-USD | 15.19 | -0.12 | exit signal |
| 2026-10-21T00:55 | Volume breakout | buy | ETH-USD | 15.31 | — | entry signal |
| 2026-10-21T00:46 | Squeeze breakout | buy | DOGE-USD | 14.60 | — | entry signal |
| 2026-10-20T23:30 | Donchian 55/20 | sell | SOL-USD | 14.33 | -0.14 | exit signal |
| 2026-10-20T23:10 | Squeeze breakout | sell | DOGE-USD | 14.49 | -0.15 | stop-loss |
| 2026-10-20T23:10 | Donchian 55/20 | buy | BTC-USD | 8.62 | — | rebalance up |
| 2026-10-20T23:10 | Donchian 55/20 | sell | ETH-USD | 14.31 | -0.13 | stop-loss |
| 2026-10-20T23:10 | ROC + volume | sell | DOGE-USD | 15.25 | -0.16 | stop-loss |
| 2026-10-20T23:05 | Keltner breakout | sell | DOGE-USD | 12.45 | -0.12 | Kill switch: down 50% from peak |
| 2026-10-20T23:05 | Keltner breakout | sell | BTC-USD | 12.53 | -0.05 | Kill switch: down 50% from peak |
| 2026-10-20T23:05 | ROC + volume | sell | SOL-USD | 15.35 | -0.07 | stop-loss |
| 2026-10-20T23:00 | Volume breakout | sell | DOGE-USD | 15.21 | -0.14 | exit signal |
| 2026-10-20T23:00 | Keltner breakout | sell | ETH-USD | 12.53 | -0.06 | exit signal |
| 2026-10-20T22:45 | Keltner breakout | sell | XRP-USD | 12.41 | -0.13 | stop-loss |
| 2026-10-20T22:45 | ROC + volume | sell | XRP-USD | 15.25 | -0.16 | stop-loss |
| 2026-10-20T22:40 | Volume breakout | buy | DOGE-USD | 15.34 | — | entry signal |
| 2026-10-20T22:40 | Squeeze breakout | buy | DOGE-USD | 14.64 | — | entry signal |
| 2026-10-20T22:40 | Keltner breakout | buy | XRP-USD | 12.54 | — | entry signal |
| 2026-10-20T22:40 | Keltner breakout | buy | DOGE-USD | 12.56 | — | entry signal |
| 2026-10-20T22:40 | ROC + volume | buy | XRP-USD | 15.41 | — | entry signal |
| 2026-10-20T22:40 | ROC + volume | buy | DOGE-USD | 15.41 | — | entry signal |
| 2026-10-20T22:05 | Donchian 55/20 | buy | BTC-USD | 5.81 | — | entry signal |
| 2026-10-20T22:05 | Donchian 55/20 | sell | XRP-USD | 2.88 | -0.01 | rebalance down |
| 2026-10-20T22:05 | Donchian 55/20 | sell | DOGE-USD | 2.90 | -0.01 | rebalance down |
| 2026-10-20T22:01 | Heikin-Ashi · 1h | buy | DOGE-USD | 7.94 | — | entry signal |
| 2026-10-20T22:01 | Donchian 55/20 | buy | ETH-USD | 14.44 | — | entry signal |
| 2026-10-20T21:35 | Volume breakout | sell | BTC-USD | 15.28 | -0.11 | exit signal |
| 2026-10-20T21:35 | Squeeze breakout | sell | DOGE-USD | 14.58 | -0.08 | exit signal |
| 2026-10-20T21:35 | Keltner breakout | sell | DOGE-USD | 12.52 | -0.07 | exit signal |
| 2026-10-20T21:35 | ROC + volume | sell | DOGE-USD | 15.33 | -0.08 | exit signal |
| 2026-10-20T21:25 | Three white soldiers | sell | XRP-USD | 20.53 | -0.12 | exit signal |
| 2026-10-20T21:25 | Three white soldiers | sell | SOL-USD | 20.55 | -0.10 | exit signal |
| 2026-10-20T21:25 | Volume breakout | sell | SOL-USD | 15.29 | -0.10 | exit signal |
| 2026-10-20T21:20 | Volume breakout | buy | BTC-USD | 15.39 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 01:55:05.000113+00:00 -> 2026-10-21 02:05:05.000113+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
