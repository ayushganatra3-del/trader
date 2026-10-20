# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T00:55:05.000137+00:00 · 28941 ticks

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

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 630 decisions in 126 calls, $0.0089 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T00:55 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-20T00:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T00:55 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |
| VWAP reversion | BITX | 1.65 | +2.78% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 105.03 | 5.03 | 0 | — | 5.36 | 2.58 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.93 | -0.07 | 0 | — | 2.38 | 1.00 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.17 | -0.83 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.30 | -1.70 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.14 | 1.74 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -2.17 | -0.80 | -5.10 | 289 |
| 14 | Donchian 55/20 · 1h | breakout | 97.38 | -2.62 | 37 | 16.2 | -12.88 | -2.46 | -18.86 | 101 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.36 | -2.63 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.28 | -5.83 | 1 |
| 17 | Hold BTC | benchmark | 96.94 | -3.06 | 0 | — | 26.29 | 3.12 | -8.68 | 1 |
| 18 | Trend pullback · 1h | trend | 96.50 | -3.50 | 88 | 23.9 | -19.69 | -5.79 | -20.58 | 137 |
| 19 | Copy: Insider buying | copy | 96.47 | -3.53 | 23 | 43.5 | -14.93 | -2.70 | -20.62 | 73 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.40 | -3.60 | 0 | — | -5.86 | -2.32 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.44 | -4.56 | 8 | 37.5 | -20.05 | -1.69 | -34.64 | 26 |
| 23 | ADX DI cross · 1h | trend | 93.65 | -6.35 | 88 | 18.2 | -14.55 | -2.65 | -16.51 | 259 |
| 24 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.49 | 2.15 | -6.54 | 200 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 92.94 | -7.06 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.02 | -7.98 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.90 | -8.10 | 78 | 23.1 | -12.51 | -2.22 | -16.76 | 107 |
| 29 | Parabolic SAR · 1h | trend | 91.51 | -8.49 | 102 | 22.5 | -14.57 | -2.77 | -24.71 | 269 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.44 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.76 | -17.26 | 557 |
| 32 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 84 | 28.6 | -8.66 | -1.45 | -16.89 | 256 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -13.33 | -6.12 | -18.67 | 278 |
| 34 | EMA 20/50 cross · 1h | trend | 90.33 | -9.67 | 59 | 13.6 | -19.11 | -3.41 | -21.31 | 126 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 90.10 | -9.90 | 0 | — | 0.78 | 0.28 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.75 | -10.25 | 79 | 16.5 | -20.13 | -3.41 | -30.20 | 212 |
| 37 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.57 | -23.86 | 205 |
| 38 | Ichimoku · 1h | trend | 88.63 | -11.37 | 55 | 14.5 | -17.60 | -3.32 | -18.08 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.30 | -11.70 | 152 | 46.1 | -17.11 | -2.96 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -18.58 | -4.39 | -23.50 | 140 |
| 41 | Keltner breakout · 1h | breakout | 87.72 | -12.28 | 56 | 23.2 | -11.96 | -1.67 | -26.96 | 201 |
| 42 | Triple EMA stack · 1h | trend | 87.43 | -12.57 | 85 | 15.3 | -23.53 | -3.64 | -32.98 | 232 |
| 43 | Supertrend · 1h | trend | 87.29 | -12.71 | 86 | 12.8 | -22.92 | -4.70 | -26.48 | 214 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.68 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 86.02 | -13.98 | 189 | 20.6 | -28.31 | -5.53 | -32.78 | 467 |
| 46 | OBV trend · 1h | momentum | 85.39 | -14.61 | 180 | 17.8 | -26.70 | -4.06 | -36.04 | 313 |
| 47 | Z-score reversion · 1h | reversion | 85.22 | -14.78 | 91 | 30.8 | -14.19 | -2.33 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.54 | -15.46 | 209 | 31.1 | -17.24 | -2.69 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.24 | -15.76 | 87 | 14.9 | -24.79 | -4.90 | -25.19 | 217 |
| 50 | Agent (ML meta-label) | meta | 83.86 | -16.14 | 681 | 18.8 | -10.30 | -1.83 | -17.19 | 357 |
| 51 | Donchian 20/10 · 1h | breakout | 83.78 | -16.23 | 81 | 17.3 | -8.27 | -0.86 | -27.92 | 214 |
| 52 | Bollinger reversion · 1h | reversion | 82.85 | -17.15 | 158 | 34.8 | -27.80 | -5.31 | -33.53 | 349 |
| 53 | Max aggression: 1-day momentum | meta | 82.57 | -17.43 | 15 | 33.3 | -15.83 | -0.59 | -37.31 | 42 |
| 54 | Three white soldiers | momentum | 82.22 | -17.78 | 233 | 18.9 | -47.64 | -19.20 | -48.02 | 608 |
| 55 | Williams %R · 1h | reversion | 82.01 | -17.98 | 182 | 42.9 | -33.29 | -5.29 | -36.49 | 531 |
| 56 | ROC + volume · 1h | momentum | 81.47 | -18.53 | 197 | 20.8 | -22.74 | -3.45 | -33.98 | 388 |
| 57 | CCI reversion · 1h | reversion | 80.68 | -19.32 | 163 | 39.3 | -17.92 | -2.24 | -27.44 | 442 |
| 58 | RSI(14) reversion · 1h | reversion | 80.15 | -19.85 | 75 | 21.3 | -20.45 | -3.64 | -25.21 | 170 |
| 59 | EMA 9/21 cross · 1h | trend | 80.04 | -19.96 | 135 | 11.1 | -29.44 | -6.11 | -29.60 | 315 |
| 60 | Heikin-Ashi · 1h | trend | 78.87 | -21.13 | 225 | 21.3 | -39.60 | -7.88 | -44.98 | 681 |
| 61 | VWAP momentum · 1h | momentum | 77.95 | -22.05 | 433 | 20.8 | -43.33 | -7.61 | -48.42 | 1245 |
| 62 | Candlestick reversal · 1h | reversion | 77.13 | -22.87 | 214 | 27.6 | -36.51 | -6.55 | -37.48 | 528 |
| 63 | ROC + volume | momentum | 61.62 | -38.38 | 596 | 22.3 | -76.10 | -17.84 | -78.25 | 1732 |
| 64 | Volume breakout | breakout | 61.28 | -38.72 | 361 | 13.0 | -62.77 | -17.79 | -64.33 | 878 |
| 65 | Squeeze breakout | breakout | 59.82 | -40.18 | 473 | 14.0 | -64.18 | -20.09 | -65.94 | 1207 |
| 66 | Donchian 55/20 | breakout | 58.58 | -41.42 | 480 | 18.3 | -68.25 | -13.71 | -73.07 | 1267 |
| 67 | RSI(14) reversion | reversion | 57.96 | -42.04 | 707 | 25.2 | -74.73 | -16.60 | -74.88 | 1603 |
| 68 | EMA 20/50 cross | trend | 56.34 | -43.66 | 517 | 19.7 | -75.24 | -13.55 | -80.44 | 1424 |
| 69 | VWAP reversion | reversion | 53.65 | -46.35 | 749 | 25.2 | -71.83 | -14.71 | -72.48 | 1497 |
| 70 | Keltner breakout | breakout | 50.62 | -49.38 | 677 | 16.1 | -82.54 | -24.73 | -83.66 | 1810 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -28.68 | -98.69 | 5272 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.09 | -27.66 | -93.73 | 2563 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -85.88 | -18.34 | -88.21 | 1889 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.80 | -22.10 | -91.16 | 2344 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.06 | -25.73 | -91.13 | 2262 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -30.33 | -97.57 | 3492 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.53 | -33.08 | -96.77 | 3576 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -27.78 | -94.58 | 2516 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.98 | -24.48 | -82.95 | 1695 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.76 | -99.37 | 5735 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.92 | -23.33 | -92.04 | 2622 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.08 | -31.26 | -96.08 | 3467 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -37.64 | -99.74 | 6185 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -29.25 | -91.67 | 2331 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -35.33 | -97.64 | 3628 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -35.98 | -98.45 | 4687 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.74 | -31.68 | -94.01 | 2802 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.44 | -99.52 | 6157 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.75 | -22.21 | -86.78 | 2132 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.87 | -26.40 | -87.88 | 2131 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.81 | -31.97 | -95.81 | 3736 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.92 | -31.96 | -89.09 | 2095 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -33.17 | -95.71 | 4099 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.75 | -99.90 | 8279 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T00:55 | EMA 20/50 cross | sell | SOL-USD | 11.30 | -0.06 | exit signal |
| 2026-10-20T00:46 | EMA 20/50 cross | sell | DOGE-USD | 11.30 | -0.08 | exit signal |
| 2026-10-20T00:40 | RSI(14) reversion | buy | BTC-USD | 14.52 | — | entry signal |
| 2026-10-20T00:30 | Donchian 55/20 · 1h | sell | BTC-USD | 24.38 | -0.32 | stop-loss |
| 2026-10-20T00:25 | RSI(14) reversion | buy | XRP-USD | 14.54 | — | entry signal |
| 2026-10-20T00:25 | RSI(14) reversion | buy | ETH-USD | 14.54 | — | entry signal |
| 2026-10-20T00:20 | EMA 20/50 cross · 1h | sell | BTC-USD | 18.21 | -0.26 | stop-loss |
| 2026-10-20T00:20 | EMA 20/50 cross | sell | ETH-USD | 14.05 | -0.14 | stop-loss |
| 2026-10-20T00:15 | Donchian 55/20 | sell | ETH-USD | 14.66 | -0.14 | stop-loss |
| 2026-10-20T00:15 | Donchian 55/20 | sell | DOGE-USD | 14.66 | -0.12 | target is flat |
| 2026-10-20T00:15 | EMA 20/50 cross | sell | XRP-USD | 14.07 | -0.14 | stop-loss |
| 2026-10-20T00:10 | Donchian 55/20 | sell | XRP-USD | 14.63 | -0.14 | stop-loss |
| 2026-10-20T00:10 | Donchian 55/20 | sell | SOL-USD | 11.74 | -0.08 | exit signal |
| 2026-10-20T00:01 | Heikin-Ashi · 1h | buy | DOGE-USD | 3.82 | — | entry |
| 2026-10-20T00:01 | Heikin-Ashi · 1h | sell | BTC-USD | 3.82 | -0.03 | exit signal |
| 2026-10-20T00:01 | Three white soldiers | sell | DOGE-USD | 20.45 | -0.14 | exit signal |
| 2026-10-19T23:46 | Three white soldiers | buy | DOGE-USD | 20.59 | — | entry signal |
| 2026-10-19T23:20 | Donchian 55/20 | buy | XRP-USD | 5.87 | — | rebalance up |
| 2026-10-19T23:20 | Donchian 55/20 | buy | ETH-USD | 2.96 | — | rebalance up |
| 2026-10-19T23:20 | Donchian 55/20 | buy | DOGE-USD | 2.96 | — | rebalance up |
| 2026-10-19T23:20 | Donchian 55/20 | sell | BTC-USD | 14.67 | -0.13 | stop-loss |
| 2026-10-19T23:20 | EMA 20/50 cross | buy | XRP-USD | 8.47 | — | rebalance up |
| 2026-10-19T23:20 | EMA 20/50 cross | sell | BTC-USD | 14.10 | -0.12 | stop-loss |
| 2026-10-19T23:10 | Squeeze breakout | sell | SOL-USD | 14.96 | -0.13 | stop-loss |
| 2026-10-19T23:10 | Keltner breakout | sell | SOL-USD | 10.12 | -0.09 | stop-loss |
| 2026-10-19T23:10 | ROC + volume | sell | SOL-USD | 15.34 | -0.14 | exit signal |
| 2026-10-19T23:00 | Heikin-Ashi · 1h | buy | BTC-USD | 3.85 | — | entry signal |
| 2026-10-19T23:00 | Parabolic SAR · 1h | buy | SOL-USD | 22.80 | — | entry signal |
| 2026-10-19T23:00 | Parabolic SAR · 1h | buy | DOGE-USD | 22.97 | — | entry signal |
| 2026-10-19T23:00 | Squeeze breakout | sell | DOGE-USD | 11.98 | -0.07 | stop-loss |
| 2026-10-19T23:00 | Keltner breakout | sell | DOGE-USD | 10.13 | -0.09 | stop-loss |
| 2026-10-19T23:00 | ROC + volume | sell | DOGE-USD | 15.32 | -0.16 | stop-loss |
| 2026-10-19T22:36 | Three white soldiers | sell | SOL-USD | 20.47 | -0.17 | exit signal |
| 2026-10-19T22:36 | Volume breakout | sell | SOL-USD | 15.29 | -0.09 | exit signal |
| 2026-10-19T22:36 | Volume breakout | sell | ETH-USD | 15.25 | -0.12 | exit signal |
| 2026-10-19T22:36 | Squeeze breakout | sell | ETH-USD | 14.95 | -0.11 | stop-loss |
| 2026-10-19T22:36 | Squeeze breakout | sell | BTC-USD | 14.95 | -0.10 | stop-loss |
| 2026-10-19T22:36 | Keltner breakout | sell | ETH-USD | 12.65 | -0.12 | stop-loss |
| 2026-10-19T22:36 | Keltner breakout | sell | BTC-USD | 10.14 | -0.08 | stop-loss |
| 2026-10-19T22:30 | Squeeze breakout | buy | BTC-USD | 12.00 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 00:55:05.000137+00:00 -> 2026-10-20 01:05:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
