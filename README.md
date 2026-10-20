# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T12:25:05.000138+00:00 · 29497 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.38%)

Closed trades 86, win rate 39.5%, fees £2.89, max drawdown -9.99%.

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

Today: 8970 decisions in 1794 calls, $0.1256 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T12:25 | 2 / 3 / 0 | ETH-USD 18%, DOGE-USD 17% |  |
| Breezy | 2026-10-20T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T12:25 | 5 / 0 / 0 | ETH-USD 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.84 | +3.15% | 6 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.80 | 4.80 | 0 | — | 5.36 | 2.58 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.71 | -0.29 | 0 | — | 2.38 | 1.00 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 98.95 | -1.05 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.06 | 1.69 | -2.17 | 63 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.09 | -1.91 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -1.55 | -0.60 | -5.85 | 295 |
| 14 | Donchian 55/20 · 1h | breakout | 97.25 | -2.75 | 37 | 16.2 | -11.40 | -2.12 | -19.38 | 97 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.15 | -2.85 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.28 | -5.83 | 1 |
| 17 | Hold BTC | benchmark | 96.75 | -3.25 | 0 | — | 25.16 | 3.06 | -8.68 | 1 |
| 18 | Trend pullback · 1h | trend | 96.34 | -3.66 | 88 | 23.9 | -20.10 | -5.95 | -20.55 | 136 |
| 19 | Copy: Insider buying | copy | 96.25 | -3.75 | 23 | 43.5 | -11.55 | -1.97 | -20.62 | 70 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.19 | -3.81 | 0 | — | -5.86 | -2.32 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.23 | -4.77 | 8 | 37.5 | -20.05 | -1.69 | -34.64 | 26 |
| 23 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.54 | 2.17 | -6.51 | 199 |
| 24 | ADX DI cross · 1h | trend | 93.45 | -6.55 | 88 | 18.2 | -14.55 | -2.65 | -16.51 | 259 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 92.79 | -7.21 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 91.85 | -8.15 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.85 | -8.15 | 78 | 23.1 | -12.55 | -2.25 | -16.37 | 101 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.44 | -16.91 | 1 |
| 30 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.76 | -17.26 | 557 |
| 31 | Parabolic SAR · 1h | trend | 90.84 | -9.16 | 105 | 21.9 | -20.32 | -4.53 | -22.26 | 270 |
| 32 | Bollinger breakout · 1h | breakout | 90.74 | -9.26 | 84 | 28.6 | -9.11 | -1.54 | -16.89 | 253 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -14.95 | -5.33 | -20.44 | 280 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 89.90 | -10.10 | 0 | — | 0.78 | 0.28 | -14.37 | 1 |
| 35 | EMA 20/50 cross · 1h | trend | 89.90 | -10.10 | 60 | 13.3 | -19.31 | -3.46 | -21.31 | 128 |
| 36 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.57 | -23.86 | 205 |
| 37 | RSI momentum · 1h | momentum | 89.22 | -10.78 | 82 | 15.9 | -22.77 | -4.30 | -28.12 | 211 |
| 38 | Ichimoku · 1h | trend | 88.49 | -11.51 | 57 | 14.0 | -17.74 | -3.35 | -18.21 | 114 |
| 39 | Stochastic reversion · 1h | reversion | 88.11 | -11.89 | 152 | 46.1 | -17.11 | -2.96 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -14.91 | -3.38 | -22.27 | 136 |
| 41 | Keltner breakout · 1h | breakout | 87.67 | -12.33 | 56 | 23.2 | -15.89 | -2.57 | -26.96 | 201 |
| 42 | Supertrend · 1h | trend | 87.09 | -12.91 | 88 | 12.5 | -22.95 | -4.71 | -26.61 | 214 |
| 43 | Triple EMA stack · 1h | trend | 86.74 | -13.26 | 88 | 14.8 | -25.89 | -4.39 | -33.14 | 233 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.68 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 85.83 | -14.17 | 189 | 20.6 | -28.29 | -5.53 | -32.90 | 470 |
| 46 | OBV trend · 1h | momentum | 85.09 | -14.91 | 181 | 17.7 | -29.85 | -5.12 | -36.63 | 317 |
| 47 | Z-score reversion · 1h | reversion | 85.03 | -14.97 | 91 | 30.8 | -14.19 | -2.33 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.45 | -15.55 | 209 | 31.1 | -17.19 | -2.68 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.19 | -15.81 | 87 | 14.9 | -24.79 | -4.90 | -25.19 | 217 |
| 50 | Donchian 20/10 · 1h | breakout | 83.73 | -16.27 | 81 | 17.3 | -11.33 | -1.36 | -27.92 | 214 |
| 51 | Agent (ML meta-label) | meta | 83.67 | -16.33 | 681 | 18.8 | -9.84 | -1.67 | -15.61 | 375 |
| 52 | Bollinger reversion · 1h | reversion | 82.91 | -17.09 | 158 | 34.8 | -27.75 | -5.29 | -33.53 | 352 |
| 53 | Max aggression: 1-day momentum | meta | 82.39 | -17.61 | 15 | 33.3 | -15.83 | -0.59 | -37.31 | 42 |
| 54 | Three white soldiers | momentum | 81.85 | -18.15 | 235 | 18.7 | -47.40 | -18.57 | -47.87 | 602 |
| 55 | Williams %R · 1h | reversion | 81.83 | -18.17 | 182 | 42.9 | -33.28 | -5.29 | -36.50 | 532 |
| 56 | ROC + volume · 1h | momentum | 81.38 | -18.62 | 197 | 20.8 | -25.38 | -4.28 | -33.90 | 383 |
| 57 | CCI reversion · 1h | reversion | 80.50 | -19.50 | 163 | 39.3 | -17.93 | -2.24 | -27.44 | 443 |
| 58 | RSI(14) reversion · 1h | reversion | 79.98 | -20.02 | 75 | 21.3 | -20.45 | -3.64 | -25.21 | 170 |
| 59 | EMA 9/21 cross · 1h | trend | 79.36 | -20.64 | 139 | 10.8 | -29.93 | -6.23 | -30.06 | 316 |
| 60 | Heikin-Ashi · 1h | trend | 78.66 | -21.34 | 227 | 21.1 | -42.12 | -9.06 | -45.31 | 681 |
| 61 | VWAP momentum · 1h | momentum | 77.77 | -22.23 | 433 | 20.8 | -43.60 | -7.68 | -48.64 | 1248 |
| 62 | Candlestick reversal · 1h | reversion | 76.96 | -23.04 | 214 | 27.6 | -36.81 | -6.59 | -37.63 | 532 |
| 63 | ROC + volume | momentum | 61.28 | -38.72 | 599 | 22.2 | -75.77 | -16.89 | -78.28 | 1719 |
| 64 | Volume breakout | breakout | 61.11 | -38.89 | 362 | 13.0 | -62.24 | -16.66 | -64.36 | 864 |
| 65 | Squeeze breakout | breakout | 59.29 | -40.71 | 477 | 13.8 | -64.06 | -19.43 | -66.25 | 1205 |
| 66 | Donchian 55/20 | breakout | 57.90 | -42.10 | 484 | 18.2 | -70.06 | -16.70 | -73.31 | 1269 |
| 67 | RSI(14) reversion | reversion | 56.76 | -43.23 | 722 | 24.9 | -74.97 | -16.71 | -75.01 | 1606 |
| 68 | EMA 20/50 cross | trend | 55.60 | -44.40 | 522 | 19.5 | -77.47 | -16.43 | -80.70 | 1423 |
| 69 | VWAP reversion | reversion | 53.62 | -46.38 | 751 | 25.2 | -71.68 | -14.60 | -72.51 | 1496 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -28.56 | -98.72 | 5269 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.56 | -31.92 | -93.79 | 2564 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.85 | -20.88 | -88.34 | 1888 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.37 | -24.67 | -91.29 | 2347 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.02 | -25.70 | -91.17 | 2253 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.51 | -32.57 | -97.62 | 3493 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.72 | -36.55 | -96.82 | 3580 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.52 | -28.42 | -94.53 | 2501 |
| 78 | Keltner breakout | breakout | 50.32 | -49.68 | 679 | 16.1 | -82.28 | -23.15 | -83.76 | 1797 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.98 | -24.47 | -82.95 | 1684 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.12 | -99.38 | 5740 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.99 | -23.39 | -92.14 | 2621 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -31.17 | -95.92 | 3446 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -39.50 | -99.75 | 6188 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.66 | -29.36 | -91.66 | 2331 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.59 | -37.19 | -97.69 | 3618 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.40 | -98.49 | 4694 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.65 | -30.10 | -94.08 | 2791 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.99 | -99.53 | 6159 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.01 | -22.55 | -87.03 | 2143 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.91 | -26.65 | -87.99 | 2131 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -32.52 | -95.96 | 3751 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.93 | -31.97 | -89.26 | 2095 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.78 | -33.40 | -95.79 | 4105 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -42.41 | -99.90 | 8264 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T12:25 | Volume breakout | buy | ETH-USD | 15.30 | — | entry signal |
| 2026-10-20T12:25 | Volume breakout | buy | DOGE-USD | 15.30 | — | entry signal |
| 2026-10-20T12:25 | Squeeze breakout | buy | ETH-USD | 14.84 | — | entry signal |
| 2026-10-20T12:25 | Squeeze breakout | buy | DOGE-USD | 14.84 | — | entry signal |
| 2026-10-20T12:25 | Keltner breakout | buy | ETH-USD | 12.60 | — | entry signal |
| 2026-10-20T12:25 | Keltner breakout | buy | DOGE-USD | 12.60 | — | entry signal |
| 2026-10-20T12:25 | Donchian 55/20 | buy | SOL-USD | 14.51 | — | entry signal |
| 2026-10-20T12:25 | Donchian 55/20 | buy | ETH-USD | 14.51 | — | entry signal |
| 2026-10-20T12:25 | Donchian 55/20 | buy | DOGE-USD | 14.51 | — | entry signal |
| 2026-10-20T12:25 | EMA 20/50 cross | buy | DOGE-USD | 13.91 | — | entry signal |
| 2026-10-20T12:10 | Squeeze breakout | sell | XRP-USD | 14.76 | -0.11 | stop-loss |
| 2026-10-20T12:10 | Keltner breakout | sell | XRP-USD | 12.51 | -0.12 | stop-loss |
| 2026-10-20T12:10 | ROC + volume | sell | XRP-USD | 15.21 | -0.15 | stop-loss |
| 2026-10-20T12:00 | Ichimoku · 1h | sell | DOGE-USD | 22.05 | -0.10 | exit signal |
| 2026-10-20T12:00 | EMA 20/50 cross | buy | XRP-USD | 13.91 | — | entry signal |
| 2026-10-20T11:40 | Keltner breakout | buy | XRP-USD | 12.63 | — | entry signal |
| 2026-10-20T11:40 | ROC + volume | buy | XRP-USD | 15.36 | — | entry signal |
| 2026-10-20T11:30 | Squeeze breakout | buy | XRP-USD | 14.87 | — | entry signal |
| 2026-10-20T11:25 | Squeeze breakout | sell | DOGE-USD | 14.83 | -0.10 | target is flat |
| 2026-10-20T11:20 | Squeeze breakout | sell | SOL-USD | 14.80 | -0.13 | exit signal |
| 2026-10-20T11:10 | Volume breakout | sell | DOGE-USD | 15.24 | -0.08 | target is flat |
| 2026-10-20T11:05 | RSI(14) reversion | sell | DOGE-USD | 14.17 | -0.05 | exit signal |
| 2026-10-20T11:05 | Volume breakout | buy | DOGE-USD | 15.32 | — | entry signal |
| 2026-10-20T11:05 | Squeeze breakout | buy | SOL-USD | 14.93 | — | entry signal |
| 2026-10-20T11:05 | Squeeze breakout | buy | DOGE-USD | 14.93 | — | entry signal |
| 2026-10-20T11:00 | Bollinger reversion · 1h | buy | XRP-USD | 20.69 | — | entry signal |
| 2026-10-20T11:00 | Bollinger reversion · 1h | buy | ETH-USD | 20.69 | — | entry signal |
| 2026-10-20T11:00 | Ichimoku · 1h | buy | DOGE-USD | 22.15 | — | entry signal |
| 2026-10-20T10:20 | RSI(14) reversion | sell | ETH-USD | 14.21 | -0.07 | target is flat |
| 2026-10-20T10:15 | RSI(14) reversion | sell | BTC-USD | 14.19 | -0.06 | exit signal |
| 2026-10-20T10:00 | Bollinger reversion · 1h | buy | BTC-USD | 20.70 | — | entry signal |
| 2026-10-20T09:05 | RSI(14) reversion | sell | XRP-USD | 14.20 | -0.13 | stop-loss |
| 2026-10-20T09:00 | OBV trend · 1h | sell | SOL-USD | 12.64 | -0.17 | exit signal |
| 2026-10-20T09:00 | RSI momentum · 1h | sell | SOL-USD | 22.27 | -0.23 | exit signal |
| 2026-10-20T09:00 | Parabolic SAR · 1h | buy | XRP-USD | 17.80 | — | rebalance up |
| 2026-10-20T09:00 | Parabolic SAR · 1h | buy | ETH-USD | 4.70 | — | rebalance up |
| 2026-10-20T09:00 | Parabolic SAR · 1h | sell | BTC-USD | 22.50 | -0.34 | exit signal |
| 2026-10-20T09:00 | Triple EMA stack · 1h | sell | SOL-USD | 21.60 | -0.33 | exit signal |
| 2026-10-20T09:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 19.66 | -0.27 | exit signal |
| 2026-10-20T09:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 19.76 | -0.26 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 12:25:05.000138+00:00 -> 2026-10-20 12:35:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
