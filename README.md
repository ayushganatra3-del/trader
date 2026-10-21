# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T05:55:05.000192+00:00 · 30378 ticks

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

Today: 4485 decisions in 897 calls, $0.0627 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T05:55 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-21T05:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T05:55 | 1 / 4 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.11 | 6.11 | 0 | — | 8.23 | 3.84 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 100.74 | 0.74 | 9 | 44.4 | -13.29 | -0.93 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.01 | -0.98 | 0 | — | 0.33 | 0.23 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.70 | -1.30 | 62 | 35.5 | 4.19 | 2.20 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.51 | -1.49 | 0 | — | -0.73 | -0.22 | -5.15 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.09 | -1.91 | 3 | 33.3 | 4.26 | 0.99 | -7.93 | 8 |
| 14 | Hold BTC | benchmark | 97.71 | -2.29 | 0 | — | 17.91 | 2.45 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.83 | -2.16 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.98 | -3.02 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.84 | -3.16 | 0 | — | 0.02 | 0.07 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.20 | -3.80 | 40 | 15.0 | -14.58 | -2.93 | -15.92 | 99 |
| 19 | Copy: Insider buying | copy | 96.16 | -3.84 | 25 | 40.0 | -11.99 | -2.06 | -20.62 | 72 |
| 20 | Agent (rotation) | meta | 96.09 | -3.91 | 114 | 31.6 | -6.34 | -3.12 | -8.16 | 302 |
| 21 | Trend pullback · 1h | trend | 95.71 | -4.29 | 90 | 23.3 | -20.37 | -6.16 | -20.85 | 131 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.63 | -5.37 | 89 | 18.0 | -13.82 | -2.61 | -16.12 | 253 |
| 24 | Daily: Momentum burst | daily | 94.15 | -5.85 | 6 | 16.7 | -6.94 | -0.92 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.71 | 1.50 | -6.51 | 196 |
| 26 | Opening range 30m | breakout | 92.11 | -7.89 | 225 | 32.4 | -13.40 | -3.91 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.75 | -8.25 | 105 | 21.9 | -17.89 | -3.84 | -20.69 | 271 |
| 28 | Squeeze breakout · 1h | breakout | 91.63 | -8.37 | 46 | 21.7 | -3.00 | -0.65 | -11.48 | 97 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.25 | -2.32 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 91.16 | -8.84 | 7 | 0.0 | -7.95 | -0.90 | -13.10 | 13 |
| 31 | Agent | meta | 90.86 | -9.14 | 90 | 41.1 | -15.66 | -5.48 | -19.30 | 276 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.83 | -9.17 | 0 | — | 0.92 | 0.30 | -14.37 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.65 | -9.35 | 85 | 22.4 | -12.73 | -2.28 | -14.09 | 104 |
| 34 | Bollinger breakout · 1h | breakout | 90.59 | -9.41 | 87 | 29.9 | -12.79 | -2.40 | -16.36 | 258 |
| 35 | RSI momentum · 1h | momentum | 89.26 | -10.74 | 83 | 15.7 | -24.56 | -4.78 | -25.37 | 218 |
| 36 | Connors RSI(2) · 1h | reversion | 89.24 | -10.76 | 151 | 41.7 | -22.36 | -6.68 | -23.77 | 198 |
| 37 | EMA 20/50 cross · 1h | trend | 88.61 | -11.39 | 62 | 12.9 | -19.21 | -3.54 | -21.41 | 132 |
| 38 | Opening range 15m | breakout | 88.26 | -11.74 | 270 | 29.3 | -17.73 | -4.78 | -20.79 | 699 |
| 39 | Supertrend · 1h | trend | 88.16 | -11.84 | 88 | 12.5 | -20.11 | -3.75 | -28.15 | 223 |
| 40 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -15.09 | -4.04 | -18.93 | 134 |
| 41 | Stochastic reversion · 1h | reversion | 87.80 | -12.20 | 164 | 47.0 | -14.69 | -2.45 | -22.24 | 362 |
| 42 | Keltner breakout · 1h | breakout | 87.33 | -12.67 | 60 | 21.7 | -19.23 | -3.48 | -26.64 | 205 |
| 43 | Ichimoku · 1h | trend | 86.87 | -13.13 | 60 | 13.3 | -19.07 | -3.60 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.25 | -13.75 | 196 | 20.9 | -26.15 | -4.94 | -33.71 | 467 |
| 45 | Triple EMA stack · 1h | trend | 85.30 | -14.70 | 91 | 14.3 | -30.60 | -5.69 | -31.81 | 228 |
| 46 | Donchian 20/10 · 1h | breakout | 84.64 | -15.36 | 81 | 17.3 | -19.05 | -3.29 | -28.55 | 220 |
| 47 | Z-score reversion · 1h | reversion | 84.54 | -15.46 | 96 | 30.2 | -14.30 | -2.35 | -21.32 | 195 |
| 48 | MFI reversion · 1h | reversion | 83.85 | -16.15 | 220 | 30.5 | -15.08 | -2.37 | -20.43 | 140 |
| 49 | OBV trend · 1h | momentum | 83.79 | -16.21 | 186 | 17.2 | -34.95 | -6.21 | -35.49 | 315 |
| 50 | Agent (ML meta-label) | meta | 83.69 | -16.31 | 711 | 19.1 | -9.34 | -1.57 | -15.13 | 356 |
| 51 | MACD zero-line · 1h | trend | 83.58 | -16.42 | 91 | 15.4 | -25.52 | -5.03 | -26.48 | 226 |
| 52 | Three white soldiers | momentum | 82.36 | -17.64 | 252 | 19.4 | -46.80 | -18.32 | -47.43 | 612 |
| 53 | Bollinger reversion · 1h | reversion | 82.23 | -17.77 | 162 | 35.8 | -29.42 | -5.70 | -32.84 | 347 |
| 54 | Williams %R · 1h | reversion | 81.41 | -18.59 | 195 | 43.6 | -30.71 | -4.75 | -36.50 | 524 |
| 55 | ROC + volume · 1h | momentum | 81.39 | -18.61 | 208 | 22.6 | -29.33 | -5.44 | -34.03 | 390 |
| 56 | CCI reversion · 1h | reversion | 80.77 | -19.23 | 178 | 41.6 | -18.25 | -2.28 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.18 | -19.82 | 233 | 20.6 | -43.42 | -9.26 | -47.30 | 670 |
| 58 | RSI(14) reversion · 1h | reversion | 79.60 | -20.39 | 83 | 22.9 | -15.38 | -2.71 | -23.28 | 184 |
| 59 | EMA 9/21 cross · 1h | trend | 79.57 | -20.43 | 143 | 10.5 | -29.36 | -6.12 | -30.12 | 326 |
| 60 | VWAP momentum · 1h | momentum | 77.71 | -22.29 | 467 | 20.6 | -45.42 | -8.18 | -50.19 | 1255 |
| 61 | Candlestick reversal · 1h | reversion | 77.42 | -22.58 | 226 | 28.8 | -36.77 | -6.72 | -38.97 | 542 |
| 62 | Max aggression: 1-day momentum | meta | 77.11 | -22.89 | 17 | 29.4 | -27.91 | -1.54 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 61.21 | -38.79 | 632 | 22.9 | -77.42 | -21.51 | -78.41 | 1715 |
| 64 | Volume breakout | breakout | 60.89 | -39.11 | 383 | 13.8 | -63.72 | -19.64 | -64.20 | 866 |
| 65 | Squeeze breakout | breakout | 57.90 | -42.10 | 496 | 13.9 | -66.23 | -22.47 | -67.01 | 1206 |
| 66 | RSI(14) reversion | reversion | 57.37 | -42.63 | 745 | 26.6 | -74.13 | -16.21 | -74.89 | 1619 |
| 67 | Donchian 55/20 | breakout | 57.35 | -42.65 | 508 | 19.1 | -71.21 | -18.20 | -73.51 | 1276 |
| 68 | EMA 20/50 cross | trend | 55.49 | -44.51 | 555 | 19.6 | -78.02 | -17.08 | -80.87 | 1441 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 754 | 25.2 | -71.48 | -14.50 | -72.31 | 1492 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.73 | -30.38 | -98.78 | 5275 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -32.40 | -94.06 | 2598 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.42 | -21.93 | -88.50 | 1896 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.79 | -26.03 | -91.54 | 2360 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.16 | -26.03 | -91.40 | 2251 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -34.26 | -97.73 | 3522 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.86 | -38.13 | -96.89 | 3610 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.41 | -28.03 | -94.50 | 2536 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.76 | -27.82 | -82.99 | 1707 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.28 | -99.38 | 5747 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.77 | -27.48 | -92.49 | 2624 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.95 | -31.43 | -95.95 | 3462 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -41.69 | -99.75 | 6184 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.63 | -29.38 | -91.76 | 2354 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -39.22 | -97.74 | 3612 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.24 | -98.47 | 4712 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.12 | -35.41 | -94.27 | 2801 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.13 | -27.45 | -83.94 | 1800 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.58 | -99.52 | 6189 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.75 | -22.25 | -87.01 | 2147 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.71 | -26.08 | -88.03 | 2138 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -32.49 | -95.94 | 3766 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -33.58 | -89.36 | 2107 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.66 | -32.82 | -95.77 | 4108 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.97 | -99.91 | 8286 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T05:55 | Squeeze breakout | sell | XRP-USD | 14.43 | -0.11 | stop-loss |
| 2026-10-21T05:50 | VWAP reversion | buy | ETH-USD | 13.39 | — | entry signal |
| 2026-10-21T05:45 | Volume breakout | sell | XRP-USD | 15.15 | -0.10 | exit signal |
| 2026-10-21T05:45 | Squeeze breakout | sell | DOGE-USD | 14.44 | -0.12 | stop-loss |
| 2026-10-21T05:45 | Squeeze breakout | sell | BTC-USD | 14.44 | -0.12 | stop-loss |
| 2026-10-21T05:25 | EMA 20/50 cross | buy | XRP-USD | 13.89 | — | entry signal |
| 2026-10-21T05:15 | Squeeze breakout | buy | XRP-USD | 14.54 | — | entry signal |
| 2026-10-21T05:10 | Volume breakout | buy | XRP-USD | 15.25 | — | entry signal |
| 2026-10-21T05:10 | Squeeze breakout | buy | DOGE-USD | 14.57 | — | entry signal |
| 2026-10-21T05:10 | Squeeze breakout | buy | BTC-USD | 14.57 | — | entry signal |
| 2026-10-21T05:00 | MACD zero-line · 1h | sell | DOGE-USD | 14.04 | 0.17 | exit signal |
| 2026-10-21T05:00 | MACD zero-line · 1h | sell | BTC-USD | 13.98 | -0.15 | exit signal |
| 2026-10-21T05:00 | MACD cross · 1h | buy | XRP-USD | 5.75 | — | entry |
| 2026-10-21T05:00 | MACD cross · 1h | sell | ETH-USD | 5.05 | -0.04 | exit signal |
| 2026-10-21T05:00 | MACD cross · 1h | sell | DOGE-USD | 5.10 | 0.06 | exit signal |
| 2026-10-21T05:00 | MACD cross · 1h | sell | BTC-USD | 5.05 | 0.01 | exit signal |
| 2026-10-21T04:00 | Connors RSI(2) · 1h | buy | SOL-USD | 4.60 | — | entry signal |
| 2026-10-21T04:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 17.87 | — | entry signal |
| 2026-10-21T03:25 | VWAP reversion | buy | SOL-USD | 13.41 | — | entry signal |
| 2026-10-21T03:20 | Donchian 55/20 | sell | XRP-USD | 11.50 | -0.07 | exit signal |
| 2026-10-21T03:05 | EMA 20/50 cross | sell | XRP-USD | 11.20 | 0.13 | exit signal |
| 2026-10-21T03:00 | Connors RSI(2) · 1h | buy | BTC-USD | 22.36 | — | entry signal |
| 2026-10-21T03:00 | Volume breakout · 1h | sell | BTC-USD | 22.70 | -0.12 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | XRP-USD | 6.29 | 0.04 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | SOL-USD | 6.27 | 0.02 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | ETH-USD | 6.27 | 0.02 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | DOGE-USD | 6.28 | 0.03 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | BTC-USD | 5.81 | -0.00 | exit signal |
| 2026-10-21T03:00 | VWAP momentum · 1h | sell | XRP-USD | 8.68 | 0.10 | exit signal |
| 2026-10-21T03:00 | VWAP momentum · 1h | sell | ETH-USD | 8.66 | 0.05 | exit signal |
| 2026-10-21T03:00 | VWAP momentum · 1h | sell | DOGE-USD | 8.67 | 0.08 | exit signal |
| 2026-10-21T03:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 7.90 | -0.05 | exit signal |
| 2026-10-21T02:45 | EMA 20/50 cross | sell | ETH-USD | 13.88 | -0.05 | exit signal |
| 2026-10-21T02:25 | EMA 20/50 cross | sell | BTC-USD | 13.91 | -0.01 | exit signal |
| 2026-10-21T02:20 | EMA 20/50 cross | sell | SOL-USD | 13.86 | -0.05 | exit signal |
| 2026-10-21T02:15 | Donchian 55/20 | sell | DOGE-USD | 11.50 | -0.06 | exit signal |
| 2026-10-21T02:05 | Volume breakout | sell | XRP-USD | 15.15 | -0.13 | exit signal |
| 2026-10-21T01:50 | Volume breakout | buy | XRP-USD | 15.28 | — | entry signal |
| 2026-10-21T01:45 | OBV trend · 1h | sell | SOL-USD | 4.76 | -0.01 | rebalance down |
| 2026-10-21T01:45 | OBV trend · 1h | sell | BTC-USD | 4.80 | -0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 05:55:05.000192+00:00 -> 2026-10-21 06:05:05.000192+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
