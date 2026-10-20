# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T19:25:05.000143+00:00 · 29847 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.83 (-9.17%)

Closed trades 88, win rate 39.8%, fees £2.94, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.61 | +0.33 |

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

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 36660 decisions in 2841 calls, $0.4506 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T19:25 | 2 / 7 / 21 | cash |  |
| Breezy | 2026-10-20T19:25 | 0 / 22 / 8 | cash |  |
| Boozy | 2026-10-20T19:25 | 4 / 23 / 3 | MSTR 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | BITX | 1.90 | +3.32% | 6 |
| VWAP reversion | ETHU | 1.90 | +4.27% | 5 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.70 | 5.70 | 0 | — | 8.06 | 3.86 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.66 | -2.08 | -13.79 | 134 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Max aggression: 5-day momentum | meta | 99.87 | -0.13 | 9 | 44.4 | -13.99 | -1.01 | -34.64 | 26 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 60 | 35.0 | 2.41 | 1.38 | -1.45 | 61 |
| 10 | Hold SPY | benchmark | 98.84 | -1.16 | 0 | — | 0.14 | 0.12 | -3.13 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 98.33 | -1.67 | 0 | — | -0.67 | -0.19 | -5.15 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 97.79 | -2.21 | 3 | 33.3 | 3.52 | 0.84 | -7.93 | 8 |
| 14 | Hold BTC | benchmark | 97.36 | -2.64 | 0 | — | 19.47 | 2.60 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.97 | -2.25 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.01 | -2.99 | 0 | — | -4.14 | -1.58 | -7.04 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.82 | -3.18 | 0 | — | 0.05 | 0.08 | -5.31 | 1 |
| 18 | Agent (rotation) | meta | 96.03 | -3.97 | 114 | 31.6 | -6.49 | -3.00 | -8.26 | 307 |
| 19 | Donchian 55/20 · 1h | breakout | 96.03 | -3.97 | 40 | 15.0 | -18.53 | -3.66 | -22.00 | 103 |
| 20 | Copy: Insider buying | copy | 95.77 | -4.23 | 25 | 40.0 | -12.32 | -2.12 | -20.62 | 72 |
| 21 | Trend pullback · 1h | trend | 95.73 | -4.27 | 90 | 23.3 | -20.37 | -6.09 | -20.86 | 133 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.42 | -5.58 | 89 | 18.0 | -12.69 | -2.29 | -16.22 | 254 |
| 24 | Daily: Momentum burst | daily | 93.98 | -6.02 | 6 | 16.7 | -7.04 | -0.94 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.28 | 1.37 | -6.51 | 198 |
| 26 | Opening range 30m | breakout | 92.01 | -7.99 | 208 | 29.3 | -13.51 | -3.95 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.34 | -8.66 | 105 | 21.9 | -18.66 | -4.02 | -22.26 | 274 |
| 28 | Squeeze breakout · 1h | breakout | 91.30 | -8.70 | 46 | 21.7 | -4.18 | -0.95 | -11.48 | 97 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.65 | -2.41 | -16.91 | 1 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 91.14 | -8.86 | 0 | — | 0.22 | 0.20 | -14.37 | 1 |
| 31 | Daily: Bullish score | daily | 91.10 | -8.90 | 7 | 0.0 | -7.86 | -0.88 | -13.10 | 13 |
| 32 | Agent | meta | 90.83 | -9.17 | 88 | 39.8 | -7.61 | -3.45 | -13.39 | 238 |
| 33 | Volume breakout · 1h | breakout | 90.55 | -9.45 | 84 | 22.6 | -12.44 | -2.23 | -13.91 | 107 |
| 34 | Bollinger breakout · 1h | breakout | 90.44 | -9.56 | 87 | 29.9 | -11.87 | -2.19 | -16.22 | 259 |
| 35 | Connors RSI(2) · 1h | reversion | 89.48 | -10.52 | 151 | 41.7 | -22.61 | -6.74 | -24.08 | 200 |
| 36 | RSI momentum · 1h | momentum | 89.02 | -10.98 | 83 | 15.7 | -22.73 | -4.58 | -24.95 | 217 |
| 37 | EMA 20/50 cross · 1h | trend | 88.59 | -11.41 | 62 | 12.9 | -19.36 | -3.68 | -21.51 | 130 |
| 38 | Opening range 15m | breakout | 88.14 | -11.87 | 256 | 25.8 | -18.02 | -4.87 | -20.98 | 700 |
| 39 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -9.51 | -2.58 | -17.42 | 123 |
| 40 | Supertrend · 1h | trend | 87.91 | -12.09 | 88 | 12.5 | -21.67 | -4.26 | -26.62 | 222 |
| 41 | Stochastic reversion · 1h | reversion | 87.64 | -12.36 | 164 | 47.0 | -14.76 | -2.46 | -22.24 | 362 |
| 42 | Keltner breakout · 1h | breakout | 87.22 | -12.78 | 60 | 21.7 | -16.61 | -2.69 | -26.35 | 207 |
| 43 | Ichimoku · 1h | trend | 86.73 | -13.27 | 60 | 13.3 | -19.19 | -3.61 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.15 | -13.85 | 193 | 20.2 | -27.55 | -5.32 | -33.68 | 469 |
| 45 | Triple EMA stack · 1h | trend | 85.15 | -14.85 | 91 | 14.3 | -31.04 | -5.73 | -35.00 | 228 |
| 46 | Z-score reversion · 1h | reversion | 84.46 | -15.54 | 96 | 30.2 | -14.36 | -2.36 | -21.32 | 195 |
| 47 | Donchian 20/10 · 1h | breakout | 84.35 | -15.65 | 81 | 17.3 | -15.06 | -2.05 | -28.46 | 219 |
| 48 | MFI reversion · 1h | reversion | 83.75 | -16.25 | 218 | 30.7 | -15.16 | -2.39 | -20.43 | 148 |
| 49 | Agent (ML meta-label) | meta | 83.63 | -16.37 | 711 | 19.1 | -6.60 | -1.02 | -15.82 | 373 |
| 50 | OBV trend · 1h | momentum | 83.60 | -16.41 | 186 | 17.2 | -30.96 | -5.56 | -37.06 | 320 |
| 51 | MACD zero-line · 1h | trend | 83.40 | -16.60 | 89 | 14.6 | -26.10 | -5.21 | -26.71 | 224 |
| 52 | Three white soldiers | momentum | 82.67 | -17.33 | 249 | 19.7 | -46.80 | -18.02 | -47.63 | 613 |
| 53 | Bollinger reversion · 1h | reversion | 82.19 | -17.80 | 162 | 35.8 | -29.25 | -5.68 | -32.82 | 348 |
| 54 | Williams %R · 1h | reversion | 81.28 | -18.72 | 195 | 43.6 | -30.99 | -4.83 | -36.49 | 525 |
| 55 | ROC + volume · 1h | momentum | 81.18 | -18.82 | 199 | 21.6 | -29.18 | -5.34 | -34.58 | 398 |
| 56 | CCI reversion · 1h | reversion | 80.62 | -19.38 | 178 | 41.6 | -18.58 | -2.33 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.24 | -19.76 | 231 | 20.8 | -42.43 | -8.87 | -47.30 | 673 |
| 58 | RSI(14) reversion · 1h | reversion | 79.63 | -20.37 | 83 | 22.9 | -13.76 | -2.39 | -23.28 | 172 |
| 59 | EMA 9/21 cross · 1h | trend | 79.35 | -20.65 | 143 | 10.5 | -29.72 | -6.20 | -30.32 | 326 |
| 60 | VWAP momentum · 1h | momentum | 77.59 | -22.41 | 458 | 20.1 | -45.34 | -8.09 | -50.51 | 1255 |
| 61 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -27.82 | -1.54 | -41.28 | 42 |
| 62 | Candlestick reversal · 1h | reversion | 77.06 | -22.94 | 226 | 28.8 | -34.48 | -6.18 | -37.08 | 545 |
| 63 | ROC + volume | momentum | 61.72 | -38.28 | 627 | 23.1 | -77.53 | -21.39 | -78.44 | 1713 |
| 64 | Volume breakout | breakout | 61.59 | -38.41 | 377 | 14.1 | -63.18 | -18.95 | -64.18 | 872 |
| 65 | Squeeze breakout | breakout | 58.66 | -41.34 | 489 | 14.1 | -66.02 | -22.11 | -66.58 | 1203 |
| 66 | Donchian 55/20 | breakout | 57.87 | -42.13 | 503 | 19.3 | -70.47 | -17.43 | -73.50 | 1275 |
| 67 | RSI(14) reversion | reversion | 57.28 | -42.72 | 741 | 26.3 | -74.42 | -16.41 | -74.89 | 1619 |
| 68 | EMA 20/50 cross | trend | 55.56 | -44.44 | 548 | 19.2 | -77.03 | -15.83 | -80.87 | 1446 |
| 69 | VWAP reversion | reversion | 53.64 | -46.36 | 753 | 25.2 | -71.64 | -14.63 | -72.28 | 1501 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.77 | -30.96 | -98.79 | 5308 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.57 | -31.91 | -93.88 | 2593 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.67 | -20.51 | -88.38 | 1895 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.34 | -24.88 | -91.32 | 2350 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.93 | -25.48 | -91.16 | 2243 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.56 | -33.14 | -97.64 | 3522 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.72 | -37.29 | -96.73 | 3574 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -27.98 | -94.44 | 2529 |
| 78 | Keltner breakout | breakout | 50.34 | -49.66 | 703 | 16.8 | -83.20 | -27.40 | -83.82 | 1802 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.72 | -27.39 | -82.72 | 1706 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -35.96 | -99.38 | 5753 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.73 | -27.40 | -92.24 | 2625 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.98 | -31.64 | -95.98 | 3470 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -40.84 | -99.75 | 6193 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.58 | -29.00 | -91.63 | 2351 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -38.57 | -97.66 | 3615 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.01 | -98.47 | 4706 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.04 | -34.76 | -94.07 | 2797 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.56 | -99.52 | 6184 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.62 | -22.02 | -87.01 | 2140 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.73 | -26.06 | -88.04 | 2130 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -32.41 | -95.97 | 3762 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.11 | -32.75 | -89.32 | 2117 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.68 | -32.95 | -95.80 | 4116 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.40 | -99.90 | 8285 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T19:25 | Agent (ML meta-label) | buy | COIN | 6.39 | — | entry |
| 2026-10-20T19:25 | Agent | sell | ETHU | 18.01 | -0.21 | selected signal exited |
| 2026-10-20T19:25 | CCI reversion · 1h | buy | UPRO | 4.19 | — | rebalance up |
| 2026-10-20T19:25 | CCI reversion · 1h | sell | GOOGL | 3.96 | -0.09 | stop-loss |
| 2026-10-20T19:25 | Williams %R · 1h | sell | GOOGL | 13.48 | -0.26 | stop-loss |
| 2026-10-20T19:25 | Z-score reversion · 1h | buy | UPRO | 4.32 | — | rebalance up |
| 2026-10-20T19:25 | Z-score reversion · 1h | buy | TECL | 4.44 | — | rebalance up |
| 2026-10-20T19:25 | Z-score reversion · 1h | buy | SPY | 4.29 | — | rebalance up |
| 2026-10-20T19:25 | Z-score reversion · 1h | buy | PLTR | 4.31 | — | rebalance up |
| 2026-10-20T19:25 | Z-score reversion · 1h | buy | NVDA | 4.33 | — | rebalance up |
| 2026-10-20T19:25 | Z-score reversion · 1h | sell | GOOGL | 7.64 | -0.18 | stop-loss |
| 2026-10-20T19:25 | VWAP reversion | buy | AAPL | 13.41 | — | entry signal |
| 2026-10-20T19:25 | VWAP reversion | sell | GOOGL | 13.37 | -0.05 | stop-loss |
| 2026-10-20T19:25 | RSI(14) reversion | buy | AAPL | 14.32 | — | entry signal |
| 2026-10-20T19:25 | RSI(14) reversion | sell | GOOGL | 14.29 | -0.05 | stop-loss |
| 2026-10-20T19:25 | Keltner breakout | sell | LABU | 12.47 | -0.15 | stop-loss |
| 2026-10-20T19:25 | Donchian 55/20 | sell | LABU | 14.43 | 0.17 | exit signal |
| 2026-10-20T19:25 | Donchian 55/20 | sell | DOGE-USD | 14.44 | -0.05 | exit signal |
| 2026-10-20T19:25 | EMA 20/50 cross | buy | XRP-USD | 3.18 | — | rebalance up |
| 2026-10-20T19:25 | EMA 20/50 cross | buy | TNA | 4.94 | — | rebalance up |
| 2026-10-20T19:25 | EMA 20/50 cross | buy | SQQQ | 3.14 | — | rebalance up |
| 2026-10-20T19:25 | EMA 20/50 cross | buy | MSTR | 4.94 | — | rebalance up |
| 2026-10-20T19:25 | EMA 20/50 cross | buy | BTC-USD | 4.94 | — | rebalance up |
| 2026-10-20T19:25 | EMA 20/50 cross | sell | SOL-USD | 6.14 | -0.03 | exit signal |
| 2026-10-20T19:25 | EMA 20/50 cross | sell | ETHU | 6.90 | -0.03 | exit signal |
| 2026-10-20T19:20 | MFI reversion · 1h | buy | UPRO | 2.36 | — | rebalance up |
| 2026-10-20T19:20 | MFI reversion · 1h | buy | COIN | 12.00 | — | entry |
| 2026-10-20T19:20 | MFI reversion · 1h | sell | QQQ | 4.80 | -0.01 | rebalance down |
| 2026-10-20T19:20 | MFI reversion · 1h | sell | META | 4.81 | -0.00 | rebalance down |
| 2026-10-20T19:20 | MFI reversion · 1h | sell | ETH-USD | 4.76 | -0.00 | rebalance down |
| 2026-10-20T19:20 | Keltner breakout | buy | LABU | 12.62 | — | entry |
| 2026-10-20T19:20 | EMA 20/50 cross | buy | XRP-USD | 2.86 | — | rebalance up |
| 2026-10-20T19:20 | EMA 20/50 cross | buy | SQQQ | 3.31 | — | rebalance up |
| 2026-10-20T19:20 | EMA 20/50 cross | sell | BITX | 6.20 | -0.00 | exit signal |
| 2026-10-20T19:15 | Agent (ML meta-label) | sell | QQQ | 7.34 | -0.01 | selected signal exited |
| 2026-10-20T19:05 | Agent (ML meta-label) | buy | QQQ | 7.35 | — | entry |
| 2026-10-20T19:05 | MFI reversion · 1h | buy | UPRO | 5.57 | — | entry |
| 2026-10-20T19:05 | EMA 20/50 cross | buy | ETHU | 3.01 | — | rebalance up |
| 2026-10-20T19:05 | EMA 20/50 cross | sell | PLTR | 6.19 | -0.02 | exit signal |
| 2026-10-20T19:00 | Day trade: Stocks in Play ORB | sell | LABU | 24.68 | -0.05 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 19:25:05.000143+00:00 -> 2026-10-20 19:35:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
