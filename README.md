# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T12:54:05.000150+00:00 · 29519 ticks

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

Today: 9300 decisions in 1860 calls, $0.1302 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T12:54 | 2 / 1 / 2 | cash |  |
| Breezy | 2026-10-20T12:54 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T12:54 | 2 / 3 / 0 | ETH-USD 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| VWAP reversion | BITX | 1.77 | +3.00% | 6 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.78 | 4.78 | 0 | — | 5.36 | 2.58 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.69 | -0.32 | 0 | — | 2.38 | 1.00 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 98.93 | -1.07 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.06 | 1.69 | -2.17 | 63 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.07 | -1.93 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -1.55 | -0.60 | -5.85 | 295 |
| 14 | Donchian 55/20 · 1h | breakout | 97.23 | -2.77 | 37 | 16.2 | -11.41 | -2.13 | -19.38 | 97 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.13 | -2.87 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.28 | -5.83 | 1 |
| 17 | Hold BTC | benchmark | 96.70 | -3.30 | 0 | — | 25.15 | 3.06 | -8.68 | 1 |
| 18 | Trend pullback · 1h | trend | 96.32 | -3.68 | 88 | 23.9 | -20.10 | -5.95 | -20.55 | 136 |
| 19 | Copy: Insider buying | copy | 96.24 | -3.76 | 23 | 43.5 | -11.54 | -1.97 | -20.62 | 70 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.17 | -3.83 | 0 | — | -5.86 | -2.32 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.21 | -4.79 | 8 | 37.5 | -20.05 | -1.69 | -34.64 | 26 |
| 23 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.55 | 2.17 | -6.51 | 199 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 25 | ADX DI cross · 1h | trend | 93.43 | -6.57 | 88 | 18.2 | -14.55 | -2.65 | -16.51 | 259 |
| 26 | Daily: Momentum burst | daily | 92.77 | -7.23 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Volume breakout · 1h | breakout | 91.84 | -8.16 | 78 | 23.1 | -12.57 | -2.25 | -16.37 | 102 |
| 28 | Daily: Bullish score | daily | 91.84 | -8.16 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.44 | -16.91 | 1 |
| 30 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.76 | -17.26 | 557 |
| 31 | Parabolic SAR · 1h | trend | 90.80 | -9.20 | 105 | 21.9 | -20.34 | -4.54 | -22.26 | 270 |
| 32 | Bollinger breakout · 1h | breakout | 90.73 | -9.27 | 84 | 28.6 | -9.07 | -1.53 | -16.89 | 253 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -12.05 | -4.12 | -19.60 | 277 |
| 34 | EMA 20/50 cross · 1h | trend | 89.89 | -10.11 | 60 | 13.3 | -19.31 | -3.46 | -21.31 | 128 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 89.89 | -10.11 | 0 | — | 0.78 | 0.28 | -14.37 | 1 |
| 36 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.57 | -23.86 | 205 |
| 37 | RSI momentum · 1h | momentum | 89.21 | -10.79 | 82 | 15.9 | -22.77 | -4.30 | -28.12 | 211 |
| 38 | Ichimoku · 1h | trend | 88.49 | -11.51 | 57 | 14.0 | -17.74 | -3.35 | -18.21 | 114 |
| 39 | Stochastic reversion · 1h | reversion | 88.09 | -11.91 | 152 | 46.1 | -17.12 | -2.96 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -13.99 | -2.99 | -21.45 | 149 |
| 41 | Keltner breakout · 1h | breakout | 87.67 | -12.33 | 56 | 23.2 | -15.82 | -2.55 | -26.96 | 200 |
| 42 | Supertrend · 1h | trend | 87.05 | -12.95 | 88 | 12.5 | -22.97 | -4.71 | -26.61 | 214 |
| 43 | Triple EMA stack · 1h | trend | 86.73 | -13.27 | 88 | 14.8 | -25.89 | -4.39 | -33.14 | 233 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.68 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 85.81 | -14.19 | 189 | 20.6 | -28.28 | -5.53 | -32.90 | 470 |
| 46 | OBV trend · 1h | momentum | 85.08 | -14.92 | 181 | 17.7 | -29.71 | -5.10 | -36.50 | 316 |
| 47 | Z-score reversion · 1h | reversion | 85.01 | -14.99 | 91 | 30.8 | -14.19 | -2.33 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.42 | -15.58 | 209 | 31.1 | -17.21 | -2.68 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.18 | -15.81 | 87 | 14.9 | -24.79 | -4.90 | -25.19 | 217 |
| 50 | Donchian 20/10 · 1h | breakout | 83.67 | -16.33 | 81 | 17.3 | -11.38 | -1.36 | -27.92 | 214 |
| 51 | Agent (ML meta-label) | meta | 83.66 | -16.34 | 681 | 18.8 | -9.91 | -1.79 | -15.56 | 361 |
| 52 | Bollinger reversion · 1h | reversion | 82.87 | -17.13 | 158 | 34.8 | -27.77 | -5.30 | -33.53 | 352 |
| 53 | Max aggression: 1-day momentum | meta | 82.38 | -17.62 | 15 | 33.3 | -15.83 | -0.59 | -37.31 | 42 |
| 54 | Three white soldiers | momentum | 81.85 | -18.15 | 235 | 18.7 | -47.67 | -19.24 | -48.14 | 606 |
| 55 | Williams %R · 1h | reversion | 81.82 | -18.18 | 182 | 42.9 | -33.29 | -5.29 | -36.49 | 532 |
| 56 | ROC + volume · 1h | momentum | 81.37 | -18.63 | 197 | 20.8 | -25.46 | -4.29 | -33.98 | 384 |
| 57 | CCI reversion · 1h | reversion | 80.49 | -19.51 | 163 | 39.3 | -17.94 | -2.24 | -27.44 | 443 |
| 58 | RSI(14) reversion · 1h | reversion | 79.96 | -20.04 | 75 | 21.3 | -20.45 | -3.64 | -25.21 | 170 |
| 59 | EMA 9/21 cross · 1h | trend | 79.35 | -20.65 | 139 | 10.8 | -29.93 | -6.23 | -30.06 | 316 |
| 60 | Heikin-Ashi · 1h | trend | 78.64 | -21.36 | 227 | 21.1 | -42.12 | -9.06 | -45.31 | 681 |
| 61 | VWAP momentum · 1h | momentum | 77.76 | -22.24 | 433 | 20.8 | -43.60 | -7.68 | -48.64 | 1248 |
| 62 | Candlestick reversal · 1h | reversion | 76.94 | -23.06 | 214 | 27.6 | -36.64 | -6.59 | -37.48 | 531 |
| 63 | ROC + volume | momentum | 61.28 | -38.72 | 599 | 22.2 | -75.82 | -17.05 | -78.28 | 1720 |
| 64 | Volume breakout | breakout | 61.09 | -38.91 | 362 | 13.0 | -62.25 | -16.67 | -64.41 | 864 |
| 65 | Squeeze breakout | breakout | 59.15 | -40.85 | 477 | 13.8 | -63.49 | -17.83 | -66.32 | 1210 |
| 66 | Donchian 55/20 | breakout | 57.81 | -42.19 | 484 | 18.2 | -70.10 | -16.72 | -73.38 | 1270 |
| 67 | RSI(14) reversion | reversion | 56.76 | -43.23 | 722 | 24.9 | -74.96 | -16.70 | -75.01 | 1610 |
| 68 | EMA 20/50 cross | trend | 55.48 | -44.52 | 522 | 19.5 | -77.51 | -16.45 | -80.74 | 1425 |
| 69 | VWAP reversion | reversion | 53.62 | -46.38 | 751 | 25.2 | -71.65 | -14.60 | -72.48 | 1494 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -28.69 | -98.74 | 5274 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.43 | -30.82 | -93.81 | 2565 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.87 | -20.91 | -88.36 | 1889 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.33 | -24.48 | -91.31 | 2346 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.00 | -25.65 | -91.17 | 2252 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.43 | -30.72 | -97.64 | 3496 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -36.23 | -96.81 | 3579 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.54 | -28.49 | -94.55 | 2503 |
| 78 | Keltner breakout | breakout | 50.30 | -49.70 | 679 | 16.1 | -82.42 | -23.86 | -83.79 | 1797 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.98 | -24.47 | -82.95 | 1684 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.16 | -99.38 | 5741 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.01 | -23.45 | -92.14 | 2622 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -31.17 | -95.92 | 3446 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -39.49 | -99.76 | 6188 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -29.39 | -91.67 | 2332 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -37.24 | -97.70 | 3620 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.40 | -98.49 | 4694 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.68 | -30.32 | -94.10 | 2793 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.99 | -99.53 | 6159 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.01 | -22.55 | -87.03 | 2143 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.99 | -26.58 | -88.06 | 2130 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -32.52 | -95.96 | 3751 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.86 | -31.57 | -89.26 | 2095 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.78 | -33.40 | -95.79 | 4105 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -42.44 | -99.90 | 8270 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T12:45 | Squeeze breakout | buy | SOL-USD | 14.83 | — | entry signal |
| 2026-10-20T12:45 | Squeeze breakout | buy | BTC-USD | 14.83 | — | entry signal |
| 2026-10-20T12:45 | Donchian 55/20 | buy | BTC-USD | 14.48 | — | entry signal |
| 2026-10-20T12:45 | EMA 20/50 cross | buy | ETH-USD | 13.90 | — | entry signal |
| 2026-10-20T12:40 | EMA 20/50 cross | buy | SOL-USD | 13.89 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 12:54:05.000150+00:00 -> 2026-10-20 13:04:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
