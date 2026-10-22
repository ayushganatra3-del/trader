# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T00:20:05.000137+00:00 · 31248 ticks

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

Today: 240 decisions in 48 calls, $0.0034 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T00:20 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-22T00:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T00:20 | 3 / 2 / 0 | ETH-USD 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.81 | +2.89% | 6 |
| VWAP momentum | NVDA | 1.78 | +2.87% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.08 | 6.08 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.54 | 1.54 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.27 | 0.27 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.66 | -0.34 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold BTC | benchmark | 99.55 | -0.45 | 0 | — | 12.69 | 1.97 | -8.68 | 1 |
| 12 | Hold SPY | benchmark | 99.44 | -0.56 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.54 | -2.46 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.10 | -2.90 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 18 | Copy: Insider buying | copy | 96.73 | -3.27 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.79 | -4.21 | 117 | 30.8 | -8.40 | -4.90 | -8.45 | 236 |
| 20 | ADX DI cross · 1h | trend | 95.61 | -4.39 | 91 | 19.8 | -10.85 | -1.98 | -16.14 | 259 |
| 21 | Donchian 55/20 · 1h | breakout | 95.58 | -4.42 | 43 | 16.3 | -14.90 | -3.03 | -16.13 | 103 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 23 | Daily: Momentum burst | daily | 94.97 | -5.04 | 6 | 16.7 | -9.31 | -1.37 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 94.87 | -5.13 | 92 | 23.9 | -20.41 | -6.36 | -20.58 | 129 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.04 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.96 | -7.04 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.83 | -7.17 | 113 | 25.7 | -16.24 | -3.59 | -19.79 | 272 |
| 29 | Squeeze breakout · 1h | breakout | 92.66 | -7.34 | 49 | 22.4 | -2.36 | -0.50 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.22 | -7.78 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.10 | -7.90 | 92 | 29.3 | -9.48 | -1.68 | -15.29 | 263 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -18.52 | -6.47 | -19.47 | 256 |
| 34 | Volume breakout · 1h | breakout | 90.39 | -9.61 | 95 | 24.2 | -13.69 | -2.44 | -14.96 | 113 |
| 35 | Supertrend · 1h | trend | 90.08 | -9.92 | 88 | 12.5 | -20.87 | -4.17 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.60 | -10.40 | 84 | 16.7 | -18.14 | -3.63 | -20.65 | 220 |
| 37 | Connors RSI(2) · 1h | reversion | 89.59 | -10.41 | 159 | 42.1 | -22.24 | -6.65 | -23.74 | 198 |
| 38 | Stochastic reversion · 1h | reversion | 89.57 | -10.43 | 169 | 47.3 | -13.60 | -2.22 | -22.24 | 363 |
| 39 | EMA 20/50 cross · 1h | trend | 88.84 | -11.16 | 62 | 12.9 | -20.95 | -3.60 | -23.57 | 141 |
| 40 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 41 | Keltner breakout · 1h | breakout | 87.78 | -12.22 | 66 | 22.7 | -18.49 | -3.46 | -24.72 | 203 |
| 42 | MACD cross · 1h | trend | 87.47 | -12.53 | 202 | 22.3 | -23.82 | -4.51 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -20.94 | -4.35 | -20.95 | 124 |
| 44 | Z-score reversion · 1h | reversion | 86.81 | -13.19 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 45 | Ichimoku · 1h | trend | 86.79 | -13.21 | 60 | 13.3 | -17.97 | -3.37 | -20.25 | 118 |
| 46 | Donchian 20/10 · 1h | breakout | 85.89 | -14.11 | 83 | 19.3 | -19.97 | -3.70 | -29.03 | 229 |
| 47 | Triple EMA stack · 1h | trend | 85.66 | -14.34 | 92 | 15.2 | -25.75 | -4.69 | -27.28 | 221 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.57 | -2.02 | -21.11 | 140 |
| 49 | Agent (ML meta-label) | meta | 84.66 | -15.34 | 735 | 20.1 | -13.81 | -2.69 | -17.06 | 371 |
| 50 | MACD zero-line · 1h | trend | 84.56 | -15.44 | 92 | 15.2 | -23.36 | -4.54 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 83.87 | -16.13 | 189 | 18.0 | -31.22 | -5.87 | -31.76 | 310 |
| 52 | ROC + volume · 1h | momentum | 82.84 | -17.16 | 217 | 24.0 | -25.91 | -4.61 | -32.91 | 395 |
| 53 | Williams %R · 1h | reversion | 82.61 | -17.39 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 54 | Bollinger reversion · 1h | reversion | 82.60 | -17.40 | 163 | 36.2 | -29.10 | -5.61 | -32.84 | 348 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.58 | -18.05 | -46.47 | 605 |
| 56 | CCI reversion · 1h | reversion | 82.14 | -17.86 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.42 | -18.58 | 251 | 23.9 | -42.85 | -9.17 | -46.38 | 678 |
| 58 | EMA 9/21 cross · 1h | trend | 80.93 | -19.07 | 143 | 10.5 | -26.66 | -5.16 | -29.94 | 331 |
| 59 | RSI(14) reversion · 1h | reversion | 80.90 | -19.10 | 85 | 24.7 | -16.91 | -2.89 | -24.99 | 172 |
| 60 | Candlestick reversal · 1h | reversion | 79.05 | -20.95 | 231 | 30.3 | -38.28 | -7.01 | -41.79 | 535 |
| 61 | VWAP momentum · 1h | momentum | 79.01 | -20.99 | 483 | 22.2 | -46.67 | -8.90 | -52.84 | 1254 |
| 62 | Max aggression: 1-day momentum | meta | 77.17 | -22.83 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -78.10 | -22.52 | -78.99 | 1720 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.43 | -19.76 | -64.95 | 867 |
| 65 | RSI(14) reversion | reversion | 56.62 | -43.38 | 765 | 27.1 | -74.61 | -16.58 | -74.90 | 1617 |
| 66 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.06 | -19.23 | -74.04 | 1282 |
| 67 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.16 | -23.00 | -67.93 | 1208 |
| 68 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.92 | -19.35 | -80.87 | 1440 |
| 69 | VWAP reversion | reversion | 54.37 | -45.63 | 765 | 26.0 | -70.79 | -14.07 | -72.15 | 1462 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.78 | -30.85 | -98.83 | 5284 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.02 | -33.80 | -94.26 | 2597 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.92 | -23.45 | -88.68 | 1894 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.21 | -27.84 | -91.74 | 2364 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.32 | -25.81 | -91.33 | 2272 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -34.53 | -97.82 | 3506 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.92 | -37.60 | -97.02 | 3602 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.52 | -27.69 | -94.69 | 2576 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.18 | -28.10 | -83.41 | 1734 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -36.37 | -99.40 | 5729 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.12 | -29.24 | -92.67 | 2623 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.91 | -31.24 | -95.91 | 3480 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.92 | -99.77 | 6165 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.80 | -30.33 | -91.92 | 2339 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -39.42 | -97.82 | 3636 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -36.84 | -98.53 | 4709 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.28 | -35.54 | -94.46 | 2803 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.52 | -28.22 | -84.44 | 1800 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.18 | -99.55 | 6191 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.17 | -22.76 | -87.24 | 2155 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.99 | -26.55 | -88.05 | 2150 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -33.07 | -96.03 | 3767 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.48 | -33.64 | -89.52 | 2098 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.92 | -33.53 | -95.94 | 4091 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.31 | -99.91 | 8299 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T00:10 | RSI(14) reversion | buy | BTC-USD | 2.83 | — | rebalance up |
| 2026-10-22T00:10 | RSI(14) reversion | sell | ETH-USD | 2.83 | -0.01 | rebalance down |
| 2026-10-22T00:05 | RSI(14) reversion | buy | BTC-USD | 2.87 | — | entry signal |
| 2026-10-22T00:05 | RSI(14) reversion | sell | XRP-USD | 2.84 | -0.01 | rebalance down |
| 2026-10-22T00:00 | Connors RSI(2) · 1h | buy | SOL-USD | 22.38 | — | entry signal |
| 2026-10-22T00:00 | Connors RSI(2) · 1h | buy | ETH-USD | 22.38 | — | entry signal |
| 2026-10-22T00:00 | Volume breakout · 1h | sell | BTC-USD | 12.86 | -0.05 | exit signal |
| 2026-10-22T00:00 | OBV trend · 1h | sell | ETH-USD | 9.22 | 0.07 | exit signal |
| 2026-10-22T00:00 | VWAP momentum · 1h | sell | XRP-USD | 3.56 | 0.02 | exit signal |
| 2026-10-22T00:00 | VWAP momentum · 1h | sell | ETH-USD | 3.55 | 0.00 | exit signal |
| 2026-10-22T00:00 | VWAP momentum · 1h | sell | BTC-USD | 3.57 | 0.02 | exit signal |
| 2026-10-22T00:00 | Parabolic SAR · 1h | sell | SOL-USD | 13.17 | -0.14 | exit signal |
| 2026-10-22T00:00 | Parabolic SAR · 1h | sell | BTC-USD | 13.23 | 0.22 | exit signal |
| 2026-10-22T00:00 | MACD cross · 1h | sell | BTC-USD | 5.41 | 0.03 | exit signal |
| 2026-10-22T00:00 | RSI(14) reversion | buy | SOL-USD | 14.14 | — | entry signal |
| 2026-10-21T23:50 | ROC + volume · 1h | sell | SOL-USD | 2.46 | -0.03 | stop-loss |
| 2026-10-21T23:45 | Volume breakout · 1h | sell | BTC-USD | 5.13 | -0.01 | rebalance down |
| 2026-10-21T23:45 | RSI(14) reversion | buy | DOGE-USD | 14.16 | — | entry signal |
| 2026-10-21T23:45 | RSI(14) reversion | sell | SOL-USD | 14.11 | -0.14 | stop-loss |
| 2026-10-21T23:35 | RSI(14) reversion | buy | XRP-USD | 14.20 | — | entry signal |
| 2026-10-21T23:35 | RSI(14) reversion | buy | ETH-USD | 14.20 | — | entry signal |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | buy | XRP-USD | 9.40 | — | rebalance up |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | buy | SOL-USD | 5.52 | — | rebalance up |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | buy | BTC-USD | 5.36 | — | rebalance up |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | sell | ETH-USD | 13.53 | -0.27 | stop-loss |
| 2026-10-21T23:30 | Donchian 55/20 · 1h | sell | DOGE-USD | 14.96 | -0.33 | stop-loss |
| 2026-10-21T23:30 | ROC + volume · 1h | sell | XRP-USD | 4.85 | 0.03 | stop-loss |
| 2026-10-21T23:30 | ROC + volume · 1h | sell | ETH-USD | 3.91 | -0.02 | stop-loss |
| 2026-10-21T23:30 | RSI(14) reversion | sell | XRP-USD | 14.10 | -0.15 | stop-loss |
| 2026-10-21T23:16 | RSI(14) reversion | buy | XRP-USD | 14.25 | — | entry signal |
| 2026-10-21T23:16 | RSI(14) reversion | buy | SOL-USD | 14.25 | — | entry signal |
| 2026-10-21T23:14 | Volume breakout · 1h | buy | BTC-USD | 5.12 | — | rebalance up |
| 2026-10-21T23:10 | Squeeze breakout · 1h | sell | SOL-USD | 23.08 | -0.32 | stop-loss |
| 2026-10-21T23:10 | Keltner breakout · 1h | sell | SOL-USD | 8.71 | -0.09 | stop-loss |
| 2026-10-21T23:10 | Bollinger breakout · 1h | sell | SOL-USD | 5.37 | -0.05 | stop-loss |
| 2026-10-21T23:05 | ROC + volume · 1h | buy | SOL-USD | 2.48 | — | entry |
| 2026-10-21T23:05 | ROC + volume · 1h | sell | DOGE-USD | 1.99 | -0.04 | stop-loss |
| 2026-10-21T23:05 | RSI(14) reversion | sell | XRP-USD | 14.16 | -0.17 | stop-loss |
| 2026-10-21T23:05 | RSI(14) reversion | sell | DOGE-USD | 14.18 | -0.15 | stop-loss |
| 2026-10-21T23:05 | EMA 20/50 cross | sell | BTC-USD | 13.80 | -0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 00:20:05.000137+00:00 -> 2026-10-22 00:30:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
