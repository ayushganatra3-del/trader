# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T14:53:05.000153+00:00 · 30797 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.65 (-9.35%)

Closed trades 91, win rate 40.7%, fees £3.00, max drawdown -9.99%.

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

Today: 15123 decisions in 2154 calls, $0.1993 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T14:53 | 3 / 16 / 11 | XRP-USD 15% |  |
| Breezy | 2026-10-21T14:53 | 0 / 30 / 0 | cash |  |
| Boozy | 2026-10-21T14:53 | 7 / 22 / 1 | MSTR 80% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.36 | 6.36 | 0 | — | 8.49 | 3.94 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Max aggression: 5-day momentum | meta | 105.10 | 5.10 | 10 | 50.0 | -4.06 | -0.04 | -34.64 | 26 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -0.43 | -0.03 | -8.92 | 26 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold BTC | benchmark | 99.58 | -0.42 | 0 | — | 15.94 | 2.28 | -8.68 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.45 | -0.55 | 4 | 50.0 | 7.37 | 1.60 | -7.93 | 8 |
| 11 | Hold SPY | benchmark | 99.14 | -0.86 | 0 | — | 0.61 | 0.40 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.78 | -1.22 | 63 | 34.9 | 2.11 | 1.25 | -2.29 | 64 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 98.68 | -1.32 | 0 | — | -0.34 | -0.06 | -5.02 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.37 | -1.92 | -5.83 | 1 |
| 16 | Copy: Insider buying | copy | 96.99 | -3.01 | 25 | 40.0 | -11.11 | -1.88 | -20.62 | 72 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.95 | -3.05 | 0 | — | 0.41 | 0.23 | -5.31 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.86 | -3.14 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 96.30 | -3.70 | 40 | 15.0 | -14.09 | -2.81 | -15.92 | 100 |
| 20 | Agent (rotation) | meta | 96.15 | -3.85 | 114 | 31.6 | -7.97 | -4.24 | -9.43 | 305 |
| 21 | ADX DI cross · 1h | trend | 95.87 | -4.13 | 90 | 18.9 | -11.79 | -1.99 | -17.66 | 256 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | Daily: Momentum burst | daily | 95.42 | -4.58 | 6 | 16.7 | -7.17 | -0.98 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 95.38 | -4.62 | 91 | 24.2 | -19.49 | -5.91 | -19.73 | 130 |
| 25 | Gap and go | momentum | 93.55 | -6.45 | 83 | 16.9 | 4.84 | 1.54 | -7.13 | 207 |
| 26 | Squeeze breakout · 1h | breakout | 93.43 | -6.58 | 46 | 21.7 | -2.71 | -0.58 | -11.48 | 100 |
| 27 | Parabolic SAR · 1h | trend | 93.26 | -6.74 | 108 | 23.1 | -15.75 | -3.38 | -19.76 | 272 |
| 28 | Opening range 30m | breakout | 92.63 | -7.37 | 225 | 32.4 | -11.73 | -3.40 | -17.26 | 562 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 92.45 | -7.55 | 0 | — | 1.94 | 0.46 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.37 | -7.63 | 87 | 29.9 | -10.72 | -1.93 | -16.62 | 257 |
| 31 | Daily: Bullish score | daily | 91.38 | -8.62 | 8 | 0.0 | -4.32 | -0.41 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.98 | -2.08 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 91.08 | -8.92 | 88 | 23.9 | -12.87 | -2.30 | -14.48 | 108 |
| 34 | Agent | meta | 90.65 | -9.35 | 91 | 40.7 | -13.55 | -7.13 | -14.84 | 248 |
| 35 | RSI momentum · 1h | momentum | 90.22 | -9.78 | 83 | 15.7 | -20.83 | -4.18 | -22.75 | 217 |
| 36 | Supertrend · 1h | trend | 89.94 | -10.06 | 88 | 12.5 | -21.31 | -4.17 | -26.73 | 221 |
| 37 | Connors RSI(2) · 1h | reversion | 89.89 | -10.11 | 157 | 42.0 | -21.65 | -6.40 | -23.42 | 196 |
| 38 | EMA 20/50 cross · 1h | trend | 89.37 | -10.63 | 62 | 12.9 | -20.25 | -3.57 | -23.33 | 135 |
| 39 | Stochastic reversion · 1h | reversion | 89.19 | -10.81 | 167 | 47.3 | -13.08 | -2.12 | -22.24 | 362 |
| 40 | Keltner breakout · 1h | breakout | 88.64 | -11.36 | 61 | 23.0 | -18.17 | -3.44 | -26.29 | 200 |
| 41 | Opening range 15m | breakout | 87.64 | -12.36 | 273 | 28.9 | -17.11 | -4.62 | -19.78 | 699 |
| 42 | Ichimoku · 1h | trend | 87.60 | -12.40 | 60 | 13.3 | -17.89 | -3.34 | -20.25 | 117 |
| 43 | Agent (aggressive) | meta | 87.59 | -12.41 | 45 | 35.6 | -13.05 | -3.87 | -14.78 | 121 |
| 44 | MACD cross · 1h | trend | 87.55 | -12.45 | 199 | 21.1 | -25.98 | -4.91 | -29.08 | 470 |
| 45 | Z-score reversion · 1h | reversion | 86.16 | -13.84 | 97 | 30.9 | -12.30 | -1.94 | -21.32 | 195 |
| 46 | Donchian 20/10 · 1h | breakout | 86.04 | -13.96 | 82 | 18.3 | -19.99 | -3.68 | -29.13 | 221 |
| 47 | Triple EMA stack · 1h | trend | 85.82 | -14.18 | 91 | 14.3 | -29.62 | -5.44 | -30.24 | 219 |
| 48 | MFI reversion · 1h | reversion | 85.14 | -14.86 | 227 | 32.6 | -14.43 | -2.17 | -21.11 | 139 |
| 49 | Agent (ML meta-label) | meta | 84.87 | -15.13 | 714 | 19.3 | -9.40 | -1.72 | -15.74 | 378 |
| 50 | MACD zero-line · 1h | trend | 84.79 | -15.21 | 92 | 15.2 | -24.78 | -4.70 | -27.64 | 219 |
| 51 | OBV trend · 1h | momentum | 84.33 | -15.67 | 188 | 17.6 | -30.56 | -5.72 | -31.73 | 312 |
| 52 | ROC + volume · 1h | momentum | 82.93 | -17.07 | 211 | 23.7 | -26.52 | -4.80 | -33.50 | 385 |
| 53 | Three white soldiers | momentum | 82.45 | -17.55 | 253 | 19.8 | -46.37 | -18.13 | -47.14 | 610 |
| 54 | Williams %R · 1h | reversion | 82.31 | -17.69 | 196 | 43.9 | -29.54 | -4.49 | -36.50 | 523 |
| 55 | Bollinger reversion · 1h | reversion | 82.27 | -17.73 | 162 | 35.8 | -29.38 | -5.69 | -32.85 | 347 |
| 56 | CCI reversion · 1h | reversion | 81.67 | -18.33 | 181 | 42.0 | -17.98 | -2.25 | -27.44 | 441 |
| 57 | Heikin-Ashi · 1h | trend | 81.57 | -18.43 | 235 | 20.9 | -43.60 | -9.42 | -46.90 | 673 |
| 58 | EMA 9/21 cross · 1h | trend | 81.15 | -18.85 | 143 | 10.5 | -27.46 | -5.47 | -29.92 | 326 |
| 59 | RSI(14) reversion · 1h | reversion | 80.89 | -19.11 | 84 | 23.8 | -16.73 | -3.00 | -23.42 | 173 |
| 60 | VWAP momentum · 1h | momentum | 78.72 | -21.28 | 471 | 21.0 | -45.43 | -8.25 | -51.84 | 1261 |
| 61 | Candlestick reversal · 1h | reversion | 78.56 | -21.44 | 227 | 29.1 | -33.67 | -5.70 | -37.07 | 543 |
| 62 | Max aggression: 1-day momentum | meta | 76.27 | -23.73 | 17 | 29.4 | -34.96 | -2.20 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.98 | -40.02 | 653 | 22.7 | -78.06 | -22.11 | -79.09 | 1727 |
| 64 | Volume breakout | breakout | 59.78 | -40.22 | 390 | 13.6 | -64.75 | -20.33 | -65.01 | 862 |
| 65 | RSI(14) reversion | reversion | 57.08 | -42.92 | 747 | 26.5 | -74.15 | -16.24 | -74.89 | 1611 |
| 66 | Squeeze breakout | breakout | 56.56 | -43.44 | 512 | 13.7 | -67.12 | -22.87 | -67.80 | 1219 |
| 67 | Donchian 55/20 | breakout | 56.40 | -43.60 | 521 | 18.6 | -71.77 | -18.66 | -74.04 | 1289 |
| 68 | EMA 20/50 cross | trend | 55.33 | -44.67 | 563 | 19.5 | -78.28 | -17.69 | -80.87 | 1453 |
| 69 | VWAP reversion | reversion | 53.91 | -46.09 | 758 | 25.3 | -71.07 | -14.29 | -72.15 | 1477 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.80 | -31.43 | -98.80 | 5338 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.92 | -33.38 | -94.23 | 2608 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.52 | -22.03 | -88.67 | 1905 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.95 | -26.29 | -91.71 | 2375 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.37 | -26.25 | -91.62 | 2274 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -34.17 | -97.77 | 3533 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -38.14 | -96.98 | 3620 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.50 | -27.96 | -94.69 | 2542 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.86 | -27.67 | -83.33 | 1733 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.07 | -99.38 | 5737 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.01 | -28.03 | -92.66 | 2634 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.95 | -31.63 | -95.97 | 3452 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.73 | -99.76 | 6195 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.74 | -29.63 | -91.89 | 2356 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -39.75 | -97.78 | 3622 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.31 | -98.48 | 4709 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.29 | -35.81 | -94.43 | 2812 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.71 | -28.48 | -84.44 | 1813 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.14 | -99.53 | 6176 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.19 | -87.01 | 2140 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.61 | -25.66 | -88.05 | 2141 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -32.76 | -95.93 | 3763 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.31 | -33.43 | -89.39 | 2108 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -33.41 | -95.76 | 4100 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.69 | -99.91 | 8307 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T14:50 | Agent (ML meta-label) | buy | AMZN | 2.80 | — | entry |
| 2026-10-21T14:50 | Agent (ML meta-label) | sell | IWM | 2.80 | 0.00 | selected signal exited |
| 2026-10-21T14:50 | Trend pullback · 1h | sell | BTC-USD | 24.20 | 0.27 | take-profit |
| 2026-10-21T14:50 | Three white soldiers | buy | COIN | 20.62 | — | entry signal |
| 2026-10-21T14:50 | Three white soldiers | sell | TECL | 20.68 | 0.09 | target is flat |
| 2026-10-21T14:50 | Opening range 30m | buy | TQQQ | 13.22 | — | entry signal |
| 2026-10-21T14:50 | Opening range 30m | buy | QQQ | 13.24 | — | entry signal |
| 2026-10-21T14:50 | Opening range 30m | buy | COIN | 13.24 | — | entry signal |
| 2026-10-21T14:50 | Opening range 30m | sell | PLTR | 9.76 | -0.01 | rebalance down |
| 2026-10-21T14:50 | Opening range 30m | sell | MSTR | 10.15 | 0.16 | rebalance down |
| 2026-10-21T14:50 | Opening range 30m | sell | ETHU | 9.87 | 0.03 | rebalance down |
| 2026-10-21T14:50 | Opening range 30m | sell | BITX | 9.91 | 0.05 | rebalance down |
| 2026-10-21T14:50 | Opening range 15m | buy | TQQQ | 2.64 | — | entry signal |
| 2026-10-21T14:50 | Opening range 15m | buy | QQQ | 10.96 | — | entry signal |
| 2026-10-21T14:50 | Opening range 15m | sell | META | 6.71 | 0.01 | rebalance down |
| 2026-10-21T14:50 | Opening range 15m | sell | BITX | 6.89 | 0.07 | rebalance down |
| 2026-10-21T14:50 | Donchian 55/20 | buy | MSTR | 1.95 | — | rebalance up |
| 2026-10-21T14:50 | Donchian 55/20 | buy | ETHU | 5.65 | — | entry signal |
| 2026-10-21T14:50 | Donchian 55/20 | buy | DOGE-USD | 5.65 | — | entry signal |
| 2026-10-21T14:50 | Donchian 55/20 | buy | COIN | 5.65 | — | entry signal |
| 2026-10-21T14:50 | Donchian 55/20 | sell | XRP-USD | 3.81 | 0.05 | rebalance down |
| 2026-10-21T14:50 | Donchian 55/20 | sell | PLTR | 3.76 | 0.02 | rebalance down |
| 2026-10-21T14:50 | Donchian 55/20 | sell | META | 3.70 | 0.01 | rebalance down |
| 2026-10-21T14:50 | Donchian 55/20 | sell | ETH-USD | 3.76 | 0.01 | rebalance down |
| 2026-10-21T14:50 | Donchian 55/20 | sell | BITX | 3.85 | 0.05 | rebalance down |
| 2026-10-21T14:50 | Gap and go | buy | TQQQ | 12.29 | — | entry signal |
| 2026-10-21T14:50 | Gap and go | buy | TNA | 15.60 | — | entry signal |
| 2026-10-21T14:50 | Gap and go | sell | MSTR | 7.97 | 0.12 | rebalance down |
| 2026-10-21T14:50 | Gap and go | sell | ETHU | 7.78 | 0.02 | rebalance down |
| 2026-10-21T14:50 | Gap and go | sell | COIN | 7.88 | 0.09 | rebalance down |
| 2026-10-21T14:50 | ROC + volume | buy | XRP-USD | 8.57 | — | entry signal |
| 2026-10-21T14:50 | ROC + volume | buy | ETH-USD | 8.58 | — | entry signal |
| 2026-10-21T14:50 | ROC + volume | buy | DOGE-USD | 8.58 | — | entry signal |
| 2026-10-21T14:50 | ROC + volume | sell | PLTR | 6.42 | 0.03 | rebalance down |
| 2026-10-21T14:50 | ROC + volume | sell | META | 6.44 | 0.03 | rebalance down |
| 2026-10-21T14:50 | ROC + volume | sell | ETHU | 6.41 | 0.02 | rebalance down |
| 2026-10-21T14:50 | ROC + volume | sell | BITX | 6.46 | 0.05 | rebalance down |
| 2026-10-21T14:45 | Opening range 30m | buy | ETHU | 23.04 | — | entry signal |
| 2026-10-21T14:45 | Opening range 15m | buy | ETHU | 8.24 | — | entry signal |
| 2026-10-21T14:45 | Opening range 15m | buy | COIN | 14.57 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 14:53:05.000153+00:00 -> 2026-10-21 15:03:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
