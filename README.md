# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T16:40:05.000133+00:00 · 57142 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.22 (-13.79%)

Closed trades 184, win rate 35.3%, fees £5.45, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 17.45 | +0.31 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-12 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 22127 decisions in 2651 calls, $0.2850 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T16:40 | 0 / 12 / 17 | cash |  |
| Breezy | 2026-11-12T16:40 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-11-12T16:40 | 3 / 24 / 2 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.54 | +8.57% | 5 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.43 | 17.43 | 0 | — | 16.62 | 5.30 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 114.41 | 14.41 | 21 | 66.7 | 20.92 | 4.06 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 113.51 | 13.51 | 33 | 27.3 | 21.96 | 3.19 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.84 | 4.83 | 0 | — | 7.01 | 1.92 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.46 | 1.46 | 137 | 33.6 | 7.98 | 3.05 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.75 | 0.75 | 192 | 32.8 | 6.77 | 1.92 | -9.06 | 233 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent (rotation) | meta | 98.99 | -1.01 | 189 | 30.2 | -0.88 | -0.25 | -8.93 | 169 |
| 11 | Hold SPY | benchmark | 98.97 | -1.03 | 0 | — | -0.71 | -0.07 | -6.18 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -2.64 | 0.06 | -18.69 | 5 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 98.31 | -1.69 | 1 | 0.0 | -1.64 | -1.07 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.34 | -3.66 | 0 | — | -3.90 | -0.99 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 95.37 | -4.63 | 43 | 39.5 | -6.09 | -1.18 | -15.11 | 67 |
| 16 | VWAP reversion · 1h | reversion | 95.30 | -4.70 | 142 | 47.2 | -13.01 | -3.37 | -13.44 | 157 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.68 | -5.32 | 0 | — | -2.77 | -0.69 | -10.64 | 1 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 94.49 | -5.51 | 1 | 0.0 | -5.78 | -1.19 | -16.91 | 2 |
| 19 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 21 | Trend pullback · 1h | trend | 92.24 | -7.76 | 109 | 22.9 | -13.98 | -4.91 | -18.42 | 76 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -7.23 | -2.29 | -14.89 | 74 |
| 23 | Opening range 30m | breakout | 86.75 | -13.25 | 418 | 32.8 | -9.66 | -3.01 | -14.11 | 603 |
| 24 | Parabolic SAR · 1h | trend | 86.58 | -13.43 | 171 | 27.5 | -13.31 | -2.81 | -21.98 | 220 |
| 25 | Agent | meta | 86.22 | -13.79 | 184 | 35.3 | -14.39 | -7.21 | -15.39 | 211 |
| 26 | Daily: Bullish score | daily | 84.75 | -15.24 | 16 | 18.8 | -11.42 | -1.64 | -19.56 | 15 |
| 27 | Agent (aggressive) | meta | 84.50 | -15.50 | 90 | 34.4 | -15.29 | -4.22 | -18.51 | 101 |
| 28 | Hold BTC | benchmark | 84.44 | -15.56 | 1 | 0.0 | -7.96 | -0.98 | -18.34 | 1 |
| 29 | Donchian 55/20 · 1h | breakout | 84.24 | -15.76 | 73 | 13.7 | -22.15 | -4.61 | -29.68 | 94 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 83.09 | -16.91 | 2 | 0.0 | -8.10 | -0.83 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.92 | -18.08 | 114 | 23.7 | -17.66 | -3.63 | -25.87 | 176 |
| 32 | ADX DI cross · 1h | trend | 81.73 | -18.27 | 191 | 19.4 | -20.51 | -3.26 | -29.89 | 269 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -25.19 | -1.27 | -45.81 | 24 |
| 34 | Connors RSI(2) · 1h | reversion | 81.18 | -18.82 | 210 | 40.5 | -19.69 | -6.62 | -20.32 | 120 |
| 35 | MFI reversion · 1h | reversion | 80.25 | -19.75 | 377 | 35.8 | -16.97 | -2.16 | -23.02 | 163 |
| 36 | Volume breakout · 1h | breakout | 80.21 | -19.79 | 156 | 28.2 | -13.73 | -3.21 | -21.12 | 91 |
| 37 | Stochastic reversion · 1h | reversion | 79.53 | -20.47 | 297 | 47.5 | -26.72 | -3.95 | -27.36 | 389 |
| 38 | Opening range 15m | breakout | 79.18 | -20.82 | 512 | 31.2 | -17.23 | -4.60 | -21.36 | 725 |
| 39 | Heikin-Ashi · 1h | trend | 78.16 | -21.84 | 431 | 24.6 | -35.93 | -6.75 | -38.20 | 656 |
| 40 | MACD cross · 1h | trend | 77.67 | -22.33 | 370 | 21.9 | -27.38 | -4.02 | -38.93 | 464 |
| 41 | Bollinger breakout · 1h | breakout | 76.53 | -23.47 | 179 | 22.3 | -22.05 | -4.58 | -29.88 | 242 |
| 42 | MACD zero-line · 1h | trend | 76.18 | -23.82 | 164 | 17.1 | -21.48 | -4.32 | -31.17 | 207 |
| 43 | Supertrend · 1h | trend | 76.00 | -24.00 | 172 | 14.0 | -28.87 | -5.16 | -36.13 | 223 |
| 44 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -18.82 | -0.52 | -57.50 | 41 |
| 45 | RSI momentum · 1h | momentum | 75.42 | -24.57 | 162 | 13.6 | -23.48 | -3.60 | -35.96 | 214 |
| 46 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 47 | Daily: Momentum burst | daily | 75.18 | -24.82 | 27 | 11.1 | -33.28 | -4.53 | -38.17 | 33 |
| 48 | EMA 20/50 cross · 1h | trend | 75.02 | -24.98 | 105 | 10.5 | -26.81 | -4.51 | -38.13 | 119 |
| 49 | Triple EMA stack · 1h | trend | 73.74 | -26.26 | 147 | 14.3 | -26.64 | -4.39 | -37.93 | 204 |
| 50 | ROC + volume · 1h | momentum | 73.59 | -26.41 | 385 | 27.8 | -30.48 | -5.64 | -38.34 | 378 |
| 51 | Bollinger reversion · 1h | reversion | 72.67 | -27.33 | 290 | 41.0 | -30.37 | -4.66 | -34.84 | 377 |
| 52 | Donchian 20/10 · 1h | breakout | 72.60 | -27.40 | 145 | 19.3 | -27.46 | -4.96 | -35.87 | 211 |
| 53 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -33.54 | -4.89 | -35.88 | 454 |
| 54 | OBV trend · 1h | momentum | 71.99 | -28.01 | 285 | 19.6 | -26.41 | -4.50 | -36.59 | 284 |
| 55 | Williams %R · 1h | reversion | 68.29 | -31.71 | 358 | 45.5 | -41.88 | -6.86 | -42.00 | 532 |
| 56 | Z-score reversion · 1h | reversion | 67.72 | -32.28 | 199 | 38.2 | -27.30 | -3.78 | -28.98 | 234 |
| 57 | EMA 9/21 cross · 1h | trend | 67.63 | -32.37 | 257 | 9.7 | -33.21 | -6.15 | -41.74 | 335 |
| 58 | VWAP momentum · 1h | momentum | 66.89 | -33.11 | 883 | 22.3 | -51.40 | -10.63 | -52.34 | 1223 |
| 59 | Agent (ML meta-label) | meta | 66.84 | -33.16 | 1779 | 25.0 | -22.87 | -3.12 | -28.82 | 346 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -34.99 | -4.84 | -35.09 | 248 |
| 61 | Candlestick reversal · 1h | reversion | 62.81 | -37.19 | 467 | 28.5 | -42.35 | -7.60 | -42.45 | 595 |
| 62 | Three white soldiers | momentum | 58.91 | -41.09 | 534 | 14.6 | -49.41 | -22.70 | -49.41 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -43.99 | -99.01 | 5283 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.07 | -26.04 | -80.07 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.60 | -45.45 | -93.60 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.41 | -32.17 | -89.68 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.01 | -40.00 | -91.05 | 2334 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -31.20 | -90.17 | 2193 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -54.29 | -97.88 | 3461 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -55.13 | -96.32 | 3427 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.48 | -32.55 | -93.48 | 2329 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.94 | -33.77 | -83.07 | 1657 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.76 | -99.58 | 5985 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -43.32 | -92.24 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -37.05 | -95.45 | 3457 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -78.97 | -99.82 | 6144 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.20 | -44.08 | -92.20 | 2273 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.20 | -25.32 | -75.20 | 1631 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -57.63 | -97.62 | 3508 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -64.09 | -98.90 | 4915 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.35 | -26.98 | -68.44 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -57.85 | -94.76 | 2789 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.13 | -39.23 | -85.15 | 1799 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -76.85 | -99.66 | 6333 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.78 | -32.18 | -89.94 | 2305 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.09 | -20.15 | -78.41 | 1764 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.64 | -36.66 | -90.86 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.89 | -53.28 | -96.93 | 3867 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -56.99 | -89.10 | 2141 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.22 | -30.33 | -66.22 | 826 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.26 | -22.93 | -71.45 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.48 | -18.98 | -79.72 | 1718 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.34 | -49.77 | -97.37 | 4304 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -113.76 | -99.93 | 8340 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T16:40 | Agent (ML meta-label) | buy | SOXL | 3.48 | — | entry |
| 2026-11-12T16:40 | Agent (ML meta-label) | sell | PLTR | 3.48 | 0.00 | selected signal exited |
| 2026-11-12T16:40 | OBV trend · 1h | buy | TNA | 4.20 | — | rebalance up |
| 2026-11-12T16:40 | OBV trend · 1h | sell | SPY | 8.00 | 0.02 | target is flat |
| 2026-11-12T16:40 | ADX DI cross · 1h | buy | TQQQ | 4.12 | — | rebalance up |
| 2026-11-12T16:40 | ADX DI cross · 1h | sell | PLTR | 4.12 | 0.11 | rebalance down |
| 2026-11-12T16:40 | Three white soldiers | sell | MSTR | 14.69 | -0.06 | exit signal |
| 2026-11-12T16:40 | Three white soldiers | sell | DOGE-USD | 14.71 | -0.12 | exit signal |
| 2026-11-12T16:40 | Three white soldiers | sell | BTC-USD | 14.74 | -0.11 | exit signal |
| 2026-11-12T16:40 | Three white soldiers | sell | BITX | 14.77 | -0.05 | exit signal |
| 2026-11-12T16:40 | Opening range 30m | sell | ETHU | 6.12 | -0.13 | stop-loss |
| 2026-11-12T16:35 | Agent (ML meta-label) | buy | PLTR | 3.48 | — | entry |
| 2026-11-12T16:35 | Agent (ML meta-label) | buy | NVDA | 3.72 | — | entry |
| 2026-11-12T16:35 | Agent (ML meta-label) | buy | IWM | 3.72 | — | entry |
| 2026-11-12T16:35 | Agent (ML meta-label) | buy | AAPL | 3.72 | — | entry |
| 2026-11-12T16:35 | Agent (ML meta-label) | sell | TQQQ | 3.78 | 0.08 | rebalance down |
| 2026-11-12T16:35 | Agent (ML meta-label) | sell | SQQQ | 3.47 | -0.08 | rebalance down |
| 2026-11-12T16:35 | Agent (ML meta-label) | sell | SPY | 3.72 | -0.01 | rebalance down |
| 2026-11-12T16:35 | Agent (ML meta-label) | sell | MSFT | 3.66 | 0.01 | rebalance down |
| 2026-11-12T16:35 | Three white soldiers | buy | MSTR | 7.34 | — | rebalance up |
| 2026-11-12T16:35 | Three white soldiers | buy | DOGE-USD | 7.41 | — | rebalance up |
| 2026-11-12T16:35 | Three white soldiers | buy | BTC-USD | 7.42 | — | rebalance up |
| 2026-11-12T16:35 | Three white soldiers | buy | BITX | 7.40 | — | rebalance up |
| 2026-11-12T16:35 | Three white soldiers | sell | SOL-USD | 7.36 | -0.06 | exit signal |
| 2026-11-12T16:35 | Three white soldiers | sell | GOOGL | 7.41 | -0.01 | exit signal |
| 2026-11-12T16:35 | Three white soldiers | sell | ETHU | 7.41 | -0.01 | exit signal |
| 2026-11-12T16:35 | Three white soldiers | sell | ETH-USD | 7.38 | -0.04 | exit signal |
| 2026-11-12T16:31 | Agent (ML meta-label) | buy | LABU | 1.97 | — | following MFI reversion |
| 2026-11-12T16:31 | Agent (ML meta-label) | buy | COIN | 4.19 | — | entry |
| 2026-11-12T16:31 | Agent (ML meta-label) | buy | BITX | 4.19 | — | entry |
| 2026-11-12T16:31 | Agent (ML meta-label) | sell | TECL | 3.41 | 0.09 | rebalance down |
| 2026-11-12T16:31 | Agent (ML meta-label) | sell | MSTR | 3.40 | 0.11 | rebalance down |
| 2026-11-12T16:31 | Agent (ML meta-label) | sell | AMD | 3.53 | 0.17 | rebalance down |
| 2026-11-12T16:31 | Bollinger reversion · 1h | buy | MSTR | 9.07 | — | entry signal |
| 2026-11-12T16:31 | Bollinger reversion · 1h | buy | META | 9.13 | — | entry signal |
| 2026-11-12T16:31 | Bollinger reversion · 1h | buy | LABU | 9.13 | — | entry signal |
| 2026-11-12T16:31 | Bollinger reversion · 1h | sell | XRP-USD | 5.42 | -0.03 | rebalance down |
| 2026-11-12T16:31 | Bollinger reversion · 1h | sell | SOL-USD | 5.43 | -0.03 | rebalance down |
| 2026-11-12T16:31 | Bollinger reversion · 1h | sell | MSFT | 5.50 | 0.09 | rebalance down |
| 2026-11-12T16:31 | Bollinger reversion · 1h | sell | ETH-USD | 5.48 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 16:40:05.000133+00:00 -> 2026-11-12 16:50:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
