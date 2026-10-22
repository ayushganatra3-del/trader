# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T02:20:05.000139+00:00 · 31344 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.67 (-9.33%)

Closed trades 93, win rate 40.9%, fees £3.03, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-21 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.42 · VIX 16.68 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 1680 decisions in 336 calls, $0.0236 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T02:20 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-22T02:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T02:20 | 3 / 2 / 0 | ETH-USD 51% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.01 | 6.01 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.48 | 1.48 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.21 | 0.21 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.60 | -0.40 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.38 | -0.62 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Hold BTC | benchmark | 98.00 | -2.00 | 0 | — | 10.97 | 1.73 | -8.68 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.47 | -2.52 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.04 | -2.96 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 18 | Copy: Insider buying | copy | 96.67 | -3.33 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.77 | -4.23 | 117 | 30.8 | -8.40 | -4.90 | -8.45 | 236 |
| 20 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 21 | ADX DI cross · 1h | trend | 95.45 | -4.55 | 92 | 19.6 | -10.94 | -2.00 | -16.14 | 259 |
| 22 | Daily: Momentum burst | daily | 94.91 | -5.09 | 6 | 16.7 | -9.30 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.85 | -5.15 | 92 | 23.9 | -20.40 | -6.36 | -20.58 | 129 |
| 24 | Donchian 55/20 · 1h | breakout | 94.65 | -5.35 | 43 | 16.3 | -15.68 | -3.21 | -16.74 | 103 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.56 | 2.04 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.90 | -7.10 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.81 | -7.19 | 113 | 25.7 | -16.24 | -3.59 | -19.79 | 272 |
| 29 | Squeeze breakout · 1h | breakout | 92.49 | -7.51 | 50 | 24.0 | -2.55 | -0.55 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.18 | -7.83 | 8 | 0.0 | -2.44 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.00 | -8.00 | 93 | 30.1 | -9.96 | -1.80 | -14.57 | 261 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -19.66 | -6.34 | -20.51 | 263 |
| 34 | Volume breakout · 1h | breakout | 90.36 | -9.64 | 95 | 24.2 | -13.27 | -2.36 | -14.55 | 108 |
| 35 | Supertrend · 1h | trend | 89.65 | -10.35 | 92 | 14.1 | -21.13 | -4.23 | -26.66 | 218 |
| 36 | Stochastic reversion · 1h | reversion | 89.54 | -10.46 | 169 | 47.3 | -13.60 | -2.22 | -22.24 | 363 |
| 37 | RSI momentum · 1h | momentum | 89.10 | -10.90 | 89 | 18.0 | -19.22 | -3.87 | -20.75 | 220 |
| 38 | EMA 20/50 cross · 1h | trend | 88.53 | -11.47 | 62 | 12.9 | -21.18 | -3.65 | -23.57 | 141 |
| 39 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 40 | Connors RSI(2) · 1h | reversion | 87.94 | -12.06 | 161 | 41.6 | -23.68 | -7.08 | -23.74 | 199 |
| 41 | Keltner breakout · 1h | breakout | 87.66 | -12.34 | 67 | 23.9 | -18.69 | -3.47 | -24.10 | 201 |
| 42 | MACD cross · 1h | trend | 87.42 | -12.58 | 202 | 22.3 | -23.89 | -4.53 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -15.84 | -4.43 | -16.97 | 128 |
| 44 | Z-score reversion · 1h | reversion | 86.78 | -13.22 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 45 | Ichimoku · 1h | trend | 86.50 | -13.50 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 46 | Donchian 20/10 · 1h | breakout | 85.39 | -14.61 | 87 | 20.7 | -21.70 | -4.08 | -28.80 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.25 | -14.75 | 92 | 15.2 | -26.17 | -4.78 | -27.39 | 221 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.57 | -2.02 | -21.11 | 141 |
| 49 | Agent (ML meta-label) | meta | 84.62 | -15.38 | 735 | 20.1 | -12.07 | -2.22 | -15.61 | 369 |
| 50 | MACD zero-line · 1h | trend | 84.50 | -15.50 | 92 | 15.2 | -23.35 | -4.54 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 83.59 | -16.41 | 189 | 18.0 | -30.33 | -5.66 | -31.52 | 306 |
| 52 | ROC + volume · 1h | momentum | 82.76 | -17.24 | 218 | 23.9 | -27.38 | -4.97 | -32.91 | 388 |
| 53 | Bollinger reversion · 1h | reversion | 82.59 | -17.41 | 163 | 36.2 | -29.10 | -5.61 | -32.84 | 348 |
| 54 | Williams %R · 1h | reversion | 82.59 | -17.41 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.61 | -18.09 | -46.47 | 606 |
| 56 | CCI reversion · 1h | reversion | 82.11 | -17.89 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.40 | -18.60 | 251 | 23.9 | -42.85 | -9.17 | -46.38 | 678 |
| 58 | RSI(14) reversion · 1h | reversion | 80.87 | -19.13 | 85 | 24.7 | -16.91 | -2.89 | -24.99 | 172 |
| 59 | EMA 9/21 cross · 1h | trend | 80.75 | -19.25 | 144 | 11.1 | -26.77 | -5.19 | -29.94 | 331 |
| 60 | Candlestick reversal · 1h | reversion | 79.00 | -21.00 | 231 | 30.3 | -38.39 | -7.05 | -41.73 | 536 |
| 61 | VWAP momentum · 1h | momentum | 78.97 | -21.03 | 483 | 22.2 | -46.40 | -8.74 | -52.83 | 1254 |
| 62 | Max aggression: 1-day momentum | meta | 77.12 | -22.88 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.88 | -22.07 | -78.97 | 1712 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.31 | -19.56 | -64.95 | 862 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.33 | -19.62 | -74.04 | 1283 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -66.98 | -22.65 | -67.93 | 1206 |
| 67 | RSI(14) reversion | reversion | 55.78 | -44.22 | 771 | 26.8 | -74.97 | -16.85 | -75.15 | 1619 |
| 68 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.87 | -19.24 | -80.87 | 1438 |
| 69 | VWAP reversion | reversion | 54.11 | -45.89 | 766 | 26.0 | -70.94 | -14.16 | -72.15 | 1465 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.83 | -32.06 | -98.87 | 5298 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.05 | -33.98 | -94.26 | 2595 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.04 | -23.78 | -88.71 | 1894 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.25 | -28.04 | -91.74 | 2363 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.18 | -25.43 | -91.26 | 2265 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -34.67 | -97.82 | 3507 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -37.55 | -97.03 | 3610 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.57 | -28.13 | -94.69 | 2561 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.12 | -27.95 | -83.42 | 1732 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -37.05 | -99.41 | 5740 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.13 | -29.25 | -92.69 | 2623 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.89 | -31.08 | -95.89 | 3472 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -42.06 | -99.77 | 6158 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -30.17 | -91.92 | 2337 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -39.33 | -97.82 | 3629 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -37.22 | -98.54 | 4706 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.24 | -35.20 | -94.46 | 2801 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.54 | -28.26 | -84.44 | 1800 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.56 | -39.86 | -99.56 | 6195 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.29 | -23.01 | -87.35 | 2155 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.11 | -26.97 | -88.11 | 2142 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.07 | -33.46 | -96.07 | 3771 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.49 | -33.71 | -89.50 | 2098 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.98 | -34.09 | -96.00 | 4093 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.03 | -99.91 | 8304 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T02:20 | Connors RSI(2) · 1h | sell | XRP-USD | 21.90 | -0.56 | stop-loss |
| 2026-10-22T02:20 | VWAP reversion | sell | DOGE-USD | 13.43 | -0.16 | stop-loss |
| 2026-10-22T02:20 | RSI(14) reversion | sell | SOL-USD | 13.82 | -0.17 | stop-loss |
| 2026-10-22T02:10 | RSI(14) reversion | buy | SOL-USD | 13.99 | — | entry signal |
| 2026-10-22T02:05 | Connors RSI(2) · 1h | buy | BTC-USD | 17.53 | — | rebalance up |
| 2026-10-22T02:05 | Connors RSI(2) · 1h | sell | DOGE-USD | 21.97 | -0.49 | stop-loss |
| 2026-10-22T02:00 | Connors RSI(2) · 1h | buy | BTC-USD | 4.58 | — | entry signal |
| 2026-10-22T02:00 | Connors RSI(2) · 1h | sell | SOL-USD | 4.42 | -0.06 | rebalance down |
| 2026-10-22T02:00 | Donchian 20/10 · 1h | sell | XRP-USD | 7.69 | 0.19 | exit signal |
| 2026-10-22T02:00 | Donchian 20/10 · 1h | sell | ETH-USD | 7.68 | -0.12 | exit signal |
| 2026-10-22T02:00 | Donchian 20/10 · 1h | sell | DOGE-USD | 7.67 | 0.07 | exit signal |
| 2026-10-22T02:00 | Donchian 20/10 · 1h | sell | BTC-USD | 7.70 | -0.09 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | XRP-USD | 7.48 | 0.17 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | SOL-USD | 8.82 | -0.09 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | ETH-USD | 4.14 | -0.11 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | DOGE-USD | 4.87 | 0.03 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | BTC-USD | 6.30 | -0.03 | exit signal |
| 2026-10-22T02:00 | Ichimoku · 1h | sell | BTC-USD | 17.61 | -0.08 | exit signal |
| 2026-10-22T02:00 | ADX DI cross · 1h | sell | BTC-USD | 7.86 | -0.10 | exit signal |
| 2026-10-22T02:00 | Supertrend · 1h | sell | XRP-USD | 5.96 | 0.12 | exit signal |
| 2026-10-22T02:00 | Supertrend · 1h | sell | ETH-USD | 4.40 | -0.01 | exit signal |
| 2026-10-22T02:00 | Supertrend · 1h | sell | DOGE-USD | 4.88 | 0.07 | exit signal |
| 2026-10-22T02:00 | Supertrend · 1h | sell | BTC-USD | 4.46 | -0.02 | exit signal |
| 2026-10-22T02:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 4.17 | 0.02 | exit signal |
| 2026-10-22T02:00 | VWAP reversion | buy | XRP-USD | 13.59 | — | entry signal |
| 2026-10-22T02:00 | VWAP reversion | buy | DOGE-USD | 13.59 | — | entry signal |
| 2026-10-22T01:45 | ROC + volume · 1h | sell | BTC-USD | 3.92 | -0.03 | stop-loss |
| 2026-10-22T01:40 | Squeeze breakout · 1h | sell | BTC-USD | 18.51 | 0.08 | stop-loss |
| 2026-10-22T01:40 | Keltner breakout · 1h | sell | BTC-USD | 9.73 | 0.04 | stop-loss |
| 2026-10-22T01:40 | Bollinger breakout · 1h | sell | BTC-USD | 7.63 | 0.08 | stop-loss |
| 2026-10-22T01:40 | RSI(14) reversion | sell | XRP-USD | 13.96 | -0.19 | stop-loss |
| 2026-10-22T01:40 | RSI(14) reversion | sell | ETH-USD | 14.01 | -0.18 | stop-loss |
| 2026-10-22T01:40 | RSI(14) reversion | sell | DOGE-USD | 13.97 | -0.18 | stop-loss |
| 2026-10-22T01:40 | RSI(14) reversion | sell | BTC-USD | 14.01 | -0.16 | stop-loss |
| 2026-10-22T00:50 | RSI(14) reversion | buy | XRP-USD | 2.81 | — | rebalance up |
| 2026-10-22T00:50 | RSI(14) reversion | buy | ETH-USD | 2.83 | — | rebalance up |
| 2026-10-22T00:50 | RSI(14) reversion | buy | DOGE-USD | 2.84 | — | rebalance up |
| 2026-10-22T00:50 | RSI(14) reversion | buy | BTC-USD | 5.64 | — | rebalance up |
| 2026-10-22T00:50 | RSI(14) reversion | sell | SOL-USD | 11.29 | -0.02 | exit signal |
| 2026-10-22T00:40 | RSI(14) reversion | sell | SOL-USD | 2.82 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 02:20:05.000139+00:00 -> 2026-10-22 02:30:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
