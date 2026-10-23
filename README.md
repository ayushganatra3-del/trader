# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T09:45:05.000187+00:00 · 32923 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.11 (-9.89%)

Closed trades 98, win rate 39.8%, fees £3.14, max drawdown -10.53%.

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

Today: 7680 decisions in 1536 calls, $0.1072 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T09:45 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-10-23T09:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T09:45 | 3 / 2 / 0 | ETH-USD 59% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.37 | 7.37 | 0 | — | 8.89 | 4.77 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.52 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.35 | 2.02 | -5.17 | 42 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.97 | 0.97 | 0 | — | 3.62 | 1.70 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.40 | 0.40 | 82 | 43.9 | -11.80 | -3.31 | -13.74 | 153 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.48 | -0.52 | 10 | 50.0 | -11.15 | -0.95 | -27.80 | 24 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 5.35 | 2.62 | -2.17 | 100 |
| 11 | Hold SPY | benchmark | 98.34 | -1.66 | 0 | — | -0.19 | -0.06 | -3.13 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.60 | -3.40 | 118 | 31.4 | -1.83 | -1.07 | -6.22 | 193 |
| 15 | Hold BTC | benchmark | 96.50 | -3.50 | 0 | — | 1.52 | 0.43 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.93 | -4.07 | 0 | — | -0.61 | -0.20 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 95.58 | -4.42 | 0 | — | -5.46 | -2.33 | -7.04 | 1 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 5.31 | 1.77 | -8.69 | 182 |
| 21 | Copy: Insider buying | copy | 94.41 | -5.59 | 25 | 40.0 | -14.57 | -2.78 | -20.68 | 71 |
| 22 | Trend pullback · 1h | trend | 93.79 | -6.21 | 95 | 23.2 | -21.51 | -7.07 | -21.85 | 115 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -10.42 | -3.24 | -17.21 | 545 |
| 24 | Parabolic SAR · 1h | trend | 93.10 | -6.90 | 115 | 26.1 | -20.04 | -4.74 | -24.17 | 254 |
| 25 | Donchian 55/20 · 1h | breakout | 93.08 | -6.92 | 48 | 16.7 | -16.15 | -3.66 | -17.30 | 98 |
| 26 | Daily: Momentum burst | daily | 92.70 | -7.30 | 8 | 12.5 | -16.72 | -3.23 | -19.90 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.23 | -7.77 | 104 | 19.2 | -10.58 | -2.17 | -13.49 | 255 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -9.99 | -7.04 | -11.03 | 202 |
| 31 | Daily: Bullish score | daily | 89.86 | -10.14 | 8 | 0.0 | -7.63 | -0.98 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.30 | -10.70 | 104 | 27.9 | -11.95 | -2.36 | -15.96 | 241 |
| 33 | Volume breakout · 1h | breakout | 89.16 | -10.84 | 101 | 22.8 | -12.79 | -2.71 | -15.92 | 110 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 89.08 | -10.92 | 0 | — | -5.36 | -0.78 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -11.87 | -4.10 | -14.77 | 94 |
| 36 | EMA 20/50 cross · 1h | trend | 87.68 | -12.32 | 68 | 11.8 | -21.45 | -4.27 | -24.06 | 137 |
| 37 | Stochastic reversion · 1h | reversion | 87.41 | -12.59 | 183 | 45.9 | -19.79 | -3.73 | -22.47 | 382 |
| 38 | Supertrend · 1h | trend | 86.94 | -13.06 | 104 | 15.4 | -22.93 | -4.83 | -25.65 | 212 |
| 39 | RSI momentum · 1h | momentum | 86.66 | -13.34 | 96 | 16.7 | -20.40 | -4.37 | -22.08 | 216 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.69 | -4.58 | -17.87 | 683 |
| 41 | Keltner breakout · 1h | breakout | 86.25 | -13.75 | 73 | 23.3 | -22.74 | -4.84 | -24.32 | 190 |
| 42 | Connors RSI(2) · 1h | reversion | 85.13 | -14.87 | 168 | 39.9 | -26.56 | -8.16 | -26.65 | 193 |
| 43 | MACD cross · 1h | trend | 85.07 | -14.93 | 216 | 23.1 | -22.54 | -4.50 | -26.08 | 451 |
| 44 | Triple EMA stack · 1h | trend | 84.49 | -15.51 | 96 | 15.6 | -25.06 | -4.99 | -27.76 | 210 |
| 45 | Ichimoku · 1h | trend | 83.86 | -16.14 | 65 | 12.3 | -23.76 | -4.96 | -25.41 | 110 |
| 46 | Z-score reversion · 1h | reversion | 83.39 | -16.61 | 104 | 33.7 | -15.29 | -2.61 | -21.48 | 192 |
| 47 | Donchian 20/10 · 1h | breakout | 82.62 | -17.38 | 93 | 20.4 | -23.21 | -4.50 | -26.17 | 216 |
| 48 | OBV trend · 1h | momentum | 82.39 | -17.61 | 198 | 17.7 | -30.85 | -6.78 | -32.73 | 304 |
| 49 | MACD zero-line · 1h | trend | 82.24 | -17.76 | 103 | 15.5 | -21.06 | -4.41 | -24.69 | 216 |
| 50 | Williams %R · 1h | reversion | 82.24 | -17.76 | 209 | 45.0 | -33.98 | -6.04 | -36.69 | 510 |
| 51 | MFI reversion · 1h | reversion | 82.10 | -17.91 | 247 | 31.2 | -17.54 | -2.87 | -20.54 | 142 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -43.35 | -20.91 | -43.46 | 584 |
| 53 | CCI reversion · 1h | reversion | 80.82 | -19.18 | 195 | 43.1 | -25.85 | -3.87 | -28.17 | 434 |
| 54 | Agent (ML meta-label) | meta | 80.22 | -19.78 | 837 | 18.9 | -14.11 | -2.64 | -15.56 | 364 |
| 55 | Bollinger reversion · 1h | reversion | 80.21 | -19.79 | 168 | 35.1 | -31.28 | -6.57 | -32.19 | 356 |
| 56 | Heikin-Ashi · 1h | trend | 79.99 | -20.01 | 261 | 23.4 | -42.27 | -9.85 | -43.38 | 646 |
| 57 | ROC + volume · 1h | momentum | 79.50 | -20.50 | 235 | 23.8 | -29.82 | -5.95 | -31.24 | 377 |
| 58 | EMA 9/21 cross · 1h | trend | 78.28 | -21.72 | 155 | 11.6 | -29.05 | -5.94 | -32.74 | 316 |
| 59 | RSI(14) reversion · 1h | reversion | 77.90 | -22.09 | 90 | 23.3 | -15.21 | -2.82 | -23.51 | 184 |
| 60 | Candlestick reversal · 1h | reversion | 77.36 | -22.64 | 249 | 29.3 | -34.77 | -6.60 | -36.06 | 533 |
| 61 | VWAP momentum · 1h | momentum | 77.09 | -22.91 | 499 | 21.4 | -49.31 | -11.48 | -49.51 | 1191 |
| 62 | Max aggression: 1-day momentum | meta | 67.94 | -32.06 | 18 | 27.8 | -41.16 | -2.84 | -48.56 | 41 |
| 63 | ROC + volume | momentum | 58.29 | -41.71 | 697 | 23.0 | -74.53 | -27.04 | -74.54 | 1537 |
| 64 | Volume breakout | breakout | 57.55 | -42.45 | 414 | 13.3 | -60.23 | -26.09 | -60.23 | 754 |
| 65 | Donchian 55/20 | breakout | 54.95 | -45.05 | 551 | 19.6 | -70.56 | -23.90 | -70.72 | 1238 |
| 66 | Squeeze breakout | breakout | 54.43 | -45.57 | 540 | 14.3 | -65.73 | -28.48 | -65.79 | 1132 |
| 67 | EMA 20/50 cross | trend | 53.84 | -46.16 | 595 | 20.5 | -77.90 | -23.21 | -78.22 | 1381 |
| 68 | RSI(14) reversion | reversion | 53.03 | -46.97 | 808 | 26.0 | -76.49 | -19.73 | -76.67 | 1652 |
| 69 | VWAP reversion | reversion | 50.67 | -49.33 | 809 | 25.0 | -74.46 | -17.55 | -74.67 | 1540 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.57 | -44.33 | -98.59 | 4920 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -47.62 | -93.45 | 2469 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.20 | -29.98 | -88.31 | 1850 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.94 | -37.90 | -91.00 | 2278 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.99 | -31.04 | -90.02 | 2122 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.52 | -52.62 | -97.55 | 3379 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.81 | -61.38 | -95.83 | 3280 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -35.14 | -93.65 | 2415 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.18 | -36.03 | -82.23 | 1656 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.29 | -53.36 | -99.30 | 5596 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.01 | -41.48 | -92.06 | 2547 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.15 | -40.28 | -95.15 | 3322 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -81.77 | -99.73 | 5988 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.66 | -45.09 | -91.67 | 2265 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.38 | -65.48 | -97.39 | 3472 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.41 | -57.73 | -98.43 | 4641 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.99 | -59.18 | -94.01 | 2705 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.28 | -40.15 | -83.34 | 1757 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -64.15 | -99.52 | 6076 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.51 | -28.78 | -87.53 | 2148 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.90 | -38.28 | -89.96 | 2219 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.82 | -46.79 | -95.83 | 3693 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.08 | -48.48 | -89.17 | 2054 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.97 | -47.50 | -96.01 | 4068 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -108.86 | -99.89 | 8025 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T09:45 | RSI(14) reversion | buy | SOL-USD | 13.28 | — | entry signal |
| 2026-10-23T09:45 | RSI(14) reversion | buy | ETH-USD | 13.28 | — | entry signal |
| 2026-10-23T09:40 | EMA 20/50 cross | sell | XRP-USD | 10.80 | 0.03 | exit signal |
| 2026-10-23T09:40 | EMA 20/50 cross | sell | SOL-USD | 13.41 | -0.06 | exit signal |
| 2026-10-23T09:35 | EMA 20/50 cross | sell | ETH-USD | 13.41 | -0.04 | exit signal |
| 2026-10-23T09:30 | ROC + volume | sell | DOGE-USD | 14.45 | -0.16 | stop-loss |
| 2026-10-23T09:30 | EMA 20/50 cross | sell | BTC-USD | 5.29 | -0.04 | stop-loss |
| 2026-10-23T09:15 | Volume breakout | sell | DOGE-USD | 14.29 | -0.14 | stop-loss |
| 2026-10-23T09:15 | Squeeze breakout | sell | DOGE-USD | 13.56 | -0.06 | stop-loss |
| 2026-10-23T09:00 | Agent (ML meta-label) | sell | XRP-USD | 3.81 | -0.01 | selected signal exited |
| 2026-10-23T09:00 | MFI reversion · 1h | sell | SOL-USD | 10.30 | 0.01 | exit signal |
| 2026-10-23T09:00 | Candlestick reversal · 1h | sell | DOGE-USD | 5.24 | 0.08 | exit signal |
| 2026-10-23T09:00 | Bollinger breakout · 1h | buy | DOGE-USD | 22.37 | — | entry signal |
| 2026-10-23T09:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 20.34 | — | entry signal |
| 2026-10-23T09:00 | RSI momentum · 1h | buy | DOGE-USD | 14.46 | — | entry signal |
| 2026-10-23T09:00 | Supertrend · 1h | buy | DOGE-USD | 14.51 | — | entry signal |
| 2026-10-23T08:55 | Volume breakout | buy | DOGE-USD | 14.42 | — | entry signal |
| 2026-10-23T08:50 | ROC + volume | buy | DOGE-USD | 14.61 | — | entry signal |
| 2026-10-23T08:45 | Squeeze breakout | buy | DOGE-USD | 13.62 | — | entry signal |
| 2026-10-23T08:30 | EMA 20/50 cross | buy | BTC-USD | 5.33 | — | entry signal |
| 2026-10-23T08:00 | Agent (ML meta-label) | buy | XRP-USD | 3.82 | — | entry |
| 2026-10-23T08:00 | Agent (ML meta-label) | sell | ETH-USD | 3.32 | -0.02 | selected signal exited |
| 2026-10-23T08:00 | MFI reversion · 1h | buy | SOL-USD | 4.80 | — | rebalance up |
| 2026-10-23T08:00 | MFI reversion · 1h | sell | BTC-USD | 4.80 | -0.02 | exit signal |
| 2026-10-23T08:00 | Candlestick reversal · 1h | sell | XRP-USD | 4.40 | 0.03 | exit signal |
| 2026-10-23T08:00 | Candlestick reversal · 1h | sell | ETH-USD | 5.15 | -0.01 | exit signal |
| 2026-10-23T07:50 | Donchian 55/20 | sell | XRP-USD | 13.63 | -0.12 | stop-loss |
| 2026-10-23T07:30 | Agent (ML meta-label) | buy | ETH-USD | 3.34 | — | entry |
| 2026-10-23T07:30 | CCI reversion · 1h | buy | XRP-USD | 6.57 | — | entry |
| 2026-10-23T07:30 | Candlestick reversal · 1h | sell | BTC-USD | 4.81 | -0.03 | target is flat |
| 2026-10-23T07:30 | ROC + volume · 1h | sell | XRP-USD | 19.79 | -0.13 | target is flat |
| 2026-10-23T07:30 | ROC + volume · 1h | sell | ETH-USD | 19.80 | -0.13 | target is flat |
| 2026-10-23T07:30 | Heikin-Ashi · 1h | buy | DOGE-USD | 20.00 | — | entry |
| 2026-10-23T07:20 | Agent (ML meta-label) | sell | XRP-USD | 3.46 | -0.02 | selected signal exited |
| 2026-10-23T07:20 | CCI reversion · 1h | buy | ETH-USD | 4.61 | — | rebalance up |
| 2026-10-23T07:20 | CCI reversion · 1h | buy | BTC-USD | 4.63 | — | rebalance up |
| 2026-10-23T07:20 | CCI reversion · 1h | sell | XRP-USD | 13.47 | 0.02 | target is flat |
| 2026-10-23T07:20 | ROC + volume · 1h | buy | XRP-USD | 19.92 | — | entry |
| 2026-10-23T07:20 | Heikin-Ashi · 1h | sell | DOGE-USD | 19.97 | -0.03 | target is flat |
| 2026-10-23T07:16 | Candlestick reversal · 1h | buy | BTC-USD | 4.84 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 09:45:05.000187+00:00 -> 2026-10-23 09:55:05.000187+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
